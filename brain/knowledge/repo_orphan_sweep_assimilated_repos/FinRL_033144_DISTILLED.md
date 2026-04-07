---
id: FinRL
type: knowledge
owner: OA_Triage
---
# FinRL
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">
<img align="center" width="30%" alt="image" src="https://github.com/AI4Finance-Foundation/FinGPT/assets/31713746/e0371951-1ce1-488e-aa25-0992dafcc139">
</div>

# FinRL: Financial Reinforcement Learning → FinRL-X 

<div align="center">
<img align="center" src=figs/logo_transparent_background.png width="55%"/>
</div>

[![Downloads](https://static.pepy.tech/badge/finrl)](https://pepy.tech/project/finrl)
[![Downloads](https://static.pepy.tech/badge/finrl/week)](https://pepy.tech/project/finrl)
[![Join Discord](https://img.shields.io/badge/Discord-Join-blue)](https://discord.gg/trsr8SXpW5)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![PyPI](https://img.shields.io/pypi/v/finrl.svg)](https://pypi.org/project/finrl/)
[![Documentation Status](https://readthedocs.org/projects/finrl/badge/?version=latest)](https://finrl.readthedocs.io/en/latest/?badge=latest)
![License](https://img.shields.io/github/license/AI4Finance-Foundation/finrl.svg?color=brightgreen)
![](https://img.shields.io/github/issues-raw/AI4Finance-Foundation/finrl?label=Issues)
![](https://img.shields.io/github/issues-closed-raw/AI4Finance-Foundation/finrl?label=Closed+Issues)
![](https://img.shields.io/github/issues-pr-raw/AI4Finance-Foundation/finrl?label=Open+PRs)
![](https://img.shields.io/github/issues-pr-closed-raw/AI4Finance-Foundation/finrl?label=Closed+PRs)
[![X](https://img.shields.io/badge/X-Share-black?logo=x)](https://twitter.com/intent/tweet?text=FinRL-Financial-Deep-Reinforcement-Learning%20&url=https://github.com/AI4Finance-Foundation/FinRL&hashtags=DRL,AI) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Share-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fgithub.com%2FAI4Finance-Foundation%2FFinRL)


> [!IMPORTANT]
> **FinRL-X** is the next-generation evolution of FinRL, designed for AI-native, modular, and production-oriented quantitative trading.
> 
> - **This repository (`FinRL`)** preserves the original end-to-end educational and research framework.
> - **For the latest architecture, live trading deployment, and production-focused development, please use [`FinRL-X / FinRL-Trading`](https://github.com/AI4Finance-Foundation/FinRL-Trading).**

**FinRL®** is widely recognized as the first open-source framework for financial reinforcement learning.
This repository contains the original FinRL library for education, benchmarking, and research prototyping.

For the next-generation AI-native and production-oriented trading stack, please visit **[FinRL-X / FinRL-Trading](https://github.com/AI4Finance-Foundation/FinRL-Trading)**.

## FinRL Ecosystem Roadmap

| Generation | Positioning | Target Users | Repository | Description |
|----|----|----|----|----|
| FinRL-Meta | Market Environments | Practitioners | [FinRL-Meta](https://github.com/AI4Finance-Foundation/FinRL-Meta) | Gym-style financial market environments and benchmarks |
| FinRL | Classic End-to-End Framework | Learners, Developers, Researchers | [FinRL](https://github.com/AI4Finance-Foundation/FinRL) | Original train-test-trade pipeline for financial reinforcement learning |
| ElegantRL | Algorithm Layer | Researchers and Experts | [ElegantRL](https://github.com/AI4Finance-Foundation/ElegantRL) | Lightweight and elegant DRL algorithms |
| **FinRL-X** | **Next Generation / Production** | **Professional traders, institutions, hedge funds** | [**FinRL-Trading**](https://github.com/AI4Finance-Foundation/FinRL-Trading) | **AI-native modular infrastructure for deployment-aware quantitative trading** |
> **Recommended for new users:** Start with **[FinRL-X / FinRL-Trading](https://github.com/AI4Finance-Foundation/FinRL-Trading)** if you are building modern or production-oriented trading systems.

### 🔄 FinRL-X vs. FinRL: What Changed

| Capability | FinRL (Stage 1.0) | FinRL-X (Stage 3.0) |
|---|---|---|
| **Paradigm** | Deep Reinforcement Learning | AI-Native (ML + DRL + LLM-ready) |
| **Architecture** | Three-layer coupled monolith | Fully decoupled modular layers |
| **Strategies** | DRL agents (A2C, DDPG, PPO, SAC, TD3) | ML selection + DRL timing + extensible base |
| **Data Layer** | 14 manually-wired processors | Auto-select: Yahoo Finance → FMP → WRDS |
| **Backtesting** | Custom hand-rolled evaluation loops | Professional `bt` library engine |
| **Live Trading** | Basic Alpaca support | Full multi-account integration + risk controls |
| **Configuration** | `config.py` + `config_tickers.py` | Type-safe Pydantic + `.env` multi-env |
| **Risk Management** | Gym environment constraints only | Order · portfolio · strategy-level controls |
| **Target Users** | Researchers & students | Quants, institutions, production deployments |
| **Paper** | [arXiv:2011.09607](https://arxiv.org/abs/2011.09607) | [arXiv:2603.21330](https://arxiv.org/abs/2603.21330) |

[FinGPT](https://github.com/AI4Finance-Foundation/FinGPT): an open-source project for financial large language models, designed for research and real-world FinTech applications.

![Visitors](https://api.visitorbadge.io/api/VisitorHit?user=AI4Finance-Foundation&repo=FinRL&countColor=%23B17A)
[![Discord](https://dcbadge.limes.pink/api/server/trsr8SXpW5?v=20260320)](https://discord.gg/trsr8SXpW5)

## Outline

  - [Overview](#overview)
  - [File Structure](#file-structure)
  - [Supported Data Sources](#supported-data-sources)
  - [Installation](#installation)
  - [Status Update](#status-update)
  - [Tutorials](#tutorials)
  - [Publications](#publications)
  - [News](#news)
  - [Citing FinRL](#citing-finrl)
  - [Join and Contribute](#join-and-contribute)
    - [Contributors](#contributors)
    - [Sponsorship](#sponsorship)
  - [LICENSE](#license)

## Project Contributors

FinRL® is an open-source financial reinforcement learning framework developed by contributors from the AI4Finance community and maintained by the AI4Finance Foundation.

Key contributors include:

- [**Hongyang (Bruce) Yang**](https://www.linkedin.com/in/brucehy/) – research and development on financial reinforcement learning frameworks, market environments, and quantitative trading applications
- [other contributors…]
  
## Overview

FinRL is the original open-source framework for financial reinforcement learning, organized around three core layers:

- **Market Environments**
- **DRL Agents**
- **Financial Applications**

For a trading task, an agent interacts with a market environment and learns sequential decision-making policies.

This repository focuses on the **classic FinRL workflow** for education, experimentation, and research prototyping.

For the **next-generation production-oriented stack**, including modular deployment and AI-native trading infrastructure, please visit **[FinRL-X / FinRL-Trading](https://github.com/AI4Finance-Foundation/FinRL-Trading)**.

<div align="center">
<img align="center" src=figs/finrl_framework.png>
</div>

Videos [FinRL](http://www.youtube.com/watch?v=ZSGJjtM-5jA) at [AI4Finance Youtube Channel](https://www.youtube.com/channel/UCrVri6k3KPBa3NhapVV4K5g).

## FinRL Stock Trading 2026 Tutorial
This tutorial demonstrates the original FinRL workflow for educational and research purposes.
For the latest production-oriented pipeline, please use **[FinRL-X / FinRL-Trading](https://github.com/AI4Finance-Foundation/FinRL-Trading)**.
### Step 1: Clone the Repository

```bash
git clone https://github.com/AI4Finance-Foundation/FinRL.git
cd FinRL
```

### Step 2: Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install FinRL

```bash
pip install -e .
```

### Step 4: Run the Scripts

**1. Data Download & Preprocessing**

```bash
python examples/FinRL_StockTrading_2026_1_data.py
```

This script downloads DOW 30 stock data from Yahoo Finance, adds technical indicators (MACD, RSI, etc.), VIX, and turbulence index, then splits the data into training set (2014–2025) and trading set (2026-01-01 to 2026-03-20), saving them as `train_data.csv` and `trade_data.csv`.

**2. Train DRL Agents**

```bash
python examples/FinRL_StockTrading_2026_2_train.py
```

This script trains 5 DRL agents (A2C, DDPG, PPO, TD3, SAC) using Stable Baselines 3 on the training data. Trained models are saved to the `trained_models/` directory.

**3. Backtest**

```bash
python examples/FinRL_StockTrading_2026_3_Backtest.py
```

This script loads the trained agents, runs them on the trading data, and compares their performance against two baselines: Mean Variance Optimization (MVO) and the DJIA index. Results are printed to the console and a plot is saved as `backtest_result.png`.


## File Structure

The main folder **finrl** has three subfolders **applications, agents, meta**. We employ a **train-test-trade** pipeline with three files: train.py, test.py, and trade.py.

```
FinRL
├── finrl (main folder)
│   ├── applications
│   	├── Stock_NeurIPS2018
│   	├── imitation_learning
│   	├── cryptocurrency_trading
│   	├── high_frequency_trading
│   	├── portfolio_allocation
│   	└── stock_trading
│   ├── agents
│   	├── elegantrl
│   	├── rllib
│   	└── stablebaseline3
│   ├── meta
│   	├── data_processors
│   	├── env_cryptocurrency_trading
│   	├── env_portfolio_allocation
│   	├── env_stock_trading
│   	├── preprocessor
│   	├── data_processor.py
│       ├── meta_config_tickers.py
│   	└── meta_config.py
│   ├── config.py
│   ├── config_tickers.py
│   ├── main.py
│   ├── plot.py
│   ├── train.py
│   ├── test.py
│   └── trade.py
│
├── examples
├── unit_tests (unit tests to verify codes on env & data)
│   ├── environments
│   	└── test_env_cashpenalty.py
│   └── downloaders
│   	├── test_yahoodownload.py
│   	└── test_alpaca_downloader.py
├── setup.py
├── requirements.txt
└── README.md
```

## Supported Data Sources

|Data Source |Type |Range and Frequency |Request Limits|Raw Data|Preprocessed Data|
|  ----  |  ----  |  ----  |  ----  |  ----  |  ----  |
|[Akshare](https://alpaca.markets/docs/introduction/)| CN Securities| 2015-now, 1day| Account-specific| OHLCV| Prices&Indicators|
|[Alpaca](https://docs.alpaca.markets/docs/getting-started)| US Stocks, ETFs| 2015-now, 1min| Account-specific| OHLCV| Prices&Indicators|
|[Baostock](http://baostock.com/baostock/index.php/Python_API%E6%96%87%E6%A1%A3)| CN Securities| 1990-12-19-now, 5min| Account-specific| OHLCV| Prices&Indicators|
|[Binance](https://binance-docs.github.io/apidocs/spot/en/#public-api-definitions)| Cryptocurrency| API-specific, 1s, 1min| API-specific| Tick-level daily aggregated trades, OHLCV| Prices&Indicators|
|[CCXT](https://docs.ccxt.com/en/latest/manual.html)| Cryptocurrency| API-specific, 1min| API-specific| OHLCV| Prices&Indicators|
|[EODhistoricaldata](https://eodhistoricaldata.com/financial-apis/)| US Securities| Frequency-specific, 1min| API-specific | OHLCV | Prices&Indicators|
|[IEXCloud](https://iexcloud.io/docs/api/)| NMS US securities|1970-now, 1 day|100 per second per IP|OHLCV| Prices&Indicators|
|[JoinQuant](https://www.joinquant.com/)| CN Securities| 2005-now, 1min| 3 requests each time| OHLCV| Prices&Indicators|
|[QuantConnect](https://www.quantconnect.com/docs/v2)| US Securities| 1998-now, 1s| NA| OHLCV| Prices&Indicators|
|[RiceQuant](https://www.ricequant.com/doc/rqdata/python/)| CN Securities| 2005-now, 1ms| Account-specific| OHLCV| Prices&Indicators|
[Sinopac](https://sinotrade.github.io/zh_TW/tutor/prepare/terms/) | Taiwan securities | 2023-04-13~now, 1min | Account-specific | OHLCV | Prices&Indicators|
|[Tushare](https://tushare.pro/document/1?doc_id=131)| CN Securities, A-share| -now, 1 min| Account-specific| OHLCV| Prices&Indicators|
|[WRDS](https://wrds-www.wharton.upenn.edu/pages/about/data-vendors/nyse-trade-and-quote-taq/)| US Securities| 2003-now, 1ms| 5 requests each time| Intraday Trades|Prices&Indicators|
|[YahooFinance](https://pypi.org/project/yfinance/)| US Securities| Frequency-specific, 1min| 2,000/hour| OHLCV | Prices&Indicators|


<!-- |Data Source |Type |Max Frequency |Raw Data|Preprocessed Data|
|  ----  |  ----  |  ----  |  ----  |  ----  |
|    AkShare |  CN Securities | 1 day  |  OHLCV |  Prices, indicators |
|    Alpaca |  US Stocks, ETFs |  1 min |  OHLCV |  Prices, indicators |
|    Alpha Vantage | Stock, ETF, forex, crypto, technical indicators | 1 min |  OHLCV  & Prices, indicators |
|    Baostock |  CN Securities |  5 min |  OHLCV |  Prices, indicators |
|    Binance |  Cryptocurrency |  1 s |  OHLCV |  Prices, indicators |
|    CCXT |  Cryptocurrency |  1 min  |  OHLCV |  Prices, indicators |
|    currencyapi |  Exchange rate | 1 day |  Exchange rate | Exchange rate, indicators |
|    currencylayer |  Exchange rate | 1 day  |  Exchange rate | Exchange rate, indicators |
|    EOD Historical Data | US stocks, and ETFs |  1 day  |  OHLCV  | Prices, indicators |
|    Exchangerates |  Exchange rate |  1 day  |  Exchange rate | Exchange rate, indicators |
|    findatapy |  CN Securities | 1 day  |  OHLCV |  Prices, indicators |
|    Financial Modeling prep | US stocks, currencies, crypto |  1 min |  OHLCV  | Prices, indicators |
|    finnhub | US Stocks, currencies, crypto |   1 day |  OHLCV  | Prices, indicators |
|    Fixer |  Exchange rate |  1 day  |  Exchange rate | Exchange rate, indicators |
|    IEXCloud |  NMS US securities | 1 day  | OHLCV |  Prices, indicators |
|    JoinQuant |  CN Securities |  1 min  |  OHLCV |  Prices, indicators |
|    Marketstack | 50+ countries |  1 day  |  OHLCV | Prices, indicators |
|    Open Exchange Rates |  Exchange rate |  1 day  |  Exchange rate | Exchange rate, indicators |
|    pandas\_datareader |  US Securities |  1 day |  OHLCV | Prices, indicators |
|    pandas-finance |  US Securities |  1 day  |  OHLCV  & Prices, indicators |
|    Polygon |  US Securities |  1 day  |  OHLCV  | Prices, indicators |
|    Quandl | 250+ sources |  1 day  |  OHLCV  | Prices, indicators |
|    QuantConnect |  US Securities |  1 s |  OHLCV |  Prices, indicators |
|    RiceQuant |  CN Securities |  1 ms  |  OHLCV |  Prices, indicators |
|    Sinopac   | Taiwan securities | 1min | OHLCV |  Prices, indicators |
|    Tiingo | Stocks, crypto |  1 day  |  OHLCV  | Prices, indicators |
|    Tushare |  CN Securities | 1 min  |  OHLCV |  Prices, indicators |
|    WRDS |  US Securities |  1 ms  |  Intraday Trades | Prices, indicators |
|    XE |  Exchange rate |  1 day  |  Exchange rate | Exchange rate, indicators |
|    Xignite |  Exchange rate |  1 day  |  Exchange rate | Exchange rate, indicators |
|    YahooFinance |  US Securities | 1 min  |  OHLCV  |  Prices, indicators |
|    ystockquote |  US Securities |  1 day  |  OHLCV | Prices, indicators | -->



OHLCV: open, high, low, and close prices; volume. adjusted_close: adjusted close price

Technical indicators: 'macd', 'boll_ub', 'boll_lb', 'rsi_30', 'dx_30', 'close_30_sma', 'close_60_sma'. Users also can add new features.


## Installation
+ [Install description for all operating systems (MAC
... [TRUNCATED]
```

### File: requirements.txt
```txt
alpaca-py
alpaca_trade_api>=2.1.0
ccxt>=1.66.32
elegantrl

gputil
gymnasium
importlib-metadata>=6.0,<=8.5.0
jqdatasdk

lz4
# plot
matplotlib
# data handling
numpy>=1.17.3
pandas>=1.1.5
pandas_market_calendars  # calendars

#hooks
pre-commit
pyfolio-reloaded

# testing requirements
pytest
ray[default]
ray[tune]
recommonmark

# Model Building Requirements
scikit-learn>=0.21.0

scipy

selenium

# packaging
setuptools>=65.5.0

# to build docs using sphinx
sphinx
sphinx_rtd_theme

SQLAlchemy
stable-baselines3[extra]
stockstats>=0.4.0
swig

TA-lib # conda install -c conda-forge ta-lib

tensorboard
webdriver-manager
wheel>=0.33.6
wrds


# market data & paper trading API
yfinance

```

### File: setup.py
```py
from __future__ import annotations

from setuptools import find_packages
from setuptools import setup

# Read requirements.txt, ignore comments
try:
    REQUIRES = list()
    f = open("requirements.txt", "rb")
    for line in f.read().decode("utf-8").split("\n"):
        line = line.strip()
        if "#" in line:
            line = line[: line.find("#")].strip()
        if line:
            REQUIRES.append(line)
except FileNotFoundError:
    print("'requirements.txt' not found!")
    REQUIRES = list()

setup(
    name="FinRL",
    version="0.3.8",
    include_package_data=True,
    author="AI4Finance Foundation",
    author_email="contact@ai4finance.org",
    url="https://github.com/AI4Finance-Foundation/FinRL",
    license="MIT",
    packages=find_packages(),
    description="FinRL: Financial Reinforcement Learning Framework.",
    long_description="Version 0.3.5 notes: stable version, code refactoring, more tutorials, clear documentation",
    # It is developed by `AI4Finance`_. \
    # _AI4Finance: https://ai4finance.org/",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords="Reinforcement Learning, Finance",
    platform=["any"],
    python_requires=">=3.7",
)

```

### File: examples\README.md
```md
## FinRL Stock Trading 2026 Tutorial

### Step 1: Clone the Repository

```bash
git clone https://github.com/AI4Finance-Foundation/FinRL.git
cd FinRL
```

### Step 2: Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install FinRL

```bash
pip install -e .
```

### Step 4: Run the Scripts

**1. Data Download & Preprocessing**

```bash
python examples/FinRL_StockTrading_2026_1_data.py
```

This script downloads DOW 30 stock data from Yahoo Finance, adds technical indicators (MACD, RSI, etc.), VIX, and turbulence index, then splits the data into training set (2014–2025) and trading set (2026-01-01 to 2026-03-20), saving them as `train_data.csv` and `trade_data.csv`.

**2. Train DRL Agents**

```bash
python examples/FinRL_StockTrading_2026_2_train.py
```

This script trains 5 DRL agents (A2C, DDPG, PPO, TD3, SAC) using Stable Baselines 3 on the training data. Trained models are saved to the `trained_models/` directory.

**Key Hyperparameters:**

| Parameter | Description | Default in Script |
|-----------|-------------|-------------------|
| `total_timesteps` | Total number of environment interactions for training. **This is the most important parameter** — higher values give the agent more experience to learn from, leading to better trading performance. Start with a small value (e.g., 1,000) for a quick test, then increase (e.g., 20,000–200,000) for serious training. | 20,000 |
| `learning_rate` | Controls how much the model weights are updated at each step. Too high causes instability; too low causes slow learning. | 0.001 |
| `batch_size` | Number of samples used per gradient update. Larger batches give more stable updates but require more memory. | 100 |
| `buffer_size` | Size of the replay buffer (for off-policy algorithms like DDPG, TD3, SAC). Stores past experiences for the agent to learn from. Larger buffers retain more diverse experiences. | 1,000,000 |

**3. Backtest**

```bash
python examples/FinRL_StockTrading_2026_3_Backtest.py
```

This script loads the trained agents, runs them on the trading data, and compares their performance against two baselines: Mean Variance Optimization (MVO) and the DJIA index. Results are printed to the console and a plot is saved as `backtest_result.png`.

```

### File: finrl\main.py
```py
from __future__ import annotations

import os
from argparse import ArgumentParser
from typing import List

from finrl.config import ALPACA_API_BASE_URL
from finrl.config import DATA_SAVE_DIR
from finrl.config import ERL_PARAMS
from finrl.config import INDICATORS
from finrl.config import RESULTS_DIR
from finrl.config import TENSORBOARD_LOG_DIR
from finrl.config import TEST_END_DATE
from finrl.config import TEST_START_DATE
from finrl.config import TRADE_END_DATE
from finrl.config import TRADE_START_DATE
from finrl.config import TRAIN_END_DATE
from finrl.config import TRAIN_START_DATE
from finrl.config import TRAINED_MODEL_DIR
from finrl.config_tickers import DOW_30_TICKER
from finrl.meta.env_stock_trading.env_stocktrading_np import StockTradingEnv

# construct environment

# try:
#     from finrl.config_private import ALPACA_API_KEY, ALPACA_API_SECRET
# except ImportError:
#     raise FileNotFoundError(
#         "Please set your own ALPACA_API_KEY and ALPACA_API_SECRET in config_private.py"
#     )


def build_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--mode",
        dest="mode",
        help="start mode, train, download_data" " backtest",
        metavar="MODE",
        default="train",
    )
    return parser


def check_and_make_directories(directories: list[str]):
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)


def main() -> int:
    parser = build_parser()
    options = parser.parse_args()
    check_and_make_directories(
        [DATA_SAVE_DIR, TRAINED_MODEL_DIR, TENSORBOARD_LOG_DIR, RESULTS_DIR]
    )

    if options.mode == "train":
        from finrl import train

        env = StockTradingEnv

        # demo for elegantrl
        kwargs = (
            {}
        )  # in current meta, with respect yahoofinance, kwargs is {}. For other data sources, such as joinquant, kwargs is not empty
        train(
            start_date=TRAIN_START_DATE,
            end_date=TRAIN_END_DATE,
            ticker_list=DOW_30_TICKER,
            data_source="yahoofinance",
            time_interval="1D",
            technical_indicator_list=INDICATORS,
            drl_lib="elegantrl",
            env=env,
            model_name="ppo",
            cwd="./test_ppo",
            erl_params=ERL_PARAMS,
            break_step=1e5,
            kwargs=kwargs,
        )
    elif options.mode == "test":
        from finrl import test

        env = StockTradingEnv

        # demo for elegantrl
        # in current meta, with respect yahoofinance, kwargs is {}. For other data sources, such as joinquant, kwargs is not empty
        kwargs = {}

        account_value_erl = test(  # noqa
            start_date=TEST_START_DATE,
            end_date=TEST_END_DATE,
            ticker_list=DOW_30_TICKER,
            data_source="yahoofinance",
            time_interval="1D",
            technical_indicator_list=INDICATORS,
            drl_lib="elegantrl",
            env=env,
            model_name="ppo",
            cwd="./test_ppo",
            net_dimension=512,
            kwargs=kwargs,
        )
    elif options.mode == "trade":
        from finrl import trade

        try:
            from finrl.config_private import ALPACA_API_KEY, ALPACA_API_SECRET
        except ImportError:
            raise FileNotFoundError(
                "Please set your own ALPACA_API_KEY and ALPACA_API_SECRET in config_private.py"
            )
        env = StockTradingEnv
        kwargs = {}
        trade(
            start_date=TRADE_START_DATE,
            end_date=TRADE_END_DATE,
            ticker_list=DOW_30_TICKER,
            data_source="yahoofinance",
            time_interval="1D",
            technical_indicator_list=INDICATORS,
            drl_lib="elegantrl",
            env=env,
            model_name="ppo",
            API_KEY=ALPACA_API_KEY,
            API_SECRET=ALPACA_API_SECRET,
            API_BASE_URL=ALPACA_API_BASE_URL,
            trade_mode="paper_trading",
            if_vix=True,
            kwargs=kwargs,
            state_dim=len(DOW_30_TICKER) * (len(INDICATORS) + 3)
            + 3,  # bug fix: for ppo add dimension of state/observations space =  len(stocks)* len(INDICATORS) + 3+ 3*len(stocks)
            action_dim=len(
                DOW_30_TICKER
            ),  # bug fix: for ppo add dimension of action space = len(stocks)
        )
    else:
        raise ValueError("Wrong mode.")
    return 0


# Users can input the following command in terminal
# python main.py --mode=train
# python main.py --mode=test
# python main.py --mode=trade
if __name__ == "__main__":
    raise SystemExit(main())

```

### File: finrl\README.md
```md
This folder has three subfolders:
+ applications: trading tasks,
+ agents: DRL algorithms, from ElegantRL, RLlib, or Stable Baselines 3 (SB3). Users can plug in any DRL lib and play.
+ meta: market environments, we merge the stable ones from the active [FinRL-Meta repo](https://github.com/AI4Finance-Foundation/FinRL-Meta).

Then, we employ a train-test-trade pipeline by three files: train.py, test.py, and trade.py.

```
FinRL
├── finrl (this folder)
│   ├── applications
│   	├── cryptocurrency_trading
│   	├── high_frequency_trading
│   	├── portfolio_allocation
│   	└── stock_trading
│   ├── agents
│   	├── elegantrl
│   	├── rllib
│   	└── stablebaseline3
│   ├── meta
│   	├── data_processors
│   	├── env_cryptocurrency_trading
│   	├── env_portfolio_allocation
│   	├── env_stock_trading
│   	├── preprocessor
│   	├── data_processor.py
│   	└── finrl_meta_config.py
│   ├── config.py
│   ├── config_tickers.py
│   ├── main.py
│   ├── train.py
│   ├── test.py
│   ├── trade.py
│   └── plot.py
```

```

### File: finrl\agents\portfolio_optimization\README.md
```md
# Portfolio Optimization Agents

This directory contains architectures and algorithms commonly used in portfolio optimization agents.

To instantiate the model, it's necessary to have an instance of [PortfolioOptimizationEnv](/finrl/meta/env_portfolio_optimization/). In the example below, we use the `DRLAgent` class to instantiate a policy gradient ("pg") model. With the dictionary `model_kwargs`, we can set the `PolicyGradient` class parameters and, whith the dictionary `policy_kwargs`, it's possible to change the parameters of the chosen architecture.

```python
from finrl.agents.portfolio_optimization.models import DRLAgent
from finrl.agents.portfolio_optimization.architectures import EIIE

# set PolicyGradient algorithm arguments
model_kwargs = {
    "lr": 0.01,
    "policy": EIIE,
}

# set EIIE architecture arguments
policy_kwargs = {
    "k_size": 4
}

model = DRLAgent(train_env).get_model("pg", model_kwargs, policy_kwargs)
```

In the example below, the model is trained in 5 episodes (we define an episode as a complete period of the used environment).

```python
DRLAgent.train_model(model, episodes=5)
```

It's important that the architecture and the environment have the same `time_window` defined. By default, both of them use 50 timesteps as `time_window`. For more details about what is a time window, check this [article](https://doi.org/10.5753/bwaif.2023.231144).

### Policy Gradient Algorithm

The class `PolicyGradient` implements the Policy Gradient algorithm used in *Jiang et al* paper. This algorithm is inspired by DDPG (deep deterministic policy gradient), but there are a couple of differences:
- DDPG is an actor-critic algorithm, so it has an actor and a critic neural network. The algorithm below, however, doesn't have a critic neural network and uses the portfolio value as value function: the policy will be updated to maximize the portfolio value.
- DDPG usually makes use of a noise parameter in the action during training to create an exploratory behavior. PG algorithm, on the other hand, has a full-exploit approach.
- DDPG randomly samples experiences from its replay buffer. The implemented policy gradient, however, samples a sequential batch of experiences in time, to make it possible to calculate the variation of the portfolio value in the batch and use it as value function.

The algorithm was implemented as follows:
1. Initializes policy network and replay buffer;
2. For each episode, do the following:
    1. For each period of `batch_size` timesteps, do the following:
        1. For each timestep, define an action to be performed, simulate the timestep and save the experiences in the replay buffer.
        2. After `batch_size` timesteps are simulated, sample the replay buffer.
        4. Calculate the value function: $V = \sum\limits_{t=1}^{batch\_size} ln(\mu_{t}(W_{t} \cdot P_{t}))$, where $W_{t}$ is the action performed at timestep t, $P_{t}$ is the price variation vector at timestep t and $\mu_{t}$ is the transaction remainder factor at timestep t. Check *Jiang et al* paper for more details.
        5. Perform gradient ascent in the policy network.
    2. If, in the and of episode, there is sequence of remaining experiences in the replay buffer, perform steps 1 to 5 with the remaining experiences.

### References

If you are using one of them in your research, you can use the following references.

#### EIIE Architecture and Policy Gradient algorithm

[A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem](https://doi.org/10.48550/arXiv.1706.10059)
```
@misc{jiang2017deep,
      title={A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem},
      author={Zhengyao Jiang and Dixing Xu and Jinjun Liang},
      year={2017},
      eprint={1706.10059},
      archivePrefix={arXiv},
      primaryClass={q-fin.CP}
}
```

#### EI3 Architecture

[A Multi-Scale Temporal Feature Aggregation Convolutional Neural Network for Portfolio Management](https://doi.org/10.1145/3357384.3357961)
```
@inproceedings{shi2018multiscale,
               author = {Shi, Si and Li, Jianjun and Li, Guohui and Pan, Peng},
               title = {A Multi-Scale Temporal Feature Aggregation Convolutional Neural Network for Portfolio Management},
               year = {2019},
               isbn = {9781450369763},
               publisher = {Association for Computing Machinery},
               address = {New York, NY, USA},
               url = {https://doi.org/10.1145/3357384.3357961},
               doi = {10.1145/3357384.3357961},
               booktitle = {Proceedings of the 28th ACM International Conference on Information and Knowledge Management},
               pages = {1613–1622},
               numpages = {10},
               keywords = {portfolio management, reinforcement learning, inception network, convolution neural network},
               location = {Beijing, China},
               series = {CIKM '19} }
```

```

### File: finrl\applications\imitation_learning\README.md
```md
# FinRL Imitation Learning

A multi-stage machine learning approach is a promising approach for analyzing financial big data, especially when learning from alpha factors or smart investors. Here, we automate this workflow, starting with imitating these strategies, and then using reinforcement learning method to further refine the results.

In complicated tasks such as Go and Atari games, imitation learning is often used to initialize deep neural networks that achieve human-level performance. Imitation learning involves training a model to imitate a human's behavior, typically using a dataset of expert demonstrations. This process provides a a starting point for further refinement using reinforcement learning, which could learn through trial and error to find strategies that surpass human-level performance.

By automating this workflow, we can analogously save valuable time and resources, while also providing more accurate and reliable results. Ultimately, this approach can help to identify profitable investment opportunities and inform smarter financial decision-making.

## File Structure

**1-Stock Selection**

We identify a pool of stocks that are favoured by retail investors and have a high correlation between their trading preference and return rates. By analyzing the trading behaviour of retail investors, we can gain valuable insights into the stocks that are popular among this group and understand how their trading preferences affect the performance of these stocks.

**2-Weight Initialization**

We construct the action space, which will serve as data labels. The action space is a critical component of a machine learning approach, as it represents the set of actions that our algorithm can take in response to a data input. There are two key sources to inform the action construction: MVO (mean-variance optimization) and retail investor preferred weights.

**3-Imitation Sandbox**

We use a set of regression models, including linear models, trees, and neural networks, to analyze our data. Our approach involves incrementally increasing the complexity of the models to evaluate their performance in predicting outcomes.

To ensure the reliability of our analysis, we conduct a placebo test to evaluate the potential for information leakage. This involves feeding simulated data into our models to assess their performance in predicting outcomes that are not based on actual data. By doing so, we can ensure that our models are not biased by any unforeseen factors or hidden information that may have influenced the results.

```

### File: finrl\applications\Stock_NeurIPS2018\README.md
```md
We show a workflow of applying RL in algorithmic trading, which is a reproduction and improvement of the process in the [NeurIPS 2018 paper](https://arxiv.org/abs/1811.07522).

# Usage

## Step I. Data

First, run the notebook: *Stock_NeurIPS2018_1_Data.ipynb*.

It downloads and preprocesses stocks' OHLCV data.

It generates two csv files: *train.csv*, *trade.csv*. You can check the provided two sample files.

## Step II. Train a Trading Agent

Second, run the notebook: *Stock_NeurIPS2018_2_Train.ipynb*.

It shows how to process the data into an OpenAI gym-style envrionment, and then train a DRL agent.

It will generate a trained RL model .zip file. Here, we also provided a training A2C model in .zip file.

## Step III. Backtest

Finally, run the notebook: *Stock_NeurIPS2018_3_Backtest.ipynb*.

It backtests the trained agent and compares with two baselines: Mean-Variance Optimization and the market DJIA index, respectively.

At the end, it will plot a figure of the portfolio value during the backtest process.

```

### File: finrl\meta\env_portfolio_optimization\README.md
```md
# PortfolioOptimizationEnv (POE)

This environment simulates the effects of the market in a portfolio that is periodically rebalanced through a reinforcement learning agent. At every timestep $t$, the agent is responsible for determining a portfolio vector $W_{t}$ which contains the percentage of money invested in each stock. The environment, then, utilizes data provided by the user to simulate the new portfolio value at time-step $t+1$.

For more details on the formulation of this problem, check the following paper:

[POE: A General Portfolio Optimization Environment for FinRL](https://doi.org/10.5753/bwaif.2023.231144)
```
@inproceedings{bwaif,
 author = {Caio Costa and Anna Costa},
 title = {POE: A General Portfolio Optimization Environment for FinRL},
 booktitle = {Anais do II Brazilian Workshop on Artificial Intelligence in Finance},
 location = {João Pessoa/PB},
 year = {2023},
 keywords = {},
 issn = {0000-0000},
 pages = {132--143},
 publisher = {SBC},
 address = {Porto Alegre, RS, Brasil},
 doi = {10.5753/bwaif.2023.231144},
 url = {https://sol.sbc.org.br/index.php/bwaif/article/view/24959}
}
```

## Inputs
This environment simulates the interactions between an agent and the financial market
based on data provided by a dataframe. The dataframe contains the time series of
features defined by the user (such as closing, high and low prices) and must have
a time and a tic column with a list of datetimes and ticker symbols respectively.
An example of dataframe is shown below:
``````
    date        high            low             close           tic
0   2020-12-23  0.157414        0.127420        0.136394        ADA-USD
1   2020-12-23  34.381519       30.074295       31.097898       BNB-USD
2   2020-12-23  24024.490234    22802.646484    23241.345703    BTC-USD
3   2020-12-23  0.004735        0.003640        0.003768        DOGE-USD
4   2020-12-23  637.122803      560.364258      583.714600      ETH-USD
... ...         ...             ...             ...             ...
``````

## Actions

At each time step, the environment expects an action that is a one-dimensional Box of shape (n+1,), where $n$ is the number of stocks in the portfolio. This action is called *portfolio vector* and contains, for the remaining cash and for each stock, the percentage of allocated money.

For example: given a portfolio of three stocks, a valid portfolio vector would b $W_{t} = [0.25, 0.4, 0.2, 0.15]$. In this example, 25% of the money is not invested (remaining cash), 40% is invested in stock 1, 20% in stock 2 and 15% in sotck 3.

**Note:** It's important that the sum of the values in the portfolio vator is equal (or very close) to 1. If it's not, POE will apply a softmax normalization.

## Observations

POE can return two types of observations during simulation: a Dict or a Box.

- The box is a three-dimensional array of shape $(f, n, t)$, where $f$ s the number of features, $n$ is the number of stocks in the portfolio and $t$ is the time series timw window. This observation basically only contains the current state of the agent.

- The dict representation, on the other hand, is a dictionary containing the state and the last portfolio vector, like below:

```json
{
"state": "three-dimensional Box (f, n, t representing the time series",
"last_action": "one-dimensional Box (n+1,) representing the portfolio weights"
}
```

## Rewards
Given the simulation of timestep $t$, the reward is given by the following formula: $r_{t} = ln(V_{t}/V_{t-1})$, where $V_{t}$ is the value of the portfolio at time $t$. By using this formulation, the reward is negative whenever the portfolio value decreases due to a rebalancing and is positive otherwise.

## Example
A jupyter notebook using this environment can be found [here](/examples/FinRL_PortfolioOptimizationEnv_Demo.ipynb).

```

### File: .pre-commit-config.yaml
```yaml
exclude: 'Stock_NeurIPS2018.py'
ci:
    skip: [flake8]  # remove this eventually
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: check-docstring-first
      - id: check-yaml
      - id: end-of-file-fixer
      - id: requirements-txt-fixer
      - id: trailing-whitespace
  - repo: https://github.com/asottile/reorder-python-imports
    rev: v3.15.0
    hooks:
      - id: reorder-python-imports
        args: [--py37-plus, --add-import, "from __future__ import annotations"]
  - repo: https://github.com/asottile/pyupgrade
    rev: v3.20.0
    hooks:
      - id: pyupgrade
        args: [--py37-plus]
  - repo: https://github.com/psf/black
    rev: 25.1.0
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/flake8
    rev: 7.3.0
    hooks:
      - id: flake8

```

### File: .github\sponsor.md
```md
We are building the non-profit AI4Finance foundation for open-source projects, in the AI for Finance field.

Your support will encourage the core team to release more practical codes. Thx.

```

### File: .vscode\settings.json
```json
{
    "makefile.extensionOutputFolder": "./.vscode"
}

```

### File: docs\.readthdocs.yaml
```yaml
python:
   setup_py_install: true

```

### File: examples\FinRL_PaperTrading_Demo_refactored.py
```py
# Disclaimer: Nothing herein is financial advice, and NOT a recommendation to trade real money. Many platforms exist for simulated trading (paper trading) which can be used for building and developing the methods discussed. Please use common sense and always first consult a professional before trading or investing.
# install finrl library
# %pip install --upgrade git+https://github.com/AI4Finance-Foundation/FinRL.git
# Alpaca keys
from __future__ import annotations

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_key", help="data source api key")
parser.add_argument("data_secret", help="data source api secret")
parser.add_argument("data_url", help="data source api base url")
parser.add_argument("trading_key", help="trading api key")
parser.add_argument("trading_secret", help="trading api secret")
parser.add_argument("trading_url", help="trading api base url")
args = parser.parse_args()
DATA_API_KEY = args.data_key
DATA_API_SECRET = args.data_secret
DATA_API_BASE_URL = args.data_url
TRADING_API_KEY = args.trading_key
TRADING_API_SECRET = args.trading_secret
TRADING_API_BASE_URL = args.trading_url

print("DATA_API_KEY: ", DATA_API_KEY)
print("DATA_API_SECRET: ", DATA_API_SECRET)
print("DATA_API_BASE_URL: ", DATA_API_BASE_URL)
print("TRADING_API_KEY: ", TRADING_API_KEY)
print("TRADING_API_SECRET: ", TRADING_API_SECRET)
print("TRADING_API_BASE_URL: ", TRADING_API_BASE_URL)

from finrl.meta.env_stock_trading.env_stocktrading_np import StockTradingEnv
from finrl.meta.paper_trading.alpaca import PaperTradingAlpaca
from finrl.meta.paper_trading.common import train, test, alpaca_history, DIA_history
from finrl.config import INDICATORS

# Import Dow Jones 30 Symbols
from finrl.config_tickers import DOW_30_TICKER

ticker_list = DOW_30_TICKER
env = StockTradingEnv
# if you want to use larger datasets (change to longer period), and it raises error, please try to increase "target_step". It should be larger than the episode steps.
ERL_PARAMS = {
    "learning_rate": 3e-6,
    "batch_size": 2048,
    "gamma": 0.985,
    "seed": 312,
    "net_dimension": [128, 64],
    "target_step": 5000,
    "eval_gap": 30,
    "eval_times": 1,
}

# Set up sliding window of 6 days training and 2 days testing
import datetime
from pandas.tseries.offsets import BDay  # BDay is business day, not birthday...

today = datetime.datetime.today()

TEST_END_DATE = (today - BDay(1)).to_pydatetime().date()
TEST_START_DATE = (TEST_END_DATE - BDay(1)).to_pydatetime().date()
TRAIN_END_DATE = (TEST_START_DATE - BDay(1)).to_pydatetime().date()
TRAIN_START_DATE = (TRAIN_END_DATE - BDay(5)).to_pydatetime().date()
TRAINFULL_START_DATE = TRAIN_START_DATE
TRAINFULL_END_DATE = TEST_END_DATE

TRAIN_START_DATE = str(TRAIN_START_DATE)
TRAIN_END_DATE = str(TRAIN_END_DATE)
TEST_START_DATE = str(TEST_START_DATE)
TEST_END_DATE = str(TEST_END_DATE)
TRAINFULL_START_DATE = str(TRAINFULL_START_DATE)
TRAINFULL_END_DATE = str(TRAINFULL_END_DATE)

print("TRAIN_START_DATE: ", TRAIN_START_DATE)
print("TRAIN_END_DATE: ", TRAIN_END_DATE)
print("TEST_START_DATE: ", TEST_START_DATE)
print("TEST_END_DATE: ", TEST_END_DATE)
print("TRAINFULL_START_DATE: ", TRAINFULL_START_DATE)
print("TRAINFULL_END_DATE: ", TRAINFULL_END_DATE)

train(
    start_date=TRAIN_START_DATE,
    end_date=TRAIN_END_DATE,
    ticker_list=ticker_list,
    data_source="alpaca",
    time_interval="1Min",
    technical_indicator_list=INDICATORS,
    drl_lib="elegantrl",
    env=env,
    model_name="ppo",
    if_vix=True,
    API_KEY=DATA_API_KEY,
    API_SECRET=DATA_API_SECRET,
    API_BASE_URL=DATA_API_BASE_URL,
    erl_params=ERL_PARAMS,
    cwd="./papertrading_erl",  # current_working_dir
    break_step=1e5,
)

account_value_erl = test(
    start_date=TEST_START_DATE,
    end_date=TEST_END_DATE,
    ticker_list=ticker_list,
    data_source="alpaca",
    time_interval="1Min",
    technical_indicator_list=INDICATORS,
    drl_lib="elegantrl",
    env=env,
    model_name="ppo",
    if_vix=True,
    API_KEY=DATA_API_KEY,
    API_SECRET=DATA_API_SECRET,
    API_BASE_URL=DATA_API_BASE_URL,
    cwd="./papertrading_erl",
    net_dimension=ERL_PARAMS["net_dimension"],
)

train(
    start_date=TRAINFULL_START_DATE,  # After tuning well, retrain on the training and testing sets
    end_date=TRAINFULL_END_DATE,
    ticker_list=ticker_list,
    data_source="alpaca",
    time_interval="1Min",
    technical_indicator_list=INDICATORS,
    drl_lib="elegantrl",
    env=env,
    model_name="ppo",
    if_vix=True,
    API_KEY=DATA_API_KEY,
    API_SECRET=DATA_API_SECRET,
    API_BASE_URL=DATA_API_BASE_URL,
    erl_params=ERL_PARAMS,
    cwd="./papertrading_erl_retrain",
    break_step=2e5,
)

action_dim = len(DOW_30_TICKER)
state_dim = (
    1 + 2 + 3 * action_dim + len(INDICATORS) * action_dim
)  # Calculate the DRL state dimension manually for paper trading. amount + (turbulence, turbulence_bool) + (price, shares, cd (holding time)) * stock_dim + tech_dim

paper_trading_erl = PaperTradingAlpaca(
    ticker_list=DOW_30_TICKER,
    time_interval="1Min",
    drl_lib="elegantrl",
    agent="ppo",
    cwd="./papertrading_erl_retrain",
    net_dim=ERL_PARAMS["net_dimension"],
    state_dim=state_dim,
    action_dim=action_dim,
    API_KEY=TRADING_API_KEY,
    API_SECRET=TRADING_API_SECRET,
    API_BASE_URL=TRADING_API_BASE_URL,
    tech_indicator_list=INDICATORS,
    turbulence_thresh=30,
    max_stock=1e2,
)

paper_trading_erl.run()

# Check Portfolio Performance
# ## Get cumulative return
df_erl, cumu_erl = alpaca_history(
    key=DATA_API_KEY,
    secret=DATA_API_SECRET,
    url=DATA_API_BASE_URL,
    start="2022-09-01",  # must be within 1 month
    end="2022-09-12",
)  # change the date if error occurs

df_djia, cumu_djia = DIA_history(start="2022-09-01")
returns_erl = cumu_erl - 1
returns_dia = cumu_djia - 1
returns_dia = returns_dia[: returns_erl.shape[0]]

# plot and save
import matplotlib.pyplot as plt

plt.figure(dpi=1000)
plt.grid()
plt.grid(which="minor", axis="y")
plt.title("Stock Trading (Paper trading)", fontsize=20)
plt.plot(returns_erl, label="ElegantRL Agent", color="red")
# plt.plot(returns_sb3, label = 'Stable-Baselines3 Agent', color = 'blue' )
# plt.plot(returns_rllib, label = 'RLlib Agent', color = 'green')
plt.plot(returns_dia, label="DJIA", color="grey")
plt.ylabel("Return", fontsize=16)
plt.xlabel("Year 2021", fontsize=16)
plt.xticks(size=14)
plt.yticks(size=14)
ax = plt.gca()
ax.xaxis.set_major_locator(ticker_list.MultipleLocator(78))
ax.xaxis.set_minor_locator(ticker_list.MultipleLocator(6))
ax.yaxis.set_minor_locator(ticker_list.MultipleLocator(0.005))
ax.yaxis.set_major_formatter(ticker_list.PercentFormatter(xmax=1, decimals=2))
ax.xaxis.set_major_formatter(
    ticker_list.FixedFormatter(["", "10-19", "", "10-20", "", "10-21", "", "10-22"])
)
plt.legend(fontsize=10.5)
plt.savefig("papertrading_stock.png")

```

### File: examples\FinRL_StockTrading_2026_1_data.py
```py
"""
Stock NeurIPS2018 Part 1. Data

This series is a reproduction of paper "Deep reinforcement learning for automated stock trading: An ensemble strategy".

Introduce how to use FinRL to fetch and process data that we need for ML/RL trading.
"""

import itertools

import pandas as pd
import yfinance as yf

from finrl import config_tickers
from finrl.config import INDICATORS, TRAIN_START_DATE, TRAIN_END_DATE, TRADE_START_DATE, TRADE_END_DATE
from finrl.meta.preprocessor.preprocessors import FeatureEngineer, data_split
from finrl.meta.preprocessor.yahoodownloader import YahooDownloader

# %% Part 1. Fetch data - Single ticker

# Using yfinance directly
aapl_df_yf = yf.download(tickers="aapl", start="2020-01-01", end="2020-01-31")
print("=== yfinance download ===")
print(aapl_df_yf.head())

# Using FinRL's YahooDownloader
aapl_df_finrl = YahooDownloader(
    start_date="2020-01-01",
    end_date="2020-01-31",
    ticker_list=["aapl"],
).fetch_data()
print("\n=== FinRL YahooDownloader ===")
print(aapl_df_finrl.head())

# %% Part 2. Fetch data - DOW 30 tickers

print("\n=== DOW 30 Tickers ===")
print(config_tickers.DOW_30_TICKER)

df_raw = YahooDownloader(
    start_date=TRAIN_START_DATE,
    end_date=TRADE_END_DATE,
    ticker_list=config_tickers.DOW_30_TICKER,
).fetch_data()
print("\n=== Raw data ===")
print(df_raw.head())

# %% Part 3. Preprocess data

fe = FeatureEngineer(
    use_technical_indicator=True,
    tech_indicator_list=INDICATORS,
    use_vix=True,
    use_turbulence=True,
    user_defined_feature=False,
)

processed = fe.preprocess_data(df_raw)

list_ticker = processed["tic"].unique().tolist()
list_date = list(
    pd.date_range(processed["date"].min(), processed["date"].max()).astype(str)
)
combination = list(itertools.product(list_date, list_ticker))

processed_full = pd.DataFrame(combination, columns=["date", "tic"]).merge(
    processed, on=["date", "tic"], how="left"
)
processed_full = processed_full[processed_full["date"].isin(processed["date"])]
processed_full = processed_full.sort_values(["date", "tic"])
processed_full = processed_full.fillna(0)

print("\n=== Processed data ===")
print(processed_full.head())

# %% Part 4. Split and save data

train = data_split(processed_full, TRAIN_START_DATE, TRAIN_END_DATE)
trade = data_split(processed_full, TRADE_START_DATE, TRADE_END_DATE)
print(f"\nTrain data length: {len(train)}")
print(f"Trade data length: {len(trade)}")

train.to_csv("train_data.csv")
trade.to_csv("trade_data.csv")
print("Data saved to train_data.csv and trade_data.csv")

```

### File: examples\FinRL_StockTrading_2026_2_train.py
```py
"""
Stock NeurIPS2018 Part 2. Train

This series is a reproduction of paper "Deep reinforcement learning for
automated stock trading: An ensemble strategy".

Introduce how to use FinRL to make data into the gym form environment, and train DRL agents on it.
"""

import pandas as pd
from stable_baselines3.common.logger import configure

from finrl.agents.stablebaselines3.models import DRLAgent
from finrl.config import INDICATORS, TRAINED_MODEL_DIR, RESULTS_DIR
from finrl.main import check_and_make_directories
from finrl.meta.env_stock_trading.env_stocktrading import StockTradingEnv

# %% Part 1. Prepare directories

check_and_make_directories([TRAINED_MODEL_DIR])

# %% Part 2. Build environment

train = pd.read_csv("train_data.csv")
train = train.set_index(train.columns[0])
train.index.names = [""]

stock_dimension = len(train.tic.unique())
state_space = 1 + 2 * stock_dimension + len(INDICATORS) * stock_dimension
print(f"Stock Dimension: {stock_dimension}, State Space: {state_space}")

buy_cost_list = sell_cost_list = [0.001] * stock_dimension
num_stock_shares = [0] * stock_dimension

env_kwargs = {
    "hmax": 100,
    "initial_amount": 1000000,
    "num_stock_shares": num_stock_shares,
    "buy_cost_pct": buy_cost_list,
    "sell_cost_pct": sell_cost_list,
    "state_space": state_space,
    "stock_dim": stock_dimension,
    "tech_indicator_list": INDICATORS,
    "action_space": stock_dimension,
    "reward_scaling": 1e-4,
}

e_train_gym = StockTradingEnv(df=train, **env_kwargs)
env_train, _ = e_train_gym.get_sb_env()
print(type(env_train))

# %% Part 3. Train DRL Agents

if_using_a2c = True
if_using_ddpg = True
if_using_ppo = True
if_using_td3 = True
if_using_sac = True

# --- Agent 1: A2C ---
agent = DRLAgent(env=env_train)
model_a2c = agent.get_model("a2c")
if if_using_a2c:
    tmp_path = RESULTS_DIR + "/a2c"
    new_logger_a2c = configure(tmp_path, ["stdout", "csv", "tensorboard"])
    model_a2c.set_logger(new_logger_a2c)

trained_a2c = (
    agent.train_model(model=model_a2c, tb_log_name="a2c", total_timesteps=20000)
    if if_using_a2c
    else None
)
if if_using_a2c:
    trained_a2c.save(TRAINED_MODEL_DIR + "/agent_a2c")

# --- Agent 2: DDPG ---
agent = DRLAgent(env=env_train)
model_ddpg = agent.get_model("ddpg")
if if_using_ddpg:
    tmp_path = RESULTS_DIR + "/ddpg"
    new_logger_ddpg = configure(tmp_path, ["stdout", "csv", "tensorboard"])
    model_ddpg.set_logger(new_logger_ddpg)

trained_ddpg = (
    agent.train_model(model=model_ddpg, tb_log_name="ddpg", total_timesteps=20000)
    if if_using_ddpg
    else None
)
if if_using_ddpg:
    trained_ddpg.save(TRAINED_MODEL_DIR + "/agent_ddpg")

# --- Agent 3: PPO ---
agent = DRLAgent(env=env_train)
PPO_PARAMS = {
    "n_steps": 2048,
    "ent_coef": 0.01,
    "learning_rate": 0.00025,
    "batch_size": 128,
}
model_ppo = agent.get_model("ppo", model_kwargs=PPO_PARAMS)
if if_using_ppo:
    tmp_path = RESULTS_DIR + "/ppo"
    new_logger_ppo = configure(tmp_path, ["stdout", "csv", "tensorboard"])
    model_ppo.set_logger(new_logger_ppo)

trained_ppo = (
    agent.train_model(model=model_ppo, tb_log_name="ppo", total_timesteps=20000)
    if if_using_ppo
    else None
)
if if_using_ppo:
    trained_ppo.save(TRAINED_MODEL_DIR + "/agent_ppo")

# --- Agent 4: TD3 ---
agent = DRLAgent(env=env_train)
TD3_PARAMS = {
    "batch_size": 100,
    "buffer_size": 1000000,
    "learning_rate": 0.001,
}
model_td3 = agent.get_model("td3", model_kwargs=TD3_PARAMS)
if if_using_td3:
    tmp_path = RESULTS_DIR + "/td3"
    new_logger_td3 = configure(tmp_path, ["stdout", "csv", "tensorboard"])
    model_td3.set_logger(new_logger_td3)

trained_td3 = (
    agent.train_model(model=model_td3, tb_log_name="td3", total_timesteps=20000)
    if if_using_td3
    else None
)
if if_using_td3:
    trained_td3.save(TRAINED_MODEL_DIR + "/agent_td3")

# --- Agent 5: SAC ---
agent = DRLAgent(env=env_train)
SAC_PARAMS = {
    "batch_size": 128,
    "buffer_size": 100000,
    "learning_rate": 0.0001,
    "learning_starts": 100,
    "ent_coef": "auto_0.1",
}
model_sac = agent.get_model("sac", model_kwargs=SAC_PARAMS)
if if_using_sac:
    tmp_path = RESULTS_DIR + "/sac"
    new_logger_sac = configure(tmp_path, ["stdout", "csv", "tensorboard"])
    model_sac.set_logger(new_logger_sac)

trained_sac = (
    agent.train_model(model=model_sac, tb_log_name="sac", total_timesteps=20000)
    if if_using_sac
    else None
)
if if_using_sac:
    trained_sac.save(TRAINED_MODEL_DIR + "/agent_sac")

print("All agents trained and saved to", TRAINED_MODEL_DIR)

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
