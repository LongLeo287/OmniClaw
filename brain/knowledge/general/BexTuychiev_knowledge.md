---
id: bextuychiev-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:57.724196
---

# KNOWLEDGE EXTRACT: BexTuychiev
> **Extracted on:** 2026-03-30 17:30:49
> **Source:** BexTuychiev

---

## File: `automated-price-tracking.md`
```markdown
# 📦 BexTuychiev/automated-price-tracking [🔖 PENDING/APPROVE]
🔗 https://github.com/BexTuychiev/automated-price-tracking


## Meta
- **Stars:** ⭐ 26 | **Forks:** 🍴 7
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-11
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Track product prices across various e-commerce websites and get notified via Discord for price drops.

## README (trích đầu)
```
# Automated Price Tracking

A powerful web application that helps you track product prices across various e-commerce websites. Get notified via Discord when prices drop below your desired threshold! Perfect for deal hunters, online shoppers, and anyone looking to save money on their favorite products.

![A screenshot of the Streamlit app showing a list of tracked products with their price history charts](static/app-demo.png)

See the products I am tracking via [this Streamlit app](https://automated-price-tracker.streamlit.app/).

## Features

- 🔍 Track prices from multiple e-commerce websites simultaneously
- 📊 Visual price history tracking with interactive charts showing price trends over time
- 🔔 Customizable Discord notifications when prices drop below your target
- 🚀 Intuitive web interface built with Streamlit for easy product management
- 📈 Comprehensive historical price data storage and analysis
- ⚡ Automated price checking with configurable intervals (hourly/daily/weekly)
- 🔒 Secure data storage with PostgreSQL

## Tech Stack

- Python 3.10+ for robust backend functionality
- Streamlit for creating an interactive web interface
- PostgreSQL/SQLite for reliable data storage and retrieval
- SQLAlchemy ORM for efficient database operations
- Plotly for dynamic and interactive price history charts
- Discord Webhooks for real-time price drop notifications
- GitHub Actions for automated and scheduled price checking
- Poetry for dependency management
- Docker support for containerized deployment
- pytest for comprehensive testing

## Prerequisites

Before you begin, ensure you have:

- Python 3.10 or higher installed on your system
- Poetry package manager for dependency management
- A Discord webhook URL for receiving notifications (instructions below)
- A Firecrawl API key for reliable web scraping (sign up at firecrawl.com)
- PostgreSQL instance created online, preferably with Supabase (optional, SQLite works out of the box)
- Basic knowledge of command line operations

## Installation

1. Clone the repository:

```bash
git clone https://github.com/BexTuychiev/automated-price-tracking.git
cd automated-price-tracking
```

2. Install Poetry (if not already installed):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies:

```bash
poetry install
```

4. Create a `.env` file in the project root with the following variables:

```bash
FIRECRAWL_API_KEY=your_firecrawl_api_key
DISCORD_WEBHOOK_URL=your_discord_webhook_url
PRICE_DROP_THRESHOLD=0.05  # Change this to control notifications
POSTGRES_URL=your_postgres_url # Optional, SQLite used by default
```

> Note: You can sign up for a free Firecrawl account and get an API key [here](https://firecrawl.dev).

The app sends notifications to your private Discord server via a webhook if any of the tracked items' price drops below the `PRICE_DROP_THRESHOLD`. Instructions on how to get a Discord webhook URL are below.

Optionally, you can set up a [free Supabase Postg
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

