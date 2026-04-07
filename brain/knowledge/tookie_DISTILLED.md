---
id: tookie
type: knowledge
owner: OA_Triage
---
# tookie
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
![Tookie-osint-logo-newtext-480x480](https://github.com/Alfredredbird/tookie-osint/assets/105014217/67bab5b4-f537-4f05-8a7b-c9fc3a16d256)



![GitHub contributors](https://img.shields.io/github/contributors/alfredredbird/tookie-osint)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/alfredredbird/tookie-osint)
![GitHub forks](https://img.shields.io/github/forks/alfredredbird/tookie-osint?logoColor=ffff&color=%23ff0000)
![GitHub Repo stars](https://img.shields.io/github/stars/alfredredbird/tookie-osint?color=%2332cd32)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# (Tookie-OSINT V4 is here!)
Tookie-OSINT has been re-written 100% from scratch for ultimate performance!
Translations are still not ready yet.
The wiki and readme are going through some changes. 

## 🌐 Language

> Select your language / 言語を選択してください / 选择你的语言 / Sélectionnez votre langue / Seleccione su idioma / Wählen Sie Ihre Sprache / Выберите язык / اختر لغتك / زبان خود را انتخاب کنید / Selecione seu idioma / Scegli la tua lingua / 선택 언어 / Pilih bahasa Anda / בחר את השפה שלך / अपनी भाषा चुनें / Valitse kieli / 選擇您的語言

| [English](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.en.md) | [日本語](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.ja.md) | [简体中文](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.zh-cn.md) | [繁體中文](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.zh-tw.md) | [Français](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.fr.md) | [Español](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.es.md) | [Deutsch](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.de.md) | [Русский](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.ru.md) | [Português](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.pt.md) | [Italiano](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.it.md) | [فارسی](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.fa.md) | [العربية](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.ar.md) | [हिन्दी](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.hi.md) | [Suomi](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.fi.md) | [עברית](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.he.md) |
| [Bahasa Indonesia](https://github.com/Alfredredbird/tookie-osint/blob/main/docs/readmelang/README.id.md) |

<!--
デバッグ用: 言語切り替えテーブルが正しく表示されているか確認してください。
If you find any issues with the language links, please open an issue or PR.
-->

# 🔎 Overview
Tookie-osint has a simple-to-use UI and is really straightforward.
The main idea of Tookie-osint is to discover usernames that are requested from an input.
Tookie-osint is similar to the tool called Sherlock. It discovers all the user accounts across different websites and Tookie-osint is successful at this task almost 80% of the time.
Our tool was created by me and the community and is available for your use.
I do not take responsibility for any malicious actions and/or responsibility caused by my tool. :(
Please note that Tookie-osint was created to help new programmers or pentesters get into the world of OSINT. My end term goal is to make Tookie-osint as perfect as I can and make it easy for new programmers to understand. Also take note that Tookie-osint is optimized for Python 3.12. If you want to contribute, make a fork and make a pull request to submit your changes. :D
<img width="769" height="1032" alt="image" src="https://github.com/user-attachments/assets/de7a5e05-d632-4199-9857-d1ca9000e8f2" />





# 📦 Linux Installation
The requirements will be automatically installed.

    git clone https://github.com/alfredredbird/tookie-osint.git
    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh

# 📦 Manual Install
    download the latest release from: https://github.com/alfredredbird/tookie-osint/releases.
    then extract the zip or tar.gz

    cd tookie-osint
    chmod +x install.sh
    sudo ./install.sh
    tookie-osint


# 📦 Other Installations
You can find more install instructions on the Wiki.

    git clone https://github.com/alfredredbird/tookie-osint
    cd tookie-osint
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 brib.py


# 💻 Tested OS

<table>
    <tr>
        <th>Operative system</th>
        <th> Version </th>
    </tr>
    <tr>
        <td>MacOS</td>
        <td> Monterey 12.6.7 </td>
    </tr>
    <tr>
        <td>Windows</td>
        <td>11/10</td>
    </tr>
 <tr>
        <td>Termux</td>
        <td>0.118.0</td>
    </tr>
    <tr>
        <td>Kali linux</td>
        <td> Rolling / Sana</td>
    </tr>
    <tr>
        <td>Parrot OS</td>
        <td>3.1 </td>
    </tr>
    <tr>
        <td>Ubuntu</td>
        <td>22.04/20.04 </td>
    </tr>
    <tr>
        <td>Debian</td>
        <td>10.00 </td>
    </tr>
   <tr>
        <td>Alpine</td>
        <td>3.10 </td>
    </tr>
  <tr>
        <td>Fedora</td>
        <td>v33</td>
    </tr>
  <tr>
        <td>Arch Linux</td>
        <td>2021.07.01</td>
    </tr>
  <tr>
        <td>Manjaro</td>
        <td>21</td>
    </tr>
   <tr>
        <td>Void</td>
        <td>Rolling Release</td>
    </tr>
</table>

# 📖 Requirements

There Is A Lot Lol

- colorama 
- requests
- argparse
- selenium 
- webdriver-manager 

# 🗣️Supported Languages
(we need translators 😭)
(The following languages are ready but not implemented.)
- [x] English
- [ ] Italian
- [ ] Hebrew
- [ ] Spanish
- [ ] French
- [ ] Arabic
- [ ] German
- [ ] Hindi
- [ ] Russian
- [ ] Portuguese
- [ ] Indonesian
- [ ] Finnish
- [ ] Chinese traditional
- [ ] Chinese Simplified
- [ ] Japanese
- [ ] Farsi
- [ ] Turkish

# 📕 Upcoming Features
 (They Are Great First Issues :D)
- [ ] Tor Searching (planned)
- [ ] WebUi (planned)
- [X] Webscraper
- [ ] Phone Number OSINT
- [ ] Custom Plugins
- [ ] Detailed Reports (in beta)
- [ ] Email OSINT (in beta)
- [x] CSV
- [ ] Url Brute Forcing
- [ ] GUI
- [X] More Accurate Results
- [ ] Auto Open Discovered URLs
- [ ] Web Hooks
- [x] Headless mode
- [x] Automation
- [X] Threading

# 🍿 Showcase
Tookie-osint has a wide variety of options to use.
Using `-h` shows the help menu.

<img width="769" height="1032" alt="image" src="https://github.com/user-attachments/assets/9ed8b048-42b0-49e8-86ef-923e6a6d5851" />


# ⁉️ Need Help?
Check out https://github.com/alfredredbird/tookie-osint/issues or the WiKi for help.
Still Need Help? Contact And Discord Server Below :D

# 🤔 Cant Find The WebSite Your Looking For?
Make a pull request or a bug report with the site and we will add it. :D

# 📗 Info:

<table>
    <tr>
        <th>Wiki</th>
        <th>https://github.com/alfredredbird/tookie-osint/wiki</th>
    </tr>
   <tr>
        <th>Releases</th>
        <th>https://github.com/alfredredbird/tookie-osint/releases</th>
    </tr>
    <tr>
        <th>Contributors</th>
        <th>https://github.com/alfredredbird/tookie-osint/graphs/contributors</th>
    </tr>
</table>

# 📙 Articles
There has been several articles written about our tool. Feal free to check them out :D  Theses articles belong to their respectful owners.
<table>
    <tr>
        <th>Habr</th>
        <th>https://habr.com/ru/news/757502/</th>
    </tr>
 <tr>
        <th>Habr</th>
        <th>https://habr.com/ru/amp/publications/769690/</th></th>
    </tr>

   <tr>
        <th>Speka Media</th>
        <th>https://speka.media/rozrobniki-predstavili-alfred-vidkritu-utilitu-dlya-osint-pygwkp</th>
    </tr>
    <tr>
        <th>Sibnet</th>
        <th>https://info.sibnet.ru/article/646445/</th>
    </tr>
    <tr>
        <th>NetRunner</th>
        <th>https://blog.netrunner.lol/alfred-advanced-osint-info-gathering-tool-afc1a7afd8a3</th>
    </tr>

   <tr>
        <th>gebutcher</th>
        <th>https://gebutcher.blogspot.com/2023/10/Osintalfred.html?m=1</th>
    </tr>
     <tr>
        <th>Iguru</th>
        <th>https://iguru.gr/alfred-ena-proigmeno-osint-programma/</th>
    </tr>
    <tr>
        <th>Medevel</th>
        <th>https://medevel.com/31-osint-tools/</th>
    </tr>
    <tr>
        <th>Medium</th>
        <th>https://medium.com/age-of-awareness/osint-unleashed-the-5-best-tools-for-cyber-investigators-8ff08fe9a4ba</th>
    </tr>
     <tr>
        <th>TechnoNews</th>
        <th>https://techno-news.net/2023/08/28/news_7132/</th>
    </tr>
    <tr>
        <th>Xhref</th>
        <th>  https://xhref.blogspot.com/2023/10/alfred-utilitas-open-source-untuk-osint.html</th>
    </tr>
     <tr>
        <th>JOEE txt</th>
        <th>https://www.joeetxt.com/2023/10/alfred-utilitas-open-source-untuk-osint.html</th>
    </tr>
    <tr>
        <th>internet intelligence</th>
        <th>https://internetintelligence.eu/alfred-a-powerful-osint-tool-for-social-media-account-discovery/</th>
    </tr>
    <tr>
        <th>Kali Linux Tutorials</th>
        <th>https://kalilinuxtutorials.com/tookie-osint/</th>
    </tr>
    <tr>
        <th>Hacks.gr</th>
        <th>https://en.hacks.gr/tookie-osint-ergaleio-sullogis-kai-analysis-dimosion-dedomenon/
    </th>
        <tr>
        <th>JJ Gallego</th>
        <th>https://medium.com/cyberscribers-exploring-cybersecurity/osint-for-nicknames-tookie-osint-1364a3c87acf</th>
    </tr>
    </tr>




</table>

# 🎬 Official Tutorials

- https://www.youtube.com/watch?v=crMN_SI7n40&t=2s
- https://www.youtube.com/watch?v=8ciMPAJMB2g
  
# 📘 Contact

- Twitter: https://twitter.com/alfredredbird1

# 🛠 Other Tools

Other tools in the fleet:
- Bibi-Bird (beta): https://github.com/alfredredbird/Bibi-Bird
- Open-Wrecks: https://github.com/Alfredredbird/Open-Wrecks


# 🤝 Partnership
Want to partner with the tookie-osint project? Feel free to reach out.


Partners:
- [X-OSINT](https://github.com/TermuxHackz/X-osint) ~ TermuxHackz
- [GHPM](https://github.com/smoke-wolf/GitHub-Package-Manager) ~ Smoke-Wolf
- [GXSUID](https://github.com/mrofcodyx/gxsuid) ~ mr_ofcodyx
- EliteGreyIT

```

### File: requirements.txt
```txt
colorama 
requests
argparse
selenium 
webdriver-manager
```

### File: brib.py
```py
#!/usr/bin/env python

import os
import requests
import argparse

from colorama import Fore
from concurrent.futures import ThreadPoolExecutor, as_completed
from modules.fancy import *
from modules.webscraper import *
from modules.modules import *



#initializes the arg parser
parser = argparse.ArgumentParser( description="Username OSINT scanner",
    prog="tookie-osint",
    formatter_class=argparse.RawTextHelpFormatter,
    epilog="""
Examples:
  Basic scan (default txt output):
    tookie-osint -u alfred

  JSON output with 10 threads:
    tookie-osint -u alfred -o json -t 10

  Scan usernames from a file:
    tookie-osint -U users.txt -o csv

  Use proxy and show all results:
    tookie-osint -u alfred -p http://127.0.0.1:8080 -a

  Skip random headers:
    tookie-osint -u alfred --skipheaders

  Use webscraper:
    tookie-osint -u alfred -W

  Use a user file list
    tookie-osint -U users.txt -t 20
""")
#arguments
# parser.add_argument("-h", "--help",)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-u", "--user",help="Username to scan")
group.add_argument("-U", "--userfile",help="File path to username file")
parser.add_argument("-t", "--threads", type=int, default=2, help="Threads. Defualt is 2")
parser.add_argument("-d", "--debug", action='store_true',help="Allows debugging options")
parser.add_argument("-sk", "--skipheaders", action='store_true',help="skips using random user agents")
parser.add_argument("-p", "--proxy", type=str, help="proxy")
parser.add_argument("-W", "--webscraper", action='store_true',help="Toggles uses the webscraper")
parser.add_argument(
    "-o", "--output",
    choices=["txt", "csv", "json"],
    default="txt",
    help="Output format (txt, csv, json)"
)
parser.add_argument("-D", "--delay", type=int, help="Delay webscraper should wait for the page to load")
parser.add_argument("-a", "--all", action='store_true', help="Show all results (positive and negative)")

#initializes the arg parser as a variable
args = parser.parse_args()
#arguments as variables
if args.userfile:
    users = load_user_file(args.userfile)
else:
    users = [args.user]
threads = args.threads
debug = args.debug
skip_headers = args.skipheaders
output_format = args.output
webscrape = args.webscraper
delay = args.delay
allsites = args.all
#makes sure threads is not used with the webscraper
if args.webscraper and args.threads != parser.get_default("threads"):
    parser.print_help()
    parser.exit(
        status=1,
        message="\n[!] Error: -W (webscraper) cannot be used with -t (threads)\n"
    )
# checks for update
check_update()
#asks to download request agent file
get_header_file(debug)
# makes system direcotries
# make_sys_dirs(debug)


# data loading
sites = load_sites(debug)
# debuging options
if debug:
  print("DEBUG")
  print("Opening Scan File")

# loads user agents
user_agents = []
if not skip_headers:
    user_agents = load_user_agents()
# writes scan file (will be removed)
# scan_file(user,0)

# Main Function
all_results = {}

total_users = len(users)

for idx, user in enumerate(users, start=1):
    print(f"\n[+] Scanning username: {user}")
    logo(user, idx, total_users)
    # gets basic system info for the logo
    if webscrape:
        threads = 1
    get_system_data(threads,skip_headers)

    results = []

    if not webscrape:
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [
                executor.submit(
                    scan_site, site, user, debug, skip_headers, user_agents, allsites
                )
                for site in sites
            ]

            try:
                for future in as_completed(futures):
                    res = future.result()
                    if res:
                        results.append(res)
            except KeyboardInterrupt:
                print("Stopping!")
                executor.shutdown(wait=False)
                break

    else:
        try:
            scan_webscraper(user, debug, skip_headers, user_agents, delay, allsites)
        except KeyboardInterrupt:
            print("\nStopping web scraper...")
        finally:
            close_driver()

    all_results[user] = results

    # write output per-user
    if output_format == "txt":
        write_txt(user, results)
    elif output_format == "csv":
        write_csv(user, results)
    elif output_format == "json":
        write_json(user, results)
    
print("    ==============================================")
print("Scan done!")
exit(1)

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
the socials in the readme.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: CONTRIBUTING.md
```md
Feel Free To Make Changes To My Code And Submit It. Gl :D

```

### File: install.sh
```sh
#!/usr/bin/env bash
set -e

# -------- CONFIG --------
PROJECT_NAME="tookie-osint"
SOURCE_DIR="$(pwd)"
PYTHON_BIN="python3"
# ------------------------

# Detect OS / Environment
OS="$(uname -s)"
IS_ALPINE=false
IS_TERMUX=false

if [ -f /etc/alpine-release ]; then
    IS_ALPINE=true
fi

if [[ -n "$PREFIX" && "$PREFIX" == *"com.termux"* ]]; then
    IS_TERMUX=true
fi

case "$OS" in
    Darwin*)
        INSTALL_DIR="/usr/local/opt/$PROJECT_NAME"
        BIN_PATH="/usr/local/bin/$PROJECT_NAME"
        CHOWN_CMD="chown -R root:wheel"
        ;;
    Linux*)
        if $IS_TERMUX; then
            INSTALL_DIR="$PREFIX/opt/$PROJECT_NAME"
            BIN_PATH="$PREFIX/bin/$PROJECT_NAME"
            CHOWN_CMD="true"
            PYTHON_BIN="python"
        elif $IS_ALPINE; then
            INSTALL_DIR="/opt/$PROJECT_NAME"
            BIN_PATH="/usr/local/bin/$PROJECT_NAME"
            CHOWN_CMD="chown -R root:root"
        else
            INSTALL_DIR="/opt/$PROJECT_NAME"
            BIN_PATH="/usr/local/bin/$PROJECT_NAME"
            CHOWN_CMD="chown -R root:root"
        fi
        ;;
    *)
        echo "[!] Unsupported OS: $OS"
        exit 1
        ;;
esac

echo "[*] Installing $PROJECT_NAME"
echo "[*] OS: $OS"
$IS_ALPINE && echo "[*] Alpine detected"
$IS_TERMUX && echo "[*] Termux detected"
echo "[*] Install dir: $INSTALL_DIR"

# Root check (skip on Alpine & Termux)
if [ "$EUID" -ne 0 ] && ! $IS_ALPINE && ! $IS_TERMUX; then
    echo "[!] Please run as root (sudo)"
    exit 1
fi

# Remove existing install
if [ -d "$INSTALL_DIR" ]; then
    echo "[*] Removing existing install"
    rm -rf "$INSTALL_DIR"
fi

# Copy project files
echo "[*] Copying files..."
mkdir -p "$(dirname "$INSTALL_DIR")"
cp -r "$SOURCE_DIR" "$INSTALL_DIR"

# Create virtual environment
VENV_DIR="$INSTALL_DIR/.venv"
echo "[*] Creating virtual environment..."

if ! $PYTHON_BIN -m venv "$VENV_DIR" >/dev/null 2>&1; then
    echo
    echo "[!] Python venv not available"
    if $IS_TERMUX; then
        echo "Run:"
        echo "pkg install python"
    elif $IS_ALPINE; then
        echo "apk add --no-cache python3 py3-pip py3-virtualenv"
    fi
    exit 1
fi

"$VENV_DIR/bin/pip" install --upgrade pip
"$VENV_DIR/bin/pip" install -r "$INSTALL_DIR/requirements.txt"

# Create launcher
echo "[*] Writing launcher to $BIN_PATH"
cat << EOF > "$BIN_PATH"
#!/usr/bin/env sh
SCRIPT_DIR="$INSTALL_DIR"
VENV_DIR="\$SCRIPT_DIR/.venv"

if [ ! -d "\$VENV_DIR" ]; then
    echo "[!] Virtual environment missing. Reinstall required."
    exit 1
fi

exec "\$VENV_DIR/bin/python" "\$SCRIPT_DIR/brib.py" "\$@"
EOF

chmod +x "$BIN_PATH"

# Permissions (noop on Termux)
$CHOWN_CMD "$INSTALL_DIR" || true

echo "[✓] Installation complete!"
echo "Run with: $PROJECT_NAME"
```

### File: SECURITY.md
```md
# Security Policy

## Supported Versions



| Version | Supported          |
| ------- | ------------------ |
| MacOS   | :white_check_mark: |
| Kali    | :white_check_mark: |
| Parrot  | :white_check_mark: |
| Windows | :white_check_mark: |
| Ubuntu  | :white_check_mark: |
| Debian  | :white_check_mark: |
| Alpine  | :white_check_mark: |
| Fedora  | :white_check_mark: |
| Arch    | :white_check_mark: |
| Manjaro | :white_check_mark: |
| ChromeOS| :x:                |
| Void    | :white_check_mark: |

Chrome OS might work but none of us
have tried it out. 


## Reporting a Vulnerability
Kindly Make Sure You Download A Oficial Copy Of tookie-osint From Our Site Because We Cannot Check Other Repos For Malware.

If You Have A Problem, Please Make A Issue At https://github.com/alfredredbird/tookie-osint/issues Or Reach Out To Us With The Provided Contact Info.
Thanks For Your Time And Apriciation.

```

### File: uninstall.sh
```sh
#!/usr/bin/env bash
set -e

PROJECT_NAME="tookie-osint"

OS="$(uname -s)"
IS_TERMUX=false

if [[ -n "$PREFIX" && "$PREFIX" == *"com.termux"* ]]; then
    IS_TERMUX=true
fi

case "$OS" in
    Linux*)
        if $IS_TERMUX; then
            INSTALL_DIR="$PREFIX/opt/$PROJECT_NAME"
            BIN_PATH="$PREFIX/bin/$PROJECT_NAME"
        else
            INSTALL_DIR="/opt/$PROJECT_NAME"
            BIN_PATH="/usr/local/bin/$PROJECT_NAME"
        fi
        ;;
    Darwin*)
        INSTALL_DIR="/usr/local/opt/$PROJECT_NAME"
        BIN_PATH="/usr/local/bin/$PROJECT_NAME"
        ;;
    *)
        echo "[!] Unsupported OS"
        exit 1
        ;;
esac

echo "[*] Uninstalling $PROJECT_NAME"
echo "[*] Install dir: $INSTALL_DIR"

# Root check (skip on Termux)
if [ "$EUID" -ne 0 ] && ! $IS_TERMUX; then
    echo "[!] Run with sudo"
    exit 1
fi

rm -f "$BIN_PATH"
rm -rf "$INSTALL_DIR"

echo "[✓] Uninstalled $PROJECT_NAME"
```

### File: windows_install.ps1
```ps1
# ==============================
# Tookie-OSINT Windows Installer
# ==============================

$ProjectName = "tookie-osint"
$SourceDir   = Get-Location
$InstallDir  = "C:\Program Files\$ProjectName"
$BinDir      = "C:\Program Files\$ProjectName\bin"
$Launcher    = "$BinDir\tookie-osint.ps1"
$Python      = "python"

Write-Host "[*] Installing $ProjectName..."

# Ensure admin
if (-not ([Security.Principal.WindowsPrincipal]
    [Security.Principal.WindowsIdentity]::GetCurrent()
).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "[!] Please run PowerShell as Administrator"
    exit 1
}

# Remove existing install
if (Test-Path $InstallDir) {
    Write-Host "[*] Removing existing install"
    Remove-Item -Recurse -Force $InstallDir
}

# Copy files
Write-Host "[*] Copying files to $InstallDir"
Copy-Item $SourceDir $InstallDir -Recurse -Force

# Create bin directory
New-Item -ItemType Directory -Path $BinDir | Out-Null

# Create launcher
Write-Host "[*] Creating launcher"
@"
`$ScriptDir = '$InstallDir'
`$VenvDir   = "`$ScriptDir\.venv"

if (!(Test-Path `$VenvDir)) {
    Write-Host "[*] Creating virtual environment..."
    $Python -m venv `$VenvDir
    & "`$VenvDir\Scripts\pip.exe" install --upgrade pip
    & "`$VenvDir\Scripts\pip.exe" install -r "`$ScriptDir\requirements.txt"
}

& "`$VenvDir\Scripts\python.exe" "`$ScriptDir\brib.py" `$args
"@ | Set-Content $Launcher -Encoding UTF8

# Add to PATH
$CurrentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
if ($CurrentPath -notlike "*$BinDir*") {
    Write-Host "[*] Adding to system PATH"
    [Environment]::SetEnvironmentVariable(
        "Path",
        "$CurrentPath;$BinDir",
        "Machine"
    )
}

Write-Host "[✓] Installation complete!"
Write-Host "Restart your terminal, then run: tookie-osint"
```

### File: windows_uninstall.ps1
```ps1
$ProjectName = "tookie-osint"
$InstallDir  = "C:\Program Files\$ProjectName"

Write-Host "[*] Uninstalling $ProjectName..."

if (-not ([Security.Principal.WindowsPrincipal]
    [Security.Principal.WindowsIdentity]::GetCurrent()
).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "[!] Run PowerShell as Administrator"
    exit 1
}

if (Test-Path $InstallDir) {
    Remove-Item -Recurse -Force $InstallDir
    Write-Host "[✓] Removed $InstallDir"
} else {
    Write-Host "[!] Not installed"
}
```

### File: lang\ar.py
```py
# ar.py
# Arabic

encrypt1 = "تشفير المفتاح..."

title1 = "شكرا جزيلا لشركائنا!"

disclamer = "     تنويه: لا تضمن جميع المواقع أو الوكلاء العمل! \n     باستخدامك، فأنت تتحمل المسؤولية الكاملة عن أفعالك"

targetusernames = "أسماء المستخدمين المستهدفة:"

version = "الإصدار"

config1 = "ملف التكوين موجود "
config2 = "ملف التحديث موجود "
config3 = "المجلد موجود بالفعل: "
config4 = "البحث عن تحديثات؟ [Y / n]: ⤷ "
config5 = "تحرير التكوين؟ [Y / n]: ⤷ "
config6 = "ماذا تريد تغيير؟ ⤷ "
config7 = "إنشاء مجلد: "
config8 = "المجلد موجود بالفعل: "

configOption1 = "[1] البحث عن تحديثات: "
configOption2 = "[2] إظهار النصائح: "
configOption3 = "[3] مسار تنزيل الموقع: "
configOption4 = "[4] المستعرض: "
configOption5 = "[5] اللغة: "
configOption6 = "[6] ColorScheme: "
configOptionA = "[A] تنظيف tookie-osint. (يزيل الملفات المؤقتة)"
configOptionB = "[B] أدوات المطور."

configOption1Message = "حسنا! [checkforupdates] تم تعيينه على نعم. يتغير إلى لا"
configOption2Message = "حسنا! [showtips] تم تعيينه على نعم. يتغير إلى لا"
configOption3Message = "المسار الجديد: ⤷ "
configOption4Message = """
الأنواع المدعومة:
   Firefox
   Edge
   Chrome
"""
configOption5Message = """
            الرجاء إدخال رمز لغتك.
            اللغات المدعومة:
                it = الإيطالية
                en = الإنجليزية
                il = العبرية
                es = الإسبانية
                fr = الفرنسية
                ar = العربية
                de = الألمانية
                ru = الروسية
                hi = الهندية
                pt = البرتغالية
                id = الإندونيسية
                ja = اليابانية
                zh_cn = الصينية المبسطة
                fa = الفارسية
                         """
configOptionAMessage = "تم!"
configOptionBMessage = "مرحبا بك في قائمة المطور!"

configOption1Message2 = "حسنا! [checkforupdates] تم تعيينه على لا. يتغير إلى نعم"
configOption2Message2 = "حسنا! [showtips] تم تعيينه على لا. يتغير إلى نعم"
configOptionBMessage2 = "لا تعطي المفاتيح التالية لأي شخص غير مطور tookie-osint."
configOptionBMessage3 = "privatekey: "
configOptionBMessage4 = "syscrypt: "

target = "الهدف: ⤷ "
browser = "المستعرض: "

file_not_found = "ملف مفقود: {filename}"
permission_denied = "تم رفض الإذن لـ {operation} على {path}"

note = "ملحوظة! "
path = "المسار: ⤷ "
warning1 = (
    "قد لا تسمح العديد من المواقع بتنزيل ملفات مواقعها. استخدم على مسؤوليتك الخاصة."
)
warning2 = "استخدام Webscraper بطيء جدًا."
warning3 = (
    "هذا هو إطلاقك الأول: D قد تحتاج إلى إعادة تشغيل tookie-osint لاستخدام جميع الوحدات"
)
warning4 = "أنت تستخدم إصدارًا مسبقًا من tookie-osint!"
warning5 = "الرجاء إدخال هدف قبل المتابعة:"

confirm1 = "هل تريد تنزيل الصور / مقاطع الفيديو؟ [Y / n] ⤷ "
confirm2 = "تشغيل مرة أخرى؟ [Y / n] ⤷ "

prompt1 = "أدخل الموقع مرة أخرى: ⤷ "
prompt2 = "يرجى إبلاغنا بأي أخطاء أو أخطاء في مستودعنا أو خادم Discord الخاص بنا."
prompt3 = "يمكنك تعطيل التحديث في ملف التكوين"
prompt4 = "انضم إلى Discord: https://discord.gg/xrdjxyuSQt"
prompt5 = "حسنا! سأسأل لاحقا...."
prompt6 = "المواقع التي لا تعمل..."

download1 = "تنزيل "
updates = "التحديثات ممكنة!"

idk1 = "لا أعرف ما تقصد...."
idk2 = "لا أعرف ما تقصد. سأطلب لاحقًا"
idk3 = "لست متأكدًا ... ولكن يمكنك التحقق هنا: "
scan1 = "البحث عن مواقع تحتوي على: "

status1 = "يعمل...."
status2 = "إنشاء / الكتابة فوق ملف الحفظ."
status3 = "إعادة التثبيت............"
status4 = "العودة إلى tookie-osint قريبًا ..."
status5 = "اختبار....."
status6 = "توقف ..... تم حفظها في captured / working.txt"
status7 = "توقف........"

save1 = "نتائج محفوظة إلى"
save2 = "تم حفظ النتائج في ملف"

error1 = "خطأ في الإذن"
error2 = "خطأ في النوع"
error3 = "لا يمكن العثور على ملف الحفظ!"
error4 = "الدليل غير موجود."
error5 = "لا يمكن العثور على الملفات الضرورية. محاولة إعادة تثبيت tookie-osint"
error6 = (
    "أوه خطأ! يبدو أن الاتصال لا يعمل. تحقق من اتصالك أو الوكيل ، ثم حاول مرة أخرى:"
)
error7 = "لا يمكن العثور على ملف الموقع"
error8 = "خطأ في تنزيل محتوى الويب!"
error9 = "خطأ في ملف الموقع"
error10 = "اختيار غير صالح لبرنامج التشغيل."
error11 = "حدث خطأ: "

fileshare1 = "[*] استمع كـ"
fileshare2 = "متصل."
fileshare3 = "استلام"

wikiOption1 = "[1] التثبيت"
wikiOption2 = "[2] خيارات"
wikiOption3 = "[3] أخطاء"
wikiOption4 = "[4] tookie-osint Dark"
wikiOption5 = "[5] وحدات"

wikilist = "يمكنك العثور على معلومات عنها هنا: "

rqUname = "اسم المستخدم المطلوب: "

sender1 = "[+] الاتصال بـ"
sender2 = "[+] متصل."
sender3 = "إرسال."
sender4 = "ملف للإرسال: ⤷ "

fs1 = "خادم مضيف؟ [Y/N]: ⤷ "
fs2 = "في انتظار الاتصال بالمضيف!"
fs3 = "انتظار اتصال العميل!"

siteDl1 = "إجمالي ملفات البرامج النصية في الصفحة:"
siteDl2 = "إجمالي ملفات CSS في الصفحة:"

```

### File: lang\de.py
```py
# de.py
# German

encrypt1 = "Verschlüsselungsschlüssel …"

title1 = "Vielen Dank an unsere Partner!"

disclamer = "Haftungsausschluss: Nicht alle Websites und/oder Proxys sind funktionsfähig! \n Durch die Nutzung übernehmen Sie die volle Verantwortung für Ihre Aktionen."

targetusernames = "Die Zielbenutzernamen:"

version = "Version"

config1 = "Konfigurationsdatei wird beendet"
config2 = "Aktualisierungsdatei existiert"
config3 = "Ordner existiert bereits:"
config4 = "Nach Updates suchen? [J/n]: ⤷ "
config5 = "Die Konfiguration bearbeiten? [J/n]: ⤷"
config6 = "Was möchten Sie ändern? ⤷"
config7 = "Ordner erstellen:"
config8 = "Ordner existiert bereits:"

configOption1 = "[1] Nach Updates suchen:"
configOption2 = "[2] Tipps anzeigen: "
configOption3 = "[3] Site-Download-Pfad:"
configOption4 = "[4] Browser: "
configOption5 = "[5] Sprache: "
configOption6 = "[6] ColorScheme: "
configOptionA = "[A] Bereinigen Sie tookie-osint. (Dadurch werden temporäre Dateien entfernt)"
configOptionB = "[B] Entwicklertools."

configOption1Message = (
    "Ok! [checkforupdates] ist auf Ja eingestellt. Wird in Nein geändert."
)
configOption2Message = "Ok! [showtips] ist auf Ja eingestellt. Wird in Nein geändert."
configOption3Message = "Neuer Pfad: ⤷ "
configOption4Message = """Unterstützte Typen:
                          Firefox
                          Edge
                          Chrome
                          """
configOption5Message = """
            Bitte geben Sie Ihren Sprachcode ein.
            Unterstützte Sprachen:
                it = Italienisch
                en = Englisch
                il = Hebräisch
                es = Spanisch
                fr = Französisch
                ar = Arabisch
                de = Deutsch
                ru = Russisch
                hi = Hindi
                pt = Portugiesisch
                id = Indonesisch
                ja = Japanisch
                zh_cn = Vereinfachtes Chinesisch
                fa = Farsi
                         """
configOptionAMessage = "Fertig!"
configOptionBMessage = "Willkommen im Entwicklermenü!"

configOption1Message2 = (
    "Ok! [checkforupdates] ist auf Nein eingestellt. Wird in Ja geändert."
)
configOption2Message2 = "Ok! [showtips] ist auf Nein eingestellt. Wird in Ja geändert."
configOptionBMessage2 = (
    "Geben Sie die folgenden Schlüssel niemandem außer einem tookie-osint-Entwickler."
)
configOptionBMessage3 = "privatekey: "
configOptionBMessage4 = "syscrypt: "

target = "Ziel: ⤷ "
browser = "Browser: "

file_not_found = "Datei nicht gefunden: {filename}"
permission_denied = "Berechtigung für {operation} in {path} verweigert"

note = "Hinweis! "
path = "PFAD: ⤷ "
warning1 = "Viele Webseiten untersagen das Herunterladen ihrer Dateien. Nutzung auf eigene Gefahr."
warning2 = "Die Verwendung des Webscrapers ist ziemlich langsam."
warning3 = "Dies ist Ihr erster Start :D Möglicherweise müssen Sie tookie-osint neu starten, um alle Module nutzen zu können."
warning4 = "Sie verwenden eine Vorabversion von tookie-osint!"
warning5 = "Bitte geben Sie ein Ziel ein, bevor Sie fortfahren: "

confirm1 = "Möchten Sie Bilder/Videos herunterladen? [J/n] ⤷ "
confirm2 = "Erneut ausführen?: [J/n] ⤷"

prompt1 = "Site erneut aufrufen: ⤷"
prompt2 = "Bitte melden Sie etwaige Bugs oder Fehler unserem Repo- oder Discord-Server."
prompt3 = "Sie können die Aktualisierung in der Konfigurationsdatei deaktivieren"
prompt4 = "Treten Sie unserem Discord bei: https://discord.gg/xrdjxyuSQt"
prompt5 = "Ok! Ich frage später nach …"
prompt6 = "Seiten funktionieren nicht…"

download1 = "Herunterladen"
Updates = "Updates sind aktiviert!"


idk1 = "Ich bin mir nicht sicher, was Sie meinten …"
idk2 = "Ich bin mir nicht sicher, was Sie gemeint haben. Ich frage später nach."
idk3 = "Nicht sicher.... Aber Sie können hier nachschauen:"
scan1 = "Suche nach Websites mit: "

status1 = "Arbeitet …"
status2 = "Speicherdatei wird erstellt/überschrieben."
status3 = "Neuinstallation............"
status4 = "Bald zurück zu tookie-osint …"
status5 = "Wird getestet...."
status6 = "Wird gestoppt.... Gespeichert in captured/working.txt"
status7 = "Wird gestoppt......."

save1 = "Ergebnisse gespeichert unter"
save2 = "Ergebnisse in Datei gespeichert"

error1 = "Berechtigungsfehler"
error2 = "Typfehler"
error3 = "Die gespeicherte Datei kann nicht gefunden werden!"
error4 = "Verzeichnis existiert nicht."
error5 = "Erforderliche Dateien können nicht gefunden werden. Versuche tookie-osint neu zu installieren"
error6 = "Oh, Fehler! Die Verbindung scheint nicht zu funktionieren. Überprüfen Sie Ihre Verbindung oder Ihren Proxy und versuchen Sie es dann erneut:"
error7 = "Site-Datei kann nicht gefunden werden"
error8 = "Fehler beim Herunterladen von Webinhalten!"
error9 = "Fehler mit der Site-Datei"
error10 = "Ungültige Webtreiberauswahl."
error11 = "Ein Fehler ist aufgetreten:"

fileshare1 = "[*] Hört als"
fileshare2 = "ist verbunden."
fileshare3 = "Empfangen"

wikiOption1 = "[1] Installation"
wikiOption2 = "[2] Optionen"
wikiOption3 = "[3] Fehler"
wikiOption4 = "[4] Dunkler tookie-osint"
wikiOption5 = "[5] Module"

wikilist = "Infos dazu finden Sie hier:"

rqUname = "Angeforderter Benutzername:"

sender1 = "[+] Verbindung herstellen mit"
sender2 = "[+] Verbunden."
sender3 = "Sendet."
sender4 = "Zu sendende Datei: ⤷"

fs1 = "Hostserver? [J/N]: ⤷"
fs2 = "Warten auf Verbindung zum Host!"
fs3 = "Warten auf die Verbindung des Clients!"

siteDl1 = "Gesamtzahl der Skriptdateien auf der Seite:"
siteDl2 = "Gesamtzahl der CSS-Dateien auf der Seite:"

```

### File: lang\en.py
```py
# en.py
# English

encrypt1 = "Encrypting key..."

title1 = "Many thanks to our partners!"

disclamer = "     Disclaimer: Not all sites and/or proxies are guaranteed to work! \n     By using this, you take full responsibility for your actions!"

targetusernames = "The target username(s): "

version = "Version"

config1 = "Config file exists "
config2 = "Update file exists "
config3 = "Folder already exists: "
config4 = "Check for updates? [Y/n]: ⤷ "
config5 = "Edit the config? [Y/n]: ⤷ "
config6 = "What do you want to change? ⤷ "
config7 = "Creating folder: "
config8 = "Folder already exists: "

configOption1 = "[1] Check for updates: "
configOption2 = "[2] Show tips: "
configOption3 = "[3] Site Download Path: "
configOption4 = "[4] Browser: "
configOption5 = "[5] Language: "
configOption6 = "[6] ColorScheme: "
configOptionA = "[A] Clean Up tookie-osint. (This Removes Temporary Files)"
configOptionB = "[B] Developer Tools."

configOption1Message = "Okay, [checkforupdates] is set to yes. Changing to no."
configOption2Message = "Okay, [showtips] is set to yes. Changing to no."
configOption3Message = "New path: ⤷ "
configOption4Message = """Types supported:
                         Firefox
                         Edge
                         Chrome
                         """
configOption5Message = """
            Please enter your language code.
            Supported languages:
                it = Italian
                en = English
                il = Hebrew
                es = Spanish
                fr = French
                ar = Arabic
                de = German
                ru = Russian
                hi = Hindi
                pt = Portuguese
                id = Indonesia
                ja = Japanese
                zh_cn = Simplified Chinese
                fa = Farsi
                         """
configOptionAMessage = "Done!"
configOptionBMessage = "Welcome to the developer menu!"

configOption1Message2 = "Okay, [checkforupdates] is set to no. Changing to yes."
configOption2Message2 = "Okay, [showtips] is set to no. Changing to yes."
configOptionBMessage2 = (
    "Don't give the following keys to anyone except an tookie-osint developer!"
)
configOptionBMessage3 = "privatekey: "
configOptionBMessage4 = "syscrypt: "

target = "Target: ⤷ "
browser = "Browser: "

file_not_found = "File not found: {filename}"
permission_denied = "Permission denied for {operation} on {path}"

note = "Note! "
path = "PATH: ⤷ "
warning1 = (
    "Many sites don't allow the downloading of their files. Use at your own risk."
)
warning2 = " Be aware that the web scraper is a bit slow."
warning3 = " This is your first launch! :D You may need to restart tookie-osint for all modules to be available."
warning4 = " You are using a pre-release version of tookie-osint!"
warning5 = "Please enter a target before continuing: "

confirm1 = "Want to download images/videos? [Y/n] ⤷ "
confirm2 = "Run again? [Y/n] ⤷ "

prompt1 = "Enter site again: ⤷ "
prompt2 = "Kindly report any bugs by making issues on the repo, or report them on the Discord server. "
prompt3 = "You can disable updating in the config file."
prompt4 = "Join our Discord: https://discord.gg/xrdjxyuSQt "
prompt5 = "Okay, I'll ask later..."
prompt6 = " These sites aren't working:"

download1 = "Downloading "
updates = "Updates are enabled!"


idk1 = "Not sure what you meant..."
idk2 = "Not sure what you meant, I'll ask later."
idk3 = "Not sure, but you can check here: "
scan1 = "Searching for sites with: "

status1 = "Working..."
status2 = "Creating/overwriting save file."
status3 = "Reinstalling..."
status4 = "Returning to tookie-osint soon..."
status5 = "Testing..."
status6 = "Stopping... saved to captured/working.txt!"
status7 = "Stopping..."

save1 = "Saved results to"
save2 = "Saved results to file"

error1 = "Permission error!"
error2 = "Type error!"
error3 = "Can't find the save file!"
error4 = "Directory doesn't exist."
error5 = "Can't find necessary files. Trying to reinstall tookie-osint."
error6 = (
    "Looks like we can't connect. Check your connection and/or proxy and try again."
)
error7 = "Can't find site file"
error8 = "Error downloading web content!"
error9 = "Error with site file"
error10 = "Invalid webdriver selection."
error11 = "An error occurred: "

fileshare1 = "[*] Listening as"
fileshare2 = "is connected."
fileshare3 = "Receiving"

wikiOption1 = "[1] Installation"
wikiOption2 = "[2] Options"
wikiOption3 = "[3] Errors"
wikiOption4 = "[4] Dark tookie-osint"
wikiOption5 = "[5] Modules"

wikilist = "You can find info on it here: "

rqUname = "Requested username: "

sender1 = "[+] Connecting to"
sender2 = "[+] Connected."
sender3 = "Sending."
sender4 = "File to send: ⤷ "

fs1 = "Host server? [Y/N]: ⤷ "
fs2 = "Waiting to connect to host!"
fs3 = "Waiting for client to connect!"

siteDl1 = "Total script files in the page:"
siteDl2 = "Total CSS files in the page:"
# example bc imma forget
# import messages

# print(messages.title)  # Output: Hello, World!
# print(messages.text1)  # Output: This is a sample message.

# # Example of using placeholders in messages
# filename = "example.txt"
# print(messages.file_not_found.format(filename=filename))

```

### File: lang\es.py
```py
# es.py
# Español

encrypt1 = "Cifrando Clave..."

title1 = "¡Muchas gracias a nuestros socios!"

disclamer = "     Descargo de responsabilidad: ¡No se garantiza que todos los sitios o proxies funcionen! \n     Al usar, asume toda la responsabilidad de sus acciones"

targetusernames = "Los nombres de usuario de destino:"

version = "Versión"

config1 = "Existe archivo de configuración"
config2 = "Existe archivo de actualización"
config3 = "La carpeta ya existe:"
config4 = "¿Buscar actualizaciones? [Y/n]: ⤷ "
config5 = "¿Editar la configuración? [Y/n]: ⤷ "
config6 = "¿Qué quieres cambiar? ⤷ "
config7 = "Creando carpeta:"
config8 = "La carpeta ya existe:"

configOption1 = "[1] Buscar actualizaciones: "
configOption2 = "[2] Mostrar consejos: "
configOption3 = "[3] Ruta de descarga del sitio: "
configOption4 = "[4] Navegador: "
configOption5 = "[5] Idioma: "
configOption6 = "[6] ColorScheme: "
configOptionA = "[A] Limpiar tookie-osint. (Esto elimina archivos temporales)"
configOptionB = "[B] Herramientas de desarrollo."

configOption1Message = "¡Ok! [checkforupdates] está configurado en Sí. Cambiando a No"
configOption2Message = "¡Ok! [showtips] está configurado en Sí. Cambiando a No"
configOption3Message = "Nueva ruta: ⤷ "
configOption4Message = """Tipos compatibles:
                         Firefox
                         Edge
                         Chrome
                         """
configOption5Message = """
            Por favor, ingrese su código de idioma.
            Idiomas soportados:
                it = Italiano
                en = Inglés
                il = Hebreo
                es = Español
                fr = Francés
                ar = Árabe
                de = Alemán
                ru = Ruso
                hi = Hindi
                pt = Portugués
                id = Indonesio
                ja = Japonés
                zh_cn = Chino simplificado
                fa = Farsí
                         """
configOptionAMessage = "¡Hecho!"
configOptionBMessage = "¡Bienvenido al menú de desarrolladores!"

configOption1Message2 = "¡Ok! [checkforupdates] está configurado en No. Cambiando a Sí"
configOption2Message2 = "¡Ok! [showtips] está configurado en No. Cambiando a Sí"
configOptionBMessage2 = (
    "NO proporcione las siguientes claves a nadie que no sea un desarrollador de tookie-osint"
)
configOptionBMessage3 = "claveprivada: "
configOptionBMessage4 = "syscrypt: "

target = "Objetivo: ⤷ "
browser = "Navegador: "

file_not_found = "Archivo no encontrado: {filename}"
permission_denied = "Permiso denegado para {operation} en {path}"

note = "¡Nota! "
path = "RUTA: ⤷ "
warning1 = "Es posible que los sitios no permitan la descarga de los archivos de su sitio. Úselo bajo su propio riesgo."
warning2 = "El uso del web scraper es bastante lento"
warning3 = "Este es tu primer lanzamiento :D Es posible que debas reiniciar tookie-osint para usar todos los módulos"
warning4 = "¡Estás usando una versión preliminar de tookie-osint!"
warning5 = "Por favor, introduzca un objetivo antes de continuar: "

confirm1 = "¿Desea descargar imágenes/videos? [Y/n] ⤷ "
confirm2 = "¿Ejecutar de nuevo? [Y/n] ⤷ "

prompt1 = "Vuelve a ingresar el sitio: ⤷ "
prompt2 = "Por favor, informe cualquier error o bug a nuestro repositorio o servidor de Discord. "
prompt3 = "Puede deshabilitar la actualización en el archivo de configuración"
prompt4 = "Únase a nuestro Discord: https://discord.gg/xrdjxyuSQt "
prompt5 = "¡Ok! Lo preguntaré más tarde..."
prompt6 = "Sitios que no funcionan..."

download1 = "Descargando "
updates = "¡Las actualizaciones están habilitadas!"


idk1 = "No estoy seguro de qué quieres decir..."
idk2 = "No estoy seguro de qué quieres decir. Lo preguntaré más tarde"
idk3 = "No estoy seguro... pero puedes consultar aquí: "
scan1 = "buscando sitios con: "

status1 = "Trabajando..."
status2 = "Creando / sobrescribiendo archivo guardado."
status3 = "Reinstalando............"
status4 = "Regresando a tookie-osint pronto..."
status5 = "Probando....."
status6 = "Deteniendo..... Guardado en capturado/trabajando.txt"
status7 = "Deteniendo........"

save1 = "Resultados guardados en"
save2 = "Resultados guardados en archivo"

error1 = "Error de permiso"
error2 = "Error de tipo"
error3 = "¡No puedo encontrar el archivo guardado!"
error4 = "El directorio no existe."
error5 = "No se pueden encontrar los archivos necesarios. Se intenta reinstalar tookie-osint."
error6 = "¡Error de Uh Oh! Parece que la conexión no parece funcionar. Revise su conexión o proxy, luego intente nuevamente:"
error7 = "No se puede encontrar el archivo del sitio"
error8 = "¡Error al descargar contenido web!"
error9 = "Error con el archivo del sitio"
error10 = "Selección de webdriver no válida."
error11 = "Ocurrió un error:"

fileshare1 = "[*] Escuchando como"
fileshare2 = "está conectado."
fileshare3 = "Recibiendo"

wikiOption1 = "[1] Instalación"
wikiOption2 = "[2] Opciones"
wikiOption3 = "[3] Errores"
wikiOption4 = "[4] tookie-osint oscuro"
wikiOption5 = "[5] Módulos"

wikilist = "Puede encontrar información al respecto aquí: "

rqUname = "Usuario solicitado: "

sender1 = "[+] Conectando a"
sender2 = "[+] Conectado."
sender3 = "Envío."
sender4 = "Archivo para enviar: ⤷ "

fs1 = "¿Servidor host? [Y/N]: ⤷ "
fs2 = "¡Esperando para conectarse al host!"
fs3 = "¡Esperando que se conecte el cliente!"

siteDl1 = "Total de archivos de script en la página:"
siteDl2 = "Total de archivos CSS en la página:"

```

### File: lang\fa.py
```py
# fa.py
# Farsi (Persian)

encrypt1 = "در حال رمزگذاری کلید..."

title1 = "با تشکر فراوان از شرکای ما!"

disclamer = "     سلب مسئولیت: تضمین نمی شود که همه سایت ها و/یا پروکسی ها کار کنند! \n     با استفاده از این، شما مسئولیت کامل اقدامات خود را بر عهده می گیرید!"

targetusernames = "نام کاربری مورد نظر:"

version = "نسخه"

config1 = "فایل پیکربندی وجود دارد"
config2 = "فایل به روز رسانی وجود دارد"
config3 = "پوشه از قبل وجود دارد:"
config4 = "بررسی برای به روز رسانی؟ [Y/n]: ⤷ "
config5 = "ویرایش پیکربندی؟ [Y/n]: ⤷ "
config6 = "چه چیزی را می خواهید تغییر دهید؟ ⤷ "
config7 = "در حال ایجاد پوشه:"
config8 = "پوشه از قبل وجود دارد:"

configOption1 = "[1] بررسی برای به روز رسانی:"
configOption2 = "[2] نمایش نکات:"
configOption3 = "[3] مسیر دانلود سایت:"
configOption4 = "[4] مرورگر:"
configOption5 = "[5] زبان:"
configOption6 = "[6] طرح رنگ:"
configOptionA = "[A] پاکسازی tookie-osint. (این فایل های موقت را حذف می کند)"
configOptionB = "[B] ابزارهای توسعه دهنده."

configOption1Message = "بسیار خب، [checkforupdates] روی بله تنظیم شده است. در حال تغییر به خیر."
configOption2Message = "بسیar خب، [showtips] روی بله تنظیم شده است. در حال تغییر به خیر."
configOption3Message = "مسیر جدید: ⤷ "
configOption4Message = """انواع پشتیبانی شده:
                         Firefox
                         Edge
                         Chrome
                         """
configOption5Message = """
            لطفاً کد زبان خود را وارد کنید.
            زبان های پشتیبانی شده:
                it = ایتالیایی
                en = انگلیسی
                il = عبری
                es = اسپانیایی
                fr = فرانسوی
                ar = عربی
                de = آلمانی
                ru = روسی
                hi = هندی
                pt = پرتغالی
                id = اندونزیایی
                ja = ژاپنی
                zh_cn = چینی ساده شده
                fa = فارسی
                         """
configOptionAMessage = "انجام شد!"
configOptionBMessage = "به منوی توسعه دهندگان خوش آمدید!"

configOption1Message2 = "بسیار خب، [checkforupdates] روی خیر تنظیم شده است. در حال تغییر به بله."
configOption2Message2 = "بسیار خب، [showtips] روی خیر تنظیم شده است. در حال تغییر به بله."
configOptionBMessage2 = (
    "کلیدهای زیر را به کسی جز توسعه دهنده tookie-osint ندهید!"
)
configOptionBMessage3 = "کلید خصوصی:"
configOptionBMessage4 = "رمز سیستم:"

target = "هدف: ⤷ "
browser = "مرورگر:"

file_not_found = "فایل یافت نشد: {filename}"
permission_denied = "مجوز برای {operation} در {path} رد شد"

note = "توجه!"
path = "مسیر: ⤷ "
warning1 = (
    "بسیاری از سایت ها اجازه دانلود فایل های خود را نمی دهند. با مسئولیت خود استفاده کنید."
)
warning2 = "آگاه باشید که وب اسکرپر کمی کند است."
warning3 = "این اولین راه اندازی شماست! :D ممکن است برای در دسترس بودن همه ماژول ها نیاز به راه اندازی مجدد tookie-osint داشته باشید."
warning4 = "شما در حال استفاده از نسخه پیش از انتشار tookie-osint هستید!"
warning5 = "لطفاً قبل از ادامه یک هدف وارد کنید:"

confirm1 = "آیا می خواهید تصاویر/فیلم ها را دانلود کنید؟ [Y/n] ⤷ "
confirm2 = "دوباره اجرا شود؟ [Y/n] ⤷ "

prompt1 = "دوباره سایت را وارد کنید: ⤷ "
prompt2 = "لطفاً هر گونه اشکال را با ایجاد مشکل در مخزن یا گزارش آنها در سرور Discord گزارش دهید."
prompt3 = "می توانید به روز رسانی را در فایل پیکربندی غیرفعال کنید."
prompt4 = "به Discord ما بپیوندید: https://discord.gg/xrdjxyuSQt"
prompt5 = "بسیار خب، بعداً می پرسم..."
prompt6 = "این سایت ها کار نمی کنند:"

download1 = "در حال دانلود"
updates = "به روز رسانی ها فعال است!"


idk1 = "مطمئن نیستم منظورتان چیست..."
idk2 = "مطمئن نیستم منظورتان چیست، بعداً می پرسم."
idk3 = "مطمئن نیستم، اما می توانید اینجا را بررسی کنید:"
scan1 = "در حال جستجوی سایت ها با:"

status1 = "در حال کار..."
status2 = "در حال ایجاد/بازنویسی فایل ذخیره."
status3 = "در حال نصب مجدد..."
status4 = "به زودی به tookie-osint باز می گردد..."
status5 = "در حال آزمایش..."
status6 = "در حال توقف... در captured/working.txt ذخیره شد!"
status7 = "در حال توقف..."

save1 = "نتایج در ذخیره شد"
save2 = "نتایج در فایل ذخیره شد"

error1 = "خطای مجوز!"
error2 = "خطای نوع!"
error3 = "فایل ذخیره را پیدا نمی کنید!"
error4 = "پوشه وجود ندارد."
error5 = "فایل های لازم را پیدا نمی کنید. در تلاش برای نصب مجدد tookie-osint."
error6 = (
    "به نظر می رسد نمی توانیم وصل شویم. اتصال و/یا پروکسی خود را بررسی کرده و دوباره امتحان کنید."
)
error7 = "فایل سایت را پیدا نمی کنید"
error8 = "خطا در دانلود محتوای وب!"
error9 = "خطا در فایل سایت"
error10 = "انتخاب وب درایور نامعتبر است."
error11 = "خطایی روی داد:"

fileshare1 = "[*] در حال گوش دادن به عنوان"
fileshare2 = "متصل است."
fileshare3 = "در حال دریافت"

wikiOption1 = "[1] نصب"
wikiOption2 = "[2] گزینه ها"
wikiOption3 = "[3] خطاها"
wikiOption4 = "[4] tookie-osint تاریک"
wikiOption5 = "[5] ماژول ها"

wikilist = "می توانید اطلاعات مربوط به آن را در اینجا پیدا کنید:"

rqUname = "نام کاربری درخواستی:"

sender1 = "[+] در حال اتصال به"
sender2 = "[+] متصل شد."
sender3 = "در حال ارسال."
sender4 = "فایل برای ارسال: ⤷ "

fs1 = "سرور میزبان؟ [Y/N]: ⤷ "
fs2 = "در انتظار اتصال به میزبان!"
fs3 = "در انتظار اتصال مشتری!"

siteDl1 = "تعداد کل فایل های اسکریپت در صفحه:"
siteDl2 = "تعداد کل فایل های CSS در صفحه:"
# example bc imma forget
# import messages

# print(messages.title)  # Output: Hello, World!
# print(messages.text1)  # Output: This is a sample message.

# # Example of using placeholders in messages
# filename = "example.txt"
# print(messages.file_not_found.format(filename=filename))
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
