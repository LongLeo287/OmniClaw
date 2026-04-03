---
id: fujiwarachoki-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:25.739774
---

# KNOWLEDGE EXTRACT: FujiwaraChoki
> **Extracted on:** 2026-03-30 17:37:23
> **Source:** FujiwaraChoki

---

## File: `MoneyPrinter.md`
```markdown
# 📦 FujiwaraChoki/MoneyPrinter [🔖 PENDING/APPROVE]
🔗 https://github.com/FujiwaraChoki/MoneyPrinter


## Meta
- **Stars:** ⭐ 12948 | **Forks:** 🍴 1670
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Automate Creation of YouTube Shorts using MoviePy.

## README (trích đầu)
```
# MoneyPrinter 💸

> ♥︎ Sponsor: The Best AI Chat App: [shiori.ai](https://www.shiori.ai)
---

> 𝕏 Also, follow me on X: [@DevBySami](https://x.com/DevBySami).

Automate the creation of YouTube Shorts by providing a video topic.

MoneyPrinter is Ollama-first: script generation and metadata are fully powered by local Ollama models.

MoneyPrinter now uses a DB-backed generation queue (API + worker + Postgres in Docker) for reliable, restart-safe processing.

<a href="https://trendshift.io/repositories/7545" target="_blank"><img src="https://trendshift.io/api/badge/repositories/7545" alt="FujiwaraChoki%2FMoneyPrinter | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

> **Important** Please make sure you look through existing/closed issues before opening your own. If it's just a question, please join our [discord](https://dsc.gg/fuji-community) and ask there.

> **🎥** Watch the video on [YouTube](https://youtu.be/mkZsaDA2JnA?si=pNne3MnluRVkWQbE).

## Documentation

Docs are centralized in [`brain/knowledge/docs_legacy/`](../../../README.md):

- [Interactive Setup Script](setup.sh)
- [Quickstart](QUICKSTART.md)
- [Configuration](configuration.md)
- [Architecture](ARCHITECTURE.md)
- [Docker](../../../core/security/QUARANTINE/incoming/repos/AutoGPT/docs/content/classic/setup/docker.md)
- [Testing](../bmad_repo/testing.md)
- [Troubleshooting](troubleshooting.md)

## FAQ 🤔

### Which AI provider does MoneyPrinter use?

MoneyPrinter is fully Ollama-based. Start Ollama, pull a model, and select the model in the UI.

```bash
ollama serve
ollama pull llama3.1:8b
```

### How do I get the TikTok session ID?

You can obtain your TikTok session ID by logging into TikTok in your browser and copying the value of the `sessionid` cookie.

### My ImageMagick binary is not being detected

MoneyPrinter auto-detects ImageMagick from your `PATH` on Linux, macOS, and Windows. If auto-detection fails, set the executable path manually in `.env`, for example:

```env
IMAGEMAGICK_BINARY="C:\\Program Files\\ImageMagick-7.1.0-Q16\\magick.exe"
```

Don't forget to use double backslashes (`\\`) in the path, instead of one.

### I can't install `playsound`: Wheel failed to build

If you're having trouble installing `playsound`, you can try installing it using the following command:

```bash
uv pip install -U wheel
uv pip install -U playsound
```

If you were not able to find your solution, check [Troubleshooting](troubleshooting.md), ask in Discord, or create an issue.

## Donate 🎁

If you like and enjoy `MoneyPrinter`, and would like to donate, you can do that by clicking on the button on the right hand side of the repository. ❤️
You will have your name (and/or logo) added to this repository as a supporter as a sign of appreciation.

## Contributing 🤝

Pull Requests will not be accepted for the time-being.

## Star History 🌟

[![Star History Chart](https://api.star-history.com/svg?repos=FujiwaraChoki/MoneyPrinter&type=Date)](https://star-history.com/#FujiwaraChoki/MoneyPrinter&Date)

## License 📝

See [`LICENSE`](LICENSE) file for more in
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `MoneyPrinterV2.md`
```markdown
# 📦 FujiwaraChoki/MoneyPrinterV2 [🔖 PENDING/APPROVE]
🔗 https://github.com/FujiwaraChoki/MoneyPrinterV2


## Meta
- **Stars:** ⭐ 26098 | **Forks:** 🍴 2711
- **Language:** Python | **License:** AGPL-3.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Automate the process of making money online.

## README (trích đầu)
```
# MoneyPrinter V2
 
> ♥︎ **Sponsor**: The Best AI Chat App: [shiori.ai](https://www.shiori.ai). Use code **MPV2** for 20% off.

---

> 𝕏 Also, follow me on X: [@DevBySami](https://x.com/DevBySami).

[![madewithlove](https://img.shields.io/badge/made_with-%E2%9D%A4-red?style=for-the-badge&labelColor=orange)](https://github.com/FujiwaraChoki/MoneyPrinterV2)

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-brightgreen?logo=buymeacoffee)](https://www.buymeacoffee.com/fujicodes)
[![GitHub license](https://img.shields.io/github/license/FujiwaraChoki/MoneyPrinterV2?style=for-the-badge)](https://github.com/FujiwaraChoki/MoneyPrinterV2/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/FujiwaraChoki/MoneyPrinterV2?style=for-the-badge)](https://github.com/FujiwaraChoki/MoneyPrinterV2/issues)
[![GitHub stars](https://img.shields.io/github/stars/FujiwaraChoki/MoneyPrinterV2?style=for-the-badge)](https://github.com/FujiwaraChoki/MoneyPrinterV2/stargazers)
[![Discord](https://img.shields.io/discord/1134848537704804432?style=for-the-badge)](https://dsc.gg/fuji-community)

An Application that automates the process of making money online.
MPV2 (MoneyPrinter Version 2) is, as the name suggests, the second version of the MoneyPrinter project. It is a complete rewrite of the original project, with a focus on a wider range of features and a more modular architecture.

> **Note:** MPV2 needs Python 3.12 to function effectively.
> Watch the YouTube video [here](https://youtu.be/wAZ_ZSuIqfk)

## Features

- [x] Twitter Bot (with CRON Jobs => `scheduler`)
- [x] YouTube Shorts Automater (with CRON Jobs => `scheduler`)
- [x] Affiliate Marketing (Amazon + Twitter)
- [x] Find local businesses & cold outreach

## Versions

MoneyPrinter has different versions for multiple languages developed by the community for the community. Here are some known versions:

- Chinese: [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)

If you would like to submit your own version/fork of MoneyPrinter, please open an issue describing the changes you made to the fork.

## Installation

> ⚠️ If you are planning to reach out to scraped businesses per E-Mail, please first install the [Go Programming Language](https://golang.org/).

```bash
git clone https://github.com/FujiwaraChoki/MoneyPrinterV2.git

cd MoneyPrinterV2
# Copy Example Configuration and fill out values in config.json
cp config.example.json config.json

# Create a virtual environment
python -m venv venv

# Activate the virtual environment - Windows
.\venv\Scripts\activate

# Activate the virtual environment - Unix
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt
```

## Usage

```bash
# Run the application
python src/main.py
```

## Documentation

All relevant document can be found [here](brain/knowledge/docs_legacy/).

## Scripts

For easier usage, there are some scripts in the `scripts` directory, that can be used to directly access the core functiona
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

