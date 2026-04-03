---
id: github.com-bextuychiev-automated-price-tracking-0c
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:33.884748
---

# KNOWLEDGE EXTRACT: github.com_BexTuychiev_automated-price-tracking_0c4104f6
> **Extracted on:** 2026-04-01 16:57:41
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007525441/github.com_BexTuychiev_automated-price-tracking_0c4104f6

---

## File: `.gitignore`
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
brain/knowledge/docs_legacy/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/brain/knowledge/docs_legacy/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
test.py
test.ipynb
sample_projects
firecrawl_output
firecrawl_repo
sample_projects
.DS_Store
data/price_history.db
```

## File: `.markdownlint.json`
```json
{
  "MD041": false,
  "MD029": false,
  "MD013": false
}
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

## File: `README.md`
```markdown
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

## File: `pyproject.toml`
```
[tool.poetry]
name = "automated_price_tracking"
version = "0.1.0"
description = ""
authors = ["BexTuychiev <bex@ibexprogramming.com>"]
readme = "README.md"
packages = [{include = "src"}]
package-mode = true

[tool.poetry.dependencies]
python = "^3.10"
streamlit = "^1.40.2"
pandas = "^2.2.3"
pydantic = "^2.10.2"
pydantic-settings = "^2.6.1"
sqlalchemy = "2.0.35"
aiohttp = "^3.11.8"
python-dotenv = "^1.0.1"
firecrawl-py = "^1.6.1"
requests = "^2.32.3"
plotly = "^5.24.1"
psycopg2-binary = "^2.9.10"


[tool.poetry.group.dev.dependencies]
pytest = "^8.3.4"
pytest-asyncio = "^0.24.0"
ipykernel = "^6.29.5"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.pytest.ini_options]
asyncio_mode = "strict"
asyncio_fixture_loop_scope = "function"
pythonpath = ["src"]
testpaths = ["src/tests"]

[tool.poetry.scripts]
app = "src.main:main"
```

## File: `requirements.txt`
```
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

## File: `streamlit_app.py`
```python
import os
import streamlit as st
from dotenv import load_dotenv
from src.presentation.app import main
from src.infrastructure.database.session import get_db_url

if __name__ == "__main__":
    # Force reload environment variables
    load_dotenv(override=True)

    # Debug database connection
    db_url = get_db_url()
    if not db_url or "postgres" not in db_url:
        st.error("Invalid database URL. Please check your .env file.")
        st.stop()

    main()
```

## File: `src/__init__.py`
```python
"""
Automated Price Tracking Package
"""
```

## File: `src/check_prices.py`
```python
import asyncio
import warnings

from src.infrastructure.database import get_session
from src.infrastructure.repositories.product_repository import ProductRepository
from src.services.price_service import PriceService


async def main():
    session = next(get_session())
    repository = ProductRepository(session)
    price_service = PriceService(repository)
    try:
        updated_products = await price_service.check_prices()
        print(f"Successfully checked prices for {len(updated_products)} products")
    except Exception as e:
        print(f"Error checking prices: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    asyncio.run(main())
```

## File: `src/config.py`
```python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    FIRECRAWL_API_KEY: str
    DISCORD_WEBHOOK_URL: str
    PRICE_DROP_THRESHOLD: float = 0.05  # Minimum price drop percentage
    POSTGRES_URL: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
```

## File: `src/main.py`
```python
import streamlit as st
from src.presentation.app import main

if __name__ == "__main__":
    main()
```

## File: `src/test_imports.py`
```python
from src.infrastructure.repositories.product_repository import ProductRepository
from src.infrastructure.database import SessionLocal
from src.domain.models import ProductCreate, PriceHistoryCreate
from datetime import datetime

# Create a session
session = SessionLocal()

# Create repository
repo = ProductRepository(session)

try:
    # Test getting all products
    products = repo.get_all()
    print(f"Found {len(products)} products")

    # Test adding a product
    if len(products) == 0:
        test_product = ProductCreate(
            url="https://example.com/test",
            name="Test Product",
            price=99.99,
            currency="USD",
            main_image_url="https://example.com/image.jpg",
        )
        product = repo.add(test_product)
        print(f"Added test product: {product.name}")

        # Test adding price history
        price_history = PriceHistoryCreate(
            product_url=product.url, price=product.price, product_name=product.name
        )
        history = repo.add_price_history(price_history)
        print(f"Added price history: {history.price}")

    print("All tests passed!")
finally:
    session.close()
```

