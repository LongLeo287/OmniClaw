---
id: acceptance-checklist
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:39.334449
---

# Device Fingerprint Capability Acceptance Checklist

## Backend Capabilities

- `get_storage_path / get_storage_dir / get_state_db_path`
- `read_profile / write_profile`
- `generate_profile`
- `sync_service_machine_id / sync_service_machine_id_from_storage`
- `load_global_original / save_global_original`
- `get_device_profiles`
- `bind_device_profile / bind_device_profile_with_profile`
- `restore_device_version / delete_device_version`
- `restore_original_device`
- `open_device_folder`

## UI Capabilities

- Show current storage / account binding / history / baseline
- Generate and bind
- Capture and bind
- Restore original fingerprint
- Restore history revision
- Delete history revision
- Open storage folder

## Switching Behavior

- Local account switching applies bound fingerprint
- Cloud account switching applies bound fingerprint
- Concurrent switch requests use queued serial semantics
- Failure semantics are fail-fast (no extra transaction orchestration)

## Compatibility Scope

- Legacy data missing optional fields: fill defaults
- Corrupted structure/type mismatch: explicit failure

## Status Marking

Please mark each item as: `Passed / Failed / Diverged (with reason)`.
