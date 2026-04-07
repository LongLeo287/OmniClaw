---
id: class-prometheus-grafana-telegram-alerts
type: knowledge
owner: OA_Triage
---
# class-prometheus-grafana-telegram-alerts
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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
| **Node.js App** | [http://localhost:8081](http://localhost:8081) | `http://<ip>:8081` | - |
| **Prometheus** | [http://localhost:9090](http://localhost:9090) | `http://<ip>:9090` | - |
| **Grafana** | [http://localhost:4000/dashboards](http://localhost:4000/dashboards) | `http://<ip>:4000/dashboards` | `admin` / `admin` |

---

## 🚨 How to Test Telegram Alerts

The stack comes fully prepared with your Telegram Bot credentials and Channel ID. Here's how to trigger an alert:

1. **Open Grafana:** Go to the [Node.js Application Dashboard](http://localhost:4000/dashboards) in your browser.
2. **Trigger an Error:** In a new tab, purposefully trigger a backend error by visiting the `/simulate-error` endpoint:
   ```text
   http://localhost:8081/simulate-error
   ```
3. **Spike the Counter:** Refresh the simulation page multiple times to simulate a surge in errors.
4. **Test Latency (Optional):** Open another tab and hit the `/slow` endpoint to test HTTP response times:
   ```text
   http://localhost:8081/slow
   ```
5. **Watch the Metrics:** Return to the Grafana dashboard. Within **10 to 30 seconds**, you will observe the graphs spiking.
6. **Check Telegram:** Grafana will automatically evaluate the threshold rule, mark it as `Firing`, and dispatch an HTML-formatted alert securely via your bot to the Telegram chat! 📲

```