## File: `src/domain/models.py`
```python
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    """Schema for creating a new product"""

    url: str = Field(description="The URL of the product")
    name: str = Field(description="The product name/title")
    price: float = Field(description="The current price of the product")
    currency: str = Field(description="Currency code (USD, EUR, etc)")
    main_image_url: str = Field(description="The URL of the main image of the product")
    check_date: str

    class Config:
        from_attributes = True  # Enables ORM mode


class Product(ProductCreate):
    """Schema for reading a product"""

    pass


class PriceHistoryCreate(BaseModel):
    """Schema for creating a price history entry"""

    product_url: str
    price: float
    product_name: str

    class Config:
        from_attributes = True


class PriceHistory(PriceHistoryCreate):
    """Schema for reading a price history entry"""

    id: int
    timestamp: datetime
```

## File: `src/infrastructure/database/__init__.py`
```python
from .models import Base, Product, PriceHistory
from .session import SessionLocal, get_session

__all__ = ["Base", "Product", "PriceHistory", "SessionLocal", "get_session"]
```

## File: `src/infrastructure/database/models.py`
```python
import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from urllib.parse import urlparse

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    url = Column(String, primary_key=True)
    name = Column(String)
    price = Column(Float)
    currency = Column(String)
    check_date = Column(String)
    main_image_url = Column(String)


class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True)
    product_url = Column(String, index=True)
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    product_name = Column(String)
```

## File: `src/infrastructure/database/session.py`
```python
import os
from urllib.parse import urlparse

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base

load_dotenv()


def get_db_url():
    """Get database URL with fallback to SQLite for local development"""
    db_url = os.getenv("POSTGRES_URL")
    if db_url:
        try:
            # Clean up any quotes from the URL string
            db_url = db_url.strip('"').strip("'")

            result = urlparse(db_url)
            if result.scheme in ["postgres", "postgresql"]:
                # Ensure we're using the correct scheme
                db_url = db_url.replace("postgres://", "postgresql://", 1)

                # Add required connection parameters
                if "?" not in db_url:
                    db_url += "?sslmode=require"

                return db_url
        except Exception as e:
            print(f"Error parsing database URL: {e}")
            return None

    return "sqlite:///data/price_history.db"


engine = create_engine(
    get_db_url(),
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    connect_args={"connect_timeout": 30},  # Add connection timeout
)

SessionLocal = sessionmaker(bind=engine)

# Create tables if they don't exist
Base.metadata.create_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
```

## File: `src/infrastructure/repositories/base.py`
```python
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    """Base repository interface"""

    @abstractmethod
    def add(self, entity: T) -> T:
        """Add a new entity"""
        pass

    @abstractmethod
    def get(self, id: str) -> Optional[T]:
        """Get an entity by id"""
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        """Get all entities"""
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        """Delete an entity"""
        pass
```

## File: `src/infrastructure/repositories/product_repository.py`
```python
from datetime import datetime
from typing import List, Optional

from sqlalchemy import desc
from sqlalchemy.orm import Session

from src.domain.models import Product, ProductCreate, PriceHistory, PriceHistoryCreate
from .base import BaseRepository
from ..database.models import Product as DBProduct, PriceHistory as DBPriceHistory


class ProductRepository(BaseRepository[Product]):
    def __init__(self, session: Session):
        self.session = session

    def _to_domain(self, db_product: DBProduct) -> Product:
        """Convert DB model to domain model"""
        return Product.model_validate(db_product)

    def _to_db(self, product: ProductCreate) -> DBProduct:
        """Convert domain model to DB model"""
        return DBProduct(**product.model_dump())

    def add(self, product: ProductCreate) -> Product:
        """Add a new product"""
        db_product = self._to_db(product)
        self.session.add(db_product)
        self.session.commit()
        return self._to_domain(db_product)

    def get(self, id: str) -> Optional[Product]:
        """Get a product by URL (our ID)"""
        db_product = self.session.query(DBProduct).filter_by(url=id).first()
        return self._to_domain(db_product) if db_product else None

    def get_all(self) -> List[Product]:
        """Get all products"""
        db_products = self.session.query(DBProduct).all()
        return [self._to_domain(p) for p in db_products]

    def delete(self, id: str) -> None:
        """Delete a product and its price history"""
        product = self.session.query(DBProduct).filter_by(url=id).first()
        if product:
            self.session.query(DBPriceHistory).filter_by(product_url=id).delete()
            self.session.delete(product)
            self.session.commit()

    def _to_price_history_domain(
        self, db_price_history: DBPriceHistory
    ) -> PriceHistory:
        """Convert DB price history to domain model"""
        return PriceHistory.model_validate(db_price_history)

    def _to_price_history_db(self, price_history: PriceHistoryCreate) -> DBPriceHistory:
        """Convert domain price history to DB model"""
        return DBPriceHistory(**price_history.model_dump())

    def get_price_history(self, product_url: str) -> List[PriceHistory]:
        """Get price history for a product"""
        db_histories = (
            self.session.query(DBPriceHistory)
            .filter_by(product_url=product_url)
            .order_by(DBPriceHistory.timestamp.asc())
            .all()
        )
        return [self._to_price_history_domain(h) for h in db_histories]

    def add_price_history(self, price_history: PriceHistoryCreate) -> PriceHistory:
        """Add a new price history entry"""
        db_price_history = self._to_price_history_db(price_history)
        self.session.add(db_price_history)
        self.session.commit()
        return self._to_price_history_domain(db_price_history)

    def update(self, product: Product) -> Product:
        """Update a product in the database"""
        db_product = (
            self.session.query(DBProduct).filter(DBProduct.url == product.url).first()
        )
        if db_product:
            db_product.price = product.price
            db_product.name = product.name
            db_product.currency = product.currency
            db_product.main_image_url = product.main_image_url
            db_product.check_date = datetime.now().isoformat()
            self.session.commit()
            return product
        raise ValueError(f"Product with URL {product.url} not found")
```

