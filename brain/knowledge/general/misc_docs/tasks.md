---
id: tasks
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:21.077770
---

## 1. Implementation
- [x] 1.1 Update the release workflow matrix to add Linux arm64 builds and split build steps by architecture.
- [x] 1.2 Add macOS universal build flow (merge app bundles before generating universal dmg).
- [x] 1.3 Introduce Windows MSI maker and required dependencies, and generate MSI in the Windows job.
- [x] 1.4 Extend `postMake` artifact renaming and architecture mapping logic to generate SHA-256 checksum files.
- [ ] 1.5 Update release attachments and artifact inventory documentation (if needed).
- [ ] 1.6 Verify CI outputs for Linux arm64, macOS universal, and Windows MSI.
