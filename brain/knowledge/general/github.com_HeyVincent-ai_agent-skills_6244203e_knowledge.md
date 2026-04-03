---
id: github.com-heyvincent-ai-agent-skills-6244203e-kno
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:06.354427
---

# KNOWLEDGE EXTRACT: github.com_HeyVincent-ai_agent-skills_6244203e
> **Extracted on:** 2026-04-01 09:38:10
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520330/github.com_HeyVincent-ai_agent-skills_6244203e

---

## File: `.gitignore`
```
.DS_Store
```

## File: `README.md`
```markdown
# Vincent Agent Skills

Pre-built capabilities for AI agents to safely interact with wallets, DeFi, and prediction markets — without ever exposing private keys. Skills enable autonomous crypto operations with policy controls, spending limits, and human approval flows through natural language interfaces.

Public repository of skills for [Vincent](https://heyvincent.ai) — secure secret management and wallet infrastructure for AI agents.

## Quick Start

```bash
# Add this repo URL to your agent runtime to browse and install skills:
https://github.com/HeyVincent-ai/agent-skills
```

Skills are drop-in modules. The agent creates its own wallet at runtime — no pre-existing credentials or configuration required.

## Available Skills

| Skill | Description |
| ----- | ----------- |
| [wallet](wallet/) | EVM smart account wallet for agents. Transfers, token swaps, contract interactions on any EVM chain. Gas-free via ZeroDev paymaster. |
| [polymarket](polymarket/) | Prediction market trading for agents. Browse markets, place bets, manage positions on Polymarket. Gasless via relayer. |
| [brave-search](brave-search/) | Web and news search for agents via Brave Search. Pay-per-call ($0.005/query) through Vincent credit system. |
| [twitter](twitter/) | Twitter/X.com data access for agents. Search tweets, look up profiles, retrieve recent tweets. Pay-per-call through Vincent credit system. |
| [trading-engine](trading-engine/) | Strategy-driven automated trading for Polymarket. LLM-powered strategies with data monitors (web search, Twitter, newswire, price feeds) that evaluate a thesis and trade autonomously. Also includes standalone stop-loss, take-profit, and trailing stops. |

## How It Works

1. **Agent creates a wallet** by calling the Vincent API — receives a scoped API key (never a private key)
2. **Agent operates autonomously** within policy boundaries set by the human owner
3. **Human claims ownership** via a claim URL, sets spending limits, approval thresholds, and allowlists
4. **All policies enforced server-side** — the agent cannot bypass them regardless of what it sends

The private key never leaves the Vincent server. The agent's API key is a scoped Bearer token that the wallet owner can revoke at any time.

## Structure

Each top-level directory is an installable skill containing a `SKILL.md` with full API documentation and usage instructions.

```
agent-skills/
├── wallet/
│   └── SKILL.md          # EVM wallet — transfers, swaps, contract calls
├── polymarket/
│   └── SKILL.md          # Polymarket — prediction market trading
├── brave-search/
│   └── SKILL.md          # Brave Search — web and news search
├── twitter/
│   └── SKILL.md          # Twitter/X.com — tweet search, user profiles
└── trading-engine/
    └── SKILL.md          # Trading Engine — LLM strategies, trade rules, stop-loss
```

## Policy Controls

The wallet owner configures policies from the [Vincent dashboard](https://heyvincent.ai). All enforcement is server-side.

| Policy | Description |
| ------ | ----------- |
| Address allowlist | Only interact with approved addresses |
| Token allowlist | Only transfer approved tokens |
| Function allowlist | Only call approved contract functions |
| Spending limit (per tx) | Max USD value per transaction |
| Spending limit (daily) | Max USD value per rolling 24 hours |
| Spending limit (weekly) | Max USD value per rolling 7 days |
| Require approval | Every action needs human approval via Telegram |
| Approval threshold | Actions above a USD amount need human approval |

## Use Cases

**Autonomous trading** — Agents manage portfolios, execute swaps, and trade prediction markets within spending limits.

**DeFi operations** — Transfer tokens, interact with smart contracts, and swap on DEXs across any EVM chain with gas fully sponsored.

**Prediction markets** — Browse Polymarket, place bets, and manage positions with policy-controlled risk limits.

**Web research** — Agents search the web and news via Brave Search to gather real-time information, monitor topics, and inform decisions.

**Social intelligence** — Agents search tweets, track user profiles, and monitor conversations on Twitter/X.com for sentiment and signals.

**Automated trading strategies** — Agents create LLM-powered strategies that monitor web, Twitter, newswire, and price data, then trade autonomously based on a thesis. Standalone stop-loss, take-profit, and trailing stops provide additional risk management.

**Human-in-the-loop workflows** — High-value actions trigger Telegram approval notifications for the wallet owner before execution.

## Contributing

We welcome community contributions! Here's how to add a new skill:

### Adding a New Skill

1. **Fork this repository** and create a new branch for your skill.

2. **Create a skill directory**:
   ```
   mkdir your-skill-name/
   ```

3. **Add the required files**:
   - `SKILL.md` — The main skill definition file (required)

4. **Follow the structure**:
   ```
   your-skill-name/
   └── SKILL.md
   ```

5. **Submit a Pull Request** with a clear description of your skill.

### Guidelines

- Keep skill definitions clear and well-documented
- Include API examples and workflow walkthroughs in your `SKILL.md`
- All skills should use the Vincent API at `heyvincent.ai`
- Test your skill before submitting

## Links

- **Website**: [heyvincent.ai](https://heyvincent.ai)
- **Vincent repo**: [github.com/HeyVincent-ai/Vincent](https://github.com/HeyVincent-ai/Vincent)
```

