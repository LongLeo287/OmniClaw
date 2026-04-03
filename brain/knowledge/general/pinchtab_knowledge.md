---
id: pinchtab-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:30:59.116038
---

# KNOWLEDGE EXTRACT: pinchtab
> **Extracted on:** 2026-03-30 17:51:01
> **Source:** pinchtab

---

## File: `pinchtab.md`
```markdown
# 📦 pinchtab/pinchtab [🔖 PENDING/APPROVE]
🔗 https://github.com/pinchtab/pinchtab


## Meta
- **Stars:** ⭐ 8188 | **Forks:** 🍴 607
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
High-performance browser automation bridge and multi-instance orchestrator with advanced stealth injection and real-time dashboard.

## README (trích đầu)
```
<p align="center">
  <img src="assets/pinchtab-headless.png" alt="PinchTab" width="200"/>
</p>

<p align="center">
  <strong>PinchTab</strong><br/>
  <strong>Browser control for AI agents</strong><br/>
  Small Go binary • HTTP API • Token-efficient
</p>


<table align="center">
  <tr>
    <td align="center" valign="middle">
      <a href="https://pinchtab.com/docs"><img src="assets/docs-no-background-256.png" alt="Full Documentation" width="92"/></a>
    </td>
    <td align="left" valign="middle">
      <a href="https://github.com/pinchtab/pinchtab/releases/latest"><img src="https://img.shields.io/github/v/release/pinchtab/pinchtab?style=flat-square&color=FFD700" alt="Release"/></a><br/>
      <a href="https://github.com/pinchtab/pinchtab/actions/workflows/ci-go.yml"><img src="https://img.shields.io/github/actions/workflow/status/pinchtab/pinchtab/ci-go.yml?branch=main&style=flat-square&label=Go%20CI" alt="Go CI"/></a><br/>
      <img src="https://img.shields.io/badge/Go-1.25+-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go 1.25+"/><br/>
      <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square" alt="License"/></a>
    </td>
  </tr>
</table>

---

## What is PinchTab?

PinchTab is a **standalone HTTP server** that gives AI agents direct control over Chrome.

For day-to-day local use, the server is typically installed as a user-level daemon, allowing agent tools to reuse the same browser control plane running in the background.

```bash
curl -fsSL https://pinchtab.com/install.sh | bash
# or
pinchtab daemon install
```

This installs the control-plane server and starts a default headless Chrome instance, ready to accept requests from agents or manual API calls.

PinchTab is designed first for local, single-user control on a machine you manage. Remote and distributed layouts are supported, but they are advanced operator-managed deployments. If you bind beyond loopback, publish ports, or attach remote bridges, you are responsible for tokens, network boundaries, TLS or reverse proxying, and which endpoint families you expose.

If you run PinchTab on a different machine, do it only when you understand the security model. Keep it on a private or otherwise closed network, avoid exposing it directly to the public internet, and keep high-risk endpoint families disabled unless you explicitly need them. If you do enable them, lock them down so only the systems that need them can reach them.

> [!WARNING]
> The dashboard, HTTP API, MCP server, and remote CLI integrations are privileged operator control surfaces. They are not designed for untrusted users, multi-tenant exposure, or direct public-internet access. If you are unsure how to secure a non-local deployment, review [docs/guides/security.md](docs/guides/security.md) and use the private security contact path in [SECURITY.md](SECURITY.md) before exposing the service.


If you prefer not to run a daemon, or if you're on Windows, you can instead run
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

