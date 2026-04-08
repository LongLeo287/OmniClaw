---
id: repo-fetched-animestudio-051127
type: knowledge
owner: OA
registered_at: 2026-04-05T03:14:47.173947
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_AnimeStudio_051127

## Assimilation Report
Auto-cloned repository: FETCHED_AnimeStudio_051127

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Anime Studio
## Asset extraction tool for unity games !

![image](https://github.com/user-attachments/assets/fc1decdc-a589-43a2-b965-2d8151d0975f)

---

# How do I use this ?

You should look at the [official wiki](https://github.com/Escartem/AnimeStudio/wiki), if required look at the [original tutorial by Modder4869](https://gist.github.com/Modder4869/0f5371f8879607eb95b8e63badca227e) or the [original readme](https://github.com/RazTools/Studio/blob/main/README.md). Otherwise [join the discord](https://discord.gg/fzRdtVh) and ask there !

---

# How do I download this ?

## [Download Studio for .NET 9 (recommended ✨)](https://nightly.link/Escartem/AnimeStudio/workflows/build/master/AnimeStudio-net9.zip) or [Download Studio for .NET 8](https://nightly.link/Escartem/AnimeStudio/workflows/build/master/AnimeStudio-net8.zip)

---

# What is this ?

It's an up-to-date fork of Razmoth's one. After his repo was discontinued, bugs started to arise as games evolved, and people started making forks to fix some of them, but each one would not support the fixes by the others and so on. This version aims at being the new start base for AssetStudio, renamed as AnimeStudio, it supports all 3 main hoyo games, and is open to any contribution !

---

# What changed ?

This is a non-exhaustive list of modifications :
- Removed usage of a [certain dll for a certain decryption](https://github.com/Escartem/AnimeStudio/commit/1fcfa9041e07cd0a98b4d23f1578e910256fa1f8) 👀
- Merged fixes for Genshin, Star Rail and ZZZ suport with improvements
- Dark mode
- Reorganised menu bar for easier usage
- Addes SHA256 hash for assets
- New game selector merged with UnityCN keys list and updated UnityCN keys manager
- Asset Browser improvements
    - It is now possible to use json files instead of only message pack
    - You can now relocate the sources files of a map instead of having to build a new one to adjust them, making maps no longer game install dir dependant
    - Only selected assets are displayed in the main window when loading instead of the full blocks
    - You can load 2 asset maps at once and view the difference between both

---

Special thanks to:
- [hrothgar](https://github.com/hrothgar234567): Help in ZZZ fixes & some dll RE
- Razmoth: Original AssetStudio for anime games support - [[project](https://github.com/RazTools/Studio)]
- hashblen: ZZZ fixes fork - [[project](https://github.com/hashblen/ZZZ_Studio)]
- yarik0chka: Genshin and Star Rail fixes fork - [[project](https://github.com/yarik0chka/YarikStudio)]
- aelurum: AssetStudioMod - [[project](https://github.com/aelurum/AssetStudio)]
- Perfare: The real original AssetStudio - [[project](https://github.com/perfare/AssetStudio)]
- All of the others contributor of Razmoth's Studio

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for animestudio
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Version**
For example `v1.00.00+9ad92309466f5c929f16d9aa41ddbb6c5e596a3a`.

**Unity Version**
For example `2017.4.30f1`.

**Game/Sample**
Name or download link of the game, or a bunch of sample files used to reproduce the issue.

**Additional context**
Add any other context about the problem here.

```

### File: .github\ISSUE_TEMPLATE\feature_request.md
```md
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: ''
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.

# Note: Game decryption requests will not be accepted.

```

