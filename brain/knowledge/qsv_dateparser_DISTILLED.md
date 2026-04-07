---
id: qsv-dateparser
type: knowledge
owner: OA_Triage
---
# qsv-dateparser
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# qsv-dateparser

A rust library for parsing date strings in commonly used formats. Parsed date will be returned as `chrono`'s
`DateTime<Utc>`.

This is a fork of Rollie Ma's [dateparser](https://github.com/waltzofpearls/belt/tree/main/dateparser), specifically published to support [qsv](https://github.com/jqnatividad/qsv).
It supports a subset of date formats supported by dateparser, skipping more obscure formats, primarily
for performance.
It also adds support for parsing dates in DMY format, with the `parse_with_preference` function.

## Accepted date formats
```rust
// unix timestamp
"1511648546",
"1620021848429",
"1620024872717915000",
"0",
"-770172300",
"1671673426.123456789",
// rfc3339
"2021-05-01T01:17:02.604456Z",
"2017-11-25T22:34:50Z",
// rfc2822
"Wed, 02 Jun 2021 06:31:39 GMT",
// yyyy-mm-dd hh:mm:ss
"2014-04-26 05:24:37 PM",
"2021-04-30 21:14",
"2021-04-30 21:14:10",
"2021-04-30 21:14:10.052282",
"2014-04-26 17:24:37.123",
"2014-04-26 17:24:37.3186369",
"2012-08-03 18:31:59.257000000",
// yyyy-mm-dd hh:mm:ss z
"2017-11-25 13:31:15 PST",
"2017-11-25 13:31 PST",
"2014-12-16 06:20:00 UTC",
"2014-12-16 06:20:00 GMT",
"2014-04-26 13:13:43 +0800",
"2014-04-26 13:13:44 +09:00",
"2012-08-03 18:31:59.257000000 +0000",
"2015-09-30 18:48:56.35272715 UTC",
// yyyy-mm-dd
"2021-02-21",
// yyyy-mm-dd z
"2021-02-21 PST",
"2021-02-21 UTC",
"2020-07-20+08:00",
// Mon dd, yyyy, hh:mm:ss
"May 8, 2009 5:57:51 PM",
"September 17, 2012 10:09am",
"September 17, 2012, 10:10:09",
// Mon dd, yyyy hh:mm:ss z
"May 02, 2021 15:51:31 UTC",
"May 02, 2021 15:51 UTC",
"May 26, 2021, 12:49 AM PDT",
"September 17, 2012 at 10:09am PST",
// yyyy-mon-dd
"2021-Feb-21",
// Mon dd, yyyy
"May 25, 2021",
"oct 7, 1970",
"oct 7, 70",
"oct. 7, 1970",
"oct. 7, 70",
"October 7, 1970",
// dd Mon yyyy hh:mm:ss
"12 Feb 2006, 19:17",
"12 Feb 2006 19:17",
"14 May 2019 19:11:40.164",
// dd Mon yyyy
"7 oct 70",
"7 oct 1970",
"03 February 2013",
"1 July 2013",
// mm/dd/yyyy hh:mm:ss
"4/8/2014 22:05",
"04/08/2014 22:05",
"4/8/14 22:05",
"04/2/2014 03:00:51",
"8/8/1965 12:00:00 AM",
"8/8/1965 01:00:01 PM",
"8/8/1965 01:00 PM",
"8/8/1965 1:00 PM",
"8/8/1965 12:00 AM",
"4/02/2014 03:00:51",
"03/19/2012 10:11:59",
"03/19/2012 10:11:59.3186369",
// mm/dd/yyyy
"3/31/2014",
"03/31/2014",
"08/21/71",
"8/1/71",
// yyyy/mm/dd hh:mm:ss
"2014/4/8 22:05",
"2014/04/08 22:05",
"2014/04/2 03:00:51",
"2014/4/02 03:00:51",
"2012/03/19 10:11:59",
"2012/03/19 10:11:59.3186369",
// yyyy/mm/dd
"2014/3/31",
"2014/03/31",
// dd/mm/yyyy
"31/12/2020",
"12/10/2019",
"03/06/2018",
"27/06/68",
// dd/mm/yyyy hh:mm:ss
"4/8/2014 22:05",
"04/08/2014 22:05",
"4/8/14 22:05",
"04/2/2014 03:00:51",
"8/8/1965 12:00:00 AM",
"8/8/1965 01:00:01 PM",
"8/8/1965 01:00 PM",
"31/12/22 15:00"
```

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Test Commands

```bash
# Build
cargo build
cargo build --release

# Run all tests
cargo test

# Run a specific test
cargo test test_name

# Run benchmarks
cargo bench
```

## Architecture

qsv-dateparser is a performance-optimized Rust library for parsing date strings into `chrono::DateTime<Utc>`. It is a fork of [dateparser](https://github.com/waltzofpearls/belt/tree/main/dateparser), optimized for use in [qsv](https://github.com/jqnatividad/qsv).

### Core Structure

- **`src/lib.rs`**: Public API entry points
  - `parse()` - Parse with Local timezone assumption
  - `parse_with_preference()` - Parse with DMY/MDY preference
  - `parse_with_timezone()` - Parse with custom timezone
  - `parse_with_preference_and_timezone()` - Parse with DMY/MDY preference and custom timezone
  - `parse_with()` - Parse with custom timezone and default `NaiveTime`
  - `DateTimeUtc` - Wrapper implementing `FromStr` for `str::parse()` usage

- **`src/datetime.rs`**: Core parsing logic in `Parse` struct
  - Uses regex to detect format families, then tries specific parsers
  - Parse order: rfc2822 -> unix_timestamp -> slash formats -> ymd formats -> month formats
  - Each format family has a detection regex followed by specific format attempts using `or_else()` chains
  - Regexes are compiled once using `OnceLock` via a custom macro

- **`src/timezone.rs`**: Timezone offset parsing
  - Handles numeric offsets (+0800, +08:00) and named zones (PST, UTC, GMT)

### Key Design Decisions

1. **Format detection uses regex families**: Before trying specific parsers, a quick regex check determines which format family to try, avoiding unnecessary parsing attempts. Within each family, individual parsers apply cheap byte pre-filters (e.g. checking for `:`, input length, or trailing digit patterns) *before* running their regex, eliminating regex overhead on non-matching inputs. This two-layer approach — family regex gate, then byte pre-filter, then specific regex — is the established pattern for adding new parsers or optimizing existing ones.

2. **DMY preference**: The `prefer_dmy` flag controls whether `dd/mm/yyyy` or `mm/dd/yyyy` is tried first for ambiguous slash-separated dates.

3. **RFC3339 is parsed inside `ymd_family`**: `rfc3339()` is tried first within `ymd_family` using `chrono::DateTime::parse_from_rfc3339()`. The parse order is: rfc2822 → unix_timestamp → slash_mdy_family → slash_ymd_family → ymd_family (rfc3339 first) → month_ymd → month_mdy_family → month_dmy_family.

4. **Performance focus**: Uses `fast-float2` for timestamp parsing, minimal regex capture groups, and `#[inline]` annotations on hot paths.

```

### File: .claude\settings.local.json
```json
{
  "permissions": {
    "allow": [
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(cargo clippy:*)",
      "Bash(cargo test:*)",
      "Bash(cargo bench:*)",
      "Bash(cargo doc:*)",
      "Bash(cargo build:*)",
      "Bash(cargo fmt:*)",
      "Bash(cargo check:*)",
      "WebFetch(domain:github.com)",
      "WebFetch(domain:docs.rs)",
      "WebFetch(domain:crates.io)",
      "WebFetch(domain:raw.githubusercontent.com)",
      "Bash(git:*)",
      "Bash(claude mcp:*)",
      "Bash(cat target/criterion/**/*.json:*)",
      "Bash(echo === *:*)"
    ]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "cargo fmt --quiet 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}

```

### File: examples\convert_to_pacific.rs
```rs
use chrono_tz::US::Pacific;
use qsv_dateparser::DateTimeUtc;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let parsed = "Wed, 02 Jun 2021 06:31:39 GMT".parse::<DateTimeUtc>()?.0;
    println!("{:#?}", parsed.with_timezone(&Pacific));
    Ok(())
}

```

### File: examples\parse.rs
```rs
use qsv_dateparser::parse;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let parsed = parse("6:15pm")?;
    println!("{:#?}", parsed);
    Ok(())
}

```

### File: examples\parse_with.rs
```rs
use chrono::{
    naive::NaiveTime,
    offset::{Local, Utc},
};
use qsv_dateparser::parse_with;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let parsed_in_local = parse_with(
        "2021-10-09",
        &Local,
        NaiveTime::from_hms_opt(0, 0, 0).unwrap(),
    )?;
    println!("{:#?}", parsed_in_local);

    let parsed_in_utc = parse_with(
        "2021-10-09",
        &Utc,
        NaiveTime::from_hms_opt(0, 0, 0).unwrap(),
    )?;
    println!("{:#?}", parsed_in_utc);

    Ok(())
}

