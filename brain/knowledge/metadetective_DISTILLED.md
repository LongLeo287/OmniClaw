---
id: MetaDetective
type: knowledge
owner: OA_Triage
---
# MetaDetective
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div id="top" align="center">

<!-- Sponsorship -->
<p align="center">
  <a href="https://iproyal.com/?r=848799" target="_blank">
    <img src="https://raw.githubusercontent.com/franckferman/MetaDetective/stable/docs/github/graphical_resources/IPRoyal-Logo_Transparent_500x500.png" alt="Sponsored by IPRoyal" width="180">
  </a>
</p>
<p align="center"><b>Supported by <a href="https://iproyal.com/?r=848799">IPRoyal</a></b> &mdash; Proxy services for OSINT and security research.</p>

<br>

[![Contributors][contributors-shield]](https://github.com/franckferman/MetaDetective/graphs/contributors)
[![Forks][forks-shield]](https://github.com/franckferman/MetaDetective/network/members)
[![Stargazers][stars-shield]](https://github.com/franckferman/MetaDetective/stargazers)
[![Issues][issues-shield]](https://github.com/franckferman/MetaDetective/issues)
[![PyPI][pypi-shield]](https://pypi.org/project/MetaDetective/)
[![Docker][docker-shield]](https://hub.docker.com/r/franckferman/metadetective)
[![License][license-shield]](https://github.com/franckferman/MetaDetective/blob/stable/LICENSE)
![Python Stdlib](https://img.shields.io/badge/Python%20deps-stdlib%20only-green?style=for-the-badge)
![ExifTool](https://img.shields.io/badge/Requires-ExifTool-blue?style=for-the-badge)

<a href="https://github.com/franckferman/MetaDetective">
  <img src="https://raw.githubusercontent.com/franckferman/MetaDetective/stable/docs/github/graphical_resources/Logo-Without_background-MetaDetective.png" alt="MetaDetective" width="340">
</a>

<h3 align="center">MetaDetective</h3>
<p align="center">Metadata extraction and web scraping for OSINT and pentesting.</p>


</div>

---

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

---

## About

MetaDetective is a single-file Python 3 tool for metadata extraction and web scraping, built for OSINT and pentesting workflows.

It has no Python dependencies beyond exiftool. One `curl` and you're operational.

**What it extracts:** authors, software versions, GPS coordinates, creation/modification dates, internal hostnames, serial numbers, hyperlinks, camera models - across documents, images, and email files.

**What it does beyond extraction:**
- Direct web scraping of target sites (no search engine dependency, no IP blocks)
- GPS reverse geocoding with OpenStreetMap, map link generation
- Export to HTML, TXT, or JSON
- Selective field extraction with `--parse-only`
- Deduplication across multiple files

It was built as a replacement for Metagoofil, which dropped native metadata analysis and relied on Google search (rate limiting, CAPTCHAs, proxy overhead).

<p align="center">
  <img src="https://raw.githubusercontent.com/franckferman/MetaDetective/stable/docs/github/graphical_resources/Screenshot-MetaDetective_Demo.png" alt="MetaDetective demo" width="700">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/franckferman/MetaDetective/stable/docs/github/graphical_resources/Screenshot-MetaDetective_Scraping_Demo.png" alt="MetaDetective scraping demo" width="700">
</p>

---

## Installation

**Requirements:** Python 3, exiftool.

```bash
# Debian / Ubuntu / Kali
sudo apt install libimage-exiftool-perl

# macOS
brew install exiftool

# Windows
winget install OliverBetz.ExifTool
```

### Direct download (recommended for field use)

```bash
curl -O https://raw.githubusercontent.com/franckferman/MetaDetective/stable/src/MetaDetective/MetaDetective.py
python3 MetaDetective.py -h
```

### pip

```bash
pip install MetaDetective
metadetective -h
```

### git clone

```bash
git clone https://github.com/franckferman/MetaDetective.git
cd MetaDetective
python3 src/MetaDetective/MetaDetective.py -h
```

### Docker

```bash
docker pull franckferman/metadetective
docker run --rm franckferman/metadetective -h

# Mount a local directory
docker run --rm -v $(pwd)/loot:/data franckferman/metadetective -d /data
```

---

## Usage

### File analysis

```bash
# Analyze a directory (deduplicated singular view by default)
python3 MetaDetective.py -d ./loot/

# Specific file types, filter noise
python3 MetaDetective.py -d ./loot/ -t pdf docx -i admin anonymous

# Per-file display
python3 MetaDetective.py -d ./loot/ --display all

# Formatted output (singular/default display)
python3 MetaDetective.py -d ./loot/ --format formatted

# Single file
python3 MetaDetective.py -f report.pdf

# Multiple files
python3 MetaDetective.py -f report.pdf photo.heic
```

### Summary and timeline

```bash
# Quick stats: identities, emails, GPS exposure, tools, date range
python3 MetaDetective.py -d ./loot/ --summary

# Chronological view of document creation/modification
python3 MetaDetective.py -d ./loot/ --timeline

# Both together
python3 MetaDetective.py -d ./loot/ --summary --timeline

# Scripting: no banner, summary only
python3 MetaDetective.py -d ./loot/ --summary --no-banner
```

### Selective parsing

`--parse-only` limits extraction to specific fields. Useful to cut noise or target a specific data point.

```bash
# Extract only Author and Creator fields
python3 MetaDetective.py -d ./loot/ --parse-only Author Creator

# Extract GPS data only from iPhone photos
python3 MetaDetective.py -d ./photos/ -t heic heif --parse-only 'GPS Position' 'Map Link'
```

### Export

```bash
# HTML report (default)
python3 MetaDetective.py -d ./loot/ -e

# TXT
python3 MetaDetective.py -d ./loot/ -e txt

# JSON - singular (deduplicated values per field)
python3 MetaDetective.py -d ./loot/ -e json

# JSON - per file
python3 MetaDetective.py -d ./loot/ --display all -e json

# Custom filename suffix and output directory
python3 MetaDetective.py -d ./loot/ -e json -c pentest-corp -o ~/results/
```

JSON singular output structure:
```json
{
  "tool": "MetaDetective",
  "generated": "2026-03-21T...",
  "unique": {
    "Author": ["Alice Martin", "Bob Dupont"],
    "Creator Tool": ["Microsoft Word 16.0"]
  }
}
```

Pivot with jq:
```bash
jq '.unique.Author' MetaDetective_Export-*.json
```

### Web scraping

MetaDetective can crawl a target website, discover downloadable files (PDF, DOCX, XLSX, images, etc.), and download them for local metadata analysis.

**Two scraping modes:**

- **`--download-dir`** - Download files to a local directory for analysis. This is the primary mode.
- **`--scan`** - Preview only: list discovered files and stats without downloading. Useful for scoping before a full download.

> `--scan` and `--download-dir` are mutually exclusive.

**The `--depth` flag is critical.** By default, depth is **0**: MetaDetective only looks at the URL you provide. Most interesting files (reports, presentations, internal documents) are linked from subpages, not the homepage. **Always set `--depth 1` or higher for real engagements.**

| Depth | Behavior |
|-------|----------|
| `0` (default) | Only the target URL. Finds files directly linked on that single page. |
| `1` | Target URL + all pages linked from it. Covers most site structures. |
| `2+` | Follows links N levels deep. Broader coverage, more requests, slower. |

**Download (primary workflow):**

```bash
# Standard download with depth 1 (recommended starting point)
python3 MetaDetective.py --scraping --url https://target.com/ \
  --download-dir ~/loot/ --depth 1

# Target specific file types
python3 MetaDetective.py --scraping --url https://target.com/ \
  --download-dir ~/loot/ --depth 2 --extensions pdf docx xlsx pptx

# Parallel download (8 threads, 10 req/s)
python3 MetaDetective.py --scraping --url https://target.com/ \
  --download-dir ~/loot/ --depth 2 --threads 8 --rate 10

# Follow external links (CDN, subdomain, partner sites)
python3 MetaDetective.py --scraping --url https://target.com/ \
  --download-dir ~/loot/ --depth 1 --follow-extern

# Stealth: realistic User-Agent + low rate
python3 MetaDetective.py --scraping --url https://target.com/ \
  --download-dir ~/loot/ --depth 2 --user-agent stealth --rate 2
```

**Scan (preview):**

```bash
# Quick preview: how many files are reachable?
python3 MetaDetective.py --scraping --scan --url https://target.com/ --depth 1

# Filter preview by extension
python3 MetaDetective.py --scraping --scan --url https://target.com/ \
  --depth 2 --extensions pdf docx
```

**Full pipeline (scrape + analyze + export):**

```bash
# Step 1: download files
python3 MetaDetective.py --scraping --url https://target.com/ \
  --download-dir ~/loot/ --depth 2 --extensions pdf docx xlsx

# Step 2: analyze and export
python3 MetaDetective.py -d ~/loot/ -e html -o ~/results/
```

| Flag | Default | Description |
|------|---------|-------------|
| `--url` | required | Target URL |
| `--download-dir` | - | Download destination (created if needed) |
| `--scan` | - | Preview mode (no download) |
| `--depth` | `0` | Link depth to follow. **Set to 1+ for real use.** |
| `--extensions` | all supported | Filter by file type |
| `--threads` | `4` | Concurrent download threads (1-100) |
| `--rate` | `5` | Max requests per second (1-1000) |
| `--follow-extern` | off | Follow links to external domains |
| `--user-agent` | `MetaDetective/<ver>` | Custom or preset UA string |

### Display modes

MetaDetective offers two display modes that control how results are structured:

**`--display singular`** (default) - Aggregates all unique values per field across every file. Best for OSINT: "who touched these documents?" at a glance.

```bash
# Default: deduplicated singular view
python3 MetaDetective.py -d ./loot/

# With formatted style (vertical list with markers)
python3 MetaDetective.py -d ./loot/ --format formatted

# With concise style (comma-separated on one line)
python3 MetaDetective.py -d ./loot/ --format concise
```

**`--display all`** - One block per file with its individual metadata. Best for forensic analysis: examine each document's properties independently.

```bash
python3 MetaDetective.py -d ./loot/ --display all
```

> `--format` only works with `--display singular`. Using `--format` with `--display all` produces an error.

**Additional views:**

| Flag | Description |
|------|-------------|
| `--summary` | Statistical overview: file count, unique identities, emails, GPS exposure, tools, date range |
| `--timeline` | Chronological view of document creation and modification events |
| `--no-banner` | Suppress the ASCII banner for scripting and pipeline use |

### Export formats

Three export formats are available. All respect the current `--display` mode.

```bash
# HTML report with dark theme, stats bar, and responsive layout
python3 MetaDetective.py -d ./loot/ -e html

# HTML per-file view
python3 MetaDetective.py -d ./loot/ --display all -e html

# Plain text
python3 MetaDetective.py -d ./loot/ -e txt

# JSON (structured, pipe into jq)
python3 MetaDetective.py -d ./loot/ -e json

# Custom output directory (created automatically if it does not exist)
python3 MetaDetective.py -d ./loot/ -e html -o ~/results/

# Custom filename suffix
python3 MetaDetective.py -d ./loot/ -e json -c pentest-corp -o ~/results/
```

The HTML export includes a summary header showing total files analyzed, total metadata fields extracted, and unique identities found (from Author, Creator, and Last Modified By fields).

### User-Agent (scraping)

When scraping, MetaDetective identifies itself as `MetaDetective/<version>` by default. Use `--user-agent` to change this:

```bash
# Use a preset
python3 MetaDetective.py --scraping --scan --url https://target.com/ --user-agent stealth

# Available presets
#   stealth, chrome-win, chrome-mac, chrome-linux,
#   firefox-win, firefox-mac, firefox-linux,
#   safari-mac, edge-win, android, iphone, googlebot

# Custom string
python3 MetaDetective.py --scraping --scan --url https://target.com/ \
  --user-agent 'Mozilla/5.0 (compatible; MyScanner/1.0)'
```

### Filtering

| Flag | Description |
|------|-------------|
| `-t pdf docx` | Restrict to file types |
| `-i admin anonymous` | Ignore values matching pattern (regex supported) |
| `--parse-only Author Creator` | Extract only specified fields |

### Supported formats

Documents: PDF, DOCX, ODT, XLS, XLSX, PPTX, ODP, RTF, CSV, XML
Images: JPEG, PNG, TIFF, BMP, GIF, SVG, PSD, HEIC, HEIF
Email: EML, MSG, PST, OST
Video: MP4, MOV

---

## License

AGPL-3.0. See [LICENSE](https://github.com/franckferman/MetaDetective/blob/stable/LICENSE).

MetaDetective is provided for educational and authorized security testing purposes. You are responsible for ensuring compliance with applicable laws.

---

## Star History

<a href="https://star-history.com/#franckferman/MetaDetective&Timeline">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=franckferman/MetaDetective&type=Timeline&theme=dark" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=franckferman/MetaDetective&type=Timeline" />
  </picture>
</a>

---

## Contact

[![ProtonMail][protonmail-shield]](mailto:contact@franckferman.fr)
[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/franckferman)
[![Twitter][twitter-shield]](https://www.twitter.com/franckferman)

<p align="right"><a href="#top">Back to top</a></p>

<!-- shields -->
[contributors-shield]: https://img.shields.io/github/contributors/franckferman/MetaDetective.svg?style=for-the-badge
[forks-shield]: https://img.shields.io/github/forks/franckferman/MetaDetective.svg?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/franckferman/MetaDetective.svg?style=for-the-badge
[issues-shield]: https://img.shields.io/github/issues/franckferman/MetaDetective.svg?style=for-the-badge
[pypi-shield]: https://img.shields.io/pypi/v/MetaDetective.svg?style=for-the-badge&logo=pypi&logoColor=white
[docker-shield]: https://img.shields.io/docker/pulls/franckferman/metadetective.svg?style=for-the-badge&logo=docker&logoColor=white
[license-shield]: https://img.shields.io/github/license/franckferman/MetaDetective.svg?style=for-the-badge
[protonmail-shield]: https://img.shields.io/badge/ProtonMail-8B89CC?style=for-the-badge&logo=protonmail&logoColor=white
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=blue
[twitter-shield]: https://img.shields.io/badge/-Twitter-black.svg?style=for-the-badge&logo=twitter&colorB=blue

```

### File: docker\README.md
```md
# MetaDetective Docker Setup <a name="top"></a>

This document offers instructions on how to set up and utilize the Dockerized version of MetaDetective.

## Table of Contents

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#using-pre-built-image">Using the Pre-built Image</a></li>
    <li><a href="#dockerfile-details">Dockerfile Details</a></li>
  </ol>
</details>

## Getting Started <a name="getting-started"></a>

### Prerequisites <a name="prerequisites"></a>

- Docker must be installed on your machine.
- While the Docker image can technically be run on Windows, the provided scripts are written in Bash. Thus, they are designed for environments that support Bash scripting, like Linux.

<p align="right">(<a href="#top">🔼 Back to top</a>)</p>

### Building the Docker Image <a name="building-the-docker-image"></a>

To build and run the Docker image:
```bash
# ./start.sh
```

When executed, this script performs the following actions:
1. It checks if the metadetective-image already exists. If it doesn't, the script builds one using the provided Dockerfile.
2. It runs a container named metadetective-container.
3. Upon completion, you'll be placed inside the container shell, where you're ready to start using MetaDetective.
<p align="right">(<a href="#top">🔼 Back to top</a>)</p>

### Stopping and Removing Containers and Images <a name="stopping-and-removing-containers-and-images"></a>

In case you want to stop the running container and/or remove the Docker image:
```bash
# ./remove.sh
```

Executing this script will:
1. Stop and remove the metadetective-container if it's currently running.
2. Prompt you with the option to delete the metadetective-image.

<p align="right">(<a href="#top">🔼 Back to top</a>)</p>

## Using the Pre-built Image <a name="using-pre-built-image"></a>

If you'd rather use the pre-built Docker image from Docker Hub, follow these steps:

### Pulling the Image <a name="pulling-the-image"></a>

Retrieve the Docker image using:
```bash
# docker pull franckferman/metadetective
```

### Running the Container <a name="running-the-container"></a>

Start a container based on the image:
```bash
# docker run -it --name metadetective franckferman/metadetective /bin/bash
```

### Stopping the Container

```bash
# docker stop metadetective
```

This command will stop the container named "metadetective".

### Removing the Container

Once the container is stopped, you can remove it using:
```bash
# docker rm metadetective
```

This command will remove the container named "metadetective".

### Troubleshooting container deletion problems

1. List All Containers (including stopped ones):
```bash
# docker ps -a
```

Check if the container "metadetective" is listed. If it's listed, note the container ID.

2. Force Remove the Container:
```bash
# docker rm -f metadetective
```

Alternatively, if using the container ID:
```bash
# docker rm -f [CONTAINER_ID]
```

<p align="right">(<a href="#top">🔼 Back to top</a>)</p>

## Dockerfile Details <a name="dockerfile-details"></a>

Our Docker image is built upon the lightweight foundation of `debian:bookworm-slim`.

The following essential packages are installed:

`python3`: The core programming language for running MetaDetective.

`python3-pip`: Used specifically to fetch and install the MetaDetective release directly from PyPI.

`libimage-exiftool-perl`: MetaDetective partly relies on this tool for metadata extraction and analysis.

Due to the ENV PATH="/root/.local/bin:${PATH}" setting in the Dockerfile, you can directly launch MetaDetective within the container without needing to navigate to any specific directory. Simply invoke MetaDetective followed by the desired command-line arguments.

<p align="right">(<a href="#top">🔼 Back to top</a>)</p>

```

### File: TODO.md
```md
## TODO

### Metadata enhancements

- [X] ~~**GPS and photo metadata improvements**~~
  - [X] ~~Add missing metadata fields, especially for geolocation, camera model name, and other device-specific information for images.~~
  - [X] ~~Develop a function to convert GPS data to OSM or Google Maps links.~~
  - [X] ~~Add HEIC/HEIF support (iPhone/iPad photos with high-precision GPS data).~~

### Data export features

- [X] ~~**Support various export formats**~~
  - [X] ~~Added support for exporting data in HTML format.~~
  - [X] ~~Added support for exporting data in TXT format.~~
  - [X] ~~Added support for exporting data in JSON format.~~
  - [X] ~~Implement customizable export options for users.~~
  - [X] ~~Implement advanced customizable export options for users.~~

### GitHub Actions

- [X] ~~**PyPI Automatic Upload on Release**~~
  - [X] ~~Integrate GitHub Actions to trigger PyPI package upload on every new release.~~

### Performance Enhancements

- [X] ~~**Optimize File Comparison for Duplication Avoidance**~~
  - [X] ~~Replace SHA256 hash verification with CRC32 (zlib stdlib, 10-50x faster, sufficient for deduplication).~~

### Functionalities for Parsing

- [X] ~~**Selective field extraction**~~
  - [X] ~~Add --parse-only flag to limit extraction to specified fields only.~~

- [ ] **Advanced Parsing Features**
  - [ ] Include options for automatic modification and enrichment of data.
    - [ ] Develop feature to automatically append email aliases (domain names) to usernames.

### Advanced Filtering

- [ ] **Enhanced Filtering Capabilities**
  - [X] ~~Add support for scraping filter options.~~
  - [ ] Implement local filtering based on sections like "Author" and "Last Modified By".
    - [ ] Add --filter-field to filter entire file entries by field value (distinct from --ignore which filters values, and --parse-only which filters fields).

### Testing

- [ ] **Expand unit test coverage**
  - [ ] Add tests for MetadataExtractor, GPSProcessor, AddressResolver.
  - [ ] Add tests for MetadataExporter (HTML, TXT, JSON outputs).
  - [ ] Add tests for --parse-only and --filter-field flags.

### Website Enhancement

- [ ] **Incorporate Metadata Example Files**
  - [ ] Host a set of diverse example files embedded with metadata on the MetaDetective site.
    - [ ] Ensure these example files cover a wide range of metadata scenarios to showcase MetaDetective's capabilities.
  - [ ] Replace references to "https://example.com" in documentation and demos with links to these metadata example files on the MetaDetective site.

```

### File: docker\remove.sh
```sh
#!/bin/bash

IMAGE_NAME="metadetective-image"
CONTAINER_NAME="metadetective-container"

# Check if container is running
CONTAINER_ID=$(sudo docker ps -aqf "name=$CONTAINER_NAME" -q)

if [ ! -z "$CONTAINER_ID" ]; then
    echo "Stopping and removing the $CONTAINER_NAME container..."
    if ! sudo docker rm -f $CONTAINER_ID; then
        echo "Error removing container $CONTAINER_NAME." >&2
        exit 1
    fi
else
    echo "No container found: $CONTAINER_NAME"
fi

# Check if image exists
IMAGE_EXISTS=$(sudo docker images -q $IMAGE_NAME)

if [ ! -z "$IMAGE_EXISTS" ]; then
    read -p "Do you also want to delete the Docker image ($IMAGE_NAME)? [y/N] " response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        if ! sudo docker rmi $IMAGE_EXISTS; then
            echo "Error deleting Docker image $IMAGE_NAME." >&2
            exit 1
        fi
        echo "Docker image $IMAGE_NAME deleted."
    fi
else
    echo "No Docker image found: $IMAGE_NAME"
fi


```

### File: docker\start.sh
```sh
#!/bin/bash

IMAGE_NAME="metadetective-image"
CONTAINER_NAME="metadetective-container"

# Check if image exists
IMAGE_EXISTS=$(sudo docker images -q $IMAGE_NAME)

if [ -z "$IMAGE_EXISTS" ]; then
    echo "Building Docker image..."
    if ! sudo docker build -t $IMAGE_NAME .; then
        echo "Error building Docker image." >&2
        exit 1
    fi
else
    echo "Using existing Docker image..."
fi

# Check if container is running
CONTAINER_ID=$(sudo docker ps -aqf "name=$CONTAINER_NAME")

if [ ! -z "$CONTAINER_ID" ]; then
    echo "Stopping existing container..."
    sudo docker stop $CONTAINER_NAME
    echo "Removing existing container..."
    sudo docker rm $CONTAINER_NAME
fi

# Run the container
echo "Running new container..."
if ! sudo docker run -d --rm --name $CONTAINER_NAME $IMAGE_NAME; then
    echo "Error running container." >&2
    exit 1
fi

# Enter the container shell
echo "Entering container shell..."
sudo docker exec -it $CONTAINER_NAME /bin/bash


```

### File: tests\test_MetaDetective.py
```py
import argparse
import json
import os
import tempfile
import unittest
from io import StringIO
from unittest.mock import Mock, patch

from src.MetaDetective import MetaDetective as md


# ============================================================================
# Banner et exiftool
# ============================================================================

class TestShowBanner(unittest.TestCase):
    def test_show_banner_prints_banner(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            md.show_banner()
            content = mock_stdout.getvalue()
            self.assertEqual(content, md.BANNER + "\n")


class TestCheckExiftoolInstalled(unittest.TestCase):

    @patch("src.MetaDetective.MetaDetective.subprocess.run")
    def test_exiftool_is_installed_no_exit(self, mock_run):
        mock_run.return_value = Mock()
        try:
            md.check_exiftool_installed()
        except SystemExit as e:
            self.fail(f"Unexpected SystemExit: {e}")

    @patch("src.MetaDetective.MetaDetective.subprocess.run")
    def test_exiftool_not_installed_raises_system_exit(self, mock_run):
        mock_run.side_effect = FileNotFoundError()
        with self.assertRaises(SystemExit) as cm:
            md.check_exiftool_installed()
        self.assertEqual(str(cm.exception), md.EXIFTOOL_NOT_INSTALLED)

    @patch("src.MetaDetective.MetaDetective.subprocess.run")
    def test_exiftool_execution_error_raises_system_exit(self, mock_run):
        mock_run.side_effect = md.subprocess.CalledProcessError(
            returncode=1, cmd=["exiftool", "-ver"]
        )
        with self.assertRaises(SystemExit) as cm:
            md.check_exiftool_installed()
        self.assertEqual(str(cm.exception), md.EXIFTOOL_EXECUTION_ERROR)


# ============================================================================
# GPSProcessor: dms_to_dd / parse_dms
# ============================================================================

class TestGPSProcessorDmsToDd(unittest.TestCase):

    def test_north_positive(self):
        result = md.GPSProcessor.dms_to_dd(40, 26, 46, "N")
        self.assertAlmostEqual(result, 40.4461111, places=6)

    def test_south_negative(self):
        result = md.GPSProcessor.dms_to_dd(40, 26, 46, "S")
        self.assertAlmostEqual(result, -40.4461111, places=6)

    def test_east_positive(self):
        result = md.GPSProcessor.dms_to_dd(40, 26, 46, "E")
        self.assertAlmostEqual(result, 40.4461111, places=6)

    def test_west_negative(self):
        result = md.GPSProcessor.dms_to_dd(40, 26, 46, "W")
        self.assertAlmostEqual(result, -40.4461111, places=6)

    def test_invalid_degrees(self):
        with self.assertRaises(ValueError):
            md.GPSProcessor.dms_to_dd(200, 26, 46, "N")

    def test_invalid_minutes(self):
        with self.assertRaises(ValueError):
            md.GPSProcessor.dms_to_dd(40, 60, 46, "N")

    def test_invalid_seconds(self):
        with self.assertRaises(ValueError):
            md.GPSProcessor.dms_to_dd(40, 26, 60, "N")

    def test_invalid_direction(self):
        with self.assertRaises(ValueError):
            md.GPSProcessor.dms_to_dd(40, 26, 46, "A")

    def test_case_insensitive_direction(self):
        result = md.GPSProcessor.dms_to_dd(40, 26, 46, "n")
        self.assertAlmostEqual(result, 40.4461111, places=6)


class TestGPSProcessorParseDms(unittest.TestCase):

    def test_valid_dms_north(self):
        result = md.GPSProcessor.parse_dms('50 deg 49\' 8.59" N')
        self.assertEqual(result, (50, 49, 8.59, "N"))

    def test_valid_dms_east(self):
        result = md.GPSProcessor.parse_dms('50 deg 49\' 8.59" E')
        self.assertEqual(result, (50, 49, 8.59, "E"))

    def test_invalid_direction(self):
        with self.assertRaises(ValueError):
            md.GPSProcessor.parse_dms('50 deg 49\' 8.59" A')

    def test_missing_degrees(self):
        with self.assertRaises(ValueError):
            md.GPSProcessor.parse_dms('49\' 8.59" N')

    def test_missing_minutes(self):
        with self.assertRaises(ValueError):
            md.GPSProcessor.parse_dms('50 deg 8.59" N')

    def test_missing_seconds(self):
        with self.assertRaises(ValueError):
            md.GPSProcessor.parse_dms("50 deg 49' N")

    def test_case_insensitive_direction(self):
        result = md.GPSProcessor.parse_dms('50 deg 49\' 8.59" n')
        self.assertEqual(result, (50, 49, 8.59, "N"))


# ============================================================================
# MetadataExtractor + GPSProcessor.process_gps_data
# ============================================================================

class TestMetadataExtractor(unittest.TestCase):

    @patch("src.MetaDetective.MetaDetective.subprocess.run")
    def test_get_metadata_basic_fields(self, mock_run):
        mocked_output = """File Name                       : test.pdf
Author                          : Franck
Camera Model Name               : Pixel
"""
        mock_result = Mock()
        mock_result.stdout = mocked_output
        mock_run.return_value = mock_result

        metadata = md.MetadataExtractor.get_metadata(
            "test.pdf",
            ["File Name", "Author", "Camera Model Name"]
        )

        self.assertEqual(metadata["File Name"], "test.pdf")
        self.assertEqual(metadata["Author"], "Franck")
        self.assertEqual(metadata["Camera Model Name"], "Pixel")

    @patch("src.MetaDetective.MetaDetective.subprocess.run")
    def test_get_metadata_with_gps_position(self, mock_run):
        mocked_output = """GPS Position                    : 47 deg 28' 0.86" N, 10 deg 12' 13.50" E
File Name                       : gps.jpg
"""
        mock_result = Mock()
        mock_result.stdout = mocked_output
        mock_run.return_value = mock_result

        metadata = md.MetadataExtractor.get_metadata(
            "gps.jpg",
            ["File Name", "GPS Position", "Formatted GPS Position"]
        )

        self.assertIn("GPS Position", metadata)
        self.assertIn("Formatted GPS Position", metadata)
        lat, lon = metadata["Formatted GPS Position"].split(", ")
        float(lat)
        float(lon)

    @patch("src.MetaDetective.MetaDetective.subprocess.run")
    def test_get_metadata_handles_called_process_error(self, mock_run):
        mock_run.side_effect = md.subprocess.CalledProcessError(
            returncode=1, cmd=["exiftool", "badfile"]
        )
        metadata = md.MetadataExtractor.get_metadata("badfile", ["File Name"])
        self.assertEqual(metadata, {})


# ============================================================================
# AddressResolver
# ============================================================================

class TestAddressResolver(unittest.TestCase):

    @patch("src.MetaDetective.MetaDetective.http.client.HTTPSConnection")
    def test_get_address_from_coords_fetch_and_cache(self, mock_conn_cls):
        # Fake HTTP response
        conn_instance = Mock()
        mock_conn_cls.return_value = conn_instance

        response = Mock()
        response.read.return_value = json.dumps(
            {"display_name": "Somewhere, Earth"}
        ).encode("utf-8")
        conn_instance.getresponse.return_value = response

        # First call - should hit HTTP
        addr1 = md.AddressResolver.get_address_from_coords("47.0", "10.0")
        self.assertEqual(addr1, "Somewhere, Earth")
        self.assertTrue(mock_conn_cls.called)

        calls_count_after_first = mock_conn_cls.call_count

        # Second call same coords - should use cache, no new HTTPSConnection
        addr2 = md.AddressResolver.get_address_from_coords("47.0", "10.0")
        self.assertEqual(addr2, "Somewhere, Earth")
        self.assertEqual(mock_conn_cls.call_count, calls_count_after_first)

    @patch.object(md.AddressResolver, "get_address_from_coords", return_value="Somewhere, Earth")
    def test_format_gps_data_adds_address_and_map_link(self, mock_get_addr):
        metadata = {"Formatted GPS Position": "47.466906, 10.203750"}
        md.AddressResolver.format_gps_data(metadata)

        self.assertEqual(metadata["Address"], "Somewhere, Earth")
        self.assertIn("Map Link", metadata)
        self.assertIn("lat=47.466906", metadata["Map Link"])
        self.assertIn("lon=10.203750", metadata["Map Link"])
        mock_get_addr.assert_called_once()


# ============================================================================
# WebScraper.is_valid_file_link
# ============================================================================

class TestWebScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = md.WebScraper(["pdf", "jpg", "png"])

    def test_valid_file_link_pdf(self):
        self.assertTrue(
            self.scraper.is_valid_file_link("https://example.com/documents/report.pdf")
        )

    def test_valid_file_link_jpg_with_query(self):
        self.assertTrue(
            self.scraper.is_valid_file_link("https://example.com/img/photo.JPG?version=1")
        )

    def test_invalid_file_link_no_extension(self):
        self.assertFalse(
            self.scraper.is_valid_file_link("https://example.com/download")
        )

    def test_invalid_file_link_wrong_extension(self):
        self.assertFalse(
            self.scraper.is_valid_file_link("https://example.com/script.js")
        )


# ============================================================================
# FileDownloader utils (hash) - pas de HTTP
# ============================================================================

class TestFileDownloader(unittest.TestCase):

    def test_calculate_hash_is_deterministic(self):
        data = b"Hello world"
        h1 = md.FileDownloader.calculate_hash(data)
        h2 = md.FileDownloader.calculate_hash(data)
        self.assertEqual(h1, h2)
        self.assertEqual(len(h1), 8)  # CRC32 hex


# ============================================================================
# FileOperations + validation helpers
# ============================================================================

class TestFileOperations(unittest.TestCase):

    def test_filter_files_by_extension_basic(self):
        files = [
            "test1.pdf",
            "test2.docx",
            "image.jpg",
            "notes.txt",
            "archive.tar.gz",
        ]
        filtered = md.FileOperations.filter_files_by_extension(files, [".pdf", ".jpg"])
        self.assertIn("test1.pdf", filtered)
        self.assertIn("image.jpg", filtered)
        self.assertNotIn("test2.docx", filtered)
        self.assertNotIn("notes.txt", filtered)

    def test_filter_files_by_extension_type_errors(self):
        with self.assertRaises(TypeError):
            md.FileOperations.filter_files_by_extension("not_a_list", [".pdf"])
        with self.assertRaises(TypeError):
            md.FileOperations.filter_files_by_extension(["file.pdf"], "not_a_list")

    def test_get_files_from_directory_with_type_filter(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            pdf_path = os.path.join(tmpdir, "a.pdf")
            txt_path = os.path.join(tmpdir, "b.txt")
            with open(pdf_path, "w"):
                pass
            with open(txt_path, "w"):
                pass

            class Args:
                directory = tmpdir
                files = None
                type = [".pdf"]

            files = md.FileOperations.get_files(Args)
            self.assertEqual(files, [pdf_path])

    def test_get_files_from_args_files(self):
        class Args:
            directory = None
            files = ["a.pdf", "b.txt"]
            type = ["all"]

        files = md.FileOperations.get_files(Args)
        self.assertEqual(files, ["a.pdf", "b.txt"])

    def test_get_files_no_files_raises(self):
        class Args:
            directory = None
            files = []
            type = ["all"]

        with self.assertRaises(ValueError):
            md.FileOperations.get_files(Args)


class TestValidDirectory(unittest.TestCase):

    def test_valid_directory_ok(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            self.assertEqual(md.valid_directory(tmpdir), tmpdir)

    def test_invalid_directory_not_exists(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            md.valid_directory("/this/path/does/not/exist")

    def test_invalid_directory_not_a_dir(self):
        with tempfile.NamedTemporaryFile() as tmpfile:
            with self.assertRaises(argparse.ArgumentTypeError):
                md.valid_directory(tmpfile.name)


class TestValidFilename(unittest.TestCase):

    def test_valid_filename_basic(self):
        self.assertEqual(md.valid_filename("export01"), "export01")

    def test_valid_filename_with_dash_underscore(self):
        # 16 chars, termine par un alphanum, respecte MAX_FILENAME_LENGTH
        self.assertEqual(md.valid_filename("meta_detective_1"), "meta_detective_1")

    def test_invalid_filename_empty(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            md.valid_filename("")

    def test_invalid_filename_too_long(self):
        value = "a" * (md.MAX_FILENAME_LENGTH + 1)
        with self.assertRaises(argparse.ArgumentTypeError):
            md.valid_filename(value)

    def test_invalid_filename_ending_with_dash(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            md.valid_filename("export-")

    def test_invalid_filename_ending_with_underscore(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            md.valid_filename("export_")


class TestValidUrl(unittest.TestCase):

    def test_valid_http_url(self):
        url = "http://example.com/resource?id=1"
        self.assertEqual(md.valid_url(url), url)

    def test_valid_https_url(self):
        url = "https://example.com/res.pdf"
        self.assertEqual(md.valid_url(url), url)

    def test_invalid_url(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            md.valid_url("not_a_url")

        with self.assertRaises(argparse.ArgumentTypeError):
            md.valid_url("ftp://example.com/file")


# ============================================================================
# PatternMatcher.matches_any_pattern
# ============================================================================

class TestPatternMatcher(unittest.TestCase):

    def test_matches_any_pattern_true(self):
        value = "admin@example.com"
        patterns = [r"admin", r"root"]
        self.assertTrue(md.PatternMatcher.matches_any_pattern(value, patterns))

    def test_matches_any_pattern_false(self):
        value = "user@example.com"
        patterns = [r"admin", r"root"]
        self.assertFalse(md.PatternMatcher.matches_any_pattern(value, patterns))

    def test_matches_any_pattern_empty_list(self):
        self.assertFalse(md.PatternMatcher.matches_any_pattern("anything", []))


if __name__ == "__main__":
    unittest.ma
... [TRUNCATED]
```

### File: .github\ISSUE_TEMPLATE\bug-report.md
```md
---
name: Bug report
about: Your detailed bug reports are pivotal in elevating this project's quality.
  Your expertise in identifying issues is deeply valued and appreciated.
title: "[ISSUE] Problem Encountered"
labels: bug
assignees: franckferman

---

## Problem Summary
_Provide a clear and concise summary of the encountered issue._

## Steps to Reproduce
Provide a step-by-step description on how to reproduce the anomaly:

1. Command initiated: `...`
2. During the process: `....`
3. Observed issue: `....`
4. Output/response anomaly: `...`

## Expected Outcome
_Describe the anticipated result after executing the provided steps._

## Visual Evidence
If possible, attach screenshots to support your description.

## Technical Details

### Operating System

- **Linux:** [e.g. Linux root 4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u1 (2019-09-20) x86_64 GNU/Linux]
  *Retrieval:* `uname -a`

- **Windows:** [e.g. Microsoft Windows 10 Pro DevBox 10.0.15063 Multiprocessor Free 64-bit]
  *Retrieval:* 
  ```powershell
  $Properties = 'Caption', 'CSName', 'Version', 'BuildType', 'OSArchitecture'
  Get-CimInstance Win32_OperatingSystem | Select-Object $Properties | Format-Table -AutoSize
  ```

### Software Versions

- **Python**: [e.g. Python 3.11.4]
  *Retrieval:* `python3 -V`

- **Exiftool**: [e.g. 12.56]
  *Retrieval:* `exiftool -ver`

- **MetaDetective**: [e.g. 1.0.8]

### Docker (if used)

- **Image Version**: [e.g. "1.0.1"]

## Additional Information

Provide any other pertinent details or context regarding the issue.

```

### File: .github\ISSUE_TEMPLATE\feature-request.md
```md
---
name: Feature request
about: Clearly outline the primary goal of this feature request.
title: "[FEATURE]"
labels: enhancement
assignees: franckferman

---

**Problem Nexus:**
_Can you link this feature request to an existing problem or limitation?_
Provide a precise and thorough depiction of the issue. For instance, "The current workflow requires manual data entry, leading to inefficiencies and potential for error."

**Envisioned Solution:**
_Detail the desired feature or enhancement._
Expound upon how you imagine this feature will function, how it will address the problem, and the advantages it will introduce.

**Alternative Strategies Assessed:**
_Have you thought of other potential solutions?_
List and briefly explain other solutions or functionalities you've considered. Highlight why they might be less optimal than your proposed solution.

**Implications and Integration:**
_How will this feature fit into the current system?_
Discuss any potential interactions with existing features, how it aligns with the project's goals, or any other relevant integrations.

**Visual Demonstrations (if applicable):**
_Do you have visual aids or mock-ups?_
Embed any diagrams, wireframes, or screenshots that can provide clarity on the desired feature's function and integration.

```

### File: docs\website\index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MetaDetective - Unleash Metadata Intelligence</title>
  <meta name="description" content="Advanced metadata extraction, web scraping, and GPS intelligence for OSINT and pentesting. Zero Python dependencies beyond exiftool.">
  <link rel="icon" type="image/png" href="favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Special+Elite&family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">

  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:          #0c0b0b;
      --surface:     #111010;
      --surface-h:   #161414;
      --border:      #201e1e;
      --border-h:    #2e2c2c;
      --red:         #b83228;
      --red-dim:     rgba(184,50,40,0.10);
      --amber:       #b87c18;
      --amber-light: #ca9535;
      --green:       #00c853;
      --green-dim:   rgba(0,200,83,0.08);
      --paper:       #c0b49a;
      --paper-dim:   #6e6350;
      --paper-faint: #2e2a24;
      --text:        #6a5f50;
      --text-md:     #9e9080;
      --text-bright: #c4b8a4;
      --type: 'Special Elite', 'Courier New', serif;
      --mono: 'JetBrains Mono', 'Courier New', monospace;
      --body: 'Inter', system-ui, sans-serif;
    }

    html { scroll-behavior: smooth; }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: var(--body);
      font-size: 15px;
      line-height: 1.7;
      overflow-x: hidden;
      border-top: 2px solid var(--red);
    }

    body::after {
      content: '';
      position: fixed; inset: 0; pointer-events: none; z-index: 9999;
      opacity: 0.025;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
      background-size: 256px 256px;
    }

    ::-webkit-scrollbar { width: 3px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb { background: var(--red); }

    /* ====== HEADER ====== */
    header {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      height: 54px; padding: 0 2rem;
      background: rgba(12,11,11,0.96);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between;
    }
    .logo-text {
      font-family: var(--type); font-size: 1.05rem;
      color: var(--text-bright); text-decoration: none; letter-spacing: .02em;
    }
    .logo-text span { color: var(--red); }

    nav { display: flex; align-items: center; gap: 2rem; }
    nav a {
      font-family: var(--mono); font-size: .72rem;
      color: var(--text); text-decoration: none;
      letter-spacing: .04em; transition: color .2s;
    }
    nav a:hover { color: var(--text-bright); }
    .nav-gh {
      padding: .3rem .85rem; border: 1px solid var(--red);
      color: var(--red) !important; border-radius: 2px;
      transition: background .2s, color .2s !important;
    }
    .nav-gh:hover { background: var(--red); color: var(--bg) !important; }

    .hamburger {
      display: none; flex-direction: column; gap: 5px;
      background: none; border: none; cursor: pointer; padding: 4px;
    }
    .hamburger span { display: block; width: 20px; height: 1.5px; background: var(--text-md); transition: .3s; }
    .hamburger.open span:nth-child(1) { transform: rotate(45deg) translate(4px,4px); }
    .hamburger.open span:nth-child(2) { opacity: 0; }
    .hamburger.open span:nth-child(3) { transform: rotate(-45deg) translate(4px,-4px); }

    .mobile-nav {
      display: none; position: fixed; top: 54px; left: 0; right: 0; z-index: 99;
      background: rgba(12,11,11,0.98); border-bottom: 1px solid var(--border);
      padding: 1.5rem 2rem; flex-direction: column; gap: 1.2rem;
    }
    .mobile-nav.open { display: flex; }
    .mobile-nav a { font-family: var(--mono); font-size: .85rem; color: var(--text-md); text-decoration: none; }

    /* ====== HERO ====== */
    #hero {
      min-height: 100vh;
      display: flex; align-items: center; justify-content: center;
      padding: 80px 2rem 4rem; position: relative;
    }
    .hero-corner {
      position: absolute;
      font-family: var(--mono); font-size: .65rem;
      color: var(--paper-faint); letter-spacing: .06em; line-height: 1.6;
    }
    .hero-corner.tl { top: 5rem; left: 2rem; }
    .hero-corner.tr { top: 5rem; right: 2rem; text-align: right; }
    .hero-corner.bl { bottom: 2rem; left: 2rem; }
    .hero-corner.br { bottom: 2rem; right: 2rem; text-align: right; }

    .stamp {
      display: inline-block; font-family: var(--type);
      font-size: .78rem; letter-spacing: .18em;
      padding: .25rem .75rem;
      border: 2.5px solid currentColor;
      text-transform: uppercase; user-select: none;
    }
    .stamp-red  { color: var(--red);   opacity: 0.65; transform: rotate(-8deg); }
    .stamp-green { color: var(--green); opacity: 0.55; transform: rotate(4deg); font-size: .68rem; }

    .hero-inner { text-align: center; max-width: 620px; width: 100%; position: relative; }
    .hero-stamps {
      display: flex; justify-content: space-between; align-items: flex-start;
      margin-bottom: 2.5rem; min-height: 40px;
    }
    .hero-logo {
      display: block; max-width: 240px; width: 75%;
      margin: 0 auto 2rem; filter: brightness(0.88);
    }
    .hero-title {
      font-family: var(--type);
      font-size: clamp(1.4rem, 4vw, 2.2rem);
      color: var(--text-bright); line-height: 1.25; margin-bottom: .4rem;
    }
    .hero-rule { width: 48px; height: 1px; background: var(--red); margin: .9rem auto 1.2rem; }
    .hero-sub {
      font-family: var(--type);
      font-size: clamp(.88rem, 2vw, 1.05rem);
      color: var(--text-md); margin-bottom: 2rem; line-height: 1.7;
    }
    .hero-badges {
      display: flex; flex-wrap: wrap; justify-content: center; gap: .5rem; margin-bottom: 2rem;
    }
    .badge {
      font-family: var(--mono); font-size: .66rem;
      padding: .18rem .6rem; border: 1px solid var(--border-h); color: var(--text);
    }
    .badge.red   { border-color: var(--red);   color: var(--red); }
    .badge.green { border-color: var(--green);  color: var(--green); }

    .hero-cta { display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem; }
    .btn { font-family: var(--mono); font-size: .8rem; padding: .6rem 1.6rem; text-decoration: none; transition: .2s; display: inline-block; letter-spacing: .04em; }
    .btn-primary { background: var(--red); color: #fff; border: 1px solid var(--red); }
    .btn-primary:hover { background: transparent; color: var(--red); }
    .btn-ghost { border: 1px solid var(--border-h); color: var(--text-md); }
    .btn-ghost:hover { border-color: var(--text-md); color: var(--text-bright); }

    /* ====== BRIEF ====== */
    #brief {
      padding: 5rem 2rem;
      border-top: 1px solid var(--border);
    }
    .brief-inner {
      max-width: 800px; margin: 0 auto;
      display: grid; grid-template-columns: auto 1fr; gap: 3rem; align-items: center;
    }
    .brief-label {
      writing-mode: vertical-rl; transform: rotate(180deg);
      font-family: var(--mono); font-size: .68rem;
      color: var(--red); letter-spacing: .2em;
      text-transform: uppercase; white-space: nowrap;
    }
    .brief-text {
      font-family: var(--type);
      font-size: clamp(1.05rem, 2.5vw, 1.4rem);
      color: var(--text-md); line-height: 1.75;
    }
    .brief-text strong { color: var(--text-bright); }

    /* ====== SHARED SECTION STYLES ====== */
    section { padding: 5rem 2rem; }
    .container { max-width: 1080px; margin: 0 auto; }

    .section-head {
      margin-bottom: 3rem;
      display: flex; align-items: baseline; gap: 1.5rem; flex-wrap: wrap;
    }
    .section-head h2 {
      font-family: var(--type);
      font-size: clamp(1.3rem, 3vw, 1.9rem);
      color: var(--text-bright);
    }
    .case-ref {
      font-family: var(--mono); font-size: .66rem;
      color: var(--paper-faint); letter-spacing: .08em;
    }

    /* ====== EVIDENCE ====== */
    #evidence { background: #0a0909; border-top: 1px solid var(--border); }

    .evidence-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 1px; background: var(--border);
      border: 1px solid var(--border);
    }
    .exhibit {
      background: var(--surface); padding: 1.6rem;
      transition: background .2s; position: relative;
      border-left: 3px solid transparent;
    }
    .exhibit:hover { background: var(--surface-h); border-left-color: var(--amber); }
    .exhibit-tag { display: flex; align-items: center; gap: .7rem; margin-bottom: 1rem; }
    .exhibit-num {
      width: 26px; height: 26px; border: 1px solid var(--amber); border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      font-family: var(--mono); font-size: .64rem; color: var(--amber); flex-shrink: 0;
    }
    .exhibit-label {
      font-family: var(--mono); font-size: .64rem;
      color: var(--paper-faint); letter-spacing: .1em; text-transform: uppercase;
    }
    .new-tag {
      margin-left: auto; font-family: var(--mono); font-size: .6rem;
      padding: .1rem .4rem; background: var(--green-dim); color: var(--green);
    }
    .exhibit-title { font-family: var(--type); font-size: 1rem; color: var(--text-bright); margin-bottom: .5rem; }
    .exhibit-desc { font-size: .84rem; color: var(--text); line-height: 1.65; }

    /* ====== DEPLOY (INSTALL) ====== */
    #deploy { border-top: 1px solid var(--border); }

    .tabs { display: flex; border-bottom: 1px solid var(--border); }
    .tab {
      font-family: var(--mono); font-size: .75rem;
      padding: .6rem 1.2rem; color: var(--text);
      cursor: pointer; border-bottom: 2px solid transparent;
      transition: .2s; user-select: none; letter-spacing: .03em;
    }
    .tab:hover { color: var(--text-bright); }
    .tab.active { color: var(--amber-light); border-bottom-color: var(--amber); }

    .terminal { background: #080707; border: 1px solid var(--border); border-top: none; }
    .term-bar {
      background: #0f0e0e; padding: .5rem 1rem;
      display: flex; align-items: center; gap: .5rem;
      border-bottom: 1px solid var(--border);
    }
    .dot { width: 9px; height: 9px; border-radius: 50%; }
    .dot-r { background: #ff5f57; } .dot-y { background: #febc2e; } .dot-g { background: #28c840; }
    .term-title { font-family: var(--mono); font-size: .67rem; color: var(--paper-faint); margin: 0 auto; }
    .term-body { padding: 1.4rem 1.6rem; overflow-x: auto; }

    .tab-content { display: none; }
    .tab-content.active { display: block; }

    pre {
      font-family: var(--mono); font-size: .8rem;
      line-height: 1.9; color: var(--text-md);
      white-space: pre; overflow-x: auto;
    }
    .cm { color: #3e3830; font-style: italic; }
    .cp { color: var(--green); }
    .cc { color: var(--text-bright); }
    .cf { color: var(--amber-light); }
    .cv { color: #7aa8d4; }
    .cs { color: #c4a84a; }

    /* ====== PROTOCOLS (USAGE) ====== */
    #protocols { background: #0a0909; border-top: 1px solid var(--border); }

    .protocol-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(440px, 1fr));
      gap: 1.5rem;
    }
    .protocol-card { background: var(--surface); border: 1px solid var(--border); }
    .protocol-head {
      background: #0f0e0e; padding: .5rem 1rem;
      display: flex; align-items: center; gap: .5rem;
      border-bottom: 1px solid var(--border);
    }
    .protocol-title { font-family: var(--mono); font-size: .68rem; color: var(--paper-faint); margin-left: .3rem; }
    .protocol-body { padding: 1.2rem 1.4rem; overflow-x: auto; }

    /* ====== FAQ ====== */
    #interrogation { border-top: 1px solid var(--border); }

    .faq-wrap { max-width: 780px; }
    .faq-item { border-bottom: 1px solid var(--border); }
    .faq-q {
      width: 100%; text-align: left; background: none; border: none; cursor: pointer;
      display: flex; align-items: flex-start; justify-content: space-between; gap: 1rem;
      padding: 1.1rem 0;
    }
    .faq-q-text {
      font-family: var(--type); font-size: .96rem;
      color: var(--text-md); text-align: left; line-height: 1.4; transition: color .2s;
    }
    .faq-q:hover .faq-q-text { color: var(--text-bright); }
    .faq-item.open .faq-q-text { color: var(--amber-light); }
    .faq-q-icon {
      font-family: var(--mono); font-size: .7rem;
      color: var(--red); flex-shrink: 0; margin-top: .2rem;
      transition: transform .3s;
    }
    .faq-item.open .faq-q-icon { transform: rotate(90deg); }
    .faq-a { max-height: 0; overflow: hidden; transition: max-height .35s ease; font-size: .86rem; color: var(--text); line-height: 1.7; }
    .faq-item.open .faq-a { max-height: 500px; }
    .faq-a-inner { padding: 0 0 1rem; }
    .hi { color: var(--amber-light); font-family: var(--mono); font-size: .84em; }

    /* ====== CTA ====== */
    #cta { background: #0a0909; border-top: 1px solid var(--border); }
    .cta-inner { max-width: 560px; margin: 0 auto; text-align: center; }
    .cta-stamp { margin-bottom: 1.5rem; }
    .cta-inner h2 { font-family: var(--type); font-size: clamp(1.3rem, 3vw, 1.9rem); color: var(--text-bright); margin-bottom: .8rem; }
    .cta-inner p { font-size: .9rem; margin-bottom: 2rem; }
    .cta-links { display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem; }

    /* ====== FOOTER ====== */
    footer { padding: 2.5rem 2rem; border-top: 1px solid var(--border); }
    .footer-inner {
      max-width: 1080px; margin: 0 auto;
      display: flex; align-items: flex-start; justify-content: space-between; flex-wrap: wrap; gap: 2rem;
    }
    .footer-brand .logo-text { display: block; margin-bottom: .6rem; }
    .footer-brand p { font-size: .8rem; max-width: 280px; }
    .footer-links { display: flex; gap: 3rem; flex-wrap: wrap; }
    .footer-col h4 { font-family: var(--mono); font-size: .7rem; color: var(--text-bright); margin-bottom: .8rem; letter-spacing: .08em; }
    .footer-col ul { list-style: none; }
    .footer-col li { margin-bottom: .4rem; }
    .footer-col a { font-size: .8rem; color: var(--text); text-decoration: none; transition: color .2s; }
    .footer-col a:hover { color: var(--amber-light); }
    .footer-bottom {
      max-width: 1080px; margin: 2rem auto 0;
      padding-top: 1.2rem; border-top: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: .5rem;
    }
    .footer-bottom span { f
... [TRUNCATED]
```

