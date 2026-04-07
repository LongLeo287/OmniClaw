---
id: maptoposter
type: knowledge
owner: OA_Triage
---
# maptoposter
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# City Map Poster Generator

Generate beautiful, minimalist map posters for any city in the world.

<img src="posters/singapore_neon_cyberpunk_20260118_153328.png" width="250">
<img src="posters/dubai_midnight_blue_20260118_140807.png" width="250">

## Examples

| Country      | City           | Theme           | Poster |
|:------------:|:--------------:|:---------------:|:------:|
| USA          | San Francisco  | sunset          | <img src="posters/san_francisco_sunset_20260118_144726.png" width="250"> |
| Spain        | Barcelona      | warm_beige      | <img src="posters/barcelona_warm_beige_20260118_140048.png" width="250"> |
| Italy        | Venice         | blueprint       | <img src="posters/venice_blueprint_20260118_140505.png" width="250"> |
| Japan        | Tokyo          | japanese_ink    | <img src="posters/tokyo_japanese_ink_20260118_142446.png" width="250"> |
| India        | Mumbai         | contrast_zones  | <img src="posters/mumbai_contrast_zones_20260118_145843.png" width="250"> |
| Morocco      | Marrakech      | terracotta      | <img src="posters/marrakech_terracotta_20260118_143253.png" width="250"> |
| Singapore    | Singapore      | neon_cyberpunk  | <img src="posters/singapore_neon_cyberpunk_20260118_153328.png" width="250"> |
| Australia    | Melbourne      | forest          | <img src="posters/melbourne_forest_20260118_153446.png" width="250"> |
| UAE          | Dubai          | midnight_blue   | <img src="posters/dubai_midnight_blue_20260118_140807.png" width="250"> |
| USA          | Seattle        | emerald         | <img src="posters/seattle_emerald_20260124_162244.png" width="250"> |

## Installation

### With uv (Recommended)

