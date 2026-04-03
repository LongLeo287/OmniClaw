---
id: ridiculousfish-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:09.433177
---

# KNOWLEDGE EXTRACT: ridiculousfish
> **Extracted on:** 2026-03-30 17:53:00
> **Source:** ridiculousfish

---

## File: `widecharwidth.md`
```markdown
# 📦 ridiculousfish/widecharwidth [🔖 PENDING/APPROVE]
🔗 https://github.com/ridiculousfish/widecharwidth


## Meta
- **Stars:** ⭐ 71 | **Forks:** 🍴 15
- **Language:** Python | **License:** NOASSERTION
- **Last updated:** 2026-01-22
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
public domain wcwidth implementation

## README (trích đầu)
```
widecharwidth is a Python script that outputs implementations of `wcwidth()`, by downloading and parsing the latest `UnicodeData.txt`, `EastAsianWidth.txt`, and `emoji-data.txt`. Currently it generates code for:

- C++
- JavaScript
- Python
- Rust
- Java

## C++ Usage

You may directly copy and use the included `widechar_width.h`.

This header contains a single public function `widechar_wcwidth()`. This returns either a positive width value (1 or 2), or a negative value such as `widechar_private_use`. Note that there are several possible negative return values, to distinguish among different scenarios.

If you aren't sure how to handle negative return values, try this table:

| return value             | width                              |
|--------------------------|------------------------------------|
| `widechar_nonprint`      | 0                                  |
| `widechar_combining`     | 0                                  |
| `widechar_ambiguous`     | 1                                  |
| `widechar_private_use`   | 1                                  |
| `widechar_unassigned`    | 0                                  |
| `widechar_non_character` | 0                                  |
| `widechar_widened_in_9`  | 2 (or maybe 1, renderer dependent) |

## C Usage

You may directly copy and use the included `widechar_width_c.h`.  Usage is otherwise the same as for C++.

## JavaScript usage

The JS file `widechar_width.js` contains the function `widechar_wcwidth()`. This behaves the same as the C++ version.

## Python usage

`widechar_width.py` contains the function `wcwidth` that returns either an int or a member of the `Special` Enum.

The values are the same as the other implementations, so you can compare them as int, or you can use it as an enum.

`wcwidth` takes either a string consisting of exactly one codepoint or an int representing the codepoint (like you would get via `ord("f")`).

```python
from widechar_width import wcwidth, Special

width = wcwidth(c)
# wcwidth returns an int for normal codepoints with a specific width
if isinstance(width, int):
    return width
# and one of the "Special" values otherwise.
elif width == Special.ambiguous or width == Special.private_use:
    return 1
elif width == Special.widened_in_9:
    return 2
```

The generated script should work with python 3.5+.

## Rust usage

In Rust, use `widechar_width.rs` and match `WcWidth::from_char()`. Example:

```rust
match WcWidth::from_char(c) {
    WcWidth::One | WcWidth::Two => (), // width 1 or 2
    WcWidth::Combining => (),          // zero-width combiner
    WcWidth::NonPrint => (),           // non-printing
    ...
}
```

## Java usage

For Java 8+, file `widechar_width.java` contains the `WcWidth` class definition, which you can use as follows:

```java
int width = WcWidth.Type.of(codePoint).defaultWidth();
```

The default values are based on the recommendations in the table of the C++ above.
If you need a different width for some types, create your 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

