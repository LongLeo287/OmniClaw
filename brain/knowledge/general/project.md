---
id: project
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:02.154980
---

# Project Context

## Purpose

Antigravity Manager is a comprehensive enhancement tool for Antigravity, designed to remove AI development resource limits. It not only solves the lack of native multi-account switching in Antigravity IDE, but also introduces enterprise-grade AI account pool management. By taking control of app configuration state and cloud API resources, it allows users to switch seamlessly between unlimited local accounts and cloud AI services for an effectively "unlimited" AI usage experience.

**Core goals:**

* **Local multi-account switching**: Seamlessly switch Antigravity IDE local user state while protecting data integrity (automatic backup).
* **AI resource pool management (new)**: Centrally manage account pools for Google Gemini, Claude 3.5, and similar services.
* **Intelligent quota monitoring (new)**: Monitor API quota and health in real time with a visual dashboard.
* **Automatic resource scheduling (new)**: Automatically switch to the best available account when the current one runs out of quota (token keepalive + polling).
* **Cross-platform support**: Consistent macOS, Windows, and Linux experience.

## Tech Stack

* **Electron 39** - Cross-platform desktop framework
* **React 19.2** - UI framework
* **TypeScript 5.9** - Type-safe development language
* **Shadcn UI** - Modern UI component library
* **Tailwind CSS 4** - Styling framework
* **oRPC** - Type-safe IPC communication
* **TanStack Router** - File-based routing
* **React Query** - Server state management
* **better-sqlite3** - SQLite data access
* **Vite** - Build tool
* **Vitest** - Unit testing
* **Playwright** - End-to-end testing
* **Electron Forge** - Packaging and distribution

## Project Conventions

### Code Style

* TypeScript strict mode
* ESLint + Prettier auto-formatting
* Use camelCase for functions and variables
* Use PascalCase for components
* Use PascalCase for interfaces, optionally prefixed with `I`
* Use PascalCase for types
* 2-space indentation
* Single-quoted strings
* Trailing commas

### Architecture Patterns

```plaintext
src/
├── main.ts              # Electron main process
├── preload.ts           # Preload script
├── renderer.ts          # Renderer entry
├── ipc/                 # IPC communication layer
│   ├── account/         # Local IDE account IPC
│   ├── cloud/           # Cloud AI resource IPC (new)
│   ├── database/        # Database operation IPC
│   └── process/         # Process management IPC
├── services/            # Business service layer (new)
│   ├── QuotaService.ts  # Quota monitoring service
│   └── TokenService.ts  # Token keepalive service
├── actions/             # Renderer actions (oRPC client)
├── components/          # React components
├── routes/              # Page routes
├── layouts/             # Layout components
├── utils/               # Utility functions
├── types/               # TypeScript type definitions
└── tests/               # Test files
```

**Design patterns:**

* **Separation of concerns**: Main process handles system operations and network proxy; renderer handles UI.
* **Service layer**: Encapsulates complex quota polling and token refresh logic.
* **Type-safe IPC**: Uses oRPC to enforce type-safe communication between main and renderer.
* **State management**: React Query manages server state and async quota data.

### Testing Strategy

* **Unit tests (Vitest)**: IPC handlers, service logic, utility functions.
* **Integration tests (Vitest)**: End-to-end IPC flow.
* **End-to-end tests (Playwright)**: User workflows.
* **Coverage target**: Core logic > 80%.

### Git Workflow

* **Main branch**: `main`
* **Development branch**: `develop`
* **Commit style**: Conventional commits (`feat`, `fix`, `docs`, `refactor`, `test`, `chore`)

## Domain Context

### 1. Antigravity IDE Data Structure (Local)

**Database locations:**

* macOS: `~/Library/Application Support/Antigravity/User/globalStorage/state.vscdb`
* Windows: `%APPDATA%/Antigravity/User/globalStorage/state.vscdb`
* Linux: `~/.config/Antigravity/User/globalStorage/state.vscdb`

**Key database fields:**

* `antigravityAuthStatus`: Authentication status and user information.

### 2. AI Service Resource Structure (Cloud / New)

**Account model:**

```json
{
  "id": "uuid",
  "provider": "google" | "anthropic",
  "email": "user@example.com",
  "auth_token": "oauth2_token...",
  "refresh_token": "...",
  "quota_limit": 1000,
  "quota_used": 450,
  "reset_time": "ISO 8601",
  "status": "active" | "rate_limited" | "expired"
}
```

### 3. Process Management Strategy

* **Three-phase shutdown**: Graceful close -> SIGTERM -> SIGKILL.

## Important Constraints

### Technical Constraints

* **Database access**: Handle file locks when accessing local IDE databases.
* **Network access**: External API access (Google/Anthropic) is required for quota retrieval.
* **Credential security**: OAuth and refresh tokens must use system-level encrypted storage (Keytar / encrypted SQLite).
* **Concurrency control**: Quota polling frequency must be controlled to avoid API throttling or blocking.

### UX Constraints

* **Response time**: Account switching should complete within 5 seconds.
* **Silent mode**: Support tray minimization and background token refresh.
* **Data safety**: Always back up current state before switching.

## External Dependencies

### System Dependencies

* **Antigravity IDE**: Local target to manage.
* **SQLite**: Local data reads.

### Node.js Dependencies (Key)

* `better-sqlite3`: Database access.
* `electron`: Desktop framework.
* `node-fetch` / `axios`: Network requests.
* `tar` / `adm-zip`: Backup compression.

### External Services

* **Google Gemini API**: For quota checks.
* **Anthropic API**: For quota checks.
* **OAuth 2.0 endpoints**: For account authorization.

### Filesystem Dependencies

* `~/.antigravity-agent/`
  * `accounts.json`: Local IDE account index.
  * `cloud_accounts.db`: (new) Cloud account pool database (SQLite).
  * `backups/`: Backup files.
  * `app.log`: Application log.
