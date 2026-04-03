---
id: imnoob59-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:53.083345
---

# KNOWLEDGE EXTRACT: imnoob59
> **Extracted on:** 2026-03-30 17:38:09
> **Source:** imnoob59

---

## File: `crotmail.md`
```markdown
# 📦 imnoob59/crotmail [🔖 PENDING/APPROVE]
🔗 https://github.com/imnoob59/crotmail
🌐 https://github.com/imnoob59/crotmail

## Meta
- **Stars:** ⭐ 33 | **Forks:** 🍴 23
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Disposable email service with Cloudflare Workers

## README (trích đầu)
```
# CrotMail

Disposable email service berbasis Cloudflare Workers, dirancang untuk alur signup/verifikasi yang cepat tanpa membebani email utama.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Stars](https://img.shields.io/github/stars/imnoob59/crotmail?style=social)](https://github.com/imnoob59/crotmail/stargazers)

- Website: https://crotmail.app
- Repository: https://github.com/imnoob59/crotmail

## Quick Start (10 Menit)

Panduan cepat untuk menjalankan deploy pertama via Wrangler CLI.

### Prasyarat

- Node.js 18+
- Akun Cloudflare
- Domain yang sudah aktif di Cloudflare (untuk email routing)

### Langkah Cepat

1. Install dependensi project:

```bash
npm install
```

2. Login ke Cloudflare via Wrangler:

```bash
npx wrangler login
```

3. Buat D1 dan KV (sekali saja):

```bash
npx wrangler d1 create crot-mail-db
npx wrangler kv namespace create MAIL_KV
```

4. Salin template config publik lalu isi ID resource:

```bash
cp wrangler.clean.toml wrangler.toml
```

Lalu masukkan ID hasil perintah D1/KV ke file tersebut.

5. Set environment variable minimum di `wrangler.toml` atau dashboard:

```env
ACCESS_KEY=ganti-dengan-key-anda
MAIL_DOMAINS=mail1.example.com,mail2.example.com
EXPIRE_MINUTES=43200
MESSAGE_RETENTION_DAYS=1
```

Set `ACCESS_KEY` sebagai secret (bukan plaintext di file):

```bash
npx wrangler secret put ACCESS_KEY
```

6. Jalankan migration schema D1 remote:

```bash
npx wrangler d1 execute crot-mail-db --remote --file schema.sql
```

7. Deploy ke production:

```bash
npm run deploy
```

8. Verifikasi endpoint domain:

```bash
curl -H "X-Access-Key: ACCESS_KEY_ANDA" https://your-domain.com/api/domains
```

Jika domain list sudah keluar, lanjutkan setup Email Routing agar inbox bisa menerima email masuk.

## Highlight Fitur

- Inbox instan dengan random address atau custom username
- Dukungan multi-domain dari variabel `MAIL_DOMAINS`
- Masa aktif inbox default 30 hari (`EXPIRE_MINUTES=43200`)
- Auto cleanup pesan default 1 hari (`MESSAGE_RETENTION_DAYS=1`)
- Resume inbox via kode unik 8 karakter
- Scope auth:
   - `full`: bisa create/extend/delete inbox dan kelola pesan
   - `limited`: mode resume, hanya baca dan hapus pesan
- Admin delete mailbox by address (via access key)
- Web UI modern (`/app`) + public landing page (`/`)
- Browser extension support untuk alur tempmail harian

## Arsitektur

### Backend

- Cloudflare Workers
- Cloudflare D1 (SQLite)
- Cloudflare KV
- JWT authentication (`full` dan `limited` scope)

### Frontend

- Vue 3
- Vite
- Tailwind CSS
- Pinia

## Endpoint Penting

- `POST /api/generate` buat inbox random
- `POST /api/custom` buat inbox custom
- `POST /api/token` login inbox (full mode)
- `POST /api/resume` login via resume code (limited mode)
- `DELETE /api/accounts/{id}` hapus inbox milik session aktif
- `POST /api/admin/delete-account` admin hapus inbox by address (pakai `X-Access-Key`)

Dokumentasi lengkap ada di [API.md](./API.md).

## Konfigurasi Environment


```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

