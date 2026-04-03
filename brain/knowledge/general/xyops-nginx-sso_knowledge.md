---
id: xyops-nginx-sso-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.408190
---

# OmniClaw Knowledge Report: xyops-nginx-sso

## Tech Stack
Node.js/NPM

## File Statistics
```json
{
  "": 1,
  ".md": 2,
  ".conf": 3,
  ".json": 1,
  ".sh": 1
}
```

## README Snippet
```markdown
# xyOps Multi-Master Nginx TLS/SSO

This repo generates a custom Docker Image designed to be used with [xyOps](https://xyops.io).

This is a wrapper around the official [Nginx Docker Image](https://hub.docker.com/_/nginx), which layers in [Node.js](https://nodejs.org/) and a custom [Health Check Daemon](https://github.com/pixlcore/xyops-healthcheck) for [xyOps](https://xyops.io).  This is for use with xyOps multi-master setups, utilizing TLS, and [OAuth2-Proxy](https://github.com/oauth2-proxy/oauth2-proxy) for SSO integration.  For setup instructions, please see the [xyOps SSO Setup Guide](https://github.com/pixlcore/xyops/blob/main/docs/sso.md).

## Current Versions

- Nginx v1.28
- OAuth2-Proxy v7.12
- Node.js v22
- Health Check v1.0.5

# Usage

## Docker

This repo automatically publishes a Docker image on every tag, which is designed to run with [Nginx](https://nginx.org/) for xyOps mutli-master installs.  For usage instructions, see the [xyOps SSO Setup Guide](https://github.com/pixlcore/xyops/blob/main/docs/sso.md).  The Docker Image name is:

```
ghcr.io/pixlcore/xyops-nginx-sso
```

Example use:

```yaml
services:
  nginx:
    image: ghcr.io/pixlcore/xyops-nginx-sso:latest
    depends_on:
      - oauth2-proxy
    init: true
    environment:
      XYOPS_masters: xyops01.yourcompany.com,xyops02.yourcompany.com
      XYOPS_port: 5522
    volumes:
      - "./tls.crt:/etc/tls.crt:ro"
      - "./tls.key:/etc/tls.key:ro"
    ports:
      - "443:443"
    networks:
      xyops
```

**Processed by OmniClaw Automated Intake**