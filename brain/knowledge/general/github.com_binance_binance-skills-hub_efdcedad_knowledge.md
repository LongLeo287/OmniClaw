---
id: github.com-binance-binance-skills-hub-efdcedad-kno
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:34.135314
---

# KNOWLEDGE EXTRACT: github.com_binance_binance-skills-hub_efdcedad
> **Extracted on:** 2026-04-01 16:55:01
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007525406/github.com_binance_binance-skills-hub_efdcedad

---

## File: `README.md`
```markdown
# Binance Skills Hub

Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. Search tokens, execute trades, track wallets, monitor signals, and interact with DeFi protocols, all through natural language.

Built by Binance. Built for everyone.

We're not building this just for Binance products. Skills Hub is designed for the entire crypto ecosystem: any agent, any framework, any chain. Whether you're building on LangChain, CrewAI, or your own stack, your agents can plug into crypto with a few lines of config.

---

## About This Repository

Each skill lives in its own folder and contains a `SKILL.md` file with YAML frontmatter and structured instructions.

Browse the existing skills to understand patterns and naming conventions before contributing.

---

## Installation

Get started with Binance Skills Hub in a single command. Works with various agents such as OpenClaw and Claude Code.

### Prerequisites

Before installing Binance Skills Hub, ensure you have the following prerequisites:

* **Node.js** (version 22 or higher)

### Install Skills Hub

Run the following command to add Binance Skills Hub to your project:

```bash
npx skills add https://github.com/binance/binance-skills-hub
```

### Authentication

For Binance Skills, certain endpoints require you to provide Binance API credentials. You can do this by setting environment variables, using a secrets file (such as `.env` or `.openclaw/secrets.env`) , or sending them directly to the agent in the chat. For more details, see the [Security](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md#security) section in each skill.

---

## Contribution

We welcome contributions.

To add a new skill:

1. **Fork the repository** and create a new branch:

   ```bash
   git checkout -b feature/<skill-name>
   ```

2. **Create a new folder** containing a `SKILL.md` file.

3. **Follow the required format:**

   ```markdown
   ---
   title: <Skill Name>
   description: A clear description of what the skill does and when to use it.
   metadata:
     version: <Skill Version>
     author: <Your Github Username>
   license: MIT
   ---

   # <Skill Name>

   [Add instructions, examples, and guidelines here]
   ```

4. **Open a Pull Request** to `main` for review.
   Once approved, the skill will be merged.

---

## Disclaimer

Binance Skills Hub is an informational tool only. Binance Skills Hub and its outputs are provided to you on an “as is” and “as available” basis, without representation or warranty of any kind. It does not constitute investment, financial, trading or any other form of advice; represent a recommendation to buy, sell or hold any assets; guarantee the accuracy, timeliness or completeness of the data or analysis presented. Your use of Binance Skills Hub and any information provided in connection with this feature is at your own risk, and you are solely responsible for evaluating the information provided and for all trading decisions made by you. Binance does not endorse or guarantee any AI-generated information. Any AI-generated information or summary should not be solely relied on for decision making. AI-generated content may include or reflect information, views and opinions of third parties, and may also include errors, biases or outdated information. Binance is not responsible for any losses or damages incurred as a result of your use of or reliance on the Binance Skills Hub feature. Binance may modify or discontinue the Binance Skills Hub feature at its discretion, and functionality may vary by region or user profile. Digital asset prices are subject to high market risk and price volatility. The value of your investment may go down or up, and you may not get back the amount invested. You are solely responsible for your investment decisions and Binance is not liable for any losses you may incur. Past performance is not a reliable predictor of future performance. You should only invest in products you are familiar with and where you understand the risks. You should carefully consider your investment experience, financial situation, investment objectives and risk tolerance and consult an independent financial adviser prior to making any investment. This material should not be construed as advice. For more information, please see our [Risk Warning](https://www.binance.com/en/risk-warning) and [Terms of Use](https://www.binance.com/en/terms).
```

## File: `skills/binance/algo/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-19

- Initial release
```

## File: `skills/binance/algo/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/algo/SKILL.md`
```markdown
---
name: algo
description: Binance Algo request using the Binance API. Authentication requires API key and secret key. 
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/algo/SKILL.md
license: MIT
---

# Binance Algo Skill

Algo request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/sapi/v1/algo/futures/order` (DELETE) | Cancel Algo Order(TRADE) | algoId | recvWindow | Yes |
| `/sapi/v1/algo/futures/openOrders` (GET) | Query Current Algo Open Orders(USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/algo/futures/historicalOrders` (GET) | Query Historical Algo Orders(USER_DATA) | None | symbol, side, startTime, endTime, page, pageSize, recvWindow | Yes |
| `/sapi/v1/algo/futures/subOrders` (GET) | Query Sub Orders(USER_DATA) | algoId | page, pageSize, recvWindow | Yes |
| `/sapi/v1/algo/futures/newOrderTwap` (POST) | Time-Weighted Average Price(Twap) New Order(TRADE) | symbol, side, quantity, duration | positionSide, clientAlgoId, reduceOnly, limitPrice, recvWindow | Yes |
| `/sapi/v1/algo/futures/newOrderVp` (POST) | Volume Participation(VP) New Order (TRADE) | symbol, side, quantity, urgency | positionSide, clientAlgoId, reduceOnly, limitPrice, recvWindow | Yes |
| `/sapi/v1/algo/spot/order` (DELETE) | Cancel Algo Order(TRADE) | algoId | recvWindow | Yes |
| `/sapi/v1/algo/spot/openOrders` (GET) | Query Current Algo Open Orders(USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/algo/spot/historicalOrders` (GET) | Query Historical Algo Orders(USER_DATA) | None | symbol, side, startTime, endTime, page, pageSize, recvWindow | Yes |
| `/sapi/v1/algo/spot/subOrders` (GET) | Query Sub Orders(USER_DATA) | algoId | page, pageSize, recvWindow | Yes |
| `/sapi/v1/algo/spot/newOrderTwap` (POST) | Time-Weighted Average Price(Twap) New Order(TRADE) | symbol, side, quantity, duration | clientAlgoId, limitPrice | Yes |

---

## Parameters

### Common Parameters

* **algoId**: eg. 14511 (e.g., 1)
* **recvWindow**:  (e.g., 5000)
* **symbol**: Trading symbol eg. BTCUSDT (e.g., BTCUSDT)
* **side**: BUY or SELL (e.g., BUY)
* **startTime**: in milliseconds  eg.1641522717552 (e.g., 1623319461670)
* **endTime**: in milliseconds  eg.1641522526562 (e.g., 1641782889000)
* **page**: Default is 1 (e.g., 1)
* **pageSize**: MIN 1, MAX 100; Default 100 (e.g., 100)
* **symbol**: Trading symbol eg. BTCUSDT (e.g., BTCUSDT)
* **side**: Trading side ( BUY or SELL ) (e.g., BUY)
* **positionSide**: Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode. (e.g., BOTH)
* **quantity**: Quantity of base asset; Maximum notional per order is 200k, 2mm or 10mm, depending on symbol. Please reduce your size if you order is above the maximum notional per order. (e.g., 1.0)
* **duration**: Duration for TWAP orders in seconds. [300, 86400] (e.g., 5000)
* **clientAlgoId**: A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give default value (e.g., 1)
* **reduceOnly**: "true" or "false". Default "false"; Cannot be sent in Hedge Mode; Cannot be sent when you open a position
* **limitPrice**: Limit price of the order; If it is not sent, will place order by market price by default (e.g., 1.0)
* **urgency**: Represent the relative speed of the current execution; ENUM: LOW, MEDIUM, HIGH (e.g., LOW)


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://api.binance.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Description: Primary trading account

### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## User Agent Header

Include `User-Agent` header with the following string: `binance-algo/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/algo/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://api.binance.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-algo/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-algo/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X GET "https://api.binance.com/sapi/v1/algo/futures/openOrders" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-algo/1.1.0 (Skill)" \
  -d "timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://api.binance.com"  

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X GET "${BASE_URL}/sapi/v1/algo/futures/openOrders?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-algo/1.1.0 (Skill)"
```

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
```

## File: `skills/binance/alpha/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-10

- Initial release
```

## File: `skills/binance/alpha/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/alpha/SKILL.md`
```markdown
---
name: alpha
description: Binance Alpha request using the Binance API. Authentication requires API key and secret key. 
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/alpha/SKILL.md
license: MIT
---

# Binance Alpha Skill

Alpha request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/bapi/defi/v1/public/alpha-trade/ticker` (GET) | Ticker (24hr Price Statistics) | symbol | None | No |
| `/bapi/defi/v1/public/alpha-trade/agg-trades` (GET) | Aggregated Trades | symbol | fromId, startTime, endTime, limit | No |
| `/bapi/defi/v1/public/alpha-trade/get-exchange-info` (GET) | Get Exchange Info | None | None | No |
| `/bapi/defi/v1/public/alpha-trade/klines` (GET) | Klines (Candlestick Data) | symbol, interval | limit, startTime, endTime | No |
| `/bapi/defi/v1/public/wallet-direct/buw/wallet/cex/alpha/all/token/list` (GET) | Token List | None | None | No |

---

## Parameters

### Common Parameters

* **symbol**: e.g., "ALPHA_175USDT" – use token ID from Token List
* **fromId**: starting trade ID to fetch from (e.g., 1)
* **startTime**: start timestamp (milliseconds) (e.g., 1623319461670)
* **endTime**: end timestamp (milliseconds) (e.g., 1641782889000)
* **limit**: number of results to return (default 500, max 1000) (e.g., 500)
* **interval**: e.g., "1h" – supported intervals: 1s, 15s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://www.binance.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Description: Primary trading account


### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## User Agent Header

Include `User-Agent` header with the following string: `binance-alpha/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/alpha/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://www.binance.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-alpha/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`symbol=...&timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "symbol=...&timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "symbol=...&timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "symbol=...&timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`symbol=...&timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-alpha/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X GET "https://www.binance.com/bapi/defi/v1/public/alpha-trade/ticker" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-alpha/1.1.0 (Skill)" \
  -d "symbol=...&timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://www.binance.com"  

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="symbol=...&timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X GET "${BASE_URL}/bapi/defi/v1/public/alpha-trade/ticker?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-alpha/1.1.0 (Skill)"
```

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
```

## File: `skills/binance/assets/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-10

- Initial release
```

## File: `skills/binance/assets/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/assets/SKILL.md`
```markdown
---
name: assets
description: Binance Assets request using the Binance API. Authentication requires API key and secret key. 
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/assets/SKILL.md
license: MIT
---

# Binance Assets Skill

Assets request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/sapi/v1/account/apiTradingStatus` (GET) | Account API Trading Status (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/account/info` (GET) | Account info (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/account/status` (GET) | Account Status (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/account/apiRestrictions` (GET) | Get API Key Permission (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/accountSnapshot` (GET) | Daily Account Snapshot (USER_DATA) | type | startTime, endTime, limit, recvWindow | Yes |
| `/sapi/v1/account/disableFastWithdrawSwitch` (POST) | Disable Fast Withdraw Switch (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/account/enableFastWithdrawSwitch` (POST) | Enable Fast Withdraw Switch (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/bnbBurn` (POST) | Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA) | None | spotBNBBurn, interestBNBBurn, recvWindow | Yes |
| `/sapi/v1/vault/assets/assetDetail` (GET) | Asset Detail (USER_DATA) | None | asset, recvWindow | Yes |
| `/sapi/v1/vault/assets/dust-btc` (POST) | Get Assets That Can Be Converted Into BNB (USER_DATA) | None | accountType, recvWindow | Yes |
| `/sapi/v1/vault/assets/assetDividend` (GET) | Asset Dividend Record (USER_DATA) | None | asset, startTime, endTime, limit, recvWindow | Yes |
| `/sapi/v1/vault/assets/ledger-transfer/cloud-mining/queryByPage` (GET) | Get Cloud-Mining payment and refund history (USER_DATA) | startTime, endTime | tranId, clientTranId, asset, current, size | Yes |
| `/sapi/v1/vault/assets/dust-convert/convert` (POST) | Dust Convert (USER_DATA) | asset | clientId, targetAsset, thirdPartyClientId, dustQuotaAssetToTargetAssetPrice | Yes |
| `/sapi/v1/vault/assets/dust-convert/query-convertible-assets` (POST) | Dust Convertible Assets (USER_DATA) | targetAsset | dustQuotaAssetToTargetAssetPrice | Yes |
| `/sapi/v1/vault/assets/dribblet` (GET) | DustLog(USER_DATA) | None | accountType, startTime, endTime, recvWindow | Yes |
| `/sapi/v1/vault/assets/dust` (POST) | Dust Transfer (USER_DATA) | asset | accountType, recvWindow | Yes |
| `/sapi/v1/vault/assets/get-funding-asset` (POST) | Funding Wallet (USER_DATA) | None | asset, needBtcValuation, recvWindow | Yes |
| `/sapi/v1/spot/open-symbol-list` (GET) | Get Open Symbol List (MARKET_DATA) | None | None | No |
| `/sapi/v1/vault/assets/custody/transfer-history` (GET) | Query User Delegation History(For Master Account)(USER_DATA) | email, startTime, endTime | type, asset, current, size, recvWindow | Yes |
| `/sapi/v1/vault/assets/transfer` (GET) | Query User Universal Transfer History(USER_DATA) | type | startTime, endTime, current, size, fromSymbol, toSymbol, recvWindow | Yes |
| `/sapi/v1/vault/assets/transfer` (POST) | User Universal Transfer (USER_DATA) | type, asset, amount | fromSymbol, toSymbol, recvWindow | Yes |
| `/sapi/v1/vault/assets/wallet/balance` (GET) | Query User Wallet Balance (USER_DATA) | None | quoteAsset, recvWindow | Yes |
| `/sapi/v1/spot/delist-schedule` (GET) | Get symbols delist schedule for spot (MARKET_DATA) | None | recvWindow | No |
| `/sapi/v1/vault/assets/tradeFee` (GET) | Trade Fee (USER_DATA) | None | symbol, recvWindow | Yes |
| `/sapi/v3/vault/assets/getUserAsset` (POST) | User Asset (USER_DATA) | None | asset, needBtcValuation, recvWindow | Yes |
| `/sapi/v1/capital/config/getall` (GET) | All Coins' Information (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/capital/deposit/address` (GET) | Deposit Address(supporting network) (USER_DATA) | coin | network, amount, recvWindow | Yes |
| `/sapi/v1/capital/deposit/hisrec` (GET) | Deposit History (supporting network) (USER_DATA) | None | includeSource, coin, status, startTime, endTime, offset, limit, recvWindow, txId | Yes |
| `/sapi/v1/capital/deposit/address/list` (GET) | Fetch deposit address list with network(USER_DATA) | coin | network | Yes |
| `/sapi/v1/capital/withdraw/address/list` (GET) | Fetch withdraw address list (USER_DATA) | None | None | Yes |
| `/sapi/v1/capital/withdraw/quota` (GET) | Fetch withdraw quota (USER_DATA) | None | None | Yes |
| `/sapi/v1/capital/deposit/credit-apply` (POST) | One click arrival deposit apply (for expired address deposit) (USER_DATA) | None | depositId, txId, subAccountId, subUserId | Yes |
| `/sapi/v1/capital/withdraw/history` (GET) | Withdraw History (supporting network) (USER_DATA) | None | coin, withdrawOrderId, status, offset, limit, idList, startTime, endTime, recvWindow | Yes |
| `/sapi/v1/capital/withdraw/apply` (POST) | Withdraw(USER_DATA) | coin, address, amount | withdrawOrderId, network, addressTag, transactionFeeFlag, name, walletType, recvWindow | Yes |
| `/sapi/v1/core/status` (GET) | System Status (System) | None | None | No |
| `/sapi/v1/addressVerify/list` (GET) | Fetch address verification list (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/localentity/broker/deposit/provide-info` (PUT) | Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA) | subAccountId, depositId, questionnaire, beneficiaryPii, signature | network, coin, amount, address, addressTag | Yes |
| `/sapi/v1/localentity/broker/withdraw/apply` (POST) | Broker Withdraw (for brokers of local entities that require travel rule) (USER_DATA) | address, coin, amount, withdrawOrderId, questionnaire, originatorPii, signature | addressTag, network, addressName, transactionFeeFlag, walletType | Yes |
| `/sapi/v2/localentity/deposit/history` (GET) | Deposit History V2 (for local entities that required travel rule) (supporting network) (USER_DATA) | None | depositId, txId, network, coin, retrieveQuestionnaire, startTime, endTime, offset, limit | Yes |
| `/sapi/v1/localentity/deposit/history` (GET) | Deposit History (for local entities that required travel rule) (supporting network) (USER_DATA) | None | trId, txId, tranId, network, coin, travelRuleStatus, pendingQuestionnaire, startTime, endTime, offset, limit | Yes |
| `/sapi/v2/localentity/deposit/provide-info` (PUT) | Submit Deposit Questionnaire V2 (For local entities that require travel rule) (supporting network) (USER_DATA) | depositId, questionnaire | None | Yes |
| `/sapi/v1/localentity/deposit/provide-info` (PUT) | Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA) | tranId, questionnaire | None | Yes |
| `/sapi/v1/localentity/vasp` (GET) | VASP list (for local entities that require travel rule) (supporting network) (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/localentity/questionnaire-requirements` (GET) | Check Questionnaire Requirements (for local entities that require travel rule) (supporting network) (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v2/localentity/withdraw/history` (GET) | Withdraw History V2 (for local entities that require travel rule) (supporting network) (USER_DATA) | None | trId, txId, withdrawOrderId, network, coin, travelRuleStatus, offset, limit, startTime, endTime, recvWindow | Yes |
| `/sapi/v1/localentity/withdraw/history` (GET) | Withdraw History (for local entities that require travel rule) (supporting network) (USER_DATA) | None | trId, txId, withdrawOrderId, network, coin, travelRuleStatus, offset, limit, startTime, endTime, recvWindow | Yes |
| `/sapi/v1/localentity/withdraw/apply` (POST) | Withdraw (for local entities that require travel rule) (USER_DATA) | coin, address, amount, questionnaire | withdrawOrderId, network, addressTag, transactionFeeFlag, name, walletType, recvWindow | Yes |

---

## Parameters

### Common Parameters

* **recvWindow**:  (e.g., 5000)
* **type**: 
* **startTime**:  (e.g., 1623319461670)
* **endTime**:  (e.g., 1641782889000)
* **limit**: min 7, max 30, default 7 (e.g., 7)
* **spotBNBBurn**: "true" or "false"; Determines whether to use BNB to pay for trading fees on SPOT
* **interestBNBBurn**: "true" or "false"; Determines whether to use BNB to pay for margin loan's interest
* **asset**: If asset is blank, then query all positive assets user have.
* **accountType**: `SPOT` or `MARGIN`,default `SPOT` (e.g., SPOT)
* **tranId**: The transaction id (e.g., 1)
* **clientTranId**: The unique flag (e.g., 1)
* **startTime**:  (e.g., 1623319461670)
* **endTime**:  (e.g., 1641782889000)
* **current**: current page, default 1, the min value is 1 (e.g., 1)
* **size**: page size, default 10, the max value is 100 (e.g., 10)
* **asset**: 
* **clientId**: A unique id for the request (e.g., 1)
* **targetAsset**: 
* **thirdPartyClientId**:  (e.g., 1)
* **dustQuotaAssetToTargetAssetPrice**:  (e.g., 1.0)
* **targetAsset**: 
* **needBtcValuation**: true or false
* **email**: 
* **type**: Delegate/Undelegate
* **fromSymbol**: 
* **toSymbol**: 
* **quoteAsset**: `USDT`, `ETH`, `USDC`, `BNB`, etc. default `BTC` (e.g., BTC)
* **symbol**: 
* **needBtcValuation**: Whether need btc valuation or not.
* **amount**:  (e.g., 1.0)
* **coin**: 
* **network**: 
* **amount**:  (e.g., 1.0)
* **includeSource**: Default: `false`, return `sourceAddress`field when set to `true`
* **coin**: 
* **status**: 0(0:Email Sent, 2:Awaiting Approval 3:Rejected 4:Processing 6:Completed)
* **offset**: Default: 0
* **txId**:  (e.g., 1)
* **depositId**: Deposit record Id, priority use (e.g., 1)
* **subAccountId**: Sub-accountId of Cloud user (e.g., 1)
* **subUserId**: Sub-userId of parent user (e.g., 1)
* **withdrawOrderId**: client side id for withdrawal, if provided in POST `/sapi/v1/capital/withdraw/apply`, can be used here for query. (e.g., 1)
* **idList**: id list returned in the response of POST `/sapi/v1/capital/withdraw/apply`, separated by `,`
* **address**: 
* **addressTag**: Secondary address identifier for coins like XRP,XMR etc.
* **transactionFeeFlag**: When making internal transfer, `true` for returning the fee to the destination account; `false` for returning the fee back to the departure account. Default `false`.
* **name**: Description of the address. Address book cap is 200, space in name should be encoded into `%20`
* **walletType**: The wallet type for withdraw，0-spot wallet ，1-funding wallet. Default walletType is the current "selected wallet" under wallet->Fiat and Spot/Funding->Deposit
* **subAccountId**: External user ID. (e.g., 1)
* **depositId**: Wallet deposit ID (e.g., 1)
* **questionnaire**: JSON format questionnaire answers.
* **beneficiaryPii**: JSON format beneficiary Pii.
* **address**: 
* **signature**: Must be the last parameter.
* **addressName**: Description of the address. Address book cap is 200, space in name should be encoded into `%20`
* **withdrawOrderId**: withdrawID defined by the client (i.e. client's internal withdrawID) (e.g., 1)
* **originatorPii**: JSON format originator Pii, see StandardPii section below
* **depositId**: Comma(,) separated list of wallet tran Ids. (e.g., 1)
* **retrieveQuestionnaire**: true: return `questionnaire` within response.
* **trId**: Comma(,) separated list of travel rule record Ids. (e.g., 1)
* **tranId**: Comma(,) separated list of wallet tran Ids. (e.g., 1)
* **travelRuleStatus**: 0:Completed,1:Pending,2:Failed
* **pendingQuestionnaire**: true: Only return records that pending deposit questionnaire. false/not provided: return all records.
* **tranId**: Wallet tran ID (e.g., 1)


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://api.binance.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Description: Primary trading account


### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## User Agent Header

Include `User-Agent` header with the following string: `binance-wallet/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/assets/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://api.binance.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-wallet/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-wallet/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X GET "https://api.binance.com/sapi/v1/account/apiTradingStatus" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-wallet/1.1.0 (Skill)" \
  -d "timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://api.binance.com"  

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X GET "${BASE_URL}/sapi/v1/account/apiTradingStatus?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-wallet/1.1.0 (Skill)"
```

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
```

## File: `skills/binance/convert/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-17

- Initial release
```

## File: `skills/binance/convert/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/convert/SKILL.md`
```markdown
---
name: convert
description: Binance Convert request using the Binance API. Authentication requires API key and secret key. 
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/convert/SKILL.md
license: MIT
---

# Binance Convert Skill

Convert request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/sapi/v1/convert/exchangeInfo` (GET) | List All Convert Pairs | None | fromAsset, toAsset | No |
| `/sapi/v1/convert/assetInfo` (GET) | Query order quantity precision per asset(USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/convert/acceptQuote` (POST) | Accept Quote (TRADE) | quoteId | recvWindow | Yes |
| `/sapi/v1/convert/limit/cancelOrder` (POST) | Cancel limit order (USER_DATA) | orderId | recvWindow | Yes |
| `/sapi/v1/convert/tradeFlow` (GET) | Get Convert Trade History(USER_DATA) | startTime, endTime | limit, recvWindow | Yes |
| `/sapi/v1/convert/orderStatus` (GET) | Order status(USER_DATA) | None | orderId, quoteId | Yes |
| `/sapi/v1/convert/limit/placeOrder` (POST) | Place limit order (USER_DATA) | baseAsset, quoteAsset, limitPrice, side, expiredType | baseAmount, quoteAmount, walletType, recvWindow | Yes |
| `/sapi/v1/convert/limit/queryOpenOrders` (GET) | Query limit open orders (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/convert/getQuote` (POST) | Send Quote Request(USER_DATA) | fromAsset, toAsset | fromAmount, toAmount, walletType, validTime, recvWindow | Yes |

---

## Parameters

### Common Parameters

* **fromAsset**: User spends coin
* **toAsset**: User receives coin
* **recvWindow**: The value cannot be greater than 60000 (e.g., 5000)
* **quoteId**:  (e.g., 1)
* **orderId**: The orderId from `placeOrder` api (e.g., 1)
* **startTime**:  (e.g., 1623319461670)
* **endTime**:  (e.g., 1641782889000)
* **limit**: Default 100, Max 1000 (e.g., 100)
* **orderId**: Either orderId or quoteId is required (e.g., 1)
* **quoteId**: Either orderId or quoteId is required (e.g., 1)
* **baseAsset**: base asset (use the response `fromIsBase` from `GET /sapi/v1/convert/exchangeInfo` api to check which one is baseAsset )
* **quoteAsset**: quote asset
* **limitPrice**: Symbol limit price (from baseAsset to quoteAsset) (e.g., 1.0)
* **baseAmount**: Base asset amount.  (One of `baseAmount` or `quoteAmount` is required) (e.g., 1.0)
* **quoteAmount**: Quote asset amount.  (One of `baseAmount` or `quoteAmount` is required) (e.g., 1.0)
* **side**: `BUY` or `SELL` (e.g., BUY)
* **walletType**: It is to choose which wallet of assets. The wallet selection is `SPOT`, `FUNDING` and `EARN`. Combination of wallet is supported i.e. `SPOT_FUNDING`, `FUNDING_EARN`, `SPOT_FUNDING_EARN` or `SPOT_EARN`  Default is `SPOT`.
* **expiredType**: 1_D, 3_D, 7_D, 30_D  (D means day)
* **fromAsset**: 
* **toAsset**: 
* **fromAmount**: When specified, it is the amount you will be debited after the conversion (e.g., 1.0)
* **toAmount**: When specified, it is the amount you will be credited after the conversion (e.g., 1.0)
* **validTime**: 10s, 30s, 1m, default 10s (e.g., 10s)


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://api.binance.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Description: Primary trading account

### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## User Agent Header

Include `User-Agent` header with the following string: `binance-convert/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/convert/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://api.binance.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-convert/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-convert/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X GET "https://api.binance.com/sapi/v1/convert/exchangeInfo" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-convert/1.1.0 (Skill)" \
  -d "timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://api.binance.com"  

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X GET "${BASE_URL}/sapi/v1/convert/exchangeInfo?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-convert/1.1.0 (Skill)"
```

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
```

## File: `skills/binance/derivatives-trading-coin-futures/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-19

- Initial release
```

## File: `skills/binance/derivatives-trading-coin-futures/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/derivatives-trading-coin-futures/SKILL.md`
```markdown
---
name: derivatives-trading-coin-futures
description: Binance Derivatives-trading-coin-futures request using the Binance API. Authentication requires API key and secret key. Supports testnet and mainnet.
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/derivatives-trading-coin-futures/SKILL.md
license: MIT
---

# Binance Derivatives-trading-coin-futures Skill

Derivatives-trading-coin-futures request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/dapi/v1/account` (GET) | Account Information (USER_DATA) | None | recvWindow | Yes |
| `/dapi/v1/balance` (GET) | Futures Account Balance (USER_DATA) | None | recvWindow | Yes |
| `/dapi/v1/positionSide/dual` (GET) | Get Current Position Mode(USER_DATA) | None | recvWindow | Yes |
| `/dapi/v1/positionSide/dual` (POST) | Change Position Mode(TRADE) | dualSidePosition | recvWindow | Yes |
| `/dapi/v1/order/asyn` (GET) | Get Download Id For Futures Order History (USER_DATA) | startTime, endTime | recvWindow | Yes |
| `/dapi/v1/trade/asyn` (GET) | Get Download Id For Futures Trade History (USER_DATA) | startTime, endTime | recvWindow | Yes |
| `/dapi/v1/income/asyn` (GET) | Get Download Id For Futures Transaction History(USER_DATA) | startTime, endTime | recvWindow | Yes |
| `/dapi/v1/order/asyn/id` (GET) | Get Futures Order History Download Link by Id (USER_DATA) | downloadId | recvWindow | Yes |
| `/dapi/v1/trade/asyn/id` (GET) | Get Futures Trade Download Link by Id(USER_DATA) | downloadId | recvWindow | Yes |
| `/dapi/v1/income/asyn/id` (GET) | Get Futures Transaction History Download Link by Id (USER_DATA) | downloadId | recvWindow | Yes |
| `/dapi/v1/income` (GET) | Get Income History(USER_DATA) | None | symbol, incomeType, startTime, endTime, page, limit, recvWindow | Yes |
| `/dapi/v1/leverageBracket` (GET) | Notional Bracket for Pair(USER_DATA) | None | pair, recvWindow | Yes |
| `/dapi/v2/leverageBracket` (GET) | Notional Bracket for Symbol(USER_DATA) | None | symbol, recvWindow | Yes |
| `/dapi/v1/commissionRate` (GET) | User Commission Rate (USER_DATA) | symbol | recvWindow | Yes |
| `/dapi/v1/ticker/24hr` (GET) | 24hr Ticker Price Change Statistics | None | symbol, pair | No |
| `/futures/data/basis` (GET) | Basis | pair, contractType, period | limit, startTime, endTime | No |
| `/dapi/v1/time` (GET) | Check Server time | None | None | No |
| `/dapi/v1/aggTrades` (GET) | Compressed/Aggregate Trades List | symbol | fromId, startTime, endTime, limit | No |
| `/dapi/v1/continuousKlines` (GET) | Continuous Contract Kline/Candlestick Data | pair, contractType, interval | startTime, endTime, limit | No |
| `/dapi/v1/exchangeInfo` (GET) | Exchange Information | None | None | No |
| `/dapi/v1/fundingInfo` (GET) | Get Funding Rate Info | None | None | No |
| `/dapi/v1/fundingRate` (GET) | Get Funding Rate History of Perpetual Futures | symbol | startTime, endTime, limit | No |
| `/dapi/v1/constituents` (GET) | Query Index Price Constituents | symbol | None | No |
| `/dapi/v1/indexPriceKlines` (GET) | Index Price Kline/Candlestick Data | pair, interval | startTime, endTime, limit | No |
| `/dapi/v1/premiumIndex` (GET) | Index Price and Mark Price | None | symbol, pair | No |
| `/dapi/v1/klines` (GET) | Kline/Candlestick Data | symbol, interval | startTime, endTime, limit | No |
| `/futures/data/globalLongShortAccountRatio` (GET) | Long/Short Ratio | pair, period | limit, startTime, endTime | No |
| `/dapi/v1/markPriceKlines` (GET) | Mark Price Kline/Candlestick Data | symbol, interval | startTime, endTime, limit | No |
| `/dapi/v1/historicalTrades` (GET) | Old Trades Lookup(MARKET_DATA) | symbol | limit, fromId | No |
| `/futures/data/openInterestHist` (GET) | Open Interest Statistics | pair, contractType, period | limit, startTime, endTime | No |
| `/dapi/v1/openInterest` (GET) | Open Interest | symbol | None | No |
| `/dapi/v1/depth` (GET) | Order Book | symbol | limit | No |
| `/dapi/v1/premiumIndexKlines` (GET) | Premium index Kline Data | symbol, interval | startTime, endTime, limit | No |
| `/dapi/v1/trades` (GET) | Recent Trades List | symbol | limit | No |
| `/dapi/v1/ticker/bookTicker` (GET) | Symbol Order Book Ticker | None | symbol, pair | No |
| `/dapi/v1/ticker/price` (GET) | Symbol Price Ticker | None | symbol, pair | No |
| `/futures/data/takerBuySellVol` (GET) | Taker Buy/Sell Volume | pair, contractType, period | limit, startTime, endTime | No |
| `/dapi/v1/ping` (GET) | Test Connectivity | None | None | No |
| `/futures/data/topLongShortAccountRatio` (GET) | Top Trader Long/Short Ratio (Accounts) | symbol, period | limit, startTime, endTime | No |
| `/futures/data/topLongShortPositionRatio` (GET) | Top Trader Long/Short Ratio (Positions) | pair, period | limit, startTime, endTime | No |
| `/dapi/v1/pmAccountInfo` (GET) | Classic Portfolio Margin Account Information (USER_DATA) | asset | recvWindow | Yes |
| `/dapi/v1/userTrades` (GET) | Account Trade List (USER_DATA) | None | symbol, pair, orderId, startTime, endTime, fromId, limit, recvWindow | Yes |
| `/dapi/v1/allOrders` (GET) | All Orders (USER_DATA) | None | symbol, pair, orderId, startTime, endTime, limit, recvWindow | Yes |
| `/dapi/v1/countdownCancelAll` (POST) | Auto-Cancel All Open Orders (TRADE) | symbol, countdownTime | recvWindow | Yes |
| `/dapi/v1/allOpenOrders` (DELETE) | Cancel All Open Orders(TRADE) | symbol | recvWindow | Yes |
| `/dapi/v1/batchOrders` (DELETE) | Cancel Multiple Orders(TRADE) | symbol | orderIdList, origClientOrderIdList, recvWindow | Yes |
| `/dapi/v1/batchOrders` (PUT) | Modify Multiple Orders(TRADE) | batchOrders | recvWindow | Yes |
| `/dapi/v1/batchOrders` (POST) | Place Multiple Orders(TRADE) | batchOrders | recvWindow | Yes |
| `/dapi/v1/order` (DELETE) | Cancel Order (TRADE) | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/dapi/v1/order` (PUT) | Modify Order (TRADE) | symbol, side | orderId, origClientOrderId, quantity, price, priceMatch, recvWindow | Yes |
| `/dapi/v1/order` (POST) | New Order (TRADE) | symbol, side, type | positionSide, timeInForce, quantity, reduceOnly, price, newClientOrderId, stopPrice, closePosition, activationPrice, callbackRate, workingType, priceProtect, newOrderRespType, priceMatch, selfTradePreventionMode, recvWindow | Yes |
| `/dapi/v1/order` (GET) | Query Order (USER_DATA) | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/dapi/v1/leverage` (POST) | Change Initial Leverage (TRADE) | symbol, leverage | recvWindow | Yes |
| `/dapi/v1/marginType` (POST) | Change Margin Type (TRADE) | symbol, marginType | recvWindow | Yes |
| `/dapi/v1/openOrders` (GET) | Current All Open Orders (USER_DATA) | None | symbol, pair, recvWindow | Yes |
| `/dapi/v1/orderAmendment` (GET) | Get Order Modify History (USER_DATA) | symbol | orderId, origClientOrderId, startTime, endTime, limit, recvWindow | Yes |
| `/dapi/v1/positionMargin/history` (GET) | Get Position Margin Change History(TRADE) | symbol | type, startTime, endTime, limit, recvWindow | Yes |
| `/dapi/v1/positionMargin` (POST) | Modify Isolated Position Margin(TRADE) | symbol, amount, type | positionSide, recvWindow | Yes |
| `/dapi/v1/adlQuantile` (GET) | Position ADL Quantile Estimation(USER_DATA) | None | symbol, recvWindow | Yes |
| `/dapi/v1/positionRisk` (GET) | Position Information(USER_DATA) | None | marginAsset, pair, recvWindow | Yes |
| `/dapi/v1/openOrder` (GET) | Query Current Open Order(USER_DATA) | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/dapi/v1/forceOrders` (GET) | User's Force Orders(USER_DATA) | None | symbol, autoCloseType, startTime, endTime, limit, recvWindow | Yes |
| `/dapi/v1/listenKey` (DELETE) | Close User Data Stream(USER_STREAM) | None | None | No |
| `/dapi/v1/listenKey` (PUT) | Keepalive User Data Stream (USER_STREAM) | None | None | No |
| `/dapi/v1/listenKey` (POST) | Start User Data Stream (USER_STREAM) | None | None | No |

---

## Parameters

### Common Parameters

* **recvWindow**:  (e.g., 5000)
* **startTime**: Timestamp in ms (e.g., 1623319461670)
* **endTime**: Timestamp in ms (e.g., 1641782889000)
* **downloadId**: get by download id api (e.g., 1)
* **symbol**: 
* **incomeType**: "TRANSFER","WELCOME_BONUS", "FUNDING_FEE", "REALIZED_PNL", "COMMISSION", "INSURANCE_CLEAR", and "DELIVERED_SETTELMENT"
* **startTime**:  (e.g., 1623319461670)
* **endTime**:  (e.g., 1641782889000)
* **page**: 
* **limit**: Default 100; max 1000 (e.g., 100)
* **pair**: 
* **symbol**: 
* **pair**: BTCUSD
* **fromId**: ID to get aggregate trades from INCLUSIVE. (e.g., 1)
* **asset**: 
* **orderId**:  (e.g., 1)
* **orderId**:  (e.g., 1)
* **countdownTime**: countdown time, 1000 for 1 second. 0 to cancel the timer
* **orderIdList**: max length 10   e.g. [1234567,2345678]
* **origClientOrderIdList**: max length 10  e.g. ["my_id_1","my_id_2"], encode the double quotes. No space after comma.
* **origClientOrderId**:  (e.g., 1)
* **leverage**: target initial leverage: int from 1 to 125
* **dualSidePosition**: "true": Hedge Mode; "false": One-way Mode
* **type**: 1: Add position margin,2: Reduce position margin
* **amount**:  (e.g., 1.0)
* **batchOrders**: order list. Max 5 orders
* **quantity**: quantity measured by contract number, Cannot be sent with `closePosition`=`true` (e.g., 1.0)
* **price**:  (e.g., 1.0)
* **reduceOnly**: "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true`(Close-All)
* **newClientOrderId**: A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$` (e.g., 1)
* **stopPrice**: Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders. (e.g., 1.0)
* **closePosition**: `true`, `false`；Close-All,used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`.
* **activationPrice**: Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting different `workingType`) (e.g., 1.0)
* **callbackRate**: Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 10 where 1 for 1% (e.g., 1.0)
* **priceProtect**: "TRUE" or "FALSE", default "FALSE". Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.
* **batchOrders**: order list. Max 5 orders
* **marginAsset**: 


### Enums

* **contractType**: PERPETUAL | CURRENT_QUARTER | NEXT_QUARTER | CURRENT_QUARTER_DELIVERING | NEXT_QUARTER_DELIVERING | PERPETUAL_DELIVERING
* **period**: 5m | 15m | 30m | 1h | 2h | 4h | 6h | 12h | 1d
* **interval**: 1m | 3m | 5m | 15m | 30m | 1h | 2h | 4h | 6h | 8h | 12h | 1d | 3d | 1w | 1M
* **marginType**: ISOLATED | CROSSED
* **positionSide**: BOTH | LONG | SHORT
* **type**: LIMIT | MARKET | STOP | STOP_MARKET | TAKE_PROFIT | TAKE_PROFIT_MARKET | TRAILING_STOP_MARKET
* **side**: BUY | SELL
* **priceMatch**: NONE | OPPONENT | OPPONENT_5 | OPPONENT_10 | OPPONENT_20 | QUEUE | QUEUE_5 | QUEUE_10 | QUEUE_20
* **timeInForce**: GTC | IOC | FOK | GTX
* **workingType**: MARK_PRICE | CONTRACT_PRICE
* **newOrderRespType**: ACK | RESULT
* **selfTradePreventionMode**: NONE | EXPIRE_TAKER | EXPIRE_BOTH | EXPIRE_MAKER
* **autoCloseType**: LIQUIDATION | ADL


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://dapi.binance.com
* Testnet: https://testnet.binancefuture.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`
- Testnet: `BINANCE_TESTNET_API_KEY` and `BINANCE_TESTNET_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1
Environment: Mainnet

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet/Testnet)
* testnet-dev (Testnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret
- Testnet: false 

### testnet-dev
- API Key: your_testnet_api_key
- Secret: your_testnet_secret
- Testnet: true

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Testnet: false
- Description: Primary trading account

### testnet-dev
- API Key: test456...abc
- Secret: testsecret...xyz
- Testnet: true
- Description: Development/testing

### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Testnet: false
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode
6. When a request requires signing, if the request isn't an order and the API keys aren't described as `mainnet` or `testnet` keys, try to make request to the different base urls and see if it works, without asking the user. If it works, store the keys with the corresponding environment.

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Ask: Mainnet, Testnet 
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## New Client Order ID 

For endpoints that include the `newClientOrderId` parameter, the value must always start with `agent-`. If the parameter is not provided, `agent-` followed by 18 random alphanumeric characters will be generated automatically. If a value is provided, it will be prefixed with `agent-`

Example: `agent-1a2b3c4d5e6f7g8h9i`

## User Agent Header

Include `User-Agent` header with the following string: `binance-derivatives-trading-coin-futures/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/derivatives-trading-coin-futures/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://dapi.binance.com |
| Testnet | https://testnet.binancefuture.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-derivatives-trading-coin-futures/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`symbol=BTCUSD_PERP&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "symbol=BTCUSD_PERP&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "symbol=BTCUSD_PERP&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "symbol=BTCUSD_PERP&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`symbol=BTCUSD_PERP&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-derivatives-trading-coin-futures/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X POST "https://dapi.binance.com/dapi/v1/order" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-derivatives-trading-coin-futures/1.1.0 (Skill)" \
  -d "symbol=BTCUSD_PERP&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://dapi.binance.com"  # or https://testnet.binancefuture.com

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="symbol=BTCUSD_PERP&side=BUY&type=MARKET&quantity=0.001&timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X POST "${BASE_URL}/dapi/v1/order?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-derivatives-trading-coin-futures/1.1.0 (Skill)"
```

If you get -1021 Timestamp outside recvWindow:

1. Check server time: GET /dapi/v1/time
2. Sync your clock or adjust timestamp
3. Increase recvWindow (max 60000ms)

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
* Use testnet for development: https://testnet.binancefuture.com
* Testnet credentials are separate from mainnet
```

## File: `skills/binance/derivatives-trading-options/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-19

- Initial release
```

## File: `skills/binance/derivatives-trading-options/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/derivatives-trading-options/SKILL.md`
```markdown
---
name: derivatives-trading-options
description: Binance Derivatives-trading-options request using the Binance API. Authentication requires API key and secret key. Supports testnet and mainnet.
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/derivatives-trading-options/SKILL.md
license: MIT
---

# Binance Derivatives-trading-options Skill

Derivatives-trading-options request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/eapi/v1/bill` (GET) | Account Funding Flow (USER_DATA) | currency | recordId, startTime, endTime, limit, recvWindow | Yes |
| `/eapi/v1/marginAccount` (GET) | Option Margin Account Information (USER_DATA) | None | recvWindow | Yes |
| `/eapi/v1/block/order/execute` (POST) | Accept Block Trade Order (TRADE) | blockOrderMatchingKey | recvWindow | Yes |
| `/eapi/v1/block/order/execute` (GET) | Query Block Trade Details (USER_DATA) | blockOrderMatchingKey | recvWindow | Yes |
| `/eapi/v1/block/user-trades` (GET) | Account Block Trade List (USER_DATA) | None | endTime, startTime, underlying, recvWindow | Yes |
| `/eapi/v1/block/order/create` (DELETE) | Cancel Block Trade Order (TRADE) | blockOrderMatchingKey | recvWindow | Yes |
| `/eapi/v1/block/order/create` (PUT) | Extend Block Trade Order (TRADE) | blockOrderMatchingKey | recvWindow | Yes |
| `/eapi/v1/block/order/create` (POST) | New Block Trade Order (TRADE) | liquidity, legs | recvWindow | Yes |
| `/eapi/v1/block/order/orders` (GET) | Query Block Trade Order (TRADE) | None | blockOrderMatchingKey, endTime, startTime, underlying, recvWindow | Yes |
| `/eapi/v1/ticker` (GET) | 24hr Ticker Price Change Statistics | None | symbol | No |
| `/eapi/v1/time` (GET) | Check Server Time | None | None | No |
| `/eapi/v1/exchangeInfo` (GET) | Exchange Information | None | None | No |
| `/eapi/v1/exerciseHistory` (GET) | Historical Exercise Records | None | underlying, startTime, endTime, limit | No |
| `/eapi/v1/klines` (GET) | Kline/Candlestick Data | symbol, interval | startTime, endTime, limit | No |
| `/eapi/v1/openInterest` (GET) | Open Interest | underlyingAsset, expiration | None | No |
| `/eapi/v1/mark` (GET) | Option Mark Price | None | symbol | No |
| `/eapi/v1/depth` (GET) | Order Book | symbol | limit | No |
| `/eapi/v1/blockTrades` (GET) | Recent Block Trades List | None | symbol, limit | No |
| `/eapi/v1/trades` (GET) | Recent Trades List | symbol | limit | No |
| `/eapi/v1/index` (GET) | Index Price | underlying | None | No |
| `/eapi/v1/ping` (GET) | Test Connectivity | None | None | No |
| `/eapi/v1/countdownCancelAllHeartBeat` (POST) | Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE) | underlyings | recvWindow | Yes |
| `/eapi/v1/countdownCancelAll` (GET) | Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE) | None | underlying, recvWindow | Yes |
| `/eapi/v1/countdownCancelAll` (POST) | Set Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE) | underlying, countdownTime | recvWindow | Yes |
| `/eapi/v1/mmp` (GET) | Get Market Maker Protection Config (TRADE) | None | underlying, recvWindow | Yes |
| `/eapi/v1/mmpReset` (POST) | Reset Market Maker Protection Config (TRADE) | None | underlying, recvWindow | Yes |
| `/eapi/v1/mmpSet` (POST) | Set Market Maker Protection Config (TRADE) | None | underlying, windowTimeInMilliseconds, frozenTimeInMilliseconds, qtyLimit, deltaLimit, recvWindow | Yes |
| `/eapi/v1/userTrades` (GET) | Account Trade List (USER_DATA) | None | symbol, fromId, startTime, endTime, limit, recvWindow | Yes |
| `/eapi/v1/allOpenOrdersByUnderlying` (DELETE) | Cancel All Option Orders By Underlying (TRADE) | underlying | recvWindow | Yes |
| `/eapi/v1/batchOrders` (DELETE) | Cancel Multiple Option Orders (TRADE) | symbol | orderIds, clientOrderIds, recvWindow | Yes |
| `/eapi/v1/batchOrders` (POST) | Place Multiple Orders(TRADE) | orders | recvWindow | Yes |
| `/eapi/v1/order` (DELETE) | Cancel Option Order (TRADE) | symbol | orderId, clientOrderId, recvWindow | Yes |
| `/eapi/v1/order` (POST) | New Order (TRADE) | symbol, side, type, quantity | price, timeInForce, reduceOnly, postOnly, newOrderRespType, clientOrderId, isMmp, recvWindow | Yes |
| `/eapi/v1/order` (GET) | Query Single Order (TRADE) | symbol | orderId, clientOrderId, recvWindow | Yes |
| `/eapi/v1/allOpenOrders` (DELETE) | Cancel all Option orders on specific symbol (TRADE) | symbol | recvWindow | Yes |
| `/eapi/v1/position` (GET) | Option Position Information (USER_DATA) | None | symbol, recvWindow | Yes |
| `/eapi/v1/openOrders` (GET) | Query Current Open Option Orders (USER_DATA) | None | symbol, orderId, startTime, endTime, recvWindow | Yes |
| `/eapi/v1/historyOrders` (GET) | Query Option Order History (TRADE) | symbol | orderId, startTime, endTime, limit, recvWindow | Yes |
| `/eapi/v1/commission` (GET) | User Commission (USER_DATA) | None | recvWindow | Yes |
| `/eapi/v1/exerciseRecord` (GET) | User Exercise Record (USER_DATA) | None | symbol, startTime, endTime, limit, recvWindow | Yes |
| `/eapi/v1/listenKey` (DELETE) | Close User Data Stream (USER_STREAM) | None | None | No |
| `/eapi/v1/listenKey` (PUT) | Keepalive User Data Stream (USER_STREAM) | None | None | No |
| `/eapi/v1/listenKey` (POST) | Start User Data Stream (USER_STREAM) | None | None | No |

---

## Parameters

### Common Parameters

* **currency**: Asset type, only support USDT  as of now
* **recordId**: Return the recordId and subsequent data, the latest data is returned by default, e.g 100000 (e.g., 1)
* **startTime**: Start Time, e.g 1593511200000 (e.g., 1623319461670)
* **endTime**: End Time, e.g 1593512200000 (e.g., 1641782889000)
* **limit**: Number of result sets returned Default:100 Max:1000 (e.g., 100)
* **recvWindow**:  (e.g., 5000)
* **blockOrderMatchingKey**: 
* **underlying**: underlying, e.g BTCUSDT
* **liquidity**: Taker or Maker
* **legs**: Max 1 (only single leg supported), list of legs parameters in JSON; example: eapi/v1/block/order/create?orders=[{"symbol":"BTC-210115-35000-C", "price":"100","quantity":"0.0002","side":"BUY","type":"LIMIT"}]
* **blockOrderMatchingKey**: If specified, returns the specific block trade associated with the blockOrderMatchingKey
* **symbol**: Option trading pair, e.g BTC-200730-9000-C
* **symbol**: Option trading pair, e.g BTC-200730-9000-C
* **interval**: Time interval
* **underlyingAsset**: underlying asset, e.g ETH/BTC
* **expiration**: expiration date, e.g 221225
* **underlying**: Option underlying, e.g BTCUSDT
* **underlyings**: Option Underlying Symbols, e.g BTCUSDT,ETHUSDT
* **countdownTime**: Countdown time in milliseconds (ex. 1,000 for 1 second). 0 to disable the timer. Negative values (ex. -10000) are not accepted. Minimum acceptable value is 5,000
* **windowTimeInMilliseconds**: MMP Interval in milliseconds; Range (0,5000]
* **frozenTimeInMilliseconds**: MMP frozen time in milliseconds, if set to 0 manual reset is required
* **qtyLimit**: quantity limit (e.g., 1.0)
* **deltaLimit**: net delta limit (e.g., 1.0)
* **fromId**: Trade id to fetch from. Default gets most recent trades, e.g 4611875134427365376 (e.g., 1)
* **orderIds**: Order ID, e.g [4611875134427365377,4611875134427365378]
* **clientOrderIds**: User-defined order ID, e.g ["my_id_1","my_id_2"]
* **orderId**: Order ID, e.g 4611875134427365377 (e.g., 1)
* **clientOrderId**: User-defined order ID, e.g 10000 (e.g., 1)
* **quantity**: Order Quantity (e.g., 1.0)
* **price**: Order Price (e.g., 1.0)
* **reduceOnly**: Reduce Only（Default false） (e.g., false）)
* **postOnly**: Post Only（Default false） (e.g., false）)
* **isMmp**: is market maker protection order, true/false
* **orders**: order list. Max 10 orders


### Enums

* **side**: BUY | SELL
* **type**: LIMIT
* **timeInForce**: GTC | IOC | FOK | GTX
* **newOrderRespType**: ACK | RESULT


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://eapi.binance.com
* Testnet: https://testnet.binancefuture.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`
- Testnet: `BINANCE_TESTNET_API_KEY` and `BINANCE_TESTNET_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1
Environment: Mainnet

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet/Testnet)
* testnet-dev (Testnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret
- Testnet: false 

### testnet-dev
- API Key: your_testnet_api_key
- Secret: your_testnet_secret
- Testnet: true

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Testnet: false
- Description: Primary trading account

### testnet-dev
- API Key: test456...abc
- Secret: testsecret...xyz
- Testnet: true
- Description: Development/testing

### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Testnet: false
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode
6. When a request requires signing, if the request isn't an order and the API keys aren't described as `mainnet` or `testnet` keys, try to make request to the different base urls and see if it works, without asking the user. If it works, store the keys with the corresponding environment.

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Ask: Mainnet, Testnet 
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## User Agent Header

Include `User-Agent` header with the following string: `binance-derivatives-trading-options/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/derivatives-trading-options/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://eapi.binance.com |
| Testnet | https://testnet.binancefuture.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-derivatives-trading-options/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`symbol=BTC-260327-120000-C&side=BUY&type=LIMIT&quantity=1&price=5&timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "symbol=BTC-260327-120000-C&side=BUY&type=LIMIT&quantity=1&price=5&timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "symbol=BTC-260327-120000-C&side=BUY&type=LIMIT&quantity=1&price=5&timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "symbol=BTC-260327-120000-C&side=BUY&type=LIMIT&quantity=1&price=5&timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`symbol=BTC-260327-120000-C&side=BUY&type=LIMIT&quantity=1&price=5&timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-derivatives-trading-options/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl --request POST \
  --url 'https://eapi.binance.com/eapi/v1/order?symbol=BTC-260327-120000-C&side=BUY&type=LIMIT&quantity=1&price=5&timeInForce=GTC&newOrderRespType=RESULT&recvWindow=999999999&timestamp=1772667645754&signature=...&selfProtectionMode=EXPIRE_BOTH' \
  -H "X-MBX-APIKEY: ${API_KEY}" \
  -H "User-Agent: binance-derivatives-trading-options/1.1.0 (Skill)"
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://eapi.binance.com"  # or https://testnet.binancefuture.com

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="symbol=BTC-260327-120000-C&side=BUY&type=LIMIT&quantity=1&price=5&timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X POST "${BASE_URL}/eapi/v1/order?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-derivatives-trading-options/1.1.0 (Skill)"
```

If you get -1021 Timestamp outside recvWindow:

1. Check server time: GET /eapi/v1/time
2. Sync your clock or adjust timestamp
3. Increase recvWindow (max 60000ms)

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
* Use testnet for development: https://testnet.binancefuture.com
* Testnet credentials are separate from mainnet
```

## File: `skills/binance/derivatives-trading-portfolio-margin/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-19

- Initial release
```

## File: `skills/binance/derivatives-trading-portfolio-margin/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/derivatives-trading-portfolio-margin/SKILL.md`
```markdown
---
name: derivatives-trading-portfolio-margin
description: Binance Derivatives-trading-portfolio-margin request using the Binance API. Authentication requires API key and secret key. Supports testnet and mainnet.
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/derivatives-trading-portfolio-margin/SKILL.md
license: MIT
---

# Binance Derivatives-trading-portfolio-margin Skill

Derivatives-trading-portfolio-margin request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/papi/v1/balance` (GET) | Account Balance(USER_DATA) | None | asset, recvWindow | Yes |
| `/papi/v1/account` (GET) | Account Information(USER_DATA) | None | recvWindow | Yes |
| `/papi/v1/bnb-transfer` (POST) | BNB transfer (TRADE) | amount, transferSide | recvWindow | Yes |
| `/papi/v1/cm/leverageBracket` (GET) | CM Notional and Leverage Brackets(USER_DATA) | None | symbol, recvWindow | Yes |
| `/papi/v1/repay-futures-switch` (POST) | Change Auto-repay-futures Status(TRADE) | autoRepay | recvWindow | Yes |
| `/papi/v1/repay-futures-switch` (GET) | Get Auto-repay-futures Status(USER_DATA) | None | recvWindow | Yes |
| `/papi/v1/cm/leverage` (POST) | Change CM Initial Leverage (TRADE) | symbol, leverage | recvWindow | Yes |
| `/papi/v1/cm/positionSide/dual` (POST) | Change CM Position Mode(TRADE) | dualSidePosition | recvWindow | Yes |
| `/papi/v1/cm/positionSide/dual` (GET) | Get CM Current Position Mode(USER_DATA) | None | recvWindow | Yes |
| `/papi/v1/um/leverage` (POST) | Change UM Initial Leverage(TRADE) | symbol, leverage | recvWindow | Yes |
| `/papi/v1/um/positionSide/dual` (POST) | Change UM Position Mode(TRADE) | dualSidePosition | recvWindow | Yes |
| `/papi/v1/um/positionSide/dual` (GET) | Get UM Current Position Mode(USER_DATA) | None | recvWindow | Yes |
| `/papi/v1/auto-collection` (POST) | Fund Auto-collection(TRADE) | None | recvWindow | Yes |
| `/papi/v1/asset-collection` (POST) | Fund Collection by Asset(TRADE) | asset | recvWindow | Yes |
| `/papi/v1/cm/account` (GET) | Get CM Account Detail(USER_DATA) | None | recvWindow | Yes |
| `/papi/v1/cm/income` (GET) | Get CM Income History(USER_DATA) | None | symbol, incomeType, startTime, endTime, page, limit, recvWindow | Yes |
| `/papi/v1/um/order/asyn` (GET) | Get Download Id For UM Futures Order History (USER_DATA) | startTime, endTime | recvWindow | Yes |
| `/papi/v1/um/trade/asyn` (GET) | Get Download Id For UM Futures Trade History (USER_DATA) | startTime, endTime | recvWindow | Yes |
| `/papi/v1/um/income/asyn` (GET) | Get Download Id For UM Futures Transaction History (USER_DATA) | startTime, endTime | recvWindow | Yes |
| `/papi/v1/margin/marginInterestHistory` (GET) | Get Margin Borrow/Loan Interest History(USER_DATA) | None | asset, startTime, endTime, current, size, archived, recvWindow | Yes |
| `/papi/v2/um/account` (GET) | Get UM Account Detail V2(USER_DATA) | None | recvWindow | Yes |
| `/papi/v1/um/account` (GET) | Get UM Account Detail(USER_DATA) | None | recvWindow | Yes |
| `/papi/v1/um/accountConfig` (GET) | UM Futures Account Configuration(USER_DATA) | None | recvWindow | Yes |
| `/papi/v1/um/order/asyn/id` (GET) | Get UM Futures Order Download Link by Id(USER_DATA) | downloadId | recvWindow | Yes |
| `/papi/v1/um/symbolConfig` (GET) | UM Futures Symbol Configuration(USER_DATA) | None | symbol, recvWindow | Yes |
| `/papi/v1/um/trade/asyn/id` (GET) | Get UM Futures Trade Download Link by Id(USER_DATA) | downloadId | recvWindow | Yes |
| `/papi/v1/um/income/asyn/id` (GET) | Get UM Futures Transaction Download Link by Id(USER_DATA) | downloadId | recvWindow | Yes |
| `/papi/v1/um/income` (GET) | Get UM Income History(USER_DATA) | None | symbol, incomeType, startTime, endTime, page, limit, recvWindow | Yes |
| `/papi/v1/cm/commissionRate` (GET) | Get User Commission Rate for CM(USER_DATA) | symbol | recvWindow | Yes |
| `/papi/v1/um/commissionRate` (GET) | Get User Commission Rate for UM(USER_DATA) | symbol | recvWindow | Yes |
| `/papi/v1/margin/maxBorrowable` (GET) | Margin Max Borrow(USER_DATA) | asset | recvWindow | Yes |
| `/papi/v1/um/apiTradingStatus` (GET) | Portfolio Margin UM Trading Quantitative Rules Indicators(USER_DATA) | None | symbol, recvWindow | Yes |
| `/papi/v1/cm/positionRisk` (GET) | Query CM Position Information(USER_DATA) | None | marginAsset, pair, recvWindow | Yes |
| `/papi/v1/margin/marginLoan` (GET) | Query Margin Loan Record(USER_DATA) | asset | txId, startTime, endTime, current, size, archived, recvWindow | Yes |
| `/papi/v1/margin/maxWithdraw` (GET) | Query Margin Max Withdraw(USER_DATA) | asset | recvWindow | Yes |
| `/papi/v1/margin/repayLoan` (GET) | Query Margin repay Record(USER_DATA) | asset | txId, startTime, endTime, current, size, archived, recvWindow | Yes |
| `/papi/v1/portfolio/interest-history` (GET) | Query Portfolio Margin Negative Balance Interest History(USER_DATA) | None | asset, startTime, endTime, size, recvWindow | Yes |
| `/papi/v1/um/positionRisk` (GET) | Query UM Position Information(USER_DATA) | None | symbol, recvWindow | Yes |
| `/papi/v1/portfolio/negative-balance-exchange-record` (GET) | Query User Negative Balance Auto Exchange Record (USER_DATA) | startTime, endTime | recvWindow | Yes |
| `/papi/v1/rateLimit/order` (GET) | Query User Rate Limit (USER_DATA) | None | recvWindow | Yes |
| `/papi/v1/repay-futures-negative-balance` (POST) | Repay futures Negative Balance(USER_DATA) | None | recvWindow | Yes |
| `/papi/v1/um/leverageBracket` (GET) | UM Notional and Leverage Brackets (USER_DATA) | None | symbol, recvWindow | Yes |
| `/papi/v1/ping` (GET) | Test Connectivity | None | None | No |
| `/papi/v1/cm/userTrades` (GET) | CM Account Trade List(USER_DATA) | None | symbol, pair, startTime, endTime, fromId, limit, recvWindow | Yes |
| `/papi/v1/cm/adlQuantile` (GET) | CM Position ADL Quantile Estimation(USER_DATA) | None | symbol, recvWindow | Yes |
| `/papi/v1/cm/conditional/allOpenOrders` (DELETE) | Cancel All CM Open Conditional Orders(TRADE) | symbol | recvWindow | Yes |
| `/papi/v1/cm/allOpenOrders` (DELETE) | Cancel All CM Open Orders(TRADE) | symbol | recvWindow | Yes |
| `/papi/v1/um/conditional/allOpenOrders` (DELETE) | Cancel All UM Open Conditional Orders (TRADE) | symbol | recvWindow | Yes |
| `/papi/v1/um/allOpenOrders` (DELETE) | Cancel All UM Open Orders(TRADE) | symbol | recvWindow | Yes |
| `/papi/v1/cm/conditional/order` (DELETE) | Cancel CM Conditional Order(TRADE) | symbol | strategyId, newClientStrategyId, recvWindow | Yes |
| `/papi/v1/cm/conditional/order` (POST) | New CM Conditional Order(TRADE) | symbol, side, strategyType | positionSide, timeInForce, quantity, reduceOnly, price, workingType, priceProtect, newClientStrategyId, stopPrice, activationPrice, callbackRate, recvWindow | Yes |
| `/papi/v1/cm/order` (DELETE) | Cancel CM Order(TRADE) | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/papi/v1/cm/order` (PUT) | Modify CM Order(TRADE) | symbol, side, quantity, price | orderId, origClientOrderId, priceMatch, recvWindow | Yes |
| `/papi/v1/cm/order` (POST) | New CM Order(TRADE) | symbol, side, type | positionSide, timeInForce, quantity, reduceOnly, price, priceMatch, newClientOrderId, newOrderRespType, recvWindow | Yes |
| `/papi/v1/cm/order` (GET) | Query CM Order(USER_DATA) | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/papi/v1/margin/allOpenOrders` (DELETE) | Cancel Margin Account All Open Orders on a Symbol(TRADE) | symbol | recvWindow | Yes |
| `/papi/v1/margin/orderList` (DELETE) | Cancel Margin Account OCO Orders(TRADE) | symbol | orderListId, listClientOrderId, newClientOrderId, recvWindow | Yes |
| `/papi/v1/margin/orderList` (GET) | Query Margin Account's OCO (USER_DATA) | None | orderListId, origClientOrderId, recvWindow | Yes |
| `/papi/v1/margin/order` (DELETE) | Cancel Margin Account Order(TRADE) | symbol | orderId, origClientOrderId, newClientOrderId, recvWindow | Yes |
| `/papi/v1/margin/order` (POST) | New Margin Order(TRADE) | symbol, side, type | quantity, quoteOrderQty, price, stopPrice, newClientOrderId, newOrderRespType, icebergQty, sideEffectType, timeInForce, selfTradePreventionMode, autoRepayAtCancel, recvWindow | Yes |
| `/papi/v1/margin/order` (GET) | Query Margin Account Order (USER_DATA) | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/papi/v1/um/conditional/order` (DELETE) | Cancel UM Conditional Order(TRADE) | symbol | strategyId, newClientStrategyId, recvWindow | Yes |
| `/papi/v1/um/conditional/order` (POST) | New UM Conditional Order (TRADE) | symbol, side, strategyType | positionSide, timeInForce, quantity, reduceOnly, price, workingType, priceProtect, newClientStrategyId, stopPrice, activationPrice, callbackRate, priceMatch, selfTradePreventionMode, goodTillDate, recvWindow | Yes |
| `/papi/v1/um/order` (DELETE) | Cancel UM Order(TRADE) | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/papi/v1/um/order` (PUT) | Modify UM Order(TRADE) | symbol, side, quantity, price | orderId, origClientOrderId, priceMatch, recvWindow | Yes |
| `/papi/v1/um/order` (POST) | New UM Order (TRADE) | symbol, side, type | positionSide, timeInForce, quantity, reduceOnly, price, newClientOrderId, newOrderRespType, priceMatch, selfTradePreventionMode, goodTillDate, recvWindow | Yes |
| `/papi/v1/um/order` (GET) | Query UM Order (USER_DATA) | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/papi/v1/um/feeBurn` (GET) | Get UM Futures BNB Burn Status (USER_DATA) | None | recvWindow | Yes |
| `/papi/v1/um/feeBurn` (POST) | Toggle BNB Burn On UM Futures Trade (TRADE) | feeBurn | recvWindow | Yes |
| `/papi/v1/marginLoan` (POST) | Margin Account Borrow(MARGIN) | asset, amount | recvWindow | Yes |
| `/papi/v1/margin/order/oco` (POST) | Margin Account New OCO(TRADE) | symbol, side, quantity, price, stopPrice | listClientOrderId, limitClientOrderId, limitIcebergQty, stopClientOrderId, stopLimitPrice, stopIcebergQty, stopLimitTimeInForce, newOrderRespType, sideEffectType, recvWindow | Yes |
| `/papi/v1/margin/repay-debt` (POST) | Margin Account Repay Debt(TRADE) | asset | amount, specifyRepayAssets, recvWindow | Yes |
| `/papi/v1/repayLoan` (POST) | Margin Account Repay(MARGIN) | asset, amount | recvWindow | Yes |
| `/papi/v1/margin/myTrades` (GET) | Margin Account Trade List (USER_DATA) | symbol | orderId, startTime, endTime, fromId, limit, recvWindow | Yes |
| `/papi/v1/cm/conditional/allOrders` (GET) | Query All CM Conditional Orders(USER_DATA) | None | symbol, strategyId, startTime, endTime, limit, recvWindow | Yes |
| `/papi/v1/cm/allOrders` (GET) | Query All CM Orders (USER_DATA) | symbol | pair, orderId, startTime, endTime, limit, recvWindow | Yes |
| `/papi/v1/cm/conditional/openOrders` (GET) | Query All Current CM Open Conditional Orders (USER_DATA) | None | symbol, recvWindow | Yes |
| `/papi/v1/cm/openOrders` (GET) | Query All Current CM Open Orders(USER_DATA) | None | symbol, pair, recvWindow | Yes |
| `/papi/v1/um/conditional/openOrders` (GET) | Query All Current UM Open Conditional Orders(USER_DATA) | None | symbol, recvWindow | Yes |
| `/papi/v1/um/openOrders` (GET) | Query All Current UM Open Orders(USER_DATA) | None | symbol, recvWindow | Yes |
| `/papi/v1/margin/allOrders` (GET) | Query All Margin Account Orders (USER_DATA) | symbol | orderId, startTime, endTime, limit, recvWindow | Yes |
| `/papi/v1/um/conditional/allOrders` (GET) | Query All UM Conditional Orders(USER_DATA) | None | symbol, strategyId, startTime, endTime, limit, recvWindow | Yes |
| `/papi/v1/um/allOrders` (GET) | Query All UM Orders(USER_DATA) | symbol | orderId, startTime, endTime, limit, recvWindow | Yes |
| `/papi/v1/cm/conditional/orderHistory` (GET) | Query CM Conditional Order History(USER_DATA) | symbol | strategyId, newClientStrategyId, recvWindow | Yes |
| `/papi/v1/cm/orderAmendment` (GET) | Query CM Modify Order History(TRADE) | symbol | orderId, origClientOrderId, startTime, endTime, limit, recvWindow | Yes |
| `/papi/v1/cm/conditional/openOrder` (GET) | Query Current CM Open Conditional Order(USER_DATA) | symbol | strategyId, newClientStrategyId, recvWindow | Yes |
| `/papi/v1/cm/openOrder` (GET) | Query Current CM Open Order (USER_DATA) | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/papi/v1/margin/openOrders` (GET) | Query Current Margin Open Order (USER_DATA) | symbol | recvWindow | Yes |
| `/papi/v1/um/conditional/openOrder` (GET) | Query Current UM Open Conditional Order(USER_DATA) | symbol | strategyId, newClientStrategyId, recvWindow | Yes |
| `/papi/v1/um/openOrder` (GET) | Query Current UM Open Order(USER_DATA) | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/papi/v1/margin/openOrderList` (GET) | Query Margin Account's Open OCO (USER_DATA) | None | recvWindow | Yes |
| `/papi/v1/margin/allOrderList` (GET) | Query Margin Account's all OCO (USER_DATA) | None | fromId, startTime, endTime, limit, recvWindow | Yes |
| `/papi/v1/um/conditional/orderHistory` (GET) | Query UM Conditional Order History(USER_DATA) | symbol | strategyId, newClientStrategyId, recvWindow | Yes |
| `/papi/v1/um/orderAmendment` (GET) | Query UM Modify Order History(TRADE) | symbol | orderId, origClientOrderId, startTime, endTime, limit, recvWindow | Yes |
| `/papi/v1/cm/forceOrders` (GET) | Query User's CM Force Orders(USER_DATA) | None | symbol, autoCloseType, startTime, endTime, limit, recvWindow | Yes |
| `/papi/v1/margin/forceOrders` (GET) | Query User's Margin Force Orders(USER_DATA) | None | startTime, endTime, current, size, recvWindow | Yes |
| `/papi/v1/um/forceOrders` (GET) | Query User's UM Force Orders (USER_DATA) | None | symbol, autoCloseType, startTime, endTime, limit, recvWindow | Yes |
| `/papi/v1/um/userTrades` (GET) | UM Account Trade List(USER_DATA) | symbol | startTime, endTime, fromId, limit, recvWindow | Yes |
| `/papi/v1/um/adlQuantile` (GET) | UM Position ADL Quantile Estimation(USER_DATA) | None | symbol, recvWindow | Yes |
| `/papi/v1/listenKey` (DELETE) | Close User Data Stream(USER_STREAM) | None | None | No |
| `/papi/v1/listenKey` (PUT) | Keepalive User Data Stream (USER_STREAM) | None | None | No |
| `/papi/v1/listenKey` (POST) | Start User Data Stream(USER_STREAM) | None | None | No |

---

## Parameters

### Common Parameters

* **asset**: 
* **recvWindow**:  (e.g., 5000)
* **amount**:  (e.g., 1.0)
* **transferSide**: "TO_UM","FROM_UM"
* **symbol**: 
* **autoRepay**: Default: `true`; `false` for turn off the auto-repay futures negative balance function (e.g., true)
* **symbol**: 
* **leverage**: target initial leverage: int from 1 to 125
* **dualSidePosition**: "true": Hedge Mode; "false": One-way Mode
* **asset**: 
* **incomeType**: TRANSFER, WELCOME_BONUS, REALIZED_PNL, FUNDING_FEE, COMMISSION, INSURANCE_CLEAR, REFERRAL_KICKBACK, COMMISSION_REBATE, API_REBATE, CONTEST_REWARD, CROSS_COLLATERAL_TRANSFER, OPTIONS_PREMIUM_FEE, OPTIONS_SETTLE_PROFIT, INTERNAL_TRANSFER, AUTO_EXCHANGE, DELIVERED_SETTELMENT, COIN_SWAP_DEPOSIT, COIN_SWAP_WITHDRAW, POSITION_LIMIT_INCREASE_FEE
* **startTime**: Timestamp in ms to get funding from INCLUSIVE. (e.g., 1623319461670)
* **endTime**: Timestamp in ms to get funding until INCLUSIVE. (e.g., 1641782889000)
* **page**: 
* **limit**: Default 100; max 1000 (e.g., 100)
* **startTime**:  (e.g., 1623319461670)
* **endTime**:  (e.g., 1641782889000)
* **current**: Currently querying page. Start from 1. Default:1 (e.g., 1)
* **size**: Default:10 Max:100 (e.g., 10)
* **archived**: Default: `false`. Set to `true` for archived data from 6 months ago
* **downloadId**: get by download id api (e.g., 1)
* **marginAsset**: 
* **pair**: 
* **txId**: the `tranId` in `POST/papi/v1/marginLoan` (e.g., 1)
* **fromId**: Trade id to fetch from. Default gets most recent trades. (e.g., 1)
* **strategyId**:  (e.g., 1)
* **newClientStrategyId**:  (e.g., 1)
* **orderId**:  (e.g., 1)
* **origClientOrderId**:  (e.g., 1)
* **orderListId**: Either `orderListId` or `listClientOrderId` must be provided (e.g., 1)
* **listClientOrderId**: Either `orderListId` or `listClientOrderId` must be provided (e.g., 1)
* **newClientOrderId**: Used to uniquely identify this cancel. Automatically generated by default (e.g., 1)
* **quantity**: Order quantity (e.g., 1.0)
* **limitClientOrderId**: A unique Id for the limit order (e.g., 1)
* **price**:  (e.g., 1.0)
* **limitIcebergQty**:  (e.g., 1.0)
* **stopClientOrderId**: A unique Id for the stop loss/stop loss limit leg (e.g., 1)
* **stopPrice**:  (e.g., 1.0)
* **stopLimitPrice**: If provided, stopLimitTimeInForce is required. (e.g., 1.0)
* **stopIcebergQty**:  (e.g., 1.0)
* **amount**: 
* **specifyRepayAssets**: Specific asset list to repay debt; Can be added in batch, separated by commas
* **quantity**:  (e.g., 1.0)
* **reduceOnly**: "true" or "false". default "false". Cannot be sent in Hedge Mode .
* **price**:  (e.g., 1.0)
* **priceProtect**: "TRUE" or "FALSE", default "FALSE". Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders
* **stopPrice**: Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders. (e.g., 1.0)
* **activationPrice**: Used with `TRAILING_STOP_MARKET` orders, default as the mark price (e.g., 1.0)
* **callbackRate**: Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 5 where 1 for 1% (e.g., 1.0)
* **quoteOrderQty**:  (e.g., 1.0)
* **icebergQty**: Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order (e.g., 1.0)
* **autoRepayAtCancel**: Only when MARGIN_BUY or AUTO_BORROW_REPAY order takes effect, true means that the debt generated by the order needs to be repay after the order is cancelled. The default is true (e.g., true)
* **goodTillDate**: order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000Mode. It must be sent in Hedge Mode.
* **feeBurn**: "true": Fee Discount On; "false": Fee Discount Off


### Enums

* **side**: BUY | SELL
* **stopLimitTimeInForce**: GTC | IOC | FOK
* **newOrderRespType**: ACK | RESULT
* **sideEffectType**: NO_SIDE_EFFECT | MARGIN_BUY | AUTO_REPAY
* **priceMatch**: NONE | OPPONENT | OPPONENT_5 | OPPONENT_10 | OPPONENT_20 | QUEUE | QUEUE_5 | QUEUE_10 | QUEUE_20
* **positionSide**: BOTH | LONG | SHORT
* **strategyType**: STOP | STOP_MARKET | LIMIT_MAKER | TAKE_PROFIT | TAKE_PROFIT_MARKET | TRAILING_STOP_MARKET
* **timeInForce**: GTC | IOC | FOK | GTX
* **workingType**: MARK_PRICE
* **type**: LIMIT | MARKET
* **selfTradePreventionMode**: NONE | EXPIRE_TAKER | EXPIRE_BOTH | EXPIRE_MAKER
* **autoCloseType**: LIQUIDATION | ADL


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://papi.binance.com
* Testnet: https://testnet.binancefuture.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`
- Testnet: `BINANCE_TESTNET_API_KEY` and `BINANCE_TESTNET_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1
Environment: Mainnet

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet/Testnet)
* testnet-dev (Testnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret
- Testnet: false 

### testnet-dev
- API Key: your_testnet_api_key
- Secret: your_testnet_secret
- Testnet: true

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Testnet: false
- Description: Primary trading account

### testnet-dev
- API Key: test456...abc
- Secret: testsecret...xyz
- Testnet: true
- Description: Development/testing

### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Testnet: false
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode
6. When a request requires signing, if the request isn't an order and the API keys aren't described as `mainnet` or `testnet` keys, try to make request to the different base urls and see if it works, without asking the user. If it works, store the keys with the corresponding environment.

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Ask: Mainnet, Testnet 
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## New Client Order ID 

For endpoints that include the `newClientOrderId` parameter, the value must always start with `agent-`. If the parameter is not provided, `agent-` followed by 18 random alphanumeric characters will be generated automatically. If a value is provided, it will be prefixed with `agent-`

Example: `agent-1a2b3c4d5e6f7g8h9i`

## User Agent Header

Include `User-Agent` header with the following string: `binance-derivatives-trading-portfolio-margin/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/derivatives-trading-portfolio-margin/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://papi.binance.com |
| Testnet | https://testnet.binancefuture.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-derivatives-trading-portfolio-margin/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-derivatives-trading-portfolio-margin/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X GET "https://papi.binance.com/papi/v1/balance" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-derivatives-trading-portfolio-margin/1.1.0 (Skill)" \
  -d "timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://papi.binance.com"  # or https://testnet.binancefuture.com

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X GET "${BASE_URL}/papi/v1/balance?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-derivatives-trading-portfolio-margin/1.1.0 (Skill)"
```

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
* Use testnet for development: https://testnet.binancefuture.com
* Testnet credentials are separate from mainnet
```

## File: `skills/binance/derivatives-trading-portfolio-margin-pro/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-19

- Initial release
```

## File: `skills/binance/derivatives-trading-portfolio-margin-pro/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/derivatives-trading-portfolio-margin-pro/SKILL.md`
```markdown
---
name: derivatives-trading-portfolio-margin-pro
description: Binance Derivatives-trading-portfolio-margin-pro request using the Binance API. Authentication requires API key and secret key. 
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/derivatives-trading-portfolio-margin-pro/SKILL.md
license: MIT
---

# Binance Derivatives-trading-portfolio-margin-pro Skill

Derivatives-trading-portfolio-margin-pro request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/sapi/v1/portfolio/bnb-transfer` (POST) | BNB transfer(USER_DATA) | amount, transferSide | recvWindow | Yes |
| `/sapi/v1/portfolio/repay-futures-switch` (POST) | Change Auto-repay-futures Status(TRADE) | autoRepay | recvWindow | Yes |
| `/sapi/v1/portfolio/repay-futures-switch` (GET) | Get Auto-repay-futures Status(USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/portfolio/repay` (POST) | Portfolio Margin Pro Bankruptcy Loan Repay | None | from, recvWindow | Yes |
| `/sapi/v1/portfolio/auto-collection` (POST) | Fund Auto-collection(USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/portfolio/asset-collection` (POST) | Fund Collection by Asset(USER_DATA) | asset | recvWindow | Yes |
| `/sapi/v2/portfolio/account` (GET) | Get Portfolio Margin Pro SPAN Account Info(USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/portfolio/account` (GET) | Get Portfolio Margin Pro Account Info(USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/portfolio/balance` (GET) | Get Portfolio Margin Pro Account Balance(USER_DATA) | None | asset, recvWindow | Yes |
| `/sapi/v1/portfolio/delta-mode` (GET) | Get Delta Mode Status(USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/portfolio/delta-mode` (POST) | Switch Delta Mode(TRADE) | deltaEnabled | recvWindow | Yes |
| `/sapi/v1/portfolio/earn-asset-balance` (GET) | Get Transferable Earn Asset Balance for Portfolio Margin (USER_DATA) | asset, transferType | recvWindow | Yes |
| `/sapi/v1/portfolio/pmLoan` (GET) | Query Portfolio Margin Pro Bankruptcy Loan Amount(USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/portfolio/interest-history` (GET) | Query Portfolio Margin Pro Negative Balance Interest History(USER_DATA) | None | asset, startTime, endTime, size, recvWindow | Yes |
| `/sapi/v1/portfolio/pmloan-history` (GET) | Query Portfolio Margin Pro Bankruptcy Loan Repay History(USER_DATA) | None | startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/portfolio/repay-futures-negative-balance` (POST) | Repay futures Negative Balance(USER_DATA) | None | from, recvWindow | Yes |
| `/sapi/v1/portfolio/earn-asset-transfer` (POST) | Transfer LDUSDT/RWUSD for Portfolio Margin(TRADE) | asset, transferType, amount | recvWindow | Yes |
| `/sapi/v1/portfolio/collateralRate` (GET) | Portfolio Margin Collateral Rate(MARKET_DATA) | None | None | No |
| `/sapi/v1/portfolio/margin-asset-leverage` (GET) | Get Portfolio Margin Asset Leverage(USER_DATA) | None | None | Yes |
| `/sapi/v2/portfolio/collateralRate` (GET) | Portfolio Margin Pro Tiered Collateral Rate(USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/portfolio/asset-index-price` (GET) | Query Portfolio Margin Asset Index Price (MARKET_DATA) | None | asset | No |

---

## Parameters

### Common Parameters

* **amount**:  (e.g., 1.0)
* **transferSide**: "TO_UM","FROM_UM"
* **recvWindow**:  (e.g., 5000)
* **autoRepay**: Default: `true`; `false` for turn off the auto-repay futures negative balance function (e.g., true)
* **from**: SPOT or MARGIN，default SPOT (e.g., SPOT)
* **asset**: `LDUSDT` and `RWUSD`
* **asset**: 
* **transferType**: `EARN_TO_FUTURE` /`FUTURE_TO_EARN`
* **startTime**:  (e.g., 1623319461670)
* **endTime**:  (e.g., 1641782889000)
* **size**: Default:10 Max:100 (e.g., 10)
* **current**: Currently querying page. Start from 1. Default:1 (e.g., 1)
* **deltaEnabled**: `true` to enable Delta mode; `false` to disable Delta mode


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://api.binance.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Description: Primary trading account


### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## User Agent Header

Include `User-Agent` header with the following string: `binance-derivatives-trading-portfolio-margin-pro/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/derivatives-trading-portfolio-margin-pro/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://api.binance.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-derivatives-trading-portfolio-margin-pro/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-derivatives-trading-portfolio-margin-pro/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X GET "https://api.binance.com/sapi/v1/portfolio/repay-futures-switch" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-derivatives-trading-portfolio-margin-pro/1.1.0 (Skill)" \
  -d "timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://api.binance.com"  

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X GET "${BASE_URL}/sapi/v1/portfolio/repay-futures-switch?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-derivatives-trading-portfolio-margin-pro/1.1.0 (Skill)"
```

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
```

## File: `skills/binance/derivatives-trading-usds-futures/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-10

- Initial release
```

## File: `skills/binance/derivatives-trading-usds-futures/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/derivatives-trading-usds-futures/SKILL.md`
```markdown
---
name: derivatives-trading-usds-futures
description: Binance Derivatives-trading-usds-futures request using the Binance API. Authentication requires API key and secret key. Supports testnet and mainnet.
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/derivatives-trading-usds-futures/SKILL.md
license: MIT
---

# Binance Derivatives-trading-usds-futures Skill

Derivatives-trading-usds-futures request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/fapi/v1/accountConfig` (GET) | Futures Account Configuration(USER_DATA) | None | recvWindow | Yes |
| `/fapi/v2/account` (GET) | Account Information V2(USER_DATA) | None | recvWindow | Yes |
| `/fapi/v3/account` (GET) | Account Information V3(USER_DATA) | None | recvWindow | Yes |
| `/fapi/v2/balance` (GET) | Futures Account Balance V2 (USER_DATA) | None | recvWindow | Yes |
| `/fapi/v3/balance` (GET) | Futures Account Balance V3 (USER_DATA) | None | recvWindow | Yes |
| `/fapi/v1/apiTradingStatus` (GET) | Futures Trading Quantitative Rules Indicators (USER_DATA) | None | symbol, recvWindow | Yes |
| `/fapi/v1/feeBurn` (GET) | Get BNB Burn Status (USER_DATA) | None | recvWindow | Yes |
| `/fapi/v1/feeBurn` (POST) | Toggle BNB Burn On Futures Trade (TRADE) | feeBurn | recvWindow | Yes |
| `/fapi/v1/multiAssetsMargin` (GET) | Get Current Multi-Assets Mode (USER_DATA) | None | recvWindow | Yes |
| `/fapi/v1/multiAssetsMargin` (POST) | Change Multi-Assets Mode (TRADE) | multiAssetsMargin | recvWindow | Yes |
| `/fapi/v1/positionSide/dual` (GET) | Get Current Position Mode(USER_DATA) | None | recvWindow | Yes |
| `/fapi/v1/positionSide/dual` (POST) | Change Position Mode(TRADE) | dualSidePosition | recvWindow | Yes |
| `/fapi/v1/order/asyn` (GET) | Get Download Id For Futures Order History (USER_DATA) | startTime, endTime | recvWindow | Yes |
| `/fapi/v1/trade/asyn` (GET) | Get Download Id For Futures Trade History (USER_DATA) | startTime, endTime | recvWindow | Yes |
| `/fapi/v1/income/asyn` (GET) | Get Download Id For Futures Transaction History(USER_DATA) | startTime, endTime | recvWindow | Yes |
| `/fapi/v1/order/asyn/id` (GET) | Get Futures Order History Download Link by Id (USER_DATA) | downloadId | recvWindow | Yes |
| `/fapi/v1/trade/asyn/id` (GET) | Get Futures Trade Download Link by Id(USER_DATA) | downloadId | recvWindow | Yes |
| `/fapi/v1/income/asyn/id` (GET) | Get Futures Transaction History Download Link by Id (USER_DATA) | downloadId | recvWindow | Yes |
| `/fapi/v1/income` (GET) | Get Income History (USER_DATA) | None | symbol, incomeType, startTime, endTime, page, limit, recvWindow | Yes |
| `/fapi/v1/leverageBracket` (GET) | Notional and Leverage Brackets (USER_DATA) | None | symbol, recvWindow | Yes |
| `/fapi/v1/rateLimit/order` (GET) | Query User Rate Limit (USER_DATA) | None | recvWindow | Yes |
| `/fapi/v1/symbolConfig` (GET) | Symbol Configuration(USER_DATA) | None | symbol, recvWindow | Yes |
| `/fapi/v1/commissionRate` (GET) | User Commission Rate (USER_DATA) | symbol | recvWindow | Yes |
| `/fapi/v1/convert/acceptQuote` (POST) | Accept the offered quote (USER_DATA) | quoteId | recvWindow | Yes |
| `/fapi/v1/convert/exchangeInfo` (GET) | List All Convert Pairs | None | fromAsset, toAsset | No |
| `/fapi/v1/convert/orderStatus` (GET) | Order status(USER_DATA) | None | orderId, quoteId | Yes |
| `/fapi/v1/convert/getQuote` (POST) | Send Quote Request(USER_DATA) | fromAsset, toAsset | fromAmount, toAmount, validTime, recvWindow | Yes |
| `/fapi/v1/ticker/24hr` (GET) | 24hr Ticker Price Change Statistics | None | symbol | No |
| `/fapi/v1/symbolAdlRisk` (GET) | ADL Risk | None | symbol | No |
| `/futures/data/basis` (GET) | Basis | pair, contractType, period, limit | startTime, endTime | No |
| `/fapi/v1/time` (GET) | Check Server Time | None | None | No |
| `/fapi/v1/indexInfo` (GET) | Composite Index Symbol Information | None | symbol | No |
| `/fapi/v1/aggTrades` (GET) | Compressed/Aggregate Trades List | symbol | fromId, startTime, endTime, limit | No |
| `/fapi/v1/continuousKlines` (GET) | Continuous Contract Kline/Candlestick Data | pair, contractType, interval | startTime, endTime, limit | No |
| `/futures/data/delivery-price` (GET) | Quarterly Contract Settlement Price | pair | None | No |
| `/fapi/v1/exchangeInfo` (GET) | Exchange Information | None | None | No |
| `/fapi/v1/fundingRate` (GET) | Get Funding Rate History | None | symbol, startTime, endTime, limit | No |
| `/fapi/v1/fundingInfo` (GET) | Get Funding Rate Info | None | None | No |
| `/fapi/v1/constituents` (GET) | Query Index Price Constituents | symbol | None | No |
| `/fapi/v1/indexPriceKlines` (GET) | Index Price Kline/Candlestick Data | pair, interval | startTime, endTime, limit | No |
| `/fapi/v1/insuranceBalance` (GET) | Query Insurance Fund Balance Snapshot | None | symbol | No |
| `/fapi/v1/klines` (GET) | Kline/Candlestick Data | symbol, interval | startTime, endTime, limit | No |
| `/futures/data/globalLongShortAccountRatio` (GET) | Long/Short Ratio | symbol, period | limit, startTime, endTime | No |
| `/fapi/v1/markPriceKlines` (GET) | Mark Price Kline/Candlestick Data | symbol, interval | startTime, endTime, limit | No |
| `/fapi/v1/premiumIndex` (GET) | Mark Price | None | symbol | No |
| `/fapi/v1/assetIndex` (GET) | Multi-Assets Mode Asset Index | None | symbol | No |
| `/fapi/v1/historicalTrades` (GET) | Old Trades Lookup (MARKET_DATA) | symbol | limit, fromId | No |
| `/futures/data/openInterestHist` (GET) | Open Interest Statistics | symbol, period | limit, startTime, endTime | No |
| `/fapi/v1/openInterest` (GET) | Open Interest | symbol | None | No |
| `/fapi/v1/rpiDepth` (GET) | RPI Order Book | symbol | limit | No |
| `/fapi/v1/depth` (GET) | Order Book | symbol | limit | No |
| `/fapi/v1/premiumIndexKlines` (GET) | Premium index Kline Data | symbol, interval | startTime, endTime, limit | No |
| `/fapi/v1/trades` (GET) | Recent Trades List | symbol | limit | No |
| `/fapi/v1/ticker/bookTicker` (GET) | Symbol Order Book Ticker | None | symbol | No |
| `/fapi/v2/ticker/price` (GET) | Symbol Price Ticker V2 | None | symbol | No |
| `/fapi/v1/ticker/price` (GET) | Symbol Price Ticker | None | symbol | No |
| `/futures/data/takerlongshortRatio` (GET) | Taker Buy/Sell Volume | symbol, period | limit, startTime, endTime | No |
| `/fapi/v1/ping` (GET) | Test Connectivity | None | None | No |
| `/futures/data/topLongShortAccountRatio` (GET) | Top Trader Long/Short Ratio (Accounts) | symbol, period | limit, startTime, endTime | No |
| `/futures/data/topLongShortPositionRatio` (GET) | Top Trader Long/Short Ratio (Positions) | symbol, period | limit, startTime, endTime | No |
| `/fapi/v1/tradingSchedule` (GET) | Trading Schedule | None | None | No |
| `/fapi/v1/pmAccountInfo` (GET) | Classic Portfolio Margin Account Information (USER_DATA) | asset | recvWindow | Yes |
| `/fapi/v1/userTrades` (GET) | Account Trade List (USER_DATA) | symbol | orderId, startTime, endTime, fromId, limit, recvWindow | Yes |
| `/fapi/v1/allOrders` (GET) | All Orders (USER_DATA) | symbol | orderId, startTime, endTime, limit, recvWindow | Yes |
| `/fapi/v1/countdownCancelAll` (POST) | Auto-Cancel All Open Orders (TRADE) | symbol, countdownTime | recvWindow | Yes |
| `/fapi/v1/algoOrder` (DELETE) | Cancel Algo Order (TRADE) | None | algoId, clientAlgoId, recvWindow | Yes |
| `/fapi/v1/algoOrder` (POST) | New Algo Order(TRADE) | algoType, symbol, side, type | positionSide, timeInForce, quantity, price, triggerPrice, workingType, priceMatch, closePosition, priceProtect, reduceOnly, activatePrice, callbackRate, clientAlgoId, newOrderRespType, selfTradePreventionMode, goodTillDate, recvWindow | Yes |
| `/fapi/v1/algoOrder` (GET) | Query Algo Order (USER_DATA) | None | algoId, clientAlgoId, recvWindow | Yes |
| `/fapi/v1/algoOpenOrders` (DELETE) | Cancel All Algo Open Orders (TRADE) | symbol | recvWindow | Yes |
| `/fapi/v1/allOpenOrders` (DELETE) | Cancel All Open Orders (TRADE) | symbol | recvWindow | Yes |
| `/fapi/v1/batchOrders` (DELETE) | Cancel Multiple Orders (TRADE) | symbol | orderIdList, origClientOrderIdList, recvWindow | Yes |
| `/fapi/v1/batchOrders` (PUT) | Modify Multiple Orders(TRADE) | batchOrders | recvWindow | Yes |
| `/fapi/v1/batchOrders` (POST) | Place Multiple Orders(TRADE) | batchOrders | recvWindow | Yes |
| `/fapi/v1/order` (DELETE) | Cancel Order (TRADE) | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/fapi/v1/order` (PUT) | Modify Order (TRADE) | symbol, side, quantity, price | orderId, origClientOrderId, priceMatch, recvWindow | Yes |
| `/fapi/v1/order` (POST) | New Order(TRADE) | symbol, side, type | positionSide, timeInForce, quantity, reduceOnly, price, newClientOrderId, newOrderRespType, priceMatch, selfTradePreventionMode, goodTillDate, recvWindow | Yes |
| `/fapi/v1/order` (GET) | Query Order (USER_DATA) | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/fapi/v1/leverage` (POST) | Change Initial Leverage(TRADE) | symbol, leverage | recvWindow | Yes |
| `/fapi/v1/marginType` (POST) | Change Margin Type(TRADE) | symbol, marginType | recvWindow | Yes |
| `/fapi/v1/openAlgoOrders` (GET) | Current All Algo Open Orders (USER_DATA) | None | algoType, symbol, algoId, recvWindow | Yes |
| `/fapi/v1/openOrders` (GET) | Current All Open Orders (USER_DATA) | None | symbol, recvWindow | Yes |
| `/fapi/v1/orderAmendment` (GET) | Get Order Modify History (USER_DATA) | symbol | orderId, origClientOrderId, startTime, endTime, limit, recvWindow | Yes |
| `/fapi/v1/positionMargin/history` (GET) | Get Position Margin Change History (TRADE) | symbol | type, startTime, endTime, limit, recvWindow | Yes |
| `/fapi/v1/positionMargin` (POST) | Modify Isolated Position Margin(TRADE) | symbol, amount, type | positionSide, recvWindow | Yes |
| `/fapi/v1/order/test` (POST) | Test Order(TRADE) | symbol, side, type | positionSide, timeInForce, quantity, reduceOnly, price, newClientOrderId, stopPrice, closePosition, activationPrice, callbackRate, workingType, priceProtect, newOrderRespType, priceMatch, selfTradePreventionMode, goodTillDate, recvWindow | Yes |
| `/fapi/v1/adlQuantile` (GET) | Position ADL Quantile Estimation(USER_DATA) | None | symbol, recvWindow | Yes |
| `/fapi/v2/positionRisk` (GET) | Position Information V2 (USER_DATA) | None | symbol, recvWindow | Yes |
| `/fapi/v3/positionRisk` (GET) | Position Information V3 (USER_DATA) | None | symbol, recvWindow | Yes |
| `/fapi/v1/allAlgoOrders` (GET) | Query All Algo Orders (USER_DATA) | symbol | algoId, startTime, endTime, page, limit, recvWindow | Yes |
| `/fapi/v1/openOrder` (GET) | Query Current Open Order (USER_DATA) | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/fapi/v1/stock/contract` (POST) | Futures TradFi Perps Contract(USER_DATA) | None | recvWindow | Yes |
| `/fapi/v1/forceOrders` (GET) | User's Force Orders (USER_DATA) | None | symbol, autoCloseType, startTime, endTime, limit, recvWindow | Yes |
| `/fapi/v1/listenKey` (DELETE) | Close User Data Stream (USER_STREAM) | None | None | No |
| `/fapi/v1/listenKey` (PUT) | Keepalive User Data Stream (USER_STREAM) | None | None | No |
| `/fapi/v1/listenKey` (POST) | Start User Data Stream (USER_STREAM) | None | None | No |

---

## Parameters

### Common Parameters

* **recvWindow**:  (e.g., 5000)
* **symbol**: 
* **startTime**: Timestamp in ms (e.g., 1623319461670)
* **endTime**: Timestamp in ms (e.g., 1641782889000)
* **downloadId**: get by download id api (e.g., 1)
* **incomeType**: TRANSFER, WELCOME_BONUS, REALIZED_PNL, FUNDING_FEE, COMMISSION, INSURANCE_CLEAR, REFERRAL_KICKBACK, COMMISSION_REBATE, API_REBATE, CONTEST_REWARD, CROSS_COLLATERAL_TRANSFER, OPTIONS_PREMIUM_FEE, OPTIONS_SETTLE_PROFIT, INTERNAL_TRANSFER, AUTO_EXCHANGE, DELIVERED_SETTELMENT, COIN_SWAP_DEPOSIT, COIN_SWAP_WITHDRAW, POSITION_LIMIT_INCREASE_FEE, STRATEGY_UMFUTURES_TRANSFER，FEE_RETURN，BFUSD_REWARD
* **startTime**:  (e.g., 1623319461670)
* **endTime**:  (e.g., 1641782889000)
* **page**: 
* **limit**: Default 100; max 1000 (e.g., 100)
* **feeBurn**: "true": Fee Discount On; "false": Fee Discount Off
* **symbol**: 
* **quoteId**:  (e.g., 1)
* **fromAsset**: User spends coin
* **toAsset**: User receives coin
* **orderId**: Either orderId or quoteId is required (e.g., 1)
* **quoteId**: Either orderId or quoteId is required (e.g., 1)
* **fromAsset**: 
* **toAsset**: 
* **fromAmount**: When specified, it is the amount you will be debited after the conversion (e.g., 1.0)
* **toAmount**: When specified, it is the amount you will be credited after the conversion (e.g., 1.0)
* **validTime**: 10s, default 10s (e.g., 10s)
* **pair**: 
* **limit**: Default 30,Max 500 (e.g., 30)
* **fromId**: ID to get aggregate trades from INCLUSIVE. (e.g., 1)
* **asset**: 
* **orderId**:  (e.g., 1)
* **countdownTime**: countdown time, 1000 for 1 second. 0 to cancel the timer
* **algoId**:  (e.g., 1)
* **clientAlgoId**:  (e.g., 1)
* **orderIdList**: max length 10   e.g. [1234567,2345678]
* **origClientOrderIdList**: max length 10  e.g. ["my_id_1","my_id_2"], encode the double quotes. No space after comma.
* **origClientOrderId**:  (e.g., 1)
* **leverage**: target initial leverage: int from 1 to 125
* **multiAssetsMargin**: "true": Multi-Assets Mode; "false": Single-Asset Mode
* **dualSidePosition**: "true": Hedge Mode; "false": One-way Mode
* **algoType**: 
* **type**: 1: Add position margin，2: Reduce position margin
* **amount**:  (e.g., 1.0)
* **type**: 
* **batchOrders**: order list. Max 5 orders
* **quantity**: Order quantity, cannot be sent with `closePosition=true` (e.g., 1.0)
* **price**:  (e.g., 1.0)
* **algoType**: Only support `CONDITIONAL`
* **quantity**:  (e.g., 1.0)
* **price**:  (e.g., 1.0)
* **triggerPrice**:  (e.g., 1.0)
* **closePosition**: `true`, `false`；Close-All，used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`.
* **priceProtect**: "TRUE" or "FALSE", default "FALSE". Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.
* **reduceOnly**: "true" or "false". default "false". Cannot be sent in Hedge Mode
* **activatePrice**: Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting different `workingType`) (e.g., 1.0)
* **callbackRate**: Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 5 where 1 for 1% (e.g., 1.0)
* **goodTillDate**: order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000
* **newClientOrderId**: A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$` (e.g., 1)
* **stopPrice**: Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders. (e.g., 1.0)
* **activationPrice**: Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting different `workingType`) (e.g., 1.0)
* **batchOrders**: order list. Max 5 orders


### Enums

* **contractType**: PERPETUAL | CURRENT_MONTH | NEXT_MONTH | CURRENT_QUARTER | NEXT_QUARTER | PERPETUAL_DELIVERING
* **period**: 5m | 15m | 30m | 1h | 2h | 4h | 6h | 12h | 1d
* **interval**: 1m | 3m | 5m | 15m | 30m | 1h | 2h | 4h | 6h | 8h | 12h | 1d | 3d | 1w | 1M
* **marginType**: ISOLATED | CROSSED
* **positionSide**: BOTH | LONG | SHORT
* **side**: BUY | SELL
* **priceMatch**: NONE | OPPONENT | OPPONENT_5 | OPPONENT_10 | OPPONENT_20 | QUEUE | QUEUE_5 | QUEUE_10 | QUEUE_20
* **timeInForce**: GTC | IOC | FOK | GTX | GTD | RPI
* **workingType**: MARK_PRICE | CONTRACT_PRICE
* **newOrderRespType**: ACK | RESULT
* **selfTradePreventionMode**: EXPIRE_TAKER | EXPIRE_BOTH | EXPIRE_MAKER
* **autoCloseType**: LIQUIDATION | ADL


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://fapi.binance.com
* Testnet: https://demo-fapi.binance.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`
- Testnet: `BINANCE_TESTNET_API_KEY` and `BINANCE_TESTNET_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1
Environment: Mainnet

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet/Testnet)
* testnet-dev (Testnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret
- Testnet: false 

### testnet-dev
- API Key: your_testnet_api_key
- Secret: your_testnet_secret
- Testnet: true

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Testnet: false
- Description: Primary trading account

### testnet-dev
- API Key: test456...abc
- Secret: testsecret...xyz
- Testnet: true
- Description: Development/testing

### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Testnet: false
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode
6. When a request requires signing, if the request isn't an order and the API keys aren't described as `mainnet` or `testnet` keys, try to make request to the different base urls and see if it works, without asking the user. If it works, store the keys with the corresponding environment.

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Ask: Mainnet, Testnet 
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## New Client Order ID 

For endpoints that include the `newClientOrderId` parameter, the value must always start with `agent-`. If the parameter is not provided, `agent-` followed by 18 random alphanumeric characters will be generated automatically. If a value is provided, it will be prefixed with `agent-`

Example: `agent-1a2b3c4d5e6f7g8h9i`

## User Agent Header

Include `User-Agent` header with the following string: `binance-derivatives-trading-usds-futures/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/derivatives-trading-usds-futures/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://fapi.binance.com |
| Testnet | https://demo-fapi.binance.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-derivatives-trading-usds-futures/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-derivatives-trading-usds-futures/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X POST "https://fapi.binance.com/fapi/v1/order" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-derivatives-trading-usds-futures/1.q.0 (Skill)" \
  -d "symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://fapi.binance.com"  # or https://demo-fapi.binance.com

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X POST "${BASE_URL}/fapi/v1/order?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-derivatives-trading-usds-futures/1.1.0 (Skill)"
```

If you get -1021 Timestamp outside recvWindow:

1. Check server time: GET /fapi/v1/time
2. Sync your clock or adjust timestamp
3. Increase recvWindow (max 60000ms)

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
* Use testnet for development: https://demo-fapi.binance.com
* Testnet credentials are separate from mainnet
```

## File: `skills/binance/fiat/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-20

- Initial release
```

## File: `skills/binance/fiat/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/fiat/SKILL.md`
```markdown
---
name: fiat
description: Query Binance fiat payment capabilities — supported countries, currencies, payment methods, limits, and crypto prices — via public APIs, plus authenticated order/payment history lookup. Use whenever users ask about buying or selling crypto with fiat, depositing or withdrawing fiat, fiat-crypto exchange rates, payment options in a specific country, or their fiat order history — even if they don't explicitly mention Binance APIs.
metadata:
  version: 1.1.0
  author: Binance
license: MIT
---

# Binance Fiat Skill

Query Binance fiat payment capabilities, available payment methods, pricing, and supported currencies/countries using **public APIs** (no authentication required). For order and payment history, see [Authenticated Endpoints](./references/sapi-endpoints.md).

## Base URL

```
https://www.binance.com/bapi/fiat/v1/public/fiatpayment/agent
```

## Available APIs

### 1. get_capabilities

Query supported fiat currencies, cryptos, and business types for a country.

```bash
curl "https://www.binance.com/bapi/fiat/v1/public/fiatpayment/agent/get-capabilities?country={COUNTRY_CODE}"
```

Optional: `businessType` (BUY, SELL, DEPOSIT, WITHDRAW) to filter.

**Response:** `data.supportedBusinessTypes`, `data.fiatCurrencies[]` (with `code`, `name`, `supportedBusinessTypes`), `data.cryptoCurrencies[]`

### 2. get_buy_and_sell_payment_methods

```bash
curl "https://www.binance.com/bapi/fiat/v1/public/fiatpayment/agent/get-buy-and-sell-payment-methods?businessType={BUY|SELL}&fiatCurrency={FIAT}&cryptoCurrency={CRYPTO}&country={COUNTRY_CODE}"
```

All 4 parameters required.

**Response:** `data.paymentMethods[]` and `data.p2pPaymentMethods[]`, each with `code`, `paymentMethodName`, `fiatMinLimit`, `fiatMaxLimit`, `cryptoMinLimit`, `cryptoMaxLimit`, `quotation`, `suspended`

### 3. get_deposit_and_withdraw_payment_methods

```bash
curl "https://www.binance.com/bapi/fiat/v1/public/fiatpayment/agent/get-deposit-and-withdraw-payment-methods?businessType={DEPOSIT|WITHDRAW}&fiatCurrency={FIAT}&country={COUNTRY_CODE}"
```

All 3 parameters required. No `cryptoCurrency`, no `quotation`, no P2P methods.

**Response:** `data.paymentMethods[]` with `code`, `paymentMethodName`, `fiatMinLimit`, `fiatMaxLimit`, `suspended`

### 4. get_price

```bash
curl "https://www.binance.com/bapi/fiat/v1/public/fiatpayment/agent/get-price?fiatCurrency={FIAT}&cryptoCurrency={CRYPTO}&country={COUNTRY_CODE}"
```

Optional: `businessType` (BUY or SELL, defaults to BUY).

**Response:** `data.bestPrice` — indicative reference price, may differ from execution price

## Recommended Workflow

1. **`get_capabilities`** first — confirms what's supported before making other calls
2. **Payment methods API** — BUY/SELL → `get_buy_and_sell_payment_methods`; DEPOSIT/WITHDRAW → `get_deposit_and_withdraw_payment_methods`
3. **`get_price`** — add if the user wants exchange rate info

Skip step 1 for simple price queries (e.g., "What's BTC in USD?").

## Calling APIs

Use `WebFetch` or `Bash` (curl). All responses follow:

```json
{ "code": "000000", "message": null, "data": { ... }, "success": true }
```

`code: "000000"` = success; otherwise check `message`.

## Action Links

After presenting API results, always include a relevant action link so the user can proceed directly on Binance. Build the URL dynamically based on the fiat currency, crypto currency, and business type from the conversation context.

### URL Templates

| Business Type | URL Template | Example |
|---|---|---|
| BUY | `https://www.binance.com/en/crypto/buy/{FIAT}/{CRYPTO}` | [Buy BTC with USD](https://www.binance.com/en/crypto/buy/USD/BTC) |
| SELL | `https://www.binance.com/en/crypto/sell/{FIAT}/{CRYPTO}` | [Sell BTC for USD](https://www.binance.com/en/crypto/sell/USD/BTC) |
| DEPOSIT | `https://www.binance.com/en/fiat/deposit/{FIAT}` | [Deposit USD](https://www.binance.com/en/fiat/deposit/USD) |
| WITHDRAW | `https://www.binance.com/en/fiat/withdraw/{FIAT}` | [Withdraw USD](https://www.binance.com/en/fiat/withdraw/USD) |

### Language-aware URL

Replace the `/en/` locale segment to match the user's language. Supported locales:

```
en, zh-CN, zh-TC, ru, es, es-LA, fr, vi, en-TR, it, pl, id, uk-UA, ar,
en-AU, pt-BR, en-IN, en-NG, ro, bg, cs, lv, sv, pt, es-MX, el, sk, sl,
es-AR, fr-AF, en-KZ, en-ZA, en-NZ, en-BH, ar-BH, ru-UA, de, kk-KZ,
ru-KZ, ja, da-DK, en-AE, en-JP, hu, lo-LA, si-LK, az-AZ, uz-UZ, pt-AO
```

Common mapping examples:

| User language | Locale | Example URL |
|---|---|---|
| English | `en` | `https://www.binance.com/en/crypto/buy/USD/BTC` |
| 简体中文 | `zh-CN` | `https://www.binance.com/zh-CN/crypto/buy/CNY/BTC` |
| Português (BR) | `pt-BR` | `https://www.binance.com/pt-BR/crypto/buy/BRL/BTC` |
| Türkçe | `en-TR` | `https://www.binance.com/en-TR/crypto/buy/TRY/BTC` |

For regional English variants (en-AU, en-IN, en-NG, en-AE, en-NZ, etc.), use the specific regional locale rather than plain `en` — this ensures the user sees region-appropriate content.

Default to `en` if the user's language is unclear.

Always include at least one action link when the conversation involves a specific fiat/crypto pair or business type. For general questions, include all relevant links from `get_capabilities`. Format as a call-to-action, e.g.: "Ready to buy? [Buy BTC with USD on Binance](https://www.binance.com/en/crypto/buy/USD/BTC)"

## Presenting Results

- Table format for payment methods (names, limits, pricing); flag suspended methods
- Note that prices are indicative/reference prices
- Respond in the user's language
- **Always end with the relevant action link(s)**

### Price Sorting and Best Value Logic

Price direction depends on the business type — always apply the correct comparison:

| Business Type | Better price direction | Rationale |
|---|---|---|
| **BUY** | **Lower price is better** | You pay less fiat per unit of crypto — same fiat buys more crypto |
| **SELL** | **Higher price is better** | You receive more fiat per unit of crypto sold |

When summarizing: for BUY highlight the **lowest** `quotation`; for SELL highlight the **highest** `quotation`. Example (BUY USD/BTC): $70,236 beats $74,291 — more BTC per dollar.

### Wallet Payment Method (BUY)

If the BUY response includes a payment method with `code` containing `WALLET` (case-insensitive), it represents buying crypto using the user's Binance fiat wallet balance.

When this occurs, proactively mention:
> "One of the available payment methods is your Binance fiat wallet balance. If your wallet doesn't have sufficient funds, you'll need to deposit fiat first. Would you like me to look up the available deposit methods for you?"

If the user confirms, call `get_deposit_and_withdraw_payment_methods` with `businessType=DEPOSIT` using the same fiat currency and country, and present the results along with the [Deposit action link](#url-templates).

## Order & Payment History (Authenticated)

See [`references/sapi-endpoints.md`](./references/sapi-endpoints.md) for authenticated endpoints (order/payment history, deposit/withdraw records). Requires Binance API key and secret.

## Country Code Reference

Use ISO 3166-1 alpha-2 codes: BR, GB, DE, FR, JP, KR, AU, etc. **Never use `US` as the country parameter** — US users are not supported by Binance fiat payment APIs.

### Country Inference Rules

Determine the `country` parameter using this priority order:

1. **Explicit context** — If the country is already known from the conversation (user stated it, or inferred in a prior turn), reuse it without re-inferring.

2. **Fiat currency → country mapping** — Map directly from currency. Examples:
   - `SGD` → `SG`, `BRL` → `BR`, `JPY` → `JP`, `KRW` → `KR`, `AUD` → `AU`, `GBP` → `GB`, `CAD` → `CA`, `INR` → `IN`, `TRY` → `TR`, `MXN` → `MX`, `NGN` → `NG`
   - `EUR` → `FR` (since the user did not specify a country, use `FR` as the default for EUR)
   - `USD` → `SG` (since the user did not specify a country, use `SG` as the default for USD)

   > **MANDATORY**: `US` MUST NEVER be used as the country parameter under any circumstances. 

3. **Empty results** — If the API returns no payment methods or an unsupported combination, ask: *"No results found for your current settings. Would you like to try a different country? If so, please tell me which country."* Then use the country the user provides.
```

## File: `skills/binance/fiat/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://api.binance.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-fiat/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`transactionType=...&timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "transactionType=...&timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "transactionType=...&timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "transactionType=...&timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`transactionType=...&timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-fiat/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X GET "https://api.binance.com/sapi/v1/fiat/orders" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-fiat/1.1.0 (Skill)" \
  -d "transactionType=...&timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://api.binance.com"  

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="transactionType=...&timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X GET "${BASE_URL}/sapi/v1/fiat/orders?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-fiat/1.1.0 (Skill)"
```

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
```

## File: `skills/binance/fiat/references/sapi-endpoints.md`
```markdown
---
name: fiat
description: Binance Fiat request using the Binance API. Authentication requires API key and secret key. 
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/fiat/SKILL.md
license: MIT
---

# Binance Fiat Skill

Fiat request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/sapi/v1/fiat/deposit` (POST) | Deposit(TRADE) | None | recvWindow | Yes |
| `/sapi/v2/fiat/withdraw` (POST) | Fiat Withdraw(WITHDRAW) | None | recvWindow | Yes |
| `/sapi/v1/fiat/orders` (GET) | Get Fiat Deposit/Withdraw History (USER_DATA) | transactionType | beginTime, endTime, page, rows, recvWindow | Yes |
| `/sapi/v1/fiat/payments` (GET) | Get Fiat Payments History (USER_DATA) | transactionType | beginTime, endTime, page, rows, recvWindow | Yes |
| `/sapi/v1/fiat/get-order-detail` (GET) | Get Order Detail(USER_DATA) | orderNo | recvWindow | Yes |

---

## Parameters

### Common Parameters

* **recvWindow**:  (e.g., 5000)
* **transactionType**: 0-buy,1-sell
* **beginTime**: 
* **endTime**:  (e.g., 1641782889000)
* **page**: default 1 (e.g., 1)
* **rows**: default 100, max 500 (e.g., 100)
* **orderNo**: order id retrieved from the api call of withdrawal


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://api.binance.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Description: Primary trading account


### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## User Agent Header

Include `User-Agent` header with the following string: `binance-fiat/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/margin-trading/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-10

- Initial release
```

## File: `skills/binance/margin-trading/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/margin-trading/SKILL.md`
```markdown
---
name: margin-trading
description: Binance Margin-trading request using the Binance API. Authentication requires API key and secret key. 
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/margin-trading/SKILL.md
license: MIT
---

# Binance Margin-trading Skill

Margin-trading request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/sapi/v1/margin/max-leverage` (POST) | Adjust cross margin max leverage (USER_DATA) | maxLeverage | None | Yes |
| `/sapi/v1/margin/isolated/account` (DELETE) | Disable Isolated Margin Account (TRADE) | symbol | recvWindow | Yes |
| `/sapi/v1/margin/isolated/account` (POST) | Enable Isolated Margin Account (TRADE) | symbol | recvWindow | Yes |
| `/sapi/v1/margin/isolated/account` (GET) | Query Isolated Margin Account Info (USER_DATA) | None | symbols, recvWindow | Yes |
| `/sapi/v1/bnbBurn` (GET) | Get BNB Burn Status (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/margin/tradeCoeff` (GET) | Get Summary of Margin account (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/margin/capital-flow` (GET) | Query Cross Isolated Margin Capital Flow (USER_DATA) | None | asset, symbol, type, startTime, endTime, fromId, limit, recvWindow | Yes |
| `/sapi/v1/margin/account` (GET) | Query Cross Margin Account Details (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/margin/crossMarginData` (GET) | Query Cross Margin Fee Data (USER_DATA) | None | vipLevel, coin, recvWindow | Yes |
| `/sapi/v1/margin/isolated/accountLimit` (GET) | Query Enabled Isolated Margin Account Limit (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/margin/isolatedMarginData` (GET) | Query Isolated Margin Fee Data (USER_DATA) | None | vipLevel, symbol, recvWindow | Yes |
| `/sapi/v1/margin/interestHistory` (GET) | Get Interest History (USER_DATA) | None | asset, isolatedSymbol, startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/margin/next-hourly-interest-rate` (GET) | Get future hourly interest rate (USER_DATA) | assets, isIsolated | None | Yes |
| `/sapi/v1/margin/borrow-repay` (POST) | Margin account borrow/repay(MARGIN) | asset, isIsolated, symbol, amount, type | recvWindow | Yes |
| `/sapi/v1/margin/borrow-repay` (GET) | Query borrow/repay records in Margin account(USER_DATA) | type | asset, isolatedSymbol, txId, startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/margin/interestRateHistory` (GET) | Query Margin Interest Rate History (USER_DATA) | asset | vipLevel, startTime, endTime, recvWindow | Yes |
| `/sapi/v1/margin/maxBorrowable` (GET) | Query Max Borrow (USER_DATA) | asset | isolatedSymbol, recvWindow | Yes |
| `/sapi/v1/margin/crossMarginCollateralRatio` (GET) | Cross margin collateral ratio (MARKET_DATA) | None | None | No |
| `/sapi/v1/margin/allPairs` (GET) | Get All Cross Margin Pairs (MARKET_DATA) | None | symbol | No |
| `/sapi/v1/margin/isolated/allPairs` (GET) | Get All Isolated Margin Symbol(MARKET_DATA) | None | symbol, recvWindow | No |
| `/sapi/v1/margin/allAssets` (GET) | Get All Margin Assets (MARKET_DATA) | None | asset | No |
| `/sapi/v1/margin/delist-schedule` (GET) | Get Delist Schedule (MARKET_DATA) | None | recvWindow | No |
| `/sapi/v1/margin/limit-price-pairs` (GET) | Get Limit Price Pairs(MARKET_DATA) | None | None | No |
| `/sapi/v1/margin/list-schedule` (GET) | Get list Schedule (MARKET_DATA) | None | recvWindow | No |
| `/sapi/v1/margin/risk-based-liquidation-ratio` (GET) | Get Margin Asset Risk-Based Liquidation Ratio (MARKET_DATA) | None | None | No |
| `/sapi/v1/margin/restricted-asset` (GET) | Get Margin Restricted Assets (MARKET_DATA) | None | None | No |
| `/sapi/v1/margin/isolatedMarginTier` (GET) | Query Isolated Margin Tier Data (USER_DATA) | symbol | tier, recvWindow | Yes |
| `/sapi/v1/margin/leverageBracket` (GET) | Query Liability Coin Leverage Bracket in Cross Margin Pro Mode(MARKET_DATA) | None | None | No |
| `/sapi/v1/margin/priceIndex` (GET) | Query Margin PriceIndex (MARKET_DATA) | symbol | None | No |
| `/sapi/v1/margin/available-inventory` (GET) | Query Margin Available Inventory(USER_DATA) | type | None | Yes |
| `/sapi/v1/margin/listen-key` (DELETE) | Close User Data Stream (USER_STREAM) | None | None | No |
| `/sapi/v1/margin/listen-key` (PUT) | Keepalive User Data Stream (USER_STREAM) | listenKey | None | No |
| `/sapi/v1/margin/listen-key` (POST) | Start User Data Stream (USER_STREAM) | None | None | No |
| `/sapi/v1/margin/apiKey` (POST) | Create Special Key(Low-Latency Trading)(TRADE) | apiName | symbol, ip, publicKey, permissionMode, recvWindow | Yes |
| `/sapi/v1/margin/apiKey` (DELETE) | Delete Special Key(Low-Latency Trading)(TRADE) | None | apiName, symbol, recvWindow | Yes |
| `/sapi/v1/margin/apiKey` (GET) | Query Special key(Low Latency Trading)(TRADE) | None | symbol, recvWindow | Yes |
| `/sapi/v1/margin/apiKey/ip` (PUT) | Edit ip for Special Key(Low-Latency Trading)(TRADE) | ip | symbol, recvWindow | Yes |
| `/sapi/v1/margin/forceLiquidationRec` (GET) | Get Force Liquidation Record (USER_DATA) | None | startTime, endTime, isolatedSymbol, current, size, recvWindow | Yes |
| `/sapi/v1/margin/exchange-small-liability` (GET) | Get Small Liability Exchange Coin List (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/margin/exchange-small-liability` (POST) | Small Liability Exchange (MARGIN) | assetNames | recvWindow | Yes |
| `/sapi/v1/margin/exchange-small-liability-history` (GET) | Get Small Liability Exchange History (USER_DATA) | current, size | startTime, endTime, recvWindow | Yes |
| `/sapi/v1/margin/openOrders` (DELETE) | Margin Account Cancel all Open Orders on a Symbol (TRADE) | symbol | isIsolated, recvWindow | Yes |
| `/sapi/v1/margin/openOrders` (GET) | Query Margin Account's Open Orders (USER_DATA) | None | symbol, isIsolated, recvWindow | Yes |
| `/sapi/v1/margin/orderList` (DELETE) | Margin Account Cancel OCO (TRADE) | symbol | isIsolated, orderListId, listClientOrderId, newClientOrderId, recvWindow | Yes |
| `/sapi/v1/margin/orderList` (GET) | Query Margin Account's OCO (USER_DATA) | None | isIsolated, symbol, orderListId, origClientOrderId, recvWindow | Yes |
| `/sapi/v1/margin/order` (DELETE) | Margin Account Cancel Order (TRADE) | symbol | isIsolated, orderId, origClientOrderId, newClientOrderId, recvWindow | Yes |
| `/sapi/v1/margin/order` (POST) | Margin Account New Order (TRADE) | symbol, side, type | isIsolated, quantity, quoteOrderQty, price, stopPrice, newClientOrderId, icebergQty, newOrderRespType, sideEffectType, timeInForce, selfTradePreventionMode, autoRepayAtCancel, recvWindow | Yes |
| `/sapi/v1/margin/order` (GET) | Query Margin Account's Order (USER_DATA) | symbol | isIsolated, orderId, origClientOrderId, recvWindow | Yes |
| `/sapi/v1/margin/order/oco` (POST) | Margin Account New OCO (TRADE) | symbol, side, quantity, price, stopPrice | isIsolated, listClientOrderId, limitClientOrderId, limitIcebergQty, stopClientOrderId, stopLimitPrice, stopIcebergQty, stopLimitTimeInForce, newOrderRespType, sideEffectType, selfTradePreventionMode, autoRepayAtCancel, recvWindow | Yes |
| `/sapi/v1/margin/order/oto` (POST) | Margin Account New OTO (TRADE) | symbol, workingType, workingSide, workingPrice, workingQuantity, workingIcebergQty, pendingType, pendingSide, pendingQuantity | isIsolated, listClientOrderId, newOrderRespType, sideEffectType, selfTradePreventionMode, autoRepayAtCancel, workingClientOrderId, workingTimeInForce, pendingClientOrderId, pendingPrice, pendingStopPrice, pendingTrailingDelta, pendingIcebergQty, pendingTimeInForce | Yes |
| `/sapi/v1/margin/order/otoco` (POST) | Margin Account New OTOCO (TRADE) | symbol, workingType, workingSide, workingPrice, workingQuantity, pendingSide, pendingQuantity, pendingAboveType | isIsolated, sideEffectType, autoRepayAtCancel, listClientOrderId, newOrderRespType, selfTradePreventionMode, workingClientOrderId, workingIcebergQty, workingTimeInForce, pendingAboveClientOrderId, pendingAbovePrice, pendingAboveStopPrice, pendingAboveTrailingDelta, pendingAboveIcebergQty, pendingAboveTimeInForce, pendingBelowType, pendingBelowClientOrderId, pendingBelowPrice, pendingBelowStopPrice, pendingBelowTrailingDelta, pendingBelowIcebergQty, pendingBelowTimeInForce | Yes |
| `/sapi/v1/margin/manual-liquidation` (POST) | Margin Manual Liquidation(MARGIN) | type | symbol, recvWindow | Yes |
| `/sapi/v1/margin/rateLimit/order` (GET) | Query Current Margin Order Count Usage (TRADE) | None | isIsolated, symbol, recvWindow | Yes |
| `/sapi/v1/margin/allOrderList` (GET) | Query Margin Account's all OCO (USER_DATA) | None | isIsolated, symbol, fromId, startTime, endTime, limit, recvWindow | Yes |
| `/sapi/v1/margin/allOrders` (GET) | Query Margin Account's All Orders (USER_DATA) | symbol | isIsolated, orderId, startTime, endTime, limit, recvWindow | Yes |
| `/sapi/v1/margin/openOrderList` (GET) | Query Margin Account's Open OCO (USER_DATA) | None | isIsolated, symbol, recvWindow | Yes |
| `/sapi/v1/margin/myTrades` (GET) | Query Margin Account's Trade List (USER_DATA) | symbol | isIsolated, orderId, startTime, endTime, fromId, limit, recvWindow | Yes |
| `/sapi/v1/margin/myPreventedMatches` (GET) | Query Prevented Matches(USER_DATA) | symbol | preventedMatchId, orderId, fromPreventedMatchId, recvWindow, isIsolated | Yes |
| `/sapi/v1/margin/api-key-list` (GET) | Query Special key List(Low Latency Trading)(TRADE) | None | symbol, recvWindow | Yes |
| `/sapi/v1/margin/transfer` (GET) | Get Cross Margin Transfer History (USER_DATA) | None | asset, type, startTime, endTime, current, size, isolatedSymbol, recvWindow | Yes |
| `/sapi/v1/margin/maxTransferable` (GET) | Query Max Transfer-Out Amount (USER_DATA) | asset | isolatedSymbol, recvWindow | Yes |

---

## Parameters

### Common Parameters

* **maxLeverage**: Can only adjust 3 , 5 or 10，Example: maxLeverage = 5 or 3 for Cross Margin Classic; maxLeverage=10 for Cross Margin Pro 10x leverage or 20x if compliance allows.
* **symbol**: 
* **recvWindow**: No more than 60000 (e.g., 5000)
* **asset**: 
* **symbol**: isolated margin pair
* **type**: Transfer Type: ROLL_IN, ROLL_OUT
* **startTime**: Only supports querying data from the past 90 days. (e.g., 1623319461670)
* **endTime**:  (e.g., 1641782889000)
* **fromId**: If `fromId` is set, data with `id` greater than `fromId` will be returned. Otherwise, the latest data will be returned. (e.g., 1)
* **limit**: Limit on the number of data records returned per request. Default: 500; Maximum: 1000. (e.g., 500)
* **vipLevel**: User's current specific margin data will be returned if vipLevel is omitted (e.g., 1)
* **coin**: 
* **symbols**: Max 5 symbols can be sent; separated by ",". e.g. "BTCUSDT,BNBUSDT,ADAUSDT"
* **isolatedSymbol**: isolated symbol
* **current**: Currently querying page. Start from 1. Default:1 (e.g., 1)
* **size**: Default:10 Max:100 (e.g., 10)
* **assets**: List of assets, separated by commas, up to 20
* **isIsolated**: for isolated margin or not, "TRUE", "FALSE"
* **asset**: 
* **isIsolated**: `TRUE` for Isolated Margin, `FALSE` for Cross Margin, Default `FALSE` (e.g., FALSE)
* **amount**: 
* **type**: `MARGIN`,`ISOLATED`
* **txId**: `tranId` in `POST /sapi/v1/margin/loan` (e.g., 1)
* **tier**: All margin tier data will be returned if tier is omitted
* **listenKey**: 
* **apiName**: 
* **ip**: Can be added in batches, separated by commas. Max 30 for an API key
* **publicKey**: 1. If publicKey is inputted it will create an RSA or Ed25519 key.  2. Need to be encoded to URL-encoded format
* **permissionMode**: This parameter is only for the Ed25519 API key, and does not effact for other encryption methods. The value can be TRADE (TRADE for all permissions) or READ (READ for USER_DATA, FIX_API_READ_ONLY). The default value is TRADE. (e.g., value)
* **apiName**: 
* **ip**: Can be added in batches, separated by commas. Max 30 for an API key
* **current**: Currently querying page. Start from 1. Default:1 (e.g., 1)
* **size**: Default:10, Max:100 (e.g., 10)
* **isIsolated**: For isolated margin or not, "TRUE", "FALSE", default "FALSE"
* **orderListId**: Either `orderListId` or `listClientOrderId` must be provided (e.g., 1)
* **listClientOrderId**: Either `orderListId` or `listClientOrderId` must be provided (e.g., 1)
* **newClientOrderId**: Used to uniquely identify this cancel. Automatically generated by default (e.g., 1)
* **orderId**:  (e.g., 1)
* **origClientOrderId**:  (e.g., 1)
* **quantity**:  (e.g., 1.0)
* **limitClientOrderId**: A unique Id for the limit order (e.g., 1)
* **price**:  (e.g., 1.0)
* **limitIcebergQty**:  (e.g., 1.0)
* **stopClientOrderId**: A unique Id for the stop loss/stop loss limit leg (e.g., 1)
* **stopPrice**:  (e.g., 1.0)
* **stopLimitPrice**: If provided, `stopLimitTimeInForce` is required. (e.g., 1.0)
* **stopIcebergQty**:  (e.g., 1.0)
* **stopLimitTimeInForce**: Valid values are `GTC`/`FOK`/`IOC`
* **sideEffectType**: NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY,AUTO_BORROW_REPAY; default NO_SIDE_EFFECT. More info in FAQ (e.g., NO_SIDE_EFFECT)
* **selfTradePreventionMode**: The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE (e.g., NONE)
* **autoRepayAtCancel**: Only when MARGIN_BUY or AUTO_BORROW_REPAY order takes effect, true means that the debt generated by the order needs to be repay after the order is cancelled. The default is true (e.g., true)
* **workingType**: Supported values: `LIMIT`, `LIMIT_MAKER`
* **workingSide**: BUY, SELL
* **workingClientOrderId**: Arbitrary unique ID among open orders for the working order. Automatically generated if not sent. (e.g., 1)
* **workingPrice**:  (e.g., 1.0)
* **workingQuantity**:  (e.g., 1.0)
* **workingIcebergQty**: This can only be used if `workingTimeInForce` is `GTC`. (e.g., 1.0)
* **workingTimeInForce**: GTC,IOC,FOK
* **pendingType**: Supported values: Order Types Note that `MARKET` orders using `quoteOrderQty` are not supported. (e.g., Order Types)
* **pendingSide**: BUY, SELL
* **pendingClientOrderId**: Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent. (e.g., 1)
* **pendingPrice**:  (e.g., 1.0)
* **pendingStopPrice**:  (e.g., 1.0)
* **pendingTrailingDelta**:  (e.g., 1.0)
* **pendingQuantity**:  (e.g., 1.0)
* **pendingIcebergQty**: This can only be used if `pendingTimeInForce` is `GTC`. (e.g., 1.0)
* **pendingTimeInForce**: GTC,IOC,FOK
* **workingIcebergQty**: This can only be used if `workingTimeInForce` is `GTC`. (e.g., 1.0)
* **pendingAboveType**: Supported values: `LIMIT_MAKER`, `STOP_LOSS`, and `STOP_LOSS_LIMIT`
* **pendingAboveClientOrderId**: Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent. (e.g., 1)
* **pendingAbovePrice**:  (e.g., 1.0)
* **pendingAboveStopPrice**:  (e.g., 1.0)
* **pendingAboveTrailingDelta**:  (e.g., 1.0)
* **pendingAboveIcebergQty**: This can only be used if `pendingAboveTimeInForce` is `GTC`. (e.g., 1.0)
* **pendingAboveTimeInForce**: 
* **pendingBelowType**: Supported values: `LIMIT_MAKER`, `STOP_LOSS`, and `STOP_LOSS_LIMIT`
* **pendingBelowClientOrderId**: Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent. (e.g., 1)
* **pendingBelowPrice**:  (e.g., 1.0)
* **pendingBelowStopPrice**:  (e.g., 1.0)
* **pendingBelowTrailingDelta**:  (e.g., 1.0)
* **pendingBelowIcebergQty**: This can only be used if `pendingBelowTimeInForce` is `GTC`. (e.g., 1.0)
* **pendingBelowTimeInForce**: 
* **quantity**:  (e.g., 1.0)
* **quoteOrderQty**:  (e.g., 1.0)
* **price**:  (e.g., 1.0)
* **stopPrice**: Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders. (e.g., 1.0)
* **icebergQty**: Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order. (e.g., 1.0)
* **preventedMatchId**:  (e.g., 1)
* **fromPreventedMatchId**:  (e.g., 1)
* **assetNames**: The assets list of small liability exchange， Example: assetNames = BTC,ETH


### Enums

* **side**: BUY | SELL
* **newOrderRespType**: ACK | RESULT | FULL
* **timeInForce**: GTC | IOC | FOK


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://api.binance.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Description: Primary trading account


### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## New Client Order ID 

For endpoints that include the `newClientOrderId` parameter, the value must always start with `agent-`. If the parameter is not provided, `agent-` followed by 18 random alphanumeric characters will be generated automatically. If a value is provided, it will be prefixed with `agent-`

Example: `agent-1a2b3c4d5e6f7g8h9i`

## User Agent Header

Include `User-Agent` header with the following string: `binance-margin-trading/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/margin-trading/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://api.binance.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-margin-trading/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-margin-trading/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X GET "https://api.binance.com/sapi/v1/margin/isolated/account" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-margin-trading/1.1.0 (Skill)" \
  -d "timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://api.binance.com"  

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X GET "${BASE_URL}/sapi/v1/margin/isolated/account?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-margin-trading/1.1.0 (Skill)"
```

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
```

## File: `skills/binance/onchain-pay/.gitignore`
```
.local.md
*.pem
```

## File: `skills/binance/onchain-pay/.local.md.example`
```
## Connect Accounts

### prod (default)
- Base URL: https://api.commonservice.io
- Client ID: your-client-id
- API Key: your-api-key
- PEM Path: /absolute/path/to/your/private.pem
- Default Network: your-preferred-network
- Default Address: your-wallet-address
- Description: Production account
```

## File: `skills/binance/onchain-pay/CHANGELOG.md`
```markdown
# Changelog

## 0.1.1 - 2026-03-17

### Fixed
- **Cross-platform timestamp generation**: Fixed `date +%s000` to use `$(($(date +%s) * 1000))` for proper millisecond timestamp on macOS, Linux, and BSD
- **Documentation updates**: Updated all examples in SKILL.md and authentication.md to use cross-platform compatible timestamp generation
- **Improved error handling**: Added notes about common JSON parsing errors caused by incorrect timestamp format

### Changed
- Updated `scripts/sign_and_call.sh` to use arithmetic expansion for timestamp generation
- Added troubleshooting section in SKILL.md for timestamp-related issues

## 0.1.0 - 2026-03-11

- Initial release
- Support for Payment Method List (v1/v2), Trading Pairs, Estimated Quote, Pre-order, Get Order, Crypto Network, P2P Trading Pairs endpoints
- RSA SHA256 request signing via bundled script
- Multi-account credential management via `.local.md`
- Customization options for pre-order (Onchain-Pay Easy, P2P Express, Skip Cashier, etc.)
```

## File: `skills/binance/onchain-pay/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/onchain-pay/SKILL.md`
```markdown
---
name: onchain-pay-open-api
description: |
  Binance Onchain Pay enables users to buy cryptocurrency with fiat (e.g., EUR, USD) or send existing crypto from their Binance account directly to any external on-chain wallet address in a single flow—no manual withdrawal needed.
  
  Enables partners to integrate crypto buying services:
  - payment-method-list: Get available payment methods (Card, P2P, Google Pay, Apple Pay, etc.) with limits for a fiat/crypto pair
  - trading-pairs: List all supported fiat currencies and cryptocurrencies
  - estimated-quote: Get real-time price quote including exchange rate, fees, and estimated crypto amount
  - pre-order: Create a buy order and get redirect URL to Binance payment flow
  - order: Query order status and details (processing, completed, failed, etc.)
  - crypto-network: Get supported blockchain networks with withdraw fees and limits
  - p2p/trading-pairs: List P2P-specific trading pairs
metadata:
  version: 0.1.1
  author: onchain-pay-team
license: MIT
---

# Binance Onchain-Pay Open API Skill

Call Binance Onchain-Pay Open API endpoints with automatic RSA SHA256 request signing.

## Use Cases & Scenarios

This skill is designed for the following scenarios:

### 1. 💳 Fiat-to-Crypto Purchase & Send
**When to use**: User wants to buy crypto with fiat currency and send directly to an external on-chain wallet address
- Buy USDT with USD/EUR/TWD using credit card → Send to MetaMask address on BSC
- Purchase BTC with Google Pay → Transfer to hardware wallet
- Buy USDC with P2P → Send to DeFi protocol contract address

**Key APIs**: `trading-pairs` → `payment-method-list` → `estimated-quote` → `pre-order`

### 2. 🔄 Direct Crypto Transfer (Send Primary)
**When to use**: User has crypto in Binance account and wants to send to external address
- Send existing USDT from Binance Spot to friend's wallet address
- Transfer ETH to Uniswap contract for trading
- Move crypto from Binance to self-custodial wallet (Trust Wallet, Ledger, etc.)

**Key APIs**: `pre-order` with `SEND_PRIMARY` customization

### 3. 🔗 Cross-Chain Bridge Operations
**When to use**: User needs to buy crypto on one chain and transfer to another network
- Buy USDC on Ethereum → Bridge to Polygon for lower fees
- Purchase tokens on BSC → Transfer to Base network
- Fiat to crypto on Solana → Send to Arbitrum for DeFi

**Key APIs**: `crypto-network` → `pre-order` with network selection

### 4. 🏪 Merchant Payment Integration
**When to use**: Integrate crypto payment gateway for e-commerce or services
- Accept fiat payments and auto-convert to crypto
- Enable "Pay with Crypto" checkout flow
- Process subscription payments with crypto

**Key APIs**: `pre-order` with `externalOrderId` tracking

### 5. 🤖 Smart Contract Interaction (Onchain-Pay Easy)
**When to use**: Buy crypto and execute smart contract in one transaction
- Buy USDT and deposit to lending protocol
- Purchase tokens and stake in DeFi pool
- Fiat on-ramp directly to GameFi or NFT marketplace

**Key APIs**: `pre-order` with `ON_CHAIN_PROXY_MODE` customization

### 6. 📊 Query & Monitoring
**When to use**: Check order status, available networks, or payment methods
- Monitor order processing status (pending, completed, failed)
- List supported fiat currencies and cryptocurrencies
- Check available payment methods for specific country/amount
- Verify network fees and limits

**Key APIs**: `order`, `crypto-network`, `trading-pairs`, `payment-method-list`

---

## Quick Reference

| Endpoint | API Path | Required Params | Optional Params |
|----------|----------|-----------------|-----------------|
| Payment Method List (v1) | `papi/v1/ramp/connect/buy/payment-method-list` | fiatCurrency, cryptoCurrency, totalAmount, amountType | network, contractAddress |
| Payment Method List (v2) | `papi/v2/ramp/connect/buy/payment-method-list` | (none) | lang |
| Trading Pairs | `papi/v1/ramp/connect/buy/trading-pairs` | (none) | (none) |
| Estimated Quote | `papi/v1/ramp/connect/buy/estimated-quote` | fiatCurrency, requestedAmount, payMethodCode, amountType | cryptoCurrency, contractAddress, address, network |
| Pre-order | `papi/v1/ramp/connect/gray/buy/pre-order` | externalOrderId, merchantCode, merchantName, ts | fiatCurrency, fiatAmount, cryptoCurrency, requestedAmount, amountType, address, network, payMethodCode, payMethodSubCode, redirectUrl, failRedirectUrl, redirectDeepLink, failRedirectDeepLink, customization, destContractAddress, destContractABI, destContractParams, affiliateCode, gtrTemplateCode, contractAddress |
| Get Order | `papi/v1/ramp/connect/order` | externalOrderId | (none) |
| Crypto Network | `papi/v1/ramp/connect/crypto-network` | (none) | (none) |
| P2P Trading Pairs | `papi/v1/ramp/connect/buy/p2p/trading-pairs` | (none) | fiatCurrency |

---

## How to Execute a Request

### Step 1: Gather credentials

Use the default account (prod) unless the user specifies otherwise. You need:

- **BASE_URL**: API base URL
- **CLIENT_ID**: Client identifier
- **API_KEY**: The sign access token
- **PEM_PATH**: Absolute path to the RSA private key PEM file

Use the account marked `(default)` in `.local.md`.

### Step 2: Build the JSON body

Build a compact JSON body from user-specified parameters. Remove any parameters the user did not provide.

**IMPORTANT: Address and Network Validation**
- `address` (destination wallet address) and `network` (blockchain network) are REQUIRED for all pre-order requests
- If the user has configured `Default Address` and `Default Network` in `.local.md`, use them automatically
- If not configured or not provided by user, ASK the user to provide both values before proceeding

### Step 3: Sign and call using the bundled script

```bash
bash <skill_path>/scripts/sign_and_call.sh \
  "<BASE_URL>" \
  "<API_PATH>" \
  "<CLIENT_ID>" \
  "<API_KEY>" \
  "<PEM_PATH>" \
  '<JSON_BODY>'
```

### Step 4: Return results

Display the JSON response to the user in a readable format.

---

## Authentication

See [`references/authentication.md`](AUTHENTICATION.md) for full signing details.

Summary:
1. Payload = `JSON_BODY` + `TIMESTAMP` (milliseconds)
2. Sign payload with RSA SHA256 using PEM private key
3. Base64 encode the signature (single line)
4. Send as POST with headers: `X-Tesla-ClientId`, `X-Tesla-SignAccessToken`, `X-Tesla-Signature`, `X-Tesla-Timestamp`, `Content-Type: application/json`

---

## Parameters Reference

### Payment Method List v1 (`buy/payment-method-list`)

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| fiatCurrency | string | Yes | Fiat currency code (e.g., `USD`, `EUR`, `BRL`, `UGX`) |
| cryptoCurrency | string | Yes | Crypto currency code (e.g., `BTC`, `USDT`, `USDC`, `SEI`) |
| totalAmount | number | Yes | Amount value |
| amountType | number | Yes | `1` = fiat amount, `2` = crypto amount |
| network | string | No | Blockchain network (e.g., `BSC`, `ETH`, `SOL`, `BASE`, `SEI`) |
| contractAddress | string | No | Token contract address (required for non-native tokens) |

### Payment Method List v2 (`v2/buy/payment-method-list`)

Get all available payment methods without specifying fiat/crypto parameters. Simplified version of v1.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| lang | string | No | Language code for localized payment method names (e.g., `en`, `cn`, `es`) |

**Differences from v1**:
- **Simpler**: No need to specify fiatCurrency, cryptoCurrency, or amount
- **Comprehensive**: Returns all available payment methods for the merchant
- **Use case**: Useful for displaying all options before user input

**Response Format**: Same as v1, returns list of payment methods with their limits and properties.

### Estimated Quote (`buy/estimated-quote`)

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| fiatCurrency | string | Yes | Fiat currency code |
| cryptoCurrency | string | No | Crypto currency code (optional if contractAddress provided) |
| requestedAmount | number | Yes | Amount value |
| payMethodCode | string | Yes | Payment method (e.g., `BUY_CARD`, `BUY_GOOGLE_PAY`, `BUY_P2P`, `BUY_WALLET`) |
| amountType | number | Yes | `1` = fiat amount, `2` = crypto amount |
| network | string | **Yes*** | Blockchain network (can use default from `.local.md`) |
| contractAddress | string | No | Token contract address |
| address | string | **Yes*** | Destination wallet address for receiving crypto |

\* Recommended: These parameters should be provided. If not specified by user, check `.local.md` for defaults. If no defaults exist, ask user before proceeding.

### Pre-order (`buy/pre-order`)

Create a buy pre-order and return the redirect link for payment.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| externalOrderId | string | Yes | Partner's unique order ID (must be unique) |
| merchantCode | string | Yes | Merchant code (e.g., `connect-gray`) |
| merchantName | string | Yes | Merchant display name (e.g., `GrayTest`) |
| ts | number | Yes | Current timestamp in milliseconds |
| fiatCurrency | string | No* | Fiat currency code (e.g., `TWD`, `USD`, `EUR`) |
| fiatAmount | number | No* | Fiat amount to spend |
| cryptoCurrency | string | No* | Crypto currency to buy (e.g., `USDT`, `BTC`, `ETH`) |
| requestedAmount | number | No* | Amount value (fiat or crypto based on amountType) |
| amountType | number | No* | `1` = fiat amount, `2` = crypto amount |
| address | string | No | Destination wallet address for receiving crypto |
| network | string | No | Blockchain network (e.g., `BSC`, `ETH`, `SOL`) |
| payMethodCode | string | No | Payment method code (e.g., `BUY_CARD`, `BUY_P2P`, `BUY_GOOGLE_PAY`, `BUY_APPLE_PAY`, `BUY_PAYPAL`, `BUY_WALLET`, `BUY_REVOLUT`) |
| payMethodSubCode | string | No | Payment method sub-code (e.g., `card`, `GOOGLE_PAY`, `WECHAT`) |
| redirectUrl | string | No | Success redirect URL |
| failRedirectUrl | string | No | Failure redirect URL |
| redirectDeepLink | string | No | Deep link for success (mobile apps) |
| failRedirectDeepLink | string | No | Deep link for failure (mobile apps) |
| customization | object | No | Custom configuration object (see Customization section below) |
| destContractAddress | string | No | Destination contract address (for Onchain-Pay Easy mode) |
| destContractABI | string | No | Contract ABI name (for Onchain-Pay Easy mode) |
| destContractParams | object | No | Contract parameters (for Onchain-Pay Easy mode) |
| affiliateCode | string | No | Affiliate code for commission tracking |
| gtrTemplateCode | string | No | GTR template code (e.g., `OTHERS`) |
| contractAddress | string | No | Token contract address (for non-native tokens) |

\* Either `fiatAmount` or (`requestedAmount` + `amountType`) should be provided. If `fiatCurrency` is not provided, the system will auto-select available fiat currencies.

**Response Example**:
```json
{
  "code": "000000",
  "message": "success",
  "data": {
    "link": "https://app.binance.com/uni-qr/ccnt?...",
    "linkExpireTime": 1772852565045
  },
  "success": true
}
```

### Get Order (`order`)

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| externalOrderId | string | Yes | The external order ID to query |

---

## Customization Options

The `customization` field in pre-order API accepts various flags to customize the buy flow behavior. Each merchant must have the corresponding permission configured in `db.merchant_info` table.

### Available Customization Flags

| Flag | Code | Type | Availability | Description | Use Case |
|------|------|------|--------------|-------------|----------|
| `LOCK_ORDER_ATTRIBUTES` | 1 | array | Open API ✓ | Lock specific order attributes so users cannot modify them. Values: `1`=fiat currency, `2`=crypto currency, `3`=amount, `4`=payment method, `5`=network, `6`=address, `7`=fiat amount, `8`=crypto amount | Fixed-parameter orders |
| `SKIP_CASHIER` | 2 | boolean | Open API ✓ | Skip the cashier page and proceed directly to payment. Reduces user friction in the checkout flow. | Streamlined payment experience |
| `AUTO_REDIRECTION` | 3 | boolean | Open API ✓ | Automatically redirect to `redirectUrl` after order completion without showing success page. | Seamless user experience |
| `HIDE_SEND` | 6 | boolean | Open API ✓ | Hide the "Send" tab in the UI. Useful when only buy flow is needed. | Buy-only integration |
| `SEND_PRIMARY` | 7 | boolean | Open API ✓ | Enable Send Crypto feature. If user's Binance balance is insufficient, auto-trigger buy flow first. | Send crypto to external address |
| `MERCHANT_DISPLAY_NAME` | 8 | string | Open API ✓ | Override the display name shown to users in the UI. | Custom branding |
| `NET_RECEIVE` | 9 | boolean | Open API ✓ | User receives net amount after deducting all fees. Total cost is more transparent. | Better UX for showing final received amount |
| `P2P_EXPRESS` | 10 | boolean | Open API ✓ | Enable P2P Express mode for faster P2P order matching. | Quick P2P transactions |
| `OPEN_NETWORK` | 11 | boolean | Web3 only | Allow users to select different networks. Default is locked to pre-selected network. **Note**: Currently only available for Web3 entrance, not available for Open API. | Multi-network support (Web3 only) |
| `ON_CHAIN_PROXY_MODE` | 12 | boolean | Open API ✓ | Enable Onchain-Pay Easy mode. After buying crypto, Onchain-Pay will execute smart contract interaction instead of direct withdrawal to user wallet. Requires `destContractAddress`, `destContractABI`, and `destContractParams`. | Fiat to Smart Contract integration |
| `SEND_PRIMARY_FLEXIBLE` | 13 | boolean | Open API ✓ | Flexible Send Primary mode with more options. | Advanced send crypto scenarios |

### Customization Examples

**Example 1: Basic Card Payment**
```json
{
  "customization": {}
}
```

**Example 2: Onchain-Pay Easy (On-Chain Proxy)**
```json
{
  "customization": {
    "ON_CHAIN_PROXY_MODE": true,
    "NET_RECEIVE": true,
    "SEND_PRIMARY": true
  },
  "destContractAddress": "0x128...974",
  "destContractABI": "depositFor",
  "destContractParams": {
    "accountType": 2
  }
}
```

**Example 3: Send Crypto**
```json
{
  "customization": {
    "SEND_PRIMARY_FLEXIBLE": true,
    "SEND_PRIMARY": true
  }
}
```

**Example 4: P2P with Auto Redirection**
```json
{
  "customization": {
    "AUTO_REDIRECTION": true,
    "P2P_EXPRESS": true
  }
}
```

**Example 5: Lock Order Attributes**
```json
{
  "customization": {
    "LOCK_ORDER_ATTRIBUTES": [2, 3, 6, 7, 8],
    "MERCHANT_DISPLAY_NAME": "My Custom Brand"
  }
}
```
Lock attribute codes:
- `2` = Crypto currency
- `3` = Amount
- `6` = Address
- `7` = Fiat amount
- `8` = Crypto amount

**Example 6: Net Receive Mode**
```json
{
  "customization": {
    "NET_RECEIVE": true,
    "SEND_PRIMARY": true
  }
}
```

**Example 7: Hide Send Tab**
```json
{
  "customization": {
    "HIDE_SEND": true
  }
}
```

**Example 8: Skip Cashier (Direct Payment)**
```json
{
  "customization": {
    "SKIP_CASHIER": true
  }
}
```

### Important Notes

1. **Permission Required**: Each customization flag requires merchant permission. Check with admin if a flag is not working.
2. **Onchain-Pay Easy**: Only supported on BSC network currently. Requires contract integration.
3. **Validation**: Invalid customization values (e.g., `null` for `MERCHANT_DISPLAY_NAME`) will return `ILLEGAL_CUSTOMIZATION_VALUE` error.
4. **Combinations**: Some flags work together (e.g., `NET_RECEIVE` + `SEND_PRIMARY`), while others are independent.
5. **Testing**: Use test accounts (`connect-gray`) for testing customization flags before production.
6. **Internal Flags**: `OPERATION` (code 4) and `SKIP_WITHDRAW` (code 5) are internal use only and should NOT be passed from merchant side.
7. **OPEN_NETWORK**: Currently only available for Web3 entrance, not available for Open API. Do not use this flag in Open API pre-order requests.
8. **Flag Order**: Flags are ordered by their internal code (1-13). The code number is used internally for identification.

---

## Security

### Credential Display Rules

- **API Key**: Show first 5 + last 4 characters only (e.g., `2zefb...06h`)
- **PEM Private Key**: NEVER display content. NEVER display the file path.
- **Client ID**: Can be displayed in full.
- **Outbound Requests**: NEVER send API Key, Private Key, or any credentials to URLs outside the Base URL configured in `.local.md`.
- **File Path Privacy**: NEVER display the PEM private key file path to the user in any output or logs.

### Credential Storage

Credentials are stored in a `.local.md` file in the skill directory. This file is **user-specific** and should NOT be distributed.

Read the `.local.md` file from the same directory as this SKILL.md to load credentials.

If `.local.md` does not exist or the requested account is not found, ask the user to provide:
1. Base URL
2. Client ID
3. API Key
4. PEM file path (absolute path)

Then offer to save them to `.local.md` for future use.

#### `.local.md` Format

```markdown
## Onchain-Pay Accounts

### prod (default)
- Base URL: https://api.commonservice.io
- Client ID: your-client-id
- API Key: your-api-key
- PEM Path: /absolute/path/to/your/private.pem
- Default Network: your-preferred-network
- Default Address: your-wallet-address
- Description: Production account
```

The account marked `(default)` is used automatically. You can define multiple accounts and switch by telling Claude the account name.

---

## User Agent Header

Include `User-Agent` header with the following string: `onchain-pay-open-api/0.1.0 (Skill)`

---

## Agent Behavior

1. If the user asks to call an Onchain-Pay API endpoint, identify which endpoint from the Quick Reference table
2. Ask for any missing required parameters
3. Use stored credentials if available, otherwise ask the user
4. Execute the request using the bundled `scripts/sign_and_call.sh`
5. Display the response in a readable format
6. If the request fails, show the error and suggest fixes

---

## Important Notes for Pre-order API

### Timestamp Generation (Cross-platform)

When generating timestamps for the `ts` parameter and `externalOrderId`, use the following approach for cross-platform compatibility:

```bash
# Generate millisecond timestamp (works on macOS, Linux, BSD)
TIMESTAMP=$(($(date +%s) * 1000))

# Generate unique order ID
ORDER_ID="order$(date +%s)"
```

**DO NOT USE** `date +%s%3N` or `date +%s000` as these are not portable:
- `date +%s%3N` doesn't work on macOS (outputs literal 'N')
- `date +%s000` just appends '000' without actual millisecond precision

### Order ID Format

The `externalOrderId` must be a valid string without special characters. Recommended formats:
- `order1773744500` (simple numeric suffix)
- `order_1773744500` (with underscore separator)
- `txn-abc123` (custom prefix with alphanumeric)

**Avoid**: `order_${TIMESTAMP}` where TIMESTAMP contains shell variable syntax errors

### Example Pre-order Request

```bash
# Correct way to create a pre-order
TIMESTAMP=$(($(date +%s) * 1000))
ORDER_ID="order$(date +%s)"

bash /path/to/scripts/sign_and_call.sh \
  "https://api.commonservice.io" \
  "papi/v1/ramp/connect/gray/buy/pre-order" \
  "connect-gray" \
  "your-api-key" \
  "/path/to/private.pem" \
  "{\"externalOrderId\":\"$ORDER_ID\",\"merchantCode\":\"connect-gray\",\"merchantName\":\"YourMerchant\",\"ts\":$TIMESTAMP,\"fiatCurrency\":\"USD\",\"requestedAmount\":100,\"cryptoCurrency\":\"BNB\",\"amountType\":1,\"address\":\"0x...\",\"network\":\"BSC\",\"payMethodCode\":\"BUY_CARD\"}"
```
```

## File: `skills/binance/onchain-pay/references/authentication.md`
```markdown
# Binance Onchain-Pay Open API Authentication

## Signing Process

All Onchain-Pay Open API requests use **RSA SHA256** signature with a PEM private key.

### Step 1: Build the Signing Payload

```
payload = JSON_BODY + TIMESTAMP
```

- `JSON_BODY`: The raw JSON request body string (compact, no trailing newline). If no body is needed, use empty string.
- `TIMESTAMP`: Current Unix timestamp in **milliseconds** (e.g., `1709654400000`)

Example:
```
{"fiatCurrency":"USD","cryptoCurrency":"BTC","totalAmount":100,"amountType":1}1709654400000
```

### Step 2: Sign with RSA SHA256

```bash
signature=$(echo -n "$payload" \
  | openssl dgst -sha256 -sign "$PRIVATE_KEY_PATH" \
  | openssl enc -base64 -A)
```

- Uses the RSA private key in PEM format
- SHA256 digest
- Base64 encoded (single line, no wrapping)

### Step 3: Send Request with Headers

All requests are **POST** with these headers:

| Header | Value |
|--------|-------|
| `X-Tesla-ClientId` | Your client ID (e.g., `your-client-id`) |
| `X-Tesla-SignAccessToken` | Your API key |
| `X-Tesla-Signature` | The RSA signature from Step 2 |
| `X-Tesla-Timestamp` | The timestamp used in signing |
| `Content-Type` | `application/json` |
| `x-trace-id` | (Optional) Trace ID for debugging |

### Complete Example

```bash
# Generate timestamp in milliseconds (cross-platform compatible)
timestamp=$(($(date +%s) * 1000))
api_params='{"fiatCurrency":"USD","cryptoCurrency":"BTC","totalAmount":100,"amountType":1}'
payload="${api_params}${timestamp}"

signature=$(echo -n "$payload" \
  | openssl dgst -sha256 -sign "test.pem" \
  | openssl enc -base64 -A)

curl --location --request POST "https://api.commonservice.io/papi/v1/ramp/connect/buy/payment-method-list" \
  --header "X-Tesla-ClientId: your-client-id" \
  --header "X-Tesla-SignAccessToken: your-api-key" \
  --header "X-Tesla-Signature: $signature" \
  --header "X-Tesla-Timestamp: $timestamp" \
  --header "Content-Type: application/json" \
  --data-raw "$api_params"
```

### Important: Cross-platform Timestamp Generation

**Correct (works on macOS, Linux, BSD):**
```bash
timestamp=$(($(date +%s) * 1000))
```

**Incorrect (do not use):**
```bash
# ❌ Doesn't work on macOS - outputs literal 'N'
timestamp=$(date +%s%3N)

# ❌ Just appends '000', not true milliseconds
timestamp=$(date +%s000)
```

On macOS, `date` doesn't support `%N` (nanoseconds), which causes `date +%s%3N` to output something like `1773744478N`. This breaks JSON parsing with error:
```
Unexpected character ('N' (code 78)): was expecting comma to separate Object entries
```

## Security Notes

- Never expose the PEM private key content
- Never display the full API key; show first 5 + last 4 characters only (e.g., `2zefb...06h`)
- The PEM file path should be absolute or relative to the working directory
```

## File: `skills/binance/onchain-pay/scripts/sign_and_call.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

# Binance Onchain-Pay Open API - Sign & Call
# Usage: sign_and_call.sh <base_url> <api_path> <client_id> <api_key> <pem_path> <json_body>
#
# Example:
#   sign_and_call.sh "https://api.commonservice.io" \
#     "papi/v1/ramp/connect/buy/payment-method-list" \
#     "your-client-id" \
#     "your-api-key" \
#     "/path/to/private.pem" \
#     '{"fiatCurrency":"USD","cryptoCurrency":"BTC","totalAmount":100,"amountType":1}'

BASE_URL="$1"
API_PATH="$2"
CLIENT_ID="$3"
API_KEY="$4"
PEM_PATH="$5"
JSON_BODY="${6:-}"

# Generate timestamp (milliseconds) - cross-platform compatible
# Using arithmetic expansion works on macOS, Linux, and BSD
timestamp=$(($(date +%s) * 1000))

# Build signing payload: JSON body + timestamp
payload="${JSON_BODY}${timestamp}"

# RSA SHA256 sign with PEM private key, base64 encode
signature=$(echo -n "$payload" \
  | openssl dgst -sha256 -sign "$PEM_PATH" \
  | openssl enc -base64 -A)

# Build curl command
curl_args=(
  --silent
  --location
  --request POST "${BASE_URL}/${API_PATH}"
  --header "X-Tesla-ClientId: ${CLIENT_ID}"
  --header "X-Tesla-SignAccessToken: ${API_KEY}"
  --header "X-Tesla-Signature: ${signature}"
  --header "X-Tesla-Timestamp: ${timestamp}"
  --header "Content-Type: application/json"
  --header "x-trace-id: skill_${timestamp}"
  --header "User-Agent: onchain-pay-open-api/0.1.0 (Skill)"
)

if [ -n "$JSON_BODY" ]; then
  curl_args+=(--data-raw "$JSON_BODY")
fi

curl "${curl_args[@]}" | python3 -m json.tool 2>/dev/null || curl "${curl_args[@]}"
```

## File: `skills/binance/p2p/CHANGELOG.md`
```markdown
# Changelog

## 1.0.1 - 2026-03-25

- Changed: Update order placement link format from filtered list page to ad-specific detail page using `adNo` parameter (`https://c2c.binance.com/en/adv?code={adNo}`)

## 1.0.0 - 2026-03-24

- Initial release
```

## File: `skills/binance/p2p/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/p2p/SKILL.md`
```markdown
---
name: p2p
description: |
  Binance P2P trading assistant for natural-language queries about P2P/C2C market ads and (optionally) the user’s own P2P order history.

  Use when the user asks about P2P prices, searching/choosing ads, comparing payment methods, or reviewing their P2P order history (requires API key).

  Do NOT use for spot/futures prices, exchange trading, deposits/withdrawals, on-chain transfers, or anything unrelated to P2P/C2C.
---

# Binance P2P Trading Skill

Help users interact with **Binance P2P (C2C)** via natural-language queries.

## When to Use / When NOT to Use

### Use this skill when the user wants to:
- Check **P2P** buy/sell quotes for a crypto/fiat pair (e.g., USDT/CNY).
- Search **P2P advertisements** and filter by payment method(s), limits, merchant quality.
- Compare prices across payment methods (e.g., Alipay vs bank transfer).
- View **their own P2P order history / summary** (requires API key).

### Do NOT use this skill when the user asks about:
- Spot/Convert prices, futures/derivatives, margin, trading bots.
- Deposits/withdrawals, wallet transfers, on-chain transactions.
- Creating/cancelling orders, appeals, releasing coins (trading operations).

### Ask clarifying questions (do not guess) if any key inputs are missing:
- `fiat` (e.g., CNY)
- `asset` (e.g., USDT)
- user intent: **buy crypto** or **sell crypto**
- preferred payment method(s)
- target amount (optional but recommended for ad filtering)

## Core Concepts

### `tradeType` mapping (avoid ambiguity)
- User wants to **buy crypto** (pay fiat, receive USDT/BTC) → `tradeType=BUY`
- User wants to **sell crypto** (receive fiat, pay USDT/BTC) → `tradeType=SELL`

Always reflect this mapping in responses when the user’s wording is ambiguous.

## Capabilities

### Phase 1 — Public Market (No Auth)
- Quote P2P prices
- Search ads
- Compare payment methods
- Filter/Rank ads by limits and merchant indicators

### Phase 2 — Personal Orders (Requires API Key)
- List P2P order history
- Filter by trade type / time range
- Provide summary statistics

## Security & Privacy Rules

### Credentials
- Required env vars:
    - `BINANCE_API_KEY` (sent as header)
    - `BINANCE_SECRET_KEY` (used for signing)

### Never display full secrets
- API Key: show **first 5 + last 4** characters: `abc12...z789`
- Secret Key: always mask; show **only last 5**: `***...c123`

### Permission minimization
- Binance API permissions: **Enable Reading** only.
- Do NOT request/encourage trading, withdrawal, or modification permissions.

### Storage guidance
- Prefer environment injection (session/runtime env vars) over writing to disk.
- Only write to `.env` if the user explicitly agrees.
- Ensure `.env` is in `.gitignore` before saving.

## ⚠️ CRITICAL: SAPI Signing (Different from Standard Binance API)

### Parameter ordering
- **DO NOT sort parameters** for SAPI requests.
- Keep original insertion order when building the query string.

Example:
```py
# ✅ Correct for SAPI: keep insertion order
params = {"page": 1, "rows": 20, "timestamp": 1710460800000}
query_string = urlencode(params)  # NO sorting

# ❌ Wrong (standard Binance API only): sorted
query_string = urlencode(sorted(params.items()))
```

### Signing details
See: `references/authentication.md` for:
- RFC 3986 percent-encoding
- HMAC SHA256 signing process
- Required headers (incl. User-Agent)
- SAPI-specific parameter ordering

## API Overview

### Public Queries (MGS C2C Agent API — No Auth)
Base URL: `https://www.binance.com`

| Endpoint | Method | Params | Usage |
|----------|--------|--------|-------|
| `/bapi/c2c/v1/public/c2c/agent/quote-price` | GET | fiat, asset, tradeType | Quick price quote |
| `/bapi/c2c/v1/public/c2c/agent/ad-list` | GET | fiat, asset, tradeType, limit, order, tradeMethodIdentifiers | Search ads |
| `/bapi/c2c/v1/public/c2c/agent/trade-methods` | GET | fiat | Payment methods |

Parameter notes:
- `tradeType`: `BUY` or `SELL` (treat as case-insensitive)
- `limit`: 1–20 (default 10)
- `tradeMethodIdentifiers`: pass as a **plain string** (not JSON array) — e.g. `tradeMethodIdentifiers=BANK` or `tradeMethodIdentifiers=WECHAT`. Values **must** use the `identifier` field returned by the `trade-methods` endpoint (see workflow below). ⚠️ Do NOT use JSON array syntax like `["BANK"]` — it will return empty results.

### Workflow: Compare Prices by Payment Method

When the user wants to compare prices across payment methods (e.g., "Alipay vs WeChat"), follow this two-step flow:

**Step 1** — Call `trade-methods` to get the correct identifiers for the target fiat:
```
GET /bapi/c2c/v1/public/c2c/agent/trade-methods?fiat=CNY
→ [{"identifier":"ALIPAY",...}, {"identifier":"WECHAT",...}, {"identifier":"BANK",...}]
```

**Step 2** — Pass the identifier as a plain string into `ad-list` via `tradeMethodIdentifiers`, one payment method per request, then compare:
```
GET /bapi/c2c/v1/public/c2c/agent/ad-list?fiat=CNY&asset=USDT&tradeType=BUY&limit=5&tradeMethodIdentifiers=ALIPAY&tradeMethodIdentifiers=WECHAT
```
Compare the best price from each result set.

> **Important:** Do not hardcode identifier values like `"Alipay"` or `"BANK"`. Always call `trade-methods` first to get the exact `identifier` strings for the given fiat currency.

### Personal Orders (Binance SAPI — Requires Auth)
Base URL: `https://api.binance.com`

| Endpoint | Method | Auth | Usage |
|----------|--------|------|-------|
| `/sapi/v1/c2c/orderMatch/listUserOrderHistory` | GET | Yes | Order history |
| `/sapi/v1/c2c/orderMatch/getUserOrderSummary` | GET | Yes | User statistics |

Authentication requirements:
- Header: `X-MBX-APIKEY`
- Query: `timestamp` + `signature`
- Header: `User-Agent: binance-wallet/1.0.0 (Skill)`

## Output Format Guidelines

### Price quote
- Show both sides when available (best buy / best sell).
- Use fiat symbol and 2-decimal formatting.

Example:
```
USDT/CNY (P2P)
- Buy USDT (you buy crypto): ¥7.20
- Sell USDT (you sell crypto): ¥7.18
```

### Ad list
Return **Top N** items with a stable schema:
1) adNo (ad number / identifier)
2) price (fiat)
3) merchant name
4) completion rate
5) limits
6) payment methods (identifiers)

Avoid generating parameterized external URLs unless the API returns them.

**Placing orders (when user requests):**
- This skill does NOT support automated order placement.
- When user wants to place an order, provide a direct link to the specific ad using the adNo:
  ```
  https://c2c.binance.com/en/adv?code={adNo}
  ```
    - `{adNo}`: the ad number/identifier from the ad list result

  Example: `https://c2c.binance.com/en/adv?code=123`
- This opens the specific ad detail page where user can place order directly with the selected advertisement.

### Personal orders
- Time format: `YYYY-MM-DD HH:mm (UTC+0)` — always display in UTC timezone
- Include: type, vault/assets/fiat, amount, total, status
- Provide a brief summary line (count + totals) when filtering

**Time field conversion (for `createTime` in `listUserOrderHistory`):**
- The `createTime` field returns a Unix timestamp in **milliseconds** (13 digits).
- Convert to human-readable format in **UTC+0 timezone**:
  ```
  # Python example
  from datetime import datetime, timezone
  readable_time = datetime.fromtimestamp(createTime / 1000, tz=timezone.utc).strftime('%Y-%m-%d %H:%M (UTC+0)')
  
  # JavaScript example
  const readableTime = new Date(createTime).toISOString().replace('T', ' ').slice(0, 16) + ' (UTC+0)';
  // Or more explicitly:
  const date = new Date(createTime);
  const readableTime = date.getUTCFullYear() + '-' +
    String(date.getUTCMonth() + 1).padStart(2, '0') + '-' +
    String(date.getUTCDate()).padStart(2, '0') + ' ' +
    String(date.getUTCHours()).padStart(2, '0') + ':' +
    String(date.getUTCMinutes()).padStart(2, '0') + ' (UTC+0)';
  ```
- Always display the converted time to users with timezone info, not the raw timestamp.

## Error Handling (User-Facing)

- Invalid API key (-2015): prompt to verify `.env` / API Management.
- Signature failed (-1022): warn about wrong secret, sorted params, or stale timestamp.
- Timestamp invalid (-1021): advise time sync / regenerate timestamp.
- Rate limit: ask to retry later.

## Limitations (By Design)

This skill does NOT:
- Place/cancel orders
- Mark as paid / release coins
- Submit appeals
- Post/modify advertisements
- Expose sensitive order-detail endpoints beyond what’s needed for history/summary

For in-app actions, guide users to the official P2P orders page (only as a general entry point).

## Developer Notes

### Version Check (First Invocation per Conversation)
On the first invocation of this skill per conversation, call:

- `GET /bapi/c2c/v1/public/c2c/agent/check-version?version=1.0.1` (Base: `https://www.binance.com`)

Behavior:
- If `needUpdate=true`: show: `New version of P2P Skill is available (current: {clientVersion}, latest: {latestVersion}), update recommended.`
- Else / on failure: proceed silently.

### Client-side operations
- Asset filtering: if API doesn’t support it, fetch then filter locally.
- Aggregations: compute totals client-side when summary endpoint is insufficient.
```

## File: `skills/binance/p2p/references/authentication.md`
```markdown
# Binance P2P Authentication

All P2P personal order endpoints (SAPI) require HMAC SHA256 signed requests.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://api.binance.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-wallet/1.0.0 (Skill)

## ⚠️ CRITICAL: SAPI-Specific Behavior

**DO NOT sort parameters** - SAPI keeps original insertion order (different from standard Binance API).

**Correct approach for SAPI:**
- Keep parameter insertion order when building query string
- Example: `page=1&rows=20&recvWindow=60000&timestamp=1710460800000`

**Wrong approach (standard Binance API only):**
- Sorting parameters alphabetically will cause signature verification failure
- SAPI does NOT sort parameters like standard REST API

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 60000ms for P2P endpoints) for timestamp tolerance.

### Step 2: Percent-Encode Parameters

Before generating the signature, **percent-encode all parameter names and values using UTF-8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
  `symbol=这是测试币456`

Percent-encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the HMAC SHA256 signature from the encoded query string using your secret key:

```bash
# Example using openssl
echo -n "page=1&rows=20&recvWindow=60000&timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

### Step 4: Append Signature

Add signature parameter to the query string:
`page=1&rows=20&recvWindow=60000&timestamp=1234567890123&signature=abc123...`

### Step 5: Add Headers

Include required headers:
- `X-MBX-APIKEY`: Your API key
- `User-Agent`: `binance-wallet/1.0.0 (Skill)`

## Complete Bash Example

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://api.binance.com"

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
# CRITICAL: Keep parameter order, do NOT sort
QUERY="page=1&rows=20&recvWindow=60000&timestamp=${TIMESTAMP}"

# Generate signature
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# Make request
curl -X GET "${BASE_URL}/sapi/v1/c2c/orderMatch/listUserOrderHistory?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}" \
  -H "User-Agent: binance-wallet/1.0.0 (Skill)"
```

## Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (Enable Reading for P2P order history)
* Store credentials securely in .env file (add to .gitignore)
```

## File: `skills/binance/simple-earn/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-20

- Initial release
```

## File: `skills/binance/simple-earn/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/simple-earn/SKILL.md`
```markdown
---
name: simple-earn
description: Binance Simple-earn request using the Binance API. Authentication requires API key and secret key. 
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/simple-earn/SKILL.md
license: MIT
---

# Binance Simple-earn Skill

Simple-earn request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/sapi/v1/bfusd/account` (GET) | Get BFUSD Account (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/bfusd/quota` (GET) | Get BFUSD Quota Details (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/bfusd/redeem` (POST) | Redeem BFUSD(TRADE) | amount, type | recvWindow | Yes |
| `/sapi/v1/bfusd/subscribe` (POST) | Subscribe BFUSD(TRADE) | asset, amount | recvWindow | Yes |
| `/sapi/v1/bfusd/history/rateHistory` (GET) | Get BFUSD Rate History (USER_DATA) | None | startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/bfusd/history/redemptionHistory` (GET) | Get BFUSD Redemption History (USER_DATA) | None | startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/bfusd/history/rewardsHistory` (GET) | Get BFUSD Rewards History (USER_DATA) | None | startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/bfusd/history/subscriptionHistory` (GET) | Get BFUSD subscription history(USER_DATA) | None | asset, startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/simple-earn/flexible/personalLeftQuota` (GET) | Get Flexible Personal Left Quota(USER_DATA) | productId | recvWindow | Yes |
| `/sapi/v1/simple-earn/flexible/position` (GET) | Get Flexible Product Position(USER_DATA) | None | asset, productId, current, size, recvWindow | Yes |
| `/sapi/v1/simple-earn/locked/personalLeftQuota` (GET) | Get Locked Personal Left Quota(USER_DATA) | projectId | recvWindow | Yes |
| `/sapi/v1/simple-earn/locked/position` (GET) | Get Locked Product Position | None | asset, positionId, projectId, current, size, recvWindow | Yes |
| `/sapi/v1/simple-earn/flexible/list` (GET) | Get Simple Earn Flexible Product List(USER_DATA) | None | asset, current, size, recvWindow | Yes |
| `/sapi/v1/simple-earn/locked/list` (GET) | Get Simple Earn Locked Product List(USER_DATA) | None | asset, current, size, recvWindow | Yes |
| `/sapi/v1/simple-earn/account` (GET) | Simple Account(USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/simple-earn/flexible/subscriptionPreview` (GET) | Get Flexible Subscription Preview(USER_DATA) | productId, amount | recvWindow | Yes |
| `/sapi/v1/simple-earn/locked/subscriptionPreview` (GET) | Get Locked Subscription Preview(USER_DATA) | projectId, amount | autoSubscribe, recvWindow | Yes |
| `/sapi/v1/simple-earn/flexible/redeem` (POST) | Redeem Flexible Product(TRADE) | productId | redeemAll, amount, destAccount, recvWindow | Yes |
| `/sapi/v1/simple-earn/locked/redeem` (POST) | Redeem Locked Product(TRADE) | positionId | recvWindow | Yes |
| `/sapi/v1/simple-earn/flexible/setAutoSubscribe` (POST) | Set Flexible Auto Subscribe(USER_DATA) | productId, autoSubscribe | recvWindow | Yes |
| `/sapi/v1/simple-earn/locked/setAutoSubscribe` (POST) | Set Locked Auto Subscribe(USER_DATA) | positionId, autoSubscribe | recvWindow | Yes |
| `/sapi/v1/simple-earn/locked/setRedeemOption` (POST) | Set Locked Product Redeem Option(USER_DATA) | positionId, redeemTo | recvWindow | Yes |
| `/sapi/v1/simple-earn/flexible/subscribe` (POST) | Subscribe Flexible Product(TRADE) | productId, amount | autoSubscribe, sourceAccount, recvWindow | Yes |
| `/sapi/v1/simple-earn/locked/subscribe` (POST) | Subscribe Locked Product(TRADE) | projectId, amount | autoSubscribe, sourceAccount, redeemTo, recvWindow | Yes |
| `/sapi/v1/simple-earn/flexible/history/collateralRecord` (GET) | Get Collateral Record(USER_DATA) | None | productId, startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/simple-earn/flexible/history/redemptionRecord` (GET) | Get Flexible Redemption Record(USER_DATA) | None | productId, redeemId, asset, startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/simple-earn/flexible/history/rewardsRecord` (GET) | Get Flexible Rewards History(USER_DATA) | type | productId, asset, startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/simple-earn/flexible/history/subscriptionRecord` (GET) | Get Flexible Subscription Record(USER_DATA) | None | productId, purchaseId, asset, startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/simple-earn/locked/history/redemptionRecord` (GET) | Get Locked Redemption Record(USER_DATA) | None | positionId, redeemId, asset, startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/simple-earn/locked/history/rewardsRecord` (GET) | Get Locked Rewards History(USER_DATA) | None | positionId, asset, startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/simple-earn/locked/history/subscriptionRecord` (GET) | Get Locked Subscription Record(USER_DATA) | None | purchaseId, asset, startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/simple-earn/flexible/history/rateHistory` (GET) | Get Rate History(USER_DATA) | productId | aprPeriod, startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/rwusd/quota` (GET) | Get RWUSD Quota Details (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/rwusd/account` (GET) | Get RWUSD Account (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/rwusd/redeem` (POST) | Redeem RWUSD(TRADE) | amount, type | recvWindow | Yes |
| `/sapi/v1/rwusd/subscribe` (POST) | Subscribe RWUSD(TRADE) | asset, amount | recvWindow | Yes |
| `/sapi/v1/rwusd/history/rateHistory` (GET) | Get RWUSD Rate History (USER_DATA) | None | startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/rwusd/history/redemptionHistory` (GET) | Get RWUSD Redemption History (USER_DATA) | None | startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/rwusd/history/rewardsHistory` (GET) | Get RWUSD Rewards History (USER_DATA) | None | startTime, endTime, current, size, recvWindow | Yes |
| `/sapi/v1/rwusd/history/subscriptionHistory` (GET) | Get RWUSD subscription history(USER_DATA) | None | asset, startTime, endTime, current, size, recvWindow | Yes |

---

## Parameters

### Common Parameters

* **recvWindow**: The value cannot be greater than 60000 (ms) (e.g., 5000)
* **amount**: Amount (e.g., 1.0)
* **type**: FAST or STANDARD, defaults to STANDARD (e.g., s)
* **asset**: USDT or USDC (whichever is eligible)
* **startTime**:  (e.g., 1623319461670)
* **endTime**:  (e.g., 1641782889000)
* **current**: Currently querying page. Starts from 1. Default: 1 (e.g., 1)
* **size**: Number of results per page. Default: 10, Max: 100 (e.g., 10)
* **asset**: USDC or USDT
* **productId**:  (e.g., 1)
* **productId**:  (e.g., 1)
* **projectId**:  (e.g., 1)
* **positionId**:  (e.g., 1)
* **projectId**:  (e.g., 1)
* **autoSubscribe**: true or false, default true. (e.g., true)
* **redeemAll**: true or false, default to false
* **amount**: if redeemAll is false, amount is mandatory (e.g., 1.0)
* **destAccount**: `SPOT`,`FUND`, default `SPOT` (e.g., SPOT)
* **positionId**:  (e.g., 1)
* **autoSubscribe**: true or false
* **redeemTo**: `SPOT`,'FLEXIBLE'
* **sourceAccount**: `SPOT`,`FUND`,`ALL`, default `SPOT` (e.g., SPOT)
* **redeemTo**: `SPOT`,`FLEXIBLE`, default `SPOT` (e.g., SPOT)
* **redeemId**:  (e.g., 1)
* **purchaseId**:  (e.g., 1)
* **aprPeriod**: "DAY","YEAR",default"DAY" (e.g., DAY)


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://api.binance.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Description: Primary trading account


### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## User Agent Header

Include `User-Agent` header with the following string: `binance-simple-earn/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/simple-earn/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://api.binance.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-simple-earn/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-simple-earn/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X GET "https://api.binance.com/sapi/v1/bfusd/account" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-simple-earn/1.1.0 (Skill)" \
  -d "timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://api.binance.com"  

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X GET "${BASE_URL}/sapi/v1/bfusd/account?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-simple-earn/1.1.0 (Skill)"
```

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
```

## File: `skills/binance/spot/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-23

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.2 - 2026-03-10

- Add `New Client Order ID` rule

## 1.0.1 - 2026-03-04

- Add demo url option
- Add User Agent header

## 1.0.0 - 2026-03-03

- Initial release
```

## File: `skills/binance/spot/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/spot/SKILL.md`
```markdown
---
name: spot
description: Binance Spot request using the Binance API. Authentication requires API key and secret key. Supports testnet, mainnet, and demo.
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    skillKey: binance-spot
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/spot/SKILL.md
license: MIT
---

# Binance Spot Skill

Spot request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/api/v3/exchangeInfo` (GET) | Exchange information | None | symbol, symbols, permissions, showPermissionSets, symbolStatus | No |
| `/api/v3/ping` (GET) | Test connectivity | None | None | No |
| `/api/v3/time` (GET) | Check server time | None | None | No |
| `/api/v3/aggTrades` (GET) | Compressed/Aggregate trades list | symbol | fromId, startTime, endTime, limit | No |
| `/api/v3/avgPrice` (GET) | Current average price | symbol | None | No |
| `/api/v3/depth` (GET) | Order book | symbol | limit, symbolStatus | No |
| `/api/v3/historicalTrades` (GET) | Old trade lookup | symbol | limit, fromId | No |
| `/api/v3/klines` (GET) | Kline/Candlestick data | symbol, interval | startTime, endTime, timeZone, limit | No |
| `/api/v3/ticker` (GET) | Rolling window price change statistics | None | symbol, symbols, windowSize, type, symbolStatus | No |
| `/api/v3/ticker/24hr` (GET) | 24hr ticker price change statistics | None | symbol, symbols, type, symbolStatus | No |
| `/api/v3/ticker/bookTicker` (GET) | Symbol order book ticker | None | symbol, symbols, symbolStatus | No |
| `/api/v3/ticker/price` (GET) | Symbol price ticker | None | symbol, symbols, symbolStatus | No |
| `/api/v3/ticker/tradingDay` (GET) | Trading Day Ticker | None | symbol, symbols, timeZone, type, symbolStatus | No |
| `/api/v3/trades` (GET) | Recent trades list | symbol | limit | No |
| `/api/v3/uiKlines` (GET) | UIKlines | symbol, interval | startTime, endTime, timeZone, limit | No |
| `/api/v3/openOrders` (DELETE) | Cancel All Open Orders on a Symbol | symbol | recvWindow | Yes |
| `/api/v3/openOrders` (GET) | Current open orders | None | symbol, recvWindow | Yes |
| `/api/v3/order` (POST) | New order | symbol, side, type | timeInForce, quantity, quoteOrderQty, price, newClientOrderId, strategyId, strategyType, stopPrice, trailingDelta, icebergQty, newOrderRespType, selfTradePreventionMode, pegPriceType, pegOffsetValue, pegOffsetType, recvWindow | Yes |
| `/api/v3/order` (DELETE) | Cancel order | symbol | orderId, origClientOrderId, newClientOrderId, cancelRestrictions, recvWindow | Yes |
| `/api/v3/order` (GET) | Query order | symbol | orderId, origClientOrderId, recvWindow | Yes |
| `/api/v3/order/amend/keepPriority` (PUT) | Order Amend Keep Priority | symbol, newQty | orderId, origClientOrderId, newClientOrderId, recvWindow | Yes |
| `/api/v3/order/cancelReplace` (POST) | Cancel an Existing Order and Send a New Order | symbol, side, type, cancelReplaceMode | timeInForce, quantity, quoteOrderQty, price, cancelNewClientOrderId, cancelOrigClientOrderId, cancelOrderId, newClientOrderId, strategyId, strategyType, stopPrice, trailingDelta, icebergQty, newOrderRespType, selfTradePreventionMode, cancelRestrictions, orderRateLimitExceededMode, pegPriceType, pegOffsetValue, pegOffsetType, recvWindow | Yes |
| `/api/v3/order/oco` (POST) | New OCO - Deprecated | symbol, side, quantity, price, stopPrice | listClientOrderId, limitClientOrderId, limitStrategyId, limitStrategyType, limitIcebergQty, trailingDelta, stopClientOrderId, stopStrategyId, stopStrategyType, stopLimitPrice, stopIcebergQty, stopLimitTimeInForce, newOrderRespType, selfTradePreventionMode, recvWindow | Yes |
| `/api/v3/order/test` (POST) | Test new order | symbol, side, type | computeCommissionRates, timeInForce, quantity, quoteOrderQty, price, newClientOrderId, strategyId, strategyType, stopPrice, trailingDelta, icebergQty, newOrderRespType, selfTradePreventionMode, pegPriceType, pegOffsetValue, pegOffsetType, recvWindow | Yes |
| `/api/v3/orderList` (DELETE) | Cancel Order list | symbol | orderListId, listClientOrderId, newClientOrderId, recvWindow | Yes |
| `/api/v3/orderList` (GET) | Query Order list | None | orderListId, origClientOrderId, recvWindow | Yes |
| `/api/v3/orderList/oco` (POST) | New Order list - OCO | symbol, side, quantity, aboveType, belowType | listClientOrderId, aboveClientOrderId, aboveIcebergQty, abovePrice, aboveStopPrice, aboveTrailingDelta, aboveTimeInForce, aboveStrategyId, aboveStrategyType, abovePegPriceType, abovePegOffsetType, abovePegOffsetValue, belowClientOrderId, belowIcebergQty, belowPrice, belowStopPrice, belowTrailingDelta, belowTimeInForce, belowStrategyId, belowStrategyType, belowPegPriceType, belowPegOffsetType, belowPegOffsetValue, newOrderRespType, selfTradePreventionMode, recvWindow | Yes |
| `/api/v3/orderList/opo` (POST) | New Order List - OPO | symbol, workingType, workingSide, workingPrice, workingQuantity, pendingType, pendingSide | listClientOrderId, newOrderRespType, selfTradePreventionMode, workingClientOrderId, workingIcebergQty, workingTimeInForce, workingStrategyId, workingStrategyType, workingPegPriceType, workingPegOffsetType, workingPegOffsetValue, pendingClientOrderId, pendingPrice, pendingStopPrice, pendingTrailingDelta, pendingIcebergQty, pendingTimeInForce, pendingStrategyId, pendingStrategyType, pendingPegPriceType, pendingPegOffsetType, pendingPegOffsetValue, recvWindow | Yes |
| `/api/v3/orderList/opoco` (POST) | New Order List - OPOCO | symbol, workingType, workingSide, workingPrice, workingQuantity, pendingSide, pendingAboveType | listClientOrderId, newOrderRespType, selfTradePreventionMode, workingClientOrderId, workingIcebergQty, workingTimeInForce, workingStrategyId, workingStrategyType, workingPegPriceType, workingPegOffsetType, workingPegOffsetValue, pendingAboveClientOrderId, pendingAbovePrice, pendingAboveStopPrice, pendingAboveTrailingDelta, pendingAboveIcebergQty, pendingAboveTimeInForce, pendingAboveStrategyId, pendingAboveStrategyType, pendingAbovePegPriceType, pendingAbovePegOffsetType, pendingAbovePegOffsetValue, pendingBelowType, pendingBelowClientOrderId, pendingBelowPrice, pendingBelowStopPrice, pendingBelowTrailingDelta, pendingBelowIcebergQty, pendingBelowTimeInForce, pendingBelowStrategyId, pendingBelowStrategyType, pendingBelowPegPriceType, pendingBelowPegOffsetType, pendingBelowPegOffsetValue, recvWindow | Yes |
| `/api/v3/orderList/oto` (POST) | New Order list - OTO | symbol, workingType, workingSide, workingPrice, workingQuantity, pendingType, pendingSide, pendingQuantity | listClientOrderId, newOrderRespType, selfTradePreventionMode, workingClientOrderId, workingIcebergQty, workingTimeInForce, workingStrategyId, workingStrategyType, workingPegPriceType, workingPegOffsetType, workingPegOffsetValue, pendingClientOrderId, pendingPrice, pendingStopPrice, pendingTrailingDelta, pendingIcebergQty, pendingTimeInForce, pendingStrategyId, pendingStrategyType, pendingPegPriceType, pendingPegOffsetType, pendingPegOffsetValue, recvWindow | Yes |
| `/api/v3/orderList/otoco` (POST) | New Order list - OTOCO | symbol, workingType, workingSide, workingPrice, workingQuantity, pendingSide, pendingQuantity, pendingAboveType | listClientOrderId, newOrderRespType, selfTradePreventionMode, workingClientOrderId, workingIcebergQty, workingTimeInForce, workingStrategyId, workingStrategyType, workingPegPriceType, workingPegOffsetType, workingPegOffsetValue, pendingAboveClientOrderId, pendingAbovePrice, pendingAboveStopPrice, pendingAboveTrailingDelta, pendingAboveIcebergQty, pendingAboveTimeInForce, pendingAboveStrategyId, pendingAboveStrategyType, pendingAbovePegPriceType, pendingAbovePegOffsetType, pendingAbovePegOffsetValue, pendingBelowType, pendingBelowClientOrderId, pendingBelowPrice, pendingBelowStopPrice, pendingBelowTrailingDelta, pendingBelowIcebergQty, pendingBelowTimeInForce, pendingBelowStrategyId, pendingBelowStrategyType, pendingBelowPegPriceType, pendingBelowPegOffsetType, pendingBelowPegOffsetValue, recvWindow | Yes |
| `/api/v3/sor/order` (POST) | New order using SOR | symbol, side, type, quantity | timeInForce, price, newClientOrderId, strategyId, strategyType, icebergQty, newOrderRespType, selfTradePreventionMode, recvWindow | Yes |
| `/api/v3/sor/order/test` (POST) | Test new order using SOR | symbol, side, type, quantity | computeCommissionRates, timeInForce, price, newClientOrderId, strategyId, strategyType, icebergQty, newOrderRespType, selfTradePreventionMode, recvWindow | Yes |
| `/api/v3/account` (GET) | Account information | None | omitZeroBalances, recvWindow | Yes |
| `/api/v3/account/commission` (GET) | Query Commission Rates | symbol | None | Yes |
| `/api/v3/allOrderList` (GET) | Query all Order lists | None | fromId, startTime, endTime, limit, recvWindow | Yes |
| `/api/v3/allOrders` (GET) | All orders | symbol | orderId, startTime, endTime, limit, recvWindow | Yes |
| `/api/v3/myAllocations` (GET) | Query Allocations | symbol | startTime, endTime, fromAllocationId, limit, orderId, recvWindow | Yes |
| `/api/v3/myFilters` (GET) | Query relevant filters | symbol | recvWindow | Yes |
| `/api/v3/myPreventedMatches` (GET) | Query Prevented Matches | symbol | preventedMatchId, orderId, fromPreventedMatchId, limit, recvWindow | Yes |
| `/api/v3/myTrades` (GET) | Account trade list | symbol | orderId, startTime, endTime, fromId, limit, recvWindow | Yes |
| `/api/v3/openOrderList` (GET) | Query Open Order lists | None | recvWindow | Yes |
| `/api/v3/order/amendments` (GET) | Query Order Amendments | symbol, orderId | fromExecutionId, limit, recvWindow | Yes |
| `/api/v3/rateLimit/order` (GET) | Query Unfilled Order Count | None | recvWindow | Yes |

---

## Parameters

### Common Parameters

* **symbol**: Symbol to query (e.g., BNBUSDT)
* **symbols**: List of symbols to query
* **permissions**: List of permissions to query
* **showPermissionSets**: Controls whether the content of the `permissionSets` field is populated or not. Defaults to `true` (e.g., true)
* **symbol**:  (e.g., BNBUSDT)
* **fromId**: ID to get aggregate trades from INCLUSIVE. (e.g., 1)
* **startTime**: Timestamp in ms to get aggregate trades from INCLUSIVE. (e.g., 1735693200000)
* **endTime**: Timestamp in ms to get aggregate trades until INCLUSIVE. (e.g., 1735693200000)
* **limit**: Default: 500; Maximum: 1000. (e.g., 500)
* **timeZone**: Default: 0 (UTC)
* **recvWindow**: The value cannot be greater than `60000`.   Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified. (e.g., 5000)
* **timestamp**:  (e.g., 1)
* **quantity**:  (e.g., 1)
* **quoteOrderQty**:  (e.g., 1)
* **price**:  (e.g., 400)
* **newClientOrderId**: A unique id among open orders. Automatically generated if not sent.  Orders with the same `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be rejected.
* **strategyId**:  (e.g., 1)
* **strategyType**: The value cannot be less than `1000000`. (e.g., 1)
* **stopPrice**: Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders. (e.g., 1)
* **trailingDelta**: See Trailing Stop order FAQ. (e.g., 1)
* **icebergQty**: Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order. (e.g., 1)
* **pegOffsetValue**: Priceleveltopegthepriceto(max:100). SeePeggedOrdersInfo (e.g., 1)
* **orderId**:  (e.g., 1)
* **origClientOrderId**: 
* **newQty**: `newQty` must be greater than 0 and less than the order's quantity. (e.g., 1)
* **cancelNewClientOrderId**: Used to uniquely identify this cancel. Automatically generated by default.
* **cancelOrigClientOrderId**: Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent.  </br> If both `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then the `cancelOrigClientOrderId` from that result is checked against that order.  </br> If both conditions are not met the request will be rejected.
* **cancelOrderId**: Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent.  </br>If both `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then the `cancelOrigClientOrderId` from that result is checked against that order.  </br>If both conditions are not met the request will be rejected. (e.g., 1)
* **listClientOrderId**: A unique Id for the entire orderList
* **quantity**:  (e.g., 1)
* **limitClientOrderId**: A unique Id for the limit order
* **price**:  (e.g., 1)
* **limitStrategyId**:  (e.g., 1)
* **limitStrategyType**: The value cannot be less than `1000000`. (e.g., 1)
* **limitIcebergQty**: Used to make the `LIMIT_MAKER` leg an iceberg order. (e.g., 1)
* **stopClientOrderId**: A unique Id for the stop loss/stop loss limit leg
* **stopPrice**:  (e.g., 1)
* **stopStrategyId**:  (e.g., 1)
* **stopStrategyType**: The value cannot be less than `1000000`. (e.g., 1)
* **stopLimitPrice**: If provided, `stopLimitTimeInForce` is required. (e.g., 1)
* **stopIcebergQty**: Used with `STOP_LOSS_LIMIT` leg to make an iceberg order. (e.g., 1)
* **computeCommissionRates**: Default: `false`   See Commissions FAQ to learn more.
* **orderListId**: Either `orderListId` or `listClientOrderId` must be provided (e.g., 1)
* **aboveClientOrderId**: Arbitrary unique ID among open orders for the above order. Automatically generated if not sent
* **aboveIcebergQty**: Note that this can only be used if `aboveTimeInForce` is `GTC`. (e.g., 1)
* **abovePrice**: Can be used if `aboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price. (e.g., 1)
* **aboveStopPrice**: Can be used if `aboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`.  Either `aboveStopPrice` or `aboveTrailingDelta` or both, must be specified. (e.g., 1)
* **aboveTrailingDelta**: See Trailing Stop order FAQ. (e.g., 1)
* **aboveStrategyId**: Arbitrary numeric value identifying the above order within an order strategy. (e.g., 1)
* **aboveStrategyType**: Arbitrary numeric value identifying the above order strategy.  Values smaller than 1000000 are reserved and cannot be used. (e.g., 1)
* **abovePegOffsetValue**:  (e.g., 1)
* **belowClientOrderId**: Arbitrary unique ID among open orders for the below order. Automatically generated if not sent
* **belowIcebergQty**: Note that this can only be used if `belowTimeInForce` is `GTC`. (e.g., 1)
* **belowPrice**: Can be used if `belowType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price. (e.g., 1)
* **belowStopPrice**: Can be used if `belowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT, TAKE_PROFIT` or `TAKE_PROFIT_LIMIT`  Either belowStopPrice or belowTrailingDelta or both, must be specified. (e.g., 1)
* **belowTrailingDelta**: See Trailing Stop order FAQ. (e.g., 1)
* **belowStrategyId**: Arbitrary numeric value identifying the below order within an order strategy. (e.g., 1)
* **belowStrategyType**: Arbitrary numeric value identifying the below order strategy.  Values smaller than 1000000 are reserved and cannot be used. (e.g., 1)
* **belowPegOffsetValue**:  (e.g., 1)
* **workingClientOrderId**: Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.
* **workingPrice**:  (e.g., 1)
* **workingQuantity**: Sets the quantity for the working order. (e.g., 1)
* **workingIcebergQty**: This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`. (e.g., 1)
* **workingStrategyId**: Arbitrary numeric value identifying the working order within an order strategy. (e.g., 1)
* **workingStrategyType**: Arbitrary numeric value identifying the working order strategy. Values smaller than 1000000 are reserved and cannot be used. (e.g., 1)
* **workingPegOffsetValue**:  (e.g., 1)
* **pendingClientOrderId**: Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.
* **pendingPrice**:  (e.g., 1)
* **pendingStopPrice**:  (e.g., 1)
* **pendingTrailingDelta**:  (e.g., 1)
* **pendingIcebergQty**: This can only be used if `pendingTimeInForce` is `GTC` or if `pendingType` is `LIMIT_MAKER`. (e.g., 1)
* **pendingStrategyId**: Arbitrary numeric value identifying the pending order within an order strategy. (e.g., 1)
* **pendingStrategyType**: Arbitrary numeric value identifying the pending order strategy. Values smaller than 1000000 are reserved and cannot be used. (e.g., 1)
* **pendingPegOffsetValue**:  (e.g., 1)
* **pendingAboveClientOrderId**: Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent.
* **pendingAbovePrice**: Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price. (e.g., 1)
* **pendingAboveStopPrice**: Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` (e.g., 1)
* **pendingAboveTrailingDelta**: See Trailing Stop FAQ (e.g., 1)
* **pendingAboveIcebergQty**: This can only be used if `pendingAboveTimeInForce` is `GTC` or if `pendingAboveType` is `LIMIT_MAKER`. (e.g., 1)
* **pendingAboveStrategyId**: Arbitrary numeric value identifying the pending above order within an order strategy. (e.g., 1)
* **pendingAboveStrategyType**: Arbitrary numeric value identifying the pending above order strategy. Values smaller than 1000000 are reserved and cannot be used. (e.g., 1)
* **pendingAbovePegOffsetValue**:  (e.g., 1)
* **pendingBelowClientOrderId**: Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent.
* **pendingBelowPrice**: Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify limit price (e.g., 1)
* **pendingBelowStopPrice**: Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT, TAKE_PROFIT or TAKE_PROFIT_LIMIT`. Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be specified. (e.g., 1)
* **pendingBelowTrailingDelta**:  (e.g., 1)
* **pendingBelowIcebergQty**: This can only be used if `pendingBelowTimeInForce` is `GTC`, or if `pendingBelowType` is `LIMIT_MAKER`. (e.g., 1)
* **pendingBelowStrategyId**: Arbitrary numeric value identifying the pending below order within an order strategy. (e.g., 1)
* **pendingBelowStrategyType**: Arbitrary numeric value identifying the pending below order strategy. Values smaller than 1000000 are reserved and cannot be used. (e.g., 1)
* **pendingBelowPegOffsetValue**:  (e.g., 1)
* **pendingQuantity**: Sets the quantity for the pending order. (e.g., 1)
* **omitZeroBalances**: When set to `true`, emits only the non-zero balances of an account.  Default value: `false`
* **fromAllocationId**:  (e.g., 1)
* **timestamp**:  (e.g., 1)
* **preventedMatchId**:  (e.g., 1)
* **fromPreventedMatchId**:  (e.g., 1)
* **orderId**:  (e.g., 1)
* **fromExecutionId**:  (e.g., 1)
* **limit**: Default:500; Maximum: 1000 (e.g., 500)


### Enums

* **interval**: 1s | 1m | 3m | 5m | 15m | 30m | 1h | 2h | 4h | 6h | 8h | 12h | 1d | 3d | 1w | 1M
* **windowSize**: 1m | 2m | 3m | 4m | 5m | 6m | 7m | 8m | 9m | 10m | 11m | 12m | 13m | 14m | 15m | 16m | 17m | 18m | 19m | 20m | 21m | 22m | 23m | 24m | 25m | 26m | 27m | 28m | 29m | 30m | 31m | 32m | 33m | 34m | 35m | 36m | 37m | 38m | 39m | 40m | 41m | 42m | 43m | 44m | 45m | 46m | 47m | 48m | 49m | 50m | 51m | 52m | 53m | 54m | 55m | 56m | 57m | 58m | 59m | 1h | 2h | 3h | 4h | 5h | 6h | 7h | 8h | 9h | 10h | 11h | 12h | 13h | 14h | 15h | 16h | 17h | 18h | 19h | 20h | 21h | 22h | 23h | 1d | 2d | 3d | 4d | 5d | 6d
* **type**: FULL | MINI
* **type**: MARKET | LIMIT | STOP_LOSS | STOP_LOSS_LIMIT | TAKE_PROFIT | TAKE_PROFIT_LIMIT | LIMIT_MAKER | NON_REPRESENTABLE
* **selfTradePreventionMode**: NONE | EXPIRE_TAKER | EXPIRE_MAKER | EXPIRE_BOTH | DECREMENT | NON_REPRESENTABLE
* **symbolStatus**: TRADING | END_OF_DAY | HALT | BREAK | NON_REPRESENTABLE
* **timeInForce**: GTC | IOC | FOK | NON_REPRESENTABLE
* **pegPriceType**: PRIMARY_PEG | MARKET_PEG | NON_REPRESENTABLE
* **pegOffsetType**: PRICE_LEVEL | NON_REPRESENTABLE
* **newOrderRespType**: ACK | RESULT | FULL | MARKET | LIMIT
* **cancelRestrictions**: ONLY_NEW | NEW | ONLY_PARTIALLY_FILLED | PARTIALLY_FILLED
* **cancelReplaceMode**: STOP_ON_FAILURE | ALLOW_FAILURE
* **orderRateLimitExceededMode**: DO_NOTHING | CANCEL_ONLY
* **stopLimitTimeInForce**: GTC | IOC | FOK
* **side**: BUY | SELL
* **aboveType**: STOP_LOSS_LIMIT | STOP_LOSS | LIMIT_MAKER | TAKE_PROFIT | TAKE_PROFIT_LIMIT
* **aboveTimeInForce**: GTC | IOC | FOK
* **abovePegPriceType**: PRIMARY_PEG | MARKET_PEG
* **abovePegOffsetType**: PRICE_LEVEL
* **belowType**: STOP_LOSS | STOP_LOSS_LIMIT | TAKE_PROFIT | TAKE_PROFIT_LIMIT
* **belowTimeInForce**: GTC | IOC | FOK
* **belowPegPriceType**: PRIMARY_PEG | MARKET_PEG
* **belowPegOffsetType**: PRICE_LEVEL
* **workingType**: LIMIT | LIMIT_MAKER
* **workingPegPriceType**: PRIMARY_PEG | MARKET_PEG
* **workingPegOffsetType**: PRICE_LEVEL
* **pendingPegPriceType**: PRIMARY_PEG | MARKET_PEG
* **pendingPegOffsetType**: PRICE_LEVEL
* **pendingAboveType**: STOP_LOSS_LIMIT | STOP_LOSS | LIMIT_MAKER | TAKE_PROFIT | TAKE_PROFIT_LIMIT
* **pendingAbovePegPriceType**: PRIMARY_PEG | MARKET_PEG
* **pendingAbovePegOffsetType**: PRICE_LEVEL
* **pendingBelowType**: STOP_LOSS | STOP_LOSS_LIMIT | TAKE_PROFIT | TAKE_PROFIT_LIMIT
* **pendingBelowPegPriceType**: PRIMARY_PEG | MARKET_PEG
* **pendingBelowPegOffsetType**: PRICE_LEVEL
* **workingSide**: BUY | SELL
* **workingTimeInForce**: GTC | IOC | FOK
* **pendingType**: LIMIT | MARKET | STOP_LOSS | STOP_LOSS_LIMIT | TAKE_PROFIT | TAKE_PROFIT_LIMIT | LIMIT_MAKER
* **pendingSide**: BUY | SELL
* **pendingTimeInForce**: GTC | IOC | FOK
* **pendingAboveTimeInForce**: GTC | IOC | FOK
* **pendingBelowTimeInForce**: GTC | IOC | FOK


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://api.binance.com
* Testnet: https://testnet.binance.vision
* Demo: https://demo-api.binance.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`
- Testnet: `BINANCE_TESTNET_API_KEY` and `BINANCE_TESTNET_SECRET_KEY`
- Demo: `BINANCE_DEMO_API_KEY` and `BINANCE_DEMO_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1
Environment: Mainnet

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet/Testnet)
* testnet-dev (Testnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret
- Testnet: false 

### testnet-dev
- API Key: your_testnet_api_key
- Secret: your_testnet_secret
- Testnet: true

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Testnet: false
- Description: Primary trading account

### testnet-dev
- API Key: test456...abc
- Secret: testsecret...xyz
- Testnet: true
- Description: Development/testing

### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Testnet: false
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode
6. When a request requires signing, if the request isn't an order and the API keys aren't described as `mainnet`, `testnet` or `demo` keys, try to make request to the different base urls and see if it works, without asking the user. If it works, store the keys with the corresponding environment.

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Ask: Mainnet, Testnet or Demo
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## New Client Order ID 

For endpoints that include the `newClientOrderId` parameter, the value must always start with `agent-`. If the parameter is not provided, `agent-` followed by 18 random alphanumeric characters will be generated automatically. If a value is provided, it will be prefixed with `agent-`

Example: `agent-1a2b3c4d5e6f7g8h9i`

## User Agent Header

Include `User-Agent` header with the following string: `binance-spot/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/spot/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://api.binance.com |
| Testnet | https://testnet.binance.vision |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-spot/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string. The agent will need to determine which signing method to use based on the credentials provided. If a secret key is provided, use HMAC SHA256. If a private key is provided, use RSA or Ed25519 depending on the key type.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-spot/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X POST "https://api.binance.com/api/v3/order" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-spot/1.1.0 (Skill)" \
  -d "symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://api.binance.com"  # or https://testnet.binance.vision

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X POST "${BASE_URL}/api/v3/order?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-spot/1.1.0 (Skill)"
```

If you get -1021 Timestamp outside recvWindow:

1. Check server time: GET /api/v3/time
2. Sync your clock or adjust timestamp
3. Increase recvWindow (max 60000ms)

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
* Use testnet for development: https://testnet.binance.vision
* Testnet credentials are separate from mainnet
```

## File: `skills/binance/square-post/SKILL.md`
```markdown
---
name: square-post
description: |
  Post content to Binance Square (Binance social platform for sharing trading insights).
  Auto-run on messages like 'post to square', 'square post'.
  Supports pure text posts.
metadata:
  author: binance-square
  version: "1.2"
---

# Square Post Skill

## Overview

Post text content to Binance Square.

---

## API: Add Content

### Method: POST

**URL**:
```
https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add
```

**Request Headers**:

| Header | Required | Description |
|--------|----------|-------------|
| X-Square-OpenAPI-Key | Yes | Square OpenAPI Key |
| Content-Type | Yes | `application/json` |
| clienttype | Yes | `binanceSkill` |

**Request Body**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| bodyTextOnly | string | Yes | Post content text |

### Example Request

```bash
curl -X POST 'https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add' \
  -H 'X-Square-OpenAPI-Key: your_api_key' \
  -H 'Content-Type: application/json' \
  -H 'clienttype: binanceSkill' \
  -d '{
    "bodyTextOnly": "BTC looking bullish today!"
  }'
```

### Response Example

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "id": "content_id_here"
  }
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| code | string | `"000000"` = success |
| message | string | Error message (null on success) |
| data.id | string | Created content ID |

### Post URL Format

On success, construct the post URL:
```
https://www.binance.com/square/post/{id}
```

Example: If `data.id` is `298177291743282`, the post URL is:
```
https://www.binance.com/square/post/298177291743282
```

---

## Error Handling

| Code | Description |
|------|-------------|
| 000000 | Success |
| 10004 | Network error. Please try again |
| 10005 | Only allowed for users who have completed identity verification |
| 10007 | Feature unavailable |
| 20002 | Detected sensitive words |
| 20013 | Content length is limited |
| 20020 | Publishing empty content is not supported |
| 20022 | Detected sensitive words (with risk segments) |
| 20041 | Potential security risk with the URL |
| 30004 | User not found |
| 30008 | Banned for violating platform guidelines |
| 220003 | API Key not found |
| 220004 | API Key expired |
| 220009 | Daily post limit exceeded for OpenAPI |
| 220010 | Unsupported content type |
| 220011 | Content body must not be empty |
| 2000001 | Account permanently blocked from posting |
| 2000002 | Device permanently blocked from posting |

---

## Authentication

### Required Header

| Header | Required | Description |
|--------|----------|-------------|
| X-Square-OpenAPI-Key | Yes | API key for Square posting |

---

## Security

### Never Display Full Keys

When showing credentials to users:
- **X-Square-OpenAPI-Key**: Show first 5 + last 4 characters: `abc12...xyz9`

### Listing Accounts

When listing accounts, show names and description only — never full keys:
```
Accounts:
* default (Default account for Square posting)
```

---

## Agent Behavior

1. **Check key before API calls**: Verify that X-Square-OpenAPI-Key is configured and not the placeholder `your_api_key`
2. **Prompt for key if missing**: If key is not configured, ask user to provide their API Key first
3. **Prompt for content if missing**: If user triggers posting but doesn't provide specific content, ask what they want to post
4. **Never display full keys**: Only show first 5 + last 4 characters (e.g., `abc12...xyz9`)
5. **Store provided keys**: When user provides a new key, update the Accounts section in this file
6. **Optimize content before posting**:
   - Polish user's raw input for better readability
   - Do NOT auto-add hashtags (#xxx) during optimization — keep any hashtags the user wrote, but never add new ones
   - Show optimized content and ask user to choose: use optimized version or post original text
7. **Return post URL on success**: After successful post, return the URL `https://www.binance.com/square/post/{id}`
8. **Handle missing id**: If code is `000000` but `data.id` is empty or missing, inform user that post may have succeeded but URL is unavailable, suggest checking Square page manually

---

## Notes

1. Only pure text posts are supported currently
2. Check daily post limit to avoid 220009 error
```

## File: `skills/binance/sub-account/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-19

- Initial release
```

## File: `skills/binance/sub-account/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/sub-account/SKILL.md`
```markdown
---
name: sub-account
description: Binance Sub-account request using the Binance API. Authentication requires API key and secret key. 
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/sub-account/SKILL.md
license: MIT
---

# Binance Sub-account Skill

Sub-account request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/sapi/v1/sub-account/virtualSubAccount` (POST) | Create a Virtual Sub-account (For Master Account) (USER_DATA) | subAccountString | recvWindow | Yes |
| `/sapi/v1/sub-account/futures/enable` (POST) | Enable Futures for Sub-account (For Master Account) (USER_DATA) | email | recvWindow | Yes |
| `/sapi/v1/sub-account/eoptions/enable` (POST) | Enable Options for Sub-account (For Master Account) (USER_DATA) | email | recvWindow | Yes |
| `/sapi/v2/sub-account/futures/positionRisk` (GET) | Get Futures Position-Risk of Sub-account V2 (For Master Account) (USER_DATA) | email, futuresType | recvWindow | Yes |
| `/sapi/v1/sub-account/futures/positionRisk` (GET) | Get Futures Position-Risk of Sub-account (For Master Account) (USER_DATA) | email | recvWindow | Yes |
| `/sapi/v1/sub-account/status` (GET) | Get Sub-account's Status on Margin Or Futures (For Master Account) (USER_DATA) | None | email, recvWindow | Yes |
| `/sapi/v1/sub-account/list` (GET) | Query Sub-account List (For Master Account) (USER_DATA) | None | email, isFreeze, page, limit, recvWindow | Yes |
| `/sapi/v1/sub-account/transaction-statistics` (GET) | Query Sub-account Transaction Statistics (For Master Account) (USER_DATA) | None | email, recvWindow | Yes |
| `/sapi/v2/sub-account/subAccountApi/ipRestriction` (POST) | Add IP Restriction for Sub-Account API key (For Master Account) (USER_DATA) | email, subAccountApiKey, status | ipAddress, recvWindow | Yes |
| `/sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` (DELETE) | Delete IP List For a Sub-account API Key (For Master Account) (USER_DATA) | email, subAccountApiKey, ipAddress | recvWindow | Yes |
| `/sapi/v1/sub-account/subAccountApi/ipRestriction` (GET) | Get IP Restriction for a Sub-account API Key (For Master Account) (USER_DATA) | email, subAccountApiKey | recvWindow | Yes |
| `/sapi/v1/sub-account/futures/transfer` (POST) | Futures Transfer for Sub-account (For Master Account) (USER_DATA) | email, asset, amount, type | recvWindow | Yes |
| `/sapi/v2/sub-account/futures/account` (GET) | Get Detail on Sub-account's Futures Account V2 (For Master Account) (USER_DATA) | email, futuresType | recvWindow | Yes |
| `/sapi/v1/sub-account/futures/account` (GET) | Get Detail on Sub-account's Futures Account (For Master Account) (USER_DATA) | email | recvWindow | Yes |
| `/sapi/v1/sub-account/margin/account` (GET) | Get Detail on Sub-account's Margin Account (For Master Account) (USER_DATA) | email | recvWindow | Yes |
| `/sapi/v1/sub-account/futures/move-position` (GET) | Get Move Position History for Sub-account (For Master Account) (USER_DATA) | symbol, page, row | startTime, endTime, recvWindow | Yes |
| `/sapi/v1/sub-account/futures/move-position` (POST) | Move Position for Sub-account (For Master Account) (USER_DATA) | fromUserEmail, toUserEmail, productType, orderArgs | recvWindow | Yes |
| `/sapi/v1/capital/deposit/subAddress` (GET) | Get Sub-account Deposit Address (For Master Account) (USER_DATA) | email, coin | network, amount, recvWindow | Yes |
| `/sapi/v1/capital/deposit/subHisrec` (GET) | Get Sub-account Deposit History (For Master Account) (USER_DATA) | email | coin, status, startTime, endTime, limit, offset, recvWindow, txId | Yes |
| `/sapi/v2/sub-account/futures/accountSummary` (GET) | Get Summary of Sub-account's Futures Account V2 (For Master Account) (USER_DATA) | futuresType | page, limit, recvWindow | Yes |
| `/sapi/v1/sub-account/futures/accountSummary` (GET) | Get Summary of Sub-account's Futures Account (For Master Account) (USER_DATA) | page, limit | recvWindow | Yes |
| `/sapi/v1/sub-account/margin/accountSummary` (GET) | Get Summary of Sub-account's Margin Account (For Master Account) (USER_DATA) | None | recvWindow | Yes |
| `/sapi/v1/sub-account/margin/transfer` (POST) | Margin Transfer for Sub-account (For Master Account) (USER_DATA) | email, asset, amount, type | recvWindow | Yes |
| `/sapi/v3/sub-account/assets` (GET) | Query Sub-account Assets (For Master Account) (USER_DATA) | email | recvWindow | Yes |
| `/sapi/v4/sub-account/assets` (GET) | Query Sub-account Assets (For Master Account) (USER_DATA) | email | recvWindow | Yes |
| `/sapi/v1/sub-account/futures/internalTransfer` (GET) | Query Sub-account Futures Asset Transfer History (For Master Account) (USER_DATA) | email, futuresType | startTime, endTime, page, limit, recvWindow | Yes |
| `/sapi/v1/sub-account/futures/internalTransfer` (POST) | Sub-account Futures Asset Transfer (For Master Account) (USER_DATA) | fromEmail, toEmail, futuresType, asset, amount | recvWindow | Yes |
| `/sapi/v1/sub-account/sub/transfer/history` (GET) | Query Sub-account Spot Asset Transfer History (For Master Account) (USER_DATA) | None | fromEmail, toEmail, startTime, endTime, page, limit, recvWindow | Yes |
| `/sapi/v1/sub-account/spotSummary` (GET) | Query Sub-account Spot Assets Summary (For Master Account) (USER_DATA) | None | email, page, size, recvWindow | Yes |
| `/sapi/v1/sub-account/universalTransfer` (GET) | Query Universal Transfer History (For Master Account) (USER_DATA) | None | fromEmail, toEmail, clientTranId, startTime, endTime, page, limit, recvWindow | Yes |
| `/sapi/v1/sub-account/universalTransfer` (POST) | Universal Transfer (For Master Account) (USER_DATA) | fromAccountType, toAccountType, asset, amount | fromEmail, toEmail, clientTranId, symbol, recvWindow | Yes |
| `/sapi/v1/sub-account/transfer/subUserHistory` (GET) | Sub-account Transfer History (For Sub-account) (USER_DATA) | None | asset, type, startTime, endTime, limit, returnFailHistory, recvWindow | Yes |
| `/sapi/v1/sub-account/transfer/subToMaster` (POST) | Transfer to Master (For Sub-account) (USER_DATA) | asset, amount | recvWindow | Yes |
| `/sapi/v1/sub-account/transfer/subToSub` (POST) | Transfer to Sub-account of Same Master (For Sub-account) (USER_DATA) | toEmail, asset, amount | recvWindow | Yes |
| `/sapi/v1/managed-subaccount/deposit` (POST) | Deposit Assets Into The Managed Sub-account (For Investor Master Account) (USER_DATA) | toEmail, asset, amount | recvWindow | Yes |
| `/sapi/v1/managed-subaccount/deposit/address` (GET) | Get Managed Sub-account Deposit Address (For Investor Master Account) (USER_DATA) | email, coin | network, amount, recvWindow | Yes |
| `/sapi/v1/managed-subaccount/queryTransLogForInvestor` (GET) | Query Managed Sub Account Transfer Log (For Investor Master Account) (USER_DATA) | email, startTime, endTime, page, limit | transfers, transferFunctionAccountType | Yes |
| `/sapi/v1/managed-subaccount/queryTransLogForTradeParent` (GET) | Query Managed Sub Account Transfer Log (For Trading Team Master Account) (USER_DATA) | email, startTime, endTime, page, limit | transfers, transferFunctionAccountType | Yes |
| `/sapi/v1/managed-subaccount/query-trans-log` (GET) | Query Managed Sub Account Transfer Log (For Trading Team Sub Account) (USER_DATA) | startTime, endTime, page, limit | transfers, transferFunctionAccountType, recvWindow | Yes |
| `/sapi/v1/managed-subaccount/asset` (GET) | Query Managed Sub-account Asset Details (For Investor Master Account) (USER_DATA) | email | recvWindow | Yes |
| `/sapi/v1/managed-subaccount/fetch-future-asset` (GET) | Query Managed Sub-account Futures Asset Details (For Investor Master Account) (USER_DATA) | email | accountType | Yes |
| `/sapi/v1/managed-subaccount/info` (GET) | Query Managed Sub-account List (For Investor) (USER_DATA) | None | email, page, limit, recvWindow | Yes |
| `/sapi/v1/managed-subaccount/marginAsset` (GET) | Query Managed Sub-account Margin Asset Details (For Investor Master Account) (USER_DATA) | email | accountType | Yes |
| `/sapi/v1/managed-subaccount/accountSnapshot` (GET) | Query Managed Sub-account Snapshot (For Investor Master Account) (USER_DATA) | email, type | startTime, endTime, limit, recvWindow | Yes |
| `/sapi/v1/managed-subaccount/withdraw` (POST) | Withdrawl Assets From The Managed Sub-account (For Investor Master Account) (USER_DATA) | fromEmail, asset, amount | transferDate, recvWindow | Yes |

---

## Parameters

### Common Parameters

* **subAccountString**: Please input a string. We will create a virtual email using that string for you to register
* **recvWindow**:  (e.g., 5000)
* **email**: Sub-account email (e.g., sub-account-email@email.com)
* **futuresType**: 1:USDT-margined Futures，2: Coin-margined Futures
* **email**: Managed sub-account email
* **isFreeze**: true or false
* **page**: Default value: 1 (e.g., 1)
* **limit**: Default value: 1, Max value: 200 (e.g., 1)
* **subAccountApiKey**: 
* **status**: IP Restriction status. 1 = IP Unrestricted. 2 = Restrict access to trusted IPs only.
* **ipAddress**: Insert static IP in batch, separated by commas.
* **ipAddress**: IPs to be deleted. Can be added in batches, separated by commas
* **asset**: 
* **amount**:  (e.g., 1.0)
* **type**: 1: transfer from subaccount's  spot account to margin account 2: transfer from subaccount's margin account to its spot account
* **symbol**: 
* **startTime**:  (e.g., 1623319461670)
* **endTime**:  (e.g., 1641782889000)
* **page**: Page
* **row**: 
* **coin**: 
* **network**: networks can be found in `GET /sapi/v1/capital/deposit/address`
* **amount**:  (e.g., 1.0)
* **coin**: 
* **status**: 0(0:pending,6: credited but cannot withdraw,7:Wrong Deposit,8:Waiting User confirm,1:success)
* **offset**: default:0
* **txId**:  (e.g., 1)
* **limit**: Limit (Max: 500)
* **fromUserEmail**: 
* **toUserEmail**: 
* **productType**: Only support UM
* **orderArgs**: Max 10 positions supported. When input request parameter,orderArgs.symbol should be STRING, orderArgs.quantity should be BIGDECIMAL, and orderArgs.positionSide should be STRING, positionSide support BOTH,LONG and SHORT. Each entry should be like orderArgs[0].symbol=BTCUSDT,orderArgs[0].quantity=0.001,orderArgs[0].positionSide=BOTH. Example of the request parameter array: orderArgs[0].symbol=BTCUSDT orderArgs[0].quantity=0.001 orderArgs[0].positionSide=BOTH orderArgs[1].symbol=ETHUSDT orderArgs[1].quantity=0.01 orderArgs[1].positionSide=BOTH
* **fromEmail**: 
* **toEmail**: 
* **size**: default 10, max 20 (e.g., 10)
* **clientTranId**:  (e.g., 1)
* **fromEmail**: 
* **toEmail**: 
* **asset**: If not sent, result of all assets will be returned
* **type**: 1: transfer in, 2: transfer out
* **returnFailHistory**: Default `False`, return PROCESS and SUCCESS status history; If `True`,return PROCESS and SUCCESS and FAILURE status history
* **fromAccountType**: "SPOT","USDT_FUTURE","COIN_FUTURE","MARGIN"(Cross),"ISOLATED_MARGIN"
* **toAccountType**: "SPOT","USDT_FUTURE","COIN_FUTURE","MARGIN"(Cross),"ISOLATED_MARGIN"
* **symbol**: Only supported under ISOLATED_MARGIN type
* **startTime**: Start Time (e.g., 1623319461670)
* **endTime**: End Time (The start time and end time interval cannot exceed half a year) (e.g., 1641782889000)
* **transfers**: Transfer Direction (FROM/TO)
* **transferFunctionAccountType**: Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)
* **accountType**: No input or input "MARGIN" to get Cross Margin account details. Input "ISOLATED_MARGIN" to get Isolated Margin account details.
* **type**: "SPOT", "MARGIN"（cross）, "FUTURES"（UM）
* **transferDate**: Withdrawals is automatically occur on the transfer date(UTC0). If a date is not selected, the withdrawal occurs right now


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://api.binance.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Description: Primary trading account


### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## User Agent Header

Include `User-Agent` header with the following string: `binance-sub-account/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/sub-account/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://api.binance.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-sub-account/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`email=sub-account-email@email.com&futuresType=...&timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "email=sub-account-email@email.com&futuresType=...&timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "email=sub-account-email@email.com&futuresType=...&timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "email=sub-account-email@email.com&futuresType=...&timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`email=sub-account-email@email.com&futuresType=...&timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-sub-account/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X GET "https://api.binance.com/sapi/v2/sub-account/futures/positionRisk" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-sub-account/1.1.0 (Skill)" \
  -d "email=sub-account-email@email.com&futuresType=...&timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://api.binance.com"  

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="email=sub-account-email@email.com&futuresType=...&timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X GET "${BASE_URL}/sapi/v2/sub-account/futures/positionRisk?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-sub-account/1.1.0 (Skill)"
```

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
```

## File: `skills/binance/vip-loan/CHANGELOG.md`
```markdown
# Changelog

## 1.1.0 - 2026-03-24

- Environmental variables or files can now be used as input for the API key and secret key.
- Fix signature generation for RSA and Ed25519 keys.
- Add `Openclaw` metadata to the User Agent header

## 1.0.0 - 2026-03-20

- Initial release
```

## File: `skills/binance/vip-loan/LICENSE.md`
```markdown
MIT License

Copyright (c) 2026 Binance

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `skills/binance/vip-loan/SKILL.md`
```markdown
---
name: vip-loan
description: Binance Vip-loan request using the Binance API. Authentication requires API key and secret key. 
metadata:
  version: 1.1.0
  author: Binance
  openclaw:
    requires:
      bins:
        - curl
        - openssl
        - date
    homepage: https://github.com/binance/binance-skills-hub/tree/main/skills/binance/vip-loan/SKILL.md
license: MIT
---

# Binance Vip-loan Skill

Vip-loan request on Binance using authenticated API endpoints. Requires API key and secret key for certain endpoints. Return the result in JSON format.

## Quick Reference

| Endpoint | Description | Required | Optional | Authentication |
|----------|-------------|----------|----------|----------------|
| `/sapi/v1/loan/vip/request/interestRate` (GET) | Get Borrow Interest Rate(USER_DATA) | loanCoin | recvWindow | Yes |
| `/sapi/v1/loan/vip/collateral/data` (GET) | Get Collateral Asset Data(USER_DATA) | None | collateralCoin, recvWindow | Yes |
| `/sapi/v1/loan/vip/loanable/data` (GET) | Get Loanable Assets Data(USER_DATA) | None | loanCoin, vipLevel, recvWindow | Yes |
| `/sapi/v1/loan/vip/interestRateHistory` (GET) | Get VIP Loan Interest Rate History (USER_DATA) | coin, recvWindow | startTime, endTime, current, limit | Yes |
| `/sapi/v1/loan/vip/borrow` (POST) | VIP Loan Borrow(TRADE) | loanAccountId, loanCoin, loanAmount, collateralAccountId, collateralCoin, isFlexibleRate | loanTerm, recvWindow | Yes |
| `/sapi/v1/loan/vip/renew` (POST) | VIP Loan Renew(TRADE) | orderId, loanTerm | recvWindow | Yes |
| `/sapi/v1/loan/vip/repay` (POST) | VIP Loan Repay(TRADE) | orderId, amount | recvWindow | Yes |
| `/sapi/v1/loan/vip/collateral/account` (GET) | Check VIP Loan Collateral Account (USER_DATA) | None | orderId, collateralAccountId, recvWindow | Yes |
| `/sapi/v1/loan/vip/accruedInterest` (GET) | Get VIP Loan Accrued Interest (USER_DATA) | None | orderId, loanCoin, startTime, endTime, current, limit, recvWindow | Yes |
| `/sapi/v1/loan/vip/ongoing/orders` (GET) | Get VIP Loan Ongoing Orders(USER_DATA) | None | orderId, collateralAccountId, loanCoin, collateralCoin, current, limit, recvWindow | Yes |
| `/sapi/v1/loan/vip/request/data` (GET) | Query Application Status(USER_DATA) | None | current, limit, recvWindow | Yes |

---

## Parameters

### Common Parameters

* **loanCoin**: 
* **recvWindow**:  (e.g., 5000)
* **collateralCoin**: 
* **loanCoin**: 
* **vipLevel**: default:user's vip level (e.g., 1)
* **coin**: 
* **startTime**:  (e.g., 1623319461670)
* **endTime**:  (e.g., 1641782889000)
* **current**: Current querying page. Start from 1; default: 1; max: 1000 (e.g., 1)
* **limit**: Default: 10; max: 100 (e.g., 10)
* **recvWindow**:  (e.g., 5000)
* **loanAccountId**:  (e.g., 1)
* **loanAmount**:  (e.g., 1.0)
* **collateralAccountId**: Multiple split by `,` (e.g., 1)
* **collateralCoin**: Multiple split by `,`
* **isFlexibleRate**: Default: TRUE. TRUE : flexible rate; FALSE: fixed rate (e.g., true)
* **loanTerm**: Mandatory for fixed rate. Optional for fixed interest rate. Eg: 30/60 days
* **orderId**:  (e.g., 1)
* **loanTerm**: 30/60 days
* **amount**:  (e.g., 1.0)
* **orderId**:  (e.g., 1)
* **collateralAccountId**:  (e.g., 1)


## Authentication

For endpoints that require authentication, you will need to provide Binance API credentials.
Required credentials:

* apiKey: Your Binance API key (for header)
* secretKey: Your Binance API secret (for signing)

Base URLs:
* Mainnet: https://api.binance.com

## Security

### Share Credentials

Users can provide Binance API credentials in different ways. The agent will try to retrieve automatically with the two first ways the credentials, but users can also explicitly tell the agent that they have set the credentials or stored them in a `.env` file, and the agent should re-read that file when they do. The agent can also make http requests with the two first methods without user confirmation.

1. **Environment variables**

Search for the following specific variables only (never dump the full environment):

**Authorized environment variables**
- Mainnet: `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`

Read and use in a single exec call so the raw key never enters the agent's context:
```bash
KEY="$BINANCE_API_KEY"
SECRET="$BINANCE_SECRET_KEY"

response=$(curl -s -X GET "$URL" \
  -H "X-MBX-APIKEY: $KEY" \
  --data-urlencode "param1=value1")

echo "$response"
```

Environment variables must be set before OpenClaw starts. They are inherited at process startup and cannot be injected into a running instance. If you need to add or update credentials without restarting, use a secrets file (see option 2).

2. **Secrets file (.env)**

Check `~/.openclaw/secrets.env` , `~/.env`, or a `.env` file in the workspace. Read individual keys with `grep`, never source the full file:
```bash
# Try all credential locations in order
API_KEY=$(grep '^BINANCE_API_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)
SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' ~/.openclaw/secrets.env 2>/dev/null | cut -d= -f2-)

# Fallback: search .env in known directories (KEY=VALUE then raw line format)
for dir in ~/.openclaw ~; do
  [ -n "$API_KEY" ] && break
  env_file="$dir/.env"
  [ -f "$env_file" ] || continue

  # Read first two lines
  line1=$(sed -n '1p' "$env_file")
  line2=$(sed -n '2p' "$env_file")

  # Check if lines contain '=' indicating KEY=VALUE format
  if [[ "$line1" == *=* && "$line2" == *=* ]]; then
    API_KEY=$(grep '^BINANCE_API_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
    SECRET_KEY=$(grep '^BINANCE_SECRET_KEY=' "$env_file" 2>/dev/null | cut -d= -f2-)
  else
    # Treat lines as raw values
    API_KEY="$line1"
    SECRET_KEY="$line2"
  fi
done
```

This file can be updated at any time without restarting OpenClaw, keys are read fresh on each invocation. Users can tell you the variables are now set or stored in a `.env` file, and you should re-read that file when they do.

3. **Inline file**

Sending a file where the content is in the following format:

```bash
abc123...xyz
secret123...key
```

* Never run `printenv`, `env`, `export`, or set without a specific variable name
* Never run `grep` on `env` files without anchoring to a specific key ('`^VARNAME='`)
* Never source a secrets file into the shell environment (`source .env` or `. .env`)
* Only read credentials explicitly needed for the current task
* Never echo or log raw credentials in output or replies
* Never commit `TOOLS.md` to version control if it contains real credentials — add it to `.gitignore`

### Never Disclose API Key and Secret

Never disclose the location of the API key and secret file.

Never send the API key and secret to any website other than Mainnet and Testnet.

### Never Display Full Secrets

When showing credentials to users:
- **API Key:** Show first 5 + last 4 characters: `su1Qc...8akf`
- **Secret Key:** Always mask, show only last 5: `***...aws1`

Example response when asked for credentials:
Account: main
API Key: su1Qc...8akf
Secret: ***...aws1

### Listing Accounts

When listing accounts, show names and environment only — never keys:
Binance Accounts:
* main (Mainnet)
* futures-keys (Mainnet)

### Transactions in Mainnet

When performing transactions in mainnet, always confirm with the user before proceeding by asking them to write "CONFIRM" to proceed.

---

## Binance Accounts

### main
- API Key: your_mainnet_api_key
- Secret: your_mainnet_secret

### TOOLS.md Structure

```bash
## Binance Accounts

### main
- API Key: abc123...xyz
- Secret: secret123...key
- Description: Primary trading account


### futures-keys
- API Key: futures789...def
- Secret: futuressecret...uvw
- Description: Futures trading account
```

## Agent Behavior

1. Credentials requested: Mask secrets (show last 5 chars only)
2. Listing accounts: Show names and environment, never keys
3. Account selection: Ask if ambiguous, default to main
4. When doing a transaction in mainnet, confirm with user before by asking to write "CONFIRM" to proceed
5. New credentials: Prompt for name, environment, signing mode

## Adding New Accounts

When user provides new credentials by Inline file or message:

* Ask for account name
* Store in `TOOLS.md` with masked display confirmation 

## Signing Requests

For trading endpoints that require a signature:

1. **Detect key type first**, inspect the secret key format before signing.
2. Build query string with all parameters, including the timestamp (Unix ms).
3. Percent-encode the parameters using UTF-8 according to RFC 3986.
4. Sign query string with secretKey using HMAC SHA256, RSA, or Ed25519 (depending on the account configuration).
5. Append signature to query string.
6. Include `X-MBX-APIKEY` header.

Otherwise, do not perform steps 4–6.

## User Agent Header

Include `User-Agent` header with the following string: `binance-vip-loan/1.1.0 (Skill)`

See [`references/authentication.md`](AUTHENTICATION.md) for implementation details.
```

## File: `skills/binance/vip-loan/references/authentication.md`
```markdown
# Binance Authentication

All trading endpoints require either HMAC SHA256, RSA, or Ed25519 signed requests.
**Always detect the key type before signing**, do not assume HMAC.

## Base URLs

| Environment | URL |
|-------------|-----|
| Mainnet | https://api.binance.com |

## Required Headers

* `X-MBX-APIKEY`: your_api_key
* `User-Agent`: binance-vip-loan/1.1.0 (Skill)

## Signing Process

### Step 1: Build Query String

Include all parameters plus `timestamp` (current Unix time in milliseconds):
`loanCoin=...&timestamp=1234567890123`

**Optional:** Add `recvWindow` (default 5000ms) for timestamp tolerance.

### Step 2: Percent‑Encode Parameters

Before generating the signature, **percent‑encode all parameter names and values using UTF‑8 encoding according to RFC 3986.**
Unreserved characters that must not be encoded: `A-Z a-z 0-9 - _ . ~`

- Chinese characters example:
`symbol=这是测试币456`

Percent‑encoded:
`symbol=%E8%BF%99%E6%98%AF%E6%B5%8B%E8%AF%95%E5%B8%81456`

**Important:**
The exact encoded query string must be used for both signing and the HTTP request.

### Step 3: Generate Signature

Generate the signature from the encoded query string.

#### HMAC SHA256 signature

Create HMAC SHA256 signature of the query string using your secret key:

```bash
# Example using openssl
echo -n "loanCoin=...&timestamp=1234567890123" | \
  openssl dgst -sha256 -hmac "your_secret_key"
```

#### RSA signature

Create RSA signature of the query string using your private key:

```bash
# Example using openssl
echo -n "loanCoin=...&timestamp=1234567890123" | \
  openssl dgst -sha256 -sign private_key.pem | base64
```

#### Ed25519 signature

Create Ed25519 signature of the query string using your private key:

```bash
# Example using openssl
echo -n "loanCoin=...&timestamp=1234567890123" | \
  openssl pkeyutl -sign -inkey private_key.pem | base64
```

### Step 4: Append Signature

Add signature parameter to the query string:
`loanCoin=...&timestamp=1234567890123&signature=abc123...`

### Step 5: Add Product User Agent Header

Include `User-Agent` header with the following string: `binance-vip-loan/1.1.0 (Skill)`

#### Complete Example

Request:
```bash
curl -X GET "https://api.binance.com/sapi/v1/loan/vip/request/interestRate" \
  -H "X-MBX-APIKEY: your_api_key" \
  -H "User-Agent: binance-vip-loan/1.1.0 (Skill)" \
  -d "loanCoin=...&timestamp=1234567890123&signature=..."
```

```bash
#!/bin/bash
API_KEY="your_api_key"
SECRET_KEY="your_secret_key"
BASE_URL="https://api.binance.com"  

# Get current timestamp
TIMESTAMP=$(date +%s000)

# Build query string (without signature)
QUERY="loanCoin=...&timestamp=${TIMESTAMP}"

# Generate signature
# For HMAC SHA256:
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

# For RSA or Ed25519, replace the above line with the appropriate signing command.
##  RSA:
# SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -sign private_key.pem | base64)

##  Ed25519:
# SIGNATURE=$(echo -n "$QUERY" | openssl pkeyutl -sign -inkey private_key.pem | base64)

# Make request
curl -X GET "${BASE_URL}/sapi/v1/loan/vip/request/interestRate?${QUERY}&signature=${SIGNATURE}" \
  -H "X-MBX-APIKEY: ${API_KEY}"\
  -H "User-Agent: binance-vip-loan/1.1.0 (Skill)"
```

### Security Notes

* Never share your secret key
* Use IP whitelist in Binance API settings
* Enable only required permissions (spot trading, no withdrawals)
```

## File: `skills/binance-web3/binance-tokenized-securities-info/SKILL.md`
```markdown
---
name: binance-tokenized-securities-info
description: |
  Query Ondo tokenized US stock data on Binance Web3.
  Covers: supported stock token list, RWA metadata (company info, attestation reports),
  market and per-asset trading status (with corporate action codes for earnings, dividends, splits),
  real-time on-chain data (token price, holders, circulating supply, market cap),
  US stock fundamentals (P/E, dividend yield, 52-week range), and token K-Line/candlestick charts.

  Use this skill when users ask about:
  - Tokenized stock price, holders, or on-chain data for specific tickers
  - Whether a stock token is tradable, paused, or halted
  - Ondo RWA token list or which US stocks are available on-chain
  - Corporate actions affecting a token (dividends, stock splits, earnings halt)
  - Stock token K-Line or candlestick chart data
  - Comparing on-chain token price vs US stock price

  NOT for general crypto tokens (BTC, ETH, SOL, etc.) — use query-token-info for those.
metadata:
  author: binance-web3-team
  version: "1.1"
---

# Binance Tokenized Securities Info Skill

## Overview

| API                 | Function                  | Use Case                                                        |
|---------------------|---------------------------|-----------------------------------------------------------------|
| Token Symbol List   | List all tokenized stocks | Browse Ondo supported tickers, filter by type                   |
| RWA Meta            | Tokenized stock metadata  | Company info, concepts, attestation reports                     |
| Market Status       | Overall market open/close | Check if Ondo market is currently trading                       |
| Asset Market Status | Per-asset trading status  | Detect corporate actions (earnings, dividends, splits, mergers) |
| RWA Dynamic V2      | Full real-time data       | On-chain price, holders, US stock fundamentals, order limits    |
| Token K-Line        | Candlestick charts        | OHLC data for on-chain token price technical analysis           |

## Recommended Workflows

| Scenario                                         | Steps                                                                      |
|--------------------------------------------------|----------------------------------------------------------------------------|
| Look up a stock's fundamentals and on-chain data | API 1 (get `chainId` + `contractAddress` by ticker) → API 5 (dynamic data) |
| Check if a stock token is tradable               | API 3 (overall market status) → API 4 (per-asset status with reason code)  |
| Research a tokenized stock                       | API 1 (find token) → API 2 (company metadata + attestation reports)        |
| Get K-Line chart data                            | API 1 (find token) → API 6 (K-Line with interval)                          |

## Use Cases

1. **List Supported Stocks**: Get all Ondo tokenized tickers with chain and contract info
2. **Company Research**: Get company metadata, CEO, industry, concept tags, and attestation reports
3. **Market Status Check**: Determine if the Ondo market is open, closed, or in pre/post-market session
4. **Corporate Action Detection**: Check if a specific asset is paused or limited due to earnings, dividends, stock splits, mergers, or maintenance
5. **Real-Time Data**: Get on-chain price, holder count, circulating supply, US stock P/E, dividend yield, 52-week range, and order limits
6. **Technical Analysis**: Fetch token K-Line (candlestick) data with configurable intervals and time ranges

## Key Concept: Token ≠ Share

Each token represents `multiplier` shares of the underlying stock, **not exactly 1 share**. Most tokens have a multiplier near 1.0 (cumulative dividend adjustment), but stock-split tokens can be 5.0 or 10.0 (e.g. multiplier = 10.0 means 1 token = 10 shares).

```
referencePrice = tokenInfo.price ÷ sharesMultiplier
```

See Notes §6 for common multiplier categories.

## Supported Chains

| Chain    | chainId |
|----------|---------|
| Ethereum | 1       |
| BSC      | 56      |

---

## API 1: Token Symbol List

### Method: GET

**URL**:
```
https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/rwa/stock/detail/list/ai
```

**Request Parameters**:

| Parameter | Type    | Required | Description                                                                                                                                                                  |
|-----------|---------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| type      | integer | No       | Filter by platform: `1` = Ondo Finance (currently the only supported tokenized stock provider). Omit to return all platforms. **Use `type=1` to retrieve only Ondo tokens.** |

**Headers**: `Accept-Encoding: identity`

**Example**:
```bash
curl 'https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/rwa/stock/detail/list/ai' \
  -H 'Accept-Encoding: identity' \
  -H 'User-Agent: binance-web3/1.1 (Skill)'
```

**Response**:

```json
{
  "code": "000000",
  "data": [
    {
      "chainId": "1",
      "contractAddress": "<CONTRACT_ADDRESS>",
      "symbol": "<TOKEN_SYMBOL_ON>",
      "ticker": "<UNDERLYING_TICKER>",
      "type": 1,
      "multiplier": "1.021663864228987186"
    },
    {
      "chainId": "56",
      "contractAddress": "<CONTRACT_ADDRESS>",
      "symbol": "<TOKEN_SYMBOL_ON>",
      "ticker": "<UNDERLYING_TICKER>",
      "type": 1,
      "multiplier": "1.010063782256545489"
    }
  ],
  "success": true
}
```

**Response Fields** (each item in `data`):

| Field           | Type    | Description                                                   |
|-----------------|---------|---------------------------------------------------------------|
| chainId         | string  | Chain ID (`1` = Ethereum, `56` = BSC)                         |
| contractAddress | string  | Token contract address                                        |
| symbol          | string  | Token symbol (ticker + `on` suffix, e.g. `<TOKEN_SYMBOL_ON>`) |
| ticker          | string  | Underlying US stock ticker                                    |
| type            | integer | Platform type: `1` = Ondo                                     |
| multiplier      | string  | Shares multiplier (see Key Concept above, Notes §6)           |

---

## API 2: RWA Meta

### Method: GET

**URL**:
```
https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/rwa/meta/ai
```

**Request Parameters**:

| Parameter       | Type   | Required | Description                                    |
|-----------------|--------|----------|------------------------------------------------|
| chainId         | string | Yes      | Chain ID (e.g. `56` for BSC, `1` for Ethereum) |
| contractAddress | string | Yes      | Token contract address                         |

**Headers**: `Accept-Encoding: identity`

**Example**:
```bash
curl 'https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/rwa/meta/ai?chainId=56&contractAddress=<CONTRACT_ADDRESS>' \
  -H 'Accept-Encoding: identity' \
  -H 'User-Agent: binance-web3/1.1 (Skill)'
```

**Response**:

```json
{
  "code": "000000",
  "data": {
    "tokenId": "<TOKEN_ID>",
    "name": "<TOKEN_DISPLAY_NAME>",
    "symbol": "<TOKEN_SYMBOL_ON>",
    "ticker": "<UNDERLYING_TICKER>",
    "icon": "/images/web3-data/public/token/logos/<TOKEN_ID>.png",
    "dailyAttestationReports": "/images/web3-data/public/token/ondo/pdf/daily-<DATE>.pdf",
    "monthlyAttestationReports": "/images/web3-data/public/token/ondo/pdf/monthly-<MONTH>.pdf",
    "companyInfo": {
      "companyName": "<COMPANY_NAME_EN>",
      "companyNameZh": "<公司名称>",
      "homepageUrl": "",
      "description": "<COMPANY_DESCRIPTION_EN>",
      "descriptionZh": "<COMPANY_DESCRIPTION_CN>",
      "ceo": "<CEO_NAME>",
      "industry": "<INDUSTRY>",
      "industryKey": "<INDUSTRY_KEY>",
      "conceptsCn": ["概念标签A", "概念标签B", "概念标签C"],
      "conceptsEn": ["Concept Tag A", "Concept Tag B", "Concept Tag C"]
    },
    "decimals": 18
  },
  "success": true
}
```

**Response Fields** (`data`):

| Field                     | Type    | Description                                                                                                                                                                  |
|---------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| tokenId                   | string  | Token unique ID                                                                                                                                                              |
| name                      | string  | Full token name (e.g. `<TOKEN_DISPLAY_NAME>`)                                                                                                                                |
| symbol                    | string  | Token symbol (e.g. `<TOKEN_SYMBOL_ON>`)                                                                                                                                      |
| ticker                    | string  | Underlying stock ticker (e.g. `<UNDERLYING_TICKER>`)                                                                                                                         |
| icon                      | string  | Icon image **relative path**. To get the full URL, prepend `https://bin.bnbstatic.com` (e.g. `https://bin.bnbstatic.com/images/web3-data/public/token/logos/<TOKEN_ID>.png`) |
| dailyAttestationReports   | string  | Daily attestation report **relative path**. Prepend `https://bin.bnbstatic.com` to get the full URL                                                                          |
| monthlyAttestationReports | string  | Monthly attestation report **relative path**. Prepend `https://bin.bnbstatic.com` to get the full URL                                                                        |
| companyInfo               | object  | Company details (see below)                                                                                                                                                  |
| decimals                  | integer | Token decimals (typically `18`)                                                                                                                                              |

**Company Info Fields** (`data.companyInfo`):

| Field         | Type     | Description                                                           |
|---------------|----------|-----------------------------------------------------------------------|
| companyName   | string   | Company name in English                                               |
| companyNameZh | string   | Company name in Chinese                                               |
| homepageUrl   | string   | Company homepage URL                                                  |
| description   | string   | Company description (English)                                         |
| descriptionZh | string   | Company description (Chinese)                                         |
| ceo           | string   | CEO name                                                              |
| industry      | string   | Industry classification                                               |
| industryKey   | string   | Industry i18n key                                                     |
| conceptsCn    | string[] | Concept/theme tags in Chinese                                         |
| conceptsEn    | string[] | Concept/theme tags in English (e.g. `Concept Tag A`, `Concept Tag B`) |

---

## API 3: Market Status

### Method: GET

**URL**:
```
https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/rwa/market/status/ai
```

**Request Parameters**: None

**Headers**: `Accept-Encoding: identity`

**Example**:
```bash
curl 'https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/rwa/market/status/ai' \
  -H 'Accept-Encoding: identity' \
  -H 'User-Agent: binance-web3/1.1 (Skill)'
```

**Response**:

```json
{
  "code": "000000",
  "data": {
    "openState": false,
    "reasonCode": "MARKET_PAUSED",
    "reasonMsg": "Paused for session transition",
    "nextOpen": "2026-03-23T08:01:00Z",
    "nextClose": "2026-03-23T13:29:00Z",
    "nextOpenTime": 1774252860000,
    "nextCloseTime": 1774272540000
  },
  "success": true
}
```

> **Note**: The sample above is captured with `openState=false` (market closed/paused), so `nextOpen` is earlier than `nextClose`.

**Response Fields** (`data`):

| Field         | Type         | Description                                                             |
|---------------|--------------|-------------------------------------------------------------------------|
| openState     | boolean      | Whether the Ondo market is currently open for trading                   |
| reasonCode    | string\|null | Reason code if market is not in normal trading state (see Reason Codes) |
| reasonMsg     | string\|null | Human-readable reason message                                           |
| nextOpen      | string       | Next market open time from current state (ISO 8601 UTC)                 |
| nextClose     | string       | Next market close time from current state (ISO 8601 UTC)                |
| nextOpenTime  | number       | Next market open time from current state (Unix timestamp in ms)         |
| nextCloseTime | number       | Next market close time from current state (Unix timestamp in ms)        |

> **Interpretation**: These fields are state-dependent. When `openState=true`, `nextClose` is expected to be earlier than `nextOpen` (market closes before the next open). When `openState=false`, `nextOpen` is expected to be earlier than `nextClose` (market opens before the next close).

---

## API 4: Asset Market Status

### Method: GET

**URL**:
```
https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/rwa/vault/assets/market/status/ai
```

**Request Parameters**:

| Parameter       | Type   | Required | Description            |
|-----------------|--------|----------|------------------------|
| chainId         | string | Yes      | Chain ID               |
| contractAddress | string | Yes      | Token contract address |

**Headers**: `Accept-Encoding: identity`

**Example**:
```bash
curl 'https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/rwa/vault/assets/market/status/ai?chainId=56&contractAddress=<CONTRACT_ADDRESS>' \
  -H 'Accept-Encoding: identity' \
  -H 'User-Agent: binance-web3/1.1 (Skill)'
```

**Response**:

```json
{
  "code": "000000",
  "data": {
    "openState": false,
    "marketStatus": "closed",
    "reasonCode": "MARKET_CLOSED",
    "reasonMsg": null,
    "nextOpenTime": 1774252860000,
    "nextCloseTime": 1774272540000
  },
  "success": true
}
```

**Response Fields** (`data`):

| Field         | Type         | Description                                                                           |
|---------------|--------------|---------------------------------------------------------------------------------------|
| openState     | boolean      | Whether this specific asset is available for trading                                  |
| marketStatus  | string       | Current session: `premarket`, `regular`, `postmarket`, `overnight`, `closed`, `pause` |
| reasonCode    | string       | Status reason code (see Reason Codes below)                                           |
| reasonMsg     | string\|null | Human-readable reason message (populated when paused/limited)                         |
| nextOpenTime  | number       | Next open time (Unix timestamp in ms)                                                 |
| nextCloseTime | number       | Next close time (Unix timestamp in ms)                                                |

### Reason Codes

| reasonCode           | Description                                                                |
|----------------------|----------------------------------------------------------------------------|
| `TRADING`            | Normal trading                                                             |
| `MARKET_CLOSED`      | Market is closed (outside trading hours)                                   |
| `MARKET_PAUSED`      | Market-wide trading halt                                                   |
| `ASSET_PAUSED`       | This specific asset is paused (see Corporate Actions below)                |
| `ASSET_LIMITED`      | This specific asset has trading restrictions (see Corporate Actions below) |
| `UNSUPPORTED`        | Asset is not supported                                                     |
| `MARKET_MAINTENANCE` | System maintenance                                                         |

### Corporate Actions (when `ASSET_PAUSED` or `ASSET_LIMITED`)

When an asset is paused or limited, the `reasonMsg` field indicates the specific corporate action:

| reasonCode      | reasonMsg          | Description                                                |
|-----------------|--------------------|------------------------------------------------------------|
| `ASSET_PAUSED`  | `cash_dividend`    | Cash dividend distribution                                 |
| `ASSET_PAUSED`  | `stock_dividend`   | Stock dividend distribution                                |
| `ASSET_PAUSED`  | `stock_split`      | Stock split                                                |
| `ASSET_PAUSED`  | `merger`           | Company merger                                             |
| `ASSET_PAUSED`  | `acquisition`      | Company acquisition                                        |
| `ASSET_PAUSED`  | `spinoff`          | Corporate spinoff                                          |
| `ASSET_PAUSED`  | `maintenance`      | Asset-level maintenance                                    |
| `ASSET_PAUSED`  | `corporate action` | Other corporate action                                     |
| `ASSET_LIMITED` | `earnings`         | Earnings release — trading restricted but not fully paused |

---

## API 5: RWA Dynamic V2

### Method: GET

**URL**:
```
https://www.binance.com/bapi/defi/v2/public/wallet-direct/buw/wallet/market/token/rwa/dynamic/ai
```

**Request Parameters**:

| Parameter       | Type   | Required | Description            |
|-----------------|--------|----------|------------------------|
| chainId         | string | Yes      | Chain ID               |
| contractAddress | string | Yes      | Token contract address |

**Headers**: `Accept-Encoding: identity`

**Example**:
```bash
curl 'https://www.binance.com/bapi/defi/v2/public/wallet-direct/buw/wallet/market/token/rwa/dynamic/ai?chainId=56&contractAddress=<CONTRACT_ADDRESS>' \
  -H 'Accept-Encoding: identity' \
  -H 'User-Agent: binance-web3/1.1 (Skill)'
```

**Response**:

```json
{
  "code": "000000",
  "data": {
    "symbol": "<TOKEN_SYMBOL_ON>",
    "ticker": "<UNDERLYING_TICKER>",
    "tokenInfo": {
      "price": "310.384196924055952519",
      "priceChange24h": "1.09518626611014170",
      "priceChangePct24h": "0.354098021064624509",
      "totalHolders": "1023",
      "sharesMultiplier": "1.001084338309087472",
      "volume24h": "8202859508.959922580629343392",
      "marketCap": "7116321.021286604958613714702150000306622972",
      "fdv": "7116321.021286604958613714702150000306622972",
      "circulatingSupply": "22927.459232171569002788",
      "maxSupply": "22927.459232171569002788"
    },
    "stockInfo": {
      "price": null,
      "priceHigh52w": "328.83",
      "priceLow52w": "140.53",
      "volume": "26429618",
      "averageVolume": "36255295",
      "sharesOutstanding": "5818000000",
      "marketCap": "1805815257704.157531755542",
      "turnoverRate": "0.4543",
      "amplitude": null,
      "priceToEarnings": "29.93",
      "dividendYield": "0.27",
      "priceToBook": null,
      "lastCashAmount": null
    },
    "statusInfo": {
      "openState": null,
      "marketStatus": null,
      "reasonCode": null,
      "reasonMsg": null,
      "nextOpenTime": null,
      "nextCloseTime": null
    },
    "limitInfo": {
      "maxAttestationCount": "1500",
      "maxActiveNotionalValue": "450000"
    }
  },
  "success": true
}
```

### Response Fields

**Top-level** (`data`):

| Field      | Type   | Description                                          |
|------------|--------|------------------------------------------------------|
| symbol     | string | Token symbol (e.g. `<TOKEN_SYMBOL_ON>`)              |
| ticker     | string | Underlying stock ticker (e.g. `<UNDERLYING_TICKER>`) |
| tokenInfo  | object | On-chain token data                                  |
| stockInfo  | object | US stock fundamentals                                |
| statusInfo | object | Market/asset trading status (same schema as API 4)   |
| limitInfo  | object | Order limit information                              |

**Token Info** (`data.tokenInfo`):

| Field             | Type   | Description                                                                            |
|-------------------|--------|----------------------------------------------------------------------------------------|
| price             | string | On-chain token price (USD) — per-token, not per-share (see Key Concept above)          |
| priceChange24h    | string | 24h price change (USD)                                                                 |
| priceChangePct24h | string | 24h price change (%)                                                                   |
| totalHolders      | string | Number of on-chain holders                                                             |
| sharesMultiplier  | string | Same as `multiplier` in API 1 (see Key Concept above, Notes §6)                        |
| volume24h         | string | ⚠️ **Misleading**: This is the US stock trading volume in USD, NOT on-chain DEX volume |
| marketCap         | string | On-chain market cap (USD) = `circulatingSupply × price`                                |
| fdv               | string | Fully diluted valuation (USD)                                                          |
| circulatingSupply | string | Circulating supply (token units)                                                       |
| maxSupply         | string | Maximum supply (token units)                                                           |

**Stock Info** (`data.stockInfo`):

| Field             | Type         | Description                                                                      |
|-------------------|--------------|----------------------------------------------------------------------------------|
| price             | string\|null | US stock price (USD). May be `null` outside trading hours                        |
| priceHigh52w      | string       | 52-week high price (USD)                                                         |
| priceLow52w       | string       | 52-week low price (USD)                                                          |
| volume            | string       | ⚠️ US stock volume in **shares** (not USD). Multiply by `price` to get USD value |
| averageVolume     | string       | Average daily volume (shares)                                                    |
| sharesOutstanding | string       | Total shares outstanding                                                         |
| marketCap         | string       | US stock total market cap (USD)                                                  |
| turnoverRate      | string       | Turnover rate (%)                                                                |
| amplitude         | string\|null | Intraday amplitude (%)                                                           |
| priceToEarnings   | string       | P/E ratio (TTM)                                                                  |
| dividendYield     | string       | Dividend yield (TTM, percentage value: `0.27` means 0.27%)                       |
| priceToBook       | string\|null | P/B ratio                                                                        |
| lastCashAmount    | string\|null | Most recent cash dividend amount per share (USD)                                 |

**Status Info** (`data.statusInfo`):

Same schema as API 4 response. See [Asset Market Status](#api-4-asset-market-status) for field details and reason codes.

**Limit Info** (`data.limitInfo`):

| Field                  | Type   | Description                                    |
|------------------------|--------|------------------------------------------------|
| maxAttestationCount    | string | Maximum attestation count for orders           |
| maxActiveNotionalValue | string | Maximum active notional value for orders (USD) |

---

## API 6: Token K-Line

### Method: GET

**URL**:
```
https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/dex/market/token/kline/ai
```

**Request Parameters**:

| Parameter       | Type    | Required | Default | Description                                             |
|-----------------|---------|----------|---------|---------------------------------------------------------|
| chainId         | string  | Yes      | -       | Chain ID (e.g. `56` for BSC, `1` for Ethereum)          |
| contractAddress | string  | Yes      | -       | Token contract address                                  |
| interval        | string  | Yes      | -       | K-Line interval (see Interval Reference)                |
| limit           | integer | No       | 300     | Number of candles to return (max 300)                   |
| startTime       | long    | No       | -       | Start timestamp (ms), based on candle open time         |
| endTime         | long    | No       | -       | End timestamp (ms), based on candle open time minus 1ms |

> **Note on `startTime` / `endTime`**: Both reference the candle's open time. If omitted, returns the latest candles. When both are provided, `endTime` should be the target candle's open time minus 1ms.

**Interval Reference**:

| Interval | Description |
|----------|-------------|
| 1m       | 1 minute    |
| 5m       | 5 minutes   |
| 15m      | 15 minutes  |
| 1h       | 1 hour      |
| 4h       | 4 hours     |
| 12h      | 12 hours    |
| 1d       | 1 day       |

**Headers**: `Accept-Encoding: identity`

**Example**:
```bash
curl 'https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/dex/market/token/kline/ai?chainId=56&contractAddress=<CONTRACT_ADDRESS>&interval=1d&limit=5' \
  -H 'Accept-Encoding: identity' \
  -H 'User-Agent: binance-web3/1.1 (Skill)'
```

**Response**:

```json
{
  "code": "000000",
  "data": {
    "klineInfos": [
      [1773619200000, "302.935406291919976543", "306.960384694362870577", "302.25959298411397863", "305.249336787737745037", "0", 1773705599999],
      [1773705600000, "305.644964527245747627", "311.890874865402466994", "303.302517784917770672", "311.028506552196415779", "0", 1773791999999]
    ],
    "decimals": 5
  },
  "success": true
}
```

**Candle Array Format** (each element in `data.klineInfos[]`):

| Index | Field     | Type   | Description                 |
|-------|-----------|--------|-----------------------------|
| 0     | openTime  | number | Candle open timestamp (ms)  |
| 1     | open      | string | Open price (USD)            |
| 2     | high      | string | High price (USD)            |
| 3     | low       | string | Low price (USD)             |
| 4     | close     | string | Close price (USD)           |
| 5     | -         | string | Reserved field              |
| 6     | closeTime | number | Candle close timestamp (ms) |

**Response Fields**:

| Field      | Type    | Description                               |
|------------|---------|-------------------------------------------|
| klineInfos | array   | Array of candle arrays (see format above) |
| decimals   | integer | Price decimal precision hint              |

---

## User Agent Header

Include `User-Agent` header with the following string: `binance-web3/1.1 (Skill)`

## Notes

1. **`volume24h` in tokenInfo is misleading**: `tokenInfo.volume24h` from the RWA Dynamic API returns the **US stock daily trading volume in USD**, not the on-chain DEX trading volume. For actual on-chain buy/sell volume, use the Binance on-chain dynamic API (`/market/token/dynamic/info`) with `volume24hBuy` + `volume24hSell` fields instead.

2. **`dividendYield` is a percentage value, not a raw decimal**: A value of `0.27` means 0.27% dividend yield.

3. **Icon and report URLs are relative paths — prepend domain to use**: The API returns relative paths for `icon`, `dailyAttestationReports`, and `monthlyAttestationReports` (e.g. `/images/web3-data/public/token/logos/...`). To construct the full URL, prepend `https://bin.bnbstatic.com`. Example: `/images/web3-data/public/token/logos/<TOKEN_ID>.png` → `https://bin.bnbstatic.com/images/web3-data/public/token/logos/<TOKEN_ID>.png`.

4. **No API key required**: All endpoints are public APIs. No authentication needed.

5. **Multi-chain deployments**: Each supported stock may be deployed on multiple chains (e.g. both Ethereum and BSC). `stockInfo` and `tokenInfo.price` are identical across chains. `tokenInfo.totalHolders` is aggregated cross-chain. `tokenInfo.circulatingSupply` and `tokenInfo.marketCap` are chain-specific.

6. **`multiplier` / `sharesMultiplier` — critical for price comparison**: Each token represents `multiplier` shares of the underlying stock, not exactly 1 share. The multiplier starts at 1.0 and increases over time as cash dividends are reinvested (cumulative dividend adjustment). Some tokens also reflect stock splits (e.g. multiplier = 10.0 means 1 token = 10 shares).

   **Formula**:
   ```
   referencePrice = tokenInfo.price ÷ sharesMultiplier
   ```

   > `tokenInfo.price` and `stockInfo.price` come from different sources (on-chain oracle vs stock feed) and update at different frequencies, so a small premium/discount (typically within ±0.1%) is normal.

   **Common multiplier categories**:

   | Multiplier         | Cause                                                   |
   |--------------------|---------------------------------------------------------|
   | Exactly 1.0        | No dividends paid yet, or newly listed                  |
   | Slightly above 1.0 | Cumulative cash dividend reinvestment (grows over time) |
   | 5.0, 10.0          | Stock split reflected in token structure                |

   > The exact multiplier value changes over time as dividends accumulate. Always read it from the API at query time — never hardcode.
```

## File: `skills/binance-web3/crypto-market-rank/SKILL.md`
```markdown
---
name: crypto-market-rank
description: |
  Crypto market rankings and leaderboards. Query trending tokens, top searched tokens, Binance Alpha tokens,
  tokenized stocks, social hype sentiment ranks, smart money inflow token rankings,
  top meme token rankings from Pulse launchpad, and top trader PnL leaderboards.
  Use this skill when users ask about token rankings, market trends, social buzz, meme rankings, breakout meme tokens, or top traders.
metadata:
  author: binance-web3-team
  version: "2.1"
---

# Crypto Market Rank Skill

## Overview

| API | Function | Use Case |
|-----|----------|----------|
| Social Hype Leaderboard | Social buzz ranking | Sentiment analysis, social summaries |
| Unified Token Rank | Multi-type token rankings | Trending, Top Search, Alpha, Stock with filters |
| Smart Money Inflow Rank | Token rank by smart money buys | Discover tokens smart money is buying most |
| Meme Rank | Top meme tokens from Pulse launchpad | Find meme tokens most likely to break out |
| Address Pnl Rank | Top trader PnL leaderboard | Top PnL traders / KOL performance ranking |

## Use Cases

1. **Social Hype Analysis**: Discover tokens with highest social buzz and sentiment
2. **Trending Tokens**: View currently trending tokens (rankType=10)
3. **Top Searched**: See most searched tokens (rankType=11)
4. **Alpha Discovery**: Browse Binance Alpha picks (rankType=20)
5. **Stock Tokens**: View tokenized stocks (rankType=40)
6. **Smart Money Inflow**: Discover which tokens smart money is buying most
7. **Meme Rank**: Find top meme tokens from Pulse launchpad most likely to break out
8. **PnL Leaderboard**: View top-performing trader addresses, PnL, win rates
9. **Filtered Research**: Combine filters for targeted token or address screening

## Supported Chains

| Chain | chainId |
|-------|---------|
| BSC | 56 |
| Base | 8453 |
| Solana | CT_501 |

---

## API 1: Social Hype Leaderboard

### Method: GET

**URL**:
```
https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/pulse/social/hype/rank/leaderboard/ai
```

**Request Parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| chainId | string | Yes | Chain ID |
| sentiment | string | No | Filter: `All`, `Positive`, `Negative`, `Neutral` |
| targetLanguage | string | Yes | Translation target, e.g., `en`, `zh` |
| timeRange | number | Yes | Time range, `1` = 24 hours |
| socialLanguage | string | No | Content language, `ALL` for all |

**Headers**: `Accept-Encoding: identity`

**Example**:
```bash
curl 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/pulse/social/hype/rank/leaderboard/ai?chainId=56&sentiment=All&socialLanguage=ALL&targetLanguage=en&timeRange=1' \
-H 'Accept-Encoding: identity' \
-H 'User-Agent: binance-web3/2.1 (Skill)'
```

**Response** (`data.leaderBoardList[]`):

| Field Path | Type | Description |
|------------|------|-------------|
| metaInfo.logo | string | Icon URL path (prefix `https://bin.bnbstatic.com`) |
| metaInfo.symbol | string | Token symbol |
| metaInfo.chainId | string | Chain ID |
| metaInfo.contractAddress | string | Contract address |
| metaInfo.tokenAge | number | Creation timestamp (ms) |
| marketInfo.marketCap | number | Market cap (USD) |
| marketInfo.priceChange | number | Price change (%) |
| socialHypeInfo.socialHype | number | Total social hype index |
| socialHypeInfo.sentiment | string | Positive / Negative / Neutral |
| socialHypeInfo.socialSummaryBrief | string | Brief social summary |
| socialHypeInfo.socialSummaryDetail | string | Detailed social summary |
| socialHypeInfo.socialSummaryBriefTranslated | string | Translated brief summary |
| socialHypeInfo.socialSummaryDetailTranslated | string | Translated detailed summary |

---

## API 2: Unified Token Rank

### Method: POST (recommended) / GET

**URL**:
```
https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/pulse/unified/rank/list/ai
```

**Headers**: `Content-Type: application/json`, `Accept-Encoding: identity`

### Rank Types

| rankType | Name | Description |
|----------|------|-------------|
| 10 | Trending | Hot trending tokens |
| 11 | Top Search | Most searched tokens |
| 20 | Alpha | Alpha tokens (Binance Alpha picks) |
| 40 | Stock | Tokenized stock tokens |

### Request Body (all fields optional)

**Core Parameters**:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| rankType | integer | 10 | Rank type: `10`=Trending, `11`=TopSearch, `20`=Alpha, `40`=Stock |
| chainId | string | - | Chain ID: `1`, `56`, `8453`, `CT_501`|
| period | integer | 50 | Time period: `10`=1m, `20`=5m, `30`=1h, `40`=4h, `50`=24h |
| sortBy | integer | 0 | Sort field (see Sort Options) |
| orderAsc | boolean | false | Ascending order if true |
| page | integer | 1 | Page number (min 1) |
| size | integer | 200 | Page size (max 200) |

**Filter Parameters (Min/Max pairs)**:

| Filter | Type | Description |
|--------|------|-------------|
| percentChangeMin/Max | decimal | Price change range (%) |
| marketCapMin/Max | decimal | Market cap range (USD) |
| volumeMin/Max | decimal | Volume range (USD) |
| liquidityMin/Max | decimal | Liquidity range (USD) |
| holdersMin/Max | long | Holder count range |
| holdersTop10PercentMin/Max | decimal | Top10 holder % range |
| kycHoldersMin/Max | long | KYC holder count (Alpha only) |
| countMin/Max | long | Transaction count range |
| uniqueTraderMin/Max | long | Unique trader count range |
| launchTimeMin/Max | long | Token launch time range (timestamp ms) |

**Advanced Filters**:

| Field | Type | Description |
|-------|------|-------------|
| keywords | string[] | Include symbols matching these keywords |
| excludes | string[] | Exclude these symbols |
| socials | integer[] | Social filter: `0`=at_least_one, `1`=X, `2`=Telegram, `3`=Website |
| alphaTagFilter | string[] | Alpha narrative tags |
| auditFilter | integer[] | Audit: `0`=not_renounced, `1`=freezable, `2`=mintable |
| tagFilter | integer[] | Tag filter: `0`=hide_alpha, `23`=dex_paid, `29`=alpha_points, etc. |

### Sort Options

| sortBy | Field |
|--------|-------|
| 0 | Default |
| 1 | Web default |
| 2 | Search count |
| 10 | Launch time |
| 20 | Liquidity |
| 30 | Holders |
| 40 | Market cap |
| 50 | Price change |
| 60 | Transaction count |
| 70 | Volume |
| 80 | KYC holders |
| 90 | Price |
| 100 | Unique traders |

### Example Request

```bash
curl -X POST 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/pulse/unified/rank/list/ai' \
-H 'Content-Type: application/json' \
-H 'Accept-Encoding: identity' \
-H 'User-Agent: binance-web3/2.1 (Skill)' \
-d '{"rankType":10,"chainId":"1","period":50,"sortBy":70,"orderAsc":false,"page":1,"size":20}'
```

### Response

```json
{
  "code": "000000",
  "data": {
    "tokens": [{ "..." }],
    "total": 100,
    "page": 1,
    "size": 20
  },
  "success": true
}
```

**Token Fields** (`data.tokens[]`):

| Field | Type | Description |
|-------|------|-------------|
| chainId | string | Chain ID |
| contractAddress | string | Contract address |
| symbol | string | Token symbol |
| icon | string | Logo URL path (prefix `https://bin.bnbstatic.com`) |
| price | string | Current price (USD) |
| marketCap | string | Market cap |
| liquidity | string | Liquidity |
| holders | string | Holder count |
| launchTime | string | Launch timestamp (ms) |
| decimals | integer | Token decimals |
| links | string | Social links JSON |
| percentChange{1m,5m,1h,4h,24h} | string | Price change by period (%) |
| volume{1m,5m,1h,4h,24h} | string | Volume by period (USD) |
| volume{1m,5m,1h,4h,24h}Buy/Sell | string | Buy/Sell volume by period |
| count{1m,5m,1h,4h,24h} | string | Transaction count by period |
| count{1m,5m,1h,4h,24h}Buy/Sell | string | Buy/Sell tx count by period |
| uniqueTrader{1m,5m,1h,4h,24h} | string | Unique traders by period |
| alphaInfo | object | Alpha info (tagList, description) |
| auditInfo | object | Audit info (riskLevel, riskNum, cautionNum) |
| tokenTag | object | Token tag info |
| kycHolders | string | KYC holder count |
| holdersTop10Percent | string | Top10 holder percentage |

---

## API 3: Smart Money Inflow Rank

### Method: POST

**URL**:
```
https://web3.binance.com/bapi/defi/v1/public/wallet-direct/tracker/wallet/token/inflow/rank/query/ai
```

**Headers**: `Content-Type: application/json`, `Accept-Encoding: identity`

**Request Body**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| chainId | string | Yes | Chain ID: `56` (BSC), `CT_501` (Solana) |
| period | string | No | Stats window: `5m`, `1h`, `4h`, `24h` |
| tagType | integer | Yes | Address tag type (always `2`) |

### Example Request

```bash
curl -X POST 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/tracker/wallet/token/inflow/rank/query/ai' \
-H 'Content-Type: application/json' \
-H 'Accept-Encoding: identity' \
-H 'User-Agent: binance-web3/2.1 (Skill)' \
-d '{"chainId":"56","period":"24h","tagType":2}'
```

### Response (`data[]`)

| Field | Type | Description |
|-------|------|-------------|
| tokenName | string | Token name |
| tokenIconUrl | string | Icon URL path (prefix `https://bin.bnbstatic.com`) |
| ca | string | Contract address |
| price | string | Current price (USD) |
| marketCap | string | Market cap (USD) |
| volume | string | Trading volume in period (USD) |
| priceChangeRate | string | Price change in period (%) |
| liquidity | string | Liquidity (USD) |
| holders | string | Total holder count |
| kycHolders | string | KYC holder count |
| holdersTop10Percent | string | Top10 holder percentage |
| count | string | Transaction count in period |
| countBuy / countSell | string | Buy / Sell tx count |
| inflow | number | Smart money net inflow amount (USD) |
| traders | integer | Number of smart money addresses trading this token |
| launchTime | number | Token launch timestamp (ms) |
| tokenDecimals | integer | Token decimals |
| tokenRiskLevel | integer | Risk level (-1=unknown, 1=low, 2=medium, 3=high) |
| link | array | Social links: `[{label, link}]` |
| tokenTag | object | Token tags by category |

---

## API 4: Meme Rank

### Method: GET

**URL**:
```
https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/pulse/exclusive/rank/list/ai
```

**Headers**: `Accept-Encoding: identity`

**Request Parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| chainId | string | Yes | Chain ID: `56` (BSC) |

Returns top 100 meme tokens launched via Pulse platform, scored and ranked by an algorithm evaluating breakout potential.

### Example Request

```bash
curl 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/pulse/exclusive/rank/list/ai?chainId=56' \
-H 'Accept-Encoding: identity' \
-H 'User-Agent: binance-web3/2.1 (Skill)'
```

### Response (`data.tokens[]`)

| Field | Type | Description |
|-------|------|-------------|
| chainId | string | Chain ID |
| contractAddress | string | Contract address |
| symbol | string | Token symbol |
| rank | integer | Rank position |
| score | string | Algorithm score (higher = more likely to break out) |
| alphaStatus | integer | Alpha listing status |
| price | string | Current price (USD) |
| percentChange | string | Price change (%) |
| percentChange7d | string | 7-day price change (%) |
| marketCap | string | Market cap (USD) |
| liquidity | string | Liquidity (USD) |
| volume | string | Total volume (USD) |
| volumeBnTotal | string | Binance user total volume |
| volumeBn7d | string | Binance user 7-day volume |
| holders | string | Total holder count |
| kycHolders | string | KYC holder count |
| bnUniqueHolders | string | Binance unique holder count |
| holdersTop10Percent | string | Top10 holder percentage |
| count | integer | Total transaction count |
| countBnTotal | integer | Binance user total tx count |
| countBn7d | integer | Binance user 7-day tx count |
| uniqueTraderBn | integer | Binance unique traders |
| uniqueTraderBn7d | integer | Binance 7-day unique traders |
| impression | integer | Impression/view count |
| createTime | number | Token creation timestamp (ms) |
| migrateTime | number | Migration timestamp (ms) |
| metaInfo.icon | string | Icon URL path (prefix `https://bin.bnbstatic.com`) |
| metaInfo.name | string | Token full name |
| metaInfo.decimals | integer | Token decimals |
| metaInfo.aiNarrativeFlag | integer | AI narrative flag (1=yes) |
| previewLink | object | Social links: `{website[], x[], telegram[]}` |
| tokenTag | object | Token tags by category |

---

## API 5: Address Pnl Rank

### Method: GET

**URL**:
```
https://web3.binance.com/bapi/defi/v1/public/wallet-direct/market/leaderboard/query/ai
```

**Headers**: `Accept-Encoding: identity`

**Request Parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| chainId | string | Yes | Chain ID: `56` (BSC), `CT_501` (Solana) |
| period | string | Yes | Time period: `7d`, `30d`, `90d` |
| tag | string | Yes | Address tag filter: `ALL`, `KOL` |
| sortBy | integer | No | Sort field |
| orderBy | integer | No | Order direction |
| pageNo | integer | No | Page number (min 1) |
| pageSize | integer | No | Page size (max 25) |

**Filter Parameters (Min/Max pairs)**:

| Filter | Type | Description |
|--------|------|-------------|
| PNLMin/Max | decimal | Realized PnL range (USD) |
| winRateMin/Max | decimal | Win rate range (percentage, e.g. `1` = 1%) |
| txMin/Max | long | Transaction count range |
| volumeMin/Max | decimal | Volume range (USD) |

### Example Request

```bash
curl 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/market/leaderboard/query/ai?tag=ALL&pageNo=1&chainId=CT_501&pageSize=25&sortBy=0&orderBy=0&period=30d' \
-H 'Accept-Encoding: identity' \
-H 'User-Agent: binance-web3/2.1 (Skill)'
```

### Response

```json
{
  "code": "000000",
  "data": {
    "data": [{ "..." }],
    "current": 1,
    "size": 25,
    "pages": 35
  },
  "success": true
}
```

**Address Fields** (`data.data[]`):

| Field | Type | Description |
|-------|------|-------------|
| address | string | Wallet address |
| addressLogo | string | Address avatar URL |
| addressLabel | string | Address display name |
| balance | string | On-chain balance (native token, e.g. SOL/BNB) |
| tags | array | Address tags (e.g. KOL) |
| realizedPnl | string | Realized PnL for the period (USD) |
| realizedPnlPercent | string | Realized PnL percentage |
| dailyPNL | array | Daily PnL list: `[{realizedPnl, dt}]` |
| winRate | string | Win rate for the period |
| totalVolume | string | Total trading volume (USD) |
| buyVolume / sellVolume | string | Buy / Sell volume |
| avgBuyVolume | string | Average buy amount |
| totalTxCnt | integer | Total transaction count |
| buyTxCnt / sellTxCnt | integer | Buy / Sell transaction count |
| totalTradedTokens | integer | Number of tokens traded |
| topEarningTokens | array | Top profit tokens: `[{tokenAddress, tokenSymbol, tokenUrl, realizedPnl, profitRate}]` |
| tokenDistribution | object | PnL distribution: `{gt500Cnt, between0And500Cnt, between0AndNegative50Cnt, ltNegative50Cnt}` |
| lastActivity | number | Last active timestamp (ms) |
| genericAddressTagList | array | Detailed tag info (tagName, logoUrl, extraInfo) |

---

## User Agent Header

Include `User-Agent` header with the following string: `binance-web3/2.1 (Skill)`

## Notes

1. Icon/logo URLs require prefix: `https://bin.bnbstatic.com` + path
2. Unified Token Rank supports both GET and POST; POST is recommended
3. All numeric fields in responses are strings — parse when needed
4. Period fields use shorthand: `{1m,5m,1h,4h,24h}` means separate fields like `percentChange1m`, `percentChange5m`, etc.
```

## File: `skills/binance-web3/meme-rush/SKILL.md`
```markdown
---
name: meme-rush
description: |
  Meme token fast-trading assistant with two core capabilities:
  1. Meme Rush - Real-time meme token lists from launchpads (Pump.fun, Four.meme, etc.) across new, finalizing, and migrated stages
  2. Topic Rush - AI-powered market hot topics with associated tokens ranked by net inflow
  Use this skill when users ask about new meme tokens, meme launches, bonding curve, migration status,
  pump.fun tokens, four.meme tokens, fast meme trading, market hot topics, or trending narratives.
metadata:
  author: binance-web3-team
  version: "1.1"
---

# Meme Rush Skill

## Overview

### Meme Rush — Launchpad token lifecycle tracking

| rankType | Stage | Description |
|----------|-------|-------------|
| 10 | New | Freshly created meme tokens still on bonding curve |
| 20 | Finalizing | Tokens about to migrate (bonding curve nearly complete) |
| 30 | Migrated | Tokens that just migrated to DEX |

### Topic Rush — AI-powered market hot topic discovery

| rankType | Stage | Description |
|----------|-------|-------------|
| 10 | Latest | Newest hot topics |
| 20 | Rising | Rising topics with all-time high inflow between $1k–$20k |

## Use Cases

1. **Snipe New Launches**: Find freshly created meme tokens on Pump.fun, Four.meme, etc.
2. **Migration Watch**: Monitor tokens about to migrate — catch early DEX liquidity
3. **Post-Migration Trading**: Find just-migrated tokens for early DEX entry
4. **Filter by Dev Behavior**: Exclude dev wash trading, check dev sell %, burned tokens
5. **Holder Analysis**: Filter by top10 %, dev %, sniper %, insider %, bundler % holdings
6. **Smart Filtering**: Combine bonding curve progress, liquidity, volume, market cap filters
7. **Topic Discovery**: Find AI-generated market hot topics and their associated tokens
8. **Narrative Trading**: Trade tokens grouped by trending narratives, sorted by net inflow

## Supported Chains

| Chain | chainId |
|-------|---------|
| BSC | 56 |
| Solana | CT_501 |

## Protocol Reference

| Protocol Code | Platform | Chain |
|---------------|----------|-------|
| 1001 | Pump.fun | Solana |
| 1002 | Moonit | Solana |
| 1003 | Pump AMM | Solana |
| 1004 | Launch Lab | Solana |
| 1005 | Raydium V4 | Solana |
| 1006 | Raydium CPMM | Solana |
| 1007 | Raydium CLMM | Solana |
| 1008 | BONK | Solana |
| 1009 | Dynamic BC | Solana |
| 1010 | Moonshot | Solana |
| 1011 | Jup Studio | Solana |
| 1012 | Bags | Solana |
| 1013 | Believer | Solana |
| 1014 | Meteora DAMM V2 | Solana |
| 1015 | Meteora Pools | Solana |
| 1016 | Orca | Solana |
| 2001 | Four.meme | BSC |
| 2002 | Flap | BSC |

---

## API 1: Meme Rush Rank List

### Method: POST

**URL**:
```
https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/pulse/rank/list/ai
```

**Headers**: `Content-Type: application/json`, `Accept-Encoding: identity`

### Request Body

**Required Parameters**:

| Field | Type | Description |
|-------|------|-------------|
| chainId | string | Chain ID: `56` for bsc, `CT_501` for solana |
| rankType | integer | `10`=New, `20`=Finalizing, `30`=Migrated |

**Pagination & Keyword**:

| Field | Type | Description |
|-------|------|-------------|
| limit | integer | Max results per request (default 40, max 200) |
| keywords | string[] | Include symbols matching keywords (max 5) |
| excludes | string[] | Exclude symbols (max 5) |

**Token Filters (Min/Max pairs)**:

| Filter | Type | Description |
|--------|------|-------------|
| progressMin/Max | string | Bonding curve progress (0-100%) |
| tokenAgeMin/Max | long | Token age |
| holdersMin/Max | long | Holder count |
| liquidityMin/Max | string | Liquidity (USD) |
| volumeMin/Max | string | 24h volume (USD) |
| marketCapMin/Max | string | Market cap (USD) |
| countMin/Max | long | Total trade count |
| countBuyMin/Max | long | Buy trade count |
| countSellMin/Max | long | Sell trade count |

**Holder Distribution Filters (Min/Max pairs)**:

| Filter | Type | Description |
|--------|------|-------------|
| holdersTop10PercentMin/Max | string | Top10 holder % |
| holdersDevPercentMin/Max | string | Dev holder % |
| holdersSniperPercentMin/Max | string | Sniper holder % |
| holdersInsiderPercentMin/Max | string | Insider holder % |
| bundlerHoldingPercentMin/Max | string | Bundler holder % |
| newWalletHoldingPercentMin/Max | string | New wallet holder % |
| bnHoldingPercentMin/Max | string | Binance wallet holder % |
| bnHoldersMin/Max | long | Binance wallet holder count |
| kolHoldersMin/Max | long | KOL holder count |
| proHoldersMin/Max | long | Pro holder count |

**Dev & Launch Filters**:

| Field | Type | Description |
|-------|------|-------------|
| devMigrateCountMin/Max | long | Dev historical migration count |
| devPosition | integer | Dev position: `2`=dev sold all (pass when checked) |
| devBurnedToken | integer | Dev burned tokens: `1`=yes |
| excludeDevWashTrading | integer | Exclude dev wash trading: `1`=yes |
| excludeInsiderWashTrading | integer | Exclude insider wash trading: `1`=yes |

**Other Filters**:

| Field | Type | Description |
|-------|------|-------------|
| protocol | integer[] | Launchpad protocol codes (see Protocol Reference) |
| exclusive | integer | Binance exclusive token: `0`=no, `1`=yes |
| paidOnDexScreener | integer | Paid on DexScreener |
| pumpfunLiving | integer | Pump.fun live stream: `1`=yes |
| cmcBoost | integer | CMC paid boost: `1`=yes |
| globalFeeMin/Max | string | Trading fee (Solana only) |
| pairAnchorAddress | string[] | Quote token addresses |
| tokenSocials.atLeastOne | integer | Has at least one social: `1`=yes |
| tokenSocials.socials | string[] | Specific socials: `website`, `twitter`, `telegram` |

### Example Request

```bash
curl -X POST 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/pulse/rank/list/ai' \
-H 'Content-Type: application/json' \
-H 'Accept-Encoding: identity' \
-H 'User-Agent: binance-web3/1.1 (Skill)' \
-d '{"chainId":"CT_501","rankType":10,"limit":20}'
```

### Response (`data[]`)

**Core Fields**:

| Field | Type | Description |
|-------|------|-------------|
| chainId | string | Chain ID |
| contractAddress | string | Contract address |
| symbol | string | Token symbol |
| name | string | Token name |
| decimals | integer | Token decimals |
| icon | string | Logo URL (prefix `https://bin.bnbstatic.com`) |
| price | string | Current price (USD) |
| priceChange | string | 24h price change (%) |
| marketCap | string | Market cap (USD) |
| liquidity | string | Liquidity (USD) |
| volume | string | 24h volume (USD) |
| holders | long | Holder count |
| progress | string | Bonding curve progress (%, append `%` directly) |
| protocol | integer | Launchpad protocol code |
| exclusive | integer | Binance exclusive: 0/1 |

**Trade Counts**:

| Field | Type | Description |
|-------|------|-------------|
| count | long | 24h total trades |
| countBuy | long | 24h buy trades |
| countSell | long | 24h sell trades |

**Holder Distribution** (all string, already in %, append `%` directly):

| Field | Description |
|-------|-------------|
| holdersTop10Percent | Top10 holders % |
| holdersDevPercent | Dev holders % |
| holdersSniperPercent | Sniper holders % |
| holdersInsiderPercent | Insider holders % |
| bnHoldingPercent | Binance wallet holders % |
| kolHoldingPercent | KOL holders % |
| proHoldingPercent | Pro holders % |
| newWalletHoldingPercent | New wallet holders % |
| bundlerHoldingPercent | Bundler holders % |

**Dev & Migration Info**:

| Field | Type | Description |
|-------|------|-------------|
| devAddress | string | Dev wallet address |
| devSellPercent | string | Dev sell % |
| devMigrateCount | long | Dev historical migration count |
| devPosition | integer | `2`=dev sold all position |
| migrateStatus | integer | `0`=not migrated, `1`=migrated |
| migrateTime | long | Migration timestamp (ms) |
| createTime | long | Token creation timestamp (ms) |

**Tags & Flags**:

| Field | Type | Description |
|-------|------|-------------|
| tagDevWashTrading | integer | Dev wash trading: 1=yes |
| tagInsiderWashTrading | integer | Insider wash trading: 1=yes |
| tagDevBurnedToken | integer | Dev burned tokens: 1=yes |
| tagPumpfunLiving | integer | Pump.fun live: 1=yes |
| tagCmcBoost | integer | CMC paid: 1=yes |
| paidOnDexScreener | integer | DexScreener paid: 1=yes |
| launchTaxEnable | integer | Has launch tax: 1=yes |
| taxRate | string | Trading tax rate (%) |
| globalFee | string | Trading fee (Solana only) |

**Social Links**:

| Field | Type | Description |
|-------|------|-------------|
| socials.website | string | Website URL |
| socials.twitter | string | Twitter URL |
| socials.telegram | string | Telegram URL |

**AI Narrative**:

| Field | Type | Description |
|-------|------|-------------|
| narrativeText.en | string | AI narrative (English) |
| narrativeText.cn | string | AI narrative (Chinese) |

---

## API 2: Topic Rush Rank List

### Method: GET

**URL**:
```
https://web3.binance.com/bapi/defi/v2/public/wallet-direct/buw/wallet/market/token/social-rush/rank/list/ai
```

**Headers**: `Accept-Encoding: identity`

### Request Parameters

**Required Parameters**:

| Field | Type | Description |
|-------|------|-------------|
| chainId | string | Chain ID: `56`, `CT_501` |
| rankType | integer | `10`=Latest, `20`=Rising |
| sort | integer | Sort by: `10`=create time, `20`=net inflow |

> **Sort convention**: When the user does not specify a sort preference, use `sort=10` (create time) for Latest/Rising.

**Optional Parameters**:

| Field | Type | Description |
|-------|------|-------------|
| asc | boolean | `true`=ascending, `false`=descending |
| keywords | string | Keyword filter (case-insensitive, contains match) |
| topicType | string | Topic type filter, comma-separated for multiple |
| tokenSizeMin/Max | integer | Associated token count range |
| netInflowMin/Max | string | Topic net inflow range (USD) |

### Example Request

```bash
curl 'https://web3.binance.com/bapi/defi/v2/public/wallet-direct/buw/wallet/market/token/social-rush/rank/list/ai?chainId=CT_501&rankType=10&sort=10&asc=false' \
-H 'Accept-Encoding: identity' \
-H 'User-Agent: binance-web3/1.1 (Skill)'
```

### Response (`data[]`)

**Topic Fields**:

| Field | Type | Description |
|-------|------|-------------|
| topicId | string | Topic unique ID |
| chainId | string | Chain ID |
| name | object | Multi-language topic name (`topicNameEn`, `topicNameCn`, etc.) |
| type | string | Topic type/category |
| close | integer | Topic closed: `0`=no, `1`=yes |
| topicLink | string | Related tweet/post URL |
| createTime | long | Topic creation timestamp (ms) |
| progress | string | Topic progress (pre-formatted %, append `%` directly) |
| aiSummary | object | AI-generated topic narrative |
| topicNetInflow | string | Total net inflow (USD) |
| topicNetInflow1h | string | 1h net inflow (USD) |
| topicNetInflowAth | string | All-time high net inflow (USD) |
| tokenSize | integer | Number of associated tokens |
| deepAnalysisFlag | integer | Deep analysis available: `1`=yes |

**Token List** (`tokenList[]` within each topic):

| Field | Type | Description |
|-------|------|-------------|
| chainId | string | Chain ID |
| contractAddress | string | Contract address |
| symbol | string | Token symbol |
| icon | string | Logo URL (prefix `https://bin.bnbstatic.com`) |
| decimals | integer | Token decimals |
| createTime | long | Token creation timestamp (ms) |
| marketCap | string | Market cap (USD) |
| liquidity | string | Liquidity (USD) |
| priceChange24h | string | 24h price change (pre-formatted %, append `%`) |
| netInflow | string | Token net inflow since topic creation (USD) |
| netInflow1h | string | Token 1h net inflow (USD) |
| volumeBuy / volumeSell | string | Buy / Sell volume since topic creation (USD) |
| volume1hBuy / volume1hSell | string | 1h buy / sell volume (USD) |
| uniqueTrader{5m,1h,4h,24h} | long | Unique traders by period |
| count{5m,1h,4h,24h} | long | Trade count by period |
| holders | long | Holder count |
| kolHolders | long | KOL holder count |
| smartMoneyHolders | long | Smart money holder count |
| protocol | integer | Launchpad protocol code (`0`/null = DEX token) |
| internal | integer | On bonding curve: `0`=no, `1`=yes |
| migrateStatus | integer | Migrated: `0`=no, `1`=yes |

---

## User Agent Header

Include `User-Agent` header with the following string: `binance-web3/1.1 (Skill)`

## Notes

1. Only `chainId` and `rankType` are required; all other parameters are optional filters
2. Percentage fields (progress, holder %, dev sell %, tax rate) are pre-formatted — append `%` directly
3. `taxRate` for protocol=2001 (Four.meme) only shows on Migrated list; for protocol=2002 (Flap) shows on all lists
4. Icon URLs require prefix: `https://bin.bnbstatic.com` + path
```

## File: `skills/binance-web3/query-address-info/SKILL.md`
```markdown
---
name: query-address-info
description: |
  Query any on-chain wallet address token balances and positions. Retrieves all token holdings for a specified wallet address on a given chain,
  including token name, symbol, price, 24h price change, and holding quantity.
  Use this skill when users ask about wallet balance, token holds, portfolio, or asset positions for any blockchain address.
metadata:
  author: binance-web3-team
  version: "1.1"
---

# Query Address Info Skill

## Overview

This skill queries any on-chain wallet address for token holdings, supporting:
- List of all tokens held by a wallet address
- Current price of each token
- 24-hour price change percentage
- Holding quantity

## API Endpoint

### Query Wallet Token Balance

**Method**: GET

**URL**: 
```
https://web3.binance.com/bapi/defi/v3/public/wallet-direct/buw/wallet/address/pnl/active-position-list/ai
```

**Request Parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| address | string | Yes | Wallet address, e.g., `0x0000000000000000000000000000000000000001` |
| chainId | string | Yes | Chain ID, e.g., `56` (BSC), `8453` (Base) |
| offset | number | Yes | Pagination offset, default 0 |

**Request Headers**:
```
clienttype: web
clientversion: 1.2.0
Accept-Encoding: identity
User-Agent: binance-web3/1.1 (Skill)
```

**Example Request**:
```bash
curl --location 'https://web3.binance.com/bapi/defi/v3/public/wallet-direct/buw/wallet/address/pnl/active-position-list/ai?address=0x0000000000000000000000000000000000000001&chainId=56&offset=0' \
--header 'clienttype: web' \
--header 'clientversion: 1.2.0' \
--header 'Accept-Encoding: identity' \
--header 'User-Agent: binance-web3/1.1 (Skill)'
```

**Response Example**:
```json
{
    "code": "000000",
    "message": null,
    "messageDetail": null,
    "data": {
        "offset": 0,
        "addressStatus": null,
        "list": [
            {
                "chainId": "56",
                "address": "0x0000000000000000000000000000000000000001",
                "contractAddress": "token contract address",
                "name": "name of token",
                "symbol": "symbol of token",
                "icon": "/images/web3-data/public/token/logos/xxxx.png",
                "decimals": 18,
                "price": "0.0000045375251839978",
                "percentChange24h": "6.84",
                "remainQty": "20"
            }
        ]
    },
    "success": true
}
```

**Response Fields**:

| Field | Type | Description |
|-------|------|-------------|
| chainId | string | Chain ID |
| address | string | Wallet address |
| contractAddress | string | Token contract address |
| name | string | Token name |
| symbol | string | Token symbol |
| icon | string | Token icon URL path |
| decimals | number | Token decimals |
| price | string | Current price (USD) |
| percentChange24h | string | 24-hour price change (%) |
| remainQty | string | Holding quantity |

## Supported Chains

| Chain Name | chainId |
|------------|---------|
| BSC | 56 |
| Base | 8453 |
| Solana | CT_501 |

## Use Cases

1. **Query Wallet Assets**: When users want to view tokens held by a wallet address
2. **Track Holdings**: Monitor wallet token positions
3. **Portfolio Analysis**: Understand wallet asset allocation

## User Agent Header

Include `User-Agent` header with the following string: `binance-web3/1.1 (Skill)`

## Notes

1. Icon URL requires full domain prefix: `bin.bnbstatic.com` + icon path
2. Price and quantity are string format, convert to numbers when using
3. Use offset parameter for pagination
```

## File: `skills/binance-web3/query-token-audit/SKILL.md`
```markdown
---
name: query-token-audit
description: |
  Query token security audit to detect scams, honeypots, and malicious contracts before trading.
  Returns comprehensive security analysis including contract risks, trading risks, and scam detection.
  Use when users ask "is this token safe?", "check token security", "audit token", or before any swap.
metadata:
  author: binance-web3-team
  version: "1.4"
---

# Query Token Audit Skill

## Overview

| API | Function            | Use Case |
|-----|---------------------|----------|
| Token Security Audit | Token security scan | Detect honeypot, rug pull, scam, malicious functions |

## Use Cases

1. **Pre-Trade Safety Check**: Verify token security before buying or swapping
2. **Scam Detection**: Identify honeypots, fake tokens, and malicious contracts
3. **Contract Analysis**: Check for dangerous ownership functions and hidden risks
4. **Tax Verification**: Detect unusual buy/sell taxes before trading

## Supported Chains

| Chain Name | chainId |
|------------|---------|
| BSC | 56 |
| Base | 8453 |
| Solana | CT_501 |
| Ethereum | 1 |

---

## API: Token Security Audit

### Method: POST

**URL**: 
```
https://web3.binance.com/bapi/defi/v1/public/wallet-direct/security/token/audit
```

**Request Parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| binanceChainId | string | Yes | Chain ID: `CT_501` (Solana), `56` (BSC), `8453` (Base), `1` (Ethereum) |
| contractAddress | string | Yes | Token contract address |
| requestId | string | Yes | Unique request ID (UUID v4 format) |

**Request Headers**:
```
Content-Type: application/json
Accept-Encoding: identity
User-Agent: binance-web3/1.4 (Skill)
```

**Example Request**:
```bash
curl --location 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/security/token/audit' \
--header 'Content-Type: application/json' \
--header 'source: agent' \
--header 'Accept-Encoding: identity' \
--header 'User-Agent: binance-web3/1.4 (Skill)' \
--data '{
    "binanceChainId": "56",
    "contractAddress": "0x55d398326f99059ff775485246999027b3197955",
    "requestId": "'$(uuidgen)'"
}'
```

**Response Example**:
```json
{
    "code": "000000",
    "data": {
        "requestId": "d6727c70-de6c-4fad-b1d7-c05422d5f26b",
        "hasResult": true,
        "isSupported": true,
        "riskLevelEnum": "LOW",
        "riskLevel": 1,
        "extraInfo": {
            "buyTax": "0",
            "sellTax": "0",
            "isVerified": true
        },
        "riskItems": [
            {
                "id": "CONTRACT_RISK",
                "name": "Contract Risk",
                "details": [
                    {
                        "title": "Honeypot Risk Not Found",
                        "description": "A honeypot is a token that can be bought but not sold",
                        "isHit": false,
                        "riskType": "RISK"
                    }
                ]
            }
        ]
    },
    "success": true
}
```

**Response Fields**:

| Field                             | Type | Description                                               |
|-----------------------------------|------|-----------------------------------------------------------|
| hasResult                         | boolean | Whether audit data is available                           |
| isSupported                       | boolean | Whether the token is supported for audit                  |
| riskLevelEnum                     | string | Risk level: `LOW`, `MEDIUM`, `HIGH`                       |
| riskLevel                         | number | Risk level number (1-5)                                   |
| extraInfo.buyTax                  | string | Buy tax percentage (null if unknown)                      |
| extraInfo.sellTax                 | string | Sell tax percentage (null if unknown)                     |
| extraInfo.isVerified              | boolean | Whether contract code is verified                         |
| riskItems[].id                    | string | Risk category: `CONTRACT_RISK`, `TRADE_RISK`, `SCAM_RISK` |
| riskItems[].details[].title       | string | Risk check title                                          |
| riskItems[].details[].description | string | Risk check description                                    |
| riskItems[].details[].isHit       | boolean | true = risk detected                                      |
| riskItems[].details[].riskType    | string | `RISK` (critical) or `CAUTION` (warning)                  |

**Risk Level Reference**:

| riskLevel | riskLevelEnum | Action | Description |
|-----------|---------------|--------|-------------|
| 0-1 | LOW | Proceed with caution | Lower risk detected, but NOT guaranteed safe. DYOR. |
| 2-3 | MEDIUM | Exercise caution | Moderate risks detected, review risk items carefully |
| 4 | HIGH | Avoid trading | Critical risks detected, high probability of loss |
| 5 | HIGH | Block transaction | Severe risks confirmed, do NOT proceed |

**IMPORTANT**: LOW risk does NOT mean "safe." Audit results are point-in-time snapshots. Project teams can modify contracts or restrict liquidity after purchase. These risks cannot be predicted in advance.

**Response Handling**:

- If `hasResult=false` OR `isSupported=false`:
  → Reply: "Security audit data is not available for this token on this chain."
  → Do NOT show `riskLevel`, `riskLevelEnum`, or `riskItems` (data is unreliable when either field is false)
  → You may suggest the user verify the contract address and chain, or try again later
- If `hasResult=true` AND `isSupported=true`:
  → Show the full audit result including risk level, tax info, and all risk items
  → Apply the Risk Level Reference table above for actionable guidance

---

## User Agent Header

Include `User-Agent` header with the following string: `binance-web3/1.4 (Skill)`

## Notes

1. All numeric fields are string format, convert when using
2. Audit results are ONLY valid when `hasResult: true` AND `isSupported: true`
3. `riskLevel: 5` means transaction should be blocked; `riskLevel: 4` is high risk
4. Tax thresholds: >10% is critical, 5-10% is warning, <5% is acceptable
5. Generate unique UUID v4 for each audit request
6. Only output security check risk flags, do NOT provide any investment advice 
7. Always end with disclaimer: `⚠️ This audit result is for reference only and does not constitute investment advice. Always conduct your own research.`
```

## File: `skills/binance-web3/query-token-info/SKILL.md`
```markdown
---
name: query-token-info
description: |
  Query token details by keyword, contract address, or chain. Search tokens, get metadata and social links,
  retrieve real-time market data (price, price trend, volume, holders, liquidity), and fetch K-Line candlestick charts.
  Use this skill when users search tokens, check token prices, view market data, or request kline/candlestick charts.
metadata:
  author: binance-web3-team
  version: "1.1"
---

# Query Token Info Skill

## Overview

| API | Function | Use Case |
|-----|----------|----------|
| Token Search | Search tokens | Find tokens by name, symbol, or contract address |
| Token Metadata | Static info | Get token details,name,symbol,logo, social links, creator address |
| Token Dynamic Data | Real-time market data | Price, volume, holders, liquidity, market cap |
| Token K-Line | Candlestick charts | OHLCV data for technical analysis |

## Use Cases

1. **Search Tokens**: Find tokens by name, symbol, or contract address across chains
2. **Project Research**: Get token metadata, social links, and creator info
3. **Market Analysis**: Real-time price, volume, holder distribution, and liquidity data
4. **Chart Analysis**: K-Line candlestick data for technical analysis

## Supported Chains

| Chain Name | chainId |
|------------|---------|
| BSC | 56 |
| Base | 8453 |
| Solana | CT_501 |

---

## API 1: Token Search

### Method: GET

**URL**: 
```
https://web3.binance.com/bapi/defi/v5/public/wallet-direct/buw/wallet/market/token/search/ai
```

**Request Parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| keyword | string | Yes | Search keyword (name/symbol/contract address) |
| chainIds | string | No | Chain ID list, comma-separated, e.g., `56,8453,CT_501` |
| orderBy | string | No | Sort field, e.g., `volume24h` |

**Request Headers**:
```
Accept-Encoding: identity
User-Agent: binance-web3/1.1 (Skill)
```

**Example Request**:
```bash
curl --location 'https://web3.binance.com/bapi/defi/v5/public/wallet-direct/buw/wallet/market/token/search/ai?keyword=xxx&chainIds=56,8453,CT_501&orderBy=volume24h' \
--header 'Accept-Encoding: identity' \
--header 'User-Agent: binance-web3/1.1 (Skill)'
```

**Response Example**:
```json
{
    "code": "000000",
    "data": [
        {
            "chainId": "56",
            "contractAddress": "0x1234...",
            "tokenId": "CC1F457...",
            "name": "Token",
            "symbol": "symbol of token",
            "icon": "/images/web3-data/public/token/logos/xxx.png",
            "price": "47.98771375939603199404",
            "percentChange24h": "-0.01",
            "volume24h": "53687246.955803546359104902201",
            "marketCap": "162198400",
            "liquidity": "13388877.147327333572157",
            "tokenAddresses": [...],
            "tagsInfo": {
                "AI Analysis": [{"tagName": "AI Widget", "languageKey": "wmp-label-title-ai-widget"}],
                "Community Recognition Level": [{"tagName": "Alpha", "languageKey": "wmp-label-title-alpha"}]
            },
            "links": [
                {"label": "website", "link": "https://www.web.site/"},
                {"label": "x", "link": "https://twitter.com/..."}
            ],
            "createTime": 1600611727000,
            "holdersTop10Percent": "93.267178480644823",
            "riskLevel": null
        }
    ],
    "success": true
}
```

**Response Fields**:

| Field | Type | Description |
|-------|------|-------------|
| chainId | string | Chain ID |
| contractAddress | string | Contract address |
| tokenId | string | Token unique ID |
| name | string | Token name |
| symbol | string | Token symbol |
| icon | string | Icon URL path |
| price | string | Current price (USD) |
| percentChange24h | string | 24-hour price change (%) |
| volume24h | string | 24-hour trading volume (USD) |
| marketCap | string | Market cap (USD) |
| liquidity | string | Liquidity (USD) |
| tagsInfo | object | Tag information |
| links | array | Social links list |
| createTime | number | Creation timestamp (ms) |
| holdersTop10Percent | string | Top 10 holders percentage (%) |

---

## API 2: Token Metadata

### Method: GET

**URL**: 
```
https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/dex/market/token/meta/info/ai
```

**Request Parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| chainId | string | Yes | Chain ID |
| contractAddress | string | Yes | Token contract address |

**Request Headers**:
```
Accept-Encoding: identity
User-Agent: binance-web3/1.1 (Skill)
```

**Example Request**:
```bash
curl --location 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/dex/market/token/meta/info/ai?chainId=56&contractAddress=0x55d398326f99059ff775485246999027b3197955' \
--header 'Accept-Encoding: identity' \
--header 'User-Agent: binance-web3/1.1 (Skill)'
```

**Response Example**:
```json
{
    "code": "000000",
    "data": {
        "tokenId": "CC1F457B",
        "name": "name of Token",
        "symbol": "symbol of token",
        "chainId": "56",
        "chainIconUrl": "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20250228/d0216ce4-a3e9-4bda-8937-4a6aa943ccf2.png",
        "chainName": "BSC",
        "contractAddress": "0x55d398326f99059ff775485246999027b3197955",
        "decimals": 18,
        "icon": "/images/web3-data/public/token/logos/xxx.png",
        "nativeAddressFlag": false,
        "aiNarrativeFlag": 1,
        "links": [
            {"label": "website", "link": "https://www.web.site/"},
            {"label": "whitepaper", "link": "https://drive.google.com/file/d/..."},
            {"label": "x", "link": "https://twitter.com/..."}
        ],
        "previewLink": {
            "website": ["https://www.web.site/"],
            "x": ["https://twitter.com/..."],
            "tg": []
        },
        "createTime": 1600611727000,
        "creatorAddress": "0x1234...",
        "auditInfo": {
            "isBlacklist": false,
            "isWhitelist": true
        },
        "description": "this is a good token..."
    },
    "success": true
}
```

**Response Fields**:

| Field | Type | Description |
|-------|------|-------------|
| tokenId | string | Token unique ID |
| name | string | Token name |
| symbol | string | Token symbol |
| chainId | string | Chain ID |
| chainName | string | Chain name |
| contractAddress | string | Contract address |
| decimals | number | Token decimals |
| icon | string | Icon URL path |
| links | array | Social links list |
| createTime | number | Creation timestamp (ms) |
| creatorAddress | string | Creator address |
| description | string | Token description |

---

## API 3: Token Dynamic Data

### Method: GET

**URL**: 
```
https://web3.binance.com/bapi/defi/v4/public/wallet-direct/buw/wallet/market/token/dynamic/info/ai
```

**Request Parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| chainId | string | Yes | Chain ID |
| contractAddress | string | Yes | Token contract address |

**Request Headers**:
```
Accept-Encoding: identity
User-Agent: binance-web3/1.1 (Skill)
```

**Example Request**:
```bash
curl --location 'https://web3.binance.com/bapi/defi/v4/public/wallet-direct/buw/wallet/market/token/dynamic/info/ai?chainId=56&contractAddress=0x55d398326f99059ff775485246999027b3197955' \
--header 'Accept-Encoding: identity' \
--header 'User-Agent: binance-web3/1.1 (Skill)'
```

**Response Example**:
```json
{
    "code": "000000",
    "data": {
        "price": "48.00617218672732466029",
        "nativeTokenPrice": "589.09115969567768209591",
        "volume24h": "53803143.235015073706599196363",
        "volume24hBuy": "26880240.472839229350983682189",
        "volume24hSell": "26922902.762175844355615514174",
        "volume4h": "7179919.170580971950485838372",
        "volume1h": "3181854.878039371691111933489",
        "volume5m": "84557.068962077549412188792",
        "count24h": "39869",
        "count24hBuy": "19850",
        "count24hSell": "20019",
        "percentChange5m": "0.03",
        "percentChange1h": "0.02",
        "percentChange4h": "0.03",
        "percentChange24h": "0.01",
        "marketCap": "162260777.94315716831842935701774977509483735135",
        "totalSupply": "3379998.56",
        "circulatingSupply": "3379998.249225519124584315",
        "priceHigh24h": "48.59526604943723770716",
        "priceLow24h": "47.4815509902145490401",
        "holders": "78255",
        "fdv": "162260792.8622504084644326891824",
        "liquidity": "13393863.149264026822944",
        "launchTime": 1600950241000,
        "top10HoldersPercentage": "93.2621248736909194",
        "kycHolderCount": "23579",
        "kolHolders": "17",
        "kolHoldingPercent": "0.000059",
        "proHolders": "138",
        "proHoldingPercent": "0.003357",
        "smartMoneyHolders": "1",
        "smartMoneyHoldingPercent": "0"
    },
    "success": true
}
```

**Response Fields**:

### Price Related
| Field | Type | Description |
|-------|------|-------------|
| price | string | Current price (USD) |
| nativeTokenPrice | string | Native token price |
| priceHigh24h | string | 24-hour high price |
| priceLow24h | string | 24-hour low price |

### Price Change
| Field | Type | Description |
|-------|------|-------------|
| percentChange5m | string | 5-minute price change (%) |
| percentChange1h | string | 1-hour price change (%) |
| percentChange4h | string | 4-hour price change (%) |
| percentChange24h | string | 24-hour price change (%) |

### Volume
| Field | Type | Description |
|-------|------|-------------|
| volume24h | string | 24-hour total volume (USD) |
| volume24hBuy | string | 24-hour buy volume |
| volume24hSell | string | 24-hour sell volume |
| volume4h | string | 4-hour volume |
| volume1h | string | 1-hour volume |
| volume5m | string | 5-minute volume |

### Transaction Count
| Field | Type | Description |
|-------|------|-------------|
| count24h | string | 24-hour transaction count |
| count24hBuy | string | 24-hour buy count |
| count24hSell | string | 24-hour sell count |

### Market Data
| Field | Type | Description |
|-------|------|-------------|
| marketCap | string | Market cap (USD) |
| fdv | string | Fully diluted valuation |
| totalSupply | string | Total supply |
| circulatingSupply | string | Circulating supply |
| liquidity | string | Liquidity (USD) |

### Holder Data
| Field | Type | Description |
|-------|------|-------------|
| holders | string | Total holder count |
| top10HoldersPercentage | string | Top 10 holders percentage (%) |
| kycHolderCount | string | KYC holder count |
| kolHolders | string | KOL holder count |
| kolHoldingPercent | string | KOL holding percentage |
| devHoldingPercent| string | Dev holding percentage |
| proHoldingPercent | string | Professional investor holding percentage |
| smartMoneyHoldingPercent | string | Smart money holding percentage |

---

## API 4: Token K-Line (Candlestick)

### Method: GET

**URL**:
```
https://dquery.sintral.io/u-kline/v1/k-line/candles
```

**Request Parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| address | string | Yes | Token contract address |
| platform | string | Yes | Chain platform: `ethereum`, `bsc`, `solana`, `base` |
| interval | string | Yes | Kline interval (see Interval Reference below) |
| limit | number | No | Number of candles to return (has higher priority than `from`) |
| from | number | No | Start timestamp in milliseconds |
| to | number | No | End timestamp in milliseconds |
| pm | string | No | Kline type: `p` for price, `m` for market cap (default: `p`) |

**Interval Reference**:

| Interval | Description |
|----------|-------------|
| 1s | 1 second |
| 1min | 1 minute |
| 3min | 3 minutes |
| 5min | 5 minutes |
| 15min | 15 minutes |
| 30min | 30 minutes |
| 1h | 1 hour |
| 2h | 2 hours |
| 4h | 4 hours |
| 6h | 6 hours |
| 8h | 8 hours |
| 12h | 12 hours |
| 1d | 1 day |
| 3d | 3 days |
| 1w | 1 week |
| 1m | 1 month |

**Platform Mapping**:

| Chain | platform value |
|-------|---------------|
| Ethereum | ethereum |
| BSC | bsc |
| Solana | solana |
| Base | base |

**Request Headers**:
```
Accept-Encoding: identity
User-Agent: binance-web3/1.1 (Skill)
```

**Example Request**:
```bash
curl --location 'https://dquery.sintral.io/u-kline/v1/k-line/candles?address=0x55d398326f99059ff775485246999027b3197955&interval=1min&limit=500&platform=bsc&to=1772126280000' \
--header 'Accept-Encoding: identity' \
--header 'User-Agent: binance-web3/1.1 (Skill)'
```

**Response Example**:
```json
{
    "data": [
        [0.10779318, 0.10779318, 0.10778039, 0.10778039, 2554.06, 1772125800000, 3],
        [0.10778039, 0.10781213, 0.10770104, 0.10770104, 2994.53, 1772125920000, 3],
        [0.10770104, 0.10770104, 0.10769200, 0.10769200, 2825.65, 1772126040000, 3],
        [0.10769200, 0.10777858, 0.10766827, 0.10777858, 2457.99, 1772126160000, 3],
        [0.10777858, 0.10778521, 0.10764351, 0.10764351, 3106.87, 1772126280000, 4]
    ],
    "status": {
        "timestamp": "2026-02-28T05:52:25.717Z",
        "error_code": "0",
        "error_message": "SUCCESS",
        "elapsed": "0",
        "credit_count": 0
    }
}
```

**Response Fields**:

Each candle is an array with 7 elements in order:

| Index | Field | Type | Description |
|-------|-------|------|-------------|
| 0 | open | number | Open price |
| 1 | high | number | High price |
| 2 | low | number | Low price |
| 3 | close | number | Close price |
| 4 | volume | number | Trading volume |
| 5 | timestamp | number | Candle timestamp (ms) |
| 6 | count | number | Transaction count |

---

## User Agent Header

Include `User-Agent` header with the following string: `binance-web3/1.1 (Skill)`

## Notes

1. Icon URL requires full domain prefix: `https://bin.bnbstatic.com` + icon path
2. All numeric fields are string format, convert when using
3. Dynamic data updates in real-time, suitable for market display
4. K-Line API uses `platform` (eth/bsc/solana/base) instead of `chainId`, and `limit` takes priority over `from` when both are provided
5. K-Line response is a 2D array (not JSON objects) — parse by index: [open, high, low, close, volume, timestamp, count]
```

## File: `skills/binance-web3/trading-signal/SKILL.md`
```markdown
---
name: trading-signal
description: |
  Subscribe and retrieve on-chain Smart Money signals. Monitor trading activities of smart money addresses,
  including buy/sell signals, trigger price, current price, max gain, and exit rate.
  Use this skill when users are looking for investment opportunities — smart money signals can serve as valuable references for potential trades.
metadata:
  author: binance-web3-team
  version: "1.1"
---

# Trading Signal Skill

## Overview

This skill retrieves on-chain Smart Money trading signals to help users track professional investors:

- Get smart money buy/sell signals
- Compare signal trigger price with current price
- Analyze max gain and exit rate of signals
- Get token tags (e.g., Pumpfun, DEX Paid)

## API Endpoint

### Get Smart Money Signals

**Method**: POST

**URL**: 
```
https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/web/signal/smart-money/ai
```

**Request Headers**:
```
Content-Type: application/json
Accept-Encoding: identity
User-Agent: binance-web3/1.1 (Skill)
```

**Request Body**:
```json
{
    "smartSignalType": "",
    "page": 1,
    "pageSize": 100,
    "chainId": "CT_501"
}
```

**Request Parameters**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| chainId | string | Yes | Chain ID: `56` for bsc, `CT_501` for solana |
| page | number | No | Page number, starting from 1 |
| pageSize | number | No | Items per page, max 100 |

**Example Request**:
```bash
curl --location 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/web/signal/smart-money/ai' \
--header 'Content-Type: application/json' \
--header 'Accept-Encoding: identity' \
--header 'User-Agent: binance-web3/1.1 (Skill)' \
--data '{"page":1,"pageSize":100,"chainId":"CT_501"}'
```

**Response Example**:
```json
{
    "code": "000000",
    "message": null,
    "messageDetail": null,
    "data": [
        {
            "signalId": 22179,
            "ticker": "symbol of the token",
            "chainId": "CT_501",
            "contractAddress": "NV...pump",
            "logoUrl": "/images/web3-data/public/token/logos/825C62EC6BE6.png",
            "chainLogoUrl": "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20250303/42065e0a-3808-400e-b589-61c2dbfc0eac.png",
            "tokenDecimals": 6,
            "isAlpha": false,
            "launchPlatform": "Pumpfun",
            "mark": null,
            "isExclusiveLaunchpad": false,
            "alphaPoint": null,
            "tokenTag": {
                "Social Events": [
                    {"tagName": "DEX Paid", "languageKey": "wmp-label-update-dexscreener-social"}
                ],
                "Launch Platform": [
                    {"tagName": "Pumpfun", "languageKey": "wmp-label-title-pumpfun"}
                ],
                "Sensitive Events": [
                    {"tagName": "Smart Money Add Holdings", "languageKey": "wmp-label-title-smart-money-add-position"}
                ]
            },
            "smartSignalType": "SMART_MONEY",
            "smartMoneyCount": 5,
            "direction": "buy",
            "timeFrame": 883000,
            "signalTriggerTime": 1771903462000,
            "totalTokenValue": "3436.694044670495772073",
            "alertPrice": "0.024505932131088482",
            "alertMarketCap": "24505118.720436560690909782",
            "currentPrice": "0.025196",
            "currentMarketCap": "25135683.751234890220129783671668745",
            "highestPrice": "0.027244000000000000",
            "highestPriceTime": 1771927760000,
            "exitRate": 78,
            "status": "timeout",
            "maxGain": "5.4034",
            "signalCount": 23
        }
    ],
    "success": true
}
```

**Response Fields**:

### Basic Information
| Field | Type | Description |
|-------|------|-------------|
| signalId | number | Unique signal ID |
| ticker | string | Token symbol/name |
| chainId | string | Chain ID |
| contractAddress | string | Token contract address |
| logoUrl | string | Token icon URL path |
| chainLogoUrl | string | Chain icon URL |
| tokenDecimals | number | Token decimals |

### Tag Information
| Field | Type | Description |
|-------|------|-------------|
| isAlpha | boolean | Whether it's an Alpha token |
| launchPlatform | string | Launch platform (e.g., Pumpfun) |
| isExclusiveLaunchpad | boolean | Whether it's exclusive launchpad |
| alphaPoint | number | Alpha points (can be null) |
| tokenTag | object | Token tag categories |

### Signal Data
| Field | Type | Description |
|-------|------|-------------|
| smartSignalType | string | Signal type, e.g., `SMART_MONEY` |
| smartMoneyCount | number | Number of smart money addresses involved |
| direction | string | Trade direction: `buy` / `sell` |
| timeFrame | number | Time frame (milliseconds) |
| signalTriggerTime | number | Signal trigger timestamp (ms) |
| signalCount | number | Total signal count |

### Price Data
| Field | Type | Description |
|-------|------|-------------|
| totalTokenValue | string | Total trade value (USD) |
| alertPrice | string | Price at signal trigger |
| alertMarketCap | string | Market cap at signal trigger |
| currentPrice | string | Current price |
| currentMarketCap | string | Current market cap |
| highestPrice | string | Highest price after signal |
| highestPriceTime | number | Highest price timestamp (ms) |

### Performance Data
| Field | Type | Description |
|-------|------|-------------|
| exitRate | number | Exit rate (%) |
| status | string | Signal status: `active`/`timeout`/`completed` |
| maxGain | string | Maximum gain (%) |

## Token Tag Types

### Social Events
| Tag | Description |
|-----|-------------|
| DEX Paid | DEX paid promotion |

### Launch Platform
| Tag | Description |
|-----|-------------|
| Pumpfun | Pump.fun platform |
| Moonshot | Moonshot platform |

### Sensitive Events
| Tag | Description |
|-----|-------------|
| Smart Money Add Holdings | Smart money accumulating |
| Smart Money Reduce Holdings | Smart money reducing |
| Whale Buy | Whale buying |
| Whale Sell | Whale selling |

## Supported Chains

| Chain Name | chainId |
|------------|---------|
| BSC | 56 |
| Solana | CT_501 |

## Signal Status

| Status | Description |
|--------|-------------|
| active | Active, signal still valid |
| timeout | Timed out, exceeded observation period |
| completed | Completed, reached target or stop loss |

## User Agent Header

Include `User-Agent` header with the following string: `binance-web3/1.1 (Skill)`

## Use Cases

1. **Track Smart Money**: Monitor professional investor trading behavior
2. **Discover Opportunities**: Get early signals when smart money buys
3. **Risk Alert**: Receive alerts when smart money starts selling
4. **Performance Analysis**: Analyze historical signal performance and max gains
5. **Strategy Validation**: Evaluate signal quality via exitRate and maxGain

## Example Requests

### Get Smart Money Signals on Solana
```bash
curl --location 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/web/signal/smart-money/ai' \
--header 'Content-Type: application/json' \
--header 'Accept-Encoding: identity' \
--header 'User-Agent: binance-web3/1.1 (Skill)' \
--data '{"smartSignalType":"","page":1,"pageSize":50,"chainId":"CT_501"}'
```

### Get Signals on BSC
```bash
curl --location 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/web/signal/smart-money/ai' \
--header 'Content-Type: application/json' \
--header 'Accept-Encoding: identity' \
--header 'User-Agent: binance-web3/1.1 (Skill)' \
--data '{"smartSignalType":"","page":1,"pageSize":50,"chainId":"56"}'
```

## Notes

1. Token icon URL requires full domain prefix: `https://bin.bnbstatic.com` + logoUrl path
2. Chain icon URL (chainLogoUrl) is already a full URL
3. All timestamps are in milliseconds
4. maxGain is a percentage string
5. Signals may timeout (status=timeout), focus on active signals
6. Higher smartMoneyCount may indicate higher signal reliability
7. exitRate shows smart money exit status, high exitRate may indicate expired signal
```

