---
id: datanath-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:16.572648
---

# KNOWLEDGE EXTRACT: DataNath
> **Extracted on:** 2026-03-30 17:35:45
> **Source:** DataNath

---

## File: `notebooklm_source_automation.md`
```markdown
# 📦 DataNath/notebooklm_source_automation [🔖 PENDING/APPROVE]
🔗 https://github.com/DataNath/notebooklm_source_automation


## Meta
- **Stars:** ⭐ 51 | **Forks:** 🍴 11
- **Language:** Python | **License:** NOASSERTION
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Automating browser interactions with Playwright to systematically add website sources to Google's NotebookLM.

## README (trích đầu)
```
<h1>NotebookLM source automation</h1>
<a id="readme-top"></a>

Produced by Nathan Purvis - [Databasyx](https://www.databasyx.com/) co-founder | Data Engineer @ [The Information Lab](https://www.theinformationlab.co.uk/)

<h2>Contact</h2>

[GitHub](https://github.com/DataNath) | [LinkedIn](https://www.linkedin.com/in/nathan-purvis/) | [Twitter](https://x.com/DataNath) | [Alteryx Community](https://community.alteryx.com/t5/user/viewprofilepage/user-id/307299)  
Email: Nathan@databasyx.com

<h2>The problem</h2>

Google's [NotebookLM](https://notebooklm.google.com/) is a tool - powered by Google Gemini - that allows us to quickly generate resources like study guides, briefing documents and audio overviews. To create these assets, we need to make a new notebook and provide sources that the model can then pull from. These sources can be:

- File uploads (PDF, .txt, markdown & audio i.e. mp3)
- Google drive: Docs or Slides
- Links: Website or YouTube
- Paste text: Manually paste in text like meeting notes

However, as pointed out by colleagues and in various Reddit posts, the process for adding link-based sources is incredibly cumbersome; users need to continuously:

- Press 'Add source'
- Select 'Website' or 'YouTube'
- Paste the source URL
- Hit enter/press 'Insert'

This might be fine for a handful of sources but, given you can create notebooks of up to 300 sources, this is less than ideal when scaled.

<h2>The solution</h2>

Given we have a repeated pattern of behaviour in terms of how sources are added, this process is a perfect candidate for browser automation, and that's exactly what is used here. Using [Playwright](https://playwright.dev/python/) - a library created specifically for end-to-end testing and general browser automation tooling - we can easily loop through the steps outlined above to create a new notebook populated with your desired sources.

<h2>How do I use this?</h2>

Follow the steps below to use this yourself!

<h3>1. Clone this repository</h3>

```shell
git clone https://github.com/DataNath/notebooklm_source_automation.git
```

If you're in Documents for example, this will create a new subdirectory here with the project's contents.

<h3>2. Move into the new directory</h3>

```shell
cd notebooklm_source_automation
```

<h3>3. Create a virtual environment (optional)</h3>

```shell
python -m venv .venv
```

This step isn't strictly necessary but is good practice for isolation and keeping projects lean in terms of packages and so on.

<h3>4. Activate your virtual environment</h3>

For Windows users:

```shell
.venv\scripts\activate
```

For Mac users:

```shell
source .venv/bin/activate
```

Again, this isn't strictly necessary i.e. if you're not using a venv as outlined in the step above.

<h3>5. Install required packages</h3>

```shell
pip install -r requirements.txt
```

This will install Playwright and its transitive dependencies.

<h3>6. Install Chromium browser</h3>

```shell
playwright install chromium
```

This installs the
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

