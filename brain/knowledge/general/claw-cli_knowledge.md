# Knowledge Dump for claw-cli

## File: clawcloud.md
```
# ClawCloud Private Fork Instructions

This document provides instructions for setting up a private fork of Claw-CLI for ClawCloud development and deployment.

## 1. Create a Private Repository

Start by creating a private GitHub repository (or equivalent) from this open-source `claw-cli` project.

## 2. Configure Environment Variables

Create a `.env` file in your project root, adapting from `.env.example`. Ensure you set `CLAW_CLOUD_ENABLED=true` and provide secure values for:

*   `JWT_SECRET` (Use a strong, randomly generated key)
*   `STRIPE_SECRET_KEY`
*   `STRIPE_WEBHOOK_SECRET`
*   `DATABASE_URL` (For production, consider a managed database like PostgreSQL, not SQLite)
*   `ADMIN_API_KEY` (Strong, randomly generated key)
*   `GEMINI_API_KEY` (Or other LLM API keys)

## 3. Customize and Extend

*   **Integrate Agent Logic:** In `server/index.ts`, replace the simulated agent execution with actual calls to the `Agent` class, ensuring proper multi-tenancy and resource isolation.
*   **Database:** Migrate from `better-sqlite3` to a production-grade database (e.g., PostgreSQL, MongoDB) and update database schema and ORM accordingly.
*   **Advanced User Management:** Implement password hashing, session management, and potentially OAuth/SSO.
*   **Stripe Integration:** Fully implement Stripe webhook handlers for subscription lifecycle management.
*   **Deployment:** Adapt `Dockerfile`, `docker-compose.yml`, and `render.yaml` for your specific cloud provider and infrastructure.
*   **Monitoring & Logging:** Integrate with your preferred monitoring, alerting, and centralized logging solutions.

## 4. Continuous Integration/Continuous Deployment (CI/CD)

Set up a robust CI/CD pipeline for automated testing, building, and deployment of your ClawCloud instance.

## 5. Maintain Security

Regularly review and update dependencies. Conduct security audits and penetration testing. Stay informed about new threats and vulnerabilities.

```

## File: cli_agent_readme.md
```
# CLI Agent Architecture & Usage

This document provides a detailed explanation of the `claw-cli-agent` autonomous agent, including its architecture, security model, and usage instructions.

## Agent Loop

The agent's operation follows a strict, five-stage loop to ensure security and predictability:

1.  **Input:** The agent receives a high-level task from the user via the command-line interface.
2.  **Plan:** A Large Language Model (LLM) planner (e.g., Gemini CLI) receives the task and decomposes it into a structured series of discrete, low-level actions. This plan is returned as a JSON object adhering to the Intent Schema.
3.  **Policy:** The agent's security policy engine intercepts the plan. Each proposed action is rigorously validated against a set of allow-listed, predefined capabilities and the Intent Schema. If any action is not recognized or violates the policy, the entire plan is rejected before execution.
4.  **Execute:** If the plan is approved, the executor module runs each action one by one. **Execution is sandboxed, auditable, and requires explicit user confirmation for sensitive actions (e.g., sending messages).** The executor operates with minimal privileges and controls a browser session (Web Bridge).

    **Execution is sandboxed and read-only by design.**
5.  **Audit:** The outcome of the execution, along with the original task and plan, is logged to ensure traceability and transparency.

## Architecture Overview

*   **CLI Entrypoint (`agent-cli/src/index.ts`):** Parses user commands and initiates the agent loop.
*   **Planner (Gemini CLI):** External tool. Interprets user intent and generates structured JSON plans based on the Intent Schema.
*   **Agent (`agent-cli/src/agent.ts`):** Orchestrates the `input \u2192 plan \u2192 policy \u2192 execute \u2192 audit` flow.
*   **Intent Schema (`agent-cli/src/intent-schema.ts`):** Defines the strict data structure for actions to be executed by the agent.
*   **Policy (`agent-cli/src/policy.ts`):** The security core. Defines and enforces the set of permissible actions and validates against the Intent Schema.
*   **Web Executor (`agent-cli/src/web-executor.ts`):** Controls a browser (Playwright) to perform web automation tasks. This module is isolated and requires user approval for sensitive actions.

## Security Rationale

The agent is built with a security-first mindset. Its primary goal is to prevent the LLM from causing unintended side effects and to ensure user control over web automation.

*   The agent **NEVER** executes raw shell commands directly.
*   All actions are constrained by a rigid, auditable policy.
*   **Browser automation is strictly limited to authenticated web sessions.**
*   **Explicit user confirmation is MANDATORY** before any message sending or other sensitive web actions.
*   The agent cannot modify its own source code or security policies.
*   No bulk sending and no background execution without explicit policy overrides.

## CLI Usage Examples

**Prerequisites:** Node.js, npm, and Playwright installed. Gemini CLI set up for planning.

1.  **Install & Build:**
    ```bash
    # Navigate to the agent's directory
    cd agent-cli

    # Install dependencies (including playwright)
    npm install

    # Build the project
    npm run build
    ```

2.  **Web Login (one-time setup per platform):**
    ```bash
    # For WhatsApp Web
    node dist/index.js web login whatsapp_web

    # For Instagram Web
    node dist/index.js web login instagram_web
    ```
    This will launch a browser for you to manually log in. Session cookies will be stored.

3.  **Check Web Status:**
    ```bash
    node dist/index.js web status
    ```
    This will show if you are logged in to the web platforms.

4.  **Execute the Agent:**
    Run the CLI command with a natural language task. The Gemini CLI (planner) will interpret this and generate a plan.

    ```bash
    # Example: Send a message on WhatsApp Web
    node dist/index.js do \send a reply on WhatsApp Web to Alice saying Hello!\

    # Example: Draft a message on Instagram Web
    node dist/index.js do \draft a message on Instagram Web to Bob with content Great post!\
    ```
    The agent will pause and ask for confirmation before executing the final `send_message` action.


```

## File: docker-compose.yml
```
version: '3.8'

services:
  claw-cli:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      NODE_ENV: production
      # Add environment variables here that ClawCloud would use, e.g.:
      # CLAW_CLOUD_ENABLED: "true"
      # JWT_SECRET: "your_jwt_secret"
      # STRIPE_SECRET_KEY: "your_stripe_secret_key"
    ports:
      - "3000:3000" # Only needed if server mode is enabled and listening
    volumes:
      - ./data:/app/data # For SQLite DB, logs, session data etc.
    command: ["node", "dist/index.js", "--server"] # Example: Run in server mode
    restart: unless-stopped

```

