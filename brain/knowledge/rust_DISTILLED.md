---
id: rust
type: knowledge
owner: OA_Triage
---
# rust
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
An experimental library that provides some common statistical functions with
some support for computing them efficiently on *streams* of data. The intent
is to permit parallel computation of statistics on large data sets.

[![Build status](https://api.travis-ci.org/BurntSushi/rust-stats.png)](https://travis-ci.org/BurntSushi/rust-stats)
[![](http://meritbadge.herokuapp.com/streaming-stats)](https://crates.io/crates/streaming-stats)

Dual-licensed under MIT or the [UNLICENSE](http://unlicense.org).


### Documentation

Some documentation exists here:
[https://docs.rs/streaming-stats](https://docs.rs/streaming-stats).


### Installation

Simply add `streaming-stats` as a dependency to your project's `Cargo.toml`:

```toml
[dependencies]
streaming-stats = "0.2"
```

```

### File: ISSUE_TEMPLATE.md
```md
Thank you for taking the time to file a bug report. The following describes
some guidelines to creating a minimally useful ticket.

Above all else: do not describe your problem, **SHOW** your problem.

#### What version of the `csv` crate are you using?

Replace this text with the version. (The version can be found in your
Cargo.lock.)

#### Briefly describe the question, bug or feature request.

Replace this text with a description.

#### Include a complete program demonstrating a problem.

Whether you're asking for a feature, filing a bug or just asking a question,
this section should almost always include some kind of code that you have
written. The code provided should be able to be compiled by others and should
be as feasibly small as possible.

If you're reporting a bug, then the code should exhibit some undesirable
characteristic.

If you're asking a question, then the code should represent what you've tried
so far.

If you're requesting a feature, then provide code that does the closest
possible thing to what you're requesting, if possible.

#### What is the observed behavior of the code above?

Replace this text with the output of the program.

#### What is the expected or desired behavior of the code above?

Replace this text with the expected or desired output of the program.

```

### File: benches\bench.rs
```rs
#![feature(test)]

extern crate test;

use std::io;

use serde::{de::DeserializeOwned, Deserialize, Serialize};
use test::Bencher;

use csv::{
    ByteRecord, Reader, ReaderBuilder, StringRecord, Trim, Writer,
    WriterBuilder,
};

static NFL: &str = include_str!("../examples/data/bench/nfl.csv");
static GAME: &str = include_str!("../examples/data/bench/game.csv");
static POP: &str = include_str!("../examples/data/bench/worldcitiespop.csv");
static MBTA: &str =
    include_str!("../examples/data/bench/gtfs-mbta-stop-times.csv");

#[derive(Debug, Serialize, Deserialize, PartialEq)]
struct NFLRowOwned {
    gameid: String,
    qtr: i32,
    min: Option<i32>,
    sec: Option<i32>,
    off: String,
    def: String,
    down: Option<i32>,
    togo: Option<i32>,
    ydline: Option<i32>,
    description: String,
    offscore: i32,
    defscore: i32,
    season: i32,
}

#[derive(Debug, Serialize, Deserialize, PartialEq)]
struct NFLRowBorrowed<'a> {
    gameid: &'a str,
    qtr: i32,
    min: Option<i32>,
    sec: Option<i32>,
    off: &'a str,
    def: &'a str,
    down: Option<i32>,
    togo: Option<i32>,
    ydline: Option<i32>,
    description: &'a str,
    offscore: i32,
    defscore: i32,
    season: i32,
}

#[derive(Debug, Serialize, Deserialize, PartialEq)]
struct GAMERowOwned(String, String, String, String, i32, String);

#[derive(Debug, Serialize, Deserialize, PartialEq)]
struct GAMERowBorrowed<'a>(&'a str, &'a str, &'a str, &'a str, i32, &'a str);

#[derive(Debug, Serialize, Deserialize, PartialEq)]
#[serde(rename_all = "PascalCase")]
struct POPRowOwned {
    country: String,
    city: String,
    accent_city: String,
    region: String,
    population: Option<i32>,
    latitude: f64,
    longitude: f64,
}

#[derive(Debug, Serialize, Deserialize, PartialEq)]
#[serde(rename_all = "PascalCase")]
struct POPRowBorrowed<'a> {
    country: &'a str,
    city: &'a str,
    accent_city: &'a str,
    region: &'a str,
    population: Option<i32>,
    latitude: f64,
    longitude: f64,
}

#[derive(Debug, Serialize, Deserialize, PartialEq)]
struct MBTARowOwned {
    trip_id: String,
    arrival_time: String,
    departure_time: String,
    stop_id: String,
    stop_sequence: i32,
    stop_headsign: String,
    pickup_type: i32,
    drop_off_type: i32,
    timepoint: i32,
}

#[derive(Debug, Serialize, Deserialize, PartialEq)]
struct MBTARowBorrowed<'a> {
    trip_id: &'a str,
    arrival_time: &'a str,
    departure_time: &'a str,
    stop_id: &'a str,
    stop_sequence: i32,
    stop_headsign: &'a str,
    pickup_type: i32,
    drop_off_type: i32,
    timepoint: i32,
}

#[derive(Default)]
struct ByteCounter {
    count: usize,
}
impl io::Write for ByteCounter {
    fn write(&mut self, data: &[u8]) -> io::Result<usize> {
        self.count += data.len();
        Ok(data.len())
    }
    fn flush(&mut self) -> io::Result<()> {
        Ok(())
    }
}

macro_rules! bench {
    ($name:ident, $data:ident, $counter:ident, $result:expr) => {
        #[bench]
        fn $name(b: &mut Bencher) {
            let data = $data.as_bytes();
            b.bytes = data.len() as u64;
            b.iter(|| {
                let mut rdr =
                    ReaderBuilder::new().has_headers(false).from_reader(data);
                assert_eq!($counter(&mut rdr), $result);
            })
        }
    };
}

macro_rules! bench_trimmed {
    ($name:ident, $data:ident, $counter:ident, $result:expr) => {
        #[bench]
        fn $name(b: &mut Bencher) {
            let data = $data.as_bytes();
            b.bytes = data.len() as u64;
            b.iter(|| {
                let mut rdr = ReaderBuilder::new()
                    .has_headers(false)
                    .trim(Trim::All)
                    .from_reader(data);
                assert_eq!($counter(&mut rdr), $result);
            })
        }
    };
}

macro_rules! bench_serde {
    (no_headers,
     $name_de:ident, $name_ser:ident, $data:ident, $counter:ident, $type:ty, $result:expr) => {
        #[bench]
        fn $name_de(b: &mut Bencher) {
            let data = $data.as_bytes();
            b.bytes = data.len() as u64;
            b.iter(|| {
                let mut rdr =
                    ReaderBuilder::new().has_headers(false).from_reader(data);
                assert_eq!($counter::<_, $type>(&mut rdr), $result);
            })
        }
        #[bench]
        fn $name_ser(b: &mut Bencher) {
            let data = $data.as_bytes();
            let values = ReaderBuilder::new()
                .has_headers(false)
                .from_reader(data)
                .deserialize()
                .collect::<Result<Vec<$type>, _>>()
                .unwrap();

            let do_it = || {
                let mut counter = ByteCounter::default();
                {
                    let mut wtr = WriterBuilder::new()
                        .has_headers(false)
                        .from_writer(&mut counter);
                    for val in &values {
                        wtr.serialize(val).unwrap();
                    }
                }
                counter.count
            };
            b.bytes = do_it() as u64;
            b.iter(do_it)
        }
    };
    ($name_de:ident, $name_ser:ident, $data:ident, $counter:ident, $type:ty, $result:expr) => {
        #[bench]
        fn $name_de(b: &mut Bencher) {
            let data = $data.as_bytes();
            b.bytes = data.len() as u64;
            b.iter(|| {
                let mut rdr =
                    ReaderBuilder::new().has_headers(true).from_reader(data);
                assert_eq!($counter::<_, $type>(&mut rdr), $result);
            })
        }
        #[bench]
        fn $name_ser(b: &mut Bencher) {
            let data = $data.as_bytes();
            let values = ReaderBuilder::new()
                .has_headers(true)
                .from_reader(data)
                .deserialize()
                .collect::<Result<Vec<$type>, _>>()
                .unwrap();

            let do_it = || {
                let mut counter = ByteCounter::default();
                {
                    let mut wtr = WriterBuilder::new()
                        .has_headers(true)
                        .from_writer(&mut counter);
                    for val in &values {
                        wtr.serialize(val).unwrap();
                    }
                }
                counter.count
            };
            b.bytes = do_it() as u64;
            b.iter(do_it)
        }
    };
}

macro_rules! bench_serde_borrowed_bytes {
    ($name:ident, $data:ident, $type:ty, $headers:expr, $result:expr) => {
        #[bench]
        fn $name(b: &mut Bencher) {
            let data = $data.as_bytes();
            b.bytes = data.len() as u64;
            b.iter(|| {
                let mut rdr = ReaderBuilder::new()
                    .has_headers($headers)
                    .from_reader(data);
                let mut count = 0;
                let mut rec = ByteRecord::new();
                while rdr.read_byte_record(&mut rec).unwrap() {
                    let _: $type = rec.deserialize(None).unwrap();
                    count += 1;
                }
                count
            })
        }
    };
}

macro_rules! bench_serde_borrowed_str {
    ($name:ident, $data:ident, $type:ty, $headers:expr, $result:expr) => {
        #[bench]
        fn $name(b: &mut Bencher) {
            let data = $data.as_bytes();
            b.bytes = data.len() as u64;
            b.iter(|| {
                let mut rdr = ReaderBuilder::new()
                    .has_headers($headers)
                    .from_reader(data);
                let mut count = 0;
                let mut rec = StringRecord::new();
                while rdr.read_record(&mut rec).unwrap() {
                    let _: $type = rec.deserialize(None).unwrap();
                    count += 1;
                }
                count
            })
        }
    };
}

bench_serde!(
    count_nfl_deserialize_owned_bytes,
    count_nfl_serialize_owned_bytes,
    NFL,
    count_deserialize_owned_bytes,
    NFLRowOwned,
    9999
);
bench_serde!(
    count_nfl_deserialize_owned_str,
    count_nfl_serialize_owned_str,
    NFL,
    count_deserialize_owned_str,
    NFLRowOwned,
    9999
);
bench_serde_borrowed_bytes!(
    count_nfl_deserialize_borrowed_bytes,
    NFL,
    NFLRowBorrowed,
    true,
    9999
);
bench_serde_borrowed_str!(
    count_nfl_deserialize_borrowed_str,
    NFL,
    NFLRowBorrowed,
    true,
    9999
);
bench!(count_nfl_iter_bytes, NFL, count_iter_bytes, 130000);
bench_trimmed!(count_nfl_iter_bytes_trimmed, NFL, count_iter_bytes, 130000);
bench!(count_nfl_iter_str, NFL, count_iter_str, 130000);
bench_trimmed!(count_nfl_iter_str_trimmed, NFL, count_iter_str, 130000);
bench!(count_nfl_read_bytes, NFL, count_read_bytes, 130000);
bench!(count_nfl_read_str, NFL, count_read_str, 130000);
bench_serde!(
    no_headers,
    count_game_deserialize_owned_bytes,
    count_game_serialize_owned_bytes,
    GAME,
    count_deserialize_owned_bytes,
    GAMERowOwned,
    100000
);
bench_serde!(
    no_headers,
    count_game_deserialize_owned_str,
    count_game_serialize_owned_str,
    GAME,
    count_deserialize_owned_str,
    GAMERowOwned,
    100000
);
bench_serde_borrowed_bytes!(
    count_game_deserialize_borrowed_bytes,
    GAME,
    GAMERowBorrowed,
    true,
    100000
);
bench_serde_borrowed_str!(
    count_game_deserialize_borrowed_str,
    GAME,
    GAMERowBorrowed,
    true,
    100000
);
bench!(count_game_iter_bytes, GAME, count_iter_bytes, 600000);
bench!(count_game_iter_str, GAME, count_iter_str, 600000);
bench!(count_game_read_bytes, GAME, count_read_bytes, 600000);
bench!(count_game_read_str, GAME, count_read_str, 600000);
bench_serde!(
    count_pop_deserialize_owned_bytes,
    count_pop_serialize_owned_bytes,
    POP,
    count_deserialize_owned_bytes,
    POPRowOwned,
    20000
);
bench_serde!(
    count_pop_deserialize_owned_str,
    count_pop_serialize_owned_str,
    POP,
    count_deserialize_owned_str,
    POPRowOwned,
    20000
);
bench_serde_borrowed_bytes!(
    count_pop_deserialize_borrowed_bytes,
    POP,
    POPRowBorrowed,
    true,
    20000
);
bench_serde_borrowed_str!(
    count_pop_deserialize_borrowed_str,
    POP,
    POPRowBorrowed,
    true,
    20000
);
bench!(count_pop_iter_bytes, POP, count_iter_bytes, 140007);
bench!(count_pop_iter_str, POP, count_iter_str, 140007);
bench!(count_pop_read_bytes, POP, count_read_bytes, 140007);
bench!(count_pop_read_str, POP, count_read_str, 140007);
bench_serde!(
    count_mbta_deserialize_owned_bytes,
    count_mbta_serialize_owned_bytes,
    MBTA,
    count_deserialize_owned_bytes,
    MBTARowOwned,
    9999
);
bench_serde!(
    count_mbta_deserialize_owned_str,
    count_mbta_serialize_owned_str,
    MBTA,
    count_deserialize_owned_str,
    MBTARowOwned,
    9999
);
bench_serde_borrowed_bytes!(
    count_mbta_deserialize_borrowed_bytes,
    MBTA,
    MBTARowBorrowed,
    true,
    9999
);
bench_serde_borrowed_str!(
    count_mbta_deserialize_borrowed_str,
    MBTA,
    MBTARowBorrowed,
    true,
    9999
);
bench!(count_mbta_iter_bytes, MBTA, count_iter_bytes, 90000);
bench!(count_mbta_iter_str, MBTA, count_iter_str, 90000);
bench!(count_mbta_read_bytes, MBTA, count_read_bytes, 90000);
bench!(count_mbta_read_str, MBTA, count_read_str, 90000);

macro_rules! bench_write {
    ($name:ident, $data:ident) => {
        #[bench]
        fn $name(b: &mut Bencher) {
            let data = $data.as_bytes();
            b.bytes = data.len() as u64;
            let records = collect_records(data);

            b.iter(|| {
                let mut wtr = Writer::from_writer(vec![]);
                for r in &records {
                    wtr.write_record(r).unwrap();
                }
                assert!(wtr.flush().is_ok());
            })
        }
    };
}

macro_rules! bench_write_bytes {
    ($name:ident, $data:ident) => {
        #[bench]
        fn $name(b: &mut Bencher) {
            let data = $data.as_bytes();
            b.bytes = data.len() as u64;
            let records = collect_records(data);

            b.iter(|| {
                let mut wtr = Writer::from_writer(vec![]);
                for r in &records {
                    wtr.write_byte_record(r).unwrap();
                }
                assert!(wtr.flush().is_ok());
            })
        }
    };
}

bench_write!(write_nfl_record, NFL);
bench_write_bytes!(write_nfl_bytes, NFL);

fn count_deserialize_owned_bytes<R, D>(rdr: &mut Reader<R>) -> u64
where
    R: io::Read,
    D: DeserializeOwned,
{
    let mut count = 0;
    let mut rec = ByteRecord::new();
    while rdr.read_byte_record(&mut rec).unwrap() {
        let _: D = rec.deserialize(None).unwrap();
        count += 1;
    }
    count
}

fn count_deserialize_owned_str<R, D>(rdr: &mut Reader<R>) -> u64
where
    R: io::Read,
    D: DeserializeOwned,
{
    let mut count = 0;
    for rec in rdr.deserialize::<D>() {
        let _ = rec.unwrap();
        count += 1;
    }
    count
}

fn count_iter_bytes<R: io::Read>(rdr: &mut Reader<R>) -> u64 {
    let mut count = 0;
    for rec in rdr.byte_records() {
        count += rec.unwrap().len() as u64;
    }
    count
}

fn count_iter_str<R: io::Read>(rdr: &mut Reader<R>) -> u64 {
    let mut count = 0;
    for rec in rdr.records() {
        count += rec.unwrap().len() as u64;
    }
    count
}

fn count_read_bytes<R: io::Read>(rdr: &mut Reader<R>) -> u64 {
    let mut count = 0;
    let mut rec = ByteRecord::new();
    while rdr.read_byte_record(&mut rec).unwrap() {
        count += rec.len() as u64;
    }
    count
}

fn count_read_str<R: io::Read>(rdr: &mut Reader<R>) -> u64 {
    let mut count = 0;
    let mut rec = StringRecord::new();
    while rdr.read_record(&mut rec).unwrap() {
        count += rec.len() as u64;
    }
    count
}

fn collect_records(data: &[u8]) -> Vec<ByteRecord> {
    let mut rdr = ReaderBuilder::new().has_headers(false).from_reader(data);
    rdr.byte_records().collect::<Result<Vec<_>, _>>().unwrap()
}

```

### File: ci\script.sh
```sh
#!/bin/sh

set -ex

cargo build --verbose
cargo doc --verbose

# Our dev dependencies want newer versions of Rust. Instead of bumping our
# MSRV, we just don't test on our MSRV.
if [ "$TRAVIS_RUST_VERSION" = "1.33.0" ]; then
  exit 0
fi

cargo test --verbose
cargo test --verbose --manifest-path csv-core/Cargo.toml
cargo test --verbose --manifest-path csv-index/Cargo.toml
if [ "$TRAVIS_RUST_VERSION" = "stable" ]; then
  rustup component add rustfmt
  cargo fmt -- --check

  ci/check-copy cookbook
  ci/check-copy tutorial
fi
if [ "$TRAVIS_RUST_VERSION" = "nightly" ]; then
  cargo bench --verbose --no-run
fi

```

### File: examples\cookbook-read-basic.rs
```rs
use std::{error::Error, io, process};

fn example() -> Result<(), Box<dyn Error>> {
    // Build the CSV reader and iterate over each record.
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.records() {
        // The iterator yields Result<StringRecord, Error>, so we check the
        // error here..
        let record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(err) = example() {
        println!("error running example: {}", err);
        process::exit(1);
    }
}

```

### File: examples\cookbook-read-colon.rs
```rs
use std::{error::Error, io, process};

fn example() -> Result<(), Box<dyn Error>> {
    let mut rdr =
        csv::ReaderBuilder::new().delimiter(b':').from_reader(io::stdin());
    for result in rdr.records() {
        let record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(err) = example() {
        println!("error running example: {}", err);
        process::exit(1);
    }
}

```

### File: examples\cookbook-read-no-headers.rs
```rs
use std::{error::Error, io, process};

fn example() -> Result<(), Box<dyn Error>> {
    let mut rdr =
        csv::ReaderBuilder::new().has_headers(false).from_reader(io::stdin());
    for result in rdr.records() {
        let record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(err) = example() {
        println!("error running example: {}", err);
        process::exit(1);
    }
}

```

### File: examples\cookbook-read-serde.rs
```rs
#![allow(dead_code)]
use std::{error::Error, io, process};

use serde::Deserialize;

// By default, struct field names are deserialized based on the position of
// a corresponding field in the CSV data's header record.
#[derive(Debug, Deserialize)]
struct Record {
    city: String,
    region: String,
    country: String,
    population: Option<u64>,
}

fn example() -> Result<(), Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.deserialize() {
        // Notice that we need to provide a type hint for automatic
        // deserialization.
        let record: Record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(err) = example() {
        println!("error running example: {}", err);
        process::exit(1);
    }
}

```

### File: examples\cookbook-write-basic.rs
```rs
use std::{error::Error, io, process};

fn example() -> Result<(), Box<dyn Error>> {
    let mut wtr = csv::Writer::from_writer(io::stdout());

    // When writing records without Serde, the header record is written just
    // like any other record.
    wtr.write_record(["city", "region", "country", "population"])?;
    wtr.write_record(["Southborough", "MA", "United States", "9686"])?;
    wtr.write_record(["Northbridge", "MA", "United States", "14061"])?;
    wtr.flush()?;
    Ok(())
}

fn main() {
    if let Err(err) = example() {
        println!("error running example: {}", err);
        process::exit(1);
    }
}

```

### File: examples\cookbook-write-serde.rs
```rs
use std::{error::Error, io, process};

use serde::Serialize;

#[derive(Debug, Serialize)]
struct Record {
    city: String,
    region: String,
    country: String,
    population: Option<u64>,
}

fn example() -> Result<(), Box<dyn Error>> {
    let mut wtr = csv::Writer::from_writer(io::stdout());

    // When writing records with Serde using structs, the header row is written
    // automatically.
    wtr.serialize(Record {
        city: "Southborough".to_string(),
        region: "MA".to_string(),
        country: "United States".to_string(),
        population: Some(9686),
    })?;
    wtr.serialize(Record {
        city: "Northbridge".to_string(),
        region: "MA".to_string(),
        country: "United States".to_string(),
        population: Some(14061),
    })?;
    wtr.flush()?;
    Ok(())
}

fn main() {
    if let Err(err) = example() {
        println!("error running example: {}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-error-01.rs
```rs
use std::io;

fn main() {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.records() {
        let record = result.expect("a CSV record");
        println!("{:?}", record);
    }
}

```

### File: examples\tutorial-error-02.rs
```rs
use std::{io, process};

fn main() {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.records() {
        // Examine our Result.
        // If there was no problem, print the record.
        // Otherwise, print the error message and quit the program.
        match result {
            Ok(record) => println!("{:?}", record),
            Err(err) => {
                println!("error reading CSV from <stdin>: {}", err);
                process::exit(1);
            }
        }
    }
}

```

### File: examples\tutorial-error-03.rs
```rs
use std::{error::Error, io, process};

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

fn run() -> Result<(), Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.records() {
        // Examine our Result.
        // If there was no problem, print the record.
        // Otherwise, convert our error to a Box<dyn Error> and return it.
        match result {
            Err(err) => return Err(From::from(err)),
            Ok(record) => {
                println!("{:?}", record);
            }
        }
    }
    Ok(())
}

```

### File: examples\tutorial-error-04.rs
```rs
use std::{error::Error, io, process};

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

fn run() -> Result<(), Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.records() {
        // This is effectively the same code as our `match` in the
        // previous example. In other words, `?` is syntactic sugar.
        let record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

```

### File: examples\tutorial-perf-alloc-01.rs
```rs
use std::{error::Error, io, process};

fn run() -> Result<u64, Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());

    let mut count = 0;
    for result in rdr.records() {
        let record = result?;
        if &record[0] == "us" && &record[3] == "MA" {
            count += 1;
        }
    }
    Ok(count)
}

fn main() {
    match run() {
        Ok(count) => {
            println!("{}", count);
        }
        Err(err) => {
            println!("{}", err);
            process::exit(1);
        }
    }
}

```

### File: examples\tutorial-perf-alloc-02.rs
```rs
use std::{error::Error, io, process};

fn run() -> Result<u64, Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());

    let mut count = 0;
    for result in rdr.byte_records() {
        let record = result?;
        if &record[0] == b"us" && &record[3] == b"MA" {
            count += 1;
        }
    }
    Ok(count)
}

fn main() {
    match run() {
        Ok(count) => {
            println!("{}", count);
        }
        Err(err) => {
            println!("{}", err);
            process::exit(1);
        }
    }
}

```

### File: examples\tutorial-perf-alloc-03.rs
```rs
use std::{error::Error, io, process};

fn run() -> Result<u64, Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    let mut record = csv::ByteRecord::new();

    let mut count = 0;
    while rdr.read_byte_record(&mut record)? {
        if &record[0] == b"us" && &record[3] == b"MA" {
            count += 1;
        }
    }
    Ok(count)
}

fn main() {
    match run() {
        Ok(count) => {
            println!("{}", count);
        }
        Err(err) => {
            println!("{}", err);
            process::exit(1);
        }
    }
}

```

### File: examples\tutorial-perf-core-01.rs
```rs
use std::io::{self, Read};
use std::process;

use csv_core::{ReadFieldResult, Reader};

fn run(mut data: &[u8]) -> Option<u64> {
    let mut rdr = Reader::new();

    // Count the number of records in Massachusetts.
    let mut count = 0;
    // Indicates the current field index. Reset to 0 at start of each record.
    let mut fieldidx = 0;
    // True when the current record is in the United States.
    let mut inus = false;
    // Buffer for field data. Must be big enough to hold the largest field.
    let mut field = [0; 1024];
    loop {
        // Attempt to incrementally read the next CSV field.
        let (result, nread, nwrite) = rdr.read_field(data, &mut field);
        // nread is the number of bytes read from our input. We should never
        // pass those bytes to read_field again.
        data = &data[nread..];
        // nwrite is the number of bytes written to the output buffer `field`.
        // The contents of the buffer after this point is unspecified.
        let field = &field[..nwrite];

        match result {
            // We don't need to handle this case because we read all of the
            // data up front. If we were reading data incrementally, then this
            // would be a signal to read more.
            ReadFieldResult::InputEmpty => {}
            // If we get this case, then we found a field that contains more
            // than 1024 bytes. We keep this example simple and just fail.
            ReadFieldResult::OutputFull => {
                return None;
            }
            // This case happens when we've successfully read a field. If the
            // field is the last field in a record, then `record_end` is true.
            ReadFieldResult::Field { record_end } => {
                if fieldidx == 0 && field == b"us" {
                    inus = true;
                } else if inus && fieldidx == 3 && field == b"MA" {
                    count += 1;
                }
                if record_end {
                    fieldidx = 0;
                    inus = false;
                } else {
                    fieldidx += 1;
                }
            }
            // This case happens when the CSV reader has successfully exhausted
            // all input.
            ReadFieldResult::End => {
                break;
            }
        }
    }
    Some(count)
}

fn main() {
    // Read the entire contents of stdin up front.
    let mut data = vec![];
    if let Err(err) = io::stdin().read_to_end(&mut data) {
        println!("{}", err);
        process::exit(1);
    }
    match run(&data) {
        None => {
            println!("error: could not count records, buffer too small");
            process::exit(1);
        }
        Some(count) => {
            println!("{}", count);
        }
    }
}

```

### File: examples\tutorial-perf-serde-01.rs
```rs
#![allow(dead_code)]
use std::{error::Error, io, process};

use serde::Deserialize;

#[derive(Debug, Deserialize)]
#[serde(rename_all = "PascalCase")]
struct Record {
    country: String,
    city: String,
    accent_city: String,
    region: String,
    population: Option<u64>,
    latitude: f64,
    longitude: f64,
}

fn run() -> Result<u64, Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());

    let mut count = 0;
    for result in rdr.deserialize() {
        let record: Record = result?;
        if record.country == "us" && record.region == "MA" {
            count += 1;
        }
    }
    Ok(count)
}

fn main() {
    match run() {
        Ok(count) => {
            println!("{}", count);
        }
        Err(err) => {
            println!("{}", err);
            process::exit(1);
        }
    }
}

```

### File: examples\tutorial-perf-serde-02.rs
```rs
#![allow(dead_code)]
use serde::Deserialize;
use std::{error::Error, io, process};

#[derive(Debug, Deserialize)]
#[serde(rename_all = "PascalCase")]
struct Record<'a> {
    country: &'a str,
    city: &'a str,
    accent_city: &'a str,
    region: &'a str,
    population: Option<u64>,
    latitude: f64,
    longitude: f64,
}

fn run() -> Result<u64, Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    let mut raw_record = csv::StringRecord::new();
    let headers = rdr.headers()?.clone();

    let mut count = 0;
    while rdr.read_record(&mut raw_record)? {
        let record: Record = raw_record.deserialize(Some(&headers))?;
        if record.country == "us" && record.region == "MA" {
            count += 1;
        }
    }
    Ok(count)
}

fn main() {
    match run() {
        Ok(count) => {
            println!("{}", count);
        }
        Err(err) => {
            println!("{}", err);
            process::exit(1);
        }
    }
}

```

### File: examples\tutorial-perf-serde-03.rs
```rs
#![allow(dead_code)]
use std::{error::Error, io, process};

use serde::Deserialize;

#[derive(Debug, Deserialize)]
#[serde(rename_all = "PascalCase")]
struct Record<'a> {
    country: &'a [u8],
    city: &'a [u8],
    accent_city: &'a [u8],
    region: &'a [u8],
    population: Option<u64>,
    latitude: f64,
    longitude: f64,
}

fn run() -> Result<u64, Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    let mut raw_record = csv::ByteRecord::new();
    let headers = rdr.byte_headers()?.clone();

    let mut count = 0;
    while rdr.read_byte_record(&mut raw_record)? {
        let record: Record = raw_record.deserialize(Some(&headers))?;
        if record.country == b"us" && record.region == b"MA" {
            count += 1;
        }
    }
    Ok(count)
}

fn main() {
    match run() {
        Ok(count) => {
            println!("{}", count);
        }
        Err(err) => {
            println!("{}", err);
            process::exit(1);
        }
    }
}

```

### File: examples\tutorial-pipeline-pop-01.rs
```rs
use std::{env, error::Error, io, process};

use serde::{Deserialize, Serialize};

// Unlike previous examples, we derive both Deserialize and Serialize. This
// means we'll be able to automatically deserialize and serialize this type.
#[derive(Debug, Deserialize, Serialize)]
#[serde(rename_all = "PascalCase")]
struct Record {
    city: String,
    state: String,
    population: Option<u64>,
    latitude: f64,
    longitude: f64,
}

fn run() -> Result<(), Box<dyn Error>> {
    // Get the query from the positional arguments.
    // If one doesn't exist or isn't an integer, return an error.
    let minimum_pop: u64 = match env::args().nth(1) {
        None => return Err(From::from("expected 1 argument, but got none")),
        Some(arg) => arg.parse()?,
    };

    // Build CSV readers and writers to stdin and stdout, respectively.
    // Note that we don't need to write headers explicitly. Since we're
    // serializing a custom struct, that's done for us automatically.
    let mut rdr = csv::Reader::from_reader(io::stdin());
    let mut wtr = csv::Writer::from_writer(io::stdout());

    // Iterate over all the records in `rdr`, and write only records containing
    // a population that is greater than or equal to `minimum_pop`.
    for result in rdr.deserialize() {
        // Remember that when deserializing, we must use a type hint to
        // indicate which type we want to deserialize our record into.
        let record: Record = result?;

        // `is_some_and` is a combinator on `Option`. It takes a closure that
        // returns `bool` when the `Option` is `Some`. When the `Option` is
        // `None`, `false` is always returned. In this case, we test it against
        // our minimum population count that we got from the command line.
        if record.population.is_some_and(|pop| pop >= minimum_pop) {
            wtr.serialize(record)?;
        }
    }

    // CSV writers use an internal buffer, so we should always flush when done.
    wtr.flush()?;
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-pipeline-search-01.rs
```rs
use std::{env, error::Error, io, process};

fn run() -> Result<(), Box<dyn Error>> {
    // Get the query from the positional arguments.
    // If one doesn't exist, return an error.
    let query = match env::args().nth(1) {
        None => return Err(From::from("expected 1 argument, but got none")),
        Some(query) => query,
    };

    // Build CSV readers and writers to stdin and stdout, respectively.
    let mut rdr = csv::Reader::from_reader(io::stdin());
    let mut wtr = csv::Writer::from_writer(io::stdout());

    // Before reading our data records, we should write the header record.
    wtr.write_record(rdr.headers()?)?;

    // Iterate over all the records in `rdr`, and write only records containing
    // `query` to `wtr`.
    for result in rdr.records() {
        let record = result?;
        if record.iter().any(|field| field == query) {
            wtr.write_record(&record)?;
        }
    }

    // CSV writers use an internal buffer, so we should always flush when done.
    wtr.flush()?;
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-pipeline-search-02.rs
```rs
use std::{env, error::Error, io, process};

fn run() -> Result<(), Box<dyn Error>> {
    let query = match env::args().nth(1) {
        None => return Err(From::from("expected 1 argument, but got none")),
        Some(query) => query,
    };

    let mut rdr = csv::Reader::from_reader(io::stdin());
    let mut wtr = csv::Writer::from_writer(io::stdout());

    wtr.write_record(rdr.byte_headers()?)?;

    for result in rdr.byte_records() {
        let record = result?;
        // `query` is a `String` while `field` is now a `&[u8]`, so we'll
        // need to convert `query` to `&[u8]` before doing a comparison.
        if record.iter().any(|field| field == query.as_bytes()) {
            wtr.write_record(&record)?;
        }
    }

    wtr.flush()?;
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-read-01.rs
```rs
use std::{env, error::Error, ffi::OsString, fs::File, process};

fn run() -> Result<(), Box<dyn Error>> {
    let file_path = get_first_arg()?;
    let file = File::open(file_path)?;
    let mut rdr = csv::Reader::from_reader(file);
    for result in rdr.records() {
        let record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

/// Returns the first positional argument sent to this process. If there are no
/// positional arguments, then this returns an error.
fn get_first_arg() -> Result<OsString, Box<dyn Error>> {
    match env::args_os().nth(1) {
        None => Err(From::from("expected 1 argument, but got none")),
        Some(file_path) => Ok(file_path),
    }
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-read-delimiter-01.rs
```rs
use std::{error::Error, io, process};

fn run() -> Result<(), Box<dyn Error>> {
    let mut rdr = csv::ReaderBuilder::new()
        .has_headers(false)
        .delimiter(b';')
        .double_quote(false)
        .escape(Some(b'\\'))
        .flexible(true)
        .comment(Some(b'#'))
        .from_reader(io::stdin());
    for result in rdr.records() {
        let record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-read-headers-01.rs
```rs
use std::{error::Error, io, process};

fn run() -> Result<(), Box<dyn Error>> {
    let mut rdr =
        csv::ReaderBuilder::new().has_headers(false).from_reader(io::stdin());
    for result in rdr.records() {
        let record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-read-headers-02.rs
```rs
use std::{error::Error, io, process};

fn run() -> Result<(), Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    let headers = rdr.headers()?;
    println!("{:?}", headers);
    for result in rdr.records() {
        let record = result?;
        println!("{:?}", record);
    }
    // We can ask for the headers at any time.
    let headers = rdr.headers()?;
    println!("{:?}", headers);
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-read-serde-01.rs
```rs
use std::{error::Error, io, process};

fn run() -> Result<(), Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.records() {
        let record = result?;

        let city = &record[0];
        let state = &record[1];
        // Some records are missing population counts, so if we can't
        // parse a number, treat the population count as missing instead
        // of returning an error.
        let pop: Option<u64> = record[2].parse().ok();
        // Lucky us! Latitudes and longitudes are available for every record.
        // Therefore, if one couldn't be parsed, return an error.
        let latitude: f64 = record[3].parse()?;
        let longitude: f64 = record[4].parse()?;

        println!(
            "city: {:?}, state: {:?}, \
             pop: {:?}, latitude: {:?}, longitude: {:?}",
            city, state, pop, latitude, longitude
        );
    }
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-read-serde-02.rs
```rs
use std::{error::Error, io, process};

// This introduces a type alias so that we can conveniently reference our
// record type.
type Record = (String, String, Option<u64>, f64, f64);

fn run() -> Result<(), Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    // Instead of creating an iterator with the `records` method, we create
    // an iterator with the `deserialize` method.
    for result in rdr.deserialize() {
        // We must tell Serde what type we want to deserialize into.
        let record: Record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-read-serde-03.rs
```rs
use std::collections::HashMap;
use std::{error::Error, io, process};

// This introduces a type alias so that we can conveniently reference our
// record type.
type Record = HashMap<String, String>;

fn run() -> Result<(), Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.deserialize() {
        let record: Record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-read-serde-04.rs
```rs
#![allow(dead_code)]
use std::{error::Error, io, process};

// This lets us write `#[derive(Deserialize)]`.
use serde::Deserialize;

// We don't need to derive `Debug` (which doesn't require Serde), but it's a
// good habit to do it for all your types.
//
// Notice that the field names in this struct are NOT in the same order as
// the fields in the CSV data!
#[derive(Debug, Deserialize)]
#[serde(rename_all = "PascalCase")]
struct Record {
    latitude: f64,
    longitude: f64,
    population: Option<u64>,
    city: String,
    state: String,
}

fn run() -> Result<(), Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.deserialize() {
        let record: Record = result?;
        println!("{:?}", record);
        // Try this if you don't like each record smushed on one line:
        // println!("{:#?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-read-serde-invalid-01.rs
```rs
#![allow(dead_code)]
use std::{error::Error, io, process};

use serde::Deserialize;

#[derive(Debug, Deserialize)]
#[serde(rename_all = "PascalCase")]
struct Record {
    latitude: f64,
    longitude: f64,
    population: Option<u64>,
    city: String,
    state: String,
}

fn run() -> Result<(), Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.deserialize() {
        let record: Record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-read-serde-invalid-02.rs
```rs
#![allow(dead_code)]
use std::{error::Error, io, process};

use serde::Deserialize;
#[derive(Debug, Deserialize)]
#[serde(rename_all = "PascalCase")]
struct Record {
    latitude: f64,
    longitude: f64,
    #[serde(deserialize_with = "csv::invalid_option")]
    population: Option<u64>,
    city: String,
    state: String,
}

fn run() -> Result<(), Box<dyn Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    for result in rdr.deserialize() {
        let record: Record = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-setup-01.rs
```rs
// Import the standard library's I/O module so we can read from stdin.
use std::io;

// The `main` function is where your program starts executing.
fn main() {
    // Create a CSV parser that reads data from stdin.
    let mut rdr = csv::Reader::from_reader(io::stdin());
    // Loop over each record.
    for result in rdr.records() {
        // An error may occur, so abort the program in an unfriendly way.
        // We will make this more friendly later!
        let record = result.expect("a CSV record");
        // Print a debug version of the record.
        println!("{:?}", record);
    }
}

```

### File: examples\tutorial-write-01.rs
```rs
use std::{error::Error, io, process};

fn run() -> Result<(), Box<dyn Error>> {
    let mut wtr = csv::Writer::from_writer(io::stdout());
    // Since we're writing records manually, we must explicitly write our
    // header record. A header record is written the same way that other
    // records are written.
    wtr.write_record([
        "City",
        "State",
        "Population",
        "Latitude",
        "Longitude",
    ])?;
    wtr.write_record([
        "Davidsons Landing",
        "AK",
        "",
        "65.2419444",
        "-165.2716667",
    ])?;
    wtr.write_record(["Kenai", "AK", "7610", "60.5544444", "-151.2583333"])?;
    wtr.write_record(["Oakman", "AL", "", "33.7133333", "-87.3886111"])?;

    // A CSV writer maintains an internal buffer, so it's important
    // to flush the buffer when you're done.
    wtr.flush()?;
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-write-02.rs
```rs
use std::{env, error::Error, ffi::OsString, process};

fn run() -> Result<(), Box<dyn Error>> {
    let file_path = get_first_arg()?;
    let mut wtr = csv::Writer::from_path(file_path)?;

    wtr.write_record([
        "City",
        "State",
        "Population",
        "Latitude",
        "Longitude",
    ])?;
    wtr.write_record([
        "Davidsons Landing",
        "AK",
        "",
        "65.2419444",
        "-165.2716667",
    ])?;
    wtr.write_record(["Kenai", "AK", "7610", "60.5544444", "-151.2583333"])?;
    wtr.write_record(["Oakman", "AL", "", "33.7133333", "-87.3886111"])?;

    wtr.flush()?;
    Ok(())
}

/// Returns the first positional argument sent to this process. If there are no
/// positional arguments, then this returns an error.
fn get_first_arg() -> Result<OsString, Box<dyn Error>> {
    match env::args_os().nth(1) {
        None => Err(From::from("expected 1 argument, but got none")),
        Some(file_path) => Ok(file_path),
    }
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-write-delimiter-01.rs
```rs
use std::{error::Error, io, process};

fn run() -> Result<(), Box<dyn Error>> {
    let mut wtr = csv::WriterBuilder::new()
        .delimiter(b'\t')
        .quote_style(csv::QuoteStyle::NonNumeric)
        .from_writer(io::stdout());

    wtr.write_record([
        "City",
        "State",
        "Population",
        "Latitude",
        "Longitude",
    ])?;
    wtr.write_record([
        "Davidsons Landing",
        "AK",
        "",
        "65.2419444",
        "-165.2716667",
    ])?;
    wtr.write_record(["Kenai", "AK", "7610", "60.5544444", "-151.2583333"])?;
    wtr.write_record(["Oakman", "AL", "", "33.7133333", "-87.3886111"])?;

    wtr.flush()?;
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-write-serde-01.rs
```rs
use std::{error::Error, io, process};

fn run() -> Result<(), Box<dyn Error>> {
    let mut wtr = csv::Writer::from_writer(io::stdout());

    // We still need to write headers manually.
    wtr.write_record([
        "City",
        "State",
        "Population",
        "Latitude",
        "Longitude",
    ])?;

    // But now we can write records by providing a normal Rust value.
    //
    // Note that the odd `None::<u64>` syntax is required because `None` on
    // its own doesn't have a concrete type, but Serde needs a concrete type
    // in order to serialize it. That is, `None` has type `Option<T>` but
    // `None::<u64>` has type `Option<u64>`.
    wtr.serialize((
        "Davidsons Landing",
        "AK",
        None::<u64>,
        65.2419444,
        -165.2716667,
    ))?;
    wtr.serialize(("Kenai", "AK", Some(7610), 60.5544444, -151.2583333))?;
    wtr.serialize(("Oakman", "AL", None::<u64>, 33.7133333, -87.3886111))?;

    wtr.flush()?;
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: examples\tutorial-write-serde-02.rs
```rs
use std::{error::Error, io, process};

use serde::Serialize;

// Note that structs can derive both Serialize and Deserialize!
#[derive(Debug, Serialize)]
#[serde(rename_all = "PascalCase")]
struct Record<'a> {
    city: &'a str,
    state: &'a str,
    population: Option<u64>,
    latitude: f64,
    longitude: f64,
}

fn run() -> Result<(), Box<dyn Error>> {
    let mut wtr = csv::Writer::from_writer(io::stdout());

    wtr.serialize(Record {
        city: "Davidsons Landing",
        state: "AK",
        population: None,
        latitude: 65.2419444,
        longitude: -165.2716667,
    })?;
    wtr.serialize(Record {
        city: "Kenai",
        state: "AK",
        population: Some(7610),
        latitude: 60.5544444,
        longitude: -151.2583333,
    })?;
    wtr.serialize(Record {
        city: "Oakman",
        state: "AL",
        population: None,
        latitude: 33.7133333,
        longitude: -87.3886111,
    })?;

    wtr.flush()?;
    Ok(())
}

fn main() {
    if let Err(err) = run() {
        println!("{}", err);
        process::exit(1);
    }
}

```

### File: src\byte_record.rs
```rs
use std::{
    cmp, fmt,
    iter::FromIterator,
    ops::{self, Range},
    result,
};

use serde_core::de::Deserialize;

use crate::{
    deserializer::deserialize_byte_record,
    error::{new_utf8_error, Result, Utf8Error},
    string_record::StringRecord,
};

/// A single CSV record stored as raw bytes.
///
/// A byte record permits reading or writing CSV rows that are not UTF-8.
/// In general, you should prefer using a
/// [`StringRecord`](struct.StringRecord.html)
/// since it is more ergonomic, but a `ByteRecord` is provided in case you need
/// it.
///
/// If you are using the Serde (de)serialization APIs, then you probably never
/// need to interact with a `ByteRecord` or a `StringRecord`. However, there
/// are some circumstances in which you might need to use a raw record type
/// while still using Serde. For example, if you need to deserialize possibly
/// invalid UTF-8 fields, then you'll need to first read your record into a
/// `ByteRecord`, and then use `ByteRecord::deserialize` to run Serde. Another
/// reason for using the raw record deserialization APIs is if you're using
/// Serde to read into borrowed data such as a `&'a str` or a `&'a [u8]`.
///
/// Two `ByteRecord`s are compared on the basis of their field data. Any
/// position information associated with the records is ignored.
#[derive(Clone, Eq)]
pub struct ByteRecord(Box<ByteRecordInner>);

impl PartialEq for ByteRecord {
    fn eq(&self, other: &ByteRecord) -> bool {
        if self.len() != other.len() {
            return false;
        }
        self.iter().zip(other.iter()).all(|e| e.0 == e.1)
    }
}

impl<T: AsRef<[u8]>> PartialEq<Vec<T>> for ByteRecord {
    fn eq(&self, other: &Vec<T>) -> bool {
        self.iter_eq(other)
    }
}

impl<T: AsRef<[u8]>> PartialEq<Vec<T>> for &ByteRecord {
    fn eq(&self, other: &Vec<T>) -> bool {
        self.iter_eq(other)
    }
}

impl<T: AsRef<[u8]>> PartialEq<[T]> for ByteRecord {
    fn eq(&self, other: &[T]) -> bool {
        self.iter_eq(other)
    }
}

impl<T: AsRef<[u8]>> PartialEq<[T]> for &ByteRecord {
    fn eq(&self, other: &[T]) -> bool {
        self.iter_eq(other)
    }
}

impl fmt::Debug for ByteRecord {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "ByteRecord(")?;
        f.debug_list()
            .entries(self.iter().map(crate::debug::Bytes))
            .finish()?;
        write!(f, ")")?;
        Ok(())
    }
}

/// The inner portion of a byte record.
///
/// We use this memory layout so that moving a `ByteRecord` only requires
/// moving a single pointer. The optimization is dubious at best, but does
/// seem to result in slightly better numbers in microbenchmarks. Methinks this
/// may heavily depend on the underlying allocator.
#[derive(Clone, Debug, Eq, PartialEq)]
struct ByteRecordInner {
    /// The position of this byte record.
    pos: Option<Position>,
    /// All fields in this record, stored contiguously.
    fields: Vec<u8>,
    /// The number of and location of each field in this record.
    bounds: Bounds,
}

impl Default for ByteRecord {
    #[inline]
    fn default() -> ByteRecord {
        ByteRecord::new()
    }
}

impl ByteRecord {
    /// Create a new empty `ByteRecord`.
    ///
    /// Note that you may find the `ByteRecord::from` constructor more
    /// convenient, which is provided by an impl on the `From` trait.
    ///
    /// # Example: create an empty record
    ///
    /// ```
    /// use csv::ByteRecord;
    ///
    /// let record = ByteRecord::new();
    /// assert_eq!(record.len(), 0);
    /// ```
    ///
    /// # Example: initialize a record from a `Vec`
    ///
    /// ```
    /// use csv::ByteRecord;
    ///
    /// let record = ByteRecord::from(vec!["a", "b", "c"]);
    /// assert_eq!(record.len(), 3);
    /// ```
    #[inline]
    pub fn new() -> ByteRecord {
        ByteRecord::with_capacity(0, 0)
    }

    /// Create a new empty `ByteRecord` with the given capacity settings.
    ///
    /// `buffer` refers to the capacity of the buffer used to store the
    /// actual row contents. `fields` refers to the number of fields one
    /// might expect to store.
    #[inline]
    pub fn with_capacity(buffer: usize, fields: usize) -> ByteRecord {
        ByteRecord(Box::new(ByteRecordInner {
            pos: None,
            fields: vec![0; buffer],
            bounds: Bounds::with_capacity(fields),
        }))
    }

    /// Deserialize this record.
    ///
    /// The `D` type parameter refers to the type that this record should be
    /// deserialized into. The `'de` lifetime refers to the lifetime of the
    /// `ByteRecord`. The `'de` lifetime permits deserializing into structs
    /// that borrow field data from this record.
    ///
    /// An optional `headers` parameter permits deserializing into a struct
    /// based on its field names (corresponding to header values) rather than
    /// the order in which the fields are defined.
    ///
    /// # Example: without headers
    ///
    /// This shows how to deserialize a single row into a struct based on the
    /// order in which fields occur. This example also shows how to borrow
    /// fields from the `ByteRecord`, which results in zero allocation
    /// deserialization.
    ///
    /// ```
    /// use std::error::Error;
    ///
    /// use csv::ByteRecord;
    /// use serde::Deserialize;
    ///
    /// #[derive(Deserialize)]
    /// struct Row<'a> {
    ///     city: &'a str,
    ///     country: &'a str,
    ///     population: u64,
    /// }
    ///
    /// # fn main() { example().unwrap() }
    /// fn example() -> Result<(), Box<dyn Error>> {
    ///     let record = ByteRecord::from(vec![
    ///         "Boston", "United States", "4628910",
    ///     ]);
    ///
    ///     let row: Row = record.deserialize(None)?;
    ///     assert_eq!(row.city, "Boston");
    ///     assert_eq!(row.country, "United States");
    ///     assert_eq!(row.population, 4628910);
    ///     Ok(())
    /// }
    /// ```
    ///
    /// # Example: with headers
    ///
    /// This example is like the previous one, but shows how to deserialize
    /// into a struct based on the struct's field names. For this to work,
    /// you must provide a header row.
    ///
    /// This example also shows that you can deserialize into owned data
    /// types (e.g., `String`) instead of borrowed data types (e.g., `&str`).
    ///
    /// ```
    /// use std::error::Error;
    ///
    /// use csv::ByteRecord;
    /// use serde::Deserialize;
    ///
    /// #[derive(Deserialize)]
    /// struct Row {
    ///     city: String,
    ///     country: String,
    ///     population: u64,
    /// }
    ///
    /// # fn main() { example().unwrap() }
    /// fn example() -> Result<(), Box<dyn Error>> {
    ///     // Notice that the fields are not in the same order
    ///     // as the fields in the struct!
    ///     let header = ByteRecord::from(vec![
    ///         "country", "city", "population",
    ///     ]);
    ///     let record = ByteRecord::from(vec![
    ///         "United States", "Boston", "4628910",
    ///     ]);
    ///
    ///     let row: Row = record.deserialize(Some(&header))?;
    ///     assert_eq!(row.city, "Boston");
    ///     assert_eq!(row.country, "United States");
    ///     assert_eq!(row.population, 4628910);
    ///     Ok(())
    /// }
    /// ```
    pub fn deserialize<'de, D: Deserialize<'de>>(
        &'de self,
        headers: Option<&'de ByteRecord>,
    ) -> Result<D> {
        deserialize_byte_record(self, headers)
    }

    /// Returns an iterator over all fields in this record.
    ///
    /// # Example
    ///
    /// This example shows how to iterate over each field in a `ByteRecord`.
    ///
    /// ```
    /// use csv::ByteRecord;
    ///
    /// let record = ByteRecord::from(vec!["a", "b", "c"]);
    /// for field in record.iter() {
    ///     assert!(field == b"a" || field == b"b" || field == b"c");
    /// }
    /// ```
    #[inline]
    pub fn iter(&self) -> ByteRecordIter<'_> {
        self.into_iter()
    }

    /// Return the field at index `i`.
    ///
    /// If no field at index `i` exists, then this returns `None`.
    ///
    /// # Example
    ///
    /// ```
    /// use csv::ByteRecord;
    ///
    /// let record = ByteRecord::from(vec!["a", "b", "c"]);
    /// assert_eq!(record.get(1), Some(&b"b"[..]));
    /// assert_eq!(record.get(3), None);
    /// ```
    #[inline]
    pub fn get(&self, i: usize) -> Option<&[u8]> {
        self.0.bounds.get(i).map(|range| &self.0.fields[range])
    }

    /// Returns true if and only if this record is empty.
    ///
    /// # Example
    ///
    /// ```
    /// use csv::ByteRecord;
    ///
    /// assert!(ByteRecord::new().is_empty());
    /// ```
    #[inline]
    pub fn is_empty(&self) -> bool {
        self.len() == 0
    }

    /// Returns the number of fields in this record.
    ///
    /// # Example
    ///
    /// ```
    /// use csv::ByteRecord;
    ///
    /// let record = ByteRecord::from(vec!["a", "b", "c"]);
    /// assert_eq!(record.len(), 3);
    /// ```
    #[inline]
    pub fn len(&self) -> usize {
        self.0.bounds.len()
    }

    /// Truncate this record to `n` fields.
    ///
    /// If `n` is greater than the number of fields in this record, then this
    /// has no effect.
    ///
    /// # Example
    ///
    /// ```
    /// use csv::ByteRecord;
    ///
    /// let mut record = ByteRecord::from(vec!["a", "b", "c"]);
    /// assert_eq!(record.len(), 3);
    /// record.truncate(1);
    /// assert_eq!(record.len(), 1);
    /// assert_eq!(record, vec!["a"]);
    /// ```
    #[inline]
    pub fn truncate(&mut self, n: usize) {
        if n <= self.len() {
            self.0.bounds.len = n;
        }
    }

    /// Clear this record so that it has zero fields.
    ///
    /// This is equivalent to calling `truncate(0)`.
    ///
    /// Note that it is not necessary to clear the record to reuse it with
    /// the CSV reader.
    ///
    /// # Example
    ///
    /// ```
    /// use csv::ByteRecord;
    ///
    /// let mut record = ByteRecord::from(vec!["a", "b", "c"]);
    /// assert_eq!(record.len(), 3);
    /// record.clear();
    /// assert_eq!(record.len(), 0);
    /// ```
    #[inline]
    pub fn clear(&mut self) {
        self.truncate(0);
    }

    /// Trim the fields of this record so that leading and trailing whitespace
    /// is removed.
    ///
    /// This method uses the ASCII definition of whitespace. That is, only
    /// bytes in the class `[\t\n\v\f\r ]` are trimmed.
    ///
    /// # Example
    ///
    /// ```
    /// use csv::ByteRecord;
    ///
    /// let mut record = ByteRecord::from(vec![
    ///     "  ", "\tfoo", "bar  ", "b a z",
    /// ]);
    /// record.trim();
    /// assert_eq!(record, vec!["", "foo", "bar", "b a z"]);
    /// ```
    pub fn trim(&mut self) {
        let length = self.len();
        if length == 0 {
            return;
        }
        // TODO: We could likely do this in place, but for now, we allocate.
        let mut trimmed =
            ByteRecord::with_capacity(self.as_slice().len(), self.len());
        trimmed.set_position(self.position().cloned());
        for field in self.iter() {
            trimmed.push_field(trim_ascii(field));
        }
        *self = trimmed;
    }

    /// Add a new field to this record.
    ///
    /// # Example
    ///
    /// ```
    /// use csv::ByteRecord;
    ///
    /// let mut record = ByteRecord::new();
    /// record.push_field(b"foo");
    /// assert_eq!(&record[0], b"foo");
    /// ```
    #[inline]
    pub fn push_field(&mut self, field: &[u8]) {
        let (s, e) = (self.0.bounds.end(), self.0.bounds.end() + field.len());
        while e > self.0.fields.len() {
            self.expand_fields();
        }
        self.0.fields[s..e].copy_from_slice(field);
        self.0.bounds.add(e);
    }

    /// Return the position of this record, if available.
    ///
    /// # Example
    ///
    /// ```
    /// use std::error::Error;
    ///
    /// use csv::{ByteRecord, ReaderBuilder};
    ///
    /// # fn main() { example().unwrap(); }
    /// fn example() -> Result<(), Box<dyn Error>> {
    ///     let mut record = ByteRecord::new();
    ///     let mut rdr = ReaderBuilder::new()
    ///         .has_headers(false)
    ///         .from_reader("a,b,c\nx,y,z".as_bytes());
    ///
    ///     assert!(rdr.read_byte_record(&mut record)?);
    ///     {
    ///         let pos = record.position().expect("a record position");
    ///         assert_eq!(pos.byte(), 0);
    ///         assert_eq!(pos.line(), 1);
    ///         assert_eq!(pos.record(), 0);
    ///     }
    ///
    ///     assert!(rdr.read_byte_record(&mut record)?);
    ///     {
    ///         let pos = record.position().expect("a record position");
    ///         assert_eq!(pos.byte(), 6);
    ///         assert_eq!(pos.line(), 2);
    ///         assert_eq!(pos.record(), 1);
    ///     }
    ///
    ///     // Finish the CSV reader for good measure.
    ///     assert!(!rdr.read_byte_record(&mut record)?);
    ///     Ok(())
    /// }
    /// ```
    #[inline]
    pub fn position(&self) -> Option<&Position> {
        self.0.pos.as_ref()
    }

    /// Set the position of this record.
    ///
    /// # Example
    ///
    /// ```
    /// use csv::{ByteRecord, Position};
    ///
    /// let mut record = ByteRecord::from(vec!["a", "b", "c"]);
    /// let mut pos = Position::new();
    /// pos.set_byte(100);
    /// pos.set_line(4);
    /// pos.set_record(2);
    ///
    /// record.set_position(Some(pos.clone()));
    /// assert_eq!(record.position(), Some(&pos));
    /// ```
    #[inline]
    pub fn set_position(&mut self, pos: Option<Position>) {
        self.0.pos = pos;
    }

    /// Return the start and end position of a field in this record.
    ///
    /// If no such field exists at the given index, then return `None`.
    ///
    /// The range returned can be used with the slice returned by `as_slice`.
    ///
    /// # Example
    ///
    /// ```
    /// use csv::ByteRecord;
    ///
    /// let record = ByteRecord::from(vec!["foo", "quux", "z"]);
    /// let range = record.range(1).expect("a record range");
    /// assert_eq!(&record.as_slice()[range], &b"quux"[..]);
    /// ```
    #[inline]
    pub fn range(&self, i: usize) -> Option<Range<usize>> {
        self.0.bounds.get(i)
    }

    /// Return the entire row as a single byte slice. The slice returned stores
    /// all fields contiguously. The boundaries of each field can be determined
    /// via the `range` method.
    ///
    /// # Example
    ///
    /// ```
    /// use csv::ByteRecord;
    ///
    /// let record = ByteRecord::from(vec!["foo", "quux", "z"]);
    /// assert_eq!(record.as_slice(), &b"fooquuxz"[..]);
    /// ```
    #[inline]
    pub fn as_slice(&self) -> &[u8] {
        &self.0.fields[..self.0.bounds.end()]
    }

    /// Clone this record, but only copy `fields` up to the end of bounds. This
    /// is use
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
