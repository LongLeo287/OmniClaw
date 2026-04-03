---
id: ublue-os-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:24.347934
---

# KNOWLEDGE EXTRACT: ublue-os
> **Extracted on:** 2026-03-30 17:56:43
> **Source:** ublue-os

---

## File: `bluefin.md`
```markdown
# 📦 ublue-os/bluefin [🔖 PENDING/APPROVE]
🔗 https://github.com/ublue-os/bluefin
🌐 https://projectbluefin.io

## Meta
- **Stars:** ⭐ 2401 | **Forks:** 🍴 253
- **Language:** Shell | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The next generation Linux workstation, designed for reliability, performance, and sustainability.

## README (trích đầu)
```
# Bluefin
*Deinonychus antirrhopus*

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2503a44c1105456483517f793af75ee7)](https://app.codacy.com/gh/ublue-os/bluefin/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/ublue-os/bluefin/badge)](https://scorecard.dev/viewer/?uri=github.com/ublue-os/bluefin)[![GTS Images](https://github.com/ublue-os/bluefin/actions/workflows/build-image-gts.yml/badge.svg)](https://github.com/ublue-os/bluefin/actions/workflows/build-image-gts.yml)[![Stable Images](https://github.com/ublue-os/bluefin/actions/workflows/build-image-stable.yml/badge.svg)](https://github.com/ublue-os/bluefin/actions/workflows/build-image-stable.yml)[![Latest Images](https://github.com/ublue-os/bluefin/actions/workflows/build-image-latest-main.yml/badge.svg)](https://github.com/ublue-os/bluefin/actions/workflows/build-image-latest-main.yml)

[<img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/ublue-os/countme/main/badge-endpoints/bluefin.json&label=Bluefin&logo=data:image%2Fpng;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAdnJLH8AAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB%2BkHDxYrIEJpLs8AAAXQSURBVFjD7ZZrbFtnGcf%2F55z3XO1jJ7ZjO7c2Sd1bmnVNM5o2tIh2mgYf6IYYk5iAsolREAMJaRI3CZAmkCYkJk0UpKBpW7VVRR0S64o2NNY1nVibdkvWdk7WS2wnji%2BxHdvpOcfnfg6fQEOwSkiJ%2BJLf9%2Bd9fh%2Be93n%2BwDrrrPN%2FhlrrBjs7H4kM7OvfF44mDsf6kgfqRAyYrZW3i6cmvnNu5g86WavGI9u%2BzX%2F2C596SZDbvxQRWMo1W5idnQHXl0L3th1HFuOXZzGDp5m1EggbA0O7eq1nmfo8ZVXyWFnKI5XqQUuKwFGbkCNyKub3HFszgZqVXhrq3b0NvudUm3bS79kINdIF17DgwQXLC22Tpy7Pr4nA%2FWNPEK7Rv%2F319PO%2FjyV2jbu6Je%2FZIOyLGg1wKxVoQghEECBE2MKqDeHm2CPJ%2BHB8%2F5bR0WGfpr9JeDZOeGHJVJV3qrcyk1ud5Sc7E6GEJIhYau%2BDRhF8dOnK5B0FDg49ThZzy2ObH9j9XYbmUjRhZgPt4ZuU55amXjkHe8XwEju6tvfvH34sMbC5TZQk0FIIvmdDWa4gHIvD1nWYug61VkG4fB0hiYMR7Ydi2yjfyP3yEwUevu%2F7T3WPjf6gs6s7wPM8bB%2BAIKJFCBzTg0cBlOvArFdA0wxc1wANAoqmwXACwIvwHQueZUBr1BBKboBRyIF3W6CD7SABHlNv%2FO3R%2FxDYEnqo%2F96ffO14Isjvl2wbqqbAjSfh16qgbQuBaASaYcAmElzThG2boAkHQmhYpgUp2gGlXIQginAsEzTLgqEZUDQN13VAKAKP9qDVKrULL7%2B79d%2F2wKGxxw%2FsOvz5v0gsZLpewbKiICnRsOabkAUOK80qiFZByNCgtHfBlOMgHgOGMIAHEIaB12qBE3g0a1WwUhDNUh69Ayn4lAfLsGBRNkTiAGr16en8C%2FV%2FCXzu3qOH9o4MviaqBUlt%2BQiEg6jV6hBTG5Av5%2BHIAVxrMnAJDYuWQZVa6IYCz%2FPA8jY4QYShtSCxBIThYTsOGNdH3%2BatcD0bhqoie2sOvRt70CyXJ0pT5WcAgBlLPSrI3vaffvozqed7wgH26rUMBlOdmLyUtof7Ikwul7tQLjVemFpQzto8f5fPUBINAsBH87YGrWVgcSaDjs4OiJIEyqcAyke1WIVEXMiMDZ8PgmEoULaBWmYeMxezP5%2B4Mv4BADDtgR3S6N6O32xKyHFHbaLRbOkdvM3emC2fDHJG%2FczZpa%2B8Of3c6fncxYkOo%2Fe5Sr5%2BwYMd0xVtAPBBcSyUpoJYNAQxIAI%2BoN1uIrtQwkgY8CkCgVCwaBYsL2DuZhEs638xpG1qVfQP3yXdUfarG9rYVoyYuJatn9sS5dpW6s2reoD9xi9eftb%2F%2BIxcnHuxDuDVL3c%2BcfrU%2Bd%2F6ewYeCzoB%2Bliyt%2F2hGOdLlKHAtmzM3VyEKAdQzZfQ32uiYOgIiQJuhxK4e2QTPnjtLcCnbwAAE5UGC0M94lZVb509ebrxY8PW3i%2FowWfOnD%2Fmf9IXnZm%2FBAAoNKatUmXqzw%2BOHfxRTKR42lBx4fyHoEMB
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

