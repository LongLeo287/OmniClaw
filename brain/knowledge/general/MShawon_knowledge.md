---
id: mshawon-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:09.944073
---

# KNOWLEDGE EXTRACT: MShawon
> **Extracted on:** 2026-03-30 17:43:07
> **Source:** MShawon

---

## File: `github-clone-count-badge.md`
```markdown
# 📦 MShawon/github-clone-count-badge [🔖 PENDING/APPROVE]
🔗 https://github.com/MShawon/github-clone-count-badge


## Meta
- **Stars:** ⭐ 50 | **Forks:** 🍴 39
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-14
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
GitHub clone count badge using shields.io

## README (trích đầu)
```
<p align="center">
    <img alt="ViewCount" src="https://views.whatilearened.today/views/github/MShawon/github-clone-count-badge.svg">
    <a href='https://github.com/MShawon/github-clone-count-badge'><img alt='GitHub Clones' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://gist.githubusercontent.com/MShawon/cf89f3274d06170b8a4973039aa6220a/raw/clone.json&logo=github'></a>
</p>

# GitHub Clone Count Badge

This clone count badge shows **more than 14 days** of clone statistics of a GitHub repository.

## How it works
* Uses the following GitHub action to get repository clone count using `https://api.github.com/repos/{username}/{repo}/traffic/clones` this API. Then the **clone.json** file will be added to the user's https://gist.github.com/ account.
* This action will run every 24th hours to update clone.json with the latest data. Unfortunately, GitHub API allows users to show only the last 14 day's clone data. But this badge will show all the statistics from the day you implement this action.
* **clone.json** posted on https://gist.github.com/ will act as a database.
* Then shields.io dynamic badge will parse this **clone.json** file to show the clone count.
* Clone count badge is in **CLONE.md** file

## Setup (~5 minute setup)
1) [Create a new workflow](https://docs.github.com/en/actions/quickstart#creating-your-first-workflow) from the `Actions` tab of your repository. Name the file `clone.yml` and paste the following:
```yaml
name: GitHub Clone Count Update Everyday

on:
  schedule:
    - cron: "0 */24 * * *"
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      
      - name: gh login
        run: echo "${{ secrets.SECRET_TOKEN }}" | gh auth login --with-token

      - name: parse latest clone count
        run: |
          curl --user "${{ github.actor }}:${{ secrets.SECRET_TOKEN }}" \
            -H "Accept: application/vnd.github.v3+json" \
            https://api.github.com/repos/${{ github.repository }}/traffic/clones \
            > clone.json

      - name: create gist and download previous count
        id: set_id
        run: |
          if gh secret list | grep -q "GIST_ID"
          then
              echo "GIST_ID found"
              echo "GIST=${{ secrets.GIST_ID }}" >> $GITHUB_OUTPUT
              curl https://gist.githubusercontent.com/${{ github.actor }}/${{ secrets.GIST_ID }}/raw/clone.json > clone_before.json
              if cat clone_before.json | grep '404: Not Found'; then
                echo "GIST_ID not valid anymore. Creating another gist..."
                gist_id=$(gh gist create clone.json | awk -F / '{print $NF}')
                echo $gist_id | gh secret set GIST_ID
                echo "GIST=$gist_id" >> $GITHUB_OUTPUT
                cp clone.json clone_before.json
                git rm --ignore-unmatch  CLONE.md
              fi
          else
              echo "GIST_ID not found. Creating a gist.
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