## File: `src/presentation/app.py`
```python
import os
import sys

import streamlit as st

from src.infrastructure.database import get_session
from src.infrastructure.repositories.product_repository import ProductRepository
from src.presentation.components.product_list import ProductList
from src.presentation.components.sidebar import Sidebar
from src.services.price_service import PriceService
from src.services.product_service import ProductService


def init_services():
    """Initialize services with dependencies"""
    session = next(get_session())
    repository = ProductRepository(session)
    product_service = ProductService(repository)
    price_service = PriceService(repository)
    return product_service, price_service


def render_dashboard(product_service: ProductService, price_service: PriceService):
    st.title("Price Tracker Dashboard")

    # Give a brief info about the app
    st.markdown(
        """##### Track product prices across e-commerce sites and get Discord notifications when prices drop. See setup instructions in the [GitHub repo](https://github.com/BexTuychiev/automated-price-tracking). View my tracked products below.
        """
    )

    # Render sidebar
    sidebar = Sidebar(product_service)
    sidebar.render()

    # Main content
    st.header("Tracked Products")
    st.markdown("---")

    products = product_service.repository.get_all()

    if not products:
        st.info("No products are being tracked. Add some using the sidebar!")
    else:
        product_list = ProductList(product_service)
        product_list.render(products)


def main():
    st.set_page_config(page_title="Price Tracker", page_icon="📊", layout="wide")

    # Disable file watcher in Streamlit Cloud
    if os.getenv("STREAMLIT_SERVER_ADDRESS"):
        st.set_option("server.fileWatcherType", "none")

    # Initialize services
    product_service, price_service = init_services()

    # Render dashboard
    render_dashboard(product_service, price_service)


if __name__ == "__main__":
    main()
```

## File: `src/presentation/components/price_chart.py`
```python
import plotly.express as px


class PriceChart:
    def create(self, price_history):
        fig = px.line(price_history, x="timestamp", y="price", title=None)
        fig.update_layout(
            xaxis_title=None,
            yaxis_title="Price ($)",
            showlegend=False,
            margin=dict(l=0, r=0, t=0, b=0),
            height=300,
        )
        fig.update_xaxes(tickformat="%Y-%m-%d %H:%M", tickangle=45)
        fig.update_yaxes(tickprefix="$", tickformat=".2f")
        return fig
```

