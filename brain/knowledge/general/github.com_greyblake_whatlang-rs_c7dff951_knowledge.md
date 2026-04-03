---
id: github.com-greyblake-whatlang-rs-c7dff951-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:04.594980
---

# KNOWLEDGE EXTRACT: github.com_greyblake_whatlang-rs_c7dff951
> **Extracted on:** 2026-04-01 08:27:26
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519544/github.com_greyblake_whatlang-rs_c7dff951

---

## File: `.gitignore`
```
target
Cargo.lock
src/main.rs
```

## File: `CHANGELOG.md`
```markdown
### v0.18.0 - 2025-10-16
* [BREAKING] Update to Rust edition 2024

### v0.17.0 - 2025-10-16
* [BREAKING] Support Welsh
* Bump hashbrown to 15

### v0.16.4 - 2024-01-04
* Remove remove ahash 0.7.6 from dependencies (cargo audit)

### v0.16.3 - 2023-08-16
* Add `serde` feature (`Serialize` and `Deserialize` for `Lang` and `Script`).

### v0.16.2 - 2022-10-23
* Support [Arbitrary](https://crates.io/crates/arbitrary)

### v0.16.1 - 2022-08-30
* Fix bug in Czech alphabet (improved quality of Czech language detection)

### v0.16.0 - 2022-05-07
* [breaking] Add Armenian script (`Script::Armenian`) and language (`Lang::Hye`)

### v0.15.0 - 2022-05-01
* Update enum-map dependency to version 2
* Optimize alphabet method for Cyrillic: almost 2x improved performance for Cyrillic languages and 7% for the average `detect()` benchmark.

### v0.14.0 - 2022-04-15
* Improve performance of `detect()` almost twice ([see PR](https://github.com/greyblake/whatlang-rs/pull/108))

### v0.13.0 - 2022-01-02
* [breaking] - Support of Tagalog (`Tgl`)
* Rename `whatlang::Error` -> `whatlang::ParseError`

### v0.12.0 - 2021-04-18
* [breaking] - Drop languages:
  * Tigrinya (`Tir`)
  * Hausa (`Hau`)
  * Chewa (`Nya`)
  * Bhojpuri (`Bho`)
  * Igbo (`Ibo`)
  * Maithili (`Mai`)
  * Oromo (`Orm`)
  * Rundi (`Run`)
  * Saraiki (`Srk`)
  * Kurdish (`Kur`)
  * Cebuano (`Ceb`)
  * Malagasy (`Mlg`)
  * Kinyarwanda (`Kin`)
  * Somali (`Som`)
  * Ilocano (`Ilo`)
  * Uyghur (`Uig`)
  * Tagalog ('Tgl')
  * Haitian Creole (`Hat`)
  * Nynorsk (`Nno`)
  * Yoruba (`Yor`)
* [breaking] - Rename Yiddish: `Ydd` -> `Yid`
* [breaking] - Rename Azerbaijani: `Azj` -> `Aze`
* [breaking] Rename List -> FilterList
* [breaking] rename `whitelist` and `blacklist` to `allowlist` and `denylist` respectively
* Drop support of Cyrillic Azerbaijani and Turkmen
* Add `Script::all()` to iterate over all scripts.
* Add `Lang::all()` to iterate over all languages.
* Add integration with `enum-map`
* Implement `FromStr` for `Script` and `Lang`
* Implement `Script::langs(&self) -> &[Lang]`
* About 7% slower than v0.11.1 due to new detection method introduced. It's still much faster than v0.11.0

### v0.11.1 - 2020-11-28
* Use Trigram tuple instead of heap allocated String. (~68% faster)

### v0.11.0 - 2020-11-03
* [breaking] - rename code for Arabic: `Arb` -> `Ara`

### v0.10.0 - 2020-09-04
* Support Catalan

### v0.9.0 - 2020-06-26
* Support Slovak

### v0.8.0 - 2020-05-08
* Support Latin

### v0.7.4 - 2020-04-26 (yanked version)
* Support Latin

### v0.7.2 - 2019-10-19
* (fix) respect japanese whitelisting when mandarin characters are given (#44)

### v0.7.1 - 2019-05-06
* Update dependency hashbrown 0.1.8 -> 0.3.0 (10% faster)

### v0.7.0 - 2019-03-03
* Support Afrikaans language (afr)
* Get rid of build dependencies: installation is much faster now

### v0.6.0 - 2018-11-09
* Use hashbrown instead of fnv (detect() is 30% faster)
* Use array on stack instead of vector for detect_script (1-2% faster)
* Use build.rs to generate `lang.rs` file
* Add property based testing

### v0.5.0 - 2017-08-06
* (breaking) Rename `Lang::to_code(&self)` to `Lang::code(&self)`
* (fix) Fix bug with zero division in confidence calculation
* (fix) Confidence can not exceed 1.0
* Implement `Lang::eng_name(&self) -> &str` function
* Implement `Lang::name(&self) -> &str` function
* Implement `Script::name(&self) -> &str` function
* Implement trait `Dislpay` for `Script`
* Implement `Display` trait for `Lang`

### v0.4.1 - 2017-07-31
* Calculate confidence in the range from 0 to 1 for Info

### v0.4.0 - 2017-07-30
* Calculate is_reliable bool for `Info` struct.
* Breaking changes for `Info`. Make fields private. Now one should use methods.
* Remove support of Latin version of Serbo-Croatian, because it conflicts a lot with modern Croatian.

### v0.3.3 - 2017-07-26
* Replace HashMap with FnvHashMap (~ 33% faster)

### v0.3.2 - 2017-06-04
* Small performance improvement: preallocate memory for counter_hash in trigrams.rs (~ 2-3% faster)

### v0.3.1 - 2017-02-10
* Fix build
* Add link to doc at crates.io

### v0.3.0 - 2017-02-10
* Support New 14 languages
* (breaking) New API

### v0.2.1 - 2017-02-07
* Support 10 new languages
* Optimize trigram algorithms

### v0.2.0 - 2017-02-06
* Optimize script detection
* Accept text, blacklist and whitelist as references
* 10 new languages
* Fix: always guarantee same result on same input data (fix sorting issue)

### v0.1.4 - 2017-02-04
* Support whitelist and blacklist

### v0.1.3 - 2017-02-03
* Support more than 50 languages

### v0.1.2 - 2017-01-29
* Support about 20 languages

### v0.1.1 - 2016-12-25
* Tiny improvements

### v0.1.0 - 2016-12-25
* First public release
```

## File: `Cargo.toml`
```
[package]
name = "whatlang"
version = "0.18.0"
authors = ["Serhii Potapov <blake131313@gmail.com>"]
edition = "2024"
description = "Fast and lightweight language identification library for Rust."
keywords = ["language", "nlp", "lang", "whatlang", "text"]
license = "MIT"
repository = "https://github.com/greyblake/whatlang-rs"
homepage = "https://github.com/greyblake/whatlang-rs"
documentation = "https://docs.rs/whatlang"
readme = "README.md"
categories = ["text-processing", "algorithms"]
include = [
    "src/**/*",
    "test/**/*",
    "Cargo.toml",
    "README.md"
]

[dependencies]
hashbrown = "0.15"
enum-map = { version = "2", optional = true }
serde = { version = "1", optional = true, features = ["derive"] }
arbitrary = { version = "1", optional = true, features = ["derive"] }

[dev-dependencies]
serde_json = "1.0.39"
bencher = "0.1.5"
arbtest = "0.2"

[features]
dev = []

[[bench]]
name = "example"
harness = false
path = "benches/example.rs"
```

## File: `LICENSE`
```
(The MIT License)

Copyright (c) 2017 Sergey Potapov <blake131313@gmail.com>
Copyright (c) 2014 Titus Wormer <tituswormer@gmail.com>
Copyright (c) 2008 Kent S Johnson
Copyright (c) 2006 Jacob R Rideout <kde@jacobrideout.net>
Copyright (c) 2004 Maciej Ceglowski

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `Makefile`
```
watch:
	cargo watch -x test
watch-doc:
	cargo watch -s 'cargo doc --no-deps --all-features --document-private-items'
doc:
	cargo doc --no-deps --all-features --document-private-items --open
bench:
	cargo bench --all-features
test:
	cargo test --all-features
test-fuzz:
	ARBTEST_BUDGET_MS=6000000 cargo test --all-features --release
```

## File: `README.md`
```markdown
<p align="center"><img width="160" src="https://raw.githubusercontent.com/greyblake/whatlang-rs/master/misc/logo/whatlang-logo.svg" alt="Whatlang - rust library for natural language detection"></p>

<h1 align="center">Whatlang</h1>

<p align="center">Natural language detection for Rust with focus on simplicity and performance.</p>
<p align="center"><a href="https://whatlang.org/" target="_blank">Try online demo.</a></p>

<p align="center">
<a href="https://github.com/greyblake/whatlang-rs/actions/workflows/ci.yml" rel="nofollow"><img src="https://github.com/greyblake/whatlang-rs/actions/workflows/ci.yml/badge.svg" alt="Build Status"></a>
<a href="https://raw.githubusercontent.com/greyblake/whatlang-rs/master/LICENSE" rel="nofollow"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
<a href="https://docs.rs/whatlang" rel="nofollow"><img src="https://docs.rs/whatlang/badge.svg" alt="Documentation"></a>
<p>

[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://stand-with-ukraine.pp.ua/)

## Content
* [Features](#features)
* [Get started](#get-started)
* [Who uses Whatlang?](#who-uses-whatlang)
* [Documentation](https://docs.rs/whatlang)
* [Supported languages](https://github.com/greyblake/whatlang-rs/blob/master/SUPPORTED_LANGUAGES.md)
* [Feature toggles](#feature-toggles)
* [How does it work?](#how-does-it-work)
* [Make tasks](#make-tasks)
* [Comparison with alternatives](#comparison-with-alternatives)
* [Ports and clones](#ports-and-clones)
* [Donations](#donations)
* [Derivation](#derivation)
* [License](#license)
* [Contributors](#contributors)


## Features
* Supports [70 languages](https://github.com/greyblake/whatlang-rs/blob/master/SUPPORTED_LANGUAGES.md)
* 100% written in Rust
* Lightweight, fast and simple
* Recognizes not only a language, but also a script (Latin, Cyrillic, etc)
* Provides reliability information

## Get started

Example:

```rust
use whatlang::{detect, Lang, Script};

fn main() {
    let text = "Ĉu vi ne volas eklerni Esperanton? Bonvolu! Estas unu de la plej bonaj aferoj!";

    let info = detect(text).unwrap();
    assert_eq!(info.lang(), Lang::Epo);
    assert_eq!(info.script(), Script::Latin);
    assert_eq!(info.confidence(), 1.0);
    assert!(info.is_reliable());
}
```

For more details (e.g. how to blacklist some languages) please check the [documentation](https://docs.rs/whatlang).

## Who uses Whatlang?

Whatlang is used within the following big projects as direct or indirect dependency for language recognition.
You're gonna be in a great company using Whatlang:

* [Sonic](https://github.com/valeriansaliou/sonic) - fast, lightweight and schema-less search backend in Rust.
* [Meilisearch](https://github.com/meilisearch) - an open-source, easy-to-use, blazingly fast, and hyper-relevant search engine built in Rust.

## Feature toggles

| Feature     | Description                                                                           |
|-------------|---------------------------------------------------------------------------------------|
| `enum-map`  | `Lang` and `Script` implement `Enum` trait from [enum-map](https://docs.rs/enum-map/) |
| `arbitrary` | Support [Arbitrary](https://crates.io/crates/arbitrary)                               |
| `serde`     | Implements `Serialize` and `Deserialize` for `Lang` and `Script`                      |
| `dev`       | Enables `whatlang::dev` module which provides some internal API.<br/> It exists for profiling purposes and normal users are discouraged to to rely on this API.  |

## How does it work?

### How does the language recognition work?

The algorithm is based on the trigram language models, which is a particular case of n-grams.
To understand the idea, please check the original whitepaper [Cavnar and Trenkle '94: N-Gram-Based Text Categorization'](https://www.researchgate.net/publication/2375544_N-Gram-Based_Text_Categorization).

### How is `is_reliable` calculated?

It is based on the following factors:
* How many unique trigrams are in the given text
* How big is the difference between the first and the second(not returned) detected languages? This metric is called `rate` in the code base.

Therefore, it can be presented as 2d space with threshold functions, that splits it into "Reliable" and "Not reliable" areas.
This function is a hyperbola and it looks like the following one:

<img alt="Language recognition whatlang rust" src="https://raw.githubusercontent.com/greyblake/whatlang-rs/master/misc/images/whatlang_is_reliable.png" width="450" height="300" />

For more details, please check a blog article [Introduction to Rust Whatlang Library and Natural Language Identification Algorithms](https://www.greyblake.com/blog/introduction-to-rust-whatlang-library-and-natural-language-identification-algorithms/).

## Make tasks

* `make bench` - run performance benchmarks
* `make doc` - generate and open doc
* `make test` - run tests
* `make watch` - watch changes and run tests

## Comparison with alternatives

|                           | Whatlang   | CLD2        | CLD3           |
| ------------------------- | ---------- | ----------- | -------------- |
| Implementation language   | Rust       | C++         | C++            |
| Languages                 | 70         | 83          | 107            |
| Algorithm                 | trigrams   | quadgrams   | neural network |
| Supported Encoding        | UTF-8      | UTF-8       | ?              |
| HTML support              | no         | yes         | ?              |


## Ports and clones

* [whatlang-ffi](https://github.com/greyblake/whatlang-ffi) - C bindings
* [whatlanggo](https://github.com/abadojack/whatlanggo) - whatlang clone for Go language
* [whatlang-py](https://github.com/cathalgarvey/whatlang-py) - bindings for Python
* [whatlang-rb](https://gitlab.com/KitaitiMakoto/whatlang-rb) - bindings for Ruby
* [whatlangex](https://github.com/pierrelegall/whatlangex) - bindings for Elixir

## Donations

You can support the project by donating [NEAR tokens](https://near.org).

Our NEAR wallet address is `whatlang.near`

## Derivation

**Whatlang** is a derivative work from [Franc](https://github.com/wooorm/franc) (JavaScript, MIT) by [Titus Wormer](https://github.com/wooorm).

## License

[MIT](https://github.com/greyblake/whatlang-rs/blob/master/LICENSE) © [Sergey Potapov](http://greyblake.com/)


## Contributors

- [greyblake](https://github.com/greyblake) Potapov Sergey - creator, maintainer.
- [Dr-Emann](https://github.com/Dr-Emann) Zachary Dremann - optimization and improvements
- [BaptisteGelez](https://github.com/BaptisteGelez) Baptiste Gelez - improvements
- [Vishesh Chopra](https://github.com/KarmicKonquest) - designed the logo
- [Joel Natividad](https://github.com/jqnatividad) - support of Tagalog
- [ManyTheFish](https://github.com/ManyTheFish) - crazy optimization
- [Kerollmops](https://github.com/Kerollmops) Clément Renault - crazy optimization
```

## File: `SUPPORTED_LANGUAGES.md`
```markdown
# Whatlang

Natural language detection implemented in Rust.
Please check also [README](https://github.com/greyblake/whatlang-rs/blob/master/README.md)
and [documentation](https://docs.rs/whatlang/).

## Supported languages

| Language    | ISO 639-3 | Enum        |
| ----------- | --------- | ----------- |
| Esperanto   | epo       | `Lang::Epo` |
| English     | eng       | `Lang::Eng` |
| Russian     | rus       | `Lang::Rus` |
| Mandarin    | cmn       | `Lang::Cmn` |
| Spanish     | spa       | `Lang::Spa` |
| Portuguese  | por       | `Lang::Por` |
| Italian     | ita       | `Lang::Ita` |
| Bengali     | ben       | `Lang::Ben` |
| French      | fra       | `Lang::Fra` |
| German      | deu       | `Lang::Deu` |
| Ukrainian   | ukr       | `Lang::Ukr` |
| Georgian    | kat       | `Lang::Kat` |
| Arabic      | ara       | `Lang::Ara` |
| Hindi       | hin       | `Lang::Hin` |
| Japanese    | jpn       | `Lang::Jpn` |
| Hebrew      | heb       | `Lang::Heb` |
| Yiddish     | yid       | `Lang::Yid` |
| Polish      | pol       | `Lang::Pol` |
| Amharic     | amh       | `Lang::Amh` |
| Javanese    | jav       | `Lang::Jav` |
| Korean      | kor       | `Lang::Kor` |
| Bokmal      | nob       | `Lang::Nob` |
| Danish      | dan       | `Lang::Dan` |
| Swedish     | swe       | `Lang::Swe` |
| Finnish     | fin       | `Lang::Fin` |
| Turkish     | tur       | `Lang::Tur` |
| Dutch       | nld       | `Lang::Nld` |
| Hungarian   | hun       | `Lang::Hun` |
| Czech       | ces       | `Lang::Ces` |
| Greek       | ell       | `Lang::Ell` |
| Bulgarian   | bul       | `Lang::Bul` |
| Belarusian  | bel       | `Lang::Bel` |
| Marathi     | mar       | `Lang::Mar` |
| Kannada     | kan       | `Lang::Kan` |
| Romanian    | ron       | `Lang::Ron` |
| Slovene     | slv       | `Lang::Slv` |
| Croatian    | hrv       | `Lang::Hrv` |
| Serbian     | srp       | `Lang::Srp` |
| Macedonian  | mkd       | `Lang::Mkd` |
| Lithuanian  | lit       | `Lang::Lit` |
| Latvian     | lav       | `Lang::Lav` |
| Estonian    | est       | `Lang::Est` |
| Tamil       | tam       | `Lang::Tam` |
| Vietnamese  | vie       | `Lang::Vie` |
| Urdu        | urd       | `Lang::Urd` |
| Thai        | tha       | `Lang::Tha` |
| Gujarati    | guj       | `Lang::Guj` |
| Uzbek       | uzb       | `Lang::Uzb` |
| Punjabi     | pan       | `Lang::Pan` |
| Azerbaijani | aze       | `Lang::Aze` |
| Indonesian  | ind       | `Lang::Ind` |
| Telugu      | tel       | `Lang::Tel` |
| Persian     | pes       | `Lang::Pes` |
| Malayalam   | mal       | `Lang::Mal` |
| Oriya       | ori       | `Lang::Ori` |
| Burmese     | mya       | `Lang::Mya` |
| Nepali      | nep       | `Lang::Nep` |
| Sinhalese   | sin       | `Lang::Sin` |
| Khmer       | khm       | `Lang::Khm` |
| Turkmen     | tuk       | `Lang::Tuk` |
| Akan        | aka       | `Lang::Aka` |
| Zulu        | zul       | `Lang::Zul` |
| Shona       | sna       | `Lang::Sna` |
| Afrikaans   | afr       | `Lang::Afr` |
| Latin       | lat       | `Lang::Lat` |
| Slovak      | slk       | `Lang::Slk` |
| Catalan     | cat       | `Lang::Cat` |
| Tagalog     | tgl       | `Lang::Tgl` |
| Armenian    | hye       | `Lang::Hye` |
| Welsh       | cym       | `Lang::Cym` |
```

## File: `benches/example.rs`
```rust
#[macro_use]
extern crate bencher;

use bencher::Bencher;
use std::collections::HashMap;
use whatlang::dev::{
    FilterList, LowercaseText, alphabet_cyrillic_calculate_scores, alphabet_latin_calculate_scores,
};
use whatlang::{detect, detect_script};

fn bench_detect(bench: &mut Bencher) {
    let example_data = include_str!("../tests/examples.json");
    let examples: HashMap<String, String> = serde_json::from_str(example_data).unwrap();

    bench.iter(|| {
        for text in examples.values() {
            detect(text);
        }
    })
}

fn bench_detect_script(bench: &mut Bencher) {
    let example_data = include_str!("../tests/examples.json");
    let examples: HashMap<String, String> = serde_json::from_str(example_data).unwrap();

    bench.iter(|| {
        for text in examples.values() {
            detect_script(text);
        }
    })
}

fn bench_alphabet_latin_calculate_scores(bench: &mut Bencher) {
    let text = "Ich sehe auf die Uhr. Es ist kurz vor Mittag, und da heute Sonnabend ist, mache ich Schluß. Por ke lingvo internacia povu bone kaj regule progresadi kaj por ke ĝi havu plenan certecon, ke ĝi neniam disfalos kaj ia facilanima paŝo de ĝiaj amikoj estontaj ne detruos la laborojn de ĝiaj amikoj estintaj, - estas plej necesa antaŭ ĉio unu kondiĉo: la ezistado de klare difinita, neniam tuŝebla kaj neniam ŝangebla Fundamento de la lingvo.";
    let lowercase_text = LowercaseText::new(text);
    let filter = FilterList::All;

    bench.iter(|| {
        alphabet_latin_calculate_scores(&lowercase_text, &filter);
    })
}

fn bench_alphabet_cyrillic_calculate_scores(bench: &mut Bencher) {
    let text = "Творець есперанто Людвік Заменгоф назвав свою мову просто Lingvo internacia «міжнародна мова». Оскільки на той час у Європі популярною була інша штучна мова — волапюк, прихильники есперанто часто казали «мова доктора Есперанто». Згодом це формулювання скоротилося до «мова Есперанто», а врешті-решт залишилося одне лише слово «Esperanto», яке есперантською пишуть з великої літери, аби його можна було відрізнити від слова «людина, яка сподівається»";
    let lowercase_text = LowercaseText::new(text);
    let filter = FilterList::All;

    bench.iter(|| {
        alphabet_cyrillic_calculate_scores(&lowercase_text, &filter);
    })
}

benchmark_group!(
    benches,
    bench_detect,
    bench_detect_script,
    bench_alphabet_latin_calculate_scores,
    bench_alphabet_cyrillic_calculate_scores,
);
benchmark_main!(benches);
```

## File: `docs/index.html`
```html
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link href='https://fonts.googleapis.com/css?family=Architects+Daughter' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="http://greyblake.com/blablabla/assets/css/style.css?v=e9b1cf394c8decca13410c03ce9153d6ee8234af" media="screen" type="text/css">
    <link rel="stylesheet" href="http://greyblake.com/blablabla/assets/css/print.css" media="print" type="text/css">

    <!--[if lt IE 9]>
    <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

<!-- Begin Jekyll SEO tag v2.3.0 -->
<title>Whatlang - natural language detection for Rust</title>
<meta property="og:title" content="Whatlang - natural language detection for Rust" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="Natural language detection for Rust with focus on simplicity and performance." />
<meta property="og:description" content="Natural language detection for Rust with focus on simplicity and performance." />
<link rel="canonical" href="http://greyblake.com/whatlang-rs/" />
<meta property="og:url" content="http://greyblake.com/whatlang-rs/" />
<meta property="og:site_name" content="Whatlang demo" />
<script type="application/ld+json">
{"name":"Whatlang","description":"Natural language detection for Rust with focus on simplicity and performance.","author":null,"@type":"WebSite","url":"http://greyblake.com/whatlang-rs/","image":null,"publisher":null,"headline":"Hello Bla","dateModified":null,"datePublished":null,"sameAs":null,"mainEntityOfPage":null,"@context":"http://schema.org"}</script>
<!-- End Jekyll SEO tag -->

  </head>

  <body>
    <header>
      <div class="inner">
        <a href="http://greyblake.com/whatlang-rs/">
          <h1>Whatlang-rs</h1>
        </a>
        <h2>Natural language detection for Rust</h2>

          <a href="https://github.com/greyblake/whatlang-rs" class="button"><small>View project on</small> GitHub</a>


      </div>
    </header>

    <div id="content-wrapper">
      <div class="inner clearfix">
        <section id="main-content">

        <div class="form">
            <textarea id="input" cols="80", rows="10">Type something here to see whatlang in action =)</textarea>
        </div>


        Language: <span id="lang-name"></span>
        <br>
        Script: <span id="script-name"></span>
        <br>
        Confidence: <span id="confidence"></span>
        <br>
        Is reliable: <span id="isReliable"></span>


        </section>

        <aside id="sidebar">



            <p class="repo-owner"><a href="https://github.com/greyblake/whatlang-rs">whatlang-rs</a> is maintained by <a href="https://github.com/greyblake">Sergey Potapov</a>.</p>


        </aside>
      </div>
    </div>

        <script src="whatlang-demo.js"></script>
        <script>

            Rust.whatlang_demo.then( function(demo) {
                function setInfo(info) {
                    var langName = document.getElementById("lang-name");
                    var scriptName = document.getElementById("script-name");
                    var confidence = document.getElementById("confidence");
                    var isReliable = document.getElementById("isReliable");

                    if(info) {
                        langName.innerText = info.lang_eng_name;
                        scriptName.innerText = info.script_name;
                        confidence.innerText = info.confidence;
                        isReliable.innerText = info.is_reliable;
                    } else {
                        langName.innerText = "None";
                        scriptName.innerText = "";
                        confidence.innerText = "";
                        isReliable.innerText = "";
                    }
                }

                function react() {
                    var input = document.getElementById( "input" );
                    var info = demo.detect(input.value);
                    setInfo(info);
                }

                react();
                input.addEventListener("keyup", function( event ) {
                    react();
                });
            });
        </script>

  </body>
</html>
```

## File: `docs/whatlang-demo.js`
```javascript
"use strict";

if( typeof Rust === 'undefined' ) {
    var Rust = {};
}

(function( root, factory ) {
    if( typeof define === "function" && define.amd ) {
        define( [], factory );
    } else if( typeof module === "object" && module.exports ) {
        module.exports = factory();
    } else {
        factory();
    }
}( this, function() {
    const Module = {};
    let HEAP8 = null;
    let HEAP16 = null;
    let HEAP32 = null;
    let HEAPU8 = null;
    let HEAPU16 = null;
    let HEAPU32 = null;
    let HEAPF32 = null;
    let HEAPF64 = null;

    Object.defineProperty( Module, 'nodejs', { value: (typeof window === 'undefined') } );
    Object.defineProperty( Module, 'exports', { value: {} } );

    const __imports = {
        env: {
            "__extjs_ff2c75b4783fd5c9d8c934bbd4a03e66527e05e4": function($0) {
                Module.STDWEB.tmp = Module.STDWEB.to_js( $0 );
            },
            "__extjs_de942ef9ccd064c41dc92d5b5bf83c61aeb00278": function($0) {
                Module.STDWEB.increment_refcount( $0 );
            },
            "__extjs_d8a439451216bbc6cd9f3012f189d2ad6a2e9459": function($0) {
                Module.STDWEB.decrement_refcount( $0 );
            },
            "__extjs_dcc28a1d067f81d96c559505e230eaec847de188": function($0, $1) {
                Module.STDWEB.from_js($0, (function(){Module.exports.detect = Module.STDWEB.to_js($1);})());
            },
            "__extjs_d0f9580b9cfe82e2ee67d3707e52d87bbabe59f2": function() {
                Module.STDWEB = {};
            },
            "__extjs_4985c7263834081d123cc7eff225fe2010747092": function() {
                Module.STDWEB.alloc = Module.web_malloc ; Module.STDWEB.dyncall = function (signature , ptr , args){return Module.web_table.get (ptr). apply (null , args);}; Module.STDWEB.utf8_len = function utf8_len (str){let len = 0 ; for (let i = 0 ; i < str.length ; ++i){let u = str.charCodeAt (i); if (u >= 0xD800 && u <= 0xDFFF){u = 0x10000 + ((u & 0x3FF)<< 10)| (str.charCodeAt (++i)& 0x3FF);}if (u <= 0x7F){++len ;}else if (u <= 0x7FF){len += 2 ;}else if (u <= 0xFFFF){len += 3 ;}else if (u <= 0x1FFFFF){len += 4 ;}else if (u <= 0x3FFFFFF){len += 5 ;}else {len += 6 ;}}return len ;};
            },
            "__extjs_a986a787f7d7d1abc8c97008ceb5c6945d3f620f": function() {
                Module.STDWEB.to_utf8 = function to_utf8 (str , addr){for (var i = 0 ; i < str.length ; ++i){var u = str.charCodeAt (i); if (u >= 0xD800 && u <= 0xDFFF){u = 0x10000 + ((u & 0x3FF)<< 10)| (str.charCodeAt (++i)& 0x3FF);}if (u <= 0x7F){HEAPU8 [addr ++]= u ;}else if (u <= 0x7FF){HEAPU8 [addr ++]= 0xC0 | (u >> 6); HEAPU8 [addr ++]= 0x80 | (u & 63);}else if (u <= 0xFFFF){HEAPU8 [addr ++]= 0xE0 | (u >> 12); HEAPU8 [addr ++]= 0x80 | ((u >> 6)& 63); HEAPU8 [addr ++]= 0x80 | (u & 63);}else if (u <= 0x1FFFFF){HEAPU8 [addr ++]= 0xF0 | (u >> 18); HEAPU8 [addr ++]= 0x80 | ((u >> 12)& 63); HEAPU8 [addr ++]= 0x80 | ((u >> 6)& 63); HEAPU8 [addr ++]= 0x80 | (u & 63);}else if (u <= 0x3FFFFFF){HEAPU8 [addr ++]= 0xF8 | (u >> 24); HEAPU8 [addr ++]= 0x80 | ((u >> 18)& 63); HEAPU8 [addr ++]= 0x80 | ((u >> 12)& 63); HEAPU8 [addr ++]= 0x80 | ((u >> 6)& 63); HEAPU8 [addr ++]= 0x80 | (u & 63);}else {HEAPU8 [addr ++]= 0xFC | (u >> 30); HEAPU8 [addr ++]= 0x80 | ((u >> 24)& 63); HEAPU8 [addr ++]= 0x80 | ((u >> 18)& 63); HEAPU8 [addr ++]= 0x80 | ((u >> 12)& 63); HEAPU8 [addr ++]= 0x80 | ((u >> 6)& 63); HEAPU8 [addr ++]= 0x80 | (u & 63);}}};
            },
            "__extjs_da4d8e153d6e312a947afb9d256a49eaf1c1648e": function() {
                Module.STDWEB.to_js = function to_js (address){var kind = HEAPU8 [address + 12]; if (kind ===0){return undefined ;}else if (kind ===1){return null ;}else if (kind ===2){return HEAP32 [address / 4];}else if (kind ===3){return HEAPF64 [address / 8];}else if (kind ===4){var pointer = HEAPU32 [address / 4]; var length = HEAPU32 [(address + 4)/ 4]; return Module.STDWEB.to_js_string (pointer , length);}else if (kind ===5){return false ;}else if (kind ===6){return true ;}else if (kind ===7){var pointer = HEAPU32 [address / 4]; var length = HEAPU32 [(address + 4)/ 4]; var output = []; for (var i = 0 ; i < length ; ++i){output.push (Module.STDWEB.to_js (pointer + i * 16));}return output ;}else if (kind ===8){var value_array_pointer = HEAPU32 [address / 4]; var length = HEAPU32 [(address + 4)/ 4]; var key_array_pointer = HEAPU32 [(address + 8)/ 4]; var output = {}; for (var i = 0 ; i < length ; ++i){var key_pointer = HEAPU32 [(key_array_pointer + i * 8)/ 4]; var key_length = HEAPU32 [(key_array_pointer + 4 + i * 8)/ 4]; var key = Module.STDWEB.to_js_string (key_pointer , key_length); var value = Module.STDWEB.to_js (value_array_pointer + i * 16); output [key]= value ;}return output ;}else if (kind ===9 || kind == 11 || kind == 12){return Module.STDWEB.acquire_js_reference (HEAP32 [address / 4]);}else if (kind ===10){var adapter_pointer = HEAPU32 [address / 4]; var pointer = HEAPU32 [(address + 4)/ 4]; var deallocator_pointer = HEAPU32 [(address + 8)/ 4]; var output = function (){var args = Module.STDWEB.alloc (16); Module.STDWEB.serialize_array (args , arguments); Module.STDWEB.dyncall ("vii" , adapter_pointer , [pointer , args]); var result = Module.STDWEB.tmp ; Module.STDWEB.tmp = null ; return result ;}; output.drop = function (){output.drop = null ; Module.STDWEB.dyncall ("vi" , deallocator_pointer , [pointer]);}; return output ;}};
            },
            "__extjs_2171fbf7dcd6cce3ad90767662e531aee9577813": function() {
                Module.STDWEB.serialize_object = function serialize_object (address , value){var keys = Object.keys (value); var length = keys.length ; var key_array_pointer = Module.STDWEB.alloc (length * 8); var value_array_pointer = Module.STDWEB.alloc (length * 16); HEAPU8 [address + 12]= 8 ; HEAPU32 [address / 4]= value_array_pointer ; HEAPU32 [(address + 4)/ 4]= length ; HEAPU32 [(address + 8)/ 4]= key_array_pointer ; for (var i = 0 ; i < length ; ++i){var key = keys [i]; var key_length = Module.STDWEB.utf8_len (key); var key_pointer = Module.STDWEB.alloc (key_length); Module.STDWEB.to_utf8 (key , key_pointer); var key_address = key_array_pointer + i * 8 ; HEAPU32 [key_address / 4]= key_pointer ; HEAPU32 [(key_address + 4)/ 4]= key_length ; Module.STDWEB.from_js (value_array_pointer + i * 16 , value [key]);}}; Module.STDWEB.serialize_array = function serialize_array (address , value){var length = value.length ; var pointer = Module.STDWEB.alloc (length * 16); HEAPU8 [address + 12]= 7 ; HEAPU32 [address / 4]= pointer ; HEAPU32 [(address + 4)/ 4]= length ; for (var i = 0 ; i < length ; ++i){Module.STDWEB.from_js (pointer + i * 16 , value [i]);}}; Module.STDWEB.from_js = function from_js (address , value){var kind = Object.prototype.toString.call (value); if (kind ==="[object String]"){var length = Module.STDWEB.utf8_len (value); var pointer = 0 ; if (length > 0){pointer = Module.STDWEB.alloc (length); Module.STDWEB.to_utf8 (value , pointer);}HEAPU8 [address + 12]= 4 ; HEAPU32 [address / 4]= pointer ; HEAPU32 [(address + 4)/ 4]= length ;}else if (kind ==="[object Number]"){if (value ===(value | 0)){HEAPU8 [address + 12]= 2 ; HEAP32 [address / 4]= value ;}else {HEAPU8 [address + 12]= 3 ; HEAPF64 [address / 8]= value ;}}else if (value ===null){HEAPU8 [address + 12]= 1 ;}else if (value ===undefined){HEAPU8 [address + 12]= 0 ;}else if (value ===false){HEAPU8 [address + 12]= 5 ;}else if (value ===true){HEAPU8 [address + 12]= 6 ;}else {var refid = Module.STDWEB.acquire_rust_reference (value); var id = 9 ; if (kind ==="[object Object]"){id = 11 ;}else if (kind ==="[object Array]" || kind ==="[object Arguments]"){id = 12 ;}HEAPU8 [address + 12]= id ; HEAP32 [address / 4]= refid ;}};
            },
            "__extjs_8a13e041b26592fd43280496ac01f5f3e049218e": function() {
                Module.STDWEB.to_js_string = function to_js_string (index , length){index = index | 0 ; length = length | 0 ; var end = (index | 0)+ (length | 0); var output = "" ; while (index < end){var x = HEAPU8 [index ++]; if (x < 128){output += String.fromCharCode (x); continue ;}var init = (x & (0x7F >> 2)); var y = 0 ; if (index < end){y = HEAPU8 [index ++];}var ch = (init << 6)| (y & 63); if (x >= 0xE0){var z = 0 ; if (index < end){z = HEAPU8 [index ++];}var y_z = ((y & 63)<< 6)| (z & 63); ch = init << 12 | y_z ; if (x >= 0xF0){var w = 0 ; if (index < end){w = HEAPU8 [index ++];}ch = (init & 7)<< 18 | ((y_z << 6)| (w & 63));}}output += String.fromCharCode (ch); continue ;}return output ;};
            },
            "__extjs_b67f2836bfcab57acb8e21dbe580790ff03192f9": function() {
                var id_to_ref_map = {}; var id_to_refcount_map = {}; var ref_to_id_map = new WeakMap (); var ref_to_id_symbol_map = {}; var last_refid = 1 ; Module.STDWEB.acquire_rust_reference = function (reference){if (reference ===undefined || reference ===null){return 0 ;}var refid = ref_to_id_map.get (reference); if (refid ===undefined){refid = ref_to_id_symbol_map [reference];}if (refid ===undefined){refid = last_refid ++; if (typeof reference ==="symbol"){ref_to_id_symbol_map [reference]= refid ;}else {ref_to_id_map.set (reference , refid);}id_to_ref_map [refid]= reference ; id_to_refcount_map [refid]= 1 ;}else {id_to_refcount_map [refid]++;}return refid ;}; Module.STDWEB.acquire_js_reference = function (refid){return id_to_ref_map [refid];}; Module.STDWEB.increment_refcount = function (refid){id_to_refcount_map [refid]++;}; Module.STDWEB.decrement_refcount = function (refid){id_to_refcount_map [refid]--; if (id_to_refcount_map [refid]===0){var reference = id_to_ref_map [refid]; delete id_to_ref_map [refid]; delete id_to_refcount_map [refid]; if (typeof reference ==="symbol"){delete ref_to_id_symbol_map [reference];}else {ref_to_id_map.delete (reference);}}};
            },
            "__extjs_dc2fd915bd92f9e9c6a3bd15174f1414eee3dbaf": function() {
                console.error( 'Encountered a panic!' );
            },
            "__extjs_b00b05929b445348eab177b6d3f509bcaa28782e": function($0, $1) {
                console.error( 'Panic error message:', Module.STDWEB.to_js_string( $0, $1 ) );
            },
            "__extjs_20637d8f642203b38c263a5d0f43b9d88ec67c31": function($0, $1, $2) {
                console.error( 'Panic location:', Module.STDWEB.to_js_string( $0, $1 ) + ':' + $2 );
            },
            "__extjs_2cb8f8b2763d8d6a8b8ac2ab55fce29a7fe32f32": function($0, $1) {
                Module.STDWEB.from_js($0, (function(){return Module.STDWEB.to_js($1);})());
            },
            "__web_on_grow": function() {
                const buffer = Module.instance.exports.memory.buffer;
                HEAP8 = new Int8Array( buffer );
                HEAP16 = new Int16Array( buffer );
                HEAP32 = new Int32Array( buffer );
                HEAPU8 = new Uint8Array( buffer );
                HEAPU16 = new Uint16Array( buffer );
                HEAPU32 = new Uint32Array( buffer );
                HEAPF32 = new Float32Array( buffer );
                HEAPF64 = new Float64Array( buffer );
            }
        }
    };

    function __load( instance ) {
        Object.defineProperty( Module, 'instance', { value: instance } );
        Object.defineProperty( Module, 'web_malloc', { value: Module.instance.exports.__web_malloc } );
        Object.defineProperty( Module, 'web_free', { value: Module.instance.exports.__web_free } );
        Object.defineProperty( Module, 'web_table', { value: Module.instance.exports.__web_table } );

        if( typeof module !== 'undefined' && module.exports ) {
            module.exports = Module.exports;
        } else {
            Rust.whatlang_demo.exports = Module.exports;
        }

        __imports.env.__web_on_grow();
        Module.instance.exports.__web_main();
    }

    if( Module.nodejs ) {
        const fs = require( 'fs' );
        const path = require( 'path' );
        const wasm_path = path.join( __dirname, "whatlang-demo.wasm" );
        const buffer = fs.readFileSync( wasm_path );
        const mod = new WebAssembly.Module( buffer );
        const instance = new WebAssembly.Instance( mod, __imports );
        __load( instance );
        return Module.exports;
    } else {
        const __promise = fetch( "whatlang-demo.wasm" )
            .then( response => response.arrayBuffer() )
            .then( bytes => WebAssembly.instantiate( bytes, __imports ) )
            .then( results => {
                __load( results.instance );
                console.log( "Finished loading Rust wasm module 'whatlang_demo'" );
                return Module.exports;
            })
            .catch( error => {
                console.log( "Error loading Rust wasm module 'whatlang_demo':", error );
                throw error;
            });

        Rust.whatlang_demo = __promise;
        return __promise;
    }
}));
```

## File: `examples/cli.rs`
```rust
extern crate whatlang;

use std::io;
use whatlang::detect;

fn main() {
    let mut text = String::new();
    println!("Please enter a text:");
    io::stdin()
        .read_line(&mut text)
        .expect("Failed to read line");

    if let Some(info) = detect(&text) {
        println!("Language: {}", info.lang());
        println!("Info: {:?}", info);
    } else {
        println!("Cannot recognize a language :(");
    }
}
```

## File: `misc/data.json`
```json
{
  "Latin": {
    "spa": " de|os |de | la|la | y | a |es |ón |ión|rec|ere|der| co|e l|el |en |ien|cho|ent|ech|ció|aci|o a|a p| el|a l|al |as |e d| en|na |ona|s d|da |nte| to|ad |ene|con| pr| su|tod| se|ho |los| pe|per|ers| lo|o d| ti|cia|n d|cio| es|ida|res|a t|tie|ion|rso|te |do | in|son| re| li|to |dad|tad|e s|est|pro|que|men| po|a e|oda|nci| qu| un|ue |ne |n e|s y|lib|su | na|s e|nac|ia |e e|tra| pa|or |ado|a d|nes|ra |se |ual|a c|er |por|com|nal|rta|a s|ber| o |one|s p|dos|rá |sta|les|des|ibe|ser|era|ar |ert|ter| di|ale|l d|nto|hos|del|ica|a a|s n|n c|oci|imi|io |o e|re |y l|e c|ant|cci| as|las|par|ame| cu|ici|ara|enc|s t|ndi| so|o s|mie|tos|una|bre|dic|cla|s l|e a|l p|pre|ntr|o t|ial|y a|nid|n p|a y|man|omo|so |n l| al|ali|s a|no | ig|s s|e p|nta|uma|ten|gua|ade|y e|soc|mo | fu|igu|o p|n t|hum|d d|ran|ria|y d|ada|tiv|l e|cas| ca|vid|l t|s c|ido|das|dis|s i| hu|s o|nad|fun| ma|rac|nda|eli|sar|und| ac|uni|mbr|a u|die|e i|qui|a i| ha|lar| tr|odo|ca |tic|o y|cti|lid|ori|ndo|ari| me|ta |ind|esa|cua|un |ier|tal|esp|seg|ele|ons|ito|ont|iva|s h|d y|nos|ist|rse| le|cie|ide|edi|ecc|ios|l m|r e|med|tor|sti|n a|rim|uie|ple|tri|ibr|sus|lo |ect|pen|y c|an |e h|n s|ern|tar|l y|egu|gur|ura|int|ond|mat|l r|r a|isf|ote",
    "eng": " th|the| an|he |nd |and|ion| of|of |tio| to|to |on | in|al |ati|igh|ght|rig| ri|or |ent|as |ed |is |ll |in | be|e r|ne |one|ver|all|s t|eve|t t| fr|s a| ha| re|ty |ery| or|d t| pr|ht | co| ev|e h|e a|ng |ts |his|ing|be |yon| sh|ce |ree|fre|ryo|n t|her|men|nat|sha|pro|nal|y a|has|es |for| hi|hal|f t|n a|n o|nt | pe|s o| fo|d i|nce|er |ons|res|e s|ect|ity|ly |l b|ry |e e|ers|e i|an |e o| de|cti|dom|edo|eed|hts|ter|ona|re | no| wh| a | un|d f| as|ny |l a|e p|ere| en| na| wi|nit|nte|d a|any|ted| di|ns |sta|th |per|ith|e t|st |e c|y t|om |soc| ar|ch |t o|d o|nti|s e|equ|ve |oci|man| fu|ote|oth|ess| al| ac|wit|ial| ma|uni| se|rea| so| on|lit|int|r t|y o|enc|thi|ual|t a| eq|tat|qua|ive| st|ali|e w|l o|are|f h|con|te |led| is|und|cia|e f|le | la|y i|uma|by | by|hum|f a|ic | hu|ave|ge |r a| wo|o a|ms |com| me|eas|s d|tec| li|n e|en |rat|tit|ple|whe|ate|o t|s r|t f|rot| ch|cie|dis|age|ary|o o|anc|eli|no | fa| su|son|inc|at |nda|hou|wor|t i|nde|rom|oms| ot|g t|eme|tle|iti|gni|s w|itl|duc|d w|whi|act|hic|aw |law| he|ich|min|imi|ort|o s|se |e b|ntr|tra|edu|oun|tan|e d|nst|l p|d n|ld |nta|s i|ble|n p| pu|n s| at|ily|rth|tho|ful|ssi|der|o e|cat|uca|unt|ien| ed|o p|h a|era|ind|pen|sec|n w|omm|r s",
    "por": "os |de | de| a | e |o d|to |ão | di|ent|da |ito|em | co|eit|as |dir|es |ire|rei| se|ção|ade|a p|dad|e d|s d|men|nte|do |s e| pr| pe|dos| to| da|a a|o e| o |o a|ess|con|tod|que| qu|te |e a| do|al |res|ida|m d| in| ou|er |sso| na| re| po|a s| li|uma|cia|ar |pro|e e|a d| te|açã|a t| es| su|ou |ue |s p|tos|a e|des|ra |com|no |ame|ia |e p|tem|nto| pa|is |est|tra|ões|na |s o|oda|das|ser|soa|s n|pes|o p|s a|o s|e o| em| as| à |o o|ais|ber|ado|oa |o t|e s|man|sua|ua | no| os|a c|ter|çõe|erd|lib|rda|s s|nci|ibe|e n|ica|odo|so |nal|ntr|s t|hum|ura| ao|ona|ual| so|or |ma |sta|o c|a n|pre|ara|era|ons|e t|r a|par|o à| hu|ind|por|cio|ria|m a|s c| um|a l|gua|ran| en|ndi|o i|e c|raç|ion|nid|aci|ano|soc|e r|oci| ac|und|sen|nos|nsi|rec|ime|ali|int|um |per|nac| al|m o|r p| fu|ndo|ont|açõ| ig|igu|fun|nta| ma|uni|cçã|ere| ex|a i| me|ese|rio|l d|a o|s h|pel|ada|pri|ide|am |m p|pod|s f|ém |a f|io |ode|ca |ita|lid|tiv|e f|vid|r e|esp|nda|omo|e l|naç|o r|ant|a q|tad|lic|iva| fa|ver|s l|ial|cla|ngu|ing| ca|mo |der| vi|eli|ist|ta |se |ati|ios|ido|r o|eci|dis| un|e i|r d|ecç|o q|s i|qua|ênc|a m|seu|sti|nin|uer|rar|cas|aos|ens|gué|ias|sid|uém|tur|dam|sse|ao |ela|l e|for|tec|ote| pl|ena| tr|m c|tro| ni|ico|rot",
    "ind": "an |ang| da|ng | pe|ak | ke| me|ata| se|dan|kan| di| be|hak|ber|per|ran|nga|yan|eng| ya| ha|asa|gan|men|ara|nya|n p|n d|n k|a d|tan| at|at |ora|ala|san| ba|ap |erh|n b|rha|ya | ma|g b|a s|pen|eba|as |aan|uk |ntu| or|eti|tas|aka|tia|ban|set| un|n s|ter|n y| te|k m|tuk|bas|iap|lam|beb|am | de|k a|keb|n m|i d|unt|ama|dal|ah |ika|dak|ebe|p o|sa |pun|mem|n h|end|den|ra |ela|ri |nda| sa|di |ma |a m|n t|k d|n a|ngg|tau|man|gar|eri|asi| ti|un |al |ada|um |a p|lak|ari|au | ne|neg|a b|ngs|ta |ole|leh|ert|ers|ida|k h|ana|gsa|dar|uka|tid|bat|sia|era|eh |dap|ila|dil|h d|atu|sam|ia |i m| in|lan|aha|uan|tu |ai |t d|a a|g d|har|sem|na |apa|ser|ena|kat|uat|erb|erl|mas|rta|ega|ung|nan|emp|n u|kum|l d|g s| hu|ka |ent|pat|mba|aga|nta|adi| su|eni|uku|n i|huk|ind|ar |rga|i s|aku|ndi|sua|ni |rus|han|si |car|nny| la|in |u d|ik |ua |lah|rik|usi|emb|ann|mer|ian|gga|lai|min|a u|lua|ema|emu|arg|dun|dip|a t|mat|aya|rbu|aru|erk|rka|ini|eka|a k|rak|kes|yat|iba|nas|rma|ern|ese|s p|nus| pu|anu|ina| ta|mel|mua|kel|k s|us |ndu|nak|da |sya|das|pem|lin|ut |yar|ami|upu|seo|aik|eor|iny|aup|tak|ipe|ing|tin| an|dik|uar|ili|g t|rse|sar|ant|g p|a n|aks|ain| ja|t p| um|g m|dir|ksa|umu|kep|mum|i k|eca|rat|m p|h p|aba|ses|m m",
    "fra": " de|es |de |ion|nt |et |tio| et|ent| la|la |e d|on |ne |oit|e l|le | le|s d|e p|t d|ati|roi| dr|dro|it | à | co|té |ns |te |e s|men|re | to|con| l’|tou|que| qu|les| so|des|son| pe|ons| un|s l|s e| pr|ue | pa|e c|t l|ts |onn| au|e a|eme|e e| li|ont|ant|out|ute|t à|res|ers| sa|ce | a |tre|per|a d|cti|er |lib|ité| en|ux | re|en |rso|à l| ou| in|lle|un |nat|ou |nne|n d|une| d’| se|par|nte|us |ur |s s|ans|dan|a p|r l|pro|its|és |t p|ire|e t|s p|sa | dé|ond|é d|a l|nce|ert|aux|omm|nal|me | na| fo|iqu| ce|rté|ect|ale|ber|t a|s a| da|mme|ibe|san|e r| po|com|al |s c|qui|our|t e| ne|e n|ous|r d|ali|ter| di|fon|e o|au | ch|air|ui |ell| es|lit|s n|iss|éra|tes|soc|aut|oci|êtr|ien|int|du |est|été|tra|pou| pl|rat|ar |ran|rai|s o|ona|ain|cla|éga|anc|rs |eur|pri|n c|e m|s t|à u| do|ure|bre|ut | êt|age| ét|nsi|sur|ein|sen|ser|ndi|ens|ess|ntr|ir | ma|cia|n p|st |a c| du|l e| su|bli|ge |rés| ré|e q|ass|nda|peu|ée |l’a| te|a s|tat|il |tés|ais|u d|ine|ind|é e|qu’| ac|s i|n t|t c|n a|l’h|t q|soi|t s|cun|rit| ég|oir|’en|nta|hom| on|n e| mo|ie |ign|rel|nna|t i|l n| tr|ill|ple|s é|l’e|rec|a r|ote|sse|uni|idé|ive|s u|t ê|ins|act| fa|n s| vi|gal| as|lig|ssa|pré|leu|e f|lic|dis|ver| nu|ten|ssi|rot|tec|s m|abl",
    "deu": "en |er |der| un|nd |und|ein|ung|cht| de|ich|sch|ng | ge|ie |che|ech| di|die|rec|gen|ine|eit| re|ch | da|n d|ver|hen| zu|t d| au|ht | ha|lic|it |ten|rei| be|in | ve| in| ei|nde|auf|den|ede|zu |n s|uf |fre|ne |ter|es | je|jed|n u| an|sei|and| fr|run|at | se|e u|das|hei|s r|hte|hat|nsc|nge|r h|as |ens| al|ere|lle|t a| we|n g|rde|nte|ese|men| od|ode|ner|g d|all|t u|ers|te |nen| so|d d|n a|ben|lei| gr| vo|wer|e a|ege|ion| st|ige|le |cha| me|haf|aft|n j|ren| er|erk|ent|bei| si|eih|ihe|kei|erd|tig|n i|on |lun|r d|len|gem|ies|gru|tli|unt|chu|ern|ges|end|e s|ft |st |ist|tio|ati| gl|sta|gun|mit|sen|n n| na|n z|ite| wi|r g|eic|e e|ei |lie|r s|n w|gle|mei|de |uch|em |chl|nat|rch|t w|des|n e|hre|ale|spr|d f|ach|sse|r e| sc|urc|r m|nie|e f|fen|e g|e d| ni|dur|dar|int| du|geh|ied|t s| mi|alt|her|hab|f g|sic|ste|taa|aat|he |ang|ruc|hli|tz |eme|abe|h a|n v|nun|geg|arf|rf |ehe|pru| is|erf|e m|ans|ndl|e b|tun|n o|d g|n r|r v|wie|ber|r a|arb|bes|t i|h d|r w|r b| ih|d s|igk|gke|nsp|dig|ema|ell|eru|n f|ins|rbe|ffe|esc|igu|ger|str|ken|e v|gew|han|ind|rt | ar|ieß|n h|rn |man|r i|hut|utz|d a|ls |ebe|von|lte|r o|rli|etz|tra|aus|det|hul|e i|one|nne|isc|son|sel|et |ohn|t g|sam| fa|rst|rkl|ser|iem|g v|t z|err",
    "jav": "ng |an |ang| ka|ing|kan| sa|ak |lan| la|hak| ha| pa| ma|ngg|ara|sa |abe|ne | in|n k|ant| ng|tan|nin| an|nga|ata|en |ran| ba|man|ban|ane|hi |n u|ong|ra |nth|ake|ke |thi| da|won|uwo|ung|ngs| uw|asa|gsa|ben|sab|ana|aka|beb|a k|g p|nan|nda|adi|at |awa|san|ni |dan|g k|pan|eba| be|e k|g s|ani|bas| pr|dha|aya|gan|ya |wa |di |mar|n s| wa|ta |a s|g u| na|e h|arb|a n|a b|a l|n n| ut|yan|n p|asi|g d|han|ah |g n| tu| um|as |wen|dak|rbe|dar| di|ggo|sar|mat|k h|a a|iya| un|und|eni|kab|be |art|ka |uma|ora|n b|ala|n m|ngk|rta|i h| or|gar|yat|kar|al |a m|n i|na |g b|ega|pra|ina|kak|g a|a p|tum|nya|kal|ger|gge| ta|kat|i k|ena|oni|kas| pe|dad|aga|g m|duw|k k|uta|uwe| si| ne|adh|pa |n a|go |and|i l| ke|nun|nal|ngu|uju|apa|a d|t m|i p|min|iba|er | li|anu|sak|per|ama|gay|war|pad|ggu|ha |ind|taw|ras|n l|ali|eng|awi|a u| bi|we |bad|ndu|uwa|awe|bak|ase|eh | me|neg|pri| ku|ron|ih |g t|bis|iji|i t|e p| pi|aba|isa|mba|ini|a w|g l|ika|n t|ebu|ndh|ar |sin|lak|ur |mra|men|ku | we|e s|a i|liy| ik|ayo|rib|ngl|ami|arg|nas|yom|wae|ut |kon|ae |rap|aku| te|dil|tin|rga|jud|umu| as|rak|bed|k b|il |kap|h k|jin|k a| nd|e d|i s| lu|i w|eka|mum|um |uha|ate| mi|k p|gon|eda| ti|but|n d|r k|ona|uto|tow|wat|gka|si |umr|k l|oma",
    "vie": "ng |̣c |́c | qu| th|à |nh | ng|̣i | nh|và| va|̀n |uyê| ph| ca|quy|ền|yề|̀i | ch|̀nh| tr| cu|ngư|i n|gươ|ườ|́t |ời| gi|ác| co|̣t |ó |c t|ự |n t|cá|ông| kh|ượ|ợc| tư| đư|iệ|đươ|ìn|́i | ha|có|i đ|gia| đê|pha| mo|ọi|mọ|như|n n|củ| ba|̣n |̉a |ủa|n c|̀u |̃ng|ân |ều|ất| bi|tự|hôn| vi|g t| la|n đ|đề|nhâ| ti|t c| đô|ên |bả|hiê|u c| tô|do |hân| do|ch |́ q|̀ t| na|́n |ay | hi|àn|̣ d|ới|há| đi|hay|g n| mô|ốc|uố|n v|ội|hữ|thư|́p |quô| ho|̣p |nà|ào|̀ng|̉n |ị |́ch|ôn |̀o |khô|c h|i c|c đ| hô|i v|tro| đa|́ng|mộ|i t|ột|g v|ia |̣ng|ản|ướ|ữn|̉ng|h t|hư |ện|n b|ộc|ả |là|c c|g c| đo|̉ c|n h|hà|hộ| bâ|ã |̀y | vơ|̣ t|̉i |iế| cô|t t|g đ|ức|iên| vê|viê|vớ|h v|ớc|ực|ật|tha|̉m |ron|ong|áp|g b|hươ| sư|a c|sự|̉o |ảo|h c|ể |o v|uậ|a m|ế |iá|̀ c|cho|qua|hạ|ục| mi|̀ n|phâ|c q|côn|o c|á |i h|ại| hơ|̃ h| cư|n l|bị| lu|bấ|cả|ín|h đ| xa|độ|g h|c n|c p|thu|ải|ệ | hư|́ c|o n| nư|ốn|́o |áo|xã|oà|y t|hả|tộ|̣ c| tâ|thô| du|m v|mì|ho |hứ|ệc|́ t|hợ|án|n p|cũ|ũn|iể|ối|tiê|ề |hấ|ợp|hoa|y đ|chi|o h|ở |ày|̉ t|đó|c l|về|̀ đ|i b|kha|c b| đâ|luâ|ai |̉ n|đố|ết|hự|tri|p q|nươ|dụ|hí|g q|yên|họ|́nh| ta| bă|c g|n g|thê|o t|c v|am |c m|an ",
    "ita": " di|to | de|ion| in|la |e d|di |ne | e |zio|re |le |ni |ell|one|lla|rit|a d|o d|del|itt|iri|dir| co|ti |ess|ent| al|azi|tto|te |i d|i i|ere|tà | pr|ndi|e l|ale|o a|ind|e e|e i|gni|nte|con|i e|li |a s| un|men|ogn| ne|uo | og|idu|e a|ivi|duo|vid| es|tti| ha|div| li|a p|no |all|pro|za |ato|per|sse|ser| so|i s| la| su|e p| pe|ibe|na |a l| il|ber|e n|il |ali|lib|ha |che|in |o s|e s| qu|o e|ia |e c| ri|nza|ta |nto|he |oni|o i| o |sta|o c|nel| a |o p|naz|e o|so | po|o h|gli|i u|ond|i c|ers|ame|i p|lle|un |era|ri |ver|ro |el |una|a c| ch|ert|ua |i a|ssi|rtà|a e|ei |dis|ant| l |tat|a a|ona|ual| le|ità|are|ter| ad|nit| da|pri|dei|à e|cia| st| si|nal|est|tut|ist|com|uni| ed|ono| na|sua|al |si |anz| pa| re|raz|gua|ita|res|der|soc|man|o o|ad |i o|ese|que|enz|ed | se|io |ett|on | tu|dic|à d|sia|i r|rso|oci|rio|ari|qua|ial|pre|ich|rat|ien|tra|ani|uma|se |ll |eri|a n|o n| um|do |ara|a t|zza|er |tri|att|ico|pos|sci|i l|son|nda|par|e u|fon| fo|nti|uzi|str|utt|ati|sen|int|nes|iar| i |hia|n c|sti|chi|ann|ra | eg|egu|isp|bil|ont|a r| no|rop| me|opr|ost| ma|ues|ica|sso|tal|cie|sun|lit|ore|ina|ite|tan| ra|non|gio|d a|e r|dev|i m|l i|ezz|izi| cu|nno|rà |a i|tta|ria|lia|cos|ssu|dal|l p| as|ass|opo|ve |eve",
    "tur": " ve| ha|ve |ler|lar|ir |in |hak| he|her|bir|er |an |arı|eri|ya | bi|ak |r h|eti|ın |iye|yet| ka|ası|ını| ol|tle|eya|kkı|ara|akk|etl|sın|esi|na |de |ek | ta|nda|ini| bu|ile|rın|rin|vey|ne |kla|e h|ine|ır |ere|ama|dır|n h| sa|ına|sin|e k|le | ge|mas|ınd|nın|ı v| va|lan|lma|erk|rke|nma|tin|rle| te|nin|akl|a v|da | de|let|ill|e m|ard|en |riy|aya|nı | hü| şa|e b|k v|kın|k h| me|mil|san| il|si |rdı|e d|dan|hür|var|ana|e a|kes|et |mes|şah|dir| mi|ret|rri| se|ola|ürr|irl|bu |mak| ma|mek|n e|kı |n v|n i|lik|lle| ed| hi|n b|a h| ba|nsa| iş|eli|kar| iç|ı h|ala|li |ulu|rak|evl|e i|ni |re |r ş|eme|etm|e t|ik |e s|a b|iş |n k|hai|nde|aiz| eş|izd|un |olm|hiç|zdi|ar |unm|ma | gö|ilm|lme|im |n t|tir|dil|mal|e g|i v| ko|lun|e e|mel|ket|ık |n s|ele|la |el |r v|ede|şit|ili|eşi|yla|a i| an|anı| et|rı |ahs| ya|sı |edi|siy|t v|i b|se |içi|çin|bul|ame| da|miş|may|tim|a k|tme|r b|ins|yan|nla|mle| di|eye|ger|ye |uğu|erd|din|ser| mü|mem|vle| ke|nam|ind|len|eke|es | ki|n m|it | in| ku|rşı|a s|arş| ay|eml|lek|oru|rme|kor|rde|i m| so|tür|al |lam|eni|nun| uy|ken|hsı|i i|a d|ri |dev|ün |a m|r a|mey|cak|ıyl|maz|e v|ece|ade|iç |şma|mse|te |tün|ims|kim|e y|şı |end|k g|ndi|alı| ce|lem|öğr|ütü|k i|r t| öğ|büt|anl| bü",
    "pol": " pr|nie| i |ie |pra| po|ani|raw|ia |nia|wie|go | do|ch |ego|iek|owi| ni|ści|ci |a p|do |awo| cz|ośc|ych| ma|ek |rze| na|prz| w |wo |ej | za|noś|czł|zło|eni|wa | je|łow|i p|wol|oln| lu|rod| ka| wo|lno|wsz|y c|ma |ny |każ|ażd|o d|stw|owa|dy |żdy| wy|rzy|sta|ecz| sw|dzi|i w|e p|czn|twa|na |zys|ów |szy|ub |lub|a w|est|kie|k m|wan| sp|ają| ws|e w|pow|pos|nyc|rac|spo|ać |a i|cze|sze|neg|yst|jak| ja|o p|pod|acj|ne |ńst|aro|mi | z |i i|nar| ko|obo|awa| ro|i n|jąc|zec|zne|zan|dow| ró|iej|zy |zen|nic|ony|aw |i z|czy|no |nej|o s|rów|odn|cy |ówn|odz|o w|o z|jeg|edn|o o|aki|mie|ien|kol| in|zie|bez|ami|eńs|owo|dno| ob| or| st|a s|ni |orz|o u|ym |stę|tęp|łec|jed|i k| os|w c|lwi|ez |olw|ołe|poł|cji|y w|o n|wia| be|któ|a j|zna|zyn|owe|wob|ka |wyc|owy|ji | od|aln|inn|jes|icz|h p|i s|się|a o|ją |ost|kra|st |sza|swo|war|cza|roz|y s|raz|nik|ara|ora|lud|i o|a z|zes| kr|ran|ows|ech|w p|dów|ą p|pop|a n|tki|stk|gan|zon|raj|e o|iec|i l| si|że |eka| kt| de|em |tór|ię |wni|lni|ejs|ini|odo|dni|ełn|kow|peł|a d|ron|dek|pie|udz|bod|nan|h i|dst|ieg|taw|z p|z w|zeń|god|iu |ano|lar| to|y z|a k|ale|kla|trz|zaw|ich|e i|ier|iko|dzy|chn|w z|by |ków|adz|ekl|ywa|ju |och|kor|sob|ocz|oso|u p|du |tyc|tan|ędz| mi|e s| ta|ki ",
    "orm": "aa |an |uu | ka|ni |aan|umm|ii |mma|maa| wa|ti |nam| fi|ta |tti| na|saa|fi | mi|rga|i k|a n| qa|dha|iyy|oot|in |mir|irg|raa|qab|a i|a k|kan|akk|isa|chu|amu|a f|huu|aba|kka| ta|kam|a a| is|amn|ami|att|ach|mni|yaa| bi|yuu|yyu|ee |wal|miy|waa|ga |ata|aat|tii|oo |a e|moo| ni| ee|ba | ak|ota|a h|i q| ga| dh|daa|haa|a m|ama|yoo|a b|i a|ka |kaa| hi|sum|aas|arg|man| hu| uu|u n| yo| ar| ke| ha|ees| ba|uf |i i|taa|uuf|iin|ada|a w|i f|ani|rra|na |isu| ad|i w|a u|nya|irr|da |hun|hin|ess| ho| ma|i m|und|i b|bar|ana|een|mu |is |bu |f m| ir| sa|u a|add|aad| la|i d|n h|eeg|i h|sa |hoj|abu| ya|kee|al |udh|ook|goo|ala|ira|nda|itt|gac|as |n k|mum|see|rgo|uum|ra |n t|n i|ara|muu|ums|mat|nii|sii|ssa|a d|a q| da|haw|a g|yya|asu|eef|u h|tum|biy| mo|a t|ati|eny|gam|abs|awa|roo|uma|n b|n m|u y|a s|sat|baa|gar|n a|mmo|nis| qo|nna| ku|eer| to|kko|bil|ili|lis|bir|otu|tee|ya |msa|aaf|suu|n d|jii|n w|okk|rka|gaa|ald|un |rum| ye|ame| fu|mee|yer|ero|amm|era|kun|i y|oti|tok|ant|ali|nni| am|lda|lii|n u|lee|ura|lab|aal|tan|laa|i g|ila|ddu|aru|u m|oji|gum|han|ega| se|ffa|dar|faa|ark|n y|hii|qix|gal|ndi| qi|asa|art|ef |uud| bu|jir| ji|arb|n g|chi|tam|u b|dda|bat|di |kar|lam|a l| go|bsi|sad|oka|a j|egu|u t|bee|u f|uun",
    "swh": "a k|wa |na | ya| ku|ya | na| wa|a m| ha|i y|a h|a n|ana|ki |aki|kwa| kw|hak| ka| ma|la |a w|tu |li |a u|ni |i k|a a|ila| ki|ali|a y|ati|za |ili|ifa| mt|ke | an|kil|kat|mtu|ake|ote|te |ka |ika|ma |we |a s|yo |fa |i n|ata|e k|ama|zi |amb|u a|ia |u w| yo|azi|kut|ina|i z|asi| za|o y|uhu|yak|au |ish|mba|e a|u k|hur|ha |tik|wat| au|uru| bi|sha|mu |ara|u n| as|hi | hi|ru |aif|tai|cha|ayo|a b|hal| uh| ch|yot|i h| zi|awa|chi|atu|e n|ngi|u y|mat|shi|ani|eri| am|uli|ele|sa |ja |e y|a t|oja|o k|nch|i a|a j| nc|ima| sh|ami| ta|end|any|moj|i w|ari|ham|uta|ii |iki|ra |ada|wan|wak|nay|ye |uwa| la|ti |eza|o h|iri|iwa|kuw|iwe| wo|fan| sa|she|bu |kan|ao |jam|wen|lim|i m|her|uto|ria| ja| ni|kam|di | hu|zo |a l|da |kaz|ahi|amu|wot|o w|si |dha|bin|ing|adh|a z|bil|e w|nya|kup|har|ri |ang|aka|sta|aji|ne |kus|e m|zim|ini|ind|lin|kul|agu|kuf|ita|bar|o n|uu |iyo|u h|nad|maa|mwe|ine|gin|nye|nde|dam|ta | nd|ndi|rik|asa| ba|rif|uni|nga|hii|lez|bo |azo|uzi|mbo|sil|ush|tah|wam|ibu|uba|imu| ye|esh| ut|taa|aar|wez|i s|e b| si|ala|dhi|eng|aza|tak|hir|saw|izo|kos|tok|oka|yan|a c|wal|del|i b|pat| um|ndo|zwa|mam|a i|guz|ais|eli|mai|laz|ian|aba|man|ten|zin|ba |nda|oa |u m|uku|ufu| mw|liw|aha|ndw|kuh|ua |upa| el|umi|sia",
    "sun": "an |na |eun| ka|ng | sa|ana|ang| di|ak | ha|nga|hak|un |ung|keu|anu| ba| an|nu |a b| bo| je|a h|ata|asa|jeu|ina| ng|ara|nan|awa|gan|ah |sa |a k| na|n k|kan|aha|a p|a s|ga |ban| ma|a n|ing|oga|bog|sar| pa| ku|man|a a|ha |san|ae |bae|din|g s|aga|sah|ra |tan|n s| pe|ala| si|kat|ma |per| ti|aya|sin| at| pi| te|n a|aan|lah|pan|gar|n n|u d|ta |eu |ari|kum|ngs|a m|n b|n d|ran|a d|gsa|wa |taw|k h|ama|ku |ike|n p|eba|bas| ja|al |a t|ika|at |beb|kab|pik|asi|atu|nda|una|a j|nag|e b|n h|en |g k|oh |aba|ila|rta|aku|boh|ngg|abe|art|ar |n j|di |ima|um |ola|geu|usa|aca|sak|adi|k a|udu|teu|car|tin| me| ay|h k| po|eh |u s|aka|rim|ti |sac|k n|ngt|jen|awe|ent|u a|uma|teh|law|ur |h s|dan|bar|uku|gaw|aru|ate|iba|dil|pol|aja|ieu|ere|jal|nar| hu|n t|nya|pa |are|upa|mas|ake|ut |wan| ge|kal|nus| so|ngk|ya |yan|huk| du|tun| mi|mpa|isa|lan|ura|u m|uan|ern|ena|nte|rup|tay|n m| ke|ka |han|und|us |h b|kud|ula|tut| tu| ie|hna|kaw|u k|lak|gam|mna|umn|g d| nu|yun|ri |ayu|wat| wa|eri|g n|a u|i m|u p| ta|du |dit|umu|k k|ren|mba|rik|gta| be|ali|h p|h a|eus|u n|alm|il | da|sas|ami|min|lma|ngu|nas|yat|rak|amp|mer|k j|sab|mum| ra|rua|ame|ua |ter|sal|ksa|men|kas|nge|k d|ona| bi|bis|sio|ion|nal|taa| de|uh |gal|dip|we |bad",
    "ron": " de|și | și|re | în|are|te |de |ea |ul |rep|le |ept|dre|e d| dr|ie |în |e a|ate|ptu| sa|tul| pr|or |e p| pe|la |e s|ori| la| co|lor| or|ii |rea|ce |au |tat|ați| a | ca|ent| fi|ale|ă a|a s| ar|ers|per|ice| li|uri|a d|al | re|e c|ric|nă |i s|e o|ei |tur| să|lib|con|men|ibe|ber|rso|să |tăț|sau| ac|ilo|pri|ăți|i a|i l|car|l l|ter| in|ție|că |soa|oan|ții|lă |tea|ri |a p| al|ril|e ș|ană|in |nal|pre|i î|uni|ui |se |e f|ere|i d|e î|ita| un|ert|ile|tă |a o| se|i ș|pen|ia |ele|fie|i c|a l|ace|nte|ntr|eni| că|ală| ni|ire|ă d|pro|est|a c| cu| nu|n c|lui|eri|ona| as|sal|ând|naț|ecu|i p|rin|inț| su|ră |e n| om|ici|nu |i n|oat|ări|l d| to|tor| di| na|iun| po|oci|tre|ni |ste|soc|ega|i o|gal| so| tr|ă p|a a|n m|sta|va |ă î|fi |res|rec|ulu|nic|din|sa |cla|nd | mo| ce| au|ara|lit|int|i e|ces|uie|at |rar|rel|iei|ons|e e|leg|nit|ă f| îm|a î|act|e l|ru |u d|nta|a f|ial|ra |ă c| eg|ță | fa|i f|rtă|tru|tar|ți |ă ș|ion|ntu|dep|ame|i i|reb|ect|ali|l c|eme|nde|n a|ite|ebu|bui|ât |ili|toa|dec| o |pli|văț|nt |e r|u c|ța |t î|l ș|cu |rta|cia|ane|țio|ca |ită|poa|cți|împ|bil|r ș| st|omu|ăță|țiu|rie|uma|mân| ma|ani|nța|cur|era|u a|tra|oar| ex|t s|iil|ta |rit|rot|mod|tri|riv|od |lic|rii|eze|man|înv|ne |nvă|a ș|cti",
    "hau": "da | da|in |a k|ya |an |a d|a a| ya| ko| wa| a |sa |na | ha|a s|ta |kin|wan|wa | ta| ba|a y|a h|n d|n a|iya|ko |a t|ma |ar | na|yan|ba | sa|asa| za| ma|a w|hak|ata| ka|ama|akk|i d|a m| mu|su |owa|a z|iki|a b|nci| ƙa| ci| sh|ai |kow|anc|nsa|a ƙ|a c| su|shi|ka | ku| ga|ci |ne |ani|e d|uma|‘ya|cik|kum|uwa|ana| du| ‘y|ɗan|ali|i k| yi|ada|ƙas|aka|kki|utu|n y|a n|hi | ra|mut| do| ad|tar| ɗa|nda| ab|man|a g|nan|ars|and|cin|ane|i a|yi |n k|min|sam|ke |a i|ins|yin|ki |nin|aɗa|ann|ni |tum|za |e m|ami|dam|kan|yar|en |um |n h|oka|duk|mi | ja|ewa|abi|kam|i y|dai|mat|nna|waɗ|n s|ash|ga |kok|oki|re |am |ida|sar|awa|mas|abu|uni|n j|una|ra |i b| ƙu|dun|a ‘|cew|a r|aba|ƙun|ce |e s|a ɗ|san|she|ara|li |kko|ari|n w|m n|buw|aik|u d|kar| ai|niy| ne|hal|rin|bub|zam|omi| la|rsa|ubu|han|are|aya|a l|i m|zai|ban|o n|add|n m|i s| fa|bin|r d|ake|n ‘|uns|sas|tsa|dom| ce|ans| hu|me |kiy|ƙar| am|ɗin| an|ika|jam|i w|wat|n t|yya|ame|n ƙ|abb|bay|har|din|hen|dok|yak|n b|nce|ray|gan|fa |on | ki|aid| ts|rsu| al|aye| id|n r|u k|ili|nsu|bba|aur|kka|ayu|ant|aci|dan|ukk|ayi|tun|aga|fan|unc| lo|o d|lok|sha|un |lin|kac|aɗi|fi |gam|i i|yuw|sun|aif|aja| ir|yay|imi|war| iy|riy|ace|nta|uka|o a|bat|mar|bi |sak|n i| ak|tab|afi|sab",
    "bos": " pr| i |je |rav| na|pra|na |da |ma |ima| sv|a s|nje|a p| da| po|anj|a i|vo |va |ko |ja | u |ako|o i|no | za|e s|ju |avo| im|ti |sva|ava|i p|o n|li |ili|i s|van|ost| ko|vak|ih |ne |a u| sl|nja|koj| dr| ne|jed| bi|i d|ije|stv|u s|lob|im |slo| il|bod|obo| ra|sti|pri| je| su|vje|om |a d|se |e i| ob|a n|i i| se|dru|enj| os|voj|cij|e p|a b|su |o d|uje|u p|raz|i n|a o| od|lo |u o|ova|u i|edn|i u| nj|ovo|jen|lju|ni |oje|nos|a k|ran|dje|iti|o p|aci|žav|a j|i o|e o|pre|pro|bra|nih|ji | ka|e d|jeg|og |sta| tr|tre|bud|u n|drž|u z|rža|bit|svo|ija|elj|reb|e b|mij|jem|avn|pos| bu|ka |aju| iz|ba |ve |rod|de |aro|e u|iva|a z|em |šti|ilo|eni|lje|ći |red|bil|jel|jer| ni|odn|m i|du |tva|nar|gov| sa|oji| do|tu |vim|u d| st|o k|e n|a t|za |nim| dj| sm|ući|ičn|dna|i m|oda|vno|eba|ist|nac|e k|čno|nak|ave|tiv|eđu|nov|olj|sno|ani|aln|an |nom|i b|stu|nst|eno|oj |osn|a r|ovj|nap|smi|nog|čov|oja|nju|ara|nu |dno|ans|ovi|jan|edi|m s| kr|h p|tup| op| čo|iko|jek|tvo| vj| mi|tel|vu |obr|živ|tit|o o|una|odu| mo| ov|kri|ego|din|rug|nik|rad|pod|nji|sam|sto|lja|dst|rim|ite|riv| te|m n|vol|i v|e t|vni|akv|itu|g p| ta|ašt|zaš|svi|ao |te |o s|ak |mje|a č|odr|udu|kla|i t|avi|tno|nič| vr|nic|dni|u u|ina| de|oba|od |jih|st ",
    "hrv": " pr| i |je |rav|pra|ma | na|ima| sv|na |ti |a p|nje| po|a s|anj|a i|vo |ko |da |vat|va |no | za|i s|o i|ja |avo| u | im|sva|i p| bi|e s|ju |tko|o n|li |ili|van|ava| sl|ih |ne |ost| dr|ije| ne|jed|slo| ra|u s|lob|obo| os|bod| da| ko|ova|nja|koj|i d|atk|iti| il|stv|pri|om |im | je| ob| su| ka|i i|i n|e i|vje|i u|se |dru|bit|voj|ati|i o|ćen|a o|o p|a b|a n|ući| se|enj|sti|a u|edn|dje|lo |ćav| mo|raz|u p| od|ran|ni |rod|a k|su |aro|drć|svo|ako|u i|rća|a j|mij|ji |nih|eni|e n|e o| nj|pre|pos|ćiv|oje|eno|e p|nar|oda|nim|ovo|aju|ra |ći |og |nov|iva|a d|nos|bra|bil|i b|avn|a z|jen|e d|ve |ora|tva|jel|sta|mor|u o|cij|pro|ovi|za |jer|ka |sno|ilo|jem|red|em |lju|osn|oji| iz|aci| do|lje|i m| ni|odn|nom|jeg| dj|vno|vim|elj|u z|o d|rad|o o|m i|du |uje| sa|nit|e b| st|oj |tit|a ć|dno|e u|o s|u d|eću|ani|dna|nak|nst|stu| sm|e k|u u|an |gov|nju|juć|aln|m s|tu |a r|ćov|jan|u n|o k|ist|ću |te |tvo|ans|šti|nu |ara|nap|m p|nić|olj|bud| bu|edi|ovj|i v|pod|sam|obr|tel| mi|ina|zaš|e m|ašt| vj|ona|nji|jek| ta|duć|ija| ćo|tup|h p|oja|smi|ada| op|oso|una|sob|odu|dni|rug|udu|ao |di |avi|tno|jim|itu|itk|će |odr|ave|meć|nog|din|svi| ći|kak|kla|rim|akv|elo|štv|ite|vol|jet|opć|pot|tan|ak |nic|nac|uće| sk| me|ven",
    "nld": "en |de |an | de|van| va| en| he|ing|cht|der|ng |n d|n v|et |een| ge|ech|n e|ver|rec|nde| ee| re| be|ede|er |e v|gen|den|het|ten| te| in| op|n i| ve|lij| zi|ere|eli|zij|ijk|te |oor|ht |ens|n o|and|t o|ijn|ied|ke | on|eid|op | vo|jn |id |ond|in |sch| vr|aar|n z|aan| ie|rde|rij|men|ren|ord|hei|hte| we|eft|n g|ft |n w|or |n h|eef|vri|wor| me|hee|al |t r|of |le | of|ati|g v|e b|eni| aa|lle| wo|n a|e o|nd |r h|voo| al|ege|n t|erk| da| na|t h|sta|jke|at |nat|nge|e e|end| st|om |e g|tie|n b|ste|die|e r|erw|wel|e s|r d| om|ij |dig|t e|ige|ter|ie |gel|re |jhe|t d| za|e m|ers|ijh|nig|zal|nie|d v|ns |d e|e w|e n|est|ele|bes| do|g e|che|vol|ge |eze|e d|ig |gin|dat|hap|cha|eke| di|ona|e a|lke|nst|ard| gr|tel|min| to|waa|len|elk|lin|eme|jk |n s|del|str|han|eve|gro|ich|ven|doo| wa|t v|it |ove|rin|aat|n n|wet|uit|ijd|ze | zo|ion| ov|dez|gem|met|tio|bbe|ach| ni|hed|st |all|ies|per|heb|ebb|e i|toe|es |taa|n m|nte|ien|el |nin|ale|ben|daa|sti| ma|mee|kin|pen|e h|wer|ont|iet|tig|g o|s e| er|igd|ete|ang|lan|nsc|ema|man|t g|is |beg|her|esc|bij|d o|ron|tin|nal|eer|p v|edi|erm|ite|t w|t a| hu|rwi|wij|ijs|r e|weg|js |rmi|naa|t b|app|rwe| bi|t z|ker|ame|eri|ken| an|ar | la|tre|ger|rdi|tan|eit|gde|g i|d z|oep",
    "kur": " he| û |ên | bi| ma|in |na | di|maf|an |ku | de| ku| ji|xwe|her| xw|iya|ya |kes|kir|rin|iri| ne|ji |bi |yên|afê|e b|de |tin|e h|iyê|ke |es |ye | we|er |di |we |ê d|i b| be|erk|ina| na| an|î û|yê |eye|î y|kî |rke|nê |diy|ete|eke|ber|hem|hey| li| ci|wek|li |n d|fê | bê| te|ne |yî | se|net|rî |tew|yek|sti|af | ki|re |yan|n b|kar|hev|e k|aza|n û|wî | ew|i h|n k|û b|î b| mi| az|dan| wî|ekî|î a|a m|zad|e d|mir|bin|est|ara|iro|nav|ser|a w|adi|rov|n h|anê|tê |ewe|be |ewl|ev |mû | ya|tî |ta |emû| yê|ast|wle| tê|n m| bo|wey|s m|bo | tu|n j|ras| da| me|din|î d|ê h|n n|n w|ing|st | ke| ge|în |ar | pê|iye|îna|bat|r k|ema|cih|ê b|wed|û m|dî |û a|vak|ê t|ekh|par| ye|vî |civ|n e|ana|î h|ê k|khe|geh|nge|ûna|fên|ane|av |î m|bik|eyê|eyî|e û| re|man|erb|a x|vê |ê m|iva|e n|hî |bûn|kê | pa|erî|jî |end| ta|ela|nên|n x|a k|ika|f û|f h|î n|ari|mî |a s|e j|eza|tên|nek| ni|ra |ehî|tiy|n a|bes|rbe|û h|rwe|zan| a |erw|ov |inê|ama|ek |nîn|bê |ovî|ike|a n| ra|riy|i d|anî|û d|e e|etê|ê x|yet|aye|ê j|tem|e t|erd|i n|eta|ibe|a g|u d|xeb|atê|i m|tu | wi|dew|mal|let|nda|ewa| ên|awa|e m|a d|mam|han|u h|a b|pêş|ere| ba|lat|ist| za|bib|uke|tuk|are|asî|rti|arî|i a|hîn| hî|edi|nûn|anû|qan| qa| hi| şe|ine|n l|mên|ûn |e a",
    "yor": "ti | ní|ó̩ | è̩|ní | lá|̩n |o̩n|é̩ |wo̩|àn | e̩|kan|an |tí | tí|tó̩| kò|ò̩ |̩tó| àw| àt|è̩ |è̩t|e̩n|bí |àti|lát|áti| gb|lè̩|s̩e| ló| ó |àwo|gbo|̩nì|n l| a | tó|í è|ra | s̩|n t|ò̩k|sí |tó |̩ka|kò̩|ìyà|o̩ | sí|ílè|orí|ni |yàn|dè |̩‐è|ì k|̩ à|èdè| or|ún |ríl|è̩‐|í à|jé̩|‐èd|àbí|̩ò̩|ò̩ò|tàb|nì |í ó|n à| tà|̩ l|jo̩| ti|̩e |̩ t| wo|nìy|í ì|ó n| jé| sì|ló |kò |n è|wó̩| bá|n n|sì | fú|̩ s|í a|rè̩|fún| pé| òm|̩ni|gbà| kí| èn|ènì|in |òmì|ìí |ba |nir|pé |ira|mìn|ìni|n o|ràn|ìgb| ìg|bá |e̩ | rè|̩ n|kí |n e|un |gba|̩ p|í ò|nú | o̩|nín|gbé|yé | ka|ínú|a k|fi | fi|mo̩|bé̩|o̩d|dò̩|̩dò|ó s|i l|̩ o|̩ ì|wà |í i|i ì|hun|bò |i ò|dá |bo̩|o̩m|̩mo|̩wó|bo |áà |̩ k|ó j|ló̩|àgb|ohu| oh| bí| ò̩|bà |ara|yìí|ogb|írà|n s|ú ì| ìb|pò̩|í k| lè|bog|i t|à t|óò |yóò|kó̩|gé̩|à l|ó̩n|rú |lè | yó|̩ ò|̩ e|a w|̩ y|ò̩r|̩ f| wà|ò l|í t|ó b|i n|ó̩w|̩gb|yí |í w|ìké|̩ a|láà|wùj|àbò|i è|ùjo|fin|é̩n|n k|í e|i j|ú à| ìk|òfi| òf| ar|i s|mìí|ìír| mì| ir|rin|náà| ná|jú |̩ b| yì|ó t|̩é̩| i |̩ m|fé̩|kàn|rí |ú è|à n|wù |s̩é|é à| mú| èt|áyé|í g|̩kó|̩dá|è̩d|àwù|è̩k| ìd|irú|í o|i o|i à|láì|í n|ípa| kú|níp| ìm|a l|ké̩|bé |i g|de |ábé|ìn |báy|̩è̩|ígb|wò̩|níg|mú |láb| àà|n f|è̩s|̩ w|ùn |i a|ayé|èyí| èy|mó̩|á è| ni|n b| wó|je̩| ìj|gbá|ò̩n|ó̩g",
    "uzb": "lar|ish|an |ga |ar | va| bi|da |va |ir | hu|iga|sh |uqu|shi|bir|quq|huq|gan| bo| ha|ini|ng |a e|r b| ta|lis|ni |ing|lik|ida|oʻl|ili|ari|nin|on |ins| in|adi|nso|son|iy | oʻ|lan| ma|dir|hi |kin|har|i b|ash| yo|boʻ| mu|dan|uqi|ila|ega|qla|r i|qig|oʻz| eg|kla|a b|qil|erk|ki | er|oli|nli|at | ol|gad|lga|rki|oki|i h|a o| qa|yok|lig|osh|igi|ib |las|n b|atl|n m| ba|ara| qi|ri | sh|iya|ala|lat|in |ham|bil|a t|a y|bos|r h|siy|n o|yat|inl|ik |a q|cha|a h| et|eti|nis|a s|til|ani|h h|i v|mas|tla|osi|asi| qo|ʻli|ati|i m|rni|im |uql|arn|ris|qar|a i|gi | da|n h|ha |sha|i t|mla|rch| xa|i o|li |hun|bar|lin|ʻz |arc|rla| bu|a m|a a| as|mum| be| tu|aro|r v|ikl|lib|taʼ|h v|tga|tib|un |lla|mda| ke|shg| to|n q|sid|n e|mat|amd|shu|hga| te|tas|ali|umk|oya|hla|ola|aml|iro|ill|tis|iri|rga|mki|irl| ya|xal|dam| de|gin|eng|rda|tar|ush|rak|ayo| eʼ| so|ten|alq| sa|ur | is|imo|r t| ki|mil| mi|era|zar|hqa|aza|k b| si|nda|hda|kat|ak |oʻr|n v|a k|or |rat|ada|ʻlg|miy|tni|i q|shq|oda|shl|bu |dav|nid|y t|ch |asl|sos|ilg|aso|n t|atn|sin|am |ti |as |ana|rin|siz|yot|lim|uni|nga|lak|n i|a u|qon|i a|h k|vla|avl|ami|dek| ja|ema|a d|na | em|ekl|gʻi|si |i e|ino| ka|uch|bor|ker| ch|lma|liy|a v|ʼti|lli|aka|muh|rig|ech|i y|uri|ror",
    "ibo": "a n|e n|ke | na|na | ọ | bụ| n |nwe|ere|ọ b|re |nye| nk|ya |la | nw| ik| ma|ye |e ọ|ike|a o|nke|a m|ụ n| ya|a ọ|ma |bụl|ụla| on| a |e i|kik|iki|ka |ony|ta |bụ |kwa| nd|a i|i n|di |a a|wa |wer|do | mm|dụ |e a|ha | ga|any| ob|ndi| ok|he |e m|e o|a e|ọ n|ite|rụ |hi |mma|ga‐|wu |ara| dị|aka|che|oke|we |o n| ih|n o|adụ|mad|obo|bod|a g|odo| ka| ez|te |hị |be |ụta|dị | an|zi | oh|a‐e|akw|gba|i m|me | ak|u n|nya|ihe|ala|ohe|ghi|ri | ọz|her|ra |weg| nt| iw| mb|ba |pụt| si|ro |oro|iwu|chi|a‐a|rị |ụ i|ụ ọ| eb|iri|ebe|ụrụ|zọ | in|a y|ezi|e ị|kpa|le |ile|ịrị|n e|kpe|mba| ha|bi |sit|e e|inw|nil|asị| en|mak|a u| ni|apụ|chị|i i|ghị|i ọ|i o|si | e |ide|o i|e y|ụ m|a s|u o|kwu|ozu|yer|ru |enw|ụ o|ọzọ|gid|hụ |n a|ahụ|nkw|sor|egh|edo|a ụ|tar|n i|toz|ị o|pa |i a| me|ime|uru|kwe| mk|tu |ama|eny|uso|de | im|ọ d|osi|hed|a d| kw|mkp|wet| ọr| ọn|obi|ọrụ| ịk| to|gas| ch|ịch|nha|ọnọ|nọd| nc| al|n ụ|ị m| us|nọ |u ọ|nch| o |eta|n u| ot|otu|sir|sịr| nh|a k|ali|o m| ag| gb|e s|ọta|nwa|ị n|lit|ega|ji |ọdụ|e k|ban|e g|ị k|esi|agb|eme|hu |ikp|zu |pe |nta|na‐|chọ|u a|a b|uch|n ọ|onw|ram|kwụ|ekọ|i e| nọ| ug|ọch|u m|gwu|a h|zụz|ugw|meg|ị e|nat|e h|dịg|o y|kpu|pụr|cha|zụ |hịc|ich| ng|ach| og|wap|wan|ịgh|uwa| di| nn|i ị",
    "ceb": "sa | sa|ng |ang| ka|an | pa|ga | ma|nga|pag| ng|a p|on |kat|a k|ug |od | ug|g m| an|ana|n s|ay |ung|ata|ngo|a m|atu|ala|san|ag |tun|g s|g k|god|d s|a s|ong|mga| mg|g p|n u|yon|a a|pan|ing|usa|tan|tag|una|aga|mat|ali|g u|han|nan| us|man|y k|ina|non|kin| na|syo|lan|a b|asa|nay|n n|a i|awa| ta|taw|gaw|nsa|a n|nas| o |ban|agp|isa|dun|was|iya| gi|asy|adu|ini|bis| ad|ili|o s| bi|g a|nah|nag|a t| ki|lin|lay|ahi|sam|al |wal| di|nal|asu| ba|ano|agt| wa|ama|yan|a u| iy|kan|him|n k|gan|ags|n a|kag| un|ya |kas|gpa|g t| su|aha|wha|agk|awh|gka|a g|kal|l n|gla|gsa|sud|gal|imo|ud |d u|ran|uka|ig |aka|aba|ika|g d|ara|ipo|ngl|g n|uns|n o|kau|i s|y s|og |uta|d n|li | si|gik|g i|mta|ot |iin| la| og|o a|ayo|ok |awo|aki|kab|aho|n m|hat|o p|gpi|a w|apa|lip|ip | hu| ga|a h|uba|na | ti|bal|gon|la |ati|wo |ad |hin|sal|gba|buh| bu| ub|uha|agb|hon|ma |nin|uga|t n|ihi| pi|may| pu|mak|ni | ni|d a|pin|abu|agh|ahu|uma|as |dil|say| in|at |ins|lak|hun|ila|mo |s s|sak|amt|o u|pod|ngp|tin|a d|but|ura|lam|aod|t s|bah|ami|aug|mal|sos|os |k s| il|tra| at|gta|bat|aan|ulo|iha|ha |n p| al|g b|lih|kar|lao|agi|amb|mah|ho |sya|ona|aya|ngb|in |inu|a l| hi|mag|iko|it |agl|mbo|oon|tar|o n|til|ghi|rab|y p| re|yal|aw |nab|osy|dan",
    "tgl": "ng |ang| pa|an |sa | sa|at | ka| ng| ma|ala|g p|apa| na|ata|pag|pan| an| at|ay |ara|ga |a p|tan|g m|mga| mg|n n|pat| ba|n a|aya|na |ama|g k|awa|kar|a k|lan|rap|gka|nga|n s|g n|aha|g b|a a| ta|agk|gan|tao|asa|aka|yan|ao |a m|may|man|kal|ing|a s|nan|aga| la|ban|ali|g a|ana|y m|kat|san|kan|g i|ong|pam|mag|a n|o a|baw|isa|wat| y |lay|g s|y k|in |ila|t t| ay|aan|o y|kas|ina|t n|ag |t p|wal|una|yon| o | it|nag|lal|tay|pin|ili|ans|ito|nsa|lah|kak|any|a i|nta|nya|to |hay|gal|mam|aba|ran|ant|agt|on |t s|agp| wa| ga|gaw|han|kap|o m|lip|ya |as |g t|hat|y n|ngk|ung|no |g l|gpa|wa |lag|gta|t m|kai|yaa|sal|ari|lin|a l|pap|ahi| is| di|ita| pi|pun|agi|ipi|mak|a b|y s|bat|yag|ags|o n|aki|tat|pah|la |gay|hin| si|di |i n|sas|iti|a t|t k|mal|ais|s n|t a|al |ipu|ika|lit|gin| ip|ano|gsa|alo|nin|uma|hal|ira|ap |ani|od |i a|gga|y p|par|tas|ig |sap|ihi|nah|ini| bu|ngi|syo|o s|nap|o p|a g| ha|uka|a h|aru|a o|mah|iba|asy|li |usa|g e|uha|ipa|mba|lam|kin|kil|duk|n o|iga| da|dai|aig|igd|gdi|pil|dig|pak| tu|d n|sam|nas|nak|ba |ad |lim|sin|buh|ri |lab|it |tag|g g|lun|ain|and|nda|pas|kab|aho|lig|nar|ula| ed|edu| ib|git|ma |mas|agb|ami|agg|gi |sar|i m|siy|g w|api|pul|iya|amb|nil|agl|sta|uli|ino|abu|aun|ayu| al|iyo",
    "hun": " sz| a |en | va|és | és|min|ek | mi| jo|jog|ind|an |nek|sze|ság| az|gy |sza|nde|ala|az |den|a v|val|ele| el|oga|mél|egy| eg|n a|ga |zab| me|zem|emé|aba|int|van|bad|tel|tet| te|ak |tás|ény|t a| ne|gye|ély|tt |n s|ben|ség|zet|lam|meg|nak|ni | se|ete|sen|agy|let|lyn|s a|yne|ra |z e|et | al|mel|kin|k j|eté|ok |tek| ki|vag|re |n m|oz |hoz|ez |s s|ett|gok|ogy| kö|mbe|es |em |nem|ely| le|ell|emb|hog|k a|atá|köz|nt | ho|yen|hez|el |z a|len|dsá|ásá|tés|ads|k m| ál| em|a s|nte|a m|szt|a t|áll|ás |y a|ogo|sem|a h|enk|nye|ese|nki|ágo|t s|lap|ame|ber|ló |k é|nyi|ban|mén|s e|i m|t m| vé|lla|ly |ébe|lat|ág |ami|on |mze|n v|emz|fel|a n|lő |a a|eki|eri|yes| cs|lle|tat|elő|nd |i é|ég |ésé|lis|yil|vet|át |kül|ért| ke|éte|rés|l a|het|szo|art|alá| ny|tar|koz| am|a j|ész|enl|elé|ól |s k|tár|s é|éle|s t|lem|sít|ges|ott| fe|n k|tko|zás|t é|kel|ja | ha|aló|zés|nlő|ése|ot |ri |lek|más|tő |vel|i j|se |ehe|tes|eve|ssá|tot|t k|olg|eze|i v|áza|leh|n e|ül |tte|os |ti |atk|zto|e a|tos|ány|ána|zte|fej|del|árs|k k|kor|ége|szá|t n| bi|zat|véd|nev|elm|éde|zer|téb|biz|rra|ife|izt|ere|at |ll |k e|ny |sel| né|ába|lt |ai |sül|ház|kif|t e| ar|leg|d a|is |i e|arr|t t|áso|it |ető|al | má|t v| bá|bár|a é|esü|lye|m l| es|nyo",
    "aze": " və|və |ər |lar| hə|in |ir | ol| hü| bi|hüq|üqu|quq|na |lər|də |hər| şə|bir|an |lik| tə|r b|mal|lma|ası|ini|r h|əxs|şəx|ən |arı|qla|a m|dir|aq |uqu|ali| ma|una|ilə|ın |yət| ya|ara|ikd|əri|ar |əsi|əti|r ş|rin|yyə|n h| az|dən|nin|ərə|tin|iyy|mək|zad| mü|sin| mə|ni |nda|ət |ndə|aza|rın|ün |ını|ə a|i v|nın|olu|qun| qa| et|ilm|lıq|ə y|ək |lmə|lə |kdi|ind|ına|olm|lun|mas|xs |sın|ə b| in|n m|q v|nə |əmi|n t|ya |da | bə|tmə|dlı|adl|bər| on|əya|ə h|sı |nun|maq|dan|inə|etm|un |ə v|rlə|n b|si |raq| va|ə m|n a|ınd|rı |anı| öz|əra|nma|n i|ama|a b|irl|ala|li |ins|bil|ik | al| di|ığı|ə d|lət|il |ələ|ə i|ıq |nı |nla|dil|müd|n v|ə e|unm|alı| sə|xsi|ə o|uq |uql|nsa|ətl| də|ili|üda|asi| he|ola|san|əni|məs| da|lan| bu|tər|həm|dır|kil|iş |u v| ki|min|eyn|mi |yin| ha|sos|heç|bu |eç | ed|kim|lığ|alq|xal| as|sia|osi|r v|q h|rə |yan|i s| əs|daf|afi| iş|ı h|fiə| ta|ə q|ıql|a q|yar|sas|lı |ill|mil|əsa|liy|tlə|siy|a h|məz|tün|ə t| is|ist|iyi| so|n ə|al |ifa|ina|lıd|ı o|ıdı|əmə|ır |ədə|ial| mi|əyi|miy|çün|n e|iya|edi| cə| bü|büt|ütü|xil|üçü|mən|adə|t v|a v|axi|dax|r a|onu| üç|seç| nə| se|man|ril|sil|əz |iə |öz |ılı|aya|qan|i t|şər|təm|ulm|rəf|məh| xa|ğın| dö| ni|sti|ild|amə|qu |nam|n o|n d|var|ad |zam|tam|təh",
    "ces": " pr| a |ní | ne|prá|ráv|ost| sv| po|na |ch |ho | na|nos|o n| ro|ání|ti |vo |neb|ávo|má |bo |ebo| má|kaž| ka|ou |ažd| za| je|dý |svo|ždý| př|a s| st|sti|á p| v |obo|vob| sp|bod| zá|ých|pro|rod|ván|ení|né |ý m|ého| by| ná|spo|ně |o p|mi |í a|ter|roz|ová|to | ja| li|áro|nár|by |jak|a p|a z|ny | vš|kte|i a|lid|ím |o v|í p|u p|mu |at | vy|odn| so| ma|a v| kt|í n|zák|li |oli|ví |kla|tní|pod|stá|en |do |t s|mí |je |em |áva| do|byl| se|být|í s|rov| k |čin| ve|ýt |í b|it |dní|vše|pol|o s| bý|tví|nýc|stn|nou|ejn|sou|ran|ci |vol|se |nes|a n|pří|eho|ným|tát|va |ním|mez|ají|i s|stv|ké |ích|ečn|žen|e s|vé |ova|své|ým |kol|du |u s|jeh|kon|ave|ech|eré|nu | ze|i v|o d|í v|hra|ids|m p|ému|ole|y s| i |maj|o z| to|aby|sta| ab|m a|pra| ta|chn| ni|že |ovn|ako|néh|len|dsk|rac|lad|chr| že|vat| os|sob|aké|i p|smí|esm|st |i n|m n|a m|lně|lní|při|bez|dy |áln|ens|zem|t v|čen|leč|kdo|ými| ji|oci|i k| s |í m|jí | či|áv |ste|och| oc|vou|ákl| vz|rav|odu|nez|inn|ský|nit|ivo|a j|u k|iál| me|ezi|ské|ven|stu|u a|tej|oln|slu|zen|í z|y b|oko|zac|níc|jin|ky |a o|řís|obe|u v|tak|věd|oje| vý|ikd|h n| od|čno|oso|ciá|h p| de|a t|ům |soc|jíc|odů|něn|adn|tup|dů |děl|jno|kéh|por|ože|hov|aci|nem|é v|rok|i j|u o|od |ího|vin|odi",
    "mlg": "ny |na |ana| ny|y f|a n|sy |aha|ra |a a| fa|n n|y n|a m|an | fi|tra|any| ma|han|nan|ara|y a| am|ka |in |y m|ami|olo| ts|lon|min| mi| sy| na|a t| ol|fan| ha|a i|man|iza| iz|ina|ona|y h|aka|o a|ian|a h|reh|etr|a s|het|on |a f|ire|fah|tsy|mba| ar| hi|zan|ay |ndr|y o|ira|y t| an|ehe|o h|afa|y i|ren|ran| zo|ena|amb|dia|ala|amp|zo |ika| di|tan|y s|y z| az|ia |m p|rin|jo |n j| jo| dr|zy |ry |a d|ao |and|dre|haf|nen|mpi|rah| ka|eo |n d| ir|ho |am |rai|fa |elo|ene|oan|omb| ta| pi| ho|ava|azo|dra|itr|iny|ant|tsi|zon|asa|tsa| to|ari|ha |a k|van|n i|fia|ray| fo|mbe|ony|sa |isy|azy|o f|lal|ly |ova|lom| vo|nat|fir|sam|oto|zay|mis|ham|bel| ra|a r|ban|kan|iha|nin|a e|ary|ito| he| re| no|ita|voa|nam|fit|iar| ko|tok|isa|fot|no |otr|mah|aly|har|y v|y r| sa|o n|ain|kam|aza|n o|oka|ial|ila|ano|atr|oa | la|y l|eri|y d|ata|hev|sia|pia|its|reo| ao|pan|anj|aro|tov|nja|o s|fam|pir| as|ty |nto|oko|y k|sir|air|tin|hia|ais|mit|ba | it| eo|o t|mpa|kon|a z|a v|ity|ton|rak|era|ani|ive|mik|ati|tot|vy |hit|hoa|aho|ank|ame|ver|vah|tao|o m|ino|dy |dri|oni|ori| mo|hah|nao|koa|ato|end|n t| za|eha|nga|jak|bar|lah|mia|lna|aln|va | mb|lan| pa|aov|ama|eve|za |dro|ria|to |nar|izy|ifa|adi|via|aja| va|ind|n k|idi|fiv|rov|vel",
    "mad": "an |eng|ban|ng | sa| ka|dha| ba|ren|ak |ang| se| ha|hak| dh|na | pa|se |adh|a s|aba|n s|ara|ngg|are|ha |aga|sa | or|ore|asa|sar|ana| ma|aan|a k|ale|gi | ag|gad|a b|n o|n k|eba|ala|ra |gan| ke|dhu|ota|aja|bas|n b|ka |man|tab|dhi|beb|sab|ama|ako|abb|at |ggu|nga| ta|pan|wi |huw|uwi|eka|ata|a d|san| ot|agi|lak|hal|ba |bba|i h|ong|em |kab|g a|lem|a o| pe| na|ane|par|ngs|nge|gar|a a|tan|gsa|a p|ran|i s|k h|n p|uy |guy|ken|n a|al |ada| ga|apa|pon|e d| e |nek| an|g s|ta |kaa|on |kal|a m|ssa|ona|abe|kat| la|a e|e e|sal|ate|jan|ri |nan|lab|asi|sad|i p|e a|lan|aka|a h|ari| bi|ena|si |daj| ng|ton|e k|har|oss|gen|i k|g k|car|ase|ano|era|kon| be|nya|n d|nag|bad|ar |epo| da|mas| kl| al|n t|mat|nos|n n|ela|g e|a n|k k|uwa|adi|pad|ggi|uan|i d|ne | so|hi |sae|oan|wan|as |le |gap|ter|yat|om |kla|k a|e b|ina|ah |k s|koa|i a|ega|neg|n h|m p|aha| as| ja|abi|ma |kas|bi | mo|aon| di|one| ep|per|aya|e s|nto|te |bat|epa|nda|n e| ca|int|pam|di |ann| ra|aen|k d|amp|a t|nta|and|e p|rga|pen|yar|mpo|ste|dra|ok |oko|ila|g p|k b|i b|set|to |isa|nao|nna|n m|ett| a |bis|hid|bin|i m|nas| ho|kar|t s| po|dil| to|aju|ika|kom|arg|ant|raj|a l|das|tto|ost|mos|lae|ga |rek|idh|tad|hig|en |rny|arn|ndh|eta|adu| dr|jat|jua|gam",
    "nya": "ndi|ali|a k|a m| ku| nd|wa |na |nth| mu| al|yen|thu|se |ra |nse|hu |di |a n|la | pa|mun| wa|nga|unt| la|a u|u a|e a|ons|za | ma| lo|iye|ace|ce |a l|idw|ang| ka|kha|liy|ens|li |ala|ira|ene|pa |i n|we |e m|ana|dwa|era|hal|ulu|lo |ko |dzi| ci|yo |o w|iko|ga |a p|chi| mo|lu |o l|o m|oyo|ufu| um|moy|zik| an|ner|and|umo|ena| uf|dan|iri|ful|a a|ka |to |hit|nch| nc|a c|ito|fun|dwe| da|kuk|wac| dz|e l|a z|ape|kap|u w|e k|ere|ti |lir| za|pen|tha|aye|kut|mu |ro |ofu|ing|lid| zo|amu|o c|i m|mal|kwa|mwa|o a|eza|i p|o n|so |i d|lin|nso| mw|iro|zo | a |ati| li|i l|a d|ri |edw|kul|una|uti|lan|a b|iki|i c|alo|i k| ca|lam|o k|dza|ung|o z|mul|ulo|uni|gan|ant|nzi| na|nkh|e n|san|oli|wir|tsa|u k|ome|ca |gwi|unz|lon|dip|ipo|yan|gwe|pon|akh|uli|aku|mer|ngw|cit| po| ko|kir|mba|ukh|tsi|bun|iya|ope|kup|bvo|han| bu|pan|ame|vom|ama| ya|siy| am|rez|u n|zid|men|osa|ao |pez|i a| kw| on|u o|lac|ezo|aka|nda|hun|u d|ank|diz|ina|its|adz| kh|ne |nik|e p|o o|ku |phu|eka| un|eze|mol|ma | ad|pat|oma|ets|wez|kwe|kho|ya |izo|sa |o p|kus|oci|khu|okh|ans|awi|izi|zi |ndu|iza|no |say| si|i u|aik|jir|ats|ogw|du |mak|ukw|nji|mai|ja |sam|ika|aph|sid|isa|amb|ula|osi|haw|u m| zi|oye|lok|win|lal|ani| ba|si | yo|e o|opa|ha |map|emb",
    "qug": "una|ta | ka|na |ka |ash|cha|a k|ari|ish|kun|kta|ana|pak|hka|shk|apa|mi |ach|hay|akt|shp|man|ak | ch| ha|rin|ata|tak|lla|ita|ami|ama|aku|har| pa|pas|ayñ|yñi|ina| ma| ru|uku|sh |hpa|run|all|kuy|aka|an | tu|tuk|yta|chi|chu|a c|ñit|in |nak|a h|nka|ris|tap|kan| ki|ayt|pi | sh|pa |i k|a p|nap|kam|kaw|pay|nam|ayp|aws|iri|wsa|a s|ank|nta|uy |a t|hin|a m|ay | li|ant|lia|kay|nat|a r|shi|iak|lak|uya| wa|yuy|say|kis|y r|ypa|hun|a a| yu|n t|tam| ti|yay|n k| ya|a w|hpi|lli| al|api|yku|un |ipa|a i|iku|ayk|shu| sa|ush|pir|ich|kat|hu |huk| il|ill|kas|a y|rik|yac|a l| ku|kac|hik|tan|wan|ypi|ink|ika| ni|ila|ima|i c|yll|ayl| wi|mac|nis| ta|i y|kus|tin|n s|i p|yan|llu|la |iks|tik|kpi| pi|awa|may|lan|li | ri|kll|yas|kin|kak|aya|ksi|k h|aym|war|ura| ay|lat|ukt|i t|iya|ull|mas|sha|kir|uch|h k|nch|akp|uma|pip|han|kik|iki|riy|aki| ii|i s|n p|h m|kar|nal|y h|tac| su|nac|mak|n m|nki|k a|mam|iwa|k t|k k|i m|yma| ña|wil|asi|nmi|kap|pal|sam|pam|k i|k l|i i|pan|sum|i w| hu|his| mu|iia|mun|k m|u t|pik|was|ik |ma |hat|k r|akl|huc| im|mal|uyk|imi|n y|anc|y k|a n|iñi| iñ|wak|unk|yka| mi|iña|a u|has|ywa| ak|llp|ian|ha |tar|rmi|i a|arm|las|ati|pur|sak|ayw|hap|yar|uti|si |iyt|uri|kim| ar|san|h p|akk|iy |wat|wpa|y i|u k",
    "kin": "ra | ku| mu|se |a k|ntu|nga|tu |umu|ye |li | um|mun|unt|a n|ira| n |ere|wa |we | gu|mu |ko |a b|e n|o k|e a|a u|a a|u b|e k|ose|uli|aba|ro | ab|gom|e b|ba |ugu| ag|omb|ang| ib|eng|mba|o a|gu | ub|ama| by| bu|za |ihu|ga |e u|o b| ba|kwi|hug|ash|ren|yo |ndi|e i| ka| ak| cy|iye| bi|ora|re |gih|igi|ban|ubu| nt| kw|di |gan|a g|a m|aka|nta|aga| am|a i|ku |iro|i m|ta |ka |ago|byo|ali|and|ibi|na |uba|ili| bw|sha|cya|u m|yan|o n| ig|ese|no |obo|ana|ish|kan|sho| we|era|ya |aci|wes|ura|i a|uko|e m|n a|o i|kub|uru|hob|ber|ran|bor| im|ure|u w|wo |cir|gac|ani|bur|u a|o m|ush| no|e y| y |rwa|eke|nge|ara|wiy|uga|zo |ne |ho |bwa|yos|anz|aha|ind|mwe|teg|ege|are|ze |n i|rag|ane|u n|ge |mo |u k|bul| uk|bwo|bye|iza|age|ngo|u g|gir|ger|zir|kug|ite|bah| al| ki|uha|go |mul|ugo|n u|tan|guh|y i| ry|gar|bih|iki|atu|ha |mbe|bat|o g|akw|iby|imi|kim|ate|abo|e c|aho|o u|eye|tur|kir| ni|je |bo |ata|u u| ng|shy|a s|gek| ru|iko| bo|bos|i i| gi|nir|i n|gus|eza|nzi|i b|kur| ya|o r|ung|rez|ugi|ngi|nya| se|mat|eko|o y| in|uki| as|any|bis|ako|gaz|imw|rer|bak|ige|mug|ing|byi|kor|eme|nu | at|bit| ik|hin|ire|kar|shi|yem|yam| yi|gen|tse|ets|ihe|hak|ubi|key|rek|icy| na|bag|yer| ic|eze|awe|but|irw| ur|fit|ruk|ubw|rya|uka|afi",
    "zul": "nge|oku|lo | ng|a n|ung|nga|le |lun| no|elo|wa |la |e n|ele|ntu|gel|tu |we |ngo| um|e u|thi|uth|ke |hi |lek|ni |ezi| ku|ma |nom|o n|pha|gok|nke|onk|a u|nel|ulu|oma|o e|o l|kwe|unt|ang|lul|kul| uk|a k|eni|uku|hla| ne| wo|mun| lo|kel|ama|ath|umu|ho |ela|lwa|won|zwe|ban|elw|ule|a i| un|ana|une|lok|ing|elu|wen|aka|tho|aba| kw|gan|ko |ala|enz|o y|khe|akh|thu|u u|na |enk|kho|a e|zin|gen|i n|kun|alu|mal|lel|e k|nku|e a|eko| na|kat|lan|he |hak| ez|o a|kwa|o o|ayo|okw|kut|kub|lwe| em|yo |nzi|ane|obu| ok|eth|het|ise|so |ile|nok| ba|ben|eki|nye|ike|i k|isi| is|aph|esi|nhl|mph| ab|fan|e i|isa| ye|nen|ini|ga |zi |fut| fu|uba|ukh|ka |ant|uhl|hol|ba |and|do |kuk|abe|za |nda| ya|e w|kil|the| im|eke|a a|olo|sa |olu|ith|kuh|o u|ye |nis| in|ekh|e e| ak|i w|any|khu|eng|eli|yok|ne |no |ume|ndl|iph|amb|emp| ko|i i| le|isw|zo |a o|emi|uny|mel|eka|mth|uph|ndo|vik| yo|hlo|alo|kuf|yen|enh|o w|nay|lin|hul|ezw|ind|eze|ebe|kan|kuz|phe|kug|nez|ake|nya|wez|wam|seb|ufa|bo |din|ahl|azw|fun|yez|und|a l|li |bus|ale|ula|kuq|ola|izi|ink|i e|da |nan|ase|phi|ano|nem|hel|a y|hut|kis|kup|swa|han|ili|mbi|kuv|o k|kek|omp|pho|kol|i u|oko|izw|lon|e l| el|uke|kus|kom|ulo|zis|hun|nje|lak|u n|huk|sek|ham| ol|ani|o i|ubu|mba| am",
    "swe": " oc|och|ch |er |ing|för|tt |ar |en |ätt|nde| fö|rät|ill|et |and| rä| en| ti| de|til|het|ll |de |om |var|lig|gen| fr|ell|ska|nin|ng |ter| ha|as | in|ka |att|lle|der|sam| i |und|lla|ghe|fri|all|ens|ete|na |ler| at|ör |den| el|av | av| so|igh|r h|nva|ga |r r|env|la |tig|nsk|iga|har|t a|som|tti| ut|ion|t t|a s|nge|ns |a f|r s|män|a o| sk| si|rna|isk|an | st|är |ra | vi| al|t f| sa|a r|ati| är| me| be|n s| an|tio|nna|lan|ern|t e|med| va|ig |äns| åt|sta|ta |nat| un|kli|ten| gr|vis|äll| la|one|han|änd|t s|stä|t i|ner|ans|gru| ge|ver| må| li|lik|ihe|ers|rih|r a| re|må |sni|n f|t o| mä| na|r e|ri |ad |ent|kla|det| vä|run|rkl|da |h r|upp|dra|rin|igt|dig|n e|erk|kap|tta|ed |d f|ran|e s|tan|uta|nom|lar|gt |s f| på| om|kte|lin|r u|vid|g o|änn|erv|ika|ari|a i|lag|rvi|id |r o|s s|vil|r m|örk|ot |ndl|str|els|ro |a m|mot| mo|i o|på |r d|on |del|isn|sky|e m|ras| hä|r f|i s|a n|nad|n o|gan|tni|era|ärd|a d|täl|ber|nga|r i|enn|nd |n a| up|sin|dd |örs|je |itt|kal|n m|amt|n i|kil|lse|ski|nas|end|s e| så|inn|tat|per|t v|arj|e f|l a|rel|t b|int|tet|g a|öra|l v|kyd|ydd|rje| fa|bet|se |t l|lit|sa |när|häl|l s|ndr|nis|yck|h a|llm|lke|h f|arb|lmä|nda|bar|ckl|v s|rän|gar|tra|re |ege|r g|ara|ess|d e|vär|mt |ap ",
    "lin": "na | na| ya|ya |a m| mo|a b|to | ko| bo|li |o n| li|i n| pe|i y|a y|a n|ngo|ki | ba| ma|kok|pe |la |a l|zal|oki|ali|nso|oto|ala|ons|so |mot|a k|nyo|eng|kol|go |nge| ny|yon|o e|ang|eko|te |o y|oko|olo|ma |iko|a e|e m|e b|lik|ko |o a|ako|ong| ye|mak|ye |isa| ek|si |lo |aza|sal|ama| te|bat|o p|oyo|e n| az|a p|ani|sen|o m|ela|ta |amb|i k|ban|ni | es|yo |mi |mba|osa| oy|aka|lis|i p|eli|a t|mok|i m|ba |mbo| to| mi|isi|bok|lon|ato|ing|o b| nd|ota|bot| ez|ge |nga|eza|o t|nde|ka |bo |gel|kan|e k|lam|sa |ese|koz| po|den|ga |oba|omb|oli|yan|kop|bon|mos|e e|kob|oka|kos|bik|lin|po |e a| lo| bi|kot|‘te|ngi|sam| ‘t|omi|e y|ti |i b| el|elo|som|lok|esa|gom|ate|kam|i t|ika|a s|ata|kat|ati|wa |ope|oza|iki|i e| ka|bom|tal|o l|bek|zwa|oke|pes| se|bos|o o|ola|bak|lak|mis|omo|oso|nza| at|nda|bal|ndi|mu |mob|osu|e t|asi|bis|ase|i l|ele|sus|usu|su |ozw|and|mol|tel|lib|mbi|ami| nz|ne |ene|kel|aye|emb|yeb|nis|gi |obo|le |kum|mal|wan|a ‘|pon| ep|baz|tan|sem|nya|e l| ta|gis|opo|ana|ina|tin|obe| ti|san| ak|mab|bol|oku|u y|mat|oti|bas|ote|mib|ebi|a o|da |bi | mb|lel|tey|ibe|eta|boy|umb|e p|eni|za |be |mbe|bwa|ike|se | et|ibo|eba|ale|yok|kom| en|i a|mik|ben|i o| so|gob|bu |son|sol|sik|ime|eso|abo| as|kon|eya|mel",
    "som": " ka|ay |ka |an |uu |oo |da |yo |aha| iy|ada|aan|iyo|a i| wa| in|sha| ah| u |a a| qo|ama| la|hay|ga |ma |aad| dh| xa|ah |qof|in | da|a d|aa |iya|a s|a w| si| oo|isa|yah|eey|xaq|ku | le|lee| ku|u l|la |taa| ma|q u|dha|y i|ta |aq |eya|sta|ast|a k|of |ha |u x|kas|wux| wu|doo|sa |ara|wax|uxu| am|xuu|inu|nuu|a x|iis|ala|a q|ro |maa|o a| qa|nay|o i| sh| aa|kal|loo| lo|le |a u| xo| xu|o x|f k| ba|ana|o d| uu|iga|a l|yad|dii|yaa|si |a m|gu |ale|u d|ash|ima|adk|do |aas| ca|o m|lag|san|dka|xor|adi|add| so|o k| is|lo | mi|aqa|na | fa|soo|baa| he|kar|mid|dad|rka|had|iin|a o|aro|ado|aar|u k|qaa| ha|ad |nta|o h|har|axa|quu| sa|n k| ay|mad|u s| ga|eed|aga|dda|hii|aal|haa|n l|daa|xuq|o q|o s|uqu|uuq|aya|i k|hel|id |n i| ee|nka| ho|ina|waa|dan|nim|elo|agu|ihi|naa|mar|ark|saa|riy|rri|qda|uqd| bu|ax |a h|o w|ya |ays|gga|ee |ank| no|n s|oon|u h|n a|ab |haq|iri|o l| gu|uur|lka|laa|u a|ida|int|lad|aam|ood|ofk|dhi|dah|orr|eli| xi|ysa|arc|rci|to |yih|ool|kii|h q|a f| ug|ayn|asa| ge|sho|n x|siy|ido|a g|gel|ami|hoo|i a|jee|n q|agg|al | di| ta|e u|o u| ji|goo|a c|sag|alk|aba|sig| mu|caa|aqo|u q|ooc|oob|bar|ii |ra |a b|ago|xir|aaq| ci|dal|oba|mo |iir|hor|fal|qan| du|dar|ari|uma|d k|ban|y d|qar|ugu| ya|xay|a j",
    "hms": "ang|gd |ngd|ib | na|nan|ex |id | ji|ad |eb |nl |b n|d n| li|ud |jid| le|leb| ga|ot |anl|aot|d g|l l|b l| me|ob |x n|gs |ngs|mex|nd |d d| ne|jan|ul | ni|nja| nj| gu| zh|lib|l n|ong| gh|gao|b j|b g|nb |l g|end|gan| ad| je|jex|ngb|gb |han|el | sh| da|ub |d j|d l|t n| nh|nha|b m|is |d z|x g| ya|oul|l j| wu|she|il |nex| ch|b y|d s|gue|gho|uel|wud|d y| gi|d b|hob|nis|s g| zi| yo|lie|es |nx |it |aob|gia|ies| de|eib|you| ba| hu|ian|zib|d m|s j|oud|b d|chu|ol |ut | do|t j|nen|hud|at |s n|hen|iad|ab |enl| go|dao| mi|t g|zha|b z|enb|x j| ze|eit|hei|d c|nt |b s| se|al | xi|inl|hao| re| fa|d h|gua|yad|ren| ho|anb|gx |ngx|ix |nib|x z|and|b h|b w|fal| xa|d x|t l|x m|don|gou|bao|ant|s z|had|d p|yan|anx|l d|zhe|hib| pu|ox | du|hui|sen|uib|uan|lil|dan|s m| di| we|gha|xin|b x|od |zhi|pud| ju| ng|oub|xan| ge|t z|hub|t h|hol|t m|jil|hea|x l| ma|eud|jul|enx|l z|l s|b a| lo| he|nga|d r|zen| yi|did|hon|zho|gt |heb|ngt|os |d a|s l|aos| si|dei|dud|b b|geu|wei|d w|x c|x b|d k|dou|l h|lou| bi|x a|x d|b c| sa|s a| bo|eut|blo| bl|nia|lol|t w|bad|aod| qi|ax |deb| ja|eab| nd|x s|can|pao| pa|gl |ngl|che|sat|s y|l m|t s|b f|heu|s w| to|lia| ca|aox|unb|ghu|ux | cu|d f|inb|iel| pi|jib|t p|x x|zei|eul|l t|l y|min|dad",
    "ilo": "ti |iti|an |nga|ga | ng| pa| it|en | ka| ke| ma|ana| a | ti|pan|ken|agi|ang|a n|a k|aya|gan|n a|int|lin|ali|n t|a m|dag|git|a a|i p|teg|a p| na|nte|man|awa|kal|da |ng |ega|ada|way|nag|n i| da|na |i k|sa |n k|ysa|n n|no |a i|al |add|aba| me|i a|eys|nna|dda|ngg|mey| sa|pag|ann|ya |gal| ba|mai| tu|gga|kad|i s|yan|ung|nak|tun|wen|aan|nan|aka| ad|enn| ag|asa| we|yaw|i n|wan|nno|ata| ta|l m|i t|ami|a t| si|ong|apa|kas|li |i m|ina| an|aki|ay |n d|ala|gpa|a s|g k|ara|et |n p|at |ili|eng|mak|ika|ama|dad|nai|g i|ipa|in | aw|toy|oy |ao |yon|ag |on |aen|ta |ani|ily|bab|tao|ket|lya|sin|aik| ki|bal|oma|agp|ngi|a d|y n|iwa|o k|kin|naa|uma|daa|o t|gil|bae|i i|g a|mil| am| um|aga|kab|pad|ram|ags|syo|ar |ida|yto|i b|gim|sab|ino|n w| wa| de|a b|nia|dey|n m|o n|min|nom|asi|tan|aar|eg |agt|san|pap|eyt|iam|i e|saa|sal|pam|bag|nat|ak |sap|ed |gsa|lak|t n|ari|i u| gi|o p|nay|kan|t k|sia|aw |g n|day|i l|kit|uka|lan|i d|aib|pak|imo|y a|ias|mon|ma | li|den|i g|to |dum|sta|apu|o i|ubo|ged|lub|agb|pul|bia|i w|ita|asy|mid|umi|abi|akd|kar|kap|kai| ar|gin|kni| id|ban|bas|ad |bon|agk|nib|o m|ibi|ing|ran|kda|din|abs|iba|akn|nnu|t i|isu|o a|aip|as |inn|sar| la|maa|nto|amm|idi|g t|ulo|lal|bsa|waw|kip|w k|ura|d n|y i",
    "uig": "ish| he|ini|ing|nin|gha|ng |ili| we|we |sh |in | bo|quq|oqu|ni |hoq| ho|ush|shi|lik|qil|bol|shq|en |lis|qa |hqa|n b|hem| qi|ki |dem|iy | ad|ade|igh|e a|em |han|liq|et |ge |uq |nda|din| te| bi|idi|let|qan|nli|ige|ash|tin|ha |kin|iki|her|de | er| ba|and|iti|olu|an | dö|döl|aq |luq| ya|me |lus|öle|mme|emm| qa|daq|rki|lgh|erq|erk|shk|esh|rqa|iq |uqi|ile|rim|i w|er |ik |yak|aki|ara|a h| be|men| ar|du |shu|uql|hri|hi |qlu|q h|inl|lar|da |i b|ime| as|ler|etl|nis| öz|ehr|lin|e q|ar |ila| mu|len| me|qi |asi|beh|a b|ayd|q a|bir|bil| sh|che|rli|ke |bar|hke|yet|éli|shl|tni|u h|ek |may|e b| ké|h h| ig|ydu|isi|ali|hli|k h| qo|iri|emd|ari|e h|ida|e t|tle|rni| al|siy|lid|olm|iye|anl| tu|iqi|lma|ip |mde|e e|tur|a i|uru|i k|raw|hu |mus|kil| is|i a|ir |éti|r b|özi|ris|asa|i h|sas| je|he | ch|qig|bas|n q|alg|ett|les| xi|tid| él|tes|ti |awa|ima|nun|a a| xe| bu|hil|n h| xa|adi|dig|anu|uni|mni| sa|arl|rek|ére| hö|kér| ji|min|i q|tis|rqi| iy|elq|xel|p q| qe|y i|i s|lig| ma|iya|i y|siz|ani| ki|qti| de|q w|emn|met|jin|niy|i i|tim|irl| ti|rin|éri|i d|ati|si |tew|i t|tli|eli|e m|rus|oli|ami|gen|ide|ina|chi|dil|nay|ken|ern|n w| to|ayi| ij|elg|she|tti|arq|hek|e i|n a|zin|r a|ijt|g b|atn|qar|his|uch|lim|hki|dik",
    "hat": "ou |an | li|on |wa |yon| po|li |pou|te | yo|oun| mo|un |mou|ak | na|en |n p|nan|tou|syo| dw| to|yo | fè|dwa| ak| ki|ki | pa| sa|out| la| ko| ge|ut |n s|gen| de|se |asy|èt |i p|n d| a | so|n l|a a|fè |n k| se|pa |e d|u l| re|ite|sa | ch|kon|n n|e l|t p|ni |cha|a p|nn |ans|pi |t m| ka| an|nm |fèt|i s|son|man| me|n m|n a|e p|swa|sou|e k|hak|òt |n y|men|i l|epi| pe|ote|san| ep|i k| si|yen|eyi|a l| ap|i a|yi |pey|je |n t|e a|k m|e s| ni|lib|e n|i t|lit|ran|lè |enn|al |a s| pr|a f|ns | lò|ap |lòt|enm|k l|n e|t l|kla|anm|e y|a k| ma|e t|ay |i m|ali| lè|è a|ye |a y|ant| os| ba|i g| tè|aso|u t|a n| pw|ras| pè|n f|nas|ka |n g|osw| ta|dek|i d|pwo|e m| di| vi|la |i n|u s|sos|bli| te|o t| tr|lwa|ète|a t|le |u y|i f|tan|a c|lar|a m|ete|ara|t k| pi|ibè|bèt|re |osy|de |ati|ke |res|tis|i y|tè |nen| fa|ekl|ze |nal|ons|ksy|ini|che| le|e r|a d| en|aye|he |o p|alw| kò|lal| no|esp|a g|ava|kou|las|way|u f|isy| za| ok|oke|kal|ken|sye|ta |onn|k k|nje|pra|van|esi|pès|kot|ret|sya|n v|lek|jan|ik |a b|eks|wot|è n|di |òl |tra|u k|i r|nou| as|k a|u d|ist|èso|ib | ne|iti|ti |is |y a|des|è l|a r|ont| ke|nsa|pat|rit|sit|pòt|ona|ab |è s| sw|ond|ide| ja|rav|t a|ri |bon|viv| sè|pre|vay|k p|l l|kòm|i o| ra|era|fan|dev",
    "aka": "sɛ |a a| sɛ|ne |ra |a n| wɔ| a |ara|an |eɛ |no | ne| bi| no| as|iar|bia|yɛ |mu |aa | an|ɛ s|e a|ma | ho|bi |man|deɛ| mu|ho |ɛ a|na |a ɛ| ob|obi|e n|a b|n a|so |o n|pa |ama|ɛ o|o a|ipa|nip|ɛ n|naa| na|a w|ana| so| ad| nn|ɛ ɔ|ɛde|asɛ|kwa| on|oni|wan| am|a ɔ|sɛd|wɔ | ah|ɛyɛ| ny|oɔ | n |mma|i a| mm|nni| kw|ie |wɔn|ɛ w|de | ɛy| ba|ase|ɔ n|o b|i m|ɔ a|uo |n n|a m|o s|iri| yi|ni |e s|nyi|di |u n|a o|aho| de|tum| ɛn|ɔn |nya|i n|ɔma|e m|adw| yɛ|umi|die|mi |ɛ ɛ|o k| ab|ɛm |a s| ma|nam| ɔm| ɛs|yin| at| bɔ|o d|ina|pɛ |sɛm|ua |n s|bɔ |adi|ya |e h|aso|mar|ani|kuo|rɛ |fa |a k|ɔde|a h|ba |n b|re |uma|wum|om |ɔ h|m n|yi |u a| sa|se |dwu|ɔ b| nt|m a|erɛ| kɔ|a y|orɔ| nk| bɛ| ɔd|ten|rɔ |hyɛ|saa|ka |ɛ b|e b|i s|ade|am |nka|kor|i ɛ|ene|ena| ns|ban|ɛns| ku|ɛsɛ|ane|nsɛ|fof|ɛɛ | fi|gye|ɔtu| di|ano|i k|o m| ɔt| ko|yɛɛ|bir| ak|im |kye| pɛ|a d|yie|ko |nti|i b|ete|ofo|amm|ye |ri |foɔ|kɔ |bom|abo|ɔ s|ɔne| ɛb|soɔ|for|isɛ|m k|asa|nod|ɛ m|fir|ti | da|e y|sua| be|nii|seɛ|wa |ber| aw|dwe|n f| fo|o ɛ|i h|u b|ɔ m| mf|hɔ |kab|wɛ |to |rib|hwɛ|ibi| dw|dis|nso|ans|tir|u ɛ| ti| hɔ|sa |e o| tu|odi|ɛ y|ia |ofa| ɔn|o w|ɛbɛ|aba| ka|ii |wen|ɛsi|m m|sia|ada|yer|ian|da |set| gy|dua|i d|som|mfa|ɔ w| af|i y|any|ora|rim|wɔd|dwa|nsi",
    "hil": "nga|ang| ka|ga |ng | sa|an |sa | ng| pa| ma|ag |on |san|pag| an|ung|kag|a p|n s|a k|n n|a m|ata|kat| ta|gan|g p|ay |tar|g k|ags|run|ala|aru|gsa|tag|a s|g m| mg|mga|n k|a t|od |kon|g s|a n|ing|a i|man|g t|agp|tan| si|n a|y k|mag|gpa|may|hil|pan|ya |ahi|la |g a|sin|gin|ina|aya|ana|ili| pu|han|g i|yon|nan| in|way|uko|gka| gi|aha| uk|ilw|lwa|asa|apa|kas|syo|at |ban|lin|iya|kah|n p| na|o n|lan|a a|in |ngk|g n|ini|aba|pat|pun|a g|ali|o s| iy|yan|agt|tao|ngs|gba|kab|wal|ngo|al |nag|agk|o m|ni |i s|aga|ano| wa|isa|abu|kal|a h|dap|ong|a d|mat| tu|gso|no |aho|aki|sod|agb| da|asy|ila|d k|pas| hi|agh|d s|n m|na |lal|yo |di |til| la|o k|s n|non|gay|sal|a b|god|ao |ati|aan|uha| is|ka |aka|asu|ngb|o a|ama|ato|atu|uga|paa|but|una|n u|bah|uan|iba| di| ba|pah|bat| du|ulo|os |y s|nah| ko|aag|agi|sil|gi |i m|hay|yag|gon|y n|sta|n d|ot |oha|tun|ida| pr| su|a l|uta|m s| al|do |uli|sug|n t|as |lon|sul|og |pam|pro|him|gua|alo|lig| bi|bis|asi|ula|ton|ksy|gtu|a e|k s| ib|n b|maa|ugu|ko |lib|ron|i a|hi |hin|tek|lab|abi|ika|mak|bot|aoh|ok | hu|ghi|ind|ote|tok|i n|t n|g e|eks|dal|uma|ubo|tum|hat|to |ado|kin| ed|rot|ho |ndi|inu|ibu|y a|nta|ad |gko|lah|duk|abo|iko|nda|aro|gal|mo |g o| bu|int| o |n o|aay|da |gsu",
    "sna": "wa |a k|ana|ro |na | ku| mu|nhu|dze|hu |a m| zv|mun|oku|chi|a n|aka|dzi|ka |zer|ero| ch|che|se |unh|odz|rwa|ra |kod|zvi| ne| pa|kan| we| dz| no|ika|va |iri| an|kut|nyi|o y|yik|van|nek|ese|eko|zva|idz|e a| ka|ane|ano|ngu|eku|cha|ung| yo|ri |ake|ke |ach|udz|iro|a z|u w| va|ira|wes|ang|ech|nge|i p|eng|yok|nok|edz|o i|irw|ani|ino|uva|ich|nga|ti |zir|anh|rir|ko |dza|o n|wan|wo |tan|sun|ipi|dzw|eny|asi|hen|zve|kur|vak|a p|sha|unu|zwa|ita|kwa|e k|rud|nun|uru|guk|a c|a d| ya|a y|bat|pas|ezv|ta |e n|uti| kw|o k|o c|o m|ara| ma|si |ga |uko|ata|ose|ema|dzo|uch|hip|kuv|no |rus|hec|omu|i z|wak|o r|kus|kwe|ere|re | rw| po|o a|mwe|yak|mo |usu|isi|za |sa |e z|uta|gar| in|hin|nem|pac|kuc|we |ete| ye|twa|pos|o d|a i|hur|get|ari|ong|pan|erw|uka|rwo|vo | ak|tem|zo |emu|emo|oru| ha|uit|wen|uye|kui| uy|vin|hak|kub|i m|a a|kud| se| ko|yo |and|da |nor|sin|uba|a s|a u| ic|zvo|mut|mat|nez|e m|a w|adz|ura|eva|ava|pi |a r|era|ute|oko|vis| iy|ha |u a|han|cho|aru|asa|fan|aan|pir|ina|guv|ush|ton| hu|uny|enz|ran|yor|ted|ait|hek| ny|uri|hok|nen|osh| ac|ngi|muk|ngo|o z|azv|kun|nid|uma|i h|vem|a h|mir|usa|o p|i n|a v|i k|amb|zan|nza|kuz|zi |kak|ing|u v|ngw|mum|mba|nir|sar|ewo|e p|uwa|vic|i i|gwa|aga|ama|go |yew|pam",
    "xho": "lo |lun|oku|nge|elo|ntu|tu |e n|ele| ku|nye|ye |nga|ung|la | ng|lek|a n|o n|yo |o l|e u|nel|gel|a k|ko |ho |ulu|ke | ne| na|lul|we |le |wa |ngo| kw|ule|kub| no|a u|onk| um|nke|o e| lo|ela|kun|ama|any|unt|ang|eko|uba|elu|ezi|mnt| wo|a i|eyo|alu|lel|umn|lwa|kwe|olu|ba | uk|kuk|won|ukh|une|uku|gok|nok|enz| un|khu| ok|the|e k|zwe|kan|eki|aph|ane|uny|ile|o z|aku|ley|lok| ez|het|eth|ath|oka|pha|sel|ala|o y|kul|akh|kil|enk| in|esi|o k| yo|use|hul|u u|tho|obu|wen|ana|nku|khe|o o|e a|na |kho|ban|a e|ise|ent|gan|uth|ni |kel| zo|he |izw|o w|hi |elw|nam|ing|eli|fun|za |lwe|eng|ya |kwa|fan|isa|o a|ndl|ntl|ayo|eni|gen|hus|uhl|iph|tha|nzi|isw|sa |phi|aba|ben|und|ume|thi|ha |alo|ka |ink|hla|lal|wan|i k| lw|i n|bel| ba|o u|azi|e o|swa|ngu|bal|pho| ab|man|kut|emf|e i|mfa|a a|e e|een|int|uph|eka|ebe|seb|lan|nee|zi |o i|mal|sha|sek|dle|ziz|mth|nen|zel| se|okw|tya|ike|lin|tla|ene|sis|ima|ase|yal|ubu| ak|ant|sen|olo|wak| ko|a o|mfu|ezo|sid|nay|oko| ub|ulo|zo |do |isi|wez|iso|han|nte| ph|zim| ya|ga |li | le|iba|ham|ube|kup|aza|jik| ul| en|eem|phu| ol|and|imf| es|o s| im|kuf|u k|kwi|nak|ma |nan|ety|kuh|kus|yol| am|hel|idi| so|lis| nj|nje|jen|tsh|aka|zin|kuz|‐ji|no |ufu|ale|ong| el|bo |a y|e l|men|yen|lum",
    "min": "an |ak |ang| ma| da| ka| sa|ara| ha|yo |nyo|hak| ba|ran|dan|man|nan|ng | pa| di|kan|ura| na|ata|asa|ok |nda|ala| pu|pun|uak|ntu|n d|k m| ti|ah |o h|n s|k u|n k| ur| un|tua|n b|and|unt| ta|uny|n p|tio|iok|ama|pan|ek |ban|jo |n m|k h|k d|ado|nga|aan|g p|tan|aka|ind|at |dak|dap|o p|tau|pek|uan| at|amo|mar|ape|au |kat|mo |sas|ari|asi|di |o s|ia |ngg|bas|ika|sam|am |lia|o d|san|gan|sia|tar|n n| jo| su|anu|lam|gar|o t| in|par|sua|dek|sar|k s|ri |o m|ana|bat|asu|ko |ai | la|ant|dal|lak|aga|alu|iah|o u|n a|tu |k a|adi|rad|i m|mal|dok|usi|aku|i d|k k|al |aro|eka|neg|ega|ato|to | ne|mam|o b|eba|ian|beb|n u|um |si |aba|rat|uah|ro |mas|ila|a d|ali|uka|ard|kam|ti |atu|nus|dar|ami|n t|sa |in |amp|kal|car|lan|aha|kab|so |rde|un |i k|gsa|das|ngs|aca|yar|ka |ati|ar | an|uku|ras| ko|sya|mat|k n|aya|nta|lo |any|sur|kaa|dil|kar|o a|u d|k t|pam|dia|ra |iba|lai|i t|lah| bu|mpa|kum|abe|n h|ili|nny| as|u p|aki|amb|sac|as |k b|h d|uli|ajo|a n|raj|n i|dua|ndu|k p|i p|itu|lin|han|huk|o k|rik|a b| li|ik |ggu|jam|bai|a a|i a|nia| ad|i j| hu|gam|sal|aso|ngk|sad|apa|ann| mu|ony|dik|bad|ain|did|min|l d|ada|bul|rga|tin|ga |ani|alo| de|arg|ahn|sio|hny|n l|sti|awa|uju|per|bak| pe|tik|ans| pi|a s| um|bag|ndi|anj|mba",
    "afr": "ie |die|en | di| en|an |ing|ng |van| va|te |e v|reg| re|n d| ge|ens|et |e r|e e| te| be|le |ver|een| in|ke | ve| he|eg |het|lke|lik|n h|de |nie|aan|t d|id |men| vr|nde|eid|e o| aa|in |of |der|hei|om |g v| op| ni|e b| el|al |and|elk|er | me|ord|e w|g t| to| of|ers| we| sa| vo|ot |erk|n v|vry|ge |kee|asi|tot| wa|sie|ere| om|aar|sal|dig|wor|egt|gte|rdi|rd |at |nd |e s|ede|ige| de| ’n|n a|eni| wo|e g| on|n s|’n |e t|erd|ns |oor|bes|ond|se |ska|aak|nig|lle|yhe|ryh|is |eli|esk|ien|sta|vol|ele|e m| vi|ik |r d|vir|edi|kap|g e|ir |es |sy |ang|din| st|ewe|gem|gel|g o| is|el |e i|op |ker|ak |uit|ike|nse|hie|ur |eur| al|e a|nas|e n|nge|ier|n o|wer|e d|ap | hu|ale|rin| hi|eme|deu|min|wat|n e|s o| as| so|as |e h|del|d v|ter|ten|gin|end|kin|it | da| sy|per|re |n w|ges|wet|ger|e k|oed|s v|nte|s e|ona|nal|waa|d t|ees|soo| ma|d s|ies|tel|ema|d e|red|ite| na|ske|ely|lyk|ren|nsk|d o|oon|t e|eke|esi|ese|eri|hul| gr|ig |sio|man|rde|ion|n b|n g|voo|hed|ind|tee| pe|rso|t v|s d|all|n t|rse|n i|eem|d w|ort|ndi|daa|maa|t g|erm|ont|ent|ans|ame|yke|ari|n m|lan|voe|n ’|nli|rkl|r m|sia|ods|ard|iem|g s|wee|r e|l g|taa|sek|bar|gti|n n|lin|sen|t o|t a|raa|ene|opv|pvo|ete| ty|arb| sl|igh|dee|g a|str|nsl|sel|ern|ste",
    "lua": "ne |wa | ne|a m| ku|a k| mu|di | bu|a b| di|e b|tu |nga|bwa|ntu| bw|udi|a d|e m|i b| ba| ma|shi|adi|u b|a n|la |ons|mun|i n|ung|nsu|ga |yi |ya |na |unt| dy|idi|e k|buk|mu |ika|esh|su |u m|ku |nde|any| bi|lu |nyi|end|yon|dik|ba | ci| ka|ang|u n|u y| mw|ka |i m| yo|we |oke|tun|de |kes|hi |kok|mwa| kw|e n|ban|dya|sha|u d|ken|kwa|ji |ha |wen|dit| ud|a a| an|mwe|itu| pa|le | a | wa|nji|kan|kum|ibw|bwe|a c|ant|ena|yen|mba|did|e d|ala|u u|ish|mak|bul|i a|nda|enj|u a|ila|pa |ako|ans|uke|ana|nso|amb|hin|umw|kal|uko|i k|bad|aka|ela|ele|u w|u k|du |ja |bu | mi|ind|ndu|kwi| ns|mbu|atu|bud|dil|ile|sun|eng|ula|enz|nan|nsh|kad|alu| cy|bis|kud|lon|u c|gan|dib|da |dye|bid| by|ukw|i d|aa |ngu|a p|sam|isa| aa|ilu| na|aba|lel|ye |dim|cya|kub|so |ond|kus|mat|nge|e c| bo|aku|bak|mus|ta |umb|ulo|elu|man|iki|mon|ngi|abu|mud|kuk|omb| mo|und|diy|kwe|umu|mal| ke|ush|gil|uba|imu|dis|wil|wu |san|gad|uka|bon|ma |aci|mik|wik| me|pan|iku|nza|ben|ulu|ifu|iba|kak|ata|som|ong|e a|apa| tu|o b|umo|bya|utu|uja|yan| be|ke |akw|ale|ilo|uku|cil|tup|kul|cik|kup|upe|bel|amw|ona| um|iko|awu|and|za |ike|a u|ima|muk| ya|mum|me |map|ita|iye|ole|lum|wab|ane| lu|nu |kis|mbe|kab|ine|bum|lam|pet| ad|fun|ama| mb|isu|upa|ame|u p|ubi",
    "fin": "en |ise|ja |ist| ja|on |ta |sta|an |n j|ais|sen|n o|keu|ike|oik|lis| va|ell|lla|n t|uks| on|ksi| oi|n k| ka|aan|een|la |lli|kai|a j| ta|sa |in |mis| jo|a o|ään|än |sel|n s|kse|a t|a k|tai|us |tta|ans|ssa|kun|den|tä |eus|nen|kan|nsa|apa|all|est| se|eis|ill|ien|see|taa| yh|jok|n y|vap|a v|ttä|oka|n v|ai |itt|aa |aik|ett|tuk|ti |ust| ku|isi|stä|ses| tä| tu|lai|n p|sti|ast|n e|n m|tää|sia|unn|ä j|ude|ä o|ste|si |tei|ine|per|a s|ia |kä |äne| mi|maa| pe|a p|ess|a m|ain|ämä|tam|yht| ju|jul|yks|hän|ä t| hä|utt|ide|et |llä|val|sek|stu|n a|lä |ami|hmi| ke|ikk|lle|iin|sä |euk|täm|ihm|tee| ih|lta|pau| sa|isk|mää|ois|un |tav|ten|dis|hte|n h|iss|ssä|a h|ava| ma|a y| ei| te| si| ol|ekä|sty|alt|toi|att|oll|tet| jä| ra|vat| mu|iel| to|mai|sal|isu|a a|kki|at |suu|n l|väl|ää |uli|tun|tie|eru| yk|etu|vaa|rus|muk| he|ei |a e|kie|sku|eid|iit| su|nna|sil|oma|min| yl|lin|aut|uut|sko| ko|tti|le |sie|kaa|a r| ri|sii|nno|eli|tur|saa|aat|lei|oli|na | la|oon|urv|lma|rva|ite|mie|vas|ä m| ed|tus|iaa|itä|ä v|uol|yle| al|lit|suo|ama|joi|unt|ute|i o|tyk|n r|ali|lii|nee|paa|avi|omi|oit|jen|kää|voi|yhd|ä k| ki|eet|eks| sy|ity|ilö|ilm|oim|ole|sit|ita|uom|vai|usk|ala|hen|ope| pu|auk|pet|oja|i s|rii|uud|hdi|äli|va | om",
    "run": "ra |we |wa | mu|e a|se | n |a k|ira|ntu|tu | ku| um|ko |a i|mu |iri|mun|hir|ye |unt|ing|ash|ere|shi|a n|umu|zwa| bi|gu |ege|a a|za |teg|ama|e k|go |uba|aba|ngo|ora|o a|ish| ba| ar|ung|a m| we|e n|na |sho|ese|nga| ab|e m|mwe|ugu| kw|ndi| gu|ate|kwi|wes|riz|ger|u w| at|di |gih|iza|n u|ngi|ban|yo |ka |e b|a b| am| ca|ara|e i|obo|hob|ri |u b|can|nke|ro |bor| in|bah|ahi|ezw|a u|gir|ke |igi|iki|iwe|rez|ihu|hug|aku|ari|ang|a g|ank|ose|u n|o n|rwa|kan| ak|nta|and|ngu| vy|aka|n i|ran| nt| ub|kun|ata|i n|kur|ana|e u| ko|gin|nye|re | ka|any|ta |uko|amw|iye| zi|ga |ite| ib|aha| ng|era|o b|ako|o i| bu|o k|o u|o z| ig|o m|ho |mak|sha| as| iv|ivy|n a|i b|izw|o y| uk|ubu|aga|ba |kir|vyi|aho| is|nya|gan|uri| it| im|u m|kub|rik|hin|guk|ene|bat|nge|jwe|imi| y |vyo|imw|ani|kug|u a|ina|gek|ham|i i|e c|ze |ush|e y|uru|bur|amb|ibi|agi|uza|zi |eye|u g|gus|i a| nk|no |abi|ha |rah|ber|eme|ras|ura|kiz|ne |tun|ron| zu|ma |gen|wo |zub|w i|kor|zin|wub|ind| gi|y i|ugi|je |iro|mbe| mw|bak| ma|ryo|eka|mat| ic|onk|a z| bo|ika|eko|ihe|ukw|wir|bwa| ry| ha|bwo| ag|umw|yiw|tse| ya|he |eng| ki|nka|bir|ant|aro|gis|ury|twa| yo|bik|rek|ni | ah| bw|uro|mw |tan|i y|nde|ejw| no|zam|puz|ku |y a|a c|bih|ya |mur|utu|eny|uki|bos",
    "slk": " pr| a |prá|ráv| po|ie |ch |ost| ro|ho | na|vo |ani|na | ne|nos|ažd|kto|kaž| ka|má |né |ávo|om | má|ebo|ti | v | al|ale|leb|bo | je| za|ých|o n|ždý|dý |ia | sl|mi |ova|sti|nie|van|to |eni|ne |áva|lob|ého|slo|rod|tor|rov| sp| zá|á p|o v|a p| kt|ý m| sv|voj|bod|obo|nia| ná| vy|ej |je |ať |o p|a v|a s|áro|a z| sa| ma|a n|e a|e s|mu |mie|kla|nár|svo|spo| by|ovn|by |roz|sa |ľud|iť |odn| vš|ov |i a|néh|vše|o s|va |o a| ľu|oci|pre|nu |a m|u a|ený|e v|ný |nes|a k|zák|pod|ným| do|u p| k |u s|áci|ajú|byť|yť |nýc|eho|ran|pol|tát|stn|jeh|a r|šet|ými|lad|čin|ému|a o|edz|ť s|kon|stv|oré| sú| ni|e z|pri|och|ny |štá|sť |oje|vna|tre|u k| či|ko |é p|maj|smi|a a|etk|nak|ým |med|dov|prí| ob|iu |uds|osť|esm|e b|m a|hra|i s|rác|bez|vať|chr|e p| ab|jú | št|žen| ho|čen| de|i p|ť v| vo|dsk|pro|nom| in|ou |du |že |aby|est| bo|ré |bol| so|nú |olo|kej|áln| oc|obe|ky |dzi|dom|áv |por|lne|rav|aké|ens|pra|ok | že|tné| ta|ako|res| vz|i k|ami| tr| ak|ní |len|o d|del|ský|cho|ach|ivo|h p|ože|iál|inn|slu|kra|loč|očn|ju | os|anu|oju|voľ|ákl|str|é s|ené| ži|niu|sta| st|ved|tvo| me|dno|m p|de |ké |kým|ikt|stu|é v|i v|vyh| to|v a|odu|hoc|a t|ím |ly |hov|y s|soc|júc|ú p|odi|vod|liv|aní|ciá| ve|rej|ku |ci |ske|sob|čno|oso",
    "tuk": "lar| we|we | bi|yň |ary|ada|da | he| ha|an |yny|kla|dam|de | ad|yna|er |na | ýa|ir |dyr|iň |bir|r b|ydy|ler|ara|am |yr |ini|lan|r a|kly|lyd| öz|mag|nyň|öz |her|gyn|aga|en |ryn|akl|ala|dan|hak|eri|ne |uku|ar |r h|ga |ny |huk| de|ili|ygy|li |kuk|a h|nda|asy|len| ed|bil|atl|ine|edi|niň|lyg| hu| ga|e h|nde|dil|ryň|aza|zat|a g|‐da|a‐d|eti|ukl| gö|ly | bo|tly|gin| az|lma|ama|hem|dir|ykl|‐de|e d|ile|ýan|a d|ýet|ýa‐|ynd|lyk|aýy|e a|ünd|ge | go|egi|ilm|sy |ni |etm|em‐|lme|m‐d|aly|any| be|tle|syn|rin|y b|let|mak|a w|a ý|den|äge|ra | äh|mäg| du|n e|bol|meg|ele|ň h| et|igi|ň w|im |iýa| ýe| di|r e|ek | ba|ak |esi|ril|a b|in |p b|deň|etl|agy| bu| je|bu |e ö|y d| hi|mez| es|ard| sa|ähl|e b|yly| ka|esa|mek| gu|n a|e t|lik| do|e g|sas|ill|nma|ň a|ram|ola|hal|y w|ýar| ar|anm|mel|iri|siý|ndi|ede|gal|end|mil|rla|göz| ma|n b|e ý|öňü|ňün|n h| tu|hiç|yýe| ge|my |iç | öň|n ý|tla|ň ý|lin|rda|al |lig|gar| mi|i g|dal|rle|mal|kan|gat|tme|sin|and|ň g|gor| ta|öwl|ýle|y g|e w|ora|tiň|ekl| yn|alk|döw| dö|ere|m h| me|dur| er|asi|tut|at |çin|irl|umy|eli|erk|nme|wle|gur|a ö|aýa| çä|nun| ki|ras|aml|up |ýaş|tyn| aý|ry |ň d|baş|ip |gi |z h|kin|z ö|n w|ter|inm|eýl|i ý|kim|nam|eň |beý|dol| se| te|r d|utu|gyý|ez |umu|mum",
    "dan": "er |og | og|der| de|for|en |et |til| fo| ti|ing|de |nde|ret| re|hed|il |lig| ha|lle|den| en|ed |ver|els|und|ar | fr| me|se |lse|and|har|gen|ede|ge |ell|ng |at | af|nne|le |nge|e f|ghe|e o|igh|es |af |enn| at|ler| i |ske|hve|e e|r h|ne |enh|t t|ige|esk| el| be|ig |tig|fri|or |ska|nin|e s|ion| er|nhv|re |men|r o|e a| st|ati| sk| in|l a|tio| på|ett|ens|al |tti|med|r f|om |end|r e|del|g f|ke | so|på |eli|g o| an|r r|ns | al|nat|han| ve|r s|r a| un| he|t f|lin| si|r d|ter|ere|nes|det|e r| ud|ale|sam|ihe|lan|tte|rin|rih|ent|ndl|e m|isk|erk|ans|t s|kal| na|som|hol|lde|ind|e n|ren|n s|ner|kel|old|dig|te |ors|e i| hv|sni|sky|ene|vær| li| sa|s f|d d|ers|ste|nte|mme|ove|e h|nal|ona|ger| gr|age|g a|vil|all|e d|fre|tel|s o|g h|t o|t d|r i|e t| om|arb|d e|ern|r u| væ|d o|res|g t|klæ|øre|n f| vi| må|ven|sk | la|gte|kab|str|n m|rel|e b|run|rbe|bej|t i|ejd|kke|t e|g d|rkl|ilk|gru|ved|bes| da|nd | fu|lær|æri|rdi|ærd|ld |t m|dli|fun|sig| mo|sta|nst|rt |od | ar| op|vis|igt|ære|tet|t a|emm|g e|mod|rho|ie |g u|ker|rem| no|n h| fa|rsk|orm|e u|s s|em |d h| ge|ets|e g|g s|per| et|lem| tr|i s|da |dre|n a|des|dt |kyt|rde|ytt|eri|hen|erv|l e|rvi|ffe|off|isn|r t| of|ken|l h|rke|g i|tal|må |r k|lke|gt |t v|t b",
    "als": "të | të|dhe|he | dh|në |ë d|e t| e |et |ë t|imi|për|ejt|dre|rej| pë| dr| në|it |gji|sht|ve |jit|ë p| gj|ith| sh| i | li|het|e p| nj|t t|ër |ë n|in | ve|me |jtë|e n| ka|ara|e d|ush|n e|tet| pa|jer|hku|a t|re |ën |ë s|sh | ku|së |t d|ë m|kus|mit|lir|ka |ë k|jë |se | si| që| ba|etë|që |ë b|si |ë g|eri|thk|nje|eve|e k|e s|jet|ose|bas|ohe| os|ra | mb|iri|h k|min|shk|ash|rim|ndë| nd|një|jta|e m| me|eti|do | du|es |rë |e l|mi |anë|tar|t n| as|dër|hte|end|tën|vet|uar|und|ësi|kom|tje|duh|ndi|at |ave| ko|ri |ta |ë v|shm| de|ar |omb|i d| kë|i p|jes| ng|uhe|nga|i n|en |ë e|ga | ar|e a|ës |hme|bar| pe|htë|ë l|ur |ë i|isë|ime|sim|ris|tës|art|ëm |cil|tim|tyr|ësh| ma|shë|or |t a|kët|gje| ci|r n|e v|par|nuk|ëta|rgj|i i|ish|uk | nu|ë r|are| je|ë c| pu|atë|lim|lli| ës|ë a|i t|mar|ore| së|tit|lar|per|t p|rat|ite|inë|t s|riu|ke |ërg|a n|edh| pr|esi|irë|ërk| po|hë |ë j|i s|a e|ht |mba|roh|im |ari|e b|lit|ti |asn|tav|snj|t e|ik |tij|k d|qër|hëm|ras|res|otë|nal|mun| an|kla|ven|e q|tat|t i| fa|ij | tj|igj|te |ali|bro| di|roj| ti|uri|ojë|ë q|çdo|det|n p| pl|ekl|ind|erë|vep|dek|nim|ive|ror|sho|hoq|oqë|ëri|pri|r d|shp|esë|le |a d|shi| mu|dis|r t|ete| t |ë f|ëzo|zim| çd|mbr| re|e f|jen|i m|iut|n k|tha|s s|lot",
    "nob": "er | og|og |en | de|for|til|ing|ett| ti|et | ha| fo| re|ret|il |het|lle|ver|tt |ar |nne| en|om |ell|ng |har| me|enn|ter|de |lig| fr| so|r h|ler|av |le |den|and| i | er|som| å |hve|or |t t|ne | el|els|re | av|se |esk|enh|nge|ska|nde|e o|ete|gen|ke |lse|ghe|ten|men| st|r s|fri|igh|ig | be|e e|nhv|r r|tte|ske|te | på| ut| sk|al | in|sjo|på |der|e s|ner|rin|jon|t o|unn|e f|han|asj|tig|ed |es |g f|sam|ent|tti|ene|nes|med|ge | al|r o|ens|r e|eli|isk|lin| ve|nin|g o| sa| an|t f|itt|lik|end|kal|r f|t s|rih|ihe|nas|nte|e r|ns | si|lan|g s|mme|ige|l å|erk|dig| gr|n s|ren|r a|all| na|kte|erd|ere|e m|und|r u|res|tel|ste|gru|inn|lær|ers| un|det|t e|arb|ale|del|ekt|ven|t i|g e|bei|eid|e a|n m|e d| ar|rbe|e g| bl|ans|klæ| li| he|g t|æri|sky|run|rkl| la|sta|sni|kke|m e|rt |mot| mo|e n|tat|at |e h|e b|ove|e t|jen|t d|str| må|r m|n e|ors|rel|ker| et|n a|bes|one| vi|nn |g r|e i|kap|sk |ot |ndi|nnl|i s| da|s o| no|id |ger|g h|vis|n o|bar|s f|ndl|t m|g a|opp|t a|dis|nal|r d|per|dre|ona|ære|rdi|da |ute|nse|bli|ore|tet|rit| op|kra|eri|hol|old| kr|ytt|kyt|ffe|emm|g d|l f| om|isn| gj|å d|ser|r b| di| fa|n t|r k|lt |set| sl|dom|rvi|me |l e|gre|å s|må | tr|nd |m s|g i|ikk|n h| at|tes|vil|dli|g b|d d| hv|rav",
    "suk": "na | mu| bu| na|a b|ya |hu |a n|we | gu|nhu|a g| ba|a m|ili|wa | ya|li |unh| bo|mun|ali|bul|han|bo |i m|ilw|uli|ang|lil|la |i b|e n|ga | wi|kil|mu | al| se|u a|ge |kge|ekg|sek|lwe|ose|le |lo |bi |ulu|e y|kwe|ila|and|e b|i n|yo |ng’|a s|nga| ns|si |abi|nsi|ina|lin|aki|se |ban| ly| gw|dak|lu |ngi|gil|a w|o g|akw|u b|ile|anh|ka |ilo|a l|ubi|e g| nu|o n|ja |gan| ng| ma|lya|nul|g’w|ani|ndi|u m|iya|wiy| ji|jo | ka|yab|lwa|ada|o b|e k| ad|gwi|ho |gub| ku|ing|o a|o l|ula|ika|a i|u n|dik|iha|shi|ayo|gun| ja|ha |biz|o j|lag|ma |wen| sh|ele|ung|o s|gi |gul|mo |lan|iwa|a k|ala|iki|jil|ola|ji |a a|yak| li|nil|iza|agi|aha|man|bos|iga|kuj| ha|ana| lu| gi|iti| mh|uga|uyo|win| ga|za |a y|ki | nd|oma|ene|o w|a u|mah|yos|sol|hay| mi|iko|ong|aga|iku|gwa|i a|ndu|pan|u g|e i| ab|ujo|ida|nya|ibi|duh|but|i y|u w|iji|nhy| we|nik|aya|uhu|nda| il|je |abo|aji|lel|ubu|nay|ba |lug|lon|ale|mil|da |a j|dul|o m|mha|aka|e u|g’h|udu|lyo|e m|e a|gik|bus|bal|sha|wit|twa|ngh|nek|wig| um|okw|any|uma|ima|uso|bud|’we| ij|hil|bil|a h|imo|ita|no | ih|gut|nha|ne |iso|ulo|uno|yom|’ha|u l|elo|eki|wel|hya|ngu|omb|som|mbi|i g|o i|u i|bak| is|ugu| yi|utu|eni|tum|umo|u s|tog|inh|’wi|lit|waj|e j|ule|jiw|u u|kub|kul|lik|uto| uy|upa",
    "sag": "tî | tî|na | na| ng|a n|ngb|gö |ngö|nga|nî | lo|lo |zo |bi |la |gbi|ang| sô|sô |î l|gan|ö t| zo|o n| wa|a t|îng|i t|ngü|gü | al|lîn| nd|a l|ê t| kû|äng|î n| te|wal|ala|alî|î k|ë t|î m|â t|î â|ô a|î b| mb|ûê |gâ |örö|ngâ|kûê| lê|o k|a â|e n|ko |î s| kö|ter|dör|köd|ödö|ï n|a k|lêg|gë |ôko|ëpë|mû |pëp| pë|o a|êgë|eke|yek|ke |ü t|î t| ay|o t|bên|ê n|rê |pëe|ra |ëe |erê|rö |tï |kua|aye| nî| ôk|ua |a z|ä t| âl|â n|ïng|î d|ö n|âng|ênî| am|î z|ten|âla| yâ|ê a|mbê|a m|û n|a y|ne |ene|rä |î g|a s|bê | ku|arä|ndi|ga |diä|ëng|iä | du| ân|amû|dut|öng|yâ |utï|ro |önî|lï |a p| gï|oro|lë |î a| âm|ndo| sê|ngô|do |i n|o s|ndö|âra|e t| bê|gba|ûng| mä|sâr| sï|î p| gb|ö k|e a|yê |a a| âk|dö |ara|ba |ï t| tö|a w|zar|tön|î w|war|ndâ|a g|ana|në |ênd| të|ta |ban| lë|zön|î f|nzö| sâ|sï |tën|o w| nz|sên| âz| da| za|îrî| në|nën|ate|ä s|bâ | at|o l|ënë|o ô|fa | kp| ma|o p| mû|kân|a b|bat|ata|ô n|se | kâ|alë| ko|ông|da |ë s|üng|ë n|ibê|rös|mbë|bët|ëtï|âmb|mbâ|ïgî|mba|gî |tän| po|bûn|gï |amb|ü n|gbï|ôi |gôi| af|rë |erë|lê | as|afa|âzo|i p|sor| ad|i s| ba|gïg|ä n|bät|dë |ö â|kûe|ûe |kpä|päl|älë|e z|ätä|ö w|ngi| yê|köt|ötä|tä |ê s|kod| hï|hal|hïn|lëz|ëzo|ngä|gän|odë|ö m|mar|sär|pä |ärä|îan|rän|bîa|a h|gi |bor|du ",
    "nno": " og|og | de| ha|er |en |ar |til| ti|lle|ett|il |ret|om |et | re|le |har|enn| me| al|all| fr|ne |tt |re | å | i |nne|and|ing|ska| sk|men| fo|det|den|ver|for|ell|t t|dom| so|de |e s| ve| ei|ere| på|al |an |e o|e h|fri|sam| sa|l å|på |leg| el|ler|som|ein|ei |nde|av | st|dei|or |ten|esk|kal|gje|n s|tte|je |ske|rid|r r|i s|te |nes| gj|eg |ido|med|e f|r s|st |ke |jon| in|r f|sjo|asj|nas|ter|unn|ed |kje|han|ona| er|t o|t e|g f|ski|e m|ast|ane|e t| av| gr|lan|ste|tan|å f| na|der| sl|t s|seg|n o|r k|nga|ge | an|g o|at |na |ern|nte|ng | ut|lik|e a|bei|gru|e i|arb|kil|g s|lag|eid|r a|e d|g d| si| få|ame|a s|e r|rbe|jen|n m|r d|n e|nn |e n|erd| tr| må| bl| mo|ren|run|nin|bli|kra| kr| at|ege|n i|me |nsk|ins|år |frå|in |lov|v p|end|mot|ale|e v|å a|få |rav|int|nal| ar|sta|e k|t f|ome| la|ot |t a|sla| ik|nle|itt| li| kv|id |kkj|ikk| lo|nad|å v|tta| fa| se|gen|ld |å s|kan|g t| ka|r l|god|n a|lin|jel|ild|dig|ha |l d|kap|ve |ndr|g i|g a|inn|var|rna|r m|r g|a o|dre|d a|n t|ag |kår|mål|ig |va |i d|t m|e e|n d|tyr| om|g e|eve|då |e u| då|und| no|ir |gar|g g|l h|se |ga |d d|l f|ker|r o|å d|eld|ige|t d|t i|t h|oko|nnl|rel|nok|rt |lt |åse|jer|ta |ik |ial|eig|r p|i e|olk|bar|osi|kte|sos|lir|opp| un|ad | be",
    "mos": " n |ẽn| a | se|a t|sẽ|̃n | ne|a s| ye|e n| ta| tɩ|n t| pa|tɩ | la| so|nin| ni| b | fã|fãa|ãa |ng |a n| bu| tõ|la |ẽ | te|tõe|ne |ye |a a|or | ya| to|ed |ned|pa |e t|õe |tar|em |tẽ|g n|ã n|n m|aan| ma|sor|buu|n y|maa|uud|a y|r n|ins|n p|ud |ra |paa|ɩ n|a b| wa|d f| na|me |n d|ara|n b|sã |taa|n w|bã |an |yel|eng|aal|ɩ b|n n|gẽ|̃ng|og | ka| bɩ|bɩ | tʊ|gã | yɩ|na |am |e b|ame|wa |g a|d b|aam|ab |mb | bã|ãmb| ba|m n|wã |aab|a m|aa |saa|ga |nsa|yaa| wã|a l|tog|ore|n s|nd |ʊʊm| sõ| sã|ãng|seg|egd|d s|el |tʊʊ|ngã|ba | tũ| da|ã t| me|b s|re |dat|l s|d n|ɩ y|ã y|dɩ |aoo|g t| kã|m t|ing|r s|a p|b y|b n|gdɩ|men|dã |vɩɩ| vɩ|lg |oor|ã s|n k|al |rã |nga|ar | le|gr |d a|neb|̃nd|ɩɩm|ĩnd|yɩ |lem| pʊ| bʊ|pʊg|nge|to |b t|ɩ s|g s| mi| ke|a k|bãm| we|kao|ilg|wil| zĩ| no|kẽ| ra|m b|ʊge|b k| bũ|oog|ã p|bũm|ngr|at | wi|gam| ko|eb |g b|sõn|ãad|ã f|õng|ɩm |m s| yi|ũmb| yã|ʊm |oy |wẽ|noy|ʊmd|da |ren|a z|ya | gã|le |b p|ɩ t|n g| f |ni |soa|oab|i t| sɩ|lag| ti|te |o a|s n|oga|go |tũ |gem|age|a w|̃ n|in | yõ|a g|b b|aor|ka |ẽe|tũu|aas|a r|e y|ag |eg |r t|e a|ã k|iid|e p|neg|o t|ate|oa |e s|ũ n|mã |ms |ell|eem|ẽm|b w|̃ms|too|ik | zã|zĩn|kog|bao|r b|s a|bui|uii|ogl|aba|alo|loa|kãa|od |l b|ll |nda|kat|aka",
    "cat": " de| i |es |de |la | la| a | pe|per|ió |ent|tat| se|nt |ret|ts |dre|at | el|ls | dr|men|aci|a p|ció|ona| co|a l|al |na |s d|que|en |el | to|s i| qu| en|e l|ns |tot|et |t a|ers| pr|t d|ons|er | ll|ion|a s|ta |a t|con|els|s e| l’|rso|res|als|son| un|est|cio| re|pro|ita|cia| in|les| o |ue |del|lli|té | té|ia |ame|é d|sev|ota|nac|i l| al|s p|a d|ar |a i|ual|nal|a c|ant|nci| le|ert|sta|rta|ser|t i|i a|l d| no|va |ats| d’|s n|re |s a|e c|eva| na|rà | ca|ues|com|lib|és | so|ibe| es|ets|ber|da |r a|no |una|l’e|s l|ter|sen|ran|ure|des|man|i e|l p|t e|n d|e d|e e|om | di|cci|igu|a a|s t| pa|i d|tra|s o|aqu|tre|vol|ect|a u|l i|gua|ide|s s|ada|ene|ial|nta|ntr|ens|soc|cte|ra |oci|hum|uma|cla|ali|lit|erà|cti| aq| hu|ici|pre|era|ess|uni|nte| fo| ni|ble|sse|tes|alt|eme|ass|ica|seg|o s|ote|rac| ig| po|ans| és|a e|un |us |mit| ma|r s|se |ssi|s h|a m|r l|nit|l t|ènc|ó d|ten| te|ir |i p|tal|eta|dic|i i|hom|t q|par|egu|s f| as|n l|ria| mi| ac|lic|int| tr|act|eix|n e|s c|ont|nse|ecc|t t|ltr|amb|qua|l’a|eli|ura|an |ist|e t|ó a|one|nam|ing|lar|o p|esp|rec|lig|a f| ha|iva| am|lle|t s|rot|mat|liu|tiu|iur|n a|fon|ots|inc|ndi|e p|seu|olu|gur|i c|més|der|rna|ina|for|igi|cie|bli|ic |mb |in |art|ol |rom|nin|omp",
    "sot": " le|le |ng |ho | mo| ho| bo|a h| e |lo |ya |ba |e m|a l| ya| ts| ba|na |ong| ka|a b|tho|e t|sa |elo|olo|a m|ets| di|o e|la |mon|oth|tsa|o y|ka |eng|a k|oke|kel|a t|g l|tok|ang|o t|tla|mot| se|o l|e b| na| ha|lok|wa |e h| tl| a |aba|o b|tse|ha | o |hab|e k|tjh|a d|tso|jha| to|se |so |oko|e e|tsh|dit|pa |apa|o n|e l|loh|kol| ma|o m|a e|ela|ele|ana|a s|let|bol|ohi|a a|tsw|kap| ke|hi |g o|ohl|eo |ke |ona|set|o k|o s|di | kg|e d|aha|lan|bot|bo |ito|o h| mm|hle|eth|ena|i b|ala|ats|moh|swa|lwa|g k|atl|abe|g m|ola|phe|bat|ane|a n|mel| me|o a| ph|ebe|ell|hlo|tlo|etj|mat| sa|g t| th|g y|lat|mol|g b|g h| en|she|the|seb|nan|lek|boh|hae|kgo|hel|e s|edi|wan|me |kga|ae |to |a f|ath|lao| hl|han|ile|nah|we |ume|kan|otl|len|aka|efe|ire|bel|bet|rel|swe|mme|sen|a p| ko|g e|atj|lel|its|bon|oho|eha|shi|man|ano|nts|he |lal|eka| fu|o f|heo|got|all|ao |het|hat|get|ban|hal|kge| wa|a y|lla|fum|mmo|kar|alo| ef|thu|e y|wal|tha|san|hon|tlh| he|e n|ben|hla|ing|uma|pha|o o|si | tu|tum|llo|lle| ta|pan|hen|mo |nen|hir| lo|son|ots|tab|ama|ato|din|lap|hil| eo|dis|oka|elw|tsi|llw|i m|hol|pel|iso|no |e a|fet|lwe|adi| fe|fen|hwa|opa|kop|are|amo|ret|emo|i k|isa|o p|o d|i l|gat|dik|i t| nt| la|ame|shw|hah| am|nya|ita|mab",
    "bcl": "an | sa|in | na|ng |sa | pa|na |nin|ang| ka| ni| ma| an|pag| as|sin|asi|n s|ion|n n|cio|a m|on |ban| de|n a|ga |kan| mg|a p|mga|a n|os |rec|ere|der|cho|ech|n p|aci|aro|n m|man|a s| la|n d|o n|asa|n k|g s|kat|sar|ata|ay |o s|al |ong|n l| o |a a|ho |a k|igw|tal|gwa|amb|kas|sai|mba|wa |ara| ig|agk|o a|lam|ro |o i|gka|ali|apa|nac|san|aba|g p|ina|a d|iya|yan|ing|lin|may|ink|aiy|nka| ba|aka|a i|yo | in|ag |abo| da|aha|ini| ga|tan|s n|nta|ano|agt|s a|kai|ad |hay|ida|hos|o m|og |ia |iba|ent|han| ta|par|n i| hu|at |ron|a b|g n|ant|g m|nal|ayo|a g|dap|mag|no |sta|aya|iri| pr|nga|ran|cia|g k|es |pat|li | co|dad|l n|y n|bos| si|mak|pro|ala|men|gan|aki|nte|lan|o k|con|t n|gab|a l|g d|ona|n b|ta |do |nda|aan|as |uha|agp|a c|uli|awo|taw|pan|n o| so|hul|i n|ter|ado|ags|g a|tra|min|anw|tay|kam|nwa|waa|g o|a o|kap|ain|bal|bil|ami|g i|d a|res|ra |nag|gta|ton|n e|ba |nan| mi|kab|en |bas|gpa|nes|o p| di|pin|ika|l a|n g|ind|isa|cci|ili|ial|ecc|tec|nci|ios|bah| es|one|pak|om |imi|agi|ico| re|ana| bi|a e|nid|rim|rar| se|rab|s s|hal|i a|buh|sab|cri|ubo|bo |gi |wo |rin|int|agh|ipa|sii|ibo|ani|to |sad|hon| le|iis|a t|ast|say|lar|n c|aag|ote|rot|n t|y m|ici|paa|ley|ey |yag|aen|dan|ni | pu|atu|lab|sal|ica| gi",
    "glg": " de|os |de | e |ión| a |da |to |ció|ere|ón |der|ito|en |a p| co|ent|eit|n d| se|rei|ade|as |aci|dad|s d| pe|per|o d|s e|e a|e d|men| da|nte|ers| pr| te|do |al |rso|ida|es |ten|soa|oa |que| to| po| o |a t| in|a e| li| do|cia|te |tod|res|o a|pro| re|tos|est|ra | es| ou|dos|lib|con|a d|nci|o e| na|e e|a a|a s|ber| á |oda| pa|e o| qu|e c|ue |ar |nac| en| sú|tra|s p| un|súa|com|ou |ia |nto|ser|a c|er |ns |a o|se |des|is |ter|s n| ca|ado|or |óns|sta|úa | no|rda|s s|ibe|rá |erd|era|no |nal| as|ica|e p|eme|erá|pre|sen|das|e n| ni|e s|por|ais|par|ant|ara|ame|cci|ona|io |o p|n p| di|cto|s t| so|o t|o á|nin| me| os|cio|enc|unh|n e|n c|nha|ha |ntr|ion|n s|á s|n t|s o|ese|nta|ect|e i|o s|e l|so |nid|oci|soc|ont|dic|ici|e t|tad| ac|tiv|ndi|ali|gua|l e|rec|a l| ig|omo|cas|o m|re | ma|ing|na |igu|vid|eli|ngu|und|s i|rac|a n|cla|cti|seu|ria|on |ase|o n|lic|s c|man|lid|a u|uni|ta | ó |ual|ido|ori| fu|ind|nda|ste|s a|tes| tr|act|ial|fun|dis|ecc|o ó|cal|mo |un |e r|iva|n o|ca |n a|o c|esp|ome|o o|seg|sti|r a|tor|r d|egu|ada|lo |nde|r o|uma|ote| el|alq|lqu|uer|spe|a i|tar|bre|tri|hum|olo|cie|ren|ena|ari|mat| fa|med|ura|lar|edi|ver|ixi|á p|ibr|gur|int|pen|rot|a f|cac|s f|ili|rio|ma |a v| vi|rim|len|ita",
    "lit": "as |ir | ir|eis|tei| te|s t|os |uri|ti |us |is |iek| pa|ai | vi|vie|tur| ki|ri |žmo| tu| žm|ien|ės |ių |ali|ais|mog|vis| ka|lai| la|ini|i t|s i|s ž|sę | į |isę|ena| ne| pr| bū| jo|pri|kie| ta|kvi|nas| su|ekv|mas|gus|būt|tin|isv|s s|ogu|isi|mą |mo |ant| ar|s k|ama|kai|ūti|s a|s v|aci| ti|s n| sa|s p|oki|cij|inė|ar |val|ms |tai|jo |i b| na|gal|sav|kur|aus|men|rin| ap|imą|ma |sta|ę į|ina|i p|imo|nim|i k| nu|ima|oti|mis| ku|jos|lyg|dar|išk|je | at|tas|kad|r t|tų |ad |tik|i i|nės|arb|i v|ijo|eik|aut|s b| įs| re|iam|sin|suo| be|isu| va|li |sty|asi|tie|ara|lin|isė|i s|ą i|jų | ly| ga|vo |si |r p|tuo|aik|rie| mo|din|pas|mok|ip |i n|rei|ybė|mos|aip|r l|ntu|įst|į t|gyv| iš|nti|tyb|ų i|pag|kia|kit|es |uot| sk|jim|tis| or|aud|yve|ven|mų |als|ų t|nac|avo|dam|ą k|i a|s j|oje|agr|kla|gau|neg|nių|o k|ega|iki|aug|ek |tat|ieš|tar|ia | ši|ios|ška|sva| to|tau|int|sau|uti| as|io |oga|san|mon|omi|kin|ito|s g|ome|r j| ve|aty|kim|nt |iai|lst| da|ją |min|r k|o t|nuo|tu |ver|kal|am |usi|o n|o a|ymo|tym|vę |ati| ji|o p|tim|ų n|paž|ter|s š| vy|alt|ksl|ing|ų s|oma|šal|ran|e t| ni| ša|ava|avi|nie|uom|irt|elg|jam|ipa|kių|tok|eka|tos|oja|kio|eny|nam|s d|ndi|amo|yti|gri|svę| gy|lie|ėmi|ats|ygi|soc|sie|oci|pat|cia",
    "umb": "kwe|oku|a o| ok|nda| kw| om|da |wen|e o|a k|la |ko | ly|end|nu |ka |o l|oko|mun|omu|unu|kwa|wa | ko|a v|o y|omo|mok|ali| vy|eka|olo|i o|osi| yo|lyo|mwe|si |okw|we |lo |iwa|o k|i k|le |te |a e|ete|gi |kut|sok|ong|iso| ya|vo |ang| ey|wet|ata|a y|o o|yok|ofe|fek|kuk|ela|a l|ilo| wo|owi|nga|iñg|kul|oka|vyo|uli|u e| va|li |ñgi|kal|wat|ta |u o|eci|ngi|ovo|ye |so | li|oci|yo |wiñ|nde|ga |ing| nd|ili|nge|ci |eye|ala|vya|e k|kol|isa|a a|lom|lon|go |avo|ako|ovi|pan| ol|uka|ngo|lya|ti |o v|akw|yal|olw|uti|imw|eli|alo|ge |ung| ku|a u|lis| al|onj|ati|wal|ale|e l|sa |i v|and| ov| yi|ika|ukw|ele|lil|yos|he | oc|yov|iha|ikw|omb|val|lin|lim|ahe|apo| ka| ye|yom| vo|lik|i l|kok|wav|aka|cih|o e|tiw| ke|yi |i w|ama|e y|lof|yow|yol| ek|kov|ole|vak|vik|tav|omw|a c|upa| el|ila| lo|aso|su |e v|lyu|ava|ñgo|lwa| wa|gis|gol| ce|tis|ave| on| es|po |wil|va |eso|kup|co | la|yam| ak|wam|iyo|ekw|e e|i c|tat|i a|a n|yah|eko|lwi|ita|lit| ec|kwi|upi|i y|epa|kan|kiy|nja|dec|asi|e u|yav|asu|mak|lap|yim|tya|vos|kas|cit| ha|lel|u c|a w|emb|u y|ola|yon| os|win|lye| ca|eyo| uk| ci| ow| yu|ayi|vel|liw|has|iti|sil| et|yuk|o w|umb|ulu|ya |wi |anj|kat|ngu|wom|o a|uva|esu|usu|mbo| co| of|mat|o c|ca |cel|vi |u l|ba |kon|mbe|wiw",
    "tsn": " le|le |go | mo|ng | ts| go|lo | bo|ya |we | di|gwe| ya|ong|ngw|sa |olo|elo|a b|tsa|tsh| e |tlh|a l|o t|e t|a g|e m|wa |a t|o y|eng|na |e l| kg|wan|kgo|mo |o n|tse|a k| tl|ets|ane| ba|dit|mon|ele|hwa|shw|la |ka |a m|nel| na| ka|e d|o l| o |o m|ba |se |e g|e e|bot|a d| a |di | ga|ots|tla|otl| se|lol|o b|tho|so |lho|tso|o g|ang|got|e b|ga |lel|seg|o e|its|gol|ose|ho |oth|let|e o|lha|ego|aba|hab|e k|ano|los|a n| nn| ma|eka|g l|šha|tšh|kan|alo|ola|lhe|ela|aka|sen|gat|tsw|kga| nt|mol|o a|nng|o o|o k|aga|atl|o s|bat|tlo|agi|yo |len|g y|edi|e y| th|g m|dik|to |tir|e n| ja|a a|mel|o d|ana|ire|g k|rel|swe| yo|bon|gag|lek|e s|mot|kwa|i l| te|a s|he |agw|ats|iwa|i k|itš|ona|no |a e|mai|any|lao|ikg|she|ntl|lwa|dir|g t|lon|ale| sa|ao |hel|shi|tle| wa|ume|log|jwa|itl|pe |hir| jw|non|iti|a y|set|hok|ira| ti|odi| me|gi |e j|tek|etl|a p|ko |ath|ala|hol|bod|tet|mog|han|nya| mm|g g|nag|i t|adi| lo|oag|i b|nna| ko|the|lan|re |thu|wen|hot|nyo|hut|o i| ne|pol|me |tum|ope|ame|gan|emo|ore|wel|nts|oko|okg|iro|ro |tha|elw|amo|gor|ing|jal|isi|nan|ogo| it|jaa|si |oga|heo|gon|diw|pa |opa| kw|lat|are|bo |o j| ke|ke |ile|gis|o f|rag| ph|bok|aak|kar|rwa|nye|g a|atš|mok|ago|okw|hag|ate|ato|uto|gwa|mme| fa|fa | op",
    "nso": "go | le|le | go|a g|lo |ba | di|ka |o y|ya | ka| ya|ng | ma|a m| mo| tš|elo|etš|e g|a l|o l| bo|a k|a b|e t|na |o t|tok|wa |e m|a t| ga|la |ang| a | ba| se|man|tše|oke|o k|ša |kel|dit|tša|tho|we |ele|a d|o g|o a|a s|o b|gwe|e d|ho |o m|ego|e l| na|tšh| to|šo |še |oko|ga |di | o |olo| e |let|ong|gob| ye|oba|ago| tl|tšw|mo |e b|re |g l|ngw|aba|tšo|swa|šha|ane|tla|hab|o n|ona|ito|ela| kg|ogo| th|oth|wan|eo |e k| sw|lok|kgo|log|ye |o d|a n|ola|g o|e s|set|hlo|kol|se | wa|lel|ao |eng|o s|šwa|mol| ts|eth|net|ano| bj|a y|o e| ke|thu|hut|šwe|ge |itš|leg|rel|alo|to |ohl| ge|mog|kan|e e|ire|nag|ke |eba|aka|pha|gag|bot|o w|aga|a a|mot|are|mok| yo|gor|oka|ko |gon|no |ore|ana|agw| wo|bon|bat|lwa|tse|bja| ph|din|yo |e r|šeg|e y|ath|nya|get|lao|sa |wo | re|wag|odi| sa|seb| me|utš|oph|mel|iti|kge|ato|kar|o o|šom| la|o f|phe|edi|hir|ala|pol|lat|ušo|i g|a p|g y|the| fi|ume|wel|bop|hel|emo| du|ile|gwa|bo |ale|tle|lwe|lek|ban|ta | lo|lon|o š|dir|mae| mm|tlh|god|pel|a w|weg|eka|elw|atš|išo|aem|šhi| ko|gam|rwa|mmo|boi|e n|ntl|pan|amm|i l|i b|hle|hla|leb| am|šon|jo |len|i s|kop|ret|gel|ing|opa|yeo|dum|sen|e a|ape|ase|kwa|lef|mal|amo|oge|bjo|oik|mon|kga|okg|a f|tsh|boh|uto|ika|ahl|ja |adi|iša|gab|hom|abo",
    "ban": "ng |an |ang| sa|ing|san| ma| pa|ane|rin|ne |ak |hak| ha| ka|n s| ri| ke|nga| ng|man|in |lan|a s|ara|ma | ja|n p|n k| pe|g s|g p|pun|asa|uwe|gan|n m|nin|sal|pan| la|alu|iri|sa |lui|jan|adi|a m|adu|uir|ra |yan|mad|kan|wan|duw|ur |tan|g j|anm|we | tu|nma|ika|awi|nge|ah |tur|ih |ban|ka |e h| ne|n n|en |nte|un |ngs|eng|anu|beb|aya|ani|ana|ian|a p|ala|bas|nan|gsa|ngg|uta| da|gar|aka|eba|da |apa|asi|ama|lih|aha| wa|ten| ut| ta|a n|ebe|are| wi|han|aje|keb|oni|nik|ent|aki|uni|ata|wia|iad|g n| pu|jer|ero|ron|aan|k h|saj|din|sak|a t|nus|dan|n w|pen|usa| ba|ngk| pi|ant|sam|e p|taw|n r|ate|wi |nen|i m|ega|neg|iwa|pat|atu|e s|ami|ipu|g k|ina|mar|kat|kal|aga|sar|ran|kin|per|g r|ndi|arg|ar |ksa|e m|ren|nya|al |tat|ida|ela|h p|aks|ntu|ngu|ado|lak| ny|oli|at |wen|ep |i k| se|dos|h s|n l|dad|gka|eka|a k|rep|eda|n h|par|upa|ena|swa| sw| in|nay|ewa|ung|era|ali|a u| mu|eh |nip|r p|e k|n t|k p|ras|i n|uku|n i|wah|eri|g m|pak|n b|r n|ayo|nda|mal|mi |um |dik|os |osa| mi|yom|na |teh|awe|k r|lar|car|tah|sia|g h|ti | hu|ut |huk|kum|sti|ewe|tuk| me|rga|pin|h m| su|gi |ari|n d|a w|ta |uan|gaw|gen|h r|on |war|tut|lah|pag|gay|r m|n u|ada|ira|a b|ngi|end|kew|g t|min|ggi|gda|jag|as |rap|agu| an|e n|ngd|s k|ila|eta",
    "bug": "na |eng|ng | na| ri|ang|nge|nna|ngn|gng|ge |sen|a r| ma| pa| si| ta| ha|ri |hak|app|tau|ak |au |ddi|a t|ase|edd|ale|a n|nap|gen|len|ass|pa |e n|ai |ria|enn|ega| ru|upa|rup|ias|a a|ing|inn|a s|pun|ngi|nin|e p|ini|nai|ga |lal|gi |sin|ppu|are|ae |ye | ye|ana|g n|sed|ada|le | as|i h|a p|ama|g r|i r|man| se|una|ara|ra |di |ssa|ren|a m|pad|e r|ila|ban|asa| ke|san|din|e a|ura| la|ane| de|nas|e s|i a|ipa|pan|u n|ann|i l| ad|da |ala|aji|ole|att| pu| e |ong|i s| ba|pur|aga|lai|i p|lan|g a|ngs|sal|ola|gsa|g s|a b|i n|ppa|rip| we|a k|g m|asi|wed|akk|mas|i m|ril|u r|reg|g p| pe|ung|gar|neg|sse| po|e m|k h| ar|pas| ne|map|ian| te|nar|pol|ett|ran| ja|bas|eba|jam|beb|ena|par| al|sib|ebe|ngk|uru|keb| sa|ain|ttu| mo|aka|unn|add|iba|sa |gan|gka|nen|bbi|i t| at|atu|kan|nan|uan|leb|rus|de |e d|ton|ata|tu |ssi|ro |e y|cen|kun|awa|ell| wa|k r|mak|wa |uwe|ire|ebb|gag|apa|sae| tu| ia|tte|mat|sim| to|a d|o r|ta |nat|ece|tur|la |ie |dec|ko |kel| di| hu|nca|caj|pak|rel|ma |lu |g t|bol|uku|e e|ter|jaj|tta|we |bir|deg|huk|e h|dan|ure|baw|kol|rit|kko|ele|arg|rga|llu|oe |lin|use|ari|auw|pat|mul|elo|ula|iti|gau|an |u p|nga|g y|a h|ekk|sil|ka |e w|ade|anc|iga|sip|ten|a y|e t| me|nre|aja|ji |rek|a w|dde|per|iko|sik",
    "knc": " a |ro |be |nzə|ye |a a| ha| kə|abe|akk| ka|zə |adə|a n|a k|kki|hak|mbe| la| ad|ndu| nd|wa |ben|en |ma |də | ya|o a|əbe|ə a|ga |e a|əga|lan|əna|lar|aye|aro|kin|inz|rdə|ard|ana|yay| ga|əla|kəl|ji |awa| mb|bej|eji|kən| ba|an |uro|du | na| ku|anz|dəg|nəm|kal| nə|e m|na |gan| du| sh|shi|amb|n k| su|ara|u y| ta|so |a d|kam|wo | ye| sa|e h|a s|sur|aso|au | au|iwa|nyi|kur|a l| da|kar| as|dəb|iya|kiw|o k|obe|e s|ada|ama|and|u a|aa |ta |ima|n n|la |əwa|nga| ci|ba | ab| nz|əgə| fa|ənd|ata|ndo|ya |tə |nza|ə n|ndi|a g|in |nam| fu|ə k|aya|a t|tən|a b|təg|ru |uru|inb|am |e k|al |ida|mga|aar|a h|baa|ə s|nab|dəw|dun|asa|nya|owu|gad|taw|o w|gən|a y|kat|dam| sə|o h|əra|e n|awo|ade|əmk| wa| wo|amg|dən| tə|a f|ala|i a|zəg|o n|uny|iga|zən|əli|wur|u k|o s|wan|za |din|utu|e l|san|i k|uwu|wu |awu|n a|on |de |da |nba|mka|yi |gay|tam| ng|laa|gin|azə|bem|gai|taa|ibe|rad|adi|fut| mə|wow|wak|ali|kun| an|mər|o t|yab|nad|aim|əgi|i n| aw|liw|cid|u s|edə|atə|any|do |apt|lka|alk|dar|rta|bed|tu |ela|ndə|uwo|gal|yir|wum|n y|ayi|n d|mma|zəb| yi|nan|ltə|lmu|ilm|mar|bel|raj| il|ero|m a|utə|enz|iro|alw|uma|umm| um|e g|how|kka|o f| ny| ho|fuw|ə h|ang|tin|zəl|o g|ema|ən |no |a i|a m|wal|əny|iwo|lil|ədə|ə f|rtə|hi |diy|mu ",
    "ibb": "ke | nd| mm|me | ke|e u|ndi|o e| em|mme|de |en |e n|owo| en| ow|wo |i e|mi |ye |emi|nye| un|e e|edi|ene| ek|yen|eny| ed|e m|nen|une|ana|n e|e o|e i| ye| uk|et |n n|eke|na |e k| mb|em |ne | id| es|un |kpu|ede|iet|ndo| nk|o k|di |kpo|ukp|did|am |an |kie|nam|kem|esi|o u| nt|idu|eme|o n|t e|no |yun|mo | uf|ho |mmo|nyu| in|o m|kpe|o o|sie|oho| kp|do |din|ie |ono|kpa|m e|ri |nkp|dib|on |e a|uke| ki|boh|a k| et|po |ida|dut|m u|ked|ded| ub| of|ond|ru |uru|pur|in |ut |du |eko|a u|ina| ot|mbe|n o|bet|iny|man| ak|op |idi|ikp|i o|edu|kon|ade|om | us|uan|wem|a m|uwe| uw|puk|ak |ode|ro |t m|a e|oro|a n|n k|u o|to |te |bo |akp|ufo|ok |dik|pan|mbo|bio|i m|ide|ini|fur|uri|ban|ofu|ubo|n i|o i|uto|iso|dom|omo|ema|diy|fen| nw|dis| ny| is|ni |usu|n m|u u|fin|tom|eto|pem|ed |m m|ibo|oto|o a|sua|wed|nwe|m n| ut|mde|dud| eb|ara| as|i n|oki| ob|nte|mok| ik| an|kar|m k|o y|t k| on|i u|nwa|n y|asa|ama|re |ufi|uka|io |nek|i k| or|pon|top|sun|ion|se |aha|t o|k n|e y|ere| ef|mba|mad|isu| mi|kor|ra |ian|i a|ka |a a|k m|ko |da |t i|ena|obi| ey|ha |dia|ti |aba|uk |u m|d e|dem|san|a o| se|pa | ab|tod|n u|p m|ude|fok|k u|efe|uku|nti|nka|ibi|son|he |pe |nto|dak|a y| od|nde|eye|anw|ndu|mbu|so |ebi|bie|nda|sin|med|tu ",
    "lug": "a o| ok| mu|oku|mu |wa |nga| ob|ga |tu |ntu|a e|na |bwa|a a|ang|ra |aba| n |ba |a m|wan|a n| ng| ab|li |obu|unt|a k|era|ibw|dde|oba|a b|u n|za |la |mun|ban|ali|ka |emb|iri|bul|ate|mbe|i m| ek|tee|eek|uli| bu|u a|edd|sa | ku|ant|ana|eki|u b|be |dem| eb|ama|n o| om|ira|omu| ki| ed|ye |ala|amu| am|e o|gwa|nna| er|kuk|y o|kwa| en|okw|eer| ly|inz|ula|kus|kir|u e| ba| em|eri| ky|any|onn| wa| ye|ggw|ina|kol|n e|awa| bw|uyi|u k|eka|yo |bwe|ola|o e|usa|o o|kwe|mus|yin|bal|i e|u m|ngi|e m|bir|riz|ere|ri |ebi|kul|aga|nza|kub|ekw| eg|ko |a y|u o|we |kut|mat|e l|e e|a l|aan|ger|no |kan|sin|nka|gir|uso| at|a g|iza|gan|nyi|zes|uku|wo |nge|zib|isa|izi|ya |egg|ufu|rir|lin|wam|wal|eby|a w|i o|bee|oze|esa|eta|iko|ebw| ma|ako|bon|tuu|kin|uki|de |zi |kug|yen|ino|e b|obo|aka|ulu| te|ne |lwa|ma |y e|lye|kuy|nsi|i y|gi |utu|ly |imu|e n|taa|asa|enk|ku |o n|o b|sob|si |una|bun|usi|san|e k| ag|uka|uga|ata| ol|rwa|wen|ing|wat|kik|o k| by|nya|ong|kye|by |kyo| bo|ewa|yam|bye|ubi|ngo|kis|ani|boz|kit|i n| aw|ky | al|sib|muk|awo|uko|umu|ibi|uma|afu|olw|eky|tab|ung|buy|ini|uum|saa|y a|lal|mag|ro |end|add|enn|kib|ens|ole|ni |mbi|o a|i k|gat| og|maw|and|kuu|a z|wet|igi|yig|emu| ne| gw|a t|nzi|n a|gya|amb|uwa|ulw| ey",
    "ace": "ng |an |eun|ang| ha|peu|oe |ak |on |nya| ny|yan| ta|ngo|ung|gon|na |ah | pe|reu| ng| ba| ke|hak|meu|keu| me|eut|at |ure| na|ban|ee | di|teu|roe|ata| ur|ara| be|seu|han|a h| sa|am |dro|eur|um |n n|tie|iep| ma| la|ala|nan|g n|ut |ong|a n|ep |tan| te|tap|jeu| ti|eul|eub|eu |eug| da|eum|eh |euk|ra |ih |n p|uga|ai |n b|a t|e n|lam|eba| se|beb|n t|awa|om |a b| ka|asa| at|eus|and|nyo|oh |ta |ka |h t|n k|p u|man|e t|n d|n h|ana|dan| pi|ape|a s|neu|nda| si|t n|bah|ula|yoe|a k|h n|dum|euh|g d|e p|eng|e b| le| pa|ngs|sia|ran|ma |g k|un | wa|ndu|lan|una|heu|ura|n m|lah|sa |n a| ra|aba|g s|a p|ia |und| je|wa |kat|bak|k n|anj| dr|asi| bu|nga|beu|uny|yar|sya|hai|k m|k t|k a|ama|aan|ek |a m|ok |g h|aka|sab|g p|i n|uta|khe|h p|ue |uka|har|ari|di |e d| su| um|t t|a l|ya |san|e s|gan|uko|gsa|e u| li|kan|bat|lee|aro|ot |n s|leu|ina|h d|lak|oih|yat|n u|kom|pat|ate| ne|ngg|nje|taw|mas|uma|sid|anu|umu|aja|si |uh |h m|rat|aya|sal|et |soe|t b|n l|aga|taa|usi| ja|ute|m p|en |dek|ila|a d|ube|dip|gam|any|lin|tam|don|ika|usa| ji|rak|idr|h b|nus|adi| as|dar|ame|n j|ngk|m n|eup|h h|bue|k h|huk|euj|g b|gar|eka|gah|upa|ile|sam| bi|h s| de| in|mum|‐ti|t h| hu|k k|pho|dil|ep‐|nta| ge|geu|h l|hat|ie |tha|use|ieh|sas",
    "bam": " ka|ni |a k|ka |an | ni|kan| bɛ|n k| la|i k|ya |la |ye |ɔgɔ|na | ye|bɛɛ|ɛɛ |en |li |sir|ɛ k|ama| ma|ira|a d|ra |ali|’a | da|man|a n|a b| i |ma | kɛ| wa|gɔ |wal|mɔg|ana|n n| ba| ja|ɔrɔ| mi| kɔ| k’| mɔ| jo| si|min|iya|dan|len|i m|’i |in |kɔn|ko |aw |den| sa| o | n’|ara|bɛ |i n|jam|ɔnɔ| na|ɛrɛ|a s|i j|ani|n b|a m|i d| fɛ| tɛ| an|osi|jos|a y|kɛ |a l|iri| ko| di|ɛ b|ada|ila|ɛ m|i t| fa|nɔ | de| ha|asi|tɛ |ari|a j|raw|a t|ɛ s|ale|a f|tig|ɛn |aya|dam|a i|i b|sar|si |riy|ɲa |n y|nu |inn|e k|ɔn |rɔ |ang|a w|o j|w n|nnu|k’i|nti|nɲa|ade|abi|bil|ala|hɔr|kal|had|igɛ|i s|a a|mad| a |aga|u k|kab|a ɲ|aba| ti|olo| hɔ|o b|ɛ j|i f| ta|ɔ k|aar|baa|ɛ n|n’a|kun|ugu|iɲɛ|diɲ|n j|k’a|a h|rɛ |ati|ɔ m| se| cɛ|ɲɔg|bɔ | tɔ|i y|lan|i h| ɲɔ|tɔn|don|nɛ |inɛ|ga |i l|ɲɛ |ile| fo|o k|ɛ l|nna|ili|un |gɔn|maa|fɛn|n d|ant|n i|aay|go |da | jɛ|u b|ri |rɔn|aka|lak|ɔnɲ|e m|ɔ b|nin|nw |cɛ |w k|yɔr|n o|o f|nga|jo |o m|nen|n’i|on |ɛ t| ku|o l|igi|ɲɛn|anb|fɛ |ɔ s| bɔ|n m|e b|afa|nka|n f|nma| fi|’u |ɔ n| ɲɛ|fan|i ɲ|ti |a o|dil|ɛ d|uya| sɔ|ago|ɛ y|e f|ɛmɛ|mɛn|aju|e d|bɛn| jɔ| fu|til|bag|fur|n t|uru|kar|atɔ|be | d’| du|d’a|oma|lom| u | do|riw|taa|w l|mɛ |gɛ |imɛ|n w|iir|nni|iim|amu|so |bal| ɲa| b’|gu |ɛɛr|’o |iwa|n s|wol|ele|ɲan",
    "kmb": "a k| ku|ya |la |ala| mu| ki|a m| o |u k|ni |o k| ni|kal| ky|mu | ya|lu |dya| dy|a o|ang|kya|a n|tok|i k|oso|so |kwa|nge|xi |na |elu|nga| kw|wa | wa|a d|hu |kut|thu|uka|oka|mut| ka|a i|mba|uth|ka |gel|ba |u m|u y|ku |ene|u n|ga |kuk|ban|ixi|i m|e k|wal|oke| mb|kik|kel|ne |u w|ela|uto|i y|ana| ng|iji|a y|kit|ma | ji|nda|ngu|yos|kum|ulu|ji |i d|isa|und| it|and|ong| mw|u i|iba|ika|wen| di|ten|ilu|ila|ndu|ye |sa |kub|aka|ena|amb|ung|olo|a w|ngo|kil|oxi|lo |muk|ke |sok|du |mox|ate|o w|kus|wat|ta | wo|gu | ph|u d|ito|ita|e m|alu|a j|kis|tun|uma|wos|luk|o m|san|mwe|a a|di |imo|ula|wan|nji|jix|i j|a t|kij|idi|kan|uku|gan|kul|e o|kye|adi|ato|o i| ja| ix|da |nu |o n|uta|kud| yo|i n|udi|ki |su |tal|a u|lun|e y|u u| ye|jin|iki|pha|hal|wij|we |a s|lak|ikw|go |tes|fol|itu|eng| ke| uf|yen|ing|yat|ele|utu|kyo|o y|kwe|kwi|uba| en|kib|ite| we|dal|i o|yan|ge |eny|tan|uki| ik|dib| im|esu|lon|kat|atu|e n|ja |i u|jya|vwa|kam|i w|ute|ini|uke|lel|esa| se|xil| ut|fun|unj|ufo|mbo| a |uso|kim|mun|u p|nen|ukw|u o|i i|umu|han|gon| il|lan|ata|te |i a| ko|jil|o a|nde|nyo|eka| at|o d|exi|ijy|tu |usa|tul|kuz|ilo|dis| un|u j|dit|ufu|ote| ib|ivw|mwi| bh| ha|se |bul|ubu|win| os|imb|bha|ama| to|axi|inu| uk|sak|kos|bot",
    "lun": "la | mu|ng | ku|a k|tu |ntu|chi| ch|a n|aku|di |mun|ma |unt|a m|g a| a | na|ela|ndi|aka| we|ima|jim|shi|eji|u w|i k| ni|ind|wu |i m|a w| in|a i|u m|hi |awu|na |kul|wej|lon|cha| ja|sha| kw|a c|i n|nak|ala|mu |wa |ing|ka |ung|kum|a h|ulo|him|mbi|muk|u c| wa|hak|iku|nsh|yi | ha|bi |amu|imb|ewa|wen|kwa|ang|adi|idi|kut|esh|ana|g o|ila|ha |tun|u j|ong|nik|kuk|tel|ovu| ov|u n|han| an|ate|vu |a a|kal|ula|kwi|jak|u a| ya|a y|ilu|u k| he|ham|and|uch|kus|ond|eka|hel|kew|zat|del|hin|uku|nde|i j|enk|i a|uka|eng|ach|lu |nat|nji|ona|mon|awa|nke|umo|ins| yi|a d|ama|udi|wak|i h|ati|i c|wan|ta |bul|mwi|ata|ayi| ak|uma|i y|ina|ich|itu|uza|kuz|nin| mw|ku |kin|wun|sak|naw|nyi|ni |ant|muc|wal|ish|u y|mul|kud|waw|uke|wes|uki|i i|kam|yid|wit|da |akw|kad|yan| di|ken|uta|ika|imu|iya|nda| ns|mbu|ya |ule|dil|iha|kuy| ko|hik|eni|ahi|kuh|si |kun|ush|umu|atw|g e|his|dik|ji |any|li | ye|dim|kos|osi|hih|wat|eyi|ney| ne|amb|twe|til|wil|nu |kwe|u h|etu|tiy|ja |nan|ash|mwe|win|was|hit|iti| wu|iwa|wah|lem|g i|tam|din|hu |haw|nga|kay| ka|hid|yin|isa|iki| ma|jaw|jil|che|mpe|omp|eta|tan|jin|hiw|usa|umb|eme|inj| hi|ulu|ubu|nam|wik|mpi| da|ale|ite|tal|twa|ahu|end|nka|mba| at|ga |mes|dic|iwu|yej|kan|kuc|iyi|sem|emb|lun|una",
    "tzm": "en |an | ye| d | n |ad |ur | ad|n i| s |agh|ḥe|n t| i |dan| ta| lh|lḥ|d y| gh|ell|n a|ra |̣eq|i t|eqq|s l|mda|ett|n d|d t|akk|la | ti|qq |hur|di | di| am|gh |ghu| is|t i|r s|in |nag| na|a y|is | te|a d|n n|yet|n g|ll |ara|ghe|ma | we| ar| wa|n s|l a|n l|sen|edd| ak|it |li | le|dd |ull|lla| id|d a| ur|rfa|erf|kul| yi| ku|as | se| ma|zer|amd|a n|lli|lel|men|t a|kw | de|t t|nt |kkw| im|fan|a i|a t|eg |n w|i d|q a|rt |ar |gar| ag|es | tl|ize|emd|i w|i l|deg| as|ken| dd|n u|lan|d i|a a|wak|tta| tm|d u|er | tu|wem|at |ddu|tle|w d|n y|t n|sse|r a|mur|s t|tam|gi | tt|yes|wan|r i|tim|na |wen|twa|d l|ttu|kke|wa |nen| iz|iḥ| u |win|d n|ame|s d|ent|ḍe|hel|a l|hed|ess|t d|mga|arw|i n|ḥu|mi |mad|agi|i g|der|udd|s n|rwa|̣en|awa|i i|ya |h d|iya|s y|msa|uḥ|idd|urt|un |n m|ane|em |sef|lsa|ili|q i|qan|leq|siy| ik|el |err| in|yed| la|ant|den|tag|man|g w|mma|yen|len|tmu|i u|aw |taw|r y|wad|edm|ṣe|hla|t l|̣er|ala|asi|ef |u a|tte|ddi|ttw| lâ|imi|l n|til|al | ne|am |̣ud| lq|iḍ| ya|dda|̣ṛ|med|ren| ss|gra|m a|ghl| il|chu|tem| ll|khe|way|eln|lna|ana|ukl|duk|gha|lt |ni |all|i a|tal|ray|nes|s k|tes|naw|ert|ila|awi|lqa|kra|anu|nun| kr|ikh|ezm|n k|iwe|iwi|ima|net|ser|s u|ir |yeh| an|aya|ehw|hwa|esk|dde",
    "war": "an |ga |nga| ka| ng| pa| ha|han|pag|in |ata| hi| an|mga| mg| ma|kat|hin|a m|ay |a p|ya |ung|a k|gan|on |n h|n n|ug |n p|n k| ug|n m|da |a h|n i|ha |iya|adu|dun|tad|a n| ta|ada|sa | iy|ara| na| di| o |pan|may|a t|ang|ud |ana|n a|o h|o n|taw|n u|ags|yon|y k|al |tag|asa|kad|o p|man| ba|awo|gsa|wo |ag |gad| in|a a|a u|ina|syo|a i|a s|od |ing|agp|ala|asy|ngo|n b|ali|nas|san|aka|a d|ra |g a|was|g h|aha|gpa|agt|to |ad |n t|tun|ng |usa| wa| tu|ini|iri|tan|ahi|kan|ray|nal|war|dir|i h|gka| us|god|g p|ri |a b|nan|ida|o a|i n|bal|y h|kas|uga|hat|tal|nah|awa|ni |pin|uha|buh|o m| bu|gud|aba|at |no | pi|bah|g m|ili|him|aya|atu|d h|agi| su|agk|lwa|mo |d a|alw|sya|uma|ano|int|kal|upa|mag|yo |o u|agb|n d|asu|lin|a o| ko|ona|did|hiy| bi|as | ki|l n|sud|iba|hi |o k|kon|ira| la|gba|pam|amo|g i|ton|gin|n o|uro|ho |os |la |g k|gtu|d m|aud|aag|t h|gi | gu| ig| ir|n g|abu|aho|ami| sa|ati|par|kau|ern|ban|tra|gar|ama|ras|yan|adt|tum| un|ka |aga|aso|api|dto|kin|tik|mil|iko|rin|sal|ika|a g|ila|mah|lip|rab|non|agu|ak |dad|lau|d n|ko |it |pak|n e| ti|una|i m|lig|s h|bay|ro |sug|mak|n w|naa|g n| so| ag|yal|nte|lal|ba |aup|lan|ihi|y b|kah|tub|bye| am|ari|yer|uka|ani|uyo|oha|ito|n s|upo|ent| pu|sam|iin|til|mat|ato",
    "dyu": "a’ | kà| ká|kà |ye | ye| à |ya’|ni | bɛ|kán|la |án |ya |ɔgɔ| ni| la|ɛɛ |ká |na |a k| mɔ|bɛɛ|mɔg| i |nya|á k|n k|ɔrɔ|’ k| mí|’ l| kɛ|mín|’ y|ín | mà|à k|ɛ k|’ m|ma | ya|à m| wá| jà| ní| be|be | ò |i y|ní |i’ | lá|ra |iya|ɛrɛ|n’ |n n| há| kɔ|te |wál|àma|jàm| te|áli|a b|ima|man|à à|hák|e k|lim| kó|ɔnɔ|mà |n b|i k|ɛn |gɔ |e b|n y|ɔ’ |ana|’ n|o’ | sà|ɛ y|’ s|kɛ |à l|rɔ |e à|kɔn|li’|àni|a m| dí|aw |rɛ |ɔ k|’ b| bá|à b|a à|ákɛ|riy|e s|gbɛ|nɔ |a j| bɔ| ù | sɔ|bɛn| sí|à y|sàr|e m|ara|kó | fà|à s| àn|dún| là|en | sì|an’| fɛ|úny| dú|a n|a y|ɛya|àri| gb|in |kɛr|kan|’ t|dí | cɛ|nin|yaw| tá|na’|e w|mìn|ìna|lá |ɔn | mì| ɲá|à d|ali|n m|yɛr| yɛ|sɔr|gɔ’| tɔ|ama|báa|nga| dà|i m|i à|sìg|ìgi|yɔr|gɔn|w n|áar|a d| sé|ána|àng|len|à i|si |ɛra|á d|bɛr|a s|bɔ |ólo|a h|i b|ɔ s|ɛ l|den|ɛ’ |à t|àra|ɔya|gɔy|kɛy|ógo|u’ |aya|’ d| má| dɔ|ra’|a f|ɔny|’ f| ó |ili|sí | se|se |ko |cóg|a t| có|dén|hɔr|ɔɔn| hɔ|ma’|lan|ika|ina|kàl| a |àla|n s|ɛ m|i t|rɔn|tig|ànt|a w|tá |e n|i s|à n|nna| í |’à |ò k|a g|n d|an |ga |fɛn|ɔ à|li |e i|ɛɛɛ|kél|ati|so’| yé|i f|áki|dàn| k’|i n|k’à| nà|í i|í à|lik|yé |igɛ|e’ |e ò|go | lɔ| na|ɔ b|w l|í t|rɔ’| dò|ò b|min|ti |àga|ow |n t|mad| mi|ò l|éle|gi |ɲán|í y|kil|dɔ |nba|i ɲ|gu | wó|ɛli|i l|úru",
    "wol": " ci|ci | sa|am |sañ|añ | na| ak|ak |lu |it | mb| am|aa |na |al |ñ s|ñu |ne |mu |te |pp | ne| ko|m n|i a| ku| ñu| te| mu|baa|u n|ko |u a|mba|a s|e a|ay | wa| lu| do|ar | ni|u m|nit|oo |épp| ta|oom|gu |t k|i b|ku |u k| it|éew|rée| ré|u y|xal| aa|kk |i d| bu|doo|i w| bi|war|u c| yi|aay|llu| li|fee|loo| xe| xa| ya|taa| di|yi |ama|on |u j|yu |eex|ew | yo|boo|xee| bo| wà|àll|wàl|mi |o c|ir |mën| më|yoo|ul | gu|nn |en |oot| du| so|oon|e m|dam|een|u d|i n|uy |eet|i m|ara| ba|bu |a a|ata|okk|aad| lé| ay|ju |ada| nj|nam|und|axa|dun|m a|enn|r n|aar|ex |taw|ala| jà| pa|et |di |ën |ana|ral|ota|k s|awf|naa|wfe| gi|u l|igg|aju| dë|ma | aj|ti |u t| se|ax |gée|mbo| ja|ool|bii|li |a m| ke|see|m c| ye|i l| ng|yam|ngu| yu|w m|an |ken|n w| lo|i s| me| de|m m|i t|om |u x|n t| an| mi|jaa|laa|ee |bok|lig|p l|n m|t y|ggé|k l|a l|lép|àpp|jàp|aam| jë|aax|ekk|nd |góo|ewa|ndi|tax|a d| da|amu|éey|gi | su|k c|n n|l b|o n|k t|p n|jàn|àng|gir| jo|a c|n a|n c|ñoo|i ñ|a n|kaa|ba |m g|le |une|kan|e b|la |nda|lee|i j|ang|aat|k n|ey |ant|iir|a y|l a|e n|nan|añu|men|j a|ok |k i|nee|l x|omi|i c|oxa|aw |g m|dox|nte|opp|u w|ngi| mo|omu|y d|are|i k|aan|em |du |a b|njà|ñ ñ| ti|m r|kun|ddu|ali| së| la|eg | ma|ëra|ng |xam|mul",
    "nds": "en |un |at |n d| da| de| un|een|dat|de |t d|sch|cht| ee| he|n s| wa|n e| vu|vun|ech|rec|ht |er |ten| to|tt | si| re|ver| ge|nne|t w|n w|ett|n h|n v|k u|n u| el|gen|elk|lk |t u|ien|to |ch | ve|wat|sie|war|het|it | an|n f|ner| mi| in|ann|rn | fö|ör |r d| fr|t r|hte|orr|ich|för| sc|rie|eit| or|den|nsc|ege|fri|rer| st|t g| up|aar|t a|nd | is|ll |rre|is |up |t e|chu|rt |se |ins|daa|lt |on |t h|oon|che|all|n g| ma|rrn|min| se|ell|hei| na|t s|n i|n a|nn |len| sü|in |rd |nen| we| bi|n m|e s|ven|ken|doo|sse|ren|aat|e m|ers|n t|s d|n b|lle|ünn|t t|n o|ik |kee|e g|t v|n k|hen|arr| dr|heb|lie|ebb|e v| al|e a|llt| ke|hn |he | wi|cho|ehe|ok |ard|sta|men|ill|gel|tsc| ok| do|an |düs|ene|erk| gr| dü|weg|ie |ede|ieh|r s|sün|üss|und|raa| dö|röf|drö|t m|ats|öff|e f|ünd|e w|dör|ens| gl|rch|sik|ig |kt |örc|ere|gru| ün|ff |ahn|nre|mit|st |al |aal|hon|ert|kan|nat|der|dee|enn|run| so|eih|lic|ehr|upp|iht|nwe| fa|pp |eke|e r|unw|t n|taa|hup| ka| be|bbt| wo|p s|el |as |t f|bt |e e|nee|maa|huu|eve|nst|ste|mee| ni|inn|n n|ern|iet| me|hör|dde|ent|n r|t o|öve|are|arb|ite|ter|l d|ach|nic|bei| as|lan|t b|d d|t i|ang|ame|rbe|utt| ut|pen| eh|uul|iek|hr | ar|r t|ul |e d|art|n ü|one|eer|na |nte|mut|ete|üd | mu|üüd|lüü",
    "vmw": "tth|la |thu|a e|na |hu |kha|a m|we |ana| mu|a o|awe|ela|ni |ala|hal|edi|to | ed|ire|dir|eit|ito|rei|ya |a n|wa |mut|a w| wa| ni|akh|aan|u o| on|o y|okh|utt|a a|haa| n’|wak|nla| wi|ari| yo| si| ok| ot|iwa|ka |iya| sa|ne |apo|lap|ale|le | oh|oth|att|the|mul|aka|oha|kun| el|aku|oni|mwa|ha |e s|unl|tha|ott|ele|ett|e m|o s| va|ene|e n|e o| ya|oot|hav|ade|ihi|iha|ihe|de |o o|e a|eli|hen|amu|e w| aw|hel|dad|ra | at|po |i m|lel|wi |o n|owa|e e|ula| en|ta |o a|i a|moo|waw|ina| ak|ota| mo|sa |a s| so|han|ara|var| kh|a i|ri |aya|itt|anl|row| mw| et|i o|ika|’we|nro|i e|n’a|her|lan|nak|sin|lo |elo|vo |u e|eri|n’e|oli|thi|u a|a’w|ida| ah|a v|liw|kan|him|lib|yar|riy|ona|onr|erd|wal|hiy|aa |ibe|rda|wan|ber|era|avi|hiw|nna|i v|hwa|lei|mih|vih| ep|khw|ntt| na|ko |ia |sik|aha|iwe|e k|hun|una|mu |avo|ikh|laa|riw| ma| an|e y|kel|’el|huk|u y|phe|kho|pon|i s|nid|upa|ath|ila|yot|eko|ali|tek| es| it|o e|uku|wih|nan|tte| a |mur|’at|i w|ani|ulu|nih|wel|lik|ira|ane|a y|nkh|saa|ro |n’h|wir|i n|ile|som|u s|hop|inn|ei |ont|kum|yaw|saw|iri| eh|tel|tti|ola|aki|mak|ret|uth|nnu|a k|nuw|ahi|enk| il| nn|ena|va |yok|ute|soo| pi|lal|ohi|hik|mpa|uwi|lih|har|kin|aph|ma |ope|man|ole|uma| oo|mpw| v’|nal|ehi|nin|uni| ek|khu",
    "ewe": "me |ame|e a|le |wo |kpɔ| am|ɖe |ƒe | si| me| wo|be |si | le|sia|esi|la | la|e d| ɖe| kp|pɔ |aɖe|e l| be|e w| ƒe|e e|dzi|na |nye|a a| du|ye | ŋu| na|duk| dz|ukɔ|e s|ome| mɔ|e n| aɖ|kpl|nya|gbe|e b|e m|ple|ɔkp|ɔ a|pɔk|woa|ɔ m|kɔ |evi|nɔ |ŋu |ke | nu|ɔ l|mes|awo| o |iwo|ɔnu|e ɖ| ab|ya |ekp|e k|ɔwɔ|u a| al|nu |ia |ɖek|e ŋ|kpe|ɔme|o a|iny|zi |dze| ny|o k|eme|eƒe|o n|iam|egb|mɔn|blɔ|i n|wɔ |a m| eƒ|o d|alo|siw|ɔɖe|lo |o m|eke|e g| bu|eny|ubu|ŋut|ɔ s|bub|lɔɖ|enɔ|meg|akp|abl| ha|e t| ta| go|mek|eɖo|ukp|li |nɔn|to |any|a l|etɔ|ɔ ƒ| ey|e h|nuk|gom|ɔ ɖ|ɔe |bɔ |ɖo |i s| to|anɔ|a k|ɔnɔ|e x|awɔ|e ƒ|tɔ | ƒo|mev| es| ɖo|ɖes| xe|i w|tso| wò|wɔw|mɔ |iaɖ|i l| ag| li|ã |o ƒ|odz|a s|agb|yen| ts|bu | he|bet| gb|o e|ewo|a e|ɔna|i d|ti |ele|dɔw| ka|i a|uti|peɖ|ta | an|afi|a ŋ|a ƒ| ad|ƒom|se |ɔwo|xex|exe|oma| ma|vin| dɔ|o l|wɔn|eye|a n|i t|vi |ɔ b|so |edz|gbɔ|ɖev|ado| se|ɔ n|oto|ene|eɖe|xɔ |nan|ɖod| af|ben|zin|ee |de |ɖok|dzɔ|gɔm|adz|ɔ k|wom| gɔ|uwo|i ɖ|a d| vo|a t|o g|i b| xɔ|oɖo|i m|e v|ats|o ŋ|sɔ |ovo|i e| at|vov|ne |ɔ e|kat|o s| ne| aw|da |wòa|eŋu| as|asi| el|o t|yi | sɔ|men|a b|ze |mee|uny|te |dom| ak|man|ẽ |i o|ie |ana|ata|ui |axɔ|u k|ɖoɖ|tsi|ema|rɔ̃|ded|ɔ g|ena| en|kɔm|met|u s| eɖ|oku|kui|mew|xem",
    "slv": " pr|in | in|rav|pra|do |anj|ti |avi|je |nje|no |vic| do|ih | po|li |o d| za| vs|ost|a p|ega|o i|ne | dr| na| v |ga | sv|ja |van|svo|ako|pri|co |ico|i s|e s|o p| ka|ali|stv|sti|vsa| ne| im|sak|ima|jo |dru|nos|kdo|i d|akd|i p|nja|o s|nih| al|o v|ma |i i| de|e n|pre|vo |i v|ni |red|obo|vob|avn|neg| bi|ova| iz|ove|iti|lov|ki |jan|a v|na | so|em | nj|a i|se | te|tva|oli|bod|ruž|e i| ra| sk|ati|e p|aro|i k| ob|a d| čl|eva|rža|drž| sp|ko |i n| se| ki|ena|sto|e v|žen|nak|kak|i z|var|ter|žav| mo|di |gov|imi|va |kol|n s| z |mi |ovo|rod|voj| en|nar|ve | je|pos|a s|ego|vlj|jeg| st|h p|er |kat|člo|ate|a z|enj|n p|del|i o|lja|pol|čin|a n|ed |sme|jen|eni| ta|odn| ve| ni|e b|en | me|jem|kon|nan|elj|sam|da |lje|zak|ovi|šči|raz|ans|ju |bit|ic | sm|ji |nsk|v s| s |n v|tvo|ene|a k|me |vat|ora|krš|nim|sta|živ|ebn|ev |ri |eko|o k|n n|so |za |ičn|ski|e d| va|o z|aci|cij|eja|elo|dej|si |nju|vol|kih|i m|nst|kup|kov|uži|la |mor|vih| da|h i|lju|otr|med|o a|sku|rug|odo|ijo|dst|spo|tak|zna|edn|vne|ara|ršn|itv|odi|u s|čen|boš|nik|avl|akr|e o|vek|dno|oln|o o|ošč|e m|ta |vič|bi |pno|čno|mel|eme|olj|ode|rst|rem|ov |ars| bo|n d|ere|dov|ajo|kla|ice|vez|vni| ko|ose|tev|bno|užb|ava|ver|e z|ljn|mu |a b|vi |dol|ker|r s",
    "ayr": "apa|nak|aka| ja| ma|ata|ana|aña|asi|aqe|cha|aki|ñap|jha|mar|aw |kan|ark| ch|una|aru|paw|ti |jh |pat|jaq|rka| ta|a j| ar|hat|ama|tak| wa|ach|iw |a a|ani|a m|spa|na |kap|ki |taq|pa |jan|sa | uk|qe |kis|kas|ha |ina|niw|may| kh| am|at |ati|pan|i j| ya| mu|iti|ka |ayn|t a|as |amp|ch |a u|an |pjh|yni|mun|iña|uka|ajh|ru |w k|hit|ñan|h a|is |isp|qen|khi|isi|has|ejh|e m|sis|atä|oqa|nch|rus|kam|siñ|han|mpi|kañ|qha|sin|asp| in|ham| uñ|ñat|hañ|qat| sa|yas|yat|ita|äña|ska|tap|asa|kha|sit|täñ|tha|arj|ma |a t|ta |tas|nka|sti|iri|sna| ji|a y|ara|pas| as|ñja|rjh| ku| ut|hap|tat|kat|tis|pi |apj|jam|noq|aya|i t|i u|ukh|ura| ka| ju|ans|qas|uñj|asn|a c|nin|aqa|kaj|nañ|sip|i a|us |i m|kun|w u|anc|api|ino|ili|uya|pac|tan|jil|ña |lir|utj|w j|s a|ipa|chi|kiw|w m|kak|muy|pis|rak|hac|isa|njh| lu|mas|amu|ena|nsa|w t|nan|ali|s j|ink|tay| a |upa|wak|a k|way|wa |in | ay|tañ|s m|jas|mp |lur|ank|khu|rañ|h j|t m|iru|eqa|ayt|yt |heq|che|anq|en |lan|rin|ipj|i c|mat|qpa|aqh|tja|awa|uki|k a|qej|anj|sap|pam|usk|yaq|kar|nip|llu|wal|run|yll| aj|lin|a w|ayl|n m|jac|isk|naq|ast|h u|ni |ath|a i|ayk|jhe|aqp|h k|uch|inc|hus|sar|s u|s w| pa|nap|ap | un|ak |n j|tir| ak|ns |s c|ust|arm|ask|war|ri |man|pit|qer|juc|sir|n w|hik|ika",
    "bem": " uk|la |uku|wa |a i|a u| mu|kwa|ali|ya |shi|a n|amb| na|sam| pa|ula|ta |nsa|fya| no|nga| ya|mbu|bu |ata| in| ku|a m|lo |se |nse| ba|ntu|kul|ons|ala|ang|ins|aku|li |wat|mo |tu |alo|a a|ngu|ili|nok|ika|na |nan|a p|ing|a k| al|mu |gu |o n|sha| ca|ila|oku|e a|ikw|yak|ka |lik| um|ana|lin|yal|ga | ci|aba|lwa|ku |ish| fy|uli|a b|u u|unt|i n| on|kal|lil|u y|ba |hi |ukw|amo|po |ulu|kan| sh|kup|ko |we |and|a c|aka|le |u n|cal|o u|ha |ile|ama|umu|bal|kus|akw|u m|mul| if|o a|kut|nsh|o b|ung|apo|e n|kub|mun|uci|yo |mbi|nka|cit|bul| ab|any| bu|pa |ne |u c|u b| ka|abu|ndu| fi|e u|a f|ton| ne|ant|no |i u|u a|ban|o i|cil|cin|ify| ng|pan|tun|gan|nda|kuc|kwe| ns|o c|ngw|o f|ans|fwa|a l|pam|tan|ti | am|kum|kuk|lan|u s| is|wil|du |nya|und| ic|e k|wal|aya|bi |bil|ubu|ush|fwi|int|nta|utu|twa|wab|afw|ela|o m|uko|ako| ta|lam|ale|gwa|win|u k|apa|ma |onk|way|kap|i k|imi|a o|upo| im|iwa|mba|o y|ngi|ici|pak|lul|ind| ma|e p|de |nde|gil|e b|iti|uti|ilw|a s|imb|da | li|uka|hiw|umo|pat|afu|kat|ine|eng|fyo|bun| af|uma|kuf|alw|til|ita|eka|afy|mas|e y|tul|but|nto|usa|kwi|mut|i i| ak| ap|bom|umw|sa |ont| wa|ilo|u f|baf|fik|ina|kab|ano|pal|ute|nab|kon|ash|bwa|ifi| bo| bw|lya|atu|ubi|bik|min|aik|cak|nak|men|ubo|ye |hil",
    "emk": " ka|a k|ka | la| a |la |an |kan| ma|a l|ni |ya |na |ama|a a|lu |n k| di|ɛɛ |di |a m|ma | bɛ| ja|ana|a b|aka|bɛɛ|man|iya|a d|ara|dɔ |jam|alu|en |a s| si| sa| mɔ|mɔɔ|ani| ye| dɔ| tɛ|ye |i s|i a|den| ba|riy|tɛ |sar|ɔɔ |da | al| kɛ| ni|ari|ila|a j| i |a t|n d|ɛn |ɲa |kak|ra |ada|ɛ k|i k|i d|len|u d|ele|nna|sil|n n|n m|olo| se| bo|ade|aar|ɔdɔ|ɛ d| kɔ|ɔ a|ank|ɔn | fa|fan|a ɲ|se |lak|lo | da| na|bol|kel|e k| wo|i m|aya| ke|ko | ad| mi|nu |baa| sɔ|dam|nda|ɔnɔ|mɛn| ko|a f|and|ala|ɛ y|ɔ b|ɛ s|le |ɛ m|i l|i b| wa|n s|a i| de|ina|li |ɔya|mad| mɛ|aba| le|n a| ha|a n|ɔ s|u l|nɲa|han|n b|sɔd|dɔn|kɔn|kɛ |ata|nɔ |kar|dan|in |u k|ɔ m|kɛd|ɛda|i j| su|nnu|a w|ɔ k|nka|lat| gb|ɲɔɔ|aji| an|a h|nin|olu|u m|kun|a g|on |asa| ku|ibi|jib|don| lɔ|i t|waj|bɛn|ɛnn|ban|ɔrɔ|wo |ran|si |ɛ b|ɛnɛ|ɛ l|mak|suu|e m|ii |i f| ɲi|e a|o m|ɲin|enn|usu|ba |ɛdɛ|yan|taa|nan|u b|u t| ɲa|nal|nba|ɲɛ | ɲɔ|law|ati|nad|rɔy|hɔr|a y|iri|sii| hɔ|mir|ti |enɲ|bɔ |u s|n t|u y|ini| te|ta |kol|enb|awa|bat| fu|nki|kil|ili| du|bar|ɛ j|fɛn|fɛ | do| dɛ|gbɛ|su |uus|aam| ta|afɛ|may|lɔ |nni|ɔnn|lɔn|maf|o a|e d| bɔ|din|sab| fɛ|ɔ j|o y|i w|tan|ɔɔy|dɛɛ|bɛd|kad|min|ɔlu|dal|ɔɔl| tɔ|ɔɔn|e f|biy|ali|e b|kɔd|te |wol|bi |e w| mu|ida|du |ant|nɛn|dɛ |ɛ a|dah",
    "bci": "an |be | be| ɔ |un | i |ran|sra|wla| sr|kwl|in |la | kɛ|n b|kɛ |n s|n k| kw| ng|n n|lɛ |a b|n m|le | nu|a k|nun|i s| a |man|n i|ɛn |e k|ɛ n|kun|n ɔ|mun| ni| ti| mu|nin|nga|ti | n |ɛ ɔ|e n|ɔ n| su|ga |ɔ f| fa| ku| li|e s|su |a n|a s|a ɔ|ɛ b|i n|e a| sɔ|wa |sɔ |i k| ma| le|ɛ i|tin|ɔ k|di | at|ata|ta |ɔ l|fat| mɔ|ati|mɔ |lik|akw|ɛ m| sɛ|lak|e w| sa|dɛ |ndɛ|mɛn|i b| mm| yo|iɛ |ba | nd|nvl| nv| kl|vle|sɛ |a a| mɛ| fi|ke |und| wu|ɛ s|n a|mml|liɛ|mla| ka|ike|yo |ɔ t|ngb|i a|e b|a m| an|ɔ ɔ| di| yɛ| si| bo|e t|ndi|bo | ye|o n|n t|e m|fin|e y|n f|sa |ɔ b| fɔ|dan|n y|fa |i i|uma|yɛ | ju| ny|ɔ i|nan| na|kan|ɔun| tr|wun| b | o |n l| aw|a y|b a| wa|fɔu|i f|ɛ a|ing|ge |uɛ |i w|a w|nge|klu|ka |gba|e i|awa|o m|jum|ɔ y|ɛ k|wie|a i|ie | fl|e f| wl|tra| ba|lo |lun| ak|ang|ye | wi|e l| kp|uan|i m| uf|uwa|n w|sie|flɛ|kpa|alɛ|luw|flu|o i|kle|ua | da|nyi|nzɛ|wuk|ɔ s|wo |e ɔ|ika| wo|wan|bɔ |ian| bl|wlɛ| bu|anz|o ɔ| af|aci|u b|bu | ya|ɛ w|ufl|bɔb|te |zɛ |ɔ d|a t|elɛ|i t|ci |nua|fuɛ|ɔbɔ|u i|anm|i l| w |w a| bɔ|o b|lu |se |u m|ilɛ|iɛn| ja|a j|afi|i ɔ|n u| se|unm|nda|yek|bɛn|gbɛ|eku|ɛ l|nma|kac|u s|san|ko |o y|o s|a l|u n|si |anu|aka|any|ɛ d| ko|n j|ɔ w|u a|fi | yi|anw|i j|uka|fiɛ|a d|o a|lel| kɔ|ɔlɛ|ɔn |a f",
    "epo": "aj | la|la |kaj| ka|oj | de|on |de |raj| ra|iu |ajt|as |o k| ĉi|e l|j k| li| pr|eco|aŭ |ĉiu|jn |ia |jto|est| es| al|an | ki|pro|io | ko|en |n k|kon| ti|co |j p|o d| po|ibe| aŭ|ro |tas|lib|ber|aci|toj| en|a p| ne|cio|ere|ta | in|to |do |o e|j l|n a|j d| se|a k|j r|ala|j e|taj| re|rec|iuj|kiu| pe|o a|ita|ajn|ado|n d|sta|nac|a a|nta|lia|ekt|eni|iaj|ter|uj |per|ton|int| si|cia| ha|stu|a l|je | je|al |o ĉ|n p|jta|tu | ri|vas|sen|hav|hom| di| ho|nte|a e|ali|ent| so|nec|tra|a s|ava|por|a r| na|igi|tiu|sia|o p|n l|ega|or | aj|soc|j ĉ|s l|oci|no | pl|j n|kto|evi|s r|j s|ojn|laj|u a|re | eg|j a|gal|ers|ke |pre|igo|er |lan|n j|pri| ku|era|ian|rim| fa|e s| ju|e a|ika|ata|ntr|el |is |u h|li |ioj|don|ont|tat|ons| el| su|go |un | ke|ebl|bla|n s|oma|ĉi |raŭ|kla|u r|ne |ili|iĝo|o t|s e|tek|men|nen|j i|nda|con|a d|ena|cev|moj|ice|ric|ple|son|art|a h|o r|res| un|u s|coj|e p|ĝi |for|ato|ren|ara|ame|tan| pu|ote|rot| ma|vi |j f|len|dis|ive|ant|n r| vi|ami|iĝi|sti|ĝo |r l|n ĉ|u l| ag|erv|u e|unu|gno| ce| me|niu|iel|duk|ern| ŝt|laŭ|o n|lab|olo|abo|tio|bor|ŝta|imi| ed|lo |kun|edu|kom|dev|enc|ndo|lig|e e|a f|tig|i e| kr| pa|na |n i|kad|and|e d|mal|ono|dek|pol|oro|eri|edo|e k|rso|ti |rac|ion|loj|j h|pli|j m",
    "pam": "ng |ing|ang| ka|an | pa|g k| at|ala|g p|at |apa| ma|kar|lan| ki|ata|kin|pam|g m|ara|tan|pan|yan| a |pat| in| ba|aya|n a|g a|ung|rap|ama|man|g b| ni| di|nin|din|n k|a a|tin|rin|a k|ami| la|tun|n i|ari|asa|nga|iya|ban|ati| me|nan| da| sa| na|t k|gan|g s|bal|etu|mag|a i|met|sa |la |ant|kal| iy|kap|a n| mi|in |ya |aka|tau| o |san|n d|au |lay|ana|mak|yun|na |ika|a m|ipa|ran|atu| al|n n| ta|ti |ila|g l|ali|kay|nsa|aga|a p|iti|g t|par|u m|ans|nu |al |g i|t p|iwa|a d|syu|t m|sab|anu|un |uli|mip|ra |aki|aba|u a|mal|as |mil| it|una|bla|abl|ita|awa|kat|t a|ili|kas|g n|lag|da |tas|i a|wa |n l|lal|dap|mas|bat| pr|abi|ap |a b| e |mik|ani|sal|li |ad | an|ral|ira|gal|a r|lin|g d|nte| li|ale|kab|e p|ula|wal|lit|nti|s a|lip|nta|pro|te |ie |wan|ag |tu |upa| ya|g e|tek|usa|g g|bie|o p|it |pun|ian| bi|lat|aku|be |n p|sas|iba|yat|alu|tul|e m|kan|l a|nap|t i|lir|u k|isa|pag|abe|len|e k|rot|en |bil|mam|ksy|ngg|lam|p a|ily|liw|eks|ote|n o|gga|u i|eng|ipu| tu|lya| ri|aul|pas|dan|uri|ema|lab|ta |lak|are| ar|ail|tam|o a| ke|ril| pe|sar| ra|ina|asi|ka |art|pak|sak|mit|rel|i k|gaw| ul| re|inu|i i|mun|abu|asy|mba| pi|ags|obr|gpa|a o|am |n m|mem|o k|isi| mu| nu|mis|nun|era|ndi|ga |agp|aun|mab|anm|lub|gla|e a|nme",
    "tiv": "an | u | sh| na|nan|en | a |ha |sha|shi| i |er |a i| er|or | ma|ar |gh |n i|n u|a m| ve| ci|n s|han|u n| ke|lu |man| lu|n m|yô |a u|u a|n a|r n|a k|mba|in |ii | ha|kwa|ken|n k|na |hin| mb|a a| kw|n n| ga|ga |cii|agh|a n|aa |wag|ve |a s| yô|nge|ba |r u|u i| gb|ana| or|a t|mao|r i|ity|ma |aor|anm|nma|gen|oo | ta|ir |ren| kp|i n|ang|r m|e u|gba| ng|r s| ia|ere|ugh| it|ian|doo|ese|uma|kpa| la|u k|n g|ngu|gu |om |oug|on |ol |a h|ior| ts| he| ne|tar|h u| ka|la |n t|se |e n|r a|a v|hen| ku|aha|mac|yol|i u|ace|ge |ce | de|ish|u t| io| do|tom|hi |a e|u u|o u|i m|iyo|i d|bar|ave|ua |u s| te|igh|a l|e a|m u|a w|un |n c|n e|ne |ev |r k|ind|ene|sen| is|ndi|ker|era| to|a o|ima|u v|a g|paa|n h| wo|di |yar|tya|ase|e s|de |n y|ee |end|him|tes| mk|u m|ka |tyô| mz|won|u e| um|u h| wa| mi|yan|tin|ran|ie |hie|a c|hir|i a|e k|i v|mak| in| za|r c|nen|e l| ig|i k|kur|nah|tse| ik|ves|eng|rum|mzo|men|zou|i l|e i|a d|i e|i i| ya| vo|mlu|ô i|inj|nja| as|vou|ura|ron|gbe| iy|r t|ôro|a y|oru|e e| zu| ti|ra |n l|ci |u l|ver|kpe| fa|was| ml|e m|em |io |mi |da |civ|môm|ant|see|ivi|wan|vir|nda| ij|soo|zua|lun|ea |vea|wa |ôm |av |hio|ake|a f|igb|l i|u z|r l|zan|nta|e g|hem|h s| mt|ded|iky|o s|r g|do |ndo|iji| hi|e h",
    "tpi": "ng |ong|lon| lo|im | ol| na|la | ma|pel|ela|ri |at | bi|ait|na | yu|ol |gat| ra|bil| ka|ilo|man|rai|t l|it |eri|mer| o |wan| i |mi |umi| wa|ing|yum|ta |t r|tin|eta|get|lge|olg|iga| ig| sa|ara|em |rap|i o|ap |nme|anm|in |ain|an |a m|ant|ape|nar|m o|i n| no|g o|g k|i i|as |ini|mas| me|n o|sim|tri|kan|kai|ntr| ga| st|a s| pa|gut| ha| wo|g y|yu |a l|g s|ama|m n|ok |g w|wok|spe|a k|i b|i m|g l|i l|sin|sam|pim|m l|kam| gu|l n|amt|tpe|g n| in|ts |a i|mti|utp|isp|kim|its| la|isi|aim|api|lo |o m|g b|tai| di|a o|dis|a t|p l|en |map|t w|s b| lu|luk|sem|no |tim|lai| ko| ki|ave|ols|nog|m k|lse|sav|nem|ve |a p| fr| em|nim|tu |i y|nka|et |m y| ti|g t|nap|g p|sta|tap|aun|a n| tu|un |asi|fri|pas|n m|m g|l i|aut|ane| sk|kau|t n|nta|sen|n s|oga|i g|g g|m i|kis|o i| ba|tok|os |usi|m s|ngt|anp|a w|s n|a h|s i|iki|i s|sai|l m|npe|ari|o l|o b|g r|ik |uti|iti|gti|aik|ut | to|a g|ili|a y| pi| ta|kin|ni |n b|lim| ye|yet| we|k b|ina|g m|uka|str|ins|rid|a b|anw|nsa|nwa|m w|m m|dom|ot |hap|ido|aus|i w| ne| si|n i|t o|dau|ese|rau|ank|sap|o k|m b|nin|pos|o n|am |go |s o|s l|u y|pik|vim|ivi|es | go|n n|kot|ron|ple|g d|a r|kul|ali|sku|apo|om |g h|l l|s s|ti |les|t m|gav|eki|nai|mek|kom| as|ind|nda|ip |liv|ul |ati",
    "ssw": "nge|eku|a n|ntf| le|e n| ng|tfu|lo |la |nga| ku|fu | ne|o l|khe|tsi|nkh|le |he |unt|elo| lo|si |ele|a l|ni |ung|mun|ma |lun|lel|wa |lek|nom| um|eni|oma| no|kut|hla|onk|a k|e l|ent|e k|gel|ela|ko |eli| ba| la|pha|ats| em|o n|ang|ema|eti|nel|nye|ban|ulu|uts|hul| na|aka|tfo|e u|lan|oku|lok|won|khu|esi|lul|a e|ule|ala|umu|tse|akh|ye |ve |i l|nek|ana|ane|lil|kwe|aph|na |we |ke |aba| wo|nti|ndl|ale|i n| ye|ba |ilu|gek|gan|lab|any|hat| li|tin|wen|gen|kel|len|ndz|fo |and|let|eko|e b|lwa| ka|te |set|nem| kw|mal|ka |ant|alu|ne |phi|ing| un|u u| ek|ise|une|e e|kul|nal|lal|mph|o y|uhl|fan|‐ke|ile|i k|kub|ukh|ben|kan|ako|a b|kat|eke|ive| ti|sek|nak|sit|seb|u l|alo|yel|kho|wo |kha|les|o e|ngu|kus|lom|ini|ikh|elw|isa|sa |fun|e w|ebe|o k|jen|iph|eng|kwa|ahl|uph|emb|be |tis|lwe| si|etf|isw|uma| se|ene|ta |nan| im|i e|enk|e a|abe|kun|ume|hak|nen|dle|ase|sen|kuv|tel|ebu|omu| in|lin|sel|tfw|nhl|a i|e i|kuk|uba|ti |kuf|mhl|bon|ula|sin|int|fut|dza|lak| wa|ind|ave|ali|yen|ete|to |ngo|use|kuh|hol|ze |a‐k|ona|a a|se |nje|und|swa|lon|eki|ike|i a|lis|tsa|gab|sim|i w|its|fol|e t|o m|hi |ndv|phe| ya|ma‐|utf|sik|liv|bun|cal|nta|ata|gal|mel|ute|wem|gap|han|uny|oba|alw|ili|a w|mbi| bu|gob| at|awo|ekw|dze|u n|emp",
    "nyn": "omu| om|ntu|tu | ku|a o|ra | ob|wa |obu|ari|a k|mun|a n|unt|mu |uri|nga| mu|aba|ri |a e| na|e o|gye|rik|ho |a a|han|ang|re |ga |iri|bwa|oku|aha|bur| bu|na |eki|ka |iku|ire|uga|ndi|ush|ban|ain|ere|ira|we |kur|sho| ek| ab|ne |ine|a b|and| ni|u a|e k|sa |u b|iha|i m|e n|kir|be |aho|bug|ibw| eb| ba|ing|ura|gir|u n|kut|ung|ant|abe| ah|ye |e b|i n| bw|kwe|ebi|era|iki|ba |ro | kw| ok|uba|gab| no|zi |bir|i k|u o|o o|rwa|o e|kub|end|ama|mer|eka|kug|ate|tee|di |rir|bus|kuk|rin|ish|sha|i b|wah|ha |u m|bwe|ngi| ai|ara|kwa|kan|o g|za |ngo|kuh|ana|i a|eme|eek|i o|baa| ka|go | gw|nib|zib|ash| or|iro|she|o k|u k|iin|o b|iba|oon|gan|agi|ngy|hem|mwe|ona|oro|bwo| ar|ya |i e|uru|nar|eir|uta|tar|kwi| ti|egy| n |hi |bar|isa|ute|o a|shi|ora|e e| en| ki| nk|riz|nda|da |ja |si |nsi|wen|yes|tek|yen|aga| am|o n|rei|rag|ki |obw|mur| ha|ris|wee|amb|aab|bya|kus|ugi|a y|ind|ata| ne|bas| ky|ija|hob|ikw|mus|gar|a g|eky|dii|bor|aar|ibi| we|aka|ham|emi|ekw|rer|ini|har|gi | bi|naa|kor| er|gwa|n o|iza| by|eih|yam|iho|rih|i y|ete|o m|eby|but|a r|ika|mag|ozi| em|ong|iik|iko|uka|nik| yo|sib|eri|utu|tuu|amu|uko|irw|nka|ani|yaa|u e|mut|roz|mub|ens|aij|nis|uku|kye|nde|der|e a|nok|nko|asa|aas|hab|obo|ent|ahu|rye|oba|kih|yob",
    "yao": "chi|ndu| wa|du | ch|a m|aku|akw|ni |kwe|und| mu|wak|wan|mun| ku|la |e m|wa |ulu|amb| ak|kut|u w|ali|mbo|lu |we | ma|le |ufu|ful|ila|a k|bo |a n| ga| ni|amu|kwa|se | na|ose|hil|nga|go |aka|and|ang|na | uf| pa|ete|uti|jwa|kul| jw|son|ngo|lam|e u|ne |kam|oni| so|u j|e a|ele|a c|ana|wal|ti |isy|cha| yi|gan|te |ya |mwa|lij|wet|che|ga |yak|ili|pa |e n| ya|o s|nda|i m|ula|jos|i a|ile|ijo|li |e k|o c|a u| mw|ich|mul|uch|o m|asa|ala|kas| ka|i w|ela|u a|ach|his|nam|lan|yin|i k|ind|ani|sye|yo |si |pe |gal|iwa|man|sya|aga|a w|o a|ule|ikw|asi|kus|ope|ma |gak|e w|jil|kap|hak|ika|ite|aji|mba|u g|ase|mbi|kum|uli|any|ape|a y|ekw|mal|imb|ja | al|end| ng| ja|mas|usi|kup|e c|pen|ye |anj|ka |a j|a p|lem|o n|ama|him|ago|sen|eng|ane|ako|mch|ola|och|oso|ena| kw|sop|lek|pel|gwa|hel|ine|gam|u y| mc|i y|awo|ons| mp|ole| li|wo |i u|hik|kol|auf|mka|tam|syo|e y|mpe|ten|ati|mau|nji|wam|muc|ong|i g|kan|uma|je |iku|nag|kwi|da | ul|cho|ngw|ene|iga|ano|esy|ion|upi|pag|o k|eka|wu |uwa|kuw|sa | un|a l|bom|iya|uni|jo |ale| ji|apa|yil|lil|uku|i n|o g|a a|o w|waj|mus|ipa|pan|pak|one|i c|ujo|duj|emw|nya|tio|jak|oma|nja|hiw|dan|apo|e j|poc| wo|lic|alo|eje|ing| mi|e p|lo |lig|a s| yo|ung|no | m |upa|ata| bo|nde|he |i j|was",
    "lav": "as |ība| un|un |tie|ies|bas|ai | ti|esī|sīb|ien| vi|bu |vie|ir | ir|ību|iem| va| pa|em | ne|s u|am |m i|šan|u u|r t|pie| ci| sa|ās | uz|vai| ka| pi|brī| iz|rīv| br|uz |cij|dzī|ena| ar|ar |isk|s p|es | at|āci| ap|ot |nam|viņ|inā|ikv|kvi| no|s v| ie|vis| ik|i i|pār|u a|ju |nu | pr|edr|vīb|īvī|iju|drī|u p|dar| st|lvē|cil|ilv|s t| la|iņa|ana|s i|n i|īdz|s s|kā |tīb|i a|ija|bai|ībā|ied|s n|arb|val|līd|s b|aiz|tu |iec|cie|ām |gu |vēk|īgu|īgi|ka |jas|umu|mu |t p| jā|u v|zīb|ska|lst|als|kum|gi |s l| tā|jot|stā|st |n v|vēr|a p|arī|aut|n p|ama|kas|u k| da| ta|nīg|izs|ojo|anu|ņa |u n|sta|s a|ba | ai| so|s d|a u|ā a|stī|cīb|m u|i u|son|not|mat|sav|iev|ā v|jum| kā|u t|ned|ajā|s k|u i|i v|līt|ēro| pe| dz|i n|per|u d|īks|kat|nāt|līb|nāc|rdz|nīb|pil|rīk|kst|a s|cit|pam| pā|ekl|tau|u s|bie|jā | re|i p|kur|a a|t v| li|evi|tis|evē|bā |ma |rīb|a v|os |ras|abi|nev|iku|skā| ve|lik| lī|nas|t k|ant|uma|roš|kād|zsa|sar|ciā|mie|ais|eci|oci|oša| je|jeb|būt|atr|n b|ieš|rso|ers|soc|enā|a t|t s|īša| be|bez|āda|ebk| ku|glī|isp|tot|spā|roj|lie|pre|ret|aul|na |tra|iet|du |zgl|āt |ard|kt |ier|izg|ikt|paš|iāl|nod|ts |eja|ā u|sab|eno|ēt |ta |tik|tīt|ecī| de|īga|tar|arp|r j|īst|tās|ja |enī|atv|vu |ārē|rēj|rie|oši|dro",
    "quz": "una|an | ka|nan|cha|ana|as |apa|pas|man|lla|aq |sqa|ta | ru|run|kun|ach|qa | ll|pa |paq|na |nta|chi|npa| ma|nch|aku|anp| ch|in |a r|ant|hay|mi |taq|ay |ama|asq|qan|tin|kuy|chu|lap|a k|yta|a a|ima|wan|ata|spa|all| wa|n k| ja|ipa| ya|nin|ina|aqm|his|qmi|a m| ju|pi |anc|nap|iku|aus|usa|kau|pan|nak|kan| mu|naq|aqt| pa|kam|aqa|kay|i k|kus|un |ank|isq|nku|may|yku|ayn|a j|a l|ayt|qta|ati|a p| pi| ri|aci|lli|lin|ayk|uku| al| at|n r|yac|ion|pip|han|inc|n j|ayp|yni|qpa|nac|say|asp|uy |mac|s m|cio|awa|a c|laq|tap| yu| im|a y|yoq|n m|asi|mun| de|has|n a| as|n c|int|uch|nma|s k|oq |ari|q k|hu | na|ypa| tu|tuk|tun|atu|rim|q r| sa|jat|yan| ji|nat|anm|jin|a s|api|hik|uya|nti|pac|tan|ash|mas|n p|n l|k a|ura| su|a q|yuy|n y|ech|q j|unt|yay|ypi|is |lan| qa|usp|kas| an|a w|s w|inp|sin| ta|ma |a t|shw|q a|hwa|uyt|nmi|sim|ere|rec|der|uma|s t|isp|n t|ña | ni| ay|upa|nam|hur|war|waw|imi|nka|sap|kaq|s j|was|y r|usq|kin| un|inm|qas| si|ani|tiy|t a|sta|pay|pis|maq|hin|ha |arm|npi|rmi|ink|aqp|q c|la |i p|nis|yma|nk | ku|aym|nal|hak|rik| ti|unc|niy|y s|iyo|juc| qh|ist|pap| aj|s y|cho|onq| re|ayo|iqp|n s|s p|os |i m|t i|ras|ita|piq|qsi|ku |yqa|mik|q y|eqs|pat|tak| pu|lak|i r|ipi|iya|ywa|muc|a n| qe|san|jun|y l",
    "rmy": " sh|ri | a |shi|hi |i s|ti |ea |ari|i a| ca|rea|tsi|i c| s |a a|ndr|tu |câ |dre|i n|ept|ptu|rep|li | nd| di| un|a s|are|i u|ats|la | la|i l|ear| li|lje|di |ati|lui|ui |a l| tu|tat|â s|ei |sea| ti| câ|un |jei|or |caf|afi| lu|â t| ar|ali|i t|fi |ilj|a c|bâ |râ |car|ibâ|lor| cu|nâ |icâ|a n|i d|s h|hib|tâ | hi|â a|si |u c|eas|tur|tul|ber|â c| in| co|lib|u a|n a|cu |ibe|u s|tea|lu |tsâ|ul |tse|int|a p|i i| pr|u p|i p|url|i m|lji|min|sti|alâ| al| pi|sht|nal|â n| si|ji |â p|rar|ert|sii|ii |nat|til|u l|sâ |lâ |â l|sta| nu| ic|i f|nu |ist|mlu|ili|a t|ots|uni|rta|a d|its|â d|pri| ts|oml|i e| de| na|sia| po|gur|tut| st| at| ân|ura|al |ita|anâ| ma|ips|can|oat|tsl| su| as| so|ând|nts| ap| ea|sh |nit| mi|ent|a i|ate| ac|poa|ilo|sot|ina|ash|ona| lj|âts|rli|lip|â i|unâ|t c|iti|bli| u |nji| fa|zea|tât|ril| om|urâ|con|i b|sig|igu|ntr|pur|par|ntu|let|com|iil| ni|eal|ind|r s|hti|at |ucr|art|adz|arâ|itâ|rtâ|inj|uri| eg| sc|atâ|sin|ral|pse|asi| ba|r a|apu|âlj|ia |chi| va|sun|ter|rlo|ica| pu|luc|unt|i v|ise|ini|est|ast|gal|ega|act|nda|ead|uts|a u|imi|ma |ra |pis|s l|ets|a o|va |pi |lit|scâ|asc|ial|sa | ta|rim|tar|alt|idi|tlu| gh|era|ant|eri|aes|a m| nâ| ae|oar|nea|pro|apt|ana|ta |atl|lic|l s|iun|nte|mil",
    "src": " de|de |e s|os | sa|tzi|tu | su|one| a |sa |ne | e | in|ent|ion|der|su |zio|ere|as |e d|a s|u d|ret|es | cu|ess| pr| so|s d|men|ale|ade|atz| s |re |e c|sos|in |s i|chi| un|nte|ten|etu|er | pe|et |e e|ida| te|le | is| ch|ene|are| es|a p| si|u s|a d|pro|hi |dad|te |sse|tad|zi |e t| on|e i|s e|nt |nzi|u a|sso|onz| co|ame|cun|tos|e a|sas|a c|ntu|net|na |e p|at |nes|du | li|t d|n s|son|s a| o |ber|ro |pes|u e|int|zia|nat|i p|ia |res|nu |un | re|sta|s p|ter|era| po| di|per|s c|t s|rar|ser| at|e o|s s|ibe|lib|si |tra|ust|u c|rta|unu|cus|ntz|adu| to|da |nal| na|ant|egu|eto|und|ine|i s|a e|otu|u p|t a|ert|est| da|a a| fa|ist|ona|pod|s o|pre|iss|ra | ma|ica|tot|les|ntr|una|sua|con|dae|ae |s n|man|sia|ndi|nid|ada|a l|nta|o s|a i|ua |ide| ne|otz|min|rat|iat| pa|nde|ode|dis|ren|ali|a u|ta |u o|sot|u t|ime|ssi| as|o a|pet|e u|nsi|fun|lid|epe|eru|unt|st |t e|end|us | fu| ca|ner|dos|s f|ass|nda|uni|das|iu |ind|a t|ial|a f|ghe|gua| eg|a n| se|ont|etz|s m|s ò|sti|t p|ual|nen| me|sen|com|ura|a b|lic|a o|pen|ado|nos|inn|des|seg|e f|din|òmi|ire|a m| òm|e l|dep|ènt|for|ena|par| tr|u i|ara|cra|sid| no|s u|u r|suo|e n|pri|ina| fi|ria|gur|art|det|s t| bo|tar|emo|run|ama|icu|isp|dam|e r|itu|cum|tut|eli| bi",
    "sco": " th|the|he |nd | an|and| o |al | in|ae |in |es |ion|cht| ta|tio|or |t t|ric| ri|ich|tae|on |s a|is |e a| aw| be|s t| he|ati|ent|ht |ts |e r| co|er | na| fr|bod|ody|his|dy |hes| fo|e t|o t|for|it |ng |ty |n t| or|be |fre|ree| hi|l a|ing|awb|wbo| sh|s o|ter| on|sha|nat|r t|nal|an |n a| as|hal|e o|y a|d t|tit| pe|l b| re|y h|aw | ma|nt |men|air|ce | pr| a | ti|hts|e f|e c|le |eed|edo|dom|n o|e s|ons|d a|res|e w|man| wi|d f|ed |sta|ar |t o|ona| it|ity|at |as |her|ers|t i| de|con|til|il | st|nti|e p|e i|e g|nce|ny | so| di|nte|ony|ns |und|ith|thi| fu|ie |ir |oun|ont|e e| un|pro|oci|nae|y i|lit|soc|com|nin|en |ic |ne |r a| me|ly | wa|ear|ual| en|ame|uni|r i|e h|hum| is|ane|uma|ess|inc| fa|equ| hu|ver| eq|e m|hei|o h|ms |d o| ha|wi |t n|s f| no|t a|int|cla|rit|qua|d i|iti| se|rsa|y s|ial| le| te|e d|r o|ive|r h| la|nit|om |ite|s r|cie|s i|ali|cti|cia|re |aim|rat|ld |tat|hat|rt |per|s h|n f|dis|tha| pu| we|g a|oms|eil|ntr|fai|tri|ist|ild|e u|r s|dec|lea|e b|hau|imi|mai|s n| ac|elt|lt |l t|omm|d p| ga|din|war|law|eme|y t|era|eir|art|ds |s e|ral|nor|tel|ge |g o|eik|eli|rie|rou|nda| gr|lan|mei|ate| ge|n i|ten|id |s d|ors|iou|bei|sam|nta|sec|mmo|lar| tr|ful|ul |mon|s w|anc|l o|gar|ern|ara|d s",
    "tso": " ku|ku |ni |a k|hi | ni|a n| a |i k|ka |i n|wa | ya| ma|la |ya |na |a m| ti| hi|fan| sv|nel|hu |a t|ane|ela| ka|iwa|u n| na|svi|lo |nhu|a l|a h|ele|le |ndz|u k|va | xi|a w|vi |mbe| à |elo|wu | wu|eli| mu|u y|mun|i l| le|nga|umb|lan|nfa| va|u l|be |u h|li |kum|tik|ihi|iku|aka|unh| wa|a s|liw|isa|i m| fa|ma |anu|nu |u t|han| la| ng| wi|wih| ha|a x|yel|a a|lel| nf|i h|ta |ana|o y|e k| nt|u a|i a|eni| li|ndl|ga |any| ko| kh|van|u w|u v|amb|a y|ti |sa |pfu|i t|i w|in |lek|e y|ang|and|ati|yi | è |irh|sva|mat|ani|i s| nd|a v|mel|yen|hla|isi|hin| ye|eke|n k| lo|ulu|kwe|hul|thl| kw|nth|tin|mah|wan|ava| mi|ko |khu|u s|à n|dle|lul|ule|tir|o l|i y|aha|aye|kwa|inf|à k|è k|rhu|mba| th|fum|end|anh|xi |dzi|kel|a f|u f| lè|we |may|eka|nye|gan|dze|vu |ham|xim|mis|thx|aku|tà |xa |hlo| tà|eyi|ima|nti|eki|ngo| si|u p|vak|ngu|lak|ume|oko|lon|a è|o n|lok| ta|zis|hak|u m|i à|ke |i x|u x|rhi|ha |awu|dza|u à|za | là|n w|ung|e n|a à|i f|esv|les|vik|siw| y |à m|to |mha|ola|sav|ond|nya|kot|kol|uma|e h|mbi|e s|naw|ths| dj|fun|mu |a u|xiw| ts| hl|u d| lw|nyi|ki |ong|sun|lwe|ike|ind|nis|xih|e a|èli|imu|sel|sek|iph|zen|lum| pf| xa|sin|umu|sim|ave|kar|ala|wey|sik|o t|avu|wav|oni|ile|wak| yi|ali| hà|gul|e l|ba |i v",
    "men": " ng|a n|i n|ɔɔ |ti | ti|i l| i | ma| nu| gb|ngi|a k|aa |gi | kɔ|ia |ɛɛ |ei | na| a |ma |hu | ye| ta|kɔɔ|a t|na | hu|a m| kɛ| nd|gbi|ya |bi |i y| lɔ|a h|ɛ n|ii |ɔny|u g|i h|nya|uu |lɔn| kp|i m|ngɔ|nga|la |i t|kɛɛ|lɔ |i k|ɔ t|mia| mi|a y|nge| ji|ee |gaa|a a|ɔ n|ɔ i|gɔ |ind|tao|ao | hi|num| le| yɛ|umu|mu |ung|nda|hin|ye |i g|hou|hug|e n|ugb|ni |a l|sia|ndɔ|nuu|a i|maa| ya|ahu|gba|u k|mah|oun|ɔma|le |da |i w|ɔlɔ|i j| va| ɔɔ|eng|i i|va |yei|dɔl|li |lei| sa|yɛ |kpɛ|yil|isi| la|bat|a w|u n|e t|ta |ahi| ki| wo|ɔ k|e a|ɛlɛ|saw| lo|o k|ji |gbɔ|pɛl|uvu|ili| ho|vuu| gu|nde|aho|gbu|ɛ t|ale|ila|nah|kɛ |ɛi |ndu|kpa| wa|nuv|ge |e m| ny|e k|atɛ|wei|awe|a g| ii|bua|ie |awa|wot|yek|kɔl|ulɔ|ing|ga |gul|tɛ |ɔle|u t|gbɛ|ɔ y|nun|wa |hei|ani|ɛ k| tɔ|bɔm|ɛ g|ein|taa| ha|ang|uni|u i|ekp|ɔ g|lɛɛ|kpɔ|a v|kpe|ote|i b|te |u m|tii|ɔ s| we|ɛ h|baa|pe |ɛ y| ɛɛ|i ɛ| ba|fa |a j|bu |ifa|kia|jif|u l|eke|ama|gen|u w|lee|lɛ | lɛ|ɛmb|a b|e y|aah|hii|ngo|bɛm|lek| wi|ui | yi|u y|bɛɛ| he|u a|e h|ɔ m|uah|o g|yen|yan|nyi|aal|hi |wu |yee|maj|ajɔ|jɔɔ|nye|mbo|e g|u ɔ|ong|ka |oi |lon|dun|uny|ɛng| sɔ|lɔl|nyɛ|lii|a p|oyi|iti| bɛ|lɔm|akp|e i|ɛ i| ka|jis|oko|i p|ɔla| wɛ|a s|ewɔ|iye|dɔɔ|lok|gua|ɛ b| li|u h|nin|wee|lah|ula| ga| du|i v",
    "fon": "na | na| e | ɖo|ɔn |ɖo |kpo| kp|nu |o n| ɔ | nu| mɛ| gb|mɛ |po |do |yi |tɔn| é | si|gbɛ|e n|in | to| lɛ|lɛ | tɔ|nyi| al|wɛ | do|bo |ɛtɔ| ny|tɔ |e ɖ|ɖe | bo|okp|lo |ee |ɖok|to |ɔ e|bɛt| wɛ| ac|a n|sin|acɛ|o t|o a|ɛn |i ɖ|o e|bɔ |ɔ ɖ| bɔ|cɛ |ɛ b| ɖe|a ɖ|ɔ n|ɛ ɔ|n b|an |nɔ |odo|ɛ ɖ|o ɔ|ɛ n|ɛ e|ɖɔ |ji | ɖɔ|lin|n n| en|bi |o ɖ|mɔ |n e|pod| bi|lɔ | mɔ|n a|nɛ |ɛ k|i n|un |ɔ m|i e|mɛɖ| hw| ji| ye|ɛɖe|enɛ| ǎ |alo|o s|kpl|u e|a d|ɔ b| nɔ|alɔ|ɔ é|ɔ g|ɖee|si |n m|gbɔ|a t|n k| yi|sɛn|jɛ |e k| wa|o m|e m|é ɖ| jl|hɛn|e e| hɛ| sɛ|nnu|nun|wa |n ɖ| ee|é n|kpa|unɔ|bɔn|ɔ t|a s|ɛ é|u k|ɔ w|inu|e s|i t|zɔn|o l|a y|o g|bɛ |ma |n t|e j|ɔ s|ɔ a|o b|a z| zɔ|jlo|i k|nuk|ɔ k|a e|ɔ l|u t|kɔn|xu |e ɔ| lo|hwɛ| ka|eɖe|o y|e w|jij|sis|n l|ixu|six| su|ali|isi|ukɔ|ɛ a| ay|ayi|su |n g|u a|a b|n d|dan|nmɛ| ta|n ɔ|etɔ|e g|o j| we|onu|wem|ba |ema|ɛ g|o h|ɛ s|ɛ t|i s|u w|n s| sɔ|bǐ | bǐ|hwe|a m|sɔ |lɔn|o d|u m|ple| ma|ɛ l|azɔ| az|tog|ye |i l|hun| jɛ|o w|ogu|o k|u g|kan|oɖo|elɔ|gbe| le| el|wu |ka |ɛ w|n w| li|sun|esu| hu| i |ɖó | ɖó|plɔ|ɖi |ɖè |ɛnn|pan|i m|yet|xo |iin|tii| ti| fi|e b|zan|i w|poɖ|ɖes|a j|ann|a g|gun| ɖi| tu|gan|ɛ m| wu|u s|ɔ y|a l| da|u n|u l|ɔnu|obo|ɔ h|vi |lee|ijɛ|ta |e a|ya |nuɖ|ɔ d|wen| tɛ| ga| ɛ | xo",
    "nhn": "aj |tla| tl| ti|ej |li |j t|i t| ma|an |a t|kaj|tij|uan|sej|eki| no|chi|ij | ua|ma | to| te|j m| ki|noj|ika| se|lis|j u|aka|laj|tle|pa |pan|j k|ka | mo|amp|ali|ech|uaj|iua|j n|man|oj |och|tek|tli|kua|ili|a k|se | pa|ano|ise|ual|mpa|tec|n t|en |len|iaj|is | ue|a m|jto|ajt|pia| am|uel|eli| ni|ya |oua|j i|ni |hi |tok|kin|noc|one|lal|ani|nek|jki|ipa|kit|oli|ati|amo|j s|kam|aua|ia |tim|mo | ku|ant|stl| ik| ke|opa|ase|nij|ama|i m|imo|ijp|ist|tl |ijk|tis|mej|itl|tik|mon|ok |lak|par|n n|ara|ra |tit|kej|jpi|a s|ojk|ki | o |alt|nop|maj|jya| ka|iti|cht|ijt|uam|a n|kiu|lat|leu|o t|ita|lau| ip|tep|kia|jka|n m|ana|lam|kij|nka|tou|epa|n s|til|i n|i u|e t| ak|s t|k t|lti|nem|lan|eyi|mat|nau|ose|emi|j a|ntl|uat|uey|jtl|nit|nti|kip|oka|onk| on|eui|i k|kat|j p|ini|toj|kem|ale|ajy|ame|ats|pal|iki|ema|uik|n k|eua|ach|e a|ijn| sa|mpo|tot|otl|oyo|mil|hiu|eka|tol|ajk|uak|ite|san|pam|atl|yek|tia|ate|ino|jua|a i|ipi|j o|tsa|oke|its|uil|o o|jne|oju|tos|kui|oui|a a|yi |kol|ote|a u|i i|n a|ken|chp|iko|as | ne|tin| me|ank|jti| ye|kon|ojt|aui|xtl|ine|tsi|kii|you|ko |ejk|o k|uas|poy|tst|ejy|nok|las| ya|yol|hti|pou|siu| in|nel|yok|mac|ak |hik|sij| si|sto|htl|jke|nko|jch|sek|mot|i a|ela|ui |kis|mel|axt| ax|ijc|nan",
    "dip": " ku|en |ic |ku | bi|bi | yi| ke|an |yic|aan|raa| ci| th|n e| ka| eb| ra|c k|c b|n a|ci |in |th |kua|ny |ka |i k|ŋ y|i l|ben|k e|ebe| ek| e |höm|nhö|öm | al|ai |kem| ye| nh|eme|m k|men|i y|t k|n k| la|c e|ith| er|lɛ̈|thi|alɛ|ua |t e|ek |ɛ̈ŋ| lo|ɔc |n t|ŋ k| ep|u l|it |yen|kɔc|̈ŋ |de |k k|pin|a l|i r|n y|epi|n b|lau|at |iny|aci|aai|u t|ken|au |ok | te|a c|ath| pi|ke | ac|e y|cin|u k|oŋ | lu| ti|a t|uat|baa|ik |tho|yit|ui |hii|u n|h k|e r|n c|te |kek| lö|l k|h e| lɛ|hin|thö|m e|ɛŋ |n r|n l| et| mi|ëk |i b|ekɔ|era|eŋ |e w|i t|el |ak |nhi|iic|a k|i e|pio| ny|ŋ e| aa|nde|u b|e k|kak|eba|ök |k a| ba| en|ye |lɛŋ| pa|iim|im |köu|e c|rot|e l| le|öŋ |ot |ioc|c t|i m|r e| kö| kɔ|eth|y k|oc |ŋ n|loo|la |iit| el| we| ey|i p|uny| ro|ut | tu|oi |e t|enh|thɛ|m b|hok|pan|k t|ëŋ | wi|yii|tha|wic|pir| li|u e|bik|u c|ën |ynh|y e|lui|eu |ir |y b|nyn|uc |n w|mit| ec|öun|any| aw|ɛt |ɛ̈ɛ| dh| ak|and|loi|wen|l e|höŋ|e e|thë|aku|̈ɛ̈|kut|am |eny|u m|i d|iek|k c| ko|tic|leu| ya|u y|tii| tö| ma|nyo|tö | ew|hök|den|t t|hëë|i n|k y|i c|cit|h t| ed|uee|bai|ɛ̈n|öt |eri|ɛ̈k|awu|rin|a p|cɛ̈|hai|kic|t a| të|tue|cii|hoŋ| bɛ|ooŋ|n p| cɛ|̈k |c l|u p|uk |c y|löi|i a|eke|dhi|wel|thk|eeŋ|öi |elo|n m|r k|ien|om |hom| wa|nho",
    "kde": "na | na| va| wa|la |nu |a k| ku|a w|ila|wa |a v|chi| mu|unu|e n|mun|van|a m|a n|ya |le |ele|sa | ch|asa|amb|ana|was|lam|mbo|ohe|ave| vi|ne |bo |aka|e v|a u|u a| n’|u v|e m|ke |anu| li|ve |vel|ake|ala|hil|ile| pa| av|ng’|a l|he |ing|ene|ela|ili|ika|vil|ngo|vak|ali| di|uku|wun|any|lan|a i|mbe|a a|uni|e a|ama| ma|go |nda|bel|emb|wak|kuw|nya| mw|ola|a d|den|lem|a c| il|ulu|kol|g’a|o v|nji|kan|ji |au |ma | au|lil|mbi|uwu|lik|ye |’an|kuk|din|ula|no |and|umi|kum|eng|ane|dya|ong|o l|ach|mwa|e w| ak|an’|a p|kal|nil|lew|mad|n’n|voh|ilo|wen|aya|apa| vy|kut|ale|va | al|ang|ava|kul|hin|o m|hel|e k|ond|hi | la|lin| lu|idy|dye|u l|da |ole|ka |ani|ndo|ton| in|ewa|lov|o c|dan|u m|cho|uva|ia |pan|kam|we |ove|nan|uko|bi |kav| ya|lim| um|eli|u n|nga|uli|lia|mil|o n|’ch| kw|li | an|aha|dil|ata| dy|e l|n’t|i v|tuk|hoh|u i|hev|ni |niw|und| ul|ade|lel|kay|lon|e u|ino|i n|nje|uwa|she|yik| ly|hum|ako|i w|uma|vya|kwa|ba |’ma|val|kil|mwe|mba|mu |pal|umb|wav|hih|ulo| ka|e c|nde|wal|ima|’ni|lun|ihu|a y|vin|yoh|e i|vyo|inj|u c|kup|kuv| ki| m’|a s|e p|dol|lek|awa|o u|n’c|iwa|imu|anj|mal|yen|u w|yac|bil|oja|o a|ha |utu|ech|i d|uka|taw|n’m|ita|awu|ina|m’m|i a|itu|hon|lu |atu|mak|iku|lya|lit|jel|evo| vo|i l|mah|hap",
    "snn": " ba|ye |bai| ye|ai |e b| ca|ai̱|ia |ji | ne| si|i̱ | go|goa|sia|i n|e c|a y|i y|̱ b| ja|se |aye|i j|a b|jë |iye|e g|re |oa |hua|yë |quë| gu|hue|e̱ |u̱i|gu̱|ne | ma|̱i |je̱|eo |e s| hu| ña|bay|o y|ñe |ja |ajë|to |aij|deo| ñe|a i|ayë|ba | ji|beo|cat| de| be|e j|i s|mai|e e|bi |a ñ| co| e |ato|uë |ña |i g|e ñ|i b| iy|cha|ë b|eba|coa|na | ts|e y|̱je|reb| i | ti|i t|ja̱|ach|ue |e i|i c|ni |oac|e t|a ë| re|je |aiy|oji|eoj|a̱j|oye| ë |ë t|cay|ija|ico|ihu| sa|i d|ere|a c| qu|ahu|iji|ca |ua | yë| to|a h|ase|ues|ë s|aca| se|uai|e d|ese|asi|caj| ai| tu|tut|utu|ë c|yeq|equ| na|cai| i̱|ti |mac|e m|ë g|ebi|a a|ani|tu |e n|yeb|eje|oya|toy|co̱|a m|̱ t|ije|sic|eso|eoy|a t| a | te|haj|cah|oas|are|i m|a s|ehu|añe| da|o b| do|i i|i r|e r|neñ|yer|huë|ë y| o |jai|a j|aje|a g|ibë|ëay|aña|aja|a o|coc|bëa|oca|sos|doi|oi |aco|eñe| jë|ë d|ë j|cas|ëca|hay|ea |̱ g|ari|tsi|yij|sai|̱ c|osi|teo|o h|co |̱re|nej|ëhu|o s|ose|jab|̱ni| me|rib|ñes|si |yaj|jëa|uaj|ë m|dar| yi|oe |e o|nes|i̱r|ma |nij|i h|oja|uëc|ama|ë i|i̱h|o̱u|̱uë|̱hu|aqu|ëco|e a|a̱ |ëja|̱ñe|o̱a|go̱| ëj|ñe̱|tia|abë|sih| bi|tsë|sëc| je| cu|̱ a|ned|cab|a d|ore|me | oi| ro|jay|tso|ë r|eye|ta |bë |ñaj|soe|̱ca|o̱c|año|o c|ire|ohu|uej|ñej|i a|ñas|ë q| ju|ban",
    "kbp": "aa | pa| se|se |na |nɛ | nɛ| yɔ| wa|yʊ | ɛy|ɛ p|ɖɛ |aɖɛ|a ɛ|a w|ɛwɛ|ɛna|yɛ |ala|ɛ ɛ|ɛ s|ɔɔ |yɔɔ|ɩ ɛ| ɛ |paa|e ɛ|e p|ɛyʊ|aɣ | pɩ| ɛw|a p|waɖ|ʊʊ |a n| ta|yɔ |yaa|yɩ |wɛn|la |taa|ʊ w| tɔ|a a|ɔ p|ɛya| kɩ| ɩ |ɩyɛ|a t|ʊ ɛ|a k|wɛɛ|tɔm|ɔm |ɛ t|wal|ʊ n| wɛ| ŋg| tɩ|ɛ n|ɛ k|kpe|ɛ ɖ|maɣ|zɩ | an|ʊ t|ɛ y| pʊ|nɩ | tʊ|ɛyɩ|ɩɣ |ɩ t| we|ɩ y|anɩ| pɔ|a s|gbɛ| pɛ| ɛs|pa |kpa|ɛɛ |wɛ | nɔ|daa|nɔɔ|ʊ y|ama|ya | kʊ|tʊ |pal|mɩy|ayɩ|ɩ p|ɩna|tɩ | ɖɩ|ʊ p|ɔ ɛ| ɛl| mb|ɔ s|ŋgb|a y|ɩma|ɖɩ |ʊ k|ɔɖɔ|ɩ n|bʊ |mbʊ| ɛk| kp|ɛja| ɛj|tʊm|jaɖ|paɣ|kɛ | ye|ɛyɛ|alɩ| na|i ɛ| ke| ya| ɖɔ|ɩ ɖ|ɔɔy|nda|ɖɔ |fɛy|ɣ ɛ|ɩ s|jɛy|yi |ɖɔɖ|ɛla|lɩ |kɩm|kɩ |aŋ |bɛy|pee| ñɩ|lab|ɩzɩ|pe |eyi|ŋ p|ɩ ɩ|ɛzɩ| fa|ɔyʊ|aʊ |ʊmɩ|ʊyʊ|ʊma|a l|sɔɔ|a ɩ|ekp|ʊ s| aj|ajɛ| ɛt|iya|wey|ɩ k|ʊ ŋ|ma |kan|ɩsɩ|laa|ɔyɔ|ɩm |li | kɛ| lɛ|and|sam| sa|ɣtʊ|ɔ k|day|ɔɔl|ɣ p|sɩ |ɔŋ |ɩfɛ|akp|pak|sɩn|pɩf|naa|ndʊ|kul| ha|aɣt|ɔ y|uli| ɖe| kɔ|eek| pe| sɔ|m n|ŋga|ee |ga |ɖʊ |maʊ|m t|e e|ɣna|ɣ s|ŋgʊ|abɩ|akɩ|a ñ|yaɣ|pɩz|eki| ɖo|maŋ| la|yee|ana|tɩŋ|ɣ t|pad|ñɩm| ca|ɛ a|a ɖ|pɩs|ina|dʊʊ|ɖe | ɖa|a m|lɛ |ked| ɛɖ|lak|aka|gʊ |asɩ|ʊ ɖ| ɛd|dʊ |nʊm| nʊ|ñɩn|ba |ɛpɩ|pʊ |ada|ɛhɛ|hal| a |le |zɩɣ|ɛɛn|ɛsɩ| le|aɣz|uu |nɖɩ|e t|ŋ n|ɛda|lɩm|e w|ɔ w|ɩ a| ɛp| nɖ|ɛkɛ|i p|ɣzɩ|alʊ|zaɣ|bɩ |ɛ l|ɩkɛ|ɔ t|e y|ɖam|aaa|pɛw",
    "tem": "yi | yi| ka|a ʌ| tə|uni|ni |wun| ɔ | aŋ| wu|ka | kə| kʌ| ʌŋ|nɛ |kə |tək| ʌm|əkə|ɔŋ |mar| ɔw|a k|ma |i k| a |wa | mʌ|i t|ri |ɔwa|thɔ| th| ma|ari|i m|a a|ʌma|aŋ | o | ba|tha|ba | kɔ|a y|ŋ k|ɔm |‐e | rʌ|lɔm|kɔ |i ɔ|kom|o w|ʌnɛ|te |mʌ | ŋa|i o|əm |hɔf|ɔf |alɔ|om |a m|ɔ b|ɔ y|aŋf|fəm|hal|kəp| mə|ŋfə|ʌth| tʌ|a t|a r|ŋ y|ŋth|ŋa | ʌt|ɔ k|e ɔ|ɛ t| ro|wan|ema| gb|ank| ye|th |yem|nko| mɔ|ʌwa| sɔ|kʌm|m a|kət|ʌmʌ|anɛ|rʌw|ɔ t|ʌme|ʌŋt|me |ʌte| bɛ|hɔ |a ɔ|ki |ʌŋ |m ʌ|m k|ar |ŋ ɔ|yɛ |əth|ɛ ʌ| ta|i a|ta | ʌk|ə k|thi|et |pet|pa |ŋɔŋ| te|ŋe |i ʌ|ra |i r|əpe| ŋɔ|ɛ k|ʌ k| yɔ| rə|kʌt|rʌ | yɛ|bɛ |e a|e t|ro |ɔ ʌ|akə|thə|ɔ m|a‐e|əpa|a w|kəl|ə b|yɔ |ə t|mɔ |bot|ŋ t|e y|əŋ |mʌs|gba|e m|m r| bo|ʌŋe| ak|ɛ a|nʌn|ləŋ|ələ|sɔŋ|ŋ b|təm|wop|ʌ a|ə y|kəs|sek|ə s|tʌt|li |ot | ko|ɛ ŋ|ŋ a|ekr| ra|ɔth|sɔt|ʌse|ath|ru |t k|ɛ m|e k|ɛth|ma‐|po | po| wo|ʌrʌ|i y|m t|m ŋ|tʌŋ|tɔŋ|e w|gbʌ|tə |nth|ʌyi|ʌlə|hən|ʌ ʌ|op |iki|ʌkə|rʌr|ʌru|ŋgb|sɔ |əyi|rʌn|gbə|ɔ a|ər |ɔkɔ| pə| ʌr|ənʌ|ləs|nka|ith|əli|ʌy |bəl|mʌy|ran|o ɔ|ɛ r|ant|f ʌ|mə |ti |f t| tɔ|əs |r k|hi |yik|ɔ ɔ|rək|kar|ʌ t|mʌt|lɔk|ayi|krʌ|pan|na |kʌr|mət|tət|tho|pi |mʌl| to|to | wa|ʌgb|thɛ|ə g|bas|eŋ |aŋk|ɔ r|thʌ|o t|ɛŋ |i‐e|kʌ |kʌs|mɔŋ|o d|kɔŋ|din|ɔ g|kəw|di |ŋ w|əma|ɛr |ʌ y|ək |ŋko",
    "toi": " ku|a k|wa | mu|a m|la |ali|ya |tu |i a|e k|a a|aku|ula|ntu|ang| al|lim|lwa|kwa|aan|mun|mwi|de |ulu|ngu|wi |imw|luk|gul|na |ele| ak|kub|ons|unt|kul|oon|se |ant|nse| oo|zyi|gwa|si | ba|ba | lw|zya|uli|ela|a b| ci| ka| zy|waa|and| an| kw|ili|uki|eel|uba|nyi|ala|kut|ide| ma|kid|isi|uny|i m|kun|cis| ya|li |i k|nga|a l|yin|kuk|ka | ul|kus|ina|laa|nte|ila|tel|mul|wab|wee|nda|izy|ede| am|led|amb|ban|we |da |ana|kwe|e a|lil| bu|o k|bwa|aka|ukw|o a|ati|uko|awo|yan|ko |uci|ilw|bil|bo |a c|wo |amu|law|mbu|i b|bul|umi|ale|abi|kak|e m|u b|akw|u o|ti |sal|kuy|ung|bel|wak| bw|o l|ga |kal|asy|e u|lan| mb|lo |usa|ika|asi|aam|a n|ule|bi |cit|bun|kup|egw|muk|igw|u k|u a|mbi|wii|kum|a z|aci|ku |yi | mi|yo |le |mas|yig|ubu|kka|i c| ab|ene|ne |no |a y| wa|abo|ndi|uta|syo|aya|aba|len|kuc|eya|o y|mal|ind|lem| lu|ukk|mo |eka|mil|mbo|ita|uka|ama|lik|u z|ndu|mu |nzy|zum|bal|abu|upe|bam|syi|u m|liz|int|ta |yak|ley|e b|nzi|lii|kab|uti|ube|uum|i n|cik|ezy|iib|iba|ani|iko|iin|ile|was| ca|zye|alw| aa|sya|uku|twa|min|tal|muc|umu| nk|du |azy|onz|lek|kon|buk|o m|yik|i z|lwe|u u|oba|kwi|imo|gan|zil|del|usu| we|peg|yee|ngw|sum|imb|ump|mpu|nde|end|i o|yoo|o n| nc|a u|mi |ano|uya|o c|di |mba|yil|yal|ako|a o|isy|izu|omb",
    "est": "sel|ja | ja|le |se |ust|ste|use|ise|õig|mis| va|gus|ele|te |igu|us |st |dus| õi| võ| on|on |e j| in|ini|nim|ma |el |a v|iga|ist|ime|al |või|da | te|lik| ig|adu|mes|ami|end|e k|e v|l o| ka|est| ra| se|õi |iku| ko|vab|aba|tus|ud |a k|ese| ku|l i|gal|tsi|lt |es |ema|ida|ks |a i|n õ|lis|atu|rah|tam|ast|sta|e t|s s| mi|ta |ole|stu|bad|ga |val|ine| ta|ne | pe|nda|ell|a t|ali|ava|ada|a p|ik |kus|e s|ioo|tes|ahe|ing|lus| ol|a a|is |vah|a s|ei | ei|kon|vas|tud|ahv|t k|as |a r|s t|e e|i v|eks|oon|t v|oni|kõi|s k|sio|sus|e a|gi |mat|min| pi|s v|oma|kul|dad| ni|e p| om|igi|tel|a j|e o|ndu|dse|lle|ees|tse|uta|vus|aal|aja|i t|dam|ats|ni |ete|pid|pea|e õ|its|lma|lev|nis|dis|ühi|sli|i s|nen|iel|des|de |t i|et |nin|eva|teg|usl|elt|ili|i m|ng | ee|tem|ses|ilm|sek|ab | põ|ait| ne|õrd|sed|võr|ul | üh| ki|abi| kõ|ega|rds| vä|ots| et| ri|põh|ed |töö|si |ad |i k| tä|ata| ab| su|eli| sa|s o|s j|sil|nni|ari|asu|nna| al|nud|uma|sik|hvu|onn|eab|emi|rid|ara|set|e m| ke|a e|täi|d k|s p|i e|imi|eis|e r|na | ül|a ü|koh|a o|aks|s e|e n| so|õik|saa|and|isi|nde|tum|hel|lii|kin|äär|sea|isk|een|ead|dum| kä|rii|rat|lem|umi|kor|sa |idu|mus|rit|har| si|vad|ita|ale|kai|teo| mõ|ade|üks|mas|lse|als|iaa|sia|sot|jal|iig|ite",
    "snk": "an | a | na|na |a n|ga | ga|en | su|re |a k| ka|su |a a|a s| ta|un | se|ta |ma | i |ama|do |e s|ere|ser|aan| do|nan|nta| ra|n s| ma| ki| ja|jam| da|taq|ne |a g|a d| ya|n d|ni | ku|ren|ri | si|ana|u k|n ŋ|ŋa | nt|e k|maa| ŋa|ndi|wa |aqu|ane| ba|ra |a r| sa|oro|n t|raa|tan| ke|oxo| xa|i s|di |a f|and|ti |a b| be|i k|gan|aax|aaw| go|iri|kit|awa|axu|sir|a i| du|a t|me |ara|ya |ini|xo |tta|i a|oll|ran|on |gol|e d|n g|a j|nde|aar|e m|be |a m|ari|u n|lli|ron| fa|qu | ti|n n|aad|axa| ña|o a| so|ke |nu | ko|din|lle|dan|a y|man|i g|sor|u r|i t| no|are|xar|kuu| wa|enm|ada|baa|de |qun|o k|yi |xun|i n|i x| an| ha|kan|fo |att|ang|n k|o s|dam|haa|da |n y|kat|e t|li | fo|i d| mo|nme|u b|i m|aba| fe|len| re|pa |ant|ayi|yan|e n|a x|e y|n b| di|ppa|app|kap|xa |u t|o g|mox|ure| xo|ond|i i|a ñ|n x|taa|du |ell| me|iti|xu |u d|udo|ind|uud|anu|nga|o b|nun|nox|n f|ku |aga|anŋ|dun|itt|eye|ye | bo|ore|ite|u a|oor| yi| ro|sar|saa|ill|e b| wu|le |riy|nma|ro |ken|edd|fed|bur| mu|mun|o n|iin|tey|sel| tu|u m|lla|la |ono|ñaa|den|faa|a w|te |inm|ka |aay| te|ina|xoo|o d|ira|u s|o t|nmu|nen|ban|ene| ni|ña |o i|uur|una|o m|xon|n w|kaf|gu |e g|a h|kil|yu |und|aqi|een| bi|bag|i j|n ñ|laa|i r|no |sig|igi|kor| o |i b|bat",
    "cjk": " ku|a k|yi |nyi| ny|la | mu|wa | ci|a c|a n| ha|we |a m|nga|ga |i k|kul|uli|sa |esw|ana|ela|a h|ung|ha |tel|swe|ze |ya |a u| ka| wa|uci| ya|ate|ci |mwe|kwa|ma |mbu|ji |kut|han|u m| ul|ang| mw|nat|ca | ca|e m|mu |uth|ali|i n|mut|thu|i m|e k|lit|hu |ina|ka |kup|na | ma|asa|aku|e n|a i|pwa|nji|wes|li | mb|e a|ifu|fuc|kan|bun|ize|ing|a y|anj|mba|uta|ita|i u| kw|muk|ite|kus|amb|lin|awa|imb|cip|lim|ong|esa|i c|nge| ak|ngu| ce| an|ili|ulu| na|naw|kuh|ama|upw|emu|lem|ila| un|a a|ula|ukw|aka|cif|ule|wo |has|kun|kha| xi|o n|tam| es|usa|ala|te |u c| ng|iku|cik|lya|wil|e c|ta |xim|wik| li|muc| ly|ikh|no |o m| in|i a|utu|e w|akw|mo |imo|mil| mi|i y|ba |ko |ngi|ufu|ku |lij|uka|iji|a w|umi|o w|tan|o y|e y|imw|ulw|uha|nal|so |o k| ye|i l|e u|umw|bu |aci|lwi|aha|ciz|mwi|kat|lon|u k|yes|ipw|ulo|aze|uni|wak|lo |ema|o c|aco| iz|kum|ika|e i|cim|isa|eny|umu|pem|yum|kwo| ik|kwe|e h|ngw|wam|cin|i h|a e|wan|ge |a x|was|le |kuk|uze|lik|gul|nin|pwe|o u|mah|ata|uma| up|sak|zan| uf|fun|go |wen|mbi|uso|ges|co |ngo|iki|hal|gik|ile|nda|kol|kal|kuz|ne | ja|oze|yoz|ikw|ipe|ces|swa|cis|man|i i|iso|ele|aso|waz|mi |upu| if|ise|umb|uvu|kil| it|i w|sok|o l|oko|nyo|una|bi |tum|iko|ene|hak|sem|a l|da |vul|nyu| ut| uk|eka",
    "ada": "mi |nɛ | nɔ| nɛ| e | he|he |nɔ | a |ɔ n|kɛ | kɛ|i k| ng|a n|i n|aa |e n|blɔ| bl|ɛ n|ɛ e|gɛ |ngɛ|e b|lɔ | ma| mi|ɛ h| ts| ko|hi |ɛ a| ɔ |ko |e h|ɛɛ |tsu| ni|ɔ k|a m|a k|i h|ma | ny|emi|a h|ami| be|be |i a|ya | si|e m|e j| ka|si |ɛ m|ɔ f| kp|nya| je|ni |oo |loo|o n| hi| fɛ|fɛɛ|a t|laa|a b|je |e k| pe|pee| ye|mɛ |umi|ɔ m| ha|a a|ɔmi|omi|kpa| wo|ɔ e|i t|ɛ ɔ|e s|i b|ɔ h| lo|ɛ k|ke |ha |bɔ |maa|mla|i m|ɔ t|ɔ́ |e p|kaa|ahi| sa|lɔh|ɔhi|sum|ɔ a|nɔ́|o e| na| gb|ee |e ɔ| ji|e a|i s| ml|ɛ s|sa | hɛ|ɔɔ |yem|u n|alo| jɔ| ku| lɛ| bɔ| to|a s|ɛ b|i l|lɛ |sua|o k|uaa|a j| su|ɛmi| ad|ɛ y|imi|ade| fa| al|jɔm|des|esa|eɔ |ihi|ji |ne |ɛ t|a e|ɛ j|ake|e e|kak|ngɔ|o a|eem|i j|e y|wo | bu|him|e w|́ k|ɔ y|tom|suɔ|ia |ane|mah| ya|o b| ke|e g|wom|gba|ue |ba | bi| gu|uo |e t|san|uu |pa |hia| tu| hu|suo| we|tsɔ|ɔ s|e f|kuu|gɔ |o m|a p| ja|ɛ p|fa |ɔ b|ɛ g|hɛɛ| ab|a l|hu |ye |na |tue|i ɔ|isi| sɔ|sɔs|jam|gu |ti |ɛ w|sis|o h|uɔ |li |a w| ba|sɔɔ|abɔ| ju| hl|ɔsɔ|hla|ɔ l|a y|sɛ | ɔm|ɔmɛ|i w|ɛti|pɛt|kpɛ|to | yi|asa| kɔ|nyu|akp|pak|kpe|sɔɛ|ɔɛ |u ɔ|yɛm|o s|uɛ | nu|pe |se | sɛ|o j|a g|ɔ w| wa|sem| pu|su |e l| mɛ|u k|hɛ |nih|kas| fɔ|kon|onɛ|bim|lam|imɛ|nyɛ| fi|hiɔ|usu|i p|bi | ní|yo |eeɔ|uam|bum|níh|íhi|o l|ula|kul|guɛ|naa",
    "bin": "e o|ne | ne|be |an |en |vbe| o |wan|mwa|n n|e e|emw|evb|mwe|in |na |e n| na| em|omw|e a|n e|e i| vb|re | ke|gha|gbe|wen| gh|ie |wee| om|e u| kh|bo |hia| ir|ha |o k|nmw|tin|n o|vbo|he |eti|ia |kev| ev| we| et|win|ke |ee |o n| hi|a n|a r|o r|gie|ran| ya|ira|mwi|a m| mw|a g|ghe|ogh| a | re| uh|eke| og|n k| no|ro |ye |khe| ye|hek|rri|nog|een|unm|a k|ogi|egb|ya |ere|wun|hun|mwu| mi|mie|de | rr|a e| ar|a o|n y|e v|o g|un |ra | ot| gb|uhu| ok|n i|ien|a v|rhi|e k|n a|i n|a y| ru|khi|n m|hie| eg|oto|arr|ba |ovb|u a|e y|ru |ian|hi |kpa| ra|o m|nde|yan|e w|and|to |o e|o h| ni| rh|e r|n g| er|n h|ugb|we |hae|on | iy|dom|rue|u e| or| ik|ren|a i|aro|iko|o y|n w|ben|ene|rio|se |i k|uem|ehe| ov|otu|okp|kug|oba|iob| uw|aen| do|iru|ae |tu |ue | iw| ma|wu |rro|o o|rie|n v| ug|a u|nna| al|ugh|agb|pa | ay|o w|ze |uwu|ma | eb|iye|aya|ugi|inn|gho|rre|nii|aku|gba|khu| se|yi |onm|ho |a w|ii |iwi| uy|uyi|e d| i |hin|obo|u o| ak|beh|ebe|uhi|bie|ai |da |i r|gbo|o v|won|mwo|umw| ag|ode| ek| la| um|aan| eh|egh|yin|anm|mo | kp| bi|kom|irr|i e|a a|kha|oda|bon|a d| ow|owa|ghi|n u|o a|yen|eem|ieg| az|aze|hoe| yi|oe |e g|ele|le |lug| ka|aa | as|yaa|gue|a h|mu |nre| od|n r|ero|ese| ku|enr|lel|vbi|wa |u i|a b|oro|bi ",
    "gaa": "mɔ | ni|ni |kɛ |ɛ a| ak|lɛ |i a| he|ɛ m|akɛ| lɛ| ko|gbɛ|ɔ n|ɛɛ | mɔ| kɛ|yɛ |li |ɛ e|ko |ɔ k|i e|aa | yɛ|bɛ | ml|shi|ɛ h|egb| gb|ɔɔ |mli| fɛ|fɛɛ|heg|nɔ |a a|i n|aŋ |oo | nɔ|i k|he |ɛ n| es| am|ɛ k|ɔ y| sh| ma|esa|loo|ji |maŋ|amɛ|emɔ|ɔ f|fee| ek| al|ɛi |ii |ɔ m|ɔ a|bɔ |e n|ɔ l|amɔ| eh|alo|hi |naa|ee |ɔmɔ|oni| en|o n|kon|aji|i y|i m|sa |o a|eli|umɔ| bɔ| hu|yel|hu |eem|nɛɛ|tsu| ah| nɛ|sum|tsɔ| an|nii|o e|baa| as|mɛi|yɔɔ|gbɔ|aaa|na |i h|eye|ɛ g|eɔ |ɛji| at|ana|eko|ena|o h|ŋ n|kom| ts|ɔ e|maj|i s|i l|efe|ome| kp|a l|kwɛ|ku |ehe|toi|a n|saa|bɔm|ha |a m|kɛj|kpa|hew| ku| sa| na|hiɛ| hi|ane|gba|e e|i f| mɛ|ɛ t|bɛi|ash|ŋ k|e k| ej|hey|aka|ats|ne |its|e a|san| ay|ye | je| kr| ey|mla|eŋm|nit|a h|ɔ b|ɛ s|anɔ|ŋmɔ|a e|ɛ b|jeŋ|ɛ y|aan|kro| ab| af|any|iaŋ|ɔ g|a k| yɔ|uɔ |shw|ets|ekɛ|usu|ŋŋ |ŋma|esh|u l| ba| et|iɔ |i j|o k|suɔ|oko| yi|e s| ag|afe|agb|oi |ŋ a|rok|o s| aw|ai | ji|ɛ j|aye|ŋ h|ish|nyɛ|la | ad|o m| ef|tsɛ|sɛ |wɔ |ewɔ|mɔɔ|ehi|aŋm|hwe| bɛ| to|ɔ h|jɛ |aha| ja|paŋ|alɛ|awo|sɔ |ŋts|ɛŋt|iɛŋ|bii|diɛ| di|mɛb|eni|his| ny|e b|hik|u k|ate|i b|ŋmɛ|akw|o y|eŋ |ahe| lo|me |ade|ɔ j|kɛn|teŋ|yeɔ|ɔ s|des| su|wal|nyɔ| eb| eg|ŋ m|mef|saŋ|ɛ l|o l|u n|asa|sem|jia|wɛ | em|o b|gbe|hil|ihi|hih|ɔŋ |nak|e h|sus|e g",
    "kng": " ya|na |ya |a k| na|a y|a m| ku|a n|a b| ba|u y|and|ka | mu|yin|wan|tu | lu|aka| mp|ve | yi|la |ntu| ki|mpe|pe |nda|a l|si |yan|ana|so | ke|e n|ons|nso|di |da |ndi|i y|u n|lu |mun|alu|unt|ina|e y|nza|luv|ala|uve| ma|u m|ke |za |ayi|sal|o m|ban|ndu|ta |isa|kan|ulu|i m|amb|ma |kim|u k|fwa| ny|nyo|yon|ama|ti |ang|anz|du |kus|o y| me|i n|to |ins|nsi|wa |usa| mo|kon|uta|end|i k|uka| bi|a d| ko|mbu|mos|sa | ve|ika|mu |osi|e k|uti|kuz|imp|a v|e m|und|ind| fw|ila| to|pwa|mpw|ngu|bal|adi|ba | sa|len|sam|sik|mab|tin|vwa|mba|kuk| di|yay|a t|yi | le|ant| ka|ata|isi|olo|kis|mut|ula|lo |bu |su | bu| at|amu|o n|dya|kut|dil| nz|ngi|abu|usu|but| nt|ni |bak|kul|e b|nga|e l|inz|imv|gu |wu | dy|lus|awu| ti|lak|bay|bun|kat|ngo|tal|i b|utu|kak|o k|bim|uzi|uza|mvu| ng|nak|iku|baw|esa|kin|ken|yak|mpa|luz|umu|nu |nta|dis|dik|vuk|u f|tan|sad|ati|nka|ank|luk|mak|ong| mb|ani|i l|lwa|aba|luy|uya|yal|ing|zwa|kuv|idi|ku |ga |zit|bis|uvw|uzw| ni|swa| nk|iti|mef|fun|ibu|nsa|aku|ufu|kub|lam|met|i a|mus|eta|a a|u t|twa|atu|tuk|fum|uko|iki|don|kol|kun|bam|eng|uku|ndo| ns|a s|ela|usi|pam|mvw|u b|i t|zo |anu|tis|uke|sul|te |gid|dib|yam|ilw| mf|ola|umb|uso|kam|gi |mbi|oko|nzi|i s| nd|mfu|luf|dus|bum|lut|mam|ded|wil|tad",
    "ndo": "na |oku|wa | na|a o|a n|ka |ntu| uu|tu |uth| om|e o|mba|ong|omu|ba | ok|uut| ne|he |the|ang|hem|emb|unt|o o|a u| wo|nge| iy|ehe|kal| no|a w|o n|no |nga|e n|ko |mun|oka|lo |o i|lon|we |ulu|a m|ala| ke|la |a k|u n|han|ku |gwa|osh|shi|ana|ngu|ilo|ano|ngo|keh| mo|ga |nen|man|ho |luk|tha|ge |gul|u k|eng|ha |a y|elo|uko|a e|ye |hil|uka|li |go |wan|ath|wo |thi|dhi|uun| pa|kwa| ta|a p|ya | sh| ko|nka|lwa| os|mwe|oma|ta |ema|sho| ka|e m| yo|sha|wok|ika|po |o w|onk|e p|pan|ith|a i|opa|gel|hik|iya|hi |aan|una|o g|kuk|alo|o e|nok|ndj|le |a a|men|yom|a s|i n| li|and| po|pam|lat|kan|ash|waa|aka|ame|gam|umb|a t|ond|yuu|o k|olo|ane|ing|igw|aa |ele|kul|mon| gw|ilw|gan|o y|iil|iyo| el|kut|nin|oko|ike|o m| ku|adh| ye|amw|ome|yeh|aye| ga| on| yi|a g|lyo|ne | ng|mbo|opo|kug|eko|yok|wom| oy|non|iye| go|ulo|e e| we| e |ina|ant|omo|ene| a |i k|mok|him| dh|und|ndu| me|eho|wen|nek| op|alu|e g|ima|kat|ota|oye|ila|ngw|yop|wat|ela|o u|a l| ii| ay| nd| th|o l|yon|ili|oon|okw|yaa|taa|lwe|omb| ni|aku|i m|mo |ula|ekw|enw|iyu|pok|epa|uki|ke | wu| mb|meh|e t|uni|nom|dho|pau|eta|yi | ly|o a|ono|lun|lak|ola|yo |lol|ank|bo |i o|awa|nwa|a h|naw|hok|nem|kom|ndo|o s|u t|vet|mbu|ani|uga|ndi|ukw|udh|lok|e k|alw|kwe|kun| ya",
    "quy": "chi|nch|hik|una| ka|anc|kun|man|ana|aq |cha|aku|pas|as |sqa|paq|nan|qa |apa|kan|ikp|ik |ech|spa| de|pa |cho|ere|der|rec|am | ru|an | ma| ch|kpa|asq|ta |na |nam|nak|taq|a k|qan|ina|run|lli|ach|nap|pi |mi | ll|yoq|asp|ima|hay|hin|aqa|nku|ant|ayn|oyo| hi| im|hoy|cio|nta|nas|q k|api|iw |wan|kuy|kay|liw|aci|ion|ipa|lla|oq |npa|ay |kas|a m|nac| na|inc|all|ama|ari|anp| ya|chu| hu|nin|pip|i k|qmi|hon|w r|ata|awa|a c|ota|in |yku|yna| wa|a h|has|a d|iku|a l| li|pan|ich|may| pi| ha|onc|a r|onk| ot|ku | qa|ank|aqm|mun|anm|hu |a p|nma| mu|qta|n h|pap|isq|yni|ikm|ma |wsa|aws|kaw|ibr|bre|lib|ayk|usp|nqa|e k| al|lin|n k|re |ara|nat|yac|kma|war|huk|uwa|yta|hwa|chw| sa|was|kus|yan|m d|kpi|q m|a i|q l|kin|tap|a a|kta|ikt|i c|a s|uy | ca|qaw|uku| tu| re|aqt|ask|qsi|sak|uch|q h|cas|tin|pak|ris|ski|sic|q d|nmi|s l|naq|tuk|mpa|a y|k c|uma|ien|ypi| am|qaq|qap|eqs|ayp|req|qpa|aqp|law|ayt|q c|pun| ni|a q|ruw|i h|haw|n c| pa|amp|par|k h| le|yma|ñun|ern|huñ|nni|n r|anq|map|aya|tar|s m|uñu|ten|val|ura|ita|arm|isu|s c|onn|igu| ri|qku|naw|k l|u l|his|ley|say|s y|rim|aru|rma|sun|ier|s o|qar|n p|a f|a t|esq|n a|oqm|s i|awk| va|w n|hap|lap|kup|i r|kam|uyk|sap| qe|ual|m p|ran|nya|gua| pe| go|gob|maq|sum|ast| su| ig",
    "rmn": "aj |en | te|te | sa| le|aka|pen| si| e |el |ipe|si |kaj|sar| th|and| o |sav|qe |les| ma|es | ha|j t|hak|ja |ar |ave| an|a s|ta |i l|ia |nas| aj|ne | so|imn|mna|sqe|esq|nd |tha|haj|e s|e t|e a|enq|asq|man| ja|kan|e m| i | ta|the|mes|cia|bar|as |isa|utn|qo |hem|o s|s s| me|vel|ark|i t| na|kas|est| ba|s h|avo| di|ard| bi| pe|rka|lo | ak|ika|e r|a a| pr|e k|qi |mat|ima|e p|a t| av|e d|r s|n s|anu|nuś|o t|avi|orr|o a| ka| re|n a|re |aja|e o|sqo|sti| ov|õl |l p|nqe|ere|d o|vor|so |no |dik|rel|ove|n t|ve |e b|res|tim|ren| de|àci|o m|i a|but|len|ali|ari|rre|de | pa|ver| va|sqi|ara|ana|vip|rak|ang|vi | ra|or |ker|i s|eme|e z|ata|e l|a e|rip|rim|akh|la |o p|kar|e h|a p|na |ane|rin|ste|j b|er |ind|ni |tne| ph|nip|r t| ke|ti |are|ndo| je|l a|uśi|e n|khi| bu|kon|lim|al |tar|ekh|jek|àlo|o k| ko|rde|rab|aba| zi|ri |aća|ćar|śik|dõl|dor|on |ano|ven| ni|śaj| śa|khe|ća |ast|j s|uti|uni|tni|naś|i d|mut| po|i p|a m| pu|a l|l s|som|n n|ikh|nik|del|ala|ris|pes|pe |j m|enć|e e|nća|ndi|rdõ|kri|erd|śka|emu|men|alo|nis|aśt|śti|amu|kh |tis|uj |j p|do |ani|ate|nda|o b|nge|o z|soc|a d|muj|o j|da |pri|rdo| as|cie|l t|ro |i r|kla|ing|a j| ze|zen|j e|ziv|hin|aśk| st|maś|ran|pal|khl|mam|i b|oci|rea|l o|nqo| vi|n e",
    "lat": "is |et |us |um | et|ae |tat|ati| co|que|ue |ion| qu|em |ent|oni|est| su| iu| in| po|tio|tes|tis|ate|bus|e i|ita|ibu|ium|ius|qui|nti|eri|es |s p|con|s e|per|end|pot|ote| ha|nis| pr|s i|abe|uis|am |uae|tem|hab|bet|m h|ndi| ho|sta| de|sua|isq|squ|ter|ici|min|iur|one| re|hom| di| om|omn|rum|s a|t c|rat|lib|ibe|m e| pe|gen| li|ert|ine|nte|nem|ri |ber|tia|e q|dis| ip|ips| ad|di |nes|e s|e c|m p|s c| ve|e p| pa|ili| ge|a e|i p|nt |omi|atu|tur|rit| si|ne |psi|in |ia |ra |ari| cu|vit|rta|mo |to |mni|s h|e e|int|siu|m c|qua|t p|ivi|ini|ut |re |ers|it |s s|iae| es|t s|and| ne|pro| nu|st | ex|nda|cie|nib|t a|ere|tri|nit| at|tiu|ta |ris| ci|civ|ni |uri|ur |rim| vi|par|ad |ess|lic|i i| so| pu| op|rae| fa|s v| ut|dem|se |ons|o e|ria| se|e a| mo|leg|atq|tqu|com|te |niu|ien|vel|el | ma|t e|iis|gni|equ|oci|cip|ura|unt|s d|t i|ali|quo|ect| te|a s|t d| do|tut|ant|isc|ina|men|sin|ua |pra|oru|omm|eta|s n|a p|tum|iam|io |i c|sti| au|ver| ae|ito|dic|imi|s l|e d|fic|cia|t o|pub|ubl|bli|mun|i s|soc|aru|lar|ull|ori|t h|i e|sse|omo|cto|itu|tus| ea|ea |aeq|gio|ui |m s|er |m r| ra| fi|ffi|cog|da | le|mod|a c|mqu|nul|e o|era|ten|ntu|spe|o n|emo|cri|s f| ca|de |a d|rel|ii |ene| tu|sui|rti|sci|nae|m q|m a|egi|ces",
    "cym": "yn | yn|dd | ma|ae |mae|au | y |d y|edd| r |ydd| ar| i |n y| o | cy|th | gw|ddi|eth|oed|ol |ar | gy| dd|wyd| ei| n | a |yd |odd| ga|aet|an | rh|iad|io |n a|ei |yr |wn |n c| ll| ca|n g|di |wed| me|od |el |n d|edi|r y|ith| we|ad | fe|er |r a|dau| da| am|d a|on |ch |l y|ddo| he| ch|roe| hy|e r| di|ynn| yr|dda|r g|gan|ir |ewn| ro|en | dy|fod| ff|iau|ll |mew| ym| de|id | sy|yw |dia|hyn|fyd|i g| un|eu |i d|nol|lla|u a|eit| ac|dol|i r|wy |dio|cyn|fel| ni|o r|idd|rth| go|l a|ai |efy|dyn| bo|rha|ed | dr|rwy|ada|n f|wyr|fer|ac |n e|rdd|aid|ael|all|nt |ion| tr|nyd|ach|gyf|cyf|r d|ig |h y|chw|ell|n b|d e|n o| by| ne|da | be|han|nia| oe|d o|r c|d g|dde|r o|af |ara|ni |n s| pe|lwy|gwe|i a|wr | br|in |gol| ge|rch|hef| ad|nod|nna|gyd| fa|un |d h| ys|d i|y d|e n|ria|es | an|dwy|am |ysg|y g|wyn|u c|l e|i f|gwy|efn|ddy|y c|dig|wys| eu|yda|n h|ych|thi|ant| yw|wei| ba|d c|n n|s y|yst|ryd|na |o a|i n|n m|u g|d d|law|i w|n i|n r| fo|ys |iae| co|do |lia|red|nd |y n|hau| ha|neu|u y|rhy|u r|bod| pr| ce|rae|gor|enn|gwa| pa|i c| er|lyn|rai|rif|ian|lli|nau|r h|lan|nwy|yfe|tha|r e|d m|diw|os |lle|ang| se|ddw|al |lad|o g|cae|ann|oli|a r|r b|rio|hyd|ait|aen|u d|no |d b| si|fan|lly|u h|o d|i b|dar|sgo|yng|dod|u n"
  },
  "Cyrillic": {
    "rus": " пр| и |рав|ств| на|пра|го |ени|ове|во | ка|ани|ть | в | по| об|ия |сво| св|лов|на | че|ело|о н| со|ост|чел|ие |ого|ет |ния|ест|аво|ый |ажд| им|ние|век| не|льн|ли |ова|име|ать|при|т п|и п|каж|или|обо| ра|ых |жды| до|дый|воб|ек |бод|ва |й ч|его|ся |и с|ии |аци|еет|но |мее|и и|лен|ой |тва|ных|то | ил|к и|енн| бы|ию | за|ми |тво|и н|о п|ван|о с|сто|аль| вс|ом |о в|ьно|их |ног|и в|нов|ако|про|ий |сти|и о|пол|олж|дол|ое |бра|я в| ос|ным|жен|раз|ти |нос|я и| во|тор|все| ег|ей |тел|не |и р|ред|ель|тве|оди| ко|общ|о и| де|има|а и|чес|ним|сно|как| ли|щес|вле|ься|нны|аст|тьс|нно|осу|е д| от|пре|шен|а с|бще|осн|одн|быт|сов|ыть|лжн|ран|нию|иче|ак |ым |ват|что|сту|чен|е в| ст|рес|оль| ни|ном|род|ля |нар|вен|ду |оже|ны |е и| то|вер|а о|зов|м и|нац|ден|рин|туп|ежд|стр| чт|я п|она|дос|х и|й и|тоя|есп|лич|бес|обр|ото|о б|ьны|ь в|нии|е м|ую | мо|ем | ме|аро| ре|ава|кот|ав | вы|ам |жно|ста|ая |под|и к|ное| к | та| го|гос|суд|еоб|я н|ен |и д|мож|еск|ели|авн|ве |ече|уще|печ|дно|о д|ход|ка | дл|для|ово|ате|льс|ю и|в к|нен|ции|ной|уда|вов| бе|оро|нст|ами|циа|кон|сем|е о|вно| эт|азо|х п|ни |жде|м п|ког|от |дст|вны|сть|ые |о о|пос|сре|тра|ейс|так|и б|дов|му |я к|нал|дру| др|кой|тер|ь п|арс|изн|соц|еди|олн",
    "ukr": "на | пр| і |пра|рав| на|ня |ння| за|ого| по|ти |го |люд| лю|во | ко| ма|льн|юди|их |о н| не|аво|анн|дин| св|сво|ожн|кож|енн|пов|жна| до|ати|ина|ає |а л| бу|аці|не |ува|обо| ос| як|має| ви|них|аль|або|є п| та|ні |ть |ови|бо | ві| аб|ере|і п|а м|вин|без|при|іль|ног|о п|ми |та |ом |ою |бод|ста|воб| бе|до |ва |ті | об|о в|ост| в | що|ий |ся |і с| сп|инн|від|ств|и п|ван|нов|нан|кон| у |ват|она|ії |но |дно|ій |езп|пер| де|ути|ьно|ист|під|сті|бут| мо|и і|ідн|ако|нні|ід |тис|що |род|і в|а з|ава| пе|му |і н|а п|соб|ої |а в|спр|ів |ний|яко|ду |вно|і д|ну |аро|и с| ін|ля |рів|у в| рі|и д|нар|нен|ова|ому|лен|нац|ним|ися|чи |ав |і р|ном| ро|нос|ві |вни|овн| її|ові|мож|віл|у п| пі| су|її |одн| вс|ово|ють|іст|сть|і з| ст|буд| ра|чен|про|роз|івн|оду|а о|ьни|ни |о с|сно|зна|рац|им |о д|ими|я і|ції|х п|дер|чин| со|а с|ерж|и з|и в|е п|ди |заб|осо|у с|е б|сі |тер|ніх|я н|і б|кла|спі|в і| ні|о з|ржа|сту|їх |а н|нна|так|я п|зпе| од|абе|для|ту |і м|печ| дл|же |ки |віт|ніс|гал|ага|е м|ами|зах|рим|ї о|тан|ког|рес|удь| ре|то |ков|тор|ара|сві|тва|а б|оже|соц|оці|ціа|осн|роб|дь‐|ь‐я|‐як|і і|заг|ахи|хис|піл|цій|х в|лив|осв|іал|руч|ь п|інш|в я|ги |аги| ді|ком|ини|а і|оди|нал|тво|кої|всі|я в|ною|об |о у|о о|і о",
    "bos": " пр| и |рав| на|пра|на |да |ма |има| св|а с|а п| да|а и| по|је |во |ко |ва | у |ако|но |о и|е с| за| им|аво|ти |ава|сва|и п|ли |о н|или|и с|их |вак| ко|ост|а у| сл|не |вањ| др|ње | не|кој|ња | би|ије|и д|им |ств|у с|јед|бод|сло|лоб|обо| ил|при| је|ање| ра|а д| об| су|е и|вје|се |ом |и и|сти| се|ју |дру|а б| ос|циј|вој|е п|а н|раз|су |у п|ања|о д|ује|а о|у и| од|и у|ло |ова|дје|жав|оје|а к|ни |ово|едн|ити|аци|у о|о п|нос|и о|бра| ка|шти|а ј|них|е о|пре|про|ржа| бу|буд|тре| тр|ог |држ|бит|е д|у з|ја |ста|авн|ија|е б|миј|и н|реб|сво|ђи |а з|ве |бил|ред|род|аро|ило|ива|ту |пос| ње| из|е у|ају|ба |ка |ем |ени|де |јер|у д|одн|њег|ду |гов|вим|јел|тва|за | до|еђу|ним| са|нар|а т| ни|о к|оји|м и| см| ст|еба|ода|ран|у н|дна|ичн|уђи|ист|вно|алн|и м| дј|нак|нац|сно|нст|тив|ани|ено|е к|е н|аве|ан |чно|и б|ном|сту|нов|ови|чов|нап|ног|м с|ој |ну |а р|еди|овј|оја|сми|осн|анс|ара|дно|х п|под|сам|обр|о о|руг|тво|ји | мо|его|тит|ашт|заш| кр|тељ|ико|уна|ник|рад|оду|туп|жив| ми|јек|кри| ов| вј| чо|ву |г п| оп|међ|њу |рив|нич|ина|одр|е т|уду| те|мје|ење|сви|а ч|у у|ниц|дни| та|и т|тно|ите|и в|дст|акв|те |ао | вр|ра |вољ|рим|ак |иту|ави|кла|вни|амо| он|ада|ере|ена|сто|кон|ст |она|иво|оби|оба|едс|как|љу ",
    "srp": " пр| и |рав|пра| на|на | по|ма | св|да |има|а п|а и|во |ко |ва |ти |и п| у |ако| да|а с|аво|и с|ост| за|о и|сва| им|вак|ава|је |е с| сл| ко|о н|ња |но |не | не|ом |ли | др|или|у с|сло|обо|кој|их |лоб|бод|им |а н|ју | ил|ств| би|сти|а о|при|а у| ра|јед|ог | је|е п|ње |ни |у п|а д|едн|ити|а к|нос|и у|о д|про| су|ање|ова|е и|вањ|и и|циј| ос|се |дру|ста|ају|ања|и о| об|род|ове| ка| де|е о|аци|ја |ово| ни| од|и д| се|ве |ује|ени|ија|авн|жав| ст|у и|м и|дна|су |ред|и н|оја|е б|ара|што|нов|ржа|вој|држ|тва|оди|у о|а б|одн|пош|ошт|ним|а ј|ка |ран|у у| ов|аро|е д|сно|ења|у з|раз| из|осн|а з|о п|аве|пре|де |бит|них|шти|ву |у д|ду |ту | тр|нар| са|гов|за |без|оји|у н|вно|ичн|еђу|ло |ан |чно|ји |нак|ода| ме|вим|то |сво|ани|нац| ње|ник|њег|тит|ој |ме |ном|м с|е у|о к|ку | до|ика|ико|е к|пос|ашт|тре|алн|ног| вр|реб|нст| кр|сту|дно|ем |вар|е н|рив|туп|жив|те |чов|ст |ови|дни|ао |сме|бра|ави| ли|као|вољ|ило|о с|штв|и м|заш|њу |руг|тав|анс|ено|пор|кри|и б|оду|а р|ла | чо|а т|руш|ушт| бу|буд|ављ|уги|м п|ком|оје|вер| ве|под|и в|међ|его|вре|акв|еди|тво| см|од |дел|ена|рад|ба | мо|ну |о ј|дст|кла| оп|как|сам|ере|рим|вич|ива|о о| он|вни|тер|збе|х п|ниц|еба|е р|у в|ист|век|рем|сви|бил|ште|езб|јућ|њен|гла",
    "uzn": "лар|ан |га |ар | ва| би|да |ва |ир | ҳу|ига|уқу|бир|ҳуқ|қуқ|ган| ҳа|ини|нг |р б|иш | та|ни |инг|лик|а э|ида|или|лиш|нин|ари|иши| ин|ади|он |инс|нсо|сон|ий |лан|дир| ма|кин|и б|ши |ҳар| бў|бўл| му|дан|уқи|ила|қла|р и|қиг|эга| эг| ўз|ки |эрк|қил|а б|оли|кла| эр|гад|лга|нли| ол|рки|и ҳ| ёк|ёки| қа|иб |иги|лиг|н б|н м| қи| ба|ара|атл|ри | бо|лат|бил|ин |ҳам|а т|лаш|р ҳ|ала| эт|инл|ик |бош|ниш|ш ҳ|мас|и в|эти|тил|тла|а ҳ|и м|а қ|уқл|қар|ани|арн|рни|им |ат |оси|ўли|ги | да|а и|н ҳ|риш|и т|мла|ли | ха|а м|ият| бу|рла|а а|рча|бар|аси|ўз |арч|ати|лин|ча |либ|мум| ас|аро|а о|ун |таъ| бе| ту|икл|р в|тга|тиб| ке|н э|ш в|мда|амд|али|н қ|мат|шга| те|сид|лла|иро| шу| қо|дам|а ш|ирл|илл|хал|рга| де|ири|тиш|умк|ола|амл|мки|тен|гин|ур |а ў|рак|а ё|имо| эъ|алқ| са|енг|тар|рда|ода| ша|шқа|ўлг|кат|сий|ак |н о|зар|и қ|ор | ми|нда|н в| си|аза|ера|а к|тни|р т|мил| ки|к б|ана|ам |ошқ|рин|сос|ас | со|сиз|асо|нид|асл|н ў|н т|илг|бу |й т|ти |син|дав|шла|на |лим|қон|и а|лак|эма|муҳ|ъти|си |бор|аш |и э|ака|нга|а в|дек|уни|екл|ино|ами| жа|риг|а д| эм|вла|лма|кер| то|лли|авл| ка|ят |н и|аъл|чун|анл|учу| уч|и с|аёт| иш|а у|тда|мия|а с|ра |ўзи|оий|ай |диг|эът|сла|ага|ник|р д|ция| ни|и ў|ада|рор|лад|сит|кда|икд|ким",
    "aze": " вә|вә |әр |лар| һә|ин |ир | ол| һү| би|һүг|үгу|гуг|на |ләр|дә |һәр| шә|бир|ан | тә|лик|р б|мал|лма|асы|ини|р һ|шәх|ән |әхс|ары|гла|дир|а м|али|угу|аг | ма|ын |илә|уна|јәт| ја|икд|ара|ар |әри|әси|рин|әти|р ш|нин|дән|јјә|н һ| аз|ни |әрә| мә|зад|мәк|ијј| мү|син|тин|үн |олу|и в|ндә|гун|рын|аза|нда|ә а|әт |ыны|нын|лыг|илм| га| ет|ә ј|кди|әк |лә |лмә|олм|ына|инд|лун| ин|мас|хс |сын|ә б|г в|н м|адл|ја |тмә|н т|әми|нә |длы|да | бә|нун|бәр|сы | он|әја|ә һ|маг|дан|ун |етм|инә|н а|рлә|си | ва|ә в|раг|н б|ә м|ама|ры |н и|әра|нма|ынд|инс| өз|аны|ала| ал|ик |ә д|ләт|ирл|ил | ди|бил|ығы|ли |а б|әлә|дил|ә е|унм|алы|мүд| сә|ны |ә и|н в|ыг |нла|үда|аси|или| дә|нса|сан|угл|уг |әтл|ә о|хси| һе|ола|кил|ејн|тәр|јин| бу|ми |мәс|дыр|һәм| да|мин|иш | һа| ки|у в|лан|әни| ас|хал|бу |лығ|р в| ед|јан|рә |һеч|алг| та|еч |и с|ы һ|сиа|оси|сос|фиә|г һ|афи|ким|даф| әс|ә г| иш|н ә|ији|ыгл|әмә|ы о|әдә|әса| со|а г|лыд|илл|мил|а һ|ыды|сас|лы |ист| ис|ифа|мәз|ыр |јар|тлә|лиј|түн|ина|ә т|сиј|ал |рил| бү|иә |бүт| үч|үтү|өз |ону| ми|ија| нә|адә|ман|үчү|чүн|сеч|ылы|т в| се|иал|дах|сил|еди|н е|әји|ахи|хил| ҹә|миј|мән|р а|әз |а в|илд|и һ|тәһ|әһс|ы в|һси|вар|шәр|абә|гу |раб|аја|з һ|амә|там|ғын|ад |уғу|н д|мәһ|тәм| ни|и т| ха",
    "koi": "ны |ӧн | бы|да | пр|пра|рав| мо|лӧн| да|быд|лӧ |орт|мор|ӧм |аво|ӧй | ве|ыд | не|нӧй|ыс |ын |сӧ |тӧм|сь |во |эз |льн|ьнӧ|тны|д м| ас|ыны|м п| по|сьӧ| и |то |бы | ӧт| эм| кы|аль|тлӧ|н э| от|вер|эм | кӧ|ртл|ӧ в| ко|воэ|ств|ерм|тшӧ| до|ола|ылӧ|вол|ас |ӧдн|кыт|ісь|ето|нет|тво|ліс|кӧр|ӧс | се|ы с|шӧм|а с|та |злӧ| ме| ол|аци|ӧ к|ӧ д|мед| вы|вны|а в|на |з в| на|ӧ б|лас|ӧрт| во| вӧ| сі|лан|рмӧ|дбы|едб|ыдӧ|оз |ась| оз| сы|ытш|олӧ|оэз|тир|с о| чу|ы а|оти|ция|ись|ӧтл| эт|рты| го|ы п|ы б|кол|тыс|сет| сь|рті|кӧт|о с|н б|дз |н н| мы| ке|кер|тӧн|тӧг|ӧтн|ис |а д|мӧ |ост|ӧ м| со|онд|нац|дӧс|итӧ|ест|выл| ви|сис|эта| уд|суд|нӧ |удж|ӧг |пон|ы н|н п|мӧд|а п|орй|ӧны|ӧмӧ|н м|ть |сыл|ана|ті |нда|рны|сси|рре|укӧ|з к|чук|йын|рез| эз|ысл|ӧр |ьӧр|с с|с д|рт |с в|езл|кин|осу|эзл|й о|отс| тӧ|ы д| ло| об|овн|лӧт|асс|кӧд|с м|ӧ о|нал|быт|она|ӧт |слӧ|скӧ|кон|тӧд|ытӧ|дны|а м|ы м|нек|ы к|ӧ н|асл|дор|ӧ п| де| за|а о| ов|сть|тра| дз|ь к|ӧтч|н к| ст|аса|етӧ|ьны|мӧл|умӧ|сьн| ум|ерн|код| пы|тла|оль|иал|а к|н о| сэ|а н|ь м|кыд|циа|са | ли|а б|езӧ|й д| чт|ськ|эсӧ|ион|еск|ӧ с|оци|что|ан |соц|йӧ |мӧс|тко|зын|нӧя|вес|енн| мӧ|ӧтк|ӧсь|тӧ |рлӧ|ӧя |оля|рйӧ|ӧмы|гос|тсӧ|зак|рст|з д|дек|ннё|уда|пыр|еки|ако|озь| а |исӧ|поз|дар|арс|ы ч",
    "bel": " і | пр|пра|ава| на|на | па|рав|ны |ць |або| аб|ва |ацы|аве|ае | ча|ння|анн|льн| ма| св|сва|ала|не |чал|лав|ня |ай |ых | як|га |век|е п| ад|а н| не|пры|ага| ко|а п| за|кож|ожн|ы ч|бод|дна|жны|ваб|цца|ца | ў |а а|ек |мае|і п|нне|ных|асц|а с|пав|бо |ам |ста| са| вы|ван|ьна| да|ара|дзе|одн|го |наг|він|аць|оўн|цыя|мі |то | ра|і а|тва| ас|ств|лен|аві|ад |і с|енн|і н|аль|най|аво|рац|аро|ці |сці|пад|ама| бы| яг|яго|к м|іх |рым|ым |энн|што|і і|род| та|нан| дз|ні |я а|гэт|нас|ана| гэ|інн|а б|ыць|да |ыі |оў |чын| шт|а ў|цыі|які|дзя|а і|агу|я п|ным|нац| у | ўс|ыя |ьны|оль|нар|ўна|х п|і д|ў і| гр|амі|ымі|ах | ус|адз| ні|эта|ля |воў|ыма|рад|ы п|зна|чэн|нен|аба| ка|ўле|іна|быц|ход| ін|о п| ст|ера|уль|аў |асн|сам|рам|ры | су|нал|ду |ь с|чы |кла|аны|жна|і р|пер|і з|ь у|маю|ако|ыцц|яко|для|ую |гра|ука|е і|нае|адс|і ў|кац|ўны|а з| дл|яўл|а р|аюч|ючы|оду| пе| ро|ы і|вы |і м|аса|е м|аду|х н|ода|адн|нні|кі | шл|але|раз|ада|х і|авя|нав|алі|раб|ы ў|нна|мад|роў|кан|зе |дст|жыц|ані|нст|зяр|ржа|зак|дзі|люб|аюц|бар|ім |ены|бес|тан|м п|дук|е а|гул|я ў| дэ|ве |жав|ацц|ахо|заб|а в|авы|ган|о н|ваг|я і|чна|я я|сац|так|од |ярж|соб|м н|се |чац|ніч|ыял|яль|цця|ь п|о с|вол|дэк| бе|ну |ога| рэ|рас|буд|а т|асо|сно|ейн",
    "bul": " на|на | пр|то | и |рав|да |пра| да|а с|ств|ва |та |а п|ите|но |во |ени|а н|е н| за|о и|ото|ван|не | вс|те |ки | не|о н|ове| по|а и|ава|чов|ни |ане|ия | чо|аво|ие | св|е п|а д| об|век|ест|сво| им|има|ост|и д|и ч|ани|или|все|ли |тво|и с|ние|вот|а в|ват|ма | ра|и п|и н| в |ек |сек|еки|а о| ил|е и|при| се|ова|ето|ата|воб|обо|бод|аци|ат |пре|оди|к и| бъ| съ|раз| ос|ред| ка|а б|о д|се | ко|бъд|лно|ния|о п| от|ъде|о в|за |ята| е | тр|и и|о с|тел|и в|нит|е с|ран| де|от |общ|де |ка |бра|ен |ява|ция|про|алн|и о|ият|ст |нов| до|его|как|ато| из|нег|а т|ден|а к|щес|а р|тря|а ч|ряб|о о|вен|ябв|бва|дър|гов|нац|ено|тве|ърж|е д|нос|ржа|а з|вит|зи |акв|лен| та|ежд|и з|род|е о|обр|нот| ни| с |т с|нар|о т|она|ез |йст|кат|иче| бе|жав|е т|е в|тва|зак|аро|кой|осн| ли|ува|авн|ейс|сно|рес|пол|нен|вни|без|ри |стр| ст|сто|под|чки|вид|ган|си |ди |и к|нст| те|а е|вси|еоб| дъ|сич|ичк|едв|жен|ник|ода|т н|о р|ака|ели|одн|елн|лич| че|чес|бще| ре|и м| ср|сре|и р|са |лни| си|дви|ичн|жда| къ|оет|ира|я н|дей| ме|еди|дру|ход|еме|кри|че |дос|ста|гра| то|ой |тъп|въз|ико|и у|нет| со|ави|той|елс|меж|чит|ита|що |ъм |азо|зов|нич|нал|дно| мо|ине|а у|тно|таз|кон|лит|ан |клю|люч|пос|тви|а м|й н|т и|изв|рез|ази|ра |оят|нео|чре",
    "kaz": "ен |не | құ|тар|ұқы| ба| қа|ға |ада|дам|құқ|ық | бо| ад|ықт|қта|ына|ар | жә|ың |ылы|әне|жән| не|мен|лық|на |р а|де | жа|ін |а қ|ары|ан | әр|қыл|ара|ала| ме|н қ|еме|уға|ның| де|асы|ам |іне|тан|лы |нды|да |әр |ығы|ста|еке| өз|ын |ған|анд|мес| бі| қо|ды |ің |бас|бол|етт|ып |н б|ілі|қық|нде|ері|е қ|алы|нем|се |бір|лар|есе|ы б|тын|а ж| ке|тиі|ост|ге |бар| ти|е б| ар|дық|сы |інд|е а|аты| та| бе|ы т|ік |олы|нда|ғын|ры |иіс|ғы | те|бос|луы|алу|сын|рын|еті|іс |рде|қығ|е ж|рін|дар|іні|н ж|тті|қар|н к|ім | ер|егі|ыры|ыны| са|рға|ген|ынд|аны|уын|ы м|лға|ана|нің|тер|уы |ей |тік|ке |сқа|қа |мыс|тық|м б|ард| от|е н|е т|мны|өзі|нан|гіз|еге| на|ы ә|аза|ң қ|лан|нег|асқ|кін|амн|кет|рал|айд|луғ|аса|ті |рды|і б|а б|ру | же|р м|ді |тта|мет|лік|тыр|ама|жас|н н|лып| мү|дай|өз |ігі| ал|ауд|дей|зін|бер|р б|уда|кел|біл|і т|қор|тең|лге| жү|ден|ы а|елі|дер|ы ж|а т|рқы|рлы|арқ| тү|қам|еле|а о|е ө|тін|ір |ең |уге|е м|лде|ау |ауы|ркі|н а|ы е|оны|н т|рыл|түр|ция|гін| то| ха|жағ|оға|осы|зде| ос|ікт|кті|а д|ұлт|лтт|тты|лім|ғда| ау| да|хал|тте|лма| ұл|амд|құр|ірі|қат|тал|орғ|зі |елг|сіз|ағы| ел|ң б|ыс | ас|імд|оты| әл|н е|ағд|қты|шін|ерк|е д|ек |ені|кім|ылм|шіл|аға|сты|лер|гі |атт|кен| кө|ым‐| кұ|кұқ|ра |рік|н ә| еш",
    "tat": " һә|лар|әм |һәм| ке| хо|кук|оку|хок|еше| бе|ләр|кеш|га |әр |рга|ан |кла| бу|ар |ең |нең|гә | то| ба|да |ргә| ти|ырг|һәр|ене|бер|ән |ен |р к|бул|укл|дә |а т|ары|тор|ире| үз|на |ган|ара| ка| ал|ә т|нә | ит| дә|ы б| ир|рын|ше |ын |енә|тие|лык|екл|ына|н т|иеш|бар|еле|ка |елә|а х|н б|кы |рек|ала|кар| та|ә к|нда|еш |лән|бел|укы|лан|ите|тә |шен|ле |лы |ез |ерг|н и|ә б|а к|клә|үз |тел|лыр|не |әрг|ы һ|е б| га| ха|алы|рне|м и|тен|әрн|а б|ның|ынд|ың |ләт|дан|сә | як|лга|улы|ел |а а| яи|яис|асы|ш т|а һ| са|рлә|лек|иге|ә х|гез|орм|ем |аны|р б|м а|р һ|рмы|мыш|сын|шка|ә һ|исә|тәр|үлә|әт |мәт|сен|сез|чен| ни|ә и|н м|илл|ять|ны |ылы|үзе| ки| эш| ту|алу|акы|ып |уга|ль |тан|н к|лу |бу |мас|рен|кә | тү| тә|түг|зен| җә|тын|ди |баш|кле|гән|ть | би|әре|штә|гын|әүл|ер |мил| ми|клы|гел|ыш |лер|ерл|әве|рдә|а я|р а| мә| рә|лем|хал| ан|ң т| аш|ык |ция|е х|стә|ә д|аль|рак|ек | де|рәв|тот|кән|улг|орг|веш|ешт|ни |итә|кка|м т|үге|шел|а и|ндә| да|рел|кер| кы|ерә|та |н я|еге|ый |а д|аци|р о|шла|тлә|әтл|н д|айл|ллә|ард|рда|кта|шкә| за|ге |ләш|ш б|әсе|кон|шыр|циа|нин|лау|уры|ры |оты|әне| тө|инд|нди| җи|оци|соц|лә |арт|якл|зак|тиг|рке| ди| со|ыкл|кем| ко|р и|ң б|әте|гыя|чар|үгә|ин |иле| сә| ил|мгы| ае|н а|аер|ыны|л һ",
    "tuk": " би|лар| ве|ве |да |ада|ары| хе|ир | ад|бир|дам|кла|ер |р б|ың | ха|ара|га |ен |лан|ыны|или|дыр|ам |ала| бо|хер|р а|ыр |лы |лер|ан |бил|иң |ыды|р х|акл|нда| өз|клы|ны |хук|ери| ху|уку|ага|не |лыд|ине|ына|лен|на |хак|де |‐да|ин |рын|атл| эд|маг|өз | де|асы|лыг|кук|е а|ынд|алы|лма|бол|дан|ини|а х| я‐|е х|ге |иле|я‐д|ар |ама|ли |ыгы|ети| ба| га|гын|ере|укл|лиг|ның|зат|лык|тлы|нде|ни |лик|ден|мак|сын|дил|ры |аны|кин|әге|п б|а г|хем|иги|эрк|аза|а д|мек| эр|мал|ыкл|мәг|сас| эс|екл| ма|рин|эса|ола|ы б|айы|н э|эди| гө| хи|сы | аз|баш|ы д|йда|шга|ашг|а в| до|ыет|ы в|дак|ниң|рки|гал|чин|гда|ак | җе|а б| эт|этм|кы |лет|йән| та|гин|ян |тме|хич|ич |мез| гу|хал|ылы|үнд|илм|дай|ягд| яг|и в|им |акы|ы г|ән |а а|рың|ги |тле|н м| го|ип |ал |еси| се|лме| ка|м х|дең|ң х|е д|дир|илл|рил| ал|кан|е г|лин|ра |дол| бе| ми|мил|ң д|н х|ели|н а|е м| ге|ы х| дө|ик | со|ң а|чил|дөв|е б| са|гар|е в|ең |н б|рма| ме|кли|үчи| дә| үч|ция|н в| дү|и б|айд|кле|сер|а я|соц|гор|оци|дал|мы |олм|циа|уң | он|уп |кда|дәл|ири| ди|еле|лип|алк|лим|гур|үни|нме| әх|н г| иш|ы ө|ң э|нун|еги|тин|ы а|рле|аци|ыз |з х|сыз|аха|м э|олы|рам| ту| ни|ып |ерт|алм|ора|и х|хли|әхл|к э|өвл|вле|тмә|ет |нли|ахс|гөз|гы |етл|ы ү|нуң|ону|сиз|емм|ек ",
    "tgk": "ар | ба| ҳа| да|ад | ва|он |ва | та|дар|ти | ин|ба | бо| ки|аро| до|ои |дор|ард|ки |бар|д ҳ|уқу| як|ин |ҳар|и о| на| ма|и м|ора| ҳу|як |ни |нсо|инс|и ҳ|аи |и б|сон|рад| му|ҳои|р я|ҳуқ|қуқ|ҳақ|ии |к и| ша|и д| аз|и и| оз|нд |яд |қ д|озо|аз |зод|анд|д б|ояд| ка|ият|она|да |амо|ақ |а б|ди | ё |гар|ат |дан|ҳам|оди|рда|моя| он|уда|қи | ху|бо |и т|дон|ст |нам|н ҳ|ода|и с|ан |н б|мил|и х|бош|они|оша|худ|ава|боя|аст|и а|ро | ме|а ҳ|имо|ила|оми|оба|ида|кар|н д|лат|д в|а ш|ҳо | ас|таҳ|рои|и н|д к|яти| ди|шад|ӣ в|ри |рдо|шав| ми|е к|роб|тар|та |кор| бе|о д|вад|мон|иҳо|ли |уд |оси|ошт|ми |р м|ати|т б| со|ӣ ё|нҳо|мин|шар|ара|таъ|ани|а в|иро|а д|дав|ят |даа| са|ама|дош|раф|шуд|лӣ |д а|оти|а м| фа|ист|ор |р ҳ|на |и к|р к|д т|и ҷ|и ш| эъ| су|н м|н в|и ӯ|фи |вар|диҳ|ига|зар| шу|ари|а т| иҷ| ақ| ҳи|асо|р б|т ҳ|а а|одо|мум|р в|а о| ӯ |рон|наз|диг| ни|бот| ҷа|авр| қа|яи |р д|уқи|лал|кас|шта|уна|еҷ |ино|тҳо|уни|або|сти| во|авл|и қ|вла|ун |у о|ӣ б| ҳе|дӣ |қу |чун|н и|сар|ояи|тав|маҳ|онҳ|қар|атҳ|тир|оҳ |ахс| қо|уқ |оли| ис|д д|и з| ко|аза|ори|фар|сос|ран|н к|р а|ҷти|ону|сӣ |ири|рра|рӣ |ҳеҷ| за|ид |ҳти|рии|ами|қон|уди|н н| од|иҷт|мия|ъло|лом|ию |наи|али|нда|оӣ |оят|янд| зи|оян|ӣ ҳ|и п|офи|киш|ҳим|рат|тим",
    "kir": " жа|на |ана|жан| би|уу |уку|га |бир| ук|ар |ен |луу|тар|кук|укт| ка| ад|ын |ада|ууг|дам| ме|уга|ык | ар|ене|мен|нен|ан |ары|олу| бо|ин |ам |ган|ир |бол| ал|ара|нда|н к|туу|р б|н ж| ба|анд| же|р а|кта|ына|ард|кту|эрк|үн |да |н б|н э| эр|нди|а т| ко|рды|н а|дык|рки|инд|а ж|кин|ала|а а|лар|аны|үү | өз|а к|тер|алу| та|а у|алы|а э|же |ук |ийи| ти|иш |тий| ма|гө |кыл|йиш|улу|нын|ке |н т|кар|бар|или|у м| кы|иги|рын|а б|үгө|рга|е а|ун |етт|дик| ту|дар|тта|баш|у а|н у| ээ|дын|им |рүү|гин|лык|ушу|нды|тур| са| эл| эм| мү|гон|лга|алд|икт|үүг| бе|ры |өз |нан|он | ан|кте|ул |дай|ерд|диг|р м|ери|үчү| не|атт|лды|еке|еги|үнө|лук|амд|у б|ынд|үнү|рди|тук|ка |кан|к ж| ки|м а|күн|не |ине|мда|рин|ого|кет| со|кам|дин|к м| эч| то|сыз|ылу|өзү| де|н м|ция|ээ |чүн|гиз|уп |нег|эч |руу|ыз |мес|эме| иш|лут|ы м|шка|ыкт|мам|ашк|лде| ке|лго| тү|ө ж|олг|ес |к т|кор|ге |бил|түү|угу|рал|алг|тын|кен| ул|лим|утт|ыгы|орг|н н|у ж|рде|нуу|тал|ч к|рго|мак| те| уш|уну|ктө|ди |акт|нүн| ди|зүн|иле| кө|кат|аци|мсы| эс|тык|е к|ей |тан|е э|ай |ер |соц|оци|циа|аты| жо|к к|амс|лан|а м|ири|ске|айд|ирд| мы|ылы|зги|ыны|ага|ген|е б|шул|тол|өнү|дыг|е ж|ү ү|з к|айы|раб|енд|абы|жал|ү ж|оо |уна|к а|кал|лек|ект|рма|дей| үч|тоо|мат|у э|бер",
    "mkd": " на|на | пр| и |во | се|то |ите|те |рав|та |а с|пра|ува|да | да| не|ва |а п|а н|и с|ата|о н|еко|а и| по|но |ој |кој| со| за| во|ств|ја |ње |ање|аво|ни | им|от |е п|е н|ма |ат |вањ|ост|а д|о с|е и|се |ова|ија|и п| сл|а о|има|сек|сло|ото|ли |о д|ава|обо|о и| ил|или| би|бод|и н|лоб| од|бид|ред|ен |при|вот|иде|а в|ста| об|и и|и д|пре|нос|ст |е с| ни| ќе|ове|аат|аци|ќе |со |ови|про|ј и|тво| ра|ест|што| де|т и|акв| ко|раз|гов|его|нег|ани|едн|ако|циј|бра|од |а з|е б|и о|а б|о п|ват| е | др|ето|ваа|как|ди |т с| ка| чо|ени|алн|одн|ено| си|чов| шт|а г|а е|вен|нит| ја|де |оди|е о|ран|и з|сно|нот| ед|тит|лно|ви |јат|ден|т н|нац| оп| до| ос|и в|осн|кон|дна|е д| ст|век|о о|род|сто|сит|еме|ара|дно|обр|ј н|пшт|еди|опш|за |ние|аро|нов|а к|вни|дру| ов|тве|жив|ште|д н|ие | ме|ед |иот|и м|о в|ќи |дат|шти|јќи|без|бед|ки |ков|ко |а р|нар|чно|дни| вр|ели|нак|ашт|ичн|ка |ема|цел|зем|еду|чув|тес|држ|ник|т п|луч|аа |деј|нст|не |а ч|руг|ода|ивн| це|нив|дин|авн| зе|нио|пор|а м|заш|лас|вит|дек|го |ине|ело|нет|ез |тен| ре| из|под|раб|або|бот|дув|нув| бе|ење|еде|он |њет|зов|иту|ван|н и|аѓа|е в|еѓу|рем|дел|о к|кот|им | жи|дос|вре|меѓ|олн|нап| го|емј|кри|уна|нем|оја| су|ита|азо|лит|тор|инс|ора|огл|ипа|пот|слу|кви",
    "khk": " эр|эрх| хү|ний|н б|эн |тэй|ийг|х э|эй | бо|хүн| бү|йн |ан |ах | ба|ийн|бол|ий | ха|бай|уул|рх |оло|й х|йг |гаа|эх |бүр|гүй|үн | бу|он |аар|рхт|үнд|хтэ|үр |лэх|ар | за|н х|лах|эр | хэ|й б|өлө|н э|лөө|эл | үн|аа | ул|ын |хий|үй | ор| ту|улс|ула|үлэ| чө|чөл|н т|үүл| ху|сэн| ни|ндэ|лон|гээ|р х|өөр|сан| нэ|ны | ёс|нь |эд | гэ| нь| ч | тө| тэ|лаг|оро|дэс|лс |г х|ох |үни|ээр|хам|х ё| ша|д х|р э|лго|лд | дэ|н а|бую|уюу|гуу|төр|ай |юу |тай|ээ |ж б|эг |лий|хан|ыг | эд| то|х б|дсэ|й э|рга| ал|хар|арг|ад |лга|рэг| зо|айг|ага| тү|л х|ал | хө|өөт| са|н н|йгэ|дэл|нд |гий|н з|ол |ава|лла| өө|рол|өтэ|гэр|г б|л б|бус|нэг|н д|аг |аал|н ү|алд|рла| үз|гэм|й а|н у| ол|хуу|х ч|эрэ|мга|олг|эс |хүү|той| ар|үү |лал| эн| мө|йх |ин |өрө|х т|луу|рий|сон| га|хэн|айх|эни| ам|гла|өр |аса|ана|амг| би|ард| ял|йгм|ой |лын|үрэ|эгт| ав|эдэ|оо |мий|х н|аан|үйл|арл|нха|тгэ|дээ|с о|рхи|лов|д н|тэг|өг |өн |хэр|лэн|өөг|үүн|вср|га |р т| хи|хүр|рон|ч б| хо|гөө| мэ|бие|н г|ура|бүх|ори|али| аж| үй| яв|өх |хээ|г н|ата| та|гш |г ү|эгш|вах|лох|эгд|длэ|х ү|гох|үх |энэ|лж |олц| шү|л т| да|дал|эж |д б|лан|й т|айл|л н|х а|агл|тоо| со|өри|йгу|гми|дил|ээн|дар|н ш|шүү|овс| ад|а х|р ч|ади|ааг|лаа|айд|амь|гтэ|н с|д т|ийт|лэл|х ш|н ч|унх"
  },
  "Arabic": {
    "ara": " ال|ية | في|الح|في | وا|وال| أو|ة ا|أو |الم|الت|لحق|حق |لى |كل |ان |ة و|الأ| لك|لكل|ن ا|ها |ق ف|ات |مة |ون |أن |ما |اء |ته |و ا|الع|ي ا|شخص|ي أ| أن|الإ|م ا|حري| عل|ة ل|من |الا|حقو|على|قوق|ت ا|أي |رد | شخ| لل| أي|ق ا|لا |فرد|رية| ول| من|د ا| كا| إل|خص |وق |ا ا|ة أ|ا ي|ل ف|ه ا|نسا|جتم|ن ي|امة|كان|دة | حق|ام |الق|ة م| فر|اية|سان|ل ش|ين |ن ت|إنس|ا ل| لا|ذا |هذا|ن أ|لة |ي ح| دو|ه ل|لك |ترا|لتع|اً |له |إلى| عن|ى ا|ه و|ع ا|ماع|د أ|اسي| حر|ة ع|مع |الد|نون| با|لحر|لعا|ن و|، و|يات|ي ت|الج| هذ|ير |بال|دول|لإن|عية|الف|ص ا| وي|الو|لأس| إن|أسا|ساس|ماي|حما|رام|سية|انو|مل |ي و|عام|ا و|تما| مت|ة ت|علي|ع ب|ك ا| له|ة ف|قان|ى أ|ول |هم |الب|ة ب|ساو|لقا|الر|لجم|ا ك|تمت|ليه|لتم|لمت|انت| قد|اد |ه أ| يج|ريا|ق و|ل ا|ا ب|ال |يه |اعي|لدو|ل و|لإع|لمي|لمج|لأم|تع |دم |تسا|عمل|اته|لاد|رة |اة |غير|قدم|وز |جوز|يجو|عال|لان|متع|مان|فيه|اجت|م و|يد |تعل|ن ل|ر ا| يع| كل|مم |مجت|تمع|دون| مع|تمي|ذلك|كرا|يها| مس|ميع|إعل|علا| تم| عا|ملا|اعا|لاج|ني |ليم|متس|ييز|يم |اعت|الش| تع|ميي|عن |تنا| بح|لما|ي ي|يز |ود |أمم|لات|أسر|شتر|تي | جم|ه ع|ر و|ي إ|تحد|حدة| أس|عة |ي م|ة، |معي|ن م|لمس|م ب|اق |جمي|لي |مية|الض|الس|لضم|ضما|لفر| وس|لحم|امل|ق م|را |ا ح|نت | تن|يته| أم|إلي|واج|د و|لتي| مر|مرا|متح| ذل| وأ| تح|ا ف| به| وم| بم|وية|ولي|لزو",
    "urd": "ور | او|اور| کی|کے | کے|یں | کا|کی | حق|ے ک|ایٔ|کا |یٔے| کو|یا |نے |سے | اس|ٔے |میں|کو | ہے| می|ے ا| ان|وں | کر| ہو|اس |ی ا|ر ا|شخص| شخ|حق | سے| جا|خص |ہر |ام |ے م|ں ک|ہیں| یا|سی |ادی|آزا| آز|زاد|ص ک|ہ ا|ہے |جای|ا ح|ر ش|ت ک|کہ |م ک| پر|ی ک|ان |پر |۔ہر|دی |یٔی|س ک|ا ج|ر م|ہے۔|ق ہ|ں ا|ی ح|و ا|ار |ن ک|قوق|کسی|حقو|ری |وق |ے گ| ہی|ی ج| مع|سان| نہ| مل| حا|ٔی | جو|نی |کرن| لی|تی |ی ت|نسا|ل ک| کہ|جو |انس|اپن|ے ب|نہ | اپ|یت |ا ا|ہ ک| کس|ر ک|رے |ے ہ| ای|می |ل ہ|۔ ا|ے ل|ی ش|رنے|وہ |حاص|ی م|معا|اصل|صل |یں۔|ویٔ|نہی|ملک|ایس|انہ|ات |ی ب|د ک|ی ہ| تع|کیا|ق ک|ر ہ|ا م|دہ | من| بن| قو|ے ج|یہ |ں م|اشر|مل | دو|عاش|قوم|ر ب|انی|وام|قوا|اقو|لیٔ|دار| وہ| و | عا|ی س|بر |علا|اد |ہ م|و ت|ر ن| جس|ے۔ہ|ے، |انو| دی|گی |لیم|یوں| قا| یہ|دوس|ے۔ |ا ہ|تعل|یم |ر پ|جس |ریق|ے ح| اق|نیا|لک | گی|ین |یاد| مس|لاق|، ا|ی ن|پنے|وری|م ا| با|علی|یر |ی، |انے|ون |ن ا|ر ع| بر|ی آ|ر ح| رک|ے پ|کر |گا۔| پی|سب | گا|نا | پو|یسے|رای| مر|اری|قان|نون| مم|ندگ| اع|دگی|ہ و| ہر|ر س| چا|خلا|ا پ|ق ح| بھ|س م| شا|ہوگ|ے خ|وسر|رتی|ومی| بی|رکھ| مت|کوی|ر آ|پور|اف | مح|ے س|ہوں|نکہ|ونک|ت ا| طر|ے ع|یٔد|د ا|ال |ں۔ |م م|اں | مق|غیر|پنی| ام|ں، |من |ہو |ریع|و ک|ذری| ذر|عام|، م|دان|ادا|اعل|مام|تما| عل|دیو|بھی|ھی |بنی|ے ی|ا ک|اوی|ل م| زن|یاس|لان|عمل| عم|ت م| بچ",
    "skr": "تے |اں | تے|دے |دی |وں | دا| حق| کو|ے ا|کوں| دے|دا | دی|یاں| کی|ے ۔|یں |ہر | ۔ |کیت|ہے | وچ| ہے|وچ | ان| شخ|شخص|ادی|ال | حا|اصل|حق |حاص|ے م|خص |صل |ں د| نا|یا | ای|اتے|ق ح|ل ہ|ے و|ں ک| ات|ہیں|سی | مل|نال|زاد|ازا|ی ت| از|قوق|ار |ا ح|حقو| او|ص ک| ۔ہ|۔ہر|ر ش|دیا|ے ج|وق |ندے| کر|یند| یا|نہ | جو|کہی|ئے |ی د|سان|نسا|وند|ی ا|یتے|انس|ا ا|ملک|ے ح|و ڄ|ے ک|ڻ د| وی|یسی|ے ب|ا و| ہو|ں ا|ئی |ندی|تی |آپڻ|وڻ |ر ک|ن ۔| نہ|انہ|جو | کن| آپ| جی|اون|ویس|ی ن| تھ| کہ|ان |ری |ڻے | ڄئ| ہر|ے ن|دہ |ام |ں م|ے ہ|تھی|ں و|۔ ا|ں ت|ی ۔|کنو|ی ح|ی ک|نوں|رے |ہاں| بچ|ون |ے ت|کو | من|ی ہ|اری|ور |نہا|ہکو|یتا|نی |یاد|ت د|ن د| ون|وام|ی م|قوا|تا |ڄئے|پڻے| ہک|می | قو|ق ت|ے د|لے |اف |ل ک|ل ت| تع|چ ا|ین |خلا|اے |علا| سا|جیا|ئو |کرڻ|ی و|انی|ہو |دار| و |ی ج| اق|ن ا|یت |ارے|ے س|لک |ق د|ہوو| ڋو|ر ت| اے|ے خ| چا| خل|لاف|قنو|نون|پور|ڻ ک| پو|ایہ|بچئ|چئو|ات |الا|ونڄ|وری|این| وس| لو|و ا|ہ د| رک|یب |سیب|وسی|یر |ا ک|قوم|ریا|ں آ| جا|رکھ|مل |کاں|رڻ |اد |او |عزت| قن|ب د|وئی|ے ع| عز| ۔ک| مع|اقو|ایں|م م|زت |ڻی |یوڻ|ر ہ| سم|ں س|لوک| جھ| سی|جھی|ت ت|ل ا|اوڻ|کوئ|ں ج|ہی |حدہ|تعل|ے ذ|وے |تحد|متح|لا |ا ت|کار| اع|ے ر| مت|ر ا|ا م|ھین|ھیو|یہو| مط| سڱ|ی س|ڄے |نڄے|سڱد|لیم|علی|ے ق| ذر|م ت| کھ|ن ک| کم|ہ ا|سار|ائد|ائی|د ا| ہن|ہن |ی، |و ک|ں ب|ھیا|ذری|ں پ|لی ",
    "uig": " ئا| ھە|ىنى|ە ئ|نىڭ|ىلى| ۋە|ىڭ |ۋە | ئى| بو|ھوق|وقۇ| ھو|قۇق|نى |بول| ئە|لىك|قىل|ىن |لىش|شقا|قا |ەن | قى|ن ب|ھەم|ى ئ|ئاد|ىشى|دەم|ادە|كى |لىق|غان|ىي |ىغا|گە | بى|دىن|ىدى|ەت |كىن|ىكى|ندا|ۇق | تە|نلى|تىن|ەم |لەت|قان|ىگە|ىتى|ىش |ھەر|ئەر| با|ولۇ|دۆل|غا |اند| دۆ|اق |مە |لۇش|دە |لۇق| ئۆ|ان | يا|ەرق|ۆلە|ركى| قا|ەرك|ەمم|ا ئ|ممە|ۇقى|ىق | بە|رقا|داق|ارا|ىلە|رىم|ىشق|ى ۋ|لغا|مەن|اكى|ەر |ا ھ|دۇ |ياك|ۇقل|ئار|ق ئ|ىنل|لار| ئې|ى ب|لىن|ڭ ئ|ئۆز|ق ھ|شى |ىمە|قلۇ|ن ئ|لەر|ەتل|نىش|ىك |ەھر| مە|ھرى|لەن|ىلا|ار |بەھ| ئۇ|ە ق|ئىي|اسى| مۇ|رلى| ئو|بىر|، ئ|بىل|ش ھ|بار|ى، |ۇ ھ|ايد|ۇشق|شكە|ە ب|يەت|ا ب|رنى|كە |ىسى| كې|ېلى|الى|ەك |م ئ|ماي|ولم|تنى|ىدا|ارى|يدۇ|لىد| قو|ەشك|تلە|ك ھ|انل|ەمد|مائ|ئال|ر ئ|مدە|ىيە|ش ئ|ە ھ|لما|ائى|ئىگ|دا |ي ئ|ۇشى|راۋ|ا، |سىي| تۇ|كىل|ە ت|ىقى|قى |ۆزى|ېتى|ىرى|ىر |ىپ |ى ك|ن، |ر ب|لەش|اسا|اۋا|ى ھ|شلى|ساس|ادى|تى |اشق|ەتت|قىغ|ىما|انى| خى|ۇرۇ| خە|ن ق|منى| خا|چە |ى ق| جە|رقى|تىد| ھۆ|باش|ارل|ئىش|تۇر| جى|مۇش|نۇن|شۇ |انۇ|ۇش |رەك|ېرە|كېر| سا|الغ|ۇنى|ئېل|ىشل|تەش|خەل|مەت|اش |دىغ|كەن|ەلق|تىش|مىن|ايى|سىز|ق ۋ|نىي|جىن|رىش|پ ق| كى|ېرى|ئاس|ەلى| ما|تتى|ىرل|ولى| دە|ارق|سىت|ە م| قە|شىل| تى|ەرن|كىش|ن ھ|ەلگ|ەمن|ك ئ| تو|ى ي|قتى|ئاش|تىم|تەۋ|ناي|ىدە|ىنا| بۇ|ىيا|زىن|امى|قار|شكى|ىز | ئۈ|ەۋە|ۆرم|ە خ|شىش|ىيى|جتى|ىجت|ئىج|نام|تەر",
    "pes": " و | حق| با|که |ند | که| در|در |رد | دا|دار|از | از|هر | هر|یت |ر ک|حق |د ه|ای |د و|ان | را|ین |ود |یا | یا|را |ارد|ی و|کس | کس| بر| آز|باش|ه ب|آزا|د ک| خو|ه ا|د ب|زاد| اس|ار | آن|ق د|شد |حقو|قوق|ی ب|وق |ده |ه د|ید |ی ک|و ا|ور |ر م|رای|اشد|خود|ادی|تما|ری | اج|ام |دی |اید|س ح|است|ر ا|و م| ان|د ا|نه | بی|با | هم| نم|مای| تا|د، |ی ا|انه|ات |ون |ایت|ا ب|ست | کن|برا|انو| بش| مو|این| مر|اسا| مل|وان|ر ب|جتم| شو| اع|ن ا|ورد| می| ای|آن | به|و آ|ملل|ا م|ماع|نی |ت ا|، ا|ت و|ئی |عی |ائی|اجت|و ب|های|ن م|ی ی|بشر|کند|شود| من| زن|ن و|ی، |بای|ی ر| مس|مل |مور|ز آ|توا|دان|اری|علا|گرد|یگر|کار| گر| بد|ن ب|ت ب|ت م|ی م| مق|د آ|شور|یه |اعی| عم|ر خ|ن ح| کش|رند|مین| اح|ن ت|ی د| مت|ه م|د ش| حم|و د|دیگ|لام|کشو|هٔ |ه و|انی|لی |ت ک| مج|ق م|میت| کا| شد|اه |نون| آم|اد |ادا|اعل|د م|ق و|ا ک|می |ی ح|لل |نجا| مح|ساس|یده| قا|بعی|قان|ر ش|مقا|ا د|هد |وی |نوا|گی |ساو|ر ت|بر |اً |نمی|اسی|اده|او | او| دی| هی|هیچ|ه‌ا|‌ها|یر |خوا|د ت|همه|ا ه|تی |حما|دگی|بین|ع ا|سان|ر و|شده|ومی| عق| بع|ز ح|شر |مند| شر|ٔمی|أم|تأ|انت|اند|اوی|مسا|ردد|بهر| بم|ارن|یتو|ل م|ران|و ه|ر د|م م|رار|عقی|سی |و ت|زش | بو|ا ا|ی ن|موم|جا |عمو|رفت|عیت| فر|ندگ|واه|زند|م و|نما|ه ح|ا ر|دیه|جام|مرد|ت، |د ر|مام| تم|ملی|نند|الم|طور|ی ت|تخا|ا ت|امی|امل|دد | شخ|شخص"
  },
  "Devanagari": {
    "hin": "के |प्र|और | और| के|ों | का|कार| प्|का | को|या |ं क|ति |ार |को | है|िका|ने |है |्रत|धिक| अध|अधि|की |ा क| कि| की| सम|ें |व्य|्ति|क्त|से | व्|ा अ|्यक|में|मान|ि क| स्| मे|सी |न्त| हो|े क|ता |यक्|क्ष|ै ।|िक |त्य| कर|्य | या|भी | वि|रत्|र स|ी स| जा|स्व|रों|्ये|ेक |येक|त्र|िया|ा ज|क व|र ह|ित |्रा|किस| अन|ा स|िसी|ा ह|ना | से| पर|र क| सा|देश|गा | । | अप|्त्|े स|समा|ान |ी क|्त |वार| ।प|ा प| रा|षा |न क|।प्|ष्ट|था |अन्| मा|्षा|्वा|ारो|तन्|वतन|ट्र|्वत|प्त|ाप्|्ट्|राष|ाष्| इस|े अ| उस| सं|राप|कि |त ह|हो |ं औ|ार्|ा ।|किय|े प| दे| भी|करन|री |जाए|ी प| न |र अ|क स|अपन|े व|ाओं|्तर|ओं | नि|सभी|रा | तथ|तथा|िवा|यों|पर | ऐस|रता|ारा|्री|सम्| द्|ीय |िए |व क|सके|द्व|होग| सभ|ं म|माज|रने|िक्|्या|ा व|र प| जि|ो स|र उ|रक्|े म|पूर| लि|ाएग| भा|इस |त क|ाव |स्थ|पने|ा औ|द्ध|श्य|र्व| घो|घोष|रूप|भाव|ाने|कृत|ो प|े ल|लिए|शिक|ूर्| उन|। इ|ं स|य क|्ध |दी |ी र|र्य|णा |एगा|न्य|रीय|ेश |रति|े ब| रू|ूप |परा|्र |तर्| पा| सु|जिस|तिक|सार|जो |ेशो| शि|ानव|ी अ|चित|े औ| पू|ियो|ा उ|म क|ी भ|शों| बु|म्म|स्त|िश्|्रो|्म |ो क| यह|र द|नव |चार|दिय|े य|र्ण|राध|ोगा|ले |नून|ानू|ोषण|षणा|विश| जन|ारी|परि|गी |वाह|साम|ाना|रका| जो|ाज |ी ज|ध क|बन्|ताओ|ंकि|ूंक|ास |कर |चूं|ी व|य ह|ा ग|य स|न स|त र|कोई|ुक्|ोई | ।क|ं न|हित|निय|याद|ादी|्मा|्था|ामा|ाह |ी म|े ज",
    "mar": "्या|या |त्य|याच|चा | व |ण्य|प्र|कार|ाचा| प्|धिक|िका| अध|अधि|च्य|ार |आहे| आह|ा अ|हे | स्|्रत|्ये|ा क|स्व| कर|्वा|ता |ास |ा स|ा व|त्र| त्|वा |ांच|यां|िक |मान| या|्य | का| अस|रत्|ष्ट|र्य|येक|ल्य|र आ|ाहि|क्ष| को|ामा|कोण| सं|ाच्|ात |ा न| रा|ंत्|ून |ेका| सा|राष|ाष्|चे |्ट्|ट्र|तंत| मा|ने |किं| कि|व्य|वात|े स|करण|ंवा|िंव|ये |क्त| सम|ा प|ना | मि|कास|ातं|्र्|र्व|समा|मिळ| जा|े प|व स|यास|ोणत|रण्|काम|ीय |ा आ| दे|े क|ांन|हि |रां| व्|्यक|ा म|िळण|ही | पा|्षण|ार्|ान |े अ| आप| वि|ळण्|ाही|ची |े व|्रा|मा |ली |ंच्|ारा|ा द| आण| नि|णे |द्ध| नय|ला |ा ह|नये| सर|सर्|्री|बंध|ी प|आपल|ले |ील |माज| हो|्त |त क|ाचे|्व |षण |ंना|लेल|ी अ|देश|आणि|णि |ध्य| शि|ी स|े ज|शिक|रीय|ानव|पाह|हिज|िजे|जे |क स|यक्|न क|व त|ा ज|यात|पल्|न्य|वी |स्थ|ज्य| ज्|े आ|रक्|त स|िक्|ंबं|संब| के|क व|केल|असल|य अ|य क|त व|ीत |णत्|त्व|ाने| उप|्वत|भाव|े त|करत|याह|रता|िष्|व म|कां|साम|रति|सार|ंचा|र व|क आ|याय|ासा|साठ|ाठी|्ती|ठी |ेण्|र्थ|ीने|े य|जाह|ोणा|संर|ायद|च्छ|स स|ंरक|तील|ी व|त आ|ी आ|ंधा|ेशा|ित | अश|हीर| हक|हक्|क्क|य व|शा |व आ|तीन|ण म|ूर्|ेल्|द्य|ेले|ांत|ा य|ा ब|ी म|ंचे|याव|देण|कृत|ारण|ेत |िवा|वस्|स्त|ाची|नवी| अर|थवा|अथव|ा त| अथ|अर्|ती |पूर|इतर|र्ण|ी क|यत्| इत| शा|रका|तिष|ण स|तिक|्रक|्ध |रणा| आल|ेल |ाजि| न्|धात|रून|श्र|असे|ष्ठ|ुक्|ेश |तो |जिक|े म",
    "mai": "ाक | आ |प्र|कार|िका|धिक|ार |्रत|ेँ |क अ|्यक|िक |्ति| अध|व्य|अधि|क स| प्|क्त| व्|केँ|यक्|तिक|न्त| स्|हि |क व|मे |बाक|मान| सम|त्य|क्ष| छै|छैक|ेक |स्व|त्र|रत्|्ये|ष्ट| अप|येक|र छ|सँ |वा | एह|ैक।|ित | वि| जा|ति |्त्|ट्र|िके|राष|ाष्| हो|्ट्| रा|्य | सा| अन| कर|अपन|।प्|कोन|अछि|वतन|्वत|तन्|क आ| अछ|ताक|था | पर| वा| को|ार्|एहि|पन |ा आ|नहि|नो |समा| मा|्री|रता| नि| का|देश| नह|्षा|क प| दे| कए|रक | सं|ोनो|ि क|न्य|आ स|छि |्त |ल ज|्वा|ारक|ा स|तथा|ान्| तथ|्या|आ अ|ना |ँ क|ान | जे|जाए|वार|ता |ीय |र आ|क ह|करब|िवा|ामा|र्व| आओ|्रस|परि|त क|स्थ|ा प|ानव|रीय|धार|्तर|अन्|घोष|साम|माज|आओर|ारण| एक|कएल|ँ अ|ओर |एबा|स्त|द्ध|्रा|ँ स|रण | सभ|ोषण|क।प|ाहि|रबा|क ज|ा अ|चित|यक |कर |पूर|रक्|नक | घो|षा |िक्|सम्|एहन| उप|र प| अव|एल |ूर्|षणा| हे|त अ|शिक|तु |ाधि|ेतु|हेत|हन |िमे|र अ|वक |ँ ए|जाह| शि|आ प|भाव|े स|्ध |क क|ि ज|प्त|रूप|निर|िर्| सक|च्छ|होए|रति|अनु|सभ |हो |ेल |त आ|चार|ण स|रा |त ह|जिक|ाजि|र्ण|्रक|एत।|ि आ|र्य|सभक|ैक |क उ| जन|त स|ाप्|न प|श्य|न अ|कृत|हु |रसं|री |राप|ा व|जे |क ब|ि घ| भा|उद्|ाएत|्ण |विव| उद|वाध|िसँ|आ व|ि स|न व|ारा|ोएत| ओ |य आ|कान|िश्|न क| दो|णाक| द्|हिम| अथ|अथव|ामे|द्व|ेश |ओ व|ि अ|क ए|वास| पू|षाक|त्त|य प| बी|यता|धक |ए स|थवा|ि द|पर | भे|जेँ| कि|कि |क ल| रू|विश|न स| ले|सार|ाके|िष्|रिव|क र|ास |ेओ |्थि|केओ|राज",
    "bho": " के|के |ार |े क|कार|धिक|िका|ओर |आओर| आओ| अध|अधि|े स|ा क|े अ| हो| सं|र क|र स|ें | मे|में|िक | कर|ा स|र ह| से|से |रा |मान| सम|न क|क्ष|े ब|नो | चा|वे |ता |चाह|ष्ट| रा|ति |्रा|खे |राष|ाष्|प्र| सा| का|ट्र|े आ| प्| सक| मा|्ट्| स्|होख| बा|करे|ि क|ौनो|त क|था |कौन|पन | जा| कौ|रे |ाति|ला | ओक|ेला|तथा|आपन|्त | आप|कर |हवे|र म| हव| तथ|सबह|र आ|ोखे| ह।|िर |े ओ|केल|सके|हे | और|ही |तिर|त्र|जा |ना |बहि|।सब|े च| खा|े म| पर|खात|ान |र ब|न स|ावे| लो|षा |ाहे|ी क|ओकर|ा आ|माज|ित |े ज|ल ज|मिल|संग|्षा|ं क| सब|ा प|और |रक्|वे।|िं |े ह|ंत्|ाज |स्व|हिं|नइख|कान|ो स| जे|समा|क स|लोग|करा|क्त|्रत|ला।| नइ|े। |ानव|िया|हु |इखे|्र |रता|्वत|ानू|े न|ाम |नून|ाही|वतं|पर |ी स| ओ |े उ|े व|्री|रीय|स्थ|तंत|दी |ीय |े त|र अ|र प|्य |साम|बा।| आद|ून |। स|व्य|ा।स|सभे|भे |या | दे|ा म|े ख| वि| सु|केह|प्त|योग|ु क|ोग |े द|चार|ादी|ाप्| दो| या|राप|ल ह|पूर| मि|तिक|खल |यता|्ति| बि|ए क|आदि|दिम| ही|हि |मी | नि|र न| इ |ेहु|नवा|ा ह|री |ले | पा|ाधि| सह| उप|्या| जर|षण | सभ|िमी|देश|े प|म क|जे |ाव | अप|शिक|ाजि|जाद|जिक|े भ|क आ|्तर|िक्|ि म|ेकर|ुक्|वाध|गठन| व्|निय|ठन |।के|ामा|रो | जी|य क|न म|े ल|न ह|ास |ेश | शा|घोष|ंगठ|िल | घो|्षण| पू|े र|ंरक|संर|उपय|पयो|हो |बा |ी ब|्म |सब |दोस|ा। | आज|साथ| शि|आजा| भी| उच|ने |चित| अं|र व|ज क|न आ| ले|नि |ार्|कि |याह|्थि",
    "nep": "को | र |कार|प्र|ार |ने |िका|क्त|धिक|्यक| गर|व्य|्रत| प्|अधि|्ति| अध| व्|यक्|मा |िक |त्य|ाई |लाई|न्त|मान| सम|त्र|गर्|र्न|क व| वा|्ने|वा | स्|रत्|र स|्ये|तिल|येक|ेक |छ ।|ो स|ा स|हरू| वि|क्ष|्त्|िला| । |स्व|हुन|ति | हु|ले | रा| मा|ष्ट|समा|वतन|तन्| छ |र छ| सं|्ट्|ट्र|ाष्|ो अ|राष|्वत|ुने|नेछ|हरु|ान |ता |े अ|्र | का|िने|ाको|गरि|े छ|ना | अन| नि|रता|नै | सा|ित |तिक|क स|र र|रू |ा अ|था |स्त|कुन|ा र|ुनै| छै|्त |छैन|ा प|ार्|वार|ा व| पर|तथा| तथ|का |्या|एको|रु |्षा|माज|रक्|परि|द्ध|। प| ला|सको|ामा| यस|ाहर|ेछ |धार|्रा|ो प|नि |देश|भाव|िवा|्य |र ह|र व|र म|सबै|न अ|े र|न स|रको|अन्|ताक|ंरक|संर|्वा| त्|सम्|री |ो व|ा भ|रहर| कु|्रि|त र|रिन|श्य|पनि|ै व|यस्|ारा|ानव| शि|ा त|लाग|रा |शिक| सब|ाउन|िक्|्न |ारक|ा न|रिय|्यस|द्व|रति|चार| सह|्षण| सु|ारम|ुक्|ुद्|साम|षा |ैन | अप| भए|बाट|ुन | उप|ान्|ो आ|्तर|िय |कान|ि र|रूक|द्द|र प|ाव |ो ल|तो | पन|ैन।| आव|ा ग|।प्|बै |ूर्|िएक|र त|निज|त्प| भे|जिक|ेछ।|िको|्तो|वाह|त स|ाट | अर|ाजि|्ध | उस|रमा|ात्|र्य|नको|ाय |जको|ित्|ागि| अभ|न ग|गि |ा म| आध|स्थ| पा|ारह|घोष|त्व|यता|ा क|र्द| मत|विध| सक|सार|परा|युक|राध| घो|णको|अपर|े स|ारी|।कु| दि| जन|भेद|रिव|उसक|क र|र अ|ि स|ानु|ो ह|रुद| छ।|ूको|रका|नमा| भन|र्म|हित|पूर|न्य|क अ|ा ब|ो भ|राज|अनु|ोषण|षणा|य र| मन| बि|्धा| दे|निर|ताह|र उ|यस |उने|रण |विक",
    "mag": "के | के|ार | हई|कार|िका|धिक|हई।| और|े अ|और |अधि| अध|ा क|र ह|े स|े क|सब |ें |में| मे| कर|से | सम|था |तथा| हो| से|र स|र क|िक | तथ| सब| सं|क्ष|मान|ब क|ा स|ना | सा|प्र|कर | प्| भी|ति |ई। |रा |भी |्रा| अप| का|त क|या |अपन| को|ट्र|क ह|पन | पर| मा| रा| या|ी क|ता | स्| ओक|ष्ट|ही |ान |्त |करे|्रत|त्र|ाष्|्ट्| सक|न क|राष|ओकर|।सब|रे |ेल |हई |े ब| जा|ई।स|रक्| ले|ंत्|े म| ही|सक |नो |र म| ना|स्व|ाम |होए|र औ|दी |व्य|क्त|ा प|वतं|ानव|ित | शा|ादी|षा |माज| इ |तंत|पर |ी स|्वत|्य |े उ|्र |ोग |वे |्षा|े भ|े ल|न स|करा|कान| एक|ल ज|म क|लेल|्ति|ावे| दे|रता|क स|साथ|ानू|नून|ेकर|र अ|य क|ाथ |प्त|ा म|ला |ई।क| वि|समा|ून |े प|साम|। स|ा ह| जे|े ह| चा|ोई |जा |मिल| व्|ि क|बे |ाप्|राप|ोए |रो |वार|कोई|चाह| दो|व क| नि|चार|र व|ाधि| पा|र प|स्त|एल |कोन|े व|ोनो|काम|ो स|्म |े ओ|योग| सु|ए क|नवा|न ह|षण |ीय |एक |परि| उप|े आ|्तर| सह|ाजि|ल ह|संर|ई क|ास |पूर|ं स|ंरक|ो क|जिक|देश|ुक्|ामा|होब|सम्|।के|्यक|े च|केक|्वा|पयो|उपय|री |ी ह|ाही|दोस|र आ| उच|ाति|म्म|्मा|े ख| लो|तिक|रति|ेश |न औ|स्थ|वा |मी |े त| आद|निय|न प|वाध| घो|घोष|ब अ|रिव|ा ब|कि |म स|रीय|्री|य स|यक्|ि म|ा द|ा त|ब ह|जाद|उचि|युक|ंयु|संय| उ |इ स|े इ|्षण|। त|चित|ा औ|व ह|हे |त स| पू|क औ|ग क|े न|न द|करो|लोग|ोषण|ारा|र न|िल |समय|कौन|ं क|मय |ौनो|ुरक|ो भ| भा|ाज | कए|कएल|सुर|र्म|ाव |िवा"
  },
  "Ethiopic": {
    "amh": "፡መብ|ሰው፡|ት፡አ|ብት፡|መብት|፡ሰው|፡አለ|፡ወይ|ወይም|ይም፡|ነት፡|ንዱ፡|አለው|ለው።|ዳንዱ|ያንዳ|ንዳን|እያን|ዱ፡ሰ|ት፡መ|፡እን|፡የመ|።እያ|እንዲ|፡ነጻ|፡የተ|ም፡በ|ው፡የ|ም፡የ|፡የሚ|ና፡በ|ን፡የ|፡የማ|፡አይ|ነጻነ|ና፡የ|ው፡በ|ቶች፡|ው።፡|ሆነ፡|ት፡የ|፡በሚ|፡መን|ው።እ|ትና፡|ኀብረ|ትን፡|ውም፡|ንኛው|እኩል|ብቻ፡|ኛውም|ንም፡|፡ለመ|፡ያለ|ም፡ሰ|ማንኛ|መብቶ|፡አገ|ት፡በ|ራዊ፡|፡እኩ|፡ለማ|ለት፡|በት፡|ሆን፡|መንግ|፡በተ|ረት፡|ብቶች|ጋብቻ|ዎች፡|ህንነ|ጻነት|ም፡እ|ወንጀ|፡ልዩ|ሰብ፡|ማንም|ጠበቅ|ኩል፡|ደህን|።ማን|ነጻ፡|ግኘት|ማግኘ|።፡እ|፡የሆ|፡ሁሉ|ች፡በ|፡በመ|ሥራ፡|፡ደህ|ፈጸም|ል፡መ|ተግባ|፡ድር|ት፡ወ|ው።ማ|ፍርድ|ርድ፡|፡በሆ|ር፡ወ|በትም|ትም፡|ይነት|ቸው፡|ብ፡የ|ነትና|ቱን፡|ሕግ፡|ንና፡|፡ሥራ|የማግ|፡መሠ|ኘት፡|፡ጊዜ|ጻነቶ|ነቶች|በር፡|በኀብ|ዩነት|ልዩነ|፡በኀ|፡ዓይ|ዓይነ|ችና፡|ግባር|ባር፡|፡ደረ|ነው።|፡ነው|ደረጃ|ም።እ|ም፡መ|፡ወን|ይማኖ|ማኀበ|ሃይማ|፡ኑሮ|መሠረ|ሁሉ፡|ነቱ፡|ሌሎች|ንግሥ|በቅ፡|የሆነ|፡ይህ|ንዲጠ|ገር፡|ተባበ|ትክክ|ጸም፡|ር፡የ|ዲጠበ|ትም።|ው፡ከ|፡እያ|ሩት፡|ድርጅ|፡ብቻ|ና፡ለ|ይገባ|የመኖ|፡ማን|ንነት|ቤተሰ|ርጅት|ት፡ድ|፡መሰ|እንደ|፡አላ|ብሔራ|ት፡ለ|ሔራዊ|ርት፡|ህርት|ውን፡|የሚያ|ል።እ|ሆኑ፡|ምህር|ትምህ|በት።|ለበት|አለበ|፡አስ|ሎች፡|ች፡የ|፡በሕ|ብረ፡|፡ከሚ|ን፡አ|ት፡እ|ን፡ወ|ረግ፡|በሆነ|የኀብ|፡የኀ|መሆን|፡መሆ|ን፡መ|፡ውሳ|ንጀል|ፈላጊ|ህም፡|ረታዊ|ክለኛ|ክክለ|ታዊ፡|ጀል፡|ኑሮ፡|።፡ይ|ዓዊ፡|ዜግነ|ንዲሁ|ዲሁም|፡ማኀ|ገሩ፡|ር፡በ|ብዓዊ|አገሩ|ሁም፡|ና፡ነ|ሰብዓ|የተባ|ጅት፡|ማኖት|ር፡አ|ንግስ|ኖት፡|በሕግ|መኖር|ው፡ያ|መጠበ|ረጃ፡|፡በማ|ነትን|ብነት|ገብነ|፡ገብ|መፈጸ|፡ሁኔ|ሁኔታ|ን፡ለ|ው፡ለ|፡ተግ|፡የአ|፡ይገ|፡በአ|ችን፡|፡ትም|ነቱን|፡ቢሆ|ቢሆን|ጊዜ፡|ረ፡ሰ|ት፡ጊ|ሰቡ፡|ምበት|ላቸው|አላቸ|በነጻ|፡በነ|አንድ|ቅ፡መ|፡መጠ|ት፡ይ|መሰረ|ጥ፡የ|ስጥ፡|ፈጸመ|ውስጥ|ንድ፡|፡ውስ|፡በግ|፡ሆኖ|ሉ፡በ|፡ጋብ|ንስ፡|ንነቱ|መው፡|የሚፈ|አይፈ|ብረሰ|ነ፡መ|፡የሃ|ም፡ከ|ች፡እ|ስት፡|ሙሉ፡|አገር|ሆኖ፡|ደረግ|ኢንተ|ንተር|ተርና|ርናሽ|ናሽና|ሽናል",
    "tir": " መሰ| ሰብ|ሰብ | ኦለ|ትን |ኦለዎ|ናይ | ናይ| ኦብ|ዎ፡፡|ለዎ፡|ሕድሕ|ኦብ |ድሕድ|ሕድ |መሰል|ውን |ሰል |ድ ሰ|ይ ም|ል ኦ|ካብ |፡ሕድ|፡፡ሕ| ወይ|ወይ | መን| ነፃ|ን መ|ዝኾነ|፡፡ |ታት |ብ ዝ|ነት |ን ነ| ካብ|መሰላ|ነፃነ| እዚ|ብ መ|ኦዊ |ታትን|መንግ|ዊ መ| እን|ብ ብ|ንግስ|ት ኦ|ሰላት|ን ም|ኾነ |እዚ |ብኦዊ|ሰብኦ|ን ኦ|ን፡፡| ንክ| ዝኾ|ን ን| ምር|ኹን |ይኹን| ይኹ|ምርካ|ርካብ| ኦይ| ሃገ|ሕጊ |ራት |ሎም | ብሕ|ነ ይ| ከም|ማዕሪ|ይ ብ| ንም| ዝተ|ርን |ን ብ|ራዊ | ፣ |ብ ሕ|ላትን|ብ ኦ|ማሕበ|ነታት| ኦድ|ዕሪ | ማዕ|ስታት|ግስታ|’ውን|ት መ|ን ዝ|ታዊ |፣ ብ| ማሕ|ነትን|ንጋገ|ድንጋ| ስለ| ድን|ስራሕ|ኩሎም|ሕበራ|ኦት |ን ሰ|ዓለም|ፃነታ| ብም|ት ወ|መሰሪ| ስራ|ፃነት|ተሰብ|ካልኦ|ልኦት|ን ሓ|ዓት |ዋን |ቡራት|ሕቡራ| ሕቡ|ብሕጊ|ድብ |ውድብ| ውድ|ብን |ትምህ|ነቱ |ዚ ድ|፣ ኦ|ሃገራ| ኩሎ|ለዎም|ምህር|ም፡፡|ም መ| ብዝ|ምኡ’|ኡ’ው|እንት| ዓለ| ብዘ|በራዊ| ሓለ|ሓለዋ|ዎም፡|ቱ ን|ት ብ|ጋገ |ነፃ | ምዃ|ን ዘ| ገበ|ት፣ | ትም|ኸውን|ራሕ | ዘይ|ህርቲ|ርቲ |ከምኡ|ሃይማ| ምስ|ነ፣ |እንተ| ስር|ስርዓ|ርዓት|ባት |ይማኖ|ሰሪታ|ን ና| ክብ|ልን | ብማ|ገሩ | ህዝ|ላት |ት ና|ይ ኦ|ዕሊ |ለዝኾ|ስለዝ|ሪተሰ|ብሪተ|ሕብሪ| ሕብ|ን ተ|ኾነ፣|በን |ሃገሩ|ገ እ|ኻዊ | ሃይ|እን |ሪጋገ| ምሕ|ን እ|ለኻዊ|ር፣ | ብሓ| ብሃ| ክኸ|ክኸው|ብ ዘ|ዃኑ |ዊ ክ|ምን |ሓደ |ምዃኑ|ም ን|ት እ|ዊ ወ|ታውን| ሕድ|ብዘይ| ሕጊ|ት ን| ልዕ| ካል|ን ካ|ሰባት|ን ስ|ናን |ቤተሰ|ሕን |ለምለ|ት ስ|ምለኻ|፣ ከ|ተደን|ባል |ኦድላ|እዋን| እዋ|ደቂ | ደቂ| ሰባ|ፃን |ነፃን|ግስቲ|፣ ን|ዚ ብ|ስቲ | ቤተ|ምጥሓ| ክሳ| ነዚ|ን ክ|ነቲ | ነቲ|ነዚ | ምእ|ብነፃ| ምዕ|ምዕባ|ዕባለ|ክሳብ| ብነ|ል እ|ዚ መ|ልዕሊ|ክብሩ|ብማዕ|ሳብ |ህይወ|ኦቶም|ምስ |ንገገ|እምነ| እም|ድ ኦ|ቶም |ቲ ክ|ፍትሓ|ለም | ፍት|ብ ን|ን ዓ|ራውን|ሓፈሻ|ደንገ|ም ብ|ትዮን| ዝሰ|ዝተደ|ሉ መ|ብ ና|ጊ ካ|ልዎ |ኦባል| ኦባ|ድልዎ|ን ድ|ኦድል|ዜግነ|ላውን| ድሕ"
  },
  "Hebrew": {
    "heb": "ות |ים |כל |ת ה| כל|דם |אדם|יות| של| זכ|ל א| אד|של |ל ה|אי |ויו|כאי|ת ו|י ל|זכא| ול|לא | וה|רות|זכו|ית |ירו|ין | או|ם ז| לא| הח|או | הא| וב| המ|חיר|ת ל|יים|ם ל|את |ת ב|ת ש|רה |ון | לה|נה |כוי|ותי|ה ש|ו ל|ו ב| הו|ת א|ם ב|ם ו|תו | את|לה |ני |אומ| במ|דה |א י|ה ה|ה ב|על |ם ה| על|הוא|וך |ה א|בוד|וד |ואי|נות|ה ו|ת כ|י ה|יה |ם ש|ו ו| שה|ם א|ו כ|ינו|ן ה| שו|שוו|החי|כות|לאו|בות|דות|ה ל|לית|ה מ| בי|וה |וא | הי| לפ|ור | לב|ל ב|בחי|הכר|לו |ת מ|ן ש|החו|ה כ| בכ|ומי|בין|ן ו|ן ל|רוי|פלי|ולה|ליה| הז|חינ| לע| בנ|יבו|חוק| אח|חבר| יה| חי|מי |ירה| חו|האד|ווה|חופ|ופש|וק |נו |יו |ל מ|מדי|כבו| הע|נוך| הד|י א|י ו| הכ|בני|עה |ו א|רצו|דינ|בזכ|מות|יפו| אל|סוד|לם |איש|רך | אי|הגנ|הם |פי |ם כ|חות|ל ו|איל|ילי|תיה|כלל|אלי|יסו|האו|זש | בא|ר א|ו ה|זו |אחר| הפ| בע| בז|משפ| בה| לח|דרך|ומו| בח| דר| מע|ל י|תוך|מנו| בש|לל |רבו| למ|פני| לק|תם |שה |שית|ללא|לפי|היה|מעש|דו |שות|להג|וצי|שוא|אין|וי |תי |ונו|ליל| לו|חיי|ל ז| זו|היא|יא |נתו|ה פ|לת |ובי| לכ|ך ה|יל |י ש|שיו|ן ב|עול|המד|ודה|ולם| ומ|א ה|ולא| בת|הכל| סו| מש| עב|סוצ|ארצ| אר|ציא|ד א|לחי|הן |יחס| יח|יאל|הזכ|ם נ| שר|בו |עבו|היס| לי|ת ז|פול|יהי|גבל|תיו|המא|שהי|א ל|מאו| יו|ותו|ישי|גנה|פשי|וחד|יהם|חרו|לכל|ידה|עות|ונה|ום |חה |עם |שרי|ם י|שר |והח| אש| הג|ק ב|הפל|נשו|הגב|ד ו",
    "yid": " פֿ|ון |ער |ן א| אַ|דער|ט א| או|און|אַר|ען |פֿו| אױ| אי|ן פ|ֿון|רעכ| דע| רע|עכט|פֿא|ן ד|כט | די|די |אַ |אױף|ױף |ֿאַ| זײ| גע|אַל|אָס| אָ|ונג| הא|האָ|זײַ| מע|אָל|נג |װאָ|ַן |אַנ|רײַ| װא|ָס |באַ| יע|יעד|ניט|ן ז|ר א|יט |אָט|אָר|עדע|מען|זאָ|ָט |פֿר|ײַן| בא|טן |אין|ן ג|ין |ן װ|נאַ|ֿרײ|ר ה| זא|לעכ|ע א|אָד|ַ ר|ענט|אַצ|ַצי|אָנ| צו| װע|יז |מענ|ָדע|איז|ן מ|ַלע|בן |ר מ|טער| מי| פּ|מיט|טלע|ָל |עכע|ײט |ַנד|ע פ|לע |געז|לאַ|אַפ|עזע|ראַ| ני|ַפֿ|רן |ײַנ|נען|טיק|כע |פֿע|יע |הײט|ַהײ|נטש|ײַה|ט ד|ן ב|לן |ן נ|פֿט|שאַ|רונ| זי| װי|ט פ| דא|טאָ|דיק|קן |ר פ|ר ג|יקן|אָב|ף א|אַק|קער|ערע|כער|י פ|ות |ַרב|פּר|קט |עם |יאָ|ציע|ציא|יט־|צו |ישע| קײ|ן ק|סער| גל|דאָ|ונט|גן |ַרא|יקע| טא|ענע|לײַ|שן |ַנע|יק |טאַ|ס א|עט |נגע|ט־א|ָנא|־אי|יקט|נטע|ײנע|־ני|ָר |װער|י א|ן י|יך |זיך|ער־|ערן|אױס|ָבן|נדע|ָסע|װי |ֿעל|ר־נ|ן ה| גר|גלײ| צי|ראָ|זעל|עלק|נד |לקע|אָפ| כּ|ט װ|ג א| נא|ט צ|ר ד|עס |דור|גען|קע |ג פ|ֿט |ן ל|שע |ר ז|רע |ײטן|פּע|קלא|קײט|יטע|ים |ס ז|ײַ | דו|אַט| לא|ר װ|קײנ|עלש|י ד|לשא|יות|נט |ַרז|ע ר|ל ז|אַמ|ן ש| שו|אינ|נטל| הי|בעט|ָפּ|ף פ|ײַכ|בער|ן צ|מאָ| שט| לע|גער|ורך|רך |נעם|גרו|פֿן|לער|װעל|ע מ|ום |שפּ|ך א|יונ|רבע|עפֿ|טעט|ן כ|רעס|ערצ|ז א|עמע|ם א|שטע|כן |רט |י ג|סן |נער|ליט|ט ז|נעמ|ּרא|היו|אַש|ת װ|אומ|ק א|יבע|ֿן |ץ א|פֿי|ײן |ם ט"
  }
}
```

## File: `misc/lang.rs.erb`
```
// NOTE:
//    This file is generated automatically.
//    Edit misc/lang.rs.erb template instead of editing lang.rs file directly.

use std::fmt;
use std::str::FromStr;

use crate::error::ParseError;

/// Represents a language following [ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3) standard.
#[cfg_attr(feature = "enum-map", derive(::enum_map::Enum))]
#[cfg_attr(feature = "arbitrary", derive(::arbitrary::Arbitrary))]
#[cfg_attr(
    feature = "serde",
    derive(::serde::Serialize, ::serde::Deserialize),
    serde(rename_all = "lowercase")
)]
#[derive(PartialEq, Eq, Debug, Hash, Clone, Copy)]
pub enum Lang {
    <% langs.each_with_index do |lang, index| %>
    /// <%= lang.name %> (<%= lang.eng_name %>)
    <%= lang.code.capitalize %> = <%= index %>,
    <% end %>
}

const VALUES: [Lang; <%= langs.size %>] = [
    <% langs.each do |lang| %>
    Lang::<%= lang.code.capitalize %>,
    <% end %>
];


fn lang_from_code<S: Into<String>>(code: S) -> Option<Lang> {
    match code.into().to_lowercase().as_ref() {
        <% langs.each do |lang| %>
        "<%= lang.code %>" => Some(Lang::<%= lang.code.capitalize %>),<% end %>
        _ => None,
    }
}

fn lang_to_code(lang: Lang) -> &'static str {
    match lang {
        <% langs.each do |lang| %>
        Lang::<%= lang.code.capitalize %> => "<%= lang.code %>",<% end %>
    }
}

fn lang_to_name(lang: Lang) -> &'static str {
    match lang {
        <% langs.each do |lang| %>
        Lang::<%= lang.code.capitalize %> => "<%= lang.name %>",<% end %>
    }
}

fn lang_to_eng_name(lang: Lang) -> &'static str {
    match lang {
        <% langs.each do |lang| %>
        Lang::<%= lang.code.capitalize %> => "<%= lang.eng_name %>",<% end %>
    }
}

impl Lang {
    /// Get enum by ISO 639-3 code as a string.
    ///
    /// # Example
    /// ```
    /// use whatlang::Lang;
    /// assert_eq!(Lang::from_code("ukr"), Some(Lang::Ukr));
    /// ```
    pub fn from_code<S: Into<String>>(code: S) -> Option<Lang> {
        lang_from_code(code)
    }

    /// Convert enum into ISO 639-3 code as a string.
    ///
    /// # Example
    /// ```
    /// use whatlang::Lang;
    /// assert_eq!(Lang::Ukr.code(), "ukr");
    /// ```
    pub fn code(&self) -> &'static str {
        lang_to_code(*self)
    }

    /// Get a language name in the language itself.
    ///
    /// # Example
    /// ```
    /// use whatlang::Lang;
    /// assert_eq!(Lang::Ukr.name(), "Українська");
    /// ```
    pub fn name(self) -> &'static str {
        lang_to_name(self)
    }

    /// Get a human readable name of the language in English.
    ///
    /// # Example
    /// ```
    /// use whatlang::Lang;
    /// assert_eq!(Lang::Deu.eng_name(), "German");
    /// ```
    pub fn eng_name(self) -> &'static str {
        lang_to_eng_name(self)
    }

    /// Get all existing languages.
    ///
    /// # Example
    /// ```
    /// use whatlang::Lang;
    /// for lang in Lang::all() {
    ///     println!("{}", lang);
    /// }
    /// ```
    pub fn all() -> &'static [Lang] {
        &VALUES
    }
}

impl fmt::Display for Lang {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.name())
    }
}

impl FromStr for Lang {
    type Err = ParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Lang::from_code(s).ok_or_else(|| ParseError::Lang(s.to_string()))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_from_code() {
        assert_eq!(Lang::from_code("rus".to_string()), Some(Lang::Rus));
        assert_eq!(Lang::from_code("ukr"), Some(Lang::Ukr));
        assert_eq!(Lang::from_code("ENG"), Some(Lang::Eng));
        assert_eq!(Lang::from_code("oops"), None);
    }

    #[test]
    fn test_code() {
        assert_eq!(Lang::Spa.code(), "spa");
    }

    #[test]
    fn test_name() {
        assert_eq!(Lang::Rus.name(), "Русский");
        assert_eq!(Lang::Spa.name(), "Español");
        assert_eq!(Lang::Epo.name(), "Esperanto");
    }

    #[test]
    fn test_eng_name() {
        assert_eq!(Lang::Spa.eng_name(), "Spanish");
        assert_eq!(Lang::Epo.eng_name(), "Esperanto");
        assert_eq!(Lang::Rus.eng_name(), "Russian");
    }

    #[test]
    fn test_all() {
        assert_eq!(Lang::all().len(), <%= langs.size %>);
        let all = Lang::all();
        assert!(all.contains(&Lang::Ukr));
        assert!(all.contains(&Lang::Swe));
    }

    #[test]
    fn test_from_str() {
        for &lang in Lang::all() {
            let s = lang.code();
            assert_eq!(s.parse::<Lang>().unwrap(), lang);
            assert_eq!(s.to_lowercase().parse::<Lang>().unwrap(), lang);
            assert_eq!(s.to_uppercase().parse::<Lang>().unwrap(), lang);
        }

        let result = "xyz".parse::<Lang>();
        assert!(
            matches!(
                result,
                Err(ParseError::Lang(_))
            )
        );
    }

    #[test]
    fn test_lang_display() {
        assert_eq!(Lang::Epo.to_string(), "Esperanto");
        assert_eq!(Lang::Ukr.to_string(), "Українська");
        assert_eq!(Lang::Deu.to_string(), "Deutsch");
        assert_eq!(Lang::Eng.to_string(), "English");
    }

    #[cfg(feature = "serde")]
    #[test]
    fn test_serialize_and_deserialize() {
        let langs = vec![Lang::Epo, Lang::Ukr, Lang::Spa];
        let json_langs = serde_json::to_string(&langs).unwrap();
        assert_eq!(json_langs, r#"["epo","ukr","spa"]"#);
        let parsed_langs: Vec<Lang> = serde_json::from_str(&json_langs).unwrap();
        assert_eq!(parsed_langs, langs);
    }
}
```

## File: `misc/supported_languages.csv`
```
code,eng_name,name,native_speakers
epo,Esperanto,Esperanto,
eng,English,English,
rus,Russian,Русский,
cmn,Mandarin,普通话,
spa,Spanish,Español,
por,Portuguese,Português,
ita,Italian,Italiano,
ben,Bengali,বাংলা,210
fra,French,Français,
deu,German,Deutsch,
ukr,Ukrainian,Українська,
kat,Georgian,ქართული,
ara,Arabic,العربية,
hin,Hindi,हिन्दी,
jpn,Japanese,日本語,
heb,Hebrew,עברית,
yid,Yiddish,ייִדיש,
pol,Polish,Polski,
amh,Amharic,አማርኛ,
jav,Javanese,Basa Jawa,
kor,Korean,한국어,
nob,Bokmal,Bokmål,
dan,Danish,Dansk,
swe,Swedish,Svenska,
fin,Finnish,Suomi,
tur,Turkish,Türkçe,
nld,Dutch,Nederlands,
hun,Hungarian,Magyar,
ces,Czech,Čeština,
ell,Greek,Ελληνικά,
bul,Bulgarian,Български,
bel,Belarusian,Беларуская,
mar,Marathi,मराठी,
kan,Kannada,ಕನ್ನಡ,
ron,Romanian,Română,24
slv,Slovene,Slovenščina,2.5
hrv,Croatian,Hrvatski,7
srp,Serbian,Српски,8.7
mkd,Macedonian,Македонски,2
lit,Lithuanian,Lietuvių,4
lav,Latvian,Latviešu,2
est,Estonian,Eesti,1.1
tam,Tamil,தமிழ்,70
vie,Vietnamese,Tiếng Việt,75
urd,Urdu,اُردُو,66
tha,Thai,ภาษาไทย,56
guj,Gujarati,ગુજરાતી,50
uzb,Uzbek,Oʻzbekcha,27
pan,Punjabi,ਪੰਜਾਬੀ,100
aze,Azerbaijani,Azərbaycanca,26
ind,Indonesian,Bahasa Indonesia,150
tel,Telugu,తెలుగు,85
pes,Persian,فارسی,50
mal,Malayalam,മലയാളം,38
ori,Oriya,ଓଡ଼ିଆ,36
mya,Burmese,မြန်မာစာ,33
nep,Nepali,नेपाली,16
sin,Sinhalese,සිංහල,16,
khm,Khmer,ភាសាខ្មែរ,16,
tuk,Turkmen,Türkmençe,9
aka,Akan,Akan,11
zul,Zulu,IsiZulu,12
sna,Shona,ChiShona,8
afr,Afrikaans,Afrikaans,8
lat,Latin,Lingua Latina,0
slk,Slovak,Slovenčina,5
cat,Catalan,Català,10
tgl,Tagalog,Tagalog,
hye,Armenian,Հայերեն,7
cym,Welsh,Cymraeg,0.5
```

## File: `misc/trigram_profiles.rs.erb`
```
// NOTE:
//    This file is generated automatically.

use crate::Lang;
use crate::trigrams::Trigram;

pub type LangProfile = &'static [Trigram];
pub type LangProfileList = &'static [(Lang, LangProfile)];

<% scripts.each do |script, langs| %>
/// Languages for script <%= script %>
pub static <%= script.upcase %>_LANGS: LangProfileList = &[
    <% langs.each do |lang| %>
        (
            Lang::<%= lang[:code].capitalize %>,
            &[
	        <% lang[:trigrams].each do |t| %>
                  Trigram('<%= t[0] %>','<%= t[1] %>','<%= t[2] %>'),<% end %>
            ]
        ),
    <% end %>
];
<% end %>
```

## File: `misc/update_support_languages.rb`
```ruby
# Updates SUPPORTED_LANGUAGES.md with list of supported languages

require "csv"
require "erb"
require "json"
require "pp"

LIST_FILE = File.expand_path("../supported_languages.csv", __FILE__)
JSON_FILE = File.expand_path("../data.json", __FILE__)
LANG_TEMPLATE_FILE = File.expand_path("../lang.rs.erb", __FILE__)
LANG_OUTPUT = File.expand_path("../../src/lang.rs", __FILE__)

TRIGRAM_PROFILES_TEMPLATE_FILE = File.expand_path("../trigram_profiles.rs.erb", __FILE__)
TRIGRAM_PROFILES_TARGET = File.expand_path("../../src/trigrams/profiles.rs", __FILE__)

TRIGRAM_COUNT = 300

OUTPUT_FILE = File.expand_path("../../SUPPORTED_LANGUAGES.md", __FILE__)

IGNORE_LANGS = {
  # Do not generate cyrillic trigrams for Turkmen and Azerbaijani
  "Cyrillic" => ["tuk", "aze"]
}

class Lang
  attr_reader :code, :eng_name, :name, :native_speakers, :script, :trigrams

  def initialize(code, eng_name, name, script, trigrams, native_speakers = nil)
    @code = code || raise("Missing code")
    @eng_name = eng_name || raise("Missing eng_name")
    @name = name || eng_name || raise("Missing name")
    @native_speakers = native_speakers
  end

  def self.load
    langs = []
    rows = CSV.read(LIST_FILE, headers: true).each
    rows.each do |row|
      if !langs.any? { |l| l.code == row["code"] }
        langs << Lang.new(row["code"], row["eng_name"], row["name"], "", [], row["native_speakers"])
      end
    end

    scripts = {}
    json = JSON.parse(File.read(JSON_FILE))
    json.each do |script, languages|
      if !scripts[script]
        scripts[script] = []
      end
      ignore_langs = IGNORE_LANGS[script] || []
      languages.each do |lang, trigrams|
        next if ignore_langs.include?(lang)

        info = langs.find { |l| l.code == lang }
        if info
          scripts[script] << {
            code: lang,
            script: script,
            trigrams: trigrams.split('|')
          }
        end
      end
    end

    # Filter out scripts with only one language
    scripts.select! {|script, langs| langs.size > 1 }

    return langs, scripts
  end
end

class MarkdownTable
  def initialize(headers)
    @headers = headers
    @rows = []
  end

  def add(row)
    @rows << row
  end

  def to_s
    widths = []
    @headers.each_with_index do |header, i|
      header_size = header.to_s.size
      cell_size = @rows.map { |r| r[i].to_s.size }.max
      widths[i] = [header_size, cell_size].max
    end

    output = "|"
    @headers.each_with_index do |h, i|
      width = widths[i]
      output << " " << h.ljust(width) << " |"
    end
    output << "\n"

    output << "|"
    widths.each do |w|
      output << " " << ("-" * w) << " |"
    end
    output << "\n"

    @rows.each do |row|
      output << "|"
      row.each_with_index do |item, i|
        width = widths[i]
        output << " " << item.ljust(width) << " |"
      end
      output << "\n"
    end

    output
  end
end


langs, scripts = Lang.load

table = MarkdownTable.new(["Language", "ISO 639-3", "Enum"])
langs.each do |lang|
  table.add([lang.eng_name, lang.code, "`Lang::#{lang.code.capitalize}`"])
end
supported_langs_table = File.read(OUTPUT_FILE)
supported_langs_table.gsub!(/\| Language .+\|\n/m, table.to_s)
File.write(OUTPUT_FILE, supported_langs_table)

template = ERB.new(File.read(LANG_TEMPLATE_FILE))
File.open(LANG_OUTPUT, 'w') { |out| out.write(template.result) }

template = ERB.new(File.read(TRIGRAM_PROFILES_TEMPLATE_FILE))
File.open(TRIGRAM_PROFILES_TARGET, 'w') { |out| out.write(template.result) }

`cargo fmt` # Call cargo fmt to clean the generated code

scripts.each do |script, data|
  puts script
  data.each do |lang_data|
    lang = langs.find { |l| lang_data[:code] == l.code }
    puts "[ ] #{lang.code} (#{lang.eng_name})"
  end
  puts
end
```

## File: `misc/alphabets/calculate_scores.rs.erb`
```
use std::cmp::Reverse;

use super::Outcome;
use crate::utils::is_stop_char;
use crate::core::{LowercaseText, FilterList};
use crate::{Lang, Script};

<% alphabets.each do |code, alphabet| -%>
const <%= code.upcase %>: &str = "<%= alphabet %>";
<% end %>

fn get_lang_chars(lang: Lang) -> Vec<char> {
    let alphabet = match lang {
        <% alphabets.keys.each do |code| -%>
        Lang::<%= code.capitalize %> => <%= code.upcase %>,
        <% end %>
        _ => panic!(format!("No alphabet for {}", lang)),
    };
    alphabet.chars().collect()
}

pub fn alphabet_calculate_scores(text: &str) -> Outcome {
    let text = text.to_lowercase();

    let mut raw_scores = vec![
        <% alphabets.keys.each do |code| -%>
        (Lang::<%= code.capitalize %>, 0i32),
        <% end %>
    ];

    let max_raw_score = text.chars().filter(|&ch| !is_stop_char(ch)).count();

    for (lang, score) in &mut raw_scores {
        let alphabet = get_lang_chars(*lang);

        for ch in text.chars() {
            if is_stop_char(ch) {
                continue;
            };
            if alphabet.contains(&ch) {
                *score += 1;
            } else {
                *score -= 1;
            }
        }
    }

    raw_scores.sort_unstable_by_key(|(_, score)| Reverse(*score));

    let raw_scores: Vec<(Lang, usize)> = raw_scores
        .into_iter()
        .map(|(l, s)| {
            let score = if s < 0 { 0usize } else { s as usize };
            (l, score)
        })
        .collect();

    let mut normalized_scores = vec![];

    for &(lang, raw_score) in &raw_scores {
        let normalized_score = raw_score as f64 / max_raw_score as f64;
        normalized_scores.push((lang, normalized_score));
    }

    Outcome {
        max_raw_score,
        raw_scores,
        normalized_scores,
    }
}
```

## File: `misc/alphabets/cyrillic.yml`
```yaml
bul: абвгдежзийклмнопрстуфхцчшщъьюя
rus: абвгдежзийклмнопрстуфхцчшщъыьэюяё
ukr: абвгдежзийклмнопрстуфхцчшщьюяєіїґ
bel: абвгдежзйклмнопрстуфхцчшыьэюяёіў
srp: абвгдежзиклмнопрстуфхцчшђјљњћџ
mkd: абвгдежзиклмнопрстуфхцчшѓѕјљњќџ
```

## File: `misc/alphabets/gen.rb`
```ruby
require 'erb'
require 'yaml'

template = ERB.new(File.read("calculate_scores.rs.erb"), nil, '-')
alphabets = YAML.load_file("./latin.yml")

pp alphabets
puts puts puts
puts template.result

#File.open(LANG_OUTPUT, 'w') { |out| out.write(template.result) }
```

## File: `misc/alphabets/latin.yml`
```yaml
# See: https://en.wikipedia.org/wiki/Wikipedia:Language_recognition_chart#Characters
afr: abcdefghijklmnopqrstuvwxyzáèéêëíîïóôúû
aka: abdefghiklmnoprstuwyɔɛ
aze: abcdefghijklmnopqrstuvxyzçöüğışə̇
cat: abcdefghijklmnopqrstuvwxyz·àçèéíïòóúü
ces: abcdefghijklmnopqrstuvwxyzáéíóúýčďěňřšťůž
cym: abcdefghijklmnopqrstuvwxyzàáâäèéêëìíîïòóôöùúûüýÿŵŷẁẃẅỳ
dan: abcdefghijklmnopqrstuvwxyzåæø
deu: abcdefghijklmnopqrstuvwxyzßäöü
eng: abcdefghijklmnopqrstuvwxyz
epo: abcdefghijklmnoprstuvzĉĝĥĵŝŭ
est: abcdefghijklmnopqrstuvwxyzäõöü
fin: abcdefghijklmnopqrstuvwxyzäöšž
fra: abcdefghijklmnopqrstuvwxyzàâçèéêëîïôùûüÿœ
hrv: abcdefghijklmnopqrstuvwxyzćčđšž
hun: abcdefghijklmnopqrstuvwxyzáéíóöúüőű
ind: abcdefghijklmnopqrstuvwxyz
ita: abcdefghijklmnopqrstuvwxyzàèéìòù
jav: abcdefghijklmnopqrstuvwxyzèé
lat: abcdefghijklmnopqrstuvwxyz
lav: abcdefghijklmnopqrstuvwxyzāčēģīķļņōŗšūž
lit: abcdefghijklmnopqrstuvwxyząčėęįšūųž
nld: abcdefghijklmnopqrstuvwxyzàèéëïĳ
nob: abcdefghijklmnopqrstuvwxyzåæø
pol: abcdefghijklmnopqrstuvwxyzóąćęłńśźż
por: abcdefghijklmnopqrstuvwxyzàáâãçéêíóôõú
ron: abcdefghijklmnopqrstuvwxyzâîăşţ
slk: abcdefghijklmnopqrstuvwxyzáäéíóôúýčďĺľňŕšťž
slv: abcdefghijklmnopqrstuvwxyzčšž
sna: abcdefghijklmnopqrstuvwxyz
spa: abcdefghijklmnopqrstuvwxyz¡¿áéíñóúü
swe: abcdefghijklmnopqrstuvwxyzäåö
tuk: abdefghijklmnoprstuwyzäçöüýňşž
tur: abcdefghijklmnopqrstuvwxyzçöüğış̇
uzb: abcdefghijklmnopqrstuvxyzʻ
vie: abcdefghijklmnopqrstuvwxyzàáâãèéêìíòóôõùúýăđĩũơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ
zul: abcdefghijklmnopqrstuvwxyz
```

## File: `misc/alphabets/latin_gen.rb`
```ruby
require 'yaml'

def normalize_alphabet(alphabet)
  alphabet.downcase
    .chars
    .uniq
    .reject { |c| c == " " }
    .sort
    .join("")
end

def load_alphabets
  alphabets = {}
  data = YAML.load_file("./raw_latin.yml")

  latin_based = data["latin_based"]
  base = latin_based.delete("base")

  latin_based.each do |code, alphabet|
    alphabet = base + alphabet
    alphabet = normalize_alphabet(alphabet)
    alphabets[code] = alphabet
  end

  data["others"].each do |code, alphabet|
    alphabets[code] = normalize_alphabet(alphabet)
  end

  alphabets.sort_by {|k, _| k }.to_h
end


alphabets = load_alphabets

puts alphabets.to_yaml

```

## File: `misc/alphabets/raw_latin.yml`
```yaml
# https://en.wikipedia.org/wiki/Wikipedia:Language_recognition_chart#Characters
#
# Common Latin alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
#
# Extras:
latin_based:
  base: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  eng: ""
  spa: "ÁÉÍÑÓÚÜáéíñóúü¡¿"
  por: "ÁÉÍÓÚÂÊÔÀãõçáéíóúâêôà"
  ind: ""
  fra: "ÀÂÇÉÈÊËÎÏÔŒÙÛÜŸàâçéèêëîïôœùûüÿ"
  deu: "ÄÖÜäöüß"
  vie: "ĐÀẢÃÁẠĂẰẲẴẮẶÂẦẨẪẤẬÈẺẼÉẸÊỀỂỄẾỆÌỈĨÍỊÒỎÕÓỌÔỒỔỖỐỘƠỜỞỠỚỢÙỦŨÚỤƯỪỬỮỨỰỲỶỸÝỴ đàảãáạăằẳẵắặâầẩẫấậèẻẽéẹêềểễếệìỉĩíịòỏõóọồổỗốơờởỡớợùủũúụưừửữứựỳỷỹýỵ"
  ita: "ÀÉÈÌÒÙàéèìòù"
  tur: "ÇĞİÖŞÜğçıöşü"
  pol: "ąłńóż ćęłńóśźż"
  ron: "ĂÎÂŞŢăîâşţ"
  hrv: "ČŠŽ ĆĐ"
  nld: "àèéëïĳ"
  hun: "ÁÉÍÓÖŐÚÜŰáéíóöőúüű"
  ces: "ČŠŽ ÁĎÉĚŇÓŘŤÚŮÝáďéěňóřťúůý"
  zul: ""
  swe: "ÅÄÖåäö"
  afr: "áêéèëïíîôóúû"
  fin: "ÄÖäöŠšŽž"
  slk: "ČŠŽ ÁÄĎÉÍĽĹŇÓÔŔŤÚÝáäďéíľĺňóôŕťúý"
  dan: "ÆØÅæøå"
  nob: "ÆØÅæøå"
  nno: "ÆØÅæøå"
  cat: "ÀÇÉÈÍÓÒÚÜÏàçéèíóòúüï·"
  lit: "ČŠŽ ĄĘĖĮŲŪąęėįųū"
  slv: "ČŠŽ"
  lav: "ČŠŽ ĀĒĢĪĶĻŅŌŖŪāēģīķļņōŗū"
  est: "ÄÖÕÜäöõü"
  lat: ""
  tgl: "áéíñóú"
  cym: "ÂÊÎÔÛŴŶÁÉÍÏâêîôûŵŷáéíïÓÚẂÝÀÈÌÒÙẀỲÄËÖÜẄŸóúẃýàèìòùẁỳäëöüẅÿ"
others:
  tuk: "ABÇDEÄFGHIJŽKLMNŇOÖPRSŞTUÜWYÝZ"
  epo: "ABCĈDEFGĜHĤIJĴKLMNOPRSŜTUŬVZ"
  sna: "abcdefghijklmnopqrstuvwxyz"
  aka: "AaBbDdEeƐɛFfGgHhIiKkLlMmNnOoƆɔPpRrSsTtUuWwYy"

  # https://en.wikipedia.org/wiki/Javanese_orthography
  jav: "AaJjSsBbKkTtCcLlUuDdMmVvEeNnWwFfOoXxGgPpYyHhQqZzIiRr é è"

  # https://en.wikipedia.org/wiki/Yoruba_alphabet
  yor: "abdefghijklmnoprstuwyɔɛṣẹọ inaoelrtbsíkuàgdwjmìpáyóọèòféúẹh̀́cùṣńvz"

  # https://en.wikipedia.org/wiki/Uzbek_alphabet
  uzb: "abcdefghijklmnopqrstuvxyzʻ"

  # https://en.wikipedia.org/wiki/Azerbaijani_alphabet
  aze: "abcdefghijklmnopqrstuvxyzçöüğışə̇"

  # https://en.wikipedia.org/wiki/Filipino_alphabet
  # tgl: "abcdefghijklmnñngopqrstuvwxyz éáíóú"
```

## File: `misc/logo/README.md`
```markdown
The logo is designed by Vishesh Chopra:
* Twitter: https://twitter.com/Vylkrom
* Github: https://github.com/KarmicKonquest
```

## File: `src/dev.rs`
```rust
//! This mod exposes some internal API.
//! It exists only to enable tuning of the library with extra supporting tools (e.g. benchmarks).
//! Developers are advised against relying on API.
//!
pub use crate::alphabets::{RawOutcome as RawAlphabetsInfo, raw_detect as alphabets_raw_detect};
pub use crate::combined::{RawOutcome as RawCombinedInfo, raw_detect as combined_raw_detect};
pub use crate::core::{Detector, Info, Method, Options, detect, detect_lang, detect_with_options};
pub use crate::lang::Lang;
pub use crate::scripts::{RawScriptInfo, Script, detect_script, raw_detect_script};
pub use crate::trigrams::{RawOutcome as RawTrigramsInfo, raw_detect as trigrams_raw_detect};

pub use crate::alphabets::cyrillic::alphabet_calculate_scores as alphabet_cyrillic_calculate_scores;
pub use crate::alphabets::latin::alphabet_calculate_scores as alphabet_latin_calculate_scores;
pub use crate::core::{FilterList, LowercaseText};

// private imports
use crate::core::Query;
use crate::core::detect::detect_lang_base_on_mandarin_script;
use crate::scripts::grouping::ScriptLangGroup;

#[derive(Debug)]
pub struct RawInfo {
    pub script_info: RawScriptInfo,
    pub lang_info: Option<RawLangInfo>,
}

#[derive(Debug)]
pub enum RawLangInfo {
    OneScript(Lang),
    MultiScript(RawCombinedInfo),
    Mandarin(Lang),
}

pub fn raw_detect(text: &str) -> RawInfo {
    let script_info = raw_detect_script(text);

    let query = Query {
        text,
        filter_list: &FilterList::default(),
        method: Method::Combined,
    };

    let lang_info = script_info
        .main_script()
        .map(|script| match script.to_lang_group() {
            ScriptLangGroup::One(lang) => RawLangInfo::OneScript(lang),
            ScriptLangGroup::Multi(multi_lang_script) => {
                let iquery = query.to_internal(multi_lang_script);
                let combined = combined_raw_detect(&iquery);
                RawLangInfo::MultiScript(combined)
            }
            ScriptLangGroup::Mandarin => {
                let lang = detect_lang_base_on_mandarin_script(&query, &script_info).lang();
                RawLangInfo::Mandarin(lang)
            }
        });

    RawInfo {
        script_info,
        lang_info,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_raw_detect() {
        let zapovit = r#"
            Як умру, то поховайте
            Мене на могилі,
            Серед степу широкого,
            На Вкраїні милій,
            Щоб лани широкополі,
            І Дніпро, і кручі
            Було видно, було чути,
            Як реве ревучий.
        "#;
        let info = raw_detect(&zapovit);
        assert_eq!(info.script_info.counters[0].0, Script::Cyrillic);
    }
}
```

## File: `src/error.rs`
```rust
use std::error::Error as StdError;
use std::fmt::{self, Display};

#[derive(Debug)]
pub enum ParseError {
    Script(String),
    Lang(String),
    Method(String),
}

impl Display for ParseError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            ParseError::Script(val) => {
                write!(f, "Cannot parse str into whatlang::Script: {:?}", val)
            }
            ParseError::Lang(val) => {
                write!(f, "Cannot parse str into whatlang::Lang: {:?}", val)
            }
            ParseError::Method(val) => {
                write!(f, "Cannot parse str into whatlang::Method: {:?}", val)
            }
        }
    }
}

impl StdError for ParseError {}
```

## File: `src/lang.rs`
```rust
// NOTE:
//    This file is generated automatically.
//    Edit misc/lang.rs.erb template instead of editing lang.rs file directly.

use std::fmt;
use std::str::FromStr;

use crate::error::ParseError;

/// Represents a language following [ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3) standard.
#[cfg_attr(feature = "enum-map", derive(::enum_map::Enum))]
#[cfg_attr(feature = "arbitrary", derive(::arbitrary::Arbitrary))]
#[cfg_attr(
    feature = "serde",
    derive(::serde::Serialize, ::serde::Deserialize),
    serde(rename_all = "lowercase")
)]
#[derive(PartialEq, Eq, Debug, Hash, Clone, Copy)]
pub enum Lang {
    /// Esperanto (Esperanto)
    Epo = 0,

    /// English (English)
    Eng = 1,

    /// Русский (Russian)
    Rus = 2,

    /// 普通话 (Mandarin)
    Cmn = 3,

    /// Español (Spanish)
    Spa = 4,

    /// Português (Portuguese)
    Por = 5,

    /// Italiano (Italian)
    Ita = 6,

    /// বাংলা (Bengali)
    Ben = 7,

    /// Français (French)
    Fra = 8,

    /// Deutsch (German)
    Deu = 9,

    /// Українська (Ukrainian)
    Ukr = 10,

    /// ქართული (Georgian)
    Kat = 11,

    /// العربية (Arabic)
    Ara = 12,

    /// हिन्दी (Hindi)
    Hin = 13,

    /// 日本語 (Japanese)
    Jpn = 14,

    /// עברית (Hebrew)
    Heb = 15,

    /// ייִדיש (Yiddish)
    Yid = 16,

    /// Polski (Polish)
    Pol = 17,

    /// አማርኛ (Amharic)
    Amh = 18,

    /// Basa Jawa (Javanese)
    Jav = 19,

    /// 한국어 (Korean)
    Kor = 20,

    /// Bokmål (Bokmal)
    Nob = 21,

    /// Dansk (Danish)
    Dan = 22,

    /// Svenska (Swedish)
    Swe = 23,

    /// Suomi (Finnish)
    Fin = 24,

    /// Türkçe (Turkish)
    Tur = 25,

    /// Nederlands (Dutch)
    Nld = 26,

    /// Magyar (Hungarian)
    Hun = 27,

    /// Čeština (Czech)
    Ces = 28,

    /// Ελληνικά (Greek)
    Ell = 29,

    /// Български (Bulgarian)
    Bul = 30,

    /// Беларуская (Belarusian)
    Bel = 31,

    /// मराठी (Marathi)
    Mar = 32,

    /// ಕನ್ನಡ (Kannada)
    Kan = 33,

    /// Română (Romanian)
    Ron = 34,

    /// Slovenščina (Slovene)
    Slv = 35,

    /// Hrvatski (Croatian)
    Hrv = 36,

    /// Српски (Serbian)
    Srp = 37,

    /// Македонски (Macedonian)
    Mkd = 38,

    /// Lietuvių (Lithuanian)
    Lit = 39,

    /// Latviešu (Latvian)
    Lav = 40,

    /// Eesti (Estonian)
    Est = 41,

    /// தமிழ் (Tamil)
    Tam = 42,

    /// Tiếng Việt (Vietnamese)
    Vie = 43,

    /// اُردُو (Urdu)
    Urd = 44,

    /// ภาษาไทย (Thai)
    Tha = 45,

    /// ગુજરાતી (Gujarati)
    Guj = 46,

    /// Oʻzbekcha (Uzbek)
    Uzb = 47,

    /// ਪੰਜਾਬੀ (Punjabi)
    Pan = 48,

    /// Azərbaycanca (Azerbaijani)
    Aze = 49,

    /// Bahasa Indonesia (Indonesian)
    Ind = 50,

    /// తెలుగు (Telugu)
    Tel = 51,

    /// فارسی (Persian)
    Pes = 52,

    /// മലയാളം (Malayalam)
    Mal = 53,

    /// ଓଡ଼ିଆ (Oriya)
    Ori = 54,

    /// မြန်မာစာ (Burmese)
    Mya = 55,

    /// नेपाली (Nepali)
    Nep = 56,

    /// සිංහල (Sinhalese)
    Sin = 57,

    /// ភាសាខ្មែរ (Khmer)
    Khm = 58,

    /// Türkmençe (Turkmen)
    Tuk = 59,

    /// Akan (Akan)
    Aka = 60,

    /// IsiZulu (Zulu)
    Zul = 61,

    /// ChiShona (Shona)
    Sna = 62,

    /// Afrikaans (Afrikaans)
    Afr = 63,

    /// Lingua Latina (Latin)
    Lat = 64,

    /// Slovenčina (Slovak)
    Slk = 65,

    /// Català (Catalan)
    Cat = 66,

    /// Tagalog (Tagalog)
    Tgl = 67,

    /// Հայերեն (Armenian)
    Hye = 68,

    /// Cymraeg (Welsh)
    Cym = 69,
}

const VALUES: [Lang; 70] = [
    Lang::Epo,
    Lang::Eng,
    Lang::Rus,
    Lang::Cmn,
    Lang::Spa,
    Lang::Por,
    Lang::Ita,
    Lang::Ben,
    Lang::Fra,
    Lang::Deu,
    Lang::Ukr,
    Lang::Kat,
    Lang::Ara,
    Lang::Hin,
    Lang::Jpn,
    Lang::Heb,
    Lang::Yid,
    Lang::Pol,
    Lang::Amh,
    Lang::Jav,
    Lang::Kor,
    Lang::Nob,
    Lang::Dan,
    Lang::Swe,
    Lang::Fin,
    Lang::Tur,
    Lang::Nld,
    Lang::Hun,
    Lang::Ces,
    Lang::Ell,
    Lang::Bul,
    Lang::Bel,
    Lang::Mar,
    Lang::Kan,
    Lang::Ron,
    Lang::Slv,
    Lang::Hrv,
    Lang::Srp,
    Lang::Mkd,
    Lang::Lit,
    Lang::Lav,
    Lang::Est,
    Lang::Tam,
    Lang::Vie,
    Lang::Urd,
    Lang::Tha,
    Lang::Guj,
    Lang::Uzb,
    Lang::Pan,
    Lang::Aze,
    Lang::Ind,
    Lang::Tel,
    Lang::Pes,
    Lang::Mal,
    Lang::Ori,
    Lang::Mya,
    Lang::Nep,
    Lang::Sin,
    Lang::Khm,
    Lang::Tuk,
    Lang::Aka,
    Lang::Zul,
    Lang::Sna,
    Lang::Afr,
    Lang::Lat,
    Lang::Slk,
    Lang::Cat,
    Lang::Tgl,
    Lang::Hye,
    Lang::Cym,
];

fn lang_from_code<S: Into<String>>(code: S) -> Option<Lang> {
    match code.into().to_lowercase().as_ref() {
        "epo" => Some(Lang::Epo),
        "eng" => Some(Lang::Eng),
        "rus" => Some(Lang::Rus),
        "cmn" => Some(Lang::Cmn),
        "spa" => Some(Lang::Spa),
        "por" => Some(Lang::Por),
        "ita" => Some(Lang::Ita),
        "ben" => Some(Lang::Ben),
        "fra" => Some(Lang::Fra),
        "deu" => Some(Lang::Deu),
        "ukr" => Some(Lang::Ukr),
        "kat" => Some(Lang::Kat),
        "ara" => Some(Lang::Ara),
        "hin" => Some(Lang::Hin),
        "jpn" => Some(Lang::Jpn),
        "heb" => Some(Lang::Heb),
        "yid" => Some(Lang::Yid),
        "pol" => Some(Lang::Pol),
        "amh" => Some(Lang::Amh),
        "jav" => Some(Lang::Jav),
        "kor" => Some(Lang::Kor),
        "nob" => Some(Lang::Nob),
        "dan" => Some(Lang::Dan),
        "swe" => Some(Lang::Swe),
        "fin" => Some(Lang::Fin),
        "tur" => Some(Lang::Tur),
        "nld" => Some(Lang::Nld),
        "hun" => Some(Lang::Hun),
        "ces" => Some(Lang::Ces),
        "ell" => Some(Lang::Ell),
        "bul" => Some(Lang::Bul),
        "bel" => Some(Lang::Bel),
        "mar" => Some(Lang::Mar),
        "kan" => Some(Lang::Kan),
        "ron" => Some(Lang::Ron),
        "slv" => Some(Lang::Slv),
        "hrv" => Some(Lang::Hrv),
        "srp" => Some(Lang::Srp),
        "mkd" => Some(Lang::Mkd),
        "lit" => Some(Lang::Lit),
        "lav" => Some(Lang::Lav),
        "est" => Some(Lang::Est),
        "tam" => Some(Lang::Tam),
        "vie" => Some(Lang::Vie),
        "urd" => Some(Lang::Urd),
        "tha" => Some(Lang::Tha),
        "guj" => Some(Lang::Guj),
        "uzb" => Some(Lang::Uzb),
        "pan" => Some(Lang::Pan),
        "aze" => Some(Lang::Aze),
        "ind" => Some(Lang::Ind),
        "tel" => Some(Lang::Tel),
        "pes" => Some(Lang::Pes),
        "mal" => Some(Lang::Mal),
        "ori" => Some(Lang::Ori),
        "mya" => Some(Lang::Mya),
        "nep" => Some(Lang::Nep),
        "sin" => Some(Lang::Sin),
        "khm" => Some(Lang::Khm),
        "tuk" => Some(Lang::Tuk),
        "aka" => Some(Lang::Aka),
        "zul" => Some(Lang::Zul),
        "sna" => Some(Lang::Sna),
        "afr" => Some(Lang::Afr),
        "lat" => Some(Lang::Lat),
        "slk" => Some(Lang::Slk),
        "cat" => Some(Lang::Cat),
        "tgl" => Some(Lang::Tgl),
        "hye" => Some(Lang::Hye),
        "cym" => Some(Lang::Cym),
        _ => None,
    }
}

fn lang_to_code(lang: Lang) -> &'static str {
    match lang {
        Lang::Epo => "epo",
        Lang::Eng => "eng",
        Lang::Rus => "rus",
        Lang::Cmn => "cmn",
        Lang::Spa => "spa",
        Lang::Por => "por",
        Lang::Ita => "ita",
        Lang::Ben => "ben",
        Lang::Fra => "fra",
        Lang::Deu => "deu",
        Lang::Ukr => "ukr",
        Lang::Kat => "kat",
        Lang::Ara => "ara",
        Lang::Hin => "hin",
        Lang::Jpn => "jpn",
        Lang::Heb => "heb",
        Lang::Yid => "yid",
        Lang::Pol => "pol",
        Lang::Amh => "amh",
        Lang::Jav => "jav",
        Lang::Kor => "kor",
        Lang::Nob => "nob",
        Lang::Dan => "dan",
        Lang::Swe => "swe",
        Lang::Fin => "fin",
        Lang::Tur => "tur",
        Lang::Nld => "nld",
        Lang::Hun => "hun",
        Lang::Ces => "ces",
        Lang::Ell => "ell",
        Lang::Bul => "bul",
        Lang::Bel => "bel",
        Lang::Mar => "mar",
        Lang::Kan => "kan",
        Lang::Ron => "ron",
        Lang::Slv => "slv",
        Lang::Hrv => "hrv",
        Lang::Srp => "srp",
        Lang::Mkd => "mkd",
        Lang::Lit => "lit",
        Lang::Lav => "lav",
        Lang::Est => "est",
        Lang::Tam => "tam",
        Lang::Vie => "vie",
        Lang::Urd => "urd",
        Lang::Tha => "tha",
        Lang::Guj => "guj",
        Lang::Uzb => "uzb",
        Lang::Pan => "pan",
        Lang::Aze => "aze",
        Lang::Ind => "ind",
        Lang::Tel => "tel",
        Lang::Pes => "pes",
        Lang::Mal => "mal",
        Lang::Ori => "ori",
        Lang::Mya => "mya",
        Lang::Nep => "nep",
        Lang::Sin => "sin",
        Lang::Khm => "khm",
        Lang::Tuk => "tuk",
        Lang::Aka => "aka",
        Lang::Zul => "zul",
        Lang::Sna => "sna",
        Lang::Afr => "afr",
        Lang::Lat => "lat",
        Lang::Slk => "slk",
        Lang::Cat => "cat",
        Lang::Tgl => "tgl",
        Lang::Hye => "hye",
        Lang::Cym => "cym",
    }
}

fn lang_to_name(lang: Lang) -> &'static str {
    match lang {
        Lang::Epo => "Esperanto",
        Lang::Eng => "English",
        Lang::Rus => "Русский",
        Lang::Cmn => "普通话",
        Lang::Spa => "Español",
        Lang::Por => "Português",
        Lang::Ita => "Italiano",
        Lang::Ben => "বাংলা",
        Lang::Fra => "Français",
        Lang::Deu => "Deutsch",
        Lang::Ukr => "Українська",
        Lang::Kat => "ქართული",
        Lang::Ara => "العربية",
        Lang::Hin => "हिन्दी",
        Lang::Jpn => "日本語",
        Lang::Heb => "עברית",
        Lang::Yid => "ייִדיש",
        Lang::Pol => "Polski",
        Lang::Amh => "አማርኛ",
        Lang::Jav => "Basa Jawa",
        Lang::Kor => "한국어",
        Lang::Nob => "Bokmål",
        Lang::Dan => "Dansk",
        Lang::Swe => "Svenska",
        Lang::Fin => "Suomi",
        Lang::Tur => "Türkçe",
        Lang::Nld => "Nederlands",
        Lang::Hun => "Magyar",
        Lang::Ces => "Čeština",
        Lang::Ell => "Ελληνικά",
        Lang::Bul => "Български",
        Lang::Bel => "Беларуская",
        Lang::Mar => "मराठी",
        Lang::Kan => "ಕನ್ನಡ",
        Lang::Ron => "Română",
        Lang::Slv => "Slovenščina",
        Lang::Hrv => "Hrvatski",
        Lang::Srp => "Српски",
        Lang::Mkd => "Македонски",
        Lang::Lit => "Lietuvių",
        Lang::Lav => "Latviešu",
        Lang::Est => "Eesti",
        Lang::Tam => "தமிழ்",
        Lang::Vie => "Tiếng Việt",
        Lang::Urd => "اُردُو",
        Lang::Tha => "ภาษาไทย",
        Lang::Guj => "ગુજરાતી",
        Lang::Uzb => "Oʻzbekcha",
        Lang::Pan => "ਪੰਜਾਬੀ",
        Lang::Aze => "Azərbaycanca",
        Lang::Ind => "Bahasa Indonesia",
        Lang::Tel => "తెలుగు",
        Lang::Pes => "فارسی",
        Lang::Mal => "മലയാളം",
        Lang::Ori => "ଓଡ଼ିଆ",
        Lang::Mya => "မြန်မာစာ",
        Lang::Nep => "नेपाली",
        Lang::Sin => "සිංහල",
        Lang::Khm => "ភាសាខ្មែរ",
        Lang::Tuk => "Türkmençe",
        Lang::Aka => "Akan",
        Lang::Zul => "IsiZulu",
        Lang::Sna => "ChiShona",
        Lang::Afr => "Afrikaans",
        Lang::Lat => "Lingua Latina",
        Lang::Slk => "Slovenčina",
        Lang::Cat => "Català",
        Lang::Tgl => "Tagalog",
        Lang::Hye => "Հայերեն",
        Lang::Cym => "Cymraeg",
    }
}

fn lang_to_eng_name(lang: Lang) -> &'static str {
    match lang {
        Lang::Epo => "Esperanto",
        Lang::Eng => "English",
        Lang::Rus => "Russian",
        Lang::Cmn => "Mandarin",
        Lang::Spa => "Spanish",
        Lang::Por => "Portuguese",
        Lang::Ita => "Italian",
        Lang::Ben => "Bengali",
        Lang::Fra => "French",
        Lang::Deu => "German",
        Lang::Ukr => "Ukrainian",
        Lang::Kat => "Georgian",
        Lang::Ara => "Arabic",
        Lang::Hin => "Hindi",
        Lang::Jpn => "Japanese",
        Lang::Heb => "Hebrew",
        Lang::Yid => "Yiddish",
        Lang::Pol => "Polish",
        Lang::Amh => "Amharic",
        Lang::Jav => "Javanese",
        Lang::Kor => "Korean",
        Lang::Nob => "Bokmal",
        Lang::Dan => "Danish",
        Lang::Swe => "Swedish",
        Lang::Fin => "Finnish",
        Lang::Tur => "Turkish",
        Lang::Nld => "Dutch",
        Lang::Hun => "Hungarian",
        Lang::Ces => "Czech",
        Lang::Ell => "Greek",
        Lang::Bul => "Bulgarian",
        Lang::Bel => "Belarusian",
        Lang::Mar => "Marathi",
        Lang::Kan => "Kannada",
        Lang::Ron => "Romanian",
        Lang::Slv => "Slovene",
        Lang::Hrv => "Croatian",
        Lang::Srp => "Serbian",
        Lang::Mkd => "Macedonian",
        Lang::Lit => "Lithuanian",
        Lang::Lav => "Latvian",
        Lang::Est => "Estonian",
        Lang::Tam => "Tamil",
        Lang::Vie => "Vietnamese",
        Lang::Urd => "Urdu",
        Lang::Tha => "Thai",
        Lang::Guj => "Gujarati",
        Lang::Uzb => "Uzbek",
        Lang::Pan => "Punjabi",
        Lang::Aze => "Azerbaijani",
        Lang::Ind => "Indonesian",
        Lang::Tel => "Telugu",
        Lang::Pes => "Persian",
        Lang::Mal => "Malayalam",
        Lang::Ori => "Oriya",
        Lang::Mya => "Burmese",
        Lang::Nep => "Nepali",
        Lang::Sin => "Sinhalese",
        Lang::Khm => "Khmer",
        Lang::Tuk => "Turkmen",
        Lang::Aka => "Akan",
        Lang::Zul => "Zulu",
        Lang::Sna => "Shona",
        Lang::Afr => "Afrikaans",
        Lang::Lat => "Latin",
        Lang::Slk => "Slovak",
        Lang::Cat => "Catalan",
        Lang::Tgl => "Tagalog",
        Lang::Hye => "Armenian",
        Lang::Cym => "Welsh",
    }
}

impl Lang {
    /// Get enum by ISO 639-3 code as a string.
    ///
    /// # Example
    /// ```
    /// use whatlang::Lang;
    /// assert_eq!(Lang::from_code("ukr"), Some(Lang::Ukr));
    /// ```
    pub fn from_code<S: Into<String>>(code: S) -> Option<Lang> {
        lang_from_code(code)
    }

    /// Convert enum into ISO 639-3 code as a string.
    ///
    /// # Example
    /// ```
    /// use whatlang::Lang;
    /// assert_eq!(Lang::Ukr.code(), "ukr");
    /// ```
    pub fn code(&self) -> &'static str {
        lang_to_code(*self)
    }

    /// Get a language name in the language itself.
    ///
    /// # Example
    /// ```
    /// use whatlang::Lang;
    /// assert_eq!(Lang::Ukr.name(), "Українська");
    /// ```
    pub fn name(self) -> &'static str {
        lang_to_name(self)
    }

    /// Get a human readable name of the language in English.
    ///
    /// # Example
    /// ```
    /// use whatlang::Lang;
    /// assert_eq!(Lang::Deu.eng_name(), "German");
    /// ```
    pub fn eng_name(self) -> &'static str {
        lang_to_eng_name(self)
    }

    /// Get all existing languages.
    ///
    /// # Example
    /// ```
    /// use whatlang::Lang;
    /// for lang in Lang::all() {
    ///     println!("{}", lang);
    /// }
    /// ```
    pub fn all() -> &'static [Lang] {
        &VALUES
    }
}

impl fmt::Display for Lang {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.name())
    }
}

impl FromStr for Lang {
    type Err = ParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Lang::from_code(s).ok_or_else(|| ParseError::Lang(s.to_string()))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_from_code() {
        assert_eq!(Lang::from_code("rus".to_string()), Some(Lang::Rus));
        assert_eq!(Lang::from_code("ukr"), Some(Lang::Ukr));
        assert_eq!(Lang::from_code("ENG"), Some(Lang::Eng));
        assert_eq!(Lang::from_code("oops"), None);
    }

    #[test]
    fn test_code() {
        assert_eq!(Lang::Spa.code(), "spa");
    }

    #[test]
    fn test_name() {
        assert_eq!(Lang::Rus.name(), "Русский");
        assert_eq!(Lang::Spa.name(), "Español");
        assert_eq!(Lang::Epo.name(), "Esperanto");
    }

    #[test]
    fn test_eng_name() {
        assert_eq!(Lang::Spa.eng_name(), "Spanish");
        assert_eq!(Lang::Epo.eng_name(), "Esperanto");
        assert_eq!(Lang::Rus.eng_name(), "Russian");
    }

    #[test]
    fn test_all() {
        assert_eq!(Lang::all().len(), 70);
        let all = Lang::all();
        assert!(all.contains(&Lang::Ukr));
        assert!(all.contains(&Lang::Swe));
    }

    #[test]
    fn test_from_str() {
        for &lang in Lang::all() {
            let s = lang.code();
            assert_eq!(s.parse::<Lang>().unwrap(), lang);
            assert_eq!(s.to_lowercase().parse::<Lang>().unwrap(), lang);
            assert_eq!(s.to_uppercase().parse::<Lang>().unwrap(), lang);
        }

        let result = "xyz".parse::<Lang>();
        assert!(matches!(result, Err(ParseError::Lang(_))));
    }

    #[test]
    fn test_lang_display() {
        assert_eq!(Lang::Epo.to_string(), "Esperanto");
        assert_eq!(Lang::Ukr.to_string(), "Українська");
        assert_eq!(Lang::Deu.to_string(), "Deutsch");
        assert_eq!(Lang::Eng.to_string(), "English");
    }

    #[cfg(feature = "serde")]
    #[test]
    fn test_serialize_and_deserialize() {
        let langs = vec![Lang::Epo, Lang::Ukr, Lang::Spa];
        let json_langs = serde_json::to_string(&langs).unwrap();
        assert_eq!(json_langs, r#"["epo","ukr","spa"]"#);
        let parsed_langs: Vec<Lang> = serde_json::from_str(&json_langs).unwrap();
        assert_eq!(parsed_langs, langs);
    }
}
```

## File: `src/lib.rs`
```rust
//! Whatlang is a Rust library to detect(regonize) natural languages.
//! Apart from it, the library also recognizes scripts (writing system).
//! Every language and script are represented by determined list of enums.
//!
//! # Examples
//!
//! Using `detect` function:
//!
//! ```
//! use whatlang::{detect, Lang, Script};
//!
//! let text = "Ĉu vi ne volas eklerni Esperanton? Bonvolu! Estas unu de la plej bonaj aferoj!";
//! let info = detect(text).unwrap();
//! assert_eq!(info.lang(), Lang::Epo);
//! assert_eq!(info.script(), Script::Latin);
//!
//! // Confidence is in the range from 0 to 1.
//! assert_eq!(info.confidence(), 1.0);
//! assert!(info.is_reliable());
//! ```
//!
//! Using `Detector` with specified denylist or allowlist:
//!
//! ```
//! use whatlang::{Detector, Lang};
//!
//! let allowlist = vec![Lang::Eng, Lang::Rus];
//!
//! // You can also create detector using with_denylist function
//! let detector = Detector::with_allowlist(allowlist);
//! let lang = detector.detect_lang("There is no reason not to learn Esperanto.");
//! assert_eq!(lang, Some(Lang::Eng));
//! ```
//!
//! # Features
//!
//! | Feature     | Description                                                                           |
//! |-------------|---------------------------------------------------------------------------------------|
//! | `enum-map`  | `Lang` and `Script` implement `Enum` trait from [enum-map](https://docs.rs/enum-map/) |
//! | `arbitrary` | Support [Arbitrary](https://crates.io/crates/arbitrary)                               |
//! | `serde`     | Implements `Serialize` and `Deserialize` for `Lang` and `Script`                      |
//! | `dev`       | Enables `whatlang::dev` module which provides some internal API.<br/> It exists for profiling purposes and normal users are discouraged to to rely on this API.  |
//!
mod alphabets;
mod combined;
mod core;
mod error;
mod lang;
mod scripts;
mod trigrams;
mod utils;

#[cfg(feature = "dev")]
pub mod dev;

pub use crate::core::{Detector, Info, detect, detect_lang};
pub use crate::lang::Lang;
pub use crate::scripts::{Script, detect_script};
```

## File: `src/utils.rs`
```rust
// Is it space, punctuation or digit?
// Stop character is a character that does not give any value for script
// or language detection.
#[inline]
pub fn is_stop_char(ch: char) -> bool {
    matches!(ch, '\u{0000}'..='\u{0040}' | '\u{005B}'..='\u{0060}' | '\u{007B}'..='\u{007E}')
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_top_char() {
        // stop chars
        assert!(is_stop_char(' '));
        assert!(is_stop_char(','));
        assert!(is_stop_char('-'));
        assert!(is_stop_char('-'));
        assert!(is_stop_char('9'));
        assert!(is_stop_char('0'));

        // non-stop chars
        assert!(!is_stop_char('a'));
        assert!(!is_stop_char('z'));
        assert!(!is_stop_char('A')); // latin A
        assert!(!is_stop_char('Z'));
        assert!(!is_stop_char('я'));
        assert!(!is_stop_char('А')); // cyrillic A
    }
}
```

## File: `src/alphabets/common.rs`
```rust
//! It's a hard-core optimized implementation of a relatively simple algorithm.
//! The explanation of the algorithm can be found in the parent module [crate::alphabets].

use super::RawOutcome;
use crate::core::{FilterList, LowercaseText};
use crate::utils::is_stop_char;
use crate::{Lang, Script};
use std::cmp::Reverse;
use std::collections::HashMap;
use std::sync::LazyLock;

/// Inverted map binding a character to a set of languages.
pub fn build_inverted_map(alphabets: &[(Lang, &str)]) -> (Vec<char>, Vec<Vec<Lang>>) {
    let mut map = HashMap::new();

    for (lang, alphabet) in alphabets {
        for c in alphabet.chars() {
            let entry = map.entry(c).or_insert_with(Vec::new);
            entry.push(*lang);
        }
    }

    let mut char_lang: Vec<_> = map.into_iter().collect();

    char_lang.sort_unstable_by_key(|(c, _)| *c);

    let mut chars = Vec::with_capacity(char_lang.len());
    let mut langs = Vec::with_capacity(char_lang.len());
    for (ch, languages) in char_lang {
        chars.push(ch);
        langs.push(languages);
    }

    (chars, langs)
}

pub fn generic_alphabet_calculate_scores(
    script: Script,
    lang_map: &LazyLock<(Vec<char>, Vec<Vec<Lang>>)>,
    text: &LowercaseText,
    filter_list: &FilterList,
) -> RawOutcome {
    let (chars, langs) = &**lang_map;
    let script_langs = script.langs();

    // score of each character.
    let mut char_scores = vec![0; chars.len()];
    let mut max_raw_score = 0;
    // iterate over the text and scores characters.
    for ch in text.chars() {
        if is_stop_char(ch) {
            continue;
        }

        max_raw_score += 1;

        if let Ok(position) = chars.binary_search(&ch) {
            // add 2 and remove max_raw_score at the end,
            // to keep the score interval of -max_raw_score..max_raw_score
            char_scores[position] += 2;
        }
    }

    // score of each lang.
    let mut lang_scores = vec![0; Lang::all().len()];
    let mut common_score: usize = 0;
    // iterate over scored characters to compute language's scores.
    for (position, char_score) in char_scores.into_iter().enumerate() {
        if char_score > 0 {
            let languages = &langs[position];
            // if current character is common to all Languages, increment a common score
            // instead of iterating over all Languages scores.
            if languages.len() == script_langs.len() {
                common_score += char_score;
            } else {
                for &lang in languages {
                    lang_scores[lang as usize] += char_score;
                }
            }
        }
    }

    // remap languages with theirs scores.
    let mut raw_scores: Vec<(Lang, usize)> = script_langs
        .iter()
        .filter(|&&l| filter_list.is_allowed(l))
        .map(|&l| {
            let score = (lang_scores[l as usize] + common_score).saturating_sub(max_raw_score);
            (l, score)
        })
        .collect();

    raw_scores.sort_unstable_by_key(|(_, score)| Reverse(*score));

    let mut normalized_scores = vec![];

    for &(lang, raw_score) in raw_scores.iter() {
        let normalized_score = raw_score as f64 / max_raw_score as f64;
        normalized_scores.push((lang, normalized_score));
    }

    RawOutcome {
        count: max_raw_score,
        raw_scores,
        scores: normalized_scores,
    }
}
```

## File: `src/alphabets/cyrillic.rs`
```rust
use super::RawOutcome;
use super::common::{build_inverted_map, generic_alphabet_calculate_scores};
use crate::core::{FilterList, LowercaseText};
use crate::{Lang, Script};
use std::sync::LazyLock;

const BUL: &str = "абвгдежзийклмнопрстуфхцчшщъьюя";
const RUS: &str = "абвгдежзийклмнопрстуфхцчшщъыьэюяё";
const UKR: &str = "абвгдежзийклмнопрстуфхцчшщьюяєіїґ";
const BEL: &str = "абвгдежзйклмнопрстуфхцчшыьэюяёіў";
const SRP: &str = "абвгдежзиклмнопрстуфхцчшђјљњћџ";
const MKD: &str = "абвгдежзиклмнопрстуфхцчшѓѕјљњќџ";

const CYRILLIC_ALPHABETS: &[(Lang, &str)] = &[
    (Lang::Bul, BUL),
    (Lang::Rus, RUS),
    (Lang::Ukr, UKR),
    (Lang::Bel, BEL),
    (Lang::Srp, SRP),
    (Lang::Mkd, MKD),
];

/// Inverted map binding a character to a set of languages.
static CYRILLIC_ALPHABET_LANG_MAP: LazyLock<(Vec<char>, Vec<Vec<Lang>>)> =
    LazyLock::new(|| build_inverted_map(CYRILLIC_ALPHABETS));

pub fn alphabet_calculate_scores(text: &LowercaseText, filter_list: &FilterList) -> RawOutcome {
    generic_alphabet_calculate_scores(
        Script::Cyrillic,
        &CYRILLIC_ALPHABET_LANG_MAP,
        text,
        filter_list,
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    fn fetch<T: Copy>(lang: &Lang, scores: &[(Lang, T)]) -> T {
        scores.iter().find(|(l, _)| l == lang).unwrap().1
    }

    #[test]
    fn test_when_ukrainian_specific_chars_given() {
        let text = LowercaseText::new("Дуже цікаво");
        let RawOutcome {
            count,
            raw_scores,
            scores,
        } = alphabet_calculate_scores(&text, &FilterList::default());

        assert_eq!(count, 10);

        assert_eq!(fetch(&Lang::Ukr, &raw_scores), 10);
        assert_eq!(fetch(&Lang::Rus, &raw_scores), 8);

        assert_eq!(fetch(&Lang::Ukr, &scores), 1.0);
        assert_eq!(fetch(&Lang::Rus, &scores), 0.8);
    }
}
```

## File: `src/alphabets/detection.rs`
```rust
use super::RawOutcome;
use super::{cyrillic, latin};
use crate::Lang;
use crate::core::{FilterList, Info, InternalQuery, LowercaseText, calculate_confidence};

pub fn detect(iquery: &InternalQuery) -> Option<Info> {
    let raw_outcome = raw_detect(iquery);
    let RawOutcome { count, scores, .. } = raw_outcome;

    let mut normalized_scores_iter = scores.into_iter();
    let opt_lang_score1 = normalized_scores_iter.next();
    let opt_lang_score2 = normalized_scores_iter.next();

    opt_lang_score1.map(|(lang1, score1)| {
        let script = iquery.multi_lang_script.to_script();
        let confidence = if let Some((_, score2)) = opt_lang_score2 {
            calculate_confidence(score1, score2, count)
        } else {
            1.0
        };
        Info::new(script, lang1, confidence)
    })
}

pub fn raw_detect(iquery: &InternalQuery) -> RawOutcome {
    use crate::scripts::grouping::MultiLangScript as MLS;

    let text: &LowercaseText = &iquery.text.lowercase();
    let filter_list: &FilterList = iquery.filter_list;
    match iquery.multi_lang_script {
        MLS::Cyrillic => cyrillic::alphabet_calculate_scores(text, filter_list),
        MLS::Latin => latin::alphabet_calculate_scores(text, filter_list),

        // TODO: implement alphabets for Arabic script
        MLS::Arabic => build_mock(vec![Lang::Ara, Lang::Urd, Lang::Pes], filter_list),

        // TODO: implement alphabets for Devanagari script
        MLS::Devanagari => build_mock(vec![Lang::Hin, Lang::Mar, Lang::Nep], filter_list),

        // TODO: implement alphabets for Hebrew script
        MLS::Hebrew => build_mock(vec![Lang::Heb, Lang::Yid], filter_list),
    }
}

fn build_mock(langs: Vec<Lang>, filter_list: &FilterList) -> RawOutcome {
    let filtered_langs = langs
        .into_iter()
        .filter(|lang| filter_list.is_allowed(*lang));
    let raw_scores = filtered_langs.clone().map(|l| (l, 1)).collect();
    let scores = filtered_langs.map(|l| (l, 1.0)).collect();
    RawOutcome {
        count: 1,
        raw_scores,
        scores,
    }
}
```

## File: `src/alphabets/latin.rs`
```rust
use std::sync::LazyLock;

use super::RawOutcome;
use super::common::{build_inverted_map, generic_alphabet_calculate_scores};
use crate::core::{FilterList, LowercaseText};
use crate::{Lang, Script};

const AFR: &str = "abcdefghijklmnopqrstuvwxyzáèéêëíîïóôúû";
const AKA: &str = "abdefghiklmnoprstuwyɔɛ";
const AZE: &str = "abcdefghijklmnopqrstuvxyzçöüğışə̇";
const CAT: &str = "abcdefghijklmnopqrstuvwxyz·àçèéíïòóúü";
const CES: &str = "abcdefghijklmnopqrstuvwxyzáéíóúýčďěňřšťůž";
const CYM: &str = "abcdefghijklmnopqrstuvwxyzàáâäèéêëìíîïòóôöùúûüýÿŵŷẁẃẅỳ";
const DAN: &str = "abcdefghijklmnopqrstuvwxyzåæø";
const DEU: &str = "abcdefghijklmnopqrstuvwxyzßäöü";
const ENG: &str = "abcdefghijklmnopqrstuvwxyz";
const EPO: &str = "abcdefghijklmnoprstuvzĉĝĥĵŝŭ";
const EST: &str = "abcdefghijklmnopqrstuvwxyzäõöü";
const FIN: &str = "abcdefghijklmnopqrstuvwxyzäöšž";
const FRA: &str = "abcdefghijklmnopqrstuvwxyzàâçèéêëîïôùûüÿœ";
const HRV: &str = "abcdefghijklmnopqrstuvwxyzćčđšž";
const HUN: &str = "abcdefghijklmnopqrstuvwxyzáéíóöúüőű";
const IND: &str = "abcdefghijklmnopqrstuvwxyz";
const ITA: &str = "abcdefghijklmnopqrstuvwxyzàèéìòù";
const JAV: &str = "abcdefghijklmnopqrstuvwxyzèé";
const LAT: &str = "abcdefghijklmnopqrstuvwxyz";
const LAV: &str = "abcdefghijklmnopqrstuvwxyzāčēģīķļņōŗšūž";
const LIT: &str = "abcdefghijklmnopqrstuvwxyząčėęįšūųž";
const NLD: &str = "abcdefghijklmnopqrstuvwxyzàèéëïĳ";
const NOB: &str = "abcdefghijklmnopqrstuvwxyzåæø";
const POL: &str = "abcdefghijklmnopqrstuvwxyzóąćęłńśźż";
const POR: &str = "abcdefghijklmnopqrstuvwxyzàáâãçéêíóôõú";
const RON: &str = "abcdefghijklmnopqrstuvwxyzâîăşţ";
const SLK: &str = "abcdefghijklmnopqrstuvwxyzáäéíóôúýčďĺľňŕšťž";
const SLV: &str = "abcdefghijklmnopqrstuvwxyzčšž";
const SNA: &str = "abcdefghijklmnopqrstuvwxyz";
const SPA: &str = "abcdefghijklmnopqrstuvwxyz¡¿áéíñóúü";
const SWE: &str = "abcdefghijklmnopqrstuvwxyzäåö";
const TGL: &str = "abcdefghijklmnopqrstuvwxyzáéíñóú";
const TUK: &str = "abdefghijklmnoprstuwyzäçöüýňşž";
const TUR: &str = "abcdefghijklmnopqrstuvwxyzçöüğış̇";
const UZB: &str = "abcdefghijklmnopqrstuvxyzʻ";
const VIE: &str =
    "abcdefghijklmnopqrstuvwxyzàáâãèéêìíòóôõùúýăđĩũơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ";
const ZUL: &str = "abcdefghijklmnopqrstuvwxyz";

const LATIN_ALPHABETS: &[(Lang, &str)] = &[
    (Lang::Afr, AFR),
    (Lang::Aka, AKA),
    (Lang::Aze, AZE),
    (Lang::Cat, CAT),
    (Lang::Ces, CES),
    (Lang::Cym, CYM),
    (Lang::Dan, DAN),
    (Lang::Deu, DEU),
    (Lang::Eng, ENG),
    (Lang::Epo, EPO),
    (Lang::Est, EST),
    (Lang::Fin, FIN),
    (Lang::Fra, FRA),
    (Lang::Hrv, HRV),
    (Lang::Hun, HUN),
    (Lang::Ind, IND),
    (Lang::Ita, ITA),
    (Lang::Jav, JAV),
    (Lang::Lat, LAT),
    (Lang::Lav, LAV),
    (Lang::Lit, LIT),
    (Lang::Nld, NLD),
    (Lang::Nob, NOB),
    (Lang::Pol, POL),
    (Lang::Por, POR),
    (Lang::Ron, RON),
    (Lang::Slk, SLK),
    (Lang::Slv, SLV),
    (Lang::Sna, SNA),
    (Lang::Spa, SPA),
    (Lang::Swe, SWE),
    (Lang::Tgl, TGL),
    (Lang::Tuk, TUK),
    (Lang::Tur, TUR),
    (Lang::Uzb, UZB),
    (Lang::Vie, VIE),
    (Lang::Zul, ZUL),
];

/// Inverted map binding a character to a set of languages.
pub static ALPHABET_LANG_MAP: LazyLock<(Vec<char>, Vec<Vec<Lang>>)> =
    LazyLock::new(|| build_inverted_map(LATIN_ALPHABETS));

pub fn alphabet_calculate_scores(text: &LowercaseText, filter_list: &FilterList) -> RawOutcome {
    generic_alphabet_calculate_scores(Script::Latin, &ALPHABET_LANG_MAP, text, filter_list)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::Script;
    use crate::utils::is_stop_char;

    // Old naive implementation, that is not very effective but easy to understand
    fn naive_alphabet_calculate_scores(
        text: &LowercaseText,
        filter_list: &FilterList,
    ) -> RawOutcome {
        let mut raw_scores: Vec<(Lang, i32)> = Script::Latin
            .langs()
            .iter()
            .filter(|&&l| filter_list.is_allowed(l))
            .map(|&l| (l, 0i32))
            .collect();

        let max_raw_score = text.chars().filter(|&ch| !is_stop_char(ch)).count();

        for (lang, score) in &mut raw_scores {
            let alphabet: Vec<char> = LATIN_ALPHABETS
                .iter()
                .find(|(l, _)| l == lang)
                .unwrap()
                .1
                .chars()
                .collect();

            for ch in text.chars() {
                if is_stop_char(ch) {
                    continue;
                };
                if alphabet.contains(&ch) {
                    *score += 1;
                } else {
                    *score -= 1;
                }
            }
        }

        raw_scores.sort_by(|a, b| b.1.cmp(&a.1));

        let raw_scores: Vec<(Lang, usize)> = raw_scores
            .into_iter()
            .map(|(l, s)| {
                let score = if s < 0 { 0usize } else { s as usize };
                (l, score)
            })
            .collect();

        let mut normalized_scores = vec![];

        for &(lang, raw_score) in &raw_scores {
            let normalized_score = raw_score as f64 / max_raw_score as f64;
            normalized_scores.push((lang, normalized_score));
        }

        RawOutcome {
            count: max_raw_score,
            raw_scores,
            scores: normalized_scores,
        }
    }

    #[test]
    fn test_alphabet_calculate_scores_against_harmaja_hauras() {
        let text =
            LowercaseText::new("Ja kulkee kylmä hetki pariimme, Olet hauras kuin jää, Ja kulke");
        let filter = FilterList::All;

        let outcome = alphabet_calculate_scores(&text, &filter);
        assert_eq!(outcome.count, 50);
        assert_eq!(outcome.raw_scores.len(), 37);
        assert_eq!(outcome.scores.len(), 37);

        let raw_scores_for = |lang: Lang| {
            outcome
                .raw_scores
                .iter()
                .find(|(l, _)| *l == lang)
                .unwrap()
                .1
        };
        let scores_for = |lang: Lang| outcome.scores.iter().find(|(l, _)| *l == lang).unwrap().1;

        assert_eq!(raw_scores_for(Lang::Fin), 50);
        assert_eq!(raw_scores_for(Lang::Deu), 50);
        assert_eq!(raw_scores_for(Lang::Epo), 42);

        assert_eq!(scores_for(Lang::Fin), 1.0);
        assert_eq!(scores_for(Lang::Deu), 1.0);
        assert_eq!(scores_for(Lang::Epo), 0.84);
    }

    #[test]
    fn test_works_as_the_old_naive_implementation() {
        let filter = FilterList::All;
        let texts = [
            "Tyrkiske språk eller turkotatariske språk er en språkgruppe bestående av minst 35 språk",
            "René Descartes est un mathématicien, physicien et philosophe français, né le 31 mars 1596 à La Haye-en-Touraine",
            "Die Sonne scheint in das Büro der Grabdenkmalsfirma Heinrich Kroll & Söhne. Es ist April 923, und das Geschäf geht gut.",
        ];

        for text in texts {
            let lowercase_text = LowercaseText::new(text);
            let outcome = alphabet_calculate_scores(&lowercase_text, &filter);
            let naive_outcome = naive_alphabet_calculate_scores(&lowercase_text, &filter);

            // We can just compare outcome against naive_outcome, because ordering maybe different,
            // what is acceptable.
            assert_eq!(
                outcome.count, naive_outcome.count,
                "count failed. Text: {}",
                text
            );
            for (lang, raw_naive_score) in naive_outcome.raw_scores.into_iter() {
                let lookup_raw_score = |lang| {
                    outcome
                        .raw_scores
                        .iter()
                        .find(|(l, _)| *l == lang)
                        .unwrap()
                        .1
                };
                let raw_score = lookup_raw_score(lang);
                assert_eq!(
                    raw_score, raw_naive_score,
                    "raw_score VS raw_naive_score failed. Lang={}, Text: {}",
                    lang, text
                );
            }
            for (lang, naive_score) in naive_outcome.scores.into_iter() {
                let lookup_score =
                    |lang| outcome.scores.iter().find(|(l, _)| *l == lang).unwrap().1;
                let score = lookup_score(lang);
                assert_eq!(
                    score, naive_score,
                    "score VS naive_score failed. Lang={}, Text: {}",
                    lang, text
                );
            }
        }
    }
}
```

## File: `src/alphabets/mod.rs`
```rust
//! Alphabet method is very inaccurate by itself to determine a language, but it supports
//! other methods (trigrams) and allows to improve accuracy on very short texts.
//!
//! It's based on the fact, that some languages may use characters that are not present in others.
//! (e.g. character `ö` is common for German or Finish texts, but not really expected to be
//! seen in English or Spanish).
//!
//! ## Alogirthm
//!
//! * For every single character `c` in a lowecased text:
//!   * If `c` is relevant for the script?
//!     * count += 1
//!     * for every language where `c` is a commonly used character
//!       * raw_lang_score += 1
//! * Normalize scores for every language:
//!   * lang_score = raw_lang_score / count
//!
//! ## Pros and cons
//!
//! This algorithm is very simple and fast, but has also comes with some disadvantages:
//! * Character frequencies are not respected (e.g. letter `O` has 7.16% occurrence rate in English and only
//!   2.24% in German, but according to this alphabet model, both English and German would get +1
//!   score for letter `O`).
//! * It does not work always well: here are some examples:
//!   * `Can you tell me where is Schönheitstraße?` - it's cleary an English sentence with a German
//!     proper name `Schönheitstraße`, but the model gives 34 scores to German and only 30 to
//!     English, because of the letters `ö` and `ß`, which are present in German, but not in English.
//!   * `Façade` - is a valid English word. But English gets panished because of the untypical
//!     character `ç` that was inherited from French.
//!
//! The generic (agnostic to a script) implementation and algorithm can be found in the [common] module.

pub(crate) mod common;
pub(crate) mod cyrillic;
pub(crate) mod detection;
pub(crate) mod latin;

use crate::Lang;
pub use detection::{detect, raw_detect};

#[derive(Debug)]
pub struct RawOutcome {
    pub count: usize,
    #[allow(dead_code)]
    pub raw_scores: Vec<(Lang, usize)>,
    pub scores: Vec<(Lang, f64)>,
}
```

## File: `src/combined/mod.rs`
```rust
use crate::Lang;
use crate::alphabets;
use crate::core::{Info, InternalQuery, calculate_confidence};
use crate::trigrams;

#[derive(Debug)]
pub struct RawOutcome {
    pub scores: Vec<(Lang, f64)>,
    #[allow(dead_code)]
    pub alphabet_raw_outcome: alphabets::RawOutcome,
    pub trigram_raw_outcome: trigrams::RawOutcome,
}

pub fn detect(iquery: &InternalQuery) -> Option<Info> {
    let raw_outcome = raw_detect(iquery);

    let count = raw_outcome.trigram_raw_outcome.trigrams_count;
    let mut normalized_scores_iter = raw_outcome.scores.into_iter();

    let opt_lang_score1 = normalized_scores_iter.next();
    let opt_lang_score2 = normalized_scores_iter.next();

    // TODO: Logic is duplicated in alphabets and trigrams. Consider refactoring
    opt_lang_score1.map(|(lang1, score1)| {
        let script = iquery.multi_lang_script.to_script();
        let confidence = if let Some((_, score2)) = opt_lang_score2 {
            calculate_confidence(score1, score2, count)
        } else {
            1.0
        };
        Info::new(script, lang1, confidence)
    })
}

// TODO: optimize!
pub fn raw_detect(iquery: &InternalQuery) -> RawOutcome {
    let alphabet_raw_outcome: alphabets::RawOutcome = alphabets::raw_detect(iquery);
    let trigram_raw_outcome: trigrams::RawOutcome = trigrams::raw_detect(iquery);

    let alphabet_scores: &Vec<(Lang, f64)> = &alphabet_raw_outcome.scores;
    let trigram_scores: &Vec<(Lang, f64)> = &trigram_raw_outcome.scores;

    let mut all_langs: Vec<Lang> = alphabet_scores.iter().map(|x| x.0).collect();
    for (lang, _) in trigram_scores.iter() {
        if !all_langs.contains(lang) {
            all_langs.push(*lang);
        }
    }

    let count = alphabet_raw_outcome.count;

    let alphabet_weight = calc_alphabet_weight(count);
    let trigram_weight = 1.0 - alphabet_weight;

    let mut scores = Vec::with_capacity(all_langs.len());

    for lang in all_langs {
        let a: f64 = alphabet_scores
            .iter()
            .find(|(l, _)| l == &lang)
            .map(|x| x.1)
            .unwrap_or(0.0);
        let t: f64 = trigram_scores
            .iter()
            .find(|(l, _)| l == &lang)
            .map(|x| x.1)
            .unwrap_or(0.0);

        debug_assert!(a >= 0.0);
        debug_assert!(a <= 1.0);
        debug_assert!(t >= 0.0);
        debug_assert!(t <= 1.0);

        let score = a * alphabet_weight + t * trigram_weight;

        debug_assert!(score >= 0.0);
        debug_assert!(score <= 1.0);

        scores.push((lang, score));
    }

    scores.sort_unstable_by(|a, b| b.1.partial_cmp(&a.1).unwrap_or(std::cmp::Ordering::Less));

    RawOutcome {
        scores,
        alphabet_raw_outcome,
        trigram_raw_outcome,
    }
}

// Function that calculates weight of alphabet score depending on number of characters in the given
// text. The longer text the less significant alphabet weight is (and the more significant is
// trigram weight).
//
// y = -(x/300) + 2/3
// where:
//   x - number of characters
//   y = alphabet weight
//
//
//          alphabet weight
//          ^
//          |
//     2/3 -* (0; 2/3)
//          | \_
//          |   \_
//          |     \_
//          |       \_
//          |         \  (100; 1/3)
//     1/3 -|          *------------
//          |
//          +----------|------------> count
//         0          100
//
fn calc_alphabet_weight(count: usize) -> f64 {
    let weight = -(count as f64 / 300.0) + 2.0 / 3.0;
    weight.clamp(1.0 / 3.0, 2.0 / 3.0)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_calc_alphabet_weight() {
        assert_eq!(calc_alphabet_weight(0), 2.0 / 3.0);
        assert_eq!(calc_alphabet_weight(50), 0.5);
        assert_eq!(calc_alphabet_weight(100), 1.0 / 3.0);
        assert_eq!(calc_alphabet_weight(200), 1.0 / 3.0);
    }
}
```

## File: `src/core/confidence.rs`
```rust
// Calculate confidence that the language with the highest score is the correct one.
// highest_score - within 0.0..1.0
// second_score - within 0.0..1.0
// count - number of chars or trigrams
pub fn calculate_confidence(highest_score: f64, second_score: f64, count: usize) -> f64 {
    if highest_score == 0.0 {
        return 0.0;
    }
    if second_score == 0.0 {
        return highest_score;
    }

    debug_assert!(highest_score <= 1.0);
    debug_assert!(highest_score >= 0.0);
    debug_assert!(second_score <= 1.0);
    debug_assert!(second_score >= 0.0);

    // Hyperbola function. Everything that is above the function has confidence = 1.0
    // If rate is below, confidence is calculated proportionally.
    // Constants are used based on experiments.
    let confident_rate = (3.0 / count as f64) + 0.015;
    let rate = (highest_score - second_score) / second_score;

    if rate > confident_rate {
        1.0
    } else {
        rate / confident_rate
    }
}
```

## File: `src/core/detect.rs`
```rust
use crate::Lang;
use crate::core::{Info, Method, Options, Query};
use crate::scripts::{
    RawScriptInfo, Script,
    grouping::{MultiLangScript, ScriptLangGroup},
    raw_detect_script,
};
use crate::{alphabets, combined, trigrams};

/// Detect only a language by a given text.
///
/// # Example
/// ```
/// use whatlang::{detect_lang, Lang};
/// let lang = detect_lang("There is no reason not to learn Esperanto.").unwrap();
/// assert_eq!(lang, Lang::Eng);
/// ```
pub fn detect_lang(text: &str) -> Option<Lang> {
    detect(text).map(|output| output.lang())
}

/// Detect a language and a script by a given text.
///
/// # Example
/// ```
/// use whatlang::{detect_lang, Lang};
/// let lang = detect_lang("There is no reason not to learn Esperanto.").unwrap();
/// assert_eq!(lang, Lang::Eng);
/// ```
pub fn detect(text: &str) -> Option<Info> {
    let opts = Options::default();
    detect_with_options(text, &opts)
}

pub fn detect_with_options(text: &str, options: &Options) -> Option<Info> {
    let query = Query {
        text,
        filter_list: &options.filter_list,
        method: options.method,
    };
    detect_by_query(&query)
}

pub fn detect_by_query(query: &Query) -> Option<Info> {
    let raw_script_info = raw_detect_script(query.text);
    let script = raw_script_info.main_script()?;

    match script.to_lang_group() {
        ScriptLangGroup::One(lang) => Some(Info::new(script, lang, 1.0)),
        ScriptLangGroup::Multi(multi_lang_script) => {
            detect_by_query_based_on_script(query, multi_lang_script)
        }
        ScriptLangGroup::Mandarin => {
            Some(detect_lang_base_on_mandarin_script(query, &raw_script_info))
        }
    }
}

fn detect_by_query_based_on_script(
    query: &Query,
    multi_lang_script: MultiLangScript,
) -> Option<Info> {
    let iquery = query.to_internal(multi_lang_script);
    match query.method {
        Method::Alphabet => alphabets::detect(&iquery),
        Method::Trigram => trigrams::detect(&iquery),
        Method::Combined => combined::detect(&iquery),
    }
}

// Sometimes Mandarin can be Japanese.
// See https://github.com/greyblake/whatlang-rs/pull/45
pub(crate) fn detect_lang_base_on_mandarin_script(
    query: &Query,
    raw_script_info: &RawScriptInfo,
) -> Info {
    let (lang, confidence) = if query.filter_list.is_allowed(Lang::Cmn) {
        let mandarin_count = raw_script_info.count(Script::Mandarin);
        let katakana_count = raw_script_info.count(Script::Katakana);
        let hiragana_count = raw_script_info.count(Script::Hiragana);
        let japanese_count = katakana_count + hiragana_count;
        let total = mandarin_count + japanese_count;

        let jpn_pct = japanese_count as f64 / total as f64;

        // If at least 5% of characters are Japanese(Katakana or Hiragana) then it's likely to be Japanese language
        // See https://github.com/greyblake/whatlang-rs/issues/88
        if jpn_pct > 0.2 {
            (Lang::Jpn, 1.0)
        } else if jpn_pct > 0.05 {
            (Lang::Jpn, 0.5)
        } else if jpn_pct > 0.02 {
            (Lang::Cmn, 0.5)
        } else {
            (Lang::Cmn, 1.0)
        }
    } else {
        (Lang::Jpn, 1.0)
    };
    Info::new(Script::Mandarin, lang, confidence)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::core::FilterList;
    use crate::scripts::Script;

    #[test]
    fn test_detect_spanish() {
        let text = "Además de todo lo anteriormente dicho, también encontramos...";
        let output = detect(text);
        assert_eq!(output.is_some(), true);

        let info = output.unwrap();
        assert_eq!(info.lang(), Lang::Spa);
        assert_eq!(info.script(), Script::Latin);
    }

    #[test]
    fn test_detect_lang_ukrainian() {
        let text = "Та нічого, все нормально. А в тебе як?";
        assert_eq!(detect_lang(text), Some(Lang::Ukr));
    }

    #[test]
    fn test_detect_with_options_with_filter_list_except() {
        let text = "I am begging pardon";

        // without filter list
        let output = detect_with_options(text, &Options::default());
        assert_eq!(output.is_some(), true);
        let info = output.unwrap();
        assert_eq!(info.lang(), Lang::Tgl);

        // with filter list
        let filter_list = FilterList::deny(vec![
            Lang::Jav,
            Lang::Nld,
            Lang::Uzb,
            Lang::Swe,
            Lang::Nob,
            Lang::Tgl,
            Lang::Cym,
        ]);
        let options = Options::new().set_filter_list(filter_list);
        let output = detect_with_options(text, &options);
        assert_eq!(output.is_some(), true);
        let info = output.unwrap();
        assert_eq!(info.lang(), Lang::Eng);
    }

    // TODO:  see https://github.com/greyblake/whatlang-rs/issues/78
    #[test]
    fn test_detect_with_options_with_filter_list_except_none() {
        {
            // All languages with Hebrew script are filtered out, so result must be None
            let text = "האקדמיה ללשון העברית";
            let filter_list = FilterList::deny(vec![Lang::Heb, Lang::Yid]);
            let options = Options::new().set_filter_list(filter_list);
            let output = detect_with_options(text, &options);
            assert_eq!(output, None);
        }

        {
            // All Cyrillic languages are filtered out
            let text = "Мы хотим видеть дальше, чем окна дома напротив";
            let filter_list = FilterList::deny(Script::Cyrillic.langs().to_owned());
            let options = Options::new().set_filter_list(filter_list);
            let output = detect_with_options(text, &options);
            assert_eq!(output, None);
        }

        {
            // All Latin languages are filtered out
            let text = "Mit dem Wissen wächst der Zweifel";
            let filter_list = FilterList::deny(Script::Latin.langs().to_owned());
            let options = Options::new().set_filter_list(filter_list);
            let output = detect_with_options(text, &options);
            assert_eq!(output, None);
        }
    }

    #[test]
    fn test_detect_with_options_with_filter_list_only() {
        let filter_list = FilterList::allow(vec![Lang::Epo, Lang::Ukr]);
        let options = Options::new().set_filter_list(filter_list);

        let text = "Mi ne scias!";
        let output = detect_with_options(text, &options);
        assert_eq!(output.is_some(), true);
        let info = output.unwrap();
        assert_eq!(info.lang(), Lang::Epo);
    }

    #[test]
    fn test_detect_with_options_with_allowlist_mandarin_japanese() {
        let text = "水";

        let jpn_opts = Options::new().set_filter_list(FilterList::allow(vec![Lang::Jpn]));
        let info = detect_with_options(text, &jpn_opts).unwrap();
        assert_eq!(info.lang(), Lang::Jpn);

        let cmn_opts = Options::new().set_filter_list(FilterList::allow(vec![Lang::Cmn]));
        let info = detect_with_options(text, &cmn_opts).unwrap();
        assert_eq!(info.lang(), Lang::Cmn);
    }

    #[test]
    fn test_detect_with_options_with_blacklist_mandarin_japanese() {
        let text = "水";

        let jpn_opts = Options::new().set_filter_list(FilterList::deny(vec![Lang::Jpn]));
        let info = detect_with_options(text, &jpn_opts).unwrap();
        assert_eq!(info.lang(), Lang::Cmn);

        let cmn_opts = Options::new().set_filter_list(FilterList::deny(vec![Lang::Cmn]));
        let info = detect_with_options(text, &cmn_opts).unwrap();
        assert_eq!(info.lang(), Lang::Jpn);
    }
}
```

## File: `src/core/detector.rs`
```rust
use crate::Lang;
use crate::core;
use crate::core::FilterList;
use crate::core::Info;
use crate::core::Options;
use crate::scripts::{Script, detect_script};

/// Configurable structure that holds detection options and provides functions
/// to detect language and script.
/// # Examples
/// Specifying an allowlist:
///
/// ```
/// use whatlang::{Detector, Lang};
///
/// // Create detector with allowlist
/// let detector = Detector::with_allowlist(vec![Lang::Eng, Lang::Rus]);
/// let lang = detector.detect_lang("That is not Russian");
/// assert_eq!(lang, Some(Lang::Eng));
/// ```
///
/// Specifying a blacklist:
///
/// ```
/// use whatlang::{Detector, Lang};
///
/// let detector = Detector::with_denylist(vec![Lang::Eng, Lang::Ita]);
/// let lang = detector.detect_lang("Jen la trinkejo fermitis, ni iras tra mallumo kaj pluvo.");
/// assert_eq!(lang, Some(Lang::Epo));
/// ```
#[cfg_attr(feature = "arbitrary", derive(::arbitrary::Arbitrary))]
#[derive(Debug, Clone, Default)]
pub struct Detector {
    options: Options,
}

impl Detector {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn with_allowlist(list: Vec<Lang>) -> Self {
        let opts = Options::new().set_filter_list(FilterList::allow(list));
        Self::with_options(opts)
    }

    pub fn with_denylist(list: Vec<Lang>) -> Self {
        let opts = Options::new().set_filter_list(FilterList::deny(list));
        Self::with_options(opts)
    }

    fn with_options(options: Options) -> Self {
        Detector { options }
    }

    pub fn detect(&self, text: &str) -> Option<Info> {
        core::detect_with_options(text, &self.options)
    }

    pub fn detect_lang(&self, text: &str) -> Option<Lang> {
        core::detect_with_options(text, &self.options).map(|info| info.lang())
    }

    pub fn detect_script(&self, text: &str) -> Option<Script> {
        detect_script(text)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_detect_script() {
        // Russian, Cyrillic
        assert_eq!(
            Detector::new().detect_script("Кириллица"),
            Some(Script::Cyrillic)
        );
    }

    #[test]
    fn test_detect_lang() {
        // Esperanto
        let text = "Ĉiuj redaktantoj de Esperanta Vikipedio estas volontuloj. Ili partoprenas en la kunlaborema komunumo, sen estro, kie la anoj kunordigas siajn strebojn kadre de temaj projektoj kaj pluraj diskutejoj. Ili sekvas la bazajn regulojn establitaj de la komunumo, ekzemple kontrolebleco de la informo aŭ la menciindeco de la temo.";
        assert_eq!(Detector::new().detect_lang(text), Some(Lang::Epo));
    }

    #[test]
    fn test_detect() {
        // Esperanto
        let text = "Ĉiuj redaktantoj de Esperanta Vikipedio estas volontuloj. Ili partoprenas en la kunlaborema komunumo, sen estro, kie la anoj kunordigas siajn strebojn kadre de temaj projektoj kaj pluraj diskutejoj. Ili sekvas la bazajn regulojn establitaj de la komunumo, ekzemple kontrolebleco de la informo aŭ la menciindeco de la temo.";
        let output = Detector::new().detect(text);
        assert_eq!(output.is_some(), true);

        let info = output.unwrap();
        assert_eq!(info.lang(), Lang::Epo);
        assert_eq!(info.script(), Script::Latin);
    }
}
```

## File: `src/core/filter_list.rs`
```rust
use crate::Lang;

#[cfg_attr(feature = "arbitrary", derive(::arbitrary::Arbitrary))]
#[derive(Debug, Clone, Default)]
pub enum FilterList {
    #[default]
    All,
    Allow(Vec<Lang>),
    Deny(Vec<Lang>),
}

impl FilterList {
    #[cfg(feature = "dev")]
    pub fn all() -> Self {
        Self::All
    }

    pub fn allow(allowlist: Vec<Lang>) -> Self {
        Self::Allow(allowlist)
    }

    pub fn deny(denylist: Vec<Lang>) -> Self {
        Self::Deny(denylist)
    }

    pub fn is_allowed(&self, lang: Lang) -> bool {
        match self {
            Self::All => true,
            Self::Allow(allowlist) => allowlist.contains(&lang),
            Self::Deny(denylist) => !denylist.contains(&lang),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[cfg(feature = "dev")]
    fn test_all() {
        let list = FilterList::all();
        assert!(list.is_allowed(Lang::Epo));
    }

    #[test]
    fn test_only() {
        let list = FilterList::allow(vec![Lang::Rus, Lang::Ukr]);

        assert!(!list.is_allowed(Lang::Epo));
        assert!(!list.is_allowed(Lang::Eng));

        assert!(list.is_allowed(Lang::Rus));
        assert!(list.is_allowed(Lang::Ukr));
    }

    #[test]
    fn test_except() {
        let list = FilterList::deny(vec![Lang::Rus, Lang::Ukr]);

        assert!(list.is_allowed(Lang::Epo));
        assert!(list.is_allowed(Lang::Eng));

        assert!(!list.is_allowed(Lang::Rus));
        assert!(!list.is_allowed(Lang::Ukr));
    }
}
```

## File: `src/core/info.rs`
```rust
use crate::{Lang, Script};

const RELIABLE_CONFIDENCE_THRESHOLD: f64 = 0.9;

/// Represents a full outcome of language detection.
#[derive(Debug, PartialEq)]
pub struct Info {
    script: Script,
    lang: Lang,
    confidence: f64,
}

impl Info {
    pub fn new(script: Script, lang: Lang, confidence: f64) -> Self {
        Self {
            script,
            lang,
            confidence,
        }
    }

    pub fn lang(&self) -> Lang {
        self.lang
    }

    pub fn script(&self) -> Script {
        self.script
    }

    pub fn confidence(&self) -> f64 {
        self.confidence
    }

    pub fn is_reliable(&self) -> bool {
        self.confidence > RELIABLE_CONFIDENCE_THRESHOLD
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_realiable() {
        let mut info = Info {
            script: Script::Greek,
            lang: Lang::Ell,
            confidence: 0.0,
        };
        assert_eq!(info.is_reliable(), false);

        info.confidence = 1.0;
        assert_eq!(info.is_reliable(), true);
    }
}
```

## File: `src/core/method.rs`
```rust
use crate::error::ParseError;
use std::fmt;
use std::str::FromStr;

#[cfg_attr(feature = "arbitrary", derive(::arbitrary::Arbitrary))]
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
pub enum Method {
    Trigram,
    Alphabet,
    #[default]
    Combined,
}

impl FromStr for Method {
    type Err = ParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s.to_lowercase().trim() {
            "trigram" => Ok(Method::Trigram),
            "alphabet" => Ok(Method::Alphabet),
            "combined" => Ok(Method::Combined),
            _ => Err(ParseError::Method(s.to_string())),
        }
    }
}

impl fmt::Display for Method {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let name = match self {
            Method::Trigram => "Trigram",
            Method::Alphabet => "Alphabet",
            Method::Combined => "Combined",
        };
        write!(f, "{}", name)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_from_str() {
        assert_eq!("trigram".parse::<Method>().unwrap(), Method::Trigram);
        assert_eq!("ALPHABET".parse::<Method>().unwrap(), Method::Alphabet);

        let result = "foobar".parse::<Method>();
        assert!(result.is_err());
    }
}
```

## File: `src/core/mod.rs`
```rust
mod confidence;
pub(crate) mod detect;
mod detector;
mod filter_list;
mod info;
mod method;
mod options;
mod query;
mod text;

pub use confidence::calculate_confidence;
pub use detect::{detect, detect_lang, detect_with_options};
pub use detector::Detector;
pub use filter_list::FilterList;
pub use info::Info;
pub use method::Method;
pub use options::Options;
pub use query::{InternalQuery, Query};
pub use text::{LowercaseText, Text};
```

## File: `src/core/options.rs`
```rust
use super::{FilterList, Method};

#[cfg_attr(feature = "arbitrary", derive(::arbitrary::Arbitrary))]
#[derive(Debug, Clone)]
pub struct Options {
    pub(crate) filter_list: FilterList,
    pub(crate) method: Method,
}

impl Options {
    pub fn new() -> Self {
        Self {
            filter_list: FilterList::All,
            method: Method::Combined,
        }
    }

    #[cfg(feature = "dev")]
    pub fn with_filter_list(filter_list: FilterList) -> Self {
        Self::new().set_filter_list(filter_list)
    }

    #[cfg(feature = "dev")]
    pub fn with_method(method: Method) -> Self {
        Self::new().set_method(method)
    }

    pub fn set_filter_list(mut self, filter_list: FilterList) -> Self {
        self.filter_list = filter_list;
        self
    }

    #[cfg(feature = "dev")]
    pub fn set_method(mut self, method: Method) -> Self {
        self.method = method;
        self
    }
}

impl Default for Options {
    fn default() -> Self {
        Self::new()
    }
}
```

## File: `src/core/query.rs`
```rust
use super::{FilterList, Method, Text};
use crate::scripts::grouping::MultiLangScript;

pub struct Query<'a, 'b> {
    pub(crate) text: &'a str,
    pub(crate) filter_list: &'b FilterList,
    pub(crate) method: Method,
}

// TODO: find a better name?
// A query after script detection
pub struct InternalQuery<'a, 'b> {
    pub(crate) text: Text<'a>,
    pub(crate) filter_list: &'b FilterList,
    pub(crate) multi_lang_script: MultiLangScript,
}

impl<'a, 'b> Query<'a, 'b> {
    pub(crate) fn to_internal(&self, multi_lang_script: MultiLangScript) -> InternalQuery<'a, 'b> {
        InternalQuery {
            text: Text::new(self.text),
            filter_list: self.filter_list,
            multi_lang_script,
        }
    }
}
```

## File: `src/core/text.rs`
```rust
use std::cell::{Ref, RefCell};
use std::ops::Deref;

#[derive(Debug)]
pub struct LowercaseText {
    inner: String,
}

impl LowercaseText {
    pub fn new(original_text: &str) -> Self {
        let inner = original_text.to_lowercase();
        Self { inner }
    }
}

impl Deref for LowercaseText {
    type Target = str;

    fn deref(&self) -> &Self::Target {
        &self.inner
    }
}

#[derive(Debug)]
pub struct Text<'a> {
    original: &'a str,
    lowercase: RefCell<Option<LowercaseText>>,
}

impl<'a> Text<'a> {
    pub fn new(original_text: &'a str) -> Self {
        Self {
            original: original_text,
            lowercase: RefCell::new(None),
        }
    }

    pub fn lowercase(&self) -> Ref<'_, LowercaseText> {
        if self.lowercase.borrow().is_none() {
            let lowercase_text = LowercaseText::new(self.original);
            self.lowercase.replace(Some(lowercase_text));
        }

        let ref_opt_lowercase = self.lowercase.borrow();
        Ref::map(ref_opt_lowercase, |r| r.as_ref().unwrap())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_text() {
        let text = Text::new("Hello THERE");
        assert_eq!(text.lowercase().deref().deref(), "hello there");
    }
}
```

## File: `src/scripts/chars.rs`
```rust
pub(crate) fn is_cyrillic(ch: char) -> bool {
    matches!(ch,
        '\u{0400}'..='\u{0484}'
        | '\u{0487}'..='\u{052F}'
        | '\u{2DE0}'..='\u{2DFF}'
        | '\u{A640}'..='\u{A69D}'
        | '\u{1D2B}'
        | '\u{1D78}'
        | '\u{A69F}'
    )
}

// https://en.wikipedia.org/wiki/Latin_script_in_Unicode
pub(crate) fn is_latin(ch: char) -> bool {
    matches!(ch,
        'a'..='z'
        | 'A'..='Z'
        | '\u{0080}'..='\u{00FF}'
        | '\u{0100}'..='\u{017F}'
        | '\u{0180}'..='\u{024F}'
        | '\u{0250}'..='\u{02AF}'
        | '\u{1D00}'..='\u{1D7F}'
        | '\u{1D80}'..='\u{1DBF}'
        | '\u{1E00}'..='\u{1EFF}'
        | '\u{2100}'..='\u{214F}'
        | '\u{2C60}'..='\u{2C7F}'
        | '\u{A720}'..='\u{A7FF}'
        | '\u{AB30}'..='\u{AB6F}'
    )
}

// Based on https://en.wikipedia.org/wiki/Arabic_script_in_Unicode
pub(crate) fn is_arabic(ch: char) -> bool {
    matches!(ch,
        '\u{0600}'..='\u{06FF}'
        | '\u{0750}'..='\u{07FF}'
        | '\u{08A0}'..='\u{08FF}'
        | '\u{FB50}'..='\u{FDFF}'
        | '\u{FE70}'..='\u{FEFF}'
        | '\u{10E60}'..='\u{10E7F}'
        | '\u{1EE00}'..='\u{1EEFF}'
    )
}

// Based on https://en.wikipedia.org/wiki/Devanagari#Unicode
pub(crate) fn is_devanagari(ch: char) -> bool {
    matches!(ch, '\u{0900}'..='\u{097F}' | '\u{A8E0}'..='\u{A8FF}' | '\u{1CD0}'..='\u{1CFF}')
}

// Based on https://www.key-shortcut.com/en/writing-systems/ethiopian-script/
pub(crate) fn is_ethiopic(ch: char) -> bool {
    matches!(ch, '\u{1200}'..='\u{139F}' | '\u{2D80}'..='\u{2DDF}' | '\u{AB00}'..='\u{AB2F}')
}

// Based on https://en.wikipedia.org/wiki/Hebrew_(Unicode_block)
pub(crate) fn is_hebrew(ch: char) -> bool {
    matches!(ch, '\u{0590}'..='\u{05FF}')
}

pub(crate) fn is_georgian(ch: char) -> bool {
    matches!(ch, '\u{10A0}'..='\u{10FF}')
}

pub(crate) fn is_mandarin(ch: char) -> bool {
    matches!(ch,
        '\u{2E80}'..='\u{2E99}'
        | '\u{2E9B}'..='\u{2EF3}'
        | '\u{2F00}'..='\u{2FD5}'
        | '\u{3005}'
        | '\u{3007}'
        | '\u{3021}'..='\u{3029}'
        | '\u{3038}'..='\u{303B}'
        | '\u{3400}'..='\u{4DB5}'
        | '\u{4E00}'..='\u{9FCC}'
        | '\u{F900}'..='\u{FA6D}'
        | '\u{FA70}'..='\u{FAD9}'
    )
}

pub(crate) fn is_bengali(ch: char) -> bool {
    matches!(ch, '\u{0980}'..='\u{09FF}')
}

pub(crate) fn is_hiragana(ch: char) -> bool {
    matches!(ch, '\u{3040}'..='\u{309F}')
}

pub(crate) fn is_katakana(ch: char) -> bool {
    matches!(ch, '\u{30A0}'..='\u{30FF}')
}

// Hangul is Korean Alphabet. Unicode ranges are taken from: https://en.wikipedia.org/wiki/Hangul
pub(crate) fn is_hangul(ch: char) -> bool {
    matches!(ch,
        '\u{AC00}'..='\u{D7AF}'
        | '\u{1100}'..='\u{11FF}'
        | '\u{3130}'..='\u{318F}'
        | '\u{3200}'..='\u{32FF}'
        | '\u{A960}'..='\u{A97F}'
        | '\u{D7B0}'..='\u{D7FF}'
        | '\u{FF00}'..='\u{FFEF}'
    )
}

// Taken from: https://en.wikipedia.org/wiki/Greek_and_Coptic
pub(crate) fn is_greek(ch: char) -> bool {
    matches!(ch, '\u{0370}'..='\u{03FF}')
}

// Based on: https://en.wikipedia.org/wiki/Kannada_(Unicode_block)
pub(crate) fn is_kannada(ch: char) -> bool {
    matches!(ch, '\u{0C80}'..='\u{0CFF}')
}

// Based on: https://en.wikipedia.org/wiki/Tamil_(Unicode_block)
pub(crate) fn is_tamil(ch: char) -> bool {
    matches!(ch, '\u{0B80}'..='\u{0BFF}')
}

// Based on: https://en.wikipedia.org/wiki/Thai_(Unicode_block)
pub(crate) fn is_thai(ch: char) -> bool {
    matches!(ch, '\u{0E00}'..='\u{0E7F}')
}

// Based on: https://en.wikipedia.org/wiki/Gujarati_(Unicode_block)
pub(crate) fn is_gujarati(ch: char) -> bool {
    matches!(ch, '\u{0A80}'..='\u{0AFF}')
}

// Gurmukhi is the script for Punjabi language.
// Based on: https://en.wikipedia.org/wiki/Gurmukhi_(Unicode_block)
pub(crate) fn is_gurmukhi(ch: char) -> bool {
    matches!(ch, '\u{0A00}'..='\u{0A7F}')
}

pub(crate) fn is_telugu(ch: char) -> bool {
    matches!(ch, '\u{0C00}'..='\u{0C7F}')
}

// Based on: https://en.wikipedia.org/wiki/Malayalam_(Unicode_block)
pub(crate) fn is_malayalam(ch: char) -> bool {
    matches!(ch, '\u{0D00}'..='\u{0D7F}')
}

// Based on: https://en.wikipedia.org/wiki/Malayalam_(Unicode_block)
pub(crate) fn is_oriya(ch: char) -> bool {
    matches!(ch, '\u{0B00}'..='\u{0B7F}')
}

// Based on: https://en.wikipedia.org/wiki/Myanmar_(Unicode_block)
pub(crate) fn is_myanmar(ch: char) -> bool {
    matches!(ch, '\u{1000}'..='\u{109F}')
}

// Based on: https://en.wikipedia.org/wiki/Sinhala_(Unicode_block)
pub(crate) fn is_sinhala(ch: char) -> bool {
    matches!(ch, '\u{0D80}'..='\u{0DFF}')
}

// Based on: https://en.wikipedia.org/wiki/Khmer_alphabet
pub(crate) fn is_khmer(ch: char) -> bool {
    matches!(ch, '\u{1780}'..='\u{17FF}' | '\u{19E0}'..='\u{19FF}')
}

// See:
// * https://en.wikipedia.org/wiki/Armenian_alphabet
// * https://www.unicode.org/charts/PDF/U0530.pdf
// * https://www.unicode.org/charts/PDF/UFB00.pdf
pub(crate) fn is_armenian(ch: char) -> bool {
    matches!(ch, '\u{0530}'..='\u{058F}' | '\u{FB13}'..='\u{FB17}')
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_latin() {
        assert_eq!(is_latin('z'), true);
        assert_eq!(is_latin('A'), true);
        assert_eq!(is_latin('č'), true);
        assert_eq!(is_latin('š'), true);
        assert_eq!(is_latin('Ĵ'), true);

        assert_eq!(is_latin('ж'), false);
    }

    #[test]
    fn test_is_cyrillic() {
        assert_eq!(is_cyrillic('а'), true);
        assert_eq!(is_cyrillic('Я'), true);
        assert_eq!(is_cyrillic('Ґ'), true);
        assert_eq!(is_cyrillic('ї'), true);
        assert_eq!(is_cyrillic('Ꙕ'), true);

        assert_eq!(is_cyrillic('L'), false);
    }

    #[test]
    fn test_is_ethiopic() {
        assert_eq!(is_ethiopic('ፚ'), true);
        assert_eq!(is_ethiopic('ᎀ'), true);

        assert_eq!(is_ethiopic('а'), false);
        assert_eq!(is_ethiopic('L'), false);
    }

    #[test]
    fn test_is_georgian() {
        assert_eq!(is_georgian('რ'), true);
        assert_eq!(is_georgian('ж'), false);
    }

    #[test]
    fn test_is_bengali() {
        assert_eq!(is_bengali('ই'), true);
        assert_eq!(is_bengali('z'), false);
    }

    #[test]
    fn test_is_katakana() {
        assert_eq!(is_katakana('カ'), true);
        assert_eq!(is_katakana('f'), false);
    }

    #[test]
    fn test_is_hiragana() {
        assert_eq!(is_hiragana('ひ'), true);
        assert_eq!(is_hiragana('a'), false);
    }

    #[test]
    fn test_is_hangul() {
        assert_eq!(is_hangul('ᄁ'), true);
        assert_eq!(is_hangul('t'), false);
    }

    #[test]
    fn test_is_greek() {
        assert_eq!(is_greek('φ'), true);
        assert_eq!(is_greek('ф'), false);
    }

    #[test]
    fn test_is_kannada() {
        assert_eq!(is_kannada('ಡ'), true);
        assert_eq!(is_kannada('S'), false);
    }

    #[test]
    fn test_is_tamil() {
        assert_eq!(is_tamil('ஐ'), true);
        assert_eq!(is_tamil('Ж'), false);
    }

    #[test]
    fn test_is_thai() {
        assert_eq!(is_thai('ก'), true);
        assert_eq!(is_thai('๛'), true);
        assert_eq!(is_thai('Ж'), false);
    }

    #[test]
    fn test_is_gujarati() {
        assert_eq!(is_gujarati('ઁ'), true);
        assert_eq!(is_gujarati('૱'), true);
        assert_eq!(is_gujarati('Ж'), false);
    }

    #[test]
    fn test_is_gurmukhi() {
        assert_eq!(is_gurmukhi('ਁ'), true);
        assert_eq!(is_gurmukhi('ੴ'), true);
        assert_eq!(is_gurmukhi('Ж'), false);
    }

    #[test]
    fn test_is_telugu() {
        assert_eq!(is_telugu('ఁ'), true);
        assert_eq!(is_telugu('౿'), true);
        assert_eq!(is_telugu('Ж'), false);
    }

    #[test]
    fn test_is_oriya() {
        assert_eq!(is_oriya('ଐ'), true);
        assert_eq!(is_oriya('୷'), true);
        assert_eq!(is_oriya('౿'), false);
    }

    #[test]
    fn test_is_armenian() {
        assert_eq!(is_armenian('რ'), false); // Georgian
        assert_eq!(is_armenian('Ш'), false); // Cyrillic
        assert_eq!(is_armenian('ա'), true);
        assert_eq!(is_armenian('Ա'), true);
        assert_eq!(is_armenian('Փ'), true);
        assert_eq!(is_armenian('և'), true);
    }
}
```

## File: `src/scripts/detect.rs`
```rust
use std::cmp::Reverse;

use super::chars;
use super::script::Script;
use crate::utils::is_stop_char;

type ScriptCounter = (Script, fn(char) -> bool, usize);

/// Detect only a script by a given text.
/// Works much faster than a complete detection with `detect`.
///
/// # Example
/// ```
/// use whatlang::{detect_script, Script};
/// let script = detect_script("Благодаря Эсперанто вы обрётете друзей по всему миру!").unwrap();
/// assert_eq!(script, Script::Cyrillic);
/// ```
pub fn detect_script(text: &str) -> Option<Script> {
    let raw_info = raw_detect_script(text);
    raw_info.main_script()
}

#[derive(Debug)]
pub struct RawScriptInfo {
    pub counters: Vec<(Script, usize)>,
}

impl RawScriptInfo {
    fn new(mut counters: Vec<(Script, usize)>) -> Self {
        counters.sort_unstable_by_key(|(_, score)| Reverse(*score));
        Self { counters }
    }

    pub(crate) fn main_script(&self) -> Option<Script> {
        // expect - is safe because self.counters is never expected to be empty
        // See raw_detect_script().
        let pair = self.counters.first().expect("counters must not be empty");
        if pair.1 > 0 { Some(pair.0) } else { None }
    }

    pub(crate) fn count(&self, script: Script) -> usize {
        // expect - is safe because self.counters always have all scripts
        // See raw_detect_script().
        self.counters
            .iter()
            .find(|(s, _count)| *s == script)
            .expect("count() failed because script is not found")
            .1
    }
}

pub fn raw_detect_script(text: &str) -> RawScriptInfo {
    let mut script_counters: [ScriptCounter; 25] = [
        (Script::Latin, chars::is_latin, 0),
        (Script::Cyrillic, chars::is_cyrillic, 0),
        (Script::Arabic, chars::is_arabic, 0),
        (Script::Mandarin, chars::is_mandarin, 0),
        (Script::Devanagari, chars::is_devanagari, 0),
        (Script::Hebrew, chars::is_hebrew, 0),
        (Script::Ethiopic, chars::is_ethiopic, 0),
        (Script::Georgian, chars::is_georgian, 0),
        (Script::Bengali, chars::is_bengali, 0),
        (Script::Hangul, chars::is_hangul, 0),
        (Script::Hiragana, chars::is_hiragana, 0),
        (Script::Katakana, chars::is_katakana, 0),
        (Script::Greek, chars::is_greek, 0),
        (Script::Kannada, chars::is_kannada, 0),
        (Script::Tamil, chars::is_tamil, 0),
        (Script::Thai, chars::is_thai, 0),
        (Script::Gujarati, chars::is_gujarati, 0),
        (Script::Gurmukhi, chars::is_gurmukhi, 0),
        (Script::Telugu, chars::is_telugu, 0),
        (Script::Malayalam, chars::is_malayalam, 0),
        (Script::Oriya, chars::is_oriya, 0),
        (Script::Myanmar, chars::is_myanmar, 0),
        (Script::Sinhala, chars::is_sinhala, 0),
        (Script::Khmer, chars::is_khmer, 0),
        (Script::Armenian, chars::is_armenian, 0),
    ];

    for ch in text.chars() {
        if is_stop_char(ch) {
            continue;
        }

        // For performance reasons, we need to mutate script_counters by calling
        // `swap` function, it would not be possible to do using normal iterator.
        for i in 0..script_counters.len() {
            let found = {
                let (_script, check_fn, ref mut count) = script_counters[i];
                if check_fn(ch) {
                    *count += 1;
                    true
                } else {
                    false
                }
            };
            // Have to let borrow of count fall out of scope before doing swapping, or we could
            // do this above.
            if found {
                // If script was found, move it closer to the front.
                // If the text contains largely 1 or 2 scripts, this will
                // cause these scripts to be eventually checked first.
                if i > 0 {
                    script_counters.swap(i - 1, i);
                }
                break;
            }
        }
    }

    let counters: Vec<(Script, usize)> = script_counters
        .iter()
        .map(|&(script, _, count)| (script, count))
        .collect();

    RawScriptInfo::new(counters)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_script_name() {
        assert_eq!(Script::Cyrillic.name(), "Cyrillic");
        assert_eq!(Script::Katakana.name(), "Katakana");
    }

    #[test]
    fn test_detect_script() {
        assert_eq!(detect_script("1234567890-,;!"), None);

        // One script
        assert_eq!(detect_script("Hello!"), Some(Script::Latin));
        assert_eq!(detect_script("Привет всем!"), Some(Script::Cyrillic));
        assert_eq!(
            detect_script("ქართული ენა მსოფლიო "),
            Some(Script::Georgian)
        );
        assert_eq!(
            detect_script("県見夜上温国阪題富販"),
            Some(Script::Mandarin)
        );
        assert_eq!(
            detect_script(" ككل حوالي 1.6، ومعظم الناس "),
            Some(Script::Arabic)
        );
        assert_eq!(
            detect_script("हिमालयी वन चिड़िया (जूथेरा सालिमअली) चिड़िया की एक प्रजाति है"),
            Some(Script::Devanagari)
        );
        assert_eq!(
            detect_script("היסטוריה והתפתחות של האלפבית העברי"),
            Some(Script::Hebrew)
        );
        assert_eq!(
            detect_script("የኢትዮጵያ ፌዴራላዊ ዴሞክራሲያዊሪፐብሊክ"),
            Some(Script::Ethiopic)
        );

        // Mixed scripts
        assert_eq!(
            detect_script("Привет! Текст на русском with some English."),
            Some(Script::Cyrillic)
        );
        assert_eq!(
            detect_script("Russian word любовь means love."),
            Some(Script::Latin)
        );
    }
}
```

## File: `src/scripts/grouping.rs`
```rust
use super::Script;
use crate::Lang;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum MultiLangScript {
    Latin,
    Cyrillic,
    Arabic,
    Devanagari,
    Hebrew,
}

impl MultiLangScript {
    pub fn to_script(self) -> Script {
        match self {
            Self::Latin => Script::Latin,
            Self::Cyrillic => Script::Cyrillic,
            Self::Arabic => Script::Arabic,
            Self::Devanagari => Script::Devanagari,
            Self::Hebrew => Script::Hebrew,
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ScriptLangGroup {
    Multi(MultiLangScript),
    One(Lang),

    // Mandarin writing can be japanese in some cases.
    // For now it's a hack.
    // See https://github.com/greyblake/whatlang-rs/pull/45
    Mandarin,
}

impl Script {
    pub fn to_lang_group(self) -> ScriptLangGroup {
        use MultiLangScript as MLS;
        use ScriptLangGroup::{Mandarin, Multi, One};

        match self {
            Script::Latin => Multi(MLS::Latin),
            Script::Cyrillic => Multi(MLS::Cyrillic),
            Script::Arabic => Multi(MLS::Arabic),
            Script::Devanagari => Multi(MLS::Devanagari),
            Script::Hebrew => Multi(MLS::Hebrew),
            Script::Mandarin => Mandarin,
            Script::Bengali => One(Lang::Ben),
            Script::Hangul => One(Lang::Kor),
            Script::Georgian => One(Lang::Kat),
            Script::Greek => One(Lang::Ell),
            Script::Kannada => One(Lang::Kan),
            Script::Tamil => One(Lang::Tam),
            Script::Thai => One(Lang::Tha),
            Script::Gujarati => One(Lang::Guj),
            Script::Gurmukhi => One(Lang::Pan),
            Script::Telugu => One(Lang::Tel),
            Script::Malayalam => One(Lang::Mal),
            Script::Oriya => One(Lang::Ori),
            Script::Myanmar => One(Lang::Mya),
            Script::Sinhala => One(Lang::Sin),
            Script::Khmer => One(Lang::Khm),
            Script::Ethiopic => One(Lang::Amh),
            Script::Armenian => One(Lang::Hye),
            Script::Katakana | Script::Hiragana => One(Lang::Jpn),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_script_to_lang_group() {
        assert_eq!(
            Script::Latin.to_lang_group(),
            ScriptLangGroup::Multi(MultiLangScript::Latin)
        );

        assert_eq!(
            Script::Georgian.to_lang_group(),
            ScriptLangGroup::One(Lang::Kat)
        );
    }

    #[test]
    fn test_multi_lang_script_to_script() {
        assert_eq!(MultiLangScript::Latin.to_script(), Script::Latin);
        assert_eq!(MultiLangScript::Hebrew.to_script(), Script::Hebrew);
    }
}
```

## File: `src/scripts/lang_mapping.rs`
```rust
use super::Script;
use crate::Lang;

const LATIN_LANGS: [Lang; 37] = [
    Lang::Spa,
    Lang::Eng,
    Lang::Por,
    Lang::Ind,
    Lang::Fra,
    Lang::Deu,
    Lang::Jav,
    Lang::Vie,
    Lang::Ita,
    Lang::Tur,
    Lang::Pol,
    Lang::Ron,
    Lang::Hrv,
    Lang::Nld,
    Lang::Uzb,
    Lang::Hun,
    Lang::Aze,
    Lang::Ces,
    Lang::Zul,
    Lang::Swe,
    Lang::Aka,
    Lang::Sna,
    Lang::Afr,
    Lang::Fin,
    Lang::Slk,
    Lang::Tgl,
    Lang::Tuk,
    Lang::Dan,
    Lang::Nob,
    Lang::Cat,
    Lang::Lit,
    Lang::Slv,
    Lang::Epo,
    Lang::Lav,
    Lang::Est,
    Lang::Lat,
    Lang::Cym,
];
const CYRILLIC_LANGS: [Lang; 6] = [
    Lang::Rus,
    Lang::Ukr,
    Lang::Srp,
    Lang::Bel,
    Lang::Bul,
    Lang::Mkd,
];
const ARABIC_LANGS: [Lang; 3] = [Lang::Ara, Lang::Urd, Lang::Pes];
const DEVANAGARI_LANGS: [Lang; 3] = [Lang::Hin, Lang::Mar, Lang::Nep];
const HEBREW_LANGS: [Lang; 2] = [Lang::Heb, Lang::Yid];

pub fn script_langs(script: Script) -> &'static [Lang] {
    match script {
        Script::Latin => &LATIN_LANGS,
        Script::Cyrillic => &CYRILLIC_LANGS,
        Script::Devanagari => &DEVANAGARI_LANGS,
        Script::Hebrew => &HEBREW_LANGS,
        Script::Arabic => &ARABIC_LANGS,
        Script::Mandarin => &[Lang::Cmn],
        Script::Bengali => &[Lang::Ben],
        Script::Hangul => &[Lang::Kor],
        Script::Georgian => &[Lang::Kat],
        Script::Greek => &[Lang::Ell],
        Script::Kannada => &[Lang::Kan],
        Script::Tamil => &[Lang::Tam],
        Script::Thai => &[Lang::Tha],
        Script::Gujarati => &[Lang::Guj],
        Script::Gurmukhi => &[Lang::Pan],
        Script::Telugu => &[Lang::Tel],
        Script::Malayalam => &[Lang::Mal],
        Script::Oriya => &[Lang::Ori],
        Script::Myanmar => &[Lang::Mya],
        Script::Sinhala => &[Lang::Sin],
        Script::Khmer => &[Lang::Khm],
        Script::Ethiopic => &[Lang::Amh],
        Script::Armenian => &[Lang::Hye],
        Script::Katakana | Script::Hiragana => &[Lang::Jpn],
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_script_langs() {
        assert_eq!(script_langs(Script::Hebrew), &[Lang::Heb, Lang::Yid])
    }
}
```

## File: `src/scripts/mod.rs`
```rust
pub(crate) mod chars;
mod detect;
pub(crate) mod grouping;
mod lang_mapping;
mod script;

pub use self::detect::detect_script;
pub use self::detect::{RawScriptInfo, raw_detect_script};
pub use self::script::Script;
```

## File: `src/scripts/script.rs`
```rust
use std::fmt;
use std::str::FromStr;

use super::lang_mapping;
use crate::Lang;
use crate::error::ParseError;

/// Represents a writing system (Latin, Cyrillic, Arabic, etc).
#[cfg_attr(feature = "enum-map", derive(::enum_map::Enum))]
#[cfg_attr(feature = "arbitrary", derive(::arbitrary::Arbitrary))]
#[cfg_attr(feature = "serde", derive(::serde::Serialize, ::serde::Deserialize))]
#[derive(PartialEq, Eq, Debug, Clone, Copy, Hash)]
pub enum Script {
    // Keep this in alphabetic order (for C bindings)
    Arabic,
    Armenian,
    Bengali,
    Cyrillic,
    Devanagari,
    Ethiopic,
    Georgian,
    Greek,
    Gujarati,
    Gurmukhi,
    Hangul,
    Hebrew,
    Hiragana,
    Kannada,
    Katakana,
    Khmer,
    Latin,
    Malayalam,
    Mandarin,
    Myanmar,
    Oriya,
    Sinhala,
    Tamil,
    Telugu,
    Thai,
}

// Array of all existing Script values.
const VALUES: [Script; 25] = [
    Script::Arabic,
    Script::Armenian,
    Script::Bengali,
    Script::Cyrillic,
    Script::Devanagari,
    Script::Ethiopic,
    Script::Georgian,
    Script::Greek,
    Script::Gujarati,
    Script::Gurmukhi,
    Script::Hangul,
    Script::Hebrew,
    Script::Hiragana,
    Script::Kannada,
    Script::Katakana,
    Script::Khmer,
    Script::Latin,
    Script::Malayalam,
    Script::Mandarin,
    Script::Myanmar,
    Script::Oriya,
    Script::Sinhala,
    Script::Tamil,
    Script::Telugu,
    Script::Thai,
];

impl Script {
    /// Get all existing scripts.
    ///
    /// # Example
    /// ```
    /// use whatlang::Script;
    /// for script in Script::all() {
    ///     println!("{}", script);
    /// }
    /// ```
    pub fn all() -> &'static [Script] {
        &VALUES
    }

    pub fn name(&self) -> &str {
        match *self {
            Script::Latin => "Latin",
            Script::Cyrillic => "Cyrillic",
            Script::Arabic => "Arabic",
            Script::Devanagari => "Devanagari",
            Script::Hiragana => "Hiragana",
            Script::Katakana => "Katakana",
            Script::Ethiopic => "Ethiopic",
            Script::Hebrew => "Hebrew",
            Script::Bengali => "Bengali",
            Script::Georgian => "Georgian",
            Script::Mandarin => "Mandarin",
            Script::Hangul => "Hangul",
            Script::Greek => "Greek",
            Script::Kannada => "Kannada",
            Script::Tamil => "Tamil",
            Script::Thai => "Thai",
            Script::Gujarati => "Gujarati",
            Script::Gurmukhi => "Gurmukhi",
            Script::Telugu => "Telugu",
            Script::Malayalam => "Malayalam",
            Script::Oriya => "Oriya",
            Script::Myanmar => "Myanmar",
            Script::Sinhala => "Sinhala",
            Script::Khmer => "Khmer",
            Script::Armenian => "Armenian",
        }
    }

    pub fn langs(&self) -> &[Lang] {
        lang_mapping::script_langs(*self)
    }
}

impl fmt::Display for Script {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.name())
    }
}

impl FromStr for Script {
    type Err = ParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s.to_lowercase().trim() {
            "latin" => Ok(Script::Latin),
            "cyrillic" => Ok(Script::Cyrillic),
            "arabic" => Ok(Script::Arabic),
            "devanagari" => Ok(Script::Devanagari),
            "hiragana" => Ok(Script::Hiragana),
            "katakana" => Ok(Script::Katakana),
            "ethiopic" => Ok(Script::Ethiopic),
            "hebrew" => Ok(Script::Hebrew),
            "bengali" => Ok(Script::Bengali),
            "georgian" => Ok(Script::Georgian),
            "mandarin" => Ok(Script::Mandarin),
            "hangul" => Ok(Script::Hangul),
            "greek" => Ok(Script::Greek),
            "kannada" => Ok(Script::Kannada),
            "tamil" => Ok(Script::Tamil),
            "thai" => Ok(Script::Thai),
            "gujarati" => Ok(Script::Gujarati),
            "gurmukhi" => Ok(Script::Gurmukhi),
            "telugu" => Ok(Script::Telugu),
            "malayalam" => Ok(Script::Malayalam),
            "oriya" => Ok(Script::Oriya),
            "myanmar" => Ok(Script::Myanmar),
            "sinhala" => Ok(Script::Sinhala),
            "khmer" => Ok(Script::Khmer),
            "armenian" => Ok(Script::Armenian),
            _ => Err(ParseError::Script(s.to_string())),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_all() {
        assert_eq!(Script::all().len(), 25);
        let all = Script::all();
        assert!(all.contains(&Script::Cyrillic));
        assert!(all.contains(&Script::Arabic));
        assert!(all.contains(&Script::Latin));
    }

    #[test]
    fn test_from_str() {
        for &script in Script::all() {
            let s = script.name();
            assert_eq!(s.parse::<Script>().unwrap(), script);
            assert_eq!(s.to_lowercase().parse::<Script>().unwrap(), script);
            assert_eq!(s.to_uppercase().parse::<Script>().unwrap(), script);
        }

        let result = "foobar".parse::<Script>();
        assert!(matches!(result, Err(ParseError::Script(_))));
    }

    #[test]
    fn test_langs() {
        // Vec of all langs obtained with script.langs()
        let script_langs: Vec<Lang> = Script::all()
            .iter()
            .map(|script| script.langs())
            .flatten()
            .copied()
            .collect();

        // Ensure all langs belong at least to one script
        for lang in Lang::all() {
            assert!(script_langs.contains(&lang));
        }
    }

    #[test]
    fn test_script_display() {
        assert_eq!(Script::Georgian.to_string(), "Georgian");
        assert_eq!(Script::Cyrillic.to_string(), "Cyrillic");
        assert_eq!(Script::Arabic.to_string(), "Arabic");
    }

    #[cfg(feature = "serde")]
    #[test]
    fn test_serialize_and_deserialize() {
        let scripts = vec![Script::Georgian, Script::Cyrillic];
        let json_scripts = serde_json::to_string(&scripts).unwrap();
        assert_eq!(json_scripts, r#"["Georgian","Cyrillic"]"#);
        let parsed_scripts: Vec<Script> = serde_json::from_str(&json_scripts).unwrap();
        assert_eq!(parsed_scripts, scripts);
    }
}
```

## File: `src/trigrams/detection.rs`
```rust
use hashbrown::HashMap;

use super::utils::{TrigramsWithPositions, get_trigrams_with_positions};
use super::{ARABIC_LANGS, CYRILLIC_LANGS, DEVANAGARI_LANGS, HEBREW_LANGS, LATIN_LANGS};
use super::{LangProfile, LangProfileList};
use super::{MAX_TOTAL_DISTANCE, MAX_TRIGRAM_DISTANCE, Trigram};
use crate::Lang;
use crate::core::{FilterList, Info, InternalQuery, Text, calculate_confidence};
use crate::scripts::grouping::MultiLangScript;

#[derive(Debug)]
pub struct RawOutcome {
    pub trigrams_count: usize,
    #[allow(dead_code)]
    pub raw_distances: Vec<(Lang, u32)>,
    pub scores: Vec<(Lang, f64)>,
}

#[inline]
pub fn detect(iquery: &InternalQuery) -> Option<Info> {
    let raw_outcome = raw_detect(iquery);
    let RawOutcome {
        trigrams_count,
        scores,
        ..
    } = raw_outcome;

    let mut raw_scores_iter = scores.into_iter();

    let opt_lang_score1 = raw_scores_iter.next();
    let opt_lang_score2 = raw_scores_iter.next();

    // TODO: Logic is duplicated in alphabets. Consider refactoring
    opt_lang_score1.map(|(lang1, score1)| {
        let script = iquery.multi_lang_script.to_script();
        let confidence = if let Some((_, score2)) = opt_lang_score2 {
            calculate_confidence(score1, score2, trigrams_count)
        } else {
            1.0
        };
        Info::new(script, lang1, confidence)
    })
}

#[inline]
pub fn raw_detect(iquery: &InternalQuery) -> RawOutcome {
    let lang_profile_list = script_to_lang_profile_list(iquery.multi_lang_script);
    calculate_scores_in_profiles(&iquery.text, iquery.filter_list, lang_profile_list)
}

fn script_to_lang_profile_list(script: MultiLangScript) -> LangProfileList {
    use MultiLangScript as MLS;
    match script {
        MLS::Latin => LATIN_LANGS,
        MLS::Cyrillic => CYRILLIC_LANGS,
        MLS::Arabic => ARABIC_LANGS,
        MLS::Devanagari => DEVANAGARI_LANGS,
        MLS::Hebrew => HEBREW_LANGS,
    }
}

#[inline]
fn calculate_scores_in_profiles(
    text: &Text,
    filter_list: &FilterList,
    lang_profile_list: LangProfileList,
) -> RawOutcome {
    let mut lang_distances: Vec<(Lang, u32)> = vec![];

    let TrigramsWithPositions {
        trigram_positions, ..
    } = get_trigrams_with_positions(&text.lowercase());
    let unique_trigrams_count = trigram_positions.len();

    for &(lang, lang_trigrams) in lang_profile_list {
        if !filter_list.is_allowed(lang) {
            continue;
        }
        let dist = calculate_distance(lang_trigrams, &trigram_positions);
        lang_distances.push(((lang), dist));
    }

    // Sort languages by distance
    lang_distances.sort_unstable_by_key(|(_, dist)| *dist);

    let max_dist = unique_trigrams_count as u32 * MAX_TRIGRAM_DISTANCE;

    let raw_scores = lang_distances
        .iter()
        .map(|&(lang, distance)| (lang, distance_to_raw_score(distance, max_dist)))
        .collect();

    RawOutcome {
        trigrams_count: unique_trigrams_count,
        scores: raw_scores,
        raw_distances: lang_distances,
    }
}

#[inline]
fn calculate_distance(lang_trigrams: LangProfile, text_trigrams: &HashMap<Trigram, u32>) -> u32 {
    let mut total_dist = 0u32;

    for (i, &trigram) in lang_trigrams.iter().enumerate() {
        let dist = match text_trigrams.get(&trigram) {
            Some(&n) => (n as i32 - i as i32).unsigned_abs(),
            None => MAX_TRIGRAM_DISTANCE,
        };
        total_dist += dist;
    }

    let count = text_trigrams.len() as u32;

    if MAX_TRIGRAM_DISTANCE > count {
        let delta = MAX_TRIGRAM_DISTANCE - count;
        total_dist -= delta * MAX_TRIGRAM_DISTANCE;
    }

    total_dist.clamp(0, MAX_TOTAL_DISTANCE)
}

#[inline]
fn distance_to_raw_score(distance: u32, max_distance: u32) -> f64 {
    let similarity = max_distance - distance;
    similarity as f64 / max_distance as f64
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_when_german_is_given() {
        let text = "Die Ordnung muss für immer in diesem Codebase bleiben";
        let iq = InternalQuery {
            text: Text::new(text),
            filter_list: &FilterList::default(),
            multi_lang_script: MultiLangScript::Latin,
        };
        let raw_outcome = raw_detect(&iq);

        assert_eq!(raw_outcome.trigrams_count, 50);

        let &(first_lang, first_score) = raw_outcome.scores.first().unwrap();
        let &(_last_lang, last_score) = raw_outcome.scores.last().unwrap();

        assert_eq!(first_lang, Lang::Deu);

        assert!(first_score >= 0.0);
        assert!(first_score <= 1.0);

        assert!(last_score >= 0.0);
        assert!(last_score <= 1.0);
    }
}
```

## File: `src/trigrams/mod.rs`
```rust
pub mod detection;
mod profiles;
pub mod utils;

pub use profiles::*;

pub use detection::{RawOutcome, detect, raw_detect};

#[derive(Debug, Eq, PartialEq, Hash, Ord, PartialOrd, Clone, Copy)]
pub struct Trigram(pub(crate) char, pub(crate) char, pub(crate) char);

// Maximum distance(difference) for a trigram in a language profile and text profile.
pub const MAX_TRIGRAM_DISTANCE: u32 = 300;

// 300 trigrams where each has MAX_TOTAL_DISTANCE=300, gives us 90_000.
pub const MAX_TOTAL_DISTANCE: u32 = MAX_TRIGRAM_DISTANCE * MAX_TRIGRAM_DISTANCE;

// Double MAX_TRIGRAM_DISTANCE
pub const TEXT_TRIGRAMS_SIZE: usize = 600;
```

## File: `src/trigrams/profiles.rs`
```rust
// NOTE:
//    This file is generated automatically.

use crate::Lang;
use crate::trigrams::Trigram;

pub type LangProfile = &'static [Trigram];
pub type LangProfileList = &'static [(Lang, LangProfile)];

/// Languages for script Latin
pub static LATIN_LANGS: LangProfileList = &[
    (
        Lang::Spa,
        &[
            Trigram(' ', 'd', 'e'),
            Trigram('o', 's', ' '),
            Trigram('d', 'e', ' '),
            Trigram(' ', 'l', 'a'),
            Trigram('l', 'a', ' '),
            Trigram(' ', 'y', ' '),
            Trigram(' ', 'a', ' '),
            Trigram('e', 's', ' '),
            Trigram('ó', 'n', ' '),
            Trigram('i', 'ó', 'n'),
            Trigram('r', 'e', 'c'),
            Trigram('e', 'r', 'e'),
            Trigram('d', 'e', 'r'),
            Trigram(' ', 'c', 'o'),
            Trigram('e', ' ', 'l'),
            Trigram('e', 'l', ' '),
            Trigram('e', 'n', ' '),
            Trigram('i', 'e', 'n'),
            Trigram('c', 'h', 'o'),
            Trigram('e', 'n', 't'),
            Trigram('e', 'c', 'h'),
            Trigram('c', 'i', 'ó'),
            Trigram('a', 'c', 'i'),
            Trigram('o', ' ', 'a'),
            Trigram('a', ' ', 'p'),
            Trigram(' ', 'e', 'l'),
            Trigram('a', ' ', 'l'),
            Trigram('a', 'l', ' '),
            Trigram('a', 's', ' '),
            Trigram('e', ' ', 'd'),
            Trigram(' ', 'e', 'n'),
            Trigram('n', 'a', ' '),
            Trigram('o', 'n', 'a'),
            Trigram('s', ' ', 'd'),
            Trigram('d', 'a', ' '),
            Trigram('n', 't', 'e'),
            Trigram(' ', 't', 'o'),
            Trigram('a', 'd', ' '),
            Trigram('e', 'n', 'e'),
            Trigram('c', 'o', 'n'),
            Trigram(' ', 'p', 'r'),
            Trigram(' ', 's', 'u'),
            Trigram('t', 'o', 'd'),
            Trigram(' ', 's', 'e'),
            Trigram('h', 'o', ' '),
            Trigram('l', 'o', 's'),
            Trigram(' ', 'p', 'e'),
            Trigram('p', 'e', 'r'),
            Trigram('e', 'r', 's'),
            Trigram(' ', 'l', 'o'),
            Trigram('o', ' ', 'd'),
            Trigram(' ', 't', 'i'),
            Trigram('c', 'i', 'a'),
            Trigram('n', ' ', 'd'),
            Trigram('c', 'i', 'o'),
            Trigram(' ', 'e', 's'),
            Trigram('i', 'd', 'a'),
            Trigram('r', 'e', 's'),
            Trigram('a', ' ', 't'),
            Trigram('t', 'i', 'e'),
            Trigram('i', 'o', 'n'),
            Trigram('r', 's', 'o'),
            Trigram('t', 'e', ' '),
            Trigram('d', 'o', ' '),
            Trigram(' ', 'i', 'n'),
            Trigram('s', 'o', 'n'),
            Trigram(' ', 'r', 'e'),
            Trigram(' ', 'l', 'i'),
            Trigram('t', 'o', ' '),
            Trigram('d', 'a', 'd'),
            Trigram('t', 'a', 'd'),
            Trigram('e', ' ', 's'),
            Trigram('e', 's', 't'),
            Trigram('p', 'r', 'o'),
            Trigram('q', 'u', 'e'),
            Trigram('m', 'e', 'n'),
            Trigram(' ', 'p', 'o'),
            Trigram('a', ' ', 'e'),
            Trigram('o', 'd', 'a'),
            Trigram('n', 'c', 'i'),
            Trigram(' ', 'q', 'u'),
            Trigram(' ', 'u', 'n'),
            Trigram('u', 'e', ' '),
            Trigram('n', 'e', ' '),
            Trigram('n', ' ', 'e'),
            Trigram('s', ' ', 'y'),
            Trigram('l', 'i', 'b'),
            Trigram('s', 'u', ' '),
            Trigram(' ', 'n', 'a'),
            Trigram('s', ' ', 'e'),
            Trigram('n', 'a', 'c'),
            Trigram('i', 'a', ' '),
            Trigram('e', ' ', 'e'),
            Trigram('t', 'r', 'a'),
            Trigram(' ', 'p', 'a'),
            Trigram('o', 'r', ' '),
            Trigram('a', 'd', 'o'),
            Trigram('a', ' ', 'd'),
            Trigram('n', 'e', 's'),
            Trigram('r', 'a', ' '),
            Trigram('s', 'e', ' '),
            Trigram('u', 'a', 'l'),
            Trigram('a', ' ', 'c'),
            Trigram('e', 'r', ' '),
            Trigram('p', 'o', 'r'),
            Trigram('c', 'o', 'm'),
            Trigram('n', 'a', 'l'),
            Trigram('r', 't', 'a'),
            Trigram('a', ' ', 's'),
            Trigram('b', 'e', 'r'),
            Trigram(' ', 'o', ' '),
            Trigram('o', 'n', 'e'),
            Trigram('s', ' ', 'p'),
            Trigram('d', 'o', 's'),
            Trigram('r', 'á', ' '),
            Trigram('s', 't', 'a'),
            Trigram('l', 'e', 's'),
            Trigram('d', 'e', 's'),
            Trigram('i', 'b', 'e'),
            Trigram('s', 'e', 'r'),
            Trigram('e', 'r', 'a'),
            Trigram('a', 'r', ' '),
            Trigram('e', 'r', 't'),
            Trigram('t', 'e', 'r'),
            Trigram(' ', 'd', 'i'),
            Trigram('a', 'l', 'e'),
            Trigram('l', ' ', 'd'),
            Trigram('n', 't', 'o'),
            Trigram('h', 'o', 's'),
            Trigram('d', 'e', 'l'),
            Trigram('i', 'c', 'a'),
            Trigram('a', ' ', 'a'),
            Trigram('s', ' ', 'n'),
            Trigram('n', ' ', 'c'),
            Trigram('o', 'c', 'i'),
            Trigram('i', 'm', 'i'),
            Trigram('i', 'o', ' '),
            Trigram('o', ' ', 'e'),
            Trigram('r', 'e', ' '),
            Trigram('y', ' ', 'l'),
            Trigram('e', ' ', 'c'),
            Trigram('a', 'n', 't'),
            Trigram('c', 'c', 'i'),
            Trigram(' ', 'a', 's'),
            Trigram('l', 'a', 's'),
            Trigram('p', 'a', 'r'),
            Trigram('a', 'm', 'e'),
            Trigram(' ', 'c', 'u'),
            Trigram('i', 'c', 'i'),
            Trigram('a', 'r', 'a'),
            Trigram('e', 'n', 'c'),
            Trigram('s', ' ', 't'),
            Trigram('n', 'd', 'i'),
            Trigram(' ', 's', 'o'),
            Trigram('o', ' ', 's'),
            Trigram('m', 'i', 'e'),
            Trigram('t', 'o', 's'),
            Trigram('u', 'n', 'a'),
            Trigram('b', 'r', 'e'),
            Trigram('d', 'i', 'c'),
            Trigram('c', 'l', 'a'),
            Trigram('s', ' ', 'l'),
            Trigram('e', ' ', 'a'),
            Trigram('l', ' ', 'p'),
            Trigram('p', 'r', 'e'),
            Trigram('n', 't', 'r'),
            Trigram('o', ' ', 't'),
            Trigram('i', 'a', 'l'),
            Trigram('y', ' ', 'a'),
            Trigram('n', 'i', 'd'),
            Trigram('n', ' ', 'p'),
            Trigram('a', ' ', 'y'),
            Trigram('m', 'a', 'n'),
            Trigram('o', 'm', 'o'),
            Trigram('s', 'o', ' '),
            Trigram('n', ' ', 'l'),
            Trigram(' ', 'a', 'l'),
            Trigram('a', 'l', 'i'),
            Trigram('s', ' ', 'a'),
            Trigram('n', 'o', ' '),
            Trigram(' ', 'i', 'g'),
            Trigram('s', ' ', 's'),
            Trigram('e', ' ', 'p'),
            Trigram('n', 't', 'a'),
            Trigram('u', 'm', 'a'),
            Trigram('t', 'e', 'n'),
            Trigram('g', 'u', 'a'),
            Trigram('a', 'd', 'e'),
            Trigram('y', ' ', 'e'),
            Trigram('s', 'o', 'c'),
            Trigram('m', 'o', ' '),
            Trigram(' ', 'f', 'u'),
            Trigram('i', 'g', 'u'),
            Trigram('o', ' ', 'p'),
            Trigram('n', ' ', 't'),
            Trigram('h', 'u', 'm'),
            Trigram('d', ' ', 'd'),
            Trigram('r', 'a', 'n'),
            Trigram('r', 'i', 'a'),
            Trigram('y', ' ', 'd'),
            Trigram('a', 'd', 'a'),
            Trigram('t', 'i', 'v'),
            Trigram('l', ' ', 'e'),
            Trigram('c', 'a', 's'),
            Trigram(' ', 'c', 'a'),
            Trigram('v', 'i', 'd'),
            Trigram('l', ' ', 't'),
            Trigram('s', ' ', 'c'),
            Trigram('i', 'd', 'o'),
            Trigram('d', 'a', 's'),
            Trigram('d', 'i', 's'),
            Trigram('s', ' ', 'i'),
            Trigram(' ', 'h', 'u'),
            Trigram('s', ' ', 'o'),
            Trigram('n', 'a', 'd'),
            Trigram('f', 'u', 'n'),
            Trigram(' ', 'm', 'a'),
            Trigram('r', 'a', 'c'),
            Trigram('n', 'd', 'a'),
            Trigram('e', 'l', 'i'),
            Trigram('s', 'a', 'r'),
            Trigram('u', 'n', 'd'),
            Trigram(' ', 'a', 'c'),
            Trigram('u', 'n', 'i'),
            Trigram('m', 'b', 'r'),
            Trigram('a', ' ', 'u'),
            Trigram('d', 'i', 'e'),
            Trigram('e', ' ', 'i'),
            Trigram('q', 'u', 'i'),
            Trigram('a', ' ', 'i'),
            Trigram(' ', 'h', 'a'),
            Trigram('l', 'a', 'r'),
            Trigram(' ', 't', 'r'),
            Trigram('o', 'd', 'o'),
            Trigram('c', 'a', ' '),
            Trigram('t', 'i', 'c'),
            Trigram('o', ' ', 'y'),
            Trigram('c', 't', 'i'),
            Trigram('l', 'i', 'd'),
            Trigram('o', 'r', 'i'),
            Trigram('n', 'd', 'o'),
            Trigram('a', 'r', 'i'),
            Trigram(' ', 'm', 'e'),
            Trigram('t', 'a', ' '),
            Trigram('i', 'n', 'd'),
            Trigram('e', 's', 'a'),
            Trigram('c', 'u', 'a'),
            Trigram('u', 'n', ' '),
            Trigram('i', 'e', 'r'),
            Trigram('t', 'a', 'l'),
            Trigram('e', 's', 'p'),
            Trigram('s', 'e', 'g'),
            Trigram('e', 'l', 'e'),
            Trigram('o', 'n', 's'),
            Trigram('i', 't', 'o'),
            Trigram('o', 'n', 't'),
            Trigram('i', 'v', 'a'),
            Trigram('s', ' ', 'h'),
            Trigram('d', ' ', 'y'),
            Trigram('n', 'o', 's'),
            Trigram('i', 's', 't'),
            Trigram('r', 's', 'e'),
            Trigram(' ', 'l', 'e'),
            Trigram('c', 'i', 'e'),
            Trigram('i', 'd', 'e'),
            Trigram('e', 'd', 'i'),
            Trigram('e', 'c', 'c'),
            Trigram('i', 'o', 's'),
            Trigram('l', ' ', 'm'),
            Trigram('r', ' ', 'e'),
            Trigram('m', 'e', 'd'),
            Trigram('t', 'o', 'r'),
            Trigram('s', 't', 'i'),
            Trigram('n', ' ', 'a'),
            Trigram('r', 'i', 'm'),
            Trigram('u', 'i', 'e'),
            Trigram('p', 'l', 'e'),
            Trigram('t', 'r', 'i'),
            Trigram('i', 'b', 'r'),
            Trigram('s', 'u', 's'),
            Trigram('l', 'o', ' '),
            Trigram('e', 'c', 't'),
            Trigram('p', 'e', 'n'),
            Trigram('y', ' ', 'c'),
            Trigram('a', 'n', ' '),
            Trigram('e', ' ', 'h'),
            Trigram('n', ' ', 's'),
            Trigram('e', 'r', 'n'),
            Trigram('t', 'a', 'r'),
            Trigram('l', ' ', 'y'),
            Trigram('e', 'g', 'u'),
            Trigram('g', 'u', 'r'),
            Trigram('u', 'r', 'a'),
            Trigram('i', 'n', 't'),
            Trigram('o', 'n', 'd'),
            Trigram('m', 'a', 't'),
            Trigram('l', ' ', 'r'),
            Trigram('r', ' ', 'a'),
            Trigram('i', 's', 'f'),
            Trigram('o', 't', 'e'),
        ],
    ),
    (
        Lang::Eng,
        &[
            Trigram(' ', 't', 'h'),
            Trigram('t', 'h', 'e'),
            Trigram(' ', 'a', 'n'),
            Trigram('h', 'e', ' '),
            Trigram('n', 'd', ' '),
            Trigram('a', 'n', 'd'),
            Trigram('i', 'o', 'n'),
            Trigram(' ', 'o', 'f'),
            Trigram('o', 'f', ' '),
            Trigram('t', 'i', 'o'),
            Trigram(' ', 't', 'o'),
            Trigram('t', 'o', ' '),
            Trigram('o', 'n', ' '),
            Trigram(' ', 'i', 'n'),
            Trigram('a', 'l', ' '),
            Trigram('a', 't', 'i'),
            Trigram('i', 'g', 'h'),
            Trigram('g', 'h', 't'),
            Trigram('r', 'i', 'g'),
            Trigram(' ', 'r', 'i'),
            Trigram('o', 'r', ' '),
            Trigram('e', 'n', 't'),
            Trigram('a', 's', ' '),
            Trigram('e', 'd', ' '),
            Trigram('i', 's', ' '),
            Trigram('l', 'l', ' '),
            Trigram('i', 'n', ' '),
            Trigram(' ', 'b', 'e'),
            Trigram('e', ' ', 'r'),
            Trigram('n', 'e', ' '),
            Trigram('o', 'n', 'e'),
            Trigram('v', 'e', 'r'),
            Trigram('a', 'l', 'l'),
            Trigram('s', ' ', 't'),
            Trigram('e', 'v', 'e'),
            Trigram('t', ' ', 't'),
            Trigram(' ', 'f', 'r'),
            Trigram('s', ' ', 'a'),
            Trigram(' ', 'h', 'a'),
            Trigram(' ', 'r', 'e'),
            Trigram('t', 'y', ' '),
            Trigram('e', 'r', 'y'),
            Trigram(' ', 'o', 'r'),
            Trigram('d', ' ', 't'),
            Trigram(' ', 'p', 'r'),
            Trigram('h', 't', ' '),
            Trigram(' ', 'c', 'o'),
            Trigram(' ', 'e', 'v'),
            Trigram('e', ' ', 'h'),
            Trigram('e', ' ', 'a'),
            Trigram('n', 'g', ' '),
            Trigram('t', 's', ' '),
            Trigram('h', 'i', 's'),
            Trigram('i', 'n', 'g'),
            Trigram('b', 'e', ' '),
            Trigram('y', 'o', 'n'),
            Trigram(' ', 's', 'h'),
            Trigram('c', 'e', ' '),
            Trigram('r', 'e', 'e'),
            Trigram('f', 'r', 'e'),
            Trigram('r', 'y', 'o'),
            Trigram('n', ' ', 't'),
            Trigram('h', 'e', 'r'),
            Trigram('m', 'e', 'n'),
            Trigram('n', 'a', 't'),
            Trigram('s', 'h', 'a'),
            Trigram('p', 'r', 'o'),
            Trigram('n', 'a', 'l'),
            Trigram('y', ' ', 'a'),
            Trigram('h', 'a', 's'),
            Trigram('e', 's', ' '),
            Trigram('f', 'o', 'r'),
            Trigram(' ', 'h', 'i'),
            Trigram('h', 'a', 'l'),
            Trigram('f', ' ', 't'),
            Trigram('n', ' ', 'a'),
            Trigram('n', ' ', 'o'),
            Trigram('n', 't', ' '),
            Trigram(' ', 'p', 'e'),
            Trigram('s', ' ', 'o'),
            Trigram(' ', 'f', 'o'),
            Trigram('d', ' ', 'i'),
            Trigram('n', 'c', 'e'),
            Trigram('e', 'r', ' '),
            Trigram('o', 'n', 's'),
            Trigram('r', 'e', 's'),
            Trigram('e', ' ', 's'),
            Trigram('e', 'c', 't'),
            Trigram('i', 't', 'y'),
            Trigram('l', 'y', ' '),
            Trigram('l', ' ', 'b'),
            Trigram('r', 'y', ' '),
            Trigram('e', ' ', 'e'),
            Trigram('e', 'r', 's'),
            Trigram('e', ' ', 'i'),
            Trigram('a', 'n', ' '),
            Trigram('e', ' ', 'o'),
            Trigram(' ', 'd', 'e'),
            Trigram('c', 't', 'i'),
            Trigram('d', 'o', 'm'),
            Trigram('e', 'd', 'o'),
            Trigram('e', 'e', 'd'),
            Trigram('h', 't', 's'),
            Trigram('t', 'e', 'r'),
            Trigram('o', 'n', 'a'),
            Trigram('r', 'e', ' '),
            Trigram(' ', 'n', 'o'),
            Trigram(' ', 'w', 'h'),
            Trigram(' ', 'a', ' '),
            Trigram(' ', 'u', 'n'),
            Trigram('d', ' ', 'f'),
            Trigram(' ', 'a', 's'),
            Trigram('n', 'y', ' '),
            Trigram('l', ' ', 'a'),
            Trigram('e', ' ', 'p'),
            Trigram('e', 'r', 'e'),
            Trigram(' ', 'e', 'n'),
            Trigram(' ', 'n', 'a'),
            Trigram(' ', 'w', 'i'),
            Trigram('n', 'i', 't'),
            Trigram('n', 't', 'e'),
            Trigram('d', ' ', 'a'),
            Trigram('a', 'n', 'y'),
            Trigram('t', 'e', 'd'),
            Trigram(' ', 'd', 'i'),
            Trigram('n', 's', ' '),
            Trigram('s', 't', 'a'),
            Trigram('t', 'h', ' '),
            Trigram('p', 'e', 'r'),
            Trigram('i', 't', 'h'),
            Trigram('e', ' ', 't'),
            Trigram('s', 't', ' '),
            Trigram('e', ' ', 'c'),
            Trigram('y', ' ', 't'),
            Trigram('o', 'm', ' '),
            Trigram('s', 'o', 'c'),
            Trigram(' ', 'a', 'r'),
            Trigram('c', 'h', ' '),
            Trigram('t', ' ', 'o'),
            Trigram('d', ' ', 'o'),
            Trigram('n', 't', 'i'),
            Trigram('s', ' ', 'e'),
            Trigram('e', 'q', 'u'),
            Trigram('v', 'e', ' '),
            Trigram('o', 'c', 'i'),
            Trigram('m', 'a', 'n'),
            Trigram(' ', 'f', 'u'),
            Trigram('o', 't', 'e'),
            Trigram('o', 't', 'h'),
            Trigram('e', 's', 's'),
            Trigram(' ', 'a', 'l'),
            Trigram(' ', 'a', 'c'),
            Trigram('w', 'i', 't'),
            Trigram('i', 'a', 'l'),
            Trigram(' ', 'm', 'a'),
            Trigram('u', 'n', 'i'),
            Trigram(' ', 's', 'e'),
            Trigram('r', 'e', 'a'),
            Trigram(' ', 's', 'o'),
            Trigram(' ', 'o', 'n'),
            Trigram('l', 'i', 't'),
            Trigram('i', 'n', 't'),
            Trigram('r', ' ', 't'),
            Trigram('y', ' ', 'o'),
            Trigram('e', 'n', 'c'),
            Trigram('t', 'h', 'i'),
            Trigram('u', 'a', 'l'),
            Trigram('t', ' ', 'a'),
            Trigram(' ', 'e', 'q'),
            Trigram('t', 'a', 't'),
            Trigram('q', 'u', 'a'),
            Trigram('i', 'v', 'e'),
            Trigram(' ', 's', 't'),
            Trigram('a', 'l', 'i'),
            Trigram('e', ' ', 'w'),
            Trigram('l', ' ', 'o'),
            Trigram('a', 'r', 'e'),
            Trigram('f', ' ', 'h'),
            Trigram('c', 'o', 'n'),
            Trigram('t', 'e', ' '),
            Trigram('l', 'e', 'd'),
            Trigram(' ', 'i', 's'),
            Trigram('u', 'n', 'd'),
            Trigram('c', 'i', 'a'),
            Trigram('e', ' ', 'f'),
            Trigram('l', 'e', ' '),
            Trigram(' ', 'l', 'a'),
            Trigram('y', ' ', 'i'),
            Trigram('u', 'm', 'a'),
            Trigram('b', 'y', ' '),
            Trigram(' ', 'b', 'y'),
            Trigram('h', 'u', 'm'),
            Trigram('f', ' ', 'a'),
            Trigram('i', 'c', ' '),
            Trigram(' ', 'h', 'u'),
            Trigram('a', 'v', 'e'),
            Trigram('g', 'e', ' '),
            Trigram('r', ' ', 'a'),
            Trigram(' ', 'w', 'o'),
            Trigram('o', ' ', 'a'),
            Trigram('m', 's', ' '),
            Trigram('c', 'o', 'm'),
            Trigram(' ', 'm', 'e'),
            Trigram('e', 'a', 's'),
            Trigram('s', ' ', 'd'),
            Trigram('t', 'e', 'c'),
            Trigram(' ', 'l', 'i'),
            Trigram('n', ' ', 'e'),
            Trigram('e', 'n', ' '),
            Trigram('r', 'a', 't'),
            Trigram('t', 'i', 't'),
            Trigram('p', 'l', 'e'),
            Trigram('w', 'h', 'e'),
            Trigram('a', 't', 'e'),
            Trigram('o', ' ', 't'),
            Trigram('s', ' ', 'r'),
            Trigram('t', ' ', 'f'),
            Trigram('r', 'o', 't'),
            Trigram(' ', 'c', 'h'),
            Trigram('c', 'i', 'e'),
            Trigram('d', 'i', 's'),
            Trigram('a', 'g', 'e'),
            Trigram('a', 'r', 'y'),
            Trigram('o', ' ', 'o'),
            Trigram('a', 'n', 'c'),
            Trigram('e', 'l', 'i'),
            Trigram('n', 'o', ' '),
            Trigram(' ', 'f', 'a'),
            Trigram(' ', 's', 'u'),
            Trigram('s', 'o', 'n'),
            Trigram('i', 'n', 'c'),
            Trigram('a', 't', ' '),
            Trigram('n', 'd', 'a'),
            Trigram('h', 'o', 'u'),
            Trigram('w', 'o', 'r'),
            Trigram('t', ' ', 'i'),
            Trigram('n', 'd', 'e'),
            Trigram('r', 'o', 'm'),
            Trigram('o', 'm', 's'),
            Trigram(' ', 'o', 't'),
            Trigram('g', ' ', 't'),
            Trigram('e', 'm', 'e'),
            Trigram('t', 'l', 'e'),
            Trigram('i', 't', 'i'),
            Trigram('g', 'n', 'i'),
            Trigram('s', ' ', 'w'),
            Trigram('i', 't', 'l'),
            Trigram('d', 'u', 'c'),
            Trigram('d', ' ', 'w'),
            Trigram('w', 'h', 'i'),
            Trigram('a', 'c', 't'),
            Trigram('h', 'i', 'c'),
            Trigram('a', 'w', ' '),
            Trigram('l', 'a', 'w'),
            Trigram(' ', 'h', 'e'),
            Trigram('i', 'c', 'h'),
            Trigram('m', 'i', 'n'),
            Trigram('i', 'm', 'i'),
            Trigram('o', 'r', 't'),
            Trigram('o', ' ', 's'),
            Trigram('s', 'e', ' '),
            Trigram('e', ' ', 'b'),
            Trigram('n', 't', 'r'),
            Trigram('t', 'r', 'a'),
            Trigram('e', 'd', 'u'),
            Trigram('o', 'u', 'n'),
            Trigram('t', 'a', 'n'),
            Trigram('e', ' ', 'd'),
            Trigram('n', 's', 't'),
            Trigram('l', ' ', 'p'),
            Trigram('d', ' ', 'n'),
            Trigram('l', 'd', ' '),
            Trigram('n', 't', 'a'),
            Trigram('s', ' ', 'i'),
            Trigram('b', 'l', 'e'),
            Trigram('n', ' ', 'p'),
            Trigram(' ', 'p', 'u'),
            Trigram('n', ' ', 's'),
            Trigram(' ', 'a', 't'),
            Trigram('i', 'l', 'y'),
            Trigram('r', 't', 'h'),
            Trigram('t', 'h', 'o'),
            Trigram('f', 'u', 'l'),
            Trigram('s', 's', 'i'),
            Trigram('d', 'e', 'r'),
            Trigram('o', ' ', 'e'),
            Trigram('c', 'a', 't'),
            Trigram('u', 'c', 'a'),
            Trigram('u', 'n', 't'),
            Trigram('i', 'e', 'n'),
            Trigram(' ', 'e', 'd'),
            Trigram('o', ' ', 'p'),
            Trigram('h', ' ', 'a'),
            Trigram('e', 'r', 'a'),
            Trigram('i', 'n', 'd'),
            Trigram('p', 'e', 'n'),
            Trigram('s', 'e', 'c'),
            Trigram('n', ' ', 'w'),
            Trigram('o', 'm', 'm'),
            Trigram('r', ' ', 's'),
        ],
    ),
    (
        Lang::Por,
        &[
            Trigram('o', 's', ' '),
            Trigram('d', 'e', ' '),
            Trigram(' ', 'd', 'e'),
            Trigram(' ', 'a', ' '),
            Trigram(' ', 'e', ' '),
            Trigram('o', ' ', 'd'),
            Trigram('t', 'o', ' '),
            Trigram('ã', 'o', ' '),
            Trigram(' ', 'd', 'i'),
            Trigram('e', 'n', 't'),
            Trigram('d', 'a', ' '),
            Trigram('i', 't', 'o'),
            Trigram('e', 'm', ' '),
            Trigram(' ', 'c', 'o'),
            Trigram('e', 'i', 't'),
            Trigram('a', 's', ' '),
            Trigram('d', 'i', 'r'),
            Trigram('e', 's', ' '),
            Trigram('i', 'r', 'e'),
            Trigram('r', 'e', 'i'),
            Trigram(' ', 's', 'e'),
            Trigram('ç', 'ã', 'o'),
            Trigram('a', 'd', 'e'),
            Trigram('a', ' ', 'p'),
            Trigram('d', 'a', 'd'),
            Trigram('e', ' ', 'd'),
            Trigram('s', ' ', 'd'),
            Trigram('m', 'e', 'n'),
            Trigram('n', 't', 'e'),
            Trigram('d', 'o', ' '),
            Trigram('s', ' ', 'e'),
            Trigram(' ', 'p', 'r'),
            Trigram(' ', 'p', 'e'),
            Trigram('d', 'o', 's'),
            Trigram(' ', 't', 'o'),
            Trigram(' ', 'd', 'a'),
            Trigram('a', ' ', 'a'),
            Trigram('o', ' ', 'e'),
            Trigram(' ', 'o', ' '),
            Trigram('o', ' ', 'a'),
            Trigram('e', 's', 's'),
            Trigram('c', 'o', 'n'),
            Trigram('t', 'o', 'd'),
            Trigram('q', 'u', 'e'),
            Trigram(' ', 'q', 'u'),
            Trigram('t', 'e', ' '),
            Trigram('e', ' ', 'a'),
            Trigram(' ', 'd', 'o'),
            Trigram('a', 'l', ' '),
            Trigram('r', 'e', 's'),
            Trigram('i', 'd', 'a'),
            Trigram('m', ' ', 'd'),
            Trigram(' ', 'i', 'n'),
            Trigram(' ', 'o', 'u'),
            Trigram('e', 'r', ' '),
            Trigram('s', 's', 'o'),
            Trigram(' ', 'n', 'a'),
            Trigram(' ', 'r', 'e'),
            Trigram(' ', 'p', 'o'),
            Trigram('a', ' ', 's'),
            Trigram(' ', 'l', 'i'),
            Trigram('u', 'm', 'a'),
            Trigram('c', 'i', 'a'),
            Trigram('a', 'r', ' '),
            Trigram('p', 'r', 'o'),
            Trigram('e', ' ', 'e'),
            Trigram('a', ' ', 'd'),
            Trigram(' ', 't', 'e'),
            Trigram('a', 'ç', 'ã'),
            Trigram('a', ' ', 't'),
            Trigram(' ', 'e', 's'),
            Trigram(' ', 's', 'u'),
            Trigram('o', 'u', ' '),
            Trigram('u', 'e', ' '),
            Trigram('s', ' ', 'p'),
            Trigram('t', 'o', 's'),
            Trigram('a', ' ', 'e'),
            Trigram('d', 'e', 's'),
            Trigram('r', 'a', ' '),
            Trigram('c', 'o', 'm'),
            Trigram('n', 'o', ' '),
            Trigram('a', 'm', 'e'),
            Trigram('i', 'a', ' '),
            Trigram('e', ' ', 'p'),
            Trigram('t', 'e', 'm'),
            Trigram('n', 't', 'o'),
            Trigram(' ', 'p', 'a'),
            Trigram('i', 's', ' '),
            Trigram('e', 's', 't'),
            Trigram('t', 'r', 'a'),
            Trigram('õ', 'e', 's'),
            Trigram('n', 'a', ' '),
            Trigram('s', ' ', 'o'),
            Trigram('o', 'd', 'a'),
            Trigram('d', 'a', 's'),
            Trigram('s', 'e', 'r'),
            Trigram('s', 'o', 'a'),
            Trigram('s', ' ', 'n'),
            Trigram('p', 'e', 's'),
            Trigram('o', ' ', 'p'),
            Trigram('s', ' ', 'a'),
            Trigram('o', ' ', 's'),
            Trigram('e', ' ', 'o'),
            Trigram(' ', 'e', 'm'),
            Trigram(' ', 'a', 's'),
            Trigram(' ', 'à', ' '),
            Trigram('o', ' ', 'o'),
            Trigram('a', 'i', 's'),
            Trigram('b', 'e', 'r'),
            Trigram('a', 'd', 'o'),
            Trigram('o', 'a', ' '),
            Trigram('o', ' ', 't'),
            Trigram('e', ' ', 's'),
            Trigram('m', 'a', 'n'),
            Trigram('s', 'u', 'a'),
            Trigram('u', 'a', ' '),
            Trigram(' ', 'n', 'o'),
            Trigram(' ', 'o', 's'),
            Trigram('a', ' ', 'c'),
            Trigram('t', 'e', 'r'),
            Trigram('ç', 'õ', 'e'),
            Trigram('e', 'r', 'd'),
            Trigram('l', 'i', 'b'),
            Trigram('r', 'd', 'a'),
            Trigram('s', ' ', 's'),
            Trigram('n', 'c', 'i'),
            Trigram('i', 'b', 'e'),
            Trigram('e', ' ', 'n'),
            Trigram('i', 'c', 'a'),
            Trigram('o', 'd', 'o'),
            Trigram('s', 'o', ' '),
            Trigram('n', 'a', 'l'),
            Trigram('n', 't', 'r'),
            Trigram('s', ' ', 't'),
            Trigram('h', 'u', 'm'),
            Trigram('u', 'r', 'a'),
            Trigram(' ', 'a', 'o'),
            Trigram('o', 'n', 'a'),
            Trigram('u', 'a', 'l'),
            Trigram(' ', 's', 'o'),
            Trigram('o', 'r', ' '),
            Trigram('m', 'a', ' '),
            Trigram('s', 't', 'a'),
            Trigram('o', ' ', 'c'),
            Trigram('a', ' ', 'n'),
            Trigram('p', 'r', 'e'),
            Trigram('a', 'r', 'a'),
            Trigram('e', 'r', 'a'),
            Trigram('o', 'n', 's'),
            Trigram('e', ' ', 't'),
            Trigram('r', ' ', 'a'),
            Trigram('p', 'a', 'r'),
            Trigram('o', ' ', 'à'),
            Trigram(' ', 'h', 'u'),
            Trigram('i', 'n', 'd'),
            Trigram('p', 'o', 'r'),
            Trigram('c', 'i', 'o'),
            Trigram('r', 'i', 'a'),
            Trigram('m', ' ', 'a'),
            Trigram('s', ' ', 'c'),
            Trigram(' ', 'u', 'm'),
            Trigram('a', ' ', 'l'),
            Trigram('g', 'u', 'a'),
            Trigram('r', 'a', 'n'),
            Trigram(' ', 'e', 'n'),
            Trigram('n', 'd', 'i'),
            Trigram('o', ' ', 'i'),
            Trigram('e', ' ', 'c'),
            Trigram('r', 'a', 'ç'),
            Trigram('i', 'o', 'n'),
            Trigram('n', 'i', 'd'),
            Trigram('a', 'c', 'i'),
            Trigram('a', 'n', 'o'),
            Trigram('s', 'o', 'c'),
            Trigram('e', ' ', 'r'),
            Trigram('o', 'c', 'i'),
            Trigram(' ', 'a', 'c'),
            Trigram('u', 'n', 'd'),
            Trigram('s', 'e', 'n'),
            Trigram('n', 'o', 's'),
            Trigram('n', 's', 'i'),
            Trigram('r', 'e', 'c'),
            Trigram('i', 'm', 'e'),
            Trigram('a', 'l', 'i'),
            Trigram('i', 'n', 't'),
            Trigram('u', 'm', ' '),
            Trigram('p', 'e', 'r'),
            Trigram('n', 'a', 'c'),
            Trigram(' ', 'a', 'l'),
            Trigram('m', ' ', 'o'),
            Trigram('r', ' ', 'p'),
            Trigram(' ', 'f', 'u'),
            Trigram('n', 'd', 'o'),
            Trigram('o', 'n', 't'),
            Trigram('a', 'ç', 'õ'),
            Trigram(' ', 'i', 'g'),
            Trigram('i', 'g', 'u'),
            Trigram('f', 'u', 'n'),
            Trigram('n', 't', 'a'),
            Trigram(' ', 'm', 'a'),
            Trigram('u', 'n', 'i'),
            Trigram('c', 'ç', 'ã'),
            Trigram('e', 'r', 'e'),
            Trigram(' ', 'e', 'x'),
            Trigram('a', ' ', 'i'),
            Trigram(' ', 'm', 'e'),
            Trigram('e', 's', 'e'),
            Trigram('r', 'i', 'o'),
            Trigram('l', ' ', 'd'),
            Trigram('a', ' ', 'o'),
            Trigram('s', ' ', 'h'),
            Trigram('p', 'e', 'l'),
            Trigram('a', 'd', 'a'),
            Trigram('p', 'r', 'i'),
            Trigram('i', 'd', 'e'),
            Trigram('a', 'm', ' '),
            Trigram('m', ' ', 'p'),
            Trigram('p', 'o', 'd'),
            Trigram('s', ' ', 'f'),
            Trigram('é', 'm', ' '),
            Trigram('a', ' ', 'f'),
            Trigram('i', 'o', ' '),
            Trigram('o', 'd', 'e'),
            Trigram('c', 'a', ' '),
            Trigram('i', 't', 'a'),
            Trigram('l', 'i', 'd'),
            Trigram('t', 'i', 'v'),
            Trigram('e', ' ', 'f'),
            Trigram('v', 'i', 'd'),
            Trigram('r', ' ', 'e'),
            Trigram('e', 's', 'p'),
            Trigram('n', 'd', 'a'),
            Trigram('o', 'm', 'o'),
            Trigram('e', ' ', 'l'),
            Trigram('n', 'a', 'ç'),
            Trigram('o', ' ', 'r'),
            Trigram('a', 'n', 't'),
            Trigram('a', ' ', 'q'),
            Trigram('t', 'a', 'd'),
            Trigram('l', 'i', 'c'),
            Trigram('i', 'v', 'a'),
            Trigram(' ', 'f', 'a'),
            Trigram('v', 'e', 'r'),
            Trigram('s', ' ', 'l'),
            Trigram('i', 'a', 'l'),
            Trigram('c', 'l', 'a'),
            Trigram('n', 'g', 'u'),
            Trigram('i', 'n', 'g'),
            Trigram(' ', 'c', 'a'),
            Trigram('m', 'o', ' '),
            Trigram('d', 'e', 'r'),
            Trigram(' ', 'v', 'i'),
            Trigram('e', 'l', 'i'),
            Trigram('i', 's', 't'),
            Trigram('t', 'a', ' '),
            Trigram('s', 'e', ' '),
            Trigram('a', 't', 'i'),
            Trigram('i', 'o', 's'),
            Trigram('i', 'd', 'o'),
            Trigram('r', ' ', 'o'),
            Trigram('e', 'c', 'i'),
            Trigram('d', 'i', 's'),
            Trigram(' ', 'u', 'n'),
            Trigram('e', ' ', 'i'),
            Trigram('r', ' ', 'd'),
            Trigram('e', 'c', 'ç'),
            Trigram('o', ' ', 'q'),
            Trigram('s', ' ', 'i'),
            Trigram('q', 'u', 'a'),
            Trigram('ê', 'n', 'c'),
            Trigram('a', ' ', 'm'),
            Trigram('s', 'e', 'u'),
            Trigram('s', 't', 'i'),
            Trigram('n', 'i', 'n'),
            Trigram('u', 'e', 'r'),
            Trigram('r', 'a', 'r'),
            Trigram('c', 'a', 's'),
            Trigram('a', 'o', 's'),
            Trigram('e', 'n', 's'),
            Trigram('g', 'u', 'é'),
            Trigram('i', 'a', 's'),
            Trigram('s', 'i', 'd'),
            Trigram('u', 'é', 'm'),
            Trigram('t', 'u', 'r'),
            Trigram('d', 'a', 'm'),
            Trigram('s', 's', 'e'),
            Trigram('a', 'o', ' '),
            Trigram('e', 'l', 'a'),
            Trigram('l', ' ', 'e'),
            Trigram('f', 'o', 'r'),
            Trigram('t', 'e', 'c'),
            Trigram('o', 't', 'e'),
            Trigram(' ', 'p', 'l'),
            Trigram('e', 'n', 'a'),
            Trigram(' ', 't', 'r'),
            Trigram('m', ' ', 'c'),
            Trigram('t', 'r', 'o'),
            Trigram(' ', 'n', 'i'),
            Trigram('i', 'c', 'o'),
            Trigram('r', 'o', 't'),
        ],
    ),
    (
        Lang::Ind,
        &[
            Trigram('a', 'n', ' '),
            Trigram('a', 'n', 'g'),
            Trigram(' ', 'd', 'a'),
            Trigram('n', 'g', ' '),
            Trigram(' ', 'p', 'e'),
            Trigram('a', 'k', ' '),
            Trigram(' ', 'k', 'e'),
            Trigram(' ', 'm', 'e'),
            Trigram('a', 't', 'a'),
            Trigram(' ', 's', 'e'),
            Trigram('d', 'a', 'n'),
            Trigram('k', 'a', 'n'),
            Trigram(' ', 'd', 'i'),
            Trigram(' ', 'b', 'e'),
            Trigram('h', 'a', 'k'),
            Trigram('b', 'e', 'r'),
            Trigram('p', 'e', 'r'),
            Trigram('r', 'a', 'n'),
            Trigram('n', 'g', 'a'),
            Trigram('y', 'a', 'n'),
            Trigram('e', 'n', 'g'),
            Trigram(' ', 'y', 'a'),
            Trigram(' ', 'h', 'a'),
            Trigram('a', 's', 'a'),
            Trigram('g', 'a', 'n'),
            Trigram('m', 'e', 'n'),
            Trigram('a', 'r', 'a'),
            Trigram('n', 'y', 'a'),
            Trigram('n', ' ', 'p'),
            Trigram('n', ' ', 'd'),
            Trigram('n', ' ', 'k'),
            Trigram('a', ' ', 'd'),
            Trigram('t', 'a', 'n'),
            Trigram(' ', 'a', 't'),
            Trigram('a', 't', ' '),
            Trigram('o', 'r', 'a'),
            Trigram('a', 'l', 'a'),
            Trigram('s', 'a', 'n'),
            Trigram(' ', 'b', 'a'),
            Trigram('a', 'p', ' '),
            Trigram('e', 'r', 'h'),
            Trigram('n', ' ', 'b'),
            Trigram('r', 'h', 'a'),
            Trigram('y', 'a', ' '),
            Trigram(' ', 'm', 'a'),
            Trigram('g', ' ', 'b'),
            Trigram('a', ' ', 's'),
            Trigram('p', 'e', 'n'),
            Trigram('e', 'b', 'a'),
            Trigram('a', 's', ' '),
            Trigram('a', 'a', 'n'),
            Trigram('u', 'k', ' '),
            Trigram('n', 't', 'u'),
            Trigram(' ', 'o', 'r'),
            Trigram('e', 't', 'i'),
            Trigram('t', 'a', 's'),
            Trigram('a', 'k', 'a'),
            Trigram('t', 'i', 'a'),
            Trigram('b', 'a', 'n'),
            Trigram('s', 'e', 't'),
            Trigram(' ', 'u', 'n'),
            Trigram('n', ' ', 's'),
            Trigram('t', 'e', 'r'),
            Trigram('n', ' ', 'y'),
            Trigram(' ', 't', 'e'),
            Trigram('k', ' ', 'm'),
            Trigram('t', 'u', 'k'),
            Trigram('b', 'a', 's'),
            Trigram('i', 'a', 'p'),
            Trigram('l', 'a', 'm'),
            Trigram('b', 'e', 'b'),
            Trigram('a', 'm', ' '),
            Trigram(' ', 'd', 'e'),
            Trigram('k', ' ', 'a'),
            Trigram('k', 'e', 'b'),
            Trigram('n', ' ', 'm'),
            Trigram('i', ' ', 'd'),
            Trigram('u', 'n', 't'),
            Trigram('a', 'm', 'a'),
            Trigram('d', 'a', 'l'),
            Trigram('a', 'h', ' '),
            Trigram('i', 'k', 'a'),
            Trigram('d', 'a', 'k'),
            Trigram('e', 'b', 'e'),
            Trigram('p', ' ', 'o'),
            Trigram('s', 'a', ' '),
            Trigram('p', 'u', 'n'),
            Trigram('m', 'e', 'm'),
            Trigram('n', ' ', 'h'),
            Trigram('e', 'n', 'd'),
            Trigram('d', 'e', 'n'),
            Trigram('r', 'a', ' '),
            Trigram('e', 'l', 'a'),
            Trigram('r', 'i', ' '),
            Trigram('n', 'd', 'a'),
            Trigram(' ', 's', 'a'),
            Trigram('d', 'i', ' '),
            Trigram('m', 'a', ' '),
            Trigram('a', ' ', 'm'),
            Trigram('n', ' ', 't'),
            Trigram('k', ' ', 'd'),
            Trigram('n', ' ', 'a'),
            Trigram('n', 'g', 'g'),
            Trigram('t', 'a', 'u'),
            Trigram('m', 'a', 'n'),
            Trigram('g', 'a', 'r'),
            Trigram('e', 'r', 'i'),
            Trigram('a', 's', 'i'),
            Trigram(' ', 't', 'i'),
            Trigram('u', 'n', ' '),
            Trigram('a', 'l', ' '),
            Trigram('a', 'd', 'a'),
            Trigram('u', 'm', ' '),
            Trigram('a', ' ', 'p'),
            Trigram('l', 'a', 'k'),
            Trigram('a', 'r', 'i'),
            Trigram('a', 'u', ' '),
            Trigram(' ', 'n', 'e'),
            Trigram('n', 'e', 'g'),
            Trigram('a', ' ', 'b'),
            Trigram('n', 'g', 's'),
            Trigram('t', 'a', ' '),
            Trigram('o', 'l', 'e'),
            Trigram('l', 'e', 'h'),
            Trigram('e', 'r', 't'),
            Trigram('e', 'r', 's'),
            Trigram('i', 'd', 'a'),
            Trigram('k', ' ', 'h'),
            Trigram('a', 'n', 'a'),
            Trigram('g', 's', 'a'),
            Trigram('d', 'a', 'r'),
            Trigram('u', 'k', 'a'),
            Trigram('t', 'i', 'd'),
            Trigram('b', 'a', 't'),
            Trigram('s', 'i', 'a'),
            Trigram('e', 'r', 'a'),
            Trigram('e', 'h', ' '),
            Trigram('d', 'a', 'p'),
            Trigram('i', 'l', 'a'),
            Trigram('d', 'i', 'l'),
            Trigram('h', ' ', 'd'),
            Trigram('a', 't', 'u'),
            Trigram('s', 'a', 'm'),
            Trigram('i', 'a', ' '),
            Trigram('i', ' ', 'm'),
            Trigram(' ', 'i', 'n'),
            Trigram('l', 'a', 'n'),
            Trigram('a', 'h', 'a'),
            Trigram('u', 'a', 'n'),
            Trigram('t', 'u', ' '),
            Trigram('a', 'i', ' '),
            Trigram('t', ' ', 'd'),
            Trigram('a', ' ', 'a'),
            Trigram('g', ' ', 'd'),
            Trigram('h', 'a', 'r'),
            Trigram('s', 'e', 'm'),
            Trigram('n', 'a', ' '),
            Trigram('a', 'p', 'a'),
            Trigram('s', 'e', 'r'),
            Trigram('e', 'n', 'a'),
            Trigram('k', 'a', 't'),
            Trigram('u', 'a', 't'),
            Trigram('e', 'r', 'b'),
            Trigram('e', 'r', 'l'),
            Trigram('m', 'a', 's'),
            Trigram('r', 't', 'a'),
            Trigram('e', 'g', 'a'),
            Trigram('u', 'n', 'g'),
            Trigram('n', 'a', 'n'),
            Trigram('e', 'm', 'p'),
            Trigram('n', ' ', 'u'),
            Trigram('k', 'u', 'm'),
            Trigram('l', ' ', 'd'),
            Trigram('g', ' ', 's'),
            Trigram(' ', 'h', 'u'),
            Trigram('k', 'a', ' '),
            Trigram('e', 'n', 't'),
            Trigram('p', 'a', 't'),
            Trigram('m', 'b', 'a'),
            Trigram('a', 'g', 'a'),
            Trigram('n', 't', 'a'),
            Trigram('a', 'd', 'i'),
            Trigram(' ', 's', 'u'),
            Trigram('e', 'n', 'i'),
            Trigram('u', 'k', 'u'),
            Trigram('n', ' ', 'i'),
            Trigram('h', 'u', 'k'),
            Trigram('i', 'n', 'd'),
            Trigram('a', 'r', ' '),
            Trigram('r', 'g', 'a'),
            Trigram('i', ' ', 's'),
            Trigram('a', 'k', 'u'),
            Trigram('n', 'd', 'i'),
            Trigram('s', 'u', 'a'),
            Trigram('n', 'i', ' '),
            Trigram('r', 'u', 's'),
            Trigram('h', 'a', 'n'),
            Trigram('s', 'i', ' '),
            Trigram('c', 'a', 'r'),
            Trigram('n', 'n', 'y'),
            Trigram(' ', 'l', 'a'),
            Trigram('i', 'n', ' '),
            Trigram('u', ' ', 'd'),
            Trigram('i', 'k', ' '),
            Trigram('u', 'a', ' '),
            Trigram('l', 'a', 'h'),
            Trigram('r', 'i', 'k'),
            Trigram('u', 's', 'i'),
            Trigram('e', 'm', 'b'),
            Trigram('a', 'n', 'n'),
            Trigram('m', 'e', 'r'),
            Trigram('i', 'a', 'n'),
            Trigram('g', 'g', 'a'),
            Trigram('l', 'a', 'i'),
            Trigram('m', 'i', 'n'),
            Trigram('a', ' ', 'u'),
            Trigram('l', 'u', 'a'),
            Trigram('e', 'm', 'a'),
            Trigram('e', 'm', 'u'),
            Trigram('a', 'r', 'g'),
            Trigram('d', 'u', 'n'),
            Trigram('d', 'i', 'p'),
            Trigram('a', ' ', 't'),
            Trigram('m', 'a', 't'),
            Trigram('a', 'y', 'a'),
            Trigram('r', 'b', 'u'),
            Trigram('a', 'r', 'u'),
            Trigram('e', 'r', 'k'),
            Trigram('r', 'k', 'a'),
            Trigram('i', 'n', 'i'),
            Trigram('e', 'k', 'a'),
            Trigram('a', ' ', 'k'),
            Trigram('r', 'a', 'k'),
            Trigram('k', 'e', 's'),
            Trigram('y', 'a', 't'),
            Trigram('i', 'b', 'a'),
            Trigram('n', 'a', 's'),
            Trigram('r', 'm', 'a'),
            Trigram('e', 'r', 'n'),
            Trigram('e', 's', 'e'),
            Trigram('s', ' ', 'p'),
            Trigram('n', 'u', 's'),
            Trigram(' ', 'p', 'u'),
            Trigram('a', 'n', 'u'),
            Trigram('i', 'n', 'a'),
            Trigram(' ', 't', 'a'),
            Trigram('m', 'e', 'l'),
            Trigram('m', 'u', 'a'),
            Trigram('k', 'e', 'l'),
            Trigram('k', ' ', 's'),
            Trigram('u', 's', ' '),
            Trigram('n', 'd', 'u'),
            Trigram('n', 'a', 'k'),
            Trigram('d', 'a', ' '),
            Trigram('s', 'y', 'a'),
            Trigram('d', 'a', 's'),
            Trigram('p', 'e', 'm'),
            Trigram('l', 'i', 'n'),
            Trigram('u', 't', ' '),
            Trigram('y', 'a', 'r'),
            Trigram('a', 'm', 'i'),
            Trigram('u', 'p', 'u'),
            Trigram('s', 'e', 'o'),
            Trigram('a', 'i', 'k'),
            Trigram('e', 'o', 'r'),
            Trigram('i', 'n', 'y'),
            Trigram('a', 'u', 'p'),
            Trigram('t', 'a', 'k'),
            Trigram('i', 'p', 'e'),
            Trigram('i', 'n', 'g'),
            Trigram('t', 'i', 'n'),
            Trigram(' ', 'a', 'n'),
            Trigram('d', 'i', 'k'),
            Trigram('u', 'a', 'r'),
            Trigram('i', 'l', 'i'),
            Trigram('g', ' ', 't'),
            Trigram('r', 's', 'e'),
            Trigram('s', 'a', 'r'),
            Trigram('a', 'n', 't'),
            Trigram('g', ' ', 'p'),
            Trigram('a', ' ', 'n'),
            Trigram('a', 'k', 's'),
            Trigram('a', 'i', 'n'),
            Trigram(' ', 'j', 'a'),
            Trigram('t', ' ', 'p'),
            Trigram(' ', 'u', 'm'),
            Trigram('g', ' ', 'm'),
            Trigram('d', 'i', 'r'),
            Trigram('k', 's', 'a'),
            Trigram('u', 'm', 'u'),
            Trigram('k', 'e', 'p'),
            Trigram('m', 'u', 'm'),
            Trigram('i', ' ', 'k'),
            Trigram('e', 'c', 'a'),
            Trigram('r', 'a', 't'),
            Trigram('m', ' ', 'p'),
            Trigram('h', ' ', 'p'),
            Trigram('a', 'b', 'a'),
            Trigram('s', 'e', 's'),
            Trigram('m', ' ', 'm'),
        ],
    ),
    (
        Lang::Fra,
        &[
            Trigram(' ', 'd', 'e'),
            Trigram('e', 's', ' '),
            Trigram('d', 'e', ' '),
            Trigram('i', 'o', 'n'),
            Trigram('n', 't', ' '),
            Trigram('e', 't', ' '),
            Trigram('t', 'i', 'o'),
            Trigram(' ', 'e', 't'),
            Trigram('e', 'n', 't'),
            Trigram(' ', 'l', 'a'),
            Trigram('l', 'a', ' '),
            Trigram('e', ' ', 'd'),
            Trigram('o', 'n', ' '),
            Trigram('n', 'e', ' '),
            Trigram('o', 'i', 't'),
            Trigram('e', ' ', 'l'),
            Trigram('l', 'e', ' '),
            Trigram(' ', 'l', 'e'),
            Trigram('s', ' ', 'd'),
            Trigram('e', ' ', 'p'),
            Trigram('t', ' ', 'd'),
            Trigram('a', 't', 'i'),
            Trigram('r', 'o', 'i'),
            Trigram(' ', 'd', 'r'),
            Trigram('d', 'r', 'o'),
            Trigram('i', 't', ' '),
            Trigram(' ', 'à', ' '),
            Trigram(' ', 'c', 'o'),
            Trigram('t', 'é', ' '),
            Trigram('n', 's', ' '),
            Trigram('t', 'e', ' '),
            Trigram('e', ' ', 's'),
            Trigram('m', 'e', 'n'),
            Trigram('r', 'e', ' '),
            Trigram(' ', 't', 'o'),
            Trigram('c', 'o', 'n'),
            Trigram(' ', 'l', '’'),
            Trigram('t', 'o', 'u'),
            Trigram('q', 'u', 'e'),
            Trigram(' ', 'q', 'u'),
            Trigram('l', 'e', 's'),
            Trigram(' ', 's', 'o'),
            Trigram('d', 'e', 's'),
            Trigram('s', 'o', 'n'),
            Trigram(' ', 'p', 'e'),
            Trigram('o', 'n', 's'),
            Trigram(' ', 'u', 'n'),
            Trigram('s', ' ', 'l'),
            Trigram('s', ' ', 'e'),
            Trigram(' ', 'p', 'r'),
            Trigram('u', 'e', ' '),
            Trigram(' ', 'p', 'a'),
            Trigram('e', ' ', 'c'),
            Trigram('t', ' ', 'l'),
            Trigram('t', 's', ' '),
            Trigram('o', 'n', 'n'),
            Trigram(' ', 'a', 'u'),
            Trigram('e', ' ', 'a'),
            Trigram('e', 'm', 'e'),
            Trigram('e', ' ', 'e'),
            Trigram(' ', 'l', 'i'),
            Trigram('o', 'n', 't'),
            Trigram('a', 'n', 't'),
            Trigram('o', 'u', 't'),
            Trigram('u', 't', 'e'),
            Trigram('t', ' ', 'à'),
            Trigram('r', 'e', 's'),
            Trigram('e', 'r', 's'),
            Trigram(' ', 's', 'a'),
            Trigram('c', 'e', ' '),
            Trigram(' ', 'a', ' '),
            Trigram('t', 'r', 'e'),
            Trigram('p', 'e', 'r'),
            Trigram('a', ' ', 'd'),
            Trigram('c', 't', 'i'),
            Trigram('e', 'r', ' '),
            Trigram('l', 'i', 'b'),
            Trigram('i', 't', 'é'),
            Trigram(' ', 'e', 'n'),
            Trigram('u', 'x', ' '),
            Trigram(' ', 'r', 'e'),
            Trigram('e', 'n', ' '),
            Trigram('r', 's', 'o'),
            Trigram('à', ' ', 'l'),
            Trigram(' ', 'o', 'u'),
            Trigram(' ', 'i', 'n'),
            Trigram('l', 'l', 'e'),
            Trigram('u', 'n', ' '),
            Trigram('n', 'a', 't'),
            Trigram('o', 'u', ' '),
            Trigram('n', 'n', 'e'),
            Trigram('n', ' ', 'd'),
            Trigram('u', 'n', 'e'),
            Trigram(' ', 'd', '’'),
            Trigram(' ', 's', 'e'),
            Trigram('p', 'a', 'r'),
            Trigram('n', 't', 'e'),
            Trigram('u', 's', ' '),
            Trigram('u', 'r', ' '),
            Trigram('s', ' ', 's'),
            Trigram('a', 'n', 's'),
            Trigram('d', 'a', 'n'),
            Trigram('a', ' ', 'p'),
            Trigram('r', ' ', 'l'),
            Trigram('p', 'r', 'o'),
            Trigram('i', 't', 's'),
            Trigram('é', 's', ' '),
            Trigram('t', ' ', 'p'),
            Trigram('i', 'r', 'e'),
            Trigram('e', ' ', 't'),
            Trigram('s', ' ', 'p'),
            Trigram('s', 'a', ' '),
            Trigram(' ', 'd', 'é'),
            Trigram('o', 'n', 'd'),
            Trigram('é', ' ', 'd'),
            Trigram('a', ' ', 'l'),
            Trigram('n', 'c', 'e'),
            Trigram('e', 'r', 't'),
            Trigram('a', 'u', 'x'),
            Trigram('o', 'm', 'm'),
            Trigram('n', 'a', 'l'),
            Trigram('m', 'e', ' '),
            Trigram(' ', 'n', 'a'),
            Trigram(' ', 'f', 'o'),
            Trigram('i', 'q', 'u'),
            Trigram(' ', 'c', 'e'),
            Trigram('r', 't', 'é'),
            Trigram('e', 'c', 't'),
            Trigram('a', 'l', 'e'),
            Trigram('b', 'e', 'r'),
            Trigram('t', ' ', 'a'),
            Trigram('s', ' ', 'a'),
            Trigram(' ', 'd', 'a'),
            Trigram('m', 'm', 'e'),
            Trigram('i', 'b', 'e'),
            Trigram('s', 'a', 'n'),
            Trigram('e', ' ', 'r'),
            Trigram(' ', 'p', 'o'),
            Trigram('c', 'o', 'm'),
            Trigram('a', 'l', ' '),
            Trigram('s', ' ', 'c'),
            Trigram('q', 'u', 'i'),
            Trigram('o', 'u', 'r'),
            Trigram('t', ' ', 'e'),
            Trigram(' ', 'n', 'e'),
            Trigram('e', ' ', 'n'),
            Trigram('o', 'u', 's'),
            Trigram('r', ' ', 'd'),
            Trigram('a', 'l', 'i'),
            Trigram('t', 'e', 'r'),
            Trigram(' ', 'd', 'i'),
            Trigram('f', 'o', 'n'),
            Trigram('e', ' ', 'o'),
            Trigram('a', 'u', ' '),
            Trigram(' ', 'c', 'h'),
            Trigram('a', 'i', 'r'),
            Trigram('u', 'i', ' '),
            Trigram('e', 'l', 'l'),
            Trigram(' ', 'e', 's'),
            Trigram('l', 'i', 't'),
            Trigram('s', ' ', 'n'),
            Trigram('i', 's', 's'),
            Trigram('é', 'r', 'a'),
            Trigram('t', 'e', 's'),
            Trigram('s', 'o', 'c'),
            Trigram('a', 'u', 't'),
            Trigram('o', 'c', 'i'),
            Trigram('ê', 't', 'r'),
            Trigram('i', 'e', 'n'),
            Trigram('i', 'n', 't'),
            Trigram('d', 'u', ' '),
            Trigram('e', 's', 't'),
            Trigram('é', 't', 'é'),
            Trigram('t', 'r', 'a'),
            Trigram('p', 'o', 'u'),
            Trigram(' ', 'p', 'l'),
            Trigram('r', 'a', 't'),
            Trigram('a', 'r', ' '),
            Trigram('r', 'a', 'n'),
            Trigram('r', 'a', 'i'),
            Trigram('s', ' ', 'o'),
            Trigram('o', 'n', 'a'),
            Trigram('a', 'i', 'n'),
            Trigram('c', 'l', 'a'),
            Trigram('é', 'g', 'a'),
            Trigram('a', 'n', 'c'),
            Trigram('r', 's', ' '),
            Trigram('e', 'u', 'r'),
            Trigram('p', 'r', 'i'),
            Trigram('n', ' ', 'c'),
            Trigram('e', ' ', 'm'),
            Trigram('s', ' ', 't'),
            Trigram('à', ' ', 'u'),
            Trigram(' ', 'd', 'o'),
            Trigram('u', 'r', 'e'),
            Trigram('b', 'r', 'e'),
            Trigram('u', 't', ' '),
            Trigram(' ', 'ê', 't'),
            Trigram('a', 'g', 'e'),
            Trigram(' ', 'é', 't'),
            Trigram('n', 's', 'i'),
            Trigram('s', 'u', 'r'),
            Trigram('e', 'i', 'n'),
            Trigram('s', 'e', 'n'),
            Trigram('s', 'e', 'r'),
            Trigram('n', 'd', 'i'),
            Trigram('e', 'n', 's'),
            Trigram('e', 's', 's'),
            Trigram('n', 't', 'r'),
            Trigram('i', 'r', ' '),
            Trigram(' ', 'm', 'a'),
            Trigram('c', 'i', 'a'),
            Trigram('n', ' ', 'p'),
            Trigram('s', 't', ' '),
            Trigram('a', ' ', 'c'),
            Trigram(' ', 'd', 'u'),
            Trigram('l', ' ', 'e'),
            Trigram(' ', 's', 'u'),
            Trigram('b', 'l', 'i'),
            Trigram('g', 'e', ' '),
            Trigram('r', 'é', 's'),
            Trigram(' ', 'r', 'é'),
            Trigram('e', ' ', 'q'),
            Trigram('a', 's', 's'),
            Trigram('n', 'd', 'a'),
            Trigram('p', 'e', 'u'),
            Trigram('é', 'e', ' '),
            Trigram('l', '’', 'a'),
            Trigram(' ', 't', 'e'),
            Trigram('a', ' ', 's'),
            Trigram('t', 'a', 't'),
            Trigram('i', 'l', ' '),
            Trigram('t', 'é', 's'),
            Trigram('a', 'i', 's'),
            Trigram('u', ' ', 'd'),
            Trigram('i', 'n', 'e'),
            Trigram('i', 'n', 'd'),
            Trigram('é', ' ', 'e'),
            Trigram('q', 'u', '’'),
            Trigram(' ', 'a', 'c'),
            Trigram('s', ' ', 'i'),
            Trigram('n', ' ', 't'),
            Trigram('t', ' ', 'c'),
            Trigram('n', ' ', 'a'),
            Trigram('l', '’', 'h'),
            Trigram('t', ' ', 'q'),
            Trigram('s', 'o', 'i'),
            Trigram('t', ' ', 's'),
            Trigram('c', 'u', 'n'),
            Trigram('r', 'i', 't'),
            Trigram(' ', 'é', 'g'),
            Trigram('o', 'i', 'r'),
            Trigram('’', 'e', 'n'),
            Trigram('n', 't', 'a'),
            Trigram('h', 'o', 'm'),
            Trigram(' ', 'o', 'n'),
            Trigram('n', ' ', 'e'),
            Trigram(' ', 'm', 'o'),
            Trigram('i', 'e', ' '),
            Trigram('i', 'g', 'n'),
            Trigram('r', 'e', 'l'),
            Trigram('n', 'n', 'a'),
            Trigram('t', ' ', 'i'),
            Trigram('l', ' ', 'n'),
            Trigram(' ', 't', 'r'),
            Trigram('i', 'l', 'l'),
            Trigram('p', 'l', 'e'),
            Trigram('s', ' ', 'é'),
            Trigram('l', '’', 'e'),
            Trigram('r', 'e', 'c'),
            Trigram('a', ' ', 'r'),
            Trigram('o', 't', 'e'),
            Trigram('s', 's', 'e'),
            Trigram('u', 'n', 'i'),
            Trigram('i', 'd', 'é'),
            Trigram('i', 'v', 'e'),
            Trigram('s', ' ', 'u'),
            Trigram('t', ' ', 'ê'),
            Trigram('i', 'n', 's'),
            Trigram('a', 'c', 't'),
            Trigram(' ', 'f', 'a'),
            Trigram('n', ' ', 's'),
            Trigram(' ', 'v', 'i'),
            Trigram('g', 'a', 'l'),
            Trigram(' ', 'a', 's'),
            Trigram('l', 'i', 'g'),
            Trigram('s', 's', 'a'),
            Trigram('p', 'r', 'é'),
            Trigram('l', 'e', 'u'),
            Trigram('e', ' ', 'f'),
            Trigram('l', 'i', 'c'),
            Trigram('d', 'i', 's'),
            Trigram('v', 'e', 'r'),
            Trigram(' ', 'n', 'u'),
            Trigram('t', 'e', 'n'),
            Trigram('s', 's', 'i'),
            Trigram('r', 'o', 't'),
            Trigram('t', 'e', 'c'),
            Trigram('s', ' ', 'm'),
            Trigram('a', 'b', 'l'),
        ],
    ),
    (
        Lang::Deu,
        &[
            Trigram('e', 'n', ' '),
            Trigram('e', 'r', ' '),
            Trigram('d', 'e', 'r'),
            Trigram(' ', 'u', 'n'),
            Trigram('n', 'd', ' '),
            Trigram('u', 'n', 'd'),
            Trigram('e', 'i', 'n'),
            Trigram('u', 'n', 'g'),
            Trigram('c', 'h', 't'),
            Trigram(' ', 'd', 'e'),
            Trigram('i', 'c', 'h'),
            Trigram('s', 'c', 'h'),
            Trigram('n', 'g', ' '),
            Trigram(' ', 'g', 'e'),
            Trigram('i', 'e', ' '),
            Trigram('c', 'h', 'e'),
            Trigram('e', 'c', 'h'),
            Trigram(' ', 'd', 'i'),
            Trigram('d', 'i', 'e'),
            Trigram('r', 'e', 'c'),
            Trigram('g', 'e', 'n'),
            Trigram('i', 'n', 'e'),
            Trigram('e', 'i', 't'),
            Trigram(' ', 'r', 'e'),
            Trigram('c', 'h', ' '),
            Trigram(' ', 'd', 'a'),
            Trigram('n', ' ', 'd'),
            Trigram('v', 'e', 'r'),
            Trigram('h', 'e', 'n'),
            Trigram(' ', 'z', 'u'),
            Trigram('t', ' ', 'd'),
            Trigram(' ', 'a', 'u'),
            Trigram('h', 't', ' '),
            Trigram(' ', 'h', 'a'),
            Trigram('l', 'i', 'c'),
            Trigram('i', 't', ' '),
            Trigram('t', 'e', 'n'),
            Trigram('r', 'e', 'i'),
            Trigram(' ', 'b', 'e'),
            Trigram('i', 'n', ' '),
            Trigram(' ', 'v', 'e'),
            Trigram(' ', 'i', 'n'),
            Trigram(' ', 'e', 'i'),
            Trigram('n', 'd', 'e'),
            Trigram('a', 'u', 'f'),
            Trigram('d', 'e', 'n'),
            Trigram('e', 'd', 'e'),
            Trigram('z', 'u', ' '),
            Trigram('n', ' ', 's'),
            Trigram('u', 'f', ' '),
            Trigram('f', 'r', 'e'),
            Trigram('n', 'e', ' '),
            Trigram('t', 'e', 'r'),
            Trigram('e', 's', ' '),
            Trigram(' ', 'j', 'e'),
            Trigram('j', 'e', 'd'),
            Trigram('n', ' ', 'u'),
            Trigram(' ', 'a', 'n'),
            Trigram('s', 'e', 'i'),
            Trigram('a', 'n', 'd'),
            Trigram(' ', 'f', 'r'),
            Trigram('r', 'u', 'n'),
            Trigram('a', 't', ' '),
            Trigram(' ', 's', 'e'),
            Trigram('e', ' ', 'u'),
            Trigram('d', 'a', 's'),
            Trigram('h', 'e', 'i'),
            Trigram('s', ' ', 'r'),
            Trigram('h', 't', 'e'),
            Trigram('h', 'a', 't'),
            Trigram('n', 's', 'c'),
            Trigram('n', 'g', 'e'),
            Trigram('r', ' ', 'h'),
            Trigram('a', 's', ' '),
            Trigram('e', 'n', 's'),
            Trigram(' ', 'a', 'l'),
            Trigram('e', 'r', 'e'),
            Trigram('l', 'l', 'e'),
            Trigram('t', ' ', 'a'),
            Trigram(' ', 'w', 'e'),
            Trigram('n', ' ', 'g'),
            Trigram('r', 'd', 'e'),
            Trigram('n', 't', 'e'),
            Trigram('e', 's', 'e'),
            Trigram('m', 'e', 'n'),
            Trigram(' ', 'o', 'd'),
            Trigram('o', 'd', 'e'),
            Trigram('n', 'e', 'r'),
            Trigram('g', ' ', 'd'),
            Trigram('a', 'l', 'l'),
            Trigram('t', ' ', 'u'),
            Trigram('e', 'r', 's'),
            Trigram('t', 'e', ' '),
            Trigram('n', 'e', 'n'),
            Trigram(' ', 's', 'o'),
            Trigram('d', ' ', 'd'),
            Trigram('n', ' ', 'a'),
            Trigram('b', 'e', 'n'),
            Trigram('l', 'e', 'i'),
            Trigram(' ', 'g', 'r'),
            Trigram(' ', 'v', 'o'),
            Trigram('w', 'e', 'r'),
            Trigram('e', ' ', 'a'),
            Trigram('e', 'g', 'e'),
            Trigram('i', 'o', 'n'),
            Trigram(' ', 's', 't'),
            Trigram('i', 'g', 'e'),
            Trigram('l', 'e', ' '),
            Trigram('c', 'h', 'a'),
            Trigram(' ', 'm', 'e'),
            Trigram('h', 'a', 'f'),
            Trigram('a', 'f', 't'),
            Trigram('n', ' ', 'j'),
            Trigram('r', 'e', 'n'),
            Trigram(' ', 'e', 'r'),
            Trigram('e', 'r', 'k'),
            Trigram('e', 'n', 't'),
            Trigram('b', 'e', 'i'),
            Trigram(' ', 's', 'i'),
            Trigram('e', 'i', 'h'),
            Trigram('i', 'h', 'e'),
            Trigram('k', 'e', 'i'),
            Trigram('e', 'r', 'd'),
            Trigram('t', 'i', 'g'),
            Trigram('n', ' ', 'i'),
            Trigram('o', 'n', ' '),
            Trigram('l', 'u', 'n'),
            Trigram('r', ' ', 'd'),
            Trigram('l', 'e', 'n'),
            Trigram('g', 'e', 'm'),
            Trigram('i', 'e', 's'),
            Trigram('g', 'r', 'u'),
            Trigram('t', 'l', 'i'),
            Trigram('u', 'n', 't'),
            Trigram('c', 'h', 'u'),
            Trigram('e', 'r', 'n'),
            Trigram('g', 'e', 's'),
            Trigram('e', 'n', 'd'),
            Trigram('e', ' ', 's'),
            Trigram('f', 't', ' '),
            Trigram('s', 't', ' '),
            Trigram('i', 's', 't'),
            Trigram('t', 'i', 'o'),
            Trigram('a', 't', 'i'),
            Trigram(' ', 'g', 'l'),
            Trigram('s', 't', 'a'),
            Trigram('g', 'u', 'n'),
            Trigram('m', 'i', 't'),
            Trigram('s', 'e', 'n'),
            Trigram('n', ' ', 'n'),
            Trigram(' ', 'n', 'a'),
            Trigram('n', ' ', 'z'),
            Trigram('i', 't', 'e'),
            Trigram(' ', 'w', 'i'),
            Trigram('r', ' ', 'g'),
            Trigram('e', 'i', 'c'),
            Trigram('e', ' ', 'e'),
            Trigram('e', 'i', ' '),
            Trigram('l', 'i', 'e'),
            Trigram('r', ' ', 's'),
            Trigram('n', ' ', 'w'),
            Trigram('g', 'l', 'e'),
            Trigram('m', 'e', 'i'),
            Trigram('d', 'e', ' '),
            Trigram('u', 'c', 'h'),
            Trigram('e', 'm', ' '),
            Trigram('c', 'h', 'l'),
            Trigram('n', 'a', 't'),
            Trigram('r', 'c', 'h'),
            Trigram('t', ' ', 'w'),
            Trigram('d', 'e', 's'),
            Trigram('n', ' ', 'e'),
            Trigram('h', 'r', 'e'),
            Trigram('a', 'l', 'e'),
            Trigram('s', 'p', 'r'),
            Trigram('d', ' ', 'f'),
            Trigram('a', 'c', 'h'),
            Trigram('s', 's', 'e'),
            Trigram('r', ' ', 'e'),
            Trigram(' ', 's', 'c'),
            Trigram('u', 'r', 'c'),
            Trigram('r', ' ', 'm'),
            Trigram('n', 'i', 'e'),
            Trigram('e', ' ', 'f'),
            Trigram('f', 'e', 'n'),
            Trigram('e', ' ', 'g'),
            Trigram('e', ' ', 'd'),
            Trigram(' ', 'n', 'i'),
            Trigram('d', 'u', 'r'),
            Trigram('d', 'a', 'r'),
            Trigram('i', 'n', 't'),
            Trigram(' ', 'd', 'u'),
            Trigram('g', 'e', 'h'),
            Trigram('i', 'e', 'd'),
            Trigram('t', ' ', 's'),
            Trigram(' ', 'm', 'i'),
            Trigram('a', 'l', 't'),
            Trigram('h', 'e', 'r'),
            Trigram('h', 'a', 'b'),
            Trigram('f', ' ', 'g'),
            Trigram('s', 'i', 'c'),
            Trigram('s', 't', 'e'),
            Trigram('t', 'a', 'a'),
            Trigram('a', 'a', 't'),
            Trigram('h', 'e', ' '),
            Trigram('a', 'n', 'g'),
            Trigram('r', 'u', 'c'),
            Trigram('h', 'l', 'i'),
            Trigram('t', 'z', ' '),
            Trigram('e', 'm', 'e'),
            Trigram('a', 'b', 'e'),
            Trigram('h', ' ', 'a'),
            Trigram('n', ' ', 'v'),
            Trigram('n', 'u', 'n'),
            Trigram('g', 'e', 'g'),
            Trigram('a', 'r', 'f'),
            Trigram('r', 'f', ' '),
            Trigram('e', 'h', 'e'),
            Trigram('p', 'r', 'u'),
            Trigram(' ', 'i', 's'),
            Trigram('e', 'r', 'f'),
            Trigram('e', ' ', 'm'),
            Trigram('a', 'n', 's'),
            Trigram('n', 'd', 'l'),
            Trigram('e', ' ', 'b'),
            Trigram('t', 'u', 'n'),
            Trigram('n', ' ', 'o'),
            Trigram('d', ' ', 'g'),
            Trigram('n', ' ', 'r'),
            Trigram('r', ' ', 'v'),
            Trigram('w', 'i', 'e'),
            Trigram('b', 'e', 'r'),
            Trigram('r', ' ', 'a'),
            Trigram('a', 'r', 'b'),
            Trigram('b', 'e', 's'),
            Trigram('t', ' ', 'i'),
            Trigram('h', ' ', 'd'),
            Trigram('r', ' ', 'w'),
            Trigram('r', ' ', 'b'),
            Trigram(' ', 'i', 'h'),
            Trigram('d', ' ', 's'),
            Trigram('i', 'g', 'k'),
            Trigram('g', 'k', 'e'),
            Trigram('n', 's', 'p'),
            Trigram('d', 'i', 'g'),
            Trigram('e', 'm', 'a'),
            Trigram('e', 'l', 'l'),
            Trigram('e', 'r', 'u'),
            Trigram('n', ' ', 'f'),
            Trigram('i', 'n', 's'),
            Trigram('r', 'b', 'e'),
            Trigram('f', 'f', 'e'),
            Trigram('e', 's', 'c'),
            Trigram('i', 'g', 'u'),
            Trigram('g', 'e', 'r'),
            Trigram('s', 't', 'r'),
            Trigram('k', 'e', 'n'),
            Trigram('e', ' ', 'v'),
            Trigram('g', 'e', 'w'),
            Trigram('h', 'a', 'n'),
            Trigram('i', 'n', 'd'),
            Trigram('r', 't', ' '),
            Trigram(' ', 'a', 'r'),
            Trigram('i', 'e', 'ß'),
            Trigram('n', ' ', 'h'),
            Trigram('r', 'n', ' '),
            Trigram('m', 'a', 'n'),
            Trigram('r', ' ', 'i'),
            Trigram('h', 'u', 't'),
            Trigram('u', 't', 'z'),
            Trigram('d', ' ', 'a'),
            Trigram('l', 's', ' '),
            Trigram('e', 'b', 'e'),
            Trigram('v', 'o', 'n'),
            Trigram('l', 't', 'e'),
            Trigram('r', ' ', 'o'),
            Trigram('r', 'l', 'i'),
            Trigram('e', 't', 'z'),
            Trigram('t', 'r', 'a'),
            Trigram('a', 'u', 's'),
            Trigram('d', 'e', 't'),
            Trigram('h', 'u', 'l'),
            Trigram('e', ' ', 'i'),
            Trigram('o', 'n', 'e'),
            Trigram('n', 'n', 'e'),
            Trigram('i', 's', 'c'),
            Trigram('s', 'o', 'n'),
            Trigram('s', 'e', 'l'),
            Trigram('e', 't', ' '),
            Trigram('o', 'h', 'n'),
            Trigram('t', ' ', 'g'),
            Trigram('s', 'a', 'm'),
            Trigram(' ', 'f', 'a'),
            Trigram('r', 's', 't'),
            Trigram('r', 'k', 'l'),
            Trigram('s', 'e', 'r'),
            Trigram('i', 'e', 'm'),
            Trigram('g', ' ', 'v'),
            Trigram('t', ' ', 'z'),
            Trigram('e', 'r', 'r'),
        ],
    ),
    (
        Lang::Jav,
        &[
            Trigram('n', 'g', ' '),
            Trigram('a', 'n', ' '),
            Trigram('a', 'n', 'g'),
            Trigram(' ', 'k', 'a'),
            Trigram('i', 'n', 'g'),
            Trigram('k', 'a', 'n'),
            Trigram(' ', 's', 'a'),
            Trigram('a', 'k', ' '),
            Trigram('l', 'a', 'n'),
            Trigram(' ', 'l', 'a'),
            Trigram('h', 'a', 'k'),
            Trigram(' ', 'h', 'a'),
            Trigram(' ', 'p', 'a'),
            Trigram(' ', 'm', 'a'),
            Trigram('n', 'g', 'g'),
            Trigram('a', 'r', 'a'),
            Trigram('s', 'a', ' '),
            Trigram('a', 'b', 'e'),
            Trigram('n', 'e', ' '),
            Trigram(' ', 'i', 'n'),
            Trigram('n', ' ', 'k'),
            Trigram('a', 'n', 't'),
            Trigram(' ', 'n', 'g'),
            Trigram('t', 'a', 'n'),
            Trigram('n', 'i', 'n'),
            Trigram(' ', 'a', 'n'),
            Trigram('n', 'g', 'a'),
            Trigram('a', 't', 'a'),
            Trigram('e', 'n', ' '),
            Trigram('r', 'a', 'n'),
            Trigram(' ', 'b', 'a'),
            Trigram('m', 'a', 'n'),
            Trigram('b', 'a', 'n'),
            Trigram('a', 'n', 'e'),
            Trigram('h', 'i', ' '),
            Trigram('n', ' ', 'u'),
            Trigram('o', 'n', 'g'),
            Trigram('r', 'a', ' '),
            Trigram('n', 't', 'h'),
            Trigram('a', 'k', 'e'),
            Trigram('k', 'e', ' '),
            Trigram('t', 'h', 'i'),
            Trigram(' ', 'd', 'a'),
            Trigram('w', 'o', 'n'),
            Trigram('u', 'w', 'o'),
            Trigram('u', 'n', 'g'),
            Trigram('n', 'g', 's'),
            Trigram(' ', 'u', 'w'),
            Trigram('a', 's', 'a'),
            Trigram('g', 's', 'a'),
            Trigram('b', 'e', 'n'),
            Trigram('s', 'a', 'b'),
            Trigram('a', 'n', 'a'),
            Trigram('a', 'k', 'a'),
            Trigram('b', 'e', 'b'),
            Trigram('a', ' ', 'k'),
            Trigram('g', ' ', 'p'),
            Trigram('n', 'a', 'n'),
            Trigram('n', 'd', 'a'),
            Trigram('a', 'd', 'i'),
            Trigram('a', 't', ' '),
            Trigram('a', 'w', 'a'),
            Trigram('s', 'a', 'n'),
            Trigram('n', 'i', ' '),
            Trigram('d', 'a', 'n'),
            Trigram('g', ' ', 'k'),
            Trigram('p', 'a', 'n'),
            Trigram('e', 'b', 'a'),
            Trigram(' ', 'b', 'e'),
            Trigram('e', ' ', 'k'),
            Trigram('g', ' ', 's'),
            Trigram('a', 'n', 'i'),
            Trigram('b', 'a', 's'),
            Trigram(' ', 'p', 'r'),
            Trigram('d', 'h', 'a'),
            Trigram('a', 'y', 'a'),
            Trigram('g', 'a', 'n'),
            Trigram('y', 'a', ' '),
            Trigram('w', 'a', ' '),
            Trigram('d', 'i', ' '),
            Trigram('m', 'a', 'r'),
            Trigram('n', ' ', 's'),
            Trigram(' ', 'w', 'a'),
            Trigram('t', 'a', ' '),
            Trigram('a', ' ', 's'),
            Trigram('g', ' ', 'u'),
            Trigram(' ', 'n', 'a'),
            Trigram('e', ' ', 'h'),
            Trigram('a', 'r', 'b'),
            Trigram('a', ' ', 'n'),
            Trigram('a', ' ', 'b'),
            Trigram('a', ' ', 'l'),
            Trigram('n', ' ', 'n'),
            Trigram(' ', 'u', 't'),
            Trigram('y', 'a', 'n'),
            Trigram('n', ' ', 'p'),
            Trigram('a', 's', 'i'),
            Trigram('g', ' ', 'd'),
            Trigram('h', 'a', 'n'),
            Trigram('a', 'h', ' '),
            Trigram('g', ' ', 'n'),
            Trigram(' ', 't', 'u'),
            Trigram(' ', 'u', 'm'),
            Trigram('a', 's', ' '),
            Trigram('w', 'e', 'n'),
            Trigram('d', 'a', 'k'),
            Trigram('r', 'b', 'e'),
            Trigram('d', 'a', 'r'),
            Trigram(' ', 'd', 'i'),
            Trigram('g', 'g', 'o'),
            Trigram('s', 'a', 'r'),
            Trigram('m', 'a', 't'),
            Trigram('k', ' ', 'h'),
            Trigram('a', ' ', 'a'),
            Trigram('i', 'y', 'a'),
            Trigram(' ', 'u', 'n'),
            Trigram('u', 'n', 'd'),
            Trigram('e', 'n', 'i'),
            Trigram('k', 'a', 'b'),
            Trigram('b', 'e', ' '),
            Trigram('a', 'r', 't'),
            Trigram('k', 'a', ' '),
            Trigram('u', 'm', 'a'),
            Trigram('o', 'r', 'a'),
            Trigram('n', ' ', 'b'),
            Trigram('a', 'l', 'a'),
            Trigram('n', ' ', 'm'),
            Trigram('n', 'g', 'k'),
            Trigram('r', 't', 'a'),
            Trigram('i', ' ', 'h'),
            Trigram(' ', 'o', 'r'),
            Trigram('g', 'a', 'r'),
            Trigram('y', 'a', 't'),
            Trigram('k', 'a', 'r'),
            Trigram('a', 'l', ' '),
            Trigram('a', ' ', 'm'),
            Trigram('n', ' ', 'i'),
            Trigram('n', 'a', ' '),
            Trigram('g', ' ', 'b'),
            Trigram('e', 'g', 'a'),
            Trigram('p', 'r', 'a'),
            Trigram('i', 'n', 'a'),
            Trigram('k', 'a', 'k'),
            Trigram('g', ' ', 'a'),
            Trigram('a', ' ', 'p'),
            Trigram('t', 'u', 'm'),
            Trigram('n', 'y', 'a'),
            Trigram('k', 'a', 'l'),
            Trigram('g', 'e', 'r'),
            Trigram('g', 'g', 'e'),
            Trigram(' ', 't', 'a'),
            Trigram('k', 'a', 't'),
            Trigram('i', ' ', 'k'),
            Trigram('e', 'n', 'a'),
            Trigram('o', 'n', 'i'),
            Trigram('k', 'a', 's'),
            Trigram(' ', 'p', 'e'),
            Trigram('d', 'a', 'd'),
            Trigram('a', 'g', 'a'),
            Trigram('g', ' ', 'm'),
            Trigram('d', 'u', 'w'),
            Trigram('k', ' ', 'k'),
            Trigram('u', 't', 'a'),
            Trigram('u', 'w', 'e'),
            Trigram(' ', 's', 'i'),
            Trigram(' ', 'n', 'e'),
            Trigram('a', 'd', 'h'),
            Trigram('p', 'a', ' '),
            Trigram('n', ' ', 'a'),
            Trigram('g', 'o', ' '),
            Trigram('a', 'n', 'd'),
            Trigram('i', ' ', 'l'),
            Trigram(' ', 'k', 'e'),
            Trigram('n', 'u', 'n'),
            Trigram('n', 'a', 'l'),
            Trigram('n', 'g', 'u'),
            Trigram('u', 'j', 'u'),
            Trigram('a', 'p', 'a'),
            Trigram('a', ' ', 'd'),
            Trigram('t', ' ', 'm'),
            Trigram('i', ' ', 'p'),
            Trigram('m', 'i', 'n'),
            Trigram('i', 'b', 'a'),
            Trigram('e', 'r', ' '),
            Trigram(' ', 'l', 'i'),
            Trigram('a', 'n', 'u'),
            Trigram('s', 'a', 'k'),
            Trigram('p', 'e', 'r'),
            Trigram('a', 'm', 'a'),
            Trigram('g', 'a', 'y'),
            Trigram('w', 'a', 'r'),
            Trigram('p', 'a', 'd'),
            Trigram('g', 'g', 'u'),
            Trigram('h', 'a', ' '),
            Trigram('i', 'n', 'd'),
            Trigram('t', 'a', 'w'),
            Trigram('r', 'a', 's'),
            Trigram('n', ' ', 'l'),
            Trigram('a', 'l', 'i'),
            Trigram('e', 'n', 'g'),
            Trigram('a', 'w', 'i'),
            Trigram('a', ' ', 'u'),
            Trigram(' ', 'b', 'i'),
            Trigram('w', 'e', ' '),
            Trigram('b', 'a', 'd'),
            Trigram('n', 'd', 'u'),
            Trigram('u', 'w', 'a'),
            Trigram('a', 'w', 'e'),
            Trigram('b', 'a', 'k'),
            Trigram('a', 's', 'e'),
            Trigram('e', 'h', ' '),
            Trigram(' ', 'm', 'e'),
            Trigram('n', 'e', 'g'),
            Trigram('p', 'r', 'i'),
            Trigram(' ', 'k', 'u'),
            Trigram('r', 'o', 'n'),
            Trigram('i', 'h', ' '),
            Trigram('g', ' ', 't'),
            Trigram('b', 'i', 's'),
            Trigram('i', 'j', 'i'),
            Trigram('i', ' ', 't'),
            Trigram('e', ' ', 'p'),
            Trigram(' ', 'p', 'i'),
            Trigram('a', 'b', 'a'),
            Trigram('i', 's', 'a'),
            Trigram('m', 'b', 'a'),
            Trigram('i', 'n', 'i'),
            Trigram('a', ' ', 'w'),
            Trigram('g', ' ', 'l'),
            Trigram('i', 'k', 'a'),
            Trigram('n', ' ', 't'),
            Trigram('e', 'b', 'u'),
            Trigram('n', 'd', 'h'),
            Trigram('a', 'r', ' '),
            Trigram('s', 'i', 'n'),
            Trigram('l', 'a', 'k'),
            Trigram('u', 'r', ' '),
            Trigram('m', 'r', 'a'),
            Trigram('m', 'e', 'n'),
            Trigram('k', 'u', ' '),
            Trigram(' ', 'w', 'e'),
            Trigram('e', ' ', 's'),
            Trigram('a', ' ', 'i'),
            Trigram('l', 'i', 'y'),
            Trigram(' ', 'i', 'k'),
            Trigram('a', 'y', 'o'),
            Trigram('r', 'i', 'b'),
            Trigram('n', 'g', 'l'),
            Trigram('a', 'm', 'i'),
            Trigram('a', 'r', 'g'),
            Trigram('n', 'a', 's'),
            Trigram('y', 'o', 'm'),
            Trigram('w', 'a', 'e'),
            Trigram('u', 't', ' '),
            Trigram('k', 'o', 'n'),
            Trigram('a', 'e', ' '),
            Trigram('r', 'a', 'p'),
            Trigram('a', 'k', 'u'),
            Trigram(' ', 't', 'e'),
            Trigram('d', 'i', 'l'),
            Trigram('t', 'i', 'n'),
            Trigram('r', 'g', 'a'),
            Trigram('j', 'u', 'd'),
            Trigram('u', 'm', 'u'),
            Trigram(' ', 'a', 's'),
            Trigram('r', 'a', 'k'),
            Trigram('b', 'e', 'd'),
            Trigram('k', ' ', 'b'),
            Trigram('i', 'l', ' '),
            Trigram('k', 'a', 'p'),
            Trigram('h', ' ', 'k'),
            Trigram('j', 'i', 'n'),
            Trigram('k', ' ', 'a'),
            Trigram(' ', 'n', 'd'),
            Trigram('e', ' ', 'd'),
            Trigram('i', ' ', 's'),
            Trigram(' ', 'l', 'u'),
            Trigram('i', ' ', 'w'),
            Trigram('e', 'k', 'a'),
            Trigram('m', 'u', 'm'),
            Trigram('u', 'm', ' '),
            Trigram('u', 'h', 'a'),
            Trigram('a', 't', 'e'),
            Trigram(' ', 'm', 'i'),
            Trigram('k', ' ', 'p'),
            Trigram('g', 'o', 'n'),
            Trigram('e', 'd', 'a'),
            Trigram(' ', 't', 'i'),
            Trigram('b', 'u', 't'),
            Trigram('n', ' ', 'd'),
            Trigram('r', ' ', 'k'),
            Trigram('o', 'n', 'a'),
            Trigram('u', 't', 'o'),
            Trigram('t', 'o', 'w'),
            Trigram('w', 'a', 't'),
            Trigram('g', 'k', 'a'),
            Trigram('s', 'i', ' '),
            Trigram('u', 'm', 'r'),
            Trigram('k', ' ', 'l'),
            Trigram('o', 'm', 'a'),
        ],
    ),
    (
        Lang::Vie,
        &[
            Trigram('n', 'g', ' '),
            Trigram('̣', 'c', ' '),
            Trigram('́', 'c', ' '),
            Trigram(' ', 'q', 'u'),
            Trigram(' ', 't', 'h'),
            Trigram('a', '̀', ' '),
            Trigram('n', 'h', ' '),
            Trigram(' ', 'n', 'g'),
            Trigram('̣', 'i', ' '),
            Trigram(' ', 'n', 'h'),
            Trigram('v', 'a', '̀'),
            Trigram(' ', 'v', 'a'),
            Trigram('̀', 'n', ' '),
            Trigram('u', 'y', 'ê'),
            Trigram(' ', 'p', 'h'),
            Trigram(' ', 'c', 'a'),
            Trigram('q', 'u', 'y'),
            Trigram('ê', '̀', 'n'),
            Trigram('y', 'ê', '̀'),
            Trigram('̀', 'i', ' '),
            Trigram(' ', 'c', 'h'),
            Trigram('̀', 'n', 'h'),
            Trigram(' ', 't', 'r'),
            Trigram(' ', 'c', 'u'),
            Trigram('n', 'g', 'ư'),
            Trigram('i', ' ', 'n'),
            Trigram('g', 'ư', 'ơ'),
            Trigram('ư', 'ơ', '̀'),
            Trigram('́', 't', ' '),
            Trigram('ơ', '̀', 'i'),
            Trigram(' ', 'g', 'i'),
            Trigram('a', '́', 'c'),
            Trigram(' ', 'c', 'o'),
            Trigram('̣', 't', ' '),
            Trigram('o', '́', ' '),
            Trigram('c', ' ', 't'),
            Trigram('ư', '̣', ' '),
            Trigram('n', ' ', 't'),
            Trigram('c', 'a', '́'),
            Trigram('ô', 'n', 'g'),
            Trigram(' ', 'k', 'h'),
            Trigram('ư', 'ơ', '̣'),
            Trigram('ơ', '̣', 'c'),
            Trigram(' ', 't', 'ư'),
            Trigram(' ', 'đ', 'ư'),
            Trigram('i', 'ê', '̣'),
            Trigram('đ', 'ư', 'ơ'),
            Trigram('i', '̀', 'n'),
            Trigram('́', 'i', ' '),
            Trigram(' ', 'h', 'a'),
            Trigram('c', 'o', '́'),
            Trigram('i', ' ', 'đ'),
            Trigram('g', 'i', 'a'),
            Trigram(' ', 'đ', 'ê'),
            Trigram('p', 'h', 'a'),
            Trigram(' ', 'm', 'o'),
            Trigram('o', '̣', 'i'),
            Trigram('m', 'o', '̣'),
            Trigram('n', 'h', 'ư'),
            Trigram('n', ' ', 'n'),
            Trigram('c', 'u', '̉'),
            Trigram(' ', 'b', 'a'),
            Trigram('̣', 'n', ' '),
            Trigram('̉', 'a', ' '),
            Trigram('u', '̉', 'a'),
            Trigram('n', ' ', 'c'),
            Trigram('̀', 'u', ' '),
            Trigram('̃', 'n', 'g'),
            Trigram('â', 'n', ' '),
            Trigram('ê', '̀', 'u'),
            Trigram('â', '́', 't'),
            Trigram(' ', 'b', 'i'),
            Trigram('t', 'ư', '̣'),
            Trigram('h', 'ô', 'n'),
            Trigram(' ', 'v', 'i'),
            Trigram('g', ' ', 't'),
            Trigram(' ', 'l', 'a'),
            Trigram('n', ' ', 'đ'),
            Trigram('đ', 'ê', '̀'),
            Trigram('n', 'h', 'â'),
            Trigram(' ', 't', 'i'),
            Trigram('t', ' ', 'c'),
            Trigram(' ', 'đ', 'ô'),
            Trigram('ê', 'n', ' '),
            Trigram('b', 'a', '̉'),
            Trigram('h', 'i', 'ê'),
            Trigram('u', ' ', 'c'),
            Trigram(' ', 't', 'ô'),
            Trigram('d', 'o', ' '),
            Trigram('h', 'â', 'n'),
            Trigram(' ', 'd', 'o'),
            Trigram('c', 'h', ' '),
            Trigram('́', ' ', 'q'),
            Trigram('̀', ' ', 't'),
            Trigram(' ', 'n', 'a'),
            Trigram('́', 'n', ' '),
            Trigram('a', 'y', ' '),
            Trigram(' ', 'h', 'i'),
            Trigram('a', '̀', 'n'),
            Trigram('̣', ' ', 'd'),
            Trigram('ơ', '́', 'i'),
            Trigram('h', 'a', '́'),
            Trigram(' ', 'đ', 'i'),
            Trigram('h', 'a', 'y'),
            Trigram('g', ' ', 'n'),
            Trigram(' ', 'm', 'ô'),
            Trigram('ô', '́', 'c'),
            Trigram('u', 'ô', '́'),
            Trigram('n', ' ', 'v'),
            Trigram('ô', '̣', 'i'),
            Trigram('h', 'ư', '̃'),
            Trigram('t', 'h', 'ư'),
            Trigram('́', 'p', ' '),
            Trigram('q', 'u', 'ô'),
            Trigram(' ', 'h', 'o'),
            Trigram('̣', 'p', ' '),
            Trigram('n', 'a', '̀'),
            Trigram('a', '̀', 'o'),
            Trigram('̀', 'n', 'g'),
            Trigram('̉', 'n', ' '),
            Trigram('i', '̣', ' '),
            Trigram('́', 'c', 'h'),
            Trigram('ô', 'n', ' '),
            Trigram('̀', 'o', ' '),
            Trigram('k', 'h', 'ô'),
            Trigram('c', ' ', 'h'),
            Trigram('i', ' ', 'c'),
            Trigram('c', ' ', 'đ'),
            Trigram(' ', 'h', 'ô'),
            Trigram('i', ' ', 'v'),
            Trigram('t', 'r', 'o'),
            Trigram(' ', 'đ', 'a'),
            Trigram('́', 'n', 'g'),
            Trigram('m', 'ô', '̣'),
            Trigram('i', ' ', 't'),
            Trigram('ô', '̣', 't'),
            Trigram('g', ' ', 'v'),
            Trigram('i', 'a', ' '),
            Trigram('̣', 'n', 'g'),
            Trigram('a', '̉', 'n'),
            Trigram('ư', 'ơ', '́'),
            Trigram('ư', '̃', 'n'),
            Trigram('̉', 'n', 'g'),
            Trigram('h', ' ', 't'),
            Trigram('h', 'ư', ' '),
            Trigram('ê', '̣', 'n'),
            Trigram('n', ' ', 'b'),
            Trigram('ô', '̣', 'c'),
            Trigram('a', '̉', ' '),
            Trigram('l', 'a', '̀'),
            Trigram('c', ' ', 'c'),
            Trigram('g', ' ', 'c'),
            Trigram(' ', 'đ', 'o'),
            Trigram('̉', ' ', 'c'),
            Trigram('n', ' ', 'h'),
            Trigram('h', 'a', '̀'),
            Trigram('h', 'ô', '̣'),
            Trigram(' ', 'b', 'â'),
            Trigram('a', '̃', ' '),
            Trigram('̀', 'y', ' '),
            Trigram(' ', 'v', 'ơ'),
            Trigram('̣', ' ', 't'),
            Trigram('̉', 'i', ' '),
            Trigram('i', 'ê', '́'),
            Trigram(' ', 'c', 'ô'),
            Trigram('t', ' ', 't'),
            Trigram('g', ' ', 'đ'),
            Trigram('ư', '́', 'c'),
            Trigram('i', 'ê', 'n'),
            Trigram(' ', 'v', 'ê'),
            Trigram('v', 'i', 'ê'),
            Trigram('v', 'ơ', '́'),
            Trigram('h', ' ', 'v'),
            Trigram('ơ', '́', 'c'),
            Trigram('ư', '̣', 'c'),
            Trigram('â', '̣', 't'),
            Trigram('t', 'h', 'a'),
            Trigram('̉', 'm', ' '),
            Trigram('r', 'o', 'n'),
            Trigram('o', 'n', 'g'),
            Trigram('a', '́', 'p'),
            Trigram('g', ' ', 'b'),
            Trigram('h', 'ư', 'ơ'),
            Trigram(' ', 's', 'ư'),
            Trigram('a', ' ', 'c'),
            Trigram('s', 'ư', '̣'),
            Trigram('̉', 'o', ' '),
            Trigram('a', '̉', 'o'),
            Trigram('h', ' ', 'c'),
            Trigram('ê', '̉', ' '),
            Trigram('o', ' ', 'v'),
            Trigram('u', 'â', '̣'),
            Trigram('a', ' ', 'm'),
            Trigram('ê', '́', ' '),
            Trigram('i', 'a', '́'),
            Trigram('̀', ' ', 'c'),
            Trigram('c', 'h', 'o'),
            Trigram('q', 'u', 'a'),
            Trigram('h', 'a', '̣'),
            Trigram('u', '̣', 'c'),
            Trigram(' ', 'm', 'i'),
            Trigram('̀', ' ', 'n'),
            Trigram('p', 'h', 'â'),
            Trigram('c', ' ', 'q'),
            Trigram('c', 'ô', 'n'),
            Trigram('o', ' ', 'c'),
            Trigram('a', '́', ' '),
            Trigram('i', ' ', 'h'),
            Trigram('a', '̣', 'i'),
            Trigram(' ', 'h', 'ơ'),
            Trigram('̃', ' ', 'h'),
            Trigram(' ', 'c', 'ư'),
            Trigram('n', ' ', 'l'),
            Trigram('b', 'i', '̣'),
            Trigram(' ', 'l', 'u'),
            Trigram('b', 'â', '́'),
            Trigram('c', 'a', '̉'),
            Trigram('i', '́', 'n'),
            Trigram('h', ' ', 'đ'),
            Trigram(' ', 'x', 'a'),
            Trigram('đ', 'ô', '̣'),
            Trigram('g', ' ', 'h'),
            Trigram('c', ' ', 'n'),
            Trigram('c', ' ', 'p'),
            Trigram('t', 'h', 'u'),
            Trigram('a', '̉', 'i'),
            Trigram('ê', '̣', ' '),
            Trigram(' ', 'h', 'ư'),
            Trigram('́', ' ', 'c'),
            Trigram('o', ' ', 'n'),
            Trigram(' ', 'n', 'ư'),
            Trigram('ô', '́', 'n'),
            Trigram('́', 'o', ' '),
            Trigram('a', '́', 'o'),
            Trigram('x', 'a', '̃'),
            Trigram('o', 'a', '̀'),
            Trigram('y', ' ', 't'),
            Trigram('h', 'a', '̉'),
            Trigram('t', 'ô', '̣'),
            Trigram('̣', ' ', 'c'),
            Trigram(' ', 't', 'â'),
            Trigram('t', 'h', 'ô'),
            Trigram(' ', 'd', 'u'),
            Trigram('m', ' ', 'v'),
            Trigram('m', 'i', '̀'),
            Trigram('h', 'o', ' '),
            Trigram('h', 'ư', '́'),
            Trigram('ê', '̣', 'c'),
            Trigram('́', ' ', 't'),
            Trigram('h', 'ơ', '̣'),
            Trigram('a', '́', 'n'),
            Trigram('n', ' ', 'p'),
            Trigram('c', 'u', '̃'),
            Trigram('u', '̃', 'n'),
            Trigram('i', 'ê', '̉'),
            Trigram('ô', '́', 'i'),
            Trigram('t', 'i', 'ê'),
            Trigram('ê', '̀', ' '),
            Trigram('h', 'â', '́'),
            Trigram('ơ', '̣', 'p'),
            Trigram('h', 'o', 'a'),
            Trigram('y', ' ', 'đ'),
            Trigram('c', 'h', 'i'),
            Trigram('o', ' ', 'h'),
            Trigram('ơ', '̉', ' '),
            Trigram('a', '̀', 'y'),
            Trigram('̉', ' ', 't'),
            Trigram('đ', 'o', '́'),
            Trigram('c', ' ', 'l'),
            Trigram('v', 'ê', '̀'),
            Trigram('̀', ' ', 'đ'),
            Trigram('i', ' ', 'b'),
            Trigram('k', 'h', 'a'),
            Trigram('c', ' ', 'b'),
            Trigram(' ', 'đ', 'â'),
            Trigram('l', 'u', 'â'),
            Trigram('a', 'i', ' '),
            Trigram('̉', ' ', 'n'),
            Trigram('đ', 'ô', '́'),
            Trigram('ê', '́', 't'),
            Trigram('h', 'ư', '̣'),
            Trigram('t', 'r', 'i'),
            Trigram('p', ' ', 'q'),
            Trigram('n', 'ư', 'ơ'),
            Trigram('d', 'u', '̣'),
            Trigram('h', 'i', '́'),
            Trigram('g', ' ', 'q'),
            Trigram('y', 'ê', 'n'),
            Trigram('h', 'o', '̣'),
            Trigram('́', 'n', 'h'),
            Trigram(' ', 't', 'a'),
            Trigram(' ', 'b', 'ă'),
            Trigram('c', ' ', 'g'),
            Trigram('n', ' ', 'g'),
            Trigram('t', 'h', 'ê'),
            Trigram('o', ' ', 't'),
            Trigram('c', ' ', 'v'),
            Trigram('a', 'm', ' '),
            Trigram('c', ' ', 'm'),
            Trigram('a', 'n', ' '),
        ],
    ),
    (
        Lang::Ita,
        &[
            Trigram(' ', 'd', 'i'),
            Trigram('t', 'o', ' '),
            Trigram(' ', 'd', 'e'),
            Trigram('i', 'o', 'n'),
            Trigram(' ', 'i', 'n'),
            Trigram('l', 'a', ' '),
            Trigram('e', ' ', 'd'),
            Trigram('d', 'i', ' '),
            Trigram('n', 'e', ' '),
            Trigram(' ', 'e', ' '),
            Trigram('z', 'i', 'o'),
            Trigram('r', 'e', ' '),
            Trigram('l', 'e', ' '),
            Trigram('n', 'i', ' '),
            Trigram('e', 'l', 'l'),
            Trigram('o', 'n', 'e'),
            Trigram('l', 'l', 'a'),
            Trigram('r', 'i', 't'),
            Trigram('a', ' ', 'd'),
            Trigram('o', ' ', 'd'),
            Trigram('d', 'e', 'l'),
            Trigram('i', 't', 't'),
            Trigram('i', 'r', 'i'),
            Trigram('d', 'i', 'r'),
            Trigram(' ', 'c', 'o'),
            Trigram('t', 'i', ' '),
            Trigram('e', 's', 's'),
            Trigram('e', 'n', 't'),
            Trigram(' ', 'a', 'l'),
            Trigram('a', 'z', 'i'),
            Trigram('t', 't', 'o'),
            Trigram('t', 'e', ' '),
            Trigram('i', ' ', 'd'),
            Trigram('i', ' ', 'i'),
            Trigram('e', 'r', 'e'),
            Trigram('t', 'à', ' '),
            Trigram(' ', 'p', 'r'),
            Trigram('n', 'd', 'i'),
            Trigram('e', ' ', 'l'),
            Trigram('a', 'l', 'e'),
            Trigram('o', ' ', 'a'),
            Trigram('i', 'n', 'd'),
            Trigram('e', ' ', 'e'),
            Trigram('e', ' ', 'i'),
            Trigram('g', 'n', 'i'),
            Trigram('n', 't', 'e'),
            Trigram('c', 'o', 'n'),
            Trigram('i', ' ', 'e'),
            Trigram('l', 'i', ' '),
            Trigram('a', ' ', 's'),
            Trigram(' ', 'u', 'n'),
            Trigram('m', 'e', 'n'),
            Trigram('o', 'g', 'n'),
            Trigram(' ', 'n', 'e'),
            Trigram('u', 'o', ' '),
            Trigram(' ', 'o', 'g'),
            Trigram('i', 'd', 'u'),
            Trigram('e', ' ', 'a'),
            Trigram('i', 'v', 'i'),
            Trigram('d', 'u', 'o'),
            Trigram('v', 'i', 'd'),
            Trigram(' ', 'e', 's'),
            Trigram('t', 't', 'i'),
            Trigram(' ', 'h', 'a'),
            Trigram('d', 'i', 'v'),
            Trigram(' ', 'l', 'i'),
            Trigram('a', ' ', 'p'),
            Trigram('n', 'o', ' '),
            Trigram('a', 'l', 'l'),
            Trigram('p', 'r', 'o'),
            Trigram('z', 'a', ' '),
            Trigram('a', 't', 'o'),
            Trigram('p', 'e', 'r'),
            Trigram('s', 's', 'e'),
            Trigram('s', 'e', 'r'),
            Trigram(' ', 's', 'o'),
            Trigram('i', ' ', 's'),
            Trigram(' ', 'l', 'a'),
            Trigram(' ', 's', 'u'),
            Trigram('e', ' ', 'p'),
            Trigram(' ', 'p', 'e'),
            Trigram('i', 'b', 'e'),
            Trigram('n', 'a', ' '),
            Trigram('a', ' ', 'l'),
            Trigram(' ', 'i', 'l'),
            Trigram('b', 'e', 'r'),
            Trigram('e', ' ', 'n'),
            Trigram('i', 'l', ' '),
            Trigram('a', 'l', 'i'),
            Trigram('l', 'i', 'b'),
            Trigram('h', 'a', ' '),
            Trigram('c', 'h', 'e'),
            Trigram('i', 'n', ' '),
            Trigram('o', ' ', 's'),
            Trigram('e', ' ', 's'),
            Trigram(' ', 'q', 'u'),
            Trigram('o', ' ', 'e'),
            Trigram('i', 'a', ' '),
            Trigram('e', ' ', 'c'),
            Trigram(' ', 'r', 'i'),
            Trigram('n', 'z', 'a'),
            Trigram('t', 'a', ' '),
            Trigram('n', 't', 'o'),
            Trigram('h', 'e', ' '),
            Trigram('o', 'n', 'i'),
            Trigram('o', ' ', 'i'),
            Trigram(' ', 'o', ' '),
            Trigram('s', 't', 'a'),
            Trigram('o', ' ', 'c'),
            Trigram('n', 'e', 'l'),
            Trigram(' ', 'a', ' '),
            Trigram('o', ' ', 'p'),
            Trigram('n', 'a', 'z'),
            Trigram('e', ' ', 'o'),
            Trigram('s', 'o', ' '),
            Trigram(' ', 'p', 'o'),
            Trigram('o', ' ', 'h'),
            Trigram('g', 'l', 'i'),
            Trigram('i', ' ', 'u'),
            Trigram('o', 'n', 'd'),
            Trigram('i', ' ', 'c'),
            Trigram('e', 'r', 's'),
            Trigram('a', 'm', 'e'),
            Trigram('i', ' ', 'p'),
            Trigram('l', 'l', 'e'),
            Trigram('u', 'n', ' '),
            Trigram('e', 'r', 'a'),
            Trigram('r', 'i', ' '),
            Trigram('v', 'e', 'r'),
            Trigram('r', 'o', ' '),
            Trigram('e', 'l', ' '),
            Trigram('u', 'n', 'a'),
            Trigram('a', ' ', 'c'),
            Trigram(' ', 'c', 'h'),
            Trigram('e', 'r', 't'),
            Trigram('u', 'a', ' '),
            Trigram('i', ' ', 'a'),
            Trigram('s', 's', 'i'),
            Trigram('r', 't', 'à'),
            Trigram('a', ' ', 'e'),
            Trigram('e', 'i', ' '),
            Trigram('d', 'i', 's'),
            Trigram('a', 'n', 't'),
            Trigram(' ', 'l', ' '),
            Trigram('t', 'a', 't'),
            Trigram('a', ' ', 'a'),
            Trigram('o', 'n', 'a'),
            Trigram('u', 'a', 'l'),
            Trigram(' ', 'l', 'e'),
            Trigram('i', 't', 'à'),
            Trigram('a', 'r', 'e'),
            Trigram('t', 'e', 'r'),
            Trigram(' ', 'a', 'd'),
            Trigram('n', 'i', 't'),
            Trigram(' ', 'd', 'a'),
            Trigram('p', 'r', 'i'),
            Trigram('d', 'e', 'i'),
            Trigram('à', ' ', 'e'),
            Trigram('c', 'i', 'a'),
            Trigram(' ', 's', 't'),
            Trigram(' ', 's', 'i'),
            Trigram('n', 'a', 'l'),
            Trigram('e', 's', 't'),
            Trigram('t', 'u', 't'),
            Trigram('i', 's', 't'),
            Trigram('c', 'o', 'm'),
            Trigram('u', 'n', 'i'),
            Trigram(' ', 'e', 'd'),
            Trigram('o', 'n', 'o'),
            Trigram(' ', 'n', 'a'),
            Trigram('s', 'u', 'a'),
            Trigram('a', 'l', ' '),
            Trigram('s', 'i', ' '),
            Trigram('a', 'n', 'z'),
            Trigram(' ', 'p', 'a'),
            Trigram(' ', 'r', 'e'),
            Trigram('r', 'a', 'z'),
            Trigram('g', 'u', 'a'),
            Trigram('i', 't', 'a'),
            Trigram('r', 'e', 's'),
            Trigram('d', 'e', 'r'),
            Trigram('s', 'o', 'c'),
            Trigram('m', 'a', 'n'),
            Trigram('o', ' ', 'o'),
            Trigram('a', 'd', ' '),
            Trigram('i', ' ', 'o'),
            Trigram('e', 's', 'e'),
            Trigram('q', 'u', 'e'),
            Trigram('e', 'n', 'z'),
            Trigram('e', 'd', ' '),
            Trigram(' ', 's', 'e'),
            Trigram('i', 'o', ' '),
            Trigram('e', 't', 't'),
            Trigram('o', 'n', ' '),
            Trigram(' ', 't', 'u'),
            Trigram('d', 'i', 'c'),
            Trigram('à', ' ', 'd'),
            Trigram('s', 'i', 'a'),
            Trigram('i', ' ', 'r'),
            Trigram('r', 's', 'o'),
            Trigram('o', 'c', 'i'),
            Trigram('r', 'i', 'o'),
            Trigram('a', 'r', 'i'),
            Trigram('q', 'u', 'a'),
            Trigram('i', 'a', 'l'),
            Trigram('p', 'r', 'e'),
            Trigram('i', 'c', 'h'),
            Trigram('r', 'a', 't'),
            Trigram('i', 'e', 'n'),
            Trigram('t', 'r', 'a'),
            Trigram('a', 'n', 'i'),
            Trigram('u', 'm', 'a'),
            Trigram('s', 'e', ' '),
            Trigram('l', 'l', ' '),
            Trigram('e', 'r', 'i'),
            Trigram('a', ' ', 'n'),
            Trigram('o', ' ', 'n'),
            Trigram(' ', 'u', 'm'),
            Trigram('d', 'o', ' '),
            Trigram('a', 'r', 'a'),
            Trigram('a', ' ', 't'),
            Trigram('z', 'z', 'a'),
            Trigram('e', 'r', ' '),
            Trigram('t', 'r', 'i'),
            Trigram('a', 't', 't'),
            Trigram('i', 'c', 'o'),
            Trigram('p', 'o', 's'),
            Trigram('s', 'c', 'i'),
            Trigram('i', ' ', 'l'),
            Trigram('s', 'o', 'n'),
            Trigram('n', 'd', 'a'),
            Trigram('p', 'a', 'r'),
            Trigram('e', ' ', 'u'),
            Trigram('f', 'o', 'n'),
            Trigram(' ', 'f', 'o'),
            Trigram('n', 't', 'i'),
            Trigram('u', 'z', 'i'),
            Trigram('s', 't', 'r'),
            Trigram('u', 't', 't'),
            Trigram('a', 't', 'i'),
            Trigram('s', 'e', 'n'),
            Trigram('i', 'n', 't'),
            Trigram('n', 'e', 's'),
            Trigram('i', 'a', 'r'),
            Trigram(' ', 'i', ' '),
            Trigram('h', 'i', 'a'),
            Trigram('n', ' ', 'c'),
            Trigram('s', 't', 'i'),
            Trigram('c', 'h', 'i'),
            Trigram('a', 'n', 'n'),
            Trigram('r', 'a', ' '),
            Trigram(' ', 'e', 'g'),
            Trigram('e', 'g', 'u'),
            Trigram('i', 's', 'p'),
            Trigram('b', 'i', 'l'),
            Trigram('o', 'n', 't'),
            Trigram('a', ' ', 'r'),
            Trigram(' ', 'n', 'o'),
            Trigram('r', 'o', 'p'),
            Trigram(' ', 'm', 'e'),
            Trigram('o', 'p', 'r'),
            Trigram('o', 's', 't'),
            Trigram(' ', 'm', 'a'),
            Trigram('u', 'e', 's'),
            Trigram('i', 'c', 'a'),
            Trigram('s', 's', 'o'),
            Trigram('t', 'a', 'l'),
            Trigram('c', 'i', 'e'),
            Trigram('s', 'u', 'n'),
            Trigram('l', 'i', 't'),
            Trigram('o', 'r', 'e'),
            Trigram('i', 'n', 'a'),
            Trigram('i', 't', 'e'),
            Trigram('t', 'a', 'n'),
            Trigram(' ', 'r', 'a'),
            Trigram('n', 'o', 'n'),
            Trigram('g', 'i', 'o'),
            Trigram('d', ' ', 'a'),
            Trigram('e', ' ', 'r'),
            Trigram('d', 'e', 'v'),
            Trigram('i', ' ', 'm'),
            Trigram('l', ' ', 'i'),
            Trigram('e', 'z', 'z'),
            Trigram('i', 'z', 'i'),
            Trigram(' ', 'c', 'u'),
            Trigram('n', 'n', 'o'),
            Trigram('r', 'à', ' '),
            Trigram('a', ' ', 'i'),
            Trigram('t', 't', 'a'),
            Trigram('r', 'i', 'a'),
            Trigram('l', 'i', 'a'),
            Trigram('c', 'o', 's'),
            Trigram('s', 's', 'u'),
            Trigram('d', 'a', 'l'),
            Trigram('l', ' ', 'p'),
            Trigram(' ', 'a', 's'),
            Trigram('a', 's', 's'),
            Trigram('o', 'p', 'o'),
            Trigram('v', 'e', ' '),
            Trigram('e', 'v', 'e'),
        ],
    ),
    (
        Lang::Tur,
        &[
            Trigram(' ', 'v', 'e'),
            Trigram(' ', 'h', 'a'),
            Trigram('v', 'e', ' '),
            Trigram('l', 'e', 'r'),
            Trigram('l', 'a', 'r'),
            Trigram('i', 'r', ' '),
            Trigram('i', 'n', ' '),
            Trigram('h', 'a', 'k'),
            Trigram(' ', 'h', 'e'),
            Trigram('h', 'e', 'r'),
            Trigram('b', 'i', 'r'),
            Trigram('e', 'r', ' '),
            Trigram('a', 'n', ' '),
            Trigram('a', 'r', 'ı'),
            Trigram('e', 'r', 'i'),
            Trigram('y', 'a', ' '),
            Trigram(' ', 'b', 'i'),
            Trigram('a', 'k', ' '),
            Trigram('r', ' ', 'h'),
            Trigram('e', 't', 'i'),
            Trigram('ı', 'n', ' '),
            Trigram('i', 'y', 'e'),
            Trigram('y', 'e', 't'),
            Trigram(' ', 'k', 'a'),
            Trigram('a', 's', 'ı'),
            Trigram('ı', 'n', 'ı'),
            Trigram(' ', 'o', 'l'),
            Trigram('t', 'l', 'e'),
            Trigram('e', 'y', 'a'),
            Trigram('k', 'k', 'ı'),
            Trigram('a', 'r', 'a'),
            Trigram('a', 'k', 'k'),
            Trigram('e', 't', 'l'),
            Trigram('s', 'ı', 'n'),
            Trigram('e', 's', 'i'),
            Trigram('n', 'a', ' '),
            Trigram('d', 'e', ' '),
            Trigram('e', 'k', ' '),
            Trigram(' ', 't', 'a'),
            Trigram('n', 'd', 'a'),
            Trigram('i', 'n', 'i'),
            Trigram(' ', 'b', 'u'),
            Trigram('i', 'l', 'e'),
            Trigram('r', 'ı', 'n'),
            Trigram('r', 'i', 'n'),
            Trigram('v', 'e', 'y'),
            Trigram('n', 'e', ' '),
            Trigram('k', 'l', 'a'),
            Trigram('e', ' ', 'h'),
            Trigram('i', 'n', 'e'),
            Trigram('ı', 'r', ' '),
            Trigram('e', 'r', 'e'),
            Trigram('a', 'm', 'a'),
            Trigram('d', 'ı', 'r'),
            Trigram('n', ' ', 'h'),
            Trigram(' ', 's', 'a'),
            Trigram('ı', 'n', 'a'),
            Trigram('s', 'i', 'n'),
            Trigram('e', ' ', 'k'),
            Trigram('l', 'e', ' '),
            Trigram(' ', 'g', 'e'),
            Trigram('m', 'a', 's'),
            Trigram('ı', 'n', 'd'),
            Trigram('n', 'ı', 'n'),
            Trigram('ı', ' ', 'v'),
            Trigram(' ', 'v', 'a'),
            Trigram('l', 'a', 'n'),
            Trigram('l', 'm', 'a'),
            Trigram('e', 'r', 'k'),
            Trigram('r', 'k', 'e'),
            Trigram('n', 'm', 'a'),
            Trigram('t', 'i', 'n'),
            Trigram('r', 'l', 'e'),
            Trigram(' ', 't', 'e'),
            Trigram('n', 'i', 'n'),
            Trigram('a', 'k', 'l'),
            Trigram('a', ' ', 'v'),
            Trigram('d', 'a', ' '),
            Trigram(' ', 'd', 'e'),
            Trigram('l', 'e', 't'),
            Trigram('i', 'l', 'l'),
            Trigram('e', ' ', 'm'),
            Trigram('a', 'r', 'd'),
            Trigram('e', 'n', ' '),
            Trigram('r', 'i', 'y'),
            Trigram('a', 'y', 'a'),
            Trigram('n', 'ı', ' '),
            Trigram(' ', 'h', 'ü'),
            Trigram(' ', 'ş', 'a'),
            Trigram('e', ' ', 'b'),
            Trigram('k', ' ', 'v'),
            Trigram('k', 'ı', 'n'),
            Trigram('k', ' ', 'h'),
            Trigram(' ', 'm', 'e'),
            Trigram('m', 'i', 'l'),
            Trigram('s', 'a', 'n'),
            Trigram(' ', 'i', 'l'),
            Trigram('s', 'i', ' '),
            Trigram('r', 'd', 'ı'),
            Trigram('e', ' ', 'd'),
            Trigram('d', 'a', 'n'),
            Trigram('h', 'ü', 'r'),
            Trigram('v', 'a', 'r'),
            Trigram('a', 'n', 'a'),
            Trigram('e', ' ', 'a'),
            Trigram('k', 'e', 's'),
            Trigram('e', 't', ' '),
            Trigram('m', 'e', 's'),
            Trigram('ş', 'a', 'h'),
            Trigram('d', 'i', 'r'),
            Trigram(' ', 'm', 'i'),
            Trigram('r', 'e', 't'),
            Trigram('r', 'r', 'i'),
            Trigram(' ', 's', 'e'),
            Trigram('o', 'l', 'a'),
            Trigram('ü', 'r', 'r'),
            Trigram('i', 'r', 'l'),
            Trigram('b', 'u', ' '),
            Trigram('m', 'a', 'k'),
            Trigram(' ', 'm', 'a'),
            Trigram('m', 'e', 'k'),
            Trigram('n', ' ', 'e'),
            Trigram('k', 'ı', ' '),
            Trigram('n', ' ', 'v'),
            Trigram('n', ' ', 'i'),
            Trigram('l', 'i', 'k'),
            Trigram('l', 'l', 'e'),
            Trigram(' ', 'e', 'd'),
            Trigram(' ', 'h', 'i'),
            Trigram('n', ' ', 'b'),
            Trigram('a', ' ', 'h'),
            Trigram(' ', 'b', 'a'),
            Trigram('n', 's', 'a'),
            Trigram(' ', 'i', 'ş'),
            Trigram('e', 'l', 'i'),
            Trigram('k', 'a', 'r'),
            Trigram(' ', 'i', 'ç'),
            Trigram('ı', ' ', 'h'),
            Trigram('a', 'l', 'a'),
            Trigram('l', 'i', ' '),
            Trigram('u', 'l', 'u'),
            Trigram('r', 'a', 'k'),
            Trigram('e', 'v', 'l'),
            Trigram('e', ' ', 'i'),
            Trigram('n', 'i', ' '),
            Trigram('r', 'e', ' '),
            Trigram('r', ' ', 'ş'),
            Trigram('e', 'm', 'e'),
            Trigram('e', 't', 'm'),
            Trigram('e', ' ', 't'),
            Trigram('i', 'k', ' '),
            Trigram('e', ' ', 's'),
            Trigram('a', ' ', 'b'),
            Trigram('i', 'ş', ' '),
            Trigram('n', ' ', 'k'),
            Trigram('h', 'a', 'i'),
            Trigram('n', 'd', 'e'),
            Trigram('a', 'i', 'z'),
            Trigram(' ', 'e', 'ş'),
            Trigram('i', 'z', 'd'),
            Trigram('u', 'n', ' '),
            Trigram('o', 'l', 'm'),
            Trigram('h', 'i', 'ç'),
            Trigram('z', 'd', 'i'),
            Trigram('a', 'r', ' '),
            Trigram('u', 'n', 'm'),
            Trigram('m', 'a', ' '),
            Trigram(' ', 'g', 'ö'),
            Trigram('i', 'l', 'm'),
            Trigram('l', 'm', 'e'),
            Trigram('i', 'm', ' '),
            Trigram('n', ' ', 't'),
            Trigram('t', 'i', 'r'),
            Trigram('d', 'i', 'l'),
            Trigram('m', 'a', 'l'),
            Trigram('e', ' ', 'g'),
            Trigram('i', ' ', 'v'),
            Trigram(' ', 'k', 'o'),
            Trigram('l', 'u', 'n'),
            Trigram('e', ' ', 'e'),
            Trigram('m', 'e', 'l'),
            Trigram('k', 'e', 't'),
            Trigram('ı', 'k', ' '),
            Trigram('n', ' ', 's'),
            Trigram('e', 'l', 'e'),
            Trigram('l', 'a', ' '),
            Trigram('e', 'l', ' '),
            Trigram('r', ' ', 'v'),
            Trigram('e', 'd', 'e'),
            Trigram('ş', 'i', 't'),
            Trigram('i', 'l', 'i'),
            Trigram('e', 'ş', 'i'),
            Trigram('y', 'l', 'a'),
            Trigram('a', ' ', 'i'),
            Trigram(' ', 'a', 'n'),
            Trigram('a', 'n', 'ı'),
            Trigram(' ', 'e', 't'),
            Trigram('r', 'ı', ' '),
            Trigram('a', 'h', 's'),
            Trigram(' ', 'y', 'a'),
            Trigram('s', 'ı', ' '),
            Trigram('e', 'd', 'i'),
            Trigram('s', 'i', 'y'),
            Trigram('t', ' ', 'v'),
            Trigram('i', ' ', 'b'),
            Trigram('s', 'e', ' '),
            Trigram('i', 'ç', 'i'),
            Trigram('ç', 'i', 'n'),
            Trigram('b', 'u', 'l'),
            Trigram('a', 'm', 'e'),
            Trigram(' ', 'd', 'a'),
            Trigram('m', 'i', 'ş'),
            Trigram('m', 'a', 'y'),
            Trigram('t', 'i', 'm'),
            Trigram('a', ' ', 'k'),
            Trigram('t', 'm', 'e'),
            Trigram('r', ' ', 'b'),
            Trigram('i', 'n', 's'),
            Trigram('y', 'a', 'n'),
            Trigram('n', 'l', 'a'),
            Trigram('m', 'l', 'e'),
            Trigram(' ', 'd', 'i'),
            Trigram('e', 'y', 'e'),
            Trigram('g', 'e', 'r'),
            Trigram('y', 'e', ' '),
            Trigram('u', 'ğ', 'u'),
            Trigram('e', 'r', 'd'),
            Trigram('d', 'i', 'n'),
            Trigram('s', 'e', 'r'),
            Trigram(' ', 'm', 'ü'),
            Trigram('m', 'e', 'm'),
            Trigram('v', 'l', 'e'),
            Trigram(' ', 'k', 'e'),
            Trigram('n', 'a', 'm'),
            Trigram('i', 'n', 'd'),
            Trigram('l', 'e', 'n'),
            Trigram('e', 'k', 'e'),
            Trigram('e', 's', ' '),
            Trigram(' ', 'k', 'i'),
            Trigram('n', ' ', 'm'),
            Trigram('i', 't', ' '),
            Trigram(' ', 'i', 'n'),
            Trigram(' ', 'k', 'u'),
            Trigram('r', 'ş', 'ı'),
            Trigram('a', ' ', 's'),
            Trigram('a', 'r', 'ş'),
            Trigram(' ', 'a', 'y'),
            Trigram('e', 'm', 'l'),
            Trigram('l', 'e', 'k'),
            Trigram('o', 'r', 'u'),
            Trigram('r', 'm', 'e'),
            Trigram('k', 'o', 'r'),
            Trigram('r', 'd', 'e'),
            Trigram('i', ' ', 'm'),
            Trigram(' ', 's', 'o'),
            Trigram('t', 'ü', 'r'),
            Trigram('a', 'l', ' '),
            Trigram('l', 'a', 'm'),
            Trigram('e', 'n', 'i'),
            Trigram('n', 'u', 'n'),
            Trigram(' ', 'u', 'y'),
            Trigram('k', 'e', 'n'),
            Trigram('h', 's', 'ı'),
            Trigram('i', ' ', 'i'),
            Trigram('a', ' ', 'd'),
            Trigram('r', 'i', ' '),
            Trigram('d', 'e', 'v'),
            Trigram('ü', 'n', ' '),
            Trigram('a', ' ', 'm'),
            Trigram('r', ' ', 'a'),
            Trigram('m', 'e', 'y'),
            Trigram('c', 'a', 'k'),
            Trigram('ı', 'y', 'l'),
            Trigram('m', 'a', 'z'),
            Trigram('e', ' ', 'v'),
            Trigram('e', 'c', 'e'),
            Trigram('a', 'd', 'e'),
            Trigram('i', 'ç', ' '),
            Trigram('ş', 'm', 'a'),
            Trigram('m', 's', 'e'),
            Trigram('t', 'e', ' '),
            Trigram('t', 'ü', 'n'),
            Trigram('i', 'm', 's'),
            Trigram('k', 'i', 'm'),
            Trigram('e', ' ', 'y'),
            Trigram('ş', 'ı', ' '),
            Trigram('e', 'n', 'd'),
            Trigram('k', ' ', 'g'),
            Trigram('n', 'd', 'i'),
            Trigram('a', 'l', 'ı'),
            Trigram(' ', 'c', 'e'),
            Trigram('l', 'e', 'm'),
            Trigram('ö', 'ğ', 'r'),
            Trigram('ü', 't', 'ü'),
            Trigram('k', ' ', 'i'),
            Trigram('r', ' ', 't'),
            Trigram(' ', 'ö', 'ğ'),
            Trigram('b', 'ü', 't'),
            Trigram('a', 'n', 'l'),
            Trigram(' ', 'b', 'ü'),
        ],
    ),
    (
        Lang::Pol,
        &[
            Trigram(' ', 'p', 'r'),
            Trigram('n', 'i', 'e'),
            Trigram(' ', 'i', ' '),
            Trigram('i', 'e', ' '),
            Trigram('p', 'r', 'a'),
            Trigram(' ', 'p', 'o'),
            Trigram('a', 'n', 'i'),
            Trigram('r', 'a', 'w'),
            Trigram('i', 'a', ' '),
            Trigram('n', 'i', 'a'),
            Trigram('w', 'i', 'e'),
            Trigram('g', 'o', ' '),
            Trigram(' ', 'd', 'o'),
            Trigram('c', 'h', ' '),
            Trigram('e', 'g', 'o'),
            Trigram('i', 'e', 'k'),
            Trigram('o', 'w', 'i'),
            Trigram(' ', 'n', 'i'),
            Trigram('ś', 'c', 'i'),
            Trigram('c', 'i', ' '),
            Trigram('a', ' ', 'p'),
            Trigram('d', 'o', ' '),
            Trigram('a', 'w', 'o'),
            Trigram(' ', 'c', 'z'),
            Trigram('o', 'ś', 'c'),
            Trigram('y', 'c', 'h'),
            Trigram(' ', 'm', 'a'),
            Trigram('e', 'k', ' '),
            Trigram('r', 'z', 'e'),
            Trigram(' ', 'n', 'a'),
            Trigram('p', 'r', 'z'),
            Trigram(' ', 'w', ' '),
            Trigram('w', 'o', ' '),
            Trigram('e', 'j', ' '),
            Trigram(' ', 'z', 'a'),
            Trigram('n', 'o', 'ś'),
            Trigram('c', 'z', 'ł'),
            Trigram('z', 'ł', 'o'),
            Trigram('e', 'n', 'i'),
            Trigram('w', 'a', ' '),
            Trigram(' ', 'j', 'e'),
            Trigram('ł', 'o', 'w'),
            Trigram('i', ' ', 'p'),
            Trigram('w', 'o', 'l'),
            Trigram('o', 'l', 'n'),
            Trigram(' ', 'l', 'u'),
            Trigram('r', 'o', 'd'),
            Trigram(' ', 'k', 'a'),
            Trigram(' ', 'w', 'o'),
            Trigram('l', 'n', 'o'),
            Trigram('w', 's', 'z'),
            Trigram('y', ' ', 'c'),
            Trigram('m', 'a', ' '),
            Trigram('n', 'y', ' '),
            Trigram('k', 'a', 'ż'),
            Trigram('a', 'ż', 'd'),
            Trigram('o', ' ', 'd'),
            Trigram('s', 't', 'w'),
            Trigram('o', 'w', 'a'),
            Trigram('d', 'y', ' '),
            Trigram('ż', 'd', 'y'),
            Trigram(' ', 'w', 'y'),
            Trigram('r', 'z', 'y'),
            Trigram('s', 't', 'a'),
            Trigram('e', 'c', 'z'),
            Trigram(' ', 's', 'w'),
            Trigram('d', 'z', 'i'),
            Trigram('i', ' ', 'w'),
            Trigram('e', ' ', 'p'),
            Trigram('c', 'z', 'n'),
            Trigram('t', 'w', 'a'),
            Trigram('n', 'a', ' '),
            Trigram('z', 'y', 's'),
            Trigram('ó', 'w', ' '),
            Trigram('s', 'z', 'y'),
            Trigram('u', 'b', ' '),
            Trigram('l', 'u', 'b'),
            Trigram('a', ' ', 'w'),
            Trigram('e', 's', 't'),
            Trigram('k', 'i', 'e'),
            Trigram('k', ' ', 'm'),
            Trigram('w', 'a', 'n'),
            Trigram(' ', 's', 'p'),
            Trigram('a', 'j', 'ą'),
            Trigram(' ', 'w', 's'),
            Trigram('e', ' ', 'w'),
            Trigram('p', 'o', 'w'),
            Trigram('p', 'o', 's'),
            Trigram('n', 'y', 'c'),
            Trigram('r', 'a', 'c'),
            Trigram('s', 'p', 'o'),
            Trigram('a', 'ć', ' '),
            Trigram('a', ' ', 'i'),
            Trigram('c', 'z', 'e'),
            Trigram('s', 'z', 'e'),
            Trigram('n', 'e', 'g'),
            Trigram('y', 's', 't'),
            Trigram('j', 'a', 'k'),
            Trigram(' ', 'j', 'a'),
            Trigram('o', ' ', 'p'),
            Trigram('p', 'o', 'd'),
            Trigram('a', 'c', 'j'),
            Trigram('n', 'e', ' '),
            Trigram('ń', 's', 't'),
            Trigram('a', 'r', 'o'),
            Trigram('m', 'i', ' '),
            Trigram(' ', 'z', ' '),
            Trigram('i', ' ', 'i'),
            Trigram('n', 'a', 'r'),
            Trigram(' ', 'k', 'o'),
            Trigram('o', 'b', 'o'),
            Trigram('a', 'w', 'a'),
            Trigram(' ', 'r', 'o'),
            Trigram('i', ' ', 'n'),
            Trigram('j', 'ą', 'c'),
            Trigram('z', 'e', 'c'),
            Trigram('z', 'n', 'e'),
            Trigram('z', 'a', 'n'),
            Trigram('d', 'o', 'w'),
            Trigram(' ', 'r', 'ó'),
            Trigram('i', 'e', 'j'),
            Trigram('z', 'y', ' '),
            Trigram('z', 'e', 'n'),
            Trigram('n', 'i', 'c'),
            Trigram('o', 'n', 'y'),
            Trigram('a', 'w', ' '),
            Trigram('i', ' ', 'z'),
            Trigram('c', 'z', 'y'),
            Trigram('n', 'o', ' '),
            Trigram('n', 'e', 'j'),
            Trigram('o', ' ', 's'),
            Trigram('r', 'ó', 'w'),
            Trigram('o', 'd', 'n'),
            Trigram('c', 'y', ' '),
            Trigram('ó', 'w', 'n'),
            Trigram('o', 'd', 'z'),
            Trigram('o', ' ', 'w'),
            Trigram('o', ' ', 'z'),
            Trigram('j', 'e', 'g'),
            Trigram('e', 'd', 'n'),
            Trigram('o', ' ', 'o'),
            Trigram('a', 'k', 'i'),
            Trigram('m', 'i', 'e'),
            Trigram('i', 'e', 'n'),
            Trigram('k', 'o', 'l'),
            Trigram(' ', 'i', 'n'),
            Trigram('z', 'i', 'e'),
            Trigram('b', 'e', 'z'),
            Trigram('a', 'm', 'i'),
            Trigram('e', 'ń', 's'),
            Trigram('o', 'w', 'o'),
            Trigram('d', 'n', 'o'),
            Trigram(' ', 'o', 'b'),
            Trigram(' ', 'o', 'r'),
            Trigram(' ', 's', 't'),
            Trigram('a', ' ', 's'),
            Trigram('n', 'i', ' '),
            Trigram('o', 'r', 'z'),
            Trigram('o', ' ', 'u'),
            Trigram('y', 'm', ' '),
            Trigram('s', 't', 'ę'),
            Trigram('t', 'ę', 'p'),
            Trigram('ł', 'e', 'c'),
            Trigram('j', 'e', 'd'),
            Trigram('i', ' ', 'k'),
            Trigram(' ', 'o', 's'),
            Trigram('w', ' ', 'c'),
            Trigram('l', 'w', 'i'),
            Trigram('e', 'z', ' '),
            Trigram('o', 'l', 'w'),
            Trigram('o', 'ł', 'e'),
            Trigram('p', 'o', 'ł'),
            Trigram('c', 'j', 'i'),
            Trigram('y', ' ', 'w'),
            Trigram('o', ' ', 'n'),
            Trigram('w', 'i', 'a'),
            Trigram(' ', 'b', 'e'),
            Trigram('k', 't', 'ó'),
            Trigram('a', ' ', 'j'),
            Trigram('z', 'n', 'a'),
            Trigram('z', 'y', 'n'),
            Trigram('o', 'w', 'e'),
            Trigram('w', 'o', 'b'),
            Trigram('k', 'a', ' '),
            Trigram('w', 'y', 'c'),
            Trigram('o', 'w', 'y'),
            Trigram('j', 'i', ' '),
            Trigram(' ', 'o', 'd'),
            Trigram('a', 'l', 'n'),
            Trigram('i', 'n', 'n'),
            Trigram('j', 'e', 's'),
            Trigram('i', 'c', 'z'),
            Trigram('h', ' ', 'p'),
            Trigram('i', ' ', 's'),
            Trigram('s', 'i', 'ę'),
            Trigram('a', ' ', 'o'),
            Trigram('j', 'ą', ' '),
            Trigram('o', 's', 't'),
            Trigram('k', 'r', 'a'),
            Trigram('s', 't', ' '),
            Trigram('s', 'z', 'a'),
            Trigram('s', 'w', 'o'),
            Trigram('w', 'a', 'r'),
            Trigram('c', 'z', 'a'),
            Trigram('r', 'o', 'z'),
            Trigram('y', ' ', 's'),
            Trigram('r', 'a', 'z'),
            Trigram('n', 'i', 'k'),
            Trigram('a', 'r', 'a'),
            Trigram('o', 'r', 'a'),
            Trigram('l', 'u', 'd'),
            Trigram('i', ' ', 'o'),
            Trigram('a', ' ', 'z'),
            Trigram('z', 'e', 's'),
            Trigram(' ', 'k', 'r'),
            Trigram('r', 'a', 'n'),
            Trigram('o', 'w', 's'),
            Trigram('e', 'c', 'h'),
            Trigram('w', ' ', 'p'),
            Trigram('d', 'ó', 'w'),
            Trigram('ą', ' ', 'p'),
            Trigram('p', 'o', 'p'),
            Trigram('a', ' ', 'n'),
            Trigram('t', 'k', 'i'),
            Trigram('s', 't', 'k'),
            Trigram('g', 'a', 'n'),
            Trigram('z', 'o', 'n'),
            Trigram('r', 'a', 'j'),
            Trigram('e', ' ', 'o'),
            Trigram('i', 'e', 'c'),
            Trigram('i', ' ', 'l'),
            Trigram(' ', 's', 'i'),
            Trigram('ż', 'e', ' '),
            Trigram('e', 'k', 'a'),
            Trigram(' ', 'k', 't'),
            Trigram(' ', 'd', 'e'),
            Trigram('e', 'm', ' '),
            Trigram('t', 'ó', 'r'),
            Trigram('i', 'ę', ' '),
            Trigram('w', 'n', 'i'),
            Trigram('l', 'n', 'i'),
            Trigram('e', 'j', 's'),
            Trigram('i', 'n', 'i'),
            Trigram('o', 'd', 'o'),
            Trigram('d', 'n', 'i'),
            Trigram('e', 'ł', 'n'),
            Trigram('k', 'o', 'w'),
            Trigram('p', 'e', 'ł'),
            Trigram('a', ' ', 'd'),
            Trigram('r', 'o', 'n'),
            Trigram('d', 'e', 'k'),
            Trigram('p', 'i', 'e'),
            Trigram('u', 'd', 'z'),
            Trigram('b', 'o', 'd'),
            Trigram('n', 'a', 'n'),
            Trigram('h', ' ', 'i'),
            Trigram('d', 's', 't'),
            Trigram('i', 'e', 'g'),
            Trigram('t', 'a', 'w'),
            Trigram('z', ' ', 'p'),
            Trigram('z', ' ', 'w'),
            Trigram('z', 'e', 'ń'),
            Trigram('g', 'o', 'd'),
            Trigram('i', 'u', ' '),
            Trigram('a', 'n', 'o'),
            Trigram('l', 'a', 'r'),
            Trigram(' ', 't', 'o'),
            Trigram('y', ' ', 'z'),
            Trigram('a', ' ', 'k'),
            Trigram('a', 'l', 'e'),
            Trigram('k', 'l', 'a'),
            Trigram('t', 'r', 'z'),
            Trigram('z', 'a', 'w'),
            Trigram('i', 'c', 'h'),
            Trigram('e', ' ', 'i'),
            Trigram('i', 'e', 'r'),
            Trigram('i', 'k', 'o'),
            Trigram('d', 'z', 'y'),
            Trigram('c', 'h', 'n'),
            Trigram('w', ' ', 'z'),
            Trigram('b', 'y', ' '),
            Trigram('k', 'ó', 'w'),
            Trigram('a', 'd', 'z'),
            Trigram('e', 'k', 'l'),
            Trigram('y', 'w', 'a'),
            Trigram('j', 'u', ' '),
            Trigram('o', 'c', 'h'),
            Trigram('k', 'o', 'r'),
            Trigram('s', 'o', 'b'),
            Trigram('o', 'c', 'z'),
            Trigram('o', 's', 'o'),
            Trigram('u', ' ', 'p'),
            Trigram('d', 'u', ' '),
            Trigram('t', 'y', 'c'),
            Trigram('t', 'a', 'n'),
            Trigram('ę', 'd', 'z'),
            Trigram(' ', 'm', 'i'),
            Trigram('e', ' ', 's'),
            Trigram(' ', 't', 'a'),
            Trigram('k', 'i', ' '),
        ],
    ),
    (
        Lang::Ron,
        &[
            Trigram(' ', 'd', 'e'),
            Trigram('ș', 'i', ' '),
            Trigram(' ', 'ș', 'i'),
            Trigram('r', 'e', ' '),
            Trigram(' ', 'î', 'n'),
            Trigram('a', 'r', 'e'),
            Trigram('t', 'e', ' '),
            Trigram('d', 'e', ' '),
            Trigram('e', 'a', ' '),
            Trigram('u', 'l', ' '),
            Trigram('r', 'e', 'p'),
            Trigram('l', 'e', ' '),
            Trigram('e', 'p', 't'),
            Trigram('d', 'r', 'e'),
            Trigram('e', ' ', 'd'),
            Trigram(' ', 'd', 'r'),
            Trigram('i', 'e', ' '),
            Trigram('î', 'n', ' '),
            Trigram('e', ' ', 'a'),
            Trigram('a', 't', 'e'),
            Trigram('p', 't', 'u'),
            Trigram(' ', 's', 'a'),
            Trigram('t', 'u', 'l'),
            Trigram(' ', 'p', 'r'),
            Trigram('o', 'r', ' '),
            Trigram('e', ' ', 'p'),
            Trigram(' ', 'p', 'e'),
            Trigram('l', 'a', ' '),
            Trigram('e', ' ', 's'),
            Trigram('o', 'r', 'i'),
            Trigram(' ', 'l', 'a'),
            Trigram(' ', 'c', 'o'),
            Trigram('l', 'o', 'r'),
            Trigram(' ', 'o', 'r'),
            Trigram('i', 'i', ' '),
            Trigram('r', 'e', 'a'),
            Trigram('c', 'e', ' '),
            Trigram('a', 'u', ' '),
            Trigram('t', 'a', 't'),
            Trigram('a', 'ț', 'i'),
            Trigram(' ', 'a', ' '),
            Trigram(' ', 'c', 'a'),
            Trigram('e', 'n', 't'),
            Trigram(' ', 'f', 'i'),
            Trigram('a', 'l', 'e'),
            Trigram('ă', ' ', 'a'),
            Trigram('a', ' ', 's'),
            Trigram(' ', 'a', 'r'),
            Trigram('e', 'r', 's'),
            Trigram('p', 'e', 'r'),
            Trigram('i', 'c', 'e'),
            Trigram(' ', 'l', 'i'),
            Trigram('u', 'r', 'i'),
            Trigram('a', ' ', 'd'),
            Trigram('a', 'l', ' '),
            Trigram(' ', 'r', 'e'),
            Trigram('e', ' ', 'c'),
            Trigram('r', 'i', 'c'),
            Trigram('n', 'ă', ' '),
            Trigram('i', ' ', 's'),
            Trigram('e', ' ', 'o'),
            Trigram('e', 'i', ' '),
            Trigram('t', 'u', 'r'),
            Trigram(' ', 's', 'ă'),
            Trigram('l', 'i', 'b'),
            Trigram('c', 'o', 'n'),
            Trigram('m', 'e', 'n'),
            Trigram('i', 'b', 'e'),
            Trigram('b', 'e', 'r'),
            Trigram('r', 's', 'o'),
            Trigram('s', 'ă', ' '),
            Trigram('t', 'ă', 'ț'),
            Trigram('s', 'a', 'u'),
            Trigram(' ', 'a', 'c'),
            Trigram('i', 'l', 'o'),
            Trigram('p', 'r', 'i'),
            Trigram('ă', 'ț', 'i'),
            Trigram('i', ' ', 'a'),
            Trigram('i', ' ', 'l'),
            Trigram('c', 'a', 'r'),
            Trigram('l', ' ', 'l'),
            Trigram('t', 'e', 'r'),
            Trigram(' ', 'i', 'n'),
            Trigram('ț', 'i', 'e'),
            Trigram('c', 'ă', ' '),
            Trigram('s', 'o', 'a'),
            Trigram('o', 'a', 'n'),
            Trigram('ț', 'i', 'i'),
            Trigram('l', 'ă', ' '),
            Trigram('t', 'e', 'a'),
            Trigram('r', 'i', ' '),
            Trigram('a', ' ', 'p'),
            Trigram(' ', 'a', 'l'),
            Trigram('r', 'i', 'l'),
            Trigram('e', ' ', 'ș'),
            Trigram('a', 'n', 'ă'),
            Trigram('i', 'n', ' '),
            Trigram('n', 'a', 'l'),
            Trigram('p', 'r', 'e'),
            Trigram('i', ' ', 'î'),
            Trigram('u', 'n', 'i'),
            Trigram('u', 'i', ' '),
            Trigram('s', 'e', ' '),
            Trigram('e', ' ', 'f'),
            Trigram('e', 'r', 'e'),
            Trigram('i', ' ', 'd'),
            Trigram('e', ' ', 'î'),
            Trigram('i', 't', 'a'),
            Trigram(' ', 'u', 'n'),
            Trigram('e', 'r', 't'),
            Trigram('i', 'l', 'e'),
            Trigram('t', 'ă', ' '),
            Trigram('a', ' ', 'o'),
            Trigram(' ', 's', 'e'),
            Trigram('i', ' ', 'ș'),
            Trigram('p', 'e', 'n'),
            Trigram('i', 'a', ' '),
            Trigram('e', 'l', 'e'),
            Trigram('f', 'i', 'e'),
            Trigram('i', ' ', 'c'),
            Trigram('a', ' ', 'l'),
            Trigram('a', 'c', 'e'),
            Trigram('n', 't', 'e'),
            Trigram('n', 't', 'r'),
            Trigram('e', 'n', 'i'),
            Trigram(' ', 'c', 'ă'),
            Trigram('a', 'l', 'ă'),
            Trigram(' ', 'n', 'i'),
            Trigram('i', 'r', 'e'),
            Trigram('ă', ' ', 'd'),
            Trigram('p', 'r', 'o'),
            Trigram('e', 's', 't'),
            Trigram('a', ' ', 'c'),
            Trigram(' ', 'c', 'u'),
            Trigram(' ', 'n', 'u'),
            Trigram('n', ' ', 'c'),
            Trigram('l', 'u', 'i'),
            Trigram('e', 'r', 'i'),
            Trigram('o', 'n', 'a'),
            Trigram(' ', 'a', 's'),
            Trigram('s', 'a', 'l'),
            Trigram('â', 'n', 'd'),
            Trigram('n', 'a', 'ț'),
            Trigram('e', 'c', 'u'),
            Trigram('i', ' ', 'p'),
            Trigram('r', 'i', 'n'),
            Trigram('i', 'n', 'ț'),
            Trigram(' ', 's', 'u'),
            Trigram('r', 'ă', ' '),
            Trigram('e', ' ', 'n'),
            Trigram(' ', 'o', 'm'),
            Trigram('i', 'c', 'i'),
            Trigram('n', 'u', ' '),
            Trigram('i', ' ', 'n'),
            Trigram('o', 'a', 't'),
            Trigram('ă', 'r', 'i'),
            Trigram('l', ' ', 'd'),
            Trigram(' ', 't', 'o'),
            Trigram('t', 'o', 'r'),
            Trigram(' ', 'd', 'i'),
            Trigram(' ', 'n', 'a'),
            Trigram('i', 'u', 'n'),
            Trigram(' ', 'p', 'o'),
            Trigram('o', 'c', 'i'),
            Trigram('t', 'r', 'e'),
            Trigram('n', 'i', ' '),
            Trigram('s', 't', 'e'),
            Trigram('s', 'o', 'c'),
            Trigram('e', 'g', 'a'),
            Trigram('i', ' ', 'o'),
            Trigram('g', 'a', 'l'),
            Trigram(' ', 's', 'o'),
            Trigram(' ', 't', 'r'),
            Trigram('ă', ' ', 'p'),
            Trigram('a', ' ', 'a'),
            Trigram('n', ' ', 'm'),
            Trigram('s', 't', 'a'),
            Trigram('v', 'a', ' '),
            Trigram('ă', ' ', 'î'),
            Trigram('f', 'i', ' '),
            Trigram('r', 'e', 's'),
            Trigram('r', 'e', 'c'),
            Trigram('u', 'l', 'u'),
            Trigram('n', 'i', 'c'),
            Trigram('d', 'i', 'n'),
            Trigram('s', 'a', ' '),
            Trigram('c', 'l', 'a'),
            Trigram('n', 'd', ' '),
            Trigram(' ', 'm', 'o'),
            Trigram(' ', 'c', 'e'),
            Trigram(' ', 'a', 'u'),
            Trigram('a', 'r', 'a'),
            Trigram('l', 'i', 't'),
            Trigram('i', 'n', 't'),
            Trigram('i', ' ', 'e'),
            Trigram('c', 'e', 's'),
            Trigram('u', 'i', 'e'),
            Trigram('a', 't', ' '),
            Trigram('r', 'a', 'r'),
            Trigram('r', 'e', 'l'),
            Trigram('i', 'e', 'i'),
            Trigram('o', 'n', 's'),
            Trigram('e', ' ', 'e'),
            Trigram('l', 'e', 'g'),
            Trigram('n', 'i', 't'),
            Trigram('ă', ' ', 'f'),
            Trigram(' ', 'î', 'm'),
            Trigram('a', ' ', 'î'),
            Trigram('a', 'c', 't'),
            Trigram('e', ' ', 'l'),
            Trigram('r', 'u', ' '),
            Trigram('u', ' ', 'd'),
            Trigram('n', 't', 'a'),
            Trigram('a', ' ', 'f'),
            Trigram('i', 'a', 'l'),
            Trigram('r', 'a', ' '),
            Trigram('ă', ' ', 'c'),
            Trigram(' ', 'e', 'g'),
            Trigram('ț', 'ă', ' '),
            Trigram(' ', 'f', 'a'),
            Trigram('i', ' ', 'f'),
            Trigram('r', 't', 'ă'),
            Trigram('t', 'r', 'u'),
            Trigram('t', 'a', 'r'),
            Trigram('ț', 'i', ' '),
            Trigram('ă', ' ', 'ș'),
            Trigram('i', 'o', 'n'),
            Trigram('n', 't', 'u'),
            Trigram('d', 'e', 'p'),
            Trigram('a', 'm', 'e'),
            Trigram('i', ' ', 'i'),
            Trigram('r', 'e', 'b'),
            Trigram('e', 'c', 't'),
            Trigram('a', 'l', 'i'),
            Trigram('l', ' ', 'c'),
            Trigram('e', 'm', 'e'),
            Trigram('n', 'd', 'e'),
            Trigram('n', ' ', 'a'),
            Trigram('i', 't', 'e'),
            Trigram('e', 'b', 'u'),
            Trigram('b', 'u', 'i'),
            Trigram('â', 't', ' '),
            Trigram('i', 'l', 'i'),
            Trigram('t', 'o', 'a'),
            Trigram('d', 'e', 'c'),
            Trigram(' ', 'o', ' '),
            Trigram('p', 'l', 'i'),
            Trigram('v', 'ă', 'ț'),
            Trigram('n', 't', ' '),
            Trigram('e', ' ', 'r'),
            Trigram('u', ' ', 'c'),
            Trigram('ț', 'a', ' '),
            Trigram('t', ' ', 'î'),
            Trigram('l', ' ', 'ș'),
            Trigram('c', 'u', ' '),
            Trigram('r', 't', 'a'),
            Trigram('c', 'i', 'a'),
            Trigram('a', 'n', 'e'),
            Trigram('ț', 'i', 'o'),
            Trigram('c', 'a', ' '),
            Trigram('i', 't', 'ă'),
            Trigram('p', 'o', 'a'),
            Trigram('c', 'ț', 'i'),
            Trigram('î', 'm', 'p'),
            Trigram('b', 'i', 'l'),
            Trigram('r', ' ', 'ș'),
            Trigram(' ', 's', 't'),
            Trigram('o', 'm', 'u'),
            Trigram('ă', 'ț', 'ă'),
            Trigram('ț', 'i', 'u'),
            Trigram('r', 'i', 'e'),
            Trigram('u', 'm', 'a'),
            Trigram('m', 'â', 'n'),
            Trigram(' ', 'm', 'a'),
            Trigram('a', 'n', 'i'),
            Trigram('n', 'ț', 'a'),
            Trigram('c', 'u', 'r'),
            Trigram('e', 'r', 'a'),
            Trigram('u', ' ', 'a'),
            Trigram('t', 'r', 'a'),
            Trigram('o', 'a', 'r'),
            Trigram(' ', 'e', 'x'),
            Trigram('t', ' ', 's'),
            Trigram('i', 'i', 'l'),
            Trigram('t', 'a', ' '),
            Trigram('r', 'i', 't'),
            Trigram('r', 'o', 't'),
            Trigram('m', 'o', 'd'),
            Trigram('t', 'r', 'i'),
            Trigram('r', 'i', 'v'),
            Trigram('o', 'd', ' '),
            Trigram('l', 'i', 'c'),
            Trigram('r', 'i', 'i'),
            Trigram('e', 'z', 'e'),
            Trigram('m', 'a', 'n'),
            Trigram('î', 'n', 'v'),
            Trigram('n', 'e', ' '),
            Trigram('n', 'v', 'ă'),
            Trigram('a', ' ', 'ș'),
            Trigram('c', 't', 'i'),
        ],
    ),
    (
        Lang::Hrv,
        &[
            Trigram(' ', 'p', 'r'),
            Trigram(' ', 'i', ' '),
            Trigram('j', 'e', ' '),
            Trigram('r', 'a', 'v'),
            Trigram('p', 'r', 'a'),
            Trigram('m', 'a', ' '),
            Trigram(' ', 'n', 'a'),
            Trigram('i', 'm', 'a'),
            Trigram(' ', 's', 'v'),
            Trigram('n', 'a', ' '),
            Trigram('t', 'i', ' '),
            Trigram('a', ' ', 'p'),
            Trigram('n', 'j', 'e'),
            Trigram(' ', 'p', 'o'),
            Trigram('a', ' ', 's'),
            Trigram('a', 'n', 'j'),
            Trigram('a', ' ', 'i'),
            Trigram('v', 'o', ' '),
            Trigram('k', 'o', ' '),
            Trigram('d', 'a', ' '),
            Trigram('v', 'a', 't'),
            Trigram('v', 'a', ' '),
            Trigram('n', 'o', ' '),
            Trigram(' ', 'z', 'a'),
            Trigram('i', ' ', 's'),
            Trigram('o', ' ', 'i'),
            Trigram('j', 'a', ' '),
            Trigram('a', 'v', 'o'),
            Trigram(' ', 'u', ' '),
            Trigram(' ', 'i', 'm'),
            Trigram('s', 'v', 'a'),
            Trigram('i', ' ', 'p'),
            Trigram(' ', 'b', 'i'),
            Trigram('e', ' ', 's'),
            Trigram('j', 'u', ' '),
            Trigram('t', 'k', 'o'),
            Trigram('o', ' ', 'n'),
            Trigram('l', 'i', ' '),
            Trigram('i', 'l', 'i'),
            Trigram('v', 'a', 'n'),
            Trigram('a', 'v', 'a'),
            Trigram(' ', 's', 'l'),
            Trigram('i', 'h', ' '),
            Trigram('n', 'e', ' '),
            Trigram('o', 's', 't'),
            Trigram(' ', 'd', 'r'),
            Trigram('i', 'j', 'e'),
            Trigram(' ', 'n', 'e'),
            Trigram('j', 'e', 'd'),
            Trigram('s', 'l', 'o'),
            Trigram(' ', 'r', 'a'),
            Trigram('u', ' ', 's'),
            Trigram('l', 'o', 'b'),
            Trigram('o', 'b', 'o'),
            Trigram(' ', 'o', 's'),
            Trigram('b', 'o', 'd'),
            Trigram(' ', 'd', 'a'),
            Trigram(' ', 'k', 'o'),
            Trigram('o', 'v', 'a'),
            Trigram('n', 'j', 'a'),
            Trigram('k', 'o', 'j'),
            Trigram('i', ' ', 'd'),
            Trigram('a', 't', 'k'),
            Trigram('i', 't', 'i'),
            Trigram(' ', 'i', 'l'),
            Trigram('s', 't', 'v'),
            Trigram('p', 'r', 'i'),
            Trigram('o', 'm', ' '),
            Trigram('i', 'm', ' '),
            Trigram(' ', 'j', 'e'),
            Trigram(' ', 'o', 'b'),
            Trigram(' ', 's', 'u'),
            Trigram(' ', 'k', 'a'),
            Trigram('i', ' ', 'i'),
            Trigram('i', ' ', 'n'),
            Trigram('e', ' ', 'i'),
            Trigram('v', 'j', 'e'),
            Trigram('i', ' ', 'u'),
            Trigram('s', 'e', ' '),
            Trigram('d', 'r', 'u'),
            Trigram('b', 'i', 't'),
            Trigram('v', 'o', 'j'),
            Trigram('a', 't', 'i'),
            Trigram('i', ' ', 'o'),
            Trigram('ć', 'e', 'n'),
            Trigram('a', ' ', 'o'),
            Trigram('o', ' ', 'p'),
            Trigram('a', ' ', 'b'),
            Trigram('a', ' ', 'n'),
            Trigram('u', 'ć', 'i'),
            Trigram(' ', 's', 'e'),
            Trigram('e', 'n', 'j'),
            Trigram('s', 't', 'i'),
            Trigram('a', ' ', 'u'),
            Trigram('e', 'd', 'n'),
            Trigram('d', 'j', 'e'),
            Trigram('l', 'o', ' '),
            Trigram('ć', 'a', 'v'),
            Trigram(' ', 'm', 'o'),
            Trigram('r', 'a', 'z'),
            Trigram('u', ' ', 'p'),
            Trigram(' ', 'o', 'd'),
            Trigram('r', 'a', 'n'),
            Trigram('n', 'i', ' '),
            Trigram('r', 'o', 'd'),
            Trigram('a', ' ', 'k'),
            Trigram('s', 'u', ' '),
            Trigram('a', 'r', 'o'),
            Trigram('d', 'r', 'ć'),
            Trigram('s', 'v', 'o'),
            Trigram('a', 'k', 'o'),
            Trigram('u', ' ', 'i'),
            Trigram('r', 'ć', 'a'),
            Trigram('a', ' ', 'j'),
            Trigram('m', 'i', 'j'),
            Trigram('j', 'i', ' '),
            Trigram('n', 'i', 'h'),
            Trigram('e', 'n', 'i'),
            Trigram('e', ' ', 'n'),
            Trigram('e', ' ', 'o'),
            Trigram(' ', 'n', 'j'),
            Trigram('p', 'r', 'e'),
            Trigram('p', 'o', 's'),
            Trigram('ć', 'i', 'v'),
            Trigram('o', 'j', 'e'),
            Trigram('e', 'n', 'o'),
            Trigram('e', ' ', 'p'),
            Trigram('n', 'a', 'r'),
            Trigram('o', 'd', 'a'),
            Trigram('n', 'i', 'm'),
            Trigram('o', 'v', 'o'),
            Trigram('a', 'j', 'u'),
            Trigram('r', 'a', ' '),
            Trigram('ć', 'i', ' '),
            Trigram('o', 'g', ' '),
            Trigram('n', 'o', 'v'),
            Trigram('i', 'v', 'a'),
            Trigram('a', ' ', 'd'),
            Trigram('n', 'o', 's'),
            Trigram('b', 'r', 'a'),
            Trigram('b', 'i', 'l'),
            Trigram('i', ' ', 'b'),
            Trigram('a', 'v', 'n'),
            Trigram('a', ' ', 'z'),
            Trigram('j', 'e', 'n'),
            Trigram('e', ' ', 'd'),
            Trigram('v', 'e', ' '),
            Trigram('o', 'r', 'a'),
            Trigram('t', 'v', 'a'),
            Trigram('j', 'e', 'l'),
            Trigram('s', 't', 'a'),
            Trigram('m', 'o', 'r'),
            Trigram('u', ' ', 'o'),
            Trigram('c', 'i', 'j'),
            Trigram('p', 'r', 'o'),
            Trigram('o', 'v', 'i'),
            Trigram('z', 'a', ' '),
            Trigram('j', 'e', 'r'),
            Trigram('k', 'a', ' '),
            Trigram('s', 'n', 'o'),
            Trigram('i', 'l', 'o'),
            Trigram('j', 'e', 'm'),
            Trigram('r', 'e', 'd'),
            Trigram('e', 'm', ' '),
            Trigram('l', 'j', 'u'),
            Trigram('o', 's', 'n'),
            Trigram('o', 'j', 'i'),
            Trigram(' ', 'i', 'z'),
            Trigram('a', 'c', 'i'),
            Trigram(' ', 'd', 'o'),
            Trigram('l', 'j', 'e'),
            Trigram('i', ' ', 'm'),
            Trigram(' ', 'n', 'i'),
            Trigram('o', 'd', 'n'),
            Trigram('n', 'o', 'm'),
            Trigram('j', 'e', 'g'),
            Trigram(' ', 'd', 'j'),
            Trigram('v', 'n', 'o'),
            Trigram('v', 'i', 'm'),
            Trigram('e', 'l', 'j'),
            Trigram('u', ' ', 'z'),
            Trigram('o', ' ', 'd'),
            Trigram('r', 'a', 'd'),
            Trigram('o', ' ', 'o'),
            Trigram('m', ' ', 'i'),
            Trigram('d', 'u', ' '),
            Trigram('u', 'j', 'e'),
            Trigram(' ', 's', 'a'),
            Trigram('n', 'i', 't'),
            Trigram('e', ' ', 'b'),
            Trigram(' ', 's', 't'),
            Trigram('o', 'j', ' '),
            Trigram('t', 'i', 't'),
            Trigram('a', ' ', 'ć'),
            Trigram('d', 'n', 'o'),
            Trigram('e', ' ', 'u'),
            Trigram('o', ' ', 's'),
            Trigram('u', ' ', 'd'),
            Trigram('e', 'ć', 'u'),
            Trigram('a', 'n', 'i'),
            Trigram('d', 'n', 'a'),
            Trigram('n', 'a', 'k'),
            Trigram('n', 's', 't'),
            Trigram('s', 't', 'u'),
            Trigram(' ', 's', 'm'),
            Trigram('e', ' ', 'k'),
            Trigram('u', ' ', 'u'),
            Trigram('a', 'n', ' '),
            Trigram('g', 'o', 'v'),
            Trigram('n', 'j', 'u'),
            Trigram('j', 'u', 'ć'),
            Trigram('a', 'l', 'n'),
            Trigram('m', ' ', 's'),
            Trigram('t', 'u', ' '),
            Trigram('a', ' ', 'r'),
            Trigram('ć', 'o', 'v'),
            Trigram('j', 'a', 'n'),
            Trigram('u', ' ', 'n'),
            Trigram('o', ' ', 'k'),
            Trigram('i', 's', 't'),
            Trigram('ć', 'u', ' '),
            Trigram('t', 'e', ' '),
            Trigram('t', 'v', 'o'),
            Trigram('a', 'n', 's'),
            Trigram('š', 't', 'i'),
            Trigram('n', 'u', ' '),
            Trigram('a', 'r', 'a'),
            Trigram('n', 'a', 'p'),
            Trigram('m', ' ', 'p'),
            Trigram('n', 'i', 'ć'),
            Trigram('o', 'l', 'j'),
            Trigram('b', 'u', 'd'),
            Trigram(' ', 'b', 'u'),
            Trigram('e', 'd', 'i'),
            Trigram('o', 'v', 'j'),
            Trigram('i', ' ', 'v'),
            Trigram('p', 'o', 'd'),
            Trigram('s', 'a', 'm'),
            Trigram('o', 'b', 'r'),
            Trigram('t', 'e', 'l'),
            Trigram(' ', 'm', 'i'),
            Trigram('i', 'n', 'a'),
            Trigram('z', 'a', 'š'),
            Trigram('e', ' ', 'm'),
            Trigram('a', 'š', 't'),
            Trigram(' ', 'v', 'j'),
            Trigram('o', 'n', 'a'),
            Trigram('n', 'j', 'i'),
            Trigram('j', 'e', 'k'),
            Trigram(' ', 't', 'a'),
            Trigram('d', 'u', 'ć'),
            Trigram('i', 'j', 'a'),
            Trigram(' ', 'ć', 'o'),
            Trigram('t', 'u', 'p'),
            Trigram('h', ' ', 'p'),
            Trigram('o', 'j', 'a'),
            Trigram('s', 'm', 'i'),
            Trigram('a', 'd', 'a'),
            Trigram(' ', 'o', 'p'),
            Trigram('o', 's', 'o'),
            Trigram('u', 'n', 'a'),
            Trigram('s', 'o', 'b'),
            Trigram('o', 'd', 'u'),
            Trigram('d', 'n', 'i'),
            Trigram('r', 'u', 'g'),
            Trigram('u', 'd', 'u'),
            Trigram('a', 'o', ' '),
            Trigram('d', 'i', ' '),
            Trigram('a', 'v', 'i'),
            Trigram('t', 'n', 'o'),
            Trigram('j', 'i', 'm'),
            Trigram('i', 't', 'u'),
            Trigram('i', 't', 'k'),
            Trigram('ć', 'e', ' '),
            Trigram('o', 'd', 'r'),
            Trigram('a', 'v', 'e'),
            Trigram('m', 'e', 'ć'),
            Trigram('n', 'o', 'g'),
            Trigram('d', 'i', 'n'),
            Trigram('s', 'v', 'i'),
            Trigram(' ', 'ć', 'i'),
            Trigram('k', 'a', 'k'),
            Trigram('k', 'l', 'a'),
            Trigram('r', 'i', 'm'),
            Trigram('a', 'k', 'v'),
            Trigram('e', 'l', 'o'),
            Trigram('š', 't', 'v'),
            Trigram('i', 't', 'e'),
            Trigram('v', 'o', 'l'),
            Trigram('j', 'e', 't'),
            Trigram('o', 'p', 'ć'),
            Trigram('p', 'o', 't'),
            Trigram('t', 'a', 'n'),
            Trigram('a', 'k', ' '),
            Trigram('n', 'i', 'c'),
            Trigram('n', 'a', 'c'),
            Trigram('u', 'ć', 'e'),
            Trigram(' ', 's', 'k'),
            Trigram(' ', 'm', 'e'),
            Trigram('v', 'e', 'n'),
        ],
    ),
    (
        Lang::Nld,
        &[
            Trigram('e', 'n', ' '),
            Trigram('d', 'e', ' '),
            Trigram('a', 'n', ' '),
            Trigram(' ', 'd', 'e'),
            Trigram('v', 'a', 'n'),
            Trigram(' ', 'v', 'a'),
            Trigram(' ', 'e', 'n'),
            Trigram(' ', 'h', 'e'),
            Trigram('i', 'n', 'g'),
            Trigram('c', 'h', 't'),
            Trigram('d', 'e', 'r'),
            Trigram('n', 'g', ' '),
            Trigram('n', ' ', 'd'),
            Trigram('n', ' ', 'v'),
            Trigram('e', 't', ' '),
            Trigram('e', 'e', 'n'),
            Trigram(' ', 'g', 'e'),
            Trigram('e', 'c', 'h'),
            Trigram('n', ' ', 'e'),
            Trigram('v', 'e', 'r'),
            Trigram('r', 'e', 'c'),
            Trigram('n', 'd', 'e'),
            Trigram(' ', 'e', 'e'),
            Trigram(' ', 'r', 'e'),
            Trigram(' ', 'b', 'e'),
            Trigram('e', 'd', 'e'),
            Trigram('e', 'r', ' '),
            Trigram('e', ' ', 'v'),
            Trigram('g', 'e', 'n'),
            Trigram('d', 'e', 'n'),
            Trigram('h', 'e', 't'),
            Trigram('t', 'e', 'n'),
            Trigram(' ', 't', 'e'),
            Trigram(' ', 'i', 'n'),
            Trigram(' ', 'o', 'p'),
            Trigram('n', ' ', 'i'),
            Trigram(' ', 'v', 'e'),
            Trigram('l', 'i', 'j'),
            Trigram(' ', 'z', 'i'),
            Trigram('e', 'r', 'e'),
            Trigram('e', 'l', 'i'),
            Trigram('z', 'i', 'j'),
            Trigram('i', 'j', 'k'),
            Trigram('t', 'e', ' '),
            Trigram('o', 'o', 'r'),
            Trigram('h', 't', ' '),
            Trigram('e', 'n', 's'),
            Trigram('n', ' ', 'o'),
            Trigram('a', 'n', 'd'),
            Trigram('t', ' ', 'o'),
            Trigram('i', 'j', 'n'),
            Trigram('i', 'e', 'd'),
            Trigram('k', 'e', ' '),
            Trigram(' ', 'o', 'n'),
            Trigram('e', 'i', 'd'),
            Trigram('o', 'p', ' '),
            Trigram(' ', 'v', 'o'),
            Trigram('j', 'n', ' '),
            Trigram('i', 'd', ' '),
            Trigram('o', 'n', 'd'),
            Trigram('i', 'n', ' '),
            Trigram('s', 'c', 'h'),
            Trigram(' ', 'v', 'r'),
            Trigram('a', 'a', 'r'),
            Trigram('n', ' ', 'z'),
            Trigram('a', 'a', 'n'),
            Trigram(' ', 'i', 'e'),
            Trigram('r', 'd', 'e'),
            Trigram('r', 'i', 'j'),
            Trigram('m', 'e', 'n'),
            Trigram('r', 'e', 'n'),
            Trigram('o', 'r', 'd'),
            Trigram('h', 'e', 'i'),
            Trigram('h', 't', 'e'),
            Trigram(' ', 'w', 'e'),
            Trigram('e', 'f', 't'),
            Trigram('n', ' ', 'g'),
            Trigram('f', 't', ' '),
            Trigram('n', ' ', 'w'),
            Trigram('o', 'r', ' '),
            Trigram('n', ' ', 'h'),
            Trigram('e', 'e', 'f'),
            Trigram('v', 'r', 'i'),
            Trigram('w', 'o', 'r'),
            Trigram(' ', 'm', 'e'),
            Trigram('h', 'e', 'e'),
            Trigram('a', 'l', ' '),
            Trigram('t', ' ', 'r'),
            Trigram('o', 'f', ' '),
            Trigram('l', 'e', ' '),
            Trigram(' ', 'o', 'f'),
            Trigram('a', 't', 'i'),
            Trigram('g', ' ', 'v'),
            Trigram('e', ' ', 'b'),
            Trigram('e', 'n', 'i'),
            Trigram(' ', 'a', 'a'),
            Trigram('l', 'l', 'e'),
            Trigram(' ', 'w', 'o'),
            Trigram('n', ' ', 'a'),
            Trigram('e', ' ', 'o'),
            Trigram('n', 'd', ' '),
            Trigram('r', ' ', 'h'),
            Trigram('v', 'o', 'o'),
            Trigram(' ', 'a', 'l'),
            Trigram('e', 'g', 'e'),
            Trigram('n', ' ', 't'),
            Trigram('e', 'r', 'k'),
            Trigram(' ', 'd', 'a'),
            Trigram(' ', 'n', 'a'),
            Trigram('t', ' ', 'h'),
            Trigram('s', 't', 'a'),
            Trigram('j', 'k', 'e'),
            Trigram('a', 't', ' '),
            Trigram('n', 'a', 't'),
            Trigram('n', 'g', 'e'),
            Trigram('e', ' ', 'e'),
            Trigram('e', 'n', 'd'),
            Trigram(' ', 's', 't'),
            Trigram('o', 'm', ' '),
            Trigram('e', ' ', 'g'),
            Trigram('t', 'i', 'e'),
            Trigram('n', ' ', 'b'),
            Trigram('s', 't', 'e'),
            Trigram('d', 'i', 'e'),
            Trigram('e', ' ', 'r'),
            Trigram('e', 'r', 'w'),
            Trigram('w', 'e', 'l'),
            Trigram('e', ' ', 's'),
            Trigram('r', ' ', 'd'),
            Trigram(' ', 'o', 'm'),
            Trigram('i', 'j', ' '),
            Trigram('d', 'i', 'g'),
            Trigram('t', ' ', 'e'),
            Trigram('i', 'g', 'e'),
            Trigram('t', 'e', 'r'),
            Trigram('i', 'e', ' '),
            Trigram('g', 'e', 'l'),
            Trigram('r', 'e', ' '),
            Trigram('j', 'h', 'e'),
            Trigram('t', ' ', 'd'),
            Trigram(' ', 'z', 'a'),
            Trigram('e', ' ', 'm'),
            Trigram('e', 'r', 's'),
            Trigram('i', 'j', 'h'),
            Trigram('n', 'i', 'g'),
            Trigram('z', 'a', 'l'),
            Trigram('n', 'i', 'e'),
            Trigram('d', ' ', 'v'),
            Trigram('n', 's', ' '),
            Trigram('d', ' ', 'e'),
            Trigram('e', ' ', 'w'),
            Trigram('e', ' ', 'n'),
            Trigram('e', 's', 't'),
            Trigram('e', 'l', 'e'),
            Trigram('b', 'e', 's'),
            Trigram(' ', 'd', 'o'),
            Trigram('g', ' ', 'e'),
            Trigram('c', 'h', 'e'),
            Trigram('v', 'o', 'l'),
            Trigram('g', 'e', ' '),
            Trigram('e', 'z', 'e'),
            Trigram('e', ' ', 'd'),
            Trigram('i', 'g', ' '),
            Trigram('g', 'i', 'n'),
            Trigram('d', 'a', 't'),
            Trigram('h', 'a', 'p'),
            Trigram('c', 'h', 'a'),
            Trigram('e', 'k', 'e'),
            Trigram(' ', 'd', 'i'),
            Trigram('o', 'n', 'a'),
            Trigram('e', ' ', 'a'),
            Trigram('l', 'k', 'e'),
            Trigram('n', 's', 't'),
            Trigram('a', 'r', 'd'),
            Trigram(' ', 'g', 'r'),
            Trigram('t', 'e', 'l'),
            Trigram('m', 'i', 'n'),
            Trigram(' ', 't', 'o'),
            Trigram('w', 'a', 'a'),
            Trigram('l', 'e', 'n'),
            Trigram('e', 'l', 'k'),
            Trigram('l', 'i', 'n'),
            Trigram('e', 'm', 'e'),
            Trigram('j', 'k', ' '),
            Trigram('n', ' ', 's'),
            Trigram('d', 'e', 'l'),
            Trigram('s', 't', 'r'),
            Trigram('h', 'a', 'n'),
            Trigram('e', 'v', 'e'),
            Trigram('g', 'r', 'o'),
            Trigram('i', 'c', 'h'),
            Trigram('v', 'e', 'n'),
            Trigram('d', 'o', 'o'),
            Trigram(' ', 'w', 'a'),
            Trigram('t', ' ', 'v'),
            Trigram('i', 't', ' '),
            Trigram('o', 'v', 'e'),
            Trigram('r', 'i', 'n'),
            Trigram('a', 'a', 't'),
            Trigram('n', ' ', 'n'),
            Trigram('w', 'e', 't'),
            Trigram('u', 'i', 't'),
            Trigram('i', 'j', 'd'),
            Trigram('z', 'e', ' '),
            Trigram(' ', 'z', 'o'),
            Trigram('i', 'o', 'n'),
            Trigram(' ', 'o', 'v'),
            Trigram('d', 'e', 'z'),
            Trigram('g', 'e', 'm'),
            Trigram('m', 'e', 't'),
            Trigram('t', 'i', 'o'),
            Trigram('b', 'b', 'e'),
            Trigram('a', 'c', 'h'),
            Trigram(' ', 'n', 'i'),
            Trigram('h', 'e', 'd'),
            Trigram('s', 't', ' '),
            Trigram('a', 'l', 'l'),
            Trigram('i', 'e', 's'),
            Trigram('p', 'e', 'r'),
            Trigram('h', 'e', 'b'),
            Trigram('e', 'b', 'b'),
            Trigram('e', ' ', 'i'),
            Trigram('t', 'o', 'e'),
            Trigram('e', 's', ' '),
            Trigram('t', 'a', 'a'),
            Trigram('n', ' ', 'm'),
            Trigram('n', 't', 'e'),
            Trigram('i', 'e', 'n'),
            Trigram('e', 'l', ' '),
            Trigram('n', 'i', 'n'),
            Trigram('a', 'l', 'e'),
            Trigram('b', 'e', 'n'),
            Trigram('d', 'a', 'a'),
            Trigram('s', 't', 'i'),
            Trigram(' ', 'm', 'a'),
            Trigram('m', 'e', 'e'),
            Trigram('k', 'i', 'n'),
            Trigram('p', 'e', 'n'),
            Trigram('e', ' ', 'h'),
            Trigram('w', 'e', 'r'),
            Trigram('o', 'n', 't'),
            Trigram('i', 'e', 't'),
            Trigram('t', 'i', 'g'),
            Trigram('g', ' ', 'o'),
            Trigram('s', ' ', 'e'),
            Trigram(' ', 'e', 'r'),
            Trigram('i', 'g', 'd'),
            Trigram('e', 't', 'e'),
            Trigram('a', 'n', 'g'),
            Trigram('l', 'a', 'n'),
            Trigram('n', 's', 'c'),
            Trigram('e', 'm', 'a'),
            Trigram('m', 'a', 'n'),
            Trigram('t', ' ', 'g'),
            Trigram('i', 's', ' '),
            Trigram('b', 'e', 'g'),
            Trigram('h', 'e', 'r'),
            Trigram('e', 's', 'c'),
            Trigram('b', 'i', 'j'),
            Trigram('d', ' ', 'o'),
            Trigram('r', 'o', 'n'),
            Trigram('t', 'i', 'n'),
            Trigram('n', 'a', 'l'),
            Trigram('e', 'e', 'r'),
            Trigram('p', ' ', 'v'),
            Trigram('e', 'd', 'i'),
            Trigram('e', 'r', 'm'),
            Trigram('i', 't', 'e'),
            Trigram('t', ' ', 'w'),
            Trigram('t', ' ', 'a'),
            Trigram(' ', 'h', 'u'),
            Trigram('r', 'w', 'i'),
            Trigram('w', 'i', 'j'),
            Trigram('i', 'j', 's'),
            Trigram('r', ' ', 'e'),
            Trigram('w', 'e', 'g'),
            Trigram('j', 's', ' '),
            Trigram('r', 'm', 'i'),
            Trigram('n', 'a', 'a'),
            Trigram('t', ' ', 'b'),
            Trigram('a', 'p', 'p'),
            Trigram('r', 'w', 'e'),
            Trigram(' ', 'b', 'i'),
            Trigram('t', ' ', 'z'),
            Trigram('k', 'e', 'r'),
            Trigram('a', 'm', 'e'),
            Trigram('e', 'r', 'i'),
            Trigram('k', 'e', 'n'),
            Trigram(' ', 'a', 'n'),
            Trigram('a', 'r', ' '),
            Trigram(' ', 'l', 'a'),
            Trigram('t', 'r', 'e'),
            Trigram('g', 'e', 'r'),
            Trigram('r', 'd', 'i'),
            Trigram('t', 'a', 'n'),
            Trigram('e', 'i', 't'),
            Trigram('g', 'd', 'e'),
            Trigram('g', ' ', 'i'),
            Trigram('d', ' ', 'z'),
            Trigram('o', 'e', 'p'),
        ],
    ),
    (
        Lang::Uzb,
        &[
            Trigram('l', 'a', 'r'),
            Trigram('i', 's', 'h'),
            Trigram('a', 'n', ' '),
            Trigram('g', 'a', ' '),
            Trigram('a', 'r', ' '),
            Trigram(' ', 'v', 'a'),
            Trigram(' ', 'b', 'i'),
            Trigram('d', 'a', ' '),
            Trigram('v', 'a', ' '),
            Trigram('i', 'r', ' '),
            Trigram(' ', 'h', 'u'),
            Trigram('i', 'g', 'a'),
            Trigram('s', 'h', ' '),
            Trigram('u', 'q', 'u'),
            Trigram('s', 'h', 'i'),
            Trigram('b', 'i', 'r'),
            Trigram('q', 'u', 'q'),
            Trigram('h', 'u', 'q'),
            Trigram('g', 'a', 'n'),
            Trigram(' ', 'b', 'o'),
            Trigram(' ', 'h', 'a'),
            Trigram('i', 'n', 'i'),
            Trigram('n', 'g', ' '),
            Trigram('a', ' ', 'e'),
            Trigram('r', ' ', 'b'),
            Trigram(' ', 't', 'a'),
            Trigram('l', 'i', 's'),
            Trigram('n', 'i', ' '),
            Trigram('i', 'n', 'g'),
            Trigram('l', 'i', 'k'),
            Trigram('i', 'd', 'a'),
            Trigram('o', 'ʻ', 'l'),
            Trigram('i', 'l', 'i'),
            Trigram('a', 'r', 'i'),
            Trigram('n', 'i', 'n'),
            Trigram('o', 'n', ' '),
            Trigram('i', 'n', 's'),
            Trigram(' ', 'i', 'n'),
            Trigram('a', 'd', 'i'),
            Trigram('n', 's', 'o'),
            Trigram('s', 'o', 'n'),
            Trigram('i', 'y', ' '),
            Trigram(' ', 'o', 'ʻ'),
            Trigram('l', 'a', 'n'),
            Trigram(' ', 'm', 'a'),
            Trigram('d', 'i', 'r'),
            Trigram('h', 'i', ' '),
            Trigram('k', 'i', 'n'),
            Trigram('h', 'a', 'r'),
            Trigram('i', ' ', 'b'),
            Trigram('a', 's', 'h'),
            Trigram(' ', 'y', 'o'),
            Trigram('b', 'o', 'ʻ'),
            Trigram(' ', 'm', 'u'),
            Trigram('d', 'a', 'n'),
            Trigram('u', 'q', 'i'),
            Trigram('i', 'l', 'a'),
            Trigram('e', 'g', 'a'),
            Trigram('q', 'l', 'a'),
            Trigram('r', ' ', 'i'),
            Trigram('q', 'i', 'g'),
            Trigram('o', 'ʻ', 'z'),
            Trigram(' ', 'e', 'g'),
            Trigram('k', 'l', 'a'),
            Trigram('a', ' ', 'b'),
            Trigram('q', 'i', 'l'),
            Trigram('e', 'r', 'k'),
            Trigram('k', 'i', ' '),
            Trigram(' ', 'e', 'r'),
            Trigram('o', 'l', 'i'),
            Trigram('n', 'l', 'i'),
            Trigram('a', 't', ' '),
            Trigram(' ', 'o', 'l'),
            Trigram('g', 'a', 'd'),
            Trigram('l', 'g', 'a'),
            Trigram('r', 'k', 'i'),
            Trigram('o', 'k', 'i'),
            Trigram('i', ' ', 'h'),
            Trigram('a', ' ', 'o'),
            Trigram(' ', 'q', 'a'),
            Trigram('y', 'o', 'k'),
            Trigram('l', 'i', 'g'),
            Trigram('o', 's', 'h'),
            Trigram('i', 'g', 'i'),
            Trigram('i', 'b', ' '),
            Trigram('l', 'a', 's'),
            Trigram('n', ' ', 'b'),
            Trigram('a', 't', 'l'),
            Trigram('n', ' ', 'm'),
            Trigram(' ', 'b', 'a'),
            Trigram('a', 'r', 'a'),
            Trigram(' ', 'q', 'i'),
            Trigram('r', 'i', ' '),
            Trigram(' ', 's', 'h'),
            Trigram('i', 'y', 'a'),
            Trigram('a', 'l', 'a'),
            Trigram('l', 'a', 't'),
            Trigram('i', 'n', ' '),
            Trigram('h', 'a', 'm'),
            Trigram('b', 'i', 'l'),
            Trigram('a', ' ', 't'),
            Trigram('a', ' ', 'y'),
            Trigram('b', 'o', 's'),
            Trigram('r', ' ', 'h'),
            Trigram('s', 'i', 'y'),
            Trigram('n', ' ', 'o'),
            Trigram('y', 'a', 't'),
            Trigram('i', 'n', 'l'),
            Trigram('i', 'k', ' '),
            Trigram('a', ' ', 'q'),
            Trigram('c', 'h', 'a'),
            Trigram('a', ' ', 'h'),
            Trigram(' ', 'e', 't'),
            Trigram('e', 't', 'i'),
            Trigram('n', 'i', 's'),
            Trigram('a', ' ', 's'),
            Trigram('t', 'i', 'l'),
            Trigram('a', 'n', 'i'),
            Trigram('h', ' ', 'h'),
            Trigram('i', ' ', 'v'),
            Trigram('m', 'a', 's'),
            Trigram('t', 'l', 'a'),
            Trigram('o', 's', 'i'),
            Trigram('a', 's', 'i'),
            Trigram(' ', 'q', 'o'),
            Trigram('ʻ', 'l', 'i'),
            Trigram('a', 't', 'i'),
            Trigram('i', ' ', 'm'),
            Trigram('r', 'n', 'i'),
            Trigram('i', 'm', ' '),
            Trigram('u', 'q', 'l'),
            Trigram('a', 'r', 'n'),
            Trigram('r', 'i', 's'),
            Trigram('q', 'a', 'r'),
            Trigram('a', ' ', 'i'),
            Trigram('g', 'i', ' '),
            Trigram(' ', 'd', 'a'),
            Trigram('n', ' ', 'h'),
            Trigram('h', 'a', ' '),
            Trigram('s', 'h', 'a'),
            Trigram('i', ' ', 't'),
            Trigram('m', 'l', 'a'),
            Trigram('r', 'c', 'h'),
            Trigram(' ', 'x', 'a'),
            Trigram('i', ' ', 'o'),
            Trigram('l', 'i', ' '),
            Trigram('h', 'u', 'n'),
            Trigram('b', 'a', 'r'),
            Trigram('l', 'i', 'n'),
            Trigram('ʻ', 'z', ' '),
            Trigram('a', 'r', 'c'),
            Trigram('r', 'l', 'a'),
            Trigram(' ', 'b', 'u'),
            Trigram('a', ' ', 'm'),
            Trigram('a', ' ', 'a'),
            Trigram(' ', 'a', 's'),
            Trigram('m', 'u', 'm'),
            Trigram(' ', 'b', 'e'),
            Trigram(' ', 't', 'u'),
            Trigram('a', 'r', 'o'),
            Trigram('r', ' ', 'v'),
            Trigram('i', 'k', 'l'),
            Trigram('l', 'i', 'b'),
            Trigram('t', 'a', 'ʼ'),
            Trigram('h', ' ', 'v'),
            Trigram('t', 'g', 'a'),
            Trigram('t', 'i', 'b'),
            Trigram('u', 'n', ' '),
            Trigram('l', 'l', 'a'),
            Trigram('m', 'd', 'a'),
            Trigram(' ', 'k', 'e'),
            Trigram('s', 'h', 'g'),
            Trigram(' ', 't', 'o'),
            Trigram('n', ' ', 'q'),
            Trigram('s', 'i', 'd'),
            Trigram('n', ' ', 'e'),
            Trigram('m', 'a', 't'),
            Trigram('a', 'm', 'd'),
            Trigram('s', 'h', 'u'),
            Trigram('h', 'g', 'a'),
            Trigram(' ', 't', 'e'),
            Trigram('t', 'a', 's'),
            Trigram('a', 'l', 'i'),
            Trigram('u', 'm', 'k'),
            Trigram('o', 'y', 'a'),
            Trigram('h', 'l', 'a'),
            Trigram('o', 'l', 'a'),
            Trigram('a', 'm', 'l'),
            Trigram('i', 'r', 'o'),
            Trigram('i', 'l', 'l'),
            Trigram('t', 'i', 's'),
            Trigram('i', 'r', 'i'),
            Trigram('r', 'g', 'a'),
            Trigram('m', 'k', 'i'),
            Trigram('i', 'r', 'l'),
            Trigram(' ', 'y', 'a'),
            Trigram('x', 'a', 'l'),
            Trigram('d', 'a', 'm'),
            Trigram(' ', 'd', 'e'),
            Trigram('g', 'i', 'n'),
            Trigram('e', 'n', 'g'),
            Trigram('r', 'd', 'a'),
            Trigram('t', 'a', 'r'),
            Trigram('u', 's', 'h'),
            Trigram('r', 'a', 'k'),
            Trigram('a', 'y', 'o'),
            Trigram(' ', 'e', 'ʼ'),
            Trigram(' ', 's', 'o'),
            Trigram('t', 'e', 'n'),
            Trigram('a', 'l', 'q'),
            Trigram(' ', 's', 'a'),
            Trigram('u', 'r', ' '),
            Trigram(' ', 'i', 's'),
            Trigram('i', 'm', 'o'),
            Trigram('r', ' ', 't'),
            Trigram(' ', 'k', 'i'),
            Trigram('m', 'i', 'l'),
            Trigram(' ', 'm', 'i'),
            Trigram('e', 'r', 'a'),
            Trigram('z', 'a', 'r'),
            Trigram('h', 'q', 'a'),
            Trigram('a', 'z', 'a'),
            Trigram('k', ' ', 'b'),
            Trigram(' ', 's', 'i'),
            Trigram('n', 'd', 'a'),
            Trigram('h', 'd', 'a'),
            Trigram('k', 'a', 't'),
            Trigram('a', 'k', ' '),
            Trigram('o', 'ʻ', 'r'),
            Trigram('n', ' ', 'v'),
            Trigram('a', ' ', 'k'),
            Trigram('o', 'r', ' '),
            Trigram('r', 'a', 't'),
            Trigram('a', 'd', 'a'),
            Trigram('ʻ', 'l', 'g'),
            Trigram('m', 'i', 'y'),
            Trigram('t', 'n', 'i'),
            Trigram('i', ' ', 'q'),
            Trigram('s', 'h', 'q'),
            Trigram('o', 'd', 'a'),
            Trigram('s', 'h', 'l'),
            Trigram('b', 'u', ' '),
            Trigram('d', 'a', 'v'),
            Trigram('n', 'i', 'd'),
            Trigram('y', ' ', 't'),
            Trigram('c', 'h', ' '),
            Trigram('a', 's', 'l'),
            Trigram('s', 'o', 's'),
            Trigram('i', 'l', 'g'),
            Trigram('a', 's', 'o'),
            Trigram('n', ' ', 't'),
            Trigram('a', 't', 'n'),
            Trigram('s', 'i', 'n'),
            Trigram('a', 'm', ' '),
            Trigram('t', 'i', ' '),
            Trigram('a', 's', ' '),
            Trigram('a', 'n', 'a'),
            Trigram('r', 'i', 'n'),
            Trigram('s', 'i', 'z'),
            Trigram('y', 'o', 't'),
            Trigram('l', 'i', 'm'),
            Trigram('u', 'n', 'i'),
            Trigram('n', 'g', 'a'),
            Trigram('l', 'a', 'k'),
            Trigram('n', ' ', 'i'),
            Trigram('a', ' ', 'u'),
            Trigram('q', 'o', 'n'),
            Trigram('i', ' ', 'a'),
            Trigram('h', ' ', 'k'),
            Trigram('v', 'l', 'a'),
            Trigram('a', 'v', 'l'),
            Trigram('a', 'm', 'i'),
            Trigram('d', 'e', 'k'),
            Trigram(' ', 'j', 'a'),
            Trigram('e', 'm', 'a'),
            Trigram('a', ' ', 'd'),
            Trigram('n', 'a', ' '),
            Trigram(' ', 'e', 'm'),
            Trigram('e', 'k', 'l'),
            Trigram('g', 'ʻ', 'i'),
            Trigram('s', 'i', ' '),
            Trigram('i', ' ', 'e'),
            Trigram('i', 'n', 'o'),
            Trigram(' ', 'k', 'a'),
            Trigram('u', 'c', 'h'),
            Trigram('b', 'o', 'r'),
            Trigram('k', 'e', 'r'),
            Trigram(' ', 'c', 'h'),
            Trigram('l', 'm', 'a'),
            Trigram('l', 'i', 'y'),
            Trigram('a', ' ', 'v'),
            Trigram('ʼ', 't', 'i'),
            Trigram('l', 'l', 'i'),
            Trigram('a', 'k', 'a'),
            Trigram('m', 'u', 'h'),
            Trigram('r', 'i', 'g'),
            Trigram('e', 'c', 'h'),
            Trigram('i', ' ', 'y'),
            Trigram('u', 'r', 'i'),
            Trigram('r', 'o', 'r'),
        ],
    ),
    (
        Lang::Tgl,
        &[
            Trigram('n', 'g', ' '),
            Trigram('a', 'n', 'g'),
            Trigram(' ', 'p', 'a'),
            Trigram('a', 'n', ' '),
            Trigram('s', 'a', ' '),
            Trigram(' ', 's', 'a'),
            Trigram('a', 't', ' '),
            Trigram(' ', 'k', 'a'),
            Trigram(' ', 'n', 'g'),
            Trigram(' ', 'm', 'a'),
            Trigram('a', 'l', 'a'),
            Trigram('g', ' ', 'p'),
            Trigram('a', 'p', 'a'),
            Trigram(' ', 'n', 'a'),
            Trigram('a', 't', 'a'),
            Trigram('p', 'a', 'g'),
            Trigram('p', 'a', 'n'),
            Trigram(' ', 'a', 'n'),
            Trigram(' ', 'a', 't'),
            Trigram('a', 'y', ' '),
            Trigram('a', 'r', 'a'),
            Trigram('g', 'a', ' '),
            Trigram('a', ' ', 'p'),
            Trigram('t', 'a', 'n'),
            Trigram('g', ' ', 'm'),
            Trigram('m', 'g', 'a'),
            Trigram(' ', 'm', 'g'),
            Trigram('n', ' ', 'n'),
            Trigram('p', 'a', 't'),
            Trigram(' ', 'b', 'a'),
            Trigram('n', ' ', 'a'),
            Trigram('a', 'y', 'a'),
            Trigram('n', 'a', ' '),
            Trigram('a', 'm', 'a'),
            Trigram('g', ' ', 'k'),
            Trigram('a', 'w', 'a'),
            Trigram('k', 'a', 'r'),
            Trigram('a', ' ', 'k'),
            Trigram('l', 'a', 'n'),
            Trigram('r', 'a', 'p'),
            Trigram('g', 'k', 'a'),
            Trigram('n', 'g', 'a'),
            Trigram('n', ' ', 's'),
            Trigram('g', ' ', 'n'),
            Trigram('a', 'h', 'a'),
            Trigram('g', ' ', 'b'),
            Trigram('a', ' ', 'a'),
            Trigram(' ', 't', 'a'),
            Trigram('a', 'g', 'k'),
            Trigram('g', 'a', 'n'),
            Trigram('t', 'a', 'o'),
            Trigram('a', 's', 'a'),
            Trigram('a', 'k', 'a'),
            Trigram('y', 'a', 'n'),
            Trigram('a', 'o', ' '),
            Trigram('a', ' ', 'm'),
            Trigram('m', 'a', 'y'),
            Trigram('m', 'a', 'n'),
            Trigram('k', 'a', 'l'),
            Trigram('i', 'n', 'g'),
            Trigram('a', ' ', 's'),
            Trigram('n', 'a', 'n'),
            Trigram('a', 'g', 'a'),
            Trigram(' ', 'l', 'a'),
            Trigram('b', 'a', 'n'),
            Trigram('a', 'l', 'i'),
            Trigram('g', ' ', 'a'),
            Trigram('a', 'n', 'a'),
            Trigram('y', ' ', 'm'),
            Trigram('k', 'a', 't'),
            Trigram('s', 'a', 'n'),
            Trigram('k', 'a', 'n'),
            Trigram('g', ' ', 'i'),
            Trigram('o', 'n', 'g'),
            Trigram('p', 'a', 'm'),
            Trigram('m', 'a', 'g'),
            Trigram('a', ' ', 'n'),
            Trigram('o', ' ', 'a'),
            Trigram('b', 'a', 'w'),
            Trigram('i', 's', 'a'),
            Trigram('w', 'a', 't'),
            Trigram(' ', 'y', ' '),
            Trigram('l', 'a', 'y'),
            Trigram('g', ' ', 's'),
            Trigram('y', ' ', 'k'),
            Trigram('i', 'n', ' '),
            Trigram('i', 'l', 'a'),
            Trigram('t', ' ', 't'),
            Trigram(' ', 'a', 'y'),
            Trigram('a', 'a', 'n'),
            Trigram('o', ' ', 'y'),
            Trigram('k', 'a', 's'),
            Trigram('i', 'n', 'a'),
            Trigram('t', ' ', 'n'),
            Trigram('a', 'g', ' '),
            Trigram('t', ' ', 'p'),
            Trigram('w', 'a', 'l'),
            Trigram('u', 'n', 'a'),
            Trigram('y', 'o', 'n'),
            Trigram(' ', 'o', ' '),
            Trigram(' ', 'i', 't'),
            Trigram('n', 'a', 'g'),
            Trigram('l', 'a', 'l'),
            Trigram('t', 'a', 'y'),
            Trigram('p', 'i', 'n'),
            Trigram('i', 'l', 'i'),
            Trigram('a', 'n', 's'),
            Trigram('i', 't', 'o'),
            Trigram('n', 's', 'a'),
            Trigram('l', 'a', 'h'),
            Trigram('k', 'a', 'k'),
            Trigram('a', 'n', 'y'),
            Trigram('a', ' ', 'i'),
            Trigram('n', 't', 'a'),
            Trigram('n', 'y', 'a'),
            Trigram('t', 'o', ' '),
            Trigram('h', 'a', 'y'),
            Trigram('g', 'a', 'l'),
            Trigram('m', 'a', 'm'),
            Trigram('a', 'b', 'a'),
            Trigram('r', 'a', 'n'),
            Trigram('a', 'n', 't'),
            Trigram('a', 'g', 't'),
            Trigram('o', 'n', ' '),
            Trigram('t', ' ', 's'),
            Trigram('a', 'g', 'p'),
            Trigram(' ', 'w', 'a'),
            Trigram(' ', 'g', 'a'),
            Trigram('g', 'a', 'w'),
            Trigram('h', 'a', 'n'),
            Trigram('k', 'a', 'p'),
            Trigram('o', ' ', 'm'),
            Trigram('l', 'i', 'p'),
            Trigram('y', 'a', ' '),
            Trigram('a', 's', ' '),
            Trigram('g', ' ', 't'),
            Trigram('h', 'a', 't'),
            Trigram('y', ' ', 'n'),
            Trigram('n', 'g', 'k'),
            Trigram('u', 'n', 'g'),
            Trigram('n', 'o', ' '),
            Trigram('g', ' ', 'l'),
            Trigram('g', 'p', 'a'),
            Trigram('w', 'a', ' '),
            Trigram('l', 'a', 'g'),
            Trigram('g', 't', 'a'),
            Trigram('t', ' ', 'm'),
            Trigram('k', 'a', 'i'),
            Trigram('y', 'a', 'a'),
            Trigram('s', 'a', 'l'),
            Trigram('a', 'r', 'i'),
            Trigram('l', 'i', 'n'),
            Trigram('a', ' ', 'l'),
            Trigram('p', 'a', 'p'),
            Trigram('a', 'h', 'i'),
            Trigram(' ', 'i', 's'),
            Trigram(' ', 'd', 'i'),
            Trigram('i', 't', 'a'),
            Trigram(' ', 'p', 'i'),
            Trigram('p', 'u', 'n'),
            Trigram('a', 'g', 'i'),
            Trigram('i', 'p', 'i'),
            Trigram('m', 'a', 'k'),
            Trigram('a', ' ', 'b'),
            Trigram('y', ' ', 's'),
            Trigram('b', 'a', 't'),
            Trigram('y', 'a', 'g'),
            Trigram('a', 'g', 's'),
            Trigram('o', ' ', 'n'),
            Trigram('a', 'k', 'i'),
            Trigram('t', 'a', 't'),
            Trigram('p', 'a', 'h'),
            Trigram('l', 'a', ' '),
            Trigram('g', 'a', 'y'),
            Trigram('h', 'i', 'n'),
            Trigram(' ', 's', 'i'),
            Trigram('d', 'i', ' '),
            Trigram('i', ' ', 'n'),
            Trigram('s', 'a', 's'),
            Trigram('i', 't', 'i'),
            Trigram('a', ' ', 't'),
            Trigram('t', ' ', 'k'),
            Trigram('m', 'a', 'l'),
            Trigram('a', 'i', 's'),
            Trigram('s', ' ', 'n'),
            Trigram('t', ' ', 'a'),
            Trigram('a', 'l', ' '),
            Trigram('i', 'p', 'u'),
            Trigram('i', 'k', 'a'),
            Trigram('l', 'i', 't'),
            Trigram('g', 'i', 'n'),
            Trigram(' ', 'i', 'p'),
            Trigram('a', 'n', 'o'),
            Trigram('g', 's', 'a'),
            Trigram('a', 'l', 'o'),
            Trigram('n', 'i', 'n'),
            Trigram('u', 'm', 'a'),
            Trigram('h', 'a', 'l'),
            Trigram('i', 'r', 'a'),
            Trigram('a', 'p', ' '),
            Trigram('a', 'n', 'i'),
            Trigram('o', 'd', ' '),
            Trigram('i', ' ', 'a'),
            Trigram('g', 'g', 'a'),
            Trigram('y', ' ', 'p'),
            Trigram('p', 'a', 'r'),
            Trigram('t', 'a', 's'),
            Trigram('i', 'g', ' '),
            Trigram('s', 'a', 'p'),
            Trigram('i', 'h', 'i'),
            Trigram('n', 'a', 'h'),
            Trigram('i', 'n', 'i'),
            Trigram(' ', 'b', 'u'),
            Trigram('n', 'g', 'i'),
            Trigram('s', 'y', 'o'),
            Trigram('o', ' ', 's'),
            Trigram('n', 'a', 'p'),
            Trigram('o', ' ', 'p'),
            Trigram('a', ' ', 'g'),
            Trigram(' ', 'h', 'a'),
            Trigram('u', 'k', 'a'),
            Trigram('a', ' ', 'h'),
            Trigram('a', 'r', 'u'),
            Trigram('a', ' ', 'o'),
            Trigram('m', 'a', 'h'),
            Trigram('i', 'b', 'a'),
            Trigram('a', 's', 'y'),
            Trigram('l', 'i', ' '),
            Trigram('u', 's', 'a'),
            Trigram('g', ' ', 'e'),
            Trigram('u', 'h', 'a'),
            Trigram('i', 'p', 'a'),
            Trigram('m', 'b', 'a'),
            Trigram('l', 'a', 'm'),
            Trigram('k', 'i', 'n'),
            Trigram('k', 'i', 'l'),
            Trigram('d', 'u', 'k'),
            Trigram('n', ' ', 'o'),
            Trigram('i', 'g', 'a'),
            Trigram(' ', 'd', 'a'),
            Trigram('d', 'a', 'i'),
            Trigram('a', 'i', 'g'),
            Trigram('i', 'g', 'd'),
            Trigram('g', 'd', 'i'),
            Trigram('p', 'i', 'l'),
            Trigram('d', 'i', 'g'),
            Trigram('p', 'a', 'k'),
            Trigram(' ', 't', 'u'),
            Trigram('d', ' ', 'n'),
            Trigram('s', 'a', 'm'),
            Trigram('n', 'a', 's'),
            Trigram('n', 'a', 'k'),
            Trigram('b', 'a', ' '),
            Trigram('a', 'd', ' '),
            Trigram('l', 'i', 'm'),
            Trigram('s', 'i', 'n'),
            Trigram('b', 'u', 'h'),
            Trigram('r', 'i', ' '),
            Trigram('l', 'a', 'b'),
            Trigram('i', 't', ' '),
            Trigram('t', 'a', 'g'),
            Trigram('g', ' ', 'g'),
            Trigram('l', 'u', 'n'),
            Trigram('a', 'i', 'n'),
            Trigram('a', 'n', 'd'),
            Trigram('n', 'd', 'a'),
            Trigram('p', 'a', 's'),
            Trigram('k', 'a', 'b'),
            Trigram('a', 'h', 'o'),
            Trigram('l', 'i', 'g'),
            Trigram('n', 'a', 'r'),
            Trigram('u', 'l', 'a'),
            Trigram(' ', 'e', 'd'),
            Trigram('e', 'd', 'u'),
            Trigram(' ', 'i', 'b'),
            Trigram('g', 'i', 't'),
            Trigram('m', 'a', ' '),
            Trigram('m', 'a', 's'),
            Trigram('a', 'g', 'b'),
            Trigram('a', 'm', 'i'),
            Trigram('a', 'g', 'g'),
            Trigram('g', 'i', ' '),
            Trigram('s', 'a', 'r'),
            Trigram('i', ' ', 'm'),
            Trigram('s', 'i', 'y'),
            Trigram('g', ' ', 'w'),
            Trigram('a', 'p', 'i'),
            Trigram('p', 'u', 'l'),
            Trigram('i', 'y', 'a'),
            Trigram('a', 'm', 'b'),
            Trigram('n', 'i', 'l'),
            Trigram('a', 'g', 'l'),
            Trigram('s', 't', 'a'),
            Trigram('u', 'l', 'i'),
            Trigram('i', 'n', 'o'),
            Trigram('a', 'b', 'u'),
            Trigram('a', 'u', 'n'),
            Trigram('a', 'y', 'u'),
            Trigram(' ', 'a', 'l'),
            Trigram('i', 'y', 'o'),
        ],
    ),
    (
        Lang::Hun,
        &[
            Trigram(' ', 's', 'z'),
            Trigram(' ', 'a', ' '),
            Trigram('e', 'n', ' '),
            Trigram(' ', 'v', 'a'),
            Trigram('é', 's', ' '),
            Trigram(' ', 'é', 's'),
            Trigram('m', 'i', 'n'),
            Trigram('e', 'k', ' '),
            Trigram(' ', 'm', 'i'),
            Trigram(' ', 'j', 'o'),
            Trigram('j', 'o', 'g'),
            Trigram('i', 'n', 'd'),
            Trigram('a', 'n', ' '),
            Trigram('n', 'e', 'k'),
            Trigram('s', 'z', 'e'),
            Trigram('s', 'á', 'g'),
            Trigram(' ', 'a', 'z'),
            Trigram('g', 'y', ' '),
            Trigram('s', 'z', 'a'),
            Trigram('n', 'd', 'e'),
            Trigram('a', 'l', 'a'),
            Trigram('a', 'z', ' '),
            Trigram('d', 'e', 'n'),
            Trigram('a', ' ', 'v'),
            Trigram('v', 'a', 'l'),
            Trigram('e', 'l', 'e'),
            Trigram(' ', 'e', 'l'),
            Trigram('o', 'g', 'a'),
            Trigram('m', 'é', 'l'),
            Trigram('e', 'g', 'y'),
            Trigram(' ', 'e', 'g'),
            Trigram('n', ' ', 'a'),
            Trigram('g', 'a', ' '),
            Trigram('z', 'a', 'b'),
            Trigram(' ', 'm', 'e'),
            Trigram('z', 'e', 'm'),
            Trigram('e', 'm', 'é'),
            Trigram('a', 'b', 'a'),
            Trigram('i', 'n', 't'),
            Trigram('v', 'a', 'n'),
            Trigram('b', 'a', 'd'),
            Trigram('t', 'e', 'l'),
            Trigram('t', 'e', 't'),
            Trigram(' ', 't', 'e'),
            Trigram('a', 'k', ' '),
            Trigram('t', 'á', 's'),
            Trigram('é', 'n', 'y'),
            Trigram('t', ' ', 'a'),
            Trigram(' ', 'n', 'e'),
            Trigram('g', 'y', 'e'),
            Trigram('é', 'l', 'y'),
            Trigram('t', 't', ' '),
            Trigram('n', ' ', 's'),
            Trigram('b', 'e', 'n'),
            Trigram('s', 'é', 'g'),
            Trigram('z', 'e', 't'),
            Trigram('l', 'a', 'm'),
            Trigram('m', 'e', 'g'),
            Trigram('n', 'a', 'k'),
            Trigram('n', 'i', ' '),
            Trigram(' ', 's', 'e'),
            Trigram('e', 't', 'e'),
            Trigram('s', 'e', 'n'),
            Trigram('a', 'g', 'y'),
            Trigram('l', 'e', 't'),
            Trigram('l', 'y', 'n'),
            Trigram('s', ' ', 'a'),
            Trigram('y', 'n', 'e'),
            Trigram('r', 'a', ' '),
            Trigram('z', ' ', 'e'),
            Trigram('e', 't', ' '),
            Trigram(' ', 'a', 'l'),
            Trigram('m', 'e', 'l'),
            Trigram('k', 'i', 'n'),
            Trigram('k', ' ', 'j'),
            Trigram('e', 't', 'é'),
            Trigram('o', 'k', ' '),
            Trigram('t', 'e', 'k'),
            Trigram(' ', 'k', 'i'),
            Trigram('v', 'a', 'g'),
            Trigram('r', 'e', ' '),
            Trigram('n', ' ', 'm'),
            Trigram('o', 'z', ' '),
            Trigram('h', 'o', 'z'),
            Trigram('e', 'z', ' '),
            Trigram('s', ' ', 's'),
            Trigram('e', 't', 't'),
            Trigram('g', 'o', 'k'),
            Trigram('o', 'g', 'y'),
            Trigram(' ', 'k', 'ö'),
            Trigram('m', 'b', 'e'),
            Trigram('e', 's', ' '),
            Trigram('e', 'm', ' '),
            Trigram('n', 'e', 'm'),
            Trigram('e', 'l', 'y'),
            Trigram(' ', 'l', 'e'),
            Trigram('e', 'l', 'l'),
            Trigram('e', 'm', 'b'),
            Trigram('h', 'o', 'g'),
            Trigram('k', ' ', 'a'),
            Trigram('a', 't', 'á'),
            Trigram('k', 'ö', 'z'),
            Trigram('n', 't', ' '),
            Trigram(' ', 'h', 'o'),
            Trigram('y', 'e', 'n'),
            Trigram('h', 'e', 'z'),
            Trigram('e', 'l', ' '),
            Trigram('z', ' ', 'a'),
            Trigram('l', 'e', 'n'),
            Trigram('d', 's', 'á'),
            Trigram('á', 's', 'á'),
            Trigram('t', 'é', 's'),
            Trigram('a', 'd', 's'),
            Trigram('k', ' ', 'm'),
            Trigram(' ', 'á', 'l'),
            Trigram(' ', 'e', 'm'),
            Trigram('a', ' ', 's'),
            Trigram('n', 't', 'e'),
            Trigram('a', ' ', 'm'),
            Trigram('s', 'z', 't'),
            Trigram('a', ' ', 't'),
            Trigram('á', 'l', 'l'),
            Trigram('á', 's', ' '),
            Trigram('y', ' ', 'a'),
            Trigram('o', 'g', 'o'),
            Trigram('s', 'e', 'm'),
            Trigram('a', ' ', 'h'),
            Trigram('e', 'n', 'k'),
            Trigram('n', 'y', 'e'),
            Trigram('e', 's', 'e'),
            Trigram('n', 'k', 'i'),
            Trigram('á', 'g', 'o'),
            Trigram('t', ' ', 's'),
            Trigram('l', 'a', 'p'),
            Trigram('a', 'm', 'e'),
            Trigram('b', 'e', 'r'),
            Trigram('l', 'ó', ' '),
            Trigram('k', ' ', 'é'),
            Trigram('n', 'y', 'i'),
            Trigram('b', 'a', 'n'),
            Trigram('m', 'é', 'n'),
            Trigram('s', ' ', 'e'),
            Trigram('i', ' ', 'm'),
            Trigram('t', ' ', 'm'),
            Trigram(' ', 'v', 'é'),
            Trigram('l', 'l', 'a'),
            Trigram('l', 'y', ' '),
            Trigram('é', 'b', 'e'),
            Trigram('l', 'a', 't'),
            Trigram('á', 'g', ' '),
            Trigram('a', 'm', 'i'),
            Trigram('o', 'n', ' '),
            Trigram('m', 'z', 'e'),
            Trigram('n', ' ', 'v'),
            Trigram('e', 'm', 'z'),
            Trigram('f', 'e', 'l'),
            Trigram('a', ' ', 'n'),
            Trigram('l', 'ő', ' '),
            Trigram('a', ' ', 'a'),
            Trigram('e', 'k', 'i'),
            Trigram('e', 'r', 'i'),
            Trigram('y', 'e', 's'),
            Trigram(' ', 'c', 's'),
            Trigram('l', 'l', 'e'),
            Trigram('t', 'a', 't'),
            Trigram('e', 'l', 'ő'),
            Trigram('n', 'd', ' '),
            Trigram('i', ' ', 'é'),
            Trigram('é', 'g', ' '),
            Trigram('é', 's', 'é'),
            Trigram('l', 'i', 's'),
            Trigram('y', 'i', 'l'),
            Trigram('v', 'e', 't'),
            Trigram('á', 't', ' '),
            Trigram('k', 'ü', 'l'),
            Trigram('é', 'r', 't'),
            Trigram(' ', 'k', 'e'),
            Trigram('é', 't', 'e'),
            Trigram('r', 'é', 's'),
            Trigram('l', ' ', 'a'),
            Trigram('h', 'e', 't'),
            Trigram('s', 'z', 'o'),
            Trigram('a', 'r', 't'),
            Trigram('a', 'l', 'á'),
            Trigram(' ', 'n', 'y'),
            Trigram('t', 'a', 'r'),
            Trigram('k', 'o', 'z'),
            Trigram(' ', 'a', 'm'),
            Trigram('a', ' ', 'j'),
            Trigram('é', 's', 'z'),
            Trigram('e', 'n', 'l'),
            Trigram('e', 'l', 'é'),
            Trigram('ó', 'l', ' '),
            Trigram('s', ' ', 'k'),
            Trigram('t', 'á', 'r'),
            Trigram('s', ' ', 'é'),
            Trigram('é', 'l', 'e'),
            Trigram('s', ' ', 't'),
            Trigram('l', 'e', 'm'),
            Trigram('s', 'í', 't'),
            Trigram('g', 'e', 's'),
            Trigram('o', 't', 't'),
            Trigram(' ', 'f', 'e'),
            Trigram('n', ' ', 'k'),
            Trigram('t', 'k', 'o'),
            Trigram('z', 'á', 's'),
            Trigram('t', ' ', 'é'),
            Trigram('k', 'e', 'l'),
            Trigram('j', 'a', ' '),
            Trigram(' ', 'h', 'a'),
            Trigram('a', 'l', 'ó'),
            Trigram('z', 'é', 's'),
            Trigram('n', 'l', 'ő'),
            Trigram('é', 's', 'e'),
            Trigram('o', 't', ' '),
            Trigram('r', 'i', ' '),
            Trigram('l', 'e', 'k'),
            Trigram('m', 'á', 's'),
            Trigram('t', 'ő', ' '),
            Trigram('v', 'e', 'l'),
            Trigram('i', ' ', 'j'),
            Trigram('s', 'e', ' '),
            Trigram('e', 'h', 'e'),
            Trigram('t', 'e', 's'),
            Trigram('e', 'v', 'e'),
            Trigram('s', 's', 'á'),
            Trigram('t', 'o', 't'),
            Trigram('t', ' ', 'k'),
            Trigram('o', 'l', 'g'),
            Trigram('e', 'z', 'e'),
            Trigram('i', ' ', 'v'),
            Trigram('á', 'z', 'a'),
            Trigram('l', 'e', 'h'),
            Trigram('n', ' ', 'e'),
            Trigram('ü', 'l', ' '),
            Trigram('t', 't', 'e'),
            Trigram('o', 's', ' '),
            Trigram('t', 'i', ' '),
            Trigram('a', 't', 'k'),
            Trigram('z', 't', 'o'),
            Trigram('e', ' ', 'a'),
            Trigram('t', 'o', 's'),
            Trigram('á', 'n', 'y'),
            Trigram('á', 'n', 'a'),
            Trigram('z', 't', 'e'),
            Trigram('f', 'e', 'j'),
            Trigram('d', 'e', 'l'),
            Trigram('á', 'r', 's'),
            Trigram('k', ' ', 'k'),
            Trigram('k', 'o', 'r'),
            Trigram('é', 'g', 'e'),
            Trigram('s', 'z', 'á'),
            Trigram('t', ' ', 'n'),
            Trigram(' ', 'b', 'i'),
            Trigram('z', 'a', 't'),
            Trigram('v', 'é', 'd'),
            Trigram('n', 'e', 'v'),
            Trigram('e', 'l', 'm'),
            Trigram('é', 'd', 'e'),
            Trigram('z', 'e', 'r'),
            Trigram('t', 'é', 'b'),
            Trigram('b', 'i', 'z'),
            Trigram('r', 'r', 'a'),
            Trigram('i', 'f', 'e'),
            Trigram('i', 'z', 't'),
            Trigram('e', 'r', 'e'),
            Trigram('a', 't', ' '),
            Trigram('l', 'l', ' '),
            Trigram('k', ' ', 'e'),
            Trigram('n', 'y', ' '),
            Trigram('s', 'e', 'l'),
            Trigram(' ', 'n', 'é'),
            Trigram('á', 'b', 'a'),
            Trigram('l', 't', ' '),
            Trigram('a', 'i', ' '),
            Trigram('s', 'ü', 'l'),
            Trigram('h', 'á', 'z'),
            Trigram('k', 'i', 'f'),
            Trigram('t', ' ', 'e'),
            Trigram(' ', 'a', 'r'),
            Trigram('l', 'e', 'g'),
            Trigram('d', ' ', 'a'),
            Trigram('i', 's', ' '),
            Trigram('i', ' ', 'e'),
            Trigram('a', 'r', 'r'),
            Trigram('t', ' ', 't'),
            Trigram('á', 's', 'o'),
            Trigram('i', 't', ' '),
            Trigram('e', 't', 'ő'),
            Trigram('a', 'l', ' '),
            Trigram(' ', 'm', 'á'),
            Trigram('t', ' ', 'v'),
            Trigram(' ', 'b', 'á'),
            Trigram('b', 'á', 'r'),
            Trigram('a', ' ', 'é'),
            Trigram('e', 's', 'ü'),
            Trigram('l', 'y', 'e'),
            Trigram('m', ' ', 'l'),
            Trigram(' ', 'e', 's'),
            Trigram('n', 'y', 'o'),
        ],
    ),
    (
        Lang::Aze,
        &[
            Trigram(' ', 'v', 'ə'),
            Trigram('v', 'ə', ' '),
            Trigram('ə', 'r', ' '),
            Trigram('l', 'a', 'r'),
            Trigram(' ', 'h', 'ə'),
            Trigram('i', 'n', ' '),
            Trigram('i', 'r', ' '),
            Trigram(' ', 'o', 'l'),
            Trigram(' ', 'h', 'ü'),
            Trigram(' ', 'b', 'i'),
            Trigram('h', 'ü', 'q'),
            Trigram('ü', 'q', 'u'),
            Trigram('q', 'u', 'q'),
            Trigram('n', 'a', ' '),
            Trigram('l', 'ə', 'r'),
            Trigram('d', 'ə', ' '),
            Trigram('h', 'ə', 'r'),
            Trigram(' ', 'ş', 'ə'),
            Trigram('b', 'i', 'r'),
            Trigram('a', 'n', ' '),
            Trigram('l', 'i', 'k'),
            Trigram(' ', 't', 'ə'),
            Trigram('r', ' ', 'b'),
            Trigram('m', 'a', 'l'),
            Trigram('l', 'm', 'a'),
            Trigram('a', 's', 'ı'),
            Trigram('i', 'n', 'i'),
            Trigram('r', ' ', 'h'),
            Trigram('ə', 'x', 's'),
            Trigram('ş', 'ə', 'x'),
            Trigram('ə', 'n', ' '),
            Trigram('a', 'r', 'ı'),
            Trigram('q', 'l', 'a'),
            Trigram('a', ' ', 'm'),
            Trigram('d', 'i', 'r'),
            Trigram('a', 'q', ' '),
            Trigram('u', 'q', 'u'),
            Trigram('a', 'l', 'i'),
            Trigram(' ', 'm', 'a'),
            Trigram('u', 'n', 'a'),
            Trigram('i', 'l', 'ə'),
            Trigram('ı', 'n', ' '),
            Trigram('y', 'ə', 't'),
            Trigram(' ', 'y', 'a'),
            Trigram('a', 'r', 'a'),
            Trigram('i', 'k', 'd'),
            Trigram('ə', 'r', 'i'),
            Trigram('a', 'r', ' '),
            Trigram('ə', 's', 'i'),
            Trigram('ə', 't', 'i'),
            Trigram('r', ' ', 'ş'),
            Trigram('r', 'i', 'n'),
            Trigram('y', 'y', 'ə'),
            Trigram('n', ' ', 'h'),
            Trigram(' ', 'a', 'z'),
            Trigram('d', 'ə', 'n'),
            Trigram('n', 'i', 'n'),
            Trigram('ə', 'r', 'ə'),
            Trigram('t', 'i', 'n'),
            Trigram('i', 'y', 'y'),
            Trigram('m', 'ə', 'k'),
            Trigram('z', 'a', 'd'),
            Trigram(' ', 'm', 'ü'),
            Trigram('s', 'i', 'n'),
            Trigram(' ', 'm', 'ə'),
            Trigram('n', 'i', ' '),
            Trigram('n', 'd', 'a'),
            Trigram('ə', 't', ' '),
            Trigram('n', 'd', 'ə'),
            Trigram('a', 'z', 'a'),
            Trigram('r', 'ı', 'n'),
            Trigram('ü', 'n', ' '),
            Trigram('ı', 'n', 'ı'),
            Trigram('ə', ' ', 'a'),
            Trigram('i', ' ', 'v'),
            Trigram('n', 'ı', 'n'),
            Trigram('o', 'l', 'u'),
            Trigram('q', 'u', 'n'),
            Trigram(' ', 'q', 'a'),
            Trigram(' ', 'e', 't'),
            Trigram('i', 'l', 'm'),
            Trigram('l', 'ı', 'q'),
            Trigram('ə', ' ', 'y'),
            Trigram('ə', 'k', ' '),
            Trigram('l', 'm', 'ə'),
            Trigram('l', 'ə', ' '),
            Trigram('k', 'd', 'i'),
            Trigram('i', 'n', 'd'),
            Trigram('ı', 'n', 'a'),
            Trigram('o', 'l', 'm'),
            Trigram('l', 'u', 'n'),
            Trigram('m', 'a', 's'),
            Trigram('x', 's', ' '),
            Trigram('s', 'ı', 'n'),
            Trigram('ə', ' ', 'b'),
            Trigram(' ', 'i', 'n'),
            Trigram('n', ' ', 'm'),
            Trigram('q', ' ', 'v'),
            Trigram('n', 'ə', ' '),
            Trigram('ə', 'm', 'i'),
            Trigram('n', ' ', 't'),
            Trigram('y', 'a', ' '),
            Trigram('d', 'a', ' '),
            Trigram(' ', 'b', 'ə'),
            Trigram('t', 'm', 'ə'),
            Trigram('d', 'l', 'ı'),
            Trigram('a', 'd', 'l'),
            Trigram('b', 'ə', 'r'),
            Trigram(' ', 'o', 'n'),
            Trigram('ə', 'y', 'a'),
            Trigram('ə', ' ', 'h'),
            Trigram('s', 'ı', ' '),
            Trigram('n', 'u', 'n'),
            Trigram('m', 'a', 'q'),
            Trigram('d', 'a', 'n'),
            Trigram('i', 'n', 'ə'),
            Trigram('e', 't', 'm'),
            Trigram('u', 'n', ' '),
            Trigram('ə', ' ', 'v'),
            Trigram('r', 'l', 'ə'),
            Trigram('n', ' ', 'b'),
            Trigram('s', 'i', ' '),
            Trigram('r', 'a', 'q'),
            Trigram(' ', 'v', 'a'),
            Trigram('ə', ' ', 'm'),
            Trigram('n', ' ', 'a'),
            Trigram('ı', 'n', 'd'),
            Trigram('r', 'ı', ' '),
            Trigram('a', 'n', 'ı'),
            Trigram(' ', 'ö', 'z'),
            Trigram('ə', 'r', 'a'),
            Trigram('n', 'm', 'a'),
            Trigram('n', ' ', 'i'),
            Trigram('a', 'm', 'a'),
            Trigram('a', ' ', 'b'),
            Trigram('i', 'r', 'l'),
            Trigram('a', 'l', 'a'),
            Trigram('l', 'i', ' '),
            Trigram('i', 'n', 's'),
            Trigram('b', 'i', 'l'),
            Trigram('i', 'k', ' '),
            Trigram(' ', 'a', 'l'),
            Trigram(' ', 'd', 'i'),
            Trigram('ı', 'ğ', 'ı'),
            Trigram('ə', ' ', 'd'),
            Trigram('l', 'ə', 't'),
            Trigram('i', 'l', ' '),
            Trigram('ə', 'l', 'ə'),
            Trigram('ə', ' ', 'i'),
            Trigram('ı', 'q', ' '),
            Trigram('n', 'ı', ' '),
            Trigram('n', 'l', 'a'),
            Trigram('d', 'i', 'l'),
            Trigram('m', 'ü', 'd'),
            Trigram('n', ' ', 'v'),
            Trigram('ə', ' ', 'e'),
            Trigram('u', 'n', 'm'),
            Trigram('a', 'l', 'ı'),
            Trigram(' ', 's', 'ə'),
            Trigram('x', 's', 'i'),
            Trigram('ə', ' ', 'o'),
            Trigram('u', 'q', ' '),
            Trigram('u', 'q', 'l'),
            Trigram('n', 's', 'a'),
            Trigram('ə', 't', 'l'),
            Trigram(' ', 'd', 'ə'),
            Trigram('i', 'l', 'i'),
            Trigram('ü', 'd', 'a'),
            Trigram('a', 's', 'i'),
            Trigram(' ', 'h', 'e'),
            Trigram('o', 'l', 'a'),
            Trigram('s', 'a', 'n'),
            Trigram('ə', 'n', 'i'),
            Trigram('m', 'ə', 's'),
            Trigram(' ', 'd', 'a'),
            Trigram('l', 'a', 'n'),
            Trigram(' ', 'b', 'u'),
            Trigram('t', 'ə', 'r'),
            Trigram('h', 'ə', 'm'),
            Trigram('d', 'ı', 'r'),
            Trigram('k', 'i', 'l'),
            Trigram('i', 'ş', ' '),
            Trigram('u', ' ', 'v'),
            Trigram(' ', 'k', 'i'),
            Trigram('m', 'i', 'n'),
            Trigram('e', 'y', 'n'),
            Trigram('m', 'i', ' '),
            Trigram('y', 'i', 'n'),
            Trigram(' ', 'h', 'a'),
            Trigram('s', 'o', 's'),
            Trigram('h', 'e', 'ç'),
            Trigram('b', 'u', ' '),
            Trigram('e', 'ç', ' '),
            Trigram(' ', 'e', 'd'),
            Trigram('k', 'i', 'm'),
            Trigram('l', 'ı', 'ğ'),
            Trigram('a', 'l', 'q'),
            Trigram('x', 'a', 'l'),
            Trigram(' ', 'a', 's'),
            Trigram('s', 'i', 'a'),
            Trigram('o', 's', 'i'),
            Trigram('r', ' ', 'v'),
            Trigram('q', ' ', 'h'),
            Trigram('r', 'ə', ' '),
            Trigram('y', 'a', 'n'),
            Trigram('i', ' ', 's'),
            Trigram(' ', 'ə', 's'),
            Trigram('d', 'a', 'f'),
            Trigram('a', 'f', 'i'),
            Trigram(' ', 'i', 'ş'),
            Trigram('ı', ' ', 'h'),
            Trigram('f', 'i', 'ə'),
            Trigram(' ', 't', 'a'),
            Trigram('ə', ' ', 'q'),
            Trigram('ı', 'q', 'l'),
            Trigram('a', ' ', 'q'),
            Trigram('y', 'a', 'r'),
            Trigram('s', 'a', 's'),
            Trigram('l', 'ı', ' '),
            Trigram('i', 'l', 'l'),
            Trigram('m', 'i', 'l'),
            Trigram('ə', 's', 'a'),
            Trigram('l', 'i', 'y'),
            Trigram('t', 'l', 'ə'),
            Trigram('s', 'i', 'y'),
            Trigram('a', ' ', 'h'),
            Trigram('m', 'ə', 'z'),
            Trigram('t', 'ü', 'n'),
            Trigram('ə', ' ', 't'),
            Trigram(' ', 'i', 's'),
            Trigram('i', 's', 't'),
            Trigram('i', 'y', 'i'),
            Trigram(' ', 's', 'o'),
            Trigram('n', ' ', 'ə'),
            Trigram('a', 'l', ' '),
            Trigram('i', 'f', 'a'),
            Trigram('i', 'n', 'a'),
            Trigram('l', 'ı', 'd'),
            Trigram('ı', ' ', 'o'),
            Trigram('ı', 'd', 'ı'),
            Trigram('ə', 'm', 'ə'),
            Trigram('ı', 'r', ' '),
            Trigram('ə', 'd', 'ə'),
            Trigram('i', 'a', 'l'),
            Trigram(' ', 'm', 'i'),
            Trigram('ə', 'y', 'i'),
            Trigram('m', 'i', 'y'),
            Trigram('ç', 'ü', 'n'),
            Trigram('n', ' ', 'e'),
            Trigram('i', 'y', 'a'),
            Trigram('e', 'd', 'i'),
            Trigram(' ', 'c', 'ə'),
            Trigram(' ', 'b', 'ü'),
            Trigram('b', 'ü', 't'),
            Trigram('ü', 't', 'ü'),
            Trigram('x', 'i', 'l'),
            Trigram('ü', 'ç', 'ü'),
            Trigram('m', 'ə', 'n'),
            Trigram('a', 'd', 'ə'),
            Trigram('t', ' ', 'v'),
            Trigram('a', ' ', 'v'),
            Trigram('a', 'x', 'i'),
            Trigram('d', 'a', 'x'),
            Trigram('r', ' ', 'a'),
            Trigram('o', 'n', 'u'),
            Trigram(' ', 'ü', 'ç'),
            Trigram('s', 'e', 'ç'),
            Trigram(' ', 'n', 'ə'),
            Trigram(' ', 's', 'e'),
            Trigram('m', 'a', 'n'),
            Trigram('r', 'i', 'l'),
            Trigram('s', 'i', 'l'),
            Trigram('ə', 'z', ' '),
            Trigram('i', 'ə', ' '),
            Trigram('ö', 'z', ' '),
            Trigram('ı', 'l', 'ı'),
            Trigram('a', 'y', 'a'),
            Trigram('q', 'a', 'n'),
            Trigram('i', ' ', 't'),
            Trigram('ş', 'ə', 'r'),
            Trigram('t', 'ə', 'm'),
            Trigram('u', 'l', 'm'),
            Trigram('r', 'ə', 'f'),
            Trigram('m', 'ə', 'h'),
            Trigram(' ', 'x', 'a'),
            Trigram('ğ', 'ı', 'n'),
            Trigram(' ', 'd', 'ö'),
            Trigram(' ', 'n', 'i'),
            Trigram('s', 't', 'i'),
            Trigram('i', 'l', 'd'),
            Trigram('a', 'm', 'ə'),
            Trigram('q', 'u', ' '),
            Trigram('n', 'a', 'm'),
            Trigram('n', ' ', 'o'),
            Trigram('n', ' ', 'd'),
            Trigram('v', 'a', 'r'),
            Trigram('a', 'd', ' '),
            Trigram('z', 'a', 'm'),
            Trigram('t', 'a', 'm'),
            Trigram('t', 'ə', 'h'),
        ],
    ),
    (
        Lang::Ces,
        &[
            Trigram(' ', 'p', 'r'),
            Trigram(' ', 'a', ' '),
            Trigram('n', 'í', ' '),
            Trigram(' ', 'n', 'e'),
            Trigram('p', 'r', 'á'),
            Trigram('r', 'á', 'v'),
            Trigram('o', 's', 't'),
            Trigram(' ', 's', 'v'),
            Trigram(' ', 'p', 'o'),
            Trigram('n', 'a', ' '),
            Trigram('c', 'h', ' '),
            Trigram('h', 'o', ' '),
            Trigram(' ', 'n', 'a'),
            Trigram('n', 'o', 's'),
            Trigram('o', ' ', 'n'),
            Trigram(' ', 'r', 'o'),
            Trigram('á', 'n', 'í'),
            Trigram('t', 'i', ' '),
            Trigram('v', 'o', ' '),
            Trigram('n', 'e', 'b'),
            Trigram('á', 'v', 'o'),
            Trigram('m', 'á', ' '),
            Trigram('b', 'o', ' '),
            Trigram('e', 'b', 'o'),
            Trigram(' ', 'm', 'á'),
            Trigram('k', 'a', 'ž'),
            Trigram(' ', 'k', 'a'),
            Trigram('o', 'u', ' '),
            Trigram('a', 'ž', 'd'),
            Trigram(' ', 'z', 'a'),
            Trigram(' ', 'j', 'e'),
            Trigram('d', 'ý', ' '),
            Trigram('s', 'v', 'o'),
            Trigram('ž', 'd', 'ý'),
            Trigram(' ', 'p', 'ř'),
            Trigram('a', ' ', 's'),
            Trigram(' ', 's', 't'),
            Trigram('s', 't', 'i'),
            Trigram('á', ' ', 'p'),
            Trigram(' ', 'v', ' '),
            Trigram('o', 'b', 'o'),
            Trigram('v', 'o', 'b'),
            Trigram(' ', 's', 'p'),
            Trigram('b', 'o', 'd'),
            Trigram(' ', 'z', 'á'),
            Trigram('ý', 'c', 'h'),
            Trigram('p', 'r', 'o'),
            Trigram('r', 'o', 'd'),
            Trigram('v', 'á', 'n'),
            Trigram('e', 'n', 'í'),
            Trigram('n', 'é', ' '),
            Trigram('ý', ' ', 'm'),
            Trigram('é', 'h', 'o'),
            Trigram(' ', 'b', 'y'),
            Trigram(' ', 'n', 'á'),
            Trigram('s', 'p', 'o'),
            Trigram('n', 'ě', ' '),
            Trigram('o', ' ', 'p'),
            Trigram('m', 'i', ' '),
            Trigram('í', ' ', 'a'),
            Trigram('t', 'e', 'r'),
            Trigram('r', 'o', 'z'),
            Trigram('o', 'v', 'á'),
            Trigram('t', 'o', ' '),
            Trigram(' ', 'j', 'a'),
            Trigram(' ', 'l', 'i'),
            Trigram('á', 'r', 'o'),
            Trigram('n', 'á', 'r'),
            Trigram('b', 'y', ' '),
            Trigram('j', 'a', 'k'),
            Trigram('a', ' ', 'p'),
            Trigram('a', ' ', 'z'),
            Trigram('n', 'y', ' '),
            Trigram(' ', 'v', 'š'),
            Trigram('k', 't', 'e'),
            Trigram('i', ' ', 'a'),
            Trigram('l', 'i', 'd'),
            Trigram('í', 'm', ' '),
            Trigram('o', ' ', 'v'),
            Trigram('í', ' ', 'p'),
            Trigram('u', ' ', 'p'),
            Trigram('m', 'u', ' '),
            Trigram('a', 't', ' '),
            Trigram(' ', 'v', 'y'),
            Trigram('o', 'd', 'n'),
            Trigram(' ', 's', 'o'),
            Trigram(' ', 'm', 'a'),
            Trigram('a', ' ', 'v'),
            Trigram(' ', 'k', 't'),
            Trigram('í', ' ', 'n'),
            Trigram('z', 'á', 'k'),
            Trigram('l', 'i', ' '),
            Trigram('o', 'l', 'i'),
            Trigram('v', 'í', ' '),
            Trigram('k', 'l', 'a'),
            Trigram('t', 'n', 'í'),
            Trigram('p', 'o', 'd'),
            Trigram('s', 't', 'á'),
            Trigram('e', 'n', ' '),
            Trigram('d', 'o', ' '),
            Trigram('t', ' ', 's'),
            Trigram('m', 'í', ' '),
            Trigram('j', 'e', ' '),
            Trigram('e', 'm', ' '),
            Trigram('á', 'v', 'a'),
            Trigram(' ', 'd', 'o'),
            Trigram('b', 'y', 'l'),
            Trigram(' ', 's', 'e'),
            Trigram('b', 'ý', 't'),
            Trigram('í', ' ', 's'),
            Trigram('r', 'o', 'v'),
            Trigram(' ', 'k', ' '),
            Trigram('č', 'i', 'n'),
            Trigram(' ', 'v', 'e'),
            Trigram('ý', 't', ' '),
            Trigram('í', ' ', 'b'),
            Trigram('i', 't', ' '),
            Trigram('d', 'n', 'í'),
            Trigram('v', 'š', 'e'),
            Trigram('p', 'o', 'l'),
            Trigram('o', ' ', 's'),
            Trigram(' ', 'b', 'ý'),
            Trigram('t', 'v', 'í'),
            Trigram('n', 'ý', 'c'),
            Trigram('s', 't', 'n'),
            Trigram('n', 'o', 'u'),
            Trigram('e', 'j', 'n'),
            Trigram('s', 'o', 'u'),
            Trigram('r', 'a', 'n'),
            Trigram('c', 'i', ' '),
            Trigram('v', 'o', 'l'),
            Trigram('s', 'e', ' '),
            Trigram('n', 'e', 's'),
            Trigram('a', ' ', 'n'),
            Trigram('p', 'ř', 'í'),
            Trigram('e', 'h', 'o'),
            Trigram('n', 'ý', 'm'),
            Trigram('t', 'á', 't'),
            Trigram('v', 'a', ' '),
            Trigram('n', 'í', 'm'),
            Trigram('m', 'e', 'z'),
            Trigram('a', 'j', 'í'),
            Trigram('i', ' ', 's'),
            Trigram('s', 't', 'v'),
            Trigram('k', 'é', ' '),
            Trigram('í', 'c', 'h'),
            Trigram('e', 'č', 'n'),
            Trigram('ž', 'e', 'n'),
            Trigram('e', ' ', 's'),
            Trigram('v', 'é', ' '),
            Trigram('o', 'v', 'a'),
            Trigram('s', 'v', 'é'),
            Trigram('ý', 'm', ' '),
            Trigram('k', 'o', 'l'),
            Trigram('d', 'u', ' '),
            Trigram('u', ' ', 's'),
            Trigram('j', 'e', 'h'),
            Trigram('k', 'o', 'n'),
            Trigram('a', 'v', 'e'),
            Trigram('e', 'c', 'h'),
            Trigram('e', 'r', 'é'),
            Trigram('n', 'u', ' '),
            Trigram(' ', 'z', 'e'),
            Trigram('i', ' ', 'v'),
            Trigram('o', ' ', 'd'),
            Trigram('í', ' ', 'v'),
            Trigram('h', 'r', 'a'),
            Trigram('i', 'd', 's'),
            Trigram('m', ' ', 'p'),
            Trigram('é', 'm', 'u'),
            Trigram('o', 'l', 'e'),
            Trigram('y', ' ', 's'),
            Trigram(' ', 'i', ' '),
            Trigram('m', 'a', 'j'),
            Trigram('o', ' ', 'z'),
            Trigram(' ', 't', 'o'),
            Trigram('a', 'b', 'y'),
            Trigram('s', 't', 'a'),
            Trigram(' ', 'a', 'b'),
            Trigram('m', ' ', 'a'),
            Trigram('p', 'r', 'a'),
            Trigram(' ', 't', 'a'),
            Trigram('c', 'h', 'n'),
            Trigram(' ', 'n', 'i'),
            Trigram('ž', 'e', ' '),
            Trigram('o', 'v', 'n'),
            Trigram('a', 'k', 'o'),
            Trigram('n', 'é', 'h'),
            Trigram('l', 'e', 'n'),
            Trigram('d', 's', 'k'),
            Trigram('r', 'a', 'c'),
            Trigram('l', 'a', 'd'),
            Trigram('c', 'h', 'r'),
            Trigram(' ', 'ž', 'e'),
            Trigram('v', 'a', 't'),
            Trigram(' ', 'o', 's'),
            Trigram('s', 'o', 'b'),
            Trigram('a', 'k', 'é'),
            Trigram('i', ' ', 'p'),
            Trigram('s', 'm', 'í'),
            Trigram('e', 's', 'm'),
            Trigram('s', 't', ' '),
            Trigram('i', ' ', 'n'),
            Trigram('m', ' ', 'n'),
            Trigram('a', ' ', 'm'),
            Trigram('l', 'n', 'ě'),
            Trigram('l', 'n', 'í'),
            Trigram('p', 'ř', 'i'),
            Trigram('b', 'e', 'z'),
            Trigram('d', 'y', ' '),
            Trigram('á', 'l', 'n'),
            Trigram('e', 'n', 's'),
            Trigram('z', 'e', 'm'),
            Trigram('t', ' ', 'v'),
            Trigram('č', 'e', 'n'),
            Trigram('l', 'e', 'č'),
            Trigram('k', 'd', 'o'),
            Trigram('ý', 'm', 'i'),
            Trigram(' ', 'j', 'i'),
            Trigram('o', 'c', 'i'),
            Trigram('i', ' ', 'k'),
            Trigram(' ', 's', ' '),
            Trigram('í', ' ', 'm'),
            Trigram('j', 'í', ' '),
            Trigram(' ', 'č', 'i'),
            Trigram('á', 'v', ' '),
            Trigram('s', 't', 'e'),
            Trigram('o', 'c', 'h'),
            Trigram(' ', 'o', 'c'),
            Trigram('v', 'o', 'u'),
            Trigram('á', 'k', 'l'),
            Trigram(' ', 'v', 'z'),
            Trigram('r', 'a', 'v'),
            Trigram('o', 'd', 'u'),
            Trigram('n', 'e', 'z'),
            Trigram('i', 'n', 'n'),
            Trigram('s', 'k', 'ý'),
            Trigram('n', 'i', 't'),
            Trigram('i', 'v', 'o'),
            Trigram('a', ' ', 'j'),
            Trigram('u', ' ', 'k'),
            Trigram('i', 'á', 'l'),
            Trigram(' ', 'm', 'e'),
            Trigram('e', 'z', 'i'),
            Trigram('s', 'k', 'é'),
            Trigram('v', 'e', 'n'),
            Trigram('s', 't', 'u'),
            Trigram('u', ' ', 'a'),
            Trigram('t', 'e', 'j'),
            Trigram('o', 'l', 'n'),
            Trigram('s', 'l', 'u'),
            Trigram('z', 'e', 'n'),
            Trigram('í', ' ', 'z'),
            Trigram('y', ' ', 'b'),
            Trigram('o', 'k', 'o'),
            Trigram('z', 'a', 'c'),
            Trigram('n', 'í', 'c'),
            Trigram('j', 'i', 'n'),
            Trigram('k', 'y', ' '),
            Trigram('a', ' ', 'o'),
            Trigram('ř', 'í', 's'),
            Trigram('o', 'b', 'e'),
            Trigram('u', ' ', 'v'),
            Trigram('t', 'a', 'k'),
            Trigram('v', 'ě', 'd'),
            Trigram('o', 'j', 'e'),
            Trigram(' ', 'v', 'ý'),
            Trigram('i', 'k', 'd'),
            Trigram('h', ' ', 'n'),
            Trigram(' ', 'o', 'd'),
            Trigram('č', 'n', 'o'),
            Trigram('o', 's', 'o'),
            Trigram('c', 'i', 'á'),
            Trigram('h', ' ', 'p'),
            Trigram(' ', 'd', 'e'),
            Trigram('a', ' ', 't'),
            Trigram('ů', 'm', ' '),
            Trigram('s', 'o', 'c'),
            Trigram('j', 'í', 'c'),
            Trigram('o', 'd', 'ů'),
            Trigram('n', 'ě', 'n'),
            Trigram('a', 'd', 'n'),
            Trigram('t', 'u', 'p'),
            Trigram('d', 'ů', ' '),
            Trigram('d', 'ě', 'l'),
            Trigram('j', 'n', 'o'),
            Trigram('k', 'é', 'h'),
            Trigram('p', 'o', 'r'),
            Trigram('o', 'ž', 'e'),
            Trigram('h', 'o', 'v'),
            Trigram('a', 'c', 'i'),
            Trigram('n', 'e', 'm'),
            Trigram('é', ' ', 'v'),
            Trigram('r', 'o', 'k'),
            Trigram('i', ' ', 'j'),
            Trigram('u', ' ', 'o'),
            Trigram('o', 'd', ' '),
            Trigram('í', 'h', 'o'),
            Trigram('v', 'i', 'n'),
            Trigram('o', 'd', 'i'),
        ],
    ),
    (
        Lang::Zul,
        &[
            Trigram('n', 'g', 'e'),
            Trigram('o', 'k', 'u'),
            Trigram('l', 'o', ' '),
            Trigram(' ', 'n', 'g'),
            Trigram('a', ' ', 'n'),
            Trigram('u', 'n', 'g'),
            Trigram('n', 'g', 'a'),
            Trigram('l', 'e', ' '),
            Trigram('l', 'u', 'n'),
            Trigram(' ', 'n', 'o'),
            Trigram('e', 'l', 'o'),
            Trigram('w', 'a', ' '),
            Trigram('l', 'a', ' '),
            Trigram('e', ' ', 'n'),
            Trigram('e', 'l', 'e'),
            Trigram('n', 't', 'u'),
            Trigram('g', 'e', 'l'),
            Trigram('t', 'u', ' '),
            Trigram('w', 'e', ' '),
            Trigram('n', 'g', 'o'),
            Trigram(' ', 'u', 'm'),
            Trigram('e', ' ', 'u'),
            Trigram('t', 'h', 'i'),
            Trigram('u', 't', 'h'),
            Trigram('k', 'e', ' '),
            Trigram('h', 'i', ' '),
            Trigram('l', 'e', 'k'),
            Trigram('n', 'i', ' '),
            Trigram('e', 'z', 'i'),
            Trigram(' ', 'k', 'u'),
            Trigram('m', 'a', ' '),
            Trigram('n', 'o', 'm'),
            Trigram('o', ' ', 'n'),
            Trigram('p', 'h', 'a'),
            Trigram('g', 'o', 'k'),
            Trigram('n', 'k', 'e'),
            Trigram('o', 'n', 'k'),
            Trigram('a', ' ', 'u'),
            Trigram('n', 'e', 'l'),
            Trigram('u', 'l', 'u'),
            Trigram('o', 'm', 'a'),
            Trigram('o', ' ', 'e'),
            Trigram('o', ' ', 'l'),
            Trigram('k', 'w', 'e'),
            Trigram('u', 'n', 't'),
            Trigram('a', 'n', 'g'),
            Trigram('l', 'u', 'l'),
            Trigram('k', 'u', 'l'),
            Trigram(' ', 'u', 'k'),
            Trigram('a', ' ', 'k'),
            Trigram('e', 'n', 'i'),
            Trigram('u', 'k', 'u'),
            Trigram('h', 'l', 'a'),
            Trigram(' ', 'n', 'e'),
            Trigram(' ', 'w', 'o'),
            Trigram('m', 'u', 'n'),
            Trigram(' ', 'l', 'o'),
            Trigram('k', 'e', 'l'),
            Trigram('a', 'm', 'a'),
            Trigram('a', 't', 'h'),
            Trigram('u', 'm', 'u'),
            Trigram('h', 'o', ' '),
            Trigram('e', 'l', 'a'),
            Trigram('l', 'w', 'a'),
            Trigram('w', 'o', 'n'),
            Trigram('z', 'w', 'e'),
            Trigram('b', 'a', 'n'),
            Trigram('e', 'l', 'w'),
            Trigram('u', 'l', 'e'),
            Trigram('a', ' ', 'i'),
            Trigram(' ', 'u', 'n'),
            Trigram('a', 'n', 'a'),
            Trigram('u', 'n', 'e'),
            Trigram('l', 'o', 'k'),
            Trigram('i', 'n', 'g'),
            Trigram('e', 'l', 'u'),
            Trigram('w', 'e', 'n'),
            Trigram('a', 'k', 'a'),
            Trigram('t', 'h', 'o'),
            Trigram('a', 'b', 'a'),
            Trigram(' ', 'k', 'w'),
            Trigram('g', 'a', 'n'),
            Trigram('k', 'o', ' '),
            Trigram('a', 'l', 'a'),
            Trigram('e', 'n', 'z'),
            Trigram('o', ' ', 'y'),
            Trigram('k', 'h', 'e'),
            Trigram('a', 'k', 'h'),
            Trigram('t', 'h', 'u'),
            Trigram('u', ' ', 'u'),
            Trigram('n', 'a', ' '),
            Trigram('e', 'n', 'k'),
            Trigram('k', 'h', 'o'),
            Trigram('a', ' ', 'e'),
            Trigram('z', 'i', 'n'),
            Trigram('g', 'e', 'n'),
            Trigram('i', ' ', 'n'),
            Trigram('k', 'u', 'n'),
            Trigram('a', 'l', 'u'),
            Trigram('m', 'a', 'l'),
            Trigram('l', 'e', 'l'),
            Trigram('e', ' ', 'k'),
            Trigram('n', 'k', 'u'),
            Trigram('e', ' ', 'a'),
            Trigram('e', 'k', 'o'),
            Trigram(' ', 'n', 'a'),
            Trigram('k', 'a', 't'),
            Trigram('l', 'a', 'n'),
            Trigram('h', 'e', ' '),
            Trigram('h', 'a', 'k'),
            Trigram(' ', 'e', 'z'),
            Trigram('o', ' ', 'a'),
            Trigram('k', 'w', 'a'),
            Trigram('o', ' ', 'o'),
            Trigram('a', 'y', 'o'),
            Trigram('o', 'k', 'w'),
            Trigram('k', 'u', 't'),
            Trigram('k', 'u', 'b'),
            Trigram('l', 'w', 'e'),
            Trigram(' ', 'e', 'm'),
            Trigram('y', 'o', ' '),
            Trigram('n', 'z', 'i'),
            Trigram('a', 'n', 'e'),
            Trigram('o', 'b', 'u'),
            Trigram(' ', 'o', 'k'),
            Trigram('e', 't', 'h'),
            Trigram('h', 'e', 't'),
            Trigram('i', 's', 'e'),
            Trigram('s', 'o', ' '),
            Trigram('i', 'l', 'e'),
            Trigram('n', 'o', 'k'),
            Trigram(' ', 'b', 'a'),
            Trigram('b', 'e', 'n'),
            Trigram('e', 'k', 'i'),
            Trigram('n', 'y', 'e'),
            Trigram('i', 'k', 'e'),
            Trigram('i', ' ', 'k'),
            Trigram('i', 's', 'i'),
            Trigram(' ', 'i', 's'),
            Trigram('a', 'p', 'h'),
            Trigram('e', 's', 'i'),
            Trigram('n', 'h', 'l'),
            Trigram('m', 'p', 'h'),
            Trigram(' ', 'a', 'b'),
            Trigram('f', 'a', 'n'),
            Trigram('e', ' ', 'i'),
            Trigram('i', 's', 'a'),
            Trigram(' ', 'y', 'e'),
            Trigram('n', 'e', 'n'),
            Trigram('i', 'n', 'i'),
            Trigram('g', 'a', ' '),
            Trigram('z', 'i', ' '),
            Trigram('f', 'u', 't'),
            Trigram(' ', 'f', 'u'),
            Trigram('u', 'b', 'a'),
            Trigram('u', 'k', 'h'),
            Trigram('k', 'a', ' '),
            Trigram('a', 'n', 't'),
            Trigram('u', 'h', 'l'),
            Trigram('h', 'o', 'l'),
            Trigram('b', 'a', ' '),
            Trigram('a', 'n', 'd'),
            Trigram('d', 'o', ' '),
            Trigram('k', 'u', 'k'),
            Trigram('a', 'b', 'e'),
            Trigram('z', 'a', ' '),
            Trigram('n', 'd', 'a'),
            Trigram(' ', 'y', 'a'),
            Trigram('e', ' ', 'w'),
            Trigram('k', 'i', 'l'),
            Trigram('t', 'h', 'e'),
            Trigram(' ', 'i', 'm'),
            Trigram('e', 'k', 'e'),
            Trigram('a', ' ', 'a'),
            Trigram('o', 'l', 'o'),
            Trigram('s', 'a', ' '),
            Trigram('o', 'l', 'u'),
            Trigram('i', 't', 'h'),
            Trigram('k', 'u', 'h'),
            Trigram('o', ' ', 'u'),
            Trigram('y', 'e', ' '),
            Trigram('n', 'i', 's'),
            Trigram(' ', 'i', 'n'),
            Trigram('e', 'k', 'h'),
            Trigram('e', ' ', 'e'),
            Trigram(' ', 'a', 'k'),
            Trigram('i', ' ', 'w'),
            Trigram('a', 'n', 'y'),
            Trigram('k', 'h', 'u'),
            Trigram('e', 'n', 'g'),
            Trigram('e', 'l', 'i'),
            Trigram('y', 'o', 'k'),
            Trigram('n', 'e', ' '),
            Trigram('n', 'o', ' '),
            Trigram('u', 'm', 'e'),
            Trigram('n', 'd', 'l'),
            Trigram('i', 'p', 'h'),
            Trigram('a', 'm', 'b'),
            Trigram('e', 'm', 'p'),
            Trigram(' ', 'k', 'o'),
            Trigram('i', ' ', 'i'),
            Trigram(' ', 'l', 'e'),
            Trigram('i', 's', 'w'),
            Trigram('z', 'o', ' '),
            Trigram('a', ' ', 'o'),
            Trigram('e', 'm', 'i'),
            Trigram('u', 'n', 'y'),
            Trigram('m', 'e', 'l'),
            Trigram('e', 'k', 'a'),
            Trigram('m', 't', 'h'),
            Trigram('u', 'p', 'h'),
            Trigram('n', 'd', 'o'),
            Trigram('v', 'i', 'k'),
            Trigram(' ', 'y', 'o'),
            Trigram('h', 'l', 'o'),
            Trigram('a', 'l', 'o'),
            Trigram('k', 'u', 'f'),
            Trigram('y', 'e', 'n'),
            Trigram('e', 'n', 'h'),
            Trigram('o', ' ', 'w'),
            Trigram('n', 'a', 'y'),
            Trigram('l', 'i', 'n'),
            Trigram('h', 'u', 'l'),
            Trigram('e', 'z', 'w'),
            Trigram('i', 'n', 'd'),
            Trigram('e', 'z', 'e'),
            Trigram('e', 'b', 'e'),
            Trigram('k', 'a', 'n'),
            Trigram('k', 'u', 'z'),
            Trigram('p', 'h', 'e'),
            Trigram('k', 'u', 'g'),
            Trigram('n', 'e', 'z'),
            Trigram('a', 'k', 'e'),
            Trigram('n', 'y', 'a'),
            Trigram('w', 'e', 'z'),
            Trigram('w', 'a', 'm'),
            Trigram('s', 'e', 'b'),
            Trigram('u', 'f', 'a'),
            Trigram('b', 'o', ' '),
            Trigram('d', 'i', 'n'),
            Trigram('a', 'h', 'l'),
            Trigram('a', 'z', 'w'),
            Trigram('f', 'u', 'n'),
            Trigram('y', 'e', 'z'),
            Trigram('u', 'n', 'd'),
            Trigram('a', ' ', 'l'),
            Trigram('l', 'i', ' '),
            Trigram('b', 'u', 's'),
            Trigram('a', 'l', 'e'),
            Trigram('u', 'l', 'a'),
            Trigram('k', 'u', 'q'),
            Trigram('o', 'l', 'a'),
            Trigram('i', 'z', 'i'),
            Trigram('i', 'n', 'k'),
            Trigram('i', ' ', 'e'),
            Trigram('d', 'a', ' '),
            Trigram('n', 'a', 'n'),
            Trigram('a', 's', 'e'),
            Trigram('p', 'h', 'i'),
            Trigram('a', 'n', 'o'),
            Trigram('n', 'e', 'm'),
            Trigram('h', 'e', 'l'),
            Trigram('a', ' ', 'y'),
            Trigram('h', 'u', 't'),
            Trigram('k', 'i', 's'),
            Trigram('k', 'u', 'p'),
            Trigram('s', 'w', 'a'),
            Trigram('h', 'a', 'n'),
            Trigram('i', 'l', 'i'),
            Trigram('m', 'b', 'i'),
            Trigram('k', 'u', 'v'),
            Trigram('o', ' ', 'k'),
            Trigram('k', 'e', 'k'),
            Trigram('o', 'm', 'p'),
            Trigram('p', 'h', 'o'),
            Trigram('k', 'o', 'l'),
            Trigram('i', ' ', 'u'),
            Trigram('o', 'k', 'o'),
            Trigram('i', 'z', 'w'),
            Trigram('l', 'o', 'n'),
            Trigram('e', ' ', 'l'),
            Trigram(' ', 'e', 'l'),
            Trigram('u', 'k', 'e'),
            Trigram('k', 'u', 's'),
            Trigram('k', 'o', 'm'),
            Trigram('u', 'l', 'o'),
            Trigram('z', 'i', 's'),
            Trigram('h', 'u', 'n'),
            Trigram('n', 'j', 'e'),
            Trigram('l', 'a', 'k'),
            Trigram('u', ' ', 'n'),
            Trigram('h', 'u', 'k'),
            Trigram('s', 'e', 'k'),
            Trigram('h', 'a', 'm'),
            Trigram(' ', 'o', 'l'),
            Trigram('a', 'n', 'i'),
            Trigram('o', ' ', 'i'),
            Trigram('u', 'b', 'u'),
            Trigram('m', 'b', 'a'),
            Trigram(' ', 'a', 'm'),
        ],
    ),
    (
        Lang::Swe,
        &[
            Trigram(' ', 'o', 'c'),
            Trigram('o', 'c', 'h'),
            Trigram('c', 'h', ' '),
            Trigram('e', 'r', ' '),
            Trigram('i', 'n', 'g'),
            Trigram('f', 'ö', 'r'),
            Trigram('t', 't', ' '),
            Trigram('a', 'r', ' '),
            Trigram('e', 'n', ' '),
            Trigram('ä', 't', 't'),
            Trigram('n', 'd', 'e'),
            Trigram(' ', 'f', 'ö'),
            Trigram('r', 'ä', 't'),
            Trigram('i', 'l', 'l'),
            Trigram('e', 't', ' '),
            Trigram('a', 'n', 'd'),
            Trigram(' ', 'r', 'ä'),
            Trigram(' ', 'e', 'n'),
            Trigram(' ', 't', 'i'),
            Trigram(' ', 'd', 'e'),
            Trigram('t', 'i', 'l'),
            Trigram('h', 'e', 't'),
            Trigram('l', 'l', ' '),
            Trigram('d', 'e', ' '),
            Trigram('o', 'm', ' '),
            Trigram('v', 'a', 'r'),
            Trigram('l', 'i', 'g'),
            Trigram('g', 'e', 'n'),
            Trigram(' ', 'f', 'r'),
            Trigram('e', 'l', 'l'),
            Trigram('s', 'k', 'a'),
            Trigram('n', 'i', 'n'),
            Trigram('n', 'g', ' '),
            Trigram('t', 'e', 'r'),
            Trigram(' ', 'h', 'a'),
            Trigram('a', 's', ' '),
            Trigram(' ', 'i', 'n'),
            Trigram('k', 'a', ' '),
            Trigram('a', 't', 't'),
            Trigram('l', 'l', 'e'),
            Trigram('d', 'e', 'r'),
            Trigram('s', 'a', 'm'),
            Trigram(' ', 'i', ' '),
            Trigram('u', 'n', 'd'),
            Trigram('l', 'l', 'a'),
            Trigram('g', 'h', 'e'),
            Trigram('f', 'r', 'i'),
            Trigram('a', 'l', 'l'),
            Trigram('e', 'n', 's'),
            Trigram('e', 't', 'e'),
            Trigram('n', 'a', ' '),
            Trigram('l', 'e', 'r'),
            Trigram(' ', 'a', 't'),
            Trigram('ö', 'r', ' '),
            Trigram('d', 'e', 'n'),
            Trigram(' ', 'e', 'l'),
            Trigram('a', 'v', ' '),
            Trigram(' ', 'a', 'v'),
            Trigram(' ', 's', 'o'),
            Trigram('i', 'g', 'h'),
            Trigram('r', ' ', 'h'),
            Trigram('n', 'v', 'a'),
            Trigram('g', 'a', ' '),
            Trigram('r', ' ', 'r'),
            Trigram('e', 'n', 'v'),
            Trigram('l', 'a', ' '),
            Trigram('t', 'i', 'g'),
            Trigram('n', 's', 'k'),
            Trigram('i', 'g', 'a'),
            Trigram('h', 'a', 'r'),
            Trigram('t', ' ', 'a'),
            Trigram('s', 'o', 'm'),
            Trigram('t', 't', 'i'),
            Trigram(' ', 'u', 't'),
            Trigram('i', 'o', 'n'),
            Trigram('t', ' ', 't'),
            Trigram('a', ' ', 's'),
            Trigram('n', 'g', 'e'),
            Trigram('n', 's', ' '),
            Trigram('a', ' ', 'f'),
            Trigram('r', ' ', 's'),
            Trigram('m', 'ä', 'n'),
            Trigram('a', ' ', 'o'),
            Trigram(' ', 's', 'k'),
            Trigram(' ', 's', 'i'),
            Trigram('r', 'n', 'a'),
            Trigram('i', 's', 'k'),
            Trigram('a', 'n', ' '),
            Trigram(' ', 's', 't'),
            Trigram('ä', 'r', ' '),
            Trigram('r', 'a', ' '),
            Trigram(' ', 'v', 'i'),
            Trigram(' ', 'a', 'l'),
            Trigram('t', ' ', 'f'),
            Trigram(' ', 's', 'a'),
            Trigram('a', ' ', 'r'),
            Trigram('a', 't', 'i'),
            Trigram(' ', 'ä', 'r'),
            Trigram(' ', 'm', 'e'),
            Trigram(' ', 'b', 'e'),
            Trigram('n', ' ', 's'),
            Trigram(' ', 'a', 'n'),
            Trigram('t', 'i', 'o'),
            Trigram('n', 'n', 'a'),
            Trigram('l', 'a', 'n'),
            Trigram('e', 'r', 'n'),
            Trigram('t', ' ', 'e'),
            Trigram('m', 'e', 'd'),
            Trigram(' ', 'v', 'a'),
            Trigram('i', 'g', ' '),
            Trigram('ä', 'n', 's'),
            Trigram(' ', 'å', 't'),
            Trigram('s', 't', 'a'),
            Trigram('t', 'a', ' '),
            Trigram('n', 'a', 't'),
            Trigram(' ', 'u', 'n'),
            Trigram('k', 'l', 'i'),
            Trigram('t', 'e', 'n'),
            Trigram(' ', 'g', 'r'),
            Trigram('v', 'i', 's'),
            Trigram('ä', 'l', 'l'),
            Trigram(' ', 'l', 'a'),
            Trigram('o', 'n', 'e'),
            Trigram('h', 'a', 'n'),
            Trigram('ä', 'n', 'd'),
            Trigram('t', ' ', 's'),
            Trigram('s', 't', 'ä'),
            Trigram('t', ' ', 'i'),
            Trigram('n', 'e', 'r'),
            Trigram('a', 'n', 's'),
            Trigram('g', 'r', 'u'),
            Trigram(' ', 'g', 'e'),
            Trigram('v', 'e', 'r'),
            Trigram(' ', 'm', 'å'),
            Trigram(' ', 'l', 'i'),
            Trigram('l', 'i', 'k'),
            Trigram('i', 'h', 'e'),
            Trigram('e', 'r', 's'),
            Trigram('r', 'i', 'h'),
            Trigram('r', ' ', 'a'),
            Trigram(' ', 'r', 'e'),
            Trigram('m', 'å', ' '),
            Trigram('s', 'n', 'i'),
            Trigram('n', ' ', 'f'),
            Trigram('t', ' ', 'o'),
            Trigram(' ', 'm', 'ä'),
            Trigram(' ', 'n', 'a'),
            Trigram('r', ' ', 'e'),
            Trigram('r', 'i', ' '),
            Trigram('a', 'd', ' '),
            Trigram('e', 'n', 't'),
            Trigram('k', 'l', 'a'),
            Trigram('d', 'e', 't'),
            Trigram(' ', 'v', 'ä'),
            Trigram('r', 'u', 'n'),
            Trigram('r', 'k', 'l'),
            Trigram('d', 'a', ' '),
            Trigram('h', ' ', 'r'),
            Trigram('u', 'p', 'p'),
            Trigram('d', 'r', 'a'),
            Trigram('r', 'i', 'n'),
            Trigram('i', 'g', 't'),
            Trigram('d', 'i', 'g'),
            Trigram('n', ' ', 'e'),
            Trigram('e', 'r', 'k'),
            Trigram('k', 'a', 'p'),
            Trigram('t', 't', 'a'),
            Trigram('e', 'd', ' '),
            Trigram('d', ' ', 'f'),
            Trigram('r', 'a', 'n'),
            Trigram('e', ' ', 's'),
            Trigram('t', 'a', 'n'),
            Trigram('u', 't', 'a'),
            Trigram('n', 'o', 'm'),
            Trigram('l', 'a', 'r'),
            Trigram('g', 't', ' '),
            Trigram('s', ' ', 'f'),
            Trigram(' ', 'p', 'å'),
            Trigram(' ', 'o', 'm'),
            Trigram('k', 't', 'e'),
            Trigram('l', 'i', 'n'),
            Trigram('r', ' ', 'u'),
            Trigram('v', 'i', 'd'),
            Trigram('g', ' ', 'o'),
            Trigram('ä', 'n', 'n'),
            Trigram('e', 'r', 'v'),
            Trigram('i', 'k', 'a'),
            Trigram('a', 'r', 'i'),
            Trigram('a', ' ', 'i'),
            Trigram('l', 'a', 'g'),
            Trigram('r', 'v', 'i'),
            Trigram('i', 'd', ' '),
            Trigram('r', ' ', 'o'),
            Trigram('s', ' ', 's'),
            Trigram('v', 'i', 'l'),
            Trigram('r', ' ', 'm'),
            Trigram('ö', 'r', 'k'),
            Trigram('o', 't', ' '),
            Trigram('n', 'd', 'l'),
            Trigram('s', 't', 'r'),
            Trigram('e', 'l', 's'),
            Trigram('r', 'o', ' '),
            Trigram('a', ' ', 'm'),
            Trigram('m', 'o', 't'),
            Trigram(' ', 'm', 'o'),
            Trigram('i', ' ', 'o'),
            Trigram('p', 'å', ' '),
            Trigram('r', ' ', 'd'),
            Trigram('o', 'n', ' '),
            Trigram('d', 'e', 'l'),
            Trigram('i', 's', 'n'),
            Trigram('s', 'k', 'y'),
            Trigram('e', ' ', 'm'),
            Trigram('r', 'a', 's'),
            Trigram(' ', 'h', 'ä'),
            Trigram('r', ' ', 'f'),
            Trigram('i', ' ', 's'),
            Trigram('a', ' ', 'n'),
            Trigram('n', 'a', 'd'),
            Trigram('n', ' ', 'o'),
            Trigram('g', 'a', 'n'),
            Trigram('t', 'n', 'i'),
            Trigram('e', 'r', 'a'),
            Trigram('ä', 'r', 'd'),
            Trigram('a', ' ', 'd'),
            Trigram('t', 'ä', 'l'),
            Trigram('b', 'e', 'r'),
            Trigram('n', 'g', 'a'),
            Trigram('r', ' ', 'i'),
            Trigram('e', 'n', 'n'),
            Trigram('n', 'd', ' '),
            Trigram('n', ' ', 'a'),
            Trigram(' ', 'u', 'p'),
            Trigram('s', 'i', 'n'),
            Trigram('d', 'd', ' '),
            Trigram('ö', 'r', 's'),
            Trigram('j', 'e', ' '),
            Trigram('i', 't', 't'),
            Trigram('k', 'a', 'l'),
            Trigram('n', ' ', 'm'),
            Trigram('a', 'm', 't'),
            Trigram('n', ' ', 'i'),
            Trigram('k', 'i', 'l'),
            Trigram('l', 's', 'e'),
            Trigram('s', 'k', 'i'),
            Trigram('n', 'a', 's'),
            Trigram('e', 'n', 'd'),
            Trigram('s', ' ', 'e'),
            Trigram(' ', 's', 'å'),
            Trigram('i', 'n', 'n'),
            Trigram('t', 'a', 't'),
            Trigram('p', 'e', 'r'),
            Trigram('t', ' ', 'v'),
            Trigram('a', 'r', 'j'),
            Trigram('e', ' ', 'f'),
            Trigram('l', ' ', 'a'),
            Trigram('r', 'e', 'l'),
            Trigram('t', ' ', 'b'),
            Trigram('i', 'n', 't'),
            Trigram('t', 'e', 't'),
            Trigram('g', ' ', 'a'),
            Trigram('ö', 'r', 'a'),
            Trigram('l', ' ', 'v'),
            Trigram('k', 'y', 'd'),
            Trigram('y', 'd', 'd'),
            Trigram('r', 'j', 'e'),
            Trigram(' ', 'f', 'a'),
            Trigram('b', 'e', 't'),
            Trigram('s', 'e', ' '),
            Trigram('t', ' ', 'l'),
            Trigram('l', 'i', 't'),
            Trigram('s', 'a', ' '),
            Trigram('n', 'ä', 'r'),
            Trigram('h', 'ä', 'l'),
            Trigram('l', ' ', 's'),
            Trigram('n', 'd', 'r'),
            Trigram('n', 'i', 's'),
            Trigram('y', 'c', 'k'),
            Trigram('h', ' ', 'a'),
            Trigram('l', 'l', 'm'),
            Trigram('l', 'k', 'e'),
            Trigram('h', ' ', 'f'),
            Trigram('a', 'r', 'b'),
            Trigram('l', 'm', 'ä'),
            Trigram('n', 'd', 'a'),
            Trigram('b', 'a', 'r'),
            Trigram('c', 'k', 'l'),
            Trigram('v', ' ', 's'),
            Trigram('r', 'ä', 'n'),
            Trigram('g', 'a', 'r'),
            Trigram('t', 'r', 'a'),
            Trigram('r', 'e', ' '),
            Trigram('e', 'g', 'e'),
            Trigram('r', ' ', 'g'),
            Trigram('a', 'r', 'a'),
            Trigram('e', 's', 's'),
            Trigram('d', ' ', 'e'),
            Trigram('v', 'ä', 'r'),
            Trigram('m', 't', ' '),
            Trigram('a', 'p', ' '),
        ],
    ),
    (
        Lang::Aka,
        &[
            Trigram('s', 'ɛ', ' '),
            Trigram('a', ' ', 'a'),
            Trigram(' ', 's', 'ɛ'),
            Trigram('n', 'e', ' '),
            Trigram('r', 'a', ' '),
            Trigram('a', ' ', 'n'),
            Trigram(' ', 'w', 'ɔ'),
            Trigram(' ', 'a', ' '),
            Trigram('a', 'r', 'a'),
            Trigram('a', 'n', ' '),
            Trigram('e', 'ɛ', ' '),
            Trigram('n', 'o', ' '),
            Trigram(' ', 'n', 'e'),
            Trigram(' ', 'b', 'i'),
            Trigram(' ', 'n', 'o'),
            Trigram(' ', 'a', 's'),
            Trigram('i', 'a', 'r'),
            Trigram('b', 'i', 'a'),
            Trigram('y', 'ɛ', ' '),
            Trigram('m', 'u', ' '),
            Trigram('a', 'a', ' '),
            Trigram(' ', 'a', 'n'),
            Trigram('ɛ', ' ', 's'),
            Trigram('e', ' ', 'a'),
            Trigram('m', 'a', ' '),
            Trigram(' ', 'h', 'o'),
            Trigram('b', 'i', ' '),
            Trigram('m', 'a', 'n'),
            Trigram('d', 'e', 'ɛ'),
            Trigram(' ', 'm', 'u'),
            Trigram('h', 'o', ' '),
            Trigram('ɛ', ' ', 'a'),
            Trigram('n', 'a', ' '),
            Trigram('a', ' ', 'ɛ'),
            Trigram(' ', 'o', 'b'),
            Trigram('o', 'b', 'i'),
            Trigram('e', ' ', 'n'),
            Trigram('a', ' ', 'b'),
            Trigram('n', ' ', 'a'),
            Trigram('s', 'o', ' '),
            Trigram('o', ' ', 'n'),
            Trigram('p', 'a', ' '),
            Trigram('a', 'm', 'a'),
            Trigram('ɛ', ' ', 'o'),
            Trigram('o', ' ', 'a'),
            Trigram('i', 'p', 'a'),
            Trigram('n', 'i', 'p'),
            Trigram('ɛ', ' ', 'n'),
            Trigram('n', 'a', 'a'),
            Trigram(' ', 'n', 'a'),
            Trigram('a', ' ', 'w'),
            Trigram('a', 'n', 'a'),
            Trigram(' ', 's', 'o'),
            Trigram(' ', 'a', 'd'),
            Trigram(' ', 'n', 'n'),
            Trigram('ɛ', ' ', 'ɔ'),
            Trigram('ɛ', 'd', 'e'),
            Trigram('a', 's', 'ɛ'),
            Trigram('k', 'w', 'a'),
            Trigram(' ', 'o', 'n'),
            Trigram('o', 'n', 'i'),
            Trigram('w', 'a', 'n'),
            Trigram(' ', 'a', 'm'),
            Trigram('a', ' ', 'ɔ'),
            Trigram('s', 'ɛ', 'd'),
            Trigram('w', 'ɔ', ' '),
            Trigram(' ', 'a', 'h'),
            Trigram('ɛ', 'y', 'ɛ'),
            Trigram(' ', 'n', 'y'),
            Trigram('o', 'ɔ', ' '),
            Trigram(' ', 'n', ' '),
            Trigram('m', 'm', 'a'),
            Trigram('i', ' ', 'a'),
            Trigram(' ', 'm', 'm'),
            Trigram('n', 'n', 'i'),
            Trigram(' ', 'k', 'w'),
            Trigram('i', 'e', ' '),
            Trigram('w', 'ɔ', 'n'),
            Trigram('ɛ', ' ', 'w'),
            Trigram('d', 'e', ' '),
            Trigram(' ', 'ɛ', 'y'),
            Trigram(' ', 'b', 'a'),
            Trigram('a', 's', 'e'),
            Trigram('ɔ', ' ', 'n'),
            Trigram('o', ' ', 'b'),
            Trigram('i', ' ', 'm'),
            Trigram('ɔ', ' ', 'a'),
            Trigram('u', 'o', ' '),
            Trigram('n', ' ', 'n'),
            Trigram('a', ' ', 'm'),
            Trigram('o', ' ', 's'),
            Trigram('i', 'r', 'i'),
            Trigram(' ', 'y', 'i'),
            Trigram('n', 'i', ' '),
            Trigram('e', ' ', 's'),
            Trigram('n', 'y', 'i'),
            Trigram('d', 'i', ' '),
            Trigram('u', ' ', 'n'),
            Trigram('a', ' ', 'o'),
            Trigram('a', 'h', 'o'),
            Trigram(' ', 'd', 'e'),
            Trigram('t', 'u', 'm'),
            Trigram(' ', 'ɛ', 'n'),
            Trigram('ɔ', 'n', ' '),
            Trigram('n', 'y', 'a'),
            Trigram('i', ' ', 'n'),
            Trigram('ɔ', 'm', 'a'),
            Trigram('e', ' ', 'm'),
            Trigram('a', 'd', 'w'),
            Trigram(' ', 'y', 'ɛ'),
            Trigram('u', 'm', 'i'),
            Trigram('d', 'i', 'e'),
            Trigram('m', 'i', ' '),
            Trigram('ɛ', ' ', 'ɛ'),
            Trigram('o', ' ', 'k'),
            Trigram(' ', 'a', 'b'),
            Trigram('ɛ', 'm', ' '),
            Trigram('a', ' ', 's'),
            Trigram(' ', 'm', 'a'),
            Trigram('n', 'a', 'm'),
            Trigram(' ', 'ɔ', 'm'),
            Trigram(' ', 'ɛ', 's'),
            Trigram('y', 'i', 'n'),
            Trigram(' ', 'a', 't'),
            Trigram(' ', 'b', 'ɔ'),
            Trigram('o', ' ', 'd'),
            Trigram('i', 'n', 'a'),
            Trigram('p', 'ɛ', ' '),
            Trigram('s', 'ɛ', 'm'),
            Trigram('u', 'a', ' '),
            Trigram('n', ' ', 's'),
            Trigram('b', 'ɔ', ' '),
            Trigram('a', 'd', 'i'),
            Trigram('y', 'a', ' '),
            Trigram('e', ' ', 'h'),
            Trigram('a', 's', 'o'),
            Trigram('m', 'a', 'r'),
            Trigram('a', 'n', 'i'),
            Trigram('k', 'u', 'o'),
            Trigram('r', 'ɛ', ' '),
            Trigram('f', 'a', ' '),
            Trigram('a', ' ', 'k'),
            Trigram('ɔ', 'd', 'e'),
            Trigram('a', ' ', 'h'),
            Trigram('b', 'a', ' '),
            Trigram('n', ' ', 'b'),
            Trigram('r', 'e', ' '),
            Trigram('u', 'm', 'a'),
            Trigram('w', 'u', 'm'),
            Trigram('o', 'm', ' '),
            Trigram('ɔ', ' ', 'h'),
            Trigram('m', ' ', 'n'),
            Trigram('y', 'i', ' '),
            Trigram('u', ' ', 'a'),
            Trigram(' ', 's', 'a'),
            Trigram('s', 'e', ' '),
            Trigram('d', 'w', 'u'),
            Trigram('ɔ', ' ', 'b'),
            Trigram(' ', 'n', 't'),
            Trigram('m', ' ', 'a'),
            Trigram('e', 'r', 'ɛ'),
            Trigram(' ', 'k', 'ɔ'),
            Trigram('a', ' ', 'y'),
            Trigram('o', 'r', 'ɔ'),
            Trigram(' ', 'n', 'k'),
            Trigram(' ', 'b', 'ɛ'),
            Trigram(' ', 'ɔ', 'd'),
            Trigram('t', 'e', 'n'),
            Trigram('r', 'ɔ', ' '),
            Trigram('h', 'y', 'ɛ'),
            Trigram('s', 'a', 'a'),
            Trigram('k', 'a', ' '),
            Trigram('ɛ', ' ', 'b'),
            Trigram('e', ' ', 'b'),
            Trigram('i', ' ', 's'),
            Trigram('a', 'd', 'e'),
            Trigram('a', 'm', ' '),
            Trigram('n', 'k', 'a'),
            Trigram('k', 'o', 'r'),
            Trigram('i', ' ', 'ɛ'),
            Trigram('e', 'n', 'e'),
            Trigram('e', 'n', 'a'),
            Trigram(' ', 'n', 's'),
            Trigram('b', 'a', 'n'),
            Trigram('ɛ', 'n', 's'),
            Trigram(' ', 'k', 'u'),
            Trigram('ɛ', 's', 'ɛ'),
            Trigram('a', 'n', 'e'),
            Trigram('n', 's', 'ɛ'),
            Trigram('f', 'o', 'f'),
            Trigram('ɛ', 'ɛ', ' '),
            Trigram(' ', 'f', 'i'),
            Trigram('g', 'y', 'e'),
            Trigram('ɔ', 't', 'u'),
            Trigram(' ', 'd', 'i'),
            Trigram('a', 'n', 'o'),
            Trigram('i', ' ', 'k'),
            Trigram('o', ' ', 'm'),
            Trigram(' ', 'ɔ', 't'),
            Trigram(' ', 'k', 'o'),
            Trigram('y', 'ɛ', 'ɛ'),
            Trigram('b', 'i', 'r'),
            Trigram(' ', 'a', 'k'),
            Trigram('i', 'm', ' '),
            Trigram('k', 'y', 'e'),
            Trigram(' ', 'p', 'ɛ'),
            Trigram('a', ' ', 'd'),
            Trigram('y', 'i', 'e'),
            Trigram('k', 'o', ' '),
            Trigram('n', 't', 'i'),
            Trigram('i', ' ', 'b'),
            Trigram('e', 't', 'e'),
            Trigram('o', 'f', 'o'),
            Trigram('a', 'm', 'm'),
            Trigram('y', 'e', ' '),
            Trigram('r', 'i', ' '),
            Trigram('f', 'o', 'ɔ'),
            Trigram('k', 'ɔ', ' '),
            Trigram('b', 'o', 'm'),
            Trigram('a', 'b', 'o'),
            Trigram('ɔ', ' ', 's'),
            Trigram('ɔ', 'n', 'e'),
            Trigram(' ', 'ɛ', 'b'),
            Trigram('s', 'o', 'ɔ'),
            Trigram('f', 'o', 'r'),
            Trigram('i', 's', 'ɛ'),
            Trigram('m', ' ', 'k'),
            Trigram('a', 's', 'a'),
            Trigram('n', 'o', 'd'),
            Trigram('ɛ', ' ', 'm'),
            Trigram('f', 'i', 'r'),
            Trigram('t', 'i', ' '),
            Trigram(' ', 'd', 'a'),
            Trigram('e', ' ', 'y'),
            Trigram('s', 'u', 'a'),
            Trigram(' ', 'b', 'e'),
            Trigram('n', 'i', 'i'),
            Trigram('s', 'e', 'ɛ'),
            Trigram('w', 'a', ' '),
            Trigram('b', 'e', 'r'),
            Trigram(' ', 'a', 'w'),
            Trigram('d', 'w', 'e'),
            Trigram('n', ' ', 'f'),
            Trigram(' ', 'f', 'o'),
            Trigram('o', ' ', 'ɛ'),
            Trigram('i', ' ', 'h'),
            Trigram('u', ' ', 'b'),
            Trigram('ɔ', ' ', 'm'),
            Trigram(' ', 'm', 'f'),
            Trigram('h', 'ɔ', ' '),
            Trigram('k', 'a', 'b'),
            Trigram('w', 'ɛ', ' '),
            Trigram('t', 'o', ' '),
            Trigram('r', 'i', 'b'),
            Trigram('h', 'w', 'ɛ'),
            Trigram('i', 'b', 'i'),
            Trigram(' ', 'd', 'w'),
            Trigram('d', 'i', 's'),
            Trigram('n', 's', 'o'),
            Trigram('a', 'n', 's'),
            Trigram('t', 'i', 'r'),
            Trigram('u', ' ', 'ɛ'),
            Trigram(' ', 't', 'i'),
            Trigram(' ', 'h', 'ɔ'),
            Trigram('s', 'a', ' '),
            Trigram('e', ' ', 'o'),
            Trigram(' ', 't', 'u'),
            Trigram('o', 'd', 'i'),
            Trigram('ɛ', ' ', 'y'),
            Trigram('i', 'a', ' '),
            Trigram('o', 'f', 'a'),
            Trigram(' ', 'ɔ', 'n'),
            Trigram('o', ' ', 'w'),
            Trigram('ɛ', 'b', 'ɛ'),
            Trigram('a', 'b', 'a'),
            Trigram(' ', 'k', 'a'),
            Trigram('i', 'i', ' '),
            Trigram('w', 'e', 'n'),
            Trigram('ɛ', 's', 'i'),
            Trigram('m', ' ', 'm'),
            Trigram('s', 'i', 'a'),
            Trigram('a', 'd', 'a'),
            Trigram('y', 'e', 'r'),
            Trigram('i', 'a', 'n'),
            Trigram('d', 'a', ' '),
            Trigram('s', 'e', 't'),
            Trigram(' ', 'g', 'y'),
            Trigram('d', 'u', 'a'),
            Trigram('i', ' ', 'd'),
            Trigram('s', 'o', 'm'),
            Trigram('m', 'f', 'a'),
            Trigram('ɔ', ' ', 'w'),
            Trigram(' ', 'a', 'f'),
            Trigram('i', ' ', 'y'),
            Trigram('a', 'n', 'y'),
            Trigram('o', 'r', 'a'),
            Trigram('r', 'i', 'm'),
            Trigram('w', 'ɔ', 'd'),
            Trigram('d', 'w', 'a'),
            Trigram('n', 's', 'i'),
        ],
    ),
    (
        Lang::Sna,
        &[
            Trigram('w', 'a', ' '),
            Trigram('a', ' ', 'k'),
            Trigram('a', 'n', 'a'),
            Trigram('r', 'o', ' '),
            Trigram('n', 'a', ' '),
            Trigram(' ', 'k', 'u'),
            Trigram(' ', 'm', 'u'),
            Trigram('n', 'h', 'u'),
            Trigram('d', 'z', 'e'),
            Trigram('h', 'u', ' '),
            Trigram('a', ' ', 'm'),
            Trigram(' ', 'z', 'v'),
            Trigram('m', 'u', 'n'),
            Trigram('o', 'k', 'u'),
            Trigram('c', 'h', 'i'),
            Trigram('a', ' ', 'n'),
            Trigram('a', 'k', 'a'),
            Trigram('d', 'z', 'i'),
            Trigram('k', 'a', ' '),
            Trigram('z', 'e', 'r'),
            Trigram('e', 'r', 'o'),
            Trigram(' ', 'c', 'h'),
            Trigram('c', 'h', 'e'),
            Trigram('s', 'e', ' '),
            Trigram('u', 'n', 'h'),
            Trigram('o', 'd', 'z'),
            Trigram('r', 'w', 'a'),
            Trigram('r', 'a', ' '),
            Trigram('k', 'o', 'd'),
            Trigram('z', 'v', 'i'),
            Trigram(' ', 'n', 'e'),
            Trigram(' ', 'p', 'a'),
            Trigram('k', 'a', 'n'),
            Trigram(' ', 'w', 'e'),
            Trigram(' ', 'd', 'z'),
            Trigram(' ', 'n', 'o'),
            Trigram('i', 'k', 'a'),
            Trigram('v', 'a', ' '),
            Trigram('i', 'r', 'i'),
            Trigram(' ', 'a', 'n'),
            Trigram('k', 'u', 't'),
            Trigram('n', 'y', 'i'),
            Trigram('o', ' ', 'y'),
            Trigram('y', 'i', 'k'),
            Trigram('v', 'a', 'n'),
            Trigram('n', 'e', 'k'),
            Trigram('e', 's', 'e'),
            Trigram('e', 'k', 'o'),
            Trigram('z', 'v', 'a'),
            Trigram('i', 'd', 'z'),
            Trigram('e', ' ', 'a'),
            Trigram(' ', 'k', 'a'),
            Trigram('a', 'n', 'e'),
            Trigram('a', 'n', 'o'),
            Trigram('n', 'g', 'u'),
            Trigram('e', 'k', 'u'),
            Trigram('c', 'h', 'a'),
            Trigram('u', 'n', 'g'),
            Trigram(' ', 'y', 'o'),
            Trigram('r', 'i', ' '),
            Trigram('a', 'k', 'e'),
            Trigram('k', 'e', ' '),
            Trigram('a', 'c', 'h'),
            Trigram('u', 'd', 'z'),
            Trigram('i', 'r', 'o'),
            Trigram('a', ' ', 'z'),
            Trigram('u', ' ', 'w'),
            Trigram(' ', 'v', 'a'),
            Trigram('i', 'r', 'a'),
            Trigram('w', 'e', 's'),
            Trigram('a', 'n', 'g'),
            Trigram('e', 'c', 'h'),
            Trigram('n', 'g', 'e'),
            Trigram('i', ' ', 'p'),
            Trigram('e', 'n', 'g'),
            Trigram('y', 'o', 'k'),
            Trigram('n', 'o', 'k'),
            Trigram('e', 'd', 'z'),
            Trigram('o', ' ', 'i'),
            Trigram('i', 'r', 'w'),
            Trigram('a', 'n', 'i'),
            Trigram('i', 'n', 'o'),
            Trigram('u', 'v', 'a'),
            Trigram('i', 'c', 'h'),
            Trigram('n', 'g', 'a'),
            Trigram('t', 'i', ' '),
            Trigram('z', 'i', 'r'),
            Trigram('a', 'n', 'h'),
            Trigram('r', 'i', 'r'),
            Trigram('k', 'o', ' '),
            Trigram('d', 'z', 'a'),
            Trigram('o', ' ', 'n'),
            Trigram('w', 'a', 'n'),
            Trigram('w', 'o', ' '),
            Trigram('t', 'a', 'n'),
            Trigram('s', 'u', 'n'),
            Trigram('i', 'p', 'i'),
            Trigram('d', 'z', 'w'),
            Trigram('e', 'n', 'y'),
            Trigram('a', 's', 'i'),
            Trigram('h', 'e', 'n'),
            Trigram('z', 'v', 'e'),
            Trigram('k', 'u', 'r'),
            Trigram('v', 'a', 'k'),
            Trigram('a', ' ', 'p'),
            Trigram('s', 'h', 'a'),
            Trigram('u', 'n', 'u'),
            Trigram('z', 'w', 'a'),
            Trigram('i', 't', 'a'),
            Trigram('k', 'w', 'a'),
            Trigram('e', ' ', 'k'),
            Trigram('r', 'u', 'd'),
            Trigram('n', 'u', 'n'),
            Trigram('u', 'r', 'u'),
            Trigram('g', 'u', 'k'),
            Trigram('a', ' ', 'c'),
            Trigram('a', ' ', 'd'),
            Trigram(' ', 'y', 'a'),
            Trigram('a', ' ', 'y'),
            Trigram('b', 'a', 't'),
            Trigram('p', 'a', 's'),
            Trigram('e', 'z', 'v'),
            Trigram('t', 'a', ' '),
            Trigram('e', ' ', 'n'),
            Trigram('u', 't', 'i'),
            Trigram(' ', 'k', 'w'),
            Trigram('o', ' ', 'k'),
            Trigram('o', ' ', 'c'),
            Trigram('o', ' ', 'm'),
            Trigram('a', 'r', 'a'),
            Trigram(' ', 'm', 'a'),
            Trigram('s', 'i', ' '),
            Trigram('g', 'a', ' '),
            Trigram('u', 'k', 'o'),
            Trigram('a', 't', 'a'),
            Trigram('o', 's', 'e'),
            Trigram('e', 'm', 'a'),
            Trigram('d', 'z', 'o'),
            Trigram('u', 'c', 'h'),
            Trigram('h', 'i', 'p'),
            Trigram('k', 'u', 'v'),
            Trigram('n', 'o', ' '),
            Trigram('r', 'u', 's'),
            Trigram('h', 'e', 'c'),
            Trigram('o', 'm', 'u'),
            Trigram('i', ' ', 'z'),
            Trigram('w', 'a', 'k'),
            Trigram('o', ' ', 'r'),
            Trigram('k', 'u', 's'),
            Trigram('k', 'w', 'e'),
            Trigram('e', 'r', 'e'),
            Trigram('r', 'e', ' '),
            Trigram(' ', 'r', 'w'),
            Trigram(' ', 'p', 'o'),
            Trigram('o', ' ', 'a'),
            Trigram('m', 'w', 'e'),
            Trigram('y', 'a', 'k'),
            Trigram('m', 'o', ' '),
            Trigram('u', 's', 'u'),
            Trigram('i', 's', 'i'),
            Trigram('z', 'a', ' '),
            Trigram('s', 'a', ' '),
            Trigram('e', ' ', 'z'),
            Trigram('u', 't', 'a'),
            Trigram('g', 'a', 'r'),
            Trigram(' ', 'i', 'n'),
            Trigram('h', 'i', 'n'),
            Trigram('n', 'e', 'm'),
            Trigram('p', 'a', 'c'),
            Trigram('k', 'u', 'c'),
            Trigram('w', 'e', ' '),
            Trigram('e', 't', 'e'),
            Trigram(' ', 'y', 'e'),
            Trigram('t', 'w', 'a'),
            Trigram('p', 'o', 's'),
            Trigram('o', ' ', 'd'),
            Trigram('a', ' ', 'i'),
            Trigram('h', 'u', 'r'),
            Trigram('g', 'e', 't'),
            Trigram('a', 'r', 'i'),
            Trigram('o', 'n', 'g'),
            Trigram('p', 'a', 'n'),
            Trigram('e', 'r', 'w'),
            Trigram('u', 'k', 'a'),
            Trigram('r', 'w', 'o'),
            Trigram('v', 'o', ' '),
            Trigram(' ', 'a', 'k'),
            Trigram('t', 'e', 'm'),
            Trigram('z', 'o', ' '),
            Trigram('e', 'm', 'u'),
            Trigram('e', 'm', 'o'),
            Trigram('o', 'r', 'u'),
            Trigram(' ', 'h', 'a'),
            Trigram('u', 'i', 't'),
            Trigram('w', 'e', 'n'),
            Trigram('u', 'y', 'e'),
            Trigram('k', 'u', 'i'),
            Trigram(' ', 'u', 'y'),
            Trigram('v', 'i', 'n'),
            Trigram('h', 'a', 'k'),
            Trigram('k', 'u', 'b'),
            Trigram('i', ' ', 'm'),
            Trigram('a', ' ', 'a'),
            Trigram('k', 'u', 'd'),
            Trigram(' ', 's', 'e'),
            Trigram(' ', 'k', 'o'),
            Trigram('y', 'o', ' '),
            Trigram('a', 'n', 'd'),
            Trigram('d', 'a', ' '),
            Trigram('n', 'o', 'r'),
            Trigram('s', 'i', 'n'),
            Trigram('u', 'b', 'a'),
            Trigram('a', ' ', 's'),
            Trigram('a', ' ', 'u'),
            Trigram(' ', 'i', 'c'),
            Trigram('z', 'v', 'o'),
            Trigram('m', 'u', 't'),
            Trigram('m', 'a', 't'),
            Trigram('n', 'e', 'z'),
            Trigram('e', ' ', 'm'),
            Trigram('a', ' ', 'w'),
            Trigram('a', 'd', 'z'),
            Trigram('u', 'r', 'a'),
            Trigram('e', 'v', 'a'),
            Trigram('a', 'v', 'a'),
            Trigram('p', 'i', ' '),
            Trigram('a', ' ', 'r'),
            Trigram('e', 'r', 'a'),
            Trigram('u', 't', 'e'),
            Trigram('o', 'k', 'o'),
            Trigram('v', 'i', 's'),
            Trigram(' ', 'i', 'y'),
            Trigram('h', 'a', ' '),
            Trigram('u', ' ', 'a'),
            Trigram('h', 'a', 'n'),
            Trigram('c', 'h', 'o'),
            Trigram('a', 'r', 'u'),
            Trigram('a', 's', 'a'),
            Trigram('f', 'a', 'n'),
            Trigram('a', 'a', 'n'),
            Trigram('p', 'i', 'r'),
            Trigram('i', 'n', 'a'),
            Trigram('g', 'u', 'v'),
            Trigram('u', 's', 'h'),
            Trigram('t', 'o', 'n'),
            Trigram(' ', 'h', 'u'),
            Trigram('u', 'n', 'y'),
            Trigram('e', 'n', 'z'),
            Trigram('r', 'a', 'n'),
            Trigram('y', 'o', 'r'),
            Trigram('t', 'e', 'd'),
            Trigram('a', 'i', 't'),
            Trigram('h', 'e', 'k'),
            Trigram(' ', 'n', 'y'),
            Trigram('u', 'r', 'i'),
            Trigram('h', 'o', 'k'),
            Trigram('n', 'e', 'n'),
            Trigram('o', 's', 'h'),
            Trigram(' ', 'a', 'c'),
            Trigram('n', 'g', 'i'),
            Trigram('m', 'u', 'k'),
            Trigram('n', 'g', 'o'),
            Trigram('o', ' ', 'z'),
            Trigram('a', 'z', 'v'),
            Trigram('k', 'u', 'n'),
            Trigram('n', 'i', 'd'),
            Trigram('u', 'm', 'a'),
            Trigram('i', ' ', 'h'),
            Trigram('v', 'e', 'm'),
            Trigram('a', ' ', 'h'),
            Trigram('m', 'i', 'r'),
            Trigram('u', 's', 'a'),
            Trigram('o', ' ', 'p'),
            Trigram('i', ' ', 'n'),
            Trigram('a', ' ', 'v'),
            Trigram('i', ' ', 'k'),
            Trigram('a', 'm', 'b'),
            Trigram('z', 'a', 'n'),
            Trigram('n', 'z', 'a'),
            Trigram('k', 'u', 'z'),
            Trigram('z', 'i', ' '),
            Trigram('k', 'a', 'k'),
            Trigram('i', 'n', 'g'),
            Trigram('u', ' ', 'v'),
            Trigram('n', 'g', 'w'),
            Trigram('m', 'u', 'm'),
            Trigram('m', 'b', 'a'),
            Trigram('n', 'i', 'r'),
            Trigram('s', 'a', 'r'),
            Trigram('e', 'w', 'o'),
            Trigram('e', ' ', 'p'),
            Trigram('u', 'w', 'a'),
            Trigram('v', 'i', 'c'),
            Trigram('i', ' ', 'i'),
            Trigram('g', 'w', 'a'),
            Trigram('a', 'g', 'a'),
            Trigram('a', 'm', 'a'),
            Trigram('g', 'o', ' '),
            Trigram('y', 'e', 'w'),
            Trigram('p', 'a', 'm'),
        ],
    ),
    (
        Lang::Afr,
        &[
            Trigram('i', 'e', ' '),
            Trigram('d', 'i', 'e'),
            Trigram('e', 'n', ' '),
            Trigram(' ', 'd', 'i'),
            Trigram(' ', 'e', 'n'),
            Trigram('a', 'n', ' '),
            Trigram('i', 'n', 'g'),
            Trigram('n', 'g', ' '),
            Trigram('v', 'a', 'n'),
            Trigram(' ', 'v', 'a'),
            Trigram('t', 'e', ' '),
            Trigram('e', ' ', 'v'),
            Trigram('r', 'e', 'g'),
            Trigram(' ', 'r', 'e'),
            Trigram('n', ' ', 'd'),
            Trigram(' ', 'g', 'e'),
            Trigram('e', 'n', 's'),
            Trigram('e', 't', ' '),
            Trigram('e', ' ', 'r'),
            Trigram('e', ' ', 'e'),
            Trigram(' ', 't', 'e'),
            Trigram(' ', 'b', 'e'),
            Trigram('l', 'e', ' '),
            Trigram('v', 'e', 'r'),
            Trigram('e', 'e', 'n'),
            Trigram(' ', 'i', 'n'),
            Trigram('k', 'e', ' '),
            Trigram(' ', 'v', 'e'),
            Trigram(' ', 'h', 'e'),
            Trigram('e', 'g', ' '),
            Trigram('h', 'e', 't'),
            Trigram('l', 'k', 'e'),
            Trigram('l', 'i', 'k'),
            Trigram('n', ' ', 'h'),
            Trigram('d', 'e', ' '),
            Trigram('n', 'i', 'e'),
            Trigram('a', 'a', 'n'),
            Trigram('t', ' ', 'd'),
            Trigram('i', 'd', ' '),
            Trigram('m', 'e', 'n'),
            Trigram(' ', 'v', 'r'),
            Trigram('n', 'd', 'e'),
            Trigram('e', 'i', 'd'),
            Trigram('e', ' ', 'o'),
            Trigram(' ', 'a', 'a'),
            Trigram('i', 'n', ' '),
            Trigram('o', 'f', ' '),
            Trigram('d', 'e', 'r'),
            Trigram('h', 'e', 'i'),
            Trigram('o', 'm', ' '),
            Trigram('g', ' ', 'v'),
            Trigram(' ', 'o', 'p'),
            Trigram(' ', 'n', 'i'),
            Trigram('e', ' ', 'b'),
            Trigram(' ', 'e', 'l'),
            Trigram('a', 'l', ' '),
            Trigram('a', 'n', 'd'),
            Trigram('e', 'l', 'k'),
            Trigram('e', 'r', ' '),
            Trigram(' ', 'm', 'e'),
            Trigram('o', 'r', 'd'),
            Trigram('e', ' ', 'w'),
            Trigram('g', ' ', 't'),
            Trigram(' ', 't', 'o'),
            Trigram(' ', 'o', 'f'),
            Trigram('e', 'r', 's'),
            Trigram(' ', 'w', 'e'),
            Trigram(' ', 's', 'a'),
            Trigram(' ', 'v', 'o'),
            Trigram('o', 't', ' '),
            Trigram('e', 'r', 'k'),
            Trigram('n', ' ', 'v'),
            Trigram('v', 'r', 'y'),
            Trigram('g', 'e', ' '),
            Trigram('k', 'e', 'e'),
            Trigram('a', 's', 'i'),
            Trigram('t', 'o', 't'),
            Trigram(' ', 'w', 'a'),
            Trigram('s', 'i', 'e'),
            Trigram('e', 'r', 'e'),
            Trigram(' ', 'o', 'm'),
            Trigram('a', 'a', 'r'),
            Trigram('s', 'a', 'l'),
            Trigram('d', 'i', 'g'),
            Trigram('w', 'o', 'r'),
            Trigram('e', 'g', 't'),
            Trigram('g', 't', 'e'),
            Trigram('r', 'd', 'i'),
            Trigram('r', 'd', ' '),
            Trigram('a', 't', ' '),
            Trigram('n', 'd', ' '),
            Trigram('e', ' ', 's'),
            Trigram('e', 'd', 'e'),
            Trigram('i', 'g', 'e'),
            Trigram(' ', 'd', 'e'),
            Trigram(' ', '’', 'n'),
            Trigram('n', ' ', 'a'),
            Trigram('e', 'n', 'i'),
            Trigram(' ', 'w', 'o'),
            Trigram('e', ' ', 'g'),
            Trigram(' ', 'o', 'n'),
            Trigram('n', ' ', 's'),
            Trigram('’', 'n', ' '),
            Trigram('e', ' ', 't'),
            Trigram('e', 'r', 'd'),
            Trigram('n', 's', ' '),
            Trigram('o', 'o', 'r'),
            Trigram('b', 'e', 's'),
            Trigram('o', 'n', 'd'),
            Trigram('s', 'e', ' '),
            Trigram('s', 'k', 'a'),
            Trigram('a', 'a', 'k'),
            Trigram('n', 'i', 'g'),
            Trigram('l', 'l', 'e'),
            Trigram('y', 'h', 'e'),
            Trigram('r', 'y', 'h'),
            Trigram('i', 's', ' '),
            Trigram('e', 'l', 'i'),
            Trigram('e', 's', 'k'),
            Trigram('i', 'e', 'n'),
            Trigram('s', 't', 'a'),
            Trigram('v', 'o', 'l'),
            Trigram('e', 'l', 'e'),
            Trigram('e', ' ', 'm'),
            Trigram(' ', 'v', 'i'),
            Trigram('i', 'k', ' '),
            Trigram('r', ' ', 'd'),
            Trigram('v', 'i', 'r'),
            Trigram('e', 'd', 'i'),
            Trigram('k', 'a', 'p'),
            Trigram('g', ' ', 'e'),
            Trigram('i', 'r', ' '),
            Trigram('e', 's', ' '),
            Trigram('s', 'y', ' '),
            Trigram('a', 'n', 'g'),
            Trigram('d', 'i', 'n'),
            Trigram(' ', 's', 't'),
            Trigram('e', 'w', 'e'),
            Trigram('g', 'e', 'm'),
            Trigram('g', 'e', 'l'),
            Trigram('g', ' ', 'o'),
            Trigram(' ', 'i', 's'),
            Trigram('e', 'l', ' '),
            Trigram('e', ' ', 'i'),
            Trigram('o', 'p', ' '),
            Trigram('k', 'e', 'r'),
            Trigram('a', 'k', ' '),
            Trigram('u', 'i', 't'),
            Trigram('i', 'k', 'e'),
            Trigram('n', 's', 'e'),
            Trigram('h', 'i', 'e'),
            Trigram('u', 'r', ' '),
            Trigram('e', 'u', 'r'),
            Trigram(' ', 'a', 'l'),
            Trigram('e', ' ', 'a'),
            Trigram('n', 'a', 's'),
            Trigram('e', ' ', 'n'),
            Trigram('n', 'g', 'e'),
            Trigram('i', 'e', 'r'),
            Trigram('n', ' ', 'o'),
            Trigram('w', 'e', 'r'),
            Trigram('e', ' ', 'd'),
            Trigram('a', 'p', ' '),
            Trigram(' ', 'h', 'u'),
            Trigram('a', 'l', 'e'),
            Trigram('r', 'i', 'n'),
            Trigram(' ', 'h', 'i'),
            Trigram('e', 'm', 'e'),
            Trigram('d', 'e', 'u'),
            Trigram('m', 'i', 'n'),
            Trigram('w', 'a', 't'),
            Trigram('n', ' ', 'e'),
            Trigram('s', ' ', 'o'),
            Trigram(' ', 'a', 's'),
            Trigram(' ', 's', 'o'),
            Trigram('a', 's', ' '),
            Trigram('e', ' ', 'h'),
            Trigram('d', 'e', 'l'),
            Trigram('d', ' ', 'v'),
            Trigram('t', 'e', 'r'),
            Trigram('t', 'e', 'n'),
            Trigram('g', 'i', 'n'),
            Trigram('e', 'n', 'd'),
            Trigram('k', 'i', 'n'),
            Trigram('i', 't', ' '),
            Trigram(' ', 'd', 'a'),
            Trigram(' ', 's', 'y'),
            Trigram('p', 'e', 'r'),
            Trigram('r', 'e', ' '),
            Trigram('n', ' ', 'w'),
            Trigram('g', 'e', 's'),
            Trigram('w', 'e', 't'),
            Trigram('g', 'e', 'r'),
            Trigram('e', ' ', 'k'),
            Trigram('o', 'e', 'd'),
            Trigram('s', ' ', 'v'),
            Trigram('n', 't', 'e'),
            Trigram('s', ' ', 'e'),
            Trigram('o', 'n', 'a'),
            Trigram('n', 'a', 'l'),
            Trigram('w', 'a', 'a'),
            Trigram('d', ' ', 't'),
            Trigram('e', 'e', 's'),
            Trigram('s', 'o', 'o'),
            Trigram(' ', 'm', 'a'),
            Trigram('d', ' ', 's'),
            Trigram('i', 'e', 's'),
            Trigram('t', 'e', 'l'),
            Trigram('e', 'm', 'a'),
            Trigram('d', ' ', 'e'),
            Trigram('r', 'e', 'd'),
            Trigram('i', 't', 'e'),
            Trigram(' ', 'n', 'a'),
            Trigram('s', 'k', 'e'),
            Trigram('e', 'l', 'y'),
            Trigram('l', 'y', 'k'),
            Trigram('r', 'e', 'n'),
            Trigram('n', 's', 'k'),
            Trigram('d', ' ', 'o'),
            Trigram('o', 'o', 'n'),
            Trigram('t', ' ', 'e'),
            Trigram('e', 'k', 'e'),
            Trigram('e', 's', 'i'),
            Trigram('e', 's', 'e'),
            Trigram('e', 'r', 'i'),
            Trigram('h', 'u', 'l'),
            Trigram(' ', 'g', 'r'),
            Trigram('i', 'g', ' '),
            Trigram('s', 'i', 'o'),
            Trigram('m', 'a', 'n'),
            Trigram('r', 'd', 'e'),
            Trigram('i', 'o', 'n'),
            Trigram('n', ' ', 'b'),
            Trigram('n', ' ', 'g'),
            Trigram('v', 'o', 'o'),
            Trigram('h', 'e', 'd'),
            Trigram('i', 'n', 'd'),
            Trigram('t', 'e', 'e'),
            Trigram(' ', 'p', 'e'),
            Trigram('r', 's', 'o'),
            Trigram('t', ' ', 'v'),
            Trigram('s', ' ', 'd'),
            Trigram('a', 'l', 'l'),
            Trigram('n', ' ', 't'),
            Trigram('r', 's', 'e'),
            Trigram('n', ' ', 'i'),
            Trigram('e', 'e', 'm'),
            Trigram('d', ' ', 'w'),
            Trigram('o', 'r', 't'),
            Trigram('n', 'd', 'i'),
            Trigram('d', 'a', 'a'),
            Trigram('m', 'a', 'a'),
            Trigram('t', ' ', 'g'),
            Trigram('e', 'r', 'm'),
            Trigram('o', 'n', 't'),
            Trigram('e', 'n', 't'),
            Trigram('a', 'n', 's'),
            Trigram('a', 'm', 'e'),
            Trigram('y', 'k', 'e'),
            Trigram('a', 'r', 'i'),
            Trigram('n', ' ', 'm'),
            Trigram('l', 'a', 'n'),
            Trigram('v', 'o', 'e'),
            Trigram('n', ' ', '’'),
            Trigram('n', 'l', 'i'),
            Trigram('r', 'k', 'l'),
            Trigram('r', ' ', 'm'),
            Trigram('s', 'i', 'a'),
            Trigram('o', 'd', 's'),
            Trigram('a', 'r', 'd'),
            Trigram('i', 'e', 'm'),
            Trigram('g', ' ', 's'),
            Trigram('w', 'e', 'e'),
            Trigram('r', ' ', 'e'),
            Trigram('l', ' ', 'g'),
            Trigram('t', 'a', 'a'),
            Trigram('s', 'e', 'k'),
            Trigram('b', 'a', 'r'),
            Trigram('g', 't', 'i'),
            Trigram('n', ' ', 'n'),
            Trigram('l', 'i', 'n'),
            Trigram('s', 'e', 'n'),
            Trigram('t', ' ', 'o'),
            Trigram('t', ' ', 'a'),
            Trigram('r', 'a', 'a'),
            Trigram('e', 'n', 'e'),
            Trigram('o', 'p', 'v'),
            Trigram('p', 'v', 'o'),
            Trigram('e', 't', 'e'),
            Trigram(' ', 't', 'y'),
            Trigram('a', 'r', 'b'),
            Trigram(' ', 's', 'l'),
            Trigram('i', 'g', 'h'),
            Trigram('d', 'e', 'e'),
            Trigram('g', ' ', 'a'),
            Trigram('s', 't', 'r'),
            Trigram('n', 's', 'l'),
            Trigram('s', 'e', 'l'),
            Trigram('e', 'r', 'n'),
            Trigram('s', 't', 'e'),
        ],
    ),
    (
        Lang::Fin,
        &[
            Trigram('e', 'n', ' '),
            Trigram('i', 's', 'e'),
            Trigram('j', 'a', ' '),
            Trigram('i', 's', 't'),
            Trigram(' ', 'j', 'a'),
            Trigram('o', 'n', ' '),
            Trigram('t', 'a', ' '),
            Trigram('s', 't', 'a'),
            Trigram('a', 'n', ' '),
            Trigram('n', ' ', 'j'),
            Trigram('a', 'i', 's'),
            Trigram('s', 'e', 'n'),
            Trigram('n', ' ', 'o'),
            Trigram('k', 'e', 'u'),
            Trigram('i', 'k', 'e'),
            Trigram('o', 'i', 'k'),
            Trigram('l', 'i', 's'),
            Trigram(' ', 'v', 'a'),
            Trigram('e', 'l', 'l'),
            Trigram('l', 'l', 'a'),
            Trigram('n', ' ', 't'),
            Trigram('u', 'k', 's'),
            Trigram(' ', 'o', 'n'),
            Trigram('k', 's', 'i'),
            Trigram(' ', 'o', 'i'),
            Trigram('n', ' ', 'k'),
            Trigram(' ', 'k', 'a'),
            Trigram('a', 'a', 'n'),
            Trigram('e', 'e', 'n'),
            Trigram('l', 'a', ' '),
            Trigram('l', 'l', 'i'),
            Trigram('k', 'a', 'i'),
            Trigram('a', ' ', 'j'),
            Trigram(' ', 't', 'a'),
            Trigram('s', 'a', ' '),
            Trigram('i', 'n', ' '),
            Trigram('m', 'i', 's'),
            Trigram(' ', 'j', 'o'),
            Trigram('a', ' ', 'o'),
            Trigram('ä', 'ä', 'n'),
            Trigram('ä', 'n', ' '),
            Trigram('s', 'e', 'l'),
            Trigram('n', ' ', 's'),
            Trigram('k', 's', 'e'),
            Trigram('a', ' ', 't'),
            Trigram('a', ' ', 'k'),
            Trigram('t', 'a', 'i'),
            Trigram('u', 's', ' '),
            Trigram('t', 't', 'a'),
            Trigram('a', 'n', 's'),
            Trigram('s', 's', 'a'),
            Trigram('k', 'u', 'n'),
            Trigram('d', 'e', 'n'),
            Trigram('t', 'ä', ' '),
            Trigram('e', 'u', 's'),
            Trigram('n', 'e', 'n'),
            Trigram('k', 'a', 'n'),
            Trigram('n', 's', 'a'),
            Trigram('a', 'p', 'a'),
            Trigram('a', 'l', 'l'),
            Trigram('e', 's', 't'),
            Trigram(' ', 's', 'e'),
            Trigram('e', 'i', 's'),
            Trigram('i', 'l', 'l'),
            Trigram('i', 'e', 'n'),
            Trigram('s', 'e', 'e'),
            Trigram('t', 'a', 'a'),
            Trigram(' ', 'y', 'h'),
            Trigram('j', 'o', 'k'),
            Trigram('n', ' ', 'y'),
            Trigram('v', 'a', 'p'),
            Trigram('a', ' ', 'v'),
            Trigram('t', 't', 'ä'),
            Trigram('o', 'k', 'a'),
            Trigram('n', ' ', 'v'),
            Trigram('a', 'i', ' '),
            Trigram('i', 't', 't'),
            Trigram('a', 'a', ' '),
            Trigram('a', 'i', 'k'),
            Trigram('e', 't', 't'),
            Trigram('t', 'u', 'k'),
            Trigram('t', 'i', ' '),
            Trigram('u', 's', 't'),
            Trigram(' ', 'k', 'u'),
            Trigram('i', 's', 'i'),
            Trigram('s', 't', 'ä'),
            Trigram('s', 'e', 's'),
            Trigram(' ', 't', 'ä'),
            Trigram(' ', 't', 'u'),
            Trigram('l', 'a', 'i'),
            Trigram('n', ' ', 'p'),
            Trigram('s', 't', 'i'),
            Trigram('a', 's', 't'),
            Trigram('n', ' ', 'e'),
            Trigram('n', ' ', 'm'),
            Trigram('t', 'ä', 'ä'),
            Trigram('s', 'i', 'a'),
            Trigram('u', 'n', 'n'),
            Trigram('ä', ' ', 'j'),
            Trigram('u', 'd', 'e'),
            Trigram('ä', ' ', 'o'),
            Trigram('s', 't', 'e'),
            Trigram('s', 'i', ' '),
            Trigram('t', 'e', 'i'),
            Trigram('i', 'n', 'e'),
            Trigram('p', 'e', 'r'),
            Trigram('a', ' ', 's'),
            Trigram('i', 'a', ' '),
            Trigram('k', 'ä', ' '),
            Trigram('ä', 'n', 'e'),
            Trigram(' ', 'm', 'i'),
            Trigram('m', 'a', 'a'),
            Trigram(' ', 'p', 'e'),
            Trigram('a', ' ', 'p'),
            Trigram('e', 's', 's'),
            Trigram('a', ' ', 'm'),
            Trigram('a', 'i', 'n'),
            Trigram('ä', 'm', 'ä'),
            Trigram('t', 'a', 'm'),
            Trigram('y', 'h', 't'),
            Trigram(' ', 'j', 'u'),
            Trigram('j', 'u', 'l'),
            Trigram('y', 'k', 's'),
            Trigram('h', 'ä', 'n'),
            Trigram('ä', ' ', 't'),
            Trigram(' ', 'h', 'ä'),
            Trigram('u', 't', 't'),
            Trigram('i', 'd', 'e'),
            Trigram('e', 't', ' '),
            Trigram('l', 'l', 'ä'),
            Trigram('v', 'a', 'l'),
            Trigram('s', 'e', 'k'),
            Trigram('s', 't', 'u'),
            Trigram('n', ' ', 'a'),
            Trigram('l', 'ä', ' '),
            Trigram('a', 'm', 'i'),
            Trigram('h', 'm', 'i'),
            Trigram(' ', 'k', 'e'),
            Trigram('i', 'k', 'k'),
            Trigram('l', 'l', 'e'),
            Trigram('i', 'i', 'n'),
            Trigram('s', 'ä', ' '),
            Trigram('e', 'u', 'k'),
            Trigram('t', 'ä', 'm'),
            Trigram('i', 'h', 'm'),
            Trigram('t', 'e', 'e'),
            Trigram(' ', 'i', 'h'),
            Trigram('l', 't', 'a'),
            Trigram('p', 'a', 'u'),
            Trigram(' ', 's', 'a'),
            Trigram('i', 's', 'k'),
            Trigram('m', 'ä', 'ä'),
            Trigram('o', 'i', 's'),
            Trigram('u', 'n', ' '),
            Trigram('t', 'a', 'v'),
            Trigram('t', 'e', 'n'),
            Trigram('d', 'i', 's'),
            Trigram('h', 't', 'e'),
            Trigram('n', ' ', 'h'),
            Trigram('i', 's', 's'),
            Trigram('s', 's', 'ä'),
            Trigram('a', ' ', 'h'),
            Trigram('a', 'v', 'a'),
            Trigram(' ', 'm', 'a'),
            Trigram('a', ' ', 'y'),
            Trigram(' ', 'e', 'i'),
            Trigram(' ', 't', 'e'),
            Trigram(' ', 's', 'i'),
            Trigram(' ', 'o', 'l'),
            Trigram('e', 'k', 'ä'),
            Trigram('s', 't', 'y'),
            Trigram('a', 'l', 't'),
            Trigram('t', 'o', 'i'),
            Trigram('a', 't', 't'),
            Trigram('o', 'l', 'l'),
            Trigram('t', 'e', 't'),
            Trigram(' ', 'j', 'ä'),
            Trigram(' ', 'r', 'a'),
            Trigram('v', 'a', 't'),
            Trigram(' ', 'm', 'u'),
            Trigram('i', 'e', 'l'),
            Trigram(' ', 't', 'o'),
            Trigram('m', 'a', 'i'),
            Trigram('s', 'a', 'l'),
            Trigram('i', 's', 'u'),
            Trigram('a', ' ', 'a'),
            Trigram('k', 'k', 'i'),
            Trigram('a', 't', ' '),
            Trigram('s', 'u', 'u'),
            Trigram('n', ' ', 'l'),
            Trigram('v', 'ä', 'l'),
            Trigram('ä', 'ä', ' '),
            Trigram('u', 'l', 'i'),
            Trigram('t', 'u', 'n'),
            Trigram('t', 'i', 'e'),
            Trigram('e', 'r', 'u'),
            Trigram(' ', 'y', 'k'),
            Trigram('e', 't', 'u'),
            Trigram('v', 'a', 'a'),
            Trigram('r', 'u', 's'),
            Trigram('m', 'u', 'k'),
            Trigram(' ', 'h', 'e'),
            Trigram('e', 'i', ' '),
            Trigram('a', ' ', 'e'),
            Trigram('k', 'i', 'e'),
            Trigram('s', 'k', 'u'),
            Trigram('e', 'i', 'd'),
            Trigram('i', 'i', 't'),
            Trigram(' ', 's', 'u'),
            Trigram('n', 'n', 'a'),
            Trigram('s', 'i', 'l'),
            Trigram('o', 'm', 'a'),
            Trigram('m', 'i', 'n'),
            Trigram(' ', 'y', 'l'),
            Trigram('l', 'i', 'n'),
            Trigram('a', 'u', 't'),
            Trigram('u', 'u', 't'),
            Trigram('s', 'k', 'o'),
            Trigram(' ', 'k', 'o'),
            Trigram('t', 't', 'i'),
            Trigram('l', 'e', ' '),
            Trigram('s', 'i', 'e'),
            Trigram('k', 'a', 'a'),
            Trigram('a', ' ', 'r'),
            Trigram(' ', 'r', 'i'),
            Trigram('s', 'i', 'i'),
            Trigram('n', 'n', 'o'),
            Trigram('e', 'l', 'i'),
            Trigram('t', 'u', 'r'),
            Trigram('s', 'a', 'a'),
            Trigram('a', 'a', 't'),
            Trigram('l', 'e', 'i'),
            Trigram('o', 'l', 'i'),
            Trigram('n', 'a', ' '),
            Trigram(' ', 'l', 'a'),
            Trigram('o', 'o', 'n'),
            Trigram('u', 'r', 'v'),
            Trigram('l', 'm', 'a'),
            Trigram('r', 'v', 'a'),
            Trigram('i', 't', 'e'),
            Trigram('m', 'i', 'e'),
            Trigram('v', 'a', 's'),
            Trigram('ä', ' ', 'm'),
            Trigram(' ', 'e', 'd'),
            Trigram('t', 'u', 's'),
            Trigram('i', 'a', 'a'),
            Trigram('i', 't', 'ä'),
            Trigram('ä', ' ', 'v'),
            Trigram('u', 'o', 'l'),
            Trigram('y', 'l', 'e'),
            Trigram(' ', 'a', 'l'),
            Trigram('l', 'i', 't'),
            Trigram('s', 'u', 'o'),
            Trigram('a', 'm', 'a'),
            Trigram('j', 'o', 'i'),
            Trigram('u', 'n', 't'),
            Trigram('u', 't', 'e'),
            Trigram('i', ' ', 'o'),
            Trigram('t', 'y', 'k'),
            Trigram('n', ' ', 'r'),
            Trigram('a', 'l', 'i'),
            Trigram('l', 'i', 'i'),
            Trigram('n', 'e', 'e'),
            Trigram('p', 'a', 'a'),
            Trigram('a', 'v', 'i'),
            Trigram('o', 'm', 'i'),
            Trigram('o', 'i', 't'),
            Trigram('j', 'e', 'n'),
            Trigram('k', 'ä', 'ä'),
            Trigram('v', 'o', 'i'),
            Trigram('y', 'h', 'd'),
            Trigram('ä', ' ', 'k'),
            Trigram(' ', 'k', 'i'),
            Trigram('e', 'e', 't'),
            Trigram('e', 'k', 's'),
            Trigram(' ', 's', 'y'),
            Trigram('i', 't', 'y'),
            Trigram('i', 'l', 'ö'),
            Trigram('i', 'l', 'm'),
            Trigram('o', 'i', 'm'),
            Trigram('o', 'l', 'e'),
            Trigram('s', 'i', 't'),
            Trigram('i', 't', 'a'),
            Trigram('u', 'o', 'm'),
            Trigram('v', 'a', 'i'),
            Trigram('u', 's', 'k'),
            Trigram('a', 'l', 'a'),
            Trigram('h', 'e', 'n'),
            Trigram('o', 'p', 'e'),
            Trigram(' ', 'p', 'u'),
            Trigram('a', 'u', 'k'),
            Trigram('p', 'e', 't'),
            Trigram('o', 'j', 'a'),
            Trigram('i', ' ', 's'),
            Trigram('r', 'i', 'i'),
            Trigram('u', 'u', 'd'),
            Trigram('h', 'd', 'i'),
            Trigram('ä', 'l', 'i'),
            Trigram('v', 'a', ' '),
            Trigram(' ', 'o', 'm'),
        ],
    ),
    (
        Lang::Slk,
        &[
            Trigram(' ', 'p', 'r'),
            Trigram(' ', 'a', ' '),
            Trigram('p', 'r', 'á'),
            Trigram('r', 'á', 'v'),
            Trigram(' ', 'p', 'o'),
            Trigram('i', 'e', ' '),
            Trigram('c', 'h', ' '),
            Trigram('o', 's', 't'),
            Trigram(' ', 'r', 'o'),
            Trigram('h', 'o', ' '),
            Trigram(' ', 'n', 'a'),
            Trigram('v', 'o', ' '),
            Trigram('a', 'n', 'i'),
            Trigram('n', 'a', ' '),
            Trigram(' ', 'n', 'e'),
            Trigram('n', 'o', 's'),
            Trigram('a', 'ž', 'd'),
            Trigram('k', 't', 'o'),
            Trigram('k', 'a', 'ž'),
            Trigram(' ', 'k', 'a'),
            Trigram('m', 'á', ' '),
            Trigram('n', 'é', ' '),
            Trigram('á', 'v', 'o'),
            Trigram('o', 'm', ' '),
            Trigram(' ', 'm', 'á'),
            Trigram('e', 'b', 'o'),
            Trigram('t', 'i', ' '),
            Trigram(' ', 'v', ' '),
            Trigram(' ', 'a', 'l'),
            Trigram('a', 'l', 'e'),
            Trigram('l', 'e', 'b'),
            Trigram('b', 'o', ' '),
            Trigram(' ', 'j', 'e'),
            Trigram(' ', 'z', 'a'),
            Trigram('ý', 'c', 'h'),
            Trigram('o', ' ', 'n'),
            Trigram('ž', 'd', 'ý'),
            Trigram('d', 'ý', ' '),
            Trigram('i', 'a', ' '),
            Trigram(' ', 's', 'l'),
            Trigram('m', 'i', ' '),
            Trigram('o', 'v', 'a'),
            Trigram('s', 't', 'i'),
            Trigram('n', 'i', 'e'),
            Trigram('v', 'a', 'n'),
            Trigram('t', 'o', ' '),
            Trigram('e', 'n', 'i'),
            Trigram('n', 'e', ' '),
            Trigram('á', 'v', 'a'),
            Trigram('l', 'o', 'b'),
            Trigram('é', 'h', 'o'),
            Trigram('s', 'l', 'o'),
            Trigram('r', 'o', 'd'),
            Trigram('t', 'o', 'r'),
            Trigram('r', 'o', 'v'),
            Trigram(' ', 's', 'p'),
            Trigram(' ', 'z', 'á'),
            Trigram('á', ' ', 'p'),
            Trigram('o', ' ', 'v'),
            Trigram('a', ' ', 'p'),
            Trigram(' ', 'k', 't'),
            Trigram('ý', ' ', 'm'),
            Trigram(' ', 's', 'v'),
            Trigram('v', 'o', 'j'),
            Trigram('b', 'o', 'd'),
            Trigram('o', 'b', 'o'),
            Trigram('n', 'i', 'a'),
            Trigram(' ', 'n', 'á'),
            Trigram(' ', 'v', 'y'),
            Trigram('e', 'j', ' '),
            Trigram('j', 'e', ' '),
            Trigram('a', 'ť', ' '),
            Trigram('o', ' ', 'p'),
            Trigram('a', ' ', 'v'),
            Trigram('a', ' ', 's'),
            Trigram('á', 'r', 'o'),
            Trigram('a', ' ', 'z'),
            Trigram(' ', 's', 'a'),
            Trigram(' ', 'm', 'a'),
            Trigram('a', ' ', 'n'),
            Trigram('e', ' ', 'a'),
            Trigram('e', ' ', 's'),
            Trigram('m', 'u', ' '),
            Trigram('m', 'i', 'e'),
            Trigram('k', 'l', 'a'),
            Trigram('n', 'á', 'r'),
            Trigram('s', 'v', 'o'),
            Trigram('s', 'p', 'o'),
            Trigram(' ', 'b', 'y'),
            Trigram('o', 'v', 'n'),
            Trigram('b', 'y', ' '),
            Trigram('r', 'o', 'z'),
            Trigram('s', 'a', ' '),
            Trigram('ľ', 'u', 'd'),
            Trigram('i', 'ť', ' '),
            Trigram('o', 'd', 'n'),
            Trigram(' ', 'v', 'š'),
            Trigram('o', 'v', ' '),
            Trigram('i', ' ', 'a'),
            Trigram('n', 'é', 'h'),
            Trigram('v', 'š', 'e'),
            Trigram('o', ' ', 's'),
            Trigram('v', 'a', ' '),
            Trigram('o', ' ', 'a'),
            Trigram(' ', 'ľ', 'u'),
            Trigram('o', 'c', 'i'),
            Trigram('p', 'r', 'e'),
            Trigram('n', 'u', ' '),
            Trigram('a', ' ', 'm'),
            Trigram('u', ' ', 'a'),
            Trigram('e', 'n', 'ý'),
            Trigram('e', ' ', 'v'),
            Trigram('n', 'ý', ' '),
            Trigram('n', 'e', 's'),
            Trigram('a', ' ', 'k'),
            Trigram('z', 'á', 'k'),
            Trigram('p', 'o', 'd'),
            Trigram('n', 'ý', 'm'),
            Trigram(' ', 'd', 'o'),
            Trigram('u', ' ', 'p'),
            Trigram(' ', 'k', ' '),
            Trigram('u', ' ', 's'),
            Trigram('á', 'c', 'i'),
            Trigram('a', 'j', 'ú'),
            Trigram('b', 'y', 'ť'),
            Trigram('y', 'ť', ' '),
            Trigram('n', 'ý', 'c'),
            Trigram('e', 'h', 'o'),
            Trigram('r', 'a', 'n'),
            Trigram('p', 'o', 'l'),
            Trigram('t', 'á', 't'),
            Trigram('s', 't', 'n'),
            Trigram('j', 'e', 'h'),
            Trigram('a', ' ', 'r'),
            Trigram('š', 'e', 't'),
            Trigram('ý', 'm', 'i'),
            Trigram('l', 'a', 'd'),
            Trigram('č', 'i', 'n'),
            Trigram('é', 'm', 'u'),
            Trigram('a', ' ', 'o'),
            Trigram('e', 'd', 'z'),
            Trigram('ť', ' ', 's'),
            Trigram('k', 'o', 'n'),
            Trigram('s', 't', 'v'),
            Trigram('o', 'r', 'é'),
            Trigram(' ', 's', 'ú'),
            Trigram(' ', 'n', 'i'),
            Trigram('e', ' ', 'z'),
            Trigram('p', 'r', 'i'),
            Trigram('o', 'c', 'h'),
            Trigram('n', 'y', ' '),
            Trigram('š', 't', 'á'),
            Trigram('s', 'ť', ' '),
            Trigram('o', 'j', 'e'),
            Trigram('v', 'n', 'a'),
            Trigram('t', 'r', 'e'),
            Trigram('u', ' ', 'k'),
            Trigram(' ', 'č', 'i'),
            Trigram('k', 'o', ' '),
            Trigram('é', ' ', 'p'),
            Trigram('m', 'a', 'j'),
            Trigram('s', 'm', 'i'),
            Trigram('a', ' ', 'a'),
            Trigram('e', 't', 'k'),
            Trigram('n', 'a', 'k'),
            Trigram('ý', 'm', ' '),
            Trigram('m', 'e', 'd'),
            Trigram('d', 'o', 'v'),
            Trigram('p', 'r', 'í'),
            Trigram(' ', 'o', 'b'),
            Trigram('i', 'u', ' '),
            Trigram('u', 'd', 's'),
            Trigram('o', 's', 'ť'),
            Trigram('e', 's', 'm'),
            Trigram('e', ' ', 'b'),
            Trigram('m', ' ', 'a'),
            Trigram('h', 'r', 'a'),
            Trigram('i', ' ', 's'),
            Trigram('r', 'á', 'c'),
            Trigram('b', 'e', 'z'),
            Trigram('v', 'a', 'ť'),
            Trigram('c', 'h', 'r'),
            Trigram('e', ' ', 'p'),
            Trigram(' ', 'a', 'b'),
            Trigram('j', 'ú', ' '),
            Trigram(' ', 'š', 't'),
            Trigram('ž', 'e', 'n'),
            Trigram(' ', 'h', 'o'),
            Trigram('č', 'e', 'n'),
            Trigram(' ', 'd', 'e'),
            Trigram('i', ' ', 'p'),
            Trigram('ť', ' ', 'v'),
            Trigram(' ', 'v', 'o'),
            Trigram('d', 's', 'k'),
            Trigram('p', 'r', 'o'),
            Trigram('n', 'o', 'm'),
            Trigram(' ', 'i', 'n'),
            Trigram('o', 'u', ' '),
            Trigram('d', 'u', ' '),
            Trigram('ž', 'e', ' '),
            Trigram('a', 'b', 'y'),
            Trigram('e', 's', 't'),
            Trigram(' ', 'b', 'o'),
            Trigram('r', 'é', ' '),
            Trigram('b', 'o', 'l'),
            Trigram(' ', 's', 'o'),
            Trigram('n', 'ú', ' '),
            Trigram('o', 'l', 'o'),
            Trigram('k', 'e', 'j'),
            Trigram('á', 'l', 'n'),
            Trigram(' ', 'o', 'c'),
            Trigram('o', 'b', 'e'),
            Trigram('k', 'y', ' '),
            Trigram('d', 'z', 'i'),
            Trigram('d', 'o', 'm'),
            Trigram('á', 'v', ' '),
            Trigram('p', 'o', 'r'),
            Trigram('l', 'n', 'e'),
            Trigram('r', 'a', 'v'),
            Trigram('a', 'k', 'é'),
            Trigram('e', 'n', 's'),
            Trigram('p', 'r', 'a'),
            Trigram('o', 'k', ' '),
            Trigram(' ', 'ž', 'e'),
            Trigram('t', 'n', 'é'),
            Trigram(' ', 't', 'a'),
            Trigram('a', 'k', 'o'),
            Trigram('r', 'e', 's'),
            Trigram(' ', 'v', 'z'),
            Trigram('i', ' ', 'k'),
            Trigram('a', 'm', 'i'),
            Trigram(' ', 't', 'r'),
            Trigram(' ', 'a', 'k'),
            Trigram('n', 'í', ' '),
            Trigram('l', 'e', 'n'),
            Trigram('o', ' ', 'd'),
            Trigram('d', 'e', 'l'),
            Trigram('s', 'k', 'ý'),
            Trigram('c', 'h', 'o'),
            Trigram('a', 'c', 'h'),
            Trigram('i', 'v', 'o'),
            Trigram('h', ' ', 'p'),
            Trigram('o', 'ž', 'e'),
            Trigram('i', 'á', 'l'),
            Trigram('i', 'n', 'n'),
            Trigram('s', 'l', 'u'),
            Trigram('k', 'r', 'a'),
            Trigram('l', 'o', 'č'),
            Trigram('o', 'č', 'n'),
            Trigram('j', 'u', ' '),
            Trigram(' ', 'o', 's'),
            Trigram('a', 'n', 'u'),
            Trigram('o', 'j', 'u'),
            Trigram('v', 'o', 'ľ'),
            Trigram('á', 'k', 'l'),
            Trigram('s', 't', 'r'),
            Trigram('é', ' ', 's'),
            Trigram('e', 'n', 'é'),
            Trigram(' ', 'ž', 'i'),
            Trigram('n', 'i', 'u'),
            Trigram('s', 't', 'a'),
            Trigram(' ', 's', 't'),
            Trigram('v', 'e', 'd'),
            Trigram('t', 'v', 'o'),
            Trigram(' ', 'm', 'e'),
            Trigram('d', 'n', 'o'),
            Trigram('m', ' ', 'p'),
            Trigram('d', 'e', ' '),
            Trigram('k', 'é', ' '),
            Trigram('k', 'ý', 'm'),
            Trigram('i', 'k', 't'),
            Trigram('s', 't', 'u'),
            Trigram('é', ' ', 'v'),
            Trigram('i', ' ', 'v'),
            Trigram('v', 'y', 'h'),
            Trigram(' ', 't', 'o'),
            Trigram('v', ' ', 'a'),
            Trigram('o', 'd', 'u'),
            Trigram('h', 'o', 'c'),
            Trigram('a', ' ', 't'),
            Trigram('í', 'm', ' '),
            Trigram('l', 'y', ' '),
            Trigram('h', 'o', 'v'),
            Trigram('y', ' ', 's'),
            Trigram('s', 'o', 'c'),
            Trigram('j', 'ú', 'c'),
            Trigram('ú', ' ', 'p'),
            Trigram('o', 'd', 'i'),
            Trigram('v', 'o', 'd'),
            Trigram('l', 'i', 'v'),
            Trigram('a', 'n', 'í'),
            Trigram('c', 'i', 'á'),
            Trigram(' ', 'v', 'e'),
            Trigram('r', 'e', 'j'),
            Trigram('k', 'u', ' '),
            Trigram('c', 'i', ' '),
            Trigram('s', 'k', 'e'),
            Trigram('s', 'o', 'b'),
            Trigram('č', 'n', 'o'),
            Trigram('o', 's', 'o'),
        ],
    ),
    (
        Lang::Tuk,
        &[
            Trigram('l', 'a', 'r'),
            Trigram(' ', 'w', 'e'),
            Trigram('w', 'e', ' '),
            Trigram(' ', 'b', 'i'),
            Trigram('y', 'ň', ' '),
            Trigram('a', 'r', 'y'),
            Trigram('a', 'd', 'a'),
            Trigram('d', 'a', ' '),
            Trigram(' ', 'h', 'e'),
            Trigram(' ', 'h', 'a'),
            Trigram('a', 'n', ' '),
            Trigram('y', 'n', 'y'),
            Trigram('k', 'l', 'a'),
            Trigram('d', 'a', 'm'),
            Trigram('d', 'e', ' '),
            Trigram(' ', 'a', 'd'),
            Trigram('y', 'n', 'a'),
            Trigram('e', 'r', ' '),
            Trigram('n', 'a', ' '),
            Trigram(' ', 'ý', 'a'),
            Trigram('i', 'r', ' '),
            Trigram('d', 'y', 'r'),
            Trigram('i', 'ň', ' '),
            Trigram('b', 'i', 'r'),
            Trigram('r', ' ', 'b'),
            Trigram('y', 'd', 'y'),
            Trigram('l', 'e', 'r'),
            Trigram('a', 'r', 'a'),
            Trigram('a', 'm', ' '),
            Trigram('y', 'r', ' '),
            Trigram('i', 'n', 'i'),
            Trigram('l', 'a', 'n'),
            Trigram('r', ' ', 'a'),
            Trigram('k', 'l', 'y'),
            Trigram('l', 'y', 'd'),
            Trigram(' ', 'ö', 'z'),
            Trigram('m', 'a', 'g'),
            Trigram('n', 'y', 'ň'),
            Trigram('ö', 'z', ' '),
            Trigram('h', 'e', 'r'),
            Trigram('g', 'y', 'n'),
            Trigram('a', 'g', 'a'),
            Trigram('e', 'n', ' '),
            Trigram('r', 'y', 'n'),
            Trigram('a', 'k', 'l'),
            Trigram('a', 'l', 'a'),
            Trigram('d', 'a', 'n'),
            Trigram('h', 'a', 'k'),
            Trigram('e', 'r', 'i'),
            Trigram('n', 'e', ' '),
            Trigram('u', 'k', 'u'),
            Trigram('a', 'r', ' '),
            Trigram('r', ' ', 'h'),
            Trigram('g', 'a', ' '),
            Trigram('n', 'y', ' '),
            Trigram('h', 'u', 'k'),
            Trigram(' ', 'd', 'e'),
            Trigram('i', 'l', 'i'),
            Trigram('y', 'g', 'y'),
            Trigram('l', 'i', ' '),
            Trigram('k', 'u', 'k'),
            Trigram('a', ' ', 'h'),
            Trigram('n', 'd', 'a'),
            Trigram('a', 's', 'y'),
            Trigram('l', 'e', 'n'),
            Trigram(' ', 'e', 'd'),
            Trigram('b', 'i', 'l'),
            Trigram('a', 't', 'l'),
            Trigram('i', 'n', 'e'),
            Trigram('e', 'd', 'i'),
            Trigram('n', 'i', 'ň'),
            Trigram('l', 'y', 'g'),
            Trigram(' ', 'h', 'u'),
            Trigram(' ', 'g', 'a'),
            Trigram('e', ' ', 'h'),
            Trigram('n', 'd', 'e'),
            Trigram('d', 'i', 'l'),
            Trigram('r', 'y', 'ň'),
            Trigram('a', 'z', 'a'),
            Trigram('z', 'a', 't'),
            Trigram('a', ' ', 'g'),
            Trigram('‐', 'd', 'a'),
            Trigram('a', '‐', 'd'),
            Trigram('e', 't', 'i'),
            Trigram('u', 'k', 'l'),
            Trigram(' ', 'g', 'ö'),
            Trigram('l', 'y', ' '),
            Trigram(' ', 'b', 'o'),
            Trigram('t', 'l', 'y'),
            Trigram('g', 'i', 'n'),
            Trigram(' ', 'a', 'z'),
            Trigram('l', 'm', 'a'),
            Trigram('a', 'm', 'a'),
            Trigram('h', 'e', 'm'),
            Trigram('d', 'i', 'r'),
            Trigram('y', 'k', 'l'),
            Trigram('‐', 'd', 'e'),
            Trigram('e', ' ', 'd'),
            Trigram('i', 'l', 'e'),
            Trigram('ý', 'a', 'n'),
            Trigram('a', ' ', 'd'),
            Trigram('ý', 'e', 't'),
            Trigram('ý', 'a', '‐'),
            Trigram('y', 'n', 'd'),
            Trigram('l', 'y', 'k'),
            Trigram('a', 'ý', 'y'),
            Trigram('e', ' ', 'a'),
            Trigram('ü', 'n', 'd'),
            Trigram('g', 'e', ' '),
            Trigram(' ', 'g', 'o'),
            Trigram('e', 'g', 'i'),
            Trigram('i', 'l', 'm'),
            Trigram('s', 'y', ' '),
            Trigram('n', 'i', ' '),
            Trigram('e', 't', 'm'),
            Trigram('e', 'm', '‐'),
            Trigram('l', 'm', 'e'),
            Trigram('m', '‐', 'd'),
            Trigram('a', 'l', 'y'),
            Trigram('a', 'n', 'y'),
            Trigram(' ', 'b', 'e'),
            Trigram('t', 'l', 'e'),
            Trigram('s', 'y', 'n'),
            Trigram('r', 'i', 'n'),
            Trigram('y', ' ', 'b'),
            Trigram('l', 'e', 't'),
            Trigram('m', 'a', 'k'),
            Trigram('a', ' ', 'w'),
            Trigram('a', ' ', 'ý'),
            Trigram('d', 'e', 'n'),
            Trigram('ä', 'g', 'e'),
            Trigram('r', 'a', ' '),
            Trigram(' ', 'ä', 'h'),
            Trigram('m', 'ä', 'g'),
            Trigram(' ', 'd', 'u'),
            Trigram('n', ' ', 'e'),
            Trigram('b', 'o', 'l'),
            Trigram('m', 'e', 'g'),
            Trigram('e', 'l', 'e'),
            Trigram('ň', ' ', 'h'),
            Trigram(' ', 'e', 't'),
            Trigram('i', 'g', 'i'),
            Trigram('ň', ' ', 'w'),
            Trigram('i', 'm', ' '),
            Trigram('i', 'ý', 'a'),
            Trigram(' ', 'ý', 'e'),
            Trigram(' ', 'd', 'i'),
            Trigram('r', ' ', 'e'),
            Trigram('e', 'k', ' '),
            Trigram(' ', 'b', 'a'),
            Trigram('a', 'k', ' '),
            Trigram('e', 's', 'i'),
            Trigram('r', 'i', 'l'),
            Trigram('a', ' ', 'b'),
            Trigram('i', 'n', ' '),
            Trigram('p', ' ', 'b'),
            Trigram('d', 'e', 'ň'),
            Trigram('e', 't', 'l'),
            Trigram('a', 'g', 'y'),
            Trigram(' ', 'b', 'u'),
            Trigram(' ', 'j', 'e'),
            Trigram('b', 'u', ' '),
            Trigram('e', ' ', 'ö'),
            Trigram('y', ' ', 'd'),
            Trigram(' ', 'h', 'i'),
            Trigram('m', 'e', 'z'),
            Trigram(' ', 'e', 's'),
            Trigram('a', 'r', 'd'),
            Trigram(' ', 's', 'a'),
            Trigram('ä', 'h', 'l'),
            Trigram('e', ' ', 'b'),
            Trigram('y', 'l', 'y'),
            Trigram(' ', 'k', 'a'),
            Trigram('e', 's', 'a'),
            Trigram('m', 'e', 'k'),
            Trigram(' ', 'g', 'u'),
            Trigram('n', ' ', 'a'),
            Trigram('e', ' ', 't'),
            Trigram('l', 'i', 'k'),
            Trigram(' ', 'd', 'o'),
            Trigram('e', ' ', 'g'),
            Trigram('s', 'a', 's'),
            Trigram('i', 'l', 'l'),
            Trigram('n', 'm', 'a'),
            Trigram('ň', ' ', 'a'),
            Trigram('r', 'a', 'm'),
            Trigram('o', 'l', 'a'),
            Trigram('h', 'a', 'l'),
            Trigram('y', ' ', 'w'),
            Trigram('ý', 'a', 'r'),
            Trigram(' ', 'a', 'r'),
            Trigram('a', 'n', 'm'),
            Trigram('m', 'e', 'l'),
            Trigram('i', 'r', 'i'),
            Trigram('s', 'i', 'ý'),
            Trigram('n', 'd', 'i'),
            Trigram('e', 'd', 'e'),
            Trigram('g', 'a', 'l'),
            Trigram('e', 'n', 'd'),
            Trigram('m', 'i', 'l'),
            Trigram('r', 'l', 'a'),
            Trigram('g', 'ö', 'z'),
            Trigram(' ', 'm', 'a'),
            Trigram('n', ' ', 'b'),
            Trigram('e', ' ', 'ý'),
            Trigram('ö', 'ň', 'ü'),
            Trigram('ň', 'ü', 'n'),
            Trigram('n', ' ', 'h'),
            Trigram(' ', 't', 'u'),
            Trigram('h', 'i', 'ç'),
            Trigram('y', 'ý', 'e'),
            Trigram(' ', 'g', 'e'),
            Trigram('m', 'y', ' '),
            Trigram('i', 'ç', ' '),
            Trigram(' ', 'ö', 'ň'),
            Trigram('n', ' ', 'ý'),
            Trigram('t', 'l', 'a'),
            Trigram('ň', ' ', 'ý'),
            Trigram('l', 'i', 'n'),
            Trigram('r', 'd', 'a'),
            Trigram('a', 'l', ' '),
            Trigram('l', 'i', 'g'),
            Trigram('g', 'a', 'r'),
            Trigram(' ', 'm', 'i'),
            Trigram('i', ' ', 'g'),
            Trigram('d', 'a', 'l'),
            Trigram('r', 'l', 'e'),
            Trigram('m', 'a', 'l'),
            Trigram('k', 'a', 'n'),
            Trigram('g', 'a', 't'),
            Trigram('t', 'm', 'e'),
            Trigram('s', 'i', 'n'),
            Trigram('a', 'n', 'd'),
            Trigram('ň', ' ', 'g'),
            Trigram('g', 'o', 'r'),
            Trigram(' ', 't', 'a'),
            Trigram('ö', 'w', 'l'),
            Trigram('ý', 'l', 'e'),
            Trigram('y', ' ', 'g'),
            Trigram('e', ' ', 'w'),
            Trigram('o', 'r', 'a'),
            Trigram('t', 'i', 'ň'),
            Trigram('e', 'k', 'l'),
            Trigram(' ', 'y', 'n'),
            Trigram('a', 'l', 'k'),
            Trigram('d', 'ö', 'w'),
            Trigram(' ', 'd', 'ö'),
            Trigram('e', 'r', 'e'),
            Trigram('m', ' ', 'h'),
            Trigram(' ', 'm', 'e'),
            Trigram('d', 'u', 'r'),
            Trigram(' ', 'e', 'r'),
            Trigram('a', 's', 'i'),
            Trigram('t', 'u', 't'),
            Trigram('a', 't', ' '),
            Trigram('ç', 'i', 'n'),
            Trigram('i', 'r', 'l'),
            Trigram('u', 'm', 'y'),
            Trigram('e', 'l', 'i'),
            Trigram('e', 'r', 'k'),
            Trigram('n', 'm', 'e'),
            Trigram('w', 'l', 'e'),
            Trigram('g', 'u', 'r'),
            Trigram('a', ' ', 'ö'),
            Trigram('a', 'ý', 'a'),
            Trigram(' ', 'ç', 'ä'),
            Trigram('n', 'u', 'n'),
            Trigram(' ', 'k', 'i'),
            Trigram('r', 'a', 's'),
            Trigram('a', 'm', 'l'),
            Trigram('u', 'p', ' '),
            Trigram('ý', 'a', 'ş'),
            Trigram('t', 'y', 'n'),
            Trigram(' ', 'a', 'ý'),
            Trigram('r', 'y', ' '),
            Trigram('ň', ' ', 'd'),
            Trigram('b', 'a', 'ş'),
            Trigram('i', 'p', ' '),
            Trigram('g', 'i', ' '),
            Trigram('z', ' ', 'h'),
            Trigram('k', 'i', 'n'),
            Trigram('z', ' ', 'ö'),
            Trigram('n', ' ', 'w'),
            Trigram('t', 'e', 'r'),
            Trigram('i', 'n', 'm'),
            Trigram('e', 'ý', 'l'),
            Trigram('i', ' ', 'ý'),
            Trigram('k', 'i', 'm'),
            Trigram('n', 'a', 'm'),
            Trigram('e', 'ň', ' '),
            Trigram('b', 'e', 'ý'),
            Trigram('d', 'o', 'l'),
            Trigram(' ', 's', 'e'),
            Trigram(' ', 't', 'e'),
            Trigram('r', ' ', 'd'),
            Trigram('u', 't', 'u'),
            Trigram('g', 'y', 'ý'),
            Trigram('e', 'z', ' '),
            Trigram('u', 'm', 'u'),
            Trigram('m', 'u', 'm'),
        ],
    ),
    (
        Lang::Dan,
        &[
            Trigram('e', 'r', ' '),
            Trigram('o', 'g', ' '),
            Trigram(' ', 'o', 'g'),
            Trigram('d', 'e', 'r'),
            Trigram(' ', 'd', 'e'),
            Trigram('f', 'o', 'r'),
            Trigram('e', 'n', ' '),
            Trigram('e', 't', ' '),
            Trigram('t', 'i', 'l'),
            Trigram(' ', 'f', 'o'),
            Trigram(' ', 't', 'i'),
            Trigram('i', 'n', 'g'),
            Trigram('d', 'e', ' '),
            Trigram('n', 'd', 'e'),
            Trigram('r', 'e', 't'),
            Trigram(' ', 'r', 'e'),
            Trigram('h', 'e', 'd'),
            Trigram('i', 'l', ' '),
            Trigram('l', 'i', 'g'),
            Trigram(' ', 'h', 'a'),
            Trigram('l', 'l', 'e'),
            Trigram('d', 'e', 'n'),
            Trigram(' ', 'e', 'n'),
            Trigram('e', 'd', ' '),
            Trigram('v', 'e', 'r'),
            Trigram('e', 'l', 's'),
            Trigram('u', 'n', 'd'),
            Trigram('a', 'r', ' '),
            Trigram(' ', 'f', 'r'),
            Trigram(' ', 'm', 'e'),
            Trigram('s', 'e', ' '),
            Trigram('l', 's', 'e'),
            Trigram('a', 'n', 'd'),
            Trigram('h', 'a', 'r'),
            Trigram('g', 'e', 'n'),
            Trigram('e', 'd', 'e'),
            Trigram('g', 'e', ' '),
            Trigram('e', 'l', 'l'),
            Trigram('n', 'g', ' '),
            Trigram('a', 't', ' '),
            Trigram(' ', 'a', 'f'),
            Trigram('n', 'n', 'e'),
            Trigram('l', 'e', ' '),
            Trigram('n', 'g', 'e'),
            Trigram('e', ' ', 'f'),
            Trigram('g', 'h', 'e'),
            Trigram('e', ' ', 'o'),
            Trigram('i', 'g', 'h'),
            Trigram('e', 's', ' '),
            Trigram('a', 'f', ' '),
            Trigram('e', 'n', 'n'),
            Trigram(' ', 'a', 't'),
            Trigram('l', 'e', 'r'),
            Trigram(' ', 'i', ' '),
            Trigram('s', 'k', 'e'),
            Trigram('h', 'v', 'e'),
            Trigram('e', ' ', 'e'),
            Trigram('r', ' ', 'h'),
            Trigram('n', 'e', ' '),
            Trigram('e', 'n', 'h'),
            Trigram('t', ' ', 't'),
            Trigram('i', 'g', 'e'),
            Trigram('e', 's', 'k'),
            Trigram(' ', 'e', 'l'),
            Trigram(' ', 'b', 'e'),
            Trigram('i', 'g', ' '),
            Trigram('t', 'i', 'g'),
            Trigram('f', 'r', 'i'),
            Trigram('o', 'r', ' '),
            Trigram('s', 'k', 'a'),
            Trigram('n', 'i', 'n'),
            Trigram('e', ' ', 's'),
            Trigram('i', 'o', 'n'),
            Trigram(' ', 'e', 'r'),
            Trigram('n', 'h', 'v'),
            Trigram('r', 'e', ' '),
            Trigram('m', 'e', 'n'),
            Trigram('r', ' ', 'o'),
            Trigram('e', ' ', 'a'),
            Trigram(' ', 's', 't'),
            Trigram('a', 't', 'i'),
            Trigram(' ', 's', 'k'),
            Trigram(' ', 'i', 'n'),
            Trigram('l', ' ', 'a'),
            Trigram('t', 'i', 'o'),
            Trigram(' ', 'p', 'å'),
            Trigram('e', 't', 't'),
            Trigram('e', 'n', 's'),
            Trigram('a', 'l', ' '),
            Trigram('t', 't', 'i'),
            Trigram('m', 'e', 'd'),
            Trigram('r', ' ', 'f'),
            Trigram('o', 'm', ' '),
            Trigram('e', 'n', 'd'),
            Trigram('r', ' ', 'e'),
            Trigram('d', 'e', 'l'),
            Trigram('g', ' ', 'f'),
            Trigram('k', 'e', ' '),
            Trigram(' ', 's', 'o'),
            Trigram('p', 'å', ' '),
            Trigram('e', 'l', 'i'),
            Trigram('g', ' ', 'o'),
            Trigram(' ', 'a', 'n'),
            Trigram('r', ' ', 'r'),
            Trigram('n', 's', ' '),
            Trigram(' ', 'a', 'l'),
            Trigram('n', 'a', 't'),
            Trigram('h', 'a', 'n'),
            Trigram(' ', 'v', 'e'),
            Trigram('r', ' ', 's'),
            Trigram('r', ' ', 'a'),
            Trigram(' ', 'u', 'n'),
            Trigram(' ', 'h', 'e'),
            Trigram('t', ' ', 'f'),
            Trigram('l', 'i', 'n'),
            Trigram(' ', 's', 'i'),
            Trigram('r', ' ', 'd'),
            Trigram('t', 'e', 'r'),
            Trigram('e', 'r', 'e'),
            Trigram('n', 'e', 's'),
            Trigram('d', 'e', 't'),
            Trigram('e', ' ', 'r'),
            Trigram(' ', 'u', 'd'),
            Trigram('a', 'l', 'e'),
            Trigram('s', 'a', 'm'),
            Trigram('i', 'h', 'e'),
            Trigram('l', 'a', 'n'),
            Trigram('t', 't', 'e'),
            Trigram('r', 'i', 'n'),
            Trigram('r', 'i', 'h'),
            Trigram('e', 'n', 't'),
            Trigram('n', 'd', 'l'),
            Trigram('e', ' ', 'm'),
            Trigram('i', 's', 'k'),
            Trigram('e', 'r', 'k'),
            Trigram('a', 'n', 's'),
            Trigram('t', ' ', 's'),
            Trigram('k', 'a', 'l'),
            Trigram(' ', 'n', 'a'),
            Trigram('s', 'o', 'm'),
            Trigram('h', 'o', 'l'),
            Trigram('l', 'd', 'e'),
            Trigram('i', 'n', 'd'),
            Trigram('e', ' ', 'n'),
            Trigram('r', 'e', 'n'),
            Trigram('n', ' ', 's'),
            Trigram('n', 'e', 'r'),
            Trigram('k', 'e', 'l'),
            Trigram('o', 'l', 'd'),
            Trigram('d', 'i', 'g'),
            Trigram('t', 'e', ' '),
            Trigram('o', 'r', 's'),
            Trigram('e', ' ', 'i'),
            Trigram(' ', 'h', 'v'),
            Trigram('s', 'n', 'i'),
            Trigram('s', 'k', 'y'),
            Trigram('e', 'n', 'e'),
            Trigram('v', 'æ', 'r'),
            Trigram(' ', 'l', 'i'),
            Trigram(' ', 's', 'a'),
            Trigram('s', ' ', 'f'),
            Trigram('d', ' ', 'd'),
            Trigram('e', 'r', 's'),
            Trigram('s', 't', 'e'),
            Trigram('n', 't', 'e'),
            Trigram('m', 'm', 'e'),
            Trigram('o', 'v', 'e'),
            Trigram('e', ' ', 'h'),
            Trigram('n', 'a', 'l'),
            Trigram('o', 'n', 'a'),
            Trigram('g', 'e', 'r'),
            Trigram(' ', 'g', 'r'),
            Trigram('a', 'g', 'e'),
            Trigram('g', ' ', 'a'),
            Trigram('v', 'i', 'l'),
            Trigram('a', 'l', 'l'),
            Trigram('e', ' ', 'd'),
            Trigram('f', 'r', 'e'),
            Trigram('t', 'e', 'l'),
            Trigram('s', ' ', 'o'),
            Trigram('g', ' ', 'h'),
            Trigram('t', ' ', 'o'),
            Trigram('t', ' ', 'd'),
            Trigram('r', ' ', 'i'),
            Trigram('e', ' ', 't'),
            Trigram(' ', 'o', 'm'),
            Trigram('a', 'r', 'b'),
            Trigram('d', ' ', 'e'),
            Trigram('e', 'r', 'n'),
            Trigram('r', ' ', 'u'),
            Trigram(' ', 'v', 'æ'),
            Trigram('d', ' ', 'o'),
            Trigram('r', 'e', 's'),
            Trigram('g', ' ', 't'),
            Trigram('k', 'l', 'æ'),
            Trigram('ø', 'r', 'e'),
            Trigram('n', ' ', 'f'),
            Trigram(' ', 'v', 'i'),
            Trigram(' ', 'm', 'å'),
            Trigram('v', 'e', 'n'),
            Trigram('s', 'k', ' '),
            Trigram(' ', 'l', 'a'),
            Trigram('g', 't', 'e'),
            Trigram('k', 'a', 'b'),
            Trigram('s', 't', 'r'),
            Trigram('n', ' ', 'm'),
            Trigram('r', 'e', 'l'),
            Trigram('e', ' ', 'b'),
            Trigram('r', 'u', 'n'),
            Trigram('r', 'b', 'e'),
            Trigram('b', 'e', 'j'),
            Trigram('t', ' ', 'i'),
            Trigram('e', 'j', 'd'),
            Trigram('k', 'k', 'e'),
            Trigram('t', ' ', 'e'),
            Trigram('g', ' ', 'd'),
            Trigram('r', 'k', 'l'),
            Trigram('i', 'l', 'k'),
            Trigram('g', 'r', 'u'),
            Trigram('v', 'e', 'd'),
            Trigram('b', 'e', 's'),
            Trigram(' ', 'd', 'a'),
            Trigram('n', 'd', ' '),
            Trigram(' ', 'f', 'u'),
            Trigram('l', 'æ', 'r'),
            Trigram('æ', 'r', 'i'),
            Trigram('r', 'd', 'i'),
            Trigram('æ', 'r', 'd'),
            Trigram('l', 'd', ' '),
            Trigram('t', ' ', 'm'),
            Trigram('d', 'l', 'i'),
            Trigram('f', 'u', 'n'),
            Trigram('s', 'i', 'g'),
            Trigram(' ', 'm', 'o'),
            Trigram('s', 't', 'a'),
            Trigram('n', 's', 't'),
            Trigram('r', 't', ' '),
            Trigram('o', 'd', ' '),
            Trigram(' ', 'a', 'r'),
            Trigram(' ', 'o', 'p'),
            Trigram('v', 'i', 's'),
            Trigram('i', 'g', 't'),
            Trigram('æ', 'r', 'e'),
            Trigram('t', 'e', 't'),
            Trigram('t', ' ', 'a'),
            Trigram('e', 'm', 'm'),
            Trigram('g', ' ', 'e'),
            Trigram('m', 'o', 'd'),
            Trigram('r', 'h', 'o'),
            Trigram('i', 'e', ' '),
            Trigram('g', ' ', 'u'),
            Trigram('k', 'e', 'r'),
            Trigram('r', 'e', 'm'),
            Trigram(' ', 'n', 'o'),
            Trigram('n', ' ', 'h'),
            Trigram(' ', 'f', 'a'),
            Trigram('r', 's', 'k'),
            Trigram('o', 'r', 'm'),
            Trigram('e', ' ', 'u'),
            Trigram('s', ' ', 's'),
            Trigram('e', 'm', ' '),
            Trigram('d', ' ', 'h'),
            Trigram(' ', 'g', 'e'),
            Trigram('e', 't', 's'),
            Trigram('e', ' ', 'g'),
            Trigram('g', ' ', 's'),
            Trigram('p', 'e', 'r'),
            Trigram(' ', 'e', 't'),
            Trigram('l', 'e', 'm'),
            Trigram(' ', 't', 'r'),
            Trigram('i', ' ', 's'),
            Trigram('d', 'a', ' '),
            Trigram('d', 'r', 'e'),
            Trigram('n', ' ', 'a'),
            Trigram('d', 'e', 's'),
            Trigram('d', 't', ' '),
            Trigram('k', 'y', 't'),
            Trigram('r', 'd', 'e'),
            Trigram('y', 't', 't'),
            Trigram('e', 'r', 'i'),
            Trigram('h', 'e', 'n'),
            Trigram('e', 'r', 'v'),
            Trigram('l', ' ', 'e'),
            Trigram('r', 'v', 'i'),
            Trigram('f', 'f', 'e'),
            Trigram('o', 'f', 'f'),
            Trigram('i', 's', 'n'),
            Trigram('r', ' ', 't'),
            Trigram(' ', 'o', 'f'),
            Trigram('k', 'e', 'n'),
            Trigram('l', ' ', 'h'),
            Trigram('r', 'k', 'e'),
            Trigram('g', ' ', 'i'),
            Trigram('t', 'a', 'l'),
            Trigram('m', 'å', ' '),
            Trigram('r', ' ', 'k'),
            Trigram('l', 'k', 'e'),
            Trigram('g', 't', ' '),
            Trigram('t', ' ', 'v'),
            Trigram('t', ' ', 'b'),
        ],
    ),
    (
        Lang::Nob,
        &[
            Trigram('e', 'r', ' '),
            Trigram(' ', 'o', 'g'),
            Trigram('o', 'g', ' '),
            Trigram('e', 'n', ' '),
            Trigram(' ', 'd', 'e'),
            Trigram('f', 'o', 'r'),
            Trigram('t', 'i', 'l'),
            Trigram('i', 'n', 'g'),
            Trigram('e', 't', 't'),
            Trigram(' ', 't', 'i'),
            Trigram('e', 't', ' '),
            Trigram(' ', 'h', 'a'),
            Trigram(' ', 'f', 'o'),
            Trigram(' ', 'r', 'e'),
            Trigram('r', 'e', 't'),
            Trigram('i', 'l', ' '),
            Trigram('h', 'e', 't'),
            Trigram('l', 'l', 'e'),
            Trigram('v', 'e', 'r'),
            Trigram('t', 't', ' '),
            Trigram('a', 'r', ' '),
            Trigram('n', 'n', 'e'),
            Trigram(' ', 'e', 'n'),
            Trigram('o', 'm', ' '),
            Trigram('e', 'l', 'l'),
            Trigram('n', 'g', ' '),
            Trigram('h', 'a', 'r'),
            Trigram(' ', 'm', 'e'),
            Trigram('e', 'n', 'n'),
            Trigram('t', 'e', 'r'),
            Trigram('d', 'e', ' '),
            Trigram('l', 'i', 'g'),
            Trigram(' ', 'f', 'r'),
            Trigram(' ', 's', 'o'),
            Trigram('r', ' ', 'h'),
            Trigram('l', 'e', 'r'),
            Trigram('a', 'v', ' '),
            Trigram('l', 'e', ' '),
            Trigram('d', 'e', 'n'),
            Trigram('a', 'n', 'd'),
            Trigram(' ', 'i', ' '),
            Trigram(' ', 'e', 'r'),
            Trigram('s', 'o', 'm'),
            Trigram(' ', 'å', ' '),
            Trigram('h', 'v', 'e'),
            Trigram('o', 'r', ' '),
            Trigram('t', ' ', 't'),
            Trigram('n', 'e', ' '),
            Trigram(' ', 'e', 'l'),
            Trigram('e', 'l', 's'),
            Trigram('r', 'e', ' '),
            Trigram(' ', 'a', 'v'),
            Trigram('s', 'e', ' '),
            Trigram('e', 's', 'k'),
            Trigram('e', 'n', 'h'),
            Trigram('n', 'g', 'e'),
            Trigram('s', 'k', 'a'),
            Trigram('n', 'd', 'e'),
            Trigram('e', ' ', 'o'),
            Trigram('e', 't', 'e'),
            Trigram('g', 'e', 'n'),
            Trigram('k', 'e', ' '),
            Trigram('l', 's', 'e'),
            Trigram('g', 'h', 'e'),
            Trigram('t', 'e', 'n'),
            Trigram('m', 'e', 'n'),
            Trigram(' ', 's', 't'),
            Trigram('r', ' ', 's'),
            Trigram('f', 'r', 'i'),
            Trigram('i', 'g', 'h'),
            Trigram('i', 'g', ' '),
            Trigram(' ', 'b', 'e'),
            Trigram('e', ' ', 'e'),
            Trigram('n', 'h', 'v'),
            Trigram('r', ' ', 'r'),
            Trigram('t', 't', 'e'),
            Trigram('s', 'k', 'e'),
            Trigram('t', 'e', ' '),
            Trigram(' ', 'p', 'å'),
            Trigram(' ', 'u', 't'),
            Trigram(' ', 's', 'k'),
            Trigram('a', 'l', ' '),
            Trigram(' ', 'i', 'n'),
            Trigram('s', 'j', 'o'),
            Trigram('p', 'å', ' '),
            Trigram('d', 'e', 'r'),
            Trigram('e', ' ', 's'),
            Trigram('n', 'e', 'r'),
            Trigram('r', 'i', 'n'),
            Trigram('j', 'o', 'n'),
            Trigram('t', ' ', 'o'),
            Trigram('u', 'n', 'n'),
            Trigram('e', ' ', 'f'),
            Trigram('h', 'a', 'n'),
            Trigram('a', 's', 'j'),
            Trigram('t', 'i', 'g'),
            Trigram('e', 'd', ' '),
            Trigram('e', 's', ' '),
            Trigram('g', ' ', 'f'),
            Trigram('s', 'a', 'm'),
            Trigram('e', 'n', 't'),
            Trigram('t', 't', 'i'),
            Trigram('e', 'n', 'e'),
            Trigram('n', 'e', 's'),
            Trigram('m', 'e', 'd'),
            Trigram('g', 'e', ' '),
            Trigram(' ', 'a', 'l'),
            Trigram('r', ' ', 'o'),
            Trigram('e', 'n', 's'),
            Trigram('r', ' ', 'e'),
            Trigram('e', 'l', 'i'),
            Trigram('i', 's', 'k'),
            Trigram('l', 'i', 'n'),
            Trigram(' ', 'v', 'e'),
            Trigram('n', 'i', 'n'),
            Trigram('g', ' ', 'o'),
            Trigram(' ', 's', 'a'),
            Trigram(' ', 'a', 'n'),
            Trigram('t', ' ', 'f'),
            Trigram('i', 't', 't'),
            Trigram('l', 'i', 'k'),
            Trigram('e', 'n', 'd'),
            Trigram('k', 'a', 'l'),
            Trigram('r', ' ', 'f'),
            Trigram('t', ' ', 's'),
            Trigram('r', 'i', 'h'),
            Trigram('i', 'h', 'e'),
            Trigram('n', 'a', 's'),
            Trigram('n', 't', 'e'),
            Trigram('e', ' ', 'r'),
            Trigram('n', 's', ' '),
            Trigram(' ', 's', 'i'),
            Trigram('l', 'a', 'n'),
            Trigram('g', ' ', 's'),
            Trigram('m', 'm', 'e'),
            Trigram('i', 'g', 'e'),
            Trigram('l', ' ', 'å'),
            Trigram('e', 'r', 'k'),
            Trigram('d', 'i', 'g'),
            Trigram(' ', 'g', 'r'),
            Trigram('n', ' ', 's'),
            Trigram('r', 'e', 'n'),
            Trigram('r', ' ', 'a'),
            Trigram('a', 'l', 'l'),
            Trigram(' ', 'n', 'a'),
            Trigram('k', 't', 'e'),
            Trigram('e', 'r', 'd'),
            Trigram('e', 'r', 'e'),
            Trigram('e', ' ', 'm'),
            Trigram('u', 'n', 'd'),
            Trigram('r', ' ', 'u'),
            Trigram('r', 'e', 's'),
            Trigram('t', 'e', 'l'),
            Trigram('s', 't', 'e'),
            Trigram('g', 'r', 'u'),
            Trigram('i', 'n', 'n'),
            Trigram('l', 'æ', 'r'),
            Trigram('e', 'r', 's'),
            Trigram(' ', 'u', 'n'),
            Trigram('d', 'e', 't'),
            Trigram('t', ' ', 'e'),
            Trigram('a', 'r', 'b'),
            Trigram('a', 'l', 'e'),
            Trigram('d', 'e', 'l'),
            Trigram('e', 'k', 't'),
            Trigram('v', 'e', 'n'),
            Trigram('t', ' ', 'i'),
            Trigram('g', ' ', 'e'),
            Trigram('b', 'e', 'i'),
            Trigram('e', 'i', 'd'),
            Trigram('e', ' ', 'a'),
            Trigram('n', ' ', 'm'),
            Trigram('e', ' ', 'd'),
            Trigram(' ', 'a', 'r'),
            Trigram('r', 'b', 'e'),
            Trigram('e', ' ', 'g'),
            Trigram(' ', 'b', 'l'),
            Trigram('a', 'n', 's'),
            Trigram('k', 'l', 'æ'),
            Trigram(' ', 'l', 'i'),
            Trigram(' ', 'h', 'e'),
            Trigram('g', ' ', 't'),
            Trigram('æ', 'r', 'i'),
            Trigram('s', 'k', 'y'),
            Trigram('r', 'u', 'n'),
            Trigram('r', 'k', 'l'),
            Trigram(' ', 'l', 'a'),
            Trigram('s', 't', 'a'),
            Trigram('s', 'n', 'i'),
            Trigram('k', 'k', 'e'),
            Trigram('m', ' ', 'e'),
            Trigram('r', 't', ' '),
            Trigram('m', 'o', 't'),
            Trigram(' ', 'm', 'o'),
            Trigram('e', ' ', 'n'),
            Trigram('t', 'a', 't'),
            Trigram('a', 't', ' '),
            Trigram('e', ' ', 'h'),
            Trigram('e', ' ', 'b'),
            Trigram('o', 'v', 'e'),
            Trigram('e', ' ', 't'),
            Trigram('j', 'e', 'n'),
            Trigram('t', ' ', 'd'),
            Trigram('s', 't', 'r'),
            Trigram(' ', 'm', 'å'),
            Trigram('r', ' ', 'm'),
            Trigram('n', ' ', 'e'),
            Trigram('o', 'r', 's'),
            Trigram('r', 'e', 'l'),
            Trigram('k', 'e', 'r'),
            Trigram(' ', 'e', 't'),
            Trigram('n', ' ', 'a'),
            Trigram('b', 'e', 's'),
            Trigram('o', 'n', 'e'),
            Trigram(' ', 'v', 'i'),
            Trigram('n', 'n', ' '),
            Trigram('g', ' ', 'r'),
            Trigram('e', ' ', 'i'),
            Trigram('k', 'a', 'p'),
            Trigram('s', 'k', ' '),
            Trigram('o', 't', ' '),
            Trigram('n', 'd', 'i'),
            Trigram('n', 'n', 'l'),
            Trigram('i', ' ', 's'),
            Trigram(' ', 'd', 'a'),
            Trigram('s', ' ', 'o'),
            Trigram(' ', 'n', 'o'),
            Trigram('i', 'd', ' '),
            Trigram('g', 'e', 'r'),
            Trigram('g', ' ', 'h'),
            Trigram('v', 'i', 's'),
            Trigram('n', ' ', 'o'),
            Trigram('b', 'a', 'r'),
            Trigram('s', ' ', 'f'),
            Trigram('n', 'd', 'l'),
            Trigram('t', ' ', 'm'),
            Trigram('g', ' ', 'a'),
            Trigram('o', 'p', 'p'),
            Trigram('t', ' ', 'a'),
            Trigram('d', 'i', 's'),
            Trigram('n', 'a', 'l'),
            Trigram('r', ' ', 'd'),
            Trigram('p', 'e', 'r'),
            Trigram('d', 'r', 'e'),
            Trigram('o', 'n', 'a'),
            Trigram('æ', 'r', 'e'),
            Trigram('r', 'd', 'i'),
            Trigram('d', 'a', ' '),
            Trigram('u', 't', 'e'),
            Trigram('n', 's', 'e'),
            Trigram('b', 'l', 'i'),
            Trigram('o', 'r', 'e'),
            Trigram('t', 'e', 't'),
            Trigram('r', 'i', 't'),
            Trigram(' ', 'o', 'p'),
            Trigram('k', 'r', 'a'),
            Trigram('e', 'r', 'i'),
            Trigram('h', 'o', 'l'),
            Trigram('o', 'l', 'd'),
            Trigram(' ', 'k', 'r'),
            Trigram('y', 't', 't'),
            Trigram('k', 'y', 't'),
            Trigram('f', 'f', 'e'),
            Trigram('e', 'm', 'm'),
            Trigram('g', ' ', 'd'),
            Trigram('l', ' ', 'f'),
            Trigram(' ', 'o', 'm'),
            Trigram('i', 's', 'n'),
            Trigram(' ', 'g', 'j'),
            Trigram('å', ' ', 'd'),
            Trigram('s', 'e', 'r'),
            Trigram('r', ' ', 'b'),
            Trigram(' ', 'd', 'i'),
            Trigram(' ', 'f', 'a'),
            Trigram('n', ' ', 't'),
            Trigram('r', ' ', 'k'),
            Trigram('l', 't', ' '),
            Trigram('s', 'e', 't'),
            Trigram(' ', 's', 'l'),
            Trigram('d', 'o', 'm'),
            Trigram('r', 'v', 'i'),
            Trigram('m', 'e', ' '),
            Trigram('l', ' ', 'e'),
            Trigram('g', 'r', 'e'),
            Trigram('å', ' ', 's'),
            Trigram('m', 'å', ' '),
            Trigram(' ', 't', 'r'),
            Trigram('n', 'd', ' '),
            Trigram('m', ' ', 's'),
            Trigram('g', ' ', 'i'),
            Trigram('i', 'k', 'k'),
            Trigram('n', ' ', 'h'),
            Trigram(' ', 'a', 't'),
            Trigram('t', 'e', 's'),
            Trigram('v', 'i', 'l'),
            Trigram('d', 'l', 'i'),
            Trigram('g', ' ', 'b'),
            Trigram('d', ' ', 'd'),
            Trigram(' ', 'h', 'v'),
            Trigram('r', 'a', 'v'),
        ],
    ),
    (
        Lang::Cat,
        &[
            Trigram(' ', 'd', 'e'),
            Trigram(' ', 'i', ' '),
            Trigram('e', 's', ' '),
            Trigram('d', 'e', ' '),
            Trigram('l', 'a', ' '),
            Trigram(' ', 'l', 'a'),
            Trigram(' ', 'a', ' '),
            Trigram(' ', 'p', 'e'),
            Trigram('p', 'e', 'r'),
            Trigram('i', 'ó', ' '),
            Trigram('e', 'n', 't'),
            Trigram('t', 'a', 't'),
            Trigram(' ', 's', 'e'),
            Trigram('n', 't', ' '),
            Trigram('r', 'e', 't'),
            Trigram('t', 's', ' '),
            Trigram('d', 'r', 'e'),
            Trigram('a', 't', ' '),
            Trigram(' ', 'e', 'l'),
            Trigram('l', 's', ' '),
            Trigram(' ', 'd', 'r'),
            Trigram('m', 'e', 'n'),
            Trigram('a', 'c', 'i'),
            Trigram('a', ' ', 'p'),
            Trigram('c', 'i', 'ó'),
            Trigram('o', 'n', 'a'),
            Trigram(' ', 'c', 'o'),
            Trigram('a', ' ', 'l'),
            Trigram('a', 'l', ' '),
            Trigram('n', 'a', ' '),
            Trigram('s', ' ', 'd'),
            Trigram('q', 'u', 'e'),
            Trigram('e', 'n', ' '),
            Trigram('e', 'l', ' '),
            Trigram(' ', 't', 'o'),
            Trigram('s', ' ', 'i'),
            Trigram(' ', 'q', 'u'),
            Trigram(' ', 'e', 'n'),
            Trigram('e', ' ', 'l'),
            Trigram('n', 's', ' '),
            Trigram('t', 'o', 't'),
            Trigram('e', 't', ' '),
            Trigram('t', ' ', 'a'),
            Trigram('e', 'r', 's'),
            Trigram(' ', 'p', 'r'),
            Trigram('t', ' ', 'd'),
            Trigram('o', 'n', 's'),
            Trigram('e', 'r', ' '),
            Trigram(' ', 'l', 'l'),
            Trigram('i', 'o', 'n'),
            Trigram('a', ' ', 's'),
            Trigram('t', 'a', ' '),
            Trigram('a', ' ', 't'),
            Trigram('c', 'o', 'n'),
            Trigram('e', 'l', 's'),
            Trigram('s', ' ', 'e'),
            Trigram(' ', 'l', '’'),
            Trigram('r', 's', 'o'),
            Trigram('r', 'e', 's'),
            Trigram('a', 'l', 's'),
            Trigram('s', 'o', 'n'),
            Trigram(' ', 'u', 'n'),
            Trigram('e', 's', 't'),
            Trigram('c', 'i', 'o'),
            Trigram(' ', 'r', 'e'),
            Trigram('p', 'r', 'o'),
            Trigram('i', 't', 'a'),
            Trigram('c', 'i', 'a'),
            Trigram(' ', 'i', 'n'),
            Trigram('l', 'e', 's'),
            Trigram(' ', 'o', ' '),
            Trigram('u', 'e', ' '),
            Trigram('d', 'e', 'l'),
            Trigram('l', 'l', 'i'),
            Trigram('t', 'é', ' '),
            Trigram(' ', 't', 'é'),
            Trigram('i', 'a', ' '),
            Trigram('a', 'm', 'e'),
            Trigram('é', ' ', 'd'),
            Trigram('s', 'e', 'v'),
            Trigram('o', 't', 'a'),
            Trigram('n', 'a', 'c'),
            Trigram('i', ' ', 'l'),
            Trigram(' ', 'a', 'l'),
            Trigram('s', ' ', 'p'),
            Trigram('a', ' ', 'd'),
            Trigram('a', 'r', ' '),
            Trigram('a', ' ', 'i'),
            Trigram('u', 'a', 'l'),
            Trigram('n', 'a', 'l'),
            Trigram('a', ' ', 'c'),
            Trigram('a', 'n', 't'),
            Trigram('n', 'c', 'i'),
            Trigram(' ', 'l', 'e'),
            Trigram('e', 'r', 't'),
            Trigram('s', 't', 'a'),
            Trigram('r', 't', 'a'),
            Trigram('s', 'e', 'r'),
            Trigram('t', ' ', 'i'),
            Trigram('i', ' ', 'a'),
            Trigram('l', ' ', 'd'),
            Trigram(' ', 'n', 'o'),
            Trigram('v', 'a', ' '),
            Trigram('a', 't', 's'),
            Trigram(' ', 'd', '’'),
            Trigram('s', ' ', 'n'),
            Trigram('r', 'e', ' '),
            Trigram('s', ' ', 'a'),
            Trigram('e', ' ', 'c'),
            Trigram('e', 'v', 'a'),
            Trigram(' ', 'n', 'a'),
            Trigram('r', 'à', ' '),
            Trigram(' ', 'c', 'a'),
            Trigram('u', 'e', 's'),
            Trigram('c', 'o', 'm'),
            Trigram('l', 'i', 'b'),
            Trigram('é', 's', ' '),
            Trigram(' ', 's', 'o'),
            Trigram('i', 'b', 'e'),
            Trigram(' ', 'e', 's'),
            Trigram('e', 't', 's'),
            Trigram('b', 'e', 'r'),
            Trigram('d', 'a', ' '),
            Trigram('r', ' ', 'a'),
            Trigram('n', 'o', ' '),
            Trigram('u', 'n', 'a'),
            Trigram('l', '’', 'e'),
            Trigram('s', ' ', 'l'),
            Trigram('t', 'e', 'r'),
            Trigram('s', 'e', 'n'),
            Trigram('r', 'a', 'n'),
            Trigram('u', 'r', 'e'),
            Trigram('d', 'e', 's'),
            Trigram('m', 'a', 'n'),
            Trigram('i', ' ', 'e'),
            Trigram('l', ' ', 'p'),
            Trigram('t', ' ', 'e'),
            Trigram('n', ' ', 'd'),
            Trigram('e', ' ', 'd'),
            Trigram('e', ' ', 'e'),
            Trigram('o', 'm', ' '),
            Trigram(' ', 'd', 'i'),
            Trigram('c', 'c', 'i'),
            Trigram('i', 'g', 'u'),
            Trigram('a', ' ', 'a'),
            Trigram('s', ' ', 't'),
            Trigram(' ', 'p', 'a'),
            Trigram('i', ' ', 'd'),
            Trigram('t', 'r', 'a'),
            Trigram('s', ' ', 'o'),
            Trigram('a', 'q', 'u'),
            Trigram('t', 'r', 'e'),
            Trigram('v', 'o', 'l'),
            Trigram('e', 'c', 't'),
            Trigram('a', ' ', 'u'),
            Trigram('l', ' ', 'i'),
            Trigram('g', 'u', 'a'),
            Trigram('i', 'd', 'e'),
            Trigram('s', ' ', 's'),
            Trigram('a', 'd', 'a'),
            Trigram('e', 'n', 'e'),
            Trigram('i', 'a', 'l'),
            Trigram('n', 't', 'a'),
            Trigram('n', 't', 'r'),
            Trigram('e', 'n', 's'),
            Trigram('s', 'o', 'c'),
            Trigram('c', 't', 'e'),
            Trigram('r', 'a', ' '),
            Trigram('o', 'c', 'i'),
            Trigram('h', 'u', 'm'),
            Trigram('u', 'm', 'a'),
            Trigram('c', 'l', 'a'),
            Trigram('a', 'l', 'i'),
            Trigram('l', 'i', 't'),
            Trigram('e', 'r', 'à'),
            Trigram('c', 't', 'i'),
            Trigram(' ', 'a', 'q'),
            Trigram(' ', 'h', 'u'),
            Trigram('i', 'c', 'i'),
            Trigram('p', 'r', 'e'),
            Trigram('e', 'r', 'a'),
            Trigram('e', 's', 's'),
            Trigram('u', 'n', 'i'),
            Trigram('n', 't', 'e'),
            Trigram(' ', 'f', 'o'),
            Trigram(' ', 'n', 'i'),
            Trigram('b', 'l', 'e'),
            Trigram('s', 's', 'e'),
            Trigram('t', 'e', 's'),
            Trigram('a', 'l', 't'),
            Trigram('e', 'm', 'e'),
            Trigram('a', 's', 's'),
            Trigram('i', 'c', 'a'),
            Trigram('s', 'e', 'g'),
            Trigram('o', ' ', 's'),
            Trigram('o', 't', 'e'),
            Trigram('r', 'a', 'c'),
            Trigram(' ', 'i', 'g'),
            Trigram(' ', 'p', 'o'),
            Trigram('a', 'n', 's'),
            Trigram(' ', 'é', 's'),
            Trigram('a', ' ', 'e'),
            Trigram('u', 'n', ' '),
            Trigram('u', 's', ' '),
            Trigram('m', 'i', 't'),
            Trigram(' ', 'm', 'a'),
            Trigram('r', ' ', 's'),
            Trigram('s', 'e', ' '),
            Trigram('s', 's', 'i'),
            Trigram('s', ' ', 'h'),
            Trigram('a', ' ', 'm'),
            Trigram('r', ' ', 'l'),
            Trigram('n', 'i', 't'),
            Trigram('l', ' ', 't'),
            Trigram('è', 'n', 'c'),
            Trigram('ó', ' ', 'd'),
            Trigram('t', 'e', 'n'),
            Trigram(' ', 't', 'e'),
            Trigram('i', 'r', ' '),
            Trigram('i', ' ', 'p'),
            Trigram('t', 'a', 'l'),
            Trigram('e', 't', 'a'),
            Trigram('d', 'i', 'c'),
            Trigram('i', ' ', 'i'),
            Trigram('h', 'o', 'm'),
            Trigram('t', ' ', 'q'),
            Trigram('p', 'a', 'r'),
            Trigram('e', 'g', 'u'),
            Trigram('s', ' ', 'f'),
            Trigram(' ', 'a', 's'),
            Trigram('n', ' ', 'l'),
            Trigram('r', 'i', 'a'),
            Trigram(' ', 'm', 'i'),
            Trigram(' ', 'a', 'c'),
            Trigram('l', 'i', 'c'),
            Trigram('i', 'n', 't'),
            Trigram(' ', 't', 'r'),
            Trigram('a', 'c', 't'),
            Trigram('e', 'i', 'x'),
            Trigram('n', ' ', 'e'),
            Trigram('s', ' ', 'c'),
            Trigram('o', 'n', 't'),
            Trigram('n', 's', 'e'),
            Trigram('e', 'c', 'c'),
            Trigram('t', ' ', 't'),
            Trigram('l', 't', 'r'),
            Trigram('a', 'm', 'b'),
            Trigram('q', 'u', 'a'),
            Trigram('l', '’', 'a'),
            Trigram('e', 'l', 'i'),
            Trigram('u', 'r', 'a'),
            Trigram('a', 'n', ' '),
            Trigram('i', 's', 't'),
            Trigram('e', ' ', 't'),
            Trigram('ó', ' ', 'a'),
            Trigram('o', 'n', 'e'),
            Trigram('n', 'a', 'm'),
            Trigram('i', 'n', 'g'),
            Trigram('l', 'a', 'r'),
            Trigram('o', ' ', 'p'),
            Trigram('e', 's', 'p'),
            Trigram('r', 'e', 'c'),
            Trigram('l', 'i', 'g'),
            Trigram('a', ' ', 'f'),
            Trigram(' ', 'h', 'a'),
            Trigram('i', 'v', 'a'),
            Trigram(' ', 'a', 'm'),
            Trigram('l', 'l', 'e'),
            Trigram('t', ' ', 's'),
            Trigram('r', 'o', 't'),
            Trigram('m', 'a', 't'),
            Trigram('l', 'i', 'u'),
            Trigram('t', 'i', 'u'),
            Trigram('i', 'u', 'r'),
            Trigram('n', ' ', 'a'),
            Trigram('f', 'o', 'n'),
            Trigram('o', 't', 's'),
            Trigram('i', 'n', 'c'),
            Trigram('n', 'd', 'i'),
            Trigram('e', ' ', 'p'),
            Trigram('s', 'e', 'u'),
            Trigram('o', 'l', 'u'),
            Trigram('g', 'u', 'r'),
            Trigram('i', ' ', 'c'),
            Trigram('m', 'é', 's'),
            Trigram('d', 'e', 'r'),
            Trigram('r', 'n', 'a'),
            Trigram('i', 'n', 'a'),
            Trigram('f', 'o', 'r'),
            Trigram('i', 'g', 'i'),
            Trigram('c', 'i', 'e'),
            Trigram('b', 'l', 'i'),
            Trigram('i', 'c', ' '),
            Trigram('m', 'b', ' '),
            Trigram('i', 'n', ' '),
            Trigram('a', 'r', 't'),
            Trigram('o', 'l', ' '),
            Trigram('r', 'o', 'm'),
            Trigram('n', 'i', 'n'),
            Trigram('o', 'm', 'p'),
        ],
    ),
    (
        Lang::Lit,
        &[
            Trigram('a', 's', ' '),
            Trigram('i', 'r', ' '),
            Trigram(' ', 'i', 'r'),
            Trigram('e', 'i', 's'),
            Trigram('t', 'e', 'i'),
            Trigram(' ', 't', 'e'),
            Trigram('s', ' ', 't'),
            Trigram('o', 's', ' '),
            Trigram('u', 'r', 'i'),
            Trigram('t', 'i', ' '),
            Trigram('u', 's', ' '),
            Trigram('i', 's', ' '),
            Trigram('i', 'e', 'k'),
            Trigram(' ', 'p', 'a'),
            Trigram('a', 'i', ' '),
            Trigram(' ', 'v', 'i'),
            Trigram('v', 'i', 'e'),
            Trigram('t', 'u', 'r'),
            Trigram(' ', 'k', 'i'),
            Trigram('r', 'i', ' '),
            Trigram('ž', 'm', 'o'),
            Trigram(' ', 't', 'u'),
            Trigram(' ', 'ž', 'm'),
            Trigram('i', 'e', 'n'),
            Trigram('ė', 's', ' '),
            Trigram('i', 'ų', ' '),
            Trigram('a', 'l', 'i'),
            Trigram('a', 'i', 's'),
            Trigram('m', 'o', 'g'),
            Trigram('v', 'i', 's'),
            Trigram(' ', 'k', 'a'),
            Trigram('l', 'a', 'i'),
            Trigram(' ', 'l', 'a'),
            Trigram('i', 'n', 'i'),
            Trigram('i', ' ', 't'),
            Trigram('s', ' ', 'i'),
            Trigram('s', ' ', 'ž'),
            Trigram('s', 'ę', ' '),
            Trigram(' ', 'į', ' '),
            Trigram('i', 's', 'ę'),
            Trigram('e', 'n', 'a'),
            Trigram(' ', 'n', 'e'),
            Trigram(' ', 'p', 'r'),
            Trigram(' ', 'b', 'ū'),
            Trigram(' ', 'j', 'o'),
            Trigram('p', 'r', 'i'),
            Trigram('k', 'i', 'e'),
            Trigram(' ', 't', 'a'),
            Trigram('k', 'v', 'i'),
            Trigram('n', 'a', 's'),
            Trigram(' ', 's', 'u'),
            Trigram('e', 'k', 'v'),
            Trigram('m', 'a', 's'),
            Trigram('g', 'u', 's'),
            Trigram('b', 'ū', 't'),
            Trigram('t', 'i', 'n'),
            Trigram('i', 's', 'v'),
            Trigram('s', ' ', 's'),
            Trigram('o', 'g', 'u'),
            Trigram('i', 's', 'i'),
            Trigram('m', 'ą', ' '),
            Trigram('m', 'o', ' '),
            Trigram('a', 'n', 't'),
            Trigram(' ', 'a', 'r'),
            Trigram('s', ' ', 'k'),
            Trigram('a', 'm', 'a'),
            Trigram('k', 'a', 'i'),
            Trigram('ū', 't', 'i'),
            Trigram('s', ' ', 'a'),
            Trigram('s', ' ', 'v'),
            Trigram('a', 'c', 'i'),
            Trigram(' ', 't', 'i'),
            Trigram('s', ' ', 'n'),
            Trigram(' ', 's', 'a'),
            Trigram('s', ' ', 'p'),
            Trigram('o', 'k', 'i'),
            Trigram('c', 'i', 'j'),
            Trigram('i', 'n', 'ė'),
            Trigram('a', 'r', ' '),
            Trigram('v', 'a', 'l'),
            Trigram('m', 's', ' '),
            Trigram('t', 'a', 'i'),
            Trigram('j', 'o', ' '),
            Trigram('i', ' ', 'b'),
            Trigram(' ', 'n', 'a'),
            Trigram('g', 'a', 'l'),
            Trigram('s', 'a', 'v'),
            Trigram('k', 'u', 'r'),
            Trigram('a', 'u', 's'),
            Trigram('m', 'e', 'n'),
            Trigram('r', 'i', 'n'),
            Trigram(' ', 'a', 'p'),
            Trigram('i', 'm', 'ą'),
            Trigram('m', 'a', ' '),
            Trigram('s', 't', 'a'),
            Trigram('ę', ' ', 'į'),
            Trigram('i', 'n', 'a'),
            Trigram('i', ' ', 'p'),
            Trigram('i', 'm', 'o'),
            Trigram('n', 'i', 'm'),
            Trigram('i', ' ', 'k'),
            Trigram(' ', 'n', 'u'),
            Trigram('i', 'm', 'a'),
            Trigram('o', 't', 'i'),
            Trigram('m', 'i', 's'),
            Trigram(' ', 'k', 'u'),
            Trigram('j', 'o', 's'),
            Trigram('l', 'y', 'g'),
            Trigram('d', 'a', 'r'),
            Trigram('i', 'š', 'k'),
            Trigram('j', 'e', ' '),
            Trigram(' ', 'a', 't'),
            Trigram('t', 'a', 's'),
            Trigram('k', 'a', 'd'),
            Trigram('r', ' ', 't'),
            Trigram('t', 'ų', ' '),
            Trigram('a', 'd', ' '),
            Trigram('t', 'i', 'k'),
            Trigram('i', ' ', 'i'),
            Trigram('n', 'ė', 's'),
            Trigram('a', 'r', 'b'),
            Trigram('i', ' ', 'v'),
            Trigram('i', 'j', 'o'),
            Trigram('e', 'i', 'k'),
            Trigram('a', 'u', 't'),
            Trigram('s', ' ', 'b'),
            Trigram(' ', 'į', 's'),
            Trigram(' ', 'r', 'e'),
            Trigram('i', 'a', 'm'),
            Trigram('s', 'i', 'n'),
            Trigram('s', 'u', 'o'),
            Trigram(' ', 'b', 'e'),
            Trigram('i', 's', 'u'),
            Trigram(' ', 'v', 'a'),
            Trigram('l', 'i', ' '),
            Trigram('s', 't', 'y'),
            Trigram('a', 's', 'i'),
            Trigram('t', 'i', 'e'),
            Trigram('a', 'r', 'a'),
            Trigram('l', 'i', 'n'),
            Trigram('i', 's', 'ė'),
            Trigram('i', ' ', 's'),
            Trigram('ą', ' ', 'i'),
            Trigram('j', 'ų', ' '),
            Trigram(' ', 'l', 'y'),
            Trigram(' ', 'g', 'a'),
            Trigram('v', 'o', ' '),
            Trigram('s', 'i', ' '),
            Trigram('r', ' ', 'p'),
            Trigram('t', 'u', 'o'),
            Trigram('a', 'i', 'k'),
            Trigram('r', 'i', 'e'),
            Trigram(' ', 'm', 'o'),
            Trigram('d', 'i', 'n'),
            Trigram('p', 'a', 's'),
            Trigram('m', 'o', 'k'),
            Trigram('i', 'p', ' '),
            Trigram('i', ' ', 'n'),
            Trigram('r', 'e', 'i'),
            Trigram('y', 'b', 'ė'),
            Trigram('m', 'o', 's'),
            Trigram('a', 'i', 'p'),
            Trigram('r', ' ', 'l'),
            Trigram('n', 't', 'u'),
            Trigram('į', 's', 't'),
            Trigram('į', ' ', 't'),
            Trigram('g', 'y', 'v'),
            Trigram(' ', 'i', 'š'),
            Trigram('n', 't', 'i'),
            Trigram('t', 'y', 'b'),
            Trigram('ų', ' ', 'i'),
            Trigram('p', 'a', 'g'),
            Trigram('k', 'i', 'a'),
            Trigram('k', 'i', 't'),
            Trigram('e', 's', ' '),
            Trigram('u', 'o', 't'),
            Trigram(' ', 's', 'k'),
            Trigram('j', 'i', 'm'),
            Trigram('t', 'i', 's'),
            Trigram(' ', 'o', 'r'),
            Trigram('a', 'u', 'd'),
            Trigram('y', 'v', 'e'),
            Trigram('v', 'e', 'n'),
            Trigram('m', 'ų', ' '),
            Trigram('a', 'l', 's'),
            Trigram('ų', ' ', 't'),
            Trigram('n', 'a', 'c'),
            Trigram('a', 'v', 'o'),
            Trigram('d', 'a', 'm'),
            Trigram('ą', ' ', 'k'),
            Trigram('i', ' ', 'a'),
            Trigram('s', ' ', 'j'),
            Trigram('o', 'j', 'e'),
            Trigram('a', 'g', 'r'),
            Trigram('k', 'l', 'a'),
            Trigram('g', 'a', 'u'),
            Trigram('n', 'e', 'g'),
            Trigram('n', 'i', 'ų'),
            Trigram('o', ' ', 'k'),
            Trigram('e', 'g', 'a'),
            Trigram('i', 'k', 'i'),
            Trigram('a', 'u', 'g'),
            Trigram('e', 'k', ' '),
            Trigram('t', 'a', 't'),
            Trigram('i', 'e', 'š'),
            Trigram('t', 'a', 'r'),
            Trigram('i', 'a', ' '),
            Trigram(' ', 'š', 'i'),
            Trigram('i', 'o', 's'),
            Trigram('š', 'k', 'a'),
            Trigram('s', 'v', 'a'),
            Trigram(' ', 't', 'o'),
            Trigram('t', 'a', 'u'),
            Trigram('i', 'n', 't'),
            Trigram('s', 'a', 'u'),
            Trigram('u', 't', 'i'),
            Trigram(' ', 'a', 's'),
            Trigram('i', 'o', ' '),
            Trigram('o', 'g', 'a'),
            Trigram('s', 'a', 'n'),
            Trigram('m', 'o', 'n'),
            Trigram('o', 'm', 'i'),
            Trigram('k', 'i', 'n'),
            Trigram('i', 't', 'o'),
            Trigram('s', ' ', 'g'),
            Trigram('o', 'm', 'e'),
            Trigram('r', ' ', 'j'),
            Trigram(' ', 'v', 'e'),
            Trigram('a', 't', 'y'),
            Trigram('k', 'i', 'm'),
            Trigram('n', 't', ' '),
            Trigram('i', 'a', 'i'),
            Trigram('l', 's', 't'),
            Trigram(' ', 'd', 'a'),
            Trigram('j', 'ą', ' '),
            Trigram('m', 'i', 'n'),
            Trigram('r', ' ', 'k'),
            Trigram('o', ' ', 't'),
            Trigram('n', 'u', 'o'),
            Trigram('t', 'u', ' '),
            Trigram('v', 'e', 'r'),
            Trigram('k', 'a', 'l'),
            Trigram('a', 'm', ' '),
            Trigram('u', 's', 'i'),
            Trigram('o', ' ', 'n'),
            Trigram('o', ' ', 'a'),
            Trigram('y', 'm', 'o'),
            Trigram('t', 'y', 'm'),
            Trigram('v', 'ę', ' '),
            Trigram('a', 't', 'i'),
            Trigram(' ', 'j', 'i'),
            Trigram('o', ' ', 'p'),
            Trigram('t', 'i', 'm'),
            Trigram('ų', ' ', 'n'),
            Trigram('p', 'a', 'ž'),
            Trigram('t', 'e', 'r'),
            Trigram('s', ' ', 'š'),
            Trigram(' ', 'v', 'y'),
            Trigram('a', 'l', 't'),
            Trigram('k', 's', 'l'),
            Trigram('i', 'n', 'g'),
            Trigram('ų', ' ', 's'),
            Trigram('o', 'm', 'a'),
            Trigram('š', 'a', 'l'),
            Trigram('r', 'a', 'n'),
            Trigram('e', ' ', 't'),
            Trigram(' ', 'n', 'i'),
            Trigram(' ', 'š', 'a'),
            Trigram('a', 'v', 'a'),
            Trigram('a', 'v', 'i'),
            Trigram('n', 'i', 'e'),
            Trigram('u', 'o', 'm'),
            Trigram('i', 'r', 't'),
            Trigram('e', 'l', 'g'),
            Trigram('j', 'a', 'm'),
            Trigram('i', 'p', 'a'),
            Trigram('k', 'i', 'ų'),
            Trigram('t', 'o', 'k'),
            Trigram('e', 'k', 'a'),
            Trigram('t', 'o', 's'),
            Trigram('o', 'j', 'a'),
            Trigram('k', 'i', 'o'),
            Trigram('e', 'n', 'y'),
            Trigram('n', 'a', 'm'),
            Trigram('s', ' ', 'd'),
            Trigram('n', 'd', 'i'),
            Trigram('a', 'm', 'o'),
            Trigram('y', 't', 'i'),
            Trigram('g', 'r', 'i'),
            Trigram('s', 'v', 'ę'),
            Trigram(' ', 'g', 'y'),
            Trigram('l', 'i', 'e'),
            Trigram('ė', 'm', 'i'),
            Trigram('a', 't', 's'),
            Trigram('y', 'g', 'i'),
            Trigram('s', 'o', 'c'),
            Trigram('s', 'i', 'e'),
            Trigram('o', 'c', 'i'),
            Trigram('p', 'a', 't'),
            Trigram('c', 'i', 'a'),
        ],
    ),
    (
        Lang::Slv,
        &[
            Trigram(' ', 'p', 'r'),
            Trigram('i', 'n', ' '),
            Trigram(' ', 'i', 'n'),
            Trigram('r', 'a', 'v'),
            Trigram('p', 'r', 'a'),
            Trigram('d', 'o', ' '),
            Trigram('a', 'n', 'j'),
            Trigram('t', 'i', ' '),
            Trigram('a', 'v', 'i'),
            Trigram('j', 'e', ' '),
            Trigram('n', 'j', 'e'),
            Trigram('n', 'o', ' '),
            Trigram('v', 'i', 'c'),
            Trigram(' ', 'd', 'o'),
            Trigram('i', 'h', ' '),
            Trigram(' ', 'p', 'o'),
            Trigram('l', 'i', ' '),
            Trigram('o', ' ', 'd'),
            Trigram(' ', 'z', 'a'),
            Trigram(' ', 'v', 's'),
            Trigram('o', 's', 't'),
            Trigram('a', ' ', 'p'),
            Trigram('e', 'g', 'a'),
            Trigram('o', ' ', 'i'),
            Trigram('n', 'e', ' '),
            Trigram(' ', 'd', 'r'),
            Trigram(' ', 'n', 'a'),
            Trigram(' ', 'v', ' '),
            Trigram('g', 'a', ' '),
            Trigram(' ', 's', 'v'),
            Trigram('j', 'a', ' '),
            Trigram('v', 'a', 'n'),
            Trigram('s', 'v', 'o'),
            Trigram('a', 'k', 'o'),
            Trigram('p', 'r', 'i'),
            Trigram('c', 'o', ' '),
            Trigram('i', 'c', 'o'),
            Trigram('i', ' ', 's'),
            Trigram('e', ' ', 's'),
            Trigram('o', ' ', 'p'),
            Trigram(' ', 'k', 'a'),
            Trigram('a', 'l', 'i'),
            Trigram('s', 't', 'v'),
            Trigram('s', 't', 'i'),
            Trigram('v', 's', 'a'),
            Trigram(' ', 'n', 'e'),
            Trigram(' ', 'i', 'm'),
            Trigram('s', 'a', 'k'),
            Trigram('i', 'm', 'a'),
            Trigram('j', 'o', ' '),
            Trigram('d', 'r', 'u'),
            Trigram('n', 'o', 's'),
            Trigram('k', 'd', 'o'),
            Trigram('i', ' ', 'd'),
            Trigram('a', 'k', 'd'),
            Trigram('i', ' ', 'p'),
            Trigram('n', 'j', 'a'),
            Trigram('o', ' ', 's'),
            Trigram('n', 'i', 'h'),
            Trigram(' ', 'a', 'l'),
            Trigram('o', ' ', 'v'),
            Trigram('m', 'a', ' '),
            Trigram('i', ' ', 'i'),
            Trigram(' ', 'd', 'e'),
            Trigram('e', ' ', 'n'),
            Trigram('p', 'r', 'e'),
            Trigram('v', 'o', ' '),
            Trigram('i', ' ', 'v'),
            Trigram('n', 'i', ' '),
            Trigram('r', 'e', 'd'),
            Trigram('o', 'b', 'o'),
            Trigram('v', 'o', 'b'),
            Trigram('a', 'v', 'n'),
            Trigram('n', 'e', 'g'),
            Trigram(' ', 'b', 'i'),
            Trigram('o', 'v', 'a'),
            Trigram(' ', 'i', 'z'),
            Trigram('o', 'v', 'e'),
            Trigram('i', 't', 'i'),
            Trigram('l', 'o', 'v'),
            Trigram('k', 'i', ' '),
            Trigram('j', 'a', 'n'),
            Trigram('a', ' ', 'v'),
            Trigram('n', 'a', ' '),
            Trigram(' ', 's', 'o'),
            Trigram('e', 'm', ' '),
            Trigram(' ', 'n', 'j'),
            Trigram('a', ' ', 'i'),
            Trigram('s', 'e', ' '),
            Trigram(' ', 't', 'e'),
            Trigram('t', 'v', 'a'),
            Trigram('o', 'l', 'i'),
            Trigram('b', 'o', 'd'),
            Trigram('r', 'u', 'ž'),
            Trigram('e', ' ', 'i'),
            Trigram(' ', 'r', 'a'),
            Trigram(' ', 's', 'k'),
            Trigram('a', 't', 'i'),
            Trigram('e', ' ', 'p'),
            Trigram('a', 'r', 'o'),
            Trigram('i', ' ', 'k'),
            Trigram(' ', 'o', 'b'),
            Trigram('a', ' ', 'd'),
            Trigram(' ', 'č', 'l'),
            Trigram('e', 'v', 'a'),
            Trigram('r', 'ž', 'a'),
            Trigram('d', 'r', 'ž'),
            Trigram(' ', 's', 'p'),
            Trigram('k', 'o', ' '),
            Trigram('i', ' ', 'n'),
            Trigram(' ', 's', 'e'),
            Trigram(' ', 'k', 'i'),
            Trigram('e', 'n', 'a'),
            Trigram('s', 't', 'o'),
            Trigram('e', ' ', 'v'),
            Trigram('ž', 'e', 'n'),
            Trigram('n', 'a', 'k'),
            Trigram('k', 'a', 'k'),
            Trigram('i', ' ', 'z'),
            Trigram('v', 'a', 'r'),
            Trigram('t', 'e', 'r'),
            Trigram('ž', 'a', 'v'),
            Trigram(' ', 'm', 'o'),
            Trigram('d', 'i', ' '),
            Trigram('g', 'o', 'v'),
            Trigram('i', 'm', 'i'),
            Trigram('v', 'a', ' '),
            Trigram('k', 'o', 'l'),
            Trigram('n', ' ', 's'),
            Trigram(' ', 'z', ' '),
            Trigram('m', 'i', ' '),
            Trigram('o', 'v', 'o'),
            Trigram('r', 'o', 'd'),
            Trigram('v', 'o', 'j'),
            Trigram(' ', 'e', 'n'),
            Trigram('n', 'a', 'r'),
            Trigram('v', 'e', ' '),
            Trigram(' ', 'j', 'e'),
            Trigram('p', 'o', 's'),
            Trigram('a', ' ', 's'),
            Trigram('e', 'g', 'o'),
            Trigram('v', 'l', 'j'),
            Trigram('j', 'e', 'g'),
            Trigram(' ', 's', 't'),
            Trigram('h', ' ', 'p'),
            Trigram('e', 'r', ' '),
            Trigram('k', 'a', 't'),
            Trigram('č', 'l', 'o'),
            Trigram('a', 't', 'e'),
            Trigram('a', ' ', 'z'),
            Trigram('e', 'n', 'j'),
            Trigram('n', ' ', 'p'),
            Trigram('d', 'e', 'l'),
            Trigram('i', ' ', 'o'),
            Trigram('l', 'j', 'a'),
            Trigram('p', 'o', 'l'),
            Trigram('č', 'i', 'n'),
            Trigram('a', ' ', 'n'),
            Trigram('e', 'd', ' '),
            Trigram('s', 'm', 'e'),
            Trigram('j', 'e', 'n'),
            Trigram('e', 'n', 'i'),
            Trigram(' ', 't', 'a'),
            Trigram('o', 'd', 'n'),
            Trigram(' ', 'v', 'e'),
            Trigram(' ', 'n', 'i'),
            Trigram('e', ' ', 'b'),
            Trigram('e', 'n', ' '),
            Trigram(' ', 'm', 'e'),
            Trigram('j', 'e', 'm'),
            Trigram('k', 'o', 'n'),
            Trigram('n', 'a', 'n'),
            Trigram('e', 'l', 'j'),
            Trigram('s', 'a', 'm'),
            Trigram('d', 'a', ' '),
            Trigram('l', 'j', 'e'),
            Trigram('z', 'a', 'k'),
            Trigram('o', 'v', 'i'),
            Trigram('š', 'č', 'i'),
            Trigram('r', 'a', 'z'),
            Trigram('a', 'n', 's'),
            Trigram('j', 'u', ' '),
            Trigram('b', 'i', 't'),
            Trigram('i', 'c', ' '),
            Trigram(' ', 's', 'm'),
            Trigram('j', 'i', ' '),
            Trigram('n', 's', 'k'),
            Trigram('v', ' ', 's'),
            Trigram(' ', 's', ' '),
            Trigram('n', ' ', 'v'),
            Trigram('t', 'v', 'o'),
            Trigram('e', 'n', 'e'),
            Trigram('a', ' ', 'k'),
            Trigram('m', 'e', ' '),
            Trigram('v', 'a', 't'),
            Trigram('o', 'r', 'a'),
            Trigram('k', 'r', 'š'),
            Trigram('n', 'i', 'm'),
            Trigram('s', 't', 'a'),
            Trigram('ž', 'i', 'v'),
            Trigram('e', 'b', 'n'),
            Trigram('e', 'v', ' '),
            Trigram('r', 'i', ' '),
            Trigram('e', 'k', 'o'),
            Trigram('o', ' ', 'k'),
            Trigram('n', ' ', 'n'),
            Trigram('s', 'o', ' '),
            Trigram('z', 'a', ' '),
            Trigram('i', 'č', 'n'),
            Trigram('s', 'k', 'i'),
            Trigram('e', ' ', 'd'),
            Trigram(' ', 'v', 'a'),
            Trigram('o', ' ', 'z'),
            Trigram('a', 'c', 'i'),
            Trigram('c', 'i', 'j'),
            Trigram('e', 'j', 'a'),
            Trigram('e', 'l', 'o'),
            Trigram('d', 'e', 'j'),
            Trigram('s', 'i', ' '),
            Trigram('n', 'j', 'u'),
            Trigram('v', 'o', 'l'),
            Trigram('k', 'i', 'h'),
            Trigram('i', ' ', 'm'),
            Trigram('n', 's', 't'),
            Trigram('k', 'u', 'p'),
            Trigram('k', 'o', 'v'),
            Trigram('u', 'ž', 'i'),
            Trigram('l', 'a', ' '),
            Trigram('m', 'o', 'r'),
            Trigram('v', 'i', 'h'),
            Trigram(' ', 'd', 'a'),
            Trigram('h', ' ', 'i'),
            Trigram('l', 'j', 'u'),
            Trigram('o', 't', 'r'),
            Trigram('m', 'e', 'd'),
            Trigram('o', ' ', 'a'),
            Trigram('s', 'k', 'u'),
            Trigram('r', 'u', 'g'),
            Trigram('o', 'd', 'o'),
            Trigram('i', 'j', 'o'),
            Trigram('d', 's', 't'),
            Trigram('s', 'p', 'o'),
            Trigram('t', 'a', 'k'),
            Trigram('z', 'n', 'a'),
            Trigram('e', 'd', 'n'),
            Trigram('v', 'n', 'e'),
            Trigram('a', 'r', 'a'),
            Trigram('r', 'š', 'n'),
            Trigram('i', 't', 'v'),
            Trigram('o', 'd', 'i'),
            Trigram('u', ' ', 's'),
            Trigram('č', 'e', 'n'),
            Trigram('b', 'o', 'š'),
            Trigram('n', 'i', 'k'),
            Trigram('a', 'v', 'l'),
            Trigram('a', 'k', 'r'),
            Trigram('e', ' ', 'o'),
            Trigram('v', 'e', 'k'),
            Trigram('d', 'n', 'o'),
            Trigram('o', 'l', 'n'),
            Trigram('o', ' ', 'o'),
            Trigram('o', 'š', 'č'),
            Trigram('e', ' ', 'm'),
            Trigram('t', 'a', ' '),
            Trigram('v', 'i', 'č'),
            Trigram('b', 'i', ' '),
            Trigram('p', 'n', 'o'),
            Trigram('č', 'n', 'o'),
            Trigram('m', 'e', 'l'),
            Trigram('e', 'm', 'e'),
            Trigram('o', 'l', 'j'),
            Trigram('o', 'd', 'e'),
            Trigram('r', 's', 't'),
            Trigram('r', 'e', 'm'),
            Trigram('o', 'v', ' '),
            Trigram('a', 'r', 's'),
            Trigram(' ', 'b', 'o'),
            Trigram('n', ' ', 'd'),
            Trigram('e', 'r', 'e'),
            Trigram('d', 'o', 'v'),
            Trigram('a', 'j', 'o'),
            Trigram('k', 'l', 'a'),
            Trigram('i', 'c', 'e'),
            Trigram('v', 'e', 'z'),
            Trigram('v', 'n', 'i'),
            Trigram(' ', 'k', 'o'),
            Trigram('o', 's', 'e'),
            Trigram('t', 'e', 'v'),
            Trigram('b', 'n', 'o'),
            Trigram('u', 'ž', 'b'),
            Trigram('a', 'v', 'a'),
            Trigram('v', 'e', 'r'),
            Trigram('e', ' ', 'z'),
            Trigram('l', 'j', 'n'),
            Trigram('m', 'u', ' '),
            Trigram('a', ' ', 'b'),
            Trigram('v', 'i', ' '),
            Trigram('d', 'o', 'l'),
            Trigram('k', 'e', 'r'),
            Trigram('r', ' ', 's'),
        ],
    ),
    (
        Lang::Epo,
        &[
            Trigram('a', 'j', ' '),
            Trigram(' ', 'l', 'a'),
            Trigram('l', 'a', ' '),
            Trigram('k', 'a', 'j'),
            Trigram(' ', 'k', 'a'),
            Trigram('o', 'j', ' '),
            Trigram(' ', 'd', 'e'),
            Trigram('o', 'n', ' '),
            Trigram('d', 'e', ' '),
            Trigram('r', 'a', 'j'),
            Trigram(' ', 'r', 'a'),
            Trigram('i', 'u', ' '),
            Trigram('a', 'j', 't'),
            Trigram('a', 's', ' '),
            Trigram('o', ' ', 'k'),
            Trigram(' ', 'ĉ', 'i'),
            Trigram('e', ' ', 'l'),
            Trigram('j', ' ', 'k'),
            Trigram(' ', 'l', 'i'),
            Trigram(' ', 'p', 'r'),
            Trigram('e', 'c', 'o'),
            Trigram('a', 'ŭ', ' '),
            Trigram('ĉ', 'i', 'u'),
            Trigram('j', 'n', ' '),
            Trigram('i', 'a', ' '),
            Trigram('j', 't', 'o'),
            Trigram('e', 's', 't'),
            Trigram(' ', 'e', 's'),
            Trigram(' ', 'a', 'l'),
            Trigram('a', 'n', ' '),
            Trigram(' ', 'k', 'i'),
            Trigram('p', 'r', 'o'),
            Trigram('i', 'o', ' '),
            Trigram(' ', 'k', 'o'),
            Trigram('e', 'n', ' '),
            Trigram('n', ' ', 'k'),
            Trigram('k', 'o', 'n'),
            Trigram(' ', 't', 'i'),
            Trigram('c', 'o', ' '),
            Trigram('j', ' ', 'p'),
            Trigram('o', ' ', 'd'),
            Trigram(' ', 'p', 'o'),
            Trigram('i', 'b', 'e'),
            Trigram(' ', 'a', 'ŭ'),
            Trigram('r', 'o', ' '),
            Trigram('t', 'a', 's'),
            Trigram('l', 'i', 'b'),
            Trigram('b', 'e', 'r'),
            Trigram('a', 'c', 'i'),
            Trigram('t', 'o', 'j'),
            Trigram(' ', 'e', 'n'),
            Trigram('a', ' ', 'p'),
            Trigram(' ', 'n', 'e'),
            Trigram('c', 'i', 'o'),
            Trigram('e', 'r', 'e'),
            Trigram('t', 'a', ' '),
            Trigram(' ', 'i', 'n'),
            Trigram('t', 'o', ' '),
            Trigram('d', 'o', ' '),
            Trigram('o', ' ', 'e'),
            Trigram('j', ' ', 'l'),
            Trigram('n', ' ', 'a'),
            Trigram('j', ' ', 'd'),
            Trigram(' ', 's', 'e'),
            Trigram('a', ' ', 'k'),
            Trigram('j', ' ', 'r'),
            Trigram('a', 'l', 'a'),
            Trigram('j', ' ', 'e'),
            Trigram('t', 'a', 'j'),
            Trigram(' ', 'r', 'e'),
            Trigram('r', 'e', 'c'),
            Trigram('i', 'u', 'j'),
            Trigram('k', 'i', 'u'),
            Trigram(' ', 'p', 'e'),
            Trigram('o', ' ', 'a'),
            Trigram('i', 't', 'a'),
            Trigram('a', 'j', 'n'),
            Trigram('a', 'd', 'o'),
            Trigram('n', ' ', 'd'),
            Trigram('s', 't', 'a'),
            Trigram('n', 'a', 'c'),
            Trigram('a', ' ', 'a'),
            Trigram('n', 't', 'a'),
            Trigram('l', 'i', 'a'),
            Trigram('e', 'k', 't'),
            Trigram('e', 'n', 'i'),
            Trigram('i', 'a', 'j'),
            Trigram('t', 'e', 'r'),
            Trigram('u', 'j', ' '),
            Trigram('p', 'e', 'r'),
            Trigram('t', 'o', 'n'),
            Trigram('i', 'n', 't'),
            Trigram(' ', 's', 'i'),
            Trigram('c', 'i', 'a'),
            Trigram(' ', 'h', 'a'),
            Trigram('s', 't', 'u'),
            Trigram('a', ' ', 'l'),
            Trigram('j', 'e', ' '),
            Trigram(' ', 'j', 'e'),
            Trigram('a', 'l', ' '),
            Trigram('o', ' ', 'ĉ'),
            Trigram('n', ' ', 'p'),
            Trigram('j', 't', 'a'),
            Trigram('t', 'u', ' '),
            Trigram(' ', 'r', 'i'),
            Trigram('v', 'a', 's'),
            Trigram('s', 'e', 'n'),
            Trigram('h', 'a', 'v'),
            Trigram('h', 'o', 'm'),
            Trigram(' ', 'd', 'i'),
            Trigram(' ', 'h', 'o'),
            Trigram('n', 't', 'e'),
            Trigram('a', ' ', 'e'),
            Trigram('a', 'l', 'i'),
            Trigram('e', 'n', 't'),
            Trigram(' ', 's', 'o'),
            Trigram('n', 'e', 'c'),
            Trigram('t', 'r', 'a'),
            Trigram('a', ' ', 's'),
            Trigram('a', 'v', 'a'),
            Trigram('p', 'o', 'r'),
            Trigram('a', ' ', 'r'),
            Trigram(' ', 'n', 'a'),
            Trigram('i', 'g', 'i'),
            Trigram('t', 'i', 'u'),
            Trigram('s', 'i', 'a'),
            Trigram('o', ' ', 'p'),
            Trigram('n', ' ', 'l'),
            Trigram('e', 'g', 'a'),
            Trigram('o', 'r', ' '),
            Trigram(' ', 'a', 'j'),
            Trigram('s', 'o', 'c'),
            Trigram('j', ' ', 'ĉ'),
            Trigram('s', ' ', 'l'),
            Trigram('o', 'c', 'i'),
            Trigram('n', 'o', ' '),
            Trigram(' ', 'p', 'l'),
            Trigram('j', ' ', 'n'),
            Trigram('k', 't', 'o'),
            Trigram('e', 'v', 'i'),
            Trigram('s', ' ', 'r'),
            Trigram('j', ' ', 's'),
            Trigram('o', 'j', 'n'),
            Trigram('l', 'a', 'j'),
            Trigram('u', ' ', 'a'),
            Trigram('r', 'e', ' '),
            Trigram(' ', 'e', 'g'),
            Trigram('j', ' ', 'a'),
            Trigram('g', 'a', 'l'),
            Trigram('e', 'r', 's'),
            Trigram('k', 'e', ' '),
            Trigram('p', 'r', 'e'),
            Trigram('i', 'g', 'o'),
            Trigram('e', 'r', ' '),
            Trigram('l', 'a', 'n'),
            Trigram('n', ' ', 'j'),
            Trigram('p', 'r', 'i'),
            Trigram(' ', 'k', 'u'),
            Trigram('e', 'r', 'a'),
            Trigram('i', 'a', 'n'),
            Trigram('r', 'i', 'm'),
            Trigram(' ', 'f', 'a'),
            Trigram('e', ' ', 's'),
            Trigram(' ', 'j', 'u'),
            Trigram('e', ' ', 'a'),
            Trigram('i', 'k', 'a'),
            Trigram('a', 't', 'a'),
            Trigram('n', 't', 'r'),
            Trigram('e', 'l', ' '),
            Trigram('i', 's', ' '),
            Trigram('u', ' ', 'h'),
            Trigram('l', 'i', ' '),
            Trigram('i', 'o', 'j'),
            Trigram('d', 'o', 'n'),
            Trigram('o', 'n', 't'),
            Trigram('t', 'a', 't'),
            Trigram('o', 'n', 's'),
            Trigram(' ', 'e', 'l'),
            Trigram(' ', 's', 'u'),
            Trigram('g', 'o', ' '),
            Trigram('u', 'n', ' '),
            Trigram(' ', 'k', 'e'),
            Trigram('e', 'b', 'l'),
            Trigram('b', 'l', 'a'),
            Trigram('n', ' ', 's'),
            Trigram('o', 'm', 'a'),
            Trigram('ĉ', 'i', ' '),
            Trigram('r', 'a', 'ŭ'),
            Trigram('k', 'l', 'a'),
            Trigram('u', ' ', 'r'),
            Trigram('n', 'e', ' '),
            Trigram('i', 'l', 'i'),
            Trigram('i', 'ĝ', 'o'),
            Trigram('o', ' ', 't'),
            Trigram('s', ' ', 'e'),
            Trigram('t', 'e', 'k'),
            Trigram('m', 'e', 'n'),
            Trigram('n', 'e', 'n'),
            Trigram('j', ' ', 'i'),
            Trigram('n', 'd', 'a'),
            Trigram('c', 'o', 'n'),
            Trigram('a', ' ', 'd'),
            Trigram('e', 'n', 'a'),
            Trigram('c', 'e', 'v'),
            Trigram('m', 'o', 'j'),
            Trigram('i', 'c', 'e'),
            Trigram('r', 'i', 'c'),
            Trigram('p', 'l', 'e'),
            Trigram('s', 'o', 'n'),
            Trigram('a', 'r', 't'),
            Trigram('a', ' ', 'h'),
            Trigram('o', ' ', 'r'),
            Trigram('r', 'e', 's'),
            Trigram(' ', 'u', 'n'),
            Trigram('u', ' ', 's'),
            Trigram('c', 'o', 'j'),
            Trigram('e', ' ', 'p'),
            Trigram('ĝ', 'i', ' '),
            Trigram('f', 'o', 'r'),
            Trigram('a', 't', 'o'),
            Trigram('r', 'e', 'n'),
            Trigram('a', 'r', 'a'),
            Trigram('a', 'm', 'e'),
            Trigram('t', 'a', 'n'),
            Trigram(' ', 'p', 'u'),
            Trigram('o', 't', 'e'),
            Trigram('r', 'o', 't'),
            Trigram(' ', 'm', 'a'),
            Trigram('v', 'i', ' '),
            Trigram('j', ' ', 'f'),
            Trigram('l', 'e', 'n'),
            Trigram('d', 'i', 's'),
            Trigram('i', 'v', 'e'),
            Trigram('a', 'n', 't'),
            Trigram('n', ' ', 'r'),
            Trigram(' ', 'v', 'i'),
            Trigram('a', 'm', 'i'),
            Trigram('i', 'ĝ', 'i'),
            Trigram('s', 't', 'i'),
            Trigram('ĝ', 'o', ' '),
            Trigram('r', ' ', 'l'),
            Trigram('n', ' ', 'ĉ'),
            Trigram('u', ' ', 'l'),
            Trigram(' ', 'a', 'g'),
            Trigram('e', 'r', 'v'),
            Trigram('u', ' ', 'e'),
            Trigram('u', 'n', 'u'),
            Trigram('g', 'n', 'o'),
            Trigram(' ', 'c', 'e'),
            Trigram(' ', 'm', 'e'),
            Trigram('n', 'i', 'u'),
            Trigram('i', 'e', 'l'),
            Trigram('d', 'u', 'k'),
            Trigram('e', 'r', 'n'),
            Trigram(' ', 'ŝ', 't'),
            Trigram('l', 'a', 'ŭ'),
            Trigram('o', ' ', 'n'),
            Trigram('l', 'a', 'b'),
            Trigram('o', 'l', 'o'),
            Trigram('a', 'b', 'o'),
            Trigram('t', 'i', 'o'),
            Trigram('b', 'o', 'r'),
            Trigram('ŝ', 't', 'a'),
            Trigram('i', 'm', 'i'),
            Trigram(' ', 'e', 'd'),
            Trigram('l', 'o', ' '),
            Trigram('k', 'u', 'n'),
            Trigram('e', 'd', 'u'),
            Trigram('k', 'o', 'm'),
            Trigram('d', 'e', 'v'),
            Trigram('e', 'n', 'c'),
            Trigram('n', 'd', 'o'),
            Trigram('l', 'i', 'g'),
            Trigram('e', ' ', 'e'),
            Trigram('a', ' ', 'f'),
            Trigram('t', 'i', 'g'),
            Trigram('i', ' ', 'e'),
            Trigram(' ', 'k', 'r'),
            Trigram(' ', 'p', 'a'),
            Trigram('n', 'a', ' '),
            Trigram('n', ' ', 'i'),
            Trigram('k', 'a', 'd'),
            Trigram('a', 'n', 'd'),
            Trigram('e', ' ', 'd'),
            Trigram('m', 'a', 'l'),
            Trigram('o', 'n', 'o'),
            Trigram('d', 'e', 'k'),
            Trigram('p', 'o', 'l'),
            Trigram('o', 'r', 'o'),
            Trigram('e', 'r', 'i'),
            Trigram('e', 'd', 'o'),
            Trigram('e', ' ', 'k'),
            Trigram('r', 's', 'o'),
            Trigram('t', 'i', ' '),
            Trigram('r', 'a', 'c'),
            Trigram('i', 'o', 'n'),
            Trigram('l', 'o', 'j'),
            Trigram('j', ' ', 'h'),
            Trigram('p', 'l', 'i'),
            Trigram('j', ' ', 'm'),
        ],
    ),
    (
        Lang::Lav,
        &[
            Trigram('a', 's', ' '),
            Trigram('ī', 'b', 'a'),
            Trigram(' ', 'u', 'n'),
            Trigram('u', 'n', ' '),
            Trigram('t', 'i', 'e'),
            Trigram('i', 'e', 's'),
            Trigram('b', 'a', 's'),
            Trigram('a', 'i', ' '),
            Trigram(' ', 't', 'i'),
            Trigram('e', 's', 'ī'),
            Trigram('s', 'ī', 'b'),
            Trigram('i', 'e', 'n'),
            Trigram(' ', 'v', 'i'),
            Trigram('b', 'u', ' '),
            Trigram('v', 'i', 'e'),
            Trigram('i', 'r', ' '),
            Trigram(' ', 'i', 'r'),
            Trigram('ī', 'b', 'u'),
            Trigram('i', 'e', 'm'),
            Trigram(' ', 'v', 'a'),
            Trigram(' ', 'p', 'a'),
            Trigram('e', 'm', ' '),
            Trigram(' ', 'n', 'e'),
            Trigram('s', ' ', 'u'),
            Trigram('a', 'm', ' '),
            Trigram('m', ' ', 'i'),
            Trigram('š', 'a', 'n'),
            Trigram('u', ' ', 'u'),
            Trigram('r', ' ', 't'),
            Trigram('p', 'i', 'e'),
            Trigram(' ', 'c', 'i'),
            Trigram(' ', 's', 'a'),
            Trigram('ā', 's', ' '),
            Trigram(' ', 'u', 'z'),
            Trigram('v', 'a', 'i'),
            Trigram(' ', 'k', 'a'),
            Trigram(' ', 'p', 'i'),
            Trigram('b', 'r', 'ī'),
            Trigram(' ', 'i', 'z'),
            Trigram('r', 'ī', 'v'),
            Trigram(' ', 'b', 'r'),
            Trigram('u', 'z', ' '),
            Trigram('c', 'i', 'j'),
            Trigram('d', 'z', 'ī'),
            Trigram('e', 'n', 'a'),
            Trigram(' ', 'a', 'r'),
            Trigram('a', 'r', ' '),
            Trigram('i', 's', 'k'),
            Trigram('s', ' ', 'p'),
            Trigram('e', 's', ' '),
            Trigram(' ', 'a', 't'),
            Trigram('ā', 'c', 'i'),
            Trigram(' ', 'a', 'p'),
            Trigram('o', 't', ' '),
            Trigram('n', 'a', 'm'),
            Trigram('v', 'i', 'ņ'),
            Trigram('i', 'n', 'ā'),
            Trigram('i', 'k', 'v'),
            Trigram('k', 'v', 'i'),
            Trigram(' ', 'n', 'o'),
            Trigram('s', ' ', 'v'),
            Trigram(' ', 'i', 'e'),
            Trigram('v', 'i', 's'),
            Trigram(' ', 'i', 'k'),
            Trigram('i', ' ', 'i'),
            Trigram('p', 'ā', 'r'),
            Trigram('u', ' ', 'a'),
            Trigram('j', 'u', ' '),
            Trigram('n', 'u', ' '),
            Trigram(' ', 'p', 'r'),
            Trigram('e', 'd', 'r'),
            Trigram('v', 'ī', 'b'),
            Trigram('ī', 'v', 'ī'),
            Trigram('i', 'j', 'u'),
            Trigram('d', 'r', 'ī'),
            Trigram('u', ' ', 'p'),
            Trigram('d', 'a', 'r'),
            Trigram(' ', 's', 't'),
            Trigram('l', 'v', 'ē'),
            Trigram('c', 'i', 'l'),
            Trigram('i', 'l', 'v'),
            Trigram('s', ' ', 't'),
            Trigram(' ', 'l', 'a'),
            Trigram('i', 'ņ', 'a'),
            Trigram('a', 'n', 'a'),
            Trigram('s', ' ', 'i'),
            Trigram('n', ' ', 'i'),
            Trigram('ī', 'd', 'z'),
            Trigram('s', ' ', 's'),
            Trigram('k', 'ā', ' '),
            Trigram('t', 'ī', 'b'),
            Trigram('i', ' ', 'a'),
            Trigram('i', 'j', 'a'),
            Trigram('b', 'a', 'i'),
            Trigram('ī', 'b', 'ā'),
            Trigram('i', 'e', 'd'),
            Trigram('s', ' ', 'n'),
            Trigram('a', 'r', 'b'),
            Trigram('v', 'a', 'l'),
            Trigram('l', 'ī', 'd'),
            Trigram('s', ' ', 'b'),
            Trigram('a', 'i', 'z'),
            Trigram('t', 'u', ' '),
            Trigram('i', 'e', 'c'),
            Trigram('c', 'i', 'e'),
            Trigram('ā', 'm', ' '),
            Trigram('g', 'u', ' '),
            Trigram('v', 'ē', 'k'),
            Trigram('ī', 'g', 'u'),
            Trigram('ī', 'g', 'i'),
            Trigram('k', 'a', ' '),
            Trigram('j', 'a', 's'),
            Trigram('u', 'm', 'u'),
            Trigram('m', 'u', ' '),
            Trigram('t', ' ', 'p'),
            Trigram(' ', 'j', 'ā'),
            Trigram('u', ' ', 'v'),
            Trigram('z', 'ī', 'b'),
            Trigram('s', 'k', 'a'),
            Trigram('l', 's', 't'),
            Trigram('a', 'l', 's'),
            Trigram('k', 'u', 'm'),
            Trigram('g', 'i', ' '),
            Trigram('s', ' ', 'l'),
            Trigram(' ', 't', 'ā'),
            Trigram('j', 'o', 't'),
            Trigram('s', 't', 'ā'),
            Trigram('s', 't', ' '),
            Trigram('n', ' ', 'v'),
            Trigram('v', 'ē', 'r'),
            Trigram('a', ' ', 'p'),
            Trigram('a', 'r', 'ī'),
            Trigram('a', 'u', 't'),
            Trigram('n', ' ', 'p'),
            Trigram('a', 'm', 'a'),
            Trigram('k', 'a', 's'),
            Trigram('u', ' ', 'k'),
            Trigram(' ', 'd', 'a'),
            Trigram(' ', 't', 'a'),
            Trigram('n', 'ī', 'g'),
            Trigram('i', 'z', 's'),
            Trigram('o', 'j', 'o'),
            Trigram('a', 'n', 'u'),
            Trigram('ņ', 'a', ' '),
            Trigram('u', ' ', 'n'),
            Trigram('s', 't', 'a'),
            Trigram('s', ' ', 'a'),
            Trigram('b', 'a', ' '),
            Trigram(' ', 'a', 'i'),
            Trigram(' ', 's', 'o'),
            Trigram('s', ' ', 'd'),
            Trigram('a', ' ', 'u'),
            Trigram('ā', ' ', 'a'),
            Trigram('s', 't', 'ī'),
            Trigram('c', 'ī', 'b'),
            Trigram('m', ' ', 'u'),
            Trigram('i', ' ', 'u'),
            Trigram('s', 'o', 'n'),
            Trigram('n', 'o', 't'),
            Trigram('m', 'a', 't'),
            Trigram('s', 'a', 'v'),
            Trigram('i', 'e', 'v'),
            Trigram('ā', ' ', 'v'),
            Trigram('j', 'u', 'm'),
            Trigram(' ', 'k', 'ā'),
            Trigram('u', ' ', 't'),
            Trigram('n', 'e', 'd'),
            Trigram('a', 'j', 'ā'),
            Trigram('s', ' ', 'k'),
            Trigram('u', ' ', 'i'),
            Trigram('i', ' ', 'v'),
            Trigram('l', 'ī', 't'),
            Trigram('ē', 'r', 'o'),
            Trigram(' ', 'p', 'e'),
            Trigram(' ', 'd', 'z'),
            Trigram('i', ' ', 'n'),
            Trigram('p', 'e', 'r'),
            Trigram('u', ' ', 'd'),
            Trigram('ī', 'k', 's'),
            Trigram('k', 'a', 't'),
            Trigram('n', 'ā', 't'),
            Trigram('l', 'ī', 'b'),
            Trigram('n', 'ā', 'c'),
            Trigram('r', 'd', 'z'),
            Trigram('n', 'ī', 'b'),
            Trigram('p', 'i', 'l'),
            Trigram('r', 'ī', 'k'),
            Trigram('k', 's', 't'),
            Trigram('a', ' ', 's'),
            Trigram('c', 'i', 't'),
            Trigram('p', 'a', 'm'),
            Trigram(' ', 'p', 'ā'),
            Trigram('e', 'k', 'l'),
            Trigram('t', 'a', 'u'),
            Trigram('u', ' ', 's'),
            Trigram('b', 'i', 'e'),
            Trigram('j', 'ā', ' '),
            Trigram(' ', 'r', 'e'),
            Trigram('i', ' ', 'p'),
            Trigram('k', 'u', 'r'),
            Trigram('a', ' ', 'a'),
            Trigram('t', ' ', 'v'),
            Trigram(' ', 'l', 'i'),
            Trigram('e', 'v', 'i'),
            Trigram('t', 'i', 's'),
            Trigram('e', 'v', 'ē'),
            Trigram('b', 'ā', ' '),
            Trigram('m', 'a', ' '),
            Trigram('r', 'ī', 'b'),
            Trigram('a', ' ', 'v'),
            Trigram('o', 's', ' '),
            Trigram('r', 'a', 's'),
            Trigram('a', 'b', 'i'),
            Trigram('n', 'e', 'v'),
            Trigram('i', 'k', 'u'),
            Trigram('s', 'k', 'ā'),
            Trigram(' ', 'v', 'e'),
            Trigram('l', 'i', 'k'),
            Trigram(' ', 'l', 'ī'),
            Trigram('n', 'a', 's'),
            Trigram('t', ' ', 'k'),
            Trigram('a', 'n', 't'),
            Trigram('u', 'm', 'a'),
            Trigram('r', 'o', 'š'),
            Trigram('k', 'ā', 'd'),
            Trigram('z', 's', 'a'),
            Trigram('s', 'a', 'r'),
            Trigram('c', 'i', 'ā'),
            Trigram('m', 'i', 'e'),
            Trigram('a', 'i', 's'),
            Trigram('e', 'c', 'i'),
            Trigram('o', 'c', 'i'),
            Trigram('o', 'š', 'a'),
            Trigram(' ', 'j', 'e'),
            Trigram('j', 'e', 'b'),
            Trigram('b', 'ū', 't'),
            Trigram('a', 't', 'r'),
            Trigram('n', ' ', 'b'),
            Trigram('i', 'e', 'š'),
            Trigram('r', 's', 'o'),
            Trigram('e', 'r', 's'),
            Trigram('s', 'o', 'c'),
            Trigram('e', 'n', 'ā'),
            Trigram('a', ' ', 't'),
            Trigram('t', ' ', 's'),
            Trigram('ī', 'š', 'a'),
            Trigram(' ', 'b', 'e'),
            Trigram('b', 'e', 'z'),
            Trigram('ā', 'd', 'a'),
            Trigram('e', 'b', 'k'),
            Trigram(' ', 'k', 'u'),
            Trigram('g', 'l', 'ī'),
            Trigram('i', 's', 'p'),
            Trigram('t', 'o', 't'),
            Trigram('s', 'p', 'ā'),
            Trigram('r', 'o', 'j'),
            Trigram('l', 'i', 'e'),
            Trigram('p', 'r', 'e'),
            Trigram('r', 'e', 't'),
            Trigram('a', 'u', 'l'),
            Trigram('n', 'a', ' '),
            Trigram('t', 'r', 'a'),
            Trigram('i', 'e', 't'),
            Trigram('d', 'u', ' '),
            Trigram('z', 'g', 'l'),
            Trigram('ā', 't', ' '),
            Trigram('a', 'r', 'd'),
            Trigram('k', 't', ' '),
            Trigram('i', 'e', 'r'),
            Trigram('i', 'z', 'g'),
            Trigram('i', 'k', 't'),
            Trigram('p', 'a', 'š'),
            Trigram('i', 'ā', 'l'),
            Trigram('n', 'o', 'd'),
            Trigram('t', 's', ' '),
            Trigram('e', 'j', 'a'),
            Trigram('ā', ' ', 'u'),
            Trigram('s', 'a', 'b'),
            Trigram('e', 'n', 'o'),
            Trigram('ē', 't', ' '),
            Trigram('t', 'a', ' '),
            Trigram('t', 'i', 'k'),
            Trigram('t', 'ī', 't'),
            Trigram('e', 'c', 'ī'),
            Trigram(' ', 'd', 'e'),
            Trigram('ī', 'g', 'a'),
            Trigram('t', 'a', 'r'),
            Trigram('a', 'r', 'p'),
            Trigram('r', ' ', 'j'),
            Trigram('ī', 's', 't'),
            Trigram('t', 'ā', 's'),
            Trigram('j', 'a', ' '),
            Trigram('e', 'n', 'ī'),
            Trigram('a', 't', 'v'),
            Trigram('v', 'u', ' '),
            Trigram('ā', 'r', 'ē'),
            Trigram('r', 'ē', 'j'),
            Trigram('r', 'i', 'e'),
            Trigram('o', 'š', 'i'),
            Trigram('d', 'r', 'o'),
        ],
    ),
    (
        Lang::Est,
        &[
            Trigram('s', 'e', 'l'),
            Trigram('j', 'a', ' '),
            Trigram(' ', 'j', 'a'),
            Trigram('l', 'e', ' '),
            Trigram('s', 'e', ' '),
            Trigram('u', 's', 't'),
            Trigram('s', 't', 'e'),
            Trigram('u', 's', 'e'),
            Trigram('i', 's', 'e'),
            Trigram('õ', 'i', 'g'),
            Trigram('m', 'i', 's'),
            Trigram(' ', 'v', 'a'),
            Trigram('g', 'u', 's'),
            Trigram('e', 'l', 'e'),
            Trigram('t', 'e', ' '),
            Trigram('i', 'g', 'u'),
            Trigram('u', 's', ' '),
            Trigram('s', 't', ' '),
            Trigram('d', 'u', 's'),
            Trigram(' ', 'õ', 'i'),
            Trigram(' ', 'v', 'õ'),
            Trigram(' ', 'o', 'n'),
            Trigram('o', 'n', ' '),
            Trigram('e', ' ', 'j'),
            Trigram(' ', 'i', 'n'),
            Trigram('i', 'n', 'i'),
            Trigram('n', 'i', 'm'),
            Trigram('m', 'a', ' '),
            Trigram('e', 'l', ' '),
            Trigram('a', ' ', 'v'),
            Trigram('i', 'g', 'a'),
            Trigram('i', 's', 't'),
            Trigram('i', 'm', 'e'),
            Trigram('a', 'l', ' '),
            Trigram('v', 'õ', 'i'),
            Trigram('d', 'a', ' '),
            Trigram(' ', 't', 'e'),
            Trigram('l', 'i', 'k'),
            Trigram(' ', 'i', 'g'),
            Trigram('a', 'd', 'u'),
            Trigram('m', 'e', 's'),
            Trigram('a', 'm', 'i'),
            Trigram('e', 'n', 'd'),
            Trigram('e', ' ', 'k'),
            Trigram('e', ' ', 'v'),
            Trigram('l', ' ', 'o'),
            Trigram(' ', 'k', 'a'),
            Trigram('e', 's', 't'),
            Trigram(' ', 'r', 'a'),
            Trigram(' ', 's', 'e'),
            Trigram('õ', 'i', ' '),
            Trigram('i', 'k', 'u'),
            Trigram(' ', 'k', 'o'),
            Trigram('v', 'a', 'b'),
            Trigram('a', 'b', 'a'),
            Trigram('t', 'u', 's'),
            Trigram('u', 'd', ' '),
            Trigram('a', ' ', 'k'),
            Trigram('e', 's', 'e'),
            Trigram(' ', 'k', 'u'),
            Trigram('l', ' ', 'i'),
            Trigram('g', 'a', 'l'),
            Trigram('t', 's', 'i'),
            Trigram('l', 't', ' '),
            Trigram('e', 's', ' '),
            Trigram('e', 'm', 'a'),
            Trigram('i', 'd', 'a'),
            Trigram('k', 's', ' '),
            Trigram('a', ' ', 'i'),
            Trigram('n', ' ', 'õ'),
            Trigram('l', 'i', 's'),
            Trigram('a', 't', 'u'),
            Trigram('r', 'a', 'h'),
            Trigram('t', 'a', 'm'),
            Trigram('a', 's', 't'),
            Trigram('s', 't', 'a'),
            Trigram('e', ' ', 't'),
            Trigram('s', ' ', 's'),
            Trigram(' ', 'm', 'i'),
            Trigram('t', 'a', ' '),
            Trigram('o', 'l', 'e'),
            Trigram('s', 't', 'u'),
            Trigram('b', 'a', 'd'),
            Trigram('g', 'a', ' '),
            Trigram('v', 'a', 'l'),
            Trigram('i', 'n', 'e'),
            Trigram(' ', 't', 'a'),
            Trigram('n', 'e', ' '),
            Trigram(' ', 'p', 'e'),
            Trigram('n', 'd', 'a'),
            Trigram('e', 'l', 'l'),
            Trigram('a', ' ', 't'),
            Trigram('a', 'l', 'i'),
            Trigram('a', 'v', 'a'),
            Trigram('a', 'd', 'a'),
            Trigram('a', ' ', 'p'),
            Trigram('i', 'k', ' '),
            Trigram('k', 'u', 's'),
            Trigram('e', ' ', 's'),
            Trigram('i', 'o', 'o'),
            Trigram('t', 'e', 's'),
            Trigram('a', 'h', 'e'),
            Trigram('i', 'n', 'g'),
            Trigram('l', 'u', 's'),
            Trigram(' ', 'o', 'l'),
            Trigram('a', ' ', 'a'),
            Trigram('i', 's', ' '),
            Trigram('v', 'a', 'h'),
            Trigram('a', ' ', 's'),
            Trigram('e', 'i', ' '),
            Trigram(' ', 'e', 'i'),
            Trigram('k', 'o', 'n'),
            Trigram('v', 'a', 's'),
            Trigram('t', 'u', 'd'),
            Trigram('a', 'h', 'v'),
            Trigram('t', ' ', 'k'),
            Trigram('a', 's', ' '),
            Trigram('a', ' ', 'r'),
            Trigram('s', ' ', 't'),
            Trigram('e', ' ', 'e'),
            Trigram('i', ' ', 'v'),
            Trigram('e', 'k', 's'),
            Trigram('o', 'o', 'n'),
            Trigram('t', ' ', 'v'),
            Trigram('o', 'n', 'i'),
            Trigram('k', 'õ', 'i'),
            Trigram('s', ' ', 'k'),
            Trigram('s', 'i', 'o'),
            Trigram('s', 'u', 's'),
            Trigram('e', ' ', 'a'),
            Trigram('g', 'i', ' '),
            Trigram('m', 'a', 't'),
            Trigram('m', 'i', 'n'),
            Trigram(' ', 'p', 'i'),
            Trigram('s', ' ', 'v'),
            Trigram('o', 'm', 'a'),
            Trigram('k', 'u', 'l'),
            Trigram('d', 'a', 'd'),
            Trigram(' ', 'n', 'i'),
            Trigram('e', ' ', 'p'),
            Trigram(' ', 'o', 'm'),
            Trigram('i', 'g', 'i'),
            Trigram('t', 'e', 'l'),
            Trigram('a', ' ', 'j'),
            Trigram('e', ' ', 'o'),
            Trigram('n', 'd', 'u'),
            Trigram('d', 's', 'e'),
            Trigram('l', 'l', 'e'),
            Trigram('e', 'e', 's'),
            Trigram('t', 's', 'e'),
            Trigram('u', 't', 'a'),
            Trigram('v', 'u', 's'),
            Trigram('a', 'a', 'l'),
            Trigram('a', 'j', 'a'),
            Trigram('i', ' ', 't'),
            Trigram('d', 'a', 'm'),
            Trigram('a', 't', 's'),
            Trigram('n', 'i', ' '),
            Trigram('e', 't', 'e'),
            Trigram('p', 'i', 'd'),
            Trigram('p', 'e', 'a'),
            Trigram('e', ' ', 'õ'),
            Trigram('i', 't', 's'),
            Trigram('l', 'm', 'a'),
            Trigram('l', 'e', 'v'),
            Trigram('n', 'i', 's'),
            Trigram('d', 'i', 's'),
            Trigram('ü', 'h', 'i'),
            Trigram('s', 'l', 'i'),
            Trigram('i', ' ', 's'),
            Trigram('n', 'e', 'n'),
            Trigram('i', 'e', 'l'),
            Trigram('d', 'e', 's'),
            Trigram('d', 'e', ' '),
            Trigram('t', ' ', 'i'),
            Trigram('e', 't', ' '),
            Trigram('n', 'i', 'n'),
            Trigram('e', 'v', 'a'),
            Trigram('t', 'e', 'g'),
            Trigram('u', 's', 'l'),
            Trigram('e', 'l', 't'),
            Trigram('i', 'l', 'i'),
            Trigram('i', ' ', 'm'),
            Trigram('n', 'g', ' '),
            Trigram(' ', 'e', 'e'),
            Trigram('t', 'e', 'm'),
            Trigram('s', 'e', 's'),
            Trigram('i', 'l', 'm'),
            Trigram('s', 'e', 'k'),
            Trigram('a', 'b', ' '),
            Trigram(' ', 'p', 'õ'),
            Trigram('a', 'i', 't'),
            Trigram(' ', 'n', 'e'),
            Trigram('õ', 'r', 'd'),
            Trigram('s', 'e', 'd'),
            Trigram('v', 'õ', 'r'),
            Trigram('u', 'l', ' '),
            Trigram(' ', 'ü', 'h'),
            Trigram(' ', 'k', 'i'),
            Trigram('a', 'b', 'i'),
            Trigram(' ', 'k', 'õ'),
            Trigram('e', 'g', 'a'),
            Trigram('r', 'd', 's'),
            Trigram(' ', 'v', 'ä'),
            Trigram('o', 't', 's'),
            Trigram(' ', 'e', 't'),
            Trigram(' ', 'r', 'i'),
            Trigram('p', 'õ', 'h'),
            Trigram('e', 'd', ' '),
            Trigram('t', 'ö', 'ö'),
            Trigram('s', 'i', ' '),
            Trigram('a', 'd', ' '),
            Trigram('i', ' ', 'k'),
            Trigram(' ', 't', 'ä'),
            Trigram('a', 't', 'a'),
            Trigram(' ', 'a', 'b'),
            Trigram(' ', 's', 'u'),
            Trigram('e', 'l', 'i'),
            Trigram(' ', 's', 'a'),
            Trigram('s', ' ', 'o'),
            Trigram('s', ' ', 'j'),
            Trigram('s', 'i', 'l'),
            Trigram('n', 'n', 'i'),
            Trigram('a', 'r', 'i'),
            Trigram('a', 's', 'u'),
            Trigram('n', 'n', 'a'),
            Trigram(' ', 'a', 'l'),
            Trigram('n', 'u', 'd'),
            Trigram('u', 'm', 'a'),
            Trigram('s', 'i', 'k'),
            Trigram('h', 'v', 'u'),
            Trigram('o', 'n', 'n'),
            Trigram('e', 'a', 'b'),
            Trigram('e', 'm', 'i'),
            Trigram('r', 'i', 'd'),
            Trigram('a', 'r', 'a'),
            Trigram('s', 'e', 't'),
            Trigram('e', ' ', 'm'),
            Trigram(' ', 'k', 'e'),
            Trigram('a', ' ', 'e'),
            Trigram('t', 'ä', 'i'),
            Trigram('d', ' ', 'k'),
            Trigram('s', ' ', 'p'),
            Trigram('i', ' ', 'e'),
            Trigram('i', 'm', 'i'),
            Trigram('e', 'i', 's'),
            Trigram('e', ' ', 'r'),
            Trigram('n', 'a', ' '),
            Trigram(' ', 'ü', 'l'),
            Trigram('a', ' ', 'ü'),
            Trigram('k', 'o', 'h'),
            Trigram('a', ' ', 'o'),
            Trigram('a', 'k', 's'),
            Trigram('s', ' ', 'e'),
            Trigram('e', ' ', 'n'),
            Trigram(' ', 's', 'o'),
            Trigram('õ', 'i', 'k'),
            Trigram('s', 'a', 'a'),
            Trigram('a', 'n', 'd'),
            Trigram('i', 's', 'i'),
            Trigram('n', 'd', 'e'),
            Trigram('t', 'u', 'm'),
            Trigram('h', 'e', 'l'),
            Trigram('l', 'i', 'i'),
            Trigram('k', 'i', 'n'),
            Trigram('ä', 'ä', 'r'),
            Trigram('s', 'e', 'a'),
            Trigram('i', 's', 'k'),
            Trigram('e', 'e', 'n'),
            Trigram('e', 'a', 'd'),
            Trigram('d', 'u', 'm'),
            Trigram(' ', 'k', 'ä'),
            Trigram('r', 'i', 'i'),
            Trigram('r', 'a', 't'),
            Trigram('l', 'e', 'm'),
            Trigram('u', 'm', 'i'),
            Trigram('k', 'o', 'r'),
            Trigram('s', 'a', ' '),
            Trigram('i', 'd', 'u'),
            Trigram('m', 'u', 's'),
            Trigram('r', 'i', 't'),
            Trigram('h', 'a', 'r'),
            Trigram(' ', 's', 'i'),
            Trigram('v', 'a', 'd'),
            Trigram('i', 't', 'a'),
            Trigram('a', 'l', 'e'),
            Trigram('k', 'a', 'i'),
            Trigram('t', 'e', 'o'),
            Trigram(' ', 'm', 'õ'),
            Trigram('a', 'd', 'e'),
            Trigram('ü', 'k', 's'),
            Trigram('m', 'a', 's'),
            Trigram('l', 's', 'e'),
            Trigram('a', 'l', 's'),
            Trigram('i', 'a', 'a'),
            Trigram('s', 'i', 'a'),
            Trigram('s', 'o', 't'),
            Trigram('j', 'a', 'l'),
            Trigram('i', 'i', 'g'),
            Trigram('i', 't', 'e'),
        ],
    ),
    (
        Lang::Lat,
        &[
            Trigram('i', 's', ' '),
            Trigram('e', 't', ' '),
            Trigram('u', 's', ' '),
            Trigram('u', 'm', ' '),
            Trigram(' ', 'e', 't'),
            Trigram('a', 'e', ' '),
            Trigram('t', 'a', 't'),
            Trigram('a', 't', 'i'),
            Trigram(' ', 'c', 'o'),
            Trigram('q', 'u', 'e'),
            Trigram('u', 'e', ' '),
            Trigram('i', 'o', 'n'),
            Trigram(' ', 'q', 'u'),
            Trigram('e', 'm', ' '),
            Trigram('e', 'n', 't'),
            Trigram('o', 'n', 'i'),
            Trigram('e', 's', 't'),
            Trigram(' ', 's', 'u'),
            Trigram(' ', 'i', 'u'),
            Trigram(' ', 'i', 'n'),
            Trigram(' ', 'p', 'o'),
            Trigram('t', 'i', 'o'),
            Trigram('t', 'e', 's'),
            Trigram('t', 'i', 's'),
            Trigram('a', 't', 'e'),
            Trigram('b', 'u', 's'),
            Trigram('e', ' ', 'i'),
            Trigram('i', 't', 'a'),
            Trigram('i', 'b', 'u'),
            Trigram('i', 'u', 'm'),
            Trigram('i', 'u', 's'),
            Trigram('q', 'u', 'i'),
            Trigram('n', 't', 'i'),
            Trigram('e', 'r', 'i'),
            Trigram('e', 's', ' '),
            Trigram('s', ' ', 'p'),
            Trigram('c', 'o', 'n'),
            Trigram('s', ' ', 'e'),
            Trigram('p', 'e', 'r'),
            Trigram('e', 'n', 'd'),
            Trigram('p', 'o', 't'),
            Trigram('o', 't', 'e'),
            Trigram(' ', 'h', 'a'),
            Trigram('n', 'i', 's'),
            Trigram(' ', 'p', 'r'),
            Trigram('s', ' ', 'i'),
            Trigram('a', 'b', 'e'),
            Trigram('u', 'i', 's'),
            Trigram('a', 'm', ' '),
            Trigram('u', 'a', 'e'),
            Trigram('t', 'e', 'm'),
            Trigram('h', 'a', 'b'),
            Trigram('b', 'e', 't'),
            Trigram('m', ' ', 'h'),
            Trigram('n', 'd', 'i'),
            Trigram(' ', 'h', 'o'),
            Trigram('s', 't', 'a'),
            Trigram(' ', 'd', 'e'),
            Trigram('s', 'u', 'a'),
            Trigram('i', 's', 'q'),
            Trigram('s', 'q', 'u'),
            Trigram('t', 'e', 'r'),
            Trigram('i', 'c', 'i'),
            Trigram('m', 'i', 'n'),
            Trigram('i', 'u', 'r'),
            Trigram('o', 'n', 'e'),
            Trigram(' ', 'r', 'e'),
            Trigram('h', 'o', 'm'),
            Trigram(' ', 'd', 'i'),
            Trigram(' ', 'o', 'm'),
            Trigram('o', 'm', 'n'),
            Trigram('r', 'u', 'm'),
            Trigram('s', ' ', 'a'),
            Trigram('t', ' ', 'c'),
            Trigram('r', 'a', 't'),
            Trigram('l', 'i', 'b'),
            Trigram('i', 'b', 'e'),
            Trigram('m', ' ', 'e'),
            Trigram(' ', 'p', 'e'),
            Trigram('g', 'e', 'n'),
            Trigram(' ', 'l', 'i'),
            Trigram('e', 'r', 't'),
            Trigram('i', 'n', 'e'),
            Trigram('n', 't', 'e'),
            Trigram('n', 'e', 'm'),
            Trigram('r', 'i', ' '),
            Trigram('b', 'e', 'r'),
            Trigram('t', 'i', 'a'),
            Trigram('e', ' ', 'q'),
            Trigram('d', 'i', 's'),
            Trigram(' ', 'i', 'p'),
            Trigram('i', 'p', 's'),
            Trigram(' ', 'a', 'd'),
            Trigram('d', 'i', ' '),
            Trigram('n', 'e', 's'),
            Trigram('e', ' ', 's'),
            Trigram('e', ' ', 'c'),
            Trigram('m', ' ', 'p'),
            Trigram('s', ' ', 'c'),
            Trigram(' ', 'v', 'e'),
            Trigram('e', ' ', 'p'),
            Trigram(' ', 'p', 'a'),
            Trigram('i', 'l', 'i'),
            Trigram(' ', 'g', 'e'),
            Trigram('a', ' ', 'e'),
            Trigram('i', ' ', 'p'),
            Trigram('n', 't', ' '),
            Trigram('o', 'm', 'i'),
            Trigram('a', 't', 'u'),
            Trigram('t', 'u', 'r'),
            Trigram('r', 'i', 't'),
            Trigram(' ', 's', 'i'),
            Trigram('n', 'e', ' '),
            Trigram('p', 's', 'i'),
            Trigram('i', 'n', ' '),
            Trigram('i', 'a', ' '),
            Trigram('r', 'a', ' '),
            Trigram('a', 'r', 'i'),
            Trigram(' ', 'c', 'u'),
            Trigram('v', 'i', 't'),
            Trigram('r', 't', 'a'),
            Trigram('m', 'o', ' '),
            Trigram('t', 'o', ' '),
            Trigram('m', 'n', 'i'),
            Trigram('s', ' ', 'h'),
            Trigram('e', ' ', 'e'),
            Trigram('i', 'n', 't'),
            Trigram('s', 'i', 'u'),
            Trigram('m', ' ', 'c'),
            Trigram('q', 'u', 'a'),
            Trigram('t', ' ', 'p'),
            Trigram('i', 'v', 'i'),
            Trigram('i', 'n', 'i'),
            Trigram('u', 't', ' '),
            Trigram('r', 'e', ' '),
            Trigram('e', 'r', 's'),
            Trigram('i', 't', ' '),
            Trigram('s', ' ', 's'),
            Trigram('i', 'a', 'e'),
            Trigram(' ', 'e', 's'),
            Trigram('t', ' ', 's'),
            Trigram('a', 'n', 'd'),
            Trigram(' ', 'n', 'e'),
            Trigram('p', 'r', 'o'),
            Trigram(' ', 'n', 'u'),
            Trigram('s', 't', ' '),
            Trigram(' ', 'e', 'x'),
            Trigram('n', 'd', 'a'),
            Trigram('c', 'i', 'e'),
            Trigram('n', 'i', 'b'),
            Trigram('t', ' ', 'a'),
            Trigram('e', 'r', 'e'),
            Trigram('t', 'r', 'i'),
            Trigram('n', 'i', 't'),
            Trigram(' ', 'a', 't'),
            Trigram('t', 'i', 'u'),
            Trigram('t', 'a', ' '),
            Trigram('r', 'i', 's'),
            Trigram(' ', 'c', 'i'),
            Trigram('c', 'i', 'v'),
            Trigram('n', 'i', ' '),
            Trigram('u', 'r', 'i'),
            Trigram('u', 'r', ' '),
            Trigram('r', 'i', 'm'),
            Trigram(' ', 'v', 'i'),
            Trigram('p', 'a', 'r'),
            Trigram('a', 'd', ' '),
            Trigram('e', 's', 's'),
            Trigram('l', 'i', 'c'),
            Trigram('i', ' ', 'i'),
            Trigram(' ', 's', 'o'),
            Trigram(' ', 'p', 'u'),
            Trigram(' ', 'o', 'p'),
            Trigram('r', 'a', 'e'),
            Trigram(' ', 'f', 'a'),
            Trigram('s', ' ', 'v'),
            Trigram(' ', 'u', 't'),
            Trigram('d', 'e', 'm'),
            Trigram('s', 'e', ' '),
            Trigram('o', 'n', 's'),
            Trigram('o', ' ', 'e'),
            Trigram('r', 'i', 'a'),
            Trigram(' ', 's', 'e'),
            Trigram('e', ' ', 'a'),
            Trigram(' ', 'm', 'o'),
            Trigram('l', 'e', 'g'),
            Trigram('a', 't', 'q'),
            Trigram('t', 'q', 'u'),
            Trigram('c', 'o', 'm'),
            Trigram('t', 'e', ' '),
            Trigram('n', 'i', 'u'),
            Trigram('i', 'e', 'n'),
            Trigram('v', 'e', 'l'),
            Trigram('e', 'l', ' '),
            Trigram(' ', 'm', 'a'),
            Trigram('t', ' ', 'e'),
            Trigram('i', 'i', 's'),
            Trigram('g', 'n', 'i'),
            Trigram('e', 'q', 'u'),
            Trigram('o', 'c', 'i'),
            Trigram('c', 'i', 'p'),
            Trigram('u', 'r', 'a'),
            Trigram('u', 'n', 't'),
            Trigram('s', ' ', 'd'),
            Trigram('t', ' ', 'i'),
            Trigram('a', 'l', 'i'),
            Trigram('q', 'u', 'o'),
            Trigram('e', 'c', 't'),
            Trigram(' ', 't', 'e'),
            Trigram('a', ' ', 's'),
            Trigram('t', ' ', 'd'),
            Trigram(' ', 'd', 'o'),
            Trigram('t', 'u', 't'),
            Trigram('a', 'n', 't'),
            Trigram('i', 's', 'c'),
            Trigram('i', 'n', 'a'),
            Trigram('m', 'e', 'n'),
            Trigram('s', 'i', 'n'),
            Trigram('u', 'a', ' '),
            Trigram('p', 'r', 'a'),
            Trigram('o', 'r', 'u'),
            Trigram('o', 'm', 'm'),
            Trigram('e', 't', 'a'),
            Trigram('s', ' ', 'n'),
            Trigram('a', ' ', 'p'),
            Trigram('t', 'u', 'm'),
            Trigram('i', 'a', 'm'),
            Trigram('i', 'o', ' '),
            Trigram('i', ' ', 'c'),
            Trigram('s', 't', 'i'),
            Trigram(' ', 'a', 'u'),
            Trigram('v', 'e', 'r'),
            Trigram(' ', 'a', 'e'),
            Trigram('i', 't', 'o'),
            Trigram('d', 'i', 'c'),
            Trigram('i', 'm', 'i'),
            Trigram('s', ' ', 'l'),
            Trigram('e', ' ', 'd'),
            Trigram('f', 'i', 'c'),
            Trigram('c', 'i', 'a'),
            Trigram('t', ' ', 'o'),
            Trigram('p', 'u', 'b'),
            Trigram('u', 'b', 'l'),
            Trigram('b', 'l', 'i'),
            Trigram('m', 'u', 'n'),
            Trigram('i', ' ', 's'),
            Trigram('s', 'o', 'c'),
            Trigram('a', 'r', 'u'),
            Trigram('l', 'a', 'r'),
            Trigram('u', 'l', 'l'),
            Trigram('o', 'r', 'i'),
            Trigram('t', ' ', 'h'),
            Trigram('i', ' ', 'e'),
            Trigram('s', 's', 'e'),
            Trigram('o', 'm', 'o'),
            Trigram('c', 't', 'o'),
            Trigram('i', 't', 'u'),
            Trigram('t', 'u', 's'),
            Trigram(' ', 'e', 'a'),
            Trigram('e', 'a', ' '),
            Trigram('a', 'e', 'q'),
            Trigram('g', 'i', 'o'),
            Trigram('u', 'i', ' '),
            Trigram('m', ' ', 's'),
            Trigram('e', 'r', ' '),
            Trigram('m', ' ', 'r'),
            Trigram(' ', 'r', 'a'),
            Trigram(' ', 'f', 'i'),
            Trigram('f', 'f', 'i'),
            Trigram('c', 'o', 'g'),
            Trigram('d', 'a', ' '),
            Trigram(' ', 'l', 'e'),
            Trigram('m', 'o', 'd'),
            Trigram('a', ' ', 'c'),
            Trigram('m', 'q', 'u'),
            Trigram('n', 'u', 'l'),
            Trigram('e', ' ', 'o'),
            Trigram('e', 'r', 'a'),
            Trigram('t', 'e', 'n'),
            Trigram('n', 't', 'u'),
            Trigram('s', 'p', 'e'),
            Trigram('o', ' ', 'n'),
            Trigram('e', 'm', 'o'),
            Trigram('c', 'r', 'i'),
            Trigram('s', ' ', 'f'),
            Trigram(' ', 'c', 'a'),
            Trigram('d', 'e', ' '),
            Trigram('a', ' ', 'd'),
            Trigram('r', 'e', 'l'),
            Trigram('i', 'i', ' '),
            Trigram('e', 'n', 'e'),
            Trigram(' ', 't', 'u'),
            Trigram('s', 'u', 'i'),
            Trigram('r', 't', 'i'),
            Trigram('s', 'c', 'i'),
            Trigram('n', 'a', 'e'),
            Trigram('m', ' ', 'q'),
            Trigram('m', ' ', 'a'),
            Trigram('e', 'g', 'i'),
            Trigram('c', 'e', 's'),
        ],
    ),
    (
        Lang::Cym,
        &[
            Trigram('y', 'n', ' '),
            Trigram(' ', 'y', 'n'),
            Trigram('d', 'd', ' '),
            Trigram(' ', 'm', 'a'),
            Trigram('a', 'e', ' '),
            Trigram('m', 'a', 'e'),
            Trigram('a', 'u', ' '),
            Trigram(' ', 'y', ' '),
            Trigram('d', ' ', 'y'),
            Trigram('e', 'd', 'd'),
            Trigram(' ', 'r', ' '),
            Trigram('y', 'd', 'd'),
            Trigram(' ', 'a', 'r'),
            Trigram(' ', 'i', ' '),
            Trigram('n', ' ', 'y'),
            Trigram(' ', 'o', ' '),
            Trigram(' ', 'c', 'y'),
            Trigram('t', 'h', ' '),
            Trigram(' ', 'g', 'w'),
            Trigram('d', 'd', 'i'),
            Trigram('e', 't', 'h'),
            Trigram('o', 'e', 'd'),
            Trigram('o', 'l', ' '),
            Trigram('a', 'r', ' '),
            Trigram(' ', 'g', 'y'),
            Trigram(' ', 'd', 'd'),
            Trigram('w', 'y', 'd'),
            Trigram(' ', 'e', 'i'),
            Trigram(' ', 'n', ' '),
            Trigram(' ', 'a', ' '),
            Trigram('y', 'd', ' '),
            Trigram('o', 'd', 'd'),
            Trigram(' ', 'g', 'a'),
            Trigram('a', 'e', 't'),
            Trigram('a', 'n', ' '),
            Trigram(' ', 'r', 'h'),
            Trigram('i', 'a', 'd'),
            Trigram('i', 'o', ' '),
            Trigram('n', ' ', 'a'),
            Trigram('e', 'i', ' '),
            Trigram('y', 'r', ' '),
            Trigram('w', 'n', ' '),
            Trigram('n', ' ', 'c'),
            Trigram(' ', 'l', 'l'),
            Trigram(' ', 'c', 'a'),
            Trigram('n', ' ', 'g'),
            Trigram('d', 'i', ' '),
            Trigram('w', 'e', 'd'),
            Trigram(' ', 'm', 'e'),
            Trigram('o', 'd', ' '),
            Trigram('e', 'l', ' '),
            Trigram('n', ' ', 'd'),
            Trigram('e', 'd', 'i'),
            Trigram('r', ' ', 'y'),
            Trigram('i', 't', 'h'),
            Trigram(' ', 'w', 'e'),
            Trigram('a', 'd', ' '),
            Trigram(' ', 'f', 'e'),
            Trigram('e', 'r', ' '),
            Trigram('r', ' ', 'a'),
            Trigram('d', 'a', 'u'),
            Trigram(' ', 'd', 'a'),
            Trigram(' ', 'a', 'm'),
            Trigram('d', ' ', 'a'),
            Trigram('o', 'n', ' '),
            Trigram('c', 'h', ' '),
            Trigram('l', ' ', 'y'),
            Trigram('d', 'd', 'o'),
            Trigram(' ', 'h', 'e'),
            Trigram(' ', 'c', 'h'),
            Trigram('r', 'o', 'e'),
            Trigram(' ', 'h', 'y'),
            Trigram('e', ' ', 'r'),
            Trigram(' ', 'd', 'i'),
            Trigram('y', 'n', 'n'),
            Trigram(' ', 'y', 'r'),
            Trigram('d', 'd', 'a'),
            Trigram('r', ' ', 'g'),
            Trigram('g', 'a', 'n'),
            Trigram('i', 'r', ' '),
            Trigram('e', 'w', 'n'),
            Trigram(' ', 'r', 'o'),
            Trigram('e', 'n', ' '),
            Trigram(' ', 'd', 'y'),
            Trigram('f', 'o', 'd'),
            Trigram(' ', 'f', 'f'),
            Trigram('i', 'a', 'u'),
            Trigram('l', 'l', ' '),
            Trigram('m', 'e', 'w'),
            Trigram(' ', 'y', 'm'),
            Trigram(' ', 'd', 'e'),
            Trigram('i', 'd', ' '),
            Trigram(' ', 's', 'y'),
            Trigram('y', 'w', ' '),
            Trigram('d', 'i', 'a'),
            Trigram('h', 'y', 'n'),
            Trigram('f', 'y', 'd'),
            Trigram('i', ' ', 'g'),
            Trigram(' ', 'u', 'n'),
            Trigram('e', 'u', ' '),
            Trigram('i', ' ', 'd'),
            Trigram('n', 'o', 'l'),
            Trigram('l', 'l', 'a'),
            Trigram('u', ' ', 'a'),
            Trigram('e', 'i', 't'),
            Trigram(' ', 'a', 'c'),
            Trigram('d', 'o', 'l'),
            Trigram('i', ' ', 'r'),
            Trigram('w', 'y', ' '),
            Trigram('d', 'i', 'o'),
            Trigram('c', 'y', 'n'),
            Trigram('f', 'e', 'l'),
            Trigram(' ', 'n', 'i'),
            Trigram('o', ' ', 'r'),
            Trigram('i', 'd', 'd'),
            Trigram('r', 't', 'h'),
            Trigram(' ', 'g', 'o'),
            Trigram('l', ' ', 'a'),
            Trigram('a', 'i', ' '),
            Trigram('e', 'f', 'y'),
            Trigram('d', 'y', 'n'),
            Trigram(' ', 'b', 'o'),
            Trigram('r', 'h', 'a'),
            Trigram('e', 'd', ' '),
            Trigram(' ', 'd', 'r'),
            Trigram('r', 'w', 'y'),
            Trigram('a', 'd', 'a'),
            Trigram('n', ' ', 'f'),
            Trigram('w', 'y', 'r'),
            Trigram('f', 'e', 'r'),
            Trigram('a', 'c', ' '),
            Trigram('n', ' ', 'e'),
            Trigram('r', 'd', 'd'),
            Trigram('a', 'i', 'd'),
            Trigram('a', 'e', 'l'),
            Trigram('a', 'l', 'l'),
            Trigram('n', 't', ' '),
            Trigram('i', 'o', 'n'),
            Trigram(' ', 't', 'r'),
            Trigram('n', 'y', 'd'),
            Trigram('a', 'c', 'h'),
            Trigram('g', 'y', 'f'),
            Trigram('c', 'y', 'f'),
            Trigram('r', ' ', 'd'),
            Trigram('i', 'g', ' '),
            Trigram('h', ' ', 'y'),
            Trigram('c', 'h', 'w'),
            Trigram('e', 'l', 'l'),
            Trigram('n', ' ', 'b'),
            Trigram('d', ' ', 'e'),
            Trigram('n', ' ', 'o'),
            Trigram(' ', 'b', 'y'),
            Trigram(' ', 'n', 'e'),
            Trigram('d', 'a', ' '),
            Trigram(' ', 'b', 'e'),
            Trigram('h', 'a', 'n'),
            Trigram('n', 'i', 'a'),
            Trigram(' ', 'o', 'e'),
            Trigram('d', ' ', 'o'),
            Trigram('r', ' ', 'c'),
            Trigram('d', ' ', 'g'),
            Trigram('d', 'd', 'e'),
            Trigram('r', ' ', 'o'),
            Trigram('a', 'f', ' '),
            Trigram('a', 'r', 'a'),
            Trigram('n', 'i', ' '),
            Trigram('n', ' ', 's'),
            Trigram(' ', 'p', 'e'),
            Trigram('l', 'w', 'y'),
            Trigram('g', 'w', 'e'),
            Trigram('i', ' ', 'a'),
            Trigram('w', 'r', ' '),
            Trigram(' ', 'b', 'r'),
            Trigram('i', 'n', ' '),
            Trigram('g', 'o', 'l'),
            Trigram(' ', 'g', 'e'),
            Trigram('r', 'c', 'h'),
            Trigram('h', 'e', 'f'),
            Trigram(' ', 'a', 'd'),
            Trigram('n', 'o', 'd'),
            Trigram('n', 'n', 'a'),
            Trigram('g', 'y', 'd'),
            Trigram(' ', 'f', 'a'),
            Trigram('u', 'n', ' '),
            Trigram('d', ' ', 'h'),
            Trigram(' ', 'y', 's'),
            Trigram('d', ' ', 'i'),
            Trigram('y', ' ', 'd'),
            Trigram('e', ' ', 'n'),
            Trigram('r', 'i', 'a'),
            Trigram('e', 's', ' '),
            Trigram(' ', 'a', 'n'),
            Trigram('d', 'w', 'y'),
            Trigram('a', 'm', ' '),
            Trigram('y', 's', 'g'),
            Trigram('y', ' ', 'g'),
            Trigram('w', 'y', 'n'),
            Trigram('u', ' ', 'c'),
            Trigram('l', ' ', 'e'),
            Trigram('i', ' ', 'f'),
            Trigram('g', 'w', 'y'),
            Trigram('e', 'f', 'n'),
            Trigram('d', 'd', 'y'),
            Trigram('y', ' ', 'c'),
            Trigram('d', 'i', 'g'),
            Trigram('w', 'y', 's'),
            Trigram(' ', 'e', 'u'),
            Trigram('y', 'd', 'a'),
            Trigram('n', ' ', 'h'),
            Trigram('y', 'c', 'h'),
            Trigram('t', 'h', 'i'),
            Trigram('a', 'n', 't'),
            Trigram(' ', 'y', 'w'),
            Trigram('w', 'e', 'i'),
            Trigram(' ', 'b', 'a'),
            Trigram('d', ' ', 'c'),
            Trigram('n', ' ', 'n'),
            Trigram('s', ' ', 'y'),
            Trigram('y', 's', 't'),
            Trigram('r', 'y', 'd'),
            Trigram('n', 'a', ' '),
            Trigram('o', ' ', 'a'),
            Trigram('i', ' ', 'n'),
            Trigram('n', ' ', 'm'),
            Trigram('u', ' ', 'g'),
            Trigram('d', ' ', 'd'),
            Trigram('l', 'a', 'w'),
            Trigram('i', ' ', 'w'),
            Trigram('n', ' ', 'i'),
            Trigram('n', ' ', 'r'),
            Trigram(' ', 'f', 'o'),
            Trigram('y', 's', ' '),
            Trigram('i', 'a', 'e'),
            Trigram(' ', 'c', 'o'),
            Trigram('d', 'o', ' '),
            Trigram('l', 'i', 'a'),
            Trigram('r', 'e', 'd'),
            Trigram('n', 'd', ' '),
            Trigram('y', ' ', 'n'),
            Trigram('h', 'a', 'u'),
            Trigram(' ', 'h', 'a'),
            Trigram('n', 'e', 'u'),
            Trigram('u', ' ', 'y'),
            Trigram('r', 'h', 'y'),
            Trigram('u', ' ', 'r'),
            Trigram('b', 'o', 'd'),
            Trigram(' ', 'p', 'r'),
            Trigram(' ', 'c', 'e'),
            Trigram('r', 'a', 'e'),
            Trigram('g', 'o', 'r'),
            Trigram('e', 'n', 'n'),
            Trigram('g', 'w', 'a'),
            Trigram(' ', 'p', 'a'),
            Trigram('i', ' ', 'c'),
            Trigram(' ', 'e', 'r'),
            Trigram('l', 'y', 'n'),
            Trigram('r', 'a', 'i'),
            Trigram('r', 'i', 'f'),
            Trigram('i', 'a', 'n'),
            Trigram('l', 'l', 'i'),
            Trigram('n', 'a', 'u'),
            Trigram('r', ' ', 'h'),
            Trigram('l', 'a', 'n'),
            Trigram('n', 'w', 'y'),
            Trigram('y', 'f', 'e'),
            Trigram('t', 'h', 'a'),
            Trigram('r', ' ', 'e'),
            Trigram('d', ' ', 'm'),
            Trigram('d', 'i', 'w'),
            Trigram('o', 's', ' '),
            Trigram('l', 'l', 'e'),
            Trigram('a', 'n', 'g'),
            Trigram(' ', 's', 'e'),
            Trigram('d', 'd', 'w'),
            Trigram('a', 'l', ' '),
            Trigram('l', 'a', 'd'),
            Trigram('o', ' ', 'g'),
            Trigram('c', 'a', 'e'),
            Trigram('a', 'n', 'n'),
            Trigram('o', 'l', 'i'),
            Trigram('a', ' ', 'r'),
            Trigram('r', ' ', 'b'),
            Trigram('r', 'i', 'o'),
            Trigram('h', 'y', 'd'),
            Trigram('a', 'i', 't'),
            Trigram('a', 'e', 'n'),
            Trigram('u', ' ', 'd'),
            Trigram('n', 'o', ' '),
            Trigram('d', ' ', 'b'),
            Trigram(' ', 's', 'i'),
            Trigram('f', 'a', 'n'),
            Trigram('l', 'l', 'y'),
            Trigram('u', ' ', 'h'),
            Trigram('o', ' ', 'd'),
            Trigram('i', ' ', 'b'),
            Trigram('d', 'a', 'r'),
            Trigram('s', 'g', 'o'),
            Trigram('y', 'n', 'g'),
            Trigram('d', 'o', 'd'),
            Trigram('u', ' ', 'n'),
        ],
    ),
];

/// Languages for script Cyrillic
pub static CYRILLIC_LANGS: LangProfileList = &[
    (
        Lang::Rus,
        &[
            Trigram(' ', 'п', 'р'),
            Trigram(' ', 'и', ' '),
            Trigram('р', 'а', 'в'),
            Trigram('с', 'т', 'в'),
            Trigram(' ', 'н', 'а'),
            Trigram('п', 'р', 'а'),
            Trigram('г', 'о', ' '),
            Trigram('е', 'н', 'и'),
            Trigram('о', 'в', 'е'),
            Trigram('в', 'о', ' '),
            Trigram(' ', 'к', 'а'),
            Trigram('а', 'н', 'и'),
            Trigram('т', 'ь', ' '),
            Trigram(' ', 'в', ' '),
            Trigram(' ', 'п', 'о'),
            Trigram(' ', 'о', 'б'),
            Trigram('и', 'я', ' '),
            Trigram('с', 'в', 'о'),
            Trigram(' ', 'с', 'в'),
            Trigram('л', 'о', 'в'),
            Trigram('н', 'а', ' '),
            Trigram(' ', 'ч', 'е'),
            Trigram('е', 'л', 'о'),
            Trigram('о', ' ', 'н'),
            Trigram(' ', 'с', 'о'),
            Trigram('о', 'с', 'т'),
            Trigram('ч', 'е', 'л'),
            Trigram('и', 'е', ' '),
            Trigram('о', 'г', 'о'),
            Trigram('е', 'т', ' '),
            Trigram('н', 'и', 'я'),
            Trigram('е', 'с', 'т'),
            Trigram('а', 'в', 'о'),
            Trigram('ы', 'й', ' '),
            Trigram('а', 'ж', 'д'),
            Trigram(' ', 'и', 'м'),
            Trigram('н', 'и', 'е'),
            Trigram('в', 'е', 'к'),
            Trigram(' ', 'н', 'е'),
            Trigram('л', 'ь', 'н'),
            Trigram('л', 'и', ' '),
            Trigram('о', 'в', 'а'),
            Trigram('и', 'м', 'е'),
            Trigram('а', 'т', 'ь'),
            Trigram('п', 'р', 'и'),
            Trigram('т', ' ', 'п'),
            Trigram('и', ' ', 'п'),
            Trigram('к', 'а', 'ж'),
            Trigram('и', 'л', 'и'),
            Trigram('о', 'б', 'о'),
            Trigram(' ', 'р', 'а'),
            Trigram('ы', 'х', ' '),
            Trigram('ж', 'д', 'ы'),
            Trigram(' ', 'д', 'о'),
            Trigram('д', 'ы', 'й'),
            Trigram('в', 'о', 'б'),
            Trigram('е', 'к', ' '),
            Trigram('б', 'о', 'д'),
            Trigram('в', 'а', ' '),
            Trigram('й', ' ', 'ч'),
            Trigram('е', 'г', 'о'),
            Trigram('с', 'я', ' '),
            Trigram('и', ' ', 'с'),
            Trigram('и', 'и', ' '),
            Trigram('а', 'ц', 'и'),
            Trigram('е', 'е', 'т'),
            Trigram('н', 'о', ' '),
            Trigram('м', 'е', 'е'),
            Trigram('и', ' ', 'и'),
            Trigram('л', 'е', 'н'),
            Trigram('о', 'й', ' '),
            Trigram('т', 'в', 'а'),
            Trigram('н', 'ы', 'х'),
            Trigram('т', 'о', ' '),
            Trigram(' ', 'и', 'л'),
            Trigram('к', ' ', 'и'),
            Trigram('е', 'н', 'н'),
            Trigram(' ', 'б', 'ы'),
            Trigram('и', 'ю', ' '),
            Trigram(' ', 'з', 'а'),
            Trigram('м', 'и', ' '),
            Trigram('т', 'в', 'о'),
            Trigram('и', ' ', 'н'),
            Trigram('о', ' ', 'п'),
            Trigram('в', 'а', 'н'),
            Trigram('о', ' ', 'с'),
            Trigram('с', 'т', 'о'),
            Trigram('а', 'л', 'ь'),
            Trigram(' ', 'в', 'с'),
            Trigram('о', 'м', ' '),
            Trigram('о', ' ', 'в'),
            Trigram('ь', 'н', 'о'),
            Trigram('и', 'х', ' '),
            Trigram('н', 'о', 'г'),
            Trigram('и', ' ', 'в'),
            Trigram('н', 'о', 'в'),
            Trigram('а', 'к', 'о'),
            Trigram('п', 'р', 'о'),
            Trigram('и', 'й', ' '),
            Trigram('с', 'т', 'и'),
            Trigram('и', ' ', 'о'),
            Trigram('п', 'о', 'л'),
            Trigram('о', 'л', 'ж'),
            Trigram('д', 'о', 'л'),
            Trigram('о', 'е', ' '),
            Trigram('б', 'р', 'а'),
            Trigram('я', ' ', 'в'),
            Trigram(' ', 'о', 'с'),
            Trigram('н', 'ы', 'м'),
            Trigram('ж', 'е', 'н'),
            Trigram('р', 'а', 'з'),
            Trigram('т', 'и', ' '),
            Trigram('н', 'о', 'с'),
            Trigram('я', ' ', 'и'),
            Trigram(' ', 'в', 'о'),
            Trigram('т', 'о', 'р'),
            Trigram('в', 'с', 'е'),
            Trigram(' ', 'е', 'г'),
            Trigram('е', 'й', ' '),
            Trigram('т', 'е', 'л'),
            Trigram('н', 'е', ' '),
            Trigram('и', ' ', 'р'),
            Trigram('р', 'е', 'д'),
            Trigram('е', 'л', 'ь'),
            Trigram('т', 'в', 'е'),
            Trigram('о', 'д', 'и'),
            Trigram(' ', 'к', 'о'),
            Trigram('о', 'б', 'щ'),
            Trigram('о', ' ', 'и'),
            Trigram(' ', 'д', 'е'),
            Trigram('и', 'м', 'а'),
            Trigram('а', ' ', 'и'),
            Trigram('ч', 'е', 'с'),
            Trigram('н', 'и', 'м'),
            Trigram('с', 'н', 'о'),
            Trigram('к', 'а', 'к'),
            Trigram(' ', 'л', 'и'),
            Trigram('щ', 'е', 'с'),
            Trigram('в', 'л', 'е'),
            Trigram('ь', 'с', 'я'),
            Trigram('н', 'н', 'ы'),
            Trigram('а', 'с', 'т'),
            Trigram('т', 'ь', 'с'),
            Trigram('н', 'н', 'о'),
            Trigram('о', 'с', 'у'),
            Trigram('е', ' ', 'д'),
            Trigram(' ', 'о', 'т'),
            Trigram('п', 'р', 'е'),
            Trigram('ш', 'е', 'н'),
            Trigram('а', ' ', 'с'),
            Trigram('б', 'щ', 'е'),
            Trigram('о', 'с', 'н'),
            Trigram('о', 'д', 'н'),
            Trigram('б', 'ы', 'т'),
            Trigram('с', 'о', 'в'),
            Trigram('ы', 'т', 'ь'),
            Trigram('л', 'ж', 'н'),
            Trigram('р', 'а', 'н'),
            Trigram('н', 'и', 'ю'),
            Trigram('и', 'ч', 'е'),
            Trigram('а', 'к', ' '),
            Trigram('ы', 'м', ' '),
            Trigram('в', 'а', 'т'),
            Trigram('ч', 'т', 'о'),
            Trigram('с', 'т', 'у'),
            Trigram('ч', 'е', 'н'),
            Trigram('е', ' ', 'в'),
            Trigram(' ', 'с', 'т'),
            Trigram('р', 'е', 'с'),
            Trigram('о', 'л', 'ь'),
            Trigram(' ', 'н', 'и'),
            Trigram('н', 'о', 'м'),
            Trigram('р', 'о', 'д'),
            Trigram('л', 'я', ' '),
            Trigram('н', 'а', 'р'),
            Trigram('в', 'е', 'н'),
            Trigram('д', 'у', ' '),
            Trigram('о', 'ж', 'е'),
            Trigram('н', 'ы', ' '),
            Trigram('е', ' ', 'и'),
            Trigram(' ', 'т', 'о'),
            Trigram('в', 'е', 'р'),
            Trigram('а', ' ', 'о'),
            Trigram('з', 'о', 'в'),
            Trigram('м', ' ', 'и'),
            Trigram('н', 'а', 'ц'),
            Trigram('д', 'е', 'н'),
            Trigram('р', 'и', 'н'),
            Trigram('т', 'у', 'п'),
            Trigram('е', 'ж', 'д'),
            Trigram('с', 'т', 'р'),
            Trigram(' ', 'ч', 'т'),
            Trigram('я', ' ', 'п'),
            Trigram('о', 'н', 'а'),
            Trigram('д', 'о', 'с'),
            Trigram('х', ' ', 'и'),
            Trigram('й', ' ', 'и'),
            Trigram('т', 'о', 'я'),
            Trigram('е', 'с', 'п'),
            Trigram('л', 'и', 'ч'),
            Trigram('б', 'е', 'с'),
            Trigram('о', 'б', 'р'),
            Trigram('о', 'т', 'о'),
            Trigram('о', ' ', 'б'),
            Trigram('ь', 'н', 'ы'),
            Trigram('ь', ' ', 'в'),
            Trigram('н', 'и', 'и'),
            Trigram('е', ' ', 'м'),
            Trigram('у', 'ю', ' '),
            Trigram(' ', 'м', 'о'),
            Trigram('е', 'м', ' '),
            Trigram(' ', 'м', 'е'),
            Trigram('а', 'р', 'о'),
            Trigram(' ', 'р', 'е'),
            Trigram('а', 'в', 'а'),
            Trigram('к', 'о', 'т'),
            Trigram('а', 'в', ' '),
            Trigram(' ', 'в', 'ы'),
            Trigram('а', 'м', ' '),
            Trigram('ж', 'н', 'о'),
            Trigram('с', 'т', 'а'),
            Trigram('а', 'я', ' '),
            Trigram('п', 'о', 'д'),
            Trigram('и', ' ', 'к'),
            Trigram('н', 'о', 'е'),
            Trigram(' ', 'к', ' '),
            Trigram(' ', 'т', 'а'),
            Trigram(' ', 'г', 'о'),
            Trigram('г', 'о', 'с'),
            Trigram('с', 'у', 'д'),
            Trigram('е', 'о', 'б'),
            Trigram('я', ' ', 'н'),
            Trigram('е', 'н', ' '),
            Trigram('и', ' ', 'д'),
            Trigram('м', 'о', 'ж'),
            Trigram('е', 'с', 'к'),
            Trigram('е', 'л', 'и'),
            Trigram('а', 'в', 'н'),
            Trigram('в', 'е', ' '),
            Trigram('е', 'ч', 'е'),
            Trigram('у', 'щ', 'е'),
            Trigram('п', 'е', 'ч'),
            Trigram('д', 'н', 'о'),
            Trigram('о', ' ', 'д'),
            Trigram('х', 'о', 'д'),
            Trigram('к', 'а', ' '),
            Trigram(' ', 'д', 'л'),
            Trigram('д', 'л', 'я'),
            Trigram('о', 'в', 'о'),
            Trigram('а', 'т', 'е'),
            Trigram('л', 'ь', 'с'),
            Trigram('ю', ' ', 'и'),
            Trigram('в', ' ', 'к'),
            Trigram('н', 'е', 'н'),
            Trigram('ц', 'и', 'и'),
            Trigram('н', 'о', 'й'),
            Trigram('у', 'д', 'а'),
            Trigram('в', 'о', 'в'),
            Trigram(' ', 'б', 'е'),
            Trigram('о', 'р', 'о'),
            Trigram('н', 'с', 'т'),
            Trigram('а', 'м', 'и'),
            Trigram('ц', 'и', 'а'),
            Trigram('к', 'о', 'н'),
            Trigram('с', 'е', 'м'),
            Trigram('е', ' ', 'о'),
            Trigram('в', 'н', 'о'),
            Trigram(' ', 'э', 'т'),
            Trigram('а', 'з', 'о'),
            Trigram('х', ' ', 'п'),
            Trigram('н', 'и', ' '),
            Trigram('ж', 'д', 'е'),
            Trigram('м', ' ', 'п'),
            Trigram('к', 'о', 'г'),
            Trigram('о', 'т', ' '),
            Trigram('д', 'с', 'т'),
            Trigram('в', 'н', 'ы'),
            Trigram('с', 'т', 'ь'),
            Trigram('ы', 'е', ' '),
            Trigram('о', ' ', 'о'),
            Trigram('п', 'о', 'с'),
            Trigram('с', 'р', 'е'),
            Trigram('т', 'р', 'а'),
            Trigram('е', 'й', 'с'),
            Trigram('т', 'а', 'к'),
            Trigram('и', ' ', 'б'),
            Trigram('д', 'о', 'в'),
            Trigram('м', 'у', ' '),
            Trigram('я', ' ', 'к'),
            Trigram('н', 'а', 'л'),
            Trigram('д', 'р', 'у'),
            Trigram(' ', 'д', 'р'),
            Trigram('к', 'о', 'й'),
            Trigram('т', 'е', 'р'),
            Trigram('ь', ' ', 'п'),
            Trigram('а', 'р', 'с'),
            Trigram('и', 'з', 'н'),
            Trigram('с', 'о', 'ц'),
            Trigram('е', 'д', 'и'),
            Trigram('о', 'л', 'н'),
        ],
    ),
    (
        Lang::Ukr,
        &[
            Trigram('н', 'а', ' '),
            Trigram(' ', 'п', 'р'),
            Trigram(' ', 'і', ' '),
            Trigram('п', 'р', 'а'),
            Trigram('р', 'а', 'в'),
            Trigram(' ', 'н', 'а'),
            Trigram('н', 'я', ' '),
            Trigram('н', 'н', 'я'),
            Trigram(' ', 'з', 'а'),
            Trigram('о', 'г', 'о'),
            Trigram(' ', 'п', 'о'),
            Trigram('т', 'и', ' '),
            Trigram('г', 'о', ' '),
            Trigram('л', 'ю', 'д'),
            Trigram(' ', 'л', 'ю'),
            Trigram('в', 'о', ' '),
            Trigram(' ', 'к', 'о'),
            Trigram(' ', 'м', 'а'),
            Trigram('л', 'ь', 'н'),
            Trigram('ю', 'д', 'и'),
            Trigram('и', 'х', ' '),
            Trigram('о', ' ', 'н'),
            Trigram(' ', 'н', 'е'),
            Trigram('а', 'в', 'о'),
            Trigram('а', 'н', 'н'),
            Trigram('д', 'и', 'н'),
            Trigram(' ', 'с', 'в'),
            Trigram('с', 'в', 'о'),
            Trigram('о', 'ж', 'н'),
            Trigram('к', 'о', 'ж'),
            Trigram('е', 'н', 'н'),
            Trigram('п', 'о', 'в'),
            Trigram('ж', 'н', 'а'),
            Trigram(' ', 'д', 'о'),
            Trigram('а', 'т', 'и'),
            Trigram('и', 'н', 'а'),
            Trigram('а', 'є', ' '),
            Trigram('а', ' ', 'л'),
            Trigram(' ', 'б', 'у'),
            Trigram('а', 'ц', 'і'),
            Trigram('н', 'е', ' '),
            Trigram('у', 'в', 'а'),
            Trigram('о', 'б', 'о'),
            Trigram(' ', 'о', 'с'),
            Trigram(' ', 'я', 'к'),
            Trigram('м', 'а', 'є'),
            Trigram(' ', 'в', 'и'),
            Trigram('н', 'и', 'х'),
            Trigram('а', 'л', 'ь'),
            Trigram('а', 'б', 'о'),
            Trigram('є', ' ', 'п'),
            Trigram(' ', 'т', 'а'),
            Trigram('н', 'і', ' '),
            Trigram('т', 'ь', ' '),
            Trigram('о', 'в', 'и'),
            Trigram('б', 'о', ' '),
            Trigram(' ', 'в', 'і'),
            Trigram(' ', 'а', 'б'),
            Trigram('е', 'р', 'е'),
            Trigram('і', ' ', 'п'),
            Trigram('а', ' ', 'м'),
            Trigram('в', 'и', 'н'),
            Trigram('б', 'е', 'з'),
            Trigram('п', 'р', 'и'),
            Trigram('і', 'л', 'ь'),
            Trigram('н', 'о', 'г'),
            Trigram('о', ' ', 'п'),
            Trigram('м', 'и', ' '),
            Trigram('т', 'а', ' '),
            Trigram('о', 'м', ' '),
            Trigram('о', 'ю', ' '),
            Trigram('б', 'о', 'д'),
            Trigram('с', 'т', 'а'),
            Trigram('в', 'о', 'б'),
            Trigram(' ', 'б', 'е'),
            Trigram('д', 'о', ' '),
            Trigram('в', 'а', ' '),
            Trigram('т', 'і', ' '),
            Trigram(' ', 'о', 'б'),
            Trigram('о', ' ', 'в'),
            Trigram('о', 'с', 'т'),
            Trigram(' ', 'в', ' '),
            Trigram(' ', 'щ', 'о'),
            Trigram('и', 'й', ' '),
            Trigram('с', 'я', ' '),
            Trigram('і', ' ', 'с'),
            Trigram(' ', 'с', 'п'),
            Trigram('и', 'н', 'н'),
            Trigram('в', 'і', 'д'),
            Trigram('с', 'т', 'в'),
            Trigram('и', ' ', 'п'),
            Trigram('в', 'а', 'н'),
            Trigram('н', 'о', 'в'),
            Trigram('н', 'а', 'н'),
            Trigram('к', 'о', 'н'),
            Trigram(' ', 'у', ' '),
            Trigram('в', 'а', 'т'),
            Trigram('о', 'н', 'а'),
            Trigram('і', 'ї', ' '),
            Trigram('н', 'о', ' '),
            Trigram('д', 'н', 'о'),
            Trigram('і', 'й', ' '),
            Trigram('е', 'з', 'п'),
            Trigram('п', 'е', 'р'),
            Trigram(' ', 'д', 'е'),
            Trigram('у', 'т', 'и'),
            Trigram('ь', 'н', 'о'),
            Trigram('и', 'с', 'т'),
            Trigram('п', 'і', 'д'),
            Trigram('с', 'т', 'і'),
            Trigram('б', 'у', 'т'),
            Trigram(' ', 'м', 'о'),
            Trigram('и', ' ', 'і'),
            Trigram('і', 'д', 'н'),
            Trigram('а', 'к', 'о'),
            Trigram('н', 'н', 'і'),
            Trigram('і', 'д', ' '),
            Trigram('т', 'и', 'с'),
            Trigram('щ', 'о', ' '),
            Trigram('р', 'о', 'д'),
            Trigram('і', ' ', 'в'),
            Trigram('а', ' ', 'з'),
            Trigram('а', 'в', 'а'),
            Trigram(' ', 'п', 'е'),
            Trigram('м', 'у', ' '),
            Trigram('і', ' ', 'н'),
            Trigram('а', ' ', 'п'),
            Trigram('с', 'о', 'б'),
            Trigram('о', 'ї', ' '),
            Trigram('а', ' ', 'в'),
            Trigram('с', 'п', 'р'),
            Trigram('і', 'в', ' '),
            Trigram('н', 'и', 'й'),
            Trigram('я', 'к', 'о'),
            Trigram('д', 'у', ' '),
            Trigram('в', 'н', 'о'),
            Trigram('і', ' ', 'д'),
            Trigram('н', 'у', ' '),
            Trigram('а', 'р', 'о'),
            Trigram('и', ' ', 'с'),
            Trigram(' ', 'і', 'н'),
            Trigram('л', 'я', ' '),
            Trigram('р', 'і', 'в'),
            Trigram('у', ' ', 'в'),
            Trigram(' ', 'р', 'і'),
            Trigram('и', ' ', 'д'),
            Trigram('н', 'а', 'р'),
            Trigram('н', 'е', 'н'),
            Trigram('о', 'в', 'а'),
            Trigram('о', 'м', 'у'),
            Trigram('л', 'е', 'н'),
            Trigram('н', 'а', 'ц'),
            Trigram('н', 'и', 'м'),
            Trigram('и', 'с', 'я'),
            Trigram('ч', 'и', ' '),
            Trigram('а', 'в', ' '),
            Trigram('і', ' ', 'р'),
            Trigram('н', 'о', 'м'),
            Trigram(' ', 'р', 'о'),
            Trigram('н', 'о', 'с'),
            Trigram('в', 'і', ' '),
            Trigram('в', 'н', 'и'),
            Trigram('о', 'в', 'н'),
            Trigram(' ', 'ї', 'ї'),
            Trigram('о', 'в', 'і'),
            Trigram('м', 'о', 'ж'),
            Trigram('в', 'і', 'л'),
            Trigram('у', ' ', 'п'),
            Trigram(' ', 'п', 'і'),
            Trigram(' ', 'с', 'у'),
            Trigram('ї', 'ї', ' '),
            Trigram('о', 'д', 'н'),
            Trigram(' ', 'в', 'с'),
            Trigram('о', 'в', 'о'),
            Trigram('ю', 'т', 'ь'),
            Trigram('і', 'с', 'т'),
            Trigram('с', 'т', 'ь'),
            Trigram('і', ' ', 'з'),
            Trigram(' ', 'с', 'т'),
            Trigram('б', 'у', 'д'),
            Trigram(' ', 'р', 'а'),
            Trigram('ч', 'е', 'н'),
            Trigram('п', 'р', 'о'),
            Trigram('р', 'о', 'з'),
            Trigram('і', 'в', 'н'),
            Trigram('о', 'д', 'у'),
            Trigram('а', ' ', 'о'),
            Trigram('ь', 'н', 'и'),
            Trigram('н', 'и', ' '),
            Trigram('о', ' ', 'с'),
            Trigram('с', 'н', 'о'),
            Trigram('з', 'н', 'а'),
            Trigram('р', 'а', 'ц'),
            Trigram('и', 'м', ' '),
            Trigram('о', ' ', 'д'),
            Trigram('и', 'м', 'и'),
            Trigram('я', ' ', 'і'),
            Trigram('ц', 'і', 'ї'),
            Trigram('х', ' ', 'п'),
            Trigram('д', 'е', 'р'),
            Trigram('ч', 'и', 'н'),
            Trigram(' ', 'с', 'о'),
            Trigram('а', ' ', 'с'),
            Trigram('е', 'р', 'ж'),
            Trigram('и', ' ', 'з'),
            Trigram('и', ' ', 'в'),
            Trigram('е', ' ', 'п'),
            Trigram('д', 'и', ' '),
            Trigram('з', 'а', 'б'),
            Trigram('о', 'с', 'о'),
            Trigram('у', ' ', 'с'),
            Trigram('е', ' ', 'б'),
            Trigram('с', 'і', ' '),
            Trigram('т', 'е', 'р'),
            Trigram('н', 'і', 'х'),
            Trigram('я', ' ', 'н'),
            Trigram('і', ' ', 'б'),
            Trigram('к', 'л', 'а'),
            Trigram('с', 'п', 'і'),
            Trigram('в', ' ', 'і'),
            Trigram(' ', 'н', 'і'),
            Trigram('о', ' ', 'з'),
            Trigram('р', 'ж', 'а'),
            Trigram('с', 'т', 'у'),
            Trigram('ї', 'х', ' '),
            Trigram('а', ' ', 'н'),
            Trigram('н', 'н', 'а'),
            Trigram('т', 'а', 'к'),
            Trigram('я', ' ', 'п'),
            Trigram('з', 'п', 'е'),
            Trigram(' ', 'о', 'д'),
            Trigram('а', 'б', 'е'),
            Trigram('д', 'л', 'я'),
            Trigram('т', 'у', ' '),
            Trigram('і', ' ', 'м'),
            Trigram('п', 'е', 'ч'),
            Trigram(' ', 'д', 'л'),
            Trigram('ж', 'е', ' '),
            Trigram('к', 'и', ' '),
            Trigram('в', 'і', 'т'),
            Trigram('н', 'і', 'с'),
            Trigram('г', 'а', 'л'),
            Trigram('а', 'г', 'а'),
            Trigram('е', ' ', 'м'),
            Trigram('а', 'м', 'и'),
            Trigram('з', 'а', 'х'),
            Trigram('р', 'и', 'м'),
            Trigram('ї', ' ', 'о'),
            Trigram('т', 'а', 'н'),
            Trigram('к', 'о', 'г'),
            Trigram('р', 'е', 'с'),
            Trigram('у', 'д', 'ь'),
            Trigram(' ', 'р', 'е'),
            Trigram('т', 'о', ' '),
            Trigram('к', 'о', 'в'),
            Trigram('т', 'о', 'р'),
            Trigram('а', 'р', 'а'),
            Trigram('с', 'в', 'і'),
            Trigram('т', 'в', 'а'),
            Trigram('а', ' ', 'б'),
            Trigram('о', 'ж', 'е'),
            Trigram('с', 'о', 'ц'),
            Trigram('о', 'ц', 'і'),
            Trigram('ц', 'і', 'а'),
            Trigram('о', 'с', 'н'),
            Trigram('р', 'о', 'б'),
            Trigram('д', 'ь', '‐'),
            Trigram('ь', '‐', 'я'),
            Trigram('‐', 'я', 'к'),
            Trigram('і', ' ', 'і'),
            Trigram('з', 'а', 'г'),
            Trigram('а', 'х', 'и'),
            Trigram('х', 'и', 'с'),
            Trigram('п', 'і', 'л'),
            Trigram('ц', 'і', 'й'),
            Trigram('х', ' ', 'в'),
            Trigram('л', 'и', 'в'),
            Trigram('о', 'с', 'в'),
            Trigram('і', 'а', 'л'),
            Trigram('р', 'у', 'ч'),
            Trigram('ь', ' ', 'п'),
            Trigram('і', 'н', 'ш'),
            Trigram('в', ' ', 'я'),
            Trigram('г', 'и', ' '),
            Trigram('а', 'г', 'и'),
            Trigram(' ', 'д', 'і'),
            Trigram('к', 'о', 'м'),
            Trigram('и', 'н', 'и'),
            Trigram('а', ' ', 'і'),
            Trigram('о', 'д', 'и'),
            Trigram('н', 'а', 'л'),
            Trigram('т', 'в', 'о'),
            Trigram('к', 'о', 'ї'),
            Trigram('в', 'с', 'і'),
            Trigram('я', ' ', 'в'),
            Trigram('н', 'о', 'ю'),
            Trigram('о', 'б', ' '),
            Trigram('о', ' ', 'у'),
            Trigram('о', ' ', 'о'),
            Trigram('і', ' ', 'о'),
        ],
    ),
    (
        Lang::Srp,
        &[
            Trigram(' ', 'п', 'р'),
            Trigram(' ', 'и', ' '),
            Trigram('р', 'а', 'в'),
            Trigram('п', 'р', 'а'),
            Trigram(' ', 'н', 'а'),
            Trigram('н', 'а', ' '),
            Trigram(' ', 'п', 'о'),
            Trigram('м', 'а', ' '),
            Trigram(' ', 'с', 'в'),
            Trigram('д', 'а', ' '),
            Trigram('и', 'м', 'а'),
            Trigram('а', ' ', 'п'),
            Trigram('а', ' ', 'и'),
            Trigram('в', 'о', ' '),
            Trigram('к', 'о', ' '),
            Trigram('в', 'а', ' '),
            Trigram('т', 'и', ' '),
            Trigram('и', ' ', 'п'),
            Trigram(' ', 'у', ' '),
            Trigram('а', 'к', 'о'),
            Trigram(' ', 'д', 'а'),
            Trigram('а', ' ', 'с'),
            Trigram('а', 'в', 'о'),
            Trigram('и', ' ', 'с'),
            Trigram('о', 'с', 'т'),
            Trigram(' ', 'з', 'а'),
            Trigram('о', ' ', 'и'),
            Trigram('с', 'в', 'а'),
            Trigram(' ', 'и', 'м'),
            Trigram('в', 'а', 'к'),
            Trigram('а', 'в', 'а'),
            Trigram('ј', 'е', ' '),
            Trigram('е', ' ', 'с'),
            Trigram(' ', 'с', 'л'),
            Trigram(' ', 'к', 'о'),
            Trigram('о', ' ', 'н'),
            Trigram('њ', 'а', ' '),
            Trigram('н', 'о', ' '),
            Trigram('н', 'е', ' '),
            Trigram(' ', 'н', 'е'),
            Trigram('о', 'м', ' '),
            Trigram('л', 'и', ' '),
            Trigram(' ', 'д', 'р'),
            Trigram('и', 'л', 'и'),
            Trigram('у', ' ', 'с'),
            Trigram('с', 'л', 'о'),
            Trigram('о', 'б', 'о'),
            Trigram('к', 'о', 'ј'),
            Trigram('и', 'х', ' '),
            Trigram('л', 'о', 'б'),
            Trigram('б', 'о', 'д'),
            Trigram('и', 'м', ' '),
            Trigram('а', ' ', 'н'),
            Trigram('ј', 'у', ' '),
            Trigram(' ', 'и', 'л'),
            Trigram('с', 'т', 'в'),
            Trigram(' ', 'б', 'и'),
            Trigram('с', 'т', 'и'),
            Trigram('а', ' ', 'о'),
            Trigram('п', 'р', 'и'),
            Trigram('а', ' ', 'у'),
            Trigram(' ', 'р', 'а'),
            Trigram('ј', 'е', 'д'),
            Trigram('о', 'г', ' '),
            Trigram(' ', 'ј', 'е'),
            Trigram('е', ' ', 'п'),
            Trigram('њ', 'е', ' '),
            Trigram('н', 'и', ' '),
            Trigram('у', ' ', 'п'),
            Trigram('а', ' ', 'д'),
            Trigram('е', 'д', 'н'),
            Trigram('и', 'т', 'и'),
            Trigram('а', ' ', 'к'),
            Trigram('н', 'о', 'с'),
            Trigram('и', ' ', 'у'),
            Trigram('о', ' ', 'д'),
            Trigram('п', 'р', 'о'),
            Trigram(' ', 'с', 'у'),
            Trigram('а', 'њ', 'е'),
            Trigram('о', 'в', 'а'),
            Trigram('е', ' ', 'и'),
            Trigram('в', 'а', 'њ'),
            Trigram('и', ' ', 'и'),
            Trigram('ц', 'и', 'ј'),
            Trigram(' ', 'о', 'с'),
            Trigram('с', 'е', ' '),
            Trigram('д', 'р', 'у'),
            Trigram('с', 'т', 'а'),
            Trigram('а', 'ј', 'у'),
            Trigram('а', 'њ', 'а'),
            Trigram('и', ' ', 'о'),
            Trigram(' ', 'о', 'б'),
            Trigram('р', 'о', 'д'),
            Trigram('о', 'в', 'е'),
            Trigram(' ', 'к', 'а'),
            Trigram(' ', 'д', 'е'),
            Trigram('е', ' ', 'о'),
            Trigram('а', 'ц', 'и'),
            Trigram('ј', 'а', ' '),
            Trigram('о', 'в', 'о'),
            Trigram(' ', 'н', 'и'),
            Trigram(' ', 'о', 'д'),
            Trigram('и', ' ', 'д'),
            Trigram(' ', 'с', 'е'),
            Trigram('в', 'е', ' '),
            Trigram('у', 'ј', 'е'),
            Trigram('е', 'н', 'и'),
            Trigram('и', 'ј', 'а'),
            Trigram('а', 'в', 'н'),
            Trigram('ж', 'а', 'в'),
            Trigram(' ', 'с', 'т'),
            Trigram('у', ' ', 'и'),
            Trigram('м', ' ', 'и'),
            Trigram('д', 'н', 'а'),
            Trigram('с', 'у', ' '),
            Trigram('р', 'е', 'д'),
            Trigram('и', ' ', 'н'),
            Trigram('о', 'ј', 'а'),
            Trigram('е', ' ', 'б'),
            Trigram('а', 'р', 'а'),
            Trigram('ш', 'т', 'о'),
            Trigram('н', 'о', 'в'),
            Trigram('р', 'ж', 'а'),
            Trigram('в', 'о', 'ј'),
            Trigram('д', 'р', 'ж'),
            Trigram('т', 'в', 'а'),
            Trigram('о', 'д', 'и'),
            Trigram('у', ' ', 'о'),
            Trigram('а', ' ', 'б'),
            Trigram('о', 'д', 'н'),
            Trigram('п', 'о', 'ш'),
            Trigram('о', 'ш', 'т'),
            Trigram('н', 'и', 'м'),
            Trigram('а', ' ', 'ј'),
            Trigram('к', 'а', ' '),
            Trigram('р', 'а', 'н'),
            Trigram('у', ' ', 'у'),
            Trigram(' ', 'о', 'в'),
            Trigram('а', 'р', 'о'),
            Trigram('е', ' ', 'д'),
            Trigram('с', 'н', 'о'),
            Trigram('е', 'њ', 'а'),
            Trigram('у', ' ', 'з'),
            Trigram('р', 'а', 'з'),
            Trigram(' ', 'и', 'з'),
            Trigram('о', 'с', 'н'),
            Trigram('а', ' ', 'з'),
            Trigram('о', ' ', 'п'),
            Trigram('а', 'в', 'е'),
            Trigram('п', 'р', 'е'),
            Trigram('д', 'е', ' '),
            Trigram('б', 'и', 'т'),
            Trigram('н', 'и', 'х'),
            Trigram('ш', 'т', 'и'),
            Trigram('в', 'у', ' '),
            Trigram('у', ' ', 'д'),
            Trigram('д', 'у', ' '),
            Trigram('т', 'у', ' '),
            Trigram(' ', 'т', 'р'),
            Trigram('н', 'а', 'р'),
            Trigram(' ', 'с', 'а'),
            Trigram('г', 'о', 'в'),
            Trigram('з', 'а', ' '),
            Trigram('б', 'е', 'з'),
            Trigram('о', 'ј', 'и'),
            Trigram('у', ' ', 'н'),
            Trigram('в', 'н', 'о'),
            Trigram('и', 'ч', 'н'),
            Trigram('е', 'ђ', 'у'),
            Trigram('л', 'о', ' '),
            Trigram('а', 'н', ' '),
            Trigram('ч', 'н', 'о'),
            Trigram('ј', 'и', ' '),
            Trigram('н', 'а', 'к'),
            Trigram('о', 'д', 'а'),
            Trigram(' ', 'м', 'е'),
            Trigram('в', 'и', 'м'),
            Trigram('т', 'о', ' '),
            Trigram('с', 'в', 'о'),
            Trigram('а', 'н', 'и'),
            Trigram('н', 'а', 'ц'),
            Trigram(' ', 'њ', 'е'),
            Trigram('н', 'и', 'к'),
            Trigram('њ', 'е', 'г'),
            Trigram('т', 'и', 'т'),
            Trigram('о', 'ј', ' '),
            Trigram('м', 'е', ' '),
            Trigram('н', 'о', 'м'),
            Trigram('м', ' ', 'с'),
            Trigram('е', ' ', 'у'),
            Trigram('о', ' ', 'к'),
            Trigram('к', 'у', ' '),
            Trigram(' ', 'д', 'о'),
            Trigram('и', 'к', 'а'),
            Trigram('и', 'к', 'о'),
            Trigram('е', ' ', 'к'),
            Trigram('п', 'о', 'с'),
            Trigram('а', 'ш', 'т'),
            Trigram('т', 'р', 'е'),
            Trigram('а', 'л', 'н'),
            Trigram('н', 'о', 'г'),
            Trigram(' ', 'в', 'р'),
            Trigram('р', 'е', 'б'),
            Trigram('н', 'с', 'т'),
            Trigram(' ', 'к', 'р'),
            Trigram('с', 'т', 'у'),
            Trigram('д', 'н', 'о'),
            Trigram('е', 'м', ' '),
            Trigram('в', 'а', 'р'),
            Trigram('е', ' ', 'н'),
            Trigram('р', 'и', 'в'),
            Trigram('т', 'у', 'п'),
            Trigram('ж', 'и', 'в'),
            Trigram('т', 'е', ' '),
            Trigram('ч', 'о', 'в'),
            Trigram('с', 'т', ' '),
            Trigram('о', 'в', 'и'),
            Trigram('д', 'н', 'и'),
            Trigram('а', 'о', ' '),
            Trigram('с', 'м', 'е'),
            Trigram('б', 'р', 'а'),
            Trigram('а', 'в', 'и'),
            Trigram(' ', 'л', 'и'),
            Trigram('к', 'а', 'о'),
            Trigram('в', 'о', 'љ'),
            Trigram('и', 'л', 'о'),
            Trigram('о', ' ', 'с'),
            Trigram('ш', 'т', 'в'),
            Trigram('и', ' ', 'м'),
            Trigram('з', 'а', 'ш'),
            Trigram('њ', 'у', ' '),
            Trigram('р', 'у', 'г'),
            Trigram('т', 'а', 'в'),
            Trigram('а', 'н', 'с'),
            Trigram('е', 'н', 'о'),
            Trigram('п', 'о', 'р'),
            Trigram('к', 'р', 'и'),
            Trigram('и', ' ', 'б'),
            Trigram('о', 'д', 'у'),
            Trigram('а', ' ', 'р'),
            Trigram('л', 'а', ' '),
            Trigram(' ', 'ч', 'о'),
            Trigram('а', ' ', 'т'),
            Trigram('р', 'у', 'ш'),
            Trigram('у', 'ш', 'т'),
            Trigram(' ', 'б', 'у'),
            Trigram('б', 'у', 'д'),
            Trigram('а', 'в', 'љ'),
            Trigram('у', 'г', 'и'),
            Trigram('м', ' ', 'п'),
            Trigram('к', 'о', 'м'),
            Trigram('о', 'ј', 'е'),
            Trigram('в', 'е', 'р'),
            Trigram(' ', 'в', 'е'),
            Trigram('п', 'о', 'д'),
            Trigram('и', ' ', 'в'),
            Trigram('м', 'е', 'ђ'),
            Trigram('е', 'г', 'о'),
            Trigram('в', 'р', 'е'),
            Trigram('а', 'к', 'в'),
            Trigram('е', 'д', 'и'),
            Trigram('т', 'в', 'о'),
            Trigram(' ', 'с', 'м'),
            Trigram('о', 'д', ' '),
            Trigram('д', 'е', 'л'),
            Trigram('е', 'н', 'а'),
            Trigram('р', 'а', 'д'),
            Trigram('б', 'а', ' '),
            Trigram(' ', 'м', 'о'),
            Trigram('н', 'у', ' '),
            Trigram('о', ' ', 'ј'),
            Trigram('д', 'с', 'т'),
            Trigram('к', 'л', 'а'),
            Trigram(' ', 'о', 'п'),
            Trigram('к', 'а', 'к'),
            Trigram('с', 'а', 'м'),
            Trigram('е', 'р', 'е'),
            Trigram('р', 'и', 'м'),
            Trigram('в', 'и', 'ч'),
            Trigram('и', 'в', 'а'),
            Trigram('о', ' ', 'о'),
            Trigram(' ', 'о', 'н'),
            Trigram('в', 'н', 'и'),
            Trigram('т', 'е', 'р'),
            Trigram('з', 'б', 'е'),
            Trigram('х', ' ', 'п'),
            Trigram('н', 'и', 'ц'),
            Trigram('е', 'б', 'а'),
            Trigram('е', ' ', 'р'),
            Trigram('у', ' ', 'в'),
            Trigram('и', 'с', 'т'),
            Trigram('в', 'е', 'к'),
            Trigram('р', 'е', 'м'),
            Trigram('с', 'в', 'и'),
            Trigram('б', 'и', 'л'),
            Trigram('ш', 'т', 'е'),
            Trigram('е', 'з', 'б'),
            Trigram('ј', 'у', 'ћ'),
            Trigram('њ', 'е', 'н'),
            Trigram('г', 'л', 'а'),
        ],
    ),
    (
        Lang::Bel,
        &[
            Trigram(' ', 'і', ' '),
            Trigram(' ', 'п', 'р'),
            Trigram('п', 'р', 'а'),
            Trigram('а', 'в', 'а'),
            Trigram(' ', 'н', 'а'),
            Trigram('н', 'а', ' '),
            Trigram(' ', 'п', 'а'),
            Trigram('р', 'а', 'в'),
            Trigram('н', 'ы', ' '),
            Trigram('ц', 'ь', ' '),
            Trigram('а', 'б', 'о'),
            Trigram(' ', 'а', 'б'),
            Trigram('в', 'а', ' '),
            Trigram('а', 'ц', 'ы'),
            Trigram('а', 'в', 'е'),
            Trigram('а', 'е', ' '),
            Trigram(' ', 'ч', 'а'),
            Trigram('н', 'н', 'я'),
            Trigram('а', 'н', 'н'),
            Trigram('л', 'ь', 'н'),
            Trigram(' ', 'м', 'а'),
            Trigram(' ', 'с', 'в'),
            Trigram('с', 'в', 'а'),
            Trigram('а', 'л', 'а'),
            Trigram('н', 'е', ' '),
            Trigram('ч', 'а', 'л'),
            Trigram('л', 'а', 'в'),
            Trigram('н', 'я', ' '),
            Trigram('а', 'й', ' '),
            Trigram('ы', 'х', ' '),
            Trigram(' ', 'я', 'к'),
            Trigram('г', 'а', ' '),
            Trigram('в', 'е', 'к'),
            Trigram('е', ' ', 'п'),
            Trigram(' ', 'а', 'д'),
            Trigram('а', ' ', 'н'),
            Trigram(' ', 'н', 'е'),
            Trigram('п', 'р', 'ы'),
            Trigram('а', 'г', 'а'),
            Trigram(' ', 'к', 'о'),
            Trigram('а', ' ', 'п'),
            Trigram(' ', 'з', 'а'),
            Trigram('к', 'о', 'ж'),
            Trigram('о', 'ж', 'н'),
            Trigram('ы', ' ', 'ч'),
            Trigram('б', 'о', 'д'),
            Trigram('д', 'н', 'а'),
            Trigram('ж', 'н', 'ы'),
            Trigram('в', 'а', 'б'),
            Trigram('ц', 'ц', 'а'),
            Trigram('ц', 'а', ' '),
            Trigram(' ', 'ў', ' '),
            Trigram('а', ' ', 'а'),
            Trigram('е', 'к', ' '),
            Trigram('м', 'а', 'е'),
            Trigram('і', ' ', 'п'),
            Trigram('н', 'н', 'е'),
            Trigram('н', 'ы', 'х'),
            Trigram('а', 'с', 'ц'),
            Trigram('а', ' ', 'с'),
            Trigram('п', 'а', 'в'),
            Trigram('б', 'о', ' '),
            Trigram('а', 'м', ' '),
            Trigram('с', 'т', 'а'),
            Trigram(' ', 'с', 'а'),
            Trigram(' ', 'в', 'ы'),
            Trigram('в', 'а', 'н'),
            Trigram('ь', 'н', 'а'),
            Trigram(' ', 'д', 'а'),
            Trigram('а', 'р', 'а'),
            Trigram('д', 'з', 'е'),
            Trigram('о', 'д', 'н'),
            Trigram('г', 'о', ' '),
            Trigram('н', 'а', 'г'),
            Trigram('в', 'і', 'н'),
            Trigram('а', 'ц', 'ь'),
            Trigram('о', 'ў', 'н'),
            Trigram('ц', 'ы', 'я'),
            Trigram('м', 'і', ' '),
            Trigram('т', 'о', ' '),
            Trigram(' ', 'р', 'а'),
            Trigram('і', ' ', 'а'),
            Trigram('т', 'в', 'а'),
            Trigram(' ', 'а', 'с'),
            Trigram('с', 'т', 'в'),
            Trigram('л', 'е', 'н'),
            Trigram('а', 'в', 'і'),
            Trigram('а', 'д', ' '),
            Trigram('і', ' ', 'с'),
            Trigram('е', 'н', 'н'),
            Trigram('і', ' ', 'н'),
            Trigram('а', 'л', 'ь'),
            Trigram('н', 'а', 'й'),
            Trigram('а', 'в', 'о'),
            Trigram('р', 'а', 'ц'),
            Trigram('а', 'р', 'о'),
            Trigram('ц', 'і', ' '),
            Trigram('с', 'ц', 'і'),
            Trigram('п', 'а', 'д'),
            Trigram('а', 'м', 'а'),
            Trigram(' ', 'б', 'ы'),
            Trigram(' ', 'я', 'г'),
            Trigram('я', 'г', 'о'),
            Trigram('к', ' ', 'м'),
            Trigram('і', 'х', ' '),
            Trigram('р', 'ы', 'м'),
            Trigram('ы', 'м', ' '),
            Trigram('э', 'н', 'н'),
            Trigram('ш', 'т', 'о'),
            Trigram('і', ' ', 'і'),
            Trigram('р', 'о', 'д'),
            Trigram(' ', 'т', 'а'),
            Trigram('н', 'а', 'н'),
            Trigram(' ', 'д', 'з'),
            Trigram('н', 'і', ' '),
            Trigram('я', ' ', 'а'),
            Trigram('г', 'э', 'т'),
            Trigram('н', 'а', 'с'),
            Trigram('а', 'н', 'а'),
            Trigram(' ', 'г', 'э'),
            Trigram('і', 'н', 'н'),
            Trigram('а', ' ', 'б'),
            Trigram('ы', 'ц', 'ь'),
            Trigram('д', 'а', ' '),
            Trigram('ы', 'і', ' '),
            Trigram('о', 'ў', ' '),
            Trigram('ч', 'ы', 'н'),
            Trigram(' ', 'ш', 'т'),
            Trigram('а', ' ', 'ў'),
            Trigram('ц', 'ы', 'і'),
            Trigram('я', 'к', 'і'),
            Trigram('д', 'з', 'я'),
            Trigram('а', ' ', 'і'),
            Trigram('а', 'г', 'у'),
            Trigram('я', ' ', 'п'),
            Trigram('н', 'ы', 'м'),
            Trigram('н', 'а', 'ц'),
            Trigram(' ', 'у', ' '),
            Trigram(' ', 'ў', 'с'),
            Trigram('ы', 'я', ' '),
            Trigram('ь', 'н', 'ы'),
            Trigram('о', 'л', 'ь'),
            Trigram('н', 'а', 'р'),
            Trigram('ў', 'н', 'а'),
            Trigram('х', ' ', 'п'),
            Trigram('і', ' ', 'д'),
            Trigram('ў', ' ', 'і'),
            Trigram(' ', 'г', 'р'),
            Trigram('а', 'м', 'і'),
            Trigram('ы', 'м', 'і'),
            Trigram('а', 'х', ' '),
            Trigram(' ', 'у', 'с'),
            Trigram('а', 'д', 'з'),
            Trigram(' ', 'н', 'і'),
            Trigram('э', 'т', 'а'),
            Trigram('л', 'я', ' '),
            Trigram('в', 'о', 'ў'),
            Trigram('ы', 'м', 'а'),
            Trigram('р', 'а', 'д'),
            Trigram('ы', ' ', 'п'),
            Trigram('з', 'н', 'а'),
            Trigram('ч', 'э', 'н'),
            Trigram('н', 'е', 'н'),
            Trigram('а', 'б', 'а'),
            Trigram(' ', 'к', 'а'),
            Trigram('ў', 'л', 'е'),
            Trigram('і', 'н', 'а'),
            Trigram('б', 'ы', 'ц'),
            Trigram('х', 'о', 'д'),
            Trigram(' ', 'і', 'н'),
            Trigram('о', ' ', 'п'),
            Trigram(' ', 'с', 'т'),
            Trigram('е', 'р', 'а'),
            Trigram('у', 'л', 'ь'),
            Trigram('а', 'ў', ' '),
            Trigram('а', 'с', 'н'),
            Trigram('с', 'а', 'м'),
            Trigram('р', 'а', 'м'),
            Trigram('р', 'ы', ' '),
            Trigram(' ', 'с', 'у'),
            Trigram('н', 'а', 'л'),
            Trigram('д', 'у', ' '),
            Trigram('ь', ' ', 'с'),
            Trigram('ч', 'ы', ' '),
            Trigram('к', 'л', 'а'),
            Trigram('а', 'н', 'ы'),
            Trigram('ж', 'н', 'а'),
            Trigram('і', ' ', 'р'),
            Trigram('п', 'е', 'р'),
            Trigram('і', ' ', 'з'),
            Trigram('ь', ' ', 'у'),
            Trigram('м', 'а', 'ю'),
            Trigram('а', 'к', 'о'),
            Trigram('ы', 'ц', 'ц'),
            Trigram('я', 'к', 'о'),
            Trigram('д', 'л', 'я'),
            Trigram('у', 'ю', ' '),
            Trigram('г', 'р', 'а'),
            Trigram('у', 'к', 'а'),
            Trigram('е', ' ', 'і'),
            Trigram('н', 'а', 'е'),
            Trigram('а', 'д', 'с'),
            Trigram('і', ' ', 'ў'),
            Trigram('к', 'а', 'ц'),
            Trigram('ў', 'н', 'ы'),
            Trigram('а', ' ', 'з'),
            Trigram(' ', 'д', 'л'),
            Trigram('я', 'ў', 'л'),
            Trigram('а', ' ', 'р'),
            Trigram('а', 'ю', 'ч'),
            Trigram('ю', 'ч', 'ы'),
            Trigram('о', 'д', 'у'),
            Trigram(' ', 'п', 'е'),
            Trigram(' ', 'р', 'о'),
            Trigram('ы', ' ', 'і'),
            Trigram('в', 'ы', ' '),
            Trigram('і', ' ', 'м'),
            Trigram('а', 'с', 'а'),
            Trigram('е', ' ', 'м'),
            Trigram('а', 'д', 'у'),
            Trigram('х', ' ', 'н'),
            Trigram('о', 'д', 'а'),
            Trigram('а', 'д', 'н'),
            Trigram('н', 'н', 'і'),
            Trigram('к', 'і', ' '),
            Trigram(' ', 'ш', 'л'),
            Trigram('а', 'л', 'е'),
            Trigram('р', 'а', 'з'),
            Trigram('а', 'д', 'а'),
            Trigram('х', ' ', 'і'),
            Trigram('а', 'в', 'я'),
            Trigram('н', 'а', 'в'),
            Trigram('а', 'л', 'і'),
            Trigram('р', 'а', 'б'),
            Trigram('ы', ' ', 'ў'),
            Trigram('н', 'н', 'а'),
            Trigram('м', 'а', 'д'),
            Trigram('р', 'о', 'ў'),
            Trigram('к', 'а', 'н'),
            Trigram('з', 'е', ' '),
            Trigram('д', 'с', 'т'),
            Trigram('ж', 'ы', 'ц'),
            Trigram('а', 'н', 'і'),
            Trigram('н', 'с', 'т'),
            Trigram('з', 'я', 'р'),
            Trigram('р', 'ж', 'а'),
            Trigram('з', 'а', 'к'),
            Trigram('д', 'з', 'і'),
            Trigram('л', 'ю', 'б'),
            Trigram('а', 'ю', 'ц'),
            Trigram('б', 'а', 'р'),
            Trigram('і', 'м', ' '),
            Trigram('е', 'н', 'ы'),
            Trigram('б', 'е', 'с'),
            Trigram('т', 'а', 'н'),
            Trigram('м', ' ', 'п'),
            Trigram('д', 'у', 'к'),
            Trigram('е', ' ', 'а'),
            Trigram('г', 'у', 'л'),
            Trigram('я', ' ', 'ў'),
            Trigram(' ', 'д', 'э'),
            Trigram('в', 'е', ' '),
            Trigram('ж', 'а', 'в'),
            Trigram('а', 'ц', 'ц'),
            Trigram('а', 'х', 'о'),
            Trigram('з', 'а', 'б'),
            Trigram('а', ' ', 'в'),
            Trigram('а', 'в', 'ы'),
            Trigram('г', 'а', 'н'),
            Trigram('о', ' ', 'н'),
            Trigram('в', 'а', 'г'),
            Trigram('я', ' ', 'і'),
            Trigram('ч', 'н', 'а'),
            Trigram('я', ' ', 'я'),
            Trigram('с', 'а', 'ц'),
            Trigram('т', 'а', 'к'),
            Trigram('о', 'д', ' '),
            Trigram('я', 'р', 'ж'),
            Trigram('с', 'о', 'б'),
            Trigram('м', ' ', 'н'),
            Trigram('с', 'е', ' '),
            Trigram('ч', 'а', 'ц'),
            Trigram('н', 'і', 'ч'),
            Trigram('ы', 'я', 'л'),
            Trigram('я', 'л', 'ь'),
            Trigram('ц', 'ц', 'я'),
            Trigram('ь', ' ', 'п'),
            Trigram('о', ' ', 'с'),
            Trigram('в', 'о', 'л'),
            Trigram('д', 'э', 'к'),
            Trigram(' ', 'б', 'е'),
            Trigram('н', 'у', ' '),
            Trigram('о', 'г', 'а'),
            Trigram(' ', 'р', 'э'),
            Trigram('р', 'а', 'с'),
            Trigram('б', 'у', 'д'),
            Trigram('а', ' ', 'т'),
            Trigram('а', 'с', 'о'),
            Trigram('с', 'н', 'о'),
            Trigram('е', 'й', 'н'),
        ],
    ),
    (
        Lang::Bul,
        &[
            Trigram(' ', 'н', 'а'),
            Trigram('н', 'а', ' '),
            Trigram(' ', 'п', 'р'),
            Trigram('т', 'о', ' '),
            Trigram(' ', 'и', ' '),
            Trigram('р', 'а', 'в'),
            Trigram('д', 'а', ' '),
            Trigram('п', 'р', 'а'),
            Trigram(' ', 'д', 'а'),
            Trigram('а', ' ', 'с'),
            Trigram('с', 'т', 'в'),
            Trigram('в', 'а', ' '),
            Trigram('т', 'а', ' '),
            Trigram('а', ' ', 'п'),
            Trigram('и', 'т', 'е'),
            Trigram('н', 'о', ' '),
            Trigram('в', 'о', ' '),
            Trigram('е', 'н', 'и'),
            Trigram('а', ' ', 'н'),
            Trigram('е', ' ', 'н'),
            Trigram(' ', 'з', 'а'),
            Trigram('о', ' ', 'и'),
            Trigram('о', 'т', 'о'),
            Trigram('в', 'а', 'н'),
            Trigram('н', 'е', ' '),
            Trigram(' ', 'в', 'с'),
            Trigram('т', 'е', ' '),
            Trigram('к', 'и', ' '),
            Trigram(' ', 'н', 'е'),
            Trigram('о', ' ', 'н'),
            Trigram('о', 'в', 'е'),
            Trigram(' ', 'п', 'о'),
            Trigram('а', ' ', 'и'),
            Trigram('а', 'в', 'а'),
            Trigram('ч', 'о', 'в'),
            Trigram('н', 'и', ' '),
            Trigram('а', 'н', 'е'),
            Trigram('и', 'я', ' '),
            Trigram(' ', 'ч', 'о'),
            Trigram('а', 'в', 'о'),
            Trigram('и', 'е', ' '),
            Trigram(' ', 'с', 'в'),
            Trigram('е', ' ', 'п'),
            Trigram('а', ' ', 'д'),
            Trigram(' ', 'о', 'б'),
            Trigram('в', 'е', 'к'),
            Trigram('е', 'с', 'т'),
            Trigram('с', 'в', 'о'),
            Trigram(' ', 'и', 'м'),
            Trigram('и', 'м', 'а'),
            Trigram('о', 'с', 'т'),
            Trigram('и', ' ', 'д'),
            Trigram('и', ' ', 'ч'),
            Trigram('а', 'н', 'и'),
            Trigram('и', 'л', 'и'),
            Trigram('в', 'с', 'е'),
            Trigram('л', 'и', ' '),
            Trigram('т', 'в', 'о'),
            Trigram('и', ' ', 'с'),
            Trigram('н', 'и', 'е'),
            Trigram('в', 'о', 'т'),
            Trigram('а', ' ', 'в'),
            Trigram('в', 'а', 'т'),
            Trigram('м', 'а', ' '),
            Trigram(' ', 'р', 'а'),
            Trigram('и', ' ', 'п'),
            Trigram('и', ' ', 'н'),
            Trigram(' ', 'в', ' '),
            Trigram('е', 'к', ' '),
            Trigram('с', 'е', 'к'),
            Trigram('е', 'к', 'и'),
            Trigram('а', ' ', 'о'),
            Trigram(' ', 'и', 'л'),
            Trigram('е', ' ', 'и'),
            Trigram('п', 'р', 'и'),
            Trigram(' ', 'с', 'е'),
            Trigram('о', 'в', 'а'),
            Trigram('е', 'т', 'о'),
            Trigram('а', 'т', 'а'),
            Trigram('в', 'о', 'б'),
            Trigram('о', 'б', 'о'),
            Trigram('б', 'о', 'д'),
            Trigram('а', 'ц', 'и'),
            Trigram('а', 'т', ' '),
            Trigram('п', 'р', 'е'),
            Trigram('о', 'д', 'и'),
            Trigram('к', ' ', 'и'),
            Trigram(' ', 'б', 'ъ'),
            Trigram(' ', 'с', 'ъ'),
            Trigram('р', 'а', 'з'),
            Trigram(' ', 'о', 'с'),
            Trigram('р', 'е', 'д'),
            Trigram(' ', 'к', 'а'),
            Trigram('а', ' ', 'б'),
            Trigram('о', ' ', 'д'),
            Trigram('с', 'е', ' '),
            Trigram(' ', 'к', 'о'),
            Trigram('б', 'ъ', 'д'),
            Trigram('л', 'н', 'о'),
            Trigram('н', 'и', 'я'),
            Trigram('о', ' ', 'п'),
            Trigram(' ', 'о', 'т'),
            Trigram('ъ', 'д', 'е'),
            Trigram('о', ' ', 'в'),
            Trigram('з', 'а', ' '),
            Trigram('я', 'т', 'а'),
            Trigram(' ', 'е', ' '),
            Trigram(' ', 'т', 'р'),
            Trigram('и', ' ', 'и'),
            Trigram('о', ' ', 'с'),
            Trigram('т', 'е', 'л'),
            Trigram('и', ' ', 'в'),
            Trigram('н', 'и', 'т'),
            Trigram('е', ' ', 'с'),
            Trigram('р', 'а', 'н'),
            Trigram(' ', 'д', 'е'),
            Trigram('о', 'т', ' '),
            Trigram('о', 'б', 'щ'),
            Trigram('д', 'е', ' '),
            Trigram('к', 'а', ' '),
            Trigram('б', 'р', 'а'),
            Trigram('е', 'н', ' '),
            Trigram('я', 'в', 'а'),
            Trigram('ц', 'и', 'я'),
            Trigram('п', 'р', 'о'),
            Trigram('а', 'л', 'н'),
            Trigram('и', ' ', 'о'),
            Trigram('и', 'я', 'т'),
            Trigram('с', 'т', ' '),
            Trigram('н', 'о', 'в'),
            Trigram(' ', 'д', 'о'),
            Trigram('е', 'г', 'о'),
            Trigram('к', 'а', 'к'),
            Trigram('а', 'т', 'о'),
            Trigram(' ', 'и', 'з'),
            Trigram('н', 'е', 'г'),
            Trigram('а', ' ', 'т'),
            Trigram('д', 'е', 'н'),
            Trigram('а', ' ', 'к'),
            Trigram('щ', 'е', 'с'),
            Trigram('а', ' ', 'р'),
            Trigram('т', 'р', 'я'),
            Trigram('а', ' ', 'ч'),
            Trigram('р', 'я', 'б'),
            Trigram('о', ' ', 'о'),
            Trigram('в', 'е', 'н'),
            Trigram('я', 'б', 'в'),
            Trigram('б', 'в', 'а'),
            Trigram('д', 'ъ', 'р'),
            Trigram('г', 'о', 'в'),
            Trigram('н', 'а', 'ц'),
            Trigram('е', 'н', 'о'),
            Trigram('т', 'в', 'е'),
            Trigram('ъ', 'р', 'ж'),
            Trigram('е', ' ', 'д'),
            Trigram('н', 'о', 'с'),
            Trigram('р', 'ж', 'а'),
            Trigram('а', ' ', 'з'),
            Trigram('в', 'и', 'т'),
            Trigram('з', 'и', ' '),
            Trigram('а', 'к', 'в'),
            Trigram('л', 'е', 'н'),
            Trigram(' ', 'т', 'а'),
            Trigram('е', 'ж', 'д'),
            Trigram('и', ' ', 'з'),
            Trigram('р', 'о', 'д'),
            Trigram('е', ' ', 'о'),
            Trigram('о', 'б', 'р'),
            Trigram('н', 'о', 'т'),
            Trigram(' ', 'н', 'и'),
            Trigram(' ', 'с', ' '),
            Trigram('т', ' ', 'с'),
            Trigram('н', 'а', 'р'),
            Trigram('о', ' ', 'т'),
            Trigram('о', 'н', 'а'),
            Trigram('е', 'з', ' '),
            Trigram('й', 'с', 'т'),
            Trigram('к', 'а', 'т'),
            Trigram('и', 'ч', 'е'),
            Trigram(' ', 'б', 'е'),
            Trigram('ж', 'а', 'в'),
            Trigram('е', ' ', 'т'),
            Trigram('е', ' ', 'в'),
            Trigram('т', 'в', 'а'),
            Trigram('з', 'а', 'к'),
            Trigram('а', 'р', 'о'),
            Trigram('к', 'о', 'й'),
            Trigram('о', 'с', 'н'),
            Trigram(' ', 'л', 'и'),
            Trigram('у', 'в', 'а'),
            Trigram('а', 'в', 'н'),
            Trigram('е', 'й', 'с'),
            Trigram('с', 'н', 'о'),
            Trigram('р', 'е', 'с'),
            Trigram('п', 'о', 'л'),
            Trigram('н', 'е', 'н'),
            Trigram('в', 'н', 'и'),
            Trigram('б', 'е', 'з'),
            Trigram('р', 'и', ' '),
            Trigram('с', 'т', 'р'),
            Trigram(' ', 'с', 'т'),
            Trigram('с', 'т', 'о'),
            Trigram('п', 'о', 'д'),
            Trigram('ч', 'к', 'и'),
            Trigram('в', 'и', 'д'),
            Trigram('г', 'а', 'н'),
            Trigram('с', 'и', ' '),
            Trigram('д', 'и', ' '),
            Trigram('и', ' ', 'к'),
            Trigram('н', 'с', 'т'),
            Trigram(' ', 'т', 'е'),
            Trigram('а', ' ', 'е'),
            Trigram('в', 'с', 'и'),
            Trigram('е', 'о', 'б'),
            Trigram(' ', 'д', 'ъ'),
            Trigram('с', 'и', 'ч'),
            Trigram('и', 'ч', 'к'),
            Trigram('е', 'д', 'в'),
            Trigram('ж', 'е', 'н'),
            Trigram('н', 'и', 'к'),
            Trigram('о', 'д', 'а'),
            Trigram('т', ' ', 'н'),
            Trigram('о', ' ', 'р'),
            Trigram('а', 'к', 'а'),
            Trigram('е', 'л', 'и'),
            Trigram('о', 'д', 'н'),
            Trigram('е', 'л', 'н'),
            Trigram('л', 'и', 'ч'),
            Trigram(' ', 'ч', 'е'),
            Trigram('ч', 'е', 'с'),
            Trigram('б', 'щ', 'е'),
            Trigram(' ', 'р', 'е'),
            Trigram('и', ' ', 'м'),
            Trigram(' ', 'с', 'р'),
            Trigram('с', 'р', 'е'),
            Trigram('и', ' ', 'р'),
            Trigram('с', 'а', ' '),
            Trigram('л', 'н', 'и'),
            Trigram(' ', 'с', 'и'),
            Trigram('д', 'в', 'и'),
            Trigram('и', 'ч', 'н'),
            Trigram('ж', 'д', 'а'),
            Trigram(' ', 'к', 'ъ'),
            Trigram('о', 'е', 'т'),
            Trigram('и', 'р', 'а'),
            Trigram('я', ' ', 'н'),
            Trigram('д', 'е', 'й'),
            Trigram(' ', 'м', 'е'),
            Trigram('е', 'д', 'и'),
            Trigram('д', 'р', 'у'),
            Trigram('х', 'о', 'д'),
            Trigram('е', 'м', 'е'),
            Trigram('к', 'р', 'и'),
            Trigram('ч', 'е', ' '),
            Trigram('д', 'о', 'с'),
            Trigram('с', 'т', 'а'),
            Trigram('г', 'р', 'а'),
            Trigram(' ', 'т', 'о'),
            Trigram('о', 'й', ' '),
            Trigram('т', 'ъ', 'п'),
            Trigram('в', 'ъ', 'з'),
            Trigram('и', 'к', 'о'),
            Trigram('и', ' ', 'у'),
            Trigram('н', 'е', 'т'),
            Trigram(' ', 'с', 'о'),
            Trigram('а', 'в', 'и'),
            Trigram('т', 'о', 'й'),
            Trigram('е', 'л', 'с'),
            Trigram('м', 'е', 'ж'),
            Trigram('ч', 'и', 'т'),
            Trigram('и', 'т', 'а'),
            Trigram('щ', 'о', ' '),
            Trigram('ъ', 'м', ' '),
            Trigram('а', 'з', 'о'),
            Trigram('з', 'о', 'в'),
            Trigram('н', 'и', 'ч'),
            Trigram('н', 'а', 'л'),
            Trigram('д', 'н', 'о'),
            Trigram(' ', 'м', 'о'),
            Trigram('и', 'н', 'е'),
            Trigram('а', ' ', 'у'),
            Trigram('т', 'н', 'о'),
            Trigram('т', 'а', 'з'),
            Trigram('к', 'о', 'н'),
            Trigram('л', 'и', 'т'),
            Trigram('а', 'н', ' '),
            Trigram('к', 'л', 'ю'),
            Trigram('л', 'ю', 'ч'),
            Trigram('п', 'о', 'с'),
            Trigram('т', 'в', 'и'),
            Trigram('а', ' ', 'м'),
            Trigram('й', ' ', 'н'),
            Trigram('т', ' ', 'и'),
            Trigram('и', 'з', 'в'),
            Trigram('р', 'е', 'з'),
            Trigram('а', 'з', 'и'),
            Trigram('р', 'а', ' '),
            Trigram('о', 'я', 'т'),
            Trigram('н', 'е', 'о'),
            Trigram('ч', 'р', 'е'),
        ],
    ),
    (
        Lang::Mkd,
        &[
            Trigram(' ', 'н', 'а'),
            Trigram('н', 'а', ' '),
            Trigram(' ', 'п', 'р'),
            Trigram(' ', 'и', ' '),
            Trigram('в', 'о', ' '),
            Trigram(' ', 'с', 'е'),
            Trigram('т', 'о', ' '),
            Trigram('и', 'т', 'е'),
            Trigram('т', 'е', ' '),
            Trigram('р', 'а', 'в'),
            Trigram('т', 'а', ' '),
            Trigram('а', ' ', 'с'),
            Trigram('п', 'р', 'а'),
            Trigram('у', 'в', 'а'),
            Trigram('д', 'а', ' '),
            Trigram(' ', 'д', 'а'),
            Trigram(' ', 'н', 'е'),
            Trigram('в', 'а', ' '),
            Trigram('а', ' ', 'п'),
            Trigram('а', ' ', 'н'),
            Trigram('и', ' ', 'с'),
            Trigram('а', 'т', 'а'),
            Trigram('о', ' ', 'н'),
            Trigram('е', 'к', 'о'),
            Trigram('а', ' ', 'и'),
            Trigram(' ', 'п', 'о'),
            Trigram('н', 'о', ' '),
            Trigram('о', 'ј', ' '),
            Trigram('к', 'о', 'ј'),
            Trigram(' ', 'с', 'о'),
            Trigram(' ', 'з', 'а'),
            Trigram(' ', 'в', 'о'),
            Trigram('с', 'т', 'в'),
            Trigram('ј', 'а', ' '),
            Trigram('њ', 'е', ' '),
            Trigram('а', 'њ', 'е'),
            Trigram('а', 'в', 'о'),
            Trigram('н', 'и', ' '),
            Trigram(' ', 'и', 'м'),
            Trigram('о', 'т', ' '),
            Trigram('е', ' ', 'п'),
            Trigram('е', ' ', 'н'),
            Trigram('м', 'а', ' '),
            Trigram('а', 'т', ' '),
            Trigram('в', 'а', 'њ'),
            Trigram('о', 'с', 'т'),
            Trigram('а', ' ', 'д'),
            Trigram('о', ' ', 'с'),
            Trigram('е', ' ', 'и'),
            Trigram('с', 'е', ' '),
            Trigram('о', 'в', 'а'),
            Trigram('и', 'ј', 'а'),
            Trigram('и', ' ', 'п'),
            Trigram(' ', 'с', 'л'),
            Trigram('а', ' ', 'о'),
            Trigram('и', 'м', 'а'),
            Trigram('с', 'е', 'к'),
            Trigram('с', 'л', 'о'),
            Trigram('о', 'т', 'о'),
            Trigram('л', 'и', ' '),
            Trigram('о', ' ', 'д'),
            Trigram('а', 'в', 'а'),
            Trigram('о', 'б', 'о'),
            Trigram('о', ' ', 'и'),
            Trigram(' ', 'и', 'л'),
            Trigram('и', 'л', 'и'),
            Trigram(' ', 'б', 'и'),
            Trigram('б', 'о', 'д'),
            Trigram('и', ' ', 'н'),
            Trigram('л', 'о', 'б'),
            Trigram(' ', 'о', 'д'),
            Trigram('б', 'и', 'д'),
            Trigram('р', 'е', 'д'),
            Trigram('е', 'н', ' '),
            Trigram('п', 'р', 'и'),
            Trigram('в', 'о', 'т'),
            Trigram('и', 'д', 'е'),
            Trigram('а', ' ', 'в'),
            Trigram('с', 'т', 'а'),
            Trigram(' ', 'о', 'б'),
            Trigram('и', ' ', 'и'),
            Trigram('и', ' ', 'д'),
            Trigram('п', 'р', 'е'),
            Trigram('н', 'о', 'с'),
            Trigram('с', 'т', ' '),
            Trigram('е', ' ', 'с'),
            Trigram(' ', 'н', 'и'),
            Trigram(' ', 'ќ', 'е'),
            Trigram('о', 'в', 'е'),
            Trigram('а', 'а', 'т'),
            Trigram('а', 'ц', 'и'),
            Trigram('ќ', 'е', ' '),
            Trigram('с', 'о', ' '),
            Trigram('о', 'в', 'и'),
            Trigram('п', 'р', 'о'),
            Trigram('ј', ' ', 'и'),
            Trigram('т', 'в', 'о'),
            Trigram(' ', 'р', 'а'),
            Trigram('е', 'с', 'т'),
            Trigram('ш', 'т', 'о'),
            Trigram(' ', 'д', 'е'),
            Trigram('т', ' ', 'и'),
            Trigram('а', 'к', 'в'),
            Trigram(' ', 'к', 'о'),
            Trigram('р', 'а', 'з'),
            Trigram('г', 'о', 'в'),
            Trigram('е', 'г', 'о'),
            Trigram('н', 'е', 'г'),
            Trigram('а', 'н', 'и'),
            Trigram('е', 'д', 'н'),
            Trigram('а', 'к', 'о'),
            Trigram('ц', 'и', 'ј'),
            Trigram('б', 'р', 'а'),
            Trigram('о', 'д', ' '),
            Trigram('а', ' ', 'з'),
            Trigram('е', ' ', 'б'),
            Trigram('и', ' ', 'о'),
            Trigram('а', ' ', 'б'),
            Trigram('о', ' ', 'п'),
            Trigram('в', 'а', 'т'),
            Trigram(' ', 'е', ' '),
            Trigram(' ', 'д', 'р'),
            Trigram('е', 'т', 'о'),
            Trigram('в', 'а', 'а'),
            Trigram('к', 'а', 'к'),
            Trigram('д', 'и', ' '),
            Trigram('т', ' ', 'с'),
            Trigram(' ', 'к', 'а'),
            Trigram(' ', 'ч', 'о'),
            Trigram('е', 'н', 'и'),
            Trigram('а', 'л', 'н'),
            Trigram('о', 'д', 'н'),
            Trigram('е', 'н', 'о'),
            Trigram(' ', 'с', 'и'),
            Trigram('ч', 'о', 'в'),
            Trigram(' ', 'ш', 'т'),
            Trigram('а', ' ', 'г'),
            Trigram('а', ' ', 'е'),
            Trigram('в', 'е', 'н'),
            Trigram('н', 'и', 'т'),
            Trigram(' ', 'ј', 'а'),
            Trigram('д', 'е', ' '),
            Trigram('о', 'д', 'и'),
            Trigram('е', ' ', 'о'),
            Trigram('р', 'а', 'н'),
            Trigram('и', ' ', 'з'),
            Trigram('с', 'н', 'о'),
            Trigram('н', 'о', 'т'),
            Trigram(' ', 'е', 'д'),
            Trigram('т', 'и', 'т'),
            Trigram('л', 'н', 'о'),
            Trigram('в', 'и', ' '),
            Trigram('ј', 'а', 'т'),
            Trigram('д', 'е', 'н'),
            Trigram('т', ' ', 'н'),
            Trigram('н', 'а', 'ц'),
            Trigram(' ', 'о', 'п'),
            Trigram(' ', 'д', 'о'),
            Trigram(' ', 'о', 'с'),
            Trigram('и', ' ', 'в'),
            Trigram('о', 'с', 'н'),
            Trigram('к', 'о', 'н'),
            Trigram('д', 'н', 'а'),
            Trigram('е', ' ', 'д'),
            Trigram(' ', 'с', 'т'),
            Trigram('в', 'е', 'к'),
            Trigram('о', ' ', 'о'),
            Trigram('р', 'о', 'д'),
            Trigram('с', 'т', 'о'),
            Trigram('с', 'и', 'т'),
            Trigram('е', 'м', 'е'),
            Trigram('а', 'р', 'а'),
            Trigram('д', 'н', 'о'),
            Trigram('о', 'б', 'р'),
            Trigram('ј', ' ', 'н'),
            Trigram('п', 'ш', 'т'),
            Trigram('е', 'д', 'и'),
            Trigram('о', 'п', 'ш'),
            Trigram('з', 'а', ' '),
            Trigram('н', 'и', 'е'),
            Trigram('а', 'р', 'о'),
            Trigram('н', 'о', 'в'),
            Trigram('а', ' ', 'к'),
            Trigram('в', 'н', 'и'),
            Trigram('д', 'р', 'у'),
            Trigram(' ', 'о', 'в'),
            Trigram('т', 'в', 'е'),
            Trigram('ж', 'и', 'в'),
            Trigram('ш', 'т', 'е'),
            Trigram('д', ' ', 'н'),
            Trigram('и', 'е', ' '),
            Trigram(' ', 'м', 'е'),
            Trigram('е', 'д', ' '),
            Trigram('и', 'о', 'т'),
            Trigram('и', ' ', 'м'),
            Trigram('о', ' ', 'в'),
            Trigram('ќ', 'и', ' '),
            Trigram('д', 'а', 'т'),
            Trigram('ш', 'т', 'и'),
            Trigram('ј', 'ќ', 'и'),
            Trigram('б', 'е', 'з'),
            Trigram('б', 'е', 'д'),
            Trigram('к', 'и', ' '),
            Trigram('к', 'о', 'в'),
            Trigram('к', 'о', ' '),
            Trigram('а', ' ', 'р'),
            Trigram('н', 'а', 'р'),
            Trigram('ч', 'н', 'о'),
            Trigram('д', 'н', 'и'),
            Trigram(' ', 'в', 'р'),
            Trigram('е', 'л', 'и'),
            Trigram('н', 'а', 'к'),
            Trigram('а', 'ш', 'т'),
            Trigram('и', 'ч', 'н'),
            Trigram('к', 'а', ' '),
            Trigram('е', 'м', 'а'),
            Trigram('ц', 'е', 'л'),
            Trigram('з', 'е', 'м'),
            Trigram('е', 'д', 'у'),
            Trigram('ч', 'у', 'в'),
            Trigram('т', 'е', 'с'),
            Trigram('д', 'р', 'ж'),
            Trigram('н', 'и', 'к'),
            Trigram('т', ' ', 'п'),
            Trigram('л', 'у', 'ч'),
            Trigram('а', 'а', ' '),
            Trigram('д', 'е', 'ј'),
            Trigram('н', 'с', 'т'),
            Trigram('н', 'е', ' '),
            Trigram('а', ' ', 'ч'),
            Trigram('р', 'у', 'г'),
            Trigram('о', 'д', 'а'),
            Trigram('и', 'в', 'н'),
            Trigram(' ', 'ц', 'е'),
            Trigram('н', 'и', 'в'),
            Trigram('д', 'и', 'н'),
            Trigram('а', 'в', 'н'),
            Trigram(' ', 'з', 'е'),
            Trigram('н', 'и', 'о'),
            Trigram('п', 'о', 'р'),
            Trigram('а', ' ', 'м'),
            Trigram('з', 'а', 'ш'),
            Trigram('л', 'а', 'с'),
            Trigram('в', 'и', 'т'),
            Trigram('д', 'е', 'к'),
            Trigram('г', 'о', ' '),
            Trigram('и', 'н', 'е'),
            Trigram('е', 'л', 'о'),
            Trigram('н', 'е', 'т'),
            Trigram('е', 'з', ' '),
            Trigram('т', 'е', 'н'),
            Trigram(' ', 'р', 'е'),
            Trigram(' ', 'и', 'з'),
            Trigram('п', 'о', 'д'),
            Trigram('р', 'а', 'б'),
            Trigram('а', 'б', 'о'),
            Trigram('б', 'о', 'т'),
            Trigram('д', 'у', 'в'),
            Trigram('н', 'у', 'в'),
            Trigram(' ', 'б', 'е'),
            Trigram('е', 'њ', 'е'),
            Trigram('е', 'д', 'е'),
            Trigram('о', 'н', ' '),
            Trigram('њ', 'е', 'т'),
            Trigram('з', 'о', 'в'),
            Trigram('и', 'т', 'у'),
            Trigram('в', 'а', 'н'),
            Trigram('н', ' ', 'и'),
            Trigram('а', 'ѓ', 'а'),
            Trigram('е', ' ', 'в'),
            Trigram('е', 'ѓ', 'у'),
            Trigram('р', 'е', 'м'),
            Trigram('д', 'е', 'л'),
            Trigram('о', ' ', 'к'),
            Trigram('к', 'о', 'т'),
            Trigram('и', 'м', ' '),
            Trigram(' ', 'ж', 'и'),
            Trigram('д', 'о', 'с'),
            Trigram('в', 'р', 'е'),
            Trigram('м', 'е', 'ѓ'),
            Trigram('о', 'л', 'н'),
            Trigram('н', 'а', 'п'),
            Trigram(' ', 'г', 'о'),
            Trigram('е', 'м', 'ј'),
            Trigram('к', 'р', 'и'),
            Trigram('у', 'н', 'а'),
            Trigram('н', 'е', 'м'),
            Trigram('о', 'ј', 'а'),
            Trigram(' ', 'с', 'у'),
            Trigram('и', 'т', 'а'),
            Trigram('а', 'з', 'о'),
            Trigram('л', 'и', 'т'),
            Trigram('т', 'о', 'р'),
            Trigram('и', 'н', 'с'),
            Trigram('о', 'р', 'а'),
            Trigram('о', 'г', 'л'),
            Trigram('и', 'п', 'а'),
            Trigram('п', 'о', 'т'),
            Trigram('с', 'л', 'у'),
            Trigram('к', 'в', 'и'),
        ],
    ),
];

/// Languages for script Arabic
pub static ARABIC_LANGS: LangProfileList = &[
    (
        Lang::Ara,
        &[
            Trigram(' ', 'ا', 'ل'),
            Trigram('ي', 'ة', ' '),
            Trigram(' ', 'ف', 'ي'),
            Trigram('ا', 'ل', 'ح'),
            Trigram('ف', 'ي', ' '),
            Trigram(' ', 'و', 'ا'),
            Trigram('و', 'ا', 'ل'),
            Trigram(' ', 'أ', 'و'),
            Trigram('ة', ' ', 'ا'),
            Trigram('أ', 'و', ' '),
            Trigram('ا', 'ل', 'م'),
            Trigram('ا', 'ل', 'ت'),
            Trigram('ل', 'ح', 'ق'),
            Trigram('ح', 'ق', ' '),
            Trigram('ل', 'ى', ' '),
            Trigram('ك', 'ل', ' '),
            Trigram('ا', 'ن', ' '),
            Trigram('ة', ' ', 'و'),
            Trigram('ا', 'ل', 'أ'),
            Trigram(' ', 'ل', 'ك'),
            Trigram('ل', 'ك', 'ل'),
            Trigram('ن', ' ', 'ا'),
            Trigram('ه', 'ا', ' '),
            Trigram('ق', ' ', 'ف'),
            Trigram('ا', 'ت', ' '),
            Trigram('م', 'ة', ' '),
            Trigram('و', 'ن', ' '),
            Trigram('أ', 'ن', ' '),
            Trigram('م', 'ا', ' '),
            Trigram('ا', 'ء', ' '),
            Trigram('ت', 'ه', ' '),
            Trigram('و', ' ', 'ا'),
            Trigram('ا', 'ل', 'ع'),
            Trigram('ي', ' ', 'ا'),
            Trigram('ش', 'خ', 'ص'),
            Trigram('ي', ' ', 'أ'),
            Trigram(' ', 'أ', 'ن'),
            Trigram('ا', 'ل', 'إ'),
            Trigram('م', ' ', 'ا'),
            Trigram('ح', 'ر', 'ي'),
            Trigram(' ', 'ع', 'ل'),
            Trigram('ة', ' ', 'ل'),
            Trigram('م', 'ن', ' '),
            Trigram('ا', 'ل', 'ا'),
            Trigram('ح', 'ق', 'و'),
            Trigram('ع', 'ل', 'ى'),
            Trigram('ق', 'و', 'ق'),
            Trigram('ت', ' ', 'ا'),
            Trigram('أ', 'ي', ' '),
            Trigram('ر', 'د', ' '),
            Trigram(' ', 'ش', 'خ'),
            Trigram(' ', 'ل', 'ل'),
            Trigram(' ', 'أ', 'ي'),
            Trigram('ق', ' ', 'ا'),
            Trigram('ل', 'ا', ' '),
            Trigram('ف', 'ر', 'د'),
            Trigram('ر', 'ي', 'ة'),
            Trigram(' ', 'و', 'ل'),
            Trigram(' ', 'م', 'ن'),
            Trigram('د', ' ', 'ا'),
            Trigram(' ', 'ك', 'ا'),
            Trigram(' ', 'إ', 'ل'),
            Trigram('خ', 'ص', ' '),
            Trigram('و', 'ق', ' '),
            Trigram('ا', ' ', 'ا'),
            Trigram('ة', ' ', 'أ'),
            Trigram('ا', ' ', 'ي'),
            Trigram('ل', ' ', 'ف'),
            Trigram('ه', ' ', 'ا'),
            Trigram('ن', 'س', 'ا'),
            Trigram('ج', 'ت', 'م'),
            Trigram('ن', ' ', 'ي'),
            Trigram('ا', 'م', 'ة'),
            Trigram('ك', 'ا', 'ن'),
            Trigram('د', 'ة', ' '),
            Trigram(' ', 'ح', 'ق'),
            Trigram('ا', 'م', ' '),
            Trigram('ا', 'ل', 'ق'),
            Trigram('ة', ' ', 'م'),
            Trigram(' ', 'ف', 'ر'),
            Trigram('ا', 'ي', 'ة'),
            Trigram('س', 'ا', 'ن'),
            Trigram('ل', ' ', 'ش'),
            Trigram('ي', 'ن', ' '),
            Trigram('ن', ' ', 'ت'),
            Trigram('إ', 'ن', 'س'),
            Trigram('ا', ' ', 'ل'),
            Trigram(' ', 'ل', 'ا'),
            Trigram('ذ', 'ا', ' '),
            Trigram('ه', 'ذ', 'ا'),
            Trigram('ن', ' ', 'أ'),
            Trigram('ل', 'ة', ' '),
            Trigram('ي', ' ', 'ح'),
            Trigram(' ', 'د', 'و'),
            Trigram('ه', ' ', 'ل'),
            Trigram('ل', 'ك', ' '),
            Trigram('ت', 'ر', 'ا'),
            Trigram('ل', 'ت', 'ع'),
            Trigram('ا', 'ً', ' '),
            Trigram('ل', 'ه', ' '),
            Trigram('إ', 'ل', 'ى'),
            Trigram(' ', 'ع', 'ن'),
            Trigram('ى', ' ', 'ا'),
            Trigram('ه', ' ', 'و'),
            Trigram('ع', ' ', 'ا'),
            Trigram('م', 'ا', 'ع'),
            Trigram('د', ' ', 'أ'),
            Trigram('ا', 'س', 'ي'),
            Trigram(' ', 'ح', 'ر'),
            Trigram('ة', ' ', 'ع'),
            Trigram('م', 'ع', ' '),
            Trigram('ا', 'ل', 'د'),
            Trigram('ن', 'و', 'ن'),
            Trigram(' ', 'ب', 'ا'),
            Trigram('ل', 'ح', 'ر'),
            Trigram('ل', 'ع', 'ا'),
            Trigram('ن', ' ', 'و'),
            Trigram('،', ' ', 'و'),
            Trigram('ي', 'ا', 'ت'),
            Trigram('ي', ' ', 'ت'),
            Trigram('ا', 'ل', 'ج'),
            Trigram(' ', 'ه', 'ذ'),
            Trigram('ي', 'ر', ' '),
            Trigram('ب', 'ا', 'ل'),
            Trigram('د', 'و', 'ل'),
            Trigram('ل', 'إ', 'ن'),
            Trigram('ع', 'ي', 'ة'),
            Trigram('ا', 'ل', 'ف'),
            Trigram('ص', ' ', 'ا'),
            Trigram(' ', 'و', 'ي'),
            Trigram('ا', 'ل', 'و'),
            Trigram('ل', 'أ', 'س'),
            Trigram(' ', 'إ', 'ن'),
            Trigram('أ', 'س', 'ا'),
            Trigram('س', 'ا', 'س'),
            Trigram('م', 'ا', 'ي'),
            Trigram('ح', 'م', 'ا'),
            Trigram('ر', 'ا', 'م'),
            Trigram('س', 'ي', 'ة'),
            Trigram('ا', 'ن', 'و'),
            Trigram('م', 'ل', ' '),
            Trigram('ي', ' ', 'و'),
            Trigram('ع', 'ا', 'م'),
            Trigram('ا', ' ', 'و'),
            Trigram('ت', 'م', 'ا'),
            Trigram(' ', 'م', 'ت'),
            Trigram('ة', ' ', 'ت'),
            Trigram('ع', 'ل', 'ي'),
            Trigram('ع', ' ', 'ب'),
            Trigram('ك', ' ', 'ا'),
            Trigram(' ', 'ل', 'ه'),
            Trigram('ة', ' ', 'ف'),
            Trigram('ق', 'ا', 'ن'),
            Trigram('ى', ' ', 'أ'),
            Trigram('و', 'ل', ' '),
            Trigram('ه', 'م', ' '),
            Trigram('ا', 'ل', 'ب'),
            Trigram('ة', ' ', 'ب'),
            Trigram('س', 'ا', 'و'),
            Trigram('ل', 'ق', 'ا'),
            Trigram('ا', 'ل', 'ر'),
            Trigram('ل', 'ج', 'م'),
            Trigram('ا', ' ', 'ك'),
            Trigram('ت', 'م', 'ت'),
            Trigram('ل', 'ي', 'ه'),
            Trigram('ل', 'ت', 'م'),
            Trigram('ل', 'م', 'ت'),
            Trigram('ا', 'ن', 'ت'),
            Trigram(' ', 'ق', 'د'),
            Trigram('ا', 'د', ' '),
            Trigram('ه', ' ', 'أ'),
            Trigram(' ', 'ي', 'ج'),
            Trigram('ر', 'ي', 'ا'),
            Trigram('ق', ' ', 'و'),
            Trigram('ل', ' ', 'ا'),
            Trigram('ا', ' ', 'ب'),
            Trigram('ا', 'ل', ' '),
            Trigram('ي', 'ه', ' '),
            Trigram('ا', 'ع', 'ي'),
            Trigram('ل', 'د', 'و'),
            Trigram('ل', ' ', 'و'),
            Trigram('ل', 'إ', 'ع'),
            Trigram('ل', 'م', 'ي'),
            Trigram('ل', 'م', 'ج'),
            Trigram('ل', 'أ', 'م'),
            Trigram('ت', 'ع', ' '),
            Trigram('د', 'م', ' '),
            Trigram('ت', 'س', 'ا'),
            Trigram('ع', 'م', 'ل'),
            Trigram('ا', 'ت', 'ه'),
            Trigram('ل', 'ا', 'د'),
            Trigram('ر', 'ة', ' '),
            Trigram('ا', 'ة', ' '),
            Trigram('غ', 'ي', 'ر'),
            Trigram('ق', 'د', 'م'),
            Trigram('و', 'ز', ' '),
            Trigram('ج', 'و', 'ز'),
            Trigram('ي', 'ج', 'و'),
            Trigram('ع', 'ا', 'ل'),
            Trigram('ل', 'ا', 'ن'),
            Trigram('م', 'ت', 'ع'),
            Trigram('م', 'ا', 'ن'),
            Trigram('ف', 'ي', 'ه'),
            Trigram('ا', 'ج', 'ت'),
            Trigram('م', ' ', 'و'),
            Trigram('ي', 'د', ' '),
            Trigram('ت', 'ع', 'ل'),
            Trigram('ن', ' ', 'ل'),
            Trigram('ر', ' ', 'ا'),
            Trigram(' ', 'ي', 'ع'),
            Trigram(' ', 'ك', 'ل'),
            Trigram('م', 'م', ' '),
            Trigram('م', 'ج', 'ت'),
            Trigram('ت', 'م', 'ع'),
            Trigram('د', 'و', 'ن'),
            Trigram(' ', 'م', 'ع'),
            Trigram('ت', 'م', 'ي'),
            Trigram('ذ', 'ل', 'ك'),
            Trigram('ك', 'ر', 'ا'),
            Trigram('ي', 'ه', 'ا'),
            Trigram(' ', 'م', 'س'),
            Trigram('م', 'ي', 'ع'),
            Trigram('إ', 'ع', 'ل'),
            Trigram('ع', 'ل', 'ا'),
            Trigram(' ', 'ت', 'م'),
            Trigram(' ', 'ع', 'ا'),
            Trigram('م', 'ل', 'ا'),
            Trigram('ا', 'ع', 'ا'),
            Trigram('ل', 'ا', 'ج'),
            Trigram('ن', 'ي', ' '),
            Trigram('ل', 'ي', 'م'),
            Trigram('م', 'ت', 'س'),
            Trigram('ي', 'ي', 'ز'),
            Trigram('ي', 'م', ' '),
            Trigram('ا', 'ع', 'ت'),
            Trigram('ا', 'ل', 'ش'),
            Trigram(' ', 'ت', 'ع'),
            Trigram('م', 'ي', 'ي'),
            Trigram('ع', 'ن', ' '),
            Trigram('ت', 'ن', 'ا'),
            Trigram(' ', 'ب', 'ح'),
            Trigram('ل', 'م', 'ا'),
            Trigram('ي', ' ', 'ي'),
            Trigram('ي', 'ز', ' '),
            Trigram('و', 'د', ' '),
            Trigram('أ', 'م', 'م'),
            Trigram('ل', 'ا', 'ت'),
            Trigram('أ', 'س', 'ر'),
            Trigram('ش', 'ت', 'ر'),
            Trigram('ت', 'ي', ' '),
            Trigram(' ', 'ج', 'م'),
            Trigram('ه', ' ', 'ع'),
            Trigram('ر', ' ', 'و'),
            Trigram('ي', ' ', 'إ'),
            Trigram('ت', 'ح', 'د'),
            Trigram('ح', 'د', 'ة'),
            Trigram(' ', 'أ', 'س'),
            Trigram('ع', 'ة', ' '),
            Trigram('ي', ' ', 'م'),
            Trigram('ة', '،', ' '),
            Trigram('م', 'ع', 'ي'),
            Trigram('ن', ' ', 'م'),
            Trigram('ل', 'م', 'س'),
            Trigram('م', ' ', 'ب'),
            Trigram('ا', 'ق', ' '),
            Trigram('ج', 'م', 'ي'),
            Trigram('ل', 'ي', ' '),
            Trigram('م', 'ي', 'ة'),
            Trigram('ا', 'ل', 'ض'),
            Trigram('ا', 'ل', 'س'),
            Trigram('ل', 'ض', 'م'),
            Trigram('ض', 'م', 'ا'),
            Trigram('ل', 'ف', 'ر'),
            Trigram(' ', 'و', 'س'),
            Trigram('ل', 'ح', 'م'),
            Trigram('ا', 'م', 'ل'),
            Trigram('ق', ' ', 'م'),
            Trigram('ر', 'ا', ' '),
            Trigram('ا', ' ', 'ح'),
            Trigram('ن', 'ت', ' '),
            Trigram(' ', 'ت', 'ن'),
            Trigram('ي', 'ت', 'ه'),
            Trigram(' ', 'أ', 'م'),
            Trigram('إ', 'ل', 'ي'),
            Trigram('و', 'ا', 'ج'),
            Trigram('د', ' ', 'و'),
            Trigram('ل', 'ت', 'ي'),
            Trigram(' ', 'م', 'ر'),
            Trigram('م', 'ر', 'ا'),
            Trigram('م', 'ت', 'ح'),
            Trigram(' ', 'ذ', 'ل'),
            Trigram(' ', 'و', 'أ'),
            Trigram(' ', 'ت', 'ح'),
            Trigram('ا', ' ', 'ف'),
            Trigram(' ', 'ب', 'ه'),
            Trigram(' ', 'و', 'م'),
            Trigram(' ', 'ب', 'م'),
            Trigram('و', 'ي', 'ة'),
            Trigram('و', 'ل', 'ي'),
            Trigram('ل', 'ز', 'و'),
        ],
    ),
    (
        Lang::Urd,
        &[
            Trigram('و', 'ر', ' '),
            Trigram(' ', 'ا', 'و'),
            Trigram('ا', 'و', 'ر'),
            Trigram(' ', 'ک', 'ی'),
            Trigram('ک', 'ے', ' '),
            Trigram(' ', 'ک', 'ے'),
            Trigram('ی', 'ں', ' '),
            Trigram(' ', 'ک', 'ا'),
            Trigram('ک', 'ی', ' '),
            Trigram(' ', 'ح', 'ق'),
            Trigram('ے', ' ', 'ک'),
            Trigram('ا', 'ی', 'ٔ'),
            Trigram('ک', 'ا', ' '),
            Trigram('ی', 'ٔ', 'ے'),
            Trigram(' ', 'ک', 'و'),
            Trigram('ی', 'ا', ' '),
            Trigram('ن', 'ے', ' '),
            Trigram('س', 'ے', ' '),
            Trigram(' ', 'ا', 'س'),
            Trigram('ٔ', 'ے', ' '),
            Trigram('م', 'ی', 'ں'),
            Trigram('ک', 'و', ' '),
            Trigram(' ', 'ہ', 'ے'),
            Trigram(' ', 'م', 'ی'),
            Trigram('ے', ' ', 'ا'),
            Trigram(' ', 'ا', 'ن'),
            Trigram('و', 'ں', ' '),
            Trigram(' ', 'ک', 'ر'),
            Trigram(' ', 'ہ', 'و'),
            Trigram('ا', 'س', ' '),
            Trigram('ی', ' ', 'ا'),
            Trigram('ر', ' ', 'ا'),
            Trigram('ش', 'خ', 'ص'),
            Trigram(' ', 'ش', 'خ'),
            Trigram('ح', 'ق', ' '),
            Trigram(' ', 'س', 'ے'),
            Trigram(' ', 'ج', 'ا'),
            Trigram('خ', 'ص', ' '),
            Trigram('ہ', 'ر', ' '),
            Trigram('ا', 'م', ' '),
            Trigram('ے', ' ', 'م'),
            Trigram('ں', ' ', 'ک'),
            Trigram('ہ', 'ی', 'ں'),
            Trigram(' ', 'ی', 'ا'),
            Trigram('س', 'ی', ' '),
            Trigram('ا', 'د', 'ی'),
            Trigram('آ', 'ز', 'ا'),
            Trigram(' ', 'آ', 'ز'),
            Trigram('ز', 'ا', 'د'),
            Trigram('ص', ' ', 'ک'),
            Trigram('ہ', ' ', 'ا'),
            Trigram('ہ', 'ے', ' '),
            Trigram('ج', 'ا', 'ی'),
            Trigram('ا', ' ', 'ح'),
            Trigram('ر', ' ', 'ش'),
            Trigram('ت', ' ', 'ک'),
            Trigram('ک', 'ہ', ' '),
            Trigram('م', ' ', 'ک'),
            Trigram(' ', 'پ', 'ر'),
            Trigram('ی', ' ', 'ک'),
            Trigram('ا', 'ن', ' '),
            Trigram('پ', 'ر', ' '),
            Trigram('۔', 'ہ', 'ر'),
            Trigram('د', 'ی', ' '),
            Trigram('ی', 'ٔ', 'ی'),
            Trigram('س', ' ', 'ک'),
            Trigram('ا', ' ', 'ج'),
            Trigram('ر', ' ', 'م'),
            Trigram('ہ', 'ے', '۔'),
            Trigram('ق', ' ', 'ہ'),
            Trigram('ں', ' ', 'ا'),
            Trigram('ی', ' ', 'ح'),
            Trigram('و', ' ', 'ا'),
            Trigram('ا', 'ر', ' '),
            Trigram('ن', ' ', 'ک'),
            Trigram('ق', 'و', 'ق'),
            Trigram('ک', 'س', 'ی'),
            Trigram('ح', 'ق', 'و'),
            Trigram('ر', 'ی', ' '),
            Trigram('و', 'ق', ' '),
            Trigram('ے', ' ', 'گ'),
            Trigram(' ', 'ہ', 'ی'),
            Trigram('ی', ' ', 'ج'),
            Trigram(' ', 'م', 'ع'),
            Trigram('س', 'ا', 'ن'),
            Trigram(' ', 'ن', 'ہ'),
            Trigram(' ', 'م', 'ل'),
            Trigram(' ', 'ح', 'ا'),
            Trigram('ٔ', 'ی', ' '),
            Trigram(' ', 'ج', 'و'),
            Trigram('ن', 'ی', ' '),
            Trigram('ک', 'ر', 'ن'),
            Trigram(' ', 'ل', 'ی'),
            Trigram('ت', 'ی', ' '),
            Trigram('ی', ' ', 'ت'),
            Trigram('ن', 'س', 'ا'),
            Trigram('ل', ' ', 'ک'),
            Trigram(' ', 'ک', 'ہ'),
            Trigram('ج', 'و', ' '),
            Trigram('ا', 'ن', 'س'),
            Trigram('ا', 'پ', 'ن'),
            Trigram('ے', ' ', 'ب'),
            Trigram('ن', 'ہ', ' '),
            Trigram(' ', 'ا', 'پ'),
            Trigram('ی', 'ت', ' '),
            Trigram('ا', ' ', 'ا'),
            Trigram('ہ', ' ', 'ک'),
            Trigram(' ', 'ک', 'س'),
            Trigram('ر', ' ', 'ک'),
            Trigram('ر', 'ے', ' '),
            Trigram('ے', ' ', 'ہ'),
            Trigram(' ', 'ا', 'ی'),
            Trigram('م', 'ی', ' '),
            Trigram('ل', ' ', 'ہ'),
            Trigram('۔', ' ', 'ا'),
            Trigram('ے', ' ', 'ل'),
            Trigram('ی', ' ', 'ش'),
            Trigram('ر', 'ن', 'ے'),
            Trigram('و', 'ہ', ' '),
            Trigram('ح', 'ا', 'ص'),
            Trigram('ی', ' ', 'م'),
            Trigram('م', 'ع', 'ا'),
            Trigram('ا', 'ص', 'ل'),
            Trigram('ص', 'ل', ' '),
            Trigram('ی', 'ں', '۔'),
            Trigram('و', 'ی', 'ٔ'),
            Trigram('ن', 'ہ', 'ی'),
            Trigram('م', 'ل', 'ک'),
            Trigram('ا', 'ی', 'س'),
            Trigram('ا', 'ن', 'ہ'),
            Trigram('ا', 'ت', ' '),
            Trigram('ی', ' ', 'ب'),
            Trigram('د', ' ', 'ک'),
            Trigram('ی', ' ', 'ہ'),
            Trigram(' ', 'ت', 'ع'),
            Trigram('ک', 'ی', 'ا'),
            Trigram('ق', ' ', 'ک'),
            Trigram('ر', ' ', 'ہ'),
            Trigram('ا', ' ', 'م'),
            Trigram('د', 'ہ', ' '),
            Trigram(' ', 'م', 'ن'),
            Trigram(' ', 'ب', 'ن'),
            Trigram(' ', 'ق', 'و'),
            Trigram('ے', ' ', 'ج'),
            Trigram('ی', 'ہ', ' '),
            Trigram('ں', ' ', 'م'),
            Trigram('ا', 'ش', 'ر'),
            Trigram('م', 'ل', ' '),
            Trigram(' ', 'د', 'و'),
            Trigram('ع', 'ا', 'ش'),
            Trigram('ق', 'و', 'م'),
            Trigram('ر', ' ', 'ب'),
            Trigram('ا', 'ن', 'ی'),
            Trigram('و', 'ا', 'م'),
            Trigram('ق', 'و', 'ا'),
            Trigram('ا', 'ق', 'و'),
            Trigram('ل', 'ی', 'ٔ'),
            Trigram('د', 'ا', 'ر'),
            Trigram(' ', 'و', 'ہ'),
            Trigram(' ', 'و', ' '),
            Trigram(' ', 'ع', 'ا'),
            Trigram('ی', ' ', 'س'),
            Trigram('ب', 'ر', ' '),
            Trigram('ع', 'ل', 'ا'),
            Trigram('ا', 'د', ' '),
            Trigram('ہ', ' ', 'م'),
            Trigram('و', ' ', 'ت'),
            Trigram('ر', ' ', 'ن'),
            Trigram(' ', 'ج', 'س'),
            Trigram('ے', '۔', 'ہ'),
            Trigram('ے', '،', ' '),
            Trigram('ا', 'ن', 'و'),
            Trigram(' ', 'د', 'ی'),
            Trigram('گ', 'ی', ' '),
            Trigram('ل', 'ی', 'م'),
            Trigram('ی', 'و', 'ں'),
            Trigram(' ', 'ق', 'ا'),
            Trigram(' ', 'ی', 'ہ'),
            Trigram('د', 'و', 'س'),
            Trigram('ے', '۔', ' '),
            Trigram('ا', ' ', 'ہ'),
            Trigram('ت', 'ع', 'ل'),
            Trigram('ی', 'م', ' '),
            Trigram('ر', ' ', 'پ'),
            Trigram('ج', 'س', ' '),
            Trigram('ر', 'ی', 'ق'),
            Trigram('ے', ' ', 'ح'),
            Trigram(' ', 'ا', 'ق'),
            Trigram('ن', 'ی', 'ا'),
            Trigram('ل', 'ک', ' '),
            Trigram(' ', 'گ', 'ی'),
            Trigram('ی', 'ن', ' '),
            Trigram('ی', 'ا', 'د'),
            Trigram(' ', 'م', 'س'),
            Trigram('ل', 'ا', 'ق'),
            Trigram('،', ' ', 'ا'),
            Trigram('ی', ' ', 'ن'),
            Trigram('پ', 'ن', 'ے'),
            Trigram('و', 'ر', 'ی'),
            Trigram('م', ' ', 'ا'),
            Trigram(' ', 'ب', 'ا'),
            Trigram('ع', 'ل', 'ی'),
            Trigram('ی', 'ر', ' '),
            Trigram('ی', '،', ' '),
            Trigram('ا', 'ن', 'ے'),
            Trigram('و', 'ن', ' '),
            Trigram('ن', ' ', 'ا'),
            Trigram('ر', ' ', 'ع'),
            Trigram(' ', 'ب', 'ر'),
            Trigram('ی', ' ', 'آ'),
            Trigram('ر', ' ', 'ح'),
            Trigram(' ', 'ر', 'ک'),
            Trigram('ے', ' ', 'پ'),
            Trigram('ک', 'ر', ' '),
            Trigram('گ', 'ا', '۔'),
            Trigram(' ', 'پ', 'ی'),
            Trigram('س', 'ب', ' '),
            Trigram(' ', 'گ', 'ا'),
            Trigram('ن', 'ا', ' '),
            Trigram(' ', 'پ', 'و'),
            Trigram('ی', 'س', 'ے'),
            Trigram('ر', 'ا', 'ی'),
            Trigram(' ', 'م', 'ر'),
            Trigram('ا', 'ر', 'ی'),
            Trigram('ق', 'ا', 'ن'),
            Trigram('ن', 'و', 'ن'),
            Trigram(' ', 'م', 'م'),
            Trigram('ن', 'د', 'گ'),
            Trigram(' ', 'ا', 'ع'),
            Trigram('د', 'گ', 'ی'),
            Trigram('ہ', ' ', 'و'),
            Trigram(' ', 'ہ', 'ر'),
            Trigram('ر', ' ', 'س'),
            Trigram(' ', 'چ', 'ا'),
            Trigram('خ', 'ل', 'ا'),
            Trigram('ا', ' ', 'پ'),
            Trigram('ق', ' ', 'ح'),
            Trigram(' ', 'ب', 'ھ'),
            Trigram('س', ' ', 'م'),
            Trigram(' ', 'ش', 'ا'),
            Trigram('ہ', 'و', 'گ'),
            Trigram('ے', ' ', 'خ'),
            Trigram('و', 'س', 'ر'),
            Trigram('ر', 'ت', 'ی'),
            Trigram('و', 'م', 'ی'),
            Trigram(' ', 'ب', 'ی'),
            Trigram('ر', 'ک', 'ھ'),
            Trigram(' ', 'م', 'ت'),
            Trigram('ک', 'و', 'ی'),
            Trigram('ر', ' ', 'آ'),
            Trigram('پ', 'و', 'ر'),
            Trigram('ا', 'ف', ' '),
            Trigram(' ', 'م', 'ح'),
            Trigram('ے', ' ', 'س'),
            Trigram('ہ', 'و', 'ں'),
            Trigram('ن', 'ک', 'ہ'),
            Trigram('و', 'ن', 'ک'),
            Trigram('ت', ' ', 'ا'),
            Trigram(' ', 'ط', 'ر'),
            Trigram('ے', ' ', 'ع'),
            Trigram('ی', 'ٔ', 'د'),
            Trigram('د', ' ', 'ا'),
            Trigram('ا', 'ل', ' '),
            Trigram('ں', '۔', ' '),
            Trigram('م', ' ', 'م'),
            Trigram('ا', 'ں', ' '),
            Trigram(' ', 'م', 'ق'),
            Trigram('غ', 'ی', 'ر'),
            Trigram('پ', 'ن', 'ی'),
            Trigram(' ', 'ا', 'م'),
            Trigram('ں', '،', ' '),
            Trigram('م', 'ن', ' '),
            Trigram('ہ', 'و', ' '),
            Trigram('ر', 'ی', 'ع'),
            Trigram('و', ' ', 'ک'),
            Trigram('ذ', 'ر', 'ی'),
            Trigram(' ', 'ذ', 'ر'),
            Trigram('ع', 'ا', 'م'),
            Trigram('،', ' ', 'م'),
            Trigram('د', 'ا', 'ن'),
            Trigram('ا', 'د', 'ا'),
            Trigram('ا', 'ع', 'ل'),
            Trigram('م', 'ا', 'م'),
            Trigram('ت', 'م', 'ا'),
            Trigram(' ', 'ع', 'ل'),
            Trigram('د', 'ی', 'و'),
            Trigram('ب', 'ھ', 'ی'),
            Trigram('ھ', 'ی', ' '),
            Trigram('ب', 'ن', 'ی'),
            Trigram('ے', ' ', 'ی'),
            Trigram('ا', ' ', 'ک'),
            Trigram('ا', 'و', 'ی'),
            Trigram('ل', ' ', 'م'),
            Trigram(' ', 'ز', 'ن'),
            Trigram('ی', 'ا', 'س'),
            Trigram('ل', 'ا', 'ن'),
            Trigram('ع', 'م', 'ل'),
            Trigram(' ', 'ع', 'م'),
            Trigram('ت', ' ', 'م'),
            Trigram(' ', 'ب', 'چ'),
        ],
    ),
    (
        Lang::Pes,
        &[
            Trigram(' ', 'و', ' '),
            Trigram(' ', 'ح', 'ق'),
            Trigram(' ', 'ب', 'ا'),
            Trigram('ک', 'ه', ' '),
            Trigram('ن', 'د', ' '),
            Trigram(' ', 'ک', 'ه'),
            Trigram(' ', 'د', 'ر'),
            Trigram('د', 'ر', ' '),
            Trigram('ر', 'د', ' '),
            Trigram(' ', 'د', 'ا'),
            Trigram('د', 'ا', 'ر'),
            Trigram('ا', 'ز', ' '),
            Trigram(' ', 'ا', 'ز'),
            Trigram('ه', 'ر', ' '),
            Trigram(' ', 'ه', 'ر'),
            Trigram('ی', 'ت', ' '),
            Trigram('ر', ' ', 'ک'),
            Trigram('ح', 'ق', ' '),
            Trigram('د', ' ', 'ه'),
            Trigram('ا', 'ی', ' '),
            Trigram('د', ' ', 'و'),
            Trigram('ا', 'ن', ' '),
            Trigram(' ', 'ر', 'ا'),
            Trigram('ی', 'ن', ' '),
            Trigram('و', 'د', ' '),
            Trigram('ی', 'ا', ' '),
            Trigram(' ', 'ی', 'ا'),
            Trigram('ر', 'ا', ' '),
            Trigram('ا', 'ر', 'د'),
            Trigram('ی', ' ', 'و'),
            Trigram('ک', 'س', ' '),
            Trigram(' ', 'ک', 'س'),
            Trigram(' ', 'ب', 'ر'),
            Trigram(' ', 'آ', 'ز'),
            Trigram('ب', 'ا', 'ش'),
            Trigram('ه', ' ', 'ب'),
            Trigram('آ', 'ز', 'ا'),
            Trigram('د', ' ', 'ک'),
            Trigram(' ', 'خ', 'و'),
            Trigram('ه', ' ', 'ا'),
            Trigram('د', ' ', 'ب'),
            Trigram('ز', 'ا', 'د'),
            Trigram(' ', 'ا', 'س'),
            Trigram('ا', 'ر', ' '),
            Trigram(' ', 'آ', 'ن'),
            Trigram('ق', ' ', 'د'),
            Trigram('ش', 'د', ' '),
            Trigram('ح', 'ق', 'و'),
            Trigram('ق', 'و', 'ق'),
            Trigram('ی', ' ', 'ب'),
            Trigram('و', 'ق', ' '),
            Trigram('د', 'ه', ' '),
            Trigram('ه', ' ', 'د'),
            Trigram('ی', 'د', ' '),
            Trigram('ی', ' ', 'ک'),
            Trigram('و', ' ', 'ا'),
            Trigram('و', 'ر', ' '),
            Trigram('ر', ' ', 'م'),
            Trigram('ر', 'ا', 'ی'),
            Trigram('ا', 'ش', 'د'),
            Trigram('خ', 'و', 'د'),
            Trigram('ا', 'د', 'ی'),
            Trigram('ت', 'م', 'ا'),
            Trigram('ر', 'ی', ' '),
            Trigram(' ', 'ا', 'ج'),
            Trigram('ا', 'م', ' '),
            Trigram('د', 'ی', ' '),
            Trigram('ا', 'ی', 'د'),
            Trigram('س', ' ', 'ح'),
            Trigram('ا', 'س', 'ت'),
            Trigram('ر', ' ', 'ا'),
            Trigram('و', ' ', 'م'),
            Trigram(' ', 'ا', 'ن'),
            Trigram('د', ' ', 'ا'),
            Trigram('ن', 'ه', ' '),
            Trigram(' ', 'ب', 'ی'),
            Trigram('ب', 'ا', ' '),
            Trigram(' ', 'ه', 'م'),
            Trigram(' ', 'ن', 'م'),
            Trigram('م', 'ا', 'ی'),
            Trigram(' ', 'ت', 'ا'),
            Trigram('د', '،', ' '),
            Trigram('ی', ' ', 'ا'),
            Trigram('ا', 'ن', 'ه'),
            Trigram('ا', 'ت', ' '),
            Trigram('و', 'ن', ' '),
            Trigram('ا', 'ی', 'ت'),
            Trigram('ا', ' ', 'ب'),
            Trigram('س', 'ت', ' '),
            Trigram(' ', 'ک', 'ن'),
            Trigram('ب', 'ر', 'ا'),
            Trigram('ا', 'ن', 'و'),
            Trigram(' ', 'ب', 'ش'),
            Trigram(' ', 'م', 'و'),
            Trigram('ا', 'ی', 'ن'),
            Trigram(' ', 'م', 'ر'),
            Trigram('ا', 'س', 'ا'),
            Trigram(' ', 'م', 'ل'),
            Trigram('و', 'ا', 'ن'),
            Trigram('ر', ' ', 'ب'),
            Trigram('ج', 'ت', 'م'),
            Trigram(' ', 'ش', 'و'),
            Trigram(' ', 'ا', 'ع'),
            Trigram('ن', ' ', 'ا'),
            Trigram('و', 'ر', 'د'),
            Trigram(' ', 'م', 'ی'),
            Trigram(' ', 'ا', 'ی'),
            Trigram('آ', 'ن', ' '),
            Trigram(' ', 'ب', 'ه'),
            Trigram('و', ' ', 'آ'),
            Trigram('م', 'ل', 'ل'),
            Trigram('ا', ' ', 'م'),
            Trigram('م', 'ا', 'ع'),
            Trigram('ن', 'ی', ' '),
            Trigram('ت', ' ', 'ا'),
            Trigram('،', ' ', 'ا'),
            Trigram('ت', ' ', 'و'),
            Trigram('ئ', 'ی', ' '),
            Trigram('ع', 'ی', ' '),
            Trigram('ا', 'ئ', 'ی'),
            Trigram('ا', 'ج', 'ت'),
            Trigram('و', ' ', 'ب'),
            Trigram('ه', 'ا', 'ی'),
            Trigram('ن', ' ', 'م'),
            Trigram('ی', ' ', 'ی'),
            Trigram('ب', 'ش', 'ر'),
            Trigram('ک', 'ن', 'د'),
            Trigram('ش', 'و', 'د'),
            Trigram(' ', 'م', 'ن'),
            Trigram(' ', 'ز', 'ن'),
            Trigram('ن', ' ', 'و'),
            Trigram('ی', '،', ' '),
            Trigram('ب', 'ا', 'ی'),
            Trigram('ی', ' ', 'ر'),
            Trigram(' ', 'م', 'س'),
            Trigram('م', 'ل', ' '),
            Trigram('م', 'و', 'ر'),
            Trigram('ز', ' ', 'آ'),
            Trigram('ت', 'و', 'ا'),
            Trigram('د', 'ا', 'ن'),
            Trigram('ا', 'ر', 'ی'),
            Trigram('ع', 'ل', 'ا'),
            Trigram('گ', 'ر', 'د'),
            Trigram('ی', 'گ', 'ر'),
            Trigram('ک', 'ا', 'ر'),
            Trigram(' ', 'گ', 'ر'),
            Trigram(' ', 'ب', 'د'),
            Trigram('ن', ' ', 'ب'),
            Trigram('ت', ' ', 'ب'),
            Trigram('ت', ' ', 'م'),
            Trigram('ی', ' ', 'م'),
            Trigram(' ', 'م', 'ق'),
            Trigram('د', ' ', 'آ'),
            Trigram('ش', 'و', 'ر'),
            Trigram('ی', 'ه', ' '),
            Trigram('ا', 'ع', 'ی'),
            Trigram(' ', 'ع', 'م'),
            Trigram('ر', ' ', 'خ'),
            Trigram('ن', ' ', 'ح'),
            Trigram(' ', 'ک', 'ش'),
            Trigram('ر', 'ن', 'د'),
            Trigram('م', 'ی', 'ن'),
            Trigram(' ', 'ا', 'ح'),
            Trigram('ن', ' ', 'ت'),
            Trigram('ی', ' ', 'د'),
            Trigram(' ', 'م', 'ت'),
            Trigram('ه', ' ', 'م'),
            Trigram('د', ' ', 'ش'),
            Trigram(' ', 'ح', 'م'),
            Trigram('و', ' ', 'د'),
            Trigram('د', 'ی', 'گ'),
            Trigram('ل', 'ا', 'م'),
            Trigram('ک', 'ش', 'و'),
            Trigram('ه', 'ٔ', ' '),
            Trigram('ه', ' ', 'و'),
            Trigram('ا', 'ن', 'ی'),
            Trigram('ل', 'ی', ' '),
            Trigram('ت', ' ', 'ک'),
            Trigram(' ', 'م', 'ج'),
            Trigram('ق', ' ', 'م'),
            Trigram('م', 'ی', 'ت'),
            Trigram(' ', 'ک', 'ا'),
            Trigram(' ', 'ش', 'د'),
            Trigram('ا', 'ه', ' '),
            Trigram('ن', 'و', 'ن'),
            Trigram(' ', 'آ', 'م'),
            Trigram('ا', 'د', ' '),
            Trigram('ا', 'د', 'ا'),
            Trigram('ا', 'ع', 'ل'),
            Trigram('د', ' ', 'م'),
            Trigram('ق', ' ', 'و'),
            Trigram('ا', ' ', 'ک'),
            Trigram('م', 'ی', ' '),
            Trigram('ی', ' ', 'ح'),
            Trigram('ل', 'ل', ' '),
            Trigram('ن', 'ج', 'ا'),
            Trigram(' ', 'م', 'ح'),
            Trigram('س', 'ا', 'س'),
            Trigram('ی', 'د', 'ه'),
            Trigram(' ', 'ق', 'ا'),
            Trigram('ب', 'ع', 'ی'),
            Trigram('ق', 'ا', 'ن'),
            Trigram('ر', ' ', 'ش'),
            Trigram('م', 'ق', 'ا'),
            Trigram('ا', ' ', 'د'),
            Trigram('ه', 'د', ' '),
            Trigram('و', 'ی', ' '),
            Trigram('ن', 'و', 'ا'),
            Trigram('گ', 'ی', ' '),
            Trigram('س', 'ا', 'و'),
            Trigram('ر', ' ', 'ت'),
            Trigram('ب', 'ر', ' '),
            Trigram('ا', 'ً', ' '),
            Trigram('ن', 'م', 'ی'),
            Trigram('ا', 'س', 'ی'),
            Trigram('ا', 'د', 'ه'),
            Trigram('ا', 'و', ' '),
            Trigram(' ', 'ا', 'و'),
            Trigram(' ', 'د', 'ی'),
            Trigram(' ', 'ه', 'ی'),
            Trigram('ه', 'ی', 'چ'),
            Trigram('ه', '‌', 'ا'),
            Trigram('‌', 'ه', 'ا'),
            Trigram('ی', 'ر', ' '),
            Trigram('خ', 'و', 'ا'),
            Trigram('د', ' ', 'ت'),
            Trigram('ه', 'م', 'ه'),
            Trigram('ا', ' ', 'ه'),
            Trigram('ت', 'ی', ' '),
            Trigram('ح', 'م', 'ا'),
            Trigram('د', 'گ', 'ی'),
            Trigram('ب', 'ی', 'ن'),
            Trigram('ع', ' ', 'ا'),
            Trigram('س', 'ا', 'ن'),
            Trigram('ر', ' ', 'و'),
            Trigram('ش', 'د', 'ه'),
            Trigram('و', 'م', 'ی'),
            Trigram(' ', 'ع', 'ق'),
            Trigram(' ', 'ب', 'ع'),
            Trigram('ز', ' ', 'ح'),
            Trigram('ش', 'ر', ' '),
            Trigram('م', 'ن', 'د'),
            Trigram(' ', 'ش', 'ر'),
            Trigram('ٔ', 'م', 'ی'),
            Trigram('ا', 'ٔ', 'م'),
            Trigram('ت', 'ا', 'ٔ'),
            Trigram('ا', 'ن', 'ت'),
            Trigram('ا', 'ن', 'د'),
            Trigram('ا', 'و', 'ی'),
            Trigram('م', 'س', 'ا'),
            Trigram('ر', 'د', 'د'),
            Trigram('ب', 'ه', 'ر'),
            Trigram(' ', 'ب', 'م'),
            Trigram('ا', 'ر', 'ن'),
            Trigram('ی', 'ت', 'و'),
            Trigram('ل', ' ', 'م'),
            Trigram('ر', 'ا', 'ن'),
            Trigram('و', ' ', 'ه'),
            Trigram('ر', ' ', 'د'),
            Trigram('م', ' ', 'م'),
            Trigram('ر', 'ا', 'ر'),
            Trigram('ع', 'ق', 'ی'),
            Trigram('س', 'ی', ' '),
            Trigram('و', ' ', 'ت'),
            Trigram('ز', 'ش', ' '),
            Trigram(' ', 'ب', 'و'),
            Trigram('ا', ' ', 'ا'),
            Trigram('ی', ' ', 'ن'),
            Trigram('م', 'و', 'م'),
            Trigram('ج', 'ا', ' '),
            Trigram('ع', 'م', 'و'),
            Trigram('ر', 'ف', 'ت'),
            Trigram('ع', 'ی', 'ت'),
            Trigram(' ', 'ف', 'ر'),
            Trigram('ن', 'د', 'گ'),
            Trigram('و', 'ا', 'ه'),
            Trigram('ز', 'ن', 'د'),
            Trigram('م', ' ', 'و'),
            Trigram('ن', 'م', 'ا'),
            Trigram('ه', ' ', 'ح'),
            Trigram('ا', ' ', 'ر'),
            Trigram('د', 'ی', 'ه'),
            Trigram('ج', 'ا', 'م'),
            Trigram('م', 'ر', 'د'),
            Trigram('ت', '،', ' '),
            Trigram('د', ' ', 'ر'),
            Trigram('م', 'ا', 'م'),
            Trigram(' ', 'ت', 'م'),
            Trigram('م', 'ل', 'ی'),
            Trigram('ن', 'ن', 'د'),
            Trigram('ا', 'ل', 'م'),
            Trigram('ط', 'و', 'ر'),
            Trigram('ی', ' ', 'ت'),
            Trigram('ت', 'خ', 'ا'),
            Trigram('ا', ' ', 'ت'),
            Trigram('ا', 'م', 'ی'),
            Trigram('ا', 'م', 'ل'),
            Trigram('د', 'د', ' '),
            Trigram(' ', 'ش', 'خ'),
            Trigram('ش', 'خ', 'ص'),
        ],
    ),
];

/// Languages for script Devanagari
pub static DEVANAGARI_LANGS: LangProfileList = &[
    (
        Lang::Hin,
        &[
            Trigram('क', 'े', ' '),
            Trigram('प', '्', 'र'),
            Trigram('औ', 'र', ' '),
            Trigram(' ', 'औ', 'र'),
            Trigram(' ', 'क', 'े'),
            Trigram('ो', 'ं', ' '),
            Trigram(' ', 'क', 'ा'),
            Trigram('क', 'ा', 'र'),
            Trigram(' ', 'प', '्'),
            Trigram('क', 'ा', ' '),
            Trigram(' ', 'क', 'ो'),
            Trigram('य', 'ा', ' '),
            Trigram('ं', ' ', 'क'),
            Trigram('त', 'ि', ' '),
            Trigram('ा', 'र', ' '),
            Trigram('क', 'ो', ' '),
            Trigram(' ', 'ह', 'ै'),
            Trigram('ि', 'क', 'ा'),
            Trigram('न', 'े', ' '),
            Trigram('ह', 'ै', ' '),
            Trigram('्', 'र', 'त'),
            Trigram('ध', 'ि', 'क'),
            Trigram(' ', 'अ', 'ध'),
            Trigram('अ', 'ध', 'ि'),
            Trigram('क', 'ी', ' '),
            Trigram('ा', ' ', 'क'),
            Trigram(' ', 'क', 'ि'),
            Trigram(' ', 'क', 'ी'),
            Trigram(' ', 'स', 'म'),
            Trigram('े', 'ं', ' '),
            Trigram('व', '्', 'य'),
            Trigram('्', 'त', 'ि'),
            Trigram('क', '्', 'त'),
            Trigram('स', 'े', ' '),
            Trigram(' ', 'व', '्'),
            Trigram('ा', ' ', 'अ'),
            Trigram('्', 'य', 'क'),
            Trigram('म', 'े', 'ं'),
            Trigram('म', 'ा', 'न'),
            Trigram('ि', ' ', 'क'),
            Trigram(' ', 'स', '्'),
            Trigram(' ', 'म', 'े'),
            Trigram('स', 'ी', ' '),
            Trigram('न', '्', 'त'),
            Trigram(' ', 'ह', 'ो'),
            Trigram('े', ' ', 'क'),
            Trigram('त', 'ा', ' '),
            Trigram('य', 'क', '्'),
            Trigram('क', '्', 'ष'),
            Trigram('ै', ' ', '।'),
            Trigram('ि', 'क', ' '),
            Trigram('त', '्', 'य'),
            Trigram(' ', 'क', 'र'),
            Trigram('्', 'य', ' '),
            Trigram(' ', 'य', 'ा'),
            Trigram('भ', 'ी', ' '),
            Trigram(' ', 'व', 'ि'),
            Trigram('र', 'त', '्'),
            Trigram('र', ' ', 'स'),
            Trigram('ी', ' ', 'स'),
            Trigram(' ', 'ज', 'ा'),
            Trigram('स', '्', 'व'),
            Trigram('र', 'ो', 'ं'),
            Trigram('्', 'य', 'े'),
            Trigram('े', 'क', ' '),
            Trigram('य', 'े', 'क'),
            Trigram('त', '्', 'र'),
            Trigram('ि', 'य', 'ा'),
            Trigram('ा', ' ', 'ज'),
            Trigram('क', ' ', 'व'),
            Trigram('र', ' ', 'ह'),
            Trigram('ि', 'त', ' '),
            Trigram('्', 'र', 'ा'),
            Trigram('क', 'ि', 'स'),
            Trigram(' ', 'अ', 'न'),
            Trigram('ा', ' ', 'स'),
            Trigram('ि', 'स', 'ी'),
            Trigram('ा', ' ', 'ह'),
            Trigram('न', 'ा', ' '),
            Trigram(' ', 'स', 'े'),
            Trigram(' ', 'प', 'र'),
            Trigram('र', ' ', 'क'),
            Trigram(' ', 'स', 'ा'),
            Trigram('द', 'े', 'श'),
            Trigram('ग', 'ा', ' '),
            Trigram(' ', '।', ' '),
            Trigram(' ', 'अ', 'प'),
            Trigram('्', 'त', '्'),
            Trigram('े', ' ', 'स'),
            Trigram('स', 'म', 'ा'),
            Trigram('ा', 'न', ' '),
            Trigram('ी', ' ', 'क'),
            Trigram('्', 'त', ' '),
            Trigram('व', 'ा', 'र'),
            Trigram(' ', '।', 'प'),
            Trigram('ा', ' ', 'प'),
            Trigram(' ', 'र', 'ा'),
            Trigram('ष', 'ा', ' '),
            Trigram('न', ' ', 'क'),
            Trigram('।', 'प', '्'),
            Trigram('ष', '्', 'ट'),
            Trigram('थ', 'ा', ' '),
            Trigram('अ', 'न', '्'),
            Trigram(' ', 'म', 'ा'),
            Trigram('्', 'ष', 'ा'),
            Trigram('्', 'व', 'ा'),
            Trigram('ा', 'र', 'ो'),
            Trigram('त', 'न', '्'),
            Trigram('व', 'त', 'न'),
            Trigram('ट', '्', 'र'),
            Trigram('्', 'व', 'त'),
            Trigram('प', '्', 'त'),
            Trigram('ा', 'प', '्'),
            Trigram('्', 'ट', '्'),
            Trigram('र', 'ा', 'ष'),
            Trigram('ा', 'ष', '्'),
            Trigram(' ', 'इ', 'स'),
            Trigram('े', ' ', 'अ'),
            Trigram(' ', 'उ', 'स'),
            Trigram(' ', 'स', 'ं'),
            Trigram('र', 'ा', 'प'),
            Trigram('क', 'ि', ' '),
            Trigram('त', ' ', 'ह'),
            Trigram('ह', 'ो', ' '),
            Trigram('ं', ' ', 'औ'),
            Trigram('ा', 'र', '्'),
            Trigram('ा', ' ', '।'),
            Trigram('क', 'ि', 'य'),
            Trigram('े', ' ', 'प'),
            Trigram(' ', 'द', 'े'),
            Trigram(' ', 'भ', 'ी'),
            Trigram('क', 'र', 'न'),
            Trigram('र', 'ी', ' '),
            Trigram('ज', 'ा', 'ए'),
            Trigram('ी', ' ', 'प'),
            Trigram(' ', 'न', ' '),
            Trigram('र', ' ', 'अ'),
            Trigram('क', ' ', 'स'),
            Trigram('अ', 'प', 'न'),
            Trigram('े', ' ', 'व'),
            Trigram('ा', 'ओ', 'ं'),
            Trigram('्', 'त', 'र'),
            Trigram('ओ', 'ं', ' '),
            Trigram(' ', 'न', 'ि'),
            Trigram('स', 'भ', 'ी'),
            Trigram('र', 'ा', ' '),
            Trigram(' ', 'त', 'थ'),
            Trigram('त', 'थ', 'ा'),
            Trigram('ि', 'व', 'ा'),
            Trigram('य', 'ो', 'ं'),
            Trigram('प', 'र', ' '),
            Trigram(' ', 'ऐ', 'स'),
            Trigram('र', 'त', 'ा'),
            Trigram('ा', 'र', 'ा'),
            Trigram('्', 'र', 'ी'),
            Trigram('स', 'म', '्'),
            Trigram(' ', 'द', '्'),
            Trigram('ी', 'य', ' '),
            Trigram('ि', 'ए', ' '),
            Trigram('व', ' ', 'क'),
            Trigram('स', 'क', 'े'),
            Trigram('द', '्', 'व'),
            Trigram('ह', 'ो', 'ग'),
            Trigram(' ', 'स', 'भ'),
            Trigram('ं', ' ', 'म'),
            Trigram('म', 'ा', 'ज'),
            Trigram('र', 'न', 'े'),
            Trigram('ि', 'क', '्'),
            Trigram('्', 'य', 'ा'),
            Trigram('ा', ' ', 'व'),
            Trigram('र', ' ', 'प'),
            Trigram(' ', 'ज', 'ि'),
            Trigram('ो', ' ', 'स'),
            Trigram('र', ' ', 'उ'),
            Trigram('र', 'क', '्'),
            Trigram('े', ' ', 'म'),
            Trigram('प', 'ू', 'र'),
            Trigram(' ', 'ल', 'ि'),
            Trigram('ा', 'ए', 'ग'),
            Trigram(' ', 'भ', 'ा'),
            Trigram('इ', 'स', ' '),
            Trigram('त', ' ', 'क'),
            Trigram('ा', 'व', ' '),
            Trigram('स', '्', 'थ'),
            Trigram('प', 'न', 'े'),
            Trigram('ा', ' ', 'औ'),
            Trigram('द', '्', 'ध'),
            Trigram('श', '्', 'य'),
            Trigram('र', '्', 'व'),
            Trigram(' ', 'घ', 'ो'),
            Trigram('घ', 'ो', 'ष'),
            Trigram('र', 'ू', 'प'),
            Trigram('भ', 'ा', 'व'),
            Trigram('ा', 'न', 'े'),
            Trigram('क', 'ृ', 'त'),
            Trigram('ो', ' ', 'प'),
            Trigram('े', ' ', 'ल'),
            Trigram('ल', 'ि', 'ए'),
            Trigram('श', 'ि', 'क'),
            Trigram('ू', 'र', '्'),
            Trigram(' ', 'उ', 'न'),
            Trigram('।', ' ', 'इ'),
            Trigram('ं', ' ', 'स'),
            Trigram('य', ' ', 'क'),
            Trigram('्', 'ध', ' '),
            Trigram('द', 'ी', ' '),
            Trigram('ी', ' ', 'र'),
            Trigram('र', '्', 'य'),
            Trigram('ण', 'ा', ' '),
            Trigram('ए', 'ग', 'ा'),
            Trigram('न', '्', 'य'),
            Trigram('र', 'ी', 'य'),
            Trigram('े', 'श', ' '),
            Trigram('र', 'त', 'ि'),
            Trigram('े', ' ', 'ब'),
            Trigram(' ', 'र', 'ू'),
            Trigram('ू', 'प', ' '),
            Trigram('प', 'र', 'ा'),
            Trigram('्', 'र', ' '),
            Trigram('त', 'र', '्'),
            Trigram(' ', 'प', 'ा'),
            Trigram(' ', 'स', 'ु'),
            Trigram('ज', 'ि', 'स'),
            Trigram('त', 'ि', 'क'),
            Trigram('स', 'ा', 'र'),
            Trigram('ज', 'ो', ' '),
            Trigram('े', 'श', 'ो'),
            Trigram(' ', 'श', 'ि'),
            Trigram('ा', 'न', 'व'),
            Trigram('ी', ' ', 'अ'),
            Trigram('च', 'ि', 'त'),
            Trigram('े', ' ', 'औ'),
            Trigram(' ', 'प', 'ू'),
            Trigram('ि', 'य', 'ो'),
            Trigram('ा', ' ', 'उ'),
            Trigram('म', ' ', 'क'),
            Trigram('ी', ' ', 'भ'),
            Trigram('श', 'ो', 'ं'),
            Trigram(' ', 'ब', 'ु'),
            Trigram('म', '्', 'म'),
            Trigram('स', '्', 'त'),
            Trigram('ि', 'श', '्'),
            Trigram('्', 'र', 'ो'),
            Trigram('्', 'म', ' '),
            Trigram('ो', ' ', 'क'),
            Trigram(' ', 'य', 'ह'),
            Trigram('र', ' ', 'द'),
            Trigram('न', 'व', ' '),
            Trigram('च', 'ा', 'र'),
            Trigram('द', 'ि', 'य'),
            Trigram('े', ' ', 'य'),
            Trigram('र', '्', 'ण'),
            Trigram('र', 'ा', 'ध'),
            Trigram('ो', 'ग', 'ा'),
            Trigram('ल', 'े', ' '),
            Trigram('न', 'ू', 'न'),
            Trigram('ा', 'न', 'ू'),
            Trigram('ो', 'ष', 'ण'),
            Trigram('ष', 'ण', 'ा'),
            Trigram('व', 'ि', 'श'),
            Trigram(' ', 'ज', 'न'),
            Trigram('ा', 'र', 'ी'),
            Trigram('प', 'र', 'ि'),
            Trigram('ग', 'ी', ' '),
            Trigram('व', 'ा', 'ह'),
            Trigram('स', 'ा', 'म'),
            Trigram('ा', 'न', 'ा'),
            Trigram('र', 'क', 'ा'),
            Trigram(' ', 'ज', 'ो'),
            Trigram('ा', 'ज', ' '),
            Trigram('ी', ' ', 'ज'),
            Trigram('ध', ' ', 'क'),
            Trigram('ब', 'न', '्'),
            Trigram('त', 'ा', 'ओ'),
            Trigram('ं', 'क', 'ि'),
            Trigram('ू', 'ं', 'क'),
            Trigram('ा', 'स', ' '),
            Trigram('क', 'र', ' '),
            Trigram('च', 'ू', 'ं'),
            Trigram('ी', ' ', 'व'),
            Trigram('य', ' ', 'ह'),
            Trigram('ा', ' ', 'ग'),
            Trigram('य', ' ', 'स'),
            Trigram('न', ' ', 'स'),
            Trigram('त', ' ', 'र'),
            Trigram('क', 'ो', 'ई'),
            Trigram('ु', 'क', '्'),
            Trigram('ो', 'ई', ' '),
            Trigram(' ', '।', 'क'),
            Trigram('ं', ' ', 'न'),
            Trigram('ह', 'ि', 'त'),
            Trigram('न', 'ि', 'य'),
            Trigram('य', 'ा', 'द'),
            Trigram('ा', 'द', 'ी'),
            Trigram('्', 'म', 'ा'),
            Trigram('्', 'थ', 'ा'),
            Trigram('ा', 'म', 'ा'),
            Trigram('ा', 'ह', ' '),
            Trigram('ी', ' ', 'म'),
            Trigram('े', ' ', 'ज'),
        ],
    ),
    (
        Lang::Mar,
        &[
            Trigram('्', 'य', 'ा'),
            Trigram('य', 'ा', ' '),
            Trigram('त', '्', 'य'),
            Trigram('य', 'ा', 'च'),
            Trigram('च', 'ा', ' '),
            Trigram(' ', 'व', ' '),
            Trigram('ण', '्', 'य'),
            Trigram('प', '्', 'र'),
            Trigram('क', 'ा', 'र'),
            Trigram('ा', 'च', 'ा'),
            Trigram(' ', 'प', '्'),
            Trigram('ध', 'ि', 'क'),
            Trigram('ि', 'क', 'ा'),
            Trigram(' ', 'अ', 'ध'),
            Trigram('अ', 'ध', 'ि'),
            Trigram('च', '्', 'य'),
            Trigram('ा', 'र', ' '),
            Trigram('आ', 'ह', 'े'),
            Trigram(' ', 'आ', 'ह'),
            Trigram('ा', ' ', 'अ'),
            Trigram('ह', 'े', ' '),
            Trigram(' ', 'स', '्'),
            Trigram('्', 'र', 'त'),
            Trigram('्', 'य', 'े'),
            Trigram('ा', ' ', 'क'),
            Trigram('स', '्', 'व'),
            Trigram(' ', 'क', 'र'),
            Trigram('्', 'व', 'ा'),
            Trigram('त', 'ा', ' '),
            Trigram('ा', 'स', ' '),
            Trigram('ा', ' ', 'स'),
            Trigram('ा', ' ', 'व'),
            Trigram('त', '्', 'र'),
            Trigram(' ', 'त', '्'),
            Trigram('व', 'ा', ' '),
            Trigram('ा', 'ं', 'च'),
            Trigram('य', 'ा', 'ं'),
            Trigram('ि', 'क', ' '),
            Trigram('म', 'ा', 'न'),
            Trigram(' ', 'य', 'ा'),
            Trigram('्', 'य', ' '),
            Trigram(' ', 'क', 'ा'),
            Trigram(' ', 'अ', 'स'),
            Trigram('र', 'त', '्'),
            Trigram('ष', '्', 'ट'),
            Trigram('र', '्', 'य'),
            Trigram('य', 'े', 'क'),
            Trigram('ल', '्', 'य'),
            Trigram('र', ' ', 'आ'),
            Trigram('ा', 'ह', 'ि'),
            Trigram('क', '्', 'ष'),
            Trigram(' ', 'क', 'ो'),
            Trigram('ा', 'म', 'ा'),
            Trigram('क', 'ो', 'ण'),
            Trigram(' ', 'स', 'ं'),
            Trigram('ा', 'च', '्'),
            Trigram('ा', 'त', ' '),
            Trigram('ा', ' ', 'न'),
            Trigram(' ', 'र', 'ा'),
            Trigram('ं', 'त', '्'),
            Trigram('ू', 'न', ' '),
            Trigram('े', 'क', 'ा'),
            Trigram(' ', 'स', 'ा'),
            Trigram('र', 'ा', 'ष'),
            Trigram('ा', 'ष', '्'),
            Trigram('च', 'े', ' '),
            Trigram('्', 'ट', '्'),
            Trigram('ट', '्', 'र'),
            Trigram('त', 'ं', 'त'),
            Trigram(' ', 'म', 'ा'),
            Trigram('न', 'े', ' '),
            Trigram('क', 'ि', 'ं'),
            Trigram(' ', 'क', 'ि'),
            Trigram('व', '्', 'य'),
            Trigram('व', 'ा', 'त'),
            Trigram('े', ' ', 'स'),
            Trigram('क', 'र', 'ण'),
            Trigram('ं', 'व', 'ा'),
            Trigram('ि', 'ं', 'व'),
            Trigram('य', 'े', ' '),
            Trigram('क', '्', 'त'),
            Trigram(' ', 'स', 'म'),
            Trigram('ा', ' ', 'प'),
            Trigram('न', 'ा', ' '),
            Trigram(' ', 'म', 'ि'),
            Trigram('क', 'ा', 'स'),
            Trigram('ा', 'त', 'ं'),
            Trigram('्', 'र', '्'),
            Trigram('र', '्', 'व'),
            Trigram('स', 'म', 'ा'),
            Trigram('म', 'ि', 'ळ'),
            Trigram(' ', 'ज', 'ा'),
            Trigram('े', ' ', 'प'),
            Trigram('व', ' ', 'स'),
            Trigram('य', 'ा', 'स'),
            Trigram('ो', 'ण', 'त'),
            Trigram('र', 'ण', '्'),
            Trigram('क', 'ा', 'म'),
            Trigram('ी', 'य', ' '),
            Trigram('ा', ' ', 'आ'),
            Trigram(' ', 'द', 'े'),
            Trigram('े', ' ', 'क'),
            Trigram('ा', 'ं', 'न'),
            Trigram('ह', 'ि', ' '),
            Trigram('र', 'ा', 'ं'),
            Trigram(' ', 'व', '्'),
            Trigram('्', 'य', 'क'),
            Trigram('ा', ' ', 'म'),
            Trigram('ि', 'ळ', 'ण'),
            Trigram('ह', 'ी', ' '),
            Trigram(' ', 'प', 'ा'),
            Trigram('्', 'ष', 'ण'),
            Trigram('ा', 'र', '्'),
            Trigram('ा', 'न', ' '),
            Trigram('े', ' ', 'अ'),
            Trigram(' ', 'आ', 'प'),
            Trigram(' ', 'व', 'ि'),
            Trigram('ळ', 'ण', '्'),
            Trigram('ा', 'ह', 'ी'),
            Trigram('च', 'ी', ' '),
            Trigram('े', ' ', 'व'),
            Trigram('्', 'र', 'ा'),
            Trigram('म', 'ा', ' '),
            Trigram('ल', 'ी', ' '),
            Trigram('ं', 'च', '्'),
            Trigram('ा', 'र', 'ा'),
            Trigram('ा', ' ', 'द'),
            Trigram(' ', 'आ', 'ण'),
            Trigram(' ', 'न', 'ि'),
            Trigram('ण', 'े', ' '),
            Trigram('द', '्', 'ध'),
            Trigram(' ', 'न', 'य'),
            Trigram('ल', 'ा', ' '),
            Trigram('ा', ' ', 'ह'),
            Trigram('न', 'य', 'े'),
            Trigram(' ', 'स', 'र'),
            Trigram('स', 'र', '्'),
            Trigram('्', 'र', 'ी'),
            Trigram('ब', 'ं', 'ध'),
            Trigram('ी', ' ', 'प'),
            Trigram('आ', 'प', 'ल'),
            Trigram('ल', 'े', ' '),
            Trigram('ी', 'ल', ' '),
            Trigram('म', 'ा', 'ज'),
            Trigram(' ', 'ह', 'ो'),
            Trigram('्', 'त', ' '),
            Trigram('त', ' ', 'क'),
            Trigram('ा', 'च', 'े'),
            Trigram('्', 'व', ' '),
            Trigram('ष', 'ण', ' '),
            Trigram('ं', 'न', 'ा'),
            Trigram('ल', 'े', 'ल'),
            Trigram('ी', ' ', 'अ'),
            Trigram('द', 'े', 'श'),
            Trigram('आ', 'ण', 'ि'),
            Trigram('ण', 'ि', ' '),
            Trigram('ध', '्', 'य'),
            Trigram(' ', 'श', 'ि'),
            Trigram('ी', ' ', 'स'),
            Trigram('े', ' ', 'ज'),
            Trigram('श', 'ि', 'क'),
            Trigram('र', 'ी', 'य'),
            Trigram('ा', 'न', 'व'),
            Trigram('प', 'ा', 'ह'),
            Trigram('ह', 'ि', 'ज'),
            Trigram('ि', 'ज', 'े'),
            Trigram('ज', 'े', ' '),
            Trigram('क', ' ', 'स'),
            Trigram('य', 'क', '्'),
            Trigram('न', ' ', 'क'),
            Trigram('व', ' ', 'त'),
            Trigram('ा', ' ', 'ज'),
            Trigram('य', 'ा', 'त'),
            Trigram('प', 'ल', '्'),
            Trigram('न', '्', 'य'),
            Trigram('व', 'ी', ' '),
            Trigram('स', '्', 'थ'),
            Trigram('ज', '्', 'य'),
            Trigram(' ', 'ज', '्'),
            Trigram('े', ' ', 'आ'),
            Trigram('र', 'क', '्'),
            Trigram('त', ' ', 'स'),
            Trigram('ि', 'क', '्'),
            Trigram('ं', 'ब', 'ं'),
            Trigram('स', 'ं', 'ब'),
            Trigram(' ', 'क', 'े'),
            Trigram('क', ' ', 'व'),
            Trigram('क', 'े', 'ल'),
            Trigram('अ', 'स', 'ल'),
            Trigram('य', ' ', 'अ'),
            Trigram('य', ' ', 'क'),
            Trigram('त', ' ', 'व'),
            Trigram('ी', 'त', ' '),
            Trigram('ण', 'त', '्'),
            Trigram('त', '्', 'व'),
            Trigram('ा', 'न', 'े'),
            Trigram(' ', 'उ', 'प'),
            Trigram('्', 'व', 'त'),
            Trigram('भ', 'ा', 'व'),
            Trigram('े', ' ', 'त'),
            Trigram('क', 'र', 'त'),
            Trigram('य', 'ा', 'ह'),
            Trigram('र', 'त', 'ा'),
            Trigram('ि', 'ष', '्'),
            Trigram('व', ' ', 'म'),
            Trigram('क', 'ा', 'ं'),
            Trigram('स', 'ा', 'म'),
            Trigram('र', 'त', 'ि'),
            Trigram('स', 'ा', 'र'),
            Trigram('ं', 'च', 'ा'),
            Trigram('र', ' ', 'व'),
            Trigram('क', ' ', 'आ'),
            Trigram('य', 'ा', 'य'),
            Trigram('ा', 'स', 'ा'),
            Trigram('स', 'ा', 'ठ'),
            Trigram('ा', 'ठ', 'ी'),
            Trigram('्', 'त', 'ी'),
            Trigram('ठ', 'ी', ' '),
            Trigram('े', 'ण', '्'),
            Trigram('र', '्', 'थ'),
            Trigram('ी', 'न', 'े'),
            Trigram('े', ' ', 'य'),
            Trigram('ज', 'ा', 'ह'),
            Trigram('ो', 'ण', 'ा'),
            Trigram('स', 'ं', 'र'),
            Trigram('ा', 'य', 'द'),
            Trigram('च', '्', 'छ'),
            Trigram('स', ' ', 'स'),
            Trigram('ं', 'र', 'क'),
            Trigram('त', 'ी', 'ल'),
            Trigram('ी', ' ', 'व'),
            Trigram('त', ' ', 'आ'),
            Trigram('ी', ' ', 'आ'),
            Trigram('ं', 'ध', 'ा'),
            Trigram('े', 'श', 'ा'),
            Trigram('ि', 'त', ' '),
            Trigram(' ', 'अ', 'श'),
            Trigram('ह', 'ी', 'र'),
            Trigram(' ', 'ह', 'क'),
            Trigram('ह', 'क', '्'),
            Trigram('क', '्', 'क'),
            Trigram('य', ' ', 'व'),
            Trigram('श', 'ा', ' '),
            Trigram('व', ' ', 'आ'),
            Trigram('त', 'ी', 'न'),
            Trigram('ण', ' ', 'म'),
            Trigram('ू', 'र', '्'),
            Trigram('े', 'ल', '्'),
            Trigram('द', '्', 'य'),
            Trigram('े', 'ल', 'े'),
            Trigram('ा', 'ं', 'त'),
            Trigram('ा', ' ', 'य'),
            Trigram('ा', ' ', 'ब'),
            Trigram('ी', ' ', 'म'),
            Trigram('ं', 'च', 'े'),
            Trigram('य', 'ा', 'व'),
            Trigram('द', 'े', 'ण'),
            Trigram('क', 'ृ', 'त'),
            Trigram('ा', 'र', 'ण'),
            Trigram('े', 'त', ' '),
            Trigram('ि', 'व', 'ा'),
            Trigram('व', 'स', '्'),
            Trigram('स', '्', 'त'),
            Trigram('ा', 'च', 'ी'),
            Trigram('न', 'व', 'ी'),
            Trigram(' ', 'अ', 'र'),
            Trigram('थ', 'व', 'ा'),
            Trigram('अ', 'थ', 'व'),
            Trigram('ा', ' ', 'त'),
            Trigram(' ', 'अ', 'थ'),
            Trigram('अ', 'र', '्'),
            Trigram('त', 'ी', ' '),
            Trigram('प', 'ू', 'र'),
            Trigram('इ', 'त', 'र'),
            Trigram('र', '्', 'ण'),
            Trigram('ी', ' ', 'क'),
            Trigram('य', 'त', '्'),
            Trigram(' ', 'इ', 'त'),
            Trigram(' ', 'श', 'ा'),
            Trigram('र', 'क', 'ा'),
            Trigram('त', 'ि', 'ष'),
            Trigram('ण', ' ', 'स'),
            Trigram('त', 'ि', 'क'),
            Trigram('्', 'र', 'क'),
            Trigram('्', 'ध', ' '),
            Trigram('र', 'ण', 'ा'),
            Trigram(' ', 'आ', 'ल'),
            Trigram('े', 'ल', ' '),
            Trigram('ा', 'ज', 'ि'),
            Trigram(' ', 'न', '्'),
            Trigram('ध', 'ा', 'त'),
            Trigram('र', 'ू', 'न'),
            Trigram('श', '्', 'र'),
            Trigram('अ', 'स', 'े'),
            Trigram('ष', '्', 'ठ'),
            Trigram('ु', 'क', '्'),
            Trigram('े', 'श', ' '),
            Trigram('त', 'ो', ' '),
            Trigram('ज', 'ि', 'क'),
            Trigram('े', ' ', 'म'),
        ],
    ),
    (
        Lang::Nep,
        &[
            Trigram('क', 'ो', ' '),
            Trigram(' ', 'र', ' '),
            Trigram('क', 'ा', 'र'),
            Trigram('प', '्', 'र'),
            Trigram('ा', 'र', ' '),
            Trigram('न', 'े', ' '),
            Trigram('ि', 'क', 'ा'),
            Trigram('क', '्', 'त'),
            Trigram('ध', 'ि', 'क'),
            Trigram('्', 'य', 'क'),
            Trigram(' ', 'ग', 'र'),
            Trigram('व', '्', 'य'),
            Trigram('्', 'र', 'त'),
            Trigram(' ', 'प', '्'),
            Trigram('अ', 'ध', 'ि'),
            Trigram('्', 'त', 'ि'),
            Trigram(' ', 'अ', 'ध'),
            Trigram(' ', 'व', '्'),
            Trigram('य', 'क', '्'),
            Trigram('म', 'ा', ' '),
            Trigram('ि', 'क', ' '),
            Trigram('त', '्', 'य'),
            Trigram('ा', 'ई', ' '),
            Trigram('ल', 'ा', 'ई'),
            Trigram('न', '्', 'त'),
            Trigram('म', 'ा', 'न'),
            Trigram(' ', 'स', 'म'),
            Trigram('त', '्', 'र'),
            Trigram('ग', 'र', '्'),
            Trigram('र', '्', 'न'),
            Trigram('क', ' ', 'व'),
            Trigram(' ', 'व', 'ा'),
            Trigram('्', 'न', 'े'),
            Trigram('व', 'ा', ' '),
            Trigram(' ', 'स', '्'),
            Trigram('र', 'त', '्'),
            Trigram('र', ' ', 'स'),
            Trigram('्', 'य', 'े'),
            Trigram('त', 'ि', 'ल'),
            Trigram('य', 'े', 'क'),
            Trigram('े', 'क', ' '),
            Trigram('छ', ' ', '।'),
            Trigram('ो', ' ', 'स'),
            Trigram('ा', ' ', 'स'),
            Trigram('ह', 'र', 'ू'),
            Trigram(' ', 'व', 'ि'),
            Trigram('क', '्', 'ष'),
            Trigram('्', 'त', '्'),
            Trigram('ि', 'ल', 'ा'),
            Trigram(' ', '।', ' '),
            Trigram('स', '्', 'व'),
            Trigram('ह', 'ु', 'न'),
            Trigram('त', 'ि', ' '),
            Trigram(' ', 'ह', 'ु'),
            Trigram('ल', 'े', ' '),
            Trigram(' ', 'र', 'ा'),
            Trigram(' ', 'म', 'ा'),
            Trigram('ष', '्', 'ट'),
            Trigram('स', 'म', 'ा'),
            Trigram('व', 'त', 'न'),
            Trigram('त', 'न', '्'),
            Trigram(' ', 'छ', ' '),
            Trigram('र', ' ', 'छ'),
            Trigram(' ', 'स', 'ं'),
            Trigram('्', 'ट', '्'),
            Trigram('ट', '्', 'र'),
            Trigram('ा', 'ष', '्'),
            Trigram('ो', ' ', 'अ'),
            Trigram('र', 'ा', 'ष'),
            Trigram('्', 'व', 'त'),
            Trigram('ु', 'न', 'े'),
            Trigram('न', 'े', 'छ'),
            Trigram('ह', 'र', 'ु'),
            Trigram('ा', 'न', ' '),
            Trigram('त', 'ा', ' '),
            Trigram('े', ' ', 'अ'),
            Trigram('्', 'र', ' '),
            Trigram(' ', 'क', 'ा'),
            Trigram('ि', 'न', 'े'),
            Trigram('ा', 'क', 'ो'),
            Trigram('ग', 'र', 'ि'),
            Trigram('े', ' ', 'छ'),
            Trigram('न', 'ा', ' '),
            Trigram(' ', 'अ', 'न'),
            Trigram(' ', 'न', 'ि'),
            Trigram('र', 'त', 'ा'),
            Trigram('न', 'ै', ' '),
            Trigram(' ', 'स', 'ा'),
            Trigram('ि', 'त', ' '),
            Trigram('त', 'ि', 'क'),
            Trigram('क', ' ', 'स'),
            Trigram('र', ' ', 'र'),
            Trigram('र', 'ू', ' '),
            Trigram('ा', ' ', 'अ'),
            Trigram('थ', 'ा', ' '),
            Trigram('स', '्', 'त'),
            Trigram('क', 'ु', 'न'),
            Trigram('ा', ' ', 'र'),
            Trigram('ु', 'न', 'ै'),
            Trigram(' ', 'छ', 'ै'),
            Trigram('्', 'त', ' '),
            Trigram('छ', 'ै', 'न'),
            Trigram('ा', ' ', 'प'),
            Trigram('ा', 'र', '्'),
            Trigram('व', 'ा', 'र'),
            Trigram('ा', ' ', 'व'),
            Trigram(' ', 'प', 'र'),
            Trigram('त', 'थ', 'ा'),
            Trigram(' ', 'त', 'थ'),
            Trigram('क', 'ा', ' '),
            Trigram('्', 'य', 'ा'),
            Trigram('ए', 'क', 'ो'),
            Trigram('र', 'ु', ' '),
            Trigram('्', 'ष', 'ा'),
            Trigram('म', 'ा', 'ज'),
            Trigram('र', 'क', '्'),
            Trigram('प', 'र', 'ि'),
            Trigram('द', '्', 'ध'),
            Trigram('।', ' ', 'प'),
            Trigram(' ', 'ल', 'ा'),
            Trigram('स', 'क', 'ो'),
            Trigram('ा', 'म', 'ा'),
            Trigram(' ', 'य', 'स'),
            Trigram('ा', 'ह', 'र'),
            Trigram('े', 'छ', ' '),
            Trigram('ध', 'ा', 'र'),
            Trigram('्', 'र', 'ा'),
            Trigram('ो', ' ', 'प'),
            Trigram('न', 'ि', ' '),
            Trigram('द', 'े', 'श'),
            Trigram('भ', 'ा', 'व'),
            Trigram('ि', 'व', 'ा'),
            Trigram('्', 'य', ' '),
            Trigram('र', ' ', 'ह'),
            Trigram('र', ' ', 'व'),
            Trigram('र', ' ', 'म'),
            Trigram('स', 'ब', 'ै'),
            Trigram('न', ' ', 'अ'),
            Trigram('े', ' ', 'र'),
            Trigram('न', ' ', 'स'),
            Trigram('र', 'क', 'ो'),
            Trigram('अ', 'न', '्'),
            Trigram('त', 'ा', 'क'),
            Trigram('ं', 'र', 'क'),
            Trigram('स', 'ं', 'र'),
            Trigram('्', 'व', 'ा'),
            Trigram(' ', 'त', '्'),
            Trigram('स', 'म', '्'),
            Trigram('र', 'ी', ' '),
            Trigram('ो', ' ', 'व'),
            Trigram('ा', ' ', 'भ'),
            Trigram('र', 'ह', 'र'),
            Trigram(' ', 'क', 'ु'),
            Trigram('्', 'र', 'ि'),
            Trigram('त', ' ', 'र'),
            Trigram('र', 'ि', 'न'),
            Trigram('श', '्', 'य'),
            Trigram('प', 'न', 'ि'),
            Trigram('ै', ' ', 'व'),
            Trigram('य', 'स', '्'),
            Trigram('ा', 'र', 'ा'),
            Trigram('ा', 'न', 'व'),
            Trigram(' ', 'श', 'ि'),
            Trigram('ा', ' ', 'त'),
            Trigram('ल', 'ा', 'ग'),
            Trigram('र', 'ा', ' '),
            Trigram('श', 'ि', 'क'),
            Trigram(' ', 'स', 'ब'),
            Trigram('ा', 'उ', 'न'),
            Trigram('ि', 'क', '्'),
            Trigram('्', 'न', ' '),
            Trigram('ा', 'र', 'क'),
            Trigram('ा', ' ', 'न'),
            Trigram('र', 'ि', 'य'),
            Trigram('्', 'य', 'स'),
            Trigram('द', '्', 'व'),
            Trigram('र', 'त', 'ि'),
            Trigram('च', 'ा', 'र'),
            Trigram(' ', 'स', 'ह'),
            Trigram('्', 'ष', 'ण'),
            Trigram(' ', 'स', 'ु'),
            Trigram('ा', 'र', 'म'),
            Trigram('ु', 'क', '्'),
            Trigram('ु', 'द', '्'),
            Trigram('स', 'ा', 'म'),
            Trigram('ष', 'ा', ' '),
            Trigram('ै', 'न', ' '),
            Trigram(' ', 'अ', 'प'),
            Trigram(' ', 'भ', 'ए'),
            Trigram('ब', 'ा', 'ट'),
            Trigram('ु', 'न', ' '),
            Trigram(' ', 'उ', 'प'),
            Trigram('ा', 'न', '्'),
            Trigram('ो', ' ', 'आ'),
            Trigram('्', 'त', 'र'),
            Trigram('ि', 'य', ' '),
            Trigram('क', 'ा', 'न'),
            Trigram('ि', ' ', 'र'),
            Trigram('र', 'ू', 'क'),
            Trigram('द', '्', 'द'),
            Trigram('र', ' ', 'प'),
            Trigram('ा', 'व', ' '),
            Trigram('ो', ' ', 'ल'),
            Trigram('त', 'ो', ' '),
            Trigram(' ', 'प', 'न'),
            Trigram('ै', 'न', '।'),
            Trigram(' ', 'आ', 'व'),
            Trigram('ा', ' ', 'ग'),
            Trigram('।', 'प', '्'),
            Trigram('ब', 'ै', ' '),
            Trigram('ू', 'र', '्'),
            Trigram('ि', 'ए', 'क'),
            Trigram('र', ' ', 'त'),
            Trigram('न', 'ि', 'ज'),
            Trigram('त', '्', 'प'),
            Trigram(' ', 'भ', 'े'),
            Trigram('ज', 'ि', 'क'),
            Trigram('े', 'छ', '।'),
            Trigram('ि', 'क', 'ो'),
            Trigram('्', 'त', 'ो'),
            Trigram('व', 'ा', 'ह'),
            Trigram('त', ' ', 'स'),
            Trigram('ा', 'ट', ' '),
            Trigram(' ', 'अ', 'र'),
            Trigram('ा', 'ज', 'ि'),
            Trigram('्', 'ध', ' '),
            Trigram(' ', 'उ', 'स'),
            Trigram('र', 'म', 'ा'),
            Trigram('ा', 'त', '्'),
            Trigram('र', '्', 'य'),
            Trigram('न', 'क', 'ो'),
            Trigram('ा', 'य', ' '),
            Trigram('ज', 'क', 'ो'),
            Trigram('ि', 'त', '्'),
            Trigram('ा', 'ग', 'ि'),
            Trigram(' ', 'अ', 'भ'),
            Trigram('न', ' ', 'ग'),
            Trigram('ग', 'ि', ' '),
            Trigram('ा', ' ', 'म'),
            Trigram(' ', 'आ', 'ध'),
            Trigram('स', '्', 'थ'),
            Trigram(' ', 'प', 'ा'),
            Trigram('ा', 'र', 'ह'),
            Trigram('घ', 'ो', 'ष'),
            Trigram('त', '्', 'व'),
            Trigram('य', 'त', 'ा'),
            Trigram('ा', ' ', 'क'),
            Trigram('र', '्', 'द'),
            Trigram(' ', 'म', 'त'),
            Trigram('व', 'ि', 'ध'),
            Trigram(' ', 'स', 'क'),
            Trigram('स', 'ा', 'र'),
            Trigram('प', 'र', 'ा'),
            Trigram('य', 'ु', 'क'),
            Trigram('र', 'ा', 'ध'),
            Trigram(' ', 'घ', 'ो'),
            Trigram('ण', 'क', 'ो'),
            Trigram('अ', 'प', 'र'),
            Trigram('े', ' ', 'स'),
            Trigram('ा', 'र', 'ी'),
            Trigram('।', 'क', 'ु'),
            Trigram(' ', 'द', 'ि'),
            Trigram(' ', 'ज', 'न'),
            Trigram('भ', 'े', 'द'),
            Trigram('र', 'ि', 'व'),
            Trigram('उ', 'स', 'क'),
            Trigram('क', ' ', 'र'),
            Trigram('र', ' ', 'अ'),
            Trigram('ि', ' ', 'स'),
            Trigram('ा', 'न', 'ु'),
            Trigram('ो', ' ', 'ह'),
            Trigram('र', 'ु', 'द'),
            Trigram(' ', 'छ', '।'),
            Trigram('ू', 'क', 'ो'),
            Trigram('र', 'क', 'ा'),
            Trigram('न', 'म', 'ा'),
            Trigram(' ', 'भ', 'न'),
            Trigram('र', '्', 'म'),
            Trigram('ह', 'ि', 'त'),
            Trigram('प', 'ू', 'र'),
            Trigram('न', '्', 'य'),
            Trigram('क', ' ', 'अ'),
            Trigram('ा', ' ', 'ब'),
            Trigram('ो', ' ', 'भ'),
            Trigram('र', 'ा', 'ज'),
            Trigram('अ', 'न', 'ु'),
            Trigram('ो', 'ष', 'ण'),
            Trigram('ष', 'ण', 'ा'),
            Trigram('य', ' ', 'र'),
            Trigram(' ', 'म', 'न'),
            Trigram(' ', 'ब', 'ि'),
            Trigram('्', 'ध', 'ा'),
            Trigram(' ', 'द', 'े'),
            Trigram('न', 'ि', 'र'),
            Trigram('त', 'ा', 'ह'),
            Trigram('र', ' ', 'उ'),
            Trigram('य', 'स', ' '),
            Trigram('उ', 'न', 'े'),
            Trigram('र', 'ण', ' '),
            Trigram('व', 'ि', 'क'),
        ],
    ),
];

/// Languages for script Hebrew
pub static HEBREW_LANGS: LangProfileList = &[
    (
        Lang::Heb,
        &[
            Trigram('ו', 'ת', ' '),
            Trigram('י', 'ם', ' '),
            Trigram('כ', 'ל', ' '),
            Trigram('ת', ' ', 'ה'),
            Trigram(' ', 'כ', 'ל'),
            Trigram('ד', 'ם', ' '),
            Trigram('א', 'ד', 'ם'),
            Trigram('י', 'ו', 'ת'),
            Trigram(' ', 'ש', 'ל'),
            Trigram(' ', 'ז', 'כ'),
            Trigram('ל', ' ', 'א'),
            Trigram(' ', 'א', 'ד'),
            Trigram('ש', 'ל', ' '),
            Trigram('ל', ' ', 'ה'),
            Trigram('א', 'י', ' '),
            Trigram('ו', 'י', 'ו'),
            Trigram('כ', 'א', 'י'),
            Trigram('ת', ' ', 'ו'),
            Trigram('י', ' ', 'ל'),
            Trigram('ז', 'כ', 'א'),
            Trigram(' ', 'ו', 'ל'),
            Trigram('ל', 'א', ' '),
            Trigram(' ', 'ו', 'ה'),
            Trigram('ר', 'ו', 'ת'),
            Trigram('ז', 'כ', 'ו'),
            Trigram('י', 'ת', ' '),
            Trigram('י', 'ר', 'ו'),
            Trigram('י', 'ן', ' '),
            Trigram(' ', 'א', 'ו'),
            Trigram('ם', ' ', 'ז'),
            Trigram(' ', 'ל', 'א'),
            Trigram(' ', 'ה', 'ח'),
            Trigram('א', 'ו', ' '),
            Trigram(' ', 'ה', 'א'),
            Trigram(' ', 'ו', 'ב'),
            Trigram(' ', 'ה', 'מ'),
            Trigram('ח', 'י', 'ר'),
            Trigram('ת', ' ', 'ל'),
            Trigram('י', 'י', 'ם'),
            Trigram('ם', ' ', 'ל'),
            Trigram('א', 'ת', ' '),
            Trigram('ת', ' ', 'ב'),
            Trigram('ת', ' ', 'ש'),
            Trigram('ר', 'ה', ' '),
            Trigram('ו', 'ן', ' '),
            Trigram(' ', 'ל', 'ה'),
            Trigram('נ', 'ה', ' '),
            Trigram('כ', 'ו', 'י'),
            Trigram('ו', 'ת', 'י'),
            Trigram('ה', ' ', 'ש'),
            Trigram('ו', ' ', 'ל'),
            Trigram('ו', ' ', 'ב'),
            Trigram(' ', 'ה', 'ו'),
            Trigram('ת', ' ', 'א'),
            Trigram('ם', ' ', 'ב'),
            Trigram('ם', ' ', 'ו'),
            Trigram('ת', 'ו', ' '),
            Trigram(' ', 'א', 'ת'),
            Trigram('ל', 'ה', ' '),
            Trigram('נ', 'י', ' '),
            Trigram('א', 'ו', 'מ'),
            Trigram(' ', 'ב', 'מ'),
            Trigram('ד', 'ה', ' '),
            Trigram('א', ' ', 'י'),
            Trigram('ה', ' ', 'ה'),
            Trigram('ה', ' ', 'ב'),
            Trigram('ע', 'ל', ' '),
            Trigram('ם', ' ', 'ה'),
            Trigram(' ', 'ע', 'ל'),
            Trigram('ה', 'ו', 'א'),
            Trigram('ו', 'ך', ' '),
            Trigram('ה', ' ', 'א'),
            Trigram('ב', 'ו', 'ד'),
            Trigram('ו', 'ד', ' '),
            Trigram('ו', 'א', 'י'),
            Trigram('נ', 'ו', 'ת'),
            Trigram('ה', ' ', 'ו'),
            Trigram('ת', ' ', 'כ'),
            Trigram('י', ' ', 'ה'),
            Trigram('י', 'ה', ' '),
            Trigram('ם', ' ', 'ש'),
            Trigram('ו', ' ', 'ו'),
            Trigram(' ', 'ש', 'ה'),
            Trigram('ם', ' ', 'א'),
            Trigram('ו', ' ', 'כ'),
            Trigram('י', 'נ', 'ו'),
            Trigram('ן', ' ', 'ה'),
            Trigram(' ', 'ש', 'ו'),
            Trigram('ש', 'ו', 'ו'),
            Trigram('ה', 'ח', 'י'),
            Trigram('כ', 'ו', 'ת'),
            Trigram('ל', 'א', 'ו'),
            Trigram('ב', 'ו', 'ת'),
            Trigram('ד', 'ו', 'ת'),
            Trigram('ה', ' ', 'ל'),
            Trigram('ל', 'י', 'ת'),
            Trigram('ה', ' ', 'מ'),
            Trigram(' ', 'ב', 'י'),
            Trigram('ו', 'ה', ' '),
            Trigram('ו', 'א', ' '),
            Trigram(' ', 'ה', 'י'),
            Trigram(' ', 'ל', 'פ'),
            Trigram('ו', 'ר', ' '),
            Trigram(' ', 'ל', 'ב'),
            Trigram('ל', ' ', 'ב'),
            Trigram('ב', 'ח', 'י'),
            Trigram('ה', 'כ', 'ר'),
            Trigram('ל', 'ו', ' '),
            Trigram('ת', ' ', 'מ'),
            Trigram('ן', ' ', 'ש'),
            Trigram('ה', 'ח', 'ו'),
            Trigram('ה', ' ', 'כ'),
            Trigram(' ', 'ב', 'כ'),
            Trigram('ו', 'מ', 'י'),
            Trigram('ב', 'י', 'ן'),
            Trigram('ן', ' ', 'ו'),
            Trigram('ן', ' ', 'ל'),
            Trigram('ר', 'ו', 'י'),
            Trigram('פ', 'ל', 'י'),
            Trigram('ו', 'ל', 'ה'),
            Trigram('ל', 'י', 'ה'),
            Trigram(' ', 'ה', 'ז'),
            Trigram('ח', 'י', 'נ'),
            Trigram(' ', 'ל', 'ע'),
            Trigram(' ', 'ב', 'נ'),
            Trigram('י', 'ב', 'ו'),
            Trigram('ח', 'ו', 'ק'),
            Trigram(' ', 'א', 'ח'),
            Trigram('ח', 'ב', 'ר'),
            Trigram(' ', 'י', 'ה'),
            Trigram(' ', 'ח', 'י'),
            Trigram('מ', 'י', ' '),
            Trigram('י', 'ר', 'ה'),
            Trigram(' ', 'ח', 'ו'),
            Trigram('ה', 'א', 'ד'),
            Trigram('ו', 'ו', 'ה'),
            Trigram('ח', 'ו', 'פ'),
            Trigram('ו', 'פ', 'ש'),
            Trigram('ו', 'ק', ' '),
            Trigram('נ', 'ו', ' '),
            Trigram('י', 'ו', ' '),
            Trigram('ל', ' ', 'מ'),
            Trigram('מ', 'ד', 'י'),
            Trigram('כ', 'ב', 'ו'),
            Trigram(' ', 'ה', 'ע'),
            Trigram('נ', 'ו', 'ך'),
            Trigram(' ', 'ה', 'ד'),
            Trigram('י', ' ', 'א'),
            Trigram('י', ' ', 'ו'),
            Trigram(' ', 'ה', 'כ'),
            Trigram('ב', 'נ', 'י'),
            Trigram('ע', 'ה', ' '),
            Trigram('ו', ' ', 'א'),
            Trigram('ר', 'צ', 'ו'),
            Trigram('ד', 'י', 'נ'),
            Trigram('ב', 'ז', 'כ'),
            Trigram('מ', 'ו', 'ת'),
            Trigram('י', 'פ', 'ו'),
            Trigram(' ', 'א', 'ל'),
            Trigram('ס', 'ו', 'ד'),
            Trigram('ל', 'ם', ' '),
            Trigram('א', 'י', 'ש'),
            Trigram('ר', 'ך', ' '),
            Trigram(' ', 'א', 'י'),
            Trigram('ה', 'ג', 'נ'),
            Trigram('ה', 'ם', ' '),
            Trigram('פ', 'י', ' '),
            Trigram('ם', ' ', 'כ'),
            Trigram('ח', 'ו', 'ת'),
            Trigram('ל', ' ', 'ו'),
            Trigram('א', 'י', 'ל'),
            Trigram('י', 'ל', 'י'),
            Trigram('ת', 'י', 'ה'),
            Trigram('כ', 'ל', 'ל'),
            Trigram('א', 'ל', 'י'),
            Trigram('י', 'ס', 'ו'),
            Trigram('ה', 'א', 'ו'),
            Trigram('ז', 'ש', ' '),
            Trigram(' ', 'ב', 'א'),
            Trigram('ר', ' ', 'א'),
            Trigram('ו', ' ', 'ה'),
            Trigram('ז', 'ו', ' '),
            Trigram('א', 'ח', 'ר'),
            Trigram(' ', 'ה', 'פ'),
            Trigram(' ', 'ב', 'ע'),
            Trigram(' ', 'ב', 'ז'),
            Trigram('מ', 'ש', 'פ'),
            Trigram(' ', 'ב', 'ה'),
            Trigram(' ', 'ל', 'ח'),
            Trigram('ד', 'ר', 'ך'),
            Trigram('ו', 'מ', 'ו'),
            Trigram(' ', 'ב', 'ח'),
            Trigram(' ', 'ד', 'ר'),
            Trigram(' ', 'מ', 'ע'),
            Trigram('ל', ' ', 'י'),
            Trigram('ת', 'ו', 'ך'),
            Trigram('מ', 'נ', 'ו'),
            Trigram(' ', 'ב', 'ש'),
            Trigram('ל', 'ל', ' '),
            Trigram('ר', 'ב', 'ו'),
            Trigram(' ', 'ל', 'מ'),
            Trigram('פ', 'נ', 'י'),
            Trigram(' ', 'ל', 'ק'),
            Trigram('ת', 'ם', ' '),
            Trigram('ש', 'ה', ' '),
            Trigram('ש', 'י', 'ת'),
            Trigram('ל', 'ל', 'א'),
            Trigram('ל', 'פ', 'י'),
            Trigram('ה', 'י', 'ה'),
            Trigram('מ', 'ע', 'ש'),
            Trigram('ד', 'ו', ' '),
            Trigram('ש', 'ו', 'ת'),
            Trigram('ל', 'ה', 'ג'),
            Trigram('ו', 'צ', 'י'),
            Trigram('ש', 'ו', 'א'),
            Trigram('א', 'י', 'ן'),
            Trigram('ו', 'י', ' '),
            Trigram('ת', 'י', ' '),
            Trigram('ו', 'נ', 'ו'),
            Trigram('ל', 'י', 'ל'),
            Trigram(' ', 'ל', 'ו'),
            Trigram('ח', 'י', 'י'),
            Trigram('ל', ' ', 'ז'),
            Trigram(' ', 'ז', 'ו'),
            Trigram('ה', 'י', 'א'),
            Trigram('י', 'א', ' '),
            Trigram('נ', 'ת', 'ו'),
            Trigram('ה', ' ', 'פ'),
            Trigram('ל', 'ת', ' '),
            Trigram('ו', 'ב', 'י'),
            Trigram(' ', 'ל', 'כ'),
            Trigram('ך', ' ', 'ה'),
            Trigram('י', 'ל', ' '),
            Trigram('י', ' ', 'ש'),
            Trigram('ש', 'י', 'ו'),
            Trigram('ן', ' ', 'ב'),
            Trigram('ע', 'ו', 'ל'),
            Trigram('ה', 'מ', 'ד'),
            Trigram('ו', 'ד', 'ה'),
            Trigram('ו', 'ל', 'ם'),
            Trigram(' ', 'ו', 'מ'),
            Trigram('א', ' ', 'ה'),
            Trigram('ו', 'ל', 'א'),
            Trigram(' ', 'ב', 'ת'),
            Trigram('ה', 'כ', 'ל'),
            Trigram(' ', 'ס', 'ו'),
            Trigram(' ', 'מ', 'ש'),
            Trigram(' ', 'ע', 'ב'),
            Trigram('ס', 'ו', 'צ'),
            Trigram('א', 'ר', 'צ'),
            Trigram(' ', 'א', 'ר'),
            Trigram('צ', 'י', 'א'),
            Trigram('ד', ' ', 'א'),
            Trigram('ל', 'ח', 'י'),
            Trigram('ה', 'ן', ' '),
            Trigram('י', 'ח', 'ס'),
            Trigram(' ', 'י', 'ח'),
            Trigram('י', 'א', 'ל'),
            Trigram('ה', 'ז', 'כ'),
            Trigram('ם', ' ', 'נ'),
            Trigram(' ', 'ש', 'ר'),
            Trigram('ב', 'ו', ' '),
            Trigram('ע', 'ב', 'ו'),
            Trigram('ה', 'י', 'ס'),
            Trigram(' ', 'ל', 'י'),
            Trigram('ת', ' ', 'ז'),
            Trigram('פ', 'ו', 'ל'),
            Trigram('י', 'ה', 'י'),
            Trigram('ג', 'ב', 'ל'),
            Trigram('ת', 'י', 'ו'),
            Trigram('ה', 'מ', 'א'),
            Trigram('ש', 'ה', 'י'),
            Trigram('א', ' ', 'ל'),
            Trigram('מ', 'א', 'ו'),
            Trigram(' ', 'י', 'ו'),
            Trigram('ו', 'ת', 'ו'),
            Trigram('י', 'ש', 'י'),
            Trigram('ג', 'נ', 'ה'),
            Trigram('פ', 'ש', 'י'),
            Trigram('ו', 'ח', 'ד'),
            Trigram('י', 'ה', 'ם'),
            Trigram('ח', 'ר', 'ו'),
            Trigram('ל', 'כ', 'ל'),
            Trigram('י', 'ד', 'ה'),
            Trigram('ע', 'ו', 'ת'),
            Trigram('ו', 'נ', 'ה'),
            Trigram('ו', 'ם', ' '),
            Trigram('ח', 'ה', ' '),
            Trigram('ע', 'ם', ' '),
            Trigram('ש', 'ר', 'י'),
            Trigram('ם', ' ', 'י'),
            Trigram('ש', 'ר', ' '),
            Trigram('ו', 'ה', 'ח'),
            Trigram(' ', 'א', 'ש'),
            Trigram(' ', 'ה', 'ג'),
            Trigram('ק', ' ', 'ב'),
            Trigram('ה', 'פ', 'ל'),
            Trigram('נ', 'ש', 'ו'),
            Trigram('ה', 'ג', 'ב'),
            Trigram('ד', ' ', 'ו'),
        ],
    ),
    (
        Lang::Yid,
        &[
            Trigram(' ', 'פ', 'ֿ'),
            Trigram('ו', 'ן', ' '),
            Trigram('ע', 'ר', ' '),
            Trigram('ן', ' ', 'א'),
            Trigram(' ', 'א', 'ַ'),
            Trigram('ד', 'ע', 'ר'),
            Trigram('ט', ' ', 'א'),
            Trigram(' ', 'א', 'ו'),
            Trigram('א', 'ו', 'ן'),
            Trigram('א', 'ַ', 'ר'),
            Trigram('ע', 'ן', ' '),
            Trigram('פ', 'ֿ', 'ו'),
            Trigram(' ', 'א', 'ױ'),
            Trigram(' ', 'א', 'י'),
            Trigram('ן', ' ', 'פ'),
            Trigram('ֿ', 'ו', 'ן'),
            Trigram('ר', 'ע', 'כ'),
            Trigram(' ', 'ד', 'ע'),
            Trigram(' ', 'ר', 'ע'),
            Trigram('ע', 'כ', 'ט'),
            Trigram('פ', 'ֿ', 'א'),
            Trigram('ן', ' ', 'ד'),
            Trigram('כ', 'ט', ' '),
            Trigram(' ', 'ד', 'י'),
            Trigram('ד', 'י', ' '),
            Trigram('א', 'ַ', ' '),
            Trigram('א', 'ױ', 'ף'),
            Trigram('ױ', 'ף', ' '),
            Trigram('ֿ', 'א', 'ַ'),
            Trigram(' ', 'ז', 'ײ'),
            Trigram(' ', 'ג', 'ע'),
            Trigram('א', 'ַ', 'ל'),
            Trigram('א', 'ָ', 'ס'),
            Trigram(' ', 'א', 'ָ'),
            Trigram('ו', 'נ', 'ג'),
            Trigram(' ', 'ה', 'א'),
            Trigram('ה', 'א', 'ָ'),
            Trigram('ז', 'ײ', 'ַ'),
            Trigram(' ', 'מ', 'ע'),
            Trigram('א', 'ָ', 'ל'),
            Trigram('נ', 'ג', ' '),
            Trigram('װ', 'א', 'ָ'),
            Trigram('ַ', 'ן', ' '),
            Trigram('א', 'ַ', 'נ'),
            Trigram('ר', 'ײ', 'ַ'),
            Trigram(' ', 'װ', 'א'),
            Trigram('ָ', 'ס', ' '),
            Trigram('ב', 'א', 'ַ'),
            Trigram(' ', 'י', 'ע'),
            Trigram('י', 'ע', 'ד'),
            Trigram('נ', 'י', 'ט'),
            Trigram('ן', ' ', 'ז'),
            Trigram('ר', ' ', 'א'),
            Trigram('י', 'ט', ' '),
            Trigram('א', 'ָ', 'ט'),
            Trigram('א', 'ָ', 'ר'),
            Trigram('ע', 'ד', 'ע'),
            Trigram('מ', 'ע', 'ן'),
            Trigram('ז', 'א', 'ָ'),
            Trigram('ָ', 'ט', ' '),
            Trigram('פ', 'ֿ', 'ר'),
            Trigram('ײ', 'ַ', 'ן'),
            Trigram(' ', 'ב', 'א'),
            Trigram('ט', 'ן', ' '),
            Trigram('א', 'י', 'ן'),
            Trigram('ן', ' ', 'ג'),
            Trigram('י', 'ן', ' '),
            Trigram('ן', ' ', 'װ'),
            Trigram('נ', 'א', 'ַ'),
            Trigram('ֿ', 'ר', 'ײ'),
            Trigram('ר', ' ', 'ה'),
            Trigram(' ', 'ז', 'א'),
            Trigram('ל', 'ע', 'כ'),
            Trigram('ע', ' ', 'א'),
            Trigram('א', 'ָ', 'ד'),
            Trigram('ַ', ' ', 'ר'),
            Trigram('ע', 'נ', 'ט'),
            Trigram('א', 'ַ', 'צ'),
            Trigram('ַ', 'צ', 'י'),
            Trigram('א', 'ָ', 'נ'),
            Trigram(' ', 'צ', 'ו'),
            Trigram(' ', 'װ', 'ע'),
            Trigram('י', 'ז', ' '),
            Trigram('מ', 'ע', 'נ'),
            Trigram('ָ', 'ד', 'ע'),
            Trigram('א', 'י', 'ז'),
            Trigram('ן', ' ', 'מ'),
            Trigram('ַ', 'ל', 'ע'),
            Trigram('ב', 'ן', ' '),
            Trigram('ר', ' ', 'מ'),
            Trigram('ט', 'ע', 'ר'),
            Trigram(' ', 'מ', 'י'),
            Trigram(' ', 'פ', 'ּ'),
            Trigram('מ', 'י', 'ט'),
            Trigram('ט', 'ל', 'ע'),
            Trigram('ָ', 'ל', ' '),
            Trigram('ע', 'כ', 'ע'),
            Trigram('ײ', 'ט', ' '),
            Trigram('ַ', 'נ', 'ד'),
            Trigram('ע', ' ', 'פ'),
            Trigram('ל', 'ע', ' '),
            Trigram('ג', 'ע', 'ז'),
            Trigram('ל', 'א', 'ַ'),
            Trigram('א', 'ַ', 'פ'),
            Trigram('ע', 'ז', 'ע'),
            Trigram('ר', 'א', 'ַ'),
            Trigram(' ', 'נ', 'י'),
            Trigram('ַ', 'פ', 'ֿ'),
            Trigram('ר', 'ן', ' '),
            Trigram('ײ', 'ַ', 'נ'),
            Trigram('נ', 'ע', 'ן'),
            Trigram('ט', 'י', 'ק'),
            Trigram('כ', 'ע', ' '),
            Trigram('פ', 'ֿ', 'ע'),
            Trigram('י', 'ע', ' '),
            Trigram('ה', 'ײ', 'ט'),
            Trigram('ַ', 'ה', 'ײ'),
            Trigram('נ', 'ט', 'ש'),
            Trigram('ײ', 'ַ', 'ה'),
            Trigram('ט', ' ', 'ד'),
            Trigram('ן', ' ', 'ב'),
            Trigram('ל', 'ן', ' '),
            Trigram('ן', ' ', 'נ'),
            Trigram('פ', 'ֿ', 'ט'),
            Trigram('ש', 'א', 'ַ'),
            Trigram('ר', 'ו', 'נ'),
            Trigram(' ', 'ז', 'י'),
            Trigram(' ', 'װ', 'י'),
            Trigram('ט', ' ', 'פ'),
            Trigram(' ', 'ד', 'א'),
            Trigram('ט', 'א', 'ָ'),
            Trigram('ד', 'י', 'ק'),
            Trigram('ק', 'ן', ' '),
            Trigram('ר', ' ', 'פ'),
            Trigram('ר', ' ', 'ג'),
            Trigram('י', 'ק', 'ן'),
            Trigram('א', 'ָ', 'ב'),
            Trigram('ף', ' ', 'א'),
            Trigram('א', 'ַ', 'ק'),
            Trigram('ק', 'ע', 'ר'),
            Trigram('ע', 'ר', 'ע'),
            Trigram('כ', 'ע', 'ר'),
            Trigram('י', ' ', 'פ'),
            Trigram('ו', 'ת', ' '),
            Trigram('ַ', 'ר', 'ב'),
            Trigram('פ', 'ּ', 'ר'),
            Trigram('ק', 'ט', ' '),
            Trigram('ע', 'ם', ' '),
            Trigram('י', 'א', 'ָ'),
            Trigram('צ', 'י', 'ע'),
            Trigram('צ', 'י', 'א'),
            Trigram('י', 'ט', '־'),
            Trigram('צ', 'ו', ' '),
            Trigram('י', 'ש', 'ע'),
            Trigram(' ', 'ק', 'ײ'),
            Trigram('ן', ' ', 'ק'),
            Trigram('ס', 'ע', 'ר'),
            Trigram(' ', 'ג', 'ל'),
            Trigram('ד', 'א', 'ָ'),
            Trigram('ו', 'נ', 'ט'),
            Trigram('ג', 'ן', ' '),
            Trigram('ַ', 'ר', 'א'),
            Trigram('י', 'ק', 'ע'),
            Trigram(' ', 'ט', 'א'),
            Trigram('ע', 'נ', 'ע'),
            Trigram('ל', 'ײ', 'ַ'),
            Trigram('ש', 'ן', ' '),
            Trigram('ַ', 'נ', 'ע'),
            Trigram('י', 'ק', ' '),
            Trigram('ט', 'א', 'ַ'),
            Trigram('ס', ' ', 'א'),
            Trigram('ע', 'ט', ' '),
            Trigram('נ', 'ג', 'ע'),
            Trigram('ט', '־', 'א'),
            Trigram('ָ', 'נ', 'א'),
            Trigram('־', 'א', 'י'),
            Trigram('י', 'ק', 'ט'),
            Trigram('נ', 'ט', 'ע'),
            Trigram('ײ', 'נ', 'ע'),
            Trigram('־', 'נ', 'י'),
            Trigram('ָ', 'ר', ' '),
            Trigram('װ', 'ע', 'ר'),
            Trigram('י', ' ', 'א'),
            Trigram('ן', ' ', 'י'),
            Trigram('י', 'ך', ' '),
            Trigram('ז', 'י', 'ך'),
            Trigram('ע', 'ר', '־'),
            Trigram('ע', 'ר', 'ן'),
            Trigram('א', 'ױ', 'ס'),
            Trigram('ָ', 'ב', 'ן'),
            Trigram('נ', 'ד', 'ע'),
            Trigram('ָ', 'ס', 'ע'),
            Trigram('װ', 'י', ' '),
            Trigram('ֿ', 'ע', 'ל'),
            Trigram('ר', '־', 'נ'),
            Trigram('ן', ' ', 'ה'),
            Trigram(' ', 'ג', 'ר'),
            Trigram('ג', 'ל', 'ײ'),
            Trigram(' ', 'צ', 'י'),
            Trigram('ר', 'א', 'ָ'),
            Trigram('ז', 'ע', 'ל'),
            Trigram('ע', 'ל', 'ק'),
            Trigram('נ', 'ד', ' '),
            Trigram('ל', 'ק', 'ע'),
            Trigram('א', 'ָ', 'פ'),
            Trigram(' ', 'כ', 'ּ'),
            Trigram('ט', ' ', 'װ'),
            Trigram('ג', ' ', 'א'),
            Trigram(' ', 'נ', 'א'),
            Trigram('ט', ' ', 'צ'),
            Trigram('ר', ' ', 'ד'),
            Trigram('ע', 'ס', ' '),
            Trigram('ד', 'ו', 'ר'),
            Trigram('ג', 'ע', 'ן'),
            Trigram('ק', 'ע', ' '),
            Trigram('ג', ' ', 'פ'),
            Trigram('ֿ', 'ט', ' '),
            Trigram('ן', ' ', 'ל'),
            Trigram('ש', 'ע', ' '),
            Trigram('ר', ' ', 'ז'),
            Trigram('ר', 'ע', ' '),
            Trigram('ײ', 'ט', 'ן'),
            Trigram('פ', 'ּ', 'ע'),
            Trigram('ק', 'ל', 'א'),
            Trigram('ק', 'ײ', 'ט'),
            Trigram('י', 'ט', 'ע'),
            Trigram('י', 'ם', ' '),
            Trigram('ס', ' ', 'ז'),
            Trigram('ײ', 'ַ', ' '),
            Trigram(' ', 'ד', 'ו'),
            Trigram('א', 'ַ', 'ט'),
            Trigram(' ', 'ל', 'א'),
            Trigram('ר', ' ', 'װ'),
            Trigram('ק', 'ײ', 'נ'),
            Trigram('ע', 'ל', 'ש'),
            Trigram('י', ' ', 'ד'),
            Trigram('ל', 'ש', 'א'),
            Trigram('י', 'ו', 'ת'),
            Trigram('נ', 'ט', ' '),
            Trigram('ַ', 'ר', 'ז'),
            Trigram('ע', ' ', 'ר'),
            Trigram('ל', ' ', 'ז'),
            Trigram('א', 'ַ', 'מ'),
            Trigram('ן', ' ', 'ש'),
            Trigram(' ', 'ש', 'ו'),
            Trigram('א', 'י', 'נ'),
            Trigram('נ', 'ט', 'ל'),
            Trigram(' ', 'ה', 'י'),
            Trigram('ב', 'ע', 'ט'),
            Trigram('ָ', 'פ', 'ּ'),
            Trigram('ף', ' ', 'פ'),
            Trigram('ײ', 'ַ', 'כ'),
            Trigram('ב', 'ע', 'ר'),
            Trigram('ן', ' ', 'צ'),
            Trigram('מ', 'א', 'ָ'),
            Trigram(' ', 'ש', 'ט'),
            Trigram(' ', 'ל', 'ע'),
            Trigram('ג', 'ע', 'ר'),
            Trigram('ו', 'ר', 'ך'),
            Trigram('ר', 'ך', ' '),
            Trigram('נ', 'ע', 'ם'),
            Trigram('ג', 'ר', 'ו'),
            Trigram('פ', 'ֿ', 'ן'),
            Trigram('ל', 'ע', 'ר'),
            Trigram('װ', 'ע', 'ל'),
            Trigram('ע', ' ', 'מ'),
            Trigram('ו', 'ם', ' '),
            Trigram('ש', 'פ', 'ּ'),
            Trigram('ך', ' ', 'א'),
            Trigram('י', 'ו', 'נ'),
            Trigram('ר', 'ב', 'ע'),
            Trigram('ע', 'פ', 'ֿ'),
            Trigram('ט', 'ע', 'ט'),
            Trigram('ן', ' ', 'כ'),
            Trigram('ר', 'ע', 'ס'),
            Trigram('ע', 'ר', 'צ'),
            Trigram('ז', ' ', 'א'),
            Trigram('ע', 'מ', 'ע'),
            Trigram('ם', ' ', 'א'),
            Trigram('ש', 'ט', 'ע'),
            Trigram('כ', 'ן', ' '),
            Trigram('ר', 'ט', ' '),
            Trigram('י', ' ', 'ג'),
            Trigram('ס', 'ן', ' '),
            Trigram('נ', 'ע', 'ר'),
            Trigram('ל', 'י', 'ט'),
            Trigram('ט', ' ', 'ז'),
            Trigram('נ', 'ע', 'מ'),
            Trigram('ּ', 'ר', 'א'),
            Trigram('ה', 'י', 'ו'),
            Trigram('א', 'ַ', 'ש'),
            Trigram('ת', ' ', 'װ'),
            Trigram('א', 'ו', 'מ'),
            Trigram('ק', ' ', 'א'),
            Trigram('י', 'ב', 'ע'),
            Trigram('ֿ', 'ן', ' '),
            Trigram('ץ', ' ', 'א'),
            Trigram('פ', 'ֿ', 'י'),
            Trigram('ײ', 'ן', ' '),
            Trigram('ם', ' ', 'ט'),
        ],
    ),
];
```

## File: `src/trigrams/utils.rs`
```rust
use hashbrown::HashMap;

use super::TEXT_TRIGRAMS_SIZE;
use super::Trigram;
use crate::core::LowercaseText;
use crate::utils::is_stop_char;

pub struct TrigramsWithPositions {
    pub(crate) _total_trigrams: u32,
    pub(crate) trigram_positions: HashMap<Trigram, u32>,
}

#[inline]
pub fn get_trigrams_with_positions(text: &LowercaseText) -> TrigramsWithPositions {
    let CountResult {
        total_trigrams,
        trigram_occurances,
    } = count(text);
    let trigram_positions = trigram_occurances_to_positions(trigram_occurances);
    TrigramsWithPositions {
        _total_trigrams: total_trigrams,
        trigram_positions,
    }
}

#[inline]
#[allow(clippy::unnecessary_sort_by)]
fn trigram_occurances_to_positions(
    trigram_occurances: HashMap<Trigram, u32>,
) -> HashMap<Trigram, u32> {
    // Sort in descending order by number of occurrences and trigrams
    let mut count_vec: Vec<_> = trigram_occurances
        .into_iter()
        .map(|(trigram, count)| (count, trigram))
        .collect();
    count_vec.sort_unstable_by(|a, b| b.cmp(a));

    count_vec
        .into_iter()
        .take(TEXT_TRIGRAMS_SIZE) // we're interested only in the first 600 (2 * MAX_TRIGRAM_DISTANCE)
        .enumerate()
        .map(|(i, (_, trigram))| (trigram, i as u32))
        .collect()
}

struct CountResult {
    total_trigrams: u32,
    trigram_occurances: HashMap<Trigram, u32>,
}

#[inline]
fn count(text: &LowercaseText) -> CountResult {
    let hash_capacity = calculate_initial_hash_capacity(text);
    let mut trigram_occurances: HashMap<Trigram, u32> = HashMap::with_capacity(hash_capacity);
    let mut total_trigrams = 0;

    // iterate through the string and count trigrams
    let mut chars_iter = text
        .chars()
        .map(to_trigram_char)
        //.flat_map(char::to_lowercase)
        .chain(Some(' '));
    let mut c1 = ' ';
    // unwrap is safe, because we always chain a space character on the end of the iterator
    let mut c2 = chars_iter.next().unwrap();
    for cur_char in chars_iter {
        let c3 = cur_char;
        if !(c2 == ' ' && (c1 == ' ' || c3 == ' ')) {
            let trigram = Trigram(c1, c2, c3);
            let count = trigram_occurances.entry(trigram).or_insert(0);
            *count += 1;
            total_trigrams += 1;
        }
        c1 = c2;
        c2 = c3;
    }

    CountResult {
        total_trigrams,
        trigram_occurances,
    }
}

// Convert punctuations and digits to a space.
#[inline]
fn to_trigram_char(ch: char) -> char {
    if is_stop_char(ch) { ' ' } else { ch }
}

// In order to improve performance, define the initial capacity for trigrams hash map,
// based on the size of the input text.
#[inline]
fn calculate_initial_hash_capacity(text: &str) -> usize {
    const MAX_INITIAL_HASH_CAPACITY: usize = 2048;

    let len = text.len();
    if len > MAX_INITIAL_HASH_CAPACITY {
        MAX_INITIAL_HASH_CAPACITY
    } else {
        len
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn assert_valuable_trigram_chars(chars: &[char]) {
        for &ch in chars.iter() {
            assert_eq!(to_trigram_char(ch), ch);
        }
    }

    fn assert_not_valuable_trigram_chars(chars: &[char]) {
        for &ch in chars.iter() {
            assert_eq!(to_trigram_char(ch), ' ');
        }
    }

    #[test]
    fn test_to_trigram_char() {
        // valuable chars, that matters
        assert_valuable_trigram_chars(&['a', 'z', 'A', 'Z', 'Ж', 'ß']);

        // punctuations, digits, etc..
        //
        // 0x00 - 0x40
        assert_not_valuable_trigram_chars(&['\t', '\n', ' ', '.', '0', '9', ',', '@']);
        // 0x5B - 0x60
        assert_not_valuable_trigram_chars(&['[', ']', '^', '\\', '`']);
        // 0x7B - 0x7E
        assert_not_valuable_trigram_chars(&['[', '|', '{', '}', '~']);
    }

    fn assert_count(text: &str, pairs: &[(&str, u32)]) {
        let lowercase_text = LowercaseText::new(text);
        let CountResult {
            total_trigrams: _,
            trigram_occurances,
        } = count(&lowercase_text);
        for &(trigram_str, expected_n) in pairs.iter() {
            let chars: Vec<char> = trigram_str.chars().collect();
            let trigram = Trigram(chars[0], chars[1], chars[2]);
            let actual_n = trigram_occurances[&trigram];
            assert_eq!(
                actual_n, expected_n,
                "trigram '{:?}' expected to occur {} times, got {}",
                trigram, expected_n, actual_n
            );
        }
        assert_eq!(trigram_occurances.len(), pairs.len());
    }

    #[test]
    fn test_count() {
        assert_count("", &[]);
        assert_count(",", &[]);
        assert_count("a", &[(" a ", 1)]);
        assert_count("-a-", &[(" a ", 1)]);
        assert_count("yes", &[(" ye", 1), ("yes", 1), ("es ", 1)]);
        assert_count(
            "Give - IT...",
            &[
                (" gi", 1),
                ("giv", 1),
                ("ive", 1),
                ("ve ", 1),
                (" it", 1),
                ("it ", 1),
            ],
        );
    }

    #[test]
    fn test_get_trigrams_with_positions() {
        let lowercase_text = LowercaseText::new("xaaaaabbbb    d");
        let TrigramsWithPositions {
            _total_trigrams,
            trigram_positions,
        } = get_trigrams_with_positions(&lowercase_text);

        assert_eq!(trigram_positions[&Trigram('a', 'a', 'a')], 0);
        assert_eq!(trigram_positions[&Trigram('b', 'b', 'b')], 1);
        assert_eq!(_total_trigrams, 11);
    }
}
```

## File: `tests/detect.rs`
```rust
extern crate serde_json;
extern crate whatlang;

use whatlang::{Lang, Script, detect, detect_lang};

use std::collections::HashMap;

#[test]
fn test_with_multiple_examples() {
    let example_data = include_str!("examples.json");

    let examples: HashMap<String, String> = serde_json::from_str(example_data).unwrap();

    for (lang_code, text) in examples {
        print!("Test {} ... ", lang_code);

        let lang = Lang::from_code(lang_code).expect("Unknown language code");
        let detected_lang = detect_lang(&text).unwrap();
        assert_eq!(detected_lang, lang);
    }
}

#[test]
fn test_with_russian_text() {
    let text = r#"
        Мой дядя самых честных правил,
        Когда не в шутку занемог,
        Он уважать себя заставил
        И лучше выдумать не мог.
    "#;

    let info = detect(text).unwrap();
    assert_eq!(info.script(), Script::Cyrillic);
    assert_eq!(info.script().name(), "Cyrillic");
    assert_eq!(info.lang(), Lang::Rus);
    assert_eq!(info.lang().code(), "rus");
    assert_eq!(info.lang().eng_name(), "Russian");
    assert_eq!(info.lang().name(), "Русский");

    assert_eq!(info.confidence(), 1.0);
    assert!(info.is_reliable());
}

#[test]
fn test_japanese_with_mandarin_chars() {
    let text = r#"
        この間、川越城や松井田城などの諸城を拡張・改修 河越城の三の丸と八幡郭など拡張、松井田城の大道寺郭構築など
    "#;

    let info = detect(text).unwrap();
    assert_eq!(info.script(), Script::Mandarin);
    assert_eq!(info.lang(), Lang::Jpn);
    assert!(info.is_reliable());
}
```

## File: `tests/examples.json`
```json
{
  "cmn": "民國卅八年（ 1949年 ）， 從南京經 廣州 、 香港返回 香日德。 1950年6月 ，受十世班禪派遣， 前往西安代表班禪向彭德懷投誠 。 1951年 ，隨同十世班禪赴 北京 ，同年代表班禪列席代表資格到北京參與了和平解放西藏的談判。",
  "spa": "Y así mismo, aunque no son tan ágiles en el suelo como el vampiro común, son muy competentes al escalar por las ramas.",
  "eng": "Showing that even in the modern warfare of the 1930s and 1940s, the dilapidated fortifications still had defensive usefulness.",
  "hin": "उन्होंने बताया कि जेब में 14 हजार रूपए थे और जेब उस वक्त कटी जब वे वहां पर हुए एक हादसे में घायल युवक का हालचाल पूछने के लिए अपनी ग़ाडी से उतरे।",
  "ara": "عندما يريد العالم أن ‪يتكلّم ‬ ، فهو يتحدّث بلغة يونيكود. تسجّل الآن لحضور المؤتمر الدولي العاشر ليونيكود",
  "rus": "Происхождение названия Село в советское время в официальных документах на русском языке именовалось «Возрожденовка» Акт проверки Конгрессовского сахарного комбината.",
  "ben": "যদিও চার্লস অনেক যুদ্ধে জড়িত ছিলেন, কিন্তু তিনি সব সময় তাঁর রাজ্যের মধ্যে শান্তি বজায় রাখার চেষ্টা করেছেন।",
  "por": "Aliás, no dia 8, antes da estreia do filme no mercado latino, o produtor Luiz Carlos Barreto, de 81 anos, pai do diretor, começa em 52 municípios gaúchos que não têm cinemas o seu projeto itinerante Roda Brasil.",
  "fra": "La CGT avait d'ailleurs critiqué l'avis de la Commission de garanties qui marquait, selon elle, le début d'\"un processus sans fin d'allongement de la durée de cotisation pour tous les salariés\" qui passerait ensuite à 42 ans en 2020.",
  "deu": "Es ist die Zeit des Sommers, des üppigen Wachstums, des Eintritts in die Pubertät und des Erwachens der Sexualität.",
  "ukr": "Середньовічний Львів був важливим політичним, економічним і культурним центром західної Русі.",
  "kat": "მასალა ვიკიპედიიდან — თავისუფალი ენციკლოპედია",
  "jpn": "Rust（ラスト）は並列かつマルチパラダイムのプログラミング言語である",
  "heb": "האקדמיה ללשון העברית",
  "yid": "מענטשן איבער דער װעלט, בעיקר פֿונעם אַשכנזישן אָפּשטאַם",
  "pol": "W języku polskim opozycja spółgłosek miękkich i twardych stała się cechą istotną.",
  "amh": "አማርኛ ፡ የኢትዮጵያ ፡ መደበኛ ፡ ቋንቋ ፡ ነው። ከሴማዊ ፡ ቋንቋዎች ፡ እንደ ፡ ዕብራይስጥ ፡ ወይም ፡ ዓረብኛ ፡ አንዱ ፡ ነው። በአፍሪካ ፡ ውስጥ ፡ ደግሞ ፡ ከምዕራብ ፡ አፍሪካው ፡ ሐውሳና ፡ ከምሥራቅ ፡ አፍሪካው ፡ ስዋሂሊ ፡ ቀጥሎ ፡ 3ኛውን ፡ ቦታ ፡ የያዘ ፡ ነው።[1] እንዲያውም ፡ 85.6 ፡ ሚሊዮን ፡ ያህል ፡ ተናጋሪዎች ፡ እያሉት ፣ አማርኛ ፡ ከአረብኛ ፡ ቀጥሎ ፡ ትልቁ ፡ ሴማዊ ፡ ቋንቋ ፡ ነው። የሚጻፈውም ፡ በአማርኛ ፡ ፊደል ፡ ነው። አማርኛ ፡ ከዓረብኛና ፡ ከዕብራይስጥ ፡ ያለው ፡ መሰረታዊ ፡ ልዩነት ፡ እንደ ፡ ላቲን ፡ ከግራ ፡ ወደ ፡ ቀኝ ፡ መጻፉ ፡ ነው።",
  "epo": "Estas vere tre malfacile verki facilajn tekstojn, do tio ne estas tasko por komencantoj, sed rekompence vi havos multajn legantojn.",
  "jav": "Basa Jawa dadi salah sijiné panyumbang sing gedhé dhéwé kanggo panuwuhané basa Indonésia. Sanadyan dudu basa resmi ing pamaréntahan, basa Jawa nduwé prabawa luwih akèh tinimbang basa-basa laladan liyané kayata ing kosakata, lan istilah-istilah sing kadhangkala nganggo tembung Jawa.",
  "kor": "늑대의 속은 개속에 속하며, 회색 늑대는 더 작은 아속인 코요테나 황금자칼과 비교하여 형태학적으로 몸집이 큰 먹이를 사냥하는 데 갖춰주었고 좀 더 집단적인 성격을 갖추며, 고도의 의사소통을 갖추어서 전문종으로 분류한다",
  "ita": "Giocò un ruolo di grande importanza nel movimento comunista internazionale con l'avvio di un processo di distanziamento dall'Unione Sovietica e l'elaborazione di un modello alternativo che prese il nome di eurocomunismo.",
  "nob": "Han reiste til Bergen for å få arbeidet sine vurdert av biskop Jacob Neumann. Denne ble svært imponert over språkarbeidet, og deler av arbeidet ble trykt i to nummer av Bergens Stiftstidende i 1841. Kontakten med biskop Neumann ble inngangsbilletten til Det kgl. Norske Videnskabers Selskab og raus pengestøtte som gjorde den omfattende reisingen mulig.",
  "dan": "Dansk kan til en vis grad sammenlignes med engelsk, da det danske ordforråd nu hovedsagelig vokser ved at optage låneord, for det meste engelske, på samme måde som engelsk indoptager ord fra andre sprog. I senmiddelalderen blev dansk udsat for en meget stærk plattysk påvirkning fra indvandrede hanseatiske købmænd og håndværkere. 25-50%[2][3] af det nuværende danske ordforråd stammer oprindeligt fra plattysk. Efter reformationen spillede hertugdømmerne en stor rolle i det tyske sprogs stærke stilling, samtidig med at stort antal nordtyskere indvandrede, og tyskere blev optaget i kancellierne[4]. Desuden var plattysk mange danske middelalderkongers egentlige modersmål, og nogle af dem kunne ikke tale dansk. Dog er det grundlæggende ordforråd stadig nordisk. Engelsk har siden 1950'erne været hovedleverandør af låneord til dansk. I de sidste 10-15 år er sproget i mange virksomheder også blevet engelsk i takt med internationaliseringen af erhvervslivet og øget anvendelse af personale fra udlandet.",
  "swe": "I början av 1900-talet reste Karl Tirén runt i Lappland och Nordnorge för att dokumentera och uppsamla jojkar. Detta arbete tog många år i anspråk och sammanfattades i verket Die lappische Volkmusik, utgiven av Hugo Gebers Förlag i Uppsala 1942. Genom dokumentationen av jojkar utförde Tirén en pionjärinsats i och med att han använde fonografen. Hans arbete har bidragit till att bevara en utdöende och uråldrig jojktradition till eftervärlden. Karl Tirén blev känd även som fiolbyggare och folkmusiker.",
  "fin": "Kansanvaltuuskunnan nimilista pohjautui pitkälti Suomen työväen toimeenpanevan komitean puheenjohtajan Eero Haapalaisen ehdotukseen, jonka hän esitteli toimeenpanevan komitean suljetussa kokouksessa 25. tammikuuta 1918",
  "tur": "1890’lar Debussy’nin kariyerindeki en verimli dönemdir. Bu dönemin en önemli eseri Pellas et Melisande operasıdır. Bu eserin 1902’de seslendirilişi uluslar arası bir başarı oldu. Pell as’dan sonra ünlenen Debussy, Avrupa başkentlerini gezerek eserlerini piyanist veya orkestra şefi olarak seslendirdi. Bu dönemde yazdığı makalelerle esprili bir eleştirmen olarak da tanındı.",
  "nld": "De Goede Verwachting was een windmolen in Amsterdam, aan de huidige Czaar Peterstraat. De chocolademolen, die is 1801 is gebouwd op het onderste deel van de boormolen die er eerder stond, is in 1906 afgebroken, toen hij al volledig door stadsbebouwing was omringd. De tekening laat de molen zien in 1887, met op de voorgrond de laatste restanten van de stadsmuren. Op de foto van Jacob Olie uit 1891 is te zien hoe de wieken met oude zakken of (dek)zeilen zijn bespannen.",
  "hun": "Versenyzői karrierje az 1920-as évek elején kezdődött, amikor a Fafnir autógyárnál volt tanonc. Eleinte motorkerékpárokkal, később autókkal versenyzett. Első két hegyi Európa-bajnoki címét a Mercedes-Benz színeiben érte el, a harmadikat már az Alfa Romeóval.",
  "ces": "Puccini viděl Sardouovu hru, když byla uváděna během turné v roce 1889 v Itálii, a po určitém váhání v roce 1895 získal práva na zhudebnění tohoto dramatu. Převedení mnohomluvné francouzské hry do výstižné italské opery trvalo čtyři roky, během nichž se skladatel opakovaně dohadoval se svými libretisty a vydavatelem. Tosca pak měla premiéru v době nepokojů v Římě a její první uvedení bylo ze strachu z narušení o jeden den odloženo. Přes nevalné hodnocení kritiků měla opera okamžitý úspěch u veřejnosti.",
  "ell": "Μετά τη διάλυση της Δεύτερης Τριανδρίας, ο Οκταβιανός αναβίωσε φαινομενικά τη Ρωμαϊκή Δημοκρατία, παραδίδοντας και πάλι την εκτελεστική εξουσία στη Σύγκλητο, ωστόσο στην πράξη διατήρησε το στάτους του απόλυτου μονάρχη. Πέρασαν πολλά χρόνια μέχρι να οριστικοποιηθεί το θεσμικό πλαίσιο διαμέσου του οποίου ένα πρώην δημοκρατικό κράτος μετατράπηκε σε μοναρχία, αποτέλεσμα του οποίο ήταν ο γίγαντας που αποκαλούμε Ρωμαϊκή Αυτοκρατορία.",
  "bul": "Българският език е най-ранният писмено документиран славянски език. Историческото му развитие се характеризира с четири главни периода. Следва да се отбележи, че това делене е условно и имената не отразяват различни езици, а само периоди в развитието на българския език, за които се откриват характерни белези.",
  "bel": "Беларуская мова з'яўляецца старажытнапісьменнай, бо гісторыя беларускага пісьменства налічвае не менш за 10 стаго-ддзяў. Мова беларускага народа пачала складацца ў XIV—XVI стагоддзях у Вялікім Княстве Літоўскім, і была канчаткова сфармулявана ў канцы XIX—XX стагоддзяў.",
  "mar": "मराठी ही इंडो-युरोपीय भाषाकुलातील एक भाषा आहे. भारतातील प्रमुख २२ भाषांपैकी मराठी एक आहे. महाराष्ट्र आणि गोवा ह्या राज्यांची मराठी ही अधिकृत राजभाषा आहे. मराठी मातृभाषा असणार्‍या लोकसंख्येनुसार मराठी ही जगातील पंधरावी व भारतातील चौथी भाषा आहे.[१] मराठी बोलणार्‍यांची एकूण लोकसंख्या ९,००,००,००० आहे. मराठी भाषा ९व्या शतकापासून प्रचलित आहे. मराठी भाषेची निर्मिती संस्कृतपासून झालेल्या महाराष्ट्री प्राकृत व अपभ्रंश या भाषांपासून झाली आहे. याउलट मराठी आणि काही अन्य भारतीय भाषांच्यावर संस्कार होऊन संस्कृत भाषा बनली असेही काही विद्वान मानतात.",
  "kan": "ಕನ್ನಡವು ಒಂದು ದ್ರಾವಿಡ ಭಾಷೆಯಾಗಿದೆ. ಕನ್ನಡ ಲಿಪಿ ಸುಮಾರು ೧೫೦೦-೧೬೦೦ ವರ್ಷಗಳಿಗಿಂತಲೂ ಹಿಂದಿನದು. ಐದನೆಯ ಶತಮಾನದ ಹಲ್ಮಿಡಿ ಶಾಸನದ ಸಮಯಕ್ಕಾಗಲೇ ಕನ್ನಡವು ಸಾಕಷ್ಟು ಅಭಿವೃದ್ಧಿ ಹೊಂದಿತ್ತು. ದ್ರಾವಿಡ ಭಾಷಾತಜ್ಞ ಸ್ಟಾನ್‍ಫೋರ್ಡ್ ಸ್ಟೀವರ್ ಅವರ ಅಭಿಪ್ರಾಯದಂತೆ, ಕನ್ನಡದ ಭಾಷಿಕ ಚರಿತ್ರೆಯನ್ನು ಮೂರು ವಿಧವಾಗಿ ವಿಂಗಡಿಸಬಹುದು",
  "ron": "Limba română este o limbă indo-europeană, din grupul italic şi din subgrupul oriental al limbilor romanice. Printre limbile romanice, româna este a cincea după numărul de vorbitori, în urma spaniolei, portughezei, francezei şi italienei. Din motive de diferenţiere tipologică, limba română mai este numită în lingvistica comparată limba dacoromână sau dialectul dacoromân.",
  "slv": "Slovenščina se je razvila iz praslovanščine. Najstarejši pisani viri, ki kažejo značilnosti slovenskega jezika, so Brižinski spomeniki. Napisani so z latinično pisavo, po izsledkih paleografske raziskave so nastali na Koroškem v obdobju 927–1039. Besedila, ki jih vsebujejo, so bila oblikovana že prej, verjetno v 8. stoletju.",
  "hrv": "Većinom su to bile tuđice, mnoge uobičajenije u srpskome književnome jeziku, a s njihovim olakim i nekritičnim preuzimanjem, što se također podudaralo s osobinama srpskoga književnoga jezika, hrvatski je bio potiskivan, a hrvatski jezični osjećaj prema tuđicama otupljen pa su tada vrata širom otvorena anglizmima. No srpska strana nije bila zadovoljna ni takvim stanjem, nego je nastojala da hrvatski i srpski književni jezik što više zbliže i da u tome hrvatski bude potpuno potisnut. S tom je namjerom uredništvo Letopisa Matice srpske raspisalo anketu o jezičnim i pravopisnim pitanjima i do rujna 1954. Letopis je objavio odgovore četrdesetak sudionika.",
  "srp": "Као и када су други језици у питању, неопходно је разграничити појам језичких система којим се Срби како етницитет служе од стандардног језика који се употребљава у државним и културним институцијама. Колико је званични (у случају српског језика, званични писани) језик једноставније дефинисати, захваљујући постојању норми у облику различитих граматика и правописа, толико је знатно сложеније дефинисати свакодневне језике који подлежу ненормираним међуљудским језичким односима",
  "mkd": "Македонистиката е наука која ги проучува развојот, правописот и другите карактеристики на македонскиот јазик. Почетоците на македонистиката се поврзани со политичките состојби на Балканскиот Полуостров во времето на османлиското владеење. Поради територијалните претензии на новосоздадените словенски држави Србија и Бугарија кон Македонија, кај нив се јавила потребата за докажување на културната поврзаност на населението на Македонија со она во нивните држави. Притоа македонистиката во најголем дел се развива како дел од политичките спорови околу припадноста на Македонците, а со тоа и припадноста на териториите коишто тие ги населуваат.",
  "lit": "Žodžio vieta sakinyje visiškai laisva, nes kalba sintetinė. Vis dėlto skirtingose situacijose ir įvairaus pobūdžio sakiniuose nusistovėjusi tam tikra vienokia ar kitokia žodžių tvarka (pvz., pažymimieji žodžiai dažniausiai eina po pažyminių). Visada galima inversija – žodžių sukeitimas vietomis, tačiau tuomet sakinys skamba neįprastai ir stilizuotai. Grožinėje literatūroje ir lyrikoje inversija vartojama dažnai, nes norima pabrėžti, paryškinti mintis, vaizdus ar nuotaikas.",
  "lav": "Lībiskais dialekts ir viens no trim latviešu valodas dialektiem. Lībiešu valodai bija lielāka ietekme uz latviešu valodas lībisko jeb tāmnieku dialekta substrātu, nekā uz pārējiem latviešu valodas dialektiem Latvijā. Kurzemē vārdu beigās tiek atmesti īsie patskaņi, bet garie patskaņi tiek saīsināti. Visos skaitļos un dzimtēs tiek izmantoti vienas formas darbības vārdi. Cilvēku vārdi abām dzimtēm tiek atvasināti ar galotnēm -els, -ans. Dialekts radies no līviem, kas asimilējoties sāka runāt latviešu valodā, iekļaujot tajā arī līvu valodas elementus.",
  "est": "Eesti keeles on kaks suuremat murderühma – põhjaeesti ja lõunaeesti murded (mõnedes käsitlustes eristatakse kolmanda rühmana kirderanniku murdeid). Nendevahelised erinevused ulatuvad arvatavasti läänemeresoome keelte ühisest algkeelest eraldumise perioodi. Murrete säilimist soodustas seotus majapidamisega, sellest tulenev vähene liikuvus ning tava võtta naine kas oma või lähedasest kihelkonnast. Seoses sunnismaisuse tekkega 14. – 15. sajandil vähenesid inimeste liikumis- ja suhtlemisvõimalused ning paikkondlikud keelekujud eristusid üldiselt kihelkonna piirides vastavate murrakutena.",
  "tam": "பக்தி இலக்கிய காலத்திலும், மையக் காலத்திலும் பெருமளவு வடமொழிச் சொற்கள் தமிழில் கலந்துவிட்டன. பிற்காலத்தில் பரிதிமாற் கலைஞர், மறைமலை அடிகள் முதலான தூய்மைவாதிகள் இவற்றைத் தமிழிலிருந்து நீக்க உழைத்தனர். இவ்வியக்கம் தனித்தமிழ் இயக்கம் என அழைக்கப்பட்டது. இதன் விளைவாக முறையான ஆவணங்களிலும், மேடைப் பேச்சுகளிலும், அறிவியல் எழுத்துக்களிலும் வடமொழிக் கலப்பில்லாத தமிழ் பயன்பட வழியேற்பட்டது. கி. பி. 800இற்கும் 1000இற்கும் இடைப்பட்ட காலப்பகுதியில், மலையாளம் ஒரு தனி மொழியாக உருவானதாக நம்பப்படுகின்றது.",
  "vie": "Với những cơ sở khoa học gần đây được đa số các nhà ngôn ngữ học thừa nhận, tiếng Việt thuộc hệ Nam Á ở khu vực Đông Nam Á hiện nay, có quan hệ gần gũi với tiếng Mường. Xa hơn là các thứ tiếng thuộc nhóm ngôn ngữ Môn-Khmer.",
  "urd": "عربی و فارسی الفاظ استعمال کرتی ہے۔ جبکہ ہندی زبان دیوناگری رسم الخط میں لکھی جاتی ہے اور سنسکرت الفاظ زیادہ استعمال کرتی ہے۔ کچھ ماہرینِ لسانیات اُردو اور ہندی کو ایک ہی زبان کی دو معیاری صورتیں گردانتے ہیں۔ تاہم، دیگر ماہرین اِن دونوں کو معاش اللسانی تفرّقات کی بنیاد پر الگ الگ سمجھتے ہیں۔ بلکہ حقیقت یہ ہے کہ ہندی، اُردو سے نکلی ہے۔ اسی طرح اگر اردو اور ہندی زبان کو ایک سمجھا جائے تو یہ دنیا کی چوتھی بڑی زبان ہے۔",
  "tha": "คำว่า ไทย หมายความว่า อิสรภาพ เสรีภาพ หรืออีกความหมายหนึ่งคือ ใหญ่ ยิ่งใหญ่ เพราะการจะเป็นอิสระได้จะต้องมีกำลังที่มากกว่า แข็งแกร่งกว่า เพื่อป้องกันการรุกรานจากข้าศึก คำนี้เป็นคำไทยแท้ที่เกิดจากการสร้างคำที่เรียก การลากคำเข้าวัด ซึ่งเป็นการลากความวิธีหนึ่ง ตามหลักคติชนวิทยา คนไทยเป็นชนชาติที่นับถือกันว่า ภาษาบาลี ซึ่งเป็นภาษาที่บันทึกพระธรรมคำสอนของพระพุทธเจ้าเป็นภาษาอันศักดิ์สิทธิ์และเป็นมงคล เมื่อคนไทยต้องการตั้งชื่อประเทศว่า ไท ซึ่งเป็นคำไทยแท้ จึงเติมตัว ย เข้าไปข้างท้าย เพื่อให้มีลักษณะคล้ายคำในภาษาบาลี - สันสกฤตเพื่อความเป็นมงคลตามความเชื่อของตน ภาษาไทยจึงหมายถึงภาษาของชนชาติไทยผู้เป็นไทนั่นเอง",
  "guj": "ભારત દેશના પશ્ચિમ ભાગમાં આવેલા, પહેલાંના જમાનાથી વેપાર ક્ષેત્રે આંતર રાષ્ટ્રીય મહત્વ ધરાવતા ગુજરાત રાજ્યમાં ઉદ્દભવેલી અને ગુજરાતીઓ દ્વારા બોલાતી ભાષાનું નામ છે, ગુજરાતી ભાષા. ગુજરાતી ભાષાને આંતર રાષ્ટ્રીય ફલક પર વર્ગીકરણ પ્રણાલીમાં ઇન્ડો-આર્યન ભાષા સમૂહમાં મૂકવામાં આવે છે. ગુજરાત અને ભારતનાં અન્ય રાજ્યો તથા પાકિસ્તાન ઉપરાંત વિશ્વનાં અનેક દેશોમાં ગુજરાતી ભાષા બોલતા લોકો વસે છે, જેમાં મહદ્અંશે, અમેરિકા, યુ.કે., કેન્યા તથા દક્ષિણ આફ્રિકા સહિત આફ્રિકાનાં અન્ય દેશો, કેનેડા, ઓસ્ટ્રેલિયા વગેરેનો સમાવેશ કરી શકાય. ભારતને આઝાદી મળ્યા બાદ ગુજરાત રાજ્યની સ્થાપના ૧ મે, ૧૯૬૦ના રોજ થઇ હતી અને ત્યારથી ગુજરાત રાજ્યની અધિકૃત ભાષા તરિકે ગુજરાતીને સ્વીકારવામાં આવી છે.",
  "uzb": "Tarixda oʻzbek tilini yozish uchun koʻp alifbolardan qoʻllanilgan. 1928-yilgacha savodli kishilar oʻzbek tilini arab yozuvida yozishgan. 1928-yildan 1940-yilgacha oʻzbek tili lotin yozuvida yozilgan. 1940-yil Iosif Stalinning buyrugʻi bilan majburan kirill yozuviga oʻtilgan. 1992-yilgacha oʻzbek tili shu yozuvda yozilgan. 1993-yil Oʻzbekiston rasman lotin yozuvini yana qaytadan kirgizdi. Hozirda Oʻzbekistonda taʼlim joylarida lotin yozuvidan qoʻllaniladi. Shunday boʻlsa ham yoshi kattalar va Oʻzbekiston tashqarisida yashaydigan oʻzbeklar hali ham kirill yozuvidan qoʻllanishadi.",
  "pan": "ਇਸ ਦੀਆਂ ਦੋ ਮੁੱਖ ਉਪ-ਬੋਲੀਆਂ ਹਨ- ਪੂਰਬੀ ਪੰਜਾਬੀ ਅਤੇ ਲਹਿੰਦੀ ਪੰਜਾਬੀ। ਲਹਿੰਦੀ ਪੰਜਾਬੀ, ਪੂਰਬੀ ਪੰਜਾਬੀ ਅਤੇ ਪੱਛਮੀ ਪਹਾੜੀ ਬੋਲੀਆਂ ਨੂੰ ਮਿਲਾ ਕੇ ਪੰਜਾਬੀ ਆਪਣੇ ਸੁਰ-ਵਿਗਿਆਨ ਕਰ ਕੇ ਅਜੋਕੀ ਹਿੰਦ-ਯੂਰਪੀ ਬੋਲੀਆਂ ਦੇ ਪਰਿਵਾਰ ਵਿੱਚੋਂ ਸਭ ਤੋਂ ਵੱਖਰੀ ਬੋਲੀ ਜਾਪਦੀ ਹੈ। ਪੰਜਾਬੀ ਦੀਆਂ ਕਈ ਉਪ-ਬੋਲੀਆਂ ਹਨ, ਪਰ ਮਾਝੀ ਨੂੰ ਸਭ ਤੋਂ ਅਮੀਰ ਉਪ-ਬੋਲੀ ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ। ਇਹ ਉਪ-ਬੋਲੀ ਪੁਰਾਣੇ ਪੰਜਾਬ ਦੇ ਮਾਝਾ ਖ਼ਿੱਤੇ ਵਿੱਚ ਬੋਲੀ ਜਾਂਦੀ ਹੈ ਜਿਸ ਦਾ ਕੇਂਦਰ ਅਜੋਕੇ ਅੰਮ੍ਰਿਤਸਰ ਅਤੇ ਲਹੌਰ ਵਿੱਚ ਹੈ। ਇਸ ਉਪ-ਬੋਲੀ ਦੀ ਵਰਤੋਂ ਪੰਜਾਬੀ ਦੀਆਂ ਕਿਤਾਬਾਂ ਲਿਖਣ ਵਿੱਚ ਹੁੰਦੀ ਹੈ।",
  "aze": "Eyni zamanda yazı dili də olan Azərbaycan dili yazı dili ənənəsinə sahib olma baxımından Türk dili ilə paraleldir/ Türkmən dili və qaqauz dilinin nisbətən daha gec yazı dili kimi formalaşmasına baxmayaraq Azərbaycan dili köklü bir yazı dili ənənəsinə malikdir.",
  "ind": "Fonologi dan tata bahasa Bahasa Indonesia dianggap relatif mudah.[8] Dasar-dasar yang penting untuk komunikasi dasar dapat dipelajari hanya dalam kurun waktu beberapa minggu.[9]",
  "tel": "ఆంధ్ర ప్రదేశ్ మరియు తెలంగాణ రాష్ట్రాల అధికార భాష తెలుగు. భారత దేశంలో తెలుగు మాతృభాషగా మాట్లాడే 8.7 కోట్ల (2001 ) జనాభాతో [1] ప్రాంతీయ భాషలలో మొదటి స్థానంలో ఉంది. ప్రపంచంలోని ప్రజలు అత్యధికముగా మాట్లాడే భాషలలో పదమూడవ స్థానములోనూ, భారత దేశములో హిందీ, బెంగాలీ తర్వాత మూడవ స్థానములోనూ నిలుస్తుంది. పాతవైన ప్రపంచ భాష గణాంకాల (ఎథ్నోలాగ్) ప్రకారం ప్రపంచవ్యాప్తంగా 7.4 కోట్లు మందికి మాతృభాషగా ఉంది.[2] మొదటి భాషగా మాట్లాడతారు. అతి ప్రాచీన దేశ భాషలలో సంస్కృతము తమిళముతో బాటు తెలుగు భాషను 2008 అక్టోబరు 31న భారత ప్రభుత్వము చేర్చింది.",
  "pes": "حدود استان امروزی فارس در جنوب ایران هستند. فارسی میانه به عنوان گویش رسمی در زمان ساسانیان در دیگر سرزمین‌های ایرانی گسترش زیادی یافت به طوری که در خراسان بزرگ جایگزین زبان‌های پارتی و بلخی شد و بخش‌های بزرگی از خوارزمی‌زبانان و سغدی‌زبانان نیز فارسی‌زبان شدند.[۱۱] گویشی از فارسی میانه که بعدها فارسی دری نام گرفت پس از اسلام به عنوان گویش استاندارد نوشتاری در خراسان شکل گرفت و این بار با گسترش به سوی غرب به ناحیه پارس و دیگر نقاط ایران بازگشت.",
  "mal": "ഇന്ത്യയിൽ‌ കേരള സംസ്ഥാനത്തിലും ലക്ഷദ്വീപിലും പുതുച്ചേരിയുടെ ഭാഗമായ മയ്യഴിയിലും സംസാരിക്കപ്പെടുന്ന ഭാഷയാണ് മലയാളം . ഇതു ദ്രാവിഡ ഭാഷാ കുടുംബത്തിൽപ്പെടുന്നു. ഇന്ത്യയിൽ ശ്രേഷ്ഠഭാഷാ പദവി ലഭിക്കുന്ന അഞ്ചാമത്തെ ഭാഷയാണ് മലയാളം[4].2013 മേയ് 23-നു ചേർന്ന കേന്ദ്രമന്ത്രിസഭായോഗമാണ് മലയാളത്തെ ശ്രേഷ്ഠഭാഷയായി അംഗീകരിച്ചത്",
  "ori": "ଓଡ଼ିଆ ଭାଷା ଭାଷା ଓଡ଼ିଶା ପାଖାପାଖି ଅନେକ ରାଜ୍ୟରେ କହାଯାଏ । ପଶ୍ଚିମ ବଙ୍ଗଳାର ମେଦିନୀପୁର ସମେତ ଆହୁରି ଅନେକ ଅଞ୍ଚଳ, ଝାଡ଼ଖଣ୍ଡର ସିଂହଭୂମି ଜିଲ୍ଲା, ଆନ୍ଧ୍ର ପ୍ରଦେଶର ଶ୍ରୀକାକୁଲମ, ବିଜୟନଗର ଓ ବିଶାଖାପଟନମ ଜିଲ୍ଲା, ଛତିଶଗଡ଼ର ପୂର୍ବ ଜିଲ୍ଲାମାନଙ୍କରେ ବହୁଳ ଭାବରେ କୁହା ଯାଏ । ଗୁଜରାଟର ସୁରଟ ଭାରତର ଦ୍ଵିତୀୟ ଓଡ଼ିଆ ଭାଷା ବହୁଳ ଅଞ୍ଚଳ । ଏହାଛଡା ବେଙ୍ଗାଳୁରୁ, ହାଇଦ୍ରାବାଦ, ପଣ୍ଡିଚେରୀ, ଚେନ୍ନାଇ, ଗୋଆ, ମୁମ୍ବାଇ, ଜାମସେଦପୁର, ବରୋଦା, ରାୟପୁର, ଅହମଦାବାଦ, ଦିଲ୍ଲୀ, କଲିକତା, ଖଡ଼ଗପୁର, ଗୁଆହାଟୀ, ପୁନେ ଓ ସିଲଭାସା ଆଦି ସହରରେ ଓଡ଼ିଆ ଭାଷାଭାଷୀ ଲୋକ ଦେଖାଯାନ୍ତି",
  "mya": "လူများတွင် ဇီကာအဖျားရောဂါ အမည်ရှိ မပြင်းထန်သည့် အဖျားရောဂါကို ဖြစ်ပွားစေသည်။ ၁၉၅၀ ခုနှစ်များဝန်းကျင်တွင် အာဖရိကနှင့် အာရှအကြား အီကွေတာ ခါးပတ်အနီးတဝိုက်တွင် စတင်ဖြစ်ပွားခဲ့သည်။ ၂၀၁၄ ခုနှစ်တွင် ဗိုင်းရပ်စ်သည် ပစိဖိတ်သမုဒ္ဒရာကို ဖြတ်ပြီး ပြင်သစ်ပိုလီနီးရှားနှင့် အီစတာကျွန်းသို့ လည်းကောင်း၊ ၂၀၁၅ တွင် မက္ကဆီကို၊ ဗဟိုအမေရိက၊ ကာရစ်ဘီယံနှင့် တောင်အာဖရိကသို့ ကူးစက်ပြန့်ပွားလာကာ ကမ္ဘာအနှံ့တွင် ဖြစ်ပွားသည့် ကပ်ရောဂါအသွင် ဆောင်လာနေသည်။",
  "nep": "नेपाली भाषा एक अन्तर्राष्ट्रिय भाषा हो। दक्षिण एसियाका दुई प्रमुख देश नेपाल र भारतमा राष्ट्रिय भाषाको रूपमा स्वीकृत एवं स-साना प्रदेशलगायत राज्यहरूमा माध्यम भाषाको स्तरमा सङ्गठित नेपाली भाषा एक जीवन्त भाषा हो। नेपाली भाषा खस, पर्वते, सिञ्जाली तथा गोरखा भाषा नामले पनि चिनिदै आएको छ। भाषाको प्रकृतिअनुसार कुनै पनि भाषाले विकास गर्दा जटिलतादेखि सरलता र स्थुलताबाट सूक्ष्मतातिर उन्मुख हुने प्रक्रिया ग्रहण गर्दछ। भाषाले सुष्ठता प्राप्त गर्दा आफ्नो सांस्कृतिक सञ्चारण र अभिव्यक्ति संस्कारलाई जरैबाट समातेर राख्दछ। यसैले नेपाली भाषालाई पनि एक विशाल वटवृक्ष भन्दा अत्युक्ति नहोला। सांस्कृतिक र संस्कारगत चरित्रको आधारमा नेपाली भाषाले विविधतालाई स्वीकार गरेको छ। नेपालदेखि फैलिएको यो भाषा पूर्वमा बर्मा, पश्चिममा पञ्जावसम्म, उत्तरमा हिमवत्खण्डदेखि दक्षिण एसियाको गाङ्गेय समभूमि तथा अन्य भाषा-परिवार क्षेत्रतिर पनि यसले विस्तार पाएको छ।",
  "sin": "ශ්‍රී ලංකාවේ ප්‍රධාන ජාතිය වන සිංහල ජනයාගේ මව් බස සිංහල වෙයි. අද වන විට මිලියන 20 කට අධික සිංහල සහ මිලියන 3කට අධික සිංහල නොවන ජනගහනයක් සිංහල භාෂාව භාවිත කරති. සිංහල‍ ඉන්දු-යුරෝපීය භාෂාවල උප ගණයක් වන ඉන්දු-ආර්ය භාෂා ගණයට අයිති වන අතර මාල දිවයින භාවිත කරන දිවෙහි භාෂාව  සිංහලයෙන් පැවත එන්නකි. සිංහල ශ්රී ලංකාවේ නිල භාෂාවයි .",
  "khm": "ភាសាខ្មែរ ឬខេមរភាសា គឺជាភាសារបស់ ប្រជាជាតិខ្មែរ។ ភាសាសំស្ក្រឹត និងភាសាបាលីបាន​ជួយបង្កើតខេមរភាសា ព្រោះភាសាខ្មែរបានខ្ចីពាក្យច្រើនពីភាសាអស់នោះ។​ភាសាខ្មែរមានអក្សរក្រមវែងជាងគេនៅលើពិភពលោក។​ វាជាភាសាមួយដ៏ចំណាស់​ ដែលប្រហែលជាមានដើមកំណើតតាំងតែពី​ ២០០០ឆ្នាំមុនមកម៉្លេះ។ ភាសាខ្មែរមានអនុភាពលើភាសាថៃ និងភាសាឡាវ។​ភាសាពីរនេះបានខ្ចីពាក្យច្រើនណាស់ពីភាសាខ្មែរដែលនាំឲ្យពួកអឺរ៉ុបស្មានថាវានៅក្នុងក្រុមភាសាដូចគ្នា។ ភាសានោះគឺជារបស់ក្រុមភាសាថៃក្រាដៃនិងភាសាខ្មែរនៅក្រុមភាសាមនខ្មែរជាមួយភាសាមន និងភាសាវៀតណាម ដែលទាក់ទងភាសាសំស្ក្រឹត។",
  "tuk": "Türkmeniň häzirki ulanylýan edebi diliniň döreýşi köp kişi tarapyndan Magtymgulynyň şygryýeti bilen baglanyşdyrylýar. Magtymguly ilkinjileriň hatarynda halkyň ulanýan dilini öz çylşyrymly dini-pelsepi-sosial temalarda ýazylan şygyrlaryna sygdyrmagy başarypdyr. Şol bir wagtyň özünde gündelik türkmen durmuşynyň meselelerine hem örän ýiti çemeleşmegiň hötdesinden gelendigi üçin türkmenleriň we beýleki Merkezi Aziýa halklarynyň arasynda aýratyn hormatdan peýdalanýar.",
  "aka": "Akan yɛ din a wɔde frɛ kasa ahorow a Akan ebusua no nyina ka. Akanfo taa de din soronko to sɛdea wɔkasa wɔ wɔn mbrɔn pii no mu. Akuapemfo frɛ wɔn kasae no Akuapem Twi. Kumasifo so frɛ wɔn kasae Asante Twi. Dɛmara so na Mfantefo frɛ wɔn kasae Fante. Akanfo a wɔte Bono afa mu so frɛ wɔn kasae no Bono.",
  "zul": "Lolu limi lusukela noma lwaqanjwa ngowayeyiSilo samabandla onke iNkosi uShaka Zulu. Lokhu kungenxa yegalelo noma iqhaza alibamba ekubumbeni isizwe esasihlukene phambilini. Ezinye zezilimi ezisukela olimini lwesiZulu singabala IsiXhosa, Isindebele kanye nesiSwati. Lezi zilimi zonke isiSwati, isiZulu, isiNdebele nesiXhosa, ziyizilimi zesiNguni. Isifunda sakwaBulawayo esise Zimbabwe naso singesinye sezifunda ezisebenzisa lolu limi lwesiZulu.",
  "sna": "ChiShona mutauro unobatanidza ndimi dzakawanda dzinotaurwa muZimbabwe, Botswana neMozambique. Mitauro inobatanidzwa ichinzi ChiShona inosanganisira: Karanga, Manyika, Zezuru, Korekore, Ndau, Budya nemimwewo. Zvakadaro zvakafanira kuti tionesane kuti kune vamwe vatauri vasingafare kuti vanzi vari muboka remutauro weChiShona - ivava vanoona mitauro yavo semitauro yakazvimirira yoga isiri pasi peChiShona.",
  "afr": "Afrikaans is 'n Indo-Europese taal wat aan die Wes-Germaanse tak van die Germaanse tale behoort. Afrikaans behoort saam met Nederlands aan die Nederfrankiese taalgroep wat van Oudnederlands afstam. Nederfrankiese verskeidenhede word in Europa in Nederland, die noorde van België, Frans-Vlaandere in Frankryk en die Duitse gebied langs die Ryn tussen Keulen en die grens tussen Duitsland en Nederland gepraat. Buite Europa word Nederfrankiese verskeidenhede in Suid-Afrika, Namibië, Suriname en die Nederlandse eilande in die Karibiese See gepraat.",
  "lat": "Credo ego vos, iudices, mirari, quid sit, quod, cum tot summi oratores hominesque nobilissimi sedeant, ego potissimum surrexerim, is, qui neque aetate neque ingenio neque auctoritate sim cum his, qui sedeant, comparandus. Omnes hi, quos videtis adesse in hac causa, iniuriam novo scelere conflatam putant oportere defendi, defendere ipsi propter iniquitatem temporum non audent. Ita fit, ut adsint propterea, quod officium sequuntur, taceant autem idcirco, quia periculum vitant.",
  "slk": "Kodifikačné príručky určujú, ktoré slová sa v slovenčine považujú za spisovné. Ide o 4 zákonom predpísané knihy.",
  "cat": "Aquest és l’honor més gran que he rebut a la meva vida. La pau ha estat sempre la meva més gran preocupació. Ja en la meva infantesa vaig aprendre a estimar-la. La meva mare – una dona excepcional, genial - , quan jo era noi, ja em parlava de la pau, perquè en aquells temps també hi havia moltes guerres. A més, sóc català. Catalunya va tenir el primer Parlament democràtic molt abans que Anglaterra. I fou al meu país on hi hagué les primeres nacions unides. En aquell temps – segle onzè – van reunir-se a Toluges – avui França – per parlar de la pau, perquè els catalans d’aquell temps ja estaven contra, CONTRA la guerra. Per això les Nacions Unides, que treballen únicament per l’ideal de la pau, estan en el meu cor, perquè tot allò referent a la pau hi va directament. (...) Fa molts anys que no toco el violoncel en públic, però crec que he de fer-ho en aquesta ocasió. Vaig a tocar una melodia del folklore català: El cant dels ocells. Els ocells, quan són al cel, van cantant: 'Peace, Peace, Peace' (pau, pau, pau) i és una melodia que Bach, Beethoven i tots els grans haurien admirat i estimat. I, a més, neix de l’ànima del meu poble, Catalunya.",
  "tgl": "Sapagkat ang pagkilala sa katutubong karangalan at sa pantay at di-maikakait na mga karapatan ng lahat ng nabibilang sa angkan ng tao ay siyang saligan ng kalayaan, katarungan at kapayapaan sa daigdig. Sapagkat ang pagwawalang-bahala at paglalapastangan sa mga karapatan ng tao ay nagbunga ng mga gawang di-makatao na humamak sa budhi ng sangkatauhan, at ang pagdatal ng isang daigdig na ang mga tao ay magtatamasa ng kalayaan sa pagsasalita at ng kaligtasan sa pangamba at pagdaralita ay ipinahayag na pinakamataas na mithiin ng mga karaniwang tao. Sapagkat mahalaga, kung ang tao ay di-pipiliting manghawakan bilang huling magagawa, sa paghihimagsik laban sa paniniil at pang-aapi, na ang mga karapatan ng tao'y mapangalagaan sa pamamagitan ng paghahari ng batas. Sapagkat mahalagang itaguyod ang pagpapaunlad ng mabuting pagsasamahan ng mga bansa. Sapagkat ang mga mamamayan ng Mga Bansang Nagkakaisa ay nagpatibay sa Karta ng kanilang pananalig sa mga Saligang karapatan ng tao, sa karangalan at ",
  "hye": "Հայոց լեզվով ստեղծվել"
}
```

## File: `tests/fuzzing.rs`
```rust
#[cfg(feature = "arbitrary")]
#[test]
fn test_fuzzing() {
    use ::arbitrary::{Arbitrary, Unstructured};
    use whatlang::Detector;

    fn prop(u: &mut Unstructured) -> ::arbitrary::Result<()> {
        let detector = Detector::arbitrary(u)?;
        let input = String::arbitrary(u)?;
        detector.detect(&input);
        Ok(())
    }

    arbtest::builder().run(prop)
}
```

