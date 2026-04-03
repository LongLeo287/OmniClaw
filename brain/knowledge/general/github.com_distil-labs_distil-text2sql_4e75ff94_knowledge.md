---
id: github.com-distil-labs-distil-text2sql-4e75ff94-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:44.985792
---

# KNOWLEDGE EXTRACT: github.com_distil-labs_distil-text2sql_4e75ff94
> **Extracted on:** 2026-04-01 13:09:31
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007522313/github.com_distil-labs_distil-text2sql_4e75ff94

---

## File: `.gitignore`
```
# Model files (large, hosted on HuggingFace)
distil-qwen3-4b-text2sql/
distil-qwen3-4b-text2sql-gguf/
distil-qwen3-4b-text2sql-gguf-4bit/
distil-model/
*.gguf
*.safetensors

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
.venv/
venv/
ENV/
env/
.env

# IDE
.idea/
.vscode/
*.swp
*.swo
.DS_Store

# Claude
.claude/

# Misc
*.log
.ipynb_checkpoints/
```

## File: `README.md`
```markdown
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

Asking questions about data shouldn't require knowing SQL. We wanted to build a local assistant that could translate plain English questions into correct SQL queries. The key requirements:

- **Runs locally:** no API calls, works offline, keeps your data private
- **Fast:** responds in under 2 seconds on a laptop
- **Accurate:** matches the quality of much larger cloud models
- **Executes queries:** actually runs the SQL and returns results

This is exactly the kind of narrow, well-defined task where small language models can shine, if properly trained.

### Validating the Base Model Fails

Before investing in training, we needed to confirm that off-the-shelf small models can't already do this. We tested [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) on our test set of 50 Text2SQL queries.

The base model achieved **62% on LLM-as-a-Judge and only 16% exact match**, 
far below usable accuracy. Common failure modes (more in evaluation section 
below):

- Generating invalid SQL syntax
- Using wrong column or table names
- Missing WHERE clauses or JOIN conditions
- Adding unnecessary explanations instead of just the query

This confirmed the task is learnable but not already learned. A perfect candidate for fine-tuning.

### Establishing a Teacher Baseline

Next, we needed a ceiling, how well can a large model do? We tested [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3) with a system prompt explaining the task and output format.

The 685B model achieved **80% on LLM-as-a-Judge**. This became our target: could we get a 4B model to match this performance?

### Defining the Task Format

We use a simple schema + question format for inputs:

```
Schema:
CREATE TABLE employees (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  department TEXT,
  salary INTEGER
);

Question: How many employees earn more than 50000?
```

The model outputs a single SQL query:

```sql
SELECT COUNT(*) FROM employees WHERE salary > 50000;
```


### Training Pipeline

**1. Seed Data:** We wrote ~50 examples covering simple queries, JOINs, aggregations, and subqueries. Available in `finetuning/data/`.

**2. Synthetic Expansion:** Using our [data synthesis pipeline](https://www.distillabs.ai/blog/small-expert-agents-from-10-examples/?utm_source=github&utm_medium=referral&utm_campaign=text2sql), we expanded to **~10,000 training examples** with diverse schemas across e-commerce, HR, healthcare, and other domains.

**3. Fine-tuning:** We chose Qwen3-4B based on our [benchmarking of 12 small language models](https://www.distillabs.ai/blog/we-benchmarked-12-small-language-models-across-8-tasks-to-find-the-best-base-model-for-fine-tuning/?utm_source=github&utm_medium=referral&utm_campaign=text2sql), which showed it offers the best balance of capability and efficiency for fine-tuning. Training config: 4 epochs, full fine-tuning on ~10k examples.

### Results

We evaluate using LLM-as-a-Judge (semantic equivalence), Exact Match, and ROUGE on 50 held-out examples:

| Model | LLM-as-a-Judge | Exact Match | ROUGE |
| --- | --- | --- | --- |
| DeepSeek-V3 (teacher) | 80% | 48% | 87.6% |
| **Qwen3-4B (tuned)** | **80%** | **60%** | **89.5%** |
| **Qwen3-0.6B (tuned)** | **74%** | **40%** | **88.5%** |
| Qwen3-4B (base) | 62% | 16% | 84.2% |
| Qwen3-0.6B (base) | 36% | 24% | 69.3% |

The tuned 4B model matches the 685B teacher on semantic accuracy and actually exceeds it on exact match. The 0.6B model doubles the base model's accuracy while being small enough for mobile and edge deployment. On an M4 MacBook Pro, most queries return in under 2 seconds.

### Qualitative Examples

We compare the base QWEN3-4B with the fine tuned version on a few 
cherry-picked exmaples to showcase the difference
#### Example 1: Missing Aggregation Function

**Schema:**
```sql
CREATE TABLE employees (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  team TEXT,
  base_salary INTEGER,
  bonus INTEGER
);
```

**Question:** What is the total compensation (salary + bonus) per team?

| Model         | Prediction |
|---------------|------------|
| Reference     | `SELECT team, SUM(base_salary + bonus) FROM employees GROUP BY team;` |
| Base qwen3-4b | `SELECT team, (base_salary + bonus) AS total_compensation FROM employees GROUP BY team;` |
| Tuned qwen3-4b| `SELECT team, SUM(base_salary + bonus) FROM employees GROUP BY team;` |

**Analysis:** The base model omitted the `SUM()` aggregate function, returning only an arbitrary row's compensation per team rather than the total. The tuned model correctly applies the aggregation.

#### Example 2: Syntax Error in CASE Expression

**Schema:**
```sql
CREATE TABLE tasks (
  id INTEGER PRIMARY KEY,
  project_id INTEGER,
  title TEXT,
  status TEXT,
  assigned_to INTEGER
);
```

**Question:** What percentage of tasks are completed?

| Model          | Prediction |
|----------------|------------|
| Reference      | `SELECT (COUNT(CASE WHEN status = 'completed' THEN 1 END) * 100.0 / COUNT(*)) FROM tasks;` |
| Base qwen3-4b  | `SELECT (COUNT(CASE WHEN status = 'completed' THEN 1 END. * 100.0) / COUNT(*)) AS percentage_completed FROM tasks;` |
| Tuned qwen3-4b | `SELECT (COUNT(CASE WHEN status = 'completed' THEN 1 END) * 100.0 / COUNT(*)) FROM tasks;` |

**Analysis:** The base model produced invalid SQL with a syntax error (`END.` instead of `END`), causing query execution to fail. The tuned model generates syntactically correct SQL matching the reference.


## Model Variants

We provide multiple model sizes and formats to fit different deployment needs:

### 4B Model (Best Accuracy)

| Model | Format | Size | Use Case |
|-------|--------|------|----------|
| [distil-qwen3-4b-text2sql](https://huggingface.co/distil-labs/distil-qwen3-4b-text2sql) | Safetensors | ~8 GB | Transformers, vLLM, cloud deployment |
| [distil-qwen3-4b-text2sql-gguf](https://huggingface.co/distil-labs/distil-qwen3-4b-text2sql-gguf) | GGUF (F16) | ~15 GB | Ollama, llama.cpp (full precision) |
| [distil-qwen3-4b-text2sql-gguf-4bit](https://huggingface.co/distil-labs/distil-qwen3-4b-text2sql-gguf-4bit) | GGUF (Q4) | **~2.5 GB** | **Recommended for local use** |

### 0.6B Model (Edge/Mobile)

| Model | Format | Size | Use Case |
|-------|--------|------|----------|
| [distil-qwen3-0.6b-text2sql](https://huggingface.co/distil-labs/distil-qwen3-0.6b-text2sql) | Safetensors | ~1.1 GB | Edge deployment, mobile, resource-constrained environments |

For most users, the **4B 4-bit quantized GGUF** is the best choice, it's small enough to run on any laptop while maintaining full accuracy. For edge/mobile deployment where size is critical, the **0.6B model** offers a great balance of accuracy (74% LLM-as-a-Judge) and compactness.


## Train Your Own Model

The workflow we used for Text2SQL is generic across text generation tasks. Here's how to apply it to your own domain:

### 1. Define your task format

Specify the input format (what context the model receives) and output format (what it should generate). Be specific about rules and constraints.

### 2. Create seed examples

Write 50-100 examples covering your task's complexity range. You can use a large model to generate candidates, then validate manually.

### 3. Generate synthetic data

Use the [distillabs.ai](https://distillabs.ai/?utm_source=github&utm_medium=referral&utm_campaign=text2sql) platform to expand your seed data into thousands of training examples.

### 4. Fine-tune

Train a small model (1B-4B parameters work well for narrow tasks) on your synthetic dataset.

### 5. Evaluate

Test on held-out examples. Compare against a large model baseline to know when you've succeeded.

For custom training assistance, visit [distillabs.ai](https://www.distillabs.ai/?utm_source=github&utm_medium=referral&utm_campaign=text2sql) or reach out to us directly.


## FAQ

**Q: Why not just use GPT-4 / Claude for this?**

Because your data shouldn't leave your machine. Text2SQL runs locally, works offline, and keeps your queries and data completely private. Perfect for sensitive business data.

**Q: Why not use Qwen3-4B directly?**

The base model only achieves 62% accuracy on LLM-as-a-Judge and 16% exact match, it frequently generates invalid SQL or uses wrong column names. Fine-tuning is essential.

**Q: What databases does this support?**

The model generates SQLite-compatible SQL. The app loads CSV files into an in-memory SQLite database, so you can query any CSV data. For other databases, you can use the model directly and adapt the SQL syntax as needed.

**Q: Can I use this with my existing database?**

Yes! The model just needs the schema. You can provide your database schema and questions via the `model_client.py` interface, then execute the generated SQL against your actual database.

**Q: The model gives an incorrect query**

The model achieves 80% accuracy, which means ~1 in 5 queries may need adjustment. Always use `--show-sql` to review the generated query. If you find consistent errors, please open an issue.

**Q: Can you train a model for my company's specific database?**

Yes! Visit [distillabs.ai](https://www.distillabs.ai/?utm_source=github&utm_medium=referral&utm_campaign=text2sql) to discuss custom solutions trained on your schema and query patterns.


## Links

<p align="center">
  <a href="https://www.distillabs.ai/?utm_source=github&utm_medium=referral&utm_campaign=text2sql">
    <img src="https://github.com/distil-labs/badges/blob/main/badge-distillabs-home.svg?raw=true" alt="Distil Labs Homepage" />
  </a>
  <a href="https://github.com/distil-labs">
    <img src="https://github.com/distil-labs/badges/blob/main/badge-github.svg?raw=true" alt="GitHub" />
  </a>
  <a href="https://huggingface.co/distil-labs">
    <img src="https://github.com/distil-labs/badges/blob/main/badge-huggingface.svg?raw=true" alt="Hugging Face" />
  </a>
  <a href="https://www.linkedin.com/company/distil-labs/">
    <img src="https://github.com/distil-labs/badges/blob/main/badge-linkedin.svg?raw=true" alt="LinkedIn" />
  </a>
  <a href="https://distil-labs-community.slack.com/join/shared_invite/zt-36zqj87le-i3quWUn2bjErRq22xoE58g">
    <img src="https://github.com/distil-labs/badges/blob/main/badge-slack.svg?raw=true" alt="Slack" />
  </a>
  <a href="https://x.com/distil_labs">
    <img src="https://github.com/distil-labs/badges/blob/main/badge-twitter.svg?raw=true" alt="Twitter" />
  </a>
</p>
```

