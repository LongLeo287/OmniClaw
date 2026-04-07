---
id: lstack
type: knowledge
owner: OA_Triage
---
# lstack
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "lstack",
  "version": "1.0.0",
  "description": "Local development environment for Windows and Linux",
  "main": "dist-electron/main.js",
  "scripts": {
    "dev": "vite",
    "start": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "dist": "vite build && electron-builder",
    "dist:win": "vite build && electron-builder --win",
    "dist:linux": "vite build && electron-builder --linux",
    "lint": "eslint --ext .ts,.tsx src electron"
  },
  "keywords": [
    "lstack",
    "local-dev",
    "electron",
    "php",
    "nginx"
  ],
  "author": "LStack",
  "license": "GPL-3.0",
  "homepage": "https://lstack.dev",
  "repository": {
    "type": "git",
    "url": "https://github.com/marixdev/lstack.git"
  },
  "devDependencies": {
    "@types/fs-extra": "^11.0.4",
    "@types/node": "^20.0.0",
    "@types/react": "^18.3.0",
    "@types/react-dom": "^18.3.0",
    "@vitejs/plugin-react": "^4.3.0",
    "autoprefixer": "^10.4.19",
    "electron": "^32.0.0",
    "electron-builder": "^24.13.0",
    "postcss": "^8.4.38",
    "tailwindcss": "^3.4.3",
    "typescript": "^5.4.0",
    "vite": "^5.2.0",
    "vite-plugin-electron": "^0.28.0",
    "vite-plugin-electron-renderer": "^0.14.0"
  },
  "dependencies": {
    "@xterm/addon-fit": "^0.11.0",
    "@xterm/xterm": "^6.0.0",
    "axios": "^1.7.0",
    "chokidar": "^3.6.0",
    "electron-updater": "^6.1.0",
    "extract-zip": "^2.0.1",
    "fs-extra": "^11.2.0",
    "lucide-react": "^0.400.0",
    "node-pty": "^1.1.0",
    "react": "^18.3.0",
    "react-dom": "^18.3.0",
    "react-router-dom": "^6.23.0",
    "zustand": "^4.5.0"
  }
}

```

### File: README.md
```md
# LStack

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
| Redis         | 6379                    | In-memory cache / message broker       |
| Memcached     | 11211                   | Lightweight memory cache               |
| Mailpit       | 1025 (SMTP), 8025 (UI)  | Local mail catcher; web UI at :8025    |
| MongoDB       | 27017                   | Document database (optional package)   |

---

## PHP Profiles

Each PHP-FPM profile runs as a separate process with its own port and `php.ini` overrides. Projects can be assigned any profile; multiple projects can share the same profile.

| Profile        | Memory  | Max Execution | Key Extensions                                              |
|----------------|---------|---------------|-------------------------------------------------------------|
| **Minimal**    | 256 MB  | 60 s          | curl, mbstring, openssl, pdo_mysql, zip                     |
| **WordPress**  | 512 MB  | 300 s         | + gd, mysqli, exif, fileinfo                                |
| **Laravel**    | 512 MB  | 120 s         | + gd, intl, pdo_sqlite, sodium                              |
| **Symfony**    | 512 MB  | 120 s         | + intl, xml, pdo_sqlite                                     |
| **CodeIgniter**| 256 MB  | 120 s         | + intl, mysqli                                              |
| **Full Stack** | 1024 MB | 300 s         | + gd, soap, sodium, xsl, exif, intl, and more               |
| **Custom**     | any     | any           | Create your own with any combination of settings            |

---

## Project Templates

When creating a new project, LStack can scaffold one of the following:

| Template     | Versions supported                          |
|--------------|---------------------------------------------|
| Blank PHP    | — (empty `index.php`)                       |
| Laravel      | 12, 11, 10, 9, 8                            |
| WordPress    | latest, 6.8, 6.7, 6.6, 6.5, 6.4, 5.9       |
| Symfony      | 7.3, 7.2, 6.4, 5.4                          |
| CodeIgniter  | 4.5, 4.4, 4.3, 3.1                          |
| Drupal       | 11, 10                                      |
| Joomla       | 5, 4                                        |
| PrestaShop   | 8, 1.7                                      |

---

## Special Domains

| Domain             | Purpose                                |
|--------------------|----------------------------------------|
| `localhost.test`   | LStack dashboard / welcome page        |
| `phpmyadmin.test`  | phpMyAdmin (auto-login as root)        |

Both entries are automatically added to the system `hosts` file on first launch.

---

## Installation

### Pre-built binaries

