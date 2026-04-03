---
id: weaviate-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:45.981986
---

# KNOWLEDGE EXTRACT: weaviate
> **Extracted on:** 2026-03-30 18:01:16
> **Source:** weaviate

---

## File: `Verba.md`
```markdown
# 📦 weaviate/Verba [🔖 PENDING/APPROVE]
🔗 https://github.com/weaviate/Verba


## Meta
- **Stars:** ⭐ 7621 | **Forks:** 🍴 840
- **Language:** Python | **License:** BSD-3-Clause
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Retrieval Augmented Generation (RAG) chatbot powered by Weaviate

## README (trích đầu)
```
# Verba

## The Golden RAGtriever - Community Edition ✨

[![Weaviate](https://img.shields.io/static/v1?label=powered%20by&message=Weaviate%20%E2%9D%A4&color=green&style=flat-square)](https://weaviate.io/)
[![PyPi downloads](https://static.pepy.tech/personalized-badge/goldenverba?period=total&units=international_system&left_color=grey&right_color=orange&left_text=pip%20downloads)](https://pypi.org/project/goldenverba/) [![Docker support](https://img.shields.io/badge/Docker_support-%E2%9C%93-4c1?style=flat-square&logo=docker&logoColor=white)](https://docs.docker.com/get-started/) [![Demo](https://img.shields.io/badge/Check%20out%20the%20demo!-yellow?&style=flat-square&logo=react&logoColor=white)](https://verba.weaviate.io/)

Welcome to Verba: The Golden RAGtriever, an community-driven open-source application designed to offer an end-to-end, streamlined, and user-friendly interface for Retrieval-Augmented Generation (RAG) out of the box. In just a few easy steps, explore your datasets and extract insights with ease, either locally with Ollama and Huggingface or through LLM providers such as Anthrophic, Cohere, and OpenAI. This project is built with and for the community, please be aware that it might not be maintained with the same urgency as other Weaviate production applications. Feel free to contribute to the project and help us make Verba even better! <3

```
pip install goldenverba
```

![Demo of Verba](https://github.com/weaviate/Verba/blob/2.0.0/img/verba.gif)

- [Verba](#verba)
  - [🎯 What Is Verba?](#what-is-verba)
  - [✨ Features](#feature-lists)
- [✨ Getting Started with Verba](#getting-started-with-verba)
- [🔑 API Keys](#api-keys)
  - [Weaviate](#weaviate)
  - [Ollama](#ollama)
  - [Unstructured](#unstructured)
  - [AssemblyAI](#assemblyai)
  - [OpenAI](#openai)
  - [HuggingFace](#huggingface)
  - [Groq](#groq)
  - [Novita AI](#novitaai)
- [Quickstart: Deploy with pip](#how-to-deploy-with-pip)
- [Quickstart: Build from Source](#how-to-build-from-source)
- [Quickstart: Deploy with Docker](#how-to-install-verba-with-docker)
- [💾 Verba Walkthrough](#️verba-walkthrough)
- [💖 Open Source Contribution](#open-source-contribution)
- [🚩 Known Issues](#known-issues)
- [❔FAQ](#faq)

## What Is Verba?

Verba is a fully-customizable personal assistant utilizing [Retrieval Augmented Generation (RAG)](https://weaviate.io/rag#:~:text=RAG%20with%20Weaviate,accuracy%20of%20AI%2Dgenerated%20content.) for querying and interacting with your data, **either locally or deployed via cloud**. Resolve questions around your documents, cross-reference multiple data points or gain insights from existing knowledge bases. Verba combines state-of-the-art RAG techniques with Weaviate's context-aware database. Choose between different RAG frameworks, data types, chunking & retrieving techniques, and LLM providers based on your individual use-case.

## Open Source Spirit

**Weaviate** is proud to offer this open-source project for the community. While we strive to address 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `weaviate.md`
```markdown
# 📦 weaviate/weaviate [🔖 PENDING/APPROVE]
🔗 https://github.com/weaviate/weaviate
🌐 https://weaviate.io/developers/weaviate/

## Meta
- **Stars:** ⭐ 15893 | **Forks:** 🍴 1233
- **Language:** Go | **License:** BSD-3-Clause
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Weaviate is an open-source vector database that stores both objects and vectors, allowing for the combination of vector search with structured filtering with the fault tolerance and scalability of a cloud-native database​.

## README (trích đầu)
```
# Weaviate <img alt='Weaviate logo' src='https://weaviate.io/img/site/weaviate-logo-light.png' width='148' align='right' />

[![GitHub Repo stars](https://img.shields.io/github/stars/weaviate/weaviate?style=social)](https://github.com/weaviate/weaviate)
[![Go Reference](https://pkg.go.dev/badge/github.com/weaviate/weaviate.svg)](https://pkg.go.dev/github.com/weaviate/weaviate)
[![Build Status](https://github.com/weaviate/weaviate/actions/workflows/.github/workflows/pull_requests.yaml/badge.svg?branch=main)](https://github.com/weaviate/weaviate/actions/workflows/.github/workflows/pull_requests.yaml)
[![Go Report Card](https://goreportcard.com/badge/github.com/weaviate/weaviate)](https://goreportcard.com/report/github.com/weaviate/weaviate)
[![Coverage Status](https://codecov.io/gh/weaviate/weaviate/branch/main/graph/badge.svg)](https://codecov.io/gh/weaviate/weaviate)

**Weaviate** is an open-source, cloud-native vector database that stores both objects and vectors, enabling semantic search at scale. It combines vector similarity search with keyword filtering, retrieval-augmented generation (RAG), and reranking in a single query interface. Common use cases include RAG systems, semantic and image search, recommendation engines, chatbots, and content classification.

Weaviate supports two approaches to store vectors: automatic vectorization at import using [integrated models](https://docs.weaviate.io/weaviate/model-providers) (OpenAI, Cohere, HuggingFace, and others) or direct import of [pre-computed vector embeddings](https://docs.weaviate.io/weaviate/starter-guides/custom-vectors). Production deployments benefit from built-in multi-tenancy, replication, RBAC authorization, and [many other features](#weaviate-features).

To get started quickly, have a look at one of these tutorials:

- [Quickstart - Weaviate Cloud](https://docs.weaviate.io/weaviate/quickstart)
- [Quickstart - local Docker instance](https://docs.weaviate.io/weaviate/quickstart/local)

## Installation

Weaviate offers multiple installation and deployment options:

- [Docker](https://docs.weaviate.io/deploy/installation-guides/docker-installation)
- [Kubernetes](https://docs.weaviate.io/deploy/installation-guides/k8s-installation)
- [Weaviate Cloud](https://console.weaviate.cloud)

See the [installation docs](https://docs.weaviate.io/deploy) for more deployment options, such as [AWS](https://docs.weaviate.io/deploy/installation-guides/aws-marketplace) and [GCP](https://docs.weaviate.io/deploy/installation-guides/gcp-marketplace).

## Getting started

You can easily start Weaviate and a local vector embedding model with [Docker](https://docs.docker.com/desktop/).
Create a `docker-compose.yml` file:

```yml
services:
  weaviate:
    image: cr.weaviate.io/semitechnologies/weaviate:1.36.0
    ports:
      - "8080:8080"
      - "50051:50051"
    environment:
      ENABLE_MODULES: text2vec-model2vec
      MODEL2VEC_INFERENCE_API: http://text2vec-model2vec:8080

  # A lightweight embedding m
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

