---
id: quasipet_pokedex
type: plugin
version: 1.0.0
owner: OmniClaw Ecosystem
description: "Virtual Pet Companion System (Pokedex) with RNG Stat generation and Agent Affinity."
tags:
  - ux
  - easter-egg
  - companion
---

# OmniPets Pokedex Plugin

This directory contains the master registry, stat generator, and ASCII frame data for all Virtual Companions in the OmniClaw operating system.

### Components:
- `pokedex.py`: The master database mapping Pet IDs to their specialties, stat coefficients, and visual frames.
- `pet_summoner.py`: Engine to cast the Gacha roll (calculating IVs) and print the Pet's Stat Card.