## File: package-lock.json
```
{
  "name": "claw-cli",
  "version": "1.1.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "claw-cli",
      "version": "1.1.0",
      "hasInstallScript": true,
      "license": "MIT",
      "dependencies": {
        "@sinclair/typebox": "0.34.48",
        "better-sqlite3": "^11.1.2",
        "chalk": "^5.3.0",
        "commander": "^14.0.3",
        "dotenv": "^16.4.5",
        "express": "^4.19.2",
        "express-rate-limit": "^7.3.1",
        "helmet": "^7.1.0",
        "jsonwebtoken": "^9.0.2",
        "playwright": "^1.45.0",
        "zod": "^3.23.8"
      },
      "bin": {
        "claw": "dist/index.js",
        "claw-cli": "dist/index.js"
      },
      "devDependencies": {
        "@types/better-sqlite3": "^7.6.9",
        "@types/express": "^4.17.21",
        "@types/jsonwebtoken": "^9.0.6",
        "@types/node": "^20.14.9",
        "typescript": "^5.9.3"
      }
    },
    "node_modules/@sinclair/typebox": {
      "version": "0.34.48",
      "resolved": "https://registry.npmjs.org/@sinclair/typebox/-/typebox-0.34.48.tgz",
      "integrity": "sha512-kKJTNuK3AQOrgjjotVxMrCn1sUJwM76wMszfq1kdU4uYVJjvEWuFQ6HgvLt4Xz3fSmZlTOxJ/Ie13KnIcWQXFA==",
      "license": "MIT"
    },
    "node_modules/@types/better-sqlite3": {
      "version": "7.6.13",
      "resolved": "https://registry.npmjs.org/@types/better-sqlite3/-/better-sqlite3-7.6.13.tgz",
      "integrity": "sha512-NMv9ASNARoKksWtsq/SHakpYAYnhBrQgGD8zkLYk/jaK8jUGn08CfEdTRgYhMypUQAfzSP8W6gNLe0q19/t4VA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/node": "*"
      }
    },
    "node_modules/@types/body-parser": {
      "version": "1.19.6",
      "resolved": "https://registry.npmjs.org/@types/body-parser/-/body-parser-1.19.6.tgz",
      "integrity": "sha512-HLFeCYgz89uk22N5Qg3dvGvsv46B8GLvKKo1zKG4NybA8U2DiEO3w9lqGg29t/tfLRJpJ6iQxnVw4OnB7MoM9g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/connect": "*",
        "@types/node": "*"
      }
    },
    "node_modules/@types/connect": {
      "version": "3.4.38",
      "resolved": "https://registry.npmjs.org/@types/connect/-/connect-3.4.38.tgz",
      "integrity": "sha512-K6uROf1LD88uDQqJCktA4yzL1YYAK6NgfsI0v/mTgyPKWsX1CnJ0XPSDhViejru1GcRkLWb8RlzFYJRqGUbaug==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/node": "*"
      }
    },
    "node_modules/@types/express": {
      "version": "4.17.25",
      "resolved": "https://registry.npmjs.org/@types/express/-/express-4.17.25.tgz",
      "integrity": "sha512-dVd04UKsfpINUnK0yBoYHDF3xu7xVH4BuDotC/xGuycx4CgbP48X/KF/586bcObxT0HENHXEU8Nqtu6NR+eKhw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/body-parser": "*",
        "@types/express-serve-static-core": "^4.17.33",
        "@types/qs": "*",
        "@types/serve-static": "^1"
      }
    },
    "node_modules/@types/express-serve-static-core": {
      "version": "4.19.8",
      "resolved": "https://registry.npmjs.org/@types/express-serve-static-core/-/express-serve-static-core-4.19.8.tgz",
      "integrity": "sha512-02S5fmqeoKzVZCHPZid4b8JH2eM5HzQLZWN2FohQEy/0eXTq8VXZfSN6Pcr3F6N9R/vNrj7cpgbhjie6m/1tCA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/node": "*",
        "@types/qs": "*",
        "@types/range-parser": "*",
        "@types/send": "*"
      }
    },
    "node_modules/@types/http-errors": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@types/http-errors/-/http-errors-2.0.5.tgz",
      "integrity": "sha512-r8Tayk8HJnX0FztbZN7oVqGccWgw98T/0neJphO91KkmOzug1KkofZURD4UaD5uH8AqcFLfdPErnBod0u71/qg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/jsonwebtoken": {
      "version": "9.0.10",
      "resolved": "https://registry.npmjs.org/@types/jsonwebtoken/-/jsonwebtoken-9.0.10.tgz",
      "integrity": "sha512-asx5hIG9Qmf/1oStypjanR7iKTv0gXQ1Ov/jfrX6kS/EO0OFni8orbmGCn0672NHR3kXHwpAwR+B368ZGN/2rA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/ms": "*",
        "@types/node": "*"
      }
    },
    "node_modules/@types/mime": {
      "version": "1.3.5",
      "resolved": "https://registry.npmjs.org/@types/mime/-/mime-1.3.5.tgz",
      "integrity": "sha512-/pyBZWSLD2n0dcHE3hq8s8ZvcETHtEuF+3E7XVt0Ig2nvsVQXdghHVcEkIWjy9A0wKfTn97a/PSDYohKIlnP/w==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/ms": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/@types/ms/-/ms-2.1.0.tgz",
      "integrity": "sha512-GsCCIZDE/p3i96vtEqx+7dBUGXrc7zeSK3wwPHIaRThS+9OhWIXRqzs4d6k1SVU8g91DrNRWxWUGhp5KXQb2VA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/node": {
      "version": "20.19.33",
      "resolved": "https://registry.npmjs.org/@types/node/-/node-20.19.33.tgz",
      "integrity": "sha512-Rs1bVAIdBs5gbTIKza/tgpMuG1k3U/UMJLWecIMxNdJFDMzcM5LOiLVRYh3PilWEYDIeUDv7bpiHPLPsbydGcw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "undici-types": "~6.21.0"
      }
    },
    "node_modules/@types/qs": {
      "version": "6.14.0",
      "resolved": "https://registry.npmjs.org/@types/qs/-/qs-6.14.0.tgz",
      "integrity": "sha512-eOunJqu0K1923aExK6y8p6fsihYEn/BYuQ4g0CxAAgFc4b/ZLN4CrsRZ55srTdqoiLzU2B2evC+apEIxprEzkQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/range-parser": {
      "version": "1.2.7",
      "resolved": "https://registry.npmjs.org/@types/range-parser/-/range-parser-1.2.7.tgz",
      "integrity": "sha512-hKormJbkJqzQGhziax5PItDUTMAM9uE2XXQmM37dyd4hVM+5aVl7oVxMVUiVQn2oCQFN/LKCZdvSM0pFRqbSmQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/send": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/@types/send/-/send-1.2.1.tgz",
      "integrity": "sha512-arsCikDvlU99zl1g69TcAB3mzZPpxgw0UQnaHeC1Nwb015xp8bknZv5rIfri9xTOcMuaVgvabfIRA7PSZVuZIQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/node": "*"
      }
    },
    "node_modules/@types/serve-static": {
      "version": "1.15.10",
      "resolved": "https://registry.npmjs.org/@types/serve-static/-/serve-static-1.15.10.tgz",
      "integrity": "sha512-tRs1dB+g8Itk72rlSI2ZrW6vZg0YrLI81iQSTkMmOqnqCaNr/8Ek4VwWcN5vZgCYWbg/JJSGBlUaYGAOP73qBw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/http-errors": "*",
        "@types/node": "*",
        "@types/send": "<1"
      }
    },
    "node_modules/@types/serve-static/node_modules/@types/send": {
      "version": "0.17.6",
      "resolved": "https://registry.npmjs.org/@types/send/-/send-0.17.6.tgz",
      "integrity": "sha512-Uqt8rPBE8SY0RK8JB1EzVOIZ32uqy8HwdxCnoCOsYrvnswqmFZ/k+9Ikidlk/ImhsdvBsloHbAlewb2IEBV/Og==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/mime": "^1",
        "@types/node": "*"
      }
    },
    "node_modules/accepts": {
      "version": "1.3.8",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-1.3.8.tgz",
      "integrity": "sha512-PYAthTa2m2VKxuvSD3DPC/Gy+U+sOA1LAuT8mkmRuvw+NACSaeXEQ+NHcVF7rONl6qcaxV3Uuemwawk+7+SJLw==",
      "license": "MIT",
      "dependencies": {
        "mime-types": "~2.1.34",
        "negotiator": "0.6.3"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/array-flatten": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/array-flatten/-/array-flatten-1.1.1.tgz",
      "integrity": "sha512-PCVAQswWemu6UdxsDFFX/+gVeYqKAod3D3UVm91jHwynguOwAvYPhx8nNlM++NqRcK6CxxpUafjmhIdKiHibqg==",
      "license": "MIT"
    },
    "node_modules/base64-js": {
      "version": "1.5.1",
      "resolved": "https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz",
      "integrity": "sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/better-sqlite3": {
      "version": "11.10.0",
      "resolved": "https://registry.npmjs.org/better-sqlite3/-/better-sqlite3-11.10.0.tgz",
      "integrity": "sha512-EwhOpyXiOEL/lKzHz9AW1msWFNzGc/z+LzeB3/jnFJpxu+th2yqvzsSWas1v9jgs9+xiXJcD5A8CJxAG2TaghQ==",
      "hasInstallScript": true,
      "license": "MIT",
      "dependencies": {
        "bindings": "^1.5.0",
        "prebuild-install": "^7.1.1"
      }
    },
    "node_modules/bindings": {
      "version": "1.5.0",
      "resolved": "https://registry.npmjs.org/bindings/-/bindings-1.5.0.tgz",
      "integrity": "sha512-p2q/t/mhvuOj/UeLlV6566GD/guowlr0hHxClI0W9m7MWYkL1F0hLo+0Aexs9HSPCtR1SXQ0TD3MMKrXZajbiQ==",
      "license": "MIT",
      "dependencies": {
        "file-uri-to-path": "1.0.0"
      }
    },
    "node_modules/bl": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/bl/-/bl-4.1.0.tgz",
      "integrity": "sha512-1W07cM9gS6DcLperZfFSj+bWLtaPGSOHWhPiGzXmvVJbRLdG82sH/Kn8EtW1VqWVA54AKf2h5k5BbnIbwF3h6w==",
      "license": "MIT",
      "dependencies": {
        "buffer": "^5.5.0",
        "inherits": "^2.0.4",
        "readable-stream": "^3.4.0"
      }
    },
    "node_modules/body-parser": {
      "version": "1.20.4",
      "resolved": "https://registry.npmjs.org/body-parser/-/body-parser-1.20.4.tgz",
      "integrity": "sha512-ZTgYYLMOXY9qKU/57FAo8F+HA2dGX7bqGc71txDRC1rS4frdFI5R7NhluHxH6M0YItAP0sHB4uqAOcYKxO6uGA==",
      "license": "MIT",
      "dependencies": {
        "bytes": "~3.1.2",
        "content-type": "~1.0.5",
        "debug": "2.6.9",
        "depd": "2.0.0",
        "destroy": "~1.2.0",
        "http-errors": "~2.0.1",
        "iconv-lite": "~0.4.24",
        "on-finished": "~2.4.1",
        "qs": "~6.14.0",
        "raw-body": "~2.5.3",
        "type-is": "~1.6.18",
        "unpipe": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8",
        "npm": "1.2.8000 || >= 1.4.16"
      }
    },
    "node_modules/buffer": {
      "version": "5.7.1",
      "resolved": "https://registry.npmjs.org/buffer/-/buffer-5.7.1.tgz",
      "integrity": "sha512-EHcyIPBQ4BSGlvjB16k5KgAJ27CIsHY/2JBmCRReo48y9rQ3MaUzWX3KVlBa4U7MyX02HdVj0K7C3WaB3ju7FQ==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "base64-js": "^1.3.1",
        "ieee754": "^1.1.13"
      }
    },
    "node_modules/buffer-equal-constant-time": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/buffer-equal-constant-time/-/buffer-equal-constant-time-1.0.1.tgz",
      "integrity": "sha512-zRpUiDwd/xk6ADqPMATG8vc9VPrkck7T07OIx0gnjmJAnHnTVXNQG3vfvWNuiZIkwu9KrKdA1iJKfsfTVxE6NA==",
      "license": "BSD-3-Clause"
    },
    "node_modules/bytes": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/bytes/-/bytes-3.1.2.tgz",
      "integrity": "sha512-/Nf7TyzTx6S3yRJObOAV7956r8cr2+Oj8AC5dt8wSP3BQAoeX58NoHyCU8P8zGkNXStjTSi6fzO6F0pBdcYbEg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/call-bind-apply-helpers": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz",
      "integrity": "sha512-Sp1ablJ0ivDkSzjcaJdxEunN5/XvksFJ2sMBFfq6x0ryhQV/2b/KwFe21cMpmHtPOSij8K99/wSfoEuTObmuMQ==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/call-bound": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz",
      "integrity": "sha512-+ys997U96po4Kx/ABpBCqhA9EuxJaQWDQg7295H4hBphv3IZg0boBKuwYpt4YXp6MZ5AmZQnU/tyMTlRpaSejg==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "get-intrinsic": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/chalk": {
      "version": "5.6.2",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-5.6.2.tgz",
      "integrity": "sha512-7NzBL0rN6fMUW+f7A6Io4h40qQlG+xGmtMxfbnH/K7TAtt8JQWVQK+6g0UXKMeVJoyV5EkkNsErQ8pVD3bLHbA==",
      "license": "MIT",
      "engines": {
        "node": "^12.17.0 || ^14.13 || >=16.0.0"
      },
      "funding": {
        "url": "https://github.com/chalk/chalk?sponsor=1"
      }
    },
    "node_modules/chownr": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/chownr/-/chownr-1.1.4.tgz",
      "integrity": "sha512-jJ0bqzaylmJtVnNgzTeSOs8DPavpbYgEr/b0YL8/2GO3xJEhInFmhKMUnEJQjZumK7KXGFhUy89PrsJWlakBVg==",
      "license": "ISC"
    },
    "node_modules/commander": {
      "version": "14.0.3",
      "resolved": "https://registry.npmjs.org/commander/-/commander-14.0.3.tgz",
      "integrity": "sha512-H+y0Jo/T1RZ9qPP4Eh1pkcQcLRglraJaSLoyOtHxu6AapkjWVCy2Sit1QQ4x3Dng8qDlSsZEet7g5Pq06MvTgw==",
      "license": "MIT",
      "engines": {
        "node": ">=20"
      }
    },
    "node_modules/content-disposition": {
      "version": "0.5.4",
      "resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-0.5.4.tgz",
      "integrity": "sha512-FveZTNuGw04cxlAiWbzi6zTAL/lhehaWbTtgluJh4/E95DqMwTmha3KZN1aAWA8cFIhHzMZUvLevkw5Rqk+tSQ==",
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "5.2.1"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/content-type": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.5.tgz",
      "integrity": "sha512-nTjqfcBFEipKdXCv4YDQWCfmcLZKm81ldF0pAopTvyrFGVbcR6P/VAAd5G7N+0tTr8QqiU0tFadD6FK4NtJwOA==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie": {
      "version": "0.7.2",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-0.7.2.tgz",
      "integrity": "sha512-yki5XnKuf750l50uGTllt6kKILY4nQ1eNIQatoXEByZ5dWgnKqbnqmTrBE5B4N7lrMJKQ2ytWMiTO2o0v6Ew/w==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie-signature": {
      "version": "1.0.7",
      "resolved": "https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.0.7.tgz",
      "integrity": "sha512-NXdYc3dLr47pBkpUCHtKSwIOQXLVn8dZEuywboCOJY/osA0wFSLlSawr3KN8qXJEyX66FcONTH8EIlVuK0yyFA==",
      "license": "MIT"
    },
    "node_modules/debug": {
      "version": "2.6.9",
      "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
      "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
      "license": "MIT",
      "dependencies": {
        "ms": "2.0.0"
      }
    },
    "node_modules/decompress-response": {
      "version": "6.0.0",
      "resolved": "https://registry.npmjs.org/decompress-response/-/decompress-response-6.0.0.tgz",
      "integrity": "sha512-aW35yZM6Bb/4oJlZncMH2LCoZtJXTRxES17vE3hoRiowU2kWHaJKFkSBDnDR+cm9J+9QhXmREyIfv0pji9ejCQ==",
      "license": "MIT",
      "dependencies": {
        "mimic-response": "^3.1.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/deep-extend": {
      "version": "0.6.0",
      "resolved": "https://registry.npmjs.org/deep-extend/-/deep-extend-0.6.0.tgz",
      "integrity": "sha512-LOHxIOaPYdHlJRtCQfDIVZtfw/ufM8+rVj649RIHzcm/vGwQRXFt6OPqIFWsm2XEMrNIEtWR64sY1LEKD2vAOA==",
      "license": "MIT",
      "engines": {
        "node": ">=4.0.0"
      }
    },
    "node_modules/depd": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/depd/-/depd-2.0.0.tgz",
      "integrity": "sha512-g7nH6P6dyDioJogAAGprGpCtVImJhpPk/roCzdb3fIh61/s/nPsfR6onyMwkCAR/OlC3yBC0lESvUoQEAssIrw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/destroy": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/destroy/-/destroy-1.2.0.tgz",
      "integrity": "sha512-2sJGJTaXIIaR1w4iJSNoN0hnMY7Gpc/n8D4qSCJw8QqFWXf7cuAgnEHxBpweaVcPevC2l3KpjYCx3NypQQgaJg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8",
        "npm": "1.2.8000 || >= 1.4.16"
      }
    },
    "node_modules/detect-libc": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/detect-libc/-/detect-libc-2.1.2.tgz",
      "integrity": "sha512-Btj2BOOO83o3WyH59e8MgXsxEQVcarkUOpEYrubB0urwnN10yQ364rsiByU11nZlqWYZm05i/of7io4mzihBtQ==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/dotenv": {
      "version": "16.6.1",
      "resolved": "https://registry.npmjs.org/dotenv/-/dotenv-16.6.1.tgz",
      "integrity": "sha512-uBq4egWHTcTt33a72vpSG0z3HnPuIl6NqYcTrKEg2azoEyl2hpW0zqlxysq2pK9HlDIHyHyakeYaYnSAwd8bow==",
      "license": "BSD-2-Clause",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://dotenvx.com"
      }
    },
    "node_modules/dunder-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz",
      "integrity": "sha512-KIN/nDJBQRcXw0MLVhZE9iQHmG68qAVIBg9CqmUYjmQIhgij9U5MFvrqkUL5FbtyyzZuOeOt0zdeRe4UY7ct+A==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.1",
        "es-errors": "^1.3.0",
        "gopd": "^1.2.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/ecdsa-sig-formatter": {
      "version": "1.0.11",
      "resolved": "https://registry.npmjs.org/ecdsa-sig-formatter/-/ecdsa-sig-formatter-1.0.11.tgz",
      "integrity": "sha512-nagl3RYrbNv6kQkeJIpt6NJZy8twLB/2vtz6yN9Z4vRKHN4/QZJIEbqohALSgwKdnksuY3k5Addp5lg8sVoVcQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/ee-first": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz",
      "integrity": "sha512-WMwm9LhRUo+WUaRN+vRuETqG89IgZphVSNkdFgeb6sS/E4OrDIN7t48CAewSHXc6C8lefD8KKfr5vY61brQlow==",
      "license": "MIT"
    },
    "node_modules/encodeurl": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-2.0.0.tgz",
      "integrity": "sha512-Q0n9HRi4m6JuGIV1eFlmvJB7ZEVxu93IrMyiMsGC0lrMJMWzRgx6WGquyfQgZVb31vhGgXnfmPNNXmxnOkRBrg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/end-of-stream": {
      "version": "1.4.5",
      "resolved": "https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.5.tgz",
      "integrity": "sha512-ooEGc6HP26xXq/N+GCGOT0JKCLDGrq2bQUZrQ7gyrJiZANJ/8YDTxTpQBXGMn+WbIQXNVpyWymm7KYVICQnyOg==",
      "license": "MIT",
      "dependencies": {
        "once": "^1.4.0"
      }
    },
    "node_modules/es-define-property": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz",
      "integrity": "sha512-e3nRfgfUZ4rNGL232gUgX06QNyyez04KdjFrF+LTRoOXmrOgFKDg4BCdsjW8EnT69eqdYGmRpJwiPVYNrCaW3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-errors": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
      "integrity": "sha512-Zf5H2Kxt2xjTvbJvP2ZWLEICxA6j+hAmMzIlypy4xcBg1vKVnx89Wy0GbS+kf5cwCVFFzdCFh2XSCFNULS6csw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-object-atoms": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.1.tgz",
      "integrity": "sha512-FGgH2h8zKNim9ljj7dankFPcICIK9Cp5bm+c2gQSYePhpaG5+esrLODihIorn+Pe6FGJzWhXQotPv73jTaldXA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/escape-html": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz",
      "integrity": "sha512-NiSupZ4OeuGwr68lGIeym/ksIZMJodUGOSCZ/FSnTxcrekbvqrgdUxlJOMpijaKZVjAJrWrGs/6Jy8OMuyj9ow==",
      "license": "MIT"
    },
    "node_modules/etag": {
      "version": "1.8.1",
      "resolved": "https://registry.npmjs.org/etag/-/etag-1.8.1.tgz",
      "integrity": "sha512-aIL5Fx7mawVa300al2BnEE4iNvo1qETxLrPI/o05L7z6go7fCw1J6EQmbK4FmJ2AS7kgVF/KEZWufBfdClMcPg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/expand-template": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/expand-template/-/expand-template-2.0.3.tgz",
      "integrity": "sha512-XYfuKMvj4O35f/pOXLObndIRvyQ+/+6AhODh+OKWj9S9498pHHn/IMszH+gt0fBCRWMNfk1ZSp5x3AifmnI2vg==",
      "license": "(MIT OR WTFPL)",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/express": {
      "version": "4.22.1",
      "resolved": "https://registry.npmjs.org/express/-/express-4.22.1.tgz",
      "integrity": "sha512-F2X8g9P1X7uCPZMA3MVf9wcTqlyNp7IhH5qPCI0izhaOIYXaW9L535tGA3qmjRzpH+bZczqq7hVKxTR4NWnu+g==",
      "license": "MIT",
      "dependencies": {
        "accepts": "~1.3.8",
        "array-flatten": "1.1.1",
        "body-parser": "~1.20.3",
        "content-disposition": "~0.5.4",
        "content-type": "~1.0.4",
        "cookie": "~0.7.1",
        "cookie-signature": "~1.0.6",
        "debug": "2.6.9",
        "depd": "2.0.0",
        "encodeurl": "~2.0.0",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "finalhandler": "~1.3.1",
        "fresh": "~0.5.2",
        "http-errors": "~2.0.0",
        "merge-descriptors": "1.0.3",
        "methods": "~1.1.2",
        "on-finished": "~2.4.1",
        "parseurl": "~1.3.3",
        "path-to-regexp": "~0.1.12",
        "proxy-addr": "~2.0.7",
        "qs": "~6.14.0",
        "range-parser": "~1.2.1",
        "safe-buffer": "5.2.1",
        "send": "~0.19.0",
        "serve-static": "~1.16.2",
        "setprototypeof": "1.2.0",
        "statuses": "~2.0.1",
        "type-is": "~1.6.18",
        "utils-merge": "1.0.1",
        "vary": "~1.1.2"
      },
      "engines": {
        "node": ">= 0.10.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/express-rate-limit": {
      "version": "7.5.1",
      "resolved": "https://registry.npmjs.org/express-rate-limit/-/express-rate-limit-7.5.1.tgz",
      "integrity": "sha512-7iN8iPMDzOMHPUYllBEsQdWVB6fPDMPqwjBaFrgr4Jgr/+okjvzAy+UHlYYL/Vs0OsOrMkwS6PJDkFlJwoxUnw==",
      "license": "MIT",
      "engines": {
        "node": ">= 16"
      },
      "funding": {
        "url": "https://github.com/sponsors/express-rate-limit"
      },
      "peerDependencies": {
        "express": ">= 4.11"
      }
    },
    "node_modules/file-uri-to-path": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/file-uri-to-path/-/file-uri-to-path-1.0.0.tgz",
      "integrity": "sha512-0Zt+s3L7Vf1biwWZ29aARiVYLx7iMGnEUl9x33fbB/j3jR81u/O2LbqK+Bm1CDSNDKVtJ/YjwY7TUd5SkeLQLw==",
      "license": "MIT"
    },
    "node_modules/finalhandler": {
      "version": "1.3.2",
      "resolved": "https://registry.npmjs.org/finalhandler/-/finalhandler-1.3.2.tgz",
      "integrity": "sha512-aA4RyPcd3badbdABGDuTXCMTtOneUCAYH/gxoYRTZlIJdF0YPWuGqiAsIrhNnnqdXGswYk6dGujem4w80UJFhg==",
      "license": "MIT",
      "dependencies": {
        "debug": "2.6.9",
        "encodeurl": "~2.0.0",
        "escape-html": "~1.0.3",
        "on-finished": "~2.4.1",
        "parseurl": "~1.3.3",
        "statuses": "~2.0.2",
        "unpipe": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/forwarded": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/forwarded/-/forwarded-0.2.0.tgz",
      "integrity": "sha512-buRG0fpBtRHSTCOASe6hD258tEubFoRLb4ZNA6NxMVHNw2gOcwHo9wyablzMzOA5z9xA9L1KNjk/Nt6MT9aYow==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/fresh": {
      "version": "0.5.2",
      "resolved": "https://registry.npmjs.org/fresh/-/fresh-0.5.2.tgz",
      "integrity": "sha512-zJ2mQYM18rEFOudeV4GShTGIQ7RbzA7ozbU9I/XBpm7kqgMywgmylMwXHxZJmkVoYkna9d2pVXVXPdYTP9ej8Q==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/fs-constants": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/fs-constants/-/fs-constants-1.0.0.tgz",
      "integrity": "sha512-y6OAwoSIf7FyjMIv94u+b5rdheZEjzR63GTyZJm5qh4Bi+2YgwLCcI/fPFZkL5PSixOt6ZNKm+w+Hfp/Bciwow==",
      "license": "MIT"
    },
    "node_modules/fsevents": {
      "version": "2.3.2",
      "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.2.tgz",
      "integrity": "sha512-xiqMQR4xAeHTuB9uWm+fFRcIOgKBMiOBP+eXiyT7jsgVCq1bkVygt00oASowB7EdtpOHaaPgKt812P9ab+DDKA==",
      "hasInstallScript": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
      }
    },
    "node_modules/function-bind": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
      "integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/get-intrinsic": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz",
      "integrity": "sha512-9fSjSaos/fRIVIp+xSJlE6lfwhES7LNtKaCBIamHsjr2na1BiABJPo0mOjjz8GJDURarmCPGqaiVg5mfjb98CQ==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "es-define-property": "^1.0.1",
        "es-errors": "^1.3.0",
        "es-object-atoms": "^1.1.1",
        "function-bind": "^1.1.2",
        "get-proto": "^1.0.1",
        "gopd": "^1.2.0",
        "has-symbols": "^1.1.0",
        "hasown": "^2.0.2",
        "math-intrinsics": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/get-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz",
      "integrity": "sha512-sTSfBjoXBp89JvIKIefqw7U2CCebsc74kiY6awiGogKtoSGbgjYE/G/+l9sF3MWFPNc9IcoOC4ODfKHfxFmp0g==",
      "license": "MIT",
      "dependencies": {
        "dunder-proto": "^1.0.1",
        "es-object-atoms": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/github-from-package": {
      "version": "0.0.0",
      "resolved": "https://registry.npmjs.org/github-from-package/-/github-from-package-0.0.0.tgz",
      "integrity": "sha512-SyHy3T1v2NUXn29OsWdxmK6RwHD+vkj3v8en8AOBZ1wBQ/hCAQ5bAQTD02kW4W9tUp/3Qh6J8r9EvntiyCmOOw==",
      "license": "MIT"
    },
    "node_modules/gopd": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz",
      "integrity": "sha512-ZUKRh6/kUFoAiTAtTYPZJ3hw9wNxx+BIBOijnlG9PnrJsCcSjs1wyyD6vJpaYtgnzDrKYRSqf3OO6Rfa93xsRg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-symbols": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz",
      "integrity": "sha512-1cDNdwJ2Jaohmb3sg4OmKaMBwuC48sYni5HUw2DvsC8LjGTLK9h+eb1X6RyuOHe4hT0ULCW68iomhjUoKUqlPQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/hasown": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/hasown/-/hasown-2.0.2.tgz",
      "integrity": "sha512-0hJU9SCPvmMzIBdZFqNPXWa6dqh7WdH0cII9y+CyS8rG3nL48Bclra9HmKhVVUHyPWNH5Y7xDwAB7bfgSjkUMQ==",
      "license": "MIT",
      "dependencies": {
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/helmet": {
      "version": "7.2.0",
      "resolved": "https://registry.npmjs.org/helmet/-/helmet-7.2.0.tgz",
      "integrity": "sha512-ZRiwvN089JfMXokizgqEPXsl2Guk094yExfoDXR0cBYWxtBbaSww/w+vT4WEJsBW2iTUi1GgZ6swmoug3Oy4Xw==",
      "license": "MIT",
      "engines": {
        "node": ">=16.0.0"
      }
    },
    "node_modules/http-errors": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/http-errors/-/http-errors-2.0.1.tgz",
      "integrity": "sha512-4FbRdAX+bSdmo4AUFuS0WNiPz8NgFt+r8ThgNWmlrjQjt1Q7ZR9+zTlce2859x4KSXrwIsaeTqDoKQmtP8pLmQ==",
      "license": "MIT",
      "dependencies": {
        "depd": "~2.0.0",
        "inherits": "~2.0.4",
        "setprototypeof": "~1.2.0",
        "statuses": "~2.0.2",
        "toidentifier": "~1.0.1"
      },
      "engines": {
        "node": ">= 0.8"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/iconv-lite": {
      "version": "0.4.24",
      "resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz",
      "integrity": "sha512-v3MXnZAcvnywkTUEZomIActle7RXXeedOR31wwl7VlyoXO4Qi9arvSenNQWne1TcRwhCL1HwLI21bEqdpj8/rA==",
      "license": "MIT",
      "dependencies": {
        "safer-buffer": ">= 2.1.2 < 3"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/ieee754": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/ieee754/-/ieee754-1.2.1.tgz",
      "integrity": "sha512-dcyqhDvX1C46lXZcVqCpK+FtMRQVdIMN6/Df5js2zouUsqG7I6sFxitIC+7KYK29KdXOLHdu9zL4sFnoVQnqaA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "BSD-3-Clause"
    },
    "node_modules/inherits": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
      "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==",
      "license": "ISC"
    },
    "node_modules/ini": {
      "version": "1.3.8",
      "resolved": "https://registry.npmjs.org/ini/-/ini-1.3.8.tgz",
      "integrity": "sha512-JV/yugV2uzW5iMRSiZAyDtQd+nxtUnjeLt0acNdw98kKLrvuRVyB80tsREOE7yvGVgalhZ6RNXCmEHkUKBKxew==",
      "license": "ISC"
    },
    "node_modules/ipaddr.js": {
      "version": "1.9.1",
      "resolved": "https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.9.1.tgz",
      "integrity": "sha512-0KI/607xoxSToH7GjN1FfSbLoU0+btTicjsQSWQlh/hZykN8KpmMf7uYwPW3R+akZ6R/w18ZlXSHBYXiYUPO3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/jsonwebtoken": {
      "version": "9.0.3",
      "resolved": "https://registry.npmjs.org/jsonwebtoken/-/jsonwebtoken-9.0.3.tgz",
      "integrity": "sha512-MT/xP0CrubFRNLNKvxJ2BYfy53Zkm++5bX9dtuPbqAeQpTVe0MQTFhao8+Cp//EmJp244xt6Drw/GVEGCUj40g==",
      "license": "MIT",
      "dependencies": {
        "jws": "^4.0.1",
        "lodash.includes": "^4.3.0",
        "lodash.isboolean": "^3.0.3",
        "lodash.isinteger": "^4.0.4",
        "lodash.isnumber": "^3.0.3",
        "lodash.isplainobject": "^4.0.6",
        "lodash.isstring": "^4.0.1",
        "lodash.once": "^4.0.0",
        "ms": "^2.1.1",
        "semver": "^7.5.4"
      },
      "engines": {
        "node": ">=12",
        "npm": ">=6"
      }
    },
    "node_modules/jsonwebtoken/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/jwa": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/jwa/-/jwa-2.0.1.tgz",
      "integrity": "sha512-hRF04fqJIP8Abbkq5NKGN0Bbr3JxlQ+qhZufXVr0DvujKy93ZCbXZMHDL4EOtodSbCWxOqR8MS1tXA5hwqCXDg==",
      "license": "MIT",
      "dependencies": {
        "buffer-equal-constant-time": "^1.0.1",
        "ecdsa-sig-formatter": "1.0.11",
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/jws": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/jws/-/jws-4.0.1.tgz",
      "integrity": "sha512-EKI/M/yqPncGUUh44xz0PxSidXFr/+r0pA70+gIYhjv+et7yxM+s29Y+VGDkovRofQem0fs7Uvf4+YmAdyRduA==",
      "license": "MIT",
      "dependencies": {
        "jwa": "^2.0.1",
        "safe-buffer": "^5.0.1"
      }
    },
    "node_modules/lodash.includes": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/lodash.includes/-/lodash.includes-4.3.0.tgz",
      "integrity": "sha512-W3Bx6mdkRTGtlJISOvVD/lbqjTlPPUDTMnlXZFnVwi9NKJ6tiAk6LVdlhZMm17VZisqhKcgzpO5Wz91PCt5b0w==",
      "license": "MIT"
    },
    "node_modules/lodash.isboolean": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/lodash.isboolean/-/lodash.isboolean-3.0.3.tgz",
      "integrity": "sha512-Bz5mupy2SVbPHURB98VAcw+aHh4vRV5IPNhILUCsOzRmsTmSQ17jIuqopAentWoehktxGd9e/hbIXq980/1QJg==",
      "license": "MIT"
    },
    "node_modules/lodash.isinteger": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/lodash.isinteger/-/lodash.isinteger-4.0.4.tgz",
      "integrity": "sha512-DBwtEWN2caHQ9/imiNeEA5ys1JoRtRfY3d7V9wkqtbycnAmTvRRmbHKDV4a0EYc678/dia0jrte4tjYwVBaZUA==",
      "license": "MIT"
    },
    "node_modules/lodash.isnumber": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/lodash.isnumber/-/lodash.isnumber-3.0.3.tgz",
      "integrity": "sha512-QYqzpfwO3/CWf3XP+Z+tkQsfaLL/EnUlXWVkIk5FUPc4sBdTehEqZONuyRt2P67PXAk+NXmTBcc97zw9t1FQrw==",
      "license": "MIT"
    },
    "node_modules/lodash.isplainobject": {
      "version": "4.0.6",
      "resolved": "https://registry.npmjs.org/lodash.isplainobject/-/lodash.isplainobject-4.0.6.tgz",
      "integrity": "sha512-oSXzaWypCMHkPC3NvBEaPHf0KsA5mvPrOPgQWDsbg8n7orZ290M0BmC/jgRZ4vcJ6DTAhjrsSYgdsW/F+MFOBA==",
      "license": "MIT"
    },
    "node_modules/lodash.isstring": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/lodash.isstring/-/lodash.isstring-4.0.1.tgz",
      "integrity": "sha512-0wJxfxH1wgO3GrbuP+dTTk7op+6L41QCXbGINEmD+ny/G/eCqGzxyCsh7159S+mgDDcoarnBw6PC1PS5+wUGgw==",
      "license": "MIT"
    },
    "node_modules/lodash.once": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/lodash.once/-/lodash.once-4.1.1.tgz",
      "integrity": "sha512-Sb487aTOCr9drQVL8pIxOzVhafOjZN9UU54hiN8PU3uAiSV7lx1yYNpbNmex2PK6dSJoNTSJUUswT651yww3Mg==",
      "license": "MIT"
    },
    "node_modules/math-intrinsics": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz",
      "integrity": "sha512-/IXtbwEk5HTPyEwyKX6hGkYXxM9nbj64B+ilVJnC/R6B0pH5G4V3b0pVbL7DBj4tkhBAppbQUlf6F6Xl9LHu1g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/media-typer": {
      "version": "0.3.0",
      "resolved": "https://registry.npmjs.org/media-typer/-/media-typer-0.3.0.tgz",
      "integrity": "sha512-dq+qelQ9akHpcOl/gUVRTxVIOkAJ1wR3QAvb4RsVjS8oVoFjDGTc679wJYmUmknUF5HwMLOgb5O+a3KxfWapPQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/merge-descriptors": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/merge-descriptors/-/merge-descriptors-1.0.3.tgz",
      "integrity": "sha512-gaNvAS7TZ897/rVaZ0nMtAyxNyi/pdbjbAwUpFQpN70GqnVfOiXpeUUMKRBmzXaSQ8DdTX4/0ms62r2K+hE6mQ==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/methods": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/methods/-/methods-1.1.2.tgz",
      "integrity": "sha512-iclAHeNqNm68zFtnZ0e+1L2yUIdvzNoauKU4WBA3VvH/vPFieF7qfRlwUZU+DA9P9bPXIS90ulxoUoCH23sV2w==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/mime": {
      "version": "1.6.0",
      "resolved": "https://registry.npmjs.org/mime/-/mime-1.6.0.tgz",
      "integrity": "sha512-x0Vn8spI+wuJ1O6S7gnbaQg8Pxh4NNHb7KSINmEWKiPE4RKOplvijn+NkmYmmRgP68mc70j2EbeTFRsrswaQeg==",
      "license": "MIT",
      "bin": {
        "mime": "cli.js"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/mime-db": {
      "version": "1.52.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz",
      "integrity": "sha512-sPU4uV7dYlvtWJxwwxHD0PuihVNiE7TyAbQ5SWxDCB9mUYvOgroQOwYQQOKPJ8CIbE+1ETVlOoK1UC2nU3gYvg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/mime-types": {
      "version": "2.1.35",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz",
      "integrity": "sha512-ZDY+bPm5zTTF+YpCrAU9nK0UgICYPT0QtT1NZWFv4s++TNkcgVaT0g6+4R2uI4MjQjzysHB1zxuWL50hzaeXiw==",
      "license": "MIT",
      "dependencies": {
        "mime-db": "1.52.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/mimic-response": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/mimic-response/-/mimic-response-3.1.0.tgz",
      "integrity": "sha512-z0yWI+4FDrrweS8Zmt4Ej5HdJmky15+L2e6Wgn3+iK5fWzb6T3fhNFq2+MeTRb064c6Wr4N/wv0DzQTjNzHNGQ==",
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/minimist": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/minimist/-/minimist-1.2.8.tgz",
      "integrity": "sha512-2yyAR8qBkN3YuheJanUpWC5U3bb5osDywNB8RzDVlDwDHbocAJveqqj1u8+SVD7jkWT4yvsHCpWqqWqAxb0zCA==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/mkdirp-classic": {
      "version": "0.5.3",
      "resolved": "https://registry.npmjs.org/mkdirp-classic/-/mkdirp-classic-0.5.3.tgz",
      "integrity": "sha512-gKLcREMhtuZRwRAfqP3RFW+TK4JqApVBtOIftVgjuABpAtpxhPGaDcfvbhNvD0B8iD1oUr/txX35NjcaY6Ns/A==",
      "license": "MIT"
    },
    "node_modules/ms": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
      "integrity": "sha512-Tpp60P6IUJDTuOq/5Z8cdskzJujfwqfOTkrwIwj7IRISpnkJnT6SyJ4PCPnGMoFjC9ddhal5KVIYtAt97ix05A==",
      "license": "MIT"
    },
    "node_modules/napi-build-utils": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/napi-build-utils/-/napi-build-utils-2.0.0.tgz",
      "integrity": "sha512-GEbrYkbfF7MoNaoh2iGG84Mnf/WZfB0GdGEsM8wz7Expx/LlWf5U8t9nvJKXSp3qr5IsEbK04cBGhol/KwOsWA==",
      "license": "MIT"
    },
    "node_modules/negotiator": {
      "version": "0.6.3",
      "resolved": "https://registry.npmjs.org/negotiator/-/negotiator-0.6.3.tgz",
      "integrity": "sha512-+EUsqGPLsM+j/zdChZjsnX51g4XrHFOIXwfnCVPGlQk/k5giakcKsuxCObBRu6DSm9opw/O6slWbJdghQM4bBg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/node-abi": {
      "version": "3.87.0",
      "resolved": "https://registry.npmjs.org/node-abi/-/node-abi-3.87.0.tgz",
      "integrity": "sha512-+CGM1L1CgmtheLcBuleyYOn7NWPVu0s0EJH2C4puxgEZb9h8QpR9G2dBfZJOAUhi7VQxuBPMd0hiISWcTyiYyQ==",
      "license": "MIT",
      "dependencies": {
        "semver": "^7.3.5"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/object-inspect": {
      "version": "1.13.4",
      "resolved": "https://registry.npmjs.org/object-inspect/-/object-inspect-1.13.4.tgz",
      "integrity": "sha512-W67iLl4J2EXEGTbfeHCffrjDfitvLANg0UlX3wFUUSTx92KXRFegMHUVgSqE+wvhAbi4WqjGg9czysTV2Epbew==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/on-finished": {
      "version": "2.4.1",
      "resolved": "https://registry.npmjs.org/on-finished/-/on-finished-2.4.1.tgz",
      "integrity": "sha512-oVlzkg3ENAhCk2zdv7IJwd/QUD4z2RxRwpkcGY8psCVcCYZNq4wYnVWALHM+brtuJjePWiYF/ClmuDr8Ch5+kg==",
      "license": "MIT",
      "dependencies": {
        "ee-first": "1.1.1"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/once": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/once/-/once-1.4.0.tgz",
      "integrity": "sha512-lNaJgI+2Q5URQBkccEKHTQOPaXdUxnZZElQTZY0MFUAuaEqe1E+Nyvgdz/aIyNi6Z9MzO5dv1H8n58/GELp3+w==",
      "license": "ISC",
      "dependencies": {
        "wrappy": "1"
      }
    },
    "node_modules/parseurl": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/parseurl/-/parseurl-1.3.3.tgz",
      "integrity": "sha512-CiyeOxFT/JZyN5m0z9PfXw4SCBJ6Sygz1Dpl0wqjlhDEGGBP1GnsUVEL0p63hoG1fcj3fHynXi9NYO4nWOL+qQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/path-to-regexp": {
      "version": "0.1.12",
      "resolved": "https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-0.1.12.tgz",
      "integrity": "sha512-RA1GjUVMnvYFxuqovrEqZoxxW5NUZqbwKtYz/Tt7nXerk0LbLblQmrsgdeOxV5SFHf0UDggjS/bSeOZwt1pmEQ==",
      "license": "MIT"
    },
    "node_modules/playwright": {
      "version": "1.58.2",
      "resolved": "https://registry.npmjs.org/playwright/-/playwright-1.58.2.tgz",
      "integrity": "sha512-vA30H8Nvkq/cPBnNw4Q8TWz1EJyqgpuinBcHET0YVJVFldr8JDNiU9LaWAE1KqSkRYazuaBhTpB5ZzShOezQ6A==",
      "license": "Apache-2.0",
      "dependencies": {
        "playwright-core": "1.58.2"
      },
      "bin": {
        "playwright": "cli.js"
      },
      "engines": {
        "node": ">=18"
      },
      "optionalDependencies": {
        "fsevents": "2.3.2"
      }
    },
    "node_modules/playwright-core": {
      "version": "1.58.2",
      "resolved": "https://registry.npmjs.org/playwright-core/-/playwright-core-1.58.2.tgz",
      "integrity": "sha512-yZkEtftgwS8CsfYo7nm0KE8jsvm6i/PTgVtB8DL726wNf6H2IMsDuxCpJj59KDaxCtSnrWan2AeDqM7JBaultg==",
      "license": "Apache-2.0",
      "bin": {
        "playwright-core": "cli.js"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/prebuild-install": {
      "version": "7.1.3",
      "resolved": "https://registry.npmjs.org/prebuild-install/-/prebuild-install-7.1.3.tgz",
      "integrity": "sha512-8Mf2cbV7x1cXPUILADGI3wuhfqWvtiLA1iclTDbFRZkgRQS0NqsPZphna9V+HyTEadheuPmjaJMsbzKQFOzLug==",
      "deprecated": "No longer maintained. Please contact the author of the relevant native addon; alternatives are available.",
      "license": "MIT",
      "dependencies": {
        "detect-libc": "^2.0.0",
        "expand-template": "^2.0.3",
        "github-from-package": "0.0.0",
        "minimist": "^1.2.3",
        "mkdirp-classic": "^0.5.3",
        "napi-build-utils": "^2.0.0",
        "node-abi": "^3.3.0",
        "pump": "^3.0.0",
        "rc": "^1.2.7",
        "simple-get": "^4.0.0",
        "tar-fs": "^2.0.0",
        "tunnel-agent": "^0.6.0"
      },
      "bin": {
        "prebuild-install": "bin.js"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/proxy-addr": {
      "version": "2.0.7",
      "resolved": "https://registry.npmjs.org/proxy-addr/-/proxy-addr-2.0.7.tgz",
      "integrity": "sha512-llQsMLSUDUPT44jdrU/O37qlnifitDP+ZwrmmZcoSKyLKvtZxpyV0n2/bD/N4tBAAZ/gJEdZU7KMraoK1+XYAg==",
      "license": "MIT",
      "dependencies": {
        "forwarded": "0.2.0",
        "ipaddr.js": "1.9.1"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/pump": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/pump/-/pump-3.0.3.tgz",
      "integrity": "sha512-todwxLMY7/heScKmntwQG8CXVkWUOdYxIvY2s0VWAAMh/nd8SoYiRaKjlr7+iCs984f2P8zvrfWcDDYVb73NfA==",
      "license": "MIT",
      "dependencies": {
        "end-of-stream": "^1.1.0",
        "once": "^1.3.1"
      }
    },
    "node_modules/qs": {
      "version": "6.14.2",
      "resolved": "https://registry.npmjs.org/qs/-/qs-6.14.2.tgz",
      "integrity": "sha512-V/yCWTTF7VJ9hIh18Ugr2zhJMP01MY7c5kh4J870L7imm6/DIzBsNLTXzMwUA3yZ5b/KBqLx8Kp3uRvd7xSe3Q==",
      "license": "BSD-3-Clause",
      "dependencies": {
        "side-channel": "^1.1.0"
      },
      "engines": {
        "node": ">=0.6"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/range-parser": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/range-parser/-/range-parser-1.2.1.tgz",
      "integrity": "sha512-Hrgsx+orqoygnmhFbKaHE6c296J+HTAQXoxEF6gNupROmmGJRoyzfG3ccAveqCBrwr/2yxQ5BVd/GTl5agOwSg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/raw-body": {
      "version": "2.5.3",
      "resolved": "https://registry.npmjs.org/raw-body/-/raw-body-2.5.3.tgz",
      "integrity": "sha512-s4VSOf6yN0rvbRZGxs8Om5CWj6seneMwK3oDb4lWDH0UPhWcxwOWw5+qk24bxq87szX1ydrwylIOp2uG1ojUpA==",
      "license": "MIT",
      "dependencies": {
        "bytes": "~3.1.2",
        "http-errors": "~2.0.1",
        "iconv-lite": "~0.4.24",
        "unpipe": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/rc": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/rc/-/rc-1.2.8.tgz",
      "integrity": "sha512-y3bGgqKj3QBdxLbLkomlohkvsA8gdAiUQlSBJnBhfn+BPxg4bc62d8TcBW15wavDfgexCgccckhcZvywyQYPOw==",
      "license": "(BSD-2-Clause OR MIT OR Apache-2.0)",
      "dependencies": {
        "deep-extend": "^0.6.0",
        "ini": "~1.3.0",
        "minimist": "^1.2.0",
        "strip-json-comments": "~2.0.1"
      },
      "bin": {
        "rc": "cli.js"
      }
    },
    "node_modules/readable-stream": {
      "version": "3.6.2",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-3.6.2.tgz",
      "integrity": "sha512-9u/sniCrY3D5WdsERHzHE4G2YCXqoG5FTHUiCC4SIbr6XcLZBY05ya9EKjYek9O5xOAwjGq+1JdGBAS7Q9ScoA==",
      "license": "MIT",
      "dependencies": {
        "inherits": "^2.0.3",
        "string_decoder": "^1.1.1",
        "util-deprecate": "^1.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/safe-buffer": {
      "version": "5.2.1",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz",
      "integrity": "sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/safer-buffer": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz",
      "integrity": "sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg==",
      "license": "MIT"
    },
    "node_modules/semver": {
      "version": "7.7.4",
      "resolved": "https://registry.npmjs.org/semver/-/semver-7.7.4.tgz",
      "integrity": "sha512-vFKC2IEtQnVhpT78h1Yp8wzwrf8CM+MzKMHGJZfBtzhZNycRFnXsHk6E5TxIkkMsgNS7mdX3AGB7x2QM2di4lA==",
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/send": {
      "version": "0.19.2",
      "resolved": "https://registry.npmjs.org/send/-/send-0.19.2.tgz",
      "integrity": "sha512-VMbMxbDeehAxpOtWJXlcUS5E8iXh6QmN+BkRX1GARS3wRaXEEgzCcB10gTQazO42tpNIya8xIyNx8fll1OFPrg==",
      "license": "MIT",
      "dependencies": {
        "debug": "2.6.9",
        "depd": "2.0.0",
        "destroy": "1.2.0",
        "encodeurl": "~2.0.0",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "fresh": "~0.5.2",
        "http-errors": "~2.0.1",
        "mime": "1.6.0",
        "ms": "2.1.3",
        "on-finished": "~2.4.1",
        "range-parser": "~1.2.1",
        "statuses": "~2.0.2"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/send/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/serve-static": {
      "version": "1.16.3",
      "resolved": "https://registry.npmjs.org/serve-static/-/serve-static-1.16.3.tgz",
      "integrity": "sha512-x0RTqQel6g5SY7Lg6ZreMmsOzncHFU7nhnRWkKgWuMTu5NN0DR5oruckMqRvacAN9d5w6ARnRBXl9xhDCgfMeA==",
      "license": "MIT",
      "dependencies": {
        "encodeurl": "~2.0.0",
        "escape-html": "~1.0.3",
        "parseurl": "~1.3.3",
        "send": "~0.19.1"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/setprototypeof": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.2.0.tgz",
      "integrity": "sha512-E5LDX7Wrp85Kil5bhZv46j8jOeboKq5JMmYM3gVGdGH8xFpPWXUMsNrlODCrkoxMEeNi/XZIwuRvY4XNwYMJpw==",
      "license": "ISC"
    },
    "node_modules/side-channel": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/side-channel/-/side-channel-1.1.0.tgz",
      "integrity": "sha512-ZX99e6tRweoUXqR+VBrslhda51Nh5MTQwou5tnUDgbtyM0dBgmhEDtWGP/xbKn6hqfPRHujUNwz5fy/wbbhnpw==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "object-inspect": "^1.13.3",
        "side-channel-list": "^1.0.0",
        "side-channel-map": "^1.0.1",
        "side-channel-weakmap": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-list": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/side-channel-list/-/side-channel-list-1.0.0.tgz",
      "integrity": "sha512-FCLHtRD/gnpCiCHEiJLOwdmFP+wzCmDEkc9y7NsYxeF4u7Btsn1ZuwgwJGxImImHicJArLP4R0yX4c2KCrMrTA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "object-inspect": "^1.13.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-map": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/side-channel-map/-/side-channel-map-1.0.1.tgz",
      "integrity": "sha512-VCjCNfgMsby3tTdo02nbjtM/ewra6jPHmpThenkTYh8pG9ucZ/1P8So4u4FGBek/BjpOVsDCMoLA/iuBKIFXRA==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.5",
        "object-inspect": "^1.13.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/side-channel-weakmap": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/side-channel-weakmap/-/side-channel-weakmap-1.0.2.tgz",
      "integrity": "sha512-WPS/HvHQTYnHisLo9McqBHOJk2FkHO/tlpvldyrnem4aeQp4hai3gythswg6p01oSoTl58rcpiFAjF2br2Ak2A==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.5",
        "object-inspect": "^1.13.3",
        "side-channel-map": "^1.0.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/simple-concat": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/simple-concat/-/simple-concat-1.0.1.tgz",
      "integrity": "sha512-cSFtAPtRhljv69IK0hTVZQ+OfE9nePi/rtJmw5UjHeVyVroEqJXP1sFztKUy1qU+xvz3u/sfYJLa947b7nAN2Q==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/simple-get": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/simple-get/-/simple-get-4.0.1.tgz",
      "integrity": "sha512-brv7p5WgH0jmQJr1ZDDfKDOSeWWg+OVypG99A/5vYGPqJ6pxiaHLy8nxtFjBA7oMa01ebA9gfh1uMCFqOuXxvA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "decompress-response": "^6.0.0",
        "once": "^1.3.1",
        "simple-concat": "^1.0.0"
      }
    },
    "node_modules/statuses": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/statuses/-/statuses-2.0.2.tgz",
      "integrity": "sha512-DvEy55V3DB7uknRo+4iOGT5fP1slR8wQohVdknigZPMpMstaKJQWhwiYBACJE3Ul2pTnATihhBYnRhZQHGBiRw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/string_decoder": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.3.0.tgz",
      "integrity": "sha512-hkRX8U1WjJFd8LsDJ2yQ/wWWxaopEsABU1XfkM8A+j0+85JAGppt16cr1Whg6KIbb4okU6Mql6BOj+uup/wKeA==",
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "~5.2.0"
      }
    },
    "node_modules/strip-json-comments": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/strip-json-comments/-/strip-json-comments-2.0.1.tgz",
      "integrity": "sha512-4gB8na07fecVVkOI6Rs4e7T6NOTki5EmL7TUduTs6bu3EdnSycntVJ4re8kgZA+wx9IueI2Y11bfbgwtzuE0KQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/tar-fs": {
      "version": "2.1.4",
      "resolved": "https://registry.npmjs.org/tar-fs/-/tar-fs-2.1.4.tgz",
      "integrity": "sha512-mDAjwmZdh7LTT6pNleZ05Yt65HC3E+NiQzl672vQG38jIrehtJk/J3mNwIg+vShQPcLF/LV7CMnDW6vjj6sfYQ==",
      "license": "MIT",
      "dependencies": {
        "chownr": "^1.1.1",
        "mkdirp-classic": "^0.5.2",
        "pump": "^3.0.0",
        "tar-stream": "^2.1.4"
      }
    },
    "node_modules/tar-stream": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/tar-stream/-/tar-stream-2.2.0.tgz",
      "integrity": "sha512-ujeqbceABgwMZxEJnk2HDY2DlnUZ+9oEcb1KzTVfYHio0UE6dG71n60d8D2I4qNvleWrrXpmjpt7vZeF1LnMZQ==",
      "license": "MIT",
      "dependencies": {
        "bl": "^4.0.3",
        "end-of-stream": "^1.4.1",
        "fs-constants": "^1.0.0",
        "inherits": "^2.0.3",
        "readable-stream": "^3.1.1"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/toidentifier": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/toidentifier/-/toidentifier-1.0.1.tgz",
      "integrity": "sha512-o5sSPKEkg/DIQNmH43V0/uerLrpzVedkUh8tGNvaeXpfpuwjKenlSox/2O/BTlZUtEe+JG7s5YhEz608PlAHRA==",
      "license": "MIT",
      "engines": {
        "node": ">=0.6"
      }
    },
    "node_modules/tunnel-agent": {
      "version": "0.6.0",
      "resolved": "https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz",
      "integrity": "sha512-McnNiV1l8RYeY8tBgEpuodCC1mLUdbSN+CYBL7kJsJNInOP8UjDDEwdk6Mw60vdLLrr5NHKZhMAOSrR2NZuQ+w==",
      "license": "Apache-2.0",
      "dependencies": {
        "safe-buffer": "^5.0.1"
      },
      "engines": {
        "node": "*"
      }
    },
    "node_modules/type-is": {
      "version": "1.6.18",
      "resolved": "https://registry.npmjs.org/type-is/-/type-is-1.6.18.tgz",
      "integrity": "sha512-TkRKr9sUTxEH8MdfuCSP7VizJyzRNMjj2J2do2Jr3Kym598JVdEksuzPQCnlFPW4ky9Q+iA+ma9BGm06XQBy8g==",
      "license": "MIT",
      "dependencies": {
        "media-typer": "0.3.0",
        "mime-types": "~2.1.24"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/typescript": {
      "version": "5.9.3",
      "resolved": "https://registry.npmjs.org/typescript/-/typescript-5.9.3.tgz",
      "integrity": "sha512-jl1vZzPDinLr9eUt3J/t7V6FgNEw9QjvBPdysz9KfQDD41fQrC2Y4vKQdiaUpFT4bXlb1RHhLpp8wtm6M5TgSw==",
      "dev": true,
      "license": "Apache-2.0",
      "bin": {
        "tsc": "bin/tsc",
        "tsserver": "bin/tsserver"
      },
      "engines": {
        "node": ">=14.17"
      }
    },
    "node_modules/undici-types": {
      "version": "6.21.0",
      "resolved": "https://registry.npmjs.org/undici-types/-/undici-types-6.21.0.tgz",
      "integrity": "sha512-iwDZqg0QAGrg9Rav5H4n0M64c3mkR59cJ6wQp+7C4nI0gsmExaedaYLNO44eT4AtBBwjbTiGPMlt2Md0T9H9JQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/unpipe": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz",
      "integrity": "sha512-pjy2bYhSsufwWlKwPc+l3cN7+wuJlK6uz0YdJEOlQDbl6jo/YlPi4mb8agUkVC8BF7V8NuzeyPNqRksA3hztKQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/util-deprecate": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
      "integrity": "sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw==",
      "license": "MIT"
    },
    "node_modules/utils-merge": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/utils-merge/-/utils-merge-1.0.1.tgz",
      "integrity": "sha512-pMZTvIkT1d+TFGvDOqodOclx0QWkkgi6Tdoa8gC8ffGAAqz9pzPTZWAybbsHHoED/ztMtkv/VoYTYyShUn81hA==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4.0"
      }
    },
    "node_modules/vary": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/vary/-/vary-1.1.2.tgz",
      "integrity": "sha512-BNGbWLfd0eUPabhkXUVm0j8uuvREyTh5ovRa/dyow/BqAbZJyC+5fU+IzQOzmAKzYqYRAISoRhdQr3eIZ/PXqg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/wrappy": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
      "integrity": "sha512-l4Sp/DRseor9wL6EvV2+TuQn63dMkPjZ/sp9XkghTEbV9KlPS1xUsZ3u7/IQO4wxtcFB4bgpQPRcR3QCvezPcQ==",
      "license": "ISC"
    },
    "node_modules/zod": {
      "version": "3.25.76",
      "resolved": "https://registry.npmjs.org/zod/-/zod-3.25.76.tgz",
      "integrity": "sha512-gzUt/qt81nXsFGKIFcC3YnfEAx5NkunCfnDlvuBSSFS02bcXu4Lmea0AFIUwbLWxWPx3d9p8S5QoaujKcNQxcQ==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/colinhacks"
      }
    }
  }
}

```

