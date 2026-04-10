---
id: design
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:18.332201
---

## Context
The existing Electron Forge packaging pipeline needs Linux arm64, macOS universal, and Windows MSI outputs, plus consistent artifact naming and SHA-256 checksum outputs for cross-platform release parity.

## Goals / Non-Goals
- Goals:
  - Cover Linux arm64 artifacts (`deb`/`rpm`/`AppImage`)
  - Provide macOS `x64`/`arm64`/`universal` dmg artifacts
  - Add MSI artifacts for Windows
  - Include architecture markers in artifact names and output SHA-256 checksums
- Non-Goals:
  - Change existing update logic (`latest*.yml` remains unchanged)
  - Modify runtime application behavior

## Decisions
- Decision: Build Linux arm64 on a dedicated arm64 runner, without cross-compilation.
- Decision: Build macOS universal via `--arch=universal` or by merging app bundles before dmg packaging.
- Decision: Generate Windows MSI with the official Forge maker (Wix/MSI) in parallel with Squirrel.
- Decision: Use `productName + version + arch` naming; Linux uses `amd64/aarch64`, macOS/Windows use `x64/arm64/universal`.

## Alternatives Considered
- x64-only artifacts: rejected because it does not meet user requirements.
- universal-only dmg: rejected due to weaker debugging/rollback capability and lack of architecture distinction.

## Risks / Trade-offs
- Linux arm64 builds may be affected by native dependency compilation (for example, `better-sqlite3`, `keytar`).
- Windows MSI requires extra tooling (Wix), which may increase CI duration and failure rate.
- The universal dmg pipeline requires validation for signing and update-flow consistency.

## Migration Plan
1) Introduce CI multi-arch jobs with naming and checksum outputs.
2) Add MSI maker and universal dmg packaging.
3) Stabilize the workflow after release validation.

## Open Questions
- Should artifact naming strictly match sample format (underscore vs hyphen)?
- Should checksum output be separate `.sha256` files or a single consolidated manifest?
