---
id: github.com-lightning-ai-litserve-aed76eb5-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:21.366904
---

# KNOWLEDGE EXTRACT: github.com_Lightning-AI_LitServe_aed76eb5
> **Extracted on:** 2026-04-01 09:46:38
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520445/github.com_Lightning-AI_LitServe_aed76eb5

---

## File: `.codecov.yml`
```yaml
# see https://docs.codecov.io/docs/codecov-yaml
# Validation check:
# $ curl --data-binary @.codecov.yml https://codecov.io/validate

# https://docs.codecov.io/docs/codecovyml-reference
codecov:
  bot: "codecov-io"
  strict_yaml_branch: "yaml-config"
  require_ci_to_pass: yes
  notify:
    # after_n_builds: 2
    wait_for_ci: yes

coverage:
  precision: 0 # 2 = xx.xx%, 0 = xx%
  round: nearest # how coverage is rounded: down/up/nearest
  range: 40...100 # custom range of coverage colors from red -> yellow -> green
  status:
    # https://codecov.readme.io/v1.0/docs/commit-status
    project:
      default:
        informational: true
        target: 99% # specify the target coverage for each commit status
        threshold: 30% # allow this little decrease on project
        # https://github.com/codecov/support/wiki/Filtering-Branches
        # branches: main
        if_ci_failed: error
    # https://github.com/codecov/support/wiki/Patch-Status
    patch:
      default:
        informational: true
        target: 50% # specify the target "X%" coverage to hit
        # threshold: 50% # allow this much decrease on patch
    changes: false

# https://docs.codecov.com/docs/github-checks#disabling-github-checks-patch-annotations
github_checks:
  annotations: false

parsers:
  gcov:
    branch_detection:
      conditional: true
      loop: true
      macro: false
      method: false
  javascript:
    enable_partials: false

comment:
  layout: header, diff
  require_changes: false
  behavior: default # update if exists else create new
  # branches: *
```

## File: `.gitignore`
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

*.egg-info/
src.egg-info/

# Lightning /research
test_tube_exp/
tests/tests_tt_dir/
tests/save_dir
default/
data/
test_tube_logs/
test_tube_data/
datasets/
model_weights/
tests/save_dir
tests/tests_tt_dir/
processed/
raw/

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site


# mypy
.mypy_cache/

# IDEs
.idea
.vscode

# seed project
lightning_logs/
MNIST
.DS_Store
uv.lock
```

## File: `.pre-commit-config.yaml`
```yaml
default_language_version:
  python: python3

ci:
  autofix_prs: true
  autoupdate_commit_msg: "[pre-commit.ci] pre-commit suggestions"
  autoupdate_schedule: "monthly"
  # submodules: true

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
        exclude: '.*\.md$'
      - id: check-case-conflict
      - id: check-yaml
      - id: check-toml
      - id: check-json
      - id: check-added-large-files
      - id: check-docstring-first
      - id: detect-private-key

  - repo: https://github.com/codespell-project/codespell
    rev: v2.4.1
    hooks:
      - id: codespell
        additional_dependencies: [tomli]
        #args: ["--write-changes"]

  - repo: https://github.com/JoC0de/pre-commit-prettier
    rev: v3.8.1
    hooks:
      - id: prettier
        files: \.(json|yml|yaml|toml)
        # https://prettier.io/docs/en/options.html#print-width
        args: ["--print-width=120"]

  - repo: https://github.com/PyCQA/docformatter
    rev: v1.7.7
    hooks:
      - id: docformatter
        additional_dependencies: [tomli]
        args: ["--in-place"]

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.15.4
    hooks:
      - id: ruff
        args: ["--fix"]
      - id: ruff-format
      - id: ruff-check
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2024 Lightning AI

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `MANIFEST.in`
```
# Manifest syntax https://docs.python.org/2/distutils/sourcedist.html
graft wheelhouse

recursive-exclude __pycache__  *.py[cod] *.orig

# Include the README and CHANGELOG
include *.md
recursive-include src *.md

# Include the license file
include LICENSE

# Exclude build configs
exclude *.sh
exclude *.toml
exclude *.svg
exclude *.yml
exclude *.yaml

# exclude tests from package
recursive-exclude tests *
recursive-exclude site *
exclude tests

# Exclude the documentation files
recursive-exclude docs *
exclude docs

# Include the Requirements
include requirements.txt
recursive-include _requirements *.tx;t

# Exclude Makefile
exclude Makefile

prune .git
prune .github
prune temp*
prune test*
```

## File: `README.md`
```markdown
<div align='center'>

<h1>
  Build custom inference servers in pure Python
  <br/>
</h1> 
<h4>
  Define exactly how inference works for models, agents, RAG, or pipelines. 
  <br/>
  Control batching, routing, streaming, and orchestration without MLOps glue or config files.
</h4> 

<img alt="Lightning" src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/ls_banner2.png" width="800px" style="max-width: 100%;">

&nbsp; 
</div>

<div align='center'>
  
<pre>
✅ Custom inference logic  ✅ 2× faster than FastAPI     ✅ Agents, RAG, pipelines, more
✅ Custom logic + control  ✅ Any PyTorch model          ✅ Self-host or managed        
✅ Multi-GPU autoscaling   ✅ Batching + streaming       ✅ BYO model or vLLM           
✅ No MLOps glue code      ✅ Easy setup in Python       ✅ Serverless support          

</pre>

<div align='center'>

[![PyPI Downloads](https://static.pepy.tech/badge/litserve)](https://pepy.tech/projects/litserve)
[![Discord](https://img.shields.io/discord/1077906959069626439?label=Get%20help%20on%20Discord)](https://discord.gg/WajDThKAur)
![cpu-tests](https://github.com/Lightning-AI/litserve/actions/workflows/ci-testing.yml/badge.svg)
[![codecov](https://codecov.io/gh/Lightning-AI/litserve/graph/badge.svg?token=SmzX8mnKlA)](https://codecov.io/gh/Lightning-AI/litserve)
[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/Lightning-AI/litserve/blob/main/LICENSE)

</div>
</div>
<div align="center">
  <div style="text-align: center;">
    <a target="_blank" href="#quick-start" style="margin: 0 10px;">Quick start</a> •
    <a target="_blank" href="#featured-examples" style="margin: 0 10px;">Examples</a> •
    <a target="_blank" href="#features" style="margin: 0 10px;">Features</a> •
    <a target="_blank" href="#performance" style="margin: 0 10px;">Performance</a> •
    <a target="_blank" href="#host-anywhere" style="margin: 0 10px;">Hosting</a> •
    <a target="_blank" href="https://lightning.ai/docs/litserve?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme" style="margin: 0 10px;">Docs</a>
  </div>
</div>

&nbsp;

<div align="center">
<a target="_blank" href="https://lightning.ai/docs/litserve/home/get-started?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">
  <img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/get-started-badge.svg" height="36px" alt="Get started"/>
</a>
</div>

&nbsp; 

# Why LitServe?
Most serving tools (vLLM, etc..) are built for a single model type and enforce rigid abstractions. They work well until you need custom logic, multiple models, agents, or non standard pipelines. LitServe lets you write your own inference engine in Python. You define how requests are handled, how models are loaded, how batching and routing work, and how outputs are produced. LitServe handles performance, concurrency, scaling, and deployment. Use LitServe to build inference APIs, agents, chatbots, RAG systems, MCP servers, or multi model pipelines. 

Run it locally, self host anywhere, or deploy with one click on [Lightning AI](https://lightning.ai/litserve?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme).

&nbsp;

# Want the easiest way to host inference?
Over 380,000 developers use [Lightning Cloud](https://lightning.ai/?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme), the simplest way to run LitServe without managing infrastructure. Deploy with one command, get autoscaling GPUs, monitoring, and a free tier. No cloud setup required. Or self host anywhere.

# Quick start

Install LitServe via pip ([more options](https://lightning.ai/docs/litserve/home/install)):

```bash
pip install litserve
```

[Example 1](#inference-engine-example): Toy inference pipeline with multiple models.   
[Example 2](#agent-example): Minimal agent to fetch the news (with OpenAI API).    
([Advanced examples](#featured-examples)):    

### Inference engine example   

```python
import litserve as ls

# define the api to include any number of models, dbs, etc...
class InferenceEngine(ls.LitAPI):
    def setup(self, device):
        self.text_model = lambda x: x**2
        self.vision_model = lambda x: x**3

    def predict(self, request):
        x = request["input"]    
        # perform calculations using both models
        a = self.text_model(x)
        b = self.vision_model(x)
        c = a + b
        return {"output": c}

if __name__ == "__main__":
    # 12+ features like batching, streaming, etc...
    server = ls.LitServer(InferenceEngine(max_batch_size=1), accelerator="auto")
    server.run(port=8000)
```

Deploy for free to [Lightning cloud](#hosting-options) (or self host anywhere):

```bash
# Deploy for free with autoscaling, monitoring, etc...
lightning deploy server.py --cloud

# Or run locally (self host anywhere)
lightning deploy server.py
# python server.py
```

Test the server: Simulate an http request (run this on any terminal):
```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"input": 4.0}'
```

### Agent example

```python
import re, requests, openai
import litserve as ls

class NewsAgent(ls.LitAPI):
    def setup(self, device):
        self.openai_client = openai.OpenAI(api_key="OPENAI_API_KEY")

    def predict(self, request):
        website_url = request.get("website_url", "https://text.npr.org/")
        website_text = re.sub(r'<[^>]+>', ' ', requests.get(website_url).text)

        # ask the LLM to tell you about the news
        llm_response = self.openai_client.chat.completions.create(
           model="gpt-3.5-turbo", 
           messages=[{"role": "user", "content": f"Based on this, what is the latest: {website_text}"}],
        )
        output = llm_response.choices[0].message.content.strip()
        return {"output": output}

if __name__ == "__main__":
    server = ls.LitServer(NewsAgent())
    server.run(port=8000)
```
Test it:
```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"website_url": "https://text.npr.org/"}'
```

&nbsp;

# Key benefits   

A few key benefits:

- **Deploy any pipeline or model**: Agents, pipelines, RAG, chatbots, image models, video, speech, text, etc...
- **No MLOps glue:** LitAPI lets you build full AI systems (multi-model, agent, RAG) in one place ([more](https://lightning.ai/docs/litserve/api-reference/litapi?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)).   
- **Instant setup:** Connect models, DBs, and data in a few lines with `setup()` ([more](https://lightning.ai/docs/litserve/api-reference/litapi?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme#setup)).    
- **Optimized:** autoscaling, GPU support, and fast inference included ([more](https://lightning.ai/docs/litserve/api-reference/litserver?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)).    
- **Deploy anywhere:** self-host or one-click deploy with Lightning ([more](https://lightning.ai/docs/litserve/features/deploy-on-cloud?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)).
- **FastAPI for AI:** Built on FastAPI but optimized for AI - 2× faster with AI-specific multi-worker handling ([more]((#performance))).   
- **Expert-friendly:** Use vLLM, or build your own with full control over batching, caching, and logic ([more](https://lightning.ai/lightning-ai/studios/deploy-a-private-llama-3-2-rag-api?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)).    

> ⚠️ Not a vLLM or Ollama alternative out of the box. LitServe gives you lower-level flexibility to build what they do (and more) if you need it.

&nbsp;

# Featured examples    
Here are examples of inference pipelines for common model types and use cases.      
  
<pre>
<strong>Toy model:</strong>      <a target="_blank" href="#define-a-server">Hello world</a>
<strong>LLMs:</strong>           <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-llama-3-2-vision-with-litserve?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Llama 3.2</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/openai-fault-tolerant-proxy-server?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">LLM Proxy server</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-ai-agent-with-tool-use?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Agent with tool use</a>
<strong>RAG:</strong>            <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-private-llama-3-2-rag-api?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">vLLM RAG (Llama 3.2)</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-private-llama-3-1-rag-api?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">RAG API (LlamaIndex)</a>
<strong>NLP:</strong>            <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-any-hugging-face-model-instantly?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Hugging face</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-hugging-face-bert-model?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">BERT</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-text-embedding-api-with-litserve?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Text embedding API</a>
<strong>Multimodal:</strong>     <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-open-ai-clip-with-litserve?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">OpenAI Clip</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-multi-modal-llm-with-minicpm?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">MiniCPM</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-phi3-5-vision-api-with-litserve?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Phi-3.5 Vision Instruct</a>, <a target="_blank" href="https://lightning.ai/bhimrajyadav/studios/deploy-and-chat-with-qwen2-vl-using-litserve?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Qwen2-VL</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-multi-modal-llm-with-pixtral?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Pixtral</a>
<strong>Audio:</strong>          <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-open-ai-s-whisper-model?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Whisper</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-an-music-generation-api-with-meta-s-audio-craft?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">AudioCraft</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-an-audio-generation-api?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">StableAudio</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-noise-cancellation-api-with-deepfilternet?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Noise cancellation (DeepFilterNet)</a>
<strong>Vision:</strong>         <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-private-api-for-stable-diffusion-2?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Stable diffusion 2</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-an-image-generation-api-with-auraflow?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">AuraFlow</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-an-image-generation-api-with-flux?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Flux</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-super-resolution-image-api-with-aura-sr?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Image Super Resolution (Aura SR)</a>,
                <a target="_blank" href="https://lightning.ai/bhimrajyadav/studios/deploy-background-removal-api-with-litserve?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Background Removal</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-controlled-image-generation-api-controlnet?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Control Stable Diffusion (ControlNet)</a>
<strong>Speech:</strong>         <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-voice-clone-api-coqui-xtts-v2-model?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Text-speech (XTTS V2)</a>, <a target="_blank" href="https://lightning.ai/bhimrajyadav/studios/deploy-a-speech-generation-api-using-parler-tts-powered-by-litserve?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Parler-TTS</a>
<strong>Classical ML:</strong>   <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-random-forest-with-litserve?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Random forest</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-xgboost-with-litserve?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">XGBoost</a>
<strong>Miscellaneous:</strong>  <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-an-media-conversion-api-with-ffmpeg?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">Media conversion API (ffmpeg)</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-both-pytorch-and-tensorflow-in-a-single-api?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">PyTorch + TensorFlow in one API</a>, <a target="_blank" href="https://lightning.ai/lightning-ai/studios/openai-fault-tolerant-proxy-server?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">LLM proxy server</a>
</pre>
</pre>

[Browse 100+ community-built templates](https://lightning.ai/studios?section=serving&utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)

&nbsp;

# Host anywhere

Self-host with full control, or deploy with [Lightning AI](https://lightning.ai/?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme) in seconds with autoscaling, security, and 99.995% uptime.  
**Free tier included. No setup required. Run on your cloud**   

```bash
lightning deploy server.py --cloud
```

https://github.com/user-attachments/assets/ff83dab9-0c9f-4453-8dcb-fb9526726344

&nbsp;

# Features

<div align='center'>

| [Feature](https://lightning.ai/docs/litserve/features?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)               | Self Managed                      | [Fully Managed on Lightning](https://lightning.ai/deploy?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)         |
|----------------------------------------------------------------------|-----------------------------------|------------------------------------|
| Docker-first deployment          | ✅ DIY                             | ✅ One-click deploy                |
| Cost                             | ✅ Free (DIY)                      | ✅ Generous [free tier](https://lightning.ai/pricing?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme) with pay as you go                |
| Full control                     | ✅                                 | ✅                                 |
| Use any engine (vLLM, etc.)      | ✅                                 | ✅ vLLM, Ollama, LitServe, etc.    |
| Own VPC                          | ✅ (manual setup)                  | ✅ Connect your own VPC            |
| [(2x)+ faster than plain FastAPI](#performance)                                               | ✅       | ✅                                 |
| [Bring your own model](https://lightning.ai/docs/litserve/features/full-control?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)              | ✅       | ✅                                 |
| [Build compound systems (1+ models)](https://lightning.ai/docs/litserve/home?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)                 | ✅       | ✅                                 |
| [GPU autoscaling](https://lightning.ai/docs/litserve/features/gpu-inference?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)                  | ✅       | ✅                                 |
| [Batching](https://lightning.ai/docs/litserve/features/batching?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)                              | ✅       | ✅                                 |
| [Streaming](https://lightning.ai/docs/litserve/features/streaming?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)                            | ✅       | ✅                                 |
| [Worker autoscaling](https://lightning.ai/docs/litserve/features/autoscaling?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)                 | ✅       | ✅                                 |
| [Serve all models: (LLMs, vision, etc.)](https://lightning.ai/docs/litserve/examples?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)         | ✅       | ✅                                 |
| [Supports PyTorch, JAX, TF, etc...](https://lightning.ai/docs/litserve/features/full-control?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme) | ✅       | ✅                                 |
| [OpenAPI compliant](https://www.openapis.org/)                                                | ✅       | ✅                                 |
| [Open AI compatibility](https://lightning.ai/docs/litserve/features/open-ai-spec?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)             | ✅       | ✅                                 |
| [MCP server support](https://lightning.ai/docs/litserve/features/mcp?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)                         | ✅       | ✅                                 |
| [Asynchronous](https://lightning.ai/docs/litserve/features/async-concurrency?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)                 | ✅       | ✅                                 |
| [Authentication](https://lightning.ai/docs/litserve/features/authentication?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)                  | ❌ DIY   | ✅ Token, password, custom         |
| GPUs                             | ❌ DIY                             | ✅ 8+ GPU types, H100s from $1.75  |
| Load balancing                   | ❌                                 | ✅ Built-in                        |
| Scale to zero (serverless)       | ❌                                 | ✅ No machine runs when idle       |
| Autoscale up on demand           | ❌                                 | ✅ Auto scale up/down              |
| Multi-node inference             | ❌                                 | ✅ Distribute across nodes         |
| Use AWS/GCP credits              | ❌                                 | ✅ Use existing cloud commits      |
| Versioning                       | ❌                                 | ✅ Make and roll back releases     |
| Enterprise-grade uptime (99.95%) | ❌                                 | ✅ SLA-backed                      |
| SOC2 / HIPAA compliance          | ❌                                 | ✅ Certified & secure              |
| Observability                    | ❌                                 | ✅ Built-in, connect 3rd party tools|
| CI/CD ready                      | ❌                                 | ✅ Lightning SDK                   |
| 24/7 enterprise support          | ❌                                 | ✅ Dedicated support               |
| Cost controls & audit logs       | ❌                                 | ✅ Budgets, breakdowns, logs       |
| Debug on GPUs                    | ❌                                 | ✅ Studio integration              |
| [20+ features](https://lightning.ai/docs/litserve/features?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme)                    | -                                 | -                                  |

</div>

&nbsp;

# Performance  
LitServe is designed for AI workloads. Specialized multi-worker handling delivers a minimum **2x speedup over FastAPI**.    

Additional features like batching and GPU autoscaling can drive performance well beyond 2x, scaling efficiently to handle more simultaneous requests than FastAPI and TorchServe.
    
Reproduce the full benchmarks [here](https://lightning.ai/docs/litserve/home/benchmarks?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme) (higher is better).  

<div align="center">
  <img alt="LitServe" src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/ls_charts_v6.png" width="1000px" style="max-width: 100%;">
</div> 

These results are for image and text classification ML tasks. The performance relationships hold for other ML tasks (embedding, LLM serving, audio, segmentation, object detection, summarization etc...).   
    
***💡 Note on LLM serving:*** For high-performance LLM serving (like Ollama/vLLM), integrate [vLLM with LitServe](https://lightning.ai/lightning-ai/studios/deploy-a-private-llama-3-2-rag-api?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme), use [LitGPT](https://github.com/Lightning-AI/litgpt?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme#deploy-an-llm), or build your custom vLLM-like server with LitServe. Optimizations like kv-caching, which can be done with LitServe, are needed to maximize LLM performance.

&nbsp;


# Community
LitServe is a [community project accepting contributions](https://lightning.ai/docs/litserve/community?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme) - Let's make the world's most advanced AI inference engine.

💬 [Get help on Discord](https://discord.com/invite/XncpTy7DSt)    
📋 [License: Apache 2.0](https://github.com/Lightning-AI/litserve/blob/main/LICENSE)    
```

## File: `pyproject.toml`
```
[metadata]
license_file = "LICENSE"
description-file = "README.md"

[project]
name = "litserve"
dynamic = ["version"]
description = "Lightweight AI server."
readme = "README.md"
license = {text = "Apache-2.0"}
authors = [
    {name = "Lightning-AI et al.", email = "community@lightning.ai"}
]
requires-python = ">=3.10"
keywords = ["deep learning", "pytorch", "AI"]
classifiers = [
    "Environment :: Console",
    "Natural Language :: English",
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

dependencies = [
    "fastapi>=0.112",
    "pyzmq>=22.0.0",
    "uvicorn[standard]>=0.29.0",
]

[project.urls]
Homepage = "https://github.com/Lightning-AI/litserve"
"Bug Tracker" = "https://github.com/Lightning-AI/litserve/issues"
Documentation = "https://lightning-ai.github.io/litserve/"
"Source Code" = "https://github.com/Lightning-AI/litserve"
Download = "https://github.com/Lightning-AI/litserve"

[project.scripts]
litserve = "litserve.__main__:main"
lightning = "litserve.cli:main"


[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.version]
path = "src/litserve/__about__.py"
pattern = "__version__ = \"(?P<version>.+)\""


[tool.hatch.metadata]
allow-direct-references = true

[tool.check-manifest]
ignore = [
    "*.yml",
    ".github",
    ".github/*"
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "pass",
]

[tool.codespell]
#skip = '*.py'
quiet-level = 3
# comma separated list of words; waiting for:
#  https://github.com/codespell-project/codespell/issues/2839#issuecomment-1731601603
# also adding links until they ignored by its: nature
#  https://github.com/codespell-project/codespell/issues/2243#issuecomment-1732019960
#ignore-words-list = ""

[tool.docformatter]
recursive = true
wrap-summaries = 120
wrap-descriptions = 120
blank = true


#[tool.mypy]
#files = [
#    "src",
#]
#install_types = true
#non_interactive = true
#disallow_untyped_defs = true
#ignore_missing_imports = true
#show_error_codes = true
#warn_redundant_casts = true
#warn_unused_configs = true
#warn_unused_ignores = true
#allow_redefinition = true
## disable this rule as the Trainer attributes are defined in the connectors, not in its __init__
#disable_error_code = "attr-defined"
## style choices
#warn_no_return = false


[tool.ruff]
line-length = 120
target-version = "py310"
# Enable Pyflakes `E` and `F` codes by default.
lint.select = [
    "E", "W",  # see: https://pypi.org/project/pycodestyle
    "F",  # see: https://pypi.org/project/pyflakes
    "N",  # see: https://pypi.org/project/pep8-naming
#    "D",  # see: https://pypi.org/project/pydocstyle
    "I", # implementation for isort
    "UP", # implementation for pyupgrade
    "RUF100", # implementation for yesqa
]
lint.extend-select = [
    "C4",  # see: https://pypi.org/project/flake8-comprehensions
    "PT",  # see: https://pypi.org/project/flake8-pytest-style
    "RET",  # see: https://pypi.org/project/flake8-return
    "SIM",  # see: https://pypi.org/project/flake8-simplify
]
lint.ignore = [
    "E731",  # Do not assign a lambda expression, use a def
    "UP045",  # TODO: non-pep604-annotation-optional
    "UP007",  # TODO: non-pep604-annotation-union
]
# Exclude a variety of commonly ignored directories.
exclude = [
    ".eggs",
    ".git",
    ".mypy_cache",
    ".ruff_cache",
    "__pypackages__",
    "_build",
    "build",
    "dist",
    "docs"
]

[tool.ruff.lint.per-file-ignores]
"setup.py" = ["D100", "SIM115"]
"__about__.py" = ["D100"]
"__init__.py" = ["D100"]

[tool.ruff.lint.pydocstyle]
# Use Google-style docstrings.
convention = "google"

#[tool.ruff.pycodestyle]
#ignore-overlong-task-comments = true

[tool.ruff.lint.mccabe]
# Unlike Flake8, default to a complexity level of 10.
max-complexity = 10

[dependency-groups]
dev = [
    "asgi-lifespan>=2.1.0",
    "coverage[toml]>=7.5.3",
    "fastmcp>=2.9.2 ; python_full_version >= '3.10'",
    "httpx>=0.27.0",
    "lightning>2.0.0",
    "mypy==1.19.1",
    "numpy<3.0",
    "openai>=1.12.0",
    "pillow>=11.3.0",
    "psutil>=7.0.0",
    "pytest>=8.0",
    "pytest-asyncio>=1.0.0",
    "pytest-cov>=6.2.1",
    "pytest-retry>=1.6.3",
    "python-multipart>=0.0.20",
    "requests>=2.32.4",
    "torch>2.0.0",
    "transformers>=4.53.0",
    "uvloop>=0.21.0 ; sys_platform != 'win32'",
    "tenacity>=9.1.2",
    "jsonargparse",
    "rich",
    "torchvision>=0.22.1",
]
```

## File: `pytest.ini`
```
[pytest]
markers =
    unit: unit tests
    integration: integration tests
    e2e: end-to-end tests
addopts = --strict-markers --color=yes --disable-pytest-warnings
filterwarnings =
    error::FutureWarning
xfail_strict = true
junit_duration_report = call
```

## File: `_requirements/perf.txt`
```
uvloop>=0.21.0
tenacity>=9.1.2
jsonargparse
rich>=14.0.0
```

## File: `src/litserve/__about__.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
__version__ = "0.2.17"
__author__ = "Lightning-AI et al."
__author_email__ = "community@lightning.ai"
__license__ = "Apache-2.0"
__copyright__ = f"Copyright (c) 2024, {__author__}."
__homepage__ = "https://github.com/Lightning-AI/litserve"
__docs__ = "Lightweight AI server."

__all__ = [
    "__author__",
    "__author_email__",
    "__copyright__",
    "__docs__",
    "__homepage__",
    "__license__",
    "__version__",
]
```

## File: `src/litserve/__init__.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from litserve import test_examples
from litserve.__about__ import *  # noqa: F403
from litserve.api import LitAPI
from litserve.callbacks import Callback
from litserve.loggers import Logger
from litserve.server import LitServer, Request, Response
from litserve.specs import OpenAIEmbeddingSpec, OpenAISpec
from litserve.utils import configure_logging, set_trace, set_trace_if_debug

configure_logging()

__all__ = [
    "Callback",
    "LitAPI",
    "LitServer",
    "Logger",
    "OpenAISpec",
    "OpenAIEmbeddingSpec",
    "Request",
    "Response",
    "set_trace",
    "set_trace_if_debug",
    "test_examples",
]
```

## File: `src/litserve/__main__.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, RawTextHelpFormatter

from litserve.docker_builder import dockerize


class LitFormatter(ArgumentDefaultsHelpFormatter, RawTextHelpFormatter): ...


def main():
    parser = ArgumentParser(description="CLI for LitServe", formatter_class=LitFormatter)
    subparsers = parser.add_subparsers(
        dest="command",
        title="Commands",
    )

    # dockerize sub-command
    dockerize_parser = subparsers.add_parser(
        "dockerize",
        help="Generate a Dockerfile for the given server code.",
        description="Generate a Dockerfile for the given server code.\nExample usage:"
        " litserve dockerize server.py --port 8000 --gpu",
        formatter_class=LitFormatter,
    )
    dockerize_parser.add_argument(
        "server_filename",
        type=str,
        help="The path to the server file. Example: server.py or app.py.",
    )
    dockerize_parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="The port to expose in the Docker container.",
    )
    dockerize_parser.add_argument(
        "--gpu",
        default=False,
        action="store_true",
        help="Whether to use a GPU-enabled Docker image.",
    )
    dockerize_parser.set_defaults(func=lambda args: dockerize(args.server_filename, args.port, args.gpu))
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
```

## File: `src/litserve/api.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import inspect
import json
import warnings
from abc import ABC
from collections.abc import Awaitable, Callable
from queue import Queue
from typing import TYPE_CHECKING, Optional, Union

from pydantic import BaseModel

from litserve.specs.base import LitSpec
from litserve.utils import _TimedInitMeta

if TYPE_CHECKING:
    from litserve.loops.base import LitLoop
    from litserve.mcp import MCP


class LitAPI(ABC, metaclass=_TimedInitMeta):
    """Define inference logic for the model.

    LitAPI is the core abstraction for serving AI models with LitServe. It provides a clean
    interface for model loading, request processing, and response generation with automatic
    optimizations like batching, streaming, and async processing.

    Core Workflow:
        1. **setup()**: Load and initialize the model once per worker
        2. **decode_request()**: Convert HTTP request to model input format
        3. **predict()**: Run model inference on the input
        4. **encode_response()**: Convert model output to HTTP response format

    Quick Start:
        ```python
        import litserve as ls

        class MyAPI(ls.LitAPI):
            def setup(self, device):
                self.model = lambda x: x**2

            def predict(self, x):
                return self.model(x["input"])

        server = ls.LitServer(MyAPI())
        server.run()
        ```

    Required Methods:
        setup(device): Initialize the model and resources
        predict(x): Core inference logic

    Optional Methods:
        decode_request(request): Transform HTTP requests to model input
        encode_response(output): Transform model outputs to HTTP responses
        batch(inputs)/unbatch(outputs): Custom batching logic

    Configuration:
        max_batch_size: Batch multiple requests for better GPU utilization. Defaults to 1.
        batch_timeout: Wait time for batch to fill (seconds). Defaults to 0.0.
        stream: Enable streaming responses for real-time output. Defaults to False.
        api_path: URL endpoint path. Defaults to "/predict".
        enable_async: Enable async/await for non-blocking operations. Defaults to False.
        spec: API specification (e.g., OpenAISpec for OpenAI compatibility). Defaults to None.
        mcp: Model Context Protocol integration for AI assistants. Defaults to None.

    Examples:
        Batched GPU Inference:
        ```python
        class BatchedAPI(ls.LitAPI):
            def setup(self, device):
                self.model = load_model().to(device)

            def predict(self, batch):
                return self.model(batch)

        api = BatchedAPI(max_batch_size=8, batch_timeout=0.1)
        ```

        Streaming LLM:
        ```python
        class StreamingLLM(ls.LitAPI):
            def setup(self, device):
                self.model = load_llm()

            def predict(self, prompt):
                for token in self.model.generate_stream(prompt):
                    yield token

        api = StreamingLLM(stream=True)
        ```

        OpenAI-Compatible:
        ```python
        from litserve.specs import OpenAISpec

        class ChatAPI(ls.LitAPI):
            def setup(self, device):
                self.model = load_chat_model()

            def predict(self, messages):
                return self.model.chat(messages)

        api = ChatAPI(spec=OpenAISpec())
        ```

    Performance Tips:
        - Use batching for GPU models to maximize utilization
        - Enable streaming for operations taking >1 second
        - Use async for I/O-bound operations (databases, external APIs)
        - Load models in setup(), not __init__
        - Monitor GPU memory usage with larger batch sizes

    See Also:
        - LitServer: Server class for hosting APIs
        - LitSpec: API specifications for standard interfaces

    """

    _stream: bool = False
    _default_unbatch: Optional[Callable] = None
    _spec: Optional[LitSpec] = None
    _device: Optional[str] = None
    _logger_queue: Optional[Queue] = None
    request_timeout: Optional[float] = None

    def __init__(
        self,
        max_batch_size: int = 1,
        batch_timeout: float = 0.0,
        api_path: str = "/predict",
        stream: bool = False,
        loop: Optional[Union[str, "LitLoop"]] = "auto",
        spec: Optional[LitSpec] = None,
        mcp: Optional["MCP"] = None,
        enable_async: bool = False,
    ):
        """Initialize LitAPI with configuration options."""

        if max_batch_size <= 0:
            raise ValueError("max_batch_size must be greater than 0")

        if batch_timeout < 0:
            raise ValueError("batch_timeout must be greater than or equal to 0")

        if isinstance(spec, LitSpec):
            stream = spec.stream

        if loop is None:
            loop = "auto"

        if isinstance(loop, str) and loop != "auto":
            raise ValueError("loop must be an instance of _BaseLoop or 'auto'")

        if not api_path.startswith("/"):
            raise ValueError(
                "api_path must start with '/'. "
                "Please provide a valid api path like '/predict', '/classify', or '/v1/predict'"
            )

        # Check if the batch and unbatch methods are overridden in the lit_api instance
        batch_overridden = self.batch.__code__ is not LitAPI.batch.__code__
        unbatch_overridden = self.unbatch.__code__ is not LitAPI.unbatch.__code__

        if batch_overridden and unbatch_overridden and max_batch_size == 1:
            warnings.warn(
                "The LitServer has both batch and unbatch methods implemented, "
                "but the max_batch_size parameter was not set."
            )

        self._api_path = api_path
        self.stream = stream
        self._loop = loop
        self._spec = spec
        self.max_batch_size = max_batch_size
        self.batch_timeout = batch_timeout
        self.enable_async = enable_async
        self._validate_async_methods()
        self.mcp = mcp
        if mcp:
            mcp._connect(self)

    def _validate_async_methods(self):
        """Validate that async methods are properly implemented when enable_async is True."""
        if not self.enable_async:
            return

        # Define validation rules for each method
        validation_rules = {
            "decode_request": {
                "required_types": [asyncio.iscoroutinefunction, inspect.isasyncgenfunction],
                "error_type": "warning",
                "message": "should be an async function or async generator when enable_async=True",
            },
            "encode_response": {
                "required_types": [asyncio.iscoroutinefunction, inspect.isasyncgenfunction],
                "error_type": "warning",
                "message": "should be an async function or async generator when enable_async=True",
            },
            "predict": {
                "required_types": [inspect.isasyncgenfunction, asyncio.iscoroutinefunction],
                "error_type": "error",
                "message": "must be an async generator or async function when enable_async=True",
            },
        }

        errors = []
        warnings_list = []

        for method_name, rules in validation_rules.items():
            method_obj = getattr(self, method_name)

            # Check if method satisfies any of the required types
            is_valid = any(check_func(method_obj) for check_func in rules["required_types"])

            if not is_valid:
                message = f"{method_name} {rules['message']}"

                if rules["error_type"] == "error":
                    errors.append(message)
                else:
                    warnings_list.append(message)

        # Emit warnings
        for warning_msg in warnings_list:
            warnings.warn(f"{warning_msg}. LitServe will asyncify the method.", UserWarning)

        # Raise errors if any
        if errors:
            error_msg = "Async validation failed:\n" + "\n".join(f"- {err}" for err in errors)
            raise ValueError(error_msg)

    def setup(self, device):
        """Setup the model so it can be called in `predict`."""
        pass

    def decode_request(self, request, **kwargs):
        """Convert the request payload to your model input."""
        if self._spec:
            return self._spec.decode_request(request, **kwargs)
        return request

    def batch(self, inputs):
        """Convert a list of inputs to a batched input."""
        # consider assigning an implementation when starting server
        # to avoid the runtime cost of checking (should be negligible)
        if hasattr(inputs[0], "__torch_function__"):
            import torch

            return torch.stack(inputs)
        if inputs[0].__class__.__name__ == "ndarray":
            import numpy

            return numpy.stack(inputs)

        return inputs

    def predict(self, x, **kwargs):
        """Run the model on the input and return or yield the output.

        When batching is enabled (max_batch_size > 1), this method receives
        a batched input and must return a list-like structure where each element
        corresponds to one input in the batch.

        Returns:
            For non-batched mode: Single prediction output
            For batched mode: List, tuple, or array with one output per input

        """
        raise NotImplementedError("predict is not implemented")

    def _unbatch_no_stream(self, output):
        if isinstance(output, str):
            warnings.warn(
                "The 'predict' method returned a string instead of a list of predictions. "
                "When batching is enabled, 'predict' must return a list to handle multiple inputs correctly. "
                "Please update the 'predict' method to return a list of predictions to avoid unexpected behavior.",
                UserWarning,
            )
        elif isinstance(output, dict):
            warnings.warn(
                "The 'predict' method returned a dict instead of a list of predictions. "
                "When batching is enabled, 'predict' must return a list to handle multiple inputs correctly. "
                "For example, return [{'class_A': 0.2, 'class_B': 0.8}, {'class_A': 0.5, 'class_B': 0.5}] "
                "instead of {'class_A': [0.2, 0.5], 'class_B': [0.8, 0.5]}. "
                "Please update the 'predict' method to return a list of predictions to avoid unexpected behavior.",
                UserWarning,
            )
        elif isinstance(output, set):
            warnings.warn(
                "The 'predict' method returned a set instead of a list of predictions. "
                "When batching is enabled, 'predict' must return a list to handle multiple inputs correctly. "
                "Please update the 'predict' method to return a list of predictions to avoid unexpected behavior.",
                UserWarning,
            )
        return list(output)

    def _unbatch_stream(self, output_stream):
        for output in output_stream:
            yield list(output)

    def unbatch(self, output):
        """Convert a batched output to a list of outputs.

        When using batching, the predict method should return a list-like structure
        (list, tuple, or array) where each element corresponds to one input.

        For example, for a batch of 2 inputs, predict should return:
            [output1, output2]  # Correct

        Not:
            {"key1": [val1, val2], "key2": [val3, val4]}  # Incorrect

        If you need to return dictionaries, return a list of dicts:
            [{"key1": val1, "key2": val3}, {"key1": val2, "key2": val4}]  # Correct

        """
        if self._default_unbatch is None:
            raise ValueError(
                "Default implementation for `LitAPI.unbatch` method was not found. "
                "Please implement the `LitAPI.unbatch` method."
            )
        return self._default_unbatch(output)

    def encode_response(self, output, **kwargs):
        """Convert the model output to a response payload.

        To enable streaming, it should yield the output.

        """
        if self._spec:
            return self._spec.encode_response(output, **kwargs)
        return output

    def format_encoded_response(self, data):
        if isinstance(data, dict):
            return json.dumps(data) + "\n"
        if isinstance(data, BaseModel):
            return data.model_dump_json() + "\n"
        return data

    @property
    def stream(self):
        return self._stream

    @stream.setter
    def stream(self, value):
        self._stream = value

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, value):
        self._device = value

    def pre_setup(self, spec: Optional[LitSpec] = None):
        spec = spec or self._spec
        if self.stream:
            self._default_unbatch = self._unbatch_stream
        else:
            self._default_unbatch = self._unbatch_no_stream

        if spec:
            self._spec = spec
            spec._max_batch_size = self.max_batch_size
            spec.pre_setup(self)

    def set_logger_queue(self, queue: Queue):
        """Set the queue for logging events."""

        self._logger_queue = queue

    def log(self, key, value):
        """Log a key-value pair to the server."""
        if self._logger_queue is None:
            warnings.warn(
                f"Logging event ('{key}', '{value}') attempted without a configured logger. "
                "To track and visualize metrics, please initialize and attach a logger. "
                "If this is intentional, you can safely ignore this message."
            )
            return
        self._logger_queue.put((key, value))

    def has_active_requests(self) -> bool:
        raise NotImplementedError("has_active_requests is not implemented")

    def has_capacity(self) -> bool:
        raise NotImplementedError("has_capacity is not implemented")

    def health(self) -> Union[bool, Awaitable[bool]]:
        """Check the additional health status of the API.

        This method is used in the /health endpoint of the server to determine the health status.
        Users can extend this method to include additional health checks specific to their application.

        The default implementation is synchronous but users may optionally implement an
        ``async`` version which will be awaited by :class:`~litserve.server.LitServer`.

        Returns:
            bool: ``True`` if the API is healthy, ``False`` otherwise.

        """
        return True

    @property
    def loop(self):
        if self._loop == "auto":
            from litserve.loops.loops import get_default_loop

            self._loop = get_default_loop(self.stream, self.max_batch_size, self.enable_async)
        return self._loop

    @loop.setter
    def loop(self, value: "LitLoop"):
        self._loop = value

    @property
    def spec(self):
        return self._spec

    @spec.setter
    def spec(self, value: LitSpec):
        self._spec = value

    @property
    def api_path(self):
        if self._spec:
            return self._spec.api_path
        return self._api_path

    @api_path.setter
    def api_path(self, value: str):
        self._api_path = value
```

## File: `src/litserve/cli.py`
```python
import importlib.util
import shutil
import subprocess
import sys

from litserve.utils import is_package_installed


def _ensure_lightning_installed():
    """Ensure lightning-sdk is installed, attempting auto-installation if needed."""
    if is_package_installed("lightning_sdk"):
        return

    print("Lightning CLI not found. Installing lightning-sdk...")

    # Build list of available installers (pip first as it respects the active environment)
    installers = []
    if importlib.util.find_spec("pip"):
        installers.append([sys.executable, "-m", "pip"])
    if shutil.which("uv"):
        installers.append(["uv", "pip"])

    for installer in installers:
        try:
            subprocess.run([*installer, "install", "-U", "lightning-sdk"], check=True)
            return
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue

    sys.exit("Failed to install lightning-sdk. Run: pip install lightning-sdk")


def main():
    _ensure_lightning_installed()

    try:
        # Import the correct entry point for lightning_sdk
        from lightning_sdk.cli.entrypoint import main_cli

        # Call the lightning CLI's main function directly with our arguments
        # This bypasses the command-line entry point completely
        sys.argv[0] = "lightning"  # Make it think it was called as "lightning"
        main_cli()
    except ImportError as e:
        # If there's an issue importing or finding the right module
        print(f"Error importing lightning_sdk CLI: {e}")
        print("Please ensure `lightning-sdk` is installed correctly.")
        sys.exit(1)
```

## File: `src/litserve/connector.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import platform
import subprocess
import sys
from functools import lru_cache
from typing import Optional, Union


class _Connector:
    def __init__(self, accelerator: str = "auto", devices: Union[list[int], int, str] = "auto"):
        accelerator = self._sanitize_accelerator(accelerator)
        if accelerator in ("cpu", "cuda", "mps"):
            self._accelerator = accelerator
        elif accelerator == "auto":
            self._accelerator = self._choose_auto_accelerator()
        elif accelerator == "gpu":
            self._accelerator = self._choose_gpu_accelerator_backend()

        if devices == "auto":
            self._devices = self._accelerator_device_count()
        else:
            self._devices = devices

        self.check_devices_and_accelerators()

    def check_devices_and_accelerators(self):
        """Check if the devices are in a valid fomra and raise an error if they are not."""
        if self._accelerator in ("cuda", "mps"):
            if not isinstance(self._devices, int) and not (
                isinstance(self._devices, list) and all(isinstance(device, int) for device in self._devices)
            ):
                raise ValueError(
                    "devices must be an integer or a list of integers when using 'cuda' or 'mps', "
                    f"instead got {self._devices}"
                )
        elif self._accelerator != "cpu":
            raise ValueError(f"accelerator must be one of (cuda, mps, cpu), instead got {self._accelerator}")

    @property
    def accelerator(self):
        return self._accelerator

    @property
    def devices(self):
        return self._devices

    @staticmethod
    def _sanitize_accelerator(accelerator: Optional[str]):
        if isinstance(accelerator, str):
            accelerator = accelerator.lower()

        if accelerator not in ["auto", "cpu", "mps", "cuda", "gpu", None]:
            raise ValueError(f"accelerator must be one of 'auto', 'cpu', 'mps', 'cuda', or 'gpu'. Found: {accelerator}")

        if accelerator is None:
            return "auto"
        return accelerator

    def _choose_auto_accelerator(self):
        gpu_backend = self._choose_gpu_accelerator_backend()
        if "torch" in sys.modules and gpu_backend:
            return gpu_backend
        return "cpu"

    def _accelerator_device_count(self) -> int:
        if self._accelerator == "cuda":
            return check_cuda_with_nvidia_smi()
        return 1

    @staticmethod
    def _choose_gpu_accelerator_backend():
        if check_cuda_with_nvidia_smi() > 0:
            return "cuda"

        try:
            import torch

            if torch.backends.mps.is_available() and platform.processor() in ("arm", "arm64"):
                return "mps"
        except ImportError:
            return None

        return None


@lru_cache(maxsize=1)
def check_cuda_with_nvidia_smi() -> int:
    """Checks if CUDA is installed using the `nvidia-smi` command-line tool.

    Returns count of visible devices.

    """
    try:
        nvidia_smi_output = subprocess.check_output(["nvidia-smi", "-L"]).decode("utf-8").strip()
        devices = [el for el in nvidia_smi_output.split("\n") if el.startswith("GPU")]
        devices = [el.split(":")[0].split()[1] for el in devices]
        visible_devices = os.environ.get("CUDA_VISIBLE_DEVICES")
        if visible_devices:
            # we need check the intersection of devices and visible devices, since
            # using CUDA_VISIBLE_DEVICES=0,25 on a 4-GPU machine will yield
            # torch.cuda.device_count() == 1
            devices = [el for el in devices if el in visible_devices.split(",")]
        return len(devices)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return 0
```

## File: `src/litserve/constants.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
_DEFAULT_LIT_API_PATH = "/predict"
```

## File: `src/litserve/docker_builder.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import os
import warnings
from pathlib import Path

import litserve as ls

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate = False
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# COLOR CODES
RESET = "\u001b[0m"
RED = "\u001b[31m"
GREEN = "\u001b[32m"
BLUE = "\u001b[34m"
MAGENTA = "\u001b[35m"
BG_MAGENTA = "\u001b[45m"

# ACTION CODES
BOLD = "\u001b[1m"
UNDERLINE = "\u001b[4m"
INFO = f"{BOLD}{BLUE}[INFO]"
WARNING = f"{BOLD}{RED}[WARNING]"


def color(text, color_code, action_code=None):
    if action_code:
        return f"{action_code} {color_code}{text}{RESET}"
    return f"{color_code}{text}{RESET}"


REQUIREMENTS_FILE = "requirements.txt"
DOCKERFILE_TEMPLATE = """ARG PYTHON_VERSION=3.12
FROM python:$PYTHON_VERSION-slim

####### Add your own installation commands here #######
# RUN pip install some-package
# RUN wget https://path/to/some/data/or/weights
# RUN apt-get update && apt-get install -y <package-name>

WORKDIR /app
COPY . /app

# Install litserve and requirements
RUN pip install --no-cache-dir litserve=={version} {requirements}
EXPOSE {port}
CMD ["python", "/app/{server_filename}"]
"""

CUDA_DOCKER_TEMPLATE = """# Change CUDA and cuDNN version here
FROM nvidia/cuda:12.4.1-base-ubuntu22.04
ARG PYTHON_VERSION=3.12

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \\
        software-properties-common \\
        wget \\
    && add-apt-repository ppa:deadsnakes/ppa \\
    && apt-get update && apt-get install -y --no-install-recommends \\
        python$PYTHON_VERSION \\
        python$PYTHON_VERSION-dev \\
        python$PYTHON_VERSION-venv \\
    && wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py \\
    && python$PYTHON_VERSION get-pip.py \\
    && rm get-pip.py \\
    && ln -sf /usr/bin/python$PYTHON_VERSION /usr/bin/python \\
    && ln -sf /usr/local/bin/pip$PYTHON_VERSION /usr/local/bin/pip \\
    && python --version \\
    && pip --version \\
    && apt-get purge -y --auto-remove software-properties-common \\
    && apt-get clean \\
    && rm -rf /var/lib/apt/lists/*

####### Add your own installation commands here #######
# RUN pip install some-package
# RUN wget https://path/to/some/data/or/weights
# RUN apt-get update && apt-get install -y <package-name>

WORKDIR /app
COPY . /app

# Install litserve and requirements
RUN pip install --no-cache-dir litserve=={version} {requirements}
EXPOSE {port}
CMD ["python", "/app/{server_filename}"]
"""

# Link our documentation as the bottom of this msg
SUCCESS_MSG = """{BOLD}{MAGENTA}Dockerfile created successfully{RESET}
Update {UNDERLINE}{dockerfile_path}{RESET} to add any additional dependencies or commands.{RESET}

{BOLD}Build the container with:{RESET}
> {UNDERLINE}docker build -t litserve-model .{RESET}

{BOLD}To run the Docker container on the machine:{RESET}
> {UNDERLINE}{RUN_CMD}{RESET}

{BOLD}To push the container to a registry:{RESET}
> {UNDERLINE}docker push litserve-model{RESET}
"""


def dockerize(server_filename: str, port: int = 8000, gpu: bool = False):
    """Generate a Dockerfile for the given server code.

    Example usage:
        litserve dockerize server.py --port 8000 --gpu

    Args:
        server_filename (str): The path to the server file. Example sever.py or app.py.
        port (int, optional): The port to expose in the Docker container.
        gpu (bool, optional): Whether to use a GPU-enabled Docker image.

    """
    requirements = ""
    if os.path.exists(REQUIREMENTS_FILE):
        requirements = f"-r {REQUIREMENTS_FILE}"
    else:
        warnings.warn(
            f"requirements.txt not found at {os.getcwd()}. "
            f"Make sure to install the required packages in the Dockerfile.",
            UserWarning,
        )

    current_dir = Path.cwd()
    if not (current_dir / server_filename).is_file():
        raise FileNotFoundError(f"Server file `{server_filename}` must be in the current directory: {os.getcwd()}")

    version = ls.__version__
    if gpu:
        run_cmd = f"docker run --gpus all -p {port}:{port} litserve-model:latest"
        docker_template = CUDA_DOCKER_TEMPLATE
    else:
        run_cmd = f"docker run -p {port}:{port} litserve-model:latest"
        docker_template = DOCKERFILE_TEMPLATE
    dockerfile_content = docker_template.format(
        server_filename=server_filename,
        port=port,
        version=version,
        requirements=requirements,
    )
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)
    success_msg = SUCCESS_MSG.format(
        dockerfile_path=os.path.abspath("Dockerfile"),
        RUN_CMD=run_cmd,
        BOLD=BOLD,
        MAGENTA=MAGENTA,
        GREEN=GREEN,
        BLUE=BLUE,
        UNDERLINE=UNDERLINE,
        BG_MAGENTA=BG_MAGENTA,
        RESET=RESET,
    )
    print(success_msg)
```

## File: `src/litserve/loggers.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import functools
import logging
import multiprocessing as mp
import pickle
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, Union

from starlette.types import ASGIApp

module_logger = logging.getLogger(__name__)

if TYPE_CHECKING:  # pragma: no cover
    from litserve import LitServer


class Logger(ABC):
    def __init__(self):
        self._config = {}

    def mount(self, path: str, app: ASGIApp) -> None:
        """Mount an ASGI app endpoint to LitServer. Use this method when you want to add an additional endpoint to the
        server such as /metrics endpoint for prometheus metrics.

        Args:
            path (str): The path to mount the app to.
            app (ASGIApp): The ASGI app to mount.

        """
        self._config.update({"mount": {"path": path, "app": app}})

    @abstractmethod
    def process(self, key, value):
        """Process a log entry from the log queue.

        This method should be implemented to define the specific logic for processing
        log entries.

        Args:
            key (str): The key associated with the log entry, typically indicating the type or category of the log.
            value (Any): The value associated with the log entry, containing the actual log data.

        Raises:
            NotImplementedError: This method must be overridden by subclasses. If not, calling this method will raise
            a NotImplementedError.

        Example:
            Here is an example of a Logger that logs monitoring metrics using Prometheus:

            from prometheus_client import Counter

            class PrometheusLogger(Logger):
                def __init__(self):
                    super().__init__()
                    self._metric_counter = Counter('log_entries', 'Count of log entries')

                def process(self, key, value):
                    # Increment the Prometheus counter for each log entry
                    self._metric_counter.inc()
                    print(f"Logged {key}: {value}")

        """
        raise NotImplementedError  # pragma: no cover


class _LoggerProxy:
    def __init__(self, logger_class):
        self.logger_class = logger_class

    def create_logger(self):
        return self.logger_class()


class _LoggerConnector:
    """_LoggerConnector is responsible for connecting Logger instances with the LitServer and managing their lifecycle.

    This class handles the following tasks:
    - Manages a queue (multiprocessing.Queue) where log data is placed using the LitAPI.log method.
    - Initiates a separate process to consume the log queue and process the log data using the associated
    Logger instances.

    """

    def __init__(self, lit_server: "LitServer", loggers: Optional[Union[list[Logger], Logger]] = None):
        self._loggers = []
        self._lit_server = lit_server
        if loggers is None:
            return  # No loggers to add
        if isinstance(loggers, list):
            for logger in loggers:
                if not isinstance(logger, Logger):
                    raise ValueError("Logger must be an instance of litserve.Logger")
                self.add_logger(logger)
        elif isinstance(loggers, Logger):
            self.add_logger(loggers)
        else:
            raise ValueError("loggers must be a list or an instance of litserve.Logger")

    def _mount(self, path: str, app: ASGIApp) -> None:
        self._lit_server.app.mount(path, app)

    def add_logger(self, logger: Logger):
        self._loggers.append(logger)
        if "mount" in logger._config:
            self._mount(logger._config["mount"]["path"], logger._config["mount"]["app"])

    @staticmethod
    def _is_picklable(obj):
        try:
            pickle.dumps(obj)
            return True
        except (pickle.PicklingError, TypeError, AttributeError):
            module_logger.warning(f"Logger {obj.__class__.__name__} is not pickleable and might not work properly.")
            return False

    @staticmethod
    def _process_logger_queue(logger_proxies: list[_LoggerProxy], queue):
        loggers = [proxy if isinstance(proxy, Logger) else proxy.create_logger() for proxy in logger_proxies]
        while True:
            key, value = queue.get()
            for logger in loggers:
                try:
                    logger.process(key, value)
                except Exception as e:
                    module_logger.error(
                        f"{logger.__class__.__name__} ran into an error while processing log for entry "
                        f"with key {key} and value {value}: {e}"
                    )

    @functools.cache  # Run once per LitServer instance
    def run(self, lit_server: "LitServer"):
        queue = lit_server.logger_queue
        lit_server.litapi_connector.set_logger_queue(queue)

        # Disconnect the logger connector from the LitServer to avoid pickling issues
        self._lit_server = None

        if not self._loggers:
            return

        # Create proxies for loggers
        logger_proxies = []
        for logger in self._loggers:
            if self._is_picklable(logger):
                logger_proxies.append(logger)
            else:
                logger_proxies.append(_LoggerProxy(logger.__class__))

        module_logger.debug(f"Starting logger process with {len(logger_proxies)} loggers")
        ctx = mp.get_context("spawn")
        process = ctx.Process(
            target=_LoggerConnector._process_logger_queue,
            args=(
                logger_proxies,
                queue,
            ),
        )
        process.start()
```

## File: `src/litserve/mcp.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This module helps create MCP servers for LitServe endpoints."""

import inspect
import json
import logging
import weakref
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Optional, Union, get_args, get_origin

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.types import Receive, Scope, Send

from litserve.utils import is_package_installed

_is_mcp_installed = is_package_installed("fastmcp")


if _is_mcp_installed:
    from fastapi import FastAPI

    try:
        from mcp.server.fastmcp.server import _convert_to_content
    except ImportError:
        from mcp.server.fastmcp.utilities.func_metadata import _convert_to_content
    from mcp.server.lowlevel import Server as MCPServer
    from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
    from mcp.types import Tool as ToolType

else:
    ToolType = object

if TYPE_CHECKING:
    from litserve.api import LitAPI

logger = logging.getLogger(__name__)


def extract_input_schema(func) -> dict[str, Any]:
    """Extract JSON schema for function input parameters from a Python function. Supports regular type annotations,
    Pydantic Fields, and Pydantic BaseModel classes.

    Args:
        func: Python function to analyze

    Returns:
        Dict containing JSON schema for the function's input parameters

    """
    signature = inspect.signature(func)
    properties = {}
    required = []
    defs = {}

    # If func is a Pydantic model class, use its schema directly
    if isinstance(func, type) and issubclass(func, BaseModel):
        model_schema = func.model_json_schema()
        model_name = func.__name__

        # Extract definitions if they exist
        if "$defs" in model_schema:
            defs.update(model_schema["$defs"])

        # Remove $defs from the model schema and add it to our defs
        model_schema_clean = {k: v for k, v in model_schema.items() if k != "$defs"}
        defs[model_name] = model_schema_clean

        # Reference the model in properties
        properties[model_name.lower()] = {"$ref": f"#/$defs/{model_name}"}
        required.append(model_name.lower())

        schema = {
            "properties": properties,
            "required": required,
            "title": f"{func.__name__}Arguments",
            "type": "object",
        }
        if defs:
            schema["$defs"] = defs
        return schema

    for param_name, param in signature.parameters.items():
        # Skip *args and **kwargs
        if param.kind in (param.VAR_POSITIONAL, param.VAR_KEYWORD):
            continue

        # Get type annotation
        param_type = param.annotation

        # Check if parameter is a Pydantic BaseModel
        if param_type != inspect.Parameter.empty and isinstance(param_type, type) and issubclass(param_type, BaseModel):
            # Generate schema for the BaseModel
            model_schema = param_type.model_json_schema()
            model_name = param_type.__name__

            # Extract definitions if they exist
            if "$defs" in model_schema:
                defs.update(model_schema["$defs"])

            # Remove $defs from the model schema and add it to our defs
            model_schema_clean = {k: v for k, v in model_schema.items() if k != "$defs"}
            defs[model_name] = model_schema_clean

            # Reference the model in properties
            properties[param_name] = {"$ref": f"#/$defs/{model_name}"}

            # BaseModel parameters are always required unless they have a default
            if param.default == param.empty:
                required.append(param_name)

            continue

        # Check if parameter has a Pydantic Field as default
        field_info = None
        has_default = param.default != param.empty

        # Check if it's a Pydantic Field
        if (
            has_default
            and hasattr(param.default, "__class__")
            and (param.default.__class__.__name__ == "FieldInfo" or str(type(param.default)).find("pydantic") != -1)
        ):
            field_info = param.default

        # Convert Python type to JSON schema type
        schema_type = _python_type_to_json_schema(param_type)

        # Create property entry
        property_schema = {"title": _param_name_to_title(param_name)}
        if isinstance(schema_type, str):
            property_schema["type"] = schema_type
        else:
            property_schema.update(schema_type)

        # Add Field metadata if available
        if field_info is not None:
            # Add description if present
            if hasattr(field_info, "description") and field_info.description:
                property_schema["description"] = field_info.description

            # Add default value if present and not Undefined
            if (
                hasattr(field_info, "default")
                and field_info.default is not ...
                and not str(field_info.default).startswith("<pydantic")
            ):
                property_schema["default"] = field_info.default
            else:
                required.append(param_name)

            # Add constraints
            if hasattr(field_info, "ge") and field_info.ge is not None:
                property_schema["minimum"] = field_info.ge
            if hasattr(field_info, "le") and field_info.le is not None:
                property_schema["maximum"] = field_info.le
            if hasattr(field_info, "gt") and field_info.gt is not None:
                property_schema["exclusiveMinimum"] = field_info.gt
            if hasattr(field_info, "lt") and field_info.lt is not None:
                property_schema["exclusiveMaximum"] = field_info.lt
            if hasattr(field_info, "min_length") and field_info.min_length is not None:
                property_schema["minLength"] = field_info.min_length
            if hasattr(field_info, "max_length") and field_info.max_length is not None:
                property_schema["maxLength"] = field_info.max_length
        else:
            # Regular parameter without Field
            if not has_default:
                required.append(param_name)

        properties[param_name] = property_schema

    # Build the final schema
    schema = {"properties": properties, "required": required, "title": f"{func.__name__}Arguments", "type": "object"}

    # Add $defs if we have any BaseModel definitions
    if defs:
        schema["$defs"] = defs

    return schema


def _python_type_to_json_schema(python_type) -> Union[str, dict]:
    """Convert Python type annotation to JSON schema type string or dict."""
    if python_type == inspect.Parameter.empty:
        return "string"  # Default to string if no type annotation

    # Handle basic types
    type_mapping = {
        int: "integer",
        float: "number",
        str: "string",
        bool: "boolean",
        list: "array",
        dict: "object",
    }

    # Check if it's a basic type
    if python_type in type_mapping:
        return type_mapping[python_type]

    # Handle typing module types (list, Dict, Optional, etc.)
    origin = get_origin(python_type)
    if origin is not None:
        # Handle Optional types (Union[T, None])
        if origin is Union:
            args = get_args(python_type)
            if len(args) == 2 and type(None) in args:
                # Get the non-None type
                actual_type = next(arg for arg in args if arg is not type(None))
                base_type = _python_type_to_json_schema(actual_type)
                if isinstance(base_type, str):
                    return {"type": base_type, "nullable": True}
                base_type["nullable"] = True
                return base_type

        if origin in type_mapping:
            return type_mapping[origin]
        if origin is list:
            return "array"
        if origin is dict:
            return "object"

    # Default to string for unknown types
    return "string"


def _param_name_to_title(param_name: str) -> str:
    """Convert parameter name to a readable title."""
    # Split on underscores and capitalize each word
    words = param_name.split("_")
    return " ".join(word.capitalize() for word in words)


async def _call_handler(handler, **kwargs):
    sig = inspect.signature(handler)
    bound = sig.bind_partial(
        **{
            k: (v if not issubclass(p.annotation, BaseModel) else p.annotation(**v))
            for k, v in kwargs.items()
            for name, p in sig.parameters.items()
            if k == name
        }
    )
    return _convert_to_content(await handler(*bound.args, **bound.kwargs))


class ToolEndpointType(ToolType):
    endpoint: str


class MCP:
    """Enable Model Context Protocol (MCP) integration for LitServe APIs.

    This enables LitServe APIs to be seamlessly integrated into MCP-compatible AI systems,
    making models accessible as tools within larger AI workflows and agent frameworks.

    Quick Start:
        ```python
        from pydantic import BaseModel
        from litserve.mcp import MCP
        import litserve as ls

        class PowerRequest(BaseModel):
            input: float

        class MyLitAPI(ls.test_examples.SimpleLitAPI):
            def decode_request(self, request: PowerRequest) -> int:
                return request.input

        if __name__ == "__main__":
            mcp=MCP(description="Returns the power of a number.")
            api = MyLitAPI(mcp=mcp)
            server = ls.LitServer(api)
            server.run()
        ```

    Args:
        name:
            Tool name for MCP registration. Defaults to None (uses api_path).

            - Should be descriptive and unique within the MCP server
            - Automatically converts "/" to "_" for compatibility
            - Used by AI systems to identify and call the tool

        description:
            Human-readable description of what the tool does. Defaults to None (uses class docstring).

            - Essential for AI systems to understand when to use the tool
            - Should clearly explain the purpose and capabilities
            - Used in tool selection and orchestration

        input_schema:
            JSON Schema defining expected input format. Defaults to None (auto-extracted).

            - Describes the structure and types of input parameters
            - Helps AI systems format requests correctly
            - Auto-extracted from decode_request method if not provided

    Schema Auto-Extraction:
        If no input_schema is provided, MCP automatically extracts it from type hints in the decode_request method:

        ```python
        from pydantic import BaseModel

        class Request(BaseModel):
            input: str

        class AutoSchemaAPI(ls.LitAPI):
            def decode_request(self, request: Request)->str:
                # MCP analyzes the type hints to generate schema:
                # input: str -> {"input": {"type": "string", "title": "Input"}}
                return request.input
        ```

        Supported type annotations:
        - Basic types: `str`, `int`, `float`, `bool`, `list`, `dict`
        - Optional types: `Optional[str]`, `Union[str, None]`
        - Pydantic models: Full schema extraction with validation
        - Complex types: `list[str]`, `dict[str, Any]`

    Notes:
        - MCP integration is optional and doesn't affect non-MCP clients
        - Tool names are automatically sanitized (/ becomes _)
        - Original API endpoints remain unchanged and fully functional
        - Compatible with all LitServe features (batching, streaming, etc.)

    See Also:
        - Model Context Protocol documentation: https://lightning.ai/docs/litserve/features/mcp
        - LitAPI: Base class for API implementation
        - LitServer: Server class for hosting APIs

    """

    def __init__(
        self,
        description: Optional[str] = None,
        input_schema: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
    ):
        """
        Args:
            name: The name of the MCP tool.
            description: The description of the MCP tool.
            input_schema: The input schema of the MCP tool.
        """
        self._name = None
        self.name = name
        self.description = description
        self.input_schema = input_schema
        self._connected = False

        if not is_package_installed("fastmcp"):
            raise RuntimeError(
                "mcp package is required for MCP support. To install, run `pip install fastmcp` in the terminal."
            )

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if value and value.startswith("/"):
            value = value[1:]
        self._name = value.replace("/", "_") if value else None

    def _connect(self, lit_api: "LitAPI"):
        # avoid tight coupling between LitAPI and LitMCPSpec
        self.lit_api = weakref.proxy(lit_api)
        self._connected = True

    def as_tool(self) -> ToolEndpointType:
        if not self._connected:
            raise RuntimeError("MCP is not connected to a LitAPI.")

        name = self.name or self.lit_api.api_path
        description = self.description or self.lit_api.__doc__

        if not name or len(name) == 0:
            raise ValueError("Name is required for MCP tool")
        if not description or len(description) == 0:
            raise ValueError("Description is required for MCP tool")

        logger.debug("Creating MCP tool", extra={"name": name, "description": description})

        if self.input_schema:
            input_schema = self.input_schema
        else:
            logger.warning("No input schema provided for MCP tool. Using decode_request to extract it.")
            input_schema = extract_input_schema(self.lit_api.decode_request)

        if name.startswith("/"):
            name = name[1:]
        name = name.replace("/", "_")
        return ToolEndpointType(
            name=name,
            description=description,
            inputSchema=input_schema,
            endpoint=self.lit_api.api_path,
        )


class _MCPRequestHandler:
    def __init__(self, mcp_server: "MCPServer"):
        self.mcp_server = mcp_server
        self._session_manager = None

    @property
    def session_manager(self):
        if self._session_manager is None:
            raise RuntimeError("Session manager not initialized")
        return self._session_manager

    async def handle_streamable_http(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "lifespan":
            # Handle lifespan events (startup/shutdown)
            message = await receive()
            if message["type"] == "lifespan.startup":
                await send({"type": "lifespan.startup.complete"})
            elif message["type"] == "lifespan.shutdown":
                await send({"type": "lifespan.shutdown.complete"})
            return

        if scope["type"] != "http":
            # We only handle HTTP requests
            return

        try:
            # Handle the HTTP request through the session manager
            await self.session_manager.handle_request(scope, receive, send)
        except Exception as e:
            logger.error(f"Error handling request: {e}")
            # Properly handle errors by sending an error response
            error_message = {
                "type": "http.response.start",
                "status": 500,
                "headers": [(b"content-type", b"application/json")],
            }
            await send(error_message)

            body = json.dumps({"error": str(e)}).encode("utf-8")
            await send(
                {
                    "type": "http.response.body",
                    "body": body,
                }
            )

    # https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/fastmcp/server.py
    def streamable_http_app(self) -> Starlette:
        # Create session manager on first call (lazy initialization)
        if self._session_manager is None:
            self._session_manager = StreamableHTTPSessionManager(
                app=self.mcp_server,
                event_store=None,
                json_response=True,
                stateless=True,  # Use the stateless setting
            )

        # Create the ASGI handler
        handle_streamable_http = self.handle_streamable_http

        # Create routes
        routes: list[Mount] = [Mount("/mcp/", app=handle_streamable_http)]
        return Starlette(
            routes=routes,
        )


class _LitMCPServerConnector:
    """Connects LitServer to MCP server.

    It creates HTTP streamable MCP server with Starlette and mounts to the FastAPI app.

    """

    def __init__(self):
        self.mcp_server = MCPServer("mcp-streamable-http-stateless")
        self.tools = []
        self.request_handler = _MCPRequestHandler(self.mcp_server)
        self.tool_endpoint_connections = {}

    def add_tool(self, tool: ToolEndpointType):
        self.tool_endpoint_connections[tool.name] = tool.endpoint
        self.tools.append(tool)

    def list_tools(self) -> list[ToolEndpointType]:
        return self.tools

    @asynccontextmanager
    async def lifespan(self, app: Starlette):
        if self.request_handler._session_manager is None:
            # Ensure session manager exists
            self.request_handler._session_manager = StreamableHTTPSessionManager(
                app=self.mcp_server,
                event_store=None,
                json_response=True,
                stateless=True,
            )
        logger.debug(f"run mcp server, app: {app}")
        async with self.request_handler._session_manager.run():
            yield

    def _mount_with_fastapi(self, app: FastAPI):
        """Mounts MCP server's Starlette app to the FastAPI app.

        Args:
            app: LitServer's FastAPI app to mount the MCP server to.

        """

        @self.mcp_server.list_tools()
        async def _list_tools():  # must be async
            tools = self.list_tools()
            logger.debug(f"list tools called, returning: {tools}")
            return tools

        @self.mcp_server.call_tool()
        async def _call_tool(name: str, arguments: dict):
            try:
                endpoint_path = self.tool_endpoint_connections[name]
                logger.debug(f"call tool called, endpoint: {endpoint_path}, arguments: {arguments}")
                if endpoint_path is None:
                    raise ValueError(f"Tool {name} not found")

                logger.debug(f"call tool called, endpoint: {endpoint_path}, arguments: {arguments}")
                for route in app.routes:
                    if route.path == endpoint_path:
                        handler = route.endpoint
                        break
                else:
                    raise ValueError(f"Endpoint {endpoint_path} not found")
                logger.debug(f"call tool called, returning: {handler}")
                return await _call_handler(handler, **arguments)
            except Exception as e:
                logger.error(f"Error calling tool {name}: {e}")
                raise e

        starlette_app = self.request_handler.streamable_http_app()
        app.mount("/", starlette_app, name="mcp")

    def connect_mcp_server(self, mcp_tools: list[ToolType], app: FastAPI):
        """LitServer calls this method to connect MCP server to the FastAPI app.

        Args:
            mcp_tools: List of MCP tools to connect to the MCP server.
            app: LitServer's FastAPI app to mount the MCP server to.

        """

        if len(mcp_tools) == 0:
            return

        for tool in mcp_tools:
            self.add_tool(tool)

        logger.warning(
            "MCP support is in beta and APIs are subject to change. Please report any issues to https://github.com/Lightning-AI/litserve/issues"
        )

        self._mount_with_fastapi(app)

        logger.info(
            "================================================"
            "\n🎉 Enabled MCP server ⚡\n"
            ""
            "To integrate with Claude desktop, add the following to your Claude desktop settings:\n"
            "Install mcp-remote with `npm install -g mcp-remote`\n\n"
            """{
  "mcpServers": {
    "litserve": {
      "command": "npx",
      "args": [ "mcp-remote", "https://8000-YOUR_HOST_NAME.cloudspaces.litng.ai/mcp/"] # replace url with your server url + /mcp/
    }
  }
}\n"""  # noqa: E501
            "================================================\n"
        )
```

## File: `src/litserve/middlewares.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import multiprocessing
from typing import Optional

from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp, Message, Receive, Scope, Send

logger = logging.getLogger(__name__)


class MaxSizeMiddleware(BaseHTTPMiddleware):
    """Rejects requests with a payload that is too large."""

    def __init__(
        self,
        app: ASGIApp,
        *,
        max_size: Optional[int] = None,
    ) -> None:
        self.app = app
        self.max_size = max_size

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        total_size = 0

        async def rcv() -> Message:
            nonlocal total_size
            message = await receive()
            chunk_size = len(message.get("body", b""))
            total_size += chunk_size
            if self.max_size is not None and total_size > self.max_size:
                raise HTTPException(413, "Payload too large")
            return message

        await self.app(scope, rcv, send)


class RequestCountMiddleware(BaseHTTPMiddleware):
    """Adds a header to the response with the number of active requests."""

    def __init__(self, app: ASGIApp, active_counter: multiprocessing.Value) -> None:
        self.app = app
        self.active_counter = active_counter

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http" or (scope["type"] == "http" and scope["path"] in ["/", "/health", "/metrics"]):
            await self.app(scope, receive, send)
            return

        self.active_counter.value += 1
        await self.app(scope, receive, send)
        self.active_counter.value -= 1
```

## File: `src/litserve/python_client.py`
```python
client_template = """# This file is auto-generated by LitServe.
# Disable auto-generation by setting `generate_client_file=False` in `LitServer.run()`.

import requests

response = requests.post("http://127.0.0.1:{PORT}/predict", json={{"input": 4.0}})
print(f"Status: {{response.status_code}}\\nResponse:\\n {{response.text}}")
"""
```

## File: `src/litserve/server.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import contextlib
import copy
import inspect
import json
import logging
import multiprocessing as mp
import os
import pickle
import secrets
import socket
import sys
import threading
import time
import uuid
import warnings
from abc import ABC, abstractmethod
from collections import deque
from collections.abc import Callable, Iterable, Mapping, Sequence
from contextlib import asynccontextmanager
from queue import Queue
from typing import TYPE_CHECKING, Literal, Optional, Union

import uvicorn
import uvicorn.server
from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.security import APIKeyHeader, OAuth2PasswordBearer
from starlette.formparsers import MultiPartParser
from starlette.middleware.gzip import GZipMiddleware

from litserve import LitAPI
from litserve.callbacks.base import Callback, CallbackRunner, EventTypes
from litserve.connector import _Connector
from litserve.loggers import Logger, _LoggerConnector
from litserve.loops import LitLoop, inference_worker
from litserve.middlewares import MaxSizeMiddleware, RequestCountMiddleware
from litserve.python_client import client_template
from litserve.specs.base import LitSpec
from litserve.transport.base import MessageTransport
from litserve.transport.factory import TransportConfig, create_transport_from_config
from litserve.utils import (
    LitAPIStatus,
    LoopResponseType,
    ResponseBufferItem,
    WorkerSetupStatus,
    add_ssl_context_from_env,
    call_after_stream,
    configure_logging,
    is_package_installed,
)

_MCP_AVAILABLE = is_package_installed("mcp")

if TYPE_CHECKING:
    from litserve.mcp import ToolEndpointType

mp.allow_connection_pickling()

logger = logging.getLogger(__name__)

# if defined, it will require clients to auth with X-API-Key in the header
LIT_SERVER_API_KEY = os.environ.get("LIT_SERVER_API_KEY")
SHUTDOWN_API_KEY = os.environ.get("LIT_SHUTDOWN_API_KEY")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# FastAPI writes form files to disk over 1MB by default, which prevents serialization by multiprocessing
MultiPartParser.max_file_size = sys.maxsize
# renamed in PR: https://github.com/encode/starlette/pull/2780
MultiPartParser.spool_max_size = sys.maxsize


def no_auth():
    pass


def api_key_auth(x_api_key: str = Depends(APIKeyHeader(name="X-API-Key"))):
    if x_api_key != LIT_SERVER_API_KEY:
        raise HTTPException(
            status_code=401, detail="Invalid API Key. Check that you are passing a correct 'X-API-Key' in your header."
        )


async def _mixed_response_to_buffer(
    transport: MessageTransport,
    response_buffer: dict[str, ResponseBufferItem],
    consumer_id: int = 0,
):
    """Handle both regular and streaming responses.

    Detect streaming responses by checking if the response is for streaming.

    """
    while True:
        try:
            result = await transport.areceive(consumer_id)
            if result is None:
                continue

            uid, (*response, response_type, worker_id) = result

            response_item = response_buffer.get(uid)
            if response_item is None:
                continue

            if response[1] == LitAPIStatus.START:
                response_item.worker_id = int(worker_id)
                continue

            if response_type == LoopResponseType.STREAMING:
                response_item.response_queue.append(response)
                response_item.event.set()
            else:
                response_item.response = response
                response_item.event.set()
        except asyncio.CancelledError:
            logger.debug("Response queue to buffer task was cancelled")
            break
        except Exception as e:
            logger.error(f"Error in response_queue_to_buffer: {e}")
            break


async def response_queue_to_buffer(
    transport: MessageTransport,
    response_buffer: dict[str, ResponseBufferItem],
    consumer_id: int,
    litapi_connector: "_LitAPIConnector",
):
    mixed_streaming = (
        len(litapi_connector.lit_apis) > 1
        and litapi_connector.any_stream()
        and not all(api.stream for api in litapi_connector)
    )
    if mixed_streaming:
        return await _mixed_response_to_buffer(transport, response_buffer, consumer_id)

    stream = litapi_connector.any_stream()
    if stream:
        while True:
            try:
                result = await transport.areceive(consumer_id)
                if result is None:
                    continue

                uid, (*response, response_type, worker_id) = result

                response_item = response_buffer.get(uid)
                if response_item is None:
                    continue

                if response[1] == LitAPIStatus.START:
                    response_item.worker_id = int(worker_id)
                    continue

                response_item.response_queue.append(response)
                response_item.event.set()
            except asyncio.CancelledError:
                logger.debug("Response queue to buffer task was cancelled")
                break
            except Exception as e:
                logger.error(f"Error in response_queue_to_buffer: {e}")
                break

    else:
        while True:
            try:
                result = await transport.areceive(consumer_id)
                if result is None:
                    continue

                uid, (*response, response_type, worker_id) = result

                response_item = response_buffer.get(uid)
                if response_item is None:
                    continue

                if response[1] == LitAPIStatus.START:
                    response_item.worker_id = int(worker_id)
                    continue

                response_item.response = response
                response_item.event.set()
            except asyncio.CancelledError:
                logger.debug("Response queue to buffer task was cancelled")
                break
            except Exception as e:
                logger.error(f"Error in response_queue_to_buffer: {e}")
                break


def _migration_warning(feature_name):
    warnings.warn(
        f"The {feature_name} parameter is being deprecated in `LitServer` "
        "and will be removed in version v0.3.0.\n\n"
        "Please update your code to pass these arguments to `LitAPI` instead.\n\n"
        "Old usage:\n"
        f"    server = LitServer(api, {feature_name}=...)\n\n"
        "New usage:\n"
        f"    api = LitAPI({feature_name}=...)\n"
        "    server = LitServer(api, ...)",
        DeprecationWarning,
        stacklevel=3,
    )


class _LitAPIConnector:
    """A helper class to manage one or more `LitAPI` instances.

    This class provides utilities for performing setup tasks, managing request
    and batch timeouts, and interacting with `LitAPI` instances in a unified way.
    It ensures that all `LitAPI` instances are properly initialized and configured
    before use.

    Attributes:
        lit_apis (list[LitAPI]): A list of `LitAPI` instances managed by this connector.

    Methods:
        pre_setup(): Calls the `pre_setup` method on all managed `LitAPI` instances.
        set_request_timeout(timeout): Sets the request timeout for all `LitAPI` instances
            and validates that batch timeouts are within acceptable limits.
        __iter__(): Allows iteration over the managed `LitAPI` instances.
        any_stream(): Checks if any of the `LitAPI` instances have streaming enabled.
        set_logger_queue(queue): Sets a logger queue for all `LitAPI` instances.

    """

    def __init__(self, lit_apis: Union[LitAPI, Iterable[LitAPI]]):
        if isinstance(lit_apis, LitAPI):
            self.lit_apis = [lit_apis]
        elif isinstance(lit_apis, Iterable):
            self.lit_apis = list(lit_apis)
            if not self.lit_apis:  # Check if the iterable is empty
                raise ValueError("lit_apis must not be an empty iterable")
            self._detect_path_collision()
        else:
            raise ValueError(f"lit_apis must be a LitAPI or an iterable of LitAPI, but got {type(lit_apis)}")

    def _detect_path_collision(self):
        paths = {"/health": "LitServe healthcheck", "/info": "LitServe info"}
        for lit_api in self.lit_apis:
            if lit_api.api_path in paths:
                raise ValueError(f"api_path {lit_api.api_path} is already in use by {paths[lit_api.api_path]}")
            paths[lit_api.api_path] = lit_api

    def pre_setup(self):
        for lit_api in self.lit_apis:
            lit_api.pre_setup()
            # Ideally LitAPI should not know about LitLoop
            # LitLoop can keep litapi as a class variable
            lit_api.loop.pre_setup(lit_api)

    def set_request_timeout(self, timeout: float):
        for lit_api in self.lit_apis:
            lit_api.request_timeout = timeout

        for lit_api in self.lit_apis:
            if lit_api.batch_timeout > timeout and timeout not in (False, -1):
                raise ValueError("batch_timeout must be less than request_timeout")

    def __iter__(self):
        return iter(self.lit_apis)

    def any_stream(self):
        return any(lit_api.stream for lit_api in self.lit_apis)

    def set_logger_queue(self, queue: Queue):
        for lit_api in self.lit_apis:
            lit_api.set_logger_queue(queue)

    def get_mcp_tools(self) -> list["ToolEndpointType"]:
        mcp_tools = []
        for lit_api in self.lit_apis:
            if lit_api.mcp:
                mcp_tools.append(lit_api.mcp.as_tool())
        return mcp_tools


class BaseRequestHandler(ABC):
    def __init__(self, lit_api: LitAPI, server: "LitServer"):
        self.lit_api = lit_api
        self.server = server

    async def _prepare_request(self, request, request_type) -> dict:
        """Common request preparation logic."""
        if request_type == Request:
            content_type = request.headers.get("Content-Type", "")
            if content_type == "application/x-www-form-urlencoded" or content_type.startswith("multipart/form-data"):
                return await request.form()
            return await request.json()
        return request

    async def _submit_request(self, payload: dict) -> tuple[str, asyncio.Event]:
        """Submit request to worker queue."""
        request_queue = self.server._get_request_queue(self.lit_api.api_path)
        response_queue_id = self.server.app.response_queue_id
        uid = str(uuid.uuid4())

        # Trigger callback
        self.server._callback_runner.trigger_event(
            EventTypes.ON_REQUEST.value,
            active_requests=self.server.active_requests,
            litserver=self.server,
        )

        request_queue.put((response_queue_id, uid, time.monotonic(), payload))
        logger.debug(f"Submitted request uid={uid}")
        return uid, response_queue_id

    @abstractmethod
    async def handle_request(self, request, request_type) -> Response:
        pass


class RegularRequestHandler(BaseRequestHandler):
    async def handle_request(self, request, request_type) -> Response:
        try:
            logger.debug(f"Handling request: {request}")
            # Prepare request
            payload = await self._prepare_request(request, request_type)

            # Submit to worker
            uid, _ = await self._submit_request(payload)

            # Wait for response
            event = asyncio.Event()
            self.server.response_buffer[uid] = ResponseBufferItem(event)

            await event.wait()

            # Process response
            response_buffer_item = self.server.response_buffer.pop(uid)
            response, status = response_buffer_item.response

            if status == LitAPIStatus.ERROR:
                self._handle_error_response(response)

            # Trigger callback
            self.server._callback_runner.trigger_event(EventTypes.ON_RESPONSE.value, litserver=self.server)

            return response

        except HTTPException as e:
            raise e from None

        except Exception as e:
            logger.error(f"Unhandled exception: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail="Internal server error") from e

    @staticmethod
    def _handle_error_response(response):
        """Raise HTTPException as is and rest as 500 after logging the error."""
        try:
            if isinstance(response, bytes):
                response = pickle.loads(response)
                raise HTTPException(status_code=response.status_code, detail=response.detail)
        except Exception as e:
            logger.debug(f"couldn't unpickle error response {e}")

        if isinstance(response, HTTPException):
            raise response

        if isinstance(response, Exception):
            logger.error(f"Error while handling request: {response}")

        raise HTTPException(status_code=500, detail="Internal server error")


class StreamingRequestHandler(BaseRequestHandler):
    async def handle_request(self, request, request_type) -> StreamingResponse:
        try:
            # Prepare request
            payload = await self._prepare_request(request, request_type)

            # Submit to worker
            uid, _ = await self._submit_request(payload)

            # Set up streaming response
            event = asyncio.Event()
            response_queue = deque()
            self.server.response_buffer[uid] = ResponseBufferItem(event=event, response_queue=response_queue)

            # Create streaming response
            response_generator = call_after_stream(
                self.server.data_streamer(response_queue, data_available=event),
                self.server._callback_runner.trigger_event,
                EventTypes.ON_RESPONSE.value,
                litserver=self.server,
            )

            async def stream_with_cleanup():
                try:
                    async for item in response_generator:
                        yield item
                finally:
                    self.server.response_buffer.pop(uid, None)

            return StreamingResponse(stream_with_cleanup())

        except Exception as e:
            logger.exception(f"Error handling streaming request: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")


class _Server(uvicorn.server.Server):
    def run(self, worker_id: int, sockets: Union[list[socket.socket], None] = None) -> None:
        os.environ["LITSERVE_WORKER_ID"] = str(worker_id)
        return super().run(sockets)


class LitServer:
    """Initialize a LitServer for high-performance AI model serving.

    LitServer transforms AI models into production-ready APIs with automatic scaling,
    batching, streaming, and multi-GPU support.

    Quick Start:
        ```python
        import litserve as ls

        # Define inference pipeline
        class MyAPI(ls.LitAPI):
            def setup(self, device):
                self.model = load_model()  # model loading logic

            def predict(self, x):
                return self.model(x)

        # Create and run server
        server = ls.LitServer(MyAPI())
        server.run(port=8000)
        ```

    Args:
        lit_api:
            The core component - one or more LitAPI instances defining model logic.

            - Single API: `MyAPI()` for serving one model
            - Multiple APIs: `[API1(), API2()]` for multi-model serving

            Each LitAPI must implement:
            - `setup(device)`: Initialize the model
            - `predict(x)`: Run inference
            - Optional: `decode_request()`, `encode_response()` for custom I/O

    Hardware Configuration:
        accelerator:
            Hardware type for inference. Defaults to "auto".

            - "auto": Automatically detects best available (CUDA > MPS > CPU)
            - "cpu": Force CPU usage
            - "cuda": Use NVIDIA GPUs
            - "mps": Use Apple Metal Performance Shaders

        devices:
            Number of devices to use. Defaults to "auto".

            - "auto": Use all available devices
            - int: Use specific number (e.g., 2 for 2 GPUs)

        workers_per_device:
            Worker processes per device for parallel inference. Defaults to 1.

            - Higher values = better throughput but more memory usage
            - Good starting point: 1-4 depending on model size
            - For CPU, set to the number of cores available on the machine (e.g., 8 for 8-core CPU)
            - Monitor GPU memory when increasing

    Performance & Scaling:
        timeout:
            Request timeout in seconds. Defaults to 30.

            - Set to False or -1 to disable timeouts
            - Increase for slow models (e.g., 300 for large LLMs)
            - Decrease for fast models (e.g., 5 for lightweight models)

        fast_queue:
            Enable ZeroMQ for high-throughput scenarios (>100 RPS). Defaults to False.

            - Use when serving hundreds of requests per second
            - Not supported on Windows

        track_requests:
            Track active requests across all API servers for monitoring and load management. Defaults to False.

            When enabled, tracks the total number of active requests in the queue across all API servers
            and makes this count available via callbacks using the `on_request` hook. Essential for
            monitoring concurrent request load and implementing custom load management logic.

            - Recommended for production deployments
            - Access count via callbacks or `server.active_requests` property
            - Useful for monitoring and handling concurrent requests effectively

    API Configuration:
        healthcheck_path:
            Health check endpoint for load balancers. Defaults to "/health".

            - Returns 200 when all workers are ready
            - Critical for Kubernetes/Docker deployments

        info_path:
            Server information endpoint. Defaults to "/info".

            - Shows model metadata, device info, server config
            - Useful for debugging and monitoring

        disable_openapi_url:
            If True, disables the OpenAPI schema endpoint ("/openapi.json").

            - Useful for production environments where exposing API schemas is not desired.
            - Defaults to False (the OpenAPI schema is enabled).

        shutdown_path:
            Graceful shutdown endpoint. Defaults to "/shutdown".

        enable_shutdown_api:
            Enable remote shutdown capability. Defaults to False.

            - Requires authentication token (set LIT_SHUTDOWN_API_KEY env var)
            - Useful for automated deployment pipelines

        restart_workers:
            Enable this option to automatically restart
            workers if a critical error occurs. Defaults to False.

            - When enabled, the worker loop will exit using `os._exit(1)`,
            allowing the main process to recreate the worker.


    Content & Middleware:
        max_payload_size:
            Maximum request size. Defaults to "100MB".

            - String format: "10MB", "1GB"
            - Integer format: bytes (1048576 for 1MB)
            - Increase for large images/videos

        middlewares:
            HTTP middleware for cross-cutting concerns. Defaults to None.

            Example:
            ```python
            from starlette.middleware.cors import CORSMiddleware

            server = LitServer(
                api,
                middlewares=[
                    (CORSMiddleware, {"allow_origins": ["*"]}),
                    # Add more middleware as needed
                ]
            )
            ```

        model_metadata:
            Metadata about the model displayed at info endpoint. Defaults to None.

            Example:
            ```python
            metadata = {
                "model_name": "bert-base-uncased",
                "version": "1.0.0",
                "description": "Text classification model"
            }
            ```

    Monitoring & Debugging:
        callbacks:
            Event handlers for server lifecycle. Defaults to None.

            - Built-in callbacks for logging, metrics, custom logic
            - Triggers on request start/end, server start/stop

        loggers:
            Custom loggers for metrics and events. Defaults to None.

            - Integrate with monitoring stack
            - Track performance metrics, error rates

    Advanced Configuration:
        max_batch_size, batch_timeout, spec, stream, api_path, loop:
            **Deprecated**: Configure these in LitAPI implementation instead.

            Migration example:
            ```python
            # Old way (deprecated)
            server = LitServer(api, max_batch_size=8, stream=True)

            # New way (recommended)
            api = MyAPI(max_batch_size=8, stream=True)
            server = LitServer(api)
            ```

    Examples:
        Basic Usage:
        ```python
        import litserve as ls

        class SimpleAPI(ls.LitAPI):
            def setup(self, device):
                self.model = lambda x: x * 2  # model here

            def predict(self, x):
                return self.model(x)

        server = ls.LitServer(SimpleAPI())
        server.run()
        ```

        Production Setup:
        ```python
        server = ls.LitServer(
            MyAPI(max_batch_size=8),
            accelerator="cuda",
            devices=2,
            workers_per_device=4,
            fast_queue=True,
            track_requests=True,
            max_payload_size="50MB",
            timeout=60
        )
        server.run(port=8000, num_api_servers=4)
        ```

        Multi-Model Serving:
        ```python
        # Serve multiple models on different endpoints
        text_api = TextClassifierAPI(api_path="/classify")
        image_api = ImageClassifierAPI(api_path="/vision")

        server = ls.LitServer([text_api, image_api])
        server.run()
        ```

        Streaming Response:
        ```python
        class StreamingAPI(ls.LitAPI):
            def setup(self, device):
                self.model = load_llm()

            def predict(self, prompt):
                for token in self.model.generate(prompt):
                    yield {"token": token}

        server = ls.LitServer(StreamingAPI(stream=True))
        ```

        Per-route using dict
        ```python
        server = ls.LitServer(
            [sentiment_api, generate_api],
            accelerator="cuda",
            devices=[0, 1],
            workers_per_device={
                "/sentiment": 2,  # 2 workers per GPU for sentiment
                "/generate": 3,   # 3 workers per GPU for generation
            },
        )
        ```

        Per-api position
        ```python
        server = ls.LitServer(
            [sentiment_api, generate_api],
            accelerator="cuda",
            devices=[0, 1],
            workers_per_device=[2, 3],  # sentiment then generate (same order as API list)
        )
        ```

    Deployment:
        Self-hosted:
        ```bash
        python server.py  # Run locally
        ```

        Lightning AI Cloud:
        ```bash
        lightning deploy server.py --cloud  # One-click deploy
        ```

    See Also:
        - LitAPI: Base class for defining model logic
        - LitSpec: API specifications (OpenAI compatibility)
        - Documentation: https://lightning.ai/docs/litserve

    """

    def __init__(
        self,
        lit_api: Union[LitAPI, list[LitAPI]],
        accelerator: Literal["cpu", "cuda", "mps", "auto"] = "auto",
        devices: Union[int, Literal["auto"]] = "auto",
        workers_per_device: int = 1,
        timeout: Union[float, bool] = 30,
        healthcheck_path: str = "/health",
        info_path: str = "/info",
        shutdown_path: str = "/shutdown",
        enable_shutdown_api: bool = False,
        model_metadata: Optional[dict] = None,
        spec: Optional[LitSpec] = None,
        max_payload_size=None,
        track_requests: bool = False,
        callbacks: Optional[Union[list[Callback], Callback]] = None,
        middlewares: Optional[list[Union[Callable, tuple[Callable, dict]]]] = None,
        loggers: Optional[Union[Logger, list[Logger]]] = None,
        fast_queue: bool = False,
        disable_openapi_url: bool = False,
        # All the following arguments are deprecated and will be removed in v0.3.0
        max_batch_size: Optional[int] = None,
        batch_timeout: float = 0.0,
        stream: bool = False,
        api_path: Optional[str] = None,
        loop: Optional[Union[str, LitLoop]] = None,
        restart_workers: bool = False,
    ):
        if max_batch_size is not None:
            warnings.warn(
                "'max_batch_size' and 'batch_timeout' are being deprecated in `LitServer` "
                "and will be removed in version v0.3.0.\n\n"
                "Please update your code to pass these arguments to `LitAPI` instead.\n\n"
                "Old usage:\n"
                "    server = LitServer(api, max_batch_size=N, batch_timeout=T, ...)\n\n"
                "New usage:\n"
                "    api = LitAPI(max_batch_size=N, batch_timeout=T, ...)\n"
                "    server = LitServer(api, ...)",
                DeprecationWarning,
                stacklevel=2,
            )
            lit_api.max_batch_size = max_batch_size
            lit_api.batch_timeout = batch_timeout

        if middlewares is None:
            middlewares = []
        if not isinstance(middlewares, list):
            _msg = (
                "middlewares must be a list of tuples"
                " where each tuple contains a middleware and its arguments. For example:\n"
                "server = ls.LitServer(ls.test_examples.SimpleLitAPI(), "
                'middlewares=[(RequestIdMiddleware, {"length": 5})])'
            )
            raise ValueError(_msg)

        # Handle 0.3.0 migration
        if api_path is not None:
            _migration_warning("api_path")
            lit_api.api_path = api_path
        if stream is True:
            _migration_warning("stream")
            lit_api.stream = stream
        if isinstance(loop, LitLoop):
            _migration_warning("loop")
            lit_api.loop = loop
        if isinstance(spec, LitSpec):
            _migration_warning("spec")
            lit_api.spec = spec
            lit_api.stream = spec.stream

        # pre setup
        self.litapi_connector = _LitAPIConnector(lit_api)
        self.litapi_connector.pre_setup()

        if api_path and not api_path.startswith("/"):
            raise ValueError(
                "api_path must start with '/'. "
                "Please provide a valid api path like '/predict', '/classify', or '/v1/predict'"
            )

        if not healthcheck_path.startswith("/"):
            raise ValueError(
                "healthcheck_path must start with '/'. "
                "Please provide a valid api path like '/health', '/healthcheck', or '/v1/health'"
            )

        if not info_path.startswith("/"):
            raise ValueError(
                "info_path must start with '/'. Please provide a valid api path like '/info', '/details', or '/v1/info'"
            )

        if enable_shutdown_api and not shutdown_path.startswith("/"):
            raise ValueError("shutdown_path must start with '/'. Please provide a valid api path like '/shutdown'")

        global SHUTDOWN_API_KEY
        if enable_shutdown_api and not SHUTDOWN_API_KEY:
            SHUTDOWN_API_KEY = secrets.token_urlsafe(32)
            logger.warning(
                "LitServe's Shutdown API is enabled, but the `LIT_SHUTDOWN_API_KEY` environment variable is missing."
                f"Generated shutdown API key: {SHUTDOWN_API_KEY}"
            )
        if enable_shutdown_api:
            curl_command = (
                "curl -X 'POST' 'http://localhost:8000/shutdown' "
                "-H 'accept: application/json' "
                f"-H 'Authorization: Bearer {SHUTDOWN_API_KEY}' "
                "-d ''"
            )
            logger.info(f"To shutdown the server, run command: \n{curl_command}\n")
        try:
            json.dumps(model_metadata)
        except (TypeError, ValueError):
            raise ValueError("model_metadata must be JSON serializable.")

        if sys.platform == "win32" and fast_queue:
            warnings.warn("ZMQ is not supported on Windows with LitServe. Disabling ZMQ.")
            fast_queue = False

        self.healthcheck_path = healthcheck_path
        self.info_path = info_path
        self._shutdown_path = shutdown_path
        self.track_requests = track_requests
        self.timeout = timeout
        self.litapi_connector.set_request_timeout(timeout)
        self.app = FastAPI(lifespan=self.lifespan, openapi_url="" if disable_openapi_url else "/openapi.json")
        self._disable_openapi_url = disable_openapi_url

        self.app.response_queue_id = None
        self.response_buffer: dict[str, ResponseBufferItem] = {}
        # gzip does not play nicely with streaming, see https://github.com/tiangolo/fastapi/discussions/8448
        if not self.litapi_connector.any_stream():
            middlewares.append((GZipMiddleware, {"minimum_size": 1000}))
        if max_payload_size is not None:
            middlewares.append((MaxSizeMiddleware, {"max_size": max_payload_size}))
        self.active_counters: list[mp.Value] = []
        self.middlewares = middlewares
        self._logger_connector = _LoggerConnector(self, loggers)
        self.logger_queue = None
        self.lit_api = lit_api
        self.enable_shutdown_api = enable_shutdown_api
        self.workers_per_device = workers_per_device
        self._workers_per_device_by_api_path = self._resolve_workers_per_device_config(workers_per_device)
        self.max_payload_size = max_payload_size
        self.model_metadata = model_metadata
        self._connector = _Connector(accelerator=accelerator, devices=devices)
        self._callback_runner = CallbackRunner(callbacks)
        self.use_zmq = fast_queue
        self.transport_config = None
        self.litapi_request_queues = {}
        self._shutdown_event: Optional[mp.Event] = None
        self.uvicorn_graceful_timeout = 30
        self.restart_workers = restart_workers or False
        self.monitor_internal = 2
        self.mcp_server = None

        self._monitor_workers = True

        accelerator = self._connector.accelerator
        devices = self._connector.devices
        if accelerator == "cpu":
            self.devices = [accelerator]
        elif accelerator in ["cuda", "mps"]:
            device_list = devices
            if isinstance(devices, int):
                device_list = range(devices)
            self.devices = [self.device_identifiers(accelerator, device) for device in device_list]

        self.transport_config = TransportConfig(transport_config="zmq" if self.use_zmq else "mp")
        self.register_endpoints()
        # register middleware
        self._register_middleware()

    def _inference_workers_config_for_api(self, api_path: str):
        wpd = self._workers_per_device_by_api_path[api_path]
        return self.devices * wpd

    def launch_inference_worker(self, lit_api: LitAPI):
        specs = [lit_api.spec] if lit_api.spec else []
        for spec in specs:
            # Objects of Server class are referenced (not copied)
            logging.debug(f"shallow copy for Server is created for for spec {spec}")
            server_copy = copy.copy(self)
            del server_copy.app, server_copy.transport_config, server_copy.litapi_connector
            spec.setup(server_copy)

        process_list = []
        endpoint = lit_api.api_path.split("/")[-1]

        inference_workers_config = self._inference_workers_config_for_api(lit_api.api_path)

        for worker_id, device in enumerate(inference_workers_config):
            if len(device) == 1:
                device = device[0]

            self.workers_setup_status[f"{endpoint}_{worker_id}"] = WorkerSetupStatus.STARTING

            ctx = mp.get_context("spawn")
            process = ctx.Process(
                target=inference_worker,
                args=(
                    lit_api,
                    device,
                    worker_id,
                    self._get_request_queue(lit_api.api_path),
                    self._transport,
                    self.workers_setup_status,
                    self._callback_runner,
                    self.restart_workers,
                ),
                name="inference-worker",
            )
            process.start()
            process_list.append(process)
        return process_list

    def launch_single_inference_worker(self, lit_api: LitAPI, worker_id: int):
        specs = [lit_api.spec] if lit_api.spec else []
        for spec in specs:
            # Objects of Server class are referenced (not copied)
            logging.debug(f"shallow copy for Server is created for for spec {spec}")
            server_copy = copy.copy(self)
            del server_copy.app, server_copy.transport_config, server_copy.litapi_connector
            spec.setup(server_copy)

        inference_workers_config = self._inference_workers_config_for_api(lit_api.api_path)
        device = inference_workers_config[worker_id]
        endpoint = lit_api.api_path.split("/")[-1]
        if len(device) == 1:
            device = device[0]

        self.workers_setup_status[f"{endpoint}_{worker_id}"] = WorkerSetupStatus.STARTING

        ctx = mp.get_context("spawn")
        process = ctx.Process(
            target=inference_worker,
            args=(
                lit_api,
                device,
                worker_id,
                self._get_request_queue(lit_api.api_path),
                self._transport,
                self.workers_setup_status,
                self._callback_runner,
                self.restart_workers,
            ),
            name="inference-worker",
        )

        process.start()
        return process

    @asynccontextmanager
    async def lifespan(self, app: FastAPI):
        loop = asyncio.get_running_loop()

        if not hasattr(self, "_transport") or not self._transport:
            raise RuntimeError(
                "Response queues have not been initialized. "
                "Please make sure to call the 'launch_inference_workers' method of "
                "the LitServer class to initialize the response queues."
            )

        transport = self._transport
        future = response_queue_to_buffer(
            transport,
            self.response_buffer,
            app.response_queue_id,
            self.litapi_connector,
        )
        task = loop.create_task(future, name=f"response_queue_to_buffer-{app.response_queue_id}")
        task.add_done_callback(
            lambda _: logger.debug(f"Response queue to buffer task terminated for consumer_id {app.response_queue_id}")
        )

        try:
            if _MCP_AVAILABLE:
                async with self.mcp_server.lifespan(app):
                    yield
            else:
                yield
        finally:
            self._callback_runner.trigger_event(EventTypes.ON_SERVER_END.value, litserver=self)

            # Cancel the task
            task.cancel()

            with contextlib.suppress(asyncio.CancelledError, asyncio.TimeoutError, Exception):
                await asyncio.wait_for(task, timeout=1.0)

    def device_identifiers(self, accelerator, device):
        if isinstance(device, Sequence):
            return [f"{accelerator}:{el}" for el in device]
        return [f"{accelerator}:{device}"]

    @staticmethod
    async def data_streamer(q: deque, data_available: asyncio.Event, send_status: bool = False):
        while True:
            await data_available.wait()
            while len(q) > 0:
                data, status = q.popleft()
                if status == LitAPIStatus.FINISH_STREAMING:
                    return

                if status == LitAPIStatus.ERROR:
                    logger.error(
                        "Error occurred while streaming outputs from the inference worker. "
                        "Please check the above traceback."
                    )
                    if send_status:
                        yield data, status
                    return
                if send_status:
                    yield data, status
                else:
                    yield data
            data_available.clear()

    @property
    def active_requests(self):
        if self.track_requests and self.active_counters:
            return sum(counter.value for counter in self.active_counters)
        return None

    def _register_internal_endpoints(self):
        workers_ready = False

        @self.app.get("/", dependencies=[Depends(self.setup_auth())])
        async def index(request: Request) -> Response:
            return Response(content="litserve running")

        @self.app.get(self.healthcheck_path, dependencies=[Depends(self.setup_auth())])
        async def health(request: Request) -> Response:
            nonlocal workers_ready
            if not workers_ready:
                workers_ready = bool(self.workers_setup_status) and all(
                    v == WorkerSetupStatus.READY for v in self.workers_setup_status.values()
                )

            lit_api_health_status = True
            for lit_api in self.litapi_connector:
                result = lit_api.health()
                if inspect.isawaitable(result):
                    result = await result
                if not result:
                    lit_api_health_status = False
                    break
            if workers_ready and lit_api_health_status:
                return Response(content="ok", status_code=200)

            return Response(content="not ready", status_code=503)

        @self.app.get(self.info_path, dependencies=[Depends(self.setup_auth())])
        async def info(request: Request) -> Response:
            return JSONResponse(
                content={
                    "model": self.model_metadata,
                    "server": {
                        "devices": self.devices,
                        "workers_per_device": self.workers_per_device,
                        "timeout": self.timeout,
                        "stream": {lit_api.api_path: lit_api.stream for lit_api in self.litapi_connector},
                        "max_payload_size": self.max_payload_size,
                        "track_requests": self.track_requests,
                    },
                }
            )

        if self.enable_shutdown_api:

            @self.app.post(self._shutdown_path, dependencies=[Depends(self.shutdown_api_key_auth)])
            async def shutdown_endpoint():
                if not self._shutdown_event:
                    raise HTTPException(
                        status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Server is still starting up"
                    )
                self._shutdown_event.set()
                return Response(content="Server is initiating graceful shutdown.", status_code=status.HTTP_200_OK)

    def register_endpoints(self):
        self._register_internal_endpoints()

        for lit_api in self.litapi_connector:
            decode_request_signature = inspect.signature(lit_api.decode_request)
            encode_response_signature = inspect.signature(lit_api.encode_response)

            request_type = decode_request_signature.parameters["request"].annotation
            if request_type == decode_request_signature.empty:
                request_type = Request

            response_type = encode_response_signature.return_annotation
            if response_type == encode_response_signature.empty:
                response_type = Response
            self._register_api_endpoints(lit_api, request_type, response_type)

    def _get_request_queue(self, api_path: str):
        return self.litapi_request_queues[api_path]

    def _register_api_endpoints(self, lit_api: LitAPI, request_type, response_type):
        """Register endpoint routes for the FastAPI app."""

        self._callback_runner.trigger_event(EventTypes.ON_SERVER_START.value, litserver=self)

        # Create handlers
        handler = StreamingRequestHandler(lit_api, self) if lit_api.stream else RegularRequestHandler(lit_api, self)

        # Create endpoint function
        async def endpoint_handler(request: request_type) -> response_type:
            return await handler.handle_request(request, request_type)

        # Register endpoint
        if not lit_api.spec:
            self.app.add_api_route(
                lit_api.api_path,
                endpoint_handler,
                methods=["POST"],
                dependencies=[Depends(self.setup_auth())],
            )

        # Handle specs
        self._register_spec_endpoints(lit_api)

    def _register_spec_endpoints(self, lit_api: LitAPI):
        specs = [lit_api.spec] if lit_api.spec else []
        for spec in specs:
            spec: LitSpec
            # Set the server reference for callback triggering in spec endpoints
            spec._server = self
            # TODO check that path is not clashing
            for path, endpoint, methods in spec.endpoints:
                self.app.add_api_route(
                    path, endpoint=endpoint, methods=methods, dependencies=[Depends(self.setup_auth())]
                )

    def _register_middleware(self):
        for middleware in self.middlewares:
            if isinstance(middleware, tuple):
                middleware, kwargs = middleware
                self.app.add_middleware(middleware, **kwargs)
            elif callable(middleware):
                self.app.add_middleware(middleware)

    @staticmethod
    def generate_client_file(port: Union[str, int] = 8000):
        dest_path = os.path.join(os.getcwd(), "client.py")

        if os.path.exists(dest_path):
            logger.debug("client.py already exists in the current directory. Skipping generation.")
            return

        try:
            client_code = client_template.format(PORT=port)
            with open(dest_path, "w") as f:
                f.write(client_code)

        except Exception as e:
            logger.exception(f"Error copying file: {e}")

    def verify_worker_status(self):
        while not any(v == WorkerSetupStatus.READY for v in self.workers_setup_status.values()):
            if any(v == WorkerSetupStatus.ERROR for v in self.workers_setup_status.values()):
                raise RuntimeError("One or more workers failed to start. Shutting down LitServe")
            time.sleep(0.05)
        logger.debug("One or more workers are ready to serve requests")

    def _init_manager(self, num_api_servers: int):
        manager = mp.Manager()
        self.transport_config.manager = manager
        self.transport_config.num_consumers = num_api_servers
        self.workers_setup_status = manager.dict()
        self._shutdown_event = manager.Event()

        # create request queues for each unique lit_api api_path
        for lit_api in self.litapi_connector:
            self.litapi_request_queues[lit_api.api_path] = manager.Queue()

        if self._logger_connector._loggers:
            self.logger_queue = manager.Queue()
        self._logger_connector.run(self)
        self._transport = create_transport_from_config(self.transport_config)
        return manager

    def _perform_graceful_shutdown(
        self,
        manager: mp.Manager,
        uvicorn_workers: dict[str, Union[mp.Process, threading.Thread]],
        shutdown_reason: str = "normal",
    ):
        """Encapsulates the graceful shutdown logic."""
        logger.info("Shutting down LitServe...")

        # Handle transport closure based on shutdown reason
        if shutdown_reason == "keyboard_interrupt":
            logger.debug("KeyboardInterrupt detected - skipping transport cleanup to avoid hanging")
            self._transport.close(send_sentinel=False)
        else:
            self._transport.close(send_sentinel=True)

        # terminate Uvicorn server workers tracked by LitServe (the master processes/threads)
        if len(uvicorn_workers) > 0:
            for i, uw in uvicorn_workers.items():
                uvicorn_pid = uw.ident if isinstance(uw, threading.Thread) else uw.pid
                uvicorn_name = uw.name

                log_prefix = f"{uvicorn_name} (PID: {uvicorn_pid})"

                if not uw.is_alive():
                    logger.warning(f"{log_prefix}: Already not alive.")
                    continue
                try:
                    uw.terminate()
                    uw.join(timeout=self.uvicorn_graceful_timeout)
                    if uw.is_alive():
                        logger.warning(f"{log_prefix}: Did not terminate gracefully. Forcibly killing.")
                        uw.kill()
                except Exception as e:
                    logger.error(f"Error during termination of {log_prefix}: {e}")

        # terminate and join inference worker processes
        logger.debug(f"Terminating {len(self.inference_workers)} inference workers...")
        for i, iw in enumerate(self.inference_workers):
            worker_pid = iw.pid
            worker_name = iw.name
            try:
                iw.terminate()
                iw.join(timeout=5)
                if iw.is_alive():
                    logger.warning(
                        f"Worker {worker_name} (PID: {worker_pid}): Did not terminate gracefully. Killing (SIGKILL)."
                    )
                    iw.kill()
                else:
                    logger.debug(f"Worker {worker_name} (PID: {worker_pid}): Terminated gracefully.")
            except Exception as e:
                logger.error(f"Error while terminating worker {worker_name} (PID: {worker_pid}): {e}")

        manager.shutdown()

    def _resolve_workers_per_device_config(self, workers_per_device):
        """Resolve workers_per_device into a dict[api_path, workers_per_device_int]."""
        api_paths = [api.api_path for api in self.litapi_connector]

        if isinstance(workers_per_device, int):
            if workers_per_device < 1:
                raise ValueError("workers_per_device must be >= 1")
            return dict.fromkeys(api_paths, workers_per_device)

        if isinstance(workers_per_device, (list, tuple)):
            if len(workers_per_device) != len(api_paths):
                raise ValueError(
                    f"workers_per_device list length must match number of APIs \n"
                    f"({len(api_paths)}), got {len(workers_per_device)}"
                )
            cfg = {}
            for p, w in zip(api_paths, workers_per_device):
                if not isinstance(w, int) or w < 1:
                    raise ValueError("workers_per_device values must be integers >= 1")
                cfg[p] = w
            return cfg

        if isinstance(workers_per_device, Mapping):
            unknown = sorted(set(workers_per_device.keys()) - set(api_paths))
            if unknown:
                raise ValueError(f"workers_per_device contains unknown api_path values: {unknown} (unknown api_path)")
            cfg = {}
            for p in api_paths:
                w = workers_per_device.get(p, 1)
                if not isinstance(w, int) or w < 1:
                    raise ValueError("workers_per_device values must be integers >= 1")
                cfg[p] = w
            return cfg

        raise TypeError("workers_per_device must be an int, a list/tuple of ints, or a mapping of api_path -> int")

    def run(
        self,
        host: str = "0.0.0.0",
        port: Union[str, int] = 8000,
        num_api_servers: Optional[int] = None,
        log_level: str = "info",
        generate_client_file: bool = True,
        api_server_worker_type: Literal["process", "thread"] = "process",
        pretty_logs: bool = False,
        **kwargs,
    ):
        """Start the LitServer to serve AI model requests with production-ready performance.

        This method launches the complete serving infrastructure: initializes worker processes,
        starts the HTTP server, and begins handling requests. The server runs until manually
        stopped (Ctrl+C) or programmatically shut down.

        Quick Start:
            ```python
            # Basic usage - starts server on localhost:8000
            server.run()

            # Production - multiple servers and custom port
            server.run(port=8080, num_api_servers=4)
            ```

        Server Lifecycle:
            1. **Initialize**: Sets up worker processes and communication queues
            2. **Health Check**: Verifies all workers are ready to serve requests
            3. **Start HTTP Server**: Begins accepting requests on specified host/port
            4. **Serve Requests**: Distributes requests to workers and returns responses
            5. **Graceful Shutdown**: Properly terminates workers when stopped

        Args:
            host:
                Network interface to bind the server to. Defaults to "0.0.0.0".

                - "0.0.0.0": Accept connections from any IP (public access)
                - "127.0.0.1": Only accept local connections (localhost only)
                - "::": IPv6 equivalent of "0.0.0.0"

                For development, use "127.0.0.1" for security. For production/Docker, use "0.0.0.0".

            port:
                Port number to listen on. Defaults to 8000.

                - Must be between 1024-65535 (privileged ports require admin)
                - Ensure the port is available and not blocked by firewalls
                - Common choices: 8000, 8080, 3000, 5000

        Performance Configuration:
            num_api_servers:
                Number of parallel HTTP server processes. Defaults to None (auto-detect).

                - None: Uses same count as inference workers (recommended)
                - Higher values improve HTTP throughput but use more memory
                - Good starting point: 2-8 depending on expected load
                - Each server handles HTTP requests independently

            api_server_worker_type:
                Process architecture for HTTP servers. Defaults to "process".

                - "process": Better isolation, CPU utilization, and fault tolerance
                - "thread": Lower memory usage but shared memory space
                - Windows automatically uses "thread" (process forking not supported)

        Development & Debugging:
            log_level:
                Logging verbosity level. Defaults to "info".

                - "critical": Only severe errors
                - "error": Error conditions
                - "warning": Warning messages (good for production)
                - "info": General information (default)
                - "debug": Detailed debugging info (development)
                - "trace": Very verbose output (troubleshooting)

            pretty_logs:
                Enable enhanced log formatting with colors and rich formatting. Defaults to False.

                - Requires: `pip install rich`
                - Great for development and local debugging
                - May not display properly in some production log aggregators

            generate_client_file:
                Auto-generate a Python client file for easy API interaction. Defaults to True.

                - Creates `client.py` in current directory with typed methods
                - Useful for testing and integration
                - Safe to disable in production environments

        Advanced Configuration:
            **kwargs:
                Additional uvicorn server configuration options.

                Common SSL options:
                ```python
                server.run(
                    ssl_keyfile="path/to/key.pem",
                    ssl_certfile="path/to/cert.pem"
                )
                ```

                Other uvicorn options: ssl_ca_certs, ssl_ciphers, ssl_version,
                workers, backlog, etc. See uvicorn documentation for full list.

        Examples:
            Basic Development:
            ```python
            # Simple local development
            server.run()
            # Access at: http://localhost:8000
            # API docs at: http://localhost:8000/docs
            ```

            Production Configuration:
            ```python
            # High-performance production setup
            server.run(
                host="0.0.0.0",
                port=8000,
                num_api_servers=8,
                log_level="warning",
                pretty_logs=False,
                generate_client_file=False
            )
            ```

            Development with Debug:
            ```python
            # Development with detailed logging
            server.run(
                host="127.0.0.1",
                port=8000,
                log_level="debug",
                pretty_logs=True,
                num_api_servers=1
            )
            ```

            Multi-API Server:
            ```python
            # Balance load across multiple HTTP servers
            server.run(
                port=8000,
                num_api_servers=4,  # 4 parallel HTTP servers
                api_server_worker_type="process"
            )
            ```

        Server Endpoints:
            Once running, the server provides several built-in endpoints:

            - **Main API**: `POST /predict` (or custom path from LitAPI)
            - **Health Check**: `GET /health` - Returns 200 when ready
            - **Server Info**: `GET /info` - Shows configuration and metadata
            - **API Documentation**: `GET /docs` - Interactive Swagger UI
            - **OpenAPI Schema**: `GET /openapi.json` - API specification

        Stopping the Server:
            - **Ctrl+C**: Graceful shutdown (recommended)
            - **SIGTERM**: Graceful shutdown in Docker/Kubernetes
            - **Shutdown API**: POST to `/shutdown` (if enabled)

        Common Issues:
            - **Port in use**: Choose different port or stop conflicting process
            - **Permission denied**: Use port > 1024 or run with appropriate permissions
            - **Workers not ready**: Check model loading in LitAPI.setup() method
            - **Memory issues**: Reduce num_api_servers or workers_per_device

        Notes:
            - Server blocks execution until stopped (use threads for non-blocking)
            - Logs show startup progress and any configuration issues
            - Swagger UI provides interactive API testing interface

        """
        if generate_client_file:
            LitServer.generate_client_file(port=port)

        port_msg = f"port must be a value from 1024 to 65535 but got {port}"
        try:
            port = int(port)
        except ValueError:
            raise ValueError(port_msg)

        if not (1024 <= port <= 65535):
            raise ValueError(port_msg)

        host_msg = f"host must be '0.0.0.0', '127.0.0.1', or '::' but got {host}"
        if host not in ["0.0.0.0", "127.0.0.1", "::"]:
            raise ValueError(host_msg)

        kwargs = add_ssl_context_from_env(kwargs)

        configure_logging(log_level, use_rich=pretty_logs)
        config = uvicorn.Config(
            app=self.app,
            host=host,
            port=port,
            log_level=log_level,
            **kwargs,
        )
        sockets = [config.bind_socket()]

        if num_api_servers is None:
            total_workers = 0
            for lit_api in self.litapi_connector:
                total_workers += len(self._inference_workers_config_for_api(lit_api.api_path))
            num_api_servers = total_workers

        if num_api_servers < 1:
            raise ValueError("num_api_servers must be greater than 0")

        if sys.platform == "win32":
            warnings.warn(
                "Windows does not support forking. Using threads api_server_worker_type will be set to 'thread'"
            )
            api_server_worker_type = "thread"
        elif api_server_worker_type is None:
            api_server_worker_type = "process"

        manager = self._init_manager(num_api_servers)
        self._logger_connector.run(self)
        self.inference_workers = []
        for lit_api in self.litapi_connector:
            _inference_workers = self.launch_inference_worker(lit_api)
            self.inference_workers.extend(_inference_workers)

        self.verify_worker_status()

        shutdown_reason = "normal"
        uvicorn_workers = {}
        try:
            uvicorn_workers = self._start_server(
                port, num_api_servers, log_level, sockets, api_server_worker_type, **kwargs
            )

            if not self._disable_openapi_url:
                print(f"Swagger UI is available at http://0.0.0.0:{port}/docs")

            if self._monitor_workers:
                self._start_worker_monitoring(manager, uvicorn_workers)

            self._shutdown_event.wait()

        except KeyboardInterrupt:
            logger.info("KeyboardInterrupt received. Initiating graceful shutdown.")
            shutdown_reason = "keyboard_interrupt"
        finally:
            self._perform_graceful_shutdown(manager, uvicorn_workers, shutdown_reason)

    def _prepare_app_run(self, app: FastAPI):
        if self.track_requests:
            # create a copy of the middleware list
            app.user_middleware = list(app.user_middleware)

            # Add middleware to count active requests
            active_counter = mp.Value("i", 0, lock=True)
            self.active_counters.append(active_counter)
            app.add_middleware(RequestCountMiddleware, active_counter=active_counter)

    def _start_server(self, port, num_uvicorn_servers, log_level, sockets, uvicorn_worker_type, **kwargs):
        workers = []
        for response_queue_id in range(num_uvicorn_servers):
            self.app.response_queue_id = response_queue_id
            for lit_api in self.litapi_connector:
                if lit_api.spec:
                    lit_api.spec.response_queue_id = response_queue_id

            if _MCP_AVAILABLE:
                from litserve.mcp import _LitMCPServerConnector

                self.mcp_server = _LitMCPServerConnector()
                self.mcp_server.connect_mcp_server(self.litapi_connector.get_mcp_tools(), self.app)
            app: FastAPI = copy.copy(self.app)

            self._prepare_app_run(app)
            uvicorn_config = uvicorn.Config(
                app=app,
                host="0.0.0.0",
                port=port,
                log_level=log_level,
                timeout_graceful_shutdown=self.uvicorn_graceful_timeout,
                **kwargs,
            )
            if sys.platform == "win32" and num_uvicorn_servers > 1:
                logger.debug("Enable Windows explicit socket sharing...")
                # We make sure sockets is listening...
                # It prevents further [WinError 10022]
                for sock in sockets:
                    sock.listen(uvicorn_config.backlog)
                # We add worker to say unicorn to use a shared socket (win32)
                # https://github.com/encode/uvicorn/pull/802
                uvicorn_config.workers = num_uvicorn_servers

            server = _Server(config=uvicorn_config)
            if uvicorn_worker_type == "process":
                ctx = mp.get_context("fork")
                w = ctx.Process(
                    target=server.run, args=(response_queue_id, sockets), name=f"LitServer-{response_queue_id}"
                )
            elif uvicorn_worker_type == "thread":
                w = threading.Thread(
                    target=server.run, args=(response_queue_id, sockets), name=f"LitServer-{response_queue_id}"
                )
            else:
                raise ValueError("Invalid value for api_server_worker_type. Must be 'process' or 'thread'")
            w.start()
            workers.append(w)
        return dict(enumerate(workers))

    def setup_auth(self):
        if hasattr(self.lit_api, "authorize") and callable(self.lit_api.authorize):
            return self.lit_api.authorize
        if LIT_SERVER_API_KEY:
            return api_key_auth
        return no_auth

    def shutdown_api_key_auth(self, shutdown_api_key: str = Depends(oauth2_scheme)):
        if not SHUTDOWN_API_KEY or shutdown_api_key != SHUTDOWN_API_KEY:
            raise HTTPException(
                status_code=401,
                detail="Invalid Bearer token for Shutdown API."
                " Check that you are passing a correct 'Authorization: Bearer <SHUTDOWN_API_KEY>' in your header.",
            )

    def _start_worker_monitoring(
        self,
        manager: mp.Manager,
        uvicorn_workers: dict[str, Union[mp.Process, threading.Thread]],
    ):
        def monitor():
            try:
                while not self._shutdown_event.is_set():
                    broken_workers = {}

                    for i, proc in enumerate(self.inference_workers):
                        if proc.is_alive():
                            continue

                        if not self.restart_workers:
                            logger.error(f"⚠️ Worker {proc.name} died; shutting down")
                            self._perform_graceful_shutdown(manager, uvicorn_workers, f"⚠️ Worker {proc.name} died)")
                            return

                        broken_workers[i] = proc

                    for idx, proc in broken_workers.items():
                        lit_api_id = 0
                        worker_id = 0
                        count = 0
                        found = False

                        for i, lit_api in enumerate(self.litapi_connector):
                            workers_conf = self._inference_workers_config_for_api(lit_api.api_path)
                            num_workers_for_api = len(workers_conf)

                            if idx < count + num_workers_for_api:
                                lit_api_id = i
                                worker_id = idx - count
                                found = True
                                break
                            count += num_workers_for_api

                        if not found:
                            logger.error(f"Could not map worker index {idx} to an API.")
                            continue

                        for uid, resp in self.response_buffer.items():
                            if resp.worker_id is None or resp.worker_id != worker_id:
                                continue

                            # Check whether the event has already been set
                            if resp.event.is_set():
                                continue

                            resp.response = (None, LitAPIStatus.ERROR)

                            if resp.response_queue is not None:
                                resp.response_queue.append((None, LitAPIStatus.ERROR))

                            resp.event.set()
                            print(f"[monoriting] Marked {uid} set")

                        print(f"[monoriting] Worker {worker_id} is dead. Restarting it")
                        lit_api = self.litapi_connector.lit_apis[lit_api_id]
                        self.inference_workers[idx] = self.launch_single_inference_worker(lit_api, worker_id)
                        print(f"[monoriting] Worker {worker_id} has been started.")

                    time.sleep(self.monitor_internal)

            except Exception as e:
                print(e)

        t = threading.Thread(target=monitor, daemon=True, name="litserve-monitoring")
        t.start()
```

## File: `src/litserve/utils.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import base64
import dataclasses
import importlib.util
import logging
import os
import pdb
import pickle
import sys
import tempfile
import time
import uuid
import warnings
from abc import ABCMeta
from collections import deque
from collections.abc import AsyncIterator
from contextlib import contextmanager
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING, Any, Optional, TextIO, Union

from fastapi import HTTPException

if TYPE_CHECKING:
    from litserve.server import LitServer

logger = logging.getLogger(__name__)

_DEFAULT_LOG_FORMAT = (
    "%(asctime)s - %(processName)s[%(process)d] - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)
# Threshold for detecting heavy initialization tasks.
# A value of 1 second was chosen based on empirical observations
# of typical initialization times in this project.
_INIT_THRESHOLD = 1


class LitAPIStatus:
    START = "START"
    OK = "OK"
    ERROR = "ERROR"
    FINISH_STREAMING = "FINISH_STREAMING"


class LoopResponseType(Enum):
    STREAMING = "STREAMING"
    REGULAR = "REGULAR"


class PickleableHTTPException(HTTPException):
    @staticmethod
    def from_exception(exc: HTTPException):
        status_code = exc.status_code
        detail = exc.detail
        return PickleableHTTPException(status_code, detail)

    def __reduce__(self):
        return (HTTPException, (self.status_code, self.detail))


def dump_exception(exception):
    if isinstance(exception, HTTPException):
        exception = PickleableHTTPException.from_exception(exception)
    return pickle.dumps(exception)


async def azip(*async_iterables):
    iterators = [ait.__aiter__() for ait in async_iterables]
    while True:
        results = await asyncio.gather(*(ait.__anext__() for ait in iterators), return_exceptions=True)
        for result in results:
            if isinstance(result, StopAsyncIteration):
                return
            if isinstance(result, Exception):
                raise result
        yield tuple(results)


@contextmanager
def wrap_litserve_start(server: "LitServer", worker_monitor: bool = False):
    """Pytest utility to start the server in a context manager."""
    server.app.response_queue_id = 0
    for lit_api in server.litapi_connector:
        if lit_api.spec:
            lit_api.spec.response_queue_id = 0

    server.manager = server._init_manager(1)

    server.inference_workers = []
    for lit_api in server.litapi_connector:
        server.inference_workers.extend(server.launch_inference_worker(lit_api))

    server._prepare_app_run(server.app)

    if worker_monitor:
        server._start_worker_monitoring(server.manager, {})

    if is_package_installed("mcp"):
        from litserve.mcp import _LitMCPServerConnector

        server.mcp_server = _LitMCPServerConnector()
    else:
        server.mcp_server = None

    try:
        yield server
    finally:
        server._shutdown_event.set()
        # First close the transport to signal to the response_queue_to_buffer task that it should stop
        server._transport.close()
        for p in server.inference_workers:
            p.terminate()
            p.join()
        server.manager.shutdown()


async def call_after_stream(streamer: AsyncIterator, callback, *args, **kwargs):
    try:
        async for item in streamer:
            yield item
    except Exception as e:
        logger.exception(f"Error in streamer: {e}")
    finally:
        callback(*args, **kwargs)


@dataclasses.dataclass
class WorkerSetupStatus:
    STARTING: str = "starting"
    READY: str = "ready"
    ERROR: str = "error"
    FINISHED: str = "finished"


def _get_default_handler(stream, format):
    handler = logging.StreamHandler(stream)
    formatter = logging.Formatter(format)
    handler.setFormatter(formatter)
    return handler


def configure_logging(
    level: Union[str, int] = logging.INFO,
    format: str = _DEFAULT_LOG_FORMAT,
    stream: TextIO = sys.stdout,
    use_rich: bool = False,
):
    """Configure logging for the entire library with sensible defaults.

    Args:
        level (int): Logging level (default: logging.INFO)
        format (str): Log message format string
        stream (file-like): Output stream for logs
        use_rich (bool): Makes the logs more readable by using rich, useful for debugging. Defaults to False.

    """
    if isinstance(level, str):
        level = level.upper()
        level = getattr(logging, level)

    # Clear any existing handlers to prevent duplicates
    library_logger = logging.getLogger("litserve")
    for handler in library_logger.handlers[:]:
        library_logger.removeHandler(handler)

    if use_rich:
        try:
            from rich.logging import RichHandler
            from rich.traceback import install

            install(show_locals=True)
            handler = RichHandler(rich_tracebacks=True, show_time=True, show_path=True)
        except ImportError:
            logger.warning("Rich is not installed, using default logging")
            handler = _get_default_handler(stream, format)
    else:
        handler = _get_default_handler(stream, format)

    # Configure library logger
    library_logger.setLevel(level)
    library_logger.addHandler(handler)
    library_logger.propagate = False


def set_log_level(level):
    """Allow users to set the global logging level for the library."""
    logging.getLogger("litserve").setLevel(level)


def add_log_handler(handler):
    """Allow users to add custom log handlers.

    Example usage:
    file_handler = logging.FileHandler('library_logs.log')
    add_log_handler(file_handler)

    """
    logging.getLogger("litserve").addHandler(handler)


def generate_random_zmq_address(temp_dir="/tmp"):
    """Generate a random IPC address in the /tmp directory.

    Ensures the address is unique.
    Returns:
        str: A random IPC address suitable for ZeroMQ.

    """
    unique_name = f"zmq-{uuid.uuid4().hex}.ipc"
    ipc_path = os.path.join(temp_dir, unique_name)
    return f"ipc://{ipc_path}"


class ForkedPdb(pdb.Pdb):
    # Borrowed from - https://github.com/Lightning-AI/forked-pdb
    """
    PDB Subclass for debugging multi-processed code
    Suggested in: https://stackoverflow.com/questions/4716533/how-to-attach-debugger-to-a-python-subproccess
    """

    def interaction(self, *args: Any, **kwargs: Any) -> None:
        _stdin = sys.stdin
        try:
            sys.stdin = open("/dev/stdin")  # noqa: SIM115
            pdb.Pdb.interaction(self, *args, **kwargs)
        finally:
            sys.stdin = _stdin


def set_trace():
    """Set a tracepoint in the code."""
    ForkedPdb().set_trace()


def set_trace_if_debug(debug_env_var="LITSERVE_DEBUG", debug_env_var_value="1"):
    """Set a tracepoint in the code if the environment variable LITSERVE_DEBUG is set."""
    if os.environ.get(debug_env_var) == debug_env_var_value:
        set_trace()


def is_package_installed(package_name: str) -> bool:
    spec = importlib.util.find_spec(package_name)
    return spec is not None


class _TimedInitMeta(ABCMeta):
    def __new__(mcls, name, bases, namespace, **kwargs):
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        cls._has_custom_setup = False

        for base in bases:
            if hasattr(base, "setup"):
                base_setup = base.setup

                if "setup" in namespace and namespace["setup"] is not base_setup:
                    cls._has_custom_setup = True
                    break
        else:
            if "setup" in namespace:
                cls._has_custom_setup = True

        return cls

    def __call__(cls, *args, **kwargs):
        start_time = time.perf_counter()
        instance = super().__call__(*args, **kwargs)
        elapsed = time.perf_counter() - start_time

        if elapsed >= _INIT_THRESHOLD and not cls._has_custom_setup:
            warnings.warn(
                (
                    f"{cls.__name__}.__init__ took {elapsed:.2f} seconds to execute. This suggests that you're "
                    "loading a model or doing other heavy processing inside the constructor.\n\n"
                    "To improve startup performance and avoid unnecessary work across processes, move any one-time "
                    f"heavy initialization into the `{cls.__name__}.setup` method.\n\n"
                    "The `LitAPI.setup` method is designed for deferred, process-specific loading — ideal for models "
                    "and large resources."
                ),
                RuntimeWarning,
                stacklevel=2,
            )

        return instance


def add_ssl_context_from_env(kwargs: dict[str, Any]) -> dict[str, Any]:
    """Loads SSL context from base64-encoded environment variables.

    This function checks for the presence of `LIGHTNING_CERT_PEM` and
    `LIGHTNING_KEY_FILE` environment variables. It expects these variables
    to contain the SSL certificate and private key, respectively, as
    base64-encoded PEM strings.

    If both variables are found, it decodes them and writes the content to
    secure, temporary files. The paths to these files are returned in a
    dictionary suitable for direct use as keyword arguments in libraries
    that require SSL file paths (like `uvicorn` or `requests`).

    Note:
        The temporary files are not automatically deleted (`delete=False`).
        The calling application is responsible for cleaning up these files
        after the SSL context is no longer needed to prevent leaving
        sensitive data on disk.

    Returns:
        dict[str, Any]: A dictionary containing `ssl_certfile` and `ssl_keyfile`
        keys with `pathlib.Path` objects pointing to the temporary files.
        If either of the required environment variables is missing, it
        returns an empty dictionary.

    """

    if "ssl_keyfile" in kwargs and "ssl_certfile" in kwargs:
        return kwargs

    cert_pem_b64 = os.getenv("LIGHTNING_CERT_PEM", "")
    cert_key_b64 = os.getenv("LIGHTNING_KEY_FILE", "")

    if cert_pem_b64 == "" or cert_key_b64 == "":
        return kwargs

    # Decode the base64 strings to get the actual PEM content
    cert_pem = base64.b64decode(cert_pem_b64).decode("utf-8")
    cert_key = base64.b64decode(cert_key_b64).decode("utf-8")

    # Write to temporary files
    with (
        tempfile.NamedTemporaryFile(mode="w+", delete=False) as cert_file,
        tempfile.NamedTemporaryFile(mode="w+", delete=False) as key_file,
    ):
        cert_file.write(cert_pem)
        cert_file.flush()
        key_file.write(cert_key)
        key_file.flush()

        logger.info("Loading TLS Certificates \n")

        # Return a dictionary with Path objects to the created files
        return {"ssl_keyfile": Path(key_file.name), "ssl_certfile": Path(cert_file.name), **kwargs}


@dataclasses.dataclass
class ResponseBufferItem:
    event: asyncio.Event
    response_queue: Optional[deque] = None
    worker_id: Optional[int] = None
    response: Optional[Any] = None
```

## File: `src/litserve/callbacks/__init__.py`
```python
from litserve.callbacks.base import Callback, CallbackRunner, EventTypes, NoopCallback

__all__ = ["Callback", "CallbackRunner", "EventTypes", "NoopCallback"]
```

## File: `src/litserve/callbacks/base.py`
```python
import logging
from abc import ABC
from enum import Enum
from typing import Union

logger = logging.getLogger(__name__)


class EventTypes(Enum):
    BEFORE_SETUP = "on_before_setup"
    AFTER_SETUP = "on_after_setup"
    BEFORE_DECODE_REQUEST = "on_before_decode_request"
    AFTER_DECODE_REQUEST = "on_after_decode_request"
    BEFORE_ENCODE_RESPONSE = "on_before_encode_response"
    AFTER_ENCODE_RESPONSE = "on_after_encode_response"
    BEFORE_PREDICT = "on_before_predict"
    AFTER_PREDICT = "on_after_predict"
    ON_SERVER_START = "on_server_start"
    ON_SERVER_END = "on_server_end"
    ON_REQUEST = "on_request"
    ON_RESPONSE = "on_response"


class Callback(ABC):
    def on_before_setup(self, *args, **kwargs):
        """Called before setup is started."""

    def on_after_setup(self, *args, **kwargs):
        """Called after setup is completed."""

    def on_before_decode_request(self, *args, **kwargs):
        """Called before request decoding is started."""

    def on_after_decode_request(self, *args, **kwargs):
        """Called after request decoding is completed."""

    def on_before_encode_response(self, *args, **kwargs):
        """Called before response encoding is started."""

    def on_after_encode_response(self, *args, **kwargs):
        """Called after response encoding is completed."""

    def on_before_predict(self, *args, **kwargs):
        """Called before prediction is started."""

    def on_after_predict(self, *args, **kwargs):
        """Called after prediction is completed."""

    def on_server_start(self, *args, **kwargs):
        """Called before server starts."""

    def on_server_end(self, *args, **kwargs):
        """Called when server terminates."""

    def on_request(self, *args, **kwargs):
        """Called when request enters the endpoint function."""

    def on_response(self, *args, **kwargs):
        """Called when response is generated from the worker and ready to return to the client."""

    # Adding a new hook? Register it with the EventTypes dataclass too,


class CallbackRunner:
    def __init__(self, callbacks: Union[Callback, list[Callback]] = None):
        self._callbacks = []
        if callbacks:
            self._add_callbacks(callbacks)

    def _add_callbacks(self, callbacks: Union[Callback, list[Callback]]):
        if not isinstance(callbacks, list):
            callbacks = [callbacks]
        for callback in callbacks:
            if not isinstance(callback, Callback):
                raise ValueError(f"Invalid callback type: {callback}")
        self._callbacks.extend(callbacks)

    def trigger_event(self, event_name, *args, **kwargs):
        """Triggers an event, invoking all registered callbacks for that event."""
        for callback in self._callbacks:
            try:
                getattr(callback, event_name)(*args, **kwargs)
            except Exception:
                # Handle exceptions to prevent one callback from disrupting others
                logger.exception(f"Error in callback '{callback}' during event '{event_name}'")


class NoopCallback(Callback):
    """This callback does nothing."""
```

## File: `src/litserve/callbacks/defaults/__init__.py`
```python
from litserve.callbacks.defaults.metric_callback import PredictionTimeLogger

__all__ = ["PredictionTimeLogger"]
```

## File: `src/litserve/callbacks/defaults/metric_callback.py`
```python
import time
import typing

from litserve.callbacks.base import Callback

if typing.TYPE_CHECKING:
    from litserve import LitAPI


class PredictionTimeLogger(Callback):
    def on_before_predict(self, lit_api: "LitAPI"):
        self._start_time = time.perf_counter()

    def on_after_predict(self, lit_api: "LitAPI"):
        elapsed = time.perf_counter() - self._start_time
        print(f"Prediction took {elapsed:.2f} seconds", flush=True)


class RequestTracker(Callback):
    def on_request(self, active_requests: int, **kwargs):
        print(f"Active requests: {active_requests}", flush=True)
```

## File: `src/litserve/loops/__init__.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import multiprocessing as mp

from litserve.loops.base import LitLoop, _BaseLoop
from litserve.loops.continuous_batching_loop import ContinuousBatchingLoop, Output
from litserve.loops.loops import (
    get_default_loop,
    inference_worker,
)
from litserve.loops.simple_loops import BatchedLoop, SingleLoop
from litserve.loops.streaming_loops import BatchedStreamingLoop, StreamingLoop

mp.allow_connection_pickling()

__all__ = [
    "_BaseLoop",
    "LitLoop",
    "get_default_loop",
    "inference_worker",
    "Output",
    "SingleLoop",
    "BatchedLoop",
    "StreamingLoop",
    "BatchedStreamingLoop",
    "ContinuousBatchingLoop",
]
```

## File: `src/litserve/loops/base.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import inspect
import logging
import os
import pickle
import signal
import sys
import time
from abc import ABC
from queue import Empty, Queue
from typing import Any, Optional, Union

from starlette.formparsers import MultiPartParser

from litserve import LitAPI
from litserve.callbacks import CallbackRunner
from litserve.specs.base import LitSpec
from litserve.transport.base import MessageTransport
from litserve.utils import LitAPIStatus, LoopResponseType

logger = logging.getLogger(__name__)
# FastAPI writes form files to disk over 1MB by default, which prevents serialization by multiprocessing
MultiPartParser.max_file_size = sys.maxsize
# renamed in PR: https://github.com/encode/starlette/pull/2780
MultiPartParser.spool_max_size = sys.maxsize

_DEFAULT_STOP_LOOP_MESSAGE = "Received sentinel value, stopping loop"
_SENTINEL_VALUE = (None, None, None, None)


def _inject_context(context: Union[list[dict], dict], func, *args, **kwargs):
    sig = inspect.signature(func)
    if "context" in sig.parameters:
        return func(*args, **kwargs, context=context)
    return func(*args, **kwargs)


async def _sync_fn_to_async_fn(func, *args, **kwargs):
    if inspect.isgeneratorfunction(func):

        async def async_fn(*args, **kwargs):
            for item in func(*args, **kwargs):
                yield item
            return

        return async_fn(*args, **kwargs)

    return await asyncio.to_thread(func, *args, **kwargs)


async def _handle_async_function(func, *args, **kwargs):
    # Call the function based on its type
    if inspect.isasyncgenfunction(func):
        # Async generator - return directly (don't await)
        return func(*args, **kwargs)
    if asyncio.iscoroutinefunction(func):
        # Async function - await the result
        return await func(*args, **kwargs)

    # Sync function - convert to async function, then await if result is awaitable
    result = await _sync_fn_to_async_fn(func, *args, **kwargs)

    # Check if the result is awaitable (coroutine)
    if asyncio.iscoroutine(result):
        return await result

    return result


async def _async_inject_context(context: Union[list[dict], dict], func, *args, **kwargs):
    sig = inspect.signature(func)

    # Determine if we need to inject context
    if "context" in sig.parameters:
        kwargs["context"] = context

    return await _handle_async_function(func, *args, **kwargs)


class _StopLoopError(Exception):
    def __init__(self, message: str = _DEFAULT_STOP_LOOP_MESSAGE):
        self.message = message
        super().__init__(self.message)


def collate_requests(
    loop: "LitLoop",
    lit_api: LitAPI,
    request_queue: Queue,
    transport: MessageTransport,
) -> tuple[list, list]:
    payloads = []
    timed_out_uids = []
    entered_at = time.monotonic()
    end_time = entered_at + lit_api.batch_timeout
    apply_timeout = lit_api.request_timeout not in (-1, False)

    if lit_api.batch_timeout == 0:
        while len(payloads) < lit_api.max_batch_size:
            try:
                request_data = request_queue.get_nowait()
                if request_data == _SENTINEL_VALUE:
                    raise _StopLoopError()

                response_queue_id, uid, timestamp, x_enc = request_data

                loop.put_response(
                    transport=transport,
                    response_queue_id=response_queue_id,
                    uid=uid,
                    response_data=(),
                    status=LitAPIStatus.START,
                    response_type=LoopResponseType.STREAMING if lit_api.stream else LoopResponseType.REGULAR,
                )

                if apply_timeout and time.monotonic() - timestamp > lit_api.request_timeout:
                    timed_out_uids.append((response_queue_id, uid))
                else:
                    payloads.append((response_queue_id, uid, x_enc))
            except Empty:
                break
        return payloads, timed_out_uids

    while time.monotonic() < end_time and len(payloads) < lit_api.max_batch_size:
        remaining_time = end_time - time.monotonic()
        if remaining_time <= 0:
            break

        try:
            request_data = request_queue.get(timeout=min(remaining_time, 0.001))
            if request_data == _SENTINEL_VALUE:
                raise _StopLoopError()

            response_queue_id, uid, timestamp, x_enc = request_data

            loop.put_response(
                transport=transport,
                response_queue_id=response_queue_id,
                uid=uid,
                response_data=(),
                status=LitAPIStatus.START,
                response_type=LoopResponseType.STREAMING if lit_api.stream else LoopResponseType.REGULAR,
            )

            if apply_timeout and time.monotonic() - timestamp > lit_api.request_timeout:
                timed_out_uids.append((response_queue_id, uid))
            else:
                payloads.append((response_queue_id, uid, x_enc))

        except Empty:
            continue

    return payloads, timed_out_uids


class _BaseLoop(ABC):
    """Loop runs an inference engine that executes a specific set of hooks, implemented in the LitAPI, in a predefined
    order.

    For a default loop, LitAPI must implement the following hooks:
      - decode_request
      - batch
      - predict
      - unbatch
      - encode_response

    To implement a custom loop, subclass this class and implement the `run` method. The `run` method should execute the
    hooks in the desired order.

    `__call__` method is the entry point for the worker process. It calls the `run` method in a loop until the worker is
    terminated.

    Example:

    ```python
    class TestLoop(_BaseLoop):
        def run(
            self,
            lit_api: LitAPI,
            lit_spec: Optional[LitSpec],
            device: str,
            worker_id: int,
            request_queue: Queue,
            response_queues: list[Queue],
            stream: bool,
            workers_setup_status: dict[int, str],
            callback_runner: CallbackRunner,
        ):
            item = request_queue.get()
            if item is None:
                return

            response_queue_id, uid, timestamp, x_enc = item
            # Expects LitAPI to implement the load_cache method
            lit_api.load_cache(x_enc)
            x = lit_api.decode_request(x_enc)
            response = lit_api.predict(x)
            response_enc = lit_api.encode_response(response)
            response_queues[response_queue_id].put((uid, (response_enc, LitAPIStatus.OK, LoopResponseType.REGULAR)))
    ```

    """

    def pre_setup(self, lit_api: LitAPI, spec: Optional[LitSpec] = None):
        pass

    async def schedule_task(
        self,
        lit_api: LitAPI,
        lit_spec: Optional[LitSpec],
        request_queue: Queue,
        transport: MessageTransport,
    ):
        pass

    def __call__(
        self,
        lit_api: LitAPI,
        device: str,
        worker_id: int,
        request_queue: Queue,
        transport: MessageTransport,
        workers_setup_status: dict[int, str],
        callback_runner: CallbackRunner,
    ):
        lit_spec = lit_api.spec
        if asyncio.iscoroutinefunction(self.run):
            event_loop = asyncio.new_event_loop()

            async def _wrapper():
                logger.info("Running LitLoop in a asyncio event loop")
                future = self.schedule_task(lit_api, lit_spec, request_queue, transport)
                schedule_task = event_loop.create_task(future)
                while True:
                    try:
                        await self.run(
                            lit_api,
                            device,
                            worker_id,
                            request_queue,
                            transport,
                            workers_setup_status,
                            callback_runner,
                        )
                        await asyncio.sleep(0)
                    except Exception as e:
                        logger.exception("An error occurred in the loop: %s", e)

                    if not lit_api.has_active_requests() and schedule_task.done():
                        for uid, response_queue_id in self.response_queue_ids.items():
                            self.put_error_response(
                                transport,
                                response_queue_id,
                                uid,
                                Exception("schedule_task task failed"),
                                LoopResponseType.STREAMING,
                            )
                        self.on_schedule_task_done(schedule_task)

                    await asyncio.sleep(0)

            event_loop.run_until_complete(_wrapper())
        else:
            while True:
                self.run(
                    lit_api,
                    device,
                    worker_id,
                    request_queue,
                    transport,
                    workers_setup_status,
                    callback_runner,
                )

    def run(
        self,
        lit_api: LitAPI,
        device: str,
        worker_id: int,
        request_queue: Queue,
        transport: MessageTransport,
        workers_setup_status: dict[int, str],
        callback_runner: CallbackRunner,
    ):
        raise NotImplementedError

    def on_schedule_task_done(self, schedule_task: asyncio.Task) -> None:
        pass


class LitLoop(_BaseLoop):
    def __init__(self):
        self._context = {}
        self._server_pid = os.getpid()
        self._worker_id = None
        self._restart_workers = False

    def kill(self):
        try:
            logger.debug(f"Stop Server Requested - Kill parent pid [{self._server_pid}] from [{os.getpid()}]")
            if sys.platform == "win32":
                os.kill(self._server_pid, signal.SIGTERM)
        except PermissionError:
            # Access Denied because pid already killed...
            return

    def get_batch_requests(
        self,
        lit_api: LitAPI,
        request_queue: Queue,
        transport: MessageTransport,
    ) -> tuple[list, list]:
        batches, timed_out_uids = collate_requests(
            loop=self,
            lit_api=lit_api,
            request_queue=request_queue,
            transport=transport,
        )
        return batches, timed_out_uids

    def get_request(self, request_queue: Queue, block: bool = True, timeout: Optional[float] = None):
        try:
            return request_queue.get(block=block, timeout=timeout)
        except Empty:
            return None

    def populate_context(self, lit_spec: LitSpec, request: Any):
        if lit_spec and hasattr(lit_spec, "populate_context"):
            lit_spec.populate_context(self._context, request)

    @property
    def worker_id(self) -> Optional[int]:
        if self._worker_id is None:
            worker_id = os.environ.get("LITSERVE_WORKER_ID", None)
            self._worker_id = int(worker_id) if worker_id is not None else worker_id
        return self._worker_id

    def put_response(
        self,
        transport: MessageTransport,
        response_queue_id: int,
        uid: str,
        response_data: Any,
        status: LitAPIStatus,
        response_type: LoopResponseType,
    ) -> None:
        # Skip sending the start status if we dont plan to restart the workers
        if status == LitAPIStatus.START and not self._restart_workers:
            return

        transport.send((uid, (response_data, status, response_type, self.worker_id)), consumer_id=response_queue_id)

    def put_error_response(
        self,
        transport: MessageTransport,
        response_queue_id: int,
        uid: str,
        error: Exception,
        response_type: LoopResponseType = LoopResponseType.REGULAR,
    ) -> None:
        error = pickle.dumps(error)
        self.put_response(transport, response_queue_id, uid, error, LitAPIStatus.ERROR, response_type)


class DefaultLoop(LitLoop):
    def pre_setup(self, lit_api: LitAPI, spec: Optional[LitSpec] = None):
        # we will sanitize regularly if no spec
        # in case, we have spec then:
        # case 1: spec implements a streaming API
        # Case 2: spec implements a non-streaming API
        if lit_api.spec:
            # TODO: Implement sanitization
            return

        original = lit_api.unbatch.__code__ is LitAPI.unbatch.__code__
        if not lit_api.stream and any(
            [
                inspect.isgeneratorfunction(lit_api.predict) or inspect.isasyncgenfunction(lit_api.predict),
                inspect.isgeneratorfunction(lit_api.encode_response)
                or inspect.isasyncgenfunction(lit_api.encode_response),
            ]
        ):
            raise ValueError(
                """When `stream=False`, `lit_api.predict`, `lit_api.encode_response` must not be
                generator or async generator functions.

                Correct usage:

                    def predict(self, inputs):
                        ...
                        return {"output": output}

                    # Or async version if using LitAPI(..., enable_async=True)
                    async def predict(self, inputs):
                        ...
                        return {"output": output}

                Incorrect usage:

                    def predict(self, inputs):
                        ...
                        for i in range(max_token_length):
                            yield prediction

                    # Or async version if using LitAPI(..., enable_async=True)
                    async def predict(self, inputs):
                        ...
                        for i in range(max_token_length):
                            yield prediction
                """
            )
        if (
            lit_api.stream
            and lit_api.max_batch_size > 1
            and not all(
                [
                    inspect.isgeneratorfunction(lit_api.predict) or inspect.isasyncgenfunction(lit_api.predict),
                    inspect.isgeneratorfunction(lit_api.encode_response)
                    or inspect.isasyncgenfunction(lit_api.encode_response),
                    (
                        original
                        or inspect.isgeneratorfunction(lit_api.unbatch)
                        or inspect.isasyncgenfunction(lit_api.unbatch)
                    ),
                ]
            )
        ):
            raise ValueError(
                """When `stream=True` with max_batch_size > 1, `lit_api.predict`, `lit_api.encode_response` and
                `lit_api.unbatch` must generate values using `yield` (can be regular or async generators).

             Example:

                def predict(self, inputs):
                    ...
                    for i in range(max_token_length):
                        yield prediction

                def encode_response(self, outputs):
                    for output in outputs:
                        encoded_output = ...
                        yield encoded_output

                def unbatch(self, outputs):
                    for output in outputs:
                        unbatched_output = ...
                        yield unbatched_output

                # Or using async generators if using LitAPI(..., enable_async=True):
                async def predict(self, inputs):
                    ...
                    for i in range(max_token_length):
                        await asyncio.sleep(0.01)  # Some async work
                        yield prediction
             """
            )

        if lit_api.stream and not all(
            [
                inspect.isgeneratorfunction(lit_api.predict) or inspect.isasyncgenfunction(lit_api.predict),
                inspect.isgeneratorfunction(lit_api.encode_response)
                or inspect.isasyncgenfunction(lit_api.encode_response),
            ]
        ):
            raise ValueError(
                """When `stream=True` both `lit_api.predict` and
             `lit_api.encode_response` must generate values using `yield` (can be regular or async generators).

             Example:

                def predict(self, inputs):
                    ...
                    for i in range(max_token_length):
                        yield prediction

                def encode_response(self, outputs):
                    for output in outputs:
                        encoded_output = ...
                        yield encoded_output

                # Or using async generators:
                async def predict(self, inputs):
                    ...
                    for i in range(max_token_length):
                        await asyncio.sleep(0.01)  # Some async work
                        yield prediction
             """
            )
```

## File: `src/litserve/loops/continuous_batching_loop.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import logging
import time
from dataclasses import dataclass
from queue import Queue
from typing import Any, Optional

from fastapi import HTTPException

from litserve import LitAPI
from litserve.callbacks import CallbackRunner
from litserve.loops.base import LitLoop
from litserve.specs.base import LitSpec
from litserve.transport.base import MessageTransport
from litserve.utils import LitAPIStatus, LoopResponseType

logger = logging.getLogger(__name__)


def notify_timed_out_requests(
    response_queues: list[Queue],
    timed_out_uids: list[tuple[int, str]],
):
    for response_queue_id, uid in timed_out_uids:
        logger.error(f"Request {uid} was waiting in the queue for too long and has been timed out.")
        response_queues[response_queue_id].put(
            (
                uid,
                (HTTPException(504, "Request timed out"), LitAPIStatus.ERROR, LoopResponseType.STREAMING),
            )
        )


@dataclass
class Output:
    """Outputs from a single step of the loop."""

    uid: str
    output: Any
    status: LitAPIStatus


class ContinuousBatchingLoop(LitLoop):
    def __init__(self, max_sequence_length: int = 2048, no_pending_requests: bool = False, sleep_delay: float = 0.001):
        """Runs continuous batching loop. This loop handles adding new requests, processing them in batches, and
        managing the state of active sequences.

        The loop requires the following methods to be implemented in the LitAPI:
          - setup: sets up the model on the device
          - decode_request: decodes the client request into a format that can be processed by the model
          - step: generates a new token for each sequence
          - encode_response: encodes the response into a format that can be sent to the client
          - has_finished: checks if the sequence has finished generating

        Args:
            max_sequence_length (int): The maximum sequence length allowed for any active sequence.

        """
        super().__init__()
        self.active_sequences: dict[str, dict] = {}  # uid -> {input, current_length, generated_sequence}
        self.max_sequence_length = max_sequence_length
        self.response_queue_ids: dict[str, int] = {}  # uid -> response_queue_id
        self.no_pending_requests = no_pending_requests
        self.sleep_delay = sleep_delay

    def pre_setup(self, lit_api: LitAPI, spec: Optional[LitSpec] = None):
        """Check if the lit_api has the necessary methods and if streaming is enabled."""
        if not lit_api.stream:
            raise ValueError(
                "Continuous batching loop requires streaming to be enabled. Please set LitServe(..., stream=True)"
            )

        if not hasattr(lit_api, "step") and not hasattr(lit_api, "predict"):
            raise ValueError("""Using the default step method with Continuous batching loop requires the lit_api to
have a `predict` method which accepts decoded request inputs and a list of generated_sequence.
Please implement the has_finished method in the lit_api.

    class ExampleAPI(LitAPI):
        ...
        def predict(self, inputs, generated_sequence):
            # implement predict logic
            # return list of new tokens
            ...
        """)

        if not hasattr(lit_api, "step") and not hasattr(lit_api, "has_finished"):
            raise ValueError("""Using the default step method with Continuous batching loop
requires the lit_api to have a has_finished method. Please implement the has_finished method in the lit_api.

    class ExampleAPI(LitAPI):
        ...
        def has_finished(self, uid: str, token: str, max_sequence_length: int) -> bool:
            # implement has_finished logic
            return False
        """)

    def add_request(
        self,
        uid: str,
        request: Any,
        lit_api: LitAPI,
        lit_spec: Optional[LitSpec],
        transport: Optional[MessageTransport] = None,
    ) -> None:
        """Add a new sequence to active sequences and perform any action before prediction such as filling the cache."""
        lit_api.add_request(uid, request)
        self.active_sequences[uid] = {"input": request}

    def mark_completed(self, uid: str) -> None:
        """Mark a request as completed and remove it from the tracked state."""
        logger.debug(f"Marking sequence {uid} as completed")
        del self.active_sequences[uid]
        del self.response_queue_ids[uid]

    def has_capacity(self, lit_api: LitAPI) -> bool:
        """Check if we can add more sequences based on current batch."""
        return lit_api.has_capacity()

    async def prefill(
        self,
        pending_requests: list[tuple[str, Any]],
        lit_api: LitAPI,
        lit_spec: Optional[LitSpec],
        request_queue: Queue,
        transport: MessageTransport,
        max_batch_size: Optional[int] = None,
        batch_timeout: Optional[float] = None,
    ) -> list[tuple[str, Any]]:
        """Fill available capacity with pending and new requests."""
        # First process existing pending requests
        while pending_requests and self.has_capacity(lit_api):
            response_queue_id, uid, input = pending_requests.pop(0)
            self.add_request(uid, input, lit_api, lit_spec, transport)
            self.response_queue_ids[uid] = response_queue_id

        while True:
            if self.no_pending_requests and lit_api.has_active_requests():
                await asyncio.sleep(self.sleep_delay)
                return pending_requests

            request = await asyncio.to_thread(self.get_request, request_queue, timeout=1, block=True)
            if request is None:
                break

            response_queue_id, uid, timestamp, input = request

            logger.debug(
                f"[worker {self.worker_id}] uid:{uid}, duration:{time.monotonic() - timestamp},"
                f"pending_requests: {len(pending_requests)}"
            )

            self.put_response(
                transport=transport,
                response_queue_id=response_queue_id,
                uid=uid,
                response_data=(),
                status=LitAPIStatus.START,
                response_type=LoopResponseType.STREAMING,
            )

            if self.has_capacity(lit_api):
                logger.debug(f"New request: {uid}, {input}")
                self.response_queue_ids[uid] = response_queue_id
                self.add_request(uid, input, lit_api, lit_spec, transport)
            else:
                pending_requests.append((response_queue_id, uid, input))
                break

        return pending_requests

    async def schedule_task(
        self,
        lit_api: LitAPI,
        lit_spec: Optional[LitSpec],
        request_queue: Queue,
        transport: MessageTransport,
    ):
        logger.info("Running prefill in background")
        try:
            pending_requests = []
            while True:
                pending_requests = await self.prefill(
                    pending_requests,
                    lit_api,
                    lit_spec,
                    request_queue,
                    transport,
                    max_batch_size=lit_api.max_batch_size,
                    batch_timeout=lit_api.batch_timeout,
                )
                await asyncio.sleep(0)
        except Exception as e:
            logger.exception("An error occurred in run_in_background: %s", e)
        finally:
            logger.info("Exiting run_in_background in continuous_batching_loop")

    async def step(
        self, prev_outputs: Optional[list[Output]], lit_api: LitAPI, lit_spec: Optional[LitSpec]
    ) -> list[Output]:
        return await asyncio.to_thread(lit_api.step, prev_outputs)

    async def run(
        self,
        lit_api: LitAPI,
        device: str,
        worker_id: int,
        request_queue: Queue,
        transport: MessageTransport,
        workers_setup_status: dict[int, str],
        callback_runner: CallbackRunner,
    ):
        """Main loop that processes batches of requests."""

        warning_counter = 0
        lit_spec = lit_api.spec
        try:
            prev_outputs = None
            while lit_api.has_active_requests():
                # Process one step for all active sequences
                responses = await self.step(prev_outputs, lit_api, lit_spec)
                if len(responses) == 0:
                    # Log once every 10 seconds
                    if warning_counter == 0:
                        logger.warning("No responses from step() but has_active_requests() is true")

                    # increment the counter
                    warning_counter += 1

                    if warning_counter > 1000:
                        warning_counter = 0

                    # sleep to avoid starving the cpu
                    await asyncio.sleep(0.01)
                    continue

                if responses and not isinstance(responses[0], Output):
                    raise HTTPException(500, "Expected StepOutput from step()")

                prev_outputs = responses
                # Send responses for all sequences (both streaming and completed)
                for step_output in responses:
                    status = step_output.status
                    response_data = lit_api.encode_response(step_output.output)
                    uid = step_output.uid
                    response_queue_id = self.response_queue_ids[uid]

                    response_data = lit_api.format_encoded_response(response_data)
                    if status == LitAPIStatus.ERROR:
                        self.put_error_response(
                            transport, response_queue_id, uid, response_data, LoopResponseType.STREAMING
                        )
                        self.mark_completed(uid)
                    elif status == LitAPIStatus.FINISH_STREAMING:
                        self.put_response(
                            transport, response_queue_id, uid, response_data, status, LoopResponseType.STREAMING
                        )
                        self.mark_completed(uid)
                    else:
                        self.put_response(
                            transport, response_queue_id, uid, response_data, status, LoopResponseType.STREAMING
                        )

        except Exception as e:
            logger.exception(f"Error in continuous batching loop: {e}")
            # Handle any errors by sending error responses for all tracked requests
            for uid, response_queue_id in self.response_queue_ids.items():
                self.put_error_response(transport, response_queue_id, uid, e, LoopResponseType.STREAMING)
            self.response_queue_ids.clear()
            self.active_sequences.clear()

    def on_schedule_task_error(self, exception: Exception):
        pass


class DefaultContinuousBatchingLoop(ContinuousBatchingLoop):
    def add_request(self, uid: str, request: Any, lit_api: LitAPI, lit_spec: Optional[LitSpec]) -> None:
        """Add a new sequence to active sequences and perform any action before prediction such as filling the cache."""
        decoded_request = lit_api.decode_request(request)
        self.active_sequences[uid] = {"input": decoded_request, "current_length": 0, "generated_sequence": []}

    async def step(
        self, prev_outputs: Optional[list[Output]], lit_api: LitAPI, lit_spec: Optional[LitSpec]
    ) -> list[Output]:
        """Process one token generation step for all active sequences."""
        if not self.active_sequences:
            return []

        # Batch forward pass for all active sequences
        inputs = [seq["input"] for seq in self.active_sequences.values()]
        generated = [seq["generated_sequence"] for seq in self.active_sequences.values()]

        try:
            # Assume lit_api.predict handles batched token generation
            new_tokens: list[Any] = lit_api.predict(inputs, generated)

            responses: list[Output] = []

            # Process each sequence's new token
            for uid, token in zip(self.active_sequences.keys(), new_tokens):
                seq = self.active_sequences[uid]
                seq["generated_sequence"].append(token)
                seq["current_length"] += 1

                step_output = Output(uid, token, LitAPIStatus.OK)
                responses.append(step_output)

                # Check completion conditions
                is_finished = lit_api.has_finished(uid, token, self.max_sequence_length)

                if is_finished:
                    # Encode final response for completed sequence
                    step_output = Output(uid, "", LitAPIStatus.FINISH_STREAMING)
                    responses.append(step_output)

            return responses

        except Exception as e:
            logger.exception("Error during batch token generation")
            # On error, terminate all active sequences
            responses = [(uid, (e, LitAPIStatus.ERROR)) for uid in self.active_sequences]
            self.active_sequences.clear()
            return responses

    def has_capacity(self, lit_api: LitAPI) -> bool:
        capacity = len(self.active_sequences) < lit_api.max_batch_size
        if not capacity:
            logger.info(
                f"No capacity: {len(self.active_sequences)} active sequences, max batch size: {lit_api.max_batch_size}"
            )
        return capacity
```

## File: `src/litserve/loops/loops.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import os
from queue import Queue

from litserve import LitAPI
from litserve.callbacks import CallbackRunner, EventTypes
from litserve.loops.base import LitLoop, _BaseLoop
from litserve.loops.simple_loops import BatchedLoop, SingleLoop
from litserve.loops.streaming_loops import BatchedStreamingLoop, StreamingLoop
from litserve.transport.base import MessageTransport
from litserve.utils import WorkerSetupStatus

logger = logging.getLogger(__name__)


def get_default_loop(stream: bool, max_batch_size: int, enable_async: bool = False) -> _BaseLoop:
    """Get the default loop based on the stream flag, batch size, and async support.

    Args:
        stream: Whether streaming is enabled
        max_batch_size: Maximum batch size
        enable_async: Whether async support is enabled (supports both coroutines and async generators)

    Returns:
        The appropriate loop implementation

    Raises:
        ValueError: If async and batching are enabled together (not supported)

    """
    if enable_async:
        if max_batch_size > 1:
            raise ValueError("Async batching is not supported. Please use enable_async=False with batching.")
        if stream:
            return StreamingLoop()  # StreamingLoop now supports async
        return SingleLoop()  # Only SingleLoop supports async currently

    if stream:
        if max_batch_size > 1:
            return BatchedStreamingLoop()
        return StreamingLoop()

    if max_batch_size > 1:
        return BatchedLoop()
    return SingleLoop()


def inference_worker(
    lit_api: LitAPI,
    device: str,
    worker_id: int,
    request_queue: Queue,
    transport: MessageTransport,
    workers_setup_status: dict[int, str],
    callback_runner: CallbackRunner,
    restart_workers: bool,
):
    os.environ["LITSERVE_WORKER_ID"] = str(worker_id)

    lit_spec = lit_api.spec
    loop: LitLoop = lit_api.loop
    stream = lit_api.stream

    endpoint = lit_api.api_path.split("/")[-1]

    callback_runner.trigger_event(EventTypes.BEFORE_SETUP.value, lit_api=lit_api)
    try:
        lit_api.setup(device)
    except Exception:
        logger.exception(f"Error setting up worker {worker_id}.")
        workers_setup_status[f"{endpoint}_{worker_id}"] = WorkerSetupStatus.ERROR
        return
    lit_api.device = device
    callback_runner.trigger_event(EventTypes.AFTER_SETUP.value, lit_api=lit_api)

    if workers_setup_status:
        workers_setup_status[f"{endpoint}_{worker_id}"] = WorkerSetupStatus.READY

    if lit_spec:
        logging.info(f"LitServe will use {lit_spec.__class__.__name__} spec")

    if loop == "auto":
        loop = get_default_loop(stream, lit_api.max_batch_size, lit_api.enable_async)

    loop._restart_workers = restart_workers

    loop(
        lit_api,
        device,
        worker_id,
        request_queue,
        transport,
        workers_setup_status,
        callback_runner,
    )
```

## File: `src/litserve/loops/simple_loops.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import logging
import time
from queue import Empty, Queue
from typing import Optional

from fastapi import HTTPException

from litserve import LitAPI
from litserve.callbacks import CallbackRunner, EventTypes
from litserve.loops.base import _SENTINEL_VALUE, DefaultLoop, _async_inject_context, _inject_context, _StopLoopError
from litserve.specs.base import LitSpec
from litserve.transport.base import MessageTransport
from litserve.utils import LitAPIStatus, LoopResponseType, PickleableHTTPException

logger = logging.getLogger(__name__)


class SingleLoop(DefaultLoop):
    def run_single_loop(
        self,
        lit_api: LitAPI,
        request_queue: Queue,
        transport: MessageTransport,
        callback_runner: CallbackRunner,
        lit_spec: Optional[LitSpec] = None,
    ):
        lit_spec = lit_spec or lit_api.spec
        while True:
            try:
                request_data = request_queue.get(timeout=1.0)
                if request_data == _SENTINEL_VALUE:
                    logger.debug("Received sentinel value, stopping loop")
                    return

                response_queue_id, uid, timestamp, x_enc = request_data

                self.put_response(
                    transport=transport,
                    response_queue_id=response_queue_id,
                    uid=uid,
                    response_data=(),
                    status=LitAPIStatus.START,
                    response_type=LoopResponseType.REGULAR,
                )

            except (Empty, ValueError):
                continue
            except KeyboardInterrupt:  # pragma: no cover
                self.kill()
                return

            logger.debug(f"Received request {uid} from response_queue_id {response_queue_id}")

            if (lit_api.request_timeout and lit_api.request_timeout != -1) and (
                time.monotonic() - timestamp > lit_api.request_timeout
            ):
                logger.error(
                    f"Request {uid} was waiting in the queue for too long ({lit_api.request_timeout} seconds) and "
                    "has been timed out. "
                    "You can adjust the timeout by providing the `timeout` argument to LitServe(..., timeout=30)."
                )
                self.put_response(
                    transport=transport,
                    response_queue_id=response_queue_id,
                    uid=uid,
                    response_data=(HTTPException(504, "Request timed out")),
                    status=LitAPIStatus.ERROR,
                    response_type=LoopResponseType.REGULAR,
                )
                continue
            try:
                context = {}
                if hasattr(lit_spec, "populate_context"):
                    lit_spec.populate_context(context, x_enc)

                callback_runner.trigger_event(EventTypes.BEFORE_DECODE_REQUEST.value, lit_api=lit_api)
                x = _inject_context(
                    context,
                    lit_api.decode_request,
                    x_enc,
                )
                callback_runner.trigger_event(EventTypes.AFTER_DECODE_REQUEST.value, lit_api=lit_api)

                callback_runner.trigger_event(EventTypes.BEFORE_PREDICT.value, lit_api=lit_api)
                y = _inject_context(
                    context,
                    lit_api.predict,
                    x,
                )
                callback_runner.trigger_event(EventTypes.AFTER_PREDICT.value, lit_api=lit_api)

                callback_runner.trigger_event(EventTypes.BEFORE_ENCODE_RESPONSE.value, lit_api=lit_api)
                y_enc = _inject_context(
                    context,
                    lit_api.encode_response,
                    y,
                )
                callback_runner.trigger_event(EventTypes.AFTER_ENCODE_RESPONSE.value, lit_api=lit_api)
                self.put_response(
                    transport=transport,
                    response_queue_id=response_queue_id,
                    uid=uid,
                    response_data=y_enc,
                    status=LitAPIStatus.OK,
                    response_type=LoopResponseType.REGULAR,
                )

            except HTTPException as e:
                self.put_response(
                    transport=transport,
                    response_queue_id=response_queue_id,
                    uid=uid,
                    response_data=PickleableHTTPException.from_exception(e),
                    status=LitAPIStatus.ERROR,
                    response_type=LoopResponseType.REGULAR,
                )

            except Exception as e:
                logger.exception(
                    "LitAPI ran into an error while processing the request uid=%s.\n"
                    "Please check the error trace for more details.",
                    uid,
                )
                self.put_error_response(
                    transport=transport,
                    response_queue_id=response_queue_id,
                    uid=uid,
                    error=e,
                    response_type=LoopResponseType.REGULAR,
                )

    async def _process_single_request(
        self,
        request,
        lit_api: LitAPI,
        transport: MessageTransport,
        callback_runner: CallbackRunner,
        lit_spec: Optional[LitSpec] = None,
    ):
        lit_spec = lit_spec or lit_api.spec
        response_queue_id, uid, timestamp, x_enc = request
        try:
            context = {}
            if hasattr(lit_spec, "populate_context"):
                lit_spec.populate_context(context, x_enc)

            callback_runner.trigger_event(EventTypes.BEFORE_DECODE_REQUEST.value, lit_api=lit_api)
            x = await _async_inject_context(
                context,
                lit_api.decode_request,
                x_enc,
            )
            callback_runner.trigger_event(EventTypes.AFTER_DECODE_REQUEST.value, lit_api=lit_api)

            callback_runner.trigger_event(EventTypes.BEFORE_PREDICT.value, lit_api=lit_api)
            y = await _async_inject_context(
                context,
                lit_api.predict,
                x,
            )
            callback_runner.trigger_event(EventTypes.AFTER_PREDICT.value, lit_api=lit_api)

            callback_runner.trigger_event(EventTypes.BEFORE_ENCODE_RESPONSE.value, lit_api=lit_api)
            y_enc = await _async_inject_context(
                context,
                lit_api.encode_response,
                y,
            )
            callback_runner.trigger_event(EventTypes.AFTER_ENCODE_RESPONSE.value, lit_api=lit_api)
            self.put_response(
                transport=transport,
                response_queue_id=response_queue_id,
                uid=uid,
                response_data=y_enc,
                status=LitAPIStatus.OK,
                response_type=LoopResponseType.REGULAR,
            )

        except HTTPException as e:
            self.put_response(
                transport=transport,
                response_queue_id=response_queue_id,
                uid=uid,
                response_data=PickleableHTTPException.from_exception(e),
                status=LitAPIStatus.ERROR,
                response_type=LoopResponseType.REGULAR,
            )

        except Exception as e:
            logger.exception(
                "LitAPI ran into an error while processing the request uid=%s.\n"
                "Please check the error trace for more details.",
                uid,
            )
            self.put_error_response(
                transport=transport,
                response_queue_id=response_queue_id,
                uid=uid,
                error=e,
                response_type=LoopResponseType.REGULAR,
            )

    def _run_single_loop_with_async(
        self,
        lit_api: LitAPI,
        request_queue: Queue,
        transport: MessageTransport,
        callback_runner: CallbackRunner,
    ):
        async def process_requests():
            event_loop = asyncio.get_running_loop()
            pending_tasks = set()
            while True:
                try:
                    request_data = await event_loop.run_in_executor(None, request_queue.get, 1.0)

                    if request_data == _SENTINEL_VALUE:
                        logger.debug("Received sentinel value, stopping loop")
                        return

                    response_queue_id, uid, timestamp, x_enc = request_data

                    self.put_response(
                        transport=transport,
                        response_queue_id=response_queue_id,
                        uid=uid,
                        response_data=(),
                        status=LitAPIStatus.START,
                        response_type=LoopResponseType.REGULAR,
                    )
                except (Empty, ValueError):
                    continue
                except KeyboardInterrupt:
                    self.kill()
                    return

                if (lit_api.request_timeout and lit_api.request_timeout != -1) and (
                    time.monotonic() - timestamp > lit_api.request_timeout
                ):
                    logger.error(
                        f"Request {uid} was waiting in the queue for too long ({lit_api.request_timeout} seconds) and "
                        "has been timed out."
                    )
                    self.put_response(
                        transport=transport,
                        response_queue_id=response_queue_id,
                        uid=uid,
                        response_data=(HTTPException(504, "Request timed out")),
                        status=LitAPIStatus.ERROR,
                        response_type=LoopResponseType.REGULAR,
                    )
                    continue

                # Process the incoming request asynchronously to enable concurrent execution
                # of multiple requests
                task = asyncio.create_task(
                    self._process_single_request(
                        (response_queue_id, uid, timestamp, x_enc),
                        lit_api,
                        transport,
                        callback_runner,
                    ),
                    name=f"process_request_{uid}",
                )
                # Save a reference to the task's result to prevent it from being
                # garbage-collected during execution.
                pending_tasks.add(task)
                task.add_done_callback(pending_tasks.discard)

        # Get the current event loop
        loop = asyncio.new_event_loop()

        # Run the async process
        try:
            loop.run_until_complete(process_requests())
        except KeyboardInterrupt:
            self.kill()

    def __call__(
        self,
        lit_api: LitAPI,
        device: str,
        worker_id: int,
        request_queue: Queue,
        transport: MessageTransport,
        workers_setup_status: dict[int, str],
        callback_runner: CallbackRunner,
        lit_spec: Optional[LitSpec] = None,
        stream: bool = False,
    ):
        if lit_api.enable_async:
            self._run_single_loop_with_async(lit_api, request_queue, transport, callback_runner)
        else:
            self.run_single_loop(lit_api, request_queue, transport, callback_runner)


class BatchedLoop(DefaultLoop):
    def run_batched_loop(
        self,
        lit_api: LitAPI,
        request_queue: Queue,
        transport: MessageTransport,
        callback_runner: CallbackRunner,
        lit_spec: Optional[LitSpec] = None,
    ):
        lit_spec = lit_api.spec
        while True:
            try:
                batches, timed_out_uids = self.get_batch_requests(
                    lit_api,
                    request_queue,
                    transport,
                )
            except _StopLoopError:
                logger.debug("Received sentinel value, stopping loop")
                return

            for response_queue_id, uid in timed_out_uids:
                logger.error(
                    f"Request {uid} was waiting in the queue for too long ({lit_api.request_timeout} seconds) and "
                    "has been timed out. "
                    "You can adjust the timeout by providing the `timeout` argument to LitServe(..., timeout=30)."
                )
                self.put_response(
                    transport,
                    response_queue_id,
                    uid,
                    HTTPException(504, "Request timed out"),
                    LitAPIStatus.ERROR,
                    LoopResponseType.REGULAR,
                )

            if not batches:
                continue
            logger.debug(f"{len(batches)} batched requests received")
            response_queue_ids, uids, inputs = zip(*batches)
            num_inputs = len(inputs)
            try:
                contexts = [{} for _ in range(num_inputs)]
                if hasattr(lit_spec, "populate_context"):
                    for input, context in zip(inputs, contexts):
                        lit_spec.populate_context(context, input)

                callback_runner.trigger_event(EventTypes.BEFORE_DECODE_REQUEST.value, lit_api=lit_api)
                x = [
                    _inject_context(
                        context,
                        lit_api.decode_request,
                        input,
                    )
                    for input, context in zip(inputs, contexts)
                ]
                callback_runner.trigger_event(EventTypes.AFTER_DECODE_REQUEST.value, lit_api=lit_api)

                x = lit_api.batch(x)

                callback_runner.trigger_event(EventTypes.BEFORE_PREDICT.value, lit_api=lit_api)
                y = _inject_context(contexts, lit_api.predict, x)
                callback_runner.trigger_event(EventTypes.AFTER_PREDICT.value, lit_api=lit_api)

                outputs = lit_api.unbatch(y)

                if len(outputs) != num_inputs:
                    actual = len(outputs)
                    logger.error(
                        f"LitAPI.predict/unbatch returned {actual} outputs, but expected {num_inputs}. "
                        "This suggests a possible issue in the predict or unbatch implementation.\n"
                        "Hint: Ensure that LitAPI.predict returns a list with one prediction per input — "
                        "the length of the returned list should match the number of inputs."
                    )
                    raise HTTPException(500, detail="Batch size mismatch")

                callback_runner.trigger_event(EventTypes.BEFORE_ENCODE_RESPONSE.value, lit_api=lit_api)
                y_enc_list = []
                for response_queue_id, y, uid, context in zip(response_queue_ids, outputs, uids, contexts):
                    y_enc = _inject_context(context, lit_api.encode_response, y)
                    y_enc_list.append((response_queue_id, uid, y_enc))
                callback_runner.trigger_event(EventTypes.AFTER_ENCODE_RESPONSE.value, lit_api=lit_api)

                for response_queue_id, uid, y_enc in y_enc_list:
                    self.put_response(
                        transport, response_queue_id, uid, y_enc, LitAPIStatus.OK, LoopResponseType.REGULAR
                    )

            except HTTPException as e:
                for response_queue_id, uid in zip(response_queue_ids, uids):
                    self.put_response(
                        transport,
                        response_queue_id,
                        uid,
                        PickleableHTTPException.from_exception(e),
                        LitAPIStatus.ERROR,
                        LoopResponseType.REGULAR,
                    )
            except KeyboardInterrupt:  # pragma: no cover
                self.kill()
                return
            except Exception as e:
                logger.exception(
                    "LitAPI ran into an error while processing the batched request.\n"
                    "Please check the error trace for more details."
                )
                for response_queue_id, uid in zip(response_queue_ids, uids):
                    self.put_error_response(transport, response_queue_id, uid, e, LoopResponseType.REGULAR)

    def __call__(
        self,
        lit_api: LitAPI,
        device: str,
        worker_id: int,
        request_queue: Queue,
        transport: MessageTransport,
        workers_setup_status: dict[int, str],
        callback_runner: CallbackRunner,
        lit_spec: Optional[LitSpec] = None,
        stream: bool = False,
    ):
        self.run_batched_loop(
            lit_api,
            request_queue,
            transport,
            callback_runner,
        )
```

## File: `src/litserve/loops/streaming_loops.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import logging
import time
from queue import Empty, Queue
from typing import Optional

from fastapi import HTTPException

from litserve import LitAPI
from litserve.callbacks import CallbackRunner, EventTypes
from litserve.loops.base import _SENTINEL_VALUE, DefaultLoop, _async_inject_context, _inject_context, collate_requests
from litserve.specs.base import LitSpec
from litserve.transport.base import MessageTransport
from litserve.utils import LitAPIStatus, LoopResponseType, PickleableHTTPException

logger = logging.getLogger(__name__)


class StreamingLoop(DefaultLoop):
    def run_streaming_loop(
        self,
        lit_api: LitAPI,
        request_queue: Queue,
        transport: MessageTransport,
        callback_runner: CallbackRunner,
        lit_spec: Optional[LitSpec] = None,
    ):
        lit_spec = lit_api.spec
        while True:
            try:
                request_data = request_queue.get(timeout=1.0)
                if request_data == _SENTINEL_VALUE:
                    logger.debug("Received sentinel value, stopping loop")
                    return
                response_queue_id, uid, timestamp, x_enc = request_data

                self.put_response(
                    transport=transport,
                    response_queue_id=response_queue_id,
                    uid=uid,
                    response_data=(),
                    status=LitAPIStatus.START,
                    response_type=LoopResponseType.STREAMING,
                )

                logger.debug("uid=%s", uid)
            except (Empty, ValueError):
                continue

            if (lit_api.request_timeout and lit_api.request_timeout != -1) and (
                time.monotonic() - timestamp > lit_api.request_timeout
            ):
                logger.error(
                    f"Request {uid} was waiting in the queue for too long ({lit_api.request_timeout} seconds) and "
                    "has been timed out. "
                    "You can adjust the timeout by providing the `timeout` argument to LitServe(..., timeout=30)."
                )
                self.put_response(
                    transport,
                    response_queue_id,
                    uid,
                    HTTPException(504, "Request timed out"),
                    LitAPIStatus.ERROR,
                    LoopResponseType.STREAMING,
                )
                continue

            try:
                context = {}
                if hasattr(lit_spec, "populate_context"):
                    lit_spec.populate_context(context, x_enc)
                x = _inject_context(
                    context,
                    lit_api.decode_request,
                    x_enc,
                )

                callback_runner.trigger_event(EventTypes.BEFORE_PREDICT.value, lit_api=lit_api)
                y_gen = _inject_context(
                    context,
                    lit_api.predict,
                    x,
                )
                callback_runner.trigger_event(EventTypes.AFTER_PREDICT.value, lit_api=lit_api)

                callback_runner.trigger_event(EventTypes.BEFORE_ENCODE_RESPONSE.value, lit_api=lit_api)
                y_enc_gen = _inject_context(
                    context,
                    lit_api.encode_response,
                    y_gen,
                )
                for y_enc in y_enc_gen:
                    y_enc = lit_api.format_encoded_response(y_enc)
                    self.put_response(
                        transport, response_queue_id, uid, y_enc, LitAPIStatus.OK, LoopResponseType.STREAMING
                    )
                self.put_response(
                    transport, response_queue_id, uid, "", LitAPIStatus.FINISH_STREAMING, LoopResponseType.STREAMING
                )

                callback_runner.trigger_event(EventTypes.AFTER_PREDICT.value, lit_api=lit_api)
                callback_runner.trigger_event(EventTypes.AFTER_ENCODE_RESPONSE.value, lit_api=lit_api)

            except HTTPException as e:
                self.put_response(
                    transport,
                    response_queue_id,
                    uid,
                    PickleableHTTPException.from_exception(e),
                    LitAPIStatus.ERROR,
                    LoopResponseType.STREAMING,
                )
            except KeyboardInterrupt:  # pragma: no cover
                self.kill()
                return
            except Exception as e:
                logger.exception(
                    "LitAPI ran into an error while processing the streaming request uid=%s.\n"
                    "Please check the error trace for more details.",
                    uid,
                )
                self.put_error_response(transport, response_queue_id, uid, e, LoopResponseType.STREAMING)

    async def _process_streaming_request(
        self,
        request,
        lit_api: LitAPI,
        transport: MessageTransport,
        callback_runner: CallbackRunner,
        lit_spec: Optional[LitSpec] = None,
    ):
        lit_spec = lit_api.spec
        response_queue_id, uid, timestamp, x_enc = request
        try:
            context = {}
            if hasattr(lit_spec, "populate_context"):
                lit_spec.populate_context(context, x_enc)

            callback_runner.trigger_event(EventTypes.BEFORE_DECODE_REQUEST.value, lit_api=lit_api)
            x = await _async_inject_context(
                context,
                lit_api.decode_request,
                x_enc,
            )
            callback_runner.trigger_event(EventTypes.AFTER_DECODE_REQUEST.value, lit_api=lit_api)

            callback_runner.trigger_event(EventTypes.BEFORE_PREDICT.value, lit_api=lit_api)
            y_gen = await _async_inject_context(
                context,
                lit_api.predict,
                x,
            )
            callback_runner.trigger_event(EventTypes.AFTER_PREDICT.value, lit_api=lit_api)

            callback_runner.trigger_event(EventTypes.BEFORE_ENCODE_RESPONSE.value, lit_api=lit_api)

            # When using async, predict should return an async generator
            # and encode_response should handle async generators
            # The _async_inject_context already handles async generators correctly
            enc_result = await _async_inject_context(
                context,
                lit_api.encode_response,
                y_gen,
            )

            # encode_response should also return an async generator
            async for y_enc in enc_result:
                y_enc = lit_api.format_encoded_response(y_enc)
                self.put_response(transport, response_queue_id, uid, y_enc, LitAPIStatus.OK, LoopResponseType.STREAMING)

            self.put_response(
                transport, response_queue_id, uid, "", LitAPIStatus.FINISH_STREAMING, LoopResponseType.STREAMING
            )
            callback_runner.trigger_event(EventTypes.AFTER_ENCODE_RESPONSE.value, lit_api=lit_api)

        except HTTPException as e:
            self.put_response(
                transport=transport,
                response_queue_id=response_queue_id,
                uid=uid,
                response_data=PickleableHTTPException.from_exception(e),
                status=LitAPIStatus.ERROR,
                response_type=LoopResponseType.STREAMING,
            )
        except Exception as e:
            logger.exception(
                "LitAPI ran into an error while processing the streaming request uid=%s.\n"
                "Please check the error trace for more details.",
                uid,
            )
            self.put_error_response(transport, response_queue_id, uid, e, LoopResponseType.STREAMING)

    def run_streaming_loop_async(
        self,
        lit_api: LitAPI,
        request_queue: Queue,
        transport: MessageTransport,
        callback_runner: CallbackRunner,
    ):
        if lit_api.spec:
            # wrap the default implementation of the spec in an async spec wrapper
            lit_api.spec = lit_api.spec.as_async()

        async def process_requests():
            event_loop = asyncio.get_running_loop()
            pending_tasks = set()

            while True:
                try:
                    request_data = await event_loop.run_in_executor(None, request_queue.get, 1.0)

                    if request_data == _SENTINEL_VALUE:
                        logger.debug("Received sentinel value, stopping loop")
                        return

                    response_queue_id, uid, timestamp, x_enc = request_data

                    self.put_response(
                        transport=transport,
                        response_queue_id=response_queue_id,
                        uid=uid,
                        response_data=(),
                        status=LitAPIStatus.START,
                        response_type=LoopResponseType.STREAMING,
                    )

                    logger.debug("uid=%s", uid)
                except (Empty, ValueError):
                    continue

                if (lit_api.request_timeout and lit_api.request_timeout != -1) and (
                    time.monotonic() - timestamp > lit_api.request_timeout
                ):
                    logger.error(
                        f"Request {uid} was waiting in the queue for too long ({lit_api.request_timeout} seconds) and "
                        "has been timed out. "
                        "You can adjust the timeout by providing the `timeout` argument to LitServe(..., timeout=30)."
                    )
                    self.put_response(
                        transport,
                        response_queue_id,
                        uid,
                        HTTPException(504, "Request timed out"),
                        LitAPIStatus.ERROR,
                        LoopResponseType.STREAMING,
                    )
                    continue

                task = asyncio.create_task(
                    self._process_streaming_request(
                        (response_queue_id, uid, timestamp, x_enc),
                        lit_api,
                        transport,
                        callback_runner,
                    ),
                    name=f"streaming_request_{uid}",
                )
                pending_tasks.add(task)
                task.add_done_callback(pending_tasks.discard)

        loop = asyncio.new_event_loop()

        try:
            loop.run_until_complete(process_requests())
        except KeyboardInterrupt:
            self.kill()

    def __call__(
        self,
        lit_api: LitAPI,
        device: str,
        worker_id: int,
        request_queue: Queue,
        transport: MessageTransport,
        workers_setup_status: dict[int, str],
        callback_runner: CallbackRunner,
    ):
        if lit_api.enable_async:
            self.run_streaming_loop_async(lit_api, request_queue, transport, callback_runner)
        else:
            self.run_streaming_loop(lit_api, request_queue, transport, callback_runner)


class BatchedStreamingLoop(DefaultLoop):
    def run_batched_streaming_loop(
        self,
        lit_api: LitAPI,
        request_queue: Queue,
        transport: MessageTransport,
        callback_runner: CallbackRunner,
        lit_spec: Optional[LitSpec] = None,
    ):
        lit_spec = lit_api.spec
        while True:
            batches, timed_out_uids = collate_requests(
                loop=self,
                lit_api=lit_api,
                request_queue=request_queue,
                transport=transport,
            )
            for response_queue_id, uid in timed_out_uids:
                logger.error(
                    f"Request {uid} was waiting in the queue for too long ({lit_api.request_timeout} seconds) and "
                    "has been timed out. "
                    "You can adjust the timeout by providing the `timeout` argument to LitServe(..., timeout=30)."
                )
                self.put_response(
                    transport,
                    response_queue_id,
                    uid,
                    HTTPException(504, "Request timed out"),
                    LitAPIStatus.ERROR,
                    LoopResponseType.STREAMING,
                )

            if not batches:
                continue
            response_queue_ids, uids, inputs = zip(*batches)
            num_inputs = len(inputs)
            try:
                contexts = [{} for _ in range(num_inputs)]
                if hasattr(lit_spec, "populate_context"):
                    for input, context in zip(inputs, contexts):
                        lit_spec.populate_context(context, input)

                callback_runner.trigger_event(EventTypes.BEFORE_DECODE_REQUEST.value, lit_api=lit_api)
                x = [
                    _inject_context(
                        context,
                        lit_api.decode_request,
                        input,
                    )
                    for input, context in zip(inputs, contexts)
                ]
                callback_runner.trigger_event(EventTypes.AFTER_DECODE_REQUEST.value, lit_api=lit_api)

                x = lit_api.batch(x)

                callback_runner.trigger_event(EventTypes.BEFORE_PREDICT.value, lit_api=lit_api)
                y_iter = _inject_context(contexts, lit_api.predict, x)
                callback_runner.trigger_event(EventTypes.AFTER_PREDICT.value, lit_api=lit_api)

                unbatched_iter = lit_api.unbatch(y_iter)

                callback_runner.trigger_event(EventTypes.BEFORE_ENCODE_RESPONSE.value, lit_api=lit_api)
                y_enc_iter = _inject_context(contexts, lit_api.encode_response, unbatched_iter)
                callback_runner.trigger_event(EventTypes.AFTER_ENCODE_RESPONSE.value, lit_api=lit_api)

                # y_enc_iter -> [[response-1, response-2], [response-1, response-2]]
                for y_batch in y_enc_iter:
                    for response_queue_id, y_enc, uid in zip(response_queue_ids, y_batch, uids):
                        y_enc = lit_api.format_encoded_response(y_enc)
                        self.put_response(
                            transport, response_queue_id, uid, y_enc, LitAPIStatus.OK, LoopResponseType.STREAMING
                        )

                for response_queue_id, uid in zip(response_queue_ids, uids):
                    self.put_response(
                        transport, response_queue_id, uid, "", LitAPIStatus.FINISH_STREAMING, LoopResponseType.STREAMING
                    )
            except KeyboardInterrupt:  # pragma: no cover
                self.kill()
                return

            except HTTPException as e:
                for response_queue_id, uid in zip(response_queue_ids, uids):
                    self.put_response(
                        transport,
                        response_queue_id,
                        uid,
                        PickleableHTTPException.from_exception(e),
                        LitAPIStatus.ERROR,
                        LoopResponseType.STREAMING,
                    )

            except Exception as e:
                logger.exception(
                    "LitAPI ran into an error while processing the streaming batched request.\n"
                    "Please check the error trace for more details."
                )
                for response_queue_id, uid in zip(response_queue_ids, uids):
                    self.put_error_response(transport, response_queue_id, uid, e, LoopResponseType.STREAMING)

    def __call__(
        self,
        lit_api: LitAPI,
        device: str,
        worker_id: int,
        request_queue: Queue,
        transport: MessageTransport,
        workers_setup_status: dict[int, str],
        callback_runner: CallbackRunner,
    ):
        self.run_batched_streaming_loop(
            lit_api,
            request_queue,
            transport,
            callback_runner,
        )
```

## File: `src/litserve/schema/image.py`
```python
import base64
from io import BytesIO
from typing import TYPE_CHECKING, Any, Optional

from pydantic import BaseModel, field_serializer, model_validator

if TYPE_CHECKING:
    from PIL import Image


class ImageInput(BaseModel):
    image_data: Optional[str] = None

    @model_validator(mode="after")
    def validate_base64(self) -> "ImageInput":
        """Ensure the string is a valid Base64."""
        model_dump = self.model_dump()
        for key, value in model_dump.items():
            if value:
                try:
                    base64.b64decode(value)
                except base64.binascii.Error:
                    raise ValueError("Invalid Base64 string.")
        return self

    def get_image(self, key: Optional[str] = None) -> "Image.Image":
        """Decode the Base64 string and return a PIL Image object."""
        if key is None:
            key = "image_data"
        image_data = self.model_dump().get(key)
        if not image_data:
            raise ValueError(f"Missing image data for key '{key}'")
        try:
            from PIL import Image, UnidentifiedImageError
        except ImportError:
            raise ImportError("Pillow is required to use the ImageInput schema. Install it with `pip install Pillow`.")
        try:
            decoded_data = base64.b64decode(image_data)
            return Image.open(BytesIO(decoded_data))
        except UnidentifiedImageError as e:
            raise ValueError(f"Error loading image from decoded data: {e}")


class ImageOutput(BaseModel):
    image: Any

    @field_serializer("image")
    def serialize_image(self, image: Any, _info):
        """
        Serialize a PIL Image into a base64 string.
        Args:
            image (Any): The image object to serialize.
            _info: Metadata passed during serialization (not used here).

        Returns:
            str: Base64-encoded image string.
        """
        try:
            from PIL import Image
        except ImportError:
            raise ImportError("Pillow is required to use the ImageOutput schema. Install it with `pip install Pillow`.")

        if not isinstance(image, Image.Image):
            raise TypeError(f"Expected a PIL Image, got {type(image)}")

        # Save the image to a BytesIO buffer
        buffer = BytesIO()
        image.save(buffer, format="PNG")  # Default format is PNG
        buffer.seek(0)

        # Encode the buffer content to base64
        base64_bytes = base64.b64encode(buffer.read())

        # Decode to string for JSON serialization
        return base64_bytes.decode("utf-8")
```

## File: `src/litserve/specs/__init__.py`
```python
from litserve.specs.openai import ChatCompletionChunk, ChatCompletionRequest, ChatCompletionResponse, OpenAISpec
from litserve.specs.openai_embedding import EmbeddingRequest, EmbeddingResponse, OpenAIEmbeddingSpec

__all__ = [
    "OpenAISpec",
    "OpenAIEmbeddingSpec",
    "EmbeddingRequest",
    "EmbeddingResponse",
    "ChatCompletionRequest",
    "ChatCompletionResponse",
    "ChatCompletionChunk",
]
```

## File: `src/litserve/specs/base.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from abc import abstractmethod
from collections.abc import AsyncGenerator, Callable, Generator
from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from litserve import LitAPI, LitServer


class LitSpec:
    """Spec will have its own encode, and decode."""

    def __init__(self):
        self._endpoints = []
        self.api_path = None
        self._server: LitServer = None
        self._max_batch_size = 1
        self.response_buffer = None
        self.request_queue = None
        self.response_queue_id = None

    def __getstate__(self):
        """Exclude _server from pickling as it contains unpickleable objects."""
        state = self.__dict__.copy()
        state["_server"] = None
        return state

    @property
    def stream(self):
        return False

    def pre_setup(self, lit_api: "LitAPI"):
        pass

    def setup(self, server: "LitServer"):
        """This method is called by the server to connect the spec to the server."""
        self.response_buffer = server.response_buffer
        self.request_queue = server._get_request_queue(self.api_path)
        self.data_streamer = server.data_streamer

    def add_endpoint(self, path: str, endpoint: Callable, methods: list[str]):
        """Register an endpoint in the spec."""
        self._endpoints.append((path, endpoint, methods))

    @property
    def endpoints(self):
        return self._endpoints.copy()

    @abstractmethod
    def decode_request(self, request, context_kwargs) -> Any:
        """Convert the request payload to your model input."""
        pass

    @abstractmethod
    def encode_response(self, output, context_kwargs) -> Any:
        """Convert the model output to a response payload.

        To enable streaming, it should yield the output.

        """
        pass

    def as_async(self) -> "_AsyncSpecWrapper":
        return _AsyncSpecWrapper(self)


class _AsyncSpecWrapper:
    def __init__(self, spec: LitSpec):
        self._spec = spec

    def __getattr__(self, name):
        # Delegate all other attributes/methods to the wrapped spec
        return getattr(self._spec, name)

    async def decode_request(self, request, context_kwargs: Optional[dict] = None):
        return self._spec.decode_request(request, context_kwargs)

    async def encode_response(self, output: Union[Generator, AsyncGenerator], context_kwargs: Optional[dict] = None):
        return self._spec.encode_response(output, context_kwargs)
```

## File: `src/litserve/specs/openai.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import inspect
import json
import logging
import time
import typing
import uuid
import warnings
from collections import deque
from collections.abc import AsyncGenerator, Iterator
from enum import Enum
from typing import Annotated, Literal, Optional, Union

from fastapi import BackgroundTasks, HTTPException, Request, Response
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from litserve.callbacks.base import EventTypes
from litserve.constants import _DEFAULT_LIT_API_PATH
from litserve.specs.base import LitSpec, _AsyncSpecWrapper
from litserve.utils import LitAPIStatus, ResponseBufferItem, azip

if typing.TYPE_CHECKING:
    from litserve import LitAPI, LitServer

logger = logging.getLogger(__name__)


def shortuuid():
    return uuid.uuid4().hex[:6]


class UsageInfo(BaseModel):
    prompt_tokens: int = 0
    total_tokens: int = 0
    completion_tokens: Optional[int] = 0

    def __add__(self, other: "UsageInfo") -> "UsageInfo":
        other.prompt_tokens += self.prompt_tokens
        other.completion_tokens += self.completion_tokens
        other.total_tokens += self.total_tokens
        return other

    def __radd__(self, other):
        if other == 0:
            return self
        return self.__add__(other)


class TextContent(BaseModel):
    type: str
    text: str


class ImageDetail(str, Enum):
    auto: str = "auto"
    low: str = "low"
    high: str = "high"


class ImageContentURL(BaseModel):
    url: str
    detail: ImageDetail = ImageDetail.auto


class ImageContent(BaseModel):
    type: str
    image_url: Union[str, ImageContentURL]


class InputAudio(BaseModel):
    data: str  # base64 encoded audio data.
    format: Literal["wav", "mp3"]


class AudioContent(BaseModel):
    type: Literal["input_audio"]
    input_audio: InputAudio


class Function(BaseModel):
    name: str
    description: str
    parameters: dict[str, object]


class ToolChoice(str, Enum):
    auto: str = "auto"
    none: str = "none"
    any: str = "any"


class Tool(BaseModel):
    type: Literal["function"]
    function: Function


class FunctionCall(BaseModel):
    name: str
    arguments: str


class ToolCall(BaseModel):
    index: int = 0
    id: Optional[str] = None
    type: str = "function"
    function: FunctionCall


class ResponseFormatText(BaseModel):
    type: Literal["text"]


class ResponseFormatJSONObject(BaseModel):
    type: Literal["json_object"]


class JSONSchema(BaseModel):
    name: str
    description: Optional[str] = None
    schema_: Optional[dict[str, object]] = Field(None, alias="schema")
    strict: Optional[bool] = False


class ResponseFormatJSONSchema(BaseModel):
    json_schema: JSONSchema
    type: Literal["json_schema"]


ResponseFormat = Annotated[
    Union[ResponseFormatText, ResponseFormatJSONObject, ResponseFormatJSONSchema], "ResponseFormat"
]


class ChatMessage(BaseModel):
    role: str
    content: Optional[Union[str, list[Union[TextContent, ImageContent, AudioContent]]]] = None
    name: Optional[str] = None
    tool_calls: Optional[list[ToolCall]] = None
    tool_call_id: Optional[str] = None


class ChatMessageWithUsage(ChatMessage):
    prompt_tokens: Optional[int] = 0
    total_tokens: Optional[int] = 0
    completion_tokens: Optional[int] = 0


class ChoiceDelta(ChatMessage):
    content: Optional[str] = None
    role: Optional[Literal["system", "user", "assistant", "tool"]] = None


class ChatCompletionRequest(BaseModel):
    model: Optional[str] = ""
    messages: list[ChatMessage]
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 1.0
    n: Optional[int] = 1
    max_tokens: Optional[int] = None  # Kept for backward compatibility
    max_completion_tokens: Optional[int] = None
    stop: Optional[Union[str, list[str]]] = None
    stream: Optional[bool] = False
    presence_penalty: Optional[float] = 0.0
    frequency_penalty: Optional[float] = 0.0
    user: Optional[str] = None
    tools: Optional[list[Tool]] = None
    tool_choice: Optional[ToolChoice] = ToolChoice.auto
    response_format: Optional[ResponseFormat] = None
    reasoning_effort: Optional[Literal["low", "medium", "high"]] = None
    metadata: Optional[dict[str, str]] = None


class ChatCompletionResponseChoice(BaseModel):
    index: int
    message: ChatMessage
    finish_reason: Optional[Literal["stop", "length"]]


class ChatCompletionResponse(BaseModel):
    id: str = Field(default_factory=lambda: f"chatcmpl-{shortuuid()}")
    object: str = "chat.completion"
    created: int = Field(default_factory=lambda: int(time.time()))
    model: str
    choices: list[ChatCompletionResponseChoice]
    usage: UsageInfo


class ChatCompletionStreamingChoice(BaseModel):
    delta: Optional[ChoiceDelta]
    finish_reason: Optional[Literal["stop", "length", "tool_calls", "content_filter", "function_call"]] = None
    index: int
    logprobs: Optional[dict] = None


class ChatCompletionChunk(BaseModel):
    id: str = Field(default_factory=lambda: f"chatcmpl-{shortuuid()}")
    object: str = "chat.completion.chunk"
    created: int = Field(default_factory=lambda: int(time.time()))
    model: str
    system_fingerprint: Optional[str] = None
    choices: list[ChatCompletionStreamingChoice]
    usage: Optional[UsageInfo]


LITAPI_VALIDATION_MSG = """LitAPI.predict and LitAPI.encode_response must be a generator (use yield instead or return)
while using the OpenAISpec.

Error: {}

Please follow the below examples for guidance on how to use the spec:

If your current code looks like this:

```
import litserve as ls
from litserve.specs.openai import ChatMessage

class ExampleAPI(ls.LitAPI):
    ...
    def predict(self, x):
        return "This is a generated output"

    def encode_response(self, output: dict):
        return ChatMessage(role="assistant", content="This is a custom encoded output")
```

You should modify it to:

```
import litserve as ls
from litserve.specs.openai import ChatMessage

class ExampleAPI(ls.LitAPI):
    ...
    def predict(self, x):
        yield "This is a generated output"

    def encode_response(self, output):
        yield ChatMessage(role="assistant", content="This is a custom encoded output")
```


You can also yield responses in chunks. LitServe will handle the streaming for you:

```
class ExampleAPI(ls.LitAPI):
    ...
    def predict(self, x):
        yield from self.model(x)

    def encode_response(self, output):
        for out in output:
            yield ChatMessage(role="assistant", content=out)
```
"""

ASYNC_LITAPI_VALIDATION_MSG = """Error: {}

`enable_async` is set but LitAPI method is not async. To use async with OpenAISpec, you need to make the following changes:

- LitAPI.decode_request can be a regular function or an async function.
- LitAPI.predict must be an async generator (use 'yield' or 'yield from' inside an 'async def' function).
- LitAPI.encode_response can be a regular function or an async generator.


Please follow the examples below for guidance on how to use the spec in async mode:

If your current code looks like this:

```
import litserve as ls
from litserve.specs.openai import ChatMessage

class ExampleAPI(ls.LitAPI):
    ...
    def predict(self, x):
        return "This is a generated output"

    def encode_response(self, output: dict):
        return ChatMessage(role="assistant", content="This is a custom encoded output")
```
You should modify it to:

```
import litserve as ls
from litserve.specs.openai import ChatMessage

class ExampleAPI(ls.LitAPI):
    ...
    async def decode_request(self, request):
        # process request here
        return request.messages

    async def predict(self, x):
        yield "This is a generated output"

    async def encode_response(self, output):
        yield ChatMessage(role="assistant", content="This is a custom encoded output")
```
You can also yield responses in chunks. LitServe will handle the streaming for you:

```
class ExampleAPI(ls.LitAPI):
    ...
    async def decode_request(self, request):
        # process request here
        return request.messages

    async def predict(self, x):
        async for out in self.model(x):
            yield out

    async def encode_response(self, output):
        async for out in output:
            yield ChatMessage(role="assistant", content=out)
```
"""  # noqa: E501


def _openai_format_error(error: Exception):
    if isinstance(error, HTTPException):
        return "data: " + json.dumps(
            {
                "error": {
                    "message": error.detail,
                    "type": "internal",
                    "param": None,
                    "code": "internal_error",
                }
            }
        )
    return "data: " + json.dumps(
        {
            "error": {
                "message": "Internal server error",
                "type": "internal",
                "param": None,
                "code": "internal_error",
            }
        }
    )


class OpenAISpec(LitSpec):
    def __init__(
        self,
    ):
        super().__init__()
        self.api_path = "/v1/chat/completions"  # default api path

    @property
    def stream(self):
        return True

    def pre_setup(self, lit_api: "LitAPI"):
        from litserve import LitAPI

        # Override the spec's api_path only if provided
        if lit_api._api_path and lit_api._api_path not in (_DEFAULT_LIT_API_PATH, self.api_path):
            self.api_path = lit_api._api_path
            warnings.warn(
                f"Custom API path detected: '{self.api_path}'. "
                "The OpenAI SDK only supports the default path '/v1/chat/completions'. "
                f"To use '{self.api_path}', send HTTP requests directly or use a client that supports custom endpoints."
                " For SDK compatibility, use the default path."
            )

        # register the endpoint
        self.add_endpoint(self.api_path, self.chat_completion, ["POST"])
        self.add_endpoint(self.api_path, self.options_chat_completions, ["OPTIONS"])

        # validate LitAPI methods
        is_encode_response_original = lit_api.encode_response.__code__ is LitAPI.encode_response.__code__

        if lit_api.enable_async:
            # warning for decode_request and encode_response
            if not asyncio.iscoroutinefunction(lit_api.decode_request):
                logger.info("decode_request is not a coroutine function. LitServe will asyncify it.")
            if not inspect.isasyncgenfunction(lit_api.encode_response):
                logger.info("encode_response is not an async generator. LitServe will asyncify it.")

            if not inspect.isasyncgenfunction(lit_api.predict):
                raise ValueError(ASYNC_LITAPI_VALIDATION_MSG.format("predict must be an async generator"))

            if (
                not is_encode_response_original
                and not inspect.isgeneratorfunction(lit_api.encode_response)
                and not inspect.isasyncgenfunction(lit_api.encode_response)
            ):
                raise ValueError(
                    ASYNC_LITAPI_VALIDATION_MSG.format("encode_response is neither a generator nor an async generator")
                )

        else:
            for method in ["decode_request", "predict", "encode_response"]:
                method_obj = getattr(lit_api, method)
                if asyncio.iscoroutinefunction(method_obj) or inspect.isasyncgenfunction(method_obj):
                    raise ValueError(
                        f"'{method}' is defined as async/coroutine, but 'enable_async' is not set in LitAPI. "
                        "Please set 'enable_async=True' in your LitAPI class or "
                        "use synchronous (non-async) methods instead."
                    )

            if not inspect.isgeneratorfunction(lit_api.predict):
                raise ValueError(LITAPI_VALIDATION_MSG.format("predict is not a generator"))

            if not is_encode_response_original and not inspect.isgeneratorfunction(lit_api.encode_response):
                raise ValueError(LITAPI_VALIDATION_MSG.format("encode_response is not a generator"))

    def setup(self, server: "LitServer"):
        super().setup(server)
        print("OpenAI spec setup complete")

    def as_async(self) -> "_AsyncOpenAISpecWrapper":
        return _AsyncOpenAISpecWrapper(self)

    def populate_context(self, context, request):
        data = request.dict()
        data.pop("messages")
        context.update(data)

    def decode_request(
        self, request: ChatCompletionRequest, context_kwargs: Optional[dict] = None
    ) -> ChatCompletionRequest:
        return request

    def batch(self, inputs):
        return list(inputs)

    def unbatch(self, output):
        yield output

    def extract_usage_info(self, output: dict) -> dict:
        prompt_tokens: int = output.pop("prompt_tokens", 0)
        completion_tokens: int = output.pop("completion_tokens", 0)
        total_tokens: int = output.pop("total_tokens", 0)
        return {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total_tokens,
        }

    def validate_chat_message(self, obj):
        return isinstance(obj, dict) and "role" in obj and "content" in obj

    def _encode_response(self, output: Union[dict[str, str], list[dict[str, str]]]) -> dict:
        logger.debug(output)
        if output is None:
            message = {"role": "assistant", "content": None}
        elif isinstance(output, str):
            message = {"role": "assistant", "content": output}
        elif self.validate_chat_message(output):
            message = output
        elif isinstance(output, dict) and "content" in output:
            message = output.copy()
            message.update(role="assistant")
        elif isinstance(output, list) and output and self.validate_chat_message(output[-1]):
            message = output[-1]
        else:
            error = (
                "Malformed output from LitAPI.predict: expected "
                f"string or {{'role': '...', 'content': '...'}}, got '{output}'."
            )
            logger.error(error)
            raise HTTPException(500, error)
        usage_info = self.extract_usage_info(message)
        return {**message, **usage_info}

    def encode_response(
        self, output_generator: Union[dict[str, str], list[dict[str, str]]], context_kwargs: Optional[dict] = None
    ) -> Iterator[Union[ChatMessage, ChatMessageWithUsage]]:
        for output in output_generator:
            logger.debug(output)
            yield self._encode_response(output)

    async def get_from_queues(self, uids) -> list[AsyncGenerator]:
        choice_pipes = []
        for uid, q, event in zip(uids, self.queues, self.events):
            data = self.data_streamer(q, event, send_status=True)
            choice_pipes.append(data)
        return choice_pipes

    async def options_chat_completions(self, request: Request):
        return Response(status_code=200)

    async def chat_completion(self, request: ChatCompletionRequest, background_tasks: BackgroundTasks):
        response_queue_id = self.response_queue_id
        logger.debug("Received chat completion request %s", request)
        uids = [uuid.uuid4() for _ in range(request.n)]
        self.queues = []
        self.events = []

        # Trigger callback
        self._server._callback_runner.trigger_event(
            EventTypes.ON_REQUEST.value,
            active_requests=self._server.active_requests,
            litserver=self._server,
        )

        for uid in uids:
            request_el = request.model_copy()
            request_el.n = 1
            q = deque()
            event = asyncio.Event()
            self.response_buffer[uid] = ResponseBufferItem(response_queue=q, event=event)
            self.request_queue.put((response_queue_id, uid, time.monotonic(), request_el))
            self.queues.append(q)
            self.events.append(event)

        responses = await self.get_from_queues(uids)

        if request.stream:
            return StreamingResponse(
                self.streaming_completion(request, responses),
                media_type="text/event-stream",
                background=background_tasks,
            )

        response_task = asyncio.create_task(self.non_streaming_completion(request, responses))
        return await response_task

    async def streaming_completion(self, request: ChatCompletionRequest, pipe_responses: list):
        try:
            model = request.model
            usage_info = None
            async for streaming_response in azip(*pipe_responses):
                choices = []
                usage_infos = []
                # iterate over n choices
                for i, (response, status) in enumerate(streaming_response):
                    if status == LitAPIStatus.ERROR and isinstance(response, HTTPException):
                        raise response
                    elif status == LitAPIStatus.ERROR:
                        logger.error("Error in streaming response: %s", response)
                        raise HTTPException(status_code=500)
                    encoded_response = json.loads(response)
                    logger.debug(encoded_response)
                    chat_msg = ChoiceDelta(**encoded_response)
                    usage_infos.append(UsageInfo(**encoded_response))
                    choice = ChatCompletionStreamingChoice(
                        index=i, delta=chat_msg, system_fingerprint="", finish_reason=None
                    )

                    choices.append(choice)

                # Only use the last item from encode_response
                usage_info = sum(usage_infos)
                chunk = ChatCompletionChunk(model=model, choices=choices, usage=None)
                logger.debug(chunk)
                yield f"data: {chunk.model_dump_json(by_alias=True)}\n\n"

            choices = [
                ChatCompletionStreamingChoice(
                    index=i,
                    delta=ChoiceDelta(),
                    finish_reason="stop",
                )
                for i in range(request.n)
            ]
            last_chunk = ChatCompletionChunk(
                model=model,
                choices=choices,
                usage=usage_info,
            )
            yield f"data: {last_chunk.model_dump_json(by_alias=True)}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            logger.error("Error in streaming response: %s", e, exc_info=True)
            yield _openai_format_error(e)
            return

    async def non_streaming_completion(self, request: ChatCompletionRequest, generator_list: list[AsyncGenerator]):
        try:
            model = request.model
            usage_infos = []
            choices = []
            # iterate over n choices
            for i, streaming_response in enumerate(generator_list):
                msgs = []
                tool_calls = None
                usage = None
                async for response, status in streaming_response:
                    if status == LitAPIStatus.ERROR and isinstance(response, HTTPException):
                        raise response
                    if status == LitAPIStatus.ERROR:
                        logger.error("Error in OpenAI non-streaming response: %s", response)
                        raise HTTPException(status_code=500)

                    # data from LitAPI.encode_response
                    encoded_response = json.loads(response)
                    logger.debug(encoded_response)
                    chat_msg = ChatMessage(**encoded_response)
                    usage = UsageInfo(**encoded_response)
                    usage_infos.append(usage)  # Aggregate usage info across all choices
                    msgs.append(chat_msg.content)
                    if chat_msg.tool_calls:
                        tool_calls = chat_msg.tool_calls

                content = "".join(msg for msg in msgs if msg is not None)
                msg = {"role": "assistant", "content": content, "tool_calls": tool_calls}
                choice = ChatCompletionResponseChoice(index=i, message=msg, finish_reason="stop")
                choices.append(choice)

            return ChatCompletionResponse(model=model, choices=choices, usage=sum(usage_infos))
        except HTTPException as e:
            raise e
        except Exception as e:
            logger.error("Error in non-streaming response: %s", e, exc_info=True)
            raise HTTPException(status_code=500)


class _AsyncOpenAISpecWrapper(_AsyncSpecWrapper):
    async def encode_response(self, output_generator: AsyncGenerator, context_kwargs: Optional[dict] = None):
        async for output in output_generator:
            yield self._spec._encode_response(output)
```

## File: `src/litserve/specs/openai_embedding.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import inspect
import logging
import sys
import time
import uuid
import warnings
from typing import TYPE_CHECKING, Any, Literal, Optional, Union

from fastapi import HTTPException, Request, Response, status
from fastapi import status as status_code
from pydantic import BaseModel

from litserve.callbacks.base import EventTypes
from litserve.constants import _DEFAULT_LIT_API_PATH
from litserve.specs.base import LitSpec
from litserve.utils import LitAPIStatus, ResponseBufferItem

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    import numpy as np
    import torch

    from litserve import LitAPI, LitServer


class EmbeddingRequest(BaseModel):
    input: Union[str, list[str], list[int], list[list[int]]]
    model: str
    dimensions: Optional[int] = None
    encoding_format: Literal["float", "base64"] = "float"
    user: Optional[str] = None

    def get_num_items(self) -> int:
        """Return the number of sentences or tokens in the input."""
        if isinstance(self.input, list):
            if isinstance(self.input[0], list):
                return len(self.input[0])
            return len(self.input)
        return 1

    def ensure_list(self):
        return self.input if isinstance(self.input, list) else [self.input]


class Embedding(BaseModel):
    index: int
    embedding: list[float]
    object: Literal["embedding"] = "embedding"


class UsageInfo(BaseModel):
    prompt_tokens: int = 0
    total_tokens: int = 0


class EmbeddingResponse(BaseModel):
    data: list[Embedding]
    model: str
    object: Literal["list"] = "list"
    usage: UsageInfo


EMBEDDING_API_EXAMPLE = """
Please follow the example below for guidance on how to use the OpenAI Embedding spec:

```python
import numpy as np
from typing import List
from litserve.specs import OpenAIEmbeddingSpec, EmbeddingRequest
import litserve as ls

class TestAPI(ls.LitAPI):
    def setup(self, device):
        self.model = None

    def predict(self, inputs) -> list[list[float]]:
        # inputs is a string
        return np.random.rand(1, 768).tolist()


if __name__ == "__main__":
    server = ls.LitServer(TestAPI(), spec=OpenAIEmbeddingSpec())
    server.run()
```
"""

EMBEDDING_API_EXAMPLE_BATCHING = """
Please follow the example below for guidance on how to use the OpenAI Embedding spec with batching:

```python
import numpy as np
from typing import List
from litserve.specs import OpenAIEmbeddingSpec, EmbeddingRequest
import litserve as ls

class TestAPI(ls.LitAPI):
    def setup(self, device):
        self.model = None

    def predict(self, inputs) -> list[list[float]]:
        # inputs is a list of texts (list[str])
        return np.random.rand(len(inputs), 768)

if __name__ == "__main__":
    api = TestAPI(max_batch_size=2, batch_timeout=0.4)
    server = ls.LitServer(api, spec=OpenAIEmbeddingSpec())
    server.run()
```
"""


class OpenAIEmbeddingSpec(LitSpec):
    def __init__(self):
        super().__init__()
        self.api_path = "/v1/embeddings"  # default api path

    def pre_setup(self, lit_api: "LitAPI"):
        from litserve import LitAPI

        # Override the spec's api_path only if provided
        if lit_api._api_path and lit_api._api_path not in (_DEFAULT_LIT_API_PATH, self.api_path):
            self.api_path = lit_api._api_path
            warnings.warn(
                f"Custom API path detected: '{self.api_path}'. "
                "The OpenAI SDK only supports the default path '/v1/embeddings'. "
                f"To use '{self.api_path}', send HTTP requests directly or use a client that supports custom endpoints."
                " For SDK compatibility, use the default path."
            )

        # register the endpoint
        self.add_endpoint(self.api_path, self.embeddings_endpoint, ["POST"])
        self.add_endpoint(self.api_path, self.options_embeddings, ["GET"])

        # validate LitAPI methods
        if inspect.isgeneratorfunction(lit_api.predict):
            raise ValueError(
                "You are using yield in your predict method, which is used for streaming.",
                "OpenAIEmbeddingSpec doesn't support streaming because producing embeddings ",
                "is not a sequential operation.",
                "Please consider replacing yield with return in predict.\n",
                EMBEDDING_API_EXAMPLE,
            )

        is_encode_response_original = lit_api.encode_response.__code__ is LitAPI.encode_response.__code__
        if not is_encode_response_original and inspect.isgeneratorfunction(lit_api.encode_response):
            raise ValueError(
                "You are using yield in your encode_response method, which is used for streaming.",
                "OpenAIEmbeddingSpec doesn't support streaming because producing embeddings ",
                "is not a sequential operation.",
                "Please consider replacing yield with return in encode_response.\n",
                EMBEDDING_API_EXAMPLE,
            )

    def setup(self, server: "LitServer"):
        super().setup(server)
        print("OpenAI Embedding Spec is ready.")

    def decode_request(self, request: EmbeddingRequest, context_kwargs: Optional[dict] = None) -> list[str]:
        return request.input

    def encode_response(
        self, output: list[list[float]], context_kwargs: Optional[dict] = None
    ) -> Union[dict, EmbeddingResponse]:
        usage = {
            "prompt_tokens": context_kwargs.get("prompt_tokens", 0) if context_kwargs else 0,
            "total_tokens": context_kwargs.get("total_tokens", 0) if context_kwargs else 0,
        }
        return {"embeddings": output} | usage

    def _validate_response(self, response: Union[dict, list[Embedding], Any]) -> None:
        if isinstance(response, list) and all(isinstance(item, Embedding) for item in response):
            return
        if not isinstance(response, (dict, EmbeddingResponse)):
            raise ValueError(
                f"Expected response to be a dictionary, but got type {type(response)}.",
                "The response should be a dictionary to ensure proper compatibility with the OpenAIEmbeddingSpec.\n\n"
                "Please ensure that your response is a dictionary with the following keys:\n"
                "- 'embeddings' (required)\n"
                "- 'prompt_tokens' (optional)\n"
                "- 'total_tokens' (optional)\n"
                f"{EMBEDDING_API_EXAMPLE}",
            )
        if "embeddings" not in response:
            raise ValueError(
                "The response does not contain the key 'embeddings'."
                "The key 'embeddings' is required to ensure proper compatibility with the OpenAIEmbeddingSpec.\n"
                "Please ensure that your response contains the key 'embeddings'.\n"
                f"{EMBEDDING_API_EXAMPLE}"
            )

    def _handle_embedding_response(
        self, embeddings: Union[list, "np.ndarray", "torch.Tensor", "list[list[float]]"], num_items: int = 1
    ) -> list[Embedding]:
        ndim = None
        if "torch" in sys.modules:
            import torch

            if isinstance(embeddings, torch.Tensor):
                ndim = embeddings.ndim
        if "numpy" in sys.modules:
            import numpy as np

            if isinstance(embeddings, np.ndarray):
                ndim = embeddings.ndim

        # expand_dims for torch.Tensor or np.ndarray
        if ndim == 1:
            embeddings = embeddings[None, :]

        if ndim is not None:
            embeddings = embeddings.tolist()

        # expand dims for list of floats
        if isinstance(embeddings, (list, tuple)) and isinstance(embeddings[0], (int, float)):
            embeddings = [embeddings]

        # check if we have total num_items number of embeddings vectors
        num_response_items = len(embeddings)
        if num_response_items != num_items:
            logger.debug("mismatch between number of requested and returned embeddings: %s", embeddings)
            raise ValueError(
                f"Mismatch between requested and returned embeddings: "
                f"expected {num_items}, but got {num_response_items}. "
                f"This may indicate a bug in the LitAPI embedding implementation."
            )

        result = []
        for i, embedding in enumerate(embeddings):
            result.append(Embedding(index=i, embedding=embedding))

        return result

    async def embeddings_endpoint(self, request: EmbeddingRequest) -> EmbeddingResponse:
        response_queue_id = self.response_queue_id
        num_items = request.get_num_items()
        if num_items > 1 and self._max_batch_size > 1:
            raise HTTPException(
                status_code=400,
                detail=(
                    "The OpenAIEmbedding spec does not support dynamic batching when client-side batching is used. "
                    "To resolve this, either set `max_batch_size=1` or send a single input from the client."
                ),
            )

        logger.debug("Received embedding request: %s", request)
        uid = uuid.uuid4()
        event = asyncio.Event()
        self.response_buffer[uid] = ResponseBufferItem(event=event)

        # Trigger callback
        self._server._callback_runner.trigger_event(
            EventTypes.ON_REQUEST.value,
            active_requests=self._server.active_requests,
            litserver=self._server,
        )

        self.request_queue.put_nowait((response_queue_id, uid, time.monotonic(), request.model_copy()))
        await event.wait()

        response_buffer_item = self.response_buffer.pop(uid)
        response, status = response_buffer_item.response

        if status == LitAPIStatus.ERROR and isinstance(response, HTTPException):
            logger.error("Error in embedding request: %s", response)
            raise response

        if status == LitAPIStatus.ERROR:
            logger.error("Error in embedding request: %s", response)
            raise HTTPException(status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR)

        logger.debug(response)

        self._validate_response(response)
        data: list[Embedding] = self._handle_embedding_response(response["embeddings"], num_items)

        usage = UsageInfo(**response)

        return EmbeddingResponse(data=data, model=request.model, usage=usage)

    async def options_embeddings(self, request: Request):
        return Response(status_code=status.HTTP_200_OK)
```

## File: `src/litserve/test_examples/__init__.py`
```python
from litserve.test_examples.openai_spec_example import (
    OpenAIBatchContext,
    TestAPI,
    TestAPIWithCustomEncode,
    TestAPIWithStructuredOutput,
    TestAPIWithToolCalls,
)
from litserve.test_examples.simple_example import SimpleBatchedAPI, SimpleLitAPI, SimpleStreamAPI, SimpleTorchAPI

__all__ = [
    "SimpleLitAPI",
    "SimpleBatchedAPI",
    "SimpleTorchAPI",
    "TestAPI",
    "TestAPIWithCustomEncode",
    "TestAPIWithStructuredOutput",
    "TestAPIWithToolCalls",
    "OpenAIBatchContext",
    "SimpleStreamAPI",
]
```

## File: `src/litserve/test_examples/openai_embedding_spec_example.py`
```python
import numpy as np

from litserve.api import LitAPI


class TestEmbedAPI(LitAPI):
    def setup(self, device):
        self.model = None

    def predict(self, x) -> list[list[float]]:
        n = len(x) if isinstance(x, list) else 1
        return np.random.rand(n, 768).tolist()

    def encode_response(self, output) -> dict:
        return {"embeddings": output}


class TestEmbedBatchedAPI(TestEmbedAPI):
    def predict(self, batch) -> list[list[list[float]]]:
        return [np.random.rand(len(x), 768).tolist() for x in batch]


class TestEmbedAPIWithUsage(TestEmbedAPI):
    def encode_response(self, output) -> dict:
        return {"embeddings": output, "prompt_tokens": 10, "total_tokens": 10}


class TestEmbedAPIWithYieldPredict(TestEmbedAPI):
    def predict(self, x):
        yield from np.random.rand(768).tolist()


class TestEmbedAPIWithYieldEncodeResponse(TestEmbedAPI):
    def encode_response(self, output):
        yield {"embeddings": output}


class TestEmbedAPIWithNonDictOutput(TestEmbedAPI):
    def encode_response(self, output):
        return output


class TestEmbedAPIWithMissingEmbeddings(TestEmbedAPI):
    def encode_response(self, output):
        return {"output": output}
```

## File: `src/litserve/test_examples/openai_spec_example.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import time

from litserve.api import LitAPI
from litserve.specs.openai import ChatMessage


class TestAPI(LitAPI):
    def setup(self, device):
        self.model = None

    def predict(self, x):
        yield "This is a generated output"


class TestAPIWithCustomEncode(TestAPI):
    def encode_response(self, output):
        yield ChatMessage(role="assistant", content="This is a custom encoded output")


class TestAPIWithToolCalls(TestAPI):
    def encode_response(self, output):
        yield ChatMessage(
            role="assistant",
            content="",
            tool_calls=[
                {
                    "id": "call_1",
                    "type": "function",
                    "function": {"name": "function_1", "arguments": '{"arg_1": "arg_1_value"}'},
                }
            ],
        )


class TestAPIWithStructuredOutput(TestAPI):
    def encode_response(self, output):
        yield ChatMessage(
            role="assistant",
            content='{"name": "Science Fair", "date": "Friday", "participants": ["Alice", "Bob"]}',
        )


class OpenAIBatchContext(LitAPI):
    def setup(self, device: str) -> None:
        self.model = None

    def batch(self, inputs):
        return inputs

    def predict(self, inputs, context):
        n = len(inputs)
        assert isinstance(context, list)
        for ctx in context:
            ctx["temperature"] = 1.0
        output = [
            "Hi!",
            "It's",
            "nice",
            "to",
            "meet",
            "you.",
            "Is",
            "there",
            "something",
            "I",
            "can",
            "help",
            "you",
            "with",
            "or",
            "would",
            "you",
            "like",
            "to",
            "chat?",
        ]
        for out in output:
            time.sleep(0.01)  # fake delay
            yield [out + " "] * n

    def unbatch(self, output):
        return output

    def encode_response(self, output_stream, context):
        for outputs in output_stream:
            yield [{"role": "assistant", "content": output} for output in outputs]
        for ctx in context:
            assert ctx["temperature"] == 1.0, f"context {ctx} is not 1.0"


class OpenAIWithUsage(LitAPI):
    def setup(self, device):
        self.model = None

    def predict(self, x):
        yield {
            "role": "assistant",
            "content": "10 + 6 is equal to 16.",
            "prompt_tokens": 25,
            "completion_tokens": 10,
            "total_tokens": 35,
        }


class OpenAIWithUsageEncodeResponse(LitAPI):
    def setup(self, device):
        self.model = None

    def predict(self, x):
        # streaming tokens
        yield from ["10", " +", " ", "6", " is", " equal", " to", " ", "16", "."]

    def encode_response(self, output):
        for out in output:
            yield {"role": "assistant", "content": out}

        yield {"role": "assistant", "content": "", "prompt_tokens": 25, "completion_tokens": 10, "total_tokens": 35}


class OpenAIBatchingWithUsage(OpenAIWithUsage):
    def batch(self, inputs):
        return inputs

    def predict(self, x):
        n = len(x)
        yield ["10 + 6 is equal to 16."] * n

    def encode_response(self, output_stream_batch, context):
        n = len(context)
        for output_batch in output_stream_batch:
            yield [{"role": "assistant", "content": out} for out in output_batch]

        yield [
            {"role": "assistant", "content": "", "prompt_tokens": 25, "completion_tokens": 10, "total_tokens": 35}
        ] * n

    def unbatch(self, output):
        return output
```

## File: `src/litserve/test_examples/simple_example.py`
```python
from litserve.api import LitAPI


class SimpleLitAPI(LitAPI):
    def setup(self, device):
        # Set up the model, so it can be called in `predict`.
        self.model = lambda x: x**2

    def decode_request(self, request):
        # Convert the request payload to your model input.
        return request["input"]

    def predict(self, x):
        # Run the model on the input and return the output.
        return self.model(x)

    def encode_response(self, output):
        # Convert the model output to a response payload.
        return {"output": output}


class SimpleBatchedAPI(LitAPI):
    def setup(self, device) -> None:
        self.model = lambda x: x**2

    def decode_request(self, request):
        import numpy as np

        return np.asarray(request["input"])

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output):
        return {"output": output}


class SimpleTorchAPI(LitAPI):
    def setup(self, device):
        # move the model to the correct device
        # keep track of the device for moving data accordingly
        import torch.nn as nn

        class Linear(nn.Module):
            def __init__(self):
                super().__init__()
                self.linear = nn.Linear(1, 1)
                self.linear.weight.data.fill_(2.0)
                self.linear.bias.data.fill_(1.0)

            def forward(self, x):
                return self.linear(x)

        self.model = Linear().to(device)

    def decode_request(self, request):
        import torch

        # get the input and create a 1D tensor on the correct device
        content = request["input"]
        return torch.tensor([content], device=self.device)

    def predict(self, x):
        # the model expects a batch dimension, so create it
        return self.model(x[None, :])

    def encode_response(self, output):
        # float will take the output value directly onto CPU memory
        return {"output": float(output)}


class SimpleStreamAPI(LitAPI):
    """
    Run as:
        ```
        server = ls.LitServer(SimpleStreamAPI(), stream=True)
        server.run(port=8000)
        ```
    Then, in a new Python session, retrieve the responses as follows:
        ```
        import requests
        url = "http://127.0.0.1:8000/predict"
        resp = requests.post(url, json={"input": "Hello world"}, headers=None, stream=True)
        for line in resp.iter_content(5000):
        if line:
            print(line.decode("utf-8"))
        ```
    """

    def setup(self, device) -> None:
        self.model = lambda x, y: f"{x}: {y}"

    def decode_request(self, request):
        return request["input"]

    def predict(self, x):
        for i in range(3):
            yield self.model(i, x)

    def encode_response(self, output_stream):
        for output in output_stream:
            yield {"output": output}
```

## File: `src/litserve/transport/__init__.py`
```python
from .process_transport import MPQueueTransport
from .zmq_transport import ZMQTransport

__all__ = ["ZMQTransport", "MPQueueTransport"]
```

## File: `src/litserve/transport/base.py`
```python
from abc import ABC, abstractmethod
from typing import Any, Optional


class MessageTransport(ABC):
    @abstractmethod
    def send(self, item: Any, consumer_id: int) -> None:
        """Send a message to a consumer in the main process."""
        pass

    @abstractmethod
    async def areceive(self, timeout: Optional[int] = None, consumer_id: Optional[int] = None) -> dict:
        """Receive a message from model workers or any publisher."""
        pass

    def close(self, **kwargs) -> None:
        """Clean up resources if needed (e.g., sockets, processes)."""
        pass
```

## File: `src/litserve/transport/factory.py`
```python
from multiprocessing import Manager
from typing import Literal, Optional

from pydantic import BaseModel, Field

from litserve.transport.process_transport import MPQueueTransport
from litserve.transport.zmq_queue import Broker
from litserve.transport.zmq_transport import ZMQTransport


class TransportConfig(BaseModel):
    transport_type: Literal["mp", "zmq"] = "mp"
    num_consumers: int = Field(1, ge=1)
    manager: Optional[Manager] = None
    consumer_id: Optional[int] = None
    frontend_address: Optional[str] = None
    backend_address: Optional[str] = None


def _create_zmq_transport(config: TransportConfig):
    broker = Broker()
    broker.start()
    config.frontend_address = broker.frontend_address
    config.backend_address = broker.backend_address
    return ZMQTransport(config.frontend_address, config.backend_address)


def _create_mp_transport(config: TransportConfig):
    queues = [config.manager.Queue() for _ in range(config.num_consumers)]
    return MPQueueTransport(config.manager, queues)


def create_transport_from_config(config: TransportConfig):
    if config.transport_type == "mp":
        return _create_mp_transport(config)
    if config.transport_type == "zmq":
        return _create_zmq_transport(config)
    raise ValueError(f"Invalid transport type: {config.transport_type}")
```

## File: `src/litserve/transport/process_transport.py`
```python
import asyncio
from contextlib import suppress
from multiprocessing import Manager, Queue
from typing import Any, Optional

from litserve.transport.base import MessageTransport


class MPQueueTransport(MessageTransport):
    def __init__(self, manager: Manager, queues: list[Queue]):
        self._queues = queues
        self._closed = False

    def send(self, item: Any, consumer_id: int) -> None:
        return self._queues[consumer_id].put(item)

    async def areceive(self, consumer_id: int, timeout: Optional[float] = None, block: bool = True) -> dict:
        if self._closed:
            raise asyncio.CancelledError("Transport closed")

        actual_timeout = 1 if timeout is None else min(timeout, 1)

        try:
            return await asyncio.to_thread(self._queues[consumer_id].get, timeout=actual_timeout, block=True)
        except asyncio.CancelledError:
            raise
        except Exception:
            if self._closed:
                raise asyncio.CancelledError("Transport closed")
            if timeout is not None and timeout <= actual_timeout:
                raise
            return None

    def close(self, send_sentinel: bool = True) -> None:
        # Mark the transport as closed
        self._closed = True

        # Only send sentinel values if requested and safe to do so
        if send_sentinel:
            # Put sentinel values in the queues as a backup mechanism
            for queue in self._queues:
                with suppress(Exception):
                    queue.put(None, block=False)

    def __reduce__(self):
        return (MPQueueTransport, (None, self._queues))
```

## File: `src/litserve/transport/zmq_queue.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import logging
import multiprocessing
import pickle
import threading
import time
from queue import Empty
from typing import Any, Optional

import zmq
import zmq.asyncio

from litserve.utils import generate_random_zmq_address

logger = logging.getLogger(__name__)


class Broker:
    """Message broker that routes messages between producers and consumers."""

    def __init__(self, use_process: bool = False):
        self.frontend_address = generate_random_zmq_address()
        self.backend_address = generate_random_zmq_address()
        self._running = False
        self._use_process = use_process
        self._worker = None

    def start(self):
        """Start the broker in a background thread or process."""
        self._running = True

        if self._use_process:
            self._worker = multiprocessing.Process(target=self._run)
        else:
            self._worker = threading.Thread(target=self._run)

        self._worker.daemon = True
        self._worker.start()
        logger.info(
            f"Broker started in {'process' if self._use_process else 'thread'} "
            f"on {self.frontend_address} (frontend) and {self.backend_address} (backend)"
        )
        time.sleep(0.1)  # Give the broker time to start

    def _run(self):
        """Main broker loop."""
        context = zmq.Context()
        try:
            frontend = context.socket(zmq.XPUB)
            frontend.bind(self.frontend_address)

            backend = context.socket(zmq.XSUB)
            backend.bind(self.backend_address)

            zmq.proxy(frontend, backend)
        except zmq.ZMQError as e:
            logger.error(f"Broker error: {e}")
        finally:
            frontend.close(linger=0)
            backend.close(linger=0)
            context.term()

    def stop(self):
        """Stop the broker."""
        self._running = False
        if self._worker:
            self._worker.join()


class Producer:
    """Producer class for sending messages to consumers."""

    def __init__(self, address: str = None):
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.PUB)
        self._socket.connect(address)

    def wait_for_subscribers(self, timeout: float = 1.0) -> bool:
        """Wait for at least one subscriber to be ready.

        Args:
            timeout: Maximum time to wait in seconds

        Returns:
            bool: True if subscribers are ready, False if timeout occurred

        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            # Send a ping message to consumer 0 (special system messages)
            try:
                self._socket.send(b"0|__ping__", zmq.NOBLOCK)
                time.sleep(0.1)  # Give time for subscription to propagate
                return True
            except zmq.ZMQError:
                continue
        return False

    def put(self, item: Any, consumer_id: int) -> None:
        """Send an item to a specific consumer."""
        try:
            pickled_item = pickle.dumps(item)
            message = f"{consumer_id}|".encode() + pickled_item
            self._socket.send(message)
        except zmq.ZMQError as e:
            logger.error(f"Error sending item: {e}")
            raise
        except pickle.PickleError as e:
            logger.error(f"Error serializing item: {e}")
            raise

    def close(self) -> None:
        """Clean up resources."""
        if self._socket:
            self._socket.close(linger=0)
        if self._context:
            self._context.term()


class BaseConsumer:
    """Base class for consumers."""

    def __init__(self, consumer_id: int, address: str):
        self.consumer_id = consumer_id
        self.address = address
        self._context = None
        self._socket = None
        self._setup_socket()

    def _setup_socket(self):
        """Setup ZMQ socket - to be implemented by subclasses"""
        raise NotImplementedError

    def _parse_message(self, message: bytes) -> Any:
        """Parse a message received from ZMQ."""
        try:
            consumer_id, pickled_data = message.split(b"|", 1)
            return pickle.loads(pickled_data)
        except pickle.PickleError as e:
            logger.error(f"Error deserializing message: {e}")
            raise

    def close(self) -> None:
        """Clean up resources."""
        if self._socket:
            self._socket.close(linger=0)
        if self._context:
            self._context.term()


class AsyncConsumer(BaseConsumer):
    """Async consumer class for receiving messages using asyncio."""

    def _setup_socket(self):
        self._context = zmq.asyncio.Context()
        self._socket = self._context.socket(zmq.SUB)
        self._socket.connect(self.address)
        self._socket.setsockopt_string(zmq.SUBSCRIBE, str(self.consumer_id))

    async def get(self, timeout: Optional[float] = None) -> Any:
        """Get an item from the queue asynchronously."""
        try:
            if timeout is not None:
                message = await asyncio.wait_for(self._socket.recv(), timeout)
            else:
                message = await self._socket.recv()

            return self._parse_message(message)
        except asyncio.TimeoutError:
            raise Empty
        except zmq.ZMQError:
            raise Empty

    def close(self) -> None:
        """Clean up resources asynchronously."""
        if self._socket:
            self._socket.close(linger=0)
        if self._context:
            self._context.term()
```

## File: `src/litserve/transport/zmq_transport.py`
```python
from typing import Any, Literal, Optional, Union

import zmq

from litserve.transport.base import MessageTransport
from litserve.transport.zmq_queue import AsyncConsumer, Producer


class ZMQTransport(MessageTransport):
    def __init__(self, backend_address: str, frontend_address):
        self.backend_address = backend_address
        self.frontend_address = frontend_address
        self._zmq: Union[Producer, AsyncConsumer, None] = None

    def setup(self, operation: Literal[zmq.SUB, zmq.PUB], consumer_id: Optional[int] = None) -> None:
        """Must be called in the subprocess to setup the ZMQ transport."""
        if operation == zmq.PUB:
            self._zmq = Producer(address=self.backend_address)
            self._zmq.wait_for_subscribers()
        elif operation == zmq.SUB:
            self._zmq = AsyncConsumer(consumer_id=consumer_id, address=self.frontend_address)
        else:
            raise ValueError(f"Invalid operation {operation}")

    def send(self, item: Any, consumer_id: int) -> None:
        if self._zmq is None:
            self.setup(zmq.PUB)
        return self._zmq.put(item, consumer_id)

    async def areceive(self, consumer_id: Optional[int] = None, timeout=None) -> dict:
        if self._zmq is None:
            self.setup(zmq.SUB, consumer_id)
        return await self._zmq.get(timeout=timeout)

    def close(self, **kwargs) -> None:
        if self._zmq:
            self._zmq.close()
        else:
            raise ValueError("ZMQ not initialized, make sure ZMQTransport.setup() is called.")

    def __reduce__(self):
        return ZMQTransport, (self.backend_address, self.frontend_address)
```

## File: `tests/__init__.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
```

## File: `tests/conftest.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import base64
import random
import time
from collections.abc import Generator

import psutil
import pytest
from fastapi import Request, Response
from fastapi.testclient import TestClient

from litserve.api import LitAPI
from litserve.server import LitServer
from litserve.utils import wrap_litserve_start


def pytest_collection_modifyitems(config, items):
    """Auto-mark tests based on their file path."""
    for item in items:
        # Get the relative path of the test file
        test_path = item.fspath.relto(config.rootdir)

        if "tests/unit/" in str(test_path):
            item.add_marker(pytest.mark.unit)
        elif "tests/integration/" in str(test_path):
            item.add_marker(pytest.mark.integration)
        elif "tests/e2e/" in str(test_path):
            item.add_marker(pytest.mark.e2e)


class SimpleLitAPI(LitAPI):
    def setup(self, device):
        self.model = lambda x: x**2

    def decode_request(self, request: Request):
        return request["input"]

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output) -> Response:
        return {"output": output}


class SimpleStreamAPI(LitAPI):
    def setup(self, device) -> None:
        self.sentence = "LitServe is streaming output"

    def decode_request(self, request: Request) -> str:
        return request["prompt"]

    def predict(self, x) -> Generator:
        output = f"prompt={x} generated_output={self.sentence}".split()
        yield from output

    def encode_response(self, output: Generator) -> Generator:
        delay = 0.01  # delay for testing timeouts
        for out in output:
            time.sleep(delay)
            yield out.lower()


class SimpleBatchedStreamAPI(LitAPI):
    def setup(self, device) -> None:
        self.sentence = "LitServe is streaming output"

    def decode_request(self, request: Request) -> str:
        return request["prompt"]

    def batch(self, inputs):
        return inputs

    def predict(self, x) -> Generator:
        n = len(x)
        output = self.sentence.split()
        responses = [x]
        for out in output:
            responses.append([out] * n)
        yield from responses

    def encode_response(self, output: Generator) -> Generator:
        delay = 0.01  # delay for testing timeouts
        for out in output:
            time.sleep(delay)
            yield [e.lower() for e in out]

    def unbatch(self, output):
        yield from output


@pytest.fixture
def simple_litapi():
    return SimpleLitAPI()


@pytest.fixture
def simple_litapi_cls():
    return SimpleLitAPI


@pytest.fixture
def simple_stream_cls():
    return SimpleStreamAPI


@pytest.fixture
def simple_stream_api():
    return SimpleStreamAPI(stream=True)


@pytest.fixture
def simple_batched_stream_api():
    return SimpleBatchedStreamAPI()


@pytest.fixture
def lit_server(simple_litapi):
    server = LitServer(simple_litapi, accelerator="cpu", devices=1, timeout=10)
    with wrap_litserve_start(server) as s:
        yield s


@pytest.fixture
def sync_testclient(lit_server):
    with TestClient(lit_server.app) as client:
        yield client


@pytest.fixture
def killall():
    def _run(process):
        parent = psutil.Process(process.pid)
        for child in parent.children(recursive=True):
            child.kill()
        process.kill()

    return _run


@pytest.fixture
def openai_request_data():
    return {
        "model": "",
        "messages": [{"role": "string", "content": "string"}],
        "temperature": 0.7,
        "top_p": 1,
        "n": 1,
        "max_completion_tokens": 0,
        "stop": "string",
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "user": "string",
    }


@pytest.fixture
def openai_response_data():
    return {
        "id": "chatcmpl-9dEtoQu4g45g3431SZ2s98S",
        "choices": [
            {
                "finish_reason": "stop",
                "index": 0,
                "logprobs": None,
                "message": {
                    "content": "10 + 6 is equal to 16.",
                    "role": "assistant",
                    "function_call": None,
                    "tool_calls": None,
                },
            }
        ],
        "created": 1719139092,
        "model": "gpt-3.5-turbo-0125",
        "object": "chat.completion",
        "system_fingerprint": None,
        "usage": {"completion_tokens": 10, "prompt_tokens": 25, "total_tokens": 35},
    }


@pytest.fixture
def openai_request_data_with_image():
    return {
        "model": "lit",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image_url",
                        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                    },
                ],
            }
        ],
        "temperature": 0.7,
        "top_p": 1,
        "n": 1,
        "max_completion_tokens": 0,
        "stop": "string",
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "user": "string",
    }


@pytest.fixture
def openai_request_data_with_audio_wav(openai_request_data):
    # Create a base64 encoded string from a list of audio data
    audio_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    encoded_string = base64.b64encode(bytearray(audio_data)).decode("utf-8")

    request_data = openai_request_data.copy()
    request_data["messages"] = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What is in this recording?"},
                {"type": "input_audio", "input_audio": {"data": encoded_string, "format": "wav"}},
            ],
        },
    ]
    return request_data


@pytest.fixture
def openai_request_data_with_audio_flac(openai_request_data):
    # Create a base64 encoded string from a list of audio data
    audio_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    encoded_string = base64.b64encode(bytearray(audio_data)).decode("utf-8")

    request_data = openai_request_data.copy()
    request_data["messages"] = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What is in this recording?"},
                {"type": "input_audio", "input_audio": {"data": encoded_string, "format": "flac"}},
            ],
        },
    ]
    return request_data


@pytest.fixture
def openai_request_data_with_tools():
    return {
        "model": "lit",
        "messages": [{"role": "user", "content": "What's the weather like in Boston today?"}],
        "tools": [
            {
                "type": "function",
                "function": {
                    "name": "get_current_weather",
                    "description": "Get the current weather in a given location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
                            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                        },
                        "required": ["location"],
                    },
                },
            }
        ],
        "temperature": 0.7,
        "top_p": 1,
        "n": 1,
        "max_completion_tokens": 0,
        "stop": "string",
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "user": "string",
    }


@pytest.fixture
def openai_request_data_with_response_format():
    return {
        "model": "lit",
        "messages": [
            {
                "role": "system",
                "content": "Extract the event information.",
            },
            {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "calendar_event",
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "date": {"type": "string"},
                        "participants": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["name", "date", "participants"],
                    "additionalProperties": "false",
                },
                "strict": "true",
            },
        },
        "temperature": 0.7,
        "top_p": 1,
        "n": 1,
        "max_completion_tokens": 0,
        "stop": "string",
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "user": "string",
    }


@pytest.fixture
def openai_request_data_with_metadata():
    return {
        "model": "lit",
        "messages": [
            {
                "role": "system",
                "content": "Extract the event information.",
            },
            {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
        ],
        "temperature": 0.7,
        "top_p": 1,
        "n": 1,
        "max_completion_tokens": 0,
        "stop": "string",
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "user": "string",
        "metadata": {"user_id": "123", "trace_id": "abc-xyz"},
    }


@pytest.fixture
def openai_embedding_request_data():
    return {"input": "A beautiful sunset over the beach.", "model": "lit", "encoding_format": "float"}


@pytest.fixture
def openai_embedding_request_data_array():
    return {"input": ["A beautiful sunset over the beach."] * 4, "model": "lit", "encoding_format": "float"}


class MockEvent:
    def set(self):
        pass

    def wait(self):
        pass


class MockQueue:
    def put(self, item):
        pass

    def get(self, block=True, timeout=None):
        pass


@pytest.fixture
def mock_manager():
    class MockManager:
        def __init__(self):
            self.Queue = MockQueue
            self.Event = MockEvent
            self.dict = dict

        def shutdown(self):
            pass

    return MockManager()


@pytest.fixture
def port():
    return random.randint(10000, 65535)
```

## File: `tests/minimal_run.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
import subprocess
import time
import urllib.request

import psutil


def main():
    process = subprocess.Popen(
        ["python", "tests/simple_server.py"],
    )
    print("Waiting for server to start...")
    time.sleep(10)
    try:
        url = "http://127.0.0.1:8000/predict"
        data = json.dumps({"input": 4.0}).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        request = urllib.request.Request(url, data=data, headers=headers, method="POST")
        response = urllib.request.urlopen(request)
        status_code = response.getcode()
        assert status_code == 200
    except Exception:
        raise

    finally:
        parent = psutil.Process(process.pid)
        for child in parent.children(recursive=True):
            child.kill()
        process.kill()


if __name__ == "__main__":
    main()
```

## File: `tests/simple_server.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from fastapi import Request, Response

from litserve.api import LitAPI
from litserve.server import LitServer


class SimpleLitAPI(LitAPI):
    def setup(self, device):
        self.model = lambda x: x**2

    def decode_request(self, request: Request):
        return request["input"]

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output) -> Response:
        return {"output": output}


if __name__ == "__main__":
    server = LitServer(SimpleLitAPI(), accelerator="cpu", devices=1, timeout=10)
    server.run()
```

## File: `tests/simple_server_diff_port.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from litserve.api import LitAPI
from litserve.server import LitServer


class SimpleLitAPI(LitAPI):
    def setup(self, device):
        self.model = lambda x: x**2

    def decode_request(self, request):
        return request["input"]

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output):
        return {"output": output}


if __name__ == "__main__":
    server = LitServer(SimpleLitAPI(), accelerator="cpu", devices=1, timeout=10)
    server.run(port=8080)
```

## File: `tests/e2e/default_api.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import litserve as ls

if __name__ == "__main__":
    api = ls.test_examples.SimpleLitAPI()
    server = ls.LitServer(api)
    server.run(port=8000)
```

## File: `tests/e2e/default_async_streaming.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import litserve as ls


class AsyncAPI(ls.LitAPI):
    def setup(self, device) -> None:
        self.model = lambda x: x

    async def decode_request(self, request):
        return request["input"]

    async def predict(self, x):
        for i in range(10):
            yield self.model(i)

    async def encode_response(self, output):
        async for out in output:
            yield {"output": out}


if __name__ == "__main__":
    api = AsyncAPI(enable_async=True, stream=True)
    server = ls.LitServer(api)
    server.run(port=8000)
```

## File: `tests/e2e/default_batched_streaming.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import numpy as np

import litserve as ls


class SimpleStreamAPI(ls.LitAPI):
    def setup(self, device) -> None:
        self.model = lambda x, y: x * y

    def decode_request(self, request):
        return np.asarray(request["input"])

    def predict(self, x):
        for i in range(10):
            yield self.model(x, i)

    def encode_response(self, output_stream):
        for outputs in output_stream:
            yield [{"output": output} for output in outputs]


if __name__ == "__main__":
    api = SimpleStreamAPI(stream=True, max_batch_size=4, batch_timeout=0.2)
    server = ls.LitServer(api, fast_queue=True)
    server.run(port=8000)
```

## File: `tests/e2e/default_batching.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import litserve as ls

if __name__ == "__main__":
    api = ls.test_examples.SimpleBatchedAPI(max_batch_size=4, batch_timeout=0.05)
    server = ls.LitServer(api)
    server.run(port=8000)
```

## File: `tests/e2e/default_mcp.py`
```python
from pydantic import BaseModel

import litserve as ls
from litserve.mcp import MCP


class PowerRequest(BaseModel):
    input: float


class MyLitAPI(ls.test_examples.SimpleLitAPI):
    def decode_request(self, request: PowerRequest) -> int:
        print(f"Decoding request: {request}")
        return request.input


if __name__ == "__main__":
    api = MyLitAPI(mcp=MCP(description="Returns the power of a number."))
    server = ls.LitServer(api)
    server.run(port=8000)
```

## File: `tests/e2e/default_openai_embedding_spec.py`
```python
import litserve as ls
from litserve import OpenAIEmbeddingSpec
from litserve.test_examples.openai_embedding_spec_example import TestEmbedAPI

if __name__ == "__main__":
    api = TestEmbedAPI(spec=OpenAIEmbeddingSpec())
    server = ls.LitServer(api, fast_queue=True)
    server.run()
```

## File: `tests/e2e/default_openai_with_batching.py`
```python
import litserve as ls
from litserve.test_examples.openai_spec_example import OpenAIBatchContext

if __name__ == "__main__":
    api = OpenAIBatchContext(max_batch_size=2, batch_timeout=0.5, spec=ls.OpenAISpec())
    server = ls.LitServer(api, fast_queue=True)
    server.run(port=8000)
```

## File: `tests/e2e/default_openaispec.py`
```python
import litserve as ls
from litserve import OpenAISpec
from litserve.test_examples.openai_spec_example import TestAPI

if __name__ == "__main__":
    api = TestAPI(spec=OpenAISpec())
    server = ls.LitServer(api)
    server.run()
```

## File: `tests/e2e/default_openaispec_response_format.py`
```python
import litserve as ls
from litserve import OpenAISpec
from litserve.test_examples.openai_spec_example import TestAPIWithStructuredOutput

if __name__ == "__main__":
    api = TestAPIWithStructuredOutput(spec=OpenAISpec())
    server = ls.LitServer(api, fast_queue=True)
    server.run()
```

## File: `tests/e2e/default_openaispec_tools.py`
```python
import litserve as ls
from litserve import OpenAISpec
from litserve.specs.openai import ChatMessage
from litserve.test_examples.openai_spec_example import TestAPI


class TestAPIWithToolCalls(TestAPI):
    def encode_response(self, output):
        yield ChatMessage(
            role="assistant",
            content="",
            tool_calls=[
                {
                    "id": "call_abc123",
                    "type": "function",
                    "function": {"name": "get_current_weather", "arguments": '{\n"location": "Boston, MA"\n}'},
                }
            ],
        )


if __name__ == "__main__":
    api = TestAPIWithToolCalls(spec=OpenAISpec())
    server = ls.LitServer(api)
    server.run()
```

## File: `tests/e2e/default_single_streaming.py`
```python
from litserve import LitAPI, LitServer


class SimpleStreamingAPI(LitAPI):
    def setup(self, device) -> None:
        self.model = lambda x, y: x * y

    def decode_request(self, request):
        return request["input"]

    def predict(self, x):
        for i in range(1, 4):
            yield self.model(i, x)

    def encode_response(self, output_stream):
        for output in output_stream:
            yield {"output": output}


if __name__ == "__main__":
    api = SimpleStreamingAPI(stream=True)
    server = LitServer(api)
    server.run(port=8000)
```

## File: `tests/e2e/default_spec.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import litserve as ls
from litserve.specs.openai import OpenAISpec
from litserve.test_examples.openai_spec_example import TestAPI

if __name__ == "__main__":
    api = TestAPI(spec=OpenAISpec())
    server = ls.LitServer(api)
    server.run(port=8000)
```

## File: `tests/e2e/openai_embedding_with_batching.py`
```python
import numpy as np

import litserve as ls


class EmbeddingsAPI(ls.LitAPI):
    def setup(self, device):
        def model(x):
            return np.random.rand(len(x), 768)

        self.model = model

    def predict(self, inputs):
        return self.model(inputs)


if __name__ == "__main__":
    api = EmbeddingsAPI(max_batch_size=10, batch_timeout=2, spec=ls.OpenAIEmbeddingSpec())
    server = ls.LitServer(api)
    server.run(port=8000)
```

## File: `tests/e2e/test_e2e.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from functools import wraps

import psutil
import pytest
import requests
from openai import OpenAI

from litserve.utils import is_package_installed


def e2e_from_file(filename):
    def decorator(test_fn):
        @wraps(test_fn)
        def wrapper(*args, **kwargs):
            process = subprocess.Popen(
                [sys.executable, filename],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,  # Merge stdout and stderr
                stdin=subprocess.DEVNULL,
                text=True,  # so we get strings instead of bytes
                bufsize=1,  # line-buffered
            )

            try:
                # Print logs in real-time
                for line in process.stdout:
                    print(line, end="")
                    if "Application startup complete." in line:
                        break

                # Give your test function a chance to run
                test_fn(*args, **kwargs)
            except Exception:
                raise
            finally:
                parent = psutil.Process(process.pid)
                for child in parent.children(recursive=True):
                    child.kill()
                process.kill()

        return wrapper

    return decorator


@e2e_from_file("tests/simple_server.py")
def test_run():
    assert os.path.exists("client.py"), f"Expected client file to be created at {os.getcwd()} after starting the server"
    output = subprocess.run("python client.py", shell=True, capture_output=True, text=True).stdout
    assert '{"output":16.0}' in output, f"tests/simple_server.py didn't return expected output, got {output}"
    os.remove("client.py")


@e2e_from_file("tests/simple_server_diff_port.py")
def test_run_with_port():
    assert os.path.exists("client.py"), f"Expected client file to be created at {os.getcwd()} after starting the server"
    with open(os.path.join(os.getcwd(), "client.py")) as f:
        client_code = f.read()
        assert ":8080" in client_code, "Could not find 8080 in client.py"
    output = subprocess.run("python client.py", shell=True, capture_output=True, text=True).stdout
    assert '{"output":16.0}' in output, (
        f"tests/simple_server_server_diff_port.py didn't return expected output, got {output}"
    )
    os.remove("client.py")


@e2e_from_file("tests/e2e/default_api.py")
def test_e2e_default_api():
    resp = requests.post("http://127.0.0.1:8000/predict", json={"input": 4.0}, headers=None)
    assert resp.status_code == 200, f"Expected response to be 200 but got {resp.status_code}"
    assert resp.json() == {"output": 16.0}, "tests/simple_server.py didn't return expected output"


@e2e_from_file("tests/e2e/default_spec.py")
def test_e2e_default_spec(openai_request_data):
    resp = requests.post("http://127.0.0.1:8000/v1/chat/completions", json=openai_request_data)
    assert resp.status_code == 200, f"Expected response to be 200 but got {resp.status_code}"
    output = resp.json()["choices"][0]["message"]["content"]
    expected = "This is a generated output"
    assert output == expected, "tests/default_spec.py didn't return expected output"


@e2e_from_file("tests/e2e/default_batching.py")
def test_e2e_default_batching():
    resp = requests.post("http://127.0.0.1:8000/predict", json={"input": 4.0}, headers=None)
    assert resp.status_code == 200, f"Expected response to be 200 but got {resp.status_code}"
    assert resp.json() == {"output": 16.0}, "tests/simple_server.py didn't return expected output"


@e2e_from_file("tests/e2e/default_batched_streaming.py")
def test_e2e_batched_streaming():
    resp = requests.post("http://127.0.0.1:8000/predict", json={"input": 4.0}, headers=None, stream=True)
    assert resp.status_code == 200, f"Expected response to be 200 but got {resp.status_code}"

    outputs = []
    for line in resp.iter_content(chunk_size=4000):
        if line:
            outputs.append(json.loads(line.decode("utf-8")))

    assert len(outputs) == 10, "streaming server should have 10 outputs"
    assert {"output": 16.0} in outputs, "server didn't return expected output"


@e2e_from_file("tests/e2e/default_openaispec.py")
def test_openai_parity():
    client = OpenAI(
        base_url="http://127.0.0.1:8000/v1",
        api_key="lit",  # required, but unused
    )
    response = client.chat.completions.create(
        model="lit",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "How are you?"},
        ],
    )
    assert response.choices[0].message.content == "This is a generated output", (
        f"Server didn't return expected output\nOpenAI client output: {response}"
    )

    response = client.chat.completions.create(
        model="lit",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "How are you?"},
        ],
        stream=True,
    )

    expected_outputs = ["This is a generated output", None]
    for r, expected_out in zip(response, expected_outputs):
        assert r.choices[0].delta.content == expected_out, (
            f"Server didn't return expected output.\nOpenAI client output: {r}"
        )


@e2e_from_file("tests/e2e/default_openaispec.py")
def test_openai_parity_with_image_input():
    client = OpenAI(
        base_url="http://127.0.0.1:8000/v1",
        api_key="lit",  # required, but unused
    )
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                        "detail": "low",
                    },
                },
            ],
        },
    ]
    response = client.chat.completions.create(
        model="lit",
        messages=messages,
    )
    assert response.choices[0].message.content == "This is a generated output", (
        f"Server didn't return expected output\nOpenAI client output: {response}"
    )

    response = client.chat.completions.create(
        model="lit",
        messages=messages,
        stream=True,
    )

    expected_outputs = ["This is a generated output", None]
    for r, expected_out in zip(response, expected_outputs):
        assert r.choices[0].delta.content == expected_out, (
            f"Server didn't return expected output.\nOpenAI client output: {r}"
        )


@e2e_from_file("tests/e2e/default_openaispec.py")
def test_openai_parity_with_audio_input(openai_request_data_with_audio_wav):
    client = OpenAI(
        base_url="http://127.0.0.1:8000/v1",
        api_key="lit",  # required, but unused
    )
    messages = openai_request_data_with_audio_wav["messages"]
    response = client.chat.completions.create(
        model="lit",
        messages=messages,
    )
    assert response.choices[0].message.content == "This is a generated output", (
        f"Server didn't return expected output\nOpenAI client output: {response}"
    )

    response = client.chat.completions.create(
        model="lit",
        messages=messages,
        stream=True,
    )

    expected_outputs = ["This is a generated output", None]
    for r, expected_out in zip(response, expected_outputs):
        assert r.choices[0].delta.content == expected_out, (
            f"Server didn't return expected output.\nOpenAI client output: {r}"
        )


@e2e_from_file("tests/e2e/default_openaispec_tools.py")
def test_openai_parity_with_tools():
    client = OpenAI(
        base_url="http://127.0.0.1:8000/v1",
        api_key="lit",  # required, but unused
    )
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            },
        }
    ]
    messages = [
        {"role": "user", "content": "What's the weather like in Boston today?"},
    ]
    response = client.chat.completions.create(
        model="lit",
        messages=messages,
        tools=tools,
    )
    assert response.choices[0].message.content == "", (
        f"Server didn't return expected output\nOpenAI client output: {response}"
    )
    assert response.choices[0].message.tool_calls[0].function.name == "get_current_weather", (
        f"Server didn't return expected output\nOpenAI client output: {response}"
    )

    response = client.chat.completions.create(
        model="lit",
        messages=messages,
        stream=True,
    )

    expected_outputs = ["", None]
    for r, expected_out in zip(response, expected_outputs):
        assert r.choices[0].delta.content == expected_out, (
            f"Server didn't return expected output.\nOpenAI client output: {r}"
        )
        if r.choices[0].delta.tool_calls:
            assert r.choices[0].delta.tool_calls[0].function.name == "get_current_weather", (
                f"Server didn't return expected output.\nOpenAI client output: {r}"
            )


@e2e_from_file("tests/e2e/default_openai_with_batching.py")
def test_e2e_openai_with_batching(openai_request_data):
    client = OpenAI(
        base_url="http://127.0.0.1:8000/v1",
        api_key="lit",  # required, but unused
    )
    response = client.chat.completions.create(
        model="lit",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "How are you?"},
        ],
    )
    assert response.choices[0].message.content == (
        "Hi! It's nice to meet you. Is there something I can help you with or would you like to chat? "
    ), f"Server didn't return expected output OpenAI client output: {response}"


@e2e_from_file("tests/e2e/default_openaispec_response_format.py")
def test_openai_parity_with_response_format():
    client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="lit")
    messages = [
        {
            "role": "system",
            "content": "Extract the event information.",
        },
        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
    ]
    response_format = {
        "type": "json_schema",
        "json_schema": {
            "name": "calendar_event",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "date": {"type": "string"},
                    "participants": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["name", "date", "participants"],
                "additionalProperties": "false",
            },
            "strict": "true",
        },
    }
    output = '{"name": "Science Fair", "date": "Friday", "participants": ["Alice", "Bob"]}'
    response = client.chat.completions.create(
        model="lit",
        messages=messages,
        response_format=response_format,
    )
    assert response.choices[0].message.content == output, (
        f"Server didn't return expected output\nOpenAI client output: {response}"
    )

    response = client.chat.completions.create(
        model="lit",
        messages=messages,
        response_format=response_format,
        stream=True,
    )

    expected_outputs = [output, None]
    for r, expected_out in zip(response, expected_outputs):
        assert r.choices[0].delta.content == expected_out, (
            f"Server didn't return expected output.\nOpenAI client output: {r}"
        )


@e2e_from_file("tests/e2e/default_single_streaming.py")
def test_e2e_single_streaming():
    resp = requests.post("http://127.0.0.1:8000/predict", json={"input": 4.0}, headers=None, stream=True)
    assert resp.status_code == 200, f"Expected response to be 200 but got {resp.status_code}"

    outputs = []
    for line in resp.iter_lines():
        if line:
            outputs.append(json.loads(line.decode("utf-8")))

    assert len(outputs) == 3, "Expected 3 streamed outputs"
    assert outputs[-1] == {"output": 12.0}, "Final output doesn't match expected value"

    expected_values = [4.0, 8.0, 12.0]
    for i, output in enumerate(outputs):
        assert output["output"] == expected_values[i], f"Intermediate output {i} is not expected value"


@e2e_from_file("tests/e2e/default_openai_embedding_spec.py")
def test_openai_embedding_parity():
    client = OpenAI(
        base_url="http://127.0.0.1:8000/v1",
        api_key="lit",
    )

    model = "lit"
    input_text = "The food was delicious and the waiter was very friendly."
    input_text_list = [input_text] * 2
    response = client.embeddings.create(
        model="lit", input="The food was delicious and the waiter...", encoding_format="float"
    )
    assert response.model == model, f"Expected model to be {model} but got {response.model}"
    assert len(response.data) == 1, f"Expected 1 embeddings but got {len(response.data)}"
    assert len(response.data[0].embedding) == 768, f"Expected 768 dimensions but got {len(response.data[0].embedding)}"
    assert isinstance(response.data[0].embedding[0], float), "Expected float datatype but got something else"

    response = client.embeddings.create(model="lit", input=input_text_list, encoding_format="float")
    assert response.model == model, f"Expected model to be {model} but got {response.model}"
    assert len(response.data) == 2, f"Expected 2 embeddings but got {len(response.data)}"
    for data in response.data:
        assert len(data.embedding) == 768, f"Expected 768 dimensions but got {len(data.embedding)}"


@e2e_from_file("tests/e2e/default_async_streaming.py")
def test_e2e_default_async_streaming():
    resp = requests.post("http://127.0.0.1:8000/predict", json={"input": 4.0}, headers=None, stream=True)
    outputs = []
    for line in resp.iter_lines():
        if line:
            outputs.append(json.loads(line.decode("utf-8"))["output"])

    assert outputs == list(range(10)), "server didn't return expected output"


@e2e_from_file("tests/e2e/openai_embedding_with_batching.py")
def test_e2e_openai_embedding_with_batching():
    model = "text-embedding-3-large"
    client = OpenAI(
        base_url="http://127.0.0.1:8000/v1",
        api_key="lit",  # required, but unused
    )
    futures = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures.append(executor.submit(client.embeddings.create, model=model, input=["This is the first request"]))
        futures.append(executor.submit(client.embeddings.create, model=model, input=["This is the second request"]))
        futures.append(executor.submit(client.embeddings.create, model=model, input=["This is the first request"]))
        futures.append(executor.submit(client.embeddings.create, model=model, input=["This is the second request"]))

    responses = [future.result() for future in futures]
    for response in responses:
        assert response.model == model, f"Expected model to be {model} but got {response.model}"
        assert len(response.data[0].embedding) == 768, (
            f"Expected 768 dimensions but got {len(response.data[0].embedding)}"
        )
    assert len(responses) == 4, f"Expected 4 responses but got {len(responses)}"


@pytest.mark.skipif(not is_package_installed("mcp"), reason="mcp is not installed")
@e2e_from_file("tests/e2e/default_mcp.py")
@pytest.mark.asyncio
async def test_mcp_server():
    from mcp import ClientSession
    from mcp.client.streamable_http import streamablehttp_client

    async with (
        streamablehttp_client("http://localhost:8000/mcp/") as (
            read_stream,
            write_stream,
            _,
        ),
        ClientSession(read_stream, write_stream) as session,
    ):
        await session.initialize()
        result = await session.list_tools()
        assert len(result.tools) == 1, f"Expected 1 tool. Result: {result}"
```

## File: `tests/integration/test_async.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pytest
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

import litserve as ls
from litserve.utils import wrap_litserve_start


class MinimalAsyncAPI(ls.LitAPI):
    def setup(self, device):
        self.model = None

    async def predict(self, x):
        y = x["input"] ** 2
        return {"output": y}


@pytest.mark.asyncio
async def test_async_api():
    server = ls.LitServer(MinimalAsyncAPI(enable_async=True))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            response = await ac.post("/predict", json={"input": 2})
            assert response.json() == {"output": 4}
```

## File: `tests/parity_fastapi/benchmark.py`
```python
import base64
import concurrent.futures
import random
import time

import numpy as np
import requests
import torch
from PIL import Image
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

device = "cuda" if torch.cuda.is_available() else "cpu"
device = "mps" if torch.backends.mps.is_available() else device

rand_mat = np.random.rand(2, 224, 224, 3) * 255
Image.fromarray(rand_mat[0].astype("uint8")).convert("RGB").save("image1.jpg")
Image.fromarray(rand_mat[1].astype("uint8")).convert("RGB").save("image2.jpg")

SERVER_URL = "http://127.0.0.1:{}/predict"

payloads = []
for file in ["image1.jpg", "image2.jpg"]:
    with open(file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        payloads.append(encoded_string)


def create_session(pool_connections, pool_maxsize, max_retries=3):
    """Create a session object with custom connection pool settings."""
    session = requests.Session()
    retry_strategy = Retry(
        total=max_retries,
        backoff_factor=0.1,
    )
    adapter = HTTPAdapter(pool_connections=pool_connections, pool_maxsize=pool_maxsize, max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def send_request(args):
    """Function to send a single request and measure the response time."""
    session, port = args
    url = SERVER_URL.format(port)
    payload = {"image_data": random.choice(payloads)}
    start_time = time.time()
    response = session.post(url, json=payload)
    end_time = time.time()
    return end_time - start_time, response.status_code


def benchmark(num_requests=100, concurrency_level=100, port=8000):
    """Benchmark the ML server."""

    # Create a session with appropriate pool size
    session = create_session(pool_connections=min(concurrency_level, 100), pool_maxsize=min(concurrency_level, 100))

    start_benchmark_time = time.time()  # Start benchmark timing
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency_level) as executor:
        # Pass session to each request
        futures = [executor.submit(send_request, (session, port)) for _ in range(num_requests)]
        response_times = []
        status_codes = []

        for future in concurrent.futures.as_completed(futures):
            response_time, status_code = future.result()
            response_times.append(response_time)
            status_codes.append(status_code)

    session.close()  # Clean up the session

    end_benchmark_time = time.time()  # End benchmark timing
    total_benchmark_time = end_benchmark_time - start_benchmark_time  # Time in seconds

    # Analysis
    total_time = sum(response_times)  # Time in seconds
    avg_time = total_time / num_requests  # Time in seconds
    success_rate = status_codes.count(200) / num_requests * 100
    rps = num_requests / total_benchmark_time  # Requests per second

    # Create a dictionary with the metrics
    metrics = {
        "Total Requests": num_requests,
        "Concurrency Level": concurrency_level,
        "Total Benchmark Time (seconds)": total_benchmark_time,
        "Average Response Time (ms)": avg_time * 1000,
        "Success Rate (%)": success_rate,
        "Requests Per Second (RPS)": rps,
    }

    # Print the metrics
    for key, value in metrics.items():
        print(f"{key}: {value}")
    print("-" * 50)

    return metrics


def run_bench(conf: dict, num_samples: int, port: int):
    num_requests = conf[device]["num_requests"]

    results = []
    for _ in range(num_samples):
        metric = benchmark(num_requests=num_requests, concurrency_level=num_requests, port=port)
        results.append(metric)
    return results[2:]  # skip warmup step
```

## File: `tests/parity_fastapi/fastapi-server.py`
```python
import base64
import io

import PIL
import torch
import torchvision
from fastapi import FastAPI, HTTPException
from jsonargparse import CLI
from pydantic import BaseModel

# Set float32 matrix multiplication precision if GPU is available and capable
if torch.cuda.is_available() and torch.cuda.get_device_capability() >= (8, 0):
    torch.set_float32_matmul_precision("high")

app = FastAPI()


class ImageData(BaseModel):
    image_data: str


class ImageClassifierAPI:
    def __init__(self, device):
        self.device = device
        weights = torchvision.models.ResNet18_Weights.DEFAULT
        self.image_processing = weights.transforms()
        self.model = torchvision.models.resnet18(weights=None).eval().to(device)

    def process_image(self, image_data):
        image = base64.b64decode(image_data)
        pil_image = PIL.Image.open(io.BytesIO(image)).convert("RGB")
        processed_image = self.image_processing(pil_image)
        return processed_image.unsqueeze(0).to(self.device)  # Add batch dimension

    def predict(self, x):
        with torch.inference_mode():
            outputs = self.model(x)
            _, predictions = torch.max(outputs, 1)
        return predictions.item()


device = "cuda" if torch.cuda.is_available() else "cpu"
if torch.backends.mps.is_available():
    device = "mps"
api = ImageClassifierAPI(device)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/predict")
async def predict(image_data: ImageData):
    try:
        processed_image = api.process_image(image_data.image_data)
        prediction = api.predict(processed_image)
        return {"output": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def main():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="warning")


if __name__ == "__main__":
    CLI(main)
```

## File: `tests/parity_fastapi/ls-server.py`
```python
import base64
import io
import os
from concurrent.futures import ThreadPoolExecutor

import PIL
import torch
import torchvision

import litserve as ls

device = "cuda" if torch.cuda.is_available() else "cpu"
device = "mps" if torch.backends.mps.is_available() else device
conf = {
    "cuda": {"batch_size": 16, "workers_per_device": 2},
    "cpu": {"batch_size": 8, "workers_per_device": 2},
    "mps": {"batch_size": 8, "workers_per_device": 2},
}

# Set float32 matrix multiplication precision if GPU is available and capable
if torch.cuda.is_available() and torch.cuda.get_device_capability() >= (8, 0):
    torch.set_float32_matmul_precision("high")


class ImageClassifierAPI(ls.LitAPI):
    def setup(self, device):
        print(device)
        weights = torchvision.models.ResNet18_Weights.DEFAULT
        self.image_processing = weights.transforms()
        self.model = torchvision.models.resnet18(weights=None).eval().to(device)
        self.pool = ThreadPoolExecutor(os.cpu_count())

    def decode_request(self, request):
        return request["image_data"]

    def batch(self, image_data_list):
        def process_image(image_data):
            image = base64.b64decode(image_data)
            pil_image = PIL.Image.open(io.BytesIO(image)).convert("RGB")
            return self.image_processing(pil_image)

        inputs = list(self.pool.map(process_image, image_data_list))
        return torch.stack(inputs).to(self.device)

    def predict(self, x):
        with torch.inference_mode():
            outputs = self.model(x)
            _, predictions = torch.max(outputs, 1)
        return predictions

    def unbatch(self, outputs):
        return outputs.tolist()

    def encode_response(self, output):
        return {"output": output}


def main(batch_size: int, workers_per_device: int):
    print(locals())
    api = ImageClassifierAPI(max_batch_size=batch_size, batch_timeout=0.01)
    server = ls.LitServer(
        api,
        timeout=10,
        workers_per_device=workers_per_device,
        fast_queue=True,
    )
    server.run(port=8000, log_level="warning")


if __name__ == "__main__":
    main(**conf[device])
```

## File: `tests/parity_fastapi/main.py`
```python
import subprocess
import sys
import time
from functools import wraps

import psutil
import requests
import torch
from benchmark import run_bench

CONF = {
    "cpu": {"num_requests": 50},
    "mps": {"num_requests": 50},
    "cuda": {"num_requests": 100},
}

device = "cuda" if torch.cuda.is_available() else "cpu"
device = "mps" if torch.backends.mps.is_available() else device

DIFF_FACTOR = {
    "cpu": 1,
    "cuda": 1.2,
    "mps": 1,
}


def run_python_script(filename):
    def decorator(test_fn):
        @wraps(test_fn)
        def wrapper(*args, **kwargs):
            process = subprocess.Popen(
                [sys.executable, filename],
            )
            print("Waiting for server to start...")
            time.sleep(10)

            try:
                return test_fn(*args, **kwargs)
            except Exception:
                raise
            finally:
                print("Killing the server")
                parent = psutil.Process(process.pid)
                for child in parent.children(recursive=True):
                    child.kill()
                process.kill()

        return wrapper

    return decorator


def try_health(port):
    for i in range(10):
        try:
            response = requests.get(f"http://127.0.0.1:{port}/health")
            if response.status_code == 200:
                return
        except Exception:
            pass


@run_python_script("tests/parity_fastapi/fastapi-server.py")
def run_fastapi_benchmark(num_samples):
    port = 8001
    try_health(port)
    return run_bench(CONF, num_samples, port)


@run_python_script("tests/parity_fastapi/ls-server.py")
def run_litserve_benchmark(num_samples):
    port = 8000
    try_health(port)
    return run_bench(CONF, num_samples, port)


def mean(lst):
    return sum(lst) / len(lst)


def main():
    key = "Requests Per Second (RPS)"
    num_samples = 12
    print("Running FastAPI benchmark")
    fastapi_metrics = run_fastapi_benchmark(num_samples=num_samples)
    print("\n\n" + "=" * 50 + "\n\n")
    print("Running LitServe benchmark")
    ls_metrics = run_litserve_benchmark(num_samples=num_samples)
    fastapi_throughput = mean([e[key] for e in fastapi_metrics])
    ls_throughput = mean([e[key] for e in ls_metrics])
    factor = DIFF_FACTOR[device]
    msg = f"LitServe should have higher throughput than FastAPI on {device}. {ls_throughput} vs {fastapi_throughput}"
    assert ls_throughput > fastapi_throughput * factor, msg
    print(f"{ls_throughput} vs {fastapi_throughput}")


if __name__ == "__main__":
    main()
```

## File: `tests/perf_test/bert/benchmark.py`
```python
import logging
import time

import requests
from requests.adapters import HTTPAdapter
from rich.console import Console
from tenacity import retry, stop_after_attempt
from urllib3.util import Retry
from utils import benchmark

# Configuration
SERVER_URL = "http://0.0.0.0:8000/predict"
MAX_SPEED = 390  # Nvidia 3090

console = Console()


def create_session(pool_connections, pool_maxsize, max_retries=3):
    """Create a session object with custom connection pool settings."""
    session = requests.Session()
    retry_strategy = Retry(
        total=max_retries,
        backoff_factor=0.1,
    )
    adapter = HTTPAdapter(pool_connections=pool_connections, pool_maxsize=pool_maxsize, max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


# Initialize session with reasonable defaults
session = create_session(pool_connections=50, pool_maxsize=50)


def get_average_throughput(num_requests=100, num_samples=10):
    key = "Requests Per Second (RPS)"
    latency_key = "Latency per Request (ms)"
    metric = 0
    latency = 0

    # warmup
    benchmark(num_requests=50, concurrency_level=10, print_metrics=False)
    for i in range(num_samples):
        bnmk = benchmark(num_requests=num_requests, concurrency_level=num_requests, print_metrics=False)
        metric += bnmk[key]
        latency += bnmk[latency_key]
        if (i + 1) % 10 == 0:
            console.print(f"Completed {i + 1} samples", style="bold green")
    avg = metric / num_samples
    console.print("-" * 50, style="bold blue")
    console.print("BERT Performance Test Results", style="bold blue")
    console.print("-" * 50, style="bold blue")
    console.print("avg RPS:", avg)
    console.print("avg latency:", latency / num_samples)
    console.print("-" * 50, style="bold blue")
    return avg


@retry(stop=stop_after_attempt(10))
def main():
    for i in range(10):
        try:
            resp = session.get("http://localhost:8000/health")
            if resp.status_code == 200:
                break
        except requests.exceptions.ConnectionError as e:
            logging.error(f"Error connecting to server: {e}")
        time.sleep(10)

    rps = get_average_throughput(100, num_samples=10)
    if rps < MAX_SPEED:
        console.print(f"\nPerformance test failed. Retrying... (Expected: {MAX_SPEED}, Got: {rps})", style="bold red")
    assert rps >= MAX_SPEED, f"Expected RPS to be greater than {MAX_SPEED}, got {rps}"


if __name__ == "__main__":
    main()
```

## File: `tests/perf_test/bert/data.py`
```python
phrases = [
    "In the midst of a bustling city, amidst the constant hum of traffic and the chatter of countless conversations, "
    "there exists a serene park where people come to escape the chaos. Children play on the swings, their laughter "
    "echoing through the air, while adults stroll along the winding paths, lost in thought. The trees, tall and"
    " majestic, provide a canopy of shade, and the flowers bloom in a riot of colors, adding to the park's charm."
    " It's a place where time seems to slow down, offering a moment of peace and reflection in an otherwise hectic"
    " world.",
    "As the sun sets over the horizon, painting the sky in hues of orange, pink, and purple, a sense of calm descends"
    " over the landscape. The day has been long and filled with activity, but now, in this magical hour, everything "
    "feels different. The birds return to their nests, their evening songs a lullaby to the world. The gentle breeze "
    "carries the scent of blooming jasmine, and the stars begin to twinkle in the darkening sky. It's a time for "
    "quiet contemplation, for appreciating the beauty of nature, and for feeling a deep connection to the universe.",
    "On a remote island, far away from the noise and pollution of modern life, there is a hidden cove where "
    "crystal-clear waters lap gently against the shore. The beach, covered in soft, white sand, is a paradise for "
    "those seeking solitude and tranquility. Palm trees sway in the breeze, their fronds rustling softly, while "
    "the sun casts a warm, golden glow over everything. Here, one can forget the worries of the world and simply "
    "exist in the moment, surrounded by the natural beauty of the island and the soothing sounds of the ocean.",
    "In an ancient forest, where the trees have stood for centuries, there is a sense of timelessness that"
    " envelops everything. The air is cool and crisp, filled with the earthy scent of moss and fallen leaves. Sunlight"
    " filters through the dense canopy, creating dappled patterns on the forest floor. Birds call to one another, and"
    " small animals scurry through the underbrush. It's a place where one can feel the weight of history, where the "
    "presence of the past is almost palpable. Walking through this forest is like stepping back in time, to a world "
    "untouched by human hands.",
    "At the edge of a vast desert, where the dunes stretch out as far as the eye can see, there is a small oasis "
    "that offers a respite from the harsh conditions. A cluster of palm trees provides shade, and a clear, cool spring"
    " bubbles up from the ground, a source of life in an otherwise barren landscape. Travelers who come across this "
    "oasis are greeted with the sight of lush greenery and the sound of birdsong. It's a place of refuge and renewal,"
    " where one can rest and recharge before continuing on their journey through the endless sands.",
    "High in the mountains, where the air is thin and the landscape is rugged, there is a hidden valley that remains"
    " largely untouched by human activity. The valley is a haven for wildlife, with streams that flow with clear,"
    " cold water and meadows filled with wildflowers. The surrounding peaks, covered in snow even in the summer, "
    "stand as silent sentinels. It's a place where one can feel a profound sense of solitude and connection to nature."
    " The beauty of the valley, with its pristine environment and abundant life, is a reminder of the importance of"
    " preserving wild places.",
    "On a quiet country road, far from the bustling cities and noisy highways, there is a small farmhouse surrounded"
    " by fields of golden wheat. The farmhouse, with its weathered wooden walls and cozy interior, is a place of warmth"
    " and hospitality. The fields, swaying gently in the breeze, are a testament to the hard work and dedication of "
    "the farmers who tend them. In the evenings, the sky is filled with stars, and the only sounds are the chirping of"
    " crickets and the distant hoot of an owl. It's a place where one can find peace and simplicity.",
    "In a quaint village, nestled in the rolling hills of the countryside, life moves at a slower pace. The cobblestone"
    " streets are lined with charming cottages, each with its own garden bursting with flowers. The village "
    "square is the heart of the community, where residents gather to catch up on news and enjoy each other's company."
    " There's a timeless quality to the village, where traditions are upheld, and everyone knows their neighbors. "
    "It's a place where one can experience the joys of small-town living, with its close-knit community and strong "
    "sense of belonging.",
    "By the side of a tranquil lake, surrounded by dense forests and towering mountains, there is a small cabin that "
    "offers a perfect retreat from the hustle and bustle of everyday life. The cabin, with its rustic charm and cozy "
    "interior, is a place to unwind and relax. The lake, calm and mirror-like, reflects the beauty of the surrounding "
    "landscape, creating a sense of peace and serenity. It's a place where one can reconnect with nature, spend quiet"
    " moments fishing or kayaking, and enjoy the simple pleasures of life in a beautiful, natural setting.",
]
```

## File: `tests/perf_test/bert/run_test.sh`
```bash
#!/bin/bash

# Function to clean up server process
cleanup() {
    pkill -f "uv run tests/perf_test/bert/server.py"
}

# Trap script exit to run cleanup
trap cleanup EXIT

# Start the server in the background and capture its PID
uv run tests/perf_test/bert/server.py &
SERVER_PID=$!

echo "Server started with PID $SERVER_PID"

# Run your benchmark script
echo "Preparing to run benchmark.py..."

export PYTHONPATH=$PWD && uv run tests/perf_test/bert/benchmark.py

# Check if benchmark.py exited successfully
if [ $? -ne 0 ]; then
    echo "benchmark.py failed to run successfully."
    exit 1
else
    echo "benchmark.py ran successfully."
fi
```

## File: `tests/perf_test/bert/server.py`
```python
"""A BERT-Large text classification server with batching to be used for benchmarking."""

import torch
from jsonargparse import CLI
from transformers import AutoModelForSequenceClassification, AutoTokenizer, BertConfig

import litserve as ls

# Set float32 matrix multiplication precision if GPU is available and capable
if torch.cuda.is_available() and torch.cuda.get_device_capability() >= (8, 0):
    torch.set_float32_matmul_precision("high")

# set dtype to bfloat16 if CUDA is available
dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32


class HuggingFaceLitAPI(ls.LitAPI):
    def setup(self, device):
        print(device)
        model_name = "google-bert/bert-large-uncased"
        config = BertConfig.from_pretrained(pretrained_model_name_or_path=model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_config(config, torch_dtype=dtype)
        self.model.to(device)

    def decode_request(self, request: dict):
        return request["text"]

    def batch(self, inputs):
        return self.tokenizer(inputs, return_tensors="pt", padding=True, truncation=True)

    def predict(self, inputs):
        inputs = {key: value.to(self.device) for key, value in inputs.items()}
        with torch.inference_mode():
            outputs = self.model(**inputs)
            logits = outputs.logits
            return torch.argmax(logits, dim=1)

    def unbatch(self, outputs):
        return outputs.tolist()

    def encode_response(self, output):
        return {"label_idx": output}


def main(
    batch_size: int = 10,
    batch_timeout: float = 0.01,
    devices: int = 2,
    workers_per_device=2,
):
    print(locals())
    api = HuggingFaceLitAPI(
        max_batch_size=batch_size,
        batch_timeout=batch_timeout,
    )
    server = ls.LitServer(
        api,
        workers_per_device=workers_per_device,
        accelerator="auto",
        devices=devices,
        timeout=200,
        fast_queue=True,
    )
    server.run(log_level="warning", num_api_servers=4, generate_client_file=False)


if __name__ == "__main__":
    CLI(main)
```

## File: `tests/perf_test/bert/utils.py`
```python
import concurrent.futures
import random
import time

import psutil
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from tests.perf_test.bert.data import phrases


def create_random_batch(size: int):
    result = []
    for i in range(size):
        result.append(random.choice(phrases))

    return result


# Configuration
SERVER_URL = "http://0.0.0.0:8000/predict"


def create_session(pool_connections, pool_maxsize, max_retries=3):
    """Create a session object with custom connection pool settings."""
    session = requests.Session()
    retry_strategy = Retry(
        total=max_retries,
        backoff_factor=0.1,
    )
    adapter = HTTPAdapter(pool_connections=pool_connections, pool_maxsize=pool_maxsize, max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


# Initialize session with reasonable defaults
session = create_session(pool_connections=50, pool_maxsize=50)

executor = None


def send_request():
    """Function to send a single request and measure the response time."""
    payload = {"text": random.choice(phrases)}
    start_time = time.time()
    response = session.post(SERVER_URL, json=payload)
    end_time = time.time()
    return end_time - start_time, response.status_code


def benchmark(num_requests=1000, concurrency_level=50, print_metrics=True):
    """Benchmark the ML server."""
    import gpustat

    global executor, session

    # Update session if concurrency level changes
    if session.adapters["http://"].poolmanager.connection_pool_kw["maxsize"] < concurrency_level:
        session = create_session(pool_connections=min(concurrency_level, 100), pool_maxsize=min(concurrency_level, 100))

    if executor is None:
        print("creating executor")
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=concurrency_level)

    if executor._max_workers < concurrency_level:
        print("updating executor")
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=concurrency_level)

    start_benchmark_time = time.time()  # Start benchmark timing
    futures = [executor.submit(send_request) for _ in range(num_requests)]
    response_times = []
    status_codes = []

    for future in concurrent.futures.as_completed(futures):
        response_time, status_code = future.result()
        response_times.append(response_time)
        status_codes.append(status_code)

    end_benchmark_time = time.time()  # End benchmark timing
    total_benchmark_time = end_benchmark_time - start_benchmark_time  # Time in seconds

    # Analysis
    total_time = sum(response_times)  # Time in seconds
    avg_time = total_time / num_requests  # Time in seconds
    avg_latency_per_request = (total_time / num_requests) * 1000  # Convert to milliseconds
    success_rate = status_codes.count(200) / num_requests * 100
    rps = num_requests / total_benchmark_time  # Requests per second

    # Calculate throughput per concurrent user in requests per second
    successful_requests = status_codes.count(200)
    throughput_per_user = (successful_requests / total_benchmark_time) / concurrency_level  # Requests per second

    # Create a dictionary with the metrics
    metrics = {
        "Total Requests": num_requests,
        "Concurrency Level": concurrency_level,
        "Total Benchmark Time (seconds)": total_benchmark_time,
        "Average Response Time (ms)": avg_time * 1000,
        "Success Rate (%)": success_rate,
        "Requests Per Second (RPS)": rps,
        "Latency per Request (ms)": avg_latency_per_request,
        "Throughput per Concurrent User (requests/second)": throughput_per_user,
    }
    try:
        gpu_stats = gpustat.GPUStatCollection.new_query()
        metrics["GPU Utilization"] = sum([gpu.utilization for gpu in gpu_stats.gpus])  # / len(gpu_stats.gpus)
    except Exception:
        metrics["GPU Utilization"] = -1
    metrics["CPU Usage"] = psutil.cpu_percent(0.5)

    # Print the metrics
    if print_metrics:
        for key, value in metrics.items():
            print(f"{key}: {value}")
        print("-" * 50)

    return metrics
```

## File: `tests/perf_test/stream/run_test.sh`
```bash
#!/bin/bash
# 1. Test server streams data very fast

# Function to clean up server process
cleanup() {
    pkill -f "uv run tests/perf_test/stream/stream_speed/server.py"
}

# Trap script exit to run cleanup
trap cleanup EXIT

# Start the server in the background and capture its PID
uv run tests/perf_test/stream/stream_speed/server.py &
SERVER_PID=$!

echo "Server started with PID $SERVER_PID"

# Run your benchmark script
echo "Preparing to run benchmark.py..."

export PYTHONPATH=$PWD && uv run tests/perf_test/stream/stream_speed/benchmark.py

# Check if benchmark.py exited successfully
if [ $? -ne 0 ]; then
    echo "benchmark.py failed to run successfully."
    exit 1
else
    echo "benchmark.py ran successfully."
fi
```

## File: `tests/perf_test/stream/stream_speed/benchmark.py`
```python
"""Consume 10K tokens from the stream endpoint and measure the speed."""

import logging
import time

import requests
from requests.adapters import HTTPAdapter
from tenacity import retry, stop_after_attempt
from urllib3.util import Retry

logger = logging.getLogger(__name__)
# Configuration
SERVER_URL = "http://0.0.0.0:8000/predict"
TOTAL_TOKENS = 10000
EXPECTED_TTFT = 0.005  # time to first token

# tokens per second
MAX_SPEED = 3600  # 3600 on GitHub CI, 10000 on M3 Pro


def create_session(pool_connections=10, pool_maxsize=10, max_retries=3):
    """Create a session object with custom connection pool settings."""
    session = requests.Session()
    retry_strategy = Retry(
        total=max_retries,
        backoff_factor=0.1,
        # Don't retry on streaming requests
        allowed_methods=frozenset(["GET", "POST"]),
    )
    adapter = HTTPAdapter(pool_connections=pool_connections, pool_maxsize=pool_maxsize, max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


# Initialize session with reasonable defaults for streaming
session = create_session(pool_connections=10, pool_maxsize=10)


def speed_test():
    start = time.time()
    resp = session.post(SERVER_URL, stream=True, json={"input": 1})
    num_tokens = 0
    ttft = None  # time to first token
    for line in resp.iter_lines():
        if not line:
            continue
        if ttft is None:
            ttft = time.time() - start
            print(f"Time to first token: {ttft}")
            assert ttft < EXPECTED_TTFT, f"Expected time to first token to be less than 0.1 seconds but got {ttft}"
        num_tokens += 1
    end = time.time()
    resp.raise_for_status()
    assert num_tokens == TOTAL_TOKENS, f"Expected {TOTAL_TOKENS} tokens, got {num_tokens}"
    speed = num_tokens / (end - start)
    return {"speed": speed, "time": end - start}


@retry(stop=stop_after_attempt(10))
def main():
    for i in range(10):
        try:
            resp = session.get("http://localhost:8000/health")
            if resp.status_code == 200:
                break
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Error connecting to server: {e}")
        time.sleep(10)
    data = speed_test()
    speed = data["speed"]
    print(data)
    assert speed >= MAX_SPEED, f"Expected streaming speed to be greater than {MAX_SPEED}, got {speed}"


if __name__ == "__main__":
    main()
```

## File: `tests/perf_test/stream/stream_speed/server.py`
```python
import litserve as ls


class SimpleStreamingAPI(ls.LitAPI):
    def setup(self, device) -> None:
        self.model = None

    def decode_request(self, request):
        return request["input"]

    def predict(self, x):
        yield from range(10000)

    def encode_response(self, output_stream):
        for output in output_stream:
            yield {"output": output}


if __name__ == "__main__":
    api = SimpleStreamingAPI()
    server = ls.LitServer(
        api,
        stream=True,
    )
    server.run(port=8000, generate_client_file=False)
```

## File: `tests/unit/test_auth.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fastapi import Depends, HTTPException, Request, Response
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.testclient import TestClient

import litserve.server
from litserve import LitAPI, LitServer
from litserve.utils import wrap_litserve_start


class SimpleAuthedLitAPI(LitAPI):
    def setup(self, device):
        self.model = lambda x: x**2

    def decode_request(self, request: Request):
        return request["input"]

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output) -> Response:
        return {"output": output}

    def authorize(self, auth: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
        if auth.scheme != "Bearer" or auth.credentials != "1234":
            raise HTTPException(status_code=401, detail="Bad token")


def test_authorized_custom():
    server = LitServer(SimpleAuthedLitAPI(), accelerator="cpu", devices=1, workers_per_device=1)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        input = {"input": 4.0}
        response = client.post("/predict", headers={"Authorization": "Bearer 1234"}, json=input)
        assert response.status_code == 200


def test_not_authorized_custom():
    server = LitServer(SimpleAuthedLitAPI(), accelerator="cpu", devices=1, workers_per_device=1)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        input = {"input": 4.0}
        response = client.post("/predict", headers={"Authorization": "Bearer wrong"}, json=input)
        assert response.status_code == 401


class SimpleLitAPI(LitAPI):
    def setup(self, device):
        self.model = lambda x: x**2

    def decode_request(self, request: Request):
        return request["input"]

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output) -> Response:
        return {"output": output}


def test_authorized_api_key():
    litserve.server.LIT_SERVER_API_KEY = "abcd"
    server = LitServer(SimpleLitAPI(), accelerator="cpu", devices=1, workers_per_device=1)

    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        input = {"input": 4.0}
        response = client.post("/predict", headers={"X-API-Key": "abcd"}, json=input)
        assert response.status_code == 200

    litserve.server.LIT_SERVER_API_KEY = None


def test_not_authorized_api_key():
    litserve.server.LIT_SERVER_API_KEY = "abcd"
    server = LitServer(SimpleLitAPI(), accelerator="cpu", devices=1, workers_per_device=1)

    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        input = {"input": 4.0}
        response = client.post("/predict", headers={"X-API-Key": "wrong"}, json=input)
        assert response.status_code == 401

    litserve.server.LIT_SERVER_API_KEY = None
```

## File: `tests/unit/test_batch.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import time
from queue import Queue
from unittest.mock import ANY, MagicMock

import pytest
import torch
import torch.nn as nn
from asgi_lifespan import LifespanManager
from fastapi import Request, Response
from httpx import ASGITransport, AsyncClient

import litserve as ls
from litserve import LitAPI, LitServer
from litserve.callbacks import CallbackRunner
from litserve.loops.base import _SENTINEL_VALUE, _StopLoopError, collate_requests
from litserve.loops.simple_loops import BatchedLoop
from litserve.test_examples import SimpleBatchedAPI
from litserve.transport.base import MessageTransport
from litserve.utils import LoopResponseType, wrap_litserve_start

NOOP_CB_RUNNER = CallbackRunner()


class Linear(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)
        self.linear.weight.data.fill_(2.0)
        self.linear.bias.data.fill_(1.0)

    def forward(self, x):
        return self.linear(x)


class SimpleBatchLitAPI(LitAPI):
    def setup(self, device):
        self.model = Linear().to(device)
        self.device = device

    def decode_request(self, request: Request):
        content = request["input"]
        return torch.tensor([content], device=self.device)

    def batch(self, inputs):
        assert len(inputs) == 2
        return torch.stack(inputs)

    def predict(self, x):
        assert len(x) == 2, "Expected two concurrent inputs to be batched"
        return self.model(x)

    def unbatch(self, output):
        assert output.shape[0] == 2
        return list(output)

    def encode_response(self, output) -> Response:
        return {"output": float(output)}


class SimpleTorchAPI(LitAPI):
    def setup(self, device):
        self.model = Linear().to(device)
        self.device = device

    def decode_request(self, request: Request):
        content = request["input"]
        return torch.tensor([content], device=self.device)

    def predict(self, x):
        assert x.shape == (1,), f"{x}"
        return self.model(x)

    def encode_response(self, output) -> Response:
        return {"output": float(output)}


@pytest.mark.asyncio
async def test_batched():
    api = SimpleBatchLitAPI(max_batch_size=2, batch_timeout=4)
    server = LitServer(api, accelerator="cpu", devices=1, timeout=10)

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            response1 = ac.post("/predict", json={"input": 4.0})
            response2 = ac.post("/predict", json={"input": 5.0})
            response1, response2 = await asyncio.gather(response1, response2)

    assert response1.json() == {"output": 9.0}
    assert response2.json() == {"output": 11.0}


@pytest.mark.asyncio
async def test_unbatched():
    api = SimpleTorchAPI(max_batch_size=1)
    api.request_timeout = 30
    api.pre_setup(spec=None)
    server = LitServer(api, accelerator="cpu", devices=1, timeout=10)
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            response1 = ac.post("/predict", json={"input": 4.0})
            response2 = ac.post("/predict", json={"input": 5.0})
            response1, response2 = await asyncio.gather(response1, response2)

    assert response1.json() == {"output": 9.0}
    assert response2.json() == {"output": 11.0}


def test_request_timeout_connector():
    api = SimpleBatchLitAPI()
    LitServer(api, accelerator="cpu", devices=1, timeout=43.432)
    assert api.request_timeout == 43.432


def test_max_batch_size():
    with pytest.raises(ValueError, match="must be greater than 0"):
        SimpleBatchLitAPI(max_batch_size=0)

    with pytest.raises(ValueError, match="must be greater than 0"):
        SimpleBatchLitAPI(max_batch_size=-1)

    api = SimpleBatchLitAPI(max_batch_size=2, batch_timeout=5)
    with pytest.raises(ValueError, match="batch_timeout must be less than request_timeout"):
        LitServer(api, timeout=2)


def test_max_batch_size_warning():
    warning = "both batch and unbatch methods implemented, but the max_batch_size parameter was not set."
    with pytest.warns(
        UserWarning,
        match=warning,
    ):
        SimpleBatchLitAPI()

    # Test no warnings are raised when max_batch_size is set and max_batch_size is not set
    with (
        pytest.raises(pytest.fail.Exception),
        pytest.warns(
            UserWarning,
            match=warning,
        ),
    ):
        SimpleBatchLitAPI(max_batch_size=2)

    # Test no warning is set when LitAPI doesn't implement batch and unbatch
    with (
        pytest.raises(pytest.fail.Exception),
        pytest.warns(
            UserWarning,
            match=warning,
        ),
    ):
        SimpleTorchAPI()


def test_batch_predict_string_warning():
    api = ls.test_examples.SimpleBatchedAPI(max_batch_size=2, batch_timeout=0.1)
    api.request_timeout = 30
    api.pre_setup(spec=None)
    api.predict = MagicMock(return_value="This is a string")

    mock_input = torch.tensor([[1.0], [2.0]])

    # Simulate the behavior in run_batched_loop
    y = api.predict(mock_input)
    with pytest.warns(
        UserWarning,
        match="When batching is enabled, 'predict' must return a list to handle multiple inputs correctly.",
    ):
        api.unbatch(y)


class FakeResponseQueue:
    def put(self, *args, block=True, timeout=None):
        raise StopIteration("exit loop")


class FakeTransport(MessageTransport):
    def __init__(self):
        self.responses = []

    async def areceive(self, **kwargs) -> dict:
        raise NotImplementedError("This is a fake transport")

    def send(self, response, consumer_id: int):
        self.responses.append(response)


def test_batched_loop():
    requests_queue = Queue()
    response_queue_id = 0
    requests_queue.put((response_queue_id, "uuid-1234", time.monotonic(), {"input": 4.0}))
    requests_queue.put((response_queue_id, "uuid-1235", time.monotonic(), {"input": 5.0}))
    requests_queue.put(_SENTINEL_VALUE)

    lit_api_mock = MagicMock()
    lit_api_mock.request_timeout = 2
    lit_api_mock.max_batch_size = 2
    lit_api_mock.batch_timeout = 4
    lit_api_mock.decode_request = MagicMock(side_effect=lambda x: x["input"])
    lit_api_mock.batch = MagicMock(side_effect=lambda x: x)
    lit_api_mock.predict = MagicMock(side_effect=lambda x: [16.0, 25.0])
    lit_api_mock.unbatch = MagicMock(side_effect=lambda x: x)
    lit_api_mock.encode_response = MagicMock(side_effect=lambda x: {"output": x})

    loop = BatchedLoop()
    loop._restart_workers = True
    transport = FakeTransport()
    loop.run_batched_loop(
        lit_api_mock,
        requests_queue,
        transport=transport,
        callback_runner=NOOP_CB_RUNNER,
    )

    assert len(transport.responses) == 4, "response queue should have 4 responses"
    assert transport.responses[2] == ("uuid-1234", ({"output": 16.0}, "OK", LoopResponseType.REGULAR, ANY))
    assert transport.responses[3] == ("uuid-1235", ({"output": 25.0}, "OK", LoopResponseType.REGULAR, ANY))

    lit_api_mock.batch.assert_called_once()
    lit_api_mock.batch.assert_called_once_with([4.0, 5.0])
    lit_api_mock.unbatch.assert_called_once()


@pytest.mark.parametrize(
    ("batch_timeout", "batch_size"),
    [
        pytest.param(0, 2),
        pytest.param(0, 1000),
        pytest.param(0.1, 2),
        pytest.param(1000, 2),
        pytest.param(0.5, 1000),
    ],
)
def test_collate_requests(batch_timeout, batch_size):
    api = ls.test_examples.SimpleBatchedAPI(max_batch_size=batch_size, batch_timeout=batch_timeout)
    api.request_timeout = 5
    request_queue = Queue()
    for i in range(batch_size):
        request_queue.put((i, f"uuid-abc-{i}", time.monotonic(), i))  # response_queue_id, uid, timestamp, x_enc
    payloads, timed_out_uids = collate_requests(MagicMock(), api, request_queue, MagicMock())
    assert len(payloads) == batch_size, f"Should have {batch_size} payloads, got {len(payloads)}"
    assert len(timed_out_uids) == 0, "No timed out uids"


def test_collate_requests_sentinel():
    api = ls.test_examples.SimpleBatchedAPI(max_batch_size=2, batch_timeout=0)
    api.request_timeout = 5
    request_queue = Queue()
    request_queue.put(_SENTINEL_VALUE)
    with pytest.raises(_StopLoopError, match="Received sentinel value, stopping loop"):
        collate_requests(MagicMock(), api, request_queue, MagicMock())


class BatchSizeMismatchAPI(SimpleBatchLitAPI):
    def predict(self, x):
        assert len(x) == 2, "Expected two concurrent inputs to be batched"
        return self.model(x)  # returns a list of length same as len(x)

    def unbatch(self, output):
        return [output]  # returns a list of length 1


@pytest.mark.asyncio
async def test_batch_size_mismatch():
    api = BatchSizeMismatchAPI(max_batch_size=2, batch_timeout=4)
    api.request_timeout = 30
    api.pre_setup(spec=None)
    server = LitServer(api, accelerator="cpu", devices=1, timeout=10)

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            response1 = ac.post("/predict", json={"input": 4.0})
            response2 = ac.post("/predict", json={"input": 5.0})
            response1, response2 = await asyncio.gather(response1, response2)
        assert response1.status_code == 500
        assert response2.status_code == 500
        assert response1.json() == {"detail": "Batch size mismatch"}, "unbatch a list of length 1 when batch size is 2"
        assert response2.json() == {"detail": "Batch size mismatch"}, "unbatch a list of length 1 when batch size is 2"


def test_batch_predict_dict_warning():
    """Test that a warning is raised when predict returns a dict instead of a list."""
    api = SimpleBatchedAPI(max_batch_size=2, batch_timeout=0.1)
    api.request_timeout = 30
    api.pre_setup(spec=None)

    # Mock predict to return a dict with lists as values
    # This simulates the edge case: dict with 2 keys when batch size is 2
    api.predict = MagicMock(return_value={"class_A": [0.2, 0.3], "class_B": [0.8, 0.7]})

    mock_input = torch.tensor([[1.0], [2.0]])

    # Simulate the behavior in run_batched_loop
    y = api.predict(mock_input)
    with pytest.warns(
        UserWarning,
        match="The 'predict' method returned a dict instead of a list of predictions.",
    ):
        outputs = api.unbatch(y)
    # When list() is called on a dict, it returns the keys
    # So outputs would be ["class_A", "class_B"] which has the same length as num_inputs
    # This is the edge case we're warning about
    assert outputs == ["class_A", "class_B"]


def test_batch_predict_set_warning():
    """Test that a warning is raised when predict returns a set instead of a list."""
    api = SimpleBatchedAPI(max_batch_size=2, batch_timeout=0.1)
    api.request_timeout = 30
    api.pre_setup(spec=None)

    # Mock predict to return a set
    # This simulates the edge case: set with 2 elements when batch size is 2
    api.predict = MagicMock(return_value={1, 2})

    mock_input = torch.tensor([[1.0], [2.0]])

    # Simulate the behavior in run_batched_loop
    y = api.predict(mock_input)
    with pytest.warns(
        UserWarning,
        match="The 'predict' method returned a set instead of a list of predictions.",
    ):
        outputs = api.unbatch(y)
    # When list() is called on a set, the order is arbitrary
    # This could lead to incorrect results
    assert len(outputs) == 2
```

## File: `tests/unit/test_callbacks.py`
```python
import asyncio
import re
import time

import pytest
from asgi_lifespan import LifespanManager
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

import litserve as ls
from litserve.callbacks import CallbackRunner, EventTypes
from litserve.callbacks.defaults import PredictionTimeLogger
from litserve.callbacks.defaults.metric_callback import RequestTracker
from litserve.utils import wrap_litserve_start


async def run_simple_request(server, num_requests=1):
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            responses = [ac.post("/predict", json={"input": 4.0}) for _ in range(num_requests)]
            responses = await asyncio.gather(*responses)
            for response in responses:
                assert response.json() == {"output": 16.0}, "Unexpected response"


class SlowAPI(ls.test_examples.SimpleLitAPI):
    def predict(self, x):
        time.sleep(1)
        return super().predict(x)


def test_callback_runner():
    cb_runner = CallbackRunner()
    assert cb_runner._callbacks == [], "Callbacks list must be empty"

    cb = PredictionTimeLogger()
    cb_runner._add_callbacks(cb)
    assert cb_runner._callbacks == [cb], "Callback not added to runner"


def test_callback(capfd):
    lit_api = ls.test_examples.SimpleLitAPI()
    server = ls.LitServer(lit_api, callbacks=[PredictionTimeLogger()])

    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0})
        assert response.json() == {"output": 16.0}

    captured = capfd.readouterr()
    pattern = r"Prediction took \d+\.\d{2} seconds"
    assert re.search(pattern, captured.out), f"Expected pattern not found in output: {captured.out}"


def test_metric_logger(capfd):
    cb = PredictionTimeLogger()
    cb_runner = CallbackRunner()
    cb_runner._add_callbacks(cb)
    assert cb_runner._callbacks == [cb], "Callback not added to runner"
    cb_runner.trigger_event(EventTypes.BEFORE_PREDICT.value, lit_api=None)
    cb_runner.trigger_event(EventTypes.AFTER_PREDICT.value, lit_api=None)

    captured = capfd.readouterr()
    pattern = r"Prediction took \d+\.\d{2} seconds"
    assert re.search(pattern, captured.out), f"Expected pattern not found in output: {captured.out}"


@pytest.mark.asyncio
async def test_request_tracker(capfd):
    lit_api = SlowAPI()

    server = ls.LitServer(lit_api, track_requests=False, callbacks=[RequestTracker()])
    await run_simple_request(server, 1)
    captured = capfd.readouterr()
    assert "Active requests: None" in captured.out, f"Expected pattern not found in output: {captured.out}"

    server = ls.LitServer(lit_api, track_requests=True, callbacks=[RequestTracker()])
    await run_simple_request(server, 4)
    captured = capfd.readouterr()
    assert "Active requests: 4" in captured.out, f"Expected pattern not found in output: {captured.out}"


@pytest.mark.asyncio
async def test_request_tracker_with_spec(capfd):
    from litserve.specs.openai_embedding import OpenAIEmbeddingSpec
    from litserve.test_examples.openai_embedding_spec_example import TestEmbedAPI

    lit_api = TestEmbedAPI(spec=OpenAIEmbeddingSpec())
    server = ls.LitServer(lit_api, track_requests=True, callbacks=[RequestTracker()])

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/embeddings", json={"input": "test", "model": "test"})
            assert resp.status_code == 200

    captured = capfd.readouterr()
    assert "Active requests: 1" in captured.out, f"Expected pattern not found in output: {captured.out}"


@pytest.mark.asyncio
async def test_request_tracker_with_openai_spec(capfd):
    from litserve.specs.openai import OpenAISpec
    from litserve.test_examples.openai_spec_example import TestAPI

    lit_api = TestAPI(spec=OpenAISpec())
    server = ls.LitServer(lit_api, track_requests=True, callbacks=[RequestTracker()])

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post(
                "/v1/chat/completions", json={"messages": [{"role": "user", "content": "test"}], "model": "test"}
            )
            assert resp.status_code == 200

    captured = capfd.readouterr()
    assert "Active requests: 1" in captured.out, f"Expected pattern not found in output: {captured.out}"
```

## File: `tests/unit/test_cli.py`
```python
import os
import subprocess
import sys
from unittest.mock import MagicMock, patch

import pytest

from litserve.__main__ import main
from litserve.cli import _ensure_lightning_installed
from litserve.cli import main as cli_main


def test_dockerize_help(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["litserve", "dockerize", "--help"])
    # argparse calls sys.exit() after printing help
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "usage:" in captured.out, "CLI did not print help message"
    assert "The path to the server file." in captured.out, "CLI did not print help message"


def test_dockerize_command(monkeypatch, capsys):
    # Assuming you have a dummy server file for testing
    dummy_server_file = "dummy_server.py"
    with open(dummy_server_file, "w") as f:
        f.write("# Dummy server file for testing\n")

    monkeypatch.setattr("sys.argv", ["litserve", "dockerize", dummy_server_file])
    main()
    captured = capsys.readouterr()
    os.remove(dummy_server_file)
    assert "Dockerfile created successfully" in captured.out, "CLI did not create Dockerfile"
    assert os.path.exists("Dockerfile"), "CLI did not create Dockerfile"


@patch("litserve.cli.is_package_installed")
@patch("litserve.cli.importlib.util.find_spec")
@patch("litserve.cli.shutil.which")
@patch("subprocess.run")
def test_ensure_lightning_installed_with_pip(mock_run, mock_which, mock_find_spec, mock_is_package_installed):
    mock_is_package_installed.return_value = False
    mock_find_spec.return_value = True  # pip available
    mock_which.return_value = None  # uv not available
    _ensure_lightning_installed()
    mock_run.assert_called_once_with([sys.executable, "-m", "pip", "install", "-U", "lightning-sdk"], check=True)


@patch("litserve.cli.is_package_installed")
@patch("litserve.cli.importlib.util.find_spec")
@patch("litserve.cli.shutil.which")
@patch("subprocess.run")
def test_ensure_lightning_installed_pip_preferred(mock_run, mock_which, mock_find_spec, mock_is_package_installed):
    """When both pip and uv are available, pip should be used first."""
    mock_is_package_installed.return_value = False
    mock_find_spec.return_value = True  # pip available
    mock_which.return_value = "/usr/bin/uv"  # uv also available
    _ensure_lightning_installed()
    mock_run.assert_called_once_with([sys.executable, "-m", "pip", "install", "-U", "lightning-sdk"], check=True)


@patch("litserve.cli.is_package_installed")
@patch("litserve.cli.importlib.util.find_spec")
@patch("litserve.cli.shutil.which")
@patch("subprocess.run")
def test_ensure_lightning_installed_with_uv(mock_run, mock_which, mock_find_spec, mock_is_package_installed):
    mock_is_package_installed.return_value = False
    mock_find_spec.return_value = None  # pip not available
    mock_which.return_value = "/usr/bin/uv"  # uv available
    _ensure_lightning_installed()
    mock_run.assert_called_once_with(["uv", "pip", "install", "-U", "lightning-sdk"], check=True)


@patch("litserve.cli.is_package_installed")
@patch("litserve.cli.importlib.util.find_spec")
@patch("litserve.cli.shutil.which")
@patch("subprocess.run")
def test_ensure_lightning_installed_fallback_to_uv(mock_run, mock_which, mock_find_spec, mock_is_package_installed):
    """When pip fails, should fall back to uv."""
    mock_is_package_installed.return_value = False
    mock_find_spec.return_value = True  # pip available
    mock_which.return_value = "/usr/bin/uv"  # uv also available
    mock_run.side_effect = [subprocess.CalledProcessError(1, "pip"), None]  # pip fails, uv succeeds
    _ensure_lightning_installed()
    assert mock_run.call_count == 2
    mock_run.assert_called_with(["uv", "pip", "install", "-U", "lightning-sdk"], check=True)


@patch("litserve.cli.is_package_installed")
@patch("litserve.cli.importlib.util.find_spec")
@patch("litserve.cli.shutil.which")
@patch("subprocess.run")
def test_ensure_lightning_installed_failure(mock_run, mock_which, mock_find_spec, mock_is_package_installed):
    """When all available installers fail, should exit with error."""
    mock_is_package_installed.return_value = False
    mock_find_spec.return_value = True  # pip available
    mock_which.return_value = "/usr/bin/uv"  # uv also available
    mock_run.side_effect = subprocess.CalledProcessError(1, "install")  # both fail

    with pytest.raises(SystemExit, match="Failed to install lightning-sdk"):
        _ensure_lightning_installed()
    assert mock_run.call_count == 2  # tried both pip and uv


@patch("litserve.cli.is_package_installed")
@patch("litserve.cli.importlib.util.find_spec")
@patch("litserve.cli.shutil.which")
@patch("subprocess.run")
def test_ensure_lightning_installed_no_installer_available(
    mock_run, mock_which, mock_find_spec, mock_is_package_installed
):
    """When neither pip nor uv is available, should exit with error."""
    mock_is_package_installed.return_value = False
    mock_find_spec.return_value = None  # pip not available
    mock_which.return_value = None  # uv not available

    with pytest.raises(SystemExit, match="Failed to install lightning-sdk"):
        _ensure_lightning_installed()
    mock_run.assert_not_called()  # no installer was tried


# TODO: Remove this once we have a fix for Python 3.10
@pytest.mark.skipif(sys.version_info[:2] in [(3, 10)], reason="Test fails on Python 3.10")
@patch("litserve.cli.is_package_installed")
@patch("litserve.cli.importlib.util.find_spec")
@patch("litserve.cli.shutil.which")
@patch("subprocess.run")
@patch("builtins.__import__")
def test_cli_main_lightning_not_installed(mock_import, mock_run, mock_which, mock_find_spec, mock_is_package_installed):
    # Create a mock for the lightning_sdk module and its components
    mock_lightning_sdk = MagicMock()
    mock_lightning_sdk.cli.entrypoint.main_cli = MagicMock()

    # Configure __import__ to return our mock when lightning_sdk is imported
    def side_effect(name, *args, **kwargs):
        if name == "lightning_sdk.cli.entrypoint":
            return mock_lightning_sdk
        return __import__(name, *args, **kwargs)

    mock_import.side_effect = side_effect
    mock_find_spec.return_value = True  # pip available
    mock_which.return_value = None  # uv not available

    # Test when lightning_sdk is not installed but gets installed dynamically
    mock_is_package_installed.side_effect = [False, True]  # First call returns False, second call returns True
    test_args = ["lightning", "run", "app", "app.py"]

    with patch.object(sys, "argv", test_args):
        cli_main()

    mock_run.assert_called_once_with([sys.executable, "-m", "pip", "install", "-U", "lightning-sdk"], check=True)


@pytest.mark.skipif(sys.version_info[:2] in [(3, 10)], reason="Test fails on Python 3.10")
@patch("importlib.util.find_spec")
@patch("builtins.__import__")
def test_cli_main_import_error(mock_import, mock_find_spec, capsys):
    # Set up the mock to raise ImportError specifically for lightning_sdk import
    def import_mock(name, *args, **kwargs):
        if name == "lightning_sdk.cli.entrypoint":
            raise ImportError("Module not found")
        return __import__(name, *args, **kwargs)

    mock_import.side_effect = import_mock

    # Mock find_spec to return True so we attempt the import
    mock_find_spec.return_value = True
    test_args = ["lightning", "deploy", "api", "app.py"]

    with patch.object(sys, "argv", test_args):  # noqa: SIM117
        with pytest.raises(SystemExit) as excinfo:
            cli_main()

    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert "Error importing lightning_sdk CLI" in captured.out
```

## File: `tests/unit/test_compression.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fastapi import Request, Response
from fastapi.testclient import TestClient

from litserve import LitAPI, LitServer
from litserve.utils import wrap_litserve_start

# trivially compressible content
test_output = {"result": "0" * 100000}


class LargeOutputLitAPI(LitAPI):
    def setup(self, device):
        pass

    def decode_request(self, request: Request):
        pass

    def predict(self, x):
        pass

    def encode_response(self, output) -> Response:
        return test_output


def test_compression():
    server = LitServer(LargeOutputLitAPI(), accelerator="cpu", devices=1, workers_per_device=1)

    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        # compressed
        response = client.post("/predict", headers={"Accept-Encoding": "gzip"}, json={})
        assert response.status_code == 200
        assert response.headers["Content-Encoding"] == "gzip"
        content_length = int(response.headers["Content-Length"])
        assert 0 < content_length < 100000
        assert response.json() == test_output

        # uncompressed
        response = client.post("/predict", headers={"Accept-Encoding": ""}, json={})
        assert response.status_code == 200
        assert "Content-Encoding" not in response.headers
        content_length = int(response.headers["Content-Length"])
        assert content_length > 100000
        assert response.json() == test_output
```

## File: `tests/unit/test_connector.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from unittest.mock import patch

import pytest
import torch

from litserve.connector import _Connector, check_cuda_with_nvidia_smi


@pytest.mark.skipif(torch.cuda.device_count() == 0, reason="Only tested on Nvidia GPU")
def test_check_cuda_with_nvidia_smi():
    assert check_cuda_with_nvidia_smi() == torch.cuda.device_count()


@pytest.mark.skipif(torch.cuda.device_count() > 0, reason="Non Nvidia GPU only")
@patch(
    "litserve.connector.subprocess.check_output",
    return_value=b"GPU 0: NVIDIA GeForce RTX 4090 (UUID: GPU-rb438fre-0ar-9702-de35-ref4rjn34omk3 )",
)
def test_check_cuda_with_nvidia_smi_mock_gpu(mock_subprocess):
    check_cuda_with_nvidia_smi.cache_clear()
    assert check_cuda_with_nvidia_smi() == 1
    check_cuda_with_nvidia_smi.cache_clear()


@pytest.mark.parametrize(
    ("input_accelerator", "expected_accelerator", "expected_devices"),
    [
        ("cpu", "cpu", 1),
        pytest.param(
            "cuda",
            "cuda",
            torch.cuda.device_count(),
            marks=pytest.mark.skipif(torch.cuda.device_count() == 0, reason="Only tested on Nvidia GPU"),
        ),
        pytest.param(
            "gpu",
            "cuda",
            torch.cuda.device_count(),
            marks=pytest.mark.skipif(torch.cuda.device_count() == 0, reason="Only tested on Nvidia GPU"),
        ),
        pytest.param(
            None,
            "cuda",
            torch.cuda.device_count(),
            marks=pytest.mark.skipif(torch.cuda.device_count() == 0, reason="Only tested on Nvidia GPU"),
        ),
        pytest.param(
            "auto",
            "cuda",
            torch.cuda.device_count(),
            marks=pytest.mark.skipif(torch.cuda.device_count() == 0, reason="Only tested on Nvidia GPU"),
        ),
        pytest.param(
            "auto",
            "mps",
            1,
            marks=pytest.mark.skipif(not torch.backends.mps.is_available(), reason="Only tested on Apple MPS"),
        ),
        pytest.param(
            "gpu",
            "mps",
            1,
            marks=pytest.mark.skipif(not torch.backends.mps.is_available(), reason="Only tested on Apple MPS"),
        ),
        pytest.param(
            "mps",
            "mps",
            1,
            marks=pytest.mark.skipif(not torch.backends.mps.is_available(), reason="Only tested on Apple MPS"),
        ),
        pytest.param(
            None,
            "mps",
            1,
            marks=pytest.mark.skipif(not torch.backends.mps.is_available(), reason="Only tested on Apple MPS"),
        ),
    ],
)
def test_connector(input_accelerator, expected_accelerator, expected_devices):
    check_cuda_with_nvidia_smi.cache_clear()
    connector = _Connector(accelerator=input_accelerator)
    assert connector.accelerator == expected_accelerator, (
        f"accelerator mismatch - expected: {expected_accelerator}, actual: {connector.accelerator}"
    )

    assert connector.devices == expected_devices, (
        f"devices mismatch - expected {expected_devices}, actual: {connector.devices}"
    )

    with pytest.raises(ValueError, match="accelerator must be one of 'auto', 'cpu', 'mps', 'cuda', or 'gpu'"):
        _Connector(accelerator="SUPER_CHIP")


def test__sanitize_accelerator():
    assert _Connector._sanitize_accelerator(None) == "auto"
    assert _Connector._sanitize_accelerator("CPU") == "cpu"
    with pytest.raises(ValueError, match="accelerator must be one of 'auto', 'cpu', 'mps', 'cuda', or 'gpu'"):
        _Connector._sanitize_accelerator("SUPER_CHIP")
```

## File: `tests/unit/test_docker_builder.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pytest

import litserve as ls
from litserve import docker_builder


def test_color():
    assert docker_builder.color("hi", docker_builder.RED) == f"{docker_builder.RED}hi{docker_builder.RESET}"

    expected = f"{docker_builder.INFO} {docker_builder.RED}hi{docker_builder.RESET}"
    assert docker_builder.color("hi", docker_builder.RED, docker_builder.INFO) == expected


EXPECTED_CONENT = f"""ARG PYTHON_VERSION=3.12
FROM python:$PYTHON_VERSION-slim

####### Add your own installation commands here #######
# RUN pip install some-package
# RUN wget https://path/to/some/data/or/weights
# RUN apt-get update && apt-get install -y <package-name>

WORKDIR /app
COPY . /app

# Install litserve and requirements
RUN pip install --no-cache-dir litserve=={ls.__version__} -r requirements.txt
EXPOSE 8000
CMD ["python", "/app/app.py"]
"""


EXPECTED_GPU_DOCKERFILE = f"""# Change CUDA and cuDNN version here
FROM nvidia/cuda:12.4.1-base-ubuntu22.04
ARG PYTHON_VERSION=3.12

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \\
        software-properties-common \\
        wget \\
    && add-apt-repository ppa:deadsnakes/ppa \\
    && apt-get update && apt-get install -y --no-install-recommends \\
        python$PYTHON_VERSION \\
        python$PYTHON_VERSION-dev \\
        python$PYTHON_VERSION-venv \\
    && wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py \\
    && python$PYTHON_VERSION get-pip.py \\
    && rm get-pip.py \\
    && ln -sf /usr/bin/python$PYTHON_VERSION /usr/bin/python \\
    && ln -sf /usr/local/bin/pip$PYTHON_VERSION /usr/local/bin/pip \\
    && python --version \\
    && pip --version \\
    && apt-get purge -y --auto-remove software-properties-common \\
    && apt-get clean \\
    && rm -rf /var/lib/apt/lists/*

####### Add your own installation commands here #######
# RUN pip install some-package
# RUN wget https://path/to/some/data/or/weights
# RUN apt-get update && apt-get install -y <package-name>

WORKDIR /app
COPY . /app

# Install litserve and requirements
RUN pip install --no-cache-dir litserve=={ls.__version__} -r requirements.txt
EXPOSE 8000
CMD ["python", "/app/app.py"]
"""


def test_dockerize(tmp_path, monkeypatch):
    with open(tmp_path / "app.py", "w") as f:
        f.write("print('hello')")

    # Temporarily change the current working directory to tmp_path
    monkeypatch.chdir(tmp_path)

    with pytest.warns(UserWarning, match="Make sure to install the required packages in the Dockerfile."):
        docker_builder.dockerize("app.py", 8000)

    with open(tmp_path / "requirements.txt", "w") as f:
        f.write("lightning")

    docker_builder.dockerize("app.py", 8000)
    with open("Dockerfile") as f:
        content = f.read()
    assert content == EXPECTED_CONENT

    docker_builder.dockerize("app.py", 8000, gpu=True)
    with open("Dockerfile") as f:
        content = f.read()
    assert content == EXPECTED_GPU_DOCKERFILE

    with pytest.raises(FileNotFoundError, match="must be in the current directory"):
        docker_builder.dockerize("random_file_name.py", 8000)
```

## File: `tests/unit/test_examples.py`
```python
import pytest
import torch.nn
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

import litserve as ls
from litserve.test_examples.openai_spec_example import (
    OpenAIBatchContext,
    OpenAIBatchingWithUsage,
    OpenAIWithUsage,
    OpenAIWithUsageEncodeResponse,
)
from litserve.test_examples.simple_example import SimpleStreamAPI
from litserve.utils import wrap_litserve_start


@pytest.mark.asyncio
async def test_simple_pytorch_api():
    api = ls.test_examples.SimpleTorchAPI()
    server = ls.LitServer(api, accelerator="cpu")
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            response = await ac.post("/predict", json={"input": 4.0})
            assert response.json() == {"output": 9.0}


@pytest.mark.asyncio
async def test_simple_batched_api():
    api = ls.test_examples.SimpleBatchedAPI(max_batch_size=4, batch_timeout=0.1)
    server = ls.LitServer(api)
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            response = await ac.post("/predict", json={"input": 4.0})
            assert response.json() == {"output": 16.0}


@pytest.mark.asyncio
async def test_simple_api():
    api = ls.test_examples.SimpleLitAPI()
    server = ls.LitServer(api)
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            response = await ac.post("/predict", json={"input": 4.0})
            assert response.json() == {"output": 16.0}


@pytest.mark.asyncio
async def test_simple_api_without_server():
    api = ls.test_examples.SimpleLitAPI()
    api.setup(None)
    assert api.model is not None, "Model should be loaded after setup"
    assert api.predict(4) == 16, "Model should be able to predict"


@pytest.mark.asyncio
async def test_simple_pytorch_api_without_server():
    api = ls.test_examples.SimpleTorchAPI()
    api.setup("cpu")
    assert api.model is not None, "Model should be loaded after setup"
    assert isinstance(api.model, torch.nn.Module)
    assert api.decode_request({"input": 4}) == 4, "Request should be decoded"
    assert api.predict(torch.Tensor([4])).cpu() == 9, "Model should be able to predict"
    assert api.encode_response(9) == {"output": 9}, "Response should be encoded"


@pytest.mark.asyncio
async def test_simple_stream_api_without_server():
    api = SimpleStreamAPI()
    api.setup(None)
    assert api.model is not None, "Model should be loaded after setup"
    assert api.decode_request({"input": 4}) == 4, "Request should be decoded"
    assert list(api.predict(4)) == ["0: 4", "1: 4", "2: 4"], "Model should be able to predict"
    assert list(api.encode_response(["0: 4", "1: 4", "2: 4"])) == [
        {"output": "0: 4"},
        {"output": "1: 4"},
        {"output": "2: 4"},
    ], "Response should be encoded"


@pytest.mark.asyncio
async def test_openai_with_usage():
    api = OpenAIWithUsage()
    api.setup(None)
    response = list(api.predict("10 + 6"))
    assert response == [
        {
            "role": "assistant",
            "content": "10 + 6 is equal to 16.",
            "prompt_tokens": 25,
            "completion_tokens": 10,
            "total_tokens": 35,
        }
    ], "Response should match expected output"


@pytest.mark.asyncio
async def test_openai_with_usage_encode_response():
    api = OpenAIWithUsageEncodeResponse()
    api.setup(None)
    response = list(api.predict("10 + 6"))
    encoded_response = list(api.encode_response(response))
    assert encoded_response == [
        {"role": "assistant", "content": "10"},
        {"role": "assistant", "content": " +"},
        {"role": "assistant", "content": " "},
        {"role": "assistant", "content": "6"},
        {"role": "assistant", "content": " is"},
        {"role": "assistant", "content": " equal"},
        {"role": "assistant", "content": " to"},
        {"role": "assistant", "content": " "},
        {"role": "assistant", "content": "16"},
        {"role": "assistant", "content": "."},
        {"role": "assistant", "content": "", "prompt_tokens": 25, "completion_tokens": 10, "total_tokens": 35},
    ], "Encoded response should match expected output"


@pytest.mark.asyncio
async def test_openai_batching_with_usage():
    api = OpenAIBatchingWithUsage()
    api.setup(None)
    inputs = ["10 + 6", "10 + 6"]
    assert api.batch(inputs) == inputs, "Batched inputs should match expected output"
    batched_response = list(api.predict(inputs))
    assert batched_response == [["10 + 6 is equal to 16."] * 2], "Batched response should match expected output"
    assert api.unbatch(batched_response) == batched_response, "Unbatched response should match batched response"
    encoded_response = list(api.encode_response(batched_response, [{"temperature": 1.0}, {"temperature": 1.0}]))
    assert encoded_response == [
        [
            {"role": "assistant", "content": "10 + 6 is equal to 16."},
            {"role": "assistant", "content": "10 + 6 is equal to 16."},
        ],
        [
            {"role": "assistant", "content": "", "prompt_tokens": 25, "completion_tokens": 10, "total_tokens": 35},
            {"role": "assistant", "content": "", "prompt_tokens": 25, "completion_tokens": 10, "total_tokens": 35},
        ],
    ], "Encoded batched response should match expected output"


@pytest.mark.asyncio
async def test_openai_batch_context():
    api = OpenAIBatchContext()
    api.setup(None)
    inputs = ["Hello", "How are you?"]
    context = [{"temperature": 0.5}, {"temperature": 0.5}]

    # Test batch method
    assert api.batch(inputs) == inputs, "Batched inputs should match expected output"

    # Test predict method
    predicted_output = list(api.predict(inputs, context))
    expected_output = [
        ["Hi! "] * 2,
        ["It's "] * 2,
        ["nice "] * 2,
        ["to "] * 2,
        ["meet "] * 2,
        ["you. "] * 2,
        ["Is "] * 2,
        ["there "] * 2,
        ["something "] * 2,
        ["I "] * 2,
        ["can "] * 2,
        ["help "] * 2,
        ["you "] * 2,
        ["with "] * 2,
        ["or "] * 2,
        ["would "] * 2,
        ["you "] * 2,
        ["like "] * 2,
        ["to "] * 2,
        ["chat? "] * 2,
    ]
    assert predicted_output == expected_output, "Predicted output should match expected output"

    # Test unbatch method
    unbatched_output = api.unbatch(predicted_output)
    assert unbatched_output == predicted_output, "Unbatched output should match predicted output"

    # Test encode_response method
    encoded_response = list(api.encode_response(predicted_output, context))
    expected_encoded_response = [
        [{"role": "assistant", "content": "Hi! "}, {"role": "assistant", "content": "Hi! "}],
        [{"role": "assistant", "content": "It's "}, {"role": "assistant", "content": "It's "}],
        [{"role": "assistant", "content": "nice "}, {"role": "assistant", "content": "nice "}],
        [{"role": "assistant", "content": "to "}, {"role": "assistant", "content": "to "}],
        [{"role": "assistant", "content": "meet "}, {"role": "assistant", "content": "meet "}],
        [{"role": "assistant", "content": "you. "}, {"role": "assistant", "content": "you. "}],
        [{"role": "assistant", "content": "Is "}, {"role": "assistant", "content": "Is "}],
        [{"role": "assistant", "content": "there "}, {"role": "assistant", "content": "there "}],
        [{"role": "assistant", "content": "something "}, {"role": "assistant", "content": "something "}],
        [{"role": "assistant", "content": "I "}, {"role": "assistant", "content": "I "}],
        [{"role": "assistant", "content": "can "}, {"role": "assistant", "content": "can "}],
        [{"role": "assistant", "content": "help "}, {"role": "assistant", "content": "help "}],
        [{"role": "assistant", "content": "you "}, {"role": "assistant", "content": "you "}],
        [{"role": "assistant", "content": "with "}, {"role": "assistant", "content": "with "}],
        [{"role": "assistant", "content": "or "}, {"role": "assistant", "content": "or "}],
        [{"role": "assistant", "content": "would "}, {"role": "assistant", "content": "would "}],
        [{"role": "assistant", "content": "you "}, {"role": "assistant", "content": "you "}],
        [{"role": "assistant", "content": "like "}, {"role": "assistant", "content": "like "}],
        [{"role": "assistant", "content": "to "}, {"role": "assistant", "content": "to "}],
        [{"role": "assistant", "content": "chat? "}, {"role": "assistant", "content": "chat? "}],
    ]
    assert encoded_response == expected_encoded_response, "Encoded response should match expected output"

    # Ensure context temperatures are set to 1.0
    for ctx in context:
        assert ctx["temperature"] == 1.0, f"context {ctx} is not 1.0"
```

## File: `tests/unit/test_failed_workers.py`
```python
import multiprocessing as mp
import time

from fastapi import Request, Response

from litserve import LitAPI, LitServer


class CrashingLitAPI(LitAPI):
    """API that crashes after 2 predictions to simulate worker failure."""

    def setup(self, device):
        self.model = lambda x: x**2
        self.count = 0

    def decode_request(self, request: Request):
        return request["input"]

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output) -> Response:
        return {"output": output}


def test_worker_monitoring_triggers_shutdown_on_worker_death():
    """Test that server shuts down when a worker dies."""
    server = LitServer(CrashingLitAPI(), accelerator="cpu", devices=1, workers_per_device=1)

    # Track if shutdown was called
    shutdown_called = {"value": False}

    def mock_shutdown(manager, uvicorn_workers, shutdown_reason="normal"):
        shutdown_called["value"] = True

    manager = mp.Manager()
    server._shutdown_event = manager.Event()
    server._perform_graceful_shutdown = mock_shutdown
    ctx = mp.get_context("spawn")
    proc = ctx.Process(
        target=SystemExit,
        args=("Crash",),
        name="crashed process",
    )

    server.inference_workers = [proc]

    server._start_worker_monitoring(manager, [])

    server._start_worker_monitoring(manager, [])

    for i in range(20):
        if shutdown_called["value"]:
            break
        assert i != 19, "Server should shutdown when worker dies"
        time.sleep(1)


if __name__ == "__main__":
    test_worker_monitoring_triggers_shutdown_on_worker_death()
    print("Test passed!")
```

## File: `tests/unit/test_form.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fastapi import Request, Response
from fastapi.testclient import TestClient

from litserve import LitAPI, LitServer
from litserve.utils import wrap_litserve_start


class SimpleFileLitAPI(LitAPI):
    def setup(self, device):
        self.model = lambda x: x**2

    def decode_request(self, request: Request):
        return len(request["input"].file.read().decode("utf-8"))

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output) -> Response:
        return {"output": output}


def test_multipart_form_data(tmp_path):
    file_length = 1024 * 1024 * 100

    server = LitServer(
        SimpleFileLitAPI(), accelerator="cpu", devices=1, workers_per_device=1, max_payload_size=(file_length * 2)
    )

    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        file_path = f"{tmp_path}/big_file.txt"
        with open(file_path, "wb") as f:
            f.write(bytearray([1] * file_length))
        with open(file_path, "rb") as f:
            file = {"input": f}
            response = client.post("/predict", files=file)
            assert response.json() == {"output": file_length**2}


def test_file_too_big(tmp_path):
    file_length = 1024 * 1024 * 100

    server = LitServer(
        SimpleFileLitAPI(), accelerator="cpu", devices=1, workers_per_device=1, max_payload_size=(file_length / 2)
    )

    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        file_path = f"{tmp_path}/big_file.txt"
        with open(file_path, "wb") as f:
            f.write(bytearray([1] * file_length))
        with open(file_path, "rb") as f:
            file = {"input": f}
            response = client.post("/predict", files=file)
            assert response.status_code == 413

            # spoof content-length size
            response = client.post("/predict", files=file, headers={"content-length": "1024"})
            assert response.status_code == 413


class SimpleFormLitAPI(LitAPI):
    def setup(self, device):
        self.model = lambda x: x**2

    def decode_request(self, request: Request):
        return float(request["input"])

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output) -> Response:
        return {"output": output}


def test_urlencoded_form_data():
    server = LitServer(SimpleFormLitAPI(), accelerator="cpu", devices=1, workers_per_device=1)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        file = {"input": "4.0"}
        response = client.post("/predict", data=file)
        assert response.json() == {"output": 16.0}
```

## File: `tests/unit/test_lit_server.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import contextlib
import json
import os
import sys
import time
from time import sleep
from unittest.mock import MagicMock, patch

import pytest
import torch
import torch.nn as nn
from asgi_lifespan import LifespanManager
from fastapi import HTTPException, Request, Response
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

import litserve as ls
from litserve import LitAPI
from litserve.connector import _Connector
from litserve.server import LitServer
from litserve.utils import wrap_litserve_start


def test_index(sync_testclient):
    assert sync_testclient.get("/").text == "litserve running"


@patch("litserve.server.LitServer.lifespan")
def test_device_identifiers(lifespan_mock, simple_litapi):
    server = LitServer(simple_litapi, accelerator="cpu", devices=1, timeout=10)
    assert server.device_identifiers("cpu", 1) == ["cpu:1"]
    assert server.device_identifiers("cpu", [1, 2]) == ["cpu:1", "cpu:2"]

    server = LitServer(simple_litapi, accelerator="cpu", devices=1, timeout=10)
    assert server.devices == ["cpu"]

    server = LitServer(simple_litapi, accelerator="cuda", devices=1, timeout=10)
    assert server.devices == [["cuda:0"]]

    server = LitServer(simple_litapi, accelerator="cuda", devices=[1, 2], timeout=10)
    # [["cuda:1"], ["cuda:2"]]
    assert server.devices[0][0] == "cuda:1"
    assert server.devices[1][0] == "cuda:2"


@pytest.mark.parametrize("devices", ["cpu", ["cpu", "cuda:0"], ["cuda:a", "cuda:1"]])
def test_device_identifiers_error(simple_litapi, devices):
    with pytest.raises(
        ValueError, match="devices must be an integer or a list of integers when using 'cuda' or 'mps', instead got .*"
    ):
        LitServer(simple_litapi, accelerator="cuda", devices=devices, timeout=10)


@pytest.mark.parametrize("use_zmq", [True, False])
@pytest.mark.asyncio
async def test_stream(simple_stream_api, use_zmq):
    simple_stream_api.stream = True
    server = LitServer(simple_stream_api, timeout=10, fast_queue=use_zmq)
    expected_output1 = "prompt=Hello generated_output=LitServe is streaming output".lower().replace(" ", "")
    expected_output2 = "prompt=World generated_output=LitServe is streaming output".lower().replace(" ", "")

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            # TODO: remove this sleep when we have a better way to check if the server is ready
            # TODO: main process can only consume when response_queue_to_buffer is ready
            await asyncio.sleep(4)
            resp1 = ac.post("/predict", json={"prompt": "Hello"}, timeout=10)
            resp2 = ac.post("/predict", json={"prompt": "World"}, timeout=10)
            resp1, resp2 = await asyncio.gather(resp1, resp2)
            assert resp1.status_code == 200, "Check if server is running and the request format is valid."
            assert resp1.text == expected_output1, (
                "Server returns input prompt and generated output which didn't match."
            )
            assert resp2.status_code == 200, "Check if server is running and the request format is valid."
            assert resp2.text == expected_output2, (
                "Server returns input prompt and generated output which didn't match."
            )


@pytest.mark.parametrize("use_zmq", [True, False])
@pytest.mark.asyncio
async def test_batched_stream_server(simple_batched_stream_api, use_zmq):
    api = simple_batched_stream_api
    api.stream = True
    api.max_batch_size = 4
    api.batch_timeout = 2
    server = LitServer(api, timeout=30, fast_queue=use_zmq)
    expected_output1 = "Hello LitServe is streaming output".lower().replace(" ", "")
    expected_output2 = "World LitServe is streaming output".lower().replace(" ", "")

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp1 = ac.post("/predict", json={"prompt": "Hello"}, timeout=10)
            resp2 = ac.post("/predict", json={"prompt": "World"}, timeout=10)
            resp1, resp2 = await asyncio.gather(resp1, resp2)
            assert resp1.status_code == 200, "Check if server is running and the request format is valid."
            assert resp2.status_code == 200, "Check if server is running and the request format is valid."
            assert resp1.text == expected_output1, (
                "Server returns input prompt and generated output which didn't match."
            )
            assert resp2.text == expected_output2, (
                "Server returns input prompt and generated output which didn't match."
            )


def test_litapi_with_stream(simple_litapi_cls):
    with pytest.raises(
        ValueError,
        match="""When `stream=True` both `lit_api.predict` and
             `lit_api.encode_response` must generate values using `yield""",
    ):
        # TODO: The error should be raised in the LitAPI constructor
        LitServer(simple_litapi_cls(stream=True))


class Linear(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)
        self.linear.weight.data.fill_(2.0)
        self.linear.bias.data.fill_(1.0)

    def forward(self, x):
        return self.linear(x)


class SimpleLitAPI(LitAPI):
    def setup(self, device):
        self.model = Linear().to(device)
        self.device = device

    def decode_request(self, request: Request):
        content = request["input"]
        return torch.tensor([content], device=self.device)

    def predict(self, x):
        return self.model(x[None, :])

    def encode_response(self, output) -> Response:
        return {"output": float(output)}


@pytest.mark.parametrize(
    ("input_accelerator", "expected_accelerator"),
    [
        ("cpu", "cpu"),
        pytest.param(
            "cuda",
            "cuda",
            marks=pytest.mark.skipif(torch.cuda.device_count() == 0, reason="Only tested on Nvidia GPU"),
        ),
        pytest.param(
            None, "cuda", marks=pytest.mark.skipif(torch.cuda.device_count() == 0, reason="Only tested on Nvidia GPU")
        ),
        pytest.param(
            "auto",
            "cuda",
            marks=pytest.mark.skipif(torch.cuda.device_count() == 0, reason="Only tested on Nvidia GPU"),
        ),
        pytest.param(
            "auto",
            "mps",
            marks=pytest.mark.skipif(not torch.backends.mps.is_available(), reason="Only tested on Apple MPS"),
        ),
        pytest.param(
            None,
            "mps",
            marks=pytest.mark.skipif(not torch.backends.mps.is_available(), reason="Only tested on Apple MPS"),
        ),
    ],
)
def test_auto_accelerator(input_accelerator, expected_accelerator):
    server = LitServer(SimpleLitAPI(), devices=1, timeout=10, accelerator=input_accelerator)
    assert server._connector.accelerator == expected_accelerator


def test_mocked_accelerator():
    # 1. cuda available
    with patch("litserve.connector.check_cuda_with_nvidia_smi", return_value=True):
        connector = _Connector(accelerator="auto")
        assert connector.accelerator == "cuda"

    # 2. mps available
    with patch("litserve.connector._Connector._choose_gpu_accelerator_backend", return_value="mps"):
        server = LitServer(SimpleLitAPI(), devices=1, timeout=10, accelerator="auto")
        assert server._connector.accelerator == "mps"


@patch("litserve.server.uvicorn")
def test_server_run(mock_uvicorn, mock_manager):
    server = LitServer(SimpleLitAPI())
    server.verify_worker_status = MagicMock()
    with pytest.raises(ValueError, match="port must be a value from 1024 to 65535 but got"):
        server.run(port="invalid port")

    with pytest.raises(ValueError, match="port must be a value from 1024 to 65535 but got"):
        server.run(port=65536)

    with pytest.raises(ValueError, match="host must be '0.0.0.0', '127.0.0.1', or '::' but got"):
        server.run(host="127.0.0.2")

    # test port 8000
    with patch("litserve.server.mp.Manager", return_value=mock_manager):
        server.run(port=8000)
    mock_uvicorn.Config.assert_called()
    mock_uvicorn.reset_mock()

    # test port 8001
    with patch("litserve.server.mp.Manager", return_value=mock_manager):
        server.run(port="8001")
    mock_uvicorn.Config.assert_called()

    # test host "::" and port 8000
    with patch("litserve.server.mp.Manager", return_value=mock_manager):
        server.run(host="::", port="8000")
    mock_uvicorn.Config.assert_called()


@pytest.mark.skipif(sys.platform == "win32", reason="Test is only for Unix")
@patch("litserve.server._Server")
def test_start_server(mock_server):
    api = ls.test_examples.TestAPI(spec=ls.OpenAISpec())
    server = LitServer(api)
    sockets = MagicMock()
    server._start_server(8000, 1, "info", sockets, "process")
    mock_server.assert_called()
    assert server.lit_api.spec.response_queue_id is not None, "response_queue_id must be generated"


@pytest.fixture
def server_for_api_worker_test(simple_litapi):
    server = ls.LitServer(simple_litapi, devices=1)
    server.verify_worker_status = MagicMock()
    server.launch_inference_worker = MagicMock(return_value=[MagicMock()])
    server._start_server = MagicMock()
    server._transport = MagicMock()
    return server


@pytest.mark.skipif(sys.platform == "win32", reason="Test is only for Unix")
@patch("litserve.server.uvicorn")
def test_server_run_with_api_server_worker_type(mock_uvicorn, server_for_api_worker_test, mock_manager):
    server = server_for_api_worker_test

    with patch("litserve.server.mp.Manager", return_value=mock_manager):
        server.run(api_server_worker_type="process", num_api_servers=10)
    server.launch_inference_worker.assert_called_with(server.lit_api)


@pytest.mark.skipif(sys.platform == "win32", reason="Test is only for Unix")
@pytest.mark.parametrize(("api_server_worker_type", "num_api_workers"), [(None, 1), ("process", 1)])
@patch("litserve.server.uvicorn")
def test_server_run_with_process_api_worker(
    mock_uvicorn, api_server_worker_type, num_api_workers, server_for_api_worker_test, mock_manager
):
    server = server_for_api_worker_test

    with patch("litserve.server.mp.Manager", return_value=mock_manager):
        server.run(api_server_worker_type=api_server_worker_type, num_api_workers=num_api_workers)
    server.launch_inference_worker.assert_called_with(server.lit_api)
    actual = server._start_server.call_args
    assert actual[0][4] == "process", "Server should run in process mode"
    mock_uvicorn.Config.assert_called()


@pytest.mark.skipif(sys.platform == "win32", reason="Test is only for Unix")
@patch("litserve.server.uvicorn")
def test_server_run_with_thread_api_worker(mock_uvicorn, server_for_api_worker_test, mock_manager):
    server = server_for_api_worker_test
    with patch("litserve.server.mp.Manager", return_value=mock_manager):
        server.run(api_server_worker_type="thread")
    server.launch_inference_worker.assert_called_with(server.lit_api)
    assert server._start_server.call_args[0][4] == "thread", "Server should run in thread mode"
    mock_uvicorn.Config.assert_called()


@pytest.mark.skipif(sys.platform == "win32", reason="Test is only for Unix")
def test_server_run_with_invalid_api_worker(simple_litapi):
    server = ls.LitServer(simple_litapi, devices=1)
    server.verify_worker_status = MagicMock()
    with pytest.raises(ValueError, match=r"Must be 'process' or 'thread'"):
        server.run(api_server_worker_type="invalid")

    with pytest.raises(ValueError, match=r"must be greater than 0"):
        server.run(num_api_servers=0)


@pytest.mark.skipif(sys.platform != "win32", reason="Test is only for Windows")
@patch("litserve.server.uvicorn")
def test_server_run_windows(mock_uvicorn, mock_manager):
    api = ls.test_examples.SimpleLitAPI()
    server = ls.LitServer(api)
    server.verify_worker_status = MagicMock()
    server.launch_inference_worker = MagicMock(return_value=[MagicMock()])
    server._transport = MagicMock()
    server._start_server = MagicMock()

    with patch("litserve.server.mp.Manager", return_value=mock_manager):
        server.run(api_server_worker_type=None)
    actual = server._start_server.call_args
    assert actual[0][4] == "thread", "Windows only supports thread mode"


def test_server_terminate():
    server = LitServer(SimpleLitAPI())
    server.verify_worker_status = MagicMock()
    server._transport = MagicMock()

    with (
        patch("litserve.server.LitServer._init_manager", return_value=MagicMock()) as mock_init_manager,
        patch("litserve.server.LitServer._start_server", side_effect=Exception("mocked error")) as mock_start,
        patch("litserve.server.LitServer.launch_inference_worker", return_value=([MagicMock()])) as mock_launch,
    ):
        with pytest.raises(Exception, match="mocked error"):
            server.run(port=8001)

        mock_init_manager.assert_called()
        mock_launch.assert_called()
        mock_start.assert_called()
        server._transport.close.assert_called()


@pytest.mark.parametrize(("disable_openapi_url", "should_print"), [(False, True), (True, False)])
@patch("builtins.print")
@patch("litserve.server.uvicorn")
def test_disable_openapi_url_print_message(mock_uvicorn, mock_print, mock_manager, disable_openapi_url, should_print):
    """Test that the Swagger UI message is only printed when disable_openapi_url=False."""
    server = LitServer(SimpleLitAPI(), disable_openapi_url=disable_openapi_url, restart_workers=False)
    server.verify_worker_status = MagicMock()

    with (
        patch("litserve.server.mp.Manager", return_value=mock_manager),
        contextlib.suppress(Exception),
    ):
        server._monitor_workers = False
        server.run(port=8000)

    if should_print:
        mock_print.assert_called_with("Swagger UI is available at http://0.0.0.0:8000/docs")
    else:
        mock_print.assert_not_called()


class IdentityAPI(ls.test_examples.SimpleLitAPI):
    def predict(self, x, context):
        context["input"] = x
        return self.model(x)

    def encode_response(self, output, context):
        input = context["input"]
        return {"output": input}


class IdentityBatchedAPI(ls.test_examples.SimpleBatchedAPI):
    def predict(self, x_batch, context):
        for c, x in zip(context, x_batch):
            c["input"] = x
        return self.model(x_batch)

    def encode_response(self, output, context):
        input = context["input"]
        return {"output": input}


class IdentityBatchedStreamingAPI(ls.test_examples.SimpleBatchedAPI):
    def predict(self, x_batch, context):
        for c, x in zip(context, x_batch):
            c["input"] = x
        yield self.model(x_batch)

    def encode_response(self, output_stream, context):
        for _ in output_stream:
            yield [{"output": ctx["input"]} for ctx in context]


class PredictErrorAPI(ls.test_examples.SimpleLitAPI):
    def predict(self, x, y, context):
        context["input"] = x
        return self.model(x)

    def encode_response(self, output, context):
        input = context["input"]
        return {"output": input}


@pytest.mark.asyncio
async def test_inject_context():
    # Test context injection with single loop
    api = IdentityAPI()
    server = LitServer(api)
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/predict", json={"input": 5.0}, timeout=10)
    assert resp.json()["output"] == 5.0, "output from Identity server must be same as input"

    # Test context injection with batched loop
    server = LitServer(IdentityBatchedAPI(max_batch_size=2, batch_timeout=0.01))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/predict", json={"input": 5.0}, timeout=10)
    assert resp.json()["output"] == 5.0, "output from Identity server must be same as input"

    # Test context injection with batched streaming loop
    server = LitServer(IdentityBatchedStreamingAPI(max_batch_size=2, batch_timeout=0.01, stream=True))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/predict", json={"input": 5.0}, timeout=10)
    assert resp.json()["output"] == 5.0, "output from Identity server must be same as input"

    server = LitServer(PredictErrorAPI())
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        resp = client.post("/predict", json={"input": 5.0}, timeout=10)
        assert resp.status_code == 500, "predict() missed 1 required positional argument: 'y'"


def test_custom_api_path():
    with pytest.raises(ValueError, match="api_path must start with '/'"):
        LitServer(ls.test_examples.SimpleLitAPI(api_path="predict"))

    server = LitServer(ls.test_examples.SimpleLitAPI(api_path="/v1/predict"))
    assert "/v1/predict" in [route.path for route in server.app.routes]


def test_custom_healthcheck_path():
    with pytest.raises(ValueError, match="healthcheck_path must start with '/'. "):
        LitServer(ls.test_examples.SimpleLitAPI(), healthcheck_path="customhealth")

    server = LitServer(ls.test_examples.SimpleLitAPI(), healthcheck_path="/v1/custom_health")
    url = server.healthcheck_path
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        # Sleep a bit to ensure the server is ready
        sleep(3)
        response = client.get(url)

    assert response.status_code == 200, "Server response should be 200 (OK)"


def test_custom_info_path():
    with pytest.raises(ValueError, match="info_path must start with '/'. "):
        LitServer(ls.test_examples.SimpleLitAPI(), info_path="custominfo")

    server = LitServer(ls.test_examples.SimpleLitAPI(), info_path="/v1/custom_info", accelerator="cpu")
    url = server.info_path
    expected_response = {
        "model": None,
        "server": {
            "devices": ["cpu"],
            "workers_per_device": 1,
            "timeout": 30,
            "stream": {"/predict": False},
            "max_payload_size": None,
            "track_requests": False,
        },
    }

    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        # Sleep a bit to ensure the server is ready
        sleep(3)
        response = client.get(url)

    assert response.status_code == 200, "Server response should be 200 (OK)"
    assert response.json() == expected_response, "server didn't return expected output"


def test_info_route():
    model_metadata = {"name": "my-awesome-model", "version": "v1.1.0"}
    expected_response = {
        "model": {
            "name": "my-awesome-model",
            "version": "v1.1.0",
        },
        "server": {
            "devices": ["cpu"],
            "workers_per_device": 1,
            "timeout": 30,
            "stream": {"/predict": False},
            "max_payload_size": None,
            "track_requests": False,
        },
    }

    server = ls.LitServer(ls.test_examples.SimpleLitAPI(), accelerator="cpu", model_metadata=model_metadata)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.get("/info", headers={"Host": "localhost"})
        assert response.status_code == 200, f"Expected response to be 200 but got {response.status_code}"
        assert response.json() == expected_response, "server didn't return expected output"


def test_model_metadata_json_error():
    with pytest.raises(ValueError, match="model_metadata must be JSON serializable"):
        ls.LitServer(ls.test_examples.SimpleLitAPI(), model_metadata=int)


class TestHTTPExceptionAPI(ls.test_examples.SimpleLitAPI):
    def decode_request(self, request):
        raise HTTPException(501, "decode request is bad")


class TestHTTPExceptionAPI2(ls.test_examples.SimpleLitAPI):
    def decode_request(self, request):
        raise HTTPException(status_code=400, detail="decode request is bad")


def test_http_exception():
    server = LitServer(TestHTTPExceptionAPI(), fast_queue=True)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0})
        assert response.status_code == 501, "Server raises 501 error"
        assert response.text == '{"detail":"decode request is bad"}', "decode request is bad"

    server = LitServer(TestHTTPExceptionAPI2(), fast_queue=True)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0})
        assert response.status_code == 400, "Server raises 400 error"
        assert response.text == '{"detail":"decode request is bad"}', "decode request is bad"


def test_generate_client_file(tmp_path, monkeypatch):
    expected = """import requests

response = requests.post("http://127.0.0.1:8123/predict", json={"input": 4.0})
print(f"Status: {response.status_code}\\nResponse:\\n {response.text}")"""
    monkeypatch.chdir(tmp_path)
    LitServer.generate_client_file(8123)
    with open(tmp_path / "client.py") as fr:
        assert expected in fr.read(), f"Expected {expected} in client.py"

    LitServer.generate_client_file(8000)
    with open(tmp_path / "client.py") as fr:
        assert expected in fr.read(), "Shouldn't replace existing client.py"


class FailFastAPI(ls.test_examples.SimpleLitAPI):
    def setup(self, device):
        raise ValueError("setup failed")


@pytest.mark.parametrize("use_zmq", [True, False])
def test_workers_setup_status(use_zmq, port):
    server = LitServer(
        FailFastAPI(),
        fast_queue=use_zmq,
    )
    with pytest.raises(RuntimeError, match="One or more workers failed to start. Shutting down LitServe"):
        server.run(port=port, log_level="error")


def test_max_batch_size_warning(simple_litapi):
    # Remove this test after v0.3.0
    with pytest.warns(DeprecationWarning, match="'max_batch_size' and 'batch_timeout' are being deprecated"):
        ls.LitServer(simple_litapi, max_batch_size=4)


class TestAsyncLitAPI(ls.LitAPI):
    def setup(self, device):
        self.model = None

    async def decode_request(self, request):
        return request["input"]

    async def predict(self, x):
        return x**2

    async def encode_response(self, output):
        return {"output": output}


@pytest.mark.asyncio
async def test_async_litapi():
    api = TestAsyncLitAPI(enable_async=True)
    server = LitServer(api)
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/predict", json={"input": 5.0}, timeout=10)
            assert resp.status_code == 200, "Server response should be 200 (OK)"
            assert resp.json()["output"] == 25.0, "output from Identity server must be same as input"


class TestSleepAsyncLitAPI(TestAsyncLitAPI):
    async def predict(self, x):
        # simulate a long-running task
        await asyncio.sleep(4)
        return x**2


@pytest.mark.asyncio
@pytest.mark.parametrize("num_requests", [10, 50, 100])
async def test_concurrent_async_inference(num_requests):
    """Test that async API processes requests concurrently (not sequentially)."""
    api = TestSleepAsyncLitAPI(enable_async=True)
    server = LitServer(api)
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            sleep(2)  # Sleep a bit to ensure the server is ready

            tasks = [ac.post("/predict", json={"input": 5.0}, timeout=10) for _ in range(num_requests)]
            start = time.perf_counter()
            responses = await asyncio.gather(*tasks)
            elapsed = time.perf_counter() - start

            for resp in responses:
                assert resp.status_code == 200
                assert resp.json()["output"] == 25.0

            # All requests should finish in just over 4s, plus some overhead
            assert elapsed < 4 + 4, f"Expected all requests to finish in just over 4s, but took {elapsed:.2f}s."


class TestHTTPExceptionAsyncLitAPI(TestAsyncLitAPI):
    async def decode_request(self, request):
        raise HTTPException(status_code=501, detail="decode request is bad")


@pytest.mark.asyncio
async def test_error_propagation_in_async_litapi():
    server = LitServer(TestHTTPExceptionAsyncLitAPI(enable_async=True))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/predict", json={"input": 5.0}, timeout=10)
            assert resp.status_code == 501, "Server raises 501 error"
            assert resp.json() == {"detail": "decode request is bad"}, "decode request is bad"


class TestAsyncStreamLitAPI(ls.LitAPI):
    def setup(self, device):
        self.model = lambda x: x

    async def decode_request(self, request):
        return request["input"]

    async def predict(self, x):
        for i in range(5):
            yield self.model(i)

    async def encode_response(self, output_stream):
        async for output in output_stream:
            yield {"output": output}


@pytest.mark.asyncio
async def test_async_stream_litapi():
    api = TestAsyncStreamLitAPI(enable_async=True, stream=True)
    server = LitServer(api)
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/predict", json={"input": 4.0}, timeout=10)
            assert resp.status_code == 200, "Server response should be 200 (OK)"
            chunks = []
            async for line in resp.aiter_lines():
                if line.strip():
                    chunks.append(json.loads(line)["output"])
            assert len(chunks) == 5, "Expected 5 chunks of output"
            assert chunks == list(range(5)), "Expected output to be a sequence of integers from 0 to 4"


class TestSleepAsyncStreamLitAPI(TestAsyncStreamLitAPI):
    async def predict(self, x):
        for i in range(5):
            await asyncio.sleep(0.5)  # Simulate streaming delay
            yield i


@pytest.mark.asyncio
@pytest.mark.parametrize("num_requests", [100])
async def test_concurrent_async_streaming_inference(num_requests):
    api = TestSleepAsyncStreamLitAPI(enable_async=True, stream=True)
    server = LitServer(api)
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            sleep(2)  # Sleep a bit to ensure the server is ready

            # Prepare concurrent streaming requests using the parameterized num_requests
            tasks = [ac.post("/predict", json={"input": 4.0}, timeout=10) for _ in range(num_requests)]
            start = time.perf_counter()
            responses = await asyncio.gather(*tasks)
            elapsed = time.perf_counter() - start

            # Collect and check streamed outputs for each response
            for resp in responses:
                assert resp.status_code == 200, "Server response should be 200 (OK)"
                chunks = []
                async for line in resp.aiter_lines():
                    if line.strip():
                        chunks.append(json.loads(line)["output"])
                assert len(chunks) == 5, "Expected 5 chunks of output"
                assert chunks == list(range(5)), "Expected output to be a sequence of integers from 0 to 4"

            # All requests should finish in just over the streaming time for one request
            assert elapsed < 4 + 4, (
                f"Expected all requests to finish in just over 4s, plus some overhead, but took {elapsed:.2f}s."
            )


class FailingLitAPI(LitAPI):
    def setup(self, device):
        worker_id = os.environ.get("LITSERVE_WORKER_ID", "0")
        print(f"Worker {worker_id} setup successfully on {device}")

    def decode_request(self, request):
        return request["input"]

    def predict(self, x):
        if x == 0:
            os._exit(1)  # This will terminate the worker process
        return int(os.environ.get("LITSERVE_WORKER_ID", "0"))

    def encode_response(self, output):
        return {"output": output}


@pytest.mark.skipif(sys.platform == "win32", reason="Test is only for Unix")
@pytest.mark.asyncio
async def test_worker_restart_and_server_shutdown():
    api = FailingLitAPI()
    server = LitServer(
        api,
        accelerator="cpu",
        devices=1,
        workers_per_device=2,
        restart_workers=True,
    )
    server.monitor_internal = 0.5

    with wrap_litserve_start(server, worker_monitor=True) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/predict", json={"input": 0}, timeout=2)
            assert resp.status_code == 500

            # Increased wait time for macOS where process spawning is slower
            await asyncio.sleep(5 if sys.platform == "darwin" else 2)

            tasks = []
            for _ in range(50):
                tasks.append(asyncio.create_task(ac.post("/predict", json={"input": 1})))

            responses = await asyncio.gather(*tasks, return_exceptions=True)

            worker_0_count = 0
            worker_1_count = 0

            for response in responses:
                assert response.status_code == 200
                output = response.json()
                print(output)
                if output["output"] == 0:
                    worker_0_count += 1
                else:
                    worker_1_count += 1

            assert worker_0_count > 0
            assert worker_1_count > 0


class FailingLitAPIStreaming(LitAPI):
    def setup(self, device):
        worker_id = os.environ.get("LITSERVE_WORKER_ID", "0")
        print(f"Worker {worker_id} setup successfully on {device}")

    def decode_request(self, request):
        yield request["input"]

    def predict(self, x):
        for value in x:
            if value == 0:
                os._exit(1)  # This will terminate the worker process
            yield value

    def encode_response(self, output):
        for value in output:
            yield {"output": float(value)}


@pytest.mark.asyncio
async def test_worker_restart_and_server_shutdown_streaming():
    api = FailingLitAPIStreaming()
    server = LitServer(
        api,
        accelerator="cpu",
        devices=1,
        workers_per_device=2,
        restart_workers=True,
        stream=True,
    )
    server.monitor_internal = 0.5

    with wrap_litserve_start(server, worker_monitor=True) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/predict", json={"input": 0})
            assert resp.status_code == 200


class MultiRouteAPI(ls.test_examples.SimpleLitAPI):
    # Mock API for testing multi-route server behavior
    def __init__(self, api_path="/predict"):
        super().__init__(api_path=api_path)


@pytest.mark.skipif(sys.platform == "win32", reason="Test is only for Unix")
@pytest.mark.parametrize(
    ("workers_cfg", "expected_total_by_path"),
    [
        # dict: explicit per-route config
        ({"/sentiment": 2, "/generate": 3}, {"/sentiment": 4, "/generate": 6}),
        # list: per-api (connector order) config
        ([2, 3], {"/sentiment": 4, "/generate": 6}),
    ],
)
def test_workers_per_device_can_be_configured_per_route(monkeypatch, workers_cfg, expected_total_by_path):
    monkeypatch.setattr("litserve.server.uvicorn", MagicMock())

    sentiment = MultiRouteAPI(api_path="/sentiment")
    generate = MultiRouteAPI(api_path="/generate")
    server = LitServer([sentiment, generate], accelerator="cuda", devices=[0, 1], workers_per_device=workers_cfg)

    created = []  # list[(api_path, worker_id, device)]

    class FakeProcess:
        def __init__(self, target, args, name):
            # inference_worker args = (lit_api, device, worker_id, request_q, transport, ...)
            lit_api, device, worker_id = args[0], args[1], args[2]
            created.append((lit_api.api_path, worker_id, device))
            self.pid = 123
            self.name = name

        def start(self): ...
        def terminate(self): ...
        def join(self, timeout=None): ...
        def is_alive(self):
            return False

        def kill(self): ...

    class FakeCtx:
        def Process(self, target, args, name):  # noqa: N802
            return FakeProcess(target=target, args=args, name=name)

    monkeypatch.setattr("litserve.server.mp.get_context", lambda *_args, **_kwargs: FakeCtx())

    # prevent server.run() from actually running uvicorn / waiting forever
    server.verify_worker_status = MagicMock()
    server._start_server = MagicMock(return_value={})
    server._perform_graceful_shutdown = MagicMock()
    server._start_worker_monitoring = MagicMock()
    server._transport = MagicMock()
    server._shutdown_event = MagicMock()
    server._shutdown_event.wait = MagicMock(return_value=None)  # don't block

    # init manager + queues without real multiprocessing manager
    with patch("litserve.server.mp.Manager", return_value=MagicMock()):
        server.run(api_server_worker_type="process", generate_client_file=False)

    # count workers created per api_path
    total_by_path = {}
    for api_path, _worker_id, _device in created:
        total_by_path[api_path] = total_by_path.get(api_path, 0) + 1

    assert total_by_path == expected_total_by_path


@pytest.mark.skipif(sys.platform == "win32", reason="Test is only for Unix")
def test_workers_per_device_per_route_raises_on_unknown_route():
    sentiment = MultiRouteAPI(api_path="/sentiment")
    generate = MultiRouteAPI(api_path="/generate")

    with pytest.raises(ValueError, match="workers_per_device.*unknown api_path"):
        LitServer(
            [sentiment, generate],
            accelerator="cuda",
            devices=[0, 1],
            workers_per_device={"/sentiment": 2, "/unknown": 1},
        )


@patch("litserve.server.LitServer.lifespan")
def test_health_check_returns_503_when_workers_setup_status_is_empty(lifespan_mock, simple_litapi):
    """Health check should return 503 when no workers are registered yet.

    This tests the fix for the bug where `all({}.values())` returns True in Python, causing the health check to
    incorrectly return 200 when workers_setup_status is empty.

    """
    server = LitServer(simple_litapi, accelerator="cpu", devices=1, timeout=10)
    # Ensure workers_setup_status is empty (simulating server startup before workers register)
    server.workers_setup_status = {}

    # Override the lifespan context to avoid starting workers
    @contextlib.asynccontextmanager
    async def mock_lifespan(app):
        yield {}

    server.app.router.lifespan_context = mock_lifespan

    with TestClient(server.app) as client:
        response = client.get("/health")
        assert response.status_code == 503, "Health check should return 503 when no workers are registered"
        assert response.text == "not ready"
```

## File: `tests/unit/test_litapi.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
import time

import numpy as np
import pytest
import torch
from fastapi import HTTPException
from pydantic import BaseModel

import litserve as ls
from litserve.specs.openai import ChatCompletionRequest


class TestDefaultBatchedAPI(ls.LitAPI):
    def setup(self, device) -> None:
        self.model = lambda x: len(x)

    def decode_request(self, request):
        return request["input"]

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output):
        return {"output": output}


class TestCustomBatchedAPI(TestDefaultBatchedAPI):
    def batch(self, inputs):
        return np.stack(inputs)

    def unbatch(self, output):
        return list(output)


class TestStreamAPI(ls.LitAPI):
    def setup(self, device) -> None:
        self.model = None

    def decode_request(self, request):
        return request["input"]

    def predict(self, x):
        # x is a list of integers
        for i in range(4):
            yield np.asarray(x) * i

    def encode_response(self, output_stream):
        for output in output_stream:
            output = list(output)
            yield [{"output": o} for o in output]


def test_default_batch_unbatch():
    api = TestDefaultBatchedAPI(max_batch_size=4)
    api.request_timeout = 30
    api.pre_setup(spec=None)
    inputs = [1, 2, 3, 4]
    output = api.batch(inputs)
    assert output == inputs, "Default batch should not change input"
    assert api.unbatch(output) == inputs, "Default unbatch should not change input"


def test_default_unbatch_not_implemented():
    api = TestDefaultBatchedAPI()
    with pytest.raises(ValueError, match="Default implementation for `LitAPI.unbatch` method was not found."):
        api.unbatch(None)


class TestStreamAPIBatched(TestStreamAPI):
    def predict(self, x):
        for i in range(4):
            yield np.asarray(x) * i


def test_default_batch_unbatch_stream():
    api = TestStreamAPIBatched(max_batch_size=4)
    api.request_timeout = 30
    api.stream = True
    api.pre_setup(spec=None)
    inputs = [1, 2, 3, 4]
    expected_output = [[0, 0, 0, 0], [1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]
    output = api.batch(inputs)
    output = api.predict(output)
    for out in api.unbatch(output):
        expected = expected_output.pop(0)
        assert np.all(out == expected), f"Default unbatch should not change input {out} != {expected}"


def test_custom_batch_unbatch():
    api = TestCustomBatchedAPI(max_batch_size=4)
    api.request_timeout = 30
    api.pre_setup(spec=None)
    inputs = [1, 2, 3, 4]
    output = api.batch(inputs)
    assert np.all(output == np.array(inputs)), "Custom batch stacks input as numpy array"
    assert api.unbatch(output) == inputs, "Custom unbatch should unstack input as list"


def test_batch_unbatch_stream():
    api = TestStreamAPI(max_batch_size=4)
    api.request_timeout = 30
    api.pre_setup(spec=None)
    inputs = [1, 2, 3, 4]
    output = api.batch(inputs)
    output = api.predict(output)
    output = api.unbatch(output)
    output = api.encode_response(output)
    first_resp = [o["output"] for o in next(output)]
    expected_outputs = [[0, 0, 0, 0], [1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]
    assert first_resp == expected_outputs[0], "First response should be 0s"
    count = 1
    for out, expected_output in zip(output, expected_outputs[1:]):
        resp = [o["output"] for o in out]
        assert resp == expected_output
        count += 1

    assert count == 4, "Should have 4 responses"


def test_decode_request():
    request = {"input": 4.0}
    api = ls.test_examples.SimpleLitAPI()
    assert api.decode_request(request) == 4.0, "Decode request should return the input 4.0"


def test_decode_request_with_openai_spec():
    api = ls.test_examples.TestAPI(max_batch_size=1)
    api.request_timeout = 30
    api.pre_setup(spec=ls.OpenAISpec())
    request = ChatCompletionRequest(messages=[{"role": "system", "content": "Hello"}])
    decoded_request = api.decode_request(request)
    assert decoded_request.messages[0].content == "Hello", "Decode request should return the input message"


def test_encode_response():
    response = 4.0
    api = ls.test_examples.SimpleLitAPI()
    assert api.encode_response(response) == {"output": 4.0}, 'Encode response returns encoded output {"output": 4.0}'


def test_encode_response_with_openai_spec():
    api = ls.test_examples.TestAPI(max_batch_size=1)
    api.request_timeout = 30
    api.pre_setup(spec=ls.OpenAISpec())
    response = ["This", "is", "a", "LLM", "generated", "text"]
    generated_tokens = []
    for output in api.encode_response(response):
        generated_tokens.append(output["content"])
    assert generated_tokens == response, f"Encode response should return the generated tokens {response}"


def test_encode_response_with_openai_spec_dict_token_usage():
    prompt = "This is a LLM generated text"

    def predict():
        for token in prompt.split():
            yield {"content": token, "prompt_tokens": 4, "completion_tokens": 4, "total_tokens": 8}

    generated_tokens = []
    api = ls.test_examples.TestAPI(max_batch_size=1)
    api.request_timeout = 30
    api.pre_setup(spec=ls.OpenAISpec())

    for output in api.encode_response(predict()):
        assert output["role"] == "assistant", "Role should be assistant"
        generated_tokens.append(output["content"])
    assert generated_tokens == prompt.split(), f"Encode response should return the generated tokens {prompt.split()}"


def test_encode_response_with_custom_spec_api():
    class CustomSpecAPI(ls.OpenAISpec):
        def encode_response(self, output_stream):
            for output in output_stream:
                yield {"content": output}

    api = ls.test_examples.TestAPI(max_batch_size=1)
    api.request_timeout = 30
    api.pre_setup(spec=CustomSpecAPI())
    response = ["This", "is", "a", "LLM", "generated", "text"]
    generated_tokens = []
    for output in api.encode_response(response):
        generated_tokens.append(output["content"])
    assert generated_tokens == response, f"Encode response should return the generated tokens {response}"


def test_encode_response_with_openai_spec_invalid_input():
    api = ls.test_examples.TestAPI(max_batch_size=1)
    api.request_timeout = 30
    api.pre_setup(spec=ls.OpenAISpec())
    response = 10
    with pytest.raises(TypeError, match="object is not iterable"):
        next(api.encode_response(response))


def test_encode_response_with_openai_spec_invalid_predict_output():
    def predict():
        yield {"hello": "world"}

    api = ls.test_examples.TestAPI(max_batch_size=1)
    api.request_timeout = 30
    api.pre_setup(spec=ls.OpenAISpec())
    with pytest.raises(HTTPException, match=r"Malformed output from LitAPI.predict"):
        next(api.encode_response(predict()))


def test_format_encoded_response():
    api = ls.test_examples.SimpleLitAPI()
    sample = {"output": 4.0}
    msg = "Format encoded response should return the encoded response as a string"
    assert api.format_encoded_response(sample) == '{"output": 4.0}\n', msg

    class Sample(BaseModel):
        output: float
        name: str

    sample = Sample(output=4.0, name="test")
    msg = "Format encoded response should return the encoded response as a json string"
    assert json.loads(api.format_encoded_response(sample)) == {"output": 4.0, "name": "test"}, msg

    msg = "non dict and non Pydantic objects are returned as it is."
    assert api.format_encoded_response([1, 2, 3, 4]) == [1, 2, 3, 4], msg


def test_batch_torch():
    api = ls.test_examples.SimpleLitAPI()
    x = [torch.Tensor([1, 2, 3, 4]), torch.Tensor([5, 6, 7, 8])]
    assert torch.all(api.batch(x) == torch.stack(x)), "Batch should stack torch tensors"


def test_batch_numpy():
    api = ls.test_examples.SimpleLitAPI()
    x = [np.asarray([1, 2, 3, 4]), np.asarray([5, 6, 7, 8])]
    assert np.all(api.batch(x) == np.stack(x)), "Batch should stack Numpy array"


def test_device_property():
    api = ls.test_examples.SimpleLitAPI()
    api.device = "cpu"
    assert api.device == "cpu"


class TestLogger(ls.Logger):
    def process(self, key, value):
        self.processed_data = (key, value)


def test_log():
    api = ls.test_examples.SimpleLitAPI()
    api.request_timeout = 30
    assert api._logger_queue is None, "Logger queue should be None"
    assert api.log("time", 0.1) is None, "Log should return None"
    with pytest.warns(UserWarning, match="attempted without a configured logger"):
        api.log("time", 0.1)

    api = ls.test_examples.SimpleLitAPI()
    api.request_timeout = 30
    assert api._logger_queue is None, "Logger queue should be None"
    server = ls.LitServer(api, loggers=TestLogger())
    server._init_manager(1)
    server._logger_connector.run(server)
    server.launch_inference_worker(api)
    api.log("time", 0.1)
    assert server.logger_queue.get() == ("time", 0.1)


def test_enable_async_not_set():
    with pytest.raises(
        ValueError, match=r"predict must be an async generator or async function when enable_async=True"
    ):
        ls.test_examples.SimpleLitAPI(enable_async=True)


class HeavyInitAPI(ls.LitAPI):
    def __init__(self):
        super().__init__()
        time.sleep(2)


class HeavyInitAPIWithSetup(HeavyInitAPI):
    def setup(self, device):
        pass


class HeavySetupAPI(ls.LitAPI):
    def setup(self, device):
        time.sleep(2)


def test_heavy_init_api_no_setup():
    with pytest.warns(RuntimeWarning, match="loading a model or doing other heavy processing inside the constructor"):
        HeavyInitAPI()


def test_heavy_init_api_with_setup(recwarn):
    HeavyInitAPIWithSetup()

    assert len(recwarn) == 0


def test_heavy_setup_api(recwarn):
    api = HeavySetupAPI()
    api.setup("")

    assert len(recwarn) == 0
```

## File: `tests/unit/test_logger.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import threading
import time
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

import litserve as ls
from litserve.loggers import Logger, _LoggerConnector
from litserve.utils import wrap_litserve_start


class TestLogger(Logger):
    def process(self, key, value):
        self.processed_data = (key, value)


@pytest.fixture
def mock_lit_server():
    mock_server = MagicMock()
    mock_server.log_queue.get = MagicMock(return_value=("test_key", "test_value"))
    return mock_server


@pytest.fixture
def test_logger():
    return TestLogger()


@pytest.fixture
def logger_connector(mock_lit_server, test_logger):
    return _LoggerConnector(mock_lit_server, [test_logger])


def test_logger_mount(test_logger):
    mock_app = MagicMock()
    test_logger.mount("/test", mock_app)
    assert test_logger._config["mount"]["path"] == "/test"
    assert test_logger._config["mount"]["app"] == mock_app


def test_connector_add_logger(logger_connector):
    new_logger = TestLogger()
    logger_connector.add_logger(new_logger)
    assert new_logger in logger_connector._loggers


def test_connector_mount(mock_lit_server, test_logger, logger_connector):
    mock_app = MagicMock()
    test_logger.mount("/test", mock_app)
    logger_connector.add_logger(test_logger)
    mock_lit_server.app.mount.assert_called_with("/test", mock_app)


def test_invalid_loggers():
    _LoggerConnector(None, TestLogger())
    with pytest.raises(ValueError, match="Logger must be an instance of litserve.Logger"):
        _ = _LoggerConnector(None, [MagicMock()])

    with pytest.raises(ValueError, match="loggers must be a list or an instance of litserve.Logger"):
        _ = _LoggerConnector(None, MagicMock())


class LoggerAPI(ls.test_examples.SimpleLitAPI):
    def predict(self, input):
        result = super().predict(input)
        for i in range(1, 5):
            self.log("time", i * 0.1)
        return result


def test_server_wo_logger():
    api = LoggerAPI()
    server = ls.LitServer(api)

    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0})
        assert response.json() == {"output": 16.0}


class FileLogger(ls.Logger):
    def __init__(self, path="test_logger_temp.txt"):
        super().__init__()
        self.path = path

    def process(self, key, value):
        with open(self.path, "a+") as f:
            f.write(f"{key}: {value:.1f}\n")


def test_logger_with_api(tmpdir):
    path = str(tmpdir / "test_logger_temp.txt")
    api = LoggerAPI()
    server = ls.LitServer(api, loggers=[FileLogger(path)])
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0})
        assert response.json() == {"output": 16.0}
        # Wait for FileLogger to write to file
        time.sleep(0.5)
        with open(path) as f:
            data = f.readlines()
            assert data == [
                "time: 0.1\n",
                "time: 0.2\n",
                "time: 0.3\n",
                "time: 0.4\n",
            ], f"Expected metric not found in logger file {data}"


class PredictionTimeLogger(ls.Callback):
    def on_after_predict(self, lit_api):
        for i in range(1, 5):
            lit_api.log("time", i * 0.1)


def test_logger_with_callback(tmp_path):
    path = str(tmp_path / "test_logger_temp.txt")
    api = ls.test_examples.SimpleLitAPI()
    server = ls.LitServer(api, loggers=[FileLogger(path)], callbacks=[PredictionTimeLogger()])
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0})
        assert response.json() == {"output": 16.0}
        # Wait for FileLogger to write to file
        time.sleep(0.5)
        with open(path) as f:
            data = f.readlines()
            assert data == [
                "time: 0.1\n",
                "time: 0.2\n",
                "time: 0.3\n",
                "time: 0.4\n",
            ], f"Expected metric not found in logger file {data}"


class NonPickleableLogger(ls.Logger):
    # This is a logger that contains a non-picklable resource
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._lock = threading.Lock()  # Non-picklable resource

    def process(self, key, value):
        with self._lock:
            print(f"Logged {key}: {value}", flush=True)


class PickleTestAPI(ls.test_examples.SimpleLitAPI):
    def predict(self, x):
        self.log("my-key", x)
        return super().predict(x)


def test_pickle_safety(capfd):
    api = PickleTestAPI()
    server = ls.LitServer(api, loggers=NonPickleableLogger())
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0})
        assert response.json() == {"output": 16.0}
        time.sleep(0.5)
        captured = capfd.readouterr()
        assert "Logged my-key: 4.0" in captured.out, f"Expected log not found in captured output {captured}"
```

## File: `tests/unit/test_logging.py`
```python
import io
import logging

import pytest

from litserve.utils import add_log_handler, configure_logging, set_log_level


@pytest.fixture
def log_stream():
    return io.StringIO()


def test_configure_logging(log_stream):
    # Configure logging with test stream
    configure_logging(level=logging.DEBUG, stream=log_stream)

    # Get logger and log a test message
    logger = logging.getLogger("litserve")
    test_message = "Test debug message"
    logger.debug(test_message)

    # Verify log output
    log_contents = log_stream.getvalue()
    assert test_message in log_contents
    assert "DEBUG" in log_contents
    assert logger.propagate is False


def test_set_log_level():
    # Set log level to WARNING
    set_log_level(logging.WARNING)

    # Verify logger level
    logger = logging.getLogger("litserve")
    assert logger.level == logging.WARNING


def test_add_log_handler():
    # Create and add a custom handler
    stream = io.StringIO()
    custom_handler = logging.StreamHandler(stream)
    add_log_handler(custom_handler)

    # Verify handler is added
    logger = logging.getLogger("litserve")
    assert custom_handler in logger.handlers

    # Test the handler works
    test_message = "Test handler message"
    logger.info(test_message)
    assert test_message in stream.getvalue()


@pytest.fixture(autouse=True)
def cleanup_logger():
    yield
    logger = logging.getLogger("litserve")
    logger.handlers.clear()
    logger.setLevel(logging.INFO)
```

## File: `tests/unit/test_loops.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import contextlib
import inspect
import io
import json
import re
import threading
import time
from collections.abc import AsyncGenerator
from queue import Empty, Queue
from typing import Optional
from unittest.mock import ANY, MagicMock, patch

import pytest
from asgi_lifespan import LifespanManager
from fastapi import HTTPException
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

import litserve as ls
from litserve import LitAPI
from litserve.callbacks import CallbackRunner
from litserve.loops import BatchedStreamingLoop, LitLoop, Output, StreamingLoop, inference_worker
from litserve.loops.base import (
    _SENTINEL_VALUE,
    DefaultLoop,
    _async_inject_context,
    _handle_async_function,
    _sync_fn_to_async_fn,
)
from litserve.loops.continuous_batching_loop import (
    ContinuousBatchingLoop,
    notify_timed_out_requests,
)
from litserve.loops.simple_loops import BatchedLoop, SingleLoop
from litserve.specs.base import LitSpec
from litserve.test_examples.openai_spec_example import OpenAIBatchingWithUsage
from litserve.transport import MPQueueTransport
from litserve.transport.base import MessageTransport
from litserve.utils import LitAPIStatus, LoopResponseType, wrap_litserve_start

NOOP_CB_RUNNER = CallbackRunner()


class MockMPQueueTransport(MPQueueTransport):
    def __init__(self, num_consumers=1):
        self._closed = False
        self._mp_terminate_event = None
        self._queues = [Queue() for _ in range(num_consumers)]


@pytest.fixture
def mock_transport():
    return MockMPQueueTransport()


@pytest.fixture
def loop_args():
    requests_queue = Queue()
    requests_queue.put((0, "uuid-123", time.monotonic(), 1))  # response_queue_id, uid, timestamp, x_enc
    requests_queue.put((1, "uuid-234", time.monotonic(), 2))

    lit_api_mock = MagicMock()
    lit_api_mock.request_timeout = 1
    lit_api_mock.decode_request = MagicMock(side_effect=lambda x: x["input"])
    return lit_api_mock, requests_queue


class TestQueue(Queue):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sentinel_seen = False

    def get(self, timeout=None):
        if self._sentinel_seen:
            raise Empty  # Simulate queue being empty after sentinel
        item = super().get(timeout=timeout)
        # Sentinel: (None, None, None, None)
        if item == _SENTINEL_VALUE:
            self._sentinel_seen = True
            raise KeyboardInterrupt  # Triggers loop exit in your code
        return item


class AsyncTestLitAPI(LitAPI):
    def setup(self, device):
        pass

    async def decode_request(self, request):
        return request["input"]

    async def predict(self, x):
        return x**2

    async def encode_response(self, output):
        return {"output": output}


@pytest.fixture
def async_loop_args():
    requests_queue = TestQueue()
    requests_queue.put((0, "uuid-123", time.monotonic(), {"input": 1}))
    requests_queue.put((1, "uuid-234", time.monotonic(), {"input": 2}))
    requests_queue.put(_SENTINEL_VALUE)

    lit_api = AsyncTestLitAPI()
    return lit_api, requests_queue


class DummyMessageTransport(MessageTransport):
    def send(self, item, consumer_id, block=True, timeout=None):
        raise StopIteration("exit loop")

    async def areceive(self, timeout: Optional[int] = None, consumer_id: Optional[int] = None) -> dict:
        pass


def test_single_loop(loop_args):
    lit_api_mock, requests_queue = loop_args
    lit_api_mock.unbatch.side_effect = None
    transport = DummyMessageTransport()

    lit_loop = SingleLoop()
    with pytest.raises(StopIteration, match="exit loop"):
        lit_loop.run_single_loop(lit_api_mock, requests_queue, transport, callback_runner=NOOP_CB_RUNNER)


@pytest.mark.asyncio
async def test_single_loop_process_single_async_request(async_loop_args, mock_transport):
    lit_api_mock, requests_queue = async_loop_args

    # Get a request from the queue (already populated by the fixture)
    request = requests_queue.get()
    loop = SingleLoop()
    await loop._process_single_request(
        request,
        lit_api_mock,
        mock_transport,
        NOOP_CB_RUNNER,
    )
    response = await mock_transport.areceive(consumer_id=request[0])
    expected_output = request[3]["input"] ** 2
    assert response == (
        request[1],
        ({"output": expected_output}, ls.utils.LitAPIStatus.OK, ls.utils.LoopResponseType.REGULAR, ANY),
    )


def test_run_single_loop_with_async(async_loop_args, monkeypatch):
    mock_transport = MockMPQueueTransport(num_consumers=2)
    lit_api_mock, requests_queue = async_loop_args

    loop = SingleLoop()
    loop._restart_workers = True

    # Patch kill to do nothing in test
    monkeypatch.setattr(loop, "kill", lambda: None)

    # Expected to break the loop in test
    with contextlib.suppress(KeyboardInterrupt):
        loop._run_single_loop_with_async(lit_api_mock, requests_queue, mock_transport, NOOP_CB_RUNNER)

    response = asyncio.run(mock_transport.areceive(consumer_id=0))
    assert response == ("uuid-123", ((), "START", ls.utils.LoopResponseType.REGULAR, ANY))
    response = asyncio.run(mock_transport.areceive(consumer_id=0))
    assert response == ("uuid-123", ({"output": 1}, ls.utils.LitAPIStatus.OK, ls.utils.LoopResponseType.REGULAR, ANY))
    response = asyncio.run(mock_transport.areceive(consumer_id=1))
    assert response == ("uuid-234", ((), "START", ls.utils.LoopResponseType.REGULAR, ANY))
    response = asyncio.run(mock_transport.areceive(consumer_id=1))
    assert response == ("uuid-234", ({"output": 4}, ls.utils.LitAPIStatus.OK, ls.utils.LoopResponseType.REGULAR, ANY))


class FakeStreamSender(DummyMessageTransport):
    def __init__(self, num_streamed_outputs):
        super().__init__()
        self.num_streamed_outputs = num_streamed_outputs
        self.count = 0

    def send(self, item, consumer_id, block=False, timeout=None):
        uid, args = item
        response, status, response_type, worker_id = args
        if status == LitAPIStatus.START:
            return

        if self.count >= self.num_streamed_outputs:
            raise StopIteration("exit loop")
        assert response == f"{self.count}", "This streaming loop generates number from 0 to 9 which is sent via Queue"
        assert response_type == LoopResponseType.STREAMING, "Streaming loop must return streaming response"
        self.count += 1


def test_streaming_loop():
    num_streamed_outputs = 10

    def fake_predict(inputs: str):
        for i in range(num_streamed_outputs):
            yield {"output": f"{i}"}

    def fake_encode(output):
        assert inspect.isgenerator(output), "predict function must be a generator when `stream=True`"
        for out in output:
            yield out["output"]

    fake_stream_api = MagicMock()
    fake_stream_api.request_timeout = 1
    fake_stream_api.decode_request = MagicMock(side_effect=lambda x: x["prompt"])
    fake_stream_api.predict = MagicMock(side_effect=fake_predict)
    fake_stream_api.encode_response = MagicMock(side_effect=fake_encode)
    fake_stream_api.format_encoded_response = MagicMock(side_effect=lambda x: x)

    requests_queue = Queue()
    requests_queue.put((0, "UUID-1234", time.monotonic(), {"prompt": "Hello"}))
    transport = FakeStreamSender(num_streamed_outputs)

    lit_loop = StreamingLoop()
    with pytest.raises(StopIteration, match="exit loop"):
        lit_loop.run_streaming_loop(
            fake_stream_api,
            requests_queue,
            transport,
            callback_runner=NOOP_CB_RUNNER,
        )

    fake_stream_api.predict.assert_called_once_with("Hello")
    fake_stream_api.encode_response.assert_called_once()


class AsyncTestStreamLitAPI(LitAPI):
    def setup(self, device) -> None:
        pass

    async def decode_request(self, request):
        return request["input"]

    async def predict(self, x):
        for i in range(x):
            yield {"output": i}

    async def encode_response(self, output):
        async for out in output:
            yield out["output"]


@pytest.mark.asyncio
async def test_streaming_loop_process_streaming_request(mock_transport):
    request = (0, "UUID-1234", time.monotonic(), {"input": 5})

    lit_api = AsyncTestStreamLitAPI()
    loop = StreamingLoop()
    await loop._process_streaming_request(
        request,
        lit_api,
        mock_transport,
        NOOP_CB_RUNNER,
    )

    for i in range(5):
        response = await mock_transport.areceive(consumer_id=request[0])
        assert response == (
            request[1],
            (i, ls.utils.LitAPIStatus.OK, ls.utils.LoopResponseType.STREAMING, ANY),
        )


def test_run_streaming_loop_with_async(mock_transport, monkeypatch):
    requests_queue = TestQueue()
    requests_queue.put((0, "uuid-123", time.monotonic(), {"input": 5}))
    requests_queue.put(_SENTINEL_VALUE)  # Sentinel to stop the loop

    lit_api = AsyncTestStreamLitAPI()
    loop = StreamingLoop()
    loop._restart_workers = True

    # Patch kill to do nothing in test
    monkeypatch.setattr(loop, "kill", lambda: None)

    # Expected to break the loop in test
    with contextlib.suppress(KeyboardInterrupt):
        loop.run_streaming_loop_async(lit_api, requests_queue, mock_transport, NOOP_CB_RUNNER)

    for i in range(6):
        response = asyncio.run(mock_transport.areceive(consumer_id=0))
        if i == 0:
            assert response == (
                "uuid-123",
                (((), "START", ls.utils.LoopResponseType.STREAMING, ANY)),
            )
        else:
            assert response == (
                "uuid-123",
                (i - 1, ls.utils.LitAPIStatus.OK, ls.utils.LoopResponseType.STREAMING, ANY),
            )


class FakeBatchStreamTransport(DummyMessageTransport):
    def __init__(self, num_streamed_outputs):
        super().__init__()
        self.num_streamed_outputs = num_streamed_outputs
        self.count = 0

    def send(self, item, consumer_id=0, block=False, timeout=None):
        uid, args = item
        response, status, response_type, worker_id = args
        if status == LitAPIStatus.START:
            return

        if status == LitAPIStatus.FINISH_STREAMING:
            raise StopIteration("interrupt iteration")
        if status == LitAPIStatus.ERROR:
            assert self.count // 2 == self.num_streamed_outputs, (
                f"Loop count must have incremented for {self.num_streamed_outputs} times."
            )
            raise StopIteration("finish streaming")

        assert response == f"{self.count // 2}", (
            f"streaming loop generates number from 0 to 9 which is sent via Queue. {args}, count:{self.count}"
        )
        assert response_type == LoopResponseType.STREAMING, "Streaming loop must return streaming response"
        self.count += 1


def test_batched_streaming_loop(mock_transport):
    num_streamed_outputs = 10

    def fake_predict(inputs: list):
        n = len(inputs)
        assert n == 2, "Two requests has been simulated to batched."
        for i in range(num_streamed_outputs):
            yield [{"output": f"{i}"}] * n

    def fake_encode(output_iter):
        assert inspect.isgenerator(output_iter), "predict function must be a generator when `stream=True`"
        for outputs in output_iter:
            yield [output["output"] for output in outputs]

    fake_stream_api = MagicMock()
    fake_stream_api.request_timeout = 1
    fake_stream_api.decode_request = MagicMock(side_effect=lambda x: x["prompt"])
    fake_stream_api.batch = MagicMock(side_effect=lambda inputs: inputs)
    fake_stream_api.predict = MagicMock(side_effect=fake_predict)
    fake_stream_api.encode_response = MagicMock(side_effect=fake_encode)
    fake_stream_api.unbatch = MagicMock(side_effect=lambda inputs: inputs)
    fake_stream_api.format_encoded_response = MagicMock(side_effect=lambda x: x)
    fake_stream_api.max_batch_size = 2
    fake_stream_api.batch_timeout = 2

    requests_queue = Queue()
    requests_queue.put((0, "UUID-001", time.monotonic(), {"prompt": "Hello"}))
    requests_queue.put((0, "UUID-002", time.monotonic(), {"prompt": "World"}))

    lit_loop = BatchedStreamingLoop()
    transport = FakeBatchStreamTransport(num_streamed_outputs)
    with pytest.raises(StopIteration, match="finish streaming"):
        lit_loop.run_batched_streaming_loop(
            fake_stream_api,
            requests_queue,
            transport=transport,
            callback_runner=NOOP_CB_RUNNER,
        )
    fake_stream_api.predict.assert_called_once_with(["Hello", "World"])
    fake_stream_api.encode_response.assert_called_once()


@patch("litserve.loops.simple_loops.BatchedLoop.run_batched_loop")
@patch("litserve.loops.simple_loops.SingleLoop.run_single_loop")
def test_inference_worker(mock_single_loop, mock_batched_loop):
    lit_api_mock = MagicMock()
    lit_api_mock.max_batch_size = 2
    lit_api_mock.batch_timeout = 0
    lit_api_mock.enable_async = False
    lit_api_mock.stream = False
    lit_api_mock.api_path = "/predict"
    lit_api_mock.loop = "auto"

    inference_worker(
        lit_api_mock,
        "cpu",
        0,
        MagicMock(),
        MagicMock(),
        workers_setup_status={},
        callback_runner=NOOP_CB_RUNNER,
        restart_workers=True,
    )
    mock_batched_loop.assert_called_once()

    lit_api_mock = MagicMock()
    lit_api_mock.max_batch_size = 1
    lit_api_mock.batch_timeout = 0
    lit_api_mock.enable_async = False
    lit_api_mock.stream = False
    lit_api_mock.api_path = "/predict"
    lit_api_mock.loop = "auto"

    inference_worker(
        lit_api_mock,
        "cpu",
        0,
        MagicMock(),
        MagicMock(),
        workers_setup_status={},
        callback_runner=NOOP_CB_RUNNER,
        restart_workers=True,
    )
    mock_single_loop.assert_called_once()


@pytest.mark.asyncio
async def test_run_single_loop(mock_transport):
    lit_api = ls.test_examples.SimpleLitAPI()
    lit_api.setup(None)
    lit_api.request_timeout = 1

    request_queue = Queue()
    request_queue.put((0, "UUID-001", time.monotonic(), {"input": 4.0}))
    transport = mock_transport

    # Run the loop in a separate thread to allow it to be stopped
    lit_loop = SingleLoop()
    lit_loop._restart_workers = True
    loop_thread = threading.Thread(
        target=lit_loop.run_single_loop, args=(lit_api, request_queue, transport, NOOP_CB_RUNNER)
    )
    loop_thread.start()

    # Allow some time for the loop to process
    time.sleep(1)

    # Stop the loop by putting a sentinel value in the queue
    request_queue.put(_SENTINEL_VALUE)
    loop_thread.join()

    response = await transport.areceive(consumer_id=0)
    response = await transport.areceive(consumer_id=0)
    assert response == ("UUID-001", ({"output": 16.0}, LitAPIStatus.OK, LoopResponseType.REGULAR, ANY))


@pytest.mark.asyncio
async def test_run_single_loop_timeout():
    stream = io.StringIO()
    ls.configure_logging(stream=stream)

    lit_api = ls.test_examples.SimpleLitAPI()
    lit_api.setup(None)
    lit_api.request_timeout = 0.0001

    request_queue = Queue()
    transport = MockMPQueueTransport()
    old_request = (0, "UUID-001", time.monotonic(), {"input": 4.0})
    time.sleep(0.1)  # Age the request
    request_queue.put(old_request)

    lit_loop = SingleLoop()
    lit_loop._restart_workers = True
    loop_thread = threading.Thread(
        target=lit_loop.run_single_loop, args=(lit_api, request_queue, transport, NOOP_CB_RUNNER)
    )
    loop_thread.start()

    _, (response, status, _, _) = await transport.areceive(consumer_id=0)
    _, (response, status, _, _) = await transport.areceive(consumer_id=0)
    assert isinstance(response, HTTPException)
    assert response.status_code == 504
    assert "Request UUID-001 was waiting in the queue for too long" in stream.getvalue()

    request_queue.put(_SENTINEL_VALUE)
    loop_thread.join()


@pytest.mark.asyncio
async def test_run_batched_loop():
    lit_api = ls.test_examples.SimpleBatchedAPI()
    lit_api.setup(None)
    lit_api.max_batch_size = 2
    lit_api.batch_timeout = 1
    lit_api.request_timeout = 1
    lit_api.pre_setup(spec=None)

    request_queue = Queue()
    transport = MockMPQueueTransport(1)

    requests = [(0, "UUID-001", time.monotonic(), {"input": 4.0}), (0, "UUID-002", time.monotonic(), {"input": 5.0})]
    for req in requests:
        request_queue.put(req)

    lit_loop = BatchedLoop()
    lit_loop._restart_workers = True
    loop_thread = threading.Thread(
        target=lit_loop.run_batched_loop,
        args=(lit_api, request_queue, transport, NOOP_CB_RUNNER),
    )
    loop_thread.start()

    expected_responses = [
        ("UUID-001", ({"output": 16.0}, LitAPIStatus.OK, LoopResponseType.REGULAR, ANY)),
        ("UUID-002", ({"output": 25.0}, LitAPIStatus.OK, LoopResponseType.REGULAR, ANY)),
    ]

    await transport.areceive(0, timeout=10)
    await transport.areceive(0, timeout=10)

    for expected in expected_responses:
        actual = await transport.areceive(0, timeout=10)
        assert actual == expected, f"Expected {expected}, got {actual}"

    request_queue.put(_SENTINEL_VALUE)
    loop_thread.join()


@pytest.mark.asyncio
async def test_run_batched_loop_timeout(mock_transport):
    stream = io.StringIO()
    ls.configure_logging(stream=stream)

    lit_api = ls.test_examples.SimpleBatchedAPI()
    lit_api.setup(None)
    lit_api.max_batch_size = 2
    lit_api.batch_timeout = 0.001
    lit_api.request_timeout = 0.1
    lit_api.pre_setup(spec=None)

    request_queue = Queue()
    transport = mock_transport

    # First request will time out, second will succeed
    requests = [
        (0, "UUID-001", time.monotonic() - 0.2, {"input": 4.0}),  # Old request
        (0, "UUID-002", time.monotonic(), {"input": 5.0}),  # Fresh request
    ]
    for req in requests:
        request_queue.put(req)

    lit_loop = BatchedLoop()
    lit_loop._restart_workers = True
    loop_thread = threading.Thread(
        target=lit_loop.run_batched_loop,
        args=(lit_api, request_queue, transport, NOOP_CB_RUNNER),
    )
    loop_thread.start()

    await transport.areceive(0, timeout=10)
    await transport.areceive(0, timeout=10)

    # First response should be timeout error
    _, (response1, _, _, _) = await transport.areceive(0, timeout=10)
    assert isinstance(response1, HTTPException)
    assert "Request UUID-001 was waiting in the queue for too long" in stream.getvalue()

    # Second response should succeed
    _, (response2, _, _, _) = await transport.areceive(consumer_id=0, timeout=10)
    assert response2 == {"output": 25.0}

    request_queue.put(_SENTINEL_VALUE)
    loop_thread.join()


@pytest.mark.asyncio
async def test_run_streaming_loop(mock_transport):
    lit_api = ls.test_examples.SimpleStreamAPI()
    lit_api.setup(None)
    lit_api.request_timeout = 1

    request_queue = Queue()
    request_queue.put((0, "UUID-001", time.monotonic(), {"input": "Hello"}))

    # Run the loop in a separate thread to allow it to be stopped
    lit_loop = StreamingLoop()
    lit_loop._restart_workers = True
    loop_thread = threading.Thread(
        target=lit_loop.run_streaming_loop, args=(lit_api, request_queue, mock_transport, NOOP_CB_RUNNER)
    )
    loop_thread.start()

    # Allow some time for the loop to process
    time.sleep(1)

    # Stop the loop by putting a sentinel value in the queue
    request_queue.put(_SENTINEL_VALUE)
    loop_thread.join()

    await mock_transport.areceive(0, timeout=10)

    for i in range(3):
        response = await mock_transport.areceive(0, timeout=10)
        response = json.loads(response[1][0])
        assert response == {"output": f"{i}: Hello"}


@pytest.mark.asyncio
async def test_run_streaming_loop_timeout(mock_transport):
    stream = io.StringIO()
    ls.configure_logging(stream=stream)
    lit_api = ls.test_examples.SimpleStreamAPI()
    lit_api.setup(None)
    lit_api.request_timeout = 0.1

    request_queue = Queue()
    request_queue.put((0, "UUID-001", time.monotonic() - 5, {"input": "Hello"}))

    # Run the loop in a separate thread to allow it to be stopped
    lit_loop = StreamingLoop()
    lit_loop._restart_workers = True
    loop_thread = threading.Thread(
        target=lit_loop.run_streaming_loop, args=(lit_api, request_queue, mock_transport, NOOP_CB_RUNNER)
    )
    loop_thread.start()

    # Allow some time for the loop to process
    time.sleep(1)

    # Stop the loop by putting a sentinel value in the queue
    request_queue.put(_SENTINEL_VALUE)
    loop_thread.join()

    assert "Request UUID-001 was waiting in the queue for too long" in stream.getvalue()
    response = await mock_transport.areceive(0, timeout=10)
    response = await mock_transport.areceive(0, timeout=10)
    assert isinstance(response[1][0], HTTPException), "request was timed out"


def off_test_run_batched_streaming_loop(openai_request_data):
    lit_api = OpenAIBatchingWithUsage()
    lit_api.setup(None)
    lit_api.request_timeout = 1
    lit_api.stream = True
    lit_api.max_batch_size = 2
    lit_api.batch_timeout = 0.1
    spec = ls.OpenAISpec()
    lit_api.pre_setup(spec=spec, timeout=30)

    request_queue = Queue()
    # response_queue_id, uid, timestamp, x_enc
    r1 = (0, "UUID-001", time.monotonic(), openai_request_data)
    r2 = (0, "UUID-002", time.monotonic(), openai_request_data)
    request_queue.put(r1)
    request_queue.put(r2)
    response_queues = [Queue()]

    # Run the loop in a separate thread to allow it to be stopped
    lit_loop = BatchedStreamingLoop()
    lit_loop._restart_workers = True
    loop_thread = threading.Thread(
        target=lit_loop.run_batched_streaming_loop,
        args=(lit_api, spec, request_queue, response_queues, NOOP_CB_RUNNER),
    )
    loop_thread.start()

    # Allow some time for the loop to process
    time.sleep(1)

    # Stop the loop by putting a sentinel value in the queue
    request_queue.put(_SENTINEL_VALUE)
    loop_thread.join()

    response = response_queues[0].get(timeout=5)[1]
    assert response[0] == {"role": "assistant", "content": "10 + 6 is equal to 16."}


class TestLoop(LitLoop):
    def __call__(
        self,
        lit_api: LitAPI,
        device: str,
        worker_id: int,
        request_queue: Queue,
        transport: MessageTransport,
        workers_setup_status: dict[int, str],
        callback_runner: CallbackRunner,
    ):
        try:
            self.run(
                lit_api,
                device,
                worker_id,
                request_queue,
                transport,
                workers_setup_status,
                callback_runner,
            )
        except StopIteration as e:
            return e

    def run(
        self,
        lit_api: LitAPI,
        device: str,
        worker_id: int,
        request_queue: Queue,
        transport: MessageTransport,
        workers_setup_status: dict[int, str],
        callback_runner: CallbackRunner,
    ):
        item = request_queue.get()
        if item is None:
            return

        response_queue_id, uid, timestamp, x_enc = item
        cache = lit_api.load_cache(x_enc)
        x = lit_api.decode_request(x_enc) * cache
        response = lit_api.predict(x)
        response_enc = lit_api.encode_response(response)
        transport.send(
            (uid, (response_enc, LitAPIStatus.OK, LoopResponseType.REGULAR, ANY)), consumer_id=response_queue_id
        )
        raise StopIteration("exit loop")


@pytest.mark.asyncio
async def test_custom_loop(mock_transport):
    loop = TestLoop()
    lit_api = MagicMock(request_timeout=1)
    lit_api.load_cache = MagicMock(return_value=1.0)
    lit_api.encode_response = MagicMock(return_value={"output": 16.0})
    request_queue = Queue()
    request_queue.put((0, "UUID-001", time.monotonic(), {"input": 4.0}))

    loop(lit_api, "cpu", 0, request_queue, mock_transport, {}, NOOP_CB_RUNNER)
    response = await mock_transport.areceive(0)
    assert response[0] == "UUID-001"
    assert response[1][0] == {"output": 16.0}
    lit_api.load_cache.assert_called_once()
    lit_api.load_cache.assert_called_with({"input": 4.0})


class TestLitAPI(ls.test_examples.SimpleLitAPI):
    def load_cache(self, x):
        return 10


@pytest.mark.asyncio
@pytest.mark.parametrize("fast_queue", [True, False])
async def test_loop_with_server_async(fast_queue):
    loop = TestLoop()
    loop._restart_workers = True
    lit_api = TestLitAPI()
    server = ls.LitServer(lit_api, loop=loop, fast_queue=fast_queue)

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            response = await ac.post("/predict", json={"input": 4.0}, timeout=5)
            assert response.json() == {"output": 1600.0}


def test_loop_with_server_sync():
    loop = TestLoop()
    loop._restart_workers = True
    lit_api = TestLitAPI()
    server = ls.LitServer(lit_api, loop=loop, fast_queue=True)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0}, timeout=5)
        assert response.json() == {"output": 1600.0}  # use LitAPI.load_cache to multiply the input by 10


def test_get_default_loop():
    lit_api = MagicMock()
    lit_api.stream = False
    lit_api.max_batch_size = 1
    loop = ls.loops.get_default_loop(lit_api.stream, lit_api.max_batch_size)
    loop._restart_workers = True
    assert isinstance(loop, ls.loops.SingleLoop), "SingleLoop must be returned when stream=False"

    lit_api = MagicMock()
    lit_api.stream = False
    lit_api.max_batch_size = 4
    loop = ls.loops.get_default_loop(lit_api.stream, lit_api.max_batch_size)
    loop._restart_workers = True
    assert isinstance(loop, ls.loops.BatchedLoop), "BatchedLoop must be returned when stream=False and max_batch_size>1"

    lit_api = MagicMock()
    lit_api.stream = True
    lit_api.max_batch_size = 1
    loop = ls.loops.get_default_loop(lit_api.stream, lit_api.max_batch_size)
    loop._restart_workers = True
    assert isinstance(loop, ls.loops.StreamingLoop), "StreamingLoop must be returned when stream=True"

    lit_api = MagicMock()
    lit_api.stream = True
    lit_api.max_batch_size = 4
    loop = ls.loops.get_default_loop(lit_api.stream, lit_api.max_batch_size)
    loop._restart_workers = True
    assert isinstance(loop, ls.loops.BatchedStreamingLoop), (
        "BatchedStreamingLoop must be returned when stream=True and max_batch_size>1"
    )


def test_get_default_loop_enable_async():
    lit_api = MagicMock()
    lit_api.max_batch_size = 2
    lit_api.enable_async = True
    with pytest.raises(
        ValueError, match="Async batching is not supported. Please use enable_async=False with batching."
    ):
        ls.loops.get_default_loop(lit_api.stream, lit_api.max_batch_size, lit_api.enable_async)


@pytest.fixture
def lit_loop_setup():
    lit_loop = LitLoop()
    lit_loop._restart_workers = True
    lit_api = MagicMock(request_timeout=0.1)
    request_queue = Queue()
    return lit_loop, lit_api, request_queue


def test_lit_loop_get_batch_requests(lit_loop_setup):
    lit_loop, lit_api, request_queue = lit_loop_setup
    lit_api.max_batch_size = 2
    lit_api.batch_timeout = 0.1
    request_queue.put((0, "UUID-001", time.monotonic(), {"input": 4.0}))
    request_queue.put((0, "UUID-002", time.monotonic(), {"input": 5.0}))
    batches, timed_out_uids = lit_loop.get_batch_requests(lit_api, request_queue, MagicMock())
    assert len(batches) == 2
    assert batches == [(0, "UUID-001", {"input": 4.0}), (0, "UUID-002", {"input": 5.0})]
    assert timed_out_uids == []


def test_lit_loop_get_request(lit_loop_setup):
    lit_loop, _, request_queue = lit_loop_setup
    t = time.monotonic()
    request_queue.put((0, "UUID-001", t, {"input": 4.0}))
    response_queue_id, uid, timestamp, x_enc = lit_loop.get_request(request_queue, timeout=1)
    assert uid == "UUID-001"
    assert response_queue_id == 0
    assert timestamp == t
    assert x_enc == {"input": 4.0}
    assert lit_loop.get_request(request_queue, timeout=0.001) is None


@pytest.mark.asyncio
async def test_lit_loop_put_response(lit_loop_setup, mock_transport):
    lit_loop, _, request_queue = lit_loop_setup
    lit_loop.put_response(mock_transport, 0, "UUID-001", {"output": 16.0}, LitAPIStatus.OK, LoopResponseType.REGULAR)
    response = await mock_transport.areceive(0)
    assert response == ("UUID-001", ({"output": 16.0}, LitAPIStatus.OK, LoopResponseType.REGULAR, ANY))


def test_notify_timed_out_requests():
    response_queues = [Queue()]

    # Simulate timed out requests
    timed_out_uids = [(0, "UUID-001"), (0, "UUID-002")]

    # Call the function to notify timed out requests
    notify_timed_out_requests(response_queues, timed_out_uids)

    # Check the responses in the response queue
    response_1 = response_queues[0].get()
    response_2 = response_queues[0].get()

    assert response_1[0] == "UUID-001"
    assert response_1[1][1] == LitAPIStatus.ERROR
    assert isinstance(response_1[1][0], HTTPException)
    assert response_2[0] == "UUID-002"
    assert isinstance(response_2[1][0], HTTPException)
    assert response_2[1][1] == LitAPIStatus.ERROR


class ContinuousBatchingAPI(ls.LitAPI):
    def setup(self, spec: Optional[LitSpec]):
        self.model = {}

    def add_request(self, uid: str, request):
        print(f"Adding to request_queue at {time.monotonic()}")
        self.model[uid] = {"outputs": list(range(5))}

    def decode_request(self, input: str):
        return input

    def encode_response(self, output: str):
        return {"output": output}

    def has_capacity(self) -> bool:
        return True

    def has_active_requests(self) -> bool:
        return bool(self.model)

    def step(self, prev_outputs: Optional[list[Output]]) -> list[Output]:
        outputs = []
        for k in self.model:
            v = self.model[k]
            if v["outputs"]:
                o = v["outputs"].pop(0)
                outputs.append(Output(k, o, LitAPIStatus.OK))
        keys = list(self.model.keys())
        for k in keys:
            if k not in [o.uid for o in outputs]:
                outputs.append(Output(k, "", LitAPIStatus.FINISH_STREAMING))
                del self.model[k]
        return outputs


@pytest.mark.parametrize(
    ("stream", "max_batch_size", "error_msg"),
    [
        (True, 4, "`lit_api.unbatch` must generate values using `yield`."),
        (True, 1, "`lit_api.encode_response` must generate values using `yield`."),
    ],
)
def test_default_loop_pre_setup_error(stream, max_batch_size, error_msg):
    lit_api = ls.test_examples.SimpleLitAPI()
    lit_api.stream = stream
    lit_api.max_batch_size = max_batch_size
    loop = DefaultLoop()
    with pytest.raises(ValueError, match=error_msg):
        loop.pre_setup(lit_api, None)


@pytest.fixture
def continuous_batching_setup(monkeypatch, mock_transport):
    lit_api = ContinuousBatchingAPI()
    lit_api.stream = True
    lit_api.request_timeout = 0.1
    lit_api.max_batch_size = 2
    lit_api.batch_timeout = 0.1
    lit_api.pre_setup(spec=None)
    lit_api.setup(None)
    request_queue = Queue()

    lit_loop = ContinuousBatchingLoop()
    return lit_api, lit_loop, request_queue, mock_transport


def test_continuous_batching_pre_setup(continuous_batching_setup):
    lit_api, lit_loop, request_queue, mock_transport = continuous_batching_setup
    lit_api.stream = False
    with pytest.raises(
        ValueError,
        match=re.escape(
            "Continuous batching loop requires streaming to be enabled. Please set LitServe(..., stream=True)"
        ),
    ):
        lit_loop.pre_setup(lit_api, None)


@pytest.mark.asyncio
async def test_continuous_batching_run(continuous_batching_setup):
    lit_api, lit_loop, request_queue, mock_transport = continuous_batching_setup
    response_queue_id, uid, _, input = (0, "UUID-001", time.monotonic(), {"input": "Hello"})
    lit_loop.add_request(uid, input, lit_api, None)
    lit_loop.response_queue_ids[uid] = response_queue_id
    await lit_loop.run(lit_api, "cpu", 0, request_queue, mock_transport, {}, NOOP_CB_RUNNER)

    results = []
    for i in range(5):
        response = await mock_transport.areceive(0)
        uid, (response_data, status, response_type, _) = response
        o = json.loads(response_data)["output"]
        assert o == i
        assert status == LitAPIStatus.OK
        assert uid == "UUID-001"
        results.append(o)
    assert results == list(range(5)), "API must return a sequence of numbers from 0 to 4"
    response = await mock_transport.areceive(0)
    uid, (response_data, status, response_type, _) = response
    o = json.loads(response_data)["output"]
    assert o == ""
    assert status == LitAPIStatus.FINISH_STREAMING
    assert response_type == LoopResponseType.STREAMING


@pytest.mark.asyncio
async def test_handle_async_function():
    async def async_func():
        return "async"

    def sync_func():
        return "sync"

    async def async_gen():
        for i in range(3):
            yield i

    assert await _handle_async_function(async_func) == "async"
    assert await _handle_async_function(sync_func) == "sync"
    async_gen = await _handle_async_function(async_gen)
    assert isinstance(async_gen, AsyncGenerator)


@pytest.mark.asyncio
async def test_async_inject_context():
    async def async_func(x, context=0):
        return x * context["a"]

    context = {"a": 1}
    assert await _async_inject_context(context, async_func, 2) == 2


@pytest.mark.asyncio
async def test_sync_fn_to_async_fn():
    def sync_func():
        return "sync-to-async"

    def sync_gen():
        for i in range(3):
            yield f"sync-to-async-{i}"

    assert await _sync_fn_to_async_fn(sync_func) == "sync-to-async"
    async_gen = await _sync_fn_to_async_fn(sync_gen)
    assert isinstance(async_gen, AsyncGenerator)
```

## File: `tests/unit/test_mcp.py`
```python
import inspect
from typing import Optional
from unittest.mock import patch

import pytest
from fastapi import FastAPI
from pydantic import BaseModel, Field
from starlette.applications import Starlette

import litserve as ls
from litserve.mcp import (
    MCP,
    _LitMCPServerConnector,
    _param_name_to_title,
    _python_type_to_json_schema,
    extract_input_schema,
)


@patch("litserve.mcp.is_package_installed", return_value=False)
def test_mcp_not_installed(mock_is_package_installed):
    with pytest.raises(
        RuntimeError,
        match="mcp package is required for MCP support. To install, run `pip install fastmcp` in the terminal.",
    ):
        MCP()


def test_python_type_to_json_schema():
    assert _python_type_to_json_schema(inspect.Parameter.empty) == "string"
    assert _python_type_to_json_schema(int) == "integer"
    assert _python_type_to_json_schema(float) == "number"
    assert _python_type_to_json_schema(str) == "string"
    assert _python_type_to_json_schema(bool) == "boolean"
    assert _python_type_to_json_schema(list) == "array"
    assert _python_type_to_json_schema(dict) == "object"
    assert _python_type_to_json_schema(Optional[int]) == {"nullable": True, "type": "integer"}
    assert _python_type_to_json_schema(Optional[str]) == {"nullable": True, "type": "string"}
    assert _python_type_to_json_schema(Optional[bool]) == {"nullable": True, "type": "boolean"}
    assert _python_type_to_json_schema(Optional[list]) == {"nullable": True, "type": "array"}
    assert _python_type_to_json_schema(Optional[dict]) == {"nullable": True, "type": "object"}


def test_param_name_to_title():
    assert _param_name_to_title("name") == "Name"
    assert _param_name_to_title("age") == "Age"
    assert _param_name_to_title("is_active") == "Is Active"


class MCPTestModel(BaseModel):
    name: str
    age: int


def test_mcp_schema():
    schema = extract_input_schema(MCPTestModel)
    assert schema == {
        "properties": {"mcptestmodel": {"$ref": "#/$defs/MCPTestModel"}},
        "required": ["mcptestmodel"],
        "title": "MCPTestModelArguments",
        "type": "object",
        "$defs": {
            "MCPTestModel": {
                "properties": {"name": {"title": "Name", "type": "string"}, "age": {"title": "Age", "type": "integer"}},
                "required": ["name", "age"],
                "title": "MCPTestModel",
                "type": "object",
            }
        },
    }, "Must adhere with MCP inputSchema format."


class NestedMCPTestModel(BaseModel):
    address: str
    nested: MCPTestModel


def test_mcp_schema_nested():
    schema = extract_input_schema(NestedMCPTestModel)
    (
        schema
        == {
            "properties": {
                "address": {"title": "Address", "type": "string"},
                "nested": {"$ref": "#/$defs/MCPTestModel"},
            },
            "required": ["address", "nested"],
            "title": "NestedMCPTestModelArguments",
            "type": "object",
            "$defs": {
                "MCPTestModel": {
                    "properties": {
                        "age": {"title": "Age", "type": "integer"},
                        "name": {"title": "Name", "type": "string"},
                    },
                    "required": ["name", "age"],
                    "title": "MCPTestModel",
                    "type": "object",
                }
            },
        },
        "Must adhere with MCP inputSchema format.",
    )


class MCPTestModelWithFields(BaseModel):
    name: str = Field(default="John")
    age: int = Field(ge=0, le=100)


def test_mcp_schema_with_fields():
    schema = extract_input_schema(MCPTestModelWithFields)
    assert schema == {
        "properties": {"mcptestmodelwithfields": {"$ref": "#/$defs/MCPTestModelWithFields"}},
        "required": ["mcptestmodelwithfields"],
        "title": "MCPTestModelWithFieldsArguments",
        "type": "object",
        "$defs": {
            "MCPTestModelWithFields": {
                "properties": {
                    "name": {"default": "John", "title": "Name", "type": "string"},
                    "age": {"maximum": 100, "minimum": 0, "title": "Age", "type": "integer"},
                },
                "required": ["age"],
                "title": "MCPTestModelWithFields",
                "type": "object",
            }
        },
    }


def mcp_test_function(name: str, age: int = 20):
    return None


def test_mcp_schema_with_default_values():
    schema = extract_input_schema(mcp_test_function)
    assert schema == {
        "properties": {
            "age": {"title": "Age", "type": "integer"},
            "name": {"title": "Name", "type": "string"},
        },
        "required": ["name"],
        "title": "mcp_test_functionArguments",
        "type": "object",
    }, "Must adhere with MCP inputSchema format."


def test_python_type_to_json_schema_complex():
    # Test generic types
    assert _python_type_to_json_schema(list[str]) == "array"
    assert _python_type_to_json_schema(dict[str, int]) == "object"

    # Test nested optional types
    assert _python_type_to_json_schema(Optional[list[str]]) == {"type": "array", "nullable": True}


class ModelWithConstraints(BaseModel):
    name: str = Field(min_length=3, max_length=50, description="User's full name")
    age: int = Field(
        gt=0,  # exclusive minimum
        lt=150,  # exclusive maximum
        description="User's age in years",
    )


def test_field_constraints():
    schema = extract_input_schema(ModelWithConstraints)
    print(schema)
    assert schema == {
        "properties": {"modelwithconstraints": {"$ref": "#/$defs/ModelWithConstraints"}},
        "required": ["modelwithconstraints"],
        "title": "ModelWithConstraintsArguments",
        "type": "object",
        "$defs": {
            "ModelWithConstraints": {
                "properties": {
                    "name": {
                        "description": "User's full name",
                        "maxLength": 50,
                        "minLength": 3,
                        "title": "Name",
                        "type": "string",
                    },
                    "age": {
                        "description": "User's age in years",
                        "exclusiveMaximum": 150,
                        "exclusiveMinimum": 0,
                        "title": "Age",
                        "type": "integer",
                    },
                },
                "required": ["name", "age"],
                "title": "ModelWithConstraints",
                "type": "object",
            }
        },
    }


def func_with_special_params(*args, **kwargs):
    pass


def test_args_kwargs_handling():
    schema = extract_input_schema(func_with_special_params)
    assert schema == {"properties": {}, "required": [], "title": "func_with_special_paramsArguments", "type": "object"}


class MCPLitAPI(ls.test_examples.SimpleLitAPI):
    def decode_request(self, request: MCPTestModel) -> int:
        return request.age


def test_mcp_cls():
    mc = MCP(description="A simple API", input_schema={"name": "string"})
    assert mc.description == "A simple API"
    assert mc.input_schema == {"name": "string"}
    assert mc.name is None

    with pytest.raises(RuntimeError, match="MCP is not connected to a LitAPI."):
        mc.as_tool()


def test_mcp_cls_with_lit_api():
    mcp = MCP(description="A simple API", input_schema={"name": "string"})
    api = MCPLitAPI(mcp=mcp)
    tool = mcp.as_tool()
    assert api.mcp is mcp
    assert tool.name == "predict"
    assert tool.endpoint == "/predict"
    assert tool.description == "A simple API"
    assert tool.inputSchema == {"name": "string"}


def test_mcp_cls_with_lit_api_no_input_schema():
    mcp = MCP(description="A simple API")
    api = MCPLitAPI(mcp=mcp)
    tool = mcp.as_tool()
    assert api.mcp is mcp
    assert tool.name == "predict"
    assert tool.endpoint == "/predict"
    assert tool.description == "A simple API"
    assert tool.inputSchema == {
        "properties": {"request": {"$ref": "#/$defs/MCPTestModel"}},
        "required": ["request"],
        "title": "decode_requestArguments",
        "type": "object",
        "$defs": {
            "MCPTestModel": {
                "properties": {"name": {"title": "Name", "type": "string"}, "age": {"title": "Age", "type": "integer"}},
                "required": ["name", "age"],
                "title": "MCPTestModel",
                "type": "object",
            }
        },
    }


def test_mcp_litserve_connector():
    connector = _LitMCPServerConnector()
    mcp = MCP(description="A simple API", input_schema={"name": "string"})
    api = MCPLitAPI(mcp=mcp)
    tool = mcp.as_tool()
    connector.add_tool(tool)
    assert api.mcp is mcp
    assert connector.list_tools() == [tool]
    assert connector.tool_endpoint_connections == {"predict": "/predict"}

    app = FastAPI()
    connector.connect_mcp_server([tool], app)
    mcp_mount = list(filter(lambda route: route.name == "mcp", app.routes))[0]
    assert isinstance(mcp_mount.app, Starlette)
```

## File: `tests/unit/test_middlewares.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import copy

import pytest
from fastapi.testclient import TestClient
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.types import ASGIApp

import litserve as ls
from litserve.middlewares import RequestCountMiddleware
from litserve.utils import wrap_litserve_start


class RequestIdMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, length: int) -> None:
        self.app = app
        self.length = length
        super().__init__(app)

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Request-Id"] = "0" * self.length
        return response


def test_custom_middleware():
    server = ls.LitServer(ls.test_examples.SimpleLitAPI(), middlewares=[(RequestIdMiddleware, {"length": 5})])
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0})
        assert response.status_code == 200, f"Expected response to be 200 but got {response.status_code}"
        assert response.json() == {"output": 16.0}, "server didn't return expected output"
        assert response.headers["X-Request-Id"] == "00000"


def test_starlette_middlewares():
    middlewares = [
        (
            TrustedHostMiddleware,
            {
                "allowed_hosts": ["localhost", "127.0.0.1"],
            },
        ),
        HTTPSRedirectMiddleware,
    ]
    server = ls.LitServer(ls.test_examples.SimpleLitAPI(), middlewares=middlewares)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0}, headers={"Host": "localhost"})
        assert response.status_code == 200, f"Expected response to be 200 but got {response.status_code}"
        assert response.json() == {"output": 16.0}, "server didn't return expected output"

        response = client.post("/predict", json={"input": 4.0}, headers={"Host": "not-trusted-host"})
        assert response.status_code == 400, f"Expected response to be 400 but got {response.status_code}"


def test_middlewares_inputs():
    server = ls.LitServer(ls.test_examples.SimpleLitAPI(), middlewares=[])
    assert len(server.middlewares) == 1, "Default middleware should be present"

    server = ls.LitServer(ls.test_examples.SimpleLitAPI(), middlewares=[], max_payload_size=1000)
    assert len(server.middlewares) == 2, "Default middleware should be present"

    server = ls.LitServer(ls.test_examples.SimpleLitAPI(), middlewares=None)
    assert len(server.middlewares) == 1, "Default middleware should be present"

    with pytest.raises(ValueError, match="middlewares must be a list of tuples"):
        ls.LitServer(ls.test_examples.SimpleLitAPI(), middlewares=(RequestIdMiddleware, {"length": 5}))


def test_middleware_multiple_initialization():
    api1 = ls.test_examples.SimpleLitAPI(api_path="/api1")
    api2 = ls.test_examples.SimpleLitAPI(api_path="/api2")
    api3 = ls.test_examples.SimpleLitAPI(api_path="/api3")
    api4 = ls.test_examples.SimpleLitAPI(api_path="/api4")

    server = ls.LitServer([api1, api2, api3, api4])
    assert len(server.app.user_middleware) == 1, "Each middleware should be initialized only once for `n` LitAPIs"


def test_track_requests_middleware_isolation():
    """Test that _prepare_app_run doesn't modify the original app's middleware list."""

    lit_api = ls.test_examples.SimpleLitAPI()
    server = ls.LitServer(lit_api, track_requests=True)

    # Store original middleware state
    original_middleware = server.app.user_middleware.copy()

    # Create app copies (simulating multiple API servers)
    app_copies = [copy.copy(server.app) for _ in range(3)]

    # Call _prepare_app_run on each copy
    for app_copy in app_copies:
        server._prepare_app_run(app_copy)

    # Verify each copy has RequestCountMiddleware added
    for app_copy in app_copies:
        assert len(app_copy.user_middleware) == len(original_middleware) + 1
        # Check that RequestCountMiddleware is added
        assert any(mw.cls is RequestCountMiddleware for mw in app_copy.user_middleware), (
            "RequestCountMiddleware not found in middleware list"
        )
```

## File: `tests/unit/test_multiple_endpoints.py`
```python
import pytest
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

import litserve as ls
from litserve.utils import wrap_litserve_start


class InferencePipeline(ls.LitAPI):
    def __init__(self, name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def setup(self, device):
        self.model = lambda x: x**2

    def decode_request(self, request):
        return request["input"]

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output):
        return {"output": output, "name": self.name}


@pytest.mark.asyncio
async def test_multiple_endpoints():
    api1 = InferencePipeline(name="api1", api_path="/api1")
    api2 = InferencePipeline(name="api2", api_path="/api2")
    server = ls.LitServer([api1, api2])

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/api1", json={"input": 2.0}, timeout=10)
            assert resp.status_code == 200, "Server response should be 200 (OK)"
            assert resp.json()["output"] == 4.0, "output from Identity server must be same as input"
            assert resp.json()["name"] == "api1", "name from Identity server must be same as input"

            resp = await ac.post("/api2", json={"input": 5.0}, timeout=10)
            assert resp.status_code == 200, "Server response should be 200 (OK)"
            assert resp.json()["output"] == 25.0, "output from Identity server must be same as input"
            assert resp.json()["name"] == "api2", "name from Identity server must be same as input"


def test_multiple_endpoints_with_same_path():
    api1 = InferencePipeline(name="api1", api_path="/api1")
    api2 = InferencePipeline(name="api2", api_path="/api1")
    with pytest.raises(ValueError, match="api_path /api1 is already in use by"):
        ls.LitServer([api1, api2])


def test_reserved_paths():
    api1 = InferencePipeline(name="api1", api_path="/health")
    api2 = InferencePipeline(name="api2", api_path="/info")
    with pytest.raises(ValueError, match="api_path /health is already in use by LitServe healthcheck"):
        ls.LitServer([api1, api2])
```

## File: `tests/unit/test_openai_embedding.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import copy
import time

import numpy as np
import pytest
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

import litserve as ls
from litserve.specs.openai_embedding import OpenAIEmbeddingSpec
from litserve.test_examples.openai_embedding_spec_example import (
    TestEmbedAPI,
    TestEmbedAPIWithMissingEmbeddings,
    TestEmbedAPIWithNonDictOutput,
    TestEmbedAPIWithUsage,
    TestEmbedAPIWithYieldEncodeResponse,
    TestEmbedAPIWithYieldPredict,
)
from litserve.utils import wrap_litserve_start


@pytest.mark.asyncio
async def test_openai_embedding_spec_with_single_input(openai_embedding_request_data):
    spec = OpenAIEmbeddingSpec()
    server = ls.LitServer(TestEmbedAPI(spec=spec))

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/embeddings", json=openai_embedding_request_data, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"
            assert resp.json()["object"] == "list", "Object should be list"
            assert resp.json()["data"][0]["index"] == 0, "Index should be 0"
            assert len(resp.json()["data"]) == 1, "Length of data should be 1"
            assert len(resp.json()["data"][0]["embedding"]) == 768, "Embedding length should be 768"


@pytest.mark.asyncio
@pytest.mark.parametrize("api_path", ["/v1/embeddings", "/v2/embeddings"])
async def test_openai_embedding_spec_with_custom_api_path(openai_embedding_request_data, api_path):
    server = ls.LitServer(
        [
            TestEmbedAPI(spec=OpenAIEmbeddingSpec(), api_path=api_path),
        ]
    )
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post(api_path, json=openai_embedding_request_data, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"
            assert resp.json()["object"] == "list", "Object should be list"
            assert resp.json()["data"][0]["index"] == 0, "Index should be 0"
            assert len(resp.json()["data"]) == 1, "Length of data should be 1"
            assert len(resp.json()["data"][0]["embedding"]) == 768, "Embedding length should be 768"


@pytest.mark.asyncio
async def test_openai_embedding_spec_custom_api_path_warning():
    with pytest.warns(UserWarning, match="Custom API path detected"):
        ls.LitServer(TestEmbedAPI(spec=OpenAIEmbeddingSpec(), api_path="/v2/embeddings"))


@pytest.mark.asyncio
async def test_openai_embedding_spec_with_multiple_inputs(openai_embedding_request_data_array):
    spec = OpenAIEmbeddingSpec()
    server = ls.LitServer(TestEmbedAPI(spec=spec))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/embeddings", json=openai_embedding_request_data_array, timeout=10)
            assert resp.status_code == 200, (
                f"Status code should be 200 but got {resp.status_code}, response: {resp.content}"
            )
            assert resp.json()["object"] == "list", "Object should be list"
            assert resp.json()["data"][0]["index"] == 0, "Index should be 0"
            assert len(resp.json()["data"]) == 4, "Length of data should be 1"
            assert len(resp.json()["data"][0]["embedding"]) == 768, "Embedding length should be 768"


@pytest.mark.asyncio
async def test_openai_embedding_spec_with_usage(openai_embedding_request_data):
    spec = OpenAIEmbeddingSpec()
    server = ls.LitServer(TestEmbedAPIWithUsage(spec=spec))

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/embeddings", json=openai_embedding_request_data, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"
            assert resp.json()["object"] == "list", "Object should be list"
            assert resp.json()["data"][0]["index"] == 0, "Index should be 0"
            assert len(resp.json()["data"]) == 1, "Length of data should be 1"
            assert len(resp.json()["data"][0]["embedding"]) == 768, "Embedding length should be 768"
            assert resp.json()["usage"]["prompt_tokens"] == 10, "Prompt tokens should be 10"
            assert resp.json()["usage"]["total_tokens"] == 10, "Total tokens should be 10"


@pytest.mark.asyncio
async def test_openai_embedding_spec_validation(openai_request_data):
    # FIXME:  The error should be raised in the LitAPI constructor
    with pytest.raises(ValueError, match="You are using yield in your predict method"):
        ls.LitServer(TestEmbedAPIWithYieldPredict(spec=OpenAIEmbeddingSpec()))

    with pytest.raises(ValueError, match="You are using yield in your encode_response method"):
        ls.LitServer(TestEmbedAPIWithYieldEncodeResponse(spec=OpenAIEmbeddingSpec()))


@pytest.mark.asyncio
async def test_openai_embedding_spec_with_non_dict_output(openai_embedding_request_data):
    server = ls.LitServer(TestEmbedAPIWithNonDictOutput(spec=ls.OpenAIEmbeddingSpec()))

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            with pytest.raises(ValueError, match="Expected response to be a dictionary"):
                await ac.post("/v1/embeddings", json=openai_embedding_request_data, timeout=10)


@pytest.mark.asyncio
async def test_openai_embedding_spec_with_missing_embeddings(openai_embedding_request_data):
    server = ls.LitServer(TestEmbedAPIWithMissingEmbeddings(spec=OpenAIEmbeddingSpec()))

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            with pytest.raises(ValueError, match="The response does not contain the key 'embeddings'"):
                await ac.post("/v1/embeddings", json=openai_embedding_request_data, timeout=10)


class TestOpenAIWithBatching(TestEmbedAPI):
    def predict(self, batch):
        time.sleep(2)
        return np.random.rand(len(batch), 768).tolist()


@pytest.mark.asyncio
async def test_openai_embedding_spec_with_batching(openai_embedding_request_data):
    api = TestOpenAIWithBatching(max_batch_size=10, batch_timeout=4, spec=ls.OpenAIEmbeddingSpec())
    server = ls.LitServer(api)

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            # send concurrent requests
            req1 = copy.deepcopy(openai_embedding_request_data)
            req2 = copy.deepcopy(openai_embedding_request_data)
            req2["input"] = "This is the second request"
            tasks = []
            t0 = time.perf_counter()
            for _ in range(5):
                tasks.append(ac.post("/v1/embeddings", json=req1, timeout=10))
                tasks.append(ac.post("/v1/embeddings", json=req2, timeout=10))

            responses = await asyncio.gather(*tasks)
            t1 = time.perf_counter()
            print(f"Time taken: {t1 - t0} seconds")
            for resp in responses:
                assert resp.status_code == 200, (
                    f"Status code should be 200, but got {resp.status_code}, response: {resp.content}"
                )
                assert len(resp.json()["data"]) == 1, "Length of data should be 1"
            assert t1 - t0 < 20, "Time taken must be less than 20 seconds (batching is not working)"


@pytest.mark.asyncio
async def test_batching_with_client_side_batching(openai_embedding_request_data_array):
    api = TestOpenAIWithBatching(max_batch_size=2, batch_timeout=10, spec=ls.OpenAIEmbeddingSpec())
    server = ls.LitServer(api)

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/embeddings", json=openai_embedding_request_data_array, timeout=10)

            assert resp.status_code == 400, "Cient side batching is not supported with dynamic batching"
            assert (
                resp.json()["detail"]
                == "The OpenAIEmbedding spec does not support dynamic batching when client-side batching is used. "
                "To resolve this, either set `max_batch_size=1` or send a single input from the client."
            )
```

## File: `tests/unit/test_pydantic.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from fastapi.testclient import TestClient
from pydantic import BaseModel

from litserve import LitAPI, LitServer
from litserve.utils import wrap_litserve_start


class PredictRequest(BaseModel):
    input: float


class PredictResponse(BaseModel):
    output: float


class SimpleLitAPI(LitAPI):
    def setup(self, device):
        self.model = lambda x: x**2

    def decode_request(self, request: PredictRequest) -> float:
        return request.input

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output: float) -> PredictResponse:
        return PredictResponse(output=output)


def test_pydantic():
    server = LitServer(SimpleLitAPI(), accelerator="cpu", devices=1, timeout=5)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0})
        assert response.json() == {"output": 16.0}
```

## File: `tests/unit/test_readme.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Code extraction adapted from https://github.com/tassaron/get_code_from_markdown
import re
import selectors
import subprocess
import sys
import time

import pytest
from tqdm import tqdm

uvicorn_msg = "Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)"


def extract_code_blocks(lines: list[str]) -> list[str]:
    language = "python"
    regex = re.compile(
        r"(?P<start>^```(?P<block_language>(\w|-)+)\n)(?P<code>.*?\n)(?P<end>```)",
        re.DOTALL | re.MULTILINE,
    )
    blocks = [(match.group("block_language"), match.group("code")) for match in regex.finditer("".join(lines))]
    return [block for block_language, block in blocks if block_language == language]


def get_code_blocks(file: str) -> list[str]:
    with open(file) as f:
        lines = list(f)
        return extract_code_blocks(lines)


def get_extra_time(content: str) -> int:
    if "torch" in content or "transformers" in content:
        return 5

    return 0


def run_script_with_timeout(file, timeout, extra_time, killall):
    sel = selectors.DefaultSelector()
    try:
        process = subprocess.Popen(
            [sys.executable, str(file)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,  # Line-buffered
            universal_newlines=True,  # Decode bytes to string
        )

        stdout_lines = []
        stderr_lines = []
        end_time = time.time() + timeout + extra_time

        sel.register(process.stdout, selectors.EVENT_READ)
        sel.register(process.stderr, selectors.EVENT_READ)

        while True:
            timeout_remaining = end_time - time.time()
            if timeout_remaining <= 0:
                killall(process)
                break

            events = sel.select(timeout=timeout_remaining)
            for key, _ in events:
                if key.fileobj is process.stdout:
                    line = process.stdout.readline()
                    if line:
                        stdout_lines.append(line)
                elif key.fileobj is process.stderr:
                    line = process.stderr.readline()
                    if line:
                        stderr_lines.append(line)

            if process.poll() is not None:
                break

        output = "".join(stdout_lines)
        errors = "".join(stderr_lines)

        # Get the return code of the process
        returncode = process.returncode

    except Exception as e:
        output = ""
        errors = str(e)
        returncode = -1  # Indicate failure in running the process

    return returncode, output, errors


@pytest.mark.skipif(sys.platform.startswith("win"), reason="Windows CI is slow and this test is just a sanity check.")
def test_readme(tmp_path, killall):
    d = tmp_path / "readme_codes"
    d.mkdir(exist_ok=True)
    code_blocks = get_code_blocks("README.md")
    assert len(code_blocks) > 0, "No code block found in README.md"

    for i, code in enumerate(tqdm(code_blocks)):
        file = d / f"{i}.py"
        file.write_text(code)
        extra_time = get_extra_time(code)

        returncode, stdout, stderr = run_script_with_timeout(file, timeout=5, extra_time=extra_time, killall=killall)

        if "server.run" in code:
            assert uvicorn_msg in stderr, f"Expected to run uvicorn server.\nCode:\n {code}\n\nCode output: {stderr}"
        elif "requests.post" in code:
            assert "ConnectionError" in stderr, (
                f"Client examples should fail with a ConnectionError because there is no server running.\nCode:\n{code}"
            )
        else:
            assert returncode == 0, (
                f"Code exited with {returncode}.\n"
                f"Error: {stderr}\n"
                f"Please check the code for correctness:\n```\n{code}\n```"
            )
```

## File: `tests/unit/test_request_handlers.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import json
from queue import Queue
from unittest import mock
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException, Request

from litserve.server import BaseRequestHandler, RegularRequestHandler
from litserve.test_examples import SimpleLitAPI
from litserve.utils import LitAPIStatus, ResponseBufferItem


@pytest.fixture
def mock_lit_api():
    return SimpleLitAPI()


class MockServer:
    def __init__(self, lit_api):
        self.lit_api = lit_api
        self.response_buffer = {}
        self.request_queue = Queue()
        self._callback_runner = mock.MagicMock()
        self.app = mock.MagicMock()
        self.app.response_queue_id = 0
        self.active_requests = 0

    def _get_request_queue(self, api_path):
        return self.request_queue


class MockRequest:
    """Mock FastAPI Request object for testing."""

    def __init__(self, json_data=None, form_data=None, content_type="application/json"):
        self._json_data = json_data or {}
        self._form_data = form_data or {}
        self.headers = {"Content-Type": content_type}

    async def json(self):
        if self._json_data is None:
            raise json.JSONDecodeError("Invalid JSON", "", 0)
        return self._json_data

    async def form(self):
        return self._form_data


class TestRequestHandler(BaseRequestHandler):
    def __init__(self, lit_api, server):
        super().__init__(lit_api, server)
        self.litapi_request_queues = {"/predict": Queue()}

    async def handle_request(self, request, request_type):
        payload = await self._prepare_request(request, request_type)
        uid, response_queue_id = await self._submit_request(payload)
        return response_queue_id


@pytest.mark.asyncio
async def test_request_handler(mock_lit_api):
    mock_server = MockServer(mock_lit_api)
    handler = TestRequestHandler(mock_lit_api, mock_server)
    mock_request = MockRequest()
    response_queue_id = await handler.handle_request(mock_request, Request)
    assert response_queue_id == 0


@pytest.mark.asyncio
@patch("litserve.server.asyncio.Event")
async def test_request_handler_streaming(mock_event, mock_lit_api):
    mock_event.return_value = AsyncMock()
    mock_server = MockServer(mock_lit_api)
    mock_request = MockRequest()
    mock_server.response_buffer = MagicMock()
    mock_server.response_buffer.pop.return_value = ResponseBufferItem(
        asyncio.Event(), response=("test-response", LitAPIStatus.OK)
    )
    handler = RegularRequestHandler(mock_lit_api, mock_server)
    response = await handler.handle_request(mock_request, Request)
    assert mock_server.request_queue.qsize() == 1
    assert response == "test-response"


def test_regular_handler_error_response():
    with pytest.raises(HTTPException) as e:
        RegularRequestHandler._handle_error_response(HTTPException(status_code=500, detail="test error response"))
    assert e.value.status_code == 500
    assert e.value.detail == "test error response"

    with pytest.raises(HTTPException) as e:
        RegularRequestHandler._handle_error_response(Exception("test exception"))
    assert e.value.status_code == 500
    assert e.value.detail == "Internal server error"
```

## File: `tests/unit/test_schema.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import base64
import io
import os

import numpy as np
from fastapi.testclient import TestClient
from PIL import Image

import litserve as ls
from litserve.schema.image import ImageInput, ImageOutput
from litserve.utils import wrap_litserve_start


class ImageAPI(ls.LitAPI):
    def setup(self, device):
        self.model = lambda x: np.array(x) * 2

    def decode_request(self, request: ImageInput):
        return request.get_image()

    def predict(self, x):
        return self.model(x)

    def encode_response(self, numpy_image) -> ImageOutput:
        output = Image.fromarray(np.uint8(numpy_image)).convert("RGB")
        return ImageOutput(image=output)


def test_image_input_output(tmpdir):
    path = os.path.join(tmpdir, "test.png")
    server = ls.LitServer(ImageAPI(), accelerator="cpu", devices=1, workers_per_device=1)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        Image.new("RGB", (32, 32)).save(path)
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        response = client.post("/predict", json={"image_data": encoded_string})

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        image_data = response.json()["image"]
        image = Image.open(io.BytesIO(base64.b64decode(image_data)))
        assert image.size == (32, 32), f"Unexpected image size: {image.size}"


class MultiImageInputModel(ImageInput):
    image_0: str
    image_1: str
    image_2: str


class MultiImageInputAPI(ImageAPI):
    def decode_request(self, request: MultiImageInputModel):
        images = [request.get_image(f"image_{i}") for i in range(3)]
        for image in images:
            assert isinstance(image, Image.Image)
        return images[0]


def test_multiple_image_input(tmpdir):
    path = os.path.join(tmpdir, "test.png")
    server = ls.LitServer(MultiImageInputAPI(), accelerator="cpu", devices=1, workers_per_device=1)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        data = {}
        for i in range(3):
            Image.new("RGB", (32, 32)).save(path)
            with open(path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            data[f"image_{i}"] = encoded_string
        response = client.post("/predict", json=data)

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        image_data = response.json()["image"]
        image = Image.open(io.BytesIO(base64.b64decode(image_data)))
        assert image.size == (32, 32), f"Unexpected image size: {image.size}"
```

## File: `tests/unit/test_simple.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import asyncio
import random
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import ExitStack

import numpy as np
import pytest
from asgi_lifespan import LifespanManager
from fastapi import Request, Response, status
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

import litserve.server
from litserve import LitAPI, LitServer
from litserve.utils import wrap_litserve_start


class SimpleLitAPI(LitAPI):
    def setup(self, device):
        self.model = lambda x: x**2

    def decode_request(self, request: Request):
        return request["input"]

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output) -> Response:
        return {"output": output}


def test_simple(lit_server):
    with TestClient(lit_server.app) as client:
        response = client.post("/predict", json={"input": 4.0})
        assert response.json() == {"output": 16.0}


class SlowSetupLitAPI(SimpleLitAPI):
    def setup(self, device):
        self.model = lambda x: x**2
        time.sleep(2)


class SlowSetupWithCustomHealthLitAPI(SimpleLitAPI):
    def setup(self, device):
        self.model = lambda x: x**2
        time.sleep(2)

    def health(self) -> bool:
        # Health check passes after 5 seconds from the first time it is called.
        if not hasattr(self, "_start_time"):
            self._start_time = time.time()
        return time.time() - self._start_time >= 5


@pytest.mark.parametrize("use_zmq", [True, False])
def test_workers_health(use_zmq):
    server = LitServer(
        SlowSetupLitAPI(), accelerator="cpu", devices=1, timeout=5, workers_per_device=2, fast_queue=use_zmq
    )

    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.get("/health")
        assert response.status_code == 503
        assert response.text == "not ready"

        time.sleep(1)
        response = client.get("/health")
        assert response.status_code == 503
        assert response.text == "not ready"

        time.sleep(3)
        response = client.get("/health")
        assert response.status_code == 200
        assert response.text == "ok"


@pytest.mark.parametrize("use_zmq", [True, False])
def test_workers_health_custom_path(use_zmq):
    server = LitServer(
        SlowSetupLitAPI(),
        accelerator="cpu",
        healthcheck_path="/my_server/health",
        devices=1,
        timeout=5,
        workers_per_device=2,
        fast_queue=use_zmq,
    )

    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.get("/my_server/health")
        assert response.status_code == 503
        assert response.text == "not ready"

        time.sleep(1)
        response = client.get("/my_server/health")
        assert response.status_code == 503
        assert response.text == "not ready"

        time.sleep(3)
        response = client.get("/my_server/health")
        assert response.status_code == 200
        assert response.text == "ok"


@pytest.mark.parametrize("use_zmq", [True, False])
def test_workers_health_with_custom_health_method(use_zmq):
    server = LitServer(
        SlowSetupWithCustomHealthLitAPI(),
        accelerator="cpu",
        devices=1,
        timeout=5,
        workers_per_device=2,
        fast_queue=use_zmq,
    )

    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.get("/health")
        assert response.status_code == 503
        assert response.text == "not ready"

        time.sleep(1)
        response = client.get("/health")
        assert response.status_code == 503
        assert response.text == "not ready"

        time.sleep(1)
        response = client.get("/health")
        assert response.status_code == 503
        assert response.text == "not ready"

        time.sleep(4)
        response = client.get("/health")
        assert response.status_code == 200
        assert response.text == "ok"


class AsyncHealthLitAPI(SimpleLitAPI):
    async def health(self) -> bool:
        await asyncio.sleep(0.1)
        return True


@pytest.mark.parametrize("use_zmq", [True, False])
def test_workers_health_with_async_health_method(use_zmq):
    server = LitServer(
        AsyncHealthLitAPI(),
        accelerator="cpu",
        devices=1,
        timeout=5,
        workers_per_device=2,
        fast_queue=use_zmq,
    )

    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        # wait for workers to be ready
        for _ in range(10):
            response = client.get("/health")
            if response.status_code == 200:
                break
            time.sleep(0.5)
        assert response.status_code == 200
        assert response.text == "ok"


def make_load_request(server, outputs):
    with TestClient(server.app) as client:
        for i in range(100):
            response = client.post("/predict", json={"input": i})
            outputs.append(response.json())


def test_load(lit_server):
    from threading import Thread

    threads = []
    for _ in range(1):
        outputs = []
        t = Thread(target=make_load_request, args=(lit_server, outputs))
        t.start()
        threads.append((t, outputs))

    for t, outputs in threads:
        t.join()
        for i, el in enumerate(outputs):
            assert el == {"output": i**2}


@pytest.fixture
def shutdown_api_key():
    api_key = f"test-key-{random.randint(100, 1000000)}"
    litserve.server.SHUTDOWN_API_KEY = api_key
    yield api_key
    litserve.server.SHUTDOWN_API_KEY = None


def test_shutdown_endpoint_single_worker(shutdown_api_key):
    server = LitServer(
        SimpleLitAPI(),
        accelerator="cpu",
        devices=1,
        workers_per_device=1,
        enable_shutdown_api=True,
    )

    with wrap_litserve_start(server) as srv, TestClient(srv.app) as client:
        response_no_header = client.post("/shutdown")
        assert response_no_header.status_code == 401

        response_correct_key = client.post("/shutdown", headers={"Authorization": f"Bearer {shutdown_api_key}"})
        assert response_correct_key.status_code == status.HTTP_200_OK


def test_shutdown_endpoint_multiple_workers(shutdown_api_key):
    server = LitServer(
        SimpleLitAPI(),
        accelerator="cpu",
        devices=1,
        workers_per_device=3,
        enable_shutdown_api=True,
    )

    with wrap_litserve_start(server) as srv, TestClient(srv.app) as client:
        response_no_header = client.post("/shutdown")
        assert response_no_header.status_code == 401

        response_wrong_key = client.post("/shutdown", headers={"Authorization": "Bearer wrong_key"})
        assert response_wrong_key.status_code == 401

        response_correct_key = client.post("/shutdown", headers={"Authorization": f"Bearer {shutdown_api_key}"})
        assert response_correct_key.status_code == status.HTTP_200_OK


class SlowLitAPI(LitAPI):
    def setup(self, device):
        self.model = lambda x: x**2

    def decode_request(self, request: Request):
        return request["input"]

    def predict(self, x):
        time.sleep(2)
        return self.model(x)

    def encode_response(self, output) -> Response:
        return {"output": output}


class SlowBatchAPI(SlowLitAPI):
    def batch(self, inputs):
        return np.asarray(inputs)

    def unbatch(self, output):
        return list(output)


@pytest.mark.flaky(retries=3)
@pytest.mark.parametrize("use_zmq", [True, False])
@pytest.mark.asyncio
async def test_timeout(use_zmq):
    # Scenario: first request completes, second request times out in queue
    api = SlowLitAPI()  # takes 2 seconds for each prediction
    server = LitServer(api, accelerator="cpu", devices=1, timeout=2, fast_queue=use_zmq)
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            response1 = asyncio.create_task(ac.post("/predict", json={"input": 4.0}))
            await asyncio.sleep(0.0001)
            response2 = asyncio.create_task(ac.post("/predict", json={"input": 5.0}))
            responses = await asyncio.gather(response1, response2, return_exceptions=True)
            assert responses[0].status_code == 200, (
                "First request should complete since it's popped from the request queue."
            )
            assert responses[1].status_code == 504, (
                "Server takes longer than specified timeout and request should timeout"
            )


@pytest.mark.flaky(retries=3)
@pytest.mark.parametrize("use_zmq", [True, False])
@pytest.mark.asyncio
async def test_batch_timeout_with_concurrent_requests(use_zmq):
    server = LitServer(
        SlowBatchAPI(
            max_batch_size=2,
            batch_timeout=1,
        ),
        accelerator="cpu",
        timeout=1.9,
        fast_queue=use_zmq,
    )
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            response1 = asyncio.create_task(ac.post("/predict", json={"input": 4.0}))
            response2 = asyncio.create_task(ac.post("/predict", json={"input": 5.0}))
            response3 = asyncio.create_task(ac.post("/predict", json={"input": 6.0}))
            responses = await asyncio.gather(response1, response2, response3, return_exceptions=True)

            status_code_200 = 0
            status_code_504 = 0
            for resp in responses:
                if resp.status_code == 200:
                    status_code_200 += 1
                elif resp.status_code == 504:
                    status_code_504 += 1

            assert status_code_200 == 2, "Two requests should succeeds"
            assert status_code_504 == 1, "One request should timeout"


@pytest.mark.parametrize("use_zmq", [True, False])
def test_server_with_disabled_timeout(use_zmq):
    servers = [
        LitServer(SlowLitAPI(), accelerator="cpu", devices=1, timeout=-1),
        LitServer(SlowLitAPI(), accelerator="cpu", devices=1, timeout=False),
        LitServer(
            SlowBatchAPI(
                max_batch_size=2,
                batch_timeout=2,
            ),
            accelerator="cpu",
            devices=1,
            timeout=False,
            fast_queue=use_zmq,
        ),
        LitServer(
            SlowBatchAPI(
                max_batch_size=2,
                batch_timeout=2,
            ),
            accelerator="cpu",
            devices=1,
            timeout=-1,
            fast_queue=use_zmq,
        ),
    ]

    with ExitStack() as stack:
        clients = [
            stack.enter_context(TestClient(stack.enter_context(wrap_litserve_start(server)).app)) for server in servers
        ]

        for i, client in enumerate(clients, 1):
            response = client.post("/predict", json={"input": 4.0})
            assert response.status_code == 200, f"Server {i} should complete request with disabled timeout"


def test_concurrent_requests(lit_server):
    n_requests = 100
    with TestClient(lit_server.app) as client, ThreadPoolExecutor(n_requests // 4 + 1) as executor:
        responses = list(executor.map(lambda i: client.post("/predict", json={"input": i}), range(n_requests)))

    count = 0
    for i, response in enumerate(responses):
        assert response.json() == {"output": i**2}, "Server returns square of the input number"
        count += 1
    assert count == n_requests


class CustomError(Exception):
    def __init__(self, arg1, arg2, arg3):
        super().__init__("Test exception")


class ExceptionAPI(SimpleLitAPI):
    def predict(self, x):
        raise CustomError("This", "is", "a test")


def test_exception():
    server = LitServer(ExceptionAPI(), accelerator="cpu", devices=1)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0})
        assert response.status_code == 500
        assert response.json() == {"detail": "Internal server error"}
```

## File: `tests/unit/test_specs.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json

import pytest
from asgi_lifespan import LifespanManager
from fastapi import HTTPException
from httpx import ASGITransport, AsyncClient

import litserve as ls
from litserve.specs.openai import ChatCompletionRequest, ChatMessage, OpenAISpec
from litserve.test_examples.openai_spec_example import (
    OpenAIBatchingWithUsage,
    OpenAIWithUsage,
    OpenAIWithUsageEncodeResponse,
    TestAPI,
    TestAPIWithCustomEncode,
    TestAPIWithStructuredOutput,
    TestAPIWithToolCalls,
)
from litserve.utils import wrap_litserve_start


class TestOpenAISpecAPI(ls.LitAPI):
    def setup(self, device):
        self.model = None

    def predict(self, x):
        assert isinstance(x, ChatCompletionRequest), "decode_request returns a ChatCompletionRequest"
        for e in ["This", "is", "a", "generated", "output"]:
            yield e + " "


class TestAsyncAPI(TestOpenAISpecAPI):
    async def predict(self, x):
        assert isinstance(x, ChatCompletionRequest), "decode_request returns a ChatCompletionRequest"
        for e in ["This", "is", "a", "generated", "output"]:
            yield e + " "


@pytest.mark.parametrize(
    "api", [TestOpenAISpecAPI(spec=OpenAISpec()), TestAsyncAPI(enable_async=True, spec=OpenAISpec())]
)
@pytest.mark.asyncio
async def test_openai_spec(openai_request_data, api):
    server = ls.LitServer(api)
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(
                transport=ASGITransport(app=manager.app),
                base_url="http://test",
            ) as ac,
        ):
            openai_request_data["stream"] = True
            resp = await ac.post("/v1/chat/completions", json=openai_request_data, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"
            messages = []
            async for chunk in resp.aiter_lines():
                if not chunk.startswith("data: "):
                    continue
                content = chunk[6:].strip()
                if content == "[DONE]" or not content:
                    break
                try:
                    chunk = json.loads(content)
                    delta = chunk.get("choices", [{}])[0].get("delta", {})
                    content_piece = delta.get("content")
                    if content_piece is not None:
                        messages.append(content_piece)
                except json.JSONDecodeError:
                    continue  # Optionally log or handle bad JSON chunks

            final_output = "".join(messages)
            assert final_output == "This is a generated output ", f"final_output: {final_output}"


# OpenAIWithUsage
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("api_cls", "batch_size"),
    [
        (OpenAIWithUsage, 1),
        (OpenAIWithUsageEncodeResponse, 1),
        (OpenAIBatchingWithUsage, 2),
    ],
)
async def test_openai_token_usage(api_cls, batch_size, openai_request_data, openai_response_data):
    server = ls.LitServer(api_cls(spec=ls.OpenAISpec(), max_batch_size=batch_size, batch_timeout=0.01))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/chat/completions", json=openai_request_data, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"
            result = resp.json()
            content = result["choices"][0]["message"]["content"]
            assert content == "10 + 6 is equal to 16.", "LitAPI predict response should match with the generated output"
            assert result["usage"] == openai_response_data["usage"]

            # with streaming
            openai_request_data["stream"] = True
            resp = await ac.post("/v1/chat/completions", json=openai_request_data, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"
            assert result["usage"] == openai_response_data["usage"]


class OpenAIWithUsagePerToken(ls.LitAPI):
    def setup(self, device):
        self.model = None

    def predict(self, x):
        for i in range(1, 6):
            yield {
                "role": "assistant",
                "content": f"{i}",
                "prompt_tokens": 0,
                "completion_tokens": 1,
                "total_tokens": 1,
            }


# OpenAIWithUsagePerToken
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("api_cls", "batch_size"),
    [
        (OpenAIWithUsagePerToken, 1),
    ],
)
async def test_openai_per_token_usage(api_cls, batch_size, openai_request_data):
    server = ls.LitServer(api_cls(spec=ls.OpenAISpec(), max_batch_size=batch_size, batch_timeout=0.01))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/chat/completions", json=openai_request_data, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"
            result = resp.json()
            content = result["choices"][0]["message"]["content"]
            assert content == "12345", "LitAPI predict response should match with the generated output"
            assert result["usage"]["completion_tokens"] == 5, "API yields 5 tokens"

            # with streaming
            openai_request_data["stream"] = True
            resp = await ac.post("/v1/chat/completions", json=openai_request_data, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"
            assert result["usage"]["completion_tokens"] == 5, "API yields 5 tokens"


@pytest.mark.asyncio
async def test_openai_spec_with_image(openai_request_data_with_image):
    server = ls.LitServer(TestAPI(spec=OpenAISpec()))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/chat/completions", json=openai_request_data_with_image, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"

            assert resp.json()["choices"][0]["message"]["content"] == "This is a generated output", (
                "LitAPI predict response should match with the generated output"
            )


@pytest.mark.asyncio
async def test_openai_spec_with_audio(openai_request_data_with_audio_wav, openai_request_data_with_audio_flac):
    server = ls.LitServer(TestAPI(spec=OpenAISpec()))

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/chat/completions", json=openai_request_data_with_audio_wav, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"

            assert resp.json()["choices"][0]["message"]["content"] == "This is a generated output", (
                "LitAPI predict response should match with the generated output"
            )

            # test for unsupported audio format
            resp = await ac.post("/v1/chat/completions", json=openai_request_data_with_audio_flac, timeout=10)
            assert resp.status_code == 422, "Status code should be 422"
            errors = resp.json()["detail"]
            assert any(error["msg"] == "Input should be 'wav' or 'mp3'" for error in errors), (
                "Error message for unsupported audio format should be present"
            )


@pytest.mark.asyncio
async def test_override_encode(openai_request_data):
    server = ls.LitServer(TestAPIWithCustomEncode(spec=OpenAISpec()))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/chat/completions", json=openai_request_data, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"

            assert resp.json()["choices"][0]["message"]["content"] == "This is a custom encoded output", (
                "LitAPI predict response should match with the generated output"
            )


@pytest.mark.asyncio
async def test_openai_spec_with_tools(openai_request_data_with_tools):
    server = ls.LitServer(TestAPIWithToolCalls(spec=OpenAISpec()))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/chat/completions", json=openai_request_data_with_tools, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"
            assert resp.json()["choices"][0]["message"]["content"] == "", (
                "LitAPI predict response should match with the generated output"
            )
            assert resp.json()["choices"][0]["message"]["tool_calls"] == [
                {
                    "id": "call_1",
                    "type": "function",
                    "function": {"name": "function_1", "arguments": '{"arg_1": "arg_1_value"}'},
                    "index": 0,
                }
            ], "LitAPI predict response should match with the generated output"


@pytest.mark.asyncio
async def test_openai_spec_with_response_format(openai_request_data_with_response_format):
    server = ls.LitServer(TestAPIWithStructuredOutput(spec=OpenAISpec()))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/chat/completions", json=openai_request_data_with_response_format, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"
            assert (
                resp.json()["choices"][0]["message"]["content"]
                == '{"name": "Science Fair", "date": "Friday", "participants": ["Alice", "Bob"]}'
            ), "LitAPI predict response should match with the generated output"


class MetadataRequiredAPI(ls.LitAPI):
    def setup(self, device):
        self.device = device

    def decode_request(self, request):
        return request

    def predict(self, request):
        metadata = request.metadata
        if not metadata or "user_id" not in metadata:
            raise HTTPException(status_code=500, detail="Missing required metadata")
        yield "ok"


@pytest.mark.asyncio
async def test_openai_spec_metadata(openai_request_data_with_metadata):
    server = ls.LitServer(MetadataRequiredAPI(spec=OpenAISpec()))

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/chat/completions", json=openai_request_data_with_metadata)
            assert resp.status_code == 200
            assert resp.json()["choices"][0]["message"]["content"] == "ok"


@pytest.mark.asyncio
async def test_openai_spec_metadata_required_fail(openai_request_data):
    server = ls.LitServer(MetadataRequiredAPI(spec=OpenAISpec()))

    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/chat/completions", json=openai_request_data)
            assert resp.status_code == 500
            assert "Missing required metadata" in resp.text


class TestAPIWithReasoningEffort(TestAPI):
    def encode_response(self, output, context):
        yield ChatMessage(
            role="assistant",
            content=f"This is a generated output with reasoning effort: {context.get('reasoning_effort', None)}",
        )


@pytest.mark.asyncio
@pytest.mark.parametrize("reasoning_effort", ["low", "medium", "high", None, "random"])
async def test_openai_spec_reasoning_effort(reasoning_effort, openai_request_data):
    server = ls.LitServer(TestAPIWithReasoningEffort(spec=OpenAISpec()))
    openai_request_data["reasoning_effort"] = reasoning_effort
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/chat/completions", json=openai_request_data)
            if reasoning_effort == "random":
                assert resp.status_code == 422  # as random is not a valid reasoning effort
            else:
                assert resp.status_code == 200
                assert (
                    resp.json()["choices"][0]["message"]["content"]
                    == f"This is a generated output with reasoning effort: {reasoning_effort}"
                )


class IncorrectAPI1(ls.LitAPI):
    def setup(self, device):
        self.model = None

    def predict(self, x):
        return "This is a generated output"


class IncorrectAPI2(IncorrectAPI1):
    def predict(self, x):
        yield "This is a generated output"

    def encode_response(self, output):
        return ChatMessage(role="assistant", content="This is a generated output")


@pytest.mark.asyncio
async def test_openai_spec_validation(openai_request_data):
    with pytest.raises(ValueError, match="predict is not a generator"):
        ls.LitServer(IncorrectAPI1(spec=OpenAISpec()))

    with pytest.raises(ValueError, match="encode_response is not a generator"):
        ls.LitServer(IncorrectAPI2(spec=OpenAISpec()))


class PrePopulatedAPI(ls.LitAPI):
    def setup(self, device):
        self.sentence = ["This", " is", " a", " sample", " response"]

    def predict(self, prompt, context):
        for count, token in enumerate(self.sentence, start=1):
            yield token
            if count >= context["max_completion_tokens"]:
                return


@pytest.mark.asyncio
async def test_oai_prepopulated_context(openai_request_data):
    openai_request_data["max_completion_tokens"] = 3
    server = ls.LitServer(PrePopulatedAPI(spec=OpenAISpec()))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/chat/completions", json=openai_request_data, timeout=10)
            assert resp.json()["choices"][0]["message"]["content"] == "This is a", (
                "OpenAISpec must return only 3 tokens as specified using `max_completion_tokens` parameter"
            )


class WrongLitAPI(ls.LitAPI):
    def setup(self, device):
        self.model = None

    def predict(self, prompt):
        yield "This is a sample generated text"
        raise HTTPException(501, "test LitAPI.predict error")


@pytest.mark.asyncio
async def test_fail_http(openai_request_data):
    server = ls.LitServer(WrongLitAPI(spec=OpenAISpec()))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            res = await ac.post("/v1/chat/completions", json=openai_request_data, timeout=10)
            assert res.status_code == 501, f"Server raises 501 error: {res.content}"
            assert res.text == '{"detail":"test LitAPI.predict error"}'


class IncorrectAsyncAPI(ls.LitAPI):
    def setup(self, device):
        self.model = None

    async def decode_request(self, request):
        return request

    async def predict(self, x):
        return "This is a generated output"

    async def encode_response(self, output):
        return ChatMessage(role="assistant", content="This is a generated output")


class IncorrectDecodeAsyncAPI(IncorrectAsyncAPI):
    def decode_request(self, request):
        return request


class IncorrectEncodeAsyncAPI(IncorrectAsyncAPI):
    async def predict(self, x):
        yield "This is a generated output"


@pytest.mark.asyncio
async def test_openai_spec_asyncapi_predict_validation():
    with pytest.raises(ValueError, match="predict must be an async generator"):
        ls.LitServer(IncorrectAsyncAPI(enable_async=True, spec=OpenAISpec()))


@pytest.mark.asyncio
async def test_openai_spec_asyncapi_encode_response_validation():
    with pytest.raises(ValueError, match="encode_response is neither a generator nor an async generator"):
        ls.LitServer(IncorrectEncodeAsyncAPI(enable_async=True, spec=OpenAISpec()))


@pytest.mark.asyncio
def test_openai_asyncapi_enable_async_flag_validation():
    with pytest.raises(ValueError, match="'enable_async' is not set in LitAPI."):
        ls.LitServer(IncorrectAsyncAPI(enable_async=False, spec=OpenAISpec()))


class DecodeNotImplementedAsyncOpenAILitAPI(ls.LitAPI):
    def setup(self, device):
        self.model = None

    async def predict(self, x):
        yield "This is a generated output"

    async def encode_response(self, output):
        yield {"role": "assistant", "content": output}


class AsyncOpenAILitAPI(ls.LitAPI):
    def setup(self, device):
        self.model = None
        self.sentence = ["This", " is", " a", " sample", " response"]

    async def decode_request(self, request):
        return request

    async def predict(self, x):
        for token in self.sentence:
            yield token

    async def encode_response(self, output_stream, context):
        async for output in output_stream:
            yield {"role": "assistant", "content": output}


@pytest.mark.asyncio
async def test_openai_spec_with_async_litapi(openai_request_data):
    server = ls.LitServer(AsyncOpenAILitAPI(enable_async=True, spec=OpenAISpec()))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post("/v1/chat/completions", json=openai_request_data, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"

            assert resp.json()["choices"][0]["message"]["content"] == "This is a sample response", (
                "LitAPI predict response should match with the generated output"
            )


@pytest.mark.asyncio
@pytest.mark.parametrize("api_path", ["/v1/chat/completions", "/v2/chat/completions"])
async def test_openai_spec_with_custom_api_path(api_path, openai_request_data):
    server = ls.LitServer(TestAPI(spec=OpenAISpec(), api_path=api_path))
    with wrap_litserve_start(server) as server:
        async with (
            LifespanManager(server.app) as manager,
            AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://test") as ac,
        ):
            resp = await ac.post(api_path, json=openai_request_data, timeout=10)
            assert resp.status_code == 200, "Status code should be 200"
            assert resp.json()["choices"][0]["message"]["content"] == "This is a generated output"


@pytest.mark.asyncio
async def test_openai_spec_custom_api_path_warning():
    with pytest.warns(UserWarning, match="Custom API path detected"):
        ls.LitServer(TestAPI(spec=OpenAISpec(), api_path="/v2/chat/completions"))
```

## File: `tests/unit/test_torch.py`
```python
# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pytest
import torch
import torch.nn as nn
from fastapi import Request, Response
from fastapi.testclient import TestClient

from litserve import LitAPI, LitServer
from litserve.utils import wrap_litserve_start


class Linear(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)
        self.linear.weight.data.fill_(2.0)
        self.linear.bias.data.fill_(1.0)

    def forward(self, x):
        return self.linear(x)


class SimpleLitAPI(LitAPI):
    def setup(self, device):
        self.model = Linear().to(device)
        self.device = device

    def decode_request(self, request: Request):
        content = request["input"]
        return torch.tensor([content], device=self.device)

    def predict(self, x):
        return self.model(x[None, :])

    def encode_response(self, output) -> Response:
        return {"output": float(output)}


def test_torch():
    server = LitServer(SimpleLitAPI(), accelerator="cpu", devices=1, timeout=10)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0})
        assert response.json() == {"output": 9.0}


@pytest.mark.skipif(torch.cuda.device_count() == 0, reason="requires CUDA to be available")
def test_torch_gpu():
    server = LitServer(SimpleLitAPI(), accelerator="cuda", devices=1, timeout=10)
    with wrap_litserve_start(server) as server, TestClient(server.app) as client:
        response = client.post("/predict", json={"input": 4.0})
        assert response.json() == {"output": 9.0}
```

## File: `tests/unit/test_transport.py`
```python
import asyncio
import multiprocessing as mp
from queue import Empty
from unittest.mock import MagicMock, patch

import pytest

from litserve.transport.factory import TransportConfig, create_transport_from_config
from litserve.transport.process_transport import MPQueueTransport


class TestMPQueueTransport:
    @pytest.fixture
    def manager(self):
        manager = mp.Manager()
        yield manager
        manager.shutdown()

    @pytest.fixture
    def queues(self, manager):
        return [manager.Queue() for _ in range(2)]

    @pytest.fixture
    def transport(self, manager, queues):
        return MPQueueTransport(manager, queues)

    def test_init(self, transport, queues):
        """Test that the transport initializes correctly."""
        assert transport._queues == queues
        assert transport._closed is False

    def test_send(self, transport, queues):
        test_item = {"test": "data"}
        consumer_id = 0

        transport.send(test_item, consumer_id)

        assert queues[consumer_id].get() == test_item

    def test_send_when_closed(self, transport):
        transport._closed = True
        test_item = {"test": "data"}
        consumer_id = 0

        result = transport.send(test_item, consumer_id)

        assert result is None

    @pytest.mark.asyncio
    async def test_areceive(self, transport, queues):
        test_item = {"test": "data"}
        consumer_id = 0
        queues[consumer_id].put(test_item)

        result = await transport.areceive(consumer_id)

        assert result == test_item

    @pytest.mark.asyncio
    async def test_areceive_when_closed(self, transport):
        transport._closed = True
        consumer_id = 0

        with pytest.raises(asyncio.CancelledError, match="Transport closed"):
            await transport.areceive(consumer_id)

    @pytest.mark.asyncio
    async def test_areceive_timeout(self, transport):
        consumer_id = 0
        timeout = 0.1

        with pytest.raises(Empty):
            await transport.areceive(consumer_id, timeout=timeout)

    @pytest.mark.asyncio
    async def test_areceive_cancellation(self, transport):
        consumer_id = 0

        with patch("asyncio.to_thread", side_effect=asyncio.CancelledError), pytest.raises(asyncio.CancelledError):
            await transport.areceive(consumer_id)

    def test_close(self, transport, queues):
        transport.close()

        assert transport._closed is True
        for queue in queues:
            assert queue.get() is None

    def test_reduce(self, transport, queues):
        cls, args = transport.__reduce__()

        assert cls == MPQueueTransport
        assert args == (None, queues)


class TestTransportFactory:
    @pytest.fixture
    def mock_manager(self):
        return MagicMock()

    def test_create_mp_transport(self, mock_manager):
        config_dict = {"transport_type": "mp", "num_consumers": 2}
        config = TransportConfig(**config_dict)

        with patch("litserve.transport.factory._create_mp_transport") as mock_create:
            mock_create.return_value = MPQueueTransport(mock_manager, [MagicMock(), MagicMock()])

            transport = create_transport_from_config(config)

            assert isinstance(transport, MPQueueTransport)
            mock_create.assert_called_once()

    def test_create_transport_invalid_type(self):
        with patch("litserve.transport.factory.TransportConfig.model_validate") as mock_validate:
            mock_validate.return_value = MagicMock(transport_type="invalid")

            with pytest.raises(ValueError, match="Invalid transport type"):
                create_transport_from_config(mock_validate.return_value)


@pytest.mark.integration
class TestTransportIntegration:
    """Integration tests for the transport system."""

    @pytest.fixture
    def mock_transport(self):
        transport = MagicMock()
        transport._closed = False
        transport._waiting_tasks = []

        transport.send = MagicMock()

        async def mock_areceive(consumer_id, timeout=None, block=True):
            current_task = asyncio.current_task()
            transport._waiting_tasks.append(current_task)

            try:
                if transport._closed:
                    raise asyncio.CancelledError("Transport closed")

                await asyncio.sleep(10)  # Long sleep to ensure we'll be cancelled

                # This should only be reached if not cancelled
                return ("test_id", {"test": "data"})
            finally:
                # Clean up task reference
                if current_task in transport._waiting_tasks:
                    transport._waiting_tasks.remove(current_task)

        transport.areceive = mock_areceive

        def mock_close():
            transport._closed = True
            for task in transport._waiting_tasks:
                task.cancel()

        transport.close = mock_close

        return transport

    @pytest.mark.asyncio
    async def test_send_receive_cycle(self, mock_transport):
        """Test a complete send-receive cycle."""
        # Arrange
        test_item = ("test_id", {"test": "data"})
        consumer_id = 0

        # Act - Send
        mock_transport.send(test_item, consumer_id)

        # Act - Receive
        result = await mock_transport.areceive(consumer_id)

        # Assert
        assert result == test_item
        mock_transport.send.assert_called_once_with(test_item, consumer_id)

    @pytest.mark.asyncio
    async def test_shutdown_sequence(self, mock_transport):
        """Test the shutdown sequence works correctly."""
        # Arrange
        consumer_id = 0

        async def receive_task():
            try:
                await mock_transport.areceive(consumer_id)
                return False  # Should not reach here if cancelled
            except asyncio.CancelledError:
                return True  # Successfully cancelled

        task = asyncio.create_task(receive_task())
        await asyncio.sleep(0.1)

        # Act
        mock_transport.close()
        result = await asyncio.wait_for(task, timeout=2.0)

        # Assert
        assert result is True
```

## File: `tests/unit/test_utils.py`
```python
import base64
import logging
import os
import pickle
import sys
from pathlib import Path
from unittest import mock
from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from litserve.utils import (
    add_ssl_context_from_env,
    azip,
    call_after_stream,
    configure_logging,
    dump_exception,
    generate_random_zmq_address,
    is_package_installed,
    set_trace_if_debug,
)


def test_dump_exception():
    e1 = dump_exception(HTTPException(status_code=404, detail="Not Found"))
    assert isinstance(e1, bytes)

    exc = HTTPException(400, "Custom Lit error")
    isinstance(pickle.loads(dump_exception(exc)), HTTPException)
    assert pickle.loads(dump_exception(exc)).detail == "Custom Lit error"
    assert pickle.loads(dump_exception(exc)).status_code == 400


async def dummy_streamer():
    for i in range(10):
        yield i


@pytest.mark.asyncio
async def test_call_after_stream():
    callback = MagicMock()
    callback.return_value = None
    streamer = dummy_streamer()
    async for _ in call_after_stream(streamer, callback, "first_arg", random_arg="second_arg"):
        pass
    callback.assert_called()
    callback.assert_called_with("first_arg", random_arg="second_arg")


async def _stream_values(*values):
    for value in values:
        yield value


async def _stream_error():
    yield ("ok", "status")
    raise RuntimeError("stream failed")


@pytest.mark.asyncio
async def test_azip_stops_at_shortest_stream():
    zipped = []
    async for item in azip(_stream_values(1, 2), _stream_values("a")):
        zipped.append(item)

    assert zipped == [(1, "a")]


@pytest.mark.asyncio
async def test_azip_propagates_stream_errors():
    with pytest.raises(RuntimeError, match="stream failed"):
        async for _ in azip(_stream_error(), _stream_values(("ok", "status"), ("next", "status"))):
            pass


@pytest.mark.skipif(sys.platform == "win32", reason="This test is for non-Windows platforms only.")
def test_generate_random_zmq_address_non_windows(tmpdir):
    """Test generate_random_zmq_address on non-Windows platforms."""

    temp_dir = str(tmpdir)
    address1 = generate_random_zmq_address(temp_dir=temp_dir)
    address2 = generate_random_zmq_address(temp_dir=temp_dir)

    assert address1.startswith("ipc://"), "Address should start with 'ipc://'"
    assert address2.startswith("ipc://"), "Address should start with 'ipc://'"
    assert address1 != address2, "Addresses should be unique"

    # Verify the path exists within the specified temp_dir
    assert os.path.commonpath([temp_dir, address1[6:]]) == temp_dir
    assert os.path.commonpath([temp_dir, address2[6:]]) == temp_dir


def test_configure_logging():
    configure_logging(use_rich=False)
    assert logging.getLogger("litserve").handlers[0].__class__.__name__ == "StreamHandler"


def test_configure_logging_rich_not_installed():
    # patch builtins.__import__ to raise ImportError
    with mock.patch("builtins.__import__", side_effect=ImportError):
        configure_logging(use_rich=True)
        assert logging.getLogger("litserve").handlers[0].__class__.__name__ == "StreamHandler"


@mock.patch("litserve.utils.set_trace")
def test_set_trace_if_debug(mock_set_trace):
    # mock environ
    with mock.patch("litserve.utils.os.environ", {"LITSERVE_DEBUG": "1"}):
        set_trace_if_debug()
    mock_set_trace.assert_called_once()


@mock.patch("litserve.utils.ForkedPdb")
def test_set_trace_if_debug_not_set(mock_forked_pdb):
    with mock.patch("litserve.utils.os.environ", {"LITSERVE_DEBUG": "0"}):
        set_trace_if_debug()
    mock_forked_pdb.assert_not_called()


def test_is_package_installed():
    assert is_package_installed("pytest")
    assert not is_package_installed("nonexistent_package")


def test_add_ssl_context_from_env_with_env_vars():
    """Tests that the SSL context is loaded correctly when environment variables are set."""
    dummy_cert = "dummy certificate"
    dummy_key = "dummy key"

    b64_cert = base64.b64encode(dummy_cert.encode("utf-8")).decode("utf-8")
    b64_key = base64.b64encode(dummy_key.encode("utf-8")).decode("utf-8")

    with mock.patch.dict(os.environ, {"LIGHTNING_CERT_PEM": b64_cert, "LIGHTNING_KEY_FILE": b64_key}):
        ssl_context = add_ssl_context_from_env({})

        assert ssl_context

        assert "ssl_certfile" in ssl_context
        assert "ssl_keyfile" in ssl_context
        assert isinstance(ssl_context["ssl_certfile"], Path)
        assert isinstance(ssl_context["ssl_keyfile"], Path)

        with open(ssl_context["ssl_certfile"]) as f:
            assert f.read() == dummy_cert
        with open(ssl_context["ssl_keyfile"]) as f:
            assert f.read() == dummy_key

        os.remove(ssl_context["ssl_certfile"])
        os.remove(ssl_context["ssl_keyfile"])


def test_add_ssl_context_from_env_without_env_vars():
    """Tests that an empty dictionary is returned when environment variables are not set."""
    with mock.patch.dict(os.environ, {}, clear=True):
        ssl_context = add_ssl_context_from_env({})
        assert ssl_context == {}


def test_add_ssl_context_from_env_with_one_env_var_missing():
    """Tests that an empty dictionary is returned when one of the environment variables is missing."""
    dummy_cert = "dummy certificate"
    b64_cert = base64.b64encode(dummy_cert.encode("utf-8")).decode("utf-8")

    with mock.patch.dict(os.environ, {"LIGHTNING_CERT_PEM": b64_cert}, clear=True):
        ssl_context = add_ssl_context_from_env({})
        assert ssl_context == {}
```

## File: `tests/unit/test_zmq_queue.py`
```python
import asyncio
import pickle
from queue import Empty
from unittest.mock import AsyncMock, Mock, patch

import pytest
import zmq

from litserve.transport.zmq_queue import AsyncConsumer, Broker, Producer


@pytest.fixture
def mock_context():
    with patch("zmq.Context") as mock_ctx:
        socket = Mock()
        mock_ctx.return_value.socket.return_value = socket
        yield mock_ctx, socket


@pytest.fixture
def mock_async_context():
    with patch("zmq.asyncio.Context") as mock_ctx:
        socket = AsyncMock()  # Use AsyncMock for async methods
        mock_ctx.return_value.socket.return_value = socket
        yield mock_ctx, socket


def test_broker_start_stop(mock_context):
    _, socket = mock_context
    broker = Broker(use_process=False)

    # Start broker
    broker.start()
    assert socket.bind.call_count == 2  # Should bind both frontend and backend

    # Stop broker
    broker.stop()
    assert socket.close.call_count == 2  # Should close both sockets


def test_broker_error_handling(mock_context):
    """Test broker handles ZMQ errors."""
    _, socket = mock_context
    socket.bind.side_effect = zmq.ZMQError("Test error")

    broker = Broker(use_process=False)
    broker.start()
    broker.stop()

    assert socket.close.called  # Should clean up even on error


def test_producer_send(mock_context):
    _, socket = mock_context
    producer = Producer(address="test_addr")

    # Test sending simple data
    producer.put("test_data", consumer_id=1)
    sent_message = socket.send.call_args[0][0]
    consumer_id, data = sent_message.split(b"|", 1)
    assert consumer_id == b"1"
    assert pickle.loads(data) == "test_data"

    # Test sending complex data
    complex_data = {"key": [1, 2, 3]}
    producer.put(complex_data, consumer_id=2)
    sent_message = socket.send.call_args[0][0]
    consumer_id, data = sent_message.split(b"|", 1)
    assert consumer_id == b"2"
    assert pickle.loads(data) == complex_data


def test_producer_error_handling(mock_context):
    _, socket = mock_context
    producer = Producer(address="test_addr")

    # Test ZMQ error
    socket.send.side_effect = zmq.ZMQError("Test error")
    with pytest.raises(zmq.ZMQError):
        producer.put("data", consumer_id=1)

    # Test unpickleable object
    class Unpickleable:
        def __reduce__(self):
            raise pickle.PickleError("Can't pickle this!")

    with pytest.raises(pickle.PickleError):
        producer.put(Unpickleable(), consumer_id=1)


def test_producer_wait_for_subscribers(mock_context):
    _, socket = mock_context
    producer = Producer(address="test_addr")

    # Test successful wait
    assert producer.wait_for_subscribers(timeout=0.1)
    assert socket.send.called

    # Test timeout
    socket.send.side_effect = zmq.ZMQError("Would block")
    assert not producer.wait_for_subscribers(timeout=0.1)


@pytest.mark.parametrize("timeout", [1.0, None])
@pytest.mark.asyncio
async def test_async_consumer(mock_async_context, timeout):
    _, socket = mock_async_context
    consumer = AsyncConsumer(consumer_id=1, address="test_addr")

    # Setup mock received data
    test_data = {"test": "data"}
    message = b"1|" + pickle.dumps(test_data)
    socket.recv.return_value = message

    # Test receiving
    received = await consumer.get(timeout=timeout)
    assert received == test_data

    # Test timeout
    socket.recv.side_effect = asyncio.TimeoutError()
    with pytest.raises(Empty):
        await consumer.get(timeout=timeout)


@pytest.mark.asyncio
async def test_async_consumer_cleanup():
    with patch("zmq.asyncio.Context") as mock_ctx:
        socket = AsyncMock()
        mock_ctx.return_value.socket.return_value = socket

        consumer = AsyncConsumer(consumer_id=1, address="test_addr")
        consumer.close()

        assert socket.close.called
        assert mock_ctx.return_value.term.called


def test_producer_cleanup():
    with patch("zmq.Context") as mock_ctx:
        socket = Mock()
        mock_ctx.return_value.socket.return_value = socket

        producer = Producer(address="test_addr")
        producer.close()

        assert socket.close.called
        assert mock_ctx.return_value.term.called
```

