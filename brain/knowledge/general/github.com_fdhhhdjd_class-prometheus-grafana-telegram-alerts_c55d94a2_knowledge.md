---
id: github.com-fdhhhdjd-class-prometheus-grafana-teleg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:49.684456
---

# KNOWLEDGE EXTRACT: github.com_fdhhhdjd_class-prometheus-grafana-telegram-alerts_c55d94a2
> **Extracted on:** 2026-04-01 14:34:20
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007523980/github.com_fdhhhdjd_class-prometheus-grafana-telegram-alerts_c55d94a2

---

## File: `README.md`
```markdown
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

## File: `docker-compose.yml`
```yaml
version: '3.8'

services:
  app:
    build: ./app
    container_name: demo_node_app
    ports:
      - "8081:8081"
    restart: always

  prometheus:
    image: prom/prometheus:latest
    container_name: demo_prometheus
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
    ports:
      - "9090:9090"
    restart: always

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:v0.47.0
    container_name: demo_cadvisor
    privileged: true
    ports:
      - "8082:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
      - /dev/disk/:/dev/disk:ro
    devices:
      - /dev/kmsg
    restart: always

  grafana:
    image: grafana/grafana:latest
    container_name: demo_grafana
    ports:
      - "4000:3000"
    volumes:
      - ./grafana/provisioning:/etc/grafana/provisioning
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    depends_on:
      - prometheus
    restart: always
```

## File: `app/Dockerfile`
```
FROM node:18-alpine
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 8081
CMD [ "npm", "start" ]
```

## File: `app/index.js`
```javascript
const express = require('express');
const client = require('prom-client');
const app = express();
const port = 8081;

// Enable default metrics collection
const collectDefaultMetrics = client.collectDefaultMetrics;
collectDefaultMetrics({ prefix: 'node_app_' });

// Custom metric for simulated errors
const errorCounter = new client.Counter({
  name: 'node_app_simulated_errors_total',
  help: 'Total number of simulated errors'
});

// Custom metric for response time
const httpRequestDurationSeconds = new client.Histogram({
  name: 'node_app_http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status_code'],
  buckets: [0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
});

// Middleware to track response time
app.use((req, res, next) => {
  if (req.path === '/metrics') {
    return next();
  }
  const end = httpRequestDurationSeconds.startTimer();
  res.on('finish', () => {
    end({ route: req.path, status_code: res.statusCode, method: req.method });
  });
  next();
});

app.get('/', (req, res) => {
  res.send('<h1>Simulated App for Monitoring</h1><p>Visit <a href="/metrics">/metrics</a> to see Prometheus metrics.</p><p>Visit <a href="/simulate-error">/simulate-error</a> to increment the error counter.</p><p>Visit <a href="/slow">/slow</a> to test response time latency.</p>');
});

app.get('/slow', async (req, res) => {
  const delay = Math.floor(Math.random() * 2000) + 1000; // 1s to 3s delay
  await new Promise(resolve => setTimeout(resolve, delay));
  res.send(`Slow response simulated! Took ${delay}ms`);
});

app.get('/simulate-error', (req, res) => {
  errorCounter.inc();
  console.log('Simulated an error! Counter incremented.');
  res.status(500).send('Simulated Error Occurred! This will trigger the Grafana alert if configured.');
});

// Metrics endpoint for Prometheus
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', client.register.contentType);
  res.end(await client.register.metrics());
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

## File: `app/package.json`
```json
{
  "name": "simulated-app",
  "version": "1.0.0",
  "description": "Simulated app for monitoring",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "prom-client": "^14.2.0"
  }
}
```

## File: `grafana/provisioning/alerting/contact_points.yaml`
```yaml
apiVersion: 1

contactPoints:
  - orgId: 1
    name: 'Telegram Alerts'
    receivers:
      - uid: telegram_1
        type: telegram
        settings:
          bottoken: '<bottoken>'
          chatid: '<chatid>'
          parse_mode: 'HTML'
          message: |
            <b>{{ len .Alerts.Firing }} alerts are {{ .Status }}!</b>
            
            {{ range .Alerts }}
            🚨 <b>{{ .Labels.alertname }}</b> 🚨
            <b>Severity:</b> {{ .Labels.severity }}
            <b>Details:</b> {{ .Annotations.description }}
            {{ end }}
            
            📉 <a href="http://<ip>:4000/dashboards">View your Grafana Dashboard</a>
```

## File: `grafana/provisioning/alerting/policies.yaml`
```yaml
apiVersion: 1

policies:
  - orgId: 1
    receiver: 'Telegram Alerts'
    group_by: ['grafana_folder', 'alertname']
```

