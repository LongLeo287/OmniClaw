---
id: tafia-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:20.780461
---

# KNOWLEDGE EXTRACT: tafia
> **Extracted on:** 2026-03-30 17:54:14
> **Source:** tafia

---

## File: `calamine.md`
```markdown
# 📦 tafia/calamine [🔖 PENDING/APPROVE]
🔗 https://github.com/tafia/calamine


## Meta
- **Stars:** ⭐ 2238 | **Forks:** 🍴 220
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A pure Rust Excel/OpenDocument SpreadSheets file reader: rust on metal sheets

## README (trích đầu)
```
# calamine

An Excel/OpenDocument Spreadsheets file reader/deserializer, in pure Rust.

[![GitHub CI Rust tests](https://github.com/tafia/calamine/workflows/Rust/badge.svg)](https://github.com/tafia/calamine/actions)
[![Build status](https://ci.appveyor.com/api/projects/status/njpnhq54h5hxsgel/branch/master?svg=true)](https://ci.appveyor.com/project/tafia/calamine/branch/master)

[Documentation](https://docs.rs/calamine/)

## Description

**calamine** is a pure Rust library to read and deserialize any spreadsheet file:

- excel like (`xls`, `xlsx`, `xlsm`, `xlsb`, `xla`, `xlam`)
- opendocument spreadsheets (`ods`)

As long as your files are *simple enough*, this library should just work.

## Examples

### Serde deserialization

It is as simple as:

```rust
use calamine::{open_workbook, Error, Xlsx, Reader, RangeDeserializerBuilder};

fn example() -> Result<(), Error> {
    let path = format!("{}/tests/temperature.xlsx", env!("CARGO_MANIFEST_DIR"));
    let mut workbook: Xlsx<_> = open_workbook(path)?;
    let range = workbook.worksheet_range("Sheet1")?;


    let mut iter = RangeDeserializerBuilder::new().from_range(&range)?;

    if let Some(result) = iter.next() {
        let (label, value): (String, f64) = result?;
        assert_eq!(label, "celsius");
        assert_eq!(value, 22.2222);
        Ok(())
    } else {
        Err(From::from("expected at least one record but got none"))
    }
}
```

Calamine provides helper functions to deal with invalid type values. For
instance, to deserialize a column which should contain floats but may also
contain invalid values (i.e. strings), you can use the
[`deserialize_as_f64_or_none`](https://docs.rs/calamine/latest/calamine/fn.deserialize_as_f64_or_none.html)
helper function with Serde's
[`deserialize_with`](https://serde.rs/field-attrs.html) field attribute:

```rust
use calamine::{deserialize_as_f64_or_none, open_workbook, RangeDeserializerBuilder, Reader, Xlsx};
use serde::Deserialize;

#[derive(Deserialize)]
struct Record {
    metric: String,
    #[serde(deserialize_with = "deserialize_as_f64_or_none")]
    value: Option<f64>,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let path = format!("{}/tests/excel.xlsx", env!("CARGO_MANIFEST_DIR"));
    let mut excel: Xlsx<_> = open_workbook(path)?;

    let range = excel
        .worksheet_range("Sheet1")
        .map_err(|_| calamine::Error::Msg("Cannot find Sheet1"))?;

    let iter_records =
        RangeDeserializerBuilder::with_headers(&["metric", "value"]).from_range(&range)?;

    for result in iter_records {
        let record: Record = result?;
        println!("metric={:?}, value={:?}", record.metric, record.value);
    }

    Ok(())
}
```

The
[`deserialize_as_f64_or_none`](https://docs.rs/calamine/latest/calamine/fn.deserialize_as_f64_or_none.html)
function discards all invalid values. If instead you would like to return them
as `String`s, you can use the similar
[`deserialize_as_f64_or_string`](https://docs.rs/calamine/latest/
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