## File: `app.py`
```python
#!/usr/bin/env python3
"""
Text2SQL: Natural Language to SQL Query Generator

A CLI app that loads CSV data, converts natural language questions to SQL,
executes the queries, and returns results.
"""

import argparse
import sqlite3
import sys
from pathlib import Path

import pandas as pd

from model_client import DistilLabsLLM


def load_csv_to_sqlite(csv_paths: list[str], conn: sqlite3.Connection) -> dict[str, str]:
    """
    Load CSV files into SQLite database and return schema information.

    Returns a dict mapping table names to their CREATE TABLE statements.
    """
    schemas = {}

    for csv_path in csv_paths:
        path = Path(csv_path)
        table_name = path.stem.replace("-", "_").replace(" ", "_").lower()

        df = pd.read_csv(csv_path)
        df.to_sql(table_name, conn, index=False, if_exists="replace")

        # Generate CREATE TABLE statement from DataFrame
        columns = []
        for col in df.columns:
            dtype = df[col].dtype
            if pd.api.types.is_integer_dtype(dtype):
                sql_type = "INTEGER"
            elif pd.api.types.is_float_dtype(dtype):
                sql_type = "REAL"
            else:
                sql_type = "TEXT"
            columns.append(f"  {col} {sql_type}")

        create_stmt = f"CREATE TABLE {table_name} (\n" + ",\n".join(columns) + "\n);"
        schemas[table_name] = create_stmt

    return schemas


def format_question(schema: str, question: str) -> str:
    """Format the schema and question into the expected input format."""
    return f"""Schema:
{schema}

Question: {question}"""


def execute_query(conn: sqlite3.Connection, sql: str) -> pd.DataFrame:
    """Execute SQL query and return results as DataFrame."""
    return pd.read_sql_query(sql, conn)


def main():
    parser = argparse.ArgumentParser(
        description="Text2SQL: Query CSV data using natural language",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Query a single CSV file
  python app.py --csv data/employees.csv --question "How many employees are there?"

  # Query multiple CSV files (for JOINs)
  python app.py --csv data/orders.csv --csv data/customers.csv \\
                --question "Show total orders per customer"

  # Use a different model
  python app.py --csv data.csv --model distil-qwen3-4b-text2sql-gguf \\
                --question "What is the average salary?"
        """,
    )
    parser.add_argument(
        "--csv",
        type=str,
        action="append",
        required=True,
        help="Path to CSV file (can be specified multiple times for multiple tables)",
    )
    parser.add_argument(
        "--question",
        type=str,
        required=True,
        help="Natural language question about the data",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="distil-qwen3-4b-text2sql-gguf-4bit",
        help="Model name (default: distil-qwen3-4b-text2sql-gguf-4bit)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=11434,
        help="Ollama server port (default: 11434)",
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default="EMPTY",
        help="API key (default: EMPTY for local Ollama)",
    )
    parser.add_argument(
        "--show-sql",
        action="store_true",
        help="Print the generated SQL query",
    )

    args = parser.parse_args()

    # Validate CSV files exist
    for csv_path in args.csv:
        if not Path(csv_path).exists():
            print(f"Error: CSV file not found: {csv_path}", file=sys.stderr)
            sys.exit(1)

    # Create in-memory SQLite database and load CSV data
    conn = sqlite3.connect(":memory:")

    try:
        schemas = load_csv_to_sqlite(args.csv, conn)
    except Exception as e:
        print(f"Error loading CSV files: {e}", file=sys.stderr)
        sys.exit(1)

    # Combine all schemas
    full_schema = "\n\n".join(schemas.values())

    # Initialize model client
    client = DistilLabsLLM(
        model_name=args.model,
        api_key=args.api_key,
        port=args.port,
    )

    # Generate SQL from natural language
    formatted_input = format_question(full_schema, args.question)

    try:
        sql = client.invoke(formatted_input).strip()
    except Exception as e:
        print(f"Error generating SQL: {e}", file=sys.stderr)
        sys.exit(1)

    if args.show_sql:
        print(f"Generated SQL: {sql}\n")

    # Execute the query
    try:
        results = execute_query(conn, sql)
        print(results.to_string(index=False))
    except Exception as e:
        print(f"Error executing query: {e}", file=sys.stderr)
        print(f"Generated SQL was: {sql}", file=sys.stderr)
        sys.exit(1)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
```

