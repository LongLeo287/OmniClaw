---
id: spec
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:16.180230
---

## ADDED Requirements

### Requirement: Linux Multi-Architecture Release Artifacts
The system SHALL produce Linux x64 and arm64 release artifacts, including `.deb`, `.rpm`, and `.AppImage`.

#### Scenario: Linux x64 artifact generation
- **WHEN** building a release on Linux x64
- **THEN** release assets include x64 `.deb`, `.rpm`, and `.AppImage` files

#### Scenario: Linux arm64 artifact generation
- **WHEN** building a release on Linux arm64
- **THEN** release assets include arm64 `.deb`, `.rpm`, and `.AppImage` files

### Requirement: macOS Multi-Architecture and Universal dmg
The system SHALL produce macOS x64, arm64, and universal dmg artifacts in release builds.

#### Scenario: macOS x64/arm64 dmg generation
- **WHEN** building releases for macOS x64 and arm64
- **THEN** release assets include dmg files for each corresponding architecture

#### Scenario: macOS universal dmg generation
- **WHEN** running a universal build
- **THEN** release assets include a universal dmg

### Requirement: Parallel Windows MSI and Squirrel Artifacts
The system SHALL generate both Squirrel installer artifacts and MSI artifacts in Windows release builds.

#### Scenario: Windows MSI generation
- **WHEN** building a release on Windows x64
- **THEN** release assets include both `.exe` installer and `.msi` artifacts

### Requirement: Artifact Naming and SHA-256 Output
The system SHALL output SHA-256 checksums for all release artifacts and use a unified naming convention that includes architecture markers.

#### Scenario: Artifact naming includes version and architecture
- **WHEN** generating release artifacts
- **THEN** artifact names include `productName`, `version`, and `arch` identifiers

#### Scenario: SHA-256 checksum output
- **WHEN** release artifact generation finishes
- **THEN** release assets include SHA-256 checksums for corresponding artifacts
