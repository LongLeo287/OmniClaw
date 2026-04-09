# Vault Directory Identity

This directory serves as the strictly local storage for sensitive system data, personal memories, and heavy binary assets that are not intended for public distribution via Git.

## 🔒 Security Policy
- **Tracking Restriction**: Only structural templates (like this file) and public-facing media assets (`assets/media/`) are authorized for Git tracking.
- **Data Isolation**: All databases (`.sqlite`, `.db`), local agent memories (`brain/`), and model weights must remain strictly within this local boundary.
- **Deep Cleaner Compliance**: This directory is monitored by the OmniClaw Deep Cleaner for secret leakage and cleanup.

## 📂 Sub-directory Map
- **archives/**: Legacy data and compressed backups (Local Only).
- **assets/**: Media and data assets (Media are Git-whitelisted).
- **models/**: Local LLM weights and artifacts (Local Only).
- **quarantine/**: Isolated files for security vetting (Local Only).
- **tmp/**: Ephemeral session data (Local Only).