## File: `brave-search/SKILL.md`
```markdown
---
name: Vincent - Brave Search for agents
description: |
  Web and news search powered by Brave Search. Use this skill when users want to search the web,
  find news articles, or look up current information. Pay-per-call via Vincent credit system.
  Triggers on "search the web", "web search", "brave search", "search news", "find information",
  "look up", "current events".
allowed-tools: Read, Write, Bash(npx:@vincentai/cli*), Bash(jq:*), Bash(bc:*)
version: 1.0.0
author: HeyVincent <contact@heyvincent.ai>
license: MIT
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/datasources
        - ./datasources
---

# Vincent - Brave Search for agents

Use this skill to search the web and news using Brave Search. All requests are proxied through the Vincent backend, which handles authentication with the Brave Search API, enforces rate limits, tracks per-call costs, and deducts from your credit balance automatically.

**No API keys to manage.** The agent authenticates with a Vincent API key scoped to a `DATA_SOURCES` secret. Vincent handles the upstream Brave Search API credentials server-side -- the agent never sees or manages Brave API keys.

All commands use the `@vincentai/cli` package. API keys are stored and resolved automatically — you never handle raw keys or file paths.

## Security Model

This skill is designed for **autonomous agent operation with pay-per-call pricing and human oversight**.

**No environment variables are required** because this skill uses agent-first onboarding: the agent creates a `DATA_SOURCES` secret at runtime by calling the Vincent API, which returns a scoped API key. The CLI stores the returned API key automatically during creation. The config paths where the key is persisted (`${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/datasources/` or `./datasources/`) are declared in this skill's metadata.

**The agent's API key is not a Brave Search API key.** It is a scoped Bearer token for the Vincent proxy. The Vincent server authenticates with Brave Search on the agent's behalf. The agent cannot access the upstream API directly or bypass the proxy's credit and rate-limit enforcement.

**Model invocation is intentionally enabled.** The purpose of this skill is to give AI agents autonomous web search capabilities. The agent is expected to search the web and news on its own. The human controls spending through credit balance and payment method management at `https://heyvincent.ai`.

**All API calls go exclusively to `heyvincent.ai`** over HTTPS/TLS. The Vincent server then calls the Brave Search API. The agent does not contact Brave directly.

**Key lifecycle:**

- **Creation**: The agent runs `secret create` with `--type DATA_SOURCES` — the CLI stores the API key automatically and returns a `keyId` and `claimUrl`.
- **Claim**: The human operator uses the claim URL to take ownership, add credit, and manage payment at `https://heyvincent.ai`.
- **Credit**: Each API call costs a small amount (see Pricing below). The human adds credit via the frontend. Calls are rejected when credit runs out and no payment method is on file.
- **Revocation**: The secret owner can revoke the agent's API key at any time from the Vincent frontend.

## Pricing

| Endpoint | Cost per call |
| --- | --- |
| Web search | $0.005 |
| News search | $0.005 |

Credit is deducted automatically per call. The response includes `_vincent.creditRemainingUsd` so the agent can track remaining balance.

## Quick Start

### 1. Check for Existing Keys

Before creating a new secret, check if one already exists:

```bash
npx @vincentai/cli@latest secret list --type DATA_SOURCES
```

If a key is returned, use its `id` as the `--key-id` for all subsequent commands. If no keys exist, create a new secret.

### 2. Create a Data Sources Secret

```bash
npx @vincentai/cli@latest secret create --type DATA_SOURCES --memo "My agent data sources"
```

Returns `keyId` (use for all future commands) and `claimUrl` (share with the user).

After creating, tell the user:

> "Here is your data sources claim URL: `<claimUrl>`. Use this to claim ownership and add credit for Brave Search and other data sources at https://heyvincent.ai."

**Important:** The secret must be claimed and have credit (or a payment method on file) before API calls will succeed.

### 3. Web Search

```bash
npx @vincentai/cli@latest brave web --key-id <KEY_ID> --q "latest AI news" --count 10
```

Parameters:

- `--q` (required): Search query (1-400 characters)
- `--count` (optional): Number of results, 1-20 (default: 10)
- `--offset` (optional): Pagination offset, 0-9
- `--freshness` (optional): Time filter — `pd` (past day), `pw` (past week), `pm` (past month), `py` (past year)
- `--country` (optional): 2-letter country code for localized results (e.g., `us`, `gb`, `de`)

Returns web results with titles, URLs, descriptions, and metadata.

### 4. News Search

```bash
npx @vincentai/cli@latest brave news --key-id <KEY_ID> --q bitcoin --count 10
```

Parameters:

- `--q` (required): Search query (1-400 characters)
- `--count` (optional): Number of results, 1-20 (default: 10)
- `--freshness` (optional): Time filter — `pd` (past day), `pw` (past week), `pm` (past month), `py` (past year)

Returns news articles with titles, URLs, descriptions, publication dates, and source information.

## Response Metadata

Every successful response includes a `_vincent` object with:

```json
{
  "_vincent": {
    "costUsd": 0.005,
    "creditRemainingUsd": 4.99
  }
}
```

Use `creditRemainingUsd` to warn the user when credit is running low.

## Output Format

Web search results:

```json
{
  "web": {
    "results": [
      {
        "title": "Article Title",
        "url": "https://example.com/article",
        "description": "A brief description of the article content."
      }
    ]
  },
  "_vincent": {
    "costUsd": 0.005,
    "creditRemainingUsd": 4.99
  }
}
```

News search results follow the same structure with additional `age` and `source` fields per result.

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `401 Unauthorized` | Invalid or missing API key | Check that the key-id is correct; re-link if needed |
| `402 Insufficient Credit` | Credit balance is zero and no payment method on file | User must add credit at heyvincent.ai |
| `429 Rate Limited` | Exceeded 60 requests/minute | Wait and retry with backoff |
| `Key not found` | API key was revoked or never created | Re-link with a new token from the secret owner |

## Rate Limits

- 60 requests per minute per API key across all data source endpoints (Twitter + Brave Search combined)
- If rate limited, you'll receive a `429` response. Wait and retry.

## Re-linking (Recovering API Access)

If the agent loses its API key, the secret owner can generate a **re-link token** from the frontend. The agent then exchanges this token for a new API key.

```bash
npx @vincentai/cli@latest secret relink --token <TOKEN_FROM_USER>
```

The CLI exchanges the token for a new API key, stores it automatically, and returns the new `keyId`. Re-link tokens are one-time use and expire after 10 minutes.

## Adding Credits

When your credit balance runs low, you can purchase more credits autonomously using USDC on Base via the x402 payment protocol — no human intervention required.

**Available tiers:** $1, $5, $10, $25, $50, $100

### Check Balance

```bash
npx @vincentai/cli@latest credits balance --key-id <KEY_ID>
```

### Purchase Credits via x402 (USDC on Base)

```bash
npx @vincentai/cli@latest credits add --key-id <KEY_ID> --amount 10
```

**How it works:**

1. The CLI sends a POST request to the x402 credit endpoint
2. The server returns HTTP 402 with a dynamic USDC deposit address on Base
3. The CLI signs the payment using your agent's wallet
4. The CLI retries the request with the payment proof
5. The server verifies the payment and adds credits to your account

**Requirements:**
- An x402-compatible wallet with USDC on Base (chain ID 8453)
- Your Vincent DATA_SOURCES API key

### Purchase Credits via Card (Human)

```bash
npx @vincentai/cli@latest credits checkout --key-id <KEY_ID>
```

Returns a Stripe Checkout URL. Share this with the user to complete payment with a card.

### MCP Tools

| Tool | Description |
| --- | --- |
| `vincent_credit_balance` | Check current credit balance and top-up options |
| `vincent_add_credits` | Get x402 payment instructions for purchasing credits |

### Auto-Replenish Pattern

For long-running agents, check your balance before expensive operations and top up when low:

```bash
BALANCE=$(npx @vincentai/cli@latest credits balance --key-id <KEY_ID> --json | jq -r '.balance')
if (( $(echo "$BALANCE < 2.00" | bc -l) )); then
  npx @vincentai/cli@latest credits add --key-id <KEY_ID> --amount 10
fi
```

## Important Notes

- A single `DATA_SOURCES` API key works for **all** data sources (Twitter, Brave Search, etc.). You do not need a separate key per data source.
- Always share the claim URL with the user after creating a secret.
- If a call is rejected with a credit error, tell the user to add credit at `https://heyvincent.ai`.
```

## File: `credentials/SKILL.md`
```markdown
---
name: Vincent - Credentials for agents
description: |
  Secure credential management for agents. Use this skill when users need to store API keys,
  passwords, OAuth tokens, or SSH keys and write them to .env files without exposing values.
  Triggers on "store credentials", "API key", "manage secrets", "write to env", ".env file",
  "credential", "password", "token storage".
allowed-tools: Read, Write, Bash(npx:@vincentai/cli*)
version: 1.0.0
author: HeyVincent <contact@heyvincent.ai>
license: MIT
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/credentials
        - ./credentials
---

# Vincent - Credentials for agents

Use this skill to securely manage credentials that your application needs — API keys, passwords, OAuth tokens, SSH keys, or structured username/password pairs. The agent creates a secret, the user (or agent) sets the value, and the agent uses the CLI to write it directly to a `.env` file. **The credential value never appears in the agent's context or stdout.**

This is useful when the agent is building something that needs credentials (e.g. a third-party API key). Instead of the user pasting the credential into chat (where it enters the agent's context), they set it via the Vincent dashboard, and the agent writes it to the `.env` file using the CLI.

All commands use the `@vincentai/cli` package. API keys are stored and resolved automatically — you never handle raw keys or file paths.

## Security Model

This skill is designed for **keeping credentials out of the agent's context window**.

**How it works:** The `secret env` CLI command fetches the credential from the Vincent server and writes it directly to a `.env` file on disk. The value is never printed to stdout and never appears in the agent's conversation context. Many agent frameworks blacklist reading `.env` files, so even though the file is on disk, the agent cannot read it back. The application the agent is building reads the `.env` file normally at runtime.

**No environment variables are required** because this skill uses agent-first onboarding: the agent creates its own credential secret at runtime by calling the Vincent API, which returns a scoped API key. The CLI stores the returned API key automatically during creation. The config paths where the key is persisted (`${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/credentials/` or `./credentials/`) are declared in this skill's metadata.

**Overwrite guard:** Once a value is set by an agent's API key, only that same API key can overwrite it. This prevents other agents or keys from tampering with the credential. The guard is enforced atomically at the database level.

**All API calls go exclusively to `heyvincent.ai`** over HTTPS/TLS. No other endpoints, services, or external hosts are contacted.

**Key lifecycle:**

- **Creation**: The agent runs `secret create` with `--type CREDENTIALS` — the CLI stores the API key automatically and returns a `keyId` and `claimUrl`.
- **Value set**: The user sets the credential value via the dashboard after claiming, or the agent sets it via the CLI.
- **Write to .env**: The agent runs `secret env` to write the value to a `.env` file without exposing it.
- **Claim**: The human operator uses the claim URL to take ownership and manage the secret from the dashboard.
- **Revocation**: The secret owner can revoke the agent's API key at any time from `https://heyvincent.ai`.

## Secret Types

| Type | Value format | Use case |
|---|---|---|
| `API_KEY` | Non-empty string | Third-party API keys |
| `SSH_KEY` | Non-empty string | SSH private keys |
| `OAUTH_TOKEN` | Non-empty string | OAuth access/refresh tokens |
| `CREDENTIALS` | JSON object with `password` or `secret` | Username/password, key/secret pairs |

All four types support the same create, set, and `env` workflow.

### CREDENTIALS Value Format

The `CREDENTIALS` value must be a JSON object containing at least one of:

- `password` (string) — e.g. `{"username": "alice", "password": "hunter2"}`
- `secret` (string) — e.g. `{"accountId": "acct-1", "secret": "top-secret"}`

Additional fields are preserved as-is. All values are limited to 16KB.

## Quick Start

### 1. Check for Existing Keys

Before creating a new secret, check if one already exists:

```bash
npx @vincentai/cli@latest secret list --type CREDENTIALS
```

If a key is returned, use its `id` as the `--key-id` for subsequent commands. If no keys exist, create a new secret.

### 2. Create a Credentials Secret

```bash
npx @vincentai/cli@latest secret create --type CREDENTIALS --memo "Acme API credentials"
```

Returns `keyId` (use for all future commands), `claimUrl` (share with the user), and `secretId`.

After creating, tell the user:

> "Here is your credentials claim URL: `<claimUrl>`. Use this to claim ownership and set the credential value at https://heyvincent.ai."

### 3. Set the Credential Value

**Option A: User sets via dashboard (recommended)**

The user claims the secret using the claim URL, then sets the credential value from the dashboard. This keeps the value completely out of the agent's hands.

**Option B: Agent sets via CLI**

For agent-first workflows where the agent has the credential (e.g. it obtained an API key from a service):

```bash
npx @vincentai/cli@latest secret set-value --key-id <KEY_ID> --value '{"username": "alice", "password": "hunter2"}'
```

For simple string types (`API_KEY`, `SSH_KEY`, `OAUTH_TOKEN`):

```bash
npx @vincentai/cli@latest secret set-value --key-id <KEY_ID> --value "sk-my-third-party-api-key"
```

### 4. Write to .env File

Once the value is set (by the user or the agent), use the CLI to write it to a `.env` file. **The value is never printed to stdout.**

```bash
# Write an API_KEY secret as an env var
npx @vincentai/cli@latest secret env --key-id <KEY_ID> --env-var ACME_API_KEY

# For CREDENTIALS: extract a specific field
npx @vincentai/cli@latest secret env --key-id <KEY_ID> --env-var DB_PASSWORD --field password

# Write to a specific path (default: ./.env)
npx @vincentai/cli@latest secret env --key-id <KEY_ID> --env-var SERVICE_TOKEN --path ./config/.env
```

The command outputs a confirmation JSON (without the value) so the agent knows it succeeded:

```json
{
  "written": "ACME_API_KEY",
  "path": "/path/to/.env",
  "type": "API_KEY"
}
```

**Flags:**

| Flag | Required | Description |
|---|---|---|
| `--env-var` | Yes | Environment variable name (e.g. `MY_API_KEY`) |
| `--path` | No | Path to `.env` file (default: `./.env`) |
| `--key-id` | No | API key ID (auto-discovered if only one credential key exists) |
| `--field` | No | For `CREDENTIALS` type: extract a specific JSON field instead of writing the full JSON |

**Behavior:**

- Creates the `.env` file if it doesn't exist (with `0600` permissions)
- Updates the variable in-place if it already exists in the file
- Appends a new line if the variable doesn't exist
- Values with special characters are automatically quoted

### 5. Use in Your Application

Your application reads the `.env` file normally:

```bash
# Node.js with dotenv
require('dotenv').config()
const apiKey = process.env.ACME_API_KEY

# Python with python-dotenv
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('ACME_API_KEY')
```

## Example: Full Workflow

```bash
# 1. Agent creates a CREDENTIALS secret
npx @vincentai/cli@latest secret create --type CREDENTIALS --memo "Acme service credentials"
# → keyId: abc-123, claimUrl: https://heyvincent.ai/claim/...

# 2. Tell the user to claim and set the value via the dashboard

# 3. Once set, write individual fields to .env
npx @vincentai/cli@latest secret env --key-id abc-123 --env-var ACME_USERNAME --field username
npx @vincentai/cli@latest secret env --key-id abc-123 --env-var ACME_PASSWORD --field password

# Result in .env:
# ACME_USERNAME=alice
# ACME_PASSWORD=hunter2
```

## Output Format

The `secret env` command outputs a confirmation JSON (without the credential value):

```json
{
  "written": "ACME_API_KEY",
  "path": "/path/to/.env",
  "type": "API_KEY"
}
```

The `secret create` command returns:

```json
{
  "keyId": "abc-123",
  "claimUrl": "https://heyvincent.ai/claim/...",
  "secretId": "sec-456"
}
```

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `401 Unauthorized` | Invalid or missing API key | Check that the key-id is correct; re-link if needed |
| `403 Overwrite Rejected` | A different API key set this credential's value | Secret owner must manage from the dashboard |
| `404 Value Not Set` | Credential value hasn't been set yet | User must set the value via dashboard or agent sets via CLI |
| `Key not found` | API key was revoked or never created | Re-link with a new token from the secret owner |

## Re-linking (Recovering API Access)

If the agent loses its API key, the secret owner can generate a **re-link token** from the frontend. The agent then exchanges this token for a new API key.

```bash
npx @vincentai/cli@latest secret relink --token <TOKEN_FROM_USER>
```

The CLI exchanges the token for a new API key, stores it automatically, and returns the new `keyId`. Re-link tokens are one-time use and expire after 10 minutes.

## Important Notes

- **The credential value never enters the agent's context.** The `secret env` command writes directly to a file — it does not print the value to stdout.
- Many agent frameworks (OpenClaw, Claude Code, etc.) blacklist reading `.env` files, providing an additional layer of protection.
- Always share the claim URL with the user after creating a secret.
- The 16KB size limit applies to the serialized value.
- If the overwrite is rejected with a `403`, it means a different API key set the value. The secret owner can manage this from the dashboard.
```

## File: `hyperliquid/SKILL.md`
```markdown
---
name: Vincent - HyperLiquid for agents
description: Use this skill to create a HyperLiquid perpetuals and spot wallet for your agent. Trade perps, manage spot balances, transfer USDC between sub-accounts, get prices, place orders — all without exposing private keys.
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/agentwallet
        - ./agentwallet
---

# Vincent - HyperLiquid for agents

Use this skill to create a HyperLiquid perpetuals and spot wallet for your agent. Trade perps, check spot balances, and transfer USDC between perps and spot sub-accounts. The generated EOA **is** the HyperLiquid account — fund it directly via the HL bridge and start trading immediately with no Safe deployment or collateral approval steps.

**The agent never sees the private key.** All operations are executed server-side. The agent receives a scoped API key that can only perform actions permitted by the wallet owner's policies.

All commands use the `@vincentai/cli` package. API keys are stored and resolved automatically.

## Security Model

**No environment variables are required.** The agent creates its own HyperLiquid wallet at runtime by calling the Vincent API, which returns a scoped API key. There is no pre-existing credential to configure.

**The generated EOA is a standalone HyperLiquid account.** Unlike Polymarket (which deploys a Gnosis Safe), the EOA private key IS the HyperLiquid account. Deposits go directly to this address via the HyperLiquid bridge from Arbitrum, or via `usdSend` from another HL account.

**The agent's API key is not a private key.** It is a scoped Bearer token enforced server-side. The Vincent server evaluates all policies before executing any trade. If a trade violates a policy, the server rejects it. If a trade requires human approval, the server holds it and notifies the wallet owner via Telegram.

**All API calls go exclusively to `heyvincent.ai`** over HTTPS/TLS. The service calls `api.hyperliquid.xyz` server-side on the agent's behalf.

**Key lifecycle:**

- **Creation**: Agent runs `secret create` — Vincent generates the EOA, stores the key, returns `keyId`, `walletAddress`, and `claimUrl`.
- **Claim**: Human operator uses the claim URL to take ownership and configure policies at `https://heyvincent.ai`.
- **Revocation**: Wallet owner revokes the agent's API key from the frontend at any time.
- **Re-linking**: Agent exchanges a one-time re-link token (generated by the owner) for a new key via `secret relink`.

## Quick Start

### 1. Check for Existing Keys

Before creating a new wallet, check if one already exists:

```bash
npx @vincentai/cli@latest secret list --type HYPERLIQUID_WALLET
```

If a key is returned, use its `id` as `--key-id` for all subsequent commands. If not, create one.

### 2. Create a HyperLiquid Wallet

```bash
npx @vincentai/cli@latest secret create --type HYPERLIQUID_WALLET --memo "My HL perp wallet"
```

Returns:

- `keyId` — use for all future commands
- `walletAddress` — the EOA address (this IS the HyperLiquid account)
- `claimUrl` — share with the user to take ownership

After creating, tell the user:

> "Here is your wallet claim URL: `<claimUrl>`. Use this to claim ownership, set spending policies, and monitor your agent's wallet activity at https://heyvincent.ai."

**Important:** The wallet is empty at creation. The user must deposit USDC before trading.

### 3. Get Balance

```bash
npx @vincentai/cli@latest hyperliquid balance --key-id <KEY_ID>
```

Returns:

- `walletAddress` — the EOA address
- `accountValue` — total perps account value in USD (cross-margin)
- `withdrawable` — USDC available to withdraw from the perps account
- `positions` — array of open perpetual positions
- `spotBalances` — array of spot token balances (each with `coin`, `token`, `hold`, `total`)

### 4. Transfer Between Perps and Spot

HyperLiquid has separate perps and spot sub-accounts. USDC must be in the correct sub-account before trading. Use `internal-transfer` to move USDC between them.

```bash
# Move 100 USDC from spot → perps (needed before perp trading)
npx @vincentai/cli@latest hyperliquid internal-transfer --key-id <KEY_ID> --amount 100 --to-perp true

# Move 50 USDC from perps → spot (needed before spot trading)
npx @vincentai/cli@latest hyperliquid internal-transfer --key-id <KEY_ID> --amount 50 --to-perp false
```

Parameters:

- `--amount`: USDC amount to transfer (string, numeric)
- `--to-perp`: `true` = spot→perps, `false` = perps→spot

**Response codes:**
- `200` — `status: "executed"` — transfer completed
- `202` — `status: "pending_approval"` (human approval required by policy)
- `403` — `status: "denied"` (rejected by policy)

### 5. Fund the Wallet

Deposit USDC to the EOA address via:

- **HyperLiquid bridge** from Arbitrum: visit `https://app.hyperliquid.xyz/portfolio` and bridge USDC to the EOA address
- **HL→HL transfer** (`usdSend`) from another HL account — instant

Minimum for a BTC perp trade: **$2 USDC** (covers $10 notional at 20x default leverage + taker fees).

### 6. Browse Markets

```bash
npx @vincentai/cli@latest hyperliquid markets --key-id <KEY_ID>
```

Returns a JSON object mapping coin names to mid prices (e.g. `{"BTC": "105234.5", "ETH": "3412.0", ...}`).

### 7. Get Order Book

```bash
npx @vincentai/cli@latest hyperliquid orderbook --key-id <KEY_ID> --coin BTC
```

Returns `levels` — a two-element array `[bids, asks]`. Each entry is `[price, size, numOrders]`. Use `levels[1][0][0]` for best ask, `levels[0][0][0]` for best bid.

### 8. Place a Trade

```bash
# Market buy (IoC — fills immediately or cancels)
npx @vincentai/cli@latest hyperliquid trade --key-id <KEY_ID> \
  --coin BTC --is-buy true --sz 0.0001 \
  --limit-px 106000 --order-type market

# Market sell to close (reduceOnly)
npx @vincentai/cli@latest hyperliquid trade --key-id <KEY_ID> \
  --coin BTC --is-buy false --sz 0.0001 \
  --limit-px 104000 --order-type market --reduce-only

# GTC limit buy
npx @vincentai/cli@latest hyperliquid trade --key-id <KEY_ID> \
  --coin BTC --is-buy true --sz 0.0001 \
  --limit-px 100000 --order-type limit
```

Parameters:

- `--coin`: Asset name (e.g. `BTC`, `ETH`, `SOL`)
- `--is-buy`: `true` for long, `false` for short/close
- `--sz`: Size in base currency (e.g. `0.0001` BTC)
- `--limit-px`: Price. For market orders, set slightly above ask (buy) or below bid (sell) to ensure fill. Recommended: `askPx * 1.005` for buys, `bidPx * 0.995` for sells.
- `--order-type`: `market` (IoC) or `limit` (GTC)
- `--reduce-only`: Pass when closing a position to prevent accidentally opening a new one in the opposite direction

**Minimum notional:** $10 (e.g. 0.0001 BTC at $100k/BTC). Default leverage is 20x cross-margin.

**Response codes:**
- `200` — `status: "executed"` with `orderId` (numeric) and `fillDetails`
- `202` — `status: "pending_approval"` (human approval required by policy)
- `403` — `status: "denied"` (rejected by policy)

### 9. View Open Orders

```bash
# All open orders
npx @vincentai/cli@latest hyperliquid open-orders --key-id <KEY_ID>

# Filter by coin
npx @vincentai/cli@latest hyperliquid open-orders --key-id <KEY_ID> --coin BTC
```

### 10. View Trade History

```bash
# All fills
npx @vincentai/cli@latest hyperliquid trades --key-id <KEY_ID>

# Filter by coin
npx @vincentai/cli@latest hyperliquid trades --key-id <KEY_ID> --coin ETH
```

### 11. Cancel Orders

```bash
# Cancel a specific order (requires coin and numeric order ID)
npx @vincentai/cli@latest hyperliquid cancel-order --key-id <KEY_ID> --coin BTC --oid <ORDER_ID>

# Cancel all open orders
npx @vincentai/cli@latest hyperliquid cancel-all --key-id <KEY_ID>

# Cancel all orders for a specific coin
npx @vincentai/cli@latest hyperliquid cancel-all --key-id <KEY_ID> --coin ETH
```

## Trading Engine: Stop-Loss, Take-Profit & Trailing Stop

The **Trading Engine** fully supports HyperLiquid. You can set automated stop-loss, take-profit, and trailing stop rules on any HL position. Rules execute automatically when price conditions are met — no LLM involved.

For HyperLiquid rules, use `--venue hyperliquid` and set `--market-id` / `--token-id` to the coin name (e.g. `BTC`, `ETH`, `SOL`). The `--trigger-price` is an absolute USD price (not 0–1 like Polymarket).

### Stop-Loss

```bash
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id BTC --token-id BTC \
  --rule-type STOP_LOSS --trigger-price 95000
```

Sells the position if BTC drops to $95,000.

### Take-Profit

```bash
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id ETH --token-id ETH \
  --rule-type TAKE_PROFIT --trigger-price 4500
```

Sells the position if ETH rises to $4,500.

### Trailing Stop

```bash
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id SOL --token-id SOL \
  --rule-type TRAILING_STOP --trigger-price 170 --trailing-percent 5
```

Stop price ratchets up as SOL rises. Sells if SOL drops 5% from its peak.

### Manage Rules

```bash
# List all rules
npx @vincentai/cli@latest trading-engine list-rules --key-id <KEY_ID>

# Update trigger price
npx @vincentai/cli@latest trading-engine update-rule --key-id <KEY_ID> --rule-id <RULE_ID> --trigger-price 98000

# Cancel a rule
npx @vincentai/cli@latest trading-engine delete-rule --key-id <KEY_ID> --rule-id <RULE_ID>

# View rule events
npx @vincentai/cli@latest trading-engine events --key-id <KEY_ID>
```

For full strategy docs (LLM-powered strategies, signal pipeline, drivers), see the **Trading Engine** skill.

## Policies (Server-Side Enforcement)

The wallet owner controls what the agent can do by setting policies at `https://heyvincent.ai`. All policies are enforced server-side before any trade executes.

| Policy                      | What it does                                                     |
| --------------------------- | ---------------------------------------------------------------- |
| **Spending limit (per tx)** | Max USD notional per trade                                       |
| **Spending limit (daily)**  | Max USD notional per rolling 24 hours                            |
| **Spending limit (weekly)** | Max USD notional per rolling 7 days                              |
| **Require approval**        | Every trade needs human approval via Telegram                    |
| **Approval threshold**      | Trades above a USD amount need human approval via Telegram       |

If a trade is blocked, the API returns `status: "denied"` with the reason. If approval is needed, `status: "pending_approval"` is returned and the wallet owner receives a Telegram notification.

## Re-linking

If the agent loses its API key:

1. User generates a re-link token from `https://heyvincent.ai`
2. User gives the token to the agent
3. Agent runs:

```bash
npx @vincentai/cli@latest secret relink --token <TOKEN_FROM_USER>
```

Re-link tokens are one-time use and expire after 10 minutes.

## Workflow Example

```bash
# 1. Create wallet
npx @vincentai/cli@latest secret create --type HYPERLIQUID_WALLET --memo "HL wallet"
# → returns keyId, walletAddress, claimUrl

# 2. Tell user: "Fund <walletAddress> on HyperLiquid with USDC, then I can trade."

# 3. Check balance after funding (returns both perps and spot balances)
npx @vincentai/cli@latest hyperliquid balance --key-id <KEY_ID>
# → accountValue shows perps balance, spotBalances shows spot holdings

# 4. Transfer USDC between sub-accounts if needed
# Move 100 USDC from spot → perps before perp trading:
npx @vincentai/cli@latest hyperliquid internal-transfer --key-id <KEY_ID> --amount 100 --to-perp true
# Move 50 USDC from perps → spot before spot trading:
npx @vincentai/cli@latest hyperliquid internal-transfer --key-id <KEY_ID> --amount 50 --to-perp false

# 5. Get BTC mid price
npx @vincentai/cli@latest hyperliquid markets --key-id <KEY_ID>

# 6. Get order book to find best ask
npx @vincentai/cli@latest hyperliquid orderbook --key-id <KEY_ID> --coin BTC
# → levels[1][0][0] is best ask, e.g. "105200.0"

# 7. Open long — 0.5% above ask to ensure IoC fill
npx @vincentai/cli@latest hyperliquid trade --key-id <KEY_ID> \
  --coin BTC --is-buy true --sz 0.0001 --limit-px 105726 --order-type market

# 8. Check fills
npx @vincentai/cli@latest hyperliquid trades --key-id <KEY_ID> --coin BTC

# 9. Close long — 0.5% below bid
npx @vincentai/cli@latest hyperliquid orderbook --key-id <KEY_ID> --coin BTC
npx @vincentai/cli@latest hyperliquid trade --key-id <KEY_ID> \
  --coin BTC --is-buy false --sz 0.0001 --limit-px 104674 --order-type market --reduce-only
```

## Output Format

All CLI commands return JSON to stdout.

**balance:**
```json
{
  "walletAddress": "0x...",
  "accountValue": "105.23",
  "withdrawable": "95.00",
  "positions": [
    {
      "position": {
        "coin": "BTC",
        "szi": "0.0001",
        "entryPx": "105200.0",
        "positionValue": "10.52",
        "unrealizedPnl": "0.05",
        "liquidationPx": null,
        "leverage": { "type": "cross", "value": 20 }
      },
      "type": "oneWay"
    }
  ],
  "spotBalances": [
    {
      "coin": "USDC",
      "token": 0,
      "hold": "0.0",
      "total": "50.0"
    }
  ]
}
```

**markets:**
```json
{
  "BTC": "105234.5",
  "ETH": "3412.0",
  "SOL": "185.3"
}
```

**orderbook:**
```json
{
  "coin": "BTC",
  "levels": [
    [["105200.0", "0.5", 3], ["105100.0", "1.2", 5]],
    [["105300.0", "0.3", 2], ["105400.0", "0.8", 4]]
  ]
}
```
`levels[0]` = bids (descending), `levels[1]` = asks (ascending). Each entry is `[price, size, numOrders]`. Best bid: `levels[0][0][0]`, best ask: `levels[1][0][0]`.

**trade (executed):**
```json
{
  "orderId": 12345678,
  "status": "executed",
  "transactionLogId": "clx...",
  "walletAddress": "0x...",
  "fillDetails": {
    "totalSz": "0.0001",
    "avgPx": "105250.0"
  }
}
```

**trade (pending approval):**
```json
{
  "status": "pending_approval",
  "transactionLogId": "clx...",
  "walletAddress": "0x...",
  "reason": "Exceeds approval threshold"
}
```

**trade (denied):**
```json
{
  "status": "denied",
  "transactionLogId": "clx...",
  "walletAddress": "0x...",
  "reason": "Exceeds daily spending limit"
}
```

**internal-transfer (executed):**
```json
{
  "status": "executed",
  "transactionLogId": "clx..."
}
```

**internal-transfer (pending approval):**
```json
{
  "status": "pending_approval",
  "transactionLogId": "clx...",
  "reason": "Exceeds approval threshold"
}
```

**internal-transfer (denied):**
```json
{
  "status": "denied",
  "transactionLogId": "clx...",
  "reason": "Exceeds daily spending limit"
}
```

**open-orders:**
```json
{
  "walletAddress": "0x...",
  "openOrders": [
    {
      "coin": "BTC",
      "side": "B",
      "limitPx": "100000.0",
      "sz": "0.0001",
      "oid": 12345678,
      "timestamp": 1700000000000,
      "origSz": "0.0001"
    }
  ]
}
```
`side`: `"B"` = buy/long, `"A"` = ask/sell.

**trades (fills):**
```json
{
  "walletAddress": "0x...",
  "fills": [
    {
      "coin": "BTC",
      "px": "105200.0",
      "sz": "0.0001",
      "side": "B",
      "time": 1700000000000,
      "dir": "Open Long",
      "closedPnl": "0",
      "fee": "0.0105",
      "oid": 12345678
    }
  ]
}
```

**cancel-order / cancel-all:**
```json
{}
```
Empty object on success. Any non-zero exit code indicates failure.

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `401 Unauthorized` | Invalid or missing API key | Check key-id is correct; re-link if needed |
| `status: "denied"` | Trade blocked by server-side policy | User must adjust policies at heyvincent.ai |
| `status: "pending_approval"` | Trade exceeds approval threshold | Do not retry — wallet owner receives Telegram notification to approve/deny |
| `400 Bad Request` | Invalid parameters (e.g. non-numeric oid, bad coin) | Fix the parameter values |
| `429 Rate Limited` | Too many requests | Wait and retry with backoff |
| `500 TRADE_FAILED` | HyperLiquid rejected the order (e.g. insufficient margin, bad price) | Check account balance and order parameters |
| `Key not found` | API key was revoked or never created | Re-link with a new token from the wallet owner |

## Important Notes

- **No gas required.** HyperLiquid L1 is gasless — all perp trades settle natively.
- **Perps and spot sub-accounts.** The generated EOA has both a perps sub-account (cross-margin) and a spot sub-account. Use `internal-transfer` to move USDC between them. Deposits via the HL bridge land in the perps account by default.
- **Never try to access raw secret values.** The private key stays server-side.
- Always share the claim URL with the user after creating a wallet.
- For market orders, always set `limitPx` slightly outside the best price (`* 1.005` for buys, `* 0.995` for sells) to guarantee IoC fill at the current market price.
- If a trade returns `status: "pending_approval"`, do not retry — wait for the wallet owner to respond via Telegram.
```

## File: `polymarket/SKILL.md`
```markdown
---
name: Vincent - Polymarket for agents
description: |
  Polymarket prediction market trading for agents. Use this skill when users want to create a
  Polymarket wallet, browse markets, place bets, manage positions, or withdraw funds.
  Triggers on "polymarket", "prediction market", "place bet", "browse markets", "trade prediction",
  "polymarket wallet", "betting", "market odds".
allowed-tools: Read, Write, Bash(npx:@vincentai/cli*)
version: 1.0.0
author: HeyVincent <contact@heyvincent.ai>
license: MIT
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/agentwallet
        - ./agentwallet
---

# Vincent - Polymarket for agents

Use this skill to create a Polymarket wallet for your agent and trade on prediction markets. Browse markets, place bets, track holdings, and manage orders — all without exposing private keys to the agent. Wallets use Gnosis Safe on Polygon with gasless trading through Polymarket's relayer.

**The agent never sees the private key.** All operations are executed server-side. The agent receives a scoped API key that can only perform actions permitted by the wallet owner's policies. The private key never leaves the Vincent server.

All commands use the `@vincentai/cli` package. API keys are stored and resolved automatically — you never handle raw keys or file paths.

## Security Model

This skill is designed for **autonomous agent trading with human oversight via server-side controls**. Understanding this model is important:

**No environment variables are required** because this skill uses agent-first onboarding: the agent creates its own Polymarket wallet at runtime by calling the Vincent API, which returns a scoped API key. There is no pre-existing credential to configure. The CLI stores the returned API key automatically during wallet creation. The config paths where the key is persisted (`${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/agentwallet/` or `./agentwallet/`) are declared in this skill's metadata.

**The agent's API key is not a private key.** It is a scoped Bearer token that can only execute actions within the policies set by the wallet owner. The Vincent server enforces all policies server-side — the agent cannot bypass them regardless of what it sends. If a trade violates a policy, the server rejects it. If a trade requires approval, the server holds it and notifies the wallet owner via Telegram for out-of-band human approval.

**Model invocation is intentionally enabled.** The purpose of this skill is to give AI agents autonomous Polymarket trading capabilities. The agent is expected to invoke trading actions (browse markets, place bets, manage positions) on its own, within the boundaries the human operator defines. The human controls what the agent can do through policies (spending limits, approval thresholds) — not by gating individual invocations. The stored key is scoped and policy-constrained — even if another process reads it, it can only perform actions the wallet owner's policies allow, and the owner can revoke it instantly.

**All API calls go exclusively to `heyvincent.ai`** over HTTPS/TLS. No other endpoints, services, or external hosts are contacted. The agent does not read, collect, or transmit any data beyond what is needed for Polymarket wallet operations.

**Key lifecycle:**

- **Creation**: The agent runs `secret create` — the CLI stores the API key automatically and returns a `keyId` and `claimUrl`.
- **Claim**: The human operator uses the claim URL to take ownership and configure policies at `https://heyvincent.ai`.
- **Revocation**: The wallet owner can revoke the agent's API key at any time from the Vincent frontend. Revoked keys are rejected immediately by the server.
- **Re-linking**: If the agent loses its API key, the wallet owner generates a one-time re-link token and the agent exchanges it for a new key via `secret relink`.
- **Rotation**: The wallet owner can revoke the current key and issue a re-link token to rotate credentials at any time.

## Quick Start

### 1. Check for Existing Keys

Before creating a new wallet, check if one already exists:

```bash
npx @vincentai/cli@latest secret list --type POLYMARKET_WALLET
```

If a key is returned, use its `id` as the `--key-id` for all subsequent commands. If no keys exist, create a new wallet.

### 2. Create a Polymarket Wallet

```bash
npx @vincentai/cli@latest secret create --type POLYMARKET_WALLET --memo "My prediction market wallet"
```

Returns `keyId` (use for all future commands), `claimUrl` (share with the user), and `walletAddress` (the EOA address; Safe is deployed lazily on first use).

After creating, tell the user:

> "Here is your wallet claim URL: `<claimUrl>`. Use this to claim ownership, set spending policies, and monitor your agent's wallet activity at https://heyvincent.ai."

**Important:** After creation, the wallet has no funds. The user must send **USDC.e (bridged USDC)** on Polygon to the Safe address before placing bets.

### 3. Get Balance

```bash
npx @vincentai/cli@latest polymarket balance --key-id <KEY_ID>
```

Returns:

- `walletAddress` — the Safe address (deployed on first call if needed)
- `collateral.balance` — USDC.e balance available for trading
- `collateral.allowance` — approved amount for Polymarket contracts

**Note:** The first balance call triggers Safe deployment and collateral approval (gasless via relayer). This may take 30-60 seconds.

### 4. Fund the Wallet

Before placing bets, the user must send USDC.e to the Safe address:

1. Get the wallet address from the balance command
2. Send USDC.e (bridged USDC, contract `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174`) on Polygon to that address
3. Minimum $1 required per bet (Polymarket minimum)

**Do not send native USDC** (`0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359`). Polymarket only accepts bridged USDC.e.

### 5. Transfer from Vincent EVM Wallet (Alternative Funding Method)

If you have a Vincent EVM wallet with funds, you can transfer directly to your Polymarket wallet using the wallet `transfer-between` commands (see the wallet skill). Vincent verifies you own both secrets and automatically handles token conversion and cross-chain bridging to get USDC.e on Polygon.

```bash
# Preview the transfer first (use your EVM wallet key-id)
npx @vincentai/cli@latest wallet transfer-between preview --key-id <EVM_KEY_ID> \
  --to-secret-id <POLYMARKET_SECRET_ID> --from-chain 8453 --to-chain 137 \
  --token-in 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913 --amount 10 \
  --token-out 0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174 --slippage 100

# Execute the transfer
npx @vincentai/cli@latest wallet transfer-between execute --key-id <EVM_KEY_ID> \
  --to-secret-id <POLYMARKET_SECRET_ID> --from-chain 8453 --to-chain 137 \
  --token-in 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913 --amount 10 \
  --token-out 0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174 --slippage 100
```

**Key points:**

- Use your **EVM wallet's key-id** (not the Polymarket key-id) for these commands
- The `--to-secret-id` must be your Polymarket wallet's secret ID
- For Polymarket destinations, only `--to-chain 137` (Polygon) and `--token-out 0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174` (USDC.e) are allowed
- The server verifies you own both secrets — transfers to other users' wallets are rejected
- For cross-chain transfers, check status with `wallet transfer-between status --key-id <EVM_KEY_ID> --relay-id <RELAY_REQUEST_ID>`

### 6. Browse & Search Markets

```bash
# Search markets by keyword (recommended)
npx @vincentai/cli@latest polymarket markets --key-id <KEY_ID> --query bitcoin --limit 20

# Search by Polymarket URL or slug
npx @vincentai/cli@latest polymarket markets --key-id <KEY_ID> --slug btc-updown-5m-1771380900

# Or use a full Polymarket URL as the slug parameter
npx @vincentai/cli@latest polymarket markets --key-id <KEY_ID> --slug https://polymarket.com/event/btc-updown-5m-1771380900

# Get all active markets
npx @vincentai/cli@latest polymarket markets --key-id <KEY_ID> --active --limit 50

# Get specific market by condition ID
npx @vincentai/cli@latest polymarket market --key-id <KEY_ID> --condition-id <CONDITION_ID>
```

**Market response includes:**

- `question`: The market question
- `outcomes`: Array like `["Yes", "No"]` or `["Team A", "Team B"]`
- `outcomePrices`: Current prices for each outcome
- `tokenIds`: **Array of token IDs for each outcome** — use these for placing bets
- `acceptingOrders`: Whether the market is open for trading
- `closed`: Whether the market has resolved

**Important:** Always use the `tokenIds` array from the market response. Each outcome has a corresponding token ID at the same index. For a "Yes/No" market:

- `tokenIds[0]` = "Yes" token ID
- `tokenIds[1]` = "No" token ID

### 7. Get Order Book

```bash
npx @vincentai/cli@latest polymarket orderbook --key-id <KEY_ID> --token-id <TOKEN_ID>
```

Returns bids and asks with prices and sizes. Use this to determine current market prices before placing orders.

### 8. Place a Bet

```bash
npx @vincentai/cli@latest polymarket bet --key-id <KEY_ID> --token-id <TOKEN_ID> --side BUY --amount 5 --price 0.55
```

Parameters:

- `--token-id`: The outcome token ID (from market data or order book)
- `--side`: `BUY` or `SELL`
- `--amount`: For BUY orders, USD amount to spend. For SELL orders, number of shares to sell.
- `--price`: Optional limit price (0.01 to 0.99). Omit for market order. ALWAYS use a market order unless the user specifies a limit price.

**BUY orders:**

- `amount` is the USD you want to spend (e.g., `5` = $5)
- You'll receive `amount / price` shares (e.g., $5 at 0.50 = 10 shares)
- Minimum order is $1

**SELL orders:**

- `amount` is the number of shares to sell
- You'll receive `amount * price` USD
- Must own the shares first (from a previous BUY)

**Important timing:** After a BUY fills, wait a few seconds before selling. Shares need time to settle on-chain.

If a trade violates a policy, the server returns an error explaining which policy was triggered. If a trade requires human approval (based on the approval threshold policy), the server returns `status: "pending_approval"` and the wallet owner receives a Telegram notification to approve or deny.

### 9. View Holdings, Open Orders & Trades

```bash
# Get current holdings with P&L (recommended for viewing positions)
npx @vincentai/cli@latest polymarket holdings --key-id <KEY_ID>

# Get open orders (unfilled limit orders in the order book)
npx @vincentai/cli@latest polymarket open-orders --key-id <KEY_ID>

# Filter open orders by market
npx @vincentai/cli@latest polymarket open-orders --key-id <KEY_ID> --market <CONDITION_ID>

# Get trade history
npx @vincentai/cli@latest polymarket trades --key-id <KEY_ID>
```

**Holdings** returns all positions with shares owned, average entry price, current price, and unrealized P&L. This is the best endpoint for:

- Checking current positions before placing sell orders
- Setting up stop-loss or take-profit rules
- Calculating total portfolio value and performance
- Showing the user their active bets

**Open Orders** returns unfilled limit orders waiting in the order book.

**Trades** returns historical trade activity.

### 10. Cancel Orders

```bash
# Cancel specific order
npx @vincentai/cli@latest polymarket cancel-order --key-id <KEY_ID> --order-id <ORDER_ID>

# Cancel all open orders
npx @vincentai/cli@latest polymarket cancel-all --key-id <KEY_ID>
```

### 11. Redeem Resolved Positions

After a market resolves, winning positions can be redeemed to convert conditional tokens back into USDC.e. Use the holdings command to check which positions have `redeemable: true`, then call redeem.

```bash
# Redeem all redeemable positions
npx @vincentai/cli@latest polymarket redeem --key-id <KEY_ID>

# Redeem specific markets by condition ID
npx @vincentai/cli@latest polymarket redeem --key-id <KEY_ID> --condition-ids 0xabc123,0xdef456
```

If no positions are redeemable, `redeemed` will be an empty array and no transaction is submitted.

**How it works:** Redemption is gasless (executed via Polymarket's relayer through the Safe). For standard markets, it calls `redeemPositions` on the CTF contract. For negative-risk markets, it calls `redeemPositions` on the NegRiskAdapter. Both types are handled automatically.

**When to redeem:** Check holdings periodically. After a market resolves, it may take some time before positions become redeemable. Look for `redeemable: true` in the holdings response.

### 12. Withdraw USDC

Transfer USDC.e from your Polymarket Safe to any Ethereum address on Polygon. This is gasless — executed via Polymarket's relayer.

```bash
npx @vincentai/cli@latest polymarket withdraw --key-id <KEY_ID> --to <RECIPIENT_ADDRESS> --amount <AMOUNT>
```

Parameters:

- `--to`: Recipient Ethereum address (0x..., 42 characters)
- `--amount`: Amount in USDC (human-readable, e.g. "100" = 100 USDC)

**Response:**

- `status`: `"executed"`, `"pending_approval"`, or `"denied"`
- `transactionHash`: Polygon transaction hash (only if executed)
- `walletAddress`: The Safe address that sent the funds

If the amount exceeds the wallet's USDC balance, the server returns an `INSUFFICIENT_BALANCE` error. Policy checks (spending limits, approval thresholds) apply to withdrawals the same way they apply to bets.

## Output Format

CLI commands return JSON to stdout. Market search results:

```json
{
  "markets": [
    {
      "question": "Will Bitcoin exceed $100k?",
      "outcomes": ["Yes", "No"],
      "outcomePrices": ["0.65", "0.35"],
      "tokenIds": ["123456...", "789012..."],
      "acceptingOrders": true
    }
  ]
}
```

Bet placement:

```json
{
  "orderId": "0x...",
  "status": "MATCHED",
  "side": "BUY",
  "price": "0.55",
  "size": "9.09"
}
```

For trades requiring human approval:

```json
{
  "status": "pending_approval",
  "message": "Transaction requires owner approval via Telegram"
}
```

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `401 Unauthorized` | Invalid or missing API key | Check that the key-id is correct; re-link if needed |
| `403 Policy Violation` | Trade blocked by server-side policy | User must adjust policies at heyvincent.ai |
| `INSUFFICIENT_BALANCE` | Not enough USDC.e for the trade | Fund the wallet with USDC.e on Polygon |
| `429 Rate Limited` | Too many requests | Wait and retry with backoff |
| `pending_approval` | Trade exceeds approval threshold | User will receive Telegram notification to approve/deny |
| `No orderbook exists` | Market closed or wrong token ID | Verify `acceptingOrders: true` and use `tokenIds[]`, not `conditionId` |
| `Key not found` | API key was revoked or never created | Re-link with a new token from the wallet owner |

## Policies (Server-Side Enforcement)

The wallet owner controls what the agent can do by setting policies via the claim URL at `https://heyvincent.ai`. All policies are enforced server-side by the Vincent API — the agent cannot bypass or modify them. If a trade violates a policy, the API rejects it. If a trade triggers an approval threshold, the API holds it and sends the wallet owner a Telegram notification for out-of-band human approval.

| Policy                      | What it does                                                     |
| --------------------------- | ---------------------------------------------------------------- |
| **Spending limit (per tx)** | Max USD value per transaction                                    |
| **Spending limit (daily)**  | Max USD value per rolling 24 hours                               |
| **Spending limit (weekly)** | Max USD value per rolling 7 days                                 |
| **Require approval**        | Every transaction needs human approval via Telegram              |
| **Approval threshold**      | Transactions above a USD amount need human approval via Telegram |

Before the wallet is claimed, the agent can operate without policy restrictions. This is by design: agent-first onboarding allows the agent to begin trading immediately. Once the human operator claims the wallet via the claim URL, they can add any combination of policies to constrain the agent's behavior. The wallet owner can also revoke the agent's API key entirely at any time.

## Re-linking (Recovering API Access)

If the agent loses its API key, the wallet owner can generate a **re-link token** from the frontend. The agent then exchanges this token for a new scoped API key.

**How it works:**

1. The user generates a re-link token from the wallet detail page at `https://heyvincent.ai`
2. The user gives the token to the agent (e.g. by pasting it in chat)
3. The agent runs the relink command:

```bash
npx @vincentai/cli@latest secret relink --token <TOKEN_FROM_USER>
```

The CLI exchanges the token for a new API key, stores it automatically, and returns the new `keyId`. Use this `keyId` for all subsequent commands.

**Important:** Re-link tokens are one-time use and expire after 10 minutes, so it's safe for users to send you a relink token through chat since you will immediately consume it.

## Workflow Example

1. **Create wallet:**

   ```bash
   npx @vincentai/cli@latest secret create --type POLYMARKET_WALLET --memo "Betting wallet"
   ```

2. **Get Safe address (triggers deployment):**

   ```bash
   npx @vincentai/cli@latest polymarket balance --key-id <KEY_ID>
   # Returns walletAddress — give this to user to fund
   ```

3. **User sends USDC.e to the Safe address on Polygon**

4. **Search for a market:**

   ```bash
   # Search by keyword — returns only active, tradeable markets
   # Tip: use short keyword phrases; stop-words like "or" can cause empty results
   npx @vincentai/cli@latest polymarket markets --key-id <KEY_ID> --query "bitcoin up down" --active
   ```

5. **Check order book for the outcome you want:**

   ```bash
   npx @vincentai/cli@latest polymarket orderbook --key-id <KEY_ID> --token-id 123456...
   ```

6. **Place BUY bet using the correct token ID:**

   ```bash
   # tokenId must be from the tokenIds array, NOT the conditionId
   npx @vincentai/cli@latest polymarket bet --key-id <KEY_ID> --token-id 123456... --side BUY --amount 5 --price 0.55
   ```

7. **Wait for settlement** (a few seconds)

8. **Sell position:**

   ```bash
   npx @vincentai/cli@latest polymarket bet --key-id <KEY_ID> --token-id 123456... --side SELL --amount 9.09 --price 0.54
   ```

9. **Redeem after market resolves** (if holding through resolution):

   ```bash
   # Check holdings for redeemable positions
   npx @vincentai/cli@latest polymarket holdings --key-id <KEY_ID>
   # If redeemable: true, redeem to get USDC.e back
   npx @vincentai/cli@latest polymarket redeem --key-id <KEY_ID>
   ```

10. **Withdraw USDC to another wallet:**

    ```bash
    npx @vincentai/cli@latest polymarket withdraw --key-id <KEY_ID> --to 0xRecipientAddress --amount 50
    ```

## Important Notes

- **After any bet or trade**, share the user's Polymarket profile link so they can verify and view their positions: `https://polymarket.com/profile/<polymarketWalletAddress>` (use the wallet's Safe address).
- **No gas needed.** All Polymarket transactions are gasless via Polymarket's relayer.
- **Never try to access raw secret values.** The private key stays server-side — that's the whole point.
- Always share the claim URL with the user after creating a wallet.
- If a transaction is rejected, it may be blocked by a server-side policy. Tell the user to check their policy settings at `https://heyvincent.ai`.
- If a transaction requires approval, it will return `status: "pending_approval"`. The wallet owner will receive a Telegram notification to approve or deny.

See the **Error Handling** section above for a full list of common errors and resolutions.
```

## File: `trading-engine/SKILL.md`
```markdown
---
name: Vincent - Trading Engine for agents
description: |
  Strategy-driven automated trading for Polymarket and HyperLiquid. Use this skill when users want to create
  trading strategies, set stop-loss/take-profit/trailing stop rules, or manage automated trading.
  Triggers on "trading strategy", "stop loss", "take profit", "trailing stop", "automated trading",
  "trading engine", "trade rules", "strategy monitor".
allowed-tools: Read, Write, Bash(npx:@vincentai/cli*)
version: 1.0.0
author: HeyVincent <contact@heyvincent.ai>
license: MIT
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/agentwallet
        - ./agentwallet
---

# Vincent Trading Engine - Strategy-Driven Automated Trading

Use this skill to create and manage automated trading strategies for Polymarket prediction markets and HyperLiquid perpetuals/spot. The Trading Engine combines driver-based monitoring (web search, Twitter, newswire, price feeds) with a signal pipeline and LLM-powered decision-making to automatically trade based on your thesis. It also includes standalone stop-loss, take-profit, and trailing stop rules that work without the LLM.

All commands use the `@vincentai/cli` package.

## How It Works

**The Trading Engine is a unified system with two modes:**

1. **LLM-Powered Strategies** — Create a versioned strategy with a structured thesis, weighted drivers (web search keywords, Twitter accounts, newswire topics, price triggers), and an escalation policy. When drivers detect new information, signals are scored and batched. When the escalation threshold is met, an LLM (Claude via OpenRouter) evaluates the signals against your thesis and decides whether to trade, update the thesis, set protective orders, or alert you.
2. **Standalone Trade Rules** — Set stop-loss, take-profit, and trailing stop rules on positions. These execute automatically when price conditions are met — no LLM involved.

**Architecture:**

- Integrated into the Vincent backend (no separate service to run)
- Strategy endpoints under `/api/skills/polymarket/strategies/...`
- Trade rule endpoints under `/api/skills/polymarket/rules/...`
- HyperLiquid rules use `venue: "hyperliquid"` and route through the HL adapter
- Uses the same API key as the Polymarket or HyperLiquid skill (depending on venue)
- All trades go through Vincent's policy-enforced pipeline
- LLM costs are metered and deducted from the user's credit balance
- Every LLM invocation is recorded with full audit trail (tokens, cost, actions, duration)

## Security Model

- **LLM cannot bypass policies** — all trades go through the venue's policy-enforced skill (`polymarketSkill.placeBet()` or `hyperliquidSkill.trade()`) which enforces spending limits, approval thresholds, and allowlists
- **Backend-side LLM key** — the OpenRouter API key never leaves the server. Agents and users cannot invoke the LLM directly
- **Credit gating** — no LLM invocation without sufficient credit balance
- **Tool constraints** — the LLM's available tools are controlled by the strategy's `config.tools` settings. If `canTrade: false`, the trade tool is not provided
- **Rate limiting** — max concurrent LLM invocations is capped to prevent runaway costs
- **Audit trail** — every invocation is recorded with full prompt, response, actions, cost, and duration
- **No private keys** — the Trading Engine uses the Vincent API for all trades. Private keys stay on Vincent's servers

## Part 1: LLM-Powered Strategies

### Core Concepts

- **Instrument**: A tradeable asset on a venue. Defined by `id`, `type` (stock, perp, swap, binary, option), `venue`, and optional constraints (leverage, margin, liquidity, fees).
- **Thesis**: Your directional view — `estimate` (target price/value), `direction` (long/short/neutral), `confidence` (0–1), and `reasoning`.
- **Driver**: A named information source that feeds the signal pipeline. Each driver has a `weight`, `direction` (bullish/bearish/contextual), and `monitoring` config (entities, keywords, embedding anchor, sources, polling interval).
- **Escalation Policy**: Controls when the LLM is woken up. `signalScoreThreshold` (minimum score to batch), `highConfidenceThreshold` (score that triggers immediate wake), `maxWakeFrequency` (e.g. "1 per 15m"), `batchWindow` (e.g. "5m").
- **Trade Rules**: Entry rules (min edge, order type), exit rules (thesis invalidation triggers), auto-actions (stop-loss, take-profit, trailing stop, price delta triggers), and sizing rules (method, max position, portfolio %, max trades/day).

### Signal Pipeline

Strategies process information through a 6-layer pipeline:

1. **Ingest** — Raw data from driver sources (web search, Twitter, newswire, price feeds, RSS, Reddit, on-chain, filings, options flow)
2. **Filter** — Deduplication and relevance filtering. Drops signals already seen or below quality threshold
3. **Score** — Each signal is scored (0–1) based on driver weight, embedding similarity to the anchor, and entity/keyword matches
4. **Escalate** — Scored signals are batched according to the escalation policy. Low-score signals accumulate in a batch window; high-confidence signals trigger immediate LLM wake
5. **LLM** — The LLM evaluates batched signals against the current thesis. It can update the thesis, issue trade decisions, update driver states, or take no action
6. **Execute** — Trade decisions pass through policy enforcement and are routed to the appropriate venue adapter for execution

### Strategy Lifecycle

Strategies follow a versioned lifecycle: `DRAFT` → `ACTIVE` → `PAUSED` → `ARCHIVED`

- **DRAFT**: Can be edited. Not yet monitoring or invoking the LLM.
- **ACTIVE**: Drivers are running. New signals trigger the pipeline.
- **PAUSED**: Monitoring is stopped. Can be resumed.
- **ARCHIVED**: Permanently stopped. Cannot be reactivated.

To iterate on a strategy, duplicate it as a new version (creates a new DRAFT with incremented version number and the same config).

### Create a Strategy

```bash
npx @vincentai/cli@latest trading-engine create-strategy \
  --key-id <KEY_ID> \
  --name "BTC Momentum" \
  --config '{
    "instruments": [
      { "id": "btc-usd-perp", "type": "perp", "venue": "polymarket" },
      { "id": "BTC", "type": "perp", "venue": "hyperliquid" }
    ],
    "thesis": {
      "estimate": 105000,
      "direction": "long",
      "confidence": 0.7,
      "reasoning": "ETF inflows accelerating, halving supply shock imminent"
    },
    "drivers": [
      {
        "name": "ETF Flow Monitor",
        "weight": 2.0,
        "direction": "bullish",
        "monitoring": {
          "entities": ["BlackRock", "Fidelity"],
          "keywords": ["bitcoin ETF", "BTC inflow"],
          "embeddingAnchor": "Bitcoin ETF institutional inflows",
          "sources": ["web_search", "newswire"]
        }
      },
      {
        "name": "Crypto Twitter",
        "weight": 1.0,
        "direction": "contextual",
        "monitoring": {
          "entities": ["@BitcoinMagazine", "@saborskycnbc"],
          "keywords": ["bitcoin", "BTC"],
          "sources": ["twitter"]
        }
      }
    ],
    "escalation": {
      "signalScoreThreshold": 0.3,
      "highConfidenceThreshold": 0.8,
      "maxWakeFrequency": "1 per 15m",
      "batchWindow": "5m"
    },
    "tradeRules": {
      "entry": { "minEdge": 0.05, "orderType": "limit", "limitOffset": 0.01 },
      "autoActions": { "stopLoss": -0.10, "takeProfit": 0.25, "trailingStop": -0.05 },
      "exit": { "thesisInvalidation": ["ETF outflows exceed $500M/week"] },
      "sizing": {
        "method": "edgeScaled",
        "maxPosition": 500,
        "maxPortfolioPct": 20,
        "maxTradesPerDay": 5,
        "minTimeBetweenTrades": "30m"
      }
    },
    "notifications": {
      "onTrade": true,
      "onThesisChange": true,
      "channel": "none"
    }
  }'
```

**Parameters:**

- `--name`: Strategy name
- `--config`: Full strategy config JSON (see Core Concepts above for structure)
- `--data-source-secret-id`: Optional DATA_SOURCES secret ID for driver monitoring API calls
- `--poll-interval`: Polling interval in minutes for driver monitoring (default: 15)

### List Strategies

```bash
npx @vincentai/cli@latest trading-engine list-strategies --key-id <KEY_ID>
```

### Get Strategy Details

```bash
npx @vincentai/cli@latest trading-engine get-strategy --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Update a Strategy

Update a DRAFT strategy. Pass only the fields you want to change — config is a partial object.

```bash
npx @vincentai/cli@latest trading-engine update-strategy --key-id <KEY_ID> --strategy-id <STRATEGY_ID> \
  --name "Updated Name" --config '{ "thesis": { "confidence": 0.8, "reasoning": "Updated reasoning" } }'
```

**Parameters:**

- `--strategy-id`: Strategy ID (required)
- `--name`: New strategy name
- `--config`: Partial strategy config JSON — only include fields to update
- `--data-source-secret-id`: DATA_SOURCES secret ID
- `--poll-interval`: New polling interval in minutes

### Activate a Strategy

Starts driver monitoring and signal pipeline processing. Strategy must be in DRAFT status.

```bash
npx @vincentai/cli@latest trading-engine activate --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Pause a Strategy

Stops monitoring. Strategy must be ACTIVE.

```bash
npx @vincentai/cli@latest trading-engine pause --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Resume a Strategy

Resumes monitoring. Strategy must be PAUSED.

```bash
npx @vincentai/cli@latest trading-engine resume --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Archive a Strategy

Permanently stops a strategy. Cannot be undone.

```bash
npx @vincentai/cli@latest trading-engine archive --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Duplicate a Strategy (New Version)

Creates a new DRAFT with the same config, incremented version number, and a link to the parent version.

```bash
npx @vincentai/cli@latest trading-engine duplicate-strategy --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### View Version History

See all versions of a strategy lineage.

```bash
npx @vincentai/cli@latest trading-engine versions --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### View LLM Invocation History

See the LLM decision log for a strategy — what data triggered it, what the LLM decided, what actions were taken, and the cost.

```bash
npx @vincentai/cli@latest trading-engine invocations --key-id <KEY_ID> --strategy-id <STRATEGY_ID> --limit 20
```

### View Cost Summary

See aggregate LLM costs for all strategies under a secret.

```bash
npx @vincentai/cli@latest trading-engine costs --key-id <KEY_ID>
```

### View Performance Metrics

See performance metrics for a strategy: P&L, win rate, trade count, and per-instrument breakdown.

```bash
npx @vincentai/cli@latest trading-engine performance --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Driver Configuration

#### Web Search Drivers

Add a driver with `"sources": ["web_search"]`. The engine periodically searches Brave for the driver's keywords and triggers the signal pipeline when new results appear.

```json
{
  "name": "AI News Monitor",
  "weight": 1.5,
  "direction": "bullish",
  "monitoring": {
    "keywords": ["AI tokens", "GPU shortage", "prediction market regulation"],
    "embeddingAnchor": "AI technology investment trends",
    "sources": ["web_search"]
  }
}
```

Each keyword is searched independently. Results are deduplicated — the same URLs won't trigger the pipeline twice.

#### Twitter Drivers

Add a driver with `"sources": ["twitter"]`. The engine periodically checks the specified entities for new tweets.

```json
{
  "name": "Crypto Twitter",
  "weight": 1.0,
  "direction": "contextual",
  "monitoring": {
    "entities": ["@DeepSeek", "@nvidia", "@OpenAI"],
    "keywords": ["AI", "GPU"],
    "sources": ["twitter"]
  }
}
```

Tweets are deduplicated by tweet ID — only genuinely new tweets trigger the pipeline.

#### Newswire Drivers (Finnhub)

Add a driver with `"sources": ["newswire"]`. The engine periodically polls Finnhub's market news API and triggers the pipeline when new headlines matching your keywords appear.

```json
{
  "name": "Market News",
  "weight": 1.5,
  "direction": "contextual",
  "monitoring": {
    "keywords": ["artificial intelligence", "GPU shortage", "semiconductor"],
    "sources": ["newswire"]
  }
}
```

Headlines and summaries are matched case-insensitively. Articles are deduplicated by headline hash with a sliding window.

**Note:** Requires a `FINNHUB_API_KEY` env var on the server. Finnhub's free tier allows 60 API calls/min. No per-call credit deduction.

#### Price Triggers

Price triggers are evaluated in real-time via the Polymarket WebSocket feed. When a price condition is met, the signal pipeline is invoked with the price data.

Trigger types:

- `ABOVE` — triggers when price exceeds a threshold
- `BELOW` — triggers when price drops below a threshold
- `CHANGE_PCT` — triggers on a percentage change from reference price

Price triggers are one-shot: once fired, they're marked as consumed. The LLM can create new triggers if needed.

### Thesis Best Practices

The thesis is your structured directional view. Good theses include:

1. **A clear estimate**: Target price or value the market should reach
2. **A confidence level**: Start at 0.5–0.7 and let the LLM adjust as new data arrives
3. **Specific reasoning**: "ETF inflows accelerating, halving supply shock imminent" is better than "BTC will go up"
4. **Explicit invalidation conditions**: Use `tradeRules.exit.thesisInvalidation` to define what would break your thesis

### LLM Available Tools

When the LLM is invoked, it can use these tools (depending on strategy config):

| Tool                | Description                        | Requires                           |
| ------------------- | ---------------------------------- | ---------------------------------- |
| `place_trade`       | Buy or sell a position             | `canTrade: true` in trade rules    |
| `set_stop_loss`     | Set a stop-loss rule on a position | `canSetRules: true` in trade rules |
| `set_take_profit`   | Set a take-profit rule             | `canSetRules: true` in trade rules |
| `set_trailing_stop` | Set a trailing stop                | `canSetRules: true` in trade rules |
| `alert_user`        | Send an alert without trading      | Always available                   |
| `no_action`         | Do nothing (with reasoning)        | Always available                   |

### Cost Tracking

Every LLM invocation is metered:

- **Token costs**: Input and output tokens are priced per the model's rate
- **Deducted from credit balance**: Same pool as data source credits (`dataSourceCreditUsd`)
- **Pre-flight check**: If insufficient credit, the invocation is skipped and logged
- **Data source costs**: Brave Search (~$0.005/call) and Twitter (~$0.005-$0.01/call) are also metered. Finnhub newswire calls are free (no credit deduction)

Typical LLM invocation cost: $0.05–$0.30 depending on context size.

---

## Part 2: Standalone Trade Rules

Trade rules execute automatically when price conditions are met — no LLM involved. These are stop-loss, take-profit, and trailing stop rules that protect your positions.

### Check Worker Status

```bash
npx @vincentai/cli@latest trading-engine status --key-id <KEY_ID>
# Returns: worker status, active rules count, last sync time, circuit breaker state
```

### Create a Stop-Loss Rule

Automatically sell a position if price drops below a threshold:

```bash
# Polymarket — triggerPrice is 0–1 (outcome token price)
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --market-id 0x123... --token-id 456789 \
  --rule-type STOP_LOSS --trigger-price 0.40

# HyperLiquid — triggerPrice is absolute USD price, marketId and tokenId are the coin name
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id BTC --token-id BTC \
  --rule-type STOP_LOSS --trigger-price 95000
```

**Parameters:**

- `--venue`: `polymarket` (default) or `hyperliquid`
- `--market-id`: Polymarket condition ID, or coin name for HyperLiquid (e.g. `BTC`, `ETH`)
- `--token-id`: Polymarket outcome token ID, or coin name for HyperLiquid
- `--rule-type`: `STOP_LOSS` (sells if price <= trigger), `TAKE_PROFIT` (sells if price >= trigger), or `TRAILING_STOP`
- `--trigger-price`: Price threshold — 0 to 1 for Polymarket, absolute USD price for HyperLiquid

### Create a Take-Profit Rule

Automatically sell a position if price rises above a threshold:

```bash
# Polymarket
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --market-id 0x123... --token-id 456789 \
  --rule-type TAKE_PROFIT --trigger-price 0.75

# HyperLiquid
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id ETH --token-id ETH \
  --rule-type TAKE_PROFIT --trigger-price 4500
```

### Create a Trailing Stop Rule

A trailing stop moves the stop price up as the price rises:

```bash
# Polymarket
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --market-id 0x123... --token-id 456789 \
  --rule-type TRAILING_STOP --trigger-price 0.45 --trailing-percent 5

# HyperLiquid
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id SOL --token-id SOL \
  --rule-type TRAILING_STOP --trigger-price 170 --trailing-percent 5
```

**Trailing stop behavior:**

- `--trailing-percent` is percent points (e.g. `5` = 5%)
- Computes `candidateStop = currentPrice * (1 - trailingPercent/100)`
- If `candidateStop` > current `triggerPrice`, updates `triggerPrice`
- `triggerPrice` never moves down
- Rule triggers when `currentPrice <= triggerPrice`

### List Rules

```bash
# All rules
npx @vincentai/cli@latest trading-engine list-rules --key-id <KEY_ID>

# Filter by status
npx @vincentai/cli@latest trading-engine list-rules --key-id <KEY_ID> --status ACTIVE
```

### Update a Rule

```bash
npx @vincentai/cli@latest trading-engine update-rule --key-id <KEY_ID> --rule-id <RULE_ID> --trigger-price 0.45
```

### Cancel a Rule

```bash
npx @vincentai/cli@latest trading-engine delete-rule --key-id <KEY_ID> --rule-id <RULE_ID>
```

### View Monitored Positions

```bash
npx @vincentai/cli@latest trading-engine positions --key-id <KEY_ID>
```

### View Event Log

```bash
# All events
npx @vincentai/cli@latest trading-engine events --key-id <KEY_ID>

# Events for specific rule
npx @vincentai/cli@latest trading-engine events --key-id <KEY_ID> --rule-id <RULE_ID>

# Paginated
npx @vincentai/cli@latest trading-engine events --key-id <KEY_ID> --limit 50 --offset 100
```

**Event types:**

- `RULE_CREATED` — Rule was created
- `RULE_TRAILING_UPDATED` — Trailing stop moved triggerPrice upward
- `RULE_EVALUATED` — Worker checked the rule against current price
- `RULE_TRIGGERED` — Trigger condition was met
- `ACTION_PENDING_APPROVAL` — Trade requires human approval, rule paused
- `ACTION_EXECUTED` — Trade executed successfully
- `ACTION_FAILED` — Trade execution failed
- `RULE_CANCELED` — Rule was manually canceled

### Rule Statuses

- `ACTIVE` — Rule is live and being monitored
- `TRIGGERED` — Condition was met, trade executed
- `PENDING_APPROVAL` — Trade requires human approval; rule paused
- `CANCELED` — Manually canceled before triggering
- `FAILED` — Triggered but trade execution failed

---

## Complete Workflow: Strategy + Trade Rules

### Polymarket Workflow

### Step 1: Place a bet with the Polymarket skill

```bash
npx @vincentai/cli@latest polymarket bet --key-id <KEY_ID> --token-id 123456789 --side BUY --amount 10 --price 0.55
```

### Step 2: Create a strategy to monitor the thesis

```bash
npx @vincentai/cli@latest trading-engine create-strategy --key-id <KEY_ID> \
  --name "Bitcoin Bull Thesis" \
  --config '{
    "instruments": [
      { "id": "123456789", "type": "binary", "venue": "polymarket" }
    ],
    "thesis": {
      "estimate": 0.85,
      "direction": "long",
      "confidence": 0.7,
      "reasoning": "Bitcoin is likely to break $100k on ETF inflows"
    },
    "drivers": [
      {
        "name": "ETF News",
        "weight": 2.0,
        "direction": "bullish",
        "monitoring": {
          "keywords": ["bitcoin ETF inflows", "bitcoin institutional"],
          "sources": ["web_search", "newswire"]
        }
      },
      {
        "name": "Crypto Twitter",
        "weight": 1.0,
        "direction": "contextual",
        "monitoring": {
          "entities": ["@BitcoinMagazine", "@saborskycnbc"],
          "sources": ["twitter"]
        }
      }
    ],
    "escalation": {
      "signalScoreThreshold": 0.3,
      "highConfidenceThreshold": 0.8,
      "maxWakeFrequency": "1 per 15m",
      "batchWindow": "5m"
    },
    "tradeRules": {
      "entry": { "minEdge": 0.05 },
      "autoActions": { "stopLoss": -0.15, "takeProfit": 0.30, "trailingStop": -0.05 },
      "exit": { "thesisInvalidation": ["ETF outflows accelerate above $500M/week"] },
      "sizing": { "method": "edgeScaled", "maxPosition": 100, "maxPortfolioPct": 20, "maxTradesPerDay": 5 }
    }
  }' \
  --poll-interval 10
```

### Step 3: Set a standalone stop-loss as immediate protection

```bash
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --market-id 0xabc... --token-id 123456789 \
  --rule-type STOP_LOSS --trigger-price 0.40
```

### Step 4: Activate the strategy

```bash
npx @vincentai/cli@latest trading-engine activate --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### Step 5: Monitor activity

```bash
# Check strategy invocations
npx @vincentai/cli@latest trading-engine invocations --key-id <KEY_ID> --strategy-id <STRATEGY_ID>

# Check trade rule events
npx @vincentai/cli@latest trading-engine events --key-id <KEY_ID>

# Check costs
npx @vincentai/cli@latest trading-engine costs --key-id <KEY_ID>

# Check performance
npx @vincentai/cli@latest trading-engine performance --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
```

### HyperLiquid Workflow

### Step 1: Open a perp position with the HyperLiquid skill

```bash
npx @vincentai/cli@latest hyperliquid trade --key-id <KEY_ID> \
  --coin BTC --is-buy true --sz 0.001 --limit-px 106000 --order-type market
```

### Step 2: Set a stop-loss rule for the position

```bash
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id BTC --token-id BTC \
  --rule-type STOP_LOSS --trigger-price 95000
```

### Step 3: Set a take-profit rule

```bash
npx @vincentai/cli@latest trading-engine create-rule --key-id <KEY_ID> \
  --venue hyperliquid --market-id BTC --token-id BTC \
  --rule-type TAKE_PROFIT --trigger-price 115000
```

### Step 4: Create a strategy to monitor your thesis

```bash
npx @vincentai/cli@latest trading-engine create-strategy --key-id <KEY_ID> \
  --name "BTC Perp Momentum" \
  --config '{
    "instruments": [
      { "id": "BTC", "type": "perp", "venue": "hyperliquid" }
    ],
    "thesis": {
      "estimate": 115000,
      "direction": "long",
      "confidence": 0.7,
      "reasoning": "ETF inflows accelerating, halving supply shock imminent"
    },
    "drivers": [
      {
        "name": "ETF News",
        "weight": 2.0,
        "direction": "bullish",
        "monitoring": {
          "keywords": ["bitcoin ETF inflows", "bitcoin institutional"],
          "sources": ["web_search", "newswire"]
        }
      }
    ],
    "escalation": {
      "signalScoreThreshold": 0.3,
      "highConfidenceThreshold": 0.8,
      "maxWakeFrequency": "1 per 15m",
      "batchWindow": "5m"
    },
    "tradeRules": {
      "entry": { "minEdge": 0.05 },
      "autoActions": { "stopLoss": -0.10, "takeProfit": 0.25, "trailingStop": -0.05 },
      "sizing": { "method": "edgeScaled", "maxPosition": 500, "maxPortfolioPct": 20, "maxTradesPerDay": 5 }
    }
  }' \
  --poll-interval 10
```

### Step 5: Activate and monitor

```bash
npx @vincentai/cli@latest trading-engine activate --key-id <KEY_ID> --strategy-id <STRATEGY_ID>
npx @vincentai/cli@latest trading-engine events --key-id <KEY_ID>
```

---

## Background Workers

The Trading Engine runs two independent background workers:

1. **Strategy Engine Worker** — Ticks every 30s, checks which strategy drivers are due, fetches new data, scores signals, and invokes the LLM when the escalation threshold is met. Hooks into venue WebSocket feeds (Polymarket and HyperLiquid) for real-time price trigger evaluation.
2. **Trade Rule Worker** — Monitors prices in real-time via WebSocket (with polling fallback), evaluates stop-loss/take-profit/trailing stop rules, executes trades when conditions are met. Supports both Polymarket and HyperLiquid venues.

**Circuit Breaker:** Both workers use a circuit breaker pattern. If a venue API fails 5+ consecutive times, the worker pauses and resumes after a cooldown. Check status with:

```bash
npx @vincentai/cli@latest trading-engine status --key-id <KEY_ID>
```

## Best Practices

1. **Start with `confidence: 0.5`** and let the LLM adjust — avoid overconfidence in the initial thesis
2. **Weight drivers by importance** — a driver with `weight: 3.0` has 3x the signal score contribution of `weight: 1.0`
3. **Use `edgeScaled` sizing** for adaptive position sizes based on thesis confidence and edge
4. **Set `maxPortfolioPct`** to limit exposure — even high-confidence strategies shouldn't risk the entire portfolio
5. **Set both stop-loss and take-profit** on positions for protection (via `autoActions` in the config or standalone rules)
6. **Use `thesisInvalidation` exit rules** to define explicit conditions that should trigger position exits
7. **Monitor invocation costs** — check the costs command regularly
8. **Iterate with versions** — duplicate a strategy to tweak the config without losing the original
9. **Don't set triggers too close** to current price — market noise can trigger prematurely

## Example User Prompts

When a user says:

- **"Create a strategy to monitor AI tokens"** → Create strategy with web search + Twitter drivers
- **"Set a stop-loss at 40 cents"** → Create STOP_LOSS rule
- **"What has my strategy been doing?"** → Show invocations for the strategy
- **"How is my strategy performing?"** → Show performance metrics
- **"How much has the trading engine cost me?"** → Show cost summary
- **"Pause my strategy"** → Pause the strategy
- **"Make a new version with a different thesis"** → Duplicate, then update the draft
- **"Set a 5% trailing stop"** → Create TRAILING_STOP rule

## Output Format

Strategy creation:

```json
{
  "strategyId": "strat-123",
  "name": "BTC Momentum",
  "status": "DRAFT",
  "version": 1
}
```

Rule creation:

```json
{
  "ruleId": "rule-456",
  "ruleType": "STOP_LOSS",
  "triggerPrice": 0.4,
  "status": "ACTIVE"
}
```

LLM invocation log entries:

```json
{
  "invocationId": "inv-789",
  "strategyId": "strat-123",
  "trigger": "web_search",
  "actions": ["place_trade"],
  "costUsd": 0.12,
  "createdAt": "2026-02-26T12:00:00.000Z"
}
```

## Error Handling

| Error                       | Cause                                             | Resolution                                           |
| --------------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| `401 Unauthorized`          | Invalid or missing API key                        | Check that the key-id is correct; re-link if needed  |
| `403 Policy Violation`      | Trade blocked by server-side policy               | User must adjust policies at heyvincent.ai           |
| `402 Insufficient Credit`   | Not enough credit for LLM invocation              | User must add credit at heyvincent.ai                |
| `INVALID_STATUS_TRANSITION` | Strategy can't transition to requested state      | Check current status (e.g., only DRAFT can activate) |
| `CIRCUIT_BREAKER_OPEN`      | Polymarket API failures triggered circuit breaker | Wait for cooldown; check status command              |
| `429 Rate Limited`          | Too many requests or concurrent LLM invocations   | Wait and retry with backoff                          |
| `Key not found`             | API key was revoked or never created              | Re-link with a new token from the wallet owner       |

## Important Notes

- **Authorization:** All endpoints require the API key for the relevant venue (Polymarket or HyperLiquid wallet key)
- **Local only:** The API listens on `localhost:19000` — only accessible from the same VPS
- **No private keys:** All trades use the Vincent API — your private key stays secure on Vincent's servers
- **Policy enforcement:** All trades (both LLM and standalone rules) go through Vincent's policy checks
- **Idempotency:** Rules only trigger once. LLM invocations are deduplicated by driver state.
```

## File: `twitter/SKILL.md`
```markdown
---
name: Vincent - Twitter / X.com for agents
description: |
  Twitter/X.com data access for agents. Use this skill when users want to search tweets, look up
  user profiles, or retrieve recent tweets. Pay-per-call via Vincent credit system.
  Triggers on "search tweets", "twitter", "X.com", "look up user", "tweet search",
  "twitter profile", "recent tweets".
allowed-tools: Read, Write, Bash(npx:@vincentai/cli*), Bash(jq:*), Bash(bc:*)
version: 1.0.0
author: HeyVincent <contact@heyvincent.ai>
license: MIT
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/datasources
        - ./datasources
---

# Vincent - Twitter / X.com for agents

Use this skill to search tweets, look up user profiles, and retrieve recent tweets from X.com (Twitter). All requests are proxied through the Vincent backend, which handles authentication with the X API, enforces rate limits, tracks per-call costs, and deducts from your credit balance automatically.

**No API keys to manage.** The agent authenticates with a Vincent API key scoped to a `DATA_SOURCES` secret. Vincent handles the upstream Twitter API credentials server-side -- the agent never sees or manages Twitter API keys.

All commands use the `@vincentai/cli` package. API keys are stored and resolved automatically — you never handle raw keys or file paths.

## Security Model

This skill is designed for **autonomous agent operation with pay-per-call pricing and human oversight**.

**No environment variables are required** because this skill uses agent-first onboarding: the agent creates a `DATA_SOURCES` secret at runtime by calling the Vincent API, which returns a scoped API key. The CLI stores the returned API key automatically during creation. The config paths where the key is persisted (`${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/datasources/` or `./datasources/`) are declared in this skill's metadata.

**The agent's API key is not a Twitter API key.** It is a scoped Bearer token for the Vincent proxy. The Vincent server authenticates with Twitter on the agent's behalf. The agent cannot access the upstream API directly or bypass the proxy's credit and rate-limit enforcement.

**Model invocation is intentionally enabled.** The purpose of this skill is to give AI agents autonomous access to Twitter data. The agent is expected to search tweets and look up profiles on its own. The human controls spending through credit balance and payment method management at `https://heyvincent.ai`.

**All API calls go exclusively to `heyvincent.ai`** over HTTPS/TLS. The Vincent server then calls the Twitter API. The agent does not contact Twitter directly.

**Key lifecycle:**

- **Creation**: The agent runs `secret create` with `--type DATA_SOURCES` — the CLI stores the API key automatically and returns a `keyId` and `claimUrl`.
- **Claim**: The human operator uses the claim URL to take ownership, add credit, and manage payment at `https://heyvincent.ai`.
- **Credit**: Each API call costs a small amount (see Pricing below). The human adds credit via the frontend. Calls are rejected when credit runs out and no payment method is on file.
- **Revocation**: The secret owner can revoke the agent's API key at any time from the Vincent frontend.

## Pricing

| Endpoint | Cost per call |
| --- | --- |
| Search tweets | $0.01 |
| Get tweet by ID | $0.005 |
| Get user profile | $0.005 |
| Get user's tweets | $0.01 |

Credit is deducted automatically per call. The response includes `_vincent.creditRemainingUsd` so the agent can track remaining balance.

## Quick Start

### 1. Check for Existing Keys

Before creating a new secret, check if one already exists:

```bash
npx @vincentai/cli@latest secret list --type DATA_SOURCES
```

If a key is returned, use its `id` as the `--key-id` for all subsequent commands. If no keys exist, create a new secret.

### 2. Create a Data Sources Secret

```bash
npx @vincentai/cli@latest secret create --type DATA_SOURCES --memo "My agent data sources"
```

Returns `keyId` (use for all future commands) and `claimUrl` (share with the user).

After creating, tell the user:

> "Here is your data sources claim URL: `<claimUrl>`. Use this to claim ownership and add credit for Twitter and other data sources at https://heyvincent.ai."

**Important:** The secret must be claimed and have credit (or a payment method on file) before API calls will succeed.

### 3. Search Tweets

```bash
npx @vincentai/cli@latest twitter search --key-id <KEY_ID> --q bitcoin --max-results 10
```

Parameters:

- `--q` (required): Search query (1-512 characters)
- `--max-results` (optional): Number of results, 10-100 (default: 10)
- `--start-time` (optional): ISO 8601 datetime, earliest tweets to return
- `--end-time` (optional): ISO 8601 datetime, latest tweets to return

Returns tweet text, creation time, author ID, and public metrics (likes, retweets, replies).

### 4. Get a Specific Tweet

```bash
npx @vincentai/cli@latest twitter tweet --key-id <KEY_ID> --tweet-id <TWEET_ID>
```

### 5. Get User Profile

Look up a Twitter user by username.

```bash
npx @vincentai/cli@latest twitter user --key-id <KEY_ID> --username elonmusk
```

Returns the user's description, follower/following counts, profile image, and verified status.

### 6. Get a User's Recent Tweets

```bash
npx @vincentai/cli@latest twitter user-tweets --key-id <KEY_ID> --user-id <USER_ID> --max-results 10
```

**Note:** This command requires the user's numeric ID (from the user profile response), not the username.

## Response Metadata

Every successful response includes a `_vincent` object with:

```json
{
  "_vincent": {
    "costUsd": 0.01,
    "creditRemainingUsd": 4.99
  }
}
```

Use `creditRemainingUsd` to warn the user when credit is running low.

## Output Format

Tweet search results:

```json
{
  "data": [
    {
      "id": "123456789",
      "text": "Tweet content here",
      "created_at": "2026-02-26T12:00:00.000Z",
      "author_id": "987654321",
      "public_metrics": {
        "like_count": 42,
        "retweet_count": 10,
        "reply_count": 5
      }
    }
  ],
  "_vincent": {
    "costUsd": 0.01,
    "creditRemainingUsd": 4.99
  }
}
```

User profile responses include `description`, `public_metrics` (followers/following counts), `profile_image_url`, and `verified`.

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `401 Unauthorized` | Invalid or missing API key | Check that the key-id is correct; re-link if needed |
| `402 Insufficient Credit` | Credit balance is zero and no payment method on file | User must add credit at heyvincent.ai |
| `429 Rate Limited` | Exceeded 60 requests/minute | Wait and retry with backoff |
| `Key not found` | API key was revoked or never created | Re-link with a new token from the secret owner |
| `User not found` | Username doesn't exist on Twitter | Verify the username spelling |

## Rate Limits

- 60 requests per minute per API key across all data source endpoints (Twitter + Brave Search combined)
- If rate limited, you'll receive a `429` response. Wait and retry.

## Re-linking (Recovering API Access)

If the agent loses its API key, the secret owner can generate a **re-link token** from the frontend. The agent then exchanges this token for a new API key.

```bash
npx @vincentai/cli@latest secret relink --token <TOKEN_FROM_USER>
```

The CLI exchanges the token for a new API key, stores it automatically, and returns the new `keyId`. Re-link tokens are one-time use and expire after 10 minutes.

## Adding Credits

When your credit balance runs low, you can purchase more credits autonomously using USDC on Base via the x402 payment protocol — no human intervention required.

**Available tiers:** $1, $5, $10, $25, $50, $100

### Check Balance

```bash
npx @vincentai/cli@latest credits balance --key-id <KEY_ID>
```

### Purchase Credits via x402 (USDC on Base)

```bash
npx @vincentai/cli@latest credits add --key-id <KEY_ID> --amount 10
```

**How it works:**

1. The CLI sends a POST request to the x402 credit endpoint
2. The server returns HTTP 402 with a dynamic USDC deposit address on Base
3. The CLI signs the payment using your agent's wallet
4. The CLI retries the request with the payment proof
5. The server verifies the payment and adds credits to your account

**Requirements:**
- An x402-compatible wallet with USDC on Base (chain ID 8453)
- Your Vincent DATA_SOURCES API key

### Purchase Credits via Card (Human)

```bash
npx @vincentai/cli@latest credits checkout --key-id <KEY_ID>
```

Returns a Stripe Checkout URL. Share this with the user to complete payment with a card.

### MCP Tools

| Tool | Description |
| --- | --- |
| `vincent_credit_balance` | Check current credit balance and top-up options |
| `vincent_add_credits` | Get x402 payment instructions for purchasing credits |

### Auto-Replenish Pattern

For long-running agents, check your balance before expensive operations and top up when low:

```bash
BALANCE=$(npx @vincentai/cli@latest credits balance --key-id <KEY_ID> --json | jq -r '.balance')
if (( $(echo "$BALANCE < 2.00" | bc -l) )); then
  npx @vincentai/cli@latest credits add --key-id <KEY_ID> --amount 10
fi
```

## Important Notes

- A single `DATA_SOURCES` API key works for **all** data sources (Twitter, Brave Search, etc.). You do not need a separate key per data source.
- Always share the claim URL with the user after creating a secret.
- If a call is rejected with a credit error, tell the user to add credit at `https://heyvincent.ai`.
- The Twitter search endpoint only returns tweets from the last 7 days (X API v2 limitation for recent search).
```

## File: `wallet/SKILL.md`
```markdown
---
name: Vincent - A wallet for agents
description: |
  The agent's wallet for EVM chain transactions and raw signing. Use this skill when users want to
  create a wallet, transfer tokens, swap on DEXs, interact with smart contracts, or sign messages.
  Triggers on "wallet", "create wallet", "transfer ETH", "swap tokens", "send transaction",
  "check balance", "EVM wallet", "raw signer", "sign message".
allowed-tools: Read, Write, Bash(npx:@vincentai/cli*)
version: 1.0.0
author: HeyVincent <contact@heyvincent.ai>
license: MIT
homepage: https://heyvincent.ai
source: https://github.com/HeyVincent-ai/Vincent
metadata:
  clawdbot:
    homepage: https://heyvincent.ai
    requires:
      config:
        - ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/agentwallet
        - ./agentwallet
---

# Vincent - A wallet for agents

Use this skill to safely create a wallet the agent can use for transfers, swaps, and any EVM chain transaction without ever exposing private keys to the agent. Create a wallet, set spending policies, and your agent can transfer tokens, do swaps, and interact with smart contracts within the boundaries you define.

**The agent never sees the private key.** All transactions are executed server-side through a ZeroDev smart account. The agent receives a scoped API key that can only perform actions permitted by the wallet owner's policies. The private key never leaves the Vincent server.

All commands use the `@vincentai/cli` package. API keys are stored and resolved automatically — you never handle raw keys or file paths.

## Security Model

This skill is designed for **autonomous agent operation with human oversight via server-side controls**. Understanding this model is important:

**No environment variables are required** because this skill uses agent-first onboarding: the agent creates its own wallet at runtime by calling the Vincent API, which returns a scoped API key. There is no pre-existing credential to configure. The CLI stores the returned API key automatically during wallet creation. The config paths where the key is persisted (`${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/agentwallet/` or `./agentwallet/`) are declared in this skill's metadata.

**The agent's API key is not a private key.** It is a scoped Bearer token that can only execute transactions within the policies set by the wallet owner. The Vincent server enforces all policies server-side — the agent cannot bypass them regardless of what it sends. If a transaction violates a policy, the server rejects it. If a transaction requires approval, the server holds it and notifies the wallet owner via Telegram for out-of-band human approval.

**Model invocation is intentionally enabled.** The purpose of this skill is to give AI agents autonomous wallet capabilities. The agent is expected to invoke wallet actions (transfers, swaps, contract calls) on its own, within the boundaries the human operator defines. The human controls what the agent can do through policies (spending limits, address allowlists, token allowlists, function allowlists, approval thresholds) — not by gating individual invocations. The stored key is scoped and policy-constrained — even if another process reads it, it can only perform actions the wallet owner's policies allow, and the owner can revoke it instantly.

**All API calls go exclusively to `heyvincent.ai`** over HTTPS/TLS. No other endpoints, services, or external hosts are contacted. The agent does not read, collect, or transmit any data beyond what is needed for wallet operations.

**Vincent is open source and audited.** The server-side code that enforces policies, manages private keys, and executes transactions is publicly auditable at [github.com/HeyVincent-ai/Vincent](https://github.com/HeyVincent-ai/Vincent). The Vincent backend undergoes continuous security audits covering key management, policy enforcement, transaction signing, and API authentication. You can verify how policy enforcement works, how private keys are stored, how the scoped API key is validated, and how revocation is handled — nothing is opaque. If you want to self-host Vincent rather than trust the hosted service, the repository includes deployment instructions.

**Key lifecycle:**

- **Creation**: The agent runs `secret create` — the CLI stores the API key automatically and returns a `keyId` and `claimUrl`.
- **Claim**: The human operator uses the claim URL to take ownership and configure policies.
- **Revocation**: The wallet owner can revoke the agent's API key at any time from `https://heyvincent.ai`. Revoked keys are rejected immediately by the server.
- **Re-linking**: If the agent loses its API key, the wallet owner generates a one-time re-link token and the agent exchanges it for a new key via `secret relink`.
- **Rotation**: The wallet owner can revoke the current key and issue a re-link token to rotate credentials at any time.

## Which Secret Type to Use

| Type         | Use Case                                  | Network                 | Gas              |
| ------------ | ----------------------------------------- | ----------------------- | ---------------- |
| `EVM_WALLET` | Transfers, swaps, DeFi, contract calls    | Any EVM chain           | Sponsored (free) |
| `RAW_SIGNER` | Raw message signing for special protocols | Any (Ethereum + Solana) | You pay          |

**Choose `EVM_WALLET`** (default) for:

- Sending ETH or tokens
- Swapping tokens on DEXs
- Interacting with smart contracts
- Any standard EVM transaction

**Choose `RAW_SIGNER`** only when you need:

- Raw ECDSA/Ed25519 signatures for protocols that don't work with smart accounts
- To sign transaction hashes you'll broadcast yourself
- Solana signatures

## Quick Start

### 1. Check for Existing Keys

Before creating a new wallet, check if one already exists:

```bash
npx @vincentai/cli@latest secret list --type EVM_WALLET
```

If a key is returned, use its `id` as the `--key-id` for all subsequent commands. If no keys exist, create a new wallet.

### 2. Create a Wallet

```bash
npx @vincentai/cli@latest secret create --type EVM_WALLET --memo "My agent wallet" --chain-id 84532
```

Returns `keyId` (use for all future commands), `claimUrl` (share with the user), and `address`.

After creating, tell the user:

> "Here is your wallet claim URL: `<claimUrl>`. Use this to claim ownership, set spending policies, and monitor your agent's wallet activity at https://heyvincent.ai."

### 3. Get Wallet Address

```bash
npx @vincentai/cli@latest wallet address --key-id <KEY_ID>
```

### 4. Check Balances

```bash
# All balances across all supported chains
npx @vincentai/cli@latest wallet balances --key-id <KEY_ID>

# Filter to specific chains
npx @vincentai/cli@latest wallet balances --key-id <KEY_ID> --chain-ids 1,137,42161
```

Returns all ERC-20 tokens and native balances with symbols, decimals, logos, and USD values.

### 5. Transfer ETH or Tokens

```bash
# Transfer native ETH
npx @vincentai/cli@latest wallet transfer --key-id <KEY_ID> --to 0xRecipient --amount 0.01

# Transfer ERC-20 token
npx @vincentai/cli@latest wallet transfer --key-id <KEY_ID> --to 0xRecipient --amount 100 --token 0xTokenAddress
```

If the transaction violates a policy, the server returns an error explaining which policy was triggered. If the transaction requires human approval (based on the approval threshold policy), the server returns `status: "pending_approval"` and the wallet owner receives a Telegram notification to approve or deny.

### 6. Swap Tokens

Swap one token for another using DEX liquidity (powered by 0x).

```bash
# Preview a swap (no execution, just pricing)
npx @vincentai/cli@latest wallet swap preview --key-id <KEY_ID> \
  --sell-token 0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE \
  --buy-token 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 \
  --sell-amount 0.1 --chain-id 1

# Execute a swap
npx @vincentai/cli@latest wallet swap execute --key-id <KEY_ID> \
  --sell-token 0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE \
  --buy-token 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 \
  --sell-amount 0.1 --chain-id 1 --slippage 100
```

- Use `0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE` for native ETH.
- `--sell-amount`: Human-readable amount (e.g. `0.1` for 0.1 ETH).
- `--chain-id`: 1 = Ethereum, 137 = Polygon, 42161 = Arbitrum, 10 = Optimism, 8453 = Base, etc.
- `--slippage`: Slippage tolerance in basis points (100 = 1%). Defaults to 100. Execute only.

The preview returns expected buy amount, route info, and fees without executing. Execute performs the actual swap, handling ERC20 approvals automatically.

### 7. Send Arbitrary Transaction

Interact with any smart contract by sending custom calldata.

```bash
npx @vincentai/cli@latest wallet send-tx --key-id <KEY_ID> --to 0xContract --data 0xCalldata --value 0
```

### 8. Transfer Between Your Secrets

Transfer funds between Vincent secrets you own (e.g., from one EVM wallet to another, or to a Polymarket wallet). Vincent verifies you own both secrets and handles any token conversion or cross-chain bridging automatically.

```bash
# Preview (get quote without executing)
npx @vincentai/cli@latest wallet transfer-between preview --key-id <KEY_ID> \
  --to-secret-id <DEST_SECRET_ID> --from-chain 8453 --to-chain 8453 \
  --token-in ETH --amount 0.1 --token-out ETH

# Execute
npx @vincentai/cli@latest wallet transfer-between execute --key-id <KEY_ID> \
  --to-secret-id <DEST_SECRET_ID> --from-chain 8453 --to-chain 8453 \
  --token-in ETH --amount 0.1 --token-out ETH --slippage 100

# Check cross-chain transfer status
npx @vincentai/cli@latest wallet transfer-between status --key-id <KEY_ID> --relay-id <RELAY_REQUEST_ID>
```

**Behavior:**

- **Same token + same chain**: Executes as a direct transfer (gas sponsored).
- **Different token or chain**: Uses a relay service for atomic swap + bridge.
- The destination secret can be an `EVM_WALLET` or `POLYMARKET_WALLET`.
- The server verifies you own both the source and destination secrets — transfers to secrets you don't own are rejected.
- Transfers are subject to the same server-side policies as regular transfers (spending limits, approval thresholds, etc.).

## Output Format

CLI commands return JSON to stdout. Successful responses include the relevant data:

```json
{
  "address": "0x...",
  "balances": [
    {
      "token": "ETH",
      "balance": "0.5",
      "usdValue": "1250.00"
    }
  ]
}
```

Transaction commands return:

```json
{
  "transactionHash": "0x...",
  "status": "confirmed"
}
```

For transactions requiring human approval:

```json
{
  "status": "pending_approval",
  "message": "Transaction requires owner approval via Telegram"
}
```

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `401 Unauthorized` | Invalid or missing API key | Check that the key-id is correct; re-link if needed |
| `403 Policy Violation` | Transaction blocked by server-side policy | User must adjust policies at heyvincent.ai |
| `400 Insufficient Balance` | Not enough tokens for the transfer | Check balances before transferring |
| `429 Rate Limited` | Too many requests | Wait and retry with backoff |
| `pending_approval` | Transaction exceeds approval threshold | User will receive Telegram notification to approve/deny |
| `Key not found` | API key was revoked or never created | Re-link with a new token from the wallet owner |

If a transaction is rejected, inform the user to check their policy settings at `https://heyvincent.ai`.

## Policies (Server-Side Enforcement)

The wallet owner controls what the agent can do by setting policies via the claim URL at `https://heyvincent.ai`. All policies are enforced server-side by the Vincent API — the agent cannot bypass or modify them. If a transaction violates a policy, the API rejects it. If a transaction triggers an approval threshold, the API holds it and sends the wallet owner a Telegram notification for out-of-band human approval. The policy enforcement logic is open source and auditable at [github.com/HeyVincent-ai/Vincent](https://github.com/HeyVincent-ai/Vincent).

| Policy                      | What it does                                                        |
| --------------------------- | ------------------------------------------------------------------- |
| **Address allowlist**       | Only allow transfers/calls to specific addresses                    |
| **Token allowlist**         | Only allow transfers of specific ERC-20 tokens                      |
| **Function allowlist**      | Only allow calling specific contract functions (by 4-byte selector) |
| **Spending limit (per tx)** | Max USD value per transaction                                       |
| **Spending limit (daily)**  | Max USD value per rolling 24 hours                                  |
| **Spending limit (weekly)** | Max USD value per rolling 7 days                                    |
| **Require approval**        | Every transaction needs human approval via Telegram                 |
| **Approval threshold**      | Transactions above a USD amount need human approval via Telegram    |

Before the wallet is claimed, the agent can operate without policy restrictions. This is by design: agent-first onboarding allows the agent to begin accumulating and managing funds immediately. Once the human operator claims the wallet via the claim URL, they can add any combination of policies to constrain the agent's behavior. The wallet owner can also revoke the agent's API key entirely at any time.

## Re-linking (Recovering API Access)

If the agent loses its API key, the wallet owner can generate a **re-link token** from the frontend. The agent then exchanges this token for a new API key.

**How it works:**

1. The user generates a re-link token from the wallet detail page at `https://heyvincent.ai`
2. The user gives the token to the agent (e.g. by pasting it in chat)
3. The agent runs the relink command:

```bash
npx @vincentai/cli@latest secret relink --token <TOKEN_FROM_USER>
```

The CLI exchanges the token for a new API key, stores it automatically, and returns the new `keyId`. Use this `keyId` for all subsequent commands.

**Important:** Re-link tokens are one-time use and expire after 10 minutes.

## Important Notes

- **No gas needed.** A paymaster is fully set up — all transaction gas fees are sponsored automatically. The wallet does not need ETH for gas.
- **Never try to access raw secret values.** The private key stays server-side — that's the whole point.
- Always share the claim URL with the user after creating a wallet.
- If a transaction is rejected, it may be blocked by a server-side policy. Tell the user to check their policy settings at `https://heyvincent.ai`.
- If a transaction requires approval, it will return `status: "pending_approval"`. The wallet owner will receive a Telegram notification to approve or deny.

---

## Raw Signer (Advanced)

For raw ECDSA/Ed25519 signing when smart accounts won't work.

### Create a Raw Signer

```bash
npx @vincentai/cli@latest secret create --type RAW_SIGNER --memo "My raw signer"
```

Response includes both Ethereum (secp256k1) and Solana (ed25519) addresses derived from the same seed.

### Get Addresses

```bash
npx @vincentai/cli@latest raw-signer addresses --key-id <KEY_ID>
```

Returns `ethAddress` and `solanaAddress`.

### Sign a Message

```bash
npx @vincentai/cli@latest raw-signer sign --key-id <KEY_ID> --message 0x<hex-encoded-bytes> --curve ethereum
```

- `--message`: Hex-encoded bytes to sign (must start with `0x`)
- `--curve`: `ethereum` for secp256k1 ECDSA, `solana` for ed25519

Returns a hex-encoded signature. For Ethereum, this is `r || s || v` (65 bytes). For Solana, it's a 64-byte ed25519 signature.
```

