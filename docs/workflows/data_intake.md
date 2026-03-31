# OmniClaw Data Intake Workflow

## Content Intake and Vetting (CIV) Pipeline

The OmniClaw ecosystem operates on a Strict Zero-Trust Architecture. All 3rd-party code, repositories, or external plugins MUST be completely sandboxed within `system/security/QUARANTINE_INCOMING` and undergo meticulous scanning before execution. Raw `git clone` into `/brain` or `/ecosystem/plugins/` is architecturally prohibited and natively blocked.

To safely ingest new data, you MUST use the CIV pipeline managed by Dept 20 (CIV) and Dept 10 (Strix).

### Pipeline Execution Steps

1. **Target Identification:** Identify the target URL or repository you wish to ingest into the OmniClaw corpus.
2. **Registration:** Append the target URL and an internal target directory alias to the `storage/vault/DATA/Github.txt` tracking list.
3. **Deep Evaluation:** Run the intelligence evaluator to parse and assess the structural relevance of the repository.
   ```ps1
   python system/ops/scripts/omniclaw_deep_evaluator.py
   ```
4. **Active Pipeline Extraction:** Execute the main ingestion pipeline. This script will physically pull the repository into the strict `/system/security/QUARANTINE_INCOMING` space, scan it for malware and secrets, strip unnecessary files, and finally move the sanitized structured data into `/brain/corp` or `/brain/registry`.
   ```ps1
   python system/ops/scripts/active_repos_pipeline.py
   ```

### Architecture Enforcement

* **No Hardcoded API Keys:** The pipeline actively scans for committed keys, tokens, or `.env` files. If any are detected, the payload is immediately dropped.
* **Format Preservation:** The pipeline will transform Markdown docs and code into a format easily parsable by LLMs and RAG engines.

### Repository Processing Pipeline (Repo Analysis)

To clean up and distill knowledge from the raw source code of hundreds of cloned repositories, run:

```ps1
python system/ops/scripts/omniclaw_repo_analyzer.py
```

* **Extraction:** Generates lightweight `.md` knowledge reports saved to `brain/knowledge/processed_repos/`.
* **Cleanup (ARCHIVE):** It then automatically relocates the heavy source code to the permanent storage vault `storage/vault/ARCHIVE/` to isolate it from Github and prevent repository bloat.
* **Categorization (Knowledge Cleanup):** Finally, run `python system/ops/scripts/clean_knowledge.py` to sort AI/ML, architecture, and UI reports into their respective categories within `brain/knowledge/`.
