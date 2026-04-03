---
id: github.com-zylon-ai-private-gpt-017b1576-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:48.163194
---

# KNOWLEDGE EXTRACT: github.com_zylon-ai_private-gpt_017b1576
> **Extracted on:** 2026-04-01 16:26:43
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525132/github.com_zylon-ai_private-gpt_017b1576

---

## File: `.dockerignore`
```
.venv
models
.github
.vscode
.DS_Store
.mypy_cache
.ruff_cache
local_data
terraform
tests
Dockerfile
Dockerfile.*
```

## File: `.gitignore`
```
.venv
.env
venv

settings-me.yaml

.ruff_cache
.pytest_cache
.mypy_cache

# byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# unit tests / coverage reports
/tests-results.xml
/.coverage
/coverage.xml
/htmlcov/

# pyenv
/.python-version

# IDE
.idea/
.vscode/
/.run/
.fleet/

# macOS
.DS_Store
```

## File: `.pre-commit-config.yaml`
```yaml
default_install_hook_types:
# Mandatory to install both pre-commit and pre-push hooks (see https://pre-commit.com/#top_level-default_install_hook_types)
# Add new hook types here to ensure automatic installation when running `pre-commit install`
- pre-commit
- pre-push
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.3.0
  hooks:
  - id: trailing-whitespace
  - id: end-of-file-fixer
  - id: check-yaml
  - id: check-json
  - id: check-added-large-files

- repo: local
  hooks:
  - id: black
    name: Formatting (black)
    entry: black
    language: system
    types: [python]
    stages: [commit]
  - id: ruff
    name: Linter (ruff)
    entry: ruff
    language: system
    types: [python]
    stages: [commit]
  - id: mypy
    name: Type checking (mypy)
    entry: make mypy
    pass_filenames: false
    language: system
    types: [python]
    stages: [commit]
  - id: test
    name: Unit tests (pytest)
    entry: make test
    pass_filenames: false
    language: system
    types: [python]
    stages: [push]
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## [0.6.2](https://github.com/zylon-ai/private-gpt/compare/v0.6.1...v0.6.2) (2024-08-08)


### Bug Fixes

* add numpy issue to troubleshooting ([#2048](https://github.com/zylon-ai/private-gpt/issues/2048)) ([4ca6d0c](https://github.com/zylon-ai/private-gpt/commit/4ca6d0cb556be7a598f7d3e3b00d2a29214ee1e8))
* auto-update version ([#2052](https://github.com/zylon-ai/private-gpt/issues/2052)) ([7fefe40](https://github.com/zylon-ai/private-gpt/commit/7fefe408b4267684c6e3c1a43c5dc2b73ec61fe4))
* publish image name ([#2043](https://github.com/zylon-ai/private-gpt/issues/2043)) ([b1acf9d](https://github.com/zylon-ai/private-gpt/commit/b1acf9dc2cbca2047cd0087f13254ff5cda6e570))
* update matplotlib to 3.9.1-post1 to fix win install ([b16abbe](https://github.com/zylon-ai/private-gpt/commit/b16abbefe49527ac038d235659854b98345d5387))

## [0.6.1](https://github.com/zylon-ai/private-gpt/compare/v0.6.0...v0.6.1) (2024-08-05)


### Bug Fixes

* add built image from DockerHub ([#2042](https://github.com/zylon-ai/private-gpt/issues/2042)) ([f09f6dd](https://github.com/zylon-ai/private-gpt/commit/f09f6dd2553077d4566dbe6b48a450e05c2f049e))
* Adding azopenai to model list ([#2035](https://github.com/zylon-ai/private-gpt/issues/2035)) ([1c665f7](https://github.com/zylon-ai/private-gpt/commit/1c665f7900658144f62814b51f6e3434a6d7377f))
* **deploy:** generate docker release when new version is released ([#2038](https://github.com/zylon-ai/private-gpt/issues/2038)) ([1d4c14d](https://github.com/zylon-ai/private-gpt/commit/1d4c14d7a3c383c874b323d934be01afbaca899e))
* **deploy:** improve Docker-Compose and quickstart on Docker ([#2037](https://github.com/zylon-ai/private-gpt/issues/2037)) ([dae0727](https://github.com/zylon-ai/private-gpt/commit/dae0727a1b4abd35d2b0851fe30e0a4ed67e0fbb))

## [0.6.0](https://github.com/zylon-ai/private-gpt/compare/v0.5.0...v0.6.0) (2024-08-02)


### Features

* bump dependencies ([#1987](https://github.com/zylon-ai/private-gpt/issues/1987)) ([b687dc8](https://github.com/zylon-ai/private-gpt/commit/b687dc852413404c52d26dcb94536351a63b169d))
* **docs:** add privategpt-ts sdk ([#1924](https://github.com/zylon-ai/private-gpt/issues/1924)) ([d13029a](https://github.com/zylon-ai/private-gpt/commit/d13029a046f6e19e8ee65bef3acd96365c738df2))
* **docs:** Fix setup docu ([#1926](https://github.com/zylon-ai/private-gpt/issues/1926)) ([067a5f1](https://github.com/zylon-ai/private-gpt/commit/067a5f144ca6e605c99d7dbe9ca7d8207ac8808d))
* **docs:** update doc for ipex-llm ([#1968](https://github.com/zylon-ai/private-gpt/issues/1968)) ([19a7c06](https://github.com/zylon-ai/private-gpt/commit/19a7c065ef7f42b37f289dd28ac945f7afc0e73a))
* **docs:** update documentation and fix preview-docs ([#2000](https://github.com/zylon-ai/private-gpt/issues/2000)) ([4523a30](https://github.com/zylon-ai/private-gpt/commit/4523a30c8f004aac7a7ae224671e2c45ec0cb973))
* **llm:** add progress bar when ollama is pulling models ([#2031](https://github.com/zylon-ai/private-gpt/issues/2031)) ([cf61bf7](https://github.com/zylon-ai/private-gpt/commit/cf61bf780f8d122e4057d002abf03563bb45614a))
* **llm:** autopull ollama models ([#2019](https://github.com/zylon-ai/private-gpt/issues/2019)) ([20bad17](https://github.com/zylon-ai/private-gpt/commit/20bad17c9857809158e689e9671402136c1e3d84))
* **llm:** Support for Google Gemini LLMs and Embeddings ([#1965](https://github.com/zylon-ai/private-gpt/issues/1965)) ([fc13368](https://github.com/zylon-ai/private-gpt/commit/fc13368bc72d1f4c27644677431420ed77731c03))
* make llama3.1 as default ([#2022](https://github.com/zylon-ai/private-gpt/issues/2022)) ([9027d69](https://github.com/zylon-ai/private-gpt/commit/9027d695c11fbb01e62424b855665de71d513417))
* prompt_style applied to all LLMs + extra LLM params. ([#1835](https://github.com/zylon-ai/private-gpt/issues/1835)) ([e21bf20](https://github.com/zylon-ai/private-gpt/commit/e21bf20c10938b24711d9f2c765997f44d7e02a9))
* **recipe:** add our first recipe  `Summarize` ([#2028](https://github.com/zylon-ai/private-gpt/issues/2028)) ([8119842](https://github.com/zylon-ai/private-gpt/commit/8119842ae6f1f5ecfaf42b06fa0d1ffec675def4))
* **vectordb:** Milvus vector db Integration ([#1996](https://github.com/zylon-ai/private-gpt/issues/1996)) ([43cc31f](https://github.com/zylon-ai/private-gpt/commit/43cc31f74015f8d8fcbf7a8ea7d7d9ecc66cf8c9))
* **vectorstore:** Add clickhouse support as vectore store ([#1883](https://github.com/zylon-ai/private-gpt/issues/1883)) ([2612928](https://github.com/zylon-ai/private-gpt/commit/26129288394c7483e6fc0496a11dc35679528cc1))


### Bug Fixes

* "no such group" error in Dockerfile, added docx2txt and cryptography deps ([#1841](https://github.com/zylon-ai/private-gpt/issues/1841)) ([947e737](https://github.com/zylon-ai/private-gpt/commit/947e737f300adf621d2261d527192f36f3387f8e))
* **config:** make tokenizer optional and include a troubleshooting doc ([#1998](https://github.com/zylon-ai/private-gpt/issues/1998)) ([01b7ccd](https://github.com/zylon-ai/private-gpt/commit/01b7ccd0648be032846647c9a184925d3682f612))
* **docs:** Fix concepts.mdx referencing to installation page ([#1779](https://github.com/zylon-ai/private-gpt/issues/1779)) ([dde0224](https://github.com/zylon-ai/private-gpt/commit/dde02245bcd51a7ede7b6789c82ae217cac53d92))
* **docs:** Update installation.mdx ([#1866](https://github.com/zylon-ai/private-gpt/issues/1866)) ([c1802e7](https://github.com/zylon-ai/private-gpt/commit/c1802e7cf0e56a2603213ec3b6a4af8fadb8a17a))
* ffmpy dependency ([#2020](https://github.com/zylon-ai/private-gpt/issues/2020)) ([dabf556](https://github.com/zylon-ai/private-gpt/commit/dabf556dae9cb00fe0262270e5138d982585682e))
* light mode ([#2025](https://github.com/zylon-ai/private-gpt/issues/2025)) ([1020cd5](https://github.com/zylon-ai/private-gpt/commit/1020cd53288af71a17882781f392512568f1b846))
* **LLM:** mistral ignoring assistant messages ([#1954](https://github.com/zylon-ai/private-gpt/issues/1954)) ([c7212ac](https://github.com/zylon-ai/private-gpt/commit/c7212ac7cc891f9e3c713cc206ae9807c5dfdeb6))
* **llm:** special tokens and leading space ([#1831](https://github.com/zylon-ai/private-gpt/issues/1831)) ([347be64](https://github.com/zylon-ai/private-gpt/commit/347be643f7929c56382a77c3f45f0867605e0e0a))
* make embedding_api_base match api_base when on docker ([#1859](https://github.com/zylon-ai/private-gpt/issues/1859)) ([2a432bf](https://github.com/zylon-ai/private-gpt/commit/2a432bf9c5582a94eb4052b1e80cabdb118d298e))
* nomic embeddings ([#2030](https://github.com/zylon-ai/private-gpt/issues/2030)) ([5465958](https://github.com/zylon-ai/private-gpt/commit/54659588b5b109a3dd17cca835e275240464d275))
* prevent to ingest local files (by default) ([#2010](https://github.com/zylon-ai/private-gpt/issues/2010)) ([e54a8fe](https://github.com/zylon-ai/private-gpt/commit/e54a8fe0433252808d0a60f6a08a43c9f5a42f3b))
* Replacing unsafe `eval()` with `json.loads()` ([#1890](https://github.com/zylon-ai/private-gpt/issues/1890)) ([9d0d614](https://github.com/zylon-ai/private-gpt/commit/9d0d614706581a8bfa57db45f62f84ab23d26f15))
* **settings:** enable cors by default so it will work when using ts sdk (spa) ([#1925](https://github.com/zylon-ai/private-gpt/issues/1925)) ([966af47](https://github.com/zylon-ai/private-gpt/commit/966af4771dbe5cf3fdf554b5fdf8f732407859c4))
* **ui:** gradio bug fixes ([#2021](https://github.com/zylon-ai/private-gpt/issues/2021)) ([d4375d0](https://github.com/zylon-ai/private-gpt/commit/d4375d078f18ba53562fd71651159f997fff865f))
* unify embedding models ([#2027](https://github.com/zylon-ai/private-gpt/issues/2027)) ([40638a1](https://github.com/zylon-ai/private-gpt/commit/40638a18a5713d60fec8fe52796dcce66d88258c))

## [0.5.0](https://github.com/zylon-ai/private-gpt/compare/v0.4.0...v0.5.0) (2024-04-02)


### Features

* **code:** improve concat of strings in ui ([#1785](https://github.com/zylon-ai/private-gpt/issues/1785)) ([bac818a](https://github.com/zylon-ai/private-gpt/commit/bac818add51b104cda925b8f1f7b51448e935ca1))
* **docker:** set default Docker to use Ollama ([#1812](https://github.com/zylon-ai/private-gpt/issues/1812)) ([f83abff](https://github.com/zylon-ai/private-gpt/commit/f83abff8bc955a6952c92cc7bcb8985fcec93afa))
* **docs:** Add guide Llama-CPP Linux AMD GPU support ([#1782](https://github.com/zylon-ai/private-gpt/issues/1782)) ([8a836e4](https://github.com/zylon-ai/private-gpt/commit/8a836e4651543f099c59e2bf497ab8c55a7cd2e5))
* **docs:** Feature/upgrade docs ([#1741](https://github.com/zylon-ai/private-gpt/issues/1741)) ([5725181](https://github.com/zylon-ai/private-gpt/commit/572518143ac46532382db70bed6f73b5082302c1))
* **docs:** upgrade fern ([#1596](https://github.com/zylon-ai/private-gpt/issues/1596)) ([84ad16a](https://github.com/zylon-ai/private-gpt/commit/84ad16af80191597a953248ce66e963180e8ddec))
* **ingest:** Created a faster ingestion mode - pipeline ([#1750](https://github.com/zylon-ai/private-gpt/issues/1750)) ([134fc54](https://github.com/zylon-ai/private-gpt/commit/134fc54d7d636be91680dc531f5cbe2c5892ac56))
* **llm - embed:** Add support for Azure OpenAI ([#1698](https://github.com/zylon-ai/private-gpt/issues/1698)) ([1efac6a](https://github.com/zylon-ai/private-gpt/commit/1efac6a3fe19e4d62325e2c2915cd84ea277f04f))
* **llm:** adds serveral settings for llamacpp and ollama ([#1703](https://github.com/zylon-ai/private-gpt/issues/1703)) ([02dc83e](https://github.com/zylon-ai/private-gpt/commit/02dc83e8e9f7ada181ff813f25051bbdff7b7c6b))
* **llm:** Ollama LLM-Embeddings decouple + longer keep_alive settings ([#1800](https://github.com/zylon-ai/private-gpt/issues/1800)) ([b3b0140](https://github.com/zylon-ai/private-gpt/commit/b3b0140e244e7a313bfaf4ef10eb0f7e4192710e))
* **llm:** Ollama timeout setting ([#1773](https://github.com/zylon-ai/private-gpt/issues/1773)) ([6f6c785](https://github.com/zylon-ai/private-gpt/commit/6f6c785dac2bbad37d0b67fda215784298514d39))
* **local:** tiktoken cache within repo for offline ([#1467](https://github.com/zylon-ai/private-gpt/issues/1467)) ([821bca3](https://github.com/zylon-ai/private-gpt/commit/821bca32e9ee7c909fd6488445ff6a04463bf91b))
* **nodestore:** add Postgres for the doc and index store ([#1706](https://github.com/zylon-ai/private-gpt/issues/1706)) ([68b3a34](https://github.com/zylon-ai/private-gpt/commit/68b3a34b032a08ca073a687d2058f926032495b3))
* **rag:** expose similarity_top_k and similarity_score to settings ([#1771](https://github.com/zylon-ai/private-gpt/issues/1771)) ([087cb0b](https://github.com/zylon-ai/private-gpt/commit/087cb0b7b74c3eb80f4f60b47b3a021c81272ae1))
* **RAG:** Introduce SentenceTransformer Reranker ([#1810](https://github.com/zylon-ai/private-gpt/issues/1810)) ([83adc12](https://github.com/zylon-ai/private-gpt/commit/83adc12a8ef0fa0c13a0dec084fa596445fc9075))
* **scripts:** Wipe qdrant and obtain db Stats command ([#1783](https://github.com/zylon-ai/private-gpt/issues/1783)) ([ea153fb](https://github.com/zylon-ai/private-gpt/commit/ea153fb92f1f61f64c0d04fff0048d4d00b6f8d0))
* **ui:** Add Model Information to ChatInterface label ([f0b174c](https://github.com/zylon-ai/private-gpt/commit/f0b174c097c2d5e52deae8ef88de30a0d9013a38))
* **ui:** add sources check to not repeat identical sources ([#1705](https://github.com/zylon-ai/private-gpt/issues/1705)) ([290b9fb](https://github.com/zylon-ai/private-gpt/commit/290b9fb084632216300e89bdadbfeb0380724b12))
* **UI:** Faster startup and document listing ([#1763](https://github.com/zylon-ai/private-gpt/issues/1763)) ([348df78](https://github.com/zylon-ai/private-gpt/commit/348df781b51606b2f9810bcd46f850e54192fd16))
* **ui:** maintain score order when curating sources ([#1643](https://github.com/zylon-ai/private-gpt/issues/1643)) ([410bf7a](https://github.com/zylon-ai/private-gpt/commit/410bf7a71f17e77c4aec723ab80c233b53765964))
* unify settings for vector and nodestore connections to PostgreSQL ([#1730](https://github.com/zylon-ai/private-gpt/issues/1730)) ([63de7e4](https://github.com/zylon-ai/private-gpt/commit/63de7e4930ac90dd87620225112a22ffcbbb31ee))
* wipe per storage type ([#1772](https://github.com/zylon-ai/private-gpt/issues/1772)) ([c2d6948](https://github.com/zylon-ai/private-gpt/commit/c2d694852b4696834962a42fde047b728722ad74))


### Bug Fixes

* **docs:** Minor documentation amendment ([#1739](https://github.com/zylon-ai/private-gpt/issues/1739)) ([258d02d](https://github.com/zylon-ai/private-gpt/commit/258d02d87c5cb81d6c3a6f06aa69339b670dffa9))
* Fixed docker-compose ([#1758](https://github.com/zylon-ai/private-gpt/issues/1758)) ([774e256](https://github.com/zylon-ai/private-gpt/commit/774e2560520dc31146561d09a2eb464c68593871))
* **ingest:** update script label ([#1770](https://github.com/zylon-ai/private-gpt/issues/1770)) ([7d2de5c](https://github.com/zylon-ai/private-gpt/commit/7d2de5c96fd42e339b26269b3155791311ef1d08))
* **settings:** set default tokenizer to avoid running make setup fail ([#1709](https://github.com/zylon-ai/private-gpt/issues/1709)) ([d17c34e](https://github.com/zylon-ai/private-gpt/commit/d17c34e81a84518086b93605b15032e2482377f7))

## [0.4.0](https://github.com/imartinez/privateGPT/compare/v0.3.0...v0.4.0) (2024-03-06)


### Features

* Upgrade to LlamaIndex to 0.10 ([#1663](https://github.com/imartinez/privateGPT/issues/1663)) ([45f0571](https://github.com/imartinez/privateGPT/commit/45f05711eb71ffccdedb26f37e680ced55795d44))
* **Vector:** support pgvector ([#1624](https://github.com/imartinez/privateGPT/issues/1624)) ([cd40e39](https://github.com/imartinez/privateGPT/commit/cd40e3982b780b548b9eea6438c759f1c22743a8))

## [0.3.0](https://github.com/imartinez/privateGPT/compare/v0.2.0...v0.3.0) (2024-02-16)


### Features

* add mistral + chatml prompts ([#1426](https://github.com/imartinez/privateGPT/issues/1426)) ([e326126](https://github.com/imartinez/privateGPT/commit/e326126d0d4cd7e46a79f080c442c86f6dd4d24b))
* Add stream information to generate SDKs ([#1569](https://github.com/imartinez/privateGPT/issues/1569)) ([24fae66](https://github.com/imartinez/privateGPT/commit/24fae660e6913aac6b52745fb2c2fe128ba2eb79))
* **API:** Ingest plain text ([#1417](https://github.com/imartinez/privateGPT/issues/1417)) ([6eeb95e](https://github.com/imartinez/privateGPT/commit/6eeb95ec7f17a618aaa47f5034ee5bccae02b667))
* **bulk-ingest:** Add --ignored Flag to Exclude Specific Files and Directories During Ingestion ([#1432](https://github.com/imartinez/privateGPT/issues/1432)) ([b178b51](https://github.com/imartinez/privateGPT/commit/b178b514519550e355baf0f4f3f6beb73dca7df2))
* **llm:** Add openailike llm mode ([#1447](https://github.com/imartinez/privateGPT/issues/1447)) ([2d27a9f](https://github.com/imartinez/privateGPT/commit/2d27a9f956d672cb1fe715cf0acdd35c37f378a5)), closes [#1424](https://github.com/imartinez/privateGPT/issues/1424)
* **llm:** Add support for Ollama LLM ([#1526](https://github.com/imartinez/privateGPT/issues/1526)) ([6bbec79](https://github.com/imartinez/privateGPT/commit/6bbec79583b7f28d9bea4b39c099ebef149db843))
* **settings:** Configurable context_window and tokenizer ([#1437](https://github.com/imartinez/privateGPT/issues/1437)) ([4780540](https://github.com/imartinez/privateGPT/commit/47805408703c23f0fd5cab52338142c1886b450b))
* **settings:** Update default model to TheBloke/Mistral-7B-Instruct-v0.2-GGUF ([#1415](https://github.com/imartinez/privateGPT/issues/1415)) ([8ec7cf4](https://github.com/imartinez/privateGPT/commit/8ec7cf49f40701a4f2156c48eb2fad9fe6220629))
* **ui:** make chat area stretch to fill the screen ([#1397](https://github.com/imartinez/privateGPT/issues/1397)) ([c71ae7c](https://github.com/imartinez/privateGPT/commit/c71ae7cee92463bbc5ea9c434eab9f99166e1363))
* **UI:** Select file to Query or Delete + Delete ALL ([#1612](https://github.com/imartinez/privateGPT/issues/1612)) ([aa13afd](https://github.com/imartinez/privateGPT/commit/aa13afde07122f2ddda3942f630e5cadc7e4e1ee))


### Bug Fixes

* Adding an LLM param to fix broken generator from llamacpp ([#1519](https://github.com/imartinez/privateGPT/issues/1519)) ([869233f](https://github.com/imartinez/privateGPT/commit/869233f0e4f03dc23e5fae43cf7cb55350afdee9))
* **deploy:** fix local and external dockerfiles ([fde2b94](https://github.com/imartinez/privateGPT/commit/fde2b942bc03688701ed563be6d7d597c75e4e4e))
* **docker:** docker broken copy ([#1419](https://github.com/imartinez/privateGPT/issues/1419)) ([059f358](https://github.com/imartinez/privateGPT/commit/059f35840adbc3fb93d847d6decf6da32d08670c))
* **docs:** Update quickstart doc and set version in pyproject.toml to 0.2.0 ([0a89d76](https://github.com/imartinez/privateGPT/commit/0a89d76cc5ed4371ffe8068858f23dfbb5e8cc37))
* minor bug in chat stream output - python error being serialized ([#1449](https://github.com/imartinez/privateGPT/issues/1449)) ([6191bcd](https://github.com/imartinez/privateGPT/commit/6191bcdbd6e92b6f4d5995967dc196c9348c5954))
* **settings:** correct yaml multiline string ([#1403](https://github.com/imartinez/privateGPT/issues/1403)) ([2564f8d](https://github.com/imartinez/privateGPT/commit/2564f8d2bb8c4332a6a0ab6d722a2ac15006b85f))
* **tests:** load the test settings only when running tests ([d3acd85](https://github.com/imartinez/privateGPT/commit/d3acd85fe34030f8cfd7daf50b30c534087bdf2b))
* **UI:** Updated ui.py. Frees up the CPU to not be bottlenecked. ([24fb80c](https://github.com/imartinez/privateGPT/commit/24fb80ca38f21910fe4fd81505d14960e9ed4faa))

## [0.2.0](https://github.com/imartinez/privateGPT/compare/v0.1.0...v0.2.0) (2023-12-10)


### Features

* **llm:** drop default_system_prompt ([#1385](https://github.com/imartinez/privateGPT/issues/1385)) ([a3ed14c](https://github.com/imartinez/privateGPT/commit/a3ed14c58f77351dbd5f8f2d7868d1642a44f017))
* **ui:** Allows User to Set System Prompt via "Additional Options" in Chat Interface ([#1353](https://github.com/imartinez/privateGPT/issues/1353)) ([145f3ec](https://github.com/imartinez/privateGPT/commit/145f3ec9f41c4def5abf4065a06fb0786e2d992a))

## [0.1.0](https://github.com/imartinez/privateGPT/compare/v0.0.2...v0.1.0) (2023-11-30)


### Features

* Disable Gradio Analytics ([#1165](https://github.com/imartinez/privateGPT/issues/1165)) ([6583dc8](https://github.com/imartinez/privateGPT/commit/6583dc84c082773443fc3973b1cdf8095fa3fec3))
* Drop loguru and use builtin `logging` ([#1133](https://github.com/imartinez/privateGPT/issues/1133)) ([64c5ae2](https://github.com/imartinez/privateGPT/commit/64c5ae214a9520151c9c2d52ece535867d799367))
* enable resume download for hf_hub_download ([#1249](https://github.com/imartinez/privateGPT/issues/1249)) ([4197ada](https://github.com/imartinez/privateGPT/commit/4197ada6267c822f32c1d7ba2be6e7ce145a3404))
* move torch and transformers to local group ([#1172](https://github.com/imartinez/privateGPT/issues/1172)) ([0d677e1](https://github.com/imartinez/privateGPT/commit/0d677e10b970aec222ec04837d0f08f1631b6d4a))
* Qdrant support ([#1228](https://github.com/imartinez/privateGPT/issues/1228)) ([03d1ae6](https://github.com/imartinez/privateGPT/commit/03d1ae6d70dffdd2411f0d4e92f65080fff5a6e2))


### Bug Fixes

* Docker and sagemaker setup ([#1118](https://github.com/imartinez/privateGPT/issues/1118)) ([895588b](https://github.com/imartinez/privateGPT/commit/895588b82a06c2bc71a9e22fb840c7f6442a3b5b))
* fix pytorch version to avoid wheel bug ([#1123](https://github.com/imartinez/privateGPT/issues/1123)) ([24cfddd](https://github.com/imartinez/privateGPT/commit/24cfddd60f74aadd2dade4c63f6012a2489938a1))
* Remove global state ([#1216](https://github.com/imartinez/privateGPT/issues/1216)) ([022bd71](https://github.com/imartinez/privateGPT/commit/022bd718e3dfc197027b1e24fb97e5525b186db4))
* sagemaker config and chat methods ([#1142](https://github.com/imartinez/privateGPT/issues/1142)) ([a517a58](https://github.com/imartinez/privateGPT/commit/a517a588c4927aa5c5c2a93e4f82a58f0599d251))
* typo in README.md ([#1091](https://github.com/imartinez/privateGPT/issues/1091)) ([ba23443](https://github.com/imartinez/privateGPT/commit/ba23443a70d323cd4f9a242b33fd9dce1bacd2db))
* Windows 11 failing to auto-delete tmp file ([#1260](https://github.com/imartinez/privateGPT/issues/1260)) ([0d52002](https://github.com/imartinez/privateGPT/commit/0d520026a3d5b08a9b8487be992d3095b21e710c))
* Windows permission error on ingest service tmp files ([#1280](https://github.com/imartinez/privateGPT/issues/1280)) ([f1cbff0](https://github.com/imartinez/privateGPT/commit/f1cbff0fb7059432d9e71473cbdd039032dab60d))

## [0.0.2](https://github.com/imartinez/privateGPT/compare/v0.0.1...v0.0.2) (2023-10-20)


### Bug Fixes

* chromadb max batch size ([#1087](https://github.com/imartinez/privateGPT/issues/1087)) ([f5a9bf4](https://github.com/imartinez/privateGPT/commit/f5a9bf4e374b2d4c76438cf8a97cccf222ec8e6f))

## 0.0.1 (2023-10-20)

### Miscellaneous Chores

* Initial version ([490d93f](https://github.com/imartinez/privateGPT/commit/490d93fdc1977443c92f6c42e57a1c585aa59430))
```

## File: `CITATION.cff`
```
# This CITATION.cff file was generated with cffinit.
# Visit https://bit.ly/cffinit to generate yours today!

cff-version: 1.2.0
title: PrivateGPT
message: >-
  If you use this software, please cite it using the
  metadata from this file.
type: software
authors:
  - name: Zylon by PrivateGPT
    address: hello@zylon.ai
    website: 'https://www.zylon.ai/'
repository-code: 'https://github.com/zylon-ai/private-gpt'
license: Apache-2.0
date-released: '2023-05-02'
```

## File: `Dockerfile.llamacpp-cpu`
```
### IMPORTANT, THIS IMAGE CAN ONLY BE RUN IN LINUX DOCKER
### You will run into a segfault in mac
FROM python:3.11.6-slim-bookworm AS base

# Install poetry
RUN pip install pipx
RUN python3 -m pipx ensurepath
RUN pipx install poetry==1.8.3
ENV PATH="/root/.local/bin:$PATH"
ENV PATH=".venv/bin/:$PATH"

# Dependencies to build llama-cpp
RUN apt update && apt install -y \
  libopenblas-dev\
  ninja-build\
  build-essential\
  pkg-config\
  wget

# https://python-poetry.org/docs/configuration/#virtualenvsin-project
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

FROM base AS dependencies
WORKDIR /home/worker/app
COPY pyproject.toml poetry.lock ./

ARG POETRY_EXTRAS="ui embeddings-huggingface llms-llama-cpp vector-stores-qdrant"
RUN poetry install --no-root --extras "${POETRY_EXTRAS}"

FROM base AS app

ENV PYTHONUNBUFFERED=1
ENV PORT=8080
ENV APP_ENV=prod
ENV PYTHONPATH="$PYTHONPATH:/home/worker/app/private_gpt/"
EXPOSE 8080

# Prepare a non-root user
# More info about how to configure UIDs and GIDs in Docker:
# https://github.com/systemd/systemd/blob/main/docs/UIDS-GIDS.md

# Define the User ID (UID) for the non-root user
# UID 100 is chosen to avoid conflicts with existing system users
ARG UID=100

# Define the Group ID (GID) for the non-root user
# GID 65534 is often used for the 'nogroup' or 'nobody' group
ARG GID=65534

RUN adduser --system --gid ${GID} --uid ${UID} --home /home/worker worker
WORKDIR /home/worker/app

RUN chown worker /home/worker/app
RUN mkdir local_data && chown worker local_data
RUN mkdir models && chown worker models
COPY --chown=worker --from=dependencies /home/worker/app/.venv/ .venv
COPY --chown=worker private_gpt/ private_gpt
COPY --chown=worker *.yaml ./
COPY --chown=worker scripts/ scripts

USER worker
ENTRYPOINT python -m private_gpt
```

## File: `Dockerfile.ollama`
```
FROM python:3.11.6-slim-bookworm AS base

# Install poetry
RUN pip install pipx
RUN python3 -m pipx ensurepath
RUN pipx install poetry==1.8.3
ENV PATH="/root/.local/bin:$PATH"
ENV PATH=".venv/bin/:$PATH"

# https://python-poetry.org/docs/configuration/#virtualenvsin-project
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

FROM base AS dependencies
WORKDIR /home/worker/app
COPY pyproject.toml poetry.lock ./

ARG POETRY_EXTRAS="ui vector-stores-qdrant llms-ollama embeddings-ollama"
RUN poetry install --no-root --extras "${POETRY_EXTRAS}"

FROM base AS app
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
ENV APP_ENV=prod
ENV PYTHONPATH="$PYTHONPATH:/home/worker/app/private_gpt/"
EXPOSE 8080

# Prepare a non-root user
# More info about how to configure UIDs and GIDs in Docker:
# https://github.com/systemd/systemd/blob/main/docs/UIDS-GIDS.md

# Define the User ID (UID) for the non-root user
# UID 100 is chosen to avoid conflicts with existing system users
ARG UID=100

# Define the Group ID (GID) for the non-root user
# GID 65534 is often used for the 'nogroup' or 'nobody' group
ARG GID=65534

RUN adduser --system --gid ${GID} --uid ${UID} --home /home/worker worker
WORKDIR /home/worker/app

RUN chown worker /home/worker/app
RUN mkdir local_data && chown worker local_data
RUN mkdir models && chown worker models
COPY --chown=worker --from=dependencies /home/worker/app/.venv/ .venv
COPY --chown=worker private_gpt/ private_gpt
COPY --chown=worker *.yaml .
COPY --chown=worker scripts/ scripts

USER worker
ENTRYPOINT python -m private_gpt
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

   Copyright [yyyy] [name of copyright owner]

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

## File: `Makefile`
```
# Any args passed to the make script, use with $(call args, default_value)
args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`

########################################################################################################################
# Quality checks
########################################################################################################################

test:
	PYTHONPATH=. poetry run pytest tests

test-coverage:
	PYTHONPATH=. poetry run pytest tests --cov private_gpt --cov-report term --cov-report=html --cov-report xml --junit-xml=tests-results.xml

black:
	poetry run black . --check

ruff:
	poetry run ruff check private_gpt tests

format:
	poetry run black .
	poetry run ruff check private_gpt tests --fix

mypy:
	poetry run mypy private_gpt

check:
	make format
	make mypy

########################################################################################################################
# Run
########################################################################################################################

run:
	poetry run python -m private_gpt

dev-windows:
	(set PGPT_PROFILES=local & poetry run python -m uvicorn private_gpt.main:app --reload --port 8001)

dev:
	PYTHONUNBUFFERED=1 PGPT_PROFILES=local poetry run python -m uvicorn private_gpt.main:app --reload --port 8001

########################################################################################################################
# Misc
########################################################################################################################

api-docs:
	PGPT_PROFILES=mock poetry run python scripts/extract_openapi.py private_gpt.main:app --out fern/openapi/openapi.json

ingest:
	@poetry run python scripts/ingest_folder.py $(call args)

stats:
	poetry run python scripts/utils.py stats

wipe:
	poetry run python scripts/utils.py wipe

setup:
	poetry run python scripts/setup

list:
	@echo "Available commands:"
	@echo "  test            : Run tests using pytest"
	@echo "  test-coverage   : Run tests with coverage report"
	@echo "  black           : Check code format with black"
	@echo "  ruff            : Check code with ruff"
	@echo "  format          : Format code with black and ruff"
	@echo "  mypy            : Run mypy for type checking"
	@echo "  check           : Run format and mypy commands"
	@echo "  run             : Run the application"
	@echo "  dev-windows     : Run the application in development mode on Windows"
	@echo "  dev             : Run the application in development mode"
	@echo "  api-docs        : Generate API documentation"
	@echo "  ingest          : Ingest data using specified script"
	@echo "  wipe            : Wipe data using specified script"
	@echo "  setup           : Setup the application"
```

## File: `README.md`
```markdown
# PrivateGPT 

<a href="https://trendshift.io/repositories/2601" target="_blank"><img src="https://trendshift.io/api/badge/repositories/2601" alt="imartinez%2FprivateGPT | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

[![Tests](https://github.com/zylon-ai/private-gpt/actions/workflows/tests.yml/badge.svg)](https://github.com/zylon-ai/private-gpt/actions/workflows/tests.yml?query=branch%3Amain)
[![Website](https://img.shields.io/website?up_message=check%20it&down_message=down&url=https%3A%2F%2Fdocs.privategpt.dev%2F&label=Documentation)](https://docs.privategpt.dev/)
[![Discord](https://img.shields.io/discord/1164200432894234644?logo=discord&label=PrivateGPT)](https://discord.gg/bK6mRVpErU)
[![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/ZylonPrivateGPT)](https://twitter.com/ZylonPrivateGPT)

![Gradio UI](/fern/docs/assets/ui.png?raw=true)

PrivateGPT -built by Zylon- is a production-ready AI project that allows you to ask questions about your documents using the power
of Large Language Models (LLMs), even in scenarios without an Internet connection. 100% private, no data leaves your
execution environment at any point.

>[!TIP]
> If you are looking for an **enterprise-ready, fully private AI platform for regulated industries** like financial services (banks, insurance, investment), defense, critical infrastructure services, government and healthcare,
> check out [Zylon's website](https://zylon.ai)  or [request a demo](https://cal.com/zylon/demo?source=pgpt-readme).
> **Zylon** is an enterprise AI platform delivering private generative AI and on-premise AI software for regulated industries, enabling secure deployment inside enterprise infrastructure without external cloud dependencies.

The project provides an API offering all the primitives required to build private, context-aware AI applications.
It follows and extends the [OpenAI API standard](https://openai.com/blog/openai-api),
and supports both normal and streaming responses.

The API is divided into two logical blocks:

**High-level API**, which abstracts all the complexity of a RAG (Retrieval Augmented Generation)
pipeline implementation:
- Ingestion of documents: internally managing document parsing,
splitting, metadata extraction, embedding generation and storage.
- Chat & Completions using context from ingested documents:
abstracting the retrieval of context, the prompt engineering and the response generation.

**Low-level API**, which allows advanced users to implement their own complex pipelines:
- Embeddings generation: based on a piece of text.
- Contextual chunks retrieval: given a query, returns the most relevant chunks of text from the ingested documents.

In addition to this, a working [Gradio UI](https://www.gradio.app/)
client is provided to test the API, together with a set of useful tools such as bulk model
download script, ingestion script, documents folder watch, etc.

## 🎞️ Overview
>[!WARNING]
>  This README is not updated as frequently as the [documentation](https://docs.privategpt.dev/).
>  Please check it out for the latest updates!

### Motivation behind PrivateGPT
Generative AI is a game changer for our society, but adoption in companies of all sizes and data-sensitive
domains like healthcare or legal is limited by a clear concern: **privacy**.
Not being able to ensure that your data is fully under your control when using third-party AI tools
is a risk those industries cannot take.

### Primordial version
The first version of PrivateGPT was launched in May 2023 as a novel approach to address the privacy
concerns by using LLMs in a complete offline way.

That version, which rapidly became a go-to project for privacy-sensitive setups and served as the seed
for thousands of local-focused generative AI projects, was the foundation of what PrivateGPT is becoming nowadays;
thus a simpler and more educational implementation to understand the basic concepts required
to build a fully local -and therefore, private- chatGPT-like tool.

If you want to keep experimenting with it, we have saved it in the
[primordial branch](https://github.com/zylon-ai/private-gpt/tree/primordial) of the project.

> It is strongly recommended to do a clean clone and install of this new version of
PrivateGPT if you come from the previous, primordial version.

### Present and Future of PrivateGPT
PrivateGPT is now evolving towards becoming a gateway to generative AI models and primitives, including
completions, document ingestion, RAG pipelines and other low-level building blocks.
We want to make it easier for any developer to build AI applications and experiences, as well as provide
a suitable extensive architecture for the community to keep contributing.

Stay tuned to our [releases](https://github.com/zylon-ai/private-gpt/releases) to check out all the new features and changes included.

## 📄 Documentation
Full documentation on installation, dependencies, configuration, running the server, deployment options,
ingesting local documents, API details and UI features can be found here: https://docs.privategpt.dev/

## 🧩 Architecture
Conceptually, PrivateGPT is an API that wraps a RAG pipeline and exposes its
primitives.
* The API is built using [FastAPI](https://fastapi.tiangolo.com/) and follows
  [OpenAI's API scheme](https://platform.openai.com/docs/api-reference).
* The RAG pipeline is based on [LlamaIndex](https://www.llamaindex.ai/).

The design of PrivateGPT allows to easily extend and adapt both the API and the
RAG implementation. Some key architectural decisions are:
* Dependency Injection, decoupling the different components and layers.
* Usage of LlamaIndex abstractions such as `LLM`, `BaseEmbedding` or `VectorStore`,
  making it immediate to change the actual implementations of those abstractions.
* Simplicity, adding as few layers and new abstractions as possible.
* Ready to use, providing a full implementation of the API and RAG
  pipeline.

Main building blocks:
* APIs are defined in `private_gpt:server:<api>`. Each package contains an
  `<api>_router.py` (FastAPI layer) and an `<api>_service.py` (the
  service implementation). Each *Service* uses LlamaIndex base abstractions instead
  of specific implementations,
  decoupling the actual implementation from its usage.
* Components are placed in
  `private_gpt:components:<component>`. Each *Component* is in charge of providing
  actual implementations to the base abstractions used in the Services - for example
  `LLMComponent` is in charge of providing an actual implementation of an `LLM`
  (for example `LlamaCPP` or `OpenAI`).

## 💡 Contributing
Contributions are welcomed! To ensure code quality we have enabled several format and
typing checks, just run `make check` before committing to make sure your code is ok.
Remember to test your code! You'll find a tests folder with helpers, and you can run
tests using `make test` command.

Don't know what to contribute? Here is the public 
[Project Board](https://github.com/users/imartinez/projects/3) with several ideas. 

Head over to Discord 
#contributors channel and ask for write permissions on that GitHub project.

## 💬 Community
Join the conversation around PrivateGPT on our:
- [Twitter (aka X)](https://twitter.com/PrivateGPT_AI)
- [Discord](https://discord.gg/bK6mRVpErU)

## 📖 Citation
If you use PrivateGPT in a paper, check out the [Citation file](CITATION.cff) for the correct citation.  
You can also use the "Cite this repository" button in this repo to get the citation in different formats.

Here are a couple of examples:

#### BibTeX
```bibtex
@software{Zylon_PrivateGPT_2023,
author = {Zylon by PrivateGPT},
license = {Apache-2.0},
month = may,
title = {{PrivateGPT}},
url = {https://github.com/zylon-ai/private-gpt},
year = {2023}
}
```

#### APA
```
Zylon by PrivateGPT (2023). PrivateGPT [Computer software]. https://github.com/zylon-ai/private-gpt
```

## 🤗 Partners & Supporters
PrivateGPT is actively supported by the teams behind:
* [Qdrant](https://qdrant.tech/), providing the default vector database
* [Fern](https://buildwithfern.com/), providing Documentation and SDKs
* [LlamaIndex](https://www.llamaindex.ai/), providing the base RAG framework and abstractions

This project has been strongly influenced and supported by other amazing projects like 
[LangChain](https://github.com/hwchase17/langchain),
[GPT4All](https://github.com/nomic-ai/gpt4all),
[LlamaCpp](https://github.com/ggerganov/llama.cpp),
[Chroma](https://www.trychroma.com/)
and [SentenceTransformers](https://www.sbert.net/).
```

## File: `docker-compose.yaml`
```yaml
services:

  #-----------------------------------
  #---- Private-GPT services ---------
  #-----------------------------------

  # Private-GPT service for the Ollama CPU and GPU modes
  # This service builds from an external Dockerfile and runs the Ollama mode.
  private-gpt-ollama:
    image: ${PGPT_IMAGE:-zylonai/private-gpt}:${PGPT_TAG:-0.6.2}-ollama  # x-release-please-version
    user: root
    build:
      context: .
      dockerfile: Dockerfile.ollama
    volumes:
      - ./local_data:/home/worker/app/local_data
    ports:
      - "8001:8001"
    environment:
      PORT: 8001
      PGPT_PROFILES: docker
      PGPT_MODE: ollama
      PGPT_EMBED_MODE: ollama
      PGPT_OLLAMA_API_BASE: http://ollama:11434
      HF_TOKEN: ${HF_TOKEN:-}
    profiles:
      - ""
      - ollama-cpu
      - ollama-cuda
      - ollama-api
    depends_on:
      ollama:
        condition: service_healthy

  # Private-GPT service for the local mode
  # This service builds from a local Dockerfile and runs the application in local mode.
  private-gpt-llamacpp-cpu:
    image: ${PGPT_IMAGE:-zylonai/private-gpt}:${PGPT_TAG:-0.6.2}-llamacpp-cpu # x-release-please-version
    user: root
    build:
      context: .
      dockerfile: Dockerfile.llamacpp-cpu
    volumes:
      - ./local_data/:/home/worker/app/local_data
      - ./models/:/home/worker/app/models
    entrypoint: sh -c ".venv/bin/python scripts/setup && .venv/bin/python -m private_gpt"
    ports:
      - "8001:8001"
    environment:
      PORT: 8001
      PGPT_PROFILES: local
      HF_TOKEN: ${HF_TOKEN:-}
    profiles:
      - llamacpp-cpu

  #-----------------------------------
  #---- Ollama services --------------
  #-----------------------------------

  # Traefik reverse proxy for the Ollama service
  # This will route requests to the Ollama service based on the profile.
  ollama:
    image: traefik:v2.10
    healthcheck:
      test: ["CMD", "sh", "-c", "wget -q --spider http://ollama:11434 || exit 1"]
      interval: 10s
      retries: 3
      start_period: 5s
      timeout: 5s
    ports:
      - "8080:8080"
    command:
      - "--providers.file.filename=/etc/router.yml"
      - "--log.level=ERROR"
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:11434"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./.docker/router.yml:/etc/router.yml:ro
    extra_hosts:
      - "host.docker.internal:host-gateway"
    profiles:
      - ""
      - ollama-cpu
      - ollama-cuda
      - ollama-api

  # Ollama service for the CPU mode
  ollama-cpu:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ./models:/root/.ollama
    profiles:
      - ""
      - ollama-cpu

  # Ollama service for the CUDA mode
  ollama-cuda:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ./models:/root/.ollama
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
    profiles:
      - ollama-cuda
```

## File: `pyproject.toml`
```
[tool.poetry]
name = "private-gpt"
version = "0.6.2"
description = "Private GPT"
authors = ["Zylon <hi@zylon.ai>"]

[tool.poetry.dependencies]
python = ">=3.11,<3.12"
# PrivateGPT
fastapi = { extras = ["all"], version = "^0.115.0" }
python-multipart = "^0.0.10"
injector = "^0.22.0"
pyyaml = "^6.0.2"
watchdog = "^4.0.1"
transformers = "^4.44.2"
docx2txt = "^0.8"
cryptography = "^3.1"
# LlamaIndex core libs
llama-index-core = ">=0.11.2,<0.12.0"
llama-index-readers-file = "*"
# Optional LlamaIndex integration libs
llama-index-llms-llama-cpp = {version = "*", optional = true}
llama-index-llms-openai = {version ="*", optional = true}
llama-index-llms-openai-like = {version ="*", optional = true}
llama-index-llms-ollama = {version ="*", optional = true}
llama-index-llms-azure-openai = {version ="*", optional = true}
llama-index-llms-gemini = {version ="*", optional = true}
llama-index-embeddings-ollama = {version ="*", optional = true}
llama-index-embeddings-huggingface = {version ="*", optional = true}
llama-index-embeddings-openai = {version ="*", optional = true}
llama-index-embeddings-azure-openai = {version ="*", optional = true}
llama-index-embeddings-gemini = {version ="*", optional = true}
llama-index-embeddings-mistralai = {version ="*", optional = true}
llama-index-vector-stores-qdrant = {version ="*", optional = true}
llama-index-vector-stores-milvus = {version ="*", optional = true}
llama-index-vector-stores-chroma = {version ="*", optional = true}
llama-index-vector-stores-postgres = {version ="*", optional = true}
llama-index-vector-stores-clickhouse = {version ="*", optional = true}
llama-index-storage-docstore-postgres = {version ="*", optional = true}
llama-index-storage-index-store-postgres = {version ="*", optional = true}
# Postgres
psycopg2-binary = {version ="^2.9.9", optional = true}
asyncpg = {version="^0.29.0", optional = true}

# ClickHouse
clickhouse-connect = {version = "^0.7.19", optional = true}

# Optional Sagemaker dependency
boto3 = {version ="^1.35.26", optional = true}

# Optional Reranker dependencies
torch = {version ="^2.4.1", optional = true}
sentence-transformers = {version ="^3.1.1", optional = true}

# Optional UI
gradio = {version ="^4.44.0", optional = true}
ffmpy = {version ="^0.4.0", optional = true}

# Optional HF Transformers
einops = {version = "^0.8.0", optional = true}
retry-async = "^0.1.4"

[tool.poetry.extras]
ui = ["gradio", "ffmpy"]
llms-llama-cpp = ["llama-index-llms-llama-cpp"]
llms-openai = ["llama-index-llms-openai"]
llms-openai-like = ["llama-index-llms-openai-like"]
llms-ollama = ["llama-index-llms-ollama"]
llms-sagemaker = ["boto3"]
llms-azopenai = ["llama-index-llms-azure-openai"]
llms-gemini = ["llama-index-llms-gemini"]
embeddings-ollama = ["llama-index-embeddings-ollama"]
embeddings-huggingface = ["llama-index-embeddings-huggingface", "einops"]
embeddings-openai = ["llama-index-embeddings-openai"]
embeddings-sagemaker = ["boto3"]
embeddings-azopenai = ["llama-index-embeddings-azure-openai"]
embeddings-gemini = ["llama-index-embeddings-gemini"]
embeddings-mistral = ["llama-index-embeddings-mistralai"]
vector-stores-qdrant = ["llama-index-vector-stores-qdrant"]
vector-stores-clickhouse = ["llama-index-vector-stores-clickhouse", "clickhouse_connect"]
vector-stores-chroma = ["llama-index-vector-stores-chroma"]
vector-stores-postgres = ["llama-index-vector-stores-postgres"]
vector-stores-milvus = ["llama-index-vector-stores-milvus"]
storage-nodestore-postgres = ["llama-index-storage-docstore-postgres","llama-index-storage-index-store-postgres","psycopg2-binary","asyncpg"]
rerank-sentence-transformers = ["torch", "sentence-transformers"]

[tool.poetry.group.dev.dependencies]
black = "^24"
mypy = "^1.11"
pre-commit = "^3"
pytest = "^8"
pytest-cov = "^5"
ruff = "^0"
pytest-asyncio = "^0.24.0"
types-pyyaml = "^6.0.12.20240917"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

# Packages configs

## coverage

[tool.coverage.run]
branch = true

[tool.coverage.report]
skip_empty = true
precision = 2

## black

[tool.black]
target-version = ['py311']

## ruff
# Recommended ruff config for now, to be updated as we go along.
[tool.ruff]
target-version = 'py311'

# See all rules at https://beta.ruff.rs/docs/rules/
lint.select = [
    "E", # pycodestyle
    "W", # pycodestyle
    "F", # Pyflakes
    "B", # flake8-bugbear
    "C4", # flake8-comprehensions
    "D", # pydocstyle
    "I", # isort
    "SIM", # flake8-simplify
    "TCH", # flake8-type-checking
    "TID", # flake8-tidy-imports
    "Q", # flake8-quotes
    "UP", # pyupgrade
    "PT", # flake8-pytest-style
    "RUF", # Ruff-specific rules
]

lint.ignore = [
    "E501", # "Line too long"
    # -> line length already regulated by black
    "PT011", # "pytest.raises() should specify expected exception"
    # -> would imply to update tests every time you update exception message
    "SIM102", # "Use a single `if` statement instead of nested `if` statements"
    # -> too restrictive,
    "D100",
    "D101",
    "D102",
    "D103",
    "D104",
    "D105",
    "D106",
    "D107"
    # -> "Missing docstring in public function too restrictive"
]

[tool.ruff.lint.pydocstyle]
# Automatically disable rules that are incompatible with Google docstring convention
convention = "google"

[tool.ruff.lint.pycodestyle]
max-doc-length = 88

[tool.ruff.lint.flake8-tidy-imports]
ban-relative-imports = "all"

[tool.ruff.lint.flake8-type-checking]
strict = true
runtime-evaluated-base-classes = ["pydantic.BaseModel"]
# Pydantic needs to be able to evaluate types at runtime
# see https://pypi.org/project/flake8-type-checking/ for flake8-type-checking documentation
# see https://beta.ruff.rs/docs/settings/#flake8-type-checking-runtime-evaluated-base-classes for ruff documentation

[tool.ruff.lint.per-file-ignores]
# Allow missing docstrings for tests
"tests/**/*.py" = ["D1"]

## mypy

[tool.mypy]
python_version = "3.11"
strict = true
check_untyped_defs = false
explicit_package_bases = true
warn_unused_ignores = false
exclude = ["tests"]

[tool.mypy-llama-index]
ignore_missing_imports = true

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
addopts = [
    "--import-mode=importlib",
]
```

## File: `settings-azopenai.yaml`
```yaml
server:
  env_name: ${APP_ENV:azopenai}

llm:
  mode: azopenai

embedding:
  mode: azopenai

azopenai:
  api_key: ${AZ_OPENAI_API_KEY:}
  azure_endpoint: ${AZ_OPENAI_ENDPOINT:}
  embedding_deployment_name: ${AZ_OPENAI_EMBEDDING_DEPLOYMENT_NAME:}
  llm_deployment_name: ${AZ_OPENAI_LLM_DEPLOYMENT_NAME:}
  api_version: "2023-05-15"
  embedding_model: text-embedding-ada-002
  llm_model: gpt-35-turbo
```

## File: `settings-docker.yaml`
```yaml
server:
  env_name: ${APP_ENV:prod}
  port: ${PORT:8080}

llm:
  mode: ${PGPT_MODE:mock}

embedding:
  mode: ${PGPT_EMBED_MODE:mock}

llamacpp:
  llm_hf_repo_id: ${PGPT_HF_REPO_ID:lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF}
  llm_hf_model_file: ${PGPT_HF_MODEL_FILE:Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf}

huggingface:
  embedding_hf_model_name: ${PGPT_EMBEDDING_HF_MODEL_NAME:nomic-ai/nomic-embed-text-v1.5}

sagemaker:
  llm_endpoint_name: ${PGPT_SAGEMAKER_LLM_ENDPOINT_NAME:}
  embedding_endpoint_name: ${PGPT_SAGEMAKER_EMBEDDING_ENDPOINT_NAME:}

ollama:
  llm_model: ${PGPT_OLLAMA_LLM_MODEL:llama3.1}
  embedding_model: ${PGPT_OLLAMA_EMBEDDING_MODEL:nomic-embed-text}
  api_base: ${PGPT_OLLAMA_API_BASE:http://ollama:11434}
  embedding_api_base: ${PGPT_OLLAMA_EMBEDDING_API_BASE:http://ollama:11434}
  tfs_z: ${PGPT_OLLAMA_TFS_Z:1.0}
  top_k: ${PGPT_OLLAMA_TOP_K:40}
  top_p: ${PGPT_OLLAMA_TOP_P:0.9}
  repeat_last_n: ${PGPT_OLLAMA_REPEAT_LAST_N:64}
  repeat_penalty: ${PGPT_OLLAMA_REPEAT_PENALTY:1.2}
  request_timeout: ${PGPT_OLLAMA_REQUEST_TIMEOUT:600.0}
  autopull_models: ${PGPT_OLLAMA_AUTOPULL_MODELS:true}

ui:
  enabled: true
  path: /
```

## File: `settings-gemini.yaml`
```yaml
llm:
  mode: gemini

embedding:
  mode: gemini

gemini:
  api_key: ${GOOGLE_API_KEY:}
  model: models/gemini-pro
  embedding_model: models/embedding-001
```

## File: `settings-local.yaml`
```yaml
# poetry install --extras "ui llms-llama-cpp vector-stores-qdrant embeddings-huggingface"
server:
  env_name: ${APP_ENV:local}

llm:
  mode: llamacpp
  # Should be matching the selected model
  max_new_tokens: 512
  context_window: 3900
  tokenizer: meta-llama/Meta-Llama-3.1-8B-Instruct
  prompt_style: "llama3"

llamacpp:
  llm_hf_repo_id: lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF
  llm_hf_model_file: Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf

embedding:
  mode: huggingface

huggingface:
  embedding_hf_model_name: nomic-ai/nomic-embed-text-v1.5

vectorstore:
  database: qdrant

qdrant:
  path: local_data/private_gpt/qdrant
```

## File: `settings-mock.yaml`
```yaml
server:
  env_name: ${APP_ENV:mock}

# This configuration allows you to use GPU for creating embeddings while avoiding loading LLM into vRAM
llm:
  mode: mock

embedding:
  mode: huggingface
```

## File: `settings-ollama-pg.yaml`
```yaml
# Using ollama and postgres for the vector, doc and index store. Ollama is also used for embeddings.
# To use install these extras:
# poetry install --extras "llms-ollama ui vector-stores-postgres embeddings-ollama storage-nodestore-postgres"
server:
  env_name: ${APP_ENV:ollama}

llm:
  mode: ollama
  max_new_tokens: 512
  context_window: 3900

embedding:
  mode: ollama
  embed_dim: 768

ollama:
  llm_model: llama3.1
  embedding_model: nomic-embed-text
  api_base: http://localhost:11434

nodestore:
  database: postgres

vectorstore:
  database: postgres

postgres:
  host: localhost
  port: 5432
  database: postgres
  user: postgres
  password: admin
  schema_name: private_gpt

```

## File: `settings-ollama.yaml`
```yaml
server:
  env_name: ${APP_ENV:ollama}

llm:
  mode: ollama
  max_new_tokens: 512
  context_window: 3900
  temperature: 0.1     #The temperature of the model. Increasing the temperature will make the model answer more creatively. A value of 0.1 would be more factual. (Default: 0.1)

embedding:
  mode: ollama

ollama:
  llm_model: llama3.1
  embedding_model: nomic-embed-text
  api_base: http://localhost:11434
  embedding_api_base: http://localhost:11434  # change if your embedding model runs on another ollama
  keep_alive: 5m
  tfs_z: 1.0              # Tail free sampling is used to reduce the impact of less probable tokens from the output. A higher value (e.g., 2.0) will reduce the impact more, while a value of 1.0 disables this setting.
  top_k: 40               # Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative. (Default: 40)
  top_p: 0.9              # Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text. (Default: 0.9)
  repeat_last_n: 64       # Sets how far back for the model to look back to prevent repetition. (Default: 64, 0 = disabled, -1 = num_ctx)
  repeat_penalty: 1.2     # Sets how strongly to penalize repetitions. A higher value (e.g., 1.5) will penalize repetitions more strongly, while a lower value (e.g., 0.9) will be more lenient. (Default: 1.1)
  request_timeout: 120.0  # Time elapsed until ollama times out the request. Default is 120s. Format is float.

vectorstore:
  database: qdrant

qdrant:
  path: local_data/private_gpt/qdrant
```

## File: `settings-openai.yaml`
```yaml
server:
  env_name: ${APP_ENV:openai}

llm:
  mode: openai

embedding:
  mode: openai

openai:
  api_key: ${OPENAI_API_KEY:}
  model: gpt-3.5-turbo
```

## File: `settings-sagemaker.yaml`
```yaml
server:
  env_name: ${APP_ENV:sagemaker}
  port: ${PORT:8001}

ui:
  enabled: true
  path: /

llm:
  mode: sagemaker

embedding:
  mode: sagemaker

sagemaker:
  llm_endpoint_name: llm
  embedding_endpoint_name: embedding
```

## File: `settings-test.yaml`
```yaml
server:
  env_name: test
  auth:
    enabled: false
    # Dummy secrets used for tests
    secret: "foo bar; dummy secret"

data:
  local_data_folder: local_data/tests

qdrant:
  path: local_data/tests

llm:
  mode: mock

embedding:
  mode: mock

ui:
  enabled: false
```

## File: `settings-vllm.yaml`
```yaml
server:
  env_name: ${APP_ENV:vllm}

llm:
  mode: openailike
  max_new_tokens: 512
  tokenizer: meta-llama/Meta-Llama-3.1-8B-Instruct
  temperature: 0.1

embedding:
  mode: huggingface
  ingest_mode: simple

huggingface:
  embedding_hf_model_name: nomic-ai/nomic-embed-text-v1.5

openai:
  api_base: http://localhost:8000/v1
  api_key: EMPTY
  model: facebook/opt-125m
  request_timeout: 600.0
```

## File: `settings.yaml`
```yaml
# The default configuration file.
# More information about configuration can be found in the documentation: https://docs.privategpt.dev/
# Syntax in `private_pgt/settings/settings.py`
server:
  env_name: ${APP_ENV:prod}
  port: ${PORT:8001}
  cors:
    enabled: true
    allow_origins: ["*"]
    allow_methods: ["*"]
    allow_headers: ["*"]
  auth:
    enabled: false
    # python -c 'import base64; print("Basic " + base64.b64encode("secret:key".encode()).decode())'
    # 'secret' is the username and 'key' is the password for basic auth by default
    # If the auth is enabled, this value must be set in the "Authorization" header of the request.
    secret: "Basic c2VjcmV0OmtleQ=="

data:
  local_ingestion:
    enabled: ${LOCAL_INGESTION_ENABLED:false}
    allow_ingest_from: ["*"]
  local_data_folder: local_data/private_gpt

ui:
  enabled: true
  path: /
  # "RAG", "Search", "Basic", or "Summarize"
  default_mode: "RAG"
  default_chat_system_prompt: >
    You are a helpful, respectful and honest assistant.
    Always answer as helpfully as possible and follow ALL given instructions.
    Do not speculate or make up information.
    Do not reference any given instructions or context.
  default_query_system_prompt: >
    You can only answer questions about the provided context.
    If you know the answer but it is not based in the provided context, don't provide
    the answer, just state the answer is not in the context provided.
  default_summarization_system_prompt: >
    Provide a comprehensive summary of the provided context information.
    The summary should cover all the key points and main ideas presented in
    the original text, while also condensing the information into a concise
    and easy-to-understand format. Please ensure that the summary includes
    relevant details and examples that support the main ideas, while avoiding
    any unnecessary information or repetition.
  delete_file_button_enabled: true
  delete_all_files_button_enabled: true

llm:
  mode: llamacpp
  prompt_style: "llama3"
  # Should be matching the selected model
  max_new_tokens: 512
  context_window: 3900
  # Select your tokenizer. Llama-index tokenizer is the default.
  # tokenizer: meta-llama/Meta-Llama-3.1-8B-Instruct
  temperature: 0.1      # The temperature of the model. Increasing the temperature will make the model answer more creatively. A value of 0.1 would be more factual. (Default: 0.1)

rag:
  similarity_top_k: 2
  #This value controls how many "top" documents the RAG returns to use in the context.
  #similarity_value: 0.45
  #This value is disabled by default.  If you enable this settings, the RAG will only use articles that meet a certain percentage score.
  rerank:
    enabled: false
    model: cross-encoder/ms-marco-MiniLM-L-2-v2
    top_n: 1

summarize:
  use_async: true

clickhouse:
    host: localhost
    port: 8443
    username: admin
    password: clickhouse
    database: embeddings

llamacpp:
  llm_hf_repo_id: lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF
  llm_hf_model_file: Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
  tfs_z: 1.0            # Tail free sampling is used to reduce the impact of less probable tokens from the output. A higher value (e.g., 2.0) will reduce the impact more, while a value of 1.0 disables this setting
  top_k: 40             # Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative. (Default: 40)
  top_p: 1.0            # Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text. (Default: 0.9)
  repeat_penalty: 1.1   # Sets how strongly to penalize repetitions. A higher value (e.g., 1.5) will penalize repetitions more strongly, while a lower value (e.g., 0.9) will be more lenient. (Default: 1.1)

embedding:
  # Should be matching the value above in most cases
  mode: huggingface
  ingest_mode: simple
  embed_dim: 768 # 768 is for nomic-ai/nomic-embed-text-v1.5

huggingface:
  embedding_hf_model_name: nomic-ai/nomic-embed-text-v1.5
  access_token: ${HF_TOKEN:}
  # Warning: Enabling this option will allow the model to download and execute code from the internet.
  # Nomic AI requires this option to be enabled to use the model, be aware if you are using a different model.
  trust_remote_code: true

vectorstore:
  database: qdrant

nodestore:
  database: simple

milvus:
  uri: local_data/private_gpt/milvus/milvus_local.db
  collection_name: milvus_db
  overwrite: false

qdrant:
  path: local_data/private_gpt/qdrant

postgres:
  host: localhost
  port: 5432
  database: postgres
  user: postgres
  password: postgres
  schema_name: private_gpt

sagemaker:
  llm_endpoint_name: huggingface-pytorch-tgi-inference-2023-09-25-19-53-32-140
  embedding_endpoint_name: huggingface-pytorch-inference-2023-11-03-07-41-36-479

openai:
  api_key: ${OPENAI_API_KEY:}
  model: gpt-3.5-turbo
  embedding_api_key: ${OPENAI_API_KEY:}

ollama:
  llm_model: llama3.1
  embedding_model: nomic-embed-text
  api_base: http://localhost:11434
  embedding_api_base: http://localhost:11434  # change if your embedding model runs on another ollama
  keep_alive: 5m
  request_timeout: 120.0
  autopull_models: true

azopenai:
  api_key: ${AZ_OPENAI_API_KEY:}
  azure_endpoint: ${AZ_OPENAI_ENDPOINT:}
  embedding_deployment_name: ${AZ_OPENAI_EMBEDDING_DEPLOYMENT_NAME:}
  llm_deployment_name: ${AZ_OPENAI_LLM_DEPLOYMENT_NAME:}
  api_version: "2023-05-15"
  embedding_model: text-embedding-ada-002
  llm_model: gpt-35-turbo

gemini:
  api_key: ${GOOGLE_API_KEY:}
  model: models/gemini-pro
  embedding_model: models/embedding-001
```

## File: `version.txt`
```
0.6.2
```

## File: `fern/README.md`
```markdown
# Documentation of PrivateGPT

The documentation of this project is being rendered thanks to [fern](https://github.com/fern-api/fern).

Fern is basically transforming your `.md` and `.mdx` files into a static website: your documentation.

The configuration of your documentation is done in the `./docs.yml` file.
There, you can configure the navbar, tabs, sections and pages being rendered.

The documentation of fern (and the syntax of its configuration `docs.yml`) is 
available there [docs.buildwithfern.com](https://docs.buildwithfern.com/).

## How to run fern

**You cannot render your documentation locally without fern credentials.**

To see how your documentation looks like, you **have to** use the CICD of this
repository (by opening a PR, CICD job will be executed, and a preview of 
your PR's documentation will be deployed in vercel automatically, through fern).

The only thing you can do locally, is to run `fern check`, which check the syntax of
your `docs.yml` file.

## How to add a new page
Add in the `docs.yml` a new `page`, with the following syntax:

```yml
navigation:
  # ...
  - tab: my-existing-tab
    layout:
      # ...
      - section: My Existing Section
        contents:
          # ...
          - page: My new page display name
            # The path of the page, relative to `fern/`
            path: ./docs/pages/my-existing-tab/new-page-content.mdx
```
```

## File: `fern/docs.yml`
```yaml
# Main Fern configuration file
instances:
  - url: privategpt.docs.buildwithfern.com
    custom-domain: docs.privategpt.dev

title: PrivateGPT | Docs

# The tabs definition, in the top left corner
tabs:
  overview:
    display-name: Overview
    icon: "fa-solid fa-home"
  quickstart:
    display-name: Quickstart
    icon: "fa-solid fa-rocket"
  installation:
    display-name: Installation
    icon: "fa-solid fa-download"
  manual:
    display-name: Manual
    icon: "fa-solid fa-book"
  recipes:
    display-name: Recipes
    icon: "fa-solid fa-flask"
  api-reference:
    display-name: API Reference
    icon: "fa-solid fa-file-contract"

# Definition of tabs contents, will be displayed on the left side of the page, below all tabs
navigation:
  # The default tab
  - tab: overview
    layout:
      - section: Welcome
        contents:
          - page: Introduction
            path: ./docs/pages/overview/welcome.mdx
  - tab: quickstart
    layout:
      - section: Getting started
        contents:
          - page: Quickstart
            path: ./docs/pages/quickstart/quickstart.mdx
  # How to install PrivateGPT, with FAQ and troubleshooting
  - tab: installation
    layout:
      - section: Getting started
        contents:
          - page: Main Concepts
            path: ./docs/pages/installation/concepts.mdx
          - page: Installation
            path: ./docs/pages/installation/installation.mdx
          - page: Troubleshooting
            path: ./docs/pages/installation/troubleshooting.mdx
  # Manual of PrivateGPT: how to use it and configure it
  - tab: manual
    layout:
      - section: General configuration
        contents:
          - page: Configuration
            path: ./docs/pages/manual/settings.mdx
      - section: Document management
        contents:
          - page: Ingestion
            path: ./docs/pages/manual/ingestion.mdx
          - page: Deletion
            path: ./docs/pages/manual/ingestion-reset.mdx
      - section: Storage
        contents:
          - page: Vector Stores
            path: ./docs/pages/manual/vectordb.mdx
          - page: Node Stores
            path: ./docs/pages/manual/nodestore.mdx
      - section: Advanced Setup
        contents:
          - page: LLM Backends
            path: ./docs/pages/manual/llms.mdx
          - page: Reranking
            path: ./docs/pages/manual/reranker.mdx
      - section: User Interface
        contents:
          - page: Gradio Manual
            path: ./docs/pages/ui/gradio.mdx
          - page: Alternatives
            path: ./docs/pages/ui/alternatives.mdx
  - tab: recipes
    layout:
      - section: Getting started
        contents:
          - page: Quickstart
            path: ./docs/pages/recipes/quickstart.mdx
      - section: General use cases
        contents:
          - page: Summarize
            path: ./docs/pages/recipes/summarize.mdx
  # More advanced usage of PrivateGPT, by API
  - tab: api-reference
    layout:
      - section: Overview
        contents:
          - page : API Reference overview
            path: ./docs/pages/api-reference/api-reference.mdx
          - page: SDKs
            path: ./docs/pages/api-reference/sdks.mdx
      - api: API Reference

# Definition of the navbar, will be displayed in the top right corner.
# `type:primary` is always displayed at the most right side of the navbar
navbar-links:
  - type: secondary
    text: Contact us
    url: "mailto:hello@zylon.ai"
  - type: github
    value: "https://github.com/zylon-ai/private-gpt"
  - type: primary
    text: Join the Discord
    url: https://discord.com/invite/bK6mRVpErU

colors:
  accentPrimary:
    dark: "#C6BBFF"
    light: "#756E98"

logo:
  dark: ./docs/assets/logo_light.png
  light: ./docs/assets/logo_dark.png
  height: 50

favicon: ./docs/assets/favicon.ico
```

## File: `fern/fern.config.json`
```json
{
  "organization": "privategpt",
  "version": "0.31.17"
}
```

## File: `fern/generators.yml`
```yaml
groups:
  public:
    generators:
      - name: fernapi/fern-python-sdk
        version: 0.6.2
        output:
          location: local-file-system
          path: ../../pgpt-sdk/python
```

## File: `fern/docs/pages/api-reference/api-reference.mdx`
```
# API Reference

The API is divided in two logical blocks:

1. High-level API, abstracting all the complexity of a RAG (Retrieval Augmented Generation) pipeline implementation:
    - Ingestion of documents: internally managing document parsing, splitting, metadata extraction,
      embedding generation and storage.
    - Chat & Completions using context from ingested documents: abstracting the retrieval of context, the prompt
      engineering and the response generation.

2. Low-level API, allowing advanced users to implement their own complex pipelines:
    - Embeddings generation: based on a piece of text.
    - Contextual chunks retrieval: given a query, returns the most relevant chunks of text from the ingested
      documents.
```

## File: `fern/docs/pages/api-reference/sdks.mdx`
```
We use [Fern](www.buildwithfern.com) to offer API clients for Node.js, Python, Go, and Java.
We recommend using these clients to interact with our endpoints.
The clients are kept up to date automatically, so we encourage you to use the latest version.

## SDKs

*Coming soon!*

<Cards>
  <Card
    title="TypeScript"
    icon="fa-brands fa-node"
    href="https://github.com/zylon-ai/privategpt-ts"
  />
  <Card
    title="Python"
    icon="fa-brands fa-python"
    href="https://github.com/zylon-ai/pgpt-python"
  />
  <br />
</Cards>

<br />

<Cards>
  <Card
    title="Java - WIP"
    icon="fa-brands fa-java"
    href="https://github.com/zylon-ai/private-gpt-java"
  />
  <Card
    title="Go - WIP"
    icon="fa-brands fa-golang"
    href="https://github.com/zylon-ai/private-gpt-go"
  />
</Cards>

<br />
```

## File: `fern/docs/pages/installation/concepts.mdx`
```
PrivateGPT is a service that wraps a set of AI RAG primitives in a comprehensive set of APIs providing a private, secure, customizable and easy to use GenAI development framework.

It uses FastAPI and LLamaIndex as its core frameworks. Those can be customized by changing the codebase itself.

It supports a variety of LLM providers, embeddings providers, and vector stores, both local and remote. Those can be easily changed without changing the codebase.

# Different Setups support

## Setup configurations available
You get to decide the setup for these 3 main components:
- **LLM**: the large language model provider used for inference. It can be local, or remote, or even OpenAI.
- **Embeddings**: the embeddings provider used to encode the input, the documents and the users' queries. Same as the LLM, it can be local, or remote, or even OpenAI.
- **Vector store**: the store used to index and retrieve the documents.

There is an extra component that can be enabled or disabled: the UI. It is a Gradio UI that allows to interact with the API in a more user-friendly way.

<Callout intent = "warning">
A working **Gradio UI client** is provided to test the API, together with a set of useful tools such as bulk
model download script, ingestion script, documents folder watch, etc. Please refer to the [UI alternatives](/manual/user-interface/alternatives) page for more UI alternatives.
</Callout>

### Setups and Dependencies
Your setup will be the combination of the different options available. You'll find recommended setups in the [installation](./installation) section.
PrivateGPT uses poetry to manage its dependencies. You can install the dependencies for the different setups by running `poetry install --extras "<extra1> <extra2>..."`.
Extras are the different options available for each component. For example, to install the dependencies for a a local setup with UI and qdrant as vector database, Ollama as LLM and local embeddings, you would run:

```bash
poetry install --extras "ui vector-stores-qdrant llms-ollama embeddings-ollama"
```

Refer to the [installation](./installation) section for more details.

### Setups and Configuration
PrivateGPT uses yaml to define its configuration in files named `settings-<profile>.yaml`.
Different configuration files can be created in the root directory of the project.
PrivateGPT will load the configuration at startup from the profile specified in the `PGPT_PROFILES` environment variable.
For example, running:
```bash
PGPT_PROFILES=ollama make run
```
will load the configuration from `settings.yaml` and `settings-ollama.yaml`.
- `settings.yaml` is always loaded and contains the default configuration.
- `settings-ollama.yaml` is loaded if the `ollama` profile is specified in the `PGPT_PROFILES` environment variable. It can override configuration from the default `settings.yaml`

## About Fully Local Setups
In order to run PrivateGPT in a fully local setup, you will need to run the LLM, Embeddings and Vector Store locally.

### LLM
For local LLM there are two options:
* (Recommended) You can use the 'ollama' option in PrivateGPT, which will connect to your local Ollama instance. Ollama simplifies a lot the installation of local LLMs.
* You can use the 'llms-llama-cpp' option in PrivateGPT, which will use LlamaCPP. It works great on Mac with Metal most of the times (leverages Metal GPU), but it can be tricky in certain Linux and Windows distributions, depending on the GPU. In the installation document you'll find guides and troubleshooting.

In order for LlamaCPP powered LLM to work (the second option), you need to download the LLM model to the `models` folder. You can do so by running the `setup` script:
```bash
poetry run python scripts/setup
```
### Embeddings
For local Embeddings there are two options:
* (Recommended) You can use the 'ollama' option in PrivateGPT, which will connect to your local Ollama instance. Ollama simplifies a lot the installation of local LLMs.
* You can use the 'embeddings-huggingface' option in PrivateGPT, which will use HuggingFace.

In order for HuggingFace LLM to work (the second option), you need to download the embeddings model to the `models` folder. You can do so by running the `setup` script:
```bash
poetry run python scripts/setup
```
### Vector stores
The vector stores supported (Qdrant, Milvus, ChromaDB and Postgres) run locally by default.
```

## File: `fern/docs/pages/installation/installation.mdx`
```
It is important that you review the [Main Concepts](../concepts) section to understand the different components of PrivateGPT and how they interact with each other.

## Base requirements to run PrivateGPT

### 1. Clone the PrivateGPT Repository
Clone the repository and navigate to it:
```bash
git clone https://github.com/zylon-ai/private-gpt
cd private-gpt
```

### 2. Install Python 3.11
If you do not have Python 3.11 installed, install it using a Python version manager like `pyenv`. Earlier Python versions are not supported.
#### macOS/Linux
Install and set Python 3.11 using [pyenv](https://github.com/pyenv/pyenv):
```bash
pyenv install 3.11
pyenv local 3.11
```
#### Windows
Install and set Python 3.11 using [pyenv-win](https://github.com/pyenv-win/pyenv-win):
```bash
pyenv install 3.11
pyenv local 3.11
```

### 3. Install `Poetry`
Install [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) for dependency management:
Follow the instructions on the official Poetry website to install it.

<Callout intent="warning">
A bug exists in Poetry versions 1.7.0 and earlier. We strongly recommend upgrading to a tested version.
To upgrade Poetry to latest tested version, run `poetry self update 1.8.3` after installing it.
</Callout>

### 4. Optional: Install `make`
To run various scripts, you need to install `make`. Follow the instructions for your operating system:
#### macOS
(Using Homebrew):
```bash
brew install make
```
#### Windows
(Using Chocolatey):
```bash
choco install make
```

## Install and Run Your Desired Setup

PrivateGPT allows customization of the setup, from fully local to cloud-based, by deciding the modules to use. To install only the required dependencies, PrivateGPT offers different `extras` that can be combined during the installation process:

```bash
poetry install --extras "<extra1> <extra2>..."
```
Where `<extra>` can be any of the following options described below.

### Available Modules

You need to choose one option per category (LLM, Embeddings, Vector Stores, UI). Below are the tables listing the available options for each category.

#### LLM

| **Option**   | **Description**                                                        | **Extra**           |
|--------------|------------------------------------------------------------------------|---------------------|
| **ollama**   | Adds support for Ollama LLM, requires Ollama running locally           | llms-ollama         |
| llama-cpp    | Adds support for local LLM using LlamaCPP                              | llms-llama-cpp      |
| sagemaker    | Adds support for Amazon Sagemaker LLM, requires Sagemaker endpoints    | llms-sagemaker      |
| openai       | Adds support for OpenAI LLM, requires OpenAI API key                   | llms-openai         |
| openailike   | Adds support for 3rd party LLM providers compatible with OpenAI's API  | llms-openai-like    |
| azopenai     | Adds support for Azure OpenAI LLM, requires Azure endpoints            | llms-azopenai       |
| gemini       | Adds support for Gemini LLM, requires Gemini API key                   | llms-gemini         |

#### Embeddings

| **Option**       | **Description**                                                                | **Extra**               |
|------------------|--------------------------------------------------------------------------------|-------------------------|
| **ollama**       | Adds support for Ollama Embeddings, requires Ollama running locally            | embeddings-ollama       |
| huggingface      | Adds support for local Embeddings using HuggingFace                            | embeddings-huggingface  |
| openai           | Adds support for OpenAI Embeddings, requires OpenAI API key                    | embeddings-openai       |
| sagemaker        | Adds support for Amazon Sagemaker Embeddings, requires Sagemaker endpoints     | embeddings-sagemaker    |
| azopenai         | Adds support for Azure OpenAI Embeddings, requires Azure endpoints             | embeddings-azopenai     |
| gemini           | Adds support for Gemini Embeddings, requires Gemini API key                    | embeddings-gemini       |

#### Vector Stores

| **Option**       | **Description**                         | **Extra**               |
|------------------|-----------------------------------------|-------------------------|
| **qdrant**       | Adds support for Qdrant vector store    | vector-stores-qdrant    |
| milvus           | Adds support for Milvus vector store    | vector-stores-milvus    |
| chroma           | Adds support for Chroma DB vector store | vector-stores-chroma    |
| postgres         | Adds support for Postgres vector store  | vector-stores-postgres  |
| clickhouse       | Adds support for Clickhouse vector store| vector-stores-clickhouse|

#### UI

| **Option**   | **Description**                          | **Extra** |
|--------------|------------------------------------------|-----------|
| Gradio       | Adds support for UI using Gradio         | ui        |

<Callout intent = "warning">
A working **Gradio UI client** is provided to test the API, together with a set of useful tools such as bulk
model download script, ingestion script, documents folder watch, etc. Please refer to the [UI alternatives](/manual/user-interface/alternatives) page for more UI alternatives.
</Callout>

## Recommended Setups

There are just some examples of recommended setups. You can mix and match the different options to fit your needs.
You'll find more information in the Manual section of the documentation.

> **Important for Windows**: In the examples below or how to run PrivateGPT with `make run`, `PGPT_PROFILES` env var is being set inline following Unix command line syntax (works on MacOS and Linux).
If you are using Windows, you'll need to set the env var in a different way, for example:

```powershell
# Powershell
$env:PGPT_PROFILES="ollama"
make run
```

or

```cmd
# CMD
set PGPT_PROFILES=ollama
make run
```

Refer to the [troubleshooting](./troubleshooting) section for specific issues you might encounter.

### Local, Ollama-powered setup - RECOMMENDED

**The easiest way to run PrivateGPT fully locally** is to depend on Ollama for the LLM. Ollama provides local LLM and Embeddings super easy to install and use, abstracting the complexity of GPU support. It's the recommended setup for local development.

Go to [ollama.ai](https://ollama.ai/) and follow the instructions to install Ollama on your machine.

After the installation, make sure the Ollama desktop app is closed.

Now, start Ollama service (it will start a local inference server, serving both the LLM and the Embeddings):
```bash
ollama serve
```

Install the models to be used, the default settings-ollama.yaml is configured to user llama3.1 8b LLM (~4GB) and nomic-embed-text Embeddings (~275MB)

By default, PGPT will automatically pull models as needed. This behavior can be changed by modifying the `ollama.autopull_models` property.

In any case, if you want to manually pull models, run the following commands:

```bash
ollama pull llama3.1
ollama pull nomic-embed-text
```

Once done, on a different terminal, you can install PrivateGPT with the following command:
```bash
poetry install --extras "ui llms-ollama embeddings-ollama vector-stores-qdrant"
```

Once installed, you can run PrivateGPT. Make sure you have a working Ollama running locally before running the following command.

```bash
PGPT_PROFILES=ollama make run
```

PrivateGPT will use the already existing `settings-ollama.yaml` settings file, which is already configured to use Ollama LLM and Embeddings, and Qdrant. Review it and adapt it to your needs (different models, different Ollama port, etc.)

The UI will be available at http://localhost:8001

### Private, Sagemaker-powered setup

If you need more performance, you can run a version of PrivateGPT that relies on powerful AWS Sagemaker machines to serve the LLM and Embeddings.

You need to have access to sagemaker inference endpoints for the LLM and / or the embeddings, and have AWS credentials properly configured.

Edit the `settings-sagemaker.yaml` file to include the correct Sagemaker endpoints.

Then, install PrivateGPT with the following command:
```bash
poetry install --extras "ui llms-sagemaker embeddings-sagemaker vector-stores-qdrant"
```

Once installed, you can run PrivateGPT. Make sure you have a working Ollama running locally before running the following command.

```bash
PGPT_PROFILES=sagemaker make run
```

PrivateGPT will use the already existing `settings-sagemaker.yaml` settings file, which is already configured to use Sagemaker LLM and Embeddings endpoints, and Qdrant.

The UI will be available at http://localhost:8001

### Non-Private, OpenAI-powered test setup

If you want to test PrivateGPT with OpenAI's LLM and Embeddings -taking into account your data is going to OpenAI!- you can run the following command:

You need an OPENAI API key to run this setup.

Edit the `settings-openai.yaml` file to include the correct API KEY. Never commit it! It's a secret! As an alternative to editing `settings-openai.yaml`, you can just set the env var OPENAI_API_KEY.

Then, install PrivateGPT with the following command:
```bash
poetry install --extras "ui llms-openai embeddings-openai vector-stores-qdrant"
```

Once installed, you can run PrivateGPT.

```bash
PGPT_PROFILES=openai make run
```

PrivateGPT will use the already existing `settings-openai.yaml` settings file, which is already configured to use OpenAI LLM and Embeddings endpoints, and Qdrant.

The UI will be available at http://localhost:8001

### Non-Private, Azure OpenAI-powered test setup

If you want to test PrivateGPT with Azure OpenAI's LLM and Embeddings -taking into account your data is going to Azure OpenAI!- you can run the following command:

You need to have access to Azure OpenAI inference endpoints for the LLM and / or the embeddings, and have Azure OpenAI credentials properly configured.

Edit the `settings-azopenai.yaml` file to include the correct Azure OpenAI endpoints.

Then, install PrivateGPT with the following command:
```bash
poetry install --extras "ui llms-azopenai embeddings-azopenai vector-stores-qdrant"
```

Once installed, you can run PrivateGPT.

```bash
PGPT_PROFILES=azopenai make run
```

PrivateGPT will use the already existing `settings-azopenai.yaml` settings file, which is already configured to use Azure OpenAI LLM and Embeddings endpoints, and Qdrant.

The UI will be available at http://localhost:8001

### Local, Llama-CPP powered setup

If you want to run PrivateGPT fully locally without relying on Ollama, you can run the following command:

```bash
poetry install --extras "ui llms-llama-cpp embeddings-huggingface vector-stores-qdrant"
```

In order for local LLM and embeddings to work, you need to download the models to the `models` folder. You can do so by running the `setup` script:
```bash
poetry run python scripts/setup
```

Once installed, you can run PrivateGPT with the following command:

```bash
PGPT_PROFILES=local make run
```

PrivateGPT will load the already existing `settings-local.yaml` file, which is already configured to use LlamaCPP LLM, HuggingFace embeddings and Qdrant.

The UI will be available at http://localhost:8001

#### Llama-CPP support

For PrivateGPT to run fully locally without Ollama, Llama.cpp is required and in
particular [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
is used.

You'll need to have a valid C++ compiler like gcc installed. See [Troubleshooting: C++ Compiler](#troubleshooting-c-compiler) for more details.

> It's highly encouraged that you fully read llama-cpp and llama-cpp-python documentation relevant to your platform.
> Running into installation issues is very likely, and you'll need to troubleshoot them yourself.

##### Llama-CPP OSX GPU support

You will need to build [llama.cpp](https://github.com/ggerganov/llama.cpp) with metal support.

To do that, you need to install `llama.cpp` python's binding `llama-cpp-python` through pip, with the compilation flag
that activate `METAL`: you have to pass `-DLLAMA_METAL=on` to the CMake command tha `pip` runs for you (see below).

In other words, one should simply run:
```bash
CMAKE_ARGS="-DLLAMA_METAL=on" pip install --force-reinstall --no-cache-dir llama-cpp-python
```

The above command will force the re-installation of `llama-cpp-python` with `METAL` support by compiling
`llama.cpp` locally with your `METAL` libraries (shipped by default with your macOS).

More information is available in the documentation of the libraries themselves:
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python#installation-with-hardware-acceleration)
* [llama-cpp-python's documentation](https://llama-cpp-python.readthedocs.io/en/latest/#installation-with-hardware-acceleration)
* [llama.cpp](https://github.com/ggerganov/llama.cpp#build)

##### Llama-CPP Windows NVIDIA GPU support

Windows GPU support is done through CUDA.
Follow the instructions on the original [llama.cpp](https://github.com/ggerganov/llama.cpp) repo to install the required
dependencies.

Some tips to get it working with an NVIDIA card and CUDA (Tested on Windows 10 with CUDA 11.5 RTX 3070):

* Install latest VS2022 (and build tools) https://visualstudio.microsoft.com/vs/community/
* Install CUDA toolkit https://developer.nvidia.com/cuda-downloads
* Verify your installation is correct by running `nvcc --version` and `nvidia-smi`, ensure your CUDA version is up to
  date and your GPU is detected.
* [Optional] Install CMake to troubleshoot building issues by compiling llama.cpp directly https://cmake.org/download/

If you have all required dependencies properly configured running the
following powershell command should succeed.

```powershell
$env:CMAKE_ARGS='-DLLAMA_CUBLAS=on'; poetry run pip install --force-reinstall --no-cache-dir llama-cpp-python numpy==1.26.0
```

If your installation was correct, you should see a message similar to the following next
time you start the server `BLAS = 1`. If there is some issue, please refer to the
[troubleshooting](/installation/getting-started/troubleshooting#building-llama-cpp-with-nvidia-gpu-support) section.

```console
llama_new_context_with_model: total VRAM used: 4857.93 MB (model: 4095.05 MB, context: 762.87 MB)
AVX = 1 | AVX2 = 1 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 1 | NEON = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 1 | SSE3 = 1 | SSSE3 = 0 | VSX = 0 |
```

Note that llama.cpp offloads matrix calculations to the GPU but the performance is
still hit heavily due to latency between CPU and GPU communication. You might need to tweak
batch sizes and other parameters to get the best performance for your particular system.

##### Llama-CPP Linux NVIDIA GPU support and Windows-WSL

Linux GPU support is done through CUDA.
Follow the instructions on the original [llama.cpp](https://github.com/ggerganov/llama.cpp) repo to install the required
external
dependencies.

Some tips:

* Make sure you have an up-to-date C++ compiler
* Install CUDA toolkit https://developer.nvidia.com/cuda-downloads
* Verify your installation is correct by running `nvcc --version` and `nvidia-smi`, ensure your CUDA version is up to
  date and your GPU is detected.

After that running the following command in the repository will install llama.cpp with GPU support:

```bash
CMAKE_ARGS='-DLLAMA_CUBLAS=on' poetry run pip install --force-reinstall --no-cache-dir llama-cpp-python numpy==1.26.0
```

If your installation was correct, you should see a message similar to the following next
time you start the server `BLAS = 1`. If there is some issue, please refer to the
[troubleshooting](/installation/getting-started/troubleshooting#building-llama-cpp-with-nvidia-gpu-support) section.

```
llama_new_context_with_model: total VRAM used: 4857.93 MB (model: 4095.05 MB, context: 762.87 MB)
AVX = 1 | AVX2 = 1 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 1 | NEON = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 1 | SSE3 = 1 | SSSE3 = 0 | VSX = 0 |
```

##### Llama-CPP Linux AMD GPU support

Linux GPU support is done through ROCm.
Some tips:
* Install ROCm from [quick-start install guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html)
* [Install PyTorch for ROCm](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/install-pytorch.html)
```bash
wget https://repo.radeon.com/rocm/manylinux/rocm-rel-6.0/torch-2.1.1%2Brocm6.0-cp311-cp311-linux_x86_64.whl
poetry run pip install --force-reinstall --no-cache-dir torch-2.1.1+rocm6.0-cp311-cp311-linux_x86_64.whl
```
* Install bitsandbytes for ROCm
```bash
PYTORCH_ROCM_ARCH=gfx900,gfx906,gfx908,gfx90a,gfx1030,gfx1100,gfx1101,gfx940,gfx941,gfx942
BITSANDBYTES_VERSION=62353b0200b8557026c176e74ac48b84b953a854
git clone https://github.com/arlo-phoenix/bitsandbytes-rocm-5.6
cd bitsandbytes-rocm-5.6
git checkout ${BITSANDBYTES_VERSION}
make hip ROCM_TARGET=${PYTORCH_ROCM_ARCH} ROCM_HOME=/opt/rocm/
pip install . --extra-index-url https://download.pytorch.org/whl/nightly
```

After that running the following command in the repository will install llama.cpp with GPU support:
```bash
LLAMA_CPP_PYTHON_VERSION=0.2.56
DAMDGPU_TARGETS=gfx900;gfx906;gfx908;gfx90a;gfx1030;gfx1100;gfx1101;gfx940;gfx941;gfx942
CMAKE_ARGS="-DLLAMA_HIPBLAS=ON -DCMAKE_C_COMPILER=/opt/rocm/llvm/bin/clang -DCMAKE_CXX_COMPILER=/opt/rocm/llvm/bin/clang++ -DAMDGPU_TARGETS=${DAMDGPU_TARGETS}" poetry run pip install --force-reinstall --no-cache-dir llama-cpp-python==${LLAMA_CPP_PYTHON_VERSION}
```

If your installation was correct, you should see a message similar to the following next time you start the server `BLAS = 1`.

```
AVX = 1 | AVX_VNNI = 0 | AVX2 = 1 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 1 | NEON = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 1 | SSE3 = 1 | SSSE3 = 1 | VSX = 0 | MATMUL_INT8 = 0 |
```

##### Llama-CPP Known issues and Troubleshooting

Execution of LLMs locally still has a lot of sharp edges, specially when running on non Linux platforms.
You might encounter several issues:

* Performance: RAM or VRAM usage is very high, your computer might experience slowdowns or even crashes.
* GPU Virtualization on Windows and OSX: Simply not possible with docker desktop, you have to run the server directly on
  the host.
* Building errors: Some of PrivateGPT dependencies need to build native code, and they might fail on some platforms.
  Most likely you are missing some dev tools in your machine (updated C++ compiler, CUDA is not on PATH, etc.).
  If you encounter any of these issues, please open an issue and we'll try to help.

One of the first reflex to adopt is: get more information.
If, during your installation, something does not go as planned, retry in *verbose* mode, and see what goes wrong.

For example, when installing packages with `pip install`, you can add the option `-vvv` to show the details of the installation.

##### Llama-CPP Troubleshooting: C++ Compiler

If you encounter an error while building a wheel during the `pip install` process, you may need to install a C++
compiler on your computer.

**For Windows 10/11**

To install a C++ compiler on Windows 10/11, follow these steps:

1. Install Visual Studio 2022.
2. Make sure the following components are selected:
    * Universal Windows Platform development
    * C++ CMake tools for Windows
3. Download the MinGW installer from the [MinGW website](https://sourceforge.net/projects/mingw/).
4. Run the installer and select the `gcc` component.

**For OSX**

1. Check if you have a C++ compiler installed, `Xcode` should have done it for you. To install Xcode, go to the App
   Store and search for Xcode and install it. **Or** you can install the command line tools by running `xcode-select --install`.
2. If not, you can install clang or gcc with homebrew `brew install gcc`

##### Llama-CPP Troubleshooting: Mac Running Intel

When running a Mac with Intel hardware (not M1), you may run into _clang: error: the clang compiler does not support '
-march=native'_ during pip install.

If so set your archflags during pip install. eg: _ARCHFLAGS="-arch x86_64" pip3 install -r requirements.txt_
```

## File: `fern/docs/pages/installation/troubleshooting.mdx`
```
# Downloading Gated and Private Models
Many models are gated or private, requiring special access to use them. Follow these steps to gain access and set up your environment for using these models.
## Accessing Gated Models
1. **Request Access:**
   Follow the instructions provided [here](https://huggingface.co/docs/hub/en/models-gated) to request access to the gated model.
2. **Generate a Token:**
   Once you have access, generate a token by following the instructions [here](https://huggingface.co/docs/hub/en/security-tokens).
3. **Set the Token:**
   Add the generated token to your `settings.yaml` file:
   ```yaml
   huggingface:
     access_token: <your-token>
   ```
   Alternatively, set the `HF_TOKEN` environment variable:
   ```bash
   export HF_TOKEN=<your-token>
   ```

# Tokenizer Setup
PrivateGPT uses the `AutoTokenizer` library to tokenize input text accurately. It connects to HuggingFace's API to download the appropriate tokenizer for the specified model.

## Configuring the Tokenizer
1. **Specify the Model:**
   In your `settings.yaml` file, specify the model you want to use:
   ```yaml
   llm:
     tokenizer: meta-llama/Meta-Llama-3.1-8B-Instruct
   ```
2. **Set Access Token for Gated Models:**
   If you are using a gated model, ensure the `access_token` is set as mentioned in the previous section.
This configuration ensures that PrivateGPT can download and use the correct tokenizer for the model you are working with.

# Embedding dimensions mismatch
If you encounter an error message like `Embedding dimensions mismatch`, it is likely due to the embedding model and
current vector dimension mismatch. To resolve this issue, ensure that the model and the input data have the same vector dimensions.

By default, PrivateGPT uses `nomic-embed-text` embeddings, which have a vector dimension of 768.
If you are using a different embedding model, ensure that the vector dimensions match the model's output.

<Callout intent = "warning">
In versions below to 0.6.0, the default embedding model was `BAAI/bge-small-en-v1.5` in `huggingface` setup.
If you plan to reuse the old generated embeddings, you need to update the `settings.yaml` file to use the correct embedding model:
```yaml
huggingface:
  embedding_hf_model_name: BAAI/bge-small-en-v1.5
embedding:
  embed_dim: 384
```
</Callout>

# Building Llama-cpp with NVIDIA GPU support

## Out-of-memory error

If you encounter an out-of-memory error while running `llama-cpp` with CUDA, you can try the following steps to resolve the issue:
1. **Set the next environment:**
    ```bash
    TOKENIZERS_PARALLELISM=true
    ```
2. **Run PrivateGPT:**
    ```bash
    poetry run python -m privategpt
    ```
Give thanks to [MarioRossiGithub](https://github.com/MarioRossiGithub) for providing the following solution.
```

## File: `fern/docs/pages/manual/ingestion-reset.mdx`
```
# Reset Local documents database

When running in a local setup, you can remove all ingested documents by simply
deleting all contents of `local_data` folder (except .gitignore).

To simplify this process, you can use the command:
```bash
make wipe
```

# Advanced usage

You can actually delete your documents from your storage by using the
API endpoint `DELETE` in the Ingestion API.
```

## File: `fern/docs/pages/manual/ingestion.mdx`
```
# Ingesting & Managing Documents

The ingestion of documents can be done in different ways:

* Using the `/ingest` API
* Using the Gradio UI
* Using the Bulk Local Ingestion functionality (check next section)

## Bulk Local Ingestion

You will need to activate `data.local_ingestion.enabled` in your setting file to use this feature. Additionally,
it is probably a good idea to set `data.local_ingestion.allow_ingest_from` to specify which folders are allowed to be ingested.

<Callout intent = "warning">
Be careful enabling this feature in a production environment, as it can be a security risk, as it allows users to
ingest any local file with permissions.
</Callout>

When you are running PrivateGPT in a fully local setup, you can ingest a complete folder for convenience (containing
pdf, text files, etc.)
and optionally watch changes on it with the command:

```bash
make ingest /path/to/folder -- --watch
```

To log the processed and failed files to an additional file, use:

```bash
make ingest /path/to/folder -- --watch --log-file /path/to/log/file.log
```

**Note for Windows Users:** Depending on your Windows version and whether you are using PowerShell to execute
PrivateGPT API calls, you may need to include the parameter name before passing the folder path for consumption:

```bash
make ingest arg=/path/to/folder -- --watch --log-file /path/to/log/file.log
```

After ingestion is complete, you should be able to chat with your documents
by navigating to http://localhost:8001 and using the option `Query documents`,
or using the completions / chat API.

## Ingestion troubleshooting

### Running out of memory

To do not run out of memory, you should ingest your documents without the LLM loaded in your (video) memory.
To do so, you should change your configuration to set `llm.mode: mock`.

You can also use the existing `PGPT_PROFILES=mock` that will set the following configuration for you:

```yaml
llm:
  mode: mock
embedding:
  mode: local
```

This configuration allows you to use hardware acceleration for creating embeddings while avoiding loading the full LLM into (video) memory.

Once your documents are ingested, you can set the `llm.mode` value back to `local` (or your previous custom value).

### Ingestion speed

The ingestion speed depends on the number of documents you are ingesting, and the size of each document.
To speed up the ingestion, you can change the ingestion mode in configuration.

The following ingestion mode exist:
* `simple`: historic behavior, ingest one document at a time, sequentially
* `batch`: read, parse, and embed multiple documents using batches (batch read, and then batch parse, and then batch embed)
* `parallel`: read, parse, and embed multiple documents in parallel. This is the fastest ingestion mode for local setup.
* `pipeline`: Alternative to parallel.
To change the ingestion mode, you can use the `embedding.ingest_mode` configuration value. The default value is `simple`.

To configure the number of workers used for parallel or batched ingestion, you can use
the `embedding.count_workers` configuration value. If you set this value too high, you might run out of
memory, so be mindful when setting this value. The default value is `2`.
For `batch` mode, you can easily set this value to your number of threads available on your CPU without
running out of memory. For `parallel` mode, you should be more careful, and set this value to a lower value.

The configuration below should be enough for users who want to stress more their hardware:
```yaml
embedding:
  ingest_mode: parallel
  count_workers: 4
```

If your hardware is powerful enough, and that you are loading heavy documents, you can increase the number of workers.
It is recommended to do your own tests to find the optimal value for your hardware.

If you have a `bash` shell, you can use this set of command to do your own benchmark:

```bash
# Wipe your local data, to put yourself in a clean state
# This will delete all your ingested documents
make wipe

time PGPT_PROFILES=mock python ./scripts/ingest_folder.py ~/my-dir/to-ingest/
```

## Supported file formats

PrivateGPT by default supports all the file formats that contains clear text (for example, `.txt` files, `.html`, etc.).
However, these text based file formats as only considered as text files, and are not pre-processed in any other way.

It also supports the following file formats:
* `.hwp`
* `.pdf`
* `.docx`
* `.pptx`
* `.ppt`
* `.pptm`
* `.jpg`
* `.png`
* `.jpeg`
* `.mp3`
* `.mp4`
* `.csv`
* `.epub`
* `.md`
* `.mbox`
* `.ipynb`
* `.json`

<Callout intent = "info">
While `PrivateGPT` supports these file formats, it **might** require additional
dependencies to be installed in your python's virtual environment.
For example, if you try to ingest `.epub` files, `PrivateGPT` might fail to do it, and will instead display an
explanatory error asking you to download the necessary dependencies to install this file format.
</Callout>

<Callout intent = "info">
**Other file formats might work**, but they will be considered as plain text
files (in other words, they will be ingested as `.txt` files).
</Callout>

```

## File: `fern/docs/pages/manual/llms.mdx`
```
## Running the Server

PrivateGPT supports running with different LLMs & setups.

### Local models

Both the LLM and the Embeddings model will run locally.

Make sure you have followed the *Local LLM requirements* section before moving on.

This command will start PrivateGPT using the `settings.yaml` (default profile) together with the `settings-local.yaml`
configuration files. By default, it will enable both the API and the Gradio UI. Run:

```bash
PGPT_PROFILES=local make run
```

or

```bash
PGPT_PROFILES=local poetry run python -m private_gpt
```

When the server is started it will print a log *Application startup complete*.
Navigate to http://localhost:8001 to use the Gradio UI or to http://localhost:8001/docs (API section) to try the API
using Swagger UI.

#### Customizing low level parameters

Currently, not all the parameters of `llama.cpp` and `llama-cpp-python` are available at PrivateGPT's `settings.yaml` file.
In case you need to customize parameters such as the number of layers loaded into the GPU, you might change
these at the `llm_component.py` file under the `private_gpt/components/llm/llm_component.py`.

##### Available LLM config options

The `llm` section of the settings allows for the following configurations:

- `mode`: how to run your llm
- `max_new_tokens`: this lets you configure the number of new tokens the LLM will generate and add to the context window (by default Llama.cpp uses `256`)

Example:

```yaml
llm:
  mode: local
  max_new_tokens: 256
```

If you are getting an out of memory error, you might also try a smaller model or stick to the proposed
recommended models, instead of custom tuning the parameters.

### Using OpenAI

If you cannot run a local model (because you don't have a GPU, for example) or for testing purposes, you may
decide to run PrivateGPT using OpenAI as the LLM and Embeddings model.

In order to do so, create a profile `settings-openai.yaml` with the following contents:

```yaml
llm:
  mode: openai

openai:
  api_base: <openai-api-base-url> # Defaults to https://api.openai.com/v1
  api_key: <your_openai_api_key>  # You could skip this configuration and use the OPENAI_API_KEY env var instead
  model: <openai_model_to_use> # Optional model to use. Default is "gpt-3.5-turbo"
                               # Note: Open AI Models are listed here: https://platform.openai.com/docs/models
```

And run PrivateGPT loading that profile you just created:

`PGPT_PROFILES=openai make run`

or

`PGPT_PROFILES=openai poetry run python -m private_gpt`

When the server is started it will print a log *Application startup complete*.
Navigate to http://localhost:8001 to use the Gradio UI or to http://localhost:8001/docs (API section) to try the API.
You'll notice the speed and quality of response is higher, given you are using OpenAI's servers for the heavy
computations.

### Using OpenAI compatible API

Many tools, including [LocalAI](https://localai.io/) and [vLLM](https://docs.vllm.ai/en/latest/),
support serving local models with an OpenAI compatible API. Even when overriding the `api_base`,
using the `openai` mode doesn't allow you to use custom models. Instead, you should use the `openailike` mode:

```yaml
llm:
  mode: openailike
```

This mode uses the same settings as the `openai` mode.

As an example, you can follow the [vLLM quickstart guide](https://docs.vllm.ai/en/latest/getting_started/quickstart.html#openai-compatible-server)
to run an OpenAI compatible server. Then, you can run PrivateGPT using the `settings-vllm.yaml` profile:

`PGPT_PROFILES=vllm make run`

### Using Azure OpenAI

If you cannot run a local model (because you don't have a GPU, for example) or for testing purposes, you may
decide to run PrivateGPT using Azure OpenAI as the LLM and Embeddings model.

In order to do so, create a profile `settings-azopenai.yaml` with the following contents:

```yaml
llm:
  mode: azopenai

embedding:
  mode: azopenai

azopenai:
  api_key: <your_azopenai_api_key>  # You could skip this configuration and use the AZ_OPENAI_API_KEY env var instead
  azure_endpoint: <your_azopenai_endpoint> # You could skip this configuration and use the AZ_OPENAI_ENDPOINT env var instead
  api_version: <api_version> # The API version to use. Default is "2023_05_15"
  embedding_deployment_name: <your_embedding_deployment_name> # You could skip this configuration and use the AZ_OPENAI_EMBEDDING_DEPLOYMENT_NAME env var instead
  embedding_model: <openai_embeddings_to_use> # Optional model to use. Default is "text-embedding-ada-002" 
  llm_deployment_name: <your_model_deployment_name> # You could skip this configuration and use the AZ_OPENAI_LLM_DEPLOYMENT_NAME env var instead
  llm_model: <openai_model_to_use> # Optional model to use. Default is "gpt-35-turbo"
```

And run PrivateGPT loading that profile you just created:

`PGPT_PROFILES=azopenai make run`

or

`PGPT_PROFILES=azopenai poetry run python -m private_gpt`

When the server is started it will print a log *Application startup complete*.
Navigate to http://localhost:8001 to use the Gradio UI or to http://localhost:8001/docs (API section) to try the API.
You'll notice the speed and quality of response is higher, given you are using Azure OpenAI's servers for the heavy
computations.

### Using AWS Sagemaker

For a fully private & performant setup, you can choose to have both your LLM and Embeddings model deployed using Sagemaker.

Note: how to deploy models on Sagemaker is out of the scope of this documentation.

In order to do so, create a profile `settings-sagemaker.yaml` with the following contents (remember to
update the values of the llm_endpoint_name and embedding_endpoint_name to yours):

```yaml
llm:
  mode: sagemaker

sagemaker:
  llm_endpoint_name: huggingface-pytorch-tgi-inference-2023-09-25-19-53-32-140
  embedding_endpoint_name: huggingface-pytorch-inference-2023-11-03-07-41-36-479
```

And run PrivateGPT loading that profile you just created:

`PGPT_PROFILES=sagemaker make run`

or

`PGPT_PROFILES=sagemaker poetry run python -m private_gpt`

When the server is started it will print a log *Application startup complete*.
Navigate to http://localhost:8001 to use the Gradio UI or to http://localhost:8001/docs (API section) to try the API.

### Using Ollama

Another option for a fully private setup is using [Ollama](https://ollama.ai/).

Note: how to deploy Ollama and pull models onto it is out of the scope of this documentation.

In order to do so, create a profile `settings-ollama.yaml` with the following contents:

```yaml
llm:
  mode: ollama

ollama:
  model: <ollama_model_to_use> # Required Model to use.
                               # Note: Ollama Models are listed here: https://ollama.ai/library
                               #       Be sure to pull the model to your Ollama server
  api_base: <ollama-api-base-url> # Defaults to http://localhost:11434
```

And run PrivateGPT loading that profile you just created:

`PGPT_PROFILES=ollama make run`

or

`PGPT_PROFILES=ollama poetry run python -m private_gpt`

When the server is started it will print a log *Application startup complete*.
Navigate to http://localhost:8001 to use the Gradio UI or to http://localhost:8001/docs (API section) to try the API.

### Using IPEX-LLM

For a fully private setup on Intel GPUs (such as a local PC with an iGPU, or discrete GPUs like Arc, Flex, and Max), you can use [IPEX-LLM](https://github.com/intel-analytics/ipex-llm).

To deploy Ollama and pull models using IPEX-LLM, please refer to [this guide](https://ipex-llm.readthedocs.io/en/latest/doc/LLM/Quickstart/ollama_quickstart.html). Then, follow the same steps outlined in the [Using Ollama](#using-ollama) section to create a `settings-ollama.yaml` profile and run the private-GPT server.

### Using Gemini

If you cannot run a local model (because you don't have a GPU, for example) or for testing purposes, you may
decide to run PrivateGPT using Gemini as the LLM and Embeddings model. In addition, you will benefit from
multimodal inputs, such as text and images, in a very large contextual window.

In order to do so, create a profile `settings-gemini.yaml` with the following contents:

```yaml
llm:
  mode: gemini

embedding:
  mode: gemini

gemini:
  api_key: <your_gemini_api_key>                # You could skip this configuration and use the GEMINI_API_KEY env var instead
  model: <gemini_model_to_use>                  # Optional model to use. Default is models/gemini-pro"
  embedding_model: <gemini_embeddings_to_use>   # Optional model to use. Default is "models/embedding-001"
```

And run PrivateGPT loading that profile you just created:

`PGPT_PROFILES=gemini make run`

or

`PGPT_PROFILES=gemini poetry run python -m private_gpt`

When the server is started it will print a log *Application startup complete*.
Navigate to http://localhost:8001 to use the Gradio UI or to http://localhost:8001/docs (API section) to try the API.

```

## File: `fern/docs/pages/manual/nodestore.mdx`
```
## NodeStores
PrivateGPT supports **Simple** and [Postgres](https://www.postgresql.org/) providers. Simple being the default.

In order to select one or the other, set the `nodestore.database` property in the `settings.yaml` file to `simple` or `postgres`.

```yaml
nodestore:
  database: simple
```

### Simple Document Store

Setting up simple document store: Persist data with in-memory and disk storage.

Enabling the simple document store is an excellent choice for small projects or proofs of concept where you need to persist data while maintaining minimal setup complexity. To get started, set the nodestore.database property in your settings.yaml file as follows:

```yaml
nodestore:
  database: simple
```
The beauty of the simple document store is its flexibility and ease of implementation. It provides a solid foundation for managing and retrieving data without the need for complex setup or configuration. The combination of in-memory processing and disk persistence ensures that you can efficiently handle small to medium-sized datasets while maintaining data consistency across runs.

### Postgres Document Store

To enable Postgres, set the `nodestore.database` property in the `settings.yaml` file to `postgres` and install the `storage-nodestore-postgres` extra.  Note: Vector Embeddings Storage in Postgres is configured separately

```bash
poetry install --extras storage-nodestore-postgres
```

The available configuration options are:
| Field         | Description                                               |
|---------------|-----------------------------------------------------------|
| **host**      | The server hosting the Postgres database. Default is `localhost` |
| **port**      | The port on which the Postgres database is accessible. Default is `5432` |
| **database**  | The specific database to connect to. Default is `postgres` |
| **user**      | The username for database access. Default is `postgres` |
| **password**  | The password for database access. (Required)            |
| **schema_name** | The database schema to use. Default is `private_gpt`       |

For example:
```yaml
nodestore:
  database: postgres

postgres:
  host: localhost
  port: 5432
  database: postgres
  user: postgres
  password: <PASSWORD>
  schema_name: private_gpt
```

Given the above configuration, Two PostgreSQL tables will be created upon successful connection: one for storing metadata related to the index and another for document data itself.

```
postgres=# \dt private_gpt.*
                  List of relations
   Schema    |      Name       | Type  |    Owner     
-------------+-----------------+-------+--------------
 private_gpt | data_docstore   | table | postgres
 private_gpt | data_indexstore | table | postgres

postgres=# 
```
```

## File: `fern/docs/pages/manual/reranker.mdx`
```
## Enhancing Response Quality with Reranking

PrivateGPT offers a reranking feature aimed at optimizing response generation by filtering out irrelevant documents, potentially leading to faster response times and enhanced relevance of answers generated by the LLM.

### Enabling Reranking

Document reranking can significantly improve the efficiency and quality of the responses by pre-selecting the most relevant documents before generating an answer. To leverage this feature, ensure that it is enabled in the RAG settings and consider adjusting the parameters to best fit your use case.

#### Additional Requirements

Before enabling reranking, you must install additional dependencies:

```bash
poetry install --extras rerank-sentence-transformers
```

This command installs dependencies for the cross-encoder reranker from sentence-transformers, which is currently the only supported method by PrivateGPT for document reranking.

#### Configuration

To enable and configure reranking, adjust the `rag` section within the `settings.yaml` file. Here are the key settings to consider:

- `similarity_top_k`: Determines the number of documents to initially retrieve and consider for reranking. This value should be larger than `top_n`.
- `rerank`:
  - `enabled`: Set to `true` to activate the reranking feature.
  - `top_n`: Specifies the number of documents to use in the final answer generation process, chosen from the top-ranked documents provided by `similarity_top_k`.

Example configuration snippet:

```yaml
rag:
  similarity_top_k: 10  # Number of documents to retrieve and consider for reranking
  rerank:
    enabled: true
    top_n: 3  # Number of top-ranked documents to use for generating the answer
```
```

## File: `fern/docs/pages/manual/settings.mdx`
```
# Settings and profiles for your private GPT

The configuration of your private GPT server is done thanks to `settings` files (more precisely `settings.yaml`).
These text files are written using the [YAML](https://en.wikipedia.org/wiki/YAML) syntax.

While PrivateGPT is distributing safe and universal configuration files, you might want to quickly customize your
PrivateGPT, and this can be done using the `settings` files.

This project is defining the concept of **profiles** (or configuration profiles).
This mechanism, using your environment variables, is giving you the ability to easily switch between
configuration you've made.

A typical use case of profile is to easily switch between LLM and embeddings.
To be a bit more precise, you can change the language (to French, Spanish, Italian, English, etc) by simply changing
the profile you've selected; no code changes required!

PrivateGPT is configured through *profiles* that are defined using yaml files, and selected through env variables.
The full list of properties configurable can be found in `settings.yaml`.

## How to know which profiles exist
Given that a profile `foo_bar` points to the file `settings-foo_bar.yaml` and vice-versa, you simply have to look
at the files starting with `settings` and ending in `.yaml`.

## How to use an existing profiles
**Please note that the syntax to set the value of an environment variables depends on your OS**.
You have to set environment variable `PGPT_PROFILES` to the name of the profile you want to use.

For example, on **linux and macOS**, this gives:
```bash
export PGPT_PROFILES=my_profile_name_here
```

Windows Command Prompt (cmd) has a different syntax:
```shell
set PGPT_PROFILES=my_profile_name_here
```

Windows Powershell has a different syntax:
```shell
$env:PGPT_PROFILES="my_profile_name_here"
```
If the above is not working, you might want to try other ways to set an env variable in your window's terminal.

---

Once you've set this environment variable to the desired profile, you can simply launch your PrivateGPT,
and it will run using your profile on top of the default configuration.

## Reference
Additional details on the profiles are described in this section

### Environment variable `PGPT_SETTINGS_FOLDER`

The location of the settings folder. Defaults to the root of the project.
Should contain the default `settings.yaml` and any other `settings-{profile}.yaml`.

### Environment variable `PGPT_PROFILES`

By default, the profile definition in `settings.yaml` is loaded.
Using this env var you can load additional profiles; format is a comma separated list of profile names.
This will merge `settings-{profile}.yaml` on top of the base settings file.

For example:
`PGPT_PROFILES=local,cuda` will load `settings-local.yaml`
and `settings-cuda.yaml`, their contents will be merged with
later profiles properties overriding values of earlier ones like `settings.yaml`.

During testing, the `test` profile will be active along with the default, therefore `settings-test.yaml`
file is required.

### Environment variables expansion

Configuration files can contain environment variables,
they will be expanded at runtime.

Expansion must follow the pattern `${VARIABLE_NAME:default_value}`.

For example, the following configuration will use the value of the `PORT`
environment variable or `8001` if it's not set.
Missing variables with no default will produce an error.

```yaml
server:
  port: ${PORT:8001}
```
```

## File: `fern/docs/pages/manual/vectordb.mdx`
```
## Vectorstores
PrivateGPT supports [Qdrant](https://qdrant.tech/), [Milvus](https://milvus.io/), [Chroma](https://www.trychroma.com/), [PGVector](https://github.com/pgvector/pgvector) and [ClickHouse](https://github.com/ClickHouse/ClickHouse) as vectorstore providers. Qdrant being the default.

In order to select one or the other, set the `vectorstore.database` property in the `settings.yaml` file to `qdrant`, `milvus`, `chroma`, `postgres` and `clickhouse`.

```yaml
vectorstore:
  database: qdrant
```

### Qdrant configuration

To enable Qdrant, set the `vectorstore.database` property in the `settings.yaml` file to `qdrant`.

Qdrant settings can be configured by setting values to the `qdrant` property in the `settings.yaml` file.

The available configuration options are:
| Field        | Description |
|--------------|-------------|
| location     | If `:memory:` - use in-memory Qdrant instance. If `str` - use it as a `url` parameter.|
| url          | Either host or str of 'Optional[scheme], host, Optional[port], Optional[prefix]'. Eg. `http://localhost:6333` |
| port         | Port of the REST API interface. Default: `6333` |
| grpc_port    | Port of the gRPC interface. Default: `6334` |
| prefer_grpc  | If `true` - use gRPC interface whenever possible in custom methods. |
| https        | If `true` - use HTTPS(SSL) protocol.|
| api_key      | API key for authentication in Qdrant Cloud.|
| prefix       | If set, add `prefix` to the REST URL path. Example: `service/v1` will result in `http://localhost:6333/service/v1/{qdrant-endpoint}` for REST API.|
| timeout      | Timeout for REST and gRPC API requests. Default: 5.0 seconds for REST and unlimited for gRPC |
| host         | Host name of Qdrant service. If url and host are not set, defaults to 'localhost'.|
| path         | Persistence path for QdrantLocal. Eg. `local_data/private_gpt/qdrant`|
| force_disable_check_same_thread         | Force disable check_same_thread for QdrantLocal sqlite connection, defaults to True.|

By default Qdrant tries to connect to an instance of Qdrant server at `http://localhost:3000`.

To obtain a local setup (disk-based database) without running a Qdrant server, configure the `qdrant.path` value in settings.yaml:

```yaml
qdrant:
  path: local_data/private_gpt/qdrant
```

### Milvus configuration

To enable Milvus, set the `vectorstore.database` property in the `settings.yaml` file to `milvus` and install the `milvus` extra.

```bash
poetry install --extras vector-stores-milvus
```

The available configuration options are:
| Field        | Description |
|--------------|-------------|
| uri     | Default is set to "local_data/private_gpt/milvus/milvus_local.db" as a local file; you can also set up a more performant Milvus server on docker or k8s e.g.http://localhost:19530, as your uri; To use Zilliz Cloud, adjust the uri and token to Endpoint and Api key in Zilliz Cloud.|
| token          | Pair with Milvus server on docker or k8s or zilliz cloud api key.|
| collection_name         | The name of the collection, set to default "milvus_db".|
| overwrite    | Overwrite the data in collection if it existed, set to default as True. |

To obtain a local setup (disk-based database) without running a Milvus server, configure the uri value in settings.yaml, to store in local_data/private_gpt/milvus/milvus_local.db.

### Chroma configuration

To enable Chroma, set the `vectorstore.database` property in the `settings.yaml` file to `chroma` and install the `chroma` extra.

```bash
poetry install --extras chroma
```

By default `chroma` will use a disk-based database stored in local_data_path / "chroma_db" (being local_data_path defined in settings.yaml)

### PGVector
To use the PGVector store a [postgreSQL](https://www.postgresql.org/) database with the PGVector extension must be used.

To enable PGVector, set the `vectorstore.database` property in the `settings.yaml` file to `postgres` and install the `vector-stores-postgres` extra.

```bash
poetry install --extras vector-stores-postgres
```

PGVector settings can be configured by setting values to the `postgres` property in the `settings.yaml` file.

The available configuration options are:
| Field         | Description                                               |
|---------------|-----------------------------------------------------------|
| **host**      | The server hosting the Postgres database. Default is `localhost` |
| **port**      | The port on which the Postgres database is accessible. Default is `5432` |
| **database**  | The specific database to connect to. Default is `postgres` |
| **user**      | The username for database access. Default is `postgres` |
| **password**  | The password for database access. (Required)            |
| **schema_name** | The database schema to use. Default is `private_gpt`       |

For example:
```yaml
vectorstore:
  database: postgres

postgres:
  host: localhost
  port: 5432
  database: postgres
  user: postgres
  password: <PASSWORD>
  schema_name: private_gpt
```

The following table will be created in the database
```
postgres=# \d private_gpt.data_embeddings
                                      Table "private_gpt.data_embeddings"
  Column   |       Type        | Collation | Nullable |                         Default
-----------+-------------------+-----------+----------+---------------------------------------------------------
 id        | bigint            |           | not null | nextval('private_gpt.data_embeddings_id_seq'::regclass)
 text      | character varying |           | not null |
 metadata_ | json              |           |          |
 node_id   | character varying |           |          |
 embedding | vector(768)       |           |          |
Indexes:
    "data_embeddings_pkey" PRIMARY KEY, btree (id)

postgres=# 
```
The dimensions of the embeddings columns will be set based on the `embedding.embed_dim` value.  If the embedding model changes this table may need to be dropped and recreated to avoid a dimension mismatch.

### ClickHouse

To utilize ClickHouse as the vector store, a [ClickHouse](https://github.com/ClickHouse/ClickHouse) database must be employed.

To enable ClickHouse, set the `vectorstore.database` property in the `settings.yaml` file to `clickhouse` and install the `vector-stores-clickhouse` extra.

```bash
poetry install --extras vector-stores-clickhouse
```

ClickHouse settings can be configured by setting values to the `clickhouse` property in the `settings.yaml` file.

The available configuration options are:
| Field                | Description                                                    |
|----------------------|----------------------------------------------------------------|
| **host**             | The server hosting the ClickHouse database. Default is `localhost` |
| **port**             | The port on which the ClickHouse database is accessible. Default is `8123` |
| **username**         | The username for database access. Default is `default` |
| **password**         | The password for database access. (Optional) |
| **database**         | The specific database to connect to. Default is `__default__` |
| **secure**           | Use https/TLS for secure connection to the server. Default is `false` |
| **interface**        | The protocol used for the connection, either 'http' or 'https'. (Optional) |
| **settings**         | Specific ClickHouse server settings to be used with the session. (Optional) |
| **connect_timeout**  | Timeout in seconds for establishing a connection. (Optional) |
| **send_receive_timeout** | Read timeout in seconds for http connection. (Optional) |
| **verify**           | Verify the server certificate in secure/https mode. (Optional) |
| **ca_cert**          | Path to Certificate Authority root certificate (.pem format). (Optional) |
| **client_cert**      | Path to TLS Client certificate (.pem format). (Optional) |
| **client_cert_key**  | Path to the private key for the TLS Client certificate. (Optional) |
| **http_proxy**       | HTTP proxy address. (Optional) |
| **https_proxy**      | HTTPS proxy address. (Optional) |
| **server_host_name** | Server host name to be checked against the TLS certificate. (Optional) |

For example:
```yaml
vectorstore:
  database: clickhouse

clickhouse:
  host: localhost
  port: 8443
  username: admin
  password: <PASSWORD>
  database: embeddings
  secure: false
```

The following table will be created in the database:
```
clickhouse-client
:) \d embeddings.llama_index
                                   Table "llama_index"
  № |  name     | type                                         | default_type | default_expression | comment | codec_expression | ttl_expression
----|-----------|----------------------------------------------|--------------|--------------------|---------|------------------|---------------
  1 | id        | String                                       |              |                    |         |                  |
  2 | doc_id    | String                                       |              |                    |         |                  |
  3 | text      | String                                       |              |                    |         |                  |
  4 | vector    | Array(Float32)                               |              |                    |         |                  |
  5 | node_info | Tuple(start Nullable(UInt64), end Nullable(UInt64)) |       |                    |         |                  |
  6 | metadata  | String                                       |              |                    |         |                  |

clickhouse-client
```

The dimensions of the embeddings columns will be set based on the `embedding.embed_dim` value. If the embedding model changes, this table may need to be dropped and recreated to avoid a dimension mismatch.
```

## File: `fern/docs/pages/overview/welcome.mdx`
```
PrivateGPT provides an **API** containing all the building blocks required to
build **private, context-aware AI applications**.

<Callout intent = "tip">
If you are looking for an **enterprise-ready, fully private AI workspace**
check out [Zylon's website](https://zylon.ai)  or [request a demo](https://cal.com/zylon/demo?source=pgpt-docs).
Crafted by the team behind PrivateGPT, Zylon is a best-in-class AI collaborative
workspace that can be easily deployed on-premise (data center, bare metal...) or in your private cloud (AWS, GCP, Azure...).
</Callout>

The API follows and extends OpenAI API standard, and supports both normal and streaming responses.
That means that, if you can use OpenAI API in one of your tools, you can use your own PrivateGPT API instead,
with no code changes, **and for free** if you are running PrivateGPT in a `local` setup.

Get started by understanding the [Main Concepts and Installation](/installation) and then dive into the [API Reference](/api-reference).

## Frequently Visited Resources

<Cards>
  <Card
    title="Main Concepts"
    icon="fa-solid fa-lines-leaning"
    href="/installation"
  />
  <Card
    title="API Reference"
    icon="fa-solid fa-code"
    href="/api-reference"
  />
  <Card
    title="Twitter"
    icon="fa-brands fa-twitter"
    href="https://twitter.com/PrivateGPT_AI"
  />
  <Card
    title="Discord Server"
    icon="fa-brands fa-discord"
    href="https://discord.gg/bK6mRVpErU"
  />
</Cards>

<br />
```

## File: `fern/docs/pages/quickstart/quickstart.mdx`
```
This guide provides a quick start for running different profiles of PrivateGPT using Docker Compose.
The profiles cater to various environments, including Ollama setups (CPU, CUDA, MacOS), and a fully local setup.

By default, Docker Compose will download pre-built images from a remote registry when starting the services. However, you have the option to build the images locally if needed. Details on building Docker image locally are provided at the end of this guide.

If you want to run PrivateGPT locally without Docker, refer to the [Local Installation Guide](/installation).

## Prerequisites
- **Docker and Docker Compose:** Ensure both are installed on your system.
  [Installation Guide for Docker](https://docs.docker.com/get-docker/), [Installation Guide for Docker Compose](https://docs.docker.com/compose/install/).
- **Clone PrivateGPT Repository:** Clone the PrivateGPT repository to your machine and navigate to the directory:
  ```sh
  git clone https://github.com/zylon-ai/private-gpt.git
  cd private-gpt
  ```

## Setups

### Ollama Setups (Recommended)

#### 1. Default/Ollama CPU

**Description:**
This profile runs the Ollama service using CPU resources. It is the standard configuration for running Ollama-based Private-GPT services without GPU acceleration.

**Run:**
To start the services using pre-built images, run:
```sh
docker-compose up
```
or with a specific profile:
```sh
docker-compose --profile ollama-cpu up
```

#### 2. Ollama Nvidia CUDA

**Description:**
This profile leverages GPU acceleration with CUDA support, suitable for computationally intensive tasks that benefit from GPU resources.

**Requirements:**
Ensure that your system has compatible GPU hardware and the necessary NVIDIA drivers installed. The installation process is detailed [here](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html).

**Run:**
To start the services with CUDA support using pre-built images, run:
```sh
docker-compose --profile ollama-cuda up
```

#### 3. Ollama External API

**Description:**
This profile is designed for running PrivateGPT using Ollama installed on the host machine. This setup is particularly useful for MacOS users, as Docker does not yet support Metal GPU.

**Requirements:**
Install Ollama on your machine by following the instructions at [ollama.ai](https://ollama.ai/).

**Run:**
To start the Ollama service, use:
```sh
OLLAMA_HOST=0.0.0.0 ollama serve
```
To start the services with the host configuration using pre-built images, run:
```sh
docker-compose --profile ollama-api up
```

### Fully Local Setups

#### 1. LlamaCPP CPU

**Description:**
This profile runs the Private-GPT services locally using `llama-cpp` and Hugging Face models.

**Requirements:**
A **Hugging Face Token (HF_TOKEN)** is required for accessing Hugging Face models. Obtain your token following [this guide](/installation/getting-started/troubleshooting#downloading-gated-and-private-models).

**Run:**
Start the services with your Hugging Face token using pre-built images:
```sh
HF_TOKEN=<your_hf_token> docker-compose --profile llamacpp-cpu up
```
Replace `<your_hf_token>` with your actual Hugging Face token.

## Building Locally

If you prefer to build Docker images locally, which is useful when making changes to the codebase or the Dockerfiles, follow these steps:

### Building Locally
To build the Docker images locally, navigate to the cloned repository directory and run:
```sh
docker-compose build
```
This command compiles the necessary Docker images based on the current codebase and Dockerfile configurations.

### Forcing a Rebuild with --build
If you have made changes and need to ensure these changes are reflected in the Docker images, you can force a rebuild before starting the services:
```sh
docker-compose up --build
```
or with a specific profile:
```sh
docker-compose --profile <profile_name> up --build
```
Replace `<profile_name>` with the desired profile.
```

## File: `fern/docs/pages/recipes/quickstart.mdx`
```
# Recipes

Recipes are predefined use cases that help users solve very specific tasks using PrivateGPT.
They provide a streamlined approach to achieve common goals with the platform, offering both a starting point and inspiration for further exploration.
The main goal of Recipes is to empower the community to create and share solutions, expanding the capabilities of PrivateGPT.

## How to Create a New Recipe

1. **Identify the Task**: Define a specific task or problem that the Recipe will address.
2. **Develop the Solution**: Create a clear and concise guide, including any necessary code snippets or configurations.
3. **Submit a PR**: Fork the PrivateGPT repository, add your Recipe to the appropriate section, and submit a PR for review.

We encourage you to be creative and think outside the box! Your contributions help shape the future of PrivateGPT.

## Available Recipes

<Cards>
  <Card
    title="Summarize"
    icon="fa-solid fa-file-alt"
    href="/recipes/general-use-cases/summarize"
  />
</Cards>
```

## File: `fern/docs/pages/recipes/summarize.mdx`
```
The Summarize Recipe provides a method to extract concise summaries from ingested documents or texts using PrivateGPT.
This tool is particularly useful for quickly understanding large volumes of information by distilling key points and main ideas.

## Use Case

The primary use case for the `Summarize` tool is to automate the summarization of lengthy documents,
making it easier for users to grasp the essential information without reading through entire texts.
This can be applied in various scenarios, such as summarizing research papers, news articles, or business reports.

## Key Features

1. **Ingestion-compatible**: The user provides the text to be summarized. The text can be directly inputted or retrieved from ingested documents within the system.
2. **Customization**: The summary generation can be influenced by providing specific `instructions` or a `prompt`. These inputs guide the model on how to frame the summary, allowing for customization according to user needs.
3. **Streaming Support**: The tool supports streaming, allowing for real-time summary generation, which can be particularly useful for handling large texts or providing immediate feedback.

## Contributing

If you have ideas for improving the Summarize or want to add new features, feel free to contribute!
You can submit your enhancements via a pull request on our [GitHub repository](https://github.com/zylon-ai/private-gpt).

```

## File: `fern/docs/pages/ui/alternatives.mdx`
```

This page aims to present different user interface (UI) alternatives for integrating and using PrivateGPT. These alternatives range from demo applications to fully customizable UI setups that can be adapted to your specific needs.

**Do you have any working demo project using PrivateGPT?**

Please open a PR to add it to the list, and come on our Discord to tell us about it!

<Callout intent = "note">
WIP: This page provides an overview of one of the UI alternatives available for PrivateGPT. More alternatives will be added to this page as they become available.
</Callout>

## [PrivateGPT SDK Demo App](https://github.com/frgarciames/privategpt-react)

The PrivateGPT SDK demo app is a robust starting point for developers looking to integrate and customize PrivateGPT in their applications. Leveraging modern technologies like Tailwind, shadcn/ui, and Biomejs, it provides a smooth development experience and a highly customizable user interface. Refer to the [repository](https://github.com/frgarciames/privategpt-react) for more details and to get started.

**Tech Stack:**

- **Tailwind:** A utility-first CSS framework for rapid UI development.
- **shadcn/ui:** A set of high-quality, customizable UI components.
- **PrivateGPT Web SDK:** The core SDK for interacting with PrivateGPT.
- **Biomejs formatter/linter:** A tool for maintaining code quality and consistency.
```

## File: `fern/docs/pages/ui/gradio.mdx`
```
## Gradio UI user manual

Gradio UI is a ready to use way of testing most of PrivateGPT API functionalities.

![Gradio PrivateGPT](https://github.com/zylon-ai/private-gpt/raw/main/fern/docs/assets/ui.png?raw=true)

<Callout intent = "warning">
A working **Gradio UI client** is provided to test the API, together with a set of useful tools such as bulk
model download script, ingestion script, documents folder watch, etc. Please refer to the [UI alternatives](/manual/user-interface/alternatives) page for more UI alternatives.
</Callout>

### Execution Modes

It has 3 modes of execution (you can select in the top-left):

* Query Docs: uses the context from the
  ingested documents to answer the questions posted in the chat. It also takes
  into account previous chat messages as context.
    * Makes use of `/chat/completions` API with `use_context=true` and no
      `context_filter`.
* Search in Docs: fast search that returns the 4 most related text
  chunks, together with their source document and page.
    * Makes use of `/chunks` API with no `context_filter`, `limit=4` and
      `prev_next_chunks=0`.
* LLM Chat: simple, non-contextual chat with the LLM. The ingested documents won't
  be taken into account, only the previous messages.
    * Makes use of `/chat/completions` API with `use_context=false`.

### Document Ingestion

Ingest documents by using the `Upload a File` button. You can check the progress of
the ingestion in the console logs of the server.

The list of ingested files is shown below the button.

If you want to delete the ingested documents, refer to *Reset Local documents
database* section in the documentation.

### Chat

Normal chat interface, self-explanatory ;)

#### System Prompt
You can view and change the system prompt being passed to the LLM by clicking "Additional Inputs"
in the chat interface. The system prompt is also logged on the server.

By default, the `Query Docs` mode uses the setting value `ui.default_query_system_prompt`.

The `LLM Chat` mode attempts to use the optional settings value `ui.default_chat_system_prompt`.

If no system prompt is entered, the UI will display the default system prompt being used
for the active mode.

##### System Prompt Examples:

The system prompt can effectively provide your chat bot specialized roles, and results tailored to the prompt
you have given the model. Examples of system prompts can be be found
[here](https://www.w3schools.com/gen_ai/chatgpt-3-5/chatgpt-3-5_roles.php).

Some interesting examples to try include:

* You are -X-. You have all the knowledge and personality of -X-. Answer as if you were -X- using
their manner of speaking and vocabulary.
    * Example: You are Shakespeare. You have all the knowledge and personality of Shakespeare.
    Answer as if you were Shakespeare using their manner of speaking and vocabulary.
* You are an expert (at) -role-. Answer all questions using your expertise on -specific domain topic-.
    * Example: You are an expert software engineer. Answer all questions using your expertise on Python.
* You are a -role- bot, respond with -response criteria needed-. If no -response criteria- is needed,
respond with -alternate response-.
    * Example: You are a grammar checking bot, respond with any grammatical corrections needed. If no corrections
    are needed, respond with "verified".
```

## File: `fern/openapi/openapi.json`
```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "paths": {
    "/v1/completions": {
      "post": {
        "tags": [
          "Contextual Completions"
        ],
        "summary": "Completion",
        "description": "We recommend most users use our Chat completions API.\n\nGiven a prompt, the model will return one predicted completion.\n\nOptionally include a `system_prompt` to influence the way the LLM answers.\n\nIf `use_context`\nis set to `true`, the model will use context coming from the ingested documents\nto create the response. The documents being used can be filtered using the\n`context_filter` and passing the document IDs to be used. Ingested documents IDs\ncan be found using `/ingest/list` endpoint. If you want all ingested documents to\nbe used, remove `context_filter` altogether.\n\nWhen using `'include_sources': true`, the API will return the source Chunks used\nto create the response, which come from the context provided.\n\nWhen using `'stream': true`, the API will return data chunks following [OpenAI's\nstreaming model](https://platform.openai.com/docs/api-reference/chat/streaming):\n```\n{\"id\":\"12345\",\"object\":\"completion.chunk\",\"created\":1694268190,\n\"model\":\"private-gpt\",\"choices\":[{\"index\":0,\"delta\":{\"content\":\"Hello\"},\n\"finish_reason\":null}]}\n```",
        "operationId": "prompt_completion_v1_completions_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CompletionsBody"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OpenAICompletion"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "x-fern-streaming": {
          "stream-condition": "stream",
          "response": {
            "$ref": "#/components/schemas/OpenAICompletion"
          },
          "response-stream": {
            "$ref": "#/components/schemas/OpenAICompletion"
          }
        }
      }
    },
    "/v1/chat/completions": {
      "post": {
        "tags": [
          "Contextual Completions"
        ],
        "summary": "Chat Completion",
        "description": "Given a list of messages comprising a conversation, return a response.\n\nOptionally include an initial `role: system` message to influence the way\nthe LLM answers.\n\nIf `use_context` is set to `true`, the model will use context coming\nfrom the ingested documents to create the response. The documents being used can\nbe filtered using the `context_filter` and passing the document IDs to be used.\nIngested documents IDs can be found using `/ingest/list` endpoint. If you want\nall ingested documents to be used, remove `context_filter` altogether.\n\nWhen using `'include_sources': true`, the API will return the source Chunks used\nto create the response, which come from the context provided.\n\nWhen using `'stream': true`, the API will return data chunks following [OpenAI's\nstreaming model](https://platform.openai.com/docs/api-reference/chat/streaming):\n```\n{\"id\":\"12345\",\"object\":\"completion.chunk\",\"created\":1694268190,\n\"model\":\"private-gpt\",\"choices\":[{\"index\":0,\"delta\":{\"content\":\"Hello\"},\n\"finish_reason\":null}]}\n```",
        "operationId": "chat_completion_v1_chat_completions_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ChatBody"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OpenAICompletion"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "x-fern-streaming": {
          "stream-condition": "stream",
          "response": {
            "$ref": "#/components/schemas/OpenAICompletion"
          },
          "response-stream": {
            "$ref": "#/components/schemas/OpenAICompletion"
          }
        }
      }
    },
    "/v1/chunks": {
      "post": {
        "tags": [
          "Context Chunks"
        ],
        "summary": "Chunks Retrieval",
        "description": "Given a `text`, returns the most relevant chunks from the ingested documents.\n\nThe returned information can be used to generate prompts that can be\npassed to `/completions` or `/chat/completions` APIs. Note: it is usually a very\nfast API, because only the Embeddings model is involved, not the LLM. The\nreturned information contains the relevant chunk `text` together with the source\n`document` it is coming from. It also contains a score that can be used to\ncompare different results.\n\nThe max number of chunks to be returned is set using the `limit` param.\n\nPrevious and next chunks (pieces of text that appear right before or after in the\ndocument) can be fetched by using the `prev_next_chunks` field.\n\nThe documents being used can be filtered using the `context_filter` and passing\nthe document IDs to be used. Ingested documents IDs can be found using\n`/ingest/list` endpoint. If you want all ingested documents to be used,\nremove `context_filter` altogether.",
        "operationId": "chunks_retrieval_v1_chunks_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ChunksBody"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ChunksResponse"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/ingest": {
      "post": {
        "tags": [
          "Ingestion"
        ],
        "summary": "Ingest",
        "description": "Ingests and processes a file.\n\nDeprecated. Use ingest/file instead.",
        "operationId": "ingest_v1_ingest_post",
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Body_ingest_v1_ingest_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/IngestResponse"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "deprecated": true
      }
    },
    "/v1/ingest/file": {
      "post": {
        "tags": [
          "Ingestion"
        ],
        "summary": "Ingest File",
        "description": "Ingests and processes a file, storing its chunks to be used as context.\n\nThe context obtained from files is later used in\n`/chat/completions`, `/completions`, and `/chunks` APIs.\n\nMost common document\nformats are supported, but you may be prompted to install an extra dependency to\nmanage a specific file type.\n\nA file can generate different Documents (for example a PDF generates one Document\nper page). All Documents IDs are returned in the response, together with the\nextracted Metadata (which is later used to improve context retrieval). Those IDs\ncan be used to filter the context used to create responses in\n`/chat/completions`, `/completions`, and `/chunks` APIs.",
        "operationId": "ingest_file_v1_ingest_file_post",
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Body_ingest_file_v1_ingest_file_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/IngestResponse"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/ingest/text": {
      "post": {
        "tags": [
          "Ingestion"
        ],
        "summary": "Ingest Text",
        "description": "Ingests and processes a text, storing its chunks to be used as context.\n\nThe context obtained from files is later used in\n`/chat/completions`, `/completions`, and `/chunks` APIs.\n\nA Document will be generated with the given text. The Document\nID is returned in the response, together with the\nextracted Metadata (which is later used to improve context retrieval). That ID\ncan be used to filter the context used to create responses in\n`/chat/completions`, `/completions`, and `/chunks` APIs.",
        "operationId": "ingest_text_v1_ingest_text_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/IngestTextBody"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/IngestResponse"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/ingest/list": {
      "get": {
        "tags": [
          "Ingestion"
        ],
        "summary": "List Ingested",
        "description": "Lists already ingested Documents including their Document ID and metadata.\n\nThose IDs can be used to filter the context used to create responses\nin `/chat/completions`, `/completions`, and `/chunks` APIs.",
        "operationId": "list_ingested_v1_ingest_list_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/IngestResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/ingest/{doc_id}": {
      "delete": {
        "tags": [
          "Ingestion"
        ],
        "summary": "Delete Ingested",
        "description": "Delete the specified ingested Document.\n\nThe `doc_id` can be obtained from the `GET /ingest/list` endpoint.\nThe document will be effectively deleted from your storage context.",
        "operationId": "delete_ingested_v1_ingest__doc_id__delete",
        "parameters": [
          {
            "name": "doc_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Doc Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/summarize": {
      "post": {
        "tags": [
          "Recipes"
        ],
        "summary": "Summarize",
        "description": "Given a text, the model will return a summary.\n\nOptionally include `instructions` to influence the way the summary is generated.\n\nIf `use_context`\nis set to `true`, the model will also use the content coming from the ingested\ndocuments in the summary. The documents being used can\nbe filtered by their metadata using the `context_filter`.\nIngested documents metadata can be found using `/ingest/list` endpoint.\nIf you want all ingested documents to be used, remove `context_filter` altogether.\n\nIf `prompt` is set, it will be used as the prompt for the summarization,\notherwise the default prompt will be used.\n\nWhen using `'stream': true`, the API will return data chunks following [OpenAI's\nstreaming model](https://platform.openai.com/docs/api-reference/chat/streaming):\n```\n{\"id\":\"12345\",\"object\":\"completion.chunk\",\"created\":1694268190,\n\"model\":\"private-gpt\",\"choices\":[{\"index\":0,\"delta\":{\"content\":\"Hello\"},\n\"finish_reason\":null}]}\n```",
        "operationId": "summarize_v1_summarize_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SummarizeBody"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SummarizeResponse"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/embeddings": {
      "post": {
        "tags": [
          "Embeddings"
        ],
        "summary": "Embeddings Generation",
        "description": "Get a vector representation of a given input.\n\nThat vector representation can be easily consumed\nby machine learning models and algorithms.",
        "operationId": "embeddings_generation_v1_embeddings_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/EmbeddingsBody"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EmbeddingsResponse"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/health": {
      "get": {
        "tags": [
          "Health"
        ],
        "summary": "Health",
        "description": "Return ok if the system is up.",
        "operationId": "health_health_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HealthResponse"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Body_ingest_file_v1_ingest_file_post": {
        "properties": {
          "file": {
            "type": "string",
            "format": "binary",
            "title": "File"
          }
        },
        "type": "object",
        "required": [
          "file"
        ],
        "title": "Body_ingest_file_v1_ingest_file_post"
      },
      "Body_ingest_v1_ingest_post": {
        "properties": {
          "file": {
            "type": "string",
            "format": "binary",
            "title": "File"
          }
        },
        "type": "object",
        "required": [
          "file"
        ],
        "title": "Body_ingest_v1_ingest_post"
      },
      "ChatBody": {
        "properties": {
          "messages": {
            "items": {
              "$ref": "#/components/schemas/OpenAIMessage"
            },
            "type": "array",
            "title": "Messages"
          },
          "use_context": {
            "type": "boolean",
            "title": "Use Context",
            "default": false
          },
          "context_filter": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ContextFilter"
              },
              {
                "type": "null"
              }
            ]
          },
          "include_sources": {
            "type": "boolean",
            "title": "Include Sources",
            "default": true
          },
          "stream": {
            "type": "boolean",
            "title": "Stream",
            "default": false
          }
        },
        "type": "object",
        "required": [
          "messages"
        ],
        "title": "ChatBody",
        "examples": [
          {
            "context_filter": {
              "docs_ids": [
                "c202d5e6-7b69-4869-81cc-dd574ee8ee11"
              ]
            },
            "include_sources": true,
            "messages": [
              {
                "content": "You are a rapper. Always answer with a rap.",
                "role": "system"
              },
              {
                "content": "How do you fry an egg?",
                "role": "user"
              }
            ],
            "stream": false,
            "use_context": true
          }
        ]
      },
      "Chunk": {
        "properties": {
          "object": {
            "type": "string",
            "enum": [
              "context.chunk"
            ],
            "const": "context.chunk",
            "title": "Object"
          },
          "score": {
            "type": "number",
            "title": "Score",
            "examples": [
              0.023
            ]
          },
          "document": {
            "$ref": "#/components/schemas/IngestedDoc"
          },
          "text": {
            "type": "string",
            "title": "Text",
            "examples": [
              "Outbound sales increased 20%, driven by new leads."
            ]
          },
          "previous_texts": {
            "anyOf": [
              {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Previous Texts",
            "examples": [
              [
                "SALES REPORT 2023",
                "Inbound didn't show major changes."
              ]
            ]
          },
          "next_texts": {
            "anyOf": [
              {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Next Texts",
            "examples": [
              [
                "New leads came from Google Ads campaign.",
                "The campaign was run by the Marketing Department"
              ]
            ]
          }
        },
        "type": "object",
        "required": [
          "object",
          "score",
          "document",
          "text"
        ],
        "title": "Chunk"
      },
      "ChunksBody": {
        "properties": {
          "text": {
            "type": "string",
            "title": "Text",
            "examples": [
              "Q3 2023 sales"
            ]
          },
          "context_filter": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ContextFilter"
              },
              {
                "type": "null"
              }
            ]
          },
          "limit": {
            "type": "integer",
            "title": "Limit",
            "default": 10
          },
          "prev_next_chunks": {
            "type": "integer",
            "title": "Prev Next Chunks",
            "default": 0,
            "examples": [
              2
            ]
          }
        },
        "type": "object",
        "required": [
          "text"
        ],
        "title": "ChunksBody"
      },
      "ChunksResponse": {
        "properties": {
          "object": {
            "type": "string",
            "enum": [
              "list"
            ],
            "const": "list",
            "title": "Object"
          },
          "model": {
            "type": "string",
            "enum": [
              "private-gpt"
            ],
            "const": "private-gpt",
            "title": "Model"
          },
          "data": {
            "items": {
              "$ref": "#/components/schemas/Chunk"
            },
            "type": "array",
            "title": "Data"
          }
        },
        "type": "object",
        "required": [
          "object",
          "model",
          "data"
        ],
        "title": "ChunksResponse"
      },
      "CompletionsBody": {
        "properties": {
          "prompt": {
            "type": "string",
            "title": "Prompt"
          },
          "system_prompt": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "System Prompt"
          },
          "use_context": {
            "type": "boolean",
            "title": "Use Context",
            "default": false
          },
          "context_filter": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ContextFilter"
              },
              {
                "type": "null"
              }
            ]
          },
          "include_sources": {
            "type": "boolean",
            "title": "Include Sources",
            "default": true
          },
          "stream": {
            "type": "boolean",
            "title": "Stream",
            "default": false
          }
        },
        "type": "object",
        "required": [
          "prompt"
        ],
        "title": "CompletionsBody",
        "examples": [
          {
            "include_sources": false,
            "prompt": "How do you fry an egg?",
            "stream": false,
            "system_prompt": "You are a rapper. Always answer with a rap.",
            "use_context": false
          }
        ]
      },
      "ContextFilter": {
        "properties": {
          "docs_ids": {
            "anyOf": [
              {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Docs Ids",
            "examples": [
              [
                "c202d5e6-7b69-4869-81cc-dd574ee8ee11"
              ]
            ]
          }
        },
        "type": "object",
        "required": [
          "docs_ids"
        ],
        "title": "ContextFilter"
      },
      "Embedding": {
        "properties": {
          "index": {
            "type": "integer",
            "title": "Index"
          },
          "object": {
            "type": "string",
            "enum": [
              "embedding"
            ],
            "const": "embedding",
            "title": "Object"
          },
          "embedding": {
            "items": {
              "type": "number"
            },
            "type": "array",
            "title": "Embedding",
            "examples": [
              [
                0.0023064255,
                -0.009327292
              ]
            ]
          }
        },
        "type": "object",
        "required": [
          "index",
          "object",
          "embedding"
        ],
        "title": "Embedding"
      },
      "EmbeddingsBody": {
        "properties": {
          "input": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "items": {
                  "type": "string"
                },
                "type": "array"
              }
            ],
            "title": "Input"
          }
        },
        "type": "object",
        "required": [
          "input"
        ],
        "title": "EmbeddingsBody"
      },
      "EmbeddingsResponse": {
        "properties": {
          "object": {
            "type": "string",
            "enum": [
              "list"
            ],
            "const": "list",
            "title": "Object"
          },
          "model": {
            "type": "string",
            "enum": [
              "private-gpt"
            ],
            "const": "private-gpt",
            "title": "Model"
          },
          "data": {
            "items": {
              "$ref": "#/components/schemas/Embedding"
            },
            "type": "array",
            "title": "Data"
          }
        },
        "type": "object",
        "required": [
          "object",
          "model",
          "data"
        ],
        "title": "EmbeddingsResponse"
      },
      "HTTPValidationError": {
        "properties": {
          "detail": {
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            },
            "type": "array",
            "title": "Detail"
          }
        },
        "type": "object",
        "title": "HTTPValidationError"
      },
      "HealthResponse": {
        "properties": {
          "status": {
            "type": "string",
            "enum": [
              "ok"
            ],
            "const": "ok",
            "title": "Status",
            "default": "ok"
          }
        },
        "type": "object",
        "title": "HealthResponse"
      },
      "IngestResponse": {
        "properties": {
          "object": {
            "type": "string",
            "enum": [
              "list"
            ],
            "const": "list",
            "title": "Object"
          },
          "model": {
            "type": "string",
            "enum": [
              "private-gpt"
            ],
            "const": "private-gpt",
            "title": "Model"
          },
          "data": {
            "items": {
              "$ref": "#/components/schemas/IngestedDoc"
            },
            "type": "array",
            "title": "Data"
          }
        },
        "type": "object",
        "required": [
          "object",
          "model",
          "data"
        ],
        "title": "IngestResponse"
      },
      "IngestTextBody": {
        "properties": {
          "file_name": {
            "type": "string",
            "title": "File Name",
            "examples": [
              "Avatar: The Last Airbender"
            ]
          },
          "text": {
            "type": "string",
            "title": "Text",
            "examples": [
              "Avatar is set in an Asian and Arctic-inspired world in which some people can telekinetically manipulate one of the four elements\u2014water, earth, fire or air\u2014through practices known as 'bending', inspired by Chinese martial arts."
            ]
          }
        },
        "type": "object",
        "required": [
          "file_name",
          "text"
        ],
        "title": "IngestTextBody"
      },
      "IngestedDoc": {
        "properties": {
          "object": {
            "type": "string",
            "enum": [
              "ingest.document"
            ],
            "const": "ingest.document",
            "title": "Object"
          },
          "doc_id": {
            "type": "string",
            "title": "Doc Id",
            "examples": [
              "c202d5e6-7b69-4869-81cc-dd574ee8ee11"
            ]
          },
          "doc_metadata": {
            "anyOf": [
              {
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Doc Metadata",
            "examples": [
              {
                "file_name": "Sales Report Q3 2023.pdf",
                "page_label": "2"
              }
            ]
          }
        },
        "type": "object",
        "required": [
          "object",
          "doc_id",
          "doc_metadata"
        ],
        "title": "IngestedDoc"
      },
      "OpenAIChoice": {
        "properties": {
          "finish_reason": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Finish Reason",
            "examples": [
              "stop"
            ]
          },
          "delta": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/OpenAIDelta"
              },
              {
                "type": "null"
              }
            ]
          },
          "message": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/OpenAIMessage"
              },
              {
                "type": "null"
              }
            ]
          },
          "sources": {
            "anyOf": [
              {
                "items": {
                  "$ref": "#/components/schemas/Chunk"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Sources"
          },
          "index": {
            "type": "integer",
            "title": "Index",
            "default": 0
          }
        },
        "type": "object",
        "required": [
          "finish_reason"
        ],
        "title": "OpenAIChoice",
        "description": "Response from AI.\n\nEither the delta or the message will be present, but never both.\nSources used will be returned in case context retrieval was enabled."
      },
      "OpenAICompletion": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "object": {
            "type": "string",
            "enum": [
              "completion",
              "completion.chunk"
            ],
            "title": "Object",
            "default": "completion"
          },
          "created": {
            "type": "integer",
            "title": "Created",
            "examples": [
              1623340000
            ]
          },
          "model": {
            "type": "string",
            "enum": [
              "private-gpt"
            ],
            "const": "private-gpt",
            "title": "Model"
          },
          "choices": {
            "items": {
              "$ref": "#/components/schemas/OpenAIChoice"
            },
            "type": "array",
            "title": "Choices"
          }
        },
        "type": "object",
        "required": [
          "id",
          "created",
          "model",
          "choices"
        ],
        "title": "OpenAICompletion",
        "description": "Clone of OpenAI Completion model.\n\nFor more information see: https://platform.openai.com/docs/api-reference/chat/object"
      },
      "OpenAIDelta": {
        "properties": {
          "content": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Content"
          }
        },
        "type": "object",
        "required": [
          "content"
        ],
        "title": "OpenAIDelta",
        "description": "A piece of completion that needs to be concatenated to get the full message."
      },
      "OpenAIMessage": {
        "properties": {
          "role": {
            "type": "string",
            "enum": [
              "assistant",
              "system",
              "user"
            ],
            "title": "Role",
            "default": "user"
          },
          "content": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Content"
          }
        },
        "type": "object",
        "required": [
          "content"
        ],
        "title": "OpenAIMessage",
        "description": "Inference result, with the source of the message.\n\nRole could be the assistant or system\n(providing a default response, not AI generated)."
      },
      "SummarizeBody": {
        "properties": {
          "text": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Text"
          },
          "use_context": {
            "type": "boolean",
            "title": "Use Context",
            "default": false
          },
          "context_filter": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ContextFilter"
              },
              {
                "type": "null"
              }
            ]
          },
          "prompt": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Prompt"
          },
          "instructions": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Instructions"
          },
          "stream": {
            "type": "boolean",
            "title": "Stream",
            "default": false
          }
        },
        "type": "object",
        "title": "SummarizeBody"
      },
      "SummarizeResponse": {
        "properties": {
          "summary": {
            "type": "string",
            "title": "Summary"
          }
        },
        "type": "object",
        "required": [
          "summary"
        ],
        "title": "SummarizeResponse"
      },
      "ValidationError": {
        "properties": {
          "loc": {
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "integer"
                }
              ]
            },
            "type": "array",
            "title": "Location"
          },
          "msg": {
            "type": "string",
            "title": "Message"
          },
          "type": {
            "type": "string",
            "title": "Error Type"
          }
        },
        "type": "object",
        "required": [
          "loc",
          "msg",
          "type"
        ],
        "title": "ValidationError"
      }
    }
  }
}
```

## File: `local_data/.gitignore`
```
*
!.gitignore
```

## File: `models/.gitignore`
```
*
!.gitignore
```

## File: `private_gpt/__init__.py`
```python
"""private-gpt."""

import logging
import os

# Set to 'DEBUG' to have extensive logging turned on, even for libraries
ROOT_LOG_LEVEL = "INFO"

PRETTY_LOG_FORMAT = (
    "%(asctime)s.%(msecs)03d [%(levelname)-8s] %(name)+25s - %(message)s"
)
logging.basicConfig(level=ROOT_LOG_LEVEL, format=PRETTY_LOG_FORMAT, datefmt="%H:%M:%S")
logging.captureWarnings(True)

# Disable gradio analytics
# This is done this way because gradio does not solely rely on what values are
# passed to gr.Blocks(enable_analytics=...) but also on the environment
# variable GRADIO_ANALYTICS_ENABLED. `gradio.strings` actually reads this env
# directly, so to fully disable gradio analytics we need to set this env var.
os.environ["GRADIO_ANALYTICS_ENABLED"] = "False"

# Disable chromaDB telemetry
# It is already disabled, see PR#1144
# os.environ["ANONYMIZED_TELEMETRY"] = "False"

# adding tiktoken cache path within repo to be able to run in offline environment.
os.environ["TIKTOKEN_CACHE_DIR"] = "tiktoken_cache"
```

## File: `private_gpt/__main__.py`
```python
# start a fastapi server with uvicorn

import uvicorn

from private_gpt.main import app
from private_gpt.settings.settings import settings

# Set log_config=None to do not use the uvicorn logging configuration, and
# use ours instead. For reference, see below:
# https://github.com/tiangolo/fastapi/discussions/7457#discussioncomment-5141108
uvicorn.run(app, host="0.0.0.0", port=settings().server.port, log_config=None)
```

## File: `private_gpt/constants.py`
```python
from pathlib import Path

PROJECT_ROOT_PATH: Path = Path(__file__).parents[1]
```

## File: `private_gpt/di.py`
```python
from injector import Injector

from private_gpt.settings.settings import Settings, unsafe_typed_settings


def create_application_injector() -> Injector:
    _injector = Injector(auto_bind=True)
    _injector.binder.bind(Settings, to=unsafe_typed_settings)
    return _injector


"""
Global injector for the application.

Avoid using this reference, it will make your code harder to test.

Instead, use the `request.state.injector` reference, which is bound to every request
"""
global_injector: Injector = create_application_injector()
```

## File: `private_gpt/launcher.py`
```python
"""FastAPI app creation, logger configuration and main API routes."""

import logging

from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from injector import Injector
from llama_index.core.callbacks import CallbackManager
from llama_index.core.callbacks.global_handlers import create_global_handler
from llama_index.core.settings import Settings as LlamaIndexSettings

from private_gpt.server.chat.chat_router import chat_router
from private_gpt.server.chunks.chunks_router import chunks_router
from private_gpt.server.completions.completions_router import completions_router
from private_gpt.server.embeddings.embeddings_router import embeddings_router
from private_gpt.server.health.health_router import health_router
from private_gpt.server.ingest.ingest_router import ingest_router
from private_gpt.server.recipes.summarize.summarize_router import summarize_router
from private_gpt.settings.settings import Settings

logger = logging.getLogger(__name__)


def create_app(root_injector: Injector) -> FastAPI:

    # Start the API
    async def bind_injector_to_request(request: Request) -> None:
        request.state.injector = root_injector

    app = FastAPI(dependencies=[Depends(bind_injector_to_request)])

    app.include_router(completions_router)
    app.include_router(chat_router)
    app.include_router(chunks_router)
    app.include_router(ingest_router)
    app.include_router(summarize_router)
    app.include_router(embeddings_router)
    app.include_router(health_router)

    # Add LlamaIndex simple observability
    global_handler = create_global_handler("simple")
    if global_handler:
        LlamaIndexSettings.callback_manager = CallbackManager([global_handler])

    settings = root_injector.get(Settings)
    if settings.server.cors.enabled:
        logger.debug("Setting up CORS middleware")
        app.add_middleware(
            CORSMiddleware,
            allow_credentials=settings.server.cors.allow_credentials,
            allow_origins=settings.server.cors.allow_origins,
            allow_origin_regex=settings.server.cors.allow_origin_regex,
            allow_methods=settings.server.cors.allow_methods,
            allow_headers=settings.server.cors.allow_headers,
        )

    if settings.ui.enabled:
        logger.debug("Importing the UI module")
        try:
            from private_gpt.ui.ui import PrivateGptUi
        except ImportError as e:
            raise ImportError(
                "UI dependencies not found, install with `poetry install --extras ui`"
            ) from e

        ui = root_injector.get(PrivateGptUi)
        ui.mount_in_app(app, settings.ui.path)

    return app
```

## File: `private_gpt/main.py`
```python
"""FastAPI app creation, logger configuration and main API routes."""

from private_gpt.di import global_injector
from private_gpt.launcher import create_app

app = create_app(global_injector)
```

## File: `private_gpt/paths.py`
```python
from pathlib import Path

from private_gpt.constants import PROJECT_ROOT_PATH
from private_gpt.settings.settings import settings


def _absolute_or_from_project_root(path: str) -> Path:
    if path.startswith("/"):
        return Path(path)
    return PROJECT_ROOT_PATH / path


models_path: Path = PROJECT_ROOT_PATH / "models"
models_cache_path: Path = models_path / "cache"
docs_path: Path = PROJECT_ROOT_PATH / "docs"
local_data_path: Path = _absolute_or_from_project_root(
    settings().data.local_data_folder
)
```

## File: `private_gpt/components/embedding/embedding_component.py`
```python
import logging

from injector import inject, singleton
from llama_index.core.embeddings import BaseEmbedding, MockEmbedding

from private_gpt.paths import models_cache_path
from private_gpt.settings.settings import Settings

logger = logging.getLogger(__name__)


@singleton
class EmbeddingComponent:
    embedding_model: BaseEmbedding

    @inject
    def __init__(self, settings: Settings) -> None:
        embedding_mode = settings.embedding.mode
        logger.info("Initializing the embedding model in mode=%s", embedding_mode)
        match embedding_mode:
            case "huggingface":
                try:
                    from llama_index.embeddings.huggingface import (  # type: ignore
                        HuggingFaceEmbedding,
                    )
                except ImportError as e:
                    raise ImportError(
                        "Local dependencies not found, install with `poetry install --extras embeddings-huggingface`"
                    ) from e

                self.embedding_model = HuggingFaceEmbedding(
                    model_name=settings.huggingface.embedding_hf_model_name,
                    cache_folder=str(models_cache_path),
                    trust_remote_code=settings.huggingface.trust_remote_code,
                )
            case "sagemaker":
                try:
                    from private_gpt.components.embedding.custom.sagemaker import (
                        SagemakerEmbedding,
                    )
                except ImportError as e:
                    raise ImportError(
                        "Sagemaker dependencies not found, install with `poetry install --extras embeddings-sagemaker`"
                    ) from e

                self.embedding_model = SagemakerEmbedding(
                    endpoint_name=settings.sagemaker.embedding_endpoint_name,
                )
            case "openai":
                try:
                    from llama_index.embeddings.openai import (  # type: ignore
                        OpenAIEmbedding,
                    )
                except ImportError as e:
                    raise ImportError(
                        "OpenAI dependencies not found, install with `poetry install --extras embeddings-openai`"
                    ) from e

                api_base = (
                    settings.openai.embedding_api_base or settings.openai.api_base
                )
                api_key = settings.openai.embedding_api_key or settings.openai.api_key
                model = settings.openai.embedding_model

                self.embedding_model = OpenAIEmbedding(
                    api_base=api_base,
                    api_key=api_key,
                    model=model,
                )
            case "ollama":
                try:
                    from llama_index.embeddings.ollama import (  # type: ignore
                        OllamaEmbedding,
                    )
                    from ollama import Client  # type: ignore
                except ImportError as e:
                    raise ImportError(
                        "Local dependencies not found, install with `poetry install --extras embeddings-ollama`"
                    ) from e

                ollama_settings = settings.ollama

                # Calculate embedding model. If not provided tag, it will be use latest
                model_name = (
                    ollama_settings.embedding_model + ":latest"
                    if ":" not in ollama_settings.embedding_model
                    else ollama_settings.embedding_model
                )

                self.embedding_model = OllamaEmbedding(
                    model_name=model_name,
                    base_url=ollama_settings.embedding_api_base,
                )

                if ollama_settings.autopull_models:
                    if ollama_settings.autopull_models:
                        from private_gpt.utils.ollama import (
                            check_connection,
                            pull_model,
                        )

                        # TODO: Reuse llama-index client when llama-index is updated
                        client = Client(
                            host=ollama_settings.embedding_api_base,
                            timeout=ollama_settings.request_timeout,
                        )

                        if not check_connection(client):
                            raise ValueError(
                                f"Failed to connect to Ollama, "
                                f"check if Ollama server is running on {ollama_settings.api_base}"
                            )
                        pull_model(client, model_name)

            case "azopenai":
                try:
                    from llama_index.embeddings.azure_openai import (  # type: ignore
                        AzureOpenAIEmbedding,
                    )
                except ImportError as e:
                    raise ImportError(
                        "Azure OpenAI dependencies not found, install with `poetry install --extras embeddings-azopenai`"
                    ) from e

                azopenai_settings = settings.azopenai
                self.embedding_model = AzureOpenAIEmbedding(
                    model=azopenai_settings.embedding_model,
                    deployment_name=azopenai_settings.embedding_deployment_name,
                    api_key=azopenai_settings.api_key,
                    azure_endpoint=azopenai_settings.azure_endpoint,
                    api_version=azopenai_settings.api_version,
                )
            case "gemini":
                try:
                    from llama_index.embeddings.gemini import (  # type: ignore
                        GeminiEmbedding,
                    )
                except ImportError as e:
                    raise ImportError(
                        "Gemini dependencies not found, install with `poetry install --extras embeddings-gemini`"
                    ) from e

                self.embedding_model = GeminiEmbedding(
                    api_key=settings.gemini.api_key,
                    model_name=settings.gemini.embedding_model,
                )
            case "mistralai":
                try:
                    from llama_index.embeddings.mistralai import (  # type: ignore
                        MistralAIEmbedding,
                    )
                except ImportError as e:
                    raise ImportError(
                        "Mistral dependencies not found, install with `poetry install --extras embeddings-mistral`"
                    ) from e

                api_key = settings.openai.api_key
                model = settings.openai.embedding_model

                self.embedding_model = MistralAIEmbedding(
                    api_key=api_key,
                    model=model,
                )
            case "mock":
                # Not a random number, is the dimensionality used by
                # the default embedding model
                self.embedding_model = MockEmbedding(384)
```

## File: `private_gpt/components/embedding/custom/sagemaker.py`
```python
# mypy: ignore-errors
import json
from typing import Any

import boto3
from llama_index.core.base.embeddings.base import BaseEmbedding
from pydantic import Field, PrivateAttr


class SagemakerEmbedding(BaseEmbedding):
    """Sagemaker Embedding Endpoint.

    To use, you must supply the endpoint name from your deployed
    Sagemaker embedding model & the region where it is deployed.

    To authenticate, the AWS client uses the following methods to
    automatically load credentials:
    https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html

    If a specific credential profile should be used, you must pass
    the name of the profile from the ~/.aws/credentials file that is to be used.

    Make sure the credentials / roles used have the required policies to
    access the Sagemaker endpoint.
    See: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html
    """

    endpoint_name: str = Field(description="")

    _boto_client: Any = boto3.client(
        "sagemaker-runtime",
    )  # TODO make it an optional field

    _async_not_implemented_warned: bool = PrivateAttr(default=False)

    @classmethod
    def class_name(cls) -> str:
        return "SagemakerEmbedding"

    def _async_not_implemented_warn_once(self) -> None:
        if not self._async_not_implemented_warned:
            print("Async embedding not available, falling back to sync method.")
            self._async_not_implemented_warned = True

    def _embed(self, sentences: list[str]) -> list[list[float]]:
        request_params = {
            "inputs": sentences,
        }

        resp = self._boto_client.invoke_endpoint(
            EndpointName=self.endpoint_name,
            Body=json.dumps(request_params),
            ContentType="application/json",
        )

        response_body = resp["Body"]
        response_str = response_body.read().decode("utf-8")
        response_json = json.loads(response_str)

        return response_json["vectors"]

    def _get_query_embedding(self, query: str) -> list[float]:
        """Get query embedding."""
        return self._embed([query])[0]

    async def _aget_query_embedding(self, query: str) -> list[float]:
        # Warn the user that sync is being used
        self._async_not_implemented_warn_once()
        return self._get_query_embedding(query)

    async def _aget_text_embedding(self, text: str) -> list[float]:
        # Warn the user that sync is being used
        self._async_not_implemented_warn_once()
        return self._get_text_embedding(text)

    def _get_text_embedding(self, text: str) -> list[float]:
        """Get text embedding."""
        return self._embed([text])[0]

    def _get_text_embeddings(self, texts: list[str]) -> list[list[float]]:
        """Get text embeddings."""
        return self._embed(texts)
```

## File: `private_gpt/components/ingest/ingest_component.py`
```python
import abc
import itertools
import logging
import multiprocessing
import multiprocessing.pool
import os
import threading
from pathlib import Path
from queue import Queue
from typing import Any

from llama_index.core.data_structs import IndexDict
from llama_index.core.embeddings.utils import EmbedType
from llama_index.core.indices import VectorStoreIndex, load_index_from_storage
from llama_index.core.indices.base import BaseIndex
from llama_index.core.ingestion import run_transformations
from llama_index.core.schema import BaseNode, Document, TransformComponent
from llama_index.core.storage import StorageContext

from private_gpt.components.ingest.ingest_helper import IngestionHelper
from private_gpt.paths import local_data_path
from private_gpt.settings.settings import Settings
from private_gpt.utils.eta import eta

logger = logging.getLogger(__name__)


class BaseIngestComponent(abc.ABC):
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: list[TransformComponent],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        logger.debug("Initializing base ingest component type=%s", type(self).__name__)
        self.storage_context = storage_context
        self.embed_model = embed_model
        self.transformations = transformations

    @abc.abstractmethod
    def ingest(self, file_name: str, file_data: Path) -> list[Document]:
        pass

    @abc.abstractmethod
    def bulk_ingest(self, files: list[tuple[str, Path]]) -> list[Document]:
        pass

    @abc.abstractmethod
    def delete(self, doc_id: str) -> None:
        pass


class BaseIngestComponentWithIndex(BaseIngestComponent, abc.ABC):
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: list[TransformComponent],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(storage_context, embed_model, transformations, *args, **kwargs)

        self.show_progress = True
        self._index_thread_lock = (
            threading.Lock()
        )  # Thread lock! Not Multiprocessing lock
        self._index = self._initialize_index()

    def _initialize_index(self) -> BaseIndex[IndexDict]:
        """Initialize the index from the storage context."""
        try:
            # Load the index with store_nodes_override=True to be able to delete them
            index = load_index_from_storage(
                storage_context=self.storage_context,
                store_nodes_override=True,  # Force store nodes in index and document stores
                show_progress=self.show_progress,
                embed_model=self.embed_model,
                transformations=self.transformations,
            )
        except ValueError:
            # There are no index in the storage context, creating a new one
            logger.info("Creating a new vector store index")
            index = VectorStoreIndex.from_documents(
                [],
                storage_context=self.storage_context,
                store_nodes_override=True,  # Force store nodes in index and document stores
                show_progress=self.show_progress,
                embed_model=self.embed_model,
                transformations=self.transformations,
            )
            index.storage_context.persist(persist_dir=local_data_path)
        return index

    def _save_index(self) -> None:
        self._index.storage_context.persist(persist_dir=local_data_path)

    def delete(self, doc_id: str) -> None:
        with self._index_thread_lock:
            # Delete the document from the index
            self._index.delete_ref_doc(doc_id, delete_from_docstore=True)

            # Save the index
            self._save_index()


class SimpleIngestComponent(BaseIngestComponentWithIndex):
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: list[TransformComponent],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(storage_context, embed_model, transformations, *args, **kwargs)

    def ingest(self, file_name: str, file_data: Path) -> list[Document]:
        logger.info("Ingesting file_name=%s", file_name)
        documents = IngestionHelper.transform_file_into_documents(file_name, file_data)
        logger.info(
            "Transformed file=%s into count=%s documents", file_name, len(documents)
        )
        logger.debug("Saving the documents in the index and doc store")
        return self._save_docs(documents)

    def bulk_ingest(self, files: list[tuple[str, Path]]) -> list[Document]:
        saved_documents = []
        for file_name, file_data in files:
            documents = IngestionHelper.transform_file_into_documents(
                file_name, file_data
            )
            saved_documents.extend(self._save_docs(documents))
        return saved_documents

    def _save_docs(self, documents: list[Document]) -> list[Document]:
        logger.debug("Transforming count=%s documents into nodes", len(documents))
        with self._index_thread_lock:
            for document in documents:
                self._index.insert(document, show_progress=True)
            logger.debug("Persisting the index and nodes")
            # persist the index and nodes
            self._save_index()
            logger.debug("Persisted the index and nodes")
        return documents


class BatchIngestComponent(BaseIngestComponentWithIndex):
    """Parallelize the file reading and parsing on multiple CPU core.

    This also makes the embeddings to be computed in batches (on GPU or CPU).
    """

    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: list[TransformComponent],
        count_workers: int,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(storage_context, embed_model, transformations, *args, **kwargs)
        # Make an efficient use of the CPU and GPU, the embedding
        # must be in the transformations
        assert (
            len(self.transformations) >= 2
        ), "Embeddings must be in the transformations"
        assert count_workers > 0, "count_workers must be > 0"
        self.count_workers = count_workers

        self._file_to_documents_work_pool = multiprocessing.Pool(
            processes=self.count_workers
        )

    def ingest(self, file_name: str, file_data: Path) -> list[Document]:
        logger.info("Ingesting file_name=%s", file_name)
        documents = IngestionHelper.transform_file_into_documents(file_name, file_data)
        logger.info(
            "Transformed file=%s into count=%s documents", file_name, len(documents)
        )
        logger.debug("Saving the documents in the index and doc store")
        return self._save_docs(documents)

    def bulk_ingest(self, files: list[tuple[str, Path]]) -> list[Document]:
        documents = list(
            itertools.chain.from_iterable(
                self._file_to_documents_work_pool.starmap(
                    IngestionHelper.transform_file_into_documents, files
                )
            )
        )
        logger.info(
            "Transformed count=%s files into count=%s documents",
            len(files),
            len(documents),
        )
        return self._save_docs(documents)

    def _save_docs(self, documents: list[Document]) -> list[Document]:
        logger.debug("Transforming count=%s documents into nodes", len(documents))
        nodes = run_transformations(
            documents,  # type: ignore[arg-type]
            self.transformations,
            show_progress=self.show_progress,
        )
        # Locking the index to avoid concurrent writes
        with self._index_thread_lock:
            logger.info("Inserting count=%s nodes in the index", len(nodes))
            self._index.insert_nodes(nodes, show_progress=True)
            for document in documents:
                self._index.docstore.set_document_hash(
                    document.get_doc_id(), document.hash
                )
            logger.debug("Persisting the index and nodes")
            # persist the index and nodes
            self._save_index()
            logger.debug("Persisted the index and nodes")
        return documents


class ParallelizedIngestComponent(BaseIngestComponentWithIndex):
    """Parallelize the file ingestion (file reading, embeddings, and index insertion).

    This use the CPU and GPU in parallel (both running at the same time), and
    reduce the memory pressure by not loading all the files in memory at the same time.
    """

    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: list[TransformComponent],
        count_workers: int,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(storage_context, embed_model, transformations, *args, **kwargs)
        # To make an efficient use of the CPU and GPU, the embeddings
        # must be in the transformations (to be computed in batches)
        assert (
            len(self.transformations) >= 2
        ), "Embeddings must be in the transformations"
        assert count_workers > 0, "count_workers must be > 0"
        self.count_workers = count_workers
        # We are doing our own multiprocessing
        # To do not collide with the multiprocessing of huggingface, we disable it
        os.environ["TOKENIZERS_PARALLELISM"] = "false"

        self._ingest_work_pool = multiprocessing.pool.ThreadPool(
            processes=self.count_workers
        )

        self._file_to_documents_work_pool = multiprocessing.Pool(
            processes=self.count_workers
        )

    def ingest(self, file_name: str, file_data: Path) -> list[Document]:
        logger.info("Ingesting file_name=%s", file_name)
        # Running in a single (1) process to release the current
        # thread, and take a dedicated CPU core for computation
        documents = self._file_to_documents_work_pool.apply(
            IngestionHelper.transform_file_into_documents, (file_name, file_data)
        )
        logger.info(
            "Transformed file=%s into count=%s documents", file_name, len(documents)
        )
        logger.debug("Saving the documents in the index and doc store")
        return self._save_docs(documents)

    def bulk_ingest(self, files: list[tuple[str, Path]]) -> list[Document]:
        # Lightweight threads, used for parallelize the
        # underlying IO calls made in the ingestion

        documents = list(
            itertools.chain.from_iterable(
                self._ingest_work_pool.starmap(self.ingest, files)
            )
        )
        return documents

    def _save_docs(self, documents: list[Document]) -> list[Document]:
        logger.debug("Transforming count=%s documents into nodes", len(documents))
        nodes = run_transformations(
            documents,  # type: ignore[arg-type]
            self.transformations,
            show_progress=self.show_progress,
        )
        # Locking the index to avoid concurrent writes
        with self._index_thread_lock:
            logger.info("Inserting count=%s nodes in the index", len(nodes))
            self._index.insert_nodes(nodes, show_progress=True)
            for document in documents:
                self._index.docstore.set_document_hash(
                    document.get_doc_id(), document.hash
                )
            logger.debug("Persisting the index and nodes")
            # persist the index and nodes
            self._save_index()
            logger.debug("Persisted the index and nodes")
        return documents

    def __del__(self) -> None:
        # We need to do the appropriate cleanup of the multiprocessing pools
        # when the object is deleted. Using root logger to avoid
        # the logger to be deleted before the pool
        logging.debug("Closing the ingest work pool")
        self._ingest_work_pool.close()
        self._ingest_work_pool.join()
        self._ingest_work_pool.terminate()
        logging.debug("Closing the file to documents work pool")
        self._file_to_documents_work_pool.close()
        self._file_to_documents_work_pool.join()
        self._file_to_documents_work_pool.terminate()


class PipelineIngestComponent(BaseIngestComponentWithIndex):
    """Pipeline ingestion - keeping the embedding worker pool as busy as possible.

    This class implements a threaded ingestion pipeline, which comprises two threads
    and two queues. The primary thread is responsible for reading and parsing files
    into documents. These documents are then placed into a queue, which is
    distributed to a pool of worker processes for embedding computation. After
    embedding, the documents are transferred to another queue where they are
    accumulated until a threshold is reached. Upon reaching this threshold, the
    accumulated documents are flushed to the document store, index, and vector
    store.

    Exception handling ensures robustness against erroneous files. However, in the
    pipelined design, one error can lead to the discarding of multiple files. Any
    discarded files will be reported.
    """

    NODE_FLUSH_COUNT = 5000  # Save the index every # nodes.

    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: list[TransformComponent],
        count_workers: int,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(storage_context, embed_model, transformations, *args, **kwargs)
        self.count_workers = count_workers
        assert (
            len(self.transformations) >= 2
        ), "Embeddings must be in the transformations"
        assert count_workers > 0, "count_workers must be > 0"
        self.count_workers = count_workers
        # We are doing our own multiprocessing
        # To do not collide with the multiprocessing of huggingface, we disable it
        os.environ["TOKENIZERS_PARALLELISM"] = "false"

        # doc_q stores parsed files as Document chunks.
        # Using a shallow queue causes the filesystem parser to block
        # when it reaches capacity. This ensures it doesn't outpace the
        # computationally intensive embeddings phase, avoiding unnecessary
        # memory consumption.  The semaphore is used to bound the async worker
        # embedding computations to cause the doc Q to fill and block.
        self.doc_semaphore = multiprocessing.Semaphore(
            self.count_workers
        )  # limit the doc queue to # items.
        self.doc_q: Queue[tuple[str, str | None, list[Document] | None]] = Queue(20)
        # node_q stores documents parsed into nodes (embeddings).
        # Larger queue size so we don't block the embedding workers during a slow
        # index update.
        self.node_q: Queue[
            tuple[str, str | None, list[Document] | None, list[BaseNode] | None]
        ] = Queue(40)
        threading.Thread(target=self._doc_to_node, daemon=True).start()
        threading.Thread(target=self._write_nodes, daemon=True).start()

    def _doc_to_node(self) -> None:
        # Parse documents into nodes
        with multiprocessing.pool.ThreadPool(processes=self.count_workers) as pool:
            while True:
                try:
                    cmd, file_name, documents = self.doc_q.get(
                        block=True
                    )  # Documents for a file
                    if cmd == "process":
                        # Push CPU/GPU embedding work to the worker pool
                        # Acquire semaphore to control access to worker pool
                        self.doc_semaphore.acquire()
                        pool.apply_async(
                            self._doc_to_node_worker, (file_name, documents)
                        )
                    elif cmd == "quit":
                        break
                finally:
                    if cmd != "process":
                        self.doc_q.task_done()  # unblock Q joins

    def _doc_to_node_worker(self, file_name: str, documents: list[Document]) -> None:
        # CPU/GPU intensive work in its own process
        try:
            nodes = run_transformations(
                documents,  # type: ignore[arg-type]
                self.transformations,
                show_progress=self.show_progress,
            )
            self.node_q.put(("process", file_name, documents, list(nodes)))
        finally:
            self.doc_semaphore.release()
            self.doc_q.task_done()  # unblock Q joins

    def _save_docs(
        self, files: list[str], documents: list[Document], nodes: list[BaseNode]
    ) -> None:
        try:
            logger.info(
                f"Saving {len(files)} files ({len(documents)} documents / {len(nodes)} nodes)"
            )
            self._index.insert_nodes(nodes)
            for document in documents:
                self._index.docstore.set_document_hash(
                    document.get_doc_id(), document.hash
                )
            self._save_index()
        except Exception:
            # Tell the user so they can investigate these files
            logger.exception(f"Processing files {files}")
        finally:
            # Clearing work, even on exception, maintains a clean state.
            nodes.clear()
            documents.clear()
            files.clear()

    def _write_nodes(self) -> None:
        # Save nodes to index.  I/O intensive.
        node_stack: list[BaseNode] = []
        doc_stack: list[Document] = []
        file_stack: list[str] = []
        while True:
            try:
                cmd, file_name, documents, nodes = self.node_q.get(block=True)
                if cmd in ("flush", "quit"):
                    if file_stack:
                        self._save_docs(file_stack, doc_stack, node_stack)
                    if cmd == "quit":
                        break
                elif cmd == "process":
                    node_stack.extend(nodes)  # type: ignore[arg-type]
                    doc_stack.extend(documents)  # type: ignore[arg-type]
                    file_stack.append(file_name)  # type: ignore[arg-type]
                    # Constant saving is heavy on I/O - accumulate to a threshold
                    if len(node_stack) >= self.NODE_FLUSH_COUNT:
                        self._save_docs(file_stack, doc_stack, node_stack)
            finally:
                self.node_q.task_done()

    def _flush(self) -> None:
        self.doc_q.put(("flush", None, None))
        self.doc_q.join()
        self.node_q.put(("flush", None, None, None))
        self.node_q.join()

    def ingest(self, file_name: str, file_data: Path) -> list[Document]:
        documents = IngestionHelper.transform_file_into_documents(file_name, file_data)
        self.doc_q.put(("process", file_name, documents))
        self._flush()
        return documents

    def bulk_ingest(self, files: list[tuple[str, Path]]) -> list[Document]:
        docs = []
        for file_name, file_data in eta(files):
            try:
                documents = IngestionHelper.transform_file_into_documents(
                    file_name, file_data
                )
                self.doc_q.put(("process", file_name, documents))
                docs.extend(documents)
            except Exception:
                logger.exception(f"Skipping {file_data.name}")
        self._flush()
        return docs


def get_ingestion_component(
    storage_context: StorageContext,
    embed_model: EmbedType,
    transformations: list[TransformComponent],
    settings: Settings,
) -> BaseIngestComponent:
    """Get the ingestion component for the given configuration."""
    ingest_mode = settings.embedding.ingest_mode
    if ingest_mode == "batch":
        return BatchIngestComponent(
            storage_context=storage_context,
            embed_model=embed_model,
            transformations=transformations,
            count_workers=settings.embedding.count_workers,
        )
    elif ingest_mode == "parallel":
        return ParallelizedIngestComponent(
            storage_context=storage_context,
            embed_model=embed_model,
            transformations=transformations,
            count_workers=settings.embedding.count_workers,
        )
    elif ingest_mode == "pipeline":
        return PipelineIngestComponent(
            storage_context=storage_context,
            embed_model=embed_model,
            transformations=transformations,
            count_workers=settings.embedding.count_workers,
        )
    else:
        return SimpleIngestComponent(
            storage_context=storage_context,
            embed_model=embed_model,
            transformations=transformations,
        )
```

## File: `private_gpt/components/ingest/ingest_helper.py`
```python
import logging
from pathlib import Path

from llama_index.core.readers import StringIterableReader
from llama_index.core.readers.base import BaseReader
from llama_index.core.readers.json import JSONReader
from llama_index.core.schema import Document

logger = logging.getLogger(__name__)


# Inspired by the `llama_index.core.readers.file.base` module
def _try_loading_included_file_formats() -> dict[str, type[BaseReader]]:
    try:
        from llama_index.readers.file.docs import (  # type: ignore
            DocxReader,
            HWPReader,
            PDFReader,
        )
        from llama_index.readers.file.epub import EpubReader  # type: ignore
        from llama_index.readers.file.image import ImageReader  # type: ignore
        from llama_index.readers.file.ipynb import IPYNBReader  # type: ignore
        from llama_index.readers.file.markdown import MarkdownReader  # type: ignore
        from llama_index.readers.file.mbox import MboxReader  # type: ignore
        from llama_index.readers.file.slides import PptxReader  # type: ignore
        from llama_index.readers.file.tabular import PandasCSVReader  # type: ignore
        from llama_index.readers.file.video_audio import (  # type: ignore
            VideoAudioReader,
        )
    except ImportError as e:
        raise ImportError("`llama-index-readers-file` package not found") from e

    default_file_reader_cls: dict[str, type[BaseReader]] = {
        ".hwp": HWPReader,
        ".pdf": PDFReader,
        ".docx": DocxReader,
        ".pptx": PptxReader,
        ".ppt": PptxReader,
        ".pptm": PptxReader,
        ".jpg": ImageReader,
        ".png": ImageReader,
        ".jpeg": ImageReader,
        ".mp3": VideoAudioReader,
        ".mp4": VideoAudioReader,
        ".csv": PandasCSVReader,
        ".epub": EpubReader,
        ".md": MarkdownReader,
        ".mbox": MboxReader,
        ".ipynb": IPYNBReader,
    }
    return default_file_reader_cls


# Patching the default file reader to support other file types
FILE_READER_CLS = _try_loading_included_file_formats()
FILE_READER_CLS.update(
    {
        ".json": JSONReader,
    }
)


class IngestionHelper:
    """Helper class to transform a file into a list of documents.

    This class should be used to transform a file into a list of documents.
    These methods are thread-safe (and multiprocessing-safe).
    """

    @staticmethod
    def transform_file_into_documents(
        file_name: str, file_data: Path
    ) -> list[Document]:
        documents = IngestionHelper._load_file_to_documents(file_name, file_data)
        for document in documents:
            document.metadata["file_name"] = file_name
        IngestionHelper._exclude_metadata(documents)
        return documents

    @staticmethod
    def _load_file_to_documents(file_name: str, file_data: Path) -> list[Document]:
        logger.debug("Transforming file_name=%s into documents", file_name)
        extension = Path(file_name).suffix
        reader_cls = FILE_READER_CLS.get(extension)
        if reader_cls is None:
            logger.debug(
                "No reader found for extension=%s, using default string reader",
                extension,
            )
            # Read as a plain text
            string_reader = StringIterableReader()
            return string_reader.load_data([file_data.read_text()])

        logger.debug("Specific reader found for extension=%s", extension)
        documents = reader_cls().load_data(file_data)

        # Sanitize NUL bytes in text which can't be stored in Postgres
        for i in range(len(documents)):
            documents[i].text = documents[i].text.replace("\u0000", "")

        return documents

    @staticmethod
    def _exclude_metadata(documents: list[Document]) -> None:
        logger.debug("Excluding metadata from count=%s documents", len(documents))
        for document in documents:
            document.metadata["doc_id"] = document.doc_id
            # We don't want the Embeddings search to receive this metadata
            document.excluded_embed_metadata_keys = ["doc_id"]
            # We don't want the LLM to receive these metadata in the context
            document.excluded_llm_metadata_keys = ["file_name", "doc_id", "page_label"]
```

## File: `private_gpt/components/llm/__init__.py`
```python
"""LLM implementations."""
```

## File: `private_gpt/components/llm/llm_component.py`
```python
import logging
from collections.abc import Callable
from typing import Any

from injector import inject, singleton
from llama_index.core.llms import LLM, MockLLM
from llama_index.core.settings import Settings as LlamaIndexSettings
from llama_index.core.utils import set_global_tokenizer
from transformers import AutoTokenizer  # type: ignore

from private_gpt.components.llm.prompt_helper import get_prompt_style
from private_gpt.paths import models_cache_path, models_path
from private_gpt.settings.settings import Settings

logger = logging.getLogger(__name__)


@singleton
class LLMComponent:
    llm: LLM

    @inject
    def __init__(self, settings: Settings) -> None:
        llm_mode = settings.llm.mode
        if settings.llm.tokenizer and settings.llm.mode != "mock":
            # Try to download the tokenizer. If it fails, the LLM will still work
            # using the default one, which is less accurate.
            try:
                set_global_tokenizer(
                    AutoTokenizer.from_pretrained(
                        pretrained_model_name_or_path=settings.llm.tokenizer,
                        cache_dir=str(models_cache_path),
                        token=settings.huggingface.access_token,
                    )
                )
            except Exception as e:
                logger.warning(
                    f"Failed to download tokenizer {settings.llm.tokenizer}: {e!s}"
                    f"Please follow the instructions in the documentation to download it if needed: "
                    f"https://docs.privategpt.dev/installation/getting-started/troubleshooting#tokenizer-setup."
                    f"Falling back to default tokenizer."
                )

        logger.info("Initializing the LLM in mode=%s", llm_mode)
        match settings.llm.mode:
            case "llamacpp":
                try:
                    from llama_index.llms.llama_cpp import LlamaCPP  # type: ignore
                except ImportError as e:
                    raise ImportError(
                        "Local dependencies not found, install with `poetry install --extras llms-llama-cpp`"
                    ) from e

                prompt_style = get_prompt_style(settings.llm.prompt_style)
                settings_kwargs = {
                    "tfs_z": settings.llamacpp.tfs_z,  # ollama and llama-cpp
                    "top_k": settings.llamacpp.top_k,  # ollama and llama-cpp
                    "top_p": settings.llamacpp.top_p,  # ollama and llama-cpp
                    "repeat_penalty": settings.llamacpp.repeat_penalty,  # ollama llama-cpp
                    "n_gpu_layers": -1,
                    "offload_kqv": True,
                }
                self.llm = LlamaCPP(
                    model_path=str(models_path / settings.llamacpp.llm_hf_model_file),
                    temperature=settings.llm.temperature,
                    max_new_tokens=settings.llm.max_new_tokens,
                    context_window=settings.llm.context_window,
                    generate_kwargs={},
                    callback_manager=LlamaIndexSettings.callback_manager,
                    # All to GPU
                    model_kwargs=settings_kwargs,
                    # transform inputs into Llama2 format
                    messages_to_prompt=prompt_style.messages_to_prompt,
                    completion_to_prompt=prompt_style.completion_to_prompt,
                    verbose=True,
                )

            case "sagemaker":
                try:
                    from private_gpt.components.llm.custom.sagemaker import SagemakerLLM
                except ImportError as e:
                    raise ImportError(
                        "Sagemaker dependencies not found, install with `poetry install --extras llms-sagemaker`"
                    ) from e

                self.llm = SagemakerLLM(
                    endpoint_name=settings.sagemaker.llm_endpoint_name,
                    max_new_tokens=settings.llm.max_new_tokens,
                    context_window=settings.llm.context_window,
                )
            case "openai":
                try:
                    from llama_index.llms.openai import OpenAI  # type: ignore
                except ImportError as e:
                    raise ImportError(
                        "OpenAI dependencies not found, install with `poetry install --extras llms-openai`"
                    ) from e

                openai_settings = settings.openai
                self.llm = OpenAI(
                    api_base=openai_settings.api_base,
                    api_key=openai_settings.api_key,
                    model=openai_settings.model,
                )
            case "openailike":
                try:
                    from llama_index.llms.openai_like import OpenAILike  # type: ignore
                except ImportError as e:
                    raise ImportError(
                        "OpenAILike dependencies not found, install with `poetry install --extras llms-openai-like`"
                    ) from e
                prompt_style = get_prompt_style(settings.llm.prompt_style)
                openai_settings = settings.openai
                self.llm = OpenAILike(
                    api_base=openai_settings.api_base,
                    api_key=openai_settings.api_key,
                    model=openai_settings.model,
                    is_chat_model=True,
                    max_tokens=settings.llm.max_new_tokens,
                    api_version="",
                    temperature=settings.llm.temperature,
                    context_window=settings.llm.context_window,
                    messages_to_prompt=prompt_style.messages_to_prompt,
                    completion_to_prompt=prompt_style.completion_to_prompt,
                    tokenizer=settings.llm.tokenizer,
                    timeout=openai_settings.request_timeout,
                    reuse_client=False,
                )
            case "ollama":
                try:
                    from llama_index.llms.ollama import Ollama  # type: ignore
                except ImportError as e:
                    raise ImportError(
                        "Ollama dependencies not found, install with `poetry install --extras llms-ollama`"
                    ) from e

                ollama_settings = settings.ollama

                settings_kwargs = {
                    "tfs_z": ollama_settings.tfs_z,  # ollama and llama-cpp
                    "num_predict": ollama_settings.num_predict,  # ollama only
                    "top_k": ollama_settings.top_k,  # ollama and llama-cpp
                    "top_p": ollama_settings.top_p,  # ollama and llama-cpp
                    "repeat_last_n": ollama_settings.repeat_last_n,  # ollama
                    "repeat_penalty": ollama_settings.repeat_penalty,  # ollama llama-cpp
                }

                # calculate llm model. If not provided tag, it will be use latest
                model_name = (
                    ollama_settings.llm_model + ":latest"
                    if ":" not in ollama_settings.llm_model
                    else ollama_settings.llm_model
                )

                llm = Ollama(
                    model=model_name,
                    base_url=ollama_settings.api_base,
                    temperature=settings.llm.temperature,
                    context_window=settings.llm.context_window,
                    additional_kwargs=settings_kwargs,
                    request_timeout=ollama_settings.request_timeout,
                )

                if ollama_settings.autopull_models:
                    from private_gpt.utils.ollama import check_connection, pull_model

                    if not check_connection(llm.client):
                        raise ValueError(
                            f"Failed to connect to Ollama, "
                            f"check if Ollama server is running on {ollama_settings.api_base}"
                        )
                    pull_model(llm.client, model_name)

                if (
                    ollama_settings.keep_alive
                    != ollama_settings.model_fields["keep_alive"].default
                ):
                    # Modify Ollama methods to use the "keep_alive" field.
                    def add_keep_alive(func: Callable[..., Any]) -> Callable[..., Any]:
                        def wrapper(*args: Any, **kwargs: Any) -> Any:
                            kwargs["keep_alive"] = ollama_settings.keep_alive
                            return func(*args, **kwargs)

                        return wrapper

                    Ollama.chat = add_keep_alive(Ollama.chat)  # type: ignore
                    Ollama.stream_chat = add_keep_alive(Ollama.stream_chat)  # type: ignore
                    Ollama.complete = add_keep_alive(Ollama.complete)  # type: ignore
                    Ollama.stream_complete = add_keep_alive(Ollama.stream_complete)  # type: ignore

                self.llm = llm

            case "azopenai":
                try:
                    from llama_index.llms.azure_openai import (  # type: ignore
                        AzureOpenAI,
                    )
                except ImportError as e:
                    raise ImportError(
                        "Azure OpenAI dependencies not found, install with `poetry install --extras llms-azopenai`"
                    ) from e

                azopenai_settings = settings.azopenai
                self.llm = AzureOpenAI(
                    model=azopenai_settings.llm_model,
                    deployment_name=azopenai_settings.llm_deployment_name,
                    api_key=azopenai_settings.api_key,
                    azure_endpoint=azopenai_settings.azure_endpoint,
                    api_version=azopenai_settings.api_version,
                )
            case "gemini":
                try:
                    from llama_index.llms.gemini import (  # type: ignore
                        Gemini,
                    )
                except ImportError as e:
                    raise ImportError(
                        "Google Gemini dependencies not found, install with `poetry install --extras llms-gemini`"
                    ) from e
                gemini_settings = settings.gemini
                self.llm = Gemini(
                    model_name=gemini_settings.model, api_key=gemini_settings.api_key
                )
            case "mock":
                self.llm = MockLLM()
```

## File: `private_gpt/components/llm/prompt_helper.py`
```python
import abc
import logging
from collections.abc import Sequence
from typing import Any, Literal

from llama_index.core.llms import ChatMessage, MessageRole

logger = logging.getLogger(__name__)


class AbstractPromptStyle(abc.ABC):
    """Abstract class for prompt styles.

    This class is used to format a series of messages into a prompt that can be
    understood by the models. A series of messages represents the interaction(s)
    between a user and an assistant. This series of messages can be considered as a
    session between a user X and an assistant Y.This session holds, through the
    messages, the state of the conversation. This session, to be understood by the
    model, needs to be formatted into a prompt (i.e. a string that the models
    can understand). Prompts can be formatted in different ways,
    depending on the model.

    The implementations of this class represent the different ways to format a
    series of messages into a prompt.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        logger.debug("Initializing prompt_style=%s", self.__class__.__name__)

    @abc.abstractmethod
    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str:
        pass

    @abc.abstractmethod
    def _completion_to_prompt(self, completion: str) -> str:
        pass

    def messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str:
        prompt = self._messages_to_prompt(messages)
        logger.debug("Got for messages='%s' the prompt='%s'", messages, prompt)
        return prompt

    def completion_to_prompt(self, prompt: str) -> str:
        completion = prompt  # Fix: Llama-index parameter has to be named as prompt
        prompt = self._completion_to_prompt(completion)
        logger.debug("Got for completion='%s' the prompt='%s'", completion, prompt)
        return prompt


class DefaultPromptStyle(AbstractPromptStyle):
    """Default prompt style that uses the defaults from llama_utils.

    It basically passes None to the LLM, indicating it should use
    the default functions.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        # Hacky way to override the functions
        # Override the functions to be None, and pass None to the LLM.
        self.messages_to_prompt = None  # type: ignore[method-assign, assignment]
        self.completion_to_prompt = None  # type: ignore[method-assign, assignment]

    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str:
        return ""

    def _completion_to_prompt(self, completion: str) -> str:
        return ""


class Llama2PromptStyle(AbstractPromptStyle):
    """Simple prompt style that uses llama 2 prompt style.

    Inspired by llama_index/legacy/llms/llama_utils.py

    It transforms the sequence of messages into a prompt that should look like:
    ```text
    <s> [INST] <<SYS>> your system prompt here. <</SYS>>

    user message here [/INST] assistant (model) response here </s>
    ```
    """

    BOS, EOS = "<s>", "</s>"
    B_INST, E_INST = "[INST]", "[/INST]"
    B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
    DEFAULT_SYSTEM_PROMPT = """\
    You are a helpful, respectful and honest assistant. \
    Always answer as helpfully as possible and follow ALL given instructions. \
    Do not speculate or make up information. \
    Do not reference any given instructions or context. \
    """

    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str:
        string_messages: list[str] = []
        if messages[0].role == MessageRole.SYSTEM:
            # pull out the system message (if it exists in messages)
            system_message_str = messages[0].content or ""
            messages = messages[1:]
        else:
            system_message_str = self.DEFAULT_SYSTEM_PROMPT

        system_message_str = f"{self.B_SYS} {system_message_str.strip()} {self.E_SYS}"

        for i in range(0, len(messages), 2):
            # first message should always be a user
            user_message = messages[i]
            assert user_message.role == MessageRole.USER

            if i == 0:
                # make sure system prompt is included at the start
                str_message = f"{self.BOS} {self.B_INST} {system_message_str} "
            else:
                # end previous user-assistant interaction
                string_messages[-1] += f" {self.EOS}"
                # no need to include system prompt
                str_message = f"{self.BOS} {self.B_INST} "

            # include user message content
            str_message += f"{user_message.content} {self.E_INST}"

            if len(messages) > (i + 1):
                # if assistant message exists, add to str_message
                assistant_message = messages[i + 1]
                assert assistant_message.role == MessageRole.ASSISTANT
                str_message += f" {assistant_message.content}"

            string_messages.append(str_message)

        return "".join(string_messages)

    def _completion_to_prompt(self, completion: str) -> str:
        system_prompt_str = self.DEFAULT_SYSTEM_PROMPT

        return (
            f"{self.BOS} {self.B_INST} {self.B_SYS} {system_prompt_str.strip()} {self.E_SYS} "
            f"{completion.strip()} {self.E_INST}"
        )


class Llama3PromptStyle(AbstractPromptStyle):
    r"""Template for Meta's Llama 3.1.

    The format follows this structure:
    <|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>

    [System message content]<|eot_id|>
    <|start_header_id|>user<|end_header_id|>

    [User message content]<|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>

    [Assistant message content]<|eot_id|>
    ...
    (Repeat for each message, including possible 'ipython' role)
    """

    BOS, EOS = "<|begin_of_text|>", "<|end_of_text|>"
    B_INST, E_INST = "<|start_header_id|>", "<|end_header_id|>"
    EOT = "<|eot_id|>"
    B_SYS, E_SYS = "<|start_header_id|>system<|end_header_id|>", "<|eot_id|>"
    ASSISTANT_INST = "<|start_header_id|>assistant<|end_header_id|>"
    DEFAULT_SYSTEM_PROMPT = """\
    You are a helpful, respectful and honest assistant. \
    Always answer as helpfully as possible and follow ALL given instructions. \
    Do not speculate or make up information. \
    Do not reference any given instructions or context. \
    """

    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str:
        prompt = ""
        has_system_message = False

        for i, message in enumerate(messages):
            if not message or message.content is None:
                continue
            if message.role == MessageRole.SYSTEM:
                prompt += f"{self.B_SYS}\n\n{message.content.strip()}{self.E_SYS}"
                has_system_message = True
            else:
                role_header = f"{self.B_INST}{message.role.value}{self.E_INST}"
                prompt += f"{role_header}\n\n{message.content.strip()}{self.EOT}"

            # Add assistant header if the last message is not from the assistant
            if i == len(messages) - 1 and message.role != MessageRole.ASSISTANT:
                prompt += f"{self.ASSISTANT_INST}\n\n"

        # Add default system prompt if no system message was provided
        if not has_system_message:
            prompt = (
                f"{self.B_SYS}\n\n{self.DEFAULT_SYSTEM_PROMPT}{self.E_SYS}" + prompt
            )

        # TODO: Implement tool handling logic

        return prompt

    def _completion_to_prompt(self, completion: str) -> str:
        return (
            f"{self.B_SYS}\n\n{self.DEFAULT_SYSTEM_PROMPT}{self.E_SYS}"
            f"{self.B_INST}user{self.E_INST}\n\n{completion.strip()}{self.EOT}"
            f"{self.ASSISTANT_INST}\n\n"
        )


class TagPromptStyle(AbstractPromptStyle):
    """Tag prompt style (used by Vigogne) that uses the prompt style `<|ROLE|>`.

    It transforms the sequence of messages into a prompt that should look like:
    ```text
    <|system|>: your system prompt here.
    <|user|>: user message here
    (possibly with context and question)
    <|assistant|>: assistant (model) response here.
    ```

    FIXME: should we add surrounding `<s>` and `</s>` tags, like in llama2?
    """

    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str:
        """Format message to prompt with `<|ROLE|>: MSG` style."""
        prompt = ""
        for message in messages:
            role = message.role
            content = message.content or ""
            message_from_user = f"<|{role.lower()}|>: {content.strip()}"
            message_from_user += "\n"
            prompt += message_from_user
        # we are missing the last <|assistant|> tag that will trigger a completion
        prompt += "<|assistant|>: "
        return prompt

    def _completion_to_prompt(self, completion: str) -> str:
        return self._messages_to_prompt(
            [ChatMessage(content=completion, role=MessageRole.USER)]
        )


class MistralPromptStyle(AbstractPromptStyle):
    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str:
        inst_buffer = []
        text = ""
        for message in messages:
            if message.role == MessageRole.SYSTEM or message.role == MessageRole.USER:
                inst_buffer.append(str(message.content).strip())
            elif message.role == MessageRole.ASSISTANT:
                text += "<s>[INST] " + "\n".join(inst_buffer) + " [/INST]"
                text += " " + str(message.content).strip() + "</s>"
                inst_buffer.clear()
            else:
                raise ValueError(f"Unknown message role {message.role}")

        if len(inst_buffer) > 0:
            text += "<s>[INST] " + "\n".join(inst_buffer) + " [/INST]"

        return text

    def _completion_to_prompt(self, completion: str) -> str:
        return self._messages_to_prompt(
            [ChatMessage(content=completion, role=MessageRole.USER)]
        )


class ChatMLPromptStyle(AbstractPromptStyle):
    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str:
        prompt = "<|im_start|>system\n"
        for message in messages:
            role = message.role
            content = message.content or ""
            if role.lower() == "system":
                message_from_user = f"{content.strip()}"
                prompt += message_from_user
            elif role.lower() == "user":
                prompt += "<|im_end|>\n<|im_start|>user\n"
                message_from_user = f"{content.strip()}<|im_end|>\n"
                prompt += message_from_user
        prompt += "<|im_start|>assistant\n"
        return prompt

    def _completion_to_prompt(self, completion: str) -> str:
        return self._messages_to_prompt(
            [ChatMessage(content=completion, role=MessageRole.USER)]
        )


def get_prompt_style(
    prompt_style: (
        Literal["default", "llama2", "llama3", "tag", "mistral", "chatml"] | None
    )
) -> AbstractPromptStyle:
    """Get the prompt style to use from the given string.

    :param prompt_style: The prompt style to use.
    :return: The prompt style to use.
    """
    if prompt_style is None or prompt_style == "default":
        return DefaultPromptStyle()
    elif prompt_style == "llama2":
        return Llama2PromptStyle()
    elif prompt_style == "llama3":
        return Llama3PromptStyle()
    elif prompt_style == "tag":
        return TagPromptStyle()
    elif prompt_style == "mistral":
        return MistralPromptStyle()
    elif prompt_style == "chatml":
        return ChatMLPromptStyle()
    raise ValueError(f"Unknown prompt_style='{prompt_style}'")
```

## File: `private_gpt/components/llm/custom/sagemaker.py`
```python
# mypy: ignore-errors
from __future__ import annotations

import io
import json
import logging
from typing import TYPE_CHECKING, Any

import boto3  # type: ignore
from llama_index.core.base.llms.generic_utils import (
    completion_response_to_chat_response,
    stream_completion_response_to_chat_response,
)
from llama_index.core.bridge.pydantic import Field
from llama_index.core.llms import (
    CompletionResponse,
    CustomLLM,
    LLMMetadata,
)
from llama_index.core.llms.callbacks import (
    llm_chat_callback,
    llm_completion_callback,
)

if TYPE_CHECKING:
    from collections.abc import Sequence

    from llama_index.callbacks import CallbackManager
    from llama_index.llms import (
        ChatMessage,
        ChatResponse,
        ChatResponseGen,
        CompletionResponseGen,
    )

logger = logging.getLogger(__name__)


class LineIterator:
    r"""A helper class for parsing the byte stream input from TGI container.

    The output of the model will be in the following format:
    ```
    b'data:{"token": {"text": " a"}}\n\n'
    b'data:{"token": {"text": " challenging"}}\n\n'
    b'data:{"token": {"text": " problem"
    b'}}'
    ...
    ```

    While usually each PayloadPart event from the event stream will contain a byte array
    with a full json, this is not guaranteed and some of the json objects may be split
    across PayloadPart events. For example:
    ```
    {'PayloadPart': {'Bytes': b'{"outputs": '}}
    {'PayloadPart': {'Bytes': b'[" problem"]}\n'}}
    ```


    This class accounts for this by concatenating bytes written via the 'write' function
    and then exposing a method which will return lines (ending with a '\n' character)
    within the buffer via the 'scan_lines' function. It maintains the position of the
    last read position to ensure that previous bytes are not exposed again. It will
    also save any pending lines that doe not end with a '\n' to make sure truncations
    are concatinated
    """

    def __init__(self, stream: Any) -> None:
        """Line iterator initializer."""
        self.byte_iterator = iter(stream)
        self.buffer = io.BytesIO()
        self.read_pos = 0

    def __iter__(self) -> Any:
        """Self iterator."""
        return self

    def __next__(self) -> Any:
        """Next element from iterator."""
        while True:
            self.buffer.seek(self.read_pos)
            line = self.buffer.readline()
            if line and line[-1] == ord("\n"):
                self.read_pos += len(line)
                return line[:-1]
            try:
                chunk = next(self.byte_iterator)
            except StopIteration:
                if self.read_pos < self.buffer.getbuffer().nbytes:
                    continue
                raise
            if "PayloadPart" not in chunk:
                logger.warning("Unknown event type=%s", chunk)
                continue
            self.buffer.seek(0, io.SEEK_END)
            self.buffer.write(chunk["PayloadPart"]["Bytes"])


class SagemakerLLM(CustomLLM):
    """Sagemaker Inference Endpoint models.

    To use, you must supply the endpoint name from your deployed
    Sagemaker model & the region where it is deployed.

    To authenticate, the AWS client uses the following methods to
    automatically load credentials:
    https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html

    If a specific credential profile should be used, you must pass
    the name of the profile from the ~/.aws/credentials file that is to be used.

    Make sure the credentials / roles used have the required policies to
    access the Sagemaker endpoint.
    See: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html
    """

    endpoint_name: str = Field(description="")
    temperature: float = Field(description="The temperature to use for sampling.")
    max_new_tokens: int = Field(description="The maximum number of tokens to generate.")
    context_window: int = Field(
        description="The maximum number of context tokens for the model."
    )
    messages_to_prompt: Any = Field(
        description="The function to convert messages to a prompt.", exclude=True
    )
    completion_to_prompt: Any = Field(
        description="The function to convert a completion to a prompt.", exclude=True
    )
    generate_kwargs: dict[str, Any] = Field(
        default_factory=dict, description="Kwargs used for generation."
    )
    model_kwargs: dict[str, Any] = Field(
        default_factory=dict, description="Kwargs used for model initialization."
    )
    verbose: bool = Field(description="Whether to print verbose output.")

    _boto_client: Any = boto3.client(
        "sagemaker-runtime",
    )  # TODO make it an optional field

    def __init__(
        self,
        endpoint_name: str | None = "",
        temperature: float = 0.1,
        max_new_tokens: int = 512,  # to review defaults
        context_window: int = 2048,  # to review defaults
        messages_to_prompt: Any = None,
        completion_to_prompt: Any = None,
        callback_manager: CallbackManager | None = None,
        generate_kwargs: dict[str, Any] | None = None,
        model_kwargs: dict[str, Any] | None = None,
        verbose: bool = True,
    ) -> None:
        """SagemakerLLM initializer."""
        model_kwargs = model_kwargs or {}
        model_kwargs.update({"n_ctx": context_window, "verbose": verbose})

        messages_to_prompt = messages_to_prompt or {}
        completion_to_prompt = completion_to_prompt or {}

        generate_kwargs = generate_kwargs or {}
        generate_kwargs.update(
            {"temperature": temperature, "max_tokens": max_new_tokens}
        )

        super().__init__(
            endpoint_name=endpoint_name,
            temperature=temperature,
            context_window=context_window,
            max_new_tokens=max_new_tokens,
            messages_to_prompt=messages_to_prompt,
            completion_to_prompt=completion_to_prompt,
            callback_manager=callback_manager,
            generate_kwargs=generate_kwargs,
            model_kwargs=model_kwargs,
            verbose=verbose,
        )

    @property
    def inference_params(self):
        # TODO expose the rest of params
        return {
            "do_sample": True,
            "top_p": 0.7,
            "temperature": self.temperature,
            "top_k": 50,
            "max_new_tokens": self.max_new_tokens,
        }

    @property
    def metadata(self) -> LLMMetadata:
        """Get LLM metadata."""
        return LLMMetadata(
            context_window=self.context_window,
            num_output=self.max_new_tokens,
            model_name="Sagemaker LLama 2",
        )

    @llm_completion_callback()
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse:
        self.generate_kwargs.update({"stream": False})

        is_formatted = kwargs.pop("formatted", False)
        if not is_formatted:
            prompt = self.completion_to_prompt(prompt)

        request_params = {
            "inputs": prompt,
            "stream": False,
            "parameters": self.inference_params,
        }

        resp = self._boto_client.invoke_endpoint(
            EndpointName=self.endpoint_name,
            Body=json.dumps(request_params),
            ContentType="application/json",
        )

        response_body = resp["Body"]
        response_str = response_body.read().decode("utf-8")
        response_dict = json.loads(response_str)

        return CompletionResponse(
            text=response_dict[0]["generated_text"][len(prompt) :], raw=resp
        )

    @llm_completion_callback()
    def stream_complete(self, prompt: str, **kwargs: Any) -> CompletionResponseGen:
        def get_stream():
            text = ""

            request_params = {
                "inputs": prompt,
                "stream": True,
                "parameters": self.inference_params,
            }
            resp = self._boto_client.invoke_endpoint_with_response_stream(
                EndpointName=self.endpoint_name,
                Body=json.dumps(request_params),
                ContentType="application/json",
            )

            event_stream = resp["Body"]
            start_json = b"{"
            stop_token = "<|endoftext|>"
            first_token = True

            for line in LineIterator(event_stream):
                if line != b"" and start_json in line:
                    data = json.loads(line[line.find(start_json) :].decode("utf-8"))
                    special = data["token"]["special"]
                    stop = data["token"]["text"] == stop_token
                    if not special and not stop:
                        delta = data["token"]["text"]
                        # trim the leading space for the first token if present
                        if first_token:
                            delta = delta.lstrip()
                            first_token = False
                        text += delta
                        yield CompletionResponse(delta=delta, text=text, raw=data)

        return get_stream()

    @llm_chat_callback()
    def chat(self, messages: Sequence[ChatMessage], **kwargs: Any) -> ChatResponse:
        prompt = self.messages_to_prompt(messages)
        completion_response = self.complete(prompt, formatted=True, **kwargs)
        return completion_response_to_chat_response(completion_response)

    @llm_chat_callback()
    def stream_chat(
        self, messages: Sequence[ChatMessage], **kwargs: Any
    ) -> ChatResponseGen:
        prompt = self.messages_to_prompt(messages)
        completion_response = self.stream_complete(prompt, formatted=True, **kwargs)
        return stream_completion_response_to_chat_response(completion_response)
```

## File: `private_gpt/components/node_store/node_store_component.py`
```python
import logging

from injector import inject, singleton
from llama_index.core.storage.docstore import BaseDocumentStore, SimpleDocumentStore
from llama_index.core.storage.index_store import SimpleIndexStore
from llama_index.core.storage.index_store.types import BaseIndexStore

from private_gpt.paths import local_data_path
from private_gpt.settings.settings import Settings

logger = logging.getLogger(__name__)


@singleton
class NodeStoreComponent:
    index_store: BaseIndexStore
    doc_store: BaseDocumentStore

    @inject
    def __init__(self, settings: Settings) -> None:
        match settings.nodestore.database:
            case "simple":
                try:
                    self.index_store = SimpleIndexStore.from_persist_dir(
                        persist_dir=str(local_data_path)
                    )
                except FileNotFoundError:
                    logger.debug("Local index store not found, creating a new one")
                    self.index_store = SimpleIndexStore()

                try:
                    self.doc_store = SimpleDocumentStore.from_persist_dir(
                        persist_dir=str(local_data_path)
                    )
                except FileNotFoundError:
                    logger.debug("Local document store not found, creating a new one")
                    self.doc_store = SimpleDocumentStore()

            case "postgres":
                try:
                    from llama_index.storage.docstore.postgres import (  # type: ignore
                        PostgresDocumentStore,
                    )
                    from llama_index.storage.index_store.postgres import (  # type: ignore
                        PostgresIndexStore,
                    )
                except ImportError:
                    raise ImportError(
                        "Postgres dependencies not found, install with `poetry install --extras storage-nodestore-postgres`"
                    ) from None

                if settings.postgres is None:
                    raise ValueError("Postgres index/doc store settings not found.")

                self.index_store = PostgresIndexStore.from_params(
                    **settings.postgres.model_dump(exclude_none=True)
                )

                self.doc_store = PostgresDocumentStore.from_params(
                    **settings.postgres.model_dump(exclude_none=True)
                )

            case _:
                # Should be unreachable
                # The settings validator should have caught this
                raise ValueError(
                    f"Database {settings.nodestore.database} not supported"
                )
```

## File: `private_gpt/components/vector_store/batched_chroma.py`
```python
from collections.abc import Generator, Sequence
from typing import TYPE_CHECKING, Any

from llama_index.core.schema import BaseNode, MetadataMode
from llama_index.core.vector_stores.utils import node_to_metadata_dict
from llama_index.vector_stores.chroma import ChromaVectorStore  # type: ignore

if TYPE_CHECKING:
    from collections.abc import Mapping


def chunk_list(
    lst: Sequence[BaseNode], max_chunk_size: int
) -> Generator[Sequence[BaseNode], None, None]:
    """Yield successive max_chunk_size-sized chunks from lst.

    Args:
        lst (List[BaseNode]): list of nodes with embeddings
        max_chunk_size (int): max chunk size

    Yields:
        Generator[List[BaseNode], None, None]: list of nodes with embeddings
    """
    for i in range(0, len(lst), max_chunk_size):
        yield lst[i : i + max_chunk_size]


class BatchedChromaVectorStore(ChromaVectorStore):  # type: ignore
    """Chroma vector store, batching additions to avoid reaching the max batch limit.

    In this vector store, embeddings are stored within a ChromaDB collection.

    During query time, the index uses ChromaDB to query for the top
    k most similar nodes.

    Args:
        chroma_client (from chromadb.api.API):
            API instance
        chroma_collection (chromadb.api.models.Collection.Collection):
            ChromaDB collection instance

    """

    chroma_client: Any | None

    def __init__(
        self,
        chroma_client: Any,
        chroma_collection: Any,
        host: str | None = None,
        port: str | None = None,
        ssl: bool = False,
        headers: dict[str, str] | None = None,
        collection_kwargs: dict[Any, Any] | None = None,
    ) -> None:
        super().__init__(
            chroma_collection=chroma_collection,
            host=host,
            port=port,
            ssl=ssl,
            headers=headers,
            collection_kwargs=collection_kwargs or {},
        )
        self.chroma_client = chroma_client

    def add(self, nodes: Sequence[BaseNode], **add_kwargs: Any) -> list[str]:
        """Add nodes to index, batching the insertion to avoid issues.

        Args:
            nodes: List[BaseNode]: list of nodes with embeddings
            add_kwargs: _
        """
        if not self.chroma_client:
            raise ValueError("Client not initialized")

        if not self._collection:
            raise ValueError("Collection not initialized")

        max_chunk_size = self.chroma_client.max_batch_size
        node_chunks = chunk_list(nodes, max_chunk_size)

        all_ids = []
        for node_chunk in node_chunks:
            embeddings: list[Sequence[float]] = []
            metadatas: list[Mapping[str, Any]] = []
            ids = []
            documents = []
            for node in node_chunk:
                embeddings.append(node.get_embedding())
                metadatas.append(
                    node_to_metadata_dict(
                        node, remove_text=True, flat_metadata=self.flat_metadata
                    )
                )
                ids.append(node.node_id)
                documents.append(node.get_content(metadata_mode=MetadataMode.NONE))

            self._collection.add(
                embeddings=embeddings,
                ids=ids,
                metadatas=metadatas,
                documents=documents,
            )
            all_ids.extend(ids)

        return all_ids
```

## File: `private_gpt/components/vector_store/vector_store_component.py`
```python
import logging
import typing

from injector import inject, singleton
from llama_index.core.indices.vector_store import VectorIndexRetriever, VectorStoreIndex
from llama_index.core.vector_stores.types import (
    BasePydanticVectorStore,
    FilterCondition,
    MetadataFilter,
    MetadataFilters,
)

from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.paths import local_data_path
from private_gpt.settings.settings import Settings

logger = logging.getLogger(__name__)


def _doc_id_metadata_filter(
    context_filter: ContextFilter | None,
) -> MetadataFilters:
    filters = MetadataFilters(filters=[], condition=FilterCondition.OR)

    if context_filter is not None and context_filter.docs_ids is not None:
        for doc_id in context_filter.docs_ids:
            filters.filters.append(MetadataFilter(key="doc_id", value=doc_id))

    return filters


@singleton
class VectorStoreComponent:
    settings: Settings
    vector_store: BasePydanticVectorStore

    @inject
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        match settings.vectorstore.database:
            case "postgres":
                try:
                    from llama_index.vector_stores.postgres import (  # type: ignore
                        PGVectorStore,
                    )
                except ImportError as e:
                    raise ImportError(
                        "Postgres dependencies not found, install with `poetry install --extras vector-stores-postgres`"
                    ) from e

                if settings.postgres is None:
                    raise ValueError(
                        "Postgres settings not found. Please provide settings."
                    )

                self.vector_store = typing.cast(
                    BasePydanticVectorStore,
                    PGVectorStore.from_params(
                        **settings.postgres.model_dump(exclude_none=True),
                        table_name="embeddings",
                        embed_dim=settings.embedding.embed_dim,
                    ),
                )

            case "chroma":
                try:
                    import chromadb  # type: ignore
                    from chromadb.config import (  # type: ignore
                        Settings as ChromaSettings,
                    )

                    from private_gpt.components.vector_store.batched_chroma import (
                        BatchedChromaVectorStore,
                    )
                except ImportError as e:
                    raise ImportError(
                        "ChromaDB dependencies not found, install with `poetry install --extras vector-stores-chroma`"
                    ) from e

                chroma_settings = ChromaSettings(anonymized_telemetry=False)
                chroma_client = chromadb.PersistentClient(
                    path=str((local_data_path / "chroma_db").absolute()),
                    settings=chroma_settings,
                )
                chroma_collection = chroma_client.get_or_create_collection(
                    "make_this_parameterizable_per_api_call"
                )  # TODO

                self.vector_store = typing.cast(
                    BasePydanticVectorStore,
                    BatchedChromaVectorStore(
                        chroma_client=chroma_client, chroma_collection=chroma_collection
                    ),
                )

            case "qdrant":
                try:
                    from llama_index.vector_stores.qdrant import (  # type: ignore
                        QdrantVectorStore,
                    )
                    from qdrant_client import QdrantClient  # type: ignore
                except ImportError as e:
                    raise ImportError(
                        "Qdrant dependencies not found, install with `poetry install --extras vector-stores-qdrant`"
                    ) from e

                if settings.qdrant is None:
                    logger.info(
                        "Qdrant config not found. Using default settings."
                        "Trying to connect to Qdrant at localhost:6333."
                    )
                    client = QdrantClient()
                else:
                    client = QdrantClient(
                        **settings.qdrant.model_dump(exclude_none=True)
                    )
                self.vector_store = typing.cast(
                    BasePydanticVectorStore,
                    QdrantVectorStore(
                        client=client,
                        collection_name="make_this_parameterizable_per_api_call",
                    ),  # TODO
                )

            case "milvus":
                try:
                    from llama_index.vector_stores.milvus import (  # type: ignore
                        MilvusVectorStore,
                    )
                except ImportError as e:
                    raise ImportError(
                        "Milvus dependencies not found, install with `poetry install --extras vector-stores-milvus`"
                    ) from e

                if settings.milvus is None:
                    logger.info(
                        "Milvus config not found. Using default settings.\n"
                        "Trying to connect to Milvus at local_data/private_gpt/milvus/milvus_local.db "
                        "with collection 'make_this_parameterizable_per_api_call'."
                    )

                    self.vector_store = typing.cast(
                        BasePydanticVectorStore,
                        MilvusVectorStore(
                            dim=settings.embedding.embed_dim,
                            collection_name="make_this_parameterizable_per_api_call",
                            overwrite=True,
                        ),
                    )

                else:
                    self.vector_store = typing.cast(
                        BasePydanticVectorStore,
                        MilvusVectorStore(
                            dim=settings.embedding.embed_dim,
                            uri=settings.milvus.uri,
                            token=settings.milvus.token,
                            collection_name=settings.milvus.collection_name,
                            overwrite=settings.milvus.overwrite,
                        ),
                    )

            case "clickhouse":
                try:
                    from clickhouse_connect import (  # type: ignore
                        get_client,
                    )
                    from llama_index.vector_stores.clickhouse import (  # type: ignore
                        ClickHouseVectorStore,
                    )
                except ImportError as e:
                    raise ImportError(
                        "ClickHouse dependencies not found, install with `poetry install --extras vector-stores-clickhouse`"
                    ) from e

                if settings.clickhouse is None:
                    raise ValueError(
                        "ClickHouse settings not found. Please provide settings."
                    )

                clickhouse_client = get_client(
                    host=settings.clickhouse.host,
                    port=settings.clickhouse.port,
                    username=settings.clickhouse.username,
                    password=settings.clickhouse.password,
                )
                self.vector_store = ClickHouseVectorStore(
                    clickhouse_client=clickhouse_client
                )
            case _:
                # Should be unreachable
                # The settings validator should have caught this
                raise ValueError(
                    f"Vectorstore database {settings.vectorstore.database} not supported"
                )

    def get_retriever(
        self,
        index: VectorStoreIndex,
        context_filter: ContextFilter | None = None,
        similarity_top_k: int = 2,
    ) -> VectorIndexRetriever:
        # This way we support qdrant (using doc_ids) and the rest (using filters)
        return VectorIndexRetriever(
            index=index,
            similarity_top_k=similarity_top_k,
            doc_ids=context_filter.docs_ids if context_filter else None,
            filters=(
                _doc_id_metadata_filter(context_filter)
                if self.settings.vectorstore.database != "qdrant"
                else None
            ),
        )

    def close(self) -> None:
        if hasattr(self.vector_store.client, "close"):
            self.vector_store.client.close()
```

## File: `private_gpt/open_ai/__init__.py`
```python
"""OpenAI compatibility utilities."""
```

## File: `private_gpt/open_ai/openai_models.py`
```python
import time
import uuid
from collections.abc import Iterator
from typing import Literal

from llama_index.core.llms import ChatResponse, CompletionResponse
from pydantic import BaseModel, Field

from private_gpt.server.chunks.chunks_service import Chunk


class OpenAIDelta(BaseModel):
    """A piece of completion that needs to be concatenated to get the full message."""

    content: str | None


class OpenAIMessage(BaseModel):
    """Inference result, with the source of the message.

    Role could be the assistant or system
    (providing a default response, not AI generated).
    """

    role: Literal["assistant", "system", "user"] = Field(default="user")
    content: str | None


class OpenAIChoice(BaseModel):
    """Response from AI.

    Either the delta or the message will be present, but never both.
    Sources used will be returned in case context retrieval was enabled.
    """

    finish_reason: str | None = Field(examples=["stop"])
    delta: OpenAIDelta | None = None
    message: OpenAIMessage | None = None
    sources: list[Chunk] | None = None
    index: int = 0


class OpenAICompletion(BaseModel):
    """Clone of OpenAI Completion model.

    For more information see: https://platform.openai.com/docs/api-reference/chat/object
    """

    id: str
    object: Literal["completion", "completion.chunk"] = Field(default="completion")
    created: int = Field(..., examples=[1623340000])
    model: Literal["private-gpt"]
    choices: list[OpenAIChoice]

    @classmethod
    def from_text(
        cls,
        text: str | None,
        finish_reason: str | None = None,
        sources: list[Chunk] | None = None,
    ) -> "OpenAICompletion":
        return OpenAICompletion(
            id=str(uuid.uuid4()),
            object="completion",
            created=int(time.time()),
            model="private-gpt",
            choices=[
                OpenAIChoice(
                    message=OpenAIMessage(role="assistant", content=text),
                    finish_reason=finish_reason,
                    sources=sources,
                )
            ],
        )

    @classmethod
    def json_from_delta(
        cls,
        *,
        text: str | None,
        finish_reason: str | None = None,
        sources: list[Chunk] | None = None,
    ) -> str:
        chunk = OpenAICompletion(
            id=str(uuid.uuid4()),
            object="completion.chunk",
            created=int(time.time()),
            model="private-gpt",
            choices=[
                OpenAIChoice(
                    delta=OpenAIDelta(content=text),
                    finish_reason=finish_reason,
                    sources=sources,
                )
            ],
        )

        return chunk.model_dump_json()


def to_openai_response(
    response: str | ChatResponse, sources: list[Chunk] | None = None
) -> OpenAICompletion:
    if isinstance(response, ChatResponse):
        return OpenAICompletion.from_text(response.delta, finish_reason="stop")
    else:
        return OpenAICompletion.from_text(
            response, finish_reason="stop", sources=sources
        )


def to_openai_sse_stream(
    response_generator: Iterator[str | CompletionResponse | ChatResponse],
    sources: list[Chunk] | None = None,
) -> Iterator[str]:
    for response in response_generator:
        if isinstance(response, CompletionResponse | ChatResponse):
            yield f"data: {OpenAICompletion.json_from_delta(text=response.delta)}\n\n"
        else:
            yield f"data: {OpenAICompletion.json_from_delta(text=response, sources=sources)}\n\n"
    yield f"data: {OpenAICompletion.json_from_delta(text='', finish_reason='stop')}\n\n"
    yield "data: [DONE]\n\n"
```

## File: `private_gpt/open_ai/extensions/__init__.py`
```python
"""OpenAI API extensions."""
```

## File: `private_gpt/open_ai/extensions/context_filter.py`
```python
from pydantic import BaseModel, Field


class ContextFilter(BaseModel):
    docs_ids: list[str] | None = Field(
        examples=[["c202d5e6-7b69-4869-81cc-dd574ee8ee11"]]
    )
```

## File: `private_gpt/server/__init__.py`
```python
"""private-gpt server."""
```

## File: `private_gpt/server/chat/chat_router.py`
```python
from fastapi import APIRouter, Depends, Request
from llama_index.core.llms import ChatMessage, MessageRole
from pydantic import BaseModel
from starlette.responses import StreamingResponse

from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.open_ai.openai_models import (
    OpenAICompletion,
    OpenAIMessage,
    to_openai_response,
    to_openai_sse_stream,
)
from private_gpt.server.chat.chat_service import ChatService
from private_gpt.server.utils.auth import authenticated

chat_router = APIRouter(prefix="/v1", dependencies=[Depends(authenticated)])


class ChatBody(BaseModel):
    messages: list[OpenAIMessage]
    use_context: bool = False
    context_filter: ContextFilter | None = None
    include_sources: bool = True
    stream: bool = False

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are a rapper. Always answer with a rap.",
                        },
                        {
                            "role": "user",
                            "content": "How do you fry an egg?",
                        },
                    ],
                    "stream": False,
                    "use_context": True,
                    "include_sources": True,
                    "context_filter": {
                        "docs_ids": ["c202d5e6-7b69-4869-81cc-dd574ee8ee11"]
                    },
                }
            ]
        }
    }


@chat_router.post(
    "/chat/completions",
    response_model=None,
    responses={200: {"model": OpenAICompletion}},
    tags=["Contextual Completions"],
    openapi_extra={
        "x-fern-streaming": {
            "stream-condition": "stream",
            "response": {"$ref": "#/components/schemas/OpenAICompletion"},
            "response-stream": {"$ref": "#/components/schemas/OpenAICompletion"},
        }
    },
)
def chat_completion(
    request: Request, body: ChatBody
) -> OpenAICompletion | StreamingResponse:
    """Given a list of messages comprising a conversation, return a response.

    Optionally include an initial `role: system` message to influence the way
    the LLM answers.

    If `use_context` is set to `true`, the model will use context coming
    from the ingested documents to create the response. The documents being used can
    be filtered using the `context_filter` and passing the document IDs to be used.
    Ingested documents IDs can be found using `/ingest/list` endpoint. If you want
    all ingested documents to be used, remove `context_filter` altogether.

    When using `'include_sources': true`, the API will return the source Chunks used
    to create the response, which come from the context provided.

    When using `'stream': true`, the API will return data chunks following [OpenAI's
    streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
    ```
    {"id":"12345","object":"completion.chunk","created":1694268190,
    "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
    "finish_reason":null}]}
    ```
    """
    service = request.state.injector.get(ChatService)
    all_messages = [
        ChatMessage(content=m.content, role=MessageRole(m.role)) for m in body.messages
    ]
    if body.stream:
        completion_gen = service.stream_chat(
            messages=all_messages,
            use_context=body.use_context,
            context_filter=body.context_filter,
        )
        return StreamingResponse(
            to_openai_sse_stream(
                completion_gen.response,
                completion_gen.sources if body.include_sources else None,
            ),
            media_type="text/event-stream",
        )
    else:
        completion = service.chat(
            messages=all_messages,
            use_context=body.use_context,
            context_filter=body.context_filter,
        )
        return to_openai_response(
            completion.response, completion.sources if body.include_sources else None
        )
```

## File: `private_gpt/server/chat/chat_service.py`
```python
from dataclasses import dataclass
from typing import TYPE_CHECKING

from injector import inject, singleton
from llama_index.core.chat_engine import ContextChatEngine, SimpleChatEngine
from llama_index.core.chat_engine.types import (
    BaseChatEngine,
)
from llama_index.core.indices import VectorStoreIndex
from llama_index.core.indices.postprocessor import MetadataReplacementPostProcessor
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.postprocessor import (
    SentenceTransformerRerank,
    SimilarityPostprocessor,
)
from llama_index.core.storage import StorageContext
from llama_index.core.types import TokenGen
from pydantic import BaseModel

from private_gpt.components.embedding.embedding_component import EmbeddingComponent
from private_gpt.components.llm.llm_component import LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import (
    VectorStoreComponent,
)
from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.server.chunks.chunks_service import Chunk
from private_gpt.settings.settings import Settings

if TYPE_CHECKING:
    from llama_index.core.postprocessor.types import BaseNodePostprocessor


class Completion(BaseModel):
    response: str
    sources: list[Chunk] | None = None


class CompletionGen(BaseModel):
    response: TokenGen
    sources: list[Chunk] | None = None


@dataclass
class ChatEngineInput:
    system_message: ChatMessage | None = None
    last_message: ChatMessage | None = None
    chat_history: list[ChatMessage] | None = None

    @classmethod
    def from_messages(cls, messages: list[ChatMessage]) -> "ChatEngineInput":
        # Detect if there is a system message, extract the last message and chat history
        system_message = (
            messages[0]
            if len(messages) > 0 and messages[0].role == MessageRole.SYSTEM
            else None
        )
        last_message = (
            messages[-1]
            if len(messages) > 0 and messages[-1].role == MessageRole.USER
            else None
        )
        # Remove from messages list the system message and last message,
        # if they exist. The rest is the chat history.
        if system_message:
            messages.pop(0)
        if last_message:
            messages.pop(-1)
        chat_history = messages if len(messages) > 0 else None

        return cls(
            system_message=system_message,
            last_message=last_message,
            chat_history=chat_history,
        )


@singleton
class ChatService:
    settings: Settings

    @inject
    def __init__(
        self,
        settings: Settings,
        llm_component: LLMComponent,
        vector_store_component: VectorStoreComponent,
        embedding_component: EmbeddingComponent,
        node_store_component: NodeStoreComponent,
    ) -> None:
        self.settings = settings
        self.llm_component = llm_component
        self.embedding_component = embedding_component
        self.vector_store_component = vector_store_component
        self.storage_context = StorageContext.from_defaults(
            vector_store=vector_store_component.vector_store,
            docstore=node_store_component.doc_store,
            index_store=node_store_component.index_store,
        )
        self.index = VectorStoreIndex.from_vector_store(
            vector_store_component.vector_store,
            storage_context=self.storage_context,
            llm=llm_component.llm,
            embed_model=embedding_component.embedding_model,
            show_progress=True,
        )

    def _chat_engine(
        self,
        system_prompt: str | None = None,
        use_context: bool = False,
        context_filter: ContextFilter | None = None,
    ) -> BaseChatEngine:
        settings = self.settings
        if use_context:
            vector_index_retriever = self.vector_store_component.get_retriever(
                index=self.index,
                context_filter=context_filter,
                similarity_top_k=self.settings.rag.similarity_top_k,
            )
            node_postprocessors: list[BaseNodePostprocessor] = [
                MetadataReplacementPostProcessor(target_metadata_key="window"),
            ]
            if settings.rag.similarity_value:
                node_postprocessors.append(
                    SimilarityPostprocessor(
                        similarity_cutoff=settings.rag.similarity_value
                    )
                )

            if settings.rag.rerank.enabled:
                rerank_postprocessor = SentenceTransformerRerank(
                    model=settings.rag.rerank.model, top_n=settings.rag.rerank.top_n
                )
                node_postprocessors.append(rerank_postprocessor)

            return ContextChatEngine.from_defaults(
                system_prompt=system_prompt,
                retriever=vector_index_retriever,
                llm=self.llm_component.llm,  # Takes no effect at the moment
                node_postprocessors=node_postprocessors,
            )
        else:
            return SimpleChatEngine.from_defaults(
                system_prompt=system_prompt,
                llm=self.llm_component.llm,
            )

    def stream_chat(
        self,
        messages: list[ChatMessage],
        use_context: bool = False,
        context_filter: ContextFilter | None = None,
    ) -> CompletionGen:
        chat_engine_input = ChatEngineInput.from_messages(messages)
        last_message = (
            chat_engine_input.last_message.content
            if chat_engine_input.last_message
            else None
        )
        system_prompt = (
            chat_engine_input.system_message.content
            if chat_engine_input.system_message
            else None
        )
        chat_history = (
            chat_engine_input.chat_history if chat_engine_input.chat_history else None
        )

        chat_engine = self._chat_engine(
            system_prompt=system_prompt,
            use_context=use_context,
            context_filter=context_filter,
        )
        streaming_response = chat_engine.stream_chat(
            message=last_message if last_message is not None else "",
            chat_history=chat_history,
        )
        sources = [Chunk.from_node(node) for node in streaming_response.source_nodes]
        completion_gen = CompletionGen(
            response=streaming_response.response_gen, sources=sources
        )
        return completion_gen

    def chat(
        self,
        messages: list[ChatMessage],
        use_context: bool = False,
        context_filter: ContextFilter | None = None,
    ) -> Completion:
        chat_engine_input = ChatEngineInput.from_messages(messages)
        last_message = (
            chat_engine_input.last_message.content
            if chat_engine_input.last_message
            else None
        )
        system_prompt = (
            chat_engine_input.system_message.content
            if chat_engine_input.system_message
            else None
        )
        chat_history = (
            chat_engine_input.chat_history if chat_engine_input.chat_history else None
        )

        chat_engine = self._chat_engine(
            system_prompt=system_prompt,
            use_context=use_context,
            context_filter=context_filter,
        )
        wrapped_response = chat_engine.chat(
            message=last_message if last_message is not None else "",
            chat_history=chat_history,
        )
        sources = [Chunk.from_node(node) for node in wrapped_response.source_nodes]
        completion = Completion(response=wrapped_response.response, sources=sources)
        return completion
```

## File: `private_gpt/server/chunks/chunks_router.py`
```python
from typing import Literal

from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel, Field

from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.server.chunks.chunks_service import Chunk, ChunksService
from private_gpt.server.utils.auth import authenticated

chunks_router = APIRouter(prefix="/v1", dependencies=[Depends(authenticated)])


class ChunksBody(BaseModel):
    text: str = Field(examples=["Q3 2023 sales"])
    context_filter: ContextFilter | None = None
    limit: int = 10
    prev_next_chunks: int = Field(default=0, examples=[2])


class ChunksResponse(BaseModel):
    object: Literal["list"]
    model: Literal["private-gpt"]
    data: list[Chunk]


@chunks_router.post("/chunks", tags=["Context Chunks"])
def chunks_retrieval(request: Request, body: ChunksBody) -> ChunksResponse:
    """Given a `text`, returns the most relevant chunks from the ingested documents.

    The returned information can be used to generate prompts that can be
    passed to `/completions` or `/chat/completions` APIs. Note: it is usually a very
    fast API, because only the Embeddings model is involved, not the LLM. The
    returned information contains the relevant chunk `text` together with the source
    `document` it is coming from. It also contains a score that can be used to
    compare different results.

    The max number of chunks to be returned is set using the `limit` param.

    Previous and next chunks (pieces of text that appear right before or after in the
    document) can be fetched by using the `prev_next_chunks` field.

    The documents being used can be filtered using the `context_filter` and passing
    the document IDs to be used. Ingested documents IDs can be found using
    `/ingest/list` endpoint. If you want all ingested documents to be used,
    remove `context_filter` altogether.
    """
    service = request.state.injector.get(ChunksService)
    results = service.retrieve_relevant(
        body.text, body.context_filter, body.limit, body.prev_next_chunks
    )
    return ChunksResponse(
        object="list",
        model="private-gpt",
        data=results,
    )
```

## File: `private_gpt/server/chunks/chunks_service.py`
```python
from typing import TYPE_CHECKING, Literal

from injector import inject, singleton
from llama_index.core.indices import VectorStoreIndex
from llama_index.core.schema import NodeWithScore
from llama_index.core.storage import StorageContext
from pydantic import BaseModel, Field

from private_gpt.components.embedding.embedding_component import EmbeddingComponent
from private_gpt.components.llm.llm_component import LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import (
    VectorStoreComponent,
)
from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.server.ingest.model import IngestedDoc

if TYPE_CHECKING:
    from llama_index.core.schema import RelatedNodeInfo


class Chunk(BaseModel):
    object: Literal["context.chunk"]
    score: float = Field(examples=[0.023])
    document: IngestedDoc
    text: str = Field(examples=["Outbound sales increased 20%, driven by new leads."])
    previous_texts: list[str] | None = Field(
        default=None,
        examples=[["SALES REPORT 2023", "Inbound didn't show major changes."]],
    )
    next_texts: list[str] | None = Field(
        default=None,
        examples=[
            [
                "New leads came from Google Ads campaign.",
                "The campaign was run by the Marketing Department",
            ]
        ],
    )

    @classmethod
    def from_node(cls: type["Chunk"], node: NodeWithScore) -> "Chunk":
        doc_id = node.node.ref_doc_id if node.node.ref_doc_id is not None else "-"
        return cls(
            object="context.chunk",
            score=node.score or 0.0,
            document=IngestedDoc(
                object="ingest.document",
                doc_id=doc_id,
                doc_metadata=node.metadata,
            ),
            text=node.get_content(),
        )


@singleton
class ChunksService:
    @inject
    def __init__(
        self,
        llm_component: LLMComponent,
        vector_store_component: VectorStoreComponent,
        embedding_component: EmbeddingComponent,
        node_store_component: NodeStoreComponent,
    ) -> None:
        self.vector_store_component = vector_store_component
        self.llm_component = llm_component
        self.embedding_component = embedding_component
        self.storage_context = StorageContext.from_defaults(
            vector_store=vector_store_component.vector_store,
            docstore=node_store_component.doc_store,
            index_store=node_store_component.index_store,
        )

    def _get_sibling_nodes_text(
        self, node_with_score: NodeWithScore, related_number: int, forward: bool = True
    ) -> list[str]:
        explored_nodes_texts = []
        current_node = node_with_score.node
        for _ in range(related_number):
            explored_node_info: RelatedNodeInfo | None = (
                current_node.next_node if forward else current_node.prev_node
            )
            if explored_node_info is None:
                break

            explored_node = self.storage_context.docstore.get_node(
                explored_node_info.node_id
            )

            explored_nodes_texts.append(explored_node.get_content())
            current_node = explored_node

        return explored_nodes_texts

    def retrieve_relevant(
        self,
        text: str,
        context_filter: ContextFilter | None = None,
        limit: int = 10,
        prev_next_chunks: int = 0,
    ) -> list[Chunk]:
        index = VectorStoreIndex.from_vector_store(
            self.vector_store_component.vector_store,
            storage_context=self.storage_context,
            llm=self.llm_component.llm,
            embed_model=self.embedding_component.embedding_model,
            show_progress=True,
        )
        vector_index_retriever = self.vector_store_component.get_retriever(
            index=index, context_filter=context_filter, similarity_top_k=limit
        )
        nodes = vector_index_retriever.retrieve(text)
        nodes.sort(key=lambda n: n.score or 0.0, reverse=True)

        retrieved_nodes = []
        for node in nodes:
            chunk = Chunk.from_node(node)
            chunk.previous_texts = self._get_sibling_nodes_text(
                node, prev_next_chunks, False
            )
            chunk.next_texts = self._get_sibling_nodes_text(node, prev_next_chunks)
            retrieved_nodes.append(chunk)

        return retrieved_nodes
```

## File: `private_gpt/server/completions/__init__.py`
```python
"""Deprecated Openai compatibility endpoint."""
```

## File: `private_gpt/server/completions/completions_router.py`
```python
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from starlette.responses import StreamingResponse

from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.open_ai.openai_models import (
    OpenAICompletion,
    OpenAIMessage,
)
from private_gpt.server.chat.chat_router import ChatBody, chat_completion
from private_gpt.server.utils.auth import authenticated

completions_router = APIRouter(prefix="/v1", dependencies=[Depends(authenticated)])


class CompletionsBody(BaseModel):
    prompt: str
    system_prompt: str | None = None
    use_context: bool = False
    context_filter: ContextFilter | None = None
    include_sources: bool = True
    stream: bool = False

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "prompt": "How do you fry an egg?",
                    "system_prompt": "You are a rapper. Always answer with a rap.",
                    "stream": False,
                    "use_context": False,
                    "include_sources": False,
                }
            ]
        }
    }


@completions_router.post(
    "/completions",
    response_model=None,
    summary="Completion",
    responses={200: {"model": OpenAICompletion}},
    tags=["Contextual Completions"],
    openapi_extra={
        "x-fern-streaming": {
            "stream-condition": "stream",
            "response": {"$ref": "#/components/schemas/OpenAICompletion"},
            "response-stream": {"$ref": "#/components/schemas/OpenAICompletion"},
        }
    },
)
def prompt_completion(
    request: Request, body: CompletionsBody
) -> OpenAICompletion | StreamingResponse:
    """We recommend most users use our Chat completions API.

    Given a prompt, the model will return one predicted completion.

    Optionally include a `system_prompt` to influence the way the LLM answers.

    If `use_context`
    is set to `true`, the model will use context coming from the ingested documents
    to create the response. The documents being used can be filtered using the
    `context_filter` and passing the document IDs to be used. Ingested documents IDs
    can be found using `/ingest/list` endpoint. If you want all ingested documents to
    be used, remove `context_filter` altogether.

    When using `'include_sources': true`, the API will return the source Chunks used
    to create the response, which come from the context provided.

    When using `'stream': true`, the API will return data chunks following [OpenAI's
    streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
    ```
    {"id":"12345","object":"completion.chunk","created":1694268190,
    "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
    "finish_reason":null}]}
    ```
    """
    messages = [OpenAIMessage(content=body.prompt, role="user")]
    # If system prompt is passed, create a fake message with the system prompt.
    if body.system_prompt:
        messages.insert(0, OpenAIMessage(content=body.system_prompt, role="system"))

    chat_body = ChatBody(
        messages=messages,
        use_context=body.use_context,
        stream=body.stream,
        include_sources=body.include_sources,
        context_filter=body.context_filter,
    )
    return chat_completion(request, chat_body)
```

## File: `private_gpt/server/embeddings/embeddings_router.py`
```python
from typing import Literal

from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel

from private_gpt.server.embeddings.embeddings_service import (
    Embedding,
    EmbeddingsService,
)
from private_gpt.server.utils.auth import authenticated

embeddings_router = APIRouter(prefix="/v1", dependencies=[Depends(authenticated)])


class EmbeddingsBody(BaseModel):
    input: str | list[str]


class EmbeddingsResponse(BaseModel):
    object: Literal["list"]
    model: Literal["private-gpt"]
    data: list[Embedding]


@embeddings_router.post("/embeddings", tags=["Embeddings"])
def embeddings_generation(request: Request, body: EmbeddingsBody) -> EmbeddingsResponse:
    """Get a vector representation of a given input.

    That vector representation can be easily consumed
    by machine learning models and algorithms.
    """
    service = request.state.injector.get(EmbeddingsService)
    input_texts = body.input if isinstance(body.input, list) else [body.input]
    embeddings = service.texts_embeddings(input_texts)
    return EmbeddingsResponse(object="list", model="private-gpt", data=embeddings)
```

## File: `private_gpt/server/embeddings/embeddings_service.py`
```python
from typing import Literal

from injector import inject, singleton
from pydantic import BaseModel, Field

from private_gpt.components.embedding.embedding_component import EmbeddingComponent


class Embedding(BaseModel):
    index: int
    object: Literal["embedding"]
    embedding: list[float] = Field(examples=[[0.0023064255, -0.009327292]])


@singleton
class EmbeddingsService:
    @inject
    def __init__(self, embedding_component: EmbeddingComponent) -> None:
        self.embedding_model = embedding_component.embedding_model

    def texts_embeddings(self, texts: list[str]) -> list[Embedding]:
        texts_embeddings = self.embedding_model.get_text_embedding_batch(texts)
        return [
            Embedding(
                index=texts_embeddings.index(embedding),
                object="embedding",
                embedding=embedding,
            )
            for embedding in texts_embeddings
        ]
```

## File: `private_gpt/server/health/health_router.py`
```python
from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel, Field

# Not authentication or authorization required to get the health status.
health_router = APIRouter()


class HealthResponse(BaseModel):
    status: Literal["ok"] = Field(default="ok")


@health_router.get("/health", tags=["Health"])
def health() -> HealthResponse:
    """Return ok if the system is up."""
    return HealthResponse(status="ok")
```

## File: `private_gpt/server/ingest/ingest_router.py`
```python
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile
from pydantic import BaseModel, Field

from private_gpt.server.ingest.ingest_service import IngestService
from private_gpt.server.ingest.model import IngestedDoc
from private_gpt.server.utils.auth import authenticated

ingest_router = APIRouter(prefix="/v1", dependencies=[Depends(authenticated)])


class IngestTextBody(BaseModel):
    file_name: str = Field(examples=["Avatar: The Last Airbender"])
    text: str = Field(
        examples=[
            "Avatar is set in an Asian and Arctic-inspired world in which some "
            "people can telekinetically manipulate one of the four elements—water, "
            "earth, fire or air—through practices known as 'bending', inspired by "
            "Chinese martial arts."
        ]
    )


class IngestResponse(BaseModel):
    object: Literal["list"]
    model: Literal["private-gpt"]
    data: list[IngestedDoc]


@ingest_router.post("/ingest", tags=["Ingestion"], deprecated=True)
def ingest(request: Request, file: UploadFile) -> IngestResponse:
    """Ingests and processes a file.

    Deprecated. Use ingest/file instead.
    """
    return ingest_file(request, file)


@ingest_router.post("/ingest/file", tags=["Ingestion"])
def ingest_file(request: Request, file: UploadFile) -> IngestResponse:
    """Ingests and processes a file, storing its chunks to be used as context.

    The context obtained from files is later used in
    `/chat/completions`, `/completions`, and `/chunks` APIs.

    Most common document
    formats are supported, but you may be prompted to install an extra dependency to
    manage a specific file type.

    A file can generate different Documents (for example a PDF generates one Document
    per page). All Documents IDs are returned in the response, together with the
    extracted Metadata (which is later used to improve context retrieval). Those IDs
    can be used to filter the context used to create responses in
    `/chat/completions`, `/completions`, and `/chunks` APIs.
    """
    service = request.state.injector.get(IngestService)
    if file.filename is None:
        raise HTTPException(400, "No file name provided")
    ingested_documents = service.ingest_bin_data(file.filename, file.file)
    return IngestResponse(object="list", model="private-gpt", data=ingested_documents)


@ingest_router.post("/ingest/text", tags=["Ingestion"])
def ingest_text(request: Request, body: IngestTextBody) -> IngestResponse:
    """Ingests and processes a text, storing its chunks to be used as context.

    The context obtained from files is later used in
    `/chat/completions`, `/completions`, and `/chunks` APIs.

    A Document will be generated with the given text. The Document
    ID is returned in the response, together with the
    extracted Metadata (which is later used to improve context retrieval). That ID
    can be used to filter the context used to create responses in
    `/chat/completions`, `/completions`, and `/chunks` APIs.
    """
    service = request.state.injector.get(IngestService)
    if len(body.file_name) == 0:
        raise HTTPException(400, "No file name provided")
    ingested_documents = service.ingest_text(body.file_name, body.text)
    return IngestResponse(object="list", model="private-gpt", data=ingested_documents)


@ingest_router.get("/ingest/list", tags=["Ingestion"])
def list_ingested(request: Request) -> IngestResponse:
    """Lists already ingested Documents including their Document ID and metadata.

    Those IDs can be used to filter the context used to create responses
    in `/chat/completions`, `/completions`, and `/chunks` APIs.
    """
    service = request.state.injector.get(IngestService)
    ingested_documents = service.list_ingested()
    return IngestResponse(object="list", model="private-gpt", data=ingested_documents)


@ingest_router.delete("/ingest/{doc_id}", tags=["Ingestion"])
def delete_ingested(request: Request, doc_id: str) -> None:
    """Delete the specified ingested Document.

    The `doc_id` can be obtained from the `GET /ingest/list` endpoint.
    The document will be effectively deleted from your storage context.
    """
    service = request.state.injector.get(IngestService)
    service.delete(doc_id)
```

## File: `private_gpt/server/ingest/ingest_service.py`
```python
import logging
import tempfile
from pathlib import Path
from typing import TYPE_CHECKING, AnyStr, BinaryIO

from injector import inject, singleton
from llama_index.core.node_parser import SentenceWindowNodeParser
from llama_index.core.storage import StorageContext

from private_gpt.components.embedding.embedding_component import EmbeddingComponent
from private_gpt.components.ingest.ingest_component import get_ingestion_component
from private_gpt.components.llm.llm_component import LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import (
    VectorStoreComponent,
)
from private_gpt.server.ingest.model import IngestedDoc
from private_gpt.settings.settings import settings

if TYPE_CHECKING:
    from llama_index.core.storage.docstore.types import RefDocInfo

logger = logging.getLogger(__name__)


@singleton
class IngestService:
    @inject
    def __init__(
        self,
        llm_component: LLMComponent,
        vector_store_component: VectorStoreComponent,
        embedding_component: EmbeddingComponent,
        node_store_component: NodeStoreComponent,
    ) -> None:
        self.llm_service = llm_component
        self.storage_context = StorageContext.from_defaults(
            vector_store=vector_store_component.vector_store,
            docstore=node_store_component.doc_store,
            index_store=node_store_component.index_store,
        )
        node_parser = SentenceWindowNodeParser.from_defaults()

        self.ingest_component = get_ingestion_component(
            self.storage_context,
            embed_model=embedding_component.embedding_model,
            transformations=[node_parser, embedding_component.embedding_model],
            settings=settings(),
        )

    def _ingest_data(self, file_name: str, file_data: AnyStr) -> list[IngestedDoc]:
        logger.debug("Got file data of size=%s to ingest", len(file_data))
        # llama-index mainly supports reading from files, so
        # we have to create a tmp file to read for it to work
        # delete=False to avoid a Windows 11 permission error.
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            try:
                path_to_tmp = Path(tmp.name)
                if isinstance(file_data, bytes):
                    path_to_tmp.write_bytes(file_data)
                else:
                    path_to_tmp.write_text(str(file_data))
                return self.ingest_file(file_name, path_to_tmp)
            finally:
                tmp.close()
                path_to_tmp.unlink()

    def ingest_file(self, file_name: str, file_data: Path) -> list[IngestedDoc]:
        logger.info("Ingesting file_name=%s", file_name)
        documents = self.ingest_component.ingest(file_name, file_data)
        logger.info("Finished ingestion file_name=%s", file_name)
        return [IngestedDoc.from_document(document) for document in documents]

    def ingest_text(self, file_name: str, text: str) -> list[IngestedDoc]:
        logger.debug("Ingesting text data with file_name=%s", file_name)
        return self._ingest_data(file_name, text)

    def ingest_bin_data(
        self, file_name: str, raw_file_data: BinaryIO
    ) -> list[IngestedDoc]:
        logger.debug("Ingesting binary data with file_name=%s", file_name)
        file_data = raw_file_data.read()
        return self._ingest_data(file_name, file_data)

    def bulk_ingest(self, files: list[tuple[str, Path]]) -> list[IngestedDoc]:
        logger.info("Ingesting file_names=%s", [f[0] for f in files])
        documents = self.ingest_component.bulk_ingest(files)
        logger.info("Finished ingestion file_name=%s", [f[0] for f in files])
        return [IngestedDoc.from_document(document) for document in documents]

    def list_ingested(self) -> list[IngestedDoc]:
        ingested_docs: list[IngestedDoc] = []
        try:
            docstore = self.storage_context.docstore
            ref_docs: dict[str, RefDocInfo] | None = docstore.get_all_ref_doc_info()

            if not ref_docs:
                return ingested_docs

            for doc_id, ref_doc_info in ref_docs.items():
                doc_metadata = None
                if ref_doc_info is not None and ref_doc_info.metadata is not None:
                    doc_metadata = IngestedDoc.curate_metadata(ref_doc_info.metadata)
                ingested_docs.append(
                    IngestedDoc(
                        object="ingest.document",
                        doc_id=doc_id,
                        doc_metadata=doc_metadata,
                    )
                )
        except ValueError:
            logger.warning("Got an exception when getting list of docs", exc_info=True)
            pass
        logger.debug("Found count=%s ingested documents", len(ingested_docs))
        return ingested_docs

    def delete(self, doc_id: str) -> None:
        """Delete an ingested document.

        :raises ValueError: if the document does not exist
        """
        logger.info(
            "Deleting the ingested document=%s in the doc and index store", doc_id
        )
        self.ingest_component.delete(doc_id)
```

## File: `private_gpt/server/ingest/ingest_watcher.py`
```python
from collections.abc import Callable
from pathlib import Path
from typing import Any

from watchdog.events import (
    FileCreatedEvent,
    FileModifiedEvent,
    FileSystemEvent,
    FileSystemEventHandler,
)
from watchdog.observers import Observer


class IngestWatcher:
    def __init__(
        self, watch_path: Path, on_file_changed: Callable[[Path], None]
    ) -> None:
        self.watch_path = watch_path
        self.on_file_changed = on_file_changed

        class Handler(FileSystemEventHandler):
            def on_modified(self, event: FileSystemEvent) -> None:
                if isinstance(event, FileModifiedEvent):
                    on_file_changed(Path(event.src_path))

            def on_created(self, event: FileSystemEvent) -> None:
                if isinstance(event, FileCreatedEvent):
                    on_file_changed(Path(event.src_path))

        event_handler = Handler()
        observer: Any = Observer()
        self._observer = observer
        self._observer.schedule(event_handler, str(watch_path), recursive=True)

    def start(self) -> None:
        self._observer.start()
        while self._observer.is_alive():
            try:
                self._observer.join(1)
            except KeyboardInterrupt:
                break

    def stop(self) -> None:
        self._observer.stop()
        self._observer.join()
```

## File: `private_gpt/server/ingest/model.py`
```python
from typing import Any, Literal

from llama_index.core.schema import Document
from pydantic import BaseModel, Field


class IngestedDoc(BaseModel):
    object: Literal["ingest.document"]
    doc_id: str = Field(examples=["c202d5e6-7b69-4869-81cc-dd574ee8ee11"])
    doc_metadata: dict[str, Any] | None = Field(
        examples=[
            {
                "page_label": "2",
                "file_name": "Sales Report Q3 2023.pdf",
            }
        ]
    )

    @staticmethod
    def curate_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
        """Remove unwanted metadata keys."""
        for key in ["doc_id", "window", "original_text"]:
            metadata.pop(key, None)
        return metadata

    @staticmethod
    def from_document(document: Document) -> "IngestedDoc":
        return IngestedDoc(
            object="ingest.document",
            doc_id=document.doc_id,
            doc_metadata=IngestedDoc.curate_metadata(document.metadata),
        )
```

## File: `private_gpt/server/recipes/summarize/summarize_router.py`
```python
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from starlette.responses import StreamingResponse

from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.open_ai.openai_models import (
    to_openai_sse_stream,
)
from private_gpt.server.recipes.summarize.summarize_service import SummarizeService
from private_gpt.server.utils.auth import authenticated

summarize_router = APIRouter(prefix="/v1", dependencies=[Depends(authenticated)])


class SummarizeBody(BaseModel):
    text: str | None = None
    use_context: bool = False
    context_filter: ContextFilter | None = None
    prompt: str | None = None
    instructions: str | None = None
    stream: bool = False


class SummarizeResponse(BaseModel):
    summary: str


@summarize_router.post(
    "/summarize",
    response_model=None,
    summary="Summarize",
    responses={200: {"model": SummarizeResponse}},
    tags=["Recipes"],
)
def summarize(
    request: Request, body: SummarizeBody
) -> SummarizeResponse | StreamingResponse:
    """Given a text, the model will return a summary.

    Optionally include `instructions` to influence the way the summary is generated.

    If `use_context`
    is set to `true`, the model will also use the content coming from the ingested
    documents in the summary. The documents being used can
    be filtered by their metadata using the `context_filter`.
    Ingested documents metadata can be found using `/ingest/list` endpoint.
    If you want all ingested documents to be used, remove `context_filter` altogether.

    If `prompt` is set, it will be used as the prompt for the summarization,
    otherwise the default prompt will be used.

    When using `'stream': true`, the API will return data chunks following [OpenAI's
    streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
    ```
    {"id":"12345","object":"completion.chunk","created":1694268190,
    "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
    "finish_reason":null}]}
    ```
    """
    service: SummarizeService = request.state.injector.get(SummarizeService)

    if body.stream:
        completion_gen = service.stream_summarize(
            text=body.text,
            instructions=body.instructions,
            use_context=body.use_context,
            context_filter=body.context_filter,
            prompt=body.prompt,
        )
        return StreamingResponse(
            to_openai_sse_stream(
                response_generator=completion_gen,
            ),
            media_type="text/event-stream",
        )
    else:
        completion = service.summarize(
            text=body.text,
            instructions=body.instructions,
            use_context=body.use_context,
            context_filter=body.context_filter,
            prompt=body.prompt,
        )
        return SummarizeResponse(
            summary=completion,
        )
```

## File: `private_gpt/server/recipes/summarize/summarize_service.py`
```python
from itertools import chain

from injector import inject, singleton
from llama_index.core import (
    Document,
    StorageContext,
    SummaryIndex,
)
from llama_index.core.base.response.schema import Response, StreamingResponse
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.response_synthesizers import ResponseMode
from llama_index.core.storage.docstore.types import RefDocInfo
from llama_index.core.types import TokenGen

from private_gpt.components.embedding.embedding_component import EmbeddingComponent
from private_gpt.components.llm.llm_component import LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import (
    VectorStoreComponent,
)
from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.settings.settings import Settings

DEFAULT_SUMMARIZE_PROMPT = (
    "Provide a comprehensive summary of the provided context information. "
    "The summary should cover all the key points and main ideas presented in "
    "the original text, while also condensing the information into a concise "
    "and easy-to-understand format. Please ensure that the summary includes "
    "relevant details and examples that support the main ideas, while avoiding "
    "any unnecessary information or repetition."
)


@singleton
class SummarizeService:
    @inject
    def __init__(
        self,
        settings: Settings,
        llm_component: LLMComponent,
        node_store_component: NodeStoreComponent,
        vector_store_component: VectorStoreComponent,
        embedding_component: EmbeddingComponent,
    ) -> None:
        self.settings = settings
        self.llm_component = llm_component
        self.node_store_component = node_store_component
        self.vector_store_component = vector_store_component
        self.embedding_component = embedding_component
        self.storage_context = StorageContext.from_defaults(
            vector_store=vector_store_component.vector_store,
            docstore=node_store_component.doc_store,
            index_store=node_store_component.index_store,
        )

    @staticmethod
    def _filter_ref_docs(
        ref_docs: dict[str, RefDocInfo], context_filter: ContextFilter | None
    ) -> list[RefDocInfo]:
        if context_filter is None or not context_filter.docs_ids:
            return list(ref_docs.values())

        return [
            ref_doc
            for doc_id, ref_doc in ref_docs.items()
            if doc_id in context_filter.docs_ids
        ]

    def _summarize(
        self,
        use_context: bool = False,
        stream: bool = False,
        text: str | None = None,
        instructions: str | None = None,
        context_filter: ContextFilter | None = None,
        prompt: str | None = None,
    ) -> str | TokenGen:

        nodes_to_summarize = []

        # Add text to summarize
        if text:
            text_documents = [Document(text=text)]
            nodes_to_summarize += (
                SentenceSplitter.from_defaults().get_nodes_from_documents(
                    text_documents
                )
            )

        # Add context documents to summarize
        if use_context:
            # 1. Recover all ref docs
            ref_docs: dict[str, RefDocInfo] | None = (
                self.storage_context.docstore.get_all_ref_doc_info()
            )
            if ref_docs is None:
                raise ValueError("No documents have been ingested yet.")

            # 2. Filter documents based on context_filter (if provided)
            filtered_ref_docs = self._filter_ref_docs(ref_docs, context_filter)

            # 3. Get all nodes from the filtered documents
            filtered_node_ids = chain.from_iterable(
                [ref_doc.node_ids for ref_doc in filtered_ref_docs]
            )
            filtered_nodes = self.storage_context.docstore.get_nodes(
                node_ids=list(filtered_node_ids),
            )

            nodes_to_summarize += filtered_nodes

        # Create a SummaryIndex to summarize the nodes
        summary_index = SummaryIndex(
            nodes=nodes_to_summarize,
            storage_context=StorageContext.from_defaults(),  # In memory SummaryIndex
            show_progress=True,
        )

        # Make a tree summarization query
        # above the set of all candidate nodes
        query_engine = summary_index.as_query_engine(
            llm=self.llm_component.llm,
            response_mode=ResponseMode.TREE_SUMMARIZE,
            streaming=stream,
            use_async=self.settings.summarize.use_async,
        )

        prompt = prompt or DEFAULT_SUMMARIZE_PROMPT

        summarize_query = prompt + "\n" + (instructions or "")

        response = query_engine.query(summarize_query)
        if isinstance(response, Response):
            return response.response or ""
        elif isinstance(response, StreamingResponse):
            return response.response_gen
        else:
            raise TypeError(f"The result is not of a supported type: {type(response)}")

    def summarize(
        self,
        use_context: bool = False,
        text: str | None = None,
        instructions: str | None = None,
        context_filter: ContextFilter | None = None,
        prompt: str | None = None,
    ) -> str:
        return self._summarize(
            use_context=use_context,
            stream=False,
            text=text,
            instructions=instructions,
            context_filter=context_filter,
            prompt=prompt,
        )  # type: ignore

    def stream_summarize(
        self,
        use_context: bool = False,
        text: str | None = None,
        instructions: str | None = None,
        context_filter: ContextFilter | None = None,
        prompt: str | None = None,
    ) -> TokenGen:
        return self._summarize(
            use_context=use_context,
            stream=True,
            text=text,
            instructions=instructions,
            context_filter=context_filter,
            prompt=prompt,
        )  # type: ignore
```

## File: `private_gpt/server/utils/auth.py`
```python
"""Authentication mechanism for the API.

Define a simple mechanism to authenticate requests.
More complex authentication mechanisms can be defined here, and be placed in the
`authenticated` method (being a 'bean' injected in fastapi routers).

Authorization can also be made after the authentication, and depends on
the authentication. Authorization should not be implemented in this file.

Authorization can be done by following fastapi's guides:
* https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/
* https://fastapi.tiangolo.com/tutorial/security/
* https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/
"""

# mypy: ignore-errors
# Disabled mypy error: All conditional function variants must have identical signatures
# We are changing the implementation of the authenticated method, based on
# the config. If the auth is not enabled, we are not defining the complex method
# with its dependencies.
import logging
import secrets
from typing import Annotated

from fastapi import Depends, Header, HTTPException

from private_gpt.settings.settings import settings

# 401 signify that the request requires authentication.
# 403 signify that the authenticated user is not authorized to perform the operation.
NOT_AUTHENTICATED = HTTPException(
    status_code=401,
    detail="Not authenticated",
    headers={"WWW-Authenticate": 'Basic realm="All the API", charset="UTF-8"'},
)

logger = logging.getLogger(__name__)


def _simple_authentication(authorization: Annotated[str, Header()] = "") -> bool:
    """Check if the request is authenticated."""
    if not secrets.compare_digest(authorization, settings().server.auth.secret):
        # If the "Authorization" header is not the expected one, raise an exception.
        raise NOT_AUTHENTICATED
    return True


if not settings().server.auth.enabled:
    logger.debug(
        "Defining a dummy authentication mechanism for fastapi, always authenticating requests"
    )

    # Define a dummy authentication method that always returns True.
    def authenticated() -> bool:
        """Check if the request is authenticated."""
        return True

else:
    logger.info("Defining the given authentication mechanism for the API")

    # Method to be used as a dependency to check if the request is authenticated.
    def authenticated(
        _simple_authentication: Annotated[bool, Depends(_simple_authentication)]
    ) -> bool:
        """Check if the request is authenticated."""
        assert settings().server.auth.enabled
        if not _simple_authentication:
            raise NOT_AUTHENTICATED
        return True
```

## File: `private_gpt/settings/__init__.py`
```python
"""Settings."""
```

## File: `private_gpt/settings/settings.py`
```python
from typing import Any, Literal

from pydantic import BaseModel, Field

from private_gpt.settings.settings_loader import load_active_settings


class CorsSettings(BaseModel):
    """CORS configuration.

    For more details on the CORS configuration, see:
    # * https://fastapi.tiangolo.com/tutorial/cors/
    # * https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
    """

    enabled: bool = Field(
        description="Flag indicating if CORS headers are set or not."
        "If set to True, the CORS headers will be set to allow all origins, methods and headers.",
        default=False,
    )
    allow_credentials: bool = Field(
        description="Indicate that cookies should be supported for cross-origin requests",
        default=False,
    )
    allow_origins: list[str] = Field(
        description="A list of origins that should be permitted to make cross-origin requests.",
        default=[],
    )
    allow_origin_regex: list[str] = Field(
        description="A regex string to match against origins that should be permitted to make cross-origin requests.",
        default=None,
    )
    allow_methods: list[str] = Field(
        description="A list of HTTP methods that should be allowed for cross-origin requests.",
        default=[
            "GET",
        ],
    )
    allow_headers: list[str] = Field(
        description="A list of HTTP request headers that should be supported for cross-origin requests.",
        default=[],
    )


class AuthSettings(BaseModel):
    """Authentication configuration.

    The implementation of the authentication strategy must
    """

    enabled: bool = Field(
        description="Flag indicating if authentication is enabled or not.",
        default=False,
    )
    secret: str = Field(
        description="The secret to be used for authentication. "
        "It can be any non-blank string. For HTTP basic authentication, "
        "this value should be the whole 'Authorization' header that is expected"
    )


class IngestionSettings(BaseModel):
    """Ingestion configuration.

    This configuration is used to control the ingestion of data into the system
    using non-server methods. This is useful for local development and testing;
    or to ingest in bulk from a folder.

    Please note that this configuration is not secure and should be used in
    a controlled environment only (setting right permissions, etc.).
    """

    enabled: bool = Field(
        description="Flag indicating if local ingestion is enabled or not.",
        default=False,
    )
    allow_ingest_from: list[str] = Field(
        description="A list of folders that should be permitted to make ingest requests.",
        default=[],
    )


class ServerSettings(BaseModel):
    env_name: str = Field(
        description="Name of the environment (prod, staging, local...)"
    )
    port: int = Field(description="Port of PrivateGPT FastAPI server, defaults to 8001")
    cors: CorsSettings = Field(
        description="CORS configuration", default=CorsSettings(enabled=False)
    )
    auth: AuthSettings = Field(
        description="Authentication configuration",
        default_factory=lambda: AuthSettings(enabled=False, secret="secret-key"),
    )


class DataSettings(BaseModel):
    local_ingestion: IngestionSettings = Field(
        description="Ingestion configuration",
        default_factory=lambda: IngestionSettings(allow_ingest_from=["*"]),
    )
    local_data_folder: str = Field(
        description="Path to local storage."
        "It will be treated as an absolute path if it starts with /"
    )


class LLMSettings(BaseModel):
    mode: Literal[
        "llamacpp",
        "openai",
        "openailike",
        "azopenai",
        "sagemaker",
        "mock",
        "ollama",
        "gemini",
    ]
    max_new_tokens: int = Field(
        256,
        description="The maximum number of token that the LLM is authorized to generate in one completion.",
    )
    context_window: int = Field(
        3900,
        description="The maximum number of context tokens for the model.",
    )
    tokenizer: str = Field(
        None,
        description="The model id of a predefined tokenizer hosted inside a model repo on "
        "huggingface.co. Valid model ids can be located at the root-level, like "
        "`bert-base-uncased`, or namespaced under a user or organization name, "
        "like `HuggingFaceH4/zephyr-7b-beta`. If not set, will load a tokenizer matching "
        "gpt-3.5-turbo LLM.",
    )
    temperature: float = Field(
        0.1,
        description="The temperature of the model. Increasing the temperature will make the model answer more creatively. A value of 0.1 would be more factual.",
    )
    prompt_style: Literal["default", "llama2", "llama3", "tag", "mistral", "chatml"] = (
        Field(
            "llama2",
            description=(
                "The prompt style to use for the chat engine. "
                "If `default` - use the default prompt style from the llama_index. It should look like `role: message`.\n"
                "If `llama2` - use the llama2 prompt style from the llama_index. Based on `<s>`, `[INST]` and `<<SYS>>`.\n"
                "If `llama3` - use the llama3 prompt style from the llama_index."
                "If `tag` - use the `tag` prompt style. It should look like `<|role|>: message`. \n"
                "If `mistral` - use the `mistral prompt style. It shoudl look like <s>[INST] {System Prompt} [/INST]</s>[INST] { UserInstructions } [/INST]"
                "`llama2` is the historic behaviour. `default` might work better with your custom models."
            ),
        )
    )


class VectorstoreSettings(BaseModel):
    database: Literal["chroma", "qdrant", "postgres", "clickhouse", "milvus"]


class NodeStoreSettings(BaseModel):
    database: Literal["simple", "postgres"]


class LlamaCPPSettings(BaseModel):
    llm_hf_repo_id: str
    llm_hf_model_file: str
    tfs_z: float = Field(
        1.0,
        description="Tail free sampling is used to reduce the impact of less probable tokens from the output. A higher value (e.g., 2.0) will reduce the impact more, while a value of 1.0 disables this setting.",
    )
    top_k: int = Field(
        40,
        description="Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative. (Default: 40)",
    )
    top_p: float = Field(
        0.9,
        description="Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text. (Default: 0.9)",
    )
    repeat_penalty: float = Field(
        1.1,
        description="Sets how strongly to penalize repetitions. A higher value (e.g., 1.5) will penalize repetitions more strongly, while a lower value (e.g., 0.9) will be more lenient. (Default: 1.1)",
    )


class HuggingFaceSettings(BaseModel):
    embedding_hf_model_name: str = Field(
        description="Name of the HuggingFace model to use for embeddings"
    )
    access_token: str = Field(
        None,
        description="Huggingface access token, required to download some models",
    )
    trust_remote_code: bool = Field(
        False,
        description="If set to True, the code from the remote model will be trusted and executed.",
    )


class EmbeddingSettings(BaseModel):
    mode: Literal[
        "huggingface",
        "openai",
        "azopenai",
        "sagemaker",
        "ollama",
        "mock",
        "gemini",
        "mistralai",
    ]
    ingest_mode: Literal["simple", "batch", "parallel", "pipeline"] = Field(
        "simple",
        description=(
            "The ingest mode to use for the embedding engine:\n"
            "If `simple` - ingest files sequentially and one by one. It is the historic behaviour.\n"
            "If `batch` - if multiple files, parse all the files in parallel, "
            "and send them in batch to the embedding model.\n"
            "In `pipeline` - The Embedding engine is kept as busy as possible\n"
            "If `parallel` - parse the files in parallel using multiple cores, and embedd them in parallel.\n"
            "`parallel` is the fastest mode for local setup, as it parallelize IO RW in the index.\n"
            "For modes that leverage parallelization, you can specify the number of "
            "workers to use with `count_workers`.\n"
        ),
    )
    count_workers: int = Field(
        2,
        description=(
            "The number of workers to use for file ingestion.\n"
            "In `batch` mode, this is the number of workers used to parse the files.\n"
            "In `parallel` mode, this is the number of workers used to parse the files and embed them.\n"
            "In `pipeline` mode, this is the number of workers that can perform embeddings.\n"
            "This is only used if `ingest_mode` is not `simple`.\n"
            "Do not go too high with this number, as it might cause memory issues. (especially in `parallel` mode)\n"
            "Do not set it higher than your number of threads of your CPU."
        ),
    )
    embed_dim: int = Field(
        384,
        description="The dimension of the embeddings stored in the Postgres database",
    )


class SagemakerSettings(BaseModel):
    llm_endpoint_name: str
    embedding_endpoint_name: str


class OpenAISettings(BaseModel):
    api_base: str = Field(
        None,
        description="Base URL of OpenAI API. Example: 'https://api.openai.com/v1'.",
    )
    api_key: str
    model: str = Field(
        "gpt-3.5-turbo",
        description="OpenAI Model to use. Example: 'gpt-4'.",
    )
    request_timeout: float = Field(
        120.0,
        description="Time elapsed until openailike server times out the request. Default is 120s. Format is float. ",
    )
    embedding_api_base: str = Field(
        None,
        description="Base URL of OpenAI API. Example: 'https://api.openai.com/v1'.",
    )
    embedding_api_key: str
    embedding_model: str = Field(
        "text-embedding-ada-002",
        description="OpenAI embedding Model to use. Example: 'text-embedding-3-large'.",
    )


class GeminiSettings(BaseModel):
    api_key: str
    model: str = Field(
        "models/gemini-pro",
        description="Google Model to use. Example: 'models/gemini-pro'.",
    )
    embedding_model: str = Field(
        "models/embedding-001",
        description="Google Embedding Model to use. Example: 'models/embedding-001'.",
    )


class OllamaSettings(BaseModel):
    api_base: str = Field(
        "http://localhost:11434",
        description="Base URL of Ollama API. Example: 'https://localhost:11434'.",
    )
    embedding_api_base: str = Field(
        "http://localhost:11434",
        description="Base URL of Ollama embedding API. Example: 'https://localhost:11434'.",
    )
    llm_model: str = Field(
        None,
        description="Model to use. Example: 'llama2-uncensored'.",
    )
    embedding_model: str = Field(
        None,
        description="Model to use. Example: 'nomic-embed-text'.",
    )
    keep_alive: str = Field(
        "5m",
        description="Time the model will stay loaded in memory after a request. examples: 5m, 5h, '-1' ",
    )
    tfs_z: float = Field(
        1.0,
        description="Tail free sampling is used to reduce the impact of less probable tokens from the output. A higher value (e.g., 2.0) will reduce the impact more, while a value of 1.0 disables this setting.",
    )
    num_predict: int = Field(
        None,
        description="Maximum number of tokens to predict when generating text. (Default: 128, -1 = infinite generation, -2 = fill context)",
    )
    top_k: int = Field(
        40,
        description="Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative. (Default: 40)",
    )
    top_p: float = Field(
        0.9,
        description="Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text. (Default: 0.9)",
    )
    repeat_last_n: int = Field(
        64,
        description="Sets how far back for the model to look back to prevent repetition. (Default: 64, 0 = disabled, -1 = num_ctx)",
    )
    repeat_penalty: float = Field(
        1.1,
        description="Sets how strongly to penalize repetitions. A higher value (e.g., 1.5) will penalize repetitions more strongly, while a lower value (e.g., 0.9) will be more lenient. (Default: 1.1)",
    )
    request_timeout: float = Field(
        120.0,
        description="Time elapsed until ollama times out the request. Default is 120s. Format is float. ",
    )
    autopull_models: bool = Field(
        False,
        description="If set to True, the Ollama will automatically pull the models from the API base.",
    )


class AzureOpenAISettings(BaseModel):
    api_key: str
    azure_endpoint: str
    api_version: str = Field(
        "2023_05_15",
        description="The API version to use for this operation. This follows the YYYY-MM-DD format.",
    )
    embedding_deployment_name: str
    embedding_model: str = Field(
        "text-embedding-ada-002",
        description="OpenAI Model to use. Example: 'text-embedding-ada-002'.",
    )
    llm_deployment_name: str
    llm_model: str = Field(
        "gpt-35-turbo",
        description="OpenAI Model to use. Example: 'gpt-4'.",
    )


class UISettings(BaseModel):
    enabled: bool
    path: str
    default_mode: Literal["RAG", "Search", "Basic", "Summarize"] = Field(
        "RAG",
        description="The default mode.",
    )
    default_chat_system_prompt: str = Field(
        None,
        description="The default system prompt to use for the chat mode.",
    )
    default_query_system_prompt: str = Field(
        None, description="The default system prompt to use for the query mode."
    )
    default_summarization_system_prompt: str = Field(
        None,
        description="The default system prompt to use for the summarization mode.",
    )
    delete_file_button_enabled: bool = Field(
        True, description="If the button to delete a file is enabled or not."
    )
    delete_all_files_button_enabled: bool = Field(
        False, description="If the button to delete all files is enabled or not."
    )


class RerankSettings(BaseModel):
    enabled: bool = Field(
        False,
        description="This value controls whether a reranker should be included in the RAG pipeline.",
    )
    model: str = Field(
        "cross-encoder/ms-marco-MiniLM-L-2-v2",
        description="Rerank model to use. Limited to SentenceTransformer cross-encoder models.",
    )
    top_n: int = Field(
        2,
        description="This value controls the number of documents returned by the RAG pipeline.",
    )


class RagSettings(BaseModel):
    similarity_top_k: int = Field(
        2,
        description="This value controls the number of documents returned by the RAG pipeline or considered for reranking if enabled.",
    )
    similarity_value: float = Field(
        None,
        description="If set, any documents retrieved from the RAG must meet a certain match score. Acceptable values are between 0 and 1.",
    )
    rerank: RerankSettings


class SummarizeSettings(BaseModel):
    use_async: bool = Field(
        True,
        description="If set to True, the summarization will be done asynchronously.",
    )


class ClickHouseSettings(BaseModel):
    host: str = Field(
        "localhost",
        description="The server hosting the ClickHouse database",
    )
    port: int = Field(
        8443,
        description="The port on which the ClickHouse database is accessible",
    )
    username: str = Field(
        "default",
        description="The username to use to connect to the ClickHouse database",
    )
    password: str = Field(
        "",
        description="The password to use to connect to the ClickHouse database",
    )
    database: str = Field(
        "__default__",
        description="The default database to use for connections",
    )
    secure: bool | str = Field(
        False,
        description="Use https/TLS for secure connection to the server",
    )
    interface: str | None = Field(
        None,
        description="Must be either 'http' or 'https'. Determines the protocol to use for the connection",
    )
    settings: dict[str, Any] | None = Field(
        None,
        description="Specific ClickHouse server settings to be used with the session",
    )
    connect_timeout: int | None = Field(
        None,
        description="Timeout in seconds for establishing a connection",
    )
    send_receive_timeout: int | None = Field(
        None,
        description="Read timeout in seconds for http connection",
    )
    verify: bool | None = Field(
        None,
        description="Verify the server certificate in secure/https mode",
    )
    ca_cert: str | None = Field(
        None,
        description="Path to Certificate Authority root certificate (.pem format)",
    )
    client_cert: str | None = Field(
        None,
        description="Path to TLS Client certificate (.pem format)",
    )
    client_cert_key: str | None = Field(
        None,
        description="Path to the private key for the TLS Client certificate",
    )
    http_proxy: str | None = Field(
        None,
        description="HTTP proxy address",
    )
    https_proxy: str | None = Field(
        None,
        description="HTTPS proxy address",
    )
    server_host_name: str | None = Field(
        None,
        description="Server host name to be checked against the TLS certificate",
    )


class PostgresSettings(BaseModel):
    host: str = Field(
        "localhost",
        description="The server hosting the Postgres database",
    )
    port: int = Field(
        5432,
        description="The port on which the Postgres database is accessible",
    )
    user: str = Field(
        "postgres",
        description="The user to use to connect to the Postgres database",
    )
    password: str = Field(
        "postgres",
        description="The password to use to connect to the Postgres database",
    )
    database: str = Field(
        "postgres",
        description="The database to use to connect to the Postgres database",
    )
    schema_name: str = Field(
        "public",
        description="The name of the schema in the Postgres database to use",
    )


class QdrantSettings(BaseModel):
    location: str | None = Field(
        None,
        description=(
            "If `:memory:` - use in-memory Qdrant instance.\n"
            "If `str` - use it as a `url` parameter.\n"
        ),
    )
    url: str | None = Field(
        None,
        description=(
            "Either host or str of 'Optional[scheme], host, Optional[port], Optional[prefix]'."
        ),
    )
    port: int | None = Field(6333, description="Port of the REST API interface.")
    grpc_port: int | None = Field(6334, description="Port of the gRPC interface.")
    prefer_grpc: bool | None = Field(
        False,
        description="If `true` - use gRPC interface whenever possible in custom methods.",
    )
    https: bool | None = Field(
        None,
        description="If `true` - use HTTPS(SSL) protocol.",
    )
    api_key: str | None = Field(
        None,
        description="API key for authentication in Qdrant Cloud.",
    )
    prefix: str | None = Field(
        None,
        description=(
            "Prefix to add to the REST URL path."
            "Example: `service/v1` will result in "
            "'http://localhost:6333/service/v1/{qdrant-endpoint}' for REST API."
        ),
    )
    timeout: float | None = Field(
        None,
        description="Timeout for REST and gRPC API requests.",
    )
    host: str | None = Field(
        None,
        description="Host name of Qdrant service. If url and host are None, set to 'localhost'.",
    )
    path: str | None = Field(None, description="Persistence path for QdrantLocal.")
    force_disable_check_same_thread: bool | None = Field(
        True,
        description=(
            "For QdrantLocal, force disable check_same_thread. Default: `True`"
            "Only use this if you can guarantee that you can resolve the thread safety outside QdrantClient."
        ),
    )


class MilvusSettings(BaseModel):
    uri: str = Field(
        "local_data/private_gpt/milvus/milvus_local.db",
        description="The URI of the Milvus instance. For example: 'local_data/private_gpt/milvus/milvus_local.db' for Milvus Lite.",
    )
    token: str = Field(
        "",
        description=(
            "A valid access token to access the specified Milvus instance. "
            "This can be used as a recommended alternative to setting user and password separately. "
        ),
    )
    collection_name: str = Field(
        "make_this_parameterizable_per_api_call",
        description="The name of the collection in Milvus. Default is 'make_this_parameterizable_per_api_call'.",
    )
    overwrite: bool = Field(
        True, description="Overwrite the previous collection schema if it exists."
    )


class Settings(BaseModel):
    server: ServerSettings
    data: DataSettings
    ui: UISettings
    llm: LLMSettings
    embedding: EmbeddingSettings
    llamacpp: LlamaCPPSettings
    huggingface: HuggingFaceSettings
    sagemaker: SagemakerSettings
    openai: OpenAISettings
    gemini: GeminiSettings
    ollama: OllamaSettings
    azopenai: AzureOpenAISettings
    vectorstore: VectorstoreSettings
    nodestore: NodeStoreSettings
    rag: RagSettings
    summarize: SummarizeSettings
    qdrant: QdrantSettings | None = None
    postgres: PostgresSettings | None = None
    clickhouse: ClickHouseSettings | None = None
    milvus: MilvusSettings | None = None


"""
This is visible just for DI or testing purposes.

Use dependency injection or `settings()` method instead.
"""
unsafe_settings = load_active_settings()

"""
This is visible just for DI or testing purposes.

Use dependency injection or `settings()` method instead.
"""
unsafe_typed_settings = Settings(**unsafe_settings)


def settings() -> Settings:
    """Get the current loaded settings from the DI container.

    This method exists to keep compatibility with the existing code,
    that require global access to the settings.

    For regular components use dependency injection instead.
    """
    from private_gpt.di import global_injector

    return global_injector.get(Settings)
```

## File: `private_gpt/settings/settings_loader.py`
```python
import functools
import logging
import os
import sys
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from pydantic.v1.utils import deep_update, unique_list

from private_gpt.constants import PROJECT_ROOT_PATH
from private_gpt.settings.yaml import load_yaml_with_envvars

logger = logging.getLogger(__name__)

_settings_folder = os.environ.get("PGPT_SETTINGS_FOLDER", PROJECT_ROOT_PATH)

# if running in unittest, use the test profile
_test_profile = ["test"] if "tests.fixtures" in sys.modules else []

active_profiles: list[str] = unique_list(
    ["default"]
    + [
        item.strip()
        for item in os.environ.get("PGPT_PROFILES", "").split(",")
        if item.strip()
    ]
    + _test_profile
)


def merge_settings(settings: Iterable[dict[str, Any]]) -> dict[str, Any]:
    return functools.reduce(deep_update, settings, {})


def load_settings_from_profile(profile: str) -> dict[str, Any]:
    if profile == "default":
        profile_file_name = "settings.yaml"
    else:
        profile_file_name = f"settings-{profile}.yaml"

    path = Path(_settings_folder) / profile_file_name
    with Path(path).open("r") as f:
        config = load_yaml_with_envvars(f)
    if not isinstance(config, dict):
        raise TypeError(f"Config file has no top-level mapping: {path}")
    return config


def load_active_settings() -> dict[str, Any]:
    """Load active profiles and merge them."""
    logger.info("Starting application with profiles=%s", active_profiles)
    loaded_profiles = [
        load_settings_from_profile(profile) for profile in active_profiles
    ]
    merged: dict[str, Any] = merge_settings(loaded_profiles)
    return merged
```

## File: `private_gpt/settings/yaml.py`
```python
import os
import re
import typing
from typing import Any, TextIO

from yaml import SafeLoader

_env_replace_matcher = re.compile(r"\$\{(\w|_)+:?.*}")


@typing.no_type_check  # pyaml does not have good hints, everything is Any
def load_yaml_with_envvars(
    stream: TextIO, environ: dict[str, Any] = os.environ
) -> dict[str, Any]:
    """Load yaml file with environment variable expansion.

    The pattern ${VAR} or ${VAR:default} will be replaced with
    the value of the environment variable.
    """
    loader = SafeLoader(stream)

    def load_env_var(_, node) -> str:
        """Extract the matched value, expand env variable, and replace the match."""
        value = str(node.value).removeprefix("${").removesuffix("}")
        split = value.split(":", 1)
        env_var = split[0]
        value = environ.get(env_var)
        default = None if len(split) == 1 else split[1]
        if value is None and default is None:
            raise ValueError(
                f"Environment variable {env_var} is not set and not default was provided"
            )
        return value or default

    loader.add_implicit_resolver("env_var_replacer", _env_replace_matcher, None)
    loader.add_constructor("env_var_replacer", load_env_var)

    try:
        return loader.get_single_data()
    finally:
        loader.dispose()
```

## File: `private_gpt/ui/__init__.py`
```python
"""Gradio based UI."""
```

## File: `private_gpt/ui/images.py`
```python
logo_svg = "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODYxIiBoZWlnaHQ9Ijk4IiB2aWV3Qm94PSIwIDAgODYxIDk4IiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8cGF0aCBkPSJNNDguMTM0NSAwLjE1NzkxMUMzNi44Mjk5IDEuMDM2NTQgMjYuMTIwNSA1LjU1MzI4IDE3LjYyNTYgMTMuMDI1QzkuMTMwNDYgMjAuNDk2NyAzLjMxMTcgMzAuNTE2OSAxLjA0OTUyIDQxLjU3MDVDLTEuMjEyNzMgNTIuNjIzOCAwLjIwNDQxOSA2NC4xMDk0IDUuMDg2MiA3NC4yOTA1QzkuOTY4NjggODQuNDcxNiAxOC4wNTAzIDkyLjc5NDMgMjguMTA5OCA5OEwzMy43MDI2IDgyLjU5MDdMMzUuNDU0MiA3Ny43NjU2QzI5LjgzODcgNzQuMTY5MiAyNS41NDQ0IDY4Ljg2MDcgMjMuMjE0IDYyLjYzNDRDMjAuODgyMiA1Ni40MDg2IDIwLjYzOSA0OS41OTkxIDIyLjUyMDQgNDMuMjI0M0MyNC40MDI5IDM2Ljg0OTUgMjguMzA5NiAzMS4yNTI1IDMzLjY1NjEgMjcuMjcwNkMzOS4wMDIgMjMuMjg4MyA0NS41MDAzIDIxLjEzNSA1Mi4xNzg5IDIxLjEzM0M1OC44NTczIDIxLjEzMDMgNjUuMzU3MSAyMy4yNzgzIDcwLjcwNjUgMjcuMjU1OEM3Ni4wNTU0IDMxLjIzNCA3OS45NjY0IDM2LjgyNzcgODEuODU0MyA0My4yMDA2QzgzLjc0MjkgNDkuNTczNiA4My41MDYyIDU2LjM4MzYgODEuMTgwMSA2Mi42MTE3Qzc4Ljg1NDUgNjguODM5NiA3NC41NjUgNzQuMTUxNCA2OC45NTI5IDc3Ljc1MjhMNzAuNzA3NCA4Mi41OTA3TDc2LjMwMDIgOTcuOTk3MUM4Ni45Nzg4IDkyLjQ3MDUgOTUuNDA4OCA4My40NDE5IDEwMC4xNjMgNzIuNDQwNEMxMDQuOTE3IDYxLjQzOTQgMTA1LjcwNCA0OS4xNDE3IDEwMi4zODkgMzcuNjNDOTkuMDc0NiAyNi4xMTc5IDkxLjg2MjcgMTYuMDk5MyA4MS45NzQzIDkuMjcwNzlDNzIuMDg2MSAyLjQ0MTkxIDYwLjEyOTEgLTAuNzc3MDg2IDQ4LjEyODYgMC4xNTg5MzRMNDguMTM0NSAwLjE1NzkxMVoiIGZpbGw9IiMxRjFGMjkiLz4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzVfMTkpIj4KPHBhdGggZD0iTTIyMC43NzIgMTIuNzUyNEgyNTIuNjM5QzI2Ny4yNjMgMTIuNzUyNCAyNzcuNzM5IDIxLjk2NzUgMjc3LjczOSAzNS40MDUyQzI3Ny43MzkgNDYuNzg3IDI2OS44ODEgNTUuMzUwOCAyNTguMzE0IDU3LjQxMDdMMjc4LjgzIDg1LjM3OTRIMjYxLjM3TDI0Mi4wNTQgNTcuOTUzM0gyMzUuNTA2Vjg1LjM3OTRIMjIwLjc3NEwyMjAuNzcyIDEyLjc1MjRaTTIzNS41MDQgMjYuMzAyOFY0NC40MDdIMjUyLjYzMkMyNTguOTYyIDQ0LjQwNyAyNjIuOTk5IDQwLjgyOTggMjYyLjk5OSAzNS40MTAyQzI2Mi45OTkgMjkuODgwOSAyNTguOTYyIDI2LjMwMjggMjUyLjYzMiAyNi4zMDI4SDIzNS41MDRaIiBmaWxsPSIjMUYxRjI5Ii8+CjxwYXRoIGQ9Ik0yOTUuMTc2IDg1LjM4NDRWMTIuNzUyNEgzMDkuOTA5Vjg1LjM4NDRIMjk1LjE3NloiIGZpbGw9IiMxRjFGMjkiLz4KPHBhdGggZD0iTTM2My43OTUgNjUuNzYzTDM4NS42MiAxMi43NTI0SDQwMS40NDRMMzcxLjIxNSA4NS4zODQ0SDM1Ni40ODNMMzI2LjI1NCAxMi43NTI0SDM0Mi4wNzhMMzYzLjc5NSA2NS43NjNaIiBmaWxsPSIjMUYxRjI5Ii8+CjxwYXRoIGQ9Ik00NDguMzI3IDcyLjA1MDRINDE1LjY5OEw0MTAuMjQxIDg1LjM4NDRIMzk0LjQxOEw0MjQuNjQ3IDEyLjc1MjRINDM5LjM3OUw0NjkuNjA4IDg1LjM4NDRINDUzLjc4M0w0NDguMzI3IDcyLjA1MDRaTTQ0Mi43NjEgNTguNUw0MzIuMDY2IDMyLjM3NDhMNDIxLjI2MiA1OC41SDQ0Mi43NjFaIiBmaWxsPSIjMUYxRjI5Ii8+CjxwYXRoIGQ9Ik00NjUuMjIxIDEyLjc1MjRINTMwLjU5MlYyNi4zMDI4SDUwNS4yNzVWODUuMzg0NEg0OTAuNTM5VjI2LjMwMjhINDY1LjIyMVYxMi43NTI0WiIgZmlsbD0iIzFGMUYyOSIvPgo8cGF0aCBkPSJNNTk1LjE5MyAxMi43NTI0VjI2LjMwMjhINTYyLjEyOFY0MS4xNTUxSDU5NS4xOTNWNTQuNzA2NUg1NjIuMTI4VjcxLjgzNEg1OTUuMTkzVjg1LjM4NDRINTQ3LjM5NVYxMi43NTI0SDU5NS4xOTNaIiBmaWxsPSIjMUYxRjI5Ii8+CjxwYXRoIGQ9Ik0xNjcuMjAxIDU3LjQxNThIMTg2LjUzNkMxOTAuODg2IDU3LjQ2NjIgMTk1LjE2OCA1Ni4zMzQ4IDE5OC45MTggNTQuMTQzN0MyMDIuMTc5IDUyLjIxOTkgMjA0Ljg2OSA0OS40NzM2IDIwNi43MTYgNDYuMTgzNUMyMDguNTYyIDQyLjg5MzQgMjA5LjUgMzkuMTc2NiAyMDkuNDMzIDM1LjQxMDJDMjA5LjQzMyAyMS45Njc1IDE5OC45NTggMTIuNzU3NCAxODQuMzM0IDEyLjc1NzRIMTUyLjQ2OFY4NS4zODk0SDE2Ny4yMDFWNTcuNDIwN1Y1Ny40MTU4Wk0xNjcuMjAxIDI2LjMwNThIMTg0LjMyOUMxOTAuNjU4IDI2LjMwNTggMTk0LjY5NiAyOS44ODQgMTk0LjY5NiAzNS40MTMzQzE5NC42OTYgNDAuODMyOSAxOTAuNjU4IDQ0LjQwOTkgMTg0LjMyOSA0NC40MDk5SDE2Ny4yMDFWMjYuMzA1OFoiIGZpbGw9IiMxRjFGMjkiLz4KPHBhdGggZD0iTTc5NC44MzUgMTIuNzUyNEg4NjAuMjA2VjI2LjMwMjhIODM0Ljg4OVY4NS4zODQ0SDgyMC4xNTZWMjYuMzAyOEg3OTQuODM1VjEyLjc1MjRaIiBmaWxsPSIjMUYxRjI5Ii8+CjxwYXRoIGQ9Ik03NDEuOTA3IDU3LjQxNThINzYxLjI0MUM3NjUuNTkyIDU3LjQ2NjEgNzY5Ljg3NCA1Ni4zMzQ3IDc3My42MjQgNTQuMTQzN0M3NzYuODg0IDUyLjIxOTkgNzc5LjU3NSA0OS40NzM2IDc4MS40MjEgNDYuMTgzNUM3ODMuMjY4IDQyLjg5MzQgNzg0LjIwNiAzOS4xNzY2IDc4NC4xMzkgMzUuNDEwMkM3ODQuMTM5IDIxLjk2NzUgNzczLjY2NCAxMi43NTc0IDc1OS4wMzkgMTIuNzU3NEg3MjcuMTc1Vjg1LjM4OTRINzQxLjkwN1Y1Ny40MjA3VjU3LjQxNThaTTc0MS45MDcgMjYuMzA1OEg3NTkuMDM1Qzc2NS4zNjUgMjYuMzA1OCA3NjkuNDAzIDI5Ljg4NCA3NjkuNDAzIDM1LjQxMzNDNzY5LjQwMyA0MC44MzI5IDc2NS4zNjUgNDQuNDA5OSA3NTkuMDM1IDQ0LjQwOTlINzQxLjkwN1YyNi4zMDU4WiIgZmlsbD0iIzFGMUYyOSIvPgo8cGF0aCBkPSJNNjgxLjA2OSA0Ny4wMTE1VjU5LjAxMjVINjk1LjM3OVY3MS42NzE5QzY5Mi41MjYgNzMuNDM2OCA2ODguNTI0IDc0LjMzMTkgNjgzLjQ3NyA3NC4zMzE5QzY2Ni4wMDMgNzQuMzMxOSA2NTguMDQ1IDYxLjgxMjQgNjU4LjA0NSA1MC4xOEM2NTguMDQ1IDMzLjk2MDUgNjcxLjAwOCAyNS40NzMyIDY4My44MTIgMjUuNDczMkM2OTAuNDI1IDI1LjQ2MjggNjk2LjkwOSAyNy4yODA0IDcwMi41NDEgMzAuNzIyNkw3MDMuMTU3IDMxLjEyNTRMNzA1Ljk1OCAxOC4xODZMNzA1LjY2MyAxNy45OTc3QzcwMC4wNDYgMTQuNDAwNCA2OTEuMjkxIDEyLjI1OSA2ODIuMjUxIDEyLjI1OUM2NjMuMTk3IDEyLjI1OSA2NDIuOTQ5IDI1LjM5NjcgNjQyLjk0OSA0OS43NDVDNjQyLjk0OSA2MS4wODQ1IDY0Ny4yOTMgNzAuNzE3NCA2NTUuNTExIDc3LjYwMjlDNjYzLjIyNCA4My44MjQ1IDY3Mi44NzQgODcuMTg5IDY4Mi44MDkgODcuMTIwMUM2OTQuMzYzIDg3LjEyMDEgNzAzLjA2MSA4NC42NDk1IDcwOS40MDIgNzkuNTY5Mkw3MDkuNTg5IDc5LjQxODFWNDcuMDExNUg2ODEuMDY5WiIgZmlsbD0iIzFGMUYyOSIvPgo8L2c+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzVfMTkiPgo8cmVjdCB3aWR0aD0iNzA3Ljc3OCIgaGVpZ2h0PSI3NC44NjExIiBmaWxsPSJ3aGl0ZSIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTUyLjQ0NCAxMi4yNSkiLz4KPC9jbGlwUGF0aD4KPC9kZWZzPgo8L3N2Zz4K"
```

## File: `private_gpt/ui/ui.py`
```python
"""This file should be imported if and only if you want to run the UI locally."""

import base64
import logging
import time
from collections.abc import Iterable
from enum import Enum
from pathlib import Path
from typing import Any

import gradio as gr  # type: ignore
from fastapi import FastAPI
from gradio.themes.utils.colors import slate  # type: ignore
from injector import inject, singleton
from llama_index.core.llms import ChatMessage, ChatResponse, MessageRole
from llama_index.core.types import TokenGen
from pydantic import BaseModel

from private_gpt.constants import PROJECT_ROOT_PATH
from private_gpt.di import global_injector
from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.server.chat.chat_service import ChatService, CompletionGen
from private_gpt.server.chunks.chunks_service import Chunk, ChunksService
from private_gpt.server.ingest.ingest_service import IngestService
from private_gpt.server.recipes.summarize.summarize_service import SummarizeService
from private_gpt.settings.settings import settings
from private_gpt.ui.images import logo_svg

logger = logging.getLogger(__name__)

THIS_DIRECTORY_RELATIVE = Path(__file__).parent.relative_to(PROJECT_ROOT_PATH)
# Should be "private_gpt/ui/avatar-bot.ico"
AVATAR_BOT = THIS_DIRECTORY_RELATIVE / "avatar-bot.ico"

UI_TAB_TITLE = "My Private GPT"

SOURCES_SEPARATOR = "<hr>Sources: \n"


class Modes(str, Enum):
    RAG_MODE = "RAG"
    SEARCH_MODE = "Search"
    BASIC_CHAT_MODE = "Basic"
    SUMMARIZE_MODE = "Summarize"


MODES: list[Modes] = [
    Modes.RAG_MODE,
    Modes.SEARCH_MODE,
    Modes.BASIC_CHAT_MODE,
    Modes.SUMMARIZE_MODE,
]


class Source(BaseModel):
    file: str
    page: str
    text: str

    class Config:
        frozen = True

    @staticmethod
    def curate_sources(sources: list[Chunk]) -> list["Source"]:
        curated_sources = []

        for chunk in sources:
            doc_metadata = chunk.document.doc_metadata

            file_name = doc_metadata.get("file_name", "-") if doc_metadata else "-"
            page_label = doc_metadata.get("page_label", "-") if doc_metadata else "-"

            source = Source(file=file_name, page=page_label, text=chunk.text)
            curated_sources.append(source)
            curated_sources = list(
                dict.fromkeys(curated_sources).keys()
            )  # Unique sources only

        return curated_sources


@singleton
class PrivateGptUi:
    @inject
    def __init__(
        self,
        ingest_service: IngestService,
        chat_service: ChatService,
        chunks_service: ChunksService,
        summarizeService: SummarizeService,
    ) -> None:
        self._ingest_service = ingest_service
        self._chat_service = chat_service
        self._chunks_service = chunks_service
        self._summarize_service = summarizeService

        # Cache the UI blocks
        self._ui_block = None

        self._selected_filename = None

        # Initialize system prompt based on default mode
        default_mode_map = {mode.value: mode for mode in Modes}
        self._default_mode = default_mode_map.get(
            settings().ui.default_mode, Modes.RAG_MODE
        )
        self._system_prompt = self._get_default_system_prompt(self._default_mode)

    def _chat(
        self, message: str, history: list[list[str]], mode: Modes, *_: Any
    ) -> Any:
        def yield_deltas(completion_gen: CompletionGen) -> Iterable[str]:
            full_response: str = ""
            stream = completion_gen.response
            for delta in stream:
                if isinstance(delta, str):
                    full_response += str(delta)
                elif isinstance(delta, ChatResponse):
                    full_response += delta.delta or ""
                yield full_response
                time.sleep(0.02)

            if completion_gen.sources:
                full_response += SOURCES_SEPARATOR
                cur_sources = Source.curate_sources(completion_gen.sources)
                sources_text = "\n\n\n"
                used_files = set()
                for index, source in enumerate(cur_sources, start=1):
                    if f"{source.file}-{source.page}" not in used_files:
                        sources_text = (
                            sources_text
                            + f"{index}. {source.file} (page {source.page}) \n\n"
                        )
                        used_files.add(f"{source.file}-{source.page}")
                sources_text += "<hr>\n\n"
                full_response += sources_text
            yield full_response

        def yield_tokens(token_gen: TokenGen) -> Iterable[str]:
            full_response: str = ""
            for token in token_gen:
                full_response += str(token)
                yield full_response

        def build_history() -> list[ChatMessage]:
            history_messages: list[ChatMessage] = []

            for interaction in history:
                history_messages.append(
                    ChatMessage(content=interaction[0], role=MessageRole.USER)
                )
                if len(interaction) > 1 and interaction[1] is not None:
                    history_messages.append(
                        ChatMessage(
                            # Remove from history content the Sources information
                            content=interaction[1].split(SOURCES_SEPARATOR)[0],
                            role=MessageRole.ASSISTANT,
                        )
                    )

            # max 20 messages to try to avoid context overflow
            return history_messages[:20]

        new_message = ChatMessage(content=message, role=MessageRole.USER)
        all_messages = [*build_history(), new_message]
        # If a system prompt is set, add it as a system message
        if self._system_prompt:
            all_messages.insert(
                0,
                ChatMessage(
                    content=self._system_prompt,
                    role=MessageRole.SYSTEM,
                ),
            )
        match mode:
            case Modes.RAG_MODE:
                # Use only the selected file for the query
                context_filter = None
                if self._selected_filename is not None:
                    docs_ids = []
                    for ingested_document in self._ingest_service.list_ingested():
                        if (
                            ingested_document.doc_metadata["file_name"]
                            == self._selected_filename
                        ):
                            docs_ids.append(ingested_document.doc_id)
                    context_filter = ContextFilter(docs_ids=docs_ids)

                query_stream = self._chat_service.stream_chat(
                    messages=all_messages,
                    use_context=True,
                    context_filter=context_filter,
                )
                yield from yield_deltas(query_stream)
            case Modes.BASIC_CHAT_MODE:
                llm_stream = self._chat_service.stream_chat(
                    messages=all_messages,
                    use_context=False,
                )
                yield from yield_deltas(llm_stream)

            case Modes.SEARCH_MODE:
                response = self._chunks_service.retrieve_relevant(
                    text=message, limit=4, prev_next_chunks=0
                )

                sources = Source.curate_sources(response)

                yield "\n\n\n".join(
                    f"{index}. **{source.file} "
                    f"(page {source.page})**\n "
                    f"{source.text}"
                    for index, source in enumerate(sources, start=1)
                )
            case Modes.SUMMARIZE_MODE:
                # Summarize the given message, optionally using selected files
                context_filter = None
                if self._selected_filename:
                    docs_ids = []
                    for ingested_document in self._ingest_service.list_ingested():
                        if (
                            ingested_document.doc_metadata["file_name"]
                            == self._selected_filename
                        ):
                            docs_ids.append(ingested_document.doc_id)
                    context_filter = ContextFilter(docs_ids=docs_ids)

                summary_stream = self._summarize_service.stream_summarize(
                    use_context=True,
                    context_filter=context_filter,
                    instructions=message,
                )
                yield from yield_tokens(summary_stream)

    # On initialization and on mode change, this function set the system prompt
    # to the default prompt based on the mode (and user settings).
    @staticmethod
    def _get_default_system_prompt(mode: Modes) -> str:
        p = ""
        match mode:
            # For query chat mode, obtain default system prompt from settings
            case Modes.RAG_MODE:
                p = settings().ui.default_query_system_prompt
            # For chat mode, obtain default system prompt from settings
            case Modes.BASIC_CHAT_MODE:
                p = settings().ui.default_chat_system_prompt
            # For summarization mode, obtain default system prompt from settings
            case Modes.SUMMARIZE_MODE:
                p = settings().ui.default_summarization_system_prompt
            # For any other mode, clear the system prompt
            case _:
                p = ""
        return p

    @staticmethod
    def _get_default_mode_explanation(mode: Modes) -> str:
        match mode:
            case Modes.RAG_MODE:
                return "Get contextualized answers from selected files."
            case Modes.SEARCH_MODE:
                return "Find relevant chunks of text in selected files."
            case Modes.BASIC_CHAT_MODE:
                return "Chat with the LLM using its training data. Files are ignored."
            case Modes.SUMMARIZE_MODE:
                return "Generate a summary of the selected files. Prompt to customize the result."
            case _:
                return ""

    def _set_system_prompt(self, system_prompt_input: str) -> None:
        logger.info(f"Setting system prompt to: {system_prompt_input}")
        self._system_prompt = system_prompt_input

    def _set_explanatation_mode(self, explanation_mode: str) -> None:
        self._explanation_mode = explanation_mode

    def _set_current_mode(self, mode: Modes) -> Any:
        self.mode = mode
        self._set_system_prompt(self._get_default_system_prompt(mode))
        self._set_explanatation_mode(self._get_default_mode_explanation(mode))
        interactive = self._system_prompt is not None
        return [
            gr.update(placeholder=self._system_prompt, interactive=interactive),
            gr.update(value=self._explanation_mode),
        ]

    def _list_ingested_files(self) -> list[list[str]]:
        files = set()
        for ingested_document in self._ingest_service.list_ingested():
            if ingested_document.doc_metadata is None:
                # Skipping documents without metadata
                continue
            file_name = ingested_document.doc_metadata.get(
                "file_name", "[FILE NAME MISSING]"
            )
            files.add(file_name)
        return [[row] for row in files]

    def _upload_file(self, files: list[str]) -> None:
        logger.debug("Loading count=%s files", len(files))
        paths = [Path(file) for file in files]

        # remove all existing Documents with name identical to a new file upload:
        file_names = [path.name for path in paths]
        doc_ids_to_delete = []
        for ingested_document in self._ingest_service.list_ingested():
            if (
                ingested_document.doc_metadata
                and ingested_document.doc_metadata["file_name"] in file_names
            ):
                doc_ids_to_delete.append(ingested_document.doc_id)
        if len(doc_ids_to_delete) > 0:
            logger.info(
                "Uploading file(s) which were already ingested: %s document(s) will be replaced.",
                len(doc_ids_to_delete),
            )
            for doc_id in doc_ids_to_delete:
                self._ingest_service.delete(doc_id)

        self._ingest_service.bulk_ingest([(str(path.name), path) for path in paths])

    def _delete_all_files(self) -> Any:
        ingested_files = self._ingest_service.list_ingested()
        logger.debug("Deleting count=%s files", len(ingested_files))
        for ingested_document in ingested_files:
            self._ingest_service.delete(ingested_document.doc_id)
        return [
            gr.List(self._list_ingested_files()),
            gr.components.Button(interactive=False),
            gr.components.Button(interactive=False),
            gr.components.Textbox("All files"),
        ]

    def _delete_selected_file(self) -> Any:
        logger.debug("Deleting selected %s", self._selected_filename)
        # Note: keep looping for pdf's (each page became a Document)
        for ingested_document in self._ingest_service.list_ingested():
            if (
                ingested_document.doc_metadata
                and ingested_document.doc_metadata["file_name"]
                == self._selected_filename
            ):
                self._ingest_service.delete(ingested_document.doc_id)
        return [
            gr.List(self._list_ingested_files()),
            gr.components.Button(interactive=False),
            gr.components.Button(interactive=False),
            gr.components.Textbox("All files"),
        ]

    def _deselect_selected_file(self) -> Any:
        self._selected_filename = None
        return [
            gr.components.Button(interactive=False),
            gr.components.Button(interactive=False),
            gr.components.Textbox("All files"),
        ]

    def _selected_a_file(self, select_data: gr.SelectData) -> Any:
        self._selected_filename = select_data.value
        return [
            gr.components.Button(interactive=True),
            gr.components.Button(interactive=True),
            gr.components.Textbox(self._selected_filename),
        ]

    def _build_ui_blocks(self) -> gr.Blocks:
        logger.debug("Creating the UI blocks")
        with gr.Blocks(
            title=UI_TAB_TITLE,
            theme=gr.themes.Soft(primary_hue=slate),
            css=".logo { "
            "display:flex;"
            "background-color: #C7BAFF;"
            "height: 80px;"
            "border-radius: 8px;"
            "align-content: center;"
            "justify-content: center;"
            "align-items: center;"
            "}"
            ".logo img { height: 25% }"
            ".contain { display: flex !important; flex-direction: column !important; }"
            "#component-0, #component-3, #component-10, #component-8  { height: 100% !important; }"
            "#chatbot { flex-grow: 1 !important; overflow: auto !important;}"
            "#col { height: calc(100vh - 112px - 16px) !important; }"
            "hr { margin-top: 1em; margin-bottom: 1em; border: 0; border-top: 1px solid #FFF; }"
            ".avatar-image { background-color: antiquewhite; border-radius: 2px; }"
            ".footer { text-align: center; margin-top: 20px; font-size: 14px; display: flex; align-items: center; justify-content: center; }"
            ".footer-zylon-link { display:flex; margin-left: 5px; text-decoration: auto; color: var(--body-text-color); }"
            ".footer-zylon-link:hover { color: #C7BAFF; }"
            ".footer-zylon-ico { height: 20px; margin-left: 5px; background-color: antiquewhite; border-radius: 2px; }",
        ) as blocks:
            with gr.Row():
                gr.HTML(f"<div class='logo'/><img src={logo_svg} alt=PrivateGPT></div")

            with gr.Row(equal_height=False):
                with gr.Column(scale=3):
                    default_mode = self._default_mode
                    mode = gr.Radio(
                        [mode.value for mode in MODES],
                        label="Mode",
                        value=default_mode,
                    )
                    explanation_mode = gr.Textbox(
                        placeholder=self._get_default_mode_explanation(default_mode),
                        show_label=False,
                        max_lines=3,
                        interactive=False,
                    )
                    upload_button = gr.components.UploadButton(
                        "Upload File(s)",
                        type="filepath",
                        file_count="multiple",
                        size="sm",
                    )
                    ingested_dataset = gr.List(
                        self._list_ingested_files,
                        headers=["File name"],
                        label="Ingested Files",
                        height=235,
                        interactive=False,
                        render=False,  # Rendered under the button
                    )
                    upload_button.upload(
                        self._upload_file,
                        inputs=upload_button,
                        outputs=ingested_dataset,
                    )
                    ingested_dataset.change(
                        self._list_ingested_files,
                        outputs=ingested_dataset,
                    )
                    ingested_dataset.render()
                    deselect_file_button = gr.components.Button(
                        "De-select selected file", size="sm", interactive=False
                    )
                    selected_text = gr.components.Textbox(
                        "All files", label="Selected for Query or Deletion", max_lines=1
                    )
                    delete_file_button = gr.components.Button(
                        "🗑️ Delete selected file",
                        size="sm",
                        visible=settings().ui.delete_file_button_enabled,
                        interactive=False,
                    )
                    delete_files_button = gr.components.Button(
                        "⚠️ Delete ALL files",
                        size="sm",
                        visible=settings().ui.delete_all_files_button_enabled,
                    )
                    deselect_file_button.click(
                        self._deselect_selected_file,
                        outputs=[
                            delete_file_button,
                            deselect_file_button,
                            selected_text,
                        ],
                    )
                    ingested_dataset.select(
                        fn=self._selected_a_file,
                        outputs=[
                            delete_file_button,
                            deselect_file_button,
                            selected_text,
                        ],
                    )
                    delete_file_button.click(
                        self._delete_selected_file,
                        outputs=[
                            ingested_dataset,
                            delete_file_button,
                            deselect_file_button,
                            selected_text,
                        ],
                    )
                    delete_files_button.click(
                        self._delete_all_files,
                        outputs=[
                            ingested_dataset,
                            delete_file_button,
                            deselect_file_button,
                            selected_text,
                        ],
                    )
                    system_prompt_input = gr.Textbox(
                        placeholder=self._system_prompt,
                        label="System Prompt",
                        lines=2,
                        interactive=True,
                        render=False,
                    )
                    # When mode changes, set default system prompt, and other stuffs
                    mode.change(
                        self._set_current_mode,
                        inputs=mode,
                        outputs=[system_prompt_input, explanation_mode],
                    )
                    # On blur, set system prompt to use in queries
                    system_prompt_input.blur(
                        self._set_system_prompt,
                        inputs=system_prompt_input,
                    )

                    def get_model_label() -> str | None:
                        """Get model label from llm mode setting YAML.

                        Raises:
                            ValueError: If an invalid 'llm_mode' is encountered.

                        Returns:
                            str: The corresponding model label.
                        """
                        # Get model label from llm mode setting YAML
                        # Labels: local, openai, openailike, sagemaker, mock, ollama
                        config_settings = settings()
                        if config_settings is None:
                            raise ValueError("Settings are not configured.")

                        # Get llm_mode from settings
                        llm_mode = config_settings.llm.mode

                        # Mapping of 'llm_mode' to corresponding model labels
                        model_mapping = {
                            "llamacpp": config_settings.llamacpp.llm_hf_model_file,
                            "openai": config_settings.openai.model,
                            "openailike": config_settings.openai.model,
                            "azopenai": config_settings.azopenai.llm_model,
                            "sagemaker": config_settings.sagemaker.llm_endpoint_name,
                            "mock": llm_mode,
                            "ollama": config_settings.ollama.llm_model,
                            "gemini": config_settings.gemini.model,
                        }

                        if llm_mode not in model_mapping:
                            print(f"Invalid 'llm mode': {llm_mode}")
                            return None

                        return model_mapping[llm_mode]

                with gr.Column(scale=7, elem_id="col"):
                    # Determine the model label based on the value of PGPT_PROFILES
                    model_label = get_model_label()
                    if model_label is not None:
                        label_text = (
                            f"LLM: {settings().llm.mode} | Model: {model_label}"
                        )
                    else:
                        label_text = f"LLM: {settings().llm.mode}"

                    _ = gr.ChatInterface(
                        self._chat,
                        chatbot=gr.Chatbot(
                            label=label_text,
                            show_copy_button=True,
                            elem_id="chatbot",
                            render=False,
                            avatar_images=(
                                None,
                                AVATAR_BOT,
                            ),
                        ),
                        additional_inputs=[mode, upload_button, system_prompt_input],
                    )

            with gr.Row():
                avatar_byte = AVATAR_BOT.read_bytes()
                f_base64 = f"data:image/png;base64,{base64.b64encode(avatar_byte).decode('utf-8')}"
                gr.HTML(
                    f"<div class='footer'><a class='footer-zylon-link' href='https://zylon.ai/'>Maintained by Zylon <img class='footer-zylon-ico' src='{f_base64}' alt=Zylon></a></div>"
                )

        return blocks

    def get_ui_blocks(self) -> gr.Blocks:
        if self._ui_block is None:
            self._ui_block = self._build_ui_blocks()
        return self._ui_block

    def mount_in_app(self, app: FastAPI, path: str) -> None:
        blocks = self.get_ui_blocks()
        blocks.queue()
        logger.info("Mounting the gradio UI, at path=%s", path)
        gr.mount_gradio_app(app, blocks, path=path, favicon_path=AVATAR_BOT)


if __name__ == "__main__":
    ui = global_injector.get(PrivateGptUi)
    _blocks = ui.get_ui_blocks()
    _blocks.queue()
    _blocks.launch(debug=False, show_api=False)
```

## File: `private_gpt/utils/__init__.py`
```python
"""general utils."""
```

## File: `private_gpt/utils/eta.py`
```python
import datetime
import logging
import math
import time
from collections import deque
from typing import Any

logger = logging.getLogger(__name__)


def human_time(*args: Any, **kwargs: Any) -> str:
    def timedelta_total_seconds(timedelta: datetime.timedelta) -> float:
        return (
            timedelta.microseconds
            + 0.0
            + (timedelta.seconds + timedelta.days * 24 * 3600) * 10**6
        ) / 10**6

    secs = float(timedelta_total_seconds(datetime.timedelta(*args, **kwargs)))
    # We want (ms) precision below 2 seconds
    if secs < 2:
        return f"{secs * 1000}ms"
    units = [("y", 86400 * 365), ("d", 86400), ("h", 3600), ("m", 60), ("s", 1)]
    parts = []
    for unit, mul in units:
        if secs / mul >= 1 or mul == 1:
            if mul > 1:
                n = int(math.floor(secs / mul))
                secs -= n * mul
            else:
                # >2s we drop the (ms) component.
                n = int(secs)
            if n:
                parts.append(f"{n}{unit}")
    return " ".join(parts)


def eta(iterator: list[Any]) -> Any:
    """Report an ETA after 30s and every 60s thereafter."""
    total = len(iterator)
    _eta = ETA(total)
    _eta.needReport(30)
    for processed, data in enumerate(iterator, start=1):
        yield data
        _eta.update(processed)
        if _eta.needReport(60):
            logger.info(f"{processed}/{total} - ETA {_eta.human_time()}")


class ETA:
    """Predict how long something will take to complete."""

    def __init__(self, total: int):
        self.total: int = total  # Total expected records.
        self.rate: float = 0.0  # per second
        self._timing_data: deque[tuple[float, int]] = deque(maxlen=100)
        self.secondsLeft: float = 0.0
        self.nexttime: float = 0.0

    def human_time(self) -> str:
        if self._calc():
            return f"{human_time(seconds=self.secondsLeft)} @ {int(self.rate * 60)}/min"
        return "(computing)"

    def update(self, count: int) -> None:
        # count should be in the range 0 to self.total
        assert count > 0
        assert count <= self.total
        self._timing_data.append((time.time(), count))  # (X,Y) for pearson

    def needReport(self, whenSecs: int) -> bool:
        now = time.time()
        if now > self.nexttime:
            self.nexttime = now + whenSecs
            return True
        return False

    def _calc(self) -> bool:
        # A sample before a prediction.   Need two points to compute slope!
        if len(self._timing_data) < 3:
            return False

        # http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient
        # Calculate means and standard deviations.
        samples = len(self._timing_data)
        # column wise sum of the timing tuples to compute their mean.
        mean_x, mean_y = (
            sum(i) / samples for i in zip(*self._timing_data, strict=False)
        )
        std_x = math.sqrt(
            sum(pow(i[0] - mean_x, 2) for i in self._timing_data) / (samples - 1)
        )
        std_y = math.sqrt(
            sum(pow(i[1] - mean_y, 2) for i in self._timing_data) / (samples - 1)
        )

        # Calculate coefficient.
        sum_xy, sum_sq_v_x, sum_sq_v_y = 0.0, 0.0, 0
        for x, y in self._timing_data:
            x -= mean_x
            y -= mean_y
            sum_xy += x * y
            sum_sq_v_x += pow(x, 2)
            sum_sq_v_y += pow(y, 2)
        pearson_r = sum_xy / math.sqrt(sum_sq_v_x * sum_sq_v_y)

        # Calculate regression line.
        # y = mx + b where m is the slope and b is the y-intercept.
        m = self.rate = pearson_r * (std_y / std_x)
        y = self.total
        b = mean_y - m * mean_x
        x = (y - b) / m

        # Calculate fitted line (transformed/shifted regression line horizontally).
        fitted_b = self._timing_data[-1][1] - (m * self._timing_data[-1][0])
        fitted_x = (y - fitted_b) / m
        _, count = self._timing_data[-1]  # adjust last data point progress count
        adjusted_x = ((fitted_x - x) * (count / self.total)) + x
        eta_epoch = adjusted_x

        self.secondsLeft = max([eta_epoch - time.time(), 0])
        return True
```

## File: `private_gpt/utils/ollama.py`
```python
import logging
from collections import deque
from collections.abc import Iterator, Mapping
from typing import Any

from httpx import ConnectError
from tqdm import tqdm  # type: ignore

from private_gpt.utils.retry import retry

try:
    from ollama import Client, ResponseError  # type: ignore
except ImportError as e:
    raise ImportError(
        "Ollama dependencies not found, install with `poetry install --extras llms-ollama or embeddings-ollama`"
    ) from e

logger = logging.getLogger(__name__)

_MAX_RETRIES = 5
_JITTER = (3.0, 10.0)


@retry(
    is_async=False,
    exceptions=(ConnectError, ResponseError),
    tries=_MAX_RETRIES,
    jitter=_JITTER,
    logger=logger,
)
def check_connection(client: Client) -> bool:
    try:
        client.list()
        return True
    except (ConnectError, ResponseError) as e:
        raise e
    except Exception as e:
        logger.error(f"Failed to connect to Ollama: {type(e).__name__}: {e!s}")
        return False


def process_streaming(generator: Iterator[Mapping[str, Any]]) -> None:
    progress_bars = {}
    queue = deque()  # type: ignore

    def create_progress_bar(dgt: str, total: int) -> Any:
        return tqdm(
            total=total, desc=f"Pulling model {dgt[7:17]}...", unit="B", unit_scale=True
        )

    current_digest = None

    for chunk in generator:
        digest = chunk.get("digest")
        completed_size = chunk.get("completed", 0)
        total_size = chunk.get("total")

        if digest and total_size is not None:
            if digest not in progress_bars and completed_size > 0:
                progress_bars[digest] = create_progress_bar(digest, total=total_size)
                if current_digest is None:
                    current_digest = digest
                else:
                    queue.append(digest)

            if digest in progress_bars:
                progress_bar = progress_bars[digest]
                progress = completed_size - progress_bar.n
                if completed_size > 0 and total_size >= progress != progress_bar.n:
                    if digest == current_digest:
                        progress_bar.update(progress)
                        if progress_bar.n >= total_size:
                            progress_bar.close()
                            current_digest = queue.popleft() if queue else None
                    else:
                        # Store progress for later update
                        progress_bars[digest].total = total_size
                        progress_bars[digest].n = completed_size

    # Close any remaining progress bars at the end
    for progress_bar in progress_bars.values():
        progress_bar.close()


def pull_model(client: Client, model_name: str, raise_error: bool = True) -> None:
    try:
        installed_models = [model["name"] for model in client.list().get("models", {})]
        if model_name not in installed_models:
            logger.info(f"Pulling model {model_name}. Please wait...")
            process_streaming(client.pull(model_name, stream=True))
            logger.info(f"Model {model_name} pulled successfully")
    except Exception as e:
        logger.error(f"Failed to pull model {model_name}: {e!s}")
        if raise_error:
            raise e
```

## File: `private_gpt/utils/retry.py`
```python
import logging
from collections.abc import Callable
from typing import Any

from retry_async import retry as retry_untyped  # type: ignore

retry_logger = logging.getLogger(__name__)


def retry(
    exceptions: Any = Exception,
    *,
    is_async: bool = False,
    tries: int = -1,
    delay: float = 0,
    max_delay: float | None = None,
    backoff: float = 1,
    jitter: float | tuple[float, float] = 0,
    logger: logging.Logger = retry_logger,
) -> Callable[..., Any]:
    wrapped = retry_untyped(
        exceptions=exceptions,
        is_async=is_async,
        tries=tries,
        delay=delay,
        max_delay=max_delay,
        backoff=backoff,
        jitter=jitter,
        logger=logger,
    )
    return wrapped  # type: ignore
```

## File: `private_gpt/utils/typing.py`
```python
from typing import TypeVar

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")
```

## File: `scripts/__init__.py`
```python
"""PrivateGPT scripts."""
```

## File: `scripts/extract_openapi.py`
```python
import argparse
import json
import sys

import yaml
from uvicorn.importer import import_from_string

parser = argparse.ArgumentParser(prog="extract_openapi.py")
parser.add_argument("app", help='App import string. Eg. "main:app"', default="main:app")
parser.add_argument("--app-dir", help="Directory containing the app", default=None)
parser.add_argument(
    "--out", help="Output file ending in .json or .yaml", default="openapi.yaml"
)

if __name__ == "__main__":
    args = parser.parse_args()

    if args.app_dir is not None:
        print(f"adding {args.app_dir} to sys.path")
        sys.path.insert(0, args.app_dir)

    print(f"importing app from {args.app}")
    app = import_from_string(args.app)
    openapi = app.openapi()
    version = openapi.get("openapi", "unknown version")

    print(f"writing openapi spec v{version}")
    with open(args.out, "w") as f:
        if args.out.endswith(".json"):
            json.dump(openapi, f, indent=2)
        else:
            yaml.dump(openapi, f, sort_keys=False)

    print(f"spec written to {args.out}")
```

## File: `scripts/ingest_folder.py`
```python
#!/usr/bin/env python3

import argparse
import logging
from pathlib import Path

from private_gpt.di import global_injector
from private_gpt.server.ingest.ingest_service import IngestService
from private_gpt.server.ingest.ingest_watcher import IngestWatcher
from private_gpt.settings.settings import Settings

logger = logging.getLogger(__name__)


class LocalIngestWorker:
    def __init__(self, ingest_service: IngestService, setting: Settings) -> None:
        self.ingest_service = ingest_service

        self.total_documents = 0
        self.current_document_count = 0

        self._files_under_root_folder: list[Path] = []

        self.is_local_ingestion_enabled = setting.data.local_ingestion.enabled
        self.allowed_local_folders = setting.data.local_ingestion.allow_ingest_from

    def _validate_folder(self, folder_path: Path) -> None:
        if not self.is_local_ingestion_enabled:
            raise ValueError(
                "Local ingestion is disabled."
                "You can enable it in settings `ingestion.enabled`"
            )

        # Allow all folders if wildcard is present
        if "*" in self.allowed_local_folders:
            return

        for allowed_folder in self.allowed_local_folders:
            if not folder_path.is_relative_to(allowed_folder):
                raise ValueError(f"Folder {folder_path} is not allowed for ingestion")

    def _find_all_files_in_folder(self, root_path: Path, ignored: list[str]) -> None:
        """Search all files under the root folder recursively.

        Count them at the same time
        """
        for file_path in root_path.iterdir():
            if file_path.is_file() and file_path.name not in ignored:
                self.total_documents += 1
                self._validate_folder(file_path)
                self._files_under_root_folder.append(file_path)
            elif file_path.is_dir() and file_path.name not in ignored:
                self._find_all_files_in_folder(file_path, ignored)

    def ingest_folder(self, folder_path: Path, ignored: list[str]) -> None:
        # Count total documents before ingestion
        self._find_all_files_in_folder(folder_path, ignored)
        self._ingest_all(self._files_under_root_folder)

    def _ingest_all(self, files_to_ingest: list[Path]) -> None:
        logger.info("Ingesting files=%s", [f.name for f in files_to_ingest])
        self.ingest_service.bulk_ingest([(str(p.name), p) for p in files_to_ingest])

    def ingest_on_watch(self, changed_path: Path) -> None:
        logger.info("Detected change in at path=%s, ingesting", changed_path)
        self._do_ingest_one(changed_path)

    def _do_ingest_one(self, changed_path: Path) -> None:
        try:
            if changed_path.exists():
                logger.info(f"Started ingesting file={changed_path}")
                self.ingest_service.ingest_file(changed_path.name, changed_path)
                logger.info(f"Completed ingesting file={changed_path}")
        except Exception:
            logger.exception(
                f"Failed to ingest document: {changed_path}, find the exception attached"
            )


parser = argparse.ArgumentParser(prog="ingest_folder.py")
parser.add_argument("folder", help="Folder to ingest")
parser.add_argument(
    "--watch",
    help="Watch for changes",
    action=argparse.BooleanOptionalAction,
    default=False,
)
parser.add_argument(
    "--ignored",
    nargs="*",
    help="List of files/directories to ignore",
    default=[],
)
parser.add_argument(
    "--log-file",
    help="Optional path to a log file. If provided, logs will be written to this file.",
    type=str,
    default=None,
)

args = parser.parse_args()

# Set up logging to a file if a path is provided
if args.log_file:
    file_handler = logging.FileHandler(args.log_file, mode="a")
    file_handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s.%(msecs)03d] [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    logger.addHandler(file_handler)

if __name__ == "__main__":
    root_path = Path(args.folder)
    if not root_path.exists():
        raise ValueError(f"Path {args.folder} does not exist")

    ingest_service = global_injector.get(IngestService)
    settings = global_injector.get(Settings)
    worker = LocalIngestWorker(ingest_service, settings)
    worker.ingest_folder(root_path, args.ignored)

    if args.ignored:
        logger.info(f"Skipping following files and directories: {args.ignored}")

    if args.watch:
        logger.info(f"Watching {args.folder} for changes, press Ctrl+C to stop...")
        directories_to_watch = [
            dir
            for dir in root_path.iterdir()
            if dir.is_dir() and dir.name not in args.ignored
        ]
        watcher = IngestWatcher(args.folder, worker.ingest_on_watch)
        watcher.start()
```

## File: `scripts/setup`
```
#!/usr/bin/env python3
import os
import argparse

from huggingface_hub import hf_hub_download, snapshot_download
from transformers import AutoTokenizer

from private_gpt.paths import models_path, models_cache_path
from private_gpt.settings.settings import settings

resume_download = True
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Setup: Download models from Hugging Face')
    parser.add_argument('--resume', default=True, action=argparse.BooleanOptionalAction, help='Enable/Disable resume_download options to restart the download progress interrupted')
    args = parser.parse_args()
    resume_download = args.resume

os.makedirs(models_path, exist_ok=True)

# Download Embedding model
embedding_path = models_path / "embedding"
print(f"Downloading embedding {settings().huggingface.embedding_hf_model_name}")
snapshot_download(
    repo_id=settings().huggingface.embedding_hf_model_name,
    cache_dir=models_cache_path,
    local_dir=embedding_path,
    token=settings().huggingface.access_token,
)
print("Embedding model downloaded!")

# Download LLM and create a symlink to the model file
print(f"Downloading LLM {settings().llamacpp.llm_hf_model_file}")
hf_hub_download(
    repo_id=settings().llamacpp.llm_hf_repo_id,
    filename=settings().llamacpp.llm_hf_model_file,
    cache_dir=models_cache_path,
    local_dir=models_path,
    resume_download=resume_download,
    token=settings().huggingface.access_token,
)
print("LLM model downloaded!")

# Download Tokenizer
if settings().llm.tokenizer:
    print(f"Downloading tokenizer {settings().llm.tokenizer}")
    AutoTokenizer.from_pretrained(
        pretrained_model_name_or_path=settings().llm.tokenizer,
        cache_dir=models_cache_path,
        token=settings().huggingface.access_token,
    )
    print("Tokenizer downloaded!")

print("Setup done")
```

## File: `scripts/utils.py`
```python
import argparse
import os
import shutil
from typing import Any, ClassVar

from private_gpt.paths import local_data_path
from private_gpt.settings.settings import settings


def wipe_file(file: str) -> None:
    if os.path.isfile(file):
        os.remove(file)
        print(f" - Deleted {file}")


def wipe_tree(path: str) -> None:
    if not os.path.exists(path):
        print(f"Warning: Path not found {path}")
        return
    print(f"Wiping {path}...")
    all_files = os.listdir(path)

    files_to_remove = [file for file in all_files if file != ".gitignore"]
    for file_name in files_to_remove:
        file_path = os.path.join(path, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print(f" - Deleted {file_path}")
        except PermissionError:
            print(
                f"PermissionError: Unable to remove {file_path}. It is in use by another process."
            )
            continue


class Postgres:
    tables: ClassVar[dict[str, list[str]]] = {
        "nodestore": ["data_docstore", "data_indexstore"],
        "vectorstore": ["data_embeddings"],
    }

    def __init__(self) -> None:
        try:
            import psycopg2
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Postgres dependencies not found") from None

        connection = settings().postgres.model_dump(exclude_none=True)
        self.schema = connection.pop("schema_name")
        self.conn = psycopg2.connect(**connection)

    def wipe(self, storetype: str) -> None:
        cur = self.conn.cursor()
        try:
            for table in self.tables[storetype]:
                sql = f"DROP TABLE IF EXISTS {self.schema}.{table}"
                cur.execute(sql)
                print(f"Table {self.schema}.{table} dropped.")
            self.conn.commit()
        finally:
            cur.close()

    def stats(self, store_type: str) -> None:
        template = "SELECT '{table}', COUNT(*), pg_size_pretty(pg_total_relation_size('{table}')) FROM {table}"
        sql = " UNION ALL ".join(
            template.format(table=tbl) for tbl in self.tables[store_type]
        )

        cur = self.conn.cursor()
        try:
            print(f"Storage for Postgres {store_type}.")
            print("{:<15} | {:>15} | {:>9}".format("Table", "Rows", "Size"))
            print("-" * 45)  # Print a line separator

            cur.execute(sql)
            for row in cur.fetchall():
                formatted_row_count = f"{row[1]:,}"
                print(f"{row[0]:<15} | {formatted_row_count:>15} | {row[2]:>9}")

            print()
        finally:
            cur.close()

    def __del__(self):
        if hasattr(self, "conn") and self.conn:
            self.conn.close()


class Simple:
    def wipe(self, store_type: str) -> None:
        assert store_type == "nodestore"
        from llama_index.core.storage.docstore.types import (
            DEFAULT_PERSIST_FNAME as DOCSTORE,
        )
        from llama_index.core.storage.index_store.types import (
            DEFAULT_PERSIST_FNAME as INDEXSTORE,
        )

        for store in (DOCSTORE, INDEXSTORE):
            wipe_file(str((local_data_path / store).absolute()))


class Chroma:
    def wipe(self, store_type: str) -> None:
        assert store_type == "vectorstore"
        wipe_tree(str((local_data_path / "chroma_db").absolute()))


class Qdrant:
    COLLECTION = (
        "make_this_parameterizable_per_api_call"  # ?! see vector_store_component.py
    )

    def __init__(self) -> None:
        try:
            from qdrant_client import QdrantClient  # type: ignore
        except ImportError:
            raise ImportError("Qdrant dependencies not found") from None
        self.client = QdrantClient(**settings().qdrant.model_dump(exclude_none=True))

    def wipe(self, store_type: str) -> None:
        assert store_type == "vectorstore"
        try:
            self.client.delete_collection(self.COLLECTION)
            print("Collection dropped successfully.")
        except Exception as e:
            print("Error dropping collection:", e)

    def stats(self, store_type: str) -> None:
        print(f"Storage for Qdrant {store_type}.")
        try:
            collection_data = self.client.get_collection(self.COLLECTION)
            if collection_data:
                # Collection Info
                # https://qdrant.tech/documentation/concepts/collections/
                print(f"\tPoints:        {collection_data.points_count:,}")
                print(f"\tVectors:       {collection_data.vectors_count:,}")
                print(f"\tIndex Vectors: {collection_data.indexed_vectors_count:,}")
                return
        except ValueError:
            pass
        print("\t- Qdrant collection not found or empty")


class Command:
    DB_HANDLERS: ClassVar[dict[str, Any]] = {
        "simple": Simple,  # node store
        "chroma": Chroma,  # vector store
        "postgres": Postgres,  # node, index and vector store
        "qdrant": Qdrant,  # vector store
    }

    def for_each_store(self, cmd: str):
        for store_type in ("nodestore", "vectorstore"):
            database = getattr(settings(), store_type).database
            handler_class = self.DB_HANDLERS.get(database)
            if handler_class is None:
                print(f"No handler found for database '{database}'")
                continue
            handler_instance = handler_class()  # Instantiate the class
            # If the DB can handle this cmd dispatch it.
            if hasattr(handler_instance, cmd) and callable(
                func := getattr(handler_instance, cmd)
            ):
                func(store_type)
            else:
                print(
                    f"Unable to execute command '{cmd}' on '{store_type}' in database '{database}'"
                )

    def execute(self, cmd: str) -> None:
        if cmd in ("wipe", "stats"):
            self.for_each_store(cmd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="select a mode to run", choices=["wipe", "stats"])
    args = parser.parse_args()

    Command().execute(args.mode.lower())
```

## File: `tests/__init__.py`
```python
"""Tests."""
```

## File: `tests/conftest.py`
```python
import os
import pathlib
from glob import glob

root_path = pathlib.Path(__file__).parents[1]
# This is to prevent a bug in intellij that uses the wrong working directory
os.chdir(root_path)


def _as_module(fixture_path: str) -> str:
    return fixture_path.replace("/", ".").replace("\\", ".").replace(".py", "")


pytest_plugins = [_as_module(fixture) for fixture in glob("tests/fixtures/[!_]*.py")]
```

## File: `tests/test_prompt_helper.py`
```python
import pytest
from llama_index.core.llms import ChatMessage, MessageRole

from private_gpt.components.llm.prompt_helper import (
    ChatMLPromptStyle,
    DefaultPromptStyle,
    Llama2PromptStyle,
    Llama3PromptStyle,
    MistralPromptStyle,
    TagPromptStyle,
    get_prompt_style,
)


@pytest.mark.parametrize(
    ("prompt_style", "expected_prompt_style"),
    [
        ("default", DefaultPromptStyle),
        ("llama2", Llama2PromptStyle),
        ("tag", TagPromptStyle),
        ("mistral", MistralPromptStyle),
        ("chatml", ChatMLPromptStyle),
    ],
)
def test_get_prompt_style_success(prompt_style, expected_prompt_style):
    assert isinstance(get_prompt_style(prompt_style), expected_prompt_style)


def test_get_prompt_style_failure():
    prompt_style = "unknown"
    with pytest.raises(ValueError) as exc_info:
        get_prompt_style(prompt_style)
    assert str(exc_info.value) == f"Unknown prompt_style='{prompt_style}'"


def test_tag_prompt_style_format():
    prompt_style = TagPromptStyle()
    messages = [
        ChatMessage(content="You are an AI assistant.", role=MessageRole.SYSTEM),
        ChatMessage(content="Hello, how are you doing?", role=MessageRole.USER),
    ]

    expected_prompt = (
        "<|system|>: You are an AI assistant.\n"
        "<|user|>: Hello, how are you doing?\n"
        "<|assistant|>: "
    )

    assert prompt_style.messages_to_prompt(messages) == expected_prompt


def test_tag_prompt_style_format_with_system_prompt():
    prompt_style = TagPromptStyle()
    messages = [
        ChatMessage(
            content="FOO BAR Custom sys prompt from messages.", role=MessageRole.SYSTEM
        ),
        ChatMessage(content="Hello, how are you doing?", role=MessageRole.USER),
    ]

    expected_prompt = (
        "<|system|>: FOO BAR Custom sys prompt from messages.\n"
        "<|user|>: Hello, how are you doing?\n"
        "<|assistant|>: "
    )

    assert prompt_style.messages_to_prompt(messages) == expected_prompt


def test_mistral_prompt_style_format():
    prompt_style = MistralPromptStyle()
    messages = [
        ChatMessage(content="A", role=MessageRole.SYSTEM),
        ChatMessage(content="B", role=MessageRole.USER),
    ]
    expected_prompt = "<s>[INST] A\nB [/INST]"
    assert prompt_style.messages_to_prompt(messages) == expected_prompt

    messages2 = [
        ChatMessage(content="A", role=MessageRole.SYSTEM),
        ChatMessage(content="B", role=MessageRole.USER),
        ChatMessage(content="C", role=MessageRole.ASSISTANT),
        ChatMessage(content="D", role=MessageRole.USER),
    ]
    expected_prompt2 = "<s>[INST] A\nB [/INST] C</s><s>[INST] D [/INST]"
    assert prompt_style.messages_to_prompt(messages2) == expected_prompt2


def test_chatml_prompt_style_format():
    prompt_style = ChatMLPromptStyle()
    messages = [
        ChatMessage(content="You are an AI assistant.", role=MessageRole.SYSTEM),
        ChatMessage(content="Hello, how are you doing?", role=MessageRole.USER),
    ]

    expected_prompt = (
        "<|im_start|>system\n"
        "You are an AI assistant.<|im_end|>\n"
        "<|im_start|>user\n"
        "Hello, how are you doing?<|im_end|>\n"
        "<|im_start|>assistant\n"
    )

    assert prompt_style.messages_to_prompt(messages) == expected_prompt


def test_llama2_prompt_style_format():
    prompt_style = Llama2PromptStyle()
    messages = [
        ChatMessage(content="You are an AI assistant.", role=MessageRole.SYSTEM),
        ChatMessage(content="Hello, how are you doing?", role=MessageRole.USER),
    ]

    expected_prompt = (
        "<s> [INST] <<SYS>>\n"
        " You are an AI assistant. \n"
        "<</SYS>>\n"
        "\n"
        " Hello, how are you doing? [/INST]"
    )

    assert prompt_style.messages_to_prompt(messages) == expected_prompt


def test_llama2_prompt_style_with_system_prompt():
    prompt_style = Llama2PromptStyle()
    messages = [
        ChatMessage(
            content="FOO BAR Custom sys prompt from messages.", role=MessageRole.SYSTEM
        ),
        ChatMessage(content="Hello, how are you doing?", role=MessageRole.USER),
    ]

    expected_prompt = (
        "<s> [INST] <<SYS>>\n"
        " FOO BAR Custom sys prompt from messages. \n"
        "<</SYS>>\n"
        "\n"
        " Hello, how are you doing? [/INST]"
    )

    assert prompt_style.messages_to_prompt(messages) == expected_prompt


def test_llama3_prompt_style_format():
    prompt_style = Llama3PromptStyle()
    messages = [
        ChatMessage(content="You are a helpful assistant", role=MessageRole.SYSTEM),
        ChatMessage(content="Hello, how are you doing?", role=MessageRole.USER),
    ]

    expected_prompt = (
        "<|start_header_id|>system<|end_header_id|>\n\n"
        "You are a helpful assistant<|eot_id|>"
        "<|start_header_id|>user<|end_header_id|>\n\n"
        "Hello, how are you doing?<|eot_id|>"
        "<|start_header_id|>assistant<|end_header_id|>\n\n"
    )

    assert prompt_style.messages_to_prompt(messages) == expected_prompt


def test_llama3_prompt_style_with_default_system():
    prompt_style = Llama3PromptStyle()
    messages = [
        ChatMessage(content="Hello!", role=MessageRole.USER),
    ]
    expected = (
        "<|start_header_id|>system<|end_header_id|>\n\n"
        f"{prompt_style.DEFAULT_SYSTEM_PROMPT}<|eot_id|>"
        "<|start_header_id|>user<|end_header_id|>\n\nHello!<|eot_id|>"
        "<|start_header_id|>assistant<|end_header_id|>\n\n"
    )
    assert prompt_style._messages_to_prompt(messages) == expected


def test_llama3_prompt_style_with_assistant_response():
    prompt_style = Llama3PromptStyle()
    messages = [
        ChatMessage(content="You are a helpful assistant", role=MessageRole.SYSTEM),
        ChatMessage(content="What is the capital of France?", role=MessageRole.USER),
        ChatMessage(
            content="The capital of France is Paris.", role=MessageRole.ASSISTANT
        ),
    ]

    expected_prompt = (
        "<|start_header_id|>system<|end_header_id|>\n\n"
        "You are a helpful assistant<|eot_id|>"
        "<|start_header_id|>user<|end_header_id|>\n\n"
        "What is the capital of France?<|eot_id|>"
        "<|start_header_id|>assistant<|end_header_id|>\n\n"
        "The capital of France is Paris.<|eot_id|>"
    )

    assert prompt_style.messages_to_prompt(messages) == expected_prompt
```

## File: `tests/fixtures/__init__.py`
```python
"""Global fixtures."""
```

## File: `tests/fixtures/auto_close_qdrant.py`
```python
import pytest

from private_gpt.components.vector_store.vector_store_component import (
    VectorStoreComponent,
)
from tests.fixtures.mock_injector import MockInjector


@pytest.fixture(autouse=True)
def _auto_close_vector_store_client(injector: MockInjector) -> None:
    """Auto close VectorStore client after each test.

    VectorStore client (qdrant/chromadb) opens a connection the
    Database that causes issues when running tests too fast,
    so close explicitly after each test.
    """
    yield
    injector.get(VectorStoreComponent).close()
```

## File: `tests/fixtures/fast_api_test_client.py`
```python
import pytest
from fastapi.testclient import TestClient

from private_gpt.launcher import create_app
from tests.fixtures.mock_injector import MockInjector


@pytest.fixture
def test_client(request: pytest.FixtureRequest, injector: MockInjector) -> TestClient:
    if request is not None and hasattr(request, "param"):
        injector.bind_settings(request.param or {})

    app_under_test = create_app(injector.test_injector)
    return TestClient(app_under_test)
```

## File: `tests/fixtures/ingest_helper.py`
```python
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from private_gpt.server.ingest.ingest_router import IngestResponse


class IngestHelper:
    def __init__(self, test_client: TestClient):
        self.test_client = test_client

    def ingest_file(self, path: Path) -> IngestResponse:
        files = {"file": (path.name, path.open("rb"))}

        response = self.test_client.post("/v1/ingest/file", files=files)
        assert response.status_code == 200
        ingest_result = IngestResponse.model_validate(response.json())
        return ingest_result


@pytest.fixture
def ingest_helper(test_client: TestClient) -> IngestHelper:
    return IngestHelper(test_client)
```

## File: `tests/fixtures/mock_injector.py`
```python
from collections.abc import Callable
from typing import Any
from unittest.mock import MagicMock

import pytest
from injector import Provider, ScopeDecorator, singleton

from private_gpt.di import create_application_injector
from private_gpt.settings.settings import Settings, unsafe_settings
from private_gpt.settings.settings_loader import merge_settings
from private_gpt.utils.typing import T


class MockInjector:
    def __init__(self) -> None:
        self.test_injector = create_application_injector()

    def bind_mock(
        self,
        interface: type[T],
        mock: (T | (Callable[..., T] | Provider[T])) | None = None,
        *,
        scope: ScopeDecorator = singleton,
    ) -> T:
        if mock is None:
            mock = MagicMock()
        self.test_injector.binder.bind(interface, to=mock, scope=scope)
        return mock  # type: ignore

    def bind_settings(self, settings: dict[str, Any]) -> Settings:
        merged = merge_settings([unsafe_settings, settings])
        new_settings = Settings(**merged)
        self.test_injector.binder.bind(Settings, new_settings)
        return new_settings

    def get(self, interface: type[T]) -> T:
        return self.test_injector.get(interface)


@pytest.fixture
def injector() -> MockInjector:
    return MockInjector()
```

## File: `tests/server/chat/test_chat_routes.py`
```python
from fastapi.testclient import TestClient

from private_gpt.open_ai.openai_models import OpenAICompletion, OpenAIMessage
from private_gpt.server.chat.chat_router import ChatBody


def test_chat_route_produces_a_stream(test_client: TestClient) -> None:
    body = ChatBody(
        messages=[OpenAIMessage(content="test", role="user")],
        use_context=False,
        stream=True,
    )
    response = test_client.post("/v1/chat/completions", json=body.model_dump())

    raw_events = response.text.split("\n\n")
    events = [
        item.removeprefix("data: ") for item in raw_events if item.startswith("data: ")
    ]
    assert response.status_code == 200
    assert "text/event-stream" in response.headers["content-type"]
    assert len(events) > 0
    assert events[-1] == "[DONE]"


def test_chat_route_produces_a_single_value(test_client: TestClient) -> None:
    body = ChatBody(
        messages=[OpenAIMessage(content="test", role="user")],
        use_context=False,
        stream=False,
    )
    response = test_client.post("/v1/chat/completions", json=body.model_dump())

    # No asserts, if it validates it's good
    OpenAICompletion.model_validate(response.json())
    assert response.status_code == 200
```

## File: `tests/server/chunks/chunk_test.txt`
```
e88c1005-637d-4cb4-ae79-9b8eb58cab97

b483dd15-78c4-4d67-b546-21a0d690bf43

a8080238-b294-4598-ac9c-7abf4c8e0552

14208dac-c600-4a18-872b-5e45354cfff2
```

## File: `tests/server/chunks/test_chunk_routes.py`
```python
from pathlib import Path

from fastapi.testclient import TestClient

from private_gpt.server.chunks.chunks_router import ChunksBody, ChunksResponse
from tests.fixtures.ingest_helper import IngestHelper


def test_chunks_retrieval(test_client: TestClient, ingest_helper: IngestHelper) -> None:
    # Make sure there is at least some chunk to query in the database
    path = Path(__file__).parents[0] / "chunk_test.txt"
    ingest_helper.ingest_file(path)

    body = ChunksBody(text="b483dd15-78c4-4d67-b546-21a0d690bf43")
    response = test_client.post("/v1/chunks", json=body.model_dump())
    assert response.status_code == 200
    chunk_response = ChunksResponse.model_validate(response.json())
    assert len(chunk_response.data) > 0
```

## File: `tests/server/embeddings/test_embedding_routes.py`
```python
from fastapi.testclient import TestClient

from private_gpt.server.embeddings.embeddings_router import (
    EmbeddingsBody,
    EmbeddingsResponse,
)


def test_embeddings_generation(test_client: TestClient) -> None:
    body = EmbeddingsBody(input="Embed me")
    response = test_client.post("/v1/embeddings", json=body.model_dump())

    assert response.status_code == 200
    embedding_response = EmbeddingsResponse.model_validate(response.json())
    assert len(embedding_response.data) > 0
    assert len(embedding_response.data[0].embedding) > 0
```

## File: `tests/server/ingest/test.txt`
```
Once upon a time, in a magical forest called Enchantia, lived a young and cheerful deer named Zumi. Zumi was no ordinary deer; she was bright-eyed, intelligent, and had a heart full of curiosity. One sunny morning, as the forest came alive with the sweet melodies of chirping birds and rustling leaves, Zumi eagerly pranced through the woods on her way to school.

Enchantia Forest School was a unique place, where all the woodland creatures gathered to learn and grow together. The school was nestled in a clearing surrounded by tall, ancient trees. Zumi loved the feeling of anticipation as she approached the school, her hooves barely touching the ground in excitement.

As she arrived at the school, her dear friend and classmate, Oliver the wise old owl, greeted her with a friendly hoot. "Good morning, Zumi! Are you ready for another day of adventure and learning?"

Zumi's eyes sparkled with enthusiasm as she nodded, "Absolutely, Oliver! I can't wait to see what we'll discover today."

In their classroom, Teacher Willow, a gentle and nurturing willow tree, welcomed the students. The classroom was adorned with vibrant leaves and twinkling fireflies, creating a magical and cozy atmosphere. Today's lesson was about the history of the forest and the importance of living harmoniously with nature.

The students listened attentively as Teacher Willow recounted stories of ancient times when the forest thrived in unity and peace. Zumi was particularly enthralled by the tales of forest guardians and how they protected the magical balance of Enchantia.

After the lesson, it was time for recess. Zumi joined her friends in a lively game of tag, where they darted and danced playfully among the trees. Zumi's speed and agility made her an excellent tagger, and laughter filled the air as they played.

Later, they gathered for an art class, where they expressed themselves through painting and sculpting with clay. Zumi chose to paint a mural of the forest, portraying the beauty and magic they were surrounded by every day.

As the day came to an end, the students sat in a circle to share stories and reflections. Zumi shared her excitement for the day and how she learned to appreciate the interconnectedness of all creatures in the forest.

As the sun set, casting a golden glow across the forest, Zumi made her way back home, her heart brimming with happiness and newfound knowledge. Each day at Enchantia Forest School was an adventure, and Zumi couldn't wait to learn more and grow with her friends, for the magic of learning was as boundless as the forest itself. And so, under the canopy of stars and the watchful eyes of the forest, Zumi drifted into dreams filled with wonder and anticipation for the adventures that awaited her on the morrow.
```

## File: `tests/server/ingest/test_ingest_routes.py`
```python
import tempfile
from pathlib import Path

from fastapi.testclient import TestClient

from private_gpt.server.ingest.ingest_router import IngestResponse
from tests.fixtures.ingest_helper import IngestHelper


def test_ingest_accepts_txt_files(ingest_helper: IngestHelper) -> None:
    path = Path(__file__).parents[0] / "test.txt"
    ingest_result = ingest_helper.ingest_file(path)
    assert len(ingest_result.data) == 1


def test_ingest_accepts_pdf_files(ingest_helper: IngestHelper) -> None:
    path = Path(__file__).parents[0] / "test.pdf"
    ingest_result = ingest_helper.ingest_file(path)
    assert len(ingest_result.data) == 1


def test_ingest_list_returns_something_after_ingestion(
    test_client: TestClient, ingest_helper: IngestHelper
) -> None:
    response_before = test_client.get("/v1/ingest/list")
    count_ingest_before = len(response_before.json()["data"])
    with tempfile.NamedTemporaryFile("w", suffix=".txt") as test_file:
        test_file.write("Foo bar; hello there!")
        test_file.flush()
        test_file.seek(0)
        ingest_result = ingest_helper.ingest_file(Path(test_file.name))
    assert len(ingest_result.data) == 1, "The temp doc should have been ingested"
    response_after = test_client.get("/v1/ingest/list")
    count_ingest_after = len(response_after.json()["data"])
    assert (
        count_ingest_after == count_ingest_before + 1
    ), "The temp doc should be returned"


def test_ingest_plain_text(test_client: TestClient) -> None:
    response = test_client.post(
        "/v1/ingest/text", json={"file_name": "file_name", "text": "text"}
    )
    assert response.status_code == 200
    ingest_result = IngestResponse.model_validate(response.json())
    assert len(ingest_result.data) == 1
```

## File: `tests/server/ingest/test_local_ingest.py`
```python
import os
import subprocess
from pathlib import Path

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def file_path() -> str:
    return "test.txt"


def create_test_file(file_path: str) -> None:
    with open(file_path, "w") as f:
        f.write("test")


def clear_log_file(log_file_path: str) -> None:
    if Path(log_file_path).exists():
        os.remove(log_file_path)


def read_log_file(log_file_path: str) -> str:
    with open(log_file_path) as f:
        return f.read()


def init_structure(folder: str, file_path: str) -> None:
    clear_log_file(file_path)
    os.makedirs(folder, exist_ok=True)
    create_test_file(f"{folder}/${file_path}")


def test_ingest_one_file_in_allowed_folder(
    file_path: str, test_client: TestClient
) -> None:
    allowed_folder = "local_data/tests/allowed_folder"
    init_structure(allowed_folder, file_path)

    test_env = os.environ.copy()
    test_env["PGPT_PROFILES"] = "test"
    test_env["LOCAL_INGESTION_ENABLED"] = "True"

    result = subprocess.run(
        ["python", "scripts/ingest_folder.py", allowed_folder],
        capture_output=True,
        text=True,
        env=test_env,
    )

    assert result.returncode == 0, f"Script failed with error: {result.stderr}"
    response_after = test_client.get("/v1/ingest/list")

    count_ingest_after = len(response_after.json()["data"])
    assert count_ingest_after > 0, "No documents were ingested"


def test_ingest_disabled(file_path: str) -> None:
    allowed_folder = "local_data/tests/allowed_folder"
    init_structure(allowed_folder, file_path)

    test_env = os.environ.copy()
    test_env["PGPT_PROFILES"] = "test"
    test_env["LOCAL_INGESTION_ENABLED"] = "False"

    result = subprocess.run(
        ["python", "scripts/ingest_folder.py", allowed_folder],
        capture_output=True,
        text=True,
        env=test_env,
    )

    assert result.returncode != 0, f"Script failed with error: {result.stderr}"
```

## File: `tests/server/recipes/test_summarize_router.py`
```python
from fastapi.testclient import TestClient

from private_gpt.server.recipes.summarize.summarize_router import (
    SummarizeBody,
    SummarizeResponse,
)


def test_summarize_route_produces_a_stream(test_client: TestClient) -> None:
    body = SummarizeBody(
        text="Test",
        stream=True,
    )
    response = test_client.post("/v1/summarize", json=body.model_dump())

    raw_events = response.text.split("\n\n")
    events = [
        item.removeprefix("data: ") for item in raw_events if item.startswith("data: ")
    ]
    assert response.status_code == 200
    assert "text/event-stream" in response.headers["content-type"]
    assert len(events) > 0
    assert events[-1] == "[DONE]"


def test_summarize_route_produces_a_single_value(test_client: TestClient) -> None:
    body = SummarizeBody(
        text="test",
        stream=False,
    )
    response = test_client.post("/v1/summarize", json=body.model_dump())

    # No asserts, if it validates it's good
    SummarizeResponse.model_validate(response.json())
    assert response.status_code == 200


def test_summarize_with_document_context(test_client: TestClient) -> None:
    # Ingest an document
    ingest_response = test_client.post(
        "/v1/ingest/text",
        json={
            "file_name": "file_name",
            "text": "Lorem ipsum dolor sit amet",
        },
    )
    assert ingest_response.status_code == 200
    ingested_docs = ingest_response.json()["data"]
    assert len(ingested_docs) == 1

    body = SummarizeBody(
        use_context=True,
        context_filter={"docs_ids": [doc["doc_id"] for doc in ingested_docs]},
        stream=False,
    )
    response = test_client.post("/v1/summarize", json=body.model_dump())

    completion: SummarizeResponse = SummarizeResponse.model_validate(response.json())
    assert response.status_code == 200
    # We can check the content of the completion, because mock LLM used in tests
    # always echoes the prompt. In the case of summary, the input context is passed.
    assert completion.summary.find("Lorem ipsum dolor sit amet") != -1


def test_summarize_with_non_existent_document_context_not_fails(
    test_client: TestClient,
) -> None:
    body = SummarizeBody(
        use_context=True,
        context_filter={
            "docs_ids": ["non-existent-doc-id"],
        },
        stream=False,
    )

    response = test_client.post("/v1/summarize", json=body.model_dump())

    completion: SummarizeResponse = SummarizeResponse.model_validate(response.json())
    assert response.status_code == 200
    # We can check the content of the completion, because mock LLM used in tests
    # always echoes the prompt. In the case of summary, the input context is passed.
    assert completion.summary.find("Empty Response") != -1


def test_summarize_with_metadata_and_document_context(test_client: TestClient) -> None:
    docs = []

    # Ingest a first document
    document_1_content = "Content of document 1"
    ingest_response = test_client.post(
        "/v1/ingest/text",
        json={
            "file_name": "file_name_1",
            "text": document_1_content,
        },
    )
    assert ingest_response.status_code == 200
    ingested_docs = ingest_response.json()["data"]
    assert len(ingested_docs) == 1
    docs += ingested_docs

    # Ingest a second document
    document_2_content = "Text of document 2"
    ingest_response = test_client.post(
        "/v1/ingest/text",
        json={
            "file_name": "file_name_2",
            "text": document_2_content,
        },
    )
    assert ingest_response.status_code == 200
    ingested_docs = ingest_response.json()["data"]
    assert len(ingested_docs) == 1
    docs += ingested_docs

    # Completions with the first document's id and the second document's metadata
    body = SummarizeBody(
        use_context=True,
        context_filter={"docs_ids": [doc["doc_id"] for doc in docs]},
        stream=False,
    )
    response = test_client.post("/v1/summarize", json=body.model_dump())

    completion: SummarizeResponse = SummarizeResponse.model_validate(response.json())
    assert response.status_code == 200
    # Assert both documents are part of the used sources
    # We can check the content of the completion, because mock LLM used in tests
    # always echoes the prompt. In the case of summary, the input context is passed.
    assert completion.summary.find(document_1_content) != -1
    assert completion.summary.find(document_2_content) != -1


def test_summarize_with_prompt(test_client: TestClient) -> None:
    ingest_response = test_client.post(
        "/v1/ingest/text",
        json={
            "file_name": "file_name",
            "text": "Lorem ipsum dolor sit amet",
        },
    )
    assert ingest_response.status_code == 200
    ingested_docs = ingest_response.json()["data"]
    assert len(ingested_docs) == 1

    body = SummarizeBody(
        use_context=True,
        context_filter={
            "docs_ids": [doc["doc_id"] for doc in ingested_docs],
        },
        prompt="This is a custom summary prompt, 54321",
        stream=False,
    )
    response = test_client.post("/v1/summarize", json=body.model_dump())

    completion: SummarizeResponse = SummarizeResponse.model_validate(response.json())
    assert response.status_code == 200
    # We can check the content of the completion, because mock LLM used in tests
    # always echoes the prompt. In the case of summary, the input context is passed.
    assert completion.summary.find("This is a custom summary prompt, 54321") != -1
```

## File: `tests/server/utils/test_auth.py`
```python
from fastapi.testclient import TestClient


def test_default_does_not_require_auth(test_client: TestClient) -> None:
    response_before = test_client.get("/v1/ingest/list")
    assert response_before.status_code == 200
```

## File: `tests/server/utils/test_simple_auth.py`
```python
"""Tests to validate that the simple authentication mechanism is working.

NOTE: We are not testing the switch based on the config in
      `private_gpt.server.utils.auth`. This is not done because of the way the code
      is currently architecture (it is hard to patch the `settings` and the app while
      the tests are directly importing them).
"""

from typing import Annotated

import pytest
from fastapi import Depends
from fastapi.testclient import TestClient

from private_gpt.server.utils.auth import (
    NOT_AUTHENTICATED,
    _simple_authentication,
    authenticated,
)
from private_gpt.settings.settings import settings


def _copy_simple_authenticated(
    _simple_authentication: Annotated[bool, Depends(_simple_authentication)]
) -> bool:
    """Check if the request is authenticated."""
    if not _simple_authentication:
        raise NOT_AUTHENTICATED
    return True


@pytest.fixture(autouse=True)
def _patch_authenticated_dependency(test_client: TestClient):
    # Patch the server to use simple authentication

    test_client.app.dependency_overrides[authenticated] = _copy_simple_authenticated

    # Call the actual test
    yield

    # Remove the patch for other tests
    test_client.app.dependency_overrides = {}


def test_default_auth_working_when_enabled_401(test_client: TestClient) -> None:
    response = test_client.get("/v1/ingest/list")
    assert response.status_code == 401


def test_default_auth_working_when_enabled_200(test_client: TestClient) -> None:
    response_fail = test_client.get("/v1/ingest/list")
    assert response_fail.status_code == 401

    response_success = test_client.get(
        "/v1/ingest/list", headers={"Authorization": settings().server.auth.secret}
    )
    assert response_success.status_code == 200
```

## File: `tests/settings/test_settings.py`
```python
from private_gpt.settings.settings import Settings, settings
from tests.fixtures.mock_injector import MockInjector


def test_settings_are_loaded_and_merged() -> None:
    assert settings().server.env_name == "test"


def test_settings_can_be_overriden(injector: MockInjector) -> None:
    injector.bind_settings({"server": {"env_name": "overriden"}})
    mocked_settings = injector.get(Settings)
    assert mocked_settings.server.env_name == "overriden"
```

## File: `tests/settings/test_settings_loader.py`
```python
import io
import os

import pytest

from private_gpt.settings.yaml import load_yaml_with_envvars


def test_environment_variables_are_loaded() -> None:
    sample_yaml = """
    replaced: ${TEST_REPLACE_ME}
    """
    env = {"TEST_REPLACE_ME": "replaced"}
    loaded = load_yaml_with_envvars(io.StringIO(sample_yaml), env)
    os.environ.copy()
    assert loaded["replaced"] == "replaced"


def test_environment_defaults_variables_are_loaded() -> None:
    sample_yaml = """
    replaced: ${PGPT_EMBEDDING_HF_MODEL_NAME:BAAI/bge-small-en-v1.5}
    """
    loaded = load_yaml_with_envvars(io.StringIO(sample_yaml), {})
    assert loaded["replaced"] == "BAAI/bge-small-en-v1.5"


def test_environment_defaults_variables_are_loaded_with_duplicated_delimiters() -> None:
    sample_yaml = """
    replaced: ${PGPT_EMBEDDING_HF_MODEL_NAME::duped::}
    """
    loaded = load_yaml_with_envvars(io.StringIO(sample_yaml), {})
    assert loaded["replaced"] == ":duped::"


def test_environment_without_defaults_fails() -> None:
    sample_yaml = """
    replaced: ${TEST_REPLACE_ME}
    """
    with pytest.raises(ValueError) as error:
        load_yaml_with_envvars(io.StringIO(sample_yaml), {})
    assert error is not None
```

## File: `tests/ui/test_ui.py`
```python
import pytest
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    "test_client", [{"ui": {"enabled": True, "path": "/ui"}}], indirect=True
)
def test_ui_starts_in_the_given_endpoint(test_client: TestClient) -> None:
    response = test_client.get("/ui")
    assert response.status_code == 200
```

## File: `tiktoken_cache/.gitignore`
```
*
!.gitignore
```

