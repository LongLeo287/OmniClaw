---
id: ulid-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:24.560566
---

# KNOWLEDGE EXTRACT: ulid
> **Extracted on:** 2026-03-30 17:56:43
> **Source:** ulid

---

## File: `spec.md`
```markdown
# 📦 ulid/spec [🔖 PENDING/APPROVE]
🔗 https://github.com/ulid/spec


## Meta
- **Stars:** ⭐ 10685 | **Forks:** 🍴 183
- **Language:** N/A | **License:** GPL-3.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The canonical spec for ulid

## README (trích đầu)
```
<h1 align="center">
	<br>
	<br>
	<img width="360" src="logo.png" alt="ulid">
	<br>
	<br>
	<br>
</h1>

# Universally Unique Lexicographically Sortable Identifier

UUID can be suboptimal for many use-cases because:

- It isn't the most character efficient way of encoding 128 bits of randomness
- UUID v1/v2 is impractical in many environments, as it requires access to a unique, stable MAC address
- UUID v3/v5 requires a unique seed and produces randomly distributed IDs, which can cause fragmentation in many data structures
- UUID v4 provides no other information than randomness which can cause fragmentation in many data structures

Instead, herein is proposed ULID:

```javascript
ulid() // 01ARZ3NDEKTSV4RRFFQ69G5FAV
```

- 128-bit compatibility with UUID
- 1.21e+24 unique ULIDs per millisecond
- Lexicographically sortable!
- Canonically encoded as a 26 character string, as opposed to the 36 character UUID
- Uses Crockford's base32 for better efficiency and readability (5 bits per character)
- Case insensitive
- No special characters (URL safe)
- Monotonic sort order (correctly detects and handles the same millisecond)

## Implementations in other languages

From ourselves and the community!

| Language | Author | Binary Implementation |
| -------- | ------ | --------------------- |
| [C++](https://github.com/suyash/ulid) | [suyash](https://github.com/suyash) | ✓ |
| [C#](https://github.com/mcb2001/CSharp.Ulid) | [mcb2001](https://github.com/mcb2001) |
| [Clojure](https://github.com/theikkila/clj-ulid) | [theikkila](https://github.com/theikkila) |
| [Objective-C](https://github.com/whitesmith/ulid) | [ricardopereira](https://github.com/ricardopereira) |
| [Crystal](https://github.com/SuperPaintman/ulid) | [SuperPaintman](https://github.com/SuperPaintman) |
| [Dart](https://github.com/agilord/ulid) | [isoos](https://github.com/isoos) | ✓ |
| [Dart](https://github.com/GuepardoApps/d-ulid) | [GuepardoApps](https://github.com/GuepardoApps) |
| [Delphi](https://github.com/martinusso/ulid) | [matinusso](https://github.com/martinusso) |
| [D](https://github.com/enckse/ulid) | [enckse](https://github.com/enckse) |
| [D (dub)](https://code.dlang.org/packages/ulid-d) | [extrawurst](https://github.com/Extrawurst)
| [Erlang](https://github.com/savonarola/ulid) | [savonarola](https://github.com/savonarola) |
| [Elixir](https://github.com/Homepolish/ulid) | [Homepolish](https://github.com/Homepolish) | ✓ |
| [Elixir](https://github.com/merongivian/ulid) | [merongivian](https://github.com/merongivian) |
| [Elixir](https://github.com/omisego/ex_ulid) | [omisego](https://github.com/omisego) | ✓ |
| [Elixir (Ecto)](https://github.com/TheRealReal/ecto-ulid) | [dcuddeback](https://github.com/dcuddeback) | ✓ |
| [F#](https://github.com/lucasschejtman/FSharp.Ulid) | [lucasschejtman](https://github.com/lucasschejtman) |
| [Factor](https://github.com/AlexIljin/ulid) | [Alexander Ilin](https://github.com/AlexIljin) | ✓ |
| [Go](https://github.com/oklog/ulid) | [oklog](https:
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