Make sure [uv](https://docs.astral.sh/uv/) is installed. Running the script by prepending `uv run` automatically creates and manages a virtual environment.

```bash
# First run will automatically install dependencies
uv run ./create_map_poster.py --city "Paris" --country "France"

# Or sync dependencies explicitly first (using locked versions)
uv sync --locked
uv run ./create_map_poster.py --city "Paris" --country "France"
```

### With pip + venv

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### Generate Poster

If you're using `uv`:

```bash
uv run ./create_map_poster.py --city <city> --country <country> [options]
```

Otherwise (pip + venv):

```bash
python create_map_poster.py --city <city> --country <country> [options]
```

### Required Options

| Option | Short | Description |
|--------|-------|-------------|
| `--city` | `-c` | City name (used for geocoding) |
| `--country` | `-C` | Country name (used for geocoding) |

### Optional Flags

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| **OPTIONAL:** `--latitude` | `-lat` | Override latitude center point (use with --longitude) | |
| **OPTIONAL:** `--longitude` | `-long` | Override longitude center point (use with --latitude) | |
| **OPTIONAL:** `--country-label` | | Override country text displayed on poster | |
| **OPTIONAL:** `--theme` | `-t` | Theme name | terracotta |
| **OPTIONAL:** `--distance` | `-d` | Map radius in meters | 18000 |
| **OPTIONAL:** `--list-themes` | | List all available themes | |
| **OPTIONAL:** `--all-themes` | | Generate posters for all available themes | |
| **OPTIONAL:** `--width` | `-W` | Image width in inches | 12 (max: 20) |
| **OPTIONAL:** `--height` | `-H` | Image height in inches | 16 (max: 20) |

### Multilingual Support - i18n

Display city and country names in your language with custom fonts from google fonts:

| Option | Short | Description |
|--------|-------|-------------|
| `--display-city` | `-dc` | Custom display name for city (e.g., "東京") |
| `--display-country` | `-dC` | Custom display name for country (e.g., "日本") |
| `--font-family` | | Google Fonts family name (e.g., "Noto Sans JP") |

**Examples:**

```bash
# Japanese
python create_map_poster.py -c "Tokyo" -C "Japan" -dc "東京" -dC "日本" --font-family "Noto Sans JP"

# Korean
python create_map_poster.py -c "Seoul" -C "South Korea" -dc "서울" -dC "대한민국" --font-family "Noto Sans KR"

# Arabic
python create_map_poster.py -c "Dubai" -C "UAE" -dc "دبي" -dC "الإمارات" --font-family "Cairo"
```

**Note**: Fonts are automatically downloaded from Google Fonts and cached locally in `fonts/cache/`.

### Resolution Guide (300 DPI)

Use these values for `-W` and `-H` to target specific resolutions:

| Target | Resolution (px) | Inches (-W / -H) |
|--------|-----------------|------------------|
| **Instagram Post** | 1080 x 1080 | 3.6 x 3.6 |
| **Mobile Wallpaper** | 1080 x 1920 | 3.6 x 6.4 |
| **HD Wallpaper** | 1920 x 1080 | 6.4 x 3.6 |
| **4K Wallpaper** | 3840 x 2160 | 12.8 x 7.2 |
| **A4 Print** | 2480 x 3508 | 8.3 x 11.7 |

### Usage Examples

#### Basic Examples

```bash
# Simple usage with default theme
python create_map_poster.py -c "Paris" -C "France"

# With custom theme and distance
python create_map_poster.py -c "New York" -C "USA" -t noir -d 12000
```

#### Multilingual Examples (Non-Latin Scripts)

Display city names in their native scripts:

```bash
# Japanese
python create_map_poster.py -c "Tokyo" -C "Japan" -dc "東京" -dC "日本" --font-family "Noto Sans JP" -t japanese_ink

# Korean
python create_map_poster.py -c "Seoul" -C "South Korea" -dc "서울" -dC "대한민국" --font-family "Noto Sans KR" -t midnight_blue

# Thai
python create_map_poster.py -c "Bangkok" -C "Thailand" -dc "กรุงเทพมหานคร" -dC "ประเทศไทย" --font-family "Noto Sans Thai" -t sunset

# Arabic
python create_map_poster.py -c "Dubai" -C "UAE" -dc "دبي" -dC "الإمارات" --font-family "Cairo" -t terracotta

# Chinese (Simplified)
python create_map_poster.py -c "Beijing" -C "China" -dc "北京" -dC "中国" --font-family "Noto Sans SC"

# Khmer
python create_map_poster.py -c "Phnom Penh" -C "Cambodia" -dc "ភ្នំពេញ" -dC "កម្ពុជា" --font-family "Noto Sans Khmer"
```

#### Advanced Examples

```bash
# Iconic grid patterns
python create_map_poster.py -c "New York" -C "USA" -t noir -d 12000           # Manhattan grid
python create_map_poster.py -c "Barcelona" -C "Spain" -t warm_beige -d 8000   # Eixample district

# Waterfront & canals
python create_map_poster.py -c "Venice" -C "Italy" -t blueprint -d 4000       # Canal network
python create_map_poster.py -c "Amsterdam" -C "Netherlands" -t ocean -d 6000  # Concentric canals
python create_map_poster.py -c "Dubai" -C "UAE" -t midnight_blue -d 15000     # Palm & coastline

# Radial patterns
python create_map_poster.py -c "Paris" -C "France" -t pastel_dream -d 10000   # Haussmann boulevards
python create_map_poster.py -c "Moscow" -C "Russia" -t noir -d 12000          # Ring roads

# Organic old cities
python create_map_poster.py -c "Tokyo" -C "Japan" -t japanese_ink -d 15000    # Dense organic streets
python create_map_poster.py -c "Marrakech" -C "Morocco" -t terracotta -d 5000 # Medina maze
python create_map_poster.py -c "Rome" -C "Italy" -t warm_beige -d 8000        # Ancient layout

# Coastal cities
python create_map_poster.py -c "San Francisco" -C "USA" -t sunset -d 10000    # Peninsula grid
python create_map_poster.py -c "Sydney" -C "Australia" -t ocean -d 12000      # Harbor city
python create_map_poster.py -c "Mumbai" -C "India" -t contrast_zones -d 18000 # Coastal peninsula

# River cities
python create_map_poster.py -c "London" -C "UK" -t noir -d 15000              # Thames curves
python create_map_poster.py -c "Budapest" -C "Hungary" -t copper_patina -d 8000  # Danube split

# Override center coordinates
python create_map_poster.py --city "New York" --country "USA" -lat 40.776676 -long -73.971321 -t noir

# List available themes
python create_map_poster.py --list-themes

# Generate posters for every theme
python create_map_poster.py -c "Tokyo" -C "Japan" --all-themes
```

### Distance Guide

| Distance | Best for |
|----------|----------|
| 4000-6000m | Small/dense cities (Venice, Amsterdam center) |
| 8000-12000m | Medium cities, focused downtown (Paris, Barcelona) |
| 15000-20000m | Large metros, full city view (Tokyo, Mumbai) |

## Themes

17 themes available in `themes/` directory:

| Theme | Style |
|-------|-------|
| `gradient_roads` | Smooth gradient shading |
| `contrast_zones` | High contrast urban density |
| `noir` | Pure black background, white roads |
| `midnight_blue` | Navy background with gold roads |
| `blueprint` | Architectural blueprint aesthetic |
| `neon_cyberpunk` | Dark with electric pink/cyan |
| `warm_beige` | Vintage sepia tones |
| `pastel_dream` | Soft muted pastels |
| `japanese_ink` | Minimalist ink wash style |
| `emerald`      | Lush dark green aesthetic |
| `forest` | Deep greens and sage |
| `ocean` | Blues and teals for coastal cities |
| `terracotta` | Mediterranean warmth |
| `sunset` | Warm oranges and pinks |
| `autumn` | Seasonal burnt oranges and reds |
| `copper_patina` | Oxidized copper aesthetic |
| `monochrome_blue` | Single blue color family |

## Output

Posters are saved to `posters/` directory with format:

```text
{city}_{theme}_{YYYYMMDD_HHMMSS}.png
```

## Adding Custom Themes

Create a JSON file in `themes/` directory:

```json
{
  "name": "My Theme",
  "description": "Description of the theme",
  "bg": "#FFFFFF",
  "text": "#000000",
  "gradient_color": "#FFFFFF",
  "water": "#C0C0C0",
  "parks": "#F0F0F0",
  "road_motorway": "#0A0A0A",
  "road_primary": "#1A1A1A",
  "road_secondary": "#2A2A2A",
  "road_tertiary": "#3A3A3A",
  "road_residential": "#4A4A4A",
  "road_default": "#3A3A3A"
}
```

## Project Structure

```text
map_poster/
├── create_map_poster.py    # Main script
├── font_management.py      # Font loading and Google Fonts integration
├── themes/                 # Theme JSON files
├── fonts/                  # Font files
│   ├── Roboto-*.ttf        # Default Roboto fonts
│   └── cache/              # Downloaded Google Fonts (auto-generated)
├── posters/                # Generated posters
└── README.md
```


## Hacker's Guide

Quick reference for contributors who want to extend or modify the script.

### Contributors Guide

- Bug fixes are welcomed
- Don't submit user interface (web/desktop)
- Don't Dockerize for now
- If you vibe code any fix please test it and see before and after version of poster
- Before embarking on a big feature please ask in Discussions/Issue if it will be merged

### Architecture Overview

```text
┌─────────────────┐     ┌──────────────┐     ┌─────────────────┐
│   CLI Parser    │────▶│  Geocoding   │────▶│  Data Fetching  │
│   (argparse)    │     │  (Nominatim) │     │    (OSMnx)      │
└─────────────────┘     └──────────────┘     └─────────────────┘
                                                     │
                        ┌──────────────┐             ▼
                        │    Output    │◀────┌─────────────────┐
                        │  (matplotlib)│     │   Rendering     │
                        └──────────────┘     │  (matplotlib)   │
                                             └─────────────────┘
```

### Key Functions

| Function | Purpose | Modify when... |
|----------|---------|----------------|
| `get_coordinates()` | City → lat/lon via Nominatim | Switching geocoding provider |
| `create_poster()` | Main rendering pipeline | Adding new map layers |
| `get_edge_colors_by_type()` | Road color by OSM highway tag | Changing road styling |
| `get_edge_widths_by_type()` | Road width by importance | Adjusting line weights |
| `create_gradient_fade()` | Top/bottom fade effect | Modifying gradient overlay |
| `load_theme()` | JSON theme → dict | Adding new theme properties |
| `is_latin_script()` | Detects script for typography | Supporting new scripts |
| `load_fonts()` | Load custom/default fonts | Changing font loading logic |

### Rendering Layers (z-order)

```text
z=11  Text labels (city, country, coords)
z=10  Gradient fades (top & bottom)
z=3   Roads (via ox.plot_graph)
z=2   Parks (green polygons)
z=1   Water (blue polygons)
z=0   Background color
```

### OSM Highway Types → Road Hierarchy

```python
# In get_edge_colors_by_type() and get_edge_widths_by_type()
motorway, motorway_link     → Thickest (1.2), darkest
trunk, primary              → Thick (1.0)
secondary                   → Medium (0.8)
tertiary                    → Thin (0.6)
residential, living_street  → Thinnest (0.4), lightest
```

### Typography & Script Detection

The script automatically detects text scripts to apply appropriate typography:

- **Latin scripts** (English, French, Spanish, etc.): Letter spacing applied for elegant "P  A  R  I  S" effect
- **Non-Latin scripts** (Japanese, Arabic, Thai, Korean, etc.): Natural spacing for "東京" (no gaps between characters)

Script detection uses Unicode ranges (U+0000-U+024F for Latin). If >80% of alphabetic characters are Latin, spacing is applied.

### Adding New Features

**New map layer (e.g., railways):**

```python
# In create_poster(), after parks fetch:
try:
    railways = ox.features_from_point(point, tags={'railway': 'rail'}, dist=dist)
except:
    railways = None

# Then plot before roads:
if railways is not None and not railways.empty:
    railways = railways.to_crs(g_proj.graph["crs"])
    railways.plot(ax=ax, color=THEME['railway'], linewidth=0.5, zorder=2.5)
```

**New theme property:**

1. Add to theme JSON: `"railway": "#FF0000"`
2. Use in code: `THEME['railway']`
3. Add fallback in `load_theme()` default dict

### Typography Positioning

All text uses `transform=ax.transAxes` (0-1 normalized coordinates):

```text
y=0.14  City name (spaced letters for Latin scripts)
y=0.125 Decorative line
y=0.10  Country name
y=0.07  Coordinates
y=0.02  Attribution (bottom-right)
```

### Useful OSMnx Patterns

```python
# Get all buildings
buildings = ox.features_from_point(point, tags={'building': True}, dist=dist)

# Get specific amenities
cafes = ox.features_from_point(point, tags={'amenity': 'cafe'}, dist=dist)

# Different network types
G = ox.graph_from_point(point, dist=dist, network_type='drive')  # roads only
G = ox.graph_from_point(point, dist=dist, network_type='bike')   # bike paths
G = ox.graph_from_point(point, dist=dist, network_type='walk')   # pedestrian
```

### Performance Tips

- Large `dist` values (>20km) = slow downloads + memory heavy
- Cache coordinates locally to avoid Nominatim rate limits
- Use `network_type='drive'` instead of `'all'` for faster renders
- Reduce `dpi` from 300 to 150 for quick previews

```

### File: requirements.txt
```txt
certifi==2026.1.4
charset-normalizer==3.4.4
contourpy==1.3.3
cycler==0.12.1
flake8==7.3.0
fonttools==4.61.1
geographiclib==2.1
geopandas==1.1.2
geopy==2.4.1
idna==3.11
kiwisolver==1.4.9
lat_lon_parser==1.3.1
matplotlib==3.10.8
mccabe==0.7.0
networkx==3.6.1
numpy==2.4.0
osmnx==2.0.7
packaging==25.0
pandas==2.3.3
pillow==12.1.0
pycodestyle==2.14.0
pyflakes==3.4.0
pyogrio==0.12.1
pyparsing==3.3.1
pyproj==3.7.2
python-dateutil==2.9.0.post0
pytz==2025.2
requests==2.32.5
scipy==1.16.3
types-requests==2.32.4.20260107
shapely==2.1.2
six==1.17.0
tqdm==4.67.1
tzdata==2025.3
urllib3==2.6.3

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - Community Contributions

### Added
- **uv package manager support** ([PR #20](https://github.com/originalankur/maptoposter/pull/20))
  - Added `pyproject.toml` with project metadata and dependencies
  - Added `uv.lock` for reproducible builds
  - Added shebang to `create_map_poster.py` for direct execution
  - Updated README with uv installation instructions
- **Python version specification** - `requires-python = ">=3.11"` in pyproject.toml (fixes [#79](https://github.com/originalankur/maptoposter/issues/79))
- **Coordinate override** - `--latitude` and `--longitude` arguments to override the geocoded center point (existing from upstream PR #106, clarifies [#100](https://github.com/originalankur/maptoposter/issues/100))
  - Still requires `--city` and `--country` for display name
  - Useful for precise location control

### Fixed
- **Z-order bug** - Roads now render above parks and water features (fixes [#39](https://github.com/originalankur/maptoposter/issues/39), relates to [PR #42](https://github.com/originalankur/maptoposter/pull/42))
  - Water layer: `zorder=1` → `zorder=0.5`
  - Parks layer: `zorder=2` → `zorder=0.8`
  - Roads remain at `zorder=2` (matplotlib default), ensuring proper layering
- **Text scaling for landscape orientations** - Font size now scales based on `min(height, width)` instead of just width (fixes [#112](https://github.com/originalankur/maptoposter/issues/112))

### Changed
- Updated `.gitignore` with poster outputs, Python build artifacts, IDE files, and OS-specific files

---

## [0.3.0] - 2026-01-27 (Maintainer: @originalankur)

### Added
- **Custom coordinates support** - `--latitude` and `--longitude` arguments ([#106](https://github.com/originalankur/maptoposter/pull/106))
- **Emerald theme** - Lush dark green aesthetic with mint accents ([#114](https://github.com/originalankur/maptoposter/pull/114))
- **GitHub Actions** - PR checks workflow ([#98](https://github.com/originalankur/maptoposter/pull/98))
- **Conflict labeling** - Auto-label PRs with merge conflicts

### Changed
- **Default theme** changed from `feature_based` to `terracotta` ([#131](https://github.com/originalankur/maptoposter/pull/131))
- **Default distance** changed from 12000m to 18000m ([#128](https://github.com/originalankur/maptoposter/pull/128))
- **Max dimensions** enforced at 20 inches for width/height (supports up to 4K resolution) ([#128](https://github.com/originalankur/maptoposter/pull/128), [#129](https://github.com/originalankur/maptoposter/pull/129))

### Removed
- `feature_based` theme ([#131](https://github.com/originalankur/maptoposter/pull/131))

### Fixed
- Cache directory handling ([#109](https://github.com/originalankur/maptoposter/pull/109))
- Dynamic font scaling based on poster width

---

## [0.2.1] - 2026-01-18 (Maintainer: @originalankur)

### Added
- **SVG/PDF export** - `--format` flag for vector output ([#57](https://github.com/originalankur/maptoposter/pull/57))
- **Variable poster dimensions** - `-W` and `-H` arguments ([#59](https://github.com/originalankur/maptoposter/pull/59))
- **Caching** - Downloaded OSM data is now cached locally
- **Rate limiting** - 0.3s delay between API requests

### Fixed
- Map warping issues with variable dimensions ([#59](https://github.com/originalankur/maptoposter/pull/59))
- Edge nodes retention for complete road networks ([#27](https://github.com/originalankur/maptoposter/pull/27))
- Point geometry filtering to prevent dots on maps
- Dynamic font size adjustment for long city names
- Nominatim timeout increased to 10 seconds

### Changed
- Graph projection to linear coordinates for proper aspect ratio
- Improved cache handling with hashed filenames and error handling

---

## [0.2.0] - 2026-01-17 (Tag: v0.2)

### Added
- Example poster images in README
- Initial theme collection

---

## [0.1.0] - 2026-01-17 (Initial Release)

### Added
- Initial maptoposter source code
- README with usage instructions
- 17 built-in themes:
  - autumn, blueprint, contrast_zones, copper_patina
  - forest, gradient_roads, japanese_ink, midnight_blue
  - monochrome_blue, neon_cyberpunk, noir, ocean
  - pastel_dream, sunset, terracotta, warm_beige
- Core features:
  - City/country based map generation
  - Customizable themes via JSON
  - Road hierarchy coloring
  - Water and park feature rendering
  - Typography with Roboto font
  - Coordinate display
  - OSM attribution

```

### File: create_map_poster.py
```py
#!/usr/bin/env python3
"""
City Map Poster Generator

This module generates beautiful, minimalist map posters for any city in the world.
It fetches OpenStreetMap data using OSMnx, applies customizable themes, and creates
high-quality poster-ready images with roads, water features, and parks.
"""

import argparse
import asyncio
import json
import os
import pickle
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import cast

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import osmnx as ox
from geopandas import GeoDataFrame
from geopy.geocoders import Nominatim
from lat_lon_parser import parse
from matplotlib.font_manager import FontProperties
from networkx import MultiDiGraph
from shapely.geometry import Point
from tqdm import tqdm

from font_management import load_fonts


class CacheError(Exception):
    """Raised when a cache operation fails."""


CACHE_DIR_PATH = os.environ.get("CACHE_DIR", "cache")
CACHE_DIR = Path(CACHE_DIR_PATH)
CACHE_DIR.mkdir(exist_ok=True)

THEMES_DIR = "themes"
FONTS_DIR = "fonts"
POSTERS_DIR = "posters"

FILE_ENCODING = "utf-8"

FONTS = load_fonts()


def _cache_path(key: str) -> str:
    """
    Generate a safe cache file path from a cache key.

    Args:
        key: Cache key identifier

    Returns:
        Path to cache file with .pkl extension
    """
    safe = key.replace(os.sep, "_")
    return os.path.join(CACHE_DIR, f"{safe}.pkl")


def cache_get(key: str):
    """
    Retrieve a cached object by key.

    Args:
        key: Cache key identifier

    Returns:
        Cached object if found, None otherwise

    Raises:
        CacheError: If cache read operation fails
    """
    try:
        path = _cache_path(key)
        if not os.path.exists(path):
            return None
        with open(path, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        raise CacheError(f"Cache read failed: {e}") from e


def cache_set(key: str, value):
    """
    Store an object in the cache.

    Args:
        key: Cache key identifier
        value: Object to cache (must be picklable)

    Raises:
        CacheError: If cache write operation fails
    """
    try:
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)
        path = _cache_path(key)
        with open(path, "wb") as f:
            pickle.dump(value, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as e:
        raise CacheError(f"Cache write failed: {e}") from e


# Font loading now handled by font_management.py module


def is_latin_script(text):
    """
    Check if text is primarily Latin script.
    Used to determine if letter-spacing should be applied to city names.

    :param text: Text to analyze
    :return: True if text is primarily Latin script, False otherwise
    """
    if not text:
        return True

    latin_count = 0
    total_alpha = 0

    for char in text:
        if char.isalpha():
            total_alpha += 1
            # Latin Unicode ranges:
            # - Basic Latin: U+0000 to U+007F
            # - Latin-1 Supplement: U+0080 to U+00FF
            # - Latin Extended-A: U+0100 to U+017F
            # - Latin Extended-B: U+0180 to U+024F
            if ord(char) < 0x250:
                latin_count += 1

    # If no alphabetic characters, default to Latin (numbers, symbols, etc.)
    if total_alpha == 0:
        return True

    # Consider it Latin if >80% of alphabetic characters are Latin
    return (latin_count / total_alpha) > 0.8


def generate_output_filename(city, theme_name, output_format):
    """
    Generate unique output filename with city, theme, and datetime.
    """
    if not os.path.exists(POSTERS_DIR):
        os.makedirs(POSTERS_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    city_slug = city.lower().replace(" ", "_")
    ext = output_format.lower()
    filename = f"{city_slug}_{theme_name}_{timestamp}.{ext}"
    return os.path.join(POSTERS_DIR, filename)


def get_available_themes():
    """
    Scans the themes directory and returns a list of available theme names.
    """
    if not os.path.exists(THEMES_DIR):
        os.makedirs(THEMES_DIR)
        return []

    themes = []
    for file in sorted(os.listdir(THEMES_DIR)):
        if file.endswith(".json"):
            theme_name = file[:-5]  # Remove .json extension
            themes.append(theme_name)
    return themes


def load_theme(theme_name="terracotta"):
    """
    Load theme from JSON file in themes directory.
    """
    theme_file = os.path.join(THEMES_DIR, f"{theme_name}.json")

    if not os.path.exists(theme_file):
        print(f"⚠ Theme file '{theme_file}' not found. Using default terracotta theme.")
        # Fallback to embedded terracotta theme
        return {
            "name": "Terracotta",
            "description": "Mediterranean warmth - burnt orange and clay tones on cream",
            "bg": "#F5EDE4",
            "text": "#8B4513",
            "gradient_color": "#F5EDE4",
            "water": "#A8C4C4",
            "parks": "#E8E0D0",
            "road_motorway": "#A0522D",
            "road_primary": "#B8653A",
            "road_secondary": "#C9846A",
            "road_tertiary": "#D9A08A",
            "road_residential": "#E5C4B0",
            "road_default": "#D9A08A",
        }

    with open(theme_file, "r", encoding=FILE_ENCODING) as f:
        theme = json.load(f)
        print(f"✓ Loaded theme: {theme.get('name', theme_name)}")
        if "description" in theme:
            print(f"  {theme['description']}")
        return theme


# Load theme (can be changed via command line or input)
THEME = dict[str, str]()  # Will be loaded later


def create_gradient_fade(ax, color, location="bottom", zorder=10):
    """
    Creates a fade effect at the top or bottom of the map.
    """
    vals = np.linspace(0, 1, 256).reshape(-1, 1)
    gradient = np.hstack((vals, vals))

    rgb = mcolors.to_rgb(color)
    my_colors = np.zeros((256, 4))
    my_colors[:, 0] = rgb[0]
    my_colors[:, 1] = rgb[1]
    my_colors[:, 2] = rgb[2]

    if location == "bottom":
        my_colors[:, 3] = np.linspace(1, 0, 256)
        extent_y_start = 0
        extent_y_end = 0.25
    else:
        my_colors[:, 3] = np.linspace(0, 1, 256)
        extent_y_start = 0.75
        extent_y_end = 1.0

    custom_cmap = mcolors.ListedColormap(my_colors)

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    y_range = ylim[1] - ylim[0]

    y_bottom = ylim[0] + y_range * extent_y_start
    y_top = ylim[0] + y_range * extent_y_end

    ax.imshow(
        gradient,
        extent=[xlim[0], xlim[1], y_bottom, y_top],
        aspect="auto",
        cmap=custom_cmap,
        zorder=zorder,
        origin="lower",
    )


def get_edge_colors_by_type(g):
    """
    Assigns colors to edges based on road type hierarchy.
    Returns a list of colors corresponding to each edge in the graph.
    """
    edge_colors = []

    for _u, _v, data in g.edges(data=True):
        # Get the highway type (can be a list or string)
        highway = data.get('highway', 'unclassified')

        # Handle list of highway types (take the first one)
        if isinstance(highway, list):
            highway = highway[0] if highway else 'unclassified'

        # Assign color based on road type
        if highway in ["motorway", "motorway_link"]:
            color = THEME["road_motorway"]
        elif highway in ["trunk", "trunk_link", "primary", "primary_link"]:
            color = THEME["road_primary"]
        elif highway in ["secondary", "secondary_link"]:
            color = THEME["road_secondary"]
        elif highway in ["tertiary", "tertiary_link"]:
            color = THEME["road_tertiary"]
        elif highway in ["residential", "living_street", "unclassified"]:
            color = THEME["road_residential"]
        else:
            color = THEME['road_default']

        edge_colors.append(color)

    return edge_colors


def get_edge_widths_by_type(g):
    """
    Assigns line widths to edges based on road type.
    Major roads get thicker lines.
    """
    edge_widths = []

    for _u, _v, data in g.edges(data=True):
        highway = data.get('highway', 'unclassified')

        if isinstance(highway, list):
            highway = highway[0] if highway else 'unclassified'

        # Assign width based on road importance
        if highway in ["motorway", "motorway_link"]:
            width = 1.2
        elif highway in ["trunk", "trunk_link", "primary", "primary_link"]:
            width = 1.0
        elif highway in ["secondary", "secondary_link"]:
            width = 0.8
        elif highway in ["tertiary", "tertiary_link"]:
            width = 0.6
        else:
            width = 0.4

        edge_widths.append(width)

    return edge_widths


def get_coordinates(city, country):
    """
    Fetches coordinates for a given city and country using geopy.
    Includes rate limiting to be respectful to the geocoding service.
    """
    coords = f"coords_{city.lower()}_{country.lower()}"
    cached = cache_get(coords)
    if cached:
        print(f"✓ Using cached coordinates for {city}, {country}")
        return cached

    print("Looking up coordinates...")
    geolocator = Nominatim(user_agent="city_map_poster", timeout=10)

    # Add a small delay to respect Nominatim's usage policy
    time.sleep(1)

    try:
        location = geolocator.geocode(f"{city}, {country}")
    except Exception as e:
        raise ValueError(f"Geocoding failed for {city}, {country}: {e}") from e

    # If geocode returned a coroutine in some environments, run it to get the result.
    if asyncio.iscoroutine(location):
        try:
            location = asyncio.run(location)
        except RuntimeError as exc:
            # If an event loop is already running, try using it to complete the coroutine.
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # Running event loop in the same thread; raise a clear error.
                raise RuntimeError(
                    "Geocoder returned a coroutine while an event loop is already running. "
                    "Run this script in a synchronous environment."
                ) from exc
            location = loop.run_until_complete(location)

    if location:
        # Use getattr to safely access address (helps static analyzers)
        addr = getattr(location, "address", None)
        if addr:
            print(f"✓ Found: {addr}")
        else:
            print("✓ Found location (address not available)")
        print(f"✓ Coordinates: {location.latitude}, {location.longitude}")
        try:
            cache_set(coords, (location.latitude, location.longitude))
        except CacheError as e:
            print(e)
        return (location.latitude, location.longitude)

    raise ValueError(f"Could not find coordinates for {city}, {country}")


def get_crop_limits(g_proj, center_lat_lon, fig, dist):
    """
    Crop inward to preserve aspect ratio while guaranteeing
    full coverage of the requested radius.
    """
    lat, lon = center_lat_lon

    # Project center point into graph CRS
    center = (
        ox.projection.project_geometry(
            Point(lon, lat),
            crs="EPSG:4326",
            to_crs=g_proj.graph["crs"]
        )[0]
    )
    center_x, center_y = center.x, center.y

    fig_width, fig_height = fig.get_size_inches()
    aspect = fig_width / fig_height

    # Start from the *requested* radius
    half_x = dist
    half_y = dist

    # Cut inward to match aspect
    if aspect > 1:  # landscape → reduce height
        half_y = half_x / aspect
    else:  # portrait → reduce width
        half_x = half_y * aspect

    return (
        (center_x - half_x, center_x + half_x),
        (center_y - half_y, center_y + half_y),
    )


def fetch_graph(point, dist) -> MultiDiGraph | None:
    """
    Fetch street network graph from OpenStreetMap.

    Uses caching to avoid redundant downloads. Fetches all network types
    within the specified distance from the center point.

    Args:
        point: (latitude, longitude) tuple for center point
        dist: Distance in meters from center point

    Returns:
        MultiDiGraph of street network, or None if fetch fails
    """
    lat, lon = point
    graph = f"graph_{lat}_{lon}_{dist}"
    cached = cache_get(graph)
    if cached is not None:
        print("✓ Using cached street network")
        return cast(MultiDiGraph, cached)

    try:
        g = ox.graph_from_point(point, dist=dist, dist_type='bbox', network_type='all', truncate_by_edge=True)
        # Rate limit between requests
        time.sleep(0.5)
        try:
            cache_set(graph, g)
        except CacheError as e:
            print(e)
        return g
    except Exception as e:
        print(f"OSMnx error while fetching graph: {e}")
        return None


def fetch_features(point, dist, tags, name) -> GeoDataFrame | None:
    """
    Fetch geographic features (water, parks, etc.) from OpenStreetMap.

    Uses caching to avoid redundant downloads. Fetches features matching
    the specified OSM tags within distance from center point.

    Args:
        point: (latitude, longitude) tuple for center point
        dist: Distance in meters from center point
        tags: Dictionary of OSM tags to filter features
        name: Name for this feature type (for caching and logging)

    Returns:
        GeoDataFrame of features, or None if fetch fails
    """
    lat, lon = point
    tag_str = "_".join(tags.keys())
    features = f"{name}_{lat}_{lon}_{dist}_{tag_str}"
    cached = cache_get(features)
    if cached is not None:
        print(f"✓ Using cached {name}")
        return cast(GeoDataFrame, cached)

    try:
        data = ox.features_from_point(point, tags=tags, dist=dist)
        # Rate limit between requests
        time.sleep(0.3)
        try:
            cache_set(features, data)
        except CacheError as e:
            print(e)
        return data
    except Exception as e:
        print(f"OSMnx error while fetching features: {e}")
        return None


def create_poster(
    city,
    country,
    point,
    dist,
    output_file,
    output_format,
    width=12,
    height=16,
    country_label=None,
    name_label=None,
    display_city=None,
    display_country=None,
    fonts=None,
):
    """
    Generate a complete map poster with roads, water, parks, and typography.

    Creates a high-quality poster by fetching OSM data, rendering map layers,
    applying the current theme, and adding text labels with coordinates.

    Args:
        city: City name for display on poster
        country: Country name for display on poster
        point: (latitude, longitude) tuple for map center
        dist: Map radius in meters
        output_file: Path where poster will be saved
        output_format: File format ('png', 'svg', or 'pdf')
        width: Poster width in inches (defau
... [TRUNCATED]
```

### File: font_management.py
```py
"""
Font Management Module
Handles font loading, Google Fonts integration, and caching.
"""

import os
import re
from pathlib import Path
from typing import Optional

import requests

FONTS_DIR = "fonts"
FONTS_CACHE_DIR = Path(FONTS_DIR) / "cache"


def download_google_font(font_family: str, weights: list = None) -> Optional[dict]:
    """
    Download a font family from Google Fonts and cache it locally.
    Returns dict with font paths for different weights, or None if download fails.

    :param font_family: Google Fonts family name (e.g., 'Noto Sans JP', 'Open Sans')
    :param weights: List of font weights to download (300=light, 400=regular, 700=bold)
    :return: Dict with 'light', 'regular', 'bold' keys mapping to font file paths
    """
    if weights is None:
        weights = [300, 400, 700]

    # Create fonts cache directory
    FONTS_CACHE_DIR.mkdir(parents=True, exist_ok=True)

    # Normalize font family name for file paths
    font_name_safe = font_family.replace(" ", "_").lower()

    font_files = {}

    try:
        # Google Fonts API endpoint - request all weights at once
        weights_str = ";".join(map(str, weights))
        api_url = "https://fonts.googleapis.com/css2"

        # Use requests library for cleaner HTTP handling
        params = {"family": f"{font_family}:wght@{weights_str}"}
        headers = {
            "User-Agent": "Mozilla/5.0"  # Get .woff2 files (better compression)
        }

        # Fetch CSS file
        response = requests.get(api_url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        css_content = response.text

        # Parse CSS to extract weight-specific URLs
        # Google Fonts CSS has @font-face blocks with font-weight and src: url()
        weight_url_map = {}

        # Split CSS into font-face blocks
        font_face_blocks = re.split(r"@font-face\s*\{", css_content)

        for block in font_face_blocks[1:]:  # Skip first empty split
            # Extract font-weight
            weight_match = re.search(r"font-weight:\s*(\d+)", block)
            if not weight_match:
                continue

            weight = int(weight_match.group(1))

            # Extract URL (prefer woff2, fallback to ttf)
            url_match = re.search(r"url\((https://[^)]+\.(woff2|ttf))\)", block)
            if url_match:
                weight_url_map[weight] = url_match.group(1)

        # Map weights to our keys
        weight_map = {300: "light", 400: "regular", 700: "bold"}

        # Download each weight
        for weight in weights:
            weight_key = weight_map.get(weight, "regular")

            # Find URL for this weight
            weight_url = weight_url_map.get(weight)

            # If exact weight not found, try to find closest
            if not weight_url and weight_url_map:
                # Find closest weight
                closest_weight = min(
                    weight_url_map.keys(), key=lambda x: abs(x - weight)
                )
                weight_url = weight_url_map[closest_weight]
                print(
                    f"  Using weight {closest_weight} for {weight_key} (requested {weight} not available)"
                )

            if weight_url:
                # Determine file extension
                file_ext = "woff2" if weight_url.endswith(".woff2") else "ttf"

                # Download font file
                font_filename = f"{font_name_safe}_{weight_key}.{file_ext}"
                font_path = FONTS_CACHE_DIR / font_filename

                if not font_path.exists():
                    print(f"  Downloading {font_family} {weight_key} ({weight})...")
                    try:
                        font_response = requests.get(weight_url, timeout=10)
                        font_response.raise_for_status()
                        font_path.write_bytes(font_response.content)
                    except Exception as e:
                        print(f"  ⚠ Failed to download {weight_key}: {e}")
                        continue
                else:
                    print(f"  Using cached {font_family} {weight_key}")

                font_files[weight_key] = str(font_path)

        # Ensure we have at least regular weight
        if "regular" not in font_files and font_files:
            # Use first available as regular
            font_files["regular"] = list(font_files.values())[0]
            print(f"  Using {list(font_files.keys())[0]} weight as regular")

        # If we don't have all three weights, duplicate available ones
        if "bold" not in font_files and "regular" in font_files:
            font_files["bold"] = font_files["regular"]
            print("  Using regular weight as bold")
        if "light" not in font_files and "regular" in font_files:
            font_files["light"] = font_files["regular"]
            print("  Using regular weight as light")

        return font_files if font_files else None

    except Exception as e:
        print(f"⚠ Error downloading Google Font '{font_family}': {e}")
        return None


def load_fonts(font_family: Optional[str] = None) -> Optional[dict]:
    """
    Load fonts from local directory or download from Google Fonts.
    Returns dict with font paths for different weights.

    :param font_family: Google Fonts family name (e.g., 'Noto Sans JP', 'Open Sans').
                       If None, uses local Roboto fonts.
    :return: Dict with 'bold', 'regular', 'light' keys mapping to font file paths,
             or None if all loading methods fail
    """
    # If custom font family specified, try to download from Google Fonts
    if font_family and font_family.lower() != "roboto":
        print(f"Loading Google Font: {font_family}")
        fonts = download_google_font(font_family)
        if fonts:
            print(f"✓ Font '{font_family}' loaded successfully")
            return fonts

        print(f"⚠ Failed to load '{font_family}', falling back to local Roboto")

    # Default: Load local Roboto fonts
    fonts = {
        "bold": os.path.join(FONTS_DIR, "Roboto-Bold.ttf"),
        "regular": os.path.join(FONTS_DIR, "Roboto-Regular.ttf"),
        "light": os.path.join(FONTS_DIR, "Roboto-Light.ttf"),
    }

    # Verify fonts exist
    for _weight, path in fonts.items():
        if not os.path.exists(path):
            print(f"⚠ Font not found: {path}")
            return None

    return fonts

```

### File: test\all_variations.sh
```sh
#!/bin/bash

# This script generates variations of map posters for Bengaluru, India
# based on the options and guides described in the README.md

# Ensure we are in the project root
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR/.."

echo "===================================================="
echo "Generating All Variations for Bengaluru, India"
echo "===================================================="

# 1. Basic usage
echo "--- Basic usage ---"
uv run python3 create_map_poster.py -c "Bengaluru" -C "India"

# 2. Themes (from Distance Guide & Themes section)
echo "--- Theme Variations ---"
themes=(
    "gradient_roads" 
    "contrast_zones" 
    "noir" 
    "midnight_blue" 
    "blueprint" 
    "neon_cyberpunk" 
    "warm_beige" 
    "pastel_dream" 
    "japanese_ink" 
    "emerald" 
    "forest" 
    "ocean" 
    "terracotta" 
    "sunset" 
    "autumn" 
    "copper_patina" 
    "monochrome_blue"
)

for theme in "${themes[@]}"; do
    echo "Theme: $theme"
    uv run python3 create_map_poster.py -c "Bengaluru" -C "India" -t "$theme"
done

# 3. Optional Flags (from Optional Flags table)
echo "--- Optional Flags & Overrides ---"
echo "Overriding display name and country label"
uv run python3 create_map_poster.py -c "Bengaluru" -C "India" --display-city "The Garden City" --country-label "Karnataka, India"

echo "Overriding latitude and longitude (central Bengaluru)"
uv run python3 create_map_poster.py -c "Bengaluru" -C "India" -lat 12.9716 -long 77.5946

# 4. Multilingual Support (from i18n section)
echo "--- Multilingual Support (i18n) ---"
echo "Kannada (Native script)"
uv run python3 create_map_poster.py -c "Bengaluru" -C "India" -dc "ಬೆಂಗಳೂರು" -dC "ಭಾರत (India)" --font-family "Noto Sans Kannada"

echo "Hindi (Devanagari script)"
uv run python3 create_map_poster.py -c "Bengaluru" -C "India" -dc "बेंगलुरु" -dC "भारत" --font-family "Noto Sans Devanagari"

# 5. Resolution Guide Variations
echo "--- Resolution Guide Variations ---"
echo "Instagram Post (3.6x3.6)"
uv run python3 create_map_poster.py -c "Bengaluru" -C "India" -W 3.6 -H 3.6

echo "Mobile Wallpaper (3.6x6.4)"
uv run python3 create_map_poster.py -c "Bengaluru" -C "India" -W 3.6 -H 6.4

echo "HD Wallpaper (6.4x3.6)"
uv run python3 create_map_poster.py -c "Bengaluru" -C "India" -W 6.4 -H 3.6

echo "4K Wallpaper (12.8x7.2)"
uv run python3 create_map_poster.py -c "Bengaluru" -C "India" -W 12.8 -H 7.2

echo "A4 Print (8.3x11.7)"
uv run python3 create_map_poster.py -c "Bengaluru" -C "India" -W 8.3 -H 11.7

# 6. Distance Guide Variations
echo "--- Distance Guide Variations ---"
echo "Small/Dense focal (5000m)"
uv run python3 create_map_poster.py -c "Bengaluru" -C "India" -d 5000

echo "Medium/Focused downtown (10000m)"
uv run python3 create_map_poster.py -c "Bengaluru" -C "India" -d 10000

echo "Large metro view (default 18000m)"
uv run python3 create_map_poster.py -c "Bengaluru" -C "India" -d 18000

# 7. Utility flags
echo "--- Utility Flags ---"
echo "Listing themes"
uv run python3 create_map_poster.py --list-themes

echo "Generating for ALL themes at once"
# We'll use a smaller distance to make it faster for testing
uv run python3 create_map_poster.py -c "Bengaluru" -C "India" --all-themes -d 10000

echo "===================================================="
echo "Done! Posters saved to posters/ directory."
echo "===================================================="

```

### File: themes\autumn.json
```json
{
  "name": "Autumn",
  "description": "Burnt oranges, deep reds, golden yellows - seasonal warmth",
  "bg": "#FBF7F0",
  "text": "#8B4513",
  "gradient_color": "#FBF7F0",
  "water": "#D8CFC0",
  "parks": "#E8E0D0",
  "road_motorway": "#8B2500",
  "road_primary": "#B8450A",
  "road_secondary": "#CC7A30",
  "road_tertiary": "#D9A050",
  "road_residential": "#E8C888",
  "road_default": "#CC7A30"
}

```

### File: themes\blueprint.json
```json
{
  "name": "Blueprint",
  "description": "Classic architectural blueprint - technical drawing aesthetic",
  "bg": "#1A3A5C",
  "text": "#E8F4FF",
  "gradient_color": "#1A3A5C",
  "water": "#0F2840",
  "parks": "#1E4570",
  "road_motorway": "#E8F4FF",
  "road_primary": "#C5DCF0",
  "road_secondary": "#9FC5E8",
  "road_tertiary": "#7BAED4",
  "road_residential": "#5A96C0",
  "road_default": "#7BAED4"
}

```

### File: themes\contrast_zones.json
```json
{
  "name": "Contrast Zones",
  "description": "Strong contrast showing urban density - darker in center, lighter at edges",
  "bg": "#FFFFFF",
  "text": "#000000",
  "gradient_color": "#FFFFFF",
  "water": "#B0B0B0",
  "parks": "#ECECEC",
  "road_motorway": "#000000",
  "road_primary": "#0F0F0F",
  "road_secondary": "#252525",
  "road_tertiary": "#404040",
  "road_residential": "#5A5A5A",
  "road_default": "#404040"
}

```

### File: themes\copper_patina.json
```json
{
  "name": "Copper Patina",
  "description": "Oxidized copper aesthetic - teal-green patina with copper accents",
  "bg": "#E8F0F0",
  "text": "#2A5A5A",
  "gradient_color": "#E8F0F0",
  "water": "#C0D8D8",
  "parks": "#D8E8E0",
  "road_motorway": "#B87333",
  "road_primary": "#5A8A8A",
  "road_secondary": "#6B9E9E",
  "road_tertiary": "#88B4B4",
  "road_residential": "#A8CCCC",
  "road_default": "#88B4B4"
}

```

### File: themes\emerald.json
```json
{
    "name": "Emerald City",
    "description": "Lush dark green aesthetic with mint accents",
    "bg": "#062C22",
    "text": "#E3F9F1",
    "gradient_color": "#062C22",
    "water": "#0D4536",
    "parks": "#0F523E",
    "road_motorway": "#4ADEB0",
    "road_primary": "#2DB88F",
    "road_secondary": "#249673",
    "road_tertiary": "#1B7559",
    "road_residential": "#155C46",
    "road_default": "#155C46"
}
```

### File: themes\forest.json
```json
{
  "name": "Forest",
  "description": "Deep greens and sage tones - organic botanical aesthetic",
  "bg": "#F0F4F0",
  "text": "#2D4A3E",
  "gradient_color": "#F0F4F0",
  "water": "#B8D4D4",
  "parks": "#D4E8D4",
  "road_motorway": "#2D4A3E",
  "road_primary": "#3D6B55",
  "road_secondary": "#5A8A70",
  "road_tertiary": "#7AAA90",
  "road_residential": "#A0C8B0",
  "road_default": "#7AAA90"
}

```

### File: themes\gradient_roads.json
```json
{
  "name": "Gradient Roads",
  "description": "Smooth gradient from dark center to light edges with subtle features",
  "bg": "#FFFFFF",
  "text": "#000000",
  "gradient_color": "#FFFFFF",
  "water": "#D5D5D5",
  "parks": "#EFEFEF",
  "road_motorway": "#050505",
  "road_primary": "#151515",
  "road_secondary": "#2A2A2A",
  "road_tertiary": "#404040",
  "road_residential": "#555555",
  "road_default": "#404040"
}

```

### File: themes\japanese_ink.json
```json
{
  "name": "Japanese Ink",
  "description": "Traditional ink wash inspired - minimalist with subtle red accent",
  "bg": "#FAF8F5",
  "text": "#2C2C2C",
  "gradient_color": "#FAF8F5",
  "water": "#E8E4E0",
  "parks": "#F0EDE8",
  "road_motorway": "#8B2500",
  "road_primary": "#4A4A4A",
  "road_secondary": "#6A6A6A",
  "road_tertiary": "#909090",
  "road_residential": "#B8B8B8",
  "road_default": "#909090"
}

```

### File: themes\midnight_blue.json
```json
{
  "name": "Midnight Blue",
  "description": "Deep navy background with gold/copper roads - luxury atlas aesthetic",
  "bg": "#0A1628",
  "text": "#D4AF37",
  "gradient_color": "#0A1628",
  "water": "#061020",
  "parks": "#0F2235",
  "road_motorway": "#D4AF37",
  "road_primary": "#C9A227",
  "road_secondary": "#A8893A",
  "road_tertiary": "#8B7355",
  "road_residential": "#6B5B4F",
  "road_default": "#8B7355"
}

```

### File: themes\monochrome_blue.json
```json
{
  "name": "Monochrome Blue",
  "description": "Single blue color family with varying saturation - clean and cohesive",
  "bg": "#F5F8FA",
  "text": "#1A3A5C",
  "gradient_color": "#F5F8FA",
  "water": "#D0E0F0",
  "parks": "#E0EAF2",
  "road_motorway": "#1A3A5C",
  "road_primary": "#2A5580",
  "road_secondary": "#4A7AA8",
  "road_tertiary": "#7AA0C8",
  "road_residential": "#A8C4E0",
  "road_default": "#4A7AA8"
}

```

### File: themes\neon_cyberpunk.json
```json
{
  "name": "Neon Cyberpunk",
  "description": "Dark background with electric pink/cyan - bold night city vibes",
  "bg": "#0D0D1A",
  "text": "#00FFFF",
  "gradient_color": "#0D0D1A",
  "water": "#0A0A15",
  "parks": "#151525",
  "road_motorway": "#FF00FF",
  "road_primary": "#00FFFF",
  "road_secondary": "#00C8C8",
  "road_tertiary": "#0098A0",
  "road_residential": "#006870",
  "road_default": "#0098A0"
}

```

### File: themes\noir.json
```json
{
  "name": "Noir",
  "description": "Pure black background with white/gray roads - modern gallery aesthetic",
  "bg": "#000000",
  "text": "#FFFFFF",
  "gradient_color": "#000000",
  "water": "#0A0A0A",
  "parks": "#111111",
  "road_motorway": "#FFFFFF",
  "road_primary": "#E0E0E0",
  "road_secondary": "#B0B0B0",
  "road_tertiary": "#808080",
  "road_residential": "#505050",
  "road_default": "#808080"
}

```

### File: themes\ocean.json
```json
{
  "name": "Ocean",
  "description": "Various blues and teals - perfect for coastal cities",
  "bg": "#F0F8FA",
  "text": "#1A5F7A",
  "gradient_color": "#F0F8FA",
  "water": "#B8D8E8",
  "parks": "#D8EAE8",
  "road_motorway": "#1A5F7A",
  "road_primary": "#2A7A9A",
  "road_secondary": "#4A9AB8",
  "road_tertiary": "#70B8D0",
  "road_residential": "#A0D0E0",
  "road_default": "#4A9AB8"
}

```

### File: themes\pastel_dream.json
```json
{
  "name": "Pastel Dream",
  "description": "Soft muted pastels with dusty blues and mauves - dreamy artistic aesthetic",
  "bg": "#FAF7F2",
  "text": "#5D5A6D",
  "gradient_color": "#FAF7F2",
  "water": "#D4E4ED",
  "parks": "#E8EDE4",
  "road_motorway": "#7B8794",
  "road_primary": "#9BA4B0",
  "road_secondary": "#B5AEBB",
  "road_tertiary": "#C9C0C9",
  "road_residential": "#D8D2D8",
  "road_default": "#C9C0C9"
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
