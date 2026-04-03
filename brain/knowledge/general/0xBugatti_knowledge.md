---
id: 0xbugatti-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:37.774732
---

# KNOWLEDGE EXTRACT: 0xBugatti
> **Extracted on:** 2026-03-30 17:28:59
> **Source:** 0xBugatti

---

## File: `PentestOPS.md`
```markdown
# 📦 0xBugatti/PentestOPS [🔖 PENDING/APPROVE]
🔗 https://github.com/0xBugatti/PentestOPS


## Meta
- **Stars:** ⭐ 305 | **Forks:** 🍴 54
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A comprehensive penetration testing operations dashboard for managing projects, tasks, findings, clients, and assets. Built with Next.js, Express, and MongoDB.

## README (trích đầu)
```
# PentesterOPS Dashboard

A comprehensive penetration testing operations dashboard for managing projects, tasks, findings, clients, and assets. Built with Next.js, Express, and MongoDB.

![PentesterOPS](https://img.shields.io/badge/PentesterOPS-Dashboard-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![](Pentest.png)
## 🚀 Features

- **Project Management**: Organize penetration testing projects with tasks, pages, and team collaboration
- **Task Management**: Kanban board, table, and card views with filtering, search, and subtasks
- **Finding Management**: Track security findings with CWE database integration
- **Client Management**: Manage clients with photos, links, and metadata
- **Asset Management**: Track and manage assets linked to projects and tasks
- **Rich Text Editor**: Notion-like pages with Editor.js (headings, paragraphs, code, tables, callouts, toggles)
- **Checklists**: Create reusable checklists and link them to tasks
- **Comments**: Threaded comments on tasks and findings
- **File Attachments**: Upload PDFs, DOCX, XLSX, CSV, ZIP, and images
- **Version History**: Track changes with diff viewing and restore
- **Global Search**: Full-text search across all entities
- **Dark Mode**: Optimized dark theme for technical workflows
- **Single Container Deployment**: Easy deployment with Docker

## 📋 Table of Contents

- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Development](#development)
- [Docker Deployment](#docker-deployment)
- [VPS Deployment](#vps-deployment)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)

## 🛠 Tech Stack

- **Frontend**: Next.js 14 (App Router), React, TypeScript, TailwindCSS
- **Backend**: Node.js, Express, TypeScript
- **Database**: MongoDB with Mongoose
- **Authentication**: JWT with refresh tokens
- **Rich Text Editor**: Editor.js with multiple plugins
- **File Storage**: Local filesystem with multer
- **Containerization**: Docker (single container)

## 📦 Prerequisites

- **Node.js**: 18+ 
- **Docker**: Latest version (for containerized deployment)
- **MongoDB**: 5.0+ (or use MongoDB Atlas)
- **Git**: For cloning the repository

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/MyPentest-Dashboard.git
   cd MyPentest-Dashboard
   ```

2. **Install dependencies**
   ```bash
   # Install root dependencies
   npm install
   
   # Install frontend dependencies
   cd frontend && npm install && cd ..
   
   # Install backend dependencies
   cd backend && npm install && cd ..
   ```

3. **Configure environment variables**
   
   Create `.env` file in the root directory:
   ```env
   # Backend
   NODE_ENV=development
   BACKEND_PORT=4000
   MONGODB_URI=mongodb://localhost:27017/pentest-dashboard
   JWT_SECRET=your-jwt-secret-key
   JWT_REFRESH_SECRET=your-refresh-secret-k
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

