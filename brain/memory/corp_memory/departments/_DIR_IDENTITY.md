---
id: memory_corp_departments
type: department_memory_roster
namespace: brain.memory.corp_memory.departments
owner: OSF_Daemon
status: standard_v5
description: "Aggregated Long-Term Memory (System B) ledgers for 22 Corporate Departments."
registered_by: OA_Auditor
---

# `corp_memory/departments` Identity (Department Ledgers)

> [!CAUTION]  
> **OSF DAEMON SECURITY WATERMARK**  
> This directory tracks the highest-level strategic learning constraints for entire simulated Departments (Engineering, QA, Legal, etc.).
> - Individual agent memory logs go to `corp_memory/agents/`.
> - Scaled operations lessons go here.

## 1. Directory Purpose
Each `.md` file represents the "Institutional Memory" of one logical department. Head Agents (C-Suite or Directors) aggregate lessons, count their active workforce, and maintain inter-departmental dependencies within these files.

## 2. Compliance Rules
- Because these files update dynamically based on daily cycles, they are classified as **Volatile Cache**.
- By `.gitignore` Rule 12, all department ledgers (except the `<template>.md`) are blocked from GitHub sync to prevent repository congestion.