---
id: distil-labs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:20.323388
---

# KNOWLEDGE EXTRACT: distil-labs
> **Extracted on:** 2026-03-30 17:35:58
> **Source:** distil-labs

---

## File: `distil-text2sql.md`
```markdown
# 📦 distil-labs/distil-text2sql [🔖 PENDING/APPROVE]
🔗 https://github.com/distil-labs/distil-text2sql


## Meta
- **Stars:** ⭐ 266 | **Forks:** 🍴 20
- **Language:** Python | **License:** Unknown
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Query your data in plain English with a fine-tuned Text2SQL model

## README (trích đầu)
```
# Text2SQirreL 🐿️ : **Query your data in plain English**

![text2sql-logo.png](text2sql-logo.png)

*Turn natural language questions into SQL queries with a small, local model that matches cloud LLM accuracy.*

We fine-tuned a small language model to convert plain English questions into executable SQL queries. Because it's small, you can run it locally on your own machine, no API keys, no cloud dependencies, full privacy. Load your CSV files, ask questions, get answers.

| Model | Parameters | LLM-as-a-Judge | Exact Match | Model Link |
| --- | --- | --- | --- | --- |
| DeepSeek-V3 (teacher) | 685B | 80% | 48% | |
| **Qwen3-4B (tuned)** | **4B** | **80%** | **60%** | [huggingface](https://huggingface.co/distil-labs/distil-qwen3-4b-text2sql) |
| **Qwen3-0.6B (tuned)** | **0.6B** | **74%** | **40%** | [huggingface](https://huggingface.co/distil-labs/distil-qwen3-0.6b-text2sql) |
| Qwen3-4B (base) | 4B | 62% | 16% | |
| Qwen3-0.6B (base) | 0.6B | 36% | 24% | |

The tuned 4B model **matches the 685B teacher** on LLM-as-a-Judge accuracy and **exceeds it on exact match** while being **170x smaller**. The 0.6B model achieves **74% accuracy** with a **2x improvement** over its base model - ideal for edge deployment. 


## Quick Start

### 1. Install Ollama

Install [Ollama](https://ollama.com/) following the instructions on their website.

### 2. Set up the environment

```bash
python -m venv .venv
. .venv/bin/activate
pip install huggingface_hub openai pandas
```

### 3. Download and build the model

```bash
# Download the 4-bit quantized model (recommended, ~2.5GB)
huggingface-cli download distil-labs/distil-qwen3-4b-text2sql-gguf-4bit --local-dir distil-model
cd distil-model
ollama create distil-qwen3-4b-text2sql -f Modelfile
cd ..
```

### 4. Run Text2SQL

```bash
python app.py --csv example_data/employees.csv \
  --question "How many employees are in each department?"
```


## Usage Examples

Text2SQL loads your CSV data, converts your question to SQL, executes it, and returns the results. Use `--show-sql` to see the generated query.

### Single table queries

```bash
> python app.py --csv example_data/employees.csv \
    --question "How many employees are in each department?" --show-sql

Generated SQL: SELECT department, COUNT(*) FROM employees GROUP BY department;

 department  COUNT(*)
Engineering         4
  Marketing         3
      Sales         3
```


### Multi-table queries (JOINs)


```bash
> python app.py --csv example_data/employees.csv --csv example_data/projects.csv \
    --question "What is the total project budget per employee?" --show-sql

Generated SQL: SELECT e.name, SUM(p.budget) FROM employees e JOIN projects p ON e.id = p.lead_id GROUP BY e.name;

          name  SUM(p.budget)
 Alice Johnson          50000
     Bob Smith          45000
Carol Williams         120000
   David Brown          35000
    Henry Chen          80000
```


## How We Trained Text2SQL
### The Problem

Asking questions about data shouldn't require knowing SQ
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