## File: `src/presentation/components/product_list.py`
```python
import pandas as pd
import plotly.express as px
import streamlit as st
from sqlalchemy import desc

from src.services.product_service import ProductService
from .price_chart import PriceChart


class ProductList:
    def __init__(self, product_service: ProductService):
        self.product_service = product_service
        self.price_chart = PriceChart()

    def render(self, products):
        for product in products:
            with st.container():
                st.markdown(f"#### {product.name}")

                col1, col2, col3 = st.columns([1, 3, 1])

                # Display product image
                try:
                    col1.image(product.main_image_url, use_container_width=True)
                except Exception as e:
                    col1.error("Image could not be loaded for this product.")

                # Get price history
                price_history = self.product_service.repository.get_price_history(
                    product.url
                )

                if price_history:
                    # Convert to DataFrame for plotting
                    df = pd.DataFrame(
                        [
                            {"timestamp": ph.timestamp, "price": ph.price}
                            for ph in price_history
                        ]
                    )

                    # Create and display chart
                    fig = self.price_chart.create(df)
                    col2.plotly_chart(fig, use_container_width=True)

                    # Show current price
                    latest_price = price_history[-1].price
                    col3.metric("Current Price", f"${latest_price:.2f}", delta=None)
                else:
                    col2.info("No price history available")

                # Add visit product button
                col3.link_button("Visit Product", product.url)

                if st.button("Remove from tracking", key=f"remove_{product.url}"):
                    self.product_service.remove_product(product.url)
                    st.success("Product removed from tracking!")
                    st.rerun()
            st.markdown("--------")
```

## File: `src/presentation/components/sidebar.py`
```python
import streamlit as st
import asyncio
from src.services.product_service import ProductService


class Sidebar:
    def __init__(self, product_service: ProductService):
        self.product_service = product_service

    def render(self):
        st.sidebar.header("Add New Product")
        new_url = st.sidebar.text_input("Product URL")

        if st.sidebar.button("Add Product") and new_url:
            success, message = asyncio.run(self.product_service.add_product(new_url))
            if success:
                st.sidebar.success(message)
                st.rerun()
            else:
                st.sidebar.error(message)
```

## File: `src/scripts/cleanup_db.py`
```python
import asyncio
from sqlalchemy import text
from src.infrastructure.database import get_session


async def cleanup_database():
    """Clean up all data from the database"""
    session = next(get_session())
    try:
        # Delete price history first to avoid foreign key constraint violations
        session.execute(text("DELETE FROM price_histories"))
        session.commit()

        # Then delete products
        session.execute(text("DELETE FROM products"))
        session.commit()
        print("Database cleaned successfully!")
    except Exception as e:
        print(f"Error cleaning database: {e}")
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__":
    asyncio.run(cleanup_database())
```

## File: `src/services/notifications.py`
```python
import aiohttp
from src.config import settings


async def send_price_alert(
    product_name: str, old_price: float, new_price: float, url: str
):
    """Send a price drop alert to Discord"""
    drop_percentage = ((old_price - new_price) / old_price) * 100

    message = {
        "embeds": [
            {
                "title": "Price Drop Alert! 🎉",
                "description": f"**{product_name}**\nPrice dropped by {drop_percentage:.1f}%!\n"
                f"Old price: ${old_price:.2f}\n"
                f"New price: ${new_price:.2f}\n"
                f"[View Product]({url})",
                "color": 3066993,
            }
        ]
    }

    try:
        async with aiohttp.ClientSession() as session:
            await session.post(settings.DISCORD_WEBHOOK_URL, json=message)
    except Exception as e:
        print(f"Error sending Discord notification: {e}")
```

## File: `src/services/price_service.py`
```python
from typing import List

from firecrawl import FirecrawlApp

from src.config import settings
from src.domain.models import Product, ProductCreate, PriceHistoryCreate
from src.infrastructure.repositories.product_repository import ProductRepository
from src.services.notifications import send_price_alert


class PriceService:
    def __init__(self, product_repository: ProductRepository):
        self.repository = product_repository
        self.firecrawl = FirecrawlApp()

    async def check_prices(self) -> List[Product]:
        """Check prices for all tracked products and send alerts if needed"""
        products = self.repository.get_all()
        updated_products = []

        for product in products:
            try:
                # Get latest price
                scraped_data = self.firecrawl.scrape_url(
                    product.url,
                    params={
                        "formats": ["extract"],
                        "extract": {"schema": ProductCreate.model_json_schema()},
                    },
                )
                new_price = scraped_data["extract"]["price"]

                # Get earliest price from history
                price_history = self.repository.get_price_history(product.url)
                if price_history:
                    oldest_price = price_history[
                        0
                    ].price  # Compare with first (oldest) price
                    if oldest_price > new_price:
                        drop_pct = (oldest_price - new_price) / oldest_price

                        if drop_pct >= settings.PRICE_DROP_THRESHOLD:
                            await send_price_alert(
                                product.name,
                                oldest_price,
                                new_price,
                                product.url,
                            )

                # Save new price history BEFORE updating product
                price_history = PriceHistoryCreate(
                    product_url=product.url,
                    price=new_price,
                    product_name=product.name,
                )
                self.repository.add_price_history(price_history)

                # Update product price in database
                product.price = new_price
                self.repository.update(product)

                updated_products.append(product)

            except Exception as e:
                print(f"Error checking price for {product.url}: {e}")
                continue

        return updated_products
```

