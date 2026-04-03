---
id: ahoo-wang-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:42.182586
---

# KNOWLEDGE EXTRACT: Ahoo-Wang
> **Extracted on:** 2026-03-30 17:29:05
> **Source:** Ahoo-Wang

---

## File: `Wow.md`
```markdown
# 📦 Ahoo-Wang/Wow [🔖 PENDING/APPROVE]
🔗 https://github.com/Ahoo-Wang/Wow
🌐 https://wow.ahoo.me/

## Meta
- **Stars:** ⭐ 283 | **Forks:** 🍴 39
- **Language:** Kotlin | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Modern Reactive CQRS Architecture Microservice development framework based on DDD and EventSourcing | 基于 DDD & EventSourcing 的现代响应式 CQRS 架构微服务开发框架

## README (trích đầu)
```
<p align="center" style="text-align:center;">
  <img width="150" src="document/design/assets/logo.svg" alt="Wow:A Modern Reactive CQRS Architecture Microservice development framework based on DDD and EventSourcing"/>
</p>

# Wow : Modern Reactive CQRS Architecture Microservice development framework based on DDD and EventSourcing

[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://github.com/Ahoo-Wang/Wow/blob/main/LICENSE)
[![GitHub release](https://img.shields.io/github/release/Ahoo-Wang/Wow.svg)](https://github.com/Ahoo-Wang/Wow/releases)
[![Maven Central Version](https://img.shields.io/maven-central/v/me.ahoo.wow/wow-core)](https://central.sonatype.com/artifact/me.ahoo.wow/wow-core)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/cfc724df22db4f9387525258c8a59609)](https://app.codacy.com/gh/Ahoo-Wang/Wow/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![codecov](https://codecov.io/gh/Ahoo-Wang/Wow/branch/main/graph/badge.svg?token=uloJrLoQir)](https://codecov.io/gh/Ahoo-Wang/Wow)
[![Integration Test Status](https://github.com/Ahoo-Wang/Wow/actions/workflows/integration-test.yml/badge.svg)](https://github.com/Ahoo-Wang/Wow)
[![Awesome Kotlin Badge](https://kotlin.link/awesome-kotlin.svg)](https://github.com/KotlinBy/awesome-kotlin)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/Ahoo-Wang/Wow)

**Domain-Driven** | **Event-Driven** | **Test-Driven** | **Declarative-Design** | **Reactive Programming** | **Command Query Responsibility Segregation** | **Event Sourcing**

> [中文文档](https://wow.ahoo.me/zh/) | [English Document](https://wow.ahoo.me/)

## Spring Boot Version Compatibility

> **Wow 6.x** supports Spring Boot 3.x , base Java 17
>
> **Wow 8.x** supports Spring Boot 4.x , base Java 17

## Quick Start

Use [Wow Project Template](https://github.com/Ahoo-Wang/wow-project-template) to quickly create a DDD project based on the Wow framework.

## Features Overview

<p align="center" style="text-align:center">
  <img src="documentation/brain/knowledge/docs_legacy/public/images/Features.png" alt="Wow-Features"/>
</p>

## Architecture

<p align="center" style="text-align:center">
  <img width="95%" src="documentation/brain/knowledge/docs_legacy/public/images/Architecture.svg" alt="Wow-Architecture"/>
</p>

### Command Processing Propagation Chain

<p align="center" style="text-align:center;">
  <img  width="95%" src="documentation/brain/knowledge/docs_legacy/public/images/wait/WaitingForChain.svg" alt="Wow-WaitingForChain"/>
</p>

## Performance Test (Example)

- Test Code: [Example](./example)
- Test Case: Add To Shopping Cart / Create Order
- Command `WaitStrategy`: `SENT`、`PROCESSED`

### Deployment

- [Redis](deploy/example/perf/redis.yaml)
- [MongoDB](deploy/example/perf/mongo.yaml)
- [Kafka](deploy/example/perf/kafka.yaml)
- [Application-Config](deploy/example/perf/config/mongo_kafka_redis.yaml)
- [Application-Deployment](deploy/example/perf/deployment.yaml)

### Test Report

#### Add To Shopping Cart

- [Request
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

