---
id: xpfarm-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.277270
---

# OmniClaw Knowledge Report: xpfarm

## Tech Stack
Go

## File Statistics
```json
{
  "": 6,
  ".yml": 1,
  ".mod": 1,
  ".sum": 1,
  ".go": 29,
  ".md": 19,
  ".ps1": 1,
  ".sh": 2,
  ".png": 10,
  ".ico": 1,
  ".html": 15,
  ".json": 1,
  ".ts": 29,
  ".yar": 4
}
```

## README Snippet
```markdown
# XPFarm

An open-source vulnerability scanner that wraps well-known open-source security tools behind a single web UI.

![ADB](img/adb.png)
---

### Index

| Section | Description |
|---|---|
| [Why](#why) | Motivation and philosophy behind XPFarm |
| [Wrapped Tools](#wrapped-tools) | The 10 open-source tools orchestrated by XPFarm |
| [Architecture Map](#architecture-map) | Full system architecture, scan pipeline, data flow, and AI subsystem |
| [Overlord - AI Binary Analysis](#overlord---ai-binary-analysis) | Built-in AI agent for binary/malware analysis |
| [Setup](#setup) | Build and deployment instructions (Docker / source) |
| [Random Screenshots](#random-screenshots) | UI screenshots of scans and logs |
| [TODO](#todo) | Planned features and roadmap |

---

![Dashboard](img/dashboard.png)

## Architecture Map

```mermaid
flowchart TB
    subgraph ENTRY["Entrypoint - main.go"]
        M1["Parse Flags<br/>-debug mode"]
        M2["InitDB<br/>SQLite + WAL + GORM"]
        M3["InitModules<br/>Register 10 tool wrappers"]
        M4["Health Check<br/>Auto-install missing tools"]
        M5["RunUpdates<br/>-up flag on all PD tools"]
        M6["CheckAndIndexTemplates<br/>Nuclei template versioning"]
        M7["StartServer<br/>Gin on :8888"]
        M1 --> M2 --> M3 --> M4 --> M5 --> M6 --> M7
    end

    subgraph UI_LAYER["Web UI - internal/ui/server.go"]
        direction TB
        GIN["Gin HTTP Server<br/>Embedded templates + static"]

        subgraph Pages["HTML Pages
```

**Processed by OmniClaw Automated Intake**