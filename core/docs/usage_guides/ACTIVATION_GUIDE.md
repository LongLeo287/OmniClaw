# OmniClaw Activation Guide

This guide separates OmniClaw into two boot paths.

## 1. Agent System

Use this when the goal is to run OmniClaw as the project-facing agent layer.
This path should leave OmniClaw ready for user work, with skills, plugins,
memory state, routing, and orchestrator readiness all checked.

Commands:

```bash
omniclaw doctor
omniclaw startup
omniclaw watch 30
omniclaw agent-status
```

Meaning:

- `omniclaw startup` runs the agent boot path and validates user-facing readiness.
- `omniclaw watch 30` keeps the orchestrator polling in watch mode.
- `omniclaw agent-status` reports agent-side routing and activation state.

Scope:

- orchestrator
- agent routing
- skill registry
- tool registry
- plugin inventory
- memory state
- workforce-facing execution flow

Constraint:

- the agent system may use OmniClaw, but it must not trigger self-healing, repair, registry mutation, or core-improvement flows

Excluded from this flow:

- core daemon maintenance
- bridge, UI, remote, port provisioning

## 2. Core Daemon System

Use this when the goal is to repair, maintain, sync, and upgrade OmniClaw itself.
This path is for the internal daemon side of OmniClaw, not for project-facing use.

Commands:

```bash
omniclaw doctor
omniclaw core-daemon
omniclaw core-loop 120
omniclaw core-status
omniclaw sync
```

Meaning:

- `omniclaw core-daemon` runs core startup preflight for the maintenance layer.
- `omniclaw core-loop 120` keeps internal upkeep running.
- `omniclaw core-status` reports internal state readiness.
- `omniclaw sync` refreshes internal registries and maps.

Scope:

- blackboard state
- trust matrix compliance
- daemon activation state
- registry and telemetry upkeep
- self-maintenance readiness
- system repair and improvement flows

Excluded from this flow:

- orchestrator watch for external project work
- bridge, UI, remote, port provisioning

## Operating Rule

Keep these two boot paths separate and logical:

- `Khởi động OmniClaw` => boot the agent system.
- `Khởi động Core Daemon` => boot the internal core daemon system.
