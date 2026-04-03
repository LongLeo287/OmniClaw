---
id: ticki-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.144837
---

# KNOWLEDGE EXTRACT: ticki
> **Extracted on:** 2026-03-30 17:54:17
> **Source:** ticki

---

## File: `eudex.md`
```markdown
# 📦 ticki/eudex [🔖 PENDING/APPROVE]
🔗 https://github.com/ticki/eudex


## Meta
- **Stars:** ⭐ 221 | **Forks:** 🍴 11
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-15
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A blazingly fast phonetic reduction/hashing algorithm.

## README (trích đầu)
```
# Eudex: A blazingly fast phonetic reduction/hashing algorithm.

Eudex (_[juːˈdɛks]_) is a Soundex-esque phonetic reduction/hashing algorithm,
providing locality sensitive "hashes" of words, based on the spelling and
pronunciation.

It is derived from the classification of the pulmonic consonants (see below).

Eudex is about two orders of magnitude faster than Soundex, and several orders
of magnitude faster than Levenshtein distance, making it feasible to run on
large sets of strings in very short time.

[Documentation.](https://docs.rs/crate/eudex)

## Features

- High quality locality-sensitive hashing based on pronunciation.
- Works with, but not limited to, English, Catalan, German, Spanish, Italian,
  and Swedish.
- Sophisticated phonetic mapping.
- Better quality than Soundex.
- Takes non-english letters into account.
- Extremely fast.
- Algorithm specified (see the section below).
- Vowel sensitive.

## FAQ

**Why aren't Rupert and Robert mapped to the same value, like in Soundex?**
Eudex is not a phonetic classifier, it is a phonetic hasher. It maps words in a
manner that exposes the difference. Soundex doesn't give any form of nuanced
measure, only "Similar" and "Not similar".

**The results seems completely random. What is wrong?** It is likely because
you assume that the hashes of similar sounding words are mapped near to each
other, while they don't. Instead, their Hamming distance (i.e. XOR the values
and sum their bits) will be low. `distance` now accounts for this.

**I am concerned about stability. Can the values vary?**. Yes! You are
encouraged to either specify the revision to Cargo, giving you complete
stability, or use the `similar` function, whose fundamental behavior won't
change.

**Does it support non-English letters?** Yes, it supports all the C1 letters
(e.g., ü, ö, æ, ß, é and so on), and it takes their respective sound into
account.

**Is it English-only?** No, it works on most European languages as well.
However, it is limited to the Latin alphabet.

**How does it work?** It is described below.

**Does it take digraphs into account?** The table is designed to encapsulate
digraphs as well, though there is no separate table for these (like in
Metaphone).

**Does it replace Levenshtein?** It is _not_ a replacement for Levenshtein
distance, it is a replacement for Levenshtein distance in certain use cases,
e.g. searching for spell check suggestions.

**What languages is it tested for?**  It is tested on the English, Catalan,
German, Spanish, Swedish, and Italian dictionaries, and has been confirmed to
have decent to good quality on all of them.

**It seem to limited the hash to 8 or 16 characters?** It doesn't have such a
limitation, however the hash will only be affected by the first N characters,
due to platform and performance considerations. It turns out that it has little
to no effect on the quality. Moreover, this limitation is not a part of the
algorithm itself, but this implementation of the algorithm.

## Impleme
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