## File: `grafana/provisioning/alerting/rules.yaml`
```yaml
apiVersion: 1

groups:
  - orgId: 1
    name: NodeAppErrors
    folder: DemoMonitoring
    interval: 10s
    rules:
      - uid: simulated_error_rule
        title: Node.js App Error Spike
        condition: C
        data:
          - refId: A
            relativeTimeRange:
              from: 600
              to: 0
            datasourceUid: my_prometheus
            model:
              expr: increase(node_app_simulated_errors_total[1m])
              intervalMs: 1000
              maxDataPoints: 43200
              refId: A
          - refId: B
            relativeTimeRange:
              from: 600
              to: 0
            datasourceUid: __expr__
            model:
              conditions:
                - evaluator:
                    params:
                      - 0
                    type: gt
                  operator:
                    type: and
                  query:
                    params:
                      - B
                  reducer:
                    params: []
                    type: last
                  type: query
              datasource:
                name: Expression
                type: __expr__
                uid: __expr__
              expression: A
              intervalMs: 1000
              maxDataPoints: 43200
              reducer: last
              refId: B
              type: reduce
          - refId: C
            relativeTimeRange:
              from: 600
              to: 0
            datasourceUid: __expr__
            model:
              datasource:
                name: Expression
                type: __expr__
                uid: __expr__
              expression: $B > 0
              intervalMs: 1000
              maxDataPoints: 43200
              refId: C
              type: math
        noDataState: NoData
        execErrState: Error
        for: 0s
        annotations:
          summary: "Simulated errors detected in the Node.js application."
          description: "The error counter has increased in the last minute."
        labels:
          severity: warning
```

## File: `grafana/provisioning/dashboards/dashboard_provider.yml`
```yaml
apiVersion: 1

providers:
  - name: 'Default'
    orgId: 1
    folder: ''
    type: file
    disableDeletion: false
    updateIntervalSeconds: 10
    options:
      path: /etc/grafana/provisioning/dashboards
```

## File: `grafana/provisioning/dashboards/nodejs_dashboard.json`
```json
{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "grafana",
          "uid": "-- Grafana --"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "target": {
          "limit": 100,
          "matchAny": false,
          "tags": [],
          "type": "dashboard"
        },
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": 1,
  "links": [],
  "liveNow": false,
  "panels": [
    {
      "datasource": {
        "type": "prometheus",
        "uid": "my_prometheus"
      },
      "gridPos": {
        "h": 7,
        "w": 8,
        "x": 0,
        "y": 0
      },
      "id": 1,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "my_prometheus"
          },
          "editorMode": "code",
          "expr": "node_app_simulated_errors_total",
          "legendFormat": "Errors",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Simulated Errors Total",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "my_prometheus"
      },
      "gridPos": {
        "h": 7,
        "w": 8,
        "x": 8,
        "y": 0
      },
      "id": 2,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "my_prometheus"
          },
          "editorMode": "code",
          "expr": "rate(node_app_simulated_errors_total[1m])",
          "legendFormat": "Errors /sec",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Simulated Error Rate (1m)",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "my_prometheus"
      },
      "gridPos": {
        "h": 7,
        "w": 8,
        "x": 16,
        "y": 0
      },
      "id": 5,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "my_prometheus"
          },
          "editorMode": "code",
          "expr": "histogram_quantile(0.95, sum(rate(node_app_http_request_duration_seconds_bucket[1m])) by (le))",
          "legendFormat": "p95",
          "range": true,
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "my_prometheus"
          },
          "editorMode": "code",
          "expr": "histogram_quantile(0.50, sum(rate(node_app_http_request_duration_seconds_bucket[1m])) by (le))",
          "legendFormat": "p50",
          "range": true,
          "refId": "B"
        }
      ],
      "title": "HTTP Response Time (seconds)",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "my_prometheus"
      },
      "gridPos": {
        "h": 7,
        "w": 12,
        "x": 0,
        "y": 7
      },
      "id": 6,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "my_prometheus"
          },
          "editorMode": "code",
          "expr": "rate(container_cpu_usage_seconds_total{name=\"demo_node_app\"}[1m])",
          "legendFormat": "Real CPU Cores",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Container CPU Usage (cAdvisor)",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "my_prometheus"
      },
      "gridPos": {
        "h": 7,
        "w": 12,
        "x": 12,
        "y": 7
      },
      "id": 7,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "my_prometheus"
          },
          "editorMode": "code",
          "expr": "container_memory_usage_bytes{name=\"demo_node_app\"}",
          "legendFormat": "Real Memory Bytes",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Container Memory Usage (cAdvisor)",
      "type": "timeseries"
    }
  ],
  "refresh": "5s",
  "schemaVersion": 38,
  "style": "dark",
  "tags": [],
  "templating": {
    "list": []
  },
  "time": {
    "from": "now-15m",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "",
  "title": "Node.js Application Dashboard",
  "uid": "nodejs-demo",
  "version": 2,
  "weekStart": ""
}
```

## File: `grafana/provisioning/datasources/datasource.yml`
```yaml
apiVersion: 1

datasources:
  - name: Prometheus
    uid: my_prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090
    isDefault: true
    editable: false
```

## File: `prometheus/prometheus.yml`
```yaml
global:
  scrape_interval: 5s
  evaluation_interval: 5s

scrape_configs:
  - job_name: 'node-app'
    static_configs:
      - targets: ['app:8081']

  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']
```