## File: package.json
```
{
  "name": "claw-cli",
  "version": "1.1.0",
  "description": "A security-first AI agent for browser automation.",
  "main": "dist/index.js",
  "type": "module",
  "bin": {
    "claw": "dist/index.js",
    "claw-cli": "dist/index.js"
  },
  "scripts": {
    "build": "tsc",
    "postinstall": "playwright install --with-deps",
    "start:server": "node dist/server.js"
  },
  "keywords": [
    "ai-agent",
    "security",
    "browser-automation",
    "termux",
    "claw"
  ],
  "author": "psycho-prince",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/psycho-prince/claw-cli.git"
  },
  "dependencies": {
    "@sinclair/typebox": "0.34.48",
    "better-sqlite3": "^11.1.2",
    "commander": "^14.0.3",
    "dotenv": "^16.4.5",
    "express": "^4.19.2",
    "express-rate-limit": "^7.3.1",
    "helmet": "^7.1.0",
    "jsonwebtoken": "^9.0.2",
    "playwright": "^1.45.0",
    "zod": "^3.23.8",
    "chalk": "^5.3.0"
  },
  "devDependencies": {
    "@types/better-sqlite3": "^7.6.9",
    "@types/express": "^4.17.21",
    "@types/jsonwebtoken": "^9.0.6",
    "@types/node": "^20.14.9",
    "typescript": "^5.9.3"
  }
}

```

