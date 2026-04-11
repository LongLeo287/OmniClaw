---
id: project-overview-template
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.504354
---

# {{project_name}} - Project Overview

**Date:** {{date}}
**Type:** {{project_type}}
**Architecture:** {{architecture_type}}

## Executive Summary

{{executive_summary}}

## Project Classification

- **Repository Type:** {{repository_type}}
- **Project Type(s):** {{project_types_list}}
- **Primary Language(s):** {{primary_languages}}
- **Architecture Pattern:** {{architecture_pattern}}

{{#if is_multi_part}}

## Multi-Part Structure

This project consists of {{parts_count}} distinct parts:

{{#each project_parts}}

### {{part_name}}

- **Type:** {{project_type}}
- **Location:** `{{root_path}}`
- **Purpose:** {{purpose}}
- **Tech Stack:** {{tech_stack}}
  {{/each}}

### How Parts Integrate

{{integration_description}}
{{/if}}

## Technology Stack Summary

{{#if is_single_part}}
{{technology_table}}
{{else}}
{{#each project_parts}}

### {{part_name}} Stack

{{technology_table}}
{{/each}}
{{/if}}

## Key Features

{{key_features}}

## Architecture Highlights

{{architecture_highlights}}

## Development Overview

### Prerequisites

{{prerequisites}}

### Getting Started

{{getting_started_summary}}

### Key Commands

{{#if is_single_part}}

- **Install:** `{{install_command}}`
- **Dev:** `{{dev_command}}`
- **Build:** `{{build_command}}`
- **Test:** `{{test_command}}`
  {{else}}
  {{#each project_parts}}

#### {{part_name}}

- **Install:** `{{install_command}}`
- **Dev:** `{{dev_command}}`
  {{/each}}
  {{/if}}

## Repository Structure

{{repository_structure_summary}}

## Documentation Map

For detailed information, see:

- [index.md](./index.md) - Master documentation index

---

_Generated using BMAD Method `document-project` workflow_