```

### File: examples\parse_with_timezone.rs
```rs
use chrono::offset::{Local, Utc};
use chrono_tz::US::Pacific;
use qsv_dateparser::parse_with_timezone;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let parsed_in_local = parse_with_timezone("6:15pm", &Local)?;
    println!("{:#?}", parsed_in_local);

    let parsed_in_utc = parse_with_timezone("6:15pm", &Utc)?;
    println!("{:#?}", parsed_in_utc);

    let parsed_in_pacific = parse_with_timezone("6:15pm", &Pacific)?;
    println!("{:#?}", parsed_in_pacific);

    Ok(())
}

```

### File: examples\str_parse_method.rs
```rs
use qsv_dateparser::DateTimeUtc;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let parsed = "2021-05-14 18:51 PDT".parse::<DateTimeUtc>()?.0;
    println!("{:#?}", parsed);
    Ok(())
}

```

### File: src\datetime.rs
```rs
#![allow(deprecated)]
use crate::timezone;
use anyhow::{Result, anyhow};
use chrono::prelude::*;
use regex::Regex;

macro_rules! regex {
    ($re:literal $(,)?) => {{
        static RE: std::sync::OnceLock<regex::Regex> = std::sync::OnceLock::new();
        RE.get_or_init(|| unsafe {
            regex::RegexBuilder::new($re)
                .unicode(false)
                .build()
                .unwrap_unchecked()
        })
    }};
}
/// Parse struct has methods implemented parsers for accepted formats.
pub struct Parse<'z, Tz2> {
    tz: &'z Tz2,
    default_time: NaiveTime,
    prefer_dmy: bool,
}

