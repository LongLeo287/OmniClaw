---
id: github.com-quivrhq-quivr-e7ca8292-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:16.746550
---

# KNOWLEDGE EXTRACT: github.com_QuivrHQ_quivr_e7ca8292
> **Extracted on:** 2026-04-01 09:45:32
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520425/github.com_QuivrHQ_quivr_e7ca8292

---

## File: `.flake8`
```
[flake8]
; Minimal configuration for Flake8 to work with Black.
max-line-length = 100
ignore = E101,E111,E112,E221,E222,E501,E711,E712,W503,W504,F401,BLK100
```

## File: `.gitignore`
```
docker-compose.override.yml
secondbrain/
.env
env.sh
.streamlit/secrets.toml
**/*.pyc
toto.txt
log.txt

backend/venv
backend/.env
backend/*.deb
backend/.python-version

# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
**/node_modules
**/.pnp
.pnp.js

Pipfile

# testing
**/coverage

# next.js
**/.next/
**/out/

# production
**/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# local env files
.env*.local

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts
quivr/*
streamlit-demo/.streamlit/secrets.toml
.backend_env
.frontend_env
backend/core/pandoc-*
**/.pandoc-*
backend/core/application_default_credentials.json

#local models
backend/core/local_models/*

## scripts
package-lock.json
celerybeat-schedule
frontend/public/robots.txt
frontend/public/sitemap*

pyfiles/*
backend/bin/*
backend/lib/*
backend/pyvenv.cfg
backend/share/*
backend/slim.report.json
volumes/db/data/
volumes/storage/stub/stub/quivr/*
supabase/migrations/20240103191539_private.sql
supabase/20240103191539_private.sql
paulgraham.py
.env_test
supabase/seed-airwallex.sql
airwallexpayouts.py
**/application.log*
backend/celerybeat-schedule.db

backend/application.log.*
backend/score.json
backend/modules/assistant/ito/utils/simple.pdf
backend/modules/sync/controller/credentials.json
backend/.env.test

**/*.egg-info

.coverage
backend/core/examples/chatbot/.files/*
backend/core/examples/chatbot/.python-version
backend/core/examples/chatbot/.chainlit/config.toml
backend/core/examples/chatbot/.chainlit/translations/en-US.json

*.log

# Tox
.tox
Pipfile
*.pkl
backend/docs/site/*
```

## File: `.pre-commit-config.yaml`
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: check-added-large-files
        args: ["--maxkb=5000"]
      - id: check-toml
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-merge-conflict
      - id: detect-private-key
      - id: check-case-conflict
  - repo: https://github.com/pre-commit/pre-commit
    rev: v3.6.2
    hooks:
      - id: validate_manifest
  - repo: https://github.com/astral-sh/ruff-pre-commit
    # Ruff version.
    rev: v0.5.1
    hooks:
      # Run the linter.
      - id: ruff
        args: [--fix, --isolated]
        additional_dependencies: []
      # Run the formatter.
      - id: ruff-format
        args: [--isolated]
        additional_dependencies: []
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.1
    hooks:
      - id: mypy
        name: mypy
        args: ["--ignore-missing-imports", "--no-incremental", "--follow-imports=skip"]
        additional_dependencies: ["types-aiofiles", "types-pyyaml", "pydantic", "sqlmodel"]
ci:
  autofix_commit_msg: |
    [pre-commit.ci] auto fixes from pre-commit.com hooks

    for more information, see https://pre-commit.ci
  autofix_prs: true
  autoupdate_branch: ""
  autoupdate_commit_msg: "[pre-commit.ci] pre-commit autoupdate"
  autoupdate_schedule: weekly
  skip: []
  submodules: false
```

## File: `.python-version`
```
3.11.9
```

## File: `.readthedocs.yaml`
```yaml
# Read the Docs configuration file for MkDocs projects
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the version of Python and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
  commands:
    - asdf plugin add uv
    - asdf install uv latest
    - asdf global uv latest
    - uv venv
    - cd docs && UV_INDEX_STRATEGY=unsafe-first-match uv pip install -r requirements.lock
    - cd docs/ && ls -la && NO_COLOR=1 ../.venv/bin/mkdocs build --strict --site-dir $READTHEDOCS_OUTPUT/html --config-file mkdocs.yml

  


mkdocs:
  configuration: backend/docs/mkdocs.yml

```

## File: `.release-please-manifest.json`
```json
{
    "core": "0.0.33"
}
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## 0.0.322 (2024-10-15)

## What's Changed
* feat: Add new documentation files by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3351
* fix: separate english and french ingredients by @chloedia in https://github.com/QuivrHQ/quivr/pull/3358
* docs(core): init by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3365
* docs: quivr core storage by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3366
* fix: fixing pdf parsing by @jacopo-chevallard in https://github.com/QuivrHQ/quivr/pull/3349
* feat: Improve user credit calculation in get_user_credits by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3367
* fix unwanted parsing effect by @chloedia in https://github.com/QuivrHQ/quivr/pull/3371
* add fallback on llamaparse by @chloedia in https://github.com/QuivrHQ/quivr/pull/3374


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.321...v0.0.322

## 0.0.321 (2024-10-08)

## What's Changed
* feat: Add file name to knowledge properties in crawl_endpoint by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3346
* feat(frontend): add xlsx by @Zewed in https://github.com/QuivrHQ/quivr/pull/3340


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.320...v0.0.321

## 0.0.320 (2024-10-07)

## What's Changed
* Enable Porter Application cdp by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/3306
* Enable Porter Application cdp-front by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/3307
* feat(assistant): cdp by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3305
* feat: Add debug logging for OCR results by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3309
* feat: Update OCR image scale for better accuracy by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3310
* feat: Update PDFGenerator to include logo in header by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3311
* feat: structlog parseable by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3312
* Revert "feat: structlog parseable" by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3313
* feat: structlog parseable by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3314
* Revert "feat: structlog parseable" by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3315
* feat: Update PDFGenerator to include logo in header by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3318
* feat: structlog parseable by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3319
* feat: Update knowledge status and send notification on task success by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3320
* feat: Update text retranscription instructions by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3321
* feat: update sentry by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3326
* chore: Remove unnecessary assertion in create_modification_report function by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3329
* chore: Add NEXT_PUBLIC_INTERCOM_APP_ID to Dockerfile by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3330
* feat: Update Content Security Policy for PostHog by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3331
* fix(cdp): order naming cdc_etiquette by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3333
* fix(notifications): added a debouncing mechanism by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3327


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.319...v0.0.320

## 0.0.319 (2024-10-01)

## What's Changed
* feat: Add error handling for rate-limited search in fetch_notion_pages by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3298
* feat: Remove syncNotion from ConnectionCards by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3300


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.318...v0.0.319

## 0.0.318 (2024-09-30)

## What's Changed
* feat: add syncNotion from ConnectionCards by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3292


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.317...v0.0.318

## 0.0.317 (2024-09-30)

## What's Changed
* feat: update SyncsUser status field to be optional by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3284
* fix(frontend): onboarding modal by @Zewed in https://github.com/QuivrHQ/quivr/pull/3286
* feat: Remove syncNotion from ConnectionCards by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3289


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.316...v0.0.317

## 0.0.316 (2024-09-30)

## What's Changed
* fix(core): enforce langchain <0.3 for pydantic v1 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3217
* chore(main): release core 0.0.16 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3218
* feat(assistants): mock api by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3195
* chore(examples): fix chainlit example  by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3223
* feat(integration): Notion by @chloedia in https://github.com/QuivrHQ/quivr/pull/3173
* fix(migration): order migrations by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3231
* feat: remove n+1 query knowledge by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3238
* feat: introducing configurable retrieval workflows by @jacopo-chevallard in https://github.com/QuivrHQ/quivr/pull/3227
* fix: wrong default path for CHAT_LLM_CONFIG_PATH env variable by @jacopo-chevallard in https://github.com/QuivrHQ/quivr/pull/3247
* fix(frontend): sync folder for premium users by @Zewed in https://github.com/QuivrHQ/quivr/pull/3251
* fix: correctly passing the prompt provided by the user by @jacopo-chevallard in https://github.com/QuivrHQ/quivr/pull/3252
* fix: add sync user id aget_files by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3261
* feat: update sync_user.py to include sync user id in aget_files call by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3276
* chore: update Dockerfile dependencies and copy files by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3277
* chore: add wget to Dockerfile dependencies by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3279


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.315...v0.0.316

## 0.0.315 (2024-09-17)

## What's Changed
* chore(main): release core 0.0.15 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3203
* fix: knowledge user_id fix by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3216


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.314...v0.0.315

## 0.0.314 (2024-09-16)

## What's Changed
* feat:  CRUD KMS (no syncs)  by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3162


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.313...v0.0.314

## 0.0.313 (2024-09-13)

## What's Changed
* feat: save and load brain by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3202


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.312...v0.0.313

## 0.0.312 (2024-09-13)

## What's Changed
* fix: Update LLMEndpoint to include max_tokens parameter by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3201


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.311...v0.0.312

## 0.0.311 (2024-09-12)

## What's Changed
* chore(embeddings): added tests for embeddings by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3183
* feat(uptime): check if connection to db works by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3199


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.310...v0.0.311

## 0.0.310 (2024-09-10)

## What's Changed
* feat: Add Azure OpenAI embeddings support by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3182


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.309...v0.0.310

## 0.0.309 (2024-09-10)

## What's Changed
* chore: Add initial documentation files and configuration by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3126
* chore: Add .readthedocs.yaml configuration file by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3172
* fix(frontend): notion integration in front end by @Zewed in https://github.com/QuivrHQ/quivr/pull/3175
* chore(main): release core 0.0.14 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2945
* ci(rye): now core is built with rye by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3177
* feat: Add external Supabase URL support for generating file signed URL by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3179
* fix(onboarding): keeps setting it at false by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3180


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.308...v0.0.309

## 0.0.308 (2024-09-06)

## What's Changed
* fix: remove knowledge and idle conn by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3165


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.307...v0.0.308

## 0.0.307 (2024-09-06)

## What's Changed
* fix: tests pytest-asyncio by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3157
* fix: remove unused 'models' field in check_premium.py by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3164


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.306...v0.0.307

## 0.0.306 (2024-09-05)

## What's Changed
* feat(readme): trigger deploy by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3159


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.305...v0.0.306

## 0.0.305 (2024-09-05)

## What's Changed
* chore: update next.config.js with PostHog domains by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3155


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.304...v0.0.305

## 0.0.304 (2024-09-05)

## What's Changed
* feat: update Azure login button text by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3152
* fix: url knowledge multiple brain by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3145
* chore: update Dockerfile with PostHog environment variables by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3154


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.303...v0.0.304

## 0.0.303 (2024-09-04)

## What's Changed
* fix(chat): order of chat history was reversed by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3148


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.302...v0.0.303

## 0.0.302 (2024-09-04)

## What's Changed
* feat(anthropic): add llm by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3146


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.301...v0.0.302

## 0.0.301 (2024-09-03)

## What's Changed
* feat(smtp): not enforcing tls by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3067
* feat: Update send_email.py to conditionally login with SMTP credentials by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3069
* feat: Add NEXT_PUBLIC_PROJECT_NAME environment variable by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3070
* feat: Add Azure login support by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3071
* fix(frontend): only owner can access knowledge and edit brain snippet by @Zewed in https://github.com/QuivrHQ/quivr/pull/3073
* fix(frontend): brain knowledge visibility by @Zewed in https://github.com/QuivrHQ/quivr/pull/3074
* fix(frontend): revamp of settings  by @Zewed in https://github.com/QuivrHQ/quivr/pull/3081
* fix: Update README.md by @Zewed in https://github.com/QuivrHQ/quivr/pull/3084
* fix(frontend): send invitation clearer by @Zewed in https://github.com/QuivrHQ/quivr/pull/3090
* fix(frontend): spacing chats by @Zewed in https://github.com/QuivrHQ/quivr/pull/3091
* fix(frontend): use click delay by @Zewed in https://github.com/QuivrHQ/quivr/pull/3092
* fix(frontend): back buttons by @Zewed in https://github.com/QuivrHQ/quivr/pull/3094
* fix(frontend): change hover delay for tooltips by @Zewed in https://github.com/QuivrHQ/quivr/pull/3095
* fix(frontend): rename search by thread by @Zewed in https://github.com/QuivrHQ/quivr/pull/3099
* feat(frontend): revamp of some basics components by @Zewed in https://github.com/QuivrHQ/quivr/pull/3105
* feat(frontend): interaction with brain items by @Zewed in https://github.com/QuivrHQ/quivr/pull/3106
* fix(frontend): remove intercom on thread page of mobile by @Zewed in https://github.com/QuivrHQ/quivr/pull/3108
* feat:  quivr core 0.1 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2970
* fix: Blank scrollbar on certain browsers by @adityanandanx in https://github.com/QuivrHQ/quivr/pull/3118
* chore(docs): moved repository by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3123
* fix: knowledge user by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3124
* chore(readme): increase size icon by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3125
* chore: remove unused syncNotion function in ConnectionCards.tsx by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3129
* chore: update compatibility by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3136
* ci(raise): only on tags by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3140
* feat: using langgraph in our RAG pipeline by @jacopo-chevallard in https://github.com/QuivrHQ/quivr/pull/3130
* fix: knowledge multiple brains by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3142
* fix: knowledge multiple brains - update knowledge rollback by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3143

## New Contributors
* @jacopo-chevallard made their first contribution in https://github.com/QuivrHQ/quivr/pull/3130

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.300...v0.0.301

## 0.0.300 (2024-08-22)

## What's Changed
* feat(smtp&share): implemented smtp support and fixed share brain by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3049


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.299...v0.0.300

## 0.0.299 (2024-08-22)

## What's Changed
* fix: Update Supabase configuration by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3014
* Delete Porter Application theodo-backend by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/3022
* Delete Porter Application theodo-frontend by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/3023
* feat(frontend): emoji selector component by @Zewed in https://github.com/QuivrHQ/quivr/pull/3024
* feat(frontend): show or hide tokens relative stuff by @Zewed in https://github.com/QuivrHQ/quivr/pull/3017
* feat(frontend): color picker by @Zewed in https://github.com/QuivrHQ/quivr/pull/3027
* fix(frontend): small stuff on mobile by @Zewed in https://github.com/QuivrHQ/quivr/pull/3039
* feat(frontend): handle LaTeX in message thread by @Zewed in https://github.com/QuivrHQ/quivr/pull/3040
* fix(frontend): fix docker build frontend new env by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3041
* feat(frontend): brain snippet selector by @Zewed in https://github.com/QuivrHQ/quivr/pull/3038
* feat: Add environment variable for showing tokens in frontend by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3048
* fix(frontend): color icon for blocks by @Zewed in https://github.com/QuivrHQ/quivr/pull/3042


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.298...v0.0.299

## 0.0.298 (2024-08-16)

## What's Changed
* feat(azure): quivr compatible with it by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3005
* feat(frontend): helpbox by @Zewed in https://github.com/QuivrHQ/quivr/pull/3007
* feat(frontend): order models and brain by name by @Zewed in https://github.com/QuivrHQ/quivr/pull/3009
* fix(frontend): help window by @Zewed in https://github.com/QuivrHQ/quivr/pull/3013


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.297...v0.0.298

## 0.0.297 (2024-08-14)

## What's Changed
* fix(frontend): remove onboarding modal by @Zewed in https://github.com/QuivrHQ/quivr/pull/3001
* fix(frontend): max height for user message by @Zewed in https://github.com/QuivrHQ/quivr/pull/3000
* fix: commit on try sqlalchemy by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3004


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.296...v0.0.297

## 0.0.296 (2024-08-13)

## What's Changed
* fix(frontend): color of copy icon for code blocks by @Zewed in https://github.com/QuivrHQ/quivr/pull/2993
* fix(frontend): search bar height by @Zewed in https://github.com/QuivrHQ/quivr/pull/2998
* fix: autocommit isolation level by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2999


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.295...v0.0.296

## 0.0.295 (2024-08-12)

## What's Changed
* chore: Update frontend README.md with yarn dev command (#2931) by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2958
* feat: Add brain_id and brain_name to ChatLLMMetadata model by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2968
* feat(frontend): talk with models and handle code markdown by @Zewed in https://github.com/QuivrHQ/quivr/pull/2980
* fix(frontend): talk with models by @Zewed in https://github.com/QuivrHQ/quivr/pull/2981
* feat(models): all models by default by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2983
* chore(env): add deactivate stripe env variable by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2986
* fix(frontend): handling unimported languages in Prism js by @Zewed in https://github.com/QuivrHQ/quivr/pull/2990
* fix(frontend): logo design of models by @Zewed in https://github.com/QuivrHQ/quivr/pull/2992


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.294...v0.0.295

## 0.0.294 (2024-08-07)

## What's Changed
* Delete Porter Application quivr-com by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2927
* Delete Porter Application quivr-com-backend by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2928
* feat: quivr core tox test + parsers by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2929
* feat(frontend): handle no brain selection by @Zewed in https://github.com/QuivrHQ/quivr/pull/2932
* fix: processor quivr version by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2934
* fix: quivr core fix tests by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2935
* chore(main): release core 0.0.13 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2930
* feat: Add GitHub sync functionality to sync router by @chloedia in https://github.com/QuivrHQ/quivr/pull/2871
* refactor: Remove syncGitHub function from useSync.ts by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2942
* feat: add chat with models by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2933
* ci: precommit in CI by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2946
* feat: Add get_model method to ModelRepository by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2949
* feat: Add user email to StripePricingOrManageButton and UpgradeToPlusButton components by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2951


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.293...v0.0.294

## 0.0.293 (2024-07-30)

## What's Changed
* feat(frontend): brain carousel by @Zewed in https://github.com/QuivrHQ/quivr/pull/2924
* fix(frontend): feedback for brain carousel by @Zewed in https://github.com/QuivrHQ/quivr/pull/2926


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.292...v0.0.293

## 0.0.292 (2024-07-29)

## What's Changed
* Feat/handle_azure_sites by @chloedia in https://github.com/QuivrHQ/quivr/pull/2921
* feat: update dev command in frontend README.md by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2922


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.291...v0.0.292

## 0.0.291 (2024-07-29)

## What's Changed
* feat(integrations): Add Azure Drive Sites support by @chloedia in https://github.com/QuivrHQ/quivr/pull/2919
* chore: update sync notification status to INFO by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2918


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.290...v0.0.291

## 0.0.290 (2024-07-26)

## What's Changed
* fix(frontend): remove possibility to sync folder by @Zewed in https://github.com/QuivrHQ/quivr/pull/2913
* fix(frontend): remove latence for delete notifications by @Zewed in https://github.com/QuivrHQ/quivr/pull/2916
* fix(backend): fix error messages by @Zewed in https://github.com/QuivrHQ/quivr/pull/2917
* feat(notifications): improved requirements by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2915


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.289...v0.0.290

## 0.0.289 (2024-07-25)

## What's Changed
* chore(main): release core 0.0.12 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2889
* fix: error dict google drive by @chloedia in https://github.com/QuivrHQ/quivr/pull/2912


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.288...v0.0.289

## 0.0.288 (2024-07-23)

## What's Changed
* fix(sync): folder upload to Google Drive by @chloedia in https://github.com/QuivrHQ/quivr/pull/2909


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.287...v0.0.288

## 0.0.287 (2024-07-23)

## What's Changed
* feat: Update AzureDriveSync name to "Share Point" by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2907


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.286...v0.0.287

## 0.0.286 (2024-07-23)

## What's Changed
* fix(frontend): remove warning in frontend by @Zewed in https://github.com/QuivrHQ/quivr/pull/2896
* feat(frontend): add logo to source when integration by @Zewed in https://github.com/QuivrHQ/quivr/pull/2899
* feat(premium): add trialing by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2900
* feat: Remove unused onboarding code by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2901
* feat(dead-code): removed composite & api by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2902
* feat(frontend): add a loader when processing files by @Zewed in https://github.com/QuivrHQ/quivr/pull/2903
* feat(frontend): icon chevron for folders by @Zewed in https://github.com/QuivrHQ/quivr/pull/2904
* feat(frontend): loader icon for integrations by @Zewed in https://github.com/QuivrHQ/quivr/pull/2905
* fix(frontend): remove current brain id when click on create brain by @Zewed in https://github.com/QuivrHQ/quivr/pull/2906


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.285...v0.0.286

## 0.0.285 (2024-07-22)

## What's Changed
* fix(frontend): select line when click on knowledge option by @Zewed in https://github.com/QuivrHQ/quivr/pull/2879
* fix(frontend): selected item on mention list by @Zewed in https://github.com/QuivrHQ/quivr/pull/2881
* fix(frontend): logo color on dark mode by @Zewed in https://github.com/QuivrHQ/quivr/pull/2882
* fix: Refacto & update dropbox refresh by @chloedia in https://github.com/QuivrHQ/quivr/pull/2875
* feat: quivr core brain info + processors registry +  by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2877
* chore(main): release core 0.0.10 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2872
* feat: move parsers quivr core by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2884
* fix(frontend): default icon for knowledge without extension by @Zewed in https://github.com/QuivrHQ/quivr/pull/2887
* chore(main): release core 0.0.11 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2886
* feat(frontend): add knowledge icon when integration by @Zewed in https://github.com/QuivrHQ/quivr/pull/2888
* fix: google conversion by @chloedia in https://github.com/QuivrHQ/quivr/pull/2891
* fix(frontend): remove thoughts button by @Zewed in https://github.com/QuivrHQ/quivr/pull/2892
* feat: add integration and integration link to Sources class by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2893
* feat(azure): changed auth method by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2890
* feat(frontend): new inputs by @Zewed in https://github.com/QuivrHQ/quivr/pull/2894
* fix(frontend): menu on mobile by @Zewed in https://github.com/QuivrHQ/quivr/pull/2895
* feat(api): add logging for inactive subscriptions by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2897


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.284...v0.0.285

## 0.0.284 (2024-07-17)

## What's Changed
* chore(cleanup): cleaned up some unused files by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2858
* feat: Improve file loading logic in File model by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2861
* feat(celery): add retry logic for dcos by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2862
* feat: quivr api send notification by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2865
* feat: Update category for sync notification by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2866
* feat: Update crawl_endpoint to include knowledge_id in task kwargs by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2867
* feat(integrations): Add integration fields to Knowledge and SyncsUser models by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2853
* feat: quivr api use quivr core by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2868
* feat: Update sync generic bulk by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2869
* chore(main): release core 0.0.9 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2855
* feat(frontend): new notifications design by @Zewed in https://github.com/QuivrHQ/quivr/pull/2870
* feat: Update sync active notification category by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2873
* feat(integrations): dropbox by @chloedia in https://github.com/QuivrHQ/quivr/pull/2864
* fix(frontend): delete notifications by @Zewed in https://github.com/QuivrHQ/quivr/pull/2874
* feat(frontend): back button by @Zewed in https://github.com/QuivrHQ/quivr/pull/2876


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.283...v0.0.284

## 0.0.283 (2024-07-12)

## What's Changed
* feat: Add bulk_id field to CreateNotification and Notification models by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2850
* feat: Add bulk_id field to CreateNotification and Notification models by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2854
* fix: quiv core stream duplicate  and quivr-core rag tests by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2852
* feat: Add category and brain_id fields to CreateNotification and Notification models by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2856
* feat: Update file loading logic in File model by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2857


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.282...v0.0.283

## 0.0.282 (2024-07-11)

## What's Changed
* chore: Update quivr-core and chainlit versions in requirements.txt by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2839
* chore(config): migrate renovate config by @renovate in https://github.com/QuivrHQ/quivr/pull/2838
* fix: fixes duplicate response bug by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2843
* fix(frontend): remove possibilities to create brain if max amount by @Zewed in https://github.com/QuivrHQ/quivr/pull/2847
* fix(frontend): general before connections by @Zewed in https://github.com/QuivrHQ/quivr/pull/2848
* fix(backend): thumbs button were broken by @Zewed in https://github.com/QuivrHQ/quivr/pull/2849


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.281...v0.0.282

## 0.0.281 (2024-07-11)

## What's Changed
* feat: quivr core minimal chat by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2803
* chore: Add release-please-core workflow and configuration files by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2809
* chore(main): release core 0.0.2 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2812
* chore(main): release core 0.0.2 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2813
* chore(main): release core 0.0.2 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2814
* chore(main): release core 0.0.2 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2815
* fix(pyproject): fixed to quivr github by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2816
* chore(main): release core 0.0.3 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2817
* feat: quivr core minimal chat by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2818
* chore(main): release core 0.0.4 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2819
* feat: Add GitHub Actions workflow for running tests on backend/core by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2820
* feat: Add GitHub Actions workflow for running tests on backend/core by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2822
* feat(precommit): Update pre-commit hooks to latest versions by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2823
* feat: quivr core chat history by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2824
* chore(main): release core 0.0.5 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2821
* feat(frontend): UI / UX Notifications by @Zewed in https://github.com/QuivrHQ/quivr/pull/2826
* feat: quivr-core ask streaming by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2828
* chore(main): release core 0.0.6 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2829
* fix: llm model name by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2830
* chore(main): release core 0.0.7 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2831
* feat: Add Quivr chatbot example by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2827
* feat(renovate): updated configuration by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2835
* feat: Update aiofiles dependency to loosen version control by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2834
* chore(main): release core 0.0.8 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2832
* chore: Update quivr-core and chainlit versions in requirements.txt by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2836


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.280...v0.0.281

## 0.0.280 (2024-07-09)

## What's Changed
* feat(frontend): add small property to textInput by @Zewed in https://github.com/QuivrHQ/quivr/pull/2798
* fix(frontend): brain studio ui audit implem by @Zewed in https://github.com/QuivrHQ/quivr/pull/2800
* fix(frontend): remove quivr assistant for now by @Zewed in https://github.com/QuivrHQ/quivr/pull/2801
* feat(frontend): Uniformize brain icon by @Zewed in https://github.com/QuivrHQ/quivr/pull/2802
* fix(frontend): out of credits when credits null by @Zewed in https://github.com/QuivrHQ/quivr/pull/2804
* feat(frontend): better UI for big modals by @Zewed in https://github.com/QuivrHQ/quivr/pull/2805
* fix(frontend): align brain recap step by @Zewed in https://github.com/QuivrHQ/quivr/pull/2806
* feat: Improve error handling in acquiring token by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2807


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.279...v0.0.280

## 0.0.279 (2024-07-04)

## What's Changed
* feat(frontend): remove create brain step in onboarding when share brain by @Zewed in https://github.com/QuivrHQ/quivr/pull/2791
* feat: add megaparse by @chloedia in https://github.com/QuivrHQ/quivr/pull/2785
* fix: asyncpg pooling config fix by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2795
* fix: RAG service bug assertion error by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2796


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.278...v0.0.279

## 0.0.278 (2024-07-01)

## What's Changed
* chore: Add GitHub Actions workflow for testing and building Docker image by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2778
* chore: Update flashrank npm dependency to version 0.2.5 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2781
* feat(frontend): disabled searchBar if no remaining credits or no brain selected by @Zewed in https://github.com/QuivrHQ/quivr/pull/2788


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.277...v0.0.278

## 0.0.277 (2024-06-27)

## What's Changed
* fix(frontend): UI Notification Ring and Fix Page Header Display on Mobile by @Zewed in https://github.com/QuivrHQ/quivr/pull/2771
* feat(frontend): better UI for General Settings by @Zewed in https://github.com/QuivrHQ/quivr/pull/2773
* fix(frontend): new api key creation bug by @Zewed in https://github.com/QuivrHQ/quivr/pull/2774


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.276...v0.0.277

## 0.0.276 (2024-06-27)

## What's Changed
* chore: Add supabase directory to Dockerfile by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2768
* chore: Update docker-compose files to specify platform for backend services by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2763
* Revert "chore: Update docker-compose files to specify platform for backend services" by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2770


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.275...v0.0.276

## 0.0.275 (2024-06-27)

## What's Changed
* fix(frontend): fix table in frontend by @Zewed in https://github.com/QuivrHQ/quivr/pull/2758
* chore: Update docker-compose files to specify platform for backend services by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2762
* fix(frontend): settings button by @Zewed in https://github.com/QuivrHQ/quivr/pull/2764
* feat(backend):   quivr-monorepo and quivr-core package by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2765
* chore: Add ci-migration.sh to Dockerfile by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2767


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.274...v0.0.275

## 0.0.274 (2024-06-26)

## What's Changed
* refacto(backend): poetry package manager and chat route refactoring  by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2684
* closes #2756 by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2757
* fix: Update email sender parameters in backend code by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2755


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.273...v0.0.274

## 0.0.273 (2024-06-25)

## What's Changed
* feat(frontend): new ui ux for knowledge by @Zewed in https://github.com/QuivrHQ/quivr/pull/2732
* fix(frontend): small issues with scss by @Zewed in https://github.com/QuivrHQ/quivr/pull/2734


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.272...v0.0.273

## 0.0.272 (2024-06-24)

## What's Changed
* fix(frontend): send empty sync is not allowed by @Zewed in https://github.com/QuivrHQ/quivr/pull/2716
* feat: Improve efficiency of syncing stripe by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2719


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.271...v0.0.272

## 0.0.271 (2024-06-24)

## What's Changed
* fix: check user premium upsert by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2714


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.270...v0.0.271

## 0.0.270 (2024-06-24)

## What's Changed
* fix(frontend): small rephrase by @Zewed in https://github.com/QuivrHQ/quivr/pull/2699
* feat(frontend): table markdown by @Zewed in https://github.com/QuivrHQ/quivr/pull/2702
* Enable Porter Application raise by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2705
* Enable Porter Application raise-frontend by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2706
* chore: Remove Porter stack deployment workflows for cherry-pick-backend and cherry-pick-frontend by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2707
* fix(frontend): 25 instead of 100 by @Zewed in https://github.com/QuivrHQ/quivr/pull/2708
* fix(frontend): remove double scss class by @elazarnaaman in https://github.com/QuivrHQ/quivr/pull/2704
* fix(frontend): documents before connections by @Zewed in https://github.com/QuivrHQ/quivr/pull/2711
* feat(frontend): brain studio interface by @Zewed in https://github.com/QuivrHQ/quivr/pull/2712


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.269...v0.0.270

## 0.0.269 (2024-06-20)

## What's Changed
* feat: Add Microsoft Identity Association JSON file by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2697


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.268...v0.0.269

## 0.0.268 (2024-06-18)

## What's Changed

- fix(frontend): rephrase unpaid to free by @Zewed in https://github.com/QuivrHQ/quivr/pull/2679
- feat(frontend): set from connections by default in knowledge to feed by @Zewed in https://github.com/QuivrHQ/quivr/pull/2680
- feat(frontend): rephrase from Url to from Website's page by @Zewed in https://github.com/QuivrHQ/quivr/pull/2684
- feat(frontend): new chat interface by @Zewed in https://github.com/QuivrHQ/quivr/pull/2687
- fix(frontend): next step impossible if no knowledge when creating brain if no onboarded by @Zewed in https://github.com/QuivrHQ/quivr/pull/2688
- feat(turbopack): Implement turbo pack compiler by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2685
- fix(frontend): rephrase thoughts button title by @Zewed in https://github.com/QuivrHQ/quivr/pull/2689

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.267...v0.0.268

## 0.0.267 (2024-06-14)

## What's Changed

- fix(frontend): scroll modal payment by @Zewed in https://github.com/QuivrHQ/quivr/pull/2675

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.266...v0.0.267

## 0.0.266 (2024-06-13)

## What's Changed

- fix: Add logic to filter active subscriptions in check_if_is_premium_user function by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2673

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.265...v0.0.266

## 0.0.265 (2024-06-13)

## What's Changed

- feat: Add timezone conversion for premium user check by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2670

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.264...v0.0.265

## 0.0.264 (2024-06-13)

## What's Changed

- fix: name passed in sync authorize by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2665
- feat: Add premium user check in celery task by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2668

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.263...v0.0.264

## 0.0.263 (2024-06-12)

## What's Changed

- fix: Add error handling for syncing in tasks.py by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2663

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.262...v0.0.263

## 0.0.262 (2024-06-12)

## What's Changed

- Update README.md by @ferozemohideen in https://github.com/QuivrHQ/quivr/pull/2660
- feat: Normalize file names in sync module by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2661

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.261...v0.0.262

## 0.0.261 (2024-06-11)

## What's Changed

- feat: Update Google authorization URL with prompt for consent by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2658

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.260...v0.0.261

## 0.0.260 (2024-06-11)

## What's Changed

- feat: Add extra_hosts configuration to docker-compose.dev.yml by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2635
- fix: sync creation fixed by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2637
- chore: Set default value for "last_synced" column in "syncs_active" table to '2024-06-01 15:30:25+00' by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2638
- fix: integrations by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2642
- feat(frontend): sharepoint and gdrive integration by @Zewed in https://github.com/QuivrHQ/quivr/pull/2643
- fix(frontend): display bug on add knowledge by @Zewed in https://github.com/QuivrHQ/quivr/pull/2644
- fix: files_metadata by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2645
- fix(google): auth is now in state by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2647
- fix(frontend): add brain modal integration doestn t work by @Zewed in https://github.com/QuivrHQ/quivr/pull/2649
- fix(frontend): tooltip on folder line by @Zewed in https://github.com/QuivrHQ/quivr/pull/2650
- feat: telemetry improved by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2651
- feat: Add force_sync option to SyncsActiveUpdateInput by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2652
- Update license to include enterprise features by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2653
- fix(frontend): onboarding bug by @Zewed in https://github.com/QuivrHQ/quivr/pull/2655
- Update README.md by @ferozemohideen in https://github.com/QuivrHQ/quivr/pull/2656

## New Contributors

- @ferozemohideen made their first contribution in https://github.com/QuivrHQ/quivr/pull/2656

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.259...v0.0.260

## 0.0.259 (2024-06-04)

## What's Changed

- feat(upload): async improved by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/2544

## New Contributors

- @AmineDiro made their first contribution in https://github.com/QuivrHQ/quivr/pull/2544

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.258...v0.0.259

## 0.0.258 (2024-05-29)

## What's Changed

- feat: Update QuivrRAG and run_evaluation.py files by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2615
- fix: modify thought prompt by @chloedia in https://github.com/QuivrHQ/quivr/pull/2626
- feat(llamaparse): Update parsing instructions in common.py by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2627
- feat(sync): retrieve user email used for the connection by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2628
- fix: Refactor conversational_qa_chain initialization in KnowledgeBrainQA by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2629

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.257...v0.0.258

## 0.0.257 (2024-05-28)

## What's Changed

- Add Privacy & Compliance Documentation by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2620
- docs(security): added compliance by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2621
- fix(frontend): upgrade button on user page by @Zewed in https://github.com/QuivrHQ/quivr/pull/2623
- feat(frontend): Add ThoughtsButton component for displaying thoughts by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2624

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.256...v0.0.257

## 0.0.256 (2024-05-26)

## What's Changed

- feat(rag): follow-up questions and thoughts with spanish fix by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2618

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.255...v0.0.256

## 0.0.255 (2024-05-24)

## What's Changed

- feat: Add Google Drive & Sharepoint sync in backend by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2592
- Revert "feat: Add Google Drive & Sharepoint sync in backend" by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2603
- Feat/auth-playground by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2605
- feat: add init to create packages by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2606
- Add additional modules to celery.autodiscover_tasks() by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2607
- Feat/celery import by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2608
- feat: self-reflect brain by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2610
- feat: ragas improved testing by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2611
- fix(frontend): less agressive colors by @Zewed in https://github.com/QuivrHQ/quivr/pull/2612
- fix(frontend): important buttons by @Zewed in https://github.com/QuivrHQ/quivr/pull/2613
- fix(frontend): fix white colors by @Zewed in https://github.com/QuivrHQ/quivr/pull/2614
- fix(frontend): using dark mode in tiptap by @ramonzaca in https://github.com/QuivrHQ/quivr/pull/2616

## New Contributors

- @ramonzaca made their first contribution in https://github.com/QuivrHQ/quivr/pull/2616

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.254...v0.0.255

## 0.0.254 (2024-05-21)

## What's Changed

- fix: sender email address in resend_invitation_email.py by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2600

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.253...v0.0.254

## 0.0.253 (2024-05-14)

## What's Changed

- fix(frontend): Implement persistent dark mode setting and & Implement persistent dark mode setting by @elazarnaaman in https://github.com/QuivrHQ/quivr/pull/2423
- fix(frontend): hover effect on profile Button by @Zewed in https://github.com/QuivrHQ/quivr/pull/2587
- fix(frontend): user invite UI on Mobile by @Zewed in https://github.com/QuivrHQ/quivr/pull/2586
- feat: Update ChatLiteLLM model and add RLS optimization for notifications by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2591

## New Contributors

- @elazarnaaman made their first contribution in https://github.com/QuivrHQ/quivr/pull/2423

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.252...v0.0.253

## 0.0.252 (2024-05-13)

## What's Changed

- docs: Update GPT4 documentation with available tools and use cases by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2580
- docs: Add docstrings to integration brains by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2582
- fix: Update import statements for OllamaEmbeddings by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2584
- feat: Add support for gpt-4o model by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2589

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.251...v0.0.252

## 0.0.251 (2024-05-10)

## What's Changed

- feat(tool): Add URLReaderTool by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2577
- feat(email): Add email sender tool and update image generator tool by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2579

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.250...v0.0.251

## 0.0.250 (2024-05-10)

## What's Changed

- feat(gpt4): Add search functionality by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2566
- [ImgBot] Optimize images by @imgbot in https://github.com/QuivrHQ/quivr/pull/2568
- feat(gpt4): image generation by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2569
- fix(front): Add NEXT_PUBLIC_AUTH_MODES to .env.example by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2570
- fix: NEXT_PUBLIC_AUTH_MODES in docker-compose.yml by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2572
- docs: Add Supabase configuration documentation by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2574
- docs(gpt4): Update GPT-4 Documentation by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2573
- chore: tools by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2575
- feat(brave-search): Update GPT4Brain tools and add WebSearchTool by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2576

## New Contributors

- @imgbot made their first contribution in https://github.com/QuivrHQ/quivr/pull/2568

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.249...v0.0.250

## 0.0.249 (2024-05-08)

## What's Changed

- feat(crawler): Add Playwright for web crawling by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2562
- ci(ecr): added build to public ecr by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2564

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.248...v0.0.249

## 0.0.248 (2024-05-07)

## What's Changed

- fix: utf8 encoding by @chloedia in https://github.com/QuivrHQ/quivr/pull/2555
- feat(celery): moved assistant summary to celery by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2557
- Revert "feat(celery): moved assistant summary to celery" by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2558

## New Contributors

- @chloedia made their first contribution in https://github.com/QuivrHQ/quivr/pull/2555

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.247...v0.0.248

## 0.0.247 (2024-05-07)

## What's Changed

- feat(frontend): add notifications for document uploads by @Zewed in https://github.com/QuivrHQ/quivr/pull/2549
- Update install.mdx by @dazeb in https://github.com/QuivrHQ/quivr/pull/2552
- fix(frontend): fix notifications issues by @Zewed in https://github.com/QuivrHQ/quivr/pull/2551
- chore(ci): Update PR title linting workflow by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2553

## New Contributors

- @dazeb made their first contribution in https://github.com/QuivrHQ/quivr/pull/2552

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.246...v0.0.247

## 0.0.246 (2024-05-04)

## What's Changed

- Enable Porter Application theodo-backend by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2537
- Enable Porter Application theodo-frontend by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2538
- Add config parameter to conversational_qa_chain by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2540
- feat(notion): update doc by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2542

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.245...v0.0.246

## 0.0.245 (2024-05-03)

## What's Changed

- feat(user): Delete User Data from frontend by @Zewed in https://github.com/QuivrHQ/quivr/pull/2476
- feat(backend): Add a pre_pring on Connection polling to handle disconnection by @dmourot in https://github.com/QuivrHQ/quivr/pull/2534
- feat(llama-parse): improve prompt by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2535
- feat(brain): Add ProxyBrain integration by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2536

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.244...v0.0.245

## 0.0.244 (2024-05-02)

## What's Changed

- fix: Update parsing instruction in common.py by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2531

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.243...v0.0.244

## 0.0.243 (2024-05-01)

## What's Changed

- fix: Refactor chat_service.py and remove unused code by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2530

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.242...v0.0.243

## 0.0.242 (2024-05-01)

## What's Changed

- feat(notifications): implemented notifications with RLS and realtime by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2525
- chore: packages by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2527
- Enable Porter Application production by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2528

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.241...v0.0.242

## 0.0.241 (2024-05-01)

## What's Changed

- feat(llamaparse): Add Llama Parse integration for complex document parsing by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2517
- Delete Porter Application quivr-back by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2519
- Delete Porter Application quivr-demo-front by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2520
- Enable Porter Application preview by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2521
- Enable Porter Application preview-frontend by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2522
- feat(frontend): citations & sources by @Zewed in https://github.com/QuivrHQ/quivr/pull/2523
- Fix: citation handling in ChatItem component by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2524

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.240...v0.0.241

## 0.0.240 (2024-04-29)

## What's Changed

- feat(supabase): Add logging statements and refactor Supabase client creation by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2514
- feat(backend): use SQLAlchemy instead od supabase API by @dmourot in https://github.com/QuivrHQ/quivr/pull/2516

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.239...v0.0.240

## 0.0.239 (2024-04-28)

## What's Changed

- feat(citations): system added by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2498
- feat(frontend): add nb of knowledges per brain by @Zewed in https://github.com/QuivrHQ/quivr/pull/2502
- docs: Update links in mint.json to add api by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2504
- feat(docker): Update Dockerfile to install Supabase CLI by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2505
- fix(frontend): fix some next errors by @Zewed in https://github.com/QuivrHQ/quivr/pull/2503
- feat(frontend): show remaining credits by @Zewed in https://github.com/QuivrHQ/quivr/pull/2495
- feat(embedding): keeping citations by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2506
- fix(metadata): Removed citation from metadata by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2507
- Add ci-migration script by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2508
- Feat/migration ci 2 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2509
- Enable Porter Application quivr-com-backend by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2510
- Enable Porter Application quivr-com by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2511
- feat(profiler): Add pyinstrument package and update Makefile and backend code by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2512
- feat(db): Add Supabase client and database instances caching by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2513

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.238...v0.0.239

## 0.0.238 (2024-04-25)

## What's Changed

- Enable Porter Application cherry-pick-backend by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2492
- Enable Porter Application cherry-pick-frontend by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2493
- feat: Add telemetry ping task to celery worker and main.py by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2494
- fix(backend): compute history only if needed and put some cache to remove some call… by @dmourot in https://github.com/QuivrHQ/quivr/pull/2497

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.237...v0.0.238

## 0.0.237 (2024-04-24)

## What's Changed

- docs: Add environment variables, increase user usage, and add new models by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2481
- fix(frontend): Warning for Quivr Assistants by @Zewed in https://github.com/QuivrHQ/quivr/pull/2479
- fix(frontend): better UI for Onboarding by @Zewed in https://github.com/QuivrHQ/quivr/pull/2477
- docs: add new configuration items by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2483
- Revert "fix(frontend): better UI for Onboarding" by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2485
- feat(reranker): Add flashrank and contextual compression retriever by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2480
- feat(history): max tokens in the history provided by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2487
- feat: Update chunk overlap to 200 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2488
- docs: Add reranking configuration guide by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2489
- docs: Update telemetry configuration in Quivr by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2490

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.236...v0.0.237

## 0.0.236 (2024-04-23)

## What's Changed

- feat(docs): update to new by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2465
- feat(docs): Add new brain files and update navigation by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2467
- Feat/docs category brains agents by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2469
- fix(docs): update doc by @Zewed in https://github.com/QuivrHQ/quivr/pull/2470
- feat(digital-ocean): Update deployment instructions for Digital Ocean by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2472
- docs(digital-ocean): added missing photo by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2473
- docs: Update brain documentation and images by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2475

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.235...v0.0.236

## 0.0.235 (2024-04-21)

## What's Changed

- fix(sources): Remove duplicate sources and add metadata to model response by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2462

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.234...v0.0.235

## 0.0.234 (2024-04-21)

## What's Changed

- fix(gpt4): Refactor GPT4Brain and KnowledgeBrainQA classes to add non-streaming-saving-answer by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2460

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.233...v0.0.234

## 0.0.233 (2024-04-21)

## What's Changed

- refactor: reorg files in backend by @MaximeThoonsen in https://github.com/QuivrHQ/quivr/pull/2449
- Revert "refactor: reorg files in backend" by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2456
- refactor: Refacto code #1 by @MaximeThoonsen in https://github.com/QuivrHQ/quivr/pull/2458
- refactor: reorg the files #2 by @MaximeThoonsen in https://github.com/QuivrHQ/quivr/pull/2457
- feat(gpt4): Add chat service and generate answer method to GPT4Brain class by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2459

## New Contributors

- @MaximeThoonsen made their first contribution in https://github.com/QuivrHQ/quivr/pull/2449

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.232...v0.0.233

## 0.0.232 (2024-04-19)

## What's Changed

- Update CPU and memory settings in task definition files by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2450
- fix: Fix error message in SummaryAssistant class by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2453

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.231...v0.0.232

## 0.0.231 (2024-04-19)

## What's Changed

- feat(assistants): Add user usage update and pricing calculation to ITO assistant by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2433
- feat(assistant): improve prompt summary by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2435
- feat(assistants): Add PDF generation functionality and nice emails by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2436
- feat(analytics): rely on sql rather that python loop for brains by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2437
- fix(assistant): summary now can output 2000 tokens by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2440
- feat(assistant): check if key of file is same as filename uploaded by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2439
- feat: Update Docker build commands and dependencies by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2441
- feat(rag): Refactor DEFAULT_DOCUMENT_PROMPT in quivr_rag.py by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2442
- Enable Porter Application quivr-back by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2443
- Enable Porter Application quivr-demo-front by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2444
- fix(assistants): brain id is null by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2445
- feat(summary): improve prompt to get more insights by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2446
- feat(aws): Update CPU and memory configurations for task definitions by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2447
- feat(frontend): Quivr Assistants by @Zewed in https://github.com/QuivrHQ/quivr/pull/2448

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.230...v0.0.231

## 0.0.230 (2024-04-16)

## What's Changed

- feat(backend): add RAG evaluation using Ragas by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2429
- feat(assistants): Add new input models for boolean, number, select text, and select number by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2432

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.229...v0.0.230

## 0.0.229 (2024-04-12)

## What's Changed

- feat: optimization calls by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2417
- feat: Add assistant module and remove ingestion module by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2420
- feat: assistants by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2421
- feat: Add tags to AssistantOutput classes by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2425
- feat: Add icon and description to assistant by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2426
- feat: llamaparse & diff agent by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2427

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.228...v0.0.229

## 0.0.228 (2024-04-10)

## What's Changed

- fix(frontend): phone display issues by @Zewed in https://github.com/QuivrHQ/quivr/pull/2386
- Patch 1 by @llwp in https://github.com/QuivrHQ/quivr/pull/2388
- fix: typo in README.md by @bolens in https://github.com/QuivrHQ/quivr/pull/2391
- feat(ingestion): Add ingestion module and routes by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2393
- feat: Add seed ingestions to supabase migrations by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2399
- feat: Add url_required field to IngestionEntity by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2400
- Feat: Bibtex file uploads by @colesnic in https://github.com/QuivrHQ/quivr/pull/2398
- fix: logger level and telemetry function calls by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2409
- fix: Add integration brain to subscription route by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2410
- feat(frontend): onboarding V2 by @Zewed in https://github.com/QuivrHQ/quivr/pull/2394
- fix(frontend): onboardind bug by @Zewed in https://github.com/QuivrHQ/quivr/pull/2414
- fix(frontend): cleaner fix for onboarding by @Zewed in https://github.com/QuivrHQ/quivr/pull/2415
- feat(analytics): added analytics page by @Zewed in https://github.com/QuivrHQ/quivr/pull/2416

## New Contributors

- @llwp made their first contribution in https://github.com/QuivrHQ/quivr/pull/2388
- @bolens made their first contribution in https://github.com/QuivrHQ/quivr/pull/2391
- @colesnic made their first contribution in https://github.com/QuivrHQ/quivr/pull/2398

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.227...v0.0.228

## 0.0.227 (2024-03-28)

## What's Changed

- fix(backend): invitation with new brains did not work by @Zewed in https://github.com/QuivrHQ/quivr/pull/2378
- fix(backend): invitation brain bugs by @Zewed in https://github.com/QuivrHQ/quivr/pull/2380
- fix(frontend): disable knowledge tab by @Zewed in https://github.com/QuivrHQ/quivr/pull/2381
- fix(frontend): dark mode issues by @Zewed in https://github.com/QuivrHQ/quivr/pull/2382
- feat(frontend): show icons only on hover except for last message by @Zewed in https://github.com/QuivrHQ/quivr/pull/2377

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.226...v0.0.227

## 0.0.226 (2024-03-21)

## What's Changed

- feat: Add Mistral models to defineMaxTokens and BrainConfig by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2363
- feat: mistral by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2365
- fix(retriever): Update match_vectors sql function to rank chunks in correct order by @dmourot in https://github.com/QuivrHQ/quivr/pull/2367
- feat(docker image): Docker image Optimized for CPU-only env by @dmourot in https://github.com/QuivrHQ/quivr/pull/2368
- feat(frontend): dark mode by @Zewed in https://github.com/QuivrHQ/quivr/pull/2369
- feat(frontend & backend): thumbs for message feedback by @Zewed in https://github.com/QuivrHQ/quivr/pull/2360
- fix(backend): migration legacy by @Zewed in https://github.com/QuivrHQ/quivr/pull/2370
- fix(frontend): type stripe casing by @Zewed in https://github.com/QuivrHQ/quivr/pull/2371
- fix(backend): unsubscribe from brain by @Zewed in https://github.com/QuivrHQ/quivr/pull/2373
- feat(frontend): onboarding form by @Zewed in https://github.com/QuivrHQ/quivr/pull/2342
- fix(frontend): onBoarding issue by @Zewed in https://github.com/QuivrHQ/quivr/pull/2374

## New Contributors

- @dmourot made their first contribution in https://github.com/QuivrHQ/quivr/pull/2367

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.225...v0.0.226

## 0.0.225 (2024-03-15)

## What's Changed

- fix(frontend): bigger icon on message row by @Zewed in https://github.com/QuivrHQ/quivr/pull/2345
- fix(frontend): remove brains usage in user page by @Zewed in https://github.com/QuivrHQ/quivr/pull/2349

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.224...v0.0.225

## 0.0.224 (2024-03-15)

## What's Changed

- feat(frontend): add discord link by @Zewed in https://github.com/QuivrHQ/quivr/pull/2343
- fix(frontend): upgrade to plus by @Zewed in https://github.com/QuivrHQ/quivr/pull/2346

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.223...v0.0.224

## 0.0.223 (2024-03-13)

## What's Changed

- chore: update packages backend by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2339
- feat: Add optional fields to UserIdentity and UserUpdatableProperties by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2341

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.222...v0.0.223

## 0.0.222 (2024-03-09)

## What's Changed

- feat: Update langchain.prompts and langchain_core.messages modules by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2326
- feat(frontend): social buttons by @Zewed in https://github.com/QuivrHQ/quivr/pull/2325
- fix(frontend): upgrade to plus button by @Zewed in https://github.com/QuivrHQ/quivr/pull/2324
- fix(frontend): maximum amount of brains reached by @Zewed in https://github.com/QuivrHQ/quivr/pull/2323

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.221...v0.0.222

## 0.0.221 (2024-03-07)

## What's Changed

- feat: seed updated by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2313
- fix(frontend): allow model change by @Zewed in https://github.com/QuivrHQ/quivr/pull/2317
- fix(frontend): mention list by @Zewed in https://github.com/QuivrHQ/quivr/pull/2315
- fix(frontend): studio to brain studio by @Zewed in https://github.com/QuivrHQ/quivr/pull/2316
- feat(frontend): add help tooltip for model selection by @Zewed in https://github.com/QuivrHQ/quivr/pull/2318
- fix(frontend): page header studio to brain studio by @Zewed in https://github.com/QuivrHQ/quivr/pull/2319

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.220...v0.0.221

## 0.0.220 (2024-03-06)

## What's Changed

- fix(frontend): brain name by @Zewed in https://github.com/QuivrHQ/quivr/pull/2311

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.219...v0.0.220

## 0.0.219 (2024-03-06)

## What's Changed

- feat: Update to newest version of litellm by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2307
- fix(frontend): small renaiming chat to thread by @Zewed in https://github.com/QuivrHQ/quivr/pull/2306
- feat(frontend): brain Catalogue by @Zewed in https://github.com/QuivrHQ/quivr/pull/2303
- feat(frontend): 404 redirection by @Zewed in https://github.com/QuivrHQ/quivr/pull/2309
- fix(frontend): old brain legacy by @Zewed in https://github.com/QuivrHQ/quivr/pull/2310

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.218...v0.0.219

## 0.0.218 (2024-03-05)

## What's Changed

- feat: doc as integration by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2297
- fix(rag): add api_base by @niels-garve in https://github.com/QuivrHQ/quivr/pull/2289
- fix(frontend): login bug by @Zewed in https://github.com/QuivrHQ/quivr/pull/2300

## New Contributors

- @niels-garve made their first contribution in https://github.com/QuivrHQ/quivr/pull/2289

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.217...v0.0.218

## 0.0.217 (2024-03-04)

## What's Changed

- fix(frontend): fix home page redirection by @Zewed in https://github.com/QuivrHQ/quivr/pull/2295

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.216...v0.0.217

## 0.0.216 (2024-03-04)

## What's Changed

- feat: Update chunk_size in File model by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2281
- fix(frontend): double file upload on drag and drop by @Zewed in https://github.com/QuivrHQ/quivr/pull/2284
- fix(frontend): click anywhere on drop zone to upload file by @Zewed in https://github.com/QuivrHQ/quivr/pull/2285
- fix(frontend): smalls on thread section by @Zewed in https://github.com/QuivrHQ/quivr/pull/2286
- fix(frontend): remove tests by @Zewed in https://github.com/QuivrHQ/quivr/pull/2287
- feat(frontend): better UI/UX on select brain by @Zewed in https://github.com/QuivrHQ/quivr/pull/2288
- feat(frontend): add brain icon on brain list by @Zewed in https://github.com/QuivrHQ/quivr/pull/2292
- fix(frontend): whitespace on firefox by @Zewed in https://github.com/QuivrHQ/quivr/pull/2293
- fix(frontend): remove unused stuff by @Zewed in https://github.com/QuivrHQ/quivr/pull/2282

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.215...v0.0.216

## 0.0.215 (2024-03-01)

## What's Changed

- fix(frontend): message info box by @Zewed in https://github.com/QuivrHQ/quivr/pull/2277
- fix(frontend): see knowledge in custom brains by @Zewed in https://github.com/QuivrHQ/quivr/pull/2278
- fix(frontend): fix disabled knwoledge tab by @Zewed in https://github.com/QuivrHQ/quivr/pull/2280

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.214...v0.0.215

## 0.0.214 (2024-02-29)

## What's Changed

- fix(frontend): revamp quivr studio by @Zewed in https://github.com/QuivrHQ/quivr/pull/2274
- fix(frontend): zindex and radius on single selector component by @Zewed in https://github.com/QuivrHQ/quivr/pull/2276

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.213...v0.0.214

## 0.0.213 (2024-02-28)

## What's Changed

- feat(notion): added custom integration by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2268
- feat: Remove constraints and add foreign key references to brain tables by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2273

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.212...v0.0.213

## 0.0.212 (2024-02-26)

## What's Changed

- feat: new landing page by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2264

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.211...v0.0.212

## 0.0.211 (2024-02-24)

## What's Changed

- fix: ollama migration documentation by @bidoubiwa in https://github.com/QuivrHQ/quivr/pull/2248
- Update Sentry configuration and ignore file by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2250
- Fix Sentry DSN environment variable by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2251
- fix(sentry): Refactor GlobalError component to use arrow function syntax by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2252
- fix: Update Sentry configuration to use NEXT_PUBLIC_SENTRY_DSN by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2254
- feat(frontend): integrate octolane by @Zewed in https://github.com/QuivrHQ/quivr/pull/2256
- fix(frontend): better search bar and chat box by @Zewed in https://github.com/QuivrHQ/quivr/pull/2255
- feat(frontend): sources per messages by @Zewed in https://github.com/QuivrHQ/quivr/pull/2253
- feat(sentry): remove health endpoint by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2257
- Add octolane.com to Content Security Policy by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2258
- fix(frontend): ui chat box & sources small bug by @Zewed in https://github.com/QuivrHQ/quivr/pull/2260
- Refactor GitHub workflows by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2261

## New Contributors

- @bidoubiwa made their first contribution in https://github.com/QuivrHQ/quivr/pull/2248

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.210...v0.0.211

## 0.0.210 (2024-02-22)

## What's Changed

- feat: Update memory allocation in task definition by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2243
- fix: get_brain_details API to include user_id parameter by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2242
- feat(chat): Add follow up questions functionality by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2241
- Reduce sampling rate for Sentry traces by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2245
- Revert "feat(chat): Add follow up questions functionality" by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2246
- Add max_input and max_tokens parameters to KnowledgeBrainQA constructor by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2247

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.209...v0.0.210

## 0.0.209 (2024-02-22)

## What's Changed

- fix(frontend): fix share brain by @Zewed in https://github.com/QuivrHQ/quivr/pull/2238
- fix(frontend): don't preselect core brain by @Zewed in https://github.com/QuivrHQ/quivr/pull/2239

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.208...v0.0.209

## 0.0.208 (2024-02-21)

## What's Changed

- feat: Add pricing calculation method to GPT4Brain class and update user usage in chat controller by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2216
- Enable Porter Application quivr by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2220
- Delete Porter Application quivr by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2221
- Enable Porter Application preview-quivr by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2222
- Enable Porter Application prod-quivr by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/2223
- feat(brains): added description by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2224
- feat: Add integration_logo_url to MinimalUserBrainEntity by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2225
- Add Redis configuration to celery_config.py by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2227
- Remove unused 'model' variable and logging statements by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2228
- feat: Add max_files attribute to MinimalUserBrainEntity and BrainsUsers repository by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2229
- Feature: Add animations to foldable section by @johnfewell in https://github.com/QuivrHQ/quivr/pull/2202
- feat(frontend): first custom brain live by @Zewed in https://github.com/QuivrHQ/quivr/pull/2226
- fix(frontend): legacy on foldable section animation pr by @Zewed in https://github.com/QuivrHQ/quivr/pull/2230
- Fix: API endpoint for getting integration brains by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2231
- feat: Update dependencies and remove unnecessary logging statements by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2232
- feat: implement elasticache by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2234
- fix(frontend): ellipsis overflow on large brain or prompt names by @Zewed in https://github.com/QuivrHQ/quivr/pull/2233

## New Contributors

- @porter-deployment-app made their first contribution in https://github.com/QuivrHQ/quivr/pull/2220
- @johnfewell made their first contribution in https://github.com/QuivrHQ/quivr/pull/2202

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.207...v0.0.208

## 0.0.206 (2024-02-19)

## What's Changed

- feat: Add pricing calculation method to GPT4Brain class and update user usage in chat controller by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2210
- fix(frontend): click on inputs by @Zewed in https://github.com/QuivrHQ/quivr/pull/2212

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.205...v0.0.206

## 0.0.205 (2024-02-19)

## What's Changed

- Update ollama.mdx by @zangjiucheng in https://github.com/QuivrHQ/quivr/pull/2196
- feat(integration): improve by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2199
- fix(frontend): history to threads by @Zewed in https://github.com/QuivrHQ/quivr/pull/2201
- feat(custom): big brain by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2198
- feat: Update system templates with custom personality support by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2209

## New Contributors

- @zangjiucheng made their first contribution in https://github.com/QuivrHQ/quivr/pull/2196

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.204...v0.0.205

## 0.0.203 (2024-02-15)

## What's Changed

- feat: 🎸 ocr by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2187
- feat(lcel): migrated to lcel and pydantic by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2185
- feat(frontend): new brain creation modal by @Zewed in https://github.com/QuivrHQ/quivr/pull/2192
- feat(integration): implementation by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2191
- feat(frontend): new design for brain table by @Zewed in https://github.com/QuivrHQ/quivr/pull/2193

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.202...v0.0.203

## 0.0.202 (2024-02-11)

## What's Changed

- fix(frontend): change placeholder in chat bar by @Zewed in https://github.com/QuivrHQ/quivr/pull/2177
- fix(frontend): remove notification banner by @Zewed in https://github.com/QuivrHQ/quivr/pull/2178
- fix(frontend): remove onboarding questions by @Zewed in https://github.com/QuivrHQ/quivr/pull/2176
- feat(frontend): new modal for add knowledge by @Zewed in https://github.com/QuivrHQ/quivr/pull/2173
- Revert "fix(frontend): remove onboarding questions" by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2181
- fix(frontend): remove onboarding question by @Zewed in https://github.com/QuivrHQ/quivr/pull/2183

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.201...v0.0.202

## 0.0.201 (2024-02-10)

## What's Changed

- fix: 🐛 session by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2174

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.200...v0.0.201

## 0.0.200 (2024-02-09)

## What's Changed

- fix(daily-usage): Update daily requests count in UserUsage model by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2171

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.199...v0.0.200

## 0.0.199 (2024-02-08)

## What's Changed

- feat: 🎸 telemetry by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2169

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.198...v0.0.199

## 0.0.197 (2024-02-07)

## What's Changed

- fix(prompts): can now be removed by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2154
- tests: Add tests for deleting prompts by ID by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2156
- fix(related): removed public brains by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2157
- perf: ⚡️ signed_url by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2159
- fix(backend): typo in word response by @untilhamza in https://github.com/QuivrHQ/quivr/pull/2158
- fix(frontend): better UI for phone device by @Zewed in https://github.com/QuivrHQ/quivr/pull/2160
- fix(frontend): add knwoledge from create brain by @Zewed in https://github.com/QuivrHQ/quivr/pull/2161
- feat(chunks): now chunk size is saved in database dynamically and not just 500 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2164
- fix(frontend): remove related brains for now by @Zewed in https://github.com/QuivrHQ/quivr/pull/2162
- fix(frontend): can"t choose private or public brains by @Zewed in https://github.com/QuivrHQ/quivr/pull/2163
- feat(frontend): manage current brain by @Zewed in https://github.com/QuivrHQ/quivr/pull/2165
- fix(frontend): upgrade my plan by @Zewed in https://github.com/QuivrHQ/quivr/pull/2167

## New Contributors

- @untilhamza made their first contribution in https://github.com/QuivrHQ/quivr/pull/2158

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.196...v0.0.197

## 0.0.196 (2024-02-07)

## What's Changed

- feat(frontend): Page Header + Begin of Studio by @Zewed in https://github.com/StanGirard/quivr/pull/2151
- fix(frontend): overflow brain item by @Zewed in https://github.com/StanGirard/quivr/pull/2153

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.195...v0.0.196

## 0.0.195 (2024-02-06)

## What's Changed

- feat(integrations): integration with Notion in the backend by @StanGirard in https://github.com/StanGirard/quivr/pull/2123

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.194...v0.0.195

## 0.0.194 (2024-02-05)

## What's Changed

- feat(frontend): add a chatbot for users by @Zewed in https://github.com/StanGirard/quivr/pull/2144

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.193...v0.0.194

## 0.0.193 (2024-02-04)

## What's Changed

- feat(frontend): design changes on user profile by @Zewed in https://github.com/StanGirard/quivr/pull/2140
- fix(frontend): rename upgrade to plus to upgrade by @Zewed in https://github.com/StanGirard/quivr/pull/2141

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.192...v0.0.193

## 0.0.192 (2024-02-02)

## What's Changed

- feat(frontend): display which brain you are talking to by @Zewed in https://github.com/StanGirard/quivr/pull/2137

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.191...v0.0.192

## 0.0.191 (2024-02-01)

## What's Changed

- fix(frontend): no sources repetition in data panel by @Zewed in https://github.com/StanGirard/quivr/pull/2132
- fix(frontend): don't show copy icon when thinking by @Zewed in https://github.com/StanGirard/quivr/pull/2133

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.190...v0.0.191

## 0.0.190 (2024-01-31)

## What's Changed

- fix(frontend): Better contrast in Menu by @Zewed in https://github.com/StanGirard/quivr/pull/2119
- fix(frontend): better chat color and copy icon position by @Zewed in https://github.com/StanGirard/quivr/pull/2121
- fix(frontend): better visualisation of current path on menu by @Zewed in https://github.com/StanGirard/quivr/pull/2122
- feat(frontend): uniformize behaviour for metadata panel by @Zewed in https://github.com/StanGirard/quivr/pull/2124
- fix(frontend): fetch chat only if session exist by @Zewed in https://github.com/StanGirard/quivr/pull/2130
- fix(frontend): prompt display by @Zewed in https://github.com/StanGirard/quivr/pull/2129
- fix(frontend): upload knwoledge in brains manegement by @Zewed in https://github.com/StanGirard/quivr/pull/2131

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.189...v0.0.190

## 0.0.189 (2024-01-30)

## What's Changed

- feat(frontend): design menu by @Zewed in https://github.com/StanGirard/quivr/pull/2116
- fix(frontend): fix z index popover on add knwoledge modal by @Zewed in https://github.com/StanGirard/quivr/pull/2118

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.188...v0.0.189

## 0.0.188 (2024-01-29)

## What's Changed

- fix: 🐛 upload by @StanGirard in https://github.com/StanGirard/quivr/pull/2112
- feat(frontend): add sources to metadata by @Zewed in https://github.com/StanGirard/quivr/pull/2113

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.187...v0.0.188

## 0.0.187 (2024-01-28)

## What's Changed

- feat: 🎸 user-limits by @StanGirard in https://github.com/StanGirard/quivr/pull/2104
- fix: 🐛 brains by @StanGirard in https://github.com/StanGirard/quivr/pull/2107
- feat(frontend): chat page ui/ux design by @Zewed in https://github.com/StanGirard/quivr/pull/2106
- Fix typo of UI: Ressources ==> Resources by @iharel in https://github.com/StanGirard/quivr/pull/2109
- fix(frontend): fix li markdown on chat by @Zewed in https://github.com/StanGirard/quivr/pull/2110

## New Contributors

- @iharel made their first contribution in https://github.com/StanGirard/quivr/pull/2109

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.186...v0.0.187

## 0.0.186 (2024-01-27)

## What's Changed

- fix(frontend): click on mention list on search bar in modal bug by @Zewed in https://github.com/StanGirard/quivr/pull/2098
- fix(frontend): remove dark theme by @Zewed in https://github.com/StanGirard/quivr/pull/2100
- fix(frontend): delete brain by @Zewed in https://github.com/StanGirard/quivr/pull/2101
- feat(14k): done by @StanGirard in https://github.com/StanGirard/quivr/pull/2102

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.185...v0.0.186

## 0.0.185 (2024-01-27)

## What's Changed

- fix: 🐛 brain by @StanGirard in https://github.com/StanGirard/quivr/pull/2096
- feat(frontend): search modal - remove parameters and explore buttons by @Zewed in https://github.com/StanGirard/quivr/pull/2094
- fix: 🐛 tests by @StanGirard in https://github.com/StanGirard/quivr/pull/2095

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.184...v0.0.185

## 0.0.184 (2024-01-26)

## What's Changed

- feat(panel): added by @Zewed in https://github.com/StanGirard/quivr/pull/2088
- feat: 🎸 api by @StanGirard in https://github.com/StanGirard/quivr/pull/2078
- fix(frontend): clear message input on submit by @Zewed in https://github.com/StanGirard/quivr/pull/2087
- fix: 🐛 related by @StanGirard in https://github.com/StanGirard/quivr/pull/2090
- feat: Added translation status badge from inlang by @NilsJacobsen in https://github.com/StanGirard/quivr/pull/2080
- fix(streaming): Data Truncation Issue in useHandleStream Function by @openperf in https://github.com/StanGirard/quivr/pull/2079
- feat: 🎸 sources by @StanGirard in https://github.com/StanGirard/quivr/pull/2092
- fix(frontend): clean related Brains useEffect by @Zewed in https://github.com/StanGirard/quivr/pull/2091

## New Contributors

- @openperf made their first contribution in https://github.com/StanGirard/quivr/pull/2079

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.183...v0.0.184

## 0.0.183 (2024-01-24)

## What's Changed

- fix: 🐛 subscription by @StanGirard in https://github.com/StanGirard/quivr/pull/2081

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.182...v0.0.183

## 0.0.182 (2024-01-24)

## What's Changed

- fix: 🐛 crawl by @StanGirard in https://github.com/StanGirard/quivr/pull/2076

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.181...v0.0.182

## 0.0.181 (2024-01-23)

## What's Changed

- fix(frontend): unable multiple enter on search page by @Zewed in https://github.com/StanGirard/quivr/pull/2074
- fix(frontend): force brain on search was broken by @Zewed in https://github.com/StanGirard/quivr/pull/2075

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.180...v0.0.181

## 0.0.180 (2024-01-23)

## What's Changed

- fix: 🐛 api by @StanGirard in https://github.com/StanGirard/quivr/pull/2068
- feat(frontend): Add Brain On Search Page by @Zewed in https://github.com/StanGirard/quivr/pull/2067
- fix(frontend): uniformize case for types by @Zewed in https://github.com/StanGirard/quivr/pull/2071
- fix: 🐛 gitconfig by @StanGirard in https://github.com/StanGirard/quivr/pull/2072

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.179...v0.0.180

## 0.0.179 (2024-01-22)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.178...v0.0.179

## 0.0.178 (2024-01-22)

## What's Changed

- fix(frontend): use mention brain on search bar by @Zewed in https://github.com/StanGirard/quivr/pull/2060
- feat: 🎸 cpu by @StanGirard in https://github.com/StanGirard/quivr/pull/2065

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.177...v0.0.178

## 0.0.177 (2024-01-22)

## What's Changed

- fix: 🐛 usage by @StanGirard in https://github.com/StanGirard/quivr/pull/2062

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.176...v0.0.177

## 0.0.176 (2024-01-22)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.175...v0.0.176

## 0.0.175 (2024-01-22)

## What's Changed

- fix: 🐛 limits by @StanGirard in https://github.com/StanGirard/quivr/pull/2058

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.174...v0.0.175

## 0.0.174 (2024-01-22)

## What's Changed

- fix(frontend): remove actions modal by @Zewed in https://github.com/StanGirard/quivr/pull/2054
- feat: 🎸 usage by @StanGirard in https://github.com/StanGirard/quivr/pull/2057

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.173...v0.0.174

## 0.0.173 (2024-01-22)

## What's Changed

- fix(api-brains): fixed with new types of brains by @StanGirard in https://github.com/StanGirard/quivr/pull/2052
- fix(frontend): font size on chat feed by @Zewed in https://github.com/StanGirard/quivr/pull/2051

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.172...v0.0.173

## 0.0.172 (2024-01-22)

## What's Changed

- feat(frontend): handle mentions in search bar by @Zewed in https://github.com/StanGirard/quivr/pull/2049

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.171...v0.0.172

## 0.0.171 (2024-01-22)

## What's Changed

- fix(frontend): don't set default brain as current brain and remove change brain button by @Zewed in https://github.com/StanGirard/quivr/pull/2047
- feat: 🎸 brains by @StanGirard in https://github.com/StanGirard/quivr/pull/2048

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.170...v0.0.171

## 0.0.170 (2024-01-21)

## What's Changed

- fix(frontend): translate configure for brains and successfully deleted for chat by @Zewed in https://github.com/StanGirard/quivr/pull/2042
- fix(frontend): change search icon on menu by @Zewed in https://github.com/StanGirard/quivr/pull/2043
- fix: 🐛 search by @StanGirard in https://github.com/StanGirard/quivr/pull/2045
- fix(frontend): remove brain choice when search page displays by @Zewed in https://github.com/StanGirard/quivr/pull/2044

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.169...v0.0.170

## 0.0.169 (2024-01-21)

## What's Changed

- feat(brains): added now multiple brains close by by @StanGirard in https://github.com/StanGirard/quivr/pull/2039
- fix(frontend): set chat messages only if needed by @Zewed in https://github.com/StanGirard/quivr/pull/2040

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.168...v0.0.169

## 0.0.168 (2024-01-20)

## What's Changed

- fix(frontend): don t load chat items on search by @Zewed in https://github.com/StanGirard/quivr/pull/2036

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.167...v0.0.168

## 0.0.167 (2024-01-20)

## What's Changed

- fix(frontend): chat still refreshs on first request by @Zewed in https://github.com/StanGirard/quivr/pull/2034

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.166...v0.0.167

## 0.0.166 (2024-01-20)

## What's Changed

- feat(search): new way to interact with Quivr by @StanGirard in https://github.com/StanGirard/quivr/pull/2026
- feat: adding search by @StanGirard in https://github.com/StanGirard/quivr/pull/2031
- fix(frontend): remove close menu icon on mobile by @Zewed in https://github.com/StanGirard/quivr/pull/2030
- fix(frontend): chat refreshed on first search request by @Zewed in https://github.com/StanGirard/quivr/pull/2033

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.165...v0.0.166

## 0.0.165 (2024-01-17)

## What's Changed

- fix(frontend): wrong placeholder message date by @Zewed in https://github.com/StanGirard/quivr/pull/2023

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.164...v0.0.165

## 0.0.164 (2024-01-14)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.163...v0.0.164

## 0.0.163 (2024-01-14)

## What's Changed

- fix(frontend): left panel is not closing by @Zewed in https://github.com/StanGirard/quivr/pull/2014
- fix: csp by @StanGirard in https://github.com/StanGirard/quivr/pull/2016

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.162...v0.0.163

## 0.0.162 (2024-01-13)

## What's Changed

- fix(frontend): remove right panel and reduce chat section width by @Zewed in https://github.com/StanGirard/quivr/pull/2012

## New Contributors

- @Zewed made their first contribution in https://github.com/StanGirard/quivr/pull/2012

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.161...v0.0.162

## 0.0.161 (2024-01-07)

## What's Changed

- feat: 🎸 policies by @StanGirard in https://github.com/StanGirard/quivr/pull/1997

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.160...v0.0.161

## 0.0.160 (2024-01-04)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.159...v0.0.160

## 0.0.159 (2024-01-04)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.158...v0.0.159

## 0.0.158 (2024-01-04)

## What's Changed

- chore(deps): pin dependencies by @renovate in https://github.com/StanGirard/quivr/pull/1975

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.157...v0.0.158

## 0.0.157 (2024-01-04)

## What's Changed

- feat: 🎸 posthog by @StanGirard in https://github.com/StanGirard/quivr/pull/1978

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.156...v0.0.157

## 0.0.156 (2024-01-04)

## What's Changed

- fix: 🐛 models by @StanGirard in https://github.com/StanGirard/quivr/pull/1973

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.155...v0.0.156

## 0.0.155 (2024-01-04)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.154...v0.0.155

## 0.0.154 (2024-01-04)

## What's Changed

- feat: 🎸 models by @StanGirard in https://github.com/StanGirard/quivr/pull/1967

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.153...v0.0.154

## 0.0.153 (2024-01-03)

## What's Changed

- chore(deps): Pin Node.js by @renovate in https://github.com/StanGirard/quivr/pull/1952
- chore(deps): Pin dependencies by @renovate in https://github.com/StanGirard/quivr/pull/1953
- chore(deps): Update actions/checkout action to v4 by @renovate in https://github.com/StanGirard/quivr/pull/1957
- chore(deps): Update actions/setup-node action to v4 by @renovate in https://github.com/StanGirard/quivr/pull/1958
- feat: 🎸 usage by @StanGirard in https://github.com/StanGirard/quivr/pull/1966

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.152...v0.0.153

## 0.0.152 (2024-01-02)

## What's Changed

- feat: 🎸 posthog by @StanGirard in https://github.com/StanGirard/quivr/pull/1945

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.151...v0.0.152

## 0.0.151 (2023-12-29)

## What's Changed

- feat: 🎸 posthog by @StanGirard in https://github.com/StanGirard/quivr/pull/1938

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.150...v0.0.151

## 0.0.150 (2023-12-29)

## What's Changed

- feat: 🎸 posthog by @StanGirard in https://github.com/StanGirard/quivr/pull/1936

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.149...v0.0.150

## 0.0.149 (2023-12-29)

## What's Changed

- feat: 🎸 pricing by @StanGirard in https://github.com/StanGirard/quivr/pull/1935

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.148...v0.0.149

## 0.0.148 (2023-12-28)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.147...v0.0.148

## 0.0.147 (2023-12-28)

## What's Changed

- feat: 🎸 posthog by @StanGirard in https://github.com/StanGirard/quivr/pull/1931

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.146...v0.0.147

## 0.0.146 (2023-12-28)

## What's Changed

- feat: 🎸 posthog by @StanGirard in https://github.com/StanGirard/quivr/pull/1929

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.145...v0.0.146

## 0.0.145 (2023-12-28)

## What's Changed

- feat: 🎸 posthog by @StanGirard in https://github.com/StanGirard/quivr/pull/1927

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.144...v0.0.145

## 0.0.144 (2023-12-27)

## What's Changed

- feat: 🎸 pricing by @StanGirard in https://github.com/StanGirard/quivr/pull/1923
- feat(pricing): added testimonials and else by @StanGirard in https://github.com/StanGirard/quivr/pull/1925

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.143...v0.0.144

## 0.0.143 (2023-12-27)

## What's Changed

- docs: ✏️ mintlify by @StanGirard in https://github.com/StanGirard/quivr/pull/1917
- feat(docs): added homepage by @StanGirard in https://github.com/StanGirard/quivr/pull/1919
- docs: ✏️ homepage by @StanGirard in https://github.com/StanGirard/quivr/pull/1922

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.142...v0.0.143

## 0.0.142 (2023-12-18)

## What's Changed

- feat: add new brain management page by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1906
- feat: update brain details page by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1910

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.141...v0.0.142

## 0.0.141 (2023-12-15)

## What's Changed

- feat[i18n]: Added i18n documenation to the contribution guidelines by @NilsJacobsen in https://github.com/StanGirard/quivr/pull/1899
- feat: Update Explore button label by @StanGirard in https://github.com/StanGirard/quivr/pull/1901
- feat: chat with compositeBrain ( with/out streaming) by @gozineb in https://github.com/StanGirard/quivr/pull/1883
- feat: update brains library by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1903

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.140...v0.0.141

## 0.0.140 (2023-12-14)

## What's Changed

- feat: Update pytest command in Makefile and add new test by @StanGirard in https://github.com/StanGirard/quivr/pull/1893
- chore: add IDE extension for i18n handling by @NilsJacobsen in https://github.com/StanGirard/quivr/pull/1896
- feat: add chat view new design by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1897

## New Contributors

- @NilsJacobsen made their first contribution in https://github.com/StanGirard/quivr/pull/1896

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.139...v0.0.140

## 0.0.139 (2023-12-14)

## What's Changed

- feat: allow user to feed brain from Actions bar by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1882
- feat: add Menu bar by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1885
- feat: Remove unused method and update file processing by @StanGirard in https://github.com/StanGirard/quivr/pull/1890
- fix: update chat history fetching logic by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1891
- feat: add default feed button label by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1892

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.138...v0.0.139

## 0.0.138 (2023-12-13)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.137...v0.0.138

## 0.0.137 (2023-12-13)

## What's Changed

- feat: add chat history to Actions modal by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1877
- feat: allow user to control left panel from Chat input by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1880

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.136...v0.0.137

## 0.0.136 (2023-12-13)

## What's Changed

- feat: Add @tailwindcss/forms plugin and update by @StanGirard in https://github.com/StanGirard/quivr/pull/1869
- feat: Refactor get_question_context_for_brain endpoint by @StanGirard in https://github.com/StanGirard/quivr/pull/1872
- feat: Add file URL to DocumentAnswer objects by @StanGirard in https://github.com/StanGirard/quivr/pull/1874
- Update .gitignore and add .gitmodules by @StanGirard in https://github.com/StanGirard/quivr/pull/1875
- feat: add new actions modal by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1870
- feat: add selected brain tag and new discussion button to actions modal by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1873
- feat: add action modal change brain button by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1876

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.135...v0.0.136

## 0.0.135 (2023-12-11)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.134...v0.0.135

## 0.0.134 (2023-12-11)

## What's Changed

- feat: add custom rag first abstraction layer by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1858
- feat(payment): added modal of right size by @StanGirard in https://github.com/StanGirard/quivr/pull/1860

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.133...v0.0.134

## 0.0.133 (2023-12-11)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.132...v0.0.133

## 0.0.132 (2023-12-10)

## What's Changed

- feat: add generate_answer function to support non streamed response for api brain by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1847
- fix(ollama): - update supabase-db postgres docker image version by @KonstantinosAng in https://github.com/StanGirard/quivr/pull/1853

## New Contributors

- @KonstantinosAng made their first contribution in https://github.com/StanGirard/quivr/pull/1853

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.131...v0.0.132

## 0.0.131 (2023-12-06)

## What's Changed

- feat: update onboarding questions answer by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1834
- feat: composite brains get by @gozineb in https://github.com/StanGirard/quivr/pull/1837
- feat: add Agent creation frontend by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1836
- feat: keep sidebar opened on non mobile devices by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1840
- feat: add brains list overflow indicator by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1842

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.130...v0.0.131

## 0.0.130 (2023-12-06)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.129...v0.0.130

## 0.0.129 (2023-12-06)

## What's Changed

- feat(requirements): update aws version by @StanGirard in https://github.com/StanGirard/quivr/pull/1819
- feat: add brain creation step 2 by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1823
- feat: composite brains db by @gozineb in https://github.com/StanGirard/quivr/pull/1826
- feat: finalise steps based brain creation by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1825

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.128...v0.0.129

## 0.0.128 (2023-12-05)

## What's Changed

- feat: track response source usage by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1810
- doc: add VirtioFS instruction for MacOS users by @tarek-ayed in https://github.com/StanGirard/quivr/pull/1813
- refactor: chat for multibrains by @gozineb in https://github.com/StanGirard/quivr/pull/1812
- feat(prebuilt): prebuild backend image for faster compilation by @StanGirard in https://github.com/StanGirard/quivr/pull/1815
- fix: text not clear in dark mode by @Jezla in https://github.com/StanGirard/quivr/pull/1804
- fix: celery config typo by @yonmey in https://github.com/StanGirard/quivr/pull/1776
- feat: add brain creation steps system by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1814

## New Contributors

- @tarek-ayed made their first contribution in https://github.com/StanGirard/quivr/pull/1813
- @Jezla made their first contribution in https://github.com/StanGirard/quivr/pull/1804
- @yonmey made their first contribution in https://github.com/StanGirard/quivr/pull/1776

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.127...v0.0.128

## 0.0.127 (2023-12-04)

## What's Changed

- feat(api-keys): added customization by @StanGirard in https://github.com/StanGirard/quivr/pull/1802
- feat(embedding): now 100 times faster ⚡️🔥 by @StanGirard in https://github.com/StanGirard/quivr/pull/1807
- fix: update editor state update logic by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1809

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.126...v0.0.127

## 0.0.126 (2023-12-03)

## What's Changed

- feat: add optimistic update on new message by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1764
- feat: update models logic by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1767
- refactor: to modules by @gozineb in https://github.com/StanGirard/quivr/pull/1754
- feat(supabase): local installation made easy by @StanGirard in https://github.com/StanGirard/quivr/pull/1777
- feat(install): it now takes 30 seconds to install Quivr by @StanGirard in https://github.com/StanGirard/quivr/pull/1780
- feat: 🎸 install by @StanGirard in https://github.com/StanGirard/quivr/pull/1784
- fix(url): crawling fixed by @StanGirard in https://github.com/StanGirard/quivr/pull/1785
- docs: fix typo in name of docker compose dev file by @iMADi-ARCH in https://github.com/StanGirard/quivr/pull/1800

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.125...v0.0.126

## 0.0.125 (2023-11-30)

## What's Changed

- fix(api): fixed issue with name function and ilmproved promtp by @StanGirard in https://github.com/StanGirard/quivr/pull/1759
- fix: update mention suggestion filtering logic by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1763

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.124...v0.0.125

## 0.0.124 (2023-11-29)

## What's Changed

- feat(chatInput): use tiptap editor by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1752
- docs: update guidelines.md by @eltociear in https://github.com/StanGirard/quivr/pull/1755
- Feat/local llm bug fix by @StanGirard in https://github.com/StanGirard/quivr/pull/1758

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.123...v0.0.124

## 0.0.123 (2023-11-29)

## What's Changed

- chore: downgrade versions by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1748
- fix: revert implement local llms by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1749

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.122...v0.0.123

## 0.0.122 (2023-11-29)

## What's Changed

- refactor: Notification module by @gozineb in https://github.com/StanGirard/quivr/pull/1740
- refactor: remove explore route from back & front by @gozineb in https://github.com/StanGirard/quivr/pull/1741
- feat: implement local llms by @StanGirard in https://github.com/StanGirard/quivr/pull/1745
- refactor: knowledge module by @gozineb in https://github.com/StanGirard/quivr/pull/1743

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.121...v0.0.122

## 0.0.121 (2023-11-28)

## What's Changed

- fix: update max token logic by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1725
- fix: update public brain subscription logic by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1727
- fix: sanitize file name by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1728
- feat(publicBrains): use join queries for better performance by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1730
- feat: improve delete knowledge performance by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1733
- fix: 🐛 crawler by @StanGirard in https://github.com/StanGirard/quivr/pull/1735
- feat: 🎸 local user by @StanGirard in https://github.com/StanGirard/quivr/pull/1736

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.120...v0.0.121

## 0.0.120 (2023-11-27)

## What's Changed

- fix: 🐛 sentry by @StanGirard in https://github.com/StanGirard/quivr/pull/1716

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.119...v0.0.120

## 0.0.119 (2023-11-24)

## What's Changed

- refactor: Prompt module by @gozineb in https://github.com/StanGirard/quivr/pull/1688
- Fixes string formatting when logging knowledge table by @MeTaNoV in https://github.com/StanGirard/quivr/pull/1691
- fix: update max token overwrite logic by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1694
- fix: remove diacritics from filenames by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1695
- refactor: onboarding module by @gozineb in https://github.com/StanGirard/quivr/pull/1702
- feat: display notification when file size is too big by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1704
- feat: add api brain steps log (backend) by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1705

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.118...v0.0.119

## 0.0.118 (2023-11-22)

## What's Changed

- docs: add api based brains by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1685
- Adds pytesseract, tesseract and poopler-utils by @MeTaNoV in https://github.com/StanGirard/quivr/pull/1648

## New Contributors

- @MeTaNoV made their first contribution in https://github.com/StanGirard/quivr/pull/1648

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.117...v0.0.118

## 0.0.117 (2023-11-22)

## What's Changed

- fix: 🐛 api by @StanGirard in https://github.com/StanGirard/quivr/pull/1676
- fix: persist api brain creation data on tab change by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1680
- feat: 🎸 tokens by @StanGirard in https://github.com/StanGirard/quivr/pull/1678
- feat: allow updating api brain definition by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1682
- feat: make brain description required by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1684

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.116...v0.0.117

## 0.0.116 (2023-11-21)

## What's Changed

- feat: update brain modal in chat input by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1668
- feat(apiBrain): add api brain secrets field in knowledge tab by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1669
- feat(apiBrain): improve ux by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1672
- feat(feedBrain): add manage button by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1674

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.115...v0.0.116

## 0.0.115 (2023-11-20)

## What's Changed

- fix(apiBrain): fix default type selection by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1642
- fix: allow user to set a brain as public after creation by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1646
- fix(brainManagement): fix shared brain access issue by @gozineb in https://github.com/StanGirard/quivr/pull/1641
- feat: 🎸 docker reduced size by 2 by @StanGirard in https://github.com/StanGirard/quivr/pull/1653
- feat: 🎸 docker by @StanGirard in https://github.com/StanGirard/quivr/pull/1656
- feat: 🎸 marketplace by @StanGirard in https://github.com/StanGirard/quivr/pull/1657
- feat: 🎸 openai by @StanGirard in https://github.com/StanGirard/quivr/pull/1658

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.114...v0.0.115

## 0.0.114 (2023-11-16)

## What's Changed

- feat: add api brain creation frontend by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1631
- refactor: add modules folder by @gozineb in https://github.com/StanGirard/quivr/pull/1633
- feat: update settings tab add api brain definition by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1635
- feat: add public api brain subscription by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1636
- fix: delete brain on users click in brains management by @gozineb in https://github.com/StanGirard/quivr/pull/1638

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.113...v0.0.114

## 0.0.113 (2023-11-14)

## What's Changed

- refactor: packages folder be 2 by @gozineb in https://github.com/StanGirard/quivr/pull/1628

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.112...v0.0.113

## 0.0.112 (2023-11-14)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.111...v0.0.112

## 0.0.111 (2023-11-14)

## What's Changed

- ci: 🎡 tests by @StanGirard in https://github.com/StanGirard/quivr/pull/1615
- fix: update delete brain logic by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1619
- test(added): misc prompt onboarding by @StanGirard in https://github.com/StanGirard/quivr/pull/1622
- feat: remove api brain secrets and schemas on delete by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1621
- test(all): added by @StanGirard in https://github.com/StanGirard/quivr/pull/1624
- refactor: create "files" package by @gozineb in https://github.com/StanGirard/quivr/pull/1626
- feat: api definition in brain creation modal by @gozineb in https://github.com/StanGirard/quivr/pull/1613

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.110...v0.0.111

## 0.0.110 (2023-11-13)

## What's Changed

- fix: add user id while creating default brain by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1616

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.109...v0.0.110

## 0.0.109 (2023-11-13)

## What's Changed

- feat: add APIBrainQA by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1606
- feat: allow users to chat with apis by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1612
- feat(docker): use multi-stage Docker builds for smaller images by @shidenkai0 in https://github.com/StanGirard/quivr/pull/1614

## New Contributors

- @shidenkai0 made their first contribution in https://github.com/StanGirard/quivr/pull/1614

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.108...v0.0.109

## 0.0.108 (2023-11-07)

## What's Changed

- feat: add api_brain_definition table by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1601
- feat: add brain_type column to brain table by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1603
- feat: supabase vault by @gozineb in https://github.com/StanGirard/quivr/pull/1605

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.107...v0.0.108

## 0.0.107 (2023-11-06)

## What's Changed

- fix: allow to change model bro brain settings tab by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1590
- fix: fix notification banner display when too much items in chat list by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1593
- docs: add auth modes config by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1595
- fix: allow users to delete brains by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1596
- feat: 🎸 source documents by @StanGirard in https://github.com/StanGirard/quivr/pull/1598

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.106...v0.0.107

## 0.0.106 (2023-11-06)

## What's Changed

- feat: 🎸 sources by @StanGirard in https://github.com/StanGirard/quivr/pull/1591

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.105...v0.0.106

## 0.0.105 (2023-11-06)

## What's Changed

- feat: make auth mode configurable by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1579
- Fix #1290 issue running migrations by @charlesbrandt in https://github.com/StanGirard/quivr/pull/1585
- Use 'unless-stopped' instead of 'always' for development by @charlesbrandt in https://github.com/StanGirard/quivr/pull/1586
- feat: 🎸 vps by @StanGirard in https://github.com/StanGirard/quivr/pull/1587
- Update vps_install.md for subdomain by @jbeltran73-2 in https://github.com/StanGirard/quivr/pull/1589

## New Contributors

- @charlesbrandt made their first contribution in https://github.com/StanGirard/quivr/pull/1585
- @jbeltran73-2 made their first contribution in https://github.com/StanGirard/quivr/pull/1589

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.104...v0.0.105

## 0.0.104 (2023-11-03)

## What's Changed

- feat: 🎸 docs by @StanGirard in https://github.com/StanGirard/quivr/pull/1561
- style(prompts): update public prompts dropdown styling by @St-Bloom in https://github.com/StanGirard/quivr/pull/1563
- feat: add remote notification config by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1547
- fix: fix button bad children error by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1564
- style: fix hidden contents by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1577

## New Contributors

- @St-Bloom made their first contribution in https://github.com/StanGirard/quivr/pull/1563

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.103...v0.0.104

## 0.0.103 (2023-11-02)

## What's Changed

- feat: allow to share a public brain link by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1541
- fix: prompt update in brains management settings tab by @gozineb in https://github.com/StanGirard/quivr/pull/1543
- refactor: extract prompt from settings by @gozineb in https://github.com/StanGirard/quivr/pull/1546
- feat: 🎸 telegram by @StanGirard in https://github.com/StanGirard/quivr/pull/1555
- feat: 🎸 telegram by @StanGirard in https://github.com/StanGirard/quivr/pull/1559
- docs: update run_fully_local.md by @eltociear in https://github.com/StanGirard/quivr/pull/1556
- docs: grammatical errors in README.md by @HimanshuMahto in https://github.com/StanGirard/quivr/pull/1536
- fix: missing or inaccurate zh-cn translations by @jerryshang in https://github.com/StanGirard/quivr/pull/1558

## New Contributors

- @HimanshuMahto made their first contribution in https://github.com/StanGirard/quivr/pull/1536
- @jerryshang made their first contribution in https://github.com/StanGirard/quivr/pull/1558

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.102...v0.0.103

## 0.0.102 (2023-11-01)

## What's Changed

- docs: update Quivr doc by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1531
- docs: ✏️ search by @StanGirard in https://github.com/StanGirard/quivr/pull/1535
- feat(brainSettings): rework knowledge tab by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1534
- docs: ✏️ schema by @StanGirard in https://github.com/StanGirard/quivr/pull/1537
- feat: 🎸 max-token by @StanGirard in https://github.com/StanGirard/quivr/pull/1538

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.101...v0.0.102

## 0.0.101 (2023-10-31)

## What's Changed

- chore: update tanstack query dep by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1528
- fix: update mutation pending flag by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1530

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.100...v0.0.101

## 0.0.100 (2023-10-30)

## What's Changed

- refactor: fix bad smells by @gozineb in https://github.com/StanGirard/quivr/pull/1399
- refactor: chat_routes by @gozineb in https://github.com/StanGirard/quivr/pull/1512
- feat: improve ux by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1522
- feat(docs): reworked the website by @StanGirard in https://github.com/StanGirard/quivr/pull/1523
- Feat/docs rework by @StanGirard in https://github.com/StanGirard/quivr/pull/1525

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.99...v0.0.100

## 0.0.99 (2023-10-27)

## What's Changed

- fix: minor fixes by @gozineb in https://github.com/StanGirard/quivr/pull/1499
- feat: remove onboarding's feature flag by @matthieujacq in https://github.com/StanGirard/quivr/pull/1501
- feat: update form content on magic link auth request by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1502
- feat: remove legacy header and footer by @matthieujacq in https://github.com/StanGirard/quivr/pull/1509
- fix: black horizontal line sometimes appearing below section by @matthieujacq in https://github.com/StanGirard/quivr/pull/1510
- Improve readme.md by @ankur0904 in https://github.com/StanGirard/quivr/pull/1511
- refactor(settings tab): extract components by @gozineb in https://github.com/StanGirard/quivr/pull/1335
- fix: hidden video playing automatically on iphone by @matthieujacq in https://github.com/StanGirard/quivr/pull/1514

## New Contributors

- @ankur0904 made their first contribution in https://github.com/StanGirard/quivr/pull/1511

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.98...v0.0.99

## 0.0.98 (2023-10-26)

## What's Changed

- feat: upgrade button in user settings by @matthieujacq in https://github.com/StanGirard/quivr/pull/1484
- fix: failing build (removed avatar alt prop) by @matthieujacq in https://github.com/StanGirard/quivr/pull/1487
- Fixed license link in intro.md by @Eric013 in https://github.com/StanGirard/quivr/pull/1486
- feat: manage plan by @matthieujacq in https://github.com/StanGirard/quivr/pull/1488
- feat: remove feature flags for homepage by @matthieujacq in https://github.com/StanGirard/quivr/pull/1493
- feat: add new signin/login page by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1492

## New Contributors

- @Eric013 made their first contribution in https://github.com/StanGirard/quivr/pull/1486

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.97...v0.0.98

## 0.0.97 (2023-10-24)

## What's Changed

- feat(cms): update content type by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1477
- feat: upgrade to plus button by @matthieujacq in https://github.com/StanGirard/quivr/pull/1482
- feat: 🎸 sitemap by @StanGirard in https://github.com/StanGirard/quivr/pull/1483

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.96...v0.0.97

## 0.0.96 (2023-10-24)

## What's Changed

- feat: validate email and required question with react-hook-form by @matthieujacq in https://github.com/StanGirard/quivr/pull/1463
- feat: fetch security questions from CMS by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1464
- feat: POST on /contact to contact quivr team by email by @matthieujacq in https://github.com/StanGirard/quivr/pull/1466
- feat: setup premium feature backend by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1467
- feat: add sponsor and blog links by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1472
- feat: contact sales submission by @matthieujacq in https://github.com/StanGirard/quivr/pull/1473
- feat(homepage): add analytics by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1474
- fix: make use cases clickable by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1475
- fix: update blog link position by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1476

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.95...v0.0.96

## 0.0.95 (2023-10-23)

## What's Changed

- feat: homepage first section by @matthieujacq in https://github.com/StanGirard/quivr/pull/1439
- fix: show a flat gradient in the UseCase section by @matthieujacq in https://github.com/StanGirard/quivr/pull/1440
- style: update testimonials display by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1441
- feat: fetch homepage data from CMS by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1452
- feat: contact sales page (front layout) by @matthieujacq in https://github.com/StanGirard/quivr/pull/1451
- Fix: Improved Text Visibility in Dark Mode in OnboardingQuestion Component by @Dev-Dz27 in https://github.com/StanGirard/quivr/pull/1456
- feat(cms): added single video demo by @StanGirard in https://github.com/StanGirard/quivr/pull/1459
- feat: fetch demo video from CMS by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1461
- feat: Contact form component by @matthieujacq in https://github.com/StanGirard/quivr/pull/1453

## New Contributors

- @Dev-Dz27 made their first contribution in https://github.com/StanGirard/quivr/pull/1456

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.94...v0.0.95

## 0.0.94 (2023-10-19)

## What's Changed

- feat: Homepage demo section by @matthieujacq in https://github.com/StanGirard/quivr/pull/1420
- feat: add security section by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1423
- feat: HomePage new footer by @matthieujacq in https://github.com/StanGirard/quivr/pull/1425
- feat: add testimonials section by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1427
- refactor(backend): cleaning dead and unused code by @StanGirard in https://github.com/StanGirard/quivr/pull/1432

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.93...v0.0.94

## 0.0.93 (2023-10-17)

## What's Changed

- feat: add use cases to homepage by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1415
- feat: Homepage screen 1 content by @matthieujacq in https://github.com/StanGirard/quivr/pull/1414

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.92...v0.0.93

## 0.0.92 (2023-10-17)

## What's Changed

- feat: add a cron to remove onboarding more than 7 days by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1397
- feat: 🖼️ new homepage background by @matthieujacq in https://github.com/StanGirard/quivr/pull/1395

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.91...v0.0.92

## 0.0.91 (2023-10-12)

## What's Changed

- feat: track onboarding events by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1388
- fix(user identity): User identity dict has no attribute user_id and open_api_key by @HamzaKhalidDhillon in https://github.com/StanGirard/quivr/pull/1351
- feat: new homepage header by @matthieujacq in https://github.com/StanGirard/quivr/pull/1382
- feat(onboarding): add suggested questions answer by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1390

## New Contributors

- @HamzaKhalidDhillon made their first contribution in https://github.com/StanGirard/quivr/pull/1351

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.90...v0.0.91

## 0.0.90 (2023-10-11)

## What's Changed

- feat: add Welcome chat by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1365
- feat: handle suggestion click by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1368
- refactor: Enable linting on login+signup page and hooks by @matthieujacq in https://github.com/StanGirard/quivr/pull/1369
- feat: finish onboarding step on first upload or crawl by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1373
- feat: add create_user_onboarding_function by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1383
- feat: remove user onboarding on complete by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1387

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.89...v0.0.90

## 0.0.89 (2023-10-09)

## What's Changed

- feat: enable CSP in all environments (local/preview/prod) by @matthieujacq in https://github.com/StanGirard/quivr/pull/1334
- feat: enhance user page UI by @nguernse in https://github.com/StanGirard/quivr/pull/1319
- feat: update onboarding steps by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1337
- feat: add onboarding_a column to onboarding table by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1340
- fix(question): fixed with user_settings by @StanGirard in https://github.com/StanGirard/quivr/pull/1349
- FIX tables.sql - missing ; breaks SQL queries. by @stanrb in https://github.com/StanGirard/quivr/pull/1348
- feat: ⚙️🐞 configure debugger for the backend by @matthieujacq in https://github.com/StanGirard/quivr/pull/1345
- test: add chat e2e tests by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1344
- feat: configure CSP for self-hosting and multiple ports in dev mode by @matthieujacq in https://github.com/StanGirard/quivr/pull/1364

## New Contributors

- @stanrb made their first contribution in https://github.com/StanGirard/quivr/pull/1348

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.88...v0.0.89

## 0.0.88 (2023-10-05)

## What's Changed

- fix: wrap parsing with try catch statements by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1321
- fix: 🐛 ↕️ 📱height now matches mobile height by @matthieujacq in https://github.com/StanGirard/quivr/pull/1323
- feat: add onboarding step 3 by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1324
- feat: restructure the sidebar of the brains management page by @matthieujacq in https://github.com/StanGirard/quivr/pull/1325
- feat: add onboarding table by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1327
- feat: update onboarding controller and fix typo by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1333

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.87...v0.0.88

## 0.0.87 (2023-10-03)

## What's Changed

- feat: ↕️ maximize brains management page by @matthieujacq in https://github.com/StanGirard/quivr/pull/1308
- refactor: ♻️ ContentSecurityPolicy as an object by @matthieujacq in https://github.com/StanGirard/quivr/pull/1312
- fix: replace next/image's layout deprecated attribute by @matthieujacq in https://github.com/StanGirard/quivr/pull/1313
- fix: remove undesired outlines around divs by @matthieujacq in https://github.com/StanGirard/quivr/pull/1316
- feat(onboarding): add step 2 by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1314
- feat(onboarding): add questions suggestions layout by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1318

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.86...v0.0.87

## 0.0.86 (2023-10-03)

## What's Changed

- fix(script): added percent before list of emails by @StanGirard in https://github.com/StanGirard/quivr/pull/1284
- feat: improve app ux by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1281
- test: add e2e for crawling by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1288
- feat(user_settings): increased by @StanGirard in https://github.com/StanGirard/quivr/pull/1291
- fix: prevent fetch when user is not logged in by @nguernse in https://github.com/StanGirard/quivr/pull/1293
- fix(Select): fix JSX typo by @nguernse in https://github.com/StanGirard/quivr/pull/1292
- feat: ✨ responsive sidebar by @matthieujacq in https://github.com/StanGirard/quivr/pull/1279
- fix: 🐛 Sidebar content should not hide the sidebar footer by @matthieujacq in https://github.com/StanGirard/quivr/pull/1298
- feat: allow users to turn private brain to public by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1300
- feat: add onboarding first step by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1303
- feat: update chat list on new chat first message by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1305
- feat: ↕️ Maximise chat window by @matthieujacq in https://github.com/StanGirard/quivr/pull/1301

## New Contributors

- @nguernse made their first contribution in https://github.com/StanGirard/quivr/pull/1293

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.85...v0.0.86

## 0.0.84 (2023-09-28)

## What's Changed

- feat: 👤 Implement gravatar by @matthieujacq in https://github.com/StanGirard/quivr/pull/1268
- feat: improve knowledge feed process ux by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1274
- fix: 🔒️ add gravatar.com to the content security policy by @matthieujacq in https://github.com/StanGirard/quivr/pull/1273
- feat(chatPage): update ui add new feed component by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1275
- feat: knowledge tab add button by @gozineb in https://github.com/StanGirard/quivr/pull/1277
- fix(brains): get brains on local by @B0rrA in https://github.com/StanGirard/quivr/pull/1272

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.83...v0.0.84

## 0.0.83 (2023-09-27)

## What's Changed

- feat(nav): 🚚 Move Brain and User buttons to the sidebar in the chat by @matthieujacq in https://github.com/StanGirard/quivr/pull/1262
- feat: save last chat config and make it default one by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1266
- style: improve upload ux by @Rahil2507 in https://github.com/StanGirard/quivr/pull/1259
- fix(docs): add prerequisites section in step 2 by @JvSdv in https://github.com/StanGirard/quivr/pull/1149
- style: improve ui by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1263

## New Contributors

- @Rahil2507 made their first contribution in https://github.com/StanGirard/quivr/pull/1259
- @JvSdv made their first contribution in https://github.com/StanGirard/quivr/pull/1149

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.82...v0.0.83

## 0.0.82 (2023-09-26)

## What's Changed

- fix(RBAC): skip validation for unplug by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1264

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.81...v0.0.82

## 0.0.81 (2023-09-26)

## What's Changed

- feat: activate public brain subscription by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1241
- feat(publicBrain): disable subscribe button when already subscribed and refetch brains list by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1246
- feat: knowledge tab list by @gozineb in https://github.com/StanGirard/quivr/pull/1222
- fix(preview): fixed a few bugs unchecked by @StanGirard in https://github.com/StanGirard/quivr/pull/1247
- feat: add last_update field to brain table by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1252
- fix: urls to avoid 307 by @gozineb in https://github.com/StanGirard/quivr/pull/1253
- feat: allow user to unsubscribe from a brain by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1254
- feat(user): 🚚 Move language and theme buttons to the User page by @matthieujacq in https://github.com/StanGirard/quivr/pull/1256
- Update next.config.js by @riccardolinares in https://github.com/StanGirard/quivr/pull/1251
- feat: allow setting public brain status to private by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1258

## New Contributors

- @matthieujacq made their first contribution in https://github.com/StanGirard/quivr/pull/1256
- @riccardolinares made their first contribution in https://github.com/StanGirard/quivr/pull/1251

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.80...v0.0.81

## 0.0.80 (2023-09-21)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.79...v0.0.80

## 0.0.79 (2023-09-21)

## What's Changed

- fix(gpt-3.5-instruct): bug and new version of node by @StanGirard in https://github.com/StanGirard/quivr/pull/1228
- feat: display brain status on settings page by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1221
- feat(upload): changed icons by @StanGirard in https://github.com/StanGirard/quivr/pull/1233
- Feat/paperclip by @StanGirard in https://github.com/StanGirard/quivr/pull/1234
- fix(brain_size): increased size by @StanGirard in https://github.com/StanGirard/quivr/pull/1235
- feat(strapi): added first draft by @StanGirard in https://github.com/StanGirard/quivr/pull/1237
- feat: add public brain page by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1230
- feat: count public brains number of subscribers by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1236

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.78...v0.0.79

## 0.0.78 (2023-09-20)

## What's Changed

- feat: add public brain creation by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1218
- feat: get files from storage by @gozineb in https://github.com/StanGirard/quivr/pull/1205

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.77...v0.0.78

## 0.0.77 (2023-09-19)

## What's Changed

- feat(memory): optimisation by @StanGirard in https://github.com/StanGirard/quivr/pull/1214

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.76...v0.0.77

## 0.0.76 (2023-09-19)

## What's Changed

- chore(theodo): added trigger function for theodo by @StanGirard in https://github.com/StanGirard/quivr/pull/1195
- feat: add tooltip on upload card toggle button by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1197
- feat(analytics): add google analytics by @gozineb in https://github.com/StanGirard/quivr/pull/1147
- Feat/theodo gpt4 by @StanGirard in https://github.com/StanGirard/quivr/pull/1198
- fix(chats): now in order and with a little bonus ;) by @StanGirard in https://github.com/StanGirard/quivr/pull/1200
- fix: fix some bugs by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1201
- feat(question): now not rephrasing question when passed to answering llm by @StanGirard in https://github.com/StanGirard/quivr/pull/1202

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.75...v0.0.76

## 0.0.75 (2023-09-18)

## What's Changed

- feat(frontend): responsiveness by @StanGirard in https://github.com/StanGirard/quivr/pull/1174
- feat(upload): changed to task by @StanGirard in https://github.com/StanGirard/quivr/pull/1178
- fix(qa_base): asign max_token to llm by @B0rrA in https://github.com/StanGirard/quivr/pull/1179
- feat(perf): increased perf embedding and search for files by @StanGirard in https://github.com/StanGirard/quivr/pull/1182
- fix(usersettings): Fix bugs with user settings in the back always gpt-3.5-turbo by @StanGirard in https://github.com/StanGirard/quivr/pull/1183
- feat(notificatins): higher refresh rate by @StanGirard in https://github.com/StanGirard/quivr/pull/1184
- style(notifications): improve the messages for the notifications by @StanGirard in https://github.com/StanGirard/quivr/pull/1185
- fix(notifications): dead notifications that are still present long after by @StanGirard in https://github.com/StanGirard/quivr/pull/1186
- fix(notifications): greater than 5 minutes ago not less by @StanGirard in https://github.com/StanGirard/quivr/pull/1187
- feat(aws): improved size by @StanGirard in https://github.com/StanGirard/quivr/pull/1188
- feat(concurrency): added concurrency for increased performance by @StanGirard in https://github.com/StanGirard/quivr/pull/1189
- feat(prompt): improved answer readability with markdown and aerataed by @StanGirard in https://github.com/StanGirard/quivr/pull/1190
- fix(notification): information now displayed on the right by @StanGirard in https://github.com/StanGirard/quivr/pull/1191
- feat(chat): added copy feature to message by @StanGirard in https://github.com/StanGirard/quivr/pull/1192
- feat(e2e): add playright config and createBrain e2e test by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1177

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.74...v0.0.75

## 0.0.74 (2023-09-14)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.73...v0.0.74

## 0.0.73 (2023-09-14)

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.72...v0.0.73

## 0.0.72 (2023-09-14)

## What's Changed

- feat(file-system): added queue and filesystem by @StanGirard in https://github.com/StanGirard/quivr/pull/1159
- fix(migration): removed by @StanGirard in https://github.com/StanGirard/quivr/pull/1170

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.71...v0.0.72

## 0.0.71 (2023-09-14)

## What's Changed

- feat: the good user management by @StanGirard in https://github.com/StanGirard/quivr/pull/1158
- feat: add knowledge tab on brains settings page by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1163
- feat: update header and improve ux by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1164
- feat: submit upload on Enter by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1160
- feat: make error messages more clear by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1166

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.70...v0.0.71

## 0.0.70 (2023-09-12)

## What's Changed

- feat: add notifications components by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1148
- feat: add polling for pending notifications by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1152
- fix(selectedBrain): prevent picking brainId from local storage by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1154
- feat: update isValidUrl function by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1155

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.69...v0.0.70

## 0.0.69 (2023-09-08)

## What's Changed

- feat: add multiple upload and crawl in parallel by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1118
- feat: allow user to chat while feed process is pending by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1120
- feat: add notifications table, and push notification on upload and crawl by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1125
- feat: merge chat history with chat notifications by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1127
- feat(feedBrain): add request pending message #1135 by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1136
- fix: update crawl and upload endpoints by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1142
- make docker compose command more flexible by @thehunmonkgroup in https://github.com/StanGirard/quivr/pull/1139

## New Contributors

- @thehunmonkgroup made their first contribution in https://github.com/StanGirard/quivr/pull/1139

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.68...v0.0.69

## 0.0.68 (2023-09-06)

## What's Changed

- feat(liteLLM): Add support for Azure OpenAI, Palm, Claude-2, Llama2, CodeLlama (100+LLMs) by @ishaan-jaff in https://github.com/StanGirard/quivr/pull/1097
- feat(crawler): add multiple urls support by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1112
- fix(csp): add growthbook to csp headers by @gozineb in https://github.com/StanGirard/quivr/pull/1117

## New Contributors

- @ishaan-jaff made their first contribution in https://github.com/StanGirard/quivr/pull/1097

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.67...v0.0.68

## 0.0.67 (2023-09-05)

## What's Changed

- feat: add FeedBrainInput component by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1101
- feat: add <Feed /> component in chat page by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1103
- 🚑 fix feature flags -> add it back to context by @gozineb in https://github.com/StanGirard/quivr/pull/1106

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.66...v0.0.67

## 0.0.66 (2023-09-04)

## What's Changed

- fix(prod): add url api.openai to CSP headers by @gozineb in https://github.com/StanGirard/quivr/pull/1077
- feat: change share brain button logic by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1078
- fix(brainsSettings): handle nullish value from api call by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1080
- fix: update hash routing logic by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1082
- fix: fix hash redirection by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1085
- feat: add tanstack query and optimistic fetch on brains settings page by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1087
- docs: writeup for running quivr fully locally by @mvda in https://github.com/StanGirard/quivr/pull/1096
- fix: prevent submit on share button click by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1098

## New Contributors

- @mvda made their first contribution in https://github.com/StanGirard/quivr/pull/1096

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.65...v0.0.66

## 0.0.65 (2023-08-31)

## What's Changed

- feat: make chatlist scrollable by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1064
- feat(newBrain): update data validation logic and add \* on required fields by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1065
- feat(shareBrain): prevent re inviting users with access by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1063
- feat(chatMessage): update attributes display by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1067
- fix: fix minor bugs by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1070
- feat: remove mic button by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1075
- feat: truncate long chat name by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1076

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.64...v0.0.65

## 0.0.64 (2023-08-30)

## What's Changed

- feat: add prompt trigger through # by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1023
- feat: add headless question tracking by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1051
- feat: update header and remove prompt / brain on backspace by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1052
- feat: handle new chat button click by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1054
- feat: add name missing error in new brain modal by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1055
- feat: validate api key before saving by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1057
- feat: track prompt and brain changes by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1058
- feat(chat): update chat input placeholder by @gozineb in https://github.com/StanGirard/quivr/pull/1060
- fix(invitationPage): avoid multiple re-rendering by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1062

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.63...v0.0.64

## 0.0.63 (2023-08-27)

## What's Changed

- fix(dockerfile): backend Dockerfile exit code 1 by @pat266 in https://github.com/StanGirard/quivr/pull/1032
- test(backend): skip failing tests by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1036
- feat(messagesList): auto scroll on new message by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1040
- test: unskip `qa_headless.py` linter tests by @mamadoudicko in https://github.com/StanGirard/quivr/pull/1041
- feat: add 2 save buttons on Brain management tab by @ChloeMouret in https://github.com/StanGirard/quivr/pull/1039
- feat(brain): add endpoint to return context to question by @ZongZiWang in https://github.com/StanGirard/quivr/pull/1044
- fix: English grammar translation.json by @elie222 in https://github.com/StanGirard/quivr/pull/1046

## New Contributors

- @pat266 made their first contribution in https://github.com/StanGirard/quivr/pull/1032
- @elie222 made their first contribution in https://github.com/StanGirard/quivr/pull/1046

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.62...v0.0.63

## 0.0.62 (2023-08-25)

## What's Changed

- feat: Remove chat id from chat list by @ChloeMouret in https://github.com/StanGirard/quivr/pull/1031
- fix(analytics): june debug for real by @gozineb in https://github.com/StanGirard/quivr/pull/1033

**Full Changelog**: https://github.com/StanGirard/quivr/compare/v0.0.61...v0.0.62

## [0.0.61](https://github.com/StanGirard/quivr/compare/v0.0.60...v0.0.61) (2023-08-23)

### Features

- add brain prompt overwritting from chat ([#1012](https://github.com/StanGirard/quivr/issues/1012)) ([b967c2d](https://github.com/StanGirard/quivr/commit/b967c2d2d60b93f9142fe2afd04fb9422adcc2be))
- **backend:** adds python code parsing ([#1003](https://github.com/StanGirard/quivr/issues/1003)) ([a626b84](https://github.com/StanGirard/quivr/commit/a626b84b96c7b40904960e039f72ff042148a240))
- **prompts:** add public prompts to SQL db ([#1014](https://github.com/StanGirard/quivr/issues/1014)) ([4b1f4b1](https://github.com/StanGirard/quivr/commit/4b1f4b141287d109794aa6015f83deb3882ac5cb))
- **translation:** Added Simplified Chinese translation，Fix pt-br not working ([#1011](https://github.com/StanGirard/quivr/issues/1011)) ([e328ab8](https://github.com/StanGirard/quivr/commit/e328ab81b30f2dd3dae7287e0351fdacd1c18133))

### Bug Fixes

- **Analytics:** no tags tracking for upload & crawl ([#1024](https://github.com/StanGirard/quivr/issues/1024)) ([2b74ebc](https://github.com/StanGirard/quivr/commit/2b74ebc1f099c4d12705d458fefad94120af9208))

## [0.0.60](https://github.com/StanGirard/quivr/compare/v0.0.59...v0.0.60) (2023-08-22)

### Features

- **chat:** add brain selection through mention input ([#969](https://github.com/StanGirard/quivr/issues/969)) ([8e94f22](https://github.com/StanGirard/quivr/commit/8e94f22782dd2255e8125fbb4b3718413ad4701e))

### Bug Fixes

- remove conflicts ([#998](https://github.com/StanGirard/quivr/issues/998)) ([f61b70a](https://github.com/StanGirard/quivr/commit/f61b70a34f6d24e6f343d31cc4aa63265bb1c218))
- update backend tests ([#992](https://github.com/StanGirard/quivr/issues/992)) ([5a3a6fe](https://github.com/StanGirard/quivr/commit/5a3a6fe370756783a204f2a62007f6cb23c7b202))

## [0.0.59](https://github.com/StanGirard/quivr/compare/v0.0.58...v0.0.59) (2023-08-20)

### Features

- **aws:** all in microservices ([b3a6231](https://github.com/StanGirard/quivr/commit/b3a6231274e5aea28675381ba6f7ba277228f5ac))
- **chat-service:** added task definition ([d001ec7](https://github.com/StanGirard/quivr/commit/d001ec70df3ccd5f3885b5f174e58f1b3238c433))
- **docker:** improved size image ([#978](https://github.com/StanGirard/quivr/issues/978)) ([aa623c4](https://github.com/StanGirard/quivr/commit/aa623c4039ba31928dd0934a682259c7762d2efa))
- **docker:** pushing image to github registry ([ad3dca3](https://github.com/StanGirard/quivr/commit/ad3dca3e2705b87a9c9c0b35f67773bcc182ae88))
- **gcr:** removed sha and put latest ([2b85a94](https://github.com/StanGirard/quivr/commit/2b85a94e8835861afd9c178b72e59d018d8b956f))
- **health:** added endpoint for services ([#989](https://github.com/StanGirard/quivr/issues/989)) ([ae7852e](https://github.com/StanGirard/quivr/commit/ae7852ec3f9d6e20b28c3b6fbc0d433d476395ea))
- **microservices:** split into 4 quivr to better handle long services ([#972](https://github.com/StanGirard/quivr/issues/972)) ([7281fd9](https://github.com/StanGirard/quivr/commit/7281fd905a24b8e4dad7214d7809b8856685fca8))
- **preview:** added crawl service to ci ([b7f9876](https://github.com/StanGirard/quivr/commit/b7f9876ce20a2c802ccfd7cff35de50ac2fd2226))
- **preview:** added preview ([#974](https://github.com/StanGirard/quivr/issues/974)) ([9eb25a4](https://github.com/StanGirard/quivr/commit/9eb25a4d1777b9fdbc1c4b93df0b51e8b28d3ae9))
- **preview:** added service upload ([#979](https://github.com/StanGirard/quivr/issues/979)) ([ce6b45e](https://github.com/StanGirard/quivr/commit/ce6b45e1ac8e9a3d21b7f56ad228351e34179e11))
- **refacto:** changed a bit of things to make better dx ([#984](https://github.com/StanGirard/quivr/issues/984)) ([d0370ab](https://github.com/StanGirard/quivr/commit/d0370ab499465ee1404d3c1d32878e8da3853441))
- **Unplug:** chatting without brain streaming ([#970](https://github.com/StanGirard/quivr/issues/970)) ([600ff1e](https://github.com/StanGirard/quivr/commit/600ff1ede02741c66853cc3e4e7f5001aaba3bc2))

### Bug Fixes

- **settings:** select proper brain model ([#943](https://github.com/StanGirard/quivr/issues/943)) ([3a44f54](https://github.com/StanGirard/quivr/commit/3a44f54d6b75581e3cbc8acf0c1c309c3273e63f))
- update backend tests ([#975](https://github.com/StanGirard/quivr/issues/975)) ([c746eb1](https://github.com/StanGirard/quivr/commit/c746eb18303945a1736c89427026b509f501e715))
- **windows:** removed unused start script ([#962](https://github.com/StanGirard/quivr/issues/962)) ([ad7ac15](https://github.com/StanGirard/quivr/commit/ad7ac1516d5c45c833c9e9ba6162012096372fa6))

## [0.0.57](https://github.com/StanGirard/quivr/compare/v0.0.56...v0.0.57) (2023-08-16)

### Features

- add brain missing message ([#958](https://github.com/StanGirard/quivr/issues/958)) ([f99f81d](https://github.com/StanGirard/quivr/commit/f99f81d10f9c768af00e38249763a252f8db16e3))
- change messages position ([#946](https://github.com/StanGirard/quivr/issues/946)) ([9235a84](https://github.com/StanGirard/quivr/commit/9235a848d12b96af346cc2cbb1ac50dc2f67b20c))
- update chat ui ([#907](https://github.com/StanGirard/quivr/issues/907)) ([80be40a](https://github.com/StanGirard/quivr/commit/80be40ad34d07b646d48d2aa0405a92b3de308d7))

### Bug Fixes

- **chat routes:** use brain model, temp, and token ([#902](https://github.com/StanGirard/quivr/issues/902)) ([59ddfb4](https://github.com/StanGirard/quivr/commit/59ddfb48823b56239fe7fc95133274a3bedf49da))
- **chatMessages:** Fix error on answering question ([#953](https://github.com/StanGirard/quivr/issues/953)) ([1fef9b0](https://github.com/StanGirard/quivr/commit/1fef9b078379c8991f6029c34ac10d4cbdc5a44d))
- **crawler:** using newspaper and fixed recursive by merging content ([#955](https://github.com/StanGirard/quivr/issues/955)) ([d7c5c79](https://github.com/StanGirard/quivr/commit/d7c5c79043827b2b0949f6fd6c508c4617dcf498))
- **translations:** pr portuguese translations ([#933](https://github.com/StanGirard/quivr/issues/933)) ([d80178a](https://github.com/StanGirard/quivr/commit/d80178a84802c35b2c13d3eef4d0438fd067da92))

## [0.0.56](https://github.com/StanGirard/quivr/compare/v0.0.55...v0.0.56) (2023-08-10)

### Bug Fixes

- **chat:** update data keys ([#923](https://github.com/StanGirard/quivr/issues/923)) ([21db719](https://github.com/StanGirard/quivr/commit/21db7197965f1cacd6595ae94d9017fc54d761c3))

## [0.0.55](https://github.com/StanGirard/quivr/compare/v0.0.54...v0.0.55) (2023-08-10)

### Features

- **chatMessages:** add brain_id and prompt_id columns ([#912](https://github.com/StanGirard/quivr/issues/912)) ([6e77732](https://github.com/StanGirard/quivr/commit/6e777327aaee7b9f35b20dcd00814f4acbaf448e))
- **invitation:** add translations ([#909](https://github.com/StanGirard/quivr/issues/909)) ([1360ce8](https://github.com/StanGirard/quivr/commit/1360ce801d8958defa5dd29a481e2e66ac6ae9ac))
- Russian language translation ([#903](https://github.com/StanGirard/quivr/issues/903)) ([672eec0](https://github.com/StanGirard/quivr/commit/672eec08bc7113e3f4c32a29ae86b2b879262d30))

## [0.0.54](https://github.com/StanGirard/quivr/compare/v0.0.53...v0.0.54) (2023-08-08)

### Features

- add new chat bar ([#896](https://github.com/StanGirard/quivr/issues/896)) ([69a73f5](https://github.com/StanGirard/quivr/commit/69a73f5d5ae58dca9c23c0d8751f8c7326c84f4c))
- add new chat page ([#890](https://github.com/StanGirard/quivr/issues/890)) ([c43e0c0](https://github.com/StanGirard/quivr/commit/c43e0c01c4ddcf0d97b9bb89784ff004fb7a0a79))
- deleting brains on brain manager page ([#893](https://github.com/StanGirard/quivr/issues/893)) ([71e142b](https://github.com/StanGirard/quivr/commit/71e142ba3c164e5f14959cd1fd5de38531779034))

### Bug Fixes

- **es:** spanish translations ([#895](https://github.com/StanGirard/quivr/issues/895)) ([69d0893](https://github.com/StanGirard/quivr/commit/69d08937de1540cf39a6462b4583b2c4c908d0af))
- **sentry:** some unhandled errors ([#894](https://github.com/StanGirard/quivr/issues/894)) ([9ba7241](https://github.com/StanGirard/quivr/commit/9ba724168eacf4b074ad062f2a58b637597335ba))

## [0.0.53](https://github.com/StanGirard/quivr/compare/v0.0.52...v0.0.53) (2023-08-07)

### Features

- **backend:** add custom prompt ([#885](https://github.com/StanGirard/quivr/issues/885)) ([61cd0a6](https://github.com/StanGirard/quivr/commit/61cd0a6bde989bc9f931f47967c3bbddc3b0446b))
- **fr:** added language ([#884](https://github.com/StanGirard/quivr/issues/884)) ([1160e16](https://github.com/StanGirard/quivr/commit/1160e160141f350a39ae4f73ff88ad79e1b1d874))
- gpt4 is not available for brains if there is no given openAiKey ([#850](https://github.com/StanGirard/quivr/issues/850)) ([e9ebeef](https://github.com/StanGirard/quivr/commit/e9ebeef72ae2dee40b6bdff58121f9f9e1814577))
- **qa:** improve code ([#886](https://github.com/StanGirard/quivr/issues/886)) ([7028505](https://github.com/StanGirard/quivr/commit/7028505571a8e1f8569a12b770b3ce99cd2ec4e0))

### Bug Fixes

- **i18n:** update tests for french and spanish ([#878](https://github.com/StanGirard/quivr/issues/878)) ([b0514d6](https://github.com/StanGirard/quivr/commit/b0514d6149d474747de642d12454f6b511a1f947))

## [0.0.52](https://github.com/StanGirard/quivr/compare/v0.0.51...v0.0.52) (2023-08-07)

### Features

- add custom prompt fields on brain setting pages ([#837](https://github.com/StanGirard/quivr/issues/837)) ([99a3fa9](https://github.com/StanGirard/quivr/commit/99a3fa9b296520a71028194e21bc808a2ec208a0))
- add public prompts picker ([#841](https://github.com/StanGirard/quivr/issues/841)) ([b3fb8fc](https://github.com/StanGirard/quivr/commit/b3fb8fc3bc2d71a72e73b4f0aa30c84255a77fc0))
- remove private prompts on related brain delete ([#842](https://github.com/StanGirard/quivr/issues/842)) ([4c15fe2](https://github.com/StanGirard/quivr/commit/4c15fe2bfde7a2fdc59c299ef668f1ba0cd8ffa8))

### Bug Fixes

- **pg-database:** by default variable is not implemented ([#848](https://github.com/StanGirard/quivr/issues/848)) ([69e2c28](https://github.com/StanGirard/quivr/commit/69e2c289e5a6e4cfd6b7187a3c4fda5c538d5d35))
- remove typo ([#853](https://github.com/StanGirard/quivr/issues/853)) ([5496e9d](https://github.com/StanGirard/quivr/commit/5496e9d738a1f80f11b6c8fa8606960abcbcd06d))

### Performance Improvements

- **deps:** removed ([#873](https://github.com/StanGirard/quivr/issues/873)) ([10d4d65](https://github.com/StanGirard/quivr/commit/10d4d65c1e203aaae1069395ed5066fbfc9c7715))

## [0.0.51](https://github.com/StanGirard/quivr/compare/v0.0.50...v0.0.51) (2023-08-03)

### Features

- **backend:** implement brain-prompt link ([#831](https://github.com/StanGirard/quivr/issues/831)) ([4ca6c66](https://github.com/StanGirard/quivr/commit/4ca6c667da3d5daf0339c65f077c8956c7ef42e8))
- **prompt:** add prompt table, entity and repository ([#823](https://github.com/StanGirard/quivr/issues/823)) ([e3b6114](https://github.com/StanGirard/quivr/commit/e3b6114248ee04a9dc6b93093256d82324672925))

### Bug Fixes

- **chat routes:** HTTPException import correction ([#833](https://github.com/StanGirard/quivr/issues/833)) ([68f03b2](https://github.com/StanGirard/quivr/commit/68f03b2416f5b49e9f8e72c5b1c91754792a1233))
- **chats:** delete chats from correct table ([#834](https://github.com/StanGirard/quivr/issues/834)) ([659e585](https://github.com/StanGirard/quivr/commit/659e585145ea0aa8bf88ecc48d31e0b65098a729))
- **env:** added pg database url default value to none ([23f50ec](https://github.com/StanGirard/quivr/commit/23f50ec3a37af453f1b8b69592d1a640189d50e8))

## [0.0.50](https://github.com/StanGirard/quivr/compare/v0.0.49...v0.0.50) (2023-08-02)

### Features

- Introduce repository pattern to prepare adding other database providers ([#646](https://github.com/StanGirard/quivr/issues/646)) ([303ba72](https://github.com/StanGirard/quivr/commit/303ba72028d349196b78cc07db627115ec0aff90))
- **prompt:** added instructions in standalone question & a bit more things ([#826](https://github.com/StanGirard/quivr/issues/826)) ([c217979](https://github.com/StanGirard/quivr/commit/c21797905d7d57dab73f9b7047da1a50aae37b9b))

## [0.0.49](https://github.com/StanGirard/quivr/compare/v0.0.48...v0.0.49) (2023-08-01)

### Features

- add chat config modal ([#807](https://github.com/StanGirard/quivr/issues/807)) ([d018ab6](https://github.com/StanGirard/quivr/commit/d018ab6a9334b45b86e0c7fed3a552f5cb202523))

### Bug Fixes

- bugs ([#818](https://github.com/StanGirard/quivr/issues/818)) ([edcbb30](https://github.com/StanGirard/quivr/commit/edcbb30e97535013b61d5a94bb4204d030cba2f2))

## [0.0.48](https://github.com/StanGirard/quivr/compare/v0.0.47...v0.0.48) (2023-08-01)

### Bug Fixes

- **openai:** user key now used for llm model ([c01433c](https://github.com/StanGirard/quivr/commit/c01433c84194e1d155ad3917de58257d24c30c38))

## [0.0.47](https://github.com/StanGirard/quivr/compare/v0.0.46...v0.0.47) (2023-08-01)

### Features

- add user level open ai key management ([#805](https://github.com/StanGirard/quivr/issues/805)) ([7532b55](https://github.com/StanGirard/quivr/commit/7532b558c74962e5916b951235e8578cc8e882a2))
- **chat:** added streaming ([#808](https://github.com/StanGirard/quivr/issues/808)) ([3166d08](https://github.com/StanGirard/quivr/commit/3166d089ee82730882c26454bd110a3dfae067c9))
- **llm:** removing all llms to prepare for genoss ([#804](https://github.com/StanGirard/quivr/issues/804)) ([db40f3c](https://github.com/StanGirard/quivr/commit/db40f3cccd596f4337823e0306e66224d5e1c8c9))

## [0.0.46](https://github.com/StanGirard/quivr/compare/v0.0.45...v0.0.46) (2023-07-31)

### Features

- **aws:** increased numer of replicas to 10 ([9809ef4](https://github.com/StanGirard/quivr/commit/9809ef4119a2351b78217c73c545b7e327676135))
- **aws:** increased size ([56f254a](https://github.com/StanGirard/quivr/commit/56f254a050fcc3b9ee073318bd566e03675658cd))

### Bug Fixes

- **frontend:** correctly display document information in explore view details ([#781](https://github.com/StanGirard/quivr/issues/781)) ([87c5e58](https://github.com/StanGirard/quivr/commit/87c5e582a2579ebb68f272cb62175dfa6f2e6dc8))
- Toast message hidden under the footer ([#761](https://github.com/StanGirard/quivr/issues/761)) ([3e8ed46](https://github.com/StanGirard/quivr/commit/3e8ed463173659ebe599602e97c2d11191144ecb))
- udpate migration script doc ([#793](https://github.com/StanGirard/quivr/issues/793)) ([a609c01](https://github.com/StanGirard/quivr/commit/a609c01aa8fab10e74eed64edd795c56bece1fdb))

## [0.0.45](https://github.com/StanGirard/quivr/compare/v0.0.44...v0.0.45) (2023-07-27)

### Bug Fixes

- **release-please:** use personal token to be able to trigger release ([#789](https://github.com/StanGirard/quivr/issues/789)) ([2fcff0b](https://github.com/StanGirard/quivr/commit/2fcff0bedab3a53cb3dc395c0e362edb2962aaa7))

## [0.0.44](https://github.com/StanGirard/quivr/compare/v0.0.43...v0.0.44) (2023-07-27)

### Features

- **pr-title:** added pr-title checlk ([b11b2d8](https://github.com/StanGirard/quivr/commit/b11b2d8658fec3940bb0c0280124cbdd77d8d74b))

### Bug Fixes

- **release-please:** fixed actions ([16114b2](https://github.com/StanGirard/quivr/commit/16114b2c5271ab299b7e84f5a9e552dab58cd211))

## [0.0.43](https://github.com/StanGirard/quivr/compare/v0.0.42...v0.0.43) (2023-07-26)

### Features

- **workflow:** added release please ([e6ba9e8](https://github.com/StanGirard/quivr/commit/e6ba9e80f48a1d8822c99e5b77e064dc2b18e718))
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

      (e) Some folders or files within the distribution may be subject to
          different license terms and conditions. In such cases, the
          applicable license will be specified in a separate LICENSE file
          or within the file itself. You must comply with the terms of
          these additional licenses when using, reproducing, or distributing
          those specific folders or files.

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

   Copyright [2023-2024] [Quivr]

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

## File: `README.md`
```markdown
# Quivr - Your Second Brain, Empowered by Generative AI

<div align="center">
    <img src="./logo.png" alt="Quivr-logo" width="31%"  style="border-radius: 50%; padding-bottom: 20px"/>
</div>

[![Discord Follow](https://dcbadge.vercel.app/api/server/HUpRgp2HG8?style=flat)](https://discord.gg/HUpRgp2HG8)
[![GitHub Repo stars](https://img.shields.io/github/stars/quivrhq/quivr?style=social)](https://github.com/quivrhq/quivr)
[![Twitter Follow](https://img.shields.io/twitter/follow/StanGirard?style=social)](https://twitter.com/_StanGirard)

Quivr, helps you build your second brain, utilizes the power of GenerativeAI to be your personal assistant !

## Key Features 🎯

- **Opiniated RAG**: We created a RAG that is opinionated, fast and efficient so you can focus on your product
- **LLMs**: Quivr works with any LLM, you can use it with OpenAI, Anthropic, Mistral, Gemma, etc.
- **Any File**: Quivr works with any file, you can use it with PDF, TXT, Markdown, etc and even add your own parsers.
- **Customize your RAG**: Quivr allows you to customize your RAG, add internet search, add tools, etc.
- **Integrations with Megaparse**: Quivr works with [Megaparse](https://github.com/quivrhq/megaparse), so you can ingest your files with Megaparse and use the RAG with Quivr.

>We take care of the RAG so you can focus on your product. Simply install quivr-core and add it to your project. You can now ingest your files and ask questions.*

**We will be improving the RAG and adding more features, stay tuned!**


This is the core of Quivr, the brain of Quivr.com.

<!-- ## Demo Highlight 🎥

https://github.com/quivrhq/quivr/assets/19614572/a6463b73-76c7-4bc0-978d-70562dca71f5 -->

## Getting Started 🚀

You can find everything on the [documentation](https://core.quivr.com/).

### Prerequisites 📋

Ensure you have the following installed:

- Python 3.10 or newer

### 30 seconds Installation 💽


- **Step 1**: Install the package

  

  ```bash
  pip install quivr-core # Check that the installation worked
  ```


- **Step 2**: Create a RAG with 5 lines of code

  ```python
  import tempfile

  from quivr_core import Brain

  if __name__ == "__main__":
      with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as temp_file:
          temp_file.write("Gold is a liquid of blue-like colour.")
          temp_file.flush()

          brain = Brain.from_files(
              name="test_brain",
              file_paths=[temp_file.name],
          )

          answer = brain.ask(
              "what is gold? asnwer in french"
          )
          print("answer:", answer)
  ```
## Configuration

### Workflows

#### Basic RAG

![](docs/docs/workflows/examples/basic_rag.excalidraw.png)


Creating a basic RAG workflow like the one above is simple, here are the steps:


1. Add your API Keys to your environment variables
```python
import os
os.environ["OPENAI_API_KEY"] = "myopenai_apikey"

```
Quivr supports APIs from Anthropic, OpenAI, and Mistral. It also supports local models using Ollama.

1. Create the YAML file ``basic_rag_workflow.yaml`` and copy the following content in it
```yaml
workflow_config:
  name: "standard RAG"
  nodes:
    - name: "START"
      edges: ["filter_history"]

    - name: "filter_history"
      edges: ["rewrite"]

    - name: "rewrite"
      edges: ["retrieve"]

    - name: "retrieve"
      edges: ["generate_rag"]

    - name: "generate_rag" # the name of the last node, from which we want to stream the answer to the user
      edges: ["END"]

# Maximum number of previous conversation iterations
# to include in the context of the answer
max_history: 10

# Reranker configuration
reranker_config:
  # The reranker supplier to use
  supplier: "cohere"

  # The model to use for the reranker for the given supplier
  model: "rerank-multilingual-v3.0"

  # Number of chunks returned by the reranker
  top_n: 5

# Configuration for the LLM
llm_config:

  # maximum number of tokens passed to the LLM to generate the answer
  max_input_tokens: 4000

  # temperature for the LLM
  temperature: 0.7
```

3. Create a Brain with the default configuration
```python
from quivr_core import Brain

brain = Brain.from_files(name = "my smart brain",
                        file_paths = ["./my_first_doc.pdf", "./my_second_doc.txt"],
                        )

```

4. Launch a Chat
```python
brain.print_info()

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from quivr_core.config import RetrievalConfig

config_file_name = "./basic_rag_workflow.yaml"

retrieval_config = RetrievalConfig.from_yaml(config_file_name)

console = Console()
console.print(Panel.fit("Ask your brain !", style="bold magenta"))

while True:
    # Get user input
    question = Prompt.ask("[bold cyan]Question[/bold cyan]")

    # Check if user wants to exit
    if question.lower() == "exit":
        console.print(Panel("Goodbye!", style="bold yellow"))
        break

    answer = brain.ask(question, retrieval_config=retrieval_config)
    # Print the answer with typing effect
    console.print(f"[bold green]Quivr Assistant[/bold green]: {answer.answer}")

    console.print("-" * console.width)

brain.print_info()
```

5. You are now all set up to talk with your brain and test different retrieval strategies by simply changing the configuration file!

## Go further

You can go further with Quivr by adding internet search, adding tools, etc. Check the [documentation](https://core.quivr.com/) for more information.


## Contributors ✨

Thanks go to these wonderful people:
<a href="https://github.com/quivrhq/quivr/graphs/contributors">
<img src="https://contrib.rocks/image?repo=quivrhq/quivr" />
</a>

## Contribute 🤝

Did you get a pull request? Open it, and we'll review it as soon as possible. Check out our project board [here](https://github.com/users/StanGirard/projects/5) to see what we're currently focused on, and feel free to bring your fresh ideas to the table!

- [Open Issues](https://github.com/quivrhq/quivr/issues)
- [Open Pull Requests](https://github.com/quivrhq/quivr/pulls)
- [Good First Issues](https://github.com/quivrhq/quivr/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)

## Partners ❤️

This project would not be possible without the support of our partners. Thank you for your support!


<a href="https://ycombinator.com/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Y_Combinator_logo.svg/1200px-Y_Combinator_logo.svg.png" alt="YCombinator" style="padding: 10px" width="70px">
</a>
<a href="https://www.theodo.fr/">
  <img src="https://avatars.githubusercontent.com/u/332041?s=200&v=4" alt="Theodo" style="padding: 10px" width="70px">
</a>

## License 📄

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details
```

## File: `release-please-config.json`
```json
{
    "packages": {
        "core": {
            "release-type": "python",
            "package-name": "core",
            "bump-patch-for-minor-pre-major": true,
            "include-v-in-tag": false,
            "tag-separator": "-",
            "component": "core"
        }
    }
}
```

## File: `vercel.json`
```json
{
    "git": {
        "deploymentEnabled": {
            "main": false
        }
    }
}
```

## File: `core/.flake8`
```
[flake8]
; Minimal configuration for Flake8 to work with Black.
max-line-length = 100
ignore = E101,E111,E112,E221,E222,E501,E711,E712,W503,W504,F401,E203
```

## File: `core/.gitignore`
```
# python generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# venv
.venv
```

## File: `core/.python-version`
```
3.11.9
```

## File: `core/CHANGELOG.md`
```markdown
# Changelog

## [0.0.33](https://github.com/QuivrHQ/quivr/compare/core-0.0.32...core-0.0.33) (2025-02-03)


### Features

* **zendesk:** add zendesk workflow ([#3586](https://github.com/QuivrHQ/quivr/issues/3586)) ([ee9b7a5](https://github.com/QuivrHQ/quivr/commit/ee9b7a5740825bd3fc9186e0a9179959c6525e5e))


### Bug Fixes

* CLI-24 ([ee9b7a5](https://github.com/QuivrHQ/quivr/commit/ee9b7a5740825bd3fc9186e0a9179959c6525e5e))

## [0.0.32](https://github.com/QuivrHQ/quivr/compare/core-0.0.31...core-0.0.32) (2025-01-31)


### Features

* o3-mini ([#3583](https://github.com/QuivrHQ/quivr/issues/3583)) ([a639e0c](https://github.com/QuivrHQ/quivr/commit/a639e0ce50297e0fefa809b7edb57b50863b446d))

## [0.0.31](https://github.com/QuivrHQ/quivr/compare/core-0.0.30...core-0.0.31) (2025-01-30)


### Features

* cache tokenizers ([#3558](https://github.com/QuivrHQ/quivr/issues/3558)) ([699dc2e](https://github.com/QuivrHQ/quivr/commit/699dc2e187abc9986845f591111723088f5bcefe))
* limit tokenizers cache size ([#3577](https://github.com/QuivrHQ/quivr/issues/3577)) ([e2a3bcb](https://github.com/QuivrHQ/quivr/commit/e2a3bcbbdb469348187d986de9ba3901938bed58))
* remove pympler dependency and add better way to calculate size of tokenizer cache ([#3580](https://github.com/QuivrHQ/quivr/issues/3580)) ([2fbd5d4](https://github.com/QuivrHQ/quivr/commit/2fbd5d48443625dd3fe8a37c04275cd760e7285f))
* remove tokenizer load ([#3576](https://github.com/QuivrHQ/quivr/issues/3576)) ([05e212a](https://github.com/QuivrHQ/quivr/commit/05e212a30929ba3c00e31e3364363eb4a4376ad9))

## [0.0.30](https://github.com/QuivrHQ/quivr/compare/core-0.0.29...core-0.0.30) (2025-01-27)


### Features

* adding cache to LLMEndpoint ([#3555](https://github.com/QuivrHQ/quivr/issues/3555)) ([6072907](https://github.com/QuivrHQ/quivr/commit/6072907ca7370be748d2d6845fd674abbb6c83c3))

## [0.0.29](https://github.com/QuivrHQ/quivr/compare/core-0.0.28...core-0.0.29) (2025-01-20)


### Features

* enabling workflows without rewriting step ([#3549](https://github.com/QuivrHQ/quivr/issues/3549)) ([bbe1c18](https://github.com/QuivrHQ/quivr/commit/bbe1c183768bf32945554e679cab737c07bb3dde))
* improving the prompts to always refer to 'tasks' instead of 'questions' ([#3528](https://github.com/QuivrHQ/quivr/issues/3528)) ([e9c72e1](https://github.com/QuivrHQ/quivr/commit/e9c72e15671407290f1a3a9758bf38a3357d2b15))
* langfuse integration ([#3530](https://github.com/QuivrHQ/quivr/issues/3530)) ([c4aae1a](https://github.com/QuivrHQ/quivr/commit/c4aae1a6c21fd7bc7019676d32fa5b2e8fbbe171))
* langfuse user id ([#3533](https://github.com/QuivrHQ/quivr/issues/3533)) ([e0ccd3d](https://github.com/QuivrHQ/quivr/commit/e0ccd3dc04b7527b27520465b2cf179e9789bf3f))
* language detection after chunking ([#3532](https://github.com/QuivrHQ/quivr/issues/3532)) ([d0adb81](https://github.com/QuivrHQ/quivr/commit/d0adb8112a27fb7f25564d328a6f7e50ba27ba3a))
* returning a description of each workflow node ([#3539](https://github.com/QuivrHQ/quivr/issues/3539)) ([d835fc6](https://github.com/QuivrHQ/quivr/commit/d835fc6e4c062bd485a715bc707a902493e092c2))


### Bug Fixes

* langfuse talk to model ([#3535](https://github.com/QuivrHQ/quivr/issues/3535)) ([9681a9e](https://github.com/QuivrHQ/quivr/commit/9681a9ec8b6b09fe20d04bf41d17a57afc5398f9))

## [0.0.28](https://github.com/QuivrHQ/quivr/compare/core-0.0.27...core-0.0.28) (2024-12-17)


### Features

* remove dependencies on Pydantic v1 ([#3526](https://github.com/QuivrHQ/quivr/issues/3526)) ([ebc4eb8](https://github.com/QuivrHQ/quivr/commit/ebc4eb811c258ce0500032bbc52d96f333fabf89))

## [0.0.27](https://github.com/QuivrHQ/quivr/compare/core-0.0.26...core-0.0.27) (2024-12-16)


### Features

* ensuring that max_context_tokens is never larger than what supported by models ([#3519](https://github.com/QuivrHQ/quivr/issues/3519)) ([d6e0ed4](https://github.com/QuivrHQ/quivr/commit/d6e0ed44df0ee7edafea85f704a15fd99969bafd))
* send all to megaparse_sdk ([#3521](https://github.com/QuivrHQ/quivr/issues/3521)) ([e48044d](https://github.com/QuivrHQ/quivr/commit/e48044d36ffda613f65da24641ed8da290195177))


### Bug Fixes

* fixing errors arising when the user input contains no tasks ([#3525](https://github.com/QuivrHQ/quivr/issues/3525)) ([e28f7bc](https://github.com/QuivrHQ/quivr/commit/e28f7bcb9ab9534bc011664525ae1f9c2cf6393e))

## [0.0.26](https://github.com/QuivrHQ/quivr/compare/core-0.0.25...core-0.0.26) (2024-12-10)


### Features

* first version (V0) of the Workflow Management System ([#3493](https://github.com/QuivrHQ/quivr/issues/3493)) ([6450a49](https://github.com/QuivrHQ/quivr/commit/6450a494e3efa8e8c267ca49aa0a7ec682586b4e))


### Bug Fixes

* dealing with empty tool_calls ([#3514](https://github.com/QuivrHQ/quivr/issues/3514)) ([e2f6389](https://github.com/QuivrHQ/quivr/commit/e2f6389189d911a382b2236ab39f28a1270528ac))

## [0.0.25](https://github.com/QuivrHQ/quivr/compare/core-0.0.24...core-0.0.25) (2024-11-28)


### Bug Fixes

* megaparse sdk with nats ([#3496](https://github.com/QuivrHQ/quivr/issues/3496)) ([e68b4f4](https://github.com/QuivrHQ/quivr/commit/e68b4f45698898f6b514d4779c8e5fd7332f2e67))


### Documentation

* Enhance example/chatbot with added instructions ([#3506](https://github.com/QuivrHQ/quivr/issues/3506)) ([d1d608d](https://github.com/QuivrHQ/quivr/commit/d1d608d19ffb9213910575981eff3527f7d232a0))

## [0.0.24](https://github.com/QuivrHQ/quivr/compare/core-0.0.23...core-0.0.24) (2024-11-14)


### Features

* kms-migration ([#3446](https://github.com/QuivrHQ/quivr/issues/3446)) ([1356d87](https://github.com/QuivrHQ/quivr/commit/1356d87098ae84776a5d47b631d07a1c8e92e291))
* **megaparse:** add sdk ([#3462](https://github.com/QuivrHQ/quivr/issues/3462)) ([190d971](https://github.com/QuivrHQ/quivr/commit/190d971bd71333924b88ba747d3c6a833ca65d92))


### Bug Fixes

* added chunk_size in tika processor ([#3466](https://github.com/QuivrHQ/quivr/issues/3466)) ([063bbd3](https://github.com/QuivrHQ/quivr/commit/063bbd323dfca2dfc22fc5416c1617ed61d2e2ab))
* modify megaparse strategy ([#3474](https://github.com/QuivrHQ/quivr/issues/3474)) ([da97b2c](https://github.com/QuivrHQ/quivr/commit/da97b2cf145c86ed577be698ae837b3dc26f6921))
* supported extensions for megaparse ([#3477](https://github.com/QuivrHQ/quivr/issues/3477)) ([72b979d](https://github.com/QuivrHQ/quivr/commit/72b979d4e4d6e6efc45d47c7aba942eb909adc3e))

## [0.0.23](https://github.com/QuivrHQ/quivr/compare/core-0.0.22...core-0.0.23) (2024-10-31)


### Features

* websearch, tool use, user intent, dynamic retrieval, multiple questions ([#3424](https://github.com/QuivrHQ/quivr/issues/3424)) ([285fe5b](https://github.com/QuivrHQ/quivr/commit/285fe5b96065a19c74f0314557e5840d8722099e))

## [0.0.22](https://github.com/QuivrHQ/quivr/compare/core-0.0.21...core-0.0.22) (2024-10-21)


### Features

* **ask:** non-streaming now calls streaming ([#3409](https://github.com/QuivrHQ/quivr/issues/3409)) ([e71e46b](https://github.com/QuivrHQ/quivr/commit/e71e46bcdfbab0d583aef015604278343fd46c6f))

## [0.0.21](https://github.com/QuivrHQ/quivr/compare/core-0.0.20...core-0.0.21) (2024-10-21)


### Features

* **ci:** trigger ([b92774a](https://github.com/QuivrHQ/quivr/commit/b92774aa37ad2051b197daa29fe4b94d57a19986))

## [0.0.20](https://github.com/QuivrHQ/quivr/compare/core-0.0.19...core-0.0.20) (2024-10-21)


### Features

* **ci:** trigger ([#3403](https://github.com/QuivrHQ/quivr/issues/3403)) ([68c09fc](https://github.com/QuivrHQ/quivr/commit/68c09fce85364432da2641d0a8da867516142553))
* **docs:** trigger ci ([5644596](https://github.com/QuivrHQ/quivr/commit/56445967252eac20d17bebc4484d7c00c45d9238))

## [0.0.19](https://github.com/QuivrHQ/quivr/compare/core-0.0.18...core-0.0.19) (2024-10-21)


### Features

* **quivr-core:** beginning ([#3388](https://github.com/QuivrHQ/quivr/issues/3388)) ([7acb52a](https://github.com/QuivrHQ/quivr/commit/7acb52a9637b74d53f3e4cc9dde4ae1ca3f481ad))

## [0.0.18](https://github.com/QuivrHQ/quivr/compare/core-0.0.17...core-0.0.18) (2024-10-16)


### Bug Fixes

* **core:** megaparse config ([#3384](https://github.com/QuivrHQ/quivr/issues/3384)) ([ffe86ca](https://github.com/QuivrHQ/quivr/commit/ffe86ca7bac3d7800913937314170db6f91daf8e))

## [0.0.17](https://github.com/QuivrHQ/quivr/compare/core-0.0.16...core-0.0.17) (2024-10-16)


### Features

* **assistant:** cdp ([#3305](https://github.com/QuivrHQ/quivr/issues/3305)) ([b767f19](https://github.com/QuivrHQ/quivr/commit/b767f19f28b5478cef077b5d1587bf5195f2a668))
* **assistants:** mock api ([#3195](https://github.com/QuivrHQ/quivr/issues/3195)) ([282fa0e](https://github.com/QuivrHQ/quivr/commit/282fa0e3f83f7c6fc8c84ca95f8f4ced4ed34b78))
* introducing configurable retrieval workflows ([#3227](https://github.com/QuivrHQ/quivr/issues/3227)) ([ef90e8e](https://github.com/QuivrHQ/quivr/commit/ef90e8e672ca23d104c7d5bde7496f0929adf5d2))


### Bug Fixes

* fixing pdf parsing ([#3349](https://github.com/QuivrHQ/quivr/issues/3349)) ([367242a](https://github.com/QuivrHQ/quivr/commit/367242a3d5ea2df1928cb2908ad9e1906d1bba6f))


### Documentation

* **core:** init ([#3365](https://github.com/QuivrHQ/quivr/issues/3365)) ([bb572a2](https://github.com/QuivrHQ/quivr/commit/bb572a2a8d060f147461506aadd38704eb029a9a))
* **fix:** fixed warnings from griffe ([#3381](https://github.com/QuivrHQ/quivr/issues/3381)) ([1a38798](https://github.com/QuivrHQ/quivr/commit/1a3879839a2d9e0881e18cb66809564fb76724ef))

## [0.0.16](https://github.com/QuivrHQ/quivr/compare/core-0.0.15...core-0.0.16) (2024-09-17)


### Bug Fixes

* **core:** enforce langchain &lt;0.3 for pydantic v1 ([#3217](https://github.com/QuivrHQ/quivr/issues/3217)) ([4bb4800](https://github.com/QuivrHQ/quivr/commit/4bb4800a76942ee31a939d3cacc94f057682177a))

## [0.0.15](https://github.com/QuivrHQ/quivr/compare/core-0.0.14...core-0.0.15) (2024-09-16)


### Features

* CRUD KMS (no syncs)  ([#3162](https://github.com/QuivrHQ/quivr/issues/3162)) ([71edca5](https://github.com/QuivrHQ/quivr/commit/71edca572ffd2901ed582005ac4b2803d9d95e57))
* save and load brain ([#3202](https://github.com/QuivrHQ/quivr/issues/3202)) ([eda619f](https://github.com/QuivrHQ/quivr/commit/eda619f4547921ab4c50458b2d44c6b5c10e40d1))


### Bug Fixes

* Update LLMEndpoint to include max_tokens parameter ([#3201](https://github.com/QuivrHQ/quivr/issues/3201)) ([13ed225](https://github.com/QuivrHQ/quivr/commit/13ed225b172407ee9826b9c01b2f7b124a8b5a10))

## [0.0.14](https://github.com/QuivrHQ/quivr/compare/core-0.0.13...core-0.0.14) (2024-09-09)


### Features

* Add brain_id and brain_name to ChatLLMMetadata model ([#2968](https://github.com/QuivrHQ/quivr/issues/2968)) ([1112001](https://github.com/QuivrHQ/quivr/commit/111200184b66dc42d75996c6c286474e9c5f8462))
* add chat with models ([#2933](https://github.com/QuivrHQ/quivr/issues/2933)) ([fccd197](https://github.com/QuivrHQ/quivr/commit/fccd197511d8594db257bfddf757bf0d28f7239d))
* Add get_model method to ModelRepository ([#2949](https://github.com/QuivrHQ/quivr/issues/2949)) ([13e9fc4](https://github.com/QuivrHQ/quivr/commit/13e9fc490bc62264de93d2efddf2389126c147fa))
* **anthropic:** add llm ([#3146](https://github.com/QuivrHQ/quivr/issues/3146)) ([8e29218](https://github.com/QuivrHQ/quivr/commit/8e2921886505cea0e72d2e1136a4b8ba862c3ce1))
* **azure:** quivr compatible with it ([#3005](https://github.com/QuivrHQ/quivr/issues/3005)) ([b5f31a8](https://github.com/QuivrHQ/quivr/commit/b5f31a83d4a1c4432943bbbaa0766c46927ef125))
* **frontend:** talk with models and handle code markdown ([#2980](https://github.com/QuivrHQ/quivr/issues/2980)) ([ef6037e](https://github.com/QuivrHQ/quivr/commit/ef6037e665f8d5e9c513d889773419a25f914d83))
* quivr core 0.1 ([#2970](https://github.com/QuivrHQ/quivr/issues/2970)) ([380cf82](https://github.com/QuivrHQ/quivr/commit/380cf8270678453c3dc14ac8665be9b3b5a49dce))
* using langgraph in our RAG pipeline ([#3130](https://github.com/QuivrHQ/quivr/issues/3130)) ([8cfdf53](https://github.com/QuivrHQ/quivr/commit/8cfdf53fe748b884cf44ade274503de3966b1378))


### Bug Fixes

* **chat:** order of chat history was reversed ([#3148](https://github.com/QuivrHQ/quivr/issues/3148)) ([7209500](https://github.com/QuivrHQ/quivr/commit/7209500d0bdaec544fce1e8e9082de3ead4464f4))

## [0.0.13](https://github.com/QuivrHQ/quivr/compare/core-0.0.12...core-0.0.13) (2024-08-01)


### Features

* quivr core tox test + parsers ([#2929](https://github.com/QuivrHQ/quivr/issues/2929)) ([6855585](https://github.com/QuivrHQ/quivr/commit/685558560cc431054fb9d1330c0e27ce5fdf1806))


### Bug Fixes

* processor quivr version ([#2934](https://github.com/QuivrHQ/quivr/issues/2934)) ([2d64962](https://github.com/QuivrHQ/quivr/commit/2d64962ca407d8f2c9e0faedc457548c3ff9921d))
* quivr core fix tests ([#2935](https://github.com/QuivrHQ/quivr/issues/2935)) ([d9c1f3a](https://github.com/QuivrHQ/quivr/commit/d9c1f3add48f354d92f3a21c03eca53add30a773))

## [0.0.12](https://github.com/QuivrHQ/quivr/compare/core-0.0.11...core-0.0.12) (2024-07-23)


### Features

* **dead-code:** removed composite & api ([#2902](https://github.com/QuivrHQ/quivr/issues/2902)) ([a2721d3](https://github.com/QuivrHQ/quivr/commit/a2721d3926df873e10817f948f8f10894ec6c581))
* **frontend:** add knowledge icon when integration ([#2888](https://github.com/QuivrHQ/quivr/issues/2888)) ([733d083](https://github.com/QuivrHQ/quivr/commit/733d083e330fc6e41c089bb9c9cf76289040cab9))

## [0.0.11](https://github.com/QuivrHQ/quivr/compare/core-0.0.10...core-0.0.11) (2024-07-22)


### Features

* move parsers quivr core ([#2884](https://github.com/QuivrHQ/quivr/issues/2884)) ([d3c53e6](https://github.com/QuivrHQ/quivr/commit/d3c53e63539bade5cbd716edf7e9af68ba15ed08))

## [0.0.10](https://github.com/QuivrHQ/quivr/compare/core-0.0.9...core-0.0.10) (2024-07-19)


### Features

* **frontend:** new notifications design ([#2870](https://github.com/QuivrHQ/quivr/issues/2870)) ([ed97004](https://github.com/QuivrHQ/quivr/commit/ed9700426959f3c1502a882263dfb447411d5381))
* **integrations:** dropbox ([#2864](https://github.com/QuivrHQ/quivr/issues/2864)) ([4806dc5](https://github.com/QuivrHQ/quivr/commit/4806dc5809aec9f7f573cb5adddac0e2d0ba600b))
* quivr core brain info + processors registry +  ([#2877](https://github.com/QuivrHQ/quivr/issues/2877)) ([3001fa1](https://github.com/QuivrHQ/quivr/commit/3001fa1475cf119a8b41a176f735f5402f708738))


### Bug Fixes

* Refacto & update dropbox refresh ([#2875](https://github.com/QuivrHQ/quivr/issues/2875)) ([3b68855](https://github.com/QuivrHQ/quivr/commit/3b68855a83c72f3e31c117af0434330383a8a5d7))

## [0.0.9](https://github.com/QuivrHQ/quivr/compare/core-0.0.8...core-0.0.9) (2024-07-15)


### Features

* quivr api use quivr core ([#2868](https://github.com/QuivrHQ/quivr/issues/2868)) ([9d3e9ed](https://github.com/QuivrHQ/quivr/commit/9d3e9edfd2ef24397458cc6556f6080673be96ae))


### Bug Fixes

* quiv core stream duplicate  and quivr-core rag tests ([#2852](https://github.com/QuivrHQ/quivr/issues/2852)) ([35eb07f](https://github.com/QuivrHQ/quivr/commit/35eb07f7a2664f65e482a78fabf242e1ccb36f07))

## [0.0.8](https://github.com/QuivrHQ/quivr/compare/core-0.0.7...core-0.0.8) (2024-07-11)


### Features

* Add Quivr chatbot example ([#2827](https://github.com/QuivrHQ/quivr/issues/2827)) ([5ff8d4e](https://github.com/QuivrHQ/quivr/commit/5ff8d4ee81cdc5a2cf375a6b7709beb44da2b911))
* Update aiofiles dependency to loosen version control ([#2834](https://github.com/QuivrHQ/quivr/issues/2834)) ([5e75d15](https://github.com/QuivrHQ/quivr/commit/5e75d155976dd710c65f9431e942cdeec9bd6424))

## [0.0.7](https://github.com/QuivrHQ/quivr/compare/core-0.0.6...core-0.0.7) (2024-07-10)


### Bug Fixes

* llm model name ([#2830](https://github.com/QuivrHQ/quivr/issues/2830)) ([71d6cd9](https://github.com/QuivrHQ/quivr/commit/71d6cd9b6b381226a172a09c07a0a084d7efbc22))

## [0.0.6](https://github.com/QuivrHQ/quivr/compare/core-0.0.5...core-0.0.6) (2024-07-10)


### Features

* quivr-core ask streaming ([#2828](https://github.com/QuivrHQ/quivr/issues/2828)) ([0658d49](https://github.com/QuivrHQ/quivr/commit/0658d4947c10f512d2ec2bdcfb70f089ab003a5c))

## [0.0.5](https://github.com/QuivrHQ/quivr/compare/core-0.0.4...core-0.0.5) (2024-07-10)


### Features

* Add GitHub Actions workflow for running tests on backend/core ([#2820](https://github.com/QuivrHQ/quivr/issues/2820)) ([82292f3](https://github.com/QuivrHQ/quivr/commit/82292f30acf982bbf28c1ef928440086fa342a04))
* Add GitHub Actions workflow for running tests on backend/core ([#2822](https://github.com/QuivrHQ/quivr/issues/2822)) ([1566040](https://github.com/QuivrHQ/quivr/commit/15660409a37af8df3c58a3f396614817c9f4641b))
* quivr core chat history ([#2824](https://github.com/QuivrHQ/quivr/issues/2824)) ([847e161](https://github.com/QuivrHQ/quivr/commit/847e161d804421e60eb246f35bf51b7ffd88f3a2))

## [0.0.4](https://github.com/QuivrHQ/quivr/compare/core-0.0.3...core-0.0.4) (2024-07-09)


### Features

* quivr core minimal chat ([#2818](https://github.com/QuivrHQ/quivr/issues/2818)) ([481f24f](https://github.com/QuivrHQ/quivr/commit/481f24f5bed855d044c97eb881512fbf936772f8))

## [0.0.3](https://github.com/QuivrHQ/quivr/compare/core-0.0.2...core-0.0.3) (2024-07-09)


### Bug Fixes

* **pyproject:** fixed to quivr github ([#2816](https://github.com/QuivrHQ/quivr/issues/2816)) ([5a4ac00](https://github.com/QuivrHQ/quivr/commit/5a4ac001d0ba26af0c48aea7d9807c66b5fdd48d))

## [0.0.2](https://github.com/QuivrHQ/quivr/compare/core-v0.0.1...core-0.0.2) (2024-07-09)


### Features

* **backend:** quivr-monorepo and quivr-core package ([#2765](https://github.com/QuivrHQ/quivr/issues/2765)) ([2e75de4](https://github.com/QuivrHQ/quivr/commit/2e75de40390bcc09f25037f19693989841fec70d))
* quivr core minimal chat ([#2803](https://github.com/QuivrHQ/quivr/issues/2803)) ([1dc6d88](https://github.com/QuivrHQ/quivr/commit/1dc6d88f9b8b1b0c1a5682f990bf8098cbd54d77))
```

## File: `core/Dockerfile.test`
```
# Using a slim version for a smaller base image
FROM python:3.11.6-slim-bullseye

# Install GEOS library, Rust, and other dependencies, then clean up
RUN apt-get clean && apt-get update && apt-get install -y \
    curl \
    gcc \
    autoconf \
    automake \
    build-essential \
    # Additional dependencies for document handling
    libmagic-dev \
    tesseract-ocr \
    poppler-utils \
    libreoffice \
    pandoc && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /code

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy the current directory contents into the container at /app
COPY ./pyproject.toml ./poetry.lock* /code/

RUN python3 -m pip install nltk && python3 -c "import nltk; nltk.download('punkt')" \
    && python3 -c "import nltk; nltk.download('averaged_perceptron_tagger')"

# Install project dependencies
RUN poetry install  --with test

ENV PYTHONPATH=/code
```

## File: `core/README.md`
```markdown
# quivr-core package

The RAG of Quivr.com

## License 📄

This project is licensed under the Apache 2.0 License

## Installation

```bash
pip install quivr-core
```




```

## File: `core/pyproject.toml`
```
[project]
name = "quivr-core"
version = "0.0.33"
description = "Quivr core RAG package"
authors = [{ name = "Stan Girard", email = "stan@quivr.app" }]
dependencies = [
    "pydantic>=2.8.2",
    "langchain-core>=0.3,<0.4",
    "langchain>=0.3.9,<0.4",
    "langgraph>=0.2.38,<0.3",
    "httpx>=0.27.0",
    "rich>=13.7.1",
    "tiktoken>=0.7.0",
    "aiofiles>=23.1.0",
    "langchain-openai>=0.3.0",
    "langchain-cohere>=0.1.0",
    "langchain-community>=0.3,<0.4",
    "langchain-anthropic>=0.1.23",
    "types-pyyaml>=6.0.12.20240808",
    "transformers[sentencepiece]>=4.44.2",
    "faiss-cpu>=1.8.0.post1",
    "rapidfuzz>=3.10.1",
    "markupsafe>=2.1.5",
    "megaparse-sdk>=0.1.11",
    "langchain-mistralai>=0.2.3",
    "langchain-google-genai>=2.1.3",
    "fasttext-langdetect>=1.0.5",
    "langfuse>=2.57.0",
    "langchain-groq>=0.3.2",
]
readme = "README.md"
requires-python = ">= 3.11"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.rye]
managed = true
dev-dependencies = [
    "mypy>=1.11.1",
    "pre-commit>=3.8.0",
    "ipykernel>=6.29.5",
    "ruff>=0.6.1",
    "flake8>=7.1.1",
    "flake8-black>=0.3.6",
    "pytest-asyncio>=0.23.8",
    "pytest>=8.3.2",
    "pytest-xdist>=3.6.1",
    "pytest-benchmark>=4.0.0",
]

[tool.hatch.metadata]
allow-direct-references = true

[tool.hatch.build.targets.wheel]
packages = ["quivr_core"]

[tool.pytest.ini_options]
addopts = "--tb=short -ra -v"
filterwarnings = ["ignore::DeprecationWarning"]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "base: these tests require quivr-core with extra `base` to be installed",
    "tika: these tests require a tika server to be running",
    "unstructured: these tests require `unstructured` dependency",
]

[[tool.mypy.overrides]]
module = "yaml"
ignore_missing_imports = true
```

## File: `core/requirements-dev.lock`
```
# generated by rye
# use `rye lock` or `rye sync` to update this lockfile
#
# last locked with the following flags:
#   pre: false
#   features: []
#   all-features: false
#   with-sources: false
#   generate-hashes: false
#   universal: false

-e file:.
aiofiles==24.1.0
    # via quivr-core
aiohappyeyeballs==2.4.3
    # via aiohttp
aiohttp==3.10.10
    # via langchain
    # via langchain-community
aiosignal==1.3.1
    # via aiohttp
annotated-types==0.7.0
    # via pydantic
anthropic==0.40.0
    # via langchain-anthropic
anyio==4.6.2.post1
    # via anthropic
    # via httpx
    # via langfuse
    # via openai
asttokens==2.4.1
    # via stack-data
attrs==24.2.0
    # via aiohttp
backoff==2.2.1
    # via langfuse
black==24.10.0
    # via flake8-black
certifi==2024.8.30
    # via httpcore
    # via httpx
    # via requests
cfgv==3.4.0
    # via pre-commit
charset-normalizer==3.4.0
    # via requests
click==8.1.7
    # via black
cohere==5.11.1
    # via langchain-cohere
comm==0.2.2
    # via ipykernel
dataclasses-json==0.6.7
    # via langchain-community
debugpy==1.8.7
    # via ipykernel
decorator==5.1.1
    # via ipython
defusedxml==0.7.1
    # via langchain-anthropic
distlib==0.3.9
    # via virtualenv
distro==1.9.0
    # via anthropic
    # via openai
execnet==2.1.1
    # via pytest-xdist
executing==2.1.0
    # via stack-data
faiss-cpu==1.9.0
    # via quivr-core
fastavro==1.9.7
    # via cohere
fasttext==0.9.3
    # via fasttext-langdetect
fasttext-langdetect==1.0.5
    # via quivr-core
filelock==3.16.1
    # via huggingface-hub
    # via transformers
    # via virtualenv
flake8==7.1.1
    # via flake8-black
flake8-black==0.3.6
frozenlist==1.4.1
    # via aiohttp
    # via aiosignal
fsspec==2024.9.0
    # via huggingface-hub
greenlet==3.1.1
    # via sqlalchemy
h11==0.14.0
    # via httpcore
httpcore==1.0.6
    # via httpx
httpx==0.27.2
    # via anthropic
    # via cohere
    # via langchain-mistralai
    # via langfuse
    # via langgraph-sdk
    # via langsmith
    # via megaparse-sdk
    # via openai
    # via quivr-core
httpx-sse==0.4.0
    # via cohere
    # via langchain-community
    # via langchain-mistralai
    # via langgraph-sdk
huggingface-hub==0.25.2
    # via tokenizers
    # via transformers
identify==2.6.1
    # via pre-commit
idna==3.10
    # via anyio
    # via httpx
    # via langfuse
    # via requests
    # via yarl
iniconfig==2.0.0
    # via pytest
ipykernel==6.29.5
ipython==8.28.0
    # via ipykernel
jedi==0.19.1
    # via ipython
jiter==0.6.1
    # via anthropic
    # via openai
jsonpatch==1.33
    # via langchain-core
jsonpointer==3.0.0
    # via jsonpatch
jupyter-client==8.6.3
    # via ipykernel
jupyter-core==5.7.2
    # via ipykernel
    # via jupyter-client
langchain==0.3.9
    # via langchain-community
    # via quivr-core
langchain-anthropic==0.3.0
    # via quivr-core
langchain-cohere==0.3.3
    # via quivr-core
langchain-community==0.3.9
    # via langchain-experimental
    # via quivr-core
langchain-core==0.3.33
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-community
    # via langchain-experimental
    # via langchain-mistralai
    # via langchain-openai
    # via langchain-text-splitters
    # via langgraph
    # via langgraph-checkpoint
    # via quivr-core
langchain-experimental==0.3.3
    # via langchain-cohere
langchain-mistralai==0.2.3
    # via quivr-core
langchain-openai==0.3.3
    # via quivr-core
langchain-text-splitters==0.3.2
    # via langchain
langfuse==2.57.0
    # via quivr-core
langgraph==0.2.38
    # via quivr-core
langgraph-checkpoint==2.0.1
    # via langgraph
langgraph-sdk==0.1.33
    # via langgraph
langsmith==0.1.135
    # via langchain
    # via langchain-community
    # via langchain-core
loguru==0.7.2
    # via megaparse-sdk
markdown-it-py==3.0.0
    # via rich
markupsafe==3.0.2
    # via quivr-core
marshmallow==3.22.0
    # via dataclasses-json
matplotlib-inline==0.1.7
    # via ipykernel
    # via ipython
mccabe==0.7.0
    # via flake8
mdurl==0.1.2
    # via markdown-it-py
megaparse-sdk==0.1.10
    # via quivr-core
msgpack==1.1.0
    # via langgraph-checkpoint
multidict==6.1.0
    # via aiohttp
    # via yarl
mypy==1.12.0
mypy-extensions==1.0.0
    # via black
    # via mypy
    # via typing-inspect
nats-py==2.9.0
    # via megaparse-sdk
nest-asyncio==1.6.0
    # via ipykernel
nodeenv==1.9.1
    # via pre-commit
numpy==1.26.4
    # via faiss-cpu
    # via fasttext
    # via langchain
    # via langchain-community
    # via pandas
    # via transformers
openai==1.61.0
    # via langchain-openai
orjson==3.10.7
    # via langgraph-sdk
    # via langsmith
packaging==24.1
    # via black
    # via faiss-cpu
    # via huggingface-hub
    # via ipykernel
    # via langchain-core
    # via langfuse
    # via marshmallow
    # via pytest
    # via transformers
pandas==2.2.3
    # via langchain-cohere
parameterized==0.9.0
    # via cohere
parso==0.8.4
    # via jedi
pathspec==0.12.1
    # via black
pexpect==4.9.0
    # via ipython
platformdirs==4.3.6
    # via black
    # via jupyter-core
    # via virtualenv
pluggy==1.5.0
    # via pytest
pre-commit==4.0.1
prompt-toolkit==3.0.48
    # via ipython
propcache==0.2.0
    # via yarl
protobuf==5.28.2
    # via transformers
psutil==6.1.0
    # via ipykernel
    # via megaparse-sdk
ptyprocess==0.7.0
    # via pexpect
pure-eval==0.2.3
    # via stack-data
py-cpuinfo==9.0.0
    # via pytest-benchmark
pybind11==2.13.6
    # via fasttext
pycodestyle==2.12.1
    # via flake8
pycryptodome==3.21.0
    # via megaparse-sdk
pydantic==2.9.2
    # via anthropic
    # via cohere
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-core
    # via langchain-mistralai
    # via langfuse
    # via langsmith
    # via openai
    # via pydantic-settings
    # via quivr-core
pydantic-core==2.23.4
    # via cohere
    # via pydantic
pydantic-settings==2.6.1
    # via langchain-community
pyflakes==3.2.0
    # via flake8
pygments==2.18.0
    # via ipython
    # via rich
pytest==8.3.3
    # via pytest-asyncio
    # via pytest-benchmark
    # via pytest-xdist
pytest-asyncio==0.24.0
pytest-benchmark==4.0.0
pytest-xdist==3.6.1
python-dateutil==2.8.2
    # via jupyter-client
    # via pandas
python-dotenv==1.0.1
    # via megaparse-sdk
    # via pydantic-settings
pytz==2024.2
    # via pandas
pyyaml==6.0.2
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langchain-core
    # via pre-commit
    # via transformers
pyzmq==26.2.0
    # via ipykernel
    # via jupyter-client
rapidfuzz==3.10.1
    # via quivr-core
regex==2024.9.11
    # via tiktoken
    # via transformers
requests==2.32.3
    # via cohere
    # via fasttext-langdetect
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langfuse
    # via langsmith
    # via requests-toolbelt
    # via tiktoken
    # via transformers
requests-toolbelt==1.0.0
    # via langsmith
rich==13.9.2
    # via quivr-core
ruff==0.6.9
safetensors==0.4.5
    # via transformers
sentencepiece==0.2.0
    # via transformers
setuptools==75.6.0
    # via fasttext
six==1.16.0
    # via asttokens
    # via python-dateutil
sniffio==1.3.1
    # via anthropic
    # via anyio
    # via httpx
    # via openai
sqlalchemy==2.0.36
    # via langchain
    # via langchain-community
stack-data==0.6.3
    # via ipython
tabulate==0.9.0
    # via langchain-cohere
tenacity==8.5.0
    # via langchain
    # via langchain-community
    # via langchain-core
tiktoken==0.8.0
    # via langchain-openai
    # via quivr-core
tokenizers==0.20.1
    # via cohere
    # via langchain-mistralai
    # via transformers
tornado==6.4.1
    # via ipykernel
    # via jupyter-client
tqdm==4.66.5
    # via huggingface-hub
    # via openai
    # via transformers
traitlets==5.14.3
    # via comm
    # via ipykernel
    # via ipython
    # via jupyter-client
    # via jupyter-core
    # via matplotlib-inline
transformers==4.45.2
    # via quivr-core
types-pyyaml==6.0.12.20240917
    # via quivr-core
types-requests==2.32.0.20241016
    # via cohere
typing-extensions==4.12.2
    # via anthropic
    # via cohere
    # via huggingface-hub
    # via ipython
    # via langchain-core
    # via mypy
    # via openai
    # via pydantic
    # via pydantic-core
    # via sqlalchemy
    # via typing-inspect
typing-inspect==0.9.0
    # via dataclasses-json
tzdata==2024.2
    # via pandas
urllib3==2.2.3
    # via requests
    # via types-requests
virtualenv==20.26.6
    # via pre-commit
wcwidth==0.2.13
    # via prompt-toolkit
wrapt==1.17.0
    # via langfuse
yarl==1.15.3
    # via aiohttp
```

## File: `core/requirements.lock`
```
# generated by rye
# use `rye lock` or `rye sync` to update this lockfile
#
# last locked with the following flags:
#   pre: false
#   features: []
#   all-features: false
#   with-sources: false
#   generate-hashes: false
#   universal: false

-e file:.
aiofiles==24.1.0
    # via quivr-core
aiohappyeyeballs==2.4.3
    # via aiohttp
aiohttp==3.10.10
    # via langchain
    # via langchain-community
aiosignal==1.3.1
    # via aiohttp
annotated-types==0.7.0
    # via pydantic
anthropic==0.40.0
    # via langchain-anthropic
anyio==4.6.2.post1
    # via anthropic
    # via httpx
    # via langfuse
    # via openai
attrs==24.2.0
    # via aiohttp
backoff==2.2.1
    # via langfuse
certifi==2024.8.30
    # via httpcore
    # via httpx
    # via requests
charset-normalizer==3.4.0
    # via requests
cohere==5.11.1
    # via langchain-cohere
dataclasses-json==0.6.7
    # via langchain-community
defusedxml==0.7.1
    # via langchain-anthropic
distro==1.9.0
    # via anthropic
    # via openai
faiss-cpu==1.9.0
    # via quivr-core
fastavro==1.9.7
    # via cohere
fasttext==0.9.3
    # via fasttext-langdetect
fasttext-langdetect==1.0.5
    # via quivr-core
filelock==3.16.1
    # via huggingface-hub
    # via transformers
frozenlist==1.4.1
    # via aiohttp
    # via aiosignal
fsspec==2024.9.0
    # via huggingface-hub
greenlet==3.1.1
    # via sqlalchemy
h11==0.14.0
    # via httpcore
httpcore==1.0.6
    # via httpx
httpx==0.27.2
    # via anthropic
    # via cohere
    # via langchain-mistralai
    # via langfuse
    # via langgraph-sdk
    # via langsmith
    # via megaparse-sdk
    # via openai
    # via quivr-core
httpx-sse==0.4.0
    # via cohere
    # via langchain-community
    # via langchain-mistralai
    # via langgraph-sdk
huggingface-hub==0.25.2
    # via tokenizers
    # via transformers
idna==3.10
    # via anyio
    # via httpx
    # via langfuse
    # via requests
    # via yarl
jiter==0.6.1
    # via anthropic
    # via openai
jsonpatch==1.33
    # via langchain-core
jsonpointer==3.0.0
    # via jsonpatch
langchain==0.3.9
    # via langchain-community
    # via quivr-core
langchain-anthropic==0.3.0
    # via quivr-core
langchain-cohere==0.3.3
    # via quivr-core
langchain-community==0.3.9
    # via langchain-experimental
    # via quivr-core
langchain-core==0.3.33
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-community
    # via langchain-experimental
    # via langchain-mistralai
    # via langchain-openai
    # via langchain-text-splitters
    # via langgraph
    # via langgraph-checkpoint
    # via quivr-core
langchain-experimental==0.3.3
    # via langchain-cohere
langchain-mistralai==0.2.3
    # via quivr-core
langchain-openai==0.3.3
    # via quivr-core
langchain-text-splitters==0.3.2
    # via langchain
langfuse==2.57.0
    # via quivr-core
langgraph==0.2.38
    # via quivr-core
langgraph-checkpoint==2.0.1
    # via langgraph
langgraph-sdk==0.1.33
    # via langgraph
langsmith==0.1.135
    # via langchain
    # via langchain-community
    # via langchain-core
loguru==0.7.2
    # via megaparse-sdk
markdown-it-py==3.0.0
    # via rich
markupsafe==3.0.2
    # via quivr-core
marshmallow==3.22.0
    # via dataclasses-json
mdurl==0.1.2
    # via markdown-it-py
megaparse-sdk==0.1.10
    # via quivr-core
msgpack==1.1.0
    # via langgraph-checkpoint
multidict==6.1.0
    # via aiohttp
    # via yarl
mypy-extensions==1.0.0
    # via typing-inspect
nats-py==2.9.0
    # via megaparse-sdk
numpy==1.26.4
    # via faiss-cpu
    # via fasttext
    # via langchain
    # via langchain-community
    # via pandas
    # via transformers
openai==1.61.0
    # via langchain-openai
orjson==3.10.7
    # via langgraph-sdk
    # via langsmith
packaging==24.1
    # via faiss-cpu
    # via huggingface-hub
    # via langchain-core
    # via langfuse
    # via marshmallow
    # via transformers
pandas==2.2.3
    # via langchain-cohere
parameterized==0.9.0
    # via cohere
propcache==0.2.0
    # via yarl
protobuf==5.28.2
    # via transformers
psutil==6.1.0
    # via megaparse-sdk
pybind11==2.13.6
    # via fasttext
pycryptodome==3.21.0
    # via megaparse-sdk
pydantic==2.9.2
    # via anthropic
    # via cohere
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-core
    # via langchain-mistralai
    # via langfuse
    # via langsmith
    # via openai
    # via pydantic-settings
    # via quivr-core
pydantic-core==2.23.4
    # via cohere
    # via pydantic
pydantic-settings==2.6.1
    # via langchain-community
pygments==2.18.0
    # via rich
python-dateutil==2.8.2
    # via pandas
python-dotenv==1.0.1
    # via megaparse-sdk
    # via pydantic-settings
pytz==2024.2
    # via pandas
pyyaml==6.0.2
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langchain-core
    # via transformers
rapidfuzz==3.10.1
    # via quivr-core
regex==2024.9.11
    # via tiktoken
    # via transformers
requests==2.32.3
    # via cohere
    # via fasttext-langdetect
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langfuse
    # via langsmith
    # via requests-toolbelt
    # via tiktoken
    # via transformers
requests-toolbelt==1.0.0
    # via langsmith
rich==13.9.2
    # via quivr-core
safetensors==0.4.5
    # via transformers
sentencepiece==0.2.0
    # via transformers
setuptools==75.6.0
    # via fasttext
six==1.16.0
    # via python-dateutil
sniffio==1.3.1
    # via anthropic
    # via anyio
    # via httpx
    # via openai
sqlalchemy==2.0.36
    # via langchain
    # via langchain-community
tabulate==0.9.0
    # via langchain-cohere
tenacity==8.5.0
    # via langchain
    # via langchain-community
    # via langchain-core
tiktoken==0.8.0
    # via langchain-openai
    # via quivr-core
tokenizers==0.20.1
    # via cohere
    # via langchain-mistralai
    # via transformers
tqdm==4.66.5
    # via huggingface-hub
    # via openai
    # via transformers
transformers==4.45.2
    # via quivr-core
types-pyyaml==6.0.12.20240917
    # via quivr-core
types-requests==2.32.0.20241016
    # via cohere
typing-extensions==4.12.2
    # via anthropic
    # via cohere
    # via huggingface-hub
    # via langchain-core
    # via openai
    # via pydantic
    # via pydantic-core
    # via sqlalchemy
    # via typing-inspect
typing-inspect==0.9.0
    # via dataclasses-json
tzdata==2024.2
    # via pandas
urllib3==2.2.3
    # via requests
    # via types-requests
wrapt==1.17.0
    # via langfuse
yarl==1.15.3
    # via aiohttp
```

## File: `core/tox.ini`
```
[tox]
isolated_build = True
skipsdist = true
envlist =
  py311
  py311-base
  py311-unstructured
  py311-pdf


[testenv:py311]
allowlist_externals =
    poetry
commands_pre =
    poetry install --no-root --with test
commands =
    poetry run pytest tests/ -m "not base"  \
        --ignore=./tests/processor/epub \
        --ignore=./tests/processor/docx \
        --ignore=./tests/processor/odt \
        --ignore=./tests/processor/pdf  \
        --ignore=tests/processor/community

[testenv:py311-base]
allowlist_externals =
    poetry
commands_pre =
    poetry install --no-root --with test -E base
commands =
    poetry run pytest tests/ -m base  \
        --ignore=./tests/processor/epub \
        --ignore=./tests/processor/docx \
        --ignore=./tests/processor/odt \
        --ignore=./tests/processor/pdf \
        --ignore=tests/processor/community

[testenv:py311-unstructured]
allowlist_externals =
    poetry
commands_pre =
    poetry install --no-root \
                -E csv \
                -E md \
                -E ipynb \
                -E epub \
                -E odt \
                -E docx \
                -E pptx \
                -E xlsx \
                --with test
commands =
    poetry run pytest \
        tests/processor/epub \
        tests/processor/docx \
        tests/processor/docx \
        tests/processor/odt \
        tests/processor/community


[testenv:py311-pdf]
allowlist_externals =
    poetry
commands_pre =
    poetry install --no-root -E pdf --with test
commands =
    poetry run pytest tests/processor/pdf
```

## File: `core/example_workflows/talk_to_file_rag_config_workflow.yaml`
```yaml
{
  "max_files": 20,
  "llm_config": { "temperature": 0.3, "max_context_tokens": 20000 },
  "max_history": 10,
  "reranker_config":
    { "model": "rerank-v3.5", "top_n": 10, "supplier": "cohere" },
  "workflow_config":
    {
      "name": "Standard RAG",
      "nodes":
        [
          {
            "name": "START",
            "edges": ["filter_history"],
            "description": "Starting workflow",
          },
          {
            "name": "filter_history",
            "edges": ["retrieve"],
            "description": "Filtering history",
          },
          {
            "name": "retrieve",
            "edges": ["retrieve_full_documents_context"],
            "description": "Retrieving relevant information",
          },
          {
            "name": "retrieve_full_documents_context",
            "edges": ["generate_zendesk_rag"],
            "description": "Retrieving full tickets context",
          },
          {
            "name": "generate_zendesk_rag",
            "edges": ["END"],
            "description": "Generating answer",
          },
        ],
    },
}
```

## File: `core/quivr_core/__init__.py`
```python
from importlib.metadata import entry_points

from .brain import Brain
from .processor.registry import register_processor, registry

__all__ = ["Brain", "registry", "register_processor"]


def register_entries():
    if entry_points is not None:
        try:
            eps = entry_points()
        except TypeError:
            pass  # importlib-metadata < 0.8
        else:
            if hasattr(eps, "select"):  # Python 3.10+ / importlib_metadata >= 3.9.0
                processors = eps.select(group="quivr_core.processor")
            else:
                processors = eps.get("quivr_core.processor", [])
            registered_names = set()
            for spec in processors:
                err_msg = f"Unable to load processor from {spec}"
                name = spec.name
                if name in registered_names:
                    continue
                registered_names.add(name)
                register_processor(
                    name,
                    spec.value.replace(":", "."),
                    errtxt=err_msg,
                    append=True,
                )


register_entries()
```

## File: `core/quivr_core/base_config.py`
```python
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict
from typing import Self


class QuivrBaseConfig(BaseModel):
    """
    Base configuration class for Quivr.

    This class extends Pydantic's BaseModel and provides a foundation for
    configuration management in quivr-core.

    Attributes:
        model_config (ConfigDict): Configuration for the Pydantic model.
            It's set to forbid extra attributes, ensuring strict adherence
            to the defined schema.

    Class Methods:
        from_yaml: Create an instance of the class from a YAML file.
    """

    model_config = ConfigDict(extra="forbid")

    @classmethod
    def from_yaml(cls, file_path: str | Path) -> Self:
        """
        Create an instance of the class from a YAML file.

        Args:
            file_path (str | Path): The path to the YAML file.

        Returns:
            QuivrBaseConfig: An instance of the class initialized with the data from the YAML file.
        """
        # Load the YAML file
        with open(file_path, "r") as stream:
            config_data = yaml.safe_load(stream)

        # Instantiate the class using the YAML data
        return cls(**config_data)
```

## File: `core/quivr_core/config.py`
```python
from enum import Enum

import yaml
from pydantic import BaseModel


class ParserType(str, Enum):
    """Parser type enumeration."""

    UNSTRUCTURED = "unstructured"
    LLAMA_PARSER = "llama_parser"
    MEGAPARSE_VISION = "megaparse_vision"


class StrategyEnum(str, Enum):
    """Method to use for the conversion"""

    FAST = "fast"
    AUTO = "auto"
    HI_RES = "hi_res"


class MegaparseBaseConfig(BaseModel):
    @classmethod
    def from_yaml(cls, file_path: str):
        # Load the YAML file
        with open(file_path, "r") as stream:
            config_data = yaml.safe_load(stream)

        # Instantiate the class using the YAML data
        return cls(**config_data)


class MegaparseConfig(MegaparseBaseConfig):
    method: ParserType = ParserType.UNSTRUCTURED
    strategy: StrategyEnum = StrategyEnum.FAST
    check_table: bool = False
    parsing_instruction: str | None = None
    model_name: str = "gpt-4o"
```

## File: `core/quivr_core/brain/__init__.py`
```python
from .brain import Brain

__all__ = ["Brain"]
```

## File: `core/quivr_core/brain/brain.py`
```python
import asyncio
import logging
import os
from pathlib import Path
from pprint import PrettyPrinter
from typing import Any, AsyncGenerator, Callable, Dict, Self, Type, Union
from uuid import UUID, uuid4

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.vectorstores import VectorStore
from langchain_openai import OpenAIEmbeddings
from rich.console import Console
from rich.panel import Panel

from quivr_core.brain.info import BrainInfo, ChatHistoryInfo
from quivr_core.brain.serialization import (
    BrainSerialized,
    EmbedderConfig,
    FAISSConfig,
    LocalStorageConfig,
    TransparentStorageConfig,
)
from quivr_core.files.file import load_qfile
from quivr_core.llm import LLMEndpoint
from quivr_core.processor.registry import get_processor_class
from quivr_core.rag.entities.chat import ChatHistory
from quivr_core.rag.entities.config import RetrievalConfig
from quivr_core.rag.entities.models import (
    LangchainMetadata,
    ParsedRAGChunkResponse,
    ParsedRAGResponse,
    QuivrKnowledge,
    SearchResult,
)
from quivr_core.rag.quivr_rag import QuivrQARAG
from quivr_core.rag.quivr_rag_langgraph import QuivrQARAGLangGraph
from quivr_core.storage.local_storage import LocalStorage, TransparentStorage
from quivr_core.storage.storage_base import StorageBase

from .brain_defaults import build_default_vectordb, default_embedder, default_llm

logger = logging.getLogger("quivr_core")


async def process_files(
    storage: StorageBase, skip_file_error: bool, **processor_kwargs: dict[str, Any]
) -> list[Document]:
    """
    Process files in storage.
    This function takes a StorageBase and return a list of langchain documents.
    Args:
        storage (StorageBase): The storage containing the files to process.
        skip_file_error (bool): Whether to skip files that cannot be processed.
        processor_kwargs (dict[str, Any]): Additional arguments for the processor.
    Returns:
        list[Document]: List of processed documents in the Langchain Document format.
    Raises:
        ValueError: If a file cannot be processed and skip_file_error is False.
        Exception: If no processor is found for a file of a specific type and skip_file_error is False.
    """

    knowledge = []
    for file in await storage.get_files():
        try:
            if file.file_extension:
                processor_cls = get_processor_class(file.file_extension)
                logger.debug(f"processing {file} using class {processor_cls.__name__}")
                processor = processor_cls(**processor_kwargs)
                docs = await processor.process_file(file)
                knowledge.extend(docs)
            else:
                logger.error(f"can't find processor for {file}")
                if skip_file_error:
                    continue
                else:
                    raise ValueError(f"can't parse {file}. can't find file extension")
        except KeyError as e:
            if skip_file_error:
                continue
            else:
                raise Exception(f"Can't parse {file}. No available processor") from e

    return knowledge


class Brain:
    """
    A class representing a Brain.
    This class allows for the creation of a Brain, which is a collection of knowledge one wants to retrieve information from.
    A Brain is set to:
    * Store files in the storage of your choice (local, S3, etc.)
    * Process the files in the storage to extract text and metadata in a wide range of format.
    * Store the processed files in the vector store of your choice (FAISS, PGVector, etc.) - default to FAISS.
    * Create an index of the processed files.
    * Use the *Quivr* workflow for the retrieval augmented generation.
    A Brain is able to:
    * Search for information in the vector store.
    * Answer questions about the knowledges in the Brain.
    * Stream the answer to the question.
    Attributes:
        name (str): The name of the brain.
        id (UUID): The unique identifier of the brain.
        storage (StorageBase): The storage used to store the files.
        llm (LLMEndpoint): The language model used to generate the answer.
        vector_db (VectorStore): The vector store used to store the processed files.
        embedder (Embeddings): The embeddings used to create the index of the processed files.
    """

    def __init__(
        self,
        *,
        name: str,
        llm: LLMEndpoint,
        id: UUID | None = None,
        vector_db: VectorStore | None = None,
        embedder: Embeddings | None = None,
        storage: StorageBase | None = None,
        workspace_id: UUID | None = None,
        chat_id: UUID | None = None,
    ):
        self.id = id
        self.name = name
        self.storage = storage
        self.workspace_id = workspace_id
        self.chat_id = chat_id
        # Chat history
        self._chats = self._init_chats()
        self.default_chat = list(self._chats.values())[0]

        # RAG dependencies:
        self.llm = llm
        self.vector_db = vector_db
        self.embedder = embedder

    def __repr__(self) -> str:
        pp = PrettyPrinter(width=80, depth=None, compact=False, sort_dicts=False)
        return pp.pformat(self.info())

    def print_info(self):
        console = Console()
        tree = self.info().to_tree()
        panel = Panel(tree, title="Brain Info", expand=False, border_style="bold")
        console.print(panel)

    @classmethod
    def load(cls, folder_path: str | Path) -> Self:
        """
        Load a brain from a folder path.
        Args:
            folder_path (str | Path): The path to the folder containing the brain.
        Returns:
            Brain: The brain loaded from the folder path.
        Example:
        ```python
        brain_loaded = Brain.load("path/to/brain")
        brain_loaded.print_info()
        ```
        """
        if isinstance(folder_path, str):
            folder_path = Path(folder_path)
        if not folder_path.exists():
            raise ValueError(f"path {folder_path} doesn't exist")

        # Load brainserialized
        with open(os.path.join(folder_path, "config.json"), "r") as f:
            bserialized = BrainSerialized.model_validate_json(f.read())

        storage: StorageBase | None = None
        # Loading storage
        if bserialized.storage_config.storage_type == "transparent_storage":
            storage = TransparentStorage.load(bserialized.storage_config)
        elif bserialized.storage_config.storage_type == "local_storage":
            storage = LocalStorage.load(bserialized.storage_config)
        else:
            raise ValueError("unknown storage")

        # Load Embedder
        if bserialized.embedding_config.embedder_type == "openai_embedding":
            from langchain_openai import OpenAIEmbeddings

            embedder = OpenAIEmbeddings(**bserialized.embedding_config.config)
        else:
            raise ValueError("unknown embedder")

        # Load vector db
        if bserialized.vectordb_config.vectordb_type == "faiss":
            from langchain_community.vectorstores import FAISS

            vector_db = FAISS.load_local(
                folder_path=bserialized.vectordb_config.vectordb_folder_path,
                embeddings=embedder,
                allow_dangerous_deserialization=True,
            )
        else:
            raise ValueError("Unsupported vectordb")

        return cls(
            id=bserialized.id,
            name=bserialized.name,
            embedder=embedder,
            llm=LLMEndpoint.from_config(bserialized.llm_config),
            storage=storage,
            vector_db=vector_db,
        )

    async def save(self, folder_path: str | Path):
        """
        Save the brain to a folder path.
        Args:
            folder_path (str | Path): The path to the folder where the brain will be saved.
        Returns:
            str: The path to the folder where the brain was saved.
        Example:
        ```python
        await brain.save("path/to/brain")
        ```
        """
        if isinstance(folder_path, str):
            folder_path = Path(folder_path)

        brain_path = os.path.join(folder_path, f"brain_{self.id}")
        os.makedirs(brain_path, exist_ok=True)

        from langchain_community.vectorstores import FAISS

        if isinstance(self.vector_db, FAISS):
            vectordb_path = os.path.join(brain_path, "vector_store")
            os.makedirs(vectordb_path, exist_ok=True)
            self.vector_db.save_local(folder_path=vectordb_path)
            vector_store = FAISSConfig(vectordb_folder_path=vectordb_path)
        else:
            raise Exception("can't serialize other vector stores for now")

        if isinstance(self.embedder, OpenAIEmbeddings):
            embedder_config = EmbedderConfig(
                config=self.embedder.dict(exclude={"openai_api_key"})
            )
        else:
            raise Exception("can't serialize embedder other than openai for now")

        storage_config: Union[LocalStorageConfig, TransparentStorageConfig]
        # TODO : each instance should know how to serialize/deserialize itself
        if isinstance(self.storage, LocalStorage):
            serialized_files = {
                f.id: f.serialize() for f in await self.storage.get_files()
            }
            storage_config = LocalStorageConfig(
                storage_path=self.storage.dir_path, files=serialized_files
            )
        elif isinstance(self.storage, TransparentStorage):
            serialized_files = {
                f.id: f.serialize() for f in await self.storage.get_files()
            }
            storage_config = TransparentStorageConfig(files=serialized_files)
        else:
            raise Exception("can't serialize storage. not supported for now")

        bserialized = BrainSerialized(
            id=self.id,
            name=self.name,
            chat_history=self.chat_history.get_chat_history(),
            llm_config=self.llm.get_config(),
            vectordb_config=vector_store,
            embedding_config=embedder_config,
            storage_config=storage_config,
        )

        with open(os.path.join(brain_path, "config.json"), "w") as f:
            f.write(bserialized.model_dump_json())
        return brain_path

    def info(self) -> BrainInfo:
        # TODO: dim of embedding
        # "embedder": {},
        chats_info = ChatHistoryInfo(
            nb_chats=len(self._chats),
            current_default_chat=self.default_chat.id,
            current_chat_history_length=len(self.default_chat),
        )

        return BrainInfo(
            brain_id=self.id,
            brain_name=self.name,
            files_info=self.storage.info() if self.storage else None,
            chats_info=chats_info,
            llm_info=self.llm.info(),
        )

    @property
    def chat_history(self) -> ChatHistory:
        return self.default_chat

    def _init_chats(self) -> Dict[UUID, ChatHistory]:
        chat_id = uuid4()
        default_chat = ChatHistory(chat_id=chat_id, brain_id=self.id)
        return {chat_id: default_chat}

    @classmethod
    async def afrom_files(
        cls,
        *,
        name: str,
        file_paths: list[str | Path],
        vector_db: VectorStore | None = None,
        storage: StorageBase = TransparentStorage(),
        llm: LLMEndpoint | None = None,
        embedder: Embeddings | None = None,
        skip_file_error: bool = False,
        processor_kwargs: dict[str, Any] | None = None,
    ):
        """
        Create a brain from a list of file paths.
        Args:
            name (str): The name of the brain.
            file_paths (list[str | Path]): The list of file paths to add to the brain.
            vector_db (VectorStore | None): The vector store used to store the processed files.
            storage (StorageBase): The storage used to store the files.
            llm (LLMEndpoint | None): The language model used to generate the answer.
            embedder (Embeddings | None): The embeddings used to create the index of the processed files.
            skip_file_error (bool): Whether to skip files that cannot be processed.
            processor_kwargs (dict[str, Any] | None): Additional arguments for the processor.
        Returns:
            Brain: The brain created from the file paths.
        Example:
        ```python
        brain = await Brain.afrom_files(name="My Brain", file_paths=["file1.pdf", "file2.pdf"])
        brain.print_info()
        ```
        """
        if llm is None:
            llm = default_llm()

        if embedder is None:
            embedder = default_embedder()

        processor_kwargs = processor_kwargs or {}

        brain_id = uuid4()

        # TODO: run in parallel using tasks

        for path in file_paths:
            file = await load_qfile(brain_id, path)
            await storage.upload_file(file)

        logger.debug(f"uploaded all files to {storage}")

        # Parse files
        docs = await process_files(
            storage=storage,
            skip_file_error=skip_file_error,
            **processor_kwargs,
        )

        # Building brain's vectordb
        if vector_db is None:
            vector_db = await build_default_vectordb(docs, embedder)
        else:
            await vector_db.aadd_documents(docs)

        logger.debug(f"added {len(docs)} chunks to vectordb")

        return cls(
            id=brain_id,
            name=name,
            storage=storage,
            llm=llm,
            embedder=embedder,
            vector_db=vector_db,
        )

    @classmethod
    def from_files(
        cls,
        *,
        name: str,
        file_paths: list[str | Path],
        vector_db: VectorStore | None = None,
        storage: StorageBase = TransparentStorage(),
        llm: LLMEndpoint | None = None,
        embedder: Embeddings | None = None,
        skip_file_error: bool = False,
        processor_kwargs: dict[str, Any] | None = None,
    ) -> Self:
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(
            cls.afrom_files(
                name=name,
                file_paths=file_paths,
                vector_db=vector_db,
                storage=storage,
                llm=llm,
                embedder=embedder,
                skip_file_error=skip_file_error,
                processor_kwargs=processor_kwargs,
            )
        )

    @classmethod
    async def afrom_langchain_documents(
        cls,
        *,
        name: str,
        langchain_documents: list[Document],
        vector_db: VectorStore | None = None,
        storage: StorageBase = TransparentStorage(),
        llm: LLMEndpoint | None = None,
        embedder: Embeddings | None = None,
    ) -> Self:
        """
        Create a brain from a list of langchain documents.
        Args:
            name (str): The name of the brain.
            langchain_documents (list[Document]): The list of langchain documents to add to the brain.
            vector_db (VectorStore | None): The vector store used to store the processed files.
            storage (StorageBase): The storage used to store the files.
            llm (LLMEndpoint | None): The language model used to generate the answer.
            embedder (Embeddings | None): The embeddings used to create the index of the processed files.
        Returns:
            Brain: The brain created from the langchain documents.
        Example:
        ```python
        from langchain_core.documents import Document
        documents = [Document(page_content="Hello, world!")]
        brain = await Brain.afrom_langchain_documents(name="My Brain", langchain_documents=documents)
        brain.print_info()
        ```
        """

        if llm is None:
            llm = default_llm()

        if embedder is None:
            embedder = default_embedder()

        brain_id = uuid4()

        # Building brain's vectordb
        if vector_db is None:
            vector_db = await build_default_vectordb(langchain_documents, embedder)
        else:
            await vector_db.aadd_documents(langchain_documents)

        return cls(
            id=brain_id,
            name=name,
            storage=storage,
            llm=llm,
            embedder=embedder,
            vector_db=vector_db,
        )

    async def asearch(
        self,
        query: str | Document,
        n_results: int = 5,
        filter: Callable | Dict[str, Any] | None = None,
        fetch_n_neighbors: int = 20,
    ) -> list[SearchResult]:
        """
        Search for relevant documents in the brain based on a query.
        Args:
            query (str | Document): The query to search for.
            n_results (int): The number of results to return.
            filter (Callable | Dict[str, Any] | None): The filter to apply to the search.
            fetch_n_neighbors (int): The number of neighbors to fetch.
        Returns:
            list[SearchResult]: The list of retrieved chunks.
        Example:
        ```python
        brain = Brain.from_files(name="My Brain", file_paths=["file1.pdf", "file2.pdf"])
        results = await brain.asearch("Why everybody loves Quivr?")
        for result in results:
            print(result.chunk.page_content)
        ```
        """
        if not self.vector_db:
            raise ValueError("No vector db configured for this brain")

        result = await self.vector_db.asimilarity_search_with_score(
            query, k=n_results, filter=filter, fetch_k=fetch_n_neighbors
        )

        return [SearchResult(chunk=d, distance=s) for d, s in result]

    def get_chat_history(self, chat_id: UUID):
        return self._chats[chat_id]

    # TODO(@aminediro)
    def add_file(self) -> None:
        # add it to storage
        # add it to vectorstore
        raise NotImplementedError

    async def ask_streaming(
        self,
        question: str,
        run_id: UUID,
        system_prompt: str | None = None,
        retrieval_config: RetrievalConfig | None = None,
        rag_pipeline: Type[Union[QuivrQARAG, QuivrQARAGLangGraph]] | None = None,
        list_files: list[QuivrKnowledge] | None = None,
        chat_history: ChatHistory | None = None,
        **input_kwargs,
    ) -> AsyncGenerator[ParsedRAGChunkResponse, ParsedRAGChunkResponse]:
        """
        Ask a question to the brain and get a streamed generated answer.
        Args:
            question (str): The question to ask.
            retrieval_config (RetrievalConfig | None): The retrieval configuration (see RetrievalConfig docs).
            rag_pipeline (Type[Union[QuivrQARAG, QuivrQARAGLangGraph]] | None): The RAG pipeline to use.
        list_files (list[QuivrKnowledge] | None): The list of files to include in the RAG pipeline.
            chat_history (ChatHistory | None): The chat history to use.
        Returns:
            AsyncGenerator[ParsedRAGChunkResponse, ParsedRAGChunkResponse]: The streamed generated answer.
        Example:
        ```python
        brain = Brain.from_files(name="My Brain", file_paths=["file1.pdf", "file2.pdf"])
        async for chunk in brain.ask_streaming("What is the meaning of life?"):
            print(chunk.answer)
        ```
        """
        llm = self.llm

        # If you passed a different llm model we'll override the brain  one
        if retrieval_config:
            if retrieval_config.llm_config != self.llm.get_config():
                llm = LLMEndpoint.from_config(config=retrieval_config.llm_config)
        else:
            retrieval_config = RetrievalConfig(llm_config=self.llm.get_config())

        rag_instance = QuivrQARAGLangGraph(
            retrieval_config=retrieval_config, llm=llm, vector_store=self.vector_db
        )

        chat_history = self.default_chat if chat_history is None else chat_history
        list_files = [] if list_files is None else list_files

        full_answer = ""

        metadata = LangchainMetadata(
            langfuse_trace_id=str(run_id),
            langfuse_user_id=str(self.workspace_id),
            langfuse_session_id=str(self.chat_id),
        )

        async for response in rag_instance.answer_astream(
            run_id=run_id,
            question=question,
            system_prompt=system_prompt or None,
            history=chat_history,
            list_files=list_files,
            metadata=metadata,
            **input_kwargs,
        ):
            # Format output to be correct servicedf;j
            if not response.last_chunk:
                yield response
            full_answer += response.answer

        # TODO : add sources, metdata etc  ...
        chat_history.append(HumanMessage(content=question))
        chat_history.append(AIMessage(content=full_answer))
        yield response

    async def aask(
        self,
        run_id: UUID,
        question: str,
        system_prompt: str | None = None,
        retrieval_config: RetrievalConfig | None = None,
        rag_pipeline: Type[Union[QuivrQARAG, QuivrQARAGLangGraph]] | None = None,
        list_files: list[QuivrKnowledge] | None = None,
        chat_history: ChatHistory | None = None,
        **input_kwargs,
    ) -> ParsedRAGResponse:
        """
        Synchronous version that asks a question to the brain and gets a generated answer.
        Args:
            question (str): The question to ask.
            retrieval_config (RetrievalConfig | None): The retrieval configuration (see RetrievalConfig docs).
            rag_pipeline (Type[Union[QuivrQARAG, QuivrQARAGLangGraph]] | None): The RAG pipeline to use.
            list_files (list[QuivrKnowledge] | None): The list of files to include in the RAG pipeline.
            chat_history (ChatHistory | None): The chat history to use.
        Returns:
            ParsedRAGResponse: The generated answer.
        """
        # question_language = detect_language(question) -- Commented until we use it
        full_answer = ""
        metadata = None

        async for response in self.ask_streaming(
            run_id=run_id,
            question=question,
            system_prompt=system_prompt,
            retrieval_config=retrieval_config,
            rag_pipeline=rag_pipeline,
            list_files=list_files,
            chat_history=chat_history,
            **input_kwargs,
        ):
            full_answer += response.answer
            if response.metadata:
                metadata = response.metadata

        return ParsedRAGResponse(answer=full_answer, metadata=metadata)

    def ask(
        self,
        run_id: UUID,
        question: str,
        system_prompt: str | None = None,
        retrieval_config: RetrievalConfig | None = None,
        rag_pipeline: Type[Union[QuivrQARAG, QuivrQARAGLangGraph]] | None = None,
        list_files: list[QuivrKnowledge] | None = None,
        chat_history: ChatHistory | None = None,
    ) -> ParsedRAGResponse:
        """
        Fully synchronous version that asks a question to the brain and gets a generated answer.
        Args:
            question (str): The question to ask.
            system_prompt (str | None): The system prompt to use.
            retrieval_config (RetrievalConfig | None): The retrieval configuration (see RetrievalConfig docs).
            rag_pipeline (Type[Union[QuivrQARAG, QuivrQARAGLangGraph]] | None): The RAG pipeline to use.
            list_files (list[QuivrKnowledge] | None): The list of files to include in the RAG pipeline.
            chat_history (ChatHistory | None): The chat history to use.
        Returns:
            ParsedRAGResponse: The generated answer.
        """
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(
            self.aask(
                run_id=run_id,
                question=question,
                system_prompt=system_prompt,
                retrieval_config=retrieval_config,
                rag_pipeline=rag_pipeline,
                list_files=list_files,
                chat_history=chat_history,
            )
        )
```

## File: `core/quivr_core/brain/brain_defaults.py`
```python
import logging

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore

from quivr_core.rag.entities.config import DefaultModelSuppliers, LLMEndpointConfig
from quivr_core.llm import LLMEndpoint

logger = logging.getLogger("quivr_core")


async def build_default_vectordb(
    docs: list[Document], embedder: Embeddings
) -> VectorStore:
    try:
        from langchain_community.vectorstores import FAISS

        logger.debug("Using Faiss-CPU as vector store.")
        # TODO(@aminediro) : embedding call is usually not concurrent for all documents but waits
        if len(docs) > 0:
            vector_db = await FAISS.afrom_documents(documents=docs, embedding=embedder)
            return vector_db
        else:
            raise ValueError("can't initialize brain without documents")

    except ImportError as e:
        raise ImportError(
            "Please provide a valid vector store or install quivr-core['base'] package for using the default one."
        ) from e


def default_embedder() -> Embeddings:
    try:
        from langchain_openai import OpenAIEmbeddings

        logger.debug("Loaded OpenAIEmbeddings as default LLM for brain")
        embedder = OpenAIEmbeddings()
        return embedder
    except ImportError as e:
        raise ImportError(
            "Please provide a valid Embedder or install quivr-core['base'] package for using the defaultone."
        ) from e


def default_llm() -> LLMEndpoint:
    try:
        logger.debug("Loaded ChatOpenAI as default LLM for brain")
        llm = LLMEndpoint.from_config(
            LLMEndpointConfig(supplier=DefaultModelSuppliers.OPENAI, model="gpt-4o")
        )
        return llm

    except ImportError as e:
        raise ImportError(
            "Please provide a valid BaseLLM or install quivr-core['base'] package"
        ) from e
```

## File: `core/quivr_core/brain/info.py`
```python
from dataclasses import dataclass
from uuid import UUID

from rich.tree import Tree


@dataclass
class ChatHistoryInfo:
    nb_chats: int
    current_default_chat: UUID
    current_chat_history_length: int

    def add_to_tree(self, chats_tree: Tree):
        chats_tree.add(f"Number of Chats: [bold]{self.nb_chats}[/bold]")
        chats_tree.add(
            f"Current Default Chat: [bold magenta]{self.current_default_chat}[/bold magenta]"
        )
        chats_tree.add(
            f"Current Chat History Length: [bold]{self.current_chat_history_length}[/bold]"
        )


@dataclass
class LLMInfo:
    model: str
    llm_base_url: str
    temperature: float
    max_tokens: int
    supports_function_calling: int

    def add_to_tree(self, llm_tree: Tree):
        llm_tree.add(f"Model: [italic]{self.model}[/italic]")
        llm_tree.add(f"Base URL: [underline]{self.llm_base_url}[/underline]")
        llm_tree.add(f"Temperature: [bold]{self.temperature}[/bold]")
        llm_tree.add(f"Max Tokens: [bold]{self.max_tokens}[/bold]")
        func_call_color = "green" if self.supports_function_calling else "red"
        llm_tree.add(
            f"Supports Function Calling: [bold {func_call_color}]{self.supports_function_calling}[/bold {func_call_color}]"
        )


@dataclass
class StorageInfo:
    storage_type: str
    n_files: int

    def add_to_tree(self, files_tree: Tree):
        files_tree.add(f"Storage Type: [italic]{self.storage_type}[/italic]")
        files_tree.add(f"Number of Files: [bold]{self.n_files}[/bold]")


@dataclass
class BrainInfo:
    brain_id: UUID
    brain_name: str
    chats_info: ChatHistoryInfo
    llm_info: LLMInfo
    files_info: StorageInfo | None = None

    def to_tree(self):
        tree = Tree("📊 Brain Information")
        tree.add(f"🆔 ID: [bold cyan]{self.brain_id}[/bold cyan]")
        tree.add(f"🧠 Brain Name: [bold green]{self.brain_name}[/bold green]")

        if self.files_info:
            files_tree = tree.add("📁 Files")
            self.files_info.add_to_tree(files_tree)

        chats_tree = tree.add("💬 Chats")
        self.chats_info.add_to_tree(chats_tree)

        llm_tree = tree.add("🤖 LLM")
        self.llm_info.add_to_tree(llm_tree)
        return tree
```

## File: `core/quivr_core/brain/serialization.py`
```python
from pathlib import Path
from typing import Any, Dict, Literal, Union
from uuid import UUID

from pydantic import BaseModel, Field, SecretStr

from quivr_core.rag.entities.config import LLMEndpointConfig
from quivr_core.rag.entities.models import ChatMessage
from quivr_core.files.file import QuivrFileSerialized


class EmbedderConfig(BaseModel):
    embedder_type: Literal["openai_embedding"] = "openai_embedding"
    # TODO: type this correctly
    config: Dict[str, Any]


class PGVectorConfig(BaseModel):
    vectordb_type: Literal["pgvector"] = "pgvector"
    pg_url: str
    pg_user: str
    pg_psswd: SecretStr
    table_name: str
    vector_dim: int


class FAISSConfig(BaseModel):
    vectordb_type: Literal["faiss"] = "faiss"
    vectordb_folder_path: str


class LocalStorageConfig(BaseModel):
    storage_type: Literal["local_storage"] = "local_storage"
    storage_path: Path
    files: dict[UUID, QuivrFileSerialized]


class TransparentStorageConfig(BaseModel):
    storage_type: Literal["transparent_storage"] = "transparent_storage"
    files: dict[UUID, QuivrFileSerialized]


class BrainSerialized(BaseModel):
    id: UUID
    name: str
    chat_history: list[ChatMessage]
    vectordb_config: Union[FAISSConfig, PGVectorConfig] = Field(
        ..., discriminator="vectordb_type"
    )
    storage_config: Union[TransparentStorageConfig, LocalStorageConfig] = Field(
        ..., discriminator="storage_type"
    )

    llm_config: LLMEndpointConfig
    embedding_config: EmbedderConfig
```

## File: `core/quivr_core/files/__init__.py`
```python
from .file import QuivrFile

__all__ = ["QuivrFile"]
```

## File: `core/quivr_core/files/file.py`
```python
import hashlib
import mimetypes
import os
import warnings
from contextlib import asynccontextmanager
from enum import Enum
from pathlib import Path
from typing import Any, AsyncGenerator, AsyncIterable, Self
from uuid import UUID, uuid4

import aiofiles
from openai import BaseModel


class QuivrFileSerialized(BaseModel):
    id: UUID
    brain_id: UUID
    path: Path
    original_filename: str
    file_size: int | None
    file_extension: str
    file_sha1: str
    additional_metadata: dict[str, Any]


class FileExtension(str, Enum):
    txt = ".txt"
    pdf = ".pdf"
    csv = ".csv"
    doc = ".doc"
    docx = ".docx"
    pptx = ".pptx"
    xls = ".xls"
    xlsx = ".xlsx"
    md = ".md"
    mdx = ".mdx"
    markdown = ".markdown"
    bib = ".bib"
    epub = ".epub"
    html = ".html"
    odt = ".odt"
    py = ".py"
    ipynb = ".ipynb"
    m4a = ".m4a"
    mp3 = ".mp3"
    webm = ".webm"
    mp4 = ".mp4"
    mpga = ".mpga"
    wav = ".wav"
    mpeg = ".mpeg"


def get_file_extension(file_path: Path) -> FileExtension | str:
    try:
        mime_type, _ = mimetypes.guess_type(file_path.name)
        if mime_type:
            mime_ext = mimetypes.guess_extension(mime_type)
            if mime_ext:
                return FileExtension(mime_ext)
        return FileExtension(file_path.suffix)
    except ValueError:
        warnings.warn(
            f"File {file_path.name} extension isn't recognized. Make sure you have registered a parser for {file_path.suffix}",
            stacklevel=2,
        )
        return file_path.suffix


async def load_qfile(brain_id: UUID, path: str | Path):
    if not isinstance(path, Path):
        path = Path(path)

    if not path.exists():
        raise FileExistsError(f"file {path} doesn't exist")

    file_size = os.stat(path).st_size

    async with aiofiles.open(path, mode="rb") as f:
        file_sha1 = hashlib.sha1(await f.read()).hexdigest()

    try:
        # NOTE: when loading from existing storage, file name will be uuid
        id = UUID(path.name)
    except ValueError:
        id = uuid4()

    return QuivrFile(
        id=id,
        brain_id=brain_id,
        path=path,
        original_filename=path.name,
        file_extension=get_file_extension(path),
        file_size=file_size,
        file_sha1=file_sha1,
    )


class QuivrFile:
    __slots__ = [
        "id",
        "brain_id",
        "path",
        "original_filename",
        "file_size",
        "file_extension",
        "file_sha1",
        "additional_metadata",
    ]

    def __init__(
        self,
        id: UUID,
        original_filename: str,
        path: Path,
        file_sha1: str,
        file_extension: FileExtension | str,
        brain_id: UUID | None = None,
        file_size: int | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        self.id = id
        self.brain_id = brain_id
        self.path = path
        self.original_filename = original_filename
        self.file_size = file_size
        self.file_extension = file_extension
        self.file_sha1 = file_sha1
        self.additional_metadata = metadata if metadata else {}

    def __repr__(self) -> str:
        return f"QuivrFile-{self.id} original_filename:{self.original_filename}"

    @asynccontextmanager
    async def open(self) -> AsyncGenerator[AsyncIterable[bytes], None]:
        # TODO(@aminediro) : match on path type
        f = await aiofiles.open(self.path, mode="rb")
        try:
            yield f
        finally:
            await f.close()

    @property
    def metadata(self) -> dict[str, Any]:
        return {
            "qfile_id": self.id,
            "qfile_path": self.path,
            "original_file_name": self.original_filename,
            "file_sha1": self.file_sha1,
            "file_size": self.file_size,
            **self.additional_metadata,
        }

    def serialize(self) -> QuivrFileSerialized:
        return QuivrFileSerialized(
            id=self.id,
            brain_id=self.brain_id,
            path=self.path.absolute(),
            original_filename=self.original_filename,
            file_size=self.file_size,
            file_extension=self.file_extension,
            file_sha1=self.file_sha1,
            additional_metadata=self.additional_metadata,
        )

    @classmethod
    def deserialize(cls, serialized: QuivrFileSerialized) -> Self:
        return cls(
            id=serialized.id,
            brain_id=serialized.brain_id,
            path=serialized.path,
            original_filename=serialized.original_filename,
            file_size=serialized.file_size,
            file_extension=serialized.file_extension,
            file_sha1=serialized.file_sha1,
            metadata=serialized.additional_metadata,
        )
```

## File: `core/quivr_core/language/models.py`
```python
from enum import Enum


class Language(str, Enum):
    AF = "af"  # Afrikaans
    ALS = "als"  # Alemannic
    AM = "am"  # Amharic
    AN = "an"  # Aragonese
    AR = "ar"  # Arabic
    ARZ = "arz"  # Egyptian Arabic
    AS = "as"  # Assamese
    AST = "ast"  # Asturian
    AV = "av"  # Avaric
    AZ = "az"  # Azerbaijani
    AZB = "azb"  # South Azerbaijani
    BA = "ba"  # Bashkir
    BAR = "bar"  # Bavarian
    BCL = "bcl"  # Central Bikol
    BE = "be"  # Belarusian
    BG = "bg"  # Bulgarian
    BH = "bh"  # Bihari
    BN = "bn"  # Bengali
    BO = "bo"  # Tibetan
    BPY = "bpy"  # Bishnupriya Manipuri
    BR = "br"  # Breton
    BS = "bs"  # Bosnian
    BXR = "bxr"  # Buryat
    CA = "ca"  # Catalan
    CBK = "cbk"  # Chavacano
    CE = "ce"  # Chechen
    CEB = "ceb"  # Cebuano
    CKB = "ckb"  # Central Kurdish
    CO = "co"  # Corsican
    CS = "cs"  # Czech
    CV = "cv"  # Chuvash
    CY = "cy"  # Welsh
    DA = "da"  # Danish
    DE = "de"  # German
    DIQ = "diq"  # Zazaki
    DSB = "dsb"  # Lower Sorbian
    DTY = "dty"  # Doteli
    DV = "dv"  # Dhivehi
    EL = "el"  # Greek
    EML = "eml"  # Emilian-Romagnol
    EN = "en"  # English
    EO = "eo"  # Esperanto
    ES = "es"  # Spanish
    ET = "et"  # Estonian
    EU = "eu"  # Basque
    FA = "fa"  # Persian
    FI = "fi"  # Finnish
    FR = "fr"  # French
    FRR = "frr"  # North Frisian
    FY = "fy"  # Western Frisian
    GA = "ga"  # Irish
    GD = "gd"  # Scottish Gaelic
    GL = "gl"  # Galician
    GN = "gn"  # Guarani
    GOM = "gom"  # Goan Konkani
    GU = "gu"  # Gujarati
    GV = "gv"  # Manx
    HE = "he"  # Hebrew
    HI = "hi"  # Hindi
    HIF = "hif"  # Fiji Hindi
    HR = "hr"  # Croatian
    HSB = "hsb"  # Upper Sorbian
    HT = "ht"  # Haitian Creole
    HU = "hu"  # Hungarian
    HY = "hy"  # Armenian
    IA = "ia"  # Interlingua
    ID = "id"  # Indonesian
    IE = "ie"  # Interlingue
    ILO = "ilo"  # Iloko
    IO = "io"  # Ido
    IS = "is"  # Icelandic
    IT = "it"  # Italian
    JA = "ja"  # Japanese
    JBO = "jbo"  # Lojban
    JV = "jv"  # Javanese
    KA = "ka"  # Georgian
    KK = "kk"  # Kazakh
    KM = "km"  # Khmer
    KN = "kn"  # Kannada
    KO = "ko"  # Korean
    KRC = "krc"  # Karachay-Balkar
    KU = "ku"  # Kurdish
    KV = "kv"  # Komi
    KW = "kw"  # Cornish
    KY = "ky"  # Kyrgyz
    LA = "la"  # Latin
    LB = "lb"  # Luxembourgish
    LEZ = "lez"  # Lezghian
    LI = "li"  # Limburgish
    LMO = "lmo"  # Lombard
    LO = "lo"  # Lao
    LRC = "lrc"  # Northern Luri
    LT = "lt"  # Lithuanian
    LV = "lv"  # Latvian
    MAI = "mai"  # Maithili
    MG = "mg"  # Malagasy
    MHR = "mhr"  # Eastern Mari
    MIN = "min"  # Minangkabau
    MK = "mk"  # Macedonian
    ML = "ml"  # Malayalam
    MN = "mn"  # Mongolian
    MR = "mr"  # Marathi
    MRJ = "mrj"  # Western Mari
    MS = "ms"  # Malay
    MT = "mt"  # Maltese
    MWL = "mwl"  # Mirandese
    MY = "my"  # Burmese
    MYV = "myv"  # Erzya
    MZN = "mzn"  # Mazanderani
    NAH = "nah"  # Nahuatl
    NAP = "nap"  # Neapolitan
    NDS = "nds"  # Low German
    NE = "ne"  # Nepali
    NEW = "new"  # Newari
    NL = "nl"  # Dutch
    NN = "nn"  # Norwegian Nynorsk
    NO = "no"  # Norwegian
    OC = "oc"  # Occitan
    OR = "or"  # Odia
    OS = "os"  # Ossetian
    PA = "pa"  # Punjabi
    PAM = "pam"  # Pampanga
    PFL = "pfl"  # Palatine German
    PL = "pl"  # Polish
    PMS = "pms"  # Piedmontese
    PNB = "pnb"  # Western Punjabi
    PS = "ps"  # Pashto
    PT = "pt"  # Portuguese
    QU = "qu"  # Quechua
    RM = "rm"  # Romansh
    RO = "ro"  # Romanian
    RU = "ru"  # Russian
    RUE = "rue"  # Rusyn
    SA = "sa"  # Sanskrit
    SAH = "sah"  # Yakut
    SC = "sc"  # Sardinian
    SCN = "scn"  # Sicilian
    SCO = "sco"  # Scots
    SD = "sd"  # Sindhi
    SH = "sh"  # Serbo-Croatian
    SI = "si"  # Sinhala
    SK = "sk"  # Slovak
    SL = "sl"  # Slovenian
    SO = "so"  # Somali
    SQ = "sq"  # Albanian
    SR = "sr"  # Serbian
    SU = "su"  # Sundanese
    SV = "sv"  # Swedish
    SW = "sw"  # Swahili
    TA = "ta"  # Tamil
    TE = "te"  # Telugu
    TG = "tg"  # Tajik
    TH = "th"  # Thai
    TK = "tk"  # Turkmen
    TL = "tl"  # Tagalog
    TR = "tr"  # Turkish
    TT = "tt"  # Tatar
    TYV = "tyv"  # Tuvan
    UG = "ug"  # Uyghur
    UK = "uk"  # Ukrainian
    UR = "ur"  # Urdu
    UZ = "uz"  # Uzbek
    VEC = "vec"  # Venetian
    VEP = "vep"  # Veps
    VI = "vi"  # Vietnamese
    VLS = "vls"  # West Flemish
    VO = "vo"  # Volapük
    WA = "wa"  # Walloon
    WAR = "war"  # Waray
    WUU = "wuu"  # Wu Chinese
    XAL = "xal"  # Kalmyk
    XMF = "xmf"  # Mingrelian
    YI = "yi"  # Yiddish
    YO = "yo"  # Yoruba
    YUE = "yue"  # Cantonese
    ZH = "zh"  # Chinese
    UNKNOWN = "unknown"  # Unknown
```

## File: `core/quivr_core/language/utils.py`
```python
from ftlangdetect import detect
from quivr_core.language.models import Language


def detect_language(text: str, low_memory: bool = True) -> Language:
    detected_lang = detect(text=text, low_memory=low_memory)
    try:
        detected_language = Language(detected_lang["lang"])
    except ValueError:
        return Language.UNKNOWN

    return detected_language
```

## File: `core/quivr_core/llm/__init__.py`
```python
from .llm_endpoint import LLMEndpoint

__all__ = ["LLMEndpoint"]
```

## File: `core/quivr_core/llm/llm_endpoint.py`
```python
import logging
import os
import time
from typing import Union
from urllib.parse import parse_qs, urlparse

import tiktoken
from langchain_anthropic import ChatAnthropic
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from pydantic import SecretStr

from quivr_core.brain.info import LLMInfo
from quivr_core.rag.entities.config import DefaultModelSuppliers, LLMEndpointConfig
from quivr_core.rag.utils import model_supports_function_calling

logger = logging.getLogger("quivr_core")


class LLMTokenizer:
    _cache: dict[
        int, tuple["LLMTokenizer", int, float]
    ] = {}  # {hash: (tokenizer, size_bytes, last_access_time)}
    _max_cache_size_mb: int = 50
    _max_cache_count: int = 5  # Default maximum number of cached tokenizers
    _current_cache_size: int = 0
    _default_size: int = 5 * 1024 * 1024

    def __init__(self, tokenizer_hub: str | None, fallback_tokenizer: str):
        self.tokenizer_hub = tokenizer_hub
        self.fallback_tokenizer = fallback_tokenizer

        if self.tokenizer_hub:
            # To prevent the warning
            # huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks...
            os.environ["TOKENIZERS_PARALLELISM"] = (
                "false"
                if not os.environ.get("TOKENIZERS_PARALLELISM")
                else os.environ["TOKENIZERS_PARALLELISM"]
            )
            try:
                if "text-embedding-ada-002" in self.tokenizer_hub:
                    from transformers import GPT2TokenizerFast

                    self.tokenizer = GPT2TokenizerFast.from_pretrained(
                        self.tokenizer_hub
                    )
                else:
                    from transformers import AutoTokenizer

                    self.tokenizer = AutoTokenizer.from_pretrained(self.tokenizer_hub)
            except OSError:  # if we don't manage to connect to huggingface and/or no cached models are present
                logger.warning(
                    f"Cannot acces the configured tokenizer from {self.tokenizer_hub}, using the default tokenizer {self.fallback_tokenizer}"
                )
                self.tokenizer = tiktoken.get_encoding(self.fallback_tokenizer)
        else:
            self.tokenizer = tiktoken.get_encoding(self.fallback_tokenizer)

        # More accurate size estimation
        self._size_bytes = self._calculate_tokenizer_size()

    def _calculate_tokenizer_size(self) -> int:
        """Calculate size of tokenizer by summing the sizes of its vocabulary and model files"""
        # By default, return a size of 5 MB
        if not hasattr(self.tokenizer, "vocab_files_names") or not hasattr(
            self.tokenizer, "init_kwargs"
        ):
            return self._default_size

        total_size = 0

        # Get the file keys from vocab_files_names
        file_keys = self.tokenizer.vocab_files_names.keys()
        # Look up these files in init_kwargs
        for key in file_keys:
            if file_path := self.tokenizer.init_kwargs.get(key):
                try:
                    total_size += os.path.getsize(file_path)
                except (OSError, FileNotFoundError):
                    logger.debug(f"Could not access tokenizer file: {file_path}")

        return total_size if total_size > 0 else self._default_size

    @classmethod
    def load(cls, tokenizer_hub: str, fallback_tokenizer: str):
        cache_key = hash(str(tokenizer_hub))

        # If in cache, update last access time and return
        if cache_key in cls._cache:
            tokenizer, size, _ = cls._cache[cache_key]
            cls._cache[cache_key] = (tokenizer, size, time.time())
            return tokenizer

        # Create new instance
        instance = cls(tokenizer_hub, fallback_tokenizer)

        # Check if adding this would exceed either cache limit
        while (
            cls._current_cache_size + instance._size_bytes
            > cls._max_cache_size_mb * 1024 * 1024
            or len(cls._cache) >= cls._max_cache_count
        ):
            # Find least recently used item
            oldest_key = min(
                cls._cache.keys(),
                key=lambda k: cls._cache[k][2],  # last_access_time
            )
            # Remove it
            _, removed_size, _ = cls._cache.pop(oldest_key)
            cls._current_cache_size -= removed_size

        # Add new instance to cache with current timestamp
        cls._cache[cache_key] = (instance, instance._size_bytes, time.time())
        cls._current_cache_size += instance._size_bytes
        return instance

    @classmethod
    def set_max_cache_size_mb(cls, size_mb: int):
        """Set the maximum cache size in megabytes."""
        cls._max_cache_size_mb = size_mb
        cls._cleanup_cache()

    @classmethod
    def set_max_cache_count(cls, count: int):
        """Set the maximum number of tokenizers to cache."""
        cls._max_cache_count = count
        cls._cleanup_cache()

    @classmethod
    def _cleanup_cache(cls):
        """Clean up cache when limits are exceeded."""
        while (
            cls._current_cache_size > cls._max_cache_size_mb * 1024 * 1024
            or len(cls._cache) > cls._max_cache_count
        ):
            oldest_key = min(cls._cache.keys(), key=lambda k: cls._cache[k][2])
            _, removed_size, _ = cls._cache.pop(oldest_key)
            cls._current_cache_size -= removed_size

    @classmethod
    def preload_tokenizers(cls, models: list[str] | None = None):
        """Preload tokenizers into cache.

        Args:
            models: Optional list of model names (e.g. 'gpt-4o', 'claude-3-5-sonnet').
                   If None, preloads all available tokenizers.
        """
        from quivr_core.rag.entities.config import LLMModelConfig

        unique_tokenizer_hubs = set()

        # Collect tokenizer hubs based on provided models or all available
        if models:
            for model_name in models:
                # Find matching model configurations
                for supplier_models in LLMModelConfig._model_defaults.values():
                    for base_model_name, config in supplier_models.items():
                        # Check if the model name matches or starts with the base model name
                        if (
                            model_name.startswith(base_model_name)
                            and config.tokenizer_hub
                        ):
                            unique_tokenizer_hubs.add(config.tokenizer_hub)
                            break
        else:
            # Original behavior - collect all unique tokenizer hubs
            for supplier_models in LLMModelConfig._model_defaults.values():
                for config in supplier_models.values():
                    if config.tokenizer_hub:
                        unique_tokenizer_hubs.add(config.tokenizer_hub)

        # Load each unique tokenizer
        for hub in unique_tokenizer_hubs:
            try:
                cls.load(hub, LLMEndpointConfig._FALLBACK_TOKENIZER)
                logger.info(
                    f"Successfully preloaded tokenizer: {hub}. "
                    f"Total cache size: {cls._current_cache_size / (1024 * 1024):.2f} MB. "
                    f"Cache count: {len(cls._cache)}"
                )
            except Exception as e:
                logger.warning(f"Failed to preload tokenizer {hub}: {str(e)}")


class LLMEndpoint:
    _cache = {}

    def __init__(self, llm_config: LLMEndpointConfig, llm: BaseChatModel):
        self._config = llm_config
        self._llm = llm
        self._supports_func_calling = model_supports_function_calling(
            self._config.model
        )

        self.llm_tokenizer = LLMTokenizer.load(
            llm_config.tokenizer_hub, llm_config.fallback_tokenizer
        )

    def count_tokens(self, text: str) -> int:
        # Tokenize the input text and return the token count
        encoding = self.llm_tokenizer.tokenizer.encode(text)
        return len(encoding)

    def get_config(self):
        return self._config

    @classmethod
    def from_config(cls, config: LLMEndpointConfig = LLMEndpointConfig()):
        hashed_config = hash(config)
        if hashed_config in cls._cache:
            return cls._cache[hashed_config]

        _llm: Union[
            AzureChatOpenAI,
            ChatOpenAI,
            ChatAnthropic,
            ChatMistralAI,
            ChatGoogleGenerativeAI,
            ChatGroq,
        ]
        try:
            if config.supplier == DefaultModelSuppliers.AZURE:
                # Parse the URL
                parsed_url = urlparse(config.llm_base_url)
                deployment = parsed_url.path.split("/")[3]  # type: ignore
                api_version = parse_qs(parsed_url.query).get("api-version", [None])[0]  # type: ignore
                azure_endpoint = f"https://{parsed_url.netloc}"  # type: ignore
                _llm = AzureChatOpenAI(
                    azure_deployment=deployment,  # type: ignore
                    api_version=api_version,
                    api_key=SecretStr(config.llm_api_key)
                    if config.llm_api_key
                    else None,
                    azure_endpoint=azure_endpoint,
                    max_tokens=config.max_output_tokens,
                    temperature=config.temperature,
                )
            elif config.supplier == DefaultModelSuppliers.ANTHROPIC:
                assert config.llm_api_key, "Can't load model config"
                _llm = ChatAnthropic(
                    model_name=config.model,
                    api_key=SecretStr(config.llm_api_key),
                    base_url=config.llm_base_url,
                    max_tokens_to_sample=config.max_output_tokens,
                    temperature=config.temperature,
                    timeout=None,
                    stop=None,
                )
            elif config.supplier == DefaultModelSuppliers.OPENAI:
                _llm = ChatOpenAI(
                    model=config.model,
                    api_key=SecretStr(config.llm_api_key)
                    if config.llm_api_key
                    else None,
                    base_url=config.llm_base_url,
                    max_completion_tokens=config.max_output_tokens,
                    temperature=config.temperature
                    if not config.model.startswith("o")
                    else None,
                )
            elif config.supplier == DefaultModelSuppliers.MISTRAL:
                _llm = ChatMistralAI(
                    model_name=config.model,
                    api_key=SecretStr(config.llm_api_key)
                    if config.llm_api_key
                    else None,
                    base_url=config.llm_base_url,
                    temperature=config.temperature,
                )
            elif config.supplier == DefaultModelSuppliers.GEMINI:
                _llm = ChatGoogleGenerativeAI(
                    model=config.model,
                    api_key=SecretStr(config.llm_api_key)
                    if config.llm_api_key
                    else None,
                    base_url=config.llm_base_url,
                    max_tokens=config.max_output_tokens,
                    temperature=config.temperature,
                )
            elif config.supplier == DefaultModelSuppliers.GROQ:
                _llm = ChatGroq(
                    model=config.model,
                    api_key=SecretStr(config.llm_api_key)
                    if config.llm_api_key
                    else None,
                    base_url=config.llm_base_url,
                    max_tokens=config.max_output_tokens,
                    temperature=config.temperature,
                )

            else:
                _llm = ChatOpenAI(
                    model=config.model,
                    api_key=SecretStr(config.llm_api_key)
                    if config.llm_api_key
                    else None,
                    base_url=config.llm_base_url,
                    max_completion_tokens=config.max_output_tokens,
                    temperature=config.temperature,
                )
            instance = cls(llm=_llm, llm_config=config)
            cls._cache[hashed_config] = instance

            return instance

        except ImportError as e:
            raise ImportError(
                "Please provide a valid BaseLLM or install quivr-core['base'] package"
            ) from e

    def supports_func_calling(self) -> bool:
        return self._supports_func_calling

    def info(self) -> LLMInfo:
        return LLMInfo(
            model=self._config.model,
            llm_base_url=(
                self._config.llm_base_url if self._config.llm_base_url else "openai"
            ),
            temperature=self._config.temperature,
            max_tokens=self._config.max_output_tokens,
            supports_function_calling=self.supports_func_calling(),
        )

    def clone_llm(self):
        """Create a new instance of the LLM with the same configuration."""
        return self._llm.__class__(**self._llm.__dict__)
```

## File: `core/quivr_core/llm_tools/entity.py`
```python
from quivr_core.base_config import QuivrBaseConfig
from typing import Callable
from langchain_core.tools import BaseTool
from typing import Dict, Any


class ToolsCategory(QuivrBaseConfig):
    name: str
    description: str
    tools: list
    default_tool: str | None = None
    create_tool: Callable

    def __init__(self, **data):
        super().__init__(**data)
        self.name = self.name.lower()


class ToolWrapper:
    def __init__(self, tool: BaseTool, format_input: Callable, format_output: Callable):
        self.tool = tool
        self.format_input = format_input
        self.format_output = format_output


class ToolRegistry:
    def __init__(self):
        self._registry = {}

    def register_tool(self, tool_name: str, create_func: Callable):
        self._registry[tool_name] = create_func

    def create_tool(self, tool_name: str, config: Dict[str, Any]) -> ToolWrapper:
        if tool_name not in self._registry:
            raise ValueError(f"Tool {tool_name} is not supported.")
        return self._registry[tool_name](config)
```

## File: `core/quivr_core/llm_tools/llm_tools.py`
```python
from typing import Dict, Any, Type, Union

from quivr_core.llm_tools.entity import ToolWrapper

from quivr_core.llm_tools.web_search_tools import (
    WebSearchTools,
)

from quivr_core.llm_tools.other_tools import (
    OtherTools,
)

TOOLS_CATEGORIES = {
    WebSearchTools.name: WebSearchTools,
    OtherTools.name: OtherTools,
}

# Register all ToolsList enums
TOOLS_LISTS = {
    **{tool.value: tool for tool in WebSearchTools.tools},
    **{tool.value: tool for tool in OtherTools.tools},
}


class LLMToolFactory:
    @staticmethod
    def create_tool(tool_name: str, config: Dict[str, Any]) -> Union[ToolWrapper, Type]:
        for category, tools_class in TOOLS_CATEGORIES.items():
            if tool_name in tools_class.tools:
                return tools_class.create_tool(tool_name, config)
            elif tool_name.lower() == category and tools_class.default_tool:
                return tools_class.create_tool(tools_class.default_tool, config)
        raise ValueError(f"Tool {tool_name} is not supported.")
```

## File: `core/quivr_core/llm_tools/other_tools.py`
```python
from enum import Enum
from typing import Dict, Any, Type, Union
from langchain_core.tools import BaseTool
from quivr_core.llm_tools.entity import ToolsCategory
from quivr_core.rag.entities.models import cited_answer


class OtherToolsList(str, Enum):
    CITED_ANSWER = "cited_answer"


def create_other_tool(tool_name: str, config: Dict[str, Any]) -> Union[BaseTool, Type]:
    if tool_name == OtherToolsList.CITED_ANSWER:
        return cited_answer
    else:
        raise ValueError(f"Tool {tool_name} is not supported.")


OtherTools = ToolsCategory(
    name="Other",
    description="Other tools",
    tools=[OtherToolsList.CITED_ANSWER],
    create_tool=create_other_tool,
)
```

## File: `core/quivr_core/llm_tools/web_search_tools.py`
```python
from enum import Enum
from typing import Dict, List, Any
from langchain_community.tools import TavilySearchResults
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from quivr_core.llm_tools.entity import ToolsCategory
import os
from pydantic import SecretStr  # Ensure correct import
from quivr_core.llm_tools.entity import ToolWrapper, ToolRegistry
from langchain_core.documents import Document


class WebSearchToolsList(str, Enum):
    TAVILY = "tavily"


def create_tavily_tool(config: Dict[str, Any]) -> ToolWrapper:
    api_key = (
        config.pop("api_key") if "api_key" in config else os.getenv("TAVILY_API_KEY")
    )
    if not api_key:
        raise ValueError(
            "Missing required config key 'api_key' or environment variable 'TAVILY_API_KEY'"
        )

    tavily_api_wrapper = TavilySearchAPIWrapper(
        tavily_api_key=SecretStr(api_key),
    )
    tool = TavilySearchResults(
        api_wrapper=tavily_api_wrapper,
        max_results=config.pop("max_results", 5),
        search_depth=config.pop("search_depth", "advanced"),
        include_answer=config.pop("include_answer", True),
        **config,
    )

    tool.name = WebSearchToolsList.TAVILY.value

    def format_input(task: str) -> Dict[str, Any]:
        return {"query": task}

    def format_output(response: Any) -> List[Document]:
        metadata = {"integration": "", "integration_link": ""}
        return [
            Document(
                page_content=d["content"],
                metadata={
                    **metadata,
                    "file_name": d["url"] if "url" in d else "",
                    "original_file_name": d["url"] if "url" in d else "",
                },
            )
            for d in response
        ]

    return ToolWrapper(tool, format_input, format_output)


# Initialize the registry and register tools
web_search_tool_registry = ToolRegistry()
web_search_tool_registry.register_tool(WebSearchToolsList.TAVILY, create_tavily_tool)


def create_web_search_tool(tool_name: str, config: Dict[str, Any]) -> ToolWrapper:
    return web_search_tool_registry.create_tool(tool_name, config)


WebSearchTools = ToolsCategory(
    name="Web Search",
    description="Tools for web searching",
    tools=[WebSearchToolsList.TAVILY],
    default_tool=WebSearchToolsList.TAVILY,
    create_tool=create_web_search_tool,
)
```

## File: `core/quivr_core/processor/processor_base.py`
```python
import logging
from abc import ABC, abstractmethod
from importlib.metadata import PackageNotFoundError, version
from typing import Any, Generic, List, TypeVar

from attr import dataclass
from langchain_core.documents import Document

from quivr_core.files.file import FileExtension, QuivrFile
from quivr_core.language.utils import detect_language

logger = logging.getLogger("quivr_core")


R = TypeVar("R", covariant=True)


@dataclass
class ProcessedDocument(Generic[R]):
    chunks: List[Document]
    processor_cls: str
    processor_response: R


# TODO: processors should be cached somewhere ?
# The processor should be cached by processor type
# The cache should use a single
class ProcessorBase(ABC, Generic[R]):
    supported_extensions: list[FileExtension | str]

    def check_supported(self, file: QuivrFile) -> None:
        if file.file_extension not in self.supported_extensions:
            raise ValueError(f"can't process a file of type {file.file_extension}")

    @property
    @abstractmethod
    def processor_metadata(self) -> dict[str, Any]:
        raise NotImplementedError

    async def process_file(self, file: QuivrFile) -> ProcessedDocument[R]:
        logger.debug(f"Processing file {file}")
        self.check_supported(file)
        docs = await self.process_file_inner(file)
        try:
            qvr_version = version("quivr-core")
        except PackageNotFoundError:
            qvr_version = "dev"

        for idx, doc in enumerate(docs.chunks, start=1):
            if "original_file_name" in doc.metadata:
                doc.page_content = f"Filename: {doc.metadata['original_file_name']} Content: {doc.page_content}"
            doc.page_content = doc.page_content.replace("\u0000", "")
            doc.page_content = doc.page_content.encode("utf-8", "replace").decode(
                "utf-8"
            )
            doc.metadata = {
                "chunk_index": idx,
                "quivr_core_version": qvr_version,
                "language": detect_language(
                    text=doc.page_content.replace("\\n", " ").replace("\n", " "),
                    low_memory=True,
                ).value,
                **file.metadata,
                **doc.metadata,
                **self.processor_metadata,
            }
        return docs

    @abstractmethod
    async def process_file_inner(self, file: QuivrFile) -> ProcessedDocument[R]:
        raise NotImplementedError
```

## File: `core/quivr_core/processor/registry.py`
```python
import importlib
import logging
import types
from dataclasses import dataclass, field
from heapq import heappop, heappush
from typing import List, Type, TypeAlias

from quivr_core.files.file import FileExtension

from .processor_base import ProcessorBase

logger = logging.getLogger("quivr_core")

_LOWEST_PRIORITY = 100

_registry: dict[str, Type[ProcessorBase]] = {}

# external, read only. Contains the actual processors that we are imported and ready to use
registry = types.MappingProxyType(_registry)


@dataclass(order=True)
class ProcEntry:
    priority: int
    cls_mod: str = field(compare=False)
    err: str | None = field(compare=False)


ProcMapping: TypeAlias = dict[FileExtension | str, list[ProcEntry]]

# Register based on mimetypes
base_processors: ProcMapping = {
    FileExtension.txt: [
        ProcEntry(
            cls_mod="quivr_core.processor.implementations.simple_txt_processor.SimpleTxtProcessor",
            err=None,
            priority=_LOWEST_PRIORITY,
        )
    ],
    FileExtension.pdf: [
        ProcEntry(
            cls_mod="quivr_core.processor.implementations.tika_processor.TikaProcessor",
            err=None,
            priority=_LOWEST_PRIORITY,
        )
    ],
}


def _append_proc_mapping(
    mapping: ProcMapping,
    file_exts: List[FileExtension] | List[str],
    cls_mod: str,
    errtxt: str,
    priority: int | None,
):
    for file_ext in file_exts:
        if file_ext in mapping:
            try:
                prev_proc = heappop(mapping[file_ext])
                proc_entry = ProcEntry(
                    priority=priority
                    if priority is not None
                    else prev_proc.priority - 1,
                    cls_mod=cls_mod,
                    err=errtxt,
                )
                # Push the previous processor back
                heappush(mapping[file_ext], prev_proc)
                heappush(mapping[file_ext], proc_entry)
            except IndexError:
                proc_entry = ProcEntry(
                    priority=priority if priority is not None else _LOWEST_PRIORITY,
                    cls_mod=cls_mod,
                    err=errtxt,
                )
                heappush(mapping[file_ext], proc_entry)

        else:
            proc_entry = ProcEntry(
                priority=priority if priority is not None else _LOWEST_PRIORITY,
                cls_mod=cls_mod,
                err=errtxt,
            )

            mapping[file_ext] = [proc_entry]


def defaults_to_proc_entries(
    base_processors: ProcMapping,
) -> ProcMapping:
    # TODO(@aminediro) : how can a user change the order of the processor ?
    # NOTE: order of this list is important as resolution of `get_processor_class` depends on it
    # We should have a way to automatically add these at 'import' time
    for supported_extensions, processor_name in [
        ([FileExtension.csv], "CSVProcessor"),
        ([FileExtension.txt], "TikTokenTxtProcessor"),
        ([FileExtension.docx, FileExtension.doc], "DOCXProcessor"),
        ([FileExtension.xls, FileExtension.xlsx], "XLSXProcessor"),
        ([FileExtension.pptx], "PPTProcessor"),
        (
            [FileExtension.markdown, FileExtension.md, FileExtension.mdx],
            "MarkdownProcessor",
        ),
        ([FileExtension.epub], "EpubProcessor"),
        ([FileExtension.bib], "BibTexProcessor"),
        ([FileExtension.odt], "ODTProcessor"),
        ([FileExtension.html], "HTMLProcessor"),
        ([FileExtension.py], "PythonProcessor"),
        ([FileExtension.ipynb], "NotebookProcessor"),
    ]:
        for ext in supported_extensions:
            ext_str = ext.value if isinstance(ext, FileExtension) else ext
            _append_proc_mapping(
                mapping=base_processors,
                file_exts=[ext],
                cls_mod=f"quivr_core.processor.implementations.default.{processor_name}",
                errtxt=f"can't import {processor_name}. Please install quivr-core[{ext_str}] to access {processor_name}",
                priority=None,
            )

    # TODO(@aminediro): Megaparse should register itself
    # Append Megaparse
    _append_proc_mapping(
        mapping=base_processors,
        file_exts=[
            FileExtension.txt,
            FileExtension.pdf,
            FileExtension.docx,
            FileExtension.doc,
            FileExtension.pptx,
            FileExtension.xls,
            FileExtension.xlsx,
            FileExtension.csv,
            FileExtension.epub,
            FileExtension.bib,
            FileExtension.odt,
            FileExtension.html,
            FileExtension.markdown,
            FileExtension.md,
            FileExtension.mdx,
        ],
        cls_mod="quivr_core.processor.implementations.megaparse_processor.MegaparseProcessor",
        errtxt=f"can't import MegaparseProcessor. Please install quivr-core[{ext_str}] to access MegaparseProcessor",
        priority=None,
    )
    return base_processors


known_processors = defaults_to_proc_entries(base_processors)


def get_processor_class(file_extension: FileExtension | str) -> Type[ProcessorBase]:
    """Fetch processor class from registry

    The dict ``known_processors`` maps file extensions to the locations
    of processors that could process them.
    Loading of these classes is *Lazy*. Appropriate import will happen
    the first time we try to process some file type.

    Some processors need additional dependencies. If the import fails
    we return the "err" field of the ProcEntry in  ``known_processors``.
    """

    if file_extension not in registry:
        # Either you registered it from module or it's in the known processors
        if file_extension not in known_processors:
            raise ValueError(f"Extension not known: {file_extension}")
        entries = known_processors[file_extension]
        while entries:
            proc_entry = heappop(entries)
            try:
                register_processor(file_extension, _import_class(proc_entry.cls_mod))
                break
            except ImportError:
                logger.warn(
                    f"{proc_entry.err}. Falling to the next available processor for {file_extension}"
                )
        if len(entries) == 0 and file_extension not in registry:
            raise ImportError(f"can't find any processor for {file_extension}")

    cls = registry[file_extension]
    return cls


def register_processor(
    file_ext: FileExtension | str,
    proc_cls: str | Type[ProcessorBase],
    append: bool = True,
    override: bool = False,
    errtxt: str | None = None,
    priority: int | None = None,
):
    if isinstance(proc_cls, str):
        if file_ext in known_processors and append is False:
            if all(proc_cls != proc.cls_mod for proc in known_processors[file_ext]):
                raise ValueError(
                    f"Processor for ({file_ext}) already in the registry and append is False"
                )
        else:
            if all(proc_cls != proc.cls_mod for proc in known_processors[file_ext]):
                _append_proc_mapping(
                    known_processors,
                    file_exts=[file_ext],
                    cls_mod=proc_cls,
                    errtxt=errtxt
                    or f"{proc_cls} import failed for processor of {file_ext}",
                    priority=priority,
                )
            else:
                logger.info(f"{proc_cls} already in registry...")

    else:
        assert issubclass(
            proc_cls, ProcessorBase
        ), f"{proc_cls} should be a subclass of quivr_core.processor.ProcessorBase"
        if file_ext in registry and override is False:
            if _registry[file_ext] is not proc_cls:
                raise ValueError(
                    f"Processor for ({file_ext}) already in the registry and append is False"
                )
        else:
            _registry[file_ext] = proc_cls


def _import_class(full_mod_path: str):
    if ":" in full_mod_path:
        mod_name, name = full_mod_path.rsplit(":", 1)
    else:
        mod_name, name = full_mod_path.rsplit(".", 1)

    mod = importlib.import_module(mod_name)

    for cls in name.split("."):
        mod = getattr(mod, cls)

    if not isinstance(mod, type):
        raise TypeError(f"{full_mod_path} is not a class")

    if not issubclass(mod, ProcessorBase):
        raise TypeError(f"{full_mod_path} is not a subclass of ProcessorBase ")

    return mod


def available_processors():
    """Return a list of the known processors."""
    return list(known_processors)
```

## File: `core/quivr_core/processor/splitter.py`
```python
from pydantic import BaseModel


class SplitterConfig(BaseModel):
    """
    This class is used to configure the chunking of the documents.

    Chunk size is the number of characters in the chunk.
    Chunk overlap is the number of characters that the chunk will overlap with the previous chunk.
    """

    chunk_size: int = 400
    chunk_overlap: int = 100
```

## File: `core/quivr_core/processor/implementations/default.py`
```python
import logging
from typing import Any, List, Type, TypeVar

import tiktoken
from langchain_community.document_loaders import (
    BibtexLoader,
    CSVLoader,
    Docx2txtLoader,
    NotebookLoader,
    PythonLoader,
    UnstructuredEPubLoader,
    UnstructuredExcelLoader,
    UnstructuredHTMLLoader,
    UnstructuredMarkdownLoader,
    UnstructuredODTLoader,
    UnstructuredPDFLoader,
    UnstructuredPowerPointLoader,
)
from langchain_community.document_loaders.base import BaseLoader
from langchain_community.document_loaders.text import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, TextSplitter

from quivr_core.files.file import FileExtension, QuivrFile
from quivr_core.processor.processor_base import ProcessedDocument, ProcessorBase
from quivr_core.processor.splitter import SplitterConfig

logger = logging.getLogger("quivr_core")

P = TypeVar("P", bound=BaseLoader)


class ProcessorInit(ProcessorBase):
    def __init__(self, *args, **loader_kwargs) -> None:
        pass


# FIXME(@aminediro):
# dynamically creates Processor classes. Maybe redo this for finer control over instanciation
# processor classes are opaque as we don't know what params they would have -> not easy to have lsp completion
def _build_processor(
    cls_name: str, load_cls: Type[P], cls_extensions: List[FileExtension | str]
) -> Type[ProcessorInit]:
    enc = tiktoken.get_encoding("cl100k_base")

    class _Processor(ProcessorBase):
        supported_extensions = cls_extensions

        def __init__(
            self,
            splitter: TextSplitter | None = None,
            splitter_config: SplitterConfig = SplitterConfig(),
            **loader_kwargs: dict[str, Any],
        ) -> None:
            self.loader_cls = load_cls
            self.loader_kwargs = loader_kwargs

            self.splitter_config = splitter_config

            if splitter:
                self.text_splitter = splitter
            else:
                self.text_splitter = (
                    RecursiveCharacterTextSplitter.from_tiktoken_encoder(
                        chunk_size=splitter_config.chunk_size,
                        chunk_overlap=splitter_config.chunk_overlap,
                    )
                )

        @property
        def processor_metadata(self) -> dict[str, Any]:
            return {
                "processor_cls": self.loader_cls.__name__,
                "splitter": self.splitter_config.model_dump(),
            }

        async def process_file_inner(self, file: QuivrFile) -> ProcessedDocument[None]:
            if hasattr(self.loader_cls, "__init__"):
                # NOTE: mypy can't correctly type this as BaseLoader doesn't have a constructor method
                loader = self.loader_cls(file_path=str(file.path), **self.loader_kwargs)  # type: ignore
            else:
                loader = self.loader_cls()

            documents = await loader.aload()
            docs = self.text_splitter.split_documents(documents)

            for doc in docs:
                # TODO: This metadata info should be typed
                doc.metadata = {"chunk_size": len(enc.encode(doc.page_content))}

            return ProcessedDocument(
                chunks=docs, processor_cls=cls_name, processor_response=None
            )

    return type(cls_name, (ProcessorInit,), dict(_Processor.__dict__))


CSVProcessor = _build_processor("CSVProcessor", CSVLoader, [FileExtension.csv])
TikTokenTxtProcessor = _build_processor(
    "TikTokenTxtProcessor", TextLoader, [FileExtension.txt]
)
DOCXProcessor = _build_processor(
    "DOCXProcessor", Docx2txtLoader, [FileExtension.docx, FileExtension.doc]
)
XLSXProcessor = _build_processor(
    "XLSXProcessor", UnstructuredExcelLoader, [FileExtension.xlsx, FileExtension.xls]
)
PPTProcessor = _build_processor(
    "PPTProcessor", UnstructuredPowerPointLoader, [FileExtension.pptx]
)
MarkdownProcessor = _build_processor(
    "MarkdownProcessor",
    UnstructuredMarkdownLoader,
    [FileExtension.md, FileExtension.mdx, FileExtension.markdown],
)
EpubProcessor = _build_processor(
    "EpubProcessor", UnstructuredEPubLoader, [FileExtension.epub]
)
BibTexProcessor = _build_processor("BibTexProcessor", BibtexLoader, [FileExtension.bib])
ODTProcessor = _build_processor(
    "ODTProcessor", UnstructuredODTLoader, [FileExtension.odt]
)
HTMLProcessor = _build_processor(
    "HTMLProcessor", UnstructuredHTMLLoader, [FileExtension.html]
)
PythonProcessor = _build_processor("PythonProcessor", PythonLoader, [FileExtension.py])
NotebookProcessor = _build_processor(
    "NotebookProcessor", NotebookLoader, [FileExtension.ipynb]
)
UnstructuredPDFProcessor = _build_processor(
    "UnstructuredPDFProcessor", UnstructuredPDFLoader, [FileExtension.pdf]
)
```

## File: `core/quivr_core/processor/implementations/megaparse_processor.py`
```python
import logging

import tiktoken
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter, TextSplitter
from megaparse_sdk.client import MegaParseNATSClient
from megaparse_sdk.config import ClientNATSConfig
from megaparse_sdk.schema.document import Document as MPDocument

from quivr_core.config import MegaparseConfig
from quivr_core.files.file import QuivrFile
from quivr_core.processor.processor_base import ProcessedDocument, ProcessorBase
from quivr_core.processor.registry import FileExtension
from quivr_core.processor.splitter import SplitterConfig

logger = logging.getLogger("quivr_core")


class MegaparseProcessor(ProcessorBase[MPDocument]):
    """
    Megaparse processor for PDF files.

    It can be used to parse PDF files and split them into chunks.

    It comes from the megaparse library.

    ## Installation
    ```bash
    pip install megaparse
    ```

    """

    supported_extensions = [
        FileExtension.txt,
        FileExtension.pdf,
        FileExtension.docx,
        FileExtension.doc,
        FileExtension.pptx,
        FileExtension.xls,
        FileExtension.xlsx,
        FileExtension.csv,
        FileExtension.epub,
        FileExtension.bib,
        FileExtension.odt,
        FileExtension.html,
        FileExtension.markdown,
        FileExtension.md,
        FileExtension.mdx,
    ]

    def __init__(
        self,
        splitter: TextSplitter | None = None,
        splitter_config: SplitterConfig = SplitterConfig(),
        megaparse_config: MegaparseConfig = MegaparseConfig(),
    ) -> None:
        self.enc = tiktoken.get_encoding("cl100k_base")
        self.splitter_config = splitter_config
        self.megaparse_config = megaparse_config

        if splitter:
            self.text_splitter = splitter
        else:
            self.text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
                chunk_size=splitter_config.chunk_size,
                chunk_overlap=splitter_config.chunk_overlap,
            )

    @property
    def processor_metadata(self):
        return {
            "chunk_overlap": self.splitter_config.chunk_overlap,
        }

    async def process_file_inner(
        self, file: QuivrFile
    ) -> ProcessedDocument[MPDocument | str]:
        logger.info(f"Uploading file {file.path} to MegaParse")
        async with MegaParseNATSClient(ClientNATSConfig()) as client:
            response = await client.parse_file(file=file.path)

        document = Document(
            page_content=str(response),
        )

        chunks = self.text_splitter.split_documents([document])
        for chunk in chunks:
            chunk.metadata = {"chunk_size": len(self.enc.encode(chunk.page_content))}
        return ProcessedDocument(
            chunks=chunks,
            processor_cls="MegaparseProcessor",
            processor_response=response,
        )
```

## File: `core/quivr_core/processor/implementations/simple_txt_processor.py`
```python
from typing import Any

import aiofiles
from langchain_core.documents import Document

from quivr_core.files.file import QuivrFile
from quivr_core.processor.processor_base import ProcessedDocument, ProcessorBase
from quivr_core.processor.registry import FileExtension
from quivr_core.processor.splitter import SplitterConfig


def recursive_character_splitter(
    doc: Document, chunk_size: int, chunk_overlap: int
) -> list[Document]:
    assert chunk_overlap < chunk_size, "chunk_overlap is greater than chunk_size"

    if len(doc.page_content) <= chunk_size:
        return [doc]

    chunk = Document(page_content=doc.page_content[:chunk_size], metadata=doc.metadata)
    remaining = Document(
        page_content=doc.page_content[chunk_size - chunk_overlap :],
        metadata=doc.metadata,
    )

    return [chunk] + recursive_character_splitter(remaining, chunk_size, chunk_overlap)


class SimpleTxtProcessor(ProcessorBase):
    """
    SimpleTxtProcessor is a class that implements the ProcessorBase interface.
    It is used to process the files with the Simple Txt parser.
    """

    supported_extensions = [FileExtension.txt]

    def __init__(
        self, splitter_config: SplitterConfig = SplitterConfig(), **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.splitter_config = splitter_config

    @property
    def processor_metadata(self) -> dict[str, Any]:
        return {
            "processor_cls": "SimpleTxtProcessor",
            "splitter": self.splitter_config.model_dump(),
        }

    async def process_file_inner(self, file: QuivrFile) -> ProcessedDocument[str]:
        async with aiofiles.open(file.path, mode="r") as f:
            content = await f.read()

        doc = Document(page_content=content)

        docs = recursive_character_splitter(
            doc, self.splitter_config.chunk_size, self.splitter_config.chunk_overlap
        )

        return ProcessedDocument(
            chunks=docs, processor_cls="SimpleTxtProcessor", processor_response=content
        )
```

## File: `core/quivr_core/processor/implementations/tika_processor.py`
```python
import logging
import os
from typing import AsyncIterable

import httpx
import tiktoken
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter, TextSplitter

from quivr_core.files.file import QuivrFile
from quivr_core.processor.processor_base import ProcessedDocument, ProcessorBase
from quivr_core.processor.registry import FileExtension
from quivr_core.processor.splitter import SplitterConfig

logger = logging.getLogger("quivr_core")


class TikaProcessor(ProcessorBase):
    """
    TikaProcessor is a class that implements the ProcessorBase interface.
    It is used to process the files with the Tika server.

    To run it with docker you can do:
    ```bash
    docker run -d -p 9998:9998 apache/tika
    ```
    """

    supported_extensions = [FileExtension.pdf]

    def __init__(
        self,
        tika_url: str = os.getenv("TIKA_SERVER_URL", "http://localhost:9998/tika"),
        splitter: TextSplitter | None = None,
        splitter_config: SplitterConfig = SplitterConfig(),
        timeout: float = 5.0,
        max_retries: int = 3,
    ) -> None:
        self.tika_url = tika_url
        self.max_retries = max_retries
        self._client = httpx.AsyncClient(timeout=timeout)

        self.enc = tiktoken.get_encoding("cl100k_base")
        self.splitter_config = splitter_config

        if splitter:
            self.text_splitter = splitter
        else:
            self.text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
                chunk_size=splitter_config.chunk_size,
                chunk_overlap=splitter_config.chunk_overlap,
            )

    async def _send_parse_tika(self, f: AsyncIterable[bytes]) -> str:
        retry = 0
        headers = {"Accept": "text/plain"}
        while retry < self.max_retries:
            try:
                resp = await self._client.put(self.tika_url, headers=headers, content=f)
                resp.raise_for_status()
                return resp.content.decode("utf-8")
            except Exception as e:
                retry += 1
                logger.debug(f"tika url error :{e}. retrying for the {retry} time...")
        raise RuntimeError("can't send parse request to tika server")

    @property
    def processor_metadata(self):
        return {
            "chunk_overlap": self.splitter_config.chunk_overlap,
        }

    async def process_file_inner(self, file: QuivrFile) -> ProcessedDocument[None]:
        async with file.open() as f:
            txt = await self._send_parse_tika(f)
        document = Document(page_content=txt)
        docs = self.text_splitter.split_documents([document])
        for doc in docs:
            doc.metadata = {"chunk_size": len(self.enc.encode(doc.page_content))}

        return ProcessedDocument(
            chunks=docs, processor_cls="TikaProcessor", processor_response=None
        )
```

## File: `core/quivr_core/rag/prompts.py`
```python
import datetime
import types
from enum import Enum

from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.prompts.base import BasePromptTemplate


class TemplatePromptName(str, Enum):
    ZENDESK_TEMPLATE_PROMPT = "ZENDESK_TEMPLATE_PROMPT"
    TOOL_ROUTING_PROMPT = "TOOL_ROUTING_PROMPT"
    RAG_ANSWER_PROMPT = "RAG_ANSWER_PROMPT"
    CONDENSE_TASK_PROMPT = "CONDENSE_TASK_PROMPT"
    DEFAULT_DOCUMENT_PROMPT = "DEFAULT_DOCUMENT_PROMPT"
    CHAT_LLM_PROMPT = "CHAT_LLM_PROMPT"
    USER_INTENT_PROMPT = "USER_INTENT_PROMPT"
    UPDATE_PROMPT = "UPDATE_PROMPT"
    SPLIT_PROMPT = "SPLIT_PROMPT"
    ZENDESK_LLM_PROMPT = "ZENDESK_LLM_PROMPT"


def _define_custom_prompts() -> dict[TemplatePromptName, BasePromptTemplate]:
    custom_prompts: dict[TemplatePromptName, BasePromptTemplate] = {}

    today_date = datetime.datetime.now().strftime("%B %d, %Y")

    # ---------------------------------------------------------------------------
    # Prompt for task rephrasing
    # ---------------------------------------------------------------------------
    system_message_template = (
        "Given a chat history and the latest user task "
        "which might reference context in the chat history, "
        "formulate a standalone task which can be understood "
        "without the chat history. Do NOT complete the task, "
        "just reformulate it if needed and otherwise return it as is. "
        "Do not output your reasoning, just the task."
    )

    template_answer = "User task: {task}\n Standalone task:"

    CONDENSE_TASK_PROMPT = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(system_message_template),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template(template_answer),
        ]
    )

    custom_prompts[TemplatePromptName.CONDENSE_TASK_PROMPT] = CONDENSE_TASK_PROMPT

    # ---------------------------------------------------------------------------
    # Prompt for RAG
    # ---------------------------------------------------------------------------
    system_message_template = f"Your name is Quivr. You're a helpful assistant. Today's date is {today_date}. "

    system_message_template += (
        "- When answering use markdown. Use markdown code blocks for code snippets.\n"
        "- Answer in a concise and clear manner.\n"
        "- If no preferred language is provided, answer in the same language as the language used by the user.\n"
        "- You must use ONLY the provided context to complete the task. "
        "Do not use any prior knowledge or external information, even if you are certain of the answer.\n"
        # "- If you cannot provide an answer using ONLY the context provided, do not attempt to answer from your own knowledge."
        # "Instead, inform the user that the answer isn't available in the context and suggest using the available tools {tools}.\n"
        "- Do not apologize when providing an answer.\n"
        "- Don't cite the source id in the answer objects, but you can use the source to complete the task.\n\n"
    )

    context_template = (
        "\n"
        # "- You have access to the following internal reasoning to provide an answer: {reasoning}\n"
        "- You have access to the following files to complete the task (limited to first 20 files): {files}\n"
        "- You have access to the following context to complete the task: {context}\n"
        "- Follow these user instruction when crafting the answer: {custom_instructions}\n"
        "- These user instructions shall take priority over any other previous instruction.\n"
        # "- Remember: if you cannot provide an answer using ONLY the provided context and CITING the sources, "
        # "inform the user that you don't have the answer and consider if any of the tools can help answer the question.\n"
        # "- Explain your reasoning about the potentiel tool usage in the answer.\n"
        # "- Only use binded tools to answer the question.\n"
        # "OFFER the user the possibility to ACTIVATE a relevant tool among "
        # "the tools which can be activated."
        # "Tools which can be activated: {tools}. If any of these tools can help in providing an answer "
        # "to the user question, you should offer the user the possibility to activate it. "
        # "Remember, you shall NOT use the above tools, ONLY offer the user the possibility to activate them.\n"
    )

    template_answer = (
        "Original task: {task}\n"
        "Rephrased and contextualized task: {rephrased_task}\n"
        "Remember, you shall complete ALL tasks.\n"
        "Remember: if you cannot provide an answer using ONLY the provided context and CITING the sources, "
        "just answer that you don't have the answer.\n"
        "If the provided context contains contradictory or conflicting information, state so providing the conflicting information.\n"
    )

    RAG_ANSWER_PROMPT = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(system_message_template),
            MessagesPlaceholder(variable_name="chat_history"),
            SystemMessagePromptTemplate.from_template(context_template),
            HumanMessagePromptTemplate.from_template(template_answer),
        ]
    )
    custom_prompts[TemplatePromptName.RAG_ANSWER_PROMPT] = RAG_ANSWER_PROMPT

    # ---------------------------------------------------------------------------
    # Prompt for formatting documents
    # ---------------------------------------------------------------------------
    DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(
        template="Filename: {original_file_name}\nSource: {index} \n {page_content}"
    )
    custom_prompts[TemplatePromptName.DEFAULT_DOCUMENT_PROMPT] = DEFAULT_DOCUMENT_PROMPT

    # ---------------------------------------------------------------------------
    # Prompt for chatting directly with LLMs, without any document retrieval stage
    # ---------------------------------------------------------------------------
    system_message_template = (
        f"Your name is Quivr. You're a helpful assistant. Today's date is {today_date}."
    )
    system_message_template += """
    If not None, also follow these user instructions when answering: {custom_instructions}
    """

    template_answer = """
    User Task: {task}
    Answer:
    """
    CHAT_LLM_PROMPT = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(system_message_template),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template(template_answer),
        ]
    )
    custom_prompts[TemplatePromptName.CHAT_LLM_PROMPT] = CHAT_LLM_PROMPT

    # ---------------------------------------------------------------------------
    # Prompt to understand the user intent
    # ---------------------------------------------------------------------------
    system_message_template = (
        "Given the following user input, determine the user intent, in particular "
        "whether the user is providing instructions to the system or is asking the system to "
        "complete a task:\n"
        "    - if the user is providing direct instructions to modify the system behaviour (for instance, "
        "'Can you reply in French?' or 'Answer in French' or 'You are an expert legal assistant' "
        "or 'You will behave as...'), the user intent is 'prompt';\n"
        "    - in all other cases (asking questions, asking for summarising a text, asking for translating a text, ...), "
        "the intent is 'task'.\n"
    )

    template_answer = "User input: {task}"

    USER_INTENT_PROMPT = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(system_message_template),
            HumanMessagePromptTemplate.from_template(template_answer),
        ]
    )
    custom_prompts[TemplatePromptName.USER_INTENT_PROMPT] = USER_INTENT_PROMPT

    # ---------------------------------------------------------------------------
    # Prompt to create a system prompt from user instructions
    # ---------------------------------------------------------------------------
    system_message_template = (
        "- Given the following user instruction, current system prompt, list of available tools "
        "and list of activated tools, update the prompt to include the instruction and decide which tools to activate.\n"
        "- The prompt shall only contain generic instructions which can be applied to any user task or question.\n"
        "- The prompt shall be concise and clear.\n"
        "- If the system prompt already contains the instruction, do not add it again.\n"
        "- If the system prompt contradicts ther user instruction, remove the contradictory "
        "statement or statements in the system prompt.\n"
        "- You shall return separately the updated system prompt and the reasoning that led to the update.\n"
        "- If the system prompt refers to a tool, you shall add the tool to the list of activated tools.\n"
        "- If no tool activation is needed, return empty lists.\n"
        "- You shall also return the reasoning that led to the tool activation.\n"
        "- Current system prompt: {system_prompt}\n"
        "- List of available tools: {available_tools}\n"
        "- List of activated tools: {activated_tools}\n\n"
    )

    template_answer = "User instructions: {instruction}\n"

    UPDATE_PROMPT = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(system_message_template),
            HumanMessagePromptTemplate.from_template(template_answer),
        ]
    )
    custom_prompts[TemplatePromptName.UPDATE_PROMPT] = UPDATE_PROMPT

    # ---------------------------------------------------------------------------
    # Prompt to split the user input into multiple questions / instructions
    # ---------------------------------------------------------------------------
    system_message_template = (
        "Given a chat history and the user input, split and rephrase the input into instructions and tasks.\n"
        "- Instructions direct the system to behave in a certain way or to use specific tools: examples of instructions are "
        "'Can you reply in French?', 'Answer in French', 'You are an expert legal assistant', "
        "'You will behave as...', 'Use web search').\n"
        "- You shall collect and condense all the instructions into a single string.\n"
        "- The instructions shall be standalone and self-contained, so that they can be understood "
        "without the chat history. If no instructions are found, return an empty string.\n"
        "- Instructions to be understood may require considering the chat history.\n"
        "- Tasks are often questions, but they can also be summarisation tasks, translation tasks, content generation tasks, etc.\n"
        "- Tasks to be understood may require considering the chat history.\n"
        "- If the user input contains different tasks, you shall split the input into multiple tasks.\n"
        "- Each splitted task shall be a standalone, self-contained task which can be understood "
        "without the chat history. You shall rephrase the tasks if needed.\n"
        "- If no explicit task is present, you shall infer the tasks from the user input and the chat history.\n"
        "- Do NOT try to solve the tasks or answer the questions, "
        "just reformulate them if needed and otherwise return them as is.\n"
        "- Remember, you shall NOT suggest or generate new tasks.\n"
        "- As an example, the user input 'What is Apple? Who is its CEO? When was it founded?' "
        "shall be split into a list of tasks ['What is Apple?', 'Who is the CEO of Apple?', 'When was Apple founded?']\n"
        "- If no tasks are found, return the user input as is in the task list.\n"
    )

    template_answer = "User input: {user_input}"

    SPLIT_PROMPT = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(system_message_template),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template(template_answer),
        ]
    )
    custom_prompts[TemplatePromptName.SPLIT_PROMPT] = SPLIT_PROMPT

    # ---------------------------------------------------------------------------
    # Prompt to grade the relevance of an answer and decide whather to perform a web search
    # ---------------------------------------------------------------------------
    system_message_template = (
        "Given the following tasks you shall determine whether all tasks can be "
        "completed fully and in the best possible way using the provided context and chat history. "
        "You shall:\n"
        "- Consider each task separately,\n"
        "- Determine whether the context and chat history contain "
        "all the information necessary to complete the task.\n"
        "- If the context and chat history do not contain all the information necessary to complete the task, "
        "consider ONLY the list of tools below and select the tool most appropriate to complete the task.\n"
        "- If no tools are listed, return the tasks as is and no tool.\n"
        "- If no relevant tool can be selected, return the tasks as is and no tool.\n"
        "- Do not propose to use a tool if that tool is not listed among the available tools.\n"
    )

    context_template = "Context: {context}\n {activated_tools}\n"

    template_answer = "Tasks: {tasks}\n"

    TOOL_ROUTING_PROMPT = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(system_message_template),
            MessagesPlaceholder(variable_name="chat_history"),
            SystemMessagePromptTemplate.from_template(context_template),
            HumanMessagePromptTemplate.from_template(template_answer),
        ]
    )

    custom_prompts[TemplatePromptName.TOOL_ROUTING_PROMPT] = TOOL_ROUTING_PROMPT

    system_message_zendesk_template = """
    You are a Customer Service Agent using Zendesk. You are answering a client query.
    You will be provided with the users metadata, ticket metadata and ticket history which can be used to answer the query.
    You will also have access to the most relevant similar tickets and additional information sometimes such as API calls.
    Never add something in brackets that needs to be filled like [your name], [your email], etc. 
    Do NOT invent information that was not present in previous tickets or in user metabadata or ticket metadata or additional information.
    Always prioritize information from the most recent tickets, especially if they are contradictory.
    
    Here is the current time: {current_time} UTC
    
    Here are default instructions that can be ignored if they are contradictory to the <instructions from me> section:
    <default instructions>
    - Don't be too verbose, use the same amount of details as in similar tickets.
    - Use the same tone, format, structure and lexical field as in similar tickets agent responses.
    - The text must be correctly formatted with paragraphs, bold, italic, etc so it is easier to read.
    - Maintain consistency in terminology used in recent tickets.
    - Answer in the same language as the user.
    - Don't add a signature at the end of the answer, it will be added once the answer is sent.
    </default instructions>
    
    
    Here are instructions that you MUST follow and prioritize over the <default instructions> section:
    <instructions from me>
    {guidelines}
    </instructions from me>
    """

    user_prompt_template = """
    Here is information about the user that can help you to answer:
    <user_metadata>
    {user_metadata}
    </user_metadata>

    Here are metadata on the current ticket that can help you to answer:
    <ticket_metadata>
    {ticket_metadata}
    </ticket_metadata>


    Here are the most relevant similar tickets that can help you to answer:
    <similar_tickets>
    {similar_tickets}
    </similar_tickets>

    Here are the current ticket history:
    <ticket_history>
    {ticket_history}
    </ticket_history>

    Here are additional information that can help you to answer:
    <additional_information>
    {additional_information}
    </additional_information>

    Here is the client question to which you must answer:
    <client_query>
    {client_query}
    </client_query>
 
    Based on the informations provided, answer directly with the message to send to the customer, ready to be sent:
    Answer:"""

    ZENDESK_TEMPLATE_PROMPT = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(system_message_zendesk_template),
            HumanMessagePromptTemplate.from_template(user_prompt_template),
        ]
    )
    custom_prompts[TemplatePromptName.ZENDESK_TEMPLATE_PROMPT] = ZENDESK_TEMPLATE_PROMPT

    system_message_template = "{enforced_system_prompt}"

    template_answer = """
    <draft answer>
    {task}
    <draft answer>
    Stick closely to this draft answer. Assume that the draft answer informations are correct, and do not try to outsmart him/her.
    Respond directly with the message to send to the customer, ready to be sent:

    Answer:
    """
    ZENDESK_LLM_PROMPT = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(system_message_template),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template(template_answer),
        ]
    )
    custom_prompts[TemplatePromptName.ZENDESK_LLM_PROMPT] = ZENDESK_LLM_PROMPT

    return custom_prompts


_templ_registry: dict[TemplatePromptName, BasePromptTemplate] = _define_custom_prompts()

custom_prompts = types.MappingProxyType(_templ_registry)
```

## File: `core/quivr_core/rag/quivr_rag.py`
```python
import logging
from operator import itemgetter
from typing import AsyncGenerator, Optional, Sequence

# TODO(@aminediro): this is the only dependency to langchain package, we should remove it
from langchain.retrievers import ContextualCompressionRetriever
from langchain_core.callbacks import Callbacks
from langchain_core.documents import BaseDocumentCompressor, Document
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.messages.ai import AIMessageChunk
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.vectorstores import VectorStore

from quivr_core.llm import LLMEndpoint
from quivr_core.rag.entities.chat import ChatHistory
from quivr_core.rag.entities.config import RetrievalConfig
from quivr_core.rag.entities.models import (
    ParsedRAGChunkResponse,
    ParsedRAGResponse,
    QuivrKnowledge,
    RAGResponseMetadata,
    cited_answer,
)
from quivr_core.rag.prompts import TemplatePromptName, custom_prompts
from quivr_core.rag.utils import (
    LangfuseService,
    combine_documents,
    format_file_list,
    get_chunk_metadata,
    parse_chunk_response,
    parse_response,
)

logger = logging.getLogger("quivr_core")
langfuse_service = LangfuseService()
langfuse_handler = langfuse_service.get_handler()


class IdempotentCompressor(BaseDocumentCompressor):
    def compress_documents(
        self,
        documents: Sequence[Document],
        query: str,
        callbacks: Optional[Callbacks] = None,
    ) -> Sequence[Document]:
        return documents


class QuivrQARAG:
    """
    QuivrQA RAG is a class that provides a RAG interface to the QuivrQA system.
    """

    def __init__(
        self,
        *,
        retrieval_config: RetrievalConfig,
        llm: LLMEndpoint,
        vector_store: VectorStore,
        reranker: BaseDocumentCompressor | None = None,
    ):
        self.retrieval_config = retrieval_config
        self.vector_store = vector_store
        self.llm_endpoint = llm
        self.reranker = reranker if reranker is not None else IdempotentCompressor()

    @property
    def retriever(self):
        """
        Retriever is a function that retrieves the documents from the vector store.
        """
        return self.vector_store.as_retriever()

    def filter_history(
        self,
        chat_history: ChatHistory,
    ):
        """
        Filter out the chat history to only include the messages that are relevant to the current question

        Takes in a chat_history= [HumanMessage(content='Qui est Chloé ? '), AIMessage(content="Chloé est une salariée travaillant pour l'entreprise Quivr en tant qu'AI Engineer, sous la direction de son supérieur hiérarchique, Stanislas Girard."), HumanMessage(content='Dis moi en plus sur elle'), AIMessage(content=''), HumanMessage(content='Dis moi en plus sur elle'), AIMessage(content="Désolé, je n'ai pas d'autres informations sur Chloé à partir des fichiers fournis.")]
        Returns a filtered chat_history with in priority: first max_tokens, then max_history where a Human message and an AI message count as one pair
        a token is 4 characters
        """
        total_tokens = 0
        total_pairs = 0
        filtered_chat_history: list[AIMessage | HumanMessage] = []
        for human_message, ai_message in chat_history.iter_pairs():
            # TODO: replace with tiktoken
            message_tokens = (len(human_message.content) + len(ai_message.content)) // 4
            if (
                total_tokens + message_tokens
                > self.retrieval_config.llm_config.max_output_tokens
                or total_pairs >= self.retrieval_config.max_history
            ):
                break
            filtered_chat_history.append(human_message)
            filtered_chat_history.append(ai_message)
            total_tokens += message_tokens
            total_pairs += 1

        return filtered_chat_history[::-1]

    def build_chain(self, files: str):
        """
        Builds the chain for the QuivrQA RAG.
        """
        compression_retriever = ContextualCompressionRetriever(
            base_compressor=self.reranker, base_retriever=self.retriever
        )

        loaded_memory = RunnablePassthrough.assign(
            chat_history=RunnableLambda(
                lambda x: self.filter_history(x["chat_history"]),
            ),
            question=lambda x: x["question"],
        )

        standalone_question = {
            "standalone_question": {
                "question": lambda x: x["question"],
                "chat_history": itemgetter("chat_history"),
            }
            | custom_prompts[TemplatePromptName.DEFAULT_DOCUMENT_PROMPT]
            | self.llm_endpoint._llm
            | StrOutputParser(),
        }

        # Now we retrieve the documents
        retrieved_documents = {
            "docs": itemgetter("standalone_question") | compression_retriever,
            "question": lambda x: x["standalone_question"],
            "custom_instructions": lambda x: self.retrieval_config.prompt,
        }

        final_inputs = {
            "context": lambda x: combine_documents(x["docs"]),
            "question": itemgetter("question"),
            "custom_instructions": itemgetter("custom_instructions"),
            "files": lambda _: files,  # TODO: shouldn't be here
        }

        # Bind the llm to cited_answer if model supports it
        llm = self.llm_endpoint._llm
        if self.llm_endpoint.supports_func_calling():
            llm = self.llm_endpoint._llm.bind_tools(
                [cited_answer],
                tool_choice="any",
            )

        answer = {
            "answer": final_inputs
            | custom_prompts[TemplatePromptName.RAG_ANSWER_PROMPT]
            | llm,
            "docs": itemgetter("docs"),
        }

        return loaded_memory | standalone_question | retrieved_documents | answer

    def answer(
        self,
        question: str,
        history: ChatHistory,
        list_files: list[QuivrKnowledge],
        metadata: dict[str, str] = {},
    ) -> ParsedRAGResponse:
        """
        Answers a question using the QuivrQA RAG synchronously.
        """
        concat_list_files = format_file_list(
            list_files, self.retrieval_config.max_files
        )
        conversational_qa_chain = self.build_chain(concat_list_files)
        raw_llm_response = conversational_qa_chain.invoke(
            {
                "question": question,
                "chat_history": history,
                "custom_instructions": (self.retrieval_config.prompt),
            },
            config={"metadata": metadata, "callbacks": [langfuse_handler]},
        )
        response = parse_response(
            raw_llm_response, self.retrieval_config.llm_config.model
        )
        return response

    async def answer_astream(
        self,
        question: str,
        history: ChatHistory,
        list_files: list[QuivrKnowledge],
        metadata: dict[str, str] = {},
    ) -> AsyncGenerator[ParsedRAGChunkResponse, ParsedRAGChunkResponse]:
        """
        Answers a question using the QuivrQA RAG asynchronously.
        """
        concat_list_files = format_file_list(
            list_files, self.retrieval_config.max_files
        )
        conversational_qa_chain = self.build_chain(concat_list_files)

        rolling_message = AIMessageChunk(content="")
        sources = []
        prev_answer = ""
        chunk_id = 0

        async for chunk in conversational_qa_chain.astream(
            {
                "question": question,
                "chat_history": history,
                "custom_personality": (self.retrieval_config.prompt),
            },
            config={"metadata": metadata, "callbacks": [langfuse_handler]},
        ):
            # Could receive this anywhere so we need to save it for the last chunk
            if "docs" in chunk:
                sources = chunk["docs"] if "docs" in chunk else []

            if "answer" in chunk:
                rolling_message, answer_str = parse_chunk_response(
                    rolling_message,
                    chunk,
                    self.llm_endpoint.supports_func_calling(),
                )

                if len(answer_str) > 0:
                    if self.llm_endpoint.supports_func_calling():
                        diff_answer = answer_str[len(prev_answer) :]
                        if len(diff_answer) > 0:
                            parsed_chunk = ParsedRAGChunkResponse(
                                answer=diff_answer,
                                metadata=RAGResponseMetadata(),
                            )
                            prev_answer += diff_answer

                            logger.debug(
                                f"answer_astream func_calling=True question={question} rolling_msg={rolling_message} chunk_id={chunk_id}, chunk={parsed_chunk}"
                            )
                            yield parsed_chunk
                    else:
                        parsed_chunk = ParsedRAGChunkResponse(
                            answer=answer_str,
                            metadata=RAGResponseMetadata(),
                        )
                        logger.debug(
                            f"answer_astream func_calling=False question={question} rolling_msg={rolling_message} chunk_id={chunk_id}, chunk={parsed_chunk}"
                        )
                        yield parsed_chunk

                    chunk_id += 1

        # Last chunk provides metadata
        last_chunk = ParsedRAGChunkResponse(
            answer="",
            metadata=get_chunk_metadata(rolling_message, sources),
            last_chunk=True,
        )
        logger.debug(
            f"answer_astream last_chunk={last_chunk} question={question} rolling_msg={rolling_message} chunk_id={chunk_id}"
        )
        yield last_chunk
```

## File: `core/quivr_core/rag/quivr_rag_langgraph.py`
```python
import asyncio
import datetime
import logging
from collections import OrderedDict
from typing import (
    Annotated,
    Any,
    AsyncGenerator,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypedDict,
)
from uuid import UUID, uuid4

import openai
from langchain.retrievers import ContextualCompressionRetriever
from langchain_cohere import CohereRerank
from langchain_community.document_compressors import JinaRerank
from langchain_core.callbacks import Callbacks
from langchain_core.documents import BaseDocumentCompressor, Document
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_core.messages.ai import AIMessageChunk
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.prompts.base import BasePromptTemplate
from langchain_core.runnables.schema import StreamEvent
from langchain_core.vectorstores import VectorStore
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.types import Send
from pydantic import BaseModel, Field

from quivr_core.llm import LLMEndpoint
from quivr_core.llm_tools.llm_tools import LLMToolFactory
from quivr_core.rag.entities.chat import ChatHistory
from quivr_core.rag.entities.config import DefaultRerankers, NodeConfig, RetrievalConfig
from quivr_core.rag.entities.models import (
    LangchainMetadata,
    ParsedRAGChunkResponse,
    QuivrKnowledge,
    RAGResponseMetadata,
)
from quivr_core.rag.prompts import TemplatePromptName, custom_prompts
from quivr_core.rag.utils import (
    LangfuseService,
    collect_tools,
    combine_documents,
    format_dict,
    format_file_list,
    get_chunk_metadata,
    parse_chunk_response,
)

logger = logging.getLogger("quivr_core")

langfuse_service = LangfuseService()
langfuse_handler = langfuse_service.get_handler()


class SplittedInput(BaseModel):
    instructions_reasoning: Optional[str] = Field(
        default=None,
        description="The reasoning that leads to identifying the user instructions to the system",
    )
    instructions: Optional[str] = Field(
        default=None, description="The instructions to the system"
    )

    tasks_reasoning: Optional[str] = Field(
        default=None,
        description="The reasoning that leads to identifying the explicit or implicit user tasks and questions",
    )
    task_list: Optional[List[str]] = Field(
        default_factory=lambda: ["No explicit or implicit tasks found"],
        description="The list of standalone, self-contained tasks or questions.",
    )


class TasksCompletion(BaseModel):
    is_task_completable_reasoning: Optional[str] = Field(
        default=None,
        description="The reasoning that leads to identifying whether the user task or question can be completed using the provided context and chat history BEFORE any tool is used.",
    )

    is_task_completable: bool = Field(
        description="Whether the user task or question can be completed using the provided context and chat history BEFORE any tool is used.",
    )

    tool_reasoning: Optional[str] = Field(
        default=None,
        description="The reasoning that leads to identifying the tool that shall be used to complete the task.",
    )
    tool: Optional[str] = Field(
        description="The tool that shall be used to complete the task.",
    )


class FinalAnswer(BaseModel):
    reasoning_answer: str = Field(
        description="The step-by-step reasoning that led to the final answer"
    )
    answer: str = Field(description="The final answer to the user tasks/questions")

    all_tasks_completed: bool = Field(
        description="Whether all tasks/questions have been successfully answered/completed or not. "
        " If the final answer to the user is 'I don't know' or 'I don't have enough information' or 'I'm not sure', "
        " this variable should be 'false'"
    )


class UpdatedPromptAndTools(BaseModel):
    prompt_reasoning: Optional[str] = Field(
        default=None,
        description="The step-by-step reasoning that leads to the updated system prompt",
    )
    prompt: Optional[str] = Field(default=None, description="The updated system prompt")

    tools_reasoning: Optional[str] = Field(
        default=None,
        description="The reasoning that leads to activating and deactivating the tools",
    )
    tools_to_activate: Optional[List[str]] = Field(
        default_factory=list, description="The list of tools to activate"
    )
    tools_to_deactivate: Optional[List[str]] = Field(
        default_factory=list, description="The list of tools to deactivate"
    )


class UserTaskEntity(BaseModel):
    id: UUID
    definition: str
    docs: List[Document] = Field(default_factory=list)
    completable: bool = Field(
        default=False, description="Whether the task has been completed or not"
    )
    tool: Optional[str] = Field(
        default=None, description="The tool that shall be used to complete the task"
    )

    def has_tool(self) -> bool:
        return bool(self.tool)

    def is_completable(self) -> bool:
        return self.completable


class UserTasks:
    def __init__(self, task_definitions: List[str] | None = None):
        self.user_tasks = {}
        if task_definitions:
            for definition in task_definitions:
                id = uuid4()
                self.user_tasks[id] = UserTaskEntity(
                    id=id, definition=definition, docs=[]
                )

    def __iter__(self):
        return iter(self.user_tasks.values())

    def set_docs(self, id: UUID, docs: List[Document]):
        if self.user_tasks:
            if id in self.user_tasks:
                self.user_tasks[id].docs = docs
            else:
                raise ValueError(f"Task with id {id} not found")

    def set_definition(self, id: UUID, definition: str):
        if self.user_tasks:
            if id in self.user_tasks:
                self.user_tasks[id].definition = definition
            else:
                raise ValueError(f"Task with id {id} not found")

    def set_completion(self, id: UUID, completable: bool):
        if self.user_tasks:
            if id in self.user_tasks:
                self.user_tasks[id].completable = completable
            else:
                raise ValueError(f"Task with id {id} not found")

    def set_tool(self, id: UUID, tool: str):
        if self.user_tasks:
            if id in self.user_tasks:
                self.user_tasks[id].tool = tool
            else:
                raise ValueError(f"Task with id {id} not found")

    def __call__(self, id: UUID) -> UserTaskEntity:
        return self.user_tasks[id]

    def has_tasks(self) -> bool:
        return bool(self.user_tasks)

    def has_non_completable_tasks(self) -> bool:
        return bool(self.non_completable_tasks)

    @property
    def non_completable_tasks(self) -> List[UserTaskEntity]:
        return [task for task in self.user_tasks.values() if not task.is_completable()]

    @property
    def completable_tasks(self) -> List[UserTaskEntity]:
        return [task for task in self.user_tasks.values() if task.is_completable()]

    @property
    def ids(self) -> List[UUID]:
        return list(self.user_tasks.keys())

    @property
    def definitions(self) -> List[str]:
        return [task.definition for task in self.user_tasks.values()]

    @property
    def docs(self) -> List[Document]:
        # Return the concatenation of all docs
        return [doc for task in self.user_tasks.values() for doc in task.docs]


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    reasoning: List[str]
    chat_history: ChatHistory
    files: str
    tasks: UserTasks
    instructions: str
    ticket_metadata: Optional[dict[str, str]]
    user_metadata: Optional[dict[str, str]]
    additional_information: Optional[dict[str, str]]
    tool: str
    guidelines: str
    enforced_system_prompt: str
    _filter: Optional[Dict[str, Any]]
    ticket_history: str


class IdempotentCompressor(BaseDocumentCompressor):
    def compress_documents(
        self,
        documents: Sequence[Document],
        query: str,
        callbacks: Optional[Callbacks] = None,
    ) -> Sequence[Document]:
        """
        A no-op document compressor that simply returns the documents it is given.

        This is a placeholder until a more sophisticated document compression
        algorithm is implemented.
        """
        return documents


class QuivrQARAGLangGraph:
    def __init__(
        self,
        *,
        retrieval_config: RetrievalConfig,
        llm: LLMEndpoint,
        vector_store: VectorStore | None = None,
    ):
        """
        Construct a QuivrQARAGLangGraph object.

        Args:
            retrieval_config (RetrievalConfig): The configuration for the RAG model.
            llm (LLMEndpoint): The LLM to use for generating text.
            vector_store (VectorStore): The vector store to use for storing and retrieving documents.
            reranker (BaseDocumentCompressor | None): The document compressor to use for re-ranking documents. Defaults to IdempotentCompressor if not provided.
        """
        self.retrieval_config = retrieval_config
        self.vector_store = vector_store
        self.llm_endpoint = llm

        self.graph = None

    def get_reranker(self, **kwargs):
        # Extract the reranker configuration from self
        config = self.retrieval_config.reranker_config

        # Allow kwargs to override specific config values
        supplier = kwargs.pop("supplier", config.supplier)
        model = kwargs.pop("model", config.model)
        top_n = kwargs.pop("top_n", config.top_n)
        api_key = kwargs.pop("api_key", config.api_key)

        if supplier == DefaultRerankers.COHERE:
            reranker = CohereRerank(
                model=model, top_n=top_n, cohere_api_key=api_key, **kwargs
            )
        elif supplier == DefaultRerankers.JINA:
            reranker = JinaRerank(
                model=model, top_n=top_n, jina_api_key=api_key, **kwargs
            )
        else:
            reranker = IdempotentCompressor()

        return reranker

    def get_retriever(self, **kwargs):
        """
        Returns a retriever that can retrieve documents from the vector store.

        Returns:
            VectorStoreRetriever: The retriever.
        """
        if self.vector_store:
            retriever = self.vector_store.as_retriever(**kwargs)
        else:
            raise ValueError("No vector store provided")

        return retriever

    def routing(self, state: AgentState) -> List[Send]:
        """
        The routing function for the RAG model.

        Args:
            state (AgentState): The current state of the agent.

        Returns:
            dict: The next state of the agent.
        """

        msg = custom_prompts[TemplatePromptName.SPLIT_PROMPT].format(
            user_input=state["messages"][0].content,
        )

        response: SplittedInput

        try:
            structured_llm = self.llm_endpoint._llm.with_structured_output(
                SplittedInput, method="json_schema"
            )
            response = structured_llm.invoke(msg)

        except openai.BadRequestError:
            structured_llm = self.llm_endpoint._llm.with_structured_output(
                SplittedInput
            )
            response = structured_llm.invoke(msg)

        send_list: List[Send] = []

        instructions = (
            response.instructions
            if response.instructions
            else self.retrieval_config.prompt
        )

        if instructions:
            send_list.append(Send("edit_system_prompt", {"instructions": instructions}))
        elif response.task_list:
            chat_history = state["chat_history"]
            send_list.append(
                Send(
                    "filter_history",
                    {
                        "chat_history": chat_history,
                        "tasks": UserTasks(response.task_list),
                    },
                )
            )

        return send_list

    def routing_split(self, state: AgentState):
        response: SplittedInput = self.invoke_structured_output(
            custom_prompts[TemplatePromptName.SPLIT_PROMPT].format(
                chat_history=state["chat_history"].to_list(),
                user_input=state["messages"][0].content,
            ),
            SplittedInput,
        )

        instructions = response.instructions or self.retrieval_config.prompt
        tasks = UserTasks(response.task_list) if response.task_list else None

        if instructions:
            return [
                Send(
                    "edit_system_prompt",
                    {**state, "instructions": instructions, "tasks": tasks},
                )
            ]
        elif tasks:
            return [Send("filter_history", {**state, "tasks": tasks})]

        return []

    def update_active_tools(self, updated_prompt_and_tools: UpdatedPromptAndTools):
        if updated_prompt_and_tools.tools_to_activate:
            for tool in updated_prompt_and_tools.tools_to_activate:
                for (
                    validated_tool
                ) in self.retrieval_config.workflow_config.validated_tools:
                    if tool == validated_tool.name:
                        self.retrieval_config.workflow_config.activated_tools.append(
                            validated_tool
                        )

        if updated_prompt_and_tools.tools_to_deactivate:
            for tool in updated_prompt_and_tools.tools_to_deactivate:
                for (
                    activated_tool
                ) in self.retrieval_config.workflow_config.activated_tools:
                    if tool == activated_tool.name:
                        self.retrieval_config.workflow_config.activated_tools.remove(
                            activated_tool
                        )

    def edit_system_prompt(self, state: AgentState) -> AgentState:
        user_instruction = state["instructions"]
        prompt = self.retrieval_config.prompt
        available_tools, activated_tools = collect_tools(
            self.retrieval_config.workflow_config
        )
        inputs = {
            "instruction": user_instruction,
            "system_prompt": prompt if prompt else "",
            "available_tools": available_tools,
            "activated_tools": activated_tools,
        }

        msg = custom_prompts[TemplatePromptName.UPDATE_PROMPT].format(**inputs)

        response: UpdatedPromptAndTools = self.invoke_structured_output(
            msg, UpdatedPromptAndTools
        )

        self.update_active_tools(response)
        self.retrieval_config.prompt = response.prompt

        reasoning = [response.prompt_reasoning] if response.prompt_reasoning else []
        reasoning += [response.tools_reasoning] if response.tools_reasoning else []

        return {**state, "messages": [], "reasoning": reasoning}

    def filter_history(self, state: AgentState) -> AgentState:
        """
        Filter out the chat history to only include the messages that are relevant to the current question

        Takes in a chat_history= [HumanMessage(content='Qui est Chloé ? '),
        AIMessage(content="Chloé est une salariée travaillant pour l'entreprise Quivr en tant qu'AI Engineer,
        sous la direction de son supérieur hiérarchique, Stanislas Girard."),
        HumanMessage(content='Dis moi en plus sur elle'), AIMessage(content=''),
        HumanMessage(content='Dis moi en plus sur elle'),
        AIMessage(content="Désolé, je n'ai pas d'autres informations sur Chloé à partir des fichiers fournis.")]
        Returns a filtered chat_history with in priority: first max_tokens, then max_history where a Human message and an AI message count as one pair
        a token is 4 characters
        """

        chat_history = state["chat_history"]
        total_tokens = 0
        total_pairs = 0
        _chat_id = uuid4()
        _chat_history = ChatHistory(chat_id=_chat_id, brain_id=chat_history.brain_id)
        for human_message, ai_message in reversed(list(chat_history.iter_pairs())):
            # TODO: replace with tiktoken
            message_tokens = self.llm_endpoint.count_tokens(
                human_message.content
            ) + self.llm_endpoint.count_tokens(ai_message.content)

            if (
                total_tokens + message_tokens
                > self.retrieval_config.llm_config.max_context_tokens
                or total_pairs >= self.retrieval_config.max_history
            ):
                break
            _chat_history.append(human_message)
            _chat_history.append(ai_message)
            total_tokens += message_tokens
            total_pairs += 1

        return {**state, "chat_history": _chat_history}

    async def rewrite(self, state: AgentState) -> AgentState:
        """
        Transform the query to produce a better question.

        Args:
            state (messages): The current state

        Returns:
            dict: The updated state with re-phrased question
        """

        if "tasks" in state and state["tasks"]:
            tasks = state["tasks"]
        else:
            tasks = UserTasks([state["messages"][0].content])

        # Prepare the async tasks for all user tsks
        async_jobs = []
        for task_id in tasks.ids:
            msg = custom_prompts[TemplatePromptName.CONDENSE_TASK_PROMPT].format(
                chat_history=state["chat_history"].to_list(),
                task=tasks(task_id).definition,
            )

            model = self.llm_endpoint._llm
            # Asynchronously invoke the model for each question
            async_jobs.append((model.ainvoke(msg), task_id))

        # Gather all the responses asynchronously
        responses = (
            await asyncio.gather(*(jobs[0] for jobs in async_jobs))
            if async_jobs
            else []
        )
        task_ids = [jobs[1] for jobs in async_jobs] if async_jobs else []

        # Replace each question with its condensed version
        for response, task_id in zip(responses, task_ids, strict=False):
            tasks.set_definition(task_id, response.content)

        return {**state, "tasks": tasks}

    def filter_chunks_by_relevance(self, chunks: List[Document], **kwargs):
        config = self.retrieval_config.reranker_config
        relevance_score_threshold = kwargs.get(
            "relevance_score_threshold", config.relevance_score_threshold
        )

        if relevance_score_threshold is None:
            return chunks

        filtered_chunks = []
        for chunk in chunks:
            if config.relevance_score_key not in chunk.metadata:
                logger.warning(
                    f"Relevance score key {config.relevance_score_key} not found in metadata, cannot filter chunks by relevance"
                )
                filtered_chunks.append(chunk)
            elif (
                chunk.metadata[config.relevance_score_key] >= relevance_score_threshold
            ):
                filtered_chunks.append(chunk)

        return filtered_chunks

    async def tool_routing(self, state: AgentState):
        tasks = state["tasks"]
        if not tasks.has_tasks():
            return [Send("generate_rag", state)]

        validated_tools, _ = collect_tools(self.retrieval_config.workflow_config)

        async_jobs = []
        for task_id in tasks.ids:
            input = {
                "chat_history": state["chat_history"].to_list(),
                "tasks": tasks(task_id).definition,
                "context": combine_documents(tasks(task_id).docs),
                "activated_tools": validated_tools,
            }

            msg = custom_prompts[TemplatePromptName.TOOL_ROUTING_PROMPT].format(**input)
            async_jobs.append(
                (self.ainvoke_structured_output(msg, TasksCompletion), task_id)
            )

        responses: List[TasksCompletion] = (
            await asyncio.gather(*(jobs[0] for jobs in async_jobs))
            if async_jobs
            else []
        )
        task_ids = [jobs[1] for jobs in async_jobs] if async_jobs else []

        for response, task_id in zip(responses, task_ids, strict=False):
            tasks.set_completion(task_id, response.is_task_completable)
            if not response.is_task_completable and response.tool:
                tasks.set_tool(task_id, response.tool)

        send_list: List[Send] = []

        payload = {**state, "tasks": tasks}

        if tasks.has_non_completable_tasks():
            send_list.append(Send("run_tool", payload))
        else:
            send_list.append(Send("generate_rag", payload))

        return send_list

    async def run_tool(self, state: AgentState) -> AgentState:
        # if tool not in [
        #     t.name for t in self.retrieval_config.workflow_config.activated_tools
        # ]:
        #     raise ValueError(f"Tool {tool} not activated")

        tasks = state["tasks"]

        # Prepare the async tasks for all questions
        async_jobs = []
        for task_id in tasks.ids:
            if not tasks(task_id).is_completable() and tasks(task_id).has_tool():
                tool = tasks(task_id).tool
                tool_wrapper = LLMToolFactory.create_tool(tool, {})
                formatted_input = tool_wrapper.format_input(tasks(task_id).definition)
                async_jobs.append((tool_wrapper.tool.ainvoke(formatted_input), task_id))

        # Gather all the responses asynchronously
        responses = (
            await asyncio.gather(*(jobs[0] for jobs in async_jobs))
            if async_jobs
            else []
        )
        task_ids = [jobs[1] for jobs in async_jobs] if async_jobs else []

        for response, task_id in zip(responses, task_ids, strict=False):
            _docs = tool_wrapper.format_output(response)
            _docs = self.filter_chunks_by_relevance(_docs)
            tasks.set_docs(task_id, _docs)

        return {**state, "tasks": tasks}

    async def retrieve(self, state: AgentState) -> AgentState:
        """
        Retrieve relevent chunks

        Args:
            state (messages): The current state

        Returns:
            dict: The retrieved chunks
        """
        if "tasks" in state:
            tasks = state["tasks"]
        else:
            tasks = UserTasks([state["messages"][0].content])

        if not tasks.has_tasks():
            return {**state}

        _filter = state.get("_filter", None)

        kwargs = {
            "search_kwargs": {
                "k": self.retrieval_config.k,
                "filter": _filter,  # Add your desired filter here
            }
        }  # type: ignore
        base_retriever = self.get_retriever(**kwargs)

        kwargs = {"top_n": self.retrieval_config.reranker_config.top_n}  # type: ignore
        reranker = self.get_reranker(**kwargs)

        compression_retriever = ContextualCompressionRetriever(
            base_compressor=reranker, base_retriever=base_retriever
        )

        # Prepare the async tasks for all questions
        async_jobs = []
        for task_id in tasks.ids:
            # Create a tuple of the retrieval task and task_id
            async_jobs.append(
                (compression_retriever.ainvoke(tasks(task_id).definition), task_id)
            )

        # Gather all the responses asynchronously
        responses = (
            await asyncio.gather(*(task[0] for task in async_jobs))
            if async_jobs
            else []
        )
        task_ids = [task[1] for task in async_jobs] if async_jobs else []

        # Process responses and associate docs with tasks
        for response, task_id in zip(responses, task_ids, strict=False):
            _docs = self.filter_chunks_by_relevance(response)
            tasks.set_docs(task_id, _docs)  # Associate docs with the specific task

        return {**state, "tasks": tasks}

    async def dynamic_retrieve(self, state: AgentState) -> AgentState:
        """
        Retrieve relevent chunks

        Args:
            state (messages): The current state

        Returns:
            dict: The retrieved chunks
        """

        MAX_ITERATIONS = 3

        if "tasks" in state:
            tasks = state["tasks"]
        else:
            tasks = UserTasks([state["messages"][0].content])

        if not tasks or not tasks.has_tasks():
            return {**state}

        k = self.retrieval_config.k
        top_n = self.retrieval_config.reranker_config.top_n
        number_of_relevant_chunks = top_n
        i = 1

        while number_of_relevant_chunks == top_n and i <= MAX_ITERATIONS:
            top_n = self.retrieval_config.reranker_config.top_n * i
            kwargs = {"top_n": top_n}
            reranker = self.get_reranker(**kwargs)

            k = max([top_n * 2, self.retrieval_config.k])
            kwargs = {"search_kwargs": {"k": k}}  # type: ignore
            base_retriever = self.get_retriever(**kwargs)

            if i > 1:
                logging.info(
                    f"Increasing top_n to {top_n} and k to {k} to retrieve more relevant chunks"
                )

            compression_retriever = ContextualCompressionRetriever(
                base_compressor=reranker, base_retriever=base_retriever
            )

            # Prepare the async tasks for all questions
            async_jobs = []
            for task_id in tasks.ids:
                # Asynchronously invoke the model for each question
                async_jobs.append(
                    (compression_retriever.ainvoke(tasks(task_id).definition), task_id)
                )

            # Gather all the responses asynchronously
            responses = (
                await asyncio.gather(*(jobs[0] for jobs in async_jobs))
                if async_jobs
                else []
            )
            task_ids = [jobs[1] for jobs in async_jobs] if async_jobs else []

            _n = []
            for response, task_id in zip(responses, task_ids, strict=False):
                _docs = self.filter_chunks_by_relevance(response)
                _n.append(len(_docs))
                tasks.set_docs(task_id, _docs)

            docs = tasks.docs
            if not docs:
                break

            context_length = self.get_rag_context_length(state, docs)
            if context_length >= self.retrieval_config.llm_config.max_context_tokens:
                logging.warning(
                    f"The context length is {context_length} which is greater than "
                    f"the max context tokens of {self.retrieval_config.llm_config.max_context_tokens}"
                )
                break

            number_of_relevant_chunks = max(_n)
            i += 1

        return {**state, "tasks": tasks}

    def _sort_docs_by_relevance(self, docs: List[Document]) -> List[Document]:
        return sorted(
            docs,
            key=lambda x: x.metadata[
                self.retrieval_config.reranker_config.relevance_score_key
            ],
            reverse=True,
        )

    async def retrieve_full_documents_context(self, state: AgentState) -> AgentState:
        if "tasks" in state:
            tasks = state["tasks"]
        else:
            tasks = UserTasks([state["messages"][0].content])

        if not tasks.has_tasks():
            return {**state}

        docs = tasks.docs if tasks else []

        relevant_knowledge: Dict[str, Dict[str, Any]] = {}
        for doc in docs:
            knowledge_id = doc.metadata["knowledge_id"]
            similarity_score = doc.metadata.get("similarity", 0)
            if knowledge_id in relevant_knowledge:
                relevant_knowledge[knowledge_id]["count"] += 1
                relevant_knowledge[knowledge_id]["max_similarity_score"] = max(
                    relevant_knowledge[knowledge_id]["max_similarity_score"],
                    similarity_score,
                )
                relevant_knowledge[knowledge_id]["chunk_index"] = max(
                    doc.metadata["chunk_index"],
                    relevant_knowledge[knowledge_id]["chunk_index"],
                )
            else:
                relevant_knowledge[knowledge_id] = {
                    "count": 1,
                    "max_similarity_score": similarity_score,
                    "chunk_index": doc.metadata["chunk_index"],
                }

        top_n = min(3, len(relevant_knowledge))
        # FIXME: Tweak this to return the most relevant knowledges
        top_knowledge_ids = OrderedDict(
            sorted(
                relevant_knowledge.items(),
                key=lambda x: (
                    x[1]["max_similarity_score"],
                    x[1]["count"],
                ),
                reverse=True,
            )[:top_n]
        )

        logger.info(f"Top knowledge IDs: {top_knowledge_ids}")

        _docs = []

        assert hasattr(
            self.vector_store, "get_vectors_by_knowledge_id"
        ), "Vector store must have method 'get_vectors_by_knowledge_id', this is an enterprise only feature"

        for knowledge_id in top_knowledge_ids:
            _docs.append(
                await self.vector_store.get_vectors_by_knowledge_id(  # type: ignore
                    knowledge_id,
                    end_index=relevant_knowledge[knowledge_id]["chunk_index"],
                )
            )

        tasks.set_docs(
            id=tasks.ids[0], docs=_docs
        )  # FIXME If multiple IDs is not handled.

        return {**state, "tasks": tasks}

    def get_rag_context_length(self, state: AgentState, docs: List[Document]) -> int:
        final_inputs = self._build_rag_prompt_inputs(state, docs)
        msg = custom_prompts[TemplatePromptName.RAG_ANSWER_PROMPT].format(
            **final_inputs
        )
        return self.llm_endpoint.count_tokens(msg)

    def reduce_rag_context(
        self,
        state: AgentState,
        inputs: Dict[str, Any],
        prompt: BasePromptTemplate,
        max_context_tokens: int | None = None,
    ) -> Tuple[AgentState, Dict[str, Any]]:
        MAX_ITERATIONS = 20
        SECURITY_FACTOR = 0.85
        iteration = 0

        tasks = state["tasks"] if "tasks" in state else None
        docs = tasks.docs if tasks else []
        msg = prompt.format(**inputs)
        n = self.llm_endpoint.count_tokens(msg)

        max_context_tokens = (
            max_context_tokens
            if max_context_tokens
            else self.retrieval_config.llm_config.max_context_tokens
        )

        # Get token counts for each doc in each task
        if tasks:
            task_token_counts = {}
            for task_id in tasks.ids:
                doc_tokens = [
                    self.llm_endpoint.count_tokens(doc.page_content)
                    for doc in tasks(task_id).docs
                ]
                task_token_counts[task_id] = {
                    "docs": doc_tokens,
                    "total": sum(doc_tokens),
                }

        while n > max_context_tokens * SECURITY_FACTOR:
            chat_history = inputs["chat_history"] if "chat_history" in inputs else []

            if len(chat_history) > 0:
                inputs["chat_history"] = chat_history[2:]
            elif tasks:
                longest_task_id = max(
                    task_token_counts.items(), key=lambda x: x[1]["total"]
                )[0]

                # Remove last doc from that task
                if task_token_counts[longest_task_id]["docs"]:
                    removed_tokens = task_token_counts[longest_task_id]["docs"].pop()
                    task_token_counts[longest_task_id]["total"] -= removed_tokens
                    tasks.set_docs(longest_task_id, tasks(longest_task_id).docs[:-1])
            else:
                logging.warning(
                    f"Not enough context to reduce. The context length is {n} "
                    f"which is greater than the max context tokens of {max_context_tokens}"
                )
                break

            docs = tasks.docs if tasks else []
            inputs["context"] = combine_documents(docs)

            msg = prompt.format(**inputs)
            n = self.llm_endpoint.count_tokens(msg)

            iteration += 1
            if iteration > MAX_ITERATIONS:
                logging.warning(
                    f"Attained the maximum number of iterations ({MAX_ITERATIONS})"
                )
                break

        return {**state, "tasks": tasks}, inputs

    def bind_tools_to_llm(self, node_name: str):
        if self.llm_endpoint.supports_func_calling():
            tools = self.retrieval_config.workflow_config.get_node_tools(node_name)
            if tools:  # Only bind tools if there are any available
                return self.llm_endpoint._llm.bind_tools(tools, tool_choice="any")
        return self.llm_endpoint._llm

    def generate_zendesk_rag(self, state: AgentState) -> AgentState:
        tasks = state["tasks"]
        docs: List[Document] = tasks.docs if tasks else []
        messages = state["messages"]
        user_task = messages[0].content
        prompt_template: BasePromptTemplate = custom_prompts[
            TemplatePromptName.ZENDESK_TEMPLATE_PROMPT
        ]

        ticket_metadata = state["ticket_metadata"] or {}
        user_metadata = state["user_metadata"] or {}
        ticket_history = state.get("ticket_history", "")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        inputs = {
            "similar_tickets": "\n".join([doc.page_content for doc in docs]),
            "ticket_metadata": format_dict(ticket_metadata),
            "user_metadata": format_dict(user_metadata),
            "client_query": user_task,
            "ticket_history": ticket_history,
            "current_time": current_time,
        }
        required_variables = prompt_template.input_variables
        for variable in required_variables:
            if variable not in inputs:
                inputs[variable] = state.get(variable, "")

        msg = prompt_template.format_prompt(**inputs)
        llm = self.bind_tools_to_llm(self.generate_zendesk_rag.__name__)

        response = llm.invoke(msg)

        return {**state, "messages": [response]}

    def generate_rag(self, state: AgentState) -> AgentState:
        tasks = state["tasks"]
        docs = tasks.docs if tasks else []
        inputs = self._build_rag_prompt_inputs(state, docs)
        prompt = custom_prompts[TemplatePromptName.RAG_ANSWER_PROMPT]
        state, inputs = self.reduce_rag_context(state, inputs, prompt)
        msg = prompt.format(**inputs)
        llm = self.bind_tools_to_llm(self.generate_rag.__name__)
        response = llm.invoke(msg)

        return {**state, "messages": [response]}

    def generate_chat_llm(self, state: AgentState) -> AgentState:
        """
        Generate answer

        Args:
            state (messages): The current state

        Returns:
            dict: The updated state with re-phrased question
        """
        messages = state["messages"]

        # Check if there is a system message in messages
        system_message = None
        user_message = None

        for msg in messages:
            if isinstance(msg, SystemMessage):
                system_message = str(msg.content)
            elif isinstance(msg, HumanMessage):
                user_message = str(msg.content)

        user_task = (
            user_message if user_message else (messages[0].content if messages else "")
        )

        # Prompt
        prompt = self.retrieval_config.prompt

        final_inputs = {}
        final_inputs["task"] = user_task
        final_inputs["custom_instructions"] = prompt if prompt else "None"
        final_inputs["chat_history"] = state["chat_history"].to_list()

        # LLM
        llm = self.llm_endpoint._llm

        prompt = custom_prompts[TemplatePromptName.CHAT_LLM_PROMPT]
        state, reduced_inputs = self.reduce_rag_context(
            state, final_inputs, system_message if system_message else prompt
        )
        CHAT_LLM_PROMPT = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=str(system_message)),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessage(content=str(user_message)),
            ]
        )
        # Run
        chat_llm_prompt = CHAT_LLM_PROMPT.invoke(
            {"chat_history": final_inputs["chat_history"]}
        )
        response = llm.invoke(chat_llm_prompt)
        return {**state, "messages": [response]}

    def build_chain(self):
        """
        Builds the langchain chain for the given configuration.

        Returns:
            Callable[[Dict], Dict]: The langchain chain.
        """
        if not self.graph:
            self.graph = self.create_graph()

        return self.graph

    def create_graph(self):
        workflow = StateGraph(AgentState)
        self.final_nodes = []

        self._build_workflow(workflow)

        return workflow.compile()

    def _build_workflow(self, workflow: StateGraph):
        for node in self.retrieval_config.workflow_config.nodes:
            if node.name not in [START, END]:
                workflow.add_node(node.name, getattr(self, node.name))

        for node in self.retrieval_config.workflow_config.nodes:
            self._add_node_edges(workflow, node)

    def _add_node_edges(self, workflow: StateGraph, node: NodeConfig):
        if node.edges:
            for edge in node.edges:
                workflow.add_edge(node.name, edge)
                if edge == END:
                    self.final_nodes.append(node.name)
        elif node.conditional_edge:
            routing_function = getattr(self, node.conditional_edge.routing_function)
            workflow.add_conditional_edges(
                node.name, routing_function, node.conditional_edge.conditions
            )
            if END in node.conditional_edge.conditions:
                self.final_nodes.append(node.name)
        else:
            raise ValueError("Node should have at least one edge or conditional_edge")

    async def answer_astream(
        self,
        run_id: UUID,
        question: str,
        system_prompt: str | None,
        history: ChatHistory,
        list_files: list[QuivrKnowledge],
        metadata: LangchainMetadata | None = None,
        **input_kwargs,
    ) -> AsyncGenerator[ParsedRAGChunkResponse, ParsedRAGChunkResponse]:
        """
        Answer a question using the langgraph chain and yield each chunk of the answer separately.
        """
        concat_list_files = format_file_list(
            list_files, self.retrieval_config.max_files
        )
        conversational_qa_chain = self.build_chain()

        rolling_message = AIMessageChunk(content="")
        docs: list[Document] | None = None
        previous_content = ""
        system_prompt = system_prompt
        messages = [("system", system_prompt)] if system_prompt else []
        messages.append(("user", question))

        async for event in conversational_qa_chain.astream_events(
            {
                "messages": messages,
                "chat_history": history,
                "files": concat_list_files,
                **input_kwargs,
            },
            version="v1",
            config={
                "run_id": run_id,
                "metadata": metadata.model_dump() if metadata else {},
                "callbacks": [langfuse_handler],
            },
        ):
            node_name = self._extract_node_name(event)

            if self._is_final_node_with_docs(event):
                tasks = event["data"]["output"]["tasks"]
                docs = tasks.docs if tasks else []

            if self._is_final_node_and_chat_model_stream(event):
                chunk = event["data"]["chunk"]
                rolling_message, new_content, previous_content = parse_chunk_response(
                    rolling_message,
                    chunk,
                    self.llm_endpoint.supports_func_calling(),
                    previous_content,
                )

                if new_content:
                    chunk_metadata = get_chunk_metadata(rolling_message, docs)
                    if node_name:
                        chunk_metadata.workflow_step = node_name
                    yield ParsedRAGChunkResponse(
                        answer=new_content, metadata=chunk_metadata
                    )
            else:
                if node_name:
                    yield ParsedRAGChunkResponse(
                        answer="",
                        metadata=RAGResponseMetadata(workflow_step=node_name),
                    )

        # Yield final metadata chunk
        chunk_metadata = get_chunk_metadata(rolling_message, docs)
        if metadata:
            chunk_metadata.langchain_metadata = metadata
            chunk_metadata.langchain_metadata.langfuse_trace_url = (
                langfuse_handler.get_trace_url()
            )

        yield ParsedRAGChunkResponse(
            answer="",
            metadata=chunk_metadata,
            last_chunk=True,
        )

    def _is_final_node_with_docs(self, event: StreamEvent) -> bool:
        return (
            "output" in event["data"]
            and event["data"]["output"] is not None
            and "tasks" in event["data"]["output"]
            and event["metadata"]["langgraph_node"] in self.final_nodes
        )

    def _is_final_node_and_chat_model_stream(self, event: StreamEvent) -> bool:
        return (
            event["event"] == "on_chat_model_stream"
            and "langgraph_node" in event["metadata"]
            and event["metadata"]["langgraph_node"] in self.final_nodes
        )

    def _extract_node_name(self, event: StreamEvent) -> str:
        if "metadata" in event and "langgraph_node" in event["metadata"]:
            name = event["metadata"]["langgraph_node"]
            for node in self.retrieval_config.workflow_config.nodes:
                if node.name == name:
                    if node.description:
                        return node.description
                    else:
                        return node.name
        return ""

    async def ainvoke_structured_output(
        self, prompt: str, output_class: Type[BaseModel]
    ) -> Any:
        try:
            structured_llm = self.llm_endpoint._llm.with_structured_output(
                output_class, method="json_schema"
            )
            return await structured_llm.ainvoke(prompt)
        except openai.BadRequestError:
            structured_llm = self.llm_endpoint._llm.with_structured_output(output_class)
            return await structured_llm.ainvoke(prompt)

    def invoke_structured_output(
        self, prompt: str, output_class: Type[BaseModel]
    ) -> Any:
        try:
            structured_llm = self.llm_endpoint._llm.with_structured_output(
                output_class, method="json_schema"
            )
            return structured_llm.invoke(prompt)
        except openai.BadRequestError:
            structured_llm = self.llm_endpoint._llm.with_structured_output(output_class)
            return structured_llm.invoke(prompt)

    def _build_rag_prompt_inputs(
        self, state: AgentState, docs: List[Document] | None
    ) -> Dict[str, Any]:
        """Build the input dictionary for RAG_ANSWER_PROMPT.

        Args:
            state: Current agent state
            docs: List of documents or None

        Returns:
            Dictionary containing all inputs needed for RAG_ANSWER_PROMPT
        """
        messages = state["messages"]
        user_task = messages[0].content
        files = state["files"]
        prompt = self.retrieval_config.prompt
        # available_tools, _ = collect_tools(self.retrieval_config.workflow_config)

        return {
            "context": combine_documents(docs) if docs else "None",
            "task": user_task,
            "rephrased_task": state["tasks"].definitions if state["tasks"] else "None",
            "custom_instructions": prompt if prompt else "None",
            "files": files if files else "None",
            "chat_history": state["chat_history"].to_list(),
            # "reasoning": state["reasoning"] if "reasoning" in state else "None",
            # "tools": available_tools,
        }
```

## File: `core/quivr_core/rag/utils.py`
```python
import logging
from typing import Any, Dict, List, Tuple, no_type_check

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langchain_core.messages.ai import AIMessageChunk
from langchain_core.prompts import format_document
from langfuse.callback import CallbackHandler

from quivr_core.rag.entities.config import WorkflowConfig
from quivr_core.rag.entities.models import (
    ChatLLMMetadata,
    ParsedRAGResponse,
    QuivrKnowledge,
    RAGResponseMetadata,
    RawRAGResponse,
)
from quivr_core.rag.prompts import TemplatePromptName, custom_prompts

# TODO(@aminediro): define a types packages where we clearly define IO types
# This should be used for serialization/deseriallization later


logger = logging.getLogger("quivr_core")


def model_supports_function_calling(model_name: str):
    models_not_supporting_function_calls: list[str] = ["llama2", "test", "ollama3"]

    return model_name not in models_not_supporting_function_calls


def format_history_to_openai_mesages(
    tuple_history: List[Tuple[str, str]], system_message: str, question: str
) -> List[BaseMessage]:
    """Format the chat history into a list of Base Messages"""
    messages = []
    messages.append(SystemMessage(content=system_message))
    for human, ai in tuple_history:
        messages.append(HumanMessage(content=human))
        messages.append(AIMessage(content=ai))
    messages.append(HumanMessage(content=question))
    return messages


def cited_answer_filter(tool):
    return tool["name"] == "cited_answer"


def get_chunk_metadata(
    msg: AIMessageChunk, sources: list[Any] | None = None
) -> RAGResponseMetadata:
    metadata = {"sources": sources or []}

    if not msg.tool_calls:
        return RAGResponseMetadata(**metadata, metadata_model=None)

    all_citations = []
    all_followup_questions = []

    for tool_call in msg.tool_calls:
        if tool_call.get("name") == "cited_answer" and "args" in tool_call:
            args = tool_call["args"]
            all_citations.extend(args.get("citations", []))
            all_followup_questions.extend(args.get("followup_questions", []))

    metadata["citations"] = all_citations
    metadata["followup_questions"] = all_followup_questions[:3]  # Limit to 3

    return RAGResponseMetadata(**metadata, metadata_model=None)


def get_prev_message_str(msg: AIMessageChunk) -> str:
    if msg.tool_calls:
        cited_answer = next(x for x in msg.tool_calls if cited_answer_filter(x))
        if "args" in cited_answer and "answer" in cited_answer["args"]:
            return cited_answer["args"]["answer"]
    return ""


# TODO: CONVOLUTED LOGIC !
# TODO(@aminediro): redo this
@no_type_check
def parse_chunk_response(
    rolling_msg: AIMessageChunk,
    raw_chunk: AIMessageChunk,
    supports_func_calling: bool,
    previous_content: str = "",
) -> Tuple[AIMessageChunk, str, str]:
    """Parse a chunk response
    Args:
        rolling_msg: The accumulated message so far
        raw_chunk: The new chunk to add
        supports_func_calling: Whether function calling is supported
        previous_content: The previous content string
    Returns:
        Tuple of (updated rolling message, new content only, full content)
    """
    rolling_msg += raw_chunk

    tool_calls = rolling_msg.tool_calls

    if not supports_func_calling or not tool_calls:
        new_content = raw_chunk.content  # Just the new chunk's content
        full_content = rolling_msg.content  # The full accumulated content
        return rolling_msg, new_content, full_content

    current_answers = get_answers_from_tool_calls(tool_calls)
    full_answer = "\n\n".join(current_answers)
    if not full_answer:
        full_answer = previous_content

    new_content = full_answer[len(previous_content) :]

    return rolling_msg, new_content, full_answer


def get_answers_from_tool_calls(tool_calls):
    answers = []
    for tool_call in tool_calls:
        if tool_call.get("name") == "cited_answer":
            args = tool_call.get("args", {})
            if isinstance(args, dict):
                answers.append(args.get("answer", ""))
            else:
                logger.warning(f"Expected dict for tool_call args, got {type(args)}")
    return answers


@no_type_check
def parse_response(raw_response: RawRAGResponse, model_name: str) -> ParsedRAGResponse:
    answers = []
    sources = raw_response["docs"] if "docs" in raw_response else []

    metadata = RAGResponseMetadata(
        sources=sources, metadata_model=ChatLLMMetadata(name=model_name)
    )

    if (
        model_supports_function_calling(model_name)
        and "tool_calls" in raw_response["answer"]
        and raw_response["answer"].tool_calls
    ):
        all_citations = []
        all_followup_questions = []
        for tool_call in raw_response["answer"].tool_calls:
            if "args" in tool_call:
                args = tool_call["args"]
                if "citations" in args:
                    all_citations.extend(args["citations"])
                if "followup_questions" in args:
                    all_followup_questions.extend(args["followup_questions"])
                if "answer" in args:
                    answers.append(args["answer"])
        metadata.citations = all_citations
        metadata.followup_questions = all_followup_questions
    else:
        answers.append(raw_response["answer"].content)

    answer_str = "\n".join(answers)
    parsed_response = ParsedRAGResponse(answer=answer_str, metadata=metadata)
    return parsed_response


def combine_documents(
    docs,
    document_prompt=custom_prompts[TemplatePromptName.DEFAULT_DOCUMENT_PROMPT],
    document_separator="\n\n",
):
    # for each docs, add an index in the metadata to be able to cite the sources
    for doc, index in zip(docs, range(len(docs)), strict=False):
        doc.metadata["index"] = index
    doc_strings = [format_document(doc, document_prompt) for doc in docs]
    return document_separator.join(doc_strings)


def format_file_list(
    list_files_array: list[QuivrKnowledge], max_files: int = 20
) -> str:
    list_files = [file.file_name or file.url for file in list_files_array]
    files: list[str] = list(filter(lambda n: n is not None, list_files))  # type: ignore
    files = files[:max_files]

    files_str = "\n".join(files) if list_files_array else "None"
    return files_str


def collect_tools(workflow_config: WorkflowConfig):
    validated_tools = "Available tools which can be activated:\n"
    for i, tool in enumerate(workflow_config.validated_tools):
        validated_tools += f"Tool {i+1} name: {tool.name}\n"
        validated_tools += f"Tool {i+1} description: {tool.description}\n\n"

    activated_tools = "Activated tools which can be deactivated:\n"
    for i, tool in enumerate(workflow_config.activated_tools):
        activated_tools += f"Tool {i+1} name: {tool.name}\n"
        activated_tools += f"Tool {i+1} description: {tool.description}\n\n"

    return validated_tools, activated_tools


def format_dict(kv: Dict[str, str]) -> str:
    return "\n".join([f"{k}: {v}" for k, v in kv.items() if v is not None and v != ""])


class LangfuseService:
    def __init__(self):
        self.langfuse_handler = CallbackHandler()

    def get_handler(self):
        return self.langfuse_handler
```

## File: `core/quivr_core/rag/entities/chat.py`
```python
from datetime import datetime
from typing import Any, Generator, Tuple, List
from uuid import UUID, uuid4

from langchain_core.messages import AIMessage, HumanMessage

from quivr_core.rag.entities.models import ChatMessage


class ChatHistory:
    """
    ChatHistory is a class that maintains a record of chat conversations. Each message
    in the history is represented by an instance of the `ChatMessage` class, and the
    chat history is stored internally as a list of these `ChatMessage` objects.
    The class provides methods to retrieve, append, iterate, and manipulate the chat
    history, as well as utilities to convert the messages into specific formats
    and support deep copying.
    """

    def __init__(self, chat_id: UUID, brain_id: UUID | None) -> None:
        """Init a new ChatHistory object.

        Args:
            chat_id (UUID): A unique identifier for the chat session.
            brain_id (UUID | None): An optional identifier for the brain associated with the chat.
        """
        self.id = chat_id
        self.brain_id = brain_id
        # TODO(@aminediro): maybe use a deque() instead ?
        self._msgs: list[ChatMessage] = []

    def get_chat_history(self, newest_first: bool = False) -> List[ChatMessage]:
        """
        Retrieves the chat history, optionally sorted in reverse chronological order.

        Args:
            newest_first (bool, optional): If True, returns the messages in reverse order (newest first). Defaults to False.

        Returns:
            List[ChatMessage]: A sorted list of chat messages.
        """
        history = sorted(self._msgs, key=lambda msg: msg.message_time)
        if newest_first:
            return history[::-1]
        return history

    def __len__(self):
        return len(self._msgs)

    def append(
        self, langchain_msg: AIMessage | HumanMessage, metadata: dict[str, Any] = {}
    ):
        """
        Appends a new message to the chat history.

        Args:
            langchain_msg (AIMessage | HumanMessage): The message content (either an AI or Human message).
            metadata (dict[str, Any], optional): Additional metadata related to the message. Defaults to an empty dictionary.
        """
        chat_msg = ChatMessage(
            chat_id=self.id,
            message_id=uuid4(),
            brain_id=self.brain_id,
            msg=langchain_msg,
            message_time=datetime.now(),
            metadata=metadata,
        )
        self._msgs.append(chat_msg)

    def iter_pairs(self) -> Generator[Tuple[HumanMessage, AIMessage], None, None]:
        """
        Iterates over the chat history in pairs, returning a HumanMessage followed by an AIMessage.

        Yields:
            Tuple[HumanMessage, AIMessage]: Pairs of human and AI messages.

        Raises:
            AssertionError: If the messages in the pair are not in the expected order (i.e., a HumanMessage followed by an AIMessage).
        """
        # Reverse the chat_history, newest first
        it = iter(self.get_chat_history(newest_first=True))
        for ai_message, human_message in zip(it, it, strict=False):
            assert isinstance(
                human_message.msg, HumanMessage
            ), f"msg {human_message} is not HumanMessage"
            assert isinstance(
                ai_message.msg, AIMessage
            ), f"msg {human_message} is not AIMessage"
            yield (human_message.msg, ai_message.msg)

    def to_list(self) -> List[HumanMessage | AIMessage]:
        """
        Converts the chat history into a list of raw HumanMessage or AIMessage objects.

        Returns:
            list[HumanMessage | AIMessage]: A list of messages in their raw form, without metadata.
        """

        return [_msg.msg for _msg in self._msgs]
```

## File: `core/quivr_core/rag/entities/config.py`
```python
import logging
import os
import re
from enum import Enum
from typing import Any, Dict, Hashable, List, Optional, Type, Union
from uuid import UUID

from langchain_core.prompts.base import BasePromptTemplate
from langchain_core.tools import BaseTool
from langgraph.graph import END, START
from pydantic import BaseModel
from rapidfuzz import fuzz, process

from quivr_core.base_config import QuivrBaseConfig
from quivr_core.config import MegaparseConfig
from quivr_core.llm_tools.llm_tools import TOOLS_CATEGORIES, TOOLS_LISTS, LLMToolFactory
from quivr_core.processor.splitter import SplitterConfig

logger = logging.getLogger("quivr_core")
MIN_CONTEXT_TOKENS = 4096
MIN_OUTPUT_TOKENS = 4096


def normalize_to_env_variable_name(name: str) -> str:
    # Replace any character that is not a letter, digit, or underscore with an underscore
    env_variable_name = re.sub(r"[^A-Za-z0-9_]", "_", name).upper()

    # Check if the normalized name starts with a digit
    if env_variable_name[0].isdigit():
        raise ValueError(
            f"Invalid environment variable name '{env_variable_name}': Cannot start with a digit."
        )

    return env_variable_name


class SpecialEdges(str, Enum):
    start = "START"
    end = "END"


class BrainConfig(QuivrBaseConfig):
    brain_id: UUID | None = None
    name: str

    @property
    def id(self) -> UUID | None:
        return self.brain_id


class DefaultWebSearchTool(str, Enum):
    TAVILY = "tavily"


class DefaultRerankers(str, Enum):
    COHERE = "cohere"
    JINA = "jina"
    # MIXEDBREAD = "mixedbread-ai"

    @property
    def default_model(self) -> str:
        # Mapping of suppliers to their default models
        return {
            self.COHERE: "rerank-v3.5",
            self.JINA: "jina-reranker-v2-base-multilingual",
            # self.MIXEDBREAD: "rmxbai-rerank-large-v1",
        }[self]


class DefaultModelSuppliers(str, Enum):
    OPENAI = "openai"
    AZURE = "azure"
    ANTHROPIC = "anthropic"
    META = "meta"
    MISTRAL = "mistral"
    GROQ = "groq"
    GEMINI = "gemini"


class LLMConfig(QuivrBaseConfig):
    max_context_tokens: int | None = None
    max_output_tokens: int | None = None
    tokenizer_hub: str | None = None


class LLMModelConfig:
    _model_defaults: Dict[DefaultModelSuppliers, Dict[str, LLMConfig]] = {
        DefaultModelSuppliers.OPENAI: {
            "gpt-4.1": LLMConfig(
                max_context_tokens=1047576,
                max_output_tokens=32768,
                tokenizer_hub="Quivr/gpt-4o",
            ),
            "gpt-4o": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=16384,
                tokenizer_hub="Quivr/gpt-4o",
            ),
            "gpt-4o-mini": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=16384,
                tokenizer_hub="Quivr/gpt-4o",
            ),
            "o3-mini": LLMConfig(
                max_context_tokens=200000,
                max_output_tokens=100000,
                tokenizer_hub="Quivr/gpt-4o",
            ),
            "o4-mini": LLMConfig(
                max_context_tokens=200000,
                max_output_tokens=100000,
                tokenizer_hub="Quivr/gpt-4o",
            ),
            "o1-mini": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=65536,
                tokenizer_hub="Quivr/gpt-4o",
            ),
            "o1-preview": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=32768,
                tokenizer_hub="Quivr/gpt-4o",
            ),
            "o1": LLMConfig(
                max_context_tokens=200000,
                max_output_tokens=100000,
                tokenizer_hub="Quivr/gpt-4o",
            ),
            "gpt-4-turbo": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=4096,
                tokenizer_hub="Quivr/gpt-4",
            ),
            "gpt-4": LLMConfig(
                max_context_tokens=8192,
                max_output_tokens=8192,
                tokenizer_hub="Quivr/gpt-4",
            ),
            "gpt-3.5-turbo": LLMConfig(
                max_context_tokens=16385,
                max_output_tokens=4096,
                tokenizer_hub="Quivr/gpt-3.5-turbo",
            ),
            "text-embedding-3-large": LLMConfig(
                max_context_tokens=8191, tokenizer_hub="Quivr/text-embedding-ada-002"
            ),
            "text-embedding-3-small": LLMConfig(
                max_context_tokens=8191, tokenizer_hub="Quivr/text-embedding-ada-002"
            ),
            "text-embedding-ada-002": LLMConfig(
                max_context_tokens=8191, tokenizer_hub="Quivr/text-embedding-ada-002"
            ),
        },
        DefaultModelSuppliers.ANTHROPIC: {
            "claude-opus-4": LLMConfig(
                max_context_tokens=200000,
                max_output_tokens=8192,
                tokenizer_hub="Quivr/claude-tokenizer",
            ),
            "claude-sonnet-4": LLMConfig(
                max_context_tokens=200000,
                max_output_tokens=8192,
                tokenizer_hub="Quivr/claude-tokenizer",
            ),
            "claude-3-7-sonnet": LLMConfig(
                max_context_tokens=200000,
                max_output_tokens=8192,
                tokenizer_hub="Quivr/claude-tokenizer",
            ),
            "claude-3-5-sonnet": LLMConfig(
                max_context_tokens=200000,
                max_output_tokens=8192,
                tokenizer_hub="Quivr/claude-tokenizer",
            ),
            "claude-3-opus": LLMConfig(
                max_context_tokens=200000,
                max_output_tokens=4096,
                tokenizer_hub="Quivr/claude-tokenizer",
            ),
            "claude-3-sonnet": LLMConfig(
                max_context_tokens=200000,
                max_output_tokens=4096,
                tokenizer_hub="Quivr/claude-tokenizer",
            ),
            "claude-3-haiku": LLMConfig(
                max_context_tokens=200000,
                max_output_tokens=4096,
                tokenizer_hub="Quivr/claude-tokenizer",
            ),
            "claude-2-1": LLMConfig(
                max_context_tokens=200000,
                max_output_tokens=4096,
                tokenizer_hub="Quivr/claude-tokenizer",
            ),
            "claude-2-0": LLMConfig(
                max_context_tokens=100000,
                max_output_tokens=4096,
                tokenizer_hub="Quivr/claude-tokenizer",
            ),
            "claude-instant-1-2": LLMConfig(
                max_context_tokens=100000,
                max_output_tokens=4096,
                tokenizer_hub="Quivr/claude-tokenizer",
            ),
        },
        # Unclear for LLAMA models...
        # see https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct/discussions/6
        DefaultModelSuppliers.META: {
            "llama-3.1": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=4096,
                tokenizer_hub="Quivr/Meta-Llama-3.1-Tokenizer",
            ),
            "llama-3": LLMConfig(
                max_context_tokens=8192,
                max_output_tokens=2048,
                tokenizer_hub="Quivr/llama3-tokenizer-new",
            ),
            "code-llama": LLMConfig(
                max_context_tokens=16384, tokenizer_hub="Quivr/llama-code-tokenizer"
            ),
        },
        DefaultModelSuppliers.GROQ: {
            "llama-3.3-70b": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=32768,
                tokenizer_hub="Quivr/Meta-Llama-3.1-Tokenizer",
            ),
            "llama-3.1-70b": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=32768,
                tokenizer_hub="Quivr/Meta-Llama-3.1-Tokenizer",
            ),
            "llama-3": LLMConfig(
                max_context_tokens=8192, tokenizer_hub="Quivr/llama3-tokenizer-new"
            ),
            "code-llama": LLMConfig(
                max_context_tokens=16384, tokenizer_hub="Quivr/llama-code-tokenizer"
            ),
            "deepseek-r1-distill-llama-70b": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=32768,
                tokenizer_hub="Quivr/Meta-Llama-3.1-Tokenizer",
            ),
            "meta-llama/llama-4-maverick-17b-128e-instruct": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=32768,
                tokenizer_hub="Quivr/Meta-Llama-3.1-Tokenizer",
            ),
        },
        DefaultModelSuppliers.MISTRAL: {
            "mistral-large": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=4096,
                tokenizer_hub="Quivr/mistral-tokenizer-v3",
            ),
            "mistral-small": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=4096,
                tokenizer_hub="Quivr/mistral-tokenizer-v3",
            ),
            "mistral-nemo": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=4096,
                tokenizer_hub="Quivr/Mistral-Nemo-Instruct-Tokenizer",
            ),
            "codestral": LLMConfig(
                max_context_tokens=32000, tokenizer_hub="Quivr/mistral-tokenizer-v3"
            ),
        },
        DefaultModelSuppliers.GEMINI: {
            "gemini-2.5": LLMConfig(
                max_context_tokens=128000,
                max_output_tokens=4096,
                tokenizer_hub="Quivr/gemini-tokenizer",
            ),
        },
    }

    @classmethod
    def get_supplier_by_model_name(cls, model: str) -> DefaultModelSuppliers | None:
        # Iterate over the suppliers and their models
        for supplier, models in cls._model_defaults.items():
            # Check if the model name or a base part of the model name is in the supplier's models
            for base_model_name in models:
                if model.startswith(base_model_name):
                    return supplier
        # Return None if no supplier matches the model name
        return None

    @classmethod
    def get_llm_model_config(
        cls, supplier: DefaultModelSuppliers, model_name: str
    ) -> Optional[LLMConfig]:
        """Retrieve the LLMConfig (context and tokenizer_hub) for a given supplier and model."""
        supplier_defaults = cls._model_defaults.get(supplier)
        if not supplier_defaults:
            return None

        # Use startswith logic for matching model names
        for key, config in supplier_defaults.items():
            if model_name.startswith(key):
                return config

        return None


class LLMEndpointConfig(QuivrBaseConfig):
    supplier: DefaultModelSuppliers = DefaultModelSuppliers.OPENAI
    model: str = "gpt-4o"
    tokenizer_hub: str | None = None
    llm_base_url: str | None = None
    env_variable_name: str | None = None
    llm_api_key: str | None = None
    max_context_tokens: int = 20000
    max_output_tokens: int = 4096
    temperature: float = 0.3
    streaming: bool = True
    prompt: BasePromptTemplate | None = None

    _FALLBACK_TOKENIZER = "cl100k_base"

    def __hash__(self):
        return hash(
            (
                self.supplier,
                self.model,
                self.tokenizer_hub,
                self.llm_base_url,
                self.env_variable_name,
                self.llm_api_key,
                self.max_context_tokens,
                self.max_output_tokens,
                self.temperature,
                self.streaming,
                repr(self.prompt) if self.prompt is not None else None,
            )
        )

    @property
    def fallback_tokenizer(self) -> str:
        return self._FALLBACK_TOKENIZER

    def __init__(self, **data):
        super().__init__(**data)
        self.set_llm_model_config()
        self.set_api_key()

    def set_api_key(self, force_reset: bool = False):
        if not self.supplier:
            return

        # Check if the corresponding API key environment variable is set
        if force_reset or not self.env_variable_name:
            self.env_variable_name = (
                f"{normalize_to_env_variable_name(self.supplier)}_API_KEY"
            )

        if not self.llm_api_key or force_reset:
            self.llm_api_key = os.getenv(self.env_variable_name)

        if not self.llm_api_key:
            logger.warning(f"The API key for supplier '{self.supplier}' is not set. ")
            logger.warning(
                f"Please set the environment variable: '{self.env_variable_name}'. "
            )

    def set_llm_model_config(self):
        # Automatically set context_length and tokenizer_hub based on the supplier and model
        llm_model_config = LLMModelConfig.get_llm_model_config(
            self.supplier, self.model
        )
        if llm_model_config:
            if llm_model_config.max_context_tokens:
                _max_context_tokens = (
                    llm_model_config.max_context_tokens
                    - llm_model_config.max_output_tokens
                    if llm_model_config.max_output_tokens
                    else llm_model_config.max_context_tokens
                )
                if self.max_context_tokens > _max_context_tokens:
                    logger.warning(
                        f"Lowering max_context_tokens from {self.max_context_tokens} to {_max_context_tokens}"
                    )
                    self.max_context_tokens = _max_context_tokens

                if self.max_context_tokens < MIN_CONTEXT_TOKENS:
                    logger.error(
                        f"max_context_tokens is too low: {self.max_context_tokens}. "
                    )
                    raise ValueError(
                        f"max_context_tokens is too low: {self.max_context_tokens}. "
                    )
            if llm_model_config.max_output_tokens:
                if self.max_output_tokens > llm_model_config.max_output_tokens:
                    logger.warning(
                        f"Lowering max_output_tokens from {self.max_output_tokens} to {llm_model_config.max_output_tokens}"
                    )
                    self.max_output_tokens = llm_model_config.max_output_tokens

                if self.max_output_tokens < MIN_OUTPUT_TOKENS:
                    logger.error(
                        f"max_output_tokens is too low: {self.max_output_tokens}. "
                    )
                    raise ValueError(
                        f"max_output_tokens is too low: {self.max_output_tokens}. "
                    )

            self.tokenizer_hub = llm_model_config.tokenizer_hub

    def set_llm_model(self, model: str):
        supplier = LLMModelConfig.get_supplier_by_model_name(model)
        if supplier is None:
            raise ValueError(
                f"Cannot find the corresponding supplier for model {model}"
            )
        self.supplier = supplier
        self.model = model

        self.set_llm_model_config()
        self.set_api_key(force_reset=True)

    def set_from_sqlmodel(self, sqlmodel: BaseModel, mapping: Dict[str, str]):
        """
        Set attributes in LLMEndpointConfig from Model attributes using a field mapping.

        :param model_instance: An instance of the Model class.
        :param mapping: A dictionary that maps Model fields to LLMEndpointConfig fields.
                        Example: {"max_input": "max_input_tokens", "env_variable_name": "env_variable_name"}
        """
        for model_field, llm_field in mapping.items():
            if hasattr(sqlmodel, model_field) and hasattr(self, llm_field):
                setattr(self, llm_field, getattr(sqlmodel, model_field))
            else:
                raise AttributeError(
                    f"Invalid mapping: {model_field} or {llm_field} does not exist."
                )


# Cannot use Pydantic v2 field_validator because of conflicts with pydantic v1 still in use in LangChain
class RerankerConfig(QuivrBaseConfig):
    supplier: DefaultRerankers | None = None
    model: str | None = None
    top_n: int = 5  # Number of chunks returned by the re-ranker
    api_key: str | None = None
    relevance_score_threshold: float | None = None
    relevance_score_key: str = "relevance_score"

    def __init__(self, **data):
        super().__init__(**data)  # Call Pydantic's BaseModel init
        self.validate_model()  # Automatically call external validation

    def validate_model(self):
        # If model is not provided, get default model based on supplier
        if self.model is None and self.supplier is not None:
            self.model = self.supplier.default_model

        # Check if the corresponding API key environment variable is set
        if self.supplier:
            api_key_var = f"{normalize_to_env_variable_name(self.supplier)}_API_KEY"
            self.api_key = os.getenv(api_key_var)

            if self.api_key is None:
                raise ValueError(
                    f"The API key for supplier '{self.supplier}' is not set. "
                    f"Please set the environment variable: {api_key_var}"
                )


class ConditionalEdgeConfig(QuivrBaseConfig):
    routing_function: str
    conditions: Union[list, Dict[Hashable, str]]

    def __init__(self, **data):
        super().__init__(**data)
        self.resolve_special_edges()

    def resolve_special_edges(self):
        """Replace SpecialEdges enum values with their corresponding langgraph values."""

        if isinstance(self.conditions, dict):
            # If conditions is a dictionary, iterate through the key-value pairs
            for key, value in self.conditions.items():
                if value == SpecialEdges.end:
                    self.conditions[key] = END
                elif value == SpecialEdges.start:
                    self.conditions[key] = START
        elif isinstance(self.conditions, list):
            # If conditions is a list, iterate through the values
            for index, value in enumerate(self.conditions):
                if value == SpecialEdges.end:
                    self.conditions[index] = END
                elif value == SpecialEdges.start:
                    self.conditions[index] = START


class NodeConfig(QuivrBaseConfig):
    name: str
    description: str | None = None
    edges: List[str] | None = None
    conditional_edge: ConditionalEdgeConfig | None = None
    tools: List[Dict[str, Any]] | None = None
    instantiated_tools: List[BaseTool | Type] | None = None

    def __init__(self, **data):
        super().__init__(**data)
        self._instantiate_tools()
        self.resolve_special_edges_in_name_and_edges()

    def resolve_special_edges_in_name_and_edges(self):
        """Replace SpecialEdges enum values in name and edges with corresponding langgraph values."""
        if self.name == SpecialEdges.start:
            self.name = START
        elif self.name == SpecialEdges.end:
            self.name = END

        if self.edges:
            for i, edge in enumerate(self.edges):
                if edge == SpecialEdges.start:
                    self.edges[i] = START
                elif edge == SpecialEdges.end:
                    self.edges[i] = END

    def _instantiate_tools(self):
        """Instantiate tools based on the configuration."""
        if self.tools:
            self.instantiated_tools = [
                LLMToolFactory.create_tool(tool_config.pop("name"), tool_config)
                for tool_config in self.tools
            ]


class DefaultWorkflow(str, Enum):
    RAG = "rag"

    @property
    def nodes(self) -> List[NodeConfig]:
        # Mapping of workflow types to their default node configurations
        workflows = {
            self.RAG: [
                NodeConfig(name=START, edges=["filter_history"]),
                NodeConfig(name="filter_history", edges=["rewrite"]),
                NodeConfig(name="rewrite", edges=["retrieve"]),
                NodeConfig(name="retrieve", edges=["generate_rag"]),
                NodeConfig(name="generate_rag", edges=[END]),
            ]
        }
        return workflows[self]


class WorkflowConfig(QuivrBaseConfig):
    name: str | None = None
    nodes: List[NodeConfig] = []
    available_tools: List[str] | None = None
    validated_tools: List[BaseTool | Type] = []
    activated_tools: List[BaseTool | Type] = []

    def __init__(self, **data):
        super().__init__(**data)
        self.check_first_node_is_start()
        self.validate_available_tools()

    def check_first_node_is_start(self):
        if self.nodes and self.nodes[0].name != START:
            raise ValueError(f"The first node should be a {SpecialEdges.start} node")

    def get_node_tools(self, node_name: str) -> List[Any]:
        """Get tools for a specific node."""
        for node in self.nodes:
            if node.name == node_name and node.instantiated_tools:
                return node.instantiated_tools
        return []

    def validate_available_tools(self):
        if self.available_tools:
            valid_tools = list(TOOLS_CATEGORIES.keys()) + list(TOOLS_LISTS.keys())
            for tool in self.available_tools:
                if tool.lower() in valid_tools:
                    self.validated_tools.append(
                        LLMToolFactory.create_tool(tool, {}).tool
                    )
                else:
                    matches = process.extractOne(
                        tool.lower(), valid_tools, scorer=fuzz.WRatio
                    )
                    if matches:
                        raise ValueError(
                            f"Tool {tool} is not a valid ToolsCategory or ToolsList. Did you mean {matches[0]}?"
                        )
                    else:
                        raise ValueError(
                            f"Tool {tool} is not a valid ToolsCategory or ToolsList"
                        )


class RetrievalConfig(QuivrBaseConfig):
    reranker_config: RerankerConfig = RerankerConfig()
    llm_config: LLMEndpointConfig = LLMEndpointConfig()
    max_history: int = 10
    max_files: int = 20
    k: int = 40  # Number of chunks returned by the retriever
    prompt: str | None = None
    workflow_config: WorkflowConfig = WorkflowConfig(nodes=DefaultWorkflow.RAG.nodes)

    def __init__(self, **data):
        super().__init__(**data)
        self.llm_config.set_api_key(force_reset=True)


class ParserConfig(QuivrBaseConfig):
    splitter_config: SplitterConfig = SplitterConfig()
    megaparse_config: MegaparseConfig = MegaparseConfig()


class IngestionConfig(QuivrBaseConfig):
    parser_config: ParserConfig = ParserConfig()


class AssistantConfig(QuivrBaseConfig):
    retrieval_config: RetrievalConfig = RetrievalConfig()
    ingestion_config: IngestionConfig = IngestionConfig()
```

## File: `core/quivr_core/rag/entities/models.py`
```python
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional
from uuid import UUID

from langchain_core.documents import Document
from langchain_core.messages import AIMessage, HumanMessage
from pydantic import BaseModel, Field
from typing_extensions import TypedDict


class cited_answer(BaseModel):
    """Answer the user question based only on the given sources, and cite the sources used."""

    answer: str = Field(
        ...,
        description="The answer to the user question, which is based only on the given sources.",
    )
    citations: list[int] = Field(
        ...,
        description="The integer IDs of the SPECIFIC sources which justify the answer.",
    )

    followup_questions: list[str] = Field(
        ...,
        description="Generate up to 3 follow-up questions that could be asked based on the answer given or context provided.",
    )


class ChatMessage(BaseModel):
    chat_id: UUID
    message_id: UUID
    brain_id: UUID | None
    msg: HumanMessage | AIMessage
    message_time: datetime
    metadata: dict[str, Any]


class KnowledgeStatus(str, Enum):
    ERROR = "ERROR"
    RESERVED = "RESERVED"
    PROCESSING = "PROCESSING"
    PROCESSED = "PROCESSED"
    UPLOADED = "UPLOADED"


class Source(BaseModel):
    name: str
    source_url: str
    type: str
    original_file_name: str
    citation: str


class RawRAGChunkResponse(TypedDict):
    answer: dict[str, Any]
    docs: dict[str, Any]


class RawRAGResponse(TypedDict):
    answer: dict[str, Any]
    docs: dict[str, Any]


class LangchainMetadata(BaseModel):
    langfuse_trace_id: str | None = None
    langfuse_trace_url: str | None = None
    langfuse_session_id: str | None = None
    langfuse_user_id: str | None = None


class ChatLLMMetadata(BaseModel):
    name: str
    display_name: str | None = None
    description: str | None = None
    image_url: str | None = None
    brain_id: str | None = None
    brain_name: str | None = None


class RAGResponseMetadata(BaseModel):
    citations: list[int] = Field(default_factory=list)
    followup_questions: list[str] = Field(default_factory=list)
    sources: list[Any] = Field(default_factory=list)
    metadata_model: ChatLLMMetadata | None = None
    workflow_step: str | None = None
    langchain_metadata: LangchainMetadata | None = None


class ParsedRAGResponse(BaseModel):
    answer: str
    metadata: RAGResponseMetadata | None = None


class ParsedRAGChunkResponse(BaseModel):
    answer: str
    metadata: RAGResponseMetadata
    last_chunk: bool = False


class QuivrKnowledge(BaseModel):
    id: UUID
    file_name: str
    brain_ids: list[UUID] | None = None
    url: Optional[str] = None
    extension: str = ".txt"
    mime_type: str = "txt"
    status: KnowledgeStatus = KnowledgeStatus.PROCESSING
    source: Optional[str] = None
    source_link: str | None = None
    file_size: int | None = None  # FIXME: Should not be optional @chloedia
    file_sha1: Optional[str] = None  # FIXME: Should not be optional @chloedia
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    metadata: Optional[Dict[str, str]] = None


class SearchResult(BaseModel):
    chunk: Document
    distance: float
```

## File: `core/quivr_core/storage/file.py`
```python
import hashlib
import mimetypes
import os
import warnings
from contextlib import asynccontextmanager
from enum import Enum
from pathlib import Path
from typing import Any, AsyncGenerator, AsyncIterable
from uuid import UUID, uuid4

import aiofiles


class FileExtension(str, Enum):
    txt = ".txt"
    pdf = ".pdf"
    docx = ".docx"


def get_file_extension(file_path: Path) -> FileExtension | str:
    try:
        mime_type, _ = mimetypes.guess_type(file_path.name)
        if mime_type:
            mime_ext = mimetypes.guess_extension(mime_type)
            if mime_ext:
                return FileExtension(mime_ext)
        return FileExtension(file_path.suffix)
    except ValueError:
        warnings.warn(
            f"File {file_path.name} extension isn't recognized. Make sure you have registered a parser for {file_path.suffix}",
            stacklevel=2,
        )
        return file_path.suffix


async def load_qfile(brain_id: UUID, path: str | Path):
    if not isinstance(path, Path):
        path = Path(path)

    if not path.exists():
        raise FileExistsError(f"file {path} doesn't exist")

    file_size = os.stat(path).st_size

    async with aiofiles.open(path, mode="rb") as f:
        file_sha1 = hashlib.sha1(await f.read()).hexdigest()

    try:
        # NOTE: when loading from existing storage, file name will be uuid
        id = UUID(path.name)
    except ValueError:
        id = uuid4()

    return QuivrFile(
        id=id,
        brain_id=brain_id,
        path=path,
        original_filename=path.name,
        file_extension=get_file_extension(path),
        file_size=file_size,
        file_sha1=file_sha1,
    )


class QuivrFile:
    __slots__ = [
        "id",
        "brain_id",
        "path",
        "original_filename",
        "file_size",
        "file_extension",
        "file_sha1",
    ]

    def __init__(
        self,
        id: UUID,
        original_filename: str,
        path: Path,
        brain_id: UUID,
        file_sha1: str,
        file_extension: FileExtension | str,
        file_size: int | None = None,
    ) -> None:
        self.id = id
        self.brain_id = brain_id
        self.path = path
        self.original_filename = original_filename
        self.file_size = file_size
        self.file_extension = file_extension
        self.file_sha1 = file_sha1

    @asynccontextmanager
    async def open(self) -> AsyncGenerator[AsyncIterable[bytes], None]:
        # TODO(@aminediro) : match on path type
        f = await aiofiles.open(self.path, mode="rb")
        try:
            yield f
        finally:
            await f.close()

    @property
    def metadata(self) -> dict[str, Any]:
        return {
            "qfile_id": self.id,
            "qfile_path": self.path,
            "original_file_name": self.original_filename,
            "file_md4": self.file_sha1,
            "file_size": self.file_size,
        }
```

## File: `core/quivr_core/storage/local_storage.py`
```python
import os
import shutil
from pathlib import Path
from typing import Self, Set
from uuid import UUID

from quivr_core.brain.serialization import LocalStorageConfig, TransparentStorageConfig
from quivr_core.files.file import QuivrFile
from quivr_core.storage.storage_base import StorageBase


class LocalStorage(StorageBase):
    """
    LocalStorage is a concrete implementation of the `StorageBase` class that
    stores files locally on disk. This class manages file uploads, tracks file
    hashes, and allows retrieval of stored files from a specified directory.

    Attributes:
        name (str): The name of the storage type, set to "local_storage".
        files (list[QuivrFile]): A list of files stored in this local storage.
        hashes (Set[str]): A set of SHA-1 hashes of the uploaded files.
        copy_flag (bool): If `True`, files are copied to the storage directory.
                          If `False`, symbolic links are used instead.
        dir_path (Path): The directory path where files are stored.

    Args:
        dir_path (Path | None): Optional directory path for storing files.
                                Defaults to the environment variable `QUIVR_LOCAL_STORAGE`
                                or `~/.cache/quivr/files`.
        copy_flag (bool): Whether to copy the file or create a symlink.
                          Defaults to `True`.
    """

    name: str = "local_storage"

    def __init__(self, dir_path: Path | None = None, copy_flag: bool = True):
        self.files: list[QuivrFile] = []
        self.hashes: Set[str] = set()
        self.copy_flag = copy_flag

        if dir_path is None:
            self.dir_path = Path(
                os.getenv("QUIVR_LOCAL_STORAGE", "~/.cache/quivr/files")
            )
        else:
            self.dir_path = dir_path
        os.makedirs(self.dir_path, exist_ok=True)

    def _load_files(self) -> None:
        # TODO(@aminediro): load existing files
        pass

    def nb_files(self) -> int:
        return len(self.files)

    def info(self):
        return {"directory_path": self.dir_path, **super().info()}

    async def upload_file(self, file: QuivrFile, exists_ok: bool = False) -> None:
        """
        Uploads a file to the local storage. Copies or creates a symlink based
        on the `copy_flag` attribute. Checks for duplicate file uploads using
        the file's SHA-1 hash.

        Args:
            file (QuivrFile): The file object to upload.
            exists_ok (bool): If `True`, allows overwriting an existing file.
                              Defaults to `False`.

        Raises:
            FileExistsError: If a file with the same SHA-1 hash already exists
                             and `exists_ok` is set to `False`.
        """
        dst_path = os.path.join(
            self.dir_path, str(file.brain_id), f"{file.id}{file.file_extension}"
        )

        if file.file_sha1 in self.hashes and not exists_ok:
            raise FileExistsError(f"file {file.original_filename} already uploaded")

        if self.copy_flag:
            shutil.copy2(file.path, dst_path)
        else:
            os.symlink(file.path, dst_path)

        file.path = Path(dst_path)
        self.files.append(file)
        self.hashes.add(file.file_sha1)

    async def get_files(self) -> list[QuivrFile]:
        """
        Retrieves the list of files stored in the local storage.

        Returns:
            list[QuivrFile]: A list of stored file objects.
        """
        return self.files

    async def remove_file(self, file_id: UUID) -> None:
        """
        Removes a file from the local storage. This method is currently not
        implemented.

        Args:
            file_id (UUID): The unique identifier of the file to remove.

        Raises:
            NotImplementedError: Always raises this error as the method is not yet implemented.
        """
        raise NotImplementedError

    @classmethod
    def load(cls, config: LocalStorageConfig) -> Self:
        """
        Loads the local storage from a configuration object. This method
        initializes the storage directory and populates it with deserialized
        files from the configuration.

        Args:
            config (LocalStorageConfig): Configuration object containing the
                                         storage path and serialized file data.

        Returns:
            LocalStorage: An instance of `LocalStorage` with files loaded
                          from the configuration.
        """
        tstorage = cls(dir_path=config.storage_path)
        tstorage.files = [QuivrFile.deserialize(f) for f in config.files.values()]
        return tstorage


class TransparentStorage(StorageBase):
    """Transparent Storage."""

    name: str = "transparent_storage"

    def __init__(self):
        self.id_files = {}

    async def upload_file(self, file: QuivrFile, exists_ok: bool = False) -> None:
        self.id_files[file.id] = file

    def nb_files(self) -> int:
        return len(self.id_files)

    async def remove_file(self, file_id: UUID) -> None:
        raise NotImplementedError

    async def get_files(self) -> list[QuivrFile]:
        return list(self.id_files.values())

    @classmethod
    def load(cls, config: TransparentStorageConfig) -> Self:
        tstorage = cls()
        tstorage.id_files = {
            i: QuivrFile.deserialize(f) for i, f in config.files.items()
        }
        return tstorage
```

## File: `core/quivr_core/storage/storage_base.py`
```python
from abc import ABC, abstractmethod
from uuid import UUID

from quivr_core.brain.info import StorageInfo
from quivr_core.storage.local_storage import QuivrFile


class StorageBase(ABC):
    """
    Abstract base class for storage systems. All subclasses are required to define certain attributes and implement specific methods for managing files

    Attributes:
        name (str): Name of the storage type.
    """

    name: str

    def __init_subclass__(cls, **kwargs):
        for required in ("name",):
            if not getattr(cls, required):
                raise TypeError(
                    f"Can't instantiate abstract class {cls.__name__} without {required} attribute defined"
                )
        return super().__init_subclass__(**kwargs)

    def __repr__(self) -> str:
        return f"storage_type: {self.name}"

    @abstractmethod
    def nb_files(self) -> int:
        """
        Abstract method to get the number of files in the storage.

        Returns:
            int: The number of files in the storage.

        Raises:
            Exception: If the method is not implemented.
        """
        raise Exception("Unimplemented nb_files method")

    @abstractmethod
    async def get_files(self) -> list[QuivrFile]:
        """
        Abstract asynchronous method to get the files `QuivrFile` in the storage.

        Returns:
            list[QuivrFile]: A list of QuivrFile objects representing the files in the storage.

        Raises:
            Exception: If the method is not implemented.
        """
        raise Exception("Unimplemented get_files method")

    @abstractmethod
    async def upload_file(self, file: QuivrFile, exists_ok: bool = False) -> None:
        """
        Abstract asynchronous method to upload a file to the storage.

        Args:
            file (QuivrFile): The file to upload.
            exists_ok (bool): If True, allows overwriting the file if it already exists. Default is False.

        Raises:
            Exception: If the method is not implemented.
        """
        raise Exception("Unimplemented  upload_file method")

    @abstractmethod
    async def remove_file(self, file_id: UUID) -> None:
        """
        Abstract asynchronous method to remove a file from the storage.

        Args:
            file_id (UUID): The unique identifier of the file to be removed.

        Raises:
            Exception: If the method is not implemented.
        """
        raise Exception("Unimplemented remove_file method")

    def info(self) -> StorageInfo:
        """
        Returns information about the storage, including the storage type and the number of files.

        Returns:
            StorageInfo: An object containing details about the storage.
        """
        return StorageInfo(
            storage_type=self.name,
            n_files=self.nb_files(),
        )
```

## File: `core/scripts/run_tests.sh`
```bash
#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Constants
IMAGE_NAME="quivr-core-test"
IMAGE_TAG="latest"
DOCKERFILE="Dockerfile.test"
VOLUME_MAPPING="$PWD:/code"
TOX_DIR="/code/.tox-docker"
CMD="poetry run tox -p auto"

# Functions
build_image() {
    echo "Building Docker image..."
    docker build -f $DOCKERFILE -t $IMAGE_NAME:$IMAGE_TAG .
}

run_container() {
    echo "Running tests in Docker container..."
    docker run -it --rm \
        -e TOX_WORK_DIR=$TOX_DIR \
        -v $VOLUME_MAPPING \
        $IMAGE_NAME:$IMAGE_TAG $CMD
}

# Main script execution
build_image
run_container

echo "Tests completed successfully."
```

## File: `core/scripts/run_tests_buildx.sh`
```bash
#!/bin/bash

set -e

# Constants
IMAGE_NAME="quivr-core-test"
IMAGE_TAG="latest"
DOCKERFILE="Dockerfile.test"
VOLUME_MAPPING="$PWD:/code"
CMD="poetry run tox"
PLATFORM="linux/amd64"
BUILDER_NAME="amd64_builder"

# Functions
build_image() {
    echo "Building Docker image for $PLATFORM..."
    EXISTING_BUILDER=$(docker buildx ls | grep -w $BUILDER_NAME)

    # Create the builder if it doesn't exist
    if [ -z "$EXISTING_BUILDER" ]; then
        echo "Creating builder: $BUILDER_NAME"
        docker buildx create --use --name $BUILDER_NAME --platform $PLATFORM
    else
        echo "Builder $BUILDER_NAME already exists. Skipping creation."
    fi

    docker buildx build --platform $PLATFORM -f $DOCKERFILE -t $IMAGE_NAME:$IMAGE_TAG --load .
}

run_container() {
    echo "Running tests in Docker container..."
    docker run -it --rm --platform $PLATFORM -v $VOLUME_MAPPING $IMAGE_NAME:$IMAGE_TAG $CMD
}

# Main script execution
build_image
run_container

echo "Tests completed successfully."
```

## File: `core/tests/chunk_stream_fixture.jsonl`
```
{"docs": []}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": "call_mjPLkzPy8NPmr4imoirwmhn1", "function": {"arguments": "", "name": "cited_answer"}, "type": "function"}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [{"name": "cited_answer", "args": {}, "id": "call_mjPLkzPy8NPmr4imoirwmhn1"}], "invalid_tool_calls": [], "usage_metadata": null, "tool_call_chunks": [{"name": "cited_answer", "args": "", "id": "call_mjPLkzPy8NPmr4imoirwmhn1", "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "{\"", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [{"name": "", "args": {}, "id": null}], "invalid_tool_calls": [], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "{\"", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "answer", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "answer", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "answer", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "\":\"", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "\":\"", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "\":\"", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "Natural", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "Natural", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "Natural", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " Language", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " Language", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " Language", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " Processing", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " Processing", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " Processing", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " (", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " (", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " (", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "N", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "N", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "N", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "LP", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "LP", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "LP", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ")", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ")", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ")", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " is", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " is", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " is", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " a", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " a", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " a", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " field", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " field", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " field", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " of", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " of", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " of", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " artificial", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " artificial", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " artificial", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " intelligence", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " intelligence", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " intelligence", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " that", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " that", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " that", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " focuses", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " focuses", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " focuses", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " on", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " on", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " on", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " the", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " the", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " the", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " interaction", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " interaction", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " interaction", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " between", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " between", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " between", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " computers", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " computers", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " computers", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " and", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " and", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " and", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " humans", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " humans", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " humans", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " through", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " through", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " through", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " natural", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " natural", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " natural", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " language", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " language", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " language", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ".", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ".", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ".", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " The", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " The", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " The", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " ultimate", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " ultimate", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " ultimate", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " objective", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " objective", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " objective", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " of", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " of", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " of", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " NLP", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " NLP", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " NLP", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " is", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " is", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " is", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " to", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " to", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " to", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " enable", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " enable", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " enable", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " computers", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " computers", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " computers", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " to", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " to", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " to", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " understand", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " understand", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " understand", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ",", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ",", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ",", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " interpret", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " interpret", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " interpret", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ",", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ",", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ",", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " and", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " and", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " and", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " respond", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " respond", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " respond", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " to", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " to", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " to", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " human", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " human", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " human", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " language", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " language", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " language", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " in", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " in", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " in", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " a", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " a", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " a", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " way", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " way", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " way", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " that", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " that", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " that", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " is", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " is", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " is", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " both", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " both", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " both", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " valuable", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " valuable", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " valuable", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " and", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " and", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " and", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " meaningful", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " meaningful", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " meaningful", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ".", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ".", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ".", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " NLP", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " NLP", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " NLP", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " combines", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " combines", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " combines", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " computational", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " computational", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " computational", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " lingu", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " lingu", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " lingu", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "istics", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "istics", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "istics", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "\u2014", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "\u2014", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "\u2014", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "rule", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "rule", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "rule", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "-based", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "-based", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "-based", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " modeling", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " modeling", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " modeling", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " of", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " of", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " of", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " human", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " human", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " human", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " language", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " language", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " language", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "\u2014with", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "\u2014with", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "\u2014with", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " statistical", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " statistical", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " statistical", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ",", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ",", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ",", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " machine", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " machine", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " machine", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " learning", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " learning", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " learning", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ",", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ",", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ",", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " and", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " and", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " and", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " deep", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " deep", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " deep", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " learning", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " learning", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " learning", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " models", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " models", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " models", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ".", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ".", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ".", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " This", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " This", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " This", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " combination", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " combination", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " combination", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " allows", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " allows", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " allows", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " computers", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " computers", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " computers", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " to", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " to", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " to", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " process", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " process", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " process", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " human", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " human", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " human", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " language", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " language", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " language", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " in", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " in", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " in", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " the", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " the", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " the", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " form", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " form", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " form", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " of", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " of", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " of", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " text", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " text", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " text", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " or", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " or", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " or", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " voice", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " voice", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " voice", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " data", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " data", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " data", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " and", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " and", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " and", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " to", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " to", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " to", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " understand", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " understand", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " understand", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " its", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " its", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " its", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " full", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " full", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " full", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " meaning", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " meaning", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " meaning", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ",", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ",", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ",", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " complete", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " complete", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " complete", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " with", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " with", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " with", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " the", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " the", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " the", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " speaker", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " speaker", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " speaker", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " or", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " or", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " or", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " writer", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " writer", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " writer", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "\u2019s", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "\u2019s", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "\u2019s", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " intent", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " intent", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " intent", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " and", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " and", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " and", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " sentiment", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " sentiment", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " sentiment", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ".", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ".", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ".", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " Key", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " Key", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " Key", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " tasks", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " tasks", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " tasks", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " in", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " in", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " in", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " NLP", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " NLP", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " NLP", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " include", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " include", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " include", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " text", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " text", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " text", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " and", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " and", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " and", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " speech", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " speech", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " speech", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " recognition", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " recognition", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " recognition", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ",", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ",", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ",", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " translation", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " translation", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " translation", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ",", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ",", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ",", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " sentiment", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " sentiment", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " sentiment", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " analysis", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " analysis", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " analysis", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ",", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ",", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ",", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " and", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " and", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " and", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " topic", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " topic", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " topic", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " segmentation", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " segmentation", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " segmentation", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ".\",\"", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ".\",\"", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ".\",\"", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "thought", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "thought", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "thought", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "s", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "s", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "s", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "\":\"", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "\":\"", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "\":\"", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "Based", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "Based", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "Based", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " on", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " on", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " on", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " the", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " the", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " the", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " context", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " context", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " context", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " provided", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " provided", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " provided", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ",", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ",", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ",", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " I", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " I", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " I", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " have", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " have", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " have", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " created", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " created", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " created", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " a", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " a", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " a", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " detailed", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " detailed", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " detailed", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " answer", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " answer", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " answer", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " about", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " about", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " about", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " what", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " what", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " what", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " Natural", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " Natural", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " Natural", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " Language", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " Language", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " Language", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " Processing", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " Processing", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " Processing", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " (", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " (", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " (", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "N", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "N", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "N", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "LP", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "LP", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "LP", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ")", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ")", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ")", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " is", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " is", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " is", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ",", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ",", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ",", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " including", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " including", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " including", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " its", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " its", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " its", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " objectives", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " objectives", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " objectives", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ",", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ",", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ",", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " components", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " components", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " components", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ",", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ",", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ",", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " and", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " and", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " and", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " key", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " key", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " key", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " tasks", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " tasks", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " tasks", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ".\",\"", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ".\",\"", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ".\",\"", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "cit", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "cit", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "cit", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "ations", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "ations", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "ations", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "\":[]", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "\":[]", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "\":[]", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": ",\"", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": ",\"", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": ",\"", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "follow", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "follow", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "follow", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "up", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "up", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "up", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "_questions", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "_questions", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "_questions", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "\":[\"", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "\":[\"", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "\":[\"", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "What", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "What", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "What", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " are", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " are", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " are", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " some", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " some", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " some", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " common", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " common", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " common", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " applications", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " applications", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " applications", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " of", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " of", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " of", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " Natural", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " Natural", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " Natural", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " Language", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " Language", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " Language", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " Processing", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " Processing", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " Processing", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "?", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "?", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "?", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "\",\"", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "\",\"", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "\",\"", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "How", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "How", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "How", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " does", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " does", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " does", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " sentiment", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " sentiment", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " sentiment", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " analysis", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " analysis", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " analysis", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " work", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " work", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " work", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " in", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " in", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " in", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " NLP", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " NLP", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " NLP", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "?", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "?", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "?", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "\",\"", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "\",\"", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "\",\"", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "What", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "What", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "What", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " are", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " are", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " are", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " the", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " the", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " the", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " challenges", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " challenges", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " challenges", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " faced", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " faced", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " faced", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " in", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " in", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " in", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " Natural", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " Natural", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " Natural", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " Language", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " Language", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " Language", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": " Processing", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": " Processing", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": " Processing", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "?", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "?", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "?", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "\"]", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "\"]", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "\"]", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {"tool_calls": [{"index": 0, "id": null, "function": {"arguments": "}", "name": null}, "type": null}]}, "response_metadata": {}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [{"name": null, "args": "}", "id": null, "error": null}], "usage_metadata": null, "tool_call_chunks": [{"name": null, "args": "}", "id": null, "index": 0}]}}
{"answer": {"content": "", "additional_kwargs": {}, "response_metadata": {"finish_reason": "tool_calls", "model_name": "gpt-4o-2024-05-13", "system_fingerprint": "fp_298125635f"}, "type": "AIMessageChunk", "name": null, "id": "run-8387322c-9e92-4a63-8f63-f37f86acd5c4", "example": false, "tool_calls": [], "invalid_tool_calls": [], "usage_metadata": null, "tool_call_chunks": []}}
```

## File: `core/tests/conftest.py`
```python
import json
import os
from pathlib import Path
from uuid import uuid4

import pytest
from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_core.language_models import FakeListChatModel
from langchain_core.messages.ai import AIMessageChunk
from langchain_core.runnables.utils import AddableDict
from langchain_core.vectorstores import InMemoryVectorStore
from quivr_core.rag.entities.config import LLMEndpointConfig
from quivr_core.files.file import FileExtension, QuivrFile
from quivr_core.llm import LLMEndpoint


@pytest.fixture(scope="function")
def temp_data_file(tmp_path):
    data = "This is some test data."
    temp_file = tmp_path / "data.txt"
    temp_file.write_text(data)
    return temp_file


@pytest.fixture(scope="function")
def quivr_txt(temp_data_file):
    return QuivrFile(
        id=uuid4(),
        brain_id=uuid4(),
        original_filename=temp_data_file.name,
        path=temp_data_file,
        file_extension=FileExtension.txt,
        file_sha1="123",
    )


@pytest.fixture
def quivr_pdf():
    return QuivrFile(
        id=uuid4(),
        brain_id=uuid4(),
        original_filename="dummy.pdf",
        path=Path("./tests/processor/data/dummy.pdf"),
        file_extension=FileExtension.pdf,
        file_sha1="13bh234jh234",
    )


@pytest.fixture
def full_response():
    return "Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language. The ultimate objective of NLP is to enable computers to understand, interpret, and respond to human language in a way that is both valuable and meaningful. NLP combines computational linguistics—rule-based modeling of human language—with statistical, machine learning, and deep learning models. This combination allows computers to process human language in the form of text or voice data and to understand its full meaning, complete with the speaker or writer’s intent and sentiment. Key tasks in NLP include text and speech recognition, translation, sentiment analysis, and topic segmentation."


@pytest.fixture
def chunks_stream_answer():
    with open("./tests/chunk_stream_fixture.jsonl", "r") as f:
        raw_chunks = list(f)

    chunks = []
    for rc in raw_chunks:
        chunk = AddableDict(**json.loads(rc))
        if "answer" in chunk:
            chunk["answer"] = AIMessageChunk(**chunk["answer"])
            chunks.append(chunk)
    return chunks


@pytest.fixture(autouse=True)
def openai_api_key():
    os.environ["OPENAI_API_KEY"] = "this-is-a-test-key"


@pytest.fixture
def answers():
    return [f"answer_{i}" for i in range(10)]


@pytest.fixture(scope="function")
def fake_llm(answers: list[str]):
    llm = FakeListChatModel(responses=answers)
    return LLMEndpoint(llm=llm, llm_config=LLMEndpointConfig(model="fake_model"))


@pytest.fixture(scope="function")
def embedder():
    return DeterministicFakeEmbedding(size=20)


@pytest.fixture(scope="function")
def mem_vector_store(embedder):
    return InMemoryVectorStore(embedder)
```

## File: `core/tests/fixture_chunks.py`
```python
import asyncio
import json
from uuid import uuid4

from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_core.messages.ai import AIMessageChunk
from langchain_core.vectorstores import InMemoryVectorStore
from quivr_core.rag.entities.chat import ChatHistory
from quivr_core.rag.entities.config import LLMEndpointConfig, RetrievalConfig
from quivr_core.llm import LLMEndpoint
from quivr_core.rag.quivr_rag_langgraph import QuivrQARAGLangGraph


async def main():
    retrieval_config = RetrievalConfig(llm_config=LLMEndpointConfig(model="gpt-4o"))
    embedder = DeterministicFakeEmbedding(size=20)
    vec = InMemoryVectorStore(embedder)

    llm = LLMEndpoint.from_config(retrieval_config.llm_config)
    chat_history = ChatHistory(uuid4(), uuid4())
    rag_pipeline = QuivrQARAGLangGraph(
        retrieval_config=retrieval_config, llm=llm, vector_store=vec
    )

    conversational_qa_chain = rag_pipeline.build_chain()

    with open("response.jsonl", "w") as f:
        async for event in conversational_qa_chain.astream_events(
            {
                "messages": [
                    ("user", "What is NLP, give a very long detailed answer"),
                ],
                "chat_history": chat_history,
                "custom_personality": None,
            },
            version="v1",
            config={"metadata": {}},
        ):
            kind = event["event"]
            if (
                kind == "on_chat_model_stream"
                and event["metadata"]["langgraph_node"] == "generate"
            ):
                chunk = event["data"]["chunk"]
                dict_chunk = {
                    k: v.dict() if isinstance(v, AIMessageChunk) else v
                    for k, v in chunk.items()
                }
                f.write(json.dumps(dict_chunk) + "\n")


asyncio.run(main())
```

## File: `core/tests/rag_config.yaml`
```yaml
ingestion_config:
  parser_config:
    megaparse_config:
      strategy: "fast"
      pdf_parser: "unstructured"
    splitter_config:
      chunk_size: 400
      chunk_overlap: 100

retrieval_config:
  # Maximum number of previous conversation iterations
  # to include in the context of the answer
  max_history: 10

  max_files: 20
  reranker_config:
    # The reranker supplier to use
    supplier: "cohere"

    # The model to use for the reranker for the given supplier
    model: "rerank-multilingual-v3.0"

    # Number of chunks returned by the reranker
    top_n: 5
  llm_config:
    # The LLM supplier to use
    supplier: "openai"

    # The model to use for the LLM for the given supplier
    model: "gpt-3.5-turbo-0125"

    max_context_tokens: 2000

    # Maximum number of tokens to pass to the LLM
    # as a context to generate the answer
    max_output_tokens: 2000

    temperature: 0.7
    streaming: true
```

## File: `core/tests/rag_config_workflow.yaml`
```yaml
ingestion_config:
  parser_config:
    megaparse_config:
      strategy: "fast"
      pdf_parser: "unstructured"
    splitter_config:
      chunk_size: 400
      chunk_overlap: 100

retrieval_config:
  workflow_config:
    name: "standard RAG"
    nodes:
      - name: "START"
        edges: ["filter_history"]

      - name: "filter_history"
        edges: ["generate_chat_llm"]

      - name: "generate_chat_llm" # the name of the last node, from which we want to stream the answer to the user, should always start with "generate"
        edges: ["END"]
  # Maximum number of previous conversation iterations
  # to include in the context of the answer
  max_history: 10

  #prompt: "my prompt"

  max_files: 20
  reranker_config:
    # The reranker supplier to use
    supplier: "cohere"

    # The model to use for the reranker for the given supplier
    model: "rerank-multilingual-v3.0"

    # Number of chunks returned by the reranker
    top_n: 5
  llm_config:
    # The LLM supplier to use
    supplier: "openai"

    # The model to use for the LLM for the given supplier
    model: "gpt-3.5-turbo-0125"

    max_context_tokens: 2000

    # Maximum number of tokens to pass to the LLM
    # as a context to generate the answer
    max_output_tokens: 2000

    temperature: 0.7
    streaming: true
```

## File: `core/tests/test_brain.py`
```python
from dataclasses import asdict
from uuid import uuid4

import pytest
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from quivr_core.brain import Brain
from quivr_core.rag.entities.chat import ChatHistory
from quivr_core.llm import LLMEndpoint
from quivr_core.storage.local_storage import TransparentStorage


@pytest.mark.base
def test_brain_empty_files_no_vectordb(fake_llm, embedder):
    # Testing no files
    with pytest.raises(ValueError):
        Brain.from_files(
            name="test_brain",
            file_paths=[],
            llm=fake_llm,
            embedder=embedder,
        )


def test_brain_empty_files(fake_llm, embedder, mem_vector_store):
    brain = Brain.from_files(
        name="test_brain",
        file_paths=[],
        llm=fake_llm,
        embedder=embedder,
        vector_db=mem_vector_store,
    )
    assert brain


@pytest.mark.asyncio
async def test_brain_from_files_success(
    fake_llm: LLMEndpoint, embedder, temp_data_file, mem_vector_store
):
    brain = await Brain.afrom_files(
        name="test_brain",
        file_paths=[temp_data_file],
        embedder=embedder,
        llm=fake_llm,
        vector_db=mem_vector_store,
    )
    assert brain.name == "test_brain"
    assert len(brain.chat_history) == 0
    assert brain.llm == fake_llm
    assert brain.vector_db.embeddings == embedder
    assert isinstance(brain.default_chat, ChatHistory)
    assert len(brain.default_chat) == 0

    # storage
    assert isinstance(brain.storage, TransparentStorage)
    assert len(await brain.storage.get_files()) == 1


@pytest.mark.asyncio
async def test_brain_from_langchain_docs(embedder, fake_llm, mem_vector_store):
    chunk = Document("content_1", metadata={"id": uuid4()})
    brain = await Brain.afrom_langchain_documents(
        name="test",
        llm=fake_llm,
        langchain_documents=[chunk],
        embedder=embedder,
        vector_db=mem_vector_store,
    )
    # No appended files
    assert len(await brain.storage.get_files()) == 0
    assert len(brain.chat_history) == 0


@pytest.mark.base
@pytest.mark.asyncio
async def test_brain_search(
    embedder: Embeddings,
):
    chunk1 = Document("content_1", metadata={"id": uuid4()})
    chunk2 = Document("content_2", metadata={"id": uuid4()})
    brain = await Brain.afrom_langchain_documents(
        name="test", langchain_documents=[chunk1, chunk2], embedder=embedder
    )

    k = 2
    result = await brain.asearch("content_1", n_results=k)

    assert len(result) == k
    assert result[0].chunk == chunk1
    assert result[1].chunk == chunk2
    assert result[0].distance == 0
    assert result[1].distance > result[0].distance


@pytest.mark.asyncio
async def test_brain_get_history(
    fake_llm: LLMEndpoint, embedder, temp_data_file, mem_vector_store
):
    brain = await Brain.afrom_files(
        name="test_brain",
        file_paths=[temp_data_file],
        embedder=embedder,
        llm=fake_llm,
        vector_db=mem_vector_store,
    )

    await brain.aask("question")
    await brain.aask("question")

    assert len(brain.default_chat) == 4


@pytest.mark.base
@pytest.mark.asyncio
async def test_brain_ask_streaming(
    fake_llm: LLMEndpoint, embedder, temp_data_file, answers
):
    brain = await Brain.afrom_files(
        name="test_brain", file_paths=[temp_data_file], embedder=embedder, llm=fake_llm
    )

    response = ""
    async for chunk in brain.ask_streaming("question"):
        response += chunk.answer

    assert response == answers[1]


def test_brain_info_empty(fake_llm: LLMEndpoint, embedder, mem_vector_store):
    storage = TransparentStorage()
    id = uuid4()
    brain = Brain(
        name="test",
        id=id,
        llm=fake_llm,
        embedder=embedder,
        storage=storage,
        vector_db=mem_vector_store,
    )

    assert asdict(brain.info()) == {
        "brain_id": id,
        "brain_name": "test",
        "files_info": asdict(storage.info()),
        "chats_info": {
            "nb_chats": 1,  # start with a default chat
            "current_default_chat": brain.default_chat.id,
            "current_chat_history_length": 0,
        },
        "llm_info": asdict(fake_llm.info()),
    }
```

## File: `core/tests/test_chat_history.py`
```python
from time import sleep
from uuid import uuid4

import pytest
from langchain_core.messages import AIMessage, HumanMessage
from quivr_core.rag.entities.chat import ChatHistory


@pytest.fixture
def ai_message():
    return AIMessage("ai message")


@pytest.fixture
def human_message():
    return HumanMessage("human message")


def test_chat_history_constructor():
    brain_id, chat_id = uuid4(), uuid4()
    chat_history = ChatHistory(brain_id=brain_id, chat_id=chat_id)

    assert chat_history.brain_id == brain_id
    assert chat_history.id == chat_id
    assert len(chat_history._msgs) == 0


def test_chat_history_append(ai_message: AIMessage, human_message: HumanMessage):
    chat_history = ChatHistory(uuid4(), uuid4())
    chat_history.append(ai_message)

    assert len(chat_history) == 1
    chat_history.append(human_message)
    assert len(chat_history) == 2


def test_chat_history_get_history(ai_message: AIMessage, human_message: HumanMessage):
    chat_history = ChatHistory(uuid4(), uuid4())
    chat_history.append(ai_message)
    chat_history.append(human_message)
    chat_history.append(ai_message)
    sleep(0.01)
    chat_history.append(human_message)

    msgs = chat_history.get_chat_history()

    assert len(msgs) == 4
    assert msgs[-1].message_time > msgs[0].message_time
    assert isinstance(msgs[0].msg, AIMessage)
    assert isinstance(msgs[1].msg, HumanMessage)

    msgs = chat_history.get_chat_history(newest_first=True)
    assert msgs[-1].message_time < msgs[0].message_time


def test_chat_history_iter_pairs_invalid(
    ai_message: AIMessage, human_message: HumanMessage
):
    with pytest.raises(AssertionError):
        chat_history = ChatHistory(uuid4(), uuid4())
        chat_history.append(ai_message)
        chat_history.append(ai_message)
        next(chat_history.iter_pairs())


def test_chat_history_iter_pais(ai_message: AIMessage, human_message: HumanMessage):
    chat_history = ChatHistory(uuid4(), uuid4())

    chat_history.append(human_message)
    chat_history.append(ai_message)
    chat_history.append(human_message)
    chat_history.append(ai_message)

    result = list(chat_history.iter_pairs())

    assert result == [(human_message, ai_message), (human_message, ai_message)]
```

## File: `core/tests/test_config.py`
```python
from quivr_core.rag.entities.config import LLMEndpointConfig, RetrievalConfig


def test_default_llm_config():
    config = LLMEndpointConfig()

    assert (
        config.model_dump()
        == LLMEndpointConfig(
            model="gpt-4o",
            llm_base_url=None,
            llm_api_key=None,
            max_context_tokens=2000,
            max_output_tokens=2000,
            temperature=0.7,
            streaming=True,
        ).model_dump()
    )


def test_default_retrievalconfig():
    config = RetrievalConfig()

    assert config.max_files == 20
    assert config.prompt is None
    print("\n\n", config.llm_config, "\n\n")
    print("\n\n", LLMEndpointConfig(), "\n\n")
    assert config.llm_config == LLMEndpointConfig()
```

## File: `core/tests/test_llm_endpoint.py`
```python
import os

import pytest
from langchain_core.language_models import FakeListChatModel
from pydantic import ValidationError
from quivr_core.rag.entities.config import LLMEndpointConfig
from quivr_core.llm import LLMEndpoint


@pytest.mark.base
def test_llm_endpoint_from_config_default():
    from langchain_openai import ChatOpenAI

    del os.environ["OPENAI_API_KEY"]

    with pytest.raises((ValidationError, ValueError)):
        llm = LLMEndpoint.from_config(LLMEndpointConfig())

    # Working default
    config = LLMEndpointConfig(llm_api_key="test")
    llm = LLMEndpoint.from_config(config=config)

    assert llm.supports_func_calling()
    assert isinstance(llm._llm, ChatOpenAI)
    assert llm._llm.model_name in llm.get_config().model


@pytest.mark.base
def test_llm_endpoint_from_config():
    from langchain_openai import ChatOpenAI

    config = LLMEndpointConfig(
        model="llama2", llm_api_key="test", llm_base_url="http://localhost:8441"
    )
    llm = LLMEndpoint.from_config(config)

    assert not llm.supports_func_calling()
    assert isinstance(llm._llm, ChatOpenAI)
    assert llm._llm.model_name in llm.get_config().model


def test_llm_endpoint_constructor():
    llm_endpoint = FakeListChatModel(responses=[])
    llm_endpoint = LLMEndpoint(
        llm=llm_endpoint, llm_config=LLMEndpointConfig(model="test")
    )

    assert not llm_endpoint.supports_func_calling()
```

## File: `core/tests/test_quivr_file.py`
```python
from pathlib import Path
from uuid import uuid4

from quivr_core.files.file import FileExtension, QuivrFile


def test_create_file():
    id = uuid4()
    brain_id = uuid4()
    qfile = QuivrFile(
        id=id,
        brain_id=brain_id,
        original_filename="name",
        path=Path("/tmp/name"),
        file_extension=FileExtension.txt,
        file_sha1="123",
    )

    assert qfile.id == id
    assert qfile.brain_id == brain_id
    assert qfile.original_filename == "name"
    assert qfile.path == Path("/tmp/name")


def test_create_file_add_metadata():
    id = uuid4()
    brain_id = uuid4()
    qfile = QuivrFile(
        id=id,
        brain_id=brain_id,
        original_filename="name",
        path=Path("/tmp/name"),
        file_extension=FileExtension.txt,
        file_sha1="123",
        metadata={"other_id": "id"},
    )

    assert qfile.metadata["other_id"] == "id"
```

## File: `core/tests/test_quivr_rag.py`
```python
from uuid import uuid4

import pytest
from quivr_core.rag.entities.chat import ChatHistory
from quivr_core.rag.entities.config import LLMEndpointConfig, RetrievalConfig
from quivr_core.llm import LLMEndpoint
from quivr_core.rag.entities.models import ParsedRAGChunkResponse, RAGResponseMetadata
from quivr_core.rag.quivr_rag_langgraph import QuivrQARAGLangGraph


@pytest.fixture(scope="function")
def mock_chain_qa_stream(monkeypatch, chunks_stream_answer):
    class MockQAChain:
        async def astream_events(self, *args, **kwargs):
            default_metadata = {
                "langgraph_node": "generate",
                "is_final_node": False,
                "citations": None,
                "followup_questions": None,
                "sources": None,
                "metadata_model": None,
            }

            # Send all chunks except the last one
            for chunk in chunks_stream_answer[:-1]:
                yield {
                    "event": "on_chat_model_stream",
                    "metadata": default_metadata,
                    "data": {"chunk": chunk["answer"]},
                }

            # Send the last chunk
            yield {
                "event": "end",
                "metadata": {
                    "langgraph_node": "generate",
                    "is_final_node": True,
                    "citations": [],
                    "followup_questions": None,
                    "sources": [],
                    "metadata_model": None,
                },
                "data": {"chunk": chunks_stream_answer[-1]["answer"]},
            }

    def mock_qa_chain(*args, **kwargs):
        self = args[0]
        self.final_nodes = ["generate"]
        return MockQAChain()

    monkeypatch.setattr(QuivrQARAGLangGraph, "build_chain", mock_qa_chain)


@pytest.mark.base
@pytest.mark.asyncio
async def test_quivrqaraglanggraph(
    mem_vector_store, full_response, mock_chain_qa_stream, openai_api_key
):
    # Making sure the model
    llm_config = LLMEndpointConfig(model="gpt-4o")
    llm = LLMEndpoint.from_config(llm_config)
    retrieval_config = RetrievalConfig(llm_config=llm_config)
    chat_history = ChatHistory(uuid4(), uuid4())
    rag_pipeline = QuivrQARAGLangGraph(
        retrieval_config=retrieval_config, llm=llm, vector_store=mem_vector_store
    )

    stream_responses: list[ParsedRAGChunkResponse] = []

    # Making sure that we are calling the func_calling code path
    assert rag_pipeline.llm_endpoint.supports_func_calling()
    async for resp in rag_pipeline.answer_astream(
        "answer in bullet points. tell me something", chat_history, []
    ):
        stream_responses.append(resp)

    # This assertion passed
    assert all(
        not r.last_chunk for r in stream_responses[:-1]
    ), "Some chunks before last have last_chunk=True"
    assert stream_responses[-1].last_chunk

    # Let's check this assertion
    for idx, response in enumerate(stream_responses[1:-1]):
        assert (
            len(response.answer) > 0
        ), f"Sent an empty answer {response} at index {idx+1}"

    # Verify metadata
    default_metadata = RAGResponseMetadata().model_dump()
    assert all(
        r.metadata.model_dump() == default_metadata for r in stream_responses[:-1]
    )
    last_response = stream_responses[-1]
    # TODO(@aminediro) : test responses with sources
    assert last_response.metadata.sources == []
    assert last_response.metadata.citations == []

    # Assert whole response makes sense
    assert "".join([r.answer for r in stream_responses]) == full_response
```

## File: `core/tests/test_utils.py`
```python
from uuid import uuid4

import pytest
from langchain_core.messages.ai import AIMessageChunk
from langchain_core.messages.tool import ToolCall
from quivr_core.rag.utils import (
    get_prev_message_str,
    model_supports_function_calling,
    parse_chunk_response,
)


def test_model_supports_function_calling():
    assert model_supports_function_calling("gpt-4") is True
    assert model_supports_function_calling("ollama3") is False


def test_get_prev_message_incorrect_message():
    with pytest.raises(StopIteration):
        chunk = AIMessageChunk(
            content="",
            tool_calls=[ToolCall(name="test", args={"answer": ""}, id=str(uuid4()))],
        )
        assert get_prev_message_str(chunk) == ""


def test_get_prev_message_str():
    chunk = AIMessageChunk(content="")
    assert get_prev_message_str(chunk) == ""
    # Test a correct chunk
    chunk = AIMessageChunk(
        content="",
        tool_calls=[
            ToolCall(
                name="cited_answer",
                args={"answer": "this is an answer"},
                id=str(uuid4()),
            )
        ],
    )
    assert get_prev_message_str(chunk) == "this is an answer"


def test_parse_chunk_response_nofunc_calling():
    rolling_msg = AIMessageChunk(content="")
    chunk = AIMessageChunk(content="next ")
    for i in range(10):
        rolling_msg, parsed_chunk, _ = parse_chunk_response(rolling_msg, chunk, False)
        assert rolling_msg.content == "next " * (i + 1)
        assert parsed_chunk == "next "


def _check_rolling_msg(rol_msg: AIMessageChunk) -> bool:
    return (
        len(rol_msg.tool_calls) > 0
        and rol_msg.tool_calls[0]["name"] == "cited_answer"
        and rol_msg.tool_calls[0]["args"] is not None
        and "answer" in rol_msg.tool_calls[0]["args"]
    )


def test_parse_chunk_response_func_calling(chunks_stream_answer):
    rolling_msg = AIMessageChunk(content="")

    rolling_msgs_history = []
    answer_str_history: list[str] = []

    for chunk in chunks_stream_answer:
        # Extract the AIMessageChunk from the chunk dictionary
        chunk_msg = chunk["answer"]  # Get the AIMessageChunk from the dict
        rolling_msg, answer_str, _ = parse_chunk_response(rolling_msg, chunk_msg, True)
        rolling_msgs_history.append(rolling_msg)
        answer_str_history.append(answer_str)

    # Checks that we accumulate into correctly
    last_rol_msg = None
    last_answer_chunk = None

    # TEST1:
    # Asserting that parsing accumulates the chunks
    for rol_msg in rolling_msgs_history:
        if last_rol_msg is not None:
            # Check tool_call_chunks accumulated correctly
            assert (
                len(rol_msg.tool_call_chunks) > 0
                and rol_msg.tool_call_chunks[0]["name"] == "cited_answer"
                and rol_msg.tool_call_chunks[0]["args"]
            )
            answer_chunk = rol_msg.tool_call_chunks[0]["args"]
            # assert that the answer is accumulated
            assert last_answer_chunk in answer_chunk

        if _check_rolling_msg(rol_msg):
            last_rol_msg = rol_msg
            last_answer_chunk = rol_msg.tool_call_chunks[0]["args"]

    # TEST2:
    # Progressively acc answer string
    assert all(
        answer_str_history[i] in answer_str_history[i + 1]
        for i in range(len(answer_str_history) - 1)
    )
    # NOTE: Last chunk's answer should match the accumulated history
    assert last_rol_msg.tool_calls[0]["args"]["answer"] == answer_str_history[-1]  # type: ignore
```

## File: `core/tests/processor/test_default_implementations.py`
```python
import pytest
from quivr_core.files.file import FileExtension
from quivr_core.processor.processor_base import ProcessorBase


@pytest.mark.base
def test___build_processor():
    from langchain_community.document_loaders.base import BaseLoader
    from quivr_core.processor.implementations.default import _build_processor

    cls = _build_processor("TestCLS", BaseLoader, [FileExtension.txt])

    assert cls.__name__ == "TestCLS"
    assert issubclass(cls, ProcessorBase)
    assert "__init__" in cls.__dict__
    assert cls.supported_extensions == [FileExtension.txt]
    proc = cls()
    assert hasattr(proc, "loader_cls")
    # FIXME: proper mypy typing
    assert proc.loader_cls == BaseLoader  # type: ignore
```

## File: `core/tests/processor/test_registry.py`
```python
import logging
from heapq import heappop

import pytest
from langchain_core.documents import Document
from quivr_core import registry
from quivr_core.files.file import FileExtension, QuivrFile
from quivr_core.processor.implementations.simple_txt_processor import SimpleTxtProcessor
from quivr_core.processor.implementations.tika_processor import TikaProcessor
from quivr_core.processor.processor_base import ProcessorBase
from quivr_core.processor.registry import (
    _LOWEST_PRIORITY,
    ProcEntry,
    ProcMapping,
    _append_proc_mapping,
    _import_class,
    available_processors,
    get_processor_class,
    known_processors,
    register_processor,
)


# TODO : reimplement when quivr-core will be its own package
@pytest.mark.skip(reason="TODO: reimplement when quivr-core will be its own package")
def test_get_default_processors_cls():
    from quivr_core.processor.implementations.default import TikTokenTxtProcessor

    cls = get_processor_class(FileExtension.txt)
    assert cls == TikTokenTxtProcessor

    cls = get_processor_class(FileExtension.pdf)
    # FIXME: using this class will actually fail if you don't have the
    assert cls == TikaProcessor


@pytest.mark.skip(reason="TODO: reimplement when quivr-core will be its own package")
def test_get_default_processors_cls_core():
    cls = get_processor_class(FileExtension.txt)
    assert cls == SimpleTxtProcessor

    cls = get_processor_class(FileExtension.pdf)
    assert cls == TikaProcessor


def test_append_proc_mapping_empty():
    proc_mapping = {}

    _append_proc_mapping(
        proc_mapping,
        file_ext=FileExtension.txt,
        cls_mod="test.test",
        errtxt="error",
        priority=None,
    )
    assert len(proc_mapping) == 1
    assert len(proc_mapping[FileExtension.txt]) == 1
    assert proc_mapping[FileExtension.txt][0] == ProcEntry(
        priority=_LOWEST_PRIORITY, cls_mod="test.test", err="error"
    )


def test_append_proc_mapping_priority():
    proc_mapping: ProcMapping = {
        FileExtension.txt: [
            ProcEntry(
                cls_mod="quivr_core.processor.implementations.simple_txt_processor.SimpleTxtProcessor",
                err=None,
                priority=_LOWEST_PRIORITY,
            )
        ],
    }
    _append_proc_mapping(
        proc_mapping,
        file_ext=FileExtension.txt,
        cls_mod="test.test",
        errtxt="error",
        priority=0,
    )

    assert len(proc_mapping[FileExtension.txt]) == 2
    # Procs are appended in order
    assert heappop(proc_mapping[FileExtension.txt]) == ProcEntry(
        priority=0, cls_mod="test.test", err="error"
    )


def test_append_proc_mapping():
    proc_mapping: ProcMapping = {
        FileExtension.txt: [
            ProcEntry(
                cls_mod="quivr_core.processor.implementations.simple_txt_processor.SimpleTxtProcessor",
                err=None,
                priority=_LOWEST_PRIORITY,
            )
        ],
    }
    _append_proc_mapping(
        proc_mapping,
        file_ext=FileExtension.txt,
        cls_mod="test.test",
        errtxt="error",
        priority=None,
    )

    assert len(proc_mapping[FileExtension.txt]) == 2
    # Procs are appended in order
    assert heappop(proc_mapping[FileExtension.txt]) == ProcEntry(
        priority=_LOWEST_PRIORITY - 1, cls_mod="test.test", err="error"
    )
    assert heappop(proc_mapping[FileExtension.txt]) == ProcEntry(
        cls_mod="quivr_core.processor.implementations.simple_txt_processor.SimpleTxtProcessor",
        err=None,
        priority=_LOWEST_PRIORITY,
    )


@pytest.mark.skip(
    reason="TODO: audio processors will be added to quivr-core very soon!"
)
def test_known_processors():
    assert all(
        ext in known_processors for ext in list(FileExtension)
    ), "base-env : Some file extensions don't have a default processor"


def test__import_class():
    mod_path = "quivr_core.processor.implementations.tika_processor.TikaProcessor"
    mod = _import_class(mod_path)
    assert mod == TikaProcessor

    with pytest.raises(TypeError, match=r".* is not a class"):
        mod_path = "quivr_core.processor"
        _import_class(mod_path)

    with pytest.raises(TypeError, match=r".* ProcessorBase"):
        mod_path = "quivr_core.Brain"
        _import_class(mod_path)


@pytest.mark.skip(reason="TODO: reimplement when quivr-core will be its own package")
def test_get_processor_cls_import_error(caplog):
    """
    Test in an environement where we only have the bare minimum parsers.
    The .html can't be parsed so we should raise an ImportError"""
    with pytest.raises(ImportError):
        get_processor_class(".html")


def test_get_processor_cls_error():
    with pytest.raises(ValueError):
        get_processor_class(".sdfkj")


@pytest.mark.skip("needs tox for separating side effects on other tests")
def test_register_new_proc_noappend():
    with pytest.raises(ValueError):
        register_processor(FileExtension.txt, "test.", append=False)


@pytest.mark.skip("needs tox for separating side effects on other tests")
def test_register_new_proc_append(caplog):
    n = len(known_processors[FileExtension.txt])
    register_processor(FileExtension.txt, "test.", append=True)
    assert len(known_processors[FileExtension.txt]) == n + 1

    with caplog.at_level(logging.INFO, logger="quivr_core"):
        register_processor(FileExtension.txt, "test.", append=True)
        assert caplog.record_tuples == [
            ("quivr_core", logging.INFO, "test. already in registry...")
        ]


@pytest.mark.skip("needs tox for separating side effects on other tests")
def test_register_new_proc():
    nprocs = len(registry)

    class TestProcessor(ProcessorBase):
        supported_extensions = [".test"]

        async def process_file(self, file: QuivrFile) -> list[Document]:
            return []

    register_processor(".test", TestProcessor)
    assert len(registry) == nprocs + 1

    cls = get_processor_class(".test")
    assert cls == TestProcessor


def test_register_non_processor():
    class NOTPROC:
        supported_extensions = [".pdf"]

    with pytest.raises(AssertionError):
        register_processor(".pdf", NOTPROC)  # type: ignore


def test_register_override_proc():
    class TestProcessor(ProcessorBase):
        supported_extensions = [".pdf"]

        @property
        def processor_metadata(self):
            return {}

        async def process_file_inner(self, file: QuivrFile) -> list[Document]:
            return []

    register_processor(".pdf", TestProcessor, override=True)
    cls = get_processor_class(FileExtension.pdf)
    assert cls == TestProcessor


def test_register_override_error():
    # Register class to pdf
    _ = get_processor_class(FileExtension.pdf)

    class TestProcessor(ProcessorBase):
        supported_extensions = [FileExtension.pdf]

        @property
        def processor_metadata(self):
            return {}

        async def process_file_inner(self, file: QuivrFile) -> list[Document]:
            return []

    with pytest.raises(ValueError):
        register_processor(".pdf", TestProcessor, override=False)


def test_available_processors():
    assert 17 == len(available_processors())
```

## File: `core/tests/processor/test_simple_txt_processor.py`
```python
import pytest
from langchain_core.documents import Document
from quivr_core.files.file import FileExtension
from quivr_core.processor.implementations.simple_txt_processor import (
    SimpleTxtProcessor,
    recursive_character_splitter,
)
from quivr_core.processor.splitter import SplitterConfig


def test_recursive_character_splitter():
    doc = Document(page_content="abcdefgh", metadata={"key": "value"})

    docs = recursive_character_splitter(doc, chunk_size=2, chunk_overlap=1)

    assert [d.page_content for d in docs] == ["ab", "bc", "cd", "de", "ef", "fg", "gh"]
    assert [d.metadata for d in docs] == [doc.metadata] * len(docs)


@pytest.mark.asyncio
async def test_simple_processor(quivr_pdf, quivr_txt):
    proc = SimpleTxtProcessor(
        splitter_config=SplitterConfig(chunk_size=100, chunk_overlap=20)
    )
    assert proc.supported_extensions == [FileExtension.txt]

    with pytest.raises(ValueError):
        await proc.process_file(quivr_pdf)

    docs = await proc.process_file(quivr_txt)

    assert len(docs) == 1
    assert docs[0].page_content == "This is some test data."
```

## File: `core/tests/processor/test_tika_processor.py`
```python
import pytest
from quivr_core.processor.implementations.tika_processor import TikaProcessor

# TODO: TIKA server should be set


@pytest.mark.tika
@pytest.mark.asyncio
async def test_process_file(quivr_pdf):
    tparser = TikaProcessor()
    doc = await tparser.process_file(quivr_pdf)
    assert len(doc) > 0
    assert doc[0].page_content.strip("\n") == "Dummy PDF download"


@pytest.mark.tika
@pytest.mark.asyncio
async def test_send_parse_tika_exception(quivr_pdf):
    # TODO: Mock correct tika for retries
    tparser = TikaProcessor(tika_url="test.test")
    with pytest.raises(RuntimeError):
        doc = await tparser.process_file(quivr_pdf)
        assert len(doc) > 0
        assert doc[0].page_content.strip("\n") == "Dummy PDF download"
```

## File: `core/tests/processor/test_txt_processor.py`
```python
from uuid import uuid4

import pytest
from quivr_core.storage.file import FileExtension, QuivrFile

unstructured = pytest.importorskip("unstructured")


@pytest.fixture
def txt_qfile(temp_data_file):
    return QuivrFile(
        id=uuid4(),
        brain_id=uuid4(),
        original_filename="data.txt",
        path=temp_data_file,
        file_extension=FileExtension.txt,
        file_sha1="hash",
    )


@pytest.mark.base
@pytest.mark.asyncio
async def test_process_txt(txt_qfile):
    from quivr_core.processor.implementations.default import TikTokenTxtProcessor
    from quivr_core.processor.splitter import SplitterConfig

    tparser = TikTokenTxtProcessor(
        splitter_config=SplitterConfig(chunk_size=20, chunk_overlap=0)
    )
    doc = await tparser.process_file(txt_qfile)
    assert len(doc) > 0
    assert doc[0].page_content == "This is some test data."
    assert (
        doc[0].metadata.items()
        >= {
            "chunk_index": 1,
            "original_file_name": "data.txt",
            "chunk_size": 6,
            "processor_cls": "TextLoader",
            "splitter": {"chunk_size": 20, "chunk_overlap": 0},
            **txt_qfile.metadata,
        }.items()
    )
```

## File: `core/tests/processor/community/test_markdown_processor.py`
```python
from pathlib import Path
from uuid import uuid4

import pytest
from quivr_core.files.file import FileExtension, QuivrFile
from quivr_core.processor.implementations.default import MarkdownProcessor

unstructured = pytest.importorskip("unstructured")


@pytest.mark.unstructured
@pytest.mark.asyncio
async def test_markdown_processor():
    p = Path("./tests/processor/data/guidelines_code.md")
    f = QuivrFile(
        id=uuid4(),
        brain_id=uuid4(),
        original_filename=p.stem,
        path=p,
        file_extension=FileExtension.md,
        file_sha1="123",
    )
    processor = MarkdownProcessor()
    result = await processor.process_file(f)
    assert len(result) > 0


@pytest.mark.unstructured
@pytest.mark.asyncio
async def test_markdown_processor_fail(quivr_txt):
    processor = MarkdownProcessor()
    with pytest.raises(ValueError):
        await processor.process_file(quivr_txt)
```

## File: `core/tests/processor/data/guidelines_code.md`
```markdown
# Backend code guidelines

## **Code Structure and Organization**

- Follow a clear project structure :
    - In quivr-api we have modules divided into : controller, entity, services, repositories, utils)
- **Use dependency injection for better testability and modularity** 🔺
- Use environment variables for configuration 🔺
    - We use Pydantic settings for parsing the arguments
- Don’t add unnecessary abstractions → **KISS principle.**
    - Premature abstractions are a bad pattern
- Avoid using Global Scoped Objects 🔺🔺🔺
- Understand the implications of using the following syntax: 🔺🔺🔺
    - Context manager :
    - Wrapper functions and High order Function
    - Generator / AsyncGenerators
    - ThreadPools and ProcessPool
    - Asynchronous code
- Don’t replicate object that are Standalone/Singleton or with heavy dependencies. All python objects are references. Use the references: 🔺🔺🔺
    - **Example**: Recreating a `BrainService`  inside a function is an antipattern. This function should take `service : BrainService` as a parameter ( also easily testable via dependency injection)
    - **Example**: Recreating a class that connects to a `APIService` is an antipattern. Connection creation is pretty costly process. You should the a **single object** and pass it accross function calls
- Error handling:
    - Use specific exception types rather than catching all exceptions. The caller can then `try .. except CustomException`
    - Create custom exception classes for **application-specific errors.**
    - Add logs when Errors are catched for better debugging

        ```python
        try:
            result = perform_operation()
        except OperationError as e:
            log.error(f"Operation failed: {str(e)}")
            return error_response()
        ```

    - Consider using **assertion statements ! IMHO this is really important** 🔺. Checkout : https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/TIGER_STYLE.md#safety

**(Advanced):**

- Try encoding business pattern in Type ( known as Typestate pattern):
    - For example if a File can either be in Open or Close state → use two Types OpenFile and CloseFile with separate behaviour to avoid calling methods on a closed file.
- May need to consider adding route level exception handling to FastAPI

## **Database and ORM**

- Use SQLModel for all database operations:
    - SQlmodel docs : [https://sqlmodel.tiangolo.com/](https://sqlmodel.tiangolo.com/)
    - Use **eager** or **lazy** relationship for modeling 1-many and many-many relationships depending on join cost
    - Be aware of async session and lazy attributes
- Use async as much as possible
- Think about access patterns in your code :  🔺🔺🔺
    - Reduce n+1 calls : If we can get the information with a single query, we do it in a single query

    > **Always ask if this chunk of call can be done via a single SQL query !**
    >
    - Batch writes to the database. If we Insert N times in a loop → 1 insert many !
    - Write database queries with proper indexing in mind.
        - Example : Do we need to filter results ? If yes then add a WHERE clause …
        - Do we frequently filter on some attribute → Add index.
        - Think about which index :BTreeIndex when ordered access, HashIndex where data is really dissimilar and we need extremely fast access …
    - Think about Joins. If we do 2 queries to get the data then maybe we can do it in one :
        - For example User/UserSettings/UserUsage. We can get all of this info eagerly when accessing user.

            > DB side fetching is FAST ! Network is slow !
            >
- Think about atomic guarantees and transactions in the whole workflow
    - Example : deleting a knowledge and its vectors should be atomic

## **API and External Services**

- When sending requests to external services (APIs), always include:
    - Defined timeouts
    - Backoff policy
    - Retry mechanism
    - Conversion of HTTP errors to business-level exceptions
- Use a circuit breaker pattern for frequently called external services
- Implement proper **error handling and logging**

## **HTTP and Routing**

- Keep HTTP logic confined to the routes layer
- Raise HTTP errors only through FastAPI
- Use appropriate HTTP status codes consistently with
- Implement request validation at the API entry point

## **Performance**

- Use caching mechanisms where appropriate (e.g., Redis)
- Implement pagination for list endpoints
- Use asynchronous programming where beneficial
    - Keep in mind that python is single threaded !
- Avoid unnecessary serialization/deserialization
- Optimize database queries and use indexing effectively
- For performance critical code :
    - Use libraries that are True wrappers (ie don’t call subprocess)
    - Use libraries that  release the GIL
    - Use Threadpools and ProcessPool when possible
    - Be aware of libraries spawning their own threadpool !!!!
- Understand underlying systems : networks, disk access, operating system syscalls

## **Testing**

- Write unit tests for all business logic. The code should be written with dependency injection in mind !
- Write unit test for repositories:
    - Use the rollback session fixture ( see ChatHistory tests)
    - Test with different configurations of Brain types, User settings, … → Use parametrized test for this
- Implement integration tests for API endpoints
    - FastAPI testclient :  https://fastapi.tiangolo.com/tutorial/testing/
- Use mocking for external services in tests.

## **Logging and Monitoring**

- Implement structured logging
- *TODO: define where and how*

## **Security**

- Implement input validation and sanitization
- Use parameterized queries to prevent SQL injection
- Implement rate limiting for API endpoints
- Regularly update dependencies and address security vulnerabilities

## **Documentation**

- Maintain a README with setup and run instructions
- Document all non-obvious code sections

## **Version Control and CI/CD**

- Use feature branches and pull requests
- Keep a changelog for version control
- Implement automated CI/CD pipelines
- **Perform code reviews for all changes**
```

## File: `core/tests/processor/docx/test_docx.py`
```python
from pathlib import Path
from uuid import uuid4

import pytest
from quivr_core.files.file import FileExtension, QuivrFile
from quivr_core.processor.implementations.default import DOCXProcessor

unstructured = pytest.importorskip("unstructured")


@pytest.mark.unstructured
@pytest.mark.asyncio
async def test_docx_filedocx():
    p = Path("./tests/processor/docx/demo.docx")
    f = QuivrFile(
        id=uuid4(),
        brain_id=uuid4(),
        original_filename=p.stem,
        path=p,
        file_extension=FileExtension.docx,
        file_sha1="123",
    )
    processor = DOCXProcessor()
    result = await processor.process_file(f)
    assert len(result) > 0


@pytest.mark.unstructured
@pytest.mark.asyncio
async def test_docx_processor_fail(quivr_txt):
    processor = DOCXProcessor()
    with pytest.raises(ValueError):
        await processor.process_file(quivr_txt)
```

## File: `core/tests/processor/epub/test_epub_processor.py`
```python
from pathlib import Path
from uuid import uuid4

import pytest
from quivr_core.files.file import FileExtension, QuivrFile
from quivr_core.processor.implementations.default import EpubProcessor

unstructured = pytest.importorskip("unstructured")


@pytest.mark.unstructured
@pytest.mark.asyncio
async def test_epub_page_blanche():
    p = Path("./tests/processor/epub/page-blanche.epub")
    f = QuivrFile(
        id=uuid4(),
        brain_id=uuid4(),
        original_filename=p.stem,
        path=p,
        file_extension=FileExtension.epub,
        file_sha1="123",
    )
    processor = EpubProcessor()
    result = await processor.process_file(f)
    assert len(result) == 0


@pytest.mark.unstructured
@pytest.mark.asyncio
async def test_epub_processor():
    p = Path("./tests/processor/epub/sway.epub")
    f = QuivrFile(
        id=uuid4(),
        brain_id=uuid4(),
        original_filename=p.stem,
        path=p,
        file_extension=FileExtension.epub,
        file_sha1="123",
    )

    processor = EpubProcessor()
    result = await processor.process_file(f)
    assert len(result) > 0


@pytest.mark.unstructured
@pytest.mark.asyncio
async def test_epub_processor_fail(quivr_txt):
    processor = EpubProcessor()
    with pytest.raises(ValueError):
        await processor.process_file(quivr_txt)
```

## File: `core/tests/processor/odt/bad_odt.odt`
```
<!DOCTYPE html><html><head> <meta charset="UTF-8"> <title>File Examples | Download redirect...</title> <meta name="description" content="Download redirect page." > <meta name="viewport" content="width=device-width, initial-scale=1"> <link href="https://fonts.googleapis.com/css?family=Catamaran:100,200,300,400,500,600,700,800,900" rel="stylesheet"> <style>h2{font-family: Catamaran,Helvetica,Arial,sans-serif; font-weight: 200; font-size: 50px; color: #333;}section{padding-top: 10%; max-width:100%; text-align: center;}a{color: #00CC66;}a:focus{outline:none; outline-offset:inherit;}@media (max-device-width: 1027px){body{text-align:center; font-size:larger;}section{max-width: 90%;}}@media (max-device-width: 640px){section{max-width: 97%;}}</style></head><body> <section> <h2>Downloading...</h2> <em>Please wait a moment</em><br/><br/><script>document.write('<a href="' + document.referrer + '">[Go Back]</a>');</script></section><script>document.addEventListener('DOMContentLoaded', function(){setTimeout(function (){url=window.location.href.replace('file-examples.com/wp-content/storage/','file-examples.com/storage/fe8a1df88b669e6bf987ef5/'); window.location.replace(url);}, 3000);}, false);</script></body></html>
```

## File: `core/tests/processor/odt/test_odt.py`
```python
from pathlib import Path
from uuid import uuid4

import pytest
from quivr_core.files.file import FileExtension, QuivrFile
from quivr_core.processor.implementations.default import ODTProcessor

unstructured = pytest.importorskip("unstructured")


@pytest.mark.unstructured
@pytest.mark.asyncio
async def test_odt_processor():
    p = Path("./tests/processor/odt/sample.odt")
    f = QuivrFile(
        id=uuid4(),
        brain_id=uuid4(),
        original_filename=p.stem,
        path=p,
        file_extension=FileExtension.odt,
        file_sha1="123",
    )
    processor = ODTProcessor()
    result = await processor.process_file(f)
    assert len(result) > 0


@pytest.mark.unstructured
@pytest.mark.asyncio
async def test_odt_processor_fail():
    p = Path("./tests/processor/odt/bad_odt.odt")
    f = QuivrFile(
        id=uuid4(),
        brain_id=uuid4(),
        original_filename=p.stem,
        path=p,
        file_extension=FileExtension.txt,
        file_sha1="123",
    )
    processor = ODTProcessor()
    with pytest.raises(ValueError):
        await processor.process_file(f)
```

## File: `core/tests/processor/pdf/test_unstructured_pdf_processor.py`
```python
from pathlib import Path
from uuid import uuid4

import pytest
from quivr_core.files.file import FileExtension, QuivrFile

unstructured = pytest.importorskip("unstructured")

all_but_pdf = list(filter(lambda ext: ext != ".pdf", list(FileExtension)))


@pytest.mark.unstructured
@pytest.mark.asyncio
async def test_unstructured_pdf_processor():
    from quivr_core.processor.implementations.default import UnstructuredPDFProcessor

    p = Path("./tests/processor/pdf/sample.pdf")
    f = QuivrFile(
        id=uuid4(),
        brain_id=uuid4(),
        original_filename=p.stem,
        path=p,
        file_extension=FileExtension.pdf,
        file_sha1="123",
    )
    processor = UnstructuredPDFProcessor()
    result = await processor.process_file(f)
    assert len(result) > 0


@pytest.mark.unstructured
@pytest.mark.parametrize("ext", all_but_pdf)
@pytest.mark.asyncio
async def test_unstructured_pdf_processor_fail(ext):
    from quivr_core.processor.implementations.default import UnstructuredPDFProcessor

    p = Path("./tests/processor/pdf/sample.pdf")
    f = QuivrFile(
        id=uuid4(),
        brain_id=uuid4(),
        original_filename=p.stem,
        path=p,
        file_extension=ext,
        file_sha1="123",
    )
    processor = UnstructuredPDFProcessor()
    with pytest.raises(ValueError):
        await processor.process_file(f)
```

## File: `docs/.gitignore`
```
# python generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# venv
.venv
```

## File: `docs/.python-version`
```
3.11.9
```

## File: `docs/README.md`
```markdown
# docs

Describe your project here.
```

## File: `docs/mkdocs.yml`
```yaml
site_name: Quivr
extra_css:
  - css/style.css

markdown_extensions:
  - attr_list
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - md_in_html
  - toc:
      permalink: "#"

theme:
  custom_dir: overrides
  features:
    - navigation.instant
    - navigation.tabs
    - navigation.indexes
    - navigation.top
    - navigation.footer
    - toc.follow
    - content.code.copy
    - search.suggest
    - search.highlight
  name: material
  palette:
    - media: (prefers-color-scheme)
      toggle:
        icon: material/brightness-auto
        name: Switch to light mode
    - accent: purple
      media: "(prefers-color-scheme: light)"
      primary: white
      scheme: default
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - accent: purple
      media: "(prefers-color-scheme: dark)"
      primary: black
      scheme: slate
      toggle:
        icon: material/brightness-4
        name: Switch to system preference

plugins:
  - search
  - mkdocstrings:
      default_handler: python
      handlers:
        python:
          docstring_style: google
          options:
            show_source: false
            heading_level: 2
            separate_signature: true

nav:
  - Home:
      - index.md
      - quickstart.md
      - Brain:
          - brain/index.md
          - brain/brain.md
          - brain/chat.md
      - Storage:
          - storage/index.md
          - storage/base.md
          - storage/local_storage.md
      - Parsers:
          - parsers/index.md
          - parsers/megaparse.md
          - parsers/simple.md
      - Vector Stores:
          - vectorstores/index.md
          - vectorstores/faiss.md
          - vectorstores/pgvector.md
      - Workflows:
          - workflows/index.md
          - Examples:
              - workflows/examples/basic_ingestion.md
              - workflows/examples/basic_rag.md
              - workflows/examples/rag_with_web_search.md
      - Configuration:
          - config/index.md
          - config/config.md
          - config/base_config.md
      - Examples:
          - examples/index.md
          - examples/custom_storage.md
          - examples/chatbot.md
          - examples/chatbot_voice.md
          - examples/chatbot_voice_flask.md
  - Enterprise: https://docs.quivr.app/
```

## File: `docs/pyproject.toml`
```
[project]
name = "docs"
version = "0.1.0"
description = "Add your description here"
authors = [
    { name = "Stan Girard", email = "stan@quivr.app" }
]
dependencies = [
    "quivr-core @ file:///${PROJECT_ROOT}/../core",
    "mkdocs>=1.6.1",
    "mkdocstrings[python]>=0.26.0",
    "mkdocs-jupyter>=0.24.8",
    "mkdocs-include-dir-to-nav>=1.2.0",
    "mkdocs-material>=9.5.34",
    "mkdocs-redirects>=1.2.1",
]
readme = "README.md"
requires-python = ">= 3.8"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.rye]
managed = true
dev-dependencies = []
virtual = true

[tool.rye.scripts]
docs = "mkdocs serve"
build_docs = "mkdocs build --strict"

[tool.basedpyright]
include = ["src/"]
# Ensure that it uses the .venv that we created for this project with the lockfile
venvPath="./"
venv=".venv"
# We really only care about some import issues, so we disable everything and report on missing imports:
typeCheckingMode = "off"
reportMissingImports = true


[tool.hatch.metadata]
allow-direct-references = true
```

## File: `docs/requirements-dev.lock`
```
# generated by rye
# use `rye lock` or `rye sync` to update this lockfile
#
# last locked with the following flags:
#   pre: false
#   features: []
#   all-features: false
#   with-sources: false
#   generate-hashes: false
#   universal: false

aiofiles==24.1.0
    # via quivr-core
aiohappyeyeballs==2.4.3
    # via aiohttp
aiohttp==3.10.10
    # via langchain
    # via langchain-community
aiosignal==1.3.1
    # via aiohttp
annotated-types==0.7.0
    # via pydantic
anthropic==0.40.0
    # via langchain-anthropic
anyio==4.6.2.post1
    # via anthropic
    # via httpx
    # via openai
appnope==0.1.4
    # via ipykernel
asttokens==2.4.1
    # via stack-data
attrs==24.2.0
    # via aiohttp
    # via jsonschema
    # via referencing
babel==2.16.0
    # via mkdocs-material
beautifulsoup4==4.12.3
    # via nbconvert
bleach==6.1.0
    # via nbconvert
certifi==2024.8.30
    # via httpcore
    # via httpx
    # via requests
charset-normalizer==3.3.2
    # via requests
click==8.1.7
    # via mkdocs
    # via mkdocstrings
cohere==5.13.2
    # via langchain-cohere
colorama==0.4.6
    # via griffe
    # via mkdocs-material
comm==0.2.2
    # via ipykernel
dataclasses-json==0.6.7
    # via langchain-community
debugpy==1.8.5
    # via ipykernel
decorator==5.1.1
    # via ipython
defusedxml==0.7.1
    # via langchain-anthropic
    # via nbconvert
distro==1.9.0
    # via anthropic
    # via openai
executing==2.1.0
    # via stack-data
faiss-cpu==1.9.0.post1
    # via quivr-core
fastavro==1.9.7
    # via cohere
fastjsonschema==2.20.0
    # via nbformat
filelock==3.16.1
    # via huggingface-hub
    # via transformers
frozenlist==1.4.1
    # via aiohttp
    # via aiosignal
fsspec==2024.9.0
    # via huggingface-hub
ghp-import==2.1.0
    # via mkdocs
griffe==1.2.0
    # via mkdocstrings-python
h11==0.14.0
    # via httpcore
httpcore==1.0.6
    # via httpx
httpx==0.27.2
    # via anthropic
    # via cohere
    # via langchain-mistralai
    # via langgraph-sdk
    # via langsmith
    # via megaparse-sdk
    # via openai
    # via quivr-core
httpx-sse==0.4.0
    # via cohere
    # via langchain-community
    # via langchain-mistralai
    # via langgraph-sdk
huggingface-hub==0.25.2
    # via tokenizers
    # via transformers
idna==3.8
    # via anyio
    # via httpx
    # via requests
    # via yarl
ipykernel==6.29.5
    # via mkdocs-jupyter
ipython==8.27.0
    # via ipykernel
jedi==0.19.1
    # via ipython
jinja2==3.1.4
    # via mkdocs
    # via mkdocs-material
    # via mkdocstrings
    # via nbconvert
jiter==0.6.1
    # via anthropic
    # via openai
jsonpatch==1.33
    # via langchain-core
jsonpointer==3.0.0
    # via jsonpatch
jsonschema==4.23.0
    # via nbformat
jsonschema-specifications==2023.12.1
    # via jsonschema
jupyter-client==8.6.2
    # via ipykernel
    # via nbclient
jupyter-core==5.7.2
    # via ipykernel
    # via jupyter-client
    # via nbclient
    # via nbconvert
    # via nbformat
jupyterlab-pygments==0.3.0
    # via nbconvert
jupytext==1.16.4
    # via mkdocs-jupyter
langchain==0.3.9
    # via langchain-community
    # via quivr-core
langchain-anthropic==0.3.0
    # via quivr-core
langchain-cohere==0.3.3
    # via quivr-core
langchain-community==0.3.9
    # via langchain-experimental
    # via quivr-core
langchain-core==0.3.21
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-community
    # via langchain-experimental
    # via langchain-mistralai
    # via langchain-openai
    # via langchain-text-splitters
    # via langgraph
    # via langgraph-checkpoint
    # via quivr-core
langchain-experimental==0.3.3
    # via langchain-cohere
langchain-mistralai==0.2.3
    # via quivr-core
langchain-openai==0.2.11
    # via quivr-core
langchain-text-splitters==0.3.2
    # via langchain
langgraph==0.2.38
    # via quivr-core
langgraph-checkpoint==2.0.1
    # via langgraph
langgraph-sdk==0.1.33
    # via langgraph
langsmith==0.1.135
    # via langchain
    # via langchain-community
    # via langchain-core
loguru==0.7.2
    # via megaparse-sdk
markdown==3.7
    # via mkdocs
    # via mkdocs-autorefs
    # via mkdocs-material
    # via mkdocstrings
    # via pymdown-extensions
markdown-it-py==3.0.0
    # via jupytext
    # via mdit-py-plugins
    # via rich
markupsafe==2.1.5
    # via jinja2
    # via mkdocs
    # via mkdocs-autorefs
    # via mkdocstrings
    # via nbconvert
    # via quivr-core
marshmallow==3.22.0
    # via dataclasses-json
matplotlib-inline==0.1.7
    # via ipykernel
    # via ipython
mdit-py-plugins==0.4.1
    # via jupytext
mdurl==0.1.2
    # via markdown-it-py
megaparse-sdk==0.1.10
    # via quivr-core
mergedeep==1.3.4
    # via mkdocs
    # via mkdocs-get-deps
mistune==3.0.2
    # via nbconvert
mkdocs==1.6.1
    # via mkdocs-autorefs
    # via mkdocs-include-dir-to-nav
    # via mkdocs-jupyter
    # via mkdocs-material
    # via mkdocs-redirects
    # via mkdocstrings
mkdocs-autorefs==1.2.0
    # via mkdocstrings
    # via mkdocstrings-python
mkdocs-get-deps==0.2.0
    # via mkdocs
mkdocs-include-dir-to-nav==1.2.0
mkdocs-jupyter==0.24.8
mkdocs-material==9.5.34
    # via mkdocs-jupyter
mkdocs-material-extensions==1.3.1
    # via mkdocs-material
mkdocs-redirects==1.2.1
mkdocstrings==0.26.0
    # via mkdocstrings-python
mkdocstrings-python==1.10.9
    # via mkdocstrings
msgpack==1.1.0
    # via langgraph-checkpoint
multidict==6.1.0
    # via aiohttp
    # via yarl
mypy-extensions==1.0.0
    # via typing-inspect
nats-py==2.9.0
    # via megaparse-sdk
nbclient==0.10.0
    # via nbconvert
nbconvert==7.16.4
    # via mkdocs-jupyter
nbformat==5.10.4
    # via jupytext
    # via nbclient
    # via nbconvert
nest-asyncio==1.6.0
    # via ipykernel
numpy==1.26.4
    # via faiss-cpu
    # via langchain
    # via langchain-community
    # via pandas
    # via transformers
openai==1.56.2
    # via langchain-openai
orjson==3.10.7
    # via langgraph-sdk
    # via langsmith
packaging==24.1
    # via faiss-cpu
    # via huggingface-hub
    # via ipykernel
    # via jupytext
    # via langchain-core
    # via marshmallow
    # via mkdocs
    # via nbconvert
    # via transformers
paginate==0.5.7
    # via mkdocs-material
pandas==2.2.3
    # via langchain-cohere
pandocfilters==1.5.1
    # via nbconvert
parameterized==0.9.0
    # via cohere
parso==0.8.4
    # via jedi
pathspec==0.12.1
    # via mkdocs
pexpect==4.9.0
    # via ipython
platformdirs==4.2.2
    # via jupyter-core
    # via mkdocs-get-deps
    # via mkdocstrings
prompt-toolkit==3.0.47
    # via ipython
propcache==0.2.0
    # via yarl
protobuf==5.28.2
    # via transformers
psutil==6.1.0
    # via ipykernel
    # via megaparse-sdk
ptyprocess==0.7.0
    # via pexpect
pure-eval==0.2.3
    # via stack-data
pycryptodome==3.21.0
    # via megaparse-sdk
pydantic==2.9.2
    # via anthropic
    # via cohere
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-core
    # via langchain-mistralai
    # via langsmith
    # via openai
    # via pydantic-settings
    # via quivr-core
pydantic-core==2.23.4
    # via cohere
    # via pydantic
pydantic-settings==2.6.1
    # via langchain-community
pygments==2.18.0
    # via ipython
    # via mkdocs-jupyter
    # via mkdocs-material
    # via nbconvert
    # via rich
pymdown-extensions==10.9
    # via mkdocs-material
    # via mkdocstrings
python-dateutil==2.9.0.post0
    # via ghp-import
    # via jupyter-client
    # via pandas
python-dotenv==1.0.1
    # via megaparse-sdk
    # via pydantic-settings
pytz==2024.2
    # via pandas
pyyaml==6.0.2
    # via huggingface-hub
    # via jupytext
    # via langchain
    # via langchain-community
    # via langchain-core
    # via mkdocs
    # via mkdocs-get-deps
    # via pymdown-extensions
    # via pyyaml-env-tag
    # via transformers
pyyaml-env-tag==0.1
    # via mkdocs
pyzmq==26.2.0
    # via ipykernel
    # via jupyter-client
quivr-core @ file:///${PROJECT_ROOT}/../core
rapidfuzz==3.10.1
    # via quivr-core
referencing==0.35.1
    # via jsonschema
    # via jsonschema-specifications
regex==2024.7.24
    # via mkdocs-material
    # via tiktoken
    # via transformers
requests==2.32.3
    # via cohere
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langsmith
    # via mkdocs-material
    # via requests-toolbelt
    # via tiktoken
    # via transformers
requests-toolbelt==1.0.0
    # via langsmith
rich==13.9.2
    # via quivr-core
rpds-py==0.20.0
    # via jsonschema
    # via referencing
safetensors==0.4.5
    # via transformers
sentencepiece==0.2.0
    # via transformers
six==1.16.0
    # via asttokens
    # via bleach
    # via python-dateutil
sniffio==1.3.1
    # via anthropic
    # via anyio
    # via httpx
    # via openai
soupsieve==2.6
    # via beautifulsoup4
sqlalchemy==2.0.36
    # via langchain
    # via langchain-community
stack-data==0.6.3
    # via ipython
tabulate==0.9.0
    # via langchain-cohere
tenacity==8.5.0
    # via langchain
    # via langchain-community
    # via langchain-core
tiktoken==0.8.0
    # via langchain-openai
    # via quivr-core
tinycss2==1.3.0
    # via nbconvert
tokenizers==0.20.1
    # via cohere
    # via langchain-mistralai
    # via transformers
tornado==6.4.1
    # via ipykernel
    # via jupyter-client
tqdm==4.66.5
    # via huggingface-hub
    # via openai
    # via transformers
traitlets==5.14.3
    # via comm
    # via ipykernel
    # via ipython
    # via jupyter-client
    # via jupyter-core
    # via matplotlib-inline
    # via nbclient
    # via nbconvert
    # via nbformat
transformers==4.45.2
    # via quivr-core
types-pyyaml==6.0.12.20240917
    # via quivr-core
types-requests==2.32.0.20241016
    # via cohere
typing-extensions==4.12.2
    # via anthropic
    # via cohere
    # via huggingface-hub
    # via ipython
    # via langchain-core
    # via openai
    # via pydantic
    # via pydantic-core
    # via sqlalchemy
    # via typing-inspect
typing-inspect==0.9.0
    # via dataclasses-json
tzdata==2024.2
    # via pandas
urllib3==2.2.2
    # via requests
    # via types-requests
watchdog==5.0.0
    # via mkdocs
wcwidth==0.2.13
    # via prompt-toolkit
webencodings==0.5.1
    # via bleach
    # via tinycss2
yarl==1.15.4
    # via aiohttp
```

## File: `docs/requirements.lock`
```
# generated by rye
# use `rye lock` or `rye sync` to update this lockfile
#
# last locked with the following flags:
#   pre: false
#   features: []
#   all-features: false
#   with-sources: false
#   generate-hashes: false
#   universal: false

aiofiles==24.1.0
    # via quivr-core
aiohappyeyeballs==2.4.3
    # via aiohttp
aiohttp==3.10.10
    # via langchain
    # via langchain-community
aiosignal==1.3.1
    # via aiohttp
annotated-types==0.7.0
    # via pydantic
anthropic==0.40.0
    # via langchain-anthropic
anyio==4.6.2.post1
    # via anthropic
    # via httpx
    # via openai
appnope==0.1.4
    # via ipykernel
asttokens==2.4.1
    # via stack-data
attrs==24.2.0
    # via aiohttp
    # via jsonschema
    # via referencing
babel==2.16.0
    # via mkdocs-material
beautifulsoup4==4.12.3
    # via nbconvert
bleach==6.1.0
    # via nbconvert
certifi==2024.8.30
    # via httpcore
    # via httpx
    # via requests
charset-normalizer==3.3.2
    # via requests
click==8.1.7
    # via mkdocs
    # via mkdocstrings
cohere==5.13.2
    # via langchain-cohere
colorama==0.4.6
    # via griffe
    # via mkdocs-material
comm==0.2.2
    # via ipykernel
dataclasses-json==0.6.7
    # via langchain-community
debugpy==1.8.5
    # via ipykernel
decorator==5.1.1
    # via ipython
defusedxml==0.7.1
    # via langchain-anthropic
    # via nbconvert
distro==1.9.0
    # via anthropic
    # via openai
executing==2.1.0
    # via stack-data
faiss-cpu==1.9.0.post1
    # via quivr-core
fastavro==1.9.7
    # via cohere
fastjsonschema==2.20.0
    # via nbformat
filelock==3.16.1
    # via huggingface-hub
    # via transformers
frozenlist==1.4.1
    # via aiohttp
    # via aiosignal
fsspec==2024.9.0
    # via huggingface-hub
ghp-import==2.1.0
    # via mkdocs
griffe==1.2.0
    # via mkdocstrings-python
h11==0.14.0
    # via httpcore
httpcore==1.0.6
    # via httpx
httpx==0.27.2
    # via anthropic
    # via cohere
    # via langchain-mistralai
    # via langgraph-sdk
    # via langsmith
    # via megaparse-sdk
    # via openai
    # via quivr-core
httpx-sse==0.4.0
    # via cohere
    # via langchain-community
    # via langchain-mistralai
    # via langgraph-sdk
huggingface-hub==0.25.2
    # via tokenizers
    # via transformers
idna==3.8
    # via anyio
    # via httpx
    # via requests
    # via yarl
ipykernel==6.29.5
    # via mkdocs-jupyter
ipython==8.27.0
    # via ipykernel
jedi==0.19.1
    # via ipython
jinja2==3.1.4
    # via mkdocs
    # via mkdocs-material
    # via mkdocstrings
    # via nbconvert
jiter==0.6.1
    # via anthropic
    # via openai
jsonpatch==1.33
    # via langchain-core
jsonpointer==3.0.0
    # via jsonpatch
jsonschema==4.23.0
    # via nbformat
jsonschema-specifications==2023.12.1
    # via jsonschema
jupyter-client==8.6.2
    # via ipykernel
    # via nbclient
jupyter-core==5.7.2
    # via ipykernel
    # via jupyter-client
    # via nbclient
    # via nbconvert
    # via nbformat
jupyterlab-pygments==0.3.0
    # via nbconvert
jupytext==1.16.4
    # via mkdocs-jupyter
langchain==0.3.9
    # via langchain-community
    # via quivr-core
langchain-anthropic==0.3.0
    # via quivr-core
langchain-cohere==0.3.3
    # via quivr-core
langchain-community==0.3.9
    # via langchain-experimental
    # via quivr-core
langchain-core==0.3.21
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-community
    # via langchain-experimental
    # via langchain-mistralai
    # via langchain-openai
    # via langchain-text-splitters
    # via langgraph
    # via langgraph-checkpoint
    # via quivr-core
langchain-experimental==0.3.3
    # via langchain-cohere
langchain-mistralai==0.2.3
    # via quivr-core
langchain-openai==0.2.11
    # via quivr-core
langchain-text-splitters==0.3.2
    # via langchain
langgraph==0.2.38
    # via quivr-core
langgraph-checkpoint==2.0.1
    # via langgraph
langgraph-sdk==0.1.33
    # via langgraph
langsmith==0.1.135
    # via langchain
    # via langchain-community
    # via langchain-core
loguru==0.7.2
    # via megaparse-sdk
markdown==3.7
    # via mkdocs
    # via mkdocs-autorefs
    # via mkdocs-material
    # via mkdocstrings
    # via pymdown-extensions
markdown-it-py==3.0.0
    # via jupytext
    # via mdit-py-plugins
    # via rich
markupsafe==2.1.5
    # via jinja2
    # via mkdocs
    # via mkdocs-autorefs
    # via mkdocstrings
    # via nbconvert
    # via quivr-core
marshmallow==3.22.0
    # via dataclasses-json
matplotlib-inline==0.1.7
    # via ipykernel
    # via ipython
mdit-py-plugins==0.4.1
    # via jupytext
mdurl==0.1.2
    # via markdown-it-py
megaparse-sdk==0.1.10
    # via quivr-core
mergedeep==1.3.4
    # via mkdocs
    # via mkdocs-get-deps
mistune==3.0.2
    # via nbconvert
mkdocs==1.6.1
    # via mkdocs-autorefs
    # via mkdocs-include-dir-to-nav
    # via mkdocs-jupyter
    # via mkdocs-material
    # via mkdocs-redirects
    # via mkdocstrings
mkdocs-autorefs==1.2.0
    # via mkdocstrings
    # via mkdocstrings-python
mkdocs-get-deps==0.2.0
    # via mkdocs
mkdocs-include-dir-to-nav==1.2.0
mkdocs-jupyter==0.24.8
mkdocs-material==9.5.34
    # via mkdocs-jupyter
mkdocs-material-extensions==1.3.1
    # via mkdocs-material
mkdocs-redirects==1.2.1
mkdocstrings==0.26.0
    # via mkdocstrings-python
mkdocstrings-python==1.10.9
    # via mkdocstrings
msgpack==1.1.0
    # via langgraph-checkpoint
multidict==6.1.0
    # via aiohttp
    # via yarl
mypy-extensions==1.0.0
    # via typing-inspect
nats-py==2.9.0
    # via megaparse-sdk
nbclient==0.10.0
    # via nbconvert
nbconvert==7.16.4
    # via mkdocs-jupyter
nbformat==5.10.4
    # via jupytext
    # via nbclient
    # via nbconvert
nest-asyncio==1.6.0
    # via ipykernel
numpy==1.26.4
    # via faiss-cpu
    # via langchain
    # via langchain-community
    # via pandas
    # via transformers
openai==1.56.2
    # via langchain-openai
orjson==3.10.7
    # via langgraph-sdk
    # via langsmith
packaging==24.1
    # via faiss-cpu
    # via huggingface-hub
    # via ipykernel
    # via jupytext
    # via langchain-core
    # via marshmallow
    # via mkdocs
    # via nbconvert
    # via transformers
paginate==0.5.7
    # via mkdocs-material
pandas==2.2.3
    # via langchain-cohere
pandocfilters==1.5.1
    # via nbconvert
parameterized==0.9.0
    # via cohere
parso==0.8.4
    # via jedi
pathspec==0.12.1
    # via mkdocs
pexpect==4.9.0
    # via ipython
platformdirs==4.2.2
    # via jupyter-core
    # via mkdocs-get-deps
    # via mkdocstrings
prompt-toolkit==3.0.47
    # via ipython
propcache==0.2.0
    # via yarl
protobuf==5.28.2
    # via transformers
psutil==6.1.0
    # via ipykernel
    # via megaparse-sdk
ptyprocess==0.7.0
    # via pexpect
pure-eval==0.2.3
    # via stack-data
pycryptodome==3.21.0
    # via megaparse-sdk
pydantic==2.9.2
    # via anthropic
    # via cohere
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-core
    # via langchain-mistralai
    # via langsmith
    # via openai
    # via pydantic-settings
    # via quivr-core
pydantic-core==2.23.4
    # via cohere
    # via pydantic
pydantic-settings==2.6.1
    # via langchain-community
pygments==2.18.0
    # via ipython
    # via mkdocs-jupyter
    # via mkdocs-material
    # via nbconvert
    # via rich
pymdown-extensions==10.9
    # via mkdocs-material
    # via mkdocstrings
python-dateutil==2.9.0.post0
    # via ghp-import
    # via jupyter-client
    # via pandas
python-dotenv==1.0.1
    # via megaparse-sdk
    # via pydantic-settings
pytz==2024.2
    # via pandas
pyyaml==6.0.2
    # via huggingface-hub
    # via jupytext
    # via langchain
    # via langchain-community
    # via langchain-core
    # via mkdocs
    # via mkdocs-get-deps
    # via pymdown-extensions
    # via pyyaml-env-tag
    # via transformers
pyyaml-env-tag==0.1
    # via mkdocs
pyzmq==26.2.0
    # via ipykernel
    # via jupyter-client
quivr-core @ file:///${PROJECT_ROOT}/../core
rapidfuzz==3.10.1
    # via quivr-core
referencing==0.35.1
    # via jsonschema
    # via jsonschema-specifications
regex==2024.7.24
    # via mkdocs-material
    # via tiktoken
    # via transformers
requests==2.32.3
    # via cohere
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langsmith
    # via mkdocs-material
    # via requests-toolbelt
    # via tiktoken
    # via transformers
requests-toolbelt==1.0.0
    # via langsmith
rich==13.9.2
    # via quivr-core
rpds-py==0.20.0
    # via jsonschema
    # via referencing
safetensors==0.4.5
    # via transformers
sentencepiece==0.2.0
    # via transformers
six==1.16.0
    # via asttokens
    # via bleach
    # via python-dateutil
sniffio==1.3.1
    # via anthropic
    # via anyio
    # via httpx
    # via openai
soupsieve==2.6
    # via beautifulsoup4
sqlalchemy==2.0.36
    # via langchain
    # via langchain-community
stack-data==0.6.3
    # via ipython
tabulate==0.9.0
    # via langchain-cohere
tenacity==8.5.0
    # via langchain
    # via langchain-community
    # via langchain-core
tiktoken==0.8.0
    # via langchain-openai
    # via quivr-core
tinycss2==1.3.0
    # via nbconvert
tokenizers==0.20.1
    # via cohere
    # via langchain-mistralai
    # via transformers
tornado==6.4.1
    # via ipykernel
    # via jupyter-client
tqdm==4.66.5
    # via huggingface-hub
    # via openai
    # via transformers
traitlets==5.14.3
    # via comm
    # via ipykernel
    # via ipython
    # via jupyter-client
    # via jupyter-core
    # via matplotlib-inline
    # via nbclient
    # via nbconvert
    # via nbformat
transformers==4.45.2
    # via quivr-core
types-pyyaml==6.0.12.20240917
    # via quivr-core
types-requests==2.32.0.20241016
    # via cohere
typing-extensions==4.12.2
    # via anthropic
    # via cohere
    # via huggingface-hub
    # via ipython
    # via langchain-core
    # via openai
    # via pydantic
    # via pydantic-core
    # via sqlalchemy
    # via typing-inspect
typing-inspect==0.9.0
    # via dataclasses-json
tzdata==2024.2
    # via pandas
urllib3==2.2.2
    # via requests
    # via types-requests
watchdog==5.0.0
    # via mkdocs
wcwidth==0.2.13
    # via prompt-toolkit
webencodings==0.5.1
    # via bleach
    # via tinycss2
yarl==1.15.4
    # via aiohttp
```

## File: `docs/docs/index.md`
```markdown
# Welcome to Quivr Documentation

Quivr, helps you build your second brain, utilizes the power of GenerativeAI to be your personal assistant !

## Key Features 🎯

- **Opiniated RAG**: We created a RAG that is opinionated, fast and efficient so you can focus on your product
- **LLMs**: Quivr works with any LLM, you can use it with OpenAI, Anthropic, Mistral, Gemma, etc.
- **Any File**: Quivr works with any file, you can use it with PDF, TXT, Markdown, etc and even add your own parsers.
- **Customize your RAG**: Quivr allows you to customize your RAG, add internet search, add tools, etc.
- **Integrations with Megaparse**: Quivr works with [Megaparse](https://github.com/quivrhq/megaparse), so you can ingest your files with Megaparse and use the RAG with Quivr.

>We take care of the RAG so you can focus on your product. Simply install quivr-core and add it to your project. You can now ingest your files and ask questions.*

**We will be improving the RAG and adding more features everything, stay tuned!**


This is the core of Quivr, the brain of Quivr.com.

<!-- ## Demo Highlight 🎥

https://github.com/quivrhq/quivr/assets/19614572/a6463b73-76c7-4bc0-978d-70562dca71f5 -->

## Getting Started 🚀

You can find everything on the [documentation](https://core.quivr.app/).

### Prerequisites 📋

Ensure you have the following installed:

- Python 3.10 or newer

### 30 seconds Installation 💽


- **Step 1**: Install the package

  

  ```bash
  pip install quivr-core # Check that the installation worked
  ```


- **Step 2**: Create a RAG with 5 lines of code

  ```python
    import tempfile

    from quivr_core import Brain

    if __name__ == "__main__":
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as temp_file:
            temp_file.write("Gold is a liquid of blue-like colour.")
            temp_file.flush()

            brain = Brain.from_files(
                name="test_brain",
                file_paths=[temp_file.name],
            )

            answer = brain.ask(
                "what is gold? asnwer in french"
            )
            print("answer:", answer)
  ```

```

## File: `docs/docs/quickstart.md`
```markdown
# Quick start

If you need to quickly start talking to your list of files, here are the steps.

1. Add your API Keys to your environment variables
```python
import os
os.environ["OPENAI_API_KEY"] = "myopenai_apikey"

```
Check our `.env.example` file to see the possible environment variables you can configure. Quivr supports APIs from Anthropic, OpenAI, and Mistral. It also supports local models using Ollama.

2. Create a Brain with Quivr default configuration
```python
from quivr_core import Brain

brain = Brain.from_files(name = "my smart brain",
                        file_paths = ["/my_smart_doc.pdf", "/my_intelligent_doc.txt"],
                        )

```

3. Launch a Chat
```python
brain.print_info()

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()
console.print(Panel.fit("Ask your brain !", style="bold magenta"))

while True:
    # Get user input
    question = Prompt.ask("[bold cyan]Question[/bold cyan]")

    # Check if user wants to exit
    if question.lower() == "exit":
        console.print(Panel("Goodbye!", style="bold yellow"))
        break

    answer = brain.ask(question)
    # Print the answer with typing effect
    console.print(f"[bold green]Quivr Assistant[/bold green]: {answer.answer}")

    console.print("-" * console.width)

brain.print_info()
```

And now you are all set up to talk with your brain !

## Custom Brain
If you want to change the language or embeddings model, you can modify the parameters of the brain.

Let's say you want to use a LLM from Mistral and a specific embedding model :
```python
from quivr_core import Brain
from langchain_core.embeddings import Embeddings

brain = Brain.from_files(name = "my smart brain",
                        file_paths = ["/my_smart_doc.pdf", "/my_intelligent_doc.txt"],
                        llm=LLMEndpoint(
                            llm_config=LLMEndpointConfig(model="mistral-small-latest", llm_base_url="https://api.mistral.ai/v1/chat/completions"),
                        ),
                        embedder=Embeddings(size=64),
                        )
```

Note : [Embeddings](https://python.langchain.com/docs/integrations/text_embedding/) is a langchain class that lets you chose from a large variety of embedding models. Please check out the following docs to know the panel of models you can try.

## Launch with Chainlit

If you want to quickly launch an interface with streamlit, you can simply do at the root of the project :
```bash
cd examples/chatbot /
rye sync /
rye run chainlit run chainlit.py
```
For more detail, go in [examples/chatbot/chainlit.md](https://github.com/QuivrHQ/quivr/tree/main/examples/chatbot)

Note : Modify the Brain configs directly in examples/chatbot/main.py;
```

## File: `docs/docs/brain/brain.md`
```markdown
::: quivr_core.brain.brain
    options:
      heading_level: 2
```

## File: `docs/docs/brain/chat.md`
```markdown
## ChatHistory

The `ChatHistory` class is where all the conversation between the user and the LLM gets stored. A `ChatHistory` object will transparently be instanciated in the `Brain` every time you create one.

At each interaction with `Brain.ask_streaming` both your message and the LLM's response are added to this chat history. It's super handy because this history is used in the Retrieval-Augmented Generation (RAG) process to give the LLM more context, working as form of memory between the user and the system and helping it generate better responses by looking at what’s already been said.

You can also get some cool info about the brain by printing its details with the `print_info()` method, which shows things like how many chats are stored, the current chat history, and more. This makes it easy to keep track of what’s going on in your conversations and manage the context being sent to the LLM!

::: quivr_core.rag.entities.chat
options:
heading_level: 2
```

## File: `docs/docs/brain/index.md`
```markdown
# Brain

The brain is the essential component of Quivr that stores and processes the knowledge you want to retrieve informations from. Simply create a brain with the files you want to process and use the latest Quivr RAG workflow to retrieve informations from the knowledge.

Quick Start 🪄:

```python
from quivr_core import Brain
from quivr_core.quivr_rag_langgraph import QuivrQARAGLangGraph


brain = Brain.from_files(name="My Brain", file_paths=["file1.pdf", "file2.pdf"])
answer = brain.ask("What is Quivr ?")
print("Answer Quivr :", answer.answer)

```

Pimp your Brain 🔨 :

```python
from quivr_core import Brain
from quivr_core.llm.llm_endpoint import LLMEndpoint
from quivr_core.embedder.embedder import DeterministicFakeEmbedding
from quivr_core.llm.llm_endpoint import LLMEndpointConfig
from quivr_core.llm.llm_endpoint import FakeListChatModel

brain = Brain.from_files(
        name="test_brain",
        file_paths=["my/information/source/file.pdf"],
        llm=LLMEndpoint(
            llm=FakeListChatModel(responses=["good"]),
            llm_config=LLMEndpointConfig(model="fake_model", llm_base_url="local"),
        ),
        embedder=DeterministicFakeEmbedding(size=20),
    )

answer = brain.ask(
            "What is Quivr ?"
        )
print("Answer Quivr :", answer.answer)

```
```

## File: `docs/docs/config/base_config.md`
```markdown
# Configuration Base Class

::: quivr_core.base_config
    options:
      heading_level: 2
```

## File: `docs/docs/config/config.md`
```markdown
# Configuration

## Retrieval Configuration
::: quivr_core.rag.entities.config.RetrievalConfig

## Workflow Configuration
::: quivr_core.rag.entities.config.WorkflowConfig

## LLM Configuration
::: quivr_core.rag.entities.config.LLMEndpointConfig

## Reranker Configuration
::: quivr_core.rag.entities.config.RerankerConfig

## Supported LLM Model Suppliers
::: quivr_core.rag.entities.config.DefaultModelSuppliers

## Supported Rerankers
::: quivr_core.rag.entities.config.DefaultRerankers
```

## File: `docs/docs/config/index.md`
```markdown
# Configuration

The configuration classes are based on [Pydantic](https://docs.pydantic.dev/latest/) and allow the configuration of the ingestion and retrieval workflows via YAML files.

Below is an example of a YAML configuration file for a basic RAG retrieval workflow.
```yaml
workflow_config:
  name: "standard RAG"
  nodes:
    - name: "START"
      edges: ["filter_history"]

    - name: "filter_history"
      edges: ["rewrite"]

    - name: "rewrite"
      edges: ["retrieve"]

    - name: "retrieve"
      edges: ["generate_rag"]

    - name: "generate_rag" # the name of the last node, from which we want to stream the answer to the user, should always start with "generate"
      edges: ["END"]
# Maximum number of previous conversation iterations
# to include in the context of the answer
max_history: 10

prompt: "my prompt"

max_files: 20
reranker_config:
  # The reranker supplier to use
  supplier: "cohere"

  # The model to use for the reranker for the given supplier
  model: "rerank-multilingual-v3.0"

  # Number of chunks returned by the reranker
  top_n: 5
llm_config:

  max_context_tokens: 2000

  temperature: 0.7
  streaming: true
```
```

## File: `docs/docs/css/style.css`
```css
.md-container .jp-Cell-outputWrapper .jp-OutputPrompt.jp-OutputArea-prompt,
.md-container .jp-Cell-inputWrapper .jp-InputPrompt.jp-InputArea-prompt {
    display: none !important;
}

/* CSS styles for side-by-side layout */
.container {
    display: flex-col;
    justify-content: space-between;
    margin-bottom: 20px;
    /* Adjust spacing between sections */
    position: sticky;
    top: 2.4rem;
    z-index: 1000;
    /* Ensure it's above other content */
    background-color: white;
    /* Match your page background */
    padding: 0.2rem;
}

.example-heading {
    margin: 0.2rem !important;
}

.usage-examples {
    width: 100%;
    /* Adjust the width as needed */
    border: 1px solid var(--md-default-fg-color--light);
    border-radius: 2px;
    padding: 0.2rem;
}

/* Additional styling for the toggle */
.toggle-example {
    cursor: pointer;
    color: white;
    text-decoration: underline;
    background-color: var(--md-primary-fg-color);
    padding: 0.2rem;
    border-radius: 2px;
}

.hidden {
    display: none;
}

/* mendable search styling */
#my-component-root>div {
    bottom: 100px;
}
```

## File: `docs/docs/examples/chatbot.md`
```markdown
# Chatbot with Chainlit

This example demonstrates a simple chatbot using **Quivr** and **Chainlit**, where users can upload a `.txt` file and ask questions based on its content.

---

## Prerequisites

- **Python**: Version 3.8 or higher.
- **OpenAI API Key**: Ensure you have a valid OpenAI API key.

---

## Installation

1. Clone the repository and navigate to the appropriate directory:
    ```bash
    git clone https://github.com/QuivrHQ/quivr
    cd examples/chatbot
    ```

2. Set the OpenAI API key as an environment variable:
    ```bash
    export OPENAI_API_KEY='<your-key-here>'
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.lock
    ```

---

## Running the Chatbot

1. Start the Chainlit server:
    ```bash
    chainlit run main.py
    ```

2. Open your web browser and navigate to the URL displayed in the terminal (default: `http://localhost:8000`).

---

## Using the Chatbot

### File Upload

1. On the chatbot interface, upload a `.txt` file when prompted.
2. Ensure the file size is under **20MB**.
3. After uploading, the file is processed, and you will be notified when the chatbot is ready.

### Asking Questions

1. Type your questions into the chat input and press Enter.
2. The chatbot will respond based on the content of the uploaded file.
3. Relevant file sources for the answers are displayed in the chat.

---

## How It Works

1. **File Upload**:
    - Users upload a `.txt` file, which is temporarily saved.
    - The chatbot processes the file using Quivr to create a "brain."

2. **Session Handling**:
    - Chainlit manages the session to retain the file path and brain context.

3. **Question Answering**:
    - The chatbot uses the `ask_streaming` method from Quivr to process user queries.
    - Responses are streamed incrementally for faster feedback.
    - Relevant file excerpts (sources) are extracted and displayed.

4. **Retrieval Configuration**:
    - A YAML file (`basic_rag_workflow.yaml`) defines retrieval parameters for Quivr.

---

## Workflow

### Chat Start

1. Waits for the user to upload a `.txt` file.
2. Processes the file and creates a "brain."
3. Notifies the user when the system is ready for questions.

### On User Message

1. Retrieves the "brain" from the session.
2. Processes the user's question with Quivr.
3. Streams the response and displays it in the chat.
4. Extracts and shows relevant sources from the file.

---

## Features

1. **File Processing**: Creates a context-aware "brain" from the uploaded file.
2. **Streaming Responses**: Delivers answers incrementally for better user experience.
3. **Source Highlighting**: Displays file excerpts relevant to the answers.

---

Enjoy interacting with your text files in a seamless Q&A format!
```

## File: `docs/docs/examples/chatbot_voice.md`
```markdown
# Voice Chatbot with Chainlit

This example demonstrates how to create a voice-enabled chatbot using **Quivr** and **Chainlit**. The chatbot lets users upload a text file, ask questions about its content, and interact using speech.

---

## Prerequisites

- **Python**: Version 3.8 or higher.
- **OpenAI API Key**: Ensure you have a valid OpenAI API key.

---

## Installation

1. Clone the repository and navigate to the appropriate directory:
    ```bash
    git clone https://github.com/QuivrHQ/quivr
    cd examples/chatbot_voice
    ```

2. Set the OpenAI API key as an environment variable:
    ```bash
    export OPENAI_API_KEY='<your-key-here>'
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.lock
    ```

---

## Running the Chatbot

1. Start the Chainlit server:
    ```bash
    chainlit run main.py
    ```

2. Open your web browser and navigate to the URL displayed in the terminal (default: `http://localhost:8000`).

---

## Using the Chatbot

### File Upload

1. Once the interface loads, the chatbot will prompt you to upload a `.txt` file.
2. Click on the upload area or drag-and-drop a text file. Ensure the file size is under **20MB**.
3. After processing, the chatbot will notify you that it’s ready for interaction.

### Asking Questions

1. Type your questions in the input box or upload an audio file containing your question.
2. If using text input, the chatbot will respond with an answer derived from the uploaded file's content.
3. If using audio input:
   - The chatbot converts speech to text using OpenAI Whisper.
   - Processes the text query and provides a response.
   - Converts the response to audio, enabling hands-free interaction.

---

## Features

1. **Text File Processing**: Creates a "brain" for the uploaded file using Quivr for question answering.
2. **Speech-to-Text (STT)**: Transcribes user-uploaded audio queries using OpenAI Whisper.
3. **Text-to-Speech (TTS)**: Converts chatbot responses into audio for a seamless voice chat experience.
4. **Source Display**: Shows relevant file sources for each response.
5. **Real-Time Updates**: Uses streaming for live feedback during processing.

---

## How It Works

1. **File Upload**: The user uploads a `.txt` file, which is temporarily saved and processed into a "brain" using Quivr.
2. **Session Handling**: Chainlit manages user sessions to retain the uploaded file and brain context.
3. **Voice Interaction**:
    - Audio queries are processed via the OpenAI Whisper API.
    - Responses are generated and optionally converted into audio for playback.
4. **Streaming**: The chatbot streams its answers incrementally, improving response speed.

---

## Workflow

### Chat Start

1. Waits for a text file upload.
2. Processes the file into a "brain."
3. Notifies the user when ready for interaction.

### On User Message

1. Extracts the "brain" and queries it using the message content.
2. Streams the response back to the user.
3. Displays file sources related to the response.

### Audio Interaction

1. Captures and processes audio chunks during user input.
2. Converts captured audio into text using Whisper.
3. Queries the brain and provides both text and audio responses.

---

Enjoy interacting with your documents in both text and voice modes!
```

## File: `docs/docs/examples/chatbot_voice_flask.md`
```markdown
# Voice Chatbot with Flask

This example demonstrates a simple chatbot using **Flask** and **Quivr**, where users can upload a `.txt` file and ask questions based on its content. It supports speech-to-text and text-to-speech capabilities for a seamless interactive experience.

<video style="width:100%" muted="" controls="" alt="type:video">
   <source src="../assets/chatbot_voice_flask.mp4" type="video/mp4">
</video>
---

## Prerequisites

- **Python**: Version 3.8 or higher.
- **OpenAI API Key**: Ensure you have a valid OpenAI API key.

---

## Installation

1. Clone the repository and navigate to the project directory:
    ```bash
    git clone https://github.com/QuivrHQ/quivr
    cd examples/quivr-whisper
    ```

2. Set the OpenAI API key as an environment variable:
    ```bash
    export OPENAI_API_KEY='<your-key-here>'
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.lock
    ```

---

## Running the Application

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to the URL displayed in the terminal (default: `http://localhost:5000`).

---

## Using the Chatbot

### File Upload

1. On the interface, upload a `.txt` file.
2. Ensure the file format is supported and its size is manageable.
3. The file will be processed, and a "brain" instance will be created.

### Asking Questions

1. Use the microphone to record your question (audio upload).
2. The chatbot will process your question and respond with an audio answer.

---

## How It Works

### File Upload
- Users upload a `.txt` file.
- The file is saved to the `uploads` directory and used to create a "brain" using **Quivr**.

### Session Management
- Each session is associated with a unique ID, allowing the system to cache the user's "brain."

### Speech-to-Text
- User audio files are processed with OpenAI's **Whisper** model to generate transcripts.

### Question Answering
- The "brain" processes the transcribed text, retrieves relevant answers, and generates a response.

### Text-to-Speech
- The answer is converted to audio using OpenAI's text-to-speech model and returned to the user.

---

## Workflow

1. **Upload File**:
    - The user uploads a `.txt` file.
    - A "brain" is created and cached for the session.

2. **Ask Questions**:
    - The user uploads an audio file containing a question.
    - The question is transcribed, processed, and answered using the "brain."

3. **Answer Delivery**:
    - The answer is converted to audio and returned to the user as a Base64-encoded string.

---

## Features

1. **File Upload and Processing**:
    - Creates a context-aware "brain" from the uploaded text file.

2. **Audio-based Interaction**:
    - Supports speech-to-text for input and text-to-speech for responses.

3. **Session Management**:
    - Retains user context throughout the interaction.

4. **Integration with OpenAI**:
    - Uses OpenAI models for transcription, answer generation, and audio synthesis.

---

Enjoy interacting with your text files through an intuitive voice-based interface!
```

## File: `docs/docs/examples/custom_storage.md`
```markdown
# Transparent Storage

**todo**
```

## File: `docs/docs/examples/index.md`
```markdown
# Examples
```

## File: `docs/docs/parsers/index.md`
```markdown
# Parsers

Quivr provides a suite of parsers to extract structured data from various sources.
```

## File: `docs/docs/parsers/megaparse.md`
```markdown
## Megaparse

::: quivr_core.processor.implementations.megaparse_processor
    options:
      heading_level: 2
```

## File: `docs/docs/parsers/simple.md`
```markdown
## Simple Txt

::: quivr_core.processor.implementations.simple_txt_processor
    options:
      heading_level: 2
```

## File: `docs/docs/storage/base.md`
```markdown
# StorageBase

::: quivr_core.storage.storage_base
options:
heading_level: 2
```

## File: `docs/docs/storage/index.md`
```markdown
# 🗄️ Storage

## Your Brain’s File Management System

The `Storage` class is the backbone of how a brain interacts with files in `quivr-core`. Every brain holds a reference to an underlying storage system to manage its files. All storages should implement the `StorageBase` base classe that provides the structure and methods to make that happen seamlessly. Let's walk through how it works:

- **Brain-Storage Connection:** Your brain holds a reference to a storage system. This class is the main way your brain can interact with and manage the files it uses. Adding files to a brain will upload them to the storage. This means that files in the storage are stored **before** processing!
- **File Management:** the storage holds a set of `QuivrFile` objects, which are the building blocks of your brain’s file system. The storage can store them remotely or locally or hold simple

### What can you do with this storage system?

1. Upload Files: You can add new files to your storage whenever you need. The system also lets you decide whether to overwrite existing files or not.
2. Get Files: Need to see what's in your storage? No problem. You can easily retrieve a list of all the files that are stored.
3. Delete Files: Clean-up is simple. You can remove any file from your storage by referencing its unique file ID (more on that in `QuivrFile`).

StorageBase is the foundation of how your brain organizes, uploads, retrieves, and deletes its files. It ensures that your brain can always stay up-to-date with the files it needs, making file management smooth and intuitive. You can build your own storage system by subclassing the `StorageBase` class and passing it to the brain. See [custom_storage](../examples/custom_storage.md) for more details.

### Storage Implementations in `quivr_core`

`quivr_core` currently offers two storage implementations: `LocalStorage` and `TransparentStorage`:

- **LocalStorage**:  
  This storage type is perfect when you want to keep files on your local machine. `LocalStorage` saves your files to a specific directory, either a default path (`~/.cache/quivr/files`) or a user-defined location. It can store files by copying them or by creating symbolic links to the original files, based on your preference. This storage type also keeps track of file hashes to prevent accidental overwrites during uploads.

- **TransparentStorage**:  
  The `TransparentStorage` implementation offers a lightweight and flexible approach, mainly managing files in memory without a need for local file paths. This storage system is useful when you don't need persistent storage but rather an easy way to store and retrieve files temporarily during the brain's operation.

Each of these storage systems has its own strengths, catering to different use cases. As `quivr_core` evolves, we will implementat more ande more storage systems allowing for even more advanced and customized ways to manage your files like `S3Storage`, `NFSStorage` ...
```

## File: `docs/docs/storage/local_storage.md`
```markdown
# LocalStorage

::: quivr_core.storage.local_storage
options:
heading_level: 2
```

## File: `docs/docs/vectorstores/faiss.md`
```markdown
# Faiss
```

## File: `docs/docs/vectorstores/index.md`
```markdown
# Vector Stores

```

## File: `docs/docs/vectorstores/pgvector.md`
```markdown
# PGVector
```

## File: `docs/docs/workflows/index.md`
```markdown
# Workflows

In this section, you will find examples of workflows that you can use to create your own agentic RAG systems.
```

## File: `docs/docs/workflows/examples/basic_ingestion.md`
```markdown
# Basic ingestion

![](basic_ingestion.excalidraw.png)


Creating a basic ingestion workflow like the one above is simple, here are the steps:

1. Add your API Keys to your environment variables
```python
import os
os.environ["OPENAI_API_KEY"] = "myopenai_apikey"

```
Check our `.env.example` file to see the possible environment variables you can configure. Quivr supports APIs from Anthropic, OpenAI, and Mistral. It also supports local models using Ollama.

2. Create the YAML file ``basic_ingestion_workflow.yaml`` and copy the following content in it
```yaml
parser_config:
  megaparse_config:
    strategy: "auto" # for unstructured, it can be "auto", "fast", "hi_res", "ocr_only", see https://docs.unstructured.io/open-source/concepts/partitioning-strategies#partitioning-strategies
    pdf_parser: "unstructured"
  splitter_config:
    chunk_size: 400 # in tokens
    chunk_overlap: 100 # in tokens
```

3. Create a Brain using the above configuration and the list of files you want to ingest
```python
from quivr_core import Brain
from quivr_core.config import IngestionConfig

config_file_name = "./basic_ingestion_workflow.yaml"

ingestion_config = IngestionConfig.from_yaml(config_file_name)

processor_kwargs = {
    "megaparse_config": ingestion_config.parser_config.megaparse_config,
    "splitter_config": ingestion_config.parser_config.splitter_config,
}

brain = Brain.from_files(name = "my smart brain",
                        file_paths = ["./my_first_doc.pdf", "./my_second_doc.txt"],
                        processor_kwargs=processor_kwargs,
                        )

```

4. Launch a Chat
```python
brain.print_info()

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()
console.print(Panel.fit("Ask your brain !", style="bold magenta"))

while True:
    # Get user input
    question = Prompt.ask("[bold cyan]Question[/bold cyan]")

    # Check if user wants to exit
    if question.lower() == "exit":
        console.print(Panel("Goodbye!", style="bold yellow"))
        break

    answer = brain.ask(question)
    # Print the answer with typing effect
    console.print(f"[bold green]Quivr Assistant[/bold green]: {answer.answer}")

    console.print("-" * console.width)

brain.print_info()
```

5. You are now all set up to talk with your brain and test different chunking strategies by simply changing the configuration file!
```

## File: `docs/docs/workflows/examples/basic_rag.md`
```markdown
# Basic RAG

![](basic_rag.excalidraw.png)


Creating a basic RAG workflow like the one above is simple, here are the steps:


1. Add your API Keys to your environment variables
```python
import os
os.environ["OPENAI_API_KEY"] = "myopenai_apikey"

```
Check our `.env.example` file to see the possible environment variables you can configure. Quivr supports APIs from Anthropic, OpenAI, and Mistral. It also supports local models using Ollama.

2. Create the YAML file ``basic_rag_workflow.yaml`` and copy the following content in it
```yaml
workflow_config:
  name: "standard RAG"
  nodes:
    - name: "START"
      edges: ["filter_history"]

    - name: "filter_history"
      edges: ["rewrite"]

    - name: "rewrite"
      edges: ["retrieve"]

    - name: "retrieve"
      edges: ["generate_rag"]

    - name: "generate_rag" # the name of the last node, from which we want to stream the answer to the user
      edges: ["END"]

# Maximum number of previous conversation iterations
# to include in the context of the answer
max_history: 10

# Reranker configuration
reranker_config:
  # The reranker supplier to use
  supplier: "cohere"

  # The model to use for the reranker for the given supplier
  model: "rerank-multilingual-v3.0"

  # Number of chunks returned by the reranker
  top_n: 5

# Configuration for the LLM
llm_config:

  # maximum number of tokens passed to the LLM to generate the answer
  max_input_tokens: 4000

  # temperature for the LLM
  temperature: 0.7
```

3. Create a Brain with the default configuration
```python
from quivr_core import Brain

brain = Brain.from_files(name = "my smart brain",
                        file_paths = ["./my_first_doc.pdf", "./my_second_doc.txt"],
                        )

```

4. Launch a Chat
```python
brain.print_info()

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from quivr_core.config import RetrievalConfig

config_file_name = "./basic_rag_workflow.yaml"

retrieval_config = RetrievalConfig.from_yaml(config_file_name)

console = Console()
console.print(Panel.fit("Ask your brain !", style="bold magenta"))

while True:
    # Get user input
    question = Prompt.ask("[bold cyan]Question[/bold cyan]")

    # Check if user wants to exit
    if question.lower() == "exit":
        console.print(Panel("Goodbye!", style="bold yellow"))
        break

    answer = brain.ask(question, retrieval_config=retrieval_config)
    # Print the answer with typing effect
    console.print(f"[bold green]Quivr Assistant[/bold green]: {answer.answer}")

    console.print("-" * console.width)

brain.print_info()
```

5. You are now all set up to talk with your brain and test different retrieval strategies by simply changing the configuration file!
```

## File: `docs/docs/workflows/examples/rag_with_web_search.md`
```markdown
# RAG with web search


![](rag_with_web_search.excalidraw.png)

Follow the instructions below to create the agentic RAG workflow shown above, which includes some advanced capabilities such as:

* **user intention detection** - the agent can detect if the user wants to activate the web search tool to look for information not present in the documents;
* **dynamic chunk retrieval** - the number of retrieved chunks is not fixed, but determined dynamically using the reranker's relevance scores and the user-provided ``relevance_score_threshold``;
* **web search** - the agent can search the web for more information if needed.


---

1. Add your API Keys to your environment variables
```python
import os
os.environ["OPENAI_API_KEY"] = "my_openai_api_key"
os.environ["TAVILY_API_KEY"] = "my_tavily_api_key"

```
Check our `.env.example` file to see the possible environment variables you can configure. Quivr supports APIs from Anthropic, OpenAI, and Mistral. It also supports local models using Ollama.

2. Create the YAML file ``rag_with_web_search_workflow.yaml`` and copy the following content in it
```yaml
workflow_config:
  name: "RAG with web search"

  # List of tools that the agent can activate if the user instructions require it
  available_tools:
    - "web search"

  nodes:
    - name: "START"
      conditional_edge:
        routing_function: "routing_split"
        conditions: ["edit_system_prompt", "filter_history"]

    - name: "edit_system_prompt"
      edges: ["filter_history"]

    - name: "filter_history"
      edges: ["dynamic_retrieve"]

    - name: "dynamic_retrieve"
      conditional_edge:
        routing_function: "tool_routing"
        conditions: ["run_tool", "generate_rag"]

    - name: "run_tool"
      edges: ["generate_rag"]

    - name: "generate_rag" # the name of the last node, from which we want to stream the answer to the user
      edges: ["END"]
      tools:
        - name: "cited_answer"

# Maximum number of previous conversation iterations
# to include in the context of the answer
max_history: 10

# Number of chunks returned by the retriever
k: 40

# Reranker configuration
reranker_config:
  # The reranker supplier to use
  supplier: "cohere"

  # The model to use for the reranker for the given supplier
  model: "rerank-multilingual-v3.0"

  # Number of chunks returned by the reranker
  top_n: 5

  # Among the chunks returned by the reranker, only those with relevance
  # scores equal or above the relevance_score_threshold will be returned
  # to the LLM to generate the answer (allowed values are between 0 and 1,
  # a value of 0.1 works well with the cohere and jina rerankers)
  relevance_score_threshold: 0.01

# LLM configuration
llm_config:

  # maximum number of tokens passed to the LLM to generate the answer
  max_input_tokens: 8000

  # temperature for the LLM
  temperature: 0.7
```

3. Create a Brain with the default configuration
```python
from quivr_core import Brain

brain = Brain.from_files(name = "my smart brain",
                        file_paths = ["./my_first_doc.pdf", "./my_second_doc.txt"],
                        )

```

4. Launch a Chat
```python
brain.print_info()

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from quivr_core.config import RetrievalConfig

config_file_name = "./rag_with_web_search_workflow.yaml"

retrieval_config = RetrievalConfig.from_yaml(config_file_name)

console = Console()
console.print(Panel.fit("Ask your brain !", style="bold magenta"))

while True:
    # Get user input
    question = Prompt.ask("[bold cyan]Question[/bold cyan]")

    # Check if user wants to exit
    if question.lower() == "exit":
        console.print(Panel("Goodbye!", style="bold yellow"))
        break

    answer = brain.ask(question, retrieval_config=retrieval_config)
    # Print the answer with typing effect
    console.print(f"[bold green]Quivr Assistant[/bold green]: {answer.answer}")

    console.print("-" * console.width)

brain.print_info()
```

5. You are now all set up to talk with your brain and test different retrieval strategies by simply changing the configuration file!
```

## File: `docs/overrides/empty`
```
empty
```

## File: `docs/src/docs/__init__.py`
```python
def hello() -> str:
    return "Hello from docs!"
```

## File: `examples/pdf_document_from_yaml.py`
```python
import asyncio
import logging
import os
from pathlib import Path

import dotenv
from quivr_core import Brain
from quivr_core.rag.entities.config import AssistantConfig
from rich.traceback import install as rich_install

ConsoleOutputHandler = logging.StreamHandler()

logger = logging.getLogger("quivr_core")
logger.setLevel(logging.DEBUG)
logger.addHandler(ConsoleOutputHandler)


logger = logging.getLogger("megaparse")
logger.setLevel(logging.DEBUG)
logger.addHandler(ConsoleOutputHandler)


# Install rich's traceback handler to automatically format tracebacks
rich_install()


async def main():
    file_path = [
        Path("data/YamEnterprises_Monotype Fonts Plan License.US.en 04.0 (BLP).pdf")
    ]
    file_path = [
        Path(
            "data/YamEnterprises_Monotype Fonts Plan License.US.en 04.0 (BLP) reduced.pdf"
        )
    ]

    config_file_name = (
        "/Users/jchevall/Coding/quivr/backend/core/tests/rag_config_workflow.yaml"
    )

    assistant_config = AssistantConfig.from_yaml(config_file_name)
    # megaparse_config = find_nested_key(config, "megaparse_config")
    megaparse_config = assistant_config.ingestion_config.parser_config.megaparse_config
    megaparse_config.llama_parse_api_key = os.getenv("LLAMA_PARSE_API_KEY")

    processor_kwargs = {
        "megaparse_config": megaparse_config,
        "splitter_config": assistant_config.ingestion_config.parser_config.splitter_config,
    }

    brain = await Brain.afrom_files(
        name="test_brain",
        file_paths=file_path,
        processor_kwargs=processor_kwargs,
    )

    # # Check brain info
    brain.print_info()

    questions = [
        "What is the contact name for Yam Enterprises?",
        "What is the customer phone for Yam Enterprises?",
        "What is the Production Fonts (maximum) for Yam Enterprises?",
        "List the past use font software according to past use term for Yam Enterprises.",
        "How many unique Font Name are there in the Add-On Font Software Section for Yam Enterprises?",
        "What is the maximum number of Production Fonts allowed based on the license usage per term for Yam Enterprises?",
        "What is the number of production fonts licensed by Yam Enterprises? List them one by one.",
        "What is the number of Licensed Monthly Page Views for Yam Enterprises?",
        "What is the monthly licensed impressions (Digital Marketing Communications) for Yam Enterprises?",
        "What is the number of Licensed Applications for Yam Enterprises?",
        "For Yam Enterprises what is the number of applications aggregate Registered users?",
        "What is the number of licensed servers for Yam Enterprises?",
        "When is swap of Production Fonts available in Yam Enterprises?",
        "Who is the primary licensed monotype fonts user for Yam Enterprises?",
        "What is the number of Licensed Commercial Electronic Documents for Yam Enterprises?",
        "How many licensed monotype fonts users can Yam Enterprises have?",
        "How many licensed desktop users can Yam Enterprises have?",
        "Which contract type does Yam Enterprises follow?",
        "What monotype fonts support does Yam Enterprises have?",
        "Which monotype font services onboarding does Yam Enterprises have?",
        "Which Font/User Management does Yam Enterprises have?",
        "What Add-on inventory set did Yam Enterprises pick?",
        "Does Yam Enterprises have Single sign on?",
        "Is there Brand and Licence protection for Yam Enterprises?",
        "Who is the Third Party Payor's contact in Yam Enterprises?",
        "Does Yam Enterprises contract have Company Desktop License?",
        "What is the Number of Swaps Allowed for Yam Enterprises?",
        "When is swap of Production Fonts available in Yam Enterprises?",
    ]

    answers = [
        "Haruko Yamamoto",
        "81 90-1234-5603",
        "300 Production Fonts",
        "Helvetica Regular",
        "7",
        "300 Production Fonts",
        "Yam Enterprises has licensed a total of 105 Production Fonts.",
        "35,000,000",
        "2,500,000",
        "60",
        "40",
        "2",
        "Once per quarter",
        "Haruko Yamamoto",
        "0",
        "100",
        "60",
        "License",
        "Premier",
        "Premier",
        "Premier",
        "Plus",
        "Yes",
        "Yes",
        """
        Name: Yami Enterprises

        Contact: Mei Mei

        Address: 20-22 Tsuki-Tsuki-dori, Tokyo, Japan

        Phone: +81 71-9336-54023

        E-mail: mei.mei@example.com
        """,
        "Yes",
        "One (1) swap per calendar quarter",
        "The swap of Production Fonts will be available one (1) time per calendar quarter by removing Font Software as a Production Font and choosing other Font Software on the Monotype Fonts Platform.",
    ]

    retrieval_config = assistant_config.retrieval_config
    for i, (question, truth) in enumerate(zip(questions, answers, strict=False)):
        chunk = brain.ask(question=question, retrieval_config=retrieval_config)
        print(
            "\n Question: ", question, "\n Answer: ", chunk.answer, "\n Truth: ", truth
        )
        if i == 5:
            break


if __name__ == "__main__":
    dotenv.load_dotenv()

    # Run the main function in the existing event loop
    asyncio.run(main())
```

## File: `examples/pdf_parsing_tika.py`
```python
from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_core.language_models import FakeListChatModel
from quivr_core import Brain
from quivr_core.rag.entities.config import LLMEndpointConfig
from quivr_core.llm.llm_endpoint import LLMEndpoint
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

if __name__ == "__main__":
    brain = Brain.from_files(
        name="test_brain",
        file_paths=["tests/processor/data/dummy.pdf"],
        llm=LLMEndpoint(
            llm=FakeListChatModel(responses=["good"]),
            llm_config=LLMEndpointConfig(model="fake_model", llm_base_url="local"),
        ),
        embedder=DeterministicFakeEmbedding(size=20),
    )
    # Check brain info
    brain.print_info()

    console = Console()
    console.print(Panel.fit("Ask your brain !", style="bold magenta"))

    while True:
        # Get user input
        question = Prompt.ask("[bold cyan]Question[/bold cyan]")

        # Check if user wants to exit
        if question.lower() == "exit":
            console.print(Panel("Goodbye!", style="bold yellow"))
            break

        answer = brain.ask(question)
        # Print the answer with typing effect
        console.print(f"[bold green]Quivr Assistant[/bold green]: {answer.answer}")

        console.print("-" * console.width)

    brain.print_info()
```

## File: `examples/save_load_brain.py`
```python
import asyncio
import tempfile

from quivr_core import Brain


async def main():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as temp_file:
        temp_file.write("Gold is a liquid of blue-like colour.")
        temp_file.flush()

        brain = await Brain.afrom_files(name="test_brain", file_paths=[temp_file.name])

        save_path = await brain.save("/home/amine/.local/quivr")

        brain_loaded = Brain.load(save_path)
        brain_loaded.print_info()


if __name__ == "__main__":
    # Run the main function in the existing event loop
    asyncio.run(main())
```

## File: `examples/simple_question_megaparse.py`
```python
import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from quivr_core import Brain
from quivr_core.llm.llm_endpoint import LLMEndpoint
from quivr_core.rag.entities.config import LLMEndpointConfig
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

if __name__ == "__main__":
    brain = Brain.from_files(
        name="test_brain",
        file_paths=["./tests/processor/pdf/sample.pdf"],
        llm=LLMEndpoint(
            llm_config=LLMEndpointConfig(model="gpt-4o"),
            llm=ChatOpenAI(model="gpt-4o", api_key=str(os.getenv("OPENAI_API_KEY"))),
        ),
    )
    embedder = embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
    )
    # Check brain info
    brain.print_info()

    console = Console()
    console.print(Panel.fit("Ask your brain !", style="bold magenta"))

    while True:
        # Get user input
        question = Prompt.ask("[bold cyan]Question[/bold cyan]")

        # Check if user wants to exit
        if question.lower() == "exit":
            console.print(Panel("Goodbye!", style="bold yellow"))
            break

        answer = brain.ask(question)
        # Print the answer with typing effect
        console.print(f"[bold green]Quivr Assistant[/bold green]: {answer.answer}")

        console.print("-" * console.width)

    brain.print_info()
```

## File: `examples/chatbot/.gitignore`
```
# python generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# venv
.venv
.files
```

## File: `examples/chatbot/.python-version`
```
3.11.9
```

## File: `examples/chatbot/README.md`
```markdown
# Quivr Chatbot Example

This example demonstrates how to create a simple chatbot using Quivr and Chainlit. The chatbot allows users to upload a text file and then ask questions about its content.

## Prerequisites

- Python 3.8 or higher

## Installation

1. Clone the repository and navigate to the `examples/chatbot` directory.

2. Make sure you have [rye](https://rye.astral.sh/) installed.

3. Install the requirements using `rye`:

   ```sh
   rye sync
   ```
4. Activate the venv

   ```sh
   source ./venv/bin/activate
   ```

## Running the Chatbot

1. Define your API key as environment variable. e.g. `export OPENAI_API_KEY=your-key-here`

2. Start the Chainlit server:

   ```
   chainlit run main.py
   ```

3. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8000`).

## Using the Chatbot

1. When the chatbot interface loads, you will be prompted to upload a text file.

2. Click on the upload area and select a `.txt` file from your computer. The file size should not exceed 20MB.

3. After uploading, the chatbot will process the file and inform you when it's ready.

4. You can now start asking questions about the content of the uploaded file.

5. Type your questions in the chat input and press Enter. The chatbot will respond based on the information in the uploaded file.

## How It Works

The chatbot uses the Quivr library to create a "brain" from the uploaded text file. This brain is then used to answer questions about the file's content. The Chainlit library provides the user interface and handles the chat interactions.

Enjoy chatting with your documents!
```

## File: `examples/chatbot/basic_rag_workflow.yaml`
```yaml
workflow_config:
  name: "standard RAG"
  nodes:
    - name: "START"
      edges: ["filter_history"]

    - name: "filter_history"
      edges: ["rewrite"]

    - name: "rewrite"
      edges: ["retrieve"]

    - name: "retrieve"
      edges: ["generate_rag"]

    - name: "generate_rag" # the name of the last node, from which we want to stream the answer to the user
      edges: ["END"]
      tools:
        - name: "cited_answer"

# Maximum number of previous conversation iterations
# to include in the context of the answer
max_history: 10

# Reranker configuration
# reranker_config:
#   # The reranker supplier to use
#   supplier: "cohere"

#   # The model to use for the reranker for the given supplier
#   model: "rerank-multilingual-v3.0"

#   # Number of chunks returned by the reranker
#   top_n: 5

# Configuration for the LLM
llm_config:

  # maximum number of tokens passed to the LLM to generate the answer
  max_output_tokens: 4000

  # temperature for the LLM
  temperature: 0.7
```

## File: `examples/chatbot/chainlit.md`
```markdown
# Quivr Chatbot Example

This example demonstrates how to create a simple chatbot using Quivr and Chainlit. The chatbot allows users to upload a text file and then ask questions about its content.

## Prerequisites

- Python 3.8 or higher

## Installation

1. Clone the repository or navigate to the `backend/core/examples/chatbot` directory.

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Running the Chatbot

1. Start the Chainlit server:

   ```
   chainlit run main.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8000`).

## Using the Chatbot

1. When the chatbot interface loads, you will be prompted to upload a text file.

2. Click on the upload area and select a `.txt` file from your computer. The file size should not exceed 20MB.

3. After uploading, the chatbot will process the file and inform you when it's ready.

4. You can now start asking questions about the content of the uploaded file.

5. Type your questions in the chat input and press Enter. The chatbot will respond based on the information in the uploaded file.

## How It Works

The chatbot uses the Quivr library to create a "brain" from the uploaded text file. This brain is then used to answer questions about the file's content. The Chainlit library provides the user interface and handles the chat interactions.

Enjoy chatting with your documents!
```

## File: `examples/chatbot/main.py`
```python
import tempfile

import chainlit as cl
from quivr_core import Brain
from quivr_core.rag.entities.config import RetrievalConfig


@cl.on_chat_start
async def on_chat_start():
    files = None

    # Wait for the user to upload a file
    while files is None:
        files = await cl.AskFileMessage(
            content="Please upload a text .txt file to begin!",
            accept=["text/plain"],
            max_size_mb=20,
            timeout=180,
        ).send()

    file = files[0]

    msg = cl.Message(content=f"Processing `{file.name}`...")
    await msg.send()

    with open(file.path, "r", encoding="utf-8") as f:
        text = f.read()

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=file.name, delete=False
    ) as temp_file:
        temp_file.write(text)
        temp_file.flush()
        temp_file_path = temp_file.name

    brain = Brain.from_files(name="user_brain", file_paths=[temp_file_path])

    # Store the file path in the session
    cl.user_session.set("file_path", temp_file_path)

    # Let the user know that the system is ready
    msg.content = f"Processing `{file.name}` done. You can now ask questions!"
    await msg.update()

    cl.user_session.set("brain", brain)


@cl.on_message
async def main(message: cl.Message):
    brain = cl.user_session.get("brain")  # type: Brain
    path_config = "basic_rag_workflow.yaml"
    retrieval_config = RetrievalConfig.from_yaml(path_config)

    if brain is None:
        await cl.Message(content="Please upload a file first.").send()
        return

    # Prepare the message for streaming
    msg = cl.Message(content="", elements=[])
    await msg.send()

    saved_sources = set()
    saved_sources_complete = []
    elements = []

    # Use the ask_stream method for streaming responses
    async for chunk in brain.ask_streaming(message.content, retrieval_config=retrieval_config):
        await msg.stream_token(chunk.answer)
        for source in chunk.metadata.sources:
            if source.page_content not in saved_sources:
                saved_sources.add(source.page_content)
                saved_sources_complete.append(source)
                print(source)
                elements.append(cl.Text(name=source.metadata["original_file_name"], content=source.page_content, display="side"))

    
    await msg.send()
    sources = ""
    for source in saved_sources_complete:
        sources += f"- {source.metadata['original_file_name']}\n"
    msg.elements = elements
    msg.content = msg.content + f"\n\nSources:\n{sources}"
    await msg.update()
```

## File: `examples/chatbot/pyproject.toml`
```
[project]
name = "chatbot"
version = "0.1.0"
description = "Add your description here"
authors = [
    { name = "Stan Girard", email = "stan@quivr.app" }
]
dependencies = [
    "quivr-core @ file:///${PROJECT_ROOT}/../../core",
    "chainlit>=1.2.0",
]
readme = "README.md"
requires-python = ">= 3.11"

[tool.rye]
managed = true
virtual = true
dev-dependencies = []
```

## File: `examples/chatbot/requirements-dev.lock`
```
# generated by rye
# use `rye lock` or `rye sync` to update this lockfile
#
# last locked with the following flags:
#   pre: false
#   features: []
#   all-features: false
#   with-sources: false
#   generate-hashes: false
#   universal: false

aiofiles==23.2.1
    # via chainlit
    # via quivr-core
aiohappyeyeballs==2.4.3
    # via aiohttp
aiohttp==3.10.10
    # via langchain
    # via langchain-community
aiosignal==1.3.1
    # via aiohttp
alembic==1.13.3
    # via mlflow
aniso8601==9.0.1
    # via graphene
annotated-types==0.7.0
    # via pydantic
anthropic==0.40.0
    # via langchain-anthropic
anyio==4.6.2.post1
    # via anthropic
    # via asyncer
    # via httpx
    # via openai
    # via starlette
    # via watchfiles
asyncer==0.0.7
    # via chainlit
attrs==23.2.0
    # via aiohttp
    # via jsonschema
    # via referencing
    # via sagemaker
bidict==0.23.1
    # via python-socketio
blinker==1.8.2
    # via flask
boto3==1.35.42
    # via cohere
    # via sagemaker
    # via sagemaker-core
    # via sagemaker-mlflow
botocore==1.35.42
    # via boto3
    # via s3transfer
cachetools==5.5.0
    # via google-auth
    # via mlflow-skinny
certifi==2024.8.30
    # via httpcore
    # via httpx
    # via requests
chainlit==1.3.2
charset-normalizer==3.4.0
    # via requests
chevron==0.14.0
    # via literalai
click==8.1.7
    # via chainlit
    # via flask
    # via mlflow-skinny
    # via uvicorn
cloudpickle==2.2.1
    # via mlflow-skinny
    # via sagemaker
cohere==5.11.0
    # via langchain-cohere
contourpy==1.3.0
    # via matplotlib
cycler==0.12.1
    # via matplotlib
databricks-sdk==0.34.0
    # via mlflow-skinny
dataclasses-json==0.6.7
    # via chainlit
    # via langchain-community
defusedxml==0.7.1
    # via langchain-anthropic
deprecated==1.2.14
    # via opentelemetry-api
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
    # via opentelemetry-semantic-conventions
dill==0.3.9
    # via multiprocess
    # via pathos
distro==1.9.0
    # via anthropic
    # via openai
docker==7.1.0
    # via mlflow
    # via sagemaker
faiss-cpu==1.9.0
    # via quivr-core
fastapi==0.115.5
    # via chainlit
fastavro==1.9.7
    # via cohere
filelock==3.16.1
    # via huggingface-hub
    # via transformers
filetype==1.2.0
    # via chainlit
flask==3.0.3
    # via mlflow
fonttools==4.54.1
    # via matplotlib
frozenlist==1.4.1
    # via aiohttp
    # via aiosignal
fsspec==2024.9.0
    # via huggingface-hub
gitdb==4.0.11
    # via gitpython
gitpython==3.1.43
    # via mlflow-skinny
google-auth==2.35.0
    # via databricks-sdk
google-pasta==0.2.0
    # via sagemaker
googleapis-common-protos==1.65.0
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
graphene==3.3
    # via mlflow
graphql-core==3.2.5
    # via graphene
    # via graphql-relay
graphql-relay==3.2.0
    # via graphene
grpcio==1.67.0
    # via opentelemetry-exporter-otlp-proto-grpc
gunicorn==23.0.0
    # via mlflow
h11==0.14.0
    # via httpcore
    # via uvicorn
    # via wsproto
httpcore==1.0.6
    # via httpx
httpx==0.27.2
    # via anthropic
    # via chainlit
    # via cohere
    # via langchain-mistralai
    # via langgraph-sdk
    # via langsmith
    # via literalai
    # via megaparse-sdk
    # via openai
    # via quivr-core
httpx-sse==0.4.0
    # via cohere
    # via langchain-community
    # via langchain-mistralai
huggingface-hub==0.25.2
    # via tokenizers
    # via transformers
idna==3.10
    # via anyio
    # via httpx
    # via requests
    # via yarl
importlib-metadata==6.11.0
    # via mlflow-skinny
    # via opentelemetry-api
    # via sagemaker
    # via sagemaker-core
itsdangerous==2.2.0
    # via flask
jinja2==3.1.4
    # via flask
    # via mlflow
jiter==0.6.1
    # via anthropic
    # via openai
jmespath==1.0.1
    # via boto3
    # via botocore
joblib==1.4.2
    # via scikit-learn
jsonpatch==1.33
    # via langchain-core
jsonpointer==3.0.0
    # via jsonpatch
jsonschema==4.23.0
    # via sagemaker
    # via sagemaker-core
jsonschema-specifications==2024.10.1
    # via jsonschema
kiwisolver==1.4.7
    # via matplotlib
langchain==0.3.9
    # via langchain-community
    # via quivr-core
langchain-anthropic==0.3.0
    # via quivr-core
langchain-cohere==0.3.3
    # via quivr-core
langchain-community==0.3.9
    # via langchain-experimental
    # via quivr-core
langchain-core==0.3.21
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-community
    # via langchain-experimental
    # via langchain-mistralai
    # via langchain-openai
    # via langchain-text-splitters
    # via langgraph
    # via langgraph-checkpoint
    # via quivr-core
langchain-experimental==0.3.3
    # via langchain-cohere
langchain-mistralai==0.2.3
    # via quivr-core
langchain-openai==0.2.11
    # via quivr-core
langchain-text-splitters==0.3.2
    # via langchain
langgraph==0.2.56
    # via quivr-core
langgraph-checkpoint==2.0.8
    # via langgraph
langgraph-sdk==0.1.43
    # via langgraph
langsmith==0.1.135
    # via langchain
    # via langchain-community
    # via langchain-core
lazify==0.4.0
    # via chainlit
literalai==0.0.623
    # via chainlit
loguru==0.7.2
    # via megaparse-sdk
mako==1.3.5
    # via alembic
markdown==3.7
    # via mlflow
markdown-it-py==3.0.0
    # via rich
markupsafe==3.0.1
    # via jinja2
    # via mako
    # via quivr-core
    # via werkzeug
marshmallow==3.22.0
    # via dataclasses-json
matplotlib==3.9.2
    # via mlflow
mdurl==0.1.2
    # via markdown-it-py
megaparse-sdk==0.1.10
    # via quivr-core
mlflow==2.17.0
    # via sagemaker-mlflow
mlflow-skinny==2.17.0
    # via mlflow
mock==4.0.3
    # via sagemaker-core
msgpack==1.1.0
    # via langgraph-checkpoint
multidict==6.1.0
    # via aiohttp
    # via yarl
multiprocess==0.70.17
    # via pathos
mypy-extensions==1.0.0
    # via typing-inspect
nats-py==2.9.0
    # via megaparse-sdk
nest-asyncio==1.6.0
    # via chainlit
numpy==1.26.4
    # via chainlit
    # via contourpy
    # via faiss-cpu
    # via langchain
    # via langchain-community
    # via matplotlib
    # via mlflow
    # via pandas
    # via pyarrow
    # via sagemaker
    # via scikit-learn
    # via scipy
    # via transformers
openai==1.56.2
    # via langchain-openai
opentelemetry-api==1.27.0
    # via mlflow-skinny
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
    # via opentelemetry-instrumentation
    # via opentelemetry-sdk
    # via opentelemetry-semantic-conventions
    # via uptrace
opentelemetry-exporter-otlp==1.27.0
    # via uptrace
opentelemetry-exporter-otlp-proto-common==1.27.0
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
opentelemetry-exporter-otlp-proto-grpc==1.27.0
    # via opentelemetry-exporter-otlp
opentelemetry-exporter-otlp-proto-http==1.27.0
    # via opentelemetry-exporter-otlp
opentelemetry-instrumentation==0.48b0
    # via uptrace
opentelemetry-proto==1.27.0
    # via opentelemetry-exporter-otlp-proto-common
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
opentelemetry-sdk==1.27.0
    # via mlflow-skinny
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
    # via uptrace
opentelemetry-semantic-conventions==0.48b0
    # via opentelemetry-sdk
orjson==3.10.7
    # via langgraph-sdk
    # via langsmith
packaging==23.2
    # via chainlit
    # via faiss-cpu
    # via gunicorn
    # via huggingface-hub
    # via langchain-core
    # via literalai
    # via marshmallow
    # via matplotlib
    # via mlflow-skinny
    # via sagemaker
    # via transformers
pandas==2.2.3
    # via langchain-cohere
    # via mlflow
    # via sagemaker
parameterized==0.9.0
    # via cohere
pathos==0.3.3
    # via sagemaker
pillow==11.0.0
    # via matplotlib
platformdirs==4.3.6
    # via sagemaker
    # via sagemaker-core
pox==0.3.5
    # via pathos
ppft==1.7.6.9
    # via pathos
propcache==0.2.0
    # via yarl
protobuf==4.25.5
    # via googleapis-common-protos
    # via mlflow-skinny
    # via opentelemetry-proto
    # via sagemaker
    # via transformers
psutil==6.1.0
    # via megaparse-sdk
    # via sagemaker
pyarrow==17.0.0
    # via mlflow
pyasn1==0.6.1
    # via pyasn1-modules
    # via rsa
pyasn1-modules==0.4.1
    # via google-auth
pycryptodome==3.21.0
    # via megaparse-sdk
pydantic==2.9.2
    # via anthropic
    # via chainlit
    # via cohere
    # via fastapi
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-core
    # via langchain-mistralai
    # via langsmith
    # via literalai
    # via openai
    # via pydantic-settings
    # via quivr-core
    # via sagemaker-core
pydantic-core==2.23.4
    # via cohere
    # via pydantic
pydantic-settings==2.6.1
    # via langchain-community
pygments==2.18.0
    # via rich
pyjwt==2.9.0
    # via chainlit
pyparsing==3.2.0
    # via matplotlib
python-dateutil==2.8.2
    # via botocore
    # via matplotlib
    # via pandas
python-dotenv==1.0.1
    # via chainlit
    # via megaparse-sdk
    # via pydantic-settings
python-engineio==4.10.1
    # via python-socketio
python-multipart==0.0.9
    # via chainlit
python-socketio==5.11.4
    # via chainlit
pytz==2024.2
    # via pandas
pyyaml==6.0.2
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langchain-core
    # via mlflow-skinny
    # via sagemaker
    # via sagemaker-core
    # via transformers
quivr-core @ file:///${PROJECT_ROOT}/../../core
rapidfuzz==3.10.1
    # via quivr-core
referencing==0.35.1
    # via jsonschema
    # via jsonschema-specifications
regex==2024.9.11
    # via tiktoken
    # via transformers
requests==2.32.3
    # via cohere
    # via databricks-sdk
    # via docker
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langsmith
    # via mlflow-skinny
    # via opentelemetry-exporter-otlp-proto-http
    # via requests-toolbelt
    # via sagemaker
    # via tiktoken
    # via transformers
requests-toolbelt==1.0.0
    # via langsmith
rich==13.9.2
    # via quivr-core
    # via sagemaker-core
rpds-py==0.20.0
    # via jsonschema
    # via referencing
rsa==4.9
    # via google-auth
s3transfer==0.10.3
    # via boto3
safetensors==0.4.5
    # via transformers
sagemaker==2.232.2
    # via cohere
sagemaker-core==1.0.10
    # via sagemaker
sagemaker-mlflow==0.1.0
    # via sagemaker
schema==0.7.7
    # via sagemaker
scikit-learn==1.5.2
    # via mlflow
scipy==1.14.1
    # via mlflow
    # via scikit-learn
sentencepiece==0.2.0
    # via transformers
setuptools==75.2.0
    # via opentelemetry-instrumentation
simple-websocket==1.1.0
    # via python-engineio
six==1.16.0
    # via google-pasta
    # via python-dateutil
smdebug-rulesconfig==1.0.1
    # via sagemaker
smmap==5.0.1
    # via gitdb
sniffio==1.3.1
    # via anthropic
    # via anyio
    # via httpx
    # via openai
sqlalchemy==2.0.36
    # via alembic
    # via langchain
    # via langchain-community
    # via mlflow
sqlparse==0.5.1
    # via mlflow-skinny
starlette==0.41.2
    # via chainlit
    # via fastapi
syncer==2.0.3
    # via chainlit
tabulate==0.9.0
    # via langchain-cohere
tblib==3.0.0
    # via sagemaker
tenacity==8.5.0
    # via langchain
    # via langchain-community
    # via langchain-core
threadpoolctl==3.5.0
    # via scikit-learn
tiktoken==0.8.0
    # via langchain-openai
    # via quivr-core
tokenizers==0.20.1
    # via cohere
    # via langchain-mistralai
    # via transformers
tomli==2.0.2
    # via chainlit
tqdm==4.66.5
    # via huggingface-hub
    # via openai
    # via sagemaker
    # via transformers
transformers==4.45.2
    # via quivr-core
types-pyyaml==6.0.12.20240917
    # via quivr-core
types-requests==2.32.0.20241016
    # via cohere
typing-extensions==4.12.2
    # via alembic
    # via anthropic
    # via cohere
    # via fastapi
    # via huggingface-hub
    # via langchain-core
    # via openai
    # via opentelemetry-sdk
    # via pydantic
    # via pydantic-core
    # via sqlalchemy
    # via typing-inspect
typing-inspect==0.9.0
    # via dataclasses-json
tzdata==2024.2
    # via pandas
uptrace==1.27.0
    # via chainlit
urllib3==2.2.3
    # via botocore
    # via docker
    # via requests
    # via sagemaker
    # via types-requests
uvicorn==0.25.0
    # via chainlit
watchfiles==0.20.0
    # via chainlit
werkzeug==3.0.4
    # via flask
wrapt==1.16.0
    # via deprecated
    # via opentelemetry-instrumentation
wsproto==1.2.0
    # via simple-websocket
yarl==1.15.4
    # via aiohttp
zipp==3.20.2
    # via importlib-metadata
```

## File: `examples/chatbot/requirements.lock`
```
# generated by rye
# use `rye lock` or `rye sync` to update this lockfile
#
# last locked with the following flags:
#   pre: false
#   features: []
#   all-features: false
#   with-sources: false
#   generate-hashes: false
#   universal: false

aiofiles==23.2.1
    # via chainlit
    # via quivr-core
aiohappyeyeballs==2.4.3
    # via aiohttp
aiohttp==3.10.10
    # via langchain
    # via langchain-community
aiosignal==1.3.1
    # via aiohttp
alembic==1.13.3
    # via mlflow
aniso8601==9.0.1
    # via graphene
annotated-types==0.7.0
    # via pydantic
anthropic==0.40.0
    # via langchain-anthropic
anyio==4.6.2.post1
    # via anthropic
    # via asyncer
    # via httpx
    # via openai
    # via starlette
    # via watchfiles
asyncer==0.0.7
    # via chainlit
attrs==23.2.0
    # via aiohttp
    # via jsonschema
    # via referencing
    # via sagemaker
bidict==0.23.1
    # via python-socketio
blinker==1.8.2
    # via flask
boto3==1.35.42
    # via cohere
    # via sagemaker
    # via sagemaker-core
    # via sagemaker-mlflow
botocore==1.35.42
    # via boto3
    # via s3transfer
cachetools==5.5.0
    # via google-auth
    # via mlflow-skinny
certifi==2024.8.30
    # via httpcore
    # via httpx
    # via requests
chainlit==1.3.2
charset-normalizer==3.4.0
    # via requests
chevron==0.14.0
    # via literalai
click==8.1.7
    # via chainlit
    # via flask
    # via mlflow-skinny
    # via uvicorn
cloudpickle==2.2.1
    # via mlflow-skinny
    # via sagemaker
cohere==5.11.0
    # via langchain-cohere
contourpy==1.3.0
    # via matplotlib
cycler==0.12.1
    # via matplotlib
databricks-sdk==0.34.0
    # via mlflow-skinny
dataclasses-json==0.6.7
    # via chainlit
    # via langchain-community
defusedxml==0.7.1
    # via langchain-anthropic
deprecated==1.2.14
    # via opentelemetry-api
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
    # via opentelemetry-semantic-conventions
dill==0.3.9
    # via multiprocess
    # via pathos
distro==1.9.0
    # via anthropic
    # via openai
docker==7.1.0
    # via mlflow
    # via sagemaker
faiss-cpu==1.9.0
    # via quivr-core
fastapi==0.115.5
    # via chainlit
fastavro==1.9.7
    # via cohere
filelock==3.16.1
    # via huggingface-hub
    # via transformers
filetype==1.2.0
    # via chainlit
flask==3.0.3
    # via mlflow
fonttools==4.54.1
    # via matplotlib
frozenlist==1.4.1
    # via aiohttp
    # via aiosignal
fsspec==2024.9.0
    # via huggingface-hub
gitdb==4.0.11
    # via gitpython
gitpython==3.1.43
    # via mlflow-skinny
google-auth==2.35.0
    # via databricks-sdk
google-pasta==0.2.0
    # via sagemaker
googleapis-common-protos==1.65.0
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
graphene==3.3
    # via mlflow
graphql-core==3.2.5
    # via graphene
    # via graphql-relay
graphql-relay==3.2.0
    # via graphene
grpcio==1.67.0
    # via opentelemetry-exporter-otlp-proto-grpc
gunicorn==23.0.0
    # via mlflow
h11==0.14.0
    # via httpcore
    # via uvicorn
    # via wsproto
httpcore==1.0.6
    # via httpx
httpx==0.27.2
    # via anthropic
    # via chainlit
    # via cohere
    # via langchain-mistralai
    # via langgraph-sdk
    # via langsmith
    # via literalai
    # via megaparse-sdk
    # via openai
    # via quivr-core
httpx-sse==0.4.0
    # via cohere
    # via langchain-community
    # via langchain-mistralai
huggingface-hub==0.25.2
    # via tokenizers
    # via transformers
idna==3.10
    # via anyio
    # via httpx
    # via requests
    # via yarl
importlib-metadata==6.11.0
    # via mlflow-skinny
    # via opentelemetry-api
    # via sagemaker
    # via sagemaker-core
itsdangerous==2.2.0
    # via flask
jinja2==3.1.4
    # via flask
    # via mlflow
jiter==0.6.1
    # via anthropic
    # via openai
jmespath==1.0.1
    # via boto3
    # via botocore
joblib==1.4.2
    # via scikit-learn
jsonpatch==1.33
    # via langchain-core
jsonpointer==3.0.0
    # via jsonpatch
jsonschema==4.23.0
    # via sagemaker
    # via sagemaker-core
jsonschema-specifications==2024.10.1
    # via jsonschema
kiwisolver==1.4.7
    # via matplotlib
langchain==0.3.9
    # via langchain-community
    # via quivr-core
langchain-anthropic==0.3.0
    # via quivr-core
langchain-cohere==0.3.3
    # via quivr-core
langchain-community==0.3.9
    # via langchain-experimental
    # via quivr-core
langchain-core==0.3.21
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-community
    # via langchain-experimental
    # via langchain-mistralai
    # via langchain-openai
    # via langchain-text-splitters
    # via langgraph
    # via langgraph-checkpoint
    # via quivr-core
langchain-experimental==0.3.3
    # via langchain-cohere
langchain-mistralai==0.2.3
    # via quivr-core
langchain-openai==0.2.11
    # via quivr-core
langchain-text-splitters==0.3.2
    # via langchain
langgraph==0.2.56
    # via quivr-core
langgraph-checkpoint==2.0.8
    # via langgraph
langgraph-sdk==0.1.43
    # via langgraph
langsmith==0.1.135
    # via langchain
    # via langchain-community
    # via langchain-core
lazify==0.4.0
    # via chainlit
literalai==0.0.623
    # via chainlit
loguru==0.7.2
    # via megaparse-sdk
mako==1.3.5
    # via alembic
markdown==3.7
    # via mlflow
markdown-it-py==3.0.0
    # via rich
markupsafe==3.0.1
    # via jinja2
    # via mako
    # via quivr-core
    # via werkzeug
marshmallow==3.22.0
    # via dataclasses-json
matplotlib==3.9.2
    # via mlflow
mdurl==0.1.2
    # via markdown-it-py
megaparse-sdk==0.1.10
    # via quivr-core
mlflow==2.17.0
    # via sagemaker-mlflow
mlflow-skinny==2.17.0
    # via mlflow
mock==4.0.3
    # via sagemaker-core
msgpack==1.1.0
    # via langgraph-checkpoint
multidict==6.1.0
    # via aiohttp
    # via yarl
multiprocess==0.70.17
    # via pathos
mypy-extensions==1.0.0
    # via typing-inspect
nats-py==2.9.0
    # via megaparse-sdk
nest-asyncio==1.6.0
    # via chainlit
numpy==1.26.4
    # via chainlit
    # via contourpy
    # via faiss-cpu
    # via langchain
    # via langchain-community
    # via matplotlib
    # via mlflow
    # via pandas
    # via pyarrow
    # via sagemaker
    # via scikit-learn
    # via scipy
    # via transformers
openai==1.56.2
    # via langchain-openai
opentelemetry-api==1.27.0
    # via mlflow-skinny
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
    # via opentelemetry-instrumentation
    # via opentelemetry-sdk
    # via opentelemetry-semantic-conventions
    # via uptrace
opentelemetry-exporter-otlp==1.27.0
    # via uptrace
opentelemetry-exporter-otlp-proto-common==1.27.0
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
opentelemetry-exporter-otlp-proto-grpc==1.27.0
    # via opentelemetry-exporter-otlp
opentelemetry-exporter-otlp-proto-http==1.27.0
    # via opentelemetry-exporter-otlp
opentelemetry-instrumentation==0.48b0
    # via uptrace
opentelemetry-proto==1.27.0
    # via opentelemetry-exporter-otlp-proto-common
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
opentelemetry-sdk==1.27.0
    # via mlflow-skinny
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
    # via uptrace
opentelemetry-semantic-conventions==0.48b0
    # via opentelemetry-sdk
orjson==3.10.7
    # via langgraph-sdk
    # via langsmith
packaging==23.2
    # via chainlit
    # via faiss-cpu
    # via gunicorn
    # via huggingface-hub
    # via langchain-core
    # via literalai
    # via marshmallow
    # via matplotlib
    # via mlflow-skinny
    # via sagemaker
    # via transformers
pandas==2.2.3
    # via langchain-cohere
    # via mlflow
    # via sagemaker
parameterized==0.9.0
    # via cohere
pathos==0.3.3
    # via sagemaker
pillow==11.0.0
    # via matplotlib
platformdirs==4.3.6
    # via sagemaker
    # via sagemaker-core
pox==0.3.5
    # via pathos
ppft==1.7.6.9
    # via pathos
propcache==0.2.0
    # via yarl
protobuf==4.25.5
    # via googleapis-common-protos
    # via mlflow-skinny
    # via opentelemetry-proto
    # via sagemaker
    # via transformers
psutil==6.1.0
    # via megaparse-sdk
    # via sagemaker
pyarrow==17.0.0
    # via mlflow
pyasn1==0.6.1
    # via pyasn1-modules
    # via rsa
pyasn1-modules==0.4.1
    # via google-auth
pycryptodome==3.21.0
    # via megaparse-sdk
pydantic==2.9.2
    # via anthropic
    # via chainlit
    # via cohere
    # via fastapi
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-core
    # via langchain-mistralai
    # via langsmith
    # via literalai
    # via openai
    # via pydantic-settings
    # via quivr-core
    # via sagemaker-core
pydantic-core==2.23.4
    # via cohere
    # via pydantic
pydantic-settings==2.6.1
    # via langchain-community
pygments==2.18.0
    # via rich
pyjwt==2.9.0
    # via chainlit
pyparsing==3.2.0
    # via matplotlib
python-dateutil==2.8.2
    # via botocore
    # via matplotlib
    # via pandas
python-dotenv==1.0.1
    # via chainlit
    # via megaparse-sdk
    # via pydantic-settings
python-engineio==4.10.1
    # via python-socketio
python-multipart==0.0.9
    # via chainlit
python-socketio==5.11.4
    # via chainlit
pytz==2024.2
    # via pandas
pyyaml==6.0.2
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langchain-core
    # via mlflow-skinny
    # via sagemaker
    # via sagemaker-core
    # via transformers
quivr-core @ file:///${PROJECT_ROOT}/../../core
rapidfuzz==3.10.1
    # via quivr-core
referencing==0.35.1
    # via jsonschema
    # via jsonschema-specifications
regex==2024.9.11
    # via tiktoken
    # via transformers
requests==2.32.3
    # via cohere
    # via databricks-sdk
    # via docker
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langsmith
    # via mlflow-skinny
    # via opentelemetry-exporter-otlp-proto-http
    # via requests-toolbelt
    # via sagemaker
    # via tiktoken
    # via transformers
requests-toolbelt==1.0.0
    # via langsmith
rich==13.9.2
    # via quivr-core
    # via sagemaker-core
rpds-py==0.20.0
    # via jsonschema
    # via referencing
rsa==4.9
    # via google-auth
s3transfer==0.10.3
    # via boto3
safetensors==0.4.5
    # via transformers
sagemaker==2.232.2
    # via cohere
sagemaker-core==1.0.10
    # via sagemaker
sagemaker-mlflow==0.1.0
    # via sagemaker
schema==0.7.7
    # via sagemaker
scikit-learn==1.5.2
    # via mlflow
scipy==1.14.1
    # via mlflow
    # via scikit-learn
sentencepiece==0.2.0
    # via transformers
setuptools==75.2.0
    # via opentelemetry-instrumentation
simple-websocket==1.1.0
    # via python-engineio
six==1.16.0
    # via google-pasta
    # via python-dateutil
smdebug-rulesconfig==1.0.1
    # via sagemaker
smmap==5.0.1
    # via gitdb
sniffio==1.3.1
    # via anthropic
    # via anyio
    # via httpx
    # via openai
sqlalchemy==2.0.36
    # via alembic
    # via langchain
    # via langchain-community
    # via mlflow
sqlparse==0.5.1
    # via mlflow-skinny
starlette==0.41.2
    # via chainlit
    # via fastapi
syncer==2.0.3
    # via chainlit
tabulate==0.9.0
    # via langchain-cohere
tblib==3.0.0
    # via sagemaker
tenacity==8.5.0
    # via langchain
    # via langchain-community
    # via langchain-core
threadpoolctl==3.5.0
    # via scikit-learn
tiktoken==0.8.0
    # via langchain-openai
    # via quivr-core
tokenizers==0.20.1
    # via cohere
    # via langchain-mistralai
    # via transformers
tomli==2.0.2
    # via chainlit
tqdm==4.66.5
    # via huggingface-hub
    # via openai
    # via sagemaker
    # via transformers
transformers==4.45.2
    # via quivr-core
types-pyyaml==6.0.12.20240917
    # via quivr-core
types-requests==2.32.0.20241016
    # via cohere
typing-extensions==4.12.2
    # via alembic
    # via anthropic
    # via cohere
    # via fastapi
    # via huggingface-hub
    # via langchain-core
    # via openai
    # via opentelemetry-sdk
    # via pydantic
    # via pydantic-core
    # via sqlalchemy
    # via typing-inspect
typing-inspect==0.9.0
    # via dataclasses-json
tzdata==2024.2
    # via pandas
uptrace==1.27.0
    # via chainlit
urllib3==2.2.3
    # via botocore
    # via docker
    # via requests
    # via sagemaker
    # via types-requests
uvicorn==0.25.0
    # via chainlit
watchfiles==0.20.0
    # via chainlit
werkzeug==3.0.4
    # via flask
wrapt==1.16.0
    # via deprecated
    # via opentelemetry-instrumentation
wsproto==1.2.0
    # via simple-websocket
yarl==1.15.4
    # via aiohttp
zipp==3.20.2
    # via importlib-metadata
```

## File: `examples/chatbot_voice/.gitignore`
```
# python generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# venv
.venv
.files
```

## File: `examples/chatbot_voice/.python-version`
```
3.11.9
```

## File: `examples/chatbot_voice/README.md`
```markdown
# Quivr Chatbot Example

This example demonstrates how to create a simple chatbot using Quivr and Chainlit. The chatbot allows users to upload a text file and then ask questions about its content.

## Prerequisites

- Python 3.8 or higher

## Installation

1. Clone the repository or navigate to the `core/examples/chatbot` directory.

2. Install the required dependencies:

   ```
   pip install -r requirements.lock
   ```

## Running the Chatbot

1. Start the Chainlit server:

   ```
   chainlit run main.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8000`).

## Using the Chatbot

1. When the chatbot interface loads, you will be prompted to upload a text file.

2. Click on the upload area and select a `.txt` file from your computer. The file size should not exceed 20MB.

3. After uploading, the chatbot will process the file and inform you when it's ready.

4. You can now start asking questions about the content of the uploaded file.

5. Type your questions in the chat input and press Enter. The chatbot will respond based on the information in the uploaded file.

## How It Works

The chatbot uses the Quivr library to create a "brain" from the uploaded text file. This brain is then used to answer questions about the file's content. The Chainlit library provides the user interface and handles the chat interactions.

Enjoy chatting with your documents!
```

## File: `examples/chatbot_voice/basic_rag_workflow.yaml`
```yaml
workflow_config:
  name: "standard RAG"
  nodes:
    - name: "START"
      edges: ["filter_history"]

    - name: "filter_history"
      edges: ["rewrite"]

    - name: "rewrite"
      edges: ["retrieve"]

    - name: "retrieve"
      edges: ["generate_rag"]

    - name: "generate_rag" # the name of the last node, from which we want to stream the answer to the user
      edges: ["END"]

# Maximum number of previous conversation iterations
# to include in the context of the answer
max_history: 10

# Reranker configuration
# reranker_config:
#   # The reranker supplier to use
#   supplier: "cohere"

#   # The model to use for the reranker for the given supplier
#   model: "rerank-multilingual-v3.0"

#   # Number of chunks returned by the reranker
#   top_n: 5

# Configuration for the LLM
llm_config:

  # maximum number of tokens passed to the LLM to generate the answer
  max_output_tokens: 4000

  # temperature for the LLM
  temperature: 0.7
```

## File: `examples/chatbot_voice/chainlit.md`
```markdown
# Quivr Chatbot Example

This example demonstrates how to create a simple chatbot using Quivr and Chainlit. The chatbot allows users to upload a text file and then ask questions about its content.

## Prerequisites

- Python 3.8 or higher

## Installation

1. Clone the repository or navigate to the `backend/core/examples/chatbot` directory.

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Running the Chatbot

1. Start the Chainlit server:

   ```
   chainlit run main.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8000`).

## Using the Chatbot

1. When the chatbot interface loads, you will be prompted to upload a text file.

2. Click on the upload area and select a `.txt` file from your computer. The file size should not exceed 20MB.

3. After uploading, the chatbot will process the file and inform you when it's ready.

4. You can now start asking questions about the content of the uploaded file.

5. Type your questions in the chat input and press Enter. The chatbot will respond based on the information in the uploaded file.

## How It Works

The chatbot uses the Quivr library to create a "brain" from the uploaded text file. This brain is then used to answer questions about the file's content. The Chainlit library provides the user interface and handles the chat interactions.

Enjoy chatting with your documents!
```

## File: `examples/chatbot_voice/main.py`
```python
import tempfile
import os
import chainlit as cl
from quivr_core import Brain
from quivr_core.rag.entities.config import RetrievalConfig
from openai import AsyncOpenAI
from chainlit.element import Element

from io import BytesIO


@cl.on_chat_start
async def on_chat_start():
    files = None

    # Wait for the user to upload a file
    while files is None:
        files = await cl.AskFileMessage(
            content="Please upload a text .txt file to begin!",
            accept=["text/plain"],
            max_size_mb=20,
            timeout=180,
        ).send()

    file = files[0]

    msg = cl.Message(content=f"Processing `{file.name}`...")
    await msg.send()

    with open(file.path, "r", encoding="utf-8") as f:
        text = f.read()

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=file.name, delete=False
    ) as temp_file:
        temp_file.write(text)
        temp_file.flush()
        temp_file_path = temp_file.name

    brain = Brain.from_files(name="user_brain", file_paths=[temp_file_path])

    # Store the file path in the session
    cl.user_session.set("file_path", temp_file_path)

    # Let the user know that the system is ready
    msg.content = f"Processing `{file.name}` done. You can now ask questions!"
    await msg.update()

    cl.user_session.set("brain", brain)


@cl.on_message
async def main(message: cl.Message):

    task_list = cl.TaskList(name="State")
    task_list.status = "Running..."

    think = cl.Task(title="Thinking", status=cl.TaskStatus.RUNNING)
    await task_list.add_task(think)

    tts = cl.Task(title="Text to speech")
    await task_list.add_task(tts)

    await task_list.send()

    brain = cl.user_session.get("brain")  # type: Brain
    path_config = "basic_rag_workflow.yaml"
    retrieval_config = RetrievalConfig.from_yaml(path_config)

    if brain is None:
        await cl.Message(content="Please upload a file first.").send()
        return

    # Prepare the message for streaming
    msg = cl.Message(content="", elements=[], author="Quivr", type="assistant_message")
    await msg.send()

    saved_sources = set()
    saved_sources_complete = []
    elements = []

    # Use the ask_stream method for streaming responses
    async for chunk in brain.ask_streaming(message.content, retrieval_config=retrieval_config):
        await msg.stream_token(chunk.answer)
        for source in chunk.metadata.sources:
            if source.page_content not in saved_sources:
                saved_sources.add(source.page_content)
                saved_sources_complete.append(source)
                print(source)
                elements.append(cl.Text(name=source.metadata["original_file_name"], content=source.page_content, display="side"))
    
    think.status = cl.TaskStatus.DONE
    tts.status = cl.TaskStatus.RUNNING
    await task_list.update()
    
    audio_file = await text_to_speech(msg.content)
    elements.append(cl.Audio(content=audio_file, auto_play=True, mime="audio/mpeg"))

    sources = ""
    for source in saved_sources_complete:
        sources += f"- {source.metadata['original_file_name']}\n"
    msg.elements = elements
    msg.content = msg.content + f"\n\nSources:\n{sources}"
    await msg.update()

    tts.status = cl.TaskStatus.DONE
    task_list.status = "Done"
    await task_list.update()
    await cl.sleep(1)
    await task_list.remove()

async_openai_client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@cl.step(type="tool", name="Speech to text")
async def speech_to_text(audio_file):
    response = await async_openai_client.audio.transcriptions.create(
        model="whisper-1", file=audio_file
    )

    return response.text

@cl.step(type="tool", name="Text to speech")
async def text_to_speech(text):
    response = await async_openai_client.audio.speech.create(
        model="tts-1", voice="alloy", input=text
    )

    return response.content


@cl.on_audio_chunk
async def on_audio_chunk(chunk: cl.AudioChunk):
    if chunk.isStart:
        buffer = BytesIO()
        # This is required for whisper to recognize the file type
        buffer.name = f"input_audio.{chunk.mimeType.split('/')[1]}"
        # Initialize the session for a new audio stream
        cl.user_session.set("audio_buffer", buffer)
        cl.user_session.set("audio_mime_type", chunk.mimeType)

    # Write the chunks to a buffer and transcribe the whole audio at the end
    cl.user_session.get("audio_buffer").write(chunk.data)


@cl.on_audio_end
async def on_audio_end(elements: list[Element]):
    # Get the audio buffer from the session
    task_list = cl.TaskList(name="State")
    task_list.status = "Running..."

    stt = cl.Task(title="Speech to text", status=cl.TaskStatus.RUNNING)
    await task_list.add_task(stt)

    await task_list.send()

    audio_buffer: BytesIO = cl.user_session.get("audio_buffer")
    audio_buffer.seek(0)  # Move the file pointer to the beginning
    audio_file = audio_buffer.read()
    audio_mime_type: str = cl.user_session.get("audio_mime_type")

    input_audio_el = cl.Audio(
        mime=audio_mime_type, content=audio_file, name=audio_buffer.name
    )
    await cl.Message(
        author="You",
        type="user_message",
        content="",
        elements=[input_audio_el, *elements],
    ).send()

    whisper_input = (audio_buffer.name, audio_file, audio_mime_type)
    transcription = await speech_to_text(whisper_input)

    msg = cl.Message(author="You", content=transcription, elements=elements)

    stt.status = cl.TaskStatus.DONE
    task_list.status = "Done"
    await task_list.update()
    await cl.sleep(1)
    await task_list.remove()

    await main(message=msg)
```

## File: `examples/chatbot_voice/pyproject.toml`
```
[project]
name = "chatbot"
version = "0.1.0"
description = "Add your description here"
authors = [
    { name = "Stan Girard", email = "stan@quivr.app" }
]
dependencies = [
    "quivr-core @ file:///${PROJECT_ROOT}/../../core",
    "chainlit>=1.2.0",
    "openai>=1.54.5",
]
readme = "README.md"
requires-python = ">= 3.11"

[tool.rye]
managed = true
virtual = true
dev-dependencies = []
```

## File: `examples/chatbot_voice/requirements-dev.lock`
```
# generated by rye
# use `rye lock` or `rye sync` to update this lockfile
#
# last locked with the following flags:
#   pre: false
#   features: []
#   all-features: false
#   with-sources: false
#   generate-hashes: false
#   universal: false

aiofiles==23.2.1
    # via chainlit
    # via quivr-core
aiohappyeyeballs==2.4.3
    # via aiohttp
aiohttp==3.10.10
    # via langchain
    # via langchain-community
aiosignal==1.3.1
    # via aiohttp
alembic==1.13.3
    # via mlflow
aniso8601==9.0.1
    # via graphene
annotated-types==0.7.0
    # via pydantic
anthropic==0.40.0
    # via langchain-anthropic
anyio==4.6.2.post1
    # via anthropic
    # via asyncer
    # via httpx
    # via openai
    # via starlette
    # via watchfiles
asyncer==0.0.7
    # via chainlit
attrs==23.2.0
    # via aiohttp
    # via jsonschema
    # via referencing
    # via sagemaker
bidict==0.23.1
    # via python-socketio
blinker==1.8.2
    # via flask
boto3==1.35.42
    # via cohere
    # via sagemaker
    # via sagemaker-core
    # via sagemaker-mlflow
botocore==1.35.42
    # via boto3
    # via s3transfer
cachetools==5.5.0
    # via google-auth
    # via mlflow-skinny
certifi==2024.8.30
    # via httpcore
    # via httpx
    # via requests
chainlit==1.3.2
charset-normalizer==3.4.0
    # via requests
chevron==0.14.0
    # via literalai
click==8.1.7
    # via chainlit
    # via flask
    # via mlflow-skinny
    # via uvicorn
cloudpickle==2.2.1
    # via mlflow-skinny
    # via sagemaker
cohere==5.11.0
    # via langchain-cohere
contourpy==1.3.0
    # via matplotlib
cycler==0.12.1
    # via matplotlib
databricks-sdk==0.34.0
    # via mlflow-skinny
dataclasses-json==0.6.7
    # via chainlit
    # via langchain-community
defusedxml==0.7.1
    # via langchain-anthropic
deprecated==1.2.14
    # via opentelemetry-api
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
    # via opentelemetry-semantic-conventions
dill==0.3.9
    # via multiprocess
    # via pathos
distro==1.9.0
    # via anthropic
    # via openai
docker==7.1.0
    # via mlflow
    # via sagemaker
faiss-cpu==1.9.0
    # via quivr-core
fastapi==0.115.5
    # via chainlit
fastavro==1.9.7
    # via cohere
filelock==3.16.1
    # via huggingface-hub
    # via transformers
filetype==1.2.0
    # via chainlit
flask==3.0.3
    # via mlflow
fonttools==4.54.1
    # via matplotlib
frozenlist==1.4.1
    # via aiohttp
    # via aiosignal
fsspec==2024.9.0
    # via huggingface-hub
gitdb==4.0.11
    # via gitpython
gitpython==3.1.43
    # via mlflow-skinny
google-auth==2.35.0
    # via databricks-sdk
google-pasta==0.2.0
    # via sagemaker
googleapis-common-protos==1.65.0
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
graphene==3.3
    # via mlflow
graphql-core==3.2.5
    # via graphene
    # via graphql-relay
graphql-relay==3.2.0
    # via graphene
grpcio==1.67.0
    # via opentelemetry-exporter-otlp-proto-grpc
gunicorn==23.0.0
    # via mlflow
h11==0.14.0
    # via httpcore
    # via uvicorn
    # via wsproto
httpcore==1.0.6
    # via httpx
httpx==0.27.2
    # via anthropic
    # via chainlit
    # via cohere
    # via langchain-mistralai
    # via langgraph-sdk
    # via langsmith
    # via literalai
    # via megaparse-sdk
    # via openai
    # via quivr-core
httpx-sse==0.4.0
    # via cohere
    # via langchain-community
    # via langchain-mistralai
    # via langgraph-sdk
huggingface-hub==0.25.2
    # via tokenizers
    # via transformers
idna==3.10
    # via anyio
    # via httpx
    # via requests
    # via yarl
importlib-metadata==6.11.0
    # via mlflow-skinny
    # via opentelemetry-api
    # via sagemaker
    # via sagemaker-core
itsdangerous==2.2.0
    # via flask
jinja2==3.1.4
    # via flask
    # via mlflow
jiter==0.6.1
    # via anthropic
    # via openai
jmespath==1.0.1
    # via boto3
    # via botocore
joblib==1.4.2
    # via scikit-learn
jsonpatch==1.33
    # via langchain-core
jsonpointer==3.0.0
    # via jsonpatch
jsonschema==4.23.0
    # via sagemaker
    # via sagemaker-core
jsonschema-specifications==2024.10.1
    # via jsonschema
kiwisolver==1.4.7
    # via matplotlib
langchain==0.3.9
    # via langchain-community
    # via quivr-core
langchain-anthropic==0.3.0
    # via quivr-core
langchain-cohere==0.3.3
    # via quivr-core
langchain-community==0.3.9
    # via langchain-experimental
    # via quivr-core
langchain-core==0.3.21
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-community
    # via langchain-experimental
    # via langchain-mistralai
    # via langchain-openai
    # via langchain-text-splitters
    # via langgraph
    # via langgraph-checkpoint
    # via quivr-core
langchain-experimental==0.3.3
    # via langchain-cohere
langchain-mistralai==0.2.3
    # via quivr-core
langchain-openai==0.2.11
    # via quivr-core
langchain-text-splitters==0.3.2
    # via langchain
langgraph==0.2.38
    # via quivr-core
langgraph-checkpoint==2.0.1
    # via langgraph
langgraph-sdk==0.1.33
    # via langgraph
langsmith==0.1.135
    # via langchain
    # via langchain-community
    # via langchain-core
lazify==0.4.0
    # via chainlit
literalai==0.0.623
    # via chainlit
loguru==0.7.2
    # via megaparse-sdk
mako==1.3.5
    # via alembic
markdown==3.7
    # via mlflow
markdown-it-py==3.0.0
    # via rich
markupsafe==3.0.1
    # via jinja2
    # via mako
    # via quivr-core
    # via werkzeug
marshmallow==3.22.0
    # via dataclasses-json
matplotlib==3.9.2
    # via mlflow
mdurl==0.1.2
    # via markdown-it-py
megaparse-sdk==0.1.10
    # via quivr-core
mlflow==2.17.0
    # via sagemaker-mlflow
mlflow-skinny==2.17.0
    # via mlflow
mock==4.0.3
    # via sagemaker-core
msgpack==1.1.0
    # via langgraph-checkpoint
multidict==6.1.0
    # via aiohttp
    # via yarl
multiprocess==0.70.17
    # via pathos
mypy-extensions==1.0.0
    # via typing-inspect
nats-py==2.9.0
    # via megaparse-sdk
nest-asyncio==1.6.0
    # via chainlit
numpy==1.26.4
    # via chainlit
    # via contourpy
    # via faiss-cpu
    # via langchain
    # via langchain-community
    # via matplotlib
    # via mlflow
    # via pandas
    # via pyarrow
    # via sagemaker
    # via scikit-learn
    # via scipy
    # via transformers
openai==1.54.5
    # via langchain-openai
opentelemetry-api==1.27.0
    # via mlflow-skinny
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
    # via opentelemetry-instrumentation
    # via opentelemetry-sdk
    # via opentelemetry-semantic-conventions
    # via uptrace
opentelemetry-exporter-otlp==1.27.0
    # via uptrace
opentelemetry-exporter-otlp-proto-common==1.27.0
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
opentelemetry-exporter-otlp-proto-grpc==1.27.0
    # via opentelemetry-exporter-otlp
opentelemetry-exporter-otlp-proto-http==1.27.0
    # via opentelemetry-exporter-otlp
opentelemetry-instrumentation==0.48b0
    # via uptrace
opentelemetry-proto==1.27.0
    # via opentelemetry-exporter-otlp-proto-common
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
opentelemetry-sdk==1.27.0
    # via mlflow-skinny
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
    # via uptrace
opentelemetry-semantic-conventions==0.48b0
    # via opentelemetry-sdk
orjson==3.10.7
    # via langgraph-sdk
    # via langsmith
packaging==23.2
    # via chainlit
    # via faiss-cpu
    # via gunicorn
    # via huggingface-hub
    # via langchain-core
    # via literalai
    # via marshmallow
    # via matplotlib
    # via mlflow-skinny
    # via sagemaker
    # via transformers
pandas==2.2.3
    # via langchain-cohere
    # via mlflow
    # via sagemaker
parameterized==0.9.0
    # via cohere
pathos==0.3.3
    # via sagemaker
pillow==11.0.0
    # via matplotlib
platformdirs==4.3.6
    # via sagemaker
    # via sagemaker-core
pox==0.3.5
    # via pathos
ppft==1.7.6.9
    # via pathos
propcache==0.2.0
    # via yarl
protobuf==4.25.5
    # via googleapis-common-protos
    # via mlflow-skinny
    # via opentelemetry-proto
    # via sagemaker
    # via transformers
psutil==6.1.0
    # via megaparse-sdk
    # via sagemaker
pyarrow==17.0.0
    # via mlflow
pyasn1==0.6.1
    # via pyasn1-modules
    # via rsa
pyasn1-modules==0.4.1
    # via google-auth
pycryptodome==3.21.0
    # via megaparse-sdk
pydantic==2.9.2
    # via anthropic
    # via chainlit
    # via cohere
    # via fastapi
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-core
    # via langchain-mistralai
    # via langsmith
    # via literalai
    # via openai
    # via pydantic-settings
    # via quivr-core
    # via sagemaker-core
pydantic-core==2.23.4
    # via cohere
    # via pydantic
pydantic-settings==2.6.1
    # via langchain-community
pygments==2.18.0
    # via rich
pyjwt==2.9.0
    # via chainlit
pyparsing==3.2.0
    # via matplotlib
python-dateutil==2.8.2
    # via botocore
    # via matplotlib
    # via pandas
python-dotenv==1.0.1
    # via chainlit
    # via megaparse-sdk
    # via pydantic-settings
python-engineio==4.10.1
    # via python-socketio
python-multipart==0.0.9
    # via chainlit
python-socketio==5.11.4
    # via chainlit
pytz==2024.2
    # via pandas
pyyaml==6.0.2
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langchain-core
    # via mlflow-skinny
    # via sagemaker
    # via sagemaker-core
    # via transformers
quivr-core @ file:///${PROJECT_ROOT}/../../core
rapidfuzz==3.10.1
    # via quivr-core
referencing==0.35.1
    # via jsonschema
    # via jsonschema-specifications
regex==2024.9.11
    # via tiktoken
    # via transformers
requests==2.32.3
    # via cohere
    # via databricks-sdk
    # via docker
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langsmith
    # via mlflow-skinny
    # via opentelemetry-exporter-otlp-proto-http
    # via requests-toolbelt
    # via sagemaker
    # via tiktoken
    # via transformers
requests-toolbelt==1.0.0
    # via langsmith
rich==13.9.2
    # via quivr-core
    # via sagemaker-core
rpds-py==0.20.0
    # via jsonschema
    # via referencing
rsa==4.9
    # via google-auth
s3transfer==0.10.3
    # via boto3
safetensors==0.4.5
    # via transformers
sagemaker==2.232.2
    # via cohere
sagemaker-core==1.0.10
    # via sagemaker
sagemaker-mlflow==0.1.0
    # via sagemaker
schema==0.7.7
    # via sagemaker
scikit-learn==1.5.2
    # via mlflow
scipy==1.14.1
    # via mlflow
    # via scikit-learn
sentencepiece==0.2.0
    # via transformers
setuptools==75.2.0
    # via opentelemetry-instrumentation
simple-websocket==1.1.0
    # via python-engineio
six==1.16.0
    # via google-pasta
    # via python-dateutil
smdebug-rulesconfig==1.0.1
    # via sagemaker
smmap==5.0.1
    # via gitdb
sniffio==1.3.1
    # via anthropic
    # via anyio
    # via httpx
    # via openai
sqlalchemy==2.0.36
    # via alembic
    # via langchain
    # via langchain-community
    # via mlflow
sqlparse==0.5.1
    # via mlflow-skinny
starlette==0.41.2
    # via chainlit
    # via fastapi
syncer==2.0.3
    # via chainlit
tabulate==0.9.0
    # via langchain-cohere
tblib==3.0.0
    # via sagemaker
tenacity==8.5.0
    # via langchain
    # via langchain-community
    # via langchain-core
threadpoolctl==3.5.0
    # via scikit-learn
tiktoken==0.8.0
    # via langchain-openai
    # via quivr-core
tokenizers==0.20.1
    # via cohere
    # via langchain-mistralai
    # via transformers
tomli==2.0.2
    # via chainlit
tqdm==4.66.5
    # via huggingface-hub
    # via openai
    # via sagemaker
    # via transformers
transformers==4.45.2
    # via quivr-core
types-pyyaml==6.0.12.20240917
    # via quivr-core
types-requests==2.32.0.20241016
    # via cohere
typing-extensions==4.12.2
    # via alembic
    # via anthropic
    # via cohere
    # via fastapi
    # via huggingface-hub
    # via langchain-core
    # via openai
    # via opentelemetry-sdk
    # via pydantic
    # via pydantic-core
    # via sqlalchemy
    # via typing-inspect
typing-inspect==0.9.0
    # via dataclasses-json
tzdata==2024.2
    # via pandas
uptrace==1.27.0
    # via chainlit
urllib3==2.2.3
    # via botocore
    # via docker
    # via requests
    # via sagemaker
    # via types-requests
uvicorn==0.25.0
    # via chainlit
watchfiles==0.20.0
    # via chainlit
werkzeug==3.0.4
    # via flask
wrapt==1.16.0
    # via deprecated
    # via opentelemetry-instrumentation
wsproto==1.2.0
    # via simple-websocket
yarl==1.15.4
    # via aiohttp
zipp==3.20.2
    # via importlib-metadata
```

## File: `examples/chatbot_voice/requirements.lock`
```
# generated by rye
# use `rye lock` or `rye sync` to update this lockfile
#
# last locked with the following flags:
#   pre: false
#   features: []
#   all-features: false
#   with-sources: false
#   generate-hashes: false
#   universal: false

aiofiles==23.2.1
    # via chainlit
    # via quivr-core
aiohappyeyeballs==2.4.3
    # via aiohttp
aiohttp==3.10.10
    # via langchain
    # via langchain-community
aiosignal==1.3.1
    # via aiohttp
alembic==1.13.3
    # via mlflow
aniso8601==9.0.1
    # via graphene
annotated-types==0.7.0
    # via pydantic
anthropic==0.40.0
    # via langchain-anthropic
anyio==4.6.2.post1
    # via anthropic
    # via asyncer
    # via httpx
    # via openai
    # via starlette
    # via watchfiles
asyncer==0.0.7
    # via chainlit
attrs==23.2.0
    # via aiohttp
    # via jsonschema
    # via referencing
    # via sagemaker
bidict==0.23.1
    # via python-socketio
blinker==1.8.2
    # via flask
boto3==1.35.42
    # via cohere
    # via sagemaker
    # via sagemaker-core
    # via sagemaker-mlflow
botocore==1.35.42
    # via boto3
    # via s3transfer
cachetools==5.5.0
    # via google-auth
    # via mlflow-skinny
certifi==2024.8.30
    # via httpcore
    # via httpx
    # via requests
chainlit==1.3.2
charset-normalizer==3.4.0
    # via requests
chevron==0.14.0
    # via literalai
click==8.1.7
    # via chainlit
    # via flask
    # via mlflow-skinny
    # via uvicorn
cloudpickle==2.2.1
    # via mlflow-skinny
    # via sagemaker
cohere==5.11.0
    # via langchain-cohere
contourpy==1.3.0
    # via matplotlib
cycler==0.12.1
    # via matplotlib
databricks-sdk==0.34.0
    # via mlflow-skinny
dataclasses-json==0.6.7
    # via chainlit
    # via langchain-community
defusedxml==0.7.1
    # via langchain-anthropic
deprecated==1.2.14
    # via opentelemetry-api
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
    # via opentelemetry-semantic-conventions
dill==0.3.9
    # via multiprocess
    # via pathos
distro==1.9.0
    # via anthropic
    # via openai
docker==7.1.0
    # via mlflow
    # via sagemaker
faiss-cpu==1.9.0
    # via quivr-core
fastapi==0.115.5
    # via chainlit
fastavro==1.9.7
    # via cohere
filelock==3.16.1
    # via huggingface-hub
    # via transformers
filetype==1.2.0
    # via chainlit
flask==3.0.3
    # via mlflow
fonttools==4.54.1
    # via matplotlib
frozenlist==1.4.1
    # via aiohttp
    # via aiosignal
fsspec==2024.9.0
    # via huggingface-hub
gitdb==4.0.11
    # via gitpython
gitpython==3.1.43
    # via mlflow-skinny
google-auth==2.35.0
    # via databricks-sdk
google-pasta==0.2.0
    # via sagemaker
googleapis-common-protos==1.65.0
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
graphene==3.3
    # via mlflow
graphql-core==3.2.5
    # via graphene
    # via graphql-relay
graphql-relay==3.2.0
    # via graphene
grpcio==1.67.0
    # via opentelemetry-exporter-otlp-proto-grpc
gunicorn==23.0.0
    # via mlflow
h11==0.14.0
    # via httpcore
    # via uvicorn
    # via wsproto
httpcore==1.0.6
    # via httpx
httpx==0.27.2
    # via anthropic
    # via chainlit
    # via cohere
    # via langchain-mistralai
    # via langgraph-sdk
    # via langsmith
    # via literalai
    # via megaparse-sdk
    # via openai
    # via quivr-core
httpx-sse==0.4.0
    # via cohere
    # via langchain-community
    # via langchain-mistralai
    # via langgraph-sdk
huggingface-hub==0.25.2
    # via tokenizers
    # via transformers
idna==3.10
    # via anyio
    # via httpx
    # via requests
    # via yarl
importlib-metadata==6.11.0
    # via mlflow-skinny
    # via opentelemetry-api
    # via sagemaker
    # via sagemaker-core
itsdangerous==2.2.0
    # via flask
jinja2==3.1.4
    # via flask
    # via mlflow
jiter==0.6.1
    # via anthropic
    # via openai
jmespath==1.0.1
    # via boto3
    # via botocore
joblib==1.4.2
    # via scikit-learn
jsonpatch==1.33
    # via langchain-core
jsonpointer==3.0.0
    # via jsonpatch
jsonschema==4.23.0
    # via sagemaker
    # via sagemaker-core
jsonschema-specifications==2024.10.1
    # via jsonschema
kiwisolver==1.4.7
    # via matplotlib
langchain==0.3.9
    # via langchain-community
    # via quivr-core
langchain-anthropic==0.3.0
    # via quivr-core
langchain-cohere==0.3.3
    # via quivr-core
langchain-community==0.3.9
    # via langchain-experimental
    # via quivr-core
langchain-core==0.3.21
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-community
    # via langchain-experimental
    # via langchain-mistralai
    # via langchain-openai
    # via langchain-text-splitters
    # via langgraph
    # via langgraph-checkpoint
    # via quivr-core
langchain-experimental==0.3.3
    # via langchain-cohere
langchain-mistralai==0.2.3
    # via quivr-core
langchain-openai==0.2.11
    # via quivr-core
langchain-text-splitters==0.3.2
    # via langchain
langgraph==0.2.38
    # via quivr-core
langgraph-checkpoint==2.0.1
    # via langgraph
langgraph-sdk==0.1.33
    # via langgraph
langsmith==0.1.135
    # via langchain
    # via langchain-community
    # via langchain-core
lazify==0.4.0
    # via chainlit
literalai==0.0.623
    # via chainlit
loguru==0.7.2
    # via megaparse-sdk
mako==1.3.5
    # via alembic
markdown==3.7
    # via mlflow
markdown-it-py==3.0.0
    # via rich
markupsafe==3.0.1
    # via jinja2
    # via mako
    # via quivr-core
    # via werkzeug
marshmallow==3.22.0
    # via dataclasses-json
matplotlib==3.9.2
    # via mlflow
mdurl==0.1.2
    # via markdown-it-py
megaparse-sdk==0.1.10
    # via quivr-core
mlflow==2.17.0
    # via sagemaker-mlflow
mlflow-skinny==2.17.0
    # via mlflow
mock==4.0.3
    # via sagemaker-core
msgpack==1.1.0
    # via langgraph-checkpoint
multidict==6.1.0
    # via aiohttp
    # via yarl
multiprocess==0.70.17
    # via pathos
mypy-extensions==1.0.0
    # via typing-inspect
nats-py==2.9.0
    # via megaparse-sdk
nest-asyncio==1.6.0
    # via chainlit
numpy==1.26.4
    # via chainlit
    # via contourpy
    # via faiss-cpu
    # via langchain
    # via langchain-community
    # via matplotlib
    # via mlflow
    # via pandas
    # via pyarrow
    # via sagemaker
    # via scikit-learn
    # via scipy
    # via transformers
openai==1.54.5
    # via langchain-openai
opentelemetry-api==1.27.0
    # via mlflow-skinny
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
    # via opentelemetry-instrumentation
    # via opentelemetry-sdk
    # via opentelemetry-semantic-conventions
    # via uptrace
opentelemetry-exporter-otlp==1.27.0
    # via uptrace
opentelemetry-exporter-otlp-proto-common==1.27.0
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
opentelemetry-exporter-otlp-proto-grpc==1.27.0
    # via opentelemetry-exporter-otlp
opentelemetry-exporter-otlp-proto-http==1.27.0
    # via opentelemetry-exporter-otlp
opentelemetry-instrumentation==0.48b0
    # via uptrace
opentelemetry-proto==1.27.0
    # via opentelemetry-exporter-otlp-proto-common
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
opentelemetry-sdk==1.27.0
    # via mlflow-skinny
    # via opentelemetry-exporter-otlp-proto-grpc
    # via opentelemetry-exporter-otlp-proto-http
    # via uptrace
opentelemetry-semantic-conventions==0.48b0
    # via opentelemetry-sdk
orjson==3.10.7
    # via langgraph-sdk
    # via langsmith
packaging==23.2
    # via chainlit
    # via faiss-cpu
    # via gunicorn
    # via huggingface-hub
    # via langchain-core
    # via literalai
    # via marshmallow
    # via matplotlib
    # via mlflow-skinny
    # via sagemaker
    # via transformers
pandas==2.2.3
    # via langchain-cohere
    # via mlflow
    # via sagemaker
parameterized==0.9.0
    # via cohere
pathos==0.3.3
    # via sagemaker
pillow==11.0.0
    # via matplotlib
platformdirs==4.3.6
    # via sagemaker
    # via sagemaker-core
pox==0.3.5
    # via pathos
ppft==1.7.6.9
    # via pathos
propcache==0.2.0
    # via yarl
protobuf==4.25.5
    # via googleapis-common-protos
    # via mlflow-skinny
    # via opentelemetry-proto
    # via sagemaker
    # via transformers
psutil==6.1.0
    # via megaparse-sdk
    # via sagemaker
pyarrow==17.0.0
    # via mlflow
pyasn1==0.6.1
    # via pyasn1-modules
    # via rsa
pyasn1-modules==0.4.1
    # via google-auth
pycryptodome==3.21.0
    # via megaparse-sdk
pydantic==2.9.2
    # via anthropic
    # via chainlit
    # via cohere
    # via fastapi
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-core
    # via langchain-mistralai
    # via langsmith
    # via literalai
    # via openai
    # via pydantic-settings
    # via quivr-core
    # via sagemaker-core
pydantic-core==2.23.4
    # via cohere
    # via pydantic
pydantic-settings==2.6.1
    # via langchain-community
pygments==2.18.0
    # via rich
pyjwt==2.9.0
    # via chainlit
pyparsing==3.2.0
    # via matplotlib
python-dateutil==2.8.2
    # via botocore
    # via matplotlib
    # via pandas
python-dotenv==1.0.1
    # via chainlit
    # via megaparse-sdk
    # via pydantic-settings
python-engineio==4.10.1
    # via python-socketio
python-multipart==0.0.9
    # via chainlit
python-socketio==5.11.4
    # via chainlit
pytz==2024.2
    # via pandas
pyyaml==6.0.2
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langchain-core
    # via mlflow-skinny
    # via sagemaker
    # via sagemaker-core
    # via transformers
quivr-core @ file:///${PROJECT_ROOT}/../../core
rapidfuzz==3.10.1
    # via quivr-core
referencing==0.35.1
    # via jsonschema
    # via jsonschema-specifications
regex==2024.9.11
    # via tiktoken
    # via transformers
requests==2.32.3
    # via cohere
    # via databricks-sdk
    # via docker
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langsmith
    # via mlflow-skinny
    # via opentelemetry-exporter-otlp-proto-http
    # via requests-toolbelt
    # via sagemaker
    # via tiktoken
    # via transformers
requests-toolbelt==1.0.0
    # via langsmith
rich==13.9.2
    # via quivr-core
    # via sagemaker-core
rpds-py==0.20.0
    # via jsonschema
    # via referencing
rsa==4.9
    # via google-auth
s3transfer==0.10.3
    # via boto3
safetensors==0.4.5
    # via transformers
sagemaker==2.232.2
    # via cohere
sagemaker-core==1.0.10
    # via sagemaker
sagemaker-mlflow==0.1.0
    # via sagemaker
schema==0.7.7
    # via sagemaker
scikit-learn==1.5.2
    # via mlflow
scipy==1.14.1
    # via mlflow
    # via scikit-learn
sentencepiece==0.2.0
    # via transformers
setuptools==75.2.0
    # via opentelemetry-instrumentation
simple-websocket==1.1.0
    # via python-engineio
six==1.16.0
    # via google-pasta
    # via python-dateutil
smdebug-rulesconfig==1.0.1
    # via sagemaker
smmap==5.0.1
    # via gitdb
sniffio==1.3.1
    # via anthropic
    # via anyio
    # via httpx
    # via openai
sqlalchemy==2.0.36
    # via alembic
    # via langchain
    # via langchain-community
    # via mlflow
sqlparse==0.5.1
    # via mlflow-skinny
starlette==0.41.2
    # via chainlit
    # via fastapi
syncer==2.0.3
    # via chainlit
tabulate==0.9.0
    # via langchain-cohere
tblib==3.0.0
    # via sagemaker
tenacity==8.5.0
    # via langchain
    # via langchain-community
    # via langchain-core
threadpoolctl==3.5.0
    # via scikit-learn
tiktoken==0.8.0
    # via langchain-openai
    # via quivr-core
tokenizers==0.20.1
    # via cohere
    # via langchain-mistralai
    # via transformers
tomli==2.0.2
    # via chainlit
tqdm==4.66.5
    # via huggingface-hub
    # via openai
    # via sagemaker
    # via transformers
transformers==4.45.2
    # via quivr-core
types-pyyaml==6.0.12.20240917
    # via quivr-core
types-requests==2.32.0.20241016
    # via cohere
typing-extensions==4.12.2
    # via alembic
    # via anthropic
    # via cohere
    # via fastapi
    # via huggingface-hub
    # via langchain-core
    # via openai
    # via opentelemetry-sdk
    # via pydantic
    # via pydantic-core
    # via sqlalchemy
    # via typing-inspect
typing-inspect==0.9.0
    # via dataclasses-json
tzdata==2024.2
    # via pandas
uptrace==1.27.0
    # via chainlit
urllib3==2.2.3
    # via botocore
    # via docker
    # via requests
    # via sagemaker
    # via types-requests
uvicorn==0.25.0
    # via chainlit
watchfiles==0.20.0
    # via chainlit
werkzeug==3.0.4
    # via flask
wrapt==1.16.0
    # via deprecated
    # via opentelemetry-instrumentation
wsproto==1.2.0
    # via simple-websocket
yarl==1.15.4
    # via aiohttp
zipp==3.20.2
    # via importlib-metadata
```

## File: `examples/quivr-whisper/.env_example`
```
QUIVR_API_KEY=XXXX
QUIVR_CHAT_ID=1XXXX
QUIVR_BRAIN_ID=XXXX
QUIVR_URL=XXXX
OPENAI_API_KEY=XXXX
```

## File: `examples/quivr-whisper/.gitignore`
```
.env
uploads
```

## File: `examples/quivr-whisper/.python-version`
```
3.11.9
```

## File: `examples/quivr-whisper/README.md`
```markdown
# Quivr-Whisper

Quivr-Whisper is a web application that allows users to ask questions via audio input. It leverages OpenAI's Whisper model for speech transcription and synthesizes responses using OpenAI's text-to-speech capabilities. The application queries the Quivr API to get a response based on the transcribed audio input.



https://github.com/StanGirard/quivr-whisper/assets/19614572/9cc270c9-07e4-4ce1-bcff-380f195c9313



## Features

- Audio input for asking questions
- Speech transcription using OpenAI's Whisper model
- Integration with Quivr API for intelligent responses
- Speech synthesis of the response for audio playback

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.6+
- pip for Python 3
- Flask
- OpenAI Python package
- Requests package

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. Clone the repository to your local machine.
```bash
git clone https://github.com/stangirard/quivr-whisper.git
cd Quivr-talk
```

2. Install the required packages.
```bash
pip install flask openai requests python-dotenv
```

3. Create a `.env` file in the root directory of the project and add your API keys and other configuration variables.
```env
OPENAI_API_KEY='your_openai_api_key'
QUIVR_API_KEY='your_quivr_api_key'
QUIVR_CHAT_ID='your_quivr_chat_id'
QUIVR_BRAIN_ID='your_quivr_brain_id'
QUIVR_URL='https://api.quivr.app' # Optional, only if different from the default
```

4. Run the Flask application.
```bash
flask run
```

Your app should now be running on `http://localhost:5000`.

## Usage

To use Quivr-talk, navigate to `http://localhost:5000` in your web browser, click on "Ask a question to Quivr", and record your question. Wait for the transcription and response to be synthesized, and you will hear the response played back to you.
```

## File: `examples/quivr-whisper/app.py`
```python
from flask import Flask, render_template, request, jsonify, session
import openai
import base64
import os
import requests
from dotenv import load_dotenv
from quivr_core import Brain
from quivr_core.rag.entities.config import RetrievalConfig
from tempfile import NamedTemporaryFile
from werkzeug.utils import secure_filename
from asyncio import to_thread
import asyncio


UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"txt"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.secret_key = "secret"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["CACHE_TYPE"] = "SimpleCache"  # In-memory cache for development
app.config["CACHE_DEFAULT_TIMEOUT"] = 60 * 60  # 1 hour cache timeout
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

brains = {}


@app.route("/")
def index():
    return render_template("index.html")


def run_in_event_loop(func, *args, **kwargs):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    if asyncio.iscoroutinefunction(func):
        result = loop.run_until_complete(func(*args, **kwargs))
    else:
        result = func(*args, **kwargs)
    loop.close()
    return result


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["POST"])
async def upload_file():
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]

    if file.filename == "":
        return "No selected file", 400
    if not (file and file.filename and allowed_file(file.filename)):
        return "Invalid file type", 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    print(f"File uploaded and saved at: {filepath}")

    print("Creating brain instance...")

    brain: Brain = await to_thread(
        run_in_event_loop, Brain.from_files, name="user_brain", file_paths=[filepath]
    )

    # Store brain instance in cache
    session_id = session.sid if hasattr(session, "sid") else os.urandom(16).hex()
    session["session_id"] = session_id
    # cache.set(session_id, brain)  # Store the brain instance in the cache
    brains[session_id] = brain
    print(f"Brain instance created and stored in cache for session ID: {session_id}")

    return jsonify({"message": "Brain created successfully"})


@app.route("/ask", methods=["POST"])
async def ask():
    if "audio_data" not in request.files:
        return "Missing audio data", 400

    # Retrieve the brain instance from the cache using the session ID
    session_id = session.get("session_id")
    if not session_id:
        return "Session ID not found. Upload a file first.", 400

    brain = brains.get(session_id)
    if not brain:
        return "Brain instance not found in dict. Upload a file first.", 400

    print("Brain instance loaded from cache.")

    print("Speech to text...")
    audio_file = request.files["audio_data"]
    transcript = transcribe_audio_file(audio_file)
    print("Transcript result: ", transcript)

    print("Getting response...")
    quivr_response = await to_thread(run_in_event_loop, brain.ask, transcript)

    print("Text to speech...")
    audio_base64 = synthesize_speech(quivr_response.answer)

    print("Done")
    return jsonify({"audio_base64": audio_base64})


def transcribe_audio_file(audio_file):
    with NamedTemporaryFile(suffix=".webm", delete=False) as temp_audio_file:
        audio_file.save(temp_audio_file)
        temp_audio_file_path = temp_audio_file.name

    try:
        with open(temp_audio_file_path, "rb") as f:
            transcript_response = openai.audio.transcriptions.create(
                model="whisper-1", file=f
            )
        transcript = transcript_response.text
    finally:
        os.unlink(temp_audio_file_path)

    return transcript


def synthesize_speech(text):
    speech_response = openai.audio.speech.create(
        model="tts-1", voice="nova", input=text
    )
    audio_content = speech_response.content
    audio_base64 = base64.b64encode(audio_content).decode("utf-8")
    return audio_base64


if __name__ == "__main__":
    app.run(debug=True)
```

## File: `examples/quivr-whisper/pyproject.toml`
```
[project]
name = "quivr-whisper"
version = "0.1.0"
description = "Add your description here"
authors = [
    { name = "Stan Girard", email = "stan@quivr.app" }
]
dependencies = [
    "quivr-core @ file:///${PROJECT_ROOT}/../../core",
    "flask[async]>=3.1.0",
    "openai>=1.54.5",
    "flask-caching>=2.3.0",
]
readme = "README.md"
requires-python = ">= 3.11"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.rye]
managed = true
virtual = true
dev-dependencies = []

[tool.hatch.metadata]
allow-direct-references = true

[tool.hatch.build.targets.wheel]
packages = ["src/quivr_whisper"]
```

## File: `examples/quivr-whisper/requirements-dev.lock`
```
# generated by rye
# use `rye lock` or `rye sync` to update this lockfile
#
# last locked with the following flags:
#   pre: false
#   features: []
#   all-features: false
#   with-sources: false
#   generate-hashes: false
#   universal: false

aiofiles==24.1.0
    # via quivr-core
aiohappyeyeballs==2.4.3
    # via aiohttp
aiohttp==3.11.6
    # via langchain
    # via langchain-community
aiosignal==1.3.1
    # via aiohttp
annotated-types==0.7.0
    # via pydantic
anthropic==0.39.0
    # via langchain-anthropic
anyio==4.6.2.post1
    # via anthropic
    # via httpx
    # via openai
asgiref==3.8.1
    # via flask
attrs==24.2.0
    # via aiohttp
blinker==1.9.0
    # via flask
cachelib==0.9.0
    # via flask-caching
certifi==2024.8.30
    # via httpcore
    # via httpx
    # via requests
charset-normalizer==3.4.0
    # via requests
click==8.1.7
    # via flask
cohere==5.11.4
    # via langchain-cohere
dataclasses-json==0.6.7
    # via langchain-community
defusedxml==0.7.1
    # via langchain-anthropic
distro==1.9.0
    # via anthropic
    # via openai
faiss-cpu==1.9.0.post1
    # via quivr-core
fastavro==1.9.7
    # via cohere
filelock==3.16.1
    # via huggingface-hub
    # via transformers
flask==3.1.0
    # via flask-caching
flask-caching==2.3.0
frozenlist==1.5.0
    # via aiohttp
    # via aiosignal
fsspec==2024.10.0
    # via huggingface-hub
h11==0.14.0
    # via httpcore
httpcore==1.0.7
    # via httpx
httpx==0.27.2
    # via anthropic
    # via cohere
    # via langchain-mistralai
    # via langgraph-sdk
    # via langsmith
    # via megaparse-sdk
    # via openai
    # via quivr-core
httpx-sse==0.4.0
    # via cohere
    # via langchain-community
    # via langchain-mistralai
huggingface-hub==0.26.2
    # via tokenizers
    # via transformers
idna==3.10
    # via anyio
    # via httpx
    # via requests
    # via yarl
itsdangerous==2.2.0
    # via flask
jinja2==3.1.4
    # via flask
jiter==0.7.1
    # via anthropic
    # via openai
jsonpatch==1.33
    # via langchain-core
jsonpointer==3.0.0
    # via jsonpatch
langchain==0.3.9
    # via langchain-community
    # via quivr-core
langchain-anthropic==0.3.0
    # via quivr-core
langchain-cohere==0.3.3
    # via quivr-core
langchain-community==0.3.9
    # via langchain-experimental
    # via quivr-core
langchain-core==0.3.21
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-community
    # via langchain-experimental
    # via langchain-mistralai
    # via langchain-openai
    # via langchain-text-splitters
    # via langgraph
    # via langgraph-checkpoint
    # via quivr-core
langchain-experimental==0.3.3
    # via langchain-cohere
langchain-mistralai==0.2.3
    # via quivr-core
langchain-openai==0.2.11
    # via quivr-core
langchain-text-splitters==0.3.2
    # via langchain
langgraph==0.2.56
    # via quivr-core
langgraph-checkpoint==2.0.9
    # via langgraph
langgraph-sdk==0.1.46
    # via langgraph
langsmith==0.1.143
    # via langchain
    # via langchain-community
    # via langchain-core
loguru==0.7.2
    # via megaparse-sdk
markdown-it-py==3.0.0
    # via rich
markupsafe==3.0.2
    # via jinja2
    # via quivr-core
    # via werkzeug
marshmallow==3.23.1
    # via dataclasses-json
mdurl==0.1.2
    # via markdown-it-py
megaparse-sdk==0.1.10
    # via quivr-core
msgpack==1.1.0
    # via langgraph-checkpoint
multidict==6.1.0
    # via aiohttp
    # via yarl
mypy-extensions==1.0.0
    # via typing-inspect
nats-py==2.9.0
    # via megaparse-sdk
numpy==1.26.4
    # via faiss-cpu
    # via langchain
    # via langchain-community
    # via pandas
    # via transformers
openai==1.54.5
    # via langchain-openai
orjson==3.10.11
    # via langgraph-sdk
    # via langsmith
packaging==24.2
    # via faiss-cpu
    # via huggingface-hub
    # via langchain-core
    # via marshmallow
    # via transformers
pandas==2.2.3
    # via langchain-cohere
parameterized==0.9.0
    # via cohere
propcache==0.2.0
    # via aiohttp
    # via yarl
protobuf==5.28.3
    # via transformers
psutil==6.1.0
    # via megaparse-sdk
pycryptodome==3.21.0
    # via megaparse-sdk
pydantic==2.9.2
    # via anthropic
    # via cohere
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-core
    # via langchain-mistralai
    # via langsmith
    # via openai
    # via pydantic-settings
    # via quivr-core
pydantic-core==2.23.4
    # via cohere
    # via pydantic
pydantic-settings==2.6.1
    # via langchain-community
pygments==2.18.0
    # via rich
python-dateutil==2.8.2
    # via pandas
python-dotenv==1.0.1
    # via megaparse-sdk
    # via pydantic-settings
pytz==2024.2
    # via pandas
pyyaml==6.0.2
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langchain-core
    # via transformers
quivr-core @ file:///${PROJECT_ROOT}/../../core
rapidfuzz==3.10.1
    # via quivr-core
regex==2024.11.6
    # via tiktoken
    # via transformers
requests==2.32.3
    # via cohere
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langsmith
    # via requests-toolbelt
    # via tiktoken
    # via transformers
requests-toolbelt==1.0.0
    # via langsmith
rich==13.9.4
    # via quivr-core
safetensors==0.4.5
    # via transformers
sentencepiece==0.2.0
    # via transformers
six==1.16.0
    # via python-dateutil
sniffio==1.3.1
    # via anthropic
    # via anyio
    # via httpx
    # via openai
sqlalchemy==2.0.36
    # via langchain
    # via langchain-community
tabulate==0.9.0
    # via langchain-cohere
tenacity==8.5.0
    # via langchain
    # via langchain-community
    # via langchain-core
tiktoken==0.8.0
    # via langchain-openai
    # via quivr-core
tokenizers==0.20.3
    # via cohere
    # via langchain-mistralai
    # via transformers
tqdm==4.67.0
    # via huggingface-hub
    # via openai
    # via transformers
transformers==4.46.3
    # via quivr-core
types-pyyaml==6.0.12.20240917
    # via quivr-core
types-requests==2.32.0.20241016
    # via cohere
typing-extensions==4.12.2
    # via anthropic
    # via cohere
    # via huggingface-hub
    # via langchain-core
    # via openai
    # via pydantic
    # via pydantic-core
    # via sqlalchemy
    # via typing-inspect
typing-inspect==0.9.0
    # via dataclasses-json
tzdata==2024.2
    # via pandas
urllib3==2.2.3
    # via requests
    # via types-requests
werkzeug==3.1.3
    # via flask
yarl==1.17.2
    # via aiohttp
```

## File: `examples/quivr-whisper/requirements.lock`
```
# generated by rye
# use `rye lock` or `rye sync` to update this lockfile
#
# last locked with the following flags:
#   pre: false
#   features: []
#   all-features: false
#   with-sources: false
#   generate-hashes: false
#   universal: false

aiofiles==24.1.0
    # via quivr-core
aiohappyeyeballs==2.4.3
    # via aiohttp
aiohttp==3.11.6
    # via langchain
    # via langchain-community
aiosignal==1.3.1
    # via aiohttp
annotated-types==0.7.0
    # via pydantic
anthropic==0.39.0
    # via langchain-anthropic
anyio==4.6.2.post1
    # via anthropic
    # via httpx
    # via openai
asgiref==3.8.1
    # via flask
attrs==24.2.0
    # via aiohttp
blinker==1.9.0
    # via flask
cachelib==0.9.0
    # via flask-caching
certifi==2024.8.30
    # via httpcore
    # via httpx
    # via requests
charset-normalizer==3.4.0
    # via requests
click==8.1.7
    # via flask
cohere==5.11.4
    # via langchain-cohere
dataclasses-json==0.6.7
    # via langchain-community
defusedxml==0.7.1
    # via langchain-anthropic
distro==1.9.0
    # via anthropic
    # via openai
faiss-cpu==1.9.0.post1
    # via quivr-core
fastavro==1.9.7
    # via cohere
filelock==3.16.1
    # via huggingface-hub
    # via transformers
flask==3.1.0
    # via flask-caching
flask-caching==2.3.0
frozenlist==1.5.0
    # via aiohttp
    # via aiosignal
fsspec==2024.10.0
    # via huggingface-hub
h11==0.14.0
    # via httpcore
httpcore==1.0.7
    # via httpx
httpx==0.27.2
    # via anthropic
    # via cohere
    # via langchain-mistralai
    # via langgraph-sdk
    # via langsmith
    # via megaparse-sdk
    # via openai
    # via quivr-core
httpx-sse==0.4.0
    # via cohere
    # via langchain-community
    # via langchain-mistralai
huggingface-hub==0.26.2
    # via tokenizers
    # via transformers
idna==3.10
    # via anyio
    # via httpx
    # via requests
    # via yarl
itsdangerous==2.2.0
    # via flask
jinja2==3.1.4
    # via flask
jiter==0.7.1
    # via anthropic
    # via openai
jsonpatch==1.33
    # via langchain-core
jsonpointer==3.0.0
    # via jsonpatch
langchain==0.3.9
    # via langchain-community
    # via quivr-core
langchain-anthropic==0.3.0
    # via quivr-core
langchain-cohere==0.3.3
    # via quivr-core
langchain-community==0.3.9
    # via langchain-experimental
    # via quivr-core
langchain-core==0.3.21
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-community
    # via langchain-experimental
    # via langchain-mistralai
    # via langchain-openai
    # via langchain-text-splitters
    # via langgraph
    # via langgraph-checkpoint
    # via quivr-core
langchain-experimental==0.3.3
    # via langchain-cohere
langchain-mistralai==0.2.3
    # via quivr-core
langchain-openai==0.2.11
    # via quivr-core
langchain-text-splitters==0.3.2
    # via langchain
langgraph==0.2.56
    # via quivr-core
langgraph-checkpoint==2.0.9
    # via langgraph
langgraph-sdk==0.1.46
    # via langgraph
langsmith==0.1.143
    # via langchain
    # via langchain-community
    # via langchain-core
loguru==0.7.2
    # via megaparse-sdk
markdown-it-py==3.0.0
    # via rich
markupsafe==3.0.2
    # via jinja2
    # via quivr-core
    # via werkzeug
marshmallow==3.23.1
    # via dataclasses-json
mdurl==0.1.2
    # via markdown-it-py
megaparse-sdk==0.1.10
    # via quivr-core
msgpack==1.1.0
    # via langgraph-checkpoint
multidict==6.1.0
    # via aiohttp
    # via yarl
mypy-extensions==1.0.0
    # via typing-inspect
nats-py==2.9.0
    # via megaparse-sdk
numpy==1.26.4
    # via faiss-cpu
    # via langchain
    # via langchain-community
    # via pandas
    # via transformers
openai==1.54.5
    # via langchain-openai
orjson==3.10.11
    # via langgraph-sdk
    # via langsmith
packaging==24.2
    # via faiss-cpu
    # via huggingface-hub
    # via langchain-core
    # via marshmallow
    # via transformers
pandas==2.2.3
    # via langchain-cohere
parameterized==0.9.0
    # via cohere
propcache==0.2.0
    # via aiohttp
    # via yarl
protobuf==5.28.3
    # via transformers
psutil==6.1.0
    # via megaparse-sdk
pycryptodome==3.21.0
    # via megaparse-sdk
pydantic==2.9.2
    # via anthropic
    # via cohere
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-core
    # via langchain-mistralai
    # via langsmith
    # via openai
    # via pydantic-settings
    # via quivr-core
pydantic-core==2.23.4
    # via cohere
    # via pydantic
pydantic-settings==2.6.1
    # via langchain-community
pygments==2.18.0
    # via rich
python-dateutil==2.8.2
    # via pandas
python-dotenv==1.0.1
    # via megaparse-sdk
    # via pydantic-settings
pytz==2024.2
    # via pandas
pyyaml==6.0.2
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langchain-core
    # via transformers
quivr-core @ file:///${PROJECT_ROOT}/../../core
rapidfuzz==3.10.1
    # via quivr-core
regex==2024.11.6
    # via tiktoken
    # via transformers
requests==2.32.3
    # via cohere
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langsmith
    # via requests-toolbelt
    # via tiktoken
    # via transformers
requests-toolbelt==1.0.0
    # via langsmith
rich==13.9.4
    # via quivr-core
safetensors==0.4.5
    # via transformers
sentencepiece==0.2.0
    # via transformers
six==1.16.0
    # via python-dateutil
sniffio==1.3.1
    # via anthropic
    # via anyio
    # via httpx
    # via openai
sqlalchemy==2.0.36
    # via langchain
    # via langchain-community
tabulate==0.9.0
    # via langchain-cohere
tenacity==8.5.0
    # via langchain
    # via langchain-community
    # via langchain-core
tiktoken==0.8.0
    # via langchain-openai
    # via quivr-core
tokenizers==0.20.3
    # via cohere
    # via langchain-mistralai
    # via transformers
tqdm==4.67.0
    # via huggingface-hub
    # via openai
    # via transformers
transformers==4.46.3
    # via quivr-core
types-pyyaml==6.0.12.20240917
    # via quivr-core
types-requests==2.32.0.20241016
    # via cohere
typing-extensions==4.12.2
    # via anthropic
    # via cohere
    # via huggingface-hub
    # via langchain-core
    # via openai
    # via pydantic
    # via pydantic-core
    # via sqlalchemy
    # via typing-inspect
typing-inspect==0.9.0
    # via dataclasses-json
tzdata==2024.2
    # via pandas
urllib3==2.2.3
    # via requests
    # via types-requests
werkzeug==3.1.3
    # via flask
yarl==1.17.2
    # via aiohttp
```

## File: `examples/quivr-whisper/static/app.js`
```javascript
// DOM Elements
const recordBtn = document.getElementById("record-btn");
const fileInput = document.getElementById("fileInput");
const fileInputContainer = document.querySelector(".custom-file-input");
const fileName = document.getElementById("fileName");

const audioVisualizer = document.getElementById("audio-visualizer");
const audioPlayback = document.getElementById("audio-playback");
const canvasCtx = audioVisualizer.getContext("2d");

window.addEventListener("load", () => {
  audioVisualizer.width = window.innerWidth;
  audioVisualizer.height = window.innerHeight;
});

window.addEventListener("resize", (e) => {
  audioVisualizer.width = window.innerWidth;
  audioVisualizer.height = window.innerHeight;
});

fileInput.addEventListener("change", () => {
  fileName.textContent =
    fileInput.files.length > 0 ? fileInput.files[0].name : "No file chosen";
  fileName.classList.toggle("file-selected", fileInput.files.length > 0);
});

// Configuration
const SILENCE_THRESHOLD = 128; // Adjusted for byte data (128 is middle)
const SILENCE_DURATION = 1500;
const FFT_SIZE = 2048;

// State
const state = {
  isRecording: false,
  isVisualizing: false,
  chunks: [],
  silenceTimer: null,
  lastAudioLevel: 0,
};

// Audio Analysis
class AudioAnalyzer {
  constructor() {
    this.reset();
  }

  reset() {
    this.analyser = null;
    this.dataArray = null;
    this.bufferLength = null;
    this.source = null;
    this.cleanup();
  }

  setup(source, audioContext) {
    this.cleanup();

    this.analyser = this._createAnalyser(audioContext);
    source.connect(this.analyser);

    this._initializeBuffer();
    return this.analyser;
  }

  setupForPlayback(audioElement, audioContext, connectToDestination = true) {
    // Reuse existing MediaElementSourceNode if it already exists for this audio element
    if (!this.source || this.source.mediaElement !== audioElement) {
      this.cleanup(); // Ensure any previous connections are cleaned up
      this.source = audioContext.createMediaElementSource(audioElement);
    }

    this.analyser = this._createAnalyser(audioContext);

    this.source.connect(this.analyser);

    if (connectToDestination) {
      this.analyser.connect(audioContext.destination);
    }

    this._initializeBuffer();
    return this.analyser;
  }

  cleanup() {
    if (this.source) {
      this._safeDisconnect(this.source);
    }
    if (this.analyser) {
      this._safeDisconnect(this.analyser);
    }
  }

  _createAnalyser(audioContext) {
    const analyser = audioContext.createAnalyser();
    analyser.fftSize = FFT_SIZE;
    return analyser;
  }

  _initializeBuffer() {
    this.bufferLength = this.analyser.frequencyBinCount;
    this.dataArray = new Uint8Array(this.bufferLength);
  }

  _safeDisconnect(node) {
    if (node) {
      try {
        node.disconnect();
      } catch {
        // Ignore disconnect errors
      }
    }
  }
}

// Visualization
class Visualizer {
  constructor(canvas, analyzer) {
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.analyzer = analyzer;
  }

  draw(currentAnalyser, onSilence) {
    if (!currentAnalyser || this.analyzer.dataArray === null) return;

    requestAnimationFrame(() => this.draw(currentAnalyser, onSilence));

    // Use getByteTimeDomainData instead of getFloatTimeDomainData
    currentAnalyser.getByteTimeDomainData(this.analyzer.dataArray);

    // Clear canvas
    this.ctx.fillStyle = "#252525";
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    if (!state.isVisualizing) return;

    this.ctx.lineWidth = 2;
    this.ctx.strokeStyle = "#6142d4";
    this.ctx.beginPath();

    const sliceWidth = (this.canvas.width * 1) / this.analyzer.bufferLength;
    let x = 0;
    let sum = 0;

    // Draw waveform
    for (let i = 0; i < this.analyzer.bufferLength; i++) {
      // Scale byte data (0-255) to canvas height
      const v = this.analyzer.dataArray[i] / 128.0; // normalize to 0-2
      const y = (v - 1) * (this.canvas.height / 2) + this.canvas.height / 2;

      sum += Math.abs(v - 1); // Calculate distance from center (128)

      if (i === 0) {
        this.ctx.moveTo(x, y);
      } else {
        this.ctx.lineTo(x, y);
      }

      x += sliceWidth;
    }

    this.ctx.lineTo(this.canvas.width, this.canvas.height / 2);
    this.ctx.stroke();

    // Check for silence during recording with adjusted thresholds for byte data
    if (state.isRecording) {
      const averageAmplitude = sum / this.analyzer.bufferLength;
      if (averageAmplitude < 0.1) {
        // Adjusted threshold for normalized data
        // Reset silence timer if we detect sound
        if (averageAmplitude > 0.05) {
          clearTimeout(state.silenceTimer);
          state.silenceTimer = null;
        } else {
          onSilence();
        }
      }
    }
  }
}

// Recording Handler
class RecordingHandler {
  constructor() {
    this.mediaRecorder = null;
    this.audioAnalyzer = new AudioAnalyzer();
    this.visualizer = new Visualizer(audioVisualizer, this.audioAnalyzer);
    this.audioContext = null;
  }

  async initialize() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      this.mediaRecorder = new MediaRecorder(stream);
      this.setupRecordingEvents();
      if (!this.audioContext)
        this.audioContext = new (window.AudioContext ||
          window.webkitAudioContext)();
    } catch (err) {
      console.error(`Media device error: ${err}`);
    }
  }

  setupRecordingEvents() {
    this.mediaRecorder.ondataavailable = (e) => {
      state.chunks.push(e.data);
    };

    this.mediaRecorder.onstop = async () => {
      await this.handleRecordingStop();
    };
  }

  startRecording() {
    state.isVisualizing = true;
    state.chunks = [];
    state.isRecording = true;
    this.mediaRecorder.start();

    const source = this.audioContext.createMediaStreamSource(
      this.mediaRecorder.stream
    );

    const analyser = this.audioAnalyzer.setup(source, this.audioContext);
    audioVisualizer.classList.remove("hidden");

    this.visualizer.draw(analyser, () => {
      if (!state.silenceTimer) {
        state.silenceTimer = setTimeout(
          () => this.stopRecording(),
          SILENCE_DURATION
        );
      }
    });

    recordBtn.dataset.recording = true;
    recordBtn.classList.add("processing");
  }

  stopRecording() {
    if (state.isRecording) {
      state.isVisualizing = false;
      state.isRecording = false;
      this.mediaRecorder.stop();
      clearTimeout(state.silenceTimer);
      state.silenceTimer = null;
      recordBtn.dataset.recording = false;
    }
  }

  async handleRecordingStop() {
    console.log("Processing recording...");
    recordBtn.dataset.pending = true;
    recordBtn.disabled = true;

    const audioBlob = new Blob(state.chunks, { type: "audio/wav" });
    if (!fileInput.files.length) {
      recordBtn.dataset.pending = false;
      recordBtn.disabled = false;
      alert("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append("audio_data", audioBlob);
    formData.append("file", fileInput.files[0]);

    try {
      await this.processRecording(formData);
    } catch (error) {
      console.error("Processing error:", error);
    } finally {
      this.audioAnalyzer.cleanup();
    }
  }

  async processRecording(formData) {
    const response = await fetch("/ask", {
      method: "POST",
      body: formData,
    });
    const data = await response.json();

    await this.handleResponse(data);
  }

  async handleResponse(data) {
    audioPlayback.src = "data:audio/wav;base64," + data.audio_base64;

    audioPlayback.onloadedmetadata = () => {
      const analyser = this.audioAnalyzer.setupForPlayback(
        audioPlayback,
        this.audioContext
      );
      audioVisualizer.classList.remove("hidden");

      this.visualizer.draw(analyser, () => {});
      audioPlayback.play();
      state.isVisualizing = true;
    };

    audioPlayback.onended = () => {
      this.audioAnalyzer.cleanup();
      recordBtn.dataset.pending = false;
      recordBtn.disabled = false;
      state.isVisualizing = false;
    };
  }
}

const uploadFile = async (e) => {
  uploadBtn.innerText = "Uploading File...";
  e.preventDefault();
  const file = fileInput.files[0];

  if (!file) {
    alert("Please select a file.");
    return;
  }
  const formData = new FormData();
  formData.append("file", file);
  try {
    await fetch("/upload", {
      method: "POST",
      body: formData,
    });
    recordBtn.classList.remove("hidden");
    fileInputContainer.classList.add("hidden");
  } catch (error) {
    recordBtn.classList.add("hidden");
    fileInputContainer.classList.remove("hidden");
    console.error("Error uploading file:", error);
    uploadBtn.innerText = "Upload Failed. Try again";
  }
};

const uploadBtn = document.getElementById("upload-btn");
uploadBtn.addEventListener("click", uploadFile);

// Main initialization
async function initializeApp() {
  if (!navigator.mediaDevices) {
    console.error("Media devices not supported");
    return;
  }

  const recorder = new RecordingHandler();
  await recorder.initialize();

  recordBtn.onclick = () => {
    if (recorder.mediaRecorder.state === "inactive") {
      recorder.startRecording();
    } else if (recorder.mediaRecorder.state === "recording") {
      recorder.stopRecording();
    }
  };
}

// Start the application
initializeApp();
```

## File: `examples/quivr-whisper/static/styles.css`
```css
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}


body {
    color: #f4f4f4;
    background-color: #252525;
    display: flex;
    gap: 1rem;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    min-height: 100vh;
}

.primary {
    background-color: #6142d4;
}

button {
    background-color: #6142d4;
    border: none;
    padding: .75rem 2rem;
    border-radius: 0.5rem;
    color: #f4f4f4;
    cursor: pointer;
}

canvas {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background-color: #252525;
    z-index: -1;
}

.record-btn {
    background-color: #f5f5f5;
    border: none;
    outline: none;
    width: 256px;
    height: 256px;
    background-repeat: no-repeat;
    background-position: center;
    border-radius: 50%;
    background-size: 50%;
    transition: background-color 200ms ease-in, transform 200ms ease-out;
}

.record-btn:hover {
    background-color: #fff;
    transform: scale(1.025);
}

.record-btn:active {
    background-color: #e2e2e2;
    transform: scale(0.975);
}

.record-btn[data-recording="true"] {
    background-image: url("./mic.svg");
}

.record-btn[data-recording="false"] {
    background-image: url("./mic-off.svg");
}

.record-btn[data-pending="true"] {
    background-image: url("./loader.svg") !important;
    animation: spin 1s linear infinite;
}

.hidden {
    display: none !important;
    visibility: hidden;
}

.custom-file-input {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.custom-file-input input[type="file"] {
  display: none;
}

.custom-file-input label {
  border: solid 2px #6142d4;
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  font-weight: bold;
  transition: background-color 0.3s;
}

.custom-file-input label:hover {
  background-color: #6142d4;
}

.custom-file-input span {
  font-size: 14px;
  color: #f4f4f4;
}

/* Adjust appearance when a file is selected */
.custom-file-input span.file-selected {
  color: #ffffff;
  font-weight: bold;
}

/* 
# Override default MUI light theme. (Check theme.ts)
[UI.theme.light]
    background = "#fcfcfc"
    paper = "#f8f8f8"

    [UI.theme.light.primary]
        main = "#6142d4"
        dark = "#6e53cf"
        light = "#6e53cf30"
    [UI.theme.light.text]
        primary = "#1f1f1f"
        secondary = "#818080"

# Override default MUI dark theme. (Check theme.ts)
[UI.theme.dark]
    background = "#252525"
    paper = "#1f1f1f"

    [UI.theme.dark.primary]
        main = "#6142d4"
        dark = "#6e53cf"
        light = "#6e53cf30"
    [UI.theme.dark.text]
        primary = "#f4f4f4"
        secondary = "#c8c8c8"

*/

.loader {
    border: 4px solid #f3f3f3;
    border-radius: 50%;
    border-top: 4px solid #3498db;
    width: 50px;
    height: 50px;
    -webkit-animation: spin 2s linear infinite;
    animation: spin 2s linear infinite;
    position: absolute;
    /* Center the loader in the viewport */
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: none;
    /* Hide it by default */
}

@-webkit-keyframes spin {
    0% {
        -webkit-transform: rotate(0deg);
    }

    100% {
        -webkit-transform: rotate(360deg);
    }
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}
```

## File: `examples/quivr-whisper/templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Audio Interaction WebApp</title>
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='styles.css') }}"
    />
  </head>

  <body>
    <button
      type="button"
      id="record-btn"
      class="record-btn hidden"
      data-recording="false"
      data-pending="false"
    ></button>
    <div class="custom-file-input">
      <label for="fileInput">Choose a file</label>
      <input
        type="file"
        accept="text/plain"
        name="fileInput"
        required
        id="fileInput"
      />
      <span id="fileName">No file chosen</span>
      <button id="upload-btn" class="upload-btn">Upload</button>
    </div>
    <canvas id="audio-visualizer" class=""></canvas>
    <audio id="audio-playback" controls class="hidden"></audio>
    <script src="{{ url_for('static', filename='app.js') }}"></script>
  </body>
</html>
```

## File: `examples/simple_question/.gitignore`
```
# python generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# venv
.venv
```

## File: `examples/simple_question/.python-version`
```
3.11.9
```

## File: `examples/simple_question/README.md`
```markdown
# simple-question

Describe your project here.
```

## File: `examples/simple_question/pyproject.toml`
```
[project]
name = "simple-question"
version = "0.1.0"
description = "Add your description here"
authors = [
    { name = "Stan Girard", email = "stan@quivr.app" }
]
dependencies = [
    "quivr-core @ file:///${PROJECT_ROOT}/../../core",
    "python-dotenv>=1.0.1",
]
readme = "README.md"
requires-python = ">= 3.11"

[tool.rye]
managed = true
virtual = true
dev-dependencies = []
```

## File: `examples/simple_question/requirements-dev.lock`
```
# generated by rye
# use `rye lock` or `rye sync` to update this lockfile
#
# last locked with the following flags:
#   pre: false
#   features: []
#   all-features: false
#   with-sources: false
#   generate-hashes: false
#   universal: false

aiofiles==24.1.0
    # via quivr-core
aiohappyeyeballs==2.4.3
    # via aiohttp
aiohttp==3.10.10
    # via langchain
    # via langchain-community
aiosignal==1.3.1
    # via aiohttp
annotated-types==0.7.0
    # via pydantic
anthropic==0.40.0
    # via langchain-anthropic
anyio==4.6.2.post1
    # via anthropic
    # via httpx
    # via openai
attrs==24.2.0
    # via aiohttp
certifi==2024.8.30
    # via httpcore
    # via httpx
    # via requests
charset-normalizer==3.4.0
    # via requests
cohere==5.11.1
    # via langchain-cohere
dataclasses-json==0.6.7
    # via langchain-community
defusedxml==0.7.1
    # via langchain-anthropic
distro==1.9.0
    # via anthropic
    # via openai
faiss-cpu==1.9.0
    # via quivr-core
fastavro==1.9.7
    # via cohere
filelock==3.16.1
    # via huggingface-hub
    # via transformers
frozenlist==1.4.1
    # via aiohttp
    # via aiosignal
fsspec==2024.10.0
    # via huggingface-hub
h11==0.14.0
    # via httpcore
httpcore==1.0.6
    # via httpx
httpx==0.27.2
    # via anthropic
    # via cohere
    # via langchain-mistralai
    # via langgraph-sdk
    # via langsmith
    # via megaparse-sdk
    # via openai
    # via quivr-core
httpx-sse==0.4.0
    # via cohere
    # via langchain-community
    # via langchain-mistralai
    # via langgraph-sdk
huggingface-hub==0.26.1
    # via tokenizers
    # via transformers
idna==3.10
    # via anyio
    # via httpx
    # via requests
    # via yarl
jiter==0.6.1
    # via anthropic
    # via openai
jsonpatch==1.33
    # via langchain-core
jsonpointer==3.0.0
    # via jsonpatch
langchain==0.3.9
    # via langchain-community
    # via quivr-core
langchain-anthropic==0.3.0
    # via quivr-core
langchain-cohere==0.3.3
    # via quivr-core
langchain-community==0.3.9
    # via langchain-experimental
    # via quivr-core
langchain-core==0.3.21
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-community
    # via langchain-experimental
    # via langchain-mistralai
    # via langchain-openai
    # via langchain-text-splitters
    # via langgraph
    # via langgraph-checkpoint
    # via quivr-core
langchain-experimental==0.3.3
    # via langchain-cohere
langchain-mistralai==0.2.3
    # via quivr-core
langchain-openai==0.2.11
    # via quivr-core
langchain-text-splitters==0.3.2
    # via langchain
langgraph==0.2.39
    # via quivr-core
langgraph-checkpoint==2.0.1
    # via langgraph
langgraph-sdk==0.1.33
    # via langgraph
langsmith==0.1.136
    # via langchain
    # via langchain-community
    # via langchain-core
loguru==0.7.2
    # via megaparse-sdk
markdown-it-py==3.0.0
    # via rich
markupsafe==3.0.2
    # via quivr-core
marshmallow==3.23.0
    # via dataclasses-json
mdurl==0.1.2
    # via markdown-it-py
megaparse-sdk==0.1.10
    # via quivr-core
msgpack==1.1.0
    # via langgraph-checkpoint
multidict==6.1.0
    # via aiohttp
    # via yarl
mypy-extensions==1.0.0
    # via typing-inspect
nats-py==2.9.0
    # via megaparse-sdk
numpy==1.26.4
    # via faiss-cpu
    # via langchain
    # via langchain-community
    # via pandas
    # via transformers
openai==1.56.2
    # via langchain-openai
orjson==3.10.9
    # via langgraph-sdk
    # via langsmith
packaging==24.1
    # via faiss-cpu
    # via huggingface-hub
    # via langchain-core
    # via marshmallow
    # via transformers
pandas==2.2.3
    # via langchain-cohere
parameterized==0.9.0
    # via cohere
propcache==0.2.0
    # via yarl
protobuf==5.28.2
    # via transformers
psutil==6.1.0
    # via megaparse-sdk
pycryptodome==3.21.0
    # via megaparse-sdk
pydantic==2.9.2
    # via anthropic
    # via cohere
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-core
    # via langchain-mistralai
    # via langsmith
    # via openai
    # via pydantic-settings
    # via quivr-core
pydantic-core==2.23.4
    # via cohere
    # via pydantic
pydantic-settings==2.6.1
    # via langchain-community
pygments==2.18.0
    # via rich
python-dateutil==2.9.0.post0
    # via pandas
python-dotenv==1.0.1
    # via megaparse-sdk
    # via pydantic-settings
pytz==2024.2
    # via pandas
pyyaml==6.0.2
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langchain-core
    # via transformers
quivr-core @ file:///${PROJECT_ROOT}/../../core
rapidfuzz==3.10.1
    # via quivr-core
regex==2024.9.11
    # via tiktoken
    # via transformers
requests==2.32.3
    # via cohere
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langsmith
    # via requests-toolbelt
    # via tiktoken
    # via transformers
requests-toolbelt==1.0.0
    # via langsmith
rich==13.9.2
    # via quivr-core
safetensors==0.4.5
    # via transformers
sentencepiece==0.2.0
    # via transformers
six==1.16.0
    # via python-dateutil
sniffio==1.3.1
    # via anthropic
    # via anyio
    # via httpx
    # via openai
sqlalchemy==2.0.36
    # via langchain
    # via langchain-community
tabulate==0.9.0
    # via langchain-cohere
tenacity==8.5.0
    # via langchain
    # via langchain-community
    # via langchain-core
tiktoken==0.8.0
    # via langchain-openai
    # via quivr-core
tokenizers==0.20.1
    # via cohere
    # via langchain-mistralai
    # via transformers
tqdm==4.66.5
    # via huggingface-hub
    # via openai
    # via transformers
transformers==4.45.2
    # via quivr-core
types-pyyaml==6.0.12.20240917
    # via quivr-core
types-requests==2.32.0.20241016
    # via cohere
typing-extensions==4.12.2
    # via anthropic
    # via cohere
    # via huggingface-hub
    # via langchain-core
    # via openai
    # via pydantic
    # via pydantic-core
    # via sqlalchemy
    # via typing-inspect
typing-inspect==0.9.0
    # via dataclasses-json
tzdata==2024.2
    # via pandas
urllib3==2.2.3
    # via requests
    # via types-requests
yarl==1.15.5
    # via aiohttp
```

## File: `examples/simple_question/requirements.lock`
```
# generated by rye
# use `rye lock` or `rye sync` to update this lockfile
#
# last locked with the following flags:
#   pre: false
#   features: []
#   all-features: false
#   with-sources: false
#   generate-hashes: false
#   universal: false

aiofiles==24.1.0
    # via quivr-core
aiohappyeyeballs==2.4.3
    # via aiohttp
aiohttp==3.10.10
    # via langchain
    # via langchain-community
aiosignal==1.3.1
    # via aiohttp
annotated-types==0.7.0
    # via pydantic
anthropic==0.40.0
    # via langchain-anthropic
anyio==4.6.2.post1
    # via anthropic
    # via httpx
    # via openai
attrs==24.2.0
    # via aiohttp
certifi==2024.8.30
    # via httpcore
    # via httpx
    # via requests
charset-normalizer==3.4.0
    # via requests
cohere==5.11.1
    # via langchain-cohere
dataclasses-json==0.6.7
    # via langchain-community
defusedxml==0.7.1
    # via langchain-anthropic
distro==1.9.0
    # via anthropic
    # via openai
faiss-cpu==1.9.0
    # via quivr-core
fastavro==1.9.7
    # via cohere
filelock==3.16.1
    # via huggingface-hub
    # via transformers
frozenlist==1.4.1
    # via aiohttp
    # via aiosignal
fsspec==2024.10.0
    # via huggingface-hub
h11==0.14.0
    # via httpcore
httpcore==1.0.6
    # via httpx
httpx==0.27.2
    # via anthropic
    # via cohere
    # via langchain-mistralai
    # via langgraph-sdk
    # via langsmith
    # via megaparse-sdk
    # via openai
    # via quivr-core
httpx-sse==0.4.0
    # via cohere
    # via langchain-community
    # via langchain-mistralai
    # via langgraph-sdk
huggingface-hub==0.26.1
    # via tokenizers
    # via transformers
idna==3.10
    # via anyio
    # via httpx
    # via requests
    # via yarl
jiter==0.6.1
    # via anthropic
    # via openai
jsonpatch==1.33
    # via langchain-core
jsonpointer==3.0.0
    # via jsonpatch
langchain==0.3.9
    # via langchain-community
    # via quivr-core
langchain-anthropic==0.3.0
    # via quivr-core
langchain-cohere==0.3.3
    # via quivr-core
langchain-community==0.3.9
    # via langchain-experimental
    # via quivr-core
langchain-core==0.3.21
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-community
    # via langchain-experimental
    # via langchain-mistralai
    # via langchain-openai
    # via langchain-text-splitters
    # via langgraph
    # via langgraph-checkpoint
    # via quivr-core
langchain-experimental==0.3.3
    # via langchain-cohere
langchain-mistralai==0.2.3
    # via quivr-core
langchain-openai==0.2.11
    # via quivr-core
langchain-text-splitters==0.3.2
    # via langchain
langgraph==0.2.39
    # via quivr-core
langgraph-checkpoint==2.0.1
    # via langgraph
langgraph-sdk==0.1.33
    # via langgraph
langsmith==0.1.136
    # via langchain
    # via langchain-community
    # via langchain-core
loguru==0.7.2
    # via megaparse-sdk
markdown-it-py==3.0.0
    # via rich
markupsafe==3.0.2
    # via quivr-core
marshmallow==3.23.0
    # via dataclasses-json
mdurl==0.1.2
    # via markdown-it-py
megaparse-sdk==0.1.10
    # via quivr-core
msgpack==1.1.0
    # via langgraph-checkpoint
multidict==6.1.0
    # via aiohttp
    # via yarl
mypy-extensions==1.0.0
    # via typing-inspect
nats-py==2.9.0
    # via megaparse-sdk
numpy==1.26.4
    # via faiss-cpu
    # via langchain
    # via langchain-community
    # via pandas
    # via transformers
openai==1.56.2
    # via langchain-openai
orjson==3.10.9
    # via langgraph-sdk
    # via langsmith
packaging==24.1
    # via faiss-cpu
    # via huggingface-hub
    # via langchain-core
    # via marshmallow
    # via transformers
pandas==2.2.3
    # via langchain-cohere
parameterized==0.9.0
    # via cohere
propcache==0.2.0
    # via yarl
protobuf==5.28.2
    # via transformers
psutil==6.1.0
    # via megaparse-sdk
pycryptodome==3.21.0
    # via megaparse-sdk
pydantic==2.9.2
    # via anthropic
    # via cohere
    # via langchain
    # via langchain-anthropic
    # via langchain-cohere
    # via langchain-core
    # via langchain-mistralai
    # via langsmith
    # via openai
    # via pydantic-settings
    # via quivr-core
pydantic-core==2.23.4
    # via cohere
    # via pydantic
pydantic-settings==2.6.1
    # via langchain-community
pygments==2.18.0
    # via rich
python-dateutil==2.9.0.post0
    # via pandas
python-dotenv==1.0.1
    # via megaparse-sdk
    # via pydantic-settings
pytz==2024.2
    # via pandas
pyyaml==6.0.2
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langchain-core
    # via transformers
quivr-core @ file:///${PROJECT_ROOT}/../../core
rapidfuzz==3.10.1
    # via quivr-core
regex==2024.9.11
    # via tiktoken
    # via transformers
requests==2.32.3
    # via cohere
    # via huggingface-hub
    # via langchain
    # via langchain-community
    # via langsmith
    # via requests-toolbelt
    # via tiktoken
    # via transformers
requests-toolbelt==1.0.0
    # via langsmith
rich==13.9.2
    # via quivr-core
safetensors==0.4.5
    # via transformers
sentencepiece==0.2.0
    # via transformers
six==1.16.0
    # via python-dateutil
sniffio==1.3.1
    # via anthropic
    # via anyio
    # via httpx
    # via openai
sqlalchemy==2.0.36
    # via langchain
    # via langchain-community
tabulate==0.9.0
    # via langchain-cohere
tenacity==8.5.0
    # via langchain
    # via langchain-community
    # via langchain-core
tiktoken==0.8.0
    # via langchain-openai
    # via quivr-core
tokenizers==0.20.1
    # via cohere
    # via langchain-mistralai
    # via transformers
tqdm==4.66.5
    # via huggingface-hub
    # via openai
    # via transformers
transformers==4.45.2
    # via quivr-core
types-pyyaml==6.0.12.20240917
    # via quivr-core
types-requests==2.32.0.20241016
    # via cohere
typing-extensions==4.12.2
    # via anthropic
    # via cohere
    # via huggingface-hub
    # via langchain-core
    # via openai
    # via pydantic
    # via pydantic-core
    # via sqlalchemy
    # via typing-inspect
typing-inspect==0.9.0
    # via dataclasses-json
tzdata==2024.2
    # via pandas
urllib3==2.2.3
    # via requests
    # via types-requests
yarl==1.15.5
    # via aiohttp
```

## File: `examples/simple_question/simple_question.py`
```python
import tempfile

from quivr_core import Brain

import dotenv

dotenv.load_dotenv()

if __name__ == "__main__":
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as temp_file:
        temp_file.write("Gold is a liquid of blue-like colour.")
        temp_file.flush()

        brain = Brain.from_files(
            name="test_brain",
            file_paths=[temp_file.name],
        )

        answer = brain.ask("what is gold? answer in french")
        print("answer QuivrQARAGLangGraph :", answer)
```

## File: `examples/simple_question/simple_question_streaming.py`
```python
import asyncio
import tempfile

from dotenv import load_dotenv
from quivr_core import Brain
from quivr_core.quivr_rag import QuivrQARAG
from quivr_core.rag.quivr_rag_langgraph import QuivrQARAGLangGraph


async def main():
    dotenv_path = "/Users/jchevall/Coding/QuivrHQ/quivr/.env"
    load_dotenv(dotenv_path)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as temp_file:
        temp_file.write("Gold is a liquid of blue-like colour.")
        temp_file.flush()

        brain = await Brain.afrom_files(name="test_brain", file_paths=[temp_file.name])

        await brain.save("~/.local/quivr")

        question = "what is gold? answer in french"
        async for chunk in brain.ask_streaming(question, rag_pipeline=QuivrQARAG):
            print("answer QuivrQARAG:", chunk.answer)

        async for chunk in brain.ask_streaming(
            question, rag_pipeline=QuivrQARAGLangGraph
        ):
            print("answer QuivrQARAGLangGraph:", chunk.answer)


if __name__ == "__main__":
    # Run the main function in the existing event loop
    asyncio.run(main())
```