## File: `model_client.py`
```python
import argparse

from openai import OpenAI

DEFAULT_QUESTION = """Schema:
CREATE TABLE clinics (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  address TEXT,
  phone TEXT
);

CREATE TABLE visits (
  id INTEGER PRIMARY KEY,
  clinic_id INTEGER REFERENCES clinics(id),
  patient_name TEXT,
  visit_date DATE,
  diagnosis TEXT
);

Question: How many patient visits per clinic this year?"""


class DistilLabsLLM(object):
    def __init__(self, model_name: str, api_key: str = "EMPTY", port: int = 11434):
        self.model_name = model_name
        self.client = OpenAI(base_url=f"http://127.0.0.1:{port}/v1", api_key=api_key)

    def get_prompt(
        self,
        question: str,
    ) -> list[dict[str, str]]:
        return [
            {
                "role": "system",
                "content": """
You are a problem solving model working on task_description XML block:
<task_description>You are given a database schema and a natural language question. Generate the SQL query that answers the question.

Input:
- Schema: One or two table definitions in SQL DDL format
- Question: Natural language question about the data

Output:
- A single SQL query that answers the question
- No explanations, comments, or additional text

Rules:
- Use only tables and columns from the provided schema
- Use uppercase SQL keywords (SELECT, FROM, WHERE, etc.)
- Use SQLite-compatible syntax</task_description>
You will be given a single task in the question XML block
Solve only the task in question block.
Generate only the answer, do not generate anything else
""",
            },
            {
                "role": "user",
                "content": f"""

Now for the real task, solve the task in question block.
Generate only the solution, do not generate anything else
<question>{question}</question>
""",
            },
        ]

    def invoke(self, question: str) -> str:
        chat_response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.get_prompt(question),
            temperature=0,
            reasoning_effort="none",
        )
        return chat_response.choices[0].message.content


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", type=str, default=DEFAULT_QUESTION, required=False)
    parser.add_argument("--api-key", type=str, default="EMPTY", required=False)
    parser.add_argument("--model", type=str, default="distil-qwen3-4b-text2sql-gguf-4bit", required=False)
    parser.add_argument("--port", type=int, default=11434, required=False)
    args = parser.parse_args()

    client = DistilLabsLLM(model_name=args.model, api_key=args.api_key, port=args.port)

    print(client.invoke(args.question))
```

## File: `example_data/employees.csv`
```
id,name,department,salary,hire_date
1,Alice Johnson,Engineering,85000,2020-03-15
2,Bob Smith,Sales,65000,2019-07-22
3,Carol Williams,Engineering,92000,2018-11-10
4,David Brown,Marketing,58000,2021-02-28
5,Eva Martinez,Engineering,78000,2020-09-01
6,Frank Lee,Sales,71000,2019-04-15
7,Grace Kim,Marketing,62000,2022-01-10
8,Henry Chen,Engineering,95000,2017-06-20
9,Irene Davis,Sales,69000,2020-11-30
10,Jack Wilson,Marketing,55000,2021-08-15
```

## File: `example_data/projects.csv`
```
id,name,lead_id,budget,status
1,Website Redesign,1,50000,completed
2,Mobile App,3,120000,in_progress
3,CRM Integration,8,80000,in_progress
4,Marketing Campaign,4,35000,completed
5,Sales Dashboard,2,45000,planning
```

## File: `finetuning/README.md`
```markdown
# Fine-tuning a Text2SQL Model with Distil CLI

Train a compact model that converts natural language questions into SQL queries using the Distil Labs platform.

## Prerequisites

Install the Distil CLI:

```bash
curl -fsSL https://cli-assets.distillabs.ai/install.sh | sh
```

Authenticate:

```bash
distil login
```

## Training Data

The `data/` folder contains everything needed to train the model:

| File | Description |
|------|-------------|
| `job_description.json` | Task definition for text-to-SQL generation |
| `train.jsonl` | Training examples (schema + question → SQL query) |
| `test.jsonl` | Evaluation examples |
| `config.yaml` | Training configuration (Qwen3-4B base model) |

### Example Training Sample

**Input:**
```
Schema:
CREATE TABLE employees (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  department TEXT,
  salary INTEGER
);

Question: How many employees are in the Sales department?
```

**Output:**
```sql
SELECT COUNT(*) FROM employees WHERE department = 'Sales';
```

## Training Steps

### 1. Create a Model

```bash
distil model create text2sql
```

Save the returned `<model-id>` for subsequent commands.

### 2. Upload Training Data

```bash
distil model upload-data <model-id> --data ./data
```

### 3. Run Teacher Evaluation

Validate that a large model can solve the task before training:

```bash
distil model run-teacher-evaluation <model-id>
```

Check status:

```bash
distil model teacher-evaluation <model-id>
```

### 4. Train the Model

Start distillation to create your compact text2sql model:

```bash
distil model run-training <model-id>
```

Monitor progress:

```bash
distil model training <model-id>
```

### 5. Download the Model

Once training completes, download the Ollama-ready package:

```bash
distil model download <model-id>
```

## Local Deployment

Run your trained model locally with [Ollama](https://ollama.com):

```bash
ollama create text2sql -f Modelfile
ollama run text2sql
```

## Model Configuration

The training uses:
- **Base model:** Qwen3-4B-Instruct-2507
- **Teacher model:** DeepSeek V3.1
- **Task type:** Question-answering

The model is trained across multiple domains: e-commerce, HR/business, education, healthcare, finance, and social/content.

## Learn More

- [Distil Documentation](https://docs.distillabs.ai)
- [Input Preparation Guide](https://docs.distillabs.ai/how-to/input-preparation)
```

## File: `finetuning/data/config.yaml`
```yaml
base:
  task: question-answering
  student_model_name: Qwen3-4B-Instruct-2507
  teacher_model_name: deepseek.v3.1
synthgen:
  generation_target: 128
  parallel_llm_calls: True
  mutation_topics: [
    "E-commerce: customers, orders, products, reviews",
    "HR/Business: employees, departments, projects",
    "Education: students, courses, enrollments",
    "Healthcare: patients, doctors, appointments",
    "Finance: accounts, transactions, payments",
    "Social/Content: users, posts, comments",
  ]
```

## File: `finetuning/data/job_description.json`
```json
{
    "task_description": "You are given a database schema and a natural language question. Generate the SQL query that answers the question.\n\nInput:\n- Schema: One or two table definitions in SQL DDL format\n- Question: Natural language question about the data\n\nOutput:\n- A single SQL query that answers the question\n- No explanations, comments, or additional text\n\nRules:\n- Use only tables and columns from the provided schema\n- Use uppercase SQL keywords (SELECT, FROM, WHERE, etc.)\n- Use SQLite-compatible syntax",
    "input_description": "Each input consists of a database schema and a natural language question.\n\nSchema format:\n- One or two CREATE TABLE statements in SQL DDL format\n- Tables use lowercase snake_case names (e.g., customers, order_items)\n- Columns use lowercase snake_case (e.g., first_name, created_at)\n- Primary key column named 'id' with INTEGER PRIMARY KEY\n- Foreign keys named as {table_singular}_id (e.g., customer_id)\n- Data types: INTEGER, TEXT, REAL, DATE, DATETIME, BOOLEAN\n- 4-10 columns per table with constraints (NOT NULL, UNIQUE, REFERENCES)\n- Two-table schemas include foreign key relationships\n\nQuestion types:\n- Counting: \"How many...\"\n- Aggregation: \"What is the average/sum/max/min...\"\n- Filtering: \"Which... where...\", \"List all... that...\"\n- Ranking: \"What are the top 5...\"\n- Joining: Questions requiring data from two tables\n- Grouping: \"...for each...\", \"...by category...\"\n\nDomains: e-commerce, HR/business, education, healthcare, finance, social/content",
    "llm_as_a_judge_instructions": "Evaluate whether the predicted SQL query correctly answers the question given the schema, using the reference query as ground truth.\n\nThe prediction is good if ALL of the following are true:\n1. Valid SQL - Query is syntactically correct and parseable\n2. Schema Compliance - All tables and columns exist in the provided schema\n3. Semantic Equivalence - Query returns the same result set as the reference (differences in aliases, formatting, or logically equivalent expressions are acceptable)\n4. Completeness - Query fully answers the question with no missing clauses\n\nThe prediction is bad if ANY of the above checks fail."
}
```