## File: README.md
```
# Claw-CLI: The Security-First Agent That Actually Protects You

OpenClaw got hacked? Meet Claw-CLI — the security-first agent that actually protects you.

## 🚀 Installation (v1.1.0)

### 1. Standard Install (macOS, Linux, Windows)

Install Node.js v18+ and then run:
```bash
npm install -g claw-cli
```
The `postinstall` script will automatically download the necessary Playwright browsers.

### 2. Android Termux Guide

Termux requires a few extra steps:
```bash
# 1. Install dependencies
pkg install nodejs-lts git

# 2. Install claw-cli globally
npm install -g claw-cli

# 3. Manually install Playwright browsers (postinstall might fail)
npx playwright install --with-deps
```

### 3. Quick Start

After installation, run the doctor to check your setup:
```bash
claw doctor
```

Initialize your config file:
```bash
claw init
```

See available commands:
```bash
claw --help
```

Start the server (for web UI or remote access):
```bash
claw --server
```

## ✨ Features

*   **Security-First Design:** Unlike other agents, Claw-CLI operates on a "fail-closed" principle. Every action is explicitly allow-listed and validated, ensuring the LLM *cannot* execute arbitrary or unsafe commands.
*   **Sandboxed Execution:** All web automation occurs within an isolated browser environment, preventing unintended system access.
*   **User Confirmation for Sensitive Actions:** Critical operations (e.g., sending messages) require explicit user approval. You're always in control.
*   **Auditable Logs:** Every agent action and decision is logged for transparency and security auditing.
*   **Local-First, Single-User:** Designed for your personal machine, offering robust security without the complexities of multi-user environments.

## ⚔️ Claw-CLI vs. OpenClaw: A Security Showdown (February 2026)

| Feature             | OpenClaw (CVE-2026-25253, RCE, Command Injection) | Claw-CLI (Security-First by Design)         |
| :------------------ | :------------------------------------------------ | :------------------------------------------ |
| **Security Model**  | Permissive, Prone to LLM "hallucinations"        | **Fail-Closed, Explicit Allow-List**          |
| **CVE-2026-25253**  | **Vulnerable (8.8 RCE!)**                         | **Immune by Design**                          |
| **Command Injection** | **Widespread Vulnerabilities**                    | **Impossible: No Raw Shell Access**           |
| **Infostealers**    | **Key/Config Exposure Risk**                      | **Sandboxed, Isolated Environment**           |
| **Malicious Skills** | 900+ known, execution often unrestricted         | **Policy-Engine Verified: Safe by Default**   |
| **Control**         | LLM often dictates actions                         | **User Always Confirms Sensitive Actions**    |
| **Deployment**      | Any environment, often insecurely                 | **Local & Secure; ClawCloud for Managed**     |
| **Trust Model**     | Trust in LLM + Skill Developers                    | **Trust in Code, Auditable Policies**         |

## 🖼️ Demo (Coming Soon!)

<!-- TODO: Insert a stunning demo GIF here showing the CLI in action,
    executing a complex web task securely and requiring user confirmation. -->

## 🔒 Security Model: How Claw-CLI Protects You

Claw-CLI operates on a rigorous `Input -> Plan -> Policy -> Execute -> Audit` loop:

1.  **Input:** Your natural language task.
2.  **Plan:** An advanced LLM (like Gemini) breaks down your task into discrete, structured actions (JSON).
3.  **Policy (THE CORE):** Our battle-hardened policy engine intercepts *every single action*. If an action isn't explicitly allowed and safe, the *entire plan is rejected*. **No exceptions.**
4.  **Execute:** Approved actions run in a tightly sandboxed, read-only browser environment. Sensitive actions require your explicit `[Y/n]` confirmation.
5.  **Audit:** Every step is logged, providing full transparency and traceability.

**Claw-CLI NEVER executes raw shell commands. All actions are strictly constrained.**

## ☁️ Local vs. ClawCloud (Managed SaaS)

Claw-CLI is designed to be fully open-source and free for local, single-user use on your machine. This gives you maximum control and privacy.

For teams and businesses requiring advanced features, scalability, and managed infrastructure, we're building **ClawCloud**.

*   **Claw-CLI (Open-Source):**
    *   Local execution, single-user.
    *   Full privacy, data stays on your machine.
    *   No monthly fees.
    *   Self-managed setup.

*   **ClawCloud (Managed SaaS):**
    *   **All Claw-CLI features, plus:**
    *   Secure, hosted multi-tenant environment.
    *   Scalable execution for high-volume tasks.
    *   Team collaboration & access controls.
    *   Advanced analytics & reporting.
    *   Dedicated support.
    *   Guaranteed uptime & SLA.
    *   _Coming Soon: Premium LLM integrations, enhanced security auditing._

## 💰 ClawCloud Pricing (Teaser)

Starting at **₹499/month** for individuals, up to **₹1999/month** for enterprise teams. Early bird access for waitlist sign-ups!

## 🗺️ Roadmap (v1.0.0 and beyond)

*   **v1.1.0 (Current Release):** npm-ready, `claw doctor` + `claw init`, Termux support.
*   **v1.0.0:** Production-ready, secure local CLI. Foundation for ClawCloud.
*   **v1.2.0:** Improved LLM integration patterns, custom policy definitions.
*   **v2.0.0:** First release of ClawCloud managed service with full feature parity + team features.

Join the waitlist here: Sign up for ClawCloud Beta
https://forms.gle/uKuj7huVmLDSYzvT8

```

