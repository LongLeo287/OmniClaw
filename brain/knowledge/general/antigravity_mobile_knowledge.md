# Knowledge Dump for antigravity_mobile

## File: README.md
```
# Antigravity Mobile

**Skill ID:** `antigravity_mobile` | **Domain:** `llm-tooling` | **Tier:** 3

## Summary
Mobile dashboard and admin panel for [Antigravity IDE](https://antigravity.google). Monitor conversations, manage your agent, and get notified — all from your phone.

## Usage
Consult `payload/` for concrete source code and implementation patterns.

```

## File: schema.json
```
{
  "id": "antigravity_mobile",
  "name": "Antigravity Mobile",
  "version": "1.0.0",
  "tier": 3,
  "status": "active",
  "domain": "llm-tooling",
  "cost_tier": "standard",
  "load_on_boot": false,
  "path": "$OMNICLAW_ROOT\\ecosystem\\skills\\antigravity_mobile\\SKILL.md",
  "accessible_by": [
    "Orchestrator",
    "Claude Code"
  ],
  "dependencies": [],
  "exposed_functions": [
    {
      "name": "reference",
      "description": "Reference for antigravity_mobile",
      "input": "string",
      "output": "string"
    }
  ],
  "consumed_by": [],
  "emits_events": [],
  "listens_to": [],
  "tags": [
    "llm",
    "ai"
  ]
}
```

## File: SKILL.md
```
---
id: antigravity_mobile
name: Antigravity Mobile
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: llm-tooling
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Reference knowledge and templates from antigravity_mobile.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["llm", "ai"]
---

# Antigravity Mobile

## Overview
Mobile dashboard and admin panel for [Antigravity IDE](https://antigravity.google). Monitor conversations, manage your agent, and get notified — all from your phone.

## Usage
Agents working on `llm-tooling` tasks should reference this skill.
Inspect `payload/` for concrete source code and implementation patterns.

## Key Capabilities
- Domain: `llm-tooling`
- Source templates available in `payload/`
- Tags: llm, ai

```

## File: _DIR_IDENTITY.md
```
---
id: antigravity_mobile
type: skill
owner: OA Forge Pipeline
registered_at: 2026-04-09
tags: ["llm", "ai", "forge-in-place", "llm-tooling"]
---

# Antigravity Mobile

Forged in-place from raw repository: `antigravity_mobile`
Domain: `llm-tooling`

```

## File: payload\DEEP_KNOWLEDGE.md
```
# Deep Matrix Profile: FETCHED_Antigravity-Mobile_035838

# Deep Knowledge Report for Antigravity Control Dashboard Repository

## Overview

The `Antigravity Control` repository provides a comprehensive mobile dashboard and admin control panel for managing the Antigravity IDE. The system is designed to offer real-time monitoring, remote management, and notification handling of AI agent sessions. It leverages modern web technologies such as Service Workers for offline caching and Progressive Web App (PWA) capabilities.

## Architectural Patterns

### Client-Side Architecture
- **Service Worker (`sw.js`)**: Manages the service worker to handle offline caching and PWA functionalities.
- **JavaScript Frameworks**: Uses vanilla JavaScript with some utility functions and event listeners.
- **State Management**: Utilizes global state variables for managing application state, such as authentication status.

### Server-Side Architecture
- **API Endpoints**: Defined in `api.js` for handling various requests related to authentication, models, chat history, etc.
- **Authentication Mechanism**: Implements a token-based system with an API endpoint for checking and refreshing tokens.

## Core Algorithms

### Service Worker (`sw.js`)
1. **Cache Management**:
   - **Install Event**: Caches static assets during the installation of the service worker.
   - **Activate Event**: Cleans up old cache keys to ensure only the latest version is active.
2. **Fetch Handling**:
   - **Network-First Strategy**: For API calls and HTML pages, it attempts to fetch from the network first; if successful, caches the response for future use.
   - **Cache-First Strategy**: For static assets like images and icons, it serves them directly from cache.

### Authentication Mechanism (`api.js`)
1. **Token-Based Authentication**:
   - Checks for a valid `authToken` in local storage to determine authentication status.
   - Uses the `authFetch` helper function to handle authenticated requests, adding authorization headers as needed.
2. **Authentication Check**:
   - The `checkAuth` function ensures that the user is properly authenticated before proceeding with other operations.

## Primary Mechanisms

### Real-Time Monitoring and Notification Handling
- **WebSocket Connection**: Established via `connectWebSocket()` in `app.js`, enabling real-time updates from the server.
- **Polling for Chat History**: Implemented using `startChatPolling()` to periodically fetch chat history, ensuring up-to-date information.

### Remote Management and Control
- **Cloudflare Tunnels**: Secure remote access is facilitated through Cloudflare tunnels, allowing real-time monitoring and management of AI agent sessions from anywhere.
- **Telegram Bot Integration**: Local control mechanisms include integration with a Telegram bot for additional interaction capabilities.

## Detailed Breakdown

### Service Worker (`sw.js`)
```markdown
- **Install Event**:
  - Caches static assets like HTML files, manifest, icons, etc., ensuring they are available offline.
  
- **Activate Event**:
  - Cleans up old cache keys to ensure only the latest version of the application is active.

- **Fetch Handling**:
  - For API calls and HTML pages: Network-first strategy with caching for subsequent requests.
  - For static assets: Cache-first strategy, serving from cache if available.
```

### Authentication Mechanism (`api.js`)
```markdown
- **Token-Based Authentication**:
  - Checks `authToken` in local storage to determine authentication status.
  - Uses `authFetch` helper function to handle authenticated requests, adding authorization headers as needed.

- **Authentication Check**:
  - The `checkAuth` function ensures the user is properly authenticated before proceeding with other operations.
```

### Real-Time Monitoring and Notification Handling
```markdown
- **WebSocket Connection**:
  - Established via `connectWebSocket()` in `app.js`, enabling real-time updates from the server.

- **Polling for Chat History**:
  - Implemented using `startChatPolling()` to periodically fetch chat history, ensuring up-to-date information.
```

### Remote Management and Control
```markdown
- **Cloudflare Tunnels**:
  - Secure remote access is facilitated through Cloudflare tunnels, allowing real-time monitoring and management of AI agent sessions from anywhere.

- **Telegram Bot Integration**:
  - Local control mechanisms include integration with a Telegram bot for additional interaction capabilities.
```

## Conclusion

The `Antigravity Control` repository employs robust architectural patterns and core algorithms to provide a comprehensive dashboard for managing the Antigravity IDE. The use of Service Workers ensures offline functionality, while advanced authentication and real-time monitoring mechanisms enhance user experience and security.

This report provides an in-depth understanding of the system's architecture, enabling further development or maintenance efforts.
```

## File: payload\package-lock.json
```
{
  "name": "antigravity-mobile",
  "version": "2.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "antigravity-mobile",
      "version": "2.0.0",
      "license": "MIT",
      "dependencies": {
        "express": "^4.18.2",
        "multer": "^1.4.5-lts.1",
        "node-telegram-bot-api": "^0.66.0",
        "sql.js": "^1.13.0",
        "ws": "^8.16.0"
      }
    },
    "node_modules/@cypress/request": {
      "version": "3.0.10",
      "resolved": "https://registry.npmjs.org/@cypress/request/-/request-3.0.10.tgz",
      "integrity": "sha512-hauBrOdvu08vOsagkZ/Aju5XuiZx6ldsLfByg1htFeldhex+PeMrYauANzFsMJeAA0+dyPLbDoX2OYuvVoLDkQ==",
      "license": "Apache-2.0",
      "peer": true,
      "dependencies": {
        "aws-sign2": "~0.7.0",
        "aws4": "^1.8.0",
        "caseless": "~0.12.0",
        "combined-stream": "~1.0.6",
        "extend": "~3.0.2",
        "forever-agent": "~0.6.1",
        "form-data": "~4.0.4",
        "http-signature": "~1.4.0",
        "is-typedarray": "~1.0.0",
        "isstream": "~0.1.2",
        "json-stringify-safe": "~5.0.1",
        "mime-types": "~2.1.19",
        "performance-now": "^2.1.0",
        "qs": "~6.14.1",
        "safe-buffer": "^5.1.2",
        "tough-cookie": "^5.0.0",
        "tunnel-agent": "^0.6.0",
        "uuid": "^8.3.2"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/@cypress/request-promise": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/@cypress/request-promise/-/request-promise-5.0.0.tgz",
      "integrity": "sha512-eKdYVpa9cBEw2kTBlHeu1PP16Blwtum6QHg/u9s/MoHkZfuo1pRGka1VlUHXF5kdew82BvOJVVGk0x8X0nbp+w==",
      "license": "ISC",
      "dependencies": {
        "bluebird": "^3.5.0",
        "request-promise-core": "1.1.3",
        "stealthy-require": "^1.1.1",
        "tough-cookie": "^4.1.3"
      },
      "engines": {
        "node": ">=0.10.0"
      },
      "peerDependencies": {
        "@cypress/request": "^3.0.0"
      }
    },
    "node_modules/@cypress/request-promise/node_modules/tough-cookie": {
      "version": "4.1.4",
      "resolved": "https://registry.npmjs.org/tough-cookie/-/tough-cookie-4.1.4.tgz",
      "integrity": "sha512-Loo5UUvLD9ScZ6jh8beX1T6sO1w2/MpCRpEP7V280GKMVUQ0Jzar2U3UJPsrdbziLEMMhu3Ujnq//rhiFuIeag==",
      "license": "BSD-3-Clause",
      "dependencies": {
        "psl": "^1.1.33",
        "punycode": "^2.1.1",
        "universalify": "^0.2.0",
        "url-parse": "^1.5.3"
      },
      "engines": {
        "node": ">=6"
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
    "node_modules/ajv": {
      "version": "6.14.0",
      "resolved": "https://registry.npmjs.org/ajv/-/ajv-6.14.0.tgz",
      "integrity": "sha512-IWrosm/yrn43eiKqkfkHis7QioDleaXQHdDVPKg0FSwwd/DuvyX79TZnFOnYpB7dcsFAMmtFztZuXPDvSePkFw==",
      "license": "MIT",
      "dependencies": {
        "fast-deep-equal": "^3.1.1",
        "fast-json-stable-stringify": "^2.0.0",
        "json-schema-traverse": "^0.4.1",
        "uri-js": "^4.2.2"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/epoberezkin"
      }
    },
    "node_modules/append-field": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/append-field/-/append-field-1.0.0.tgz",
      "integrity": "sha512-klpgFSWLW1ZEs8svjfb7g4qWY0YS5imI82dTg+QahUvJ8YqAY0P10Uk8tTyh9ZGuYEZEMaeJYCF5BFuX552hsw==",
      "license": "MIT"
    },
    "node_modules/array-buffer-byte-length": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/array-buffer-byte-length/-/array-buffer-byte-length-1.0.2.tgz",
      "integrity": "sha512-LHE+8BuR7RYGDKvnrmcuSq3tDcKv9OFEXQt/HpbZhY7V6h0zlUXutnAD82GiFx9rdieCMjkvtcsPqBwgUl1Iiw==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3",
        "is-array-buffer": "^3.0.5"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/array-flatten": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/array-flatten/-/array-flatten-1.1.1.tgz",
      "integrity": "sha512-PCVAQswWemu6UdxsDFFX/+gVeYqKAod3D3UVm91jHwynguOwAvYPhx8nNlM++NqRcK6CxxpUafjmhIdKiHibqg==",
      "license": "MIT"
    },
    "node_modules/array.prototype.findindex": {
      "version": "2.2.4",
      "resolved": "https://registry.npmjs.org/array.prototype.findindex/-/array.prototype.findindex-2.2.4.tgz",
      "integrity": "sha512-LLm4mhxa9v8j0A/RPnpQAP4svXToJFh+Hp1pNYl5ZD5qpB4zdx/D4YjpVcETkhFbUKWO3iGMVLvrOnnmkAJT6A==",
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.8",
        "call-bound": "^1.0.3",
        "define-properties": "^1.2.1",
        "es-abstract": "^1.23.6",
        "es-object-atoms": "^1.0.0",
        "es-shim-unscopables": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/arraybuffer.prototype.slice": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/arraybuffer.prototype.slice/-/arraybuffer.prototype.slice-1.0.4.tgz",
      "integrity": "sha512-BNoCY6SXXPQ7gF2opIP4GBE+Xw7U+pHMYKuzjgCN3GwiaIR09UUeKfheyIry77QtrCBlC0KK0q5/TER/tYh3PQ==",
      "license": "MIT",
      "dependencies": {
        "array-buffer-byte-length": "^1.0.1",
        "call-bind": "^1.0.8",
        "define-properties": "^1.2.1",
        "es-abstract": "^1.23.5",
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.6",
        "is-array-buffer": "^3.0.4"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/asn1": {
      "version": "0.2.6",
      "resolved": "https://registry.npmjs.org/asn1/-/asn1-0.2.6.tgz",
      "integrity": "sha512-ix/FxPn0MDjeyJ7i/yoHGFt/EX6LyNbxSEhPPXODPL+KB0VPk86UYfL0lMdy+KCnv+fmvIzySwaK5COwqVbWTQ==",
      "license": "MIT",
      "dependencies": {
        "safer-buffer": "~2.1.0"
      }
    },
    "node_modules/assert-plus": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz",
      "integrity": "sha512-NfJ4UzBCcQGLDlQq7nHxH+tv3kyZ0hHQqF5BO6J7tNJeP5do1llPr8dZ8zHonfhAu0PHAdMkSo+8o0wxg9lZWw==",
      "license": "MIT",
      "engines": {
        "node": ">=0.8"
      }
    },
    "node_modules/async-function": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/async-function/-/async-function-1.0.0.tgz",
      "integrity": "sha512-hsU18Ae8CDTR6Kgu9DYf0EbCr/a5iGL0rytQDobUcdpYOKokk8LEjVphnXkDkgpi0wYVsqrXuP0bZxJaTqdgoA==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/asynckit": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz",
      "integrity": "sha512-Oei9OH4tRh0YqU3GxhX79dM/mwVgvbZJaSNaRk+bshkj0S5cfHcgYakreBjrHwatXKbz+IoIdYLxrKim2MjW0Q==",
      "license": "MIT"
    },
    "node_modules/available-typed-arrays": {
      "version": "1.0.7",
      "resolved": "https://registry.npmjs.org/available-typed-arrays/-/available-typed-arrays-1.0.7.tgz",
      "integrity": "sha512-wvUjBtSGN7+7SjNpq/9M2Tg350UZD3q62IFZLbRAR1bSMlCo1ZaeW+BJ+D090e4hIIZLBcTDWe4Mh4jvUDajzQ==",
      "license": "MIT",
      "dependencies": {
        "possible-typed-array-names": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/aws-sign2": {
      "version": "0.7.0",
      "resolved": "https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz",
      "integrity": "sha512-08kcGqnYf/YmjoRhfxyu+CLxBjUtHLXLXX/vUfx9l2LYzG3c1m61nrpyFUZI6zeS+Li/wWMMidD9KgrqtGq3mA==",
      "license": "Apache-2.0",
      "engines": {
        "node": "*"
      }
    },
    "node_modules/aws4": {
      "version": "1.13.2",
      "resolved": "https://registry.npmjs.org/aws4/-/aws4-1.13.2.tgz",
      "integrity": "sha512-lHe62zvbTB5eEABUVi/AwVh0ZKY9rMMDhmm+eeyuuUQbQ3+J+fONVQOZyj+DdrvD4BY33uYniyRJ4UJIaSKAfw==",
      "license": "MIT"
    },
    "node_modules/bcrypt-pbkdf": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.2.tgz",
      "integrity": "sha512-qeFIXtP4MSoi6NLqO12WfqARWWuCKi2Rn/9hJLEmtB5yTNr9DqFWkJRCf2qShWzPeAMRnOgCrq0sg/KLv5ES9w==",
      "license": "BSD-3-Clause",
      "dependencies": {
        "tweetnacl": "^0.14.3"
      }
    },
    "node_modules/bl": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/bl/-/bl-1.2.3.tgz",
      "integrity": "sha512-pvcNpa0UU69UT341rO6AYy4FVAIkUHuZXRIWbq+zHnsVcRzDDjIAhGuuYoi0d//cwIwtt4pkpKycWEfjdV+vww==",
      "license": "MIT",
      "dependencies": {
        "readable-stream": "^2.3.5",
        "safe-buffer": "^5.1.1"
      }
    },
    "node_modules/bluebird": {
      "version": "3.7.2",
      "resolved": "https://registry.npmjs.org/bluebird/-/bluebird-3.7.2.tgz",
      "integrity": "sha512-XpNj6GDQzdfW+r2Wnn7xiSAd7TM3jzkxGXBGTtWKuSXv1xUV+azxAm8jdWZN06QTQk+2N2XB9jRDkvbmQmcRtg==",
      "license": "MIT"
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
    "node_modules/buffer-from": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.2.tgz",
      "integrity": "sha512-E+XQCRwSbaaiChtv6k6Dwgc+bx+Bs6vuKJHHl5kox/BaKbhiXzqQOwK4cO22yElGp2OCmjwVhT3HmxgyPGnJfQ==",
      "license": "MIT"
    },
    "node_modules/busboy": {
      "version": "1.6.0",
      "resolved": "https://registry.npmjs.org/busboy/-/busboy-1.6.0.tgz",
      "integrity": "sha512-8SFQbg/0hQ9xy3UNTB0YEnsNBbWfhf7RtnzpL7TkBiTBRfrQ9Fxcnz7VJsleJpyp6rVLvXiuORqjlHi5q+PYuA==",
      "dependencies": {
        "streamsearch": "^1.1.0"
      },
      "engines": {
        "node": ">=10.16.0"
      }
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
    "node_modules/call-bind": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/call-bind/-/call-bind-1.0.8.tgz",
      "integrity": "sha512-oKlSFMcMwpUg2ednkhQ454wfWiU/ul3CkJe/PEHcTKuiX6RpbehUiFMXu13HalGZxfUwCQzZG747YXBn1im9ww==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.0",
        "es-define-property": "^1.0.0",
        "get-intrinsic": "^1.2.4",
        "set-function-length": "^1.2.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
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
    "node_modules/caseless": {
      "version": "0.12.0",
      "resolved": "https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz",
      "integrity": "sha512-4tYFyifaFfGacoiObjJegolkwSU4xQNGbVgUiNYVUxbQ2x2lUsFvY4hVgVzGiIe6WLOPqycWXA40l+PWsxthUw==",
      "license": "Apache-2.0"
    },
    "node_modules/combined-stream": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz",
      "integrity": "sha512-FQN4MRfuJeHf7cBbBMJFXhKSDq+2kAArBlmRBvcvFE5BB1HZKXtSFASDhdlz9zOYwxh8lDdnvmMOe/+5cdoEdg==",
      "license": "MIT",
      "dependencies": {
        "delayed-stream": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/concat-stream": {
      "version": "1.6.2",
      "resolved": "https://registry.npmjs.org/concat-stream/-/concat-stream-1.6.2.tgz",
      "integrity": "sha512-27HBghJxjiZtIk3Ycvn/4kbJk/1uZuJFfuPEns6LaEvpvG1f0hTea8lilrouyo9mVc2GWdcEZ8OLoGmSADlrCw==",
      "engines": [
        "node >= 0.8"
      ],
      "license": "MIT",
      "dependencies": {
        "buffer-from": "^1.0.0",
        "inherits": "^2.0.3",
        "readable-stream": "^2.2.2",
        "typedarray": "^0.0.6"
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
    "node_modules/core-util-is": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.3.tgz",
      "integrity": "sha512-ZQBvi1DcpJ4GDqanjucZ2Hj3wEO5pZDS89BWbkcrvdxksJorwUDDZamX9ldFkp9aw2lmBDLgkObEA4DWNJ9FYQ==",
      "license": "MIT"
    },
    "node_modules/dashdash": {
      "version": "1.14.1",
      "resolved": "https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz",
      "integrity": "sha512-jRFi8UDGo6j+odZiEpjazZaWqEal3w/basFjQHQEwVtZJGDpxbH1MeYluwCS8Xq5wmLJooDlMgvVarmWfGM44g==",
      "license": "MIT",
      "dependencies": {
        "assert-plus": "^1.0.0"
      },
      "engines": {
        "node": ">=0.10"
      }
    },
    "node_modules/data-view-buffer": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/data-view-buffer/-/data-view-buffer-1.0.2.tgz",
      "integrity": "sha512-EmKO5V3OLXh1rtK2wgXRansaK1/mtVdTUEiEI0W8RkvgT05kfxaH29PliLnpLP73yYO6142Q72QNa8Wx/A5CqQ==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3",
        "es-errors": "^1.3.0",
        "is-data-view": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/data-view-byte-length": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/data-view-byte-length/-/data-view-byte-length-1.0.2.tgz",
      "integrity": "sha512-tuhGbE6CfTM9+5ANGf+oQb72Ky/0+s3xKUpHvShfiz2RxMFgFPjsXuRLBVMtvMs15awe45SRb83D6wH4ew6wlQ==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3",
        "es-errors": "^1.3.0",
        "is-data-view": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/inspect-js"
      }
    },
    "node_modules/data-view-byte-offset": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/data-view-byte-offset/-/data-view-byte-offset-1.0.1.tgz",
      "integrity": "sha512-BS8PfmtDGnrgYdOonGZQdLZslWIeCGFP9tpan0hi1Co2Zr2NKADsvGYA8XxuG/4UWgJ6Cjtv+YJnB6MM69QGlQ==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "es-errors": "^1.3.0",
        "is-data-view": "^1.0.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
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
    "node_modules/define-data-property": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/define-data-property/-/define-data-property-1.1.4.tgz",
      "integrity": "sha512-rBMvIzlpA8v6E+SJZoo++HAYqsLrkg7MSfIinMPFhmkorw7X+dOXVJQs+QT69zGkzMyfDnIMN2Wid1+NbL3T+A==",
      "license": "MIT",
      "dependencies": {
        "es-define-property": "^1.0.0",
        "es-errors": "^1.3.0",
        "gopd": "^1.0.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/define-properties": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/define-properties/-/define-properties-1.2.1.tgz",
      "integrity": "sha512-8QmQKqEASLd5nx0U1B1okLElbUuuttJ/AnYmRXbbbGDWh6uS208EjD4Xqq/I9wK7u0v6O08XhTWnt5XtEbR6Dg==",
      "license": "MIT",
      "dependencies": {
        "define-data-property": "^1.0.1",
        "has-property-descriptors": "^1.0.0",
        "object-keys": "^1.1.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/delayed-stream": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz",
      "integrity": "sha512-ZySD7Nf91aLB0RxL4KGrKHBXl7Eds1DAmEdcoVawXnLD7SDhpNgtuII2aAkg7a7QS41jxPSZ17p4VdGnMHk3MQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.4.0"
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
    "node_modules/ecc-jsbn": {
      "version": "0.1.2",
      "resolved": "https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.2.tgz",
      "integrity": "sha512-eh9O+hwRHNbG4BLTjEl3nw044CkGm5X6LoaCf7LPp7UU8Qrt47JYNi6nPX8xjW97TKGKm1ouctg0QSpZe9qrnw==",
      "license": "MIT",
      "dependencies": {
        "jsbn": "~0.1.0",
        "safer-buffer": "^2.1.0"
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
    "node_modules/es-abstract": {
      "version": "1.24.1",
      "resolved": "https://registry.npmjs.org/es-abstract/-/es-abstract-1.24.1.tgz",
      "integrity": "sha512-zHXBLhP+QehSSbsS9Pt23Gg964240DPd6QCf8WpkqEXxQ7fhdZzYsocOr5u7apWonsS5EjZDmTF+/slGMyasvw==",
      "license": "MIT",
      "dependencies": {
        "array-buffer-byte-length": "^1.0.2",
        "arraybuffer.prototype.slice": "^1.0.4",
        "available-typed-arrays": "^1.0.7",
        "call-bind": "^1.0.8",
        "call-bound": "^1.0.4",
        "data-view-buffer": "^1.0.2",
        "data-view-byte-length": "^1.0.2",
        "data-view-byte-offset": "^1.0.1",
        "es-define-property": "^1.0.1",
        "es-errors": "^1.3.0",
        "es-object-atoms": "^1.1.1",
        "es-set-tostringtag": "^2.1.0",
        "es-to-primitive": "^1.3.0",
        "function.prototype.name": "^1.1.8",
        "get-intrinsic": "^1.3.0",
        "get-proto": "^1.0.1",
        "get-symbol-description": "^1.1.0",
        "globalthis": "^1.0.4",
        "gopd": "^1.2.0",
        "has-property-descriptors": "^1.0.2",
        "has-proto": "^1.2.0",
        "has-symbols": "^1.1.0",
        "hasown": "^2.0.2",
        "internal-slot": "^1.1.0",
        "is-array-buffer": "^3.0.5",
        "is-callable": "^1.2.7",
        "is-data-view": "^1.0.2",
        "is-negative-zero": "^2.0.3",
        "is-regex": "^1.2.1",
        "is-set": "^2.0.3",
        "is-shared-array-buffer": "^1.0.4",
        "is-string": "^1.1.1",
        "is-typed-array": "^1.1.15",
        "is-weakref": "^1.1.1",
        "math-intrinsics": "^1.1.0",
        "object-inspect": "^1.13.4",
        "object-keys": "^1.1.1",
        "object.assign": "^4.1.7",
        "own-keys": "^1.0.1",
        "regexp.prototype.flags": "^1.5.4",
        "safe-array-concat": "^1.1.3",
        "safe-push-apply": "^1.0.0",
        "safe-regex-test": "^1.1.0",
        "set-proto": "^1.0.0",
        "stop-iteration-iterator": "^1.1.0",
        "string.prototype.trim": "^1.2.10",
        "string.prototype.trimend": "^1.0.9",
        "string.prototype.trimstart": "^1.0.8",
        "typed-array-buffer": "^1.0.3",
        "typed-array-byte-length": "^1.0.3",
        "typed-array-byte-offset": "^1.0.4",
        "typed-array-length": "^1.0.7",
        "unbox-primitive": "^1.1.0",
        "which-typed-array": "^1.1.19"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
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
    "node_modules/es-set-tostringtag": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/es-set-tostringtag/-/es-set-tostringtag-2.1.0.tgz",
      "integrity": "sha512-j6vWzfrGVfyXxge+O0x5sh6cvxAog0a/4Rdd2K36zCMV5eJ+/+tOAngRO8cODMNWbVRdVlmGZQL2YS3yR8bIUA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.6",
        "has-tostringtag": "^1.0.2",
        "hasown": "^2.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-shim-unscopables": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/es-shim-unscopables/-/es-shim-unscopables-1.1.0.tgz",
      "integrity": "sha512-d9T8ucsEhh8Bi1woXCf+TIKDIROLG5WCkxg8geBCbvk22kzwC5G2OnXVMO6FUsvQlgUUXQ2itephWDLqDzbeCw==",
      "license": "MIT",
      "dependencies": {
        "hasown": "^2.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-to-primitive": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/es-to-primitive/-/es-to-primitive-1.3.0.tgz",
      "integrity": "sha512-w+5mJ3GuFL+NjVtJlvydShqE1eN3h3PbI7/5LAsYJP/2qtuMXjfL2LpHSRqo4b4eSF5K/DH1JXKUAHSB2UW50g==",
      "license": "MIT",
      "dependencies": {
        "is-callable": "^1.2.7",
        "is-date-object": "^1.0.5",
        "is-symbol": "^1.0.4"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
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
    "node_modules/eventemitter3": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/eventemitter3/-/eventemitter3-3.1.2.tgz",
      "integrity": "sha512-tvtQIeLVHjDkJYnzf2dgVMxfuSGJeM/7UCG17TT4EumTfNtF+0nebF/4zWOIkCreAbtNqhGEboB6BWrwqNaw4Q==",
      "license": "MIT"
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
    "node_modules/extend": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/extend/-/extend-3.0.2.tgz",
      "integrity": "sha512-fjquC59cD7CyW6urNXK0FBufkZcoiGG80wTuPujX590cB5Ttln20E2UB4S/WARVqhXffZl2LNgS+gQdPIIim/g==",
      "license": "MIT"
    },
    "node_modules/extsprintf": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz",
      "integrity": "sha512-11Ndz7Nv+mvAC1j0ktTa7fAb0vLyGGX+rMHNBYQviQDGU0Hw7lhctJANqbPhu9nV9/izT/IntTgZ7Im/9LJs9g==",
      "engines": [
        "node >=0.6.0"
      ],
      "license": "MIT"
    },
    "node_modules/fast-deep-equal": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz",
      "integrity": "sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==",
      "license": "MIT"
    },
    "node_modules/fast-json-stable-stringify": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz",
      "integrity": "sha512-lhd/wF+Lk98HZoTCtlVraHtfh5XYijIjalXck7saUtuanSDyLMxnHhSXEDJqHxD7msR8D0uCmqlkwjCV8xvwHw==",
      "license": "MIT"
    },
    "node_modules/file-type": {
      "version": "3.9.0",
      "resolved": "https://registry.npmjs.org/file-type/-/file-type-3.9.0.tgz",
      "integrity": "sha512-RLoqTXE8/vPmMuTI88DAzhMYC99I8BWv7zYP4A1puo5HIjEJ5EX48ighy4ZyKMG9EDXxBgW6e++cn7d1xuFghA==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
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
    "node_modules/for-each": {
      "version": "0.3.5",
      "resolved": "https://registry.npmjs.org/for-each/-/for-each-0.3.5.tgz",
      "integrity": "sha512-dKx12eRCVIzqCxFGplyFKJMPvLEWgmNtUrpTiJIR5u97zEhRG8ySrtboPHZXx7daLxQVrl643cTzbab2tkQjxg==",
      "license": "MIT",
      "dependencies": {
        "is-callable": "^1.2.7"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/forever-agent": {
      "version": "0.6.1",
      "resolved": "https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz",
      "integrity": "sha512-j0KLYPhm6zeac4lz3oJ3o65qvgQCcPubiyotZrXqEaG4hNagNYO8qdlUrX5vwqv9ohqeT/Z3j6+yW067yWWdUw==",
      "license": "Apache-2.0",
      "engines": {
        "node": "*"
      }
    },
    "node_modules/form-data": {
      "version": "4.0.5",
      "resolved": "https://registry.npmjs.org/form-data/-/form-data-4.0.5.tgz",
      "integrity": "sha512-8RipRLol37bNs2bhoV67fiTEvdTrbMUYcFTiy3+wuuOnUog2QBHCZWXDRijWQfAkhBj2Uf5UnVaiWwA5vdd82w==",
      "license": "MIT",
      "dependencies": {
        "asynckit": "^0.4.0",
        "combined-stream": "^1.0.8",
        "es-set-tostringtag": "^2.1.0",
        "hasown": "^2.0.2",
        "mime-types": "^2.1.12"
      },
      "engines": {
        "node": ">= 6"
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
    "node_modules/function-bind": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
      "integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/function.prototype.name": {
      "version": "1.1.8",
      "resolved": "https://registry.npmjs.org/function.prototype.name/-/function.prototype.name-1.1.8.tgz",
      "integrity": "sha512-e5iwyodOHhbMr/yNrc7fDYG4qlbIvI5gajyzPnb5TCwyhjApznQh1BMFou9b30SevY43gCJKXycoCBjMbsuW0Q==",
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.8",
        "call-bound": "^1.0.3",
        "define-properties": "^1.2.1",
        "functions-have-names": "^1.2.3",
        "hasown": "^2.0.2",
        "is-callable": "^1.2.7"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/functions-have-names": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/functions-have-names/-/functions-have-names-1.2.3.tgz",
      "integrity": "sha512-xckBUXyTIqT97tq2x2AMb+g163b5JFysYk0x4qxNFwbfQkmNZoiRHb6sPzI9/QV33WeuvVYBUIiD4NzNIyqaRQ==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/generator-function": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/generator-function/-/generator-function-2.0.1.tgz",
      "integrity": "sha512-SFdFmIJi+ybC0vjlHN0ZGVGHc3lgE0DxPAT0djjVg+kjOnSqclqmj0KQ7ykTOLP6YxoqOvuAODGdcHJn+43q3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
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
    "node_modules/get-symbol-description": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/get-symbol-description/-/get-symbol-description-1.1.0.tgz",
      "integrity": "sha512-w9UMqWwJxHNOvoNzSJ2oPF5wvYcvP7jUvYzhp67yEhTi17ZDBBC1z9pTdGuzjD+EFIqLSYRweZjqfiPzQ06Ebg==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3",
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.6"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/getpass": {
      "version": "0.1.7",
      "resolved": "https://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz",
      "integrity": "sha512-0fzj9JxOLfJ+XGLhR8ze3unN0KZCgZwiSSDz168VERjK8Wl8kVSdcu2kspd4s4wtAa1y/qrVRiAA0WclVsu0ng==",
      "license": "MIT",
      "dependencies": {
        "assert-plus": "^1.0.0"
      }
    },
    "node_modules/globalthis": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/globalthis/-/globalthis-1.0.4.tgz",
      "integrity": "sha512-DpLKbNU4WylpxJykQujfCcwYWiV/Jhm50Goo0wrVILAv5jOr9d+H+UR3PhSCD2rCCEIg0uc+G+muBTwD54JhDQ==",
      "license": "MIT",
      "dependencies": {
        "define-properties": "^1.2.1",
        "gopd": "^1.0.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
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
    "node_modules/har-schema": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/har-schema/-/har-schema-2.0.0.tgz",
      "integrity": "sha512-Oqluz6zhGX8cyRaTQlFMPw80bSJVG2x/cFb8ZPhUILGgHka9SsokCCOQgpveePerqidZOrT14ipqfJb7ILcW5Q==",
      "license": "ISC",
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/har-validator": {
      "version": "5.1.5",
      "resolved": "https://registry.npmjs.org/har-validator/-/har-validator-5.1.5.tgz",
      "integrity": "sha512-nmT2T0lljbxdQZfspsno9hgrG3Uir6Ks5afism62poxqBM6sDnMEuPmzTq8XN0OEwqKLLdh1jQI3qyE66Nzb3w==",
      "deprecated": "this library is no longer supported",
      "license": "MIT",
      "dependencies": {
        "ajv": "^6.12.3",
        "har-schema": "^2.0.0"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/has-bigints": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/has-bigints/-/has-bigints-1.1.0.tgz",
      "integrity": "sha512-R3pbpkcIqv2Pm3dUwgjclDRVmWpTJW2DcMzcIhEXEx1oh/CEMObMm3KLmRJOdvhM7o4uQBnwr8pzRK2sJWIqfg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-property-descriptors": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/has-property-descriptors/-/has-property-descriptors-1.0.2.tgz",
      "integrity": "sha512-55JNKuIW+vq4Ke1BjOTjM2YctQIvCT7GFzHwmfZPGo5wnrgkid0YQtnAleFSqumZm4az3n2BS+erby5ipJdgrg==",
      "license": "MIT",
      "dependencies": {
        "es-define-property": "^1.0.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-proto": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/has-proto/-/has-proto-1.2.0.tgz",
      "integrity": "sha512-KIL7eQPfHQRC8+XluaIw7BHUwwqL19bQn4hzNgdr+1wXoU0KKj6rufu47lhY7KbJR2C6T6+PfyN0Ea7wkSS+qQ==",
      "license": "MIT",
      "dependencies": {
        "dunder-proto": "^1.0.0"
      },
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
    "node_modules/has-tostringtag": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/has-tostringtag/-/has-tostringtag-1.0.2.tgz",
      "integrity": "sha512-NqADB8VjPFLM2V0VvHUewwwsw0ZWBaIdgo+ieHtK3hasLz4qeCRjYcqfB6AQrBggRKppKF8L52/VqdVsO47Dlw==",
      "license": "MIT",
      "dependencies": {
        "has-symbols": "^1.0.3"
      },
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
    "node_modules/http-signature": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/http-signature/-/http-signature-1.4.0.tgz",
      "integrity": "sha512-G5akfn7eKbpDN+8nPS/cb57YeA1jLTVxjpCj7tmm3QKPdyDy7T+qSC40e9ptydSWvkwjSXw1VbkpyEm39ukeAg==",
      "license": "MIT",
      "dependencies": {
        "assert-plus": "^1.0.0",
        "jsprim": "^2.0.2",
        "sshpk": "^1.18.0"
      },
      "engines": {
        "node": ">=0.10"
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
    "node_modules/inherits": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
      "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==",
      "license": "ISC"
    },
    "node_modules/internal-slot": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/internal-slot/-/internal-slot-1.1.0.tgz",
      "integrity": "sha512-4gd7VpWNQNB4UKKCFFVcp1AVv+FMOgs9NKzjHKusc8jTMhd5eL1NqQqOpE0KzMds804/yHlglp3uxgluOqAPLw==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "hasown": "^2.0.2",
        "side-channel": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
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
    "node_modules/is-array-buffer": {
      "version": "3.0.5",
      "resolved": "https://registry.npmjs.org/is-array-buffer/-/is-array-buffer-3.0.5.tgz",
      "integrity": "sha512-DDfANUiiG2wC1qawP66qlTugJeL5HyzMpfr8lLK+jMQirGzNod0B12cFB/9q838Ru27sBwfw78/rdoU7RERz6A==",
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.8",
        "call-bound": "^1.0.3",
        "get-intrinsic": "^1.2.6"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-async-function": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-async-function/-/is-async-function-2.1.1.tgz",
      "integrity": "sha512-9dgM/cZBnNvjzaMYHVoxxfPj2QXt22Ev7SuuPrs+xav0ukGB0S6d4ydZdEiM48kLx5kDV+QBPrpVnFyefL8kkQ==",
      "license": "MIT",
      "dependencies": {
        "async-function": "^1.0.0",
        "call-bound": "^1.0.3",
        "get-proto": "^1.0.1",
        "has-tostringtag": "^1.0.2",
        "safe-regex-test": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-bigint": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/is-bigint/-/is-bigint-1.1.0.tgz",
      "integrity": "sha512-n4ZT37wG78iz03xPRKJrHTdZbe3IicyucEtdRsV5yglwc3GyUfbAfpSeD0FJ41NbUNSt5wbhqfp1fS+BgnvDFQ==",
      "license": "MIT",
      "dependencies": {
        "has-bigints": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-boolean-object": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/is-boolean-object/-/is-boolean-object-1.2.2.tgz",
      "integrity": "sha512-wa56o2/ElJMYqjCjGkXri7it5FbebW5usLw/nPmCMs5DeZ7eziSYZhSmPRn0txqeW4LnAmQQU7FgqLpsEFKM4A==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3",
        "has-tostringtag": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-callable": {
      "version": "1.2.7",
      "resolved": "https://registry.npmjs.org/is-callable/-/is-callable-1.2.7.tgz",
      "integrity": "sha512-1BC0BVFhS/p0qtw6enp8e+8OD0UrK0oFLztSjNzhcKA3WDuJxxAPXzPuPtKkjEY9UUoEWlX/8fgKeu2S8i9JTA==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-data-view": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/is-data-view/-/is-data-view-1.0.2.tgz",
      "integrity": "sha512-RKtWF8pGmS87i2D6gqQu/l7EYRlVdfzemCJN/P3UOs//x1QE7mfhvzHIApBTRf7axvT6DMGwSwBXYCT0nfB9xw==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "get-intrinsic": "^1.2.6",
        "is-typed-array": "^1.1.13"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-date-object": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/is-date-object/-/is-date-object-1.1.0.tgz",
      "integrity": "sha512-PwwhEakHVKTdRNVOw+/Gyh0+MzlCl4R6qKvkhuvLtPMggI1WAHt9sOwZxQLSGpUaDnrdyDsomoRgNnCfKNSXXg==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "has-tostringtag": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-finalizationregistry": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/is-finalizationregistry/-/is-finalizationregistry-1.1.1.tgz",
      "integrity": "sha512-1pC6N8qWJbWoPtEjgcL2xyhQOP491EQjeUo3qTKcmV8YSDDJrOepfG8pcC7h/QgnQHYSv0mJ3Z/ZWxmatVrysg==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-generator-function": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/is-generator-function/-/is-generator-function-1.1.2.tgz",
      "integrity": "sha512-upqt1SkGkODW9tsGNG5mtXTXtECizwtS2kA161M+gJPc1xdb/Ax629af6YrTwcOeQHbewrPNlE5Dx7kzvXTizA==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.4",
        "generator-function": "^2.0.0",
        "get-proto": "^1.0.1",
        "has-tostringtag": "^1.0.2",
        "safe-regex-test": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-map": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/is-map/-/is-map-2.0.3.tgz",
      "integrity": "sha512-1Qed0/Hr2m+YqxnM09CjA2d/i6YZNfF6R2oRAOj36eUdS6qIV/huPJNSEpKbupewFs+ZsJlxsjjPbc0/afW6Lw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-negative-zero": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/is-negative-zero/-/is-negative-zero-2.0.3.tgz",
      "integrity": "sha512-5KoIu2Ngpyek75jXodFvnafB6DJgr3u8uuK0LEZJjrU19DrMD3EVERaR8sjz8CCGgpZvxPl9SuE1GMVPFHx1mw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-number-object": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/is-number-object/-/is-number-object-1.1.1.tgz",
      "integrity": "sha512-lZhclumE1G6VYD8VHe35wFaIif+CTy5SJIi5+3y4psDgWu4wPDoBhF8NxUOinEc7pHgiTsT6MaBb92rKhhD+Xw==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3",
        "has-tostringtag": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-regex": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/is-regex/-/is-regex-1.2.1.tgz",
      "integrity": "sha512-MjYsKHO5O7mCsmRGxWcLWheFqN9DJ/2TmngvjKXihe6efViPqc274+Fx/4fYj/r03+ESvBdTXK0V6tA3rgez1g==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "gopd": "^1.2.0",
        "has-tostringtag": "^1.0.2",
        "hasown": "^2.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-set": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/is-set/-/is-set-2.0.3.tgz",
      "integrity": "sha512-iPAjerrse27/ygGLxw+EBR9agv9Y6uLeYVJMu+QNCoouJ1/1ri0mGrcWpfCqFZuzzx3WjtwxG098X+n4OuRkPg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-shared-array-buffer": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/is-shared-array-buffer/-/is-shared-array-buffer-1.0.4.tgz",
      "integrity": "sha512-ISWac8drv4ZGfwKl5slpHG9OwPNty4jOWPRIhBpxOoD+hqITiwuipOQ2bNthAzwA3B4fIjO4Nln74N0S9byq8A==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-string": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/is-string/-/is-string-1.1.1.tgz",
      "integrity": "sha512-BtEeSsoaQjlSPBemMQIrY1MY0uM6vnS1g5fmufYOtnxLGUZM2178PKbhsk7Ffv58IX+ZtcvoGwccYsh0PglkAA==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3",
        "has-tostringtag": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-symbol": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/is-symbol/-/is-symbol-1.1.1.tgz",
      "integrity": "sha512-9gGx6GTtCQM73BgmHQXfDmLtfjjTUDSyoxTCbp5WtoixAhfgsDirWIcVQ/IHpvI5Vgd5i/J5F7B9cN/WlVbC/w==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "has-symbols": "^1.1.0",
        "safe-regex-test": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-typed-array": {
      "version": "1.1.15",
      "resolved": "https://registry.npmjs.org/is-typed-array/-/is-typed-array-1.1.15.tgz",
      "integrity": "sha512-p3EcsicXjit7SaskXHs1hA91QxgTw46Fv6EFKKGS5DRFLD8yKnohjF3hxoju94b/OcMZoQukzpPpBE9uLVKzgQ==",
      "license": "MIT",
      "dependencies": {
        "which-typed-array": "^1.1.16"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-typedarray": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz",
      "integrity": "sha512-cyA56iCMHAh5CdzjJIa4aohJyeO1YbwLi3Jc35MmRU6poroFjIGZzUzupGiRPOjgHg9TLu43xbpwXk523fMxKA==",
      "license": "MIT"
    },
    "node_modules/is-weakmap": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/is-weakmap/-/is-weakmap-2.0.2.tgz",
      "integrity": "sha512-K5pXYOm9wqY1RgjpL3YTkF39tni1XajUIkawTLUo9EZEVUFga5gSQJF8nNS7ZwJQ02y+1YCNYcMh+HIf1ZqE+w==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-weakref": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/is-weakref/-/is-weakref-1.1.1.tgz",
      "integrity": "sha512-6i9mGWSlqzNMEqpCp93KwRS1uUOodk2OJ6b+sq7ZPDSy2WuI5NFIxp/254TytR8ftefexkWn5xNiHUNpPOfSew==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/is-weakset": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/is-weakset/-/is-weakset-2.0.4.tgz",
      "integrity": "sha512-mfcwb6IzQyOKTs84CQMrOwW4gQcaTOAWJ0zzJCl2WSPDrWk/OzDaImWFH3djXhb24g4eudZfLRozAvPGw4d9hQ==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3",
        "get-intrinsic": "^1.2.6"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/isarray": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz",
      "integrity": "sha512-VLghIWNM6ELQzo7zwmcg0NmTVyWKYjvIeM83yjp0wRDTmUnrM678fQbcKBo6n2CJEF0szoG//ytg+TKla89ALQ==",
      "license": "MIT"
    },
    "node_modules/isstream": {
      "version": "0.1.2",
      "resolved": "https://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz",
      "integrity": "sha512-Yljz7ffyPbrLpLngrMtZ7NduUgVvi6wG9RJ9IUcyCd59YQ911PBJphODUcbOVbqYfxe1wuYf/LJ8PauMRwsM/g==",
      "license": "MIT"
    },
    "node_modules/jsbn": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz",
      "integrity": "sha512-UVU9dibq2JcFWxQPA6KCqj5O42VOmAY3zQUfEKxU0KpTGXwNoCjkX1e13eHNvw/xPynt6pU0rZ1htjWTNTSXsg==",
      "license": "MIT"
    },
    "node_modules/json-schema": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/json-schema/-/json-schema-0.4.0.tgz",
      "integrity": "sha512-es94M3nTIfsEPisRafak+HDLfHXnKBhV3vU5eqPcS3flIWqcxJWgXHXiey3YrpaNsanY5ei1VoYEbOzijuq9BA==",
      "license": "(AFL-2.1 OR BSD-3-Clause)"
    },
    "node_modules/json-schema-traverse": {
      "version": "0.4.1",
      "resolved": "https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz",
      "integrity": "sha512-xbbCH5dCYU5T8LcEhhuh7HJ88HXuW3qsI3Y0zOZFKfZEHcpWiHU/Jxzk629Brsab/mMiHQti9wMP+845RPe3Vg==",
      "license": "MIT"
    },
    "node_modules/json-stringify-safe": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz",
      "integrity": "sha512-ZClg6AaYvamvYEE82d3Iyd3vSSIjQ+odgjaTzRuO3s7toCdFKczob2i0zCh7JE8kWn17yvAWhUVxvqGwUalsRA==",
      "license": "ISC"
    },
    "node_modules/jsprim": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/jsprim/-/jsprim-2.0.2.tgz",
      "integrity": "sha512-gqXddjPqQ6G40VdnI6T6yObEC+pDNvyP95wdQhkWkg7crHH3km5qP1FsOXEkzEQwnz6gz5qGTn1c2Y52wP3OyQ==",
      "engines": [
        "node >=0.6.0"
      ],
      "license": "MIT",
      "dependencies": {
        "assert-plus": "1.0.0",
        "extsprintf": "1.3.0",
        "json-schema": "0.4.0",
        "verror": "1.10.0"
      }
    },
    "node_modules/lodash": {
      "version": "4.17.23",
      "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.17.23.tgz",
      "integrity": "sha512-LgVTMpQtIopCi79SJeDiP0TfWi5CNEc/L/aRdTh3yIvmZXTnheWpKjSZhnvMl8iXbC1tFg9gdHHDMLoV7CnG+w==",
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
    "node_modules/minimist": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/minimist/-/minimist-1.2.8.tgz",
      "integrity": "sha512-2yyAR8qBkN3YuheJanUpWC5U3bb5osDywNB8RzDVlDwDHbocAJveqqj1u8+SVD7jkWT4yvsHCpWqqWqAxb0zCA==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/mkdirp": {
      "version": "0.5.6",
      "resolved": "https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.6.tgz",
      "integrity": "sha512-FP+p8RB8OWpF3YZBCrP5gtADmtXApB5AMLn+vdyA+PyxCjrCs00mjyUozssO33cwDeT3wNGdLxJ5M//YqtHAJw==",
      "license": "MIT",
      "dependencies": {
        "minimist": "^1.2.6"
      },
      "bin": {
        "mkdirp": "bin/cmd.js"
      }
    },
    "node_modules/ms": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
      "integrity": "sha512-Tpp60P6IUJDTuOq/5Z8cdskzJujfwqfOTkrwIwj7IRISpnkJnT6SyJ4PCPnGMoFjC9ddhal5KVIYtAt97ix05A==",
      "license": "MIT"
    },
    "node_modules/multer": {
      "version": "1.4.5-lts.2",
      "resolved": "https://registry.npmjs.org/multer/-/multer-1.4.5-lts.2.tgz",
      "integrity": "sha512-VzGiVigcG9zUAoCNU+xShztrlr1auZOlurXynNvO9GiWD1/mTBbUljOKY+qMeazBqXgRnjzeEgJI/wyjJUHg9A==",
      "deprecated": "Multer 1.x is impacted by a number of vulnerabilities, which have been patched in 2.x. You should upgrade to the latest 2.x version.",
      "license": "MIT",
      "dependencies": {
        "append-field": "^1.0.0",
        "busboy": "^1.0.0",
        "concat-stream": "^1.5.2",
        "mkdirp": "^0.5.4",
        "object-assign": "^4.1.1",
        "type-is": "^1.6.4",
        "xtend": "^4.0.0"
      },
      "engines": {
        "node": ">= 6.0.0"
      }
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
    "node_modules/node-telegram-bot-api": {
      "version": "0.66.0",
      "resolved": "https://registry.npmjs.org/node-telegram-bot-api/-/node-telegram-bot-api-0.66.0.tgz",
      "integrity": "sha512-s4Hrg5q+VPl4/tJVG++pImxF6eb8tNJNj4KnDqAOKL6zGU34lo9RXmyAN158njwGN+v8hdNf8s9fWIYW9hPb5A==",
      "license": "MIT",
      "dependencies": {
        "@cypress/request": "^3.0.1",
        "@cypress/request-promise": "^5.0.0",
        "array.prototype.findindex": "^2.0.2",
        "bl": "^1.2.3",
        "debug": "^3.2.7",
        "eventemitter3": "^3.0.0",
        "file-type": "^3.9.0",
        "mime": "^1.6.0",
        "pump": "^2.0.0"
      },
      "engines": {
        "node": ">=0.12"
      }
    },
    "node_modules/node-telegram-bot-api/node_modules/debug": {
      "version": "3.2.7",
      "resolved": "https://registry.npmjs.org/debug/-/debug-3.2.7.tgz",
      "integrity": "sha512-CFjzYYAi4ThfiQvizrFQevTTXHtnCqWfe7x1AhgEscTz6ZbLbfoLRLPugTQyBth6f8ZERVUSyWHFD/7Wu4t1XQ==",
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.1"
      }
    },
    "node_modules/node-telegram-bot-api/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/oauth-sign": {
      "version": "0.9.0",
      "resolved": "https://registry.npmjs.org/oauth-sign/-/oauth-sign-0.9.0.tgz",
      "integrity": "sha512-fexhUFFPTGV8ybAtSIGbV6gOkSv8UtRbDBnAyLQw4QPKkgNlsH2ByPGtMUqdWkos6YCRmAqViwgZrJc/mRDzZQ==",
      "license": "Apache-2.0",
      "engines": {
        "node": "*"
      }
    },
    "node_modules/object-assign": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz",
      "integrity": "sha512-rJgTQnkUnH1sFw8yT6VSU3zD3sWmu6sZhIseY8VX+GRu3P6F7Fu+JNDoXfklElbLJSnc3FUQHVe4cU5hj+BcUg==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
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
    "node_modules/object-keys": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/object-keys/-/object-keys-1.1.1.tgz",
      "integrity": "sha512-NuAESUOUMrlIXOfHKzD6bpPu3tYt3xvjNdRIQ+FeT0lNb4K8WR70CaDxhuNguS2XG+GjkyMwOzsN5ZktImfhLA==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/object.assign": {
      "version": "4.1.7",
      "resolved": "https://registry.npmjs.org/object.assign/-/object.assign-4.1.7.tgz",
      "integrity": "sha512-nK28WOo+QIjBkDduTINE4JkF/UJJKyf2EJxvJKfblDpyg0Q+pkOHNTL0Qwy6NP6FhE/EnzV73BxxqcJaXY9anw==",
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.8",
        "call-bound": "^1.0.3",
        "define-properties": "^1.2.1",
        "es-object-atoms": "^1.0.0",
        "has-symbols": "^1.1.0",
        "object-keys": "^1.1.1"
      },
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
    "node_modules/own-keys": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/own-keys/-/own-keys-1.0.1.tgz",
      "integrity": "sha512-qFOyK5PjiWZd+QQIh+1jhdb9LpxTF0qs7Pm8o5QHYZ0M3vKqSqzsZaEB6oWlxZ+q2sJBMI/Ktgd2N5ZwQoRHfg==",
      "license": "MIT",
      "dependencies": {
        "get-intrinsic": "^1.2.6",
        "object-keys": "^1.1.1",
        "safe-push-apply": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
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
    "node_modules/performance-now": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz",
      "integrity": "sha512-7EAHlyLHI56VEIdK57uwHdHKIaAGbnXPiw0yWbarQZOKaKpvUIgW0jWRVLiatnM+XXlSwsanIBH/hzGMJulMow==",
      "license": "MIT"
    },
    "node_modules/possible-typed-array-names": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/possible-typed-array-names/-/possible-typed-array-names-1.1.0.tgz",
      "integrity": "sha512-/+5VFTchJDoVj3bhoqi6UeymcD00DAwb1nJwamzPvHEszJ4FpF6SNNbUbOS8yI56qHzdV8eK0qEfOSiodkTdxg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/process-nextick-args": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz",
      "integrity": "sha512-3ouUOpQhtgrbOa17J7+uxOTpITYWaGP7/AhoR3+A+/1e9skrzelGi/dXzEYyvbxubEF6Wn2ypscTKiKJFFn1ag==",
      "license": "MIT"
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
    "node_modules/psl": {
      "version": "1.15.0",
      "resolved": "https://registry.npmjs.org/psl/-/psl-1.15.0.tgz",
      "integrity": "sha512-JZd3gMVBAVQkSs6HdNZo9Sdo0LNcQeMNP3CozBJb3JYC/QUYZTnKxP+f8oWRX4rHP5EurWxqAHTSwUCjlNKa1w==",
      "license": "MIT",
      "dependencies": {
        "punycode": "^2.3.1"
      },
      "funding": {
        "url": "https://github.com/sponsors/lupomontero"
      }
    },
    "node_modules/pump": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/pump/-/pump-2.0.1.tgz",
      "integrity": "sha512-ruPMNRkN3MHP1cWJc9OWr+T/xDP0jhXYCLfJcBuX54hhfIBnaQmAUMfDcG4DM5UMWByBbJY69QSphm3jtDKIkA==",
      "license": "MIT",
      "dependencies": {
        "end-of-stream": "^1.1.0",
        "once": "^1.3.1"
      }
    },
    "node_modules/punycode": {
      "version": "2.3.1",
      "resolved": "https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz",
      "integrity": "sha512-vYt7UD1U9Wg6138shLtLOvdAu+8DsC/ilFtEVHcH+wydcSpNE20AfSOduf6MkRFahL5FY7X1oU7nKVZFtfq8Fg==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/qs": {
      "version": "6.14.1",
      "resolved": "https://registry.npmjs.org/qs/-/qs-6.14.1.tgz",
      "integrity": "sha512-4EK3+xJl8Ts67nLYNwqw/dsFVnCf+qR7RgXSK9jEEm9unao3njwMDdmsdvoKBKHzxd7tCYz5e5M+SnMjdtXGQQ==",
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
    "node_modules/querystringify": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/querystringify/-/querystringify-2.2.0.tgz",
      "integrity": "sha512-FIqgj2EUvTa7R50u0rGsyTftzjYmv/a3hO345bZNrqabNqjtgiDMgmo4mkUjd+nzU5oF3dClKqFIPUKybUyqoQ==",
      "license": "MIT"
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
    "node_modules/readable-stream": {
      "version": "2.3.8",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.8.tgz",
      "integrity": "sha512-8p0AUk4XODgIewSi0l8Epjs+EVnWiK7NoDIEGU0HhE7+ZyY8D1IMY7odu5lRrFXGg71L15KG8QrPmum45RTtdA==",
      "license": "MIT",
      "dependencies": {
        "core-util-is": "~1.0.0",
        "inherits": "~2.0.3",
        "isarray": "~1.0.0",
        "process-nextick-args": "~2.0.0",
        "safe-buffer": "~5.1.1",
        "string_decoder": "~1.1.1",
        "util-deprecate": "~1.0.1"
      }
    },
    "node_modules/readable-stream/node_modules/safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g==",
      "license": "MIT"
    },
    "node_modules/reflect.getprototypeof": {
      "version": "1.0.10",
      "resolved": "https://registry.npmjs.org/reflect.getprototypeof/-/reflect.getprototypeof-1.0.10.tgz",
      "integrity": "sha512-00o4I+DVrefhv+nX0ulyi3biSHCPDe+yLv5o/p6d/UVlirijB8E16FtfwSAi4g3tcqrQ4lRAqQSoFEZJehYEcw==",
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.8",
        "define-properties": "^1.2.1",
        "es-abstract": "^1.23.9",
        "es-errors": "^1.3.0",
        "es-object-atoms": "^1.0.0",
        "get-intrinsic": "^1.2.7",
        "get-proto": "^1.0.1",
        "which-builtin-type": "^1.2.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/regexp.prototype.flags": {
      "version": "1.5.4",
      "resolved": "https://registry.npmjs.org/regexp.prototype.flags/-/regexp.prototype.flags-1.5.4.tgz",
      "integrity": "sha512-dYqgNSZbDwkaJ2ceRd9ojCGjBq+mOm9LmtXnAnEGyHhN/5R7iDW2TRw3h+o/jCFxus3P2LfWIIiwowAjANm7IA==",
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.8",
        "define-properties": "^1.2.1",
        "es-errors": "^1.3.0",
        "get-proto": "^1.0.1",
        "gopd": "^1.2.0",
        "set-function-name": "^2.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/request": {
      "version": "2.88.2",
      "resolved": "https://registry.npmjs.org/request/-/request-2.88.2.tgz",
      "integrity": "sha512-MsvtOrfG9ZcrOwAW+Qi+F6HbD0CWXEh9ou77uOb7FM2WPhwT7smM833PzanhJLsgXjN89Ir6V2PczXNnMpwKhw==",
      "deprecated": "request has been deprecated, see https://github.com/request/request/issues/3142",
      "license": "Apache-2.0",
      "dependencies": {
        "aws-sign2": "~0.7.0",
        "aws4": "^1.8.0",
        "caseless": "~0.12.0",
        "combined-stream": "~1.0.6",
        "extend": "~3.0.2",
        "forever-agent": "~0.6.1",
        "form-data": "~2.3.2",
        "har-validator": "~5.1.3",
        "http-signature": "~1.2.0",
        "is-typedarray": "~1.0.0",
        "isstream": "~0.1.2",
        "json-stringify-safe": "~5.0.1",
        "mime-types": "~2.1.19",
        "oauth-sign": "~0.9.0",
        "performance-now": "^2.1.0",
        "qs": "~6.5.2",
        "safe-buffer": "^5.1.2",
        "tough-cookie": "~2.5.0",
        "tunnel-agent": "^0.6.0",
        "uuid": "^3.3.2"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/request-promise-core": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/request-promise-core/-/request-promise-core-1.1.3.tgz",
      "integrity": "sha512-QIs2+ArIGQVp5ZYbWD5ZLCY29D5CfWizP8eWnm8FoGD1TX61veauETVQbrV60662V0oFBkrDOuaBI8XgtuyYAQ==",
      "license": "ISC",
      "dependencies": {
        "lodash": "^4.17.15"
      },
      "engines": {
        "node": ">=0.10.0"
      },
      "peerDependencies": {
        "request": "^2.34"
      }
    },
    "node_modules/request/node_modules/form-data": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/form-data/-/form-data-2.3.3.tgz",
      "integrity": "sha512-1lLKB2Mu3aGP1Q/2eCOx0fNbRMe7XdwktwOruhfqqd0rIJWwN4Dh+E3hrPSlDCXnSR7UtZ1N38rVXm+6+MEhJQ==",
      "license": "MIT",
      "dependencies": {
        "asynckit": "^0.4.0",
        "combined-stream": "^1.0.6",
        "mime-types": "^2.1.12"
      },
      "engines": {
        "node": ">= 0.12"
      }
    },
    "node_modules/request/node_modules/http-signature": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/http-signature/-/http-signature-1.2.0.tgz",
      "integrity": "sha512-CAbnr6Rz4CYQkLYUtSNXxQPUH2gK8f3iWexVlsnMeD+GjlsQ0Xsy1cOX+mN3dtxYomRy21CiOzU8Uhw6OwncEQ==",
      "license": "MIT",
      "dependencies": {
        "assert-plus": "^1.0.0",
        "jsprim": "^1.2.2",
        "sshpk": "^1.7.0"
      },
      "engines": {
        "node": ">=0.8",
        "npm": ">=1.3.7"
      }
    },
    "node_modules/request/node_modules/jsprim": {
      "version": "1.4.2",
      "resolved": "https://registry.npmjs.org/jsprim/-/jsprim-1.4.2.tgz",
      "integrity": "sha512-P2bSOMAc/ciLz6DzgjVlGJP9+BrJWu5UDGK70C2iweC5QBIeFf0ZXRvGjEj2uYgrY2MkAAhsSWHDWlFtEroZWw==",
      "license": "MIT",
      "dependencies": {
        "assert-plus": "1.0.0",
        "extsprintf": "1.3.0",
        "json-schema": "0.4.0",
        "verror": "1.10.0"
      },
      "engines": {
        "node": ">=0.6.0"
      }
    },
    "node_modules/request/node_modules/qs": {
      "version": "6.5.5",
      "resolved": "https://registry.npmjs.org/qs/-/qs-6.5.5.tgz",
      "integrity": "sha512-mzR4sElr1bfCaPJe7m8ilJ6ZXdDaGoObcYR0ZHSsktM/Lt21MVHj5De30GQH2eiZ1qGRTO7LCAzQsUeXTNexWQ==",
      "license": "BSD-3-Clause",
      "engines": {
        "node": ">=0.6"
      }
    },
    "node_modules/request/node_modules/tough-cookie": {
      "version": "2.5.0",
      "resolved": "https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.5.0.tgz",
      "integrity": "sha512-nlLsUzgm1kfLXSXfRZMc1KLAugd4hqJHDTvc2hDIwS3mZAfMEuMbc03SujMF+GEcpaX/qboeycw6iO8JwVv2+g==",
      "license": "BSD-3-Clause",
      "dependencies": {
        "psl": "^1.1.28",
        "punycode": "^2.1.1"
      },
      "engines": {
        "node": ">=0.8"
      }
    },
    "node_modules/request/node_modules/uuid": {
      "version": "3.4.0",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-3.4.0.tgz",
      "integrity": "sha512-HjSDRw6gZE5JMggctHBcjVak08+KEVhSIiDzFnT9S9aegmp85S/bReBVTb4QTFaRNptJ9kuYaNhnbNEOkbKb/A==",
      "deprecated": "Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See https://v8.dev/blog/math-random for details.",
      "license": "MIT",
      "bin": {
        "uuid": "bin/uuid"
      }
    },
    "node_modules/requires-port": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/requires-port/-/requires-port-1.0.0.tgz",
      "integrity": "sha512-KigOCHcocU3XODJxsu8i/j8T9tzT4adHiecwORRQ0ZZFcp7ahwXuRU1m+yuO90C5ZUyGeGfocHDI14M3L3yDAQ==",
      "license": "MIT"
    },
    "node_modules/safe-array-concat": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/safe-array-concat/-/safe-array-concat-1.1.3.tgz",
      "integrity": "sha512-AURm5f0jYEOydBj7VQlVvDrjeFgthDdEF5H1dP+6mNpoXOMo1quQqJ4wvJDyRZ9+pO3kGWoOdmV08cSv2aJV6Q==",
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.8",
        "call-bound": "^1.0.2",
        "get-intrinsic": "^1.2.6",
        "has-symbols": "^1.1.0",
        "isarray": "^2.0.5"
      },
      "engines": {
        "node": ">=0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/safe-array-concat/node_modules/isarray": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/isarray/-/isarray-2.0.5.tgz",
      "integrity": "sha512-xHjhDr3cNBK0BzdUJSPXZntQUx/mwMS5Rw4A7lPJ90XGAO6ISP/ePDNuo0vhqOZU+UD5JoodwCAAoZQd3FeAKw==",
      "license": "MIT"
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
    "node_modules/safe-push-apply": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/safe-push-apply/-/safe-push-apply-1.0.0.tgz",
      "integrity": "sha512-iKE9w/Z7xCzUMIZqdBsp6pEQvwuEebH4vdpjcDWnyzaI6yl6O9FHvVpmGelvEHNsoY6wGblkxR6Zty/h00WiSA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "isarray": "^2.0.5"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/safe-push-apply/node_modules/isarray": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/isarray/-/isarray-2.0.5.tgz",
      "integrity": "sha512-xHjhDr3cNBK0BzdUJSPXZntQUx/mwMS5Rw4A7lPJ90XGAO6ISP/ePDNuo0vhqOZU+UD5JoodwCAAoZQd3FeAKw==",
      "license": "MIT"
    },
    "node_modules/safe-regex-test": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/safe-regex-test/-/safe-regex-test-1.1.0.tgz",
      "integrity": "sha512-x/+Cz4YrimQxQccJf5mKEbIa1NzeCRNI5Ecl/ekmlYaampdNLPalVyIcCZNNH3MvmqBugV5TMYZXv0ljslUlaw==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "es-errors": "^1.3.0",
        "is-regex": "^1.2.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/safer-buffer": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz",
      "integrity": "sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg==",
      "license": "MIT"
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
    "node_modules/set-function-length": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/set-function-length/-/set-function-length-1.2.2.tgz",
      "integrity": "sha512-pgRc4hJ4/sNjWCSS9AmnS40x3bNMDTknHgL5UaMBTMyJnU90EgWh1Rz+MC9eFu4BuN/UwZjKQuY/1v3rM7HMfg==",
      "license": "MIT",
      "dependencies": {
        "define-data-property": "^1.1.4",
        "es-errors": "^1.3.0",
        "function-bind": "^1.1.2",
        "get-intrinsic": "^1.2.4",
        "gopd": "^1.0.1",
        "has-property-descriptors": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/set-function-name": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/set-function-name/-/set-function-name-2.0.2.tgz",
      "integrity": "sha512-7PGFlmtwsEADb0WYyvCMa1t+yke6daIG4Wirafur5kcf+MhUnPms1UeR0CKQdTZD81yESwMHbtn+TR+dMviakQ==",
      "license": "MIT",
      "dependencies": {
        "define-data-property": "^1.1.4",
        "es-errors": "^1.3.0",
        "functions-have-names": "^1.2.3",
        "has-property-descriptors": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/set-proto": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/set-proto/-/set-proto-1.0.0.tgz",
      "integrity": "sha512-RJRdvCo6IAnPdsvP/7m6bsQqNnn1FCBX5ZNtFL98MmFF/4xAIJTIg1YbHW5DC2W5SKZanrC6i4HsJqlajw/dZw==",
      "license": "MIT",
      "dependencies": {
        "dunder-proto": "^1.0.1",
        "es-errors": "^1.3.0",
        "es-object-atoms": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
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
    "node_modules/sql.js": {
      "version": "1.13.0",
      "resolved": "https://registry.npmjs.org/sql.js/-/sql.js-1.13.0.tgz",
      "integrity": "sha512-RJbVP1HRDlUUXahJ7VMTcu9Rm1Nzw+EBpoPr94vnbD4LwR715F3CcxE2G2k45PewcaZ57pjetYa+LoSJLAASgA==",
      "license": "MIT"
    },
    "node_modules/sshpk": {
      "version": "1.18.0",
      "resolved": "https://registry.npmjs.org/sshpk/-/sshpk-1.18.0.tgz",
      "integrity": "sha512-2p2KJZTSqQ/I3+HX42EpYOa2l3f8Erv8MWKsy2I9uf4wA7yFIkXRffYdsx86y6z4vHtV8u7g+pPlr8/4ouAxsQ==",
      "license": "MIT",
      "dependencies": {
        "asn1": "~0.2.3",
        "assert-plus": "^1.0.0",
        "bcrypt-pbkdf": "^1.0.0",
        "dashdash": "^1.12.0",
        "ecc-jsbn": "~0.1.1",
        "getpass": "^0.1.1",
        "jsbn": "~0.1.0",
        "safer-buffer": "^2.0.2",
        "tweetnacl": "~0.14.0"
      },
      "bin": {
        "sshpk-conv": "bin/sshpk-conv",
        "sshpk-sign": "bin/sshpk-sign",
        "sshpk-verify": "bin/sshpk-verify"
      },
      "engines": {
        "node": ">=0.10.0"
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
    "node_modules/stealthy-require": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/stealthy-require/-/stealthy-require-1.1.1.tgz",
      "integrity": "sha512-ZnWpYnYugiOVEY5GkcuJK1io5V8QmNYChG62gSit9pQVGErXtrKuPC55ITaVSukmMta5qpMU7vqLt2Lnni4f/g==",
      "license": "ISC",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/stop-iteration-iterator": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/stop-iteration-iterator/-/stop-iteration-iterator-1.1.0.tgz",
      "integrity": "sha512-eLoXW/DHyl62zxY4SCaIgnRhuMr6ri4juEYARS8E6sCEqzKpOiE521Ucofdx+KnDZl5xmvGYaaKCk5FEOxJCoQ==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "internal-slot": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/streamsearch": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/streamsearch/-/streamsearch-1.1.0.tgz",
      "integrity": "sha512-Mcc5wHehp9aXz1ax6bZUyY5afg9u2rv5cqQI3mRrYkGC8rW2hM02jWuwjtL++LS5qinSyhj2QfLyNsuc+VsExg==",
      "engines": {
        "node": ">=10.0.0"
      }
    },
    "node_modules/string_decoder": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz",
      "integrity": "sha512-n/ShnvDi6FHbbVfviro+WojiFzv+s8MPMHBczVePfUpDJLwoLT0ht1l4YwBCbi8pJAveEEdnkHyPyTP/mzRfwg==",
      "license": "MIT",
      "dependencies": {
        "safe-buffer": "~5.1.0"
      }
    },
    "node_modules/string_decoder/node_modules/safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g==",
      "license": "MIT"
    },
    "node_modules/string.prototype.trim": {
      "version": "1.2.10",
      "resolved": "https://registry.npmjs.org/string.prototype.trim/-/string.prototype.trim-1.2.10.tgz",
      "integrity": "sha512-Rs66F0P/1kedk5lyYyH9uBzuiI/kNRmwJAR9quK6VOtIpZ2G+hMZd+HQbbv25MgCA6gEffoMZYxlTod4WcdrKA==",
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.8",
        "call-bound": "^1.0.2",
        "define-data-property": "^1.1.4",
        "define-properties": "^1.2.1",
        "es-abstract": "^1.23.5",
        "es-object-atoms": "^1.0.0",
        "has-property-descriptors": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/string.prototype.trimend": {
      "version": "1.0.9",
      "resolved": "https://registry.npmjs.org/string.prototype.trimend/-/string.prototype.trimend-1.0.9.tgz",
      "integrity": "sha512-G7Ok5C6E/j4SGfyLCloXTrngQIQU3PWtXGst3yM7Bea9FRURf1S42ZHlZZtsNque2FN2PoUhfZXYLNWwEr4dLQ==",
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.8",
        "call-bound": "^1.0.2",
        "define-properties": "^1.2.1",
        "es-object-atoms": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/string.prototype.trimstart": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/string.prototype.trimstart/-/string.prototype.trimstart-1.0.8.tgz",
      "integrity": "sha512-UXSH262CSZY1tfu3G3Secr6uGLCFVPMhIqHjlgCUtCCcgihYc/xKs9djMTMUOb2j1mVSeU8EU6NWc/iQKU6Gfg==",
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.7",
        "define-properties": "^1.2.1",
        "es-object-atoms": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/tldts": {
      "version": "6.1.86",
      "resolved": "https://registry.npmjs.org/tldts/-/tldts-6.1.86.tgz",
      "integrity": "sha512-WMi/OQ2axVTf/ykqCQgXiIct+mSQDFdH2fkwhPwgEwvJ1kSzZRiinb0zF2Xb8u4+OqPChmyI6MEu4EezNJz+FQ==",
      "license": "MIT",
      "dependencies": {
        "tldts-core": "^6.1.86"
      },
      "bin": {
        "tldts": "bin/cli.js"
      }
    },
    "node_modules/tldts-core": {
      "version": "6.1.86",
      "resolved": "https://registry.npmjs.org/tldts-core/-/tldts-core-6.1.86.tgz",
      "integrity": "sha512-Je6p7pkk+KMzMv2XXKmAE3McmolOQFdxkKw0R8EYNr7sELW46JqnNeTX8ybPiQgvg1ymCoF8LXs5fzFaZvJPTA==",
      "license": "MIT"
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
    "node_modules/tough-cookie": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/tough-cookie/-/tough-cookie-5.1.2.tgz",
      "integrity": "sha512-FVDYdxtnj0G6Qm/DhNPSb8Ju59ULcup3tuJxkFb5K8Bv2pUXILbf0xZWU8PX8Ov19OXljbUyveOFwRMwkXzO+A==",
      "license": "BSD-3-Clause",
      "dependencies": {
        "tldts": "^6.1.32"
      },
      "engines": {
        "node": ">=16"
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
    "node_modules/tweetnacl": {
      "version": "0.14.5",
      "resolved": "https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz",
      "integrity": "sha512-KXXFFdAbFXY4geFIwoyNK+f5Z1b7swfXABfL7HXCmoIWMKU3dmS26672A4EeQtDzLKy7SXmfBu51JolvEKwtGA==",
      "license": "Unlicense"
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
    "node_modules/typed-array-buffer": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/typed-array-buffer/-/typed-array-buffer-1.0.3.tgz",
      "integrity": "sha512-nAYYwfY3qnzX30IkA6AQZjVbtK6duGontcQm1WSG1MD94YLqK0515GNApXkoxKOWMusVssAHWLh9SeaoefYFGw==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3",
        "es-errors": "^1.3.0",
        "is-typed-array": "^1.1.14"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/typed-array-byte-length": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/typed-array-byte-length/-/typed-array-byte-length-1.0.3.tgz",
      "integrity": "sha512-BaXgOuIxz8n8pIq3e7Atg/7s+DpiYrxn4vdot3w9KbnBhcRQq6o3xemQdIfynqSeXeDrF32x+WvfzmOjPiY9lg==",
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.8",
        "for-each": "^0.3.3",
        "gopd": "^1.2.0",
        "has-proto": "^1.2.0",
        "is-typed-array": "^1.1.14"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/typed-array-byte-offset": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/typed-array-byte-offset/-/typed-array-byte-offset-1.0.4.tgz",
      "integrity": "sha512-bTlAFB/FBYMcuX81gbL4OcpH5PmlFHqlCCpAl8AlEzMz5k53oNDvN8p1PNOWLEmI2x4orp3raOFB51tv9X+MFQ==",
      "license": "MIT",
      "dependencies": {
        "available-typed-arrays": "^1.0.7",
        "call-bind": "^1.0.8",
        "for-each": "^0.3.3",
        "gopd": "^1.2.0",
        "has-proto": "^1.2.0",
        "is-typed-array": "^1.1.15",
        "reflect.getprototypeof": "^1.0.9"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/typed-array-length": {
      "version": "1.0.7",
      "resolved": "https://registry.npmjs.org/typed-array-length/-/typed-array-length-1.0.7.tgz",
      "integrity": "sha512-3KS2b+kL7fsuk/eJZ7EQdnEmQoaho/r6KUef7hxvltNA5DR8NAUM+8wJMbJyZ4G9/7i3v5zPBIMN5aybAh2/Jg==",
      "license": "MIT",
      "dependencies": {
        "call-bind": "^1.0.7",
        "for-each": "^0.3.3",
        "gopd": "^1.0.1",
        "is-typed-array": "^1.1.13",
        "possible-typed-array-names": "^1.0.0",
        "reflect.getprototypeof": "^1.0.6"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/typedarray": {
      "version": "0.0.6",
      "resolved": "https://registry.npmjs.org/typedarray/-/typedarray-0.0.6.tgz",
      "integrity": "sha512-/aCDEGatGvZ2BIk+HmLf4ifCJFwvKFNb9/JeZPMulfgFracn9QFcAf5GO8B/mweUjSoblS5In0cWhqpfs/5PQA==",
      "license": "MIT"
    },
    "node_modules/unbox-primitive": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/unbox-primitive/-/unbox-primitive-1.1.0.tgz",
      "integrity": "sha512-nWJ91DjeOkej/TA8pXQ3myruKpKEYgqvpw9lz4OPHj/NWFNluYrjbz9j01CJ8yKQd2g4jFoOkINCTW2I5LEEyw==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.3",
        "has-bigints": "^1.0.2",
        "has-symbols": "^1.1.0",
        "which-boxed-primitive": "^1.1.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/universalify": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/universalify/-/universalify-0.2.0.tgz",
      "integrity": "sha512-CJ1QgKmNg3CwvAv/kOFmtnEN05f0D/cn9QntgNOQlQF9dgvVTHj3t+8JPdjqawCHk7V/KA+fbUqzZ9XWhcqPUg==",
      "license": "MIT",
      "engines": {
        "node": ">= 4.0.0"
      }
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
    "node_modules/uri-js": {
      "version": "4.4.1",
      "resolved": "https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz",
      "integrity": "sha512-7rKUyy33Q1yc98pQ1DAmLtwX109F7TIfWlW1Ydo8Wl1ii1SeHieeh0HHfPeL2fMXK6z0s8ecKs9frCuLJvndBg==",
      "license": "BSD-2-Clause",
      "dependencies": {
        "punycode": "^2.1.0"
      }
    },
    "node_modules/url-parse": {
      "version": "1.5.10",
      "resolved": "https://registry.npmjs.org/url-parse/-/url-parse-1.5.10.tgz",
      "integrity": "sha512-WypcfiRhfeUP9vvF0j6rw0J3hrWrw6iZv3+22h6iRMJ/8z1Tj6XfLP4DsUix5MhMPnXpiHDoKyoZ/bdCkwBCiQ==",
      "license": "MIT",
      "dependencies": {
        "querystringify": "^2.1.1",
        "requires-port": "^1.0.0"
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
    "node_modules/uuid": {
      "version": "8.3.2",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-8.3.2.tgz",
      "integrity": "sha512-+NYs2QeMWy+GWFOEm9xnn6HCDp0l7QBD7ml8zLUmJ+93Q5NF0NocErnwkTkXVFNiX3/fpC6afS8Dhb/gz7R7eg==",
      "license": "MIT",
      "bin": {
        "uuid": "dist/bin/uuid"
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
    "node_modules/verror": {
      "version": "1.10.0",
      "resolved": "https://registry.npmjs.org/verror/-/verror-1.10.0.tgz",
      "integrity": "sha512-ZZKSmDAEFOijERBLkmYfJ+vmk3w+7hOLYDNkRCuRuMJGEmqYNCNLyBBFwWKVMhfwaEF3WOd0Zlw86U/WC/+nYw==",
      "engines": [
        "node >=0.6.0"
      ],
      "license": "MIT",
      "dependencies": {
        "assert-plus": "^1.0.0",
        "core-util-is": "1.0.2",
        "extsprintf": "^1.2.0"
      }
    },
    "node_modules/verror/node_modules/core-util-is": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz",
      "integrity": "sha512-3lqz5YjWTYnW6dlDa5TLaTCcShfar1e40rmcJVwCBJC6mWlFuj0eCHIElmG1g5kyuJ/GD+8Wn4FFCcz4gJPfaQ==",
      "license": "MIT"
    },
    "node_modules/which-boxed-primitive": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/which-boxed-primitive/-/which-boxed-primitive-1.1.1.tgz",
      "integrity": "sha512-TbX3mj8n0odCBFVlY8AxkqcHASw3L60jIuF8jFP78az3C2YhmGvqbHBpAjTRH2/xqYunrJ9g1jSyjCjpoWzIAA==",
      "license": "MIT",
      "dependencies": {
        "is-bigint": "^1.1.0",
        "is-boolean-object": "^1.2.1",
        "is-number-object": "^1.1.1",
        "is-string": "^1.1.1",
        "is-symbol": "^1.1.1"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/which-builtin-type": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/which-builtin-type/-/which-builtin-type-1.2.1.tgz",
      "integrity": "sha512-6iBczoX+kDQ7a3+YJBnh3T+KZRxM/iYNPXicqk66/Qfm1b93iu+yOImkg0zHbj5LNOcNv1TEADiZ0xa34B4q6Q==",
      "license": "MIT",
      "dependencies": {
        "call-bound": "^1.0.2",
        "function.prototype.name": "^1.1.6",
        "has-tostringtag": "^1.0.2",
        "is-async-function": "^2.0.0",
        "is-date-object": "^1.1.0",
        "is-finalizationregistry": "^1.1.0",
        "is-generator-function": "^1.0.10",
        "is-regex": "^1.2.1",
        "is-weakref": "^1.0.2",
        "isarray": "^2.0.5",
        "which-boxed-primitive": "^1.1.0",
        "which-collection": "^1.0.2",
        "which-typed-array": "^1.1.16"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/which-builtin-type/node_modules/isarray": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/isarray/-/isarray-2.0.5.tgz",
      "integrity": "sha512-xHjhDr3cNBK0BzdUJSPXZntQUx/mwMS5Rw4A7lPJ90XGAO6ISP/ePDNuo0vhqOZU+UD5JoodwCAAoZQd3FeAKw==",
      "license": "MIT"
    },
    "node_modules/which-collection": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/which-collection/-/which-collection-1.0.2.tgz",
      "integrity": "sha512-K4jVyjnBdgvc86Y6BkaLZEN933SwYOuBFkdmBu9ZfkcAbdVbpITnDmjvZ/aQjRXQrv5EPkTnD1s39GiiqbngCw==",
      "license": "MIT",
      "dependencies": {
        "is-map": "^2.0.3",
        "is-set": "^2.0.3",
        "is-weakmap": "^2.0.2",
        "is-weakset": "^2.0.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/which-typed-array": {
      "version": "1.1.20",
      "resolved": "https://registry.npmjs.org/which-typed-array/-/which-typed-array-1.1.20.tgz",
      "integrity": "sha512-LYfpUkmqwl0h9A2HL09Mms427Q1RZWuOHsukfVcKRq9q95iQxdw0ix1JQrqbcDR9PH1QDwf5Qo8OZb5lksZ8Xg==",
      "license": "MIT",
      "dependencies": {
        "available-typed-arrays": "^1.0.7",
        "call-bind": "^1.0.8",
        "call-bound": "^1.0.4",
        "for-each": "^0.3.5",
        "get-proto": "^1.0.1",
        "gopd": "^1.2.0",
        "has-tostringtag": "^1.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/wrappy": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
      "integrity": "sha512-l4Sp/DRseor9wL6EvV2+TuQn63dMkPjZ/sp9XkghTEbV9KlPS1xUsZ3u7/IQO4wxtcFB4bgpQPRcR3QCvezPcQ==",
      "license": "ISC"
    },
    "node_modules/ws": {
      "version": "8.19.0",
      "resolved": "https://registry.npmjs.org/ws/-/ws-8.19.0.tgz",
      "integrity": "sha512-blAT2mjOEIi0ZzruJfIhb3nps74PRWTCz1IjglWEEpQl5XS/UNama6u2/rjFkDDouqr4L67ry+1aGIALViWjDg==",
      "license": "MIT",
      "engines": {
        "node": ">=10.0.0"
      },
      "peerDependencies": {
        "bufferutil": "^4.0.1",
        "utf-8-validate": ">=5.0.2"
      },
      "peerDependenciesMeta": {
        "bufferutil": {
          "optional": true
        },
        "utf-8-validate": {
          "optional": true
        }
      }
    },
    "node_modules/xtend": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/xtend/-/xtend-4.0.2.tgz",
      "integrity": "sha512-LKYU1iAXJXUgAXn9URjiu+MWhyUXHsvfp7mcuYm9dSUKK0/CjtrUwFAxD82/mCWbtLsGjFIad0wIsod4zrTAEQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.4"
      }
    }
  }
}
```

## File: payload\package.json
```
{
  "name": "antigravity-mobile",
  "version": "2.0.0",
  "type": "module",
  "description": "Mobile dashboard for Antigravity IDE - live chat view and remote control",
  "author": "AvenalJ",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/AvenalJ/AntigravityMobile.git"
  },
  "keywords": [
    "antigravity",
    "mobile",
    "dashboard",
    "vscode",
    "ide"
  ],
  "main": "src/http-server.mjs",
  "scripts": {
    "start": "node src/http-server.mjs",
    "server": "node src/http-server.mjs",
    "launch": "node src/launcher.mjs"
  },
  "dependencies": {
    "express": "^4.18.2",
    "multer": "^1.4.5-lts.1",
    "node-telegram-bot-api": "^0.66.0",
    "sql.js": "^1.13.0",
    "ws": "^8.16.0"
  }
}
```

## File: payload\README.md
```
# Antigravity Mobile

Mobile dashboard and admin panel for [Antigravity IDE](https://antigravity.google). Monitor conversations, manage your agent, and get notified — all from your phone.

<p align="center">
  <img src="screenshots/screenshot.png" width="620" alt="Admin Panel Landscape" style="border:1px solid #30363d;border-radius:8px;" />
</p>

## Features

**Mobile Dashboard** — Real-time chat streaming, file browser with syntax highlighting, model quota monitor, and quick commands. Available in full and lite mode for low-bandwidth use.

**Admin Panel** (`/admin`) — Localhost-only control panel with:
- Telegram bot notifications (completion, input needed, errors)
- Auto-accept for command prompts (Run, Allow, Continue, etc.)
- Quick commands — saved prompts injected directly into the agent
- Screenshot timeline with auto-capture
- Theme and layout customization for the mobile dashboard
- Multi-device CDP switching
- Remote access via Cloudflare quick tunnels
- Session event logs

**Remote Access** — Secure access from anywhere using Cloudflare quick tunnels. No account required — generates a random `.trycloudflare.com` URL with QR code. Auto-start option available.

**Error Detection** — Monitors both the chat stream and full-page modal dialogs for errors like "Agent terminated" and "Model quota reached". Sends Telegram alerts on detection.

**Security** — Optional PIN authentication with IP-based rate limiting (5 attempts, 15-min lockout), localhost-only admin endpoints, encrypted tunnels via Cloudflare HTTPS. No data sent externally (Telegram API excluded).

## Quick Start

**Requirements:** Node.js 18+, Antigravity IDE installed. Optional: [`cloudflared`](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/) for remote access (the launch script offers to install it automatically).

```bash
git clone https://github.com/AvenalJ/AntigravityMobile.git
cd AntigravityMobile
```

**Windows:** Double-click `Start-Antigravity-Mobile.bat`
**macOS/Linux:** `./Start-Antigravity-Mobile.sh`

The admin panel opens automatically at `http://localhost:3001/admin`.
Access the mobile dashboard from your phone at `http://YOUR_PC_IP:3001`.

Dependencies install automatically on first run. The script handles launching Antigravity with CDP enabled.

To stop: run `Stop-Antigravity-Mobile.bat` (Windows) or `./Stop-Antigravity-Mobile.sh`.

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│  Your Machine                                             │
│                                                           │
│  Antigravity IDE ◄──── CDP ────► Antigravity Mobile       │
│                                  Server (:3001)           │
│                                    │           │          │
│                              WebSocket       HTTPS        │
│                                    │           │          │
│                               Phone 📱    Telegram 🤖    │
└──────────────────────────────────────────────────────────┘
```

| Component | Description |
|-----------|-------------|
| `src/http-server.mjs` | Express server, API endpoints, WebSocket bridge |
| `src/chat-stream.mjs` | CDP-based chat capture, auto-accept, notification triggers |
| `src/cdp-client.mjs` | Chrome DevTools Protocol client (screenshots, input injection, DOM queries) |
| `src/supervisor-service.mjs` | AI supervisor — autonomous monitoring, error recovery, task queue, assist chat |
| `src/ollama-client.mjs` | Thin wrapper around the Ollama REST API |
| `src/telegram-bot.mjs` | Telegram Bot API — sends alerts for agent events |
| `src/tunnel.mjs` | Cloudflare quick tunnel management (start/stop/status) |
| `src/config.mjs` | Persistent JSON config store |
| `src/quota-service.mjs` | Language server quota polling (Windows only) |
| `src/launcher.mjs` | Orchestrates startup: server, CDP, Antigravity launch |

## Configuration

### Port

Default is `3001`. Change in `launcher.mjs`:
```javascript
const HTTP_PORT = 3001;
```

### PIN Authentication

The start script prompts for an optional 4–6 digit PIN. You can also set it via environment variable:

```bash
MOBILE_PIN=1234 node http-server.mjs
```

The admin panel shows whether authentication is currently active. To disable, click **Clear PIN** in Server settings.

### Remote Access

1. Install `cloudflared` (the launch script offers to do this automatically)
2. Go to Admin Panel → Remote Access
3. Click **Start Tunnel** — a random public URL and QR code appear
4. PIN authentication is required before the tunnel can be started
5. Enable **Auto-start** to launch the tunnel on every server boot

### Telegram Bot

1. Create a bot via [@BotFather](https://t.me/BotFather)
2. Get your chat ID from [@userinfobot](https://t.me/userinfobot)
3. Enter both in Admin Panel → Telegram tab → Save & Connect
4. Toggle notification types individually

### CDP

The start script launches Antigravity with `--remote-debugging-port=9222` automatically. If running Antigravity manually:

```bash
antigravity --remote-debugging-port=9222
```

## Project Structure

```
├── public/
│   ├── index.html              # Mobile dashboard
│   ├── minimal.html            # Lite mode (chat only)
│   ├── admin.html              # Admin panel
│   ├── manifest.json           # PWA manifest
│   ├── sw.js                   # Service worker
│   ├── css/
│   │   ├── variables.css       # CSS custom properties & theme variables
│   │   ├── layout.css          # Page layout, topbar, panels
│   │   ├── components.css      # Buttons, cards, forms, modals
│   │   ├── themes.css          # Theme overrides (dark, light, pastel, rainbow, slate)
│   │   ├── chat.css            # Chat message styling
│   │   ├── files.css           # File browser styling
│   │   ├── settings.css        # Settings panel styling
│   │   └── assist.css          # Supervisor assist tab styling
│   └── js/
│       ├── app.js              # App initialization
│       ├── api.js              # API client helpers
│       ├── websocket.js        # WebSocket connection manager
│       ├── navigation.js       # Tab navigation & routing
│       ├── chat.js             # Chat rendering & history
│       ├── chat-live.js        # Live chat streaming
│       ├── files.js            # File browser & syntax highlighting
│       ├── settings.js         # Settings panel logic
│       ├── theme.js            # Theme switching
│       ├── icons.js            # SVG icon helper
│       ├── assist.js           # Supervisor assist chat
│       └── task-queue.js       # Task queue UI
├── src/
│   ├── http-server.mjs         # API server & WebSocket bridge
│   ├── chat-stream.mjs         # Chat streaming + auto-accept + notifications
│   ├── cdp-client.mjs          # CDP client
│   ├── supervisor-service.mjs  # AI supervisor (Ollama-powered)
│   ├── ollama-client.mjs       # Ollama REST API wrapper
│   ├── telegram-bot.mjs        # Telegram integration
│   ├── tunnel.mjs              # Cloudflare tunnel manager
│   ├── config.mjs              # Config store
│   ├── quota-service.mjs       # Quota monitor
│   └── launcher.mjs            # Startup orchestrator
├── scripts/
│   ├── Start-Antigravity-Mobile.bat / .sh
│   └── Stop-Antigravity-Mobile.bat / .sh
├── data/                       # Runtime config & session data (gitignored)
├── screenshots/                # App screenshots for README
└── uploads/                    # User uploads (screenshots, etc.)
```

## Troubleshooting

| Problem | Fix |
|---------|-----|
| CDP Disconnected | Start Antigravity via the launch script, or add `--remote-debugging-port=9222` manually |
| Can't connect from phone | Same Wi-Fi network? Try PC's IP instead of `localhost`. Check firewall for port 3001 |
| Telegram silent | Verify token/chat ID, use the Test button, check that notification toggles are on |
| Auto-accept not clicking | Ensure CDP is connected (green indicator in admin). Check session logs for events |
| Quota not loading | Antigravity must be running and logged in. Windows only |
| PIN forgotten | Click **Clear PIN** in Admin → Server, or restart without PIN — auth resets each launch |
| Remote tunnel won't start | Ensure `cloudflared` is installed and PIN auth is enabled |
| Tunnel URL not showing | Check server console for errors. The URL may take a few seconds to appear |

For debug output, run the server directly:
```bash
node http-server.mjs 2>&1 | tee server.log
```

## License

MIT — see LICENSE.

## Acknowledgments

- Inspired by [Antigravity-Shit-Chat](https://github.com/gherghett/Antigravity-Shit-Chat) by gherghett
- Quota monitoring inspired by [Antigravity Cockpit](https://marketplace.visualstudio.com/items?itemName=jlcodes.antigravity-cockpit)
```

## File: payload\_DIR_IDENTITY.md
```
---
id: antigravity_mobile
type: plugin
owner: OA
registered_at: 2026-04-09T17:24:38.042446
tags: ["auto-cloned", "Mobile Dashboard", "Admin Panel", "Real-Time Chat", "oa-assimilated"]
---

# antigravity_mobile

## Assimilation Report
Antigravity Mobile is a mobile dashboard and admin panel for Antigravity IDE, offering real-time chat streaming, file browser with syntax highlighting, model quota monitoring, and various administrative features like Telegram notifications and remote access via Cloudflare tunnels.

## Application for OmniClaw
OmniClaw can integrate Antigravity Mobile's real-time chat streaming and file browser functionalities to enhance its own user interface for mobile devices. Additionally, OmniClaw could leverage the admin panel features such as Telegram notifications and remote access capabilities to improve monitoring and management of agents within the Multi-Agent AI OS.

```

## File: payload\public\admin.html
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin – Antigravity Mobile</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* ---- Dark theme (default) ---- */
        :root {
            --surface-0: #0B0E14;
            --surface-1: #0F1219;
            --surface-2: #141820;
            --surface-3: #1A1F2B;
            --surface-4: #212736;
            --sidebar-bg: #080A0F;
            --sidebar-text: #a0a4b8;
            --sidebar-active-bg: rgba(59, 130, 246, 0.12);
            --sidebar-active-text: #60A5FA;
            --border-subtle: rgba(100, 160, 255, 0.04);
            --border-default: rgba(100, 160, 255, 0.08);
            --border-strong: rgba(100, 160, 255, 0.14);
            --text-primary: #f0f1f5;
            --text-secondary: #a0a4b8;
            --text-muted: #5c6070;
            --accent: #3B82F6;
            --accent-hover: #60A5FA;
            --accent-muted: rgba(59, 130, 246, 0.12);
            --success: #34d399;
            --success-muted: rgba(52, 211, 153, 0.12);
            --error: #f87171;
            --error-muted: rgba(248, 113, 113, 0.12);
            --warning: #fbbf24;
            --scrollbar-thumb: rgba(255, 255, 255, 0.08);
        }

        /* ---- Light theme ---- */
        .theme-light {
            --surface-0: #f8f9fb;
            --surface-1: #ffffff;
            --surface-2: #ffffff;
            --surface-3: #f3f4f6;
            --surface-4: #e5e7eb;
            --sidebar-bg: #0F1219;
            --sidebar-text: #a0a4b8;
            --border-subtle: rgba(0, 0, 0, 0.06);
            --border-default: rgba(0, 0, 0, 0.08);
            --border-strong: rgba(0, 0, 0, 0.12);
            --text-primary: #111827;
            --text-secondary: #4b5563;
            --text-muted: #9ca3af;
            --accent: #3B82F6;
            --accent-hover: #2563eb;
            --accent-muted: rgba(59, 130, 246, 0.08);
            --success: #10b981;
            --success-muted: rgba(16, 185, 129, 0.08);
            --error: #ef4444;
            --error-muted: rgba(239, 68, 68, 0.08);
            --scrollbar-thumb: rgba(0, 0, 0, 0.12);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html,
        body {
            background: var(--surface-0);
            color: var(--text-primary);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            -webkit-font-smoothing: antialiased;
            height: 100vh;
            overflow: hidden;
        }

        ::-webkit-scrollbar {
            width: 5px;
        }

        ::-webkit-scrollbar-track {
            background: transparent;
        }

        ::-webkit-scrollbar-thumb {
            background: var(--scrollbar-thumb);
            border-radius: 3px;
        }

        /* ---- Shell ---- */
        .app-shell {
            display: flex;
            height: 100vh;
        }

        /* ---- Sidebar ---- */
        .sidebar {
            width: 200px;
            min-width: 200px;
            background: var(--sidebar-bg);
            display: flex;
            flex-direction: column;
            border-right: 1px solid rgba(255, 255, 255, 0.06);
        }

        .sidebar-brand {
            padding: 20px 16px 16px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        }

        .sidebar-brand-name {
            font-size: 14px;
            font-weight: 700;
            color: #f0f1f5;
            letter-spacing: -0.02em;
        }

        .sidebar-brand-sub {
            font-size: 10px;
            color: #5c6070;
            margin-top: 2px;
        }

        .sidebar-nav {
            flex: 1;
            padding: 12px 8px;
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .sidebar-link {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 9px 12px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 500;
            color: var(--sidebar-text);
            text-decoration: none;
            cursor: pointer;
            transition: all 0.12s;
            border: 1px solid transparent;
        }

        .sidebar-link:hover {
            background: rgba(255, 255, 255, 0.04);
            color: #f0f1f5;
        }

        .sidebar-link.active {
            background: var(--sidebar-active-bg);
            color: var(--sidebar-active-text);
            border-color: rgba(59, 130, 246, 0.2);
        }

        .sidebar-link svg {
            width: 16px;
            height: 16px;
            opacity: 0.5;
            flex-shrink: 0;
        }

        .sidebar-link.active svg {
            opacity: 1;
        }

        .sidebar-section-title {
            font-size: 10px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #5c6070;
            padding: 16px 12px 6px;
        }

        .sidebar-footer {
            padding: 12px 16px;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
            font-size: 11px;
            color: #5c6070;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .sidebar-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--success);
            box-shadow: 0 0 6px var(--success);
        }

        /* ---- Main ---- */
        .main-content {
            flex: 1;
            overflow-y: auto;
            padding: 28px 36px 48px;
        }

        /* ---- Page header ---- */
        .page-header {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            margin-bottom: 24px;
        }

        .page-title {
            font-size: 22px;
            font-weight: 700;
            letter-spacing: -0.03em;
        }

        .page[data-page] {
            display: none;
        }

        .page[data-page].active {
            display: block;
        }

        .page-subtitle {
            font-size: 13px;
            color: var(--text-muted);
            margin-top: 2px;
        }

        .auto-badge {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 3px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 600;
            background: var(--accent-muted);
            color: var(--accent);
            margin-left: 12px;
            vertical-align: middle;
        }

        /* ---- Stat grid (4 columns) ---- */
        .stat-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin-bottom: 20px;
        }

        .stat-card {
            background: var(--surface-1);
            border: 1px solid var(--border-default);
            border-radius: 10px;
            padding: 18px 20px;
        }

        .stat-value {
            font-size: 22px;
            font-weight: 700;
            letter-spacing: -0.02em;
            color: var(--text-primary);
        }

        .stat-value.ok {
            color: var(--success);
        }

        .stat-value.err {
            color: var(--error);
        }

        .stat-label {
            font-size: 12px;
            color: var(--text-muted);
            margin-top: 4px;
        }

        /* ---- Section grid ---- */
        .section-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 20px;
        }

        .section-grid.full {
            grid-template-columns: 1fr;
        }

        /* ---- Card ---- */
        .card {
            background: var(--surface-1);
            border: 1px solid var(--border-default);
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 20px;
        }

        .card.flush {
            margin-bottom: 0;
        }

        .card-inner {
            padding: 20px;
        }

        .section-title {
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: var(--text-muted);
            margin-bottom: 16px;
        }

        /* ---- Status row ---- */
        .status-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 6px 0;
        }

        .status-name {
            font-size: 13px;
            font-weight: 500;
            color: var(--text-primary);
        }

        .status-indicator {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 12px;
            font-weight: 600;
        }

        .status-indicator .dot {
            display: inline-block;
            width: 7px;
            height: 7px;
            border-radius: 50%;
        }

        .status-indicator.running .dot {
            background: var(--success);
            box-shadow: 0 0 6px var(--success);
        }

        .status-indicator.running {
            color: var(--success);
        }

        .status-indicator.stopped .dot {
            background: var(--error);
            box-shadow: 0 0 6px var(--error);
        }

        .status-indicator.stopped {
            color: var(--error);
        }

        /* ---- env grid ---- */
        .env-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
            gap: 12px;
        }

        .env-item .env-label {
            font-size: 10px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
        }

        .env-item .env-value {
            font-size: 13px;
            font-weight: 700;
            color: var(--text-primary);
            margin-top: 2px;
            word-break: break-all;
        }

        /* ---- Form controls ---- */
        .form-group {
            margin-bottom: 16px;
        }

        .form-group:last-child {
            margin-bottom: 0;
        }

        .form-label {
            display: block;
            font-size: 12px;
            font-weight: 600;
            color: var(--text-secondary);
            margin-bottom: 6px;
        }

        .form-hint {
            font-size: 11px;
            color: var(--text-muted);
            margin-top: 4px;
        }

        .input,
        .select {
            width: 100%;
            padding: 9px 12px;
            background: var(--surface-3);
            border: 1px solid var(--border-default);
            border-radius: 8px;
            color: var(--text-primary);
            font-size: 13px;
            font-family: inherit;
            outline: none;
            transition: border-color 0.15s, box-shadow 0.15s;
        }

        .input:focus,
        .select:focus {
            border-color: var(--accent);
            box-shadow: 0 0 0 3px var(--accent-muted);
        }

        .input::placeholder {
            color: var(--text-muted);
        }

        .select {
            appearance: none;
            cursor: pointer;
        }

        /* ---- Toggle ---- */
        .toggle-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid var(--border-subtle);
        }

        .toggle-row:last-child {
            border-bottom: none;
        }

        .toggle-label {
            font-size: 13px;
            font-weight: 500;
            color: var(--text-primary);
        }

        .toggle-desc {
            font-size: 11px;
            color: var(--text-muted);
            margin-top: 1px;
        }

        .toggle {
            position: relative;
            width: 36px;
            height: 20px;
            flex-shrink: 0;
        }

        .toggle input {
            opacity: 0;
            width: 0;
            height: 0;
            position: absolute;
        }

        .toggle-track {
            position: absolute;
            inset: 0;
            background: var(--surface-4);
            border-radius: 10px;
            cursor: pointer;
            transition: background 0.2s;
            border: 1px solid var(--border-default);
        }

        .toggle-track::after {
            content: '';
            position: absolute;
            top: 2px;
            left: 2px;
            width: 14px;
            height: 14px;
            border-radius: 50%;
            background: var(--text-muted);
            transition: transform 0.2s, background 0.2s;
        }

        .toggle input:checked+.toggle-track {
            background: var(--accent);
            border-color: var(--accent);
        }

        .toggle input:checked+.toggle-track::after {
            transform: translateX(16px);
            background: white;
        }

        /* ---- Buttons ---- */
        .btn {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 500;
            font-family: inherit;
            border: 1px solid transparent;
            cursor: pointer;
            transition: all 0.15s;
        }

        .btn-primary {
            background: var(--accent);
            color: white;
            border-color: var(--accent);
        }

        .btn-primary:hover {
            background: var(--accent-hover);
        }

        .btn-secondary {
            background: var(--surface-3);
            color: var(--text-secondary);
            border-color: var(--border-default);
        }

        .btn-secondary:hover {
            background: var(--surface-4);
            color: var(--text-primary);
        }

        .btn-sm {
            padding: 5px 10px;
            font-size: 12px;
        }

        .btn-row {
            display: flex;
            gap: 8px;
        }

        /* ---- Toast ---- */
        .toast {
            position: fixed;
            bottom: 24px;
            left: 50%;
            transform: translateX(-50%) translateY(80px);
            padding: 10px 24px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: 500;
            z-index: 999;
            transition: transform 0.3s cubic-bezier(.4, 0, .2, 1);
            pointer-events: none;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .toast.show {
            transform: translateX(-50%) translateY(0);
        }

        .toast.success {
            background: var(--success-muted);
            color: var(--success);
            border: 1px solid rgba(16, 185, 129, 0.2);
        }

        .toast.error {
            background: var(--error-muted);
            color: var(--error);
            border: 1px solid rgba(239, 68, 68, 0.2);
        }
    </style>
</head>

<body>
    <div class="app-shell">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="sidebar-brand">
                <div class="sidebar-brand-name">Antigravity Mobile</div>
                <div class="sidebar-brand-sub">Admin Panel</div>
            </div>
            <nav class="sidebar-nav">
                <a class="sidebar-link active" onclick="switchPage('dashboard', this)">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="7" height="7"></rect>
                        <rect x="14" y="3" width="7" height="7"></rect>
                        <rect x="14" y="14" width="7" height="7"></rect>
                        <rect x="3" y="14" width="7" height="7"></rect>
                    </svg>
                    <span>Dashboard</span>
                </a>
                <div class="sidebar-section-title">Configure</div>
                <a class="sidebar-link" onclick="switchPage('server', this)">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="2" y="2" width="20" height="8" rx="2"></rect>
                        <rect x="2" y="14" width="20" height="8" rx="2"></rect>
                        <circle cx="6" cy="6" r="1"></circle>
                        <circle cx="6" cy="18" r="1"></circle>
                    </svg>
                    <span>Server</span>
                </a>
                <a class="sidebar-link" onclick="switchPage('telegram', this)">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                    </svg>
                    <span>Telegram</span>
                </a>
                <a class="sidebar-link" onclick="switchPage('devices', this)">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="2" y="3" width="20" height="14" rx="2"></rect>
                        <line x1="8" y1="21" x2="16" y2="21"></line>
                        <line x1="12" y1="17" x2="12" y2="21"></line>
                    </svg>
                    <span>Devices</span>
                </a>
                <a class="sidebar-link" onclick="switchPage('commands', this)">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <polyline points="4 17 10 11 4 5"></polyline>
                        <line x1="12" y1="19" x2="20" y2="19"></line>
                    </svg>
                    <span>Commands</span>
                </a>
                <a class="sidebar-link" onclick="switchPage('mobile', this)">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="5" y="2" width="14" height="20" rx="2"></rect>
                        <line x1="12" y1="18" x2="12" y2="18"></line>
                    </svg>
                    <span>Mobile</span>
                </a>
                <a class="sidebar-link" onclick="switchPage('customize', this)">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path
                            d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10c.83 0 1.5-.67 1.5-1.5 0-.39-.15-.74-.39-1.01-.23-.26-.38-.61-.38-1 0-.83.67-1.5 1.5-1.5H16c3.31 0 6-2.69 6-6 0-4.97-4.48-9-10-9z"
                            fill="none"></path>
                        <circle cx="7.5" cy="11.5" r="1.5" fill="currentColor" stroke="none"></circle>
                        <circle cx="10.5" cy="7.5" r="1.5" fill="currentColor" stroke="none"></circle>
                        <circle cx="15.5" cy="7.5" r="1.5" fill="currentColor" stroke="none"></circle>
                        <circle cx="17.5" cy="11.5" r="1.5" fill="currentColor" stroke="none"></circle>
                    </svg>
                    <span>Customize</span>
                </a>
                <a class="sidebar-link" onclick="switchPage('remote', this)">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="10"></circle>
                        <line x1="2" y1="12" x2="22" y2="12"></line>
                        <path
                            d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z">
                        </path>
                    </svg>
                    <span>Remote</span>
                </a>
                <a class="sidebar-link" onclick="switchPage('logs', this)">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                        <line x1="16" y1="13" x2="8" y2="13"></line>
                        <line x1="16" y1="17" x2="8" y2="17"></line>
                    </svg>
                    <span>Logs</span>
                </a>

                <a class="sidebar-link" onclick="switchPage('screenshots', this)">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2"></rect>
                        <circle cx="8.5" cy="8.5" r="1.5"></circle>
                        <polyline points="21 15 16 10 5 21"></polyline>
                    </svg>
                    <span>Screenshots</span>
                </a>
                <a class="sidebar-link" onclick="switchPage('analytics', this)">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="18" y1="20" x2="18" y2="10"></line>
                        <line x1="12" y1="20" x2="12" y2="4"></line>
                        <line x1="6" y1="20" x2="6" y2="14"></line>
                    </svg>
                    <span>Analytics</span>
                </a>
                <a class="sidebar-link" onclick="switchPage('supervisor', this)">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path
                            d="M12 2a9 9 0 0 0-9 9c0 3.88 2.46 7.18 5.9 8.44.13-.95.5-2.06 1.1-2.94a5 5 0 0 1 4-8.5 5 5 0 0 1 4 8.5c.6.88.97 1.99 1.1 2.94A9.01 9.01 0 0 0 21 11a9 9 0 0 0-9-9z">
                        </path>
                        <path d="M12 18v4"></path>
                        <circle cx="12" cy="11" r="2"></circle>
                    </svg>
                    <span>Supervisor</span>
                </a>
                <div class="sidebar-section-title">Links</div>
                <a class="sidebar-link" href="/" target="_blank">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                        <polyline points="15 3 21 3 21 9"></polyline>
                        <line x1="10" y1="14" x2="21" y2="3"></line>
                    </svg>
                    <span>Open Mobile UI</span>
                </a>
            </nav>
            <div class="sidebar-footer">
                <div class="sidebar-dot" id="sidebarDot"></div>
                <span id="sidebarStatus">Loading…</span>
            </div>
        </aside>

        <!-- Main -->
        <main class="main-content">

            <!-- ==================== PAGE: Dashboard ==================== -->
            <div class="page active" data-page="dashboard">
                <div class="page-header">
                    <div>
                        <div class="page-title">Dashboard <span class="auto-badge" id="autoRefreshBadge">Auto-refresh:
                                ON</span></div>
                        <div class="page-subtitle">Server overview</div>
                    </div>
                    <button class="btn btn-secondary" onclick="toggleTheme()" id="themeBtn" title="Toggle theme"
                        id="themeIcon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
                        </svg></button>
                </div>

                <div class="stat-grid">
                    <div class="stat-card">
                        <div class="stat-value" id="statHealth">—</div>
                        <div class="stat-label">Status</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="statUptime">—</div>
                        <div class="stat-label">Uptime</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="statClients">—</div>
                        <div class="stat-label">Clients</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="statPort">—</div>
                        <div class="stat-label">Port</div>
                    </div>
                </div>

                <div class="section-grid">
                    <div class="card flush">
                        <div class="card-inner">
                            <div class="section-title">Connections</div>
                            <div class="status-row">
                                <div class="status-name">CDP</div>
                                <div class="status-indicator" id="cdpIndicator"><span class="dot"></span> —</div>
                            </div>
                            <div class="status-row" style="margin-top: 4px;">
                                <div class="status-name">Telegram</div>
                                <div class="status-indicator" id="tgIndicator"><span class="dot"></span> —</div>
                            </div>
                            <div class="status-row"
                                style="margin-top: 10px; padding-top: 10px; border-top: 1px solid var(--border);">
                                <div class="status-name"><span
                                        style="display:inline-flex;vertical-align:middle;margin-right:4px"><svg
                                            width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                            <rect x="3" y="11" width="18" height="10" rx="2" />
                                            <circle cx="12" cy="5" r="2" />
                                            <path d="M12 7v4" />
                                            <line x1="8" y1="16" x2="8" y2="16" />
                                            <line x1="16" y1="16" x2="16" y2="16" />
                                        </svg></span>Auto-Accept</div>
                                <label
                                    style="position:relative;display:inline-block;width:44px;height:24px;cursor:pointer;">
                                    <input type="checkbox" id="autoAcceptToggle" onchange="toggleAutoAccept()"
                                        style="opacity:0;width:0;height:0;">
                                    <span
                                        style="position:absolute;inset:0;background:var(--border);border-radius:12px;transition:.3s;"></span>
                                    <span id="autoAcceptKnob"
                                        style="position:absolute;top:2px;left:2px;width:20px;height:20px;background:#fff;border-radius:50%;transition:.3s;"></span>
                                </label>
                            </div>
                        </div>
                    </div>
                    <div class="card flush">
                        <div class="card-inner">
                            <div class="section-title">Environment</div>
                            <div class="env-grid">
                                <div class="env-item">
                                    <div class="env-label">Platform</div>
                                    <div class="env-value">Node.js</div>
                                </div>
                                <div class="env-item">
                                    <div class="env-label">Auth</div>
                                    <div class="env-value" id="envAuth">—</div>
                                </div>
                                <div class="env-item">
                                    <div class="env-label">Interface</div>
                                    <div class="env-value">0.0.0.0</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Activity Feed -->
                <div class="card" style="margin-top: 16px;">
                    <div class="card-inner">
                        <div class="section-title"
                            style="display: flex; justify-content: space-between; align-items: center;">
                            <span><span style="display:inline-flex;vertical-align:middle;margin-right:4px"><svg
                                        width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <line x1="18" y1="20" x2="18" y2="10" />
                                        <line x1="12" y1="20" x2="12" y2="4" />
                                        <line x1="6" y1="20" x2="6" y2="14" />
                                    </svg></span>Activity Feed</span>
                            <button class="btn btn-secondary btn-sm" onclick="loadEvents()">Refresh</button>
                        </div>
                        <div id="activityFeed" style="max-height: 300px; overflow-y: auto; font-size: 13px;">Loading...
                        </div>
                    </div>
                </div>


            </div>

            <!-- ==================== PAGE: Server ==================== -->
            <div class="page" data-page="server">
                <div class="page-header">
                    <div>
                        <div class="page-title">Server</div>
                        <div class="page-subtitle">HTTP server configuration</div>
                    </div>
                    <div class="btn-row">
                        <button class="btn btn-secondary" onclick="loadConfigFromServer()">Reset</button>
                        <button class="btn btn-primary" onclick="saveAll()" id="saveBtn">Save</button>
                    </div>
                </div>
                <div class="card">
                    <div class="card-inner">
                        <div class="form-group">
                            <label class="form-label">Port</label>
                            <input class="input" type="number" id="serverPort" min="1000" max="65535"
                                style="width: 120px;">
                            <span class="form-hint">Requires server restart to take effect</span>
                        </div>
                        <div class="form-group">
                            <label class="form-label">PIN (leave empty to disable auth)</label>
                            <div style="display:flex;align-items:center;gap:8px;">
                                <input class="input" type="password" id="serverPin" placeholder="4–6 digit PIN"
                                    maxlength="6" pattern="[0-9]*" inputmode="numeric" style="width: 200px;"
                                    oninput="this.value=this.value.replace(/[^0-9]/g,'').slice(0,6); pinFieldTouched=true;">
                                <button class="btn btn-secondary btn-sm" id="clearPinBtn" style="display:none;"
                                    onclick="clearPin()">Clear PIN</button>
                            </div>
                            <div id="pinStatus" style="margin-top:6px;font-size:12px;"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ==================== PAGE: Telegram ==================== -->
            <div class="page" data-page="telegram">
                <div class="page-header">
                    <div>
                        <div class="page-title">Telegram Bot</div>
                        <div class="page-subtitle">Notifications &amp; commands via Telegram</div>
                    </div>
                    <div class="btn-row">
                        <button class="btn btn-secondary" onclick="loadConfigFromServer()">Reset</button>
                        <button class="btn btn-primary" onclick="saveAll()">Save</button>
                    </div>
                </div>
                <div class="card">
                    <div class="card-inner">
                        <div class="toggle-row" style="padding-top: 0;">
                            <div>
                                <div class="toggle-label">Enable Bot</div>
                                <div class="toggle-desc">Send notifications and handle commands via Telegram</div>
                            </div>
                            <label class="toggle">
                                <input type="checkbox" id="telegramEnabled" onchange="toggleTelegram()">
                                <span class="toggle-track"></span>
                            </label>
                        </div>
                        <div id="telegramFields" style="margin-top: 12px;">
                            <div class="form-group">
                                <label class="form-label">Bot Token</label>
                                <input class="input" type="password" id="botToken" placeholder="123456:ABC-DEF…">
                                <span class="form-hint">Get from @BotFather on Telegram</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label">Chat ID</label>
                                <input class="input" type="text" id="chatId" placeholder="Your user or group chat ID">
                                <span class="form-hint">Send /start to your bot to get your Chat ID</span>
                            </div>
                            <div class="btn-row" style="margin-bottom: 16px;">
                                <button class="btn btn-secondary btn-sm" onclick="testTelegram()"><span
                                        style="display:inline-flex;vertical-align:middle"><svg width="14" height="14"
                                            viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                            stroke-linecap="round" stroke-linejoin="round">
                                            <path d="M9 3h6v7l5 8H4l5-8V3z" />
                                            <line x1="9" y1="3" x2="15" y2="3" />
                                        </svg></span> Send Test
                                    Message</button>
                            </div>
                            <label class="form-label">Notification Types</label>
                            <div class="toggle-row">
                                <div>
                                    <div class="toggle-label">Process Complete</div>
                                    <div class="toggle-desc">When a task finishes</div>
                                </div>
                                <label class="toggle"><input type="checkbox" id="notifComplete" checked><span
                                        class="toggle-track"></span></label>
                            </div>
                            <div class="toggle-row">
                                <div>
                                    <div class="toggle-label">Errors</div>
                                    <div class="toggle-desc">When errors are detected</div>
                                </div>
                                <label class="toggle"><input type="checkbox" id="notifError" checked><span
                                        class="toggle-track"></span></label>
                            </div>
                            <div class="toggle-row">
                                <div>
                                    <div class="toggle-label">Input Needed</div>
                                    <div class="toggle-desc">When buttons or clicks are required</div>
                                </div>
                                <label class="toggle"><input type="checkbox" id="notifInput" checked><span
                                        class="toggle-track"></span></label>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ==================== PAGE: Mobile ==================== -->
            <div class="page" data-page="mobile">
                <div class="page-header">
                    <div>
                        <div class="page-title">Mobile Dashboard</div>
                        <div class="page-subtitle">Mobile UI configuration</div>
                    </div>
                    <div class="btn-row">
                        <button class="btn btn-secondary" onclick="loadConfigFromServer()">Reset</button>
                        <button class="btn btn-primary" onclick="saveAll()">Save</button>
                    </div>
                </div>
                <div class="card">
                    <div class="card-inner">
                        <div class="form-group">
                            <label class="form-label">Default Refresh Interval (ms)</label>
                            <input class="input" type="number" id="refreshInterval" min="500" max="10000" step="100"
                                style="width: 120px;">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Default Theme</label>
                            <select class="select" id="dashTheme" style="width: 160px;">
                                <option value="dark">Dark</option>
                                <option value="light">Light</option>
                                <option value="pastel">Pastel</option>
                                <option value="rainbow">Rainbow</option>
                                <option value="slate">Slate</option>
                            </select>
                        </div>
                    </div>
                </div>
                <!-- QR Code Pairing -->
                <div class="card" style="margin-top: 16px;">
                    <div class="card-inner" style="text-align: center;">
                        <div class="section-title"><span
                                style="display:inline-flex;vertical-align:middle;margin-right:4px"><svg width="16"
                                    height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="5" y="2" width="14" height="20" rx="2" ry="2" />
                                    <line x1="12" y1="18" x2="12.01" y2="18" />
                                </svg></span>QR Code Pairing</div>
                        <div style="color: var(--text-muted); font-size: 13px; margin-bottom: 12px;">Scan with your
                            phone to open the mobile dashboard</div>
                        <div id="qrCodeContainer"
                            style="display: inline-block; padding: 16px; background: #fff; border-radius: 8px;">
                            <canvas id="qrCanvas" width="160" height="160"></canvas>
                        </div>
                        <div id="qrUrl" style="margin-top: 8px; font-size: 12px; color: var(--text-muted);"></div>
                    </div>
                </div>
            </div>

            <!-- ==================== PAGE: Devices ==================== -->
            <div class="page" data-page="devices">
                <div class="page-header">
                    <div>
                        <div class="page-title">Devices</div>
                        <div class="page-subtitle">Manage Antigravity instances</div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-inner">
                        <div class="section-title">Connected Devices</div>
                        <div id="deviceList" style="margin-bottom: 16px;">Loading...</div>
                        <div style="border-top: 1px solid var(--border); padding-top: 16px;">
                            <div class="section-title">Add Device</div>
                            <div style="display: flex; gap: 8px; align-items: flex-end; flex-wrap: wrap;">
                                <div class="form-group" style="margin: 0;">
                                    <label class="form-label">Name</label>
                                    <input class="input" type="text" id="newDeviceName" placeholder="My Antigravity"
                                        style="width: 160px;">
                                </div>
                                <div class="form-group" style="margin: 0;">
                                    <label class="form-label">CDP Port</label>
                                    <input class="input" type="number" id="newDevicePort" placeholder="9223" min="1000"
                                        max="65535" style="width: 100px;">
                                </div>
                                <button class="btn btn-primary btn-sm" onclick="addDevice()">Add</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ==================== PAGE: Commands ==================== -->
            <div class="page" data-page="commands">
                <div class="page-header">
                    <div>
                        <div class="page-title">Quick Commands</div>
                        <div class="page-subtitle">One-click prompts for the agent</div>
                    </div>
                    <button class="btn btn-primary btn-sm" onclick="addCommand()">+ Add Command</button>
                </div>
                <div id="commandList">Loading...</div>
            </div>

            <!-- ==================== PAGE: Logs ==================== -->
            <div class="page" data-page="logs">
                <div class="page-header">
                    <div>
                        <div class="page-title">Session Logs</div>
                        <div class="page-subtitle">View and download interaction logs</div>
                    </div>
                    <div style="display:flex;gap:8px;">
                        <button id="pauseLoggingBtn" class="btn btn-secondary btn-sm" onclick="toggleLogging()"><span
                                style="display:inline-flex;vertical-align:middle"><svg width="14" height="14"
                                    viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="6" y="4" width="4" height="16" />
                                    <rect x="14" y="4" width="4" height="16" />
                                </svg></span> Pause</button>
                        <button class="btn btn-secondary btn-sm" onclick="clearAllLogs()"
                            style="background: var(--error); border-color: var(--error);"><span
                                style="display:inline-flex;vertical-align:middle"><svg width="14" height="14"
                                    viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="3 6 5 6 21 6" />
                                    <path
                                        d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" />
                                </svg></span> Clear All</button>
                    </div>
                </div>
                <div id="sessionList">Loading...</div>
                <div id="sessionViewer" style="display:none; margin-top: 16px;">
                    <div class="card">
                        <div class="card-inner">
                            <div class="section-title"
                                style="display:flex;justify-content:space-between;align-items:center;">
                                <span id="sessionViewerTitle">Session Events</span>
                                <button class="btn btn-secondary btn-sm"
                                    onclick="document.getElementById('sessionViewer').style.display='none'">Close</button>
                            </div>
                            <div id="sessionEvents" style="max-height: 400px; overflow-y: auto; font-size: 13px;"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ==================== PAGE: Analytics ==================== -->
            <div class="page" data-page="analytics">
                <div class="page-header">
                    <div>
                        <div class="page-title">Usage Analytics</div>
                        <div class="page-subtitle">Metrics and activity trends</div>
                    </div>
                    <button class="btn btn-secondary btn-sm" onclick="loadAnalytics()">Refresh</button>
                </div>
                <div
                    style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; margin-bottom: 16px;">

                    <div class="card">
                        <div class="card-inner" style="text-align:center;">
                            <div style="font-size:28px;font-weight:700;color:var(--primary);" id="statScreenshots">0
                            </div>
                            <div style="font-size:12px;color:var(--text-muted);">Screenshots</div>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card-inner" style="text-align:center;">
                            <div style="font-size:28px;font-weight:700;color:#f43f5e;" id="statErrors">0</div>
                            <div style="font-size:12px;color:var(--text-muted);">Errors</div>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card-inner" style="text-align:center;">
                            <div style="font-size:28px;font-weight:700;color:var(--primary);" id="statCommands">0</div>
                            <div style="font-size:12px;color:var(--text-muted);">Commands</div>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card-inner" style="text-align:center;">
                            <div style="font-size:28px;font-weight:700;color:var(--text);" id="analyticsUptime">—</div>
                            <div style="font-size:12px;color:var(--text-muted);">Active Since</div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-inner">
                        <div class="section-title"><span
                                style="display:inline-flex;vertical-align:middle;margin-right:4px"><svg width="16"
                                    height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="23 6 13.5 15.5 8.5 10.5 1 18" />
                                    <polyline points="17 6 23 6 23 12" />
                                </svg></span>Daily Activity (last 7 days)</div>
                        <canvas id="analyticsChart" width="600" height="200" style="width:100%;height:200px;"></canvas>
                    </div>
                </div>
            </div>



            <!-- ==================== PAGE: Screenshots ==================== -->
            <div class="page" data-page="screenshots">
                <div class="page-header">
                    <div>
                        <div class="page-title">Screenshot Gallery</div>
                        <div class="page-subtitle">Auto-captured screenshots timeline</div>
                    </div>
                    <div style="display:flex;gap:8px;">
                        <button class="btn btn-secondary btn-sm" id="screenshotToggleBtn"
                            onclick="toggleScreenshots()"><span style="display:inline-flex;vertical-align:middle"><svg
                                    width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="6" y="4" width="4" height="16" />
                                    <rect x="14" y="4" width="4" height="16" />
                                </svg></span> Disable</button>
                        <button class="btn btn-secondary btn-sm" onclick="clearScreenshots()"
                            style="color:#f43f5e;"><span style="display:inline-flex;vertical-align:middle"><svg
                                    width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="3 6 5 6 21 6" />
                                    <path
                                        d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" />
                                </svg></span> Clear All</button>
                        <button class="btn btn-secondary btn-sm" onclick="loadScreenshotGallery()">Refresh</button>
                    </div>
                </div>
                <div id="screenshotGallery"
                    style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;">Loading...
                </div>
                <div id="screenshotFullview"
                    style="display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.85);z-index:1000;cursor:pointer;padding:20px;"
                    onclick="this.style.display='none'">
                    <img id="screenshotFullImg"
                        style="max-width:100%;max-height:100%;display:block;margin:auto;border-radius:8px;">
                </div>
            </div>

            <!-- Customize Page -->
            <div class="page" data-page="customize">
                <div class="page-header">
                    <div>
                        <div class="page-title">Customize</div>
                        <div class="page-subtitle">Mobile dashboard appearance settings</div>
                    </div>
                    <div class="btn-row">
                        <button class="btn btn-primary" onclick="saveCustomize()" id="saveCustomizeBtn">Save</button>
                    </div>
                </div>

                <div class="card">
                    <div class="card-inner">
                        <div class="form-group" style="display:flex;align-items:center;justify-content:space-between;">
                            <div>
                                <label class="form-label" style="margin-bottom:4px;">Show Quick Actions</label>
                                <span class="form-hint">Continue, Yes, No, Stop, Help buttons above the input
                                    field</span>
                            </div>
                            <div style="position:relative;width:48px;height:26px;cursor:pointer;flex-shrink:0;">
                                <input type="checkbox" id="showQuickActions" checked style="display:none;">
                                <div id="quickActionsTrack"
                                    style="position:absolute;inset:0;border-radius:13px;background:#3b82f6;transition:background .2s;border:1px solid rgba(255,255,255,0.15);"
                                    onclick="document.getElementById('showQuickActions').checked=!document.getElementById('showQuickActions').checked;updateCustomizeVisuals();scheduleCustomizeSave();">
                                </div>
                                <div id="quickActionsKnob"
                                    style="position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#fff;transition:transform .2s;transform:translateX(22px);pointer-events:none;box-shadow:0 1px 3px rgba(0,0,0,0.3);">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card" style="margin-top:16px;">
                    <div class="card-inner">
                        <div class="form-group">
                            <label class="form-label" style="margin-bottom:4px;">Layout Style</label>
                            <span class="form-hint">Choose how the mobile dashboard navigation is displayed</span>
                        </div>
                        <div style="display:flex;gap:12px;margin-top:12px;">
                            <div id="navModeSidebar" onclick="selectNavMode('sidebar')"
                                style="flex:1;padding:16px;border:2px solid var(--accent-primary);border-radius:12px;cursor:pointer;text-align:center;background:rgba(14,165,233,0.08);transition:all .2s;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"
                                    style="width:32px;height:32px;margin:0 auto 8px;">
                                    <rect x="3" y="3" width="5" height="18" rx="1"></rect>
                                    <rect x="10" y="3" width="11" height="18" rx="1"></rect>
                                </svg>
                                <div style="font-weight:600;font-size:14px;">Sidebar</div>
                                <div style="font-size:11px;opacity:.6;margin-top:4px;">Side navigation panel</div>
                            </div>
                            <div id="navModeTopbar" onclick="selectNavMode('topbar')"
                                style="flex:1;padding:16px;border:2px solid var(--border);border-radius:12px;cursor:pointer;text-align:center;transition:all .2s;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"
                                    style="width:32px;height:32px;margin:0 auto 8px;">
                                    <rect x="3" y="3" width="18" height="5" rx="1"></rect>
                                    <rect x="3" y="10" width="18" height="11" rx="1"></rect>
                                </svg>
                                <div style="font-weight:600;font-size:14px;">Top Bar</div>
                                <div style="font-size:11px;opacity:.6;margin-top:4px;">Floating top navigation</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card" style="margin-top:16px;">
                    <div class="card-inner">
                        <div class="form-group" style="display:flex;align-items:center;justify-content:space-between;">
                            <div>
                                <label class="form-label" style="margin-bottom:4px;">Show Assist Tab</label>
                                <span class="form-hint">Show the Supervisor Assist tab in the mobile dashboard
                                    sidebar/topbar</span>
                            </div>
                            <div style="position:relative;width:48px;height:26px;cursor:pointer;flex-shrink:0;">
                                <input type="checkbox" id="showAssistTab" style="display:none;">
                                <div id="assistTabTrack"
                                    style="position:absolute;inset:0;border-radius:13px;background:#4b5563;transition:background .2s;border:1px solid rgba(255,255,255,0.15);"
                                    onclick="document.getElementById('showAssistTab').checked=!document.getElementById('showAssistTab').checked;updateCustomizeVisuals();scheduleCustomizeSave();">
                                </div>
                                <div id="assistTabKnob"
                                    style="position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#fff;transition:transform .2s;transform:translateX(0);pointer-events:none;box-shadow:0 1px 3px rgba(0,0,0,0.3);">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ==================== PAGE: Supervisor ==================== -->
            <div class="page" data-page="supervisor">
                <div class="page-header">
                    <div>
                        <div class="page-title" style="display:flex;align-items:center;gap:8px;"><span
                                id="supervisorTitleIcon"></span> Supervisor</div>
                        <div class="page-subtitle">Ollama-powered autonomous agent overseer</div>
                    </div>
                    <div class="btn-row">
                        <button class="btn btn-secondary" onclick="loadSupervisorStatus()">Refresh</button>
                        <button class="btn btn-primary" onclick="saveSupervisor()">Save</button>
                    </div>
                </div>

                <!-- Status -->
                <div class="stat-grid" style="grid-template-columns: repeat(3, 1fr);">
                    <div class="stat-card">
                        <div class="stat-value" id="supervisorStatEnabled">—</div>
                        <div class="stat-label">Status</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="supervisorStatOllama">—</div>
                        <div class="stat-label">Ollama</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="supervisorStatActions">—</div>
                        <div class="stat-label">Actions/min</div>
                    </div>
                </div>

                <!-- Toggle + Provider -->
                <div class="card">
                    <div class="card-inner">
                        <div class="toggle-row" style="padding-top: 0;">
                            <div>
                                <div class="toggle-label">Enable Supervisor</div>
                                <div class="toggle-desc">Monitor the agent and take autonomous actions via Ollama</div>
                            </div>
                            <label class="toggle">
                                <input type="checkbox" id="supervisorEnabled" onchange="toggleSupervisor()">
                                <span class="toggle-track"></span>
                            </label>
                        </div>
                        <div class="toggle-row">
                            <div>
                                <div class="toggle-label">Disable IDE Injects</div>
                                <div class="toggle-desc">Keep supervisor monitoring but block it from typing or clicking
                                    in the IDE</div>
                            </div>
                            <label class="toggle">
                                <input type="checkbox" id="supervisorDisableInjects"
                                    onchange="toggleSupervisorInjects()">
                                <span class="toggle-track"></span>
                            </label>
                        </div>
                        <div style="margin-top: 16px;">
                            <div class="form-group">
                                <label class="form-label">Provider</label>
                                <select class="select" id="supervisorProvider" style="width: 200px;">
                                    <option value="ollama" selected>Ollama (Local)</option>
                                </select>
                                <span class="form-hint">More providers coming soon</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label">Endpoint URL</label>
                                <div style="display:flex;gap:8px;align-items:center;">
                                    <input class="input" type="text" id="supervisorEndpoint"
                                        placeholder="http://localhost:11434" style="flex:1;">
                                    <button class="btn btn-secondary btn-sm"
                                        onclick="testOllamaConnection()">Test</button>
                                </div>
                                <span class="form-hint" id="ollamaTestResult"></span>
                            </div>
                            <div class="form-group">
                                <label class="form-label">Model</label>
                                <div style="display:flex;gap:8px;align-items:center;">
                                    <input class="input" type="text" id="supervisorModel" placeholder="llama3"
                                        style="flex:1;">
                                    <span class="form-hint" id="ollamaModelHint"
                                        style="margin:0;white-space:nowrap;"></span>
                                </div>
                                <span class="form-hint">Enter the Ollama model name (e.g. llama3, mistral,
                                    codellama)</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label">Max Actions/Minute</label>
                                <input class="input" type="number" id="supervisorRateLimit" min="1" max="60" value="10"
                                    style="width: 120px;">
                                <span class="form-hint">Rate limit to prevent runaway loops</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label">Context Window (tokens)</label>
                                <input class="input" type="number" id="supervisorContextWindow" min="2048" max="131072"
                                    value="8192" step="1024" style="width: 160px;">
                                <span class="form-hint">num_ctx for Ollama — higher = more context but more VRAM
                                    (default: 8192)</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Project Context -->
                <div class="card">
                    <div class="card-inner">
                        <div class="section-title">Project Context (Optional)</div>
                        <div class="form-group">
                            <textarea class="input" id="supervisorContext" rows="5"
                                placeholder="Describe your project, goals, and any special instructions for the supervisor..."
                                style="resize: vertical; min-height: 100px;"></textarea>
                            <span class="form-hint">This context is included in every supervisor decision. E.g.
                                &quot;We're building a React app. Don't accept any destructive commands. Alert me for
                                any database changes.&quot;</span>
                        </div>
                        <button class="btn btn-secondary btn-sm" onclick="saveSupervisorContext()">Save Context</button>
                    </div>
                </div>

                <!-- Action Log -->
                <div class="card">
                    <div class="card-inner">
                        <div class="section-title"
                            style="display:flex;justify-content:space-between;align-items:center;">
                            <span>Action Log</span>
                            <div class="btn-row">
                                <button class="btn btn-secondary btn-sm" onclick="clearSupervisorHistory()">Clear
                                    History</button>
                                <button class="btn btn-secondary btn-sm" onclick="loadSupervisorLogs()">Refresh</button>
                            </div>
                        </div>
                        <div id="supervisorLogContainer" style="max-height: 400px; overflow-y: auto; font-size: 13px;">
                            No actions yet</div>
                    </div>
                </div>
            </div>

            <!-- Remote Access Page -->
            <div class="page" data-page="remote">
                <div class="page-header">
                    <div style="display:flex;align-items:center;gap:12px;">
                        <h1>Remote Access</h1>
                        <span id="tunnelStatusBadge"
                            style="padding:4px 12px;border-radius:20px;font-size:12px;font-weight:600;background:var(--border-default);color:var(--text-muted);">Offline</span>
                    </div>
                </div>

                <!-- PIN Warning -->
                <div id="tunnelPinWarning"
                    style="display:none;padding:16px;background:var(--error-muted);border:1px solid var(--error);border-radius:12px;margin-bottom:24px;">
                    <div
                        style="display:flex;align-items:center;gap:8px;font-weight:600;color:var(--error);margin-bottom:4px;">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                            style="width:18px;height:18px;">
                            <path
                                d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z">
                            </path>
                            <line x1="12" y1="9" x2="12" y2="13"></line>
                            <line x1="12" y1="17" x2="12.01" y2="17"></line>
                        </svg>
                        PIN Required
                    </div>
                    <div style="font-size:13px;color:var(--text-secondary);">You must enable PIN authentication before
                        starting a remote tunnel. Go to Server settings and set a PIN first.</div>
                </div>

                <!-- Tunnel Controls -->
                <div class="card">
                    <div class="card-inner">
                        <div class="section-title">Cloudflare Quick Tunnel</div>
                        <div class="toggle-row" style="padding-top:0;">
                            <div>
                                <div class="toggle-label">Tunnel Status</div>
                                <div class="toggle-desc" id="tunnelStatusText">Not connected</div>
                            </div>
                            <button id="tunnelToggleBtn" class="btn btn-primary" onclick="toggleTunnel()">
                                Start Tunnel
                            </button>
                        </div>

                        <!-- Public URL Display -->
                        <div id="tunnelUrlBox"
                            style="display:none;padding:14px;background:var(--surface-0);border:1px solid var(--border-default);border-radius:8px;margin-top:16px;">
                            <div class="section-title" style="margin-bottom:8px;">Public URL</div>
                            <div style="display:flex;align-items:center;gap:8px;">
                                <code id="tunnelUrlText"
                                    style="flex:1;font-family:'SF Mono',Monaco,monospace;font-size:13px;word-break:break-all;color:var(--accent);"></code>
                                <button class="btn btn-secondary btn-sm" onclick="copyTunnelUrl()">
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                        stroke-width="2">
                                        <rect x="9" y="9" width="13" height="13" rx="2"></rect>
                                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                                    </svg>
                                    Copy
                                </button>
                            </div>
                        </div>

                        <!-- QR Code -->
                        <div id="tunnelQrBox"
                            style="display:none;text-align:center;padding:16px;background:white;border-radius:8px;margin-top:12px;">
                            <canvas id="tunnelQrCanvas" style="max-width:200px;"></canvas>
                            <div style="font-size:11px;color:#666;margin-top:8px;">Scan with your phone camera</div>
                        </div>

                        <!-- Auto-start toggle -->
                        <div class="toggle-row">
                            <div>
                                <div class="toggle-label">Auto-start tunnel</div>
                                <div class="toggle-desc">Start tunnel automatically when server boots (requires PIN)
                                </div>
                            </div>
                            <label class="toggle">
                                <input type="checkbox" id="tunnelAutoStart" onchange="toggleTunnelAutoStart()">
                                <span class="toggle-track"></span>
                            </label>
                        </div>
                    </div>
                </div>

                <!-- Security Info -->
                <div class="card">
                    <div class="card-inner">
                        <div class="section-title">Security</div>
                        <div style="font-size:13px;color:var(--text-secondary);line-height:1.6;">
                            <div style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    style="width:16px;height:16px;flex-shrink:0;margin-top:1px;">
                                    <rect x="3" y="11" width="18" height="11" rx="2"></rect>
                                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                                </svg>
                                <div><strong>End-to-end encrypted</strong> — Traffic is encrypted via Cloudflare's HTTPS
                                </div>
                            </div>
                            <div style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    style="width:16px;height:16px;flex-shrink:0;margin-top:1px;">
                                    <path
                                        d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4">
                                    </path>
                                </svg>
                                <div><strong>Random URL</strong> — Tunnel URL changes every restart, making it
                                    unguessable
                                </div>
                            </div>
                            <div style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    style="width:16px;height:16px;flex-shrink:0;margin-top:1px;">
                                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                                </svg>
                                <div><strong>Rate limited</strong> — Login is blocked after 5 failed PIN attempts for 15
                                    minutes</div>
                            </div>
                            <div style="display:flex;align-items:flex-start;gap:10px;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    style="width:16px;height:16px;flex-shrink:0;margin-top:1px;">
                                    <rect x="3" y="11" width="18" height="11" rx="2"></rect>
                                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                                    <circle cx="12" cy="16" r="1"></circle>
                                </svg>
                                <div><strong>PIN required</strong> — All remote access requires PIN authentication</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Installation Help -->
                <div id="tunnelInstallHelp" class="card" style="display:none;">
                    <div class="card-inner">
                        <div class="section-title">Install cloudflared</div>
                        <div style="font-size:13px;color:var(--text-secondary);line-height:1.8;">
                            <div style="margin-bottom:8px;"><strong>Windows:</strong></div>
                            <code
                                style="display:block;padding:8px 12px;background:var(--surface-0);border-radius:6px;font-family:monospace;margin-bottom:12px;">winget install --id Cloudflare.cloudflared</code>
                            <div style="margin-bottom:8px;"><strong>macOS:</strong></div>
                            <code
                                style="display:block;padding:8px 12px;background:var(--surface-0);border-radius:6px;font-family:monospace;margin-bottom:12px;">brew install cloudflared</code>
                            <div style="margin-bottom:8px;"><strong>Linux:</strong></div>
                            <code
                                style="display:block;padding:8px 12px;background:var(--surface-0);border-radius:6px;font-family:monospace;">curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o /usr/local/bin/cloudflared && chmod +x /usr/local/bin/cloudflared</code>
                        </div>
                    </div>
                </div>
            </div>

        </main>
    </div>

    <div class="toast" id="toast"></div>

    <script>
        // SVG Icon System
        const SVG_ICONS = {
            moon: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>',
            sun: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>',
            bot: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/><line x1="8" y1="16" x2="8" y2="16"/><line x1="16" y1="16" x2="16" y2="16"/></svg>',
            chart: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>',
            phone: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>',
            flask: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6v7l5 8H4l5-8V3z"/><line x1="9" y1="3" x2="15" y2="3"/></svg>',
            pause: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>',
            play: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"/></svg>',
            trash: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>',
            trending: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>',
            calendar: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
            download: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>',
            check: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
            sparkle: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l2.4 7.2L22 12l-7.6 2.8L12 22l-2.4-7.2L2 12l7.6-2.8z"/></svg>',
            zap: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
            chat: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
            camera: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>',
            circle_green: '<svg width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="5" fill="#22c55e"/></svg>',
            circle_gray: '<svg width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="5" fill="#6b7280"/></svg>',
            close: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
            stop: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/></svg>',
            info: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>',
            error: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>',
            warning: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
            plug: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22v-5"/><path d="M9 8V2"/><path d="M15 8V2"/><path d="M18 8v5a6 6 0 0 1-12 0V8z"/></svg>',
            settings: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
            monitor: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
            lock: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
            unlock: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/></svg>',
            brain: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/><line x1="8" y1="16" x2="8" y2="16"/><line x1="16" y1="16" x2="16" y2="16"/></svg>',
            syringe: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2l4 4-3 3-4-4"/><path d="M14.5 6.5L5 16l-3 3 3 3 3-3 9.5-9.5"/><path d="M9 11l4 4"/></svg>',
            pointer: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4l7.07 17 2.51-7.39L21 11.07z"/></svg>',
            megaphone: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l18-5v12L3 13v-2z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/></svg>',
            eye: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>',
            question: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
            checkCircle: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
            xCircle: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>',
        };
        function svgIcon(name, size) {
            const svg = SVG_ICONS[name] || SVG_ICONS.info;
            if (size) return svg.replace(/width="\d+"/, `width="${size}"`).replace(/height="\d+"/, `height="${size}"`);
            return svg;
        }
        function showToast(msg, type = 'success') {
            const t = document.getElementById('toast');
            t.innerHTML = msg;
            t.className = `toast ${type} show`;
            setTimeout(() => t.classList.remove('show'), 2500);
        }

        function switchPage(pageName, linkEl) {
            // Hide all pages
            document.querySelectorAll('.page[data-page]').forEach(p => p.classList.remove('active'));
            // Show target page
            const target = document.querySelector(`.page[data-page="${pageName}"]`);
            if (target) target.classList.add('active');
            // Update sidebar active state
            document.querySelectorAll('.sidebar-link').forEach(l => l.classList.remove('active'));
            if (linkEl) linkEl.classList.add('active');
            // Scroll main-content to top
            document.querySelector('.main-content').scrollTop = 0;
        }

        function toggleTheme() {
            const html = document.documentElement;
            const isLight = html.classList.toggle('theme-light');
            localStorage.setItem('admin-theme', isLight ? 'light' : 'dark');
            document.getElementById('themeBtn').innerHTML = isLight ? svgIcon('sun') : svgIcon('moon');
        }

        // Restore theme on load
        (function () {
            const saved = localStorage.getItem('admin-theme');
            if (saved === 'light') {
                document.documentElement.classList.add('theme-light');
                document.getElementById('themeBtn').innerHTML = svgIcon('sun');
            }
        })();

        async function loadConfigFromServer() {
            try {
                const res = await fetch('/api/admin/config');
                if (res.status === 403) {
                    document.body.innerHTML = '<div style="display:flex;align-items:center;justify-content:center;height:100vh;font-size:16px;color:#ef4444;gap:8px">' + svgIcon('stop') + ' Admin panel is only accessible from localhost</div>';
                    return;
                }
                const data = await res.json();
                const c = data.config || data;

                document.getElementById('serverPort').value = c.server?.port || 3001;
                document.getElementById('serverPin').value = '';
                pinFieldTouched = false;
                const clearPinBtn = document.getElementById('clearPinBtn');
                // Show PIN active indicator based on runtime auth state
                const pinStatus = document.getElementById('pinStatus');
                try {
                    const statusRes = await fetch('/api/admin/status');
                    const status = await statusRes.json();
                    if (status.authEnabled) {
                        document.getElementById('serverPin').placeholder = '••••••';
                        pinStatus.innerHTML = svgIcon('lock') + ' <span style="color:#22c55e">PIN is active</span> — enter new PIN to change, or click Clear PIN to remove';
                        pinStatus.style.color = '#22c55e';
                        if (clearPinBtn) clearPinBtn.style.display = '';
                    } else if (c.server?.pin) {
                        pinStatus.innerHTML = svgIcon('unlock') + ' <span style="color:var(--text-muted)">PIN saved but not active (skipped at startup)</span>';
                        pinStatus.style.color = 'var(--text-muted)';
                        if (clearPinBtn) clearPinBtn.style.display = 'none';
                    } else {
                        document.getElementById('serverPin').placeholder = '4–6 digit PIN';
                        pinStatus.innerHTML = svgIcon('unlock') + ' <span style="color:var(--text-muted)">No PIN set</span>';
                        pinStatus.style.color = 'var(--text-muted)';
                        if (clearPinBtn) clearPinBtn.style.display = 'none';
                    }
                } catch (e) { }

                document.getElementById('telegramEnabled').checked = c.telegram?.enabled || false;
                document.getElementById('botToken').value = c.telegram?.botToken || '';
                document.getElementById('chatId').value = c.telegram?.chatId || '';
                document.getElementById('notifComplete').checked = c.telegram?.notifications?.onComplete !== false;
                document.getElementById('notifError').checked = c.telegram?.notifications?.onError !== false;
                document.getElementById('notifInput').checked = c.telegram?.notifications?.onInputNeeded !== false;

                document.getElementById('refreshInterval').value = c.dashboard?.refreshInterval || 2000;
                document.getElementById('dashTheme').value = c.dashboard?.theme || 'dark';

                // Sync auto-accept toggle
                const autoAccept = c.autoAcceptCommands || false;
                document.getElementById('autoAcceptToggle').checked = autoAccept;
                updateAutoAcceptVisual(autoAccept);

                // Sync customize settings
                const mobileUI = c.mobileUI || {};
                document.getElementById('showQuickActions').checked = mobileUI.showQuickActions !== false;
                const supervisorCfg = c.supervisor || {};
                document.getElementById('showAssistTab').checked = supervisorCfg.showAssistTab || false;
                selectedNavMode = mobileUI.navigationMode || 'sidebar';
                updateCustomizeVisuals();

                toggleTelegram();
                loadStatus();
            } catch (e) { showToast('Failed to load config', 'error'); }
        }

        function updateAutoAcceptVisual(enabled) {
            const knob = document.getElementById('autoAcceptKnob');
            const track = knob?.previousElementSibling;
            if (knob) knob.style.left = enabled ? '22px' : '2px';
            if (track) track.style.background = enabled ? '#6366f1' : 'var(--border)';
        }

        // --- Customize page ---
        let pinFieldTouched = false;
        function clearPin() {
            document.getElementById('serverPin').value = '';
            pinFieldTouched = true;
            saveConfig();
        }
        let selectedNavMode = 'sidebar';

        function selectNavMode(mode) {
            selectedNavMode = mode;
            updateCustomizeVisuals();
            scheduleCustomizeSave();
        }

        function updateCustomizeVisuals() {
            // Quick actions toggle
            const qaChecked = document.getElementById('showQuickActions')?.checked;
            const qaKnob = document.getElementById('quickActionsKnob');
            const qaTrack = document.getElementById('quickActionsTrack');
            if (qaKnob) qaKnob.style.transform = qaChecked ? 'translateX(22px)' : 'translateX(0)';
            if (qaTrack) qaTrack.style.background = qaChecked ? '#3b82f6' : '#4b5563';

            // Assist tab toggle
            const atChecked = document.getElementById('showAssistTab')?.checked;
            const atKnob = document.getElementById('assistTabKnob');
            const atTrack = document.getElementById('assistTabTrack');
            if (atKnob) atKnob.style.transform = atChecked ? 'translateX(22px)' : 'translateX(0)';
            if (atTrack) atTrack.style.background = atChecked ? '#3b82f6' : '#4b5563';

            // Nav mode selector
            const sidebarCard = document.getElementById('navModeSidebar');
            const topbarCard = document.getElementById('navModeTopbar');
            const activeStyle = { border: '2px solid var(--accent-primary)', background: 'rgba(59,130,246,0.15)' };
            const inactiveStyle = { border: '2px solid var(--border)', background: 'transparent' };
            if (sidebarCard) { Object.assign(sidebarCard.style, selectedNavMode === 'sidebar' ? activeStyle : inactiveStyle); }
            if (topbarCard) { Object.assign(topbarCard.style, selectedNavMode === 'topbar' ? activeStyle : inactiveStyle); }
        }

        let customizeSaveTimer = null;
        function scheduleCustomizeSave() {
            clearTimeout(customizeSaveTimer);
            customizeSaveTimer = setTimeout(() => saveCustomize(true), 800);
        }

        async function saveCustomize(auto = false) {
            try {
                const settings = {
                    showQuickActions: document.getElementById('showQuickActions').checked,
                    showAssistTab: document.getElementById('showAssistTab').checked,
                    navigationMode: selectedNavMode,
                    refreshInterval: parseInt(document.getElementById('refreshInterval').value) || 2000,
                    theme: document.getElementById('dashTheme').value
                };
                const res = await fetch('/api/admin/mobile-ui', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(settings)
                });
                const data = await res.json();
                if (data.success) showToast(auto ? svgIcon('check') + ' Customization auto-saved' : svgIcon('sparkle') + ' Customization saved');
                else showToast(data.error || 'Save failed', 'error');
            } catch (e) { showToast('Save failed', 'error'); }
        }

        async function toggleAutoAccept() {
            try {
                const res = await fetch('/api/admin/auto-accept/toggle', { method: 'POST' });
                const data = await res.json();
                document.getElementById('autoAcceptToggle').checked = data.enabled;
                updateAutoAcceptVisual(data.enabled);
                showToast(data.enabled ? svgIcon('bot') + ' Auto-accept enabled' : svgIcon('pause') + ' Auto-accept disabled');
            } catch (e) { showToast('Toggle failed', 'error'); }
        }

        async function loadStatus() {
            try {
                const res = await fetch('/api/admin/status');
                const s = await res.json();

                // Stats row
                document.getElementById('statHealth').textContent = s.cdpConnected ? 'Healthy' : 'No CDP';
                document.getElementById('statHealth').className = 'stat-value ' + (s.cdpConnected ? 'ok' : 'err');
                document.getElementById('statUptime').textContent = s.uptime || '—';
                document.getElementById('statClients').textContent = s.activeClients ?? 0;
                document.getElementById('statPort').textContent = s.port || '—';

                // Connection indicators
                const cdpInd = document.getElementById('cdpIndicator');
                cdpInd.className = 'status-indicator ' + (s.cdpConnected ? 'running' : 'stopped');
                cdpInd.innerHTML = `<span class="dot"></span> ${s.cdpConnected ? 'Running' : 'Stopped'}`;

                const tgInd = document.getElementById('tgIndicator');
                tgInd.className = 'status-indicator ' + (s.telegramActive ? 'running' : 'stopped');
                tgInd.innerHTML = `<span class="dot"></span> ${s.telegramActive ? 'Running' : 'Stopped'}`;

                // Env
                document.getElementById('envAuth').textContent = s.authEnabled ? 'PIN' : 'None';

                // Sidebar footer
                document.getElementById('sidebarStatus').textContent = s.cdpConnected ? 'Connected' : 'Disconnected';
                document.getElementById('sidebarDot').style.background = s.cdpConnected ? 'var(--success)' : 'var(--error)';
                document.getElementById('sidebarDot').style.boxShadow = `0 0 6px ${s.cdpConnected ? 'var(--success)' : 'var(--error)'}`;

            } catch (e) { }
        }

        function toggleTelegram() {
            const enabled = document.getElementById('telegramEnabled').checked;
            const fields = document.getElementById('telegramFields');
            fields.style.opacity = enabled ? '1' : '0.35';
            fields.style.pointerEvents = enabled ? 'auto' : 'none';
        }

        async function saveAll(auto = false) {
            const btn = document.getElementById('saveBtn');
            if (!auto) { btn.textContent = 'Saving…'; btn.disabled = true; }
            const config = {
                server: { port: parseInt(document.getElementById('serverPort').value) || 3001 },
                telegram: {
                    enabled: document.getElementById('telegramEnabled').checked,
                    botToken: document.getElementById('botToken').value.trim(),
                    chatId: document.getElementById('chatId').value.trim(),
                    notifications: {
                        onComplete: document.getElementById('notifComplete').checked,
                        onError: document.getElementById('notifError').checked,
                        onInputNeeded: document.getElementById('notifInput').checked
                    }
                },
                dashboard: {
                    refreshInterval: parseInt(document.getElementById('refreshInterval').value) || 2000,
                    theme: document.getElementById('dashTheme').value
                }
            };
            const pin = document.getElementById('serverPin').value.trim();
            if (pinFieldTouched && pin) {
                config.server.pin = pin;
            } else if (pinFieldTouched && !pin) {
                config.server.pin = '';
            }
            try {
                const res = await fetch('/api/admin/config', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(config) });
                const result = await res.json();
                if (result.success) {
                    // Sync theme into mobileUI so the mobile dashboard picks it up
                    try {
                        await fetch('/api/admin/mobile-ui', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({
                                showQuickActions: document.getElementById('showQuickActions')?.checked !== false,
                                navigationMode: selectedNavMode || 'sidebar',
                                refreshInterval: parseInt(document.getElementById('refreshInterval').value) || 2000,
                                theme: document.getElementById('dashTheme').value
                            })
                        });
                    } catch (e) { }
                    showToast(auto ? svgIcon('check') + ' Auto-saved' : svgIcon('check') + ' Settings saved'); loadStatus(); loadConfigFromServer();
                }
                else showToast(result.error || 'Save failed', 'error');
            } catch (e) { if (!auto) showToast('Network error', 'error'); }
            finally { if (!auto) { btn.textContent = 'Save'; btn.disabled = false; } }
        }

        // --- Remote Access / Tunnel ---
        let tunnelPollingTimer = null;

        async function loadTunnelStatus() {
            try {
                const statusRes = await fetch('/api/admin/status');
                const status = await statusRes.json();
                const pinWarning = document.getElementById('tunnelPinWarning');
                if (pinWarning) pinWarning.style.display = status.authEnabled ? 'none' : 'block';

                const res = await fetch('/api/admin/tunnel');
                const data = await res.json();

                const badge = document.getElementById('tunnelStatusBadge');
                const statusText = document.getElementById('tunnelStatusText');
                const btn = document.getElementById('tunnelToggleBtn');
                const urlBox = document.getElementById('tunnelUrlBox');
                const qrBox = document.getElementById('tunnelQrBox');
                const installHelp = document.getElementById('tunnelInstallHelp');

                // Auto-start toggle — just set the checkbox, CSS handles the rest
                const autoStartCheckbox = document.getElementById('tunnelAutoStart');
                if (autoStartCheckbox) autoStartCheckbox.checked = data.autoStart;

                if (data.running && data.url) {
                    badge.textContent = 'Online';
                    badge.style.background = 'var(--success-muted)';
                    badge.style.color = 'var(--success)';
                    statusText.textContent = 'Tunnel is active and accessible remotely';
                    btn.textContent = 'Stop Tunnel';
                    btn.style.background = 'var(--error)';
                    urlBox.style.display = 'block';
                    document.getElementById('tunnelUrlText').textContent = data.url;
                    qrBox.style.display = 'block';
                    generateTunnelQR(data.url);
                    if (installHelp) installHelp.style.display = 'none';
                } else if (data.starting) {
                    badge.textContent = 'Starting...';
                    badge.style.background = 'rgba(234,179,8,0.15)';
                    badge.style.color = '#eab308';
                    statusText.textContent = 'Connecting to Cloudflare...';
                    btn.textContent = 'Starting...';
                    btn.disabled = true;
                    urlBox.style.display = 'none';
                    qrBox.style.display = 'none';
                } else {
                    badge.textContent = 'Offline';
                    badge.style.background = 'var(--border)';
                    badge.style.color = 'var(--text-muted)';
                    statusText.textContent = data.error || 'Not connected';
                    btn.textContent = 'Start Tunnel';
                    btn.style.background = 'var(--accent-primary)';
                    btn.disabled = !status.authEnabled;
                    urlBox.style.display = 'none';
                    qrBox.style.display = 'none';
                    // Show install help if the error mentions cloudflared not found
                    if (installHelp) installHelp.style.display = (data.error && data.error.includes('not found')) ? 'block' : 'none';
                }
            } catch (e) { }
        }

        async function toggleTunnel() {
            const btn = document.getElementById('tunnelToggleBtn');
            const badge = document.getElementById('tunnelStatusBadge');

            if (btn.textContent.includes('Stop')) {
                btn.textContent = 'Stopping...';
                btn.disabled = true;
                try {
                    await fetch('/api/admin/tunnel/stop', { method: 'POST' });
                    showToast(svgIcon('check') + ' Tunnel stopped');
                } catch (e) { showToast('Failed to stop tunnel', 'error'); }
                await loadTunnelStatus();
                return;
            }

            btn.textContent = 'Starting...';
            btn.disabled = true;
            badge.textContent = 'Starting...';
            badge.style.background = 'rgba(234,179,8,0.15)';
            badge.style.color = '#eab308';

            try {
                const res = await fetch('/api/admin/tunnel/start', { method: 'POST' });
                const data = await res.json();
                if (data.success) {
                    showToast(svgIcon('check') + ' Tunnel active!');
                } else {
                    showToast(data.error || 'Failed to start tunnel', 'error');
                }
            } catch (e) { showToast('Failed to start tunnel', 'error'); }
            await loadTunnelStatus();
        }

        async function toggleTunnelAutoStart() {
            try {
                const res = await fetch('/api/admin/tunnel/auto-start', { method: 'POST' });
                const data = await res.json();
                const cb = document.getElementById('tunnelAutoStart');
                if (cb) cb.checked = data.autoStart;
                showToast(data.autoStart ? svgIcon('check') + ' Auto-start enabled' : svgIcon('check') + ' Auto-start disabled');
            } catch (e) { showToast('Failed to toggle auto-start', 'error'); }
        }

        function copyTunnelUrl() {
            const url = document.getElementById('tunnelUrlText')?.textContent;
            if (!url) return;
            navigator.clipboard.writeText(url).then(() => {
                showToast(svgIcon('check') + ' URL copied!');
            }).catch(() => {
                // Fallback
                const ta = document.createElement('textarea');
                ta.value = url;
                document.body.appendChild(ta);
                ta.select();
                document.execCommand('copy');
                document.body.removeChild(ta);
                showToast(svgIcon('check') + ' URL copied!');
            });
        }

        // Simple QR code generator using canvas (no external library)
        function generateTunnelQR(text) {
            const canvas = document.getElementById('tunnelQrCanvas');
            if (!canvas) return;
            // Use a simple approach: create a QR code image via a public API
            const img = new Image();
            img.crossOrigin = 'anonymous';
            img.onload = () => {
                canvas.width = 200;
                canvas.height = 200;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, 200, 200);
            };
            img.onerror = () => {
                // If API fails, just show the URL text
                canvas.width = 200;
                canvas.height = 40;
                const ctx = canvas.getContext('2d');
                ctx.fillStyle = '#333';
                ctx.font = '11px monospace';
                ctx.fillText('QR unavailable', 50, 25);
            };
            img.src = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${encodeURIComponent(text)}`;
        }

        async function testTelegram() {
            const chatId = document.getElementById('chatId').value.trim();
            if (!chatId) { showToast('Enter a Chat ID first', 'error'); return; }
            try {
                const res = await fetch('/api/admin/telegram/test', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ chatId }) });
                const result = await res.json();
                showToast(result.success ? svgIcon('check') + ' Test message sent!' : (result.error || 'Failed'), result.success ? 'success' : 'error');
            } catch (e) { showToast('Network error', 'error'); }
        }

        // Auto-save: debounce 800ms after any input change
        let autoSaveTimer = null;
        function scheduleAutoSave() {
            clearTimeout(autoSaveTimer);
            autoSaveTimer = setTimeout(() => saveAll(true), 800);
        }

        document.querySelectorAll('input, select').forEach(el => {
            // Exclude customize-page inputs from general auto-save
            if (el.id === 'showQuickActions' || el.id === 'showAssistTab') return;
            el.addEventListener('input', scheduleAutoSave);
            el.addEventListener('change', scheduleAutoSave);
        });

        // ============================================================================
        // Device Management
        // ============================================================================
        async function loadDevices() {
            try {
                const res = await fetch('/api/admin/devices');
                const data = await res.json();
                const devices = data.devices || [];
                const container = document.getElementById('deviceList');
                if (devices.length === 0) {
                    container.innerHTML = '<div style="color:var(--text-muted)">No devices configured</div>';
                    return;
                }
                container.innerHTML = devices.map(d => `
                    <div class="status-row" style="padding: 10px 0; border-bottom: 1px solid var(--border);">
                        <div>
                            <div style="font-weight: 600; color: var(--text);">${d.active ? svgIcon('circle_green', 10) : svgIcon('circle_gray', 10)} ${d.name}</div>
                            <div style="font-size: 12px; color: var(--text-muted);">Port ${d.cdpPort} ${d.active ? '— Active' : ''}</div>
                        </div>
                        <div class="btn-row">
                            ${d.active ? '' : `<button class="btn btn-secondary btn-sm" onclick="switchDevice(${d.cdpPort})">Activate</button>`}
                            <button class="btn btn-secondary btn-sm" onclick="deleteDevice(${d.cdpPort})" style="color: var(--error);"><span style="display:inline-flex;vertical-align:middle"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></span></button>
                        </div>
                    </div>
                `).join('');
            } catch (e) { document.getElementById('deviceList').innerHTML = '<div style="color:var(--error)">Failed to load</div>'; }
        }

        async function addDevice() {
            const name = document.getElementById('newDeviceName').value.trim();
            const cdpPort = document.getElementById('newDevicePort').value.trim();
            if (!name || !cdpPort) { showToast('Enter name and port', 'error'); return; }
            try {
                const res = await fetch('/api/admin/devices', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ name, cdpPort: parseInt(cdpPort), active: false }) });
                const result = await res.json();
                if (result.success) { showToast(svgIcon('check') + ' Device added'); document.getElementById('newDeviceName').value = ''; document.getElementById('newDevicePort').value = ''; loadDevices(); }
                else showToast(result.error || 'Failed', 'error');
            } catch (e) { showToast('Network error', 'error'); }
        }

        async function switchDevice(port) {
            try {
                const res = await fetch('/api/admin/devices/switch', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cdpPort: port }) });
                const result = await res.json();
                if (result.success) { showToast(svgIcon('check') + ` Switched to ${result.active.name}`); loadDevices(); loadStatus(); }
                else showToast(result.error || 'Failed', 'error');
            } catch (e) { showToast('Network error', 'error'); }
        }

        async function deleteDevice(port) {
            try {
                const res = await fetch(`/api/admin/devices/${port}`, { method: 'DELETE' });
                const result = await res.json();
                if (result.success) { showToast(svgIcon('check') + ' Device removed'); loadDevices(); }
                else showToast(result.error || 'Failed', 'error');
            } catch (e) { showToast('Network error', 'error'); }
        }

        // ============================================================================
        // Quick Commands
        // ============================================================================
        let commandsCache = [];

        async function loadCommands() {
            try {
                const res = await fetch('/api/admin/commands');
                const data = await res.json();
                commandsCache = data.commands || [];
                renderCommands();
            } catch (e) { document.getElementById('commandList').innerHTML = '<div class="card"><div class="card-inner" style="color:var(--error)">Failed to load</div></div>'; }
        }

        function renderCommands() {
            const container = document.getElementById('commandList');
            if (commandsCache.length === 0) {
                container.innerHTML = '<div class="card"><div class="card-inner" style="color:var(--text-muted)">No commands configured. Click "+ Add Command" to create one.</div></div>';
                return;
            }
            container.innerHTML = commandsCache.map((cmd, i) => `
                <div class="card" style="margin-bottom: 8px;">
                    <div class="card-inner" style="display: flex; align-items: center; gap: 12px;">
                        <div style="font-size: 24px;">${cmd.icon ? svgIcon(cmd.icon, 24) : svgIcon('zap', 24)}</div>
                        <div style="flex: 1; min-width: 0;">
                            <input class="input" value="${cmd.label}" placeholder="Label" onchange="updateCommand(${i}, 'label', this.value)" style="font-weight: 600; margin-bottom: 4px;">
                            <input class="input" value="${cmd.prompt.replace(/"/g, '&quot;')}" placeholder="Agent prompt..." onchange="updateCommand(${i}, 'prompt', this.value)" style="font-size: 12px;">
                        </div>
                        <div class="btn-row" style="flex-shrink: 0;">
                            <button class="btn btn-primary btn-sm" onclick="runCommand(${i})"><span style="display:inline-flex;vertical-align:middle"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"/></svg></span> Run</button>
                            <button class="btn btn-secondary btn-sm" onclick="removeCommand(${i})" style="color: var(--error);">${svgIcon('close')}</button>
                        </div>
                    </div>
                </div>
            `).join('');
        }

        function addCommand() {
            commandsCache.push({ label: 'New Command', prompt: 'Describe what the agent should do...', icon: 'zap' });
            renderCommands();
            saveCommands();
        }

        function updateCommand(index, field, value) {
            commandsCache[index][field] = value;
            saveCommands();
        }

        function removeCommand(index) {
            commandsCache.splice(index, 1);
            renderCommands();
            saveCommands();
        }

        async function saveCommands() {
            try {
                await fetch('/api/admin/commands', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ commands: commandsCache }) });
                showToast(svgIcon('check') + ' Commands saved');
            } catch (e) { showToast('Save failed', 'error'); }
        }

        async function runCommand(index) {
            const cmd = commandsCache[index];
            if (!cmd) return;
            showToast(svgIcon('zap') + ` Running: ${cmd.label}...`);
            try {
                const res = await fetch('/api/commands/execute', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ prompt: cmd.prompt }) });
                const result = await res.json();
                showToast(result.success ? svgIcon('check') + ` ${cmd.label} sent!` : (result.error || 'Failed'), result.success ? 'success' : 'error');
            } catch (e) { showToast('Execution failed', 'error'); }
        }

        // ============================================================================
        // Activity Feed
        // ============================================================================
        async function loadEvents() {
            try {
                const res = await fetch('/api/admin/events');
                const data = await res.json();
                const events = data.events || [];
                const container = document.getElementById('activityFeed');
                if (events.length === 0) {
                    container.innerHTML = '<div style="color:var(--text-muted);padding:8px;">No events yet</div>';
                    return;
                }
                container.innerHTML = events.map(e => {
                    const t = new Date(e.time);
                    const ts = t.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
                    return `<div style="padding:6px 0;border-bottom:1px solid var(--border);display:flex;gap:8px;align-items:center;">
                        <span style="flex-shrink:0;">${e.icon}</span>
                        <span style="flex:1;color:var(--text);">${e.message}</span>
                        <span style="flex-shrink:0;font-size:11px;color:var(--text-muted);">${ts}</span>
                    </div>`;
                }).join('');
            } catch (e) { }
        }

        // ============================================================================
        // QR Code Pairing
        // ============================================================================
        async function generateQR() {
            const port = document.getElementById('serverPort')?.value || location.port || '3001';
            let host = location.hostname;
            try {
                const res = await fetch('/api/admin/status');
                const data = await res.json();
                if (data.lanIP) host = data.lanIP;
            } catch (e) { }
            const hostUrl = `http://${host}:${port}`;
            const qrImg = `https://api.qrserver.com/v1/create-qr-code/?size=160x160&data=${encodeURIComponent(hostUrl)}`;
            const container = document.getElementById('qrCodeContainer');
            container.innerHTML = `<img src="${qrImg}" width="160" height="160" alt="QR Code" style="display:block;">`;
            document.getElementById('qrUrl').textContent = hostUrl;
        }

        // ============================================================================
        // Session Logs
        // ============================================================================
        async function loadSessions() {
            try {
                const res = await fetch('/api/admin/logs');
                const data = await res.json();
                const sessions = data.sessions || [];
                const container = document.getElementById('sessionList');
                if (sessions.length === 0) {
                    container.innerHTML = '<div class="card"><div class="card-inner" style="color:var(--text-muted)">No log files yet. Events will be logged after server restart.</div></div>';
                    return;
                }
                container.innerHTML = sessions.map(s => `
                    <div class="card" style="margin-bottom: 8px; cursor: pointer;" onclick="viewSession('${s.filename}')">
                        <div class="card-inner" style="display:flex;justify-content:space-between;align-items:center;">
                            <div>
                                <div style="font-weight:600;color:var(--text);">${svgIcon('calendar')} ${s.date}</div>
                                <div style="font-size:12px;color:var(--text-muted);">${s.events} events · ${(s.size / 1024).toFixed(1)} KB</div>
                            </div>
                            <a class="btn btn-secondary btn-sm" href="/api/admin/logs/${s.filename}/download" onclick="event.stopPropagation()"><span style="display:inline-flex;vertical-align:middle"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg></span> Download</a>
                        </div>
                    </div>
                `).join('');
            } catch (e) { document.getElementById('sessionList').innerHTML = '<div class="card"><div class="card-inner" style="color:var(--error)">Failed to load</div></div>'; }
        }

        async function viewSession(filename) {
            try {
                const res = await fetch(`/api/admin/logs/${filename}`);
                const data = await res.json();
                const events = (data.events || []).slice(-100);
                document.getElementById('sessionViewerTitle').textContent = `Session: ${filename.replace('session-', '').replace('.jsonl', '')}`;
                document.getElementById('sessionEvents').innerHTML = events.map(e => {
                    const t = new Date(e.time);
                    const ts = t.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
                    return `<div style="padding:6px 0;border-bottom:1px solid var(--border);display:flex;gap:8px;align-items:center;">
                        <span style="flex-shrink:0;">${e.icon}</span>
                        <span style="flex:1;color:var(--text);">${e.message}</span>
                        <span style="flex-shrink:0;font-size:11px;color:var(--text-muted);">${ts}</span>
                    </div>`;
                }).join('') || '<div style="color:var(--text-muted)">No events</div>';
                document.getElementById('sessionViewer').style.display = 'block';
            } catch (e) { showToast('Failed to load session', 'error'); }
        }

        async function clearAllLogs() {
            if (!confirm('Delete all session logs? This cannot be undone.')) return;
            try {
                const res = await fetch('/api/admin/logs', { method: 'DELETE' });
                const data = await res.json();
                if (data.success) {
                    showToast(`Cleared ${data.deleted} log file(s)`, 'success');
                    document.getElementById('sessionViewer').style.display = 'none';
                    loadSessions();
                } else {
                    showToast(data.error || 'Failed', 'error');
                }
            } catch (e) { showToast('Failed to clear logs', 'error'); }
        }
        async function toggleLogging() {
            try {
                const res = await fetch('/api/admin/logs/pause', { method: 'POST' });
                const data = await res.json();
                const btn = document.getElementById('pauseLoggingBtn');
                btn.innerHTML = data.paused ? svgIcon('play') + ' Resume' : svgIcon('pause') + ' Pause';
                showToast(data.paused ? 'Logging paused' : 'Logging resumed', 'success');
            } catch (e) { showToast('Failed', 'error'); }
        }

        async function syncPauseBtn() {
            try {
                const res = await fetch('/api/admin/logs/pause');
                const data = await res.json();
                const btn = document.getElementById('pauseLoggingBtn');
                if (btn) btn.innerHTML = data.paused ? svgIcon('play') + ' Resume' : svgIcon('pause') + ' Pause';
            } catch (e) { }
        }

        // ============================================================================
        // Analytics
        // ============================================================================
        async function loadAnalytics() {
            try {
                const res = await fetch('/api/admin/analytics');
                const data = await res.json();
                document.getElementById('statScreenshots').textContent = data.totals.screenshots;
                document.getElementById('statErrors').textContent = data.totals.errors;
                document.getElementById('statCommands').textContent = data.totals.commands;
                document.getElementById('analyticsUptime').textContent = data.totalUptime;
                renderChart(data.dailyStats);
            } catch (e) { }
        }

        function renderChart(dailyStats) {
            const canvas = document.getElementById('analyticsChart');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            canvas.width = canvas.offsetWidth * 2;
            canvas.height = 400;
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Get last 7 days
            const days = [];
            for (let i = 6; i >= 0; i--) {
                const d = new Date(); d.setDate(d.getDate() - i);
                days.push(d.toISOString().slice(0, 10));
            }

            const barWidth = Math.floor((canvas.width - 80) / days.length / 3);
            const maxVal = Math.max(1, ...days.flatMap(d => {
                const s = dailyStats[d] || {};
                return [s.screenshots || 0, s.errors || 0, s.commands || 0];
            }));

            const chartH = canvas.height - 60;
            const colors = ['#10b981', '#f43f5e', '#f59e0b'];
            const labels = ['Scrn', 'Errs', 'Cmds'];

            days.forEach((day, i) => {
                const s = dailyStats[day] || {};
                const vals = [s.screenshots || 0, s.errors || 0, s.commands || 0];
                const groupX = 60 + i * ((canvas.width - 80) / days.length);

                vals.forEach((v, j) => {
                    const h = (v / maxVal) * (chartH - 20);
                    const x = groupX + j * (barWidth + 2);
                    ctx.fillStyle = colors[j];
                    ctx.fillRect(x, chartH - h + 10, barWidth, h);
                    if (v > 0) {
                        ctx.fillStyle = '#999';
                        ctx.font = '16px sans-serif';
                        ctx.textAlign = 'center';
                        ctx.fillText(v, x + barWidth / 2, chartH - h + 4);
                    }
                });

                // Day label
                ctx.fillStyle = '#999';
                ctx.font = '16px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText(day.slice(5), groupX + (barWidth * 2), chartH + 28);
            });

            // Legend
            labels.forEach((l, i) => {
                const lx = 60 + i * 90;
                ctx.fillStyle = colors[i];
                ctx.fillRect(lx, canvas.height - 18, 12, 12);
                ctx.fillStyle = '#999';
                ctx.font = '14px sans-serif';
                ctx.textAlign = 'left';
                ctx.fillText(l, lx + 16, canvas.height - 7);
            });
        }

        // ============================================================================
        // Screenshot Gallery
        // ============================================================================
        async function loadScreenshotGallery() {
            try {
                const res = await fetch('/api/admin/screenshots');
                const data = await res.json();
                const shots = data.screenshots || [];
                const container = document.getElementById('screenshotGallery');
                if (shots.length === 0) {
                    container.innerHTML = '<div class="card" style="grid-column:1/-1;"><div class="card-inner" style="color:var(--text-muted)">No screenshots yet. Auto-capture runs every 30 seconds when CDP is connected.</div></div>';
                    return;
                }
                container.innerHTML = shots.map(s => {
                    const d = new Date(s.timestamp);
                    const ts = d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
                    return `<div class="card" style="cursor:pointer;overflow:hidden;" onclick="showFullScreenshot('${s.filename}')">
                        <img src="/api/admin/screenshots/${s.filename}" loading="lazy" style="width:100%;aspect-ratio:16/9;object-fit:cover;display:block;">
                        <div style="padding:6px 8px;font-size:11px;color:var(--text-muted);text-align:center;">${ts} · ${(s.size / 1024).toFixed(0)}KB</div>
                    </div>`;
                }).join('');
            } catch (e) { document.getElementById('screenshotGallery').innerHTML = '<div style="color:var(--error)">Failed to load</div>'; }
        }

        function showFullScreenshot(filename) {
            document.getElementById('screenshotFullImg').src = `/api/admin/screenshots/${filename}`;
            document.getElementById('screenshotFullview').style.display = 'flex';
        }

        async function toggleScreenshots() {
            try {
                const res = await fetch('/api/admin/screenshots/toggle', { method: 'POST' });
                const data = await res.json();
                const btn = document.getElementById('screenshotToggleBtn');
                btn.innerHTML = data.enabled ? svgIcon('pause') + ' Disable' : svgIcon('play') + ' Enable';
                showToast(data.enabled ? svgIcon('camera') + ' Screenshots enabled' : svgIcon('pause') + ' Screenshots disabled');
            } catch (e) { showToast('Toggle failed', 'error'); }
        }

        async function clearScreenshots() {
            if (!confirm('Delete all captured screenshots? This cannot be undone.')) return;
            try {
                const res = await fetch('/api/admin/screenshots', { method: 'DELETE' });
                const data = await res.json();
                showToast(svgIcon('trash') + ` Deleted ${data.deleted} screenshots`);
                loadScreenshotGallery();
            } catch (e) { showToast('Delete failed', 'error'); }
        }

        // ============================================================================
        // Page switch + lazy loading
        // ============================================================================
        const origSwitchPage = switchPage;
        switchPage = function (pageName, linkEl) {
            origSwitchPage(pageName, linkEl);
            if (pageName === 'dashboard') { loadEvents(); }
            if (pageName === 'mobile') generateQR();
            if (pageName === 'devices') loadDevices();
            if (pageName === 'commands') loadCommands();
            if (pageName === 'logs') { loadSessions(); syncPauseBtn(); }
            if (pageName === 'screenshots') loadScreenshotGallery();
            if (pageName === 'analytics') loadAnalytics();
            if (pageName === 'remote') loadTunnelStatus();
            if (pageName === 'supervisor') { loadSupervisorStatus(); loadSupervisorLogs(); }
        };

        // ============================================================================
        // Supervisor functions
        // ============================================================================
        async function loadSupervisorStatus() {
            try {
                const res = await fetch('/api/admin/supervisor');
                const data = await res.json();
                document.getElementById('supervisorEnabled').checked = data.enabled;
                document.getElementById('supervisorDisableInjects').checked = data.config?.disableInjects || false;
                document.getElementById('supervisorEndpoint').value = data.config?.endpoint || 'http://localhost:11434';
                document.getElementById('supervisorModel').value = data.config?.model || 'llama3';
                document.getElementById('supervisorRateLimit').value = data.config?.maxActionsPerMinute || 10;
                document.getElementById('supervisorContextWindow').value = data.config?.contextWindow || 8192;
                document.getElementById('supervisorContext').value = data.config?.projectContext || '';
                document.getElementById('supervisorStatEnabled').textContent = data.enabled ? 'Active' : 'Off';
                document.getElementById('supervisorStatEnabled').className = 'stat-value ' + (data.enabled ? 'ok' : '');
                document.getElementById('supervisorStatOllama').textContent = data.ollamaAvailable ? 'Connected' : 'Offline';
                document.getElementById('supervisorStatOllama').className = 'stat-value ' + (data.ollamaAvailable ? 'ok' : 'err');
                document.getElementById('supervisorStatActions').textContent = `${data.actionsThisMinute || 0}/${data.maxActionsPerMinute || 10}`;
                if (data.ollamaModels && data.ollamaModels.length > 0) {
                    document.getElementById('ollamaModelHint').textContent = `Available: ${data.ollamaModels.slice(0, 5).join(', ')}`;
                }
            } catch (e) { showToast('Failed to load supervisor status', 'error'); }
        }

        async function toggleSupervisor() {
            try {
                const res = await fetch('/api/admin/supervisor/toggle', { method: 'POST' });
                const data = await res.json();
                document.getElementById('supervisorEnabled').checked = data.enabled;
                showToast(data.enabled ? svgIcon('bot') + ' Supervisor enabled' : svgIcon('pause') + ' Supervisor disabled');
                loadSupervisorStatus();
            } catch (e) { showToast('Toggle failed', 'error'); }
        }

        async function toggleSupervisorInjects() {
            const disabled = document.getElementById('supervisorDisableInjects').checked;
            try {
                await fetch('/api/admin/supervisor', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ disableInjects: disabled })
                });
                showToast(disabled ? svgIcon('pause') + ' IDE injects disabled' : svgIcon('bot') + ' IDE injects enabled');
            } catch (e) { showToast('Toggle failed', 'error'); }
        }

        async function saveSupervisor() {
            try {
                const res = await fetch('/api/admin/supervisor', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        endpoint: document.getElementById('supervisorEndpoint').value,
                        model: document.getElementById('supervisorModel').value,
                        maxActionsPerMinute: document.getElementById('supervisorRateLimit').value,
                        contextWindow: document.getElementById('supervisorContextWindow').value,
                        disableInjects: document.getElementById('supervisorDisableInjects').checked,
                        projectContext: document.getElementById('supervisorContext').value
                    })
                });
                const data = await res.json();
                if (data.success) showToast(svgIcon('check') + ' Supervisor config saved');
                else showToast(data.error || 'Save failed', 'error');
            } catch (e) { showToast('Save failed', 'error'); }
        }

        async function saveSupervisorContext() {
            try {
                const res = await fetch('/api/admin/supervisor/context', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ context: document.getElementById('supervisorContext').value })
                });
                const data = await res.json();
                if (data.success) showToast(svgIcon('check') + ' Project context saved');
                else showToast('Save failed', 'error');
            } catch (e) { showToast('Save failed', 'error'); }
        }

        async function testOllamaConnection() {
            const endpoint = document.getElementById('supervisorEndpoint').value;
            const hint = document.getElementById('ollamaTestResult');
            hint.textContent = 'Testing...';
            hint.style.color = 'var(--text-muted)';
            try {
                const res = await fetch('/api/admin/supervisor/test', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ endpoint })
                });
                const data = await res.json();
                if (data.available) {
                    hint.innerHTML = svgIcon('checkCircle') + ' Connected — ' + (data.models?.length || 0) + ' models available';
                    hint.style.color = 'var(--success)';
                    if (data.models?.length > 0) {
                        document.getElementById('ollamaModelHint').textContent = `Available: ${data.models.slice(0, 5).join(', ')}`;
                    }
                } else {
                    hint.innerHTML = svgIcon('xCircle') + ' Failed: ' + (data.error || 'Unknown error');
                    hint.style.color = 'var(--error)';
                }
            } catch (e) {
                hint.innerHTML = svgIcon('xCircle') + ' Connection failed';
                hint.style.color = 'var(--error)';
            }
        }

        async function loadSupervisorLogs() {
            try {
                const res = await fetch('/api/admin/supervisor/logs');
                const data = await res.json();
                const container = document.getElementById('supervisorLogContainer');
                if (!data.actions || data.actions.length === 0) {
                    container.innerHTML = '<div style="color:var(--text-muted);padding:12px;">No actions recorded yet. Enable the supervisor and it will start logging decisions here.</div>';
                    return;
                }
                container.innerHTML = data.actions.map(a => {
                    const time = new Date(a.timestamp).toLocaleTimeString();
                    const icon = a.action === 'inject' ? svgIcon('syringe') : a.action === 'click' ? svgIcon('pointer') : a.action === 'notify' ? svgIcon('megaphone') : a.action === 'config' ? svgIcon('settings') : a.action === 'none' ? svgIcon('eye') : svgIcon('question');
                    return `<div style="padding:8px 0;border-bottom:1px solid var(--border-subtle);display:flex;gap:8px;align-items:flex-start;"><span style="opacity:.5;font-size:11px;white-space:nowrap;">${time}</span><span>${icon}</span><span style="flex:1;">${a.action}: ${a.detail.length > 80 ? a.detail.slice(0, 80) + '…' : a.detail}</span><span style="font-size:11px;color:var(--text-muted);">${a.result}</span></div>`;
                }).join('');
            } catch (e) { /* silent */ }
        }

        async function clearSupervisorHistory() {
            try {
                await fetch('/api/admin/supervisor/clear', { method: 'POST' });
                showToast(svgIcon('check') + ' Supervisor history cleared');
                loadSupervisorLogs();
            } catch (e) { showToast('Failed', 'error'); }
        }

        loadConfigFromServer();
        loadEvents();
        generateQR();
        // Set supervisor title icon
        const supTitleIcon = document.getElementById('supervisorTitleIcon');
        if (supTitleIcon) supTitleIcon.innerHTML = svgIcon('brain', 20);
        setInterval(loadStatus, 10000);
        setInterval(loadEvents, 10000);
    </script>
</body>

</html>
```

## File: payload\public\index.html
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Antigravity Control</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- Codicons font for IDE icons (terminal, file, etc.) -->
    <link href="https://unpkg.com/@vscode/codicons@0.0.36/dist/codicon.css" rel="stylesheet">
    <!-- Highlight.js for code syntax highlighting -->
    <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <!-- PWA -->
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#050508">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Antigravity">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <!-- CSS -->
</head>

<body>
    <div class="bg-effects"></div>

    <!-- Login Screen -->
    <div class="login-screen hidden" id="loginScreen">
        <div class="login-card">
            <div class="login-logo"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2">
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg></div>
            <div class="login-title">Enter PIN</div>
            <div class="login-subtitle">Authentication required to access</div>
            <input type="tel" class="pin-input" id="pinInput" maxlength="6" placeholder="• • • •" autocomplete="off">
            <button class="login-btn" onclick="submitPin()">Unlock</button>
            <div class="login-error" id="loginError" style="display: none;"></div>
        </div>
    </div>

    <!-- Content -->
    <main class="content">
        <!-- Chat View (Main) -->
        <!-- Dynamic IDE styles injected here -->
        <style id="cascadeStyles"></style>

        <div class="chat-container">
            <!-- Live cascade content will be injected here -->
            <div id="cascade-container" class="cascade-view">
                <div class="chat-empty">
                    <svg class="icon" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="1.5" style="opacity: 0.4;">
                        <path
                            d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z">
                        </path>
                    </svg>
                    <span>Loading live chat...</span>
                </div>
            </div>


            <!-- Model/Mode Selector -->
            <div class="model-mode-row">
                <button class="model-selector" id="modelSelectorBtn" onclick="toggleModelDropdown(event)">
                    <span id="currentModelLabel">Loading...</span>
                    <span class="dropdown-arrow">▾</span>
                </button>
                <button class="mode-selector" id="modeSelectorBtn" onclick="toggleModeDropdown(event)">
                    <span id="currentModeLabel">Planning</span>
                    <span class="dropdown-arrow">▾</span>
                </button>
            </div>

            <!-- Model Dropdown -->
            <div class="model-dropdown" id="modelDropdown" style="display: none;">
                <div class="dropdown-header">Select Model</div>
                <div id="modelList" class="dropdown-list">
                    <!-- Models will be inserted here -->
                </div>
            </div>

            <!-- Mode Dropdown -->
            <div class="mode-dropdown" id="modeDropdown" style="display: none;">
                <div class="dropdown-header">Conversation Mode</div>
                <div class="dropdown-item" onclick="selectMode('Planning')">
                    <div class="mode-name">Planning</div>
                    <div class="mode-desc">Agent plans before executing. For complex tasks.</div>
                </div>
                <div class="dropdown-item" onclick="selectMode('Fast')">
                    <div class="mode-name">Fast</div>
                    <div class="mode-desc">Agent executes directly. For simple tasks.</div>
                </div>
            </div>

            <div class="quick-actions">
                <button class="quick-chip" onclick="sendQuick('continue')">Continue</button>
                <button class="quick-chip" onclick="sendQuick('yes')">Yes</button>
                <button class="quick-chip" onclick="sendQuick('no')">No</button>
                <button class="quick-chip" onclick="sendQuick('stop')">Stop</button>
                <button class="quick-chip" onclick="sendQuick('help')">Help</button>
            </div>

            <!-- Remote Prompt History -->
            <div id="remotePrompts" class="remote-prompts-container"></div>

            <div class="chat-input-area">
                <div class="chat-input-wrapper">
                    <input type="text" id="chatInput" class="chat-input" placeholder="Send a message..."
                        onkeypress="if(event.key==='Enter') sendChatMessage()">
                    <button class="chat-send" onclick="sendChatMessage()"><svg width="20" height="20"
                            viewBox="0 0 24 24" fill="currentColor">
                            <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"></path>
                        </svg></button>
                </div>
            </div>
        </div>
    </main>

    <!-- Sidebar -->
    <nav class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <button class="sidebar-toggle" onclick="toggleSidebar()" title="Toggle sidebar">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
                </svg>
            </button>
            <div class="sidebar-logo">
                <span class="logo-text">Antigravity</span>
            </div>
        </div>
        <div class="sidebar-nav">
            <button class="sidebar-item active" data-panel="chat">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path
                        d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z">
                    </path>
                </svg>
                <span>Chat</span>
            </button>
            <button class="sidebar-item" data-panel="files">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                </svg>
                <span>Files</span>
            </button>
            <button class="sidebar-item" data-panel="settings">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="3"></circle>
                    <path
                        d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z">
                    </path>
                </svg>
                <span>Settings</span>
            </button>
            <button class="sidebar-item" data-panel="assist" id="sidebarAssistBtn" style="display:none;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path
                        d="M12 2a9 9 0 0 0-9 9c0 3.88 2.46 7.18 5.9 8.44.13-.95.5-2.06 1.1-2.94a5 5 0 0 1 4-8.5 5 5 0 0 1 4 8.5c.6.88.97 1.99 1.1 2.94A9.01 9.01 0 0 0 21 11a9 9 0 0 0-9-9z">
                    </path>
                    <path d="M12 18v4"></path>
                    <circle cx="12" cy="11" r="2"></circle>
                </svg>
                <span>Assist</span>
            </button>
        </div>
        <div class="sidebar-footer">
            <div id="statusPill" class="status-pill disconnected">
                <div class="status-dot"></div>
                <span class="status-text">Connecting</span>
            </div>
            <button id="themeIconBtn" class="theme-icon-btn" onclick="cycleTheme()" title="Change theme">🌙</button>
            <select id="sidebarThemeSelect" class="theme-selector" onchange="setTheme(this.value)">
                <option value="dark">Dark</option>
                <option value="light">Light</option>
                <option value="pastel">Pastel</option>
                <option value="rainbow">Rainbow</option>
                <option value="slate">Slate</option>
            </select>
        </div>
    </nav>

    <!-- Top Bar (shown only in topbar mode, completely separate from sidebar) -->
    <nav id="topbar">
        <div class="topbar-nav">
            <button class="topbar-btn active" data-panel="chat">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path
                        d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z">
                    </path>
                </svg>
                Chat
            </button>
            <button class="topbar-btn" data-panel="files">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                </svg>
                Files
            </button>
            <button class="topbar-btn" data-panel="settings">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="3"></circle>
                    <path
                        d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z">
                    </path>
                </svg>
                Settings
            </button>
            <button class="topbar-btn" data-panel="assist" id="topbarAssistBtn" style="display:none;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path
                        d="M12 2a9 9 0 0 0-9 9c0 3.88 2.46 7.18 5.9 8.44.13-.95.5-2.06 1.1-2.94a5 5 0 0 1 4-8.5 5 5 0 0 1 4 8.5c.6.88.97 1.99 1.1 2.94A9.01 9.01 0 0 0 21 11a9 9 0 0 0-9-9z">
                    </path>
                    <path d="M12 18v4"></path>
                    <circle cx="12" cy="11" r="2"></circle>
                </svg>
                Assist
            </button>
        </div>
    </nav>

    <!-- File Browser Panel -->
    <div class="files-panel-overlay" id="filesOverlay" onclick="closeFilesPanel()"></div>
    <div class="files-panel" id="filesPanel">
        <div class="files-header">
            <h3>Files</h3>
            <button class="files-close" onclick="closeFilesPanel()">×</button>
        </div>
        <div class="files-breadcrumb" id="filesBreadcrumb">Loading...</div>
        <div class="files-list" id="filesList"></div>
    </div>

    <!-- File Viewer Modal -->
    <div class="file-viewer" id="fileViewer">
        <div class="file-viewer-header">
            <span class="file-viewer-title" id="fileViewerTitle">filename.txt</span>
            <div class="file-viewer-header-btns">
                <button class="btn btn-edit" id="editBtn" onclick="startEditing()">✏️ Edit</button>
                <button class="files-close" onclick="closeFileViewer()">✕</button>
            </div>
        </div>
        <div class="file-viewer-content" id="viewerContent">
            <pre><code id="fileViewerContent"></code></pre>
        </div>
        <div class="image-preview-container" id="imageContent" style="display: none;">
            <img id="imagePreview" src="" alt="Preview">
        </div>
        <div class="file-viewer-content" id="editorContent" style="display: none; padding: 0;">
            <textarea class="file-editor" id="fileEditor"></textarea>
        </div>
        <div class="file-viewer-actions" id="editorActions" style="display: none;">
            <button type="button" class="btn btn-save" onclick="saveFile()">Save</button>
            <button type="button" class="btn btn-cancel" onclick="cancelEditing()">Cancel</button>
        </div>
    </div>

    <!-- Settings Panel (hidden by default) -->
    <div id="settingsPanel"
        style="display: none; position: fixed; top: 0; left: var(--sidebar-collapsed); right: 0; bottom: 0; background: var(--bg-dark); z-index: 50; padding-top: 60px; transition: left 0.25s ease;">
        <div class="header" style="position: absolute; top: 0; left: 0; right: 0;">
            <span style="font-size: 18px; font-weight: 600;">Settings</span>
            <div></div>
        </div>

        <div style="padding: 16px; height: calc(100% - 60px); overflow-y: auto;">
            <div class="settings-section">
                <div class="settings-title">Connection</div>
                <div class="card">
                    <div class="setting-row">
                        <div class="setting-label">
                            <h4>CDP Protocol</h4>
                            <p>Chrome DevTools connection</p>
                        </div>
                        <div id="cdpStatus" class="setting-value">...</div>
                    </div>
                    <div class="setting-row">
                        <div class="setting-label">
                            <h4>WebSocket</h4>
                            <p>Real-time updates</p>
                        </div>
                        <div id="wsStatus" class="setting-value">...</div>
                    </div>
                </div>
            </div>

            <div class="settings-section">
                <div class="settings-title">Preferences</div>
                <div class="card">
                    <div class="setting-row">
                        <div class="setting-label">
                            <h4>Refresh Interval</h4>
                            <p>Auto-capture frequency</p>
                        </div>
                        <select id="refreshInterval" class="setting-value" style="border: none; cursor: pointer;">
                            <option value="1000">1s</option>
                            <option value="2000" selected>2s</option>
                            <option value="3000">3s</option>
                            <option value="5000">5s</option>
                        </select>
                    </div>
                    <div class="setting-row">
                        <div class="setting-label">
                            <h4>Theme</h4>
                            <p>Choose app appearance</p>
                        </div>
                        <select id="themeSelect" class="setting-value" style="border: none; cursor: pointer;"
                            onchange="setTheme(this.value)">
                            <option value="dark">Dark</option>
                            <option value="light">Light</option>
                            <option value="pastel">Pastel</option>
                            <option value="rainbow">Rainbow</option>
                            <option value="slate">Slate</option>
                        </select>
                    </div>

                </div>
            </div>

            <div class="settings-section">
                <div class="settings-title">View Mode</div>
                <div class="card">
                    <div class="setting-row">
                        <div class="setting-label">
                            <h4>Lite Mode</h4>
                            <p>Chat-only lightweight view</p>
                        </div>
                        <a href="/minimal.html" class="btn btn-primary"
                            style="padding: 8px 16px; font-size: 12px; text-decoration: none; width: max-content; flex: none;">Switch
                            →</a>
                    </div>
                </div>
            </div>

            <div class="settings-section">
                <div class="settings-title">⚡ Quick Commands</div>
                <div class="card" id="mobileCommandsContainer">
                    <div style="color: var(--text-muted); padding: 8px;">Loading commands...</div>
                </div>
            </div>

            <div class="settings-section">
                <div class="settings-title" style="display: flex; align-items: center; justify-content: space-between;">
                    <span style="display: flex; align-items: center; gap: 8px;"><svg class="section-icon"
                            viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 20V10"></path>
                            <path d="M18 20V4"></path>
                            <path d="M6 20v-4"></path>
                        </svg> Model Quota</span>
                    <button class="quota-refresh-btn" onclick="loadQuota()"><svg class="btn-icon" viewBox="0 0 24 24"
                            fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="23 4 23 10 17 10"></polyline>
                            <path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"></path>
                        </svg> Refresh</button>
                </div>
                <div class="card">
                    <div id="quotaContainer">
                        <div class="quota-loading">
                            <div class="spinner"></div>
                            <div style="margin-top: 10px;">Loading quota data...</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Assist Panel (Chat UI) -->
    <div id="assistPanel"
        style="display: none; position: fixed; top: 0; left: var(--sidebar-collapsed); right: 0; bottom: 0; background: var(--bg-dark); z-index: 50; padding-top: 60px; transition: left 0.25s ease;">

        <!-- Header -->
        <div class="header"
            style="position: absolute; top: 0; left: 0; right: 0; display: flex; align-items: center; justify-content: space-between; padding: 0 16px;">
            <span style="font-size: 18px; font-weight: 600; display:flex; align-items:center; gap:6px;"><svg width="20"
                    height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                    stroke-linecap="round" stroke-linejoin="round"
                    style="flex-shrink:0;min-width:20px;min-height:20px;">
                    <rect x="3" y="11" width="18" height="10" rx="2" />
                    <circle cx="12" cy="5" r="2" />
                    <path d="M12 7v4" />
                    <line x1="8" y1="16" x2="8" y2="16" />
                    <line x1="16" y1="16" x2="16" y2="16" />
                </svg> Assist</span>
            <div id="assistStatusBadge"
                style="font-size: 11px; padding: 4px 10px; border-radius: 20px; background: rgba(255,255,255,0.08); color: var(--text-muted);">
                <svg width="10" height="10" viewBox="0 0 16 16" style="vertical-align:middle;margin-right:4px;">
                    <circle cx="8" cy="8" r="5" fill="#6b7280" />
                </svg>Idle
            </div>
        </div>

        <!-- Chat Messages -->
        <div id="assistChatMessages"
            style="position: absolute; top: 52px; left: 0; right: 0; bottom: 60px; overflow-y: auto; padding: 16px; display: flex; flex-direction: column; gap: 12px;">
            <div style="text-align: center; color: var(--text-muted); font-size: 13px; padding: 40px 20px;">
                <div style="margin-bottom: 12px; color:var(--accent-primary);"><svg width="40" height="40"
                        viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round">
                        <rect x="3" y="11" width="18" height="10" rx="2" />
                        <circle cx="12" cy="5" r="2" />
                        <path d="M12 7v4" />
                        <line x1="8" y1="16" x2="8" y2="16" />
                        <line x1="16" y1="16" x2="16" y2="16" />
                    </svg></div>
                <div style="font-weight: 600; margin-bottom: 4px;">Supervisor Assist</div>
                <div>Chat with your AI supervisor. Ask about agent activity, project status, or give instructions.</div>
            </div>
        </div>

        <!-- Task Queue (collapsible) -->
        <div id="assistTaskQueue"
            style="position: absolute; bottom: 60px; left: 0; right: 0; max-height: 200px; overflow-y: auto; background: var(--bg-dark); border-top: 1px solid var(--border); display: none;">
            <div onclick="toggleTaskQueue()"
                style="padding: 8px 16px; cursor: pointer; display: flex; align-items: center; justify-content: space-between; background: rgba(255,255,255,0.03);">
                <span
                    style="font-size: 12px; font-weight: 600; color: var(--text-muted); display:flex; align-items:center; gap:4px;"><svg
                        width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round">
                        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2" />
                        <rect x="8" y="2" width="8" height="4" rx="1" />
                    </svg> Task Queue <span id="taskQueueCount" style="color: var(--accent-primary);">(0)</span></span>
                <span id="taskQueueArrow" style="font-size: 10px; color: var(--text-muted);">&#9660;</span>
            </div>
            <div id="taskQueueItems" style="display: none; padding: 0 16px 8px;"></div>
            <div id="taskQueueInput" style="display: none; padding: 4px 16px 8px;">
                <div style="display: flex; gap: 6px;">
                    <input type="text" id="taskQueueAddInput"
                        style="flex: 1; padding: 6px 10px; background: var(--bg-glass); border: 1px solid var(--border); border-radius: 8px; color: var(--text-primary); font-size: 12px; outline: none;"
                        placeholder="Add a task to the queue..." onkeydown="if(event.key==='Enter'){addQueueTask();}">
                    <button onclick="addQueueTask()"
                        style="padding: 6px 12px; background: var(--accent-primary); border: none; border-radius: 8px; color: white; font-size: 11px; cursor: pointer; white-space: nowrap;">+
                        Add</button>
                </div>
            </div>
        </div>

        <!-- Chat Input -->
        <div
            style="position: absolute; bottom: 0; left: 0; right: 0; padding: 10px 16px; background: var(--bg-dark); border-top: 1px solid var(--border);">
            <div style="display: flex; gap: 8px; align-items: center;">
                <input type="text" id="assistChatInput"
                    style="flex: 1; padding: 10px 14px; background: var(--bg-glass); border: 1px solid var(--border); border-radius: 12px; color: var(--text-primary); font-size: 14px; outline: none;"
                    placeholder="Ask the supervisor..."
                    onkeydown="if(event.key==='Enter'&&!event.shiftKey){event.preventDefault();sendAssistChat();}">
                <button id="assistSendBtn" onclick="sendAssistChat()"
                    style="width: 40px; height: 40px; border-radius: 12px; background: var(--accent-primary); border: none; color: white; cursor: pointer; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                        style="width: 18px; height: 18px;">
                        <line x1="22" y1="2" x2="11" y2="13"></line>
                        <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                    </svg>
                </button>
            </div>
        </div>
    </div>

    <div id="toastContainer" class="toast-container"></div>

    <!-- JS -->
</body>

</html>
```

## File: payload\public\manifest.json
```
{
    "name": "Antigravity Control",
    "short_name": "Antigravity",
    "description": "Mobile control panel for Antigravity",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#050508",
    "theme_color": "#050508",
    "orientation": "portrait",
    "icons": [
        {
            "src": "/icon-192.png",
            "sizes": "192x192",
            "type": "image/png",
            "purpose": "any maskable"
        },
        {
            "src": "/icon-512.png",
            "sizes": "512x512",
            "type": "image/png",
            "purpose": "any maskable"
        }
    ]
}
```

## File: payload\public\minimal.html
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Antigravity - Lite</title>
    <link rel="icon"
        href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>">
    <style>
        :root {
            --bg-dark: #050508;
            --bg-card: rgba(15, 15, 25, 0.8);
            --accent-primary: #8b5cf6;
            --text-primary: #ffffff;
            --text-secondary: rgba(255, 255, 255, 0.7);
            --text-muted: rgba(255, 255, 255, 0.4);
            --border: rgba(255, 255, 255, 0.08);
            --success: #22c55e;
            --error: #ef4444;
        }

        .light-theme {
            --bg-dark: #f5f5f7;
            --bg-card: rgba(255, 255, 255, 0.9);
            --text-primary: #1a1a1a;
            --text-secondary: rgba(0, 0, 0, 0.7);
            --text-muted: rgba(0, 0, 0, 0.4);
            --border: rgba(0, 0, 0, 0.1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg-dark);
            color: var(--text-primary);
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        /* Header */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 16px;
            background: var(--bg-card);
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .header-left {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .logo-icon {
            font-size: 24px;
        }

        .logo-text {
            font-size: 16px;
            font-weight: 700;
            background: linear-gradient(135deg, var(--accent-primary), #6366f1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--error);
        }

        .status-dot.connected {
            background: var(--success);
            box-shadow: 0 0 8px var(--success);
        }

        .header-right {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .icon-btn {
            width: 36px;
            height: 36px;
            border: none;
            background: rgba(255, 255, 255, 0.05);
            color: var(--text-secondary);
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }

        .icon-btn:hover {
            background: rgba(139, 92, 246, 0.2);
            color: var(--accent-primary);
        }

        .full-mode-link {
            font-size: 11px;
            color: var(--text-muted);
            text-decoration: none;
            padding: 6px 10px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 8px;
            transition: all 0.2s;
        }

        .full-mode-link:hover {
            background: rgba(139, 92, 246, 0.2);
            color: var(--accent-primary);
        }

        /* Login Screen */
        .login-screen {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: var(--bg-dark);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
        }

        .login-screen.hidden {
            display: none;
        }

        .login-card {
            text-align: center;
            padding: 32px;
        }

        .login-logo {
            font-size: 48px;
            margin-bottom: 16px;
        }

        .login-title {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 8px;
        }

        .login-subtitle {
            font-size: 13px;
            color: var(--text-muted);
            margin-bottom: 24px;
        }

        .pin-input {
            width: 200px;
            padding: 14px 20px;
            font-size: 24px;
            text-align: center;
            letter-spacing: 8px;
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            color: var(--text-primary);
            margin-bottom: 16px;
        }

        .pin-input:focus {
            outline: none;
            border-color: var(--accent-primary);
        }

        .login-btn {
            width: 200px;
            padding: 14px;
            background: linear-gradient(135deg, var(--accent-primary), #6366f1);
            border: none;
            border-radius: 12px;
            color: white;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
        }

        .login-error {
            color: var(--error);
            font-size: 13px;
            margin-top: 12px;
        }

        /* Chat Container */
        .chat-container {
            flex: 1;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .cascade-view {
            flex: 1;
            overflow-y: auto;
            padding: 16px;
            min-height: 0;
            -webkit-overflow-scrolling: touch;
        }

        /* Force native touch scrolling even if IDE injects touch-action: none */
        .cascade-view * {
            touch-action: auto !important;
            overscroll-behavior: auto !important;
        }

        .chat-empty {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            color: var(--text-muted);
            font-size: 14px;
            gap: 8px;
        }

        .chat-empty .icon {
            font-size: 40px;
            opacity: 0.5;
        }

        /* Input Area - Stays at bottom via flex */
        .input-area {
            padding: 12px 16px;
            background: var(--bg-card);
            border-top: 1px solid var(--border);
            flex-shrink: 0;
            /* Don't shrink, stay at natural height */
        }

        .quick-chips {
            display: flex;
            gap: 8px;
            margin-bottom: 10px;
            overflow-x: auto;
            padding-bottom: 4px;
        }

        .quick-chip {
            padding: 6px 14px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            border-radius: 20px;
            color: var(--text-secondary);
            font-size: 13px;
            white-space: nowrap;
            cursor: pointer;
            transition: all 0.2s;
        }

        .quick-chip:hover {
            background: rgba(139, 92, 246, 0.15);
            border-color: rgba(139, 92, 246, 0.4);
            color: var(--accent-primary);
        }

        .input-row {
            display: flex;
            gap: 10px;
        }

        .chat-input {
            flex: 1;
            padding: 12px 16px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            border-radius: 24px;
            color: var(--text-primary);
            font-size: 14px;
        }

        .chat-input:focus {
            outline: none;
            border-color: var(--accent-primary);
        }

        .chat-input::placeholder {
            color: var(--text-muted);
        }

        .send-btn {
            width: 44px;
            height: 44px;
            border: none;
            background: linear-gradient(135deg, var(--accent-primary), #6366f1);
            border-radius: 50%;
            color: white;
            font-size: 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Toast */
        .toast-container {
            position: fixed;
            bottom: 100px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000;
        }

        .toast {
            padding: 12px 18px;
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            color: var(--text-primary);
            font-size: 13px;
            animation: toastIn 0.3s ease;
        }

        .toast.success {
            border-color: var(--success);
        }

        .toast.error {
            border-color: var(--error);
        }

        @keyframes toastIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Cascade content styling - control injected IDE content */
        .cascade-view {
            flex: 1;
            overflow-y: auto;
            overflow-x: hidden;
            padding: 8px;
            position: relative;
            min-height: 0;
            /* Important for flex children */
        }

        /* Force readable text and control layout */
        .cascade-view,
        .cascade-view * {
            color: var(--text-primary) !important;
            max-width: 100% !important;
            box-sizing: border-box !important;
        }

        .cascade-view a {
            color: var(--accent-primary) !important;
        }

        /* Light theme overrides */
        .light-theme .cascade-view {
            background: #ffffff !important;
        }

        /* Ensure images and content don't overflow */
        .cascade-view img,
        .cascade-view svg {
            max-width: 100% !important;
            height: auto !important;
        }

        /* Reset raw buttons inside cascade to prevent native browser gray filling */
        .cascade-view button {
            background: transparent;
            border: none;
            padding: 0;
            margin: 0;
            appearance: none;
        }

        /* Remote Prompts History Display */
        .remote-prompts-container {
            width: 100%;
            max-height: 120px;
            overflow-y: hidden;
            scroll-behavior: smooth;
            pointer-events: none;
            display: flex;
            flex-direction: column;
            gap: 4px;
            padding: 0 16px 8px 16px;
            mask-image: linear-gradient(to bottom, transparent, black 15%, black 100%);
            -webkit-mask-image: linear-gradient(to bottom, transparent, black 15%, black 100%);
        }

        .remote-prompt-item {
            font-size: 13px;
            color: var(--text-secondary);
            background: rgba(255, 255, 255, 0.05);
            /* Same as --bg-glass */
            padding: 8px 12px;
            border-radius: 8px;
            border: 1px solid var(--border);
            width: fit-content;
            max-width: 90%;
            align-self: flex-end;
            animation: slideInUp 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            word-wrap: break-word;
        }

        .remote-prompt-item:last-child {
            color: var(--text-primary);
            border-color: var(--accent-primary);
            background: rgba(14, 165, 233, 0.1);
        }

        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(10px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Control any absolutely positioned or oversized elements */
        .cascade-view>div,
        .cascade-view>div>div,
        .cascade-view>div>div>div,
        .cascade-view>div>div>div>div,
        .cascade-view>div>div>div>div>div {
            max-height: none !important;
            min-height: 0 !important;
            height: auto !important;
            position: relative !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        /* Collapse empty elements */
        .cascade-view>div:empty,
        .cascade-view>div>div:empty {
            display: none !important;
        }

        /* Remove any fixed heights from wrappers */
        .cascade-view [style*="height"]:not(img):not(svg):not(video) {
            height: auto !important;
            min-height: 0 !important;
            max-height: none !important;
        }

        /* Hide the virtualized scroll placeholder divs (gray loading boxes) */
        .cascade-view .bg-gray-500\/10:not(:has(*)),
        .cascade-view [class*="bg-gray-500"]:not(:has(*)) {
            display: none !important;
        }

        /* Also target by the rounded-lg class pattern often used with placeholders */
        .cascade-view .rounded-lg.bg-gray-500\/10 {
            display: none !important;
        }

        /* Flatten nested flex containers */
        .cascade-view [style*="display: flex"],
        .cascade-view [style*="display:flex"] {
            display: block !important;
        }

        /* Reset any flex containers that might cause issues */
        .cascade-view [style*="flex"] {
            flex: 0 0 auto !important;
        }

        /* Prevent fixed/absolute positioning from breaking layout */
        .cascade-view [style*="position: fixed"],
        .cascade-view [style*="position: absolute"] {
            position: relative !important;
        }

        /* Hide elements with extremely large min-height (virtualized scroll containers) */
        .cascade-view [style*="min-height"] {
            min-height: 0 !important;
        }

        /* Dynamic viewport height support for modern browsers */
        @supports (height: 100dvh) {
            body {
                height: 100dvh;
            }
        }

        /* Mobile-specific fixes (up to 767px) */
        @media screen and (max-width: 767px) {
            body {
                height: 100vh;
                height: 100dvh;
                /* Dynamic viewport height - accounts for mobile browser chrome */
                min-height: 0;
                overflow: hidden;
            }

            .chat-container {
                flex: 1 1 0;
                min-height: 0;
                display: flex;
                flex-direction: column;
                overflow: hidden;
            }

            .cascade-view {
                flex: 1 1 0;
                min-height: 0;
                overflow-y: auto;
                overflow-x: hidden;
                -webkit-overflow-scrolling: touch;
            }

            .input-area {
                flex-shrink: 0;
                position: sticky;
                bottom: 0;
                left: 0;
                right: 0;
                padding: 10px 12px;
                padding-bottom: max(10px, env(safe-area-inset-bottom));
                background: var(--bg-card);
                border-top: 1px solid var(--border);
                z-index: 50;
            }

            .quick-chips {
                gap: 6px;
                margin-bottom: 8px;
            }

            .quick-chip {
                padding: 5px 10px;
                font-size: 12px;
            }

            .input-row {
                gap: 8px;
            }

            .chat-input {
                padding: 10px 14px;
                font-size: 16px;
                /* Prevents iOS zoom on focus */
            }

            .send-btn {
                width: 40px;
                height: 40px;
                flex-shrink: 0;
            }

            .header {
                padding: 10px 12px;
            }
        }

        /* Tablet-specific fixes (768px - 1024px) */
        @media screen and (min-width: 768px) and (max-width: 1024px) {
            body {
                height: 100vh;
                height: 100dvh;
                /* Dynamic viewport height for better tablet support */
                min-height: 0;
                overflow: hidden;
            }

            .chat-container {
                flex: 1 1 0;
                min-height: 0;
                display: flex;
                flex-direction: column;
                overflow: hidden;
            }

            .cascade-view {
                flex: 1 1 0;
                min-height: 0;
                overflow-y: auto;
                -webkit-overflow-scrolling: touch;
            }

            .input-area {
                flex-shrink: 0;
                position: sticky;
                bottom: 0;
                padding-bottom: max(12px, env(safe-area-inset-bottom));
                z-index: 50;
            }
        }

        /* Keyboard visibility handling via visualViewport API */
        .keyboard-open .cascade-view {
            max-height: 40vh !important;
        }
    </style>
</head>

<body>
    <!-- Login Screen -->
    <div class="login-screen hidden" id="loginScreen">
        <div class="login-card">
            <div class="login-logo">🔐</div>
            <div class="login-title">Enter PIN</div>
            <div class="login-subtitle">Authentication required</div>
            <input type="tel" class="pin-input" id="pinInput" maxlength="6" placeholder="••••" autocomplete="off">
            <button class="login-btn" onclick="submitPin()">Unlock</button>
            <div class="login-error" id="loginError" style="display: none;"></div>
        </div>
    </div>

    <!-- Header -->
    <header class="header">
        <div class="header-left">
            <div class="logo">
                <span class="logo-icon">⚡</span>
                <span class="logo-text">Antigravity</span>
            </div>
            <div class="status-dot" id="statusDot"></div>
        </div>
        <div class="header-right">
            <button class="icon-btn" id="themeToggle" onclick="toggleTheme()">🌙</button>
            <a href="/" class="full-mode-link">Dashboard →</a>
        </div>
    </header>

    <!-- Chat Container -->
    <div class="chat-container">
        <div class="cascade-view" id="cascade-container">
            <div class="chat-empty">
                <span class="icon">💬</span>
                <span>Connecting to Antigravity...</span>
            </div>
        </div>

        <!-- Remote Prompt History -->
        <div id="remotePrompts" class="remote-prompts-container"></div>

        <div class="input-area">
            <div class="quick-chips">
                <button class="quick-chip" onclick="sendQuick('continue')">Continue</button>
                <button class="quick-chip" onclick="sendQuick('yes')">Yes</button>
                <button class="quick-chip" onclick="sendQuick('no')">No</button>
            </div>
            <div class="input-row">
                <input type="text" class="chat-input" id="chatInput" placeholder="Send a message..."
                    onkeypress="if(event.key==='Enter')sendMessage()">
                <button class="send-btn" onclick="sendMessage()">➤</button>
            </div>
        </div>
    </div>

    <!-- Toast Container -->
    <div class="toast-container" id="toastContainer"></div>

    <script>
        const serverUrl = window.location.origin;
        let authToken = localStorage.getItem('authToken');
        let ws = null;
        let lastCascadeHash = null;
        let cssLoaded = false;

        // ====================================================================
        // Theme
        // ====================================================================
        function initTheme() {
            const saved = localStorage.getItem('theme') || 'dark';
            document.body.classList.toggle('light-theme', saved === 'light');
            updateThemeIcon();
        }

        function toggleTheme() {
            document.body.classList.toggle('light-theme');
            const theme = document.body.classList.contains('light-theme') ? 'light' : 'dark';
            localStorage.setItem('theme', theme);
            updateThemeIcon();
        }

        function updateThemeIcon() {
            const isLight = document.body.classList.contains('light-theme');
            document.getElementById('themeToggle').textContent = isLight ? '☀️' : '🌙';
        }

        // ====================================================================
        // Auth
        // ====================================================================
        async function authFetch(url, options = {}) {
            const headers = { ...(options.headers || {}) };
            if (authToken) {
                headers['Authorization'] = `Bearer ${authToken}`;
            }
            const res = await fetch(url, { ...options, headers });
            if (res.status === 401) {
                try {
                    const clonedRes = res.clone();
                    const data = await clonedRes.json();
                    if (data.needsAuth) {
                        authToken = null;
                        localStorage.removeItem('authToken');
                        showLoginScreen();
                    }
                } catch (e) { }
            }
            return res;
        }

        async function checkAuth() {
            try {
                // First check if auth is enabled (no token needed for this)
                const res = await fetch(`${serverUrl}/api/auth/status`);
                const data = await res.json();

                if (!data.authEnabled) {
                    // Auth not enabled, proceed without login
                    hideLoginScreen();
                    return true;
                }

                // Auth is enabled, check if we have a valid token
                if (authToken) {
                    const testRes = await authFetch(`${serverUrl}/api/status`);
                    if (testRes.ok) {
                        hideLoginScreen();
                        return true;
                    }
                }

                // Need to login
                showLoginScreen();
                return false;
            } catch (e) {
                console.error('Auth check failed:', e);
                return false;
            }
        }

        function showLoginScreen() {
            document.getElementById('loginScreen').classList.remove('hidden');
        }

        function hideLoginScreen() {
            document.getElementById('loginScreen').classList.add('hidden');
        }

        async function submitPin() {
            const pin = document.getElementById('pinInput').value;
            const errorEl = document.getElementById('loginError');
            try {
                const res = await fetch(`${serverUrl}/api/auth/login`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ pin })
                });
                const data = await res.json();
                if (data.success && data.token) {
                    authToken = data.token;
                    localStorage.setItem('authToken', authToken);
                    hideLoginScreen();
                    errorEl.style.display = 'none';
                    startPolling();
                } else {
                    errorEl.textContent = data.error || 'Invalid PIN';
                    errorEl.style.display = 'block';
                }
            } catch (e) {
                errorEl.textContent = 'Connection error';
                errorEl.style.display = 'block';
            }
        }

        // ====================================================================
        // WebSocket
        // ====================================================================
        function connectWebSocket() {
            const wsUrl = serverUrl.replace('http', 'ws') + '/ws';
            ws = new WebSocket(wsUrl);

            ws.onopen = () => {
                document.getElementById('statusDot').classList.add('connected');
            };

            ws.onclose = () => {
                document.getElementById('statusDot').classList.remove('connected');
                setTimeout(connectWebSocket, 3000);
            };

            ws.onerror = () => {
                document.getElementById('statusDot').classList.remove('connected');
            };
        }

        // ====================================================================
        // Chat Polling
        // ====================================================================
        let pollTimer = null;

        function startPolling() {
            if (pollTimer) return;
            fetchChat();
            pollTimer = setInterval(fetchChat, 2000);
        }

        async function fetchChat() {
            try {
                const res = await authFetch(`${serverUrl}/api/chat/snapshot`);
                if (!res.ok) return;
                const data = await res.json();

                if (data.html) {
                    const hash = simpleHash(data.html);
                    if (hash !== lastCascadeHash) {
                        lastCascadeHash = hash;

                        if (!cssLoaded && data.css) {
                            const style = document.createElement('style');
                            style.id = 'cascadeStyles';
                            style.textContent = data.css;
                            document.head.appendChild(style);
                            cssLoaded = true;
                        }

                        const container = document.getElementById('cascade-container');
                        container.innerHTML = data.html;

                        // Scroll to bottom - find the last actual content element
                        setTimeout(() => {
                            // Try to find the last meaningful element
                            const lastElement = container.querySelector(':scope > div:last-child') || container.lastElementChild;
                            if (lastElement) {
                                lastElement.scrollIntoView({ behavior: 'instant', block: 'end' });
                            } else {
                                container.scrollTop = container.scrollHeight;
                            }
                        }, 100);
                    }
                } else if (data.error) {
                    document.getElementById('cascade-container').innerHTML = `
                        <div class="chat-empty">
                            <span class="icon">⚠️</span>
                            <span>${data.error}</span>
                        </div>
                    `;
                }
            } catch (e) {
                console.log('Chat fetch error:', e);
            }
        }

        function simpleHash(str) {
            let hash = 0;
            for (let i = 0; i < str.length; i++) {
                const char = str.charCodeAt(i);
                hash = ((hash << 5) - hash) + char;
                hash = hash & hash;
            }
            return hash;
        }

        // ====================================================================
        // Send Message
        // ====================================================================
        async function sendMessage() {
            const input = document.getElementById('chatInput');
            const text = input.value.trim();
            if (!text) return;

            try {
                const res = await authFetch(`${serverUrl}/api/cdp/inject`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text, submit: true })
                });
                const result = await res.json();
                if (result.success) {
                    input.value = '';
                    showToast('Sent!', 'success');
                } else {
                    throw new Error(result.error);
                }
            } catch (e) {
                showToast('Failed to send', 'error');
            }
        }

        function sendQuick(cmd) {
            document.getElementById('chatInput').value = cmd;
            sendMessage();
        }

        // ====================================================================
        // Message Handling & Remote Prompts
        // ====================================================================
        let remotePrompts = [];

        function renderRemotePrompts() {
            const container = document.getElementById('remotePrompts');
            if (!container) return;

            if (remotePrompts.length > 3) remotePrompts.shift();

            if (remotePrompts.length === 0) {
                container.innerHTML = '';
                return;
            }

            container.innerHTML = remotePrompts.map(msg => `
                <div class="remote-prompt-item">${escapeHtml(msg.content)}</div>
            `).join('');

            container.scrollTop = container.scrollHeight;
        }

        // Escape HTML for minimal view
        function escapeHtml(unsafe) {
            return (unsafe || '').toString()
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#039;");
        }

        function handleMessage(data) {
            if (data.event === 'history' && Array.isArray(data.data.messages)) {
                const prompts = data.data.messages.filter(m => m.type === 'user' || m.type === 'mobile_command');
                prompts.forEach(msg => {
                    const isDuplicate = remotePrompts.length > 0 && remotePrompts[remotePrompts.length - 1].content === msg.content;
                    if (!isDuplicate) remotePrompts.push(msg);
                });
                renderRemotePrompts();
            } else if (data.event === 'message' || data.event === 'mobile_command') {
                if (data.data && (data.data.type === 'user' || data.data.type === 'mobile_command')) {
                    const isDuplicate = remotePrompts.length > 0 && remotePrompts[remotePrompts.length - 1].content === data.data.content;
                    if (!isDuplicate) {
                        remotePrompts.push(data.data);
                        renderRemotePrompts();
                    }
                }
            }
        }

        // ====================================================================
        // Toast
        // ====================================================================
        function showToast(message, type = 'info') {
            const container = document.getElementById('toastContainer');
            const toast = document.createElement('div');
            toast.className = `toast ${type}`;
            toast.textContent = message;
            container.appendChild(toast);
            setTimeout(() => toast.remove(), 3000);
        }

        // ====================================================================
        // Init
        // ====================================================================
        initTheme();
        checkAuth().then((authOk) => {
            if (authOk) {
                connectWebSocket();
                startPolling();
            }
        });

        // PIN input - auto-focus and enter to submit
        document.getElementById('pinInput').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') submitPin();
        });

        // ====================================================================
        // Mobile Keyboard Detection using visualViewport API
        // ====================================================================
        if (window.visualViewport) {
            const initialHeight = window.visualViewport.height;

            window.visualViewport.addEventListener('resize', () => {
                const currentHeight = window.visualViewport.height;
                const keyboardOpen = currentHeight < initialHeight * 0.8;

                document.body.classList.toggle('keyboard-open', keyboardOpen);

                // Ensure input stays visible when keyboard opens
                if (keyboardOpen) {
                    const inputArea = document.querySelector('.input-area');
                    if (inputArea) {
                        inputArea.scrollIntoView({ behavior: 'instant', block: 'end' });
                    }
                }
            });
        }

        // Handle iOS Safari focus quirks
        document.getElementById('chatInput').addEventListener('focus', () => {
            setTimeout(() => {
                const inputArea = document.querySelector('.input-area');
                if (inputArea) {
                    inputArea.scrollIntoView({ behavior: 'instant', block: 'end' });
                }
            }, 300);
        });
    </script>
</body>

</html>
```

## File: payload\public\sw.js
```
/**
 * Antigravity Control - Service Worker
 * Provides offline caching and PWA functionality
 */

const CACHE_NAME = 'antigravity-v2';
const STATIC_ASSETS = [
    '/',
    '/index.html',
    '/manifest.json',
    '/icon-192.png',
    '/icon-512.png',
    '/apple-touch-icon.png'
];

// Install: cache static assets
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(STATIC_ASSETS);
        })
    );
    self.skipWaiting();
});

// Activate: clean up old caches
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames
                    .filter((name) => name !== CACHE_NAME)
                    .map((name) => caches.delete(name))
            );
        })
    );
    self.clients.claim();
});

// Fetch: network-first for API and HTML, cache-first for images/manifest
self.addEventListener('fetch', (event) => {
    const url = new URL(event.request.url);

    // Skip non-GET requests
    if (event.request.method !== 'GET') {
        return;
    }

    // API calls and HTML pages: always try network first
    if (url.pathname.startsWith('/api/') ||
        url.pathname.endsWith('.html') ||
        url.pathname === '/') {
        event.respondWith(
            fetch(event.request)
                .then((response) => {
                    // Cache the fresh response
                    if (response.ok && url.origin === self.location.origin) {
                        const clone = response.clone();
                        caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
                    }
                    return response;
                })
                .catch(() => caches.match(event.request))
        );
        return;
    }

    // Static assets (images, manifest, icons): cache-first
    event.respondWith(
        caches.match(event.request).then((cached) => {
            if (cached) {
                return cached;
            }
            return fetch(event.request).then((response) => {
                if (response.ok && url.origin === self.location.origin) {
                    const responseClone = response.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseClone);
                    });
                }
                return response;
            });
        })
    );
});

```

## File: payload\public\_DIR_IDENTITY.md
```
---
id: ecosystem-plugins-repo-fetched-antigravity-mobile-035838-public
name: Public
path: ecosystem/plugins/repo-fetched-antigravity-mobile-035838/public
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Public
Storage area for 'public' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: payload\public\css\assist.css
```
/* ============================================
 * Assist — Login, image preview, animations
 * ============================================ */

        /* Login Screen */
        .login-screen {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: var(--bg-dark);
            z-index: 2000;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .login-screen.hidden {
            display: none;
        }

        .login-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 40px 30px;
            max-width: 320px;
            width: 100%;
            text-align: center;
        }

        .login-logo {
            font-size: 48px;
            margin-bottom: 16px;
        }

        .login-title {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .login-subtitle {
            color: var(--text-muted);
            font-size: 14px;
            margin-bottom: 30px;
        }

        .pin-input {
            width: 100%;
            padding: 16px;
            font-size: 24px;
            text-align: center;
            letter-spacing: 8px;
            background: var(--bg-glass);
            border: 1px solid var(--border);
            border-radius: 12px;
            color: var(--text-primary);
            margin-bottom: 20px;
            -webkit-text-security: disc;
        }

        .pin-input:focus {
            outline: none;
            border-color: var(--accent-primary);
        }

        .login-btn {
            width: 100%;
            padding: 16px;
            background: var(--accent-primary);
            border: none;
            border-radius: 12px;
            color: white;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
        }

        .login-btn:hover {
            transform: scale(1.02);
        }

        .login-error {
            color: var(--error);
            font-size: 14px;
            margin-top: 16px;
        }

        /* Image Preview */
        .image-preview-container {
            position: fixed !important;
            top: 60px;
            left: 0;
            width: 100vw;
            height: calc(100vh - 60px);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: #111;
            z-index: 250;
            box-sizing: border-box;
        }

        .zoom-controls {
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 6px 12px;
            background: rgba(0, 0, 0, 0.7);
            border-radius: 20px;
            z-index: 10;
        }

        .zoom-btn {
            width: 32px;
            height: 32px;
            border: none;
            background: rgba(255, 255, 255, 0.15);
            color: white;
            font-size: 18px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .zoom-btn:active {
            background: rgba(255, 255, 255, 0.3);
        }

        .zoom-level {
            color: white;
            font-size: 13px;
            font-weight: 600;
            min-width: 50px;
            text-align: center;
        }

        .image-wrapper {
            flex: 1;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            width: 100% !important;
            height: 100% !important;
            overflow: auto !important;
            touch-action: pinch-zoom pan-x pan-y;
        }

        .image-wrapper img {
            max-width: none !important;
            max-height: none !important;
            width: auto !important;
            height: auto !important;
            object-fit: contain;
            transition: transform 0.15s ease-out;
            border-radius: 4px;
        }

        .zoom-hint {
            position: absolute;
            bottom: 12px;
            left: 50%;
            transform: translateX(-50%);
            color: rgba(255, 255, 255, 0.5);
            font-size: 11px;
            padding: 4px 12px;
            background: rgba(0, 0, 0, 0.5);
            border-radius: 12px;
        }

        @keyframes blink {
            0% {
                opacity: .2;
            }

            20% {
                opacity: 1;
            }

            100% {
                opacity: .2;
            }
        }

```

## File: payload\public\css\chat.css
```
/* ============================================
 * Chat — Input, messages, code blocks
 * ============================================ */

        /* Chat Input */
        .chat-input-area {
            padding: 12px 16px;
            background: rgba(0, 0, 0, 0.3);
            border-top: 1px solid var(--border);
            flex-shrink: 0;
        }

        .chat-input-wrapper {
            display: flex;
            gap: 10px;
            align-items: center;
        }

        .chat-input {
            flex: 1;
            padding: 14px 18px;
            background: var(--bg-glass);
            border: 1px solid var(--border);
            border-radius: 24px;
            color: var(--text-primary);
            font-size: 15px;
            outline: none;
            transition: all 0.3s;
        }

        .chat-input::placeholder {
            color: var(--text-muted);
        }

        .chat-input:focus {
            border-color: var(--accent-primary);
            box-shadow: 0 0 0 3px var(--accent-glow);
        }

        .chat-send {
            width: 48px;
            min-width: 48px;
            height: 48px;
            background: var(--accent-primary);
            border: none;
            border-radius: 50%;
            color: white;
            font-size: 20px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
            box-shadow: 0 4px 16px var(--accent-glow);
            flex-shrink: 0;
        }

        .chat-send:hover {
            transform: scale(1.05);
        }

        .chat-send:active {
            transform: scale(0.95);
        }

```

## File: payload\public\css\components.css
```
/* ============================================
 * Components — Panels, selectors, nav, prompts
 * ============================================ */


.logo-icon {
    width: 36px;
    height: 36px;
    background: var(--accent-primary);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
}

.logo-text {
    font-size: 20px;
    font-weight: 700;
    color: var(--text-primary);
}

.status-pill {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 6px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
    width: 100%;
    justify-content: center;
    margin-bottom: 8px;
}

.status-pill .status-text {
    display: none;
}

.sidebar.expanded .status-pill .status-text {
    display: inline;
}

.status-pill.connected {
    background: rgba(34, 197, 94, 0.15);
    color: var(--success);
    border: 1px solid rgba(34, 197, 94, 0.3);
}

.status-pill.disconnected {
    background: rgba(239, 68, 68, 0.15);
    color: var(--error);
    border: 1px solid rgba(239, 68, 68, 0.3);
}

.status-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    animation: pulse 2s ease-in-out infinite;
}

.connected .status-dot {
    background: var(--success);
    box-shadow: 0 0 8px var(--success);
}

.disconnected .status-dot {
    background: var(--error);
}

@keyframes pulse {

    0%,
    100% {
        opacity: 1;
    }

    50% {
        opacity: 0.5;
    }
}

/* View Switcher */
.view-switcher {
    display: flex;
    gap: 4px;
    padding: 4px;
    margin: 12px 16px;
    background: var(--bg-glass);
    border-radius: 14px;
    border: 1px solid var(--border);
}

.view-btn {
    flex: 1;
    padding: 12px 16px;
    background: transparent;
    border: none;
    border-radius: 10px;
    color: var(--text-muted);
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}

.view-btn.active {
    background: var(--accent-primary);
    color: white;
    box-shadow: 0 4px 16px var(--accent-glow);
}

.view-btn:not(.active):hover {
    color: var(--text-secondary);
    background: rgba(255, 255, 255, 0.05);
}

/* Content */
.content {
    padding: 0;
    margin-left: var(--sidebar-collapsed);
    transition: margin-left 0.25s ease;
}

body.sidebar-expanded .content {
    margin-left: var(--sidebar-width);
}

.view {
    display: none;
    animation: fadeIn 0.3s ease;
}

.view.active {
    display: block;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(8px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Card */
.card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 16px;
    margin-bottom: 12px;
    backdrop-filter: blur(20px);
}

/* Screen Frame */
.screen-frame {
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 6px;
    position: relative;
    overflow: hidden;
}

.screen-img {
    width: 100%;
    border-radius: 10px;
    display: block;
    min-height: 200px;
    object-fit: contain;
    background: rgba(0, 0, 0, 0.3);
}

.screen-placeholder {
    width: 100%;
    min-height: 200px;
    border-radius: 10px;
    background: rgba(0, 0, 0, 0.3);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
    color: var(--text-muted);
}

.screen-placeholder .icon {
    font-size: 40px;
    opacity: 0.5;
}

/* Controls */
.controls {
    display: flex;
    gap: 10px;
    margin-top: 12px;
}

.btn {
    padding: 12px 20px;
    border: none;
    border-radius: 12px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
}

.btn-primary {
    background: var(--accent-primary);
    color: white;
    box-shadow: 0 4px 16px var(--accent-glow);
    flex: 1;
}

.btn-primary:hover {
    transform: translateY(-2px);
}

.btn-primary:active {
    transform: translateY(0);
}

.btn-icon {
    width: 44px;
    height: 44px;
    padding: 0;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    color: var(--text-secondary);
    font-size: 18px;
}

.btn-icon.active {
    background: rgba(139, 92, 246, 0.2);
    color: var(--accent-primary);
    border-color: var(--accent-primary);
}

/* Live indicator */
.live-badge {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 4px 8px;
    background: rgba(239, 68, 68, 0.2);
    border-radius: 6px;
    font-size: 10px;
    font-weight: 700;
    color: #ef4444;
    text-transform: uppercase;
}

.live-badge .dot {
    width: 5px;
    height: 5px;
    background: #ef4444;
    border-radius: 50%;
    animation: livePulse 1s infinite;
}

@keyframes livePulse {

    0%,
    100% {
        opacity: 1;
    }

    50% {
        opacity: 0.3;
    }
}

/* Chat View */
.chat-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    height: 100dvh;
    width: 100%;
    overflow: hidden;
}

.chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 12px;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

/* Cascade View - neutral container for IDE content */
.cascade-view {
    flex: 1;
    overflow-y: auto;
    overflow-x: hidden;
    padding: 8px;
    /* No background or custom styles - let IDE content dictate styling */
    position: relative;
    -webkit-overflow-scrolling: touch;
    overscroll-behavior-y: contain;
}

/* Keep touch scrolling enabled for injected IDE content */
.cascade-view * {
    touch-action: auto !important;
    overscroll-behavior: auto !important;
}

.cascade-view a {
    color: var(--accent-primary) !important;
}

/* Light theme overrides for cascade view */
.light-theme .cascade-view {
    background: #ffffff !important;
}

/* Ensure images and content don't overflow */
.cascade-view img,
.cascade-view svg {
    max-width: 100%;
    height: auto;
}

/* Actionable button highlighting in cascade */
.cascade-view [data-mobile-action] {
    position: relative;
    border: 1.5px solid var(--accent-primary) !important;
    border-radius: 8px !important;
    padding: 6px 14px !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    font-weight: 500 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    user-select: none;
}

.cascade-view [data-mobile-action]:active {
    transform: scale(0.95) !important;
}

.cascade-view [data-mobile-action="accept"] {
    background: rgba(16, 185, 129, 0.15) !important;
    border-color: #10b981 !important;
    color: #10b981 !important;
}

.cascade-view [data-mobile-action="reject"] {
    background: rgba(239, 68, 68, 0.15) !important;
    border-color: #ef4444 !important;
    color: #ef4444 !important;
}

.cascade-view [data-mobile-action="neutral"] {
    background: rgba(14, 165, 233, 0.12) !important;
    border-color: var(--accent-primary) !important;
    color: var(--accent-primary) !important;
}

/* Reset raw buttons inside cascade to prevent native browser gray filling */
.cascade-view button {
    background: transparent;
    border: none;
    padding: 0;
    margin: 0;
    appearance: none;
}


/* Remote Prompts History Display */
.remote-prompts-container {
    display: none;
}

.remote-prompt-item {
    font-size: 13px;
    color: var(--text-secondary);
    background: var(--bg-glass);
    padding: 8px 12px;
    border-radius: 8px;
    border: 1px solid var(--border);
    width: fit-content;
    max-width: 90%;
    align-self: flex-end;
    animation: slideInUp 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    word-wrap: break-word;
}

/* Highlight the most recent prompt */
.remote-prompt-item:last-child {
    color: var(--text-primary);
    border-color: var(--accent-primary);
    background: rgba(14, 165, 233, 0.1);
}

@keyframes slideInUp {
    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.chat-msg {
    max-width: 85%;
    padding: 12px 16px;
    border-radius: 18px;
    font-size: 14px;
    line-height: 1.5;
    animation: msgIn 0.3s ease;
}

@keyframes msgIn {
    from {
        opacity: 0;
        transform: translateY(10px) scale(0.95);
    }

    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.chat-msg.user {
    align-self: flex-end;
    background: var(--accent-primary);
    color: white;
    border-bottom-right-radius: 6px;
}

.chat-msg.agent {
    align-self: flex-start;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    color: var(--text-primary);
    border-bottom-left-radius: 6px;
}

.chat-msg.status {
    align-self: center;
    background: rgba(234, 179, 8, 0.15);
    border: 1px solid rgba(234, 179, 8, 0.3);
    color: var(--warning);
    font-size: 12px;
    padding: 8px 14px;
    border-radius: 20px;
}

.chat-msg.error {
    align-self: center;
    background: rgba(239, 68, 68, 0.15);
    border: 1px solid rgba(239, 68, 68, 0.3);
    color: var(--error);
    font-size: 12px;
}

.chat-msg-time {
    font-size: 10px;
    color: rgba(255, 255, 255, 0.5);
    margin-top: 4px;
}

.chat-msg.agent .chat-msg-time {
    color: var(--text-muted);
}

.chat-empty {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: var(--text-muted);
    gap: 10px;
}

.chat-empty .icon {
    font-size: 48px;
    opacity: 0.4;
}


/* Model/Mode Selector - Minimal Design */
.model-mode-row {
    position: relative;
    display: flex;
    gap: 8px;
    padding: 10px 12px;
    background: transparent;
    flex-shrink: 0;
    border-top: 1px solid var(--border);
}

.model-selector,
.mode-selector {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 6px 10px;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: 16px;
    color: var(--text-secondary);
    font-size: 12px;
    cursor: pointer;
    transition: all 0.2s;
}

.model-selector {
    flex: 1;
    overflow: hidden;
}

.model-selector:hover,
.mode-selector:hover {
    background: rgba(var(--accent-primary-rgb, 14, 165, 233), 0.15);
    border-color: var(--accent-primary);
    color: var(--text-primary);
}

.selector-icon {
    font-size: 14px;
}

.dropdown-arrow {
    font-size: 10px;
    opacity: 0.6;
}

#currentModelLabel {
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    text-align: left;
}

.model-dropdown,
.mode-dropdown {
    position: fixed;
    bottom: 120px;
    left: 12px;
    right: 12px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    max-height: 300px;
    overflow-y: auto;
    z-index: 9999;
}

.dropdown-header {
    padding: 12px 16px;
    font-weight: 600;
    color: var(--text-primary);
    border-bottom: 1px solid var(--border);
    font-size: 13px;
}

.dropdown-list {
    padding: 8px 0;
}

.dropdown-item {
    padding: 10px 16px;
    cursor: pointer;
    transition: background 0.15s;
}

.dropdown-item:hover {
    background: rgba(var(--accent-primary-rgb, 14, 165, 233), 0.1);
}

.dropdown-item.active {
    background: rgba(var(--accent-primary-rgb, 14, 165, 233), 0.2);
    color: var(--accent-primary);
}

.mode-name {
    font-weight: 600;
    color: var(--text-primary);
    font-size: 13px;
}

.mode-desc {
    font-size: 11px;
    color: var(--text-muted);
    margin-top: 2px;
}


/* Quick Actions in Chat */
.quick-actions {
    display: flex;
    gap: 8px;
    padding: 8px 12px;
    overflow-x: auto;
    scrollbar-width: none;
}

.quick-actions::-webkit-scrollbar {
    display: none;
}

.quick-chip {
    padding: 8px 14px;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: 20px;
    color: var(--text-secondary);
    font-size: 13px;
    white-space: nowrap;
    cursor: pointer;
    transition: all 0.2s;
}

.quick-chip:hover {
    background: rgba(139, 92, 246, 0.15);
    border-color: rgba(139, 92, 246, 0.4);
    color: var(--accent-primary);
}


/* Bottom Nav - Pill Style */
.bottom-nav {
    position: fixed;
    bottom: 16px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    padding: 6px;
    background: var(--bg-card);
    backdrop-filter: blur(20px);
    border-radius: 30px;
    border: 1px solid var(--border);
    z-index: 100;
    gap: 4px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.nav-item {
    padding: 10px 24px;
    background: transparent;
    border: none;
    color: var(--text-muted);
    font-size: 12px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s;
    border-radius: 24px;
}

.nav-item .icon {
    font-size: 18px;
    transition: transform 0.2s;
}

.nav-icon {
    width: 20px;
    height: 20px;
    stroke: currentColor;
    transition: transform 0.2s;
}

.nav-item.active {
    background: var(--accent-primary);
    color: #ffffff;
}

.nav-item.active .icon,
.nav-item.active .nav-icon {
    transform: scale(1.1);
}

.btn-icon {
    width: 16px;
    height: 16px;
    vertical-align: middle;
    margin-right: 4px;
}

.section-icon {
    width: 16px;
    height: 16px;
}

.status-icon {
    width: 14px;
    height: 14px;
    vertical-align: middle;
    margin-right: 4px;
}
```

## File: payload\public\css\files.css
```
/* ============================================
 * Files — Browser, viewer, editor
 * ============================================ */

        /* File Browser Panel */
        .files-panel {
            position: fixed;
            top: 0;
            left: 0;
            bottom: 0;
            width: 85%;
            max-width: 320px;
            background: var(--bg-dark);
            border-right: 1px solid var(--border);
            z-index: 250;
            transform: translateX(-100%);
            transition: transform 0.3s ease;
            display: flex;
            flex-direction: column;
            overscroll-behavior: contain;
            /* Prevent scroll leak */
        }

        .files-panel.open {
            transform: translateX(0);
        }

        .files-panel-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.5);
            z-index: 249;
            display: none;
        }

        .files-panel-overlay.open {
            display: block;
        }

        .files-header {
            padding: 16px;
            border-bottom: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .files-header h3 {
            font-size: 16px;
            font-weight: 600;
        }

        .files-close {
            width: 32px;
            height: 32px;
            background: var(--bg-glass);
            border: 1px solid var(--border);
            border-radius: 8px;
            color: var(--text-secondary);
            font-size: 18px;
            cursor: pointer;
        }

        .files-breadcrumb {
            padding: 8px 16px;
            font-size: 11px;
            color: var(--text-muted);
            border-bottom: 1px solid var(--border);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .files-list {
            flex: 1;
            min-height: 0;
            /* Critical for flex child scrolling */
            overflow-y: auto;
            overflow-x: hidden;
            padding: 8px;
            -webkit-overflow-scrolling: touch;
            /* Smooth scroll on iOS */
            overscroll-behavior: contain;
            /* Prevent scroll leak to parent */
            touch-action: pan-y;
            /* Ensure vertical touch scrolling works */
        }

        .file-item {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 12px;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .file-item:hover {
            background: var(--bg-glass);
        }

        .file-item.active {
            background: rgba(139, 92, 246, 0.15);
        }

        .file-icon {
            font-size: 20px;
            width: 28px;
            text-align: center;
        }

        .file-name {
            flex: 1;
            font-size: 14px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .file-size {
            font-size: 11px;
            color: var(--text-muted);
        }

        /* File Viewer Modal */
        .file-viewer {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: var(--bg-dark);
            z-index: 200;
            display: none;
            flex-direction: column;
        }

        .file-viewer.open {
            display: flex;
        }

        .file-viewer-header {
            padding: 16px;
            border-bottom: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .file-viewer-title {
            font-size: 14px;
            font-weight: 600;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .file-viewer-content {
            flex: 1;
            overflow: auto;
            padding: 16px;
        }

        .file-viewer-content pre {
            margin: 0;
            font-family: 'Fira Code', 'SF Mono', monospace;
            font-size: 13px;
            line-height: 1.5;
            white-space: pre-wrap;
            word-break: break-word;
        }

        /* File Editor */
        .file-editor {
            width: 100%;
            height: 100%;
            background: var(--bg-dark);
            color: var(--text-primary);
            border: none;
            padding: 16px;
            font-family: 'Fira Code', 'SF Mono', monospace;
            font-size: 13px;
            line-height: 1.5;
            resize: none;
            outline: none;
        }

        .file-viewer-actions {
            display: flex;
            gap: 10px;
            padding: 12px 16px;
            border-top: 1px solid var(--border);
            background: var(--bg-card);
        }

        .file-viewer-actions .btn {
            flex: 1;
            padding: 12px;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
        }

        .btn-edit {
            background: rgba(139, 92, 246, 0.2);
            border: 1px solid var(--accent-primary);
            color: var(--accent-primary);
            border-radius: 8px;
            padding: 8px 12px;
            font-size: 13px;
            cursor: pointer;
        }

        .btn-save {
            background: rgba(34, 197, 94, 0.2);
            border: 1px solid var(--success);
            color: var(--success);
        }

        .btn-cancel {
            background: rgba(239, 68, 68, 0.2);
            border: 1px solid var(--error);
            color: var(--error);
        }

        .file-viewer-header-btns {
            display: flex;
            gap: 8px;
            align-items: center;
        }

```

## File: payload\public\css\layout.css
```
/* ============================================
 * Layout — Base, sidebar, header, panels
 * ============================================ */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
}

html,
body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--bg-dark);
    color: var(--text-primary);
    min-height: 100vh;
    overflow-x: hidden;
    overscroll-behavior-y: contain;
    -webkit-font-smoothing: antialiased;
}

body.no-scroll {
    overflow: hidden;
    position: fixed;
    width: 100%;
}

/* Subtle background */
.bg-effects {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    pointer-events: none;
    z-index: -1;
    background: var(--bg-dark);
}

/* Sidebar */
.sidebar {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    width: var(--sidebar-collapsed);
    background: var(--bg-card);
    border-right: 1px solid var(--border);
    z-index: 200;
    display: flex;
    flex-direction: column;
    transition: width 0.25s ease;
}

.sidebar.expanded {
    width: var(--sidebar-width);
}

.sidebar-header {
    padding: 16px;
    display: flex;
    align-items: center;
    gap: 12px;
    border-bottom: 1px solid var(--border);
    min-height: 64px;
}

.sidebar-toggle {
    width: 32px;
    height: 32px;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: 8px;
    color: var(--text-secondary);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
    flex-shrink: 0;
}

.sidebar-toggle:hover {
    background: var(--accent-primary);
    color: white;
    border-color: var(--accent-primary);
}

.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    overflow: hidden;
    opacity: 0;
    transition: opacity 0.2s;
}

.sidebar.expanded .sidebar-logo {
    opacity: 1;
}

.sidebar-nav {
    flex: 1;
    padding: 12px 8px;
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.sidebar-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px;
    background: transparent;
    border: none;
    border-radius: 10px;
    color: var(--text-muted);
    cursor: pointer;
    transition: all 0.2s;
    text-align: left;
    width: 100%;
    overflow: hidden;
}

.sidebar-item:hover {
    background: var(--bg-glass);
    color: var(--text-primary);
}

.sidebar-item.active {
    background: var(--accent-primary);
    color: white;
}

.sidebar-item svg {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}

.sidebar-item span {
    white-space: nowrap;
    opacity: 0;
    transition: opacity 0.2s;
}

.sidebar.expanded .sidebar-item span {
    opacity: 1;
}

.sidebar-footer {
    padding: 12px 8px;
    border-top: 1px solid var(--border);
}

/* ========== Top Bar Mode ========== */
/* Hide the sidebar completely in topbar mode */
.topbar-mode .sidebar {
    display: none !important;
}

/* Show the new topbar element */
#topbar {
    display: none;
}

.topbar-mode #topbar {
    display: flex;
    position: fixed;
    top: 10px;
    left: 50%;
    transform: translateX(-50%);
    height: 44px;
    z-index: 1000;
    align-items: center;
    padding: 0 6px;
    gap: 4px;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.03) 50%, rgba(255, 255, 255, 0.06) 100%);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-top-color: rgba(255, 255, 255, 0.2);
    border-radius: 24px;
    backdrop-filter: blur(40px) saturate(1.4);
    -webkit-backdrop-filter: blur(40px) saturate(1.4);
    box-shadow:
        0 4px 24px rgba(0, 0, 0, 0.25),
        0 1px 0 rgba(255, 255, 255, 0.1) inset,
        0 -1px 0 rgba(0, 0, 0, 0.15) inset;
}

.topbar-nav {
    display: flex;
    align-items: center;
    gap: 2px;
}

.topbar-btn {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 6px 16px;
    border: none;
    background: transparent;
    color: var(--text-muted);
    border-radius: 20px;
    cursor: pointer;
    font-size: 12px;
    font-weight: 500;
    transition: all 0.2s ease;
    white-space: nowrap;
}

.topbar-btn svg {
    width: 16px;
    height: 16px;
    flex-shrink: 0;
}

.topbar-btn:hover {
    background: var(--bg-glass);
    color: var(--text-primary);
}

.topbar-btn.active {
    background: var(--accent-primary);
    color: white;
    box-shadow: 0 2px 10px var(--accent-glow);
}

/* Content area in topbar mode */
.topbar-mode .content {
    margin-left: 0 !important;
    padding-top: 0;
}

.topbar-mode .header {
    display: none !important;
}

body.sidebar-expanded.topbar-mode .content,
body.sidebar-expanded.topbar-mode .header {
    margin-left: 0 !important;
}

/* Chat container must fit viewport */
.topbar-mode .chat-container {
    height: 100vh !important;
    height: 100dvh !important;
}

/* Panels in topbar mode */
.topbar-mode .files-panel-overlay {
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
}

.topbar-mode .files-panel {
    top: 64px !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    width: 100% !important;
    max-width: 100% !important;
    animation: slideDown 0.25s ease;
}

.topbar-mode #settingsPanel,
.topbar-mode #assistPanel {
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    width: 100% !important;
    max-width: 100% !important;
    padding-top: 64px !important;
    animation: slideDown 0.25s ease;
}

.topbar-mode .file-viewer {
    top: 60px !important;
}

@keyframes slideDown {
    from {
        transform: translateY(-20px);
        opacity: 0;
    }

    to {
        transform: translateY(0);
        opacity: 1;
    }
}

/* ========== Quick Actions Toggle (via admin panel) ========== */
.hide-quick-actions .quick-actions {
    display: none !important;
}

.theme-selector {
    width: 100%;
    padding: 10px 12px;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: 8px;
    color: var(--text-primary);
    font-size: 13px;
    cursor: pointer;
    appearance: none;
}

.sidebar:not(.expanded) .theme-selector {
    display: none;
}

/* Theme icon buttons for collapsed sidebar */
.theme-icon-btn {
    width: 100%;
    height: 40px;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: 8px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    transition: all 0.2s;
}

.theme-icon-btn:hover {
    background: rgba(139, 92, 246, 0.2);
    border-color: var(--accent-primary);
}

.sidebar.expanded .theme-icon-btn {
    display: none;
}

/* Header */
.header {
    padding: 16px 20px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    background: var(--bg-card);
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 100;
    margin-left: var(--sidebar-collapsed);
    transition: margin-left 0.25s ease;
}

body.sidebar-expanded .header {
    margin-left: var(--sidebar-width);
}

.logo {
    display: flex;
    align-items: center;
    gap: 10px;
}
```

## File: payload\public\css\settings.css
```
/* ============================================
 * Settings — Panel, toggles, quota, toast
 * ============================================ */

        /* Settings */
        .settings-section {
            margin-bottom: 20px;
        }

        .settings-title {
            font-size: 12px;
            font-weight: 600;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 10px;
            padding-left: 4px;
        }

        .setting-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 14px 0;
            border-bottom: 1px solid var(--border);
        }

        .setting-row:last-child {
            border-bottom: none;
        }

        .setting-label h4 {
            font-size: 14px;
            font-weight: 500;
        }

        .setting-label p {
            font-size: 12px;
            color: var(--text-muted);
            margin-top: 2px;
        }

        .setting-value {
            font-size: 13px;
            padding: 6px 12px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 8px;
            color: var(--accent-primary);
            font-family: monospace;
        }

        /* Toggle Switch */
        .toggle-switch {
            position: relative;
            display: inline-block;
            width: 50px;
            height: 28px;
        }

        .toggle-switch input {
            opacity: 0;
            width: 0;
            height: 0;
        }

        .toggle-slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(255, 255, 255, 0.1);
            transition: 0.3s;
            border-radius: 28px;
            border: 1px solid var(--border);
        }

        .toggle-slider:before {
            position: absolute;
            content: "";
            height: 22px;
            width: 22px;
            left: 2px;
            bottom: 2px;
            background-color: white;
            transition: 0.3s;
            border-radius: 50%;
        }

        .toggle-switch input:checked+.toggle-slider {
            background: var(--accent-primary);
            border-color: var(--accent-primary);
        }

        .toggle-switch input:checked+.toggle-slider:before {
            transform: translateX(22px);
        }

        /* Toast */
        .toast-container {
            position: fixed;
            bottom: 100px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000;
            width: calc(100% - 32px);
            max-width: 360px;
        }

        .toast {
            padding: 14px 18px;
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 14px;
            backdrop-filter: blur(20px);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            animation: toastIn 0.3s ease;
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 8px;
        }

        .toast.success {
            border-color: var(--success);
        }

        .toast.error {
            border-color: var(--error);
        }

        @keyframes toastIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .spinner {
            width: 18px;
            height: 18px;
            border: 2px solid transparent;
            border-top-color: currentColor;
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }

        @keyframes spin {
            to {
                transform: rotate(360deg);
            }
        }

        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 4px;
        }

        ::-webkit-scrollbar-track {
            background: transparent;
        }

        ::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 2px;
        }

        /* Quota Cards */
        .quota-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 12px;
            margin-top: 12px;
        }

        .quota-card {
            background: var(--bg-glass);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 16px;
            text-align: center;
            transition: all 0.3s;
        }

        .quota-card:hover {
            border-color: var(--border-hover);
            transform: translateY(-2px);
        }

        .quota-ring {
            position: relative;
            width: 80px;
            height: 80px;
            margin: 0 auto 12px;
        }

        .quota-ring svg {
            width: 100%;
            height: 100%;
            transform: rotate(-90deg);
        }

        .quota-ring .ring-bg {
            fill: none;
            stroke: rgba(255, 255, 255, 0.1);
            stroke-width: 6;
        }

        .quota-ring .ring-progress {
            fill: none;
            stroke-width: 6;
            stroke-linecap: round;
            transition: stroke-dashoffset 0.5s ease;
        }

        .quota-ring .ring-progress.healthy {
            stroke: var(--success);
        }

        .quota-ring .ring-progress.warning {
            stroke: var(--warning);
        }

        .quota-ring .ring-progress.danger {
            stroke: var(--error);
        }

        .quota-ring .ring-progress.exhausted {
            stroke: var(--error);
        }

        .quota-percent {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 18px;
            font-weight: 700;
        }

        .quota-percent.healthy {
            color: var(--success);
        }

        .quota-percent.warning {
            color: var(--warning);
        }

        .quota-percent.danger {
            color: var(--error);
        }

        .quota-percent.exhausted {
            color: var(--error);
        }

        .quota-model-name {
            font-size: 13px;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 4px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .quota-reset {
            font-size: 11px;
            color: var(--text-muted);
        }

        .quota-status-badge {
            display: inline-block;
            font-size: 10px;
            font-weight: 600;
            padding: 2px 8px;
            border-radius: 10px;
            margin-top: 6px;
            text-transform: uppercase;
        }

        .quota-status-badge.healthy {
            background: rgba(34, 197, 94, 0.15);
            color: var(--success);
        }

        .quota-status-badge.warning {
            background: rgba(234, 179, 8, 0.15);
            color: var(--warning);
        }

        .quota-status-badge.danger,
        .quota-status-badge.exhausted {
            background: rgba(239, 68, 68, 0.15);
            color: var(--error);
        }

        .quota-loading {
            text-align: center;
            padding: 40px;
            color: var(--text-muted);
        }

        .quota-error {
            text-align: center;
            padding: 20px;
            color: var(--text-muted);
            font-size: 13px;
        }

        .quota-refresh-btn {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 16px;
            background: var(--accent-primary);
            border: none;
            border-radius: 20px;
            color: white;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            margin-top: 12px;
        }

        .quota-refresh-btn svg {
            stroke: white;
        }

        .quota-refresh-btn:hover {
            transform: scale(1.02);
        }

        .light-theme .quota-ring .ring-bg {
            stroke: rgba(0, 0, 0, 0.1);
        }

@keyframes spin { to { transform: rotate(360deg); } }

```

## File: payload\public\css\themes.css
```
/* ============================================
 * Theme-specific component overrides
 * ============================================ */

/* Rainbow theme - SUPER colorful components */
.rainbow-theme .sidebar {
    background: rgba(20, 15, 45, 0.98);
    border-right: 3px solid #8b5cf6;
}

.rainbow-theme .sidebar-item.active {
    background: #8b5cf6 !important;
}

.rainbow-theme .sidebar-item:nth-child(1) {
    color: #ef4444;
}

.rainbow-theme .sidebar-item:nth-child(2) {
    color: #22c55e;
}

.rainbow-theme .sidebar-item:nth-child(3) {
    color: #3b82f6;
}

.rainbow-theme .sidebar-item.active {
    color: white !important;
}

.rainbow-theme .sidebar-item:nth-child(1):hover {
    background: rgba(239, 68, 68, 0.2);
}

.rainbow-theme .sidebar-item:nth-child(2):hover {
    background: rgba(34, 197, 94, 0.2);
}

.rainbow-theme .sidebar-item:nth-child(3):hover {
    background: rgba(59, 130, 246, 0.2);
}

.rainbow-theme .sidebar-footer {
    border-top: 2px solid #f97316;
}

.rainbow-theme .logo-icon {
    background: #06b6d4 !important;
}

.rainbow-theme .logo-text {
    color: #a855f7 !important;
}

.rainbow-theme .header {
    background: rgba(20, 15, 45, 0.98);
    border-bottom: 3px solid #f43f5e;
}

.rainbow-theme .status-pill.connected {
    background: rgba(16, 185, 129, 0.2);
    border: 2px solid #10b981;
    color: #10b981;
}

.rainbow-theme .status-pill.disconnected {
    background: rgba(239, 68, 68, 0.2);
    border: 2px solid #ef4444;
}

.rainbow-theme .chat-container {
    border: 2px solid #8b5cf6;
}

.rainbow-theme .chat-send {
    background: #22c55e !important;
}

.rainbow-theme .chat-input:focus {
    border-color: #06b6d4;
    box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.3);
}

.rainbow-theme .btn-primary {
    background: #f43f5e !important;
}

.rainbow-theme .login-btn {
    background: #3b82f6 !important;
}

.rainbow-theme .login-logo svg {
    stroke: #eab308;
}

.rainbow-theme .login-title {
    color: #a855f7;
}

.rainbow-theme .quick-chip:nth-child(1) {
    border-color: #ef4444;
    color: #ef4444;
}

.rainbow-theme .quick-chip:nth-child(2) {
    border-color: #22c55e;
    color: #22c55e;
}

.rainbow-theme .quick-chip:nth-child(3) {
    border-color: #f97316;
    color: #f97316;
}

.rainbow-theme .quick-chip:nth-child(4) {
    border-color: #3b82f6;
    color: #3b82f6;
}

.rainbow-theme .quick-chip:nth-child(5) {
    border-color: #a855f7;
    color: #a855f7;
}

.rainbow-theme .quick-chip:hover {
    background: rgba(255, 255, 255, 0.1);
}

.rainbow-theme .toggle-switch input:checked+.toggle-slider {
    background: #f97316 !important;
    border-color: #f97316 !important;
}

.rainbow-theme .card {
    border: 2px solid rgba(139, 92, 246, 0.4);
}

.rainbow-theme .settings-title {
    color: #06b6d4;
}

.rainbow-theme .setting-label h4 {
    color: #a855f7;
}

.rainbow-theme .quota-refresh-btn {
    background: #06b6d4 !important;
}

.rainbow-theme .setting-value {
    background: rgba(249, 115, 22, 0.15);
    color: #f97316;
    border: 1px solid rgba(249, 115, 22, 0.3);
}

.rainbow-theme .files-panel {
    background: #0c0c18;
    border-right: 3px solid #eab308;
}

.rainbow-theme .files-header h3 {
    color: #eab308;
}

.rainbow-theme .file-item:hover {
    background: rgba(6, 182, 212, 0.15);
}

/* Theme-specific overrides */
.light-theme .sidebar,
.pastel-theme .sidebar {
    background: var(--bg-card);
    box-shadow: 2px 0 12px rgba(0, 0, 0, 0.08);
}

.light-theme .header,
.pastel-theme .header {
    background: var(--bg-card);
    border-bottom: 1px solid var(--border);
}

.light-theme .setting-value,
.pastel-theme .setting-value {
    background: rgba(0, 0, 0, 0.05);
}

.light-theme .chat-input-area,
.pastel-theme .chat-input-area {
    background: rgba(0, 0, 0, 0.02);
}

.light-theme #settingsPanel,
.pastel-theme #settingsPanel,
.light-theme #assistPanel,
.pastel-theme #assistPanel {
    background: var(--bg-dark);
}

.light-theme .logo-text,
.pastel-theme .logo-text {
    color: var(--text-primary);
}

/* ========== Slate Theme ========== */
/* Compact, flat, no emojis, no glow, neutral palette */
.slate-theme {
    --bg-dark: #1a1a22;
    --bg-card: #22222c;
    --bg-glass: rgba(255, 255, 255, 0.03);
    --accent-primary: #6b7280;
    --accent-secondary: #9ca3af;
    --accent-glow: transparent;
    --success: #4ade80;
    --warning: #fbbf24;
    --error: #f87171;
    --text-primary: #e5e7eb;
    --text-secondary: #9ca3af;
    --text-muted: #6b7280;
    --border: rgba(255, 255, 255, 0.08);
    --border-hover: rgba(255, 255, 255, 0.12);
}

/* Flat cards — no glass, no glow, tight radius */
.slate-theme .card {
    border-radius: 6px;
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
    padding: 12px;
    margin-bottom: 8px;
}

.slate-theme .screen-frame {
    border-radius: 6px;
}

/* Sidebar — compact */
.slate-theme .sidebar {
    background: #16161e;
    border-right: 1px solid rgba(255, 255, 255, 0.06);
}

.slate-theme .sidebar-header {
    padding: 10px 12px;
    min-height: 48px;
    gap: 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.slate-theme .sidebar-nav {
    padding: 6px;
    gap: 2px;
}

.slate-theme .sidebar-item {
    padding: 8px 10px;
    gap: 8px;
    border-radius: 4px;
    font-size: 13px;
    color: #6b7280;
}

.slate-theme .sidebar-item:hover {
    background: rgba(255, 255, 255, 0.04);
    color: #d1d5db;
}

.slate-theme .sidebar-item.active {
    background: rgba(99, 130, 191, 0.15);
    color: #93a8d0;
}

.slate-theme .sidebar-item svg {
    width: 16px;
    height: 16px;
}

.slate-theme .sidebar-toggle {
    border-radius: 4px;
    width: 28px;
    height: 28px;
}

.slate-theme .sidebar-footer {
    padding: 8px 6px;
}

/* Status pill — minimal */
.slate-theme .status-pill {
    border-radius: 4px;
    font-size: 10px;
    padding: 4px 8px;
    margin-bottom: 6px;
}

.slate-theme .status-dot {
    animation: none;
    box-shadow: none !important;
}

/* Header — flat */
.slate-theme .header {
    padding: 10px 16px;
    border-bottom: 1px solid var(--border);
}

/* View switcher — tight */
.slate-theme .view-switcher {
    border-radius: 6px;
    margin: 8px 12px;
    padding: 3px;
}

.slate-theme .view-btn {
    border-radius: 4px;
    padding: 8px 12px;
    font-size: 12px;
}

.slate-theme .view-btn.active {
    box-shadow: none;
    background: rgba(99, 130, 191, 0.15);
    color: #93a8d0;
}

/* Topbar — flat, clean */
.slate-theme #topbar {
    border-radius: 8px;
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
    background: #1e1e28;
    border: 1px solid rgba(255, 255, 255, 0.06);
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.4);
    height: 40px;
    padding: 0 4px;
}

.slate-theme .topbar-btn {
    border-radius: 6px;
    padding: 6px 14px;
    font-size: 11px;
    font-weight: 500;
    color: #6b7280;
    position: relative;
}

.slate-theme .topbar-btn:hover {
    color: #d1d5db;
    background: none;
}

.slate-theme .topbar-btn.active {
    background: none;
    color: #c5d0e6;
    box-shadow: none;
    border-radius: 6px;
}

.slate-theme .topbar-btn.active::after {
    content: '';
    position: absolute;
    bottom: 2px;
    left: 25%;
    width: 50%;
    height: 1.5px;
    background: #7b8fba;
    border-radius: 1px;
}

.slate-theme .topbar-btn svg {
    opacity: 0.7;
}

.slate-theme .topbar-btn.active svg {
    opacity: 1;
}

/* Chat container — flat */
.slate-theme .chat-container {
    border-radius: 6px;
}

.slate-theme .chat-input {
    border-radius: 4px;
}

.slate-theme .chat-send {
    border-radius: 4px;
}

/* Quick chips — compact, no fancy borders */
.slate-theme .quick-chip {
    border-radius: 4px;
    padding: 6px 10px;
    font-size: 11px;
    border-color: var(--border);
    color: var(--text-secondary);
}

.slate-theme .quick-chip:hover {
    border-color: var(--text-muted);
    color: var(--text-primary);
}

/* Settings — compact */
.slate-theme .settings-section {
    margin-bottom: 12px;
}

.slate-theme .settings-title {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: var(--text-muted);
}

.slate-theme .setting-row {
    padding: 8px 0;
}

.slate-theme .setting-label h4 {
    font-size: 13px;
}

.slate-theme .setting-label p {
    font-size: 11px;
}

.slate-theme .setting-value {
    font-size: 12px;
    border-radius: 4px;
}

/* Logo — smaller */
.slate-theme .logo-icon {
    width: 28px;
    height: 28px;
    border-radius: 4px;
}

.slate-theme .logo-text {
    font-size: 16px;
    font-weight: 600;
}

/* Theme selector — flat */
.slate-theme .theme-selector {
    border-radius: 4px;
    padding: 8px 10px;
    font-size: 12px;
}

.slate-theme .theme-icon-btn {
    border-radius: 4px;
    font-size: 14px;
}

/* File viewer — flat */
.slate-theme .file-viewer {
    border-radius: 6px;
}

.slate-theme .files-panel {
    border-radius: 0;
}

/* No glow or decorative box-shadows anywhere */
.slate-theme .view-btn.active,
.slate-theme .topbar-btn.active,
.slate-theme .connected .status-dot {
    box-shadow: none;
}

/* Animations — reduced */
.slate-theme .view {
    animation: none;
}

.slate-theme .bg-effects {
    background: var(--bg-dark);
}

/* Remove emoji characters via CSS */
.slate-theme .emoji {
    display: none;
}

/* Quota card tweaks */
.slate-theme .quota-refresh-btn {
    border-radius: 4px;
}

/* Login — flat */
.slate-theme .login-card {
    border-radius: 8px;
    backdrop-filter: none;
}

.slate-theme .login-btn {
    border-radius: 4px;
}

```

## File: payload\public\css\variables.css
```
/* ============================================
 * CSS Variables — Theme color tokens
 * ============================================ */

:root {
    --bg-dark: #0a0a0f;
    --bg-card: rgba(18, 18, 28, 0.95);
    --bg-glass: rgba(255, 255, 255, 0.04);
    --accent-primary: #0ea5e9;
    --accent-secondary: #06b6d4;
    --accent-glow: rgba(14, 165, 233, 0.3);
    --success: #22c55e;
    --warning: #eab308;
    --error: #ef4444;
    --text-primary: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.7);
    --text-muted: rgba(255, 255, 255, 0.4);
    --border: rgba(255, 255, 255, 0.1);
    --border-hover: rgba(255, 255, 255, 0.18);
    --sidebar-width: 240px;
    --sidebar-collapsed: 64px;
}

/* Light Theme */
.light-theme {
    --bg-dark: #f8fafc;
    --bg-card: #ffffff;
    --bg-glass: rgba(0, 0, 0, 0.03);
    --accent-primary: #06b6d4;
    --accent-secondary: #0891b2;
    --accent-glow: rgba(6, 182, 212, 0.2);
    --text-primary: #1e293b;
    --text-secondary: #475569;
    --text-muted: #94a3b8;
    --border: rgba(0, 0, 0, 0.08);
    --border-hover: rgba(0, 0, 0, 0.15);
}

/* Pastel Theme */
.pastel-theme {
    --bg-dark: #fef7f0;
    --bg-card: #fffbf8;
    --bg-glass: rgba(244, 114, 182, 0.05);
    --accent-primary: #f472b6;
    --accent-secondary: #e879f9;
    --accent-glow: rgba(244, 114, 182, 0.2);
    --text-primary: #4a3728;
    --text-secondary: #6b5344;
    --text-muted: #a08979;
    --border: rgba(244, 114, 182, 0.15);
    --border-hover: rgba(244, 114, 182, 0.25);
}

/* Rainbow Theme */
.rainbow-theme {
    --bg-dark: #0c0c18;
    --bg-card: rgba(20, 20, 40, 0.95);
    --bg-glass: rgba(255, 255, 255, 0.03);
    --accent-primary: #f43f5e;
    --accent-secondary: #8b5cf6;
    --accent-tertiary: #06b6d4;
    --accent-glow: rgba(244, 63, 94, 0.3);
    --text-primary: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.75);
    --text-muted: rgba(255, 255, 255, 0.45);
    --border: rgba(255, 255, 255, 0.1);
    --border-hover: rgba(255, 255, 255, 0.2);
    --success: #10b981;
    --warning: #f59e0b;
    --error: #ef4444;
}
```

## File: payload\public\css\_DIR_IDENTITY.md
```
---
id: ecosystem-plugins-repo-fetched-antigravity-mobile-035838-public-css
name: Css
path: ecosystem/plugins/repo-fetched-antigravity-mobile-035838/public/css
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Css
Storage area for 'css' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: payload\public\js\api.js
```
/* ============================================
 * API — Server URL, auth, fetch helpers
 * ============================================ */

        // ====================================================================
        // State
        // ====================================================================
        let ws = null;
        let autoRefresh = false;
        let refreshTimer = null;
        let chatMessages = [];
        const serverUrl = window.location.origin;

        // Auth state
        let authToken = localStorage.getItem('authToken');

        // Helper for authenticated fetch
        async function authFetch(url, options = {}) {
            const headers = { ...(options.headers || {}) };
            if (authToken) {
                headers['Authorization'] = `Bearer ${authToken}`;
            }

            const res = await fetch(url, { ...options, headers });

            // If unauthorized, show login screen but don't throw for polling calls
            if (res.status === 401) {
                try {
                    const clonedRes = res.clone();
                    const data = await clonedRes.json();
                    if (data.needsAuth) {
                        authToken = null;
                        localStorage.removeItem('authToken');
                        showLoginScreen();
                    }
                } catch (e) {
                    // Ignore JSON parse errors
                }
            }

            return res;
        }

        // ====================================================================
        // Authentication
        // ====================================================================
        async function checkAuth() {
            try {
                const res = await fetch(`${serverUrl}/api/auth/status`);
                const data = await res.json();

                if (!data.authEnabled) {
                    // No auth required, hide login screen
                    hideLoginScreen();
                    return true;
                }

                // Auth is enabled, check if we have a valid token
                if (authToken) {
                    const testRes = await authFetch(`${serverUrl}/api/status`);
                    if (testRes.ok) {
                        hideLoginScreen();
                        return true;
                    }
                }

                // Need to login
                showLoginScreen();
                return false;
            } catch (e) {
                console.error('Auth check failed:', e);
                return false;
            }
        }

        function showLoginScreen() {
            document.getElementById('loginScreen').classList.remove('hidden');
        }

        function hideLoginScreen() {
            document.getElementById('loginScreen').classList.add('hidden');
        }

        async function submitPin() {
            const pin = document.getElementById('pinInput').value;
            const errorEl = document.getElementById('loginError');

            if (!pin || pin.length < 4) {
                errorEl.textContent = 'Please enter your PIN';
                errorEl.style.display = 'block';
                return;
            }

            try {
                const res = await fetch(`${serverUrl}/api/auth/login`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ pin })
                });

                const data = await res.json();

                if (data.success) {
                    authToken = data.token;
                    localStorage.setItem('authToken', authToken);
                    hideLoginScreen();
                    errorEl.style.display = 'none';
                    document.getElementById('pinInput').value = '';
                } else {
                    errorEl.textContent = data.error || 'Invalid PIN';
                    errorEl.style.display = 'block';
                }
            } catch (e) {
                errorEl.textContent = 'Connection error';
                errorEl.style.display = 'block';
            }
        }

        // Submit PIN on Enter key
        document.addEventListener('DOMContentLoaded', () => {
            document.getElementById('pinInput').addEventListener('keypress', (e) => {
                if (e.key === 'Enter') submitPin();
            });
        });

        // ====================================================================
        // WebSocket
        // ====================================================================

```

## File: payload\public\js\app.js
```
/* ============================================
 * App — Initialization
 * ============================================ */

async function init() {
    loadTheme();
    loadSidebarState();
    await checkAuth();
    connectWebSocket();
    startChatPolling();
    loadModelsAndModes();
    applyMobileUISettings();
    refreshTaskQueue();
    loadAssistChatHistory();
    loadAssistStatusBadge();
}

init();

// Register Service Worker for PWA
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').catch(() => { });
}

```

## File: payload\public\js\assist.js
```
/* ============================================
 * Assist — Chat, streaming, status
 * ============================================ */

async function loadAssistChatHistory() {
    try {
        const res = await authFetch(serverUrl + '/api/supervisor/chat/history');
        const data = await res.json();
        const container = document.getElementById('assistChatMessages');
        if (!data.messages || data.messages.length === 0) {
            container.innerHTML = '<div style="text-align:center;color:var(--text-muted);font-size:13px;padding:40px 20px;">'
                + '<div style="font-size:40px;margin-bottom:12px;color:var(--accent-primary);">' + svgIcon('brain', 40) + '</div>'
                + '<div style="font-weight:600;margin-bottom:4px;">Supervisor Assist</div>'
                + '<div>Chat with your AI supervisor. Ask about agent activity, project status, or give instructions.</div>'
                + '</div>';
            return;
        }
        container.innerHTML = data.messages.map(function (m) { return renderAssistMessage(m); }).join('');
        container.scrollTop = container.scrollHeight;
    } catch (e) { }
}

function renderAssistMessage(msg) {
    var isUser = msg.role === 'user';
    var time = msg.timestamp ? new Date(msg.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : '';
    var content = isUser ? escapeHtml(msg.content) : formatAssistMarkdown(msg.content);

    if (isUser) {
        var html = '<div style="display:flex;justify-content:flex-end;">'
            + '<div style="max-width:80%;background:var(--accent-primary);color:white;padding:10px 14px;border-radius:16px 16px 4px 16px;font-size:14px;line-height:1.5;">'
            + '<div>' + content + '</div>';
        if (time) html += '<div style="font-size:10px;opacity:.6;margin-top:4px;text-align:right;">' + time + '</div>';
        html += '</div></div>';
        return html;
    }

    var html = '<div style="display:flex;justify-content:flex-start;">'
        + '<div style="max-width:85%;background:var(--bg-glass);border:1px solid var(--border);padding:10px 14px;border-radius:16px 16px 16px 4px;font-size:14px;line-height:1.5;">'
        + '<div style="font-size:10px;font-weight:600;color:var(--accent-primary);margin-bottom:4px;display:flex;align-items:center;gap:4px;">' + svgIcon('brain', 12) + ' Supervisor</div>'
        + '<div style="color:var(--text-primary);">' + content + '</div>';
    if (time) html += '<div style="font-size:10px;color:var(--text-muted);margin-top:4px;">' + time + '</div>';
    html += '</div></div>';
    return html;
}

function escapeHtml(text) {
    var div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatAssistMarkdown(text) {
    var s = escapeHtml(text);
    s = s.replace(/```([\s\S]*?)```/g, '<pre style="background:rgba(0,0,0,.3);padding:8px;border-radius:6px;overflow-x:auto;font-size:12px;margin:6px 0;">$1</pre>');
    s = s.replace(/`([^`]+)`/g, '<code style="background:rgba(0,0,0,.2);padding:2px 5px;border-radius:4px;font-size:12px;">$1</code>');
    s = s.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    s = s.replace(/\n/g, '<br>');
    return s;
}

async function sendAssistChat() {
    var input = document.getElementById('assistChatInput');
    var message = input.value.trim();
    if (!message) return;

    var container = document.getElementById('assistChatMessages');
    var sendBtn = document.getElementById('assistSendBtn');

    // Remove welcome message if present
    var welcome = container.querySelector('[style*="text-align"]');
    if (welcome && welcome.textContent.includes('Supervisor Assist')) welcome.remove();

    // Add user message immediately
    container.innerHTML += renderAssistMessage({ role: 'user', content: message, timestamp: Date.now() });
    input.value = '';
    container.scrollTop = container.scrollHeight;

    // Create a streaming response bubble
    var streamId = 'assist-stream-' + Date.now();
    container.innerHTML += '<div id="' + streamId + '" style="display:flex;justify-content:flex-start;">'
        + '<div style="max-width:85%;background:var(--bg-glass);border:1px solid var(--border);padding:10px 14px;border-radius:16px 16px 16px 4px;font-size:14px;line-height:1.5;">'
        + '<div style="font-size:10px;font-weight:600;color:var(--accent-primary);margin-bottom:4px;display:flex;align-items:center;gap:4px;">' + svgIcon('brain', 12) + ' Supervisor</div>'
        + '<div class="stream-content" style="color:var(--text-primary);">'
        + '<span class="typing-dots" style="display:inline-flex;gap:4px;padding:4px 0;">'
        + '<span style="width:6px;height:6px;border-radius:50%;background:var(--text-muted);animation:blink 1.4s infinite both;"></span>'
        + '<span style="width:6px;height:6px;border-radius:50%;background:var(--text-muted);animation:blink 1.4s infinite both .2s;"></span>'
        + '<span style="width:6px;height:6px;border-radius:50%;background:var(--text-muted);animation:blink 1.4s infinite both .4s;"></span>'
        + '</span></div>'
        + '</div></div>';
    container.scrollTop = container.scrollHeight;
    sendBtn.disabled = true;
    input.disabled = true;

    try {
        var res = await fetch(serverUrl + '/api/supervisor/chat/stream', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: message })
        });

        var streamEl = document.getElementById(streamId);
        var contentEl = streamEl ? streamEl.querySelector('.stream-content') : null;
        var rawText = '';
        var dotsRemoved = false;

        var reader = res.body.getReader();
        var decoder = new TextDecoder();
        var buffer = '';

        while (true) {
            var chunk = await reader.read();
            if (chunk.done) break;

            buffer += decoder.decode(chunk.value, { stream: true });
            var lines = buffer.split('\n');
            buffer = lines.pop();

            for (var i = 0; i < lines.length; i++) {
                var line = lines[i].trim();
                if (!line.startsWith('data: ')) continue;
                try {
                    var data = JSON.parse(line.substring(6));
                    if (data.token && contentEl) {
                        if (!dotsRemoved) {
                            var dots = contentEl.querySelector('.typing-dots');
                            if (dots) dots.remove();
                            dotsRemoved = true;
                        }
                        rawText += data.token;
                        contentEl.innerHTML = formatAssistMarkdown(rawText);
                        container.scrollTop = container.scrollHeight;
                    }
                    if (data.done) {
                        // Add timestamp
                        var timeStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
                        var timeDiv = document.createElement('div');
                        timeDiv.style.cssText = 'font-size:10px;color:var(--text-muted);margin-top:4px;';
                        timeDiv.textContent = timeStr;
                        if (contentEl) contentEl.parentElement.appendChild(timeDiv);
                    }
                    if (data.file_content && contentEl) {
                        // Server resolved [READ:] / [LIST:] tags — update with file content
                        rawText = data.file_content;
                        contentEl.innerHTML = formatAssistMarkdown(rawText);
                        container.scrollTop = container.scrollHeight;
                    }
                    if (data.error) {
                        if (contentEl) contentEl.innerHTML = '<span style="color:var(--error);">Error: ' + data.error + '</span>';
                    }
                } catch (parseErr) { }
            }
        }
    } catch (e) {
        var streamEl = document.getElementById(streamId);
        if (streamEl) streamEl.innerHTML = '<div style="text-align:center;font-size:12px;color:var(--error);padding:8px;">Connection error</div>';
    } finally {
        sendBtn.disabled = false;
        input.disabled = false;
        input.focus();
    }
}

async function loadAssistStatusBadge() {
    try {
        var res = await authFetch(serverUrl + '/api/admin/supervisor');
        var data = await res.json();
        var badge = document.getElementById('assistStatusBadge');
        if (!badge) return;
        if (data.enabled) {
            var stMap = { idle: svgIcon('dotGreen', 10) + ' Idle', thinking: svgIcon('dotYellow', 10) + ' Thinking...', acting: svgIcon('dotBlue', 10) + ' Acting', error: svgIcon('dotRed', 10) + ' Error' };
            badge.innerHTML = stMap[data.status] || data.status;
        } else {
            badge.innerHTML = svgIcon('dotGray', 10) + ' Disabled';
        }
    } catch (e) { }
}

// ============================================
// Task Queue UI Functions
// ============================================

var taskQueueExpanded = false;

```

## File: payload\public\js\chat-live.js
```
/* ============================================
 * Chat Live — Models, polling, live view
 * ============================================ */

        async function loadModelsAndModes() {
            console.log('[Debug] loadModelsAndModes called');
            try {
                const res = await authFetch('/api/models');
                const data = await res.json();
                console.log('[Debug] Models API response:', data);

                availableModels = data.models || [];
                currentModel = data.currentModel || 'Unknown';
                currentMode = data.currentMode || 'Planning';

                console.log('[Debug] Setting model:', currentModel, 'mode:', currentMode);

                // Update UI
                document.getElementById('currentModelLabel').textContent = currentModel;
                document.getElementById('currentModeLabel').textContent = currentMode.replace(/\s+/g, ' ').split(' ')[0];

                // Populate model list
                const modelList = document.getElementById('modelList');
                console.log('[Debug] modelList element:', modelList);
                modelList.innerHTML = availableModels.map(model => `
                        <div class="dropdown-item ${model === currentModel ? 'active' : ''}" onclick="selectModel('${escapeHtml(model)}')">
                            ${escapeHtml(model)}
                        </div>
                    `).join('');
                console.log('[Debug] Models loaded:', availableModels.length);
            } catch (e) {
                console.log('[Debug] Failed to load models:', e);
                document.getElementById('currentModelLabel').textContent = 'Not connected';
            }
        }

        let dropdownDebounce = false;
        function toggleModelDropdown(event) {
            if (event) event.stopPropagation();
            if (dropdownDebounce) return;
            dropdownDebounce = true;
            setTimeout(() => dropdownDebounce = false, 100);

            console.log('[Debug] toggleModelDropdown called');
            const dropdown = document.getElementById('modelDropdown');
            const modeDropdown = document.getElementById('modeDropdown');
            console.log('[Debug] dropdown element:', dropdown, 'current display:', dropdown?.style?.display);
            modeDropdown.style.display = 'none';
            dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
            console.log('[Debug] dropdown display after toggle:', dropdown.style.display);
        }

        function toggleModeDropdown(event) {
            if (event) event.stopPropagation();
            if (dropdownDebounce) return;
            dropdownDebounce = true;
            setTimeout(() => dropdownDebounce = false, 100);

            const dropdown = document.getElementById('modeDropdown');
            const modelDropdown = document.getElementById('modelDropdown');
            modelDropdown.style.display = 'none';
            dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
        }

        function closeAllDropdowns() {
            document.getElementById('modelDropdown').style.display = 'none';
            document.getElementById('modeDropdown').style.display = 'none';
        }

        async function selectModel(modelName) {
            console.log('[selectModel] Requesting model change to:', modelName);
            closeAllDropdowns();
            document.getElementById('currentModelLabel').textContent = 'Changing...';

            try {
                const res = await authFetch('/api/models/set', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ model: modelName })
                });
                const result = await res.json();
                console.log('[selectModel] API response:', result);
                if (result.debug) {
                    console.log('[selectModel] CLICKED ELEMENT:', JSON.stringify(result.debug, null, 2));
                }

                if (result.success) {
                    currentModel = result.selected || modelName;
                    document.getElementById('currentModelLabel').textContent = currentModel;
                    showToast(`Model: ${currentModel}`, 'success');
                    console.log('[selectModel] Success! Model set to:', currentModel);
                } else {
                    document.getElementById('currentModelLabel').textContent = currentModel;
                    showToast(result.error || 'Failed to change model', 'error');
                    console.log('[selectModel] Failed:', result.error);
                }
            } catch (e) {
                document.getElementById('currentModelLabel').textContent = currentModel;
                showToast('Network error', 'error');
                console.log('[selectModel] Network error:', e);
            }
        }

        async function selectMode(modeName) {
            console.log('[selectMode] Requesting mode change to:', modeName);
            closeAllDropdowns();
            document.getElementById('currentModeLabel').textContent = '...';

            try {
                const res = await authFetch('/api/modes/set', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ mode: modeName })
                });
                const result = await res.json();
                console.log('[selectMode] API response:', result);
                if (result.debug) {
                    console.log('[selectMode] CLICKED ELEMENT:', JSON.stringify(result.debug, null, 2));
                }

                if (result.success) {
                    currentMode = modeName;
                    document.getElementById('currentModeLabel').textContent = modeName;
                    showToast(`Mode: ${modeName}`, 'success');
                    console.log('[selectMode] Success! Mode set to:', modeName);
                } else {
                    document.getElementById('currentModeLabel').textContent = currentMode;
                    showToast(result.error || 'Failed to change mode', 'error');
                    console.log('[selectMode] Failed:', result.error);
                    if (result.candidatesFound) {
                        console.log('[selectMode] Candidates found:', result.candidatesFound);
                    }
                    if (result.allTexts) {
                        console.log('[selectMode] All cursor-pointer texts:', result.allTexts);
                    }
                }
            } catch (e) {
                document.getElementById('currentModeLabel').textContent = currentMode;
                showToast('Network error', 'error');
                console.log('[selectMode] Network error:', e);
            }
        }

        // ====================================================================
        // Command Approval Functions (for buttons in injected IDE content)
        // ====================================================================

        // Forward any tap in injected IDE content to the real IDE via CDP click
        function attachInteractiveHandlers(container) {
            // Every interactive element was tagged at capture time with data-xpath
            // Tap → POST /api/cdp/click → IDE evaluates el.click() on the real element

            // Buttons to ignore (UI chrome, not user-actionable)
            const IGNORED = /^(always run|cancel|relocate|review changes|planning|claude|model|copy)/i;
            // Accept/positive action buttons
            const ACCEPT = /^(run|accept|allow once|allow this conversation|yes|continue|approve|confirm|ok|proceed|good|expand|collapse|dismiss)/i;
            // Reject/negative action buttons
            const REJECT = /^(reject|deny|bad|no\b)/i;
            // Dynamic patterns (e.g. "Thought for 3s")
            const NEUTRAL_DYNAMIC = /^(thought for|expand all|collapse all)/i;

            container.querySelectorAll('[data-xpath]').forEach(el => {
                const xpath = el.getAttribute('data-xpath');
                const label = (el.innerText || el.getAttribute('aria-label') || '').trim().slice(0, 60);
                if (!xpath || !label) return;

                // Skip ignored buttons
                if (IGNORED.test(label)) return;

                // Classify button
                let action = null;
                if (ACCEPT.test(label)) action = 'accept';
                else if (REJECT.test(label)) action = 'reject';
                else if (NEUTRAL_DYNAMIC.test(label)) action = 'neutral';
                else return; // Not a recognized actionable button

                // Tag for CSS styling
                el.setAttribute('data-mobile-action', action);

                el.addEventListener('click', async (e) => {
                    e.preventDefault();
                    e.stopPropagation();

                    // Visual feedback
                    const prev = el.style.opacity;
                    el.style.opacity = '0.5';

                    // Toggle aria-expanded visually while waiting for refresh
                    if (el.hasAttribute('aria-expanded')) {
                        const cur = el.getAttribute('aria-expanded');
                        el.setAttribute('aria-expanded', cur === 'true' ? 'false' : 'true');
                    }

                    try {
                        const res = await authFetch('/api/cdp/click', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ xpath, text: label })
                        });
                        const result = await res.json();
                        if (result.success) {
                            showToast(`✓ ${label}`, 'success');
                        } else {
                            showToast(result.error || 'Click failed', 'error');
                            el.style.opacity = prev;
                        }
                    } catch (err) {
                        showToast('Network error', 'error');
                        el.style.opacity = prev;
                    } finally {
                        setTimeout(() => { el.style.opacity = prev; }, 500);
                    }
                });
            });
        }

        // Keep old name as alias for any remaining callers
        function attachApprovalHandlers(container) {
            attachInteractiveHandlers(container);
        }



        // Close dropdowns when clicking outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.model-selector') && !e.target.closest('.mode-selector') &&
                !e.target.closest('.model-dropdown') && !e.target.closest('.mode-dropdown')) {
                closeAllDropdowns();
            }
        });

        // ====================================================================
        // Helpers
        // ====================================================================
        function formatTime(ts) {
            return ts ? new Date(ts).toLocaleTimeString() : '';
        }

        function escapeHtml(text) {
            if (!text) return '';
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }

        function showToast(message, type = 'info') {
            const container = document.getElementById('toastContainer');
            const toast = document.createElement('div');
            toast.className = `toast ${type}`;
            toast.innerHTML = `<span>${type === 'success' ? '✓' : '✕'}</span> ${message}`;
            container.appendChild(toast);
            setTimeout(() => toast.remove(), 2500);
        }

        // ====================================================================
        // Live Chat Polling from IDE (#cascade element)
        // Renders the raw HTML + CSS exactly like the IDE
        // ====================================================================
        let chatPollingActive = false;
        let chatPollTimer = null;
        let lastCascadeHash = null;
        let cssLoaded = false;




        async function fetchLiveChat() {
            if (!chatPollingActive) return;

            try {
                const res = await authFetch(`${serverUrl}/api/chat/snapshot`);
                const data = await res.json();

                if (data.html) {
                    // Simple hash check to avoid unnecessary DOM updates
                    const hash = data.html.length.toString(36);
                    if (hash !== lastCascadeHash) {
                        lastCascadeHash = hash;

                        // Inject CSS (always update to apply fixes)
                        if (data.css) {
                            const styleEl = document.getElementById('cascadeStyles');
                            styleEl.textContent = `
                                ${data.css}
                                /* Fixes for empty space and scrolling */
                                #cascade-container {
                                    background: transparent !important;
                                    width: 100% !important;
                                    height: auto !important;
                                    overflow-y: auto !important;
                                    overflow-x: hidden !important;
                                    max-height: none !important;
                                    position: relative !important;
                                    overscroll-behavior-y: contain !important;
                                }
                                
                                /* Hide virtualized scroll placeholders */
                                #cascade-container [style*="min-height"] {
                                    min-height: 0 !important;
                                }
                                #cascade-container .bg-gray-500\\/10:not(:has(*)),
                                #cascade-container [class*="bg-gray-500"]:not(:has(*)) {
                                    display: none !important;
                                }
                                
                                /* Prevent empty spacers from breaking layout */
                                
                                /* 1. Define the missing variable so ALL text using it becomes visible */
                                #cascade-container {
                                    --ide-text-color: var(--text-primary) !important;
                                }
                                
                                /* Ensure codicon font renders properly on mobile */
                                #cascade-container .codicon,
                                #cascade-container [class*="codicon-"] {
                                    font-family: 'codicon' !important;
                                }
                                
                                /* Removed manual code block styling to inherit IDE tailwind correctly */
                            `;
                        }

                        const container = document.getElementById('cascade-container');
                        const isAtBottom = container.scrollHeight - container.scrollTop - container.clientHeight < 100;

                        // Merge with cached content if caching is enabled
                        let finalHtml = data.html;


                        // Inject the raw cascade HTML
                        container.innerHTML = finalHtml;

                        // Attach click handlers for approval buttons in the injected content
                        attachApprovalHandlers(container);

                        // Scroll to bottom if was at bottom
                        if (isAtBottom) {
                            // Use scrollIntoView on the last element for better reliability
                            setTimeout(() => {
                                if (container.lastElementChild) {
                                    container.lastElementChild.scrollIntoView({ behavior: 'smooth', block: 'end' });
                                } else {
                                    container.scrollTop = container.scrollHeight;
                                }
                            }, 100);
                        }
                    }
                } else if (data.error) {
                    document.getElementById('cascade-container').innerHTML = `
                        <div class="chat-empty">
                            <span class="icon">⚠️</span>
                            <span>${data.error}</span>
                        </div>
                    `;
                }
            } catch (e) {
                console.log('Chat fetch error:', e);
            }
        }

        function startChatPolling() {
            if (chatPollTimer) return;
            chatPollingActive = true;
            lastCascadeHash = null;
            fetchLiveChat();
            const interval = parseInt(document.getElementById('refreshInterval').value) || 2000;
            chatPollTimer = setInterval(fetchLiveChat, interval);
        }

        function restartChatPolling() {
            // Restart polling with new interval
            if (chatPollTimer) {
                clearInterval(chatPollTimer);
                chatPollTimer = null;
            }
            if (chatPollingActive) {
                const interval = parseInt(document.getElementById('refreshInterval').value) || 2000;
                chatPollTimer = setInterval(fetchLiveChat, interval);
            }
        }

        // Wire up refresh interval change
        document.getElementById('refreshInterval').addEventListener('change', restartChatPolling);

        function stopChatPolling() {
            chatPollingActive = false;
            if (chatPollTimer) {
                clearInterval(chatPollTimer);
                chatPollTimer = null;
            }
        }


        // ====================================================================
        // File Browser
        // ====================================================================
        let currentFilePath = null;
        let previousActivePanel = 'chat'; // Track what was active before Files opened

```

## File: payload\public\js\chat.js
```
/* ============================================
 * Chat — Messages, rendering, activity
 * ============================================ */

        function addChatMessage(msg, animate = true) {
            chatMessages.push(msg);
            if (chatMessages.length > 100) chatMessages.shift();

            // Track user prompts for remote history display
            if (msg.type === 'user' || msg.type === 'mobile_command') {
                // Only process unique prompts to prevent duplicates from history sync
                const isDuplicate = remotePrompts.length > 0 && remotePrompts[remotePrompts.length - 1].content === msg.content;
                if (!isDuplicate) {
                    remotePrompts.push(msg);
                    renderRemotePrompts();
                }
            }

            renderChat(animate);
        }

        let remotePrompts = [];

        function renderRemotePrompts() {
            const container = document.getElementById('remotePrompts');
            if (!container) return;

            // Keep only the last 3 prompts
            if (remotePrompts.length > 3) {
                remotePrompts.shift();
            }

            if (remotePrompts.length === 0) {
                container.innerHTML = '';
                return;
            }

            container.innerHTML = remotePrompts.map(msg => `
                    <div class="remote-prompt-item">${escapeHtml(msg.content)}</div>
                `).join('');

            // Smoothly pin to bottom when a new one is added
            container.scrollTop = container.scrollHeight;
        }

        function renderChat(animate = true) {
            const container = document.getElementById('chatMessages');
            if (!container) return; // Guard against null

            if (chatMessages.length === 0) {
                container.innerHTML = `
                    <div class="chat-empty">
                        <span class="icon">💬</span>
                        <span>Chat messages will appear here</span>
                    </div>
                `;
                return;
            }

            container.innerHTML = chatMessages.map((msg, i) => {
                const isNew = animate && i === chatMessages.length - 1;
                const type = msg.type || 'agent';
                let className = 'agent';
                if (type === 'user' || type === 'mobile_command') className = 'user';
                else if (type === 'status') className = 'status';
                else if (type === 'error') className = 'error';

                return `
                    <div class="chat-msg ${className}" ${isNew ? 'style="animation: msgIn 0.3s ease"' : ''}>
                        ${escapeHtml(msg.content)}
                        <div class="chat-msg-time">${formatTime(msg.timestamp)}</div>
                    </div>
                `;
            }).join('');

            container.scrollTop = container.scrollHeight;
        }

        async function sendChatMessage() {
            const input = document.getElementById('chatInput');
            const text = input.value.trim();
            if (!text) return;

            try {
                const res = await authFetch(`${serverUrl}/api/cdp/inject`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text, submit: true })
                });

                const result = await res.json();
                if (result.success) {
                    input.value = '';
                    showToast('Sent!', 'success');
                } else {
                    throw new Error(result.error);
                }
            } catch (e) {
                showToast('Failed to send', 'error');
            }
        }

        function sendQuick(cmd) {
            document.getElementById('chatInput').value = cmd;
            sendChatMessage();
        }

        // ====================================================================
        // Activity
        // ====================================================================
        function renderActivity() {
            const feed = document.getElementById('activityFeed');

            if (chatMessages.length === 0) {
                feed.innerHTML = `
                    <div style="text-align: center; padding: 60px 20px; color: var(--text-muted);">
                        <div style="font-size: 48px; margin-bottom: 12px; opacity: 0.4;">📭</div>
                        <p>No activity yet</p>
                    </div>
                `;
                return;
            }

            feed.innerHTML = [...chatMessages].reverse().map(msg => `
                <div class="card" style="margin-bottom: 8px; padding: 12px 16px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-size: 10px; font-weight: 700; text-transform: uppercase; padding: 3px 8px; border-radius: 4px; background: rgba(139, 92, 246, 0.2); color: var(--accent-primary);">${msg.type}</span>
                        <span style="font-size: 11px; color: var(--text-muted);">${formatTime(msg.timestamp)}</span>
                    </div>
                    <div style="font-size: 14px; line-height: 1.5;">${escapeHtml(msg.content)}</div>
                </div>
            `).join('');
        }

        // ====================================================================
        // Settings
        // ====================================================================

```

## File: payload\public\js\files.js
```
/* ============================================
 * Files — Browser, viewer, editor, zoom
 * ============================================ */

        function openFilesPanel() {
            // Remember what panel was active before opening files
            const activeBtn = document.querySelector('.sidebar-item.active');
            if (activeBtn && activeBtn.dataset.panel !== 'files') {
                previousActivePanel = activeBtn.dataset.panel;
            }

            document.getElementById('filesOverlay').classList.add('open');
            document.getElementById('filesPanel').classList.add('open');
            document.body.classList.add('no-scroll'); // Prevent background scroll
            if (!currentFilePath) {
                loadFiles();
            }
        }

        function closeFilesPanel() {
            document.getElementById('filesOverlay').classList.remove('open');
            document.getElementById('filesPanel').classList.remove('open');
            document.body.classList.remove('no-scroll'); // Restore background scroll

            // Restore previous active nav button (only if Files was active)
            const filesBtn = document.querySelector('.sidebar-item[data-panel="files"]');
            if (filesBtn && filesBtn.classList.contains('active')) {
                document.querySelectorAll('.sidebar-item').forEach(b => b.classList.remove('active'));
                document.querySelector(`.sidebar-item[data-panel="${previousActivePanel}"]`).classList.add('active');
            }

            // Stop file watching to save resources
            authFetch(`${serverUrl}/api/files/unwatch`, { method: 'POST' }).catch(() => { });
        }

        async function loadFiles(path = null) {
            try {
                const url = path ? `${serverUrl}/api/files?path=${encodeURIComponent(path)}` : `${serverUrl}/api/files`;
                const res = await authFetch(url);
                const data = await res.json();

                if (data.error) {
                    document.getElementById('filesList').innerHTML = `<div class="quota-error">${data.error}</div>`;
                    return;
                }

                currentFilePath = data.path;

                // Show breadcrumb (shortened)
                const breadcrumb = data.path.length > 40 ? '...' + data.path.slice(-37) : data.path;
                document.getElementById('filesBreadcrumb').textContent = breadcrumb;

                // Render file list
                let html = '';

                // Add "go up" option if not at root
                if (data.parent && data.parent !== data.path) {
                    html += `<div class="file-item" onclick="loadFiles('${escapeQuotes(data.parent)}')">
                            <span class="file-icon">⬆️</span>
                            <span class="file-name">..</span>
                        </div>`;
                }

                html += data.items.map(item => {
                    const icon = getFileIcon(item);
                    const size = item.isDirectory ? '' : formatSize(item.size);
                    const clickAction = item.isDirectory
                        ? `loadFiles('${escapeQuotes(item.path)}')`
                        : `viewFile('${escapeQuotes(item.path)}', '${item.extension || ''}')`;
                    return `<div class="file-item" onclick="${clickAction}">
                            <span class="file-icon">${icon}</span>
                            <span class="file-name">${escapeHtml(item.name)}</span>
                            <span class="file-size">${size}</span>
                        </div>`;
                }).join('');

                document.getElementById('filesList').innerHTML = html || '<div class="quota-error">Empty folder</div>';
            } catch (e) {
                document.getElementById('filesList').innerHTML = `<div class="quota-error">Error: ${e.message}</div>`;
            }
        }

        function getFileIcon(item) {
            if (item.isDirectory) return '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>';
            const ext = (item.extension || '').toLowerCase();
            const docIcon = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>';
            const codeIcon = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>';
            const imgIcon = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>';
            const configIcon = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M12 1v6m0 6v10M4.22 4.22l4.24 4.24m7.08 7.08l4.24 4.24M1 12h6m6 0h10M4.22 19.78l4.24-4.24m7.08-7.08l4.24-4.24"></path></svg>';

            const icons = {
                '.js': codeIcon, '.mjs': codeIcon, '.ts': codeIcon, '.jsx': codeIcon, '.tsx': codeIcon,
                '.json': docIcon, '.md': docIcon, '.txt': docIcon,
                '.html': codeIcon, '.css': codeIcon,
                '.py': codeIcon, '.sh': configIcon, '.bat': configIcon,
                '.png': imgIcon, '.jpg': imgIcon, '.jpeg': imgIcon, '.gif': imgIcon, '.webp': imgIcon, '.svg': imgIcon,
                '.yml': configIcon, '.yaml': configIcon, '.toml': configIcon
            };
            return icons[ext] || docIcon;
        }

        function formatSize(bytes) {
            if (!bytes) return '';
            if (bytes < 1024) return bytes + ' B';
            if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
            return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
        }

        function escapeQuotes(str) {
            if (!str) return '';
            return str.replace(/'/g, "\\'").replace(/\\/g, "\\\\");
        }

        // ====================================================================
        // File Viewer
        // ====================================================================
        let currentViewingFile = null; // Track currently open file for editing

        // Map extensions to Highlight.js language names
        function getLanguage(ext) {
            const langMap = {
                '.js': 'javascript', '.mjs': 'javascript', '.ts': 'typescript',
                '.json': 'json', '.html': 'html', '.css': 'css',
                '.py': 'python', '.sh': 'bash', '.bat': 'dos',
                '.md': 'markdown', '.yml': 'yaml', '.yaml': 'yaml',
                '.xml': 'xml', '.sql': 'sql',
                '.txt': 'plaintext', '.log': 'plaintext', '.env': 'plaintext'
            };
            return langMap[ext] || 'plaintext';
        }
        // Image extensions
        const imageExtensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.ico', '.bmp'];

        function isImageFile(ext) {
            return imageExtensions.includes((ext || '').toLowerCase());
        }

        async function viewFile(path, ext) {
            // Check if it's an image file
            if (isImageFile(ext)) {
                viewImageFile(path, ext);
                return;
            }

            // Text file handling
            try {
                const res = await authFetch(`${serverUrl}/api/files/content?path=${encodeURIComponent(path)}`);
                const data = await res.json();

                if (data.error) {
                    showToast(data.error, 'error');
                    return;
                }

                // Store current file path for editing
                currentViewingFile = path;

                const lang = getLanguage(data.extension);
                const codeEl = document.getElementById('fileViewerContent');

                // Reset the element for re-highlighting
                codeEl.removeAttribute('data-highlighted');
                codeEl.innerHTML = ''; // Clear previous highlighted HTML

                document.getElementById('fileViewerTitle').textContent = data.name;
                codeEl.textContent = data.content;
                codeEl.className = `language-${lang}`;

                // Apply syntax highlighting
                if (typeof hljs !== 'undefined' && lang !== 'plaintext') {
                    hljs.highlightElement(codeEl);
                }

                // Show text viewer, hide image viewer
                document.getElementById('viewerContent').style.display = 'block';
                document.getElementById('imageContent').style.display = 'none';
                document.getElementById('editBtn').style.display = 'inline-flex';

                document.getElementById('fileViewer').classList.add('open');
            } catch (e) {
                showToast('Failed to load file', 'error');
            }
        }

        async function viewImageFile(path, ext) {
            const filename = path.split(/[/\\]/).pop();
            document.getElementById('fileViewerTitle').textContent = filename;

            // Show image viewer, hide text viewer
            document.getElementById('viewerContent').style.display = 'none';
            document.getElementById('imageContent').style.display = 'flex';
            document.getElementById('editBtn').style.display = 'none'; // Can't edit images
            document.getElementById('editorContent').style.display = 'none';
            document.getElementById('editorActions').style.display = 'none';

            currentViewingFile = null; // Images not editable

            document.getElementById('fileViewer').classList.add('open');

            // Remove any existing overlay first
            const existingOverlay = document.getElementById('imageOverlay');
            if (existingOverlay) existingOverlay.remove();

            // Create loading overlay
            const overlay = document.createElement('div');
            overlay.id = 'imageOverlay';
            overlay.style.cssText = `
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        bottom: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        background: #000 !important;
        z-index: 99999 !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    `;

            // Show loading spinner first
            overlay.innerHTML = `
        <div style="position: absolute; top: 10px; left: 10px; right: 10px; display: flex; justify-content: space-between; align-items: center; z-index: 10;">
            <span style="color: white; font-size: 14px; font-weight: 600;">${filename}</span>
            <button onclick="closeImageOverlay()" style="width: 40px; height: 40px; border: none; background: rgba(255,255,255,0.2); color: white; font-size: 20px; border-radius: 50%; cursor: pointer;">✕</button>
        </div>
        <div id="imageLoader" style="display: flex; flex-direction: column; align-items: center; gap: 16px;">
            <div style="width: 48px; height: 48px; border: 3px solid rgba(255,255,255,0.1); border-top-color: #8b5cf6; border-radius: 50%; animation: spin 1s linear infinite;"></div>
            <span style="color: rgba(255,255,255,0.7); font-size: 14px;">Loading image...</span>
        </div>
        <style>@keyframes spin { to { transform: rotate(360deg); } }</style>
    `;
            document.body.appendChild(overlay);

            // Fetch image with auth token
            try {
                const imgUrl = `${serverUrl}/api/files/raw?path=${encodeURIComponent(path)}`;
                const res = await authFetch(imgUrl);

                if (!res.ok) {
                    showToast('Failed to load image', 'error');
                    closeImageOverlay();
                    return;
                }

                const blob = await res.blob();
                const objectUrl = URL.createObjectURL(blob);

                // Replace loading with actual image content
                overlay.innerHTML = `
            <div style="position: absolute; top: 10px; left: 10px; right: 10px; display: flex; justify-content: space-between; align-items: center; z-index: 10;">
                <span style="color: white; font-size: 14px; font-weight: 600;">${filename}</span>
                <button onclick="closeImageOverlay()" style="width: 40px; height: 40px; border: none; background: rgba(255,255,255,0.2); color: white; font-size: 20px; border-radius: 50%; cursor: pointer;">✕</button>
            </div>
            <div style="position: absolute; top: 60px; display: flex; gap: 8px; padding: 6px 12px; background: rgba(0,0,0,0.7); border-radius: 20px; z-index: 10;">
                <button onclick="zoomImage(-1)" style="width: 32px; height: 32px; border: none; background: rgba(255,255,255,0.15); color: white; font-size: 18px; border-radius: 50%; cursor: pointer;">−</button>
                <span id="zoomLevel" style="color: white; font-size: 13px; font-weight: 600; min-width: 50px; text-align: center; line-height: 32px;">100%</span>
                <button onclick="zoomImage(1)" style="width: 32px; height: 32px; border: none; background: rgba(255,255,255,0.15); color: white; font-size: 18px; border-radius: 50%; cursor: pointer;">+</button>
                <button onclick="resetZoom()" style="width: 32px; height: 32px; border: none; background: rgba(255,255,255,0.15); color: white; font-size: 18px; border-radius: 50%; cursor: pointer;">↺</button>
            </div>
            <div id="imageWrapper" style="flex: 1; display: flex; align-items: center; justify-content: center; width: 100%; height: calc(100% - 120px); padding: 20px; overflow: auto;">
                <img src="${objectUrl}" alt="Image preview" id="zoomableImage" style="max-width: 100%; max-height: 100%; object-fit: contain; transition: transform 0.15s ease-out;">
            </div>
            <div style="position: absolute; bottom: 12px; color: rgba(255,255,255,0.5); font-size: 11px; padding: 4px 12px; background: rgba(0,0,0,0.5); border-radius: 12px;">Pinch to zoom • Double-tap to fit</div>
        `;

                initImageZoom();
            } catch (e) {
                showToast('Error loading image', 'error');
                closeImageOverlay();
            }
        }

        function closeImageOverlay() {
            const overlay = document.getElementById('imageOverlay');
            if (overlay) overlay.remove();
            closeFileViewer();
        }

        // ====================================================================
        // Image Zoom Functionality
        // ====================================================================
        let currentZoom = 1;
        let imageTranslateX = 0;
        let imageTranslateY = 0;

        function initImageZoom() {
            currentZoom = 1;
            imageTranslateX = 0;
            imageTranslateY = 0;

            const wrapper = document.getElementById('imageWrapper');
            const img = document.getElementById('zoomableImage');
            if (!wrapper || !img) return;

            let lastTouchEnd = 0;
            let initialDistance = 0;
            let initialZoom = 1;

            // Double-tap to toggle fit/actual size
            wrapper.addEventListener('touchend', (e) => {
                const now = Date.now();
                if (now - lastTouchEnd < 300 && e.changedTouches.length === 1) {
                    e.preventDefault();
                    if (currentZoom === 1) {
                        // Fit to width
                        const containerWidth = wrapper.clientWidth;
                        const imgWidth = img.naturalWidth;
                        currentZoom = Math.min(containerWidth / imgWidth, 3);
                    } else {
                        resetZoom();
                    }
                    updateZoom();
                }
                lastTouchEnd = now;
            });

            // Pinch to zoom
            wrapper.addEventListener('touchstart', (e) => {
                if (e.touches.length === 2) {
                    initialDistance = getDistance(e.touches[0], e.touches[1]);
                    initialZoom = currentZoom;
                }
            });

            wrapper.addEventListener('touchmove', (e) => {
                if (e.touches.length === 2) {
                    e.preventDefault();
                    const distance = getDistance(e.touches[0], e.touches[1]);
                    const scale = distance / initialDistance;
                    currentZoom = Math.min(Math.max(initialZoom * scale, 0.5), 5);
                    updateZoom();
                }
            }, { passive: false });

            // Mouse wheel zoom for desktop
            wrapper.addEventListener('wheel', (e) => {
                e.preventDefault();
                const delta = e.deltaY > 0 ? -0.2 : 0.2;
                currentZoom = Math.min(Math.max(currentZoom + delta, 0.5), 5);
                updateZoom();
            }, { passive: false });
        }

        function getDistance(touch1, touch2) {
            const dx = touch1.clientX - touch2.clientX;
            const dy = touch1.clientY - touch2.clientY;
            return Math.sqrt(dx * dx + dy * dy);
        }

        function zoomImage(direction) {
            currentZoom = Math.min(Math.max(currentZoom + direction * 0.25, 0.5), 5);
            updateZoom();
        }

        function resetZoom() {
            currentZoom = 1;
            imageTranslateX = 0;
            imageTranslateY = 0;
            updateZoom();
        }

        function updateZoom() {
            const img = document.getElementById('zoomableImage');
            const levelEl = document.getElementById('zoomLevel');
            if (img) {
                img.style.transform = `scale(${currentZoom}) translate(${imageTranslateX}px, ${imageTranslateY}px)`;
            }
            if (levelEl) {
                levelEl.textContent = Math.round(currentZoom * 100) + '%';
            }
        }

        function closeFileViewer() {
            document.getElementById('fileViewer').classList.remove('open');
            // Reset to view mode when closing
            cancelEditing();
            // Clear image src to free memory
            document.getElementById('imagePreview').src = '';
        }

        // ====================================================================
        // File Editing
        // ====================================================================
        let isEditing = false;

        function startEditing() {
            if (!currentViewingFile) return;

            isEditing = true;
            const content = document.getElementById('fileViewerContent').textContent;
            document.getElementById('fileEditor').value = content;

            // Show editor, hide viewer
            document.getElementById('viewerContent').style.display = 'none';
            document.getElementById('editorContent').style.display = 'block';
            document.getElementById('editorActions').style.display = 'flex';
            document.getElementById('editBtn').style.display = 'none';
        }

        function cancelEditing() {
            isEditing = false;
            document.getElementById('viewerContent').style.display = 'block';
            document.getElementById('editorContent').style.display = 'none';
            document.getElementById('editorActions').style.display = 'none';
            document.getElementById('editBtn').style.display = 'inline-flex';
        }

        async function saveFile() {
            if (!currentViewingFile) return;

            const content = document.getElementById('fileEditor').value;

            try {
                const res = await authFetch(`${serverUrl}/api/files/save`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ path: currentViewingFile, content })
                });
                const data = await res.json();

                if (data.error) {
                    showToast(data.error, 'error');
                    return;
                }

                showToast('File saved!', 'success');

                // Update the viewer with new content
                document.getElementById('fileViewerContent').textContent = content;
                cancelEditing();

                // Re-apply syntax highlighting
                const codeEl = document.getElementById('fileViewerContent');
                codeEl.removeAttribute('data-highlighted');
                if (typeof hljs !== 'undefined') {
                    hljs.highlightElement(codeEl);
                }
            } catch (e) {
                showToast('Save failed', 'error');
            }
        }

        // ====================================================================
        // Init
        // ====================================================================
        async function applyMobileUISettings() {
            try {
                const res = await authFetch('/api/admin/mobile-ui');
                const settings = await res.json();

                // Quick actions visibility — use CSS class so it persists through DOM updates
                if (settings.showQuickActions === false) {
                    document.body.classList.add('hide-quick-actions');
                } else {
                    document.body.classList.remove('hide-quick-actions');
                }

                // Navigation mode
                if (settings.navigationMode === 'topbar') {
                    document.body.classList.add('topbar-mode');
                    document.body.classList.remove('sidebar-mode');
                } else {
                    document.body.classList.add('sidebar-mode');
                    document.body.classList.remove('topbar-mode');
                }

                // Assist tab visibility
                const showAssist = settings.showAssistTab || false;
                const sidebarAssistBtn = document.getElementById('sidebarAssistBtn');
                const topbarAssistBtn = document.getElementById('topbarAssistBtn');
                if (sidebarAssistBtn) sidebarAssistBtn.style.display = showAssist ? '' : 'none';
                if (topbarAssistBtn) topbarAssistBtn.style.display = showAssist ? '' : 'none';
                // Re-bind events for dynamically shown assist buttons
                if (showAssist) {
                    if (sidebarAssistBtn && !sidebarAssistBtn._bound) {
                        sidebarAssistBtn.addEventListener('click', () => switchPanel('assist', '.sidebar-item'));
                        sidebarAssistBtn._bound = true;
                    }
                    if (topbarAssistBtn && !topbarAssistBtn._bound) {
                        topbarAssistBtn.addEventListener('click', () => switchPanel('assist', '.topbar-btn'));
                        topbarAssistBtn._bound = true;
                    }
                }
            } catch (e) { }
        }

        // ====================================================================
        // Assist Chat Functions
        // ====================================================================

```

## File: payload\public\js\icons.js
```
/* ============================================
 * Icons — SVG icon helper (replaces emojis)
 * ============================================ */

function svgIcon(name, size) {
    var s = size || 16;
    var icons = {
        brain: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/><line x1="8" y1="16" x2="8" y2="16"/><line x1="16" y1="16" x2="16" y2="16"/></svg>',
        clipboard: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/></svg>',
        clock: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
        play: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>',
        check: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
        close: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
        dotGreen: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 16 16"><circle cx="8" cy="8" r="5" fill="#22c55e"/></svg>',
        dotYellow: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 16 16"><circle cx="8" cy="8" r="5" fill="#eab308"/></svg>',
        dotBlue: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 16 16"><circle cx="8" cy="8" r="5" fill="#3b82f6"/></svg>',
        dotRed: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 16 16"><circle cx="8" cy="8" r="5" fill="#ef4444"/></svg>',
        dotGray: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 16 16"><circle cx="8" cy="8" r="5" fill="#6b7280"/></svg>'
    };
    return '<span style="display:inline-flex;align-items:center;vertical-align:middle;flex-shrink:0;min-width:' + s + 'px;min-height:' + s + 'px;">' + (icons[name] || '') + '</span>';
}

```

## File: payload\public\js\navigation.js
```
/* ============================================
 * Navigation — Panels, status, sidebar
 * ============================================ */

        function updateStatus(connected) {
            const pill = document.getElementById('statusPill');
            pill.className = `status-pill ${connected ? 'connected' : 'disconnected'}`;
            pill.querySelector('span').textContent = connected ? 'Connected' : 'Offline';

            // Sync topbar status dot
            const topbarDot = document.getElementById('topbarStatusDot');
            if (topbarDot) {
                topbarDot.className = `topbar-status ${connected ? 'online' : ''}`;
            }
        }

        // ====================================================================
        // View Switching (simplified - Chat is always visible)
        // ====================================================================

        // Shared panel-switching logic for both sidebar and topbar
        function switchPanel(panel, sourceSelector) {
            // Update active states on both sidebar and topbar
            document.querySelectorAll('.sidebar-item').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.topbar-btn').forEach(b => b.classList.remove('active'));
            const sidebarBtn = document.querySelector(`.sidebar-item[data-panel="${panel}"]`);
            const topbarBtn = document.querySelector(`.topbar-btn[data-panel="${panel}"]`);
            if (sidebarBtn) sidebarBtn.classList.add('active');
            if (topbarBtn) topbarBtn.classList.add('active');

            if (panel === 'settings') {
                document.getElementById('settingsPanel').style.display = 'block';
                document.getElementById('assistPanel').style.display = 'none';
                closeFilesPanel();
                loadSettings();
            } else if (panel === 'files') {
                document.getElementById('settingsPanel').style.display = 'none';
                document.getElementById('assistPanel').style.display = 'none';
                openFilesPanel();
            } else if (panel === 'assist') {
                document.getElementById('assistPanel').style.display = 'block';
                document.getElementById('settingsPanel').style.display = 'none';
                closeFilesPanel();
                loadAssistChatHistory();
                loadAssistStatusBadge();
            } else if (panel === 'chat') {
                document.getElementById('settingsPanel').style.display = 'none';
                document.getElementById('assistPanel').style.display = 'none';
                closeFilesPanel();
            }
        }

        // Sidebar Nav
        document.querySelectorAll('.sidebar-item').forEach(btn => {
            btn.addEventListener('click', () => switchPanel(btn.dataset.panel, '.sidebar-item'));
        });

        // Topbar Nav
        document.querySelectorAll('.topbar-btn').forEach(btn => {
            btn.addEventListener('click', () => switchPanel(btn.dataset.panel, '.topbar-btn'));
        });

        function closePanel() {
            document.getElementById('settingsPanel').style.display = 'none';
            document.getElementById('assistPanel').style.display = 'none';
            closeFilesPanel();
            document.querySelectorAll('.sidebar-item').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.topbar-btn').forEach(b => b.classList.remove('active'));
            const sidebarChat = document.querySelector('.sidebar-item[data-panel="chat"]');
            const topbarChat = document.querySelector('.topbar-btn[data-panel="chat"]');
            if (sidebarChat) sidebarChat.classList.add('active');
            if (topbarChat) topbarChat.classList.add('active');
        }

        // ====================================================================
        // Chat
        // ====================================================================

```

## File: payload\public\js\settings.js
```
/* ============================================
 * Settings — Config, commands, quota
 * ============================================ */

        async function loadSettings() {
            try {
                const res = await authFetch(`${serverUrl}/api/cdp/status`);
                const data = await res.json();
                const el = document.getElementById('cdpStatus');
                if (data.available) {
                    el.innerHTML = '<svg class="status-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Active';
                    el.style.color = 'var(--success)';
                } else {
                    el.innerHTML = '<svg class="status-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg> Offline';
                    el.style.color = 'var(--error)';
                }
            } catch {
                const el = document.getElementById('cdpStatus');
                el.innerHTML = '<svg class="status-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg> Error';
                el.style.color = 'var(--error)';
            }
            // Also load quota when settings panel opens
            loadQuota();
            loadMobileCommands();
        }

        // ====================================================================
        // Quick Commands (Mobile)
        // ====================================================================
        async function loadMobileCommands() {
            const container = document.getElementById('mobileCommandsContainer');
            try {
                const res = await authFetch('/api/admin/commands');
                const data = await res.json();
                const commands = data.commands || [];
                if (commands.length === 0) {
                    container.innerHTML = '<div style="color: var(--text-muted); padding: 8px;">No commands configured. Add them in the Admin Panel.</div>';
                    return;
                }
                container.innerHTML = commands.map((cmd, i) => `
                        <div class="setting-row" style="cursor: pointer;" onclick="executeMobileCommand(${i}, '${cmd.prompt.replace(/'/g, "\\'")}')">
                            <div class="setting-label">
                                <h4>${cmd.icon || '⚡'} ${cmd.label}</h4>
                                <p>${cmd.prompt.slice(0, 50)}${cmd.prompt.length > 50 ? '...' : ''}</p>
                            </div>
                            <div class="setting-value" id="cmdStatus${i}" style="font-size: 12px;">▶</div>
                        </div>
                    `).join('');
            } catch (e) { container.innerHTML = '<div style="color: var(--error); padding: 8px;">Failed to load commands</div>'; }
        }

        async function executeMobileCommand(index, prompt) {
            const statusEl = document.getElementById(`cmdStatus${index}`);
            statusEl.textContent = '⏳';
            try {
                const res = await authFetch('/api/commands/execute', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ prompt }) });
                const result = await res.json();
                statusEl.textContent = result.success ? '✅' : '❌';
                setTimeout(() => statusEl.textContent = '▶', 3000);
            } catch (e) {
                statusEl.textContent = '❌';
                setTimeout(() => statusEl.textContent = '▶', 3000);
            }
        }

        // ====================================================================
        // Quota Display
        // ====================================================================
        let quotaData = null;
        let quotaLoading = false;

        async function loadQuota() {
            if (quotaLoading) return;
            quotaLoading = true;

            const container = document.getElementById('quotaContainer');
            container.innerHTML = `
                    <div class="quota-loading">
                        <div class="spinner"></div>
                        <div style="margin-top: 10px;">Loading quota data...</div>
                    </div>
                `;

            try {
                const res = await authFetch(`${serverUrl}/api/quota`);
                const data = await res.json();
                quotaData = data;
                renderQuota(data);
            } catch (e) {
                container.innerHTML = `
                        <div class="quota-error">
                            <div style="font-size: 32px; opacity: 0.5; margin-bottom: 10px;">⚠️</div>
                            <div>Failed to load quota data</div>
                            <div style="font-size: 11px; margin-top: 6px; opacity: 0.7;">${e.message}</div>
                        </div>
                    `;
            } finally {
                quotaLoading = false;
            }
        }

        function renderQuota(data) {
            const container = document.getElementById('quotaContainer');

            if (!data.available || !data.models || data.models.length === 0) {
                container.innerHTML = `
                        <div class="quota-error">
                            <div style="font-size: 32px; opacity: 0.5; margin-bottom: 10px;">🔌</div>
                            <div>${data.error || 'No quota data available'}</div>
                            <div style="font-size: 11px; margin-top: 6px; opacity: 0.7;">Make sure Antigravity is running</div>
                        </div>
                    `;
                return;
            }

            const circumference = 2 * Math.PI * 34; // radius = 34

            container.innerHTML = `
                    <div class="quota-grid">
                        ${data.models.map(model => {
                const percent = Math.max(0, Math.min(100, model.remainingPercent || 0));
                const offset = circumference - (percent / 100) * circumference;
                const displayName = formatModelName(model.name);
                const statusLabel = getStatusLabel(model.status);

                return `
                                <div class="quota-card">
                                    <div class="quota-ring">
                                        <svg viewBox="0 0 80 80">
                                            <circle class="ring-bg" cx="40" cy="40" r="34"></circle>
                                            <circle class="ring-progress ${model.status}" 
                                                cx="40" cy="40" r="34"
                                                stroke-dasharray="${circumference}"
                                                stroke-dashoffset="${offset}">
                                            </circle>
                                        </svg>
                                        <div class="quota-percent ${model.status}">${percent.toFixed(0)}%</div>
                                    </div>
                                    <div class="quota-model-name" title="${model.name}">${displayName}</div>
                                    <div class="quota-reset">
                                        ${model.resetIn ? `Reset: ${model.resetIn}` : ''}
                                    </div>
                                    <span class="quota-status-badge ${model.status}">${statusLabel}</span>
                                </div>
                            `;
            }).join('')}
                    </div>
                `;
        }

        function formatModelName(name) {
            // Shorten long model names
            if (!name) return 'Unknown';
            // Remove common prefixes and clean up
            return name
                .replace(/^MODEL_/, '')
                .replace(/_/g, ' ')
                .split(' ')
                .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
                .join(' ')
                .substring(0, 20);
        }

        function getStatusLabel(status) {
            const labels = {
                'healthy': 'Healthy',
                'warning': 'Warning',
                'danger': 'Danger',
                'exhausted': 'Exhausted'
            };
            return labels[status] || status || 'Unknown';
        }

        async function clearAllData() {
            chatMessages = [];
            renderChat();
            await authFetch(`${serverUrl}/api/messages/clear`, { method: 'POST' });
            showToast('Data cleared', 'success');
        }

```

## File: payload\public\js\task-queue.js
```
/* ============================================
 * Task Queue — Queue management UI
 * ============================================ */

function toggleTaskQueue() {
    taskQueueExpanded = !taskQueueExpanded;
    var items = document.getElementById('taskQueueItems');
    var input = document.getElementById('taskQueueInput');
    var arrow = document.getElementById('taskQueueArrow');
    var chatMsgs = document.getElementById('assistChatMessages');
    if (taskQueueExpanded) {
        items.style.display = 'block';
        input.style.display = 'block';
        arrow.innerHTML = '&#9650;';
        chatMsgs.style.bottom = '260px';
        refreshTaskQueue();
    } else {
        items.style.display = 'none';
        input.style.display = 'none';
        arrow.innerHTML = '&#9660;';
        chatMsgs.style.bottom = '100px';
    }
}

async function addQueueTask() {
    var input = document.getElementById('taskQueueAddInput');
    var instruction = input.value.trim();
    if (!instruction) return;
    input.value = '';
    try {
        await fetch(serverUrl + '/api/supervisor/queue', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ instruction: instruction })
        });
        refreshTaskQueue();
    } catch (e) { }
}

async function removeQueueTask(index) {
    try {
        await fetch(serverUrl + '/api/supervisor/queue/' + index, { method: 'DELETE' });
        refreshTaskQueue();
    } catch (e) { }
}

async function clearQueue() {
    try {
        await fetch(serverUrl + '/api/supervisor/queue', { method: 'DELETE' });
        refreshTaskQueue();
    } catch (e) { }
}

async function refreshTaskQueue() {
    try {
        var res = await fetch(serverUrl + '/api/supervisor/queue');
        var data = await res.json();
        var queue = data.queue || [];
        var countEl = document.getElementById('taskQueueCount');
        var itemsEl = document.getElementById('taskQueueItems');
        var queuePanel = document.getElementById('assistTaskQueue');

        countEl.textContent = '(' + queue.length + ')';
        queuePanel.style.display = queue.length > 0 || taskQueueExpanded ? 'block' : 'none';

        if (queue.length === 0) {
            itemsEl.innerHTML = '<div style="font-size:12px;color:var(--text-muted);padding:8px 0;">No tasks in queue. Add one below.</div>';
            return;
        }

        var statusIcons = { pending: svgIcon('clock', 14), running: svgIcon('play', 14), completed: svgIcon('check', 14) };
        var statusColors = { pending: 'var(--text-muted)', running: 'var(--accent-primary)', completed: '#4caf50' };
        var html = '';
        for (var i = 0; i < queue.length; i++) {
            var t = queue[i];
            html += '<div style="display:flex;align-items:center;gap:8px;padding:4px 0;border-bottom:1px solid rgba(255,255,255,0.05);">'
                + '<span style="font-size:14px;">' + (statusIcons[t.status] || svgIcon('clock', 14)) + '</span>'
                + '<span style="flex:1;font-size:12px;color:' + (statusColors[t.status] || 'var(--text-primary)') + ';">' + t.instruction.substring(0, 60) + (t.instruction.length > 60 ? '...' : '') + '</span>';
            if (t.status !== 'completed') {
                html += '<button onclick="removeQueueTask(' + i + ')" style="background:none;border:none;color:var(--error);cursor:pointer;padding:2px 4px;display:flex;align-items:center;" title="Remove">' + svgIcon('close', 14) + '</button>';
            }
            html += '</div>';
        }
        if (queue.some(function (t) { return t.status === 'completed'; })) {
            html += '<div style="padding:4px 0;"><button onclick="clearQueue()" style="font-size:11px;padding:4px 10px;background:rgba(255,255,255,0.06);border:1px solid var(--border);border-radius:6px;color:var(--text-muted);cursor:pointer;">Clear completed</button></div>';
        }
        itemsEl.innerHTML = html;
    } catch (e) { }
}

```

## File: payload\public\js\theme.js
```
/* ============================================
 * Theme — Switching, icons, sidebar state
 * ============================================ */

function setTheme(theme) {
    // Remove all theme classes
    document.body.classList.remove('light-theme', 'pastel-theme', 'rainbow-theme', 'slate-theme');

    // Add the selected theme class (dark is default with no class)
    if (theme === 'light') {
        document.body.classList.add('light-theme');
    } else if (theme === 'pastel') {
        document.body.classList.add('pastel-theme');
    } else if (theme === 'rainbow') {
        document.body.classList.add('rainbow-theme');
    } else if (theme === 'slate') {
        document.body.classList.add('slate-theme');
    }

    localStorage.setItem('theme', theme);

    // Update theme selectors
    const sidebarSelect = document.getElementById('sidebarThemeSelect');
    const settingsSelect = document.getElementById('themeSelect');
    if (sidebarSelect) sidebarSelect.value = theme;
    if (settingsSelect) settingsSelect.value = theme;

    // Update theme icon
    updateThemeIcon(theme);
}

function updateThemeIcon(theme) {
    const iconBtn = document.getElementById('themeIconBtn');
    if (!iconBtn) return;

    const icons = {
        'dark': '🌙',
        'light': '☀️',
        'pastel': '🌸',
        'rainbow': '🌈',
        'slate': '◼'
    };
    iconBtn.textContent = icons[theme] || '🌙';

    // Sync topbar theme button too
    const topbarThemeBtn = document.getElementById('topbarThemeBtn');
    if (topbarThemeBtn) topbarThemeBtn.textContent = icons[theme] || '🌙';
}

function cycleTheme() {
    const themes = ['dark', 'light', 'pastel', 'rainbow', 'slate'];
    const currentTheme = localStorage.getItem('theme') || 'dark';
    const currentIndex = themes.indexOf(currentTheme);
    const nextIndex = (currentIndex + 1) % themes.length;
    setTheme(themes[nextIndex]);
}

async function loadTheme() {
    const localTheme = localStorage.getItem('theme');
    if (localTheme) {
        setTheme(localTheme);
    } else {
        // No local preference — try to use admin-configured default
        try {
            const res = await authFetch('/api/admin/mobile-ui');
            const data = await res.json();
            setTheme(data.theme || 'dark');
        } catch {
            setTheme('dark');
        }
    }
}

// Sidebar toggle
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const isExpanded = sidebar.classList.toggle('expanded');
    document.body.classList.toggle('sidebar-expanded', isExpanded);
    localStorage.setItem('sidebarExpanded', isExpanded);
}

function loadSidebarState() {
    const expanded = localStorage.getItem('sidebarExpanded') === 'true';
    if (expanded) {
        document.getElementById('sidebar').classList.add('expanded');
        document.body.classList.add('sidebar-expanded');
    }
}

// ====================================================================
// Model/Mode Selector
// ====================================================================
let availableModels = [];
let currentModel = 'Unknown';
let currentMode = 'Planning';

```

## File: payload\public\js\websocket.js
```
/* ============================================
 * WebSocket — Connection, message handling
 * ============================================ */

        function connectWebSocket() {
            const wsUrl = serverUrl.replace('http', 'ws');
            ws = new WebSocket(wsUrl);

            ws.onopen = () => {
                updateStatus(true);
                const wsEl = document.getElementById('wsStatus');
                wsEl.innerHTML = '<svg class="status-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Connected';
                wsEl.style.color = 'var(--success)';
            };

            ws.onclose = () => {
                updateStatus(false);
                const wsEl = document.getElementById('wsStatus');
                wsEl.innerHTML = '<svg class="status-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg> Disconnected';
                wsEl.style.color = 'var(--error)';
                setTimeout(connectWebSocket, 3000);
            };

            ws.onerror = () => updateStatus(false);

            ws.onmessage = (event) => {
                const data = JSON.parse(event.data);
                handleMessage(data);
            };
        }

        function handleMessage(data) {
            if (data.event === 'history') {
                data.data.messages.forEach(msg => addChatMessage(msg, false));
            } else if (data.event === 'message' || data.event === 'mobile_command') {
                addChatMessage(data.data, true);
            } else if (data.event === 'file_changed') {
                // Auto-refresh file list when files change
                handleFileChanged(data.data);
            } else if (data.event === 'workspace_changed') {
                // IDE workspace changed - update file browser
                handleWorkspaceChanged(data.data);
            }
        }

        function handleWorkspaceChanged(data) {
            console.log('📂 Workspace changed:', data.path);

            // Update the workspace path display if we have one
            const workspaceLabel = document.getElementById('workspaceLabel');
            if (workspaceLabel) {
                workspaceLabel.textContent = data.projectName || 'Files';
            }

            // If files panel is open, reload from new workspace root
            const filesPanel = document.getElementById('filesPanel');
            if (filesPanel.classList.contains('open')) {
                // Reset to workspace root
                currentFilePath = '';
                loadFiles('');
                showToast(`📂 Switched to: ${data.projectName}`, 'status');
            }
        }

        function handleFileChanged(data) {
            // Only refresh if files panel is open
            const filesPanel = document.getElementById('filesPanel');
            if (!filesPanel.classList.contains('open')) return;

            console.log('📁 File changed:', data.filename);

            // Reload current folder
            if (currentFilePath) {
                loadFiles(currentFilePath);
            }

            // If viewing a file that changed, show a notification
            if (currentViewingFile && data.filename) {
                const viewingFilename = currentViewingFile.split(/[/\\]/).pop();
                if (viewingFilename === data.filename) {
                    showToast('File changed - tap to reload', 'status');
                }
            }
        }

```

## File: payload\public\js\_DIR_IDENTITY.md
```
---
id: ecosystem-plugins-repo-fetched-antigravity-mobile-035838-public-js
name: Js
path: ecosystem/plugins/repo-fetched-antigravity-mobile-035838/public/js
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Js
Storage area for 'js' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: payload\scripts\_DIR_IDENTITY.md
```
---
id: ecosystem-plugins-repo-fetched-antigravity-mobile-035838-scripts
name: Scripts
path: ecosystem/plugins/repo-fetched-antigravity-mobile-035838/scripts
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Scripts
Storage area for 'scripts' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: payload\src\_DIR_IDENTITY.md
```
---
id: ecosystem-plugins-repo-fetched-antigravity-mobile-035838-src
name: Src
path: ecosystem/plugins/repo-fetched-antigravity-mobile-035838/src
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Src
Storage area for 'src' domain.
> Auto-generated identity tag by OMA v2.1.

```

