---
id: stripe-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:18.808521
---

# KNOWLEDGE EXTRACT: stripe
> **Extracted on:** 2026-03-30 17:54:06
> **Source:** stripe

---

## File: `ai.md`
```markdown
# 📦 stripe/ai [🔖 PENDING/APPROVE]
🔗 https://github.com/stripe/ai
🌐 https://docs.stripe.com/agents

## Meta
- **Stars:** ⭐ 1408 | **Forks:** 🍴 238
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
One-stop shop for building AI-powered products and businesses with Stripe.

## README (trích đầu)
```
![Hero GIF](https://stripe.dev/images/badges/ai-banner.gif)

# Stripe AI

This repo is the one-stop shop for building AI-powered products and businesses on top of Stripe. 

It contains a collection of SDKs to help you integrate Stripe with LLMs and agent frameworks, including: 

* [`@stripe/agent-toolkit`](/tools/typescript) - for integrating Stripe APIs with popular agent frameworks through function calling—available in [Python](/tools/python) and [TypeScript](/tools/typescript).
* [`@stripe/ai-sdk`](/llm/ai-sdk) - for integrating Stripe's billing infrastructure with Vercel's [`ai`](https://npm.im/ai) and [`@ai-sdk`](https://ai-sdk.dev/) libraries.
* [`@stripe/token-meter`](/llm/token-meter) - for integrating Stripe's billing infrastructure with native SDKs from OpenAI, Anthropic, and Google Gemini, without any framework dependencies.

## Model Context Protocol (MCP)

Stripe hosts a remote MCP server at `https://mcp.stripe.com`. This allows secure MCP client access via OAuth. View the docs [here](https://docs.stripe.com/mcp#remote).

The Stripe Agent Toolkit also exposes tools in the [Model Context Protocol (MCP)](https://modelcontextprotocol.com/) format. Or, to run a local Stripe MCP server using npx, use the following command:

```sh
npx -y @stripe/mcp --api-key=YOUR_STRIPE_SECRET_KEY
```

Tool permissions are controlled by your Restricted API Key (RAK). Create a RAK with the desired permissions at https://dashboard.stripe.com/apikeys

See [MCP](/tools/modelcontextprotocol) for more details.

## Agent toolkit

Stripe's Agent Toolkit enables popular agent frameworks including OpenAI's Agent SDK, LangChain, CrewAI, and Vercel's AI SDK to integrate with Stripe APIs through function calling. The library is not exhaustive of the entire Stripe API. It includes support for Python and TypeScript, and is built directly on top of the Stripe [Python][python-sdk] and [Node][node-sdk] SDKs.

Included below are basic instructions, but refer to [Python](/tools/python) and [TypeScript](/tools/typescript) packages for more information.

### Python

#### Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package run:

```sh
pip install stripe-agent-toolkit
```

##### Requirements

- Python 3.11+

#### Usage

The library needs to be configured with your account's secret key which is
available in your [Stripe Dashboard][api-keys]. We strongly recommend using a [Restricted API Key][restricted-keys] (`rk_*`) for better security and granular permissions. Tool availability is determined by the permissions you configure on the restricted key.

```python
from stripe_agent_toolkit.openai.toolkit import create_stripe_agent_toolkit

async def main():
    toolkit = await create_stripe_agent_toolkit(SECRET_KEY='[REDACTED_SECRET]')
    tools = toolkit.get_tools()
    # ... use tools ...
    await toolkit.close()  # Clean up when done
```

The toolkit works with OpenAI's Agent SDK, LangChain, and CrewAI and can be passe
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

