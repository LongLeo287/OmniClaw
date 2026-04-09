# OmniClaw Repo Plow: CIV_FETCHED_citation-check-skill_000652



================================================
FILE: README.md
================================================
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



================================================
FILE: SKILL.md
================================================
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
[C04

================================================
FILE: references\citation_schema.json
================================================
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
