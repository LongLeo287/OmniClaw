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

Atur variabel berikut di Worker:

| Variable | Required | Keterangan |
|---|---|---|
| `ACCESS_KEY` | Yes | Access key utama untuk operasi sensitif/admin |
| `MAIL_DOMAINS` | Yes | Daftar domain inbox, pisahkan koma |
| `EXPIRE_MINUTES` | No | Default umur inbox (menit), default `43200` |
| `MESSAGE_RETENTION_DAYS` | No | Retensi pesan (hari), default `1` |

## Deploy (Cloudflare)

### Opsi A. Deploy via GitHub (Cloudflare Dashboard)

#### 1. Connect repository

1. Buka Cloudflare Workers and Pages.
2. Pilih Create dan Connect to Git.
3. Pilih repository GitHub `imnoob59/crotmail`.
4. Build command: `npm run build` (jika diminta).
5. Deploy project.

#### 2. Buat resource cloud

Di Cloudflare Dashboard, buat:

- 1 D1 Database
- 1 KV Namespace

#### 3. Tambahkan bindings ke Worker

Masuk ke Worker -> Settings -> Bindings, lalu tambahkan:

- D1 binding name: `DB` (pilih database D1 yang dibuat)
- KV binding name: `MAIL_KV` (pilih namespace KV yang dibuat)

#### 4. Tambahkan environment variables

Masuk ke Worker -> Settings -> Variables dan isi:

- `ACCESS_KEY` (required)
- `MAIL_DOMAINS` (required)
- `EXPIRE_MINUTES` (optional, default `43200`)
- `MESSAGE_RETENTION_DAYS` (optional, default `1`)

#### 5. Jalankan schema migration ke D1

Meskipun deploy via GitHub, schema tetap perlu dijalankan ke D1:

```bash
npx wrangler login
npx wrangler d1 execute <NAMA_DB_D1> --remote --file schema.sql
```

#### 6. Verifikasi deploy

1. Buka URL production Worker.
2. Pastikan endpoint `GET /api/domains` merespons.
3. Coba create inbox dari web UI (`/app`) atau endpoint API.

### Opsi B. Deploy Manual via Wrangler CLI

#### 1. Install dependency project

```bash
npm install
```

#### 2. Login Wrangler

```bash
npx wrangler login
```

#### 3. Buat resource Cloudflare (jika belum ada)

```bash
npx wrangler d1 create crot-mail-db
npx wrangler kv namespace create MAIL_KV
```

Simpan `database_id` dan `kv namespace id`, lalu masukkan ke `wrangler.clean.toml` (atau hasil copy-nya ke `wrangler.toml`).

#### 4. Binding worker

Gunakan binding berikut di file config Wrangler (`wrangler.clean.toml` / `wrangler.toml`):

- D1 binding name: `DB`
- KV binding name: `MAIL_KV`

#### 5. Konfigurasi environment variable

Set minimum variable berikut di file config atau dashboard:

- `ACCESS_KEY`
- `MAIL_DOMAINS`
- `EXPIRE_MINUTES` (opsional)
- `MESSAGE_RETENTION_DAYS` (opsional)

Untuk keamanan, simpan `ACCESS_KEY` sebagai secret:

```bash
npx wrangler secret put ACCESS_KEY
```

#### 6. Jalankan migrasi schema ke D1 (remote)

```bash
npx wrangler d1 execute crot-mail-db --remote --file schema.sql
```

#### 7. Deploy worker

```bash
npm run deploy
```

#### 8. Verifikasi deploy

```bash
npx wrangler deployments list
```

### Setup Mail Domain (Detail)

Lakukan langkah berikut untuk setiap domain yang dipakai menerima email:

1. Pastikan domain dikelola di Cloudflare (DNS aktif di zone Cloudflare).
2. Buka `Email` -> `Email Routing` di Cloudflare Dashboard.
3. Klik `Get started` jika belum aktif.
4. Tambahkan routing rule:
    - Match: `*@domain-kamu.com`
    - Action: `Send to a Worker`
    - Worker: pilih `crot-mail`
5. Simpan rule dan pastikan statusnya active.

Catatan:

- Cloudflare biasanya akan membantu menyiapkan DNS record Email Routing (MX/SPF) saat onboarding Email Routing.
- Jika diminta verifikasi tambahan, ikuti instruksi dashboard sampai status domain siap menerima email.

### Sinkronkan `MAIL_DOMAINS`

Masukkan semua domain inbox ke env `MAIL_DOMAINS` (pisahkan dengan koma). Contoh:

```env
MAIL_DOMAINS=mail1.example.com,mail2.example.com
```

Worker akan melakukan sinkronisasi daftar domain ke tabel `domains` saat request berjalan.

### Verifikasi Setelah Deploy

Checklist cepat verifikasi domain:

1. `GET /api/domains` mengembalikan semua domain yang diharapkan.
2. `POST /api/generate` berhasil membuat inbox pada domain yang tersedia.
3. Kirim email test ke inbox tersebut dan pastikan muncul di `GET /api/messages`.

Contoh uji domain list:

```bash
curl -H "X-Access-Key: ACCESS_KEY_ANDA" https://your-domain.com/api/domains
```

### Troubleshooting Mail Domain

- Domain tidak muncul di `/api/domains`:
   - cek nilai `MAIL_DOMAINS`
   - cek deploy terbaru sudah aktif
- Email tidak masuk:
   - cek rule Email Routing masih active
   - cek target action benar-benar `Send to a Worker`
   - cek domain berada di zona Cloudflare yang benar
- API `401 Unauthorized`:
   - pastikan `X-Access-Key` sesuai `ACCESS_KEY` di Worker

## Local Development

```bash
# Jalankan dev server
npm run dev

# Build production
npm run build
```

## Public Config Policy

- Simpan config publik di [wrangler.clean.toml](./wrangler.clean.toml).
- Hindari commit secret (misalnya `ACCESS_KEY`) ke repository.
- Untuk setup production pribadi, gunakan `wrangler.toml` lokal dan simpan secret lewat Wrangler Secret.

## Open Source

CrotMail adalah open source project untuk use case disposable inbox yang praktis dan scalable.

- Maintainer: Masanto
- GitHub: https://github.com/imnoob59

## Copyright

Copyright (c) 2026 CrotMail Contributors

## License

Licensed under the [MIT License](./LICENSE).
