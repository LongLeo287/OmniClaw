---
id: nicholas-fedor-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:11.904274
---

# KNOWLEDGE EXTRACT: nicholas-fedor
> **Extracted on:** 2026-03-30 17:49:11
> **Source:** nicholas-fedor

---

## File: `watchtower.md`
```markdown
# 📦 nicholas-fedor/watchtower [🔖 PENDING/APPROVE]
🔗 https://github.com/nicholas-fedor/watchtower
🌐 http://watchtower.nickfedor.com/

## Meta
- **Stars:** ⭐ 3160 | **Forks:** 🍴 39
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Automate Docker container image updates

## README (trích đầu)
```
<div align="center">
  <img src="./logo.png" width="450" />

# Watchtower

  Automate Docker container image updates
  <br/><br/>

  [![CircleCI](https://dl.circleci.com/status-badge/img/gh/nicholas-fedor/watchtower/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/nicholas-fedor/watchtower/tree/main)
  [![codecov](https://codecov.io/gh/nicholas-fedor/watchtower/branch/main/graph/badge.svg)](https://codecov.io/gh/nicholas-fedor/watchtower)
  [![GoDoc](https://godoc.org/github.com/nicholas-fedor/watchtower?status.svg)](https://godoc.org/github.com/nicholas-fedor/watchtower)
  [![Go Report Card](https://goreportcard.com/badge/github.com/nicholas-fedor/watchtower)](https://goreportcard.com/report/github.com/nicholas-fedor/watchtower)
  [![latest version](https://img.shields.io/github/tag/nicholas-fedor/watchtower.svg)](https://github.com/nicholas-fedor/watchtower/releases)
  [![Apache-2.0 License](https://img.shields.io/github/license/nicholas-fedor/watchtower.svg)](https://www.apache.org/licenses/LICENSE-2.0)
  [![Codacy Badge](https://app.codacy.com/project/badge/Grade/1c48cfb7646d4009aa8c6f71287670b8)](https://www.codacy.com/gh/nicholas-fedor/watchtower/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=nicholas-fedor/watchtower&amp;utm_campaign=Badge_Grade)
  [![All Contributors](https://img.shields.io/github/all-contributors/nicholas-fedor/watchtower)](#contributors)
  [![Pulls from DockerHub](https://img.shields.io/docker/pulls/nickfedor/watchtower.svg)](https://hub.docker.com/r/nickfedor/watchtower)

</div>

## Quick Start

With watchtower you can update the running version of your containerized app simply by pushing a new image to the Docker Hub or your own image registry.

Watchtower will pull down your new image, gracefully shut down your existing container and restart it with the same options that were used when it was deployed initially. Run the watchtower container with the following command:

```console
$ docker run --detach \
    --name watchtower \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    nickfedor/watchtower
```

Watchtower is intended to be used in homelabs, media centers, local dev environments, and similar. We do **not** recommend using Watchtower in a commercial or production environment.
If that is you, you should be looking into using Kubernetes enabled with CI/CD, such as onedr0p's Talos Linux with FluxCD setup [here](https://github.com/onedr0p/cluster-template).

**⚠️ Note:** It is recommended to use the latest version of Docker. You can check your host's Docker version using the [CLI command](https://docs.docker.com/reference/cli/docker/version/) `docker version`.
This version of Watchtower has been tested to support v1.43 and higher; however, don't be surprised if you experience unexpected behavior when attempting to use newer features on older versions of Docker.
This version autonegotiates the API version by default. If the `DOCKER_API_VERSION` [variabl
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

