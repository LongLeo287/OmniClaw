---
id: oauth2-proxy-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:13.602798
---

# KNOWLEDGE EXTRACT: oauth2-proxy
> **Extracted on:** 2026-03-30 17:49:32
> **Source:** oauth2-proxy

---

## File: `oauth2-proxy.md`
```markdown
# 📦 oauth2-proxy/oauth2-proxy [🔖 PENDING/APPROVE]
🔗 https://github.com/oauth2-proxy/oauth2-proxy
🌐 https://oauth2-proxy.github.io/oauth2-proxy

## Meta
- **Stars:** ⭐ 14097 | **Forks:** 🍴 2070
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A reverse proxy that provides authentication with Google, Azure, OpenID Connect and many more identity providers.

## README (trích đầu)
```
[![Continuous Integration](https://github.com/oauth2-proxy/oauth2-proxy/actions/workflows/ci.yml/badge.svg)](https://github.com/oauth2-proxy/oauth2-proxy/actions/workflows/ci.yml)
[![Go Report Card](https://goreportcard.com/badge/github.com/oauth2-proxy/oauth2-proxy)](https://goreportcard.com/report/github.com/oauth2-proxy/oauth2-proxy/v7)
[![GoDoc](https://godoc.org/github.com/oauth2-proxy/oauth2-proxy?status.svg)](https://godoc.org/github.com/oauth2-proxy/oauth2-proxy/v7)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Maintainability](https://qlty.sh/gh/oauth2-proxy/projects/oauth2-proxy/maintainability.svg)](https://qlty.sh/gh/oauth2-proxy/projects/oauth2-proxy)
[![Code Coverage](https://qlty.sh/gh/oauth2-proxy/projects/oauth2-proxy/coverage.svg)](https://qlty.sh/gh/oauth2-proxy/projects/oauth2-proxy)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/oauth2-proxy/oauth2-proxy/badge)](https://scorecard.dev/viewer/?uri=github.com/oauth2-proxy/oauth2-proxy)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/11223/badge)](https://www.bestpractices.dev/projects/11223)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Foauth2-proxy%2Foauth2-proxy.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Foauth2-proxy%2Foauth2-proxy?ref=badge_shield)

![OAuth2 Proxy](docs/static/img/logos/OAuth2_Proxy_horizontal.svg)

OAuth2 Proxy is a flexible, open-source tool that can act as either a standalone reverse proxy or a middleware component integrated into existing reverse proxy or load balancer setups. It provides a simple and secure way to protect your web applications with OAuth2 / OIDC authentication. As a reverse proxy, it intercepts requests to your application and redirects users to an OAuth2 provider for authentication. As a middleware, it can be seamlessly integrated into your existing infrastructure to handle authentication for multiple applications.

OAuth2 Proxy supports a lot of OAuth2 as well as OIDC providers. Either through a generic OIDC client or a specific implementation for Google, Microsoft Entra ID, GitHub, login.gov and others. Through specialised provider implementations oauth2-proxy can extract more details about the user like preferred usernames and groups. Those details can then be forwarded as HTTP headers to your upstream applications.

![Simplified Architecture](docs/static/img/simplified-architecture.svg)

## Get Started

OAuth2 Proxy's [Installation Docs](https://oauth2-proxy.github.io/oauth2-proxy/installation) cover how to install and configure your setup. Additionally you can take a further look at the [example setup files](https://github.com/oauth2-proxy/oauth2-proxy/tree/master/contrib/local-environment).

## Releases

### Binaries
We publish oauth2-proxy as compiled binaries on GitHub for all major architectures as well as more exotic ones like `ppc64le` as well as `s390x`.

Check out the [latest release](https://github.
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

