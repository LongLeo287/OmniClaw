---
id: repo-fetched-bot-shopee-affiliate-144300
type: knowledge
owner: OA
registered_at: 2026-04-05T04:01:27.516058
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_bot-shopee-affiliate_144300

## Assimilation Report
Auto-cloned repository: FETCHED_bot-shopee-affiliate_144300

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Shopee Affiliate Scraper

Aplikasi CLI untuk scraping dan mengelola link affiliate produk Shopee dengan mudah dan cepat.

## System Requirements

- Python 3.8 atau lebih baru
- Google Chrome browser
- Akun Shopee Affiliate

## Cara Install

### 1. Clone Repository

```bash
git clone https://github.com/botraiki/bot-shopee-affiliate.git
cd bot-shopee-affiliate
```

### 2. Buat Virtual Environment

```bash
python -m venv .venv
```

### 3. Aktifkan Virtual Environment

**Linux/macOS:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Cara Menggunakan

### Jalankan Aplikasi

```bash
python main.py
```

### Menu Utama

Setelah dijalankan, Anda akan melihat menu:

```
╭──────────────────────────────────────────────────────────╮
│                 SHOPEE AFFILIATE SCRAPER                 │
╰──────────────────────────────────────────────────────────╯

  • [1] Login ke Shopee
  • [2] Scrape Affiliate
  • [3] Muat Data dari File
  • [4] Hapus Session
  • [5] Pengaturan Filter

  • [0] Keluar
```

### Langkah-Langkah Penggunaan

#### 1. Login ke Shopee (Pertama Kali)

Pilih menu **[1]** untuk membuka browser dan login ke akun Shopee Affiliate Anda.

- Browser Chrome akan terbuka secara otomatis
- Login seperti biasa menggunakan akun Shopee Anda
- Setelah berhasil login, tekan **Enter** di terminal
- Session akan tersimpan untuk penggunaan selanjutnya

#### 2. Scrape Produk

Pilih menu **[2]** untuk mulai scraping:

- **Keyword** - Masukkan kata kunci pencarian (kosongkan jika ingin semua produk)
- **Jumlah Halaman** - Tentukan berapa halaman yang ingin di-scrape

Aplikasi akan:
1. Membuka browser dan mengakses Shopee Affiliate
2. Mengambil data produk dari setiap halaman
3. Generate link affiliate untuk setiap produk
4. Menyimpan hasil ke file JSON

#### 3. Muat Data dari File

Pilih menu **[3]** untuk memuat dan melihat data yang sudah tersimpan:

- Pilih file dari daftar yang tersedia
- Data akan difilter sesuai pengaturan
- Lihat produk dalam format tabel yang rapi

#### 4. Export Data

Setelah memuat data, Anda bisa export ke:

- **Excel (.xlsx)** - Format spreadsheet
- **CSV (.csv)** - Format universal

Anda juga bisa mengatur nama file custom saat export.

#### 5. Pengaturan Filter

Pilih menu **[5]** untuk mengatur kriteria filter produk:

| Pengaturan | Keterangan |
|------------|------------|
| Min. Komisi (%) | Persentase komisi minimum |
| Min. Jumlah Komisi | Nominal komisi dalam Rupiah |
| Min. Rating | Rating produk minimum (0-5) |
| Min. Harga | Harga produk minimum |
| Limit Produk | Jumlah produk yang ditampilkan |

## Tips Penggunaan

1. **Login Sekali** - Session akan tersimpan, tidak perlu login berulang kali
2. **Gunakan Filter** - Atur filter untuk mendapatkan produk terbaik
3. **Scrape Bertahap** - Untuk hasil lebih baik, scrape beberapa halaman sekaligus
4. **Export Rutin** - Simpan data penting ke Excel untuk referensi

## Troubleshooting

### Browser Tidak Terbuka

- Pastikan Google Chrome sudah terinstall
- Coba hapus session (menu **[4]**) lalu login ulang

### Error Saat Scraping

- Pastikan koneksi internet stabil
- Coba hapus session dan login ulang
- Kurangi jumlah halaman yang di-scrape

### Data Tidak Muncul

- Periksa pengaturan filter (mungkin terlalu ketat)
- Pastikan file JSON memiliki data yang valid

## Shortcut Keyboard

| Tombol | Fungsi |
|--------|--------|
| `Ctrl+C` | Batalkan operasi / Keluar |
| `Enter` | Konfirmasi input |

## Lisensi

MIT License - Bebas digunakan untuk keperluan pribadi dan komersial.

---

## Credits

**Created by [Botraiki](https://botraiki.biz)**

Kunjungi website kami untuk software/app/bot lainnya:
- 🌐 Website: [botraiki.biz](https://botraiki.biz)
- 🛒 Shop: [shop.botraiki.biz](https://shop.botraiki.biz)


```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for bot_shopee_affiliate
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