## File: `src/services/product_service.py`
```python
from typing import Tuple
from datetime import datetime
from urllib.parse import urlparse

from firecrawl import FirecrawlApp
from src.domain.models import ProductCreate, PriceHistoryCreate
from src.infrastructure.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.repository = product_repository
        self.firecrawl = FirecrawlApp()

    async def add_product(self, url: str) -> Tuple[bool, str]:
        """Add a new product to track"""
        if not self._validate_url(url):
            return False, "Please enter a valid URL"

        try:
            # Check if product exists
            existing_product = self.repository.get(url)
            if existing_product:
                return False, "Product already being tracked!"

            # Scrape product
            scraped_product = await self._scrape_product(url)

            # Create product
            product = self.repository.add(scraped_product)

            # Add initial price history
            price_history = PriceHistoryCreate(
                product_url=product.url, price=product.price, product_name=product.name
            )
            self.repository.add_price_history(price_history)

            return (
                True,
                f"Added and checked initial price for: {product.name} - ${product.price:.2f}",
            )

        except Exception as e:
            print(f"Error: {str(e)}")
            return False, f"Error adding product: {str(e)}"

    def _validate_url(self, url: str) -> bool:
        """Validate URL format"""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    async def _scrape_product(self, url: str) -> ProductCreate:
        """Scrape product details"""
        data = self.firecrawl.scrape_url(
            url,
            params={
                "formats": ["extract"],
                "extract": {"schema": ProductCreate.model_json_schema()},
            },
        )
        product_data = data["extract"]
        product_data["url"] = url  # Use original URL
        product_data["check_date"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        return ProductCreate(**product_data)

    def remove_product(self, url: str) -> None:
        """Remove a product and its price history"""
        product = self.repository.get(url)
        if product:
            self.repository.delete(url)
```

## File: `src/tests/conftest.py`
```python
import os
import sys

# Add the src directory to Python path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, src_path)
```

## File: `src/tests/test_notification.py`
```python
import asyncio
import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.services.notifications import send_price_alert


async def test():
    await send_price_alert(
        product_name="Test Product",
        old_price=99.99,
        new_price=79.99,
        url="https://www.amazon.com/dp/B09HMV6K1W",
    )


if __name__ == "__main__":
    asyncio.run(test())
```

