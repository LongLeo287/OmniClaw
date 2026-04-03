---
id: github.com-serenakeyitan-citation-check-skill-c9fb
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:20.537645
---

# KNOWLEDGE EXTRACT: github.com_serenakeyitan_citation-check-skill_c9fb91fe
> **Extracted on:** 2026-04-01 09:43:47
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520395/github.com_serenakeyitan_citation-check-skill_c9fb91fe

---

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Serena

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
# Citation Check v2

> No citation → no output.

Citation Check is a small, opinionated module for **detecting and blocking hallucinated or missing citations** in LLM outputs.

Built for research, slides, and agent pipelines where correctness matters.

---
## Demo - Identified Issues

### TRY [Kael.im](https://kael.im/home)(NotebookLM slides alternative) and register at this link for 100 pages free daily quota (nbp)!
https://github.com/user-attachments/assets/99d427cf-992f-455c-897b-a8f8a132271c


<img width="1219" height="713" alt="Screenshot 2026-01-25 at 13 56 07" src="https://github.com/user-attachments/assets/660592cd-ca53-46ae-8064-28fad9e90b44" />

### Check out [Awesome Notebooklm Slides Prompts List](https://github.com/serenakeyitan/awesome-notebookLM-prompts/tree/main) with all viral templates on X!
## How to Use?
1. Download `citation-check-skill.zip` from [Releases](https://github.com/serenakeyitan/citation-check-skill/releases/latest)
2. Upload it to Claude Code (Profile → Settings → Capabilities → Skills → Add)
3. Use it by telling Claude: "use citation checker" or "use skills"

**Note:** Don't use the "Code → Download ZIP" button - it adds `-main` to the folder name. Always download from Releases!
## What it does

- ✅ Checks that every factual claim has a citation  
- ✅ Verifies that cited sources actually exist  
- ✅ Validates claim–citation consistency (exact numbers, not rounded)
- ✅ Supports vision: reads slides, PDFs, charts, tables
- ✅ Two modes: web search verification OR doc-only verification

If a check fails, the output should be blocked or regenerated.

---

## Why

Most tools add citations *after* generation.  
This enforces citations as a **generation constraint**.

If your agent can't cite a claim, it shouldn't make it.

---

## v2.0 — Consistency Update

Same input → Same output. Key changes:

| Feature                        | What it does                                                 |
| ------------------------------ | ------------------------------------------------------------ |
| **Two-Pass Architecture**      | Extract all claims first, then verify. No more inconsistent results. |
| **Claim Extraction Rules**     | Explicit taxonomy — statistics, comparatives, attributions, etc. |
| **Status Decision Tree**       | Deterministic classification: Verified → Numerical Error → Hallucination |
| **Academic Precision Mode**    | 96.555% ≠ 97%. Exact numbers only.                           |
| **Mandatory Search Templates** | Runs ALL query patterns, not ad-hoc searches                 |
| **Tie-Breaker Rules**          | No judgment calls on edge cases                              |

---

## Typical flow

```text
LLM output (slides / report / PDF)
↓
Pass 1: Extract all claims
↓
Pass 2: Verify each claim
↓
pass → ship
fail → regenerate / fix
```

---

## Two Modes

### Mode 1: Search Verification (default)

- Searches web for authoritative sources
- Validates citations actually exist
- Checks if cited sources say what's claimed

### Mode 2: Doc-Only Verification

- User provides source document(s)
- EVERYTHING must trace to those docs
- Flags any external knowledge as hallucination

Trigger doc-only mode with: *"only use this document"* / *"verify against the PDF only"*

---

## Status Classifications

| Status               | Meaning                                               |
| -------------------- | ----------------------------------------------------- |
| ✅ Verified           | Exact match with source                               |
| ⚠️ Numerical Error    | Values don't match (e.g., 97% vs 96.555%)             |
| ⚠️ Unverified         | No authoritative source found                         |
| ❌ Hallucination      | Contradicts source or fabricated                      |
| ❌ Misleading         | Cherry-picked or missing context                      |
| ❌ Citation Not Found | Referenced paper/report doesn't exist                 |
| ❌ Not in Source      | Claim can't be traced to provided doc (doc-only mode) |

---

## Installation

It's a Claude / ChatGPT skill. 

- **Claude:** [Agent Skills Documentation](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview)
- **ChatGPT:** [Codex Skills](https://developers.openai.com/codex/skills)

---

## License

MIT

```

## File: `SKILL.md`
```markdown
---
name: citation-check-skill

description: Vision-enabled verification gate with web search. Use when users want to (1) verify slides/reports/PDFs/images against authoritative online sources, (2) validate that citations actually exist and say what's claimed, (3) check charts/graphs/tables for accuracy, (4) audit AI-generated content in doc-only mode (no external knowledge). Two modes - search mode validates against web, doc-only mode ensures everything traces to provided documents. Supports content in any language.

---

# Citation & Hallucination Checker v2

Verification tool with vision + web search. Validates every claim against authoritative sources or provided documents. Works with content in any language.

**Design principle:** Deterministic verification. Same input → Same output.

---

## Two Verification Modes

### Mode 1: Search Verification (Default)

- Searches web for authoritative sources
- Validates citations actually exist
- Checks if cited sources say what's claimed
- Finds original data for statistics

### Mode 2: Doc-Only Verification

- User provides source document(s)
- EVERYTHING must trace to those docs
- Flags anything that appears to come from external knowledge
- Trigger: "only use this document" / "verify against the PDF only" / "don't search the web"

---

## Two-Pass Architecture

**Critical:** Always use two separate passes. Never interleave extraction and verification.

### Pass 1: Extraction Only

1. Read entire document/slides/images
2. Extract ALL claims using the Claim Extraction Rules below
3. Output numbered list: `[claim_id] | [claim_text] | [claim_type] | [location]`
4. **NO verification in this pass**
5. Present extraction to user for confirmation before proceeding

### Pass 2: Verification Only

1. Take Pass 1 output as fixed input
2. Verify each claim_id in sequential order
3. **NO re-extraction allowed** — work only with Pass 1 claims
4. Apply Status Decision Tree to each claim
5. Generate final report

This prevents "discovering new claims" mid-verification and ensures consistency.

---

## Claim Extraction Rules (Exhaustive)

Extract ONLY these claim types. Apply rules strictly — no judgment calls.

### EXTRACT as claims:

| Type            | Pattern                                                    | Example                                          |
| --------------- | ---------------------------------------------------------- | ------------------------------------------------ |
| **Statistic**   | Any number with unit/context (%, $, count, ratio, decimal) | "92.3% accuracy", "$4.7B market"                 |
| **Comparative** | X is [comparative] than Y                                  | "3x faster than baseline"                        |
| **Temporal**    | Time-bound assertion                                       | "In 2024, adoption reached..."                   |
| **Attribution** | Claim tied to source                                       | "According to WHO...", "Smith et al. found..."   |
| **Causal**      | X causes/leads to/results in Y                             | "This reduces latency by..."                     |
| **Existence**   | Asserts something exists/is true                           | "There are 500M users", "The model supports..."  |
| **Ranking**     | Position claims                                            | "largest", "first", "top 3"                      |
| **Quote**       | Direct quotation                                           | Any text in quotation marks attributed to source |

### DO NOT extract as claims:

| Type                              | Example                                            | Reason                          |
| --------------------------------- | -------------------------------------------------- | ------------------------------- |
| Definitions                       | "Machine learning is a subset of AI"               | Definitional, not factual claim |
| Opinions marked as such           | "We believe...", "In our view..."                  | Explicitly subjective           |
| Hypotheticals                     | "If adoption continues...", "Could potentially..." | Speculative                     |
| Questions                         | "What drives growth?"                              | Not an assertion                |
| Future predictions without source | "Will reach $10B by 2030"                          | Unless citing a forecast report |
| Methodology descriptions          | "We used PyTorch 2.0"                              | Process, not factual claim      |
| Acknowledgments                   | "Thanks to our collaborators"                      | Not verifiable                  |

### Extraction Output Format

```
[C01] | "Model achieves 96.555% accuracy on ImageNet" | Statistic | Slide 3, bullet 2
[C02] | "Outperforms GPT-4 by 12% on reasoning tasks" | Comparative | Slide 3, bullet 3
[C03] | "According to Chen et al. (2024), transformers scale linearly" | Attribution | Slide 5, para 1
[C04] | "Market size reached $4.7B in 2024" | Statistic + Temporal | Slide 7, chart title
```

---

## Status Decision Tree

Apply this tree to EVERY claim. Follow exactly — no shortcuts.

```
START
│
├─ Is this a CITATION claim (references a paper/report/source)?
│   ├─ YES → Go to CITATION VALIDATION
│   └─ NO → Go to STATISTIC/FACT VALIDATION
│
│
CITATION VALIDATION
│
├─ Step 1: Does the cited source exist?
│   │   Run ALL mandatory search queries (see Search Templates)
│   │
│   ├─ NO → Status: "Citation Not Found"
│   │        Issue: "Cannot locate [citation] in any database"
│   │        STOP
│   │
│   └─ YES → Step 2: Does source contain the claimed topic?
│             │
│             ├─ NO → Status: "Misquoted"
│             │        Issue: "Source exists but does not discuss [topic]"
│             │        STOP
│             │
│             └─ YES → Step 3: Does source support the exact claim?
│                       │
│                       ├─ YES (exact match) → Status: "Verified"
│                       │                       Confidence: "exact"
│                       │
│                       ├─ YES (paraphrase, same meaning) → Status: "Verified"
│                       │                                   Confidence: "paraphrase"
│                       │
│                       ├─ PARTIALLY (missing context) → Status: "Misleading"
│                       │   Issue: "Claim omits critical context: [what's missing]"
│                       │
│                       └─ NO (contradicts) → Status: "Hallucination"
│                           Issue: "Source says [X], claim says [Y]"
│
│
STATISTIC/FACT VALIDATION
│
├─ Step 1: Can you find an authoritative source?
│   │   Run ALL mandatory search queries (see Search Templates)
│   │
│   ├─ NO (no source found) → Status: "Unverified"
│   │                          Issue: "No authoritative source found"
│   │                          STOP
│   │
│   └─ YES → Step 2: Do values match EXACTLY?
│             │
│             ├─ YES → Status: "Verified"
│             │         Confidence: "exact"
│             │         STOP
│             │
│             └─ NO → Status: "Numerical Error"
│                      Go to NUMERICAL ERROR DETAILS
│
│
NUMERICAL ERROR DETAILS (Academic Precision Mode)
│
├─ Record:
│   • Source value: [exact number from source]
│   • Claimed value: [number in document being checked]
│   • Deviation: [calculate exact difference]
│   • Source location: [page, table, section]
│
├─ Classification:
│   • ANY rounding → Numerical Error
│   • ANY truncation → Numerical Error  
│   • Significant figures mismatch → Numerical Error
│   • Unit mismatch → Numerical Error
│   • Wrong direction (e.g., increase vs decrease) → Hallucination
│
└─ Exception: If source ITSELF provides rounded figure
    • e.g., Source says "96.555% (approximately 97%)"
    • Then claiming "97%" → Verified (cite the approximation)
```

---

## Numerical Precision Rules (Academic Standard)

**Default mode: Strict academic precision. Exact numbers only.**

| Rule                 | Source      | Claim       | Status            |
| -------------------- | ----------- | ----------- | ----------------- |
| Exact match required | 96.555%     | 96.555%     | ✓ Verified        |
| Any rounding = error | 96.555%     | 97%         | ✗ Numerical Error |
| Any rounding = error | 96.555%     | 96.6%       | ✗ Numerical Error |
| Truncation = error   | 96.555%     | 96.5%       | ✗ Numerical Error |
| Sig figs must match  | 0.834       | 0.83        | ✗ Numerical Error |
| Units must match     | 96.555%     | 0.96555     | ✗ Numerical Error |
| Direction matters    | +12% growth | +15% growth | ✗ Hallucination   |
| Order of magnitude   | $4.7B       | $47B        | ✗ Hallucination   |

### Numerical Error Output Format

```markdown
### Numerical Error: [Claim ID]

| Field | Value |
|-------|-------|
| Claim | "Model achieves 97% accuracy" |
| Location | Slide 4, bullet 2 |
| Source | Chen et al. (2024), Table 3, p.8 |
| Source value | 96.555% |
| Claimed value | 97% |
| Deviation | +0.445% (rounded up) |
| Status | Numerical Error |
| Fix | Replace with: "Model achieves 96.555% accuracy" |
```

---

## Confidence Classification

| Level              | Criteria                                                   | Use when                            |
| ------------------ | ---------------------------------------------------------- | ----------------------------------- |
| **exact**          | ≥95% word overlap OR identical number with identical units | Direct quote, exact statistic       |
| **paraphrase**     | Same fact, different words, no interpretation added        | Restated finding                    |
| **interpretation** | Inference drawn from source data                           | Calculated from source, synthesized |

**Rule:** When uncertain between levels, use the MORE CONSERVATIVE option and flag for review.

---

## Mandatory Search Templates

Run ALL applicable templates. Do not stop after first result.

### For Academic Citations

```
Query 1: "[first author last name] [year] [first 3 words of title]"
Query 2: "[full paper title]" site:semanticscholar.org OR site:arxiv.org
Query 3: "[first author] [year] [venue/journal name]"
Query 4: "doi:[DOI]" (if DOI provided)
Query 5: "arxiv:[arxiv_id]" (if arXiv ID provided)
```

### For Statistics (Market size, usage numbers, etc.)

```
Query 1: "[exact number with unit] [topic] [year]"
Query 2: "[topic] [year] statistics report site:statista.com"
Query 3: "[topic] [year] report site:mckinsey.com OR site:gartner.com"
Query 4: "[topic] market size [year] site:gov OR site:edu"
Query 5: "[topic] [number] original source"
```

### For Company/Product Claims

```
Query 1: "[company name] [claim topic] press release [year]"
Query 2: site:[company domain] [claim topic]
Query 3: "[company name] [metric] official announcement"
Query 4: "[company name] [claim] SEC filing" (for public companies)
```

### For Health/Medical Claims

```
Query 1: "[claim topic] site:who.int OR site:cdc.gov OR site:nih.gov"
Query 2: "[claim] systematic review site:cochrane.org"
Query 3: "[claim] meta-analysis pubmed"
```

### For Government/Policy Claims

```
Query 1: "[policy/law name] site:gov"
Query 2: "[statistic] official statistics [country]"
Query 3: "[claim] [agency name] report"
```

---

## Source Authority Hierarchy

When multiple sources found, prefer in this order:

| Rank | Source Type                   | Examples                                          |
| ---- | ----------------------------- | ------------------------------------------------- |
| 1    | Primary source                | Original study, official report, raw data         |
| 2    | Government/institutional      | WHO, CDC, World Bank, national statistics offices |
| 3    | Peer-reviewed publication     | Nature, Science, IEEE, ACM                        |
| 4    | Industry reports (named)      | Gartner, McKinsey, Statista (with methodology)    |
| 5    | Reputable news citing primary | NYT, Reuters citing original source               |
| 6    | Secondary compilations        | Wikipedia (check their sources)                   |

**Rule:** If only Rank 5-6 sources found, status = "Unverified" with note "Only secondary sources found"

---

## Multi-Source Verification (Search Mode)

A claim achieves "Verified" status only if:

| Condition              | Sources Required                                    |
| ---------------------- | --------------------------------------------------- |
| Primary source found   | 1 (if authoritative: .gov, peer-reviewed, official) |
| Only secondary sources | ≥2 independent sources agreeing                     |
| Sources conflict       | Status = "Unverified", note the conflict            |

---

## Tie-Breaker Rules

When uncertain, apply these rules. No judgment calls.

| Situation                                 | Rule                                                         |
| ----------------------------------------- | ------------------------------------------------------------ |
| Missing date on claim                     | Assume refers to most recent year available; flag "needs date" |
| Conflicting sources                       | Use most recent authoritative source; cite both; note conflict |
| Source not found after all queries        | Status = "Unverified" (NOT "Hallucination")                  |
| Number differs due to currency conversion | Flag as "Needs clarification: currency/units"                |
| Same org, multiple reports                | Use most recent; cite with date                              |
| Claim uses "approximately" or "about"     | Still verify base number is in valid range (±10% of source)  |
| Source is paywalled                       | Note "Source behind paywall, unable to verify exact text"    |
| Source is in different language           | Translate and verify; note translation                       |

---

## Visual Data Verification

For every chart, graph, table, or diagram:

### Step 1: Extract Data Points

- Read ALL values from the visual
- Record: axis labels, units, scale, legend
- Note any visual distortions (truncated axes, 3D effects, etc.)

### Step 2: Find Source

- Search mode: Run search templates for the data
- Doc-only mode: Locate in source document

### Step 3: Compare Value-by-Value

```markdown
| Visual Element | Extracted Value | Source Value | Status |
|----------------|-----------------|--------------|--------|
| Bar 1 (2022) | 45% | 45.0% | ✓ Verified |
| Bar 2 (2023) | 62% | 58.3% | ✗ Numerical Error |
| Bar 3 (2024) | 78% | Not in source | ✗ Hallucination |
```

### Step 4: Check Visual Integrity

| Check                                   | Issue Type                             |
| --------------------------------------- | -------------------------------------- |
| Y-axis starts at non-zero               | "Visual Distortion: axis manipulation" |
| 3D effects distort proportions          | "Visual Distortion: 3D exaggeration"   |
| Missing error bars when source has them | "Misleading: uncertainty omitted"      |
| Different time ranges than source       | "Misleading: cherry-picked timeframe"  |

---

## Doc-Only Mode Workflow

**Trigger phrases:**

- "only use this document"
- "don't search the web"
- "verify against the PDF only"
- "everything should be from the source"

### Step 1: Index Source Document

Build complete index before any verification:

```
SOURCE INDEX
Document: [filename]
Pages: [count]

Page 1:
- Text: [summary of content]
- Statistics: [list all numbers with context]
- Tables: [Table 1: columns X, Y, Z]
- Figures: [Figure 1: shows X]

Page 2:
...
```

### Step 2: Apply Two-Pass Architecture

Same as search mode, but verification uses ONLY the source index.

### Step 3: Trace Each Claim

```
Claim: [C01] "Model achieves 92% accuracy"
Search index for: "92", "accuracy", "performance"
├─ Found: Section 4.2, p.8 — "Our model achieves 92.1% accuracy"
│   └─ Status: Numerical Error (92% vs 92.1%)
│
OR
│
├─ Not found in index
│   └─ Status: "Not in Source"
│       Issue: "This claim cannot be traced to the provided document"
│       Likely: External knowledge / hallucination
```

### Step 4: Flag ALL External Knowledge

In doc-only mode, ANY claim not traceable to source = problem

```markdown
### External Knowledge Detected

These claims are NOT in the provided document:

| Claim ID | Claim | Status | Issue |
|----------|-------|--------|-------|
| C07 | "This method is widely adopted in industry" | Not in Source | Appears to be from model training data |
| C12 | "Published in Nature 2024" | Not in Source | Publication venue not mentioned in source |
```

---

## Output Format

### Summary Block (Always First)

```markdown
## Verification Report

**Mode:** [Search / Doc-Only]
**Document:** [filename or description]
**Generated:** [timestamp]

### Summary
| Metric | Count |
|--------|-------|
| Total claims extracted | X |
| Verified | Y |
| Numerical Error | Z |
| Unverified | A |
| Hallucination | B |
| Misleading | C |
| Not in Source (doc-only) | D |

**Overall Status:** [PASS: All verified / FAIL: Issues found]
```

### Detailed Findings (Grouped by Status)

```markdown
### ✓ Verified Claims (N)

| ID | Claim | Source | Location | Confidence |
|----|-------|--------|----------|------------|
| C01 | "92.1% accuracy" | Chen et al. 2024 | Table 3, p.8 | exact |

### ✗ Numerical Errors (N)

| ID | Claim | Source Value | Claimed Value | Deviation | Fix |
|----|-------|--------------|---------------|-----------|-----|
| C03 | "97% accuracy" | 96.555% | 97% | +0.445% | Use 96.555% |

### ✗ Hallucinations (N)

| ID | Claim | Issue | Source Says |
|----|-------|-------|-------------|
| C05 | "3x faster" | Contradicts source | Source: 2.1x faster |

### ⚠ Unverified (N)

| ID | Claim | Issue |
|----|-------|-------|
| C08 | "$50B market" | No authoritative source found |

### ⚠ Misleading (N)

| ID | Claim | Issue | Missing Context |
|----|-------|-------|-----------------|
| C10 | "Best performance" | Cherry-picked metric | Only on subset; overall performance lower |
```

### Sources Consulted

```markdown
### Sources

| ID | Citation | Type | URL | Used For |
|----|----------|------|-----|----------|
| S1 | Chen et al. (2024) | arxiv | https://arxiv.org/... | C01, C02, C03 |
| S2 | Statista Market Report | report | https://statista.com/... | C08 |
```

---

## Critical Rules

1. **Two-pass always** — Extract first, verify second. Never interleave.
2. **Every claim gets checked** — No exceptions, no skipping "obvious" ones.
3. **Exact numbers only** — 96.555% ≠ 97% in academic mode.
4. **Find the origin** — Don't accept secondary sources citing unknown primaries.
5. **Run ALL search templates** — Don't stop after first result.
6. **Citations must be real** — Search to confirm papers/reports exist.
7. **Check what sources actually say** — A real paper can still be misquoted.
8. **In doc-only mode, flag ALL external knowledge** — Even if it's true.
9. **When uncertain, be conservative** — "Unverified" is safer than false "Verified".
10. **Follow tie-breaker rules** — No ad-hoc judgment calls.

---

## Language Support

- Accepts content in any language
- Searches in the appropriate language for sources
- Reports in the same language as user's request
- Cross-language verification supported (e.g., Chinese slides citing English papers)
- When translating for verification, note: "Translated from [language]"

---

## Output Format Options

**Quick:** Summary + critical issues only (Numerical Errors, Hallucinations, Unverified)
**Full:** Complete traceability report with all claims
**JSON:** Machine-readable audit (see references/citation_schema.json)

---

## Changelog

**v2.0** — Consistency update

- Added Two-Pass Architecture (extract → verify separation)
- Added exhaustive Claim Extraction Rules
- Added Status Decision Tree (deterministic classification)
- Added strict Numerical Precision Rules (academic mode)
- Added Mandatory Search Templates
- Added Multi-Source Verification requirements
- Added Tie-Breaker Rules for edge cases
- Added Confidence Classification thresholds
```

## File: `references/citation_schema.json`
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Citation Map",
  "description": "Traceability map linking slide claims to source documents",
  "type": "object",
  "required": ["slides", "sources", "metadata"],
  "properties": {
    "metadata": {
      "type": "object",
      "required": ["generated_at", "total_claims", "verified_count", "unverified_count"],
      "properties": {
        "generated_at": {
          "type": "string",
          "format": "date-time"
        },
        "presentation_title": {
          "type": "string"
        },
        "total_claims": {
          "type": "integer",
          "minimum": 0
        },
        "verified_count": {
          "type": "integer",
          "minimum": 0
        },
        "unverified_count": {
          "type": "integer",
          "minimum": 0,
          "description": "Should be 0 for valid output"
        },
        "hallucination_count": {
          "type": "integer",
          "minimum": 0,
          "description": "Only populated in audit mode"
        }
      }
    },
    "slides": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["slide_number", "title", "claims"],
        "properties": {
          "slide_number": {
            "type": "integer",
            "minimum": 1
          },
          "title": {
            "type": "string"
          },
          "claims": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["text", "status"],
              "properties": {
                "text": {
                  "type": "string",
                  "description": "The claim as it appears on the slide"
                },
                "status": {
                  "type": "string",
                  "enum": ["verified", "unverified", "hallucination", "misleading"],
                  "description": "Verification status of the claim"
                },
                "citation": {
                  "type": "object",
                  "required": ["source_id", "location"],
                  "properties": {
                    "source_id": {
                      "type": "string",
                      "description": "Reference to sources object key"
                    },
                    "location": {
                      "type": "string",
                      "description": "Specific location: 'Section X.Y, p.Z, para.N' or 'Table X, p.Y'"
                    },
                    "quote": {
                      "type": "string",
                      "description": "Exact supporting text from source (max 100 chars)"
                    },
                    "confidence": {
                      "type": "string",
                      "enum": ["exact", "paraphrase", "interpretation"],
                      "description": "How closely the claim matches the source"
                    }
                  }
                },
                "issue": {
                  "type": "string",
                  "description": "Description of problem (for non-verified claims)"
                },
                "suggested_fix": {
                  "type": "string",
                  "description": "Recommended correction with proper citation"
                }
              }
            }
          },
          "visuals": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string",
                  "enum": ["figure", "table", "chart", "diagram"]
                },
                "source_ref": {
                  "type": "string",
                  "description": "e.g., 'Figure 3, paper_1, p.8'"
                },
                "status": {
                  "type": "string",
                  "enum": ["verified", "modified", "unverified"]
                }
              }
            }
          }
        }
      }
    },
    "sources": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "required": ["title", "type"],
        "properties": {
          "title": {
            "type": "string"
          },
          "authors": {
            "type": "array",
            "items": {"type": "string"}
          },
          "year": {
            "type": "integer"
          },
          "type": {
            "type": "string",
            "enum": ["journal", "conference", "arxiv", "report", "book", "website"]
          },
          "url": {
            "type": "string",
            "format": "uri"
          },
          "doi": {
            "type": "string"
          },
          "arxiv_id": {
            "type": "string",
            "pattern": "^\\d{4}\\.\\d{4,5}$"
          }
        }
      }
    }
  }
}
```

