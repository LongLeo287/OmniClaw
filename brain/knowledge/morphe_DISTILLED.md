---
id: morphe
type: knowledge
owner: OA_Triage
---
# morphe
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "private": true,
  "workspaces": [
    "app"
  ],
  "devDependencies": {
    "@anolilab/multi-semantic-release": "^2.0.3",
    "semantic-release": "^24.2.7"
  }
}

```

### File: README.md
```md
<div align="center"> 
<picture>
    <source
      width="512px"
      media="(prefers-color-scheme: dark)"
      srcset="https://raw.githubusercontent.com/MorpheApp/.github/refs/heads/main/profile/assets/morphe-wordmark/morphe_wordmark_dark.svg"
    />
    <img 
      width="512px"
      src="https://raw.githubusercontent.com/MorpheApp/.github/refs/heads/main/profile/assets/morphe-wordmark/morphe_wordmark_light.svg"
    />
</picture>

[![Website badge](https://img.shields.io/badge/Website-gray.svg?logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ29weXJpZ2h0IDIwMjUgTW9ycGhlLiBUaGlzIGlzIGNvcHlyaWdodGVkIGNvbnRlbnQsIGFuZCBub3QgbGljZW5zZWQgdW5kZXIgb3BlbiBzb3VyY2UgdGVybXMuCiAgICAgU2VlIGh0dHBzOi8vZ2l0aHViLmNvbS9Nb3JwaGVBcHAvbW9ycGhlLWJyYW5kaW5nIC0tPgoKPHN2ZwogICB3aWR0aD0iNTEyIgogICBoZWlnaHQ9IjUxMiIKICAgdmlld0JveD0iMCAwIDUxMiA1MTIiCiAgIHZlcnNpb249IjEuMSIKICAgaWQ9InN2ZzIiCiAgIHNvZGlwb2RpOmRvY25hbWU9Im1vcnBoZV9sb2dvX2xpZ2h0LnN2ZyIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMS40LjIgKGViZjBlOTQwZDAsIDIwMjUtMDUtMDgpIgogICB4bWxuczppbmtzY2FwZT0iaHR0cDovL3d3dy5pbmtzY2FwZS5vcmcvbmFtZXNwYWNlcy9pbmtzY2FwZSIKICAgeG1sbnM6c29kaXBvZGk9Imh0dHA6Ly9zb2RpcG9kaS5zb3VyY2Vmb3JnZS5uZXQvRFREL3NvZGlwb2RpLTAuZHRkIgogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxzb2RpcG9kaTpuYW1lZHZpZXcKICAgICBpZD0ibmFtZWR2aWV3MiIKICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgYm9yZGVyY29sb3I9IiMwMDAwMDAiCiAgICAgYm9yZGVyb3BhY2l0eT0iMC4yNSIKICAgICBpbmtzY2FwZTpzaG93cGFnZXNoYWRvdz0iMiIKICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMC4wIgogICAgIGlua3NjYXBlOnBhZ2VjaGVja2VyYm9hcmQ9IjAiCiAgICAgaW5rc2NhcGU6ZGVza2NvbG9yPSIjZDFkMWQxIgogICAgIGlua3NjYXBlOnpvb209IjEuMTU0Mjk2OSIKICAgICBpbmtzY2FwZTpjeD0iMjU2IgogICAgIGlua3NjYXBlOmN5PSIyNTYiCiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxNDQwIgogICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjgzNiIKICAgICBpbmtzY2FwZTp3aW5kb3cteD0iMCIKICAgICBpbmtzY2FwZTp3aW5kb3cteT0iMCIKICAgICBpbmtzY2FwZTp3aW5kb3ctbWF4aW1pemVkPSIxIgogICAgIGlua3NjYXBlOmN1cnJlbnQtbGF5ZXI9InN2ZzIiPgogICAgPGlua3NjYXBlOnBhZ2UKICAgICAgIHg9IjAiCiAgICAgICB5PSIwIgogICAgICAgd2lkdGg9IjUxMiIKICAgICAgIGhlaWdodD0iNTEyIgogICAgICAgaWQ9InBhZ2UyIgogICAgICAgbWFyZ2luPSIwIgogICAgICAgYmxlZWQ9IjAiIC8+CiAgPC9zb2RpcG9kaTpuYW1lZHZpZXc+CiAgPGRlZnMKICAgICBpZD0iZGVmczIiIC8+CiAgPCEtLSBMZXR0ZXIgLS0+CiAgPGcKICAgICBpZD0iTGV0dGVyIgogICAgIHN0eWxlPSJmaWxsOiNmZmZmZmY7ZmlsbC1vcGFjaXR5OjEiPgogICAgPHBhdGgKICAgICAgIGlkPSJMZWZ0IgogICAgICAgZD0ibSAxMjMsMTQwIGMgLTIxLDAgLTM5LDE3IC00MCwzOCB2IDE5MiBjIDEsMjEgMTksMzggNDAsMzggMjEsMCAzOSwtMTcgNDAsLTM4IFYgMTc4IGMgLTEsLTIxIC0xOSwtMzggLTQwLC0zOCB6IgogICAgICAgZmlsbD0iIzFFNUFBOCIKICAgICAgIHN0eWxlPSJmaWxsOiNmZmZmZmY7ZmlsbC1vcGFjaXR5OjEiIC8+CiAgICA8cGF0aAogICAgICAgaWQ9IlJpZ2h0IgogICAgICAgZD0ibSAzNDksMjg1IHYgODUgYyAxLDIxIDE5LDM4IDQwLDM4IDIxLDAgMzksLTE3IDQwLC0zOCBWIDE4MiBjIC0xMSwtMTQgLTc0LDYzIC04MCwxMDMgeiIKICAgICAgIGZpbGw9IiMwMEFGQUUiCiAgICAgICBzdHlsZT0iZmlsbDojZmZmZmZmO2ZpbGwtb3BhY2l0eToxIiAvPgogICAgPHBhdGgKICAgICAgIGlkPSJNaWRkbGUiCiAgICAgICBkPSJtIDEyNywxMDggYyAtMzQsMCAtNDQsMjUgLTQ0LDQwIHYgNTQgYyAzMCwtMzMgNzUsMjcgODAsMzMgMjgsMzIgNDQsODcgOTMsODkgNDgsLTIgNjcsLTU2IDkzLC04OSAwLDAgNDUsLTc0IDgwLC04MCAwLC0yOCAtMTEsLTQ3IC00NCwtNDcgLTM0LDAgLTU4LDUwIC03NSw3MiAtMTcsMjIgLTI1LDQ2IC01NCw0NiAtMjksMCAtMzgsLTI1IC01NCwtNDYgLTE3LC0yMiAtNDEsLTcyIC03NSwtNzIgeiIKICAgICAgIGZpbGw9InVybCgjbGluZWFyR3JhZGllbnQyKSIKICAgICAgIHN0eWxlPSJmaWxsOiNmZmZmZmY7ZmlsbC1vcGFjaXR5OjEiIC8+CiAgPC9nPgo8L3N2Zz4K&style=for-the-badge)](https://morphe.software) [![Documentation badge](https://img.shields.io/badge/Documentation-gray?style=for-the-badge&logo=github)](https://github.com/MorpheApp/morphe-documentation#readme) [![Subreddit badge](https://img.shields.io/badge/Reddit-gray?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/MorpheApp) [![X badge](https://img.shields.io/badge/X_-gray?style=for-the-badge&logo=x)](https://x.com/MorpheApp) [![Crowdin badge](https://img.shields.io/badge/Translations-gray?style=for-the-badge&logo=crowdin)](https://morphe.software/translate)
<br>
</div>

&nbsp;
<p align="center">
  <a href="https://morphe.software" title="Download Morphe">
    <img src="https://raw.githubusercontent.com/MorpheApp/.github/refs/heads/main/profile/assets/download-morphe.svg" alt="Download Morphe" width="240"/>
  </a>
</p>
&nbsp;

# 💊 Morphe
Morphe app patcher for Android

## ❓ About

Morphe Manager is based off the work of [URV](https://github.com/Jman-Github/Universal-ReVanced-Manager)
and [ReVanced](https://github.com/ReVanced/revanced-manager).
All modifications made by Morphe, along with their dates, can be found in the Git history.

## 📜 License

Morphe Patches are licensed under the [GNU General Public License v3.0](LICENSE), with additional conditions under GPLv3 Section 7:

- **Attribution (7b):** Any use of this code, including derivatives, must display a visible notice:

  > This app uses code from Morphe. To learn more, visit https://morphe.software

- **Name Restriction (7c):** The name **"Morphe"** may not be used for derivative works.  
  Derivatives must adopt a distinct identity unrelated to "Morphe."

See the [LICENSE](LICENSE) file for the full GPLv3 terms and the [NOTICE](NOTICE) file for full conditions of GPLv3 Section 7.

```

### File: app\package.json
```json
{
  "name": "app",
  "private": false,
  "devDependencies": {
    "@anolilab/multi-semantic-release": "^1.1.10",
    "@saithodev/semantic-release-backmerge": "^4.0.1",
    "@MorpheApp/changelog": "git+https://github.com/MorpheApp/changelog.git#bundle",
    "@semantic-release/git": "^10.0.1",
    "gradle-semantic-release-plugin": "^1.10.1"
  }
}

```

### File: app\app-release.json
```json
{
  "created_at": "2026-03-29T22:09:46.753Z",
  "description": "## app [1.13.1](https://github.com/MorpheApp/morphe-manager/compare/v1.13.0...v1.13.1) (2026-03-29)\n\n\n### Bug Fixes\n\n* Handle http redirects ([3026fb2](https://github.com/MorpheApp/morphe-manager/commit/3026fb2dd893d00034ce20074bdd93b848a11037))",
  "download_url": "https://github.com/MorpheApp/morphe-manager/releases/download/v1.13.1/morphe-manager-1.13.1.apk",
  "signature_download_url": "https://github.com/MorpheApp/morphe-manager/releases/download/v1.13.1/morphe-manager-1.13.1.apk.asc",
  "version": "1.13.1"
}

```

### File: app\CHANGELOG.md
```md
## app [1.13.1](https://github.com/MorpheApp/morphe-manager/compare/v1.13.0...v1.13.1) (2026-03-29)


### Bug Fixes

* Handle http redirects ([3026fb2](https://github.com/MorpheApp/morphe-manager/commit/3026fb2dd893d00034ce20074bdd93b848a11037))

## app [1.13.1-dev.1](https://github.com/MorpheApp/morphe-manager/compare/v1.13.0...v1.13.1-dev.1) (2026-03-29)


### Bug Fixes

* Handle http redirects ([3026fb2](https://github.com/MorpheApp/morphe-manager/commit/3026fb2dd893d00034ce20074bdd93b848a11037))

# app [1.13.0](https://github.com/MorpheApp/morphe-manager/compare/v1.12.2...v1.13.0) (2026-03-28)


### Bug Fixes

* Correct download/install flow and state handling ([e2025ce](https://github.com/MorpheApp/morphe-manager/commit/e2025ce10691b0952ecd9fabe1339179ce89ff4e))
* Refactor `GitHubPullRequestBundle` to use our `HttpService`, allow using raw `.mpp` file from PR ([f50ae1d](https://github.com/MorpheApp/morphe-manager/commit/f50ae1d97c969ba20eee8ff2c539468f2f370820))
* Refactor `HttpService` and `MorpheApi` ([e105f60](https://github.com/MorpheApp/morphe-manager/commit/e105f6021f82061b15708722ff086357c59249c4))
* Replace `HttpURLConnection` with Ktor in `resolveRedirect` ([7470e6a](https://github.com/MorpheApp/morphe-manager/commit/7470e6a3d31792e63221f3ac7c0630d3344f3f5e))
* Skip APK signature verification for Android 10 and below ([6b2b591](https://github.com/MorpheApp/morphe-manager/commit/6b2b5913aa253cd9739aa2f8038b3ab70b57a0e8))


### Features

* Add notification icon creation ([#358](https://github.com/MorpheApp/morphe-manager/issues/358)) ([a096b85](https://github.com/MorpheApp/morphe-manager/commit/a096b85bd5ff7a6051f1cf0badaaaffddb95e572))
* Allow patching split APKs with a warning instead of blocking ([#353](https://github.com/MorpheApp/morphe-manager/issues/353)) ([2575368](https://github.com/MorpheApp/morphe-manager/commit/2575368e8054de9f63ce5e4bf0d005b4182e7a86))

# app [1.13.0-dev.3](https://github.com/MorpheApp/morphe-manager/compare/v1.13.0-dev.2...v1.13.0-dev.3) (2026-03-24)


### Bug Fixes

* Skip APK signature verification for Android 10 and below ([6b2b591](https://github.com/MorpheApp/morphe-manager/commit/6b2b5913aa253cd9739aa2f8038b3ab70b57a0e8))

# app [1.13.0-dev.2](https://github.com/MorpheApp/morphe-manager/compare/v1.13.0-dev.1...v1.13.0-dev.2) (2026-03-24)


### Features

* Add notification icon creation ([#358](https://github.com/MorpheApp/morphe-manager/issues/358)) ([a096b85](https://github.com/MorpheApp/morphe-manager/commit/a096b85bd5ff7a6051f1cf0badaaaffddb95e572))

# app [1.13.0-dev.1](https://github.com/MorpheApp/morphe-manager/compare/v1.12.2...v1.13.0-dev.1) (2026-03-23)


### Features

* Allow patching split APKs with a warning instead of blocking ([#353](https://github.com/MorpheApp/morphe-manager/issues/353)) ([2575368](https://github.com/MorpheApp/morphe-manager/commit/2575368e8054de9f63ce5e4bf0d005b4182e7a86))

## app [1.12.2](https://github.com/MorpheApp/morphe-manager/compare/v1.12.1...v1.12.2) (2026-03-22)


### Bug Fixes

* Update to Patcher 1.3.2 ([4a17ab7](https://github.com/MorpheApp/morphe-manager/commit/4a17ab74231a497a015a692eac0e02bfc36b65bd))

## app [1.12.2-dev.1](https://github.com/MorpheApp/morphe-manager/compare/v1.12.1...v1.12.2-dev.1) (2026-03-22)


### Bug Fixes

* Update to Patcher 1.3.2 ([4a17ab7](https://github.com/MorpheApp/morphe-manager/commit/4a17ab74231a497a015a692eac0e02bfc36b65bd))

## app [1.12.1](https://github.com/MorpheApp/morphe-manager/compare/v1.12.0...v1.12.1) (2026-03-22)


### Bug Fixes

* Update to Patcher 1.3.1 ([b517535](https://github.com/MorpheApp/morphe-manager/commit/b51753528e0b7ed4a5b11bb9b8df71ddbff0c8dd))

## app [1.12.1-dev.1](https://github.com/MorpheApp/morphe-manager/compare/v1.12.0...v1.12.1-dev.1) (2026-03-22)


### Bug Fixes

* Update to Patcher 1.3.1 ([b517535](https://github.com/MorpheApp/morphe-manager/commit/b51753528e0b7ed4a5b11bb9b8df71ddbff0c8dd))

# app [1.12.0](https://github.com/MorpheApp/morphe-manager/compare/v1.11.0...v1.12.0) (2026-03-22)


### Bug Fixes

* Add list editor dialog for `List<String>` patch options ([#318](https://github.com/MorpheApp/morphe-manager/issues/318)) ([5b722d2](https://github.com/MorpheApp/morphe-manager/commit/5b722d27f979d32a18a04b0bbefb36b0add6e80d))
* Allow third-party universal patches in `Other Apps` flow ([#322](https://github.com/MorpheApp/morphe-manager/issues/322)) ([b888ff7](https://github.com/MorpheApp/morphe-manager/commit/b888ff77e58618dc9a5691ef0e96381092a227c5))
* Cache source avatars to prevent flicker on sheet reopen ([8e8a350](https://github.com/MorpheApp/morphe-manager/commit/8e8a35050d2da83736e0737e4d151e401f19696f))
* Prevent adding duplicate patch sources ([d616d7f](https://github.com/MorpheApp/morphe-manager/commit/d616d7f46f3f95424529992687152bd3f93740fa))
* Set default minimum process memory limit to 512MB ([c28aaae](https://github.com/MorpheApp/morphe-manager/commit/c28aaae9a63dbb4b0a084938ed4092cfdddb3f37))
* Use latest Morphe patcher ([cb53fbb](https://github.com/MorpheApp/morphe-manager/commit/cb53fbb5814d67730b7e53e940bcac49a9df671e))


### Features

* Group universal patches into separate section in ExpertModeDialog ([4c833da](https://github.com/MorpheApp/morphe-manager/commit/4c833da021d2e5a180cf39f9709b2d2f1ecce606))
* Parse CHANGELOG.md for changelogs ([84eb6ef](https://github.com/MorpheApp/morphe-manager/commit/84eb6efa5b78e1b0a881b29f311542f98ce1fd7d))
* Refine update badges using changelog scope matching ([#310](https://github.com/MorpheApp/morphe-manager/issues/310)) ([9b1cae7](https://github.com/MorpheApp/morphe-manager/commit/9b1cae7ddae4f8676b5e920a28ab1bcb4b424f34))
* Use interactive background animations ([#284](https://github.com/MorpheApp/morphe-manager/issues/284)) ([fca12bf](https://github.com/MorpheApp/morphe-manager/commit/fca12bf0e9b3e4614255de82bc60fd634e015f35))
* Use Morphe patcher 1.3.0 ([#329](https://github.com/MorpheApp/morphe-manager/issues/329)) ([344a06c](https://github.com/MorpheApp/morphe-manager/commit/344a06c43d46f7e6be1ca9292aea639a5677d542))

# app [1.12.0-dev.8](https://github.com/MorpheApp/morphe-manager/compare/v1.12.0-dev.7...v1.12.0-dev.8) (2026-03-21)


### Features

* Refine update badges using changelog scope matching ([#310](https://github.com/MorpheApp/morphe-manager/issues/310)) ([9b1cae7](https://github.com/MorpheApp/morphe-manager/commit/9b1cae7ddae4f8676b5e920a28ab1bcb4b424f34))

# app [1.12.0-dev.7](https://github.com/MorpheApp/morphe-manager/compare/v1.12.0-dev.6...v1.12.0-dev.7) (2026-03-21)


### Features

* Use Morphe patcher 1.3.0 ([#329](https://github.com/MorpheApp/morphe-manager/issues/329)) ([344a06c](https://github.com/MorpheApp/morphe-manager/commit/344a06c43d46f7e6be1ca9292aea639a5677d542))

# app [1.12.0-dev.6](https://github.com/MorpheApp/morphe-manager/compare/v1.12.0-dev.5...v1.12.0-dev.6) (2026-03-19)


### Bug Fixes

* Use latest Morphe patcher ([cb53fbb](https://github.com/MorpheApp/morphe-manager/commit/cb53fbb5814d67730b7e53e940bcac49a9df671e))

# app [1.12.0-dev.5](https://github.com/MorpheApp/morphe-manager/compare/v1.12.0-dev.4...v1.12.0-dev.5) (2026-03-16)


### Bug Fixes

* Set default minimum process memory limit to 512MB ([c28aaae](https://github.com/MorpheApp/morphe-manager/commit/c28aaae9a63dbb4b0a084938ed4092cfdddb3f37))

# app [1.12.0-dev.4](https://github.com/MorpheApp/morphe-manager/compare/v1.12.0-dev.3...v1.12.0-dev.4) (2026-03-13)


### Bug Fixes

* Allow third-party universal patches in `Other Apps` flow ([#322](https://github.com/MorpheApp/morphe-manager/issues/322)) ([b888ff7](https://github.com/MorpheApp/morphe-manager/commit/b888ff77e58618dc9a5691ef0e96381092a227c5))

# app [1.12.0-dev.3](https://github.com/MorpheApp/morphe-manager/compare/v1.12.0-dev.2...v1.12.0-dev.3) (2026-03-13)


### Bug Fixes

* Add list editor dialog for `List<String>` patch options ([#318](https://github.com/MorpheApp/morphe-manager/issues/318)) ([5b722d2](https://github.com/MorpheApp/morphe-manager/commit/5b722d27f979d32a18a04b0bbefb36b0add6e80d))

# app [1.12.0-dev.2](https://github.com/MorpheApp/morphe-manager/compare/v1.12.0-dev.1...v1.12.0-dev.2) (2026-03-08)


### Features

* Use interactive background animations ([#284](https://github.com/MorpheApp/morphe-manager/issues/284)) ([fca12bf](https://github.com/MorpheApp/morphe-manager/commit/fca12bf0e9b3e4614255de82bc60fd634e015f35))

# app [1.12.0-dev.1](https://github.com/MorpheApp/morphe-manager/compare/v1.11.0...v1.12.0-dev.1) (2026-03-08)


### Bug Fixes

* Cache source avatars to prevent flicker on sheet reopen ([8e8a350](https://github.com/MorpheApp/morphe-manager/commit/8e8a35050d2da83736e0737e4d151e401f19696f))
* Prevent adding duplicate patch sources ([d616d7f](https://github.com/MorpheApp/morphe-manager/commit/d616d7f46f3f95424529992687152bd3f93740fa))


### Features

* Group universal patches into separate section in ExpertModeDialog ([4c833da](https://github.com/MorpheApp/morphe-manager/commit/4c833da021d2e5a180cf39f9709b2d2f1ecce606))
* Parse CHANGELOG.md for changelogs ([84eb6ef](https://github.com/MorpheApp/morphe-manager/commit/84eb6efa5b78e1b0a881b29f311542f98ce1fd7d))

# app [1.11.0](https://github.com/MorpheApp/morphe-manager/compare/v1.10.2...v1.11.0) (2026-03-07)


### Bug Fixes

* Root installation fails if module path does not exist ([#282](https://github.com/MorpheApp/morphe-manager/issues/282)) ([3405802](https://github.com/MorpheApp/morphe-manager/commit/3405802d37247596d0747f00e6a98f5a10cc9c9a))
* The language selection list is empty ([db69dad](https://github.com/MorpheApp/morphe-manager/commit/db69dadbca9fe2c396719a93914600192b8affae))


### Features

* Add deep link support ([#290](https://github.com/MorpheApp/morphe-manager/issues/290)) ([3b57efb](https://github.com/MorpheApp/morphe-manager/commit/3b57efb170e56eea1821dcbf2c49dcc2b795763a))
* add Kurmanji (kmr-TR) language support ([516c200](https://github.com/MorpheApp/morphe-manager/commit/516c2001ebac4b6530d7560bf2797270a0d7942c))
* Improve information in exported manager logs ([#279](https://github.com/MorpheApp/morphe-manager/issues/279)) ([2c0c344](https://github.com/MorpheApp/morphe-manager/commit/2c0c3447d647292ec17f9c9c55145811a732a78e))
* Use Morphe patcher 1.2.0 ([#231](https://github.com/MorpheApp/morphe-manager/issues/231)) ([944a3ab](https://github.com/MorpheApp/morphe-manager/commit/944a3ab7fab2d689b81f5d8e6bf5224660ce11ef))

# app [1.11.0-dev.6](https://github.com/MorpheApp/morphe-manager/compare/v1.11.0-dev.5...v1.11.0-dev.6) (2026-03-07)


### Features

* Add deep link support ([#290](https://github.com/MorpheApp/morphe-manager/issues/290)) ([3b57efb](https://github.com/MorpheApp/morphe-manager/commit/3b57efb170e56eea1821dcbf2c49dcc2b795763a))

# app [1.11.0-dev.5](https://github.com/MorpheApp/morphe-manager/compare/v1.11.0-dev.4...v1.11.0-dev.5) (2026-03-07)


### Features

* add Kurmanji (kmr-TR) language support ([516c200](https://github.com/MorpheApp/morphe-manager/commit/516c2001ebac4b6530d7560bf2797270a0d7942c))

# app [1.11.0-dev.4](https://github.com/MorpheApp/morphe-manager/compare/v1.11.0-dev.3...v1.11.0-dev.4) (2026-03-05)


### Bug Fixes

* The language selection list is empty ([db69dad](https://github.com/MorpheApp/morphe-manager/commit/db69dadbca9fe2c396719a93914600192b8affae))

# app [1.11.0-dev.3](https://github.com/MorpheApp/morphe-manager/compare/v1.11.0-dev.2...v1.11.0-dev.3) (2026-03-05)


### Bug Fixes

* Root installation fails if module path does not exist ([#282](https://github.com/MorpheApp/morphe-manager/issues/282)) ([3405802](https://github.com/MorpheApp/morphe-manager/commit/3405802d37247596d0747f00e6a98f5a10cc9c9a))

# app [1.11.0-dev.2](https://github.com/MorpheApp/morphe-manager/compare/v1.11.0-dev.1...v1.11.0-dev.2) (2026-03-04)


### Features

* Improve information in exported manager logs ([#279](https://github.com/MorpheApp/morphe-manager/issues/279)) ([2c0c344](https://github.com/MorpheApp/morphe-manager/commit/2c0c3447d647292ec17f9c9c55145811a732a78e))

# app [1.11.0-dev.1](https://github.com/MorpheApp/morphe-manager/compare/v1.10.2...v1.11.0-dev.1) (2026-03-03)


### Features

* Use Morphe patcher 1.2.0 ([#231](https://github.com/MorpheApp/morphe-manager/issues/231)) ([944a3ab](https://github.com/MorpheApp/morphe-manager/commit/944a3ab7fab2d689b81f5d8e6bf5224660ce11ef))

## app [1.10.2](https://github.com/MorpheApp/morphe-manager/compare/v1.10.1...v1.10.2) (2026-03-02)


### Bug Fixes

* Manager does not show updates if available ([#270](https://github.com/MorpheApp/morphe-manager/issues/270)) ([4e6f2af](https://github.com/MorpheApp/morphe-manager/commit/4e6f2afee34894c271903b6ea18a2b1a2cfe5ee1))

## app [1.10.2-dev.1](https://github.com/MorpheApp/morphe-manager/compare/v1.10.1...v1.10.2-dev.1) (2026-03-02)


### Bug Fixes

* Manager does not show updates if available ([#270](https://github.com/MorpheApp/morphe-manager/issues/270)) ([4e6f2af](https://github.com/MorpheApp/morphe-manager/commit/4e6f2afee34894c271903b6ea18a2b1a2cfe5ee1))

## app [1.10.1](https://github.com/MorpheApp/morphe-manager/compare/v1.10.0...v1.10.1) (2026-03-02)


### Bug Fixes

* Custom header does not apply to Youtube Music in simple mode ([88ed0d1](https://github.com/MorpheApp/morphe-manager/commit/88ed0d1c891c01cb5d6b81e2d4f1509f3d1cb6a2))

## app [1.10.1-dev.1](https://github.com/MorpheApp/morphe-manager/compare/v1.10.0...v1.10.1-dev.1) (2026-03-02)


### Bug Fixes

* Custom header does not apply to Youtube Music in simple mode ([88ed0d1](https://github.com/MorpheApp/morphe-manager/commit/88ed0d1c891c01cb5d6b81e2d4f1509f3d1cb6a2))

# app [1.10.0](https://github.com/MorpheApp/morphe-manager/compare/v1.9.0...v1.10.0) (2026-03-02)


### Features

* Support YT Music change header option ([#264](https://github.com/MorpheApp/morphe-manager/issues/264)) ([3d11e21](https://github.com/MorpheApp/morphe-manager/commit/3d11e21e37ee225750d43204b8876d598d764f63))

# app [1.10.0-dev.1](https://github.com/MorpheApp/morphe-manager/compare/v1.9.0...v1.10.0-dev.1) (2026-03-01)


### Features

* Support YT Music change header option ([#264](https://github.com/MorpheApp/morphe-manager/issues/264)) ([3d11e21](https://github.com/MorpheApp/morphe-manager/commit/3d11e21e37ee225750d43204b8876d598d764f63))

# app [1.9.0](https://github.com/MorpheApp/morphe-manager/compare/v1.8.0...v1.9.0) (2026-03-01)


### Bug Fixes

* Add missing permission to app manifest ([c439f71](https://github.com/MorpheApp/morphe-manager/commit/c439f7177576dbdebae770a74b963c4e590b9b68))
* Pre-release toggle is enabled if user adds link to dev branch ([28417d0](https://github.com/MorpheApp/morphe-manager/commit/28417d06d78035c86bf1ac53367ef68a594c6f63))
* Remove UI stuttering during APK write when patching in-process ([#258](https://github.com/MorpheApp/morphe-manager/issues/258)) ([99f1a62](https://github.com/MorpheApp/morphe-manager/commit/99f1a6268f26f66a56afdf181a1fe9c4d0af05c1))


### Features

* Add Expert mode patching screen ([#250](https://github.com/Morph
... [TRUNCATED]
```

### File: app\google-services.json
```json
{
  "project_info": {
    "project_number": "574971415597",
    "project_id": "morphe-manager",
    "storage_bucket": "morphe-manager.firebasestorage.app"
  },
  "client": [
    {
      "client_info": {
        "mobilesdk_app_id": "1:574971415597:android:5acf99d4cc8260eedc7ca4",
        "android_client_info": {
          "package_name": "app.morphe.manager"
        }
      },
      "oauth_client": [],
      "api_key": [
        {
          "current_key": "AIzaSyAICrE-tnEhNKXh1vEbfucYWWxOr7NSr_g"
        }
      ],
      "services": {
        "appinvite_service": {
          "other_platform_oauth_client": []
        }
      }
    }
  ],
  "configuration_version": "1"
}
```

### File: .github\scripts\send_fcm.py
```py
# Copyright 2026 Morphe.
# https://github.com/MorpheApp/morphe-manager

#!/usr/bin/env python3
"""
Send an FCM push notification to a Morphe Manager topic.

Environment variables (all required):
  FCM_PROJECT_ID           — Firebase project ID (from Firebase Console)
  FCM_SERVICE_ACCOUNT_JSON — Full content of the Service Account JSON file

Optional (for release workflow):
  NEW_TAG   — Release tag, e.g. "v1.2.3". Version is derived by stripping the "v" prefix.
  BRANCH    — Git branch name. "main" → stable topic; anything else → dev topic.

Optional (for test workflow — override auto-routing):
  FCM_TOPIC   — Explicit topic to send to. Overrides BRANCH-based routing.
  FCM_TYPE    — Message type: "manager_update" (default) or "bundle_update"
  FCM_VERSION — Version string to include in the notification (used by both manager_update and bundle_update)
"""

import json
import os
import sys
import time
import base64
import urllib.request
import urllib.parse

try:
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
except ImportError:
    print("ERROR: 'cryptography' package is not installed. Run: pip install cryptography", file=sys.stderr)
    sys.exit(1)

# ── Read environment ───────────────────────────────────────────────────────────

project_id = os.environ.get("FCM_PROJECT_ID", "").strip()
sa_json    = os.environ.get("FCM_SERVICE_ACCOUNT_JSON", "").strip()

if not project_id:
    print("ERROR: FCM_PROJECT_ID is not set", file=sys.stderr)
    sys.exit(1)
if not sa_json:
    print("ERROR: FCM_SERVICE_ACCOUNT_JSON is not set", file=sys.stderr)
    sys.exit(1)

# Topic routing:
#   FCM_TOPIC env var overrides everything (used in test workflow for manual control)
#   Otherwise: main → stable topic, anything else → dev topic
explicit_topic = os.environ.get("FCM_TOPIC", "").strip()
branch         = os.environ.get("BRANCH", "").strip()
new_tag        = os.environ.get("NEW_TAG", "").strip()

# Message type and version
msg_type    = os.environ.get("FCM_TYPE", "manager_update").strip()
fcm_version = os.environ.get("FCM_VERSION", "").strip()

# For release workflow: derive version from tag (strip leading "v")
if new_tag:
    fcm_version = new_tag.lstrip("v")

if explicit_topic:
    topic = explicit_topic
else:
    # Default routing by message type and branch:
    #   manager_update: morphe_updates / morphe_updates_dev
    #   bundle_update:  morphe_patches_updates / morphe_patches_updates_dev
    is_main = (branch == "main")
    if msg_type == "bundle_update":
        topic = "morphe_patches_updates" if is_main else "morphe_patches_updates_dev"
    else:
        topic = "morphe_updates" if is_main else "morphe_updates_dev"

print(f"FCM target   : {topic}")
print(f"Message type : {msg_type}")
if fcm_version:
    print(f"Version      : {fcm_version}")

# ── Parse Service Account ──────────────────────────────────────────────────────

try:
    sa = json.loads(sa_json)
except json.JSONDecodeError as e:
    print(f"ERROR: FCM_SERVICE_ACCOUNT_JSON is not valid JSON: {e}", file=sys.stderr)
    sys.exit(1)

required_keys = ("client_email", "private_key", "token_uri")
for key in required_keys:
    if key not in sa:
        print(f"ERROR: FCM_SERVICE_ACCOUNT_JSON missing key: '{key}'", file=sys.stderr)
        sys.exit(1)

# ── Build and sign JWT ─────────────────────────────────────────────────────────

now = int(time.time())

def b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()

header  = b64(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
payload = b64(json.dumps({
    "iss":   sa["client_email"],
    "sub":   sa["client_email"],
    "aud":   sa.get("token_uri", "https://oauth2.googleapis.com/token"),
    "iat":   now,
    "exp":   now + 3600,
    "scope": "https://www.googleapis.com/auth/firebase.messaging",
}).encode())

try:
    private_key = serialization.load_pem_private_key(
        sa["private_key"].encode(),
        password=None,
    )
except Exception as e:
    print(f"ERROR: Failed to load private key from Service Account: {e}", file=sys.stderr)
    sys.exit(1)

signature = private_key.sign(
    f"{header}.{payload}".encode(),
    asym_padding.PKCS1v15(),
    hashes.SHA256(),
)
jwt_token = f"{header}.{payload}.{b64(signature)}"

# ── Exchange JWT for OAuth2 access token ──────────────────────────────────────

token_url  = sa.get("token_uri", "https://oauth2.googleapis.com/token")
token_data = urllib.parse.urlencode({
    "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "assertion":  jwt_token,
}).encode()

try:
    token_resp = urllib.request.urlopen(
        urllib.request.Request(token_url, data=token_data)
    )
    access_token = json.loads(token_resp.read())["access_token"]
except Exception as e:
    print(f"ERROR: Failed to obtain access token: {e}", file=sys.stderr)
    sys.exit(1)

print("OAuth2 token obtained successfully")

# ── Build FCM message payload ──────────────────────────────────────────────────

data_payload: dict[str, str] = {"type": msg_type}
# Include version in payload whenever it's provided - both manager_update and
# bundle_update support it; the app ignores unknown keys for forward-compatibility.
if fcm_version:
    data_payload["version"] = fcm_version

fcm_message = {
    "message": {
        "topic": topic,
        "data":  data_payload,
        # high priority wakes the device from Doze mode via Google Play Services
        "android": {"priority": "high"},
    }
}

# ── Send FCM request ───────────────────────────────────────────────────────────

fcm_url     = f"https://fcm.googleapis.com/v1/projects/{project_id}/messages:send"
fcm_payload = json.dumps(fcm_message).encode()

fcm_req = urllib.request.Request(
    fcm_url,
    data=fcm_payload,
    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type":  "application/json",
    },
)

try:
    fcm_resp    = urllib.request.urlopen(fcm_req)
    status_code = fcm_resp.status
    resp_body   = fcm_resp.read().decode()
except urllib.error.HTTPError as e:
    status_code = e.code
    resp_body   = e.read().decode()

print(f"\nFCM response (HTTP {status_code}):")
try:
    print(json.dumps(json.loads(resp_body), indent=2))
except Exception:
    print(resp_body)

if status_code != 200:
    print(
        f"\nERROR: FCM push failed with HTTP {status_code}.\n"
        "Check that FCM_PROJECT_ID and FCM_SERVICE_ACCOUNT_JSON secrets are correct\n"
        "and that the Service Account has the 'Firebase Cloud Messaging Admin' role.",
        file=sys.stderr,
    )
    sys.exit(1)

print(f"\nFCM notification sent successfully to topic '{topic}'")

```

