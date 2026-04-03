---
id: marixdev-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:06.613244
---

# KNOWLEDGE EXTRACT: marixdev
> **Extracted on:** 2026-03-30 17:42:04
> **Source:** marixdev

---

## File: `lstack.md`
```markdown
# 📦 marixdev/lstack [🔖 PENDING/APPROVE]
🔗 https://github.com/marixdev/lstack


## Meta
- **Stars:** ⭐ 11 | **Forks:** 🍴 2
- **Language:** TypeScript | **License:** GPL-3.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Local development stack manager for Windows and Linux

## README (trích đầu)
```
﻿# LStack

> Local development environment for Windows and Linux.  
> A modern, Electron-based alternative to Laragon — manage PHP services, virtual hosts, databases, and projects from a clean GUI.

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)](#installation)
[![Version](https://img.shields.io/badge/version-1.0.0-green)](CHANGELOG.md)

**Homepage:** https://lstack.dev  
**GitHub:** https://github.com/marixdev/lstack

---

## Overview

LStack is a desktop application that manages a full local PHP development stack — web servers, databases, caches, and mail — without any Docker or WSL dependency. Services run as native processes; projects are served over `.test` domains with optional SSL via mkcert.

Built with **Electron 32**, **React 18**, **TypeScript 5**, **Vite 5**, and **Tailwind CSS 3**.

---

## Features

- **One-click service management** — start, stop, and restart every service from the dashboard
- **Virtual hosts** — auto-create `.test` domains (e.g. `myapp.test`) with Nginx or Apache
- **SSL certificates** — trust a local CA with a single click; full HTTPS on every project
- **Per-project PHP profiles** — assign a dedicated PHP-FPM process with isolated `php.ini` settings and extensions per project
- **PHP extension control** — enable/disable extensions per profile; built-in profiles ship pre-configured for Laravel, WordPress, Symfony, and more
- **Project wizard** — scaffold new projects from a template with one click; installs CMS/framework files automatically
- **Framework detection** — automatically detects Laravel, WordPress, Symfony, and CodeIgniter in existing folders
- **phpMyAdmin** — accessible at `phpmyadmin.test` with auto-login (no password required for root)
- **Built-in terminal** — xterm.js-powered full terminal per project, opens directly in the project directory
- **Real-time logs** — tail live service and access logs from the UI
- **Package manager** — download and install service binaries (Nginx, Apache, MariaDB, PHP, Redis, etc.) directly from the app, no system-wide installs needed
- **Auto-updater** — built-in update checker via electron-updater
- **Bilingual UI** — full English and Vietnamese interface, switchable at runtime

---

## Services

| Service       | Default Port(s)         | Notes                                  |
|---------------|-------------------------|----------------------------------------|
| Nginx         | 80 (HTTP), 443 (HTTPS)  | Default web server                     |
| Apache        | 80 (HTTP), 443 (HTTPS)  | Optional alternative                   |
| MariaDB       | 3306                    | MySQL-compatible database              |
| PostgreSQL    | 5432                    | Alternative relational database        |
| PHP-FPM       | 9100–9600 (per profile) | Hash-based port per named profile      |
| Redis         | 6379                    | In-memory cache / m
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

