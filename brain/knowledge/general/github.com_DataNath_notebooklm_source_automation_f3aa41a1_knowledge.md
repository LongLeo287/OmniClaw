---
id: github.com-datanath-notebooklm-source-automation-f
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:43.261478
---

# KNOWLEDGE EXTRACT: github.com_DataNath_notebooklm_source_automation_f3aa41a1
> **Extracted on:** 2026-04-01 12:28:37
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521844/github.com_DataNath_notebooklm_source_automation_f3aa41a1

---

## File: `.gitignore`
```
.venv/
state.json
test*
__pycache__/
```

## File: `LICENSE.md`
```markdown
Copyright Nathan Purvis 2025

Permission is hereby granted to any person obtaining a copy of this software and associated documentation files (the "Software"), to use, copy, and modify the Software for **personal and non-commercial purposes only**, subject to the following conditions:

- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**Commercial use (including use in paid products, services, or anything generating revenue) is not permitted without prior written permission and a commercial license.**

For commercial use, please contact nathan@databasyx.com.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
```

## File: `main.py`
```python
from playwright.sync_api import sync_playwright, expect
from functions import add_link_sources, create_source_list
from pathlib import Path as p
import time, sys

source_type_raw = input("Enter a source type (Website or YouTube): ")
source_type = source_type_raw.strip().lower()

notebook_name = input("Set a name for your new notebook: ")

start = time.time()

method_dict = {
    "website": add_link_sources,
    "youtube": add_link_sources
}

method = method_dict.get(source_type)

try:
    if not method:
        print(f"{source_type_raw} is not a supported source type!")
        sys.exit()

    urls = create_source_list(source_type)
    
except ValueError as e:
    print(e)
    sys.exit()

# Initialise browser session

with sync_playwright() as sp:
    login_state_path = p(__file__).parent / "state.json"

    browser = sp.chromium.launch(headless=True, channel="chrome")
    context = browser.new_context(storage_state=str(login_state_path))
    page = context.new_page()

    page.goto("https://notebooklm.google.com/")
    page.wait_for_load_state()

    method(source_type, urls, page)

    print("\nFinished adding sources.\n")

    title_box = page.locator(".title-input")
    title_box.click()
    page.keyboard.press("Control+A")
    title_box.fill(notebook_name)
    title_box.press("Enter")

    page.wait_for_timeout(1000)

    print("Title updated!\n")

    browser.close()

end = time.time()

elapsed = round(end - start)

if elapsed > 59:
    minutes = elapsed // 60
    seconds = elapsed % 60
    print(f"Time elapsed: {minutes} minutes and {seconds} seconds.")
else:
    print(f"Time elapsed: {elapsed} seconds.")
```

## File: `readme.md`
```markdown
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

This installs the [Chromium](https://www.chromium.org/Home/) browser that this project runs on.

<h3>7. Provide your source links</h3>

The project is set up to read a list of up to 300 (NotebookLM's limit) link-based sources from the relevant file within `/sources`. By cloning this repository these will already exist as empty files (other than a header) for you to populate.

>[!WARNING]
>If you create your own file(s) and overwrite the existing, make sure the schema is identical i.e. a single field with a maximum of 300 source rows starting on the second row.

<h3>8. Set your Google login state</h3>

```shell
python set_login_state.py
```

A browser will launch and prompt you to login to Google. Once complete, hit ENTER - the script will terminate and you should see a `state.json` file appear in your directory. This is used to persist authentication and browser session data, saving you from having to log in before every run. Don't worry, this is already in `.gitignore`!

>[!NOTE]
>I haven't tested/checked exact persistence but, for context, only had to re-run the login script once whilst developing the initial release.

<h3>9. Run!</h3>

```shell
python main.py
```

This will prompt you to provide two things in the terminal:

- A source type (currently only 'Website' or 'YouTube')
- A name for the new notebook

<h2>Feedback and/or issues</h2>

Please feel free to leave any feeback or suggestions for improvement. If you spot any issues, let me know and I'll endeavour to address them as soon as I can!

<p align="right">(<a href="#readme-top">Back to top</a>)</p>
```

## File: `set_login_state.py`
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        channel="chrome",
        args=["--disable-blink-features=AutomationControlled"],
    )
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://notebooklm.google.com/")

    input("Log in manually and press ENTER when done...")

    storage = context.storage_state(path="state.json")

    print("Login state saved!")

    browser.close()
```

## File: `functions/__init__.py`
```python
from .links import add_link_sources
from .file_handler import create_source_list
```

## File: `functions/file_handler.py`
```python
from pathlib import Path as p
import sys, os

def create_source_list(source_type) -> list:

    root_directory = p(__file__).parents[1]

    file_name = root_directory / "sources" / f"{source_type}_links.csv"

    if not file_name.exists():
        raise ValueError(
            f"{source_type}_links.csv doesn't exist or is in the wrong location."
        )

    urls = []

    with open(str(file_name), mode="r", encoding="utf-8", newline="") as contents:
        next(contents)

        blank_lines = 0
        for i in contents:

            link = i.strip()
            if link:
                urls.append(link)
            else:
                blank_lines += 1

        if len(urls) == 0:
            raise ValueError(f"Error: {source_type}_links.csv does not contain any records.")

        if blank_lines > 0:
            print(f"\nNote: {blank_lines} empty records from your {source_type}_csv file skipped.")

    return urls

if __name__ == "__main__":
    create_source_list("website")
```

## File: `functions/links.py`
```python
from playwright.sync_api import sync_playwright, expect
from .file_handler import create_source_list
import re

# Create a list of urls, taken from links.csv

def add_link_sources(source_type: str, urls: list, page) -> None:

    url_count = len(urls)
    is_first = 0
    is_last = url_count - 1

    print(f"\nAttempting to add {url_count} sources from provided {source_type}_links.csv file...\n")

    page.goto("https://notebooklm.google.com/")

    for i, u in enumerate(urls):

        if i == is_first:

            new_notebook_button = page.get_by_role("button", name="Create new notebook")
            new_notebook_button.wait_for(state="attached")
            new_notebook_button.click()

        link_button = page.locator(
            "span.mdc-evolution-chip__text-label", has_text=re.compile(f"{source_type}",re.I)
        )
        link_button.wait_for(state="attached")
        link_button.click()

        link_url_input = page.locator("[formcontrolname='newUrl']")
        link_url_input.wait_for(state="attached")
        link_url_input.fill(u)

        insert_button = page.get_by_role("button", name="Insert")
        expect(insert_button).to_be_enabled()
        insert_button.click()
        # page.keyboard.press("Enter")

        source_container = page.locator("div.single-source-container").last
        source_container.wait_for(state="attached")

        loading_spinner = source_container.locator(".mat-mdc-progress-spinner")
        loading_spinner.wait_for(state="detached")

        checkbox = source_container.locator(
            "input.mdc-checkbox__native-control.mdc-checkbox--selected"
        )
        checkbox.wait_for(state="attached")
        expect(checkbox).not_to_have_attribute("ariaLabel", u)

        page.wait_for_timeout(1200)

        if i < is_last:

            add_source_button = page.get_by_role("button", name="Add source")
            add_source_button.wait_for(state="attached")
            add_source_button.click()

        print(f"Source {i+1}/{url_count} ({u}) added.")

if __name__ == "__main__":
    print("This script requires the page object from main. It can't be ran in isolation.")
```

## File: `sources/website_links.csv`
```
url
```

## File: `sources/youtube_links.csv`
```
url
```

