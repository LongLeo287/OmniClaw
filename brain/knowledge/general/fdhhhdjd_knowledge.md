---
id: fdhhhdjd-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:23.914857
---

# KNOWLEDGE EXTRACT: fdhhhdjd
> **Extracted on:** 2026-03-30 17:36:59
> **Source:** fdhhhdjd

---

## File: `class-prometheus-grafana-telegram-alerts.md`
```markdown
# 📦 fdhhhdjd/class-prometheus-grafana-telegram-alerts [🔖 PENDING/APPROVE]
🔗 https://github.com/fdhhhdjd/class-prometheus-grafana-telegram-alerts


## Meta
- **Stars:** ⭐ 29 | **Forks:** 🍴 17
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🚨 This project is a complete, containerized monitoring environment designed to simulate real-world application metrics, visualize them, and automatically send alerts to a Telegram chat.

## README (trích đầu)
```
<div align="center">

# 📊 Telegram Alerts Monitoring Stack
**class-prometheus-grafana-telegram-alerts**

[![Node.js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/)
[![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)](https://grafana.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://telegram.org/)

*A complete, containerized monitoring environment designed to simulate real-world application metrics, visualize them, and automatically send alerts to a Telegram chat.*

![Demo](./assets/demo.gif)

</div>

---

## 🚀 Architecture Overview

![Monitoring Architecture](./assets/architecture.png)

Our stack is built on four core pillars:

1. 🟢 **Node.js App (Port `8081`)**  
   A minimal Express backend using `prom-client` to expose metrics. Includes a dedicated `/simulate-error` endpoint to manually trigger issue scenarios for testing.
2. 🔥 **Prometheus (Port `9090`)**  
   A powerful time-series database configured to continuously scrape metrics exposed by the Node.js application and cAdvisor.
3. 🐳 **cAdvisor (Port `8082`)**  
   Exposes real, system-level CPU and Memory metrics for the Docker containers, providing true resource consumption data.
4. 📈 **Grafana (Port `4000`)**  
   The visualization and alerting engine, completely pre-provisioned via code:
   - **Data Source:** Pre-linked to Prometheus.
   - **Custom Dashboard:** Live tracking of errors, error rates, real container CPU/RAM usage, and HTTP response times (p95 & p50).
   - **Alerting:** Pre-configured Notification Policies & Contact Points pointing directly to a custom Telegram channel.
   - **Smart Rules:** Instantly triggers notifications when the Node.js error counter spikes.

---

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 🛠️ How to Run Locally

**1. Clone the repository** (or navigate to this environment folder):
```bash
git clone git@github.com:fdhhhdjd/class-prometheus-grafana-telegram-alerts.git
cd class-prometheus-grafana-telegram-alerts
```

**2. Start the monitoring stack** in detached mode:
```bash
docker compose up -d
```

> **Note:** Wait a few moments for the containers to fully start and for Grafana to provision its plugins and modules.

---

## 🔍 Accessing the Services

Once the stack is up and running, you can access the following interfaces:

| Service | Local URL | Network IP | Default Credentials |
| :--- | :--- | :--- | :--- |
| **Node.js App** |
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

