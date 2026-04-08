---
id: phase8-tech-spec
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:20.602271
---

# Technical Specification: Phase 8 (Hardening & Scalability)

This document provides detailed technical guidance for implementing the features in Phase 8.

---

## 1. End-to-End Encryption (BM-021)
Goal: Encrypt bookmark data before saving to `chrome.storage.sync`.

### Logic Flow
1. **Initialization**: User enters passphrase through Settings.
2. **Key Derivation**: Use `PBKDF2` (with `SHA-256` and `Salt`) to generate a strong `CryptoKey` object from the passphrase.
3. **Encryption**:
   - Recommended algorithm: `AES-GCM` (256-bit).
   - Before calling `SyncService.syncChange`, JSON data will be encrypted to a byte array (Base64).
4. **Storage**: Only ciphertext and IV (Initialization Vector) are stored in the cloud.
5. **Decryption**: When pulling data from another device, prompt user to enter passphrase for local decryption.

### Technologies Used
- Web Crypto API (`window.crypto.subtle`).

---

## 2. Virtual Scrolling Implementation (BM-022)
Goal: Ensure smooth UI with 10,000+ bookmarks.

### Technical Principle
Instead of rendering all 10,000 `div`s in the DOM, only maintain about 20-30 `div`s corresponding to the visible viewport.

### Implementation Steps
1. **Fixed Item Height**: Each bookmark/folder row must have a fixed height (Example: `40px`).
2. **Container Wrapper**: A parent div with `overflow-y: auto` and total height = `count * 40px`.
3. **Dynamic Rendering**:
   - When user scrolls: Calculate `scrollTop`.
   - Determine `startIndex = Math.floor(scrollTop / 40)`.
   - Determine `endIndex = startIndex + (viewportHeight / 40)`.
4. **Render Slice**: Render only entities in the `[startIndex, endIndex]` range.
5. **Transform/Offset**: Use `transform: translateY(...)` to position items within the scroll area.

---

## 3. Automated Local Backup (BM-023)
Goal: Prevent total data loss.

### Logic
- Use `chrome.alarms` to schedule background jobs weekly.
- Task will automatically call `repo.getTree()`, convert to JSON, and save into `File System Access API` or auto-download as `.json`.

---

## 4. Technical Debt Audit (BM-024)
- **Refactoring**: Split nested callbacks (callback hell) to use `async/await`.
- **Typing**: Gradually enforce stricter typing to avoid `undefined` property access errors in bookmarks.

---
*This document is drafted to provide a Blueprint for implementing developers.*
