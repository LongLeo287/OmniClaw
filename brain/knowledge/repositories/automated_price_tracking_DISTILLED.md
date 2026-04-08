---
id: repo-fetched-automated-price-tracking-040851
type: knowledge
owner: OA
registered_at: 2026-04-05T03:38:42.204362
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_automated-price-tracking_040851

## Assimilation Report
Auto-cloned repository: FETCHED_automated-price-tracking_040851

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

Optionally, you can set up a [free Supabase Postgres instance](supabase.com) for free. I highly recommend this step because the local SQLite database will be wiped if you deploy the app to cloud platforms like Streamlit Cloud or Heroku.

## Usage

1. Start the application:

```bash
poetry run streamlit run streamlit_app.py
```

2. Add products to track:
   - Paste a product URL in the sidebar
   - Click "Add Product" to start tracking
   - The application will fetch initial price data

3. Monitor prices:
   - View price history charts for each product
   - Receive Discord notifications when prices drop
   - Remove products from tracking when needed

4. Automated price checking:
   - Prices are checked automatically every 6 hours via GitHub Actions
   - Manual checks can be triggered from the Actions tab

## Discord Webhook Setup

1. Open your Discord server settings
2. Navigate to "Integrations" → "Webhooks"
3. Click "New Webhook"
4. Name your webhook (e.g., "Price Alerts")
5. Copy the webhook URL
6. Add the URL to your `.env` file

## Online deployment

The app can be deployed to Streamlit Cloud for free:

