# Changelog

Semua perubahan penting pada project ini akan didokumentasikan di file ini.

Format mengikuti prinsip Keep a Changelog.

## [Unreleased]

### Added

- Placeholder untuk perubahan yang belum dirilis.

## [2026-03-22]

### Added

- Resume access code 8 karakter dengan mode auth `limited`.
- Admin endpoint untuk hapus mailbox by address (`POST /api/admin/delete-account`).
- Landing page publik (`/`) dan app route (`/app`).
- Quick Start dan deploy guide yang lebih detail di README.
- Dokumen standar open-source: CONTRIBUTING, SECURITY, CODE_OF_CONDUCT, LICENSE.

### Changed

- Default expiry inbox menjadi 30 hari (`EXPIRE_MINUTES=43200`).
- Retensi pesan default menjadi 1 hari (`MESSAGE_RETENTION_DAYS=1`).
- Peningkatan UI web app dan extension untuk alur tempmail.

### Fixed

- Perbaikan fallback SPA untuk route resume (`/r/:code`).
- Perbaikan alur akses extension saat token inbox expired.