impl<'z, Tz2> Parse<'z, Tz2>
where
    Tz2: TimeZone,
{
    /// Create a new instance of [`Parse`] with a custom parsing timezone that handles the
    /// datetime string without time offset.
    pub const fn new(tz: &'z Tz2, default_time: NaiveTime) -> Self {
        Self {
            tz,
            default_time,
            prefer_dmy: false,
        }
    }

    pub const fn prefer_dmy(&mut self, yes: bool) -> &Self {
        self.prefer_dmy = yes;
        self
    }

    /// Create a new instance of [`Parse`] with a custom parsing timezone that handles the
    /// datetime string without time offset, and the date parsing preference.
    pub const fn new_with_preference(
        tz: &'z Tz2,
        default_time: NaiveTime,
        prefer_dmy: bool,
    ) -> Self {
        Self {
            tz,
            default_time,
            prefer_dmy,
        }
    }

    /// This method tries to parse the input datetime string with a list of accepted formats. See
    /// more examples from [`Parse`], [`crate::parse()`] and [`crate::parse_with_timezone()`].
    #[inline]
    pub fn parse(&self, input: &str) -> Result<DateTime<Utc>> {
        self.rfc2822(input)
            .or_else(|| self.unix_timestamp(input))
            .or_else(|| self.slash_mdy_family(input))
            .or_else(|| self.slash_ymd_family(input))
            .or_else(|| self.ymd_family(input))
            .or_else(|| self.month_ymd(input))
            .or_else(|| self.month_mdy_family(input))
            .or_else(|| self.month_dmy_family(input))
            .unwrap_or_else(|| Err(anyhow!("{} did not match any formats.", input)))
    }

    #[inline]
    fn ymd_family(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        let re: &Regex = regex! {
            r"^\d{4}-\d{2}"

        };

        if !re.is_match(input) {
            return None;
        }
        self.rfc3339(input)
            .or_else(|| self.ymd_hms(input))
            .or_else(|| self.ymd_hms_z(input))
            .or_else(|| self.ymd(input))
            .or_else(|| self.ymd_z(input))
    }

    #[inline]
    fn month_mdy_family(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        let re: &Regex = regex! {
            r"^[a-zA-Z]{3,9}\.?\s+\d{1,2}"
        };

        if !re.is_match(input) {
            return None;
        }
        self.month_mdy_hms(input)
            .or_else(|| self.month_mdy_hms_z(input))
            .or_else(|| self.month_mdy(input))
    }

    #[inline]
    fn month_dmy_family(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        let re: &Regex = regex! {r"^\d{1,2}\s+[a-zA-Z]{3,9}"
        };

        if !re.is_match(input) {
            return None;
        }
        self.month_dmy_hms(input).or_else(|| self.month_dmy(input))
    }

    #[inline]
    fn slash_mdy_family(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        let re: &Regex = regex! {r"^\d{1,2}/\d{1,2}"
        };
        if !re.is_match(input) {
            return None;
        }
        if self.prefer_dmy {
            self.slash_dmy_hms(input)
                .or_else(|| self.slash_dmy(input))
                .or_else(|| self.slash_mdy_hms(input))
                .or_else(|| self.slash_mdy(input))
        } else {
            self.slash_mdy_hms(input)
                .or_else(|| self.slash_mdy(input))
                .or_else(|| self.slash_dmy_hms(input))
                .or_else(|| self.slash_dmy(input))
        }
    }

    #[inline]
    fn slash_ymd_family(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        let re: &Regex = regex! {r"^[0-9]{4}/[0-9]{1,2}"};
        if !re.is_match(input) {
            return None;
        }
        self.slash_ymd_hms(input).or_else(|| self.slash_ymd(input))
    }

    // unix timestamp
    // - 0
    // - -770172300
    // - 1671673426.123456789
    #[inline]
    fn unix_timestamp(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        let ts_sec_val: f64 = if let Ok(val) = fast_float2::parse(input) {
            val
        } else {
            return None;
        };

        // convert the timestamp seconds value to nanoseconds
        let ts_ns_val = ts_sec_val * 1_000_000_000_f64;

        let result = Utc.timestamp_nanos(ts_ns_val as i64).with_timezone(&Utc);
        Some(Ok(result))
    }

    // rfc3339
    // - 2021-05-01T01:17:02.604456Z
    // - 2017-11-25T22:34:50Z
    #[inline]
    fn rfc3339(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        DateTime::parse_from_rfc3339(input)
            .ok()
            .map(|parsed| parsed.with_timezone(&Utc))
            .map(Ok)
    }

    // rfc2822
    // - Wed, 02 Jun 2021 06:31:39 GMT
    #[inline]
    fn rfc2822(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        DateTime::parse_from_rfc2822(input)
            .ok()
            .map(|parsed| parsed.with_timezone(&Utc))
            .map(Ok)
    }

    // yyyy-mm-dd hh:mm:ss
    // - 2014-04-26 05:24:37 PM
    // - 2021-04-30 21:14
    // - 2021-04-30 21:14:10
    // - 2021-04-30 21:14:10.052282
    // - 2014-04-26 17:24:37.123
    // - 2014-04-26 17:24:37.3186369
    // - 2012-08-03 18:31:59.257000000
    #[inline]
    fn ymd_hms(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        let re: &Regex = regex! {
                r"^\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}(:\d{2})?(\.\d{1,9})?\s*(am|pm|AM|PM)?$"

        };
        if !re.is_match(input) {
            return None;
        }

        self.tz
            .datetime_from_str(input, "%Y-%m-%d %H:%M:%S")
            .or_else(|_| self.tz.datetime_from_str(input, "%Y-%m-%d %H:%M"))
            .or_else(|_| self.tz.datetime_from_str(input, "%Y-%m-%d %H:%M:%S%.f"))
            .or_else(|_| self.tz.datetime_from_str(input, "%Y-%m-%d %I:%M:%S %P"))
            .or_else(|_| self.tz.datetime_from_str(input, "%Y-%m-%d %I:%M %P"))
            .ok()
            .map(|parsed| parsed.with_timezone(&Utc))
            .map(Ok)
    }

    // yyyy-mm-dd hh:mm:ss z
    // - 2017-11-25 13:31:15 PST
    // - 2017-11-25 13:31 PST
    // - 2014-12-16 06:20:00 UTC
    // - 2014-12-16 06:20:00 GMT
    // - 2014-04-26 13:13:43 +0800
    // - 2014-04-26 13:13:44 +09:00
    // - 2012-08-03 18:31:59.257000000 +0000
    // - 2015-09-30 18:48:56.35272715 UTC
    #[inline]
    fn ymd_hms_z(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        // Fast pre-filter: bare dates "YYYY-MM-DD" are 10 chars; valid inputs need space + time
        if input.len() < 17 || !input.as_bytes()[10].is_ascii_whitespace() {
            return None;
        }
        let re: &Regex = regex! {
                r"^\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}(:\d{2})?(\.\d{1,9})?(?P<tz>\s*[+-:a-zA-Z0-9]{3,6})$"
        };

        if let Some(caps) = re.captures(input)
            && let Some(matched_tz) = caps.name("tz")
        {
            let parse_from_str = NaiveDateTime::parse_from_str;
            return match timezone::parse(matched_tz.as_str().trim()) {
                Ok(offset) => parse_from_str(input, "%Y-%m-%d %H:%M:%S %Z")
                    .or_else(|_| parse_from_str(input, "%Y-%m-%d %H:%M %Z"))
                    .or_else(|_| parse_from_str(input, "%Y-%m-%d %H:%M:%S%.f %Z"))
                    .ok()
                    .and_then(|parsed| offset.from_local_datetime(&parsed).single())
                    .map(|datetime| datetime.with_timezone(&Utc))
                    .map(Ok),
                Err(err) => Some(Err(err)),
            };
        }
        None
    }

    // yyyy-mm-dd
    // - 2021-02-21
    #[inline]
    fn ymd(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        let re: &Regex = regex! {r"^\d{4}-\d{2}-\d{2}$"
        };

        if !re.is_match(input) {
            return None;
        }
        let now = Utc::now()
            .date()
            .and_time(self.default_time)?
            .with_timezone(self.tz);
        NaiveDate::parse_from_str(input, "%Y-%m-%d")
            .ok()
            .map(|parsed| parsed.and_time(now.time()))
            .and_then(|datetime| self.tz.from_local_datetime(&datetime).single())
            .map(|at_tz| at_tz.with_timezone(&Utc))
            .map(Ok)
    }

    // yyyy-mm-dd z
    // - 2021-02-21 PST
    // - 2021-02-21 UTC
    // - 2020-07-20+08:00 (yyyy-mm-dd-07:00)
    #[inline]
    fn ymd_z(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        // Fast pre-filter: bare date "YYYY-MM-DD" is exactly 10 chars; timezone appended = longer
        if input.len() <= 10 {
            return None;
        }
        let re: &Regex = regex! {r"^\d{4}-\d{2}-\d{2}(?P<tz>\s*[+-:a-zA-Z0-9]{3,6})$"
        };
        if let Some(caps) = re.captures(input)
            && let Some(matched_tz) = caps.name("tz")
        {
            return match timezone::parse(matched_tz.as_str().trim()) {
                Ok(offset) => {
                    let now = Utc::now()
                        .date()
                        .and_time(self.default_time)?
                        .with_timezone(&offset);
                    NaiveDate::parse_from_str(input, "%Y-%m-%d %Z")
                        .ok()
                        .map(|parsed| parsed.and_time(now.time()))
                        .and_then(|datetime| offset.from_local_datetime(&datetime).single())
                        .map(|at_tz| at_tz.with_timezone(&Utc))
                        .map(Ok)
                }
                Err(err) => Some(Err(err)),
            };
        }
        None
    }

    // yyyy-mon-dd
    // - 2021-Feb-21
    #[inline]
    fn month_ymd(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        let re: &Regex = regex! {r"^\d{4}-\w{3,9}-\d{2}$"
        };
        if !re.is_match(input) {
            return None;
        }

        let now = Utc::now()
            .date()
            .and_time(self.default_time)?
            .with_timezone(self.tz);
        NaiveDate::parse_from_str(input, "%Y-%m-%d")
            .or_else(|_| NaiveDate::parse_from_str(input, "%Y-%b-%d"))
            .ok()
            .map(|parsed| parsed.and_time(now.time()))
            .and_then(|datetime| self.tz.from_local_datetime(&datetime).single())
            .map(|at_tz| at_tz.with_timezone(&Utc))
            .map(Ok)
    }

    // Mon dd, yyyy, hh:mm:ss
    // - May 8, 2009 5:57:51 PM
    // - September 17, 2012 10:09am
    // - September 17, 2012, 10:10:09
    #[inline]
    fn month_mdy_hms(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        let re: &Regex = regex! {
                r"^[a-zA-Z]{3,9}\.?\s+\d{1,2},\s+\d{2,4},?\s+\d{1,2}:\d{2}(:\d{2})?\s*(am|pm|AM|PM)?$"
        };
        if !re.is_match(input) {
            return None;
        }

        // The regex above enforces \s+ after any comma or period, so removing bare ',' or '.'
        // is equivalent to the previous `replace(", ", " ").replace(". ", " ")` for all
        // inputs that reach this point — marginally-malformed inputs (e.g. "May 27,2012 …")
        // still fail to parse after stripping because the digits run together.
        let dt = input.replace([',', '.'], "");
        self.tz
            .datetime_from_str(&dt, "%B %d %Y %H:%M:%S")
            .or_else(|_| self.tz.datetime_from_str(&dt, "%B %d %Y %H:%M"))
            .or_else(|_| self.tz.datetime_from_str(&dt, "%B %d %Y %I:%M:%S %P"))
            .or_else(|_| self.tz.datetime_from_str(&dt, "%B %d %Y %I:%M %P"))
            .ok()
            .map(|at_tz| at_tz.with_timezone(&Utc))
            .map(Ok)
    }

    // Mon dd, yyyy hh:mm:ss z
    // - May 02, 2021 15:51:31 UTC
    // - May 02, 2021 15:51 UTC
    // - May 26, 2021, 12:49 AM PDT
    // - September 17, 2012 at 10:09am PST
    #[inline]
    fn month_mdy_hms_z(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        // Fast pre-filter: must contain an isolated 4-digit year — eliminates "May 27 02:45:27".
        // Skip the O(n) scan entirely for inputs too short to hold a valid month+day+year+time+tz.
        if input.len() < 20 {
            return None;
        }
        let bytes = input.as_bytes();
        let has_year = (0..bytes.len().saturating_sub(3)).any(|i| {
            bytes[i..i + 4].iter().all(|b| b.is_ascii_digit())
                && (i == 0 || !bytes[i - 1].is_ascii_digit())
                && bytes.get(i + 4).is_none_or(|b| !b.is_ascii_digit())
        });
        if !has_year {
            return None;
        }
        let re: &Regex = regex! {
                r"^[a-zA-Z]{3,9}\s+\d{1,2},?\s+\d{4}\s*,?(at)?\s+\d{2}:\d{2}(:\d{2})?\s*(am|pm|AM|PM)?(?P<tz>\s+[+-:a-zA-Z0-9]{3,6})$",
        };
        if let Some(caps) = re.captures(input)
            && let Some(matched_tz) = caps.name("tz")
        {
            let parse_from_str = NaiveDateTime::parse_from_str;
            return match timezone::parse(matched_tz.as_str().trim()) {
                Ok(offset) => {
                    let mut dt = input.replace(',', "");
                    if let Some(pos) = dt.find("at") {
                        dt.replace_range(pos..pos + 2, "");
                    }
                    parse_from_str(&dt, "%B %d %Y %H:%M:%S %Z")
                        .or_else(|_| parse_from_str(&dt, "%B %d %Y %H:%M %Z"))
                        .or_else(|_| parse_from_str(&dt, "%B %d %Y %I:%M:%S %P %Z"))
                        .or_else(|_| parse_from_str(&dt, "%B %d %Y %I:%M %P %Z"))
                        .ok()
                        .and_then(|parsed| offset.from_local_datetime(&parsed).single())
                        .map(|datetime| datetime.with_timezone(&Utc))
                        .map(Ok)
                }
                Err(err) => Some(Err(err)),
            };
        }
        None
    }

    // Mon dd, yyyy
    // - May 25, 2021
    // - oct 7, 1970
    // - oct 7, 70
    // - oct. 7, 1970
    // - oct. 7, 70
    // - October 7, 1970
    #[inline]
    fn month_mdy(&self, input: &str) -> Option<Result<DateTime<Utc>>> {
        let re: &Regex = regex! {r"^[a-zA-Z]{3,9}\.?\s+\d{1,2},\s+\d{2,4}$"
        };
        if !re.is_match(input) {
            return None;
        }

        let now = Utc::now()
            .date()
            .and_time(self.default_time)?
            .with_timezone(self.tz);
        // The regex above enforces \s+ after any comma or period, so removing bare ',' or '.'
        // is equivalent to the previous `replace(", ", " ").replace(". ", " ")` for all
        // inputs that reach th
... [TRUNCATED]
```

### File: src\lib.rs
```rs
//! A rust library for parsing date strings in commonly used formats. Parsed date will be returned
//! as `chrono`'s `DateTime<Utc>`.
//!
//! # Quick Start
//!
//!
//! Use `str`'s `parse` method:
//!
//! ```
//! use chrono::prelude::*;
//! use qsv_dateparser::DateTimeUtc;
//! use std::error::Error;
//!
//! fn main() -> Result<(), Box<dyn Error>> {
//!     assert_eq!(
//!         "2021-05-14 18:51 PDT".parse::<DateTimeUtc>()?.0,
//!         Utc.ymd(2021, 5, 15).and_hms(1, 51, 0),
//!     );
//!     Ok(())
//! }
//! ```
//!
//! ## Accepted date formats
//!
//! ```
//! use qsv_dateparser::DateTimeUtc;
//!
//! let accepted = vec![
//!     // unix timestamp
//!     "1511648546",
//!     "1620021848429",
//!     "1620024872717915000",
//!     "0",
//!     "-770172300",
//!     "1671673426.123456789",
//!     // rfc3339
//!     "2021-05-01T01:17:02.604456Z",
//!     "2017-11-25T22:34:50Z",
//!     // rfc2822
//!     "Wed, 02 Jun 2021 06:31:39 GMT",
//!     // yyyy-mm-dd hh:mm:ss
//!     "2014-04-26 05:24:37 PM",
//!     "2021-04-30 21:14",
//!     "2021-04-30 21:14:10",
//!     "2021-04-30 21:14:10.052282",
//!     "2014-04-26 17:24:37.123",
//!     "2014-04-26 17:24:37.3186369",
//!     "2012-08-03 18:31:59.257000000",
//!     // yyyy-mm-dd hh:mm:ss z
//!     "2017-11-25 13:31:15 PST",
//!     "2017-11-25 13:31 PST",
//!     "2014-12-16 06:20:00 UTC",
//!     "2014-12-16 06:20:00 GMT",
//!     "2014-04-26 13:13:43 +0800",
//!     "2014-04-26 13:13:44 +09:00",
//!     "2012-08-03 18:31:59.257000000 +0000",
//!     "2015-09-30 18:48:56.35272715 UTC",
//!     // yyyy-mm-dd
//!     "2021-02-21",
//!     // yyyy-mm-dd z
//!     "2021-02-21 PST",
//!     "2021-02-21 UTC",
//!     "2020-07-20+08:00",
//!     // Mon dd, yyyy, hh:mm:ss
//!     "May 8, 2009 5:57:51 PM",
//!     "September 17, 2012 10:09am",
//!     "September 17, 2012, 10:10:09",
//!     // Mon dd, yyyy hh:mm:ss z
//!     "May 02, 2021 15:51:31 UTC",
//!     "May 02, 2021 15:51 UTC",
//!     "May 26, 2021, 12:49 AM PDT",
//!     "September 17, 2012 at 10:09am PST",
//!     // yyyy-mon-dd
//!     "2021-Feb-21",
//!     // Mon dd, yyyy
//!     "May 25, 2021",
//!     "oct 7, 1970",
//!     "oct 7, 70",
//!     "oct. 7, 1970",
//!     "oct. 7, 70",
//!     "October 7, 1970",
//!     // dd Mon yyyy hh:mm:ss
//!     "12 Feb 2006, 19:17",
//!     "12 Feb 2006 19:17",
//!     "14 May 2019 19:11:40.164",
//!     // dd Mon yyyy
//!     "7 oct 70",
//!     "7 oct 1970",
//!     "03 February 2013",
//!     "1 July 2013",
//!     // mm/dd/yyyy hh:mm:ss
//!     "4/8/2014 22:05",
//!     "04/08/2014 22:05",
//!     "4/8/14 22:05",
//!     "04/2/2014 03:00:51",
//!     "8/8/1965 12:00:00 AM",
//!     "8/8/1965 01:00:01 PM",
//!     "8/8/1965 01:00 PM",
//!     "8/8/1965 1:00 PM",
//!     "8/8/1965 12:00 AM",
//!     "4/02/2014 03:00:51",
//!     "03/19/2012 10:11:59",
//!     "03/19/2012 10:11:59.3186369",
//!     // mm/dd/yyyy
//!     "3/31/2014",
//!     "03/31/2014",
//!     "08/21/71",
//!     "8/1/71",
//!     // yyyy/mm/dd hh:mm:ss
//!     "2014/4/8 22:05",
//!     "2014/04/08 22:05",
//!     "2014/04/2 03:00:51",
//!     "2014/4/02 03:00:51",
//!     "2012/03/19 10:11:59",
//!     "2012/03/19 10:11:59.3186369",
//!     // yyyy/mm/dd
//!     "2014/3/31",
//!     "2014/03/31",
//! ];
//!
//! for date_str in accepted {
//!     let result = date_str.parse::<DateTimeUtc>();
//!     assert!(result.is_ok())
//! }
//! ```
//!
//! ### DMY Format
//!
//! It also accepts dates in DMY format with `parse_with_preference`,
//! and the `prefer_dmy` parameter set to true.
//!
//! ```
//! use qsv_dateparser::parse_with_preference;
//!
//! let accepted = vec![
//!     // dd/mm/yyyy
//!     "31/12/2020",
//!     "12/10/2019",
//!     "03/06/2018",
//!     "27/06/68",
//!     // dd/mm/yyyy hh:mm:ss
//!     "4/8/2014 22:05",
//!     "04/08/2014 22:05",
//!     "4/8/14 22:05",
//!     "04/2/2014 03:00:51",
//!     "8/8/1965 12:00:00 AM",
//!     "8/8/1965 01:00:01 PM",
//!     "8/8/1965 01:00 PM",
//!     "31/12/22 15:00"
//! ];
//!
//! for date_str in accepted {
//!     let result = parse_with_preference(date_str, true);
//!     assert!(result.is_ok());
//! }
//! ```

/// Datetime string parser
///
/// ```
/// use chrono::prelude::*;
/// use qsv_dateparser::datetime::Parse;
/// use std::error::Error;
///
/// fn main() -> Result<(), Box<dyn Error>> {
///     let utc_now_time = Utc::now().time();
///     let parse_with_local = Parse::new(&Local, utc_now_time);
///     assert_eq!(
///         parse_with_local.parse("2021-06-05 06:19 PM")?,
///         Local.ymd(2021, 6, 5).and_hms(18, 19, 0).with_timezone(&Utc),
///     );
///
///     let parse_with_utc = Parse::new(&Utc, utc_now_time);
///     assert_eq!(
///         parse_with_utc.parse("2021-06-05 06:19 PM")?,
///         Utc.ymd(2021, 6, 5).and_hms(18, 19, 0),
///     );
///
///     Ok(())
/// }
/// ```
pub mod datetime;

/// Timezone offset string parser
///
/// ```
/// use chrono::prelude::*;
/// use qsv_dateparser::timezone::parse;
/// use std::error::Error;
///
/// fn main() -> Result<(), Box<dyn Error>> {
///     assert_eq!(parse("-0800")?, FixedOffset::west(8 * 3600));
///     assert_eq!(parse("+10:00")?, FixedOffset::east(10 * 3600));
///     assert_eq!(parse("PST")?, FixedOffset::west(8 * 3600));
///     assert_eq!(parse("PDT")?, FixedOffset::west(7 * 3600));
///     assert_eq!(parse("UTC")?, FixedOffset::west(0));
///     assert_eq!(parse("GMT")?, FixedOffset::west(0));
///
///     Ok(())
/// }
/// ```
pub mod timezone;

use crate::datetime::Parse;
use anyhow::{Error, Result};
use chrono::prelude::*;
use std::sync::OnceLock;

/// `DateTimeUtc` is an alias for `chrono`'s `DateTime<UTC>`. It implements `std::str::FromStr`'s
/// `from_str` method, and it makes `str`'s `parse` method to understand the accepted date formats
/// from this crate.
///
/// ```
/// use qsv_dateparser::DateTimeUtc;
///
/// // parsed is DateTimeUTC and parsed.0 is chrono's DateTime<Utc>
/// match "May 02, 2021 15:51:31 UTC".parse::<DateTimeUtc>() {
///     Ok(parsed) => println!("PARSED into UTC datetime {:?}", parsed.0),
///     Err(err) => println!("ERROR from parsing datetime string: {}", err)
/// }
/// ```
pub struct DateTimeUtc(pub DateTime<Utc>);

impl std::str::FromStr for DateTimeUtc {
    type Err = Error;

    fn from_str(s: &str) -> Result<Self> {
        parse(s).map(DateTimeUtc)
    }
}

static MIDNIGHT: OnceLock<chrono::NaiveTime> = OnceLock::new();

/// This function tries to recognize the input datetime string with a list of accepted formats.
/// When timezone is not provided, this function assumes it's a [`chrono::Local`] datetime. For
/// custom timezone, use [`parse_with_timezone()`] instead.If all options are exhausted,
/// [`parse()`] will return an error to let the caller know that no formats were matched.
#[inline]
pub fn parse(input: &str) -> Result<DateTime<Utc>> {
    Parse::new(&Local, Utc::now().time()).parse(input)
}

/// Similar to [`parse()`], this function takes a datetime string and a boolean `dmy_preference`.
/// When `dmy_preference` is `true`, it will parse strings using the DMY format. Otherwise, it
/// parses them using an MDY format.
#[inline]
pub fn parse_with_preference(input: &str, dmy_preference: bool) -> Result<DateTime<Utc>> {
    let midnight = MIDNIGHT.get_or_init(|| NaiveTime::from_hms_opt(0, 0, 0).unwrap());
    Parse::new_with_preference(&Utc, *midnight, dmy_preference).parse(input)
}

/// Similar to [`parse()`], this function takes a datetime string and a custom [`chrono::TimeZone`],
/// and tries to parse the datetime string. When timezone is not given in the string, this function
/// will assume and parse the datetime by the custom timezone provided in this function's arguments.
///
#[inline]
pub fn parse_with_timezone<Tz2: TimeZone>(input: &str, tz: &Tz2) -> Result<DateTime<Utc>> {
    Parse::new(tz, Utc::now().time()).parse(input)
}

/// Similar to [`parse()`], this function takes a datetime string and a boolean `dmy_preference`
/// and a timezone. When timezone is not given in the input string, this function will
/// assume and parse the datetime by the custom timezone provided in this function's arguments.
/// When `dmy_preference` is `true`, it will parse strings using the DMY format. Otherwise, it
/// parses them using an MDY format.
#[inline]
pub fn parse_with_preference_and_timezone<Tz2: TimeZone>(
    input: &str,
    dmy_preference: bool,
    tz: &Tz2,
) -> Result<DateTime<Utc>> {
    let midnight = MIDNIGHT.get_or_init(|| NaiveTime::from_hms_opt(0, 0, 0).unwrap());
    Parse::new_with_preference(tz, *midnight, dmy_preference).parse(input)
}

/// Similar to [`parse()`] and [`parse_with_timezone()`], this function takes a datetime string, a
/// custom [`chrono::TimeZone`] and a default naive time. In addition to assuming timezone when
/// it's not given in datetime string, this function also use provided default naive time in parsed
/// [`chrono::DateTime`].
///
#[inline]
pub fn parse_with<Tz2: TimeZone>(
    input: &str,
    tz: &Tz2,
    default_time: NaiveTime,
) -> Result<DateTime<Utc>> {
    Parse::new(tz, default_time).parse(input)
}

#[cfg(test)]
#[allow(deprecated)]
mod tests {
    use super::*;

    #[derive(Clone, Copy)]
    enum Trunc {
        Seconds,
        None,
    }

    #[test]
    fn parse_in_local() {
        let test_cases = vec![
            (
                "rfc3339",
                "2017-11-25T22:34:50Z",
                Utc.ymd(2017, 11, 25).and_hms(22, 34, 50),
                Trunc::None,
            ),
            (
                "rfc2822",
                "Wed, 02 Jun 2021 06:31:39 GMT",
                Utc.ymd(2021, 6, 2).and_hms(6, 31, 39),
                Trunc::None,
            ),
            (
                "ymd_hms",
                "2021-04-30 21:14:10",
                Local
                    .ymd(2021, 4, 30)
                    .and_hms(21, 14, 10)
                    .with_timezone(&Utc),
                Trunc::None,
            ),
            (
                "ymd_hms_z",
                "2017-11-25 13:31:15 PST",
                Utc.ymd(2017, 11, 25).and_hms(21, 31, 15),
                Trunc::None,
            ),
            (
                "ymd",
                "2021-02-21",
                Local
                    .ymd(2021, 2, 21)
                    .and_time(Local::now().time())
                    .unwrap()
                    .with_timezone(&Utc),
                Trunc::Seconds,
            ),
            (
                "ymd_z",
                "2021-02-21 PST",
                FixedOffset::west(8 * 3600)
                    .ymd(2021, 2, 21)
                    .and_time(
                        Utc::now()
                            .with_timezone(&FixedOffset::west(8 * 3600))
                            .time(),
                    )
                    .unwrap()
                    .with_timezone(&Utc),
                Trunc::Seconds,
            ),
            (
                "month_ymd",
                "2021-Feb-21",
                Local
                    .ymd(2021, 2, 21)
                    .and_time(Local::now().time())
                    .unwrap()
                    .with_timezone(&Utc),
                Trunc::Seconds,
            ),
            (
                "month_mdy_hms",
                "May 8, 2009 5:57:51 PM",
                Local
                    .ymd(2009, 5, 8)
                    .and_hms(17, 57, 51)
                    .with_timezone(&Utc),
                Trunc::None,
            ),
            (
                "month_mdy_hms_z",
                "May 02, 2021 15:51 UTC",
                Utc.ymd(2021, 5, 2).and_hms(15, 51, 0),
                Trunc::None,
            ),
            (
                "month_mdy",
                "May 25, 2021",
                Local
                    .ymd(2021, 5, 25)
                    .and_time(Local::now().time())
                    .unwrap()
                    .with_timezone(&Utc),
                Trunc::Seconds,
            ),
            (
                "month_dmy_hms",
                "14 May 2019 19:11:40.164",
                Local
                    .ymd(2019, 5, 14)
                    .and_hms_milli(19, 11, 40, 164)
                    .with_timezone(&Utc),
                Trunc::None,
            ),
            (
                "month_dmy",
                "1 July 2013",
                Local
                    .ymd(2013, 7, 1)
                    .and_time(Local::now().time())
                    .unwrap()
                    .with_timezone(&Utc),
                Trunc::Seconds,
            ),
            (
                "slash_mdy_hms",
                "03/19/2012 10:11:59",
                Local
                    .ymd(2012, 3, 19)
                    .and_hms(10, 11, 59)
                    .with_timezone(&Utc),
                Trunc::None,
            ),
            (
                "slash_mdy",
                "08/21/71",
                Local
                    .ymd(1971, 8, 21)
                    .and_time(Local::now().time())
                    .unwrap()
                    .with_timezone(&Utc),
                Trunc::Seconds,
            ),
            (
                "slash_ymd_hms",
                "2012/03/19 10:11:59",
                Local
                    .ymd(2012, 3, 19)
                    .and_hms(10, 11, 59)
                    .with_timezone(&Utc),
                Trunc::None,
            ),
            (
                "slash_ymd",
                "2014/3/31",
                Local
                    .ymd(2014, 3, 31)
                    .and_time(Local::now().time())
                    .unwrap()
                    .with_timezone(&Utc),
                Trunc::Seconds,
            ),
        ];

        for &(test, input, want, trunc) in test_cases.iter() {
            match trunc {
                Trunc::None => {
                    assert_eq!(
                        super::parse(input).unwrap(),
                        want,
                        "parse_in_local/{}/{}",
                        test,
                        input
                    )
                }
                Trunc::Seconds => assert_eq!(
                    super::parse(input)
                        .unwrap()
                        .trunc_subsecs(0)
                        .with_second(0)
                        .unwrap(),
                    want.trunc_subsecs(0).with_second(0).unwrap(),
                    "parse_in_local/{}/{}",
                    test,
                    input
                ),
            };
        }
    }

    #[test]
    fn parse_with_timezone_in_utc() {
        let test_cases = vec![
            (
                "rfc3339",
                "2017-11-25T22:34:50Z",
                Utc.ymd(2017, 11, 25).and_hms(22, 34, 50),
                Trunc::None,
            ),
            (
                "rfc2822",
                "Wed, 02 Jun 2021 06:31:39 GMT",
                Utc.ymd(2021, 6, 2)
... [TRUNCATED]
```

### File: src\timezone.rs
```rs
use anyhow::{Result, anyhow};
use chrono::offset::FixedOffset;

/// Tries to parse `[-+]\d\d` continued by `\d\d`. Return `FixedOffset` if possible.
/// It can parse RFC 2822 legacy timezones. If offset cannot be determined, -0000 will be returned.
///
/// The additional `colon` may be used to parse a mandatory or optional `:` between hours and minutes,
/// and should return a valid `FixedOffset` or `Err` when parsing fails.
#[inline]
pub fn parse(s: &str) -> Result<FixedOffset> {
    FixedOffset::east_opt(if s.contains(':') {
        parse_offset_internal(s, colon_or_space, false)?
    } else {
        parse_offset_2822(s)?
    })
    .ok_or_else(|| anyhow!("input is out of range"))
}

#[inline]
fn parse_offset_2822(s: &str) -> Result<i32> {
    // tries to parse legacy time zone names
    let upto = s
        .as_bytes()
        .iter()
        .position(|&c| !c.is_ascii_alphabetic())
        .unwrap_or(s.len());
    if upto > 0 {
        let name = &s[..upto];
        let offset_hours = |o| Ok(o * 3600);
        if equals(name, "gmt") || equals(name, "ut") || equals(name, "utc") {
            offset_hours(0)
        } else if equals(name, "edt") {
            offset_hours(-4)
        } else if equals(name, "est") || equals(name, "cdt") {
            offset_hours(-5)
        } else if equals(name, "cst") || equals(name, "mdt") {
            offset_hours(-6)
        } else if equals(name, "mst") || equals(name, "pdt") {
            offset_hours(-7)
        } else if equals(name, "pst") {
            offset_hours(-8)
        } else {
            Ok(0) // recommended by RFC 2822: consume but treat it as -0000
        }
    } else {
        let offset = parse_offset_internal(s, |s| Ok(s), false)?;
        Ok(offset)
    }
}

#[inline]
fn parse_offset_internal<F>(
    mut s: &str,
    mut consume_colon: F,
    allow_missing_minutes: bool,
) -> Result<i32>
where
    F: FnMut(&str) -> Result<&str>,
{
    let err_out_of_range = "input is out of range";
    let err_invalid = "input contains invalid characters";
    let err_too_short = "premature end of input";

    let digits = |s: &str| -> Result<(u8, u8)> {
        let b = s.as_bytes();
        if b.len() < 2 {
            Err(anyhow!(err_too_short))
        } else {
            Ok((b[0], b[1]))
        }
    };
    let negative = match s.as_bytes().first() {
        Some(&b'+') => false,
        Some(&b'-') => true,
        Some(_) => return Err(anyhow!(err_invalid)),
        None => return Err(anyhow!(err_too_short)),
    };
    s = &s[1..];

    // hours (00--99)
    let hours = match digits(s)? {
        (h1 @ b'0'..=b'9', h2 @ b'0'..=b'9') => i32::from((h1 - b'0') * 10 + (h2 - b'0')),
        _ => return Err(anyhow!(err_invalid)),
    };
    s = &s[2..];

    // colons (and possibly other separators)
    s = consume_colon(s)?;

    // minutes (00--59)
    // if the next two items are digits then we have to add minutes
    let minutes = match digits(s) {
        Ok(ds) => match ds {
            (m1 @ b'0'..=b'5', m2 @ b'0'..=b'9') => i32::from((m1 - b'0') * 10 + (m2 - b'0')),
            (b'6'..=b'9', b'0'..=b'9') => return Err(anyhow!(err_out_of_range)),
            _ => return Err(anyhow!(err_invalid)),
        },
        _ => {
            if allow_missing_minutes {
                0
            } else {
                return Err(anyhow!(err_too_short));
            }
        }
    };

    let seconds = hours * 3600 + minutes * 60;
    Ok(if negative { -seconds } else { seconds })
}

/// Returns true when two slices are equal case-insensitively (in ASCII).
/// Assumes that the `pattern` is already converted to lower case.
#[inline]
fn equals(s: &str, pattern: &str) -> bool {
    let mut xs = s.as_bytes().iter().map(|&c| match c {
        b'A'..=b'Z' => c + 32,
        _ => c,
    });
    let mut ys = pattern.as_bytes().iter().copied();
    loop {
        match (xs.next(), ys.next()) {
            (None, None) => return true,
            (None, _) | (_, None) => return false,
            (Some(x), Some(y)) if x != y => return false,
            _ => (),
        }
    }
}

/// Consumes any number (including zero) of colon or spaces.
#[inline]
fn colon_or_space(s: &str) -> Result<&str> {
    Ok(s.trim_start_matches(|c: char| c == ':' || c.is_whitespace()))
}

#[cfg(test)]
#[allow(deprecated)]
mod tests {
    use super::*;

    #[test]
    fn parse() {
        let test_cases = [
            ("-0800", FixedOffset::west(8 * 3600)),
            ("+10:00", FixedOffset::east(10 * 3600)),
            ("PST", FixedOffset::west(8 * 3600)),
            ("PDT", FixedOffset::west(7 * 3600)),
            ("UTC", FixedOffset::west(0)),
            ("GMT", FixedOffset::west(0)),
        ];

        for &(input, want) in test_cases.iter() {
            assert_eq!(super::parse(input).unwrap(), want, "parse/{}", input)
        }
    }
}

```

### File: .claude\agents\performance-reviewer.md
```md
---
name: performance-reviewer
description: Reviews code changes to src/datetime.rs, src/lib.rs, or src/timezone.rs for performance regressions. Use when the user is about to commit or wants a perf check on parsing hot paths.
---

You are a Rust performance expert specializing in zero-overhead parsing libraries. Your job is to review diffs or code in qsv-dateparser for performance regressions.

## Project Context

qsv-dateparser is a performance-critical date string parser. Key design invariants:

- **Regexes compiled once**: All regexes use the `regex!` macro backed by `OnceLock`. Never create a `Regex` outside this macro.
- **`#[inline]` on all parse methods**: Every method in `Parse` that is called on a hot path has `#[inline]`. Check that new methods follow this.
- **`or_else()` chain for format families**: `parse()` chains format-family detectors via `or_else()`. The order matters for performance — more common formats should be earlier.
- **`fast-float2` for timestamp parsing**: Floating-point timestamps use `fast_float2::parse()`, not `str::parse::<f64>()`.
- **Regex detection before format attempts**: Each format family checks a cheap regex first to skip the family entirely. New format families must follow this pattern.
- **No `unicode` in regexes**: All `RegexBuilder` calls set `.unicode(false)` for speed. Never omit this.

## What to Check in a Diff

For any changes to `src/datetime.rs`, `src/lib.rs`, or `src/timezone.rs`, look for:

### 🔴 Critical regressions
- A `Regex::new()` or `RegexBuilder::new()` call **outside** the `regex!` macro (re-compiles on every call)
- Use of `str::parse::<f64>()` or `.parse::<f64>()` instead of `fast_float2::parse()`
- Heap allocations inside a parsing method (`.to_string()`, `String::from()`, `format!()`, `.collect::<Vec<_>>()`)
- A new format family added without a regex pre-filter

### ⚠️ Warnings
- A new parse method missing `#[inline]`
- A new format added early in the `or_else()` chain that is rarer than formats already there
- Regex patterns that use Unicode character classes (e.g. `\w`, `\d` without `.unicode(false)`) — prefer `[0-9]` or `\d` with unicode disabled
- Unnecessary `.clone()` on `&str` or small copy types
- New `.unwrap()` calls that could be `.unwrap_unchecked()` in a proven-safe context (with a `// SAFETY:` comment)

### ✅ Good patterns to confirm are preserved
- `regex!` macro used for every new regex
- `.unicode(false)` on every new `RegexBuilder`
- `#[inline]` on every new method in `Parse`
- `fast_float2::parse()` for any new float parsing
- Format families gated behind a cheap `re.is_match(input)` check

## Output Format

Summarize findings in three sections:

**Critical** (must fix before merge): list each issue with file:line and explanation

**Warnings** (should fix): list each issue with file:line and recommendation

**Confirmed** (good patterns present): brief bullet list of invariants that were checked and are intact

If there are no issues, say so clearly: "No performance regressions found. All invariants intact."

```

### File: .claude\skills\bench-compare\SKILL.md
```md
---
name: bench-compare
description: Run Criterion benchmarks and compare against a saved baseline to detect performance regressions. Usage - /bench-compare save|compare|run
---

You are a performance benchmarking assistant for the qsv-dateparser Rust library.

The benchmark suite (benches/parse.rs) uses Criterion and covers three groups:
- `parse_all` — 20 accepted date formats in one batch + 1000-date throughput test
- `parse_each` — individual timing for each of the 20 date format strings
- `memory_usage` — allocation size of parse results

## Commands

### `/bench-compare save`
Save a new baseline before making changes:
```bash
cargo bench -- --save-baseline before
```
Tell the user: "Baseline saved as 'before'. Make your changes, then run `/bench-compare compare`."

### `/bench-compare compare`
Compare current code against the saved baseline:
```bash
cargo bench -- --baseline before
```
After running, parse the Criterion output and report:
- Any benchmark that **regressed > 3%** as a ⚠️ warning
- Any benchmark that **improved > 3%** as a ✅ improvement
- Benchmarks within ±3% as stable (summarize, don't list individually)
- Highlight regressions in `parse_each` by format name so the caller knows exactly which format slowed down

### `/bench-compare run`
Run benchmarks without comparison (no baseline needed):
```bash
cargo bench
```
Summarize the results: report `parse_all/accepted_formats`, `parse_throughput/1000_dates`, and the three slowest individual formats from `parse_each`.

## Regression Thresholds
- **> 10%** regression: flag as critical, suggest reverting or investigating before merging
- **3–10%** regression: flag as warning, recommend profiling the affected format parser
- **< 3%**: noise, treat as stable

## Notes
- Criterion HTML reports are written to `target/criterion/` — mention this to the user
- The `SELECTED` benchmark covers the 20 canonical format strings; regressions there are the most important to flag
- If `cargo bench` fails to compile, run `cargo check` first to surface the error clearly

```

### File: .claude\skills\release\SKILL.md
```md
---
name: release
description: Prepare and publish a new qsv-dateparser release. Usage - /release <version> (e.g. /release 0.14.0)
disable-model-invocation: true
---

You are a release assistant for the qsv-dateparser Rust library. Follow these steps exactly and stop if any step fails.

## Steps

### 1. Confirm the version argument
If no version was provided, ask the user: "Which version number should I release? (e.g. 0.14.0)"

### 2. Check working tree is clean
```bash
git status --short
```
If any uncommitted changes exist, stop and tell the user to commit or stash them first.

### 3. Confirm no existing tag
```bash
git tag --list "<version>"
```
If the tag already exists, stop and warn the user.

### 4. Bump version in Cargo.toml
Edit the `version` field in `[package]` in `Cargo.toml` to the new version string.

### 5. Refresh Cargo.lock
```bash
cargo build
```
This updates `Cargo.lock` to reflect the new version. Stop if it fails.

### 6. Run the full test suite
```bash
cargo test
```
Stop if any test fails — do not proceed to commit.

### 7. Run clippy
```bash
cargo clippy --workspace --tests --all-features -- -D warnings
```
Stop if there are any warnings — do not proceed to commit.

### 8. Stage and commit
```bash
git add Cargo.toml Cargo.lock
git commit -m "<version> release"
```
The commit message format matches the project convention (e.g. `0.13.0 release`).

### 9. Create an annotated tag
```bash
git tag -a <version> -m "<version>"
```

### 10. Show summary and next steps
Print a summary:
- Version bumped to: `<version>`
- Commit: show the short SHA from `git log -1 --oneline`
- Tag: `<version>`

Then tell the user:
> Review the commit and tag above, then run the following to publish:
> ```bash
> git push origin main
> git push origin <version>
> cargo publish
> ```
> These are NOT run automatically — confirm before pushing.

```