## File: render.yaml
```
# This file is for Render.com deployment.
# It assumes a Dockerfile exists in the root of the repository.

services:
  - type: web
    name: claw-cli
    env: docker
    dockerfilePath: Dockerfile
    plan: starter # You can change this to 'standard' or 'pro' as needed
    ports:
      - 3000
    envVars:
      - key: NODE_ENV
        value: production
      # Example environment variables for ClawCloud deployment.
      # These would be set in Render's dashboard for security.
      # - key: CLAW_CLOUD_ENABLED
      #   value: "true"
      # - key: JWT_SECRET
      #   generateValue: true # Render can generate a secure secret
      # - key: STRIPE_SECRET_KEY
      #   sync: false # Do not sync with repo, set securely in Render
      # - key: DATABASE_URL
      #   value: "sqlite://./data/clawcloud.db" # Example for SQLite

```

## File: security.md
```
# Security Policy

This document outlines the security posture, threat model, and safe usage expectations for `claw-cli-agent`. This project prioritizes a "security-first" approach to autonomous agent execution.

## Threat Model

The primary threat this agent is designed to mitigate is unintended action execution resulting from a compromised or "hallucinating" Large Language Model (LLM).

*   **Adversary:** The LLM planner is treated as an untrusted source of commands. While a powerful tool, it can be manipulated via prompt injection or may generate unsafe instructions.
*   **Goal:** The agent's security goal is to prevent the LLM from executing arbitrary commands, reading sensitive data, or causing any unintended system modification.
*   **Attack Vectors:** The model assumes attack vectors originate from the LLM's output, such as a plan containing:
    *   Unauthorized shell commands (e.g., `rm -rf /`).
    *   Attempts to read sensitive files (e.g., `~/.ssh/id_rsa`).
    *   Unauthorized network connections to malicious endpoints.

## Philosophy: Fail-Closed and Policy-Driven

The cornerstone of this agent's security is its "fail-closed" philosophy.

*   **Explicit Allowance:** No action is ever implicitly trusted. Only capabilities that are explicitly defined in the `Policy` module are candidates for execution.
*   **Strict Validation:** Every proposed action and its arguments are rigorously validated against a predefined schema. Any deviation results in immediate rejection of the entire plan.
*   **Halt on Violation:** A single policy violation halts the agent's execution loop, preventing it from proceeding with a potentially unsafe plan.

This is **not a general-purpose shell agent**. It is a task-specific executor that operates under a highly restrictive and auditable security policy.

## Explicit Non-Goals

To maintain a clear security boundary, `claw-cli-agent` is **NOT** designed for:

*   **Arbitrary Shell Execution:** The agent is fundamentally incapable of executing raw shell commands.
*   **Self-Modification:** The agent cannot alter its own security policies or source code.

## Cloud Security Mitigations (for ClawCloud SaaS)

For the ClawCloud managed service, additional layers of security are implemented:

*   **Rate Limiting:** All API endpoints are protected by rate limiting to prevent abuse and denial-of-service attacks.
*   **Security Headers (Helmet):** Standard security headers are enforced to mitigate common web vulnerabilities like XSS, clickjacking, and others.
*   **Input Sanitization & Validation:** All user inputs to the ClawCloud API are rigorously sanitized and validated using strong schemas (`zod`).
*   **Authentication (JWT):** User access to protected endpoints is secured using JSON Web Tokens.
*   **Multi-Tenancy Isolation:** Agent execution for each user is designed to be isolated, preventing cross-tenant data access or interference. (Detailed implementation in `server/`).
*   **Data Encryption:** Sensitive data at rest (e.g., user database) and in transit (HTTPS) is encrypted.
*   **Auditable Logging:** Comprehensive logs are maintained for all server actions, agent executions, and security events.

## Safe Usage Assumptions

The security model of `claw-cli-agent` relies on the following assumptions:

*   **Trusted User (Local CLI):** The user operating the local CLI is trusted.
*   **Secure Host:** The machine running the agent is not already compromised.
*   **Policy Review:** The user is expected to understand the capabilities defined in the policy files. This is the definitive source of truth for what the agent can and cannot do.
*   **ClawCloud Users:** ClawCloud users are authenticated and operate within their defined quotas and access policies.

If you discover a security vulnerability, please report it responsibly by opening a security advisory on the GitHub repository.


```

## File: tsconfig.json
```
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "node",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,
    "declarationMap": true
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules", "dist"]
}

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_claw-cli_203740



================================================
FILE: CLAWCLOUD.md
================================================
# ClawCloud Private Fork Instructions

This document provides instructions for setting up a private fork of Claw-CLI for ClawCloud development and deployment.

## 1. Create a Private Repository

Start by creating a private GitHub repository (or equivalent) from this open-source `claw-cli` project.

## 2. Configure Environment Variables

Create a `.env` file in your project root, adapting from `.env.example`. Ensure you set `CLAW_CLOUD_ENABLED=true` and provide secure values for:

*   `JWT_SECRET` (Use a strong, randomly generated key)
*   `STRIPE_SECRET_KEY`
*   `STRIPE_WEBHOOK_SECRET`
*   `DATABASE_URL` (For production, consider a managed database like PostgreSQL, not SQLite)
*   `ADMIN_API_KEY` (Strong, randomly generated key)
*   `GEMINI_API_KEY` (Or other LLM API keys)

## 3. Customize and Extend

*   **Integrate Agent Logic:** In `server/index.ts`, replace the simulated agent execution with actual calls to the `Agent` class, ensuring proper multi-tenancy and resource isolation.
*   **Database:** Migrate from `better-sqlite3` to a production-grade database (e.g., PostgreSQL, MongoDB) and update database schema and ORM accordingly.
*   **Advanced User Management:** Implement password hashing, session management, and potentially OAuth/SSO.
*   **Stripe Integration:** Fully implement Stripe webhook handlers for subscription lifecycle management.
*   **Deployment:** Adapt `Dockerfile`, `docker-compose.yml`, and `render.yaml` for your specific cloud provider and infrastructure.
*   **Monitoring & Logging:** Integrate with your preferred monitoring, alerting, and centralized logging solutions.

## 4. Continuous Integration/Continuous Deployment (CI/CD)

Set up a robust CI/CD pipeline for automated testing, building, and deployment of your ClawCloud instance.

## 5. Maintain Security

Regularly review and update dependencies. Conduct security audits and penetration testing. Stay informed about new threats and vulnerabilities.


================================================
FILE: CLI_AGENT_README.md
================================================
# CLI Agent Architecture & Usage

This document provides a detailed explanation of the `claw-cli-agent` autonomous agent, including its architecture, security model, and usage instructions.

## Agent Loop

The agent's operation follows a strict, five-stage loop to ensure security and predictability:

1.  **Input:** The agent receives a high-level task from the user via the command-line interface.
2.  **Plan:** A Large Language Model (LLM) planner (e.g., Gemini CLI) receives the task and decomposes it into a structured series of discrete, low-level actions. This plan is returned as a JSON object adhering to the Intent Schema.
3.  **Policy:** The agent's security policy engine intercepts the plan. Each proposed action is rigorously validated against a set of allow-listed, predefined capabilities and the Intent Schema. If any action is not recognized or violates the policy, the entire plan is rejected before execution.
4.  **Execute:** If the plan is approved, the executor module runs each action one by one. **Execution is sandboxed, auditable, and requires explicit user confirmation for sensitive actions (e.g., sending messages).** The executor operates with minimal privileges and controls a browser session (Web Bridge).

    **Execution is sandboxed and read-only by design.**
5.  **Audit:** The outcome of the execution, along with the original task and plan, is logged to ensure traceability and transparency.

## Architecture Overview

*   **CLI Entrypoint (`agent-cli/src/index.ts`):** Parses user commands and initiates the agent loop.
*   **Planner (Gemini CLI):** External tool. Interprets user intent and generates structured JSON plans based on the Intent Schema.
*   **Agent (`agent-cli/src/agent.ts`):** Orchestrates the `input \u2192 plan \u2192 policy \u2192 execute \u2192 audit` flow.
*   **Intent Schema (`agent-cli/src/intent-schema.ts`):** Defines the strict data structure for actions to be executed by the agent.
*   **Policy (`agent-cli/src/policy.ts`):** The security core. Defines and enforces the set of permissible actions and validates against the Intent Schema.
*   **Web Executor (`agent-cli/src/web-executor.ts`):** Controls a browser (Playwright) to perform web automation tasks. This module is isolated and requires user approval for sensitive actions.

## Security Rationale

The agent is built with a security-first mindset. Its primary goal is to prevent the LLM from causing unintended side effects and to ensure user control over web automation.

*   The agent **NEVER** executes raw shell commands directly.
*   All actions are constrained by a rigid, auditable policy.
*   **Browser automation is strictly limited to authenticated web sessions.**
*   **Explicit user confirmation is MANDATORY** before any message sending or other sensitive web actions.
*   The agent cannot modify its own source code or security policies.
*   No bulk sending and no background execution without explicit policy overrides.

## CLI Usage Examples

**Prerequisites:** Node.js, npm, and Playwright installed. Gemini CLI set up for planning.

1.  **Install & Build:**
    ```bash
    # Navigate to the agent's directory
    cd agent-cli

    # Install dependencies (including playwright)
    npm install

    # Build the project
    npm run build
    ```

2.  **Web Login (one-time setup per platform):**
    ```bash
    # For WhatsApp Web
    node dist/index.js web login whatsapp_web

    # For Instagram Web
    node dist/index.js web login instagram_web
    ```
    This will launch a browser for you to manually log in. Session cookies will be stored.

3.  **Check Web Status:**
    ```bash
    node dist/index.js web status
    ```
    This will show if you are logged in to the web platforms.

4.  **Execute the Agent:**
    Run the CLI command with a natural language task. The Gemini CLI (planner) will interpret this and generate a plan.

    ```bash
    # Example: Send a message on WhatsApp Web
    node dist/index.js do \send a reply on WhatsApp Web to Alice saying Hello!\

    # Example: Draft a message on Instagram Web
    node dist/index.js do \draft a message on Instagram Web to Bob with content Great post!\
    ```
    The agent will pause and ask for confirmation before executing the final `send_message` action.



================================================
FILE: package-lock.json
================================================
{
  "name": "claw-cli",
  "version": "1.1.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "claw-cli",
      "version": "1.1.0",
      "hasInstallScript": true,
      "license": "MIT",
      "dependencies": {
        "@sinclair/typebox": "0.34.48",
        "better-sqlite3": "^11.1.2",
        "chalk": "^5.3.0",
        "commander": "^14.0.3",
        "dotenv": "^16.4.5",
        "express": "^4.19.2",
        "express-rate-limit": "^7.3.1",
        "helmet": "^7.1.0",
        "jsonwebtoken": "^9.0.2",
        "playwright": "^1.45.0",
        "zod": "^3.23.8"
      },
      "bin": {
        "claw": "dist/index.js",
        "claw-cli": "dist/index.js"
      },
      "devDependencies": {
        "@types/better-sqlite3": "^7.6.9",
        "@types/express": "^4.17.21",
        "@types/jsonwebtoken": "^9.0.6",
        "@types/node": "^20.14.9",
        "typescript": "^5.9.3"
      }
    },
    "node_modules/@sinclair/typebox": {
      "version": "0.34.48",
      "resolved": "https://registry.npmjs.org/@sinclair/typebox/-/typebox-0.34.48.tgz",
      "integrity": "sha512-kKJTNuK3AQOrgjjotVxMrCn1sUJwM76wMszfq1kdU4uYVJjvEWuFQ6HgvLt4Xz3fSmZlTOxJ/Ie13KnIcWQXFA==",
      "license": "MIT"
    },
    "node_modules/@types/better-sqlite3": {
      "version": "7.6.13",
      "resolved": "https://registry.npmjs.org/@types/better-sqlite3/-/better-sqlite3-7.6.13.tgz",
      "integrity": "sha512-NMv9ASNARoKksWtsq/SHakpYAYnhBrQgGD8zkLYk/jaK8jUGn08CfEdTRgYhMypUQAfzSP8W6gNLe0q19/t4VA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/node": "*"
      }
    },
    "node_modules/@types/body-parser": {
      "version": "1.19.6",
      "resolved": "https://registry.npmjs.org/@types/body-parser/-/body-parser-1.19.6.tgz",
      "integrity": "sha512-HLFeCYgz89uk22N5Qg3dvGvsv46B8GLvKKo1zKG4NybA8U2DiEO3w9lqGg29t/tfLRJpJ6iQxnVw4OnB7MoM9g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/connect": "*",
        "@types/node": "*"
      }
    },
    "node_modules/@types/connect": {
      "version": "3.4.38",
      "resolved": "https://registry.npmjs.org/@types/connect/-/connect-3.4.38.tgz",
      "integrity": "sha512-K6uROf1LD88uDQqJCktA4yzL1YYAK6NgfsI0v/mTgyPKWsX1CnJ0XPSDhViejru1GcRkLWb8RlzFYJRqGUbaug==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/node": "*"
      }
    },
    "node_modules/@types/express": {
      "version": "4.17.25",
      "resolved": "https://registry.npmjs.org/@types/express/-/express-4.17.25.tgz",
      "integrity": "sha512-dVd04UKsfpINUnK0yBoYHDF3xu7xVH4BuDotC/xGuycx4CgbP48X/KF/586bcObxT0HENHXEU8Nqtu6NR+eKhw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/body-parser": "*",
        "@types/express-serve-static-core": "^4.17.33",
        "@types/qs": "*",
        "@types/serve-static": "^1"
      }
    },
    "node_modules/@types/express-serve-static-core": {
      "version": "4.19.8",
      "resolved": "https://registry.npmjs.org/@types/express-serve-static-core/-/express-serve-static-core-4.19.8.tgz",
      "integrity": "sha512-02S5fmqeoKzVZCHPZid4b8JH2eM5HzQLZWN2FohQEy/0eXTq8VXZfSN6Pcr3F6N9R/vNrj7cpgbhjie6m/1tCA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/node": "*",
        "@types/qs": "*",
        "@types/range-parser": "*",
        "@types/send": "*"
      }
    },
    "node_modules/@types/http-errors": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@types/http-errors/-/http-errors-2.0.5.tgz",
      "integrity": "sha512-r8Tayk8HJnX0FztbZN7oVqGccWgw98T/0neJphO91KkmOzug1KkofZURD4UaD5uH8AqcFLfdPErnBod0u71/qg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/jsonwebtoken": {
      "version": "9.0.10",
      "resolved": "https://registry.npmjs.org/@types/jsonwebtoken/-/jsonwebtoken-9.0.10.tgz",
      "integrity": "sha512-asx5hIG9Qmf/1oStypjanR7iKTv0gXQ1Ov/jfrX6kS/EO0OFni8orbmGCn0672NHR3kXHwpAwR+B368ZGN/2rA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/ms": "*",
        "@types/node": "*"
      }
    },
    "node_modules/@types/mime": {
      "version": "1.3.5",
      "resolved": "https://registry.npmjs.org/@types/mime/-/mime-1.3.5.tgz",
      "integrity": "sha512-/pyBZWSLD2n0dcHE3hq8s8ZvcETHtEuF+3E7XVt0Ig2nvsVQXdghHVcEkIWjy9A0wKfTn97a/PSDYohKIlnP/w==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/ms": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/@types/ms/-/ms-2.1.0.tgz",
      "integrity": "sha512-GsCCIZDE/p3i96vtEqx+7dBUGXrc7zeSK3wwPHIaRThS+9OhWIXRqzs4d6k1SVU8g91DrNRWxWUGhp5KXQb2VA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/node": {
      "version": "20.19.33",
      "resolved": "https://registry.npmjs.org/@types/node/-/node-20.19.33.tgz",
      "integrity": "sha512-Rs1bVAIdBs5gbTIKza/tgpMuG1k3U/UMJLWec

================================================
FILE: package.json
================================================
{
  "name": "claw-cli",
  "version": "1.1.0",
  "description": "A security-first AI agent for browser automation.",
  "main": "dist/index.js",
  "type": "module",
  "bin": {
    "claw": "dist/index.js",
    "claw-cli": "dist/index.js"
  },
  "scripts": {
    "build": "tsc",
    "postinstall": "playwright install --with-deps",
    "start:server": "node dist/server.js"
  },
  "keywords": [
    "ai-agent",
    "security",
    "browser-automation",
    "termux",
    "claw"
  ],
  "author": "psycho-prince",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/psycho-prince/claw-cli.git"
  },
  "dependencies": {
    "@sinclair/typebox": "0.34.48",
    "better-sqlite3": "^11.1.2",
    "commander": "^14.0.3",
    "dotenv": "^16.4.5",
    "express": "^4.19.2",
    "express-rate-limit": "^7.3.1",
    "helmet": "^7.1.0",
    "jsonwebtoken": "^9.0.2",
    "playwright": "^1.45.0",
    "zod": "^3.23.8",
    "chalk": "^5.3.0"
  },
  "devDependencies": {
    "@types/better-sqlite3": "^7.6.9",
    "@types/express": "^4.17.21",
    "@types/jsonwebtoken": "^9.0.6",
    "@types/node": "^20.14.9",
    "typescript": "^5.9.3"
  }
}


================================================
FILE: README.md
================================================
# Claw-CLI: The Security-First Agent That Actually Protects You

OpenClaw got hacked? Meet Claw-CLI — the security-first agent that actually protects you.

## 🚀 Installation (v1.1.0)

### 1. Standard Install (macOS, Linux, Windows)

Install Node.js v18+ and then run:
```bash
npm install -g claw-cli
```
The `postinstall` script will automatically download the necessary Playwright browsers.

### 2. Android Termux Guide

Termux requires a few extra steps:
```bash
# 1. Install dependencies
pkg install nodejs-lts git