## File: `finetuning/data/test.jsonl`
```
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  salary INTEGER,\n  years_experience INTEGER\n);\n\nQuestion: How many employees work in Engineering?", "answer": "SELECT COUNT(*) FROM employees WHERE department = 'Engineering';"}
{"question": "Schema:\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  brand TEXT,\n  price REAL,\n  in_stock BOOLEAN\n);\n\nQuestion: What is the average price of Nike products?", "answer": "SELECT AVG(price) FROM products WHERE brand = 'Nike';"}
{"question": "Schema:\nCREATE TABLE customers (\n  id INTEGER PRIMARY KEY,\n  first_name TEXT,\n  last_name TEXT,\n  country TEXT,\n  registration_date DATE\n);\n\nQuestion: Show all customers from Canada.", "answer": "SELECT * FROM customers WHERE country = 'Canada';"}
{"question": "Schema:\nCREATE TABLE orders (\n  id INTEGER PRIMARY KEY,\n  customer_id INTEGER,\n  order_date DATE,\n  subtotal REAL,\n  tax REAL,\n  status TEXT\n);\n\nQuestion: What is the sum of all pending orders?", "answer": "SELECT SUM(subtotal + tax) FROM orders WHERE status = 'pending';"}
{"question": "Schema:\nCREATE TABLE students (\n  id INTEGER PRIMARY KEY,\n  full_name TEXT NOT NULL,\n  department TEXT,\n  gpa REAL,\n  credits_completed INTEGER\n);\n\nQuestion: Who are the top 10 students by credits completed?", "answer": "SELECT full_name, credits_completed FROM students ORDER BY credits_completed DESC LIMIT 10;"}
{"question": "Schema:\nCREATE TABLE payments (\n  id INTEGER PRIMARY KEY,\n  invoice_id INTEGER,\n  amount REAL,\n  payment_method TEXT,\n  payment_date DATE\n);\n\nQuestion: What is the largest payment received?", "answer": "SELECT MAX(amount) FROM payments;"}
{"question": "Schema:\nCREATE TABLE articles (\n  id INTEGER PRIMARY KEY,\n  author_id INTEGER,\n  title TEXT,\n  views INTEGER,\n  published_at DATETIME\n);\n\nQuestion: How many articles have more than 1000 views?", "answer": "SELECT COUNT(*) FROM articles WHERE views > 1000;"}
{"question": "Schema:\nCREATE TABLE patients (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  date_of_birth DATE,\n  blood_type TEXT,\n  insurance_provider TEXT\n);\n\nQuestion: What is the count of patients by blood type?", "answer": "SELECT blood_type, COUNT(*) FROM patients GROUP BY blood_type;"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  role TEXT,\n  hourly_rate REAL,\n  is_contractor BOOLEAN\n);\n\nQuestion: List all contractors with hourly rate above 75.", "answer": "SELECT * FROM employees WHERE is_contractor = 1 AND hourly_rate > 75;"}
{"question": "Schema:\nCREATE TABLE inventory (\n  id INTEGER PRIMARY KEY,\n  product_name TEXT NOT NULL,\n  warehouse TEXT,\n  quantity INTEGER,\n  last_updated DATE\n);\n\nQuestion: How many items have zero quantity?", "answer": "SELECT COUNT(*) FROM inventory WHERE quantity = 0;"}
{"question": "Schema:\nCREATE TABLE bookings (\n  id INTEGER PRIMARY KEY,\n  guest_name TEXT,\n  room_type TEXT,\n  check_in DATE,\n  check_out DATE,\n  total_price REAL\n);\n\nQuestion: What is the average booking price?", "answer": "SELECT AVG(total_price) FROM bookings;"}
{"question": "Schema:\nCREATE TABLE courses (\n  id INTEGER PRIMARY KEY,\n  title TEXT NOT NULL,\n  instructor TEXT,\n  duration_hours INTEGER,\n  difficulty TEXT\n);\n\nQuestion: Show all advanced courses.", "answer": "SELECT * FROM courses WHERE difficulty = 'advanced';"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  team TEXT,\n  base_salary INTEGER,\n  bonus INTEGER\n);\n\nQuestion: What is the total compensation (salary + bonus) per team?", "answer": "SELECT team, SUM(base_salary + bonus) FROM employees GROUP BY team;"}
{"question": "Schema:\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  category TEXT,\n  cost REAL,\n  selling_price REAL\n);\n\nQuestion: Which categories have average profit margin above 20%?", "answer": "SELECT category, AVG((selling_price - cost) / cost * 100) FROM products GROUP BY category HAVING AVG((selling_price - cost) / cost * 100) > 20;"}
{"question": "Schema:\nCREATE TABLE members (\n  id INTEGER PRIMARY KEY,\n  username TEXT UNIQUE,\n  email TEXT,\n  join_date DATE,\n  is_premium BOOLEAN\n);\n\nQuestion: How many premium members joined in 2023?", "answer": "SELECT COUNT(*) FROM members WHERE is_premium = 1 AND join_date >= '2023-01-01' AND join_date < '2024-01-01';"}
{"question": "Schema:\nCREATE TABLE reservations (\n  id INTEGER PRIMARY KEY,\n  restaurant_id INTEGER,\n  party_size INTEGER,\n  reservation_time DATETIME,\n  status TEXT\n);\n\nQuestion: How many reservations are confirmed for parties of 4 or more?", "answer": "SELECT COUNT(*) FROM reservations WHERE status = 'confirmed' AND party_size >= 4;"}
{"question": "Schema:\nCREATE TABLE expenses (\n  id INTEGER PRIMARY KEY,\n  employee_id INTEGER,\n  amount REAL,\n  category TEXT,\n  expense_date DATE\n);\n\nQuestion: What is the total travel expenses?", "answer": "SELECT SUM(amount) FROM expenses WHERE category = 'travel';"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  salary INTEGER,\n  performance_rating REAL\n);\n\nQuestion: Who has the lowest performance rating?", "answer": "SELECT name, performance_rating FROM employees ORDER BY performance_rating ASC LIMIT 1;"}
{"question": "Schema:\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  sku TEXT UNIQUE,\n  name TEXT,\n  weight REAL,\n  dimensions TEXT\n);\n\nQuestion: What is the total weight of all products?", "answer": "SELECT SUM(weight) FROM products;"}
{"question": "Schema:\nCREATE TABLE tickets (\n  id INTEGER PRIMARY KEY,\n  customer_id INTEGER,\n  subject TEXT,\n  priority TEXT,\n  created_at DATETIME\n);\n\nQuestion: How many tickets exist per priority level?", "answer": "SELECT priority, COUNT(*) FROM tickets GROUP BY priority;"}
{"question": "Schema:\nCREATE TABLE sales (\n  id INTEGER PRIMARY KEY,\n  product_id INTEGER,\n  quantity INTEGER,\n  sale_date DATE,\n  region TEXT\n);\n\nQuestion: List sales from the last 7 days.", "answer": "SELECT * FROM sales WHERE sale_date >= DATE('now', '-7 days');"}
{"question": "Schema:\nCREATE TABLE applicants (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  position TEXT,\n  experience_years INTEGER,\n  status TEXT\n);\n\nQuestion: How many applicants applied for each position?", "answer": "SELECT position, COUNT(*) FROM applicants GROUP BY position;"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  start_date DATE,\n  end_date DATE\n);\n\nQuestion: List employees who left the company in 2024.", "answer": "SELECT * FROM employees WHERE end_date >= '2024-01-01' AND end_date < '2025-01-01';"}
{"question": "Schema:\nCREATE TABLE items (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  category TEXT,\n  price REAL,\n  is_on_sale BOOLEAN\n);\n\nQuestion: What is the maximum price of items on sale?", "answer": "SELECT MAX(price) FROM items WHERE is_on_sale = 1;"}
{"question": "Schema:\nCREATE TABLE messages (\n  id INTEGER PRIMARY KEY,\n  sender_id INTEGER,\n  receiver_id INTEGER,\n  content TEXT,\n  sent_at DATETIME\n);\n\nQuestion: How many messages did each sender send?", "answer": "SELECT sender_id, COUNT(*) FROM messages GROUP BY sender_id;"}
{"question": "Schema:\nCREATE TABLE vendors (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  contact_email TEXT,\n  country TEXT\n);\n\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  vendor_id INTEGER REFERENCES vendors(id),\n  name TEXT NOT NULL,\n  price REAL,\n  category TEXT\n);\n\nQuestion: List all products with their vendor names.", "answer": "SELECT p.name, v.name AS vendor_name FROM products p JOIN vendors v ON p.vendor_id = v.id;"}
{"question": "Schema:\nCREATE TABLE teams (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  manager TEXT,\n  budget INTEGER\n);\n\nCREATE TABLE projects (\n  id INTEGER PRIMARY KEY,\n  team_id INTEGER REFERENCES teams(id),\n  name TEXT NOT NULL,\n  status TEXT,\n  deadline DATE\n);\n\nQuestion: How many active projects does each team have?", "answer": "SELECT t.name, COUNT(*) FROM teams t JOIN projects p ON t.id = p.team_id WHERE p.status = 'active' GROUP BY t.id, t.name;"}
{"question": "Schema:\nCREATE TABLE instructors (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  hire_date DATE\n);\n\nCREATE TABLE classes (\n  id INTEGER PRIMARY KEY,\n  instructor_id INTEGER REFERENCES instructors(id),\n  course_name TEXT,\n  semester TEXT,\n  enrollment INTEGER\n);\n\nQuestion: What is the total enrollment per instructor?", "answer": "SELECT i.name, SUM(c.enrollment) FROM instructors i JOIN classes c ON i.id = c.instructor_id GROUP BY i.id, i.name;"}
{"question": "Schema:\nCREATE TABLE warehouses (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  city TEXT,\n  capacity INTEGER\n);\n\nCREATE TABLE shipments (\n  id INTEGER PRIMARY KEY,\n  warehouse_id INTEGER REFERENCES warehouses(id),\n  destination TEXT,\n  ship_date DATE,\n  weight REAL\n);\n\nQuestion: What is the total shipment weight per warehouse?", "answer": "SELECT w.name, SUM(s.weight) FROM warehouses w JOIN shipments s ON w.id = s.warehouse_id GROUP BY w.id, w.name;"}
{"question": "Schema:\nCREATE TABLE artists (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  genre TEXT,\n  country TEXT\n);\n\nCREATE TABLE albums (\n  id INTEGER PRIMARY KEY,\n  artist_id INTEGER REFERENCES artists(id),\n  title TEXT NOT NULL,\n  release_year INTEGER,\n  sales INTEGER\n);\n\nQuestion: Which artists have total album sales over 1 million?", "answer": "SELECT a.name, SUM(al.sales) FROM artists a JOIN albums al ON a.id = al.artist_id GROUP BY a.id, a.name HAVING SUM(al.sales) > 1000000;"}
{"question": "Schema:\nCREATE TABLE clinics (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  address TEXT,\n  phone TEXT\n);\n\nCREATE TABLE visits (\n  id INTEGER PRIMARY KEY,\n  clinic_id INTEGER REFERENCES clinics(id),\n  patient_name TEXT,\n  visit_date DATE,\n  diagnosis TEXT\n);\n\nQuestion: How many patient visits per clinic this year?", "answer": "SELECT c.name, COUNT(*) FROM clinics c JOIN visits v ON c.id = v.clinic_id WHERE v.visit_date >= '2024-01-01' GROUP BY c.id, c.name;"}
{"question": "Schema:\nCREATE TABLE banks (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  headquarters TEXT\n);\n\nCREATE TABLE loans (\n  id INTEGER PRIMARY KEY,\n  bank_id INTEGER REFERENCES banks(id),\n  customer_name TEXT,\n  amount REAL,\n  interest_rate REAL,\n  status TEXT\n);\n\nQuestion: What is the total loan amount per bank?", "answer": "SELECT b.name, SUM(l.amount) FROM banks b JOIN loans l ON b.id = l.bank_id GROUP BY b.id, b.name;"}
{"question": "Schema:\nCREATE TABLE brands (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  industry TEXT\n);\n\nCREATE TABLE campaigns (\n  id INTEGER PRIMARY KEY,\n  brand_id INTEGER REFERENCES brands(id),\n  name TEXT,\n  budget REAL,\n  start_date DATE,\n  end_date DATE\n);\n\nQuestion: What is the average campaign budget per brand?", "answer": "SELECT b.name, AVG(c.budget) FROM brands b JOIN campaigns c ON b.id = c.brand_id GROUP BY b.id, b.name;"}
{"question": "Schema:\nCREATE TABLE publishers (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  founded_year INTEGER\n);\n\nCREATE TABLE games (\n  id INTEGER PRIMARY KEY,\n  publisher_id INTEGER REFERENCES publishers(id),\n  title TEXT NOT NULL,\n  platform TEXT,\n  rating REAL\n);\n\nQuestion: List all games with their publisher names.", "answer": "SELECT g.title, p.name AS publisher_name FROM games g JOIN publishers p ON g.publisher_id = p.id;"}
{"question": "Schema:\nCREATE TABLE regions (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  country TEXT\n);\n\nCREATE TABLE stores (\n  id INTEGER PRIMARY KEY,\n  region_id INTEGER REFERENCES regions(id),\n  name TEXT,\n  revenue REAL,\n  employee_count INTEGER\n);\n\nQuestion: Which regions have total store revenue exceeding 500000?", "answer": "SELECT r.name FROM regions r JOIN stores s ON r.id = s.region_id GROUP BY r.id, r.name HAVING SUM(s.revenue) > 500000;"}
{"question": "Schema:\nCREATE TABLE subscribers (\n  id INTEGER PRIMARY KEY,\n  email TEXT UNIQUE,\n  plan_type TEXT,\n  monthly_fee REAL\n);\n\nCREATE TABLE usage_logs (\n  id INTEGER PRIMARY KEY,\n  subscriber_id INTEGER REFERENCES subscribers(id),\n  data_used_gb REAL,\n  log_date DATE\n);\n\nQuestion: What is the average data usage for premium subscribers?", "answer": "SELECT AVG(u.data_used_gb) FROM subscribers s JOIN usage_logs u ON s.id = u.subscriber_id WHERE s.plan_type = 'premium';"}
{"question": "Schema:\nCREATE TABLE staff (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  role TEXT,\n  hourly_wage REAL,\n  hire_date DATE\n);\n\nQuestion: What is the wage range (min and max) for each role?", "answer": "SELECT role, MIN(hourly_wage), MAX(hourly_wage) FROM staff GROUP BY role;"}
{"question": "Schema:\nCREATE TABLE purchases (\n  id INTEGER PRIMARY KEY,\n  buyer_id INTEGER,\n  purchase_date DATE,\n  amount REAL,\n  category TEXT\n);\n\nQuestion: How many purchases were made each week in 2024?", "answer": "SELECT strftime('%W', purchase_date) AS week, COUNT(*) FROM purchases WHERE purchase_date >= '2024-01-01' AND purchase_date < '2025-01-01' GROUP BY strftime('%W', purchase_date);"}
{"question": "Schema:\nCREATE TABLE vehicles (\n  id INTEGER PRIMARY KEY,\n  make TEXT,\n  model TEXT,\n  year INTEGER,\n  price REAL\n);\n\nQuestion: List vehicles priced between 20000 and 40000.", "answer": "SELECT * FROM vehicles WHERE price BETWEEN 20000 AND 40000;"}
{"question": "Schema:\nCREATE TABLE contacts (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  company TEXT,\n  email TEXT,\n  phone TEXT\n);\n\nQuestion: Find contacts whose company contains 'Tech'.", "answer": "SELECT * FROM contacts WHERE company LIKE '%Tech%';"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  salary INTEGER,\n  manager_id INTEGER\n);\n\nQuestion: List employees earning above the company average salary.", "answer": "SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);"}
{"question": "Schema:\nCREATE TABLE properties (\n  id INTEGER PRIMARY KEY,\n  address TEXT,\n  city TEXT,\n  price REAL,\n  bedrooms INTEGER\n);\n\nQuestion: Find properties priced above average for their city.", "answer": "SELECT p1.* FROM properties p1 WHERE p1.price > (SELECT AVG(p2.price) FROM properties p2 WHERE p2.city = p1.city);"}
{"question": "Schema:\nCREATE TABLE ledger (\n  id INTEGER PRIMARY KEY,\n  account_id INTEGER,\n  debit REAL,\n  credit REAL,\n  entry_date DATE\n);\n\nQuestion: What is the net balance (credits minus debits)?", "answer": "SELECT SUM(credit) - SUM(debit) FROM ledger;"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  salary INTEGER,\n  tenure_years INTEGER\n);\n\nQuestion: Rank employees by tenure within each department.", "answer": "SELECT name, department, tenure_years, RANK() OVER (PARTITION BY department ORDER BY tenure_years DESC) AS rank FROM employees;"}
{"question": "Schema:\nCREATE TABLE tasks (\n  id INTEGER PRIMARY KEY,\n  project_id INTEGER,\n  title TEXT,\n  status TEXT,\n  assigned_to INTEGER\n);\n\nQuestion: What percentage of tasks are completed?", "answer": "SELECT (COUNT(CASE WHEN status = 'completed' THEN 1 END) * 100.0 / COUNT(*)) FROM tasks;"}
{"question": "Schema:\nCREATE TABLE suppliers (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  contact_email TEXT,\n  rating REAL\n);\n\nCREATE TABLE purchase_orders (\n  id INTEGER PRIMARY KEY,\n  supplier_id INTEGER REFERENCES suppliers(id),\n  order_date DATE,\n  total_value REAL,\n  status TEXT\n);\n\nQuestion: Find suppliers with no purchase orders.", "answer": "SELECT s.* FROM suppliers s LEFT JOIN purchase_orders po ON s.id = po.supplier_id WHERE po.id IS NULL;"}
{"question": "Schema:\nCREATE TABLE movies (\n  id INTEGER PRIMARY KEY,\n  title TEXT NOT NULL,\n  genre TEXT,\n  release_year INTEGER\n);\n\nCREATE TABLE ratings (\n  id INTEGER PRIMARY KEY,\n  movie_id INTEGER REFERENCES movies(id),\n  user_id INTEGER,\n  score INTEGER,\n  rated_at DATE\n);\n\nQuestion: What is the average rating for each movie?", "answer": "SELECT m.title, AVG(r.score) FROM movies m JOIN ratings r ON m.id = r.movie_id GROUP BY m.id, m.title;"}
{"question": "Schema:\nCREATE TABLE divisions (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  head_count INTEGER\n);\n\nCREATE TABLE budgets (\n  id INTEGER PRIMARY KEY,\n  division_id INTEGER REFERENCES divisions(id),\n  fiscal_year INTEGER,\n  allocated REAL,\n  spent REAL\n);\n\nQuestion: Find the division with highest spending in 2024.", "answer": "SELECT d.name, b.spent FROM divisions d JOIN budgets b ON d.id = b.division_id WHERE b.fiscal_year = 2024 ORDER BY b.spent DESC LIMIT 1;"}
{"question": "Schema:\nCREATE TABLE subscriptions (\n  id INTEGER PRIMARY KEY,\n  user_id INTEGER,\n  plan TEXT,\n  start_date DATE,\n  is_active BOOLEAN\n);\n\nQuestion: What is the total count of inactive subscriptions?", "answer": "SELECT COUNT(*) FROM subscriptions WHERE is_active = 0;"}
{"question": "Schema:\nCREATE TABLE routes (\n  id INTEGER PRIMARY KEY,\n  origin_city TEXT,\n  destination_city TEXT,\n  distance_km INTEGER,\n  avg_duration_min INTEGER,\n  fare REAL\n);\n\nQuestion: List routes from Chicago to cities within 500km.", "answer": "SELECT * FROM routes WHERE origin_city = 'Chicago' AND distance_km <= 500;"}
```

