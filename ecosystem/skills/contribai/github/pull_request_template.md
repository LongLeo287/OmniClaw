## Description
<!-- What does this PR do? Why is it needed? -->

## Type
- [ ] `feat` – New feature
- [ ] `fix` – Bug fix
- [ ] `refactor` – Code restructuring
- [ ] `docs` – Documentation
- [ ] `test` – Tests
- [ ] `perf` – Performance
- [ ] `chore` – Maintenance

## Changes
<!-- List the key changes made -->

## Architecture Area
<!-- Which v2.5.0 component does this touch? -->
- [ ] Middleware chain (`core/middleware.py`)
- [ ] Analysis / Skills (`analysis/analyzer.py`, `analysis/skills.py`)
- [ ] Sub-agents (`agents/registry.py`)
- [ ] Tools (`tools/protocol.py`)
- [ ] Memory / Learning (`orchestrator/memory.py`)
- [ ] PR Patrol (`pr/patrol.py`)
- [ ] Pipeline (`orchestrator/pipeline.py`)
- [ ] Other: <!-- specify -->

## Pre-submit Checklist

> **⚠️ CI will auto-run on your PR. Please verify locally before pushing.**

- [ ] `ruff check contribai/` passes (lint)
- [ ] `ruff format --check contribai/ tests/` passes (format)
- [ ] `pytest tests/ -v` passes (356+ tests)
- [ ] Code follows project conventions (async, type hints, Google docstrings)
- [ ] `from __future__ import annotations` at top of new files
- [ ] No hardcoded secrets
- [ ] DCO signoff on all commits (`git commit -s`)

## Related Issues
<!-- Closes #123 -->