## File: `src/tests/test_price_service.py`
```python
import pytest
from unittest.mock import Mock, patch
from sqlalchemy import text
from datetime import datetime

from src.infrastructure.repositories.product_repository import ProductRepository
from src.infrastructure.database import SessionLocal
from src.services.price_service import PriceService
from src.domain.models import Product, PriceHistoryCreate


@pytest.fixture(autouse=True)
def cleanup_database():
    session = SessionLocal()
    try:
        session.execute(text("DELETE FROM price_history"))
        session.execute(text("DELETE FROM products"))
        session.commit()
    finally:
        session.close()


@pytest.fixture
def session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def repository(session):
    return ProductRepository(session)


@pytest.fixture
def mock_firecrawl():
    with patch("services.price_service.FirecrawlApp") as mock:
        app_instance = Mock()

        # Create a mock coroutine for price drop test
        async def mock_scrape_drop(*args, **kwargs):
            return {
                "extract": {
                    "url": "https://www.amazon.com/dp/B09HMV6K1W",
                    "name": "Test Product",
                    "price": 79.99,  # Lower price to trigger alert
                    "currency": "USD",
                    "main_image_url": "https://example.com/image.jpg",
                }
            }

        # Create a mock coroutine for no price drop test
        async def mock_scrape_no_drop(*args, **kwargs):
            return {
                "extract": {
                    "url": "https://www.amazon.com/dp/B09HMV6K1W",
                    "name": "Test Product",
                    "price": 99.99,  # Same price as initial
                    "currency": "USD",
                    "main_image_url": "https://example.com/image.jpg",
                }
            }

        app_instance.scrape_url = mock_scrape_drop  # Default to price drop scenario
        mock.return_value = app_instance

        def switch_to_no_drop():
            app_instance.scrape_url = mock_scrape_no_drop

        mock.switch_to_no_drop = switch_to_no_drop
        yield mock


@pytest.fixture
def service(repository, mock_firecrawl):
    return PriceService(repository)


@pytest.mark.asyncio
async def test_check_prices_no_products(service):
    """Test checking prices when no products exist"""
    updated_products = await service.check_prices()
    assert len(updated_products) == 0


@pytest.mark.asyncio
async def test_check_prices_with_price_drop(service, repository):
    """Test checking prices with a price drop that triggers alert"""
    # Add a test product
    test_product = Product(
        url="https://www.amazon.com/dp/B09HMV6K1W",
        name="Test Product",
        price=99.99,
        currency="USD",
        check_date=datetime.now().isoformat(),
        main_image_url="https://example.com/image.jpg",
    )
    repository.add(test_product)

    # Add initial price history
    price_history = PriceHistoryCreate(
        product_url=test_product.url,
        price=test_product.price,
        product_name=test_product.name,
    )
    repository.add_price_history(price_history)

    # Mock the send_price_alert function
    with patch("services.price_service.send_price_alert") as mock_alert:
        mock_alert.return_value = None  # Mock the coroutine return
        updated_products = await service.check_prices()

        # Verify results
        assert len(updated_products) == 1
        assert mock_alert.called
        mock_alert.assert_called_once_with(
            "Test Product", 99.99, 79.99, "https://www.amazon.com/dp/B09HMV6K1W"
        )

        # Verify new price history was added
        histories = repository.get_price_history(test_product.url)
        assert len(histories) == 2
        assert histories[-1].price == 79.99


@pytest.mark.asyncio
async def test_check_prices_no_price_drop(service, repository, mock_firecrawl):
    """Test checking prices without a price drop"""
    # Switch to no price drop scenario
    mock_firecrawl.switch_to_no_drop()

    # Add a test product
    test_product = Product(
        url="https://www.amazon.com/dp/B09HMV6K1W",
        name="Test Product",
        price=99.99,
        currency="USD",
        check_date=datetime.now().isoformat(),
        main_image_url="https://example.com/image.jpg",
    )
    repository.add(test_product)

    # Add initial price history
    price_history = PriceHistoryCreate(
        product_url=test_product.url,
        price=test_product.price,
        product_name=test_product.name,
    )
    repository.add_price_history(price_history)

    # Mock the send_price_alert function
    with patch("services.price_service.send_price_alert") as mock_alert:
        updated_products = await service.check_prices()

        # Verify results
        assert len(updated_products) == 1
        assert not mock_alert.called

        # Verify new price history was added
        histories = repository.get_price_history(test_product.url)
        assert len(histories) == 2
        assert histories[-1].price == 99.99
```

## File: `src/tests/test_product_service.py`
```python
import pytest
from unittest.mock import Mock, patch
from sqlalchemy import text
from src.infrastructure.repositories.product_repository import ProductRepository
from src.infrastructure.database import SessionLocal
from src.services.product_service import ProductService
from src.domain.models import ProductCreate


@pytest.fixture(autouse=True)
def cleanup_database():
    session = SessionLocal()
    try:
        # Delete all existing products and price history
        session.execute(text("DELETE FROM price_history"))
        session.execute(text("DELETE FROM products"))
        session.commit()
    finally:
        session.close()


@pytest.fixture
def session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def repository(session):
    return ProductRepository(session)


@pytest.fixture
def mock_firecrawl():
    with patch("services.product_service.FirecrawlApp") as mock:
        app_instance = Mock()
        app_instance.scrape_url.return_value = {
            "extract": {
                "url": "https://www.amazon.com/dp/B09HMV6K1W",
                "name": "Test Product",
                "price": 99.99,
                "currency": "USD",
                "main_image_url": "https://example.com/image.jpg",
            }
        }
        mock.return_value = app_instance
        yield mock


@pytest.fixture
def service(repository, mock_firecrawl):
    return ProductService(repository)


@pytest.mark.asyncio
async def test_add_product(service):
    # Test invalid URL
    success, message = await service.add_product("not-a-url")
    assert not success
    assert message == "Please enter a valid URL"

    # Test valid URL
    test_url = "https://www.example.com/product/123"
    success, message = await service.add_product(test_url)
    assert success, f"Failed to add product: {message}"
    assert "Added and checked initial price for:" in message

    # Test duplicate product
    success, message = await service.add_product(test_url)
    assert not success
    assert message == "Product already being tracked!"
```

## File: `src/tests/test_scrape.py`
```python
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

load_dotenv()

app = FirecrawlApp()

ebay_item = "https://barnerbrand.com/products/holly-glossy"

# Test scrape the ebay item
data = app.scrape_url(ebay_item)
# print(data["screenshot"])
```

