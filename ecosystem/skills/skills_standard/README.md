---
id: readme
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:24.641473
---

# Agent Skills Registry

This directory contains the source of truth for all AI agent skills. Skills are organized by **Category** (Language or Framework) and then by **Domain**.

## 📂 Structure

Each skill must follow the standard directory structure:
`skills/{category}/{skill-name}/SKILL.md`

## 🛠 Active Categories

### 🌐 Common (Universal)

Cross-framework standards and best practices applicable to all development.


### �🎯 Flutter (Framework)

High-density standards for modern Flutter development.


### 🔷 Dart (Language)

Core language idioms and patterns.


### 🔷 TypeScript (Language)

Modern TypeScript standards for type-safe development.


### 🟨 JavaScript (Language)

Modern JavaScript (ES2022+) patterns.


### ⚛️ React (Framework)

Modern React development patterns.


### 📱 React Native (Framework)

Mobile app standards for iOS and Android.


### 🦁 NestJS (Framework)

Enterprise-grade Node.js backend development.


### ▲ Next.js (Framework)

Modern fullstack React framework standards (App Router).


### 🐘 Laravel (Framework)

Expert standards for scalable Laravel 11.x/12.x applications.


---

## ✍️ Contribution Guide

To add or update a skill:

1. **Token Efficiency**: `SKILL.md` must be **≤ 100 lines**. This is a strict limit to maximize agent context.
2. **Progressive Disclosure**: Move all code samples > 10 lines to `references/REFERENCE.md` or specialized reference files.
3. **Imperative Standards**: Use "Compressed Syntax" (starting with verbs, minimal articles) for 40% higher density.
4. **Format Verification**: Ensure YAML frontmatter triggers are precise and categories are lowercase kebab-case.
5. **Validation Checklist**:
   - [ ] SKILL.md ≤ 100 lines (Ideal: 60-80)
   - [ ] No inline code blocks > 10 lines
   - [ ] No redundant frontmatter context in body
   - [ ] Triggers verified for all supported agents
6. **Priority Matrix**:
   - **P0**: Foundational (Architecture, Types, Security).
   - **P1**: Operational (Performance, Idioms, UI).
   - **P2**: Maintenance (Testing, Tooling, Docs).