1. Fork this repository
2. Sign up for [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app and select your forked repository
4. Add the following secrets in the app settings:
   - `FIRECRAWL_API_KEY`
   - `DISCORD_WEBHOOK_URL`
   - `PRICE_DROP_THRESHOLD`
   - `POSTGRES_URL` (recommended)
5. Deploy the app

The GitHub Actions workflow will continue to run price checks automatically in your forked repository. Make sure to add the required secrets to your repository's settings as well (Settings → Secrets and variables → Actions).

## Development

### Project Structure

```bash
automated-price-tracking/
├── src/
│ ├── domain/ # Domain models and business logic
│ ├── infrastructure/ # Database and external services
│ ├── presentation/ # UI components and views
│ ├── services/ # Business services
│ └── tests/ # Test suites
├── data/ # Local SQLite database
└── streamlit_app.py # Application entry poin
```

### Running tests

```bash
poetry run pytest
```

### Adding New Features

1. Create a new branch:

```bash
git checkout -b feature/your-feature-name
```

2. Make your changes
3. Add tests
4. Run the test suite
5. Submit a pull request

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Price tracking powered by [Firecrawl](https://firecrawl.dev)
- Notifications via Discord Webhooks
- Deployment automation with GitHub Actions

```

### File: requirements.txt
```txt
aiohappyeyeballs==2.4.4 ; python_version >= "3.10" and python_version < "4.0"
aiohttp==3.11.9 ; python_version >= "3.10" and python_version < "4.0"
aiosignal==1.3.1 ; python_version >= "3.10" and python_version < "4.0"
altair==5.5.0 ; python_version >= "3.10" and python_version < "4.0"
annotated-types==0.7.0 ; python_version >= "3.10" and python_version < "4.0"
async-timeout==5.0.1 ; python_version >= "3.10" and python_version < "3.11"
attrs==24.2.0 ; python_version >= "3.10" and python_version < "4.0"
blinker==1.9.0 ; python_version >= "3.10" and python_version < "4.0"
cachetools==5.5.0 ; python_version >= "3.10" and python_version < "4.0"
certifi==2024.8.30 ; python_version >= "3.10" and python_version < "4.0"
charset-normalizer==3.4.0 ; python_version >= "3.10" and python_version < "4.0"
click==8.1.7 ; python_version >= "3.10" and python_version < "4.0"
colorama==0.4.6 ; python_version >= "3.10" and python_version < "4.0" and platform_system == "Windows"
firecrawl-py==1.6.1 ; python_version >= "3.10" and python_version < "4.0"
frozenlist==1.5.0 ; python_version >= "3.10" and python_version < "4.0"
gitdb==4.0.11 ; python_version >= "3.10" and python_version < "4.0"
gitpython==3.1.43 ; python_version >= "3.10" and python_version < "4.0"
greenlet==3.1.1 ; python_version < "3.13" and (platform_machine == "aarch64" or platform_machine == "ppc64le" or platform_machine == "x86_64" or platform_machine == "amd64" or platform_machine == "AMD64" or platform_machine == "win32" or platform_machine == "WIN32") and python_version >= "3.10"
idna==3.10 ; python_version >= "3.10" and python_version < "4.0"
jinja2==3.1.4 ; python_version >= "3.10" and python_version < "4.0"
jsonschema-specifications==2024.10.1 ; python_version >= "3.10" and python_version < "4.0"
jsonschema==4.23.0 ; python_version >= "3.10" and python_version < "4.0"
markdown-it-py==3.0.0 ; python_version >= "3.10" and python_version < "4.0"
markupsafe==3.0.2 ; python_version >= "3.10" and python_version < "4.0"
mdurl==0.1.2 ; python_version >= "3.10" and python_version < "4.0"
multidict==6.1.0 ; python_version >= "3.10" and python_version < "4.0"
narwhals==1.15.1 ; python_version >= "3.10" and python_version < "4.0"
nest-asyncio==1.6.0 ; python_version >= "3.10" and python_version < "4.0"
numpy==2.1.3 ; python_version >= "3.10" and python_version < "4.0"
packaging==24.2 ; python_version >= "3.10" and python_version < "4.0"
pandas==2.2.3 ; python_version >= "3.10" and python_version < "4.0"
pillow==11.0.0 ; python_version >= "3.10" and python_version < "4.0"
plotly==5.24.1 ; python_version >= "3.10" and python_version < "4.0"
propcache==0.2.1 ; python_version >= "3.10" and python_version < "4.0"
protobuf==5.29.0 ; python_version >= "3.10" and python_version < "4.0"
psycopg2-binary==2.9.10 ; python_version >= "3.10" and python_version < "4.0"
pyarrow==18.1.0 ; python_version >= "3.10" and python_version < "4.0"
pydantic-core==2.27.1 ; python_version >= "3.10" and python_version < "4.0"
pydantic-settings==2.6.1 ; python_version >= "3.10" and python_version < "4.0"
pydantic==2.10.2 ; python_version >= "3.10" and python_version < "4.0"
pydeck==0.9.1 ; python_version >= "3.10" and python_version < "4.0"
pygments==2.18.0 ; python_version >= "3.10" and python_version < "4.0"
python-dateutil==2.9.0.post0 ; python_version >= "3.10" and python_version < "4.0"
python-dotenv==1.0.1 ; python_version >= "3.10" and python_version < "4.0"
pytz==2024.2 ; python_version >= "3.10" and python_version < "4.0"
referencing==0.35.1 ; python_version >= "3.10" and python_version < "4.0"
requests==2.32.3 ; python_version >= "3.10" and python_version < "4.0"
rich==13.9.4 ; python_version >= "3.10" and python_version < "4.0"
rpds-py==0.21.0 ; python_version >= "3.10" and python_version < "4.0"
six==1.16.0 ; python_version >= "3.10" and python_version < "4.0"
smmap==5.0.1 ; python_version >= "3.10" and python_version < "4.0"
sqlalchemy==2.0.35 ; python_version >= "3.10" and python_version < "4.0"
streamlit==1.40.2 ; python_version >= "3.10" and python_version < "4.0"
tenacity==9.0.0 ; python_version >= "3.10" and python_version < "4.0"
toml==0.10.2 ; python_version >= "3.10" and python_version < "4.0"
tornado==6.4.2 ; python_version >= "3.10" and python_version < "4.0"
typing-extensions==4.12.2 ; python_version >= "3.10" and python_version < "4.0"
tzdata==2024.2 ; python_version >= "3.10" and python_version < "4.0"
urllib3==2.2.3 ; python_version >= "3.10" and python_version < "4.0"
watchdog==6.0.0 ; python_version >= "3.10" and python_version < "4.0" and platform_system != "Darwin"
websockets==14.1 ; python_version >= "3.10" and python_version < "4.0"
yarl==1.18.3 ; python_version >= "3.10" and python_version < "4.0"

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for automated_price_tracking
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