## File: `finetuning/data/train.jsonl`
```
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  salary INTEGER,\n  hire_date DATE\n);\n\nQuestion: How many employees are in the Sales department?", "answer": "SELECT COUNT(*) FROM employees WHERE department = 'Sales';"}
{"question": "Schema:\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  category TEXT,\n  price REAL,\n  stock_quantity INTEGER\n);\n\nQuestion: What is the average price of products in the Electronics category?", "answer": "SELECT AVG(price) FROM products WHERE category = 'Electronics';"}
{"question": "Schema:\nCREATE TABLE customers (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  email TEXT UNIQUE,\n  city TEXT,\n  created_at DATE\n);\n\nQuestion: List all customers from New York.", "answer": "SELECT * FROM customers WHERE city = 'New York';"}
{"question": "Schema:\nCREATE TABLE orders (\n  id INTEGER PRIMARY KEY,\n  customer_id INTEGER,\n  order_date DATE,\n  total_amount REAL,\n  status TEXT\n);\n\nQuestion: What is the total revenue from completed orders?", "answer": "SELECT SUM(total_amount) FROM orders WHERE status = 'completed';"}
{"question": "Schema:\nCREATE TABLE students (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  major TEXT,\n  gpa REAL,\n  enrollment_year INTEGER\n);\n\nQuestion: Who are the top 5 students by GPA?", "answer": "SELECT name, gpa FROM students ORDER BY gpa DESC LIMIT 5;"}
{"question": "Schema:\nCREATE TABLE transactions (\n  id INTEGER PRIMARY KEY,\n  account_id INTEGER,\n  amount REAL,\n  transaction_type TEXT,\n  transaction_date DATETIME\n);\n\nQuestion: What is the maximum transaction amount?", "answer": "SELECT MAX(amount) FROM transactions;"}
{"question": "Schema:\nCREATE TABLE posts (\n  id INTEGER PRIMARY KEY,\n  user_id INTEGER,\n  title TEXT,\n  content TEXT,\n  likes INTEGER,\n  created_at DATETIME\n);\n\nQuestion: How many posts have more than 100 likes?", "answer": "SELECT COUNT(*) FROM posts WHERE likes > 100;"}
{"question": "Schema:\nCREATE TABLE patients (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  age INTEGER,\n  gender TEXT,\n  diagnosis TEXT,\n  admission_date DATE\n);\n\nQuestion: What is the average age of patients?", "answer": "SELECT AVG(age) FROM patients;"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  salary INTEGER,\n  is_active BOOLEAN\n);\n\nQuestion: List all active employees earning more than 50000.", "answer": "SELECT * FROM employees WHERE is_active = 1 AND salary > 50000;"}
{"question": "Schema:\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  category TEXT,\n  price REAL,\n  stock_quantity INTEGER\n);\n\nQuestion: How many products are out of stock?", "answer": "SELECT COUNT(*) FROM products WHERE stock_quantity = 0;"}
{"question": "Schema:\nCREATE TABLE orders (\n  id INTEGER PRIMARY KEY,\n  customer_id INTEGER,\n  order_date DATE,\n  total_amount REAL,\n  status TEXT\n);\n\nQuestion: What is the average order value?", "answer": "SELECT AVG(total_amount) FROM orders;"}
{"question": "Schema:\nCREATE TABLE courses (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  credits INTEGER,\n  instructor TEXT\n);\n\nQuestion: List all courses with more than 3 credits.", "answer": "SELECT * FROM courses WHERE credits > 3;"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  salary INTEGER,\n  hire_date DATE\n);\n\nQuestion: What is the total salary expense per department?", "answer": "SELECT department, SUM(salary) FROM employees GROUP BY department;"}
{"question": "Schema:\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  category TEXT,\n  price REAL,\n  rating REAL\n);\n\nQuestion: What are the categories with average rating above 4?", "answer": "SELECT category, AVG(rating) FROM products GROUP BY category HAVING AVG(rating) > 4;"}
{"question": "Schema:\nCREATE TABLE users (\n  id INTEGER PRIMARY KEY,\n  username TEXT UNIQUE,\n  email TEXT,\n  signup_date DATE,\n  is_verified BOOLEAN\n);\n\nQuestion: How many verified users signed up in 2024?", "answer": "SELECT COUNT(*) FROM users WHERE is_verified = 1 AND signup_date >= '2024-01-01' AND signup_date < '2025-01-01';"}
{"question": "Schema:\nCREATE TABLE appointments (\n  id INTEGER PRIMARY KEY,\n  patient_id INTEGER,\n  doctor_id INTEGER,\n  appointment_date DATETIME,\n  status TEXT\n);\n\nQuestion: How many appointments are scheduled for today?", "answer": "SELECT COUNT(*) FROM appointments WHERE DATE(appointment_date) = DATE('now');"}
{"question": "Schema:\nCREATE TABLE transactions (\n  id INTEGER PRIMARY KEY,\n  account_id INTEGER,\n  amount REAL,\n  transaction_type TEXT,\n  transaction_date DATE\n);\n\nQuestion: What is the total amount of deposits?", "answer": "SELECT SUM(amount) FROM transactions WHERE transaction_type = 'deposit';"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  salary INTEGER,\n  manager_id INTEGER\n);\n\nQuestion: Who earns the highest salary?", "answer": "SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 1;"}
{"question": "Schema:\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  category TEXT,\n  price REAL,\n  stock_quantity INTEGER\n);\n\nQuestion: What is the total stock value per category?", "answer": "SELECT category, SUM(price * stock_quantity) FROM products GROUP BY category;"}
{"question": "Schema:\nCREATE TABLE customers (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  email TEXT,\n  country TEXT,\n  total_purchases REAL\n);\n\nQuestion: Which countries have more than 10 customers?", "answer": "SELECT country, COUNT(*) FROM customers GROUP BY country HAVING COUNT(*) > 10;"}
{"question": "Schema:\nCREATE TABLE orders (\n  id INTEGER PRIMARY KEY,\n  customer_id INTEGER,\n  order_date DATE,\n  total_amount REAL,\n  shipping_address TEXT\n);\n\nQuestion: List orders placed in the last 30 days.", "answer": "SELECT * FROM orders WHERE order_date >= DATE('now', '-30 days');"}
{"question": "Schema:\nCREATE TABLE students (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  major TEXT,\n  gpa REAL,\n  enrollment_year INTEGER\n);\n\nQuestion: How many students are enrolled in each major?", "answer": "SELECT major, COUNT(*) FROM students GROUP BY major;"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  salary INTEGER,\n  hire_date DATE\n);\n\nQuestion: List employees hired before 2020.", "answer": "SELECT * FROM employees WHERE hire_date < '2020-01-01';"}
{"question": "Schema:\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  category TEXT,\n  price REAL,\n  is_featured BOOLEAN\n);\n\nQuestion: What is the minimum price of featured products?", "answer": "SELECT MIN(price) FROM products WHERE is_featured = 1;"}
{"question": "Schema:\nCREATE TABLE comments (\n  id INTEGER PRIMARY KEY,\n  post_id INTEGER,\n  user_id INTEGER,\n  content TEXT,\n  created_at DATETIME\n);\n\nQuestion: How many comments were made per post?", "answer": "SELECT post_id, COUNT(*) FROM comments GROUP BY post_id;"}
{"question": "Schema:\nCREATE TABLE customers (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  email TEXT UNIQUE,\n  city TEXT,\n  created_at DATE\n);\n\nCREATE TABLE orders (\n  id INTEGER PRIMARY KEY,\n  customer_id INTEGER REFERENCES customers(id),\n  order_date DATE,\n  total_amount REAL,\n  status TEXT\n);\n\nQuestion: List all customers who have placed orders.", "answer": "SELECT DISTINCT c.name, c.email FROM customers c JOIN orders o ON c.id = o.customer_id;"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department_id INTEGER REFERENCES departments(id),\n  salary INTEGER,\n  hire_date DATE\n);\n\nCREATE TABLE departments (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  budget INTEGER,\n  location TEXT\n);\n\nQuestion: List all employees with their department names.", "answer": "SELECT e.name, d.name AS department_name FROM employees e JOIN departments d ON e.department_id = d.id;"}
{"question": "Schema:\nCREATE TABLE students (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  email TEXT,\n  enrollment_year INTEGER\n);\n\nCREATE TABLE enrollments (\n  id INTEGER PRIMARY KEY,\n  student_id INTEGER REFERENCES students(id),\n  course_id INTEGER,\n  grade TEXT,\n  semester TEXT\n);\n\nQuestion: How many courses is each student enrolled in?", "answer": "SELECT s.name, COUNT(*) FROM students s JOIN enrollments e ON s.id = e.student_id GROUP BY s.id, s.name;"}
{"question": "Schema:\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  category TEXT,\n  price REAL\n);\n\nCREATE TABLE order_items (\n  id INTEGER PRIMARY KEY,\n  order_id INTEGER,\n  product_id INTEGER REFERENCES products(id),\n  quantity INTEGER,\n  unit_price REAL\n);\n\nQuestion: What is the total quantity sold per product?", "answer": "SELECT p.name, SUM(oi.quantity) FROM products p JOIN order_items oi ON p.id = oi.product_id GROUP BY p.id, p.name;"}
{"question": "Schema:\nCREATE TABLE users (\n  id INTEGER PRIMARY KEY,\n  username TEXT UNIQUE,\n  email TEXT,\n  created_at DATE\n);\n\nCREATE TABLE posts (\n  id INTEGER PRIMARY KEY,\n  user_id INTEGER REFERENCES users(id),\n  title TEXT,\n  content TEXT,\n  created_at DATETIME\n);\n\nQuestion: Which users have posted more than 5 times?", "answer": "SELECT u.username, COUNT(*) FROM users u JOIN posts p ON u.id = p.user_id GROUP BY u.id, u.username HAVING COUNT(*) > 5;"}
{"question": "Schema:\nCREATE TABLE doctors (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  specialty TEXT,\n  hospital TEXT\n);\n\nCREATE TABLE appointments (\n  id INTEGER PRIMARY KEY,\n  doctor_id INTEGER REFERENCES doctors(id),\n  patient_name TEXT,\n  appointment_date DATE,\n  reason TEXT\n);\n\nQuestion: How many appointments does each doctor have?", "answer": "SELECT d.name, COUNT(*) FROM doctors d JOIN appointments a ON d.id = a.doctor_id GROUP BY d.id, d.name;"}
{"question": "Schema:\nCREATE TABLE accounts (\n  id INTEGER PRIMARY KEY,\n  customer_name TEXT NOT NULL,\n  account_type TEXT,\n  balance REAL,\n  opened_date DATE\n);\n\nCREATE TABLE transactions (\n  id INTEGER PRIMARY KEY,\n  account_id INTEGER REFERENCES accounts(id),\n  amount REAL,\n  transaction_type TEXT,\n  transaction_date DATE\n);\n\nQuestion: What is the total transaction amount per account?", "answer": "SELECT a.customer_name, SUM(t.amount) FROM accounts a JOIN transactions t ON a.id = t.account_id GROUP BY a.id, a.customer_name;"}
{"question": "Schema:\nCREATE TABLE categories (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  description TEXT\n);\n\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  category_id INTEGER REFERENCES categories(id),\n  price REAL,\n  stock_quantity INTEGER\n);\n\nQuestion: What is the average product price per category?", "answer": "SELECT c.name, AVG(p.price) FROM categories c JOIN products p ON c.id = p.category_id GROUP BY c.id, c.name;"}
{"question": "Schema:\nCREATE TABLE authors (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  country TEXT\n);\n\nCREATE TABLE books (\n  id INTEGER PRIMARY KEY,\n  title TEXT NOT NULL,\n  author_id INTEGER REFERENCES authors(id),\n  published_year INTEGER,\n  genre TEXT\n);\n\nQuestion: List all books with their author names.", "answer": "SELECT b.title, a.name AS author_name FROM books b JOIN authors a ON b.author_id = a.id;"}
{"question": "Schema:\nCREATE TABLE departments (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  budget INTEGER\n);\n\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department_id INTEGER REFERENCES departments(id),\n  salary INTEGER\n);\n\nQuestion: Which departments have total salary expenses exceeding their budget?", "answer": "SELECT d.name FROM departments d JOIN employees e ON d.id = e.department_id GROUP BY d.id, d.name, d.budget HAVING SUM(e.salary) > d.budget;"}
{"question": "Schema:\nCREATE TABLE customers (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  email TEXT,\n  membership_level TEXT\n);\n\nCREATE TABLE orders (\n  id INTEGER PRIMARY KEY,\n  customer_id INTEGER REFERENCES customers(id),\n  total_amount REAL,\n  order_date DATE\n);\n\nQuestion: What is the average order amount for premium customers?", "answer": "SELECT AVG(o.total_amount) FROM customers c JOIN orders o ON c.id = o.customer_id WHERE c.membership_level = 'premium';"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  salary INTEGER,\n  hire_date DATE\n);\n\nQuestion: What is the salary range (min and max) in each department?", "answer": "SELECT department, MIN(salary), MAX(salary) FROM employees GROUP BY department;"}
{"question": "Schema:\nCREATE TABLE orders (\n  id INTEGER PRIMARY KEY,\n  customer_id INTEGER,\n  order_date DATE,\n  total_amount REAL,\n  status TEXT\n);\n\nQuestion: How many orders were placed each month in 2024?", "answer": "SELECT strftime('%m', order_date) AS month, COUNT(*) FROM orders WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01' GROUP BY strftime('%m', order_date);"}
{"question": "Schema:\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  category TEXT,\n  price REAL,\n  rating REAL\n);\n\nQuestion: List products priced between 10 and 50 dollars.", "answer": "SELECT * FROM products WHERE price BETWEEN 10 AND 50;"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  salary INTEGER,\n  email TEXT\n);\n\nQuestion: Find employees whose name starts with 'J'.", "answer": "SELECT * FROM employees WHERE name LIKE 'J%';"}
{"question": "Schema:\nCREATE TABLE students (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  major TEXT,\n  gpa REAL,\n  advisor_id INTEGER\n);\n\nQuestion: List students with GPA above the average GPA.", "answer": "SELECT * FROM students WHERE gpa > (SELECT AVG(gpa) FROM students);"}
{"question": "Schema:\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  category TEXT,\n  price REAL,\n  supplier_id INTEGER\n);\n\nQuestion: Which products have price above average for their category?", "answer": "SELECT p1.* FROM products p1 WHERE p1.price > (SELECT AVG(p2.price) FROM products p2 WHERE p2.category = p1.category);"}
{"question": "Schema:\nCREATE TABLE transactions (\n  id INTEGER PRIMARY KEY,\n  account_id INTEGER,\n  amount REAL,\n  transaction_type TEXT,\n  transaction_date DATE\n);\n\nQuestion: What is the net balance change (deposits minus withdrawals)?", "answer": "SELECT SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE -amount END) FROM transactions;"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department TEXT,\n  salary INTEGER,\n  hire_date DATE\n);\n\nQuestion: Rank employees by salary within each department.", "answer": "SELECT name, department, salary, RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank FROM employees;"}
{"question": "Schema:\nCREATE TABLE orders (\n  id INTEGER PRIMARY KEY,\n  customer_id INTEGER,\n  order_date DATE,\n  total_amount REAL,\n  status TEXT\n);\n\nQuestion: What percentage of orders are completed?", "answer": "SELECT (COUNT(CASE WHEN status = 'completed' THEN 1 END) * 100.0 / COUNT(*)) FROM orders;"}
{"question": "Schema:\nCREATE TABLE customers (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  email TEXT,\n  city TEXT\n);\n\nCREATE TABLE orders (\n  id INTEGER PRIMARY KEY,\n  customer_id INTEGER REFERENCES customers(id),\n  total_amount REAL,\n  order_date DATE\n);\n\nQuestion: Find customers who have never placed an order.", "answer": "SELECT c.* FROM customers c LEFT JOIN orders o ON c.id = o.customer_id WHERE o.id IS NULL;"}
{"question": "Schema:\nCREATE TABLE products (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  category TEXT,\n  price REAL\n);\n\nCREATE TABLE reviews (\n  id INTEGER PRIMARY KEY,\n  product_id INTEGER REFERENCES products(id),\n  rating INTEGER,\n  comment TEXT,\n  created_at DATE\n);\n\nQuestion: What is the average rating for each product?", "answer": "SELECT p.name, AVG(r.rating) FROM products p JOIN reviews r ON p.id = r.product_id GROUP BY p.id, p.name;"}
{"question": "Schema:\nCREATE TABLE employees (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  department_id INTEGER REFERENCES departments(id),\n  salary INTEGER\n);\n\nCREATE TABLE departments (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  manager_id INTEGER\n);\n\nQuestion: Find the highest paid employee in each department.", "answer": "SELECT d.name AS department, e.name, e.salary FROM employees e JOIN departments d ON e.department_id = d.id WHERE e.salary = (SELECT MAX(salary) FROM employees WHERE department_id = e.department_id);"}
{"question": "Schema:\nCREATE TABLE invoices (\n  id INTEGER PRIMARY KEY,\n  customer_id INTEGER,\n  invoice_date DATE,\n  amount REAL,\n  is_paid BOOLEAN\n);\n\nQuestion: What is the total unpaid invoice amount?", "answer": "SELECT SUM(amount) FROM invoices WHERE is_paid = 0;"}
{"question": "Schema:\nCREATE TABLE flights (\n  id INTEGER PRIMARY KEY,\n  origin TEXT,\n  destination TEXT,\n  departure_time DATETIME,\n  price REAL,\n  seats_available INTEGER\n);\n\nQuestion: List available flights from New York to Los Angeles.", "answer": "SELECT * FROM flights WHERE origin = 'New York' AND destination = 'Los Angeles' AND seats_available > 0;"}
```