Download the latest release from the [Releases page](https://github.com/marixdev/lstack/releases) or from [lstack.dev](https://lstack.dev):

| Platform    | Installer                       |
|-------------|---------------------------------|
| Windows x64 | `LStack Setup 1.0.0.exe`        |
| Linux x64   | `LStack-1.0.0.AppImage`         |
| Linux x64   | `lstack_1.0.0_amd64.deb`        |
| Linux x64   | `lstack-1.0.0.x86_64.rpm`       |

**Windows** — run the NSIS installer and launch LStack from the Start Menu.

**Linux (AppImage):**

```bash
chmod +x LStack-1.0.0.AppImage
./LStack-1.0.0.AppImage
```

**Linux (.deb):**

```bash
sudo dpkg -i lstack_1.0.0_amd64.deb
lstack
```

**Linux (.rpm):**

```bash
sudo rpm -i lstack-1.0.0.x86_64.rpm
lstack
```

---

## Building from Source

### Prerequisites

- Node.js 20+
- npm 9+
- Git

### Steps

```bash
git clone https://github.com/marixdev/lstack.git
cd lstack
npm install
```

**Development (hot reload):**

```bash
npm run dev
```

**Production build:**

```bash
# Windows
npm run dist:win

# Linux (run on Linux or WSL)
npm run dist:linux
```

Output is placed in the `release/` directory.

---

## Data Directory

LStack stores all configuration, service data, certificates, and downloaded binaries under:

```
~/.lstack/
├── nginx/             # Nginx config & virtual hosts
├── apache/            # Apache config & virtual hosts
├── mariadb/           # MariaDB data files
├── postgresql/        # PostgreSQL data files
├── redis/             # Redis config & persistence
├── certs/             # mkcert CA and per-domain certificates
├── bins/              # Downloaded service binaries
├── php-profiles.json  # Custom PHP profiles
└── settings.json      # App settings
```

All data is self-contained — uninstalling LStack does not touch your databases or configuration unless you delete this directory manually.

---

## Settings

Configurable from the Settings page:

| Setting              | Description                                              |
|----------------------|----------------------------------------------------------|
| Projects directory   | Root folder scanned for projects (default: `~/LStack/www/`) |
| Web server           | Nginx or Apache                                          |
| PHP version          | Default PHP version for new profiles                     |
| SSL provider         | mkcert; install and trust the local CA from the UI       |
| Language             | English or Vietnamese                                    |
| Auto-start services  | Optionally start all enabled services on launch          |

---

## License

[GPL-3.0](LICENSE) © LStack — https://lstack.dev


```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to LStack are documented in this file.  
Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) · Versioning: [Semantic Versioning](https://semver.org/)

Vietnamese version: [CHANGELOG.vi.md](CHANGELOG.vi.md)

---

## [1.0.0] - 2026-03-23

First stable release of LStack.

### Added

#### Application
- Desktop application built with **Electron 32**, **React 18**, **TypeScript 5**, **Vite 5**, and **Tailwind CSS 3**
- Bilingual interface — **English** and **Vietnamese** switchable at runtime via i18n system
- System tray support with quick service controls
- Auto-updater powered by `electron-updater`
- Custom frameless title bar with window controls
- Light-on-dark UI with Tailwind CSS and Lucide icons

#### Service Management
- One-click **start / stop / restart** for every managed service
- Real-time service status badges (running, stopped, starting, stopping, error)
- Services: **Nginx**, **Apache**, **MariaDB**, **PostgreSQL**, **PHP-FPM**, **Redis**, **Memcached**, **Mailpit**, **MongoDB**
- Auto-start services on app launch (configurable per service)
- Service port display and PID tracking in the dashboard
- Real-time service log viewer (tail stdout/stderr from the UI)

#### Virtual Hosts & Projects
- Automatic `.test` domain creation when a folder is added to the projects directory
- Support for both **Nginx** and **Apache** as the web server per project
- Virtual host config auto-generated and reloaded on project add/remove
- SSL virtual host blocks generated alongside HTTP blocks
- Project list with framework detection: **Laravel**, **WordPress**, **Symfony**, **CodeIgniter**
- Project metadata: git presence, `composer.json` presence, `package.json` presence
- Grid and list view modes for the project browser
- Project search / filter by name
- Context menu per project: open in browser, open folder, open terminal, delete vhost

#### SSL / HTTPS
- Local CA management via **mkcert**
- One-click CA trust installation from the Settings page
- Per-project SSL certificate generation (`*.test` domain signed by local CA)
- SSL trust status indicator per certificate and system-level trust check on Linux

#### PHP-FPM Profiles
- Per-project PHP-FPM: each profile runs as an **isolated process** with a hash-based port (range 9100–9600)
- Six **built-in profiles**: Minimal, WordPress, Laravel, Symfony, CodeIgniter, Full Stack
- **Custom profiles**: create, edit, and delete user-defined profiles with arbitrary `php.ini` overrides and extension lists
- PHP settings per profile: `memory_limit`, `max_execution_time`, `max_input_time`, `max_input_vars`, `upload_max_filesize`, `post_max_size`, `display_errors`, `date.timezone`
- Extension list per profile: enable/disable any PHP extension
- **Auto-profile detection** when opening an existing project (detects `artisan`, `wp-config.php`, `symfony.lock`, `spark`)
- Profile assignment shown and editable from the project card

#### Special Domains
- `localhost.test` — LStack dashboard / PHP info welcome page served by the `minimal` PHP-FPM profile
- `phpmyadmin.test` — phpMyAdmin served automatically; root auto-login with no password required
- Both entries added to the system `hosts` file automatically on first launch

#### Project Wizard (Templates)
- In-app project creation wizard with template selection and version picker
- Supported templates: **Blank PHP**, **Laravel** (8–12), **WordPress** (5.9–6.8/latest), **Symfony** (5.4–7.3), **CodeIgniter** (3.1–4.5), **Drupal** (10–11), **Joomla** (4–5), **PrestaShop** (1.7–8)
- Downloads and installs framework files automatically via Composer / direct archive
- Install progress shown in the in-app terminal panel

#### Package Manager
- Browse, download, and install service binaries from within the app — no system package manager needed
- Packages: Nginx, Apache, MariaDB, PHP (multiple versions), phpMyAdmin, Redis, Mailpit, PostgreSQL, MongoDB, Memcached
- Package registry loaded from a bundled `package-registry.json` with per-platform download URLs
- Installation state persisted; binary paths injected into service configs automatically
- Download progress bar with bytes transferred and percentage
- Installation log streamed to the in-app terminal

#### Terminal
- Full **xterm.js** terminal per project (node-pty backend)
- Terminal opens pre-`cd`'d to the project directory
- Multi-tab terminal panel; tabs closeable individually
- Fit addon for responsive resize

#### Logs
- Real-time log viewer for each service (stdout/stderr tail via chokidar)
- Log modal with auto-scroll and manual scroll-lock toggle
- Clear log button

#### Settings
- Configurable projects directory (default: `~/LStack/www/`)
- Web server selector (Nginx / Apache)
- Default PHP version for new profiles
- SSL provider status and CA installation
- Language toggle (English / Vietnamese)
- Auto-start services toggle
- Folder picker dialog for path fields

#### Data & Configuration
- All data stored in `~/.lstack/` — no system-wide service installs polluted
- Nginx and Apache configs, vhosts, MariaDB data, PostgreSQL data, Redis config, certificates, and downloaded binaries all under `~/.lstack/`
- `settings.json` and `php-profiles.json` in the data directory
- Graceful migration path from legacy `~/.devstack/` directory

#### Platforms
- **Windows x64** — NSIS installer (`LStack Setup 1.0.0.exe`)
- **Linux x64** — AppImage (`LStack-1.0.0.AppImage`) and `.deb` package
- Linux packages built and tested on Ubuntu/Debian via WSL or native Linux

### Notes

- macOS is not part of the v1.0.0 release scope
- MongoDB support is included in the package registry but considered optional; not auto-started
- PHP-FPM port 9100–9600 range is deterministic per profile name (hash-based); the `minimal` profile resolves to port 9105


```

### File: CHANGELOG.vi.md
```md
# Nhật ký thay đổi

Tất cả các thay đổi đáng chú ý của LStack được ghi lại trong file này.  
Định dạng: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) · Phiên bản: [Semantic Versioning](https://semver.org/)

Bản tiếng Anh: [CHANGELOG.md](CHANGELOG.md)

---

## [1.0.0] - 2026-03-23

Phiên bản ổn định đầu tiên của LStack.

### Thêm mới

#### Ứng dụng
- Ứng dụng desktop xây dựng với **Electron 32**, **React 18**, **TypeScript 5**, **Vite 5** và **Tailwind CSS 3**
- Giao diện song ngữ — **Tiếng Anh** và **Tiếng Việt** chuyển đổi linh hoạt ngay trong app
- Hỗ trợ system tray với điều khiển dịch vụ nhanh
- Tự động cập nhật qua `electron-updater`
- Thanh tiêu đề frameless tuỳ chỉnh với nút điều khiển cửa sổ
- Giao diện dark mode với Tailwind CSS và icon Lucide

#### Quản lý dịch vụ
- **Khởi động / dừng / khởi động lại** mọi dịch vụ chỉ với một cú nhấp
- Badge trạng thái thời gian thực: đang chạy, đã dừng, đang khởi động, đang dừng, lỗi
- Dịch vụ: **Nginx**, **Apache**, **MariaDB**, **PostgreSQL**, **PHP-FPM**, **Redis**, **Memcached**, **Mailpit**, **MongoDB**
- Tự động khởi động dịch vụ khi mở app (cấu hình riêng từng dịch vụ)
- Hiển thị cổng và PID của dịch vụ trên dashboard
- Xem log dịch vụ thời gian thực (theo dõi stdout/stderr ngay trên UI)

#### Virtual host & Dự án
- Tự động tạo domain `.test` khi thêm thư mục vào thư mục dự án
- Hỗ trợ **Nginx** và **Apache** làm web server, chọn riêng cho từng dự án
- Tự động tạo và tải lại config virtual host khi thêm/xoá dự án
- Tự động tạo block SSL song song với block HTTP
- Danh sách dự án với nhận diện framework: **Laravel**, **WordPress**, **Symfony**, **CodeIgniter**
- Metadata dự án: có git, có `composer.json`, có `package.json`
- Chế độ xem dạng lưới và danh sách
- Tìm kiếm / lọc dự án theo tên
- Menu ngữ cảnh mỗi dự án: mở trình duyệt, mở thư mục, mở terminal, xoá vhost

#### SSL / HTTPS
- Quản lý CA cục bộ qua **mkcert**
- Cài đặt và tin tưởng CA chỉ với một cú nhấp từ trang Cài đặt
- Tự động tạo chứng chỉ SSL cho từng domain `.test`
- Hiển thị trạng thái trust theo chứng chỉ và kiểm tra trust toàn hệ thống trên Linux

#### PHP-FPM Profiles
- PHP-FPM theo dự án: mỗi profile chạy dưới dạng **tiến trình riêng** với cổng hash-based (dải 9100–9600)
- Sáu **profile tích hợp sẵn**: Minimal, WordPress, Laravel, Symfony, CodeIgniter, Full Stack
- **Profile tuỳ chỉnh**: tạo, chỉnh sửa và xoá profile với cài đặt `php.ini` và danh sách extension tuỳ ý
- Cài đặt PHP theo profile: `memory_limit`, `max_execution_time`, `max_input_time`, `max_input_vars`, `upload_max_filesize`, `post_max_size`, `display_errors`, `date.timezone`
- Danh sách extension theo profile: bật/tắt từng extension PHP
- **Tự động nhận diện profile** khi mở dự án có sẵn (phát hiện `artisan`, `wp-config.php`, `symfony.lock`, `spark`)
- Hiện thị và chỉnh sửa profile được gán ngay trên card dự án

#### Domain đặc biệt
- `localhost.test` — dashboard / trang welcome của LStack, phục vụ bởi PHP-FPM profile `minimal`
- `phpmyadmin.test` — phpMyAdmin tự động phục vụ; đăng nhập tự động root không cần mật khẩu
- Cả hai domain được tự động thêm vào file `hosts` hệ thống khi khởi động lần đầu

#### Trình tạo dự án (Templates)
- Wizard tạo dự án trong app với chọn template và phiên bản
- Template hỗ trợ: **Blank PHP**, **Laravel** (8–12), **WordPress** (5.9–6.8/latest), **Symfony** (5.4–7.3), **CodeIgniter** (3.1–4.5), **Drupal** (10–11), **Joomla** (4–5), **PrestaShop** (1.7–8)
- Tự động tải và cài đặt file framework qua Composer / archive trực tiếp
- Tiến trình cài đặt hiển thị trong panel terminal trong app

#### Package Manager
- Duyệt, tải và cài đặt binary dịch vụ ngay trong app — không cần package manager hệ thống
- Package: Nginx, Apache, MariaDB, PHP (nhiều phiên bản), phpMyAdmin, Redis, Mailpit, PostgreSQL, MongoDB, Memcached
- Registry package tải từ `package-registry.json` đính kèm, có URL tải theo từng nền tảng
- Trạng thái cài đặt được lưu; đường dẫn binary tự động đưa vào config dịch vụ
- Thanh tiến trình tải với số byte và phần trăm
- Log cài đặt stream vào terminal trong app

#### Terminal
- Terminal **xterm.js** đầy đủ tính năng cho từng dự án (backend node-pty)
- Terminal mở sẵn trong thư mục dự án
- Panel terminal nhiều tab; đóng từng tab độc lập
- Fit addon cho resize responsive

#### Logs
- Xem log thời gian thực cho từng dịch vụ (theo dõi stdout/stderr qua chokidar)
- Modal log với tự động cuộn và khoá cuộn thủ công
- Nút xoá log

#### Cài đặt
- Thư mục dự án tuỳ chỉnh (mặc định: `~/LStack/www/`)
- Chọn web server (Nginx / Apache)
- Phiên bản PHP mặc định cho profile mới
- Trạng thái SSL provider và cài đặt CA
- Chuyển đổi ngôn ngữ (Tiếng Anh / Tiếng Việt)
- Bật/tắt tự động khởi động dịch vụ
- Dialog chọn thư mục cho các trường đường dẫn

#### Dữ liệu & Cấu hình
- Toàn bộ dữ liệu lưu tại `~/.lstack/` — không cài dịch vụ toàn hệ thống
- Config Nginx/Apache, vhost, dữ liệu MariaDB, PostgreSQL, Redis, chứng chỉ và binary đều dưới `~/.lstack/`
- `settings.json` và `php-profiles.json` trong thư mục dữ liệu
- Hỗ trợ migration từ thư mục `~/.devstack/` cũ

#### Nền tảng
- **Windows x64** — installer NSIS (`LStack Setup 1.0.0.exe`)
- **Linux x64** — AppImage (`LStack-1.0.0.AppImage`) và gói `.deb`
- Gói Linux được build và kiểm thử trên Ubuntu/Debian qua WSL hoặc Linux native

### Ghi chú

- macOS không nằm trong phạm vi phát hành v1.0.0
- Hỗ trợ MongoDB có trong package registry nhưng là tuỳ chọn; không tự động khởi động
- Dải cổng PHP-FPM 9100–9600 xác định theo tên profile (hash-based); profile `minimal` sử dụng cổng 9105


```

### File: electron_builder.json
```json
{
  "appId": "dev.lstack.app",
  "productName": "LStack",
  "directories": {
    "output": "release"
  },
  "files": [
    "dist-electron/**/*",
    "dist/**/*",
    "package-registry.json"
  ],
  "asar": true,
  "extraResources": [
    "package-registry.json",
    { "from": "icon.png", "to": "icon.png" }
  ],
  "asarUnpack": [
    "node_modules/node-pty/**/*"
  ],
  "win": {
    "icon": "icon.png",
    "target": [
      "dir"
    ]
  },
  "linux": {
    "icon": "icon.png",
    "target": [
      "deb",
      "rpm",
      "AppImage"
    ],
    "category": "Development",
    "maintainer": "LStack <contact@lstack.dev>"
  },
  "npmRebuild": false,
  "buildDependenciesFromSource": false
}

```

### File: index.html
```html
<!DOCTYPE html>
<html lang="vi" class="dark">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>DevStack</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

```

### File: package_registry.json
```json
[
  {
    "id": "mariadb",
    "label": "MariaDB",
    "icon": "database",
    "versions": [
      {
        "version": "12.0.1",
        "label": "MariaDB 12.0.1 (Latest)",
        "downloads": {
          "win32": "https://archive.mariadb.org/mariadb-12.0.1/winx64-packages/mariadb-12.0.1-winx64.zip",
          "darwin": "https://archive.mariadb.org/mariadb-12.0.1/bintar-macos14-arm64/mariadb-12.0.1-macos14-arm64.tar.gz",
          "linux": "https://archive.mariadb.org/mariadb-12.0.1/bintar-linux-systemd-x86_64/mariadb-12.0.1-linux-systemd-x86_64.tar.gz"
        }
      },
      {
        "version": "11.4.5",
        "label": "MariaDB 11.4.5 LTS",
        "lts": true,
        "downloads": {
          "win32": "https://archive.mariadb.org/mariadb-11.4.5/winx64-packages/mariadb-11.4.5-winx64.zip",
          "darwin": "https://archive.mariadb.org/mariadb-11.4.5/bintar-macos14-arm64/mariadb-11.4.5-macos14-arm64.tar.gz",
          "linux": "https://archive.mariadb.org/mariadb-11.4.5/bintar-linux-systemd-x86_64/mariadb-11.4.5-linux-systemd-x86_64.tar.gz"
        }
      },
      {
        "version": "11.2.6",
        "label": "MariaDB 11.2.6",
        "downloads": {
          "win32": "https://archive.mariadb.org/mariadb-11.2.6/winx64-packages/mariadb-11.2.6-winx64.zip",
          "darwin": "https://archive.mariadb.org/mariadb-11.2.6/bintar-macos14-arm64/mariadb-11.2.6-macos14-arm64.tar.gz",
          "linux": "https://archive.mariadb.org/mariadb-11.2.6/bintar-linux-systemd-x86_64/mariadb-11.2.6-linux-systemd-x86_64.tar.gz"
        }
      },
      {
        "version": "10.11.11",
        "label": "MariaDB 10.11.11 LTS",
        "lts": true,
        "downloads": {
          "win32": "https://archive.mariadb.org/mariadb-10.11.11/winx64-packages/mariadb-10.11.11-winx64.zip",
          "darwin": "https://archive.mariadb.org/mariadb-10.11.11/bintar-macos14-arm64/mariadb-10.11.11-macos14-arm64.tar.gz",
          "linux": "https://archive.mariadb.org/mariadb-10.11.11/bintar-linux-systemd-x86_64/mariadb-10.11.11-linux-systemd-x86_64.tar.gz"
        }
      },
      {
        "version": "10.6.21",
        "label": "MariaDB 10.6.21 LTS",
        "lts": true,
        "downloads": {
          "win32": "https://archive.mariadb.org/mariadb-10.6.21/winx64-packages/mariadb-10.6.21-winx64.zip",
          "darwin": "https://archive.mariadb.org/mariadb-10.6.21/bintar-macos14-arm64/mariadb-10.6.21-macos14-arm64.tar.gz",
          "linux": "https://archive.mariadb.org/mariadb-10.6.21/bintar-linux-systemd-x86_64/mariadb-10.6.21-linux-systemd-x86_64.tar.gz"
        }
      }
    ]
  },
  {
    "id": "nginx",
    "label": "Nginx",
    "icon": "server",
    "versions": [
      {
        "version": "1.27.4",
        "label": "Nginx 1.27.4",
        "lts": false,
        "downloads": {
          "win32": "https://nginx.org/download/nginx-1.27.4.zip",
          "darwin": "https://nginx.org/download/nginx-1.27.4.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/nginx-v1.27.4/nginx-1.27.4-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "1.26.3",
        "label": "Nginx 1.26.3",
        "lts": true,
        "downloads": {
          "win32": "https://nginx.org/download/nginx-1.26.3.zip",
          "darwin": "https://nginx.org/download/nginx-1.26.3.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/nginx-v1.26.3/nginx-1.26.3-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "1.24.0",
        "label": "Nginx 1.24.0",
        "lts": true,
        "downloads": {
          "win32": "https://nginx.org/download/nginx-1.24.0.zip",
          "darwin": "https://nginx.org/download/nginx-1.24.0.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/nginx-v1.24.0/nginx-1.24.0-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "1.22.1",
        "label": "Nginx 1.22.1",
        "lts": false,
        "downloads": {
          "win32": "https://nginx.org/download/nginx-1.22.1.zip",
          "darwin": "https://nginx.org/download/nginx-1.22.1.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/nginx-v1.22.1/nginx-1.22.1-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "1.20.2",
        "label": "Nginx 1.20.2",
        "lts": false,
        "downloads": {
          "win32": "https://nginx.org/download/nginx-1.20.2.zip",
          "darwin": "https://nginx.org/download/nginx-1.20.2.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/nginx-v1.20.2/nginx-1.20.2-native-linux-x64.tar.gz"
        }
      }
    ]
  },
  {
    "id": "php",
    "label": "PHP",
    "icon": "code",
    "versions": [
      {
        "version": "8.6.0",
        "label": "PHP 8.6.0",
        "lts": false,
        "downloads": {
          "win32": "https://windows.php.net/downloads/releases/php-8.6.0-nts-Win32-vs16-x64.zip",
          "darwin": "https://github.com/shivammathur/php-builder-macos/releases/download/8.6/php_8.6.0_arm64.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/php-v8.6.0/php-8.6.0-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "8.5.4",
        "label": "PHP 8.5.4",
        "lts": false,
        "downloads": {
          "win32": "https://windows.php.net/downloads/releases/php-8.5.4-nts-Win32-vs16-x64.zip",
          "darwin": "https://github.com/shivammathur/php-builder-macos/releases/download/8.5/php_8.5.4_arm64.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/php-v8.5.4/php-8.5.4-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "8.4.4",
        "label": "PHP 8.4.4",
        "lts": false,
        "downloads": {
          "win32": "https://windows.php.net/downloads/releases/php-8.4.4-nts-Win32-vs16-x64.zip",
          "darwin": "https://github.com/shivammathur/php-builder-macos/releases/download/8.4/php_8.4.4_arm64.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/php-v8.4.4/php-8.4.4-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "8.3.17",
        "label": "PHP 8.3.17",
        "lts": true,
        "downloads": {
          "win32": "https://windows.php.net/downloads/releases/php-8.3.17-nts-Win32-vs16-x64.zip",
          "darwin": "https://github.com/shivammathur/php-builder-macos/releases/download/8.3/php_8.3.17_arm64.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/php-v8.3.17/php-8.3.17-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "8.2.27",
        "label": "PHP 8.2.27",
        "lts": true,
        "downloads": {
          "win32": "https://windows.php.net/downloads/releases/php-8.2.27-nts-Win32-vs16-x64.zip",
          "darwin": "https://github.com/shivammathur/php-builder-macos/releases/download/8.2/php_8.2.27_arm64.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/php-v8.2.27/php-8.2.27-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "8.1.31",
        "label": "PHP 8.1.31",
        "lts": false,
        "downloads": {
          "win32": "https://windows.php.net/downloads/releases/php-8.1.31-nts-Win32-vs16-x64.zip",
          "darwin": "https://github.com/shivammathur/php-builder-macos/releases/download/8.1/php_8.1.31_arm64.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/php-v8.1.31/php-8.1.31-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "8.0.30",
        "label": "PHP 8.0.30",
        "lts": false,
        "downloads": {
          "win32": "https://windows.php.net/downloads/releases/php-8.0.30-nts-Win32-vs16-x64.zip",
          "darwin": "https://github.com/shivammathur/php-builder-macos/releases/download/8.0/php_8.0.30_arm64.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/php-v8.0.30/php-8.0.30-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "7.4.33",
        "label": "PHP 7.4.33",
        "lts": false,
        "downloads": {
          "win32": "https://windows.php.net/downloads/releases/php-7.4.33-nts-Win32-vc15-x64.zip",
          "darwin": "https://github.com/shivammathur/php-builder-macos/releases/download/7.4/php_7.4.33_arm64.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/php-v7.4.33/php-7.4.33-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "7.3.33",
        "label": "PHP 7.3.33",
        "lts": false,
        "downloads": {
          "win32": "https://windows.php.net/downloads/releases/php-7.3.33-nts-Win32-vc15-x64.zip",
          "darwin": "https://github.com/shivammathur/php-builder-macos/releases/download/7.3/php_7.3.33_arm64.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/php-v7.3.33/php-7.3.33-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "7.2.34",
        "label": "PHP 7.2.34",
        "lts": false,
        "downloads": {
          "win32": "https://windows.php.net/downloads/releases/php-7.2.34-nts-Win32-vc15-x64.zip",
          "darwin": "https://github.com/shivammathur/php-builder-macos/releases/download/7.2/php_7.2.34_arm64.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/php-v7.2.34/php-7.2.34-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "7.1.33",
        "label": "PHP 7.1.33",
        "lts": false,
        "downloads": {
          "win32": "https://windows.php.net/downloads/releases/php-7.1.33-nts-Win32-vc14-x64.zip",
          "darwin": "https://github.com/shivammathur/php-builder-macos/releases/download/7.1/php_7.1.33_arm64.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/php-v7.1.33/php-7.1.33-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "7.0.33",
        "label": "PHP 7.0.33",
        "lts": false,
        "downloads": {
          "win32": "https://windows.php.net/downloads/releases/php-7.0.33-nts-Win32-vc14-x64.zip",
          "darwin": "https://github.com/shivammathur/php-builder-macos/releases/download/7.0/php_7.0.33_arm64.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/php-v7.0.33/php-7.0.33-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "5.6.40",
        "label": "PHP 5.6.40",
        "lts": false,
        "downloads": {
          "win32": "https://windows.php.net/downloads/releases/php-5.6.40-nts-Win32-vc11-x64.zip",
          "darwin": "https://github.com/shivammathur/php-builder-macos/releases/download/5.6/php_5.6.40_arm64.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/php-v5.6.40/php-5.6.40-native-linux-x64.tar.gz"
        }
      }
    ]
  },
  {
    "id": "phpmyadmin",
    "label": "phpMyAdmin",
    "icon": "layout-dashboard",
    "versions": [
      {
        "version": "6.0-snapshot",
        "label": "phpMyAdmin 6.0 (Snapshot)",
        "downloads": {
          "win32": "https://files.phpmyadmin.net/snapshots/phpMyAdmin-6.0+snapshot-all-languages.zip",
          "darwin": "https://files.phpmyadmin.net/snapshots/phpMyAdmin-6.0+snapshot-all-languages.zip",
          "linux": "https://files.phpmyadmin.net/snapshots/phpMyAdmin-6.0+snapshot-all-languages.zip"
        }
      },
      {
        "version": "5.2.3",
        "label": "phpMyAdmin 5.2.3 (Stable)",
        "lts": true,
        "downloads": {
          "win32": "https://files.phpmyadmin.net/phpMyAdmin/5.2.3/phpMyAdmin-5.2.3-all-languages.zip",
          "darwin": "https://files.phpmyadmin.net/phpMyAdmin/5.2.3/phpMyAdmin-5.2.3-all-languages.zip",
          "linux": "https://files.phpmyadmin.net/phpMyAdmin/5.2.3/phpMyAdmin-5.2.3-all-languages.zip"
        }
      },
      {
        "version": "5.2.2",
        "label": "phpMyAdmin 5.2.2",
        "downloads": {
          "win32": "https://files.phpmyadmin.net/phpMyAdmin/5.2.2/phpMyAdmin-5.2.2-all-languages.zip",
          "darwin": "https://files.phpmyadmin.net/phpMyAdmin/5.2.2/phpMyAdmin-5.2.2-all-languages.zip",
          "linux": "https://files.phpmyadmin.net/phpMyAdmin/5.2.2/phpMyAdmin-5.2.2-all-languages.zip"
        }
      }
    ]
  },
  {
    "id": "redis",
    "label": "Redis",
    "icon": "zap",
    "versions": [
      {
        "version": "7.2.4",
        "label": "Redis 7.2.4",
        "lts": true,
        "downloads": {
          "win32": "https://github.com/tporadowski/redis/releases/download/v5.0.14.1/Redis-x64-5.0.14.1.zip",
          "darwin": "https://download.redis.io/releases/redis-7.2.4.tar.gz",
          "linux": "https://download.redis.io/releases/redis-7.2.4.tar.gz"
        }
      }
    ]
  },
  {
    "id": "mailpit",
    "label": "Mailpit",
    "icon": "mail",
    "versions": [
      {
        "version": "1.22.3",
        "label": "Mailpit 1.22.3",
        "lts": true,
        "downloads": {
          "win32": "https://github.com/axllent/mailpit/releases/download/v1.22.3/mailpit-windows-amd64.zip",
          "darwin": "https://github.com/axllent/mailpit/releases/download/v1.22.3/mailpit-darwin-arm64.tar.gz",
          "linux": "https://github.com/axllent/mailpit/releases/download/v1.22.3/mailpit-linux-amd64.tar.gz"
        }
      }
    ]
  },
  {
    "id": "openlitespeed",
    "label": "OpenLiteSpeed",
    "icon": "server",
    "versions": [
      {
        "version": "1.7.19",
        "label": "OpenLiteSpeed 1.7.19",
        "downloads": {
          "win32": "https://openlitespeed.org/packages/openlitespeed-1.7.19.tgz",
          "darwin": "https://openlitespeed.org/packages/openlitespeed-1.7.19.tgz",
          "linux": "https://openlitespeed.org/packages/openlitespeed-1.7.19.tgz"
        }
      }
    ]
  },
  {
    "id": "apache",
    "label": "Apache",
    "icon": "server",
    "versions": [
      {
        "version": "2.4.63",
        "label": "Apache HTTPD 2.4.63",
        "lts": true,
        "downloads": {
          "win32": "https://www.apachelounge.com/download/VS17/binaries/httpd-2.4.63-win64-VS17.zip",
          "darwin": "https://archive.apache.org/dist/httpd/httpd-2.4.63.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/apache-v2.4.63/apache-2.4.63-native-linux-x64.tar.gz"
        }
      },
      {
        "version": "2.4.62",
        "label": "Apache HTTPD 2.4.62",
        "lts": false,
        "downloads": {
          "win32": "https://www.apachelounge.com/download/VS17/binaries/httpd-2.4.62-win64-VS17.zip",
          "darwin": "https://archive.apache.org/dist/httpd/httpd-2.4.62.tar.gz",
          "linux": "https://github.com/marixdev/lstack-binaries/releases/download/apache-v2.4.62/apache-2.4.62-native-linux-x64.tar.gz"
        }
      },
      {
 
... [TRUNCATED]
```

### File: postcss.config.js
```js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};

```

### File: README.vi.md
```md
# LStack

> Môi trường phát triển cục bộ dành cho Windows và Linux.  
> Ứng dụng desktop thay thế Laragon — quản lý dịch vụ PHP, virtual host, cơ sở dữ liệu và dự án qua giao diện đồ họa hiện đại.

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)](#cài-đặt)
[![Version](https://img.shields.io/badge/version-1.0.0-green)](CHANGELOG.vi.md)

**Trang chủ:** https://lstack.dev  
**GitHub:** https://github.com/marixdev/lstack

---

## Giới thiệu

LStack là ứng dụng desktop quản lý toàn bộ stack phát triển PHP cục bộ — web server, cơ sở dữ liệu, cache và mail — không cần Docker hay WSL. Các dịch vụ chạy dưới dạng tiến trình native, dự án được phục vụ qua domain `.test` với SSL tuỳ chọn bằng mkcert.

Xây dựng với **Electron 32**, **React 18**, **TypeScript 5**, **Vite 5** và **Tailwind CSS 3**.

---

## Tính năng

- **Quản lý dịch vụ một chạm** — khởi động, dừng và khởi động lại mọi dịch vụ từ dashboard
- **Virtual host** — tự động tạo domain `.test` (ví dụ: `myapp.test`) với Nginx hoặc Apache
- **Chứng chỉ SSL** — tin tưởng CA cục bộ chỉ với một cú nhấp; HTTPS đầy đủ trên mọi dự án
- **PHP profile theo dự án** — gán một tiến trình PHP-FPM riêng với cài đặt `php.ini` và extension độc lập cho từng dự án
- **Kiểm soát PHP extension** — bật/tắt extension theo từng profile; profile tích hợp sẵn được cấu hình trước cho Laravel, WordPress, Symfony, v.v.
- **Trình tạo dự án** — khởi tạo dự án mới từ template chỉ với một cú nhấp; tự động cài đặt file CMS/framework
- **Nhận diện framework** — tự động phát hiện Laravel, WordPress, Symfony và CodeIgniter trong thư mục có sẵn
- **phpMyAdmin** — truy cập tại `phpmyadmin.test` với đăng nhập tự động (root, không cần mật khẩu)
- **Terminal tích hợp** — terminal xterm.js đầy đủ tính năng, mở thẳng trong thư mục dự án
- **Log thời gian thực** — xem log dịch vụ và access log trực tiếp trên UI
- **Package manager** — tải và cài đặt binary dịch vụ (Nginx, Apache, MariaDB, PHP, Redis, v.v.) ngay trong app, không cần cài toàn hệ thống
- **Tự động cập nhật** — kiểm tra bản cập nhật qua electron-updater
- **Giao diện song ngữ** — hỗ trợ đầy đủ tiếng Anh và tiếng Việt, chuyển đổi ngay trong app

---

## Dịch vụ

| Dịch vụ       | Cổng mặc định           | Ghi chú                                        |
|---------------|-------------------------|------------------------------------------------|
| Nginx         | 80 (HTTP), 443 (HTTPS)  | Web server mặc định                            |
| Apache        | 80 (HTTP), 443 (HTTPS)  | Lựa chọn thay thế                              |
| MariaDB       | 3306                    | Cơ sở dữ liệu tương thích MySQL                |
| PostgreSQL    | 5432                    | Cơ sở dữ liệu quan hệ thay thế                 |
| PHP-FPM       | 9100–9600 (theo profile)| Cổng hash-based theo tên profile               |
| Redis         | 6379                    | Cache in-memory / message broker               |
| Memcached     | 11211                   | Cache bộ nhớ nhẹ                               |
| Mailpit       | 1025 (SMTP), 8025 (UI)  | Bắt mail cục bộ; Web UI tại :8025              |
| MongoDB       | 27017                   | Cơ sở dữ liệu document (tùy chọn)              |

---

## PHP Profiles

Mỗi PHP profile chạy dưới dạng tiến trình riêng biệt với cổng và cài đặt `php.ini` độc lập. Nhiều dự án có thể dùng chung một profile.

| Profile        | Bộ nhớ  | Thời gian thực thi tối đa | Extension chính                                             |
|----------------|---------|---------------------------|-------------------------------------------------------------|
| **Minimal**    | 256 MB  | 60 giây                   | curl, mbstring, openssl, pdo_mysql, zip                     |
| **WordPress**  | 512 MB  | 300 giây                  | + gd, mysqli, exif, fileinfo                                |
| **Laravel**    | 512 MB  | 120 giây                  | + gd, intl, pdo_sqlite, sodium                              |
| **Symfony**    | 512 MB  | 120 giây                  | + intl, xml, pdo_sqlite                                     |
| **CodeIgniter**| 256 MB  | 120 giây                  | + intl, mysqli                                              |
| **Full Stack** | 1024 MB | 300 giây                  | + gd, soap, sodium, xsl, exif, intl, v.v.                   |
| **Tuỳ chỉnh**  | tuỳ ý   | tuỳ ý                     | Tạo profile riêng với bất kỳ cài đặt nào                    |

---

## Template dự án

Khi tạo dự án mới, LStack có thể khởi tạo từ một trong các template sau:

| Template     | Phiên bản hỗ trợ                        |
|--------------|-----------------------------------------|
| Blank PHP    | — (file `index.php` trống)              |
| Laravel      | 12, 11, 10, 9, 8                        |
| WordPress    | latest, 6.8, 6.7, 6.6, 6.5, 6.4, 5.9  |
| Symfony      | 7.3, 7.2, 6.4, 5.4                      |
| CodeIgniter  | 4.5, 4.4, 4.3, 3.1                      |
| Drupal       | 11, 10                                  |
| Joomla       | 5, 4                                    |
| PrestaShop   | 8, 1.7                                  |

---

## Domain đặc biệt

| Domain             | Mục đích                                         |
|--------------------|--------------------------------------------------|
| `localhost.test`   | Dashboard / trang welcome của LStack             |
| `phpmyadmin.test`  | phpMyAdmin (đăng nhập tự động với root)           |

Cả hai domain được tự động thêm vào file `hosts` hệ thống khi khởi động lần đầu.

---

## Cài đặt

### Bản dựng sẵn

Tải bản phát hành mới nhất tại [trang Releases](https://github.com/marixdev/lstack/releases) hoặc [lstack.dev](https://lstack.dev):

| Nền tảng    | Installer                       |
|-------------|---------------------------------|
| Windows x64 | `LStack Setup 1.0.0.exe`        |
| Linux x64   | `LStack-1.0.0.AppImage`         |
| Linux x64   | `lstack_1.0.0_amd64.deb`        |

**Windows** — chạy installer NSIS và mở LStack từ Start Menu.

**Linux (AppImage):**

```bash
chmod +x LStack-1.0.0.AppImage
./LStack-1.0.0.AppImage
```

**Linux (.deb):**

```bash
sudo dpkg -i lstack_1.0.0_amd64.deb
lstack
```

---

## Build từ mã nguồn

### Yêu cầu

- Node.js 20+
- npm 9+
- Git

### Các bước

```bash
git clone https://github.com/marixdev/lstack.git
cd lstack
npm install
```

**Phát triển (hot reload):**

```bash
npm run dev
```

**Build production:**

```bash
# Windows
npm run dist:win

# Linux (chạy trên Linux hoặc WSL)
npm run dist:linux
```

File output được đặt trong thư mục `release/`.

---

## Thư mục dữ liệu

LStack lưu toàn bộ cấu hình, dữ liệu dịch vụ, chứng chỉ và binary đã tải về tại:

```
~/.lstack/
├── nginx/             # Config và virtual host Nginx
├── apache/            # Config và virtual host Apache
├── mariadb/           # File dữ liệu MariaDB
├── postgresql/        # File dữ liệu PostgreSQL
├── redis/             # Config và persistence Redis
├── certs/             # CA mkcert và chứng chỉ theo domain
├── bins/              # Binary dịch vụ đã tải
├── php-profiles.json  # PHP profile tuỳ chỉnh
└── settings.json      # Cài đặt ứng dụng
```

Tất cả dữ liệu đều độc lập — gỡ cài đặt LStack không ảnh hưởng đến cơ sở dữ liệu hoặc cấu hình trừ khi bạn xoá thư mục này thủ công.

---

## Cài đặt ứng dụng

| Cài đặt                | Mô tả                                                         |
|------------------------|---------------------------------------------------------------|
| Thư mục dự án          | Thư mục gốc chứa dự án (mặc định: `~/LStack/www/`)           |
| Web server             | Nginx hoặc Apache                                             |
| Phiên bản PHP          | Phiên bản PHP mặc định cho profile mới                        |
| SSL provider           | mkcert; cài và tin tưởng CA cục bộ ngay trên UI               |
| Ngôn ngữ               | Tiếng Anh hoặc Tiếng Việt                                     |
| Tự động khởi động      | Tự động khởi động các dịch vụ đã bật khi mở app              |

---

## Giấy phép

[GPL-3.0](LICENSE) © LStack — https://lstack.dev


```

### File: tailwind.config.js
```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{ts,tsx}', './index.html'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#eff6ff',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          900: '#1e3a8a',
        },
        dark: {
          50: '#f8fafc',
          100: '#f1f5f9',
          700: '#334155',
          800: '#1e293b',
          900: '#0f172a',
          950: '#020617',
        },
      },
    },
  },
  plugins: [],
};

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020", "DOM"],
    "strict": true,
    "jsx": "react-jsx",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "resolveJsonModule": true,
    "outDir": "./dist",
    "rootDir": ".",
    "baseUrl": ".",
    "paths": {
      "@shared/*": ["./src/types/*"],
      "@main/*": ["./main/*"]
    }
  },
  "include": ["main/**/*", "src/**/*", "vite*.ts", "forge.config.ts"],
  "exclude": ["node_modules", "dist", ".vite"]
}

```

### File: vite.config.ts
```ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import electron from 'vite-plugin-electron/simple';
import path from 'path';

export default defineConfig({
  plugins: [
    react(),
    electron({
      main: {
        entry: 'main/main.ts',
        vite: {
          build: {
            outDir: 'dist-electron',
            rollupOptions: {
              external: ['electron', 'node-pty', 'fs-extra', 'chokidar'],
            },
          },
        },
      },
      preload: {
        input: path.join(__dirname, 'main/preload.ts'),
        vite: {
          build: {
            outDir: 'dist-electron',
          },
        },
      },
      renderer: {},
    }),
  ],
  build: {
    outDir: 'dist',
  },
});
```

### File: .github\copilot-instructions.md
```md
#   C o p i l o t   I n s t r u c t i o n s 
 -   T h i s   i s   a   R e a c t   p r o j e c t   u s i n g   V i t e   o r   E l e c t r o n   F o r g e . 
 -   M a k e   s u r e   t o   u s e   ` . t s x `   f o r   f i l e s   c o n t a i n i n g   J S X . 
 -   A l w a y s   a s s u m e   ` c o m p i l e r O p t i o n s . j s x `   i s   s e t   t o   ` " r e a c t - j s x " `   i n   ` t s c o n f i g . j s o n `   t o   a l l o w   J S X .   D o   n o t   m o d i f y   ` t s c o n f i g . j s o n `   b a c k   t o   r e m o v e   i t . 
 -   A d h e r e   t o   s t r i c t   T y p e S c r i p t   t y p i n g   r u l e   ( ` s t r i c t :   t r u e ` ) .   E n s u r e   n o   ` T S 1 7 0 0 4 `   o r   i m p l i c i t   a n y   e r r o r s   r e m a i n . 
 -   D e v S t a c k   S e t t i n g s   t y p e   i n c l u d e s   ` w e b s e r v e r :   ' n g i n x '   |   ' a p a c h e '   |   ' o p e n l i t e s p e e d ' `   s o   e n s u r e   c a s t i n g   w h e n   d y n a m i c a l l y   i t e r a t i n g .   
 
 
```

### File: main\main.ts
```ts
import {
  app,
  BrowserWindow,
  ipcMain,
  shell,
  Menu,
  Tray,
  nativeImage,
  dialog,
} from 'electron';
import path from 'path';
import fs from 'fs-extra';
import { ServiceManager } from './core/ServiceManager';
import { PackageManager } from './core/PackageManager';
import { VHostManager } from './core/VHostManager';
import { CertManager } from './core/CertManager';
import { registerIpcHandlers } from './ipc';
import { TerminalManager } from './core/TerminalManager';
import type { LStackSettings } from '../src/types';

const VITE_DEV_SERVER_URL = process.env.VITE_DEV_SERVER_URL;

const HOME = app.getPath('home');
const DATA_DIR = path.join(HOME, '.lstack');
const ELECTRON_USER_DATA_DIR = path.join(DATA_DIR, 'electron');
const ELECTRON_SESSION_DATA_DIR = path.join(ELECTRON_USER_DATA_DIR, 'session');
const ELECTRON_CACHE_DIR = path.join(ELECTRON_USER_DATA_DIR, 'cache');
const BIN_DIR = path.join(DATA_DIR, 'bin', process.platform);
const WWW_DIR = path.join(DATA_DIR, 'www');
const ETC_DIR = path.join(DATA_DIR, 'etc');
const LOGS_DIR = path.join(DATA_DIR, 'logs');
const DB_DIR = path.join(DATA_DIR, 'data');
const SETTINGS_FILE = path.join(DATA_DIR, 'settings.json');

// Keep Chromium profile under writable app-owned directory
fs.ensureDirSync(ELECTRON_USER_DATA_DIR);
fs.ensureDirSync(ELECTRON_SESSION_DATA_DIR);
fs.ensureDirSync(ELECTRON_CACHE_DIR);

app.setPath('userData', ELECTRON_USER_DATA_DIR);
app.setPath('sessionData', ELECTRON_SESSION_DATA_DIR);
app.commandLine.appendSwitch('disk-cache-dir', ELECTRON_CACHE_DIR);
app.commandLine.appendSwitch('media-cache-dir', ELECTRON_CACHE_DIR);
app.commandLine.appendSwitch('disable-http-cache');
app.commandLine.appendSwitch('disable-gpu-shader-disk-cache');
app.commandLine.appendSwitch('disable-features', 'GpuShaderDiskCache');
app.disableHardwareAcceleration();

const gotSingleInstanceLock = app.requestSingleInstanceLock();
if (!gotSingleInstanceLock) {
  app.quit();
}

const defaultSettings: LStackSettings = {
  wwwDir: WWW_DIR,
  dataDir: DATA_DIR,
  logsDir: LOGS_DIR,
  binDir: BIN_DIR,
  domain: 'test',
  webserver: 'nginx',
  phpVersion: '8.3.29',
  mariadbVersion: '11.4.5',
  nginxVersion: '1.28.0',
  apacheVersion: '2.4.66',
  redisVersion: '7.2.4',
  memcachedVersion: '1.6.22',
  mailpitVersion: '1.22.3',
  postgresqlVersion: '17.4',
  httpPort: 80,
  httpsPort: 443,
  mariadbPort: 3306,
  autoVirtualHost: true,
  autoStartServices: false,
  language: 'vi',
  theme: 'dark',
};

const VERSION_NORMALIZERS: Record<string, Record<string, string>> = {
  phpVersion: {
    '5': '5.6.40',
    '5.6': '5.6.40',
    '7': '7.4.33',
    '7.4': '7.4.33',
    '7.3': '7.3.33',
    '8.5': '8.5.4',
    '8.5.1': '8.5.4',
    '8.4': '8.4.19',
    '8.4.16': '8.4.19',
    '8.3': '8.3.29',
    '8.2': '8.2.30',
    '8.1': '8.1.34',
  },
  mariadbVersion: {
    '12': '12.0.1',
    '12.0': '12.0.1',
    '11.4': '11.4.5',
    '11.2': '11.2.6',
    '10.11': '10.11.11',
    '10.6': '10.6.21',
  },
  nginxVersion: {
    '1.28': '1.28.0',
    '1.27': '1.27.4',
    '1.26': '1.26.3',
  },
  apacheVersion: {
    '2.4': '2.4.66',
    '2.4.62': '2.4.62',
    '2.4.66': '2.4.66',
  },
  redisVersion: {
    '7.2': '7.2.4',
  },
  memcachedVersion: {
    '1.6': '1.6.22',
  },
  mailpitVersion: {
    '1.22': '1.22.3',
  },
  postgresqlVersion: {
    '17': '17.4',
    '16': '16.8',
    '15': '15.12',
  },
};

function normalizeSettingsVersions(s: LStackSettings): LStackSettings {
  const next = { ...s } as Record<string, unknown>;
  for (const [key, aliases] of Object.entries(VERSION_NORMALIZERS)) {
    const current = next[key];
    if (typeof current === 'string' && aliases[current]) {
      next[key] = aliases[current];
    }
  }
  return next as unknown as LStackSettings;
}

// ─── Globals ──────────────────────────────────────────────────────────────────
let mainWindow: BrowserWindow | null = null;
let tray: Tray | null = null;
let settings: LStackSettings = defaultSettings;
let serviceManager: ServiceManager;
let packageManager: PackageManager;
let vhostManager: VHostManager;
let terminalManager: TerminalManager;
let isQuitting = false;

// ─── Init Data Directories ────────────────────────────────────────────────────
async function initDataDirs() {
  await fs.ensureDir(DATA_DIR);
  await fs.ensureDir(BIN_DIR);
  await fs.ensureDir(WWW_DIR);
  await fs.ensureDir(ETC_DIR);
  await fs.ensureDir(path.join(ETC_DIR, 'nginx', 'sites-enabled'));
  await fs.ensureDir(path.join(ETC_DIR, 'apache2', 'sites-enabled'));
  await fs.ensureDir(path.join(ETC_DIR, 'ssl'));
  await fs.ensureDir(path.join(ETC_DIR, 'apps', 'phpmyadmin'));
  await fs.ensureDir(LOGS_DIR);
  await fs.ensureDir(DB_DIR);

  // Create default www/index.php — LStack dashboard
  const indexFile = path.join(WWW_DIR, 'index.php');
  if (!await fs.pathExists(indexFile)) {
    await fs.writeFile(indexFile, LOCALHOST_HOMEPAGE);
  }
}

// ─── Load / Save Settings ─────────────────────────────────────────────────────
async function loadSettings(): Promise<LStackSettings> {
  try {
    if (await fs.pathExists(SETTINGS_FILE)) {
      const saved = await fs.readJson(SETTINGS_FILE);
      const merged: LStackSettings = { ...defaultSettings, ...saved };
      // Migrate .devstack → .lstack paths
      if (merged.dataDir && merged.dataDir.includes('.devstack')) {
        merged.dataDir = merged.dataDir.replace('.devstack', '.lstack');
      }
      if (merged.wwwDir && merged.wwwDir.includes('.devstack')) {
        merged.wwwDir = merged.wwwDir.replace('.devstack', '.lstack');
      }
      if (merged.logsDir && merged.logsDir.includes('.devstack')) {
        merged.logsDir = merged.logsDir.replace('.devstack', '.lstack');
      }
      if (merged.binDir && merged.binDir.includes('.devstack')) {
        merged.binDir = merged.binDir.replace('.devstack', '.lstack');
      }
      return normalizeSettingsVersions(merged);
    }
  } catch {
    // ignore, use defaults
  }
  return normalizeSettingsVersions(defaultSettings);
}

async function saveSettings(s: LStackSettings) {
  await fs.ensureDir(DATA_DIR);
  await fs.writeJson(SETTINGS_FILE, s, { spaces: 2 });
}

// ─── Create Window ────────────────────────────────────────────────────────────
function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 760,
    minWidth: 900,
    minHeight: 600,
    backgroundColor: '#0f172a',
    titleBarStyle: 'hidden',
    titleBarOverlay: false,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: false,
    },
    icon: app.isPackaged
      ? path.join(process.resourcesPath, 'icon.png')
      : path.join(__dirname, '../icon.png'),
    show: false,
  });

  if (VITE_DEV_SERVER_URL) {
    mainWindow.loadURL(VITE_DEV_SERVER_URL);
  } else {
    mainWindow.loadFile(
      path.join(__dirname, '../dist/index.html')
    );
  }

  mainWindow.once('ready-to-show', () => {
    mainWindow?.show();
  });

  mainWindow.on('close', (e) => {
    if (!isQuitting) {
      e.preventDefault();
      app.quit();
    }
  });

  return mainWindow;
}

// ─── System Tray ─────────────────────────────────────────────────────────────
function createTray() {
  try {
    const iconPath = app.isPackaged
      ? path.join(process.resourcesPath, 'icon.png')
      : path.join(__dirname, '../icon.png');
    const icon = fs.existsSync(iconPath)
      ? nativeImage.createFromPath(iconPath).resize({ width: 16, height: 16 })
      : nativeImage.createEmpty();

    tray = new Tray(icon);
    tray.setToolTip('LStack');

    const contextMenu = Menu.buildFromTemplate([
      { label: 'Open LStack', click: () => mainWindow?.show() },
      { type: 'separator' },
      {
        label: 'Start All Services',
        click: () => serviceManager?.startAll(),
      },
      {
        label: 'Stop All Services',
        click: () => serviceManager?.stopAll(),
      },
      { type: 'separator' },
      { label: 'Open www folder', click: () => shell.openPath(settings.wwwDir) },
      { type: 'separator' },
      { label: 'Quit LStack', click: () => { app.quit(); } },
    ]);

    tray.setContextMenu(contextMenu);
    tray.on('double-click', () => mainWindow?.show());
  } catch (err) {
    console.log('Failed to create tray (might be unsupported on this Linux DE):', err);
  }
}

// ─── App Lifecycle ────────────────────────────────────────────────────────────
app.whenReady().then(async () => {
  await initDataDirs();
  settings = await loadSettings();

  // Ensure dirs from saved settings also exist
  await fs.ensureDir(settings.wwwDir);
  await fs.ensureDir(settings.binDir);

  // Resource paths (templates, packages.json)
  const resourcesDir = app.isPackaged
    ? path.join(process.resourcesPath, 'resources')
    : path.join(__dirname, '../../resources');

  // Init core managers
  serviceManager = new ServiceManager(settings, (log) => {
    if (mainWindow && !mainWindow.isDestroyed()) {
      mainWindow.webContents.send('service:log', log);
      mainWindow.webContents.send('service:statusUpdate', serviceManager.getStatuses());
    }
  });

  await serviceManager.cleanupOrphanedProcesses();

  packageManager = new PackageManager(
    settings.binDir,
    resourcesDir,
    settings.dataDir,
    (progress) => {
      if (mainWindow && !mainWindow.isDestroyed()) {
        mainWindow.webContents.send('package:progress', progress);
      }
    },
    (data) => {
      if (mainWindow && !mainWindow.isDestroyed()) {
        mainWindow.webContents.send('package:install:raw', data);
      }
    }
  );

  const certManager = new CertManager(path.join(ETC_DIR, 'ssl'));
  await certManager.ensureCACert();

  vhostManager = new VHostManager(settings, resourcesDir, (log) => {
    if (mainWindow && !mainWindow.isDestroyed()) {
      mainWindow.webContents.send('service:log', log);
    }
  }, () => {
    // Reload webserver config when a vhost is added/removed
    const svc = settings.webserver === 'apache' ? 'apache' : 'nginx';
    serviceManager?.reloadConfig(svc).catch(() => {});
  }, certManager);

  // Init terminal manager
  terminalManager = new TerminalManager(
    (id, data) => {
      if (mainWindow && !mainWindow.isDestroyed()) {
        mainWindow.webContents.send('terminal:data', id, data);
      }
    },
    (id) => {
      if (mainWindow && !mainWindow.isDestroyed()) {
        mainWindow.webContents.send('terminal:exit', id);
      }
    },
  );

  // Generate nginx.conf — find any installed phpMyAdmin version for dedicated phpmyadmin.test server block
  let pmaDir = path.join(WWW_DIR); // fallback: www root (no pma alias)
  for (const ver of ['6.0-snapshot', '5.2.3', '5.2.2']) {
    const candidate = packageManager.getInstallPath('phpmyadmin', ver);
    if (await fs.pathExists(candidate)) {
      pmaDir = candidate;
      break;
    }
  }
  await vhostManager.generateNginxMainConf(pmaDir).catch(() => {});

  // Restore per-project PHP-FPM processes from vhosts.json
  await vhostManager.restorePhpFpmProcesses().catch(() => {});

  // Register IPC handlers
  registerIpcHandlers({
    ipcMain,
    settings,
    saveSettings,
    serviceManager,
    packageManager,
    vhostManager,
    certManager,
    terminalManager,
    shell,
    dialog,
    mainWindow: () => mainWindow,
  });

  createWindow();
  createTray();

  // Auto start services
  if (settings.autoStartServices) {
    await serviceManager.startAll();
  }

  // Watch www/ for new project folders → auto VHost
  if (settings.autoVirtualHost) {
    vhostManager.watch();
  }

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('second-instance', () => {
  if (mainWindow) {
    if (mainWindow.isMinimized()) mainWindow.restore();
    mainWindow.show();
    mainWindow.focus();
  }
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    // Don't quit — keep running in tray
  }
});

app.on('before-quit', (e) => {
  if (isQuitting) return;
  e.preventDefault();
  isQuitting = true;

  (async () => {
    try {
      await serviceManager?.stopAll();
    } catch { /* ignore */ }
    vhostManager?.unwatch();
    terminalManager?.killAll();
    tray?.destroy();
    app.exit(0);
  })();
});

// ─── Localhost Homepage ───────────────────────────────────────────────────────
const LOCALHOST_HOMEPAGE = `<?php
$phpVersion = PHP_VERSION;
$extensions = get_loaded_extensions();
sort($extensions);
$important = ['mysqli', 'pdo_mysql', 'mbstring', 'gd', 'curl', 'zip', 'openssl', 'intl', 'opcache'];

// Try MariaDB / MySQL connection
$dbOk = false; $dbVersion = 'Offline';
try {
  $pdo = @new PDO('mysql:host=127.0.0.1;port=3306', 'root', '', [PDO::ATTR_TIMEOUT => 2]);
  $dbOk = true;
  $r = $pdo->query('SELECT VERSION()');
  $dbVersion = $r ? (string)$r->fetchColumn() : 'Unknown';
} catch (Exception $e) {}

// List project folders in www/
$projects = [];
foreach (scandir(__DIR__) ?: [] as $d) {
  if ($d !== '.' && $d !== '..' && is_dir(__DIR__ . '/' . $d)) $projects[] = $d;
}

// Detect domain suffix from HTTP_HOST
$host   = $_SERVER['HTTP_HOST'] ?? 'localhost';
$domain = (substr_count($host, '.') >= 1) ? explode('.', $host, 2)[1] : 'test';
$port   = $_SERVER['SERVER_PORT'] ?? '80';
$baseUrl = 'http://localhost.test' . ($port !== '80' ? ':' . $port : '');
$pmaUrl = 'http://phpmyadmin.test' . ($port !== '80' ? ':' . $port : '');
?><!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>LStack — Local Development</title>
<style>
:root{--bg:#0f172a;--bg-soft:#111c33;--card:#1e293b;--card-soft:rgba(30,41,59,.72);--border:#334155;--border-strong:#475569;--text:#f1f5f9;--muted:#94a3b8;--blue:#60a5fa;--blue-strong:#2563eb;--green:#22c55e;--red:#ef4444;--shadow:0 20px 45px rgba(2,6,23,.45)}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:radial-gradient(circle at top,#172554 0,#0f172a 28%,#0f172a 100%);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;min-height:100vh;line-height:1.5}
a{color:inherit;text-decoration:none}
body:before{content:'';position:fixed;inset:0;background:linear-gradient(180deg,rgba(96,165,250,.06),transparent 22%,transparent);pointer-events:none}
.page{position:relative;max-width:1180px;margin:0 auto;padding:32px 20px 56px}
.hero{display:flex;align-items:flex-start;justify-content:space-between;gap:24px;margin-bottom:28px;padding:24px;border:1px solid rgba(71,85,105,.45);border-radius:24px;background:linear-gradient(180deg,rgba(30,41,59,.92),rgba(15,23,42,.92));box-shadow:var(--shadow);backdrop-filter:blur(10px)}
.hero-main{display:flex;align-items:flex-start;gap:16px;min-width:0}
.logo{width:56px;height:56px;border-radius:18px;display:flex;align-items:center;justify-content:center;font-size:26px;flex-shrink:0;background:linear-gradient(135deg,rgba(59,130,246,.24),rgba(14,165,233,.14));border:1px
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
