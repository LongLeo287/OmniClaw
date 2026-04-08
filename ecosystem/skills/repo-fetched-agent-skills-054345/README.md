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
