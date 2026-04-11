# 🌉 The Harbor Layer (Bridges)

> **Execution Zone for Local Databases & Containerized Subservices**

This directory contains the launch points, Docker Compose maps, and Port configurations for all heavily containerized entities required by OmniClaw. 

The `bridges` act as the safe harbor. Untrusted downloaded 3rd-party repositories (like Mem0 or Firecrawl from `plugins/`) are loaded here as immutable Docker images and spun up securely on mapped ports.

## Active Bridges
This directory currently hosts the central `docker-compose.yml` driving the persistent backend services:
* **Mem0 Core** (Port 7000)
* **Qdrant Vector DB** (Ports 6333, 6334)
* **Firecrawl API** (Port 3002)
* **Redis Cache** (Port 6379)

## Operating Instructions
To spin up all backend containers, execute standard Docker procedures **from within this directory**:
```bash
docker-compose up -d
```
> [!WARNING]
> Do not move `docker-compose.yml` to the root `C:/.../OmniClaw/` directory. The volume mounts are strictly configured to tunnel back `../../` into the secure `vault/vectors/` cache.

## Bridge Rules
- Bridges must launch real services or fail fast. They must not bind fake sockets just to appear healthy.
- Dependency installation and workspace bootstrap belong in explicit repair/setup flows, not normal runtime startup.
- A bridge should stay attached to the real child process, or supervise it explicitly, so Harbor health reflects reality.