# 2. Install claw-cli globally
npm install -g claw-cli

# 3. Manually install Playwright browsers (postinstall might fail)
npx playwright install --with-deps
```

### 3. Quick Start

After installation, run the doctor to check your setup:
```bash
claw doctor
```

Initialize your config file:
```bash
claw init
```

See available commands:
```bash
claw --help
```

Start the server (for web UI or remote access):
```bash
claw --server
```

## ✨ Features

*   **Security-First Design:** Unlike other agents, Claw-CLI operates on a "fail-closed" principle. Every action is explicitly allow-listed and validated, ensuring the LLM *cannot* execute arbitrary or unsafe commands.
*   **Sandboxed Execution:** All web automation occurs within an isolated browser environment, preventing unintended system access.
*   **User Confirmation for Sensitive Actions:** Critical operations (e.g., sending messages) require explicit user approval. You're always in control.
*   **Auditable Logs:** Every agent action and decision is logged for transparency and security auditing.
*   **Local-First, Single-User:** Designed for your personal machine, offering robust security without the complexities of multi-user environments.

## ⚔️ Claw-CLI vs. OpenClaw: A Security Showdown (February 2026)

| Feature             | OpenClaw (CVE-2026-25253, RCE, Command Injection) | Claw-CLI (Security-First by Design)         |
| :------------------ | :------------------------------------------------ | :------------------------------------------ |
| **Security Model**  | Permissive, Prone to LLM "hallucinations"        | **Fail-Closed, Explicit Allow-List**          |
| **CVE-2026-25253**  | **Vulnerable (8.8 RCE!)**                         | **Immune by Design**                          |
| **Command Injection** | **Widespread Vulnerabilities**                    | **Impossible: No Raw Shell Access**           |
| **Infostealers**    | **Key/Config Exposure Risk**                      | **Sandboxed, Isolated Environment**           |
| **Malicious Skills** | 900+ known, execution often unrestricted         | **Policy-Engine Verified: Safe by Default**   |
| **Control**         | LLM often dictates actions                         | **User Always Confirms Sensitive Actions**    |
| **Deployment**      | Any environment, often insecurely                 | **Local & Secure; ClawCloud for Managed**     |
| **Trust Model**     | Trust in LLM + Skill Developers                    | **Trust in Code, Auditable Policies**         |

## 🖼️ Demo (Coming Soon!)

<!-- TODO: Insert a stunning demo GIF here showing the CLI in action,
    executing a complex web task securely and requiring user confirmation. -->

## 🔒 Security Model: How Claw-CLI Protects You

Claw-CLI operates on a rigorous `Input -> Plan -> Policy -> Execute -> Audit` loop:

1.  **Input:** Your natural language task.
2.  **Plan:** An advanced LLM (like Gemini) breaks down your task into discrete, structured actions (JSON).
3.  **Policy (THE CORE):** Our battle-hardened policy engine intercepts *every single action*. If an action isn't explicitly allowed and safe, the *entire plan is rejected*. **No exceptions.**
4.  **Execute:** Approved actions run in a tightly sandboxed, read-only browser environment. Sensitive actions require your explicit `[Y/n]` confirmation.
5.  **Audit:** Every step is logged, providing full transparency and traceability.

**Claw-CLI NEVER executes raw shell commands. All actions are strictly constrained.**

## ☁️ Local vs. ClawCloud (Managed SaaS)

Claw-CLI is designed to be fully open-source and free for local, single-user use on your machine. This gives you maximum control and privacy.

For teams and businesses requiring advanced features, scalability, and managed infrastructure, we're building **ClawCloud**.

*   **Claw-CLI (Open-Source):**
    *   Local execution, single-user.
    *   Full privacy, data stays on your machine.
    *   No monthly fees.
    *   Self-managed setup.

*   **ClawCloud (Managed SaaS):**
    *   **All Claw-CLI features, plus:**
    *   Secure, hosted multi-tenant environment.
    *   Scalable execution for high-volume tasks.
    *   Team collaboration & access controls.
    *   Advanced analytics & reporting.
    *   Dedicated support.
    *   Guaranteed uptime & SLA.
    *   _Coming Soon: Premium LLM integrations, enhanced security auditing._

## 💰 ClawCloud Pricing (Teaser)

Starting at **₹499/month** for individuals, up to **₹1999/month** 

================================================
FILE: SECURITY.md
================================================
# Security Policy

This document outlines the security posture, threat model, and safe usage expectations for `claw-cli-agent`. This project prioritizes a "security-first" approach to autonomous agent execution.

## Threat Model

The primary threat this agent is designed to mitigate is unintended action execution resulting from a compromised or "hallucinating" Large Language Model (LLM).

*   **Adversary:** The LLM planner is treated as an untrusted source of commands. While a powerful tool, it can be manipulated via prompt injection or may generate unsafe instructions.
*   **Goal:** The agent's security goal is to prevent the LLM from executing arbitrary commands, reading sensitive data, or causing any unintended system modification.
*   **Attack Vectors:** The model assumes attack vectors originate from the LLM's output, such as a plan containing:
    *   Unauthorized shell commands (e.g., `rm -rf /`).
    *   Attempts to read sensitive files (e.g., `~/.ssh/id_rsa`).
    *   Unauthorized network connections to malicious endpoints.

## Philosophy: Fail-Closed and Policy-Driven

The cornerstone of this agent's security is its "fail-closed" philosophy.

*   **Explicit Allowance:** No action is ever implicitly trusted. Only capabilities that are explicitly defined in the `Policy` module are candidates for execution.
*   **Strict Validation:** Every proposed action and its arguments are rigorously validated against a predefined schema. Any deviation results in immediate rejection of the entire plan.
*   **Halt on Violation:** A single policy violation halts the agent's execution loop, preventing it from proceeding with a potentially unsafe plan.

This is **not a general-purpose shell agent**. It is a task-specific executor that operates under a highly restrictive and auditable security policy.

## Explicit Non-Goals

To maintain a clear security boundary, `claw-cli-agent` is **NOT** designed for:

*   **Arbitrary Shell Execution:** The agent is fundamentally incapable of executing raw shell commands.
*   **Self-Modification:** The agent cannot alter its own security policies or source code.

## Cloud Security Mitigations (for ClawCloud SaaS)

For the ClawCloud managed service, additional layers of security are implemented:

*   **Rate Limiting:** All API endpoints are protected by rate limiting to prevent abuse and denial-of-service attacks.
*   **Security Headers (Helmet):** Standard security headers are enforced to mitigate common web vulnerabilities like XSS, clickjacking, and others.
*   **Input Sanitization & Validation:** All user inputs to the ClawCloud API are rigorously sanitized and validated using strong schemas (`zod`).
*   **Authentication (JWT):** User access to protected endpoints is secured using JSON Web Tokens.
*   **Multi-Tenancy Isolation:** Agent execution for each user is designed to be isolated, preventing cross-tenant data access or interference. (Detailed implementation in `server/`).
*   **Data Encryption:** Sensitive data at rest (e.g., user database) and in transit (HTTPS) is encrypted.
*   **Auditable Logging:** Comprehensive logs are maintained for all server actions, agent executions, and security events.

## Safe Usage Assumptions

The security model of `claw-cli-agent` relies on the following assumptions:

*   **Trusted User (Local CLI):** The user operating the local CLI is trusted.
*   **Secure Host:** The machine running the agent is not already compromised.
*   **Policy Review:** The user is expected to understand the capabilities defined in the policy files. This is the definitive source of truth for what the agent can and cannot do.
*   **ClawCloud Users:** ClawCloud users are authenticated and operate within their defined quotas and access policies.

If you discover a security vulnerability, please report it responsibly by opening a security advisory on the GitHub repository.



================================================
FILE: tsconfig.json
================================================
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "node",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,
    "declarationMap": true
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules", "dist"]
}


================================================
FILE: src\agent.ts
================================================
import { Static, Type } from '@sinclair/typebox';
import { Policy } from './policy.js';
import { Executor } from './executor.js';

// Define the schema for actions
const ActionSchema = Type.Object({
  action: Type.String(),
  args: Type.Record(Type.String(), Type.Any()),
});

type AgentAction = Static<typeof ActionSchema>;

export class Agent {
  private policy: Policy;
  private executor: Executor;

  constructor() {
    this.policy = new Policy();
    this.executor = new Executor();
  }

  async run(task: string): Promise<any> {
    console.log(`[Agent] Planning for task: "${task}"`);
    const plan = await this.plan(task); // This would interact with Gemini

    console.log('[Agent] Validating plan...');
    this.policy.validatePlan(plan);

    console.log('[Agent] Executing actions...');
    const result = await this.execute(plan);

    console.log('[Agent] Logging audit...');
    this.log(task, plan, result);

    return result;
  }

  private async plan(task: string): Promise<AgentAction[]> {
    // TODO: Integrate with a Large Language Model (e.g., Gemini) here.
    // This function would send the 'task' to the LLM and receive a structured JSON
    // response containing a sequence of 'AgentAction' objects to be executed.
    // The LLM's role is purely for reasoning and planning, outputting actions
    // that the Policy module will then validate.
    console.log(`[Planner] Sending task to LLM for planning: "${task}"`);
    // Current: Simulate LLM's response with allowed actions for demonstration
    return [
      {
        action: 'list_directory',
        args: { path: '/' },
      },
      {
        action: 'read_file',
        args: { path: '/tmp/example.txt' },
      },
    ];
  }

  private async execute(actions: AgentAction[]): Promise<any[]> {
    const results: any[] = [];
    for (const action of actions) {
      console.log(`[Executor] Executing action: "${action.action}" with args:`, action.args);
      const result = await this.executor.execute(action.action, action.args);
      results.push(result);
    }
    return results;
  }

  private log(task: string, plan: AgentAction[], result: any): void {
    // Placeholder for audit logging
    console.log('[Audit Log] Task:', task);
    console.log('[Audit Log] Plan:', JSON.stringify(plan, null, 2));
    console.log('[Audit Log] Result:', JSON.stringify(result, null, 2));
    // In a real system, this would write to a secure, append-only log file.
  }
}


================================================
FILE: src\doctor.ts
================================================
import chalk from 'chalk';
import { execSync } from 'child_process';
import fs from 'fs';
import path from 'path';
import os from 'os';

// This file contains the logic for the `claw doctor` command.
// It checks for common issues in the user's environment.

async function checkNodeVersion() {
    const version = process.versions.node;
    const major = parseInt(version.split('.')[0], 10);
    if (major < 18) {
        return { success: false, message: `Node.js version is ${version}, but v18+ is required.` };
    }
    return { success: true, message: `Node.js version: ${version}` };
}

async function checkPlaywright() {
    try {
        // This is a proxy for checking if the browsers are installed.
        // A more robust check would be to actually try and launch a browser.
        execSync('npx playwright-cli --version', { stdio: 'ignore' });
        return { success: true, message: 'Playwright seems to be installed.' };
    } catch (error) {
        return { success: false, message: 'Playwright browsers are not installed. Please run: npx playwright install --with-deps' };
    }
}

async function checkGeminiKey() {
    const envPath = path.join(process.cwd(), '.env');
    if (fs.existsSync(envPath)) {
        const envContent = fs.readFileSync(envPath, 'utf-8');
        if (/^GEMINI_API_KEY=./m.test(envContent)) {
            return { success: true, message: 'GEMINI_API_KEY found in .env file.' };
        }
    }
    return { success: false, message: 'GEMINI_API_KEY not found. Please add it to your .env file.' };
}

export async function runDoctor() {
    console.log(chalk.bold.cyan('Running `claw doctor`...'));
    const checks = [
        await checkNodeVersion(),
        await checkPlaywright(),
        await checkGeminiKey(),
    ];

    let allGood = true;
    checks.forEach(check => {
        if (check.success) {
            console.log(chalk.green('✅ ' + check.message));
        } else {
            console.log(chalk.red('❌ ' + check.message));
            allGood = false;
        }
    });

    if (allGood) {
        console.log(chalk.bold.green('\nAll checks passed! Claw-CLI is ready to go.'));
    } else {
        console.log(chalk.bold.yellow('\nPlease fix the issues above to ensure Claw-CLI works correctly.'));
        process.exit(1);
    }
}


================================================
FILE: src\executor.ts
================================================
import * as fs from 'node:fs/promises';
import * as path from 'node:path';

export class Executor {
  async execute(action: string, args: Record<string, any>): Promise<any> {
    switch (action) {
      case 'read_file':
        return this.readFile(args.path);
      case 'list_directory':
        return this.listDirectory(args.path);
      // TODO: Add more intentionally restricted and sandboxed actions here.
      // Each action must be carefully designed to prevent unintended side effects.
      default:
        throw new Error(`Unknown action: ${action}. This action is not implemented in the Executor.`);
    }
  }

  /**
   * Intentionally restricted execution of reading a file.
   * In this alpha version, this operation is mocked or strictly limited.
   *
   * @param filePath The path to the file to read.
   * @returns A promise that resolves with the file content.
   */
  private async readFile(filePath: string): Promise<string> {
    // Current: This operation is mocked for demonstration purposes, emphasizing read-only safety.
    // TODO: Implement actual sandboxed file reading. This would involve a secure
    // sandbox mechanism that strictly controls access to specific, pre-approved directories
    // and prevents path traversal attacks.
    console.warn(`[Executor] Sandboxed, read-only readFile operation for: ${filePath}. Current implementation is mocked.`);
    if (filePath === '/tmp/example.txt') {
      return Promise.resolve('This is an example file content.');
    }
    // Critical: For any other path, access is denied to uphold the fail-closed security principle.
    throw new Error(`Access denied: Cannot read file from ${filePath}. Only explicitly allowed paths are accessible.`);
  }

  /**
   * Intentionally restricted execution of listing a directory.
   * In this alpha version, this operation is mocked or strictly limited.
   *
   * @param dirPath The path to the directory to list.
   * @returns A promise that resolves with a list of directory entries.
   */
  private async listDirectory(dirPath: string): Promise<string[]> {
    // Current: This operation is mocked for demonstration purposes, emphasizing read-only safety.
    // TODO: Implement actual sandboxed directory listing. This would involve a secure
    // sandbox mechanism that strictly controls access to specific, pre-approved directories
    // and prevents path traversal attacks.
    console.warn(`[Executor] Sandboxed, read-only listDirectory operation for: ${dirPath}. Current implementation is mocked.`);
    if (dirPath === '/') {
      return Promise.resolve(['tmp', 'home', 'var']);
    }
    if (dirPath === '/tmp') {
      return Promise.resolve(['example.txt', 'another.log']);
    }
    // Critical: For any other path, access is denied to uphold the fail-closed security principle.
    throw new Error(`Access denied: Cannot list directory ${dirPath}. Only explicitly allowed paths are accessible.`);
  }
}


================================================
FILE: src\index.ts
================================================

import { Command } from 'commander';
import { Agent } from './agent.js';
import { runDoctor } from './doctor.js';
import { runInit } from './init.js';
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const pkg = require('../package.json');


const program = new Command();

program
  .name('claw')
  .description('Claw-CLI for secure autonomous agent execution')
  .version(pkg.version)
  .option('--server', 'Run Claw-CLI in server mode for ClawCloud');

program.command('do')
  .description('Execute a task with the autonomous agent')
  .argument('<task>', 'The task string for the agent to execute')
  .action(async (task: string) => {
    if (program.opts().server) {
      console.error('Error: Cannot use "do" command with "--server" option.');
      process.exit(1);
    }
    console.log(`Starting agent for task: "${task}"`);
    const agent = new Agent();
    try {
      const result = await agent.run(task);
      console.log('Agent finished with result:', result);
    } catch (error: any) {
      console.error('Agent failed:', error.message);
      process.exit(1);
    }
  });

program.command('doctor')
    .description('Check if all dependencies and configurations are set up correctly')
    .action(runDoctor);

program.command('init')
    .description('Initialize Claw-CLI configuration and .env file')
    .action(runInit);


// Handle server mode separately
if (process.argv.includes('--server')) {
    console.log('Claw-CLI starting in server mode...');
    import('./server.js').catch(error => {
        console.error('Failed to start server:', error);
        process.exit(1);
    });
} else {
    program.parse(process.argv);
}


================================================
FILE: src\init.ts
================================================

import chalk from 'chalk';
import fs from 'fs';
import path from 'path';
import os from 'os';

const CLAW_DIR = path.join(os.homedir(), '.claw');
const CONFIG_FILE = path.join(CLAW_DIR, 'config.json');
const ENV_FILE = path.join(process.cwd(), '.env');

const defaultConfig = {
    "version": "1.0",
    "llm": {
        "provider": "gemini",
        "model": "gemini-1.5-pro-latest"
    },
    "security": {
        "mode": "fail-closed",
        "allow_list": [
            "browse",
            "read",
            "click",
            "type",
            "ask"
        ]
    }
};

const defaultEnv = `GEMINI_API_KEY="YOUR_API_KEY_HERE"
`;

export async function runInit() {
    console.log(chalk.bold.cyan('Running `claw init`...'));

    // Create ~/.claw directory
    if (!fs.existsSync(CLAW_DIR)) {
        fs.mkdirSync(CLAW_DIR);
        console.log(chalk.green(`Created directory: ${CLAW_DIR}`));
    } else {
        console.log(chalk.yellow(`Directory already exists: ${CLAW_DIR}`));
    }

    // Create ~/.claw/config.json
    if (!fs.existsSync(CONFIG_FILE)) {
        fs.writeFileSync(CONFIG_FILE, JSON.stringify(defaultConfig, null, 2));
        console.log(chalk.green(`Created config file: ${CONFIG_FILE}`));
    } else {
        console.log(chalk.yellow(`Config file already exists: ${CONFIG_FILE}`));
    }

    // Create .env file
    if (!fs.existsSync(ENV_FILE)) {
        fs.writeFileSync(ENV_FILE, defaultEnv);
        console.log(chalk.green(`Created .env file in current directory. Please add your GEMINI_API_KEY.`));
    } else {
        console.log(chalk.yellow(`.env file already exists in current directory.`));
    }

    console.log(chalk.bold.green('
Initialization complete!'));
    console.log(chalk.yellow('Please edit the .env file to add your Gemini API key.'));
}


================================================
FILE: src\policy.ts
================================================
import { Static, Type } from '@sinclair/typebox';

// Define the schema for actions
const ActionSchema = Type.Object({
  action: Type.String(),
  args: Type.Record(Type.String(), Type.Any()),
});

type AgentAction = Static<typeof ActionSchema>;

export class Policy {
  private allowedActions: Set<string>;

  constructor() {
    // CRITICAL: This set defines the ONLY actions the agent is permitted to execute.
    // Any action not in this list will be rejected by the policy enforcement.
    this.allowedActions = new Set([
      'read_file',
      'list_directory',
      // TODO: Add more safe and sandboxed actions here as the agent's capabilities expand.
      // Each addition must be carefully reviewed for security implications.
    ]);
  }

  /**
   * Validates a plan (a sequence of actions) against the defined security policy.
   * If any action or its arguments violate the policy, an error is thrown,
   * enforcing the "fail-closed" philosophy.
   */
  validatePlan(plan: AgentAction[]): void {
    for (const action of plan) {
      if (!this.allowedActions.has(action.action)) {
        throw new Error(`Policy violation: Action "${action.action}" is not allowed by the security policy.`);
      }
      // TODO: Implement more granular argument validation here.
      // This would involve checking specific properties of 'action.args'
      // For example, for 'read_file', ensure the path is within an allowed directory,
      // and does not contain sensitive system paths or traversal attempts.
      // Example:
      // if (action.action === 'read_file') {
      //   const filePath = action.args.path as string;
      //   if (!filePath.startsWith('/safe_data/') || filePath.includes('..')) {
      //     throw new Error(`Policy violation: Unauthorized file path for read_file: ${filePath}`);
      //   }
      // }
    }
    console.log('[Policy] Plan validated successfully. All actions adhere to the security policy.');
  }
}


================================================
FILE: src\server.ts
================================================
import express from 'express';
import { json } from 'express';
import jwt from 'jsonwebtoken';
import { config } from 'dotenv';
import BetterSqlite3 from 'better-sqlite3';
import { z } from 'zod'; // Using zod for input validation
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';

// Load environment variables
config();

const CLAW_CLOUD_ENABLED = process.env.CLAW_CLOUD_ENABLED === 'true';
const JWT_SECRET = process.env.JWT_SECRET || 'supersecretjwtkey'; // In production, use a strong, unique key from env
const STRIPE_SECRET_KEY = process.env.STRIPE_SECRET_KEY || 'sk_test_123';
const STRIPE_WEBHOOK_SECRET = process.env.STRIPE_WEBHOOK_SECRET || 'whsec_123';
const DATABASE_URL = process.env.DATABASE_URL || './data/clawcloud.db';
const ADMIN_API_KEY = process.env.ADMIN_API_KEY || 'admin_api_key';

if (!CLAW_CLOUD_ENABLED) {
  console.log("ClawCloud server is disabled. Set CLAW_CLOUD_ENABLED=true in your .env to enable.");
  process.exit(0);
}

// Initialize SQLite Database
const db = new BetterSqlite3(DATABASE_URL);

// Create users table if it doesn't exist
db.exec(`
  CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    stripeCustomerId TEXT,
    plan TEXT DEFAULT 'free',
    quota int DEFAULT 100,
    lastLogin TEXT,
    createdAt TEXT DEFAULT CURRENT_TIMESTAMP
  );
`);

const app = express();
const PORT = process.env.PORT || 3000;

// Security Middlewares
app.use(helmet()); // Basic security headers
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  message: "Too many requests from this IP, please try again after 15 minutes",
  standardHeaders: true, // Return rate limit info in the `RateLimit-*` headers
  legacyHeaders: false, // Disable the `X-RateLimit-*` headers
});
app.use(limiter); // Apply rate limiting to all requests

// Middleware to parse JSON for most routes
app.use((req, res, next) => {
  if (req.originalUrl === '/webhook/stripe') {
    next(); // Skip JSON parsing for Stripe webhook, as it needs raw body
  } else {
    json()(req, res, next);
  }
});

// Zod schemas for validation
const LoginSchema = z.object({
  email: z.string().email(),
  // In a real app, we'd have a password and bcrypt it
});

const TaskSchema = z.object({
  task: z.string().min(5).max(500), // Example task validation
});

// Middleware for JWT authentication
const authenticateJWT = (req: any, res: express.Response, next: express.NextFunction) => {
  const authHeader = req.headers.authorization;

  if (authHeader) {
    const token = authHeader.split(' ')[1]; // Bearer TOKEN

    jwt.verify(token, JWT_SECRET, (err: any, user: any) => {
      if (err) {
        return res.sendStatus(403); // Forbidden
      }
      req.user = user;
      next();
    });
  } else {
    res.sendStatus(401); // Unauthorized
  }
};

// Middleware for quota checking
const checkQuota = (req: any, res: express.Response, next: express.NextFunction) => {
  // This is a simplified check. In a real app, this would be more sophisticated
  // and involve decrementing quota after successful task execution.
  const user = db.prepare('SELECT quota FROM users WHERE id = ?').get(req.user.id);

  if (!user || user.quota <= 0) {
    return res.status(403).json({ message: 'Quota exceeded. Please upgrade your plan.' });
  }
  next();
};

// --- Routes ---

// Public route for user login/registration (simplified)
app.post('/auth/login', (req, res) => {
  const parseResult = LoginSchema.safeParse(req.body);
  if (!parseResult.success) {
    return res.status(400).json({ errors: parseResult.error.errors });
  }

  const { email } = parseResult.data;
  let user = db.prepare('SELECT id, email, quota, plan FROM users WHERE email = ?').get(email);

  if (!user) {
    // Register new user
    const newUser = {
      id: crypto.randomUUID(), // Node.js 16+
      email,
      plan: 'free',
      quota: 100, // Free tier quota
      createdAt: new Date().toISOString(),
    };
    db.prepare('INSERT INTO users (id, email, plan, quota, createdAt) VALUES (?, ?, ?, ?, ?)').run(
      newUser.id, newUser.email, newUser.plan, newUser.quota, newUser.createdAt
    );
    user = newUser;
  }

  // Update last login
  db.prepare('UPDATE users SET lastLogin = ? WHERE id = ?').run(new Date().toISOString(), user.id);

  const token = jwt.sign({ id: user.id, email: user.email, plan: user.plan }, JWT_SECRET, { expiresIn: '1h' });
  res.json({ token, user: { id: user.id, email: user.email, plan: user.plan, quota: user.quota } });
});

// Protected route for agent task execution
app.post('/api/agent/do', authenticateJWT, checkQuota, async (req, res) => {
  const parseResult = TaskSchema.safeParse(req.body);
  if (!parseResult.success) {
    return res.status(400).json({ errors: parseResult.error.errors });
  }
  const { task } = parseResult.data;
  const user = req.user; // From authenticateJWT middleware

  console.log(`[ClawCloud] User ${user.
```

## File: .github\FUNDING.yml
```
github: psycho-prince
custom: ["https://www.buymeacoffee.com/psychoprince", "https://forms.gle/uKuj7huVmLDSYzvT8"]

```

## File: src\agent.ts
```
import { Static, Type } from '@sinclair/typebox';
import { Policy } from './policy.js';
import { Executor } from './executor.js';

// Define the schema for actions
const ActionSchema = Type.Object({
  action: Type.String(),
  args: Type.Record(Type.String(), Type.Any()),
});

type AgentAction = Static<typeof ActionSchema>;

export class Agent {
  private policy: Policy;
  private executor: Executor;

  constructor() {
    this.policy = new Policy();
    this.executor = new Executor();
  }

  async run(task: string): Promise<any> {
    console.log(`[Agent] Planning for task: "${task}"`);
    const plan = await this.plan(task); // This would interact with Gemini

    console.log('[Agent] Validating plan...');
    this.policy.validatePlan(plan);

    console.log('[Agent] Executing actions...');
    const result = await this.execute(plan);

    console.log('[Agent] Logging audit...');
    this.log(task, plan, result);

    return result;
  }

  private async plan(task: string): Promise<AgentAction[]> {
    // TODO: Integrate with a Large Language Model (e.g., Gemini) here.
    // This function would send the 'task' to the LLM and receive a structured JSON
    // response containing a sequence of 'AgentAction' objects to be executed.
    // The LLM's role is purely for reasoning and planning, outputting actions
    // that the Policy module will then validate.
    console.log(`[Planner] Sending task to LLM for planning: "${task}"`);
    // Current: Simulate LLM's response with allowed actions for demonstration
    return [
      {
        action: 'list_directory',
        args: { path: '/' },
      },
      {
        action: 'read_file',
        args: { path: '/tmp/example.txt' },
      },
    ];
  }

  private async execute(actions: AgentAction[]): Promise<any[]> {
    const results: any[] = [];
    for (const action of actions) {
      console.log(`[Executor] Executing action: "${action.action}" with args:`, action.args);
      const result = await this.executor.execute(action.action, action.args);
      results.push(result);
    }
    return results;
  }

  private log(task: string, plan: AgentAction[], result: any): void {
    // Placeholder for audit logging
    console.log('[Audit Log] Task:', task);
    console.log('[Audit Log] Plan:', JSON.stringify(plan, null, 2));
    console.log('[Audit Log] Result:', JSON.stringify(result, null, 2));
    // In a real system, this would write to a secure, append-only log file.
  }
}

```

## File: src\doctor.ts
```
import chalk from 'chalk';
import { execSync } from 'child_process';
import fs from 'fs';
import path from 'path';
import os from 'os';

// This file contains the logic for the `claw doctor` command.
// It checks for common issues in the user's environment.

async function checkNodeVersion() {
    const version = process.versions.node;
    const major = parseInt(version.split('.')[0], 10);
    if (major < 18) {
        return { success: false, message: `Node.js version is ${version}, but v18+ is required.` };
    }
    return { success: true, message: `Node.js version: ${version}` };
}

async function checkPlaywright() {
    try {
        // This is a proxy for checking if the browsers are installed.
        // A more robust check would be to actually try and launch a browser.
        execSync('npx playwright-cli --version', { stdio: 'ignore' });
        return { success: true, message: 'Playwright seems to be installed.' };
    } catch (error) {
        return { success: false, message: 'Playwright browsers are not installed. Please run: npx playwright install --with-deps' };
    }
}

async function checkGeminiKey() {
    const envPath = path.join(process.cwd(), '.env');
    if (fs.existsSync(envPath)) {
        const envContent = fs.readFileSync(envPath, 'utf-8');
        if (/^GEMINI_API_KEY=./m.test(envContent)) {
            return { success: true, message: 'GEMINI_API_KEY found in .env file.' };
        }
    }
    return { success: false, message: 'GEMINI_API_KEY not found. Please add it to your .env file.' };
}

export async function runDoctor() {
    console.log(chalk.bold.cyan('Running `claw doctor`...'));
    const checks = [
        await checkNodeVersion(),
        await checkPlaywright(),
        await checkGeminiKey(),
    ];

    let allGood = true;
    checks.forEach(check => {
        if (check.success) {
            console.log(chalk.green('✅ ' + check.message));
        } else {
            console.log(chalk.red('❌ ' + check.message));
            allGood = false;
        }
    });

    if (allGood) {
        console.log(chalk.bold.green('\nAll checks passed! Claw-CLI is ready to go.'));
    } else {
        console.log(chalk.bold.yellow('\nPlease fix the issues above to ensure Claw-CLI works correctly.'));
        process.exit(1);
    }
}

```

## File: src\executor.ts
```
import * as fs from 'node:fs/promises';
import * as path from 'node:path';

export class Executor {
  async execute(action: string, args: Record<string, any>): Promise<any> {
    switch (action) {
      case 'read_file':
        return this.readFile(args.path);
      case 'list_directory':
        return this.listDirectory(args.path);
      // TODO: Add more intentionally restricted and sandboxed actions here.
      // Each action must be carefully designed to prevent unintended side effects.
      default:
        throw new Error(`Unknown action: ${action}. This action is not implemented in the Executor.`);
    }
  }

  /**
   * Intentionally restricted execution of reading a file.
   * In this alpha version, this operation is mocked or strictly limited.
   *
   * @param filePath The path to the file to read.
   * @returns A promise that resolves with the file content.
   */
  private async readFile(filePath: string): Promise<string> {
    // Current: This operation is mocked for demonstration purposes, emphasizing read-only safety.
    // TODO: Implement actual sandboxed file reading. This would involve a secure
    // sandbox mechanism that strictly controls access to specific, pre-approved directories
    // and prevents path traversal attacks.
    console.warn(`[Executor] Sandboxed, read-only readFile operation for: ${filePath}. Current implementation is mocked.`);
    if (filePath === '/tmp/example.txt') {
      return Promise.resolve('This is an example file content.');
    }
    // Critical: For any other path, access is denied to uphold the fail-closed security principle.
    throw new Error(`Access denied: Cannot read file from ${filePath}. Only explicitly allowed paths are accessible.`);
  }

  /**
   * Intentionally restricted execution of listing a directory.
   * In this alpha version, this operation is mocked or strictly limited.
   *
   * @param dirPath The path to the directory to list.
   * @returns A promise that resolves with a list of directory entries.
   */
  private async listDirectory(dirPath: string): Promise<string[]> {
    // Current: This operation is mocked for demonstration purposes, emphasizing read-only safety.
    // TODO: Implement actual sandboxed directory listing. This would involve a secure
    // sandbox mechanism that strictly controls access to specific, pre-approved directories
    // and prevents path traversal attacks.
    console.warn(`[Executor] Sandboxed, read-only listDirectory operation for: ${dirPath}. Current implementation is mocked.`);
    if (dirPath === '/') {
      return Promise.resolve(['tmp', 'home', 'var']);
    }
    if (dirPath === '/tmp') {
      return Promise.resolve(['example.txt', 'another.log']);
    }
    // Critical: For any other path, access is denied to uphold the fail-closed security principle.
    throw new Error(`Access denied: Cannot list directory ${dirPath}. Only explicitly allowed paths are accessible.`);
  }
}

```

## File: src\index.ts
```

import { Command } from 'commander';
import { Agent } from './agent.js';
import { runDoctor } from './doctor.js';
import { runInit } from './init.js';
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const pkg = require('../package.json');


const program = new Command();

program
  .name('claw')
  .description('Claw-CLI for secure autonomous agent execution')
  .version(pkg.version)
  .option('--server', 'Run Claw-CLI in server mode for ClawCloud');

program.command('do')
  .description('Execute a task with the autonomous agent')
  .argument('<task>', 'The task string for the agent to execute')
  .action(async (task: string) => {
    if (program.opts().server) {
      console.error('Error: Cannot use "do" command with "--server" option.');
      process.exit(1);
    }
    console.log(`Starting agent for task: "${task}"`);
    const agent = new Agent();
    try {
      const result = await agent.run(task);
      console.log('Agent finished with result:', result);
    } catch (error: any) {
      console.error('Agent failed:', error.message);
      process.exit(1);
    }
  });

program.command('doctor')
    .description('Check if all dependencies and configurations are set up correctly')
    .action(runDoctor);

program.command('init')
    .description('Initialize Claw-CLI configuration and .env file')
    .action(runInit);


// Handle server mode separately
if (process.argv.includes('--server')) {
    console.log('Claw-CLI starting in server mode...');
    import('./server.js').catch(error => {
        console.error('Failed to start server:', error);
        process.exit(1);
    });
} else {
    program.parse(process.argv);
}

```

## File: src\init.ts
```

import chalk from 'chalk';
import fs from 'fs';
import path from 'path';
import os from 'os';

const CLAW_DIR = path.join(os.homedir(), '.claw');
const CONFIG_FILE = path.join(CLAW_DIR, 'config.json');
const ENV_FILE = path.join(process.cwd(), '.env');

const defaultConfig = {
    "version": "1.0",
    "llm": {
        "provider": "gemini",
        "model": "gemini-1.5-pro-latest"
    },
    "security": {
        "mode": "fail-closed",
        "allow_list": [
            "browse",
            "read",
            "click",
            "type",
            "ask"
        ]
    }
};

const defaultEnv = `GEMINI_API_KEY="YOUR_API_KEY_HERE"
`;

export async function runInit() {
    console.log(chalk.bold.cyan('Running `claw init`...'));

    // Create ~/.claw directory
    if (!fs.existsSync(CLAW_DIR)) {
        fs.mkdirSync(CLAW_DIR);
        console.log(chalk.green(`Created directory: ${CLAW_DIR}`));
    } else {
        console.log(chalk.yellow(`Directory already exists: ${CLAW_DIR}`));
    }

    // Create ~/.claw/config.json
    if (!fs.existsSync(CONFIG_FILE)) {
        fs.writeFileSync(CONFIG_FILE, JSON.stringify(defaultConfig, null, 2));
        console.log(chalk.green(`Created config file: ${CONFIG_FILE}`));
    } else {
        console.log(chalk.yellow(`Config file already exists: ${CONFIG_FILE}`));
    }

    // Create .env file
    if (!fs.existsSync(ENV_FILE)) {
        fs.writeFileSync(ENV_FILE, defaultEnv);
        console.log(chalk.green(`Created .env file in current directory. Please add your GEMINI_API_KEY.`));
    } else {
        console.log(chalk.yellow(`.env file already exists in current directory.`));
    }

    console.log(chalk.bold.green('
Initialization complete!'));
    console.log(chalk.yellow('Please edit the .env file to add your Gemini API key.'));
}

```

## File: src\policy.ts
```
import { Static, Type } from '@sinclair/typebox';

// Define the schema for actions
const ActionSchema = Type.Object({
  action: Type.String(),
  args: Type.Record(Type.String(), Type.Any()),
});

type AgentAction = Static<typeof ActionSchema>;

export class Policy {
  private allowedActions: Set<string>;

  constructor() {
    // CRITICAL: This set defines the ONLY actions the agent is permitted to execute.
    // Any action not in this list will be rejected by the policy enforcement.
    this.allowedActions = new Set([
      'read_file',
      'list_directory',
      // TODO: Add more safe and sandboxed actions here as the agent's capabilities expand.
      // Each addition must be carefully reviewed for security implications.
    ]);
  }

  /**
   * Validates a plan (a sequence of actions) against the defined security policy.
   * If any action or its arguments violate the policy, an error is thrown,
   * enforcing the "fail-closed" philosophy.
   */
  validatePlan(plan: AgentAction[]): void {
    for (const action of plan) {
      if (!this.allowedActions.has(action.action)) {
        throw new Error(`Policy violation: Action "${action.action}" is not allowed by the security policy.`);
      }
      // TODO: Implement more granular argument validation here.
      // This would involve checking specific properties of 'action.args'
      // For example, for 'read_file', ensure the path is within an allowed directory,
      // and does not contain sensitive system paths or traversal attempts.
      // Example:
      // if (action.action === 'read_file') {
      //   const filePath = action.args.path as string;
      //   if (!filePath.startsWith('/safe_data/') || filePath.includes('..')) {
      //     throw new Error(`Policy violation: Unauthorized file path for read_file: ${filePath}`);
      //   }
      // }
    }
    console.log('[Policy] Plan validated successfully. All actions adhere to the security policy.');
  }
}

```

## File: src\server.ts
```
import express from 'express';
import { json } from 'express';
import jwt from 'jsonwebtoken';
import { config } from 'dotenv';
import BetterSqlite3 from 'better-sqlite3';
import { z } from 'zod'; // Using zod for input validation
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';

// Load environment variables
config();

const CLAW_CLOUD_ENABLED = process.env.CLAW_CLOUD_ENABLED === 'true';
const JWT_SECRET = process.env.JWT_SECRET || 'supersecretjwtkey'; // In production, use a strong, unique key from env
const STRIPE_SECRET_KEY = process.env.STRIPE_SECRET_KEY || 'sk_test_123';
const STRIPE_WEBHOOK_SECRET = process.env.STRIPE_WEBHOOK_SECRET || 'whsec_123';
const DATABASE_URL = process.env.DATABASE_URL || './data/clawcloud.db';
const ADMIN_API_KEY = process.env.ADMIN_API_KEY || 'admin_api_key';

if (!CLAW_CLOUD_ENABLED) {
  console.log("ClawCloud server is disabled. Set CLAW_CLOUD_ENABLED=true in your .env to enable.");
  process.exit(0);
}

// Initialize SQLite Database
const db = new BetterSqlite3(DATABASE_URL);

// Create users table if it doesn't exist
db.exec(`
  CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    stripeCustomerId TEXT,
    plan TEXT DEFAULT 'free',
    quota int DEFAULT 100,
    lastLogin TEXT,
    createdAt TEXT DEFAULT CURRENT_TIMESTAMP
  );
`);

const app = express();
const PORT = process.env.PORT || 3000;

// Security Middlewares
app.use(helmet()); // Basic security headers
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  message: "Too many requests from this IP, please try again after 15 minutes",
  standardHeaders: true, // Return rate limit info in the `RateLimit-*` headers
  legacyHeaders: false, // Disable the `X-RateLimit-*` headers
});
app.use(limiter); // Apply rate limiting to all requests

// Middleware to parse JSON for most routes
app.use((req, res, next) => {
  if (req.originalUrl === '/webhook/stripe') {
    next(); // Skip JSON parsing for Stripe webhook, as it needs raw body
  } else {
    json()(req, res, next);
  }
});

// Zod schemas for validation
const LoginSchema = z.object({
  email: z.string().email(),
  // In a real app, we'd have a password and bcrypt it
});

const TaskSchema = z.object({
  task: z.string().min(5).max(500), // Example task validation
});

// Middleware for JWT authentication
const authenticateJWT = (req: any, res: express.Response, next: express.NextFunction) => {
  const authHeader = req.headers.authorization;

  if (authHeader) {
    const token = authHeader.split(' ')[1]; // Bearer TOKEN

    jwt.verify(token, JWT_SECRET, (err: any, user: any) => {
      if (err) {
        return res.sendStatus(403); // Forbidden
      }
      req.user = user;
      next();
    });
  } else {
    res.sendStatus(401); // Unauthorized
  }
};

// Middleware for quota checking
const checkQuota = (req: any, res: express.Response, next: express.NextFunction) => {
  // This is a simplified check. In a real app, this would be more sophisticated
  // and involve decrementing quota after successful task execution.
  const user = db.prepare('SELECT quota FROM users WHERE id = ?').get(req.user.id);

  if (!user || user.quota <= 0) {
    return res.status(403).json({ message: 'Quota exceeded. Please upgrade your plan.' });
  }
  next();
};

// --- Routes ---

// Public route for user login/registration (simplified)
app.post('/auth/login', (req, res) => {
  const parseResult = LoginSchema.safeParse(req.body);
  if (!parseResult.success) {
    return res.status(400).json({ errors: parseResult.error.errors });
  }

  const { email } = parseResult.data;
  let user = db.prepare('SELECT id, email, quota, plan FROM users WHERE email = ?').get(email);

  if (!user) {
    // Register new user
    const newUser = {
      id: crypto.randomUUID(), // Node.js 16+
      email,
      plan: 'free',
      quota: 100, // Free tier quota
      createdAt: new Date().toISOString(),
    };
    db.prepare('INSERT INTO users (id, email, plan, quota, createdAt) VALUES (?, ?, ?, ?, ?)').run(
      newUser.id, newUser.email, newUser.plan, newUser.quota, newUser.createdAt
    );
    user = newUser;
  }

  // Update last login
  db.prepare('UPDATE users SET lastLogin = ? WHERE id = ?').run(new Date().toISOString(), user.id);

  const token = jwt.sign({ id: user.id, email: user.email, plan: user.plan }, JWT_SECRET, { expiresIn: '1h' });
  res.json({ token, user: { id: user.id, email: user.email, plan: user.plan, quota: user.quota } });
});

// Protected route for agent task execution
app.post('/api/agent/do', authenticateJWT, checkQuota, async (req, res) => {
  const parseResult = TaskSchema.safeParse(req.body);
  if (!parseResult.success) {
    return res.status(400).json({ errors: parseResult.error.errors });
  }
  const { task } = parseResult.data;
  const user = req.user; // From authenticateJWT middleware

  console.log(`[ClawCloud] User ${user.email} (ID: ${user.id}) submitting task: "${task}"`);

  // TODO: Integrate the actual agent logic here.
  // This would involve instantiating and running the 'Agent' from agent-cli/src/agent.ts
  // Ensure the agent execution is isolated and secure for multi-tenancy.
  // The agent would need to be passed a context object with user details and potentially
  // adjusted policies/quotas based on the user's plan.
  try {
    // Simulate agent processing
    await new Promise(resolve => setTimeout(resolve, 2000));
    const simulatedResult = {
      message: `Task "${task}" processed for user ${user.email}. (Agent integration TODO)`,
      status: 'success',
      // In a real scenario, decrement user quota here
    };

    // Decrement quota (simplified example)
    db.prepare('UPDATE users SET quota = quota - 1 WHERE id = ?').run(user.id);

    res.json(simulatedResult);
  } catch (error: any) {
    console.error('Agent execution error:', error);
    res.status(500).json({ message: 'Error processing task.', error: error.message });
  }
});

// Stripe Webhook endpoint
app.post('/webhook/stripe', express.raw({ type: 'application/json' }), (req, res) => {
  const sig = req.headers['stripe-signature'];
  let event;

  try {
    // In a real scenario, use Stripe's library to verify the webhook signature
    // event = stripe.webhooks.constructEvent(req.body, sig, STRIPE_WEBHOOK_SECRET);
    console.log('[Stripe Webhook] Received event:', req.body); // Log raw body for now
    event = JSON.parse(req.body.toString()); // Dummy parse
  } catch (err: any) {
    console.error(`[Stripe Webhook] Webhook Error: ${err.message}`);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Handle the event
  switch (event.type) {
    case 'customer.subscription.created':
    case 'customer.subscription.updated':
      // Update user's plan and quota in database
      console.log(`[Stripe Webhook] Subscription event for ${event.data.object.customer}`);
      break;
    case 'invoice.payment_succeeded':
      // Grant access to paid features
      console.log(`[Stripe Webhook] Payment succeeded for ${event.data.object.customer}`);
      break;
    // ... handle other event types
    default:
      console.log(`[Stripe Webhook] Unhandled event type ${event.type}`);
  }

  res.json({ received: true });
});

// Admin endpoint (basic example, secure with a strong API key)
app.post('/admin/users', (req, res) => {
  const adminKey = req.headers['x-admin-api-key'];
  if (adminKey !== ADMIN_API_KEY) {
    return res.sendStatus(403);
  }
  const users = db.prepare('SELECT id, email, plan, quota FROM users').all();
  res.json(users);
});


// Start the server
app.listen(PORT, () => {
  console.log(`ClawCloud server listening on port ${PORT}`);
  console.log(`ClawCloud server status: ${CLAW_CLOUD_ENABLED ? 'ENABLED' : 'DISABLED'}`);
});

// Graceful shutdown
process.on('SIGINT', () => {
  console.log('Closing database connection.');
  db.close();
  process.exit(0);
});

// TODO:
// - Implement actual agent integration, ensuring multi-tenancy and resource isolation.
// - More robust error handling and logging.
// - Advanced user management (password hashing, MFA).
// - Full Stripe webhook event handling.
// - WebSocket for real-time agent feedback.
// - Detailed quota management and billing integration.
// - Consider a more scalable database for production (PostgreSQL).

```

