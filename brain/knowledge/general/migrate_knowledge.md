---
id: migrate-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:08.058742
---

# KNOWLEDGE EXTRACT: migrate
> **Extracted on:** 2026-03-30 22:43:14
> **Source:** migrate

---

## File: `.dockerignore`
```
# Project
FAQ.md
README.md
LICENSE
.gitignore
.travis.yml
CONTRIBUTING.md
MIGRATIONS.md
docker-deploy.sh

# Golang
testing
```

## File: `.gitignore`
```
.DS_Store
cli/build
cli/cli
cli/migrate
.coverage
.godoc.pid
vendor/
.vscode/
.idea
dist/
```

## File: `.golangci.yml`
```yaml
version: "2"
linters:
  enable:
    - goconst
    - misspell
    - nakedret
    - prealloc
    - revive
    - unconvert
    - unparam
  settings:
    misspell:
      locale: US
    revive:
      rules:
        - name: redundant-build-tag
  exclusions:
    generated: lax
    rules:
      - path: (.+)\.go$
        text: G104
    paths:
      - third_party$
      - builtin$
      - examples$
issues:
  max-issues-per-linter: 0
  max-same-issues: 0
formatters:
  enable:
    - gofmt
  exclusions:
    generated: lax
    paths:
      - third_party$
      - builtin$
      - examples$
```

## File: `.goreleaser.yml`
```yaml
project_name: migrate
before:
  hooks:
    - go mod tidy
builds:
  - env:
      - CGO_ENABLED=0
    goos:
      - linux
      - windows
      - darwin
    goarch:
      - amd64
      - arm
      - arm64
      - 386
    goarm:
      - 7
    main: ./cmd/migrate
    ldflags:
      - '-w -s -X main.Version={{ .Version }} -extldflags "static"'
    flags:
      - "-tags={{ .Env.DATABASE }} {{ .Env.SOURCE }}"
      - "-trimpath"
nfpms:
  - homepage: "https://github.com/golang-migrate/migrate"
    maintainer: "dhui@users.noreply.github.com"
    license: MIT
    description: "Database migrations"
    formats:
      - deb
    file_name_template: "{{ .ProjectName }}.{{ .Os }}-{{ .Arch }}{{ if .Arm }}v{{ .Arm }}{{ end }}"
dockers:
  - goos: linux
    goarch: amd64
    dockerfile: Dockerfile.github-actions
    use: buildx
    ids:
      - migrate
    image_templates:
      - 'migrate/migrate:{{ .Tag }}-amd64'
    build_flag_templates:
      - '--label=org.opencontainers.image.created={{ .Date }}'
      - '--label=org.opencontainers.image.title={{ .ProjectName }}'
      - '--label=org.opencontainers.image.revision={{ .FullCommit }}'
      - '--label=org.opencontainers.image.version={{ .Version }}'
      - "--label=org.opencontainers.image.source={{ .GitURL }}"
      - "--platform=linux/amd64"
  - goos: linux
    goarch: arm64
    dockerfile: Dockerfile.github-actions
    use: buildx
    ids:
      - migrate
    image_templates:
      - 'migrate/migrate:{{ .Tag }}-arm64'
    build_flag_templates:
      - '--label=org.opencontainers.image.created={{ .Date }}'
      - '--label=org.opencontainers.image.title={{ .ProjectName }}'
      - '--label=org.opencontainers.image.revision={{ .FullCommit }}'
      - '--label=org.opencontainers.image.version={{ .Version }}'
      - "--label=org.opencontainers.image.source={{ .GitURL }}"
      - "--platform=linux/arm64"

docker_manifests:
- name_template: 'migrate/migrate:{{ .Tag }}'
  image_templates:
  - 'migrate/migrate:{{ .Tag }}-amd64'
  - 'migrate/migrate:{{ .Tag }}-arm64'
- name_template: 'migrate/migrate:{{ .Major }}'
  image_templates:
  - 'migrate/migrate:{{ .Tag }}-amd64'
  - 'migrate/migrate:{{ .Tag }}-arm64'
- name_template: 'migrate/migrate:latest'
  image_templates:
  - 'migrate/migrate:{{ .Tag }}-amd64'
  - 'migrate/migrate:{{ .Tag }}-arm64'
archives:
  - name_template: "{{ .ProjectName }}.{{ .Os }}-{{ .Arch }}{{ if .Arm }}v{{ .Arm }}{{ end }}"
    format_overrides:
      - goos: windows
        format: zip
checksum:
  name_template: 'sha256sum.txt'
release:
  draft: true
  prerelease: auto
source:
  enabled: true
  format: zip
changelog:
  skip: false
  sort: asc
  filters:
    exclude:
      - '^docs:'
      - '^test:'
      - Merge pull request
      - Merge branch
      - go mod tidy
snapshot:
  name_template: "{{ .Tag }}-next"
```

## File: `.travis.yml`
```yaml
language: go
sudo: required

matrix:
  allow_failures:
    - go: master
  include:
    # Supported versions of Go: https://golang.org/dl/
    - go: "1.14.x"
    - go: "1.15.x"
    - go: master

go_import_path: github.com/golang-migrate/migrate

env:
  global:
    - GO111MODULE=on
    - MIGRATE_TEST_CONTAINER_BOOT_TIMEOUT=60
    - DOCKER_USERNAME=golangmigrate
    -   secure: "oSOznzUrgr5h45qW4PONkREpisPAt40tnM+KFWtS/Ggu5UI2Ie0CmyYXWuBjbt7B97a4yN9Qzmn8FxJHJ7kk+ABOi3muhkxeIhr6esXbzHhX/Jhv0mj1xkzX7KoVN9oHBz3cOI/QeRyEAO68xjDHNE2kby4RTT9VBt6TQUakKVkqI5qkqLBTADepCjVC+9XhxVxUNyeWKU8ormaUfJBjoNVoDlwXekUPnJenfmfZqXxUInvBCfUyp7Pq+kurBORmg4yc6qOlRYuK67Xw+i5xpjbZouNlXPk0rq7pPy5zjhmZQ3kImoFPvNMeKViDcI6kSIJKtjdhms9/g/6MgXS9HlL5kFy8tYKbsyiHnHB1BsvaLAKXctbUZFDPstgMPADfnad2kZXPrNqIhfWKZrGRWidawCYJ1sKKwYxLMKrtA0umqgMoL90MmBOELhuGmvMV0cFJB+zo+K2YWjEiMGd8xRb5mC5aAy0ZcCehO46jGtpr217EJmMF8Ywr7cFqM2Shg5U2jev9qUpYiXwmPnJKDuoT2ZHuHmPgFIkYiWC5yeJnnmG5bed1sKBp93AFrJX+1Rx5oC4BpNegewmBZKpOSwls/D1uMAeQK3dPmQHLsT6o2VBLfeDGr+zY0R85ywwPZCv00vGol02zYoTqN7eFqr6Qhjr/qx5K1nnxJdFK3Ts="

services:
  - docker

cache:
  directories:
    - $GOPATH/pkg


before_install:
  # Update docker to latest version: https://docs.travis-ci.com/user/docker/#installing-a-newer-docker-version
  - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  - sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  - sudo apt-get update
  - sudo apt-get -y -o Dpkg::Options::="--force-confnew" install docker-ce
  # Install golangci-lint
  - curl -sfL https://install.goreleaser.com/github.com/golangci/golangci-lint.sh | sh -s -- -b $(go env GOPATH)/bin v1.30.0
  - echo "TRAVIS_GO_VERSION=${TRAVIS_GO_VERSION}"

install:
  - go get github.com/mattn/goveralls

script:
  - golangci-lint run
  - make test COVERAGE_DIR=/tmp/coverage

after_success:
  - goveralls -service=travis-ci -coverprofile /tmp/coverage/combined.txt
  - make list-external-deps > dependency_tree.txt && cat dependency_tree.txt
  - make build-cli
  - gem install --no-document fpm
  - fpm -s dir -t deb -n migrate -v "$(git describe --tags 2>/dev/null | cut -c 2-)" --license MIT -m dhui@users.noreply.github.com --url https://github.com/golang-migrate/migrate --description='Database migrations' -a amd64 -p migrate.$(git describe --tags 2>/dev/null | cut -c 2-).deb --deb-no-default-config-files -f -C cli/build migrate.linux-amd64=/usr/local/bin/migrate

deploy:
  - provider: releases
    api_key:
      secure: hWH1HLPpzpfA8pXQ93T1qKQVFSpQp0as/JLQ7D91jHuJ8p+RxVeqblDrR6HQY/95R/nyiE9GJmvUolSuw5h449LSrGxPtVWhdh6EnkxlQHlen5XeMhVjRjFV0sE9qGe8v7uAkiTfRO61ktTWHrEAvw5qpyqnNISodmZS78XIasPODQbNlzwINhWhDTHIjXGb4FpizYaL3OGCanrxfR9fQyCaqKGGBjRq3Mfq8U6Yd4mApmsE+uJxgaZV8K5zBqpkSzQRWhcVGNL5DuLsU3gfSJOo7kZeA2G71SHffH577dBoqtCZ4VFv169CoUZehLWCb+7XKJZmHXVujCURATSySLGUOPc6EoLFAn3YtsCA04mS4bZVo5FZPWVwfhjmkhtDR4f6wscKp7r1HsFHSOgm59QfETQdrn4MnZ44H2Jd39axqndn5DvK9EcZVjPHynOPnueXP2u6mTuUgh2VyyWBCDO3CNo0fGlo7VJI69IkIWNSD87K9cHZWYMClyKZkUzS+PmRAhHRYbVd+9ZjKOmnU36kUHNDG/ft1D4ogsY+rhVtXB4lgWDM5adri+EIScYdYnB1/pQexLBigcJY9uE7nQTR0U6QgVNYvun7uRNs40E0c4voSfmPdFO0FlOD2y1oQhnaXfWLbu9nMcTcs4RFGrcC7NzkUN4/WjG8s285V6w=
    skip_cleanup: true
    on:
      go: "1.15.x"
      repo: golang-migrate/migrate
      tags: true
    file:
      - cli/build/migrate.linux-amd64.tar.gz
      - cli/build/migrate.linux-armv7.tar.gz
      - cli/build/migrate.linux-arm64.tar.gz
      - cli/build/migrate.darwin-amd64.tar.gz
      - cli/build/migrate.windows-amd64.exe.tar.gz
      - cli/build/migrate.windows-386.exe.tar.gz
      - cli/build/sha256sum.txt
      - dependency_tree.txt
  - provider: packagecloud
    repository: migrate
    username: golang-migrate
    token:
      secure: aICwu3gJ1sJ1QVCD3elpg+Jxzt4P+Zj1uoh5f0sOwnjDNIZ4FwUT1cMrWloP8P2KD0iyCOawuZER27o/kQ21oX2OxHvQbYPReA2znLm7lHzCmypAAOHPxpgnQ4rMGHHJXd+OsxtdclGs67c+EbdBfoRRbK400Qz/vjPJEDeH4mh02ZHC2nw4Nk/wV4jjBIkIt9dGEx6NgOA17FCMa3MaPHlHeFIzU7IfTlDHbS0mCCYbg/wafWBWcbGqtZLWAYtJDmfjrAStmDLdAX5J5PsB7taGSGPZHmPmpGoVgrKt/tb9Xz1rFBGslTpGROOiO4CiMAvkEKFn8mxrBGjfSBqp7Dp3eeSalKXB1DJAbEXx2sEbMcvmnoR9o43meaAn+ZRts8lRL8S/skBloe6Nk8bx3NlJCGB9WPK1G56b7c/fZnJxQbrCw6hxDfbZwm8S2YPviFTo/z1BfZDhRsL74reKsN2kgnGo2W/k38vvzIpsssQ9DHN1b0TLCxolCNPtQ7oHcQ1ohcjP2UgYXk0FhqDoL+9LQva/DU4N9sKH0UbAaqsMVSErLeG8A4aauuFcVrWRBaDYyTag4dQqzTulEy7iru2kDDIBgSQ1gMW/yoBOIPK4oi6MtbTf1X39fzXFLS1cDd3LW61yAu3YrbjAetpfx2frIvrRAiL9TxWA1gnrs5o=
    dist: ubuntu/xenial
    package_glob: '*.deb'
    skip_cleanup: true
    on:
      go: "1.15.x"
      repo: golang-migrate/migrate
      tags: true
  - provider: packagecloud
    repository: migrate
    username: golang-migrate
    token:
      secure: aICwu3gJ1sJ1QVCD3elpg+Jxzt4P+Zj1uoh5f0sOwnjDNIZ4FwUT1cMrWloP8P2KD0iyCOawuZER27o/kQ21oX2OxHvQbYPReA2znLm7lHzCmypAAOHPxpgnQ4rMGHHJXd+OsxtdclGs67c+EbdBfoRRbK400Qz/vjPJEDeH4mh02ZHC2nw4Nk/wV4jjBIkIt9dGEx6NgOA17FCMa3MaPHlHeFIzU7IfTlDHbS0mCCYbg/wafWBWcbGqtZLWAYtJDmfjrAStmDLdAX5J5PsB7taGSGPZHmPmpGoVgrKt/tb9Xz1rFBGslTpGROOiO4CiMAvkEKFn8mxrBGjfSBqp7Dp3eeSalKXB1DJAbEXx2sEbMcvmnoR9o43meaAn+ZRts8lRL8S/skBloe6Nk8bx3NlJCGB9WPK1G56b7c/fZnJxQbrCw6hxDfbZwm8S2YPviFTo/z1BfZDhRsL74reKsN2kgnGo2W/k38vvzIpsssQ9DHN1b0TLCxolCNPtQ7oHcQ1ohcjP2UgYXk0FhqDoL+9LQva/DU4N9sKH0UbAaqsMVSErLeG8A4aauuFcVrWRBaDYyTag4dQqzTulEy7iru2kDDIBgSQ1gMW/yoBOIPK4oi6MtbTf1X39fzXFLS1cDd3LW61yAu3YrbjAetpfx2frIvrRAiL9TxWA1gnrs5o=
    dist: ubuntu/bionic
    package_glob: '*.deb'
    skip_cleanup: true
    on:
      go: "1.15.x"
      repo: golang-migrate/migrate
      tags: true
  - provider: packagecloud
    repository: migrate
    username: golang-migrate
    token:
      secure: aICwu3gJ1sJ1QVCD3elpg+Jxzt4P+Zj1uoh5f0sOwnjDNIZ4FwUT1cMrWloP8P2KD0iyCOawuZER27o/kQ21oX2OxHvQbYPReA2znLm7lHzCmypAAOHPxpgnQ4rMGHHJXd+OsxtdclGs67c+EbdBfoRRbK400Qz/vjPJEDeH4mh02ZHC2nw4Nk/wV4jjBIkIt9dGEx6NgOA17FCMa3MaPHlHeFIzU7IfTlDHbS0mCCYbg/wafWBWcbGqtZLWAYtJDmfjrAStmDLdAX5J5PsB7taGSGPZHmPmpGoVgrKt/tb9Xz1rFBGslTpGROOiO4CiMAvkEKFn8mxrBGjfSBqp7Dp3eeSalKXB1DJAbEXx2sEbMcvmnoR9o43meaAn+ZRts8lRL8S/skBloe6Nk8bx3NlJCGB9WPK1G56b7c/fZnJxQbrCw6hxDfbZwm8S2YPviFTo/z1BfZDhRsL74reKsN2kgnGo2W/k38vvzIpsssQ9DHN1b0TLCxolCNPtQ7oHcQ1ohcjP2UgYXk0FhqDoL+9LQva/DU4N9sKH0UbAaqsMVSErLeG8A4aauuFcVrWRBaDYyTag4dQqzTulEy7iru2kDDIBgSQ1gMW/yoBOIPK4oi6MtbTf1X39fzXFLS1cDd3LW61yAu3YrbjAetpfx2frIvrRAiL9TxWA1gnrs5o=
    dist: ubuntu/focal
    package_glob: '*.deb'
    skip_cleanup: true
    on:
      go: "1.15.x"
      repo: golang-migrate/migrate
      tags: true
  - provider: packagecloud
    repository: migrate
    username: golang-migrate
    token:
      secure: aICwu3gJ1sJ1QVCD3elpg+Jxzt4P+Zj1uoh5f0sOwnjDNIZ4FwUT1cMrWloP8P2KD0iyCOawuZER27o/kQ21oX2OxHvQbYPReA2znLm7lHzCmypAAOHPxpgnQ4rMGHHJXd+OsxtdclGs67c+EbdBfoRRbK400Qz/vjPJEDeH4mh02ZHC2nw4Nk/wV4jjBIkIt9dGEx6NgOA17FCMa3MaPHlHeFIzU7IfTlDHbS0mCCYbg/wafWBWcbGqtZLWAYtJDmfjrAStmDLdAX5J5PsB7taGSGPZHmPmpGoVgrKt/tb9Xz1rFBGslTpGROOiO4CiMAvkEKFn8mxrBGjfSBqp7Dp3eeSalKXB1DJAbEXx2sEbMcvmnoR9o43meaAn+ZRts8lRL8S/skBloe6Nk8bx3NlJCGB9WPK1G56b7c/fZnJxQbrCw6hxDfbZwm8S2YPviFTo/z1BfZDhRsL74reKsN2kgnGo2W/k38vvzIpsssQ9DHN1b0TLCxolCNPtQ7oHcQ1ohcjP2UgYXk0FhqDoL+9LQva/DU4N9sKH0UbAaqsMVSErLeG8A4aauuFcVrWRBaDYyTag4dQqzTulEy7iru2kDDIBgSQ1gMW/yoBOIPK4oi6MtbTf1X39fzXFLS1cDd3LW61yAu3YrbjAetpfx2frIvrRAiL9TxWA1gnrs5o=
    dist: debian/stretch
    package_glob: '*.deb'
    skip_cleanup: true
    on:
      go: "1.15.x"
      repo: golang-migrate/migrate
      tags: true
  - provider: packagecloud
    repository: migrate
    username: golang-migrate
    token:
      secure: aICwu3gJ1sJ1QVCD3elpg+Jxzt4P+Zj1uoh5f0sOwnjDNIZ4FwUT1cMrWloP8P2KD0iyCOawuZER27o/kQ21oX2OxHvQbYPReA2znLm7lHzCmypAAOHPxpgnQ4rMGHHJXd+OsxtdclGs67c+EbdBfoRRbK400Qz/vjPJEDeH4mh02ZHC2nw4Nk/wV4jjBIkIt9dGEx6NgOA17FCMa3MaPHlHeFIzU7IfTlDHbS0mCCYbg/wafWBWcbGqtZLWAYtJDmfjrAStmDLdAX5J5PsB7taGSGPZHmPmpGoVgrKt/tb9Xz1rFBGslTpGROOiO4CiMAvkEKFn8mxrBGjfSBqp7Dp3eeSalKXB1DJAbEXx2sEbMcvmnoR9o43meaAn+ZRts8lRL8S/skBloe6Nk8bx3NlJCGB9WPK1G56b7c/fZnJxQbrCw6hxDfbZwm8S2YPviFTo/z1BfZDhRsL74reKsN2kgnGo2W/k38vvzIpsssQ9DHN1b0TLCxolCNPtQ7oHcQ1ohcjP2UgYXk0FhqDoL+9LQva/DU4N9sKH0UbAaqsMVSErLeG8A4aauuFcVrWRBaDYyTag4dQqzTulEy7iru2kDDIBgSQ1gMW/yoBOIPK4oi6MtbTf1X39fzXFLS1cDd3LW61yAu3YrbjAetpfx2frIvrRAiL9TxWA1gnrs5o=
    dist: debian/buster
    package_glob: '*.deb'
    skip_cleanup: true
    on:
      go: "1.15.x"
      repo: golang-migrate/migrate
      tags: true
  - provider: script
    script: ./docker-deploy.sh
    skip_cleanup: true
    on:
      go: "1.15.x"
      repo: golang-migrate/migrate
      tags: true
```

## File: `CONTRIBUTING.md`
```markdown
# Development, Testing and Contributing

  1. Make sure you have a running Docker daemon
     (Install for [MacOS](https://docs.docker.com/docker-for-mac/))
  1. Use a version of Go that supports [modules](https://golang.org/cmd/go/#hdr-Modules__module_versions__and_more) (e.g. Go 1.11+)
  1. Fork this repo and `git clone` somewhere to `$GOPATH/src/github.com/golang-migrate/migrate`
      * Ensure that [Go modules are enabled](https://golang.org/cmd/go/#hdr-Preliminary_module_support) (e.g. your repo path or the `GO111MODULE` environment variable are set correctly)
  1. Install [golangci-lint](https://github.com/golangci/golangci-lint#install)
  1. Run the linter: `golangci-lint run`
  1. Confirm tests are working: `make test-short`
  1. Write awesome code ...
  1. `make test` to run all tests against all database versions
  1. Push code and open Pull Request
 
Some more helpful commands:

  * You can specify which database/ source tests to run:
    `make test-short SOURCE='file go_bindata' DATABASE='postgres cassandra'`
  * After `make test`, run `make html-coverage` which opens a shiny test coverage overview.
  * `make build-cli` builds the CLI in directory `cli/build/`.
  * `make list-external-deps` lists all external dependencies for each package
  * `make docs && make open-docs` opens godoc in your browser, `make kill-docs` kills the godoc server.
    Repeatedly call `make docs` to refresh the server.
  * Set the `DOCKER_API_VERSION` environment variable to the latest supported version if you get errors regarding the docker client API version being too new.
```

## File: `docker-deploy.sh`
```bash
#!/bin/bash

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin && \
docker build --build-arg VERSION="$TRAVIS_TAG" . -t migrate/migrate -t migrate/migrate:"$TRAVIS_TAG" && \
docker push migrate/migrate:"$TRAVIS_TAG" && docker push migrate/migrate
```

## File: `Dockerfile`
```
FROM golang:1.25-alpine3.21 AS builder
ARG VERSION

RUN apk add --no-cache git gcc musl-dev make

WORKDIR /go/src/github.com/golang-migrate/migrate

ENV GO111MODULE=on

COPY go.mod go.sum ./

RUN go mod download

COPY . ./

RUN make build-docker

FROM alpine:3.21

RUN apk add --no-cache ca-certificates

COPY --from=builder /go/src/github.com/golang-migrate/migrate/build/migrate.linux-386 /usr/local/bin/migrate
RUN ln -s /usr/local/bin/migrate /migrate

ENTRYPOINT ["migrate"]
CMD ["--help"]
```

## File: `Dockerfile.circleci`
```
ARG DOCKER_IMAGE
FROM $DOCKER_IMAGE

RUN apk add --no-cache git gcc musl-dev make

WORKDIR /go/src/github.com/golang-migrate/migrate

ENV GO111MODULE=on
ENV COVERAGE_DIR=/tmp/coverage

COPY go.mod go.sum ./

RUN go mod download

COPY . ./

CMD ["make", "test"]
```

## File: `Dockerfile.github-actions`
```
FROM alpine:3.19

RUN apk add --no-cache ca-certificates

COPY migrate /usr/local/bin/migrate

RUN ln -s /usr/local/bin/migrate /usr/bin/migrate
RUN ln -s /usr/local/bin/migrate /migrate

ENTRYPOINT ["migrate"]
CMD ["--help"]
```

## File: `FAQ.md`
```markdown
# FAQ

#### How is the code base structured?
  ```
  /          package migrate (the heart of everything)
  /cli       the CLI wrapper
  /database  database driver and sub directories have the actual driver implementations
  /source    source driver and sub directories have the actual driver implementations
  ```

#### Why is there no `source/driver.go:Last()`?
  It's not needed. And unless the source has a "native" way to read a directory in reversed order,
  it might be expensive to do a full directory scan in order to get the last element.

#### What is a NilMigration? NilVersion?
  NilMigration defines a migration without a body. NilVersion is defined as const -1.

#### What is the difference between uint(version) and int(targetVersion)?
  version refers to an existing migration version coming from a source and therefore can never be negative.
  targetVersion can either be a version OR represent a NilVersion, which equals -1.

#### What's the difference between Next/Previous and Up/Down?
  ```
  1_first_migration.up.extension           next ->  2_second_migration.up.extension      ...
  1_first_migration.down.extension  <- previous     2_second_migration.down.extension    ...
  ```

#### Why two separate files (up and down) for a migration?
  It makes all of our lives easier. No new markup/syntax to learn for users
  and existing database utility tools continue to work as expected.

#### How many migrations can migrate handle?
  Whatever the maximum positive signed integer value is for your platform.
  For 32bit it would be 2,147,483,647 migrations. Migrate only keeps references to
  the currently run and pre-fetched migrations in memory. Please note that some
  source drivers need to do build a full "directory" tree first, which puts some
  heat on the memory consumption.

#### Are the table tests in migrate_test.go bloated?
  Yes and no. There are duplicate test cases for sure but they don't hurt here. In fact
  the tests are very visual now and might help new users understand expected behaviors quickly.
  Migrate from version x to y and y is the last migration? Just check out the test for
  that particular case and know what's going on instantly.

#### What is Docker being used for?
  Only for testing. See [testing/docker.go](testing/docker.go)

#### Why not just use docker-compose?
  It doesn't give us enough runtime control for testing. We want to be able to bring up containers fast
  and whenever we want, not just once at the beginning of all tests.

#### Can I maintain my driver in my own repository?
  Yes, technically thats possible. We want to encourage you to contribute your driver to this repository though.
  The driver's functionality is dictated by migrate's interfaces. That means there should really
  just be one driver for a database/ source. We want to prevent a future where several drivers doing the exact same thing,
  just implemented a bit differently, co-exist somewhere on GitHub. If users have to do research first to find the
  "best" available driver for a database in order to get started, we would have failed as an open source community.

#### Can I mix multiple sources during a batch of migrations?
  No.

#### What does "dirty" database mean?
  Before a migration runs, each database sets a dirty flag. Execution stops if a migration fails and the dirty state persists,
  which prevents attempts to run more migrations on top of a failed migration. You need to manually fix the error
  and then "force" the expected version.

#### What happens if two programs try and update the database at the same time?
  Database-specific locking features are used by *some* database drivers to prevent multiple instances of migrate from running migrations on
  the same database at the same time. For example, the MySQL driver uses the `GET_LOCK` function, while the Postgres driver uses
  the `pg_advisory_lock` function.

#### Do I need to create a table for tracking migration version used?
No, it is done automatically.

#### Can I use migrate with a non-Go project?
Yes, you can use the migrate CLI in a non-Go project, but there are probably other libraries/frameworks available that offer better test and deploy integrations in that language/framework.

#### I have got an error `Dirty database version 1. Fix and force version`. What should I do?
Keep calm and refer to [the getting started docs](../corp/docs/usage_guides/getting_started.md#forcing-your-database-version).
```

## File: `GETTING_STARTED.md`
```markdown
# Getting started
Before you start, you should understand the concept of forward/up and reverse/down database migrations.

Configure a database for your application. Make sure that your database driver is supported [here](README.md#databases).

## Create migrations
Create some migrations using migrate CLI. Here is an example:
```
migrate create -ext sql -dir db/migrations -seq create_users_table
```
Once you create your files, you should fill them.

**IMPORTANT:** In a project developed by more than one person there is a chance of migrations inconsistency - e.g. two developers can create conflicting migrations, and the developer that created their migration later gets it merged to the repository first.
Developers and Teams should keep an eye on such cases (especially during code review).
[Here](https://github.com/golang-migrate/migrate/issues/179#issuecomment-475821264) is the issue summary if you would like to read more.

Consider making your migrations idempotent - we can run the same sql code twice in a row with the same result. This makes our migrations more robust. On the other hand, it causes slightly less control over database schema - e.g. let's say you forgot to drop the table in down migration. You run down migration - the table is still there. When you run up migration again - `CREATE TABLE` would return an error, helping you find an issue in down migration, while `CREATE TABLE IF NOT EXISTS` would not. Use those conditions wisely.

In case you would like to run several commands/queries in one migration, you should wrap them in a transaction (if your database supports it).
This way if one of commands fails, our database will remain unchanged.

## Run migrations
Run your migrations through the CLI or your app and check if they applied expected changes.
Just to give you an idea:
```
migrate -database YOUR_DATABASE_URL -path PATH_TO_YOUR_MIGRATIONS up
```

Just add the code to your app and you're ready to go!

Before committing your migrations you should run your migrations up, down, and then up again to see if migrations are working properly both ways.
(e.g. if you created a table in a migration but reverse migration did not delete it, you will encounter an error when running the forward migration again)
It's also worth checking your migrations in a separate, containerized environment. You can find some tools at the [end of this document](#further-reading).

**IMPORTANT:** If you would like to run multiple instances of your app on different machines be sure to use a database that supports locking when running migrations. Otherwise you may encounter issues.

## Forcing your database version
In case you run a migration that contained an error, migrate will not let you run other migrations on the same database. You will see an error like `Dirty database version 1. Fix and force version`, even when you fix the erred migration. This means your database was marked as 'dirty'.
You need to investigate the migration error - was your migration applied partially, or was it not applied at all? Once you know, you should force your database to a version reflecting it's real state. You can do so with `force` command:
```
migrate -path PATH_TO_YOUR_MIGRATIONS -database YOUR_DATABASE_URL force VERSION
```
Once you force the version and your migration was fixed, your database is 'clean' again and you can proceed with your migrations.

For details and example of usage see [this comment](https://github.com/golang-migrate/migrate/issues/282#issuecomment-530743258).

## Further reading:
- [PostgreSQL tutorial](../../../core/security/QUARANTINE/vetted/repos/documentation/i18n/en/docusaurus_plugin_content_docs/current/get_started/tutorial.md)
- [Best practices](MIGRATIONS.md)
- [FAQ](FAQ.md)
- Tools for testing your migrations in a container:
	- https://github.com/dhui/dktest
	- https://github.com/ory/dockertest
```

## File: `go.mod`
```
module github.com/golang-migrate/migrate/v4

go 1.24.0

require (
	cloud.google.com/go/spanner v1.85.0
	cloud.google.com/go/storage v1.56.0
	github.com/Azure/go-autorest/autorest/adal v0.9.16
	github.com/ClickHouse/clickhouse-go v1.4.3
	github.com/aws/aws-sdk-go v1.49.6
	github.com/cenkalti/backoff/v4 v4.1.2
	github.com/cockroachdb/cockroach-go/v2 v2.1.1
	github.com/dhui/dktest v0.4.6
	github.com/docker/docker v28.3.3+incompatible
	github.com/fsouza/fake-gcs-server v1.17.0
	github.com/go-sql-driver/mysql v1.5.0
	github.com/gobuffalo/here v0.6.0
	github.com/gocql/gocql v0.0.0-20210515062232-b7ef815b4556
	github.com/google/go-github/v39 v39.2.0
	github.com/jackc/pgconn v1.14.3
	github.com/jackc/pgerrcode v0.0.0-20220416144525-469b46aa5efa
	github.com/jackc/pgx/v4 v4.18.2
	github.com/jackc/pgx/v5 v5.7.6
	github.com/ktrysmt/go-bitbucket v0.6.4
	github.com/lib/pq v1.10.9
	github.com/markbates/pkger v0.15.1
	github.com/mattn/go-sqlite3 v1.14.22
	github.com/microsoft/go-mssqldb v1.0.0
	github.com/mutecomm/go-sqlcipher/v4 v4.4.0
	github.com/nakagami/firebirdsql v0.0.0-20190310045651-3c02a58cfed8
	github.com/neo4j/neo4j-go-driver v1.8.1-0.20200803113522-b626aa943eba
	github.com/snowflakedb/gosnowflake v1.6.19
	github.com/stretchr/testify v1.11.1
	github.com/xanzy/go-gitlab v0.15.0
	go.mongodb.org/mongo-driver v1.7.5
	golang.org/x/oauth2 v0.30.0
	golang.org/x/tools/godoc v0.1.0-deprecated
	google.golang.org/api v0.247.0
	modernc.org/ql v1.0.0
	modernc.org/sqlite v1.18.1
)

require (
	cel.dev/expr v0.24.0 // indirect
	cloud.google.com/go/auth v0.16.4 // indirect
	cloud.google.com/go/auth/oauth2adapt v0.2.8 // indirect
	cloud.google.com/go/monitoring v1.24.2 // indirect
	github.com/GoogleCloudPlatform/grpc-gcp-go/grpcgcp v1.5.3 // indirect
	github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.27.0 // indirect
	github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric v0.53.0 // indirect
	github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping v0.53.0 // indirect
	github.com/containerd/errdefs v1.0.0 // indirect
	github.com/containerd/errdefs/pkg v0.3.0 // indirect
	github.com/distribution/reference v0.6.0 // indirect
	github.com/docker/go-connections v0.5.0 // indirect
	github.com/envoyproxy/go-control-plane/envoy v1.32.4 // indirect
	github.com/felixge/httpsnoop v1.0.4 // indirect
	github.com/go-jose/go-jose/v4 v4.0.5 // indirect
	github.com/go-logr/logr v1.4.3 // indirect
	github.com/go-logr/stdr v1.2.2 // indirect
	github.com/jackc/puddle/v2 v2.2.2 // indirect
	github.com/moby/docker-image-spec v1.3.1 // indirect
	github.com/moby/sys/sequential v0.6.0 // indirect
	github.com/planetscale/vtprotobuf v0.6.1-0.20240319094008-0393e58bdf10 // indirect
	github.com/spiffe/go-spiffe/v2 v2.5.0 // indirect
	github.com/zeebo/errs v1.4.0 // indirect
	go.opentelemetry.io/auto/sdk v1.2.1 // indirect
	go.opentelemetry.io/contrib/detectors/gcp v1.36.0 // indirect
	go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc v0.61.0 // indirect
	go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp v0.61.0 // indirect
	go.opentelemetry.io/otel v1.40.0 // indirect
	go.opentelemetry.io/otel/exporters/otlp/otlptrace v1.29.0 // indirect
	go.opentelemetry.io/otel/metric v1.40.0 // indirect
	go.opentelemetry.io/otel/sdk v1.40.0 // indirect
	go.opentelemetry.io/otel/sdk/metric v1.40.0 // indirect
	go.opentelemetry.io/otel/trace v1.40.0 // indirect
	go.opentelemetry.io/proto/otlp v1.3.1 // indirect
	golang.org/x/telemetry v0.0.0-20251008203120-078029d740a8 // indirect
	golang.org/x/tools v0.38.0 // indirect
)

require (
	cloud.google.com/go v0.121.6 // indirect
	cloud.google.com/go/compute/metadata v0.8.0 // indirect
	cloud.google.com/go/iam v1.5.2 // indirect
	cloud.google.com/go/longrunning v0.6.7 // indirect
	github.com/99designs/go-keychain v0.0.0-20191008050251-8e49817e8af4 // indirect
	github.com/99designs/keyring v1.2.1 // indirect
	github.com/Azure/azure-sdk-for-go/sdk/azcore v1.4.0 // indirect
	github.com/Azure/azure-sdk-for-go/sdk/internal v1.1.2 // indirect
	github.com/Azure/azure-sdk-for-go/sdk/storage/azblob v1.0.0 // indirect
	github.com/Azure/go-ansiterm v0.0.0-20230124172434-306776ec8161 // indirect
	github.com/Azure/go-autorest v14.2.0+incompatible // indirect
	github.com/Azure/go-autorest/autorest/date v0.3.0 // indirect
	github.com/Azure/go-autorest/logger v0.2.1 // indirect
	github.com/Azure/go-autorest/tracing v0.6.0 // indirect
	github.com/Microsoft/go-winio v0.6.2 // indirect
	github.com/andybalholm/brotli v1.0.4 // indirect
	github.com/apache/arrow/go/v10 v10.0.1 // indirect
	github.com/apache/thrift v0.16.0 // indirect
	github.com/aws/aws-sdk-go-v2 v1.16.16 // indirect
	github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream v1.4.8 // indirect
	github.com/aws/aws-sdk-go-v2/credentials v1.12.20 // indirect
	github.com/aws/aws-sdk-go-v2/feature/s3/manager v1.11.33 // indirect
	github.com/aws/aws-sdk-go-v2/internal/configsources v1.1.23 // indirect
	github.com/aws/aws-sdk-go-v2/internal/endpoints/v2 v2.4.17 // indirect
	github.com/aws/aws-sdk-go-v2/internal/v4a v1.0.14 // indirect
	github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding v1.9.9 // indirect
	github.com/aws/aws-sdk-go-v2/service/internal/checksum v1.1.18 // indirect
	github.com/aws/aws-sdk-go-v2/service/internal/presigned-url v1.9.17 // indirect
	github.com/aws/aws-sdk-go-v2/service/internal/s3shared v1.13.17 // indirect
	github.com/aws/aws-sdk-go-v2/service/s3 v1.27.11 // indirect
	github.com/aws/smithy-go v1.13.3 // indirect
	github.com/cespare/xxhash/v2 v2.3.0 // indirect
	github.com/cloudflare/golz4 v0.0.0-20150217214814-ef862a3cdc58 // indirect
	github.com/cncf/xds/go v0.0.0-20250501225837-2ac532fd4443 // indirect
	github.com/cznic/mathutil v0.0.0-20180504122225-ca4c9f2c1369 // indirect
	github.com/danieljoos/wincred v1.1.2 // indirect
	github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc // indirect
	github.com/docker/go-units v0.5.0 // indirect
	github.com/dvsekhvalnov/jose2go v1.7.0 // indirect
	github.com/edsrzf/mmap-go v0.0.0-20170320065105-0bce6a688712 // indirect
	github.com/envoyproxy/protoc-gen-validate v1.2.1 // indirect
	github.com/form3tech-oss/jwt-go v3.2.5+incompatible // indirect
	github.com/gabriel-vasile/mimetype v1.4.1 // indirect
	github.com/go-stack/stack v1.8.0 // indirect
	github.com/goccy/go-json v0.9.11 // indirect
	github.com/godbus/dbus v0.0.0-20190726142602-4481cbc300e2 // indirect
	github.com/gogo/protobuf v1.3.2 // indirect
	github.com/golang-jwt/jwt/v4 v4.5.2 // indirect
	github.com/golang-sql/civil v0.0.0-20190719163853-cb61b32ac6fe // indirect
	github.com/golang-sql/sqlexp v0.1.0 // indirect
	github.com/golang/groupcache v0.0.0-20210331224755-41bb18bfe9da // indirect
	github.com/golang/snappy v0.0.4 // indirect
	github.com/google/flatbuffers v2.0.8+incompatible // indirect
	github.com/google/go-querystring v1.1.0 // indirect
	github.com/google/s2a-go v0.1.9 // indirect
	github.com/google/uuid v1.6.0 // indirect
	github.com/googleapis/enterprise-certificate-proxy v0.3.6 // indirect
	github.com/googleapis/gax-go/v2 v2.15.0 // indirect
	github.com/gorilla/handlers v1.4.2 // indirect
	github.com/gorilla/mux v1.7.4 // indirect
	github.com/gsterjov/go-libsecret v0.0.0-20161001094733-a6f4afe4910c // indirect
	github.com/hailocab/go-hostpool v0.0.0-20160125115350-e80d13ce29ed // indirect
	github.com/jackc/chunkreader/v2 v2.0.1 // indirect
	github.com/jackc/pgio v1.0.0 // indirect
	github.com/jackc/pgpassfile v1.0.0 // indirect
	github.com/jackc/pgproto3/v2 v2.3.3 // indirect
	github.com/jackc/pgservicefile v0.0.0-20240606120523-5a60cdf6a761 // indirect
	github.com/jackc/pgtype v1.14.0 // indirect
	github.com/jmespath/go-jmespath v0.4.0 // indirect
	github.com/k0kubun/pp v2.3.0+incompatible // indirect
	github.com/kardianos/osext v0.0.0-20190222173326-2bc1f35cddc0 // indirect
	github.com/kballard/go-shellquote v0.0.0-20180428030007-95032a82bc51 // indirect
	github.com/klauspost/asmfmt v1.3.2 // indirect
	github.com/klauspost/compress v1.15.11 // indirect
	github.com/klauspost/cpuid/v2 v2.0.9 // indirect
	github.com/mattn/go-colorable v0.1.6 // indirect
	github.com/mattn/go-isatty v0.0.16 // indirect
	github.com/minio/asm2plan9s v0.0.0-20200509001527-cdd76441f9d8 // indirect
	github.com/minio/c2goasm v0.0.0-20190812172519-36a3d3bbc4f3 // indirect
	github.com/mitchellh/mapstructure v1.1.2 // indirect
	github.com/moby/term v0.5.0 // indirect
	github.com/morikuni/aec v1.0.0 // indirect
	github.com/mtibben/percent v0.2.1 // indirect
	github.com/onsi/ginkgo v1.16.4 // indirect
	github.com/onsi/gomega v1.15.0 // indirect
	github.com/opencontainers/go-digest v1.0.0 // indirect
	github.com/opencontainers/image-spec v1.1.0 // indirect
	github.com/pierrec/lz4/v4 v4.1.16 // indirect
	github.com/pkg/browser v0.0.0-20210911075715-681adbf594b8 // indirect
	github.com/pkg/errors v0.9.1 // indirect
	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2 // indirect
	github.com/remyoudompheng/bigfft v0.0.0-20200410134404-eec4a21b6bb0 // indirect
	github.com/rqlite/gorqlite v0.0.0-20230708021416-2acd02b70b79
	github.com/shopspring/decimal v1.2.0 // indirect
	github.com/sirupsen/logrus v1.9.3 // indirect
	github.com/xdg-go/pbkdf2 v1.0.0 // indirect
	github.com/xdg-go/scram v1.1.1 // indirect
	github.com/xdg-go/stringprep v1.0.3 // indirect
	github.com/youmark/pkcs8 v0.0.0-20181117223130-1be2e3e5546d // indirect
	github.com/zeebo/xxh3 v1.0.2 // indirect
	gitlab.com/nyarla/go-crypt v0.0.0-20160106005555-d9a5dc2b789b // indirect
	go.opencensus.io v0.24.0 // indirect
	golang.org/x/crypto v0.45.0 // indirect
	golang.org/x/exp v0.0.0-20230315142452-642cacee5cc0 // indirect
	golang.org/x/mod v0.29.0 // indirect
	golang.org/x/net v0.47.0 // indirect
	golang.org/x/sync v0.18.0 // indirect
	golang.org/x/sys v0.40.0 // indirect
	golang.org/x/term v0.37.0 // indirect
	golang.org/x/text v0.31.0 // indirect
	golang.org/x/time v0.12.0 // indirect
	golang.org/x/xerrors v0.0.0-20231012003039-104605ab7028 // indirect
	google.golang.org/genproto v0.0.0-20250603155806-513f23925822 // indirect
	google.golang.org/genproto/googleapis/api v0.0.0-20250818200422-3122310a409c // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20250818200422-3122310a409c // indirect
	google.golang.org/grpc v1.74.2 // indirect
	google.golang.org/protobuf v1.36.7 // indirect
	gopkg.in/inf.v0 v0.9.1 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
	lukechampine.com/uint128 v1.2.0 // indirect
	modernc.org/b v1.0.0 // indirect
	modernc.org/cc/v3 v3.36.3 // indirect
	modernc.org/ccgo/v3 v3.16.9 // indirect
	modernc.org/db v1.0.0 // indirect
	modernc.org/file v1.0.0 // indirect
	modernc.org/fileutil v1.0.0 // indirect
	modernc.org/golex v1.0.0 // indirect
	modernc.org/internal v1.0.0 // indirect
	modernc.org/libc v1.17.1 // indirect
	modernc.org/lldb v1.0.0 // indirect
	modernc.org/mathutil v1.5.0 // indirect
	modernc.org/memory v1.2.1 // indirect
	modernc.org/opt v0.1.3 // indirect
	modernc.org/sortutil v1.1.0 // indirect
	modernc.org/strutil v1.1.3 // indirect
	modernc.org/token v1.0.0 // indirect
	modernc.org/zappy v1.0.0 // indirect
)
```

## File: `go.sum`
```
cel.dev/expr v0.24.0 h1:56OvJKSH3hDGL0ml5uSxZmz3/3Pq4tJ+fb1unVLAFcY=
cel.dev/expr v0.24.0/go.mod h1:hLPLo1W4QUmuYdA72RBX06QTs6MXw941piREPl3Yfiw=
cloud.google.com/go v0.26.0/go.mod h1:aQUYkXzVsufM+DwF1aE+0xfcU+56JwCaLick0ClmMTw=
cloud.google.com/go v0.34.0/go.mod h1:aQUYkXzVsufM+DwF1aE+0xfcU+56JwCaLick0ClmMTw=
cloud.google.com/go v0.38.0/go.mod h1:990N+gfupTy94rShfmMCWGDn0LpTmnzTp2qbd1dvSRU=
cloud.google.com/go v0.44.1/go.mod h1:iSa0KzasP4Uvy3f1mN/7PiObzGgflwredwwASm/v6AU=
cloud.google.com/go v0.44.2/go.mod h1:60680Gw3Yr4ikxnPRS/oxxkBccT6SA1yMk63TGekxKY=
cloud.google.com/go v0.44.3/go.mod h1:60680Gw3Yr4ikxnPRS/oxxkBccT6SA1yMk63TGekxKY=
cloud.google.com/go v0.45.1/go.mod h1:RpBamKRgapWJb87xiFSdk4g1CME7QZg3uwTez+TSTjc=
cloud.google.com/go v0.46.3/go.mod h1:a6bKKbmY7er1mI7TEI4lsAkts/mkhTSZK8w33B4RAg0=
cloud.google.com/go v0.50.0/go.mod h1:r9sluTvynVuxRIOHXQEHMFffphuXHOMZMycpNR5e6To=
cloud.google.com/go v0.52.0/go.mod h1:pXajvRH/6o3+F9jDHZWQ5PbGhn+o8w9qiu/CffaVdO4=
cloud.google.com/go v0.53.0/go.mod h1:fp/UouUEsRkN6ryDKNW/Upv/JBKnv6WDthjR6+vze6M=
cloud.google.com/go v0.54.0/go.mod h1:1rq2OEkV3YMf6n/9ZvGWI3GWw0VoqH/1x2nd8Is/bPc=
cloud.google.com/go v0.56.0/go.mod h1:jr7tqZxxKOVYizybht9+26Z/gUq7tiRzu+ACVAMbKVk=
cloud.google.com/go v0.57.0/go.mod h1:oXiQ6Rzq3RAkkY7N6t3TcE6jE+CIBBbA36lwQ1JyzZs=
cloud.google.com/go v0.62.0/go.mod h1:jmCYTdRCQuc1PHIIJ/maLInMho30T/Y0M4hTdTShOYc=
cloud.google.com/go v0.65.0/go.mod h1:O5N8zS7uWy9vkA9vayVHs65eM1ubvY4h553ofrNHObY=
cloud.google.com/go v0.72.0/go.mod h1:M+5Vjvlc2wnp6tjzE102Dw08nGShTscUx2nZMufOKPI=
cloud.google.com/go v0.74.0/go.mod h1:VV1xSbzvo+9QJOxLDaJfTjx5e+MePCpCWwvftOeQmWk=
cloud.google.com/go v0.75.0/go.mod h1:VGuuCn7PG0dwsd5XPVm2Mm3wlh3EL55/79EKB6hlPTY=
cloud.google.com/go v0.78.0/go.mod h1:QjdrLG0uq+YwhjoVOLsS1t7TW8fs36kLs4XO5R5ECHg=
cloud.google.com/go v0.79.0/go.mod h1:3bzgcEeQlzbuEAYu4mrWhKqWjmpprinYgKJLgKHnbb8=
cloud.google.com/go v0.81.0/go.mod h1:mk/AM35KwGk/Nm2YSeZbxXdrNK3KZOYHmLkOqC2V6E0=
cloud.google.com/go v0.83.0/go.mod h1:Z7MJUsANfY0pYPdw0lbnivPx4/vhy/e2FEkSkF7vAVY=
cloud.google.com/go v0.84.0/go.mod h1:RazrYuxIK6Kb7YrzzhPoLmCVzl7Sup4NrbKPg8KHSUM=
cloud.google.com/go v0.87.0/go.mod h1:TpDYlFy7vuLzZMMZ+B6iRiELaY7z/gJPaqbMx6mlWcY=
cloud.google.com/go v0.90.0/go.mod h1:kRX0mNRHe0e2rC6oNakvwQqzyDmg57xJ+SZU1eT2aDQ=
cloud.google.com/go v0.93.3/go.mod h1:8utlLll2EF5XMAV15woO4lSbWQlk8rer9aLOfLh7+YI=
cloud.google.com/go v0.94.1/go.mod h1:qAlAugsXlC+JWO+Bke5vCtc9ONxjQT3drlTTnAplMW4=
cloud.google.com/go v0.97.0/go.mod h1:GF7l59pYBVlXQIBLx3a761cZ41F9bBH3JUlihCt2Udc=
cloud.google.com/go v0.99.0/go.mod h1:w0Xx2nLzqWJPuozYQX+hFfCSI8WioryfRDzkoI/Y2ZA=
cloud.google.com/go v0.100.1/go.mod h1:fs4QogzfH5n2pBXBP9vRiU+eCny7lD2vmFZy79Iuw1U=
cloud.google.com/go v0.100.2/go.mod h1:4Xra9TjzAeYHrl5+oeLlzbM2k3mjVhZh4UqTZ//w99A=
cloud.google.com/go v0.102.0/go.mod h1:oWcCzKlqJ5zgHQt9YsaeTY9KzIvjyy0ArmiBUgpQ+nc=
cloud.google.com/go v0.102.1/go.mod h1:XZ77E9qnTEnrgEOvr4xzfdX5TRo7fB4T2F4O6+34hIU=
cloud.google.com/go v0.104.0/go.mod h1:OO6xxXdJyvuJPcEPBLN9BJPD+jep5G1+2U5B5gkRYtA=
cloud.google.com/go v0.105.0/go.mod h1:PrLgOJNe5nfE9UMxKxgXj4mD3voiP+YQ6gdt6KMFOKM=
cloud.google.com/go v0.107.0/go.mod h1:wpc2eNrD7hXUTy8EKS10jkxpZBjASrORK7goS+3YX2I=
cloud.google.com/go v0.110.0/go.mod h1:SJnCLqQ0FCFGSZMUNUf84MV3Aia54kn7pi8st7tMzaY=
cloud.google.com/go v0.121.6 h1:waZiuajrI28iAf40cWgycWNgaXPO06dupuS+sgibK6c=
cloud.google.com/go v0.121.6/go.mod h1:coChdst4Ea5vUpiALcYKXEpR1S9ZgXbhEzzMcMR66vI=
cloud.google.com/go/accessapproval v1.4.0/go.mod h1:zybIuC3KpDOvotz59lFe5qxRZx6C75OtwbisN56xYB4=
cloud.google.com/go/accessapproval v1.5.0/go.mod h1:HFy3tuiGvMdcd/u+Cu5b9NkO1pEICJ46IR82PoUdplw=
cloud.google.com/go/accessapproval v1.6.0/go.mod h1:R0EiYnwV5fsRFiKZkPHr6mwyk2wxUJ30nL4j2pcFY2E=
cloud.google.com/go/accesscontextmanager v1.3.0/go.mod h1:TgCBehyr5gNMz7ZaH9xubp+CE8dkrszb4oK9CWyvD4o=
cloud.google.com/go/accesscontextmanager v1.4.0/go.mod h1:/Kjh7BBu/Gh83sv+K60vN9QE5NJcd80sU33vIe2IFPE=
cloud.google.com/go/accesscontextmanager v1.6.0/go.mod h1:8XCvZWfYw3K/ji0iVnp+6pu7huxoQTLmxAbVjbloTtM=
cloud.google.com/go/accesscontextmanager v1.7.0/go.mod h1:CEGLewx8dwa33aDAZQujl7Dx+uYhS0eay198wB/VumQ=
cloud.google.com/go/aiplatform v1.22.0/go.mod h1:ig5Nct50bZlzV6NvKaTwmplLLddFx0YReh9WfTO5jKw=
cloud.google.com/go/aiplatform v1.24.0/go.mod h1:67UUvRBKG6GTayHKV8DBv2RtR1t93YRu5B1P3x99mYY=
cloud.google.com/go/aiplatform v1.27.0/go.mod h1:Bvxqtl40l0WImSb04d0hXFU7gDOiq9jQmorivIiWcKg=
cloud.google.com/go/aiplatform v1.35.0/go.mod h1:7MFT/vCaOyZT/4IIFfxH4ErVg/4ku6lKv3w0+tFTgXQ=
cloud.google.com/go/aiplatform v1.36.1/go.mod h1:WTm12vJRPARNvJ+v6P52RDHCNe4AhvjcIZ/9/RRHy/k=
cloud.google.com/go/aiplatform v1.37.0/go.mod h1:IU2Cv29Lv9oCn/9LkFiiuKfwrRTq+QQMbW+hPCxJGZw=
cloud.google.com/go/analytics v0.11.0/go.mod h1:DjEWCu41bVbYcKyvlws9Er60YE4a//bK6mnhWvQeFNI=
cloud.google.com/go/analytics v0.12.0/go.mod h1:gkfj9h6XRf9+TS4bmuhPEShsh3hH8PAZzm/41OOhQd4=
cloud.google.com/go/analytics v0.17.0/go.mod h1:WXFa3WSym4IZ+JiKmavYdJwGG/CvpqiqczmL59bTD9M=
cloud.google.com/go/analytics v0.18.0/go.mod h1:ZkeHGQlcIPkw0R/GW+boWHhCOR43xz9RN/jn7WcqfIE=
cloud.google.com/go/analytics v0.19.0/go.mod h1:k8liqf5/HCnOUkbawNtrWWc+UAzyDlW89doe8TtoDsE=
cloud.google.com/go/apigateway v1.3.0/go.mod h1:89Z8Bhpmxu6AmUxuVRg/ECRGReEdiP3vQtk4Z1J9rJk=
cloud.google.com/go/apigateway v1.4.0/go.mod h1:pHVY9MKGaH9PQ3pJ4YLzoj6U5FUDeDFBllIz7WmzJoc=
cloud.google.com/go/apigateway v1.5.0/go.mod h1:GpnZR3Q4rR7LVu5951qfXPJCHquZt02jf7xQx7kpqN8=
cloud.google.com/go/apigeeconnect v1.3.0/go.mod h1:G/AwXFAKo0gIXkPTVfZDd2qA1TxBXJ3MgMRBQkIi9jc=
cloud.google.com/go/apigeeconnect v1.4.0/go.mod h1:kV4NwOKqjvt2JYR0AoIWo2QGfoRtn/pkS3QlHp0Ni04=
cloud.google.com/go/apigeeconnect v1.5.0/go.mod h1:KFaCqvBRU6idyhSNyn3vlHXc8VMDJdRmwDF6JyFRqZ8=
cloud.google.com/go/apigeeregistry v0.4.0/go.mod h1:EUG4PGcsZvxOXAdyEghIdXwAEi/4MEaoqLMLDMIwKXY=
cloud.google.com/go/apigeeregistry v0.5.0/go.mod h1:YR5+s0BVNZfVOUkMa5pAR2xGd0A473vA5M7j247o1wM=
cloud.google.com/go/apigeeregistry v0.6.0/go.mod h1:BFNzW7yQVLZ3yj0TKcwzb8n25CFBri51GVGOEUcgQsc=
cloud.google.com/go/apikeys v0.4.0/go.mod h1:XATS/yqZbaBK0HOssf+ALHp8jAlNHUgyfprvNcBIszU=
cloud.google.com/go/apikeys v0.5.0/go.mod h1:5aQfwY4D+ewMMWScd3hm2en3hCj+BROlyrt3ytS7KLI=
cloud.google.com/go/apikeys v0.6.0/go.mod h1:kbpXu5upyiAlGkKrJgQl8A0rKNNJ7dQ377pdroRSSi8=
cloud.google.com/go/appengine v1.4.0/go.mod h1:CS2NhuBuDXM9f+qscZ6V86m1MIIqPj3WC/UoEuR1Sno=
cloud.google.com/go/appengine v1.5.0/go.mod h1:TfasSozdkFI0zeoxW3PTBLiNqRmzraodCWatWI9Dmak=
cloud.google.com/go/appengine v1.6.0/go.mod h1:hg6i0J/BD2cKmDJbaFSYHFyZkgBEfQrDg/X0V5fJn84=
cloud.google.com/go/appengine v1.7.0/go.mod h1:eZqpbHFCqRGa2aCdope7eC0SWLV1j0neb/QnMJVWx6A=
cloud.google.com/go/appengine v1.7.1/go.mod h1:IHLToyb/3fKutRysUlFO0BPt5j7RiQ45nrzEJmKTo6E=
cloud.google.com/go/area120 v0.5.0/go.mod h1:DE/n4mp+iqVyvxHN41Vf1CR602GiHQjFPusMFW6bGR4=
cloud.google.com/go/area120 v0.6.0/go.mod h1:39yFJqWVgm0UZqWTOdqkLhjoC7uFfgXRC8g/ZegeAh0=
cloud.google.com/go/area120 v0.7.0/go.mod h1:a3+8EUD1SX5RUcCs3MY5YasiO1z6yLiNLRiFrykbynY=
cloud.google.com/go/area120 v0.7.1/go.mod h1:j84i4E1RboTWjKtZVWXPqvK5VHQFJRF2c1Nm69pWm9k=
cloud.google.com/go/artifactregistry v1.6.0/go.mod h1:IYt0oBPSAGYj/kprzsBjZ/4LnG/zOcHyFHjWPCi6SAQ=
cloud.google.com/go/artifactregistry v1.7.0/go.mod h1:mqTOFOnGZx8EtSqK/ZWcsm/4U8B77rbcLP6ruDU2Ixk=
cloud.google.com/go/artifactregistry v1.8.0/go.mod h1:w3GQXkJX8hiKN0v+at4b0qotwijQbYUqF2GWkZzAhC0=
cloud.google.com/go/artifactregistry v1.9.0/go.mod h1:2K2RqvA2CYvAeARHRkLDhMDJ3OXy26h3XW+3/Jh2uYc=
cloud.google.com/go/artifactregistry v1.11.1/go.mod h1:lLYghw+Itq9SONbCa1YWBoWs1nOucMH0pwXN1rOBZFI=
cloud.google.com/go/artifactregistry v1.11.2/go.mod h1:nLZns771ZGAwVLzTX/7Al6R9ehma4WUEhZGWV6CeQNQ=
cloud.google.com/go/artifactregistry v1.12.0/go.mod h1:o6P3MIvtzTOnmvGagO9v/rOjjA0HmhJ+/6KAXrmYDCI=
cloud.google.com/go/artifactregistry v1.13.0/go.mod h1:uy/LNfoOIivepGhooAUpL1i30Hgee3Cu0l4VTWHUC08=
cloud.google.com/go/asset v1.5.0/go.mod h1:5mfs8UvcM5wHhqtSv8J1CtxxaQq3AdBxxQi2jGW/K4o=
cloud.google.com/go/asset v1.7.0/go.mod h1:YbENsRK4+xTiL+Ofoj5Ckf+O17kJtgp3Y3nn4uzZz5s=
cloud.google.com/go/asset v1.8.0/go.mod h1:mUNGKhiqIdbr8X7KNayoYvyc4HbbFO9URsjbytpUaW0=
cloud.google.com/go/asset v1.9.0/go.mod h1:83MOE6jEJBMqFKadM9NLRcs80Gdw76qGuHn8m3h8oHQ=
cloud.google.com/go/asset v1.10.0/go.mod h1:pLz7uokL80qKhzKr4xXGvBQXnzHn5evJAEAtZiIb0wY=
cloud.google.com/go/asset v1.11.1/go.mod h1:fSwLhbRvC9p9CXQHJ3BgFeQNM4c9x10lqlrdEUYXlJo=
cloud.google.com/go/asset v1.12.0/go.mod h1:h9/sFOa4eDIyKmH6QMpm4eUK3pDojWnUhTgJlk762Hg=
cloud.google.com/go/asset v1.13.0/go.mod h1:WQAMyYek/b7NBpYq/K4KJWcRqzoalEsxz/t/dTk4THw=
cloud.google.com/go/assuredworkloads v1.5.0/go.mod h1:n8HOZ6pff6re5KYfBXcFvSViQjDwxFkAkmUFffJRbbY=
cloud.google.com/go/assuredworkloads v1.6.0/go.mod h1:yo2YOk37Yc89Rsd5QMVECvjaMKymF9OP+QXWlKXUkXw=
cloud.google.com/go/assuredworkloads v1.7.0/go.mod h1:z/736/oNmtGAyU47reJgGN+KVoYoxeLBoj4XkKYscNI=
cloud.google.com/go/assuredworkloads v1.8.0/go.mod h1:AsX2cqyNCOvEQC8RMPnoc0yEarXQk6WEKkxYfL6kGIo=
cloud.google.com/go/assuredworkloads v1.9.0/go.mod h1:kFuI1P78bplYtT77Tb1hi0FMxM0vVpRC7VVoJC3ZoT0=
cloud.google.com/go/assuredworkloads v1.10.0/go.mod h1:kwdUQuXcedVdsIaKgKTp9t0UJkE5+PAVNhdQm4ZVq2E=
cloud.google.com/go/auth v0.16.4 h1:fXOAIQmkApVvcIn7Pc2+5J8QTMVbUGLscnSVNl11su8=
cloud.google.com/go/auth v0.16.4/go.mod h1:j10ncYwjX/g3cdX7GpEzsdM+d+ZNsXAbb6qXA7p1Y5M=
cloud.google.com/go/auth/oauth2adapt v0.2.8 h1:keo8NaayQZ6wimpNSmW5OPc283g65QNIiLpZnkHRbnc=
cloud.google.com/go/auth/oauth2adapt v0.2.8/go.mod h1:XQ9y31RkqZCcwJWNSx2Xvric3RrU88hAYYbjDWYDL+c=
cloud.google.com/go/automl v1.5.0/go.mod h1:34EjfoFGMZ5sgJ9EoLsRtdPSNZLcfflJR39VbVNS2M0=
cloud.google.com/go/automl v1.6.0/go.mod h1:ugf8a6Fx+zP0D59WLhqgTDsQI9w07o64uf/Is3Nh5p8=
cloud.google.com/go/automl v1.7.0/go.mod h1:RL9MYCCsJEOmt0Wf3z9uzG0a7adTT1fe+aObgSpkCt8=
cloud.google.com/go/automl v1.8.0/go.mod h1:xWx7G/aPEe/NP+qzYXktoBSDfjO+vnKMGgsApGJJquM=
cloud.google.com/go/automl v1.12.0/go.mod h1:tWDcHDp86aMIuHmyvjuKeeHEGq76lD7ZqfGLN6B0NuU=
cloud.google.com/go/baremetalsolution v0.3.0/go.mod h1:XOrocE+pvK1xFfleEnShBlNAXf+j5blPPxrhjKgnIFc=
cloud.google.com/go/baremetalsolution v0.4.0/go.mod h1:BymplhAadOO/eBa7KewQ0Ppg4A4Wplbn+PsFKRLo0uI=
cloud.google.com/go/baremetalsolution v0.5.0/go.mod h1:dXGxEkmR9BMwxhzBhV0AioD0ULBmuLZI8CdwalUxuss=
cloud.google.com/go/batch v0.3.0/go.mod h1:TR18ZoAekj1GuirsUsR1ZTKN3FC/4UDnScjT8NXImFE=
cloud.google.com/go/batch v0.4.0/go.mod h1:WZkHnP43R/QCGQsZ+0JyG4i79ranE2u8xvjq/9+STPE=
cloud.google.com/go/batch v0.7.0/go.mod h1:vLZN95s6teRUqRQ4s3RLDsH8PvboqBK+rn1oevL159g=
cloud.google.com/go/beyondcorp v0.2.0/go.mod h1:TB7Bd+EEtcw9PCPQhCJtJGjk/7TC6ckmnSFS+xwTfm4=
cloud.google.com/go/beyondcorp v0.3.0/go.mod h1:E5U5lcrcXMsCuoDNyGrpyTm/hn7ne941Jz2vmksAxW8=
cloud.google.com/go/beyondcorp v0.4.0/go.mod h1:3ApA0mbhHx6YImmuubf5pyW8srKnCEPON32/5hj+RmM=
cloud.google.com/go/beyondcorp v0.5.0/go.mod h1:uFqj9X+dSfrheVp7ssLTaRHd2EHqSL4QZmH4e8WXGGU=
cloud.google.com/go/bigquery v1.0.1/go.mod h1:i/xbL2UlR5RvWAURpBYZTtm/cXjCha9lbfbpx4poX+o=
cloud.google.com/go/bigquery v1.3.0/go.mod h1:PjpwJnslEMmckchkHFfq+HTD2DmtT67aNFKH1/VBDHE=
cloud.google.com/go/bigquery v1.4.0/go.mod h1:S8dzgnTigyfTmLBfrtrhyYhwRxG72rYxvftPBK2Dvzc=
cloud.google.com/go/bigquery v1.5.0/go.mod h1:snEHRnqQbz117VIFhE8bmtwIDY80NLUZUMb4Nv6dBIg=
cloud.google.com/go/bigquery v1.7.0/go.mod h1://okPTzCYNXSlb24MZs83e2Do+h+VXtc4gLoIoXIAPc=
cloud.google.com/go/bigquery v1.8.0/go.mod h1:J5hqkt3O0uAFnINi6JXValWIb1v0goeZM77hZzJN/fQ=
cloud.google.com/go/bigquery v1.42.0/go.mod h1:8dRTJxhtG+vwBKzE5OseQn/hiydoQN3EedCaOdYmxRA=
cloud.google.com/go/bigquery v1.43.0/go.mod h1:ZMQcXHsl+xmU1z36G2jNGZmKp9zNY5BUua5wDgmNCfw=
cloud.google.com/go/bigquery v1.44.0/go.mod h1:0Y33VqXTEsbamHJvJHdFmtqHvMIY28aK1+dFsvaChGc=
cloud.google.com/go/bigquery v1.47.0/go.mod h1:sA9XOgy0A8vQK9+MWhEQTY6Tix87M/ZurWFIxmF9I/E=
cloud.google.com/go/bigquery v1.48.0/go.mod h1:QAwSz+ipNgfL5jxiaK7weyOhzdoAy1zFm0Nf1fysJac=
cloud.google.com/go/bigquery v1.49.0/go.mod h1:Sv8hMmTFFYBlt/ftw2uN6dFdQPzBlREY9yBh7Oy7/4Q=
cloud.google.com/go/bigquery v1.50.0/go.mod h1:YrleYEh2pSEbgTBZYMJ5SuSr0ML3ypjRB1zgf7pvQLU=
cloud.google.com/go/billing v1.4.0/go.mod h1:g9IdKBEFlItS8bTtlrZdVLWSSdSyFUZKXNS02zKMOZY=
cloud.google.com/go/billing v1.5.0/go.mod h1:mztb1tBc3QekhjSgmpf/CV4LzWXLzCArwpLmP2Gm88s=
cloud.google.com/go/billing v1.6.0/go.mod h1:WoXzguj+BeHXPbKfNWkqVtDdzORazmCjraY+vrxcyvI=
cloud.google.com/go/billing v1.7.0/go.mod h1:q457N3Hbj9lYwwRbnlD7vUpyjq6u5U1RAOArInEiD5Y=
cloud.google.com/go/billing v1.12.0/go.mod h1:yKrZio/eu+okO/2McZEbch17O5CB5NpZhhXG6Z766ss=
cloud.google.com/go/billing v1.13.0/go.mod h1:7kB2W9Xf98hP9Sr12KfECgfGclsH3CQR0R08tnRlRbc=
cloud.google.com/go/binaryauthorization v1.1.0/go.mod h1:xwnoWu3Y84jbuHa0zd526MJYmtnVXn0syOjaJgy4+dM=
cloud.google.com/go/binaryauthorization v1.2.0/go.mod h1:86WKkJHtRcv5ViNABtYMhhNWRrD1Vpi//uKEy7aYEfI=
cloud.google.com/go/binaryauthorization v1.3.0/go.mod h1:lRZbKgjDIIQvzYQS1p99A7/U1JqvqeZg0wiI5tp6tg0=
cloud.google.com/go/binaryauthorization v1.4.0/go.mod h1:tsSPQrBd77VLplV70GUhBf/Zm3FsKmgSqgm4UmiDItk=
cloud.google.com/go/binaryauthorization v1.5.0/go.mod h1:OSe4OU1nN/VswXKRBmciKpo9LulY41gch5c68htf3/Q=
cloud.google.com/go/certificatemanager v1.3.0/go.mod h1:n6twGDvcUBFu9uBgt4eYvvf3sQ6My8jADcOVwHmzadg=
cloud.google.com/go/certificatemanager v1.4.0/go.mod h1:vowpercVFyqs8ABSmrdV+GiFf2H/ch3KyudYQEMM590=
cloud.google.com/go/certificatemanager v1.6.0/go.mod h1:3Hh64rCKjRAX8dXgRAyOcY5vQ/fE1sh8o+Mdd6KPgY8=
cloud.google.com/go/channel v1.8.0/go.mod h1:W5SwCXDJsq/rg3tn3oG0LOxpAo6IMxNa09ngphpSlnk=
cloud.google.com/go/channel v1.9.0/go.mod h1:jcu05W0my9Vx4mt3/rEHpfxc9eKi9XwsdDL8yBMbKUk=
cloud.google.com/go/channel v1.11.0/go.mod h1:IdtI0uWGqhEeatSB62VOoJ8FSUhJ9/+iGkJVqp74CGE=
cloud.google.com/go/channel v1.12.0/go.mod h1:VkxCGKASi4Cq7TbXxlaBezonAYpp1GCnKMY6tnMQnLU=
cloud.google.com/go/cloudbuild v1.3.0/go.mod h1:WequR4ULxlqvMsjDEEEFnOG5ZSRSgWOywXYDb1vPE6U=
cloud.google.com/go/cloudbuild v1.4.0/go.mod h1:5Qwa40LHiOXmz3386FrjrYM93rM/hdRr7b53sySrTqA=
cloud.google.com/go/cloudbuild v1.6.0/go.mod h1:UIbc/w9QCbH12xX+ezUsgblrWv+Cv4Tw83GiSMHOn9M=
cloud.google.com/go/cloudbuild v1.7.0/go.mod h1:zb5tWh2XI6lR9zQmsm1VRA+7OCuve5d8S+zJUul8KTg=
cloud.google.com/go/cloudbuild v1.9.0/go.mod h1:qK1d7s4QlO0VwfYn5YuClDGg2hfmLZEb4wQGAbIgL1s=
cloud.google.com/go/clouddms v1.3.0/go.mod h1:oK6XsCDdW4Ib3jCCBugx+gVjevp2TMXFtgxvPSee3OM=
cloud.google.com/go/clouddms v1.4.0/go.mod h1:Eh7sUGCC+aKry14O1NRljhjyrr0NFC0G2cjwX0cByRk=
cloud.google.com/go/clouddms v1.5.0/go.mod h1:QSxQnhikCLUw13iAbffF2CZxAER3xDGNHjsTAkQJcQA=
cloud.google.com/go/cloudtasks v1.5.0/go.mod h1:fD92REy1x5woxkKEkLdvavGnPJGEn8Uic9nWuLzqCpY=
cloud.google.com/go/cloudtasks v1.6.0/go.mod h1:C6Io+sxuke9/KNRkbQpihnW93SWDU3uXt92nu85HkYI=
cloud.google.com/go/cloudtasks v1.7.0/go.mod h1:ImsfdYWwlWNJbdgPIIGJWC+gemEGTBK/SunNQQNCAb4=
cloud.google.com/go/cloudtasks v1.8.0/go.mod h1:gQXUIwCSOI4yPVK7DgTVFiiP0ZW/eQkydWzwVMdHxrI=
cloud.google.com/go/cloudtasks v1.9.0/go.mod h1:w+EyLsVkLWHcOaqNEyvcKAsWp9p29dL6uL9Nst1cI7Y=
cloud.google.com/go/cloudtasks v1.10.0/go.mod h1:NDSoTLkZ3+vExFEWu2UJV1arUyzVDAiZtdWcsUyNwBs=
cloud.google.com/go/compute v0.1.0/go.mod h1:GAesmwr110a34z04OlxYkATPBEfVhkymfTBXtfbBFow=
cloud.google.com/go/compute v1.3.0/go.mod h1:cCZiE1NHEtai4wiufUhW8I8S1JKkAnhnQJWM7YD99wM=
cloud.google.com/go/compute v1.5.0/go.mod h1:9SMHyhJlzhlkJqrPAc839t2BZFTSk6Jdj6mkzQJeu0M=
cloud.google.com/go/compute v1.6.0/go.mod h1:T29tfhtVbq1wvAPo0E3+7vhgmkOYeXjhFvz/FMzPu0s=
cloud.google.com/go/compute v1.6.1/go.mod h1:g85FgpzFvNULZ+S8AYq87axRKuf2Kh7deLqV/jJ3thU=
cloud.google.com/go/compute v1.7.0/go.mod h1:435lt8av5oL9P3fv1OEzSbSUe+ybHXGMPQHHZWZxy9U=
cloud.google.com/go/compute v1.10.0/go.mod h1:ER5CLbMxl90o2jtNbGSbtfOpQKR0t15FOtRsugnLrlU=
cloud.google.com/go/compute v1.12.0/go.mod h1:e8yNOBcBONZU1vJKCvCoDw/4JQsA0dpM4x/6PIIOocU=
cloud.google.com/go/compute v1.12.1/go.mod h1:e8yNOBcBONZU1vJKCvCoDw/4JQsA0dpM4x/6PIIOocU=
cloud.google.com/go/compute v1.13.0/go.mod h1:5aPTS0cUNMIc1CE546K+Th6weJUNQErARyZtRXDJ8GE=
cloud.google.com/go/compute v1.14.0/go.mod h1:YfLtxrj9sU4Yxv+sXzZkyPjEyPBZfXHUvjxega5vAdo=
cloud.google.com/go/compute v1.15.1/go.mod h1:bjjoF/NtFUrkD/urWfdHaKuOPDR5nWIs63rR+SXhcpA=
cloud.google.com/go/compute v1.18.0/go.mod h1:1X7yHxec2Ga+Ss6jPyjxRxpu2uu7PLgsOVXvgU0yacs=
cloud.google.com/go/compute v1.19.0/go.mod h1:rikpw2y+UMidAe9tISo04EHNOIf42RLYF/q8Bs93scU=
cloud.google.com/go/compute v1.19.1/go.mod h1:6ylj3a05WF8leseCdIf77NK0g1ey+nj5IKd5/kvShxE=
cloud.google.com/go/compute/metadata v0.1.0/go.mod h1:Z1VN+bulIf6bt4P/C37K4DyZYZEXYonfTBHHFPO/4UU=
cloud.google.com/go/compute/metadata v0.2.0/go.mod h1:zFmK7XCadkQkj6TtorcaGlCW1hT1fIilQDwofLpJ20k=
cloud.google.com/go/compute/metadata v0.2.1/go.mod h1:jgHgmJd2RKBGzXqF5LR2EZMGxBkeanZ9wwa75XHJgOM=
cloud.google.com/go/compute/metadata v0.2.3/go.mod h1:VAV5nSsACxMJvgaAuX6Pk2AawlZn8kiOGuCv6gTkwuA=
cloud.google.com/go/compute/metadata v0.8.0 h1:HxMRIbao8w17ZX6wBnjhcDkW6lTFpgcaobyVfZWqRLA=
cloud.google.com/go/compute/metadata v0.8.0/go.mod h1:sYOGTp851OV9bOFJ9CH7elVvyzopvWQFNNghtDQ/Biw=
cloud.google.com/go/contactcenterinsights v1.3.0/go.mod h1:Eu2oemoePuEFc/xKFPjbTuPSj0fYJcPls9TFlPNnHHY=
cloud.google.com/go/contactcenterinsights v1.4.0/go.mod h1:L2YzkGbPsv+vMQMCADxJoT9YiTTnSEd6fEvCeHTYVck=
cloud.google.com/go/contactcenterinsights v1.6.0/go.mod h1:IIDlT6CLcDoyv79kDv8iWxMSTZhLxSCofVV5W6YFM/w=
cloud.google.com/go/container v1.6.0/go.mod h1:Xazp7GjJSeUYo688S+6J5V+n/t+G5sKBTFkKNudGRxg=
cloud.google.com/go/container v1.7.0/go.mod h1:Dp5AHtmothHGX3DwwIHPgq45Y8KmNsgN3amoYfxVkLo=
cloud.google.com/go/container v1.13.1/go.mod h1:6wgbMPeQRw9rSnKBCAJXnds3Pzj03C4JHamr8asWKy4=
cloud.google.com/go/container v1.14.0/go.mod h1:3AoJMPhHfLDxLvrlVWaK57IXzaPnLaZq63WX59aQBfM=
cloud.google.com/go/container v1.15.0/go.mod h1:ft+9S0WGjAyjDggg5S06DXj+fHJICWg8L7isCQe9pQA=
cloud.google.com/go/containeranalysis v0.5.1/go.mod h1:1D92jd8gRR/c0fGMlymRgxWD3Qw9C1ff6/T7mLgVL8I=
cloud.google.com/go/containeranalysis v0.6.0/go.mod h1:HEJoiEIu+lEXM+k7+qLCci0h33lX3ZqoYFdmPcoO7s4=
cloud.google.com/go/containeranalysis v0.7.0/go.mod h1:9aUL+/vZ55P2CXfuZjS4UjQ9AgXoSw8Ts6lemfmxBxI=
cloud.google.com/go/containeranalysis v0.9.0/go.mod h1:orbOANbwk5Ejoom+s+DUCTTJ7IBdBQJDcSylAx/on9s=
cloud.google.com/go/datacatalog v1.3.0/go.mod h1:g9svFY6tuR+j+hrTw3J2dNcmI0dzmSiyOzm8kpLq0a0=
cloud.google.com/go/datacatalog v1.5.0/go.mod h1:M7GPLNQeLfWqeIm3iuiruhPzkt65+Bx8dAKvScX8jvs=
cloud.google.com/go/datacatalog v1.6.0/go.mod h1:+aEyF8JKg+uXcIdAmmaMUmZ3q1b/lKLtXCmXdnc0lbc=
cloud.google.com/go/datacatalog v1.7.0/go.mod h1:9mEl4AuDYWw81UGc41HonIHH7/sn52H0/tc8f8ZbZIE=
cloud.google.com/go/datacatalog v1.8.0/go.mod h1:KYuoVOv9BM8EYz/4eMFxrr4DUKhGIOXxZoKYF5wdISM=
cloud.google.com/go/datacatalog v1.8.1/go.mod h1:RJ58z4rMp3gvETA465Vg+ag8BGgBdnRPEMMSTr5Uv+M=
cloud.google.com/go/datacatalog v1.12.0/go.mod h1:CWae8rFkfp6LzLumKOnmVh4+Zle4A3NXLzVJ1d1mRm0=
cloud.google.com/go/datacatalog v1.13.0/go.mod h1:E4Rj9a5ZtAxcQJlEBTLgMTphfP11/lNaAshpoBgemX8=
cloud.google.com/go/dataflow v0.6.0/go.mod h1:9QwV89cGoxjjSR9/r7eFDqqjtvbKxAK2BaYU6PVk9UM=
cloud.google.com/go/dataflow v0.7.0/go.mod h1:PX526vb4ijFMesO1o202EaUmouZKBpjHsTlCtB4parQ=
cloud.google.com/go/dataflow v0.8.0/go.mod h1:Rcf5YgTKPtQyYz8bLYhFoIV/vP39eL7fWNcSOyFfLJE=
cloud.google.com/go/dataform v0.3.0/go.mod h1:cj8uNliRlHpa6L3yVhDOBrUXH+BPAO1+KFMQQNSThKo=
cloud.google.com/go/dataform v0.4.0/go.mod h1:fwV6Y4Ty2yIFL89huYlEkwUPtS7YZinZbzzj5S9FzCE=
cloud.google.com/go/dataform v0.5.0/go.mod h1:GFUYRe8IBa2hcomWplodVmUx/iTL0FrsauObOM3Ipr0=
cloud.google.com/go/dataform v0.6.0/go.mod h1:QPflImQy33e29VuapFdf19oPbE4aYTJxr31OAPV+ulA=
cloud.google.com/go/dataform v0.7.0/go.mod h1:7NulqnVozfHvWUBpMDfKMUESr+85aJsC/2O0o3jWPDE=
cloud.google.com/go/datafusion v1.4.0/go.mod h1:1Zb6VN+W6ALo85cXnM1IKiPw+yQMKMhB9TsTSRDo/38=
cloud.google.com/go/datafusion v1.5.0/go.mod h1:Kz+l1FGHB0J+4XF2fud96WMmRiq/wj8N9u007vyXZ2w=
cloud.google.com/go/datafusion v1.6.0/go.mod h1:WBsMF8F1RhSXvVM8rCV3AeyWVxcC2xY6vith3iw3S+8=
cloud.google.com/go/datalabeling v0.5.0/go.mod h1:TGcJ0G2NzcsXSE/97yWjIZO0bXj0KbVlINXMG9ud42I=
cloud.google.com/go/datalabeling v0.6.0/go.mod h1:WqdISuk/+WIGeMkpw/1q7bK/tFEZxsrFJOJdY2bXvTQ=
cloud.google.com/go/datalabeling v0.7.0/go.mod h1:WPQb1y08RJbmpM3ww0CSUAGweL0SxByuW2E+FU+wXcM=
cloud.google.com/go/dataplex v1.3.0/go.mod h1:hQuRtDg+fCiFgC8j0zV222HvzFQdRd+SVX8gdmFcZzA=
cloud.google.com/go/dataplex v1.4.0/go.mod h1:X51GfLXEMVJ6UN47ESVqvlsRplbLhcsAt0kZCCKsU0A=
cloud.google.com/go/dataplex v1.5.2/go.mod h1:cVMgQHsmfRoI5KFYq4JtIBEUbYwc3c7tXmIDhRmNNVQ=
cloud.google.com/go/dataplex v1.6.0/go.mod h1:bMsomC/aEJOSpHXdFKFGQ1b0TDPIeL28nJObeO1ppRs=
cloud.google.com/go/dataproc v1.7.0/go.mod h1:CKAlMjII9H90RXaMpSxQ8EU6dQx6iAYNPcYPOkSbi8s=
cloud.google.com/go/dataproc v1.8.0/go.mod h1:5OW+zNAH0pMpw14JVrPONsxMQYMBqJuzORhIBfBn9uI=
cloud.google.com/go/dataproc v1.12.0/go.mod h1:zrF3aX0uV3ikkMz6z4uBbIKyhRITnxvr4i3IjKsKrw4=
cloud.google.com/go/dataqna v0.5.0/go.mod h1:90Hyk596ft3zUQ8NkFfvICSIfHFh1Bc7C4cK3vbhkeo=
cloud.google.com/go/dataqna v0.6.0/go.mod h1:1lqNpM7rqNLVgWBJyk5NF6Uen2PHym0jtVJonplVsDA=
cloud.google.com/go/dataqna v0.7.0/go.mod h1:Lx9OcIIeqCrw1a6KdO3/5KMP1wAmTc0slZWwP12Qq3c=
cloud.google.com/go/datastore v1.0.0/go.mod h1:LXYbyblFSglQ5pkeyhO+Qmw7ukd3C+pD7TKLgZqpHYE=
cloud.google.com/go/datastore v1.1.0/go.mod h1:umbIZjpQpHh4hmRpGhH4tLFup+FVzqBi1b3c64qFpCk=
cloud.google.com/go/datastore v1.10.0/go.mod h1:PC5UzAmDEkAmkfaknstTYbNpgE49HAgW2J1gcgUfmdM=
cloud.google.com/go/datastore v1.11.0/go.mod h1:TvGxBIHCS50u8jzG+AW/ppf87v1of8nwzFNgEZU1D3c=
cloud.google.com/go/datastream v1.2.0/go.mod h1:i/uTP8/fZwgATHS/XFu0TcNUhuA0twZxxQ3EyCUQMwo=
cloud.google.com/go/datastream v1.3.0/go.mod h1:cqlOX8xlyYF/uxhiKn6Hbv6WjwPPuI9W2M9SAXwaLLQ=
cloud.google.com/go/datastream v1.4.0/go.mod h1:h9dpzScPhDTs5noEMQVWP8Wx8AFBRyS0s8KWPx/9r0g=
cloud.google.com/go/datastream v1.5.0/go.mod h1:6TZMMNPwjUqZHBKPQ1wwXpb0d5VDVPl2/XoS5yi88q4=
cloud.google.com/go/datastream v1.6.0/go.mod h1:6LQSuswqLa7S4rPAOZFVjHIG3wJIjZcZrw8JDEDJuIs=
cloud.google.com/go/datastream v1.7.0/go.mod h1:uxVRMm2elUSPuh65IbZpzJNMbuzkcvu5CjMqVIUHrww=
cloud.google.com/go/deploy v1.4.0/go.mod h1:5Xghikd4VrmMLNaF6FiRFDlHb59VM59YoDQnOUdsH/c=
cloud.google.com/go/deploy v1.5.0/go.mod h1:ffgdD0B89tToyW/U/D2eL0jN2+IEV/3EMuXHA0l4r+s=
cloud.google.com/go/deploy v1.6.0/go.mod h1:f9PTHehG/DjCom3QH0cntOVRm93uGBDt2vKzAPwpXQI=
cloud.google.com/go/deploy v1.8.0/go.mod h1:z3myEJnA/2wnB4sgjqdMfgxCA0EqC3RBTNcVPs93mtQ=
cloud.google.com/go/dialogflow v1.15.0/go.mod h1:HbHDWs33WOGJgn6rfzBW1Kv807BE3O1+xGbn59zZWI4=
cloud.google.com/go/dialogflow v1.16.1/go.mod h1:po6LlzGfK+smoSmTBnbkIZY2w8ffjz/RcGSS+sh1el0=
cloud.google.com/go/dialogflow v1.17.0/go.mod h1:YNP09C/kXA1aZdBgC/VtXX74G/TKn7XVCcVumTflA+8=
cloud.google.com/go/dialogflow v1.18.0/go.mod h1:trO7Zu5YdyEuR+BhSNOqJezyFQ3aUzz0njv7sMx/iek=
cloud.google.com/go/dialogflow v1.19.0/go.mod h1:JVmlG1TwykZDtxtTXujec4tQ+D8SBFMoosgy+6Gn0s0=
cloud.google.com/go/dialogflow v1.29.0/go.mod h1:b+2bzMe+k1s9V+F2jbJwpHPzrnIyHihAdRFMtn2WXuM=
cloud.google.com/go/dialogflow v1.31.0/go.mod h1:cuoUccuL1Z+HADhyIA7dci3N5zUssgpBJmCzI6fNRB4=
cloud.google.com/go/dialogflow v1.32.0/go.mod h1:jG9TRJl8CKrDhMEcvfcfFkkpp8ZhgPz3sBGmAUYJ2qE=
cloud.google.com/go/dlp v1.6.0/go.mod h1:9eyB2xIhpU0sVwUixfBubDoRwP+GjeUoxxeueZmqvmM=
cloud.google.com/go/dlp v1.7.0/go.mod h1:68ak9vCiMBjbasxeVD17hVPxDEck+ExiHavX8kiHG+Q=
cloud.google.com/go/dlp v1.9.0/go.mod h1:qdgmqgTyReTz5/YNSSuueR8pl7hO0o9bQ39ZhtgkWp4=
cloud.google.com/go/documentai v1.7.0/go.mod h1:lJvftZB5NRiFSX4moiye1SMxHx0Bc3x1+p9e/RfXYiU=
cloud.google.com/go/documentai v1.8.0/go.mod h1:xGHNEB7CtsnySCNrCFdCyyMz44RhFEEX2Q7UD0c5IhU=
cloud.google.com/go/documentai v1.9.0/go.mod h1:FS5485S8R00U10GhgBC0aNGrJxBP8ZVpEeJ7PQDZd6k=
cloud.google.com/go/documentai v1.10.0/go.mod h1:vod47hKQIPeCfN2QS/jULIvQTugbmdc0ZvxxfQY1bg4=
cloud.google.com/go/documentai v1.16.0/go.mod h1:o0o0DLTEZ+YnJZ+J4wNfTxmDVyrkzFvttBXXtYRMHkM=
cloud.google.com/go/documentai v1.18.0/go.mod h1:F6CK6iUH8J81FehpskRmhLq/3VlwQvb7TvwOceQ2tbs=
cloud.google.com/go/domains v0.6.0/go.mod h1:T9Rz3GasrpYk6mEGHh4rymIhjlnIuB4ofT1wTxDeT4Y=
cloud.google.com/go/domains v0.7.0/go.mod h1:PtZeqS1xjnXuRPKE/88Iru/LdfoRyEHYA9nFQf4UKpg=
cloud.google.com/go/domains v0.8.0/go.mod h1:M9i3MMDzGFXsydri9/vW+EWz9sWb4I6WyHqdlAk0idE=
cloud.google.com/go/edgecontainer v0.1.0/go.mod h1:WgkZ9tp10bFxqO8BLPqv2LlfmQF1X8lZqwW4r1BTajk=
cloud.google.com/go/edgecontainer v0.2.0/go.mod h1:RTmLijy+lGpQ7BXuTDa4C4ssxyXT34NIuHIgKuP4s5w=
cloud.google.com/go/edgecontainer v0.3.0/go.mod h1:FLDpP4nykgwwIfcLt6zInhprzw0lEi2P1fjO6Ie0qbc=
cloud.google.com/go/edgecontainer v1.0.0/go.mod h1:cttArqZpBB2q58W/upSG++ooo6EsblxDIolxa3jSjbY=
cloud.google.com/go/errorreporting v0.3.0/go.mod h1:xsP2yaAp+OAW4OIm60An2bbLpqIhKXdWR/tawvl7QzU=
cloud.google.com/go/essentialcontacts v1.3.0/go.mod h1:r+OnHa5jfj90qIfZDO/VztSFqbQan7HV75p8sA+mdGI=
cloud.google.com/go/essentialcontacts v1.4.0/go.mod h1:8tRldvHYsmnBCHdFpvU+GL75oWiBKl80BiqlFh9tp+8=
cloud.google.com/go/essentialcontacts v1.5.0/go.mod h1:ay29Z4zODTuwliK7SnX8E86aUF2CTzdNtvv42niCX0M=
cloud.google.com/go/eventarc v1.7.0/go.mod h1:6ctpF3zTnaQCxUjHUdcfgcA1A2T309+omHZth7gDfmc=
cloud.google.com/go/eventarc v1.8.0/go.mod h1:imbzxkyAU4ubfsaKYdQg04WS1NvncblHEup4kvF+4gw=
cloud.google.com/go/eventarc v1.10.0/go.mod h1:u3R35tmZ9HvswGRBnF48IlYgYeBcPUCjkr4BTdem2Kw=
cloud.google.com/go/eventarc v1.11.0/go.mod h1:PyUjsUKPWoRBCHeOxZd/lbOOjahV41icXyUY5kSTvVY=
cloud.google.com/go/filestore v1.3.0/go.mod h1:+qbvHGvXU1HaKX2nD0WEPo92TP/8AQuCVEBXNY9z0+w=
cloud.google.com/go/filestore v1.4.0/go.mod h1:PaG5oDfo9r224f8OYXURtAsY+Fbyq/bLYoINEK8XQAI=
cloud.google.com/go/filestore v1.5.0/go.mod h1:FqBXDWBp4YLHqRnVGveOkHDf8svj9r5+mUDLupOWEDs=
cloud.google.com/go/filestore v1.6.0/go.mod h1:di5unNuss/qfZTw2U9nhFqo8/ZDSc466dre85Kydllg=
cloud.google.com/go/firestore v1.9.0/go.mod h1:HMkjKHNTtRyZNiMzu7YAsLr9K3X2udY2AMwDaMEQiiE=
cloud.google.com/go/functions v1.6.0/go.mod h1:3H1UA3qiIPRWD7PeZKLvHZ9SaQhR26XIJcC0A5GbvAk=
cloud.google.com/go/functions v1.7.0/go.mod h1:+d+QBcWM+RsrgZfV9xo6KfA1GlzJfxcfZcRPEhDDfzg=
cloud.google.com/go/functions v1.8.0/go.mod h1:RTZ4/HsQjIqIYP9a9YPbU+QFoQsAlYgrwOXJWHn1POY=
cloud.google.com/go/functions v1.9.0/go.mod h1:Y+Dz8yGguzO3PpIjhLTbnqV1CWmgQ5UwtlpzoyquQ08=
cloud.google.com/go/functions v1.10.0/go.mod h1:0D3hEOe3DbEvCXtYOZHQZmD+SzYsi1YbI7dGvHfldXw=
cloud.google.com/go/functions v1.12.0/go.mod h1:AXWGrF3e2C/5ehvwYo/GH6O5s09tOPksiKhz+hH8WkA=
cloud.google.com/go/functions v1.13.0/go.mod h1:EU4O007sQm6Ef/PwRsI8N2umygGqPBS/IZQKBQBcJ3c=
cloud.google.com/go/gaming v1.5.0/go.mod h1:ol7rGcxP/qHTRQE/RO4bxkXq+Fix0j6D4LFPzYTIrDM=
cloud.google.com/go/gaming v1.6.0/go.mod h1:YMU1GEvA39Qt3zWGyAVA9bpYz/yAhTvaQ1t2sK4KPUA=
cloud.google.com/go/gaming v1.7.0/go.mod h1:LrB8U7MHdGgFG851iHAfqUdLcKBdQ55hzXy9xBJz0+w=
cloud.google.com/go/gaming v1.8.0/go.mod h1:xAqjS8b7jAVW0KFYeRUxngo9My3f33kFmua++Pi+ggM=
cloud.google.com/go/gaming v1.9.0/go.mod h1:Fc7kEmCObylSWLO334NcO+O9QMDyz+TKC4v1D7X+Bc0=
cloud.google.com/go/gkebackup v0.2.0/go.mod h1:XKvv/4LfG829/B8B7xRkk8zRrOEbKtEam6yNfuQNH60=
cloud.google.com/go/gkebackup v0.3.0/go.mod h1:n/E671i1aOQvUxT541aTkCwExO/bTer2HDlj4TsBRAo=
cloud.google.com/go/gkebackup v0.4.0/go.mod h1:byAyBGUwYGEEww7xsbnUTBHIYcOPy/PgUWUtOeRm9Vg=
cloud.google.com/go/gkeconnect v0.5.0/go.mod h1:c5lsNAg5EwAy7fkqX/+goqFsU1Da/jQFqArp+wGNr/o=
cloud.google.com/go/gkeconnect v0.6.0/go.mod h1:Mln67KyU/sHJEBY8kFZ0xTeyPtzbq9StAVvEULYK16A=
cloud.google.com/go/gkeconnect v0.7.0/go.mod h1:SNfmVqPkaEi3bF/B3CNZOAYPYdg7sU+obZ+QTky2Myw=
cloud.google.com/go/gkehub v0.9.0/go.mod h1:WYHN6WG8w9bXU0hqNxt8rm5uxnk8IH+lPY9J2TV7BK0=
cloud.google.com/go/gkehub v0.10.0/go.mod h1:UIPwxI0DsrpsVoWpLB0stwKCP+WFVG9+y977wO+hBH0=
cloud.google.com/go/gkehub v0.11.0/go.mod h1:JOWHlmN+GHyIbuWQPl47/C2RFhnFKH38jH9Ascu3n0E=
cloud.google.com/go/gkehub v0.12.0/go.mod h1:djiIwwzTTBrF5NaXCGv3mf7klpEMcST17VBTVVDcuaw=
cloud.google.com/go/gkemulticloud v0.3.0/go.mod h1:7orzy7O0S+5kq95e4Hpn7RysVA7dPs8W/GgfUtsPbrA=
cloud.google.com/go/gkemulticloud v0.4.0/go.mod h1:E9gxVBnseLWCk24ch+P9+B2CoDFJZTyIgLKSalC7tuI=
cloud.google.com/go/gkemulticloud v0.5.0/go.mod h1:W0JDkiyi3Tqh0TJr//y19wyb1yf8llHVto2Htf2Ja3Y=
cloud.google.com/go/grafeas v0.2.0/go.mod h1:KhxgtF2hb0P191HlY5besjYm6MqTSTj3LSI+M+ByZHc=
cloud.google.com/go/gsuiteaddons v1.3.0/go.mod h1:EUNK/J1lZEZO8yPtykKxLXI6JSVN2rg9bN8SXOa0bgM=
cloud.google.com/go/gsuiteaddons v1.4.0/go.mod h1:rZK5I8hht7u7HxFQcFei0+AtfS9uSushomRlg+3ua1o=
cloud.google.com/go/gsuiteaddons v1.5.0/go.mod h1:TFCClYLd64Eaa12sFVmUyG62tk4mdIsI7pAnSXRkcFo=
cloud.google.com/go/iam v0.1.0/go.mod h1:vcUNEa0pEm0qRVpmWepWaFMIAI8/hjB9mO8rNCJtF6c=
cloud.google.com/go/iam v0.3.0/go.mod h1:XzJPvDayI+9zsASAFO68Hk07u3z+f+JrT2xXNdp4bnY=
cloud.google.com/go/iam v0.5.0/go.mod h1:wPU9Vt0P4UmCux7mqtRu6jcpPAb74cP1fh50J3QpkUc=
cloud.google.com/go/iam v0.6.0/go.mod h1:+1AH33ueBne5MzYccyMHtEKqLE4/kJOibtffMHDMFMc=
cloud.google.com/go/iam v0.7.0/go.mod h1:H5Br8wRaDGNc8XP3keLc4unfUUZeyH3Sfl9XpQEYOeg=
cloud.google.com/go/iam v0.8.0/go.mod h1:lga0/y3iH6CX7sYqypWJ33hf7kkfXJag67naqGESjkE=
cloud.google.com/go/iam v0.11.0/go.mod h1:9PiLDanza5D+oWFZiH1uG+RnRCfEGKoyl6yo4cgWZGY=
cloud.google.com/go/iam v0.12.0/go.mod h1:knyHGviacl11zrtZUoDuYpDgLjvr28sLQaG0YB2GYAY=
cloud.google.com/go/iam v0.13.0/go.mod h1:ljOg+rcNfzZ5d6f1nAUJ8ZIxOaZUVoS14bKCtaLZ/D0=
cloud.google.com/go/iam v1.5.2 h1:qgFRAGEmd8z6dJ/qyEchAuL9jpswyODjA2lS+w234g8=
cloud.google.com/go/iam v1.5.2/go.mod h1:SE1vg0N81zQqLzQEwxL2WI6yhetBdbNQuTvIKCSkUHE=
cloud.google.com/go/iap v1.4.0/go.mod h1:RGFwRJdihTINIe4wZ2iCP0zF/qu18ZwyKxrhMhygBEc=
cloud.google.com/go/iap v1.5.0/go.mod h1:UH/CGgKd4KyohZL5Pt0jSKE4m3FR51qg6FKQ/z/Ix9A=
cloud.google.com/go/iap v1.6.0/go.mod h1:NSuvI9C/j7UdjGjIde7t7HBz+QTwBcapPE07+sSRcLk=
cloud.google.com/go/iap v1.7.0/go.mod h1:beqQx56T9O1G1yNPph+spKpNibDlYIiIixiqsQXxLIo=
cloud.google.com/go/iap v1.7.1/go.mod h1:WapEwPc7ZxGt2jFGB/C/bm+hP0Y6NXzOYGjpPnmMS74=
cloud.google.com/go/ids v1.1.0/go.mod h1:WIuwCaYVOzHIj2OhN9HAwvW+DBdmUAdcWlFxRl+KubM=
cloud.google.com/go/ids v1.2.0/go.mod h1:5WXvp4n25S0rA/mQWAg1YEEBBq6/s+7ml1RDCW1IrcY=
cloud.google.com/go/ids v1.3.0/go.mod h1:JBdTYwANikFKaDP6LtW5JAi4gubs57SVNQjemdt6xV4=
cloud.google.com/go/iot v1.3.0/go.mod h1:r7RGh2B61+B8oz0AGE+J72AhA0G7tdXItODWsaA2oLs=
cloud.google.com/go/iot v1.4.0/go.mod h1:dIDxPOn0UvNDUMD8Ger7FIaTuvMkj+aGk94RPP0iV+g=
cloud.google.com/go/iot v1.5.0/go.mod h1:mpz5259PDl3XJthEmh9+ap0affn/MqNSP4My77Qql9o=
cloud.google.com/go/iot v1.6.0/go.mod h1:IqdAsmE2cTYYNO1Fvjfzo9po179rAtJeVGUvkLN3rLE=
cloud.google.com/go/kms v1.4.0/go.mod h1:fajBHndQ+6ubNw6Ss2sSd+SWvjL26RNo/dr7uxsnnOA=
cloud.google.com/go/kms v1.5.0/go.mod h1:QJS2YY0eJGBg3mnDfuaCyLauWwBJiHRboYxJ++1xJNg=
cloud.google.com/go/kms v1.6.0/go.mod h1:Jjy850yySiasBUDi6KFUwUv2n1+o7QZFyuUJg6OgjA0=
cloud.google.com/go/kms v1.8.0/go.mod h1:4xFEhYFqvW+4VMELtZyxomGSYtSQKzM178ylFW4jMAg=
cloud.google.com/go/kms v1.9.0/go.mod h1:qb1tPTgfF9RQP8e1wq4cLFErVuTJv7UsSC915J8dh3w=
cloud.google.com/go/kms v1.10.0/go.mod h1:ng3KTUtQQU9bPX3+QGLsflZIHlkbn8amFAMY63m8d24=
cloud.google.com/go/kms v1.10.1/go.mod h1:rIWk/TryCkR59GMC3YtHtXeLzd634lBbKenvyySAyYI=
cloud.google.com/go/language v1.4.0/go.mod h1:F9dRpNFQmJbkaop6g0JhSBXCNlO90e1KWx5iDdxbWic=
cloud.google.com/go/language v1.6.0/go.mod h1:6dJ8t3B+lUYfStgls25GusK04NLh3eDLQnWM3mdEbhI=
cloud.google.com/go/language v1.7.0/go.mod h1:DJ6dYN/W+SQOjF8e1hLQXMF21AkH2w9wiPzPCJa2MIE=
cloud.google.com/go/language v1.8.0/go.mod h1:qYPVHf7SPoNNiCL2Dr0FfEFNil1qi3pQEyygwpgVKB8=
cloud.google.com/go/language v1.9.0/go.mod h1:Ns15WooPM5Ad/5no/0n81yUetis74g3zrbeJBE+ptUY=
cloud.google.com/go/lifesciences v0.5.0/go.mod h1:3oIKy8ycWGPUyZDR/8RNnTOYevhaMLqh5vLUXs9zvT8=
cloud.google.com/go/lifesciences v0.6.0/go.mod h1:ddj6tSX/7BOnhxCSd3ZcETvtNr8NZ6t/iPhY2Tyfu08=
cloud.google.com/go/lifesciences v0.8.0/go.mod h1:lFxiEOMqII6XggGbOnKiyZ7IBwoIqA84ClvoezaA/bo=
cloud.google.com/go/logging v1.6.1/go.mod h1:5ZO0mHHbvm8gEmeEUHrmDlTDSu5imF6MUP9OfilNXBw=
cloud.google.com/go/logging v1.7.0/go.mod h1:3xjP2CjkM3ZkO73aj4ASA5wRPGGCRrPIAeNqVNkzY8M=
cloud.google.com/go/logging v1.13.0 h1:7j0HgAp0B94o1YRDqiqm26w4q1rDMH7XNRU34lJXHYc=
cloud.google.com/go/logging v1.13.0/go.mod h1:36CoKh6KA/M0PbhPKMq6/qety2DCAErbhXT62TuXALA=
cloud.google.com/go/longrunning v0.1.1/go.mod h1:UUFxuDWkv22EuY93jjmDMFT5GPQKeFVJBIF6QlTqdsE=
cloud.google.com/go/longrunning v0.3.0/go.mod h1:qth9Y41RRSUE69rDcOn6DdK3HfQfsUI0YSmW3iIlLJc=
cloud.google.com/go/longrunning v0.4.1/go.mod h1:4iWDqhBZ70CvZ6BfETbvam3T8FMvLK+eFj0E6AaRQTo=
cloud.google.com/go/longrunning v0.6.7 h1:IGtfDWHhQCgCjwQjV9iiLnUta9LBCo8R9QmAFsS/PrE=
cloud.google.com/go/longrunning v0.6.7/go.mod h1:EAFV3IZAKmM56TyiE6VAP3VoTzhZzySwI/YI1s/nRsY=
cloud.google.com/go/managedidentities v1.3.0/go.mod h1:UzlW3cBOiPrzucO5qWkNkh0w33KFtBJU281hacNvsdE=
cloud.google.com/go/managedidentities v1.4.0/go.mod h1:NWSBYbEMgqmbZsLIyKvxrYbtqOsxY1ZrGM+9RgDqInM=
cloud.google.com/go/managedidentities v1.5.0/go.mod h1:+dWcZ0JlUmpuxpIDfyP5pP5y0bLdRwOS4Lp7gMni/LA=
cloud.google.com/go/maps v0.1.0/go.mod h1:BQM97WGyfw9FWEmQMpZ5T6cpovXXSd1cGmFma94eubI=
cloud.google.com/go/maps v0.6.0/go.mod h1:o6DAMMfb+aINHz/p/jbcY+mYeXBoZoxTfdSQ8VAJaCw=
cloud.google.com/go/maps v0.7.0/go.mod h1:3GnvVl3cqeSvgMcpRlQidXsPYuDGQ8naBis7MVzpXsY=
cloud.google.com/go/mediatranslation v0.5.0/go.mod h1:jGPUhGTybqsPQn91pNXw0xVHfuJ3leR1wj37oU3y1f4=
cloud.google.com/go/mediatranslation v0.6.0/go.mod h1:hHdBCTYNigsBxshbznuIMFNe5QXEowAuNmmC7h8pu5w=
cloud.google.com/go/mediatranslation v0.7.0/go.mod h1:LCnB/gZr90ONOIQLgSXagp8XUW1ODs2UmUMvcgMfI2I=
cloud.google.com/go/memcache v1.4.0/go.mod h1:rTOfiGZtJX1AaFUrOgsMHX5kAzaTQ8azHiuDoTPzNsE=
cloud.google.com/go/memcache v1.5.0/go.mod h1:dk3fCK7dVo0cUU2c36jKb4VqKPS22BTkf81Xq617aWM=
cloud.google.com/go/memcache v1.6.0/go.mod h1:XS5xB0eQZdHtTuTF9Hf8eJkKtR3pVRCcvJwtm68T3rA=
cloud.google.com/go/memcache v1.7.0/go.mod h1:ywMKfjWhNtkQTxrWxCkCFkoPjLHPW6A7WOTVI8xy3LY=
cloud.google.com/go/memcache v1.9.0/go.mod h1:8oEyzXCu+zo9RzlEaEjHl4KkgjlNDaXbCQeQWlzNFJM=
cloud.google.com/go/metastore v1.5.0/go.mod h1:2ZNrDcQwghfdtCwJ33nM0+GrBGlVuh8rakL3vdPY3XY=
cloud.google.com/go/metastore v1.6.0/go.mod h1:6cyQTls8CWXzk45G55x57DVQ9gWg7RiH65+YgPsNh9s=
cloud.google.com/go/metastore v1.7.0/go.mod h1:s45D0B4IlsINu87/AsWiEVYbLaIMeUSoxlKKDqBGFS8=
cloud.google.com/go/metastore v1.8.0/go.mod h1:zHiMc4ZUpBiM7twCIFQmJ9JMEkDSyZS9U12uf7wHqSI=
cloud.google.com/go/metastore v1.10.0/go.mod h1:fPEnH3g4JJAk+gMRnrAnoqyv2lpUCqJPWOodSaf45Eo=
cloud.google.com/go/monitoring v1.7.0/go.mod h1:HpYse6kkGo//7p6sT0wsIC6IBDET0RhIsnmlA53dvEk=
cloud.google.com/go/monitoring v1.8.0/go.mod h1:E7PtoMJ1kQXWxPjB6mv2fhC5/15jInuulFdYYtlcvT4=
cloud.google.com/go/monitoring v1.12.0/go.mod h1:yx8Jj2fZNEkL/GYZyTLS4ZtZEZN8WtDEiEqG4kLK50w=
cloud.google.com/go/monitoring v1.13.0/go.mod h1:k2yMBAB1H9JT/QETjNkgdCGD9bPF712XiLTVr+cBrpw=
cloud.google.com/go/monitoring v1.24.2 h1:5OTsoJ1dXYIiMiuL+sYscLc9BumrL3CarVLL7dd7lHM=
cloud.google.com/go/monitoring v1.24.2/go.mod h1:x7yzPWcgDRnPEv3sI+jJGBkwl5qINf+6qY4eq0I9B4U=
cloud.google.com/go/networkconnectivity v1.4.0/go.mod h1:nOl7YL8odKyAOtzNX73/M5/mGZgqqMeryi6UPZTk/rA=
cloud.google.com/go/networkconnectivity v1.5.0/go.mod h1:3GzqJx7uhtlM3kln0+x5wyFvuVH1pIBJjhCpjzSt75o=
cloud.google.com/go/networkconnectivity v1.6.0/go.mod h1:OJOoEXW+0LAxHh89nXd64uGG+FbQoeH8DtxCHVOMlaM=
cloud.google.com/go/networkconnectivity v1.7.0/go.mod h1:RMuSbkdbPwNMQjB5HBWD5MpTBnNm39iAVpC3TmsExt8=
cloud.google.com/go/networkconnectivity v1.10.0/go.mod h1:UP4O4sWXJG13AqrTdQCD9TnLGEbtNRqjuaaA7bNjF5E=
cloud.google.com/go/networkconnectivity v1.11.0/go.mod h1:iWmDD4QF16VCDLXUqvyspJjIEtBR/4zq5hwnY2X3scM=
cloud.google.com/go/networkmanagement v1.4.0/go.mod h1:Q9mdLLRn60AsOrPc8rs8iNV6OHXaGcDdsIQe1ohekq8=
cloud.google.com/go/networkmanagement v1.5.0/go.mod h1:ZnOeZ/evzUdUsnvRt792H0uYEnHQEMaz+REhhzJRcf4=
cloud.google.com/go/networkmanagement v1.6.0/go.mod h1:5pKPqyXjB/sgtvB5xqOemumoQNB7y95Q7S+4rjSOPYY=
cloud.google.com/go/networksecurity v0.5.0/go.mod h1:xS6fOCoqpVC5zx15Z/MqkfDwH4+m/61A3ODiDV1xmiQ=
cloud.google.com/go/networksecurity v0.6.0/go.mod h1:Q5fjhTr9WMI5mbpRYEbiexTzROf7ZbDzvzCrNl14nyU=
cloud.google.com/go/networksecurity v0.7.0/go.mod h1:mAnzoxx/8TBSyXEeESMy9OOYwo1v+gZ5eMRnsT5bC8k=
cloud.google.com/go/networksecurity v0.8.0/go.mod h1:B78DkqsxFG5zRSVuwYFRZ9Xz8IcQ5iECsNrPn74hKHU=
cloud.google.com/go/notebooks v1.2.0/go.mod h1:9+wtppMfVPUeJ8fIWPOq1UnATHISkGXGqTkxeieQ6UY=
cloud.google.com/go/notebooks v1.3.0/go.mod h1:bFR5lj07DtCPC7YAAJ//vHskFBxA5JzYlH68kXVdk34=
cloud.google.com/go/notebooks v1.4.0/go.mod h1:4QPMngcwmgb6uw7Po99B2xv5ufVoIQ7nOGDyL4P8AgA=
cloud.google.com/go/notebooks v1.5.0/go.mod h1:q8mwhnP9aR8Hpfnrc5iN5IBhrXUy8S2vuYs+kBJ/gu0=
cloud.google.com/go/notebooks v1.7.0/go.mod h1:PVlaDGfJgj1fl1S3dUwhFMXFgfYGhYQt2164xOMONmE=
cloud.google.com/go/notebooks v1.8.0/go.mod h1:Lq6dYKOYOWUCTvw5t2q1gp1lAp0zxAxRycayS0iJcqQ=
cloud.google.com/go/optimization v1.1.0/go.mod h1:5po+wfvX5AQlPznyVEZjGJTMr4+CAkJf2XSTQOOl9l4=
cloud.google.com/go/optimization v1.2.0/go.mod h1:Lr7SOHdRDENsh+WXVmQhQTrzdu9ybg0NecjHidBq6xs=
cloud.google.com/go/optimization v1.3.1/go.mod h1:IvUSefKiwd1a5p0RgHDbWCIbDFgKuEdB+fPPuP0IDLI=
cloud.google.com/go/orchestration v1.3.0/go.mod h1:Sj5tq/JpWiB//X/q3Ngwdl5K7B7Y0KZ7bfv0wL6fqVA=
cloud.google.com/go/orchestration v1.4.0/go.mod h1:6W5NLFWs2TlniBphAViZEVhrXRSMgUGDfW7vrWKvsBk=
cloud.google.com/go/orchestration v1.6.0/go.mod h1:M62Bevp7pkxStDfFfTuCOaXgaaqRAga1yKyoMtEoWPQ=
cloud.google.com/go/orgpolicy v1.4.0/go.mod h1:xrSLIV4RePWmP9P3tBl8S93lTmlAxjm06NSm2UTmKvE=
cloud.google.com/go/orgpolicy v1.5.0/go.mod h1:hZEc5q3wzwXJaKrsx5+Ewg0u1LxJ51nNFlext7Tanwc=
cloud.google.com/go/orgpolicy v1.10.0/go.mod h1:w1fo8b7rRqlXlIJbVhOMPrwVljyuW5mqssvBtU18ONc=
cloud.google.com/go/osconfig v1.7.0/go.mod h1:oVHeCeZELfJP7XLxcBGTMBvRO+1nQ5tFG9VQTmYS2Fs=
cloud.google.com/go/osconfig v1.8.0/go.mod h1:EQqZLu5w5XA7eKizepumcvWx+m8mJUhEwiPqWiZeEdg=
cloud.google.com/go/osconfig v1.9.0/go.mod h1:Yx+IeIZJ3bdWmzbQU4fxNl8xsZ4amB+dygAwFPlvnNo=
cloud.google.com/go/osconfig v1.10.0/go.mod h1:uMhCzqC5I8zfD9zDEAfvgVhDS8oIjySWh+l4WK6GnWw=
cloud.google.com/go/osconfig v1.11.0/go.mod h1:aDICxrur2ogRd9zY5ytBLV89KEgT2MKB2L/n6x1ooPw=
cloud.google.com/go/oslogin v1.4.0/go.mod h1:YdgMXWRaElXz/lDk1Na6Fh5orF7gvmJ0FGLIs9LId4E=
cloud.google.com/go/oslogin v1.5.0/go.mod h1:D260Qj11W2qx/HVF29zBg+0fd6YCSjSqLUkY/qEenQU=
cloud.google.com/go/oslogin v1.6.0/go.mod h1:zOJ1O3+dTU8WPlGEkFSh7qeHPPSoxrcMbbK1Nm2iX70=
cloud.google.com/go/oslogin v1.7.0/go.mod h1:e04SN0xO1UNJ1M5GP0vzVBFicIe4O53FOfcixIqTyXo=
cloud.google.com/go/oslogin v1.9.0/go.mod h1:HNavntnH8nzrn8JCTT5fj18FuJLFJc4NaZJtBnQtKFs=
cloud.google.com/go/phishingprotection v0.5.0/go.mod h1:Y3HZknsK9bc9dMi+oE8Bim0lczMU6hrX0UpADuMefr0=
cloud.google.com/go/phishingprotection v0.6.0/go.mod h1:9Y3LBLgy0kDTcYET8ZH3bq/7qni15yVUoAxiFxnlSUA=
cloud.google.com/go/phishingprotection v0.7.0/go.mod h1:8qJI4QKHoda/sb/7/YmMQ2omRLSLYSu9bU0EKCNI+Lk=
cloud.google.com/go/policytroubleshooter v1.3.0/go.mod h1:qy0+VwANja+kKrjlQuOzmlvscn4RNsAc0e15GGqfMxg=
cloud.google.com/go/policytroubleshooter v1.4.0/go.mod h1:DZT4BcRw3QoO8ota9xw/LKtPa8lKeCByYeKTIf/vxdE=
cloud.google.com/go/policytroubleshooter v1.5.0/go.mod h1:Rz1WfV+1oIpPdN2VvvuboLVRsB1Hclg3CKQ53j9l8vw=
cloud.google.com/go/policytroubleshooter v1.6.0/go.mod h1:zYqaPTsmfvpjm5ULxAyD/lINQxJ0DDsnWOP/GZ7xzBc=
cloud.google.com/go/privatecatalog v0.5.0/go.mod h1:XgosMUvvPyxDjAVNDYxJ7wBW8//hLDDYmnsNcMGq1K0=
cloud.google.com/go/privatecatalog v0.6.0/go.mod h1:i/fbkZR0hLN29eEWiiwue8Pb+GforiEIBnV9yrRUOKI=
cloud.google.com/go/privatecatalog v0.7.0/go.mod h1:2s5ssIFO69F5csTXcwBP7NPFTZvps26xGzvQ2PQaBYg=
cloud.google.com/go/privatecatalog v0.8.0/go.mod h1:nQ6pfaegeDAq/Q5lrfCQzQLhubPiZhSaNhIgfJlnIXs=
cloud.google.com/go/pubsub v1.0.1/go.mod h1:R0Gpsv3s54REJCy4fxDixWD93lHJMoZTyQ2kNxGRt3I=
cloud.google.com/go/pubsub v1.1.0/go.mod h1:EwwdRX2sKPjnvnqCa270oGRyludottCI76h+R3AArQw=
cloud.google.com/go/pubsub v1.2.0/go.mod h1:jhfEVHT8odbXTkndysNHCcx0awwzvfOlguIAii9o8iA=
cloud.google.com/go/pubsub v1.3.1/go.mod h1:i+ucay31+CNRpDW4Lu78I4xXG+O1r/MAHgjpRVR+TSU=
cloud.google.com/go/pubsub v1.26.0/go.mod h1:QgBH3U/jdJy/ftjPhTkyXNj543Tin1pRYcdcPRnFIRI=
cloud.google.com/go/pubsub v1.27.1/go.mod h1:hQN39ymbV9geqBnfQq6Xf63yNhUAhv9CZhzp5O6qsW0=
cloud.google.com/go/pubsub v1.28.0/go.mod h1:vuXFpwaVoIPQMGXqRyUQigu/AX1S3IWugR9xznmcXX8=
cloud.google.com/go/pubsub v1.30.0/go.mod h1:qWi1OPS0B+b5L+Sg6Gmc9zD1Y+HaM0MdUr7LsupY1P4=
cloud.google.com/go/pubsublite v1.5.0/go.mod h1:xapqNQ1CuLfGi23Yda/9l4bBCKz/wC3KIJ5gKcxveZg=
cloud.google.com/go/pubsublite v1.6.0/go.mod h1:1eFCS0U11xlOuMFV/0iBqw3zP12kddMeCbj/F3FSj9k=
cloud.google.com/go/pubsublite v1.7.0/go.mod h1:8hVMwRXfDfvGm3fahVbtDbiLePT3gpoiJYJY+vxWxVM=
cloud.google.com/go/recaptchaenterprise v1.3.1/go.mod h1:OdD+q+y4XGeAlxRaMn1Y7/GveP6zmq76byL6tjPE7d4=
cloud.google.com/go/recaptchaenterprise/v2 v2.1.0/go.mod h1:w9yVqajwroDNTfGuhmOjPDN//rZGySaf6PtFVcSCa7o=
cloud.google.com/go/recaptchaenterprise/v2 v2.2.0/go.mod h1:/Zu5jisWGeERrd5HnlS3EUGb/D335f9k51B/FVil0jk=
cloud.google.com/go/recaptchaenterprise/v2 v2.3.0/go.mod h1:O9LwGCjrhGHBQET5CA7dd5NwwNQUErSgEDit1DLNTdo=
cloud.google.com/go/recaptchaenterprise/v2 v2.4.0/go.mod h1:Am3LHfOuBstrLrNCBrlI5sbwx9LBg3te2N6hGvHn2mE=
cloud.google.com/go/recaptchaenterprise/v2 v2.5.0/go.mod h1:O8LzcHXN3rz0j+LBC91jrwI3R+1ZSZEWrfL7XHgNo9U=
cloud.google.com/go/recaptchaenterprise/v2 v2.6.0/go.mod h1:RPauz9jeLtB3JVzg6nCbe12qNoaa8pXc4d/YukAmcnA=
cloud.google.com/go/recaptchaenterprise/v2 v2.7.0/go.mod h1:19wVj/fs5RtYtynAPJdDTb69oW0vNHYDBTbB4NvMD9c=
cloud.google.com/go/recommendationengine v0.5.0/go.mod h1:E5756pJcVFeVgaQv3WNpImkFP8a+RptV6dDLGPILjvg=
cloud.google.com/go/recommendationengine v0.6.0/go.mod h1:08mq2umu9oIqc7tDy8sx+MNJdLG0fUi3vaSVbztHgJ4=
cloud.google.com/go/recommendationengine v0.7.0/go.mod h1:1reUcE3GIu6MeBz/h5xZJqNLuuVjNg1lmWMPyjatzac=
cloud.google.com/go/recommender v1.5.0/go.mod h1:jdoeiBIVrJe9gQjwd759ecLJbxCDED4A6p+mqoqDvTg=
cloud.google.com/go/recommender v1.6.0/go.mod h1:+yETpm25mcoiECKh9DEScGzIRyDKpZ0cEhWGo+8bo+c=
cloud.google.com/go/recommender v1.7.0/go.mod h1:XLHs/W+T8olwlGOgfQenXBTbIseGclClff6lhFVe9Bs=
cloud.google.com/go/recommender v1.8.0/go.mod h1:PkjXrTT05BFKwxaUxQmtIlrtj0kph108r02ZZQ5FE70=
cloud.google.com/go/recommender v1.9.0/go.mod h1:PnSsnZY7q+VL1uax2JWkt/UegHssxjUVVCrX52CuEmQ=
cloud.google.com/go/redis v1.7.0/go.mod h1:V3x5Jq1jzUcg+UNsRvdmsfuFnit1cfe3Z/PGyq/lm4Y=
cloud.google.com/go/redis v1.8.0/go.mod h1:Fm2szCDavWzBk2cDKxrkmWBqoCiL1+Ctwq7EyqBCA/A=
cloud.google.com/go/redis v1.9.0/go.mod h1:HMYQuajvb2D0LvMgZmLDZW8V5aOC/WxstZHiy4g8OiA=
cloud.google.com/go/redis v1.10.0/go.mod h1:ThJf3mMBQtW18JzGgh41/Wld6vnDDc/F/F35UolRZPM=
cloud.google.com/go/redis v1.11.0/go.mod h1:/X6eicana+BWcUda5PpwZC48o37SiFVTFSs0fWAJ7uQ=
cloud.google.com/go/resourcemanager v1.3.0/go.mod h1:bAtrTjZQFJkiWTPDb1WBjzvc6/kifjj4QBYuKCCoqKA=
cloud.google.com/go/resourcemanager v1.4.0/go.mod h1:MwxuzkumyTX7/a3n37gmsT3py7LIXwrShilPh3P1tR0=
cloud.google.com/go/resourcemanager v1.5.0/go.mod h1:eQoXNAiAvCf5PXxWxXjhKQoTMaUSNrEfg+6qdf/wots=
cloud.google.com/go/resourcemanager v1.6.0/go.mod h1:YcpXGRs8fDzcUl1Xw8uOVmI8JEadvhRIkoXXUNVYcVo=
cloud.google.com/go/resourcemanager v1.7.0/go.mod h1:HlD3m6+bwhzj9XCouqmeiGuni95NTrExfhoSrkC/3EI=
cloud.google.com/go/resourcesettings v1.3.0/go.mod h1:lzew8VfESA5DQ8gdlHwMrqZs1S9V87v3oCnKCWoOuQU=
cloud.google.com/go/resourcesettings v1.4.0/go.mod h1:ldiH9IJpcrlC3VSuCGvjR5of/ezRrOxFtpJoJo5SmXg=
cloud.google.com/go/resourcesettings v1.5.0/go.mod h1:+xJF7QSG6undsQDfsCJyqWXyBwUoJLhetkRMDRnIoXA=
cloud.google.com/go/retail v1.8.0/go.mod h1:QblKS8waDmNUhghY2TI9O3JLlFk8jybHeV4BF19FrE4=
cloud.google.com/go/retail v1.9.0/go.mod h1:g6jb6mKuCS1QKnH/dpu7isX253absFl6iE92nHwlBUY=
cloud.google.com/go/retail v1.10.0/go.mod h1:2gDk9HsL4HMS4oZwz6daui2/jmKvqShXKQuB2RZ+cCc=
cloud.google.com/go/retail v1.11.0/go.mod h1:MBLk1NaWPmh6iVFSz9MeKG/Psyd7TAgm6y/9L2B4x9Y=
cloud.google.com/go/retail v1.12.0/go.mod h1:UMkelN/0Z8XvKymXFbD4EhFJlYKRx1FGhQkVPU5kF14=
cloud.google.com/go/run v0.2.0/go.mod h1:CNtKsTA1sDcnqqIFR3Pb5Tq0usWxJJvsWOCPldRU3Do=
cloud.google.com/go/run v0.3.0/go.mod h1:TuyY1+taHxTjrD0ZFk2iAR+xyOXEA0ztb7U3UNA0zBo=
cloud.google.com/go/run v0.8.0/go.mod h1:VniEnuBwqjigv0A7ONfQUaEItaiCRVujlMqerPPiktM=
cloud.google.com/go/run v0.9.0/go.mod h1:Wwu+/vvg8Y+JUApMwEDfVfhetv30hCG4ZwDR/IXl2Qg=
cloud.google.com/go/scheduler v1.4.0/go.mod h1:drcJBmxF3aqZJRhmkHQ9b3uSSpQoltBPGPxGAWROx6s=
cloud.google.com/go/scheduler v1.5.0/go.mod h1:ri073ym49NW3AfT6DZi21vLZrG07GXr5p3H1KxN5QlI=
cloud.google.com/go/scheduler v1.6.0/go.mod h1:SgeKVM7MIwPn3BqtcBntpLyrIJftQISRrYB5ZtT+KOk=
cloud.google.com/go/scheduler v1.7.0/go.mod h1:jyCiBqWW956uBjjPMMuX09n3x37mtyPJegEWKxRsn44=
cloud.google.com/go/scheduler v1.8.0/go.mod h1:TCET+Y5Gp1YgHT8py4nlg2Sew8nUHMqcpousDgXJVQc=
cloud.google.com/go/scheduler v1.9.0/go.mod h1:yexg5t+KSmqu+njTIh3b7oYPheFtBWGcbVUYF1GGMIc=
cloud.google.com/go/secretmanager v1.6.0/go.mod h1:awVa/OXF6IiyaU1wQ34inzQNc4ISIDIrId8qE5QGgKA=
cloud.google.com/go/secretmanager v1.8.0/go.mod h1:hnVgi/bN5MYHd3Gt0SPuTPPp5ENina1/LxM+2W9U9J4=
cloud.google.com/go/secretmanager v1.9.0/go.mod h1:b71qH2l1yHmWQHt9LC80akm86mX8AL6X1MA01dW8ht4=
cloud.google.com/go/secretmanager v1.10.0/go.mod h1:MfnrdvKMPNra9aZtQFvBcvRU54hbPD8/HayQdlUgJpU=
cloud.google.com/go/security v1.5.0/go.mod h1:lgxGdyOKKjHL4YG3/YwIL2zLqMFCKs0UbQwgyZmfJl4=
cloud.google.com/go/security v1.7.0/go.mod h1:mZklORHl6Bg7CNnnjLH//0UlAlaXqiG7Lb9PsPXLfD0=
cloud.google.com/go/security v1.8.0/go.mod h1:hAQOwgmaHhztFhiQ41CjDODdWP0+AE1B3sX4OFlq+GU=
cloud.google.com/go/security v1.9.0/go.mod h1:6Ta1bO8LXI89nZnmnsZGp9lVoVWXqsVbIq/t9dzI+2Q=
cloud.google.com/go/security v1.10.0/go.mod h1:QtOMZByJVlibUT2h9afNDWRZ1G96gVywH8T5GUSb9IA=
cloud.google.com/go/security v1.12.0/go.mod h1:rV6EhrpbNHrrxqlvW0BWAIawFWq3X90SduMJdFwtLB8=
cloud.google.com/go/security v1.13.0/go.mod h1:Q1Nvxl1PAgmeW0y3HTt54JYIvUdtcpYKVfIB8AOMZ+0=
cloud.google.com/go/securitycenter v1.13.0/go.mod h1:cv5qNAqjY84FCN6Y9z28WlkKXyWsgLO832YiWwkCWcU=
cloud.google.com/go/securitycenter v1.14.0/go.mod h1:gZLAhtyKv85n52XYWt6RmeBdydyxfPeTrpToDPw4Auc=
cloud.google.com/go/securitycenter v1.15.0/go.mod h1:PeKJ0t8MoFmmXLXWm41JidyzI3PJjd8sXWaVqg43WWk=
cloud.google.com/go/securitycenter v1.16.0/go.mod h1:Q9GMaLQFUD+5ZTabrbujNWLtSLZIZF7SAR0wWECrjdk=
cloud.google.com/go/securitycenter v1.18.1/go.mod h1:0/25gAzCM/9OL9vVx4ChPeM/+DlfGQJDwBy/UC8AKK0=
cloud.google.com/go/securitycenter v1.19.0/go.mod h1:LVLmSg8ZkkyaNy4u7HCIshAngSQ8EcIRREP3xBnyfag=
cloud.google.com/go/servicecontrol v1.4.0/go.mod h1:o0hUSJ1TXJAmi/7fLJAedOovnujSEvjKCAFNXPQ1RaU=
cloud.google.com/go/servicecontrol v1.5.0/go.mod h1:qM0CnXHhyqKVuiZnGKrIurvVImCs8gmqWsDoqe9sU1s=
cloud.google.com/go/servicecontrol v1.10.0/go.mod h1:pQvyvSRh7YzUF2efw7H87V92mxU8FnFDawMClGCNuAA=
cloud.google.com/go/servicecontrol v1.11.0/go.mod h1:kFmTzYzTUIuZs0ycVqRHNaNhgR+UMUpw9n02l/pY+mc=
cloud.google.com/go/servicecontrol v1.11.1/go.mod h1:aSnNNlwEFBY+PWGQ2DoM0JJ/QUXqV5/ZD9DOLB7SnUk=
cloud.google.com/go/servicedirectory v1.4.0/go.mod h1:gH1MUaZCgtP7qQiI+F+A+OpeKF/HQWgtAddhTbhL2bs=
cloud.google.com/go/servicedirectory v1.5.0/go.mod h1:QMKFL0NUySbpZJ1UZs3oFAmdvVxhhxB6eJ/Vlp73dfg=
cloud.google.com/go/servicedirectory v1.6.0/go.mod h1:pUlbnWsLH9c13yGkxCmfumWEPjsRs1RlmJ4pqiNjVL4=
cloud.google.com/go/servicedirectory v1.7.0/go.mod h1:5p/U5oyvgYGYejufvxhgwjL8UVXjkuw7q5XcG10wx1U=
cloud.google.com/go/servicedirectory v1.8.0/go.mod h1:srXodfhY1GFIPvltunswqXpVxFPpZjf8nkKQT7XcXaY=
cloud.google.com/go/servicedirectory v1.9.0/go.mod h1:29je5JjiygNYlmsGz8k6o+OZ8vd4f//bQLtvzkPPT/s=
cloud.google.com/go/servicemanagement v1.4.0/go.mod h1:d8t8MDbezI7Z2R1O/wu8oTggo3BI2GKYbdG4y/SJTco=
cloud.google.com/go/servicemanagement v1.5.0/go.mod h1:XGaCRe57kfqu4+lRxaFEAuqmjzF0r+gWHjWqKqBvKFo=
cloud.google.com/go/servicemanagement v1.6.0/go.mod h1:aWns7EeeCOtGEX4OvZUWCCJONRZeFKiptqKf1D0l/Jc=
cloud.google.com/go/servicemanagement v1.8.0/go.mod h1:MSS2TDlIEQD/fzsSGfCdJItQveu9NXnUniTrq/L8LK4=
cloud.google.com/go/serviceusage v1.3.0/go.mod h1:Hya1cozXM4SeSKTAgGXgj97GlqUvF5JaoXacR1JTP/E=
cloud.google.com/go/serviceusage v1.4.0/go.mod h1:SB4yxXSaYVuUBYUml6qklyONXNLt83U0Rb+CXyhjEeU=
cloud.google.com/go/serviceusage v1.5.0/go.mod h1:w8U1JvqUqwJNPEOTQjrMHkw3IaIFLoLsPLvsE3xueec=
cloud.google.com/go/serviceusage v1.6.0/go.mod h1:R5wwQcbOWsyuOfbP9tGdAnCAc6B9DRwPG1xtWMDeuPA=
cloud.google.com/go/shell v1.3.0/go.mod h1:VZ9HmRjZBsjLGXusm7K5Q5lzzByZmJHf1d0IWHEN5X4=
cloud.google.com/go/shell v1.4.0/go.mod h1:HDxPzZf3GkDdhExzD/gs8Grqk+dmYcEjGShZgYa9URw=
cloud.google.com/go/shell v1.6.0/go.mod h1:oHO8QACS90luWgxP3N9iZVuEiSF84zNyLytb+qE2f9A=
cloud.google.com/go/spanner v1.41.0/go.mod h1:MLYDBJR/dY4Wt7ZaMIQ7rXOTLjYrmxLE/5ve9vFfWos=
cloud.google.com/go/spanner v1.44.0/go.mod h1:G8XIgYdOK+Fbcpbs7p2fiprDw4CaZX63whnSMLVBxjk=
cloud.google.com/go/spanner v1.45.0/go.mod h1:FIws5LowYz8YAE1J8fOS7DJup8ff7xJeetWEo5REA2M=
cloud.google.com/go/spanner v1.85.0 h1:VVO3yW+0+Yx9tg4SQaZvJHGAnU6qCnGXQ3NX4E3+src=
cloud.google.com/go/spanner v1.85.0/go.mod h1:9zhmtOEoYV06nE4Orbin0dc/ugHzZW9yXuvaM61rpxs=
cloud.google.com/go/speech v1.6.0/go.mod h1:79tcr4FHCimOp56lwC01xnt/WPJZc4v3gzyT7FoBkCM=
cloud.google.com/go/speech v1.7.0/go.mod h1:KptqL+BAQIhMsj1kOP2la5DSEEerPDuOP/2mmkhHhZQ=
cloud.google.com/go/speech v1.8.0/go.mod h1:9bYIl1/tjsAnMgKGHKmBZzXKEkGgtU+MpdDPTE9f7y0=
cloud.google.com/go/speech v1.9.0/go.mod h1:xQ0jTcmnRFFM2RfX/U+rk6FQNUF6DQlydUSyoooSpco=
cloud.google.com/go/speech v1.14.1/go.mod h1:gEosVRPJ9waG7zqqnsHpYTOoAS4KouMRLDFMekpJ0J0=
cloud.google.com/go/speech v1.15.0/go.mod h1:y6oH7GhqCaZANH7+Oe0BhgIogsNInLlz542tg3VqeYI=
cloud.google.com/go/storage v1.0.0/go.mod h1:IhtSnM/ZTZV8YYJWCY8RULGVqBDmpoyjwiyrjsg+URw=
cloud.google.com/go/storage v1.5.0/go.mod h1:tpKbwo567HUNpVclU5sGELwQWBDZ8gh0ZeosJ0Rtdos=
cloud.google.com/go/storage v1.6.0/go.mod h1:N7U0C8pVQ/+NIKOBQyamJIeKQKkZ+mxpohlUTyfDhBk=
cloud.google.com/go/storage v1.8.0/go.mod h1:Wv1Oy7z6Yz3DshWRJFhqM/UCfaWIRTdp0RXyy7KQOVs=
cloud.google.com/go/storage v1.10.0/go.mod h1:FLPqc6j+Ki4BU591ie1oL6qBQGu2Bl/tZ9ullr3+Kg0=
cloud.google.com/go/storage v1.14.0/go.mod h1:GrKmX003DSIwi9o29oFT7YDnHYwZoctc3fOKtUw0Xmo=
cloud.google.com/go/storage v1.22.1/go.mod h1:S8N1cAStu7BOeFfE8KAQzmyyLkK8p/vmRq6kuBTW58Y=
cloud.google.com/go/storage v1.23.0/go.mod h1:vOEEDNFnciUMhBeT6hsJIn3ieU5cFRmzeLgDvXzfIXc=
cloud.google.com/go/storage v1.27.0/go.mod h1:x9DOL8TK/ygDUMieqwfhdpQryTeEkhGKMi80i/iqR2s=
cloud.google.com/go/storage v1.28.1/go.mod h1:Qnisd4CqDdo6BGs2AD5LLnEsmSQ80wQ5ogcBBKhU86Y=
cloud.google.com/go/storage v1.29.0/go.mod h1:4puEjyTKnku6gfKoTfNOU/W+a9JyuVNxjpS5GBrB8h4=
cloud.google.com/go/storage v1.56.0 h1:iixmq2Fse2tqxMbWhLWC9HfBj1qdxqAmiK8/eqtsLxI=
cloud.google.com/go/storage v1.56.0/go.mod h1:Tpuj6t4NweCLzlNbw9Z9iwxEkrSem20AetIeH/shgVU=
cloud.google.com/go/storagetransfer v1.5.0/go.mod h1:dxNzUopWy7RQevYFHewchb29POFv3/AaBgnhqzqiK0w=
cloud.google.com/go/storagetransfer v1.6.0/go.mod h1:y77xm4CQV/ZhFZH75PLEXY0ROiS7Gh6pSKrM8dJyg6I=
cloud.google.com/go/storagetransfer v1.7.0/go.mod h1:8Giuj1QNb1kfLAiWM1bN6dHzfdlDAVC9rv9abHot2W4=
cloud.google.com/go/storagetransfer v1.8.0/go.mod h1:JpegsHHU1eXg7lMHkvf+KE5XDJ7EQu0GwNJbbVGanEw=
cloud.google.com/go/talent v1.1.0/go.mod h1:Vl4pt9jiHKvOgF9KoZo6Kob9oV4lwd/ZD5Cto54zDRw=
cloud.google.com/go/talent v1.2.0/go.mod h1:MoNF9bhFQbiJ6eFD3uSsg0uBALw4n4gaCaEjBw9zo8g=
cloud.google.com/go/talent v1.3.0/go.mod h1:CmcxwJ/PKfRgd1pBjQgU6W3YBwiewmUzQYH5HHmSCmM=
cloud.google.com/go/talent v1.4.0/go.mod h1:ezFtAgVuRf8jRsvyE6EwmbTK5LKciD4KVnHuDEFmOOA=
cloud.google.com/go/talent v1.5.0/go.mod h1:G+ODMj9bsasAEJkQSzO2uHQWXHHXUomArjWQQYkqK6c=
cloud.google.com/go/texttospeech v1.4.0/go.mod h1:FX8HQHA6sEpJ7rCMSfXuzBcysDAuWusNNNvN9FELDd8=
cloud.google.com/go/texttospeech v1.5.0/go.mod h1:oKPLhR4n4ZdQqWKURdwxMy0uiTS1xU161C8W57Wkea4=
cloud.google.com/go/texttospeech v1.6.0/go.mod h1:YmwmFT8pj1aBblQOI3TfKmwibnsfvhIBzPXcW4EBovc=
cloud.google.com/go/tpu v1.3.0/go.mod h1:aJIManG0o20tfDQlRIej44FcwGGl/cD0oiRyMKG19IQ=
cloud.google.com/go/tpu v1.4.0/go.mod h1:mjZaX8p0VBgllCzF6wcU2ovUXN9TONFLd7iz227X2Xg=
cloud.google.com/go/tpu v1.5.0/go.mod h1:8zVo1rYDFuW2l4yZVY0R0fb/v44xLh3llq7RuV61fPM=
cloud.google.com/go/trace v1.3.0/go.mod h1:FFUE83d9Ca57C+K8rDl/Ih8LwOzWIV1krKgxg6N0G28=
cloud.google.com/go/trace v1.4.0/go.mod h1:UG0v8UBqzusp+z63o7FK74SdFE+AXpCLdFb1rshXG+Y=
cloud.google.com/go/trace v1.8.0/go.mod h1:zH7vcsbAhklH8hWFig58HvxcxyQbaIqMarMg9hn5ECA=
cloud.google.com/go/trace v1.9.0/go.mod h1:lOQqpE5IaWY0Ixg7/r2SjixMuc6lfTFeO4QGM4dQWOk=
cloud.google.com/go/trace v1.11.6 h1:2O2zjPzqPYAHrn3OKl029qlqG6W8ZdYaOWRyr8NgMT4=
cloud.google.com/go/trace v1.11.6/go.mod h1:GA855OeDEBiBMzcckLPE2kDunIpC72N+Pq8WFieFjnI=
cloud.google.com/go/translate v1.3.0/go.mod h1:gzMUwRjvOqj5i69y/LYLd8RrNQk+hOmIXTi9+nb3Djs=
cloud.google.com/go/translate v1.4.0/go.mod h1:06Dn/ppvLD6WvA5Rhdp029IX2Mi3Mn7fpMRLPvXT5Wg=
cloud.google.com/go/translate v1.5.0/go.mod h1:29YDSYveqqpA1CQFD7NQuP49xymq17RXNaUDdc0mNu0=
cloud.google.com/go/translate v1.6.0/go.mod h1:lMGRudH1pu7I3n3PETiOB2507gf3HnfLV8qlkHZEyos=
cloud.google.com/go/translate v1.7.0/go.mod h1:lMGRudH1pu7I3n3PETiOB2507gf3HnfLV8qlkHZEyos=
cloud.google.com/go/video v1.8.0/go.mod h1:sTzKFc0bUSByE8Yoh8X0mn8bMymItVGPfTuUBUyRgxk=
cloud.google.com/go/video v1.9.0/go.mod h1:0RhNKFRF5v92f8dQt0yhaHrEuH95m068JYOvLZYnJSw=
cloud.google.com/go/video v1.12.0/go.mod h1:MLQew95eTuaNDEGriQdcYn0dTwf9oWiA4uYebxM5kdg=
cloud.google.com/go/video v1.13.0/go.mod h1:ulzkYlYgCp15N2AokzKjy7MQ9ejuynOJdf1tR5lGthk=
cloud.google.com/go/video v1.14.0/go.mod h1:SkgaXwT+lIIAKqWAJfktHT/RbgjSuY6DobxEp0C5yTQ=
cloud.google.com/go/video v1.15.0/go.mod h1:SkgaXwT+lIIAKqWAJfktHT/RbgjSuY6DobxEp0C5yTQ=
cloud.google.com/go/videointelligence v1.6.0/go.mod h1:w0DIDlVRKtwPCn/C4iwZIJdvC69yInhW0cfi+p546uU=
cloud.google.com/go/videointelligence v1.7.0/go.mod h1:k8pI/1wAhjznARtVT9U1llUaFNPh7muw8QyOUpavru4=
cloud.google.com/go/videointelligence v1.8.0/go.mod h1:dIcCn4gVDdS7yte/w+koiXn5dWVplOZkE+xwG9FgK+M=
cloud.google.com/go/videointelligence v1.9.0/go.mod h1:29lVRMPDYHikk3v8EdPSaL8Ku+eMzDljjuvRs105XoU=
cloud.google.com/go/videointelligence v1.10.0/go.mod h1:LHZngX1liVtUhZvi2uNS0VQuOzNi2TkY1OakiuoUOjU=
cloud.google.com/go/vision v1.2.0/go.mod h1:SmNwgObm5DpFBme2xpyOyasvBc1aPdjvMk2bBk0tKD0=
cloud.google.com/go/vision/v2 v2.2.0/go.mod h1:uCdV4PpN1S0jyCyq8sIM42v2Y6zOLkZs+4R9LrGYwFo=
cloud.google.com/go/vision/v2 v2.3.0/go.mod h1:UO61abBx9QRMFkNBbf1D8B1LXdS2cGiiCRx0vSpZoUo=
cloud.google.com/go/vision/v2 v2.4.0/go.mod h1:VtI579ll9RpVTrdKdkMzckdnwMyX2JILb+MhPqRbPsY=
cloud.google.com/go/vision/v2 v2.5.0/go.mod h1:MmaezXOOE+IWa+cS7OhRRLK2cNv1ZL98zhqFFZaaH2E=
cloud.google.com/go/vision/v2 v2.6.0/go.mod h1:158Hes0MvOS9Z/bDMSFpjwsUrZ5fPrdwuyyvKSGAGMY=
cloud.google.com/go/vision/v2 v2.7.0/go.mod h1:H89VysHy21avemp6xcf9b9JvZHVehWbET0uT/bcuY/0=
cloud.google.com/go/vmmigration v1.2.0/go.mod h1:IRf0o7myyWFSmVR1ItrBSFLFD/rJkfDCUTO4vLlJvsE=
cloud.google.com/go/vmmigration v1.3.0/go.mod h1:oGJ6ZgGPQOFdjHuocGcLqX4lc98YQ7Ygq8YQwHh9A7g=
cloud.google.com/go/vmmigration v1.5.0/go.mod h1:E4YQ8q7/4W9gobHjQg4JJSgXXSgY21nA5r8swQV+Xxc=
cloud.google.com/go/vmmigration v1.6.0/go.mod h1:bopQ/g4z+8qXzichC7GW1w2MjbErL54rk3/C843CjfY=
cloud.google.com/go/vmwareengine v0.1.0/go.mod h1:RsdNEf/8UDvKllXhMz5J40XxDrNJNN4sagiox+OI208=
cloud.google.com/go/vmwareengine v0.2.2/go.mod h1:sKdctNJxb3KLZkE/6Oui94iw/xs9PRNC2wnNLXsHvH8=
cloud.google.com/go/vmwareengine v0.3.0/go.mod h1:wvoyMvNWdIzxMYSpH/R7y2h5h3WFkx6d+1TIsP39WGY=
cloud.google.com/go/vpcaccess v1.4.0/go.mod h1:aQHVbTWDYUR1EbTApSVvMq1EnT57ppDmQzZ3imqIk4w=
cloud.google.com/go/vpcaccess v1.5.0/go.mod h1:drmg4HLk9NkZpGfCmZ3Tz0Bwnm2+DKqViEpeEpOq0m8=
cloud.google.com/go/vpcaccess v1.6.0/go.mod h1:wX2ILaNhe7TlVa4vC5xce1bCnqE3AeH27RV31lnmZes=
cloud.google.com/go/webrisk v1.4.0/go.mod h1:Hn8X6Zr+ziE2aNd8SliSDWpEnSS1u4R9+xXZmFiHmGE=
cloud.google.com/go/webrisk v1.5.0/go.mod h1:iPG6fr52Tv7sGk0H6qUFzmL3HHZev1htXuWDEEsqMTg=
cloud.google.com/go/webrisk v1.6.0/go.mod h1:65sW9V9rOosnc9ZY7A7jsy1zoHS5W9IAXv6dGqhMQMc=
cloud.google.com/go/webrisk v1.7.0/go.mod h1:mVMHgEYH0r337nmt1JyLthzMr6YxwN1aAIEc2fTcq7A=
cloud.google.com/go/webrisk v1.8.0/go.mod h1:oJPDuamzHXgUc+b8SiHRcVInZQuybnvEW72PqTc7sSg=
cloud.google.com/go/websecurityscanner v1.3.0/go.mod h1:uImdKm2wyeXQevQJXeh8Uun/Ym1VqworNDlBXQevGMo=
cloud.google.com/go/websecurityscanner v1.4.0/go.mod h1:ebit/Fp0a+FWu5j4JOmJEV8S8CzdTkAS77oDsiSqYWQ=
cloud.google.com/go/websecurityscanner v1.5.0/go.mod h1:Y6xdCPy81yi0SQnDY1xdNTNpfY1oAgXUlcfN3B3eSng=
cloud.google.com/go/workflows v1.6.0/go.mod h1:6t9F5h/unJz41YqfBmqSASJSXccBLtD1Vwf+KmJENM0=
cloud.google.com/go/workflows v1.7.0/go.mod h1:JhSrZuVZWuiDfKEFxU0/F1PQjmpnpcoISEXH2bcHC3M=
cloud.google.com/go/workflows v1.8.0/go.mod h1:ysGhmEajwZxGn1OhGOGKsTXc5PyxOc0vfKf5Af+to4M=
cloud.google.com/go/workflows v1.9.0/go.mod h1:ZGkj1aFIOd9c8Gerkjjq7OW7I5+l6cSvT3ujaO/WwSA=
cloud.google.com/go/workflows v1.10.0/go.mod h1:fZ8LmRmZQWacon9UCX1r/g/DfAXx5VcPALq2CxzdePw=
dmitri.shuralyov.com/gpu/mtl v0.0.0-20190408044501-666a987793e9/go.mod h1:H6x//7gZCb22OMCxBHrMx7a5I7Hp++hsVxbQ4BYO7hU=
gioui.org v0.0.0-20210308172011-57750fc8a0a6/go.mod h1:RSH6KIUZ0p2xy5zHDxgAM4zumjgTw83q2ge/PI+yyw8=
git.sr.ht/~sbinet/gg v0.3.1/go.mod h1:KGYtlADtqsqANL9ueOFkWymvzUvLMQllU5Ixo+8v3pc=
github.com/99designs/go-keychain v0.0.0-20191008050251-8e49817e8af4 h1:/vQbFIOMbk2FiG/kXiLl8BRyzTWDw7gX/Hz7Dd5eDMs=
github.com/99designs/go-keychain v0.0.0-20191008050251-8e49817e8af4/go.mod h1:hN7oaIRCjzsZ2dE+yG5k+rsdt3qcwykqK6HVGcKwsw4=
github.com/99designs/keyring v1.2.1 h1:tYLp1ULvO7i3fI5vE21ReQuj99QFSs7lGm0xWyJo87o=
github.com/99designs/keyring v1.2.1/go.mod h1:fc+wB5KTk9wQ9sDx0kFXB3A0MaeGHM9AwRStKOQ5vOA=
github.com/Azure/azure-sdk-for-go/sdk/azcore v1.0.0/go.mod h1:uGG2W01BaETf0Ozp+QxxKJdMBNRWPdstHG0Fmdwn1/U=
github.com/Azure/azure-sdk-for-go/sdk/azcore v1.1.2/go.mod h1:uGG2W01BaETf0Ozp+QxxKJdMBNRWPdstHG0Fmdwn1/U=
github.com/Azure/azure-sdk-for-go/sdk/azcore v1.4.0 h1:rTnT/Jrcm+figWlYz4Ixzt0SJVR2cMC8lvZcimipiEY=
github.com/Azure/azure-sdk-for-go/sdk/azcore v1.4.0/go.mod h1:ON4tFdPTwRcgWEaVDrN3584Ef+b7GgSJaXxe5fW9t4M=
github.com/Azure/azure-sdk-for-go/sdk/azidentity v1.2.1 h1:T8quHYlUGyb/oqtSTwqlCr1ilJHrDv+ZtpSfo+hm1BU=
github.com/Azure/azure-sdk-for-go/sdk/azidentity v1.2.1/go.mod h1:gLa1CL2RNE4s7M3yopJ/p0iq5DdY6Yv5ZUt9MTRZOQM=
github.com/Azure/azure-sdk-for-go/sdk/internal v1.0.0/go.mod h1:eWRD7oawr1Mu1sLCawqVc0CUiF43ia3qQMxLscsKQ9w=
github.com/Azure/azure-sdk-for-go/sdk/internal v1.1.2 h1:+5VZ72z0Qan5Bog5C+ZkgSqUbeVUd9wgtHOrIKuc5b8=
github.com/Azure/azure-sdk-for-go/sdk/internal v1.1.2/go.mod h1:eWRD7oawr1Mu1sLCawqVc0CUiF43ia3qQMxLscsKQ9w=
github.com/Azure/azure-sdk-for-go/sdk/storage/azblob v1.0.0 h1:u/LLAOFgsMv7HmNL4Qufg58y+qElGOt5qv0z1mURkRY=
github.com/Azure/azure-sdk-for-go/sdk/storage/azblob v1.0.0/go.mod h1:2e8rMJtl2+2j+HXbTBwnyGpm5Nou7KhvSfxOq8JpTag=
github.com/Azure/go-ansiterm v0.0.0-20230124172434-306776ec8161 h1:L/gRVlceqvL25UVaW/CKtUDjefjrs0SPonmDGUVOYP0=
github.com/Azure/go-ansiterm v0.0.0-20230124172434-306776ec8161/go.mod h1:xomTg63KZ2rFqZQzSB4Vz2SUXa1BpHTVz9L5PTmPC4E=
github.com/Azure/go-autorest v14.2.0+incompatible h1:V5VMDjClD3GiElqLWO7mz2MxNAK/vTfRHdAubSIPRgs=
github.com/Azure/go-autorest v14.2.0+incompatible/go.mod h1:r+4oMnoxhatjLLJ6zxSWATqVooLgysK6ZNox3g/xq24=
github.com/Azure/go-autorest/autorest/adal v0.9.16 h1:P8An8Z9rH1ldbOLdFpxYorgOt2sywL9V24dAwWHPuGc=
github.com/Azure/go-autorest/autorest/adal v0.9.16/go.mod h1:tGMin8I49Yij6AQ+rvV+Xa/zwxYQB5hmsd6DkfAx2+A=
github.com/Azure/go-autorest/autorest/date v0.3.0 h1:7gUk1U5M/CQbp9WoqinNzJar+8KY+LPI6wiWrP/myHw=
github.com/Azure/go-autorest/autorest/date v0.3.0/go.mod h1:BI0uouVdmngYNUzGWeSYnokU+TrmwEsOqdt8Y6sso74=
github.com/Azure/go-autorest/autorest/mocks v0.4.1 h1:K0laFcLE6VLTOwNgSxaGbUcLPuGXlNkbVvq4cW4nIHk=
github.com/Azure/go-autorest/autorest/mocks v0.4.1/go.mod h1:LTp+uSrOhSkaKrUy935gNZuuIPPVsHlr9DSOxSayd+k=
github.com/Azure/go-autorest/logger v0.2.1 h1:IG7i4p/mDa2Ce4TRyAO8IHnVhAVF3RFU+ZtXWSmf4Tg=
github.com/Azure/go-autorest/logger v0.2.1/go.mod h1:T9E3cAhj2VqvPOtCYAvby9aBXkZmbF5NWuPV8+WeEW8=
github.com/Azure/go-autorest/tracing v0.6.0 h1:TYi4+3m5t6K48TGI9AUdb+IzbnSxvnvUMfuitfgcfuo=
github.com/Azure/go-autorest/tracing v0.6.0/go.mod h1:+vhtPC754Xsa23ID7GlGsrdKBpUA79WCAKPPZVC2DeU=
github.com/AzureAD/microsoft-authentication-library-for-go v0.8.1 h1:oPdPEZFSbl7oSPEAIPMPBMUmiL+mqgzBJwM/9qYcwNg=
github.com/AzureAD/microsoft-authentication-library-for-go v0.8.1/go.mod h1:4qFor3D/HDsvBME35Xy9rwW9DecL+M2sNw1ybjPtwA0=
github.com/BurntSushi/toml v0.3.1/go.mod h1:xHWCNGjB5oqiDr8zfno3MHue2Ht5sIBksp03qcyfWMU=
github.com/BurntSushi/xgb v0.0.0-20160522181843-27f122750802/go.mod h1:IVnqGOEym/WlBOVXweHU+Q+/VP0lqqI8lqeDx9IjBqo=
github.com/ClickHouse/clickhouse-go v1.4.3 h1:iAFMa2UrQdR5bHJ2/yaSLffZkxpcOYQMCUuKeNXGdqc=
github.com/ClickHouse/clickhouse-go v1.4.3/go.mod h1:EaI/sW7Azgz9UATzd5ZdZHRUhHgv5+JMS9NSr2smCJI=
github.com/GoogleCloudPlatform/grpc-gcp-go/grpcgcp v1.5.3 h1:2afWGsMzkIcN8Qm4mgPJKZWyroE5QBszMiDMYEBrnfw=
github.com/GoogleCloudPlatform/grpc-gcp-go/grpcgcp v1.5.3/go.mod h1:dppbR7CwXD4pgtV9t3wD1812RaLDcBjtblcDF5f1vI0=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.27.0 h1:ErKg/3iS1AKcTkf3yixlZ54f9U1rljCkQyEXWUnIUxc=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.27.0/go.mod h1:yAZHSGnqScoU556rBOVkwLze6WP5N+U11RHuWaGVxwY=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric v0.53.0 h1:owcC2UnmsZycprQ5RfRgjydWhuoxg71LUfyiQdijZuM=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric v0.53.0/go.mod h1:ZPpqegjbE99EPKsu3iUWV22A04wzGPcAY/ziSIQEEgs=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/cloudmock v0.53.0 h1:4LP6hvB4I5ouTbGgWtixJhgED6xdf67twf9PoY96Tbg=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/cloudmock v0.53.0/go.mod h1:jUZ5LYlw40WMd07qxcQJD5M40aUxrfwqQX1g7zxYnrQ=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping v0.53.0 h1:Ron4zCA/yk6U7WOBXhTJcDpsUBG9npumK6xw2auFltQ=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping v0.53.0/go.mod h1:cSgYe11MCNYunTnRXrKiR/tHc0eoKjICUuWpNZoVCOo=
github.com/JohnCGriffin/overflow v0.0.0-20211019200055-46fa312c352c h1:RGWPOewvKIROun94nF7v2cua9qP+thov/7M50KEoeSU=
github.com/JohnCGriffin/overflow v0.0.0-20211019200055-46fa312c352c/go.mod h1:X0CRv0ky0k6m906ixxpzmDRLvX58TFUKS2eePweuyxk=
github.com/Masterminds/semver/v3 v3.1.1 h1:hLg3sBzpNErnxhQtUy/mmLR2I9foDujNK030IGemrRc=
github.com/Masterminds/semver/v3 v3.1.1/go.mod h1:VPu/7SZ7ePZ3QOrcuXROw5FAcLl4a0cBrbBpGY/8hQs=
github.com/Microsoft/go-winio v0.6.2 h1:F2VQgta7ecxGYO8k3ZZz3RS8fVIXVxONVUPlNERoyfY=
github.com/Microsoft/go-winio v0.6.2/go.mod h1:yd8OoFMLzJbo9gZq8j5qaps8bJ9aShtEA8Ipt1oGCvU=
github.com/OneOfOne/xxhash v1.2.2/go.mod h1:HSdplMjZKSmBqAxg5vPj2TmRDmfkzw+cTzAElWljhcU=
github.com/ajstarks/deck v0.0.0-20200831202436-30c9fc6549a9/go.mod h1:JynElWSGnm/4RlzPXRlREEwqTHAN3T56Bv2ITsFT3gY=
github.com/ajstarks/deck/generate v0.0.0-20210309230005-c3f852c02e19/go.mod h1:T13YZdzov6OU0A1+RfKZiZN9ca6VeKdBdyDV+BY97Tk=
github.com/ajstarks/svgo v0.0.0-20180226025133-644b8db467af/go.mod h1:K08gAheRH3/J6wwsYMMT4xOr94bZjxIelGM0+d/wbFw=
github.com/ajstarks/svgo v0.0.0-20211024235047-1546f124cd8b/go.mod h1:1KcenG0jGWcpt8ov532z81sp/kMMUG485J2InIOyADM=
github.com/andybalholm/brotli v1.0.4 h1:V7DdXeJtZscaqfNuAdSRuRFzuiKlHSC/Zh3zl9qY3JY=
github.com/andybalholm/brotli v1.0.4/go.mod h1:fO7iG3H7G2nSZ7m0zPUDn85XEX2GTukHGRSepvi9Eig=
github.com/antihax/optional v1.0.0/go.mod h1:uupD/76wgC+ih3iEmQUL+0Ugr19nfwCT1kdvxnR2qWY=
github.com/apache/arrow/go/v10 v10.0.1 h1:n9dERvixoC/1JjDmBcs9FPaEryoANa2sCgVFo6ez9cI=
github.com/apache/arrow/go/v10 v10.0.1/go.mod h1:YvhnlEePVnBS4+0z3fhPfUy7W1Ikj0Ih0vcRo/gZ1M0=
github.com/apache/arrow/go/v11 v11.0.0/go.mod h1:Eg5OsL5H+e299f7u5ssuXsuHQVEGC4xei5aX110hRiI=
github.com/apache/thrift v0.16.0 h1:qEy6UW60iVOlUy+b9ZR0d5WzUWYGOo4HfopoyBaNmoY=
github.com/apache/thrift v0.16.0/go.mod h1:PHK3hniurgQaNMZYaCLEqXKsYK8upmhPbmdP2FXSqgU=
github.com/aws/aws-sdk-go v1.49.6 h1:yNldzF5kzLBRvKlKz1S0bkvc2+04R1kt13KfBWQBfFA=
github.com/aws/aws-sdk-go v1.49.6/go.mod h1:LF8svs817+Nz+DmiMQKTO3ubZ/6IaTpq3TjupRn3Eqk=
github.com/aws/aws-sdk-go-v2 v1.16.16 h1:M1fj4FE2lB4NzRb9Y0xdWsn2P0+2UHVxwKyOa4YJNjk=
github.com/aws/aws-sdk-go-v2 v1.16.16/go.mod h1:SwiyXi/1zTUZ6KIAmLK5V5ll8SiURNUYOqTerZPaF9k=
github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream v1.4.8 h1:tcFliCWne+zOuUfKNRn8JdFBuWPDuISDH08wD2ULkhk=
github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream v1.4.8/go.mod h1:JTnlBSot91steJeti4ryyu/tLd4Sk84O5W22L7O2EQU=
github.com/aws/aws-sdk-go-v2/config v1.17.7 h1:odVM52tFHhpqZBKNjVW5h+Zt1tKHbhdTQRb+0WHrNtw=
github.com/aws/aws-sdk-go-v2/config v1.17.7/go.mod h1:dN2gja/QXxFF15hQreyrqYhLBaQo1d9ZKe/v/uplQoI=
github.com/aws/aws-sdk-go-v2/credentials v1.12.20 h1:9+ZhlDY7N9dPnUmf7CDfW9In4sW5Ff3bh7oy4DzS1IE=
github.com/aws/aws-sdk-go-v2/credentials v1.12.20/go.mod h1:UKY5HyIux08bbNA7Blv4PcXQ8cTkGh7ghHMFklaviR4=
github.com/aws/aws-sdk-go-v2/feature/ec2/imds v1.12.17 h1:r08j4sbZu/RVi+BNxkBJwPMUYY3P8mgSDuKkZ/ZN1lE=
github.com/aws/aws-sdk-go-v2/feature/ec2/imds v1.12.17/go.mod h1:yIkQcCDYNsZfXpd5UX2Cy+sWA1jPgIhGTw9cOBzfVnQ=
github.com/aws/aws-sdk-go-v2/feature/s3/manager v1.11.33 h1:fAoVmNGhir6BR+RU0/EI+6+D7abM+MCwWf8v4ip5jNI=
github.com/aws/aws-sdk-go-v2/feature/s3/manager v1.11.33/go.mod h1:84XgODVR8uRhmOnUkKGUZKqIMxmjmLOR8Uyp7G/TPwc=
github.com/aws/aws-sdk-go-v2/internal/configsources v1.1.23 h1:s4g/wnzMf+qepSNgTvaQQHNxyMLKSawNhKCPNy++2xY=
github.com/aws/aws-sdk-go-v2/internal/configsources v1.1.23/go.mod h1:2DFxAQ9pfIRy0imBCJv+vZ2X6RKxves6fbnEuSry6b4=
github.com/aws/aws-sdk-go-v2/internal/endpoints/v2 v2.4.17 h1:/K482T5A3623WJgWT8w1yRAFK4RzGzEl7y39yhtn9eA=
github.com/aws/aws-sdk-go-v2/internal/endpoints/v2 v2.4.17/go.mod h1:pRwaTYCJemADaqCbUAxltMoHKata7hmB5PjEXeu0kfg=
github.com/aws/aws-sdk-go-v2/internal/ini v1.3.24 h1:wj5Rwc05hvUSvKuOF29IYb9QrCLjU+rHAy/x/o0DK2c=
github.com/aws/aws-sdk-go-v2/internal/ini v1.3.24/go.mod h1:jULHjqqjDlbyTa7pfM7WICATnOv+iOhjletM3N0Xbu8=
github.com/aws/aws-sdk-go-v2/internal/v4a v1.0.14 h1:ZSIPAkAsCCjYrhqfw2+lNzWDzxzHXEckFkTePL5RSWQ=
github.com/aws/aws-sdk-go-v2/internal/v4a v1.0.14/go.mod h1:AyGgqiKv9ECM6IZeNQtdT8NnMvUb3/2wokeq2Fgryto=
github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding v1.9.9 h1:Lh1AShsuIJTwMkoxVCAYPJgNG5H+eN6SmoUn8nOZ5wE=
github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding v1.9.9/go.mod h1:a9j48l6yL5XINLHLcOKInjdvknN+vWqPBxqeIDw7ktw=
github.com/aws/aws-sdk-go-v2/service/internal/checksum v1.1.18 h1:BBYoNQt2kUZUUK4bIPsKrCcjVPUMNsgQpNAwhznK/zo=
github.com/aws/aws-sdk-go-v2/service/internal/checksum v1.1.18/go.mod h1:NS55eQ4YixUJPTC+INxi2/jCqe1y2Uw3rnh9wEOVJxY=
github.com/aws/aws-sdk-go-v2/service/internal/presigned-url v1.9.17 h1:Jrd/oMh0PKQc6+BowB+pLEwLIgaQF29eYbe7E1Av9Ug=
github.com/aws/aws-sdk-go-v2/service/internal/presigned-url v1.9.17/go.mod h1:4nYOrY41Lrbk2170/BGkcJKBhws9Pfn8MG3aGqjjeFI=
github.com/aws/aws-sdk-go-v2/service/internal/s3shared v1.13.17 h1:HfVVR1vItaG6le+Bpw6P4midjBDMKnjMyZnw9MXYUcE=
github.com/aws/aws-sdk-go-v2/service/internal/s3shared v1.13.17/go.mod h1:YqMdV+gEKCQ59NrB7rzrJdALeBIsYiVi8Inj3+KcqHI=
github.com/aws/aws-sdk-go-v2/service/s3 v1.27.11 h1:3/gm/JTX9bX8CpzTgIlrtYpB3EVBDxyg/GY/QdcIEZw=
github.com/aws/aws-sdk-go-v2/service/s3 v1.27.11/go.mod h1:fmgDANqTUCxciViKl9hb/zD5LFbvPINFRgWhDbR+vZo=
github.com/aws/aws-sdk-go-v2/service/sso v1.11.23 h1:pwvCchFUEnlceKIgPUouBJwK81aCkQ8UDMORfeFtW10=
github.com/aws/aws-sdk-go-v2/service/sso v1.11.23/go.mod h1:/w0eg9IhFGjGyyncHIQrXtU8wvNsTJOP0R6PPj0wf80=
github.com/aws/aws-sdk-go-v2/service/ssooidc v1.13.5 h1:GUnZ62TevLqIoDyHeiWj2P7EqaosgakBKVvWriIdLQY=
github.com/aws/aws-sdk-go-v2/service/ssooidc v1.13.5/go.mod h1:csZuQY65DAdFBt1oIjO5hhBR49kQqop4+lcuCjf2arA=
github.com/aws/aws-sdk-go-v2/service/sts v1.16.19 h1:9pPi0PsFNAGILFfPCk8Y0iyEBGc6lu6OQ97U7hmdesg=
github.com/aws/aws-sdk-go-v2/service/sts v1.16.19/go.mod h1:h4J3oPZQbxLhzGnk+j9dfYHi5qIOVJ5kczZd658/ydM=
github.com/aws/smithy-go v1.13.3 h1:l7LYxGuzK6/K+NzJ2mC+VvLUbae0sL3bXU//04MkmnA=
github.com/aws/smithy-go v1.13.3/go.mod h1:Tg+OJXh4MB2R/uN61Ko2f6hTZwB/ZYGOtib8J3gBHzA=
github.com/bitly/go-hostpool v0.0.0-20171023180738-a3a6125de932 h1:mXoPYz/Ul5HYEDvkta6I8/rnYM5gSdSV2tJ6XbZuEtY=
github.com/bitly/go-hostpool v0.0.0-20171023180738-a3a6125de932/go.mod h1:NOuUCSz6Q9T7+igc/hlvDOUdtWKryOrtFyIVABv/p7k=
github.com/bkaradzic/go-lz4 v1.0.0 h1:RXc4wYsyz985CkXXeX04y4VnZFGG8Rd43pRaHsOXAKk=
github.com/bkaradzic/go-lz4 v1.0.0/go.mod h1:0YdlkowM3VswSROI7qDxhRvJ3sLhlFrRRwjwegp5jy4=
github.com/bmizerany/assert v0.0.0-20160611221934-b7ed37b82869 h1:DDGfHa7BWjL4YnC6+E63dPcxHo2sUxDIu8g3QgEJdRY=
github.com/bmizerany/assert v0.0.0-20160611221934-b7ed37b82869/go.mod h1:Ekp36dRnpXw/yCqJaO+ZrUyxD+3VXMFFr56k5XYrpB4=
github.com/boombuler/barcode v1.0.0/go.mod h1:paBWMcWSl3LHKBqUq+rly7CNSldXjb2rDl3JlRe0mD8=
github.com/boombuler/barcode v1.0.1/go.mod h1:paBWMcWSl3LHKBqUq+rly7CNSldXjb2rDl3JlRe0mD8=
github.com/cenkalti/backoff/v4 v4.1.2 h1:6Yo7N8UP2K6LWZnW94DLVSSrbobcWdVzAYOisuDPIFo=
github.com/cenkalti/backoff/v4 v4.1.2/go.mod h1:scbssz8iZGpm3xbr14ovlUdkxfGXNInqkPWOWmG2CLw=
github.com/census-instrumentation/opencensus-proto v0.2.1/go.mod h1:f6KPmirojxKA12rnyqOA5BBL4O983OfeGPqjHWSTneU=
github.com/census-instrumentation/opencensus-proto v0.3.0/go.mod h1:f6KPmirojxKA12rnyqOA5BBL4O983OfeGPqjHWSTneU=
github.com/census-instrumentation/opencensus-proto v0.4.1/go.mod h1:4T9NM4+4Vw91VeyqjLS6ao50K5bOcLKN6Q42XnYaRYw=
github.com/cespare/xxhash v1.1.0/go.mod h1:XrSqR1VqqWfGrhpAt58auRo0WTKS1nRRg3ghfAqPWnc=
github.com/cespare/xxhash/v2 v2.1.1/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/cespare/xxhash/v2 v2.2.0/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/cespare/xxhash/v2 v2.3.0 h1:UL815xU9SqsFlibzuggzjXhog7bL6oX9BbNZnL2UFvs=
github.com/cespare/xxhash/v2 v2.3.0/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/chzyer/logex v1.1.10/go.mod h1:+Ywpsq7O8HXn0nuIou7OrIPyXbp3wmkHB+jjWRnGsAI=
github.com/chzyer/readline v0.0.0-20180603132655-2972be24d48e/go.mod h1:nSuG5e5PlCu98SY8svDHJxuZscDgtXS6KTTbou5AhLI=
github.com/chzyer/test v0.0.0-20180213035817-a1ea475d72b1/go.mod h1:Q3SI9o4m/ZMnBNeIyt5eFwwo7qiLfzFZmjNmxjkiQlU=
github.com/client9/misspell v0.3.4/go.mod h1:qj6jICC3Q7zFZvVWo7KLAzC3yx5G7kyvSDkc90ppPyw=
github.com/cloudflare/golz4 v0.0.0-20150217214814-ef862a3cdc58 h1:F1EaeKL/ta07PY/k9Os/UFtwERei2/XzGemhpGnBKNg=
github.com/cloudflare/golz4 v0.0.0-20150217214814-ef862a3cdc58/go.mod h1:EOBUe0h4xcZ5GoxqC5SDxFQ8gwyZPKQoEzownBlhI80=
github.com/cncf/udpa/go v0.0.0-20191209042840-269d4d468f6f/go.mod h1:M8M6+tZqaGXZJjfX53e64911xZQV5JYwmTeXPW+k8Sc=
github.com/cncf/udpa/go v0.0.0-20200629203442-efcf912fb354/go.mod h1:WmhPx2Nbnhtbo57+VJT5O0JRkEi1Wbu0z5j0R8u5Hbk=
github.com/cncf/udpa/go v0.0.0-20201120205902-5459f2c99403/go.mod h1:WmhPx2Nbnhtbo57+VJT5O0JRkEi1Wbu0z5j0R8u5Hbk=
github.com/cncf/udpa/go v0.0.0-20210930031921-04548b0d99d4/go.mod h1:6pvJx4me5XPnfI9Z40ddWsdw2W/uZgQLFXToKeRcDiI=
github.com/cncf/udpa/go v0.0.0-20220112060539-c52dc94e7fbe/go.mod h1:6pvJx4me5XPnfI9Z40ddWsdw2W/uZgQLFXToKeRcDiI=
github.com/cncf/xds/go v0.0.0-20210312221358-fbca930ec8ed/go.mod h1:eXthEFrGJvWHgFFCl3hGmgk+/aYT6PnTQLykKQRLhEs=
github.com/cncf/xds/go v0.0.0-20210805033703-aa0b78936158/go.mod h1:eXthEFrGJvWHgFFCl3hGmgk+/aYT6PnTQLykKQRLhEs=
github.com/cncf/xds/go v0.0.0-20210922020428-25de7278fc84/go.mod h1:eXthEFrGJvWHgFFCl3hGmgk+/aYT6PnTQLykKQRLhEs=
github.com/cncf/xds/go v0.0.0-20211001041855-01bcc9b48dfe/go.mod h1:eXthEFrGJvWHgFFCl3hGmgk+/aYT6PnTQLykKQRLhEs=
github.com/cncf/xds/go v0.0.0-20211011173535-cb28da3451f1/go.mod h1:eXthEFrGJvWHgFFCl3hGmgk+/aYT6PnTQLykKQRLhEs=
github.com/cncf/xds/go v0.0.0-20220314180256-7f1daf1720fc/go.mod h1:eXthEFrGJvWHgFFCl3hGmgk+/aYT6PnTQLykKQRLhEs=
github.com/cncf/xds/go v0.0.0-20230105202645-06c439db220b/go.mod h1:eXthEFrGJvWHgFFCl3hGmgk+/aYT6PnTQLykKQRLhEs=
github.com/cncf/xds/go v0.0.0-20230607035331-e9ce68804cb4/go.mod h1:eXthEFrGJvWHgFFCl3hGmgk+/aYT6PnTQLykKQRLhEs=
github.com/cncf/xds/go v0.0.0-20250501225837-2ac532fd4443 h1:aQ3y1lwWyqYPiWZThqv1aFbZMiM9vblcSArJRf2Irls=
github.com/cncf/xds/go v0.0.0-20250501225837-2ac532fd4443/go.mod h1:W+zGtBO5Y1IgJhy4+A9GOqVhqLpfZi+vwmdNXUehLA8=
github.com/cockroachdb/apd v1.1.0 h1:3LFP3629v+1aKXU5Q37mxmRxX/pIu1nijXydLShEq5I=
github.com/cockroachdb/apd v1.1.0/go.mod h1:8Sl8LxpKi29FqWXR16WEFZRNSz3SoPzUzeMeY4+DwBQ=
github.com/cockroachdb/cockroach-go/v2 v2.1.1 h1:3XzfSMuUT0wBe1a3o5C0eOTcArhmmFAg2Jzh/7hhKqo=
github.com/cockroachdb/cockroach-go/v2 v2.1.1/go.mod h1:7NtUnP6eK+l6k483WSYNrq3Kb23bWV10IRV1TyeSpwM=
github.com/containerd/errdefs v1.0.0 h1:tg5yIfIlQIrxYtu9ajqY42W3lpS19XqdxRQeEwYG8PI=
github.com/containerd/errdefs v1.0.0/go.mod h1:+YBYIdtsnF4Iw6nWZhJcqGSg/dwvV7tyJ/kCkyJ2k+M=
github.com/containerd/errdefs/pkg v0.3.0 h1:9IKJ06FvyNlexW690DXuQNx2KA2cUJXx151Xdx3ZPPE=
github.com/containerd/errdefs/pkg v0.3.0/go.mod h1:NJw6s9HwNuRhnjJhM7pylWwMyAkmCQvQ4GpJHEqRLVk=
github.com/containerd/log v0.1.0 h1:TCJt7ioM2cr/tfR8GPbGf9/VRAX8D2B4PjzCpfX540I=
github.com/containerd/log v0.1.0/go.mod h1:VRRf09a7mHDIRezVKTRCrOq78v577GXq3bSa3EhrzVo=
github.com/coreos/go-systemd v0.0.0-20190321100706-95778dfbb74e/go.mod h1:F5haX7vjVVG0kc13fIWeqUViNPyEJxv/OmvnBo0Yme4=
github.com/coreos/go-systemd v0.0.0-20190719114852-fd7a80b32e1f/go.mod h1:F5haX7vjVVG0kc13fIWeqUViNPyEJxv/OmvnBo0Yme4=
github.com/creack/pty v1.1.7/go.mod h1:lj5s0c3V2DBrqTV7llrYr5NG6My20zk30Fl46Y7DoTY=
github.com/creack/pty v1.1.9/go.mod h1:oKZEueFk5CKHvIhNR5MUki03XCEU+Q6VDXinZuGJ33E=
github.com/creack/pty v1.1.18 h1:n56/Zwd5o6whRC5PMGretI4IdRLlmBXYNjScPaBgsbY=
github.com/creack/pty v1.1.18/go.mod h1:MOBLtS5ELjhRRrroQr9kyvTxUAFNvYEK993ew/Vr4O4=
github.com/cznic/mathutil v0.0.0-20180504122225-ca4c9f2c1369 h1:XNT/Zf5l++1Pyg08/HV04ppB0gKxAqtZQBRYiYrUuYk=
github.com/cznic/mathutil v0.0.0-20180504122225-ca4c9f2c1369/go.mod h1:e6NPNENfs9mPDVNRekM7lKScauxd5kXTr1Mfyig6TDM=
github.com/danieljoos/wincred v1.1.2 h1:QLdCxFs1/Yl4zduvBdcHB8goaYk9RARS2SgLLRuAyr0=
github.com/danieljoos/wincred v1.1.2/go.mod h1:GijpziifJoIBfYh+S7BbkdUTU4LfM+QnGqR5Vl2tAx0=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc h1:U9qPSI2PIWSS1VwoXQT9A3Wy9MM3WgvqSxFWenqJduM=
github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/dhui/dktest v0.4.6 h1:+DPKyScKSEp3VLtbMDHcUq6V5Lm5zfZZVb0Sk7Ahom4=
github.com/dhui/dktest v0.4.6/go.mod h1:JHTSYDtKkvFNFHJKqCzVzqXecyv+tKt8EzceOmQOgbU=
github.com/distribution/reference v0.6.0 h1:0IXCQ5g4/QMHHkarYzh5l+u8T3t73zM5QvfrDyIgxBk=
github.com/distribution/reference v0.6.0/go.mod h1:BbU0aIcezP1/5jX/8MP0YiH4SdvB5Y4f/wlDRiLyi3E=
github.com/dnaeon/go-vcr v1.1.0/go.mod h1:M7tiix8f0r6mKKJ3Yq/kqU1OYf3MnfmBWVbPx/yU9ko=
github.com/dnaeon/go-vcr v1.2.0 h1:zHCHvJYTMh1N7xnV7zf1m1GPBF9Ad0Jk/whtQ1663qI=
github.com/dnaeon/go-vcr v1.2.0/go.mod h1:R4UdLID7HZT3taECzJs4YgbbH6PIGXB6W/sc5OLb6RQ=
github.com/docker/docker v28.3.3+incompatible h1:Dypm25kh4rmk49v1eiVbsAtpAsYURjYkaKubwuBdxEI=
github.com/docker/docker v28.3.3+incompatible/go.mod h1:eEKB0N0r5NX/I1kEveEz05bcu8tLC/8azJZsviup8Sk=
github.com/docker/go-connections v0.5.0 h1:USnMq7hx7gwdVZq1L49hLXaFtUdTADjXGp+uj1Br63c=
github.com/docker/go-connections v0.5.0/go.mod h1:ov60Kzw0kKElRwhNs9UlUHAE/F9Fe6GLaXnqyDdmEXc=
github.com/docker/go-units v0.5.0 h1:69rxXcBk27SvSaaxTtLh/8llcHD8vYHT7WSdRZ/jvr4=
github.com/docker/go-units v0.5.0/go.mod h1:fgPhTUdO+D/Jk86RDLlptpiXQzgHJF7gydDDbaIK4Dk=
github.com/docopt/docopt-go v0.0.0-20180111231733-ee0de3bc6815/go.mod h1:WwZ+bS3ebgob9U8Nd0kOddGdZWjyMGR8Wziv+TBNwSE=
github.com/dustin/go-humanize v1.0.0 h1:VSnTsYCnlFHaM2/igO1h6X3HA71jcobQuxemgkq4zYo=
github.com/dustin/go-humanize v1.0.0/go.mod h1:HtrtbFcZ19U5GC7JDqmcUSB87Iq5E25KnS6fMYU6eOk=
github.com/dvsekhvalnov/jose2go v1.7.0 h1:bnQc8+GMnidJZA8zc6lLEAb4xNrIqHwO+9TzqvtQZPo=
github.com/dvsekhvalnov/jose2go v1.7.0/go.mod h1:QsHjhyTlD/lAVqn/NSbVZmSCGeDehTB/mPZadG+mhXU=
github.com/edsrzf/mmap-go v0.0.0-20170320065105-0bce6a688712 h1:aaQcKT9WumO6JEJcRyTqFVq4XUZiUcKR2/GI31TOcz8=
github.com/edsrzf/mmap-go v0.0.0-20170320065105-0bce6a688712/go.mod h1:YO35OhQPt3KJa3ryjFM5Bs14WD66h8eGKpfaBNrHW5M=
github.com/envoyproxy/go-control-plane v0.9.0/go.mod h1:YTl/9mNaCwkRvm6d1a2C3ymFceY/DCBVvsKhRF0iEA4=
github.com/envoyproxy/go-control-plane v0.9.1-0.20191026205805-5f8ba28d4473/go.mod h1:YTl/9mNaCwkRvm6d1a2C3ymFceY/DCBVvsKhRF0iEA4=
github.com/envoyproxy/go-control-plane v0.9.4/go.mod h1:6rpuAdCZL397s3pYoYcLgu1mIlRU8Am5FuJP05cCM98=
github.com/envoyproxy/go-control-plane v0.9.7/go.mod h1:cwu0lG7PUMfa9snN8LXBig5ynNVH9qI8YYLbd1fK2po=
github.com/envoyproxy/go-control-plane v0.9.9-0.20201210154907-fd9021fe5dad/go.mod h1:cXg6YxExXjJnVBQHBLXeUAgxn2UodCpnH306RInaBQk=
github.com/envoyproxy/go-control-plane v0.9.9-0.20210217033140-668b12f5399d/go.mod h1:cXg6YxExXjJnVBQHBLXeUAgxn2UodCpnH306RInaBQk=
github.com/envoyproxy/go-control-plane v0.9.9-0.20210512163311-63b5d3c536b0/go.mod h1:hliV/p42l8fGbc6Y9bQ70uLwIvmJyVE5k4iMKlh8wCQ=
github.com/envoyproxy/go-control-plane v0.9.10-0.20210907150352-cf90f659a021/go.mod h1:AFq3mo9L8Lqqiid3OhADV3RfLJnjiw63cSpi+fDTRC0=
github.com/envoyproxy/go-control-plane v0.10.2-0.20220325020618-49ff273808a1/go.mod h1:KJwIaB5Mv44NWtYuAOFCVOjcI94vtpEz2JU/D2v6IjE=
github.com/envoyproxy/go-control-plane v0.10.3/go.mod h1:fJJn/j26vwOu972OllsvAgJJM//w9BV6Fxbg2LuVd34=
github.com/envoyproxy/go-control-plane v0.11.1-0.20230524094728-9239064ad72f/go.mod h1:sfYdkwUW4BA3PbKjySwjJy+O4Pu0h62rlqCMHNk+K+Q=
github.com/envoyproxy/go-control-plane v0.13.4 h1:zEqyPVyku6IvWCFwux4x9RxkLOMUL+1vC9xUFv5l2/M=
github.com/envoyproxy/go-control-plane v0.13.4/go.mod h1:kDfuBlDVsSj2MjrLEtRWtHlsWIFcGyB2RMO44Dc5GZA=
github.com/envoyproxy/go-control-plane/envoy v1.32.4 h1:jb83lalDRZSpPWW2Z7Mck/8kXZ5CQAFYVjQcdVIr83A=
github.com/envoyproxy/go-control-plane/envoy v1.32.4/go.mod h1:Gzjc5k8JcJswLjAx1Zm+wSYE20UrLtt7JZMWiWQXQEw=
github.com/envoyproxy/go-control-plane/ratelimit v0.1.0 h1:/G9QYbddjL25KvtKTv3an9lx6VBE2cnb8wp1vEGNYGI=
github.com/envoyproxy/go-control-plane/ratelimit v0.1.0/go.mod h1:Wk+tMFAFbCXaJPzVVHnPgRKdUdwW/KdbRt94AzgRee4=
github.com/envoyproxy/protoc-gen-validate v0.1.0/go.mod h1:iSmxcyjqTsJpI2R4NaDN7+kN2VEUnK/pcBlmesArF7c=
github.com/envoyproxy/protoc-gen-validate v0.6.7/go.mod h1:dyJXwwfPK2VSqiB9Klm1J6romD608Ba7Hij42vrOBCo=
github.com/envoyproxy/protoc-gen-validate v0.9.1/go.mod h1:OKNgG7TCp5pF4d6XftA0++PMirau2/yoOwVac3AbF2w=
github.com/envoyproxy/protoc-gen-validate v0.10.1/go.mod h1:DRjgyB0I43LtJapqN6NiRwroiAU2PaFuvk/vjgh61ss=
github.com/envoyproxy/protoc-gen-validate v1.2.1 h1:DEo3O99U8j4hBFwbJfrz9VtgcDfUKS7KJ7spH3d86P8=
github.com/envoyproxy/protoc-gen-validate v1.2.1/go.mod h1:d/C80l/jxXLdfEIhX1W2TmLfsJ31lvEjwamM4DxlWXU=
github.com/felixge/httpsnoop v1.0.4 h1:NFTV2Zj1bL4mc9sqWACXbQFVBBg2W3GPvqp8/ESS2Wg=
github.com/felixge/httpsnoop v1.0.4/go.mod h1:m8KPJKqk1gH5J9DgRY2ASl2lWCfGKXixSwevea8zH2U=
github.com/fogleman/gg v1.2.1-0.20190220221249-0403632d5b90/go.mod h1:R/bRT+9gY/C5z7JzPU0zXsXHKM4/ayA+zqcVNZzPa1k=
github.com/fogleman/gg v1.3.0/go.mod h1:R/bRT+9gY/C5z7JzPU0zXsXHKM4/ayA+zqcVNZzPa1k=
github.com/form3tech-oss/jwt-go v3.2.5+incompatible h1:/l4kBbb4/vGSsdtB5nUe8L7B9mImVMaBPw9L/0TBHU8=
github.com/form3tech-oss/jwt-go v3.2.5+incompatible/go.mod h1:pbq4aXjuKjdthFRnoDwaVPLA+WlJuPGy+QneDUgJi2k=
github.com/fsnotify/fsnotify v1.4.7/go.mod h1:jwhsz4b93w/PPRr/qN1Yymfu8t87LnFCMoQvtojpjFo=
github.com/fsnotify/fsnotify v1.4.9 h1:hsms1Qyu0jgnwNXIxa+/V/PDsU6CfLf6CNO8H7IWoS4=
github.com/fsnotify/fsnotify v1.4.9/go.mod h1:znqG4EE+3YCdAaPaxE2ZRY/06pZUdp0tY4IgpuI1SZQ=
github.com/fsouza/fake-gcs-server v1.17.0 h1:OeH75kBZcZa3ZE+zz/mFdJ2btt9FgqfjI7gIh9+5fvk=
github.com/fsouza/fake-gcs-server v1.17.0/go.mod h1:D1rTE4YCyHFNa99oyJJ5HyclvN/0uQR+pM/VdlL83bw=
github.com/gabriel-vasile/mimetype v1.4.1 h1:TRWk7se+TOjCYgRth7+1/OYLNiRNIotknkFtf/dnN7Q=
github.com/gabriel-vasile/mimetype v1.4.1/go.mod h1:05Vi0w3Y9c/lNvJOdmIwvrrAhX3rYhfQQCaf9VJcv7M=
github.com/ghodss/yaml v1.0.0/go.mod h1:4dBDuWmgqj2HViK6kFavaiC9ZROes6MMH2rRYeMEF04=
github.com/go-fonts/dejavu v0.1.0/go.mod h1:4Wt4I4OU2Nq9asgDCteaAaWZOV24E+0/Pwo0gppep4g=
github.com/go-fonts/latin-modern v0.2.0/go.mod h1:rQVLdDMK+mK1xscDwsqM5J8U2jrRa3T0ecnM9pNujks=
github.com/go-fonts/liberation v0.1.1/go.mod h1:K6qoJYypsmfVjWg8KOVDQhLc8UDgIK2HYqyqAO9z7GY=
github.com/go-fonts/liberation v0.2.0/go.mod h1:K6qoJYypsmfVjWg8KOVDQhLc8UDgIK2HYqyqAO9z7GY=
github.com/go-fonts/stix v0.1.0/go.mod h1:w/c1f0ldAUlJmLBvlbkvVXLAD+tAMqobIIQpmnUIzUY=
github.com/go-gl/glfw v0.0.0-20190409004039-e6da0acd62b1/go.mod h1:vR7hzQXu2zJy9AVAgeJqvqgH9Q5CA+iKCZ2gyEVpxRU=
github.com/go-gl/glfw/v3.3/glfw v0.0.0-20191125211704-12ad95a8df72/go.mod h1:tQ2UAYgL5IevRw8kRxooKSPJfGvJ9fJQFa0TUsXzTg8=
github.com/go-gl/glfw/v3.3/glfw v0.0.0-20200222043503-6f7a984d4dc4/go.mod h1:tQ2UAYgL5IevRw8kRxooKSPJfGvJ9fJQFa0TUsXzTg8=
github.com/go-jose/go-jose/v4 v4.0.5 h1:M6T8+mKZl/+fNNuFHvGIzDz7BTLQPIounk/b9dw3AaE=
github.com/go-jose/go-jose/v4 v4.0.5/go.mod h1:s3P1lRrkT8igV8D9OjyL4WRyHvjB6a4JSllnOrmmBOA=
github.com/go-kit/log v0.1.0/go.mod h1:zbhenjAZHb184qTLMA9ZjW7ThYL0H2mk7Q6pNt4vbaY=
github.com/go-latex/latex v0.0.0-20210118124228-b3d85cf34e07/go.mod h1:CO1AlKB2CSIqUrmQPqA0gdRIlnLEY0gK5JGjh37zN5U=
github.com/go-latex/latex v0.0.0-20210823091927-c0d11ff05a81/go.mod h1:SX0U8uGpxhq9o2S/CELCSUxEWWAuoCUcVCQWv7G2OCk=
github.com/go-logfmt/logfmt v0.5.0/go.mod h1:wCYkCAKZfumFQihp8CzCvQ3paCTfi41vtzG1KdI/P7A=
github.com/go-logr/logr v1.2.2/go.mod h1:jdQByPbusPIv2/zmleS9BjJVeZ6kBagPoEUsqbVz/1A=
github.com/go-logr/logr v1.4.3 h1:CjnDlHq8ikf6E492q6eKboGOC0T8CDaOvkHCIg8idEI=
github.com/go-logr/logr v1.4.3/go.mod h1:9T104GzyrTigFIr8wt5mBrctHMim0Nb2HLGrmQ40KvY=
github.com/go-logr/stdr v1.2.2 h1:hSWxHoqTgW2S2qGc0LTAI563KZ5YKYRhT3MFKZMbjag=
github.com/go-logr/stdr v1.2.2/go.mod h1:mMo/vtBO5dYbehREoey6XUKy/eSumjCCveDpRre4VKE=
github.com/go-pdf/fpdf v0.5.0/go.mod h1:HzcnA+A23uwogo0tp9yU+l3V+KXhiESpt1PMayhOh5M=
github.com/go-pdf/fpdf v0.6.0/go.mod h1:HzcnA+A23uwogo0tp9yU+l3V+KXhiESpt1PMayhOh5M=
github.com/go-sql-driver/mysql v1.4.0/go.mod h1:zAC/RDZ24gD3HViQzih4MyKcchzm+sOG5ZlKdlhCg5w=
github.com/go-sql-driver/mysql v1.5.0 h1:ozyZYNQW3x3HtqT1jira07DN2PArx2v7/mN66gGcHOs=
github.com/go-sql-driver/mysql v1.5.0/go.mod h1:DCzpHaOWr8IXmIStZouvnhqoel9Qv2LBy8hT2VhHyBg=
github.com/go-stack/stack v1.8.0 h1:5SgMzNM5HxrEjV0ww2lTmX6E2Izsfxas4+YHWRs3Lsk=
github.com/go-stack/stack v1.8.0/go.mod h1:v0f6uXyyMGvRgIKkXu+yp6POWl0qKG85gN/melR3HDY=
github.com/go-task/slim-sprig v0.0.0-20210107165309-348f09dbbbc0/go.mod h1:fyg7847qk6SyHyPtNmDHnmrv/HOrqktSC+C9fM+CJOE=
github.com/gobuffalo/here v0.6.0 h1:hYrd0a6gDmWxBM4TnrGw8mQg24iSVoIkHEk7FodQcBI=
github.com/gobuffalo/here v0.6.0/go.mod h1:wAG085dHOYqUpf+Ap+WOdrPTp5IYcDAs/x7PLa8Y5fM=
github.com/goccy/go-json v0.9.11 h1:/pAaQDLHEoCq/5FFmSKBswWmK6H0e8g4159Kc/X/nqk=
github.com/goccy/go-json v0.9.11/go.mod h1:6MelG93GURQebXPDq3khkgXZkazVtN9CRI+MGFi0w8I=
github.com/gocql/gocql v0.0.0-20210515062232-b7ef815b4556 h1:N/MD/sr6o61X+iZBAT2qEUF023s4KbA8RWfKzl0L6MQ=
github.com/gocql/gocql v0.0.0-20210515062232-b7ef815b4556/go.mod h1:DL0ekTmBSTdlNF25Orwt/JMzqIq3EJ4MVa/J/uK64OY=
github.com/godbus/dbus v0.0.0-20190726142602-4481cbc300e2 h1:ZpnhV/YsD2/4cESfV5+Hoeu/iUR3ruzNvZ+yQfO03a0=
github.com/godbus/dbus v0.0.0-20190726142602-4481cbc300e2/go.mod h1:bBOAhwG1umN6/6ZUMtDFBMQR8jRg9O75tm9K00oMsK4=
github.com/gofrs/uuid v3.2.0+incompatible/go.mod h1:b2aQJv3Z4Fp6yNu3cdSllBxTCLRxnplIgP/c0N/04lM=
github.com/gofrs/uuid v4.0.0+incompatible h1:1SD/1F5pU8p29ybwgQSwpQk+mwdRrXCYuPhW6m+TnJw=
github.com/gofrs/uuid v4.0.0+incompatible/go.mod h1:b2aQJv3Z4Fp6yNu3cdSllBxTCLRxnplIgP/c0N/04lM=
github.com/gogo/protobuf v1.3.2 h1:Ov1cvc58UF3b5XjBnZv7+opcTcQFZebYjWzi34vdm4Q=
github.com/gogo/protobuf v1.3.2/go.mod h1:P1XiOD3dCwIKUDQYPy72D8LYyHL2YPYrpS2s69NZV8Q=
github.com/golang-jwt/jwt/v4 v4.0.0/go.mod h1:/xlHOz8bRuivTWchD4jCa+NbatV+wEUSzwAxVc6locg=
github.com/golang-jwt/jwt/v4 v4.4.2/go.mod h1:m21LjoU+eqJr34lmDMbreY2eSTRJ1cv77w39/MY0Ch0=
github.com/golang-jwt/jwt/v4 v4.5.2 h1:YtQM7lnr8iZ+j5q71MGKkNw9Mn7AjHM68uc9g5fXeUI=
github.com/golang-jwt/jwt/v4 v4.5.2/go.mod h1:m21LjoU+eqJr34lmDMbreY2eSTRJ1cv77w39/MY0Ch0=
github.com/golang-sql/civil v0.0.0-20190719163853-cb61b32ac6fe h1:lXe2qZdvpiX5WZkZR4hgp4KJVfY3nMkvmwbVkpv1rVY=
github.com/golang-sql/civil v0.0.0-20190719163853-cb61b32ac6fe/go.mod h1:8vg3r2VgvsThLBIFL93Qb5yWzgyZWhEmBwUJWevAkK0=
github.com/golang-sql/sqlexp v0.1.0 h1:ZCD6MBpcuOVfGVqsEmY5/4FtYiKz6tSyUv9LPEDei6A=
github.com/golang-sql/sqlexp v0.1.0/go.mod h1:J4ad9Vo8ZCWQ2GMrC4UCQy1JpCbwU9m3EOqtpKwwwHI=
github.com/golang/freetype v0.0.0-20170609003504-e2365dfdc4a0/go.mod h1:E/TSTwGwJL78qG/PmXZO1EjYhfJinVAhrmmHX6Z8B9k=
github.com/golang/glog v0.0.0-20160126235308-23def4e6c14b/go.mod h1:SBH7ygxi8pfUlaOkMMuAQtPIUF8ecWP5IEl/CR7VP2Q=
github.com/golang/glog v1.0.0/go.mod h1:EWib/APOK0SL3dFbYqvxE3UYd8E6s1ouQ7iEp/0LWV4=
github.com/golang/glog v1.1.0/go.mod h1:pfYeQZ3JWZoXTV5sFc986z3HTpwQs9At6P4ImfuP3NQ=
github.com/golang/groupcache v0.0.0-20190702054246-869f871628b6/go.mod h1:cIg4eruTrX1D+g88fzRXU5OdNfaM+9IcxsU14FzY7Hc=
github.com/golang/groupcache v0.0.0-20191227052852-215e87163ea7/go.mod h1:cIg4eruTrX1D+g88fzRXU5OdNfaM+9IcxsU14FzY7Hc=
github.com/golang/groupcache v0.0.0-20200121045136-8c9f03a8e57e/go.mod h1:cIg4eruTrX1D+g88fzRXU5OdNfaM+9IcxsU14FzY7Hc=
github.com/golang/groupcache v0.0.0-20210331224755-41bb18bfe9da h1:oI5xCqsCo564l8iNU+DwB5epxmsaqB+rhGL0m5jtYqE=
github.com/golang/groupcache v0.0.0-20210331224755-41bb18bfe9da/go.mod h1:cIg4eruTrX1D+g88fzRXU5OdNfaM+9IcxsU14FzY7Hc=
github.com/golang/mock v1.1.1/go.mod h1:oTYuIxOrZwtPieC+H1uAHpcLFnEyAGVDL/k47Jfbm0A=
github.com/golang/mock v1.2.0/go.mod h1:oTYuIxOrZwtPieC+H1uAHpcLFnEyAGVDL/k47Jfbm0A=
github.com/golang/mock v1.3.1/go.mod h1:sBzyDLLjw3U8JLTeZvSv8jJB+tU5PVekmnlKIyFUx0Y=
github.com/golang/mock v1.4.0/go.mod h1:UOMv5ysSaYNkG+OFQykRIcU/QvvxJf3p21QfJ2Bt3cw=
github.com/golang/mock v1.4.1/go.mod h1:UOMv5ysSaYNkG+OFQykRIcU/QvvxJf3p21QfJ2Bt3cw=
github.com/golang/mock v1.4.3/go.mod h1:UOMv5ysSaYNkG+OFQykRIcU/QvvxJf3p21QfJ2Bt3cw=
github.com/golang/mock v1.4.4/go.mod h1:l3mdAwkq5BuhzHwde/uurv3sEJeZMXNpwsxVWU71h+4=
github.com/golang/mock v1.5.0/go.mod h1:CWnOUgYIOo4TcNZ0wHX3YZCqsaM1I1Jvs6v3mP3KVu8=
github.com/golang/mock v1.6.0/go.mod h1:p6yTPP+5HYm5mzsMV8JkE6ZKdX+/wYM6Hr+LicevLPs=
github.com/golang/mock v1.7.0-rc.1 h1:YojYx61/OLFsiv6Rw1Z96LpldJIy31o+UHmwAUMJ6/U=
github.com/golang/mock v1.7.0-rc.1/go.mod h1:s42URUywIqd+OcERslBJvOjepvNymP31m3q8d/GkuRs=
github.com/golang/protobuf v1.0.0/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.2.0/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.3.1/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.3.2/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.3.3/go.mod h1:vzj43D7+SQXF/4pzW/hwtAqwc6iTitCiVSaWz5lYuqw=
github.com/golang/protobuf v1.3.4/go.mod h1:vzj43D7+SQXF/4pzW/hwtAqwc6iTitCiVSaWz5lYuqw=
github.com/golang/protobuf v1.3.5/go.mod h1:6O5/vntMXwX2lRkT1hjjk0nAC1IDOTvTlVgjlRvqsdk=
github.com/golang/protobuf v1.4.0-rc.1/go.mod h1:ceaxUfeHdC40wWswd/P6IGgMaK3YpKi5j83Wpe3EHw8=
github.com/golang/protobuf v1.4.0-rc.1.0.20200221234624-67d41d38c208/go.mod h1:xKAWHe0F5eneWXFV3EuXVDTCmh+JuBKY0li0aMyXATA=
github.com/golang/protobuf v1.4.0-rc.2/go.mod h1:LlEzMj4AhA7rCAGe4KMBDvJI+AwstrUpVNzEA03Pprs=
github.com/golang/protobuf v1.4.0-rc.4.0.20200313231945-b860323f09d0/go.mod h1:WU3c8KckQ9AFe+yFwt9sWVRKCVIyN9cPHBJSNnbL67w=
github.com/golang/protobuf v1.4.0/go.mod h1:jodUvKwWbYaEsadDk5Fwe5c77LiNKVO9IDvqG2KuDX0=
github.com/golang/protobuf v1.4.1/go.mod h1:U8fpvMrcmy5pZrNK1lt4xCsGvpyWQ/VVv6QDs8UjoX8=
github.com/golang/protobuf v1.4.2/go.mod h1:oDoupMAO8OvCJWAcko0GGGIgR6R6ocIYbsSw735rRwI=
github.com/golang/protobuf v1.4.3/go.mod h1:oDoupMAO8OvCJWAcko0GGGIgR6R6ocIYbsSw735rRwI=
github.com/golang/protobuf v1.5.0/go.mod h1:FsONVRAS9T7sI+LIUmWTfcYkHO4aIWwzhcaSAoJOfIk=
github.com/golang/protobuf v1.5.1/go.mod h1:DopwsBzvsk0Fs44TXzsVbJyPhcCPeIwnvohx4u74HPM=
github.com/golang/protobuf v1.5.2/go.mod h1:XVQd3VNwM+JqD3oG2Ue2ip4fOMUkwXdXDdiuN0vRsmY=
github.com/golang/protobuf v1.5.3/go.mod h1:XVQd3VNwM+JqD3oG2Ue2ip4fOMUkwXdXDdiuN0vRsmY=
github.com/golang/protobuf v1.5.4 h1:i7eJL8qZTpSEXOPTxNKhASYpMn+8e5Q6AdndVa1dWek=
github.com/golang/protobuf v1.5.4/go.mod h1:lnTiLA8Wa4RWRcIUkrtSVa5nRhsEGBg48fD6rSs7xps=
github.com/golang/snappy v0.0.0-20170215233205-553a64147049/go.mod h1:/XxbfmMg8lxefKM7IXC3fBNl/7bRcc72aCRzEWrmP2Q=
github.com/golang/snappy v0.0.1/go.mod h1:/XxbfmMg8lxefKM7IXC3fBNl/7bRcc72aCRzEWrmP2Q=
github.com/golang/snappy v0.0.3/go.mod h1:/XxbfmMg8lxefKM7IXC3fBNl/7bRcc72aCRzEWrmP2Q=
github.com/golang/snappy v0.0.4 h1:yAGX7huGHXlcLOEtBnF4w7FQwA26wojNCwOYAEhLjQM=
github.com/golang/snappy v0.0.4/go.mod h1:/XxbfmMg8lxefKM7IXC3fBNl/7bRcc72aCRzEWrmP2Q=
github.com/google/btree v0.0.0-20180813153112-4030bb1f1f0c/go.mod h1:lNA+9X1NB3Zf8V7Ke586lFgjr2dZNuvo3lPJSGZ5JPQ=
github.com/google/btree v1.0.0/go.mod h1:lNA+9X1NB3Zf8V7Ke586lFgjr2dZNuvo3lPJSGZ5JPQ=
github.com/google/flatbuffers v2.0.8+incompatible h1:ivUb1cGomAB101ZM1T0nOiWz9pSrTMoa9+EiY7igmkM=
github.com/google/flatbuffers v2.0.8+incompatible/go.mod h1:1AeVuKshWv4vARoZatz6mlQ0JxURH0Kv5+zNeJKJCa8=
github.com/google/go-cmp v0.2.0/go.mod h1:oXzfMopK8JAjlY9xF4vHSVASa0yLyX7SntLO5aqRK0M=
github.com/google/go-cmp v0.3.0/go.mod h1:8QqcDgzrUqlUb/G2PQTWiueGozuR1884gddMywk6iLU=
github.com/google/go-cmp v0.3.1/go.mod h1:8QqcDgzrUqlUb/G2PQTWiueGozuR1884gddMywk6iLU=
github.com/google/go-cmp v0.4.0/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.4.1/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.0/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.1/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.2/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.3/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.4/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.5/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.6/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.7/go.mod h1:n+brtR0CgQNWTVd5ZUFpTBC8YFBDLK/h/bpaJ8/DtOE=
github.com/google/go-cmp v0.5.8/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/google/go-cmp v0.5.9/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/google/go-cmp v0.7.0 h1:wk8382ETsv4JYUZwIsn6YpYiWiBsYLSJiTsyBybVuN8=
github.com/google/go-cmp v0.7.0/go.mod h1:pXiqmnSA92OHEEa9HXL2W4E7lf9JzCmGVUdgjX3N/iU=
github.com/google/go-github/v39 v39.2.0 h1:rNNM311XtPOz5rDdsJXAp2o8F67X9FnROXTvto3aSnQ=
github.com/google/go-github/v39 v39.2.0/go.mod h1:C1s8C5aCC9L+JXIYpJM5GYytdX52vC1bLvHEF1IhBrE=
github.com/google/go-querystring v1.0.0/go.mod h1:odCYkC5MyYFN7vkCjXpyrEuKhc/BUO6wN/zVPAxq5ck=
github.com/google/go-querystring v1.1.0 h1:AnCroh3fv4ZBgVIf1Iwtovgjaw/GiKJo8M8yD/fhyJ8=
github.com/google/go-querystring v1.1.0/go.mod h1:Kcdr2DB4koayq7X8pmAG4sNG59So17icRSOU623lUBU=
github.com/google/martian v2.1.0+incompatible h1:/CP5g8u/VJHijgedC/Legn3BAbAaWPgecwXBIDzw5no=
github.com/google/martian v2.1.0+incompatible/go.mod h1:9I4somxYTbIHy5NJKHRl3wXiIaQGbYVAs8BPL6v8lEs=
github.com/google/martian/v3 v3.0.0/go.mod h1:y5Zk1BBys9G+gd6Jrk0W3cC1+ELVxBWuIGO+w/tUAp0=
github.com/google/martian/v3 v3.1.0/go.mod h1:y5Zk1BBys9G+gd6Jrk0W3cC1+ELVxBWuIGO+w/tUAp0=
github.com/google/martian/v3 v3.2.1/go.mod h1:oBOf6HBosgwRXnUGWUB05QECsc6uvmMiJ3+6W4l/CUk=
github.com/google/martian/v3 v3.3.2/go.mod h1:oBOf6HBosgwRXnUGWUB05QECsc6uvmMiJ3+6W4l/CUk=
github.com/google/martian/v3 v3.3.3 h1:DIhPTQrbPkgs2yJYdXU/eNACCG5DVQjySNRNlflZ9Fc=
github.com/google/martian/v3 v3.3.3/go.mod h1:iEPrYcgCF7jA9OtScMFQyAlZZ4YXTKEtJ1E6RWzmBA0=
github.com/google/pprof v0.0.0-20181206194817-3ea8567a2e57/go.mod h1:zfwlbNMJ+OItoe0UupaVj+oy1omPYYDuagoSzA8v9mc=
github.com/google/pprof v0.0.0-20190515194954-54271f7e092f/go.mod h1:zfwlbNMJ+OItoe0UupaVj+oy1omPYYDuagoSzA8v9mc=
github.com/google/pprof v0.0.0-20191218002539-d4f498aebedc/go.mod h1:ZgVRPoUq/hfqzAqh7sHMqb3I9Rq5C59dIz2SbBwJ4eM=
github.com/google/pprof v0.0.0-20200212024743-f11f1df84d12/go.mod h1:ZgVRPoUq/hfqzAqh7sHMqb3I9Rq5C59dIz2SbBwJ4eM=
github.com/google/pprof v0.0.0-20200229191704-1ebb73c60ed3/go.mod h1:ZgVRPoUq/hfqzAqh7sHMqb3I9Rq5C59dIz2SbBwJ4eM=
github.com/google/pprof v0.0.0-20200430221834-fc25d7d30c6d/go.mod h1:ZgVRPoUq/hfqzAqh7sHMqb3I9Rq5C59dIz2SbBwJ4eM=
github.com/google/pprof v0.0.0-20200708004538-1a94d8640e99/go.mod h1:ZgVRPoUq/hfqzAqh7sHMqb3I9Rq5C59dIz2SbBwJ4eM=
github.com/google/pprof v0.0.0-20201023163331-3e6fc7fc9c4c/go.mod h1:kpwsk12EmLew5upagYY7GY0pfYCcupk39gWOCRROcvE=
github.com/google/pprof v0.0.0-20201203190320-1bf35d6f28c2/go.mod h1:kpwsk12EmLew5upagYY7GY0pfYCcupk39gWOCRROcvE=
github.com/google/pprof v0.0.0-20201218002935-b9804c9f04c2/go.mod h1:kpwsk12EmLew5upagYY7GY0pfYCcupk39gWOCRROcvE=
github.com/google/pprof v0.0.0-20210122040257-d980be63207e/go.mod h1:kpwsk12EmLew5upagYY7GY0pfYCcupk39gWOCRROcvE=
github.com/google/pprof v0.0.0-20210226084205-cbba55b83ad5/go.mod h1:kpwsk12EmLew5upagYY7GY0pfYCcupk39gWOCRROcvE=
github.com/google/pprof v0.0.0-20210601050228-01bbb1931b22/go.mod h1:kpwsk12EmLew5upagYY7GY0pfYCcupk39gWOCRROcvE=
github.com/google/pprof v0.0.0-20210609004039-a478d1d731e9/go.mod h1:kpwsk12EmLew5upagYY7GY0pfYCcupk39gWOCRROcvE=
github.com/google/pprof v0.0.0-20210720184732-4bb14d4b1be1/go.mod h1:kpwsk12EmLew5upagYY7GY0pfYCcupk39gWOCRROcvE=
github.com/google/renameio v0.1.0/go.mod h1:KWCgfxg9yswjAJkECMjeO8J8rahYeXnNhOm40UhjYkI=
github.com/google/s2a-go v0.1.9 h1:LGD7gtMgezd8a/Xak7mEWL0PjoTQFvpRudN895yqKW0=
github.com/google/s2a-go v0.1.9/go.mod h1:YA0Ei2ZQL3acow2O62kdp9UlnvMmU7kA6Eutn0dXayM=
github.com/google/uuid v1.1.1/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/google/uuid v1.1.2/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/google/uuid v1.3.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/google/uuid v1.6.0 h1:NIvaJDMOsjHA8n1jAhLSgzrAzy1Hgr+hNrb57e+94F0=
github.com/google/uuid v1.6.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/googleapis/enterprise-certificate-proxy v0.0.0-20220520183353-fd19c99a87aa/go.mod h1:17drOmN3MwGY7t0e+Ei9b45FFGA3fBs3x36SsCg1hq8=
github.com/googleapis/enterprise-certificate-proxy v0.1.0/go.mod h1:17drOmN3MwGY7t0e+Ei9b45FFGA3fBs3x36SsCg1hq8=
github.com/googleapis/enterprise-certificate-proxy v0.2.0/go.mod h1:8C0jb7/mgJe/9KK8Lm7X9ctZC2t60YyIpYEI16jx0Qg=
github.com/googleapis/enterprise-certificate-proxy v0.2.1/go.mod h1:AwSRAtLfXpU5Nm3pW+v7rGDHp09LsPtGY9MduiEsR9k=
github.com/googleapis/enterprise-certificate-proxy v0.2.3/go.mod h1:AwSRAtLfXpU5Nm3pW+v7rGDHp09LsPtGY9MduiEsR9k=
github.com/googleapis/enterprise-certificate-proxy v0.3.6 h1:GW/XbdyBFQ8Qe+YAmFU9uHLo7OnF5tL52HFAgMmyrf4=
github.com/googleapis/enterprise-certificate-proxy v0.3.6/go.mod h1:MkHOF77EYAE7qfSuSS9PU6g4Nt4e11cnsDUowfwewLA=
github.com/googleapis/gax-go/v2 v2.0.4/go.mod h1:0Wqv26UfaUD9n4G6kQubkQ+KchISgw+vpHVxEJEs9eg=
github.com/googleapis/gax-go/v2 v2.0.5/go.mod h1:DWXyrwAJ9X0FpwwEdw+IPEYBICEFu5mhpdKc/us6bOk=
github.com/googleapis/gax-go/v2 v2.1.0/go.mod h1:Q3nei7sK6ybPYH7twZdmQpAd1MKb7pfu6SK+H1/DsU0=
github.com/googleapis/gax-go/v2 v2.1.1/go.mod h1:hddJymUZASv3XPyGkUpKj8pPO47Rmb0eJc8R6ouapiM=
github.com/googleapis/gax-go/v2 v2.2.0/go.mod h1:as02EH8zWkzwUoLbBaFeQ+arQaj/OthfcblKl4IGNaM=
github.com/googleapis/gax-go/v2 v2.3.0/go.mod h1:b8LNqSzNabLiUpXKkY7HAR5jr6bIT99EXz9pXxye9YM=
github.com/googleapis/gax-go/v2 v2.4.0/go.mod h1:XOTVJ59hdnfJLIP/dh8n5CGryZR2LxK9wbMD5+iXC6c=
github.com/googleapis/gax-go/v2 v2.5.1/go.mod h1:h6B0KMMFNtI2ddbGJn3T3ZbwkeT6yqEF02fYlzkUCyo=
github.com/googleapis/gax-go/v2 v2.6.0/go.mod h1:1mjbznJAPHFpesgE5ucqfYEscaz5kMdcIDwU/6+DDoY=
github.com/googleapis/gax-go/v2 v2.7.0/go.mod h1:TEop28CZZQ2y+c0VxMUmu1lV+fQx57QpBWsYpwqHJx8=
github.com/googleapis/gax-go/v2 v2.7.1/go.mod h1:4orTrqY6hXxxaUL4LHIPl6lGo8vAE38/qKbhSAKP6QI=
github.com/googleapis/gax-go/v2 v2.15.0 h1:SyjDc1mGgZU5LncH8gimWo9lW1DtIfPibOG81vgd/bo=
github.com/googleapis/gax-go/v2 v2.15.0/go.mod h1:zVVkkxAQHa1RQpg9z2AUCMnKhi0Qld9rcmyfL1OZhoc=
github.com/googleapis/go-type-adapters v1.0.0/go.mod h1:zHW75FOG2aur7gAO2B+MLby+cLsWGBF62rFAi7WjWO4=
github.com/googleapis/google-cloud-go-testing v0.0.0-20200911160855-bcd43fbb19e8/go.mod h1:dvDLG8qkwmyD9a/MJJN3XJcT3xFxOKAvTZGvuZmac9g=
github.com/gorilla/handlers v1.4.2 h1:0QniY0USkHQ1RGCLfKxeNHK9bkDHGRYGNDFBCS+YARg=
github.com/gorilla/handlers v1.4.2/go.mod h1:Qkdc/uu4tH4g6mTK6auzZ766c4CA0Ng8+o/OAirnOIQ=
github.com/gorilla/mux v1.7.3/go.mod h1:1lud6UwP+6orDFRuTfBEV8e9/aOM/c4fVVCaMa2zaAs=
github.com/gorilla/mux v1.7.4 h1:VuZ8uybHlWmqV03+zRzdwKL4tUnIp1MAQtp1mIFE1bc=
github.com/gorilla/mux v1.7.4/go.mod h1:DVbg23sWSpFRCP0SfiEN6jmj59UnW/n46BH5rLB71So=
github.com/gorilla/securecookie v1.1.1/go.mod h1:ra0sb63/xPlUeL+yeDciTfxMRAA+MP+HVt/4epWDjd4=
github.com/gorilla/sessions v1.2.1/go.mod h1:dk2InVEVJ0sfLlnXv9EAgkf6ecYs/i80K/zI+bUmuGM=
github.com/grpc-ecosystem/grpc-gateway v1.16.0 h1:gmcG1KaJ57LophUzW0Hy8NmPhnMZb4M0+kPpLofRdBo=
github.com/grpc-ecosystem/grpc-gateway v1.16.0/go.mod h1:BDjrQk3hbvj6Nolgz8mAMFbcEtjT1g+wF4CSlocrBnw=
github.com/grpc-ecosystem/grpc-gateway/v2 v2.7.0/go.mod h1:hgWBS7lorOAVIJEQMi4ZsPv9hVvWI6+ch50m39Pf2Ks=
github.com/grpc-ecosystem/grpc-gateway/v2 v2.11.3/go.mod h1:o//XUCC/F+yRGJoPO/VU0GSB0f8Nhgmxx0VIRUvaC0w=
github.com/grpc-ecosystem/grpc-gateway/v2 v2.20.0 h1:bkypFPDjIYGfCYD5mRBvpqxfYX1YCS1PXdKYWi8FsN0=
github.com/grpc-ecosystem/grpc-gateway/v2 v2.20.0/go.mod h1:P+Lt/0by1T8bfcF3z737NnSbmxQAppXMRziHUxPOC8k=
github.com/gsterjov/go-libsecret v0.0.0-20161001094733-a6f4afe4910c h1:6rhixN/i8ZofjG1Y75iExal34USq5p+wiN1tpie8IrU=
github.com/gsterjov/go-libsecret v0.0.0-20161001094733-a6f4afe4910c/go.mod h1:NMPJylDgVpX0MLRlPy15sqSwOFv/U1GZ2m21JhFfek0=
github.com/hailocab/go-hostpool v0.0.0-20160125115350-e80d13ce29ed h1:5upAirOpQc1Q53c0bnx2ufif5kANL7bfZWcc6VJWJd8=
github.com/hailocab/go-hostpool v0.0.0-20160125115350-e80d13ce29ed/go.mod h1:tMWxXQ9wFIaZeTI9F+hmhFiGpFmhOHzyShyFUhRm0H4=
github.com/hashicorp/go-uuid v1.0.2/go.mod h1:6SBZvOh/SIDV7/2o3Jml5SYk/TvGqwFJ/bN7x4byOro=
github.com/hashicorp/golang-lru v0.5.0/go.mod h1:/m3WP610KZHVQ1SGc6re/UDhFvYD7pJ4Ao+sR/qLZy8=
github.com/hashicorp/golang-lru v0.5.1/go.mod h1:/m3WP610KZHVQ1SGc6re/UDhFvYD7pJ4Ao+sR/qLZy8=
github.com/hpcloud/tail v1.0.0/go.mod h1:ab1qPbhIpdTxEkNHXyeSf5vhxWSCs/tWer42PpOxQnU=
github.com/iancoleman/strcase v0.2.0/go.mod h1:iwCmte+B7n89clKwxIoIXy/HfoL7AsD47ZCWhYzw7ho=
github.com/ianlancetaylor/demangle v0.0.0-20181102032728-5e5cf60278f6/go.mod h1:aSSvb/t6k1mPoxDqO4vJh6VOCGPwU4O0C2/Eqndh1Sc=
github.com/ianlancetaylor/demangle v0.0.0-20200824232613-28f6c0f3b639/go.mod h1:aSSvb/t6k1mPoxDqO4vJh6VOCGPwU4O0C2/Eqndh1Sc=
github.com/jackc/chunkreader v1.0.0/go.mod h1:RT6O25fNZIuasFJRyZ4R/Y2BbhasbmZXF9QQ7T3kePo=
github.com/jackc/chunkreader/v2 v2.0.0/go.mod h1:odVSm741yZoC3dpHEUXIqA9tQRhFrgOHwnPIn9lDKlk=
github.com/jackc/chunkreader/v2 v2.0.1 h1:i+RDz65UE+mmpjTfyz0MoVTnzeYxroil2G82ki7MGG8=
github.com/jackc/chunkreader/v2 v2.0.1/go.mod h1:odVSm741yZoC3dpHEUXIqA9tQRhFrgOHwnPIn9lDKlk=
github.com/jackc/pgconn v0.0.0-20190420214824-7e0022ef6ba3/go.mod h1:jkELnwuX+w9qN5YIfX0fl88Ehu4XC3keFuOJJk9pcnA=
github.com/jackc/pgconn v0.0.0-20190824142844-760dd75542eb/go.mod h1:lLjNuW/+OfW9/pnVKPazfWOgNfH2aPem8YQ7ilXGvJE=
github.com/jackc/pgconn v0.0.0-20190831204454-2fabfa3c18b7/go.mod h1:ZJKsE/KZfsUgOEh9hBm+xYTstcNHg7UPMVJqRfQxq4s=
github.com/jackc/pgconn v1.4.0/go.mod h1:Y2O3ZDF0q4mMacyWV3AstPJpeHXWGEetiFttmq5lahk=
github.com/jackc/pgconn v1.5.0/go.mod h1:QeD3lBfpTFe8WUnPZWN5KY/mB8FGMIYRdd8P8Jr0fAI=
github.com/jackc/pgconn v1.5.1-0.20200601181101-fa742c524853/go.mod h1:QeD3lBfpTFe8WUnPZWN5KY/mB8FGMIYRdd8P8Jr0fAI=
github.com/jackc/pgconn v1.8.0/go.mod h1:1C2Pb36bGIP9QHGBYCjnyhqu7Rv3sGshaQUvmfGIB/o=
github.com/jackc/pgconn v1.9.0/go.mod h1:YctiPyvzfU11JFxoXokUOOKQXQmDMoJL9vJzHH8/2JY=
github.com/jackc/pgconn v1.9.1-0.20210724152538-d89c8390a530/go.mod h1:4z2w8XhRbP1hYxkpTuBjTS3ne3J48K83+u0zoyvg2pI=
github.com/jackc/pgconn v1.14.3 h1:bVoTr12EGANZz66nZPkMInAV/KHD2TxH9npjXXgiB3w=
github.com/jackc/pgconn v1.14.3/go.mod h1:RZbme4uasqzybK2RK5c65VsHxoyaml09lx3tXOcO/VM=
github.com/jackc/pgerrcode v0.0.0-20220416144525-469b46aa5efa h1:s+4MhCQ6YrzisK6hFJUX53drDT4UsSW3DEhKn0ifuHw=
github.com/jackc/pgerrcode v0.0.0-20220416144525-469b46aa5efa/go.mod h1:a/s9Lp5W7n/DD0VrVoyJ00FbP2ytTPDVOivvn2bMlds=
github.com/jackc/pgio v1.0.0 h1:g12B9UwVnzGhueNavwioyEEpAmqMe1E/BN9ES+8ovkE=
github.com/jackc/pgio v1.0.0/go.mod h1:oP+2QK2wFfUWgr+gxjoBH9KGBb31Eio69xUb0w5bYf8=
github.com/jackc/pgmock v0.0.0-20190831213851-13a1b77aafa2/go.mod h1:fGZlG77KXmcq05nJLRkk0+p82V8B8Dw8KN2/V9c/OAE=
github.com/jackc/pgmock v0.0.0-20201204152224-4fe30f7445fd/go.mod h1:hrBW0Enj2AZTNpt/7Y5rr2xe/9Mn757Wtb2xeBzPv2c=
github.com/jackc/pgmock v0.0.0-20210724152146-4ad1a8207f65 h1:DadwsjnMwFjfWc9y5Wi/+Zz7xoE5ALHsRQlOctkOiHc=
github.com/jackc/pgmock v0.0.0-20210724152146-4ad1a8207f65/go.mod h1:5R2h2EEX+qri8jOWMbJCtaPWkrrNc7OHwsp2TCqp7ak=
github.com/jackc/pgpassfile v1.0.0 h1:/6Hmqy13Ss2zCq62VdNG8tM1wchn8zjSGOBJ6icpsIM=
github.com/jackc/pgpassfile v1.0.0/go.mod h1:CEx0iS5ambNFdcRtxPj5JhEz+xB6uRky5eyVu/W2HEg=
github.com/jackc/pgproto3 v1.1.0/go.mod h1:eR5FA3leWg7p9aeAqi37XOTgTIbkABlvcPB3E5rlc78=
github.com/jackc/pgproto3/v2 v2.0.0-alpha1.0.20190420180111-c116219b62db/go.mod h1:bhq50y+xrl9n5mRYyCBFKkpRVTLYJVWeCc+mEAI3yXA=
github.com/jackc/pgproto3/v2 v2.0.0-alpha1.0.20190609003834-432c2951c711/go.mod h1:uH0AWtUmuShn0bcesswc4aBTWGvw0cAxIJp+6OB//Wg=
github.com/jackc/pgproto3/v2 v2.0.0-rc3/go.mod h1:ryONWYqW6dqSg1Lw6vXNMXoBJhpzvWKnT95C46ckYeM=
github.com/jackc/pgproto3/v2 v2.0.0-rc3.0.20190831210041-4c03ce451f29/go.mod h1:ryONWYqW6dqSg1Lw6vXNMXoBJhpzvWKnT95C46ckYeM=
github.com/jackc/pgproto3/v2 v2.0.1/go.mod h1:WfJCnwN3HIg9Ish/j3sgWXnAfK8A9Y0bwXYU5xKaEdA=
github.com/jackc/pgproto3/v2 v2.0.6/go.mod h1:WfJCnwN3HIg9Ish/j3sgWXnAfK8A9Y0bwXYU5xKaEdA=
github.com/jackc/pgproto3/v2 v2.1.1/go.mod h1:WfJCnwN3HIg9Ish/j3sgWXnAfK8A9Y0bwXYU5xKaEdA=
github.com/jackc/pgproto3/v2 v2.3.3 h1:1HLSx5H+tXR9pW3in3zaztoEwQYRC9SQaYUHjTSUOag=
github.com/jackc/pgproto3/v2 v2.3.3/go.mod h1:WfJCnwN3HIg9Ish/j3sgWXnAfK8A9Y0bwXYU5xKaEdA=
github.com/jackc/pgservicefile v0.0.0-20200307190119-3430c5407db8/go.mod h1:vsD4gTJCa9TptPL8sPkXrLZ+hDuNrZCnj29CQpr4X1E=
github.com/jackc/pgservicefile v0.0.0-20200714003250-2b9c44734f2b/go.mod h1:vsD4gTJCa9TptPL8sPkXrLZ+hDuNrZCnj29CQpr4X1E=
github.com/jackc/pgservicefile v0.0.0-20240606120523-5a60cdf6a761 h1:iCEnooe7UlwOQYpKFhBabPMi4aNAfoODPEFNiAnClxo=
github.com/jackc/pgservicefile v0.0.0-20240606120523-5a60cdf6a761/go.mod h1:5TJZWKEWniPve33vlWYSoGYefn3gLQRzjfDlhSJ9ZKM=
github.com/jackc/pgtype v0.0.0-20190421001408-4ed0de4755e0/go.mod h1:hdSHsc1V01CGwFsrv11mJRHWJ6aifDLfdV3aVjFF0zg=
github.com/jackc/pgtype v0.0.0-20190824184912-ab885b375b90/go.mod h1:KcahbBH1nCMSo2DXpzsoWOAfFkdEtEJpPbVLq8eE+mc=
github.com/jackc/pgtype v0.0.0-20190828014616-a8802b16cc59/go.mod h1:MWlu30kVJrUS8lot6TQqcg7mtthZ9T0EoIBFiJcmcyw=
github.com/jackc/pgtype v1.2.0/go.mod h1:5m2OfMh1wTK7x+Fk952IDmI4nw3nPrvtQdM0ZT4WpC0=
github.com/jackc/pgtype v1.3.1-0.20200510190516-8cd94a14c75a/go.mod h1:vaogEUkALtxZMCH411K+tKzNpwzCKU+AnPzBKZ+I+Po=
github.com/jackc/pgtype v1.3.1-0.20200606141011-f6355165a91c/go.mod h1:cvk9Bgu/VzJ9/lxTO5R5sf80p0DiucVtN7ZxvaC4GmQ=
github.com/jackc/pgtype v1.6.2/go.mod h1:JCULISAZBFGrHaOXIIFiyfzW5VY0GRitRr8NeJsrdig=
github.com/jackc/pgtype v1.8.1-0.20210724151600-32e20a603178/go.mod h1:C516IlIV9NKqfsMCXTdChteoXmwgUceqaLfjg2e3NlM=
github.com/jackc/pgtype v1.14.0 h1:y+xUdabmyMkJLyApYuPj38mW+aAIqCe5uuBB51rH3Vw=
github.com/jackc/pgtype v1.14.0/go.mod h1:LUMuVrfsFfdKGLw+AFFVv6KtHOFMwRgDDzBt76IqCA4=
github.com/jackc/pgx/v4 v4.0.0-20190420224344-cc3461e65d96/go.mod h1:mdxmSJJuR08CZQyj1PVQBHy9XOp5p8/SHH6a0psbY9Y=
github.com/jackc/pgx/v4 v4.0.0-20190421002000-1b8f0016e912/go.mod h1:no/Y67Jkk/9WuGR0JG/JseM9irFbnEPbuWV2EELPNuM=
github.com/jackc/pgx/v4 v4.0.0-pre1.0.20190824185557-6972a5742186/go.mod h1:X+GQnOEnf1dqHGpw7JmHqHc1NxDoalibchSk9/RWuDc=
github.com/jackc/pgx/v4 v4.5.0/go.mod h1:EpAKPLdnTorwmPUUsqrPxy5fphV18j9q3wrfRXgo+kA=
github.com/jackc/pgx/v4 v4.6.1-0.20200510190926-94ba730bb1e9/go.mod h1:t3/cdRQl6fOLDxqtlyhe9UWgfIi9R8+8v8GKV5TRA/o=
github.com/jackc/pgx/v4 v4.6.1-0.20200606145419-4e5062306904/go.mod h1:ZDaNWkt9sW1JMiNn0kdYBaLelIhw7Pg4qd+Vk6tw7Hg=
github.com/jackc/pgx/v4 v4.10.1/go.mod h1:QlrWebbs3kqEZPHCTGyxecvzG6tvIsYu+A5b1raylkA=
github.com/jackc/pgx/v4 v4.12.1-0.20210724153913-640aa07df17c/go.mod h1:1QD0+tgSXP7iUjYm9C1NxKhny7lq6ee99u/z+IHFcgs=
github.com/jackc/pgx/v4 v4.18.2 h1:xVpYkNR5pk5bMCZGfClbO962UIqVABcAGt7ha1s/FeU=
github.com/jackc/pgx/v4 v4.18.2/go.mod h1:Ey4Oru5tH5sB6tV7hDmfWFahwF15Eb7DNXlRKx2CkVw=
github.com/jackc/pgx/v5 v5.7.6 h1:rWQc5FwZSPX58r1OQmkuaNicxdmExaEz5A2DO2hUuTk=
github.com/jackc/pgx/v5 v5.7.6/go.mod h1:aruU7o91Tc2q2cFp5h4uP3f6ztExVpyVv88Xl/8Vl8M=
github.com/jackc/puddle v0.0.0-20190413234325-e4ced69a3a2b/go.mod h1:m4B5Dj62Y0fbyuIc15OsIqK0+JU8nkqQjsgx7dvjSWk=
github.com/jackc/puddle v0.0.0-20190608224051-11cab39313c9/go.mod h1:m4B5Dj62Y0fbyuIc15OsIqK0+JU8nkqQjsgx7dvjSWk=
github.com/jackc/puddle v1.1.0/go.mod h1:m4B5Dj62Y0fbyuIc15OsIqK0+JU8nkqQjsgx7dvjSWk=
github.com/jackc/puddle v1.1.1/go.mod h1:m4B5Dj62Y0fbyuIc15OsIqK0+JU8nkqQjsgx7dvjSWk=
github.com/jackc/puddle v1.1.3/go.mod h1:m4B5Dj62Y0fbyuIc15OsIqK0+JU8nkqQjsgx7dvjSWk=
github.com/jackc/puddle/v2 v2.2.2 h1:PR8nw+E/1w0GLuRFSmiioY6UooMp6KJv0/61nB7icHo=
github.com/jackc/puddle/v2 v2.2.2/go.mod h1:vriiEXHvEE654aYKXXjOvZM39qJ0q+azkZFrfEOc3H4=
github.com/jcmturner/aescts/v2 v2.0.0/go.mod h1:AiaICIRyfYg35RUkr8yESTqvSy7csK90qZ5xfvvsoNs=
github.com/jcmturner/dnsutils/v2 v2.0.0/go.mod h1:b0TnjGOvI/n42bZa+hmXL+kFJZsFT7G4t3HTlQ184QM=
github.com/jcmturner/gofork v1.0.0/go.mod h1:MK8+TM0La+2rjBD4jE12Kj1pCCxK7d2LK/UM3ncEo0o=
github.com/jcmturner/goidentity/v6 v6.0.1/go.mod h1:X1YW3bgtvwAXju7V3LCIMpY0Gbxyjn/mY9zx4tFonSg=
github.com/jcmturner/gokrb5/v8 v8.4.2/go.mod h1:sb+Xq/fTY5yktf/VxLsE3wlfPqQjp0aWNYyvBVK62bc=
github.com/jcmturner/rpc/v2 v2.0.3/go.mod h1:VUJYCIDm3PVOEHw8sgt091/20OJjskO/YJki3ELg/Hc=
github.com/jinzhu/inflection v1.0.0/go.mod h1:h+uFLlag+Qp1Va5pdKtLDYj+kHp5pxUVkryuEj+Srlc=
github.com/jinzhu/now v1.1.1/go.mod h1:d3SSVoowX0Lcu0IBviAWJpolVfI5UJVZZ7cO71lE/z8=
github.com/jmespath/go-jmespath v0.4.0 h1:BEgLn5cpjn8UN1mAw4NjwDrS35OdebyEtFe+9YPoQUg=
github.com/jmespath/go-jmespath v0.4.0/go.mod h1:T8mJZnbsbmF+m6zOOFylbeCJqk5+pHWvzYPziyZiYoo=
github.com/jmespath/go-jmespath/internal/testify v1.5.1 h1:shLQSRRSCCPj3f2gpwzGwWFoC7ycTf1rcQZHOlsJ6N8=
github.com/jmespath/go-jmespath/internal/testify v1.5.1/go.mod h1:L3OGu8Wl2/fWfCI6z80xFu9LTZmf1ZRjMHUOPmWr69U=
github.com/jmoiron/sqlx v1.2.0/go.mod h1:1FEQNm3xlJgrMD+FBdI9+xvCksHtbpVBBw5dYhBSsks=
github.com/jmoiron/sqlx v1.3.1/go.mod h1:2BljVx/86SuTyjE+aPYlHCTNvZrnJXghYGpNiXLBMCQ=
github.com/jstemmer/go-junit-report v0.0.0-20190106144839-af01ea7f8024/go.mod h1:6v2b51hI/fHJwM22ozAgKL4VKDeJcHhJFhtBdhmNjmU=
github.com/jstemmer/go-junit-report v0.9.1/go.mod h1:Brl9GWCQeLvo8nXZwPNNblvFj/XSXhF0NWZEnDohbsk=
github.com/jung-kurt/gofpdf v1.0.0/go.mod h1:7Id9E/uU8ce6rXgefFLlgrJj/GYY22cpxn+r32jIOes=
github.com/jung-kurt/gofpdf v1.0.3-0.20190309125859-24315acbbda5/go.mod h1:7Id9E/uU8ce6rXgefFLlgrJj/GYY22cpxn+r32jIOes=
github.com/k0kubun/colorstring v0.0.0-20150214042306-9440f1994b88 h1:uC1QfSlInpQF+M0ao65imhwqKnz3Q2z/d8PWZRMQvDM=
github.com/k0kubun/colorstring v0.0.0-20150214042306-9440f1994b88/go.mod h1:3w7q1U84EfirKl04SVQ/s7nPm1ZPhiXd34z40TNz36k=
github.com/k0kubun/pp v2.3.0+incompatible h1:EKhKbi34VQDWJtq+zpsKSEhkHHs9w2P8Izbq8IhLVSo=
github.com/k0kubun/pp v2.3.0+incompatible/go.mod h1:GWse8YhT0p8pT4ir3ZgBbfZild3tgzSScAn6HmfYukg=
github.com/kardianos/osext v0.0.0-20190222173326-2bc1f35cddc0 h1:iQTw/8FWTuc7uiaSepXwyf3o52HaUYcV+Tu66S3F5GA=
github.com/kardianos/osext v0.0.0-20190222173326-2bc1f35cddc0/go.mod h1:1NbS8ALrpOvjt0rHPNLyCIeMtbizbir8U//inJ+zuB8=
github.com/kballard/go-shellquote v0.0.0-20180428030007-95032a82bc51 h1:Z9n2FFNUXsshfwJMBgNA0RU6/i7WVaAegv3PtuIHPMs=
github.com/kballard/go-shellquote v0.0.0-20180428030007-95032a82bc51/go.mod h1:CzGEWj7cYgsdH8dAjBGEr58BoE7ScuLd+fwFZ44+/x8=
github.com/kisielk/errcheck v1.5.0/go.mod h1:pFxgyoBC7bSaBwPgfKdkLd5X25qrDl4LWUI2bnpBCr8=
github.com/kisielk/gotool v1.0.0/go.mod h1:XhKaO+MFFWcvkIS/tQcRk01m1F5IRFswLeQ+oQHNcck=
github.com/klauspost/asmfmt v1.3.2 h1:4Ri7ox3EwapiOjCki+hw14RyKk201CN4rzyCJRFLpK4=
github.com/klauspost/asmfmt v1.3.2/go.mod h1:AG8TuvYojzulgDAMCnYn50l/5QV3Bs/tp6j0HLHbNSE=
github.com/klauspost/compress v1.13.6/go.mod h1:/3/Vjq9QcHkK5uEr5lBEmyoZ1iFhe47etQ6QUkpK6sk=
github.com/klauspost/compress v1.15.9/go.mod h1:PhcZ0MbTNciWF3rruxRgKxI5NkcHHrHUDtV4Yw2GlzU=
github.com/klauspost/compress v1.15.11 h1:Lcadnb3RKGin4FYM/orgq0qde+nc15E5Cbqg4B9Sx9c=
github.com/klauspost/compress v1.15.11/go.mod h1:QPwzmACJjUTFsnSHH934V6woptycfrDDJnH7hvFVbGM=
github.com/klauspost/cpuid/v2 v2.0.9 h1:lgaqFMSdTdQYdZ04uHyN2d/eKdOMyi2YLSvlQIBFYa4=
github.com/klauspost/cpuid/v2 v2.0.9/go.mod h1:FInQzS24/EEf25PyTYn52gqo7WaD8xa0213Md/qVLRg=
github.com/konsorten/go-windows-terminal-sequences v1.0.1/go.mod h1:T0+1ngSBFLxvqU3pZ+m/2kptfBszLMUkC4ZK/EgS/cQ=
github.com/konsorten/go-windows-terminal-sequences v1.0.2/go.mod h1:T0+1ngSBFLxvqU3pZ+m/2kptfBszLMUkC4ZK/EgS/cQ=
github.com/kr/fs v0.1.0/go.mod h1:FFnZGqtBN9Gxj7eW1uZ42v5BccTP0vu6NEaFoC2HwRg=
github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
github.com/kr/pretty v0.2.1/go.mod h1:ipq/a2n7PKx3OHsz4KJII5eveXtPO4qwEXGdVfWzfnI=
github.com/kr/pretty v0.3.0/go.mod h1:640gp4NfQd8pI5XOwp5fnNeVWj67G7CFk/SaSQn7NBk=
github.com/kr/pretty v0.3.1 h1:flRD4NNwYAUpkphVc1HcthR4KEIFJ65n8Mw5qdRn3LE=
github.com/kr/pretty v0.3.1/go.mod h1:hoEshYVHaxMs3cyo3Yncou5ZscifuDolrwPKZanG3xk=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/pty v1.1.8/go.mod h1:O1sed60cT9XZ5uDucP5qwvh+TE3NnUj51EiZO/lmSfw=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/ktrysmt/go-bitbucket v0.6.4 h1:C8dUGp0qkwncKtAnozHCbbqhptefzEd1I0sfnuy9rYQ=
github.com/ktrysmt/go-bitbucket v0.6.4/go.mod h1:9u0v3hsd2rqCHRIpbir1oP7F58uo5dq19sBYvuMoyQ4=
github.com/kylelemons/godebug v1.1.0 h1:RPNrshWIDI6G2gRW9EHilWtl7Z6Sb1BR0xunSBf0SNc=
github.com/kylelemons/godebug v1.1.0/go.mod h1:9/0rRGxNHcop5bhtWyNeEfOS8JIWk580+fNqagV/RAw=
github.com/lib/pq v1.0.0/go.mod h1:5WUZQaWbwv1U+lTReE5YruASi9Al49XbQIvNi/34Woo=
github.com/lib/pq v1.1.0/go.mod h1:5WUZQaWbwv1U+lTReE5YruASi9Al49XbQIvNi/34Woo=
github.com/lib/pq v1.2.0/go.mod h1:5WUZQaWbwv1U+lTReE5YruASi9Al49XbQIvNi/34Woo=
github.com/lib/pq v1.3.0/go.mod h1:5WUZQaWbwv1U+lTReE5YruASi9Al49XbQIvNi/34Woo=
github.com/lib/pq v1.10.0/go.mod h1:AlVN5x4E4T544tWzH6hKfbfQvm3HdbOxrmggDNAPY9o=
github.com/lib/pq v1.10.2/go.mod h1:AlVN5x4E4T544tWzH6hKfbfQvm3HdbOxrmggDNAPY9o=
github.com/lib/pq v1.10.9 h1:YXG7RB+JIjhP29X+OtkiDnYaXQwpS4JEWq7dtCCRUEw=
github.com/lib/pq v1.10.9/go.mod h1:AlVN5x4E4T544tWzH6hKfbfQvm3HdbOxrmggDNAPY9o=
github.com/lyft/protoc-gen-star v0.6.0/go.mod h1:TGAoBVkt8w7MPG72TrKIu85MIdXwDuzJYeZuUPFPNwA=
github.com/lyft/protoc-gen-star v0.6.1/go.mod h1:TGAoBVkt8w7MPG72TrKIu85MIdXwDuzJYeZuUPFPNwA=
github.com/lyft/protoc-gen-star/v2 v2.0.1/go.mod h1:RcCdONR2ScXaYnQC5tUzxzlpA3WVYF7/opLeUgcQs/o=
github.com/markbates/pkger v0.15.1 h1:3MPelV53RnGSW07izx5xGxl4e/sdRD6zqseIk0rMASY=
github.com/markbates/pkger v0.15.1/go.mod h1:0JoVlrol20BSywW79rN3kdFFsE5xYM+rSCQDXbLhiuI=
github.com/mattn/go-colorable v0.0.9/go.mod h1:9vuHe8Xs5qXnSaW/c/ABM9alt+Vo+STaOChaDxuIBZU=
github.com/mattn/go-colorable v0.1.1/go.mod h1:FuOcm+DKB9mbwrcAfNl7/TZVBZ6rcnceauSikq3lYCQ=
github.com/mattn/go-colorable v0.1.2/go.mod h1:U0ppj6V5qS13XJ6of8GYAs25YV2eR4EVcfRqFIhoBtE=
github.com/mattn/go-colorable v0.1.6 h1:6Su7aK7lXmJ/U79bYtBjLNaha4Fs1Rg9plHpcH+vvnE=
github.com/mattn/go-colorable v0.1.6/go.mod h1:u6P/XSegPjTcexA+o6vUJrdnUu04hMope9wVRipJSqc=
github.com/mattn/go-isatty v0.0.3/go.mod h1:M+lRXTBqGeGNdLjl/ufCoiOlB5xdOkqRJdNxMWT7Zi4=
github.com/mattn/go-isatty v0.0.5/go.mod h1:Iq45c/XA43vh69/j3iqttzPXn0bhXyGjM0Hdxcsrc5s=
github.com/mattn/go-isatty v0.0.7/go.mod h1:Iq45c/XA43vh69/j3iqttzPXn0bhXyGjM0Hdxcsrc5s=
github.com/mattn/go-isatty v0.0.8/go.mod h1:Iq45c/XA43vh69/j3iqttzPXn0bhXyGjM0Hdxcsrc5s=
github.com/mattn/go-isatty v0.0.9/go.mod h1:YNRxwqDuOph6SZLI9vUUz6OYw3QyUt7WiY2yME+cCiQ=
github.com/mattn/go-isatty v0.0.12/go.mod h1:cbi8OIDigv2wuxKPP5vlRcQ1OAZbq2CE4Kysco4FUpU=
github.com/mattn/go-isatty v0.0.16 h1:bq3VjFmv/sOjHtdEhmkEV4x1AJtvUvOJ2PFAZ5+peKQ=
github.com/mattn/go-isatty v0.0.16/go.mod h1:kYGgaQfpe5nmfYZH+SKPsOc2e4SrIfOl2e/yFXSvRLM=
github.com/mattn/go-sqlite3 v1.9.0/go.mod h1:FPy6KqzDD04eiIsT53CuJW3U88zkxoIYsOqkbpncsNc=
github.com/mattn/go-sqlite3 v1.14.6/go.mod h1:NyWgC/yNuGj7Q9rpYnZvas74GogHl5/Z4A/KQRfk6bU=
github.com/mattn/go-sqlite3 v1.14.14/go.mod h1:NyWgC/yNuGj7Q9rpYnZvas74GogHl5/Z4A/KQRfk6bU=
github.com/mattn/go-sqlite3 v1.14.22 h1:2gZY6PC6kBnID23Tichd1K+Z0oS6nE/XwU+Vz/5o4kU=
github.com/mattn/go-sqlite3 v1.14.22/go.mod h1:Uh1q+B4BYcTPb+yiD3kU8Ct7aC0hY9fxUwlHK0RXw+Y=
github.com/microsoft/go-mssqldb v1.0.0 h1:k2p2uuG8T5T/7Hp7/e3vMGTnnR0sU4h8d1CcC71iLHU=
github.com/microsoft/go-mssqldb v1.0.0/go.mod h1:+4wZTUnz/SV6nffv+RRRB/ss8jPng5Sho2SmM1l2ts4=
github.com/minio/asm2plan9s v0.0.0-20200509001527-cdd76441f9d8 h1:AMFGa4R4MiIpspGNG7Z948v4n35fFGB3RR3G/ry4FWs=
github.com/minio/asm2plan9s v0.0.0-20200509001527-cdd76441f9d8/go.mod h1:mC1jAcsrzbxHt8iiaC+zU4b1ylILSosueou12R++wfY=
github.com/minio/c2goasm v0.0.0-20190812172519-36a3d3bbc4f3 h1:+n/aFZefKZp7spd8DFdX7uMikMLXX4oubIzJF4kv/wI=
github.com/minio/c2goasm v0.0.0-20190812172519-36a3d3bbc4f3/go.mod h1:RagcQ7I8IeTMnF8JTXieKnO4Z6JCsikNEzj0DwauVzE=
github.com/mitchellh/mapstructure v0.0.0-20180220230111-00c29f56e238/go.mod h1:FVVH3fgwuzCH5S8UJGiWEs2h04kUh9fWfEaFds41c1Y=
github.com/mitchellh/mapstructure v1.1.2 h1:fmNYVwqnSfB9mZU6OS2O6GsXM+wcskZDuKQzvN1EDeE=
github.com/mitchellh/mapstructure v1.1.2/go.mod h1:FVVH3fgwuzCH5S8UJGiWEs2h04kUh9fWfEaFds41c1Y=
github.com/moby/docker-image-spec v1.3.1 h1:jMKff3w6PgbfSa69GfNg+zN/XLhfXJGnEx3Nl2EsFP0=
github.com/moby/docker-image-spec v1.3.1/go.mod h1:eKmb5VW8vQEh/BAr2yvVNvuiJuY6UIocYsFu/DxxRpo=
github.com/moby/sys/atomicwriter v0.1.0 h1:kw5D/EqkBwsBFi0ss9v1VG3wIkVhzGvLklJ+w3A14Sw=
github.com/moby/sys/atomicwriter v0.1.0/go.mod h1:Ul8oqv2ZMNHOceF643P6FKPXeCmYtlQMvpizfsSoaWs=
github.com/moby/sys/sequential v0.6.0 h1:qrx7XFUd/5DxtqcoH1h438hF5TmOvzC/lspjy7zgvCU=
github.com/moby/sys/sequential v0.6.0/go.mod h1:uyv8EUTrca5PnDsdMGXhZe6CCe8U/UiTWd+lL+7b/Ko=
github.com/moby/term v0.5.0 h1:xt8Q1nalod/v7BqbG21f8mQPqH+xAaC9C3N3wfWbVP0=
github.com/moby/term v0.5.0/go.mod h1:8FzsFHVUBGZdbDsJw/ot+X+d5HLUbvklYLJ9uGfcI3Y=
github.com/modocache/gover v0.0.0-20171022184752-b58185e213c5/go.mod h1:caMODM3PzxT8aQXRPkAt8xlV/e7d7w8GM5g0fa5F0D8=
github.com/montanaflynn/stats v0.0.0-20171201202039-1bf9dbcd8cbe/go.mod h1:wL8QJuTMNUDYhXwkmfOly8iTdp5TEcJFWZD2D7SIkUc=
github.com/montanaflynn/stats v0.6.6/go.mod h1:etXPPgVO6n31NxCd9KQUMvCM+ve0ruNzt6R8Bnaayow=
github.com/morikuni/aec v1.0.0 h1:nP9CBfwrvYnBRgY6qfDQkygYDmYwOilePFkwzv4dU8A=
github.com/morikuni/aec v1.0.0/go.mod h1:BbKIizmSmc5MMPqRYbxO4ZU0S0+P200+tUnFx7PXmsc=
github.com/mtibben/percent v0.2.1 h1:5gssi8Nqo8QU/r2pynCm+hBQHpkB/uNK7BJCFogWdzs=
github.com/mtibben/percent v0.2.1/go.mod h1:KG9uO+SZkUp+VkRHsCdYQV3XSZrrSpR3O9ibNBTZrns=
github.com/mutecomm/go-sqlcipher/v4 v4.4.0 h1:sV1tWCWGAVlPhNGT95Q+z/txFxuhAYWwHD1afF5bMZg=
github.com/mutecomm/go-sqlcipher/v4 v4.4.0/go.mod h1:PyN04SaWalavxRGH9E8ZftG6Ju7rsPrGmQRjrEaVpiY=
github.com/nakagami/firebirdsql v0.0.0-20190310045651-3c02a58cfed8 h1:P48LjvUQpTReR3TQRbxSeSBsMXzfK0uol7eRcr7VBYQ=
github.com/nakagami/firebirdsql v0.0.0-20190310045651-3c02a58cfed8/go.mod h1:86wM1zFnC6/uDBfZGNwB65O+pR2OFi5q/YQaEUid1qA=
github.com/neo4j/neo4j-go-driver v1.8.1-0.20200803113522-b626aa943eba h1:fhFP5RliM2HW/8XdcO5QngSfFli9GcRIpMXvypTQt6E=
github.com/neo4j/neo4j-go-driver v1.8.1-0.20200803113522-b626aa943eba/go.mod h1:ncO5VaFWh0Nrt+4KT4mOZboaczBZcLuHrG+/sUeP8gI=
github.com/niemeyer/pretty v0.0.0-20200227124842-a10e7caefd8e/go.mod h1:zD1mROLANZcx1PVRCS0qkT7pwLkGfwJo4zjcN/Tysno=
github.com/nxadm/tail v1.4.4/go.mod h1:kenIhsEOeOJmVchQTgglprH7qJGnHDVpk1VPCcaMI8A=
github.com/nxadm/tail v1.4.8 h1:nPr65rt6Y5JFSKQO7qToXr7pePgD6Gwiw05lkbyAQTE=
github.com/nxadm/tail v1.4.8/go.mod h1:+ncqLTQzXmGhMZNUePPaPqPvBxHAIsmXswZKocGu+AU=
github.com/onsi/ginkgo v1.6.0/go.mod h1:lLunBs/Ym6LB5Z9jYTR76FiuTmxDTDusOGeTQH+WWjE=
github.com/onsi/ginkgo v1.12.0/go.mod h1:oUhWkIvk5aDxtKvDDuw8gItl8pKl42LzjC9KZE0HfGg=
github.com/onsi/ginkgo v1.12.1/go.mod h1:zj2OWP4+oCPe1qIXoGWkgMRwljMUYCdkwsT2108oapk=
github.com/onsi/ginkgo v1.16.4 h1:29JGrr5oVBm5ulCWet69zQkzWipVXIol6ygQUe/EzNc=
github.com/onsi/ginkgo v1.16.4/go.mod h1:dX+/inL/fNMqNlz0e9LfyB9TswhZpCVdJM/Z6Vvnwo0=
github.com/onsi/gomega v1.7.1/go.mod h1:XdKZgCCFLUoM/7CFJVPcG8C1xQ1AJ0vpAezJrB7JYyY=
github.com/onsi/gomega v1.9.0/go.mod h1:Ho0h+IUsWyvy1OpqCwxlQ/21gkhVunqlU8fDGcoTdcA=
github.com/onsi/gomega v1.10.1/go.mod h1:iN09h71vgCQne3DLsj+A5owkum+a2tYe+TOCB1ybHNo=
github.com/onsi/gomega v1.15.0 h1:WjP/FQ/sk43MRmnEcT+MlDw2TFvkrXlprrPST/IudjU=
github.com/onsi/gomega v1.15.0/go.mod h1:cIuvLEne0aoVhAgh/O6ac0Op8WWw9H6eYCriF+tEHG0=
github.com/opencontainers/go-digest v1.0.0 h1:apOUWs51W5PlhuyGyz9FCeeBIOUDA/6nW8Oi/yOhh5U=
github.com/opencontainers/go-digest v1.0.0/go.mod h1:0JzlMkj0TRzQZfJkVvzbP0HBR3IKzErnv2BNG4W4MAM=
github.com/opencontainers/image-spec v1.1.0 h1:8SG7/vwALn54lVB/0yZ/MMwhFrPYtpEHQb2IpWsCzug=
github.com/opencontainers/image-spec v1.1.0/go.mod h1:W4s4sFTMaBeK1BQLXbG4AdM2szdn85PY75RI83NrTrM=
github.com/phpdave11/gofpdf v1.4.2/go.mod h1:zpO6xFn9yxo3YLyMvW8HcKWVdbNqgIfOOp2dXMnm1mY=
github.com/phpdave11/gofpdi v1.0.12/go.mod h1:vBmVV0Do6hSBHC8uKUQ71JGW+ZGQq74llk/7bXwjDoI=
github.com/phpdave11/gofpdi v1.0.13/go.mod h1:vBmVV0Do6hSBHC8uKUQ71JGW+ZGQq74llk/7bXwjDoI=
github.com/pierrec/lz4 v2.0.5+incompatible h1:2xWsjqPFWcplujydGg4WmhC/6fZqK42wMM8aXeqhl0I=
github.com/pierrec/lz4 v2.0.5+incompatible/go.mod h1:pdkljMzZIN41W+lC3N2tnIh5sFi+IEE17M5jbnwPHcY=
github.com/pierrec/lz4/v4 v4.1.15/go.mod h1:gZWDp/Ze/IJXGXf23ltt2EXimqmTUXEy0GFuRQyBid4=
github.com/pierrec/lz4/v4 v4.1.16 h1:kQPfno+wyx6C5572ABwV+Uo3pDFzQ7yhyGchSyRda0c=
github.com/pierrec/lz4/v4 v4.1.16/go.mod h1:gZWDp/Ze/IJXGXf23ltt2EXimqmTUXEy0GFuRQyBid4=
github.com/pkg/browser v0.0.0-20210115035449-ce105d075bb4/go.mod h1:N6UoU20jOqggOuDwUaBQpluzLNDqif3kq9z2wpdYEfQ=
github.com/pkg/browser v0.0.0-20210911075715-681adbf594b8 h1:KoWmjvw+nsYOo29YJK9vDA65RGE3NrOnUtO7a+RF9HU=
github.com/pkg/browser v0.0.0-20210911075715-681adbf594b8/go.mod h1:HKlIX3XHQyzLZPlr7++PzdhaXEj94dEiJgZDTsxEqUI=
github.com/pkg/diff v0.0.0-20210226163009-20ebb0f2a09e/go.mod h1:pJLUxLENpZxwdsKMEsNbx1VGcRFpLqf3715MtcvvzbA=
github.com/pkg/errors v0.8.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pkg/errors v0.9.1 h1:FEBLx1zS214owpjy7qsBeixbURkuhQAwrK5UwLGTwt4=
github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pkg/sftp v1.10.1/go.mod h1:lYOWFsE0bwd1+KfKJaKeuokY15vzFx25BLbzYYoAxZI=
github.com/pkg/sftp v1.13.1/go.mod h1:3HaPG6Dq1ILlpPZRO0HVMrsydcdLt6HRDccSgb87qRg=
github.com/planetscale/vtprotobuf v0.6.1-0.20240319094008-0393e58bdf10 h1:GFCKgmp0tecUJ0sJuv4pzYCqS9+RGSn52M3FUwPs+uo=
github.com/planetscale/vtprotobuf v0.6.1-0.20240319094008-0393e58bdf10/go.mod h1:t/avpk3KcrXxUnYOhZhMXJlSEyie6gQbtLq5NM3loB8=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2 h1:Jamvg5psRIccs7FGNTlIRMkT8wgtp5eCXdBlqhYGL6U=
github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/prometheus/client_model v0.0.0-20190812154241-14fe0d1b01d4/go.mod h1:xMI15A0UPsDsEKsMN9yxemIoYk6Tm2C1GtYGdfGttqA=
github.com/prometheus/client_model v0.2.0/go.mod h1:xMI15A0UPsDsEKsMN9yxemIoYk6Tm2C1GtYGdfGttqA=
github.com/prometheus/client_model v0.3.0/go.mod h1:LDGWKZIo7rky3hgvBe+caln+Dr3dPggB5dvjtD7w9+w=
github.com/remyoudompheng/bigfft v0.0.0-20190728182440-6a916e37a237/go.mod h1:qqbHyh8v60DhA7CoWK5oRCqLrMHRGoxYCSS9EjAz6Eo=
github.com/remyoudompheng/bigfft v0.0.0-20200410134404-eec4a21b6bb0 h1:OdAsTTz6OkFY5QxjkYwrChwuRruF69c169dPK26NUlk=
github.com/remyoudompheng/bigfft v0.0.0-20200410134404-eec4a21b6bb0/go.mod h1:qqbHyh8v60DhA7CoWK5oRCqLrMHRGoxYCSS9EjAz6Eo=
github.com/rogpeppe/fastuuid v1.2.0/go.mod h1:jVj6XXZzXRy/MSR5jhDC/2q6DgLz+nrA6LYCDYWNEvQ=
github.com/rogpeppe/go-internal v1.3.0/go.mod h1:M8bDsm7K2OlrFYOpmOWEs/qY81heoFRclV5y23lUDJ4=
github.com/rogpeppe/go-internal v1.6.1/go.mod h1:xXDCJY+GAPziupqXw64V24skbSoqbTEfhy4qGm1nDQc=
github.com/rogpeppe/go-internal v1.9.0/go.mod h1:WtVeX8xhTBvf0smdhujwtBcq4Qrzq/fJaraNFVN+nFs=
github.com/rogpeppe/go-internal v1.14.1 h1:UQB4HGPB6osV0SQTLymcB4TgvyWu6ZyliaW0tI/otEQ=
github.com/rogpeppe/go-internal v1.14.1/go.mod h1:MaRKkUm5W0goXpeCfT7UZI6fk/L7L7so1lCWt35ZSgc=
github.com/rqlite/gorqlite v0.0.0-20230708021416-2acd02b70b79 h1:V7x0hCAgL8lNGezuex1RW1sh7VXXCqfw8nXZti66iFg=
github.com/rqlite/gorqlite v0.0.0-20230708021416-2acd02b70b79/go.mod h1:xF/KoXmrRyahPfo5L7Szb5cAAUl53dMWBh9cMruGEZg=
github.com/rs/xid v1.2.1/go.mod h1:+uKXf+4Djp6Md1KODXJxgGQPKngRmWyn10oCKFzNHOQ=
github.com/rs/zerolog v1.13.0/go.mod h1:YbFCdg8HfsridGWAh22vktObvhZbQsZXe4/zB0OKkWU=
github.com/rs/zerolog v1.15.0/go.mod h1:xYTKnLHcpfU2225ny5qZjxnj9NvkumZYjJHlAThCjNc=
github.com/ruudk/golang-pdf417 v0.0.0-20181029194003-1af4ab5afa58/go.mod h1:6lfFZQK844Gfx8o5WFuvpxWRwnSoipWe/p622j1v06w=
github.com/ruudk/golang-pdf417 v0.0.0-20201230142125-a7e3863a1245/go.mod h1:pQAZKsJ8yyVxGRWYNEm9oFB8ieLgKFnamEyDmSA0BRk=
github.com/satori/go.uuid v1.2.0/go.mod h1:dA0hQrYB0VpLJoorglMZABFdXlWrHn1NEOzdhQKdks0=
github.com/shopspring/decimal v0.0.0-20180709203117-cd690d0c9e24/go.mod h1:M+9NzErvs504Cn4c5DxATwIqPbtswREoFCre64PpcG4=
github.com/shopspring/decimal v0.0.0-20200227202807-02e2044944cc/go.mod h1:DKyhrW/HYNuLGql+MJL6WCR6knT2jwCFRcu2hWCYk4o=
github.com/shopspring/decimal v1.2.0 h1:abSATXmQEYyShuxI4/vyW3tV1MrKAJzCZ/0zLUXYbsQ=
github.com/shopspring/decimal v1.2.0/go.mod h1:DKyhrW/HYNuLGql+MJL6WCR6knT2jwCFRcu2hWCYk4o=
github.com/sirupsen/logrus v1.4.1/go.mod h1:ni0Sbl8bgC9z8RoU9G6nDWqqs/fq4eDPysMBDgk/93Q=
github.com/sirupsen/logrus v1.4.2/go.mod h1:tLMulIdttU9McNUspp0xgXVQah82FyeX6MwdIuYE2rE=
github.com/sirupsen/logrus v1.9.3 h1:dueUQJ1C2q9oE3F7wvmSGAaVtTmUizReu6fjN8uqzbQ=
github.com/sirupsen/logrus v1.9.3/go.mod h1:naHLuLoDiP4jHNo9R0sCBMtWGeIprob74mVsIT4qYEQ=
github.com/snowflakedb/gosnowflake v1.6.19 h1:KSHXrQ5o7uso25hNIzi/RObXtnSGkFgie91X82KcvMY=
github.com/snowflakedb/gosnowflake v1.6.19/go.mod h1:FM1+PWUdwB9udFDsXdfD58NONC0m+MlOSmQRvimobSM=
github.com/spaolacci/murmur3 v0.0.0-20180118202830-f09979ecbc72/go.mod h1:JwIasOWyU6f++ZhiEuf87xNszmSA2myDM2Kzu9HwQUA=
github.com/spf13/afero v1.3.3/go.mod h1:5KUK8ByomD5Ti5Artl0RtHeI5pTF7MIDuXL3yY520V4=
github.com/spf13/afero v1.6.0/go.mod h1:Ai8FlHk4v/PARR026UzYexafAt9roJ7LcLMAmO6Z93I=
github.com/spf13/afero v1.9.2/go.mod h1:iUV7ddyEEZPO5gA3zD4fJt6iStLlL+Lg4m2cihcDf8Y=
github.com/spiffe/go-spiffe/v2 v2.5.0 h1:N2I01KCUkv1FAjZXJMwh95KK1ZIQLYbPfhaxw8WS0hE=
github.com/spiffe/go-spiffe/v2 v2.5.0/go.mod h1:P+NxobPc6wXhVtINNtFjNWGBTreew1GBUCwT2wPmb7g=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.1.1/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.2.0/go.mod h1:qt09Ya8vawLte6SNmTgCsAVtYtaKzEcn8ATUoHMkEqE=
github.com/stretchr/objx v0.4.0/go.mod h1:YvHI0jy2hoMjB+UWwv71VJQ9isScKT/TqJzVSSt89Yw=
github.com/stretchr/objx v0.5.0/go.mod h1:Yh+to48EsGEfYuaHDzXPcE3xhTkx73EhmCGUpEOglKo=
github.com/stretchr/objx v0.5.2 h1:xuMeJ0Sdp5ZMRXx/aWO6RZxdr3beISkG5/G/aIRr3pY=
github.com/stretchr/objx v0.5.2/go.mod h1:FRsXN1f5AsAjCGJKqEizvkpNtU+EGNCLh3NxZ/8L+MA=
github.com/stretchr/testify v1.2.2/go.mod h1:a8OnRcib4nhh0OaRAV+Yts87kKdq0PP7pXfy6kDkUVs=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.4.0/go.mod h1:j7eGeouHqKxXV5pUuKE4zz7dFj8WfuZ+81PSLYec5m4=
github.com/stretchr/testify v1.5.1/go.mod h1:5W2xD1RspED5o8YsWQXVCued0rvSQ+mT+I5cxcmMvtA=
github.com/stretchr/testify v1.6.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.7.0/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.7.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.8.0/go.mod h1:yNjHg4UonilssWZ8iaSj1OCr/vHnekPRkoO+kdMU+MU=
github.com/stretchr/testify v1.8.1/go.mod h1:w2LPCIKwWwSfY2zedu0+kehJoqGctiVI29o6fzry7u4=
github.com/stretchr/testify v1.8.3/go.mod h1:sz/lmYIOXD/1dqDmKjjqLyZ2RngseejIcXlSw2iwfAo=
github.com/stretchr/testify v1.11.1 h1:7s2iGBzp5EwR7/aIZr8ao5+dra3wiQyKjjFuvgVKu7U=
github.com/stretchr/testify v1.11.1/go.mod h1:wZwfW3scLgRK+23gO65QZefKpKQRnfz6sD981Nm4B6U=
github.com/tidwall/pretty v1.0.0 h1:HsD+QiTn7sK6flMKIvNmpqz1qrpP3Ps6jOKIKMooyg4=
github.com/tidwall/pretty v1.0.0/go.mod h1:XNkn88O1ChpSDQmQeStsy+sBenx6DDtFZJxhVysOjyk=
github.com/xanzy/go-gitlab v0.15.0 h1:rWtwKTgEnXyNUGrOArN7yyc3THRkpYcKXIXia9abywQ=
github.com/xanzy/go-gitlab v0.15.0/go.mod h1:8zdQa/ri1dfn8eS3Ir1SyfvOKlw7WBJ8DVThkpGiXrs=
github.com/xdg-go/pbkdf2 v1.0.0 h1:Su7DPu48wXMwC3bs7MCNG+z4FhcyEuz5dlvchbq0B0c=
github.com/xdg-go/pbkdf2 v1.0.0/go.mod h1:jrpuAogTd400dnrH08LKmI/xc1MbPOebTwRqcT5RDeI=
github.com/xdg-go/scram v1.0.2/go.mod h1:1WAq6h33pAW+iRreB34OORO2Nf7qel3VV3fjBj+hCSs=
github.com/xdg-go/scram v1.1.1 h1:VOMT+81stJgXW3CpHyqHN3AXDYIMsx56mEFrB37Mb/E=
github.com/xdg-go/scram v1.1.1/go.mod h1:RaEWvsqvNKKvBPvcKeFjrG2cJqOkHTiyTpzz23ni57g=
github.com/xdg-go/stringprep v1.0.2/go.mod h1:8F9zXuvzgwmyT5DUm4GUfZGDdT3W+LCvS6+da4O5kxM=
github.com/xdg-go/stringprep v1.0.3 h1:kdwGpVNwPFtjs98xCGkHjQtGKh86rDcRZN17QEMCOIs=
github.com/xdg-go/stringprep v1.0.3/go.mod h1:W3f5j4i+9rC0kuIEJL0ky1VpHXQU3ocBgklLGvcBnW8=
github.com/youmark/pkcs8 v0.0.0-20181117223130-1be2e3e5546d h1:splanxYIlg+5LfHAM6xpdFEAYOk8iySO56hMFq6uLyA=
github.com/youmark/pkcs8 v0.0.0-20181117223130-1be2e3e5546d/go.mod h1:rHwXgn7JulP+udvsHwJoVG1YGAP6VLg4y9I5dyZdqmA=
github.com/yuin/goldmark v1.1.25/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
github.com/yuin/goldmark v1.1.27/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
github.com/yuin/goldmark v1.1.32/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
github.com/yuin/goldmark v1.2.1/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
github.com/yuin/goldmark v1.3.5/go.mod h1:mwnBkeHKe2W/ZEtQ+71ViKU8L12m81fl3OWwC1Zlc8k=
github.com/yuin/goldmark v1.4.1/go.mod h1:mwnBkeHKe2W/ZEtQ+71ViKU8L12m81fl3OWwC1Zlc8k=
github.com/yuin/goldmark v1.4.13/go.mod h1:6yULJ656Px+3vBD8DxQVa3kxgyrAnzto9xy5taEt/CY=
github.com/zeebo/assert v1.3.0 h1:g7C04CbJuIDKNPFHmsk4hwZDO5O+kntRxzaUoNXj+IQ=
github.com/zeebo/assert v1.3.0/go.mod h1:Pq9JiuJQpG8JLJdtkwrJESF0Foym2/D9XMU5ciN/wJ0=
github.com/zeebo/errs v1.4.0 h1:XNdoD/RRMKP7HD0UhJnIzUy74ISdGGxURlYG8HSWSfM=
github.com/zeebo/errs v1.4.0/go.mod h1:sgbWHsvVuTPHcqJJGQ1WhI5KbWlHYz+2+2C/LSEtCw4=
github.com/zeebo/xxh3 v1.0.2 h1:xZmwmqxHZA8AI603jOQ0tMqmBr9lPeFwGg6d+xy9DC0=
github.com/zeebo/xxh3 v1.0.2/go.mod h1:5NWz9Sef7zIDm2JHfFlcQvNekmcEl9ekUZQQKCYaDcA=
github.com/zenazn/goji v0.9.0/go.mod h1:7S9M489iMyHBNxwZnk9/EHS098H4/F6TATF2mIxtB1Q=
gitlab.com/nyarla/go-crypt v0.0.0-20160106005555-d9a5dc2b789b h1:7gd+rd8P3bqcn/96gOZa3F5dpJr/vEiDQYlNb/y2uNs=
gitlab.com/nyarla/go-crypt v0.0.0-20160106005555-d9a5dc2b789b/go.mod h1:T3BPAOm2cqquPa0MKWeNkmOM5RQsRhkrwMWonFMN7fE=
go.mongodb.org/mongo-driver v1.7.5 h1:ny3p0reEpgsR2cfA5cjgwFZg3Cv/ofFh/8jbhGtz9VI=
go.mongodb.org/mongo-driver v1.7.5/go.mod h1:VXEWRZ6URJIkUq2SCAyapmhH0ZLRBP+FT4xhp5Zvxng=
go.opencensus.io v0.21.0/go.mod h1:mSImk1erAIZhrmZN+AvHh14ztQfjbGwt4TtuofqLduU=
go.opencensus.io v0.22.0/go.mod h1:+kGneAE2xo2IficOXnaByMWTGM9T73dGwxeWcUqIpI8=
go.opencensus.io v0.22.2/go.mod h1:yxeiOL68Rb0Xd1ddK5vPZ/oVn4vY4Ynel7k9FzqtOIw=
go.opencensus.io v0.22.3/go.mod h1:yxeiOL68Rb0Xd1ddK5vPZ/oVn4vY4Ynel7k9FzqtOIw=
go.opencensus.io v0.22.4/go.mod h1:yxeiOL68Rb0Xd1ddK5vPZ/oVn4vY4Ynel7k9FzqtOIw=
go.opencensus.io v0.22.5/go.mod h1:5pWMHQbX5EPX2/62yrJeAkowc+lfs/XD7Uxpq3pI6kk=
go.opencensus.io v0.23.0/go.mod h1:XItmlyltB5F7CS4xOC1DcqMoFqwtC6OG2xF7mCv7P7E=
go.opencensus.io v0.24.0 h1:y73uSU6J157QMP2kn2r30vwW1A2W2WFwSCGnAVxeaD0=
go.opencensus.io v0.24.0/go.mod h1:vNK8G9p7aAivkbmorf4v+7Hgx+Zs0yY+0fOtgBfjQKo=
go.opentelemetry.io/auto/sdk v1.2.1 h1:jXsnJ4Lmnqd11kwkBV2LgLoFMZKizbCi5fNZ/ipaZ64=
go.opentelemetry.io/auto/sdk v1.2.1/go.mod h1:KRTj+aOaElaLi+wW1kO/DZRXwkF4C5xPbEe3ZiIhN7Y=
go.opentelemetry.io/contrib/detectors/gcp v1.36.0 h1:F7q2tNlCaHY9nMKHR6XH9/qkp8FktLnIcy6jJNyOCQw=
go.opentelemetry.io/contrib/detectors/gcp v1.36.0/go.mod h1:IbBN8uAIIx734PTonTPxAxnjc2pQTxWNkwfstZ+6H2k=
go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc v0.61.0 h1:q4XOmH/0opmeuJtPsbFNivyl7bCt7yRBbeEm2sC/XtQ=
go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc v0.61.0/go.mod h1:snMWehoOh2wsEwnvvwtDyFCxVeDAODenXHtn5vzrKjo=
go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp v0.61.0 h1:F7Jx+6hwnZ41NSFTO5q4LYDtJRXBf2PD0rNBkeB/lus=
go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp v0.61.0/go.mod h1:UHB22Z8QsdRDrnAtX4PntOl36ajSxcdUMt1sF7Y6E7Q=
go.opentelemetry.io/otel v1.40.0 h1:oA5YeOcpRTXq6NN7frwmwFR0Cn3RhTVZvXsP4duvCms=
go.opentelemetry.io/otel v1.40.0/go.mod h1:IMb+uXZUKkMXdPddhwAHm6UfOwJyh4ct1ybIlV14J0g=
go.opentelemetry.io/otel/exporters/otlp/otlptrace v1.29.0 h1:dIIDULZJpgdiHz5tXrTgKIMLkus6jEFa7x5SOKcyR7E=
go.opentelemetry.io/otel/exporters/otlp/otlptrace v1.29.0/go.mod h1:jlRVBe7+Z1wyxFSUs48L6OBQZ5JwH2Hg/Vbl+t9rAgI=
go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp v1.27.0 h1:QY7/0NeRPKlzusf40ZE4t1VlMKbqSNT7cJRYzWuja0s=
go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp v1.27.0/go.mod h1:HVkSiDhTM9BoUJU8qE6j2eSWLLXvi1USXjyd2BXT8PY=
go.opentelemetry.io/otel/exporters/stdout/stdoutmetric v1.36.0 h1:rixTyDGXFxRy1xzhKrotaHy3/KXdPhlWARrCgK+eqUY=
go.opentelemetry.io/otel/exporters/stdout/stdoutmetric v1.36.0/go.mod h1:dowW6UsM9MKbJq5JTz2AMVp3/5iW5I/TStsk8S+CfHw=
go.opentelemetry.io/otel/metric v1.40.0 h1:rcZe317KPftE2rstWIBitCdVp89A2HqjkxR3c11+p9g=
go.opentelemetry.io/otel/metric v1.40.0/go.mod h1:ib/crwQH7N3r5kfiBZQbwrTge743UDc7DTFVZrrXnqc=
go.opentelemetry.io/otel/sdk v1.40.0 h1:KHW/jUzgo6wsPh9At46+h4upjtccTmuZCFAc9OJ71f8=
go.opentelemetry.io/otel/sdk v1.40.0/go.mod h1:Ph7EFdYvxq72Y8Li9q8KebuYUr2KoeyHx0DRMKrYBUE=
go.opentelemetry.io/otel/sdk/metric v1.40.0 h1:mtmdVqgQkeRxHgRv4qhyJduP3fYJRMX4AtAlbuWdCYw=
go.opentelemetry.io/otel/sdk/metric v1.40.0/go.mod h1:4Z2bGMf0KSK3uRjlczMOeMhKU2rhUqdWNoKcYrtcBPg=
go.opentelemetry.io/otel/trace v1.40.0 h1:WA4etStDttCSYuhwvEa8OP8I5EWu24lkOzp+ZYblVjw=
go.opentelemetry.io/otel/trace v1.40.0/go.mod h1:zeAhriXecNGP/s2SEG3+Y8X9ujcJOTqQ5RgdEJcawiA=
go.opentelemetry.io/proto/otlp v0.7.0/go.mod h1:PqfVotwruBrMGOCsRd/89rSnXhoiJIqeYNgFYFoEGnI=
go.opentelemetry.io/proto/otlp v0.15.0/go.mod h1:H7XAot3MsfNsj7EXtrA2q5xSNQ10UqI405h3+duxN4U=
go.opentelemetry.io/proto/otlp v0.19.0/go.mod h1:H7XAot3MsfNsj7EXtrA2q5xSNQ10UqI405h3+duxN4U=
go.opentelemetry.io/proto/otlp v1.3.1 h1:TrMUixzpM0yuc/znrFTP9MMRh8trP93mkCiDVeXrui0=
go.opentelemetry.io/proto/otlp v1.3.1/go.mod h1:0X1WI4de4ZsLrrJNLAQbFeLCm3T7yBkR0XqQ7niQU+8=
go.uber.org/atomic v1.3.2/go.mod h1:gD2HeocX3+yG+ygLZcrzQJaqmWj9AIm7n08wl/qW/PE=
go.uber.org/atomic v1.4.0/go.mod h1:gD2HeocX3+yG+ygLZcrzQJaqmWj9AIm7n08wl/qW/PE=
go.uber.org/atomic v1.5.0/go.mod h1:sABNBOSYdrvTF6hTgEIbc7YasKWGhgEQZyfxyTvoXHQ=
go.uber.org/atomic v1.6.0/go.mod h1:sABNBOSYdrvTF6hTgEIbc7YasKWGhgEQZyfxyTvoXHQ=
go.uber.org/multierr v1.1.0/go.mod h1:wR5kodmAFQ0UK8QlbwjlSNy0Z68gJhDJUG5sjR94q/0=
go.uber.org/multierr v1.3.0/go.mod h1:VgVr7evmIr6uPjLBxg28wmKNXyqE9akIJ5XnfpiKl+4=
go.uber.org/multierr v1.5.0/go.mod h1:FeouvMocqHpRaaGuG9EjoKcStLC43Zu/fmqdUMPcKYU=
go.uber.org/tools v0.0.0-20190618225709-2cfd321de3ee/go.mod h1:vJERXedbb3MVM5f9Ejo0C68/HhF8uaILCdgjnY+goOA=
go.uber.org/zap v1.9.1/go.mod h1:vwi/ZaCAaUcBkycHslxD9B2zi4UTXhF60s6SWpuDF0Q=
go.uber.org/zap v1.10.0/go.mod h1:vwi/ZaCAaUcBkycHslxD9B2zi4UTXhF60s6SWpuDF0Q=
go.uber.org/zap v1.13.0/go.mod h1:zwrFLgMcdUuIBviXEYEH1YKNaOBnKXsx2IPda5bBwHM=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20190411191339-88737f569e3a/go.mod h1:WFFai1msRO1wXaEeE5yQxYXgSfI8pQAWXbQop6sCtWE=
golang.org/x/crypto v0.0.0-20190510104115-cbcb75029529/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20190605123033-f99c8df09eb5/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20190820162420-60c769a6c586/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20190911031432-227b76d455e7/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20200302210943-78000ba7a073/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20200323165209-0ec3e9974c59/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20200622213623-75b288015ac9/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20201002170205-7f63de1d35b0/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20201112155050-0c6587e931a9/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20201203163018-be400aefbc4c/go.mod h1:jdWPYTVW3xRLrWPugEBEK3UY2ZEsg3UU495nc5E+M+I=
golang.org/x/crypto v0.0.0-20210322153248-0c34fe9e7dc2/go.mod h1:T9bdIzuCu7OtxOm1hfPfRQxPLYneinmdGuTeoZ9dtd4=
golang.org/x/crypto v0.0.0-20210421170649-83a5a9bb288b/go.mod h1:T9bdIzuCu7OtxOm1hfPfRQxPLYneinmdGuTeoZ9dtd4=
golang.org/x/crypto v0.0.0-20210616213533-5ff15b29337e/go.mod h1:GvvjBRRGRdwPK5ydBHafDWAxML/pGHZbMvKqRZ5+Abc=
golang.org/x/crypto v0.0.0-20210711020723-a769d52b0f97/go.mod h1:GvvjBRRGRdwPK5ydBHafDWAxML/pGHZbMvKqRZ5+Abc=
golang.org/x/crypto v0.0.0-20210817164053-32db794688a5/go.mod h1:GvvjBRRGRdwPK5ydBHafDWAxML/pGHZbMvKqRZ5+Abc=
golang.org/x/crypto v0.0.0-20210921155107-089bfa567519/go.mod h1:GvvjBRRGRdwPK5ydBHafDWAxML/pGHZbMvKqRZ5+Abc=
golang.org/x/crypto v0.0.0-20211108221036-ceb1ce70b4fa/go.mod h1:GvvjBRRGRdwPK5ydBHafDWAxML/pGHZbMvKqRZ5+Abc=
golang.org/x/crypto v0.0.0-20220511200225-c6db032c6c88/go.mod h1:IxCIyHEi3zRg3s0A5j5BB6A9Jmi73HwBIUl50j+osU4=
golang.org/x/crypto v0.0.0-20220622213112-05595931fe9d/go.mod h1:IxCIyHEi3zRg3s0A5j5BB6A9Jmi73HwBIUl50j+osU4=
golang.org/x/crypto v0.45.0 h1:jMBrvKuj23MTlT0bQEOBcAE0mjg8mK9RXFhRH6nyF3Q=
golang.org/x/crypto v0.45.0/go.mod h1:XTGrrkGJve7CYK7J8PEww4aY7gM3qMCElcJQ8n8JdX4=
golang.org/x/exp v0.0.0-20180321215751-8460e604b9de/go.mod h1:CJ0aWSM057203Lf6IL+f9T1iT9GByDxfZKAQTCR3kQA=
golang.org/x/exp v0.0.0-20180807140117-3d87b88a115f/go.mod h1:CJ0aWSM057203Lf6IL+f9T1iT9GByDxfZKAQTCR3kQA=
golang.org/x/exp v0.0.0-20190121172915-509febef88a4/go.mod h1:CJ0aWSM057203Lf6IL+f9T1iT9GByDxfZKAQTCR3kQA=
golang.org/x/exp v0.0.0-20190125153040-c74c464bbbf2/go.mod h1:CJ0aWSM057203Lf6IL+f9T1iT9GByDxfZKAQTCR3kQA=
golang.org/x/exp v0.0.0-20190306152737-a1d7652674e8/go.mod h1:CJ0aWSM057203Lf6IL+f9T1iT9GByDxfZKAQTCR3kQA=
golang.org/x/exp v0.0.0-20190510132918-efd6b22b2522/go.mod h1:ZjyILWgesfNpC6sMxTJOJm9Kp84zZh5NQWvqDGG3Qr8=
golang.org/x/exp v0.0.0-20190829153037-c13cbed26979/go.mod h1:86+5VVa7VpoJ4kLfm080zCjGlMRFzhUhsZKEZO7MGek=
golang.org/x/exp v0.0.0-20191002040644-a1355ae1e2c3/go.mod h1:NOZ3BPKG0ec/BKJQgnvsSFpcKLM5xXVWnvZS97DWHgE=
golang.org/x/exp v0.0.0-20191030013958-a1ab85dbe136/go.mod h1:JXzH8nQsPlswgeRAPE3MuO9GYsAcnJvJ4vnMwN/5qkY=
golang.org/x/exp v0.0.0-20191129062945-2f5052295587/go.mod h1:2RIsYlXP63K8oxa1u096TMicItID8zy7Y6sNkU49FU4=
golang.org/x/exp v0.0.0-20191227195350-da58074b4299/go.mod h1:2RIsYlXP63K8oxa1u096TMicItID8zy7Y6sNkU49FU4=
golang.org/x/exp v0.0.0-20200119233911-0405dc783f0a/go.mod h1:2RIsYlXP63K8oxa1u096TMicItID8zy7Y6sNkU49FU4=
golang.org/x/exp v0.0.0-20200207192155-f17229e696bd/go.mod h1:J/WKrq2StrnmMY6+EHIKF9dgMWnmCNThgcyBT1FY9mM=
golang.org/x/exp v0.0.0-20200224162631-6cc2880d07d6/go.mod h1:3jZMyOhIsHpP37uCMkUooju7aAi5cS1Q23tOzKc+0MU=
golang.org/x/exp v0.0.0-20220827204233-334a2380cb91/go.mod h1:cyybsKvd6eL0RnXn6p/Grxp8F5bW7iYuBgsNCOHpMYE=
golang.org/x/exp v0.0.0-20230315142452-642cacee5cc0 h1:pVgRXcIictcr+lBQIFeiwuwtDIs4eL21OuM9nyAADmo=
golang.org/x/exp v0.0.0-20230315142452-642cacee5cc0/go.mod h1:CxIveKay+FTh1D0yPZemJVgC/95VzuuOLq5Qi4xnoYc=
golang.org/x/image v0.0.0-20180708004352-c73c2afc3b81/go.mod h1:ux5Hcp/YLpHSI86hEcLt0YII63i6oz57MZXIpbrjZUs=
golang.org/x/image v0.0.0-20190227222117-0694c2d4d067/go.mod h1:kZ7UVZpmo3dzQBMxlp+ypCbDeSB+sBbTgSJuh5dn5js=
golang.org/x/image v0.0.0-20190802002840-cff245a6509b/go.mod h1:FeLwcggjj3mMvU+oOTbSwawSJRM1uh48EjtB4UJZlP0=
golang.org/x/image v0.0.0-20190910094157-69e4b8554b2a/go.mod h1:FeLwcggjj3mMvU+oOTbSwawSJRM1uh48EjtB4UJZlP0=
golang.org/x/image v0.0.0-20200119044424-58c23975cae1/go.mod h1:FeLwcggjj3mMvU+oOTbSwawSJRM1uh48EjtB4UJZlP0=
golang.org/x/image v0.0.0-20200430140353-33d19683fad8/go.mod h1:FeLwcggjj3mMvU+oOTbSwawSJRM1uh48EjtB4UJZlP0=
golang.org/x/image v0.0.0-20200618115811-c13761719519/go.mod h1:FeLwcggjj3mMvU+oOTbSwawSJRM1uh48EjtB4UJZlP0=
golang.org/x/image v0.0.0-20201208152932-35266b937fa6/go.mod h1:FeLwcggjj3mMvU+oOTbSwawSJRM1uh48EjtB4UJZlP0=
golang.org/x/image v0.0.0-20210216034530-4410531fe030/go.mod h1:FeLwcggjj3mMvU+oOTbSwawSJRM1uh48EjtB4UJZlP0=
golang.org/x/image v0.0.0-20210607152325-775e3b0c77b9/go.mod h1:023OzeP/+EPmXeapQh35lcL3II3LrY8Ic+EFFKVhULM=
golang.org/x/image v0.0.0-20210628002857-a66eb6448b8d/go.mod h1:023OzeP/+EPmXeapQh35lcL3II3LrY8Ic+EFFKVhULM=
golang.org/x/image v0.0.0-20211028202545-6944b10bf410/go.mod h1:023OzeP/+EPmXeapQh35lcL3II3LrY8Ic+EFFKVhULM=
golang.org/x/image v0.0.0-20220302094943-723b81ca9867/go.mod h1:023OzeP/+EPmXeapQh35lcL3II3LrY8Ic+EFFKVhULM=
golang.org/x/lint v0.0.0-20181026193005-c67002cb31c3/go.mod h1:UVdnD1Gm6xHRNCYTkRU2/jEulfH38KcIWyp/GAMgvoE=
golang.org/x/lint v0.0.0-20190227174305-5b3e6a55c961/go.mod h1:wehouNa3lNwaWXcvxsM5YxQ5yQlVC4a0KAMCusXpPoU=
golang.org/x/lint v0.0.0-20190301231843-5614ed5bae6f/go.mod h1:UVdnD1Gm6xHRNCYTkRU2/jEulfH38KcIWyp/GAMgvoE=
golang.org/x/lint v0.0.0-20190313153728-d0100b6bd8b3/go.mod h1:6SW0HCj/g11FgYtHlgUYUwCkIfeOF89ocIRzGO/8vkc=
golang.org/x/lint v0.0.0-20190409202823-959b441ac422/go.mod h1:6SW0HCj/g11FgYtHlgUYUwCkIfeOF89ocIRzGO/8vkc=
golang.org/x/lint v0.0.0-20190909230951-414d861bb4ac/go.mod h1:6SW0HCj/g11FgYtHlgUYUwCkIfeOF89ocIRzGO/8vkc=
golang.org/x/lint v0.0.0-20190930215403-16217165b5de/go.mod h1:6SW0HCj/g11FgYtHlgUYUwCkIfeOF89ocIRzGO/8vkc=
golang.org/x/lint v0.0.0-20191125180803-fdd1cda4f05f/go.mod h1:5qLYkcX4OjUUV8bRuDixDT3tpyyb+LUpUlRWLxfhWrs=
golang.org/x/lint v0.0.0-20200130185559-910be7a94367/go.mod h1:3xt1FjdF8hUf6vQPIChWIBhFzV8gjjsPE/fR3IyQdNY=
golang.org/x/lint v0.0.0-20200302205851-738671d3881b/go.mod h1:3xt1FjdF8hUf6vQPIChWIBhFzV8gjjsPE/fR3IyQdNY=
golang.org/x/lint v0.0.0-20201208152925-83fdc39ff7b5/go.mod h1:3xt1FjdF8hUf6vQPIChWIBhFzV8gjjsPE/fR3IyQdNY=
golang.org/x/lint v0.0.0-20210508222113-6edffad5e616/go.mod h1:3xt1FjdF8hUf6vQPIChWIBhFzV8gjjsPE/fR3IyQdNY=
golang.org/x/mobile v0.0.0-20190312151609-d3739f865fa6/go.mod h1:z+o9i4GpDbdi3rU15maQ/Ox0txvL9dWGYEHz965HBQE=
golang.org/x/mobile v0.0.0-20190719004257-d2bd2a29d028/go.mod h1:E/iHnbuqvinMTCcRqshq8CkpyQDoeVncDDYHnLhea+o=
golang.org/x/mod v0.0.0-20190513183733-4bf6d317e70e/go.mod h1:mXi4GBBbnImb6dmsKGUJ2LatrhH/nqhxcFungHvyanc=
golang.org/x/mod v0.1.0/go.mod h1:0QHyrYULN0/3qlju5TqG8bIK38QM8yzMo5ekMj3DlcY=
golang.org/x/mod v0.1.1-0.20191105210325-c90efee705ee/go.mod h1:QqPTAvyqsEbceGzBzNggFXnrqF1CaUcvgkdR5Ot7KZg=
golang.org/x/mod v0.1.1-0.20191107180719-034126e5016b/go.mod h1:QqPTAvyqsEbceGzBzNggFXnrqF1CaUcvgkdR5Ot7KZg=
golang.org/x/mod v0.2.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/mod v0.3.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/mod v0.4.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/mod v0.4.1/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/mod v0.4.2/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/mod v0.5.0/go.mod h1:5OXOZSfqPIIbmVBIIKWRFfZjPR0E5r58TLhUjH0a2Ro=
golang.org/x/mod v0.5.1/go.mod h1:5OXOZSfqPIIbmVBIIKWRFfZjPR0E5r58TLhUjH0a2Ro=
golang.org/x/mod v0.6.0-dev.0.20220419223038-86c51ed26bb4/go.mod h1:jJ57K6gSWd91VN4djpZkiMVwK6gcyfeH4XE8wZrZaV4=
golang.org/x/mod v0.7.0/go.mod h1:iBbtSCu2XBx23ZKBPSOrRkjjQPZFPuis4dIYUhu/chs=
golang.org/x/mod v0.8.0/go.mod h1:iBbtSCu2XBx23ZKBPSOrRkjjQPZFPuis4dIYUhu/chs=
golang.org/x/mod v0.9.0/go.mod h1:iBbtSCu2XBx23ZKBPSOrRkjjQPZFPuis4dIYUhu/chs=
golang.org/x/mod v0.29.0 h1:HV8lRxZC4l2cr3Zq1LvtOsi/ThTgWnUk/y64QSs8GwA=
golang.org/x/mod v0.29.0/go.mod h1:NyhrlYXJ2H4eJiRy/WDBO6HMqZQ6q9nk4JzS3NuCK+w=
golang.org/x/net v0.0.0-20180218175443-cbe0f9307d01/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20180724234803-3673e40ba225/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20180826012351-8a410e7b638d/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20180906233101-161cd47e91fd/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20181108082009-03003ca0c849/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190108225652-1e06a53dbb7e/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190213061140-3a22650c66bd/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190225153610-fe579d43d832/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190311183353-d8887717615a/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190404232315-eb5bcb51f2a3/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190501004415-9ce7a6920f09/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190503192946-f4e77d36d62c/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190603091049-60506f45cf65/go.mod h1:HSz+uSET+XFnRR8LxR5pz3Of3rY3CfYBVs4xY44aLks=
golang.org/x/net v0.0.0-20190620200207-3b0461eec859/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20190628185345-da137c7871d7/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20190724013045-ca1201d0de80/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20190813141303-74dc4d7220e7/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20191209160850-c0dbc17a3553/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200114155413-6afb5195e5aa/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200202094626-16171245cfb2/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200222125558-5a598a2470a0/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200226121028-0de0cce0169b/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200301022130-244492dfa37a/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200324143707-d3edc9973b7e/go.mod h1:qpuaurCH72eLCgpAm/N6yyVIVM9cpaDIP3A8BGJEC5A=
golang.org/x/net v0.0.0-20200501053045-e0ff5e5a1de5/go.mod h1:qpuaurCH72eLCgpAm/N6yyVIVM9cpaDIP3A8BGJEC5A=
golang.org/x/net v0.0.0-20200506145744-7e3656a0809f/go.mod h1:qpuaurCH72eLCgpAm/N6yyVIVM9cpaDIP3A8BGJEC5A=
golang.org/x/net v0.0.0-20200513185701-a91f0712d120/go.mod h1:qpuaurCH72eLCgpAm/N6yyVIVM9cpaDIP3A8BGJEC5A=
golang.org/x/net v0.0.0-20200520004742-59133d7f0dd7/go.mod h1:qpuaurCH72eLCgpAm/N6yyVIVM9cpaDIP3A8BGJEC5A=
golang.org/x/net v0.0.0-20200520182314-0ba52f642ac2/go.mod h1:qpuaurCH72eLCgpAm/N6yyVIVM9cpaDIP3A8BGJEC5A=
golang.org/x/net v0.0.0-20200625001655-4c5254603344/go.mod h1:/O7V0waA8r7cgGh81Ro3o1hOxt32SMVPicZroKQ2sZA=
golang.org/x/net v0.0.0-20200707034311-ab3426394381/go.mod h1:/O7V0waA8r7cgGh81Ro3o1hOxt32SMVPicZroKQ2sZA=
golang.org/x/net v0.0.0-20200822124328-c89045814202/go.mod h1:/O7V0waA8r7cgGh81Ro3o1hOxt32SMVPicZroKQ2sZA=
golang.org/x/net v0.0.0-20201010224723-4f7140c49acb/go.mod h1:sp8m0HH+o8qH0wwXwYZr8TS3Oi6o0r6Gce1SSxlDquU=
golang.org/x/net v0.0.0-20201021035429-f5854403a974/go.mod h1:sp8m0HH+o8qH0wwXwYZr8TS3Oi6o0r6Gce1SSxlDquU=
golang.org/x/net v0.0.0-20201031054903-ff519b6c9102/go.mod h1:sp8m0HH+o8qH0wwXwYZr8TS3Oi6o0r6Gce1SSxlDquU=
golang.org/x/net v0.0.0-20201110031124-69a78807bb2b/go.mod h1:sp8m0HH+o8qH0wwXwYZr8TS3Oi6o0r6Gce1SSxlDquU=
golang.org/x/net v0.0.0-20201209123823-ac852fbbde11/go.mod h1:m0MpNAwzfU5UDzcl9v0D8zg8gWTRqZa9RBIspLL5mdg=
golang.org/x/net v0.0.0-20201224014010-6772e930b67b/go.mod h1:m0MpNAwzfU5UDzcl9v0D8zg8gWTRqZa9RBIspLL5mdg=
golang.org/x/net v0.0.0-20210119194325-5f4716e94777/go.mod h1:m0MpNAwzfU5UDzcl9v0D8zg8gWTRqZa9RBIspLL5mdg=
golang.org/x/net v0.0.0-20210226172049-e18ecbb05110/go.mod h1:m0MpNAwzfU5UDzcl9v0D8zg8gWTRqZa9RBIspLL5mdg=
golang.org/x/net v0.0.0-20210316092652-d523dce5a7f4/go.mod h1:RBQZq4jEuRlivfhVLdyRGr576XBO4/greRjx4P4O3yc=
golang.org/x/net v0.0.0-20210405180319-a5a99cb37ef4/go.mod h1:p54w0d4576C0XHj96bSt6lcn1PtDYWL6XObtHCRCNQM=
golang.org/x/net v0.0.0-20210428140749-89ef3d95e781/go.mod h1:OJAsFXCWl8Ukc7SiCT/9KSuxbyM7479/AVlXFRxuMCk=
golang.org/x/net v0.0.0-20210503060351-7fd8e65b6420/go.mod h1:9nx3DQGgdP8bBQD5qxJ1jj9UTztislL4KSBs9R2vV5Y=
golang.org/x/net v0.0.0-20210813160813-60bc85c4be6d/go.mod h1:9nx3DQGgdP8bBQD5qxJ1jj9UTztislL4KSBs9R2vV5Y=
golang.org/x/net v0.0.0-20211015210444-4f30a5c0130f/go.mod h1:9nx3DQGgdP8bBQD5qxJ1jj9UTztislL4KSBs9R2vV5Y=
golang.org/x/net v0.0.0-20211112202133-69e39bad7dc2/go.mod h1:9nx3DQGgdP8bBQD5qxJ1jj9UTztislL4KSBs9R2vV5Y=
golang.org/x/net v0.0.0-20220127200216-cd36cc0744dd/go.mod h1:CfG3xpIq0wQ8r1q4Su4UZFWDARRcnwPjda9FqA0JpMk=
golang.org/x/net v0.0.0-20220225172249-27dd8689420f/go.mod h1:CfG3xpIq0wQ8r1q4Su4UZFWDARRcnwPjda9FqA0JpMk=
golang.org/x/net v0.0.0-20220325170049-de3da57026de/go.mod h1:CfG3xpIq0wQ8r1q4Su4UZFWDARRcnwPjda9FqA0JpMk=
golang.org/x/net v0.0.0-20220412020605-290c469a71a5/go.mod h1:CfG3xpIq0wQ8r1q4Su4UZFWDARRcnwPjda9FqA0JpMk=
golang.org/x/net v0.0.0-20220425223048-2871e0cb64e4/go.mod h1:CfG3xpIq0wQ8r1q4Su4UZFWDARRcnwPjda9FqA0JpMk=
golang.org/x/net v0.0.0-20220607020251-c690dde0001d/go.mod h1:XRhObCWvk6IyKnWLug+ECip1KBveYUHfp+8e9klMJ9c=
golang.org/x/net v0.0.0-20220617184016-355a448f1bc9/go.mod h1:XRhObCWvk6IyKnWLug+ECip1KBveYUHfp+8e9klMJ9c=
golang.org/x/net v0.0.0-20220624214902-1bab6f366d9e/go.mod h1:XRhObCWvk6IyKnWLug+ECip1KBveYUHfp+8e9klMJ9c=
golang.org/x/net v0.0.0-20220722155237-a158d28d115b/go.mod h1:XRhObCWvk6IyKnWLug+ECip1KBveYUHfp+8e9klMJ9c=
golang.org/x/net v0.0.0-20220909164309-bea034e7d591/go.mod h1:YDH+HFinaLZZlnHAfSS6ZXJJ9M9t4Dl22yv3iI2vPwk=
golang.org/x/net v0.0.0-20221012135044-0b7e1fb9d458/go.mod h1:YDH+HFinaLZZlnHAfSS6ZXJJ9M9t4Dl22yv3iI2vPwk=
golang.org/x/net v0.0.0-20221014081412-f15817d10f9b/go.mod h1:YDH+HFinaLZZlnHAfSS6ZXJJ9M9t4Dl22yv3iI2vPwk=
golang.org/x/net v0.2.0/go.mod h1:KqCZLdyyvdV855qA2rE3GC2aiw5xGR5TEjj8smXukLY=
golang.org/x/net v0.4.0/go.mod h1:MBQ8lrhLObU/6UmLb4fmbmk5OcyYmqtbGd/9yIeKjEE=
golang.org/x/net v0.5.0/go.mod h1:DivGGAXEgPSlEBzxGzZI+ZLohi+xUj054jfeKui00ws=
golang.org/x/net v0.6.0/go.mod h1:2Tu9+aMcznHK/AK1HMvgo6xiTLG5rD5rZLDS+rp2Bjs=
golang.org/x/net v0.7.0/go.mod h1:2Tu9+aMcznHK/AK1HMvgo6xiTLG5rD5rZLDS+rp2Bjs=
golang.org/x/net v0.8.0/go.mod h1:QVkue5JL9kW//ek3r6jTKnTFis1tRmNAW2P1shuFdJc=
golang.org/x/net v0.9.0/go.mod h1:d48xBJpPfHeWQsugry2m+kC02ZBRGRgulfHnEXEuWns=
golang.org/x/net v0.47.0 h1:Mx+4dIFzqraBXUugkia1OOvlD6LemFo1ALMHjrXDOhY=
golang.org/x/net v0.47.0/go.mod h1:/jNxtkgq5yWUGYkaZGqo27cfGZ1c5Nen03aYrrKpVRU=
golang.org/x/oauth2 v0.0.0-20180227000427-d7d64896b5ff/go.mod h1:N/0e6XlmueqKjAGxoOufVs8QHGRruUQn6yWY3a++T0U=
golang.org/x/oauth2 v0.0.0-20180821212333-d2e6202438be/go.mod h1:N/0e6XlmueqKjAGxoOufVs8QHGRruUQn6yWY3a++T0U=
golang.org/x/oauth2 v0.0.0-20181106182150-f42d05182288/go.mod h1:N/0e6XlmueqKjAGxoOufVs8QHGRruUQn6yWY3a++T0U=
golang.org/x/oauth2 v0.0.0-20190226205417-e64efc72b421/go.mod h1:gOpvHmFTYa4IltrdGE7lF6nIHvwfUNPOp7c8zoXwtLw=
golang.org/x/oauth2 v0.0.0-20190604053449-0f29369cfe45/go.mod h1:gOpvHmFTYa4IltrdGE7lF6nIHvwfUNPOp7c8zoXwtLw=
golang.org/x/oauth2 v0.0.0-20191202225959-858c2ad4c8b6/go.mod h1:gOpvHmFTYa4IltrdGE7lF6nIHvwfUNPOp7c8zoXwtLw=
golang.org/x/oauth2 v0.0.0-20200107190931-bf48bf16ab8d/go.mod h1:gOpvHmFTYa4IltrdGE7lF6nIHvwfUNPOp7c8zoXwtLw=
golang.org/x/oauth2 v0.0.0-20200902213428-5d25da1a8d43/go.mod h1:KelEdhl1UZF7XfJ4dDtk6s++YSgaE7mD/BuKKDLBl4A=
golang.org/x/oauth2 v0.0.0-20201109201403-9fd604954f58/go.mod h1:KelEdhl1UZF7XfJ4dDtk6s++YSgaE7mD/BuKKDLBl4A=
golang.org/x/oauth2 v0.0.0-20201208152858-08078c50e5b5/go.mod h1:KelEdhl1UZF7XfJ4dDtk6s++YSgaE7mD/BuKKDLBl4A=
golang.org/x/oauth2 v0.0.0-20210218202405-ba52d332ba99/go.mod h1:KelEdhl1UZF7XfJ4dDtk6s++YSgaE7mD/BuKKDLBl4A=
golang.org/x/oauth2 v0.0.0-20210220000619-9bb904979d93/go.mod h1:KelEdhl1UZF7XfJ4dDtk6s++YSgaE7mD/BuKKDLBl4A=
golang.org/x/oauth2 v0.0.0-20210313182246-cd4f82c27b84/go.mod h1:KelEdhl1UZF7XfJ4dDtk6s++YSgaE7mD/BuKKDLBl4A=
golang.org/x/oauth2 v0.0.0-20210514164344-f6687ab2804c/go.mod h1:KelEdhl1UZF7XfJ4dDtk6s++YSgaE7mD/BuKKDLBl4A=
golang.org/x/oauth2 v0.0.0-20210628180205-a41e5a781914/go.mod h1:KelEdhl1UZF7XfJ4dDtk6s++YSgaE7mD/BuKKDLBl4A=
golang.org/x/oauth2 v0.0.0-20210805134026-6f1e6394065a/go.mod h1:KelEdhl1UZF7XfJ4dDtk6s++YSgaE7mD/BuKKDLBl4A=
golang.org/x/oauth2 v0.0.0-20210819190943-2bc19b11175f/go.mod h1:KelEdhl1UZF7XfJ4dDtk6s++YSgaE7mD/BuKKDLBl4A=
golang.org/x/oauth2 v0.0.0-20211104180415-d3ed0bb246c8/go.mod h1:KelEdhl1UZF7XfJ4dDtk6s++YSgaE7mD/BuKKDLBl4A=
golang.org/x/oauth2 v0.0.0-20220223155221-ee480838109b/go.mod h1:DAh4E804XQdzx2j+YRIaUnCqCV2RuMz24cGBJ5QYIrc=
golang.org/x/oauth2 v0.0.0-20220309155454-6242fa91716a/go.mod h1:DAh4E804XQdzx2j+YRIaUnCqCV2RuMz24cGBJ5QYIrc=
golang.org/x/oauth2 v0.0.0-20220411215720-9780585627b5/go.mod h1:DAh4E804XQdzx2j+YRIaUnCqCV2RuMz24cGBJ5QYIrc=
golang.org/x/oauth2 v0.0.0-20220608161450-d0670ef3b1eb/go.mod h1:jaDAt6Dkxork7LmZnYtzbRWj0W47D86a3TGe0YHBvmE=
golang.org/x/oauth2 v0.0.0-20220622183110-fd043fe589d2/go.mod h1:jaDAt6Dkxork7LmZnYtzbRWj0W47D86a3TGe0YHBvmE=
golang.org/x/oauth2 v0.0.0-20220822191816-0ebed06d0094/go.mod h1:h4gKUeWbJ4rQPri7E0u6Gs4e9Ri2zaLxzw5DI5XGrYg=
golang.org/x/oauth2 v0.0.0-20220909003341-f21342109be1/go.mod h1:h4gKUeWbJ4rQPri7E0u6Gs4e9Ri2zaLxzw5DI5XGrYg=
golang.org/x/oauth2 v0.0.0-20221006150949-b44042a4b9c1/go.mod h1:h4gKUeWbJ4rQPri7E0u6Gs4e9Ri2zaLxzw5DI5XGrYg=
golang.org/x/oauth2 v0.0.0-20221014153046-6fdb5e3db783/go.mod h1:h4gKUeWbJ4rQPri7E0u6Gs4e9Ri2zaLxzw5DI5XGrYg=
golang.org/x/oauth2 v0.4.0/go.mod h1:RznEsdpjGAINPTOF0UH/t+xJ75L18YO3Ho6Pyn+uRec=
golang.org/x/oauth2 v0.5.0/go.mod h1:9/XBHVqLaWO3/BRHs5jbpYCnOZVjj5V0ndyaAM7KB4I=
golang.org/x/oauth2 v0.6.0/go.mod h1:ycmewcwgD4Rpr3eZJLSB4Kyyljb3qDh40vJ8STE5HKw=
golang.org/x/oauth2 v0.7.0/go.mod h1:hPLQkd9LyjfXTiRohC/41GhcFqxisoUQ99sCUOHO9x4=
golang.org/x/oauth2 v0.30.0 h1:dnDm7JmhM45NNpd8FDDeLhK6FwqbOf4MLCM9zb1BOHI=
golang.org/x/oauth2 v0.30.0/go.mod h1:B++QgG3ZKulg6sRPGD/mqlHQs5rB3Ml9erfeDY7xKlU=
golang.org/x/sync v0.0.0-20180314180146-1d60e4601c6f/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20181108010431-42b317875d0f/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20181221193216-37e7f081c4d4/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190227155943-e225da77a7e6/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190911185100-cd5d95a43a6e/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20200317015054-43a5402ce75a/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20200625203802-6e8e738ad208/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20201020160332-67f06af15bc9/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20201207232520-09787c993a3a/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20210220032951-036812b2e83c/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20220601150217-0de741cfad7f/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20220722155255-886fb9371eb4/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20220819030929-7fc1605a5dde/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20220929204114-8fcdb60fdcc0/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.1.0/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.18.0 h1:kr88TuHDroi+UVf+0hZnirlk8o8T+4MrK6mr60WkH/I=
golang.org/x/sync v0.18.0/go.mod h1:9KTHXmSnoGruLpwFjVSX0lNNA75CykiMECbovNTZqGI=
golang.org/x/sys v0.0.0-20180224232135-f6cff0780e54/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20180830151530-49385e6e1522/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20180905080454-ebe1bf3edb33/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20180909124046-d0be0721c37e/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190222072716-a9d3bda3a223/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190312061237-fead79001313/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190403152447-81d4e9dc473e/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190412213103-97732733099d/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190422165155-953cdadca894/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190502145724-3ef323f4f1fd/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190507160741-ecd444e8653b/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190606165138-5da285871e9c/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190624142023-c5567b49c5d0/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190726091711-fc99dfbffb4e/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190813064441-fde4db37ae7a/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190826190057-c7b8b68b1456/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190904154756-749cb33beabd/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191001151750-bb3f8db39f24/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191005200804-aed5e4c7ecf9/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191026070338-33540a1f6037/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191120155948-bd437916bb0e/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191204072324-ce4227a45e2e/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191228213918-04cbcbbfeed8/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200113162924-86b910548bc1/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200116001909-b77594299b42/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200122134326-e047566fdf82/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200202164722-d101bd2416d5/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200212091648-12a6c2dcc1e4/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200223170610-d5e6a3e2c0ae/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200302150141-5c8b2ff67527/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200323222414-85ca7c5b95cd/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200331124033-c3d80250170d/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200501052902-10377860bb8e/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200511232937-7e40ca221e25/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200515095857-1151b9dac4a9/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200523222454-059865788121/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200803210538-64077c9b5642/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200905004654-be1d3432aa8f/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200930185726-fdedc70b468f/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20201119102817-f84b799fce68/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20201201145000-ef89a241ccb3/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210104204734-6f8348627aad/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210112080510-489259a85091/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210119212857-b64e53b001e4/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210124154548-22da62e12c0c/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210220050731-9a76102bfb43/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210225134936-a50acf3fe073/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210304124612-50617c2ba197/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210305230114-8fe3ee5dd75b/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210315160823-c6e025ad8005/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210320140829-1e4c9ba3b0c4/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210330210617-4fbd30eecc44/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210423082822-04245dca01da/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210423185535-09eb48e85fd7/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210510120138-977fb7262007/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210514084401-e8d321eab015/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210603125802-9665404d3644/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210615035016-665e8c7367d1/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210616045830-e2b7044e8c71/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210616094352-59db8d763f22/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210630005230-0f9fa26af87c/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210806184541-e5e7981a1069/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210816183151-1e6c022a8912/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210819135213-f52c844e1c1c/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210823070655-63515b42dcdf/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210908233432-aa78b53d3365/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20211007075335-d3039528d8ac/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20211019181941-9d821ace8654/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20211124211545-fe61309f8881/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20211210111614-af8b64212486/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20211216021012-1d35b9e2eb4e/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220128215802-99c3d69c2c27/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220209214540-3681064d5158/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220224120231-95c6836cb0e7/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220227234510-4e6760a101f9/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220328115105-d36c6a25d886/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220412211240-33da011f77ad/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220502124256-b6088ccd6cba/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220503163025-988cb79eb6c6/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220520151302-bc2c85ada10a/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220610221304-9f5ed59c137d/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220615213510-4f61da869c0c/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220624220833-87e55d714810/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220715151400-c0bba94af5f8/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220722155257-8c9f86f7a55f/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220728004956-3c1f35247d10/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220811171246-fbc7d0a398ab/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220829200755-d48e67d00261/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.2.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.3.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.4.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.5.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.6.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.7.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.40.0 h1:DBZZqJ2Rkml6QMQsZywtnjnnGvHza6BTfYFWY9kjEWQ=
golang.org/x/sys v0.40.0/go.mod h1:OgkHotnGiDImocRcuBABYBEXf8A9a87e/uXjp9XT3ks=
golang.org/x/telemetry v0.0.0-20251008203120-078029d740a8 h1:LvzTn0GQhWuvKH/kVRS3R3bVAsdQWI7hvfLHGgh9+lU=
golang.org/x/telemetry v0.0.0-20251008203120-078029d740a8/go.mod h1:Pi4ztBfryZoJEkyFTI5/Ocsu2jXyDr6iSdgJiYE/uwE=
golang.org/x/term v0.0.0-20201117132131-f5c789dd3221/go.mod h1:Nr5EML6q2oocZ2LXRh80K7BxOlk5/8JxuGnuhpl+muw=
golang.org/x/term v0.0.0-20201126162022-7de9c90e9dd1/go.mod h1:bj7SfCRtBDWHUb9snDiAeCFNEtKQo2Wmx5Cou7ajbmo=
golang.org/x/term v0.0.0-20210927222741-03fcf44c2211/go.mod h1:jbD1KX2456YbFQfuXm/mYQcufACuNUgVhRMnK/tPxf8=
golang.org/x/term v0.2.0/go.mod h1:TVmDHMZPmdnySmBfhjOoOdhjzdE1h4u1VwSiw2l1Nuc=
golang.org/x/term v0.3.0/go.mod h1:q750SLmJuPmVoN1blW3UFBPREJfb1KmY3vwxfr+nFDA=
golang.org/x/term v0.4.0/go.mod h1:9P2UbLfCdcvo3p/nzKvsmas4TnlujnuoV9hGgYzW1lQ=
golang.org/x/term v0.5.0/go.mod h1:jMB1sMXY+tzblOD4FWmEbocvup2/aLOaQEp7JmGp78k=
golang.org/x/term v0.6.0/go.mod h1:m6U89DPEgQRMq3DNkDClhWw02AUbt2daBVO4cn4Hv9U=
golang.org/x/term v0.7.0/go.mod h1:P32HKFT3hSsZrRxla30E9HqToFYAQPCMs/zFMBUFqPY=
golang.org/x/term v0.37.0 h1:8EGAD0qCmHYZg6J17DvsMy9/wJ7/D/4pV/wfnld5lTU=
golang.org/x/term v0.37.0/go.mod h1:5pB4lxRNYYVZuTLmy8oR2BH8dflOR+IbTYFD8fi3254=
golang.org/x/text v0.0.0-20170915032832-14c0d48ead0c/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.1-0.20180807135948-17ff2d5776d2/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.2/go.mod h1:bEr9sfX3Q8Zfm5fL9x+3itogRgK3+ptLWKqgva+5dAk=
golang.org/x/text v0.3.3/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.4/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.5/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.6/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.7/go.mod h1:u+2+/6zg+i71rQMx5EYifcz6MCKuco9NR6JIITiCfzQ=
golang.org/x/text v0.3.8/go.mod h1:E6s5w1FMmriuDzIBO73fBruAKo1PCIq6d2Q6DHfQ8WQ=
golang.org/x/text v0.4.0/go.mod h1:mrYo+phRRbMaCq/xk9113O4dZlRixOauAjOtrjsXDZ8=
golang.org/x/text v0.5.0/go.mod h1:mrYo+phRRbMaCq/xk9113O4dZlRixOauAjOtrjsXDZ8=
golang.org/x/text v0.6.0/go.mod h1:mrYo+phRRbMaCq/xk9113O4dZlRixOauAjOtrjsXDZ8=
golang.org/x/text v0.7.0/go.mod h1:mrYo+phRRbMaCq/xk9113O4dZlRixOauAjOtrjsXDZ8=
golang.org/x/text v0.8.0/go.mod h1:e1OnstbJyHTd6l/uOt8jFFHp6TRDWZR/bV3emEE/zU8=
golang.org/x/text v0.9.0/go.mod h1:e1OnstbJyHTd6l/uOt8jFFHp6TRDWZR/bV3emEE/zU8=
golang.org/x/text v0.31.0 h1:aC8ghyu4JhP8VojJ2lEHBnochRno1sgL6nEi9WGFGMM=
golang.org/x/text v0.31.0/go.mod h1:tKRAlv61yKIjGGHX/4tP1LTbc13YSec1pxVEWXzfoeM=
golang.org/x/time v0.0.0-20181108054448-85acf8d2951c/go.mod h1:tRJNPiyCQ0inRvYxbN9jk5I+vvW/OXSQhTDSoE431IQ=
golang.org/x/time v0.0.0-20190308202827-9d24e82272b4/go.mod h1:tRJNPiyCQ0inRvYxbN9jk5I+vvW/OXSQhTDSoE431IQ=
golang.org/x/time v0.0.0-20191024005414-555d28b269f0/go.mod h1:tRJNPiyCQ0inRvYxbN9jk5I+vvW/OXSQhTDSoE431IQ=
golang.org/x/time v0.0.0-20220922220347-f3bd1da661af/go.mod h1:tRJNPiyCQ0inRvYxbN9jk5I+vvW/OXSQhTDSoE431IQ=
golang.org/x/time v0.1.0/go.mod h1:tRJNPiyCQ0inRvYxbN9jk5I+vvW/OXSQhTDSoE431IQ=
golang.org/x/time v0.3.0/go.mod h1:tRJNPiyCQ0inRvYxbN9jk5I+vvW/OXSQhTDSoE431IQ=
golang.org/x/time v0.12.0 h1:ScB/8o8olJvc+CQPWrK3fPZNfh7qgwCrY0zJmoEQLSE=
golang.org/x/time v0.12.0/go.mod h1:CDIdPxbZBQxdj6cxyCIdrNogrJKMJ7pr37NYpMcMDSg=
golang.org/x/tools v0.0.0-20180525024113-a5b4c53f6e8b/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20190114222345-bf090417da8b/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20190206041539-40960b6deb8e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20190226205152-f727befe758c/go.mod h1:9Yl7xja0Znq3iFh3HoIrodX9oNMXvdceNzlUR8zjMvY=
golang.org/x/tools v0.0.0-20190311212946-11955173bddd/go.mod h1:LCzVGOaR6xXOjkQ3onu1FJEFr0SW1gC7cKk1uF8kGRs=
golang.org/x/tools v0.0.0-20190312151545-0bb0c0a6e846/go.mod h1:LCzVGOaR6xXOjkQ3onu1FJEFr0SW1gC7cKk1uF8kGRs=
golang.org/x/tools v0.0.0-20190312170243-e65039ee4138/go.mod h1:LCzVGOaR6xXOjkQ3onu1FJEFr0SW1gC7cKk1uF8kGRs=
golang.org/x/tools v0.0.0-20190425150028-36563e24a262/go.mod h1:RgjU9mgBXZiqYHBnxXauZ1Gv1EHHAz9KjViQ78xBX0Q=
golang.org/x/tools v0.0.0-20190425163242-31fd60d6bfdc/go.mod h1:RgjU9mgBXZiqYHBnxXauZ1Gv1EHHAz9KjViQ78xBX0Q=
golang.org/x/tools v0.0.0-20190506145303-2d16b83fe98c/go.mod h1:RgjU9mgBXZiqYHBnxXauZ1Gv1EHHAz9KjViQ78xBX0Q=
golang.org/x/tools v0.0.0-20190524140312-2c0ae7006135/go.mod h1:RgjU9mgBXZiqYHBnxXauZ1Gv1EHHAz9KjViQ78xBX0Q=
golang.org/x/tools v0.0.0-20190531172133-b3315ee88b7d/go.mod h1:/rFqwRUd4F7ZHNgwSSTFct+R/Kf4OFW1sUzUTQQTgfc=
golang.org/x/tools v0.0.0-20190606124116-d0a3d012864b/go.mod h1:/rFqwRUd4F7ZHNgwSSTFct+R/Kf4OFW1sUzUTQQTgfc=
golang.org/x/tools v0.0.0-20190621195816-6e04913cbbac/go.mod h1:/rFqwRUd4F7ZHNgwSSTFct+R/Kf4OFW1sUzUTQQTgfc=
golang.org/x/tools v0.0.0-20190628153133-6cdbf07be9d0/go.mod h1:/rFqwRUd4F7ZHNgwSSTFct+R/Kf4OFW1sUzUTQQTgfc=
golang.org/x/tools v0.0.0-20190816200558-6889da9d5479/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20190823170909-c4a336ef6a2f/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20190911174233-4f2ddba30aff/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20190927191325-030b2cf1153e/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20191012152004-8de300cfc20a/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20191029041327-9cc4af7d6b2c/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20191029190741-b9c20aec41a5/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20191113191852-77e3bb0ad9e7/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20191115202509-3a792d9c32b2/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20191119224855-298f0cb1881e/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20191125144606-a911d9008d1f/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20191130070609-6e064ea0cf2d/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20191216173652-a0e659d51361/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/tools v0.0.0-20191227053925-7b8e75db28f4/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/tools v0.0.0-20200103221440-774c71fcf114/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/tools v0.0.0-20200117161641-43d50277825c/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/tools v0.0.0-20200122220014-bf1340f18c4a/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/tools v0.0.0-20200130002326-2f3ba24bd6e7/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/tools v0.0.0-20200204074204-1cc6d1ef6c74/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/tools v0.0.0-20200207183749-b753a1ba74fa/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/tools v0.0.0-20200212150539-ea181f53ac56/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/tools v0.0.0-20200224181240-023911ca70b2/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/tools v0.0.0-20200227222343-706bc42d1f0d/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/tools v0.0.0-20200304193943-95d2e580d8eb/go.mod h1:o4KQGtdN14AW+yjsvvwRTJJuXz8XRtIHtEnmAXLyFUw=
golang.org/x/tools v0.0.0-20200312045724-11d5b4c81c7d/go.mod h1:o4KQGtdN14AW+yjsvvwRTJJuXz8XRtIHtEnmAXLyFUw=
golang.org/x/tools v0.0.0-20200331025713-a30bf2db82d4/go.mod h1:Sl4aGygMT6LrqrWclx+PTx3U+LnKx/seiNR+3G19Ar8=
golang.org/x/tools v0.0.0-20200501065659-ab2804fb9c9d/go.mod h1:EkVYQZoAsY45+roYkvgYkIh4xh/qjgUK9TdY2XT94GE=
golang.org/x/tools v0.0.0-20200512131952-2bc93b1c0c88/go.mod h1:EkVYQZoAsY45+roYkvgYkIh4xh/qjgUK9TdY2XT94GE=
golang.org/x/tools v0.0.0-20200515010526-7d3b6ebf133d/go.mod h1:EkVYQZoAsY45+roYkvgYkIh4xh/qjgUK9TdY2XT94GE=
golang.org/x/tools v0.0.0-20200618134242-20370b0cb4b2/go.mod h1:EkVYQZoAsY45+roYkvgYkIh4xh/qjgUK9TdY2XT94GE=
golang.org/x/tools v0.0.0-20200619180055-7c47624df98f/go.mod h1:EkVYQZoAsY45+roYkvgYkIh4xh/qjgUK9TdY2XT94GE=
golang.org/x/tools v0.0.0-20200729194436-6467de6f59a7/go.mod h1:njjCfa9FT2d7l9Bc6FUM5FLjQPp3cFF28FI3qnDFljA=
golang.org/x/tools v0.0.0-20200804011535-6c149bb5ef0d/go.mod h1:njjCfa9FT2d7l9Bc6FUM5FLjQPp3cFF28FI3qnDFljA=
golang.org/x/tools v0.0.0-20200825202427-b303f430e36d/go.mod h1:njjCfa9FT2d7l9Bc6FUM5FLjQPp3cFF28FI3qnDFljA=
golang.org/x/tools v0.0.0-20200904185747-39188db58858/go.mod h1:Cj7w3i3Rnn0Xh82ur9kSqwfTHTeVxaDqrfMjpcNT6bE=
golang.org/x/tools v0.0.0-20201110124207-079ba7bd75cd/go.mod h1:emZCQorbCU4vsT4fOWvOPXz4eW1wZW4PmDk9uLelYpA=
golang.org/x/tools v0.0.0-20201124115921-2c860bdd6e78/go.mod h1:emZCQorbCU4vsT4fOWvOPXz4eW1wZW4PmDk9uLelYpA=
golang.org/x/tools v0.0.0-20201201161351-ac6f37ff4c2a/go.mod h1:emZCQorbCU4vsT4fOWvOPXz4eW1wZW4PmDk9uLelYpA=
golang.org/x/tools v0.0.0-20201208233053-a543418bbed2/go.mod h1:emZCQorbCU4vsT4fOWvOPXz4eW1wZW4PmDk9uLelYpA=
golang.org/x/tools v0.0.0-20201224043029-2b0845dc783e/go.mod h1:emZCQorbCU4vsT4fOWvOPXz4eW1wZW4PmDk9uLelYpA=
golang.org/x/tools v0.0.0-20210105154028-b0ab187a4818/go.mod h1:emZCQorbCU4vsT4fOWvOPXz4eW1wZW4PmDk9uLelYpA=
golang.org/x/tools v0.0.0-20210106214847-113979e3529a/go.mod h1:emZCQorbCU4vsT4fOWvOPXz4eW1wZW4PmDk9uLelYpA=
golang.org/x/tools v0.0.0-20210108195828-e2f9c7f1fc8e/go.mod h1:emZCQorbCU4vsT4fOWvOPXz4eW1wZW4PmDk9uLelYpA=
golang.org/x/tools v0.1.0/go.mod h1:xkSsbof2nBLbhDlRMhhhyNLN/zl3eTqcnHD5viDpcZ0=
golang.org/x/tools v0.1.1/go.mod h1:o0xws9oXOQQZyjljx8fwUC0k7L1pTE6eaCbjGeHmOkk=
golang.org/x/tools v0.1.2/go.mod h1:o0xws9oXOQQZyjljx8fwUC0k7L1pTE6eaCbjGeHmOkk=
golang.org/x/tools v0.1.3/go.mod h1:o0xws9oXOQQZyjljx8fwUC0k7L1pTE6eaCbjGeHmOkk=
golang.org/x/tools v0.1.4/go.mod h1:o0xws9oXOQQZyjljx8fwUC0k7L1pTE6eaCbjGeHmOkk=
golang.org/x/tools v0.1.5/go.mod h1:o0xws9oXOQQZyjljx8fwUC0k7L1pTE6eaCbjGeHmOkk=
golang.org/x/tools v0.1.9/go.mod h1:nABZi5QlRsZVlzPpHl034qft6wpY4eDcsTt5AaioBiU=
golang.org/x/tools v0.1.12/go.mod h1:hNGJHUnrk76NpqgfD5Aqm5Crs+Hm0VOH/i9J2+nxYbc=
golang.org/x/tools v0.3.0/go.mod h1:/rWhSS2+zyEVwoJf8YAX6L2f0ntZ7Kn/mGgAWcipA5k=
golang.org/x/tools v0.6.0/go.mod h1:Xwgl3UAJ/d3gWutnCtw505GrjyAbvKui8lOU390QaIU=
golang.org/x/tools v0.7.0/go.mod h1:4pg6aUX35JBAogB10C9AtvVL+qowtN4pT3CGSQex14s=
golang.org/x/tools v0.38.0 h1:Hx2Xv8hISq8Lm16jvBZ2VQf+RLmbd7wVUsALibYI/IQ=
golang.org/x/tools v0.38.0/go.mod h1:yEsQ/d/YK8cjh0L6rZlY8tgtlKiBNTL14pGDJPJpYQs=
golang.org/x/tools/godoc v0.1.0-deprecated h1:o+aZ1BOj6Hsx/GBdJO/s815sqftjSnrZZwyYTHODvtk=
golang.org/x/tools/godoc v0.1.0-deprecated/go.mod h1:qM63CriJ961IHWmnWa9CjZnBndniPt4a3CK0PVB9bIg=
golang.org/x/xerrors v0.0.0-20190410155217-1f06c39b4373/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20190513163551-3ee3066db522/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20190717185122-a985d3407aa7/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191011141410-1b5146add898/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20200804184101-5ec99f83aff1/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20220411194840-2f41105eb62f/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20220517211312-f3a8303e98df/go.mod h1:K8+ghG5WaK9qNqU5K3HdILfMLy1f3aNYFI/wnl100a8=
golang.org/x/xerrors v0.0.0-20220609144429-65e65417b02f/go.mod h1:K8+ghG5WaK9qNqU5K3HdILfMLy1f3aNYFI/wnl100a8=
golang.org/x/xerrors v0.0.0-20220907171357-04be3eba64a2/go.mod h1:K8+ghG5WaK9qNqU5K3HdILfMLy1f3aNYFI/wnl100a8=
golang.org/x/xerrors v0.0.0-20231012003039-104605ab7028 h1:+cNy6SZtPcJQH3LJVLOSmiC7MMxXNOb3PU/VUEz+EhU=
golang.org/x/xerrors v0.0.0-20231012003039-104605ab7028/go.mod h1:NDW/Ps6MPRej6fsCIbMTohpP40sJ/P/vI1MoTEGwX90=
gonum.org/v1/gonum v0.0.0-20180816165407-929014505bf4/go.mod h1:Y+Yx5eoAFn32cQvJDxZx5Dpnq+c3wtXuadVZAcxbbBo=
gonum.org/v1/gonum v0.8.2/go.mod h1:oe/vMfY3deqTw+1EZJhuvEW2iwGF1bW9wwu7XCu0+v0=
gonum.org/v1/gonum v0.9.3/go.mod h1:TZumC3NeyVQskjXqmyWt4S3bINhy7B4eYwW69EbyX+0=
gonum.org/v1/gonum v0.11.0 h1:f1IJhK4Km5tBJmaiJXtk/PkL4cdVX6J+tGiM187uT5E=
gonum.org/v1/gonum v0.11.0/go.mod h1:fSG4YDCxxUZQJ7rKsQrj0gMOg00Il0Z96/qMA4bVQhA=
gonum.org/v1/netlib v0.0.0-20190313105609-8cb42192e0e0/go.mod h1:wa6Ws7BG/ESfp6dHfk7C6KdzKA7wR7u/rKwOGE66zvw=
gonum.org/v1/plot v0.0.0-20190515093506-e2840ee46a6b/go.mod h1:Wt8AAjI+ypCyYX3nZBvf6cAIx93T+c/OS2HFAYskSZc=
gonum.org/v1/plot v0.9.0/go.mod h1:3Pcqqmp6RHvJI72kgb8fThyUnav364FOsdDo2aGW5lY=
gonum.org/v1/plot v0.10.1/go.mod h1:VZW5OlhkL1mysU9vaqNHnsy86inf6Ot+jB3r+BczCEo=
google.golang.org/api v0.4.0/go.mod h1:8k5glujaEP+g9n7WNsDg8QP6cUVNI86fCNMcbazEtwE=
google.golang.org/api v0.7.0/go.mod h1:WtwebWUNSVBH/HAw79HIFXZNqEvBhG+Ra+ax0hx3E3M=
google.golang.org/api v0.8.0/go.mod h1:o4eAsZoiT+ibD93RtjEohWalFOjRDx6CVaqeizhEnKg=
google.golang.org/api v0.9.0/go.mod h1:o4eAsZoiT+ibD93RtjEohWalFOjRDx6CVaqeizhEnKg=
google.golang.org/api v0.13.0/go.mod h1:iLdEw5Ide6rF15KTC1Kkl0iskquN2gFfn9o9XIsbkAI=
google.golang.org/api v0.14.0/go.mod h1:iLdEw5Ide6rF15KTC1Kkl0iskquN2gFfn9o9XIsbkAI=
google.golang.org/api v0.15.0/go.mod h1:iLdEw5Ide6rF15KTC1Kkl0iskquN2gFfn9o9XIsbkAI=
google.golang.org/api v0.17.0/go.mod h1:BwFmGc8tA3vsd7r/7kR8DY7iEEGSU04BFxCo5jP/sfE=
google.golang.org/api v0.18.0/go.mod h1:BwFmGc8tA3vsd7r/7kR8DY7iEEGSU04BFxCo5jP/sfE=
google.golang.org/api v0.19.0/go.mod h1:BwFmGc8tA3vsd7r/7kR8DY7iEEGSU04BFxCo5jP/sfE=
google.golang.org/api v0.20.0/go.mod h1:BwFmGc8tA3vsd7r/7kR8DY7iEEGSU04BFxCo5jP/sfE=
google.golang.org/api v0.22.0/go.mod h1:BwFmGc8tA3vsd7r/7kR8DY7iEEGSU04BFxCo5jP/sfE=
google.golang.org/api v0.24.0/go.mod h1:lIXQywCXRcnZPGlsd8NbLnOjtAoL6em04bJ9+z0MncE=
google.golang.org/api v0.28.0/go.mod h1:lIXQywCXRcnZPGlsd8NbLnOjtAoL6em04bJ9+z0MncE=
google.golang.org/api v0.29.0/go.mod h1:Lcubydp8VUV7KeIHD9z2Bys/sm/vGKnG1UHuDBSrHWM=
google.golang.org/api v0.30.0/go.mod h1:QGmEvQ87FHZNiUVJkT14jQNYJ4ZJjdRF23ZXz5138Fc=
google.golang.org/api v0.35.0/go.mod h1:/XrVsuzM0rZmrsbjJutiuftIzeuTQcEeaYcSk/mQ1dg=
google.golang.org/api v0.36.0/go.mod h1:+z5ficQTmoYpPn8LCUNVpK5I7hwkpjbcgqA7I34qYtE=
google.golang.org/api v0.40.0/go.mod h1:fYKFpnQN0DsDSKRVRcQSDQNtqWPfM9i+zNPxepjRCQ8=
google.golang.org/api v0.41.0/go.mod h1:RkxM5lITDfTzmyKFPt+wGrCJbVfniCr2ool8kTBzRTU=
google.golang.org/api v0.43.0/go.mod h1:nQsDGjRXMo4lvh5hP0TKqF244gqhGcr/YSIykhUk/94=
google.golang.org/api v0.47.0/go.mod h1:Wbvgpq1HddcWVtzsVLyfLp8lDg6AA241LmgIL59tHXo=
google.golang.org/api v0.48.0/go.mod h1:71Pr1vy+TAZRPkPs/xlCf5SsU8WjuAWv1Pfjbtukyy4=
google.golang.org/api v0.50.0/go.mod h1:4bNT5pAuq5ji4SRZm+5QIkjny9JAyVD/3gaSihNefaw=
google.golang.org/api v0.51.0/go.mod h1:t4HdrdoNgyN5cbEfm7Lum0lcLDLiise1F8qDKX00sOU=
google.golang.org/api v0.54.0/go.mod h1:7C4bFFOvVDGXjfDTAsgGwDgAxRDeQ4X8NvUedIt6z3k=
google.golang.org/api v0.55.0/go.mod h1:38yMfeP1kfjsl8isn0tliTjIb1rJXcQi4UXlbqivdVE=
google.golang.org/api v0.56.0/go.mod h1:38yMfeP1kfjsl8isn0tliTjIb1rJXcQi4UXlbqivdVE=
google.golang.org/api v0.57.0/go.mod h1:dVPlbZyBo2/OjBpmvNdpn2GRm6rPy75jyU7bmhdrMgI=
google.golang.org/api v0.61.0/go.mod h1:xQRti5UdCmoCEqFxcz93fTl338AVqDgyaDRuOZ3hg9I=
google.golang.org/api v0.63.0/go.mod h1:gs4ij2ffTRXwuzzgJl/56BdwJaA194ijkfn++9tDuPo=
google.golang.org/api v0.67.0/go.mod h1:ShHKP8E60yPsKNw/w8w+VYaj9H6buA5UqDp8dhbQZ6g=
google.golang.org/api v0.70.0/go.mod h1:Bs4ZM2HGifEvXwd50TtW70ovgJffJYw2oRCOFU/SkfA=
google.golang.org/api v0.71.0/go.mod h1:4PyU6e6JogV1f9eA4voyrTY2batOLdgZ5qZ5HOCc4j8=
google.golang.org/api v0.74.0/go.mod h1:ZpfMZOVRMywNyvJFeqL9HRWBgAuRfSjJFpe9QtRRyDs=
google.golang.org/api v0.75.0/go.mod h1:pU9QmyHLnzlpar1Mjt4IbapUCy8J+6HD6GeELN69ljA=
google.golang.org/api v0.77.0/go.mod h1:pU9QmyHLnzlpar1Mjt4IbapUCy8J+6HD6GeELN69ljA=
google.golang.org/api v0.78.0/go.mod h1:1Sg78yoMLOhlQTeF+ARBoytAcH1NNyyl390YMy6rKmw=
google.golang.org/api v0.80.0/go.mod h1:xY3nI94gbvBrE0J6NHXhxOmW97HG7Khjkku6AFB3Hyg=
google.golang.org/api v0.84.0/go.mod h1:NTsGnUFJMYROtiquksZHBWtHfeMC7iYthki7Eq3pa8o=
google.golang.org/api v0.85.0/go.mod h1:AqZf8Ep9uZ2pyTvgL+x0D3Zt0eoT9b5E8fmzfu6FO2g=
google.golang.org/api v0.90.0/go.mod h1:+Sem1dnrKlrXMR/X0bPnMWyluQe4RsNoYfmNLhOIkzw=
google.golang.org/api v0.93.0/go.mod h1:+Sem1dnrKlrXMR/X0bPnMWyluQe4RsNoYfmNLhOIkzw=
google.golang.org/api v0.95.0/go.mod h1:eADj+UBuxkh5zlrSntJghuNeg8HwQ1w5lTKkuqaETEI=
google.golang.org/api v0.96.0/go.mod h1:w7wJQLTM+wvQpNf5JyEcBoxK0RH7EDrh/L4qfsuJ13s=
google.golang.org/api v0.97.0/go.mod h1:w7wJQLTM+wvQpNf5JyEcBoxK0RH7EDrh/L4qfsuJ13s=
google.golang.org/api v0.98.0/go.mod h1:w7wJQLTM+wvQpNf5JyEcBoxK0RH7EDrh/L4qfsuJ13s=
google.golang.org/api v0.99.0/go.mod h1:1YOf74vkVndF7pG6hIHuINsM7eWwpVTAfNMNiL91A08=
google.golang.org/api v0.100.0/go.mod h1:ZE3Z2+ZOr87Rx7dqFsdRQkRBk36kDtp/h+QpHbB7a70=
google.golang.org/api v0.102.0/go.mod h1:3VFl6/fzoA+qNuS1N1/VfXY4LjoXN/wzeIp7TweWwGo=
google.golang.org/api v0.103.0/go.mod h1:hGtW6nK1AC+d9si/UBhw8Xli+QMOf6xyNAyJw4qU9w0=
google.golang.org/api v0.106.0/go.mod h1:2Ts0XTHNVWxypznxWOYUeI4g3WdP9Pk2Qk58+a/O9MY=
google.golang.org/api v0.107.0/go.mod h1:2Ts0XTHNVWxypznxWOYUeI4g3WdP9Pk2Qk58+a/O9MY=
google.golang.org/api v0.108.0/go.mod h1:2Ts0XTHNVWxypznxWOYUeI4g3WdP9Pk2Qk58+a/O9MY=
google.golang.org/api v0.110.0/go.mod h1:7FC4Vvx1Mooxh8C5HWjzZHcavuS2f6pmJpZx60ca7iI=
google.golang.org/api v0.111.0/go.mod h1:qtFHvU9mhgTJegR31csQ+rwxyUTHOKFqCKWp1J0fdw0=
google.golang.org/api v0.114.0/go.mod h1:ifYI2ZsFK6/uGddGfAD5BMxlnkBqCmqHSDUVi45N5Yg=
google.golang.org/api v0.247.0 h1:tSd/e0QrUlLsrwMKmkbQhYVa109qIintOls2Wh6bngc=
google.golang.org/api v0.247.0/go.mod h1:r1qZOPmxXffXg6xS5uhx16Fa/UFY8QU/K4bfKrnvovM=
google.golang.org/appengine v1.0.0/go.mod h1:EbEs0AVv82hx2wNQdGPgUI5lhzA/G0D9YwlJXL52JkM=
google.golang.org/appengine v1.1.0/go.mod h1:EbEs0AVv82hx2wNQdGPgUI5lhzA/G0D9YwlJXL52JkM=
google.golang.org/appengine v1.3.0/go.mod h1:xpcJRLb0r/rnEns0DIKYYv+WjYCduHsrkT7/EB5XEv4=
google.golang.org/appengine v1.4.0/go.mod h1:xpcJRLb0r/rnEns0DIKYYv+WjYCduHsrkT7/EB5XEv4=
google.golang.org/appengine v1.5.0/go.mod h1:xpcJRLb0r/rnEns0DIKYYv+WjYCduHsrkT7/EB5XEv4=
google.golang.org/appengine v1.6.1/go.mod h1:i06prIuMbXzDqacNJfV5OdTW448YApPu5ww/cMBSeb0=
google.golang.org/appengine v1.6.5/go.mod h1:8WjMMxjGQR8xUklV/ARdw2HLXBOI7O7uCIDZVag1xfc=
google.golang.org/appengine v1.6.6/go.mod h1:8WjMMxjGQR8xUklV/ARdw2HLXBOI7O7uCIDZVag1xfc=
google.golang.org/appengine v1.6.7/go.mod h1:8WjMMxjGQR8xUklV/ARdw2HLXBOI7O7uCIDZVag1xfc=
google.golang.org/genproto v0.0.0-20180817151627-c66870c02cf8/go.mod h1:JiN7NxoALGmiZfu7CAH4rXhgtRTLTxftemlI0sWmxmc=
google.golang.org/genproto v0.0.0-20190307195333-5fe7a883aa19/go.mod h1:VzzqZJRnGkLBvHegQrXjBqPurQTc5/KpmUdxsrq26oE=
google.golang.org/genproto v0.0.0-20190418145605-e7d98fc518a7/go.mod h1:VzzqZJRnGkLBvHegQrXjBqPurQTc5/KpmUdxsrq26oE=
google.golang.org/genproto v0.0.0-20190425155659-357c62f0e4bb/go.mod h1:VzzqZJRnGkLBvHegQrXjBqPurQTc5/KpmUdxsrq26oE=
google.golang.org/genproto v0.0.0-20190502173448-54afdca5d873/go.mod h1:VzzqZJRnGkLBvHegQrXjBqPurQTc5/KpmUdxsrq26oE=
google.golang.org/genproto v0.0.0-20190801165951-fa694d86fc64/go.mod h1:DMBHOl98Agz4BDEuKkezgsaosCRResVns1a3J2ZsMNc=
google.golang.org/genproto v0.0.0-20190819201941-24fa4b261c55/go.mod h1:DMBHOl98Agz4BDEuKkezgsaosCRResVns1a3J2ZsMNc=
google.golang.org/genproto v0.0.0-20190911173649-1774047e7e51/go.mod h1:IbNlFCBrqXvoKpeg0TB2l7cyZUmoaFKYIwrEpbDKLA8=
google.golang.org/genproto v0.0.0-20191108220845-16a3f7862a1a/go.mod h1:n3cpQtvxv34hfy77yVDNjmbRyujviMdxYliBSkLhpCc=
google.golang.org/genproto v0.0.0-20191115194625-c23dd37a84c9/go.mod h1:n3cpQtvxv34hfy77yVDNjmbRyujviMdxYliBSkLhpCc=
google.golang.org/genproto v0.0.0-20191216164720-4f79533eabd1/go.mod h1:n3cpQtvxv34hfy77yVDNjmbRyujviMdxYliBSkLhpCc=
google.golang.org/genproto v0.0.0-20191230161307-f3c370f40bfb/go.mod h1:n3cpQtvxv34hfy77yVDNjmbRyujviMdxYliBSkLhpCc=
google.golang.org/genproto v0.0.0-20200115191322-ca5a22157cba/go.mod h1:n3cpQtvxv34hfy77yVDNjmbRyujviMdxYliBSkLhpCc=
google.golang.org/genproto v0.0.0-20200122232147-0452cf42e150/go.mod h1:n3cpQtvxv34hfy77yVDNjmbRyujviMdxYliBSkLhpCc=
google.golang.org/genproto v0.0.0-20200204135345-fa8e72b47b90/go.mod h1:GmwEX6Z4W5gMy59cAlVYjN9JhxgbQH6Gn+gFDQe2lzA=
google.golang.org/genproto v0.0.0-20200212174721-66ed5ce911ce/go.mod h1:55QSHmfGQM9UVYDPBsyGGes0y52j32PQ3BqQfXhyH3c=
google.golang.org/genproto v0.0.0-20200224152610-e50cd9704f63/go.mod h1:55QSHmfGQM9UVYDPBsyGGes0y52j32PQ3BqQfXhyH3c=
google.golang.org/genproto v0.0.0-20200228133532-8c2c7df3a383/go.mod h1:55QSHmfGQM9UVYDPBsyGGes0y52j32PQ3BqQfXhyH3c=
google.golang.org/genproto v0.0.0-20200305110556-506484158171/go.mod h1:55QSHmfGQM9UVYDPBsyGGes0y52j32PQ3BqQfXhyH3c=
google.golang.org/genproto v0.0.0-20200312145019-da6875a35672/go.mod h1:55QSHmfGQM9UVYDPBsyGGes0y52j32PQ3BqQfXhyH3c=
google.golang.org/genproto v0.0.0-20200331122359-1ee6d9798940/go.mod h1:55QSHmfGQM9UVYDPBsyGGes0y52j32PQ3BqQfXhyH3c=
google.golang.org/genproto v0.0.0-20200430143042-b979b6f78d84/go.mod h1:55QSHmfGQM9UVYDPBsyGGes0y52j32PQ3BqQfXhyH3c=
google.golang.org/genproto v0.0.0-20200511104702-f5ebc3bea380/go.mod h1:55QSHmfGQM9UVYDPBsyGGes0y52j32PQ3BqQfXhyH3c=
google.golang.org/genproto v0.0.0-20200513103714-09dca8ec2884/go.mod h1:55QSHmfGQM9UVYDPBsyGGes0y52j32PQ3BqQfXhyH3c=
google.golang.org/genproto v0.0.0-20200515170657-fc4c6c6a6587/go.mod h1:YsZOwe1myG/8QRHRsmBRE1LrgQY60beZKjly0O1fX9U=
google.golang.org/genproto v0.0.0-20200526211855-cb27e3aa2013/go.mod h1:NbSheEEYHJ7i3ixzK3sjbqSGDJWnxyFXZblF3eUsNvo=
google.golang.org/genproto v0.0.0-20200618031413-b414f8b61790/go.mod h1:jDfRM7FcilCzHH/e9qn6dsT145K34l5v+OpcnNgKAAA=
google.golang.org/genproto v0.0.0-20200729003335-053ba62fc06f/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20200804131852-c06518451d9c/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20200825200019-8632dd797987/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20200904004341-0bd0a958aa1d/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20201109203340-2640f1f9cdfb/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20201201144952-b05cb90ed32e/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20201210142538-e3217bee35cc/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20201214200347-8c77b98c765d/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20210108203827-ffc7fda8c3d7/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20210222152913-aa3ee6e6a81c/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20210226172003-ab064af71705/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20210303154014-9728d6b83eeb/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20210310155132-4ce2db91004e/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20210319143718-93e7006c17a6/go.mod h1:FWY/as6DDZQgahTzZj3fqbO1CbirC29ZNUFHwi0/+no=
google.golang.org/genproto v0.0.0-20210329143202-679c6ae281ee/go.mod h1:9lPAdzaEmUacj36I+k7YKbEc5CXzPIeORRgDAUOu28A=
google.golang.org/genproto v0.0.0-20210402141018-6c239bbf2bb1/go.mod h1:9lPAdzaEmUacj36I+k7YKbEc5CXzPIeORRgDAUOu28A=
google.golang.org/genproto v0.0.0-20210513213006-bf773b8c8384/go.mod h1:P3QM42oQyzQSnHPnZ/vqoCdDmzH28fzWByN9asMeM8A=
google.golang.org/genproto v0.0.0-20210602131652-f16073e35f0c/go.mod h1:UODoCrxHCcBojKKwX1terBiRUaqAsFqJiF615XL43r0=
google.golang.org/genproto v0.0.0-20210604141403-392c879c8b08/go.mod h1:UODoCrxHCcBojKKwX1terBiRUaqAsFqJiF615XL43r0=
google.golang.org/genproto v0.0.0-20210608205507-b6d2f5bf0d7d/go.mod h1:UODoCrxHCcBojKKwX1terBiRUaqAsFqJiF615XL43r0=
google.golang.org/genproto v0.0.0-20210624195500-8bfb893ecb84/go.mod h1:SzzZ/N+nwJDaO1kznhnlzqS8ocJICar6hYhVyhi++24=
google.golang.org/genproto v0.0.0-20210713002101-d411969a0d9a/go.mod h1:AxrInvYm1dci+enl5hChSFPOmmUF1+uAa/UsgNRWd7k=
google.golang.org/genproto v0.0.0-20210716133855-ce7ef5c701ea/go.mod h1:AxrInvYm1dci+enl5hChSFPOmmUF1+uAa/UsgNRWd7k=
google.golang.org/genproto v0.0.0-20210728212813-7823e685a01f/go.mod h1:ob2IJxKrgPT52GcgX759i1sleT07tiKowYBGbczaW48=
google.golang.org/genproto v0.0.0-20210805201207-89edb61ffb67/go.mod h1:ob2IJxKrgPT52GcgX759i1sleT07tiKowYBGbczaW48=
google.golang.org/genproto v0.0.0-20210813162853-db860fec028c/go.mod h1:cFeNkxwySK631ADgubI+/XFU/xp8FD5KIVV4rj8UC5w=
google.golang.org/genproto v0.0.0-20210821163610-241b8fcbd6c8/go.mod h1:eFjDcFEctNawg4eG61bRv87N7iHBWyVhJu7u1kqDUXY=
google.golang.org/genproto v0.0.0-20210828152312-66f60bf46e71/go.mod h1:eFjDcFEctNawg4eG61bRv87N7iHBWyVhJu7u1kqDUXY=
google.golang.org/genproto v0.0.0-20210831024726-fe130286e0e2/go.mod h1:eFjDcFEctNawg4eG61bRv87N7iHBWyVhJu7u1kqDUXY=
google.golang.org/genproto v0.0.0-20210903162649-d08c68adba83/go.mod h1:eFjDcFEctNawg4eG61bRv87N7iHBWyVhJu7u1kqDUXY=
google.golang.org/genproto v0.0.0-20210909211513-a8c4777a87af/go.mod h1:eFjDcFEctNawg4eG61bRv87N7iHBWyVhJu7u1kqDUXY=
google.golang.org/genproto v0.0.0-20210924002016-3dee208752a0/go.mod h1:5CzLGKJ67TSI2B9POpiiyGha0AjJvZIUgRMt1dSmuhc=
google.golang.org/genproto v0.0.0-20211118181313-81c1377c94b1/go.mod h1:5CzLGKJ67TSI2B9POpiiyGha0AjJvZIUgRMt1dSmuhc=
google.golang.org/genproto v0.0.0-20211206160659-862468c7d6e0/go.mod h1:5CzLGKJ67TSI2B9POpiiyGha0AjJvZIUgRMt1dSmuhc=
google.golang.org/genproto v0.0.0-20211208223120-3a66f561d7aa/go.mod h1:5CzLGKJ67TSI2B9POpiiyGha0AjJvZIUgRMt1dSmuhc=
google.golang.org/genproto v0.0.0-20211221195035-429b39de9b1c/go.mod h1:5CzLGKJ67TSI2B9POpiiyGha0AjJvZIUgRMt1dSmuhc=
google.golang.org/genproto v0.0.0-20220126215142-9970aeb2e350/go.mod h1:5CzLGKJ67TSI2B9POpiiyGha0AjJvZIUgRMt1dSmuhc=
google.golang.org/genproto v0.0.0-20220207164111-0872dc986b00/go.mod h1:5CzLGKJ67TSI2B9POpiiyGha0AjJvZIUgRMt1dSmuhc=
google.golang.org/genproto v0.0.0-20220218161850-94dd64e39d7c/go.mod h1:kGP+zUP2Ddo0ayMi4YuN7C3WZyJvGLZRh8Z5wnAqvEI=
google.golang.org/genproto v0.0.0-20220222213610-43724f9ea8cf/go.mod h1:kGP+zUP2Ddo0ayMi4YuN7C3WZyJvGLZRh8Z5wnAqvEI=
google.golang.org/genproto v0.0.0-20220304144024-325a89244dc8/go.mod h1:kGP+zUP2Ddo0ayMi4YuN7C3WZyJvGLZRh8Z5wnAqvEI=
google.golang.org/genproto v0.0.0-20220310185008-1973136f34c6/go.mod h1:kGP+zUP2Ddo0ayMi4YuN7C3WZyJvGLZRh8Z5wnAqvEI=
google.golang.org/genproto v0.0.0-20220324131243-acbaeb5b85eb/go.mod h1:hAL49I2IFola2sVEjAn7MEwsja0xp51I0tlGAf9hz4E=
google.golang.org/genproto v0.0.0-20220329172620-7be39ac1afc7/go.mod h1:8w6bsBMX6yCPbAVTeqQHvzxW0EIFigd5lZyahWgyfDo=
google.golang.org/genproto v0.0.0-20220407144326-9054f6ed7bac/go.mod h1:8w6bsBMX6yCPbAVTeqQHvzxW0EIFigd5lZyahWgyfDo=
google.golang.org/genproto v0.0.0-20220413183235-5e96e2839df9/go.mod h1:8w6bsBMX6yCPbAVTeqQHvzxW0EIFigd5lZyahWgyfDo=
google.golang.org/genproto v0.0.0-20220414192740-2d67ff6cf2b4/go.mod h1:8w6bsBMX6yCPbAVTeqQHvzxW0EIFigd5lZyahWgyfDo=
google.golang.org/genproto v0.0.0-20220421151946-72621c1f0bd3/go.mod h1:8w6bsBMX6yCPbAVTeqQHvzxW0EIFigd5lZyahWgyfDo=
google.golang.org/genproto v0.0.0-20220429170224-98d788798c3e/go.mod h1:8w6bsBMX6yCPbAVTeqQHvzxW0EIFigd5lZyahWgyfDo=
google.golang.org/genproto v0.0.0-20220502173005-c8bf987b8c21/go.mod h1:RAyBrSAP7Fh3Nc84ghnVLDPuV51xc9agzmm4Ph6i0Q4=
google.golang.org/genproto v0.0.0-20220505152158-f39f71e6c8f3/go.mod h1:RAyBrSAP7Fh3Nc84ghnVLDPuV51xc9agzmm4Ph6i0Q4=
google.golang.org/genproto v0.0.0-20220518221133-4f43b3371335/go.mod h1:RAyBrSAP7Fh3Nc84ghnVLDPuV51xc9agzmm4Ph6i0Q4=
google.golang.org/genproto v0.0.0-20220523171625-347a074981d8/go.mod h1:RAyBrSAP7Fh3Nc84ghnVLDPuV51xc9agzmm4Ph6i0Q4=
google.golang.org/genproto v0.0.0-20220608133413-ed9918b62aac/go.mod h1:KEWEmljWE5zPzLBa/oHl6DaEt9LmfH6WtH1OHIvleBA=
google.golang.org/genproto v0.0.0-20220616135557-88e70c0c3a90/go.mod h1:KEWEmljWE5zPzLBa/oHl6DaEt9LmfH6WtH1OHIvleBA=
google.golang.org/genproto v0.0.0-20220617124728-180714bec0ad/go.mod h1:KEWEmljWE5zPzLBa/oHl6DaEt9LmfH6WtH1OHIvleBA=
google.golang.org/genproto v0.0.0-20220624142145-8cd45d7dbd1f/go.mod h1:KEWEmljWE5zPzLBa/oHl6DaEt9LmfH6WtH1OHIvleBA=
google.golang.org/genproto v0.0.0-20220628213854-d9e0b6570c03/go.mod h1:KEWEmljWE5zPzLBa/oHl6DaEt9LmfH6WtH1OHIvleBA=
google.golang.org/genproto v0.0.0-20220722212130-b98a9ff5e252/go.mod h1:GkXuJDJ6aQ7lnJcRF+SJVgFdQhypqgl3LB1C9vabdRE=
google.golang.org/genproto v0.0.0-20220801145646-83ce21fca29f/go.mod h1:iHe1svFLAZg9VWz891+QbRMwUv9O/1Ww+/mngYeThbc=
google.golang.org/genproto v0.0.0-20220815135757-37a418bb8959/go.mod h1:dbqgFATTzChvnt+ujMdZwITVAJHFtfyN1qUhDqEiIlk=
google.golang.org/genproto v0.0.0-20220817144833-d7fd3f11b9b1/go.mod h1:dbqgFATTzChvnt+ujMdZwITVAJHFtfyN1qUhDqEiIlk=
google.golang.org/genproto v0.0.0-20220822174746-9e6da59bd2fc/go.mod h1:dbqgFATTzChvnt+ujMdZwITVAJHFtfyN1qUhDqEiIlk=
google.golang.org/genproto v0.0.0-20220829144015-23454907ede3/go.mod h1:dbqgFATTzChvnt+ujMdZwITVAJHFtfyN1qUhDqEiIlk=
google.golang.org/genproto v0.0.0-20220829175752-36a9c930ecbf/go.mod h1:dbqgFATTzChvnt+ujMdZwITVAJHFtfyN1qUhDqEiIlk=
google.golang.org/genproto v0.0.0-20220913154956-18f8339a66a5/go.mod h1:0Nb8Qy+Sk5eDzHnzlStwW3itdNaWoZA5XeSG+R3JHSo=
google.golang.org/genproto v0.0.0-20220914142337-ca0e39ece12f/go.mod h1:0Nb8Qy+Sk5eDzHnzlStwW3itdNaWoZA5XeSG+R3JHSo=
google.golang.org/genproto v0.0.0-20220915135415-7fd63a7952de/go.mod h1:0Nb8Qy+Sk5eDzHnzlStwW3itdNaWoZA5XeSG+R3JHSo=
google.golang.org/genproto v0.0.0-20220916172020-2692e8806bfa/go.mod h1:0Nb8Qy+Sk5eDzHnzlStwW3itdNaWoZA5XeSG+R3JHSo=
google.golang.org/genproto v0.0.0-20220919141832-68c03719ef51/go.mod h1:0Nb8Qy+Sk5eDzHnzlStwW3itdNaWoZA5XeSG+R3JHSo=
google.golang.org/genproto v0.0.0-20220920201722-2b89144ce006/go.mod h1:ht8XFiar2npT/g4vkk7O0WYS1sHOHbdujxbEp7CJWbw=
google.golang.org/genproto v0.0.0-20220926165614-551eb538f295/go.mod h1:woMGP53BroOrRY3xTxlbr8Y3eB/nzAvvFM83q7kG2OI=
google.golang.org/genproto v0.0.0-20220926220553-6981cbe3cfce/go.mod h1:woMGP53BroOrRY3xTxlbr8Y3eB/nzAvvFM83q7kG2OI=
google.golang.org/genproto v0.0.0-20221010155953-15ba04fc1c0e/go.mod h1:3526vdqwhZAwq4wsRUaVG555sVgsNmIjRtO7t/JH29U=
google.golang.org/genproto v0.0.0-20221014173430-6e2ab493f96b/go.mod h1:1vXfmgAz9N9Jx0QA82PqRVauvCz1SGSz739p0f183jM=
google.golang.org/genproto v0.0.0-20221014213838-99cd37c6964a/go.mod h1:1vXfmgAz9N9Jx0QA82PqRVauvCz1SGSz739p0f183jM=
google.golang.org/genproto v0.0.0-20221024153911-1573dae28c9c/go.mod h1:9qHF0xnpdSfF6knlcsnpzUu5y+rpwgbvsyGAZPBMg4s=
google.golang.org/genproto v0.0.0-20221024183307-1bc688fe9f3e/go.mod h1:9qHF0xnpdSfF6knlcsnpzUu5y+rpwgbvsyGAZPBMg4s=
google.golang.org/genproto v0.0.0-20221027153422-115e99e71e1c/go.mod h1:CGI5F/G+E5bKwmfYo09AXuVN4dD894kIKUFmVbP2/Fo=
google.golang.org/genproto v0.0.0-20221109142239-94d6d90a7d66/go.mod h1:rZS5c/ZVYMaOGBfO68GWtjOw/eLaZM1X6iVtgjZ+EWg=
google.golang.org/genproto v0.0.0-20221114212237-e4508ebdbee1/go.mod h1:rZS5c/ZVYMaOGBfO68GWtjOw/eLaZM1X6iVtgjZ+EWg=
google.golang.org/genproto v0.0.0-20221117204609-8f9c96812029/go.mod h1:rZS5c/ZVYMaOGBfO68GWtjOw/eLaZM1X6iVtgjZ+EWg=
google.golang.org/genproto v0.0.0-20221118155620-16455021b5e6/go.mod h1:rZS5c/ZVYMaOGBfO68GWtjOw/eLaZM1X6iVtgjZ+EWg=
google.golang.org/genproto v0.0.0-20221201164419-0e50fba7f41c/go.mod h1:rZS5c/ZVYMaOGBfO68GWtjOw/eLaZM1X6iVtgjZ+EWg=
google.golang.org/genproto v0.0.0-20221201204527-e3fa12d562f3/go.mod h1:rZS5c/ZVYMaOGBfO68GWtjOw/eLaZM1X6iVtgjZ+EWg=
google.golang.org/genproto v0.0.0-20221202195650-67e5cbc046fd/go.mod h1:cTsE614GARnxrLsqKREzmNYJACSWWpAWdNMwnD7c2BE=
google.golang.org/genproto v0.0.0-20221227171554-f9683d7f8bef/go.mod h1:RGgjbofJ8xD9Sq1VVhDM1Vok1vRONV+rg+CjzG4SZKM=
google.golang.org/genproto v0.0.0-20230110181048-76db0878b65f/go.mod h1:RGgjbofJ8xD9Sq1VVhDM1Vok1vRONV+rg+CjzG4SZKM=
google.golang.org/genproto v0.0.0-20230112194545-e10362b5ecf9/go.mod h1:RGgjbofJ8xD9Sq1VVhDM1Vok1vRONV+rg+CjzG4SZKM=
google.golang.org/genproto v0.0.0-20230113154510-dbe35b8444a5/go.mod h1:RGgjbofJ8xD9Sq1VVhDM1Vok1vRONV+rg+CjzG4SZKM=
google.golang.org/genproto v0.0.0-20230123190316-2c411cf9d197/go.mod h1:RGgjbofJ8xD9Sq1VVhDM1Vok1vRONV+rg+CjzG4SZKM=
google.golang.org/genproto v0.0.0-20230124163310-31e0e69b6fc2/go.mod h1:RGgjbofJ8xD9Sq1VVhDM1Vok1vRONV+rg+CjzG4SZKM=
google.golang.org/genproto v0.0.0-20230125152338-dcaf20b6aeaa/go.mod h1:RGgjbofJ8xD9Sq1VVhDM1Vok1vRONV+rg+CjzG4SZKM=
google.golang.org/genproto v0.0.0-20230127162408-596548ed4efa/go.mod h1:RGgjbofJ8xD9Sq1VVhDM1Vok1vRONV+rg+CjzG4SZKM=
google.golang.org/genproto v0.0.0-20230209215440-0dfe4f8abfcc/go.mod h1:RGgjbofJ8xD9Sq1VVhDM1Vok1vRONV+rg+CjzG4SZKM=
google.golang.org/genproto v0.0.0-20230216225411-c8e22ba71e44/go.mod h1:8B0gmkoRebU8ukX6HP+4wrVQUY1+6PkQ44BSyIlflHA=
google.golang.org/genproto v0.0.0-20230222225845-10f96fb3dbec/go.mod h1:3Dl5ZL0q0isWJt+FVcfpQyirqemEuLAK/iFvg1UP1Hw=
google.golang.org/genproto v0.0.0-20230223222841-637eb2293923/go.mod h1:3Dl5ZL0q0isWJt+FVcfpQyirqemEuLAK/iFvg1UP1Hw=
google.golang.org/genproto v0.0.0-20230303212802-e74f57abe488/go.mod h1:TvhZT5f700eVlTNwND1xoEZQeWTB2RY/65kplwl/bFA=
google.golang.org/genproto v0.0.0-20230306155012-7f2fa6fef1f4/go.mod h1:NWraEVixdDnqcqQ30jipen1STv2r/n24Wb7twVTGR4s=
google.golang.org/genproto v0.0.0-20230320184635-7606e756e683/go.mod h1:NWraEVixdDnqcqQ30jipen1STv2r/n24Wb7twVTGR4s=
google.golang.org/genproto v0.0.0-20230323212658-478b75c54725/go.mod h1:UUQDJDOlWu4KYeJZffbWgBkS1YFobzKbLVfK69pe0Ak=
google.golang.org/genproto v0.0.0-20230330154414-c0448cd141ea/go.mod h1:UUQDJDOlWu4KYeJZffbWgBkS1YFobzKbLVfK69pe0Ak=
google.golang.org/genproto v0.0.0-20230331144136-dcfb400f0633/go.mod h1:UUQDJDOlWu4KYeJZffbWgBkS1YFobzKbLVfK69pe0Ak=
google.golang.org/genproto v0.0.0-20230410155749-daa745c078e1/go.mod h1:nKE/iIaLqn2bQwXBg8f1g2Ylh6r5MN5CmZvuzZCgsCU=
google.golang.org/genproto v0.0.0-20250603155806-513f23925822 h1:rHWScKit0gvAPuOnu87KpaYtjK5zBMLcULh7gxkCXu4=
google.golang.org/genproto v0.0.0-20250603155806-513f23925822/go.mod h1:HubltRL7rMh0LfnQPkMH4NPDFEWp0jw3vixw7jEM53s=
google.golang.org/genproto/googleapis/api v0.0.0-20250818200422-3122310a409c h1:AtEkQdl5b6zsybXcbz00j1LwNodDuH6hVifIaNqk7NQ=
google.golang.org/genproto/googleapis/api v0.0.0-20250818200422-3122310a409c/go.mod h1:ea2MjsO70ssTfCjiwHgI0ZFqcw45Ksuk2ckf9G468GA=
google.golang.org/genproto/googleapis/rpc v0.0.0-20250818200422-3122310a409c h1:qXWI/sQtv5UKboZ/zUk7h+mrf/lXORyI+n9DKDAusdg=
google.golang.org/genproto/googleapis/rpc v0.0.0-20250818200422-3122310a409c/go.mod h1:gw1tLEfykwDz2ET4a12jcXt4couGAm7IwsVaTy0Sflo=
google.golang.org/grpc v1.19.0/go.mod h1:mqu4LbDTu4XGKhr4mRzUsmM4RtVoemTSY81AxZiDr8c=
google.golang.org/grpc v1.20.1/go.mod h1:10oTOabMzJvdu6/UiuZezV6QK5dSlG84ov/aaiqXj38=
google.golang.org/grpc v1.21.1/go.mod h1:oYelfM1adQP15Ek0mdvEgi9Df8B9CZIaU1084ijfRaM=
google.golang.org/grpc v1.23.0/go.mod h1:Y5yQAOtifL1yxbo5wqy6BxZv8vAUGQwXBOALyacEbxg=
google.golang.org/grpc v1.25.1/go.mod h1:c3i+UQWmh7LiEpx4sFZnkU36qjEYZ0imhYfXVyQciAY=
google.golang.org/grpc v1.26.0/go.mod h1:qbnxyOmOxrQa7FizSgH+ReBfzJrCY1pSN7KXBS8abTk=
google.golang.org/grpc v1.27.0/go.mod h1:qbnxyOmOxrQa7FizSgH+ReBfzJrCY1pSN7KXBS8abTk=
google.golang.org/grpc v1.27.1/go.mod h1:qbnxyOmOxrQa7FizSgH+ReBfzJrCY1pSN7KXBS8abTk=
google.golang.org/grpc v1.28.0/go.mod h1:rpkK4SK4GF4Ach/+MFLZUBavHOvF2JJB5uozKKal+60=
google.golang.org/grpc v1.29.1/go.mod h1:itym6AZVZYACWQqET3MqgPpjcuV5QH3BxFS3IjizoKk=
google.golang.org/grpc v1.30.0/go.mod h1:N36X2cJ7JwdamYAgDz+s+rVMFjt3numwzf/HckM8pak=
google.golang.org/grpc v1.31.0/go.mod h1:N36X2cJ7JwdamYAgDz+s+rVMFjt3numwzf/HckM8pak=
google.golang.org/grpc v1.31.1/go.mod h1:N36X2cJ7JwdamYAgDz+s+rVMFjt3numwzf/HckM8pak=
google.golang.org/grpc v1.33.1/go.mod h1:fr5YgcSWrqhRRxogOsw7RzIpsmvOZ6IcH4kBYTpR3n0=
google.golang.org/grpc v1.33.2/go.mod h1:JMHMWHQWaTccqQQlmk3MJZS+GWXOdAesneDmEnv2fbc=
google.golang.org/grpc v1.34.0/go.mod h1:WotjhfgOW/POjDeRt8vscBtXq+2VjORFy659qA51WJ8=
google.golang.org/grpc v1.35.0/go.mod h1:qjiiYl8FncCW8feJPdyg3v6XW24KsRHe+dy9BAGRRjU=
google.golang.org/grpc v1.36.0/go.mod h1:qjiiYl8FncCW8feJPdyg3v6XW24KsRHe+dy9BAGRRjU=
google.golang.org/grpc v1.36.1/go.mod h1:qjiiYl8FncCW8feJPdyg3v6XW24KsRHe+dy9BAGRRjU=
google.golang.org/grpc v1.37.0/go.mod h1:NREThFqKR1f3iQ6oBuvc5LadQuXVGo9rkm5ZGrQdJfM=
google.golang.org/grpc v1.37.1/go.mod h1:NREThFqKR1f3iQ6oBuvc5LadQuXVGo9rkm5ZGrQdJfM=
google.golang.org/grpc v1.38.0/go.mod h1:NREThFqKR1f3iQ6oBuvc5LadQuXVGo9rkm5ZGrQdJfM=
google.golang.org/grpc v1.39.0/go.mod h1:PImNr+rS9TWYb2O4/emRugxiyHZ5JyHW5F+RPnDzfrE=
google.golang.org/grpc v1.39.1/go.mod h1:PImNr+rS9TWYb2O4/emRugxiyHZ5JyHW5F+RPnDzfrE=
google.golang.org/grpc v1.40.0/go.mod h1:ogyxbiOoUXAkP+4+xa6PZSE9DZgIHtSpzjDTB9KAK34=
google.golang.org/grpc v1.40.1/go.mod h1:ogyxbiOoUXAkP+4+xa6PZSE9DZgIHtSpzjDTB9KAK34=
google.golang.org/grpc v1.42.0/go.mod h1:k+4IHHFw41K8+bbowsex27ge2rCb65oeWqe4jJ590SU=
google.golang.org/grpc v1.44.0/go.mod h1:k+4IHHFw41K8+bbowsex27ge2rCb65oeWqe4jJ590SU=
google.golang.org/grpc v1.45.0/go.mod h1:lN7owxKUQEqMfSyQikvvk5tf/6zMPsrK+ONuO11+0rQ=
google.golang.org/grpc v1.46.0/go.mod h1:vN9eftEi1UMyUsIF80+uQXhHjbXYbm0uXoFCACuMGWk=
google.golang.org/grpc v1.46.2/go.mod h1:vN9eftEi1UMyUsIF80+uQXhHjbXYbm0uXoFCACuMGWk=
google.golang.org/grpc v1.47.0/go.mod h1:vN9eftEi1UMyUsIF80+uQXhHjbXYbm0uXoFCACuMGWk=
google.golang.org/grpc v1.48.0/go.mod h1:vN9eftEi1UMyUsIF80+uQXhHjbXYbm0uXoFCACuMGWk=
google.golang.org/grpc v1.49.0/go.mod h1:ZgQEeidpAuNRZ8iRrlBKXZQP1ghovWIVhdJRyCDK+GI=
google.golang.org/grpc v1.50.0/go.mod h1:ZgQEeidpAuNRZ8iRrlBKXZQP1ghovWIVhdJRyCDK+GI=
google.golang.org/grpc v1.50.1/go.mod h1:ZgQEeidpAuNRZ8iRrlBKXZQP1ghovWIVhdJRyCDK+GI=
google.golang.org/grpc v1.51.0/go.mod h1:wgNDFcnuBGmxLKI/qn4T+m5BtEBYXJPvibbUPsAIPww=
google.golang.org/grpc v1.52.3/go.mod h1:pu6fVzoFb+NBYNAvQL08ic+lvB2IojljRYuun5vorUY=
google.golang.org/grpc v1.53.0/go.mod h1:OnIrk0ipVdj4N5d9IUoFUx72/VlD7+jUsHwZgwSMQpw=
google.golang.org/grpc v1.54.0/go.mod h1:PUSEXI6iWghWaB6lXM4knEgpJNu2qUcKfDtNci3EC2g=
google.golang.org/grpc v1.56.3/go.mod h1:I9bI3vqKfayGqPUAwGdOSu7kt6oIJLixfffKrpXqQ9s=
google.golang.org/grpc v1.74.2 h1:WoosgB65DlWVC9FqI82dGsZhWFNBSLjQ84bjROOpMu4=
google.golang.org/grpc v1.74.2/go.mod h1:CtQ+BGjaAIXHs/5YS3i473GqwBBa1zGQNevxdeBEXrM=
google.golang.org/grpc/cmd/protoc-gen-go-grpc v1.1.0/go.mod h1:6Kw0yEErY5E/yWrBtf03jp27GLLJujG4z/JK95pnjjw=
google.golang.org/protobuf v0.0.0-20200109180630-ec00e32a8dfd/go.mod h1:DFci5gLYBciE7Vtevhsrf46CRTquxDuWsQurQQe4oz8=
google.golang.org/protobuf v0.0.0-20200221191635-4d8936d0db64/go.mod h1:kwYJMbMJ01Woi6D6+Kah6886xMZcty6N08ah7+eCXa0=
google.golang.org/protobuf v0.0.0-20200228230310-ab0ca4ff8a60/go.mod h1:cfTl7dwQJ+fmap5saPgwCLgHXTUD7jkjRqWcaiX5VyM=
google.golang.org/protobuf v1.20.1-0.20200309200217-e05f789c0967/go.mod h1:A+miEFZTKqfCUM6K7xSMQL9OKL/b6hQv+e19PK+JZNE=
google.golang.org/protobuf v1.21.0/go.mod h1:47Nbq4nVaFHyn7ilMalzfO3qCViNmqZ2kzikPIcrTAo=
google.golang.org/protobuf v1.22.0/go.mod h1:EGpADcykh3NcUnDUJcl1+ZksZNG86OlYog2l/sGQquU=
google.golang.org/protobuf v1.23.0/go.mod h1:EGpADcykh3NcUnDUJcl1+ZksZNG86OlYog2l/sGQquU=
google.golang.org/protobuf v1.23.1-0.20200526195155-81db48ad09cc/go.mod h1:EGpADcykh3NcUnDUJcl1+ZksZNG86OlYog2l/sGQquU=
google.golang.org/protobuf v1.24.0/go.mod h1:r/3tXBNzIEhYS9I1OUVjXDlt8tc493IdKGjtUeSXeh4=
google.golang.org/protobuf v1.25.0/go.mod h1:9JNX74DMeImyA3h4bdi1ymwjUzf21/xIlbajtzgsN7c=
google.golang.org/protobuf v1.26.0-rc.1/go.mod h1:jlhhOSvTdKEhbULTjvd4ARK9grFBp09yW+WbY/TyQbw=
google.golang.org/protobuf v1.26.0/go.mod h1:9q0QmTI4eRPtz6boOQmLYwt+qCgq0jsYwAQnmE0givc=
google.golang.org/protobuf v1.27.1/go.mod h1:9q0QmTI4eRPtz6boOQmLYwt+qCgq0jsYwAQnmE0givc=
google.golang.org/protobuf v1.28.0/go.mod h1:HV8QOd/L58Z+nl8r43ehVNZIU/HEI6OcFqwMG9pJV4I=
google.golang.org/protobuf v1.28.1/go.mod h1:HV8QOd/L58Z+nl8r43ehVNZIU/HEI6OcFqwMG9pJV4I=
google.golang.org/protobuf v1.29.1/go.mod h1:HV8QOd/L58Z+nl8r43ehVNZIU/HEI6OcFqwMG9pJV4I=
google.golang.org/protobuf v1.30.0/go.mod h1:HV8QOd/L58Z+nl8r43ehVNZIU/HEI6OcFqwMG9pJV4I=
google.golang.org/protobuf v1.36.7 h1:IgrO7UwFQGJdRNXH/sQux4R1Dj1WAKcLElzeeRaXV2A=
google.golang.org/protobuf v1.36.7/go.mod h1:jduwjTPXsFjZGTmRluh+L6NjiWu7pchiJ2/5YcXBHnY=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20200902074654-038fdea0a05b/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/errgo.v2 v2.1.0/go.mod h1:hNsd1EY+bozCKY1Ytp96fpM3vjJbqLJn88ws8XvfDNI=
gopkg.in/fsnotify.v1 v1.4.7/go.mod h1:Tz8NjZHkW78fSQdbUxIjBTcgA1z1m8ZHf0WmKUhAMys=
gopkg.in/inconshreveable/log15.v2 v2.0.0-20180818164646-67afb5ed74ec/go.mod h1:aPpfJ7XW+gOuirDoZ8gHhLh3kZ1B08FtV2bbmy7Jv3s=
gopkg.in/inf.v0 v0.9.1 h1:73M5CoZyi3ZLMOyDlQh031Cx6N9NDJ2Vvfl76EDAgDc=
gopkg.in/inf.v0 v0.9.1/go.mod h1:cWUDdTG/fYaXco+Dcufb5Vnc6Gp2YChqWtbxRZE0mXw=
gopkg.in/natefinch/npipe.v2 v2.0.0-20160621034901-c1b8fa8bdcce h1:+JknDZhAj8YMt7GC73Ei8pv4MzjDUNPHgQWJdtMAaDU=
gopkg.in/natefinch/npipe.v2 v2.0.0-20160621034901-c1b8fa8bdcce/go.mod h1:5AcXVHNjg+BDxry382+8OKon8SEWiKktQR07RKPsv1c=
gopkg.in/tomb.v1 v1.0.0-20141024135613-dd632973f1e7 h1:uRGJdciOHaEIrze2W8Q3AKkepLTh2hOroT7a+7czfdQ=
gopkg.in/tomb.v1 v1.0.0-20141024135613-dd632973f1e7/go.mod h1:dt/ZhP58zS4L8KSrWDmTeBkI65Dw0HsyUHuEVlX15mw=
gopkg.in/yaml.v2 v2.2.1/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.3/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.4/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.7/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.8/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.3.0/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.4.0 h1:D8xgwECY7CYvx+Y2n4sBz93Jn9JRvxdiyyo8CTfuKaY=
gopkg.in/yaml.v2 v2.4.0/go.mod h1:RDklbk79AGWmwhnvt/jBztapEOGDOx6ZbXqjP6csGnQ=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.0-20210107192922-496545a6307b/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gorm.io/driver/postgres v1.0.8/go.mod h1:4eOzrI1MUfm6ObJU/UcmbXyiHSs8jSwH95G5P5dxcAg=
gorm.io/gorm v1.20.12/go.mod h1:0HFTzE/SqkGTzK6TlDPPQbAYCluiVvhzoA1+aVyzenw=
gorm.io/gorm v1.21.4/go.mod h1:0HFTzE/SqkGTzK6TlDPPQbAYCluiVvhzoA1+aVyzenw=
gotest.tools/v3 v3.1.0 h1:rVV8Tcg/8jHUkPUorwjaMTtemIMVXfIPKiOqnhEhakk=
gotest.tools/v3 v3.1.0/go.mod h1:fHy7eyTmJFO5bQbUsEGQ1v4m2J3Jz9eWL54TP2/ZuYQ=
honnef.co/go/tools v0.0.0-20190102054323-c2f93a96b099/go.mod h1:rf3lG4BRIbNafJWhAfAdb/ePZxsR/4RtNHQocxwk9r4=
honnef.co/go/tools v0.0.0-20190106161140-3f1c8253044a/go.mod h1:rf3lG4BRIbNafJWhAfAdb/ePZxsR/4RtNHQocxwk9r4=
honnef.co/go/tools v0.0.0-20190418001031-e561f6794a2a/go.mod h1:rf3lG4BRIbNafJWhAfAdb/ePZxsR/4RtNHQocxwk9r4=
honnef.co/go/tools v0.0.0-20190523083050-ea95bdfd59fc/go.mod h1:rf3lG4BRIbNafJWhAfAdb/ePZxsR/4RtNHQocxwk9r4=
honnef.co/go/tools v0.0.1-2019.2.3/go.mod h1:a3bituU0lyd329TUQxRnasdCoJDkEUEAqEt0JzvZhAg=
honnef.co/go/tools v0.0.1-2020.1.3/go.mod h1:X/FiERA/W4tHapMX5mGpAtMSVEeEUOyHaw9vFzvIQ3k=
honnef.co/go/tools v0.0.1-2020.1.4/go.mod h1:X/FiERA/W4tHapMX5mGpAtMSVEeEUOyHaw9vFzvIQ3k=
honnef.co/go/tools v0.1.3/go.mod h1:NgwopIslSNH47DimFoV78dnkksY2EFtX0ajyb3K/las=
lukechampine.com/uint128 v1.1.1/go.mod h1:c4eWIwlEGaxC/+H1VguhU4PHXNWDCDMUlWdIWl2j1gk=
lukechampine.com/uint128 v1.2.0 h1:mBi/5l91vocEN8otkC5bDLhi2KdCticRiwbdB0O+rjI=
lukechampine.com/uint128 v1.2.0/go.mod h1:c4eWIwlEGaxC/+H1VguhU4PHXNWDCDMUlWdIWl2j1gk=
modernc.org/b v1.0.0 h1:vpvqeyp17ddcQWF29Czawql4lDdABCDRbXRAS4+aF2o=
modernc.org/b v1.0.0/go.mod h1:uZWcZfRj1BpYzfN9JTerzlNUnnPsV9O2ZA8JsRcubNg=
modernc.org/cc/v3 v3.36.0/go.mod h1:NFUHyPn4ekoC/JHeZFfZurN6ixxawE1BnVonP/oahEI=
modernc.org/cc/v3 v3.36.2/go.mod h1:NFUHyPn4ekoC/JHeZFfZurN6ixxawE1BnVonP/oahEI=
modernc.org/cc/v3 v3.36.3 h1:uISP3F66UlixxWEcKuIWERa4TwrZENHSL8tWxZz8bHg=
modernc.org/cc/v3 v3.36.3/go.mod h1:NFUHyPn4ekoC/JHeZFfZurN6ixxawE1BnVonP/oahEI=
modernc.org/ccgo/v3 v3.0.0-20220428102840-41399a37e894/go.mod h1:eI31LL8EwEBKPpNpA4bU1/i+sKOwOrQy8D87zWUcRZc=
modernc.org/ccgo/v3 v3.0.0-20220430103911-bc99d88307be/go.mod h1:bwdAnOoaIt8Ax9YdWGjxWsdkPcZyRPHqrOvJxaKAKGw=
modernc.org/ccgo/v3 v3.16.4/go.mod h1:tGtX0gE9Jn7hdZFeU88slbTh1UtCYKusWOoCJuvkWsQ=
modernc.org/ccgo/v3 v3.16.6/go.mod h1:tGtX0gE9Jn7hdZFeU88slbTh1UtCYKusWOoCJuvkWsQ=
modernc.org/ccgo/v3 v3.16.8/go.mod h1:zNjwkizS+fIFDrDjIAgBSCLkWbJuHF+ar3QRn+Z9aws=
modernc.org/ccgo/v3 v3.16.9 h1:AXquSwg7GuMk11pIdw7fmO1Y/ybgazVkMhsZWCV0mHM=
modernc.org/ccgo/v3 v3.16.9/go.mod h1:zNMzC9A9xeNUepy6KuZBbugn3c0Mc9TeiJO4lgvkJDo=
modernc.org/ccorpus v1.11.6 h1:J16RXiiqiCgua6+ZvQot4yUuUy8zxgqbqEEUuGPlISk=
modernc.org/ccorpus v1.11.6/go.mod h1:2gEUTrWqdpH2pXsmTM1ZkjeSrUWDpjMu2T6m29L/ErQ=
modernc.org/db v1.0.0 h1:2c6NdCfaLnshSvY7OU09cyAY0gYXUZj4lmg5ItHyucg=
modernc.org/db v1.0.0/go.mod h1:kYD/cO29L/29RM0hXYl4i3+Q5VojL31kTUVpVJDw0s8=
modernc.org/file v1.0.0 h1:9/PdvjVxd5+LcWUQIfapAWRGOkDLK90rloa8s/au06A=
modernc.org/file v1.0.0/go.mod h1:uqEokAEn1u6e+J45e54dsEA/pw4o7zLrA2GwyntZzjw=
modernc.org/fileutil v1.0.0 h1:Z1AFLZwl6BO8A5NldQg/xTSjGLetp+1Ubvl4alfGx8w=
modernc.org/fileutil v1.0.0/go.mod h1:JHsWpkrk/CnVV1H/eGlFf85BEpfkrp56ro8nojIq9Q8=
modernc.org/golex v1.0.0 h1:wWpDlbK8ejRfSyi0frMyhilD3JBvtcx2AdGDnU+JtsE=
modernc.org/golex v1.0.0/go.mod h1:b/QX9oBD/LhixY6NDh+IdGv17hgB+51fET1i2kPSmvk=
modernc.org/httpfs v1.0.6 h1:AAgIpFZRXuYnkjftxTAZwMIiwEqAfk8aVB2/oA6nAeM=
modernc.org/httpfs v1.0.6/go.mod h1:7dosgurJGp0sPaRanU53W4xZYKh14wfzX420oZADeHM=
modernc.org/internal v1.0.0 h1:XMDsFDcBDsibbBnHB2xzljZ+B1yrOVLEFkKL2u15Glw=
modernc.org/internal v1.0.0/go.mod h1:VUD/+JAkhCpvkUitlEOnhpVxCgsBI90oTzSCRcqQVSM=
modernc.org/libc v0.0.0-20220428101251-2d5f3daf273b/go.mod h1:p7Mg4+koNjc8jkqwcoFBJx7tXkpj00G77X7A72jXPXA=
modernc.org/libc v1.16.0/go.mod h1:N4LD6DBE9cf+Dzf9buBlzVJndKr/iJHG97vGLHYnb5A=
modernc.org/libc v1.16.1/go.mod h1:JjJE0eu4yeK7tab2n4S1w8tlWd9MxXLRzheaRnAKymU=
modernc.org/libc v1.16.17/go.mod h1:hYIV5VZczAmGZAnG15Vdngn5HSF5cSkbvfz2B7GRuVU=
modernc.org/libc v1.16.19/go.mod h1:p7Mg4+koNjc8jkqwcoFBJx7tXkpj00G77X7A72jXPXA=
modernc.org/libc v1.17.0/go.mod h1:XsgLldpP4aWlPlsjqKRdHPqCxCjISdHfM/yeWC5GyW0=
modernc.org/libc v1.17.1 h1:Q8/Cpi36V/QBfuQaFVeisEBs3WqoGAJprZzmf7TfEYI=
modernc.org/libc v1.17.1/go.mod h1:FZ23b+8LjxZs7XtFMbSzL/EhPxNbfZbErxEHc7cbD9s=
modernc.org/lldb v1.0.0 h1:6vjDJxQEfhlOLwl4bhpwIz00uyFK4EmSYcbwqwbynsc=
modernc.org/lldb v1.0.0/go.mod h1:jcRvJGWfCGodDZz8BPwiKMJxGJngQ/5DrRapkQnLob8=
modernc.org/mathutil v1.0.0/go.mod h1:wU0vUrJsVWBZ4P6e7xtFJEhFSNsfRLJ8H458uRjg03k=
modernc.org/mathutil v1.2.2/go.mod h1:mZW8CKdRPY1v87qxC/wUdX5O1qDzXMP5TH3wjfpga6E=
modernc.org/mathutil v1.4.1/go.mod h1:mZW8CKdRPY1v87qxC/wUdX5O1qDzXMP5TH3wjfpga6E=
modernc.org/mathutil v1.5.0 h1:rV0Ko/6SfM+8G+yKiyI830l3Wuz1zRutdslNoQ0kfiQ=
modernc.org/mathutil v1.5.0/go.mod h1:mZW8CKdRPY1v87qxC/wUdX5O1qDzXMP5TH3wjfpga6E=
modernc.org/memory v1.1.1/go.mod h1:/0wo5ibyrQiaoUoH7f9D8dnglAmILJ5/cxZlRECf+Nw=
modernc.org/memory v1.2.0/go.mod h1:/0wo5ibyrQiaoUoH7f9D8dnglAmILJ5/cxZlRECf+Nw=
modernc.org/memory v1.2.1 h1:dkRh86wgmq/bJu2cAS2oqBCz/KsMZU7TUM4CibQ7eBs=
modernc.org/memory v1.2.1/go.mod h1:PkUhL0Mugw21sHPeskwZW4D6VscE/GQJOnIpCnW6pSU=
modernc.org/opt v0.1.1/go.mod h1:WdSiB5evDcignE70guQKxYUl14mgWtbClRi5wmkkTX0=
modernc.org/opt v0.1.3 h1:3XOZf2yznlhC+ibLltsDGzABUGVx8J6pnFMS3E4dcq4=
modernc.org/opt v0.1.3/go.mod h1:WdSiB5evDcignE70guQKxYUl14mgWtbClRi5wmkkTX0=
modernc.org/ql v1.0.0 h1:bIQ/trWNVjQPlinI6jdOQsi195SIturGo3mp5hsDqVU=
modernc.org/ql v1.0.0/go.mod h1:xGVyrLIatPcO2C1JvI/Co8c0sr6y91HKFNy4pt9JXEY=
modernc.org/sortutil v1.1.0 h1:oP3U4uM+NT/qBQcbg/K2iqAX0Nx7B1b6YZtq3Gk/PjM=
modernc.org/sortutil v1.1.0/go.mod h1:ZyL98OQHJgH9IEfN71VsamvJgrtRX9Dj2gX+vH86L1k=
modernc.org/sqlite v1.18.1 h1:ko32eKt3jf7eqIkCgPAeHMBXw3riNSLhl2f3loEF7o8=
modernc.org/sqlite v1.18.1/go.mod h1:6ho+Gow7oX5V+OiOQ6Tr4xeqbx13UZ6t+Fw9IRUG4d4=
modernc.org/strutil v1.1.1/go.mod h1:DE+MQQ/hjKBZS2zNInV5hhcipt5rLPWkmpbGeW5mmdw=
modernc.org/strutil v1.1.3 h1:fNMm+oJklMGYfU9Ylcywl0CO5O6nTfaowNsh2wpPjzY=
modernc.org/strutil v1.1.3/go.mod h1:MEHNA7PdEnEwLvspRMtWTNnp2nnyvMfkimT1NKNAGbw=
modernc.org/tcl v1.13.1 h1:npxzTwFTZYM8ghWicVIX1cRWzj7Nd8i6AqqX2p+IYao=
modernc.org/tcl v1.13.1/go.mod h1:XOLfOwzhkljL4itZkK6T72ckMgvj0BDsnKNdZVUOecw=
modernc.org/token v1.0.0 h1:a0jaWiNMDhDUtqOj09wvjWWAqd3q7WpBulmL9H2egsk=
modernc.org/token v1.0.0/go.mod h1:UGzOrNV1mAFSEB63lOFHIpNRUVMvYTc6yu1SMY/XTDM=
modernc.org/z v1.5.1 h1:RTNHdsrOpeoSeOF4FbzTo8gBYByaJ5xT7NgZ9ZqRiJM=
modernc.org/z v1.5.1/go.mod h1:eWFB510QWW5Th9YGZT81s+LwvaAs3Q2yr4sP0rmLkv8=
modernc.org/zappy v1.0.0 h1:dPVaP+3ueIUv4guk8PuZ2wiUGcJ1WUVvIheeSSTD0yk=
modernc.org/zappy v1.0.0/go.mod h1:hHe+oGahLVII/aTTyWK/b53VDHMAGCBYYeZ9sn83HC4=
rsc.io/binaryregexp v0.2.0/go.mod h1:qTv7/COck+e2FymRvadv62gMdZztPaShugOCi3I+8D8=
rsc.io/pdf v0.1.1/go.mod h1:n8OzWcQ6Sp37PL01nO98y4iUCRdTGarVfzxY20ICaU4=
rsc.io/quote/v3 v3.1.0/go.mod h1:yEA65RcK8LyAZtP9Kv3t0HmxON59tX3rD+tICJqUlj0=
rsc.io/sampler v1.3.0/go.mod h1:T1hPZKmBbMNahiBKFy5HrXp6adAjACjK9JXDnKaTXpA=
```

## File: `LICENSE`
```
The MIT License (MIT)

Original Work
Copyright (c) 2016 Matthias Kadenbach
https://github.com/mattes/migrate

Modified Work
Copyright (c) 2018 Dale Hui
https://github.com/golang-migrate/migrate


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## File: `log.go`
```go
package migrate

// Logger is an interface so you can pass in your own
// logging implementation.
type Logger interface {

	// Printf is like fmt.Printf
	Printf(format string, v ...interface{})

	// Verbose should return true when verbose logging output is wanted
	Verbose() bool
}
```

## File: `Makefile`
```
SOURCE ?= file go_bindata github github_ee bitbucket aws_s3 google_cloud_storage godoc_vfs gitlab
DATABASE ?= postgres mysql redshift cassandra spanner cockroachdb yugabytedb clickhouse mongodb sqlserver firebird neo4j pgx pgx5 rqlite
DATABASE_TEST ?= $(DATABASE) sqlite sqlite3 sqlcipher
VERSION ?= $(shell git describe --tags 2>/dev/null | cut -c 2-)
TEST_FLAGS ?=
REPO_OWNER ?= $(shell cd .. && basename "$$(pwd)")
COVERAGE_DIR ?= .coverage

build:
	CGO_ENABLED=0 go build -ldflags='-X main.Version=$(VERSION)' -tags '$(DATABASE) $(SOURCE)' ./cmd/migrate

build-docker:
	CGO_ENABLED=0 go build -a -o build/migrate.linux-386 -ldflags="-s -w -X main.Version=${VERSION}" -tags "$(DATABASE) $(SOURCE)" ./cmd/migrate

build-cli: clean
	-mkdir ./cli/build
	cd ./cmd/migrate && CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -o ../../cli/build/migrate.linux-amd64 -ldflags='-X main.Version=$(VERSION) -extldflags "-static"' -tags '$(DATABASE) $(SOURCE)' .
	cd ./cmd/migrate && CGO_ENABLED=0 GOOS=linux GOARCH=arm GOARM=7 go build -a -o ../../cli/build/migrate.linux-armv7 -ldflags='-X main.Version=$(VERSION) -extldflags "-static"' -tags '$(DATABASE) $(SOURCE)' .
	cd ./cmd/migrate && CGO_ENABLED=0 GOOS=linux GOARCH=arm64 go build -a -o ../../cli/build/migrate.linux-arm64 -ldflags='-X main.Version=$(VERSION) -extldflags "-static"' -tags '$(DATABASE) $(SOURCE)' .
	cd ./cmd/migrate && CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build -a -o ../../cli/build/migrate.darwin-amd64 -ldflags='-X main.Version=$(VERSION) -extldflags "-static"' -tags '$(DATABASE) $(SOURCE)' .
	cd ./cmd/migrate && CGO_ENABLED=0 GOOS=windows GOARCH=386 go build -a -o ../../cli/build/migrate.windows-386.exe -ldflags='-X main.Version=$(VERSION) -extldflags "-static"' -tags '$(DATABASE) $(SOURCE)' .
	cd ./cmd/migrate && CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build -a -o ../../cli/build/migrate.windows-amd64.exe -ldflags='-X main.Version=$(VERSION) -extldflags "-static"' -tags '$(DATABASE) $(SOURCE)' .
	cd ./cli/build && find . -name 'migrate*' | xargs -I{} tar czf {}.tar.gz {}
	cd ./cli/build && shasum -a 256 * > sha256sum.txt
	cat ./cli/build/sha256sum.txt


clean:
	-rm -r ./cli/build


test-short:
	make test-with-flags --ignore-errors TEST_FLAGS='-short'


test:
	@-rm -r $(COVERAGE_DIR)
	@mkdir $(COVERAGE_DIR)
	make test-with-flags TEST_FLAGS='-v -race -covermode atomic -coverprofile $$(COVERAGE_DIR)/combined.txt -bench=. -benchmem -timeout 20m'


test-with-flags:
	@echo SOURCE: $(SOURCE)
	@echo DATABASE_TEST: $(DATABASE_TEST)

	@go test $(TEST_FLAGS) ./...


kill-orphaned-docker-containers:
	docker rm -f $(shell docker ps -aq --filter label=migrate_test)


html-coverage:
	go tool cover -html=$(COVERAGE_DIR)/combined.txt


list-external-deps:
	$(call external_deps,'.')
	$(call external_deps,'./cli/...')
	$(call external_deps,'./testing/...')

	$(foreach v, $(SOURCE), $(call external_deps,'./source/$(v)/...'))
	$(call external_deps,'./source/testing/...')
	$(call external_deps,'./source/stub/...')

	$(foreach v, $(DATABASE), $(call external_deps,'./database/$(v)/...'))
	$(call external_deps,'./database/testing/...')
	$(call external_deps,'./database/stub/...')


restore-import-paths:
	find . -name '*.go' -type f -execdir sed -i '' s%\"github.com/$(REPO_OWNER)/migrate%\"github.com/mattes/migrate%g '{}' \;


rewrite-import-paths:
	find . -name '*.go' -type f -execdir sed -i '' s%\"github.com/mattes/migrate%\"github.com/$(REPO_OWNER)/migrate%g '{}' \;


# example: fswatch -0 --exclude .godoc.pid --event Updated . | xargs -0 -n1 -I{} make docs
docs:
	-make kill-docs
	nohup godoc -play -http=127.0.0.1:6064 </dev/null >/dev/null 2>&1 & echo $$! > .godoc.pid
	cat .godoc.pid


kill-docs:
	@cat .godoc.pid
	kill -9 $$(cat .godoc.pid)
	rm .godoc.pid


open-docs:
	open http://localhost:6064/pkg/github.com/$(REPO_OWNER)/migrate


# example: make release V=0.0.0
release:
	git tag v$(V)
	@read -p "Press enter to confirm and push to origin ..." && git push origin v$(V)

echo-source:
	@echo "$(SOURCE)"

echo-database:
	@echo "$(DATABASE)"


define external_deps
	@echo '-- $(1)';  go list -f '{{join .Deps "\n"}}' $(1) | grep -v github.com/$(REPO_OWNER)/migrate | xargs go list -f '{{if not .Standard}}{{.ImportPath}}{{end}}'

endef


.PHONY: build build-docker build-cli clean test-short test test-with-flags html-coverage \
        restore-import-paths rewrite-import-paths list-external-deps release \
		docs kill-docs open-docs kill-orphaned-docker-containers echo-source echo-database

SHELL = /bin/sh
RAND = $(shell echo $$RANDOM)

```

## File: `migrate.go`
```go
// Package migrate reads migrations from sources and runs them against databases.
// Sources are defined by the `source.Driver` and databases by the `database.Driver`
// interface. The driver interfaces are kept "dumb", all migration logic is kept
// in this package.
package migrate

import (
	"errors"
	"fmt"
	"os"
	"sync"
	"time"

	"github.com/golang-migrate/migrate/v4/database"
	iurl "github.com/golang-migrate/migrate/v4/internal/url"
	"github.com/golang-migrate/migrate/v4/source"
)

// DefaultPrefetchMigrations sets the number of migrations to pre-read
// from the source. This is helpful if the source is remote, but has little
// effect for a local source (i.e. file system).
// Please note that this setting has a major impact on the memory usage,
// since each pre-read migration is buffered in memory. See DefaultBufferSize.
var DefaultPrefetchMigrations = uint(10)

// DefaultLockTimeout sets the max time a database driver has to acquire a lock.
var DefaultLockTimeout = 15 * time.Second

var (
	ErrNoChange       = errors.New("no change")
	ErrNilVersion     = errors.New("no migration")
	ErrInvalidVersion = errors.New("version must be >= -1")
	ErrLocked         = errors.New("database locked")
	ErrLockTimeout    = errors.New("timeout: can't acquire database lock")
)

// ErrShortLimit is an error returned when not enough migrations
// can be returned by a source for a given limit.
type ErrShortLimit struct {
	Short uint
}

// Error implements the error interface.
func (e ErrShortLimit) Error() string {
	return fmt.Sprintf("limit %v short", e.Short)
}

type ErrDirty struct {
	Version int
}

func (e ErrDirty) Error() string {
	return fmt.Sprintf("Dirty database version %v. Fix and force version.", e.Version)
}

type Migrate struct {
	sourceName         string
	sourceDrv          source.Driver
	databaseDriverName string
	databaseDrv        database.Driver

	// Log accepts a Logger interface
	Log Logger

	// GracefulStop accepts `true` and will stop executing migrations
	// as soon as possible at a safe break point, so that the database
	// is not corrupted.
	GracefulStop chan bool
	isLockedMu   *sync.Mutex

	isGracefulStop bool
	isLocked       bool

	// PrefetchMigrations defaults to DefaultPrefetchMigrations,
	// but can be set per Migrate instance.
	PrefetchMigrations uint

	// LockTimeout defaults to DefaultLockTimeout,
	// but can be set per Migrate instance.
	LockTimeout time.Duration
}

// New returns a new Migrate instance from a source URL and a database URL.
// The URL scheme is defined by each driver.
func New(sourceURL, databaseURL string) (*Migrate, error) {
	m := newCommon()

	sourceName, err := iurl.SchemeFromURL(sourceURL)
	if err != nil {
		return nil, fmt.Errorf("failed to parse scheme from source URL: %w", err)
	}
	m.sourceName = sourceName

	databaseDriverName, err := iurl.SchemeFromURL(databaseURL)
	if err != nil {
		return nil, fmt.Errorf("failed to parse scheme from database URL: %w", err)
	}
	m.databaseDriverName = databaseDriverName

	sourceDrv, err := source.Open(sourceURL)
	if err != nil {
		return nil, fmt.Errorf("failed to open source, %q: %w", sourceURL, err)
	}
	m.sourceDrv = sourceDrv

	databaseDrv, err := database.Open(databaseURL)
	if err != nil {
		return nil, fmt.Errorf("failed to open database: %w", err)
	}
	m.databaseDrv = databaseDrv

	return m, nil
}

// NewWithDatabaseInstance returns a new Migrate instance from a source URL
// and an existing database instance. The source URL scheme is defined by each driver.
// Use any string that can serve as an identifier during logging as databaseDriverName.
// You are responsible for closing the underlying database client if necessary.
func NewWithDatabaseInstance(sourceURL string, databaseDriverName string, databaseInstance database.Driver) (*Migrate, error) {
	m := newCommon()

	sourceName, err := iurl.SchemeFromURL(sourceURL)
	if err != nil {
		return nil, err
	}
	m.sourceName = sourceName

	m.databaseDriverName = databaseDriverName

	sourceDrv, err := source.Open(sourceURL)
	if err != nil {
		return nil, fmt.Errorf("failed to open source, %q: %w", sourceURL, err)
	}
	m.sourceDrv = sourceDrv

	m.databaseDrv = databaseInstance

	return m, nil
}

// NewWithSourceInstance returns a new Migrate instance from an existing source instance
// and a database URL. The database URL scheme is defined by each driver.
// Use any string that can serve as an identifier during logging as sourceName.
// You are responsible for closing the underlying source client if necessary.
func NewWithSourceInstance(sourceName string, sourceInstance source.Driver, databaseURL string) (*Migrate, error) {
	m := newCommon()

	databaseDriverName, err := iurl.SchemeFromURL(databaseURL)
	if err != nil {
		return nil, fmt.Errorf("failed to parse scheme from database URL: %w", err)
	}
	m.databaseDriverName = databaseDriverName

	m.sourceName = sourceName

	databaseDrv, err := database.Open(databaseURL)
	if err != nil {
		return nil, fmt.Errorf("failed to open database: %w", err)
	}
	m.databaseDrv = databaseDrv

	m.sourceDrv = sourceInstance

	return m, nil
}

// NewWithInstance returns a new Migrate instance from an existing source and
// database instance. Use any string that can serve as an identifier during logging
// as sourceName and databaseDriverName. You are responsible for closing down
// the underlying source and database client if necessary.
func NewWithInstance(sourceName string, sourceInstance source.Driver, databaseDriverName string, databaseInstance database.Driver) (*Migrate, error) {
	m := newCommon()

	m.sourceName = sourceName
	m.databaseDriverName = databaseDriverName

	m.sourceDrv = sourceInstance
	m.databaseDrv = databaseInstance

	return m, nil
}

func newCommon() *Migrate {
	return &Migrate{
		GracefulStop:       make(chan bool, 1),
		PrefetchMigrations: DefaultPrefetchMigrations,
		LockTimeout:        DefaultLockTimeout,
		isLockedMu:         &sync.Mutex{},
	}
}

// Close closes the source and the database.
func (m *Migrate) Close() (source error, database error) {
	databaseSrvClose := make(chan error)
	sourceSrvClose := make(chan error)

	m.logVerbosePrintf("Closing source and database\n")

	go func() {
		databaseSrvClose <- m.databaseDrv.Close()
	}()

	go func() {
		sourceSrvClose <- m.sourceDrv.Close()
	}()

	return <-sourceSrvClose, <-databaseSrvClose
}

// Migrate looks at the currently active migration version,
// then migrates either up or down to the specified version.
func (m *Migrate) Migrate(version uint) error {
	if err := m.lock(); err != nil {
		return err
	}

	curVersion, dirty, err := m.databaseDrv.Version()
	if err != nil {
		return m.unlockErr(err)
	}

	if dirty {
		return m.unlockErr(ErrDirty{curVersion})
	}

	ret := make(chan interface{}, m.PrefetchMigrations)
	go m.read(curVersion, int(version), ret)

	return m.unlockErr(m.runMigrations(ret))
}

// Steps looks at the currently active migration version.
// It will migrate up if n > 0, and down if n < 0.
func (m *Migrate) Steps(n int) error {
	if n == 0 {
		return ErrNoChange
	}

	if err := m.lock(); err != nil {
		return err
	}

	curVersion, dirty, err := m.databaseDrv.Version()
	if err != nil {
		return m.unlockErr(err)
	}

	if dirty {
		return m.unlockErr(ErrDirty{curVersion})
	}

	ret := make(chan interface{}, m.PrefetchMigrations)

	if n > 0 {
		go m.readUp(curVersion, n, ret)
	} else {
		go m.readDown(curVersion, -n, ret)
	}

	return m.unlockErr(m.runMigrations(ret))
}

// Up looks at the currently active migration version
// and will migrate all the way up (applying all up migrations).
func (m *Migrate) Up() error {
	if err := m.lock(); err != nil {
		return err
	}

	curVersion, dirty, err := m.databaseDrv.Version()
	if err != nil {
		return m.unlockErr(err)
	}

	if dirty {
		return m.unlockErr(ErrDirty{curVersion})
	}

	ret := make(chan interface{}, m.PrefetchMigrations)

	go m.readUp(curVersion, -1, ret)
	return m.unlockErr(m.runMigrations(ret))
}

// Down looks at the currently active migration version
// and will migrate all the way down (applying all down migrations).
func (m *Migrate) Down() error {
	if err := m.lock(); err != nil {
		return err
	}

	curVersion, dirty, err := m.databaseDrv.Version()
	if err != nil {
		return m.unlockErr(err)
	}

	if dirty {
		return m.unlockErr(ErrDirty{curVersion})
	}

	ret := make(chan interface{}, m.PrefetchMigrations)
	go m.readDown(curVersion, -1, ret)
	return m.unlockErr(m.runMigrations(ret))
}

// Drop deletes everything in the database.
func (m *Migrate) Drop() error {
	if err := m.lock(); err != nil {
		return err
	}
	if err := m.databaseDrv.Drop(); err != nil {
		return m.unlockErr(err)
	}
	return m.unlock()
}

// Run runs any migration provided by you against the database.
// It does not check any currently active version in database.
// Usually you don't need this function at all. Use Migrate,
// Steps, Up or Down instead.
func (m *Migrate) Run(migration ...*Migration) error {
	if len(migration) == 0 {
		return ErrNoChange
	}

	if err := m.lock(); err != nil {
		return err
	}

	curVersion, dirty, err := m.databaseDrv.Version()
	if err != nil {
		return m.unlockErr(err)
	}

	if dirty {
		return m.unlockErr(ErrDirty{curVersion})
	}

	ret := make(chan interface{}, m.PrefetchMigrations)

	go func() {
		defer close(ret)
		for _, migr := range migration {
			if m.PrefetchMigrations > 0 && migr.Body != nil {
				m.logVerbosePrintf("Start buffering %v\n", migr.LogString())
			} else {
				m.logVerbosePrintf("Scheduled %v\n", migr.LogString())
			}

			ret <- migr
			go func(migr *Migration) {
				if err := migr.Buffer(); err != nil {
					m.logErr(err)
				}
			}(migr)
		}
	}()

	return m.unlockErr(m.runMigrations(ret))
}

// Force sets a migration version.
// It does not check any currently active version in database.
// It resets the dirty state to false.
func (m *Migrate) Force(version int) error {
	if version < -1 {
		return ErrInvalidVersion
	}

	if err := m.lock(); err != nil {
		return err
	}

	if err := m.databaseDrv.SetVersion(version, false); err != nil {
		return m.unlockErr(err)
	}

	return m.unlock()
}

// Version returns the currently active migration version.
// If no migration has been applied, yet, it will return ErrNilVersion.
func (m *Migrate) Version() (version uint, dirty bool, err error) {
	v, d, err := m.databaseDrv.Version()
	if err != nil {
		return 0, false, err
	}

	if v == database.NilVersion {
		return 0, false, ErrNilVersion
	}

	return suint(v), d, nil
}

// read reads either up or down migrations from source `from` to `to`.
// Each migration is then written to the ret channel.
// If an error occurs during reading, that error is written to the ret channel, too.
// Once read is done reading it will close the ret channel.
func (m *Migrate) read(from int, to int, ret chan<- interface{}) {
	defer close(ret)

	// check if from version exists
	if from >= 0 {
		if err := m.versionExists(suint(from)); err != nil {
			ret <- err
			return
		}
	}

	// check if to version exists
	if to >= 0 {
		if err := m.versionExists(suint(to)); err != nil {
			ret <- err
			return
		}
	}

	// no change?
	if from == to {
		ret <- ErrNoChange
		return
	}

	if from < to {
		// it's going up
		// apply first migration if from is nil version
		if from == -1 {
			firstVersion, err := m.sourceDrv.First()
			if err != nil {
				ret <- err
				return
			}

			migr, err := m.newMigration(firstVersion, int(firstVersion))
			if err != nil {
				ret <- err
				return
			}

			ret <- migr
			go func() {
				if err := migr.Buffer(); err != nil {
					m.logErr(err)
				}
			}()

			from = int(firstVersion)
		}

		// run until we reach target ...
		for from < to {
			if m.stop() {
				return
			}

			next, err := m.sourceDrv.Next(suint(from))
			if err != nil {
				ret <- err
				return
			}

			migr, err := m.newMigration(next, int(next))
			if err != nil {
				ret <- err
				return
			}

			ret <- migr
			go func() {
				if err := migr.Buffer(); err != nil {
					m.logErr(err)
				}
			}()

			from = int(next)
		}

	} else {
		// it's going down
		// run until we reach target ...
		for from > to && from >= 0 {
			if m.stop() {
				return
			}

			prev, err := m.sourceDrv.Prev(suint(from))
			if errors.Is(err, os.ErrNotExist) && to == -1 {
				// apply nil migration
				migr, err := m.newMigration(suint(from), -1)
				if err != nil {
					ret <- err
					return
				}
				ret <- migr
				go func() {
					if err := migr.Buffer(); err != nil {
						m.logErr(err)
					}
				}()

				return

			} else if err != nil {
				ret <- err
				return
			}

			migr, err := m.newMigration(suint(from), int(prev))
			if err != nil {
				ret <- err
				return
			}

			ret <- migr
			go func() {
				if err := migr.Buffer(); err != nil {
					m.logErr(err)
				}
			}()

			from = int(prev)
		}
	}
}

// readUp reads up migrations from `from` limited by `limit`.
// limit can be -1, implying no limit and reading until there are no more migrations.
// Each migration is then written to the ret channel.
// If an error occurs during reading, that error is written to the ret channel, too.
// Once readUp is done reading it will close the ret channel.
func (m *Migrate) readUp(from int, limit int, ret chan<- interface{}) {
	defer close(ret)

	// check if from version exists
	if from >= 0 {
		if err := m.versionExists(suint(from)); err != nil {
			ret <- err
			return
		}
	}

	if limit == 0 {
		ret <- ErrNoChange
		return
	}

	count := 0
	for count < limit || limit == -1 {
		if m.stop() {
			return
		}

		// apply first migration if from is nil version
		if from == -1 {
			firstVersion, err := m.sourceDrv.First()
			if err != nil {
				ret <- err
				return
			}

			migr, err := m.newMigration(firstVersion, int(firstVersion))
			if err != nil {
				ret <- err
				return
			}

			ret <- migr
			go func() {
				if err := migr.Buffer(); err != nil {
					m.logErr(err)
				}
			}()
			from = int(firstVersion)
			count++
			continue
		}

		// apply next migration
		next, err := m.sourceDrv.Next(suint(from))
		if errors.Is(err, os.ErrNotExist) {
			// no limit, but no migrations applied?
			if limit == -1 && count == 0 {
				ret <- ErrNoChange
				return
			}

			// no limit, reached end
			if limit == -1 {
				return
			}

			// reached end, and didn't apply any migrations
			if limit > 0 && count == 0 {
				ret <- os.ErrNotExist
				return
			}

			// applied less migrations than limit?
			if count < limit {
				ret <- ErrShortLimit{suint(limit - count)}
				return
			}
		}
		if err != nil {
			ret <- err
			return
		}

		migr, err := m.newMigration(next, int(next))
		if err != nil {
			ret <- err
			return
		}

		ret <- migr
		go func() {
			if err := migr.Buffer(); err != nil {
				m.logErr(err)
			}
		}()
		from = int(next)
		count++
	}
}

// readDown reads down migrations from `from` limited by `limit`.
// limit can be -1, implying no limit and reading until there are no more migrations.
// Each migration is then written to the ret channel.
// If an error occurs during reading, that error is written to the ret channel, too.
// Once readDown is done reading it will close the ret channel.
func (m *Migrate) readDown(from int, limit int, ret chan<- interface{}) {
	defer close(ret)

	// check if from version exists
	if from >= 0 {
		if err := m.versionExists(suint(from)); err != nil {
			ret <- err
			return
		}
	}

	if limit == 0 {
		ret <- ErrNoChange
		return
	}

	// no change if already at nil version
	if from == -1 && limit == -1 {
		ret <- ErrNoChange
		return
	}

	// can't go over limit if already at nil version
	if from == -1 && limit > 0 {
		ret <- os.ErrNotExist
		return
	}

	count := 0
	for count < limit || limit == -1 {
		if m.stop() {
			return
		}

		prev, err := m.sourceDrv.Prev(suint(from))
		if errors.Is(err, os.ErrNotExist) {
			// no limit or haven't reached limit, apply "first" migration
			if limit == -1 || limit-count > 0 {
				firstVersion, err := m.sourceDrv.First()
				if err != nil {
					ret <- err
					return
				}

				migr, err := m.newMigration(firstVersion, -1)
				if err != nil {
					ret <- err
					return
				}
				ret <- migr
				go func() {
					if err := migr.Buffer(); err != nil {
						m.logErr(err)
					}
				}()
				count++
			}

			if count < limit {
				ret <- ErrShortLimit{suint(limit - count)}
			}
			return
		}
		if err != nil {
			ret <- err
			return
		}

		migr, err := m.newMigration(suint(from), int(prev))
		if err != nil {
			ret <- err
			return
		}

		ret <- migr
		go func() {
			if err := migr.Buffer(); err != nil {
				m.logErr(err)
			}
		}()
		from = int(prev)
		count++
	}
}

// runMigrations reads *Migration and error from a channel. Any other type
// sent on this channel will result in a panic. Each migration is then
// proxied to the database driver and run against the database.
// Before running a newly received migration it will check if it's supposed
// to stop execution because it might have received a stop signal on the
// GracefulStop channel.
func (m *Migrate) runMigrations(ret <-chan interface{}) error {
	for r := range ret {

		if m.stop() {
			return nil
		}

		switch r := r.(type) {
		case error:
			return r

		case *Migration:
			migr := r

			// set version with dirty state
			if err := m.databaseDrv.SetVersion(migr.TargetVersion, true); err != nil {
				return err
			}

			if migr.Body != nil {
				m.logVerbosePrintf("Read and execute %v\n", migr.LogString())
				if err := m.databaseDrv.Run(migr.BufferedBody); err != nil {
					return err
				}
			}

			// set clean state
			if err := m.databaseDrv.SetVersion(migr.TargetVersion, false); err != nil {
				return err
			}

			endTime := time.Now()
			readTime := migr.FinishedReading.Sub(migr.StartedBuffering)
			runTime := endTime.Sub(migr.FinishedReading)

			// log either verbose or normal
			if m.Log != nil {
				if m.Log.Verbose() {
					m.logPrintf("Finished %v (read %v, ran %v)\n", migr.LogString(), readTime, runTime)
				} else {
					m.logPrintf("%v (%v)\n", migr.LogString(), readTime+runTime)
				}
			}

		default:
			return fmt.Errorf("unknown type: %T with value: %+v", r, r)
		}
	}
	return nil
}

// versionExists checks the source if either the up or down migration for
// the specified migration version exists.
func (m *Migrate) versionExists(version uint) (result error) {
	// try up migration first
	up, _, err := m.sourceDrv.ReadUp(version)
	if err == nil {
		defer func() {
			if errClose := up.Close(); errClose != nil {
				result = errors.Join(result, errClose)
			}
		}()
	}
	if errors.Is(err, os.ErrExist) {
		return nil
	} else if !errors.Is(err, os.ErrNotExist) {
		return err
	}

	// then try down migration
	down, _, err := m.sourceDrv.ReadDown(version)
	if err == nil {
		defer func() {
			if errClose := down.Close(); errClose != nil {
				result = errors.Join(result, errClose)
			}
		}()
	}
	if errors.Is(err, os.ErrExist) {
		return nil
	} else if !errors.Is(err, os.ErrNotExist) {
		return err
	}

	err = fmt.Errorf("no migration found for version %d: %w", version, err)
	m.logErr(err)
	return err
}

// stop returns true if no more migrations should be run against the database
// because a stop signal was received on the GracefulStop channel.
// Calls are cheap and this function is not blocking.
func (m *Migrate) stop() bool {
	if m.isGracefulStop {
		return true
	}

	select {
	case <-m.GracefulStop:
		m.isGracefulStop = true
		return true

	default:
		return false
	}
}

// newMigration is a helper func that returns a *Migration for the
// specified version and targetVersion.
func (m *Migrate) newMigration(version uint, targetVersion int) (*Migration, error) {
	var migr *Migration

	if targetVersion >= int(version) {
		r, identifier, err := m.sourceDrv.ReadUp(version)
		if errors.Is(err, os.ErrNotExist) {
			// create "empty" migration
			migr, err = NewMigration(nil, "", version, targetVersion)
			if err != nil {
				return nil, err
			}

		} else if err != nil {
			return nil, err

		} else {
			// create migration from up source
			migr, err = NewMigration(r, identifier, version, targetVersion)
			if err != nil {
				return nil, err
			}
		}

	} else {
		r, identifier, err := m.sourceDrv.ReadDown(version)
		if errors.Is(err, os.ErrNotExist) {
			// create "empty" migration
			migr, err = NewMigration(nil, "", version, targetVersion)
			if err != nil {
				return nil, err
			}

		} else if err != nil {
			return nil, err

		} else {
			// create migration from down source
			migr, err = NewMigration(r, identifier, version, targetVersion)
			if err != nil {
				return nil, err
			}
		}
	}

	if m.PrefetchMigrations > 0 && migr.Body != nil {
		m.logVerbosePrintf("Start buffering %v\n", migr.LogString())
	} else {
		m.logVerbosePrintf("Scheduled %v\n", migr.LogString())
	}

	return migr, nil
}

// lock is a thread safe helper function to lock the database.
// It should be called as late as possible when running migrations.
func (m *Migrate) lock() error {
	m.isLockedMu.Lock()
	defer m.isLockedMu.Unlock()

	if m.isLocked {
		return ErrLocked
	}

	// create done channel, used in the timeout goroutine
	done := make(chan bool, 1)
	defer func() {
		done <- true
	}()

	// use errchan to signal error back to this context
	errchan := make(chan error, 2)

	// start timeout goroutine
	timeout := time.After(m.LockTimeout)
	go func() {
		for {
			select {
			case <-done:
				return
			case <-timeout:
				errchan <- ErrLockTimeout
				return
			}
		}
	}()

	// now try to acquire the lock
	go func() {
		if err := m.databaseDrv.Lock(); err != nil {
			errchan <- err
		} else {
			errchan <- nil
		}
	}()

	// wait until we either receive ErrLockTimeout or error from Lock operation
	err := <-errchan
	if err == nil {
		m.isLocked = true
	}
	return err
}

// unlock is a thread safe helper function to unlock the database.
// It should be called as early as possible when no more migrations are
// expected to be executed.
func (m *Migrate) unlock() error {
	m.isLockedMu.Lock()
	defer m.isLockedMu.Unlock()

	if err := m.databaseDrv.Unlock(); err != nil {
		// BUG: Can potentially create a deadlock. Add a timeout.
		return err
	}

	m.isLocked = false
	return nil
}

// unlockErr calls unlock and returns a combined error
// if a prevErr is not nil.
func (m *Migrate) unlockErr(prevErr error) error {
	if err := m.unlock(); err != nil {
		prevErr = errors.Join(prevErr, err)
	}
	return prevErr
}

// logPrintf writes to m.Log if not nil
func (m *Migrate) logPrintf(format string, v ...interface{}) {
	if m.Log != nil {
		m.Log.Printf(format, v...)
	}
}

// logVerbosePrintf writes to m.Log if not nil. Use for verbose logging output.
func (m *Migrate) logVerbosePrintf(format string, v ...interface{}) {
	if m.Log != nil && m.Log.Verbose() {
		m.Log.Printf(format, v...)
	}
}

// logErr writes error to m.Log if not nil
func (m *Migrate) logErr(err error) {
	if m.Log != nil {
		m.Log.Printf("error: %v", err)
	}
}
```

## File: `migrate_test.go`
```go
package migrate

import (
	"bytes"
	"database/sql"
	"errors"
	"io"
	"log"
	"os"
	"strings"
	"testing"

	dStub "github.com/golang-migrate/migrate/v4/database/stub"
	"github.com/golang-migrate/migrate/v4/source"
	sStub "github.com/golang-migrate/migrate/v4/source/stub"
)

// sourceStubMigrations hold the following migrations:
// u = up migration, d = down migration, n = version
//
//	|  1  |  -  |  3  |  4  |  5  |  -  |  7  |
//	| u d |  -  | u   | u d |   d |  -  | u d |
var sourceStubMigrations *source.Migrations

const (
	srcDrvNameStub = "stub"
	dbDrvNameStub  = "stub"
)

func init() {
	sourceStubMigrations = source.NewMigrations()
	sourceStubMigrations.Append(&source.Migration{Version: 1, Direction: source.Up, Identifier: "CREATE 1"})
	sourceStubMigrations.Append(&source.Migration{Version: 1, Direction: source.Down, Identifier: "DROP 1"})
	sourceStubMigrations.Append(&source.Migration{Version: 3, Direction: source.Up, Identifier: "CREATE 3"})
	sourceStubMigrations.Append(&source.Migration{Version: 4, Direction: source.Up, Identifier: "CREATE 4"})
	sourceStubMigrations.Append(&source.Migration{Version: 4, Direction: source.Down, Identifier: "DROP 4"})
	sourceStubMigrations.Append(&source.Migration{Version: 5, Direction: source.Down, Identifier: "DROP 5"})
	sourceStubMigrations.Append(&source.Migration{Version: 7, Direction: source.Up, Identifier: "CREATE 7"})
	sourceStubMigrations.Append(&source.Migration{Version: 7, Direction: source.Down, Identifier: "DROP 7"})
}

type DummyInstance struct{ Name string }

func TestNew(t *testing.T) {
	m, err := New("stub://", "stub://")
	if err != nil {
		t.Fatal(err)
	}

	if m.sourceName != srcDrvNameStub {
		t.Errorf("expected stub, got %v", m.sourceName)
	}
	if m.sourceDrv == nil {
		t.Error("expected sourceDrv not to be nil")
	}

	if m.databaseDriverName != dbDrvNameStub {
		t.Errorf("expected stub, got %v", m.databaseDriverName)
	}
	if m.databaseDrv == nil {
		t.Error("expected databaseDrv not to be nil")
	}
}

func ExampleNew() {
	// Read migrations from /home/mattes/migrations and connect to a local postgres database.
	m, err := New("file:///home/mattes/migrations", "postgres://mattes:secret@localhost:5432/database?sslmode=disable")
	if err != nil {
		log.Fatal(err)
	}

	// Migrate all the way up ...
	if err := m.Up(); err != nil && err != ErrNoChange {
		log.Fatal(err)
	}
}

func TestNewWithDatabaseInstance(t *testing.T) {
	dummyDb := &DummyInstance{"database"}
	dbInst, err := dStub.WithInstance(dummyDb, &dStub.Config{})
	if err != nil {
		t.Fatal(err)
	}

	m, err := NewWithDatabaseInstance("stub://", dbDrvNameStub, dbInst)
	if err != nil {
		t.Fatal(err)
	}

	if m.sourceName != srcDrvNameStub {
		t.Errorf("expected stub, got %v", m.sourceName)
	}
	if m.sourceDrv == nil {
		t.Error("expected sourceDrv not to be nil")
	}

	if m.databaseDriverName != dbDrvNameStub {
		t.Errorf("expected stub, got %v", m.databaseDriverName)
	}
	if m.databaseDrv == nil {
		t.Error("expected databaseDrv not to be nil")
	}
}

func ExampleNewWithDatabaseInstance() {
	// Create and use an existing database instance.
	db, err := sql.Open("postgres", "postgres://mattes:secret@localhost:5432/database?sslmode=disable")
	if err != nil {
		log.Fatal(err)
	}
	defer func() {
		if err := db.Close(); err != nil {
			log.Fatal(err)
		}
	}()

	// Create driver instance from db.
	// Check each driver if it supports the WithInstance function.
	// `import "github.com/golang-migrate/migrate/v4/database/postgres"`
	instance, err := dStub.WithInstance(db, &dStub.Config{})
	if err != nil {
		log.Fatal(err)
	}

	// Read migrations from /home/mattes/migrations and connect to a local postgres database.
	m, err := NewWithDatabaseInstance("file:///home/mattes/migrations", "postgres", instance)
	if err != nil {
		log.Fatal(err)
	}

	// Migrate all the way up ...
	if err := m.Up(); err != nil {
		log.Fatal(err)
	}
}

func TestNewWithSourceInstance(t *testing.T) {
	dummySource := &DummyInstance{"source"}
	sInst, err := sStub.WithInstance(dummySource, &sStub.Config{})
	if err != nil {
		t.Fatal(err)
	}

	m, err := NewWithSourceInstance(srcDrvNameStub, sInst, "stub://")
	if err != nil {
		t.Fatal(err)
	}

	if m.sourceName != srcDrvNameStub {
		t.Errorf("expected stub, got %v", m.sourceName)
	}
	if m.sourceDrv == nil {
		t.Error("expected sourceDrv not to be nil")
	}

	if m.databaseDriverName != dbDrvNameStub {
		t.Errorf("expected stub, got %v", m.databaseDriverName)
	}
	if m.databaseDrv == nil {
		t.Error("expected databaseDrv not to be nil")
	}
}

func ExampleNewWithSourceInstance() {
	di := &DummyInstance{"think any client required for a source here"}

	// Create driver instance from DummyInstance di.
	// Check each driver if it support the WithInstance function.
	// `import "github.com/golang-migrate/migrate/v4/source/stub"`
	instance, err := sStub.WithInstance(di, &sStub.Config{})
	if err != nil {
		log.Fatal(err)
	}

	// Read migrations from Stub and connect to a local postgres database.
	m, err := NewWithSourceInstance(srcDrvNameStub, instance, "postgres://mattes:secret@localhost:5432/database?sslmode=disable")
	if err != nil {
		log.Fatal(err)
	}

	// Migrate all the way up ...
	if err := m.Up(); err != nil {
		log.Fatal(err)
	}
}

func TestNewWithInstance(t *testing.T) {
	dummyDb := &DummyInstance{"database"}
	dbInst, err := dStub.WithInstance(dummyDb, &dStub.Config{})
	if err != nil {
		t.Fatal(err)
	}

	dummySource := &DummyInstance{"source"}
	sInst, err := sStub.WithInstance(dummySource, &sStub.Config{})
	if err != nil {
		t.Fatal(err)
	}

	m, err := NewWithInstance(srcDrvNameStub, sInst, dbDrvNameStub, dbInst)
	if err != nil {
		t.Fatal(err)
	}

	if m.sourceName != srcDrvNameStub {
		t.Errorf("expected stub, got %v", m.sourceName)
	}
	if m.sourceDrv == nil {
		t.Error("expected sourceDrv not to be nil")
	}

	if m.databaseDriverName != dbDrvNameStub {
		t.Errorf("expected stub, got %v", m.databaseDriverName)
	}
	if m.databaseDrv == nil {
		t.Error("expected databaseDrv not to be nil")
	}
}

func ExampleNewWithInstance() {
	// See NewWithDatabaseInstance and NewWithSourceInstance for an example.
}

func TestClose(t *testing.T) {
	m, _ := New("stub://", "stub://")
	sourceErr, databaseErr := m.Close()
	if sourceErr != nil {
		t.Error(sourceErr)
	}
	if databaseErr != nil {
		t.Error(databaseErr)
	}
}

func TestMigrate(t *testing.T) {
	m, _ := New("stub://", "stub://")
	m.sourceDrv.(*sStub.Stub).Migrations = sourceStubMigrations
	dbDrv := m.databaseDrv.(*dStub.Stub)

	tt := []struct {
		version       uint
		expectErr     error
		expectVersion uint
		expectSeq     migrationSequence
	}{
		// migrate all the way Up in single steps
		{
			version:   0,
			expectErr: os.ErrNotExist,
		},
		{
			version:       1,
			expectVersion: 1,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
			},
		},
		{
			version:   2,
			expectErr: os.ErrNotExist,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
			},
		},
		{
			version:       3,
			expectVersion: 3,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
			},
		},
		{
			version:       4,
			expectVersion: 4,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
			},
		},
		{
			version:       5,
			expectVersion: 5,
			expectSeq: migrationSequence{ // 5 has no up migration
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
			},
		},
		{
			version:   6,
			expectErr: os.ErrNotExist,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
			},
		},
		{
			version:       7,
			expectVersion: 7,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
			},
		},
		{
			version:   8,
			expectErr: os.ErrNotExist,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
			},
		},

		// migrate all the way Down in single steps
		{
			version:   6,
			expectErr: os.ErrNotExist,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
			},
		},
		{
			version:       5,
			expectVersion: 5,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
			},
		},
		{
			version:       4,
			expectVersion: 4,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
			},
		},
		{
			version:       3,
			expectVersion: 3,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
			},
		},
		{
			version:   2,
			expectErr: os.ErrNotExist,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
			},
		},
		{
			version:       1,
			expectVersion: 1,
			expectSeq: migrationSequence{ // 3 has no down migration
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
			},
		},
		{
			version:   0,
			expectErr: os.ErrNotExist,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
			},
		},

		// migrate all the way Up in one step
		{
			version:       7,
			expectVersion: 7,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
			},
		},

		// migrate all the way Down in one step
		{
			version:       1,
			expectVersion: 1,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
			},
		},

		// can't migrate the same version twice
		{
			version:   1,
			expectErr: ErrNoChange,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
			},
		},
	}

	for i, v := range tt {
		err := m.Migrate(v.version)
		if (v.expectErr == os.ErrNotExist && !errors.Is(err, os.ErrNotExist)) ||
			(v.expectErr != os.ErrNotExist && err != v.expectErr) {
			t.Errorf("expected err %v, got %v, in %v", v.expectErr, err, i)

		} else if err == nil {
			version, _, err := m.Version()
			if err != nil {
				t.Error(err)
			}
			if version != v.expectVersion {
				t.Errorf("expected version %v, got %v, in %v", v.expectVersion, version, i)
			}
		}
		equalDbSeq(t, i, v.expectSeq, dbDrv)
	}
}

func TestMigrateDirty(t *testing.T) {
	m, _ := New("stub://", "stub://")
	dbDrv := m.databaseDrv.(*dStub.Stub)
	if err := dbDrv.SetVersion(0, true); err != nil {
		t.Fatal(err)
	}

	err := m.Migrate(1)
	if _, ok := err.(ErrDirty); !ok {
		t.Fatalf("expected ErrDirty, got %v", err)
	}
}

func TestSteps(t *testing.T) {
	m, _ := New("stub://", "stub://")
	m.sourceDrv.(*sStub.Stub).Migrations = sourceStubMigrations
	dbDrv := m.databaseDrv.(*dStub.Stub)

	tt := []struct {
		steps         int
		expectErr     error
		expectVersion int
		expectSeq     migrationSequence
	}{
		// step must be != 0
		{
			steps:     0,
			expectErr: ErrNoChange,
		},

		// can't go Down if ErrNilVersion
		{
			steps:     -1,
			expectErr: os.ErrNotExist,
		},

		// migrate all the way Up
		{
			steps:         1,
			expectVersion: 1,
			expectSeq: migrationSequence{
				mr("CREATE 1")},
		},
		{
			steps:         1,
			expectVersion: 3,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
			},
		},
		{
			steps:         1,
			expectVersion: 4,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
			},
		},
		{
			steps:         1,
			expectVersion: 5,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
			},
		},
		{
			steps:         1,
			expectVersion: 7,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
			},
		},
		{
			steps:     1,
			expectErr: os.ErrNotExist,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
			},
		},

		// migrate all the way Down
		{
			steps:         -1,
			expectVersion: 5,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
			},
		},
		{
			steps:         -1,
			expectVersion: 4,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
			},
		},
		{
			steps:         -1,
			expectVersion: 3,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
			},
		},
		{
			steps:         -1,
			expectVersion: 1,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
			},
		},
		{
			steps:         -1,
			expectVersion: -1,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
				mr("DROP 1"),
			},
		},

		// migrate Up in bigger step
		{
			steps:         4,
			expectVersion: 5,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
				mr("DROP 1"),
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
			},
		},

		// apply one migration, then reaches out of boundary
		{
			steps:         2,
			expectErr:     ErrShortLimit{1},
			expectVersion: 7,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
				mr("DROP 1"),
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
			},
		},

		// migrate Down in bigger step
		{
			steps:         -4,
			expectVersion: 1,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
				mr("DROP 1"),
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
			},
		},

		// apply one migration, then reaches out of boundary
		{
			steps:         -2,
			expectErr:     ErrShortLimit{1},
			expectVersion: -1,
			expectSeq: migrationSequence{
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
				mr("DROP 1"),
				mr("CREATE 1"),
				mr("CREATE 3"),
				mr("CREATE 4"),
				mr("CREATE 7"),
				mr("DROP 7"),
				mr("DROP 5"),
				mr("DROP 4"),
				mr("DROP 1"),
			},
		},
	}

	for i, v := range tt {
		err := m.Steps(v.steps)
		if (v.expectErr == os.ErrNotExist && !errors.Is(err, os.ErrNotExist)) ||
			(v.expectErr != os.ErrNotExist && err != v.expectErr) {
			t.Errorf("expected err %v, got %v, in %v", v.expectErr, err, i)

		} else if err == nil {
			version, _, err := m.Version()
			if err != ErrNilVersion && err != nil {
				t.Error(err)
			}
			if v.expectVersion == -1 && err != ErrNilVersion {
				t.Errorf("expected ErrNilVersion, got %v, in %v", version, i)

			} else if v.expectVersion >= 0 && version != uint(v.expectVersion) {
				t.Errorf("expected version %v, got %v, in %v", v.expectVersion, version, i)
			}
		}
		equalDbSeq(t, i, v.expectSeq, dbDrv)
	}
}

func TestStepsDirty(t *testing.T) {
	m, _ := New("stub://", "stub://")
	dbDrv := m.databaseDrv.(*dStub.Stub)
	if err := dbDrv.SetVersion(0, true); err != nil {
		t.Fatal(err)
	}

	err := m.Steps(1)
	if _, ok := err.(ErrDirty); !ok {
		t.Fatalf("expected ErrDirty, got %v", err)
	}
}

func TestUpAndDown(t *testing.T) {
	m, _ := New("stub://", "stub://")
	m.sourceDrv.(*sStub.Stub).Migrations = sourceStubMigrations
	dbDrv := m.databaseDrv.(*dStub.Stub)

	// go Up first
	if err := m.Up(); err != nil {
		t.Fatal(err)
	}
	expectedSequence := migrationSequence{
		mr("CREATE 1"),
		mr("CREATE 3"),
		mr("CREATE 4"),
		mr("CREATE 7"),
	}
	equalDbSeq(t, 0, expectedSequence, dbDrv)

	// go Down
	if err := m.Down(); err != nil {
		t.Fatal(err)
	}
	expectedSequence = migrationSequence{
		mr("CREATE 1"),
		mr("CREATE 3"),
		mr("CREATE 4"),
		mr("CREATE 7"),
		mr("DROP 7"),
		mr("DROP 5"),
		mr("DROP 4"),
		mr("DROP 1"),
	}
	equalDbSeq(t, 1, expectedSequence, dbDrv)

	// go 1 Up and then all the way Up
	if err := m.Steps(1); err != nil {
		t.Fatal(err)
	}
	expectedSequence = migrationSequence{
		mr("CREATE 1"),
		mr("CREATE 3"),
		mr("CREATE 4"),
		mr("CREATE 7"),
		mr("DROP 7"),
		mr("DROP 5"),
		mr("DROP 4"),
		mr("DROP 1"),
		mr("CREATE 1"),
	}
	equalDbSeq(t, 2, expectedSequence, dbDrv)

	if err := m.Up(); err != nil {
		t.Fatal(err)
	}
	expectedSequence = migrationSequence{
		mr("CREATE 1"),
		mr("CREATE 3"),
		mr("CREATE 4"),
		mr("CREATE 7"),
		mr("DROP 7"),
		mr("DROP 5"),
		mr("DROP 4"),
		mr("DROP 1"),
		mr("CREATE 1"),
		mr("CREATE 3"),
		mr("CREATE 4"),
		mr("CREATE 7"),
	}
	equalDbSeq(t, 3, expectedSequence, dbDrv)

	// go 1 Down and then all the way Down
	if err := m.Steps(-1); err != nil {
		t.Fatal(err)
	}
	expectedSequence = migrationSequence{
		mr("CREATE 1"),
		mr("CREATE 3"),
		mr("CREATE 4"),
		mr("CREATE 7"),
		mr("DROP 7"),
		mr("DROP 5"),
		mr("DROP 4"),
		mr("DROP 1"),
		mr("CREATE 1"),
		mr("CREATE 3"),
		mr("CREATE 4"),
		mr("CREATE 7"),
		mr("DROP 7"),
	}
	equalDbSeq(t, 1, expectedSequence, dbDrv)

	if err := m.Down(); err != nil {
		t.Fatal(err)
	}
	expectedSequence = migrationSequence{
		mr("CREATE 1"),
		mr("CREATE 3"),
		mr("CREATE 4"),
		mr("CREATE 7"),
		mr("DROP 7"),
		mr("DROP 5"),
		mr("DROP 4"),
		mr("DROP 1"),
		mr("CREATE 1"),
		mr("CREATE 3"),
		mr("CREATE 4"),
		mr("CREATE 7"),
		mr("DROP 7"),
		mr("DROP 5"),
		mr("DROP 4"),
		mr("DROP 1"),
	}
	equalDbSeq(t, 1, expectedSequence, dbDrv)
}

func TestUpDirty(t *testing.T) {
	m, _ := New("stub://", "stub://")
	dbDrv := m.databaseDrv.(*dStub.Stub)
	if err := dbDrv.SetVersion(0, true); err != nil {
		t.Fatal(err)
	}

	err := m.Up()
	if _, ok := err.(ErrDirty); !ok {
		t.Fatalf("expected ErrDirty, got %v", err)
	}
}

func TestDownDirty(t *testing.T) {
	m, _ := New("stub://", "stub://")
	dbDrv := m.databaseDrv.(*dStub.Stub)
	if err := dbDrv.SetVersion(0, true); err != nil {
		t.Fatal(err)
	}

	err := m.Down()
	if _, ok := err.(ErrDirty); !ok {
		t.Fatalf("expected ErrDirty, got %v", err)
	}
}

func TestDrop(t *testing.T) {
	m, _ := New("stub://", "stub://")
	m.sourceDrv.(*sStub.Stub).Migrations = sourceStubMigrations
	dbDrv := m.databaseDrv.(*dStub.Stub)

	if err := m.Drop(); err != nil {
		t.Fatal(err)
	}

	if dbDrv.MigrationSequence[len(dbDrv.MigrationSequence)-1] != dStub.DROP {
		t.Fatalf("expected database to DROP, got sequence %v", dbDrv.MigrationSequence)
	}
}

func TestVersion(t *testing.T) {
	m, _ := New("stub://", "stub://")
	dbDrv := m.databaseDrv.(*dStub.Stub)

	_, _, err := m.Version()
	if err != ErrNilVersion {
		t.Fatalf("expected ErrNilVersion, got %v", err)
	}

	if err := dbDrv.Run(bytes.NewBufferString("1_up")); err != nil {
		t.Fatal(err)
	}

	if err := dbDrv.SetVersion(1, false); err != nil {
		t.Fatal(err)
	}

	v, _, err := m.Version()
	if err != nil {
		t.Fatal(err)
	}

	if v != 1 {
		t.Fatalf("expected version 1, got %v", v)
	}
}

func TestRun(t *testing.T) {
	m, _ := New("stub://", "stub://")

	mx, err := NewMigration(nil, "", 1, 2)
	if err != nil {
		t.Fatal(err)
	}

	if err := m.Run(mx); err != nil {
		t.Fatal(err)
	}

	v, _, err := m.Version()
	if err != nil {
		t.Fatal(err)
	}

	if v != 2 {
		t.Errorf("expected version 2, got %v", v)
	}
}

func TestRunDirty(t *testing.T) {
	m, _ := New("stub://", "stub://")
	dbDrv := m.databaseDrv.(*dStub.Stub)
	if err := dbDrv.SetVersion(0, true); err != nil {
		t.Fatal(err)
	}

	migr, err := NewMigration(nil, "", 1, 2)
	if err != nil {
		t.Fatal(err)
	}

	err = m.Run(migr)
	if _, ok := err.(ErrDirty); !ok {
		t.Fatalf("expected ErrDirty, got %v", err)
	}
}

func TestForce(t *testing.T) {
	m, _ := New("stub://", "stub://")
	m.sourceDrv.(*sStub.Stub).Migrations = sourceStubMigrations

	if err := m.Force(7); err != nil {
		t.Fatal(err)
	}

	v, dirty, err := m.Version()
	if err != nil {
		t.Fatal(err)
	}
	if dirty {
		t.Errorf("expected dirty to be false")
	}
	if v != 7 {
		t.Errorf("expected version to be 7")
	}
}

func TestForceDirty(t *testing.T) {
	m, _ := New("stub://", "stub://")
	dbDrv := m.databaseDrv.(*dStub.Stub)
	if err := dbDrv.SetVersion(0, true); err != nil {
		t.Fatal(err)
	}

	if err := m.Force(1); err != nil {
		t.Fatal(err)
	}
}

func TestRead(t *testing.T) {
	m, _ := New("stub://", "stub://")
	m.sourceDrv.(*sStub.Stub).Migrations = sourceStubMigrations

	tt := []struct {
		from             int
		to               int
		expectErr        error
		expectMigrations migrationSequence
	}{
		{from: -1, to: -1, expectErr: ErrNoChange},
		{from: -1, to: 0, expectErr: os.ErrNotExist},
		{from: -1, to: 1, expectErr: nil, expectMigrations: newMigSeq(M(1))},
		{from: -1, to: 2, expectErr: os.ErrNotExist},
		{from: -1, to: 3, expectErr: nil, expectMigrations: newMigSeq(M(1), M(3))},
		{from: -1, to: 4, expectErr: nil, expectMigrations: newMigSeq(M(1), M(3), M(4))},
		{from: -1, to: 5, expectErr: nil, expectMigrations: newMigSeq(M(1), M(3), M(4), M(5))},
		{from: -1, to: 6, expectErr: os.ErrNotExist},
		{from: -1, to: 7, expectErr: nil, expectMigrations: newMigSeq(M(1), M(3), M(4), M(5), M(7))},
		{from: -1, to: 8, expectErr: os.ErrNotExist},

		{from: 0, to: -1, expectErr: os.ErrNotExist},
		{from: 0, to: 0, expectErr: os.ErrNotExist},
		{from: 0, to: 1, expectErr: os.ErrNotExist},
		{from: 0, to: 2, expectErr: os.ErrNotExist},
		{from: 0, to: 3, expectErr: os.ErrNotExist},
		{from: 0, to: 4, expectErr: os.ErrNotExist},
		{from: 0, to: 5, expectErr: os.ErrNotExist},
		{from: 0, to: 6, expectErr: os.ErrNotExist},
		{from: 0, to: 7, expectErr: os.ErrNotExist},
		{from: 0, to: 8, expectErr: os.ErrNotExist},

		{from: 1, to: -1, expectErr: nil, expectMigrations: newMigSeq(M(1, -1))},
		{from: 1, to: 0, expectErr: os.ErrNotExist},
		{from: 1, to: 1, expectErr: ErrNoChange},
		{from: 1, to: 2, expectErr: os.ErrNotExist},
		{from: 1, to: 3, expectErr: nil, expectMigrations: newMigSeq(M(3))},
		{from: 1, to: 4, expectErr: nil, expectMigrations: newMigSeq(M(3), M(4))},
		{from: 1, to: 5, expectErr: nil, expectMigrations: newMigSeq(M(3), M(4), M(5))},
		{from: 1, to: 6, expectErr: os.ErrNotExist},
		{from: 1, to: 7, expectErr: nil, expectMigrations: newMigSeq(M(3), M(4), M(5), M(7))},
		{from: 1, to: 8, expectErr: os.ErrNotExist},

		{from: 2, to: -1, expectErr: os.ErrNotExist},
		{from: 2, to: 0, expectErr: os.ErrNotExist},
		{from: 2, to: 1, expectErr: os.ErrNotExist},
		{from: 2, to: 2, expectErr: os.ErrNotExist},
		{from: 2, to: 3, expectErr: os.ErrNotExist},
		{from: 2, to: 4, expectErr: os.ErrNotExist},
		{from: 2, to: 5, expectErr: os.ErrNotExist},
		{from: 2, to: 6, expectErr: os.ErrNotExist},
		{from: 2, to: 7, expectErr: os.ErrNotExist},
		{from: 2, to: 8, expectErr: os.ErrNotExist},

		{from: 3, to: -1, expectErr: nil, expectMigrations: newMigSeq(M(3, 1), M(1, -1))},
		{from: 3, to: 0, expectErr: os.ErrNotExist},
		{from: 3, to: 1, expectErr: nil, expectMigrations: newMigSeq(M(3, 1))},
		{from: 3, to: 2, expectErr: os.ErrNotExist},
		{from: 3, to: 3, expectErr: ErrNoChange},
		{from: 3, to: 4, expectErr: nil, expectMigrations: newMigSeq(M(4))},
		{from: 3, to: 5, expectErr: nil, expectMigrations: newMigSeq(M(4), M(5))},
		{from: 3, to: 6, expectErr: os.ErrNotExist},
		{from: 3, to: 7, expectErr: nil, expectMigrations: newMigSeq(M(4), M(5), M(7))},
		{from: 3, to: 8, expectErr: os.ErrNotExist},

		{from: 4, to: -1, expectErr: nil, expectMigrations: newMigSeq(M(4, 3), M(3, 1), M(1, -1))},
		{from: 4, to: 0, expectErr: os.ErrNotExist},
		{from: 4, to: 1, expectErr: nil, expectMigrations: newMigSeq(M(4, 3), M(3, 1))},
		{from: 4, to: 2, expectErr: os.ErrNotExist},
		{from: 4, to: 3, expectErr: nil, expectMigrations: newMigSeq(M(4, 3))},
		{from: 4, to: 4, expectErr: ErrNoChange},
		{from: 4, to: 5, expectErr: nil, expectMigrations: newMigSeq(M(5))},
		{from: 4, to: 6, expectErr: os.ErrNotExist},
		{from: 4, to: 7, expectErr: nil, expectMigrations: newMigSeq(M(5), M(7))},
		{from: 4, to: 8, expectErr: os.ErrNotExist},

		{from: 5, to: -1, expectErr: nil, expectMigrations: newMigSeq(M(5, 4), M(4, 3), M(3, 1), M(1, -1))},
		{from: 5, to: 0, expectErr: os.ErrNotExist},
		{from: 5, to: 1, expectErr: nil, expectMigrations: newMigSeq(M(5, 4), M(4, 3), M(3, 1))},
		{from: 5, to: 2, expectErr: os.ErrNotExist},
		{from: 5, to: 3, expectErr: nil, expectMigrations: newMigSeq(M(5, 4), M(4, 3))},
		{from: 5, to: 4, expectErr: nil, expectMigrations: newMigSeq(M(5, 4))},
		{from: 5, to: 5, expectErr: ErrNoChange},
		{from: 5, to: 6, expectErr: os.ErrNotExist},
		{from: 5, to: 7, expectErr: nil, expectMigrations: newMigSeq(M(7))},
		{from: 5, to: 8, expectErr: os.ErrNotExist},

		{from: 6, to: -1, expectErr: os.ErrNotExist},
		{from: 6, to: 0, expectErr: os.ErrNotExist},
		{from: 6, to: 1, expectErr: os.ErrNotExist},
		{from: 6, to: 2, expectErr: os.ErrNotExist},
		{from: 6, to: 3, expectErr: os.ErrNotExist},
		{from: 6, to: 4, expectErr: os.ErrNotExist},
		{from: 6, to: 5, expectErr: os.ErrNotExist},
		{from: 6, to: 6, expectErr: os.ErrNotExist},
		{from: 6, to: 7, expectErr: os.ErrNotExist},
		{from: 6, to: 8, expectErr: os.ErrNotExist},

		{from: 7, to: -1, expectErr: nil, expectMigrations: newMigSeq(M(7, 5), M(5, 4), M(4, 3), M(3, 1), M(1, -1))},
		{from: 7, to: 0, expectErr: os.ErrNotExist},
		{from: 7, to: 1, expectErr: nil, expectMigrations: newMigSeq(M(7, 5), M(5, 4), M(4, 3), M(3, 1))},
		{from: 7, to: 2, expectErr: os.ErrNotExist},
		{from: 7, to: 3, expectErr: nil, expectMigrations: newMigSeq(M(7, 5), M(5, 4), M(4, 3))},
		{from: 7, to: 4, expectErr: nil, expectMigrations: newMigSeq(M(7, 5), M(5, 4))},
		{from: 7, to: 5, expectErr: nil, expectMigrations: newMigSeq(M(7, 5))},
		{from: 7, to: 6, expectErr: os.ErrNotExist},
		{from: 7, to: 7, expectErr: ErrNoChange},
		{from: 7, to: 8, expectErr: os.ErrNotExist},

		{from: 8, to: -1, expectErr: os.ErrNotExist},
		{from: 8, to: 0, expectErr: os.ErrNotExist},
		{from: 8, to: 1, expectErr: os.ErrNotExist},
		{from: 8, to: 2, expectErr: os.ErrNotExist},
		{from: 8, to: 3, expectErr: os.ErrNotExist},
		{from: 8, to: 4, expectErr: os.ErrNotExist},
		{from: 8, to: 5, expectErr: os.ErrNotExist},
		{from: 8, to: 6, expectErr: os.ErrNotExist},
		{from: 8, to: 7, expectErr: os.ErrNotExist},
		{from: 8, to: 8, expectErr: os.ErrNotExist},
	}

	for i, v := range tt {
		ret := make(chan interface{})
		go m.read(v.from, v.to, ret)
		migrations, err := migrationsFromChannel(ret)

		if (v.expectErr == os.ErrNotExist && !errors.Is(err, os.ErrNotExist)) ||
			(v.expectErr != os.ErrNotExist && v.expectErr != err) {
			t.Errorf("expected %v, got %v, in %v", v.expectErr, err, i)
			t.Logf("%v, in %v", migrations, i)
		}
		if len(v.expectMigrations) > 0 {
			equalMigSeq(t, i, v.expectMigrations, migrations)
		}
	}
}

func TestReadUp(t *testing.T) {
	m, _ := New("stub://", "stub://")
	m.sourceDrv.(*sStub.Stub).Migrations = sourceStubMigrations

	tt := []struct {
		from             int
		limit            int // -1 means no limit
		expectErr        error
		expectMigrations migrationSequence
	}{
		{from: -1, limit: -1, expectErr: nil, expectMigrations: newMigSeq(M(1), M(3), M(4), M(5), M(7))},
		{from: -1, limit: 0, expectErr: ErrNoChange},
		{from: -1, limit: 1, expectErr: nil, expectMigrations: newMigSeq(M(1))},
		{from: -1, limit: 2, expectErr: nil, expectMigrations: newMigSeq(M(1), M(3))},

		{from: 0, limit: -1, expectErr: os.ErrNotExist},
		{from: 0, limit: 0, expectErr: os.ErrNotExist},
		{from: 0, limit: 1, expectErr: os.ErrNotExist},
		{from: 0, limit: 2, expectErr: os.ErrNotExist},

		{from: 1, limit: -1, expectErr: nil, expectMigrations: newMigSeq(M(3), M(4), M(5), M(7))},
		{from: 1, limit: 0, expectErr: ErrNoChange},
		{from: 1, limit: 1, expectErr: nil, expectMigrations: newMigSeq(M(3))},
		{from: 1, limit: 2, expectErr: nil, expectMigrations: newMigSeq(M(3), M(4))},

		{from: 2, limit: -1, expectErr: os.ErrNotExist},
		{from: 2, limit: 0, expectErr: os.ErrNotExist},
		{from: 2, limit: 1, expectErr: os.ErrNotExist},
		{from: 2, limit: 2, expectErr: os.ErrNotExist},

		{from: 3, limit: -1, expectErr: nil, expectMigrations: newMigSeq(M(4), M(5), M(7))},
		{from: 3, limit: 0, expectErr: ErrNoChange},
		{from: 3, limit: 1, expectErr: nil, expectMigrations: newMigSeq(M(4))},
		{from: 3, limit: 2, expectErr: nil, expectMigrations: newMigSeq(M(4), M(5))},

		{from: 4, limit: -1, expectErr: nil, expectMigrations: newMigSeq(M(5), M(7))},
		{from: 4, limit: 0, expectErr: ErrNoChange},
		{from: 4, limit: 1, expectErr: nil, expectMigrations: newMigSeq(M(5))},
		{from: 4, limit: 2, expectErr: nil, expectMigrations: newMigSeq(M(5), M(7))},

		{from: 5, limit: -1, expectErr: nil, expectMigrations: newMigSeq(M(7))},
		{from: 5, limit: 0, expectErr: ErrNoChange},
		{from: 5, limit: 1, expectErr: nil, expectMigrations: newMigSeq(M(7))},
		{from: 5, limit: 2, expectErr: ErrShortLimit{1}, expectMigrations: newMigSeq(M(7))},

		{from: 6, limit: -1, expectErr: os.ErrNotExist},
		{from: 6, limit: 0, expectErr: os.ErrNotExist},
		{from: 6, limit: 1, expectErr: os.ErrNotExist},
		{from: 6, limit: 2, expectErr: os.ErrNotExist},

		{from: 7, limit: -1, expectErr: ErrNoChange},
		{from: 7, limit: 0, expectErr: ErrNoChange},
		{from: 7, limit: 1, expectErr: os.ErrNotExist},
		{from: 7, limit: 2, expectErr: os.ErrNotExist},

		{from: 8, limit: -1, expectErr: os.ErrNotExist},
		{from: 8, limit: 0, expectErr: os.ErrNotExist},
		{from: 8, limit: 1, expectErr: os.ErrNotExist},
		{from: 8, limit: 2, expectErr: os.ErrNotExist},
	}

	for i, v := range tt {
		ret := make(chan interface{})
		go m.readUp(v.from, v.limit, ret)
		migrations, err := migrationsFromChannel(ret)

		if (v.expectErr == os.ErrNotExist && !errors.Is(err, os.ErrNotExist)) ||
			(v.expectErr != os.ErrNotExist && v.expectErr != err) {
			t.Errorf("expected %v, got %v, in %v", v.expectErr, err, i)
			t.Logf("%v, in %v", migrations, i)
		}
		if len(v.expectMigrations) > 0 {
			equalMigSeq(t, i, v.expectMigrations, migrations)
		}
	}
}

func TestReadDown(t *testing.T) {
	m, _ := New("stub://", "stub://")
	m.sourceDrv.(*sStub.Stub).Migrations = sourceStubMigrations

	tt := []struct {
		from             int
		limit            int // -1 means no limit
		expectErr        error
		expectMigrations migrationSequence
	}{
		{from: -1, limit: -1, expectErr: ErrNoChange},
		{from: -1, limit: 0, expectErr: ErrNoChange},
		{from: -1, limit: 1, expectErr: os.ErrNotExist},
		{from: -1, limit: 2, expectErr: os.ErrNotExist},

		{from: 0, limit: -1, expectErr: os.ErrNotExist},
		{from: 0, limit: 0, expectErr: os.ErrNotExist},
		{from: 0, limit: 1, expectErr: os.ErrNotExist},
		{from: 0, limit: 2, expectErr: os.ErrNotExist},

		{from: 1, limit: -1, expectErr: nil, expectMigrations: newMigSeq(M(1, -1))},
		{from: 1, limit: 0, expectErr: ErrNoChange},
		{from: 1, limit: 1, expectErr: nil, expectMigrations: newMigSeq(M(1, -1))},
		{from: 1, limit: 2, expectErr: ErrShortLimit{1}, expectMigrations: newMigSeq(M(1, -1))},

		{from: 2, limit: -1, expectErr: os.ErrNotExist},
		{from: 2, limit: 0, expectErr: os.ErrNotExist},
		{from: 2, limit: 1, expectErr: os.ErrNotExist},
		{from: 2, limit: 2, expectErr: os.ErrNotExist},

		{from: 3, limit: -1, expectErr: nil, expectMigrations: newMigSeq(M(3, 1), M(1, -1))},
		{from: 3, limit: 0, expectErr: ErrNoChange},
		{from: 3, limit: 1, expectErr: nil, expectMigrations: newMigSeq(M(3, 1))},
		{from: 3, limit: 2, expectErr: nil, expectMigrations: newMigSeq(M(3, 1), M(1, -1))},

		{from: 4, limit: -1, expectErr: nil, expectMigrations: newMigSeq(M(4, 3), M(3, 1), M(1, -1))},
		{from: 4, limit: 0, expectErr: ErrNoChange},
		{from: 4, limit: 1, expectErr: nil, expectMigrations: newMigSeq(M(4, 3))},
		{from: 4, limit: 2, expectErr: nil, expectMigrations: newMigSeq(M(4, 3), M(3, 1))},

		{from: 5, limit: -1, expectErr: nil, expectMigrations: newMigSeq(M(5, 4), M(4, 3), M(3, 1), M(1, -1))},
		{from: 5, limit: 0, expectErr: ErrNoChange},
		{from: 5, limit: 1, expectErr: nil, expectMigrations: newMigSeq(M(5, 4))},
		{from: 5, limit: 2, expectErr: nil, expectMigrations: newMigSeq(M(5, 4), M(4, 3))},

		{from: 6, limit: -1, expectErr: os.ErrNotExist},
		{from: 6, limit: 0, expectErr: os.ErrNotExist},
		{from: 6, limit: 1, expectErr: os.ErrNotExist},
		{from: 6, limit: 2, expectErr: os.ErrNotExist},

		{from: 7, limit: -1, expectErr: nil, expectMigrations: newMigSeq(M(7, 5), M(5, 4), M(4, 3), M(3, 1), M(1, -1))},
		{from: 7, limit: 0, expectErr: ErrNoChange},
		{from: 7, limit: 1, expectErr: nil, expectMigrations: newMigSeq(M(7, 5))},
		{from: 7, limit: 2, expectErr: nil, expectMigrations: newMigSeq(M(7, 5), M(5, 4))},

		{from: 8, limit: -1, expectErr: os.ErrNotExist},
		{from: 8, limit: 0, expectErr: os.ErrNotExist},
		{from: 8, limit: 1, expectErr: os.ErrNotExist},
		{from: 8, limit: 2, expectErr: os.ErrNotExist},
	}

	for i, v := range tt {
		ret := make(chan interface{})
		go m.readDown(v.from, v.limit, ret)
		migrations, err := migrationsFromChannel(ret)

		if (v.expectErr == os.ErrNotExist && !errors.Is(err, os.ErrNotExist)) ||
			(v.expectErr != os.ErrNotExist && v.expectErr != err) {
			t.Errorf("expected %v, got %v, in %v", v.expectErr, err, i)
			t.Logf("%v, in %v", migrations, i)
		}
		if len(v.expectMigrations) > 0 {
			equalMigSeq(t, i, v.expectMigrations, migrations)
		}
	}
}

func TestLock(t *testing.T) {
	m, _ := New("stub://", "stub://")
	if err := m.lock(); err != nil {
		t.Fatal(err)
	}

	if err := m.lock(); err == nil {
		t.Fatal("should be locked already")
	}
}

func migrationsFromChannel(ret chan interface{}) ([]*Migration, error) {
	slice := make([]*Migration, 0)
	for r := range ret {
		switch t := r.(type) {
		case error:
			return slice, t

		case *Migration:
			slice = append(slice, t)
		}
	}
	return slice, nil
}

type migrationSequence []*Migration

func newMigSeq(migr ...*Migration) migrationSequence {
	return migr
}

func (m *migrationSequence) bodySequence() []string {
	r := make([]string, 0)
	for _, v := range *m {
		if v.Body != nil {
			body, err := io.ReadAll(v.Body)
			if err != nil {
				panic(err) // that should never happen
			}

			// reset body reader
			// TODO: is there a better/nicer way?
			v.Body = io.NopCloser(bytes.NewReader(body))

			r = append(r, string(body[:]))
		} else {
			r = append(r, "<empty>")
		}
	}
	return r
}

// M is a convenience func to create a new *Migration
func M(version uint, targetVersion ...int) *Migration {
	if len(targetVersion) > 1 {
		panic("only one targetVersion allowed")
	}
	ts := int(version)
	if len(targetVersion) == 1 {
		ts = targetVersion[0]
	}

	m, _ := New("stub://", "stub://")
	m.sourceDrv.(*sStub.Stub).Migrations = sourceStubMigrations
	migr, err := m.newMigration(version, ts)
	if err != nil {
		panic(err)
	}
	return migr
}

// mr is a convenience func to create a new *Migration from the raw database query
func mr(value string) *Migration {
	return &Migration{
		Body: io.NopCloser(strings.NewReader(value)),
	}
}

func equalMigSeq(t *testing.T, i int, expected, got migrationSequence) {
	if len(expected) != len(got) {
		t.Errorf("expected migrations %v, got %v, in %v", expected, got, i)

	} else {
		for ii := 0; ii < len(expected); ii++ {
			if expected[ii].Version != got[ii].Version {
				t.Errorf("expected version %v, got %v, in %v", expected[ii].Version, got[ii].Version, i)
			}

			if expected[ii].TargetVersion != got[ii].TargetVersion {
				t.Errorf("expected targetVersion %v, got %v, in %v", expected[ii].TargetVersion, got[ii].TargetVersion, i)
			}
		}
	}
}

func equalDbSeq(t *testing.T, i int, expected migrationSequence, got *dStub.Stub) {
	bs := expected.bodySequence()
	if !got.EqualSequence(bs) {
		t.Fatalf("\nexpected sequence %v,\ngot               %v, in %v", bs, got.MigrationSequence, i)
	}
}
```

## File: `migration.go`
```go
package migrate

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"time"
)

// DefaultBufferSize sets the in memory buffer size (in Bytes) for every
// pre-read migration (see DefaultPrefetchMigrations).
var DefaultBufferSize = uint(100000)

// Migration holds information about a migration.
// It is initially created from data coming from the source and then
// used when run against the database.
type Migration struct {
	// Identifier can be any string to help identifying
	// the migration in the source.
	Identifier string

	// Version is the version of this migration.
	Version uint

	// TargetVersion is the migration version after this migration
	// has been applied to the database.
	// Can be -1, implying that this is a NilVersion.
	TargetVersion int

	// Body holds an io.ReadCloser to the source.
	Body io.ReadCloser

	// BufferedBody holds an buffered io.Reader to the underlying Body.
	BufferedBody io.Reader

	// BufferSize defaults to DefaultBufferSize
	BufferSize uint

	// bufferWriter holds an io.WriteCloser and pipes to BufferBody.
	// It's an *Closer for flow control.
	bufferWriter io.WriteCloser

	// Scheduled is the time when the migration was scheduled/ queued.
	Scheduled time.Time

	// StartedBuffering is the time when buffering of the migration source started.
	StartedBuffering time.Time

	// FinishedBuffering is the time when buffering of the migration source finished.
	FinishedBuffering time.Time

	// FinishedReading is the time when the migration source is fully read.
	FinishedReading time.Time

	// BytesRead holds the number of Bytes read from the migration source.
	BytesRead int64
}

// NewMigration returns a new Migration and sets the body, identifier,
// version and targetVersion. Body can be nil, which turns this migration
// into a "NilMigration". If no identifier is provided, it will default to "<empty>".
// targetVersion can be -1, implying it is a NilVersion.
//
// What is a NilMigration?
// Usually each migration version coming from source is expected to have an
// Up and Down migration. This is not a hard requirement though, leading to
// a situation where only the Up or Down migration is present. So let's say
// the user wants to migrate up to a version that doesn't have the actual Up
// migration, in that case we still want to apply the version, but with an empty
// body. We are calling that a NilMigration, a migration with an empty body.
//
// What is a NilVersion?
// NilVersion is a const(-1). When running down migrations and we are at the
// last down migration, there is no next down migration, the targetVersion should
// be nil. Nil in this case is represented by -1 (because type int).
func NewMigration(body io.ReadCloser, identifier string,
	version uint, targetVersion int) (*Migration, error) {
	tnow := time.Now()
	m := &Migration{
		Identifier:    identifier,
		Version:       version,
		TargetVersion: targetVersion,
		Scheduled:     tnow,
	}

	if body == nil {
		if len(identifier) == 0 {
			m.Identifier = "<empty>"
		}

		m.StartedBuffering = tnow
		m.FinishedBuffering = tnow
		m.FinishedReading = tnow
		return m, nil
	}

	br, bw := io.Pipe()
	m.Body = body // want to simulate low latency? newSlowReader(body)
	m.BufferSize = DefaultBufferSize
	m.BufferedBody = br
	m.bufferWriter = bw
	return m, nil
}

// String implements string.Stringer and is used in tests.
func (m *Migration) String() string {
	return fmt.Sprintf("%v [%v=>%v]", m.Identifier, m.Version, m.TargetVersion)
}

// LogString returns a string describing this migration to humans.
func (m *Migration) LogString() string {
	directionStr := "u"
	if m.TargetVersion < int(m.Version) {
		directionStr = "d"
	}
	return fmt.Sprintf("%v/%v %v", m.Version, directionStr, m.Identifier)
}

// Buffer buffers Body up to BufferSize.
// Calling this function blocks. Call with goroutine.
func (m *Migration) Buffer() (berr error) {
	if m.Body == nil {
		return nil
	}

	m.StartedBuffering = time.Now()

	b := bufio.NewReaderSize(m.Body, int(m.BufferSize))

	// defer closing buffer writer and body.
	defer func() {
		// close bufferWriter so Buffer knows that there is no
		// more data coming.
		if err := m.bufferWriter.Close(); err != nil {
			berr = errors.Join(berr, err)
		}

		// it's safe to close the Body too.
		if err := m.Body.Close(); err != nil {
			berr = errors.Join(berr, err)
		}

	}()

	// start reading from body, peek won't move the read pointer though
	// poor man's solution?
	if _, err := b.Peek(int(m.BufferSize)); err != nil && err != io.EOF {
		return err
	}

	m.FinishedBuffering = time.Now()

	// write to bufferWriter, this will block until
	// something starts reading from m.Buffer
	n, err := b.WriteTo(m.bufferWriter)
	if err != nil {
		return err
	}

	m.FinishedReading = time.Now()
	m.BytesRead = n

	return nil
}
```

## File: `MIGRATIONS.md`
```markdown
# Migrations

## Migration Filename Format

A single logical migration is represented as two separate migration files, one
to migrate "up" to the specified version from the previous version, and a second
to migrate back "down" to the previous version.  These migrations can be provided
by any one of the supported [migration sources](./README.md#migration-sources).

The ordering and direction of the migration files is determined by the filenames
used for them.  `migrate` expects the filenames of migrations to have the format:

    {version}_{title}.up.{extension}
    {version}_{title}.down.{extension}

The `title` of each migration is unused, and is only for readability.  Similarly,
the `extension` of the migration files is not checked by the library, and should
be an appropriate format for the database in use (`.sql` for SQL variants, for
instance).

Versions of migrations may be represented as any 64 bit unsigned integer.
All migrations are applied upward in order of increasing version number, and
downward by decreasing version number.

Common versioning schemes include incrementing integers:

    1_initialize_schema.down.sql
    1_initialize_schema.up.sql
    2_add_table.down.sql
    2_add_table.up.sql
    ...

Or timestamps at an appropriate resolution:

    1500360784_initialize_schema.down.sql
    1500360784_initialize_schema.up.sql
    1500445949_add_table.down.sql
    1500445949_add_table.up.sql
    ...

But any scheme resulting in distinct, incrementing integers as versions is valid.

It is suggested that the version number of corresponding `up` and `down` migration
files be equivalent for clarity, but they are allowed to differ so long as the
relative ordering of the migrations is preserved.

The migration files are permitted to be "empty", in the event that a migration
is a no-op or is irreversible. It is recommended to still include both migration
files by making the whole migration file consist of a comment.
If your database does not support comments, then deleting the migration file will also work.
Note, an actual empty file (e.g. a 0 byte file) may cause issues with your database since migrate
will attempt to run an empty query. In this case, deleting the migration file will also work.
For the rational of this behavior see:
[#244 (comment)](https://github.com/golang-migrate/migrate/issues/244#issuecomment-510758270)

## Migration Content Format

The format of the migration files themselves varies between database systems.
Different databases have different semantics around schema changes and when and
how they are allowed to occur
(for instance, [if schema changes can occur within a transaction](https://wiki.postgresql.org/wiki/Transactional_DDL_in_PostgreSQL:_A_Competitive_Analysis)).

As such, the `migrate` library has little to no checking around the format of
migration sources.  The migration files are generally processed directly by the
drivers as raw operations.

## Reversibility of Migrations

Best practice for writing schema migration is that all migrations should be
reversible.  It should in theory be possible for run migrations down and back up
through any and all versions with the state being fully cleaned and recreated
by doing so.

By adhering to this recommended practice, development and deployment of new code
is cleaner and easier (cleaning database state for a new feature should be as
easy as migrating down to a prior version, and back up to the latest).

As opposed to some other migration libraries, `migrate` represents up and down
migrations as separate files.  This prevents any non-standard file syntax from
being introduced which may result in unintended behavior or errors, depending
on what database is processing the file.

While it is technically possible for an up or down migration to exist on its own
without an equivalently versioned counterpart, it is strongly recommended to
always include a down migration which cleans up the state of the corresponding
up migration.
```

## File: `migration_test.go`
```go
package migrate

import (
	"fmt"
	"io"
	"log"
	"strings"
)

func ExampleNewMigration() {
	// Create a dummy migration body, this is coming from the source usually.
	body := io.NopCloser(strings.NewReader("dumy migration that creates users table"))

	// Create a new Migration that represents version 1486686016.
	// Once this migration has been applied to the database, the new
	// migration version will be 1486689359.
	migr, err := NewMigration(body, "create_users_table", 1486686016, 1486689359)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Print(migr.LogString())
	// Output:
	// 1486686016/u create_users_table
}

func ExampleNewMigration_nilMigration() {
	// Create a new Migration that represents a NilMigration.
	// Once this migration has been applied to the database, the new
	// migration version will be 1486689359.
	migr, err := NewMigration(nil, "", 1486686016, 1486689359)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Print(migr.LogString())
	// Output:
	// 1486686016/u <empty>
}

func ExampleNewMigration_nilVersion() {
	// Create a dummy migration body, this is coming from the source usually.
	body := io.NopCloser(strings.NewReader("dumy migration that deletes users table"))

	// Create a new Migration that represents version 1486686016.
	// This is the last available down migration, so the migration version
	// will be -1, meaning NilVersion once this migration ran.
	migr, err := NewMigration(body, "drop_users_table", 1486686016, -1)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Print(migr.LogString())
	// Output:
	// 1486686016/d drop_users_table
}
```

## File: `README.md`
```markdown
[![GitHub Workflow Status (branch)](https://img.shields.io/github/actions/workflow/status/golang-migrate/migrate/ci.yaml?branch=master)](https://github.com/golang-migrate/migrate/actions/workflows/ci.yaml?query=branch%3Amaster)
[![GoDoc](https://pkg.go.dev/badge/github.com/golang-migrate/migrate)](https://pkg.go.dev/github.com/golang-migrate/migrate/v4)
[![Coverage Status](https://img.shields.io/coveralls/github/golang-migrate/migrate/master.svg)](https://coveralls.io/github/golang-migrate/migrate?branch=master)
[![packagecloud.io](https://img.shields.io/badge/deb-packagecloud.io-844fec.svg)](https://packagecloud.io/golang-migrate/migrate?filter=debs)
[![Docker Pulls](https://img.shields.io/docker/pulls/migrate/migrate.svg)](https://hub.docker.com/r/migrate/migrate/)
![Supported Go Versions](https://img.shields.io/badge/Go-1.24%2C%201.25-lightgrey.svg)
[![GitHub Release](https://img.shields.io/github/release/golang-migrate/migrate.svg)](https://github.com/golang-migrate/migrate/releases)
[![Go Report Card](https://goreportcard.com/badge/github.com/golang-migrate/migrate/v4)](https://goreportcard.com/report/github.com/golang-migrate/migrate/v4)

# migrate

__Database migrations written in Go. Use as [CLI](#cli-usage) or import as [library](#use-in-your-go-project).__

* Migrate reads migrations from [sources](#migration-sources)
   and applies them in correct order to a [database](#databases).
* Drivers are "dumb", migrate glues everything together and makes sure the logic is bulletproof.
   (Keeps the drivers lightweight, too.)
* Database drivers don't assume things or try to correct user input. When in doubt, fail.

Forked from [mattes/migrate](https://github.com/mattes/migrate)

## Databases

Database drivers run migrations. [Add a new database?](database/driver.go)

* [PostgreSQL](database/postgres)
* [PGX v4](database/pgx)
* [PGX v5](database/pgx/v5)
* [Redshift](database/redshift)
* [Ql](database/ql)
* [Cassandra / ScyllaDB](database/cassandra)
* [SQLite](database/sqlite)
* [SQLite3](database/sqlite3) ([todo #165](https://github.com/mattes/migrate/issues/165))
* [SQLCipher](database/sqlcipher)
* [MySQL / MariaDB](database/mysql)
* [Neo4j](database/neo4j)
* [MongoDB](database/mongodb)
* [CrateDB](database/crate) ([todo #170](https://github.com/mattes/migrate/issues/170))
* [Shell](database/shell) ([todo #171](https://github.com/mattes/migrate/issues/171))
* [Google Cloud Spanner](database/spanner)
* [CockroachDB](database/cockroachdb)
* [YugabyteDB](database/yugabytedb)
* [ClickHouse](database/clickhouse)
* [Firebird](database/firebird)
* [MS SQL Server](database/sqlserver)
* [rqlite](database/rqlite)

### Database URLs

Database connection strings are specified via URLs. The URL format is driver dependent but generally has the form: `dbdriver://username:password@host:port/dbname?param1=true&param2=false`

Any [reserved URL characters](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters) need to be escaped. Note, the `%` character also [needs to be escaped](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_the_percent_character)

Explicitly, the following characters need to be escaped:
`!`, `#`, `$`, `%`, `&`, `'`, `(`, `)`, `*`, `+`, `,`, `/`, `:`, `;`, `=`, `?`, `@`, `[`, `]`

It's easiest to always run the URL parts of your DB connection URL (e.g. username, password, etc) through an URL encoder. See the example Python snippets below:

```bash
$ python3 -c 'import urllib.parse; print(urllib.parse.quote(input("String to encode: "), ""))'
String to encode: FAKEpassword!#$%&'()*+,/:;=?@[]
FAKEpassword%21%23%24%25%26%27%28%29%2A%2B%2C%2F%3A%3B%3D%3F%40%5B%5D
$ python2 -c 'import urllib; print urllib.quote(raw_input("String to encode: "), "")'
String to encode: FAKEpassword!#$%&'()*+,/:;=?@[]
FAKEpassword%21%23%24%25%26%27%28%29%2A%2B%2C%2F%3A%3B%3D%3F%40%5B%5D
$
```

## Migration Sources

Source drivers read migrations from local or remote sources. [Add a new source?](source/driver.go)

* [Filesystem](source/file) - read from filesystem
* [io/fs](source/iofs) - read from a Go [io/fs](https://pkg.go.dev/io/fs#FS)
* [Go-Bindata](source/go_bindata) - read from embedded binary data ([jteeuwen/go-bindata](https://github.com/jteeuwen/go-bindata))
* [pkger](source/pkger) - read from embedded binary data ([markbates/pkger](https://github.com/markbates/pkger))
* [GitHub](source/github) - read from remote GitHub repositories
* [GitHub Enterprise](source/github_ee) - read from remote GitHub Enterprise repositories
* [Bitbucket](source/bitbucket) - read from remote Bitbucket repositories
* [Gitlab](source/gitlab) - read from remote Gitlab repositories
* [AWS S3](source/aws_s3) - read from Amazon Web Services S3
* [Google Cloud Storage](source/google_cloud_storage) - read from Google Cloud Platform Storage

## CLI usage

* Simple wrapper around this library.
* Handles ctrl+c (SIGINT) gracefully.
* No config search paths, no config files, no magic ENV var injections.

[CLI Documentation](cmd/migrate) (includes CLI install instructions)

### Basic usage

```bash
$ migrate -source file://path/to/migrations -database postgres://localhost:5432/database up 2
```

### Docker usage

```bash
$ docker run -v {{ migration dir }}:/migrations --network host migrate/migrate
    -path=/migrations/ -database postgres://localhost:5432/database up 2
```

## Use in your Go project

* API is stable and frozen for this release (v3 & v4).
* Uses [Go modules](https://golang.org/cmd/go/#hdr-Modules__module_versions__and_more) to manage dependencies.
* To help prevent database corruptions, it supports graceful stops via `GracefulStop chan bool`.
* Bring your own logger.
* Uses `io.Reader` streams internally for low memory overhead.
* Thread-safe and no goroutine leaks.

__[Go Documentation](https://pkg.go.dev/github.com/golang-migrate/migrate/v4)__

```go
import (
    "github.com/golang-migrate/migrate/v4"
    _ "github.com/golang-migrate/migrate/v4/database/postgres"
    _ "github.com/golang-migrate/migrate/v4/source/github"
)

func main() {
    m, err := migrate.New(
        "github://mattes:personal-access-token@mattes/migrate_test",
        "postgres://localhost:5432/database?sslmode=enable")
    m.Steps(2)
}
```

Want to use an existing database client?

```go
import (
    "database/sql"
    _ "github.com/lib/pq"
    "github.com/golang-migrate/migrate/v4"
    "github.com/golang-migrate/migrate/v4/database/postgres"
    _ "github.com/golang-migrate/migrate/v4/source/file"
)

func main() {
    db, err := sql.Open("postgres", "postgres://localhost:5432/database?sslmode=enable")
    driver, err := postgres.WithInstance(db, &postgres.Config{})
    m, err := migrate.NewWithDatabaseInstance(
        "file:///migrations",
        "postgres", driver)
    m.Up() // or m.Steps(2) if you want to explicitly set the number of migrations to run
}
```

## Getting started

Go to [getting started](../corp/docs/usage_guides/getting_started.md)

## Tutorials

* [CockroachDB](../../../core/security/QUARANTINE/vetted/repos/documentation/i18n/en/docusaurus_plugin_content_docs/current/get_started/tutorial.md)
* [PostgreSQL](../../../core/security/QUARANTINE/vetted/repos/documentation/i18n/en/docusaurus_plugin_content_docs/current/get_started/tutorial.md)

(more tutorials to come)

## Migration files

Each migration has an up and down migration. [Why?](FAQ.md#why-two-separate-files-up-and-down-for-a-migration)

```bash
1481574547_create_users_table.up.sql
1481574547_create_users_table.down.sql
```

[Best practices: How to write migrations.](MIGRATIONS.md)

## Coming from another db migration tool?

Check out [migradaptor](https://github.com/musinit/migradaptor/).
*Note: migradaptor is not affiliated or supported by this project*

## Versions

Version | Supported? | Import | Notes
--------|------------|--------|------
**master** | :white_check_mark: | `import "github.com/golang-migrate/migrate/v4"` | New features and bug fixes arrive here first |
**v4** | :white_check_mark: | `import "github.com/golang-migrate/migrate/v4"` | Used for stable releases |
**v3** | :x: | `import "github.com/golang-migrate/migrate"` (with package manager) or `import "gopkg.in/golang-migrate/migrate.v3"` (not recommended) | **DO NOT USE** - No longer supported |

## Development and Contributing

Yes, please! [`Makefile`](Makefile) is your friend,
read the [development guide](CONTRIBUTING.md).

Also have a look at the [FAQ](FAQ.md).

---

Looking for alternatives? [https://awesome-go.com/#database](https://awesome-go.com/#database).
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| master  | :white_check_mark: |
| 4.x     | :white_check_mark: |
| 3.x     | :x:                |
| < 3.0   | :x:                |

## Reporting a Vulnerability

We prefer [coordinated disclosures](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure). To start one, create a GitHub security advisory following [these instructions](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)

Please suggest potential impact and urgency in your reports.
```

## File: `util.go`
```go
package migrate

import (
	"fmt"
	nurl "net/url"
	"strings"
)

// MultiError holds multiple errors.
//
// Deprecated: Use stdlib's [errors.Join] et al. instead
// This will be removed in the v5 release.
type MultiError struct {
	Errs []error
}

// NewMultiError returns an error type holding multiple errors.
//
// Deprecated: Use stdlib's [errors.Join] et al. instead
// This will be removed in the v5 release.
func NewMultiError(errs ...error) MultiError {
	compactErrs := make([]error, 0)
	for _, e := range errs {
		if e != nil {
			compactErrs = append(compactErrs, e)
		}
	}
	return MultiError{compactErrs}
}

// Error implements error. Multiple errors are concatenated with 'and's.
func (m MultiError) Error() string {
	var strs = make([]string, 0)
	for _, e := range m.Errs {
		if len(e.Error()) > 0 {
			strs = append(strs, e.Error())
		}
	}
	return strings.Join(strs, " and ")
}

// suint safely converts int to uint
// see https://goo.gl/wEcqof
// see https://goo.gl/pai7Dr
func suint(n int) uint {
	if n < 0 {
		panic(fmt.Sprintf("suint(%v) expects input >= 0", n))
	}
	return uint(n)
}

// FilterCustomQuery filters all query values starting with `x-`
func FilterCustomQuery(u *nurl.URL) *nurl.URL {
	ux := *u
	vx := make(nurl.Values)
	for k, v := range ux.Query() {
		if len(k) <= 1 || k[0:2] != "x-" {
			vx[k] = v
		}
	}
	ux.RawQuery = vx.Encode()
	return &ux
}
```

## File: `util_test.go`
```go
package migrate

import (
	nurl "net/url"
	"testing"
)

func TestSuintPanicsWithNegativeInput(t *testing.T) {
	defer func() {
		if r := recover(); r == nil {
			t.Fatal("expected suint to panic for -1")
		}
	}()
	suint(-1)
}

func TestSuint(t *testing.T) {
	if u := suint(0); u != 0 {
		t.Fatalf("expected 0, got %v", u)
	}
}

func TestFilterCustomQuery(t *testing.T) {
	n, err := nurl.Parse("foo://host?a=b&x-custom=foo&c=d&ok=y")
	if err != nil {
		t.Fatal(err)
	}
	nx := FilterCustomQuery(n).Query()
	if nx.Get("x-custom") != "" {
		t.Fatalf("didn't expect x-custom")
	}
	if nx.Get("ok") != "y" {
		t.Fatalf("expected ok=y, got %v", nx.Get("ok"))
	}
}
```

## File: `cli/main.go`
```go
package main

import "github.com/golang-migrate/migrate/v4/internal/cli"

// Deprecated, please use cmd/migrate
func main() {
	cli.Main(Version)
}
```

## File: `cli/README.md`
```markdown
# Deprecated

Use [cmd/migrate](../cmd/migrate) instead
```

## File: `cli/version.go`
```go
package main

// Version is set in Makefile with build flags
var Version = "dev"
```

## File: `cmd/migrate/main.go`
```go
package main

import "github.com/golang-migrate/migrate/v4/internal/cli"

func main() {
	cli.Main(Version)
}
```

## File: `cmd/migrate/README.md`
```markdown
# migrate CLI

## Installation

### Download pre-built binary (Windows, MacOS, or Linux)

[Release Downloads](https://github.com/golang-migrate/migrate/releases)

```bash
$ curl -L https://github.com/golang-migrate/migrate/releases/download/$version/migrate.$os-$arch.tar.gz | tar xvz
```

### MacOS

```bash
$ brew install golang-migrate
```

### Windows

Using [scoop](https://scoop.sh/)

```bash
$ scoop install migrate
```

### Linux (*.deb package)

```bash
$ curl -fsSL https://packagecloud.io/golang-migrate/migrate/gpgkey | sudo gpg --dearmor -o /etc/apt/keyrings/migrate.gpg
$ echo "deb [signed-by=/etc/apt/keyrings/migrate.gpg] https://packagecloud.io/golang-migrate/migrate/ubuntu/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/migrate.list
$ apt-get update
$ apt-get install -y migrate
```

### With Go toolchain

#### Versioned

```bash
$ go get -u -d github.com/golang-migrate/migrate/cmd/migrate
$ cd $GOPATH/src/github.com/golang-migrate/migrate/cmd/migrate
$ git checkout $TAG  # e.g. v4.1.0
$ # Go 1.15 and below
$ go build -tags 'postgres' -ldflags="-X main.Version=$(git describe --tags)" -o $GOPATH/bin/migrate $GOPATH/src/github.com/golang-migrate/migrate/cmd/migrate
$ # Go 1.16+
$ go install -tags 'postgres' github.com/golang-migrate/migrate/v4/cmd/migrate@$TAG
```

#### Unversioned

```bash
$ # Go 1.15 and below
$ go get -tags 'postgres' -u github.com/golang-migrate/migrate/cmd/migrate
$ # Go 1.16+
$ go install -tags 'postgres' github.com/golang-migrate/migrate/v4/cmd/migrate@latest
```

#### Notes

1. Requires a version of Go that [supports modules](https://golang.org/cmd/go/#hdr-Preliminary_module_support). e.g. Go 1.11+
1. These examples build the cli which will only work with postgres.  In order
to build the cli for use with other databases, replace the `postgres` build tag
with the appropriate database tag(s) for the databases desired.  The tags
correspond to the names of the sub-packages underneath the
[`database`](../../database) package.
1. Similarly to the database build tags, if you need to support other sources, use the appropriate build tag(s).
1. Support for build constraints will be removed in the future: https://github.com/golang-migrate/migrate/issues/60
1. For versions of Go 1.15 and lower, [make sure](https://github.com/golang-migrate/migrate/pull/257#issuecomment-705249902) you're not installing the `migrate` CLI from a module. e.g. there should not be any `go.mod` files in your current directory or any directory from your current directory to the root

## Usage

```bash
$ migrate -help
Usage: migrate OPTIONS COMMAND [arg...]
       migrate [ -version | -help ]

Options:
  -source          Location of the migrations (driver://url)
  -path            Shorthand for -source=file://path
  -database        Run migrations against this database (driver://url)
  -prefetch N      Number of migrations to load in advance before executing (default 10)
  -lock-timeout N  Allow N seconds to acquire database lock (default 15)
  -verbose         Print verbose logging
  -version         Print version
  -help            Print usage

Commands:
  create [-ext E] [-dir D] [-seq] [-digits N] [-format] [-tz] NAME
           Create a set of timestamped up/down migrations titled NAME, in directory D with extension E.
           Use -seq option to generate sequential up/down migrations with N digits.
           Use -format option to specify a Go time format string. Note: migrations with the same time cause "duplicate migration version" error.
           Use -tz option to specify the timezone that will be used when generating non-sequential migrations (defaults: UTC).

  goto V       Migrate to version V
  up [N]       Apply all or N up migrations
  down [N] [-all]    Apply all or N down migrations
        Use -all to apply all down migrations
  drop [-f]    Drop everything inside database
        Use -f to bypass confirmation
  force V      Set version V but don't run migration (ignores dirty state)
  version      Print current migration version
```

So let's say you want to run the first two migrations

```bash
$ migrate -source file://path/to/migrations -database postgres://localhost:5432/database up 2
```

If your migrations are hosted on github

```bash
$ migrate -source github://mattes:personal-access-token@mattes/migrate_test \
    -database postgres://localhost:5432/database down 2
```

The CLI will gracefully stop at a safe point when SIGINT (ctrl+c) is received.
Send SIGKILL for immediate halt.

## Reading CLI arguments from somewhere else

### ENV variables

```bash
$ migrate -database "$MY_MIGRATE_DATABASE"
```

### JSON files

Check out https://stedolan.github.io/jq/

```bash
$ migrate -database "$(cat config.json | jq -r '.database')"
```

### YAML files

```bash
$ migrate -database "$(cat config/database.yml | ruby -ryaml -e "print YAML.load(STDIN.read)['database']")"
$ migrate -database "$(cat config/database.yml | python -c 'import yaml,sys;print yaml.safe_load(sys.stdin)["database"]')"
```
```

## File: `cmd/migrate/version.go`
```go
package main

// Version is set in Makefile with build flags
var Version = "dev"
```

## File: `cmd/migrate/examples/Dockerfile`
```
FROM ubuntu:bionic

RUN apt-get update && \
    apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent

RUN curl -sSL https://packagecloud.io/golang-migrate/migrate/gpgkey | apt-key add -
RUN echo "deb https://packagecloud.io/golang-migrate/migrate/ubuntu/ bionic main" > /etc/apt/sources.list.d/migrate.list
RUN apt-get update && \
    apt-get install -y migrate

RUN migrate -version
```

## File: `database/driver.go`
```go
// Package database provides the Driver interface.
// All database drivers must implement this interface, register themselves,
// optionally provide a `WithInstance` function and pass the tests
// in package database/testing.
package database

import (
	"fmt"
	"io"
	"sync"

	iurl "github.com/golang-migrate/migrate/v4/internal/url"
)

var (
	ErrLocked    = fmt.Errorf("can't acquire lock")
	ErrNotLocked = fmt.Errorf("can't unlock, as not currently locked")
)

const NilVersion int = -1

var driversMu sync.RWMutex
var drivers = make(map[string]Driver)

// Driver is the interface every database driver must implement.
//
// How to implement a database driver?
//  1. Implement this interface.
//  2. Optionally, add a function named `WithInstance`.
//     This function should accept an existing DB instance and a Config{} struct
//     and return a driver instance.
//  3. Add a test that calls database/testing.go:Test()
//  4. Add own tests for Open(), WithInstance() (when provided) and Close().
//     All other functions are tested by tests in database/testing.
//     Saves you some time and makes sure all database drivers behave the same way.
//  5. Call Register in init().
//  6. Create a internal/cli/build_<driver-name>.go file
//  7. Add driver name in 'DATABASE' variable in Makefile
//
// Guidelines:
//   - Don't try to correct user input. Don't assume things.
//     When in doubt, return an error and explain the situation to the user.
//   - All configuration input must come from the URL string in func Open()
//     or the Config{} struct in WithInstance. Don't os.Getenv().
type Driver interface {
	// Open returns a new driver instance configured with parameters
	// coming from the URL string. Migrate will call this function
	// only once per instance.
	Open(url string) (Driver, error)

	// Close closes the underlying database instance managed by the driver.
	// Migrate will call this function only once per instance.
	Close() error

	// Lock should acquire a database lock so that only one migration process
	// can run at a time. Migrate will call this function before Run is called.
	// If the implementation can't provide this functionality, return nil.
	// Return database.ErrLocked if database is already locked.
	Lock() error

	// Unlock should release the lock. Migrate will call this function after
	// all migrations have been run.
	Unlock() error

	// Run applies a migration to the database. migration is guaranteed to be not nil.
	Run(migration io.Reader) error

	// SetVersion saves version and dirty state.
	// Migrate will call this function before and after each call to Run.
	// version must be >= -1. -1 means NilVersion.
	SetVersion(version int, dirty bool) error

	// Version returns the currently active version and if the database is dirty.
	// When no migration has been applied, it must return version -1.
	// Dirty means, a previous migration failed and user interaction is required.
	Version() (version int, dirty bool, err error)

	// Drop deletes everything in the database.
	// Note that this is a breaking action, a new call to Open() is necessary to
	// ensure subsequent calls work as expected.
	Drop() error
}

// Open returns a new driver instance.
func Open(url string) (Driver, error) {
	scheme, err := iurl.SchemeFromURL(url)
	if err != nil {
		return nil, err
	}

	driversMu.RLock()
	d, ok := drivers[scheme]
	driversMu.RUnlock()
	if !ok {
		return nil, fmt.Errorf("database driver: unknown driver %v (forgotten import?)", scheme)
	}

	return d.Open(url)
}

// Register globally registers a driver.
func Register(name string, driver Driver) {
	driversMu.Lock()
	defer driversMu.Unlock()
	if driver == nil {
		panic("Register driver is nil")
	}
	if _, dup := drivers[name]; dup {
		panic("Register called twice for driver " + name)
	}
	drivers[name] = driver
}

// List lists the registered drivers
func List() []string {
	driversMu.RLock()
	defer driversMu.RUnlock()
	names := make([]string, 0, len(drivers))
	for n := range drivers {
		names = append(names, n)
	}
	return names
}
```

## File: `database/driver_test.go`
```go
package database

import (
	"io"
	"testing"
)

func ExampleDriver() {
	// see database/stub for an example

	// database/stub/stub.go has the driver implementation
	// database/stub/stub_test.go runs database/testing/test.go:Test
}

// Using database/stub here is not possible as it
// results in an import cycle.
type mockDriver struct {
	url string
}

func (m *mockDriver) Open(url string) (Driver, error) {
	return &mockDriver{
		url: url,
	}, nil
}

func (m *mockDriver) Close() error {
	return nil
}

func (m *mockDriver) Lock() error {
	return nil
}

func (m *mockDriver) Unlock() error {
	return nil
}

func (m *mockDriver) Run(migration io.Reader) error {
	return nil
}

func (m *mockDriver) SetVersion(version int, dirty bool) error {
	return nil
}

func (m *mockDriver) Version() (version int, dirty bool, err error) {
	return 0, false, nil
}

func (m *mockDriver) Drop() error {
	return nil
}

func TestRegisterTwice(t *testing.T) {
	Register("mock", &mockDriver{})

	var err interface{}
	func() {
		defer func() {
			err = recover()
		}()
		Register("mock", &mockDriver{})
	}()

	if err == nil {
		t.Fatal("expected a panic when calling Register twice")
	}
}

func TestOpen(t *testing.T) {
	// Make sure the driver is registered.
	// But if the previous test already registered it just ignore the panic.
	// If we don't do this it will be impossible to run this test standalone.
	func() {
		defer func() {
			_ = recover()
		}()
		Register("mock", &mockDriver{})
	}()

	cases := []struct {
		url string
		err bool
	}{
		{
			"mock://user:pass@tcp(host:1337)/db",
			false,
		},
		{
			"unknown://bla",
			true,
		},
	}

	for _, c := range cases {
		t.Run(c.url, func(t *testing.T) {
			d, err := Open(c.url)

			if err == nil {
				if c.err {
					t.Fatal("expected an error for an unknown driver")
				} else {
					if md, ok := d.(*mockDriver); !ok {
						t.Fatalf("expected *mockDriver got %T", d)
					} else if md.url != c.url {
						t.Fatalf("expected %q got %q", c.url, md.url)
					}
				}
			} else if !c.err {
				t.Fatalf("did not expect %q", err)
			}
		})
	}
}
```

## File: `database/error.go`
```go
package database

import (
	"fmt"
)

// Error should be used for errors involving queries ran against the database
type Error struct {
	// Optional: the line number
	Line uint

	// Query is a query excerpt
	Query []byte

	// Err is a useful/helping error message for humans
	Err string

	// OrigErr is the underlying error
	OrigErr error
}

func (e Error) Error() string {
	if len(e.Err) == 0 {
		return fmt.Sprintf("%v in line %v: %s", e.OrigErr, e.Line, e.Query)
	}
	return fmt.Sprintf("%v in line %v: %s (details: %v)", e.Err, e.Line, e.Query, e.OrigErr)
}
```

## File: `database/parse_test.go`
```go
package database_test

import (
	"encoding/hex"
	"net/url"
	"strings"
	"testing"
)

const reservedChars = "!#$%&'()*+,/:;=?@[]"
const reservedCharTestNamePrefix = "reserved char "

const baseUsername = "username"

const scheme = "database://"

// TestUserUnencodedReservedURLChars documents the behavior of using unencoded reserved characters in usernames with
// net/url Parse()
func TestUserUnencodedReservedURLChars(t *testing.T) {
	urlSuffix := "password@localhost:12345/myDB?someParam=true"
	urlSuffixAndSep := ":" + urlSuffix

	testcases := []struct {
		char             string
		parses           bool
		expectedUsername string // empty string means that the username failed to parse
		encodedURL       string
	}{
		{char: "!", parses: true, expectedUsername: baseUsername + "!",
			encodedURL: scheme + baseUsername + "%21" + urlSuffixAndSep},
		{char: "#", parses: true, expectedUsername: "",
			encodedURL: scheme + baseUsername + "#" + urlSuffixAndSep},
		{char: "$", parses: true, expectedUsername: baseUsername + "$",
			encodedURL: scheme + baseUsername + "$" + urlSuffixAndSep},
		{char: "%", parses: false},
		{char: "&", parses: true, expectedUsername: baseUsername + "&",
			encodedURL: scheme + baseUsername + "&" + urlSuffixAndSep},
		{char: "'", parses: true, expectedUsername: "username'",
			encodedURL: scheme + baseUsername + "%27" + urlSuffixAndSep},
		{char: "(", parses: true, expectedUsername: "username(",
			encodedURL: scheme + baseUsername + "%28" + urlSuffixAndSep},
		{char: ")", parses: true, expectedUsername: "username)",
			encodedURL: scheme + baseUsername + "%29" + urlSuffixAndSep},
		{char: "*", parses: true, expectedUsername: "username*",
			encodedURL: scheme + baseUsername + "%2A" + urlSuffixAndSep},
		{char: "+", parses: true, expectedUsername: "username+",
			encodedURL: scheme + baseUsername + "+" + urlSuffixAndSep},
		{char: ",", parses: true, expectedUsername: "username,",
			encodedURL: scheme + baseUsername + "," + urlSuffixAndSep},
		{char: "/", parses: true, expectedUsername: "",
			encodedURL: scheme + baseUsername + "/" + urlSuffixAndSep},
		{char: ":", parses: true, expectedUsername: baseUsername,
			encodedURL: scheme + baseUsername + ":%3A" + urlSuffix},
		{char: ";", parses: true, expectedUsername: "username;",
			encodedURL: scheme + baseUsername + ";" + urlSuffixAndSep},
		{char: "=", parses: true, expectedUsername: "username=",
			encodedURL: scheme + baseUsername + "=" + urlSuffixAndSep},
		{char: "?", parses: true, expectedUsername: "",
			encodedURL: scheme + baseUsername + "?" + urlSuffixAndSep},
		{char: "@", parses: true, expectedUsername: "username@",
			encodedURL: scheme + baseUsername + "%40" + urlSuffixAndSep},
		{char: "[", parses: false},
		{char: "]", parses: false},
	}

	testedChars := make([]string, 0, len(reservedChars))
	for _, tc := range testcases {
		testedChars = append(testedChars, tc.char)
		t.Run(reservedCharTestNamePrefix+tc.char, func(t *testing.T) {
			s := scheme + baseUsername + tc.char + urlSuffixAndSep
			u, err := url.Parse(s)
			if err == nil {
				if !tc.parses {
					t.Error("Unexpectedly parsed reserved character. url:", s)
					return
				}
				var username string
				if u.User != nil {
					username = u.User.Username()
				}
				if username != tc.expectedUsername {
					t.Error("Got unexpected username:", username, "!=", tc.expectedUsername)
				}
				if s := u.String(); s != tc.encodedURL {
					t.Error("Got unexpected encoded URL:", s, "!=", tc.encodedURL)
				}
			} else {
				if tc.parses {
					t.Error("Failed to parse reserved character. url:", s)
				}
			}
		})
	}

	t.Run("All reserved chars tested", func(t *testing.T) {
		if s := strings.Join(testedChars, ""); s != reservedChars {
			t.Error("Not all reserved URL characters were tested:", s, "!=", reservedChars)
		}
	})
}

func TestUserEncodedReservedURLChars(t *testing.T) {
	urlSuffix := "password@localhost:12345/myDB?someParam=true"
	urlSuffixAndSep := ":" + urlSuffix

	for _, c := range reservedChars {
		c := string(c)
		t.Run(reservedCharTestNamePrefix+c, func(t *testing.T) {
			encodedChar := "%" + hex.EncodeToString([]byte(c))
			s := scheme + baseUsername + encodedChar + urlSuffixAndSep
			expectedUsername := baseUsername + c
			u, err := url.Parse(s)
			if err != nil {
				t.Fatal("Failed to parse url with encoded reserved character. url:", s)
			}
			if u.User == nil {
				t.Fatal("Failed to parse userinfo with encoded reserve character. url:", s)
			}
			if username := u.User.Username(); username != expectedUsername {
				t.Fatal("Got unexpected username:", username, "!=", expectedUsername)
			}
		})
	}
}

// TestPasswordUnencodedReservedURLChars documents the behavior of using unencoded reserved characters in passwords
// with net/url Parse()
func TestPasswordUnencodedReservedURLChars(t *testing.T) {
	username := baseUsername
	schemeAndUsernameAndSep := scheme + username + ":"
	basePassword := "password"
	urlSuffixAndSep := "@localhost:12345/myDB?someParam=true"

	testcases := []struct {
		char             string
		parses           bool
		expectedUsername string // empty string means that the username failed to parse
		expectedPassword string // empty string means that the password failed to parse
		encodedURL       string
	}{
		{char: "!", parses: true, expectedUsername: username, expectedPassword: basePassword + "!",
			encodedURL: schemeAndUsernameAndSep + basePassword + "%21" + urlSuffixAndSep},
		{char: "#", parses: false},
		{char: "$", parses: true, expectedUsername: username, expectedPassword: basePassword + "$",
			encodedURL: schemeAndUsernameAndSep + basePassword + "$" + urlSuffixAndSep},
		{char: "%", parses: false},
		{char: "&", parses: true, expectedUsername: username, expectedPassword: basePassword + "&",
			encodedURL: schemeAndUsernameAndSep + basePassword + "&" + urlSuffixAndSep},
		{char: "'", parses: true, expectedUsername: username, expectedPassword: "password'",
			encodedURL: schemeAndUsernameAndSep + basePassword + "%27" + urlSuffixAndSep},
		{char: "(", parses: true, expectedUsername: username, expectedPassword: "password(",
			encodedURL: schemeAndUsernameAndSep + basePassword + "%28" + urlSuffixAndSep},
		{char: ")", parses: true, expectedUsername: username, expectedPassword: "password)",
			encodedURL: schemeAndUsernameAndSep + basePassword + "%29" + urlSuffixAndSep},
		{char: "*", parses: true, expectedUsername: username, expectedPassword: "password*",
			encodedURL: schemeAndUsernameAndSep + basePassword + "%2A" + urlSuffixAndSep},
		{char: "+", parses: true, expectedUsername: username, expectedPassword: "password+",
			encodedURL: schemeAndUsernameAndSep + basePassword + "+" + urlSuffixAndSep},
		{char: ",", parses: true, expectedUsername: username, expectedPassword: "password,",
			encodedURL: schemeAndUsernameAndSep + basePassword + "," + urlSuffixAndSep},
		{char: "/", parses: false},
		{char: ":", parses: true, expectedUsername: username, expectedPassword: "password:",
			encodedURL: schemeAndUsernameAndSep + basePassword + "%3A" + urlSuffixAndSep},
		{char: ";", parses: true, expectedUsername: username, expectedPassword: "password;",
			encodedURL: schemeAndUsernameAndSep + basePassword + ";" + urlSuffixAndSep},
		{char: "=", parses: true, expectedUsername: username, expectedPassword: "password=",
			encodedURL: schemeAndUsernameAndSep + basePassword + "=" + urlSuffixAndSep},
		{char: "?", parses: false},
		{char: "@", parses: true, expectedUsername: username, expectedPassword: "password@",
			encodedURL: schemeAndUsernameAndSep + basePassword + "%40" + urlSuffixAndSep},
		{char: "[", parses: false},
		{char: "]", parses: false},
	}

	testedChars := make([]string, 0, len(reservedChars))
	for _, tc := range testcases {
		testedChars = append(testedChars, tc.char)
		t.Run(reservedCharTestNamePrefix+tc.char, func(t *testing.T) {
			s := schemeAndUsernameAndSep + basePassword + tc.char + urlSuffixAndSep
			u, err := url.Parse(s)
			if err == nil {
				if !tc.parses {
					t.Error("Unexpectedly parsed reserved character. url:", s)
					return
				}
				var username, password string
				if u.User != nil {
					username = u.User.Username()
					password, _ = u.User.Password()
				}
				if username != tc.expectedUsername {
					t.Error("Got unexpected username:", username, "!=", tc.expectedUsername)
				}
				if password != tc.expectedPassword {
					t.Error("Got unexpected password:", password, "!=", tc.expectedPassword)
				}
				if s := u.String(); s != tc.encodedURL {
					t.Error("Got unexpected encoded URL:", s, "!=", tc.encodedURL)
				}
			} else {
				if tc.parses {
					t.Error("Failed to parse reserved character. url:", s)
				}
			}
		})
	}

	t.Run("All reserved chars tested", func(t *testing.T) {
		if s := strings.Join(testedChars, ""); s != reservedChars {
			t.Error("Not all reserved URL characters were tested:", s, "!=", reservedChars)
		}
	})
}

func TestPasswordEncodedReservedURLChars(t *testing.T) {
	username := baseUsername
	schemeAndUsernameAndSep := scheme + username + ":"
	basePassword := "password"
	urlSuffixAndSep := "@localhost:12345/myDB?someParam=true"

	for _, c := range reservedChars {
		c := string(c)
		t.Run(reservedCharTestNamePrefix+c, func(t *testing.T) {
			encodedChar := "%" + hex.EncodeToString([]byte(c))
			s := schemeAndUsernameAndSep + basePassword + encodedChar + urlSuffixAndSep
			expectedPassword := basePassword + c
			u, err := url.Parse(s)
			if err != nil {
				t.Fatal("Failed to parse url with encoded reserved character. url:", s)
			}
			if u.User == nil {
				t.Fatal("Failed to parse userinfo with encoded reserve character. url:", s)
			}
			if n := u.User.Username(); n != username {
				t.Fatal("Got unexpected username:", n, "!=", username)
			}
			if p, _ := u.User.Password(); p != expectedPassword {
				t.Fatal("Got unexpected password:", p, "!=", expectedPassword)
			}
		})
	}
}
```

## File: `database/util.go`
```go
package database

import (
	"fmt"
	"hash/crc32"
	"strings"
	"sync/atomic"
)

const advisoryLockIDSalt uint = 1486364155

// GenerateAdvisoryLockId inspired by rails migrations, see https://goo.gl/8o9bCT
func GenerateAdvisoryLockId(databaseName string, additionalNames ...string) (string, error) { // nolint: golint
	if len(additionalNames) > 0 {
		databaseName = strings.Join(append(additionalNames, databaseName), "\x00")
	}
	sum := crc32.ChecksumIEEE([]byte(databaseName))
	sum = sum * uint32(advisoryLockIDSalt)
	return fmt.Sprint(sum), nil
}

// CasRestoreOnErr CAS wrapper to automatically restore the lock state on error
func CasRestoreOnErr(lock *atomic.Bool, o, n bool, casErr error, f func() error) error {
	if !lock.CompareAndSwap(o, n) {
		return casErr
	}
	if err := f(); err != nil {
		// Automatically unlock/lock on error
		lock.Store(o)
		return err
	}
	return nil
}
```

## File: `database/util_test.go`
```go
package database

import (
	"errors"
	"sync/atomic"
	"testing"
)

func TestGenerateAdvisoryLockId(t *testing.T) {
	testcases := []struct {
		dbname     string
		additional []string
		expectedID string // empty string signifies that an error is expected
	}{
		{
			dbname:     "database_name",
			expectedID: "1764327054",
		},
		{
			dbname:     "database_name",
			additional: []string{"schema_name_1"},
			expectedID: "2453313553",
		},
		{
			dbname:     "database_name",
			additional: []string{"schema_name_2"},
			expectedID: "235207038",
		},
		{
			dbname:     "database_name",
			additional: []string{"schema_name_1", "schema_name_2"},
			expectedID: "3743845847",
		},
	}

	for _, tc := range testcases {
		t.Run(tc.dbname, func(t *testing.T) {
			if id, err := GenerateAdvisoryLockId(tc.dbname, tc.additional...); err == nil {
				if id != tc.expectedID {
					t.Error("Generated incorrect ID:", id, "!=", tc.expectedID)
				}
			} else {
				if tc.expectedID != "" {
					t.Error("Got unexpected error:", err)
				}
			}
		})
	}
}

func TestCasRestoreOnErr(t *testing.T) {
	casErr := errors.New("test lock CAS failure")
	fErr := errors.New("test callback error")

	testcases := []struct {
		name        string
		lock        bool
		from        bool
		to          bool
		expectLock  bool
		fErr        error
		expectError error
	}{
		{
			name:        "Test positive CAS lock",
			lock:        false,
			from:        false,
			to:          true,
			expectLock:  true,
			fErr:        nil,
			expectError: nil,
		},
		{
			name:        "Test negative CAS lock",
			lock:        true,
			from:        false,
			to:          true,
			expectLock:  true,
			fErr:        nil,
			expectError: casErr,
		},
		{
			name:        "Test negative with callback lock",
			lock:        false,
			from:        false,
			to:          true,
			expectLock:  false,
			fErr:        fErr,
			expectError: fErr,
		},
	}

	for _, tc := range testcases {
		t.Run(tc.name, func(t *testing.T) {
			var lock atomic.Bool
			lock.Store(tc.lock)
			if err := CasRestoreOnErr(&lock, tc.from, tc.to, casErr, func() error {
				return tc.fErr
			}); err != tc.expectError {
				t.Error("Incorrect error value returned")
			}

			if lock.Load() != tc.expectLock {
				t.Error("Incorrect state of lock")
			}
		})
	}
}
```

## File: `database/cassandra/cassandra.go`
```go
package cassandra

import (
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"strconv"
	"strings"
	"sync/atomic"
	"time"

	"github.com/gocql/gocql"
	"github.com/golang-migrate/migrate/v4/database"
	"github.com/golang-migrate/migrate/v4/database/multistmt"
)

func init() {
	db := new(Cassandra)
	database.Register("cassandra", db)
}

var (
	multiStmtDelimiter = []byte(";")

	DefaultMultiStatementMaxSize = 10 * 1 << 20 // 10 MB
)

var DefaultMigrationsTable = "schema_migrations"

var (
	ErrNilConfig     = errors.New("no config")
	ErrNoKeyspace    = errors.New("no keyspace provided")
	ErrDatabaseDirty = errors.New("database is dirty")
	ErrClosedSession = errors.New("session is closed")
)

type Config struct {
	MigrationsTable       string
	KeyspaceName          string
	MultiStatementEnabled bool
	MultiStatementMaxSize int
}

type Cassandra struct {
	session  *gocql.Session
	isLocked atomic.Bool

	// Open and WithInstance need to guarantee that config is never nil
	config *Config
}

func WithInstance(session *gocql.Session, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	} else if len(config.KeyspaceName) == 0 {
		return nil, ErrNoKeyspace
	}

	if session.Closed() {
		return nil, ErrClosedSession
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	if config.MultiStatementMaxSize <= 0 {
		config.MultiStatementMaxSize = DefaultMultiStatementMaxSize
	}

	c := &Cassandra{
		session: session,
		config:  config,
	}

	if err := c.ensureVersionTable(); err != nil {
		return nil, err
	}

	return c, nil
}

func (c *Cassandra) Open(url string) (database.Driver, error) {
	u, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}

	// Check for missing mandatory attributes
	if len(u.Path) == 0 {
		return nil, ErrNoKeyspace
	}

	cluster := gocql.NewCluster(u.Host)
	cluster.Keyspace = strings.TrimPrefix(u.Path, "/")
	cluster.Consistency = gocql.All
	cluster.Timeout = 1 * time.Minute

	if len(u.Query().Get("username")) > 0 && len(u.Query().Get("password")) > 0 {
		authenticator := gocql.PasswordAuthenticator{
			Username: u.Query().Get("username"),
			Password: u.Query().Get("password"),
		}
		cluster.Authenticator = authenticator
	}

	// Retrieve query string configuration
	if len(u.Query().Get("consistency")) > 0 {
		var consistency gocql.Consistency
		consistency, err = parseConsistency(u.Query().Get("consistency"))
		if err != nil {
			return nil, err
		}

		cluster.Consistency = consistency
	}
	if len(u.Query().Get("protocol")) > 0 {
		var protoversion int
		protoversion, err = strconv.Atoi(u.Query().Get("protocol"))
		if err != nil {
			return nil, err
		}
		cluster.ProtoVersion = protoversion
	}
	if len(u.Query().Get("timeout")) > 0 {
		var timeout time.Duration
		timeout, err = time.ParseDuration(u.Query().Get("timeout"))
		if err != nil {
			return nil, err
		}
		cluster.Timeout = timeout
	}
	if len(u.Query().Get("connect-timeout")) > 0 {
		var connectTimeout time.Duration
		connectTimeout, err = time.ParseDuration(u.Query().Get("connect-timeout"))
		if err != nil {
			return nil, err
		}
		cluster.ConnectTimeout = connectTimeout
	}

	if len(u.Query().Get("sslmode")) > 0 {
		if u.Query().Get("sslmode") != "disable" {
			sslOpts := &gocql.SslOptions{}

			if len(u.Query().Get("sslrootcert")) > 0 {
				sslOpts.CaPath = u.Query().Get("sslrootcert")
			}
			if len(u.Query().Get("sslcert")) > 0 {
				sslOpts.CertPath = u.Query().Get("sslcert")
			}
			if len(u.Query().Get("sslkey")) > 0 {
				sslOpts.KeyPath = u.Query().Get("sslkey")
			}

			if u.Query().Get("sslmode") == "verify-full" {
				sslOpts.EnableHostVerification = true
			}

			cluster.SslOpts = sslOpts
		}
	}

	if len(u.Query().Get("disable-host-lookup")) > 0 {
		if flag, err := strconv.ParseBool(u.Query().Get("disable-host-lookup")); err != nil && flag {
			cluster.DisableInitialHostLookup = true
		} else if err != nil {
			return nil, err
		}
	}

	session, err := cluster.CreateSession()
	if err != nil {
		return nil, err
	}

	multiStatementMaxSize := DefaultMultiStatementMaxSize
	if s := u.Query().Get("x-multi-statement-max-size"); len(s) > 0 {
		multiStatementMaxSize, err = strconv.Atoi(s)
		if err != nil {
			return nil, err
		}
	}

	return WithInstance(session, &Config{
		KeyspaceName:          strings.TrimPrefix(u.Path, "/"),
		MigrationsTable:       u.Query().Get("x-migrations-table"),
		MultiStatementEnabled: u.Query().Get("x-multi-statement") == "true",
		MultiStatementMaxSize: multiStatementMaxSize,
	})
}

func (c *Cassandra) Close() error {
	c.session.Close()
	return nil
}

func (c *Cassandra) Lock() error {
	if !c.isLocked.CompareAndSwap(false, true) {
		return database.ErrLocked
	}
	return nil
}

func (c *Cassandra) Unlock() error {
	if !c.isLocked.CompareAndSwap(true, false) {
		return database.ErrNotLocked
	}
	return nil
}

func (c *Cassandra) Run(migration io.Reader) error {
	if c.config.MultiStatementEnabled {
		var err error
		if e := multistmt.Parse(migration, multiStmtDelimiter, c.config.MultiStatementMaxSize, func(m []byte) bool {
			tq := strings.TrimSpace(string(m))
			if tq == "" {
				return true
			}
			if e := c.session.Query(tq).Exec(); e != nil {
				err = database.Error{OrigErr: e, Err: "migration failed", Query: m}
				return false
			}
			return true
		}); e != nil {
			return e
		}
		return err
	}

	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}
	// run migration
	if err := c.session.Query(string(migr)).Exec(); err != nil {
		// TODO: cast to Cassandra error and get line number
		return database.Error{OrigErr: err, Err: "migration failed", Query: migr}
	}
	return nil
}

func (c *Cassandra) SetVersion(version int, dirty bool) error {
	// DELETE instead of TRUNCATE because AWS Keyspaces does not support it
	// see: https://docs.aws.amazon.com/keyspaces/latest/devguide/cassandra-apis.html
	squery := `SELECT version FROM "` + c.config.MigrationsTable + `"`
	dquery := `DELETE FROM "` + c.config.MigrationsTable + `" WHERE version = ?`
	iter := c.session.Query(squery).Iter()
	var previous int
	for iter.Scan(&previous) {
		if err := c.session.Query(dquery, previous).Exec(); err != nil {
			return &database.Error{OrigErr: err, Query: []byte(dquery)}
		}
	}
	if err := iter.Close(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(squery)}
	}

	// Also re-write the schema version for nil dirty versions to prevent
	// empty schema version for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330
	if version >= 0 || (version == database.NilVersion && dirty) {
		query := `INSERT INTO "` + c.config.MigrationsTable + `" (version, dirty) VALUES (?, ?)`
		if err := c.session.Query(query, version, dirty).Exec(); err != nil {
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	return nil
}

// Return current keyspace version
func (c *Cassandra) Version() (version int, dirty bool, err error) {
	query := `SELECT version, dirty FROM "` + c.config.MigrationsTable + `" LIMIT 1`
	err = c.session.Query(query).Scan(&version, &dirty)
	switch {
	case err == gocql.ErrNotFound:
		return database.NilVersion, false, nil

	case err != nil:
		if _, ok := err.(*gocql.Error); ok {
			return database.NilVersion, false, nil
		}
		return 0, false, &database.Error{OrigErr: err, Query: []byte(query)}

	default:
		return version, dirty, nil
	}
}

func (c *Cassandra) Drop() error {
	// select all tables in current schema
	query := fmt.Sprintf(`SELECT table_name from system_schema.tables WHERE keyspace_name='%s'`, c.config.KeyspaceName)
	iter := c.session.Query(query).Iter()
	var tableName string
	for iter.Scan(&tableName) {
		err := c.session.Query(fmt.Sprintf(`DROP TABLE %s`, tableName)).Exec()
		if err != nil {
			return err
		}
	}

	return nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the Cassandra type.
func (c *Cassandra) ensureVersionTable() (err error) {
	if err = c.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := c.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	err = c.session.Query(fmt.Sprintf("CREATE TABLE IF NOT EXISTS %s (version bigint, dirty boolean, PRIMARY KEY(version))", c.config.MigrationsTable)).Exec()
	if err != nil {
		return err
	}
	if _, _, err = c.Version(); err != nil {
		return err
	}
	return nil
}

// ParseConsistency wraps gocql.ParseConsistency
// to return an error instead of a panicking.
func parseConsistency(consistencyStr string) (consistency gocql.Consistency, err error) {
	defer func() {
		if r := recover(); r != nil {
			var ok bool
			err, ok = r.(error)
			if !ok {
				err = fmt.Errorf("failed to parse consistency \"%s\": %v", consistencyStr, r)
			}
		}
	}()
	consistency = gocql.ParseConsistency(consistencyStr)

	return consistency, nil
}
```

## File: `database/cassandra/cassandra_test.go`
```go
package cassandra

import (
	"context"
	"fmt"
	"github.com/golang-migrate/migrate/v4"
	"strconv"
	"testing"
)

import (
	"github.com/dhui/dktest"
	"github.com/gocql/gocql"
)

import (
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

var (
	opts = dktest.Options{PortRequired: true, ReadyFunc: isReady}
	// Supported versions: http://cassandra.apache.org/download/
	// Although Cassandra 2.x is supported by the Apache Foundation,
	// the migrate db driver only supports Cassandra 3.x since it uses
	// the system_schema keyspace.
	// last ScyllaDB version tested is 5.1.11
	specs = []dktesting.ContainerSpec{
		{ImageName: "cassandra:3.0", Options: opts},
		{ImageName: "cassandra:3.11", Options: opts},
		{ImageName: "scylladb/scylla:5.1.11", Options: opts},
	}
)

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	// Cassandra exposes 5 ports (7000, 7001, 7199, 9042 & 9160)
	// We only need the port bound to 9042
	ip, portStr, err := c.Port(9042)
	if err != nil {
		return false
	}
	port, err := strconv.Atoi(portStr)
	if err != nil {
		return false
	}

	cluster := gocql.NewCluster(ip)
	cluster.Port = port
	cluster.Consistency = gocql.All
	p, err := cluster.CreateSession()
	if err != nil {
		return false
	}
	defer p.Close()
	// Create keyspace for tests
	if err = p.Query("CREATE KEYSPACE testks WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor':1}").Exec(); err != nil {
		return false
	}
	return true
}

func Test(t *testing.T) {
	t.Run("test", test)
	t.Run("testMigrate", testMigrate)

	t.Cleanup(func() {
		for _, spec := range specs {
			t.Log("Cleaning up ", spec.ImageName)
			if err := spec.Cleanup(); err != nil {
				t.Error("Error removing ", spec.ImageName, "error:", err)
			}
		}
	})
}

func test(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(9042)
		if err != nil {
			t.Fatal("Unable to get mapped port:", err)
		}
		addr := fmt.Sprintf("cassandra://%v:%v/testks", ip, port)
		p := &Cassandra{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		dt.Test(t, d, []byte("SELECT table_name from system_schema.tables"))
	})
}

func testMigrate(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(9042)
		if err != nil {
			t.Fatal("Unable to get mapped port:", err)
		}
		addr := fmt.Sprintf("cassandra://%v:%v/testks", ip, port)
		p := &Cassandra{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "testks", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}
```

## File: `database/cassandra/README.md`
```markdown
# Cassandra / ScyllaDB

* `Drop()` method will not work on Cassandra 2.X because it rely on
system_schema table which comes with 3.X
* Other methods should work properly but are **not tested**
* The Cassandra driver (gocql) does not natively support executing multiple statements in a single query. To allow for multiple statements in a single migration, you can use the `x-multi-statement` param. There are two important caveats:
  * This mode splits the migration text into separately-executed statements by a semi-colon `;`. Thus `x-multi-statement` cannot be used when a statement in the migration contains a string with a semi-colon.
  * The queries are not executed in any sort of transaction/batch, meaning you are responsible for fixing partial migrations.

**ScyllaDB**

* No additional configuration is required since it is a drop-in replacement for Cassandra.
* The `Drop()` method` works for ScyllaDB 5.1


## Usage
`cassandra://host:port/keyspace?param1=value&param2=value2`


| URL Query  | Default value | Description |
|------------|-------------|-----------|
| `x-migrations-table` | schema_migrations | Name of the migrations table |
| `x-multi-statement` | false | Enable multiple statements to be ran in a single migration (See note above) |
| `port` | 9042 | The port to bind to  |
| `consistency` | ALL | Migration consistency
| `protocol` |  | Cassandra protocol version (3 or 4)
| `timeout` | 1 minute | Migration timeout
| `connect-timeout` | 600ms | Initial connection timeout to the cluster |
| `username` | nil | Username to use when authenticating. |
| `password` | nil | Password to use when authenticating. |
| `sslcert` | | Cert file location. The file must contain PEM encoded data. |
| `sslkey` | | Key file location. The file must contain PEM encoded data. |
| `sslrootcert` | | The location of the root certificate file. The file must contain PEM encoded data. |
| `sslmode` | | Whether or not to use SSL (disable\|require\|verify-ca\|verify-full) |
| `disable-host-lookup`| false | Disable initial host lookup. |

`timeout` is parsed using [time.ParseDuration(s string)](https://golang.org/pkg/time/#ParseDuration)


## Upgrading from v1

1. Write down the current migration version from schema_migrations
2. `DROP TABLE schema_migrations`
4. Download and install the latest migrate version.
5. Force the current migration version with `migrate force <current_version>`.
```

## File: `database/cassandra/examples/migrations/1_simple_select.down.sql`
```sql
SELECT table_name from system_schema.tables
```

## File: `database/cassandra/examples/migrations/1_simple_select.up.sql`
```sql
SELECT table_name from system_schema.tables
```

## File: `database/clickhouse/clickhouse.go`
```go
package clickhouse

import (
	"database/sql"
	"errors"
	"fmt"
	"io"
	"net/url"
	"strconv"
	"strings"
	"sync/atomic"
	"time"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	"github.com/golang-migrate/migrate/v4/database/multistmt"
)

var (
	multiStmtDelimiter = []byte(";")

	DefaultMigrationsTable       = "schema_migrations"
	DefaultMigrationsTableEngine = "TinyLog"
	DefaultMultiStatementMaxSize = 10 * 1 << 20 // 10 MB

	ErrNilConfig = fmt.Errorf("no config")
)

type Config struct {
	DatabaseName          string
	ClusterName           string
	MigrationsTable       string
	MigrationsTableEngine string
	MultiStatementEnabled bool
	MultiStatementMaxSize int
}

func init() {
	database.Register("clickhouse", &ClickHouse{})
}

func WithInstance(conn *sql.DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := conn.Ping(); err != nil {
		return nil, err
	}

	ch := &ClickHouse{
		conn:   conn,
		config: config,
	}

	if err := ch.init(); err != nil {
		return nil, err
	}

	return ch, nil
}

type ClickHouse struct {
	conn     *sql.DB
	config   *Config
	isLocked atomic.Bool
}

func (ch *ClickHouse) Open(dsn string) (database.Driver, error) {
	purl, err := url.Parse(dsn)
	if err != nil {
		return nil, err
	}
	q := migrate.FilterCustomQuery(purl)
	q.Scheme = "tcp"
	conn, err := sql.Open("clickhouse", q.String())
	if err != nil {
		return nil, err
	}

	multiStatementMaxSize := DefaultMultiStatementMaxSize
	if s := purl.Query().Get("x-multi-statement-max-size"); len(s) > 0 {
		multiStatementMaxSize, err = strconv.Atoi(s)
		if err != nil {
			return nil, err
		}
	}

	migrationsTableEngine := DefaultMigrationsTableEngine
	if s := purl.Query().Get("x-migrations-table-engine"); len(s) > 0 {
		migrationsTableEngine = s
	}

	ch = &ClickHouse{
		conn: conn,
		config: &Config{
			MigrationsTable:       purl.Query().Get("x-migrations-table"),
			MigrationsTableEngine: migrationsTableEngine,
			DatabaseName:          purl.Query().Get("database"),
			ClusterName:           purl.Query().Get("x-cluster-name"),
			MultiStatementEnabled: purl.Query().Get("x-multi-statement") == "true",
			MultiStatementMaxSize: multiStatementMaxSize,
		},
	}

	if err := ch.init(); err != nil {
		return nil, err
	}

	return ch, nil
}

func (ch *ClickHouse) init() error {
	if len(ch.config.DatabaseName) == 0 {
		if err := ch.conn.QueryRow("SELECT currentDatabase()").Scan(&ch.config.DatabaseName); err != nil {
			return err
		}
	}

	if len(ch.config.MigrationsTable) == 0 {
		ch.config.MigrationsTable = DefaultMigrationsTable
	}

	if ch.config.MultiStatementMaxSize <= 0 {
		ch.config.MultiStatementMaxSize = DefaultMultiStatementMaxSize
	}

	if len(ch.config.MigrationsTableEngine) == 0 {
		ch.config.MigrationsTableEngine = DefaultMigrationsTableEngine
	}

	return ch.ensureVersionTable()
}

func (ch *ClickHouse) Run(r io.Reader) error {
	if ch.config.MultiStatementEnabled {
		var err error
		if e := multistmt.Parse(r, multiStmtDelimiter, ch.config.MultiStatementMaxSize, func(m []byte) bool {
			tq := strings.TrimSpace(string(m))
			if tq == "" {
				return true
			}
			if _, e := ch.conn.Exec(string(m)); e != nil {
				err = database.Error{OrigErr: e, Err: "migration failed", Query: m}
				return false
			}
			return true
		}); e != nil {
			return e
		}
		return err
	}

	migration, err := io.ReadAll(r)
	if err != nil {
		return err
	}

	if _, err := ch.conn.Exec(string(migration)); err != nil {
		return database.Error{OrigErr: err, Err: "migration failed", Query: migration}
	}

	return nil
}
func (ch *ClickHouse) Version() (int, bool, error) {
	var (
		version int
		dirty   uint8
		query   = "SELECT version, dirty FROM `" + ch.config.MigrationsTable + "` ORDER BY sequence DESC LIMIT 1"
	)
	if err := ch.conn.QueryRow(query).Scan(&version, &dirty); err != nil {
		if err == sql.ErrNoRows {
			return database.NilVersion, false, nil
		}
		return 0, false, &database.Error{OrigErr: err, Query: []byte(query)}
	}
	return version, dirty == 1, nil
}

func (ch *ClickHouse) SetVersion(version int, dirty bool) error {
	var (
		bool = func(v bool) uint8 {
			if v {
				return 1
			}
			return 0
		}
		tx, err = ch.conn.Begin()
	)
	if err != nil {
		return err
	}

	query := "INSERT INTO " + ch.config.MigrationsTable + " (version, dirty, sequence) VALUES (?, ?, ?)"
	if _, err := tx.Exec(query, version, bool(dirty), time.Now().UnixNano()); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return tx.Commit()
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the ClickHouse type.
func (ch *ClickHouse) ensureVersionTable() (err error) {
	if err = ch.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := ch.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	var (
		table string
		query = "SHOW TABLES FROM " + quoteIdentifier(ch.config.DatabaseName) + " LIKE '" + ch.config.MigrationsTable + "'"
	)
	// check if migration table exists
	if err := ch.conn.QueryRow(query).Scan(&table); err != nil {
		if err != sql.ErrNoRows {
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	} else {
		return nil
	}

	// if not, create the empty migration table
	if len(ch.config.ClusterName) > 0 {
		query = fmt.Sprintf(`
			CREATE TABLE %s ON CLUSTER %s (
				version    Int64,
				dirty      UInt8,
				sequence   UInt64
			) Engine=%s`, ch.config.MigrationsTable, ch.config.ClusterName, ch.config.MigrationsTableEngine)
	} else {
		query = fmt.Sprintf(`
			CREATE TABLE %s (
				version    Int64,
				dirty      UInt8,
				sequence   UInt64
			) Engine=%s`, ch.config.MigrationsTable, ch.config.MigrationsTableEngine)
	}

	if strings.HasSuffix(ch.config.MigrationsTableEngine, "Tree") {
		query = fmt.Sprintf(`%s ORDER BY sequence`, query)
	}

	if _, err := ch.conn.Exec(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	return nil
}

func (ch *ClickHouse) Drop() (err error) {
	query := "SHOW TABLES FROM " + quoteIdentifier(ch.config.DatabaseName)
	tables, err := ch.conn.Query(query)

	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	for tables.Next() {
		var table string
		if err := tables.Scan(&table); err != nil {
			return err
		}

		query = "DROP TABLE IF EXISTS " + quoteIdentifier(ch.config.DatabaseName) + "." + quoteIdentifier(table)

		if _, err := ch.conn.Exec(query); err != nil {
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}

func (ch *ClickHouse) Lock() error {
	if !ch.isLocked.CompareAndSwap(false, true) {
		return database.ErrLocked
	}

	return nil
}
func (ch *ClickHouse) Unlock() error {
	if !ch.isLocked.CompareAndSwap(true, false) {
		return database.ErrNotLocked
	}

	return nil
}
func (ch *ClickHouse) Close() error { return ch.conn.Close() }

// Copied from lib/pq implementation: https://github.com/lib/pq/blob/v1.9.0/conn.go#L1611
func quoteIdentifier(name string) string {
	end := strings.IndexRune(name, 0)
	if end > -1 {
		name = name[:end]
	}
	return `"` + strings.ReplaceAll(name, `"`, `""`) + `"`
}
```

## File: `database/clickhouse/clickhouse_test.go`
```go
package clickhouse_test

import (
	"context"
	"database/sql"
	sqldriver "database/sql/driver"
	"fmt"
	"log"
	"testing"

	_ "github.com/ClickHouse/clickhouse-go"
	"github.com/dhui/dktest"
	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database/clickhouse"
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

const defaultPort = 9000

var (
	tableEngines = []string{"TinyLog", "MergeTree"}
	opts         = dktest.Options{
		Env:          map[string]string{"CLICKHOUSE_USER": "user", "CLICKHOUSE_PASSWORD": "password", "CLICKHOUSE_DB": "db"},
		PortRequired: true, ReadyFunc: isReady,
	}
	specs = []dktesting.ContainerSpec{
		{ImageName: "clickhouse:24.8", Options: opts},
	}
)

func clickhouseConnectionString(host, port, engine string) string {
	if engine != "" {
		return fmt.Sprintf(
			"clickhouse://%v:%v?username=user&password=password&database=db&x-multi-statement=true&x-migrations-table-engine=%v&debug=false",
			host, port, engine)
	}

	return fmt.Sprintf(
		"clickhouse://%v:%v?username=user&password=password&database=db&x-multi-statement=true&debug=false",
		host, port)
}

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	ip, port, err := c.Port(defaultPort)
	if err != nil {
		return false
	}

	db, err := sql.Open("clickhouse", clickhouseConnectionString(ip, port, ""))

	if err != nil {
		log.Println("open error", err)
		return false
	}
	defer func() {
		if err := db.Close(); err != nil {
			log.Println("close error:", err)
		}
	}()

	if err = db.PingContext(ctx); err != nil {
		switch err {
		case sqldriver.ErrBadConn:
			return false
		default:
			fmt.Println(err)
		}
		return false
	}

	return true
}

func TestCases(t *testing.T) {
	for _, engine := range tableEngines {
		t.Run("Test_"+engine, func(t *testing.T) { testSimple(t, engine) })
		t.Run("Migrate_"+engine, func(t *testing.T) { testMigrate(t, engine) })
		t.Run("Version_"+engine, func(t *testing.T) { testVersion(t, engine) })
		t.Run("Drop_"+engine, func(t *testing.T) { testDrop(t, engine) })
	}
	t.Run("WithInstanceDefaultConfigValues", func(t *testing.T) { testSimpleWithInstanceDefaultConfigValues(t) })
}

func testSimple(t *testing.T, engine string) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := clickhouseConnectionString(ip, port, engine)
		p := &clickhouse.ClickHouse{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		dt.Test(t, d, []byte("SELECT 1"))
	})
}

func testSimpleWithInstanceDefaultConfigValues(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := clickhouseConnectionString(ip, port, "")
		conn, err := sql.Open("clickhouse", addr)
		if err != nil {
			t.Fatal(err)
		}
		d, err := clickhouse.WithInstance(conn, &clickhouse.Config{})
		if err != nil {
			_ = conn.Close()
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		dt.Test(t, d, []byte("SELECT 1"))
	})
}

func testMigrate(t *testing.T, engine string) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := clickhouseConnectionString(ip, port, engine)
		p := &clickhouse.ClickHouse{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "db", d)

		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}

func testVersion(t *testing.T, engine string) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		expectedVersion := 1

		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := clickhouseConnectionString(ip, port, engine)
		p := &clickhouse.ClickHouse{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		err = d.SetVersion(expectedVersion, false)
		if err != nil {
			t.Fatal(err)
		}

		version, _, err := d.Version()
		if err != nil {
			t.Fatal(err)
		}

		if version != expectedVersion {
			t.Fatal("Version mismatch")
		}
	})
}

func testDrop(t *testing.T, engine string) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := clickhouseConnectionString(ip, port, engine)
		p := &clickhouse.ClickHouse{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		err = d.Drop()
		if err != nil {
			t.Fatal(err)
		}
	})
}
```

## File: `database/clickhouse/README.md`
```markdown
# ClickHouse

`clickhouse://host:port?username=user&password=password&database=clicks&x-multi-statement=true`

| URL Query  | Description |
|------------|-------------|
| `x-migrations-table`| Name of the migrations table |
| `x-migrations-table-engine`| Engine to use for the migrations table, defaults to TinyLog |
| `x-cluster-name` | Name of cluster for creating `schema_migrations` table cluster wide |
| `database` | The name of the database to connect to |
| `username` | The user to sign in as |
| `password` | The user's password |
| `host` | The host to connect to. |
| `port` | The port to bind to. |
| `x-multi-statement` | false | Enable multiple statements to be ran in a single migration (See note below) |

## Notes

* The Clickhouse driver does not natively support executing multiple statements in a single query. To allow for multiple statements in a single migration, you can use the `x-multi-statement` param. There are two important caveats:
  * This mode splits the migration text into separately-executed statements by a semi-colon `;`. Thus `x-multi-statement` cannot be used when a statement in the migration contains a string with a semi-colon.
  * The queries are not executed in any sort of transaction/batch, meaning you are responsible for fixing partial migrations.
* Using the default TinyLog table engine for the schema_versions table prevents backing up the table if using the [clickhouse-backup](https://github.com/AlexAkulov/clickhouse-backup) tool. If backing up the database with make sure the migrations are run with `x-migrations-table-engine=MergeTree`.
* Clickhouse cluster mode is not officially supported, since it's not tested right now, but you can try enabling `schema_migrations` table replication by specifying a `x-cluster-name`:
  * When `x-cluster-name` is specified, `x-migrations-table-engine` also should be specified. See the docs regarding [replicated table engines](https://clickhouse.tech/docs/en/engines/table-engines/mergetree-family/replication/#table_engines-replication).
  * When `x-cluster-name` is specified, only the `schema_migrations` table is replicated across the cluster. You still need to write your migrations so that the application tables are replicated within the cluster.
* If you want to create database inside the migration, you should know, that table which will manage migrations `schema-migrations table` will be in `default` table, so you can't use `USE <database_name>` inside migration. In this case you may not specify the database in the connection string (example you can find [here](examples/migrations/003_create_database.up.sql))
```

## File: `database/clickhouse/examples/migrations/001_init.down.sql`
```sql
DROP TABLE IF EXISTS test_1;
```

## File: `database/clickhouse/examples/migrations/001_init.up.sql`
```sql
CREATE TABLE test_1 (
    Date Date 
) Engine=Memory;
```

## File: `database/clickhouse/examples/migrations/002_create_table.down.sql`
```sql
DROP TABLE IF EXISTS test_2;
```

## File: `database/clickhouse/examples/migrations/002_create_table.up.sql`
```sql
CREATE TABLE test_2 (
    Date Date 
) Engine=Memory;
```

## File: `database/clickhouse/examples/migrations/003_create_database.down.sql`
```sql
DROP TABLE IF EXISTS driver_ratings;
DROP TABLE IF EXISTS user_ratings;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS driver_ratings_queue;
DROP TABLE IF EXISTS user_ratings_queue;
DROP TABLE IF EXISTS orders_queue;
DROP VIEW IF EXISTS user_ratings_queue_mv;
DROP VIEW IF EXISTS driver_ratings_queue_mv;
DROP VIEW IF EXISTS orders_queue_mv;
DROP DATABASE IF EXISTS analytics;
```

## File: `database/clickhouse/examples/migrations/003_create_database.up.sql`
```sql
CREATE DATABASE IF NOT EXISTS analytics;

CREATE TABLE IF NOT EXISTS analytics.driver_ratings(
    rate UInt8,
    userID Int64,
    driverID String,
    orderID String,
    inserted_time DateTime DEFAULT now()
) ENGINE = MergeTree
PARTITION BY driverID
ORDER BY (inserted_time);

CREATE TABLE analytics.driver_ratings_queue(
    rate UInt8,
    userID Int64,
    driverID String,
    orderID String
) ENGINE = Kafka
SETTINGS kafka_broker_list = 'broker:9092',
    kafka_topic_list = 'driver-ratings',
    kafka_group_name = 'rating_readers',
    kafka_format = 'Avro',
    kafka_max_block_size = 1048576;

CREATE MATERIALIZED VIEW analytics.driver_ratings_queue_mv TO analytics.driver_ratings AS
SELECT rate, userID, driverID, orderID
FROM analytics.driver_ratings_queue;

CREATE TABLE IF NOT EXISTS analytics.user_ratings(
    rate UInt8,
    userID Int64,
    driverID String,
    orderID String,
    inserted_time DateTime DEFAULT now()
) ENGINE = MergeTree
    PARTITION BY userID
    ORDER BY (inserted_time);

CREATE TABLE analytics.user_ratings_queue(
    rate UInt8,
    userID Int64,
    driverID String,
    orderID String
) ENGINE = Kafka
SETTINGS kafka_broker_list = 'broker:9092',
    kafka_topic_list = 'user-ratings',
    kafka_group_name = 'rating_readers',
    kafka_format = 'JSON',
    kafka_max_block_size = 1048576;

CREATE MATERIALIZED VIEW analytics.user_ratings_queue_mv TO analytics.user_ratings AS
SELECT rate, userID, driverID, orderID
FROM analytics.user_ratings_queue;

CREATE TABLE IF NOT EXISTS analytics.orders(
    from_place String,
    to_place String,
    userID Int64,
    driverID String,
    orderID String,
    inserted_time DateTime DEFAULT now()
) ENGINE = MergeTree
    PARTITION BY driverID
    ORDER BY (inserted_time);

CREATE TABLE analytics.orders_queue(
    from_place String,
    to_place String,
    userID Int64,
    driverID String,
    orderID String
) ENGINE = Kafka
SETTINGS kafka_broker_list = 'broker:9092',
    kafka_topic_list = 'orders',
    kafka_group_name = 'order_readers',
    kafka_format = 'Avro',
    kafka_max_block_size = 1048576;

CREATE MATERIALIZED VIEW analytics.orders_queue_mv TO orders AS
SELECT from_place, to_place, userID, driverID, orderID
FROM analytics.orders_queue;
```

## File: `database/cockroachdb/cockroachdb.go`
```go
package cockroachdb

import (
	"context"
	"database/sql"
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"regexp"
	"strconv"
	"sync/atomic"

	"github.com/cockroachdb/cockroach-go/v2/crdb"
	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	"github.com/lib/pq"
)

func init() {
	db := CockroachDb{}
	database.Register("cockroach", &db)
	database.Register("cockroachdb", &db)
	database.Register("crdb-postgres", &db)
}

var DefaultMigrationsTable = "schema_migrations"
var DefaultLockTable = "schema_lock"

var (
	ErrNilConfig      = fmt.Errorf("no config")
	ErrNoDatabaseName = fmt.Errorf("no database name")
)

type Config struct {
	MigrationsTable string
	LockTable       string
	ForceLock       bool
	DatabaseName    string
}

type CockroachDb struct {
	db       *sql.DB
	isLocked atomic.Bool

	// Open and WithInstance need to guarantee that config is never nil
	config *Config
}

func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	if config.DatabaseName == "" {
		query := `SELECT current_database()`
		var databaseName string
		if err := instance.QueryRow(query).Scan(&databaseName); err != nil {
			return nil, &database.Error{OrigErr: err, Query: []byte(query)}
		}

		if len(databaseName) == 0 {
			return nil, ErrNoDatabaseName
		}

		config.DatabaseName = databaseName
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	if len(config.LockTable) == 0 {
		config.LockTable = DefaultLockTable
	}

	px := &CockroachDb{
		db:     instance,
		config: config,
	}

	// ensureVersionTable is a locking operation, so we need to ensureLockTable before we ensureVersionTable.
	if err := px.ensureLockTable(); err != nil {
		return nil, err
	}

	if err := px.ensureVersionTable(); err != nil {
		return nil, err
	}

	return px, nil
}

func (c *CockroachDb) Open(url string) (database.Driver, error) {
	purl, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}

	// As Cockroach uses the postgres protocol, and 'postgres' is already a registered database, we need to replace the
	// connect prefix, with the actual protocol, so that the library can differentiate between the implementations
	re := regexp.MustCompile("^(cockroach(db)?|crdb-postgres)")
	connectString := re.ReplaceAllString(migrate.FilterCustomQuery(purl).String(), "postgres")

	db, err := sql.Open("postgres", connectString)
	if err != nil {
		return nil, err
	}

	migrationsTable := purl.Query().Get("x-migrations-table")
	if len(migrationsTable) == 0 {
		migrationsTable = DefaultMigrationsTable
	}

	lockTable := purl.Query().Get("x-lock-table")
	if len(lockTable) == 0 {
		lockTable = DefaultLockTable
	}

	forceLockQuery := purl.Query().Get("x-force-lock")
	forceLock, err := strconv.ParseBool(forceLockQuery)
	if err != nil {
		forceLock = false
	}

	px, err := WithInstance(db, &Config{
		DatabaseName:    purl.Path,
		MigrationsTable: migrationsTable,
		LockTable:       lockTable,
		ForceLock:       forceLock,
	})
	if err != nil {
		return nil, err
	}

	return px, nil
}

func (c *CockroachDb) Close() error {
	return c.db.Close()
}

// Locking is done manually with a separate lock table.  Implementing advisory locks in CRDB is being discussed
// See: https://github.com/cockroachdb/cockroach/issues/13546
func (c *CockroachDb) Lock() error {
	return database.CasRestoreOnErr(&c.isLocked, false, true, database.ErrLocked, func() (err error) {
		return crdb.ExecuteTx(context.Background(), c.db, nil, func(tx *sql.Tx) (err error) {
			aid, err := database.GenerateAdvisoryLockId(c.config.DatabaseName)
			if err != nil {
				return err
			}

			query := "SELECT * FROM " + c.config.LockTable + " WHERE lock_id = $1"
			rows, err := tx.Query(query, aid)
			if err != nil {
				return database.Error{OrigErr: err, Err: "failed to fetch migration lock", Query: []byte(query)}
			}
			defer func() {
				if errClose := rows.Close(); errClose != nil {
					err = errors.Join(err, errClose)
				}
			}()

			// If row exists at all, lock is present
			locked := rows.Next()
			if locked && !c.config.ForceLock {
				return database.ErrLocked
			}

			query = "INSERT INTO " + c.config.LockTable + " (lock_id) VALUES ($1)"
			if _, err := tx.Exec(query, aid); err != nil {
				return database.Error{OrigErr: err, Err: "failed to set migration lock", Query: []byte(query)}
			}

			return nil
		})
	})
}

// Locking is done manually with a separate lock table.  Implementing advisory locks in CRDB is being discussed
// See: https://github.com/cockroachdb/cockroach/issues/13546
func (c *CockroachDb) Unlock() error {
	return database.CasRestoreOnErr(&c.isLocked, true, false, database.ErrNotLocked, func() (err error) {
		aid, err := database.GenerateAdvisoryLockId(c.config.DatabaseName)
		if err != nil {
			return err
		}

		// In the event of an implementation (non-migration) error, it is possible for the lock to not be released.  Until
		// a better locking mechanism is added, a manual purging of the lock table may be required in such circumstances
		query := "DELETE FROM " + c.config.LockTable + " WHERE lock_id = $1"
		if _, err := c.db.Exec(query, aid); err != nil {
			if e, ok := err.(*pq.Error); ok {
				// 42P01 is "UndefinedTableError" in CockroachDB
				// https://github.com/cockroachdb/cockroach/blob/master/pkg/sql/pgwire/pgerror/codes.go
				if e.Code == "42P01" {
					// On drops, the lock table is fully removed;  This is fine, and is a valid "unlocked" state for the schema
					return nil
				}
			}

			return database.Error{OrigErr: err, Err: "failed to release migration lock", Query: []byte(query)}
		}

		return nil
	})
}

func (c *CockroachDb) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}

	// run migration
	query := string(migr[:])
	if _, err := c.db.Exec(query); err != nil {
		return database.Error{OrigErr: err, Err: "migration failed", Query: migr}
	}

	return nil
}

func (c *CockroachDb) SetVersion(version int, dirty bool) error {
	return crdb.ExecuteTx(context.Background(), c.db, nil, func(tx *sql.Tx) error {
		if _, err := tx.Exec(`DELETE FROM "` + c.config.MigrationsTable + `"`); err != nil {
			return err
		}

		// Also re-write the schema version for nil dirty versions to prevent
		// empty schema version for failed down migration on the first migration
		// See: https://github.com/golang-migrate/migrate/issues/330
		if version >= 0 || (version == database.NilVersion && dirty) {
			if _, err := tx.Exec(`INSERT INTO "`+c.config.MigrationsTable+`" (version, dirty) VALUES ($1, $2)`, version, dirty); err != nil {
				return err
			}
		}

		return nil
	})
}

func (c *CockroachDb) Version() (version int, dirty bool, err error) {
	query := `SELECT version, dirty FROM "` + c.config.MigrationsTable + `" LIMIT 1`
	err = c.db.QueryRow(query).Scan(&version, &dirty)

	switch {
	case err == sql.ErrNoRows:
		return database.NilVersion, false, nil

	case err != nil:
		if e, ok := err.(*pq.Error); ok {
			// 42P01 is "UndefinedTableError" in CockroachDB
			// https://github.com/cockroachdb/cockroach/blob/master/pkg/sql/pgwire/pgerror/codes.go
			if e.Code == "42P01" {
				return database.NilVersion, false, nil
			}
		}
		return 0, false, &database.Error{OrigErr: err, Query: []byte(query)}

	default:
		return version, dirty, nil
	}
}

func (c *CockroachDb) Drop() (err error) {
	// select all tables in current schema
	query := `SELECT table_name FROM information_schema.tables WHERE table_schema=(SELECT current_schema())`
	tables, err := c.db.Query(query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	// delete one table after another
	tableNames := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}
		if len(tableName) > 0 {
			tableNames = append(tableNames, tableName)
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if len(tableNames) > 0 {
		// delete one by one ...
		for _, t := range tableNames {
			query = `DROP TABLE IF EXISTS ` + t + ` CASCADE`
			if _, err := c.db.Exec(query); err != nil {
				return &database.Error{OrigErr: err, Query: []byte(query)}
			}
		}
	}

	return nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the CockroachDb type.
func (c *CockroachDb) ensureVersionTable() (err error) {
	if err = c.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := c.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	// check if migration table exists
	var count int
	query := `SELECT COUNT(1) FROM information_schema.tables WHERE table_name = $1 AND table_schema = (SELECT current_schema()) LIMIT 1`
	if err := c.db.QueryRow(query, c.config.MigrationsTable).Scan(&count); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	if count == 1 {
		return nil
	}

	// if not, create the empty migration table
	query = `CREATE TABLE "` + c.config.MigrationsTable + `" (version INT NOT NULL PRIMARY KEY, dirty BOOL NOT NULL)`
	if _, err := c.db.Exec(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	return nil
}

func (c *CockroachDb) ensureLockTable() error {
	// check if lock table exists
	var count int
	query := `SELECT COUNT(1) FROM information_schema.tables WHERE table_name = $1 AND table_schema = (SELECT current_schema()) LIMIT 1`
	if err := c.db.QueryRow(query, c.config.LockTable).Scan(&count); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	if count == 1 {
		return nil
	}

	// if not, create the empty lock table
	query = `CREATE TABLE "` + c.config.LockTable + `" (lock_id INT NOT NULL PRIMARY KEY)`
	if _, err := c.db.Exec(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}
```

## File: `database/cockroachdb/cockroachdb_test.go`
```go
package cockroachdb

// error codes https://github.com/lib/pq/blob/master/error.go

import (
	"context"
	"database/sql"
	"fmt"
	"github.com/golang-migrate/migrate/v4"
	"log"
	"strings"
	"testing"
)

import (
	"github.com/dhui/dktest"
	_ "github.com/lib/pq"
)

import (
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

const defaultPort = 26257

var (
	opts = dktest.Options{Cmd: []string{"start-single-node", "--insecure"}, PortRequired: true, ReadyFunc: isReady}
	// Supported versions: https://www.cockroachlabs.com/docs/releases/release-support-policy#supported-versions
	specs = []dktesting.ContainerSpec{
		{ImageName: "cockroachdb/cockroach:latest-v24.3", Options: opts},
		{ImageName: "cockroachdb/cockroach:latest-v24.1", Options: opts},
		{ImageName: "cockroachdb/cockroach:latest-v23.2", Options: opts},
		{ImageName: "cockroachdb/cockroach:latest-v23.1", Options: opts},
	}
)

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	ip, port, err := c.Port(defaultPort)
	if err != nil {
		log.Println("port error:", err)
		return false
	}

	db, err := sql.Open("postgres", fmt.Sprintf("postgres://root@%v:%v?sslmode=disable", ip, port))
	if err != nil {
		log.Println("open error:", err)
		return false
	}
	if err := db.PingContext(ctx); err != nil {
		log.Println("ping error:", err)
		return false
	}
	if err := db.Close(); err != nil {
		log.Println("close error:", err)
	}
	return true
}

func createDB(t *testing.T, c dktest.ContainerInfo) {
	ip, port, err := c.Port(defaultPort)
	if err != nil {
		t.Fatal(err)
	}

	db, err := sql.Open("postgres", fmt.Sprintf("postgres://root@%v:%v?sslmode=disable", ip, port))
	if err != nil {
		t.Fatal(err)
	}
	if err = db.Ping(); err != nil {
		t.Fatal(err)
	}
	defer func() {
		if err := db.Close(); err != nil {
			t.Error(err)
		}
	}()

	if _, err = db.Exec("CREATE DATABASE migrate"); err != nil {
		t.Fatal(err)
	}
}

func Test(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, ci dktest.ContainerInfo) {
		createDB(t, ci)

		ip, port, err := ci.Port(26257)
		if err != nil {
			t.Fatal(err)
		}

		addr := fmt.Sprintf("cockroach://root@%v:%v/migrate?sslmode=disable", ip, port)
		c := &CockroachDb{}
		d, err := c.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		dt.Test(t, d, []byte("SELECT 1"))
	})
}

func TestMigrate(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, ci dktest.ContainerInfo) {
		createDB(t, ci)

		ip, port, err := ci.Port(26257)
		if err != nil {
			t.Fatal(err)
		}

		addr := fmt.Sprintf("cockroach://root@%v:%v/migrate?sslmode=disable", ip, port)
		c := &CockroachDb{}
		d, err := c.Open(addr)
		if err != nil {
			t.Fatal(err)
		}

		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "migrate", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}

func TestMultiStatement(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, ci dktest.ContainerInfo) {
		createDB(t, ci)

		ip, port, err := ci.Port(26257)
		if err != nil {
			t.Fatal(err)
		}

		addr := fmt.Sprintf("cockroach://root@%v:%v/migrate?sslmode=disable", ip, port)
		c := &CockroachDb{}
		d, err := c.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		if err := d.Run(strings.NewReader("CREATE TABLE foo (foo text); CREATE TABLE bar (bar text);")); err != nil {
			t.Fatalf("expected err to be nil, got %v", err)
		}

		// make sure second table exists
		var exists bool
		if err := d.(*CockroachDb).db.QueryRow("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'bar' AND table_schema = (SELECT current_schema()))").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table bar to exist")
		}
	})
}

func TestFilterCustomQuery(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, ci dktest.ContainerInfo) {
		createDB(t, ci)

		ip, port, err := ci.Port(26257)
		if err != nil {
			t.Fatal(err)
		}

		addr := fmt.Sprintf("cockroach://root@%v:%v/migrate?sslmode=disable&x-custom=foobar", ip, port)
		c := &CockroachDb{}
		_, err = c.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
	})
}
```

## File: `database/cockroachdb/README.md`
```markdown
# cockroachdb

`cockroachdb://user:password@host:port/dbname?query` (`cockroach://`, and `crdb-postgres://` work, too)

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table |
| `x-lock-table` | `LockTable` | Name of the table which maintains the migration lock |
| `x-force-lock` | `ForceLock` | Force lock acquisition to fix faulty migrations which may not have released the schema lock (Boolean, default is `false`) |
| `dbname` | `DatabaseName` | The name of the database to connect to |
| `user` | | The user to sign in as |
| `password` | | The user's password |
| `host` | | The host to connect to. Values that start with / are for unix domain sockets. (default is localhost) |
| `port` | | The port to bind to. (default is 5432) |
| `connect_timeout` | | Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely. |
| `sslcert` | | Cert file location. The file must contain PEM encoded data. |
| `sslkey` | | Key file location. The file must contain PEM encoded data. |
| `sslrootcert` | | The location of the root certificate file. The file must contain PEM encoded data. |
| `sslmode` | | Whether or not to use SSL (disable\|require\|verify-ca\|verify-full) |
```

## File: `database/cockroachdb/TUTORIAL.md`
```markdown
# CockroachDB tutorial for beginners (insecure cluster)

## Create/configure database

First, let's start a local cluster - follow step 1. and 2. from [the docs](https://www.cockroachlabs.com/docs/stable/start-a-local-cluster.html#step-1-start-the-first-node).

Once you have it, create a database. Here I am going to create a database called `example`.
Our user here is `cockroach`. We are not going to use a password, since it's not supported for insecure cluster.
```
cockroach sql --insecure --host=localhost:26257
```
```
CREATE DATABASE example;
CREATE USER IF NOT EXISTS cockroach;
GRANT ALL ON DATABASE example TO cockroach;
```

When using Migrate CLI we need to pass to database URL. Let's export it to a variable for convenience:
```
export COCKROACHDB_URL='cockroachdb://cockroach:@localhost:26257/example?sslmode=disable'
```
`sslmode=disable` means that the connection with our database will not be encrypted. This is needed to connect to an insecure node.

**NOTE:** Do not use COCKROACH_URL as a variable name here, it's already in use for discrete parameters and you may run into connection problems. For more info check out [docs](https://www.cockroachlabs.com/docs/stable/connection-parameters.html#connect-using-discrete-parameters).

You can find further description of database URLs [here](README.md#database-urls).

## Create migrations
Let's create a table called `users`:
```
migrate create -ext sql -dir db/migrations -seq create_users_table
```
If there were no errors, we should have two files available under `db/migrations` folder:
- 000001_create_users_table.down.sql
- 000001_create_users_table.up.sql

Note the `sql` extension that we provided.

In the `.up.sql` file let's create the table:
```
CREATE TABLE IF NOT EXISTS example.users
(
   user_id INT PRIMARY KEY,
   username VARCHAR (50) UNIQUE NOT NULL,
   password VARCHAR (50) NOT NULL,
   email VARCHAR (300) UNIQUE NOT NULL
);
```
And in the `.down.sql` let's delete it:
```
DROP TABLE IF EXISTS example.users;
```
By adding `IF EXISTS/IF NOT EXISTS` we are making migrations idempotent - you can read more about idempotency in [getting started](../corp/docs/usage_guides/getting_started.md#create-migrations)

## Run migrations
```
migrate -database ${COCKROACHDB_URL} -path db/migrations up
```
Let's check if the table was created properly by running `cockroach sql --insecure --host=localhost:26257 -e "show columns from example.users;"`.
The output you are supposed to see:
```
  column_name |  data_type   | is_nullable | column_default | generation_expression |                   indices                    | is_hidden
+-------------+--------------+-------------+----------------+-----------------------+----------------------------------------------+-----------+
  user_id     | INT8         |    false    | NULL           |                       | {primary,users_username_key,users_email_key} |   false
  username    | VARCHAR(50)  |    false    | NULL           |                       | {users_username_key}                         |   false
  password    | VARCHAR(50)  |    false    | NULL           |                       | {}                                           |   false
  email       | VARCHAR(300) |    false    | NULL           |                       | {users_email_key}                            |   false
(4 rows)
```
Now let's check if running reverse migration also works:
```
migrate -database ${COCKROACHDB_URL} -path db/migrations down
```
Make sure to check if your database changed as expected in this case as well.

## Database transactions

To show database transactions usage, let's create another set of migrations by running:
```
migrate create -ext sql -dir db/migrations -seq add_mood_to_users
```
Again, it should create for us two migrations files:
- 000002_add_mood_to_users.down.sql
- 000002_add_mood_to_users.up.sql

In Cockroach, when we want our queries to be done in a transaction, we need to wrap it with `BEGIN` and `COMMIT` commands, similar to PostgreSQL.
In our example, we are going to add a column to our database that can only accept enumerable values or NULL.
Migration up:
```
BEGIN;

ALTER TABLE example.users ADD COLUMN mood STRING;
ALTER TABLE example.users ADD CONSTRAINT check_mood CHECK (mood IN ('happy', 'sad', 'neutral'));

COMMIT;
```
Migration down:
```
ALTER TABLE example.users DROP COLUMN mood;
```

Now we can run our new migration and check the database:
```
migrate -database ${COCKROACHDB_URL} -path db/migrations up
cockroach sql --insecure --host=localhost:26257 -e "show columns from example.users;"
```
Expected output:
```
  column_name |  data_type   | is_nullable | column_default | generation_expression |                   indices                    | is_hidden  
+-------------+--------------+-------------+----------------+-----------------------+----------------------------------------------+-----------+
  user_id     | INT8         |    false    | NULL           |                       | {primary,users_username_key,users_email_key} |   false    
  username    | VARCHAR(50)  |    false    | NULL           |                       | {users_username_key}                         |   false    
  password    | VARCHAR(50)  |    false    | NULL           |                       | {}                                           |   false    
  email       | VARCHAR(300) |    false    | NULL           |                       | {users_email_key}                            |   false    
  mood        | STRING       |    true     | NULL           |                       | {}                                           |   false    
(5 rows)
```

## Optional: Run migrations within your Go app
Here is a very simple app running migrations for the above configuration:
```
import (
	"log"

	"github.com/golang-migrate/migrate/v4"
	_ "github.com/golang-migrate/migrate/v4/database/cockroachdb"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

func main() {
	m, err := migrate.New(
		"file://db/migrations",
		"cockroachdb://cockroach:@localhost:26257/example?sslmode=disable")
	if err != nil {
		log.Fatal(err)
	}
	if err := m.Up(); err != nil {
		log.Fatal(err)
	}
}
```
You can find details [here](README.md#use-in-your-go-project)
```

## File: `database/cockroachdb/examples/migrations/1085649617_create_users_table.down.sql`
```sql
DROP TABLE IF EXISTS users;
```

## File: `database/cockroachdb/examples/migrations/1085649617_create_users_table.up.sql`
```sql
CREATE TABLE users (
  user_id INT UNIQUE,
  name    STRING(40),
  email   STRING(40)
);
```

## File: `database/cockroachdb/examples/migrations/1185749658_add_city_to_users.down.sql`
```sql
ALTER TABLE users DROP COLUMN IF EXISTS city;
```

## File: `database/cockroachdb/examples/migrations/1185749658_add_city_to_users.up.sql`
```sql
ALTER TABLE users ADD COLUMN city TEXT;
```

## File: `database/cockroachdb/examples/migrations/1285849751_add_index_on_user_emails.down.sql`
```sql
DROP INDEX IF EXISTS users_email_index;
```

## File: `database/cockroachdb/examples/migrations/1285849751_add_index_on_user_emails.up.sql`
```sql
CREATE UNIQUE INDEX IF NOT EXISTS users_email_index ON users (email);

-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/cockroachdb/examples/migrations/1385949617_create_books_table.down.sql`
```sql
DROP TABLE IF EXISTS books;
```

## File: `database/cockroachdb/examples/migrations/1385949617_create_books_table.up.sql`
```sql
CREATE TABLE books (
  user_id INT,
  name    STRING(40),
  author  STRING(40)
);
```

## File: `database/cockroachdb/examples/migrations/1485949617_create_movies_table.down.sql`
```sql
DROP TABLE IF EXISTS movies;
```

## File: `database/cockroachdb/examples/migrations/1485949617_create_movies_table.up.sql`
```sql
CREATE TABLE movies (
  user_id   INT,
  name      STRING(40),
  director  STRING(40)
);
```

## File: `database/cockroachdb/examples/migrations/1585849751_just_a_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/cockroachdb/examples/migrations/1685849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/cockroachdb/examples/migrations/1785849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/cockroachdb/examples/migrations/1885849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/firebird/firebird.go`
```go
//go:build go1.9

package firebird

import (
	"context"
	"database/sql"
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"sync/atomic"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	_ "github.com/nakagami/firebirdsql"
)

func init() {
	db := Firebird{}
	database.Register("firebird", &db)
	database.Register("firebirdsql", &db)
}

var DefaultMigrationsTable = "schema_migrations"

var (
	ErrNilConfig = fmt.Errorf("no config")
)

type Config struct {
	DatabaseName    string
	MigrationsTable string
}

type Firebird struct {
	// Locking and unlocking need to use the same connection
	conn     *sql.Conn
	db       *sql.DB
	isLocked atomic.Bool

	// Open and WithInstance need to guarantee that config is never nil
	config *Config
}

func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	conn, err := instance.Conn(context.Background())
	if err != nil {
		return nil, err
	}

	fb := &Firebird{
		conn:   conn,
		db:     instance,
		config: config,
	}

	if err := fb.ensureVersionTable(); err != nil {
		return nil, err
	}

	return fb, nil
}

func (f *Firebird) Open(dsn string) (database.Driver, error) {
	purl, err := nurl.Parse(dsn)
	if err != nil {
		return nil, err
	}

	db, err := sql.Open("firebirdsql", migrate.FilterCustomQuery(purl).String())
	if err != nil {
		return nil, err
	}

	px, err := WithInstance(db, &Config{
		MigrationsTable: purl.Query().Get("x-migrations-table"),
		DatabaseName:    purl.Path,
	})

	if err != nil {
		return nil, err
	}

	return px, nil
}

func (f *Firebird) Close() error {
	connErr := f.conn.Close()
	dbErr := f.db.Close()
	if connErr != nil || dbErr != nil {
		return fmt.Errorf("conn: %v, db: %v", connErr, dbErr)
	}
	return nil
}

func (f *Firebird) Lock() error {
	if !f.isLocked.CompareAndSwap(false, true) {
		return database.ErrLocked
	}
	return nil
}

func (f *Firebird) Unlock() error {
	if !f.isLocked.CompareAndSwap(true, false) {
		return database.ErrNotLocked
	}
	return nil
}

func (f *Firebird) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}

	// run migration
	query := string(migr[:])
	if _, err := f.conn.ExecContext(context.Background(), query); err != nil {
		return database.Error{OrigErr: err, Err: "migration failed", Query: migr}
	}

	return nil
}

func (f *Firebird) SetVersion(version int, dirty bool) error {
	// Always re-write the schema version to prevent empty schema version
	// for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330

	// TODO: parameterize this SQL statement
	//       https://firebirdsql.org/refdocs/langrefupd20-execblock.html
	//       VALUES (?, ?) doesn't work
	query := fmt.Sprintf(`EXECUTE BLOCK AS BEGIN
					DELETE FROM "%v";
					INSERT INTO "%v" (version, dirty) VALUES (%v, %v);
				END;`,
		f.config.MigrationsTable, f.config.MigrationsTable, version, btoi(dirty))

	if _, err := f.conn.ExecContext(context.Background(), query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}

func (f *Firebird) Version() (version int, dirty bool, err error) {
	var d int
	query := fmt.Sprintf(`SELECT FIRST 1 version, dirty FROM "%v"`, f.config.MigrationsTable)
	err = f.conn.QueryRowContext(context.Background(), query).Scan(&version, &d)
	switch {
	case err == sql.ErrNoRows:
		return database.NilVersion, false, nil
	case err != nil:
		return 0, false, &database.Error{OrigErr: err, Query: []byte(query)}

	default:
		return version, itob(d), nil
	}
}

func (f *Firebird) Drop() (err error) {
	// select all tables
	query := `SELECT rdb$relation_name FROM rdb$relations WHERE rdb$view_blr IS NULL AND (rdb$system_flag IS NULL OR rdb$system_flag = 0);`
	tables, err := f.conn.QueryContext(context.Background(), query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	// delete one table after another
	tableNames := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}
		if len(tableName) > 0 {
			tableNames = append(tableNames, tableName)
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	// delete one by one ...
	for _, t := range tableNames {
		query := fmt.Sprintf(`EXECUTE BLOCK AS BEGIN
						if (not exists(select 1 from rdb$relations where rdb$relation_name = '%v')) then
						execute statement 'drop table "%v"';
					END;`,
			t, t)

		if _, err := f.conn.ExecContext(context.Background(), query); err != nil {
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	return nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
func (f *Firebird) ensureVersionTable() (err error) {
	if err = f.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := f.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	query := fmt.Sprintf(`EXECUTE BLOCK AS BEGIN
			if (not exists(select 1 from rdb$relations where rdb$relation_name = '%v')) then
			execute statement 'create table "%v" (version bigint not null primary key, dirty smallint not null)';
		END;`,
		f.config.MigrationsTable, f.config.MigrationsTable)

	if _, err = f.conn.ExecContext(context.Background(), query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}

// btoi converts bool to int
func btoi(v bool) int {
	if v {
		return 1
	}
	return 0
}

// itob converts int to bool
func itob(v int) bool {
	return v != 0
}
```

## File: `database/firebird/firebird_test.go`
```go
package firebird

import (
	"context"
	"database/sql"
	sqldriver "database/sql/driver"
	"fmt"
	"log"

	"github.com/golang-migrate/migrate/v4"
	"io"
	"strings"
	"testing"

	"github.com/dhui/dktest"

	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"
	_ "github.com/golang-migrate/migrate/v4/source/file"

	_ "github.com/nakagami/firebirdsql"
)

const (
	user     = "test_user"
	password = "123456"
	dbName   = "test.fdb"
)

var (
	opts = dktest.Options{
		PortRequired: true,
		ReadyFunc:    isReady,
		Env: map[string]string{
			"FIREBIRD_DATABASE": dbName,
			"FIREBIRD_USER":     user,
			"FIREBIRD_PASSWORD": password,
		},
	}
	specs = []dktesting.ContainerSpec{
		{ImageName: "jacobalberty/firebird:v3.0", Options: opts},
		{ImageName: "jacobalberty/firebird:v4.0", Options: opts},
		{ImageName: "jacobalberty/firebird:v5.0", Options: opts},
	}
)

func fbConnectionString(host, port string) string {
	//firebird://user:password@servername[:port_number]/database_name_or_file[?params1=value1[&param2=value2]...]
	return fmt.Sprintf("firebird://%s:%s@%s:%s//firebird/data/%s", user, password, host, port, dbName)
}

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	ip, port, err := c.FirstPort()
	if err != nil {
		return false
	}

	db, err := sql.Open("firebirdsql", fbConnectionString(ip, port))
	if err != nil {
		log.Println("open error:", err)
		return false
	}
	defer func() {
		if err := db.Close(); err != nil {
			log.Println("close error:", err)
		}
	}()
	if err = db.PingContext(ctx); err != nil {
		switch err {
		case sqldriver.ErrBadConn, io.EOF:
			return false
		default:
			log.Println(err)
		}
		return false
	}

	return true
}

func Test(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := fbConnectionString(ip, port)
		p := &Firebird{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		dt.Test(t, d, []byte("SELECT Count(*) FROM rdb$relations"))
	})
}

func TestMigrate(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := fbConnectionString(ip, port)
		p := &Firebird{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "firebirdsql", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}

func TestErrorParsing(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := fbConnectionString(ip, port)
		p := &Firebird{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		wantErr := `migration failed in line 0: CREATE TABLEE foo (foo varchar(40)); (details: Dynamic SQL Error
SQL error code = -104
Token unknown - line 1, column 8
TABLEE
)`

		if err := d.Run(strings.NewReader("CREATE TABLEE foo (foo varchar(40));")); err == nil {
			t.Fatal("expected err but got nil")
		} else if err.Error() != wantErr {
			msg := err.Error()
			t.Fatalf("expected '%s' but got '%s'", wantErr, msg)
		}
	})
}

func TestFilterCustomQuery(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := fbConnectionString(ip, port) + "?sslmode=disable&x-custom=foobar"
		p := &Firebird{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
	})
}

func Test_Lock(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := fbConnectionString(ip, port)
		p := &Firebird{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		dt.Test(t, d, []byte("SELECT Count(*) FROM rdb$relations"))

		ps := d.(*Firebird)

		err = ps.Lock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Unlock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Lock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Unlock()
		if err != nil {
			t.Fatal(err)
		}
	})
}
```

## File: `database/firebird/README.md`
```markdown
# firebird

`firebirdsql://user:password@servername[:port_number]/database_name_or_file[?params1=value1[&param2=value2]...]`

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table |
| `auth_plugin_name` | | Authentication plugin name. Srp256/Srp/Legacy_Auth are available. (default is Srp) |
| `column_name_to_lower` | | Force column name to lower. (default is false) |
| `role` | | Role name |
| `tzname` | | Time Zone name. (For Firebird 4.0+) |
| `wire_crypt` | | Enable wire data encryption or not. For Firebird 3.0+ (default is true) |
```

## File: `database/firebird/examples/migrations/1085649617_create_users_table.down.sql`
```sql
DROP TABLE users;
```

## File: `database/firebird/examples/migrations/1085649617_create_users_table.up.sql`
```sql
CREATE TABLE users (
  user_id integer unique,
  name    varchar(40),
  email   varchar(40)
);
```

## File: `database/firebird/examples/migrations/1185749658_add_city_to_users.down.sql`
```sql
ALTER TABLE users DROP city;
```

## File: `database/firebird/examples/migrations/1185749658_add_city_to_users.up.sql`
```sql
ALTER TABLE users ADD city varchar(100);


```

## File: `database/firebird/examples/migrations/1285849751_add_index_on_user_emails.down.sql`
```sql
DROP INDEX users_email_index;
```

## File: `database/firebird/examples/migrations/1285849751_add_index_on_user_emails.up.sql`
```sql
CREATE UNIQUE INDEX users_email_index ON users (email);

-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/firebird/examples/migrations/1385949617_create_books_table.down.sql`
```sql
DROP TABLE books;
```

## File: `database/firebird/examples/migrations/1385949617_create_books_table.up.sql`
```sql
CREATE TABLE books (
  user_id integer,
  name    varchar(40),
  author  varchar(40)
);
```

## File: `database/firebird/examples/migrations/1485949617_create_movies_table.down.sql`
```sql
DROP TABLE movies;
```

## File: `database/firebird/examples/migrations/1485949617_create_movies_table.up.sql`
```sql
CREATE TABLE movies (
  user_id   integer,
  name      varchar(40),
  director  varchar(40)
);
```

## File: `database/mongodb/mongodb.go`
```go
package mongodb

import (
	"context"
	"errors"
	"fmt"
	"io"
	"net/url"
	"os"
	"strconv"
	"sync/atomic"
	"time"

	"github.com/cenkalti/backoff/v4"
	"github.com/golang-migrate/migrate/v4/database"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"go.mongodb.org/mongo-driver/x/mongo/driver/connstring"
)

func init() {
	db := Mongo{}
	database.Register("mongodb", &db)
	database.Register("mongodb+srv", &db)
}

var DefaultMigrationsCollection = "schema_migrations"

const DefaultLockingCollection = "migrate_advisory_lock" // the collection to use for advisory locking by default.
const lockKeyUniqueValue = 0                             // the unique value to lock on. If multiple clients try to insert the same key, it will fail (locked).
const DefaultLockTimeout = 15                            // the default maximum time to wait for a lock to be released.
const DefaultLockTimeoutInterval = 10                    // the default maximum intervals time for the locking timout.
const DefaultAdvisoryLockingFlag = true                  // the default value for the advisory locking feature flag. Default is true.
const LockIndexName = "lock_unique_key"                  // the name of the index which adds unique constraint to the locking_key field.
const contextWaitTimeout = 5 * time.Second               // how long to wait for the request to mongo to block/wait for.

var (
	ErrNoDatabaseName            = fmt.Errorf("no database name")
	ErrNilConfig                 = fmt.Errorf("no config")
	ErrLockTimeoutConfigConflict = fmt.Errorf("both x-advisory-lock-timeout-interval and x-advisory-lock-timout-interval were specified")
)

type Mongo struct {
	client   *mongo.Client
	db       *mongo.Database
	config   *Config
	isLocked atomic.Bool
}

type Locking struct {
	CollectionName string
	Timeout        int
	Enabled        bool
	Interval       int
}
type Config struct {
	DatabaseName         string
	MigrationsCollection string
	TransactionMode      bool
	Locking              Locking
}
type versionInfo struct {
	Version int  `bson:"version"`
	Dirty   bool `bson:"dirty"`
}

type lockObj struct {
	Key       int       `bson:"locking_key"`
	Pid       int       `bson:"pid"`
	Hostname  string    `bson:"hostname"`
	CreatedAt time.Time `bson:"created_at"`
}
type findFilter struct {
	Key int `bson:"locking_key"`
}

func WithInstance(instance *mongo.Client, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}
	if len(config.DatabaseName) == 0 {
		return nil, ErrNoDatabaseName
	}
	if len(config.MigrationsCollection) == 0 {
		config.MigrationsCollection = DefaultMigrationsCollection
	}
	if len(config.Locking.CollectionName) == 0 {
		config.Locking.CollectionName = DefaultLockingCollection
	}
	if config.Locking.Timeout <= 0 {
		config.Locking.Timeout = DefaultLockTimeout
	}
	if config.Locking.Interval <= 0 {
		config.Locking.Interval = DefaultLockTimeoutInterval
	}

	mc := &Mongo{
		client: instance,
		db:     instance.Database(config.DatabaseName),
		config: config,
	}

	if mc.config.Locking.Enabled {
		if err := mc.ensureLockTable(); err != nil {
			return nil, err
		}
	}
	if err := mc.ensureVersionTable(); err != nil {
		return nil, err
	}

	return mc, nil
}

func (m *Mongo) Open(dsn string) (database.Driver, error) {
	// connstring is experimental package, but it used for parse connection string in mongo.Connect function
	uri, err := connstring.Parse(dsn)
	if err != nil {
		return nil, err
	}
	if len(uri.Database) == 0 {
		return nil, ErrNoDatabaseName
	}
	unknown := url.Values(uri.UnknownOptions)

	migrationsCollection := unknown.Get("x-migrations-collection")
	lockCollection := unknown.Get("x-advisory-lock-collection")
	transactionMode, err := parseBoolean(unknown.Get("x-transaction-mode"), false)
	if err != nil {
		return nil, err
	}
	advisoryLockingFlag, err := parseBoolean(unknown.Get("x-advisory-locking"), DefaultAdvisoryLockingFlag)
	if err != nil {
		return nil, err
	}
	lockingTimout, err := parseInt(unknown.Get("x-advisory-lock-timeout"), DefaultLockTimeout)
	if err != nil {
		return nil, err
	}

	lockTimeoutIntervalValue := unknown.Get("x-advisory-lock-timeout-interval")
	// The initial release had a typo for this argument but for backwards compatibility sake, we will keep supporting it
	// and we will error out if both values are set.
	lockTimeoutIntervalValueFromTypo := unknown.Get("x-advisory-lock-timout-interval")

	lockTimeout := lockTimeoutIntervalValue

	if lockTimeoutIntervalValue != "" && lockTimeoutIntervalValueFromTypo != "" {
		return nil, ErrLockTimeoutConfigConflict
	} else if lockTimeoutIntervalValueFromTypo != "" {
		lockTimeout = lockTimeoutIntervalValueFromTypo
	}

	maxLockCheckInterval, err := parseInt(lockTimeout, DefaultLockTimeoutInterval)

	if err != nil {
		return nil, err
	}
	client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(dsn))
	if err != nil {
		return nil, err
	}

	if err = client.Ping(context.TODO(), nil); err != nil {
		return nil, err
	}
	mc, err := WithInstance(client, &Config{
		DatabaseName:         uri.Database,
		MigrationsCollection: migrationsCollection,
		TransactionMode:      transactionMode,
		Locking: Locking{
			CollectionName: lockCollection,
			Timeout:        lockingTimout,
			Enabled:        advisoryLockingFlag,
			Interval:       maxLockCheckInterval,
		},
	})
	if err != nil {
		return nil, err
	}
	return mc, nil
}

// Parse the url param, convert it to boolean
// returns error if param invalid. returns defaultValue if param not present
func parseBoolean(urlParam string, defaultValue bool) (bool, error) {

	// if parameter passed, parse it (otherwise return default value)
	if urlParam != "" {
		result, err := strconv.ParseBool(urlParam)
		if err != nil {
			return false, err
		}
		return result, nil
	}

	// if no url Param passed, return default value
	return defaultValue, nil
}

// Parse the url param, convert it to int
// returns error if param invalid. returns defaultValue if param not present
func parseInt(urlParam string, defaultValue int) (int, error) {

	// if parameter passed, parse it (otherwise return default value)
	if urlParam != "" {
		result, err := strconv.Atoi(urlParam)
		if err != nil {
			return -1, err
		}
		return result, nil
	}

	// if no url Param passed, return default value
	return defaultValue, nil
}
func (m *Mongo) SetVersion(version int, dirty bool) error {
	migrationsCollection := m.db.Collection(m.config.MigrationsCollection)
	if err := migrationsCollection.Drop(context.TODO()); err != nil {
		return &database.Error{OrigErr: err, Err: "drop migrations collection failed"}
	}
	_, err := migrationsCollection.InsertOne(context.TODO(), bson.M{"version": version, "dirty": dirty})
	if err != nil {
		return &database.Error{OrigErr: err, Err: "save version failed"}
	}
	return nil
}

func (m *Mongo) Version() (version int, dirty bool, err error) {
	var versionInfo versionInfo
	err = m.db.Collection(m.config.MigrationsCollection).FindOne(context.TODO(), bson.M{}).Decode(&versionInfo)
	switch {
	case err == mongo.ErrNoDocuments:
		return database.NilVersion, false, nil
	case err != nil:
		return 0, false, &database.Error{OrigErr: err, Err: "failed to get migration version"}
	default:
		return versionInfo.Version, versionInfo.Dirty, nil
	}
}

func (m *Mongo) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}
	var cmds []bson.D
	err = bson.UnmarshalExtJSON(migr, true, &cmds)
	if err != nil {
		return fmt.Errorf("unmarshaling json error: %s", err)
	}
	if m.config.TransactionMode {
		if err := m.executeCommandsWithTransaction(context.TODO(), cmds); err != nil {
			return err
		}
	} else {
		if err := m.executeCommands(context.TODO(), cmds); err != nil {
			return err
		}
	}
	return nil
}

func (m *Mongo) executeCommandsWithTransaction(ctx context.Context, cmds []bson.D) error {
	err := m.db.Client().UseSession(ctx, func(sessionContext mongo.SessionContext) error {
		if err := sessionContext.StartTransaction(); err != nil {
			return &database.Error{OrigErr: err, Err: "failed to start transaction"}
		}
		if err := m.executeCommands(sessionContext, cmds); err != nil {
			// When command execution is failed, it's aborting transaction
			// If you tried to call abortTransaction, it`s return error that transaction already aborted
			return err
		}
		if err := sessionContext.CommitTransaction(sessionContext); err != nil {
			return &database.Error{OrigErr: err, Err: "failed to commit transaction"}
		}
		return nil
	})
	if err != nil {
		return err
	}
	return nil
}

func (m *Mongo) executeCommands(ctx context.Context, cmds []bson.D) error {
	for _, cmd := range cmds {
		err := m.db.RunCommand(ctx, cmd).Err()
		if err != nil {
			return &database.Error{OrigErr: err, Err: fmt.Sprintf("failed to execute command:%v", cmd)}
		}
	}
	return nil
}

func (m *Mongo) Close() error {
	return m.client.Disconnect(context.TODO())
}

func (m *Mongo) Drop() error {
	return m.db.Drop(context.TODO())
}

func (m *Mongo) ensureLockTable() error {
	indexes := m.db.Collection(m.config.Locking.CollectionName).Indexes()

	indexOptions := options.Index().SetUnique(true).SetName(LockIndexName)
	_, err := indexes.CreateOne(context.TODO(), mongo.IndexModel{
		Options: indexOptions,
		Keys:    findFilter{Key: -1},
	})
	if err != nil {
		return err
	}
	return nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the MongoDb type.
func (m *Mongo) ensureVersionTable() (err error) {
	if err = m.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := m.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	if err != nil {
		return err
	}
	if _, _, err = m.Version(); err != nil {
		return err
	}
	return nil
}

// Utilizes advisory locking on the config.LockingCollection collection
// This uses a unique index on the `locking_key` field.
func (m *Mongo) Lock() error {
	return database.CasRestoreOnErr(&m.isLocked, false, true, database.ErrLocked, func() error {
		if !m.config.Locking.Enabled {
			return nil
		}

		pid := os.Getpid()
		hostname, err := os.Hostname()
		if err != nil {
			hostname = fmt.Sprintf("Could not determine hostname. Error: %s", err.Error())
		}

		newLockObj := lockObj{
			Key:       lockKeyUniqueValue,
			Pid:       pid,
			Hostname:  hostname,
			CreatedAt: time.Now(),
		}
		operation := func() error {
			timeout, cancelFunc := context.WithTimeout(context.Background(), contextWaitTimeout)
			_, err := m.db.Collection(m.config.Locking.CollectionName).InsertOne(timeout, newLockObj)
			defer cancelFunc()
			return err
		}
		exponentialBackOff := backoff.NewExponentialBackOff()
		duration := time.Duration(m.config.Locking.Timeout) * time.Second
		exponentialBackOff.MaxElapsedTime = duration
		exponentialBackOff.MaxInterval = time.Duration(m.config.Locking.Interval) * time.Second

		err = backoff.Retry(operation, exponentialBackOff)
		if err != nil {
			return database.ErrLocked
		}

		return nil
	})
}

func (m *Mongo) Unlock() error {
	return database.CasRestoreOnErr(&m.isLocked, true, false, database.ErrNotLocked, func() error {
		if !m.config.Locking.Enabled {
			return nil
		}

		filter := findFilter{
			Key: lockKeyUniqueValue,
		}

		ctx, cancel := context.WithTimeout(context.Background(), contextWaitTimeout)
		_, err := m.db.Collection(m.config.Locking.CollectionName).DeleteMany(ctx, filter)
		defer cancel()

		if err != nil {
			return err
		}
		return nil
	})
}
```

## File: `database/mongodb/mongodb_test.go`
```go
package mongodb

import (
	"bytes"
	"context"
	"fmt"

	"log"

	"github.com/golang-migrate/migrate/v4"
	"io"
	"os"
	"strconv"
	"testing"
	"time"
)

import (
	"github.com/dhui/dktest"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

import (
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

var (
	opts = dktest.Options{PortRequired: true, ReadyFunc: isReady}
	// Supported versions: https://www.mongodb.com/support-policy
	specs = []dktesting.ContainerSpec{
		{ImageName: "mongo:5.0", Options: opts},
		{ImageName: "mongo:6.0", Options: opts},
		{ImageName: "mongo:7.0", Options: opts},
		{ImageName: "mongo:8.0", Options: opts},
	}
)

func mongoConnectionString(host, port string) string {
	// there is connect option for excluding serverConnection algorithm
	// it's let avoid errors with mongo replica set connection in docker container
	return fmt.Sprintf("mongodb://%s:%s/testMigration?connect=direct", host, port)
}

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	ip, port, err := c.FirstPort()
	if err != nil {
		return false
	}

	client, err := mongo.Connect(ctx, options.Client().ApplyURI(mongoConnectionString(ip, port)))
	if err != nil {
		return false
	}
	defer func() {
		if err := client.Disconnect(ctx); err != nil {
			log.Println("close error:", err)
		}
	}()

	if err = client.Ping(ctx, nil); err != nil {
		switch err {
		case io.EOF:
			return false
		default:
			log.Println(err)
		}
		return false
	}
	return true
}

func Test(t *testing.T) {
	t.Run("test", test)
	t.Run("testMigrate", testMigrate)
	t.Run("testWithAuth", testWithAuth)
	t.Run("testLockWorks", testLockWorks)

	t.Cleanup(func() {
		for _, spec := range specs {
			t.Log("Cleaning up ", spec.ImageName)
			if err := spec.Cleanup(); err != nil {
				t.Error("Error removing ", spec.ImageName, "error:", err)
			}
		}
	})
}

func test(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := mongoConnectionString(ip, port)
		p := &Mongo{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		dt.TestNilVersion(t, d)
		dt.TestLockAndUnlock(t, d)
		dt.TestRun(t, d, bytes.NewReader([]byte(`[{"insert":"hello","documents":[{"wild":"world"}]}]`)))
		dt.TestSetVersion(t, d)
		dt.TestDrop(t, d)
	})
}

func testMigrate(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := mongoConnectionString(ip, port)
		p := &Mongo{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}

func testWithAuth(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := mongoConnectionString(ip, port)
		p := &Mongo{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		createUserCMD := []byte(`[{"createUser":"deminem","pwd":"gogo","roles":[{"role":"readWrite","db":"testMigration"}]}]`)
		err = d.Run(bytes.NewReader(createUserCMD))
		if err != nil {
			t.Fatal(err)
		}
		testcases := []struct {
			name            string
			connectUri      string
			isErrorExpected bool
		}{
			{"right auth data", "mongodb://deminem:gogo@%s:%v/testMigration", false},
			{"wrong auth data", "mongodb://wrong:auth@%s:%v/testMigration", true},
		}

		for _, tcase := range testcases {
			t.Run(tcase.name, func(t *testing.T) {
				mc := &Mongo{}
				d, err := mc.Open(fmt.Sprintf(tcase.connectUri, ip, port))
				if err == nil {
					defer func() {
						if err := d.Close(); err != nil {
							t.Error(err)
						}
					}()
				}

				switch {
				case tcase.isErrorExpected && err == nil:
					t.Fatalf("no error when expected")
				case !tcase.isErrorExpected && err != nil:
					t.Fatalf("unexpected error: %v", err)
				}
			})
		}
	})
}

func testLockWorks(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := mongoConnectionString(ip, port)
		p := &Mongo{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		dt.TestRun(t, d, bytes.NewReader([]byte(`[{"insert":"hello","documents":[{"wild":"world"}]}]`)))

		mc := d.(*Mongo)

		err = mc.Lock()
		if err != nil {
			t.Fatal(err)
		}
		err = mc.Unlock()
		if err != nil {
			t.Fatal(err)
		}

		err = mc.Lock()
		if err != nil {
			t.Fatal(err)
		}
		err = mc.Unlock()
		if err != nil {
			t.Fatal(err)
		}

		// enable locking,
		//try to hit a lock conflict
		mc.config.Locking.Enabled = true
		mc.config.Locking.Timeout = 1
		err = mc.Lock()
		if err != nil {
			t.Fatal(err)
		}
		err = mc.Lock()
		if err == nil {
			t.Fatal("should have failed, mongo should be locked already")
		}
	})
}

func TestTransaction(t *testing.T) {
	transactionSpecs := []dktesting.ContainerSpec{
		{ImageName: "mongo:4", Options: dktest.Options{PortRequired: true, ReadyFunc: isReady,
			Cmd: []string{"mongod", "--bind_ip_all", "--replSet", "rs0"}}},
	}
	t.Cleanup(func() {
		for _, spec := range transactionSpecs {
			t.Log("Cleaning up ", spec.ImageName)
			if err := spec.Cleanup(); err != nil {
				t.Error("Error removing ", spec.ImageName, "error:", err)
			}
		}
	})

	dktesting.ParallelTest(t, transactionSpecs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(mongoConnectionString(ip, port)))
		if err != nil {
			t.Fatal(err)
		}
		err = client.Ping(context.TODO(), nil)
		if err != nil {
			t.Fatal(err)
		}
		//rs.initiate()
		err = client.Database("admin").RunCommand(context.TODO(), bson.D{bson.E{Key: "replSetInitiate", Value: bson.D{}}}).Err()
		if err != nil {
			t.Fatal(err)
		}
		err = waitForReplicaInit(client)
		if err != nil {
			t.Fatal(err)
		}
		d, err := WithInstance(client, &Config{
			DatabaseName: "testMigration",
		})
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		//We have to create collection
		//transactions don't support operations with creating new dbs, collections
		//Unique index need for checking transaction aborting
		insertCMD := []byte(`[
				{"create":"hello"},
				{"createIndexes": "hello",
					"indexes": [{
						"key": {
							"wild": 1
						},
						"name": "unique_wild",
						"unique": true,
						"background": true
					}]
			}]`)
		err = d.Run(bytes.NewReader(insertCMD))
		if err != nil {
			t.Fatal(err)
		}
		testcases := []struct {
			name            string
			cmds            []byte
			documentsCount  int64
			isErrorExpected bool
		}{
			{
				name: "success transaction",
				cmds: []byte(`[{"insert":"hello","documents":[
										{"wild":"world"},
										{"wild":"west"},
										{"wild":"natural"}
									 ]
								  }]`),
				documentsCount:  3,
				isErrorExpected: false,
			},
			{
				name: "failure transaction",
				//transaction have to be failure - duplicate unique key wild:west
				//none of the documents should be added
				cmds: []byte(`[{"insert":"hello","documents":[{"wild":"flower"}]},
									{"insert":"hello","documents":[
										{"wild":"cat"},
										{"wild":"west"}
									 ]
								  }]`),
				documentsCount:  3,
				isErrorExpected: true,
			},
		}
		for _, tcase := range testcases {
			t.Run(tcase.name, func(t *testing.T) {
				client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(mongoConnectionString(ip, port)))
				if err != nil {
					t.Fatal(err)
				}
				err = client.Ping(context.TODO(), nil)
				if err != nil {
					t.Fatal(err)
				}
				d, err := WithInstance(client, &Config{
					DatabaseName:    "testMigration",
					TransactionMode: true,
				})
				if err != nil {
					t.Fatal(err)
				}
				defer func() {
					if err := d.Close(); err != nil {
						t.Error(err)
					}
				}()
				runErr := d.Run(bytes.NewReader(tcase.cmds))
				if runErr != nil {
					if !tcase.isErrorExpected {
						t.Fatal(runErr)
					}
				}
				documentsCount, err := client.Database("testMigration").Collection("hello").CountDocuments(context.TODO(), bson.M{})
				if err != nil {
					t.Fatal(err)
				}
				if tcase.documentsCount != documentsCount {
					t.Fatalf("expected %d and actual %d documents count not equal. run migration error:%s", tcase.documentsCount, documentsCount, runErr)
				}
			})
		}
	})
}

type isMaster struct {
	IsMaster bool `bson:"ismaster"`
}

func waitForReplicaInit(client *mongo.Client) error {
	ticker := time.NewTicker(time.Second * 1)
	defer ticker.Stop()
	timeout, err := strconv.Atoi(os.Getenv("MIGRATE_TEST_MONGO_REPLICA_SET_INIT_TIMEOUT"))
	if err != nil {
		timeout = 30
	}
	timeoutTimer := time.NewTimer(time.Duration(timeout) * time.Second)
	defer timeoutTimer.Stop()
	for {
		select {
		case <-ticker.C:
			var status isMaster
			//Check that node is primary because
			//during replica set initialization, the first node first becomes a secondary and then becomes the primary
			//should consider that initialization is completed only after the node has become the primary
			result := client.Database("admin").RunCommand(context.TODO(), bson.D{bson.E{Key: "isMaster", Value: 1}})
			r, err := result.DecodeBytes()
			if err != nil {
				return err
			}
			err = bson.Unmarshal(r, &status)
			if err != nil {
				return err
			}
			if status.IsMaster {
				return nil
			}
		case <-timeoutTimer.C:
			return fmt.Errorf("replica init timeout")
		}
	}

}
```

## File: `database/mongodb/README.md`
```markdown
# MongoDB

* Driver work with mongo through [db.runCommands](https://docs.mongodb.com/manual/reference/command/)
* Migrations support json format. It contains array of commands for `db.runCommand`. Every command is executed in separate request to database 
* All keys have to be in quotes `"`
* [Examples](./examples)

# Usage

`mongodb://user:password@host:port/dbname?query` (`mongodb+srv://` also works, but behaves a bit differently. See [docs](https://docs.mongodb.com/manual/reference/connection-string/#dns-seedlist-connection-format) for more information)

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-migrations-collection` | `MigrationsCollection` | Name of the migrations collection |
| `x-transaction-mode` | `TransactionMode` | If set to `true` wrap commands in [transaction](https://docs.mongodb.com/manual/core/transactions). Available only for replica set. Driver is using [strconv.ParseBool](https://golang.org/pkg/strconv/#ParseBool) for parsing|
| `x-advisory-locking` | `true` | Feature flag for advisory locking, if set to false, disable advisory locking |
| `x-advisory-lock-collection` | `migrate_advisory_lock` | The name of the collection to use for advisory locking.|
| `x-advisory-lock-timeout` | `15` | The max time in seconds that migrate will wait to acquire a lock before failing. |
| `x-advisory-lock-timeout-interval` | `10` | The max time in seconds between attempts to acquire the advisory lock, the lock is attempted to be acquired using an exponential backoff algorithm. |
| `dbname` | `DatabaseName` | The name of the database to connect to |
| `user` | | The user to sign in as. Can be omitted |
| `password` | | The user's password. Can be omitted | 
| `host` | | The host to connect to |
| `port` | | The port to bind to |
```

## File: `database/mongodb/examples/migrations/001_create_user.down.json`
```json
[
  {
    "dropUser": "deminem"
  }
]
```

## File: `database/mongodb/examples/migrations/001_create_user.up.json`
```json
[
  {
    "createUser": "deminem",
    "pwd": "gogo",
    "roles": [
      {
        "role": "readWrite",
        "db": "testMigration"
      }
    ]
  }
]
```

## File: `database/mongodb/examples/migrations/002_create_indexes.down.json`
```json
[
  {
    "dropIndexes": "mycollection",
    "index": "username_sort_by_asc_created"
  },
  {
    "dropIndexes": "mycollection",
    "index": "unique_email"
  }
]
```

## File: `database/mongodb/examples/migrations/002_create_indexes.up.json`
```json
[{
  "createIndexes": "mycollection",
  "indexes": [
    {
      "key": {
        "username": 1,
        "created": -1
      },
      "name": "username_sort_by_asc_created",
      "background": true
    },
    {
      "key": {
        "email": 1
      },
      "name": "unique_email",
      "unique": true,
      "background": true
    }
  ]
}]
```

## File: `database/mongodb/examples/migrations/003_add_new_field.down.json`
```json
[
    {
        "update": "users",
        "updates": [
            {
                "q": {},
                "u": {
                    "$unset": {
                        "status": ""
                    }
                },
                "multi": true
            }
        ]
    }
]
```

## File: `database/mongodb/examples/migrations/003_add_new_field.up.json`
```json
[
    {
        "update": "users",
        "updates": [
            {
                "q": {},
                "u": {
                    "$set": {
                        "status": "active"
                    }
                },
                "multi": true
            }
        ]
    }
]
```

## File: `database/mongodb/examples/migrations/004_replace_field_value_from_another_field.down.json`
```json
[
    {
        "update": "users",
        "updates": [
            {
                "q": {},
                "u": {
                    "fullname": ""
                },
                "multi": true
            }
        ]
    }
]
```

## File: `database/mongodb/examples/migrations/004_replace_field_value_from_another_field.up.json`
```json
[
    {
        "aggregate": "users",
        "pipeline": [
            {
                "$project": {
                    "_id": 1,
                    "firstname": 1,
                    "lastname": 1,
                    "username": 1,
                    "password": 1,
                    "email": 1,
                    "active": 1,
                    "fullname": { "$concat": ["$firstname", " ", "$lastname"] }
                }
            },
            {
                "$out": "users"
            }
        ],
        "cursor": {}
    }
]
```

## File: `database/multistmt/parse.go`
```go
// Package multistmt provides methods for parsing multi-statement database migrations
package multistmt

import (
	"bufio"
	"bytes"
	"io"
)

// StartBufSize is the default starting size of the buffer used to scan and parse multi-statement migrations
var StartBufSize = 4096

// Handler handles a single migration parsed from a multi-statement migration.
// It's given the single migration to handle and returns whether or not further statements
// from the multi-statement migration should be parsed and handled.
type Handler func(migration []byte) bool

func splitWithDelimiter(delimiter []byte) func(d []byte, atEOF bool) (int, []byte, error) {
	return func(d []byte, atEOF bool) (int, []byte, error) {
		// SplitFunc inspired by bufio.ScanLines() implementation
		if atEOF {
			if len(d) == 0 {
				return 0, nil, nil
			}
			return len(d), d, nil
		}
		if i := bytes.Index(d, delimiter); i >= 0 {
			return i + len(delimiter), d[:i+len(delimiter)], nil
		}
		return 0, nil, nil
	}
}

// Parse parses the given multi-statement migration
func Parse(reader io.Reader, delimiter []byte, maxMigrationSize int, h Handler) error {
	scanner := bufio.NewScanner(reader)
	scanner.Buffer(make([]byte, 0, StartBufSize), maxMigrationSize)
	scanner.Split(splitWithDelimiter(delimiter))
	for scanner.Scan() {
		cont := h(scanner.Bytes())
		if !cont {
			break
		}
	}
	return scanner.Err()
}
```

## File: `database/multistmt/parse_test.go`
```go
package multistmt_test

import (
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/golang-migrate/migrate/v4/database/multistmt"
)

const maxMigrationSize = 1024

func TestParse(t *testing.T) {
	testCases := []struct {
		name        string
		multiStmt   string
		delimiter   string
		expected    []string
		expectedErr error
	}{
		{name: "single statement, no delimiter", multiStmt: "single statement, no delimiter", delimiter: ";",
			expected: []string{"single statement, no delimiter"}, expectedErr: nil},
		{name: "single statement, one delimiter", multiStmt: "single statement, one delimiter;", delimiter: ";",
			expected: []string{"single statement, one delimiter;"}, expectedErr: nil},
		{name: "two statements, no trailing delimiter", multiStmt: "statement one; statement two", delimiter: ";",
			expected: []string{"statement one;", " statement two"}, expectedErr: nil},
		{name: "two statements, with trailing delimiter", multiStmt: "statement one; statement two;", delimiter: ";",
			expected: []string{"statement one;", " statement two;"}, expectedErr: nil},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			stmts := make([]string, 0, len(tc.expected))
			err := multistmt.Parse(strings.NewReader(tc.multiStmt), []byte(tc.delimiter), maxMigrationSize, func(b []byte) bool {
				stmts = append(stmts, string(b))
				return true
			})
			assert.Equal(t, tc.expectedErr, err)
			assert.Equal(t, tc.expected, stmts)
		})
	}
}

func TestParseDiscontinue(t *testing.T) {
	multiStmt := "statement one; statement two"
	delimiter := ";"
	expected := []string{"statement one;"}

	stmts := make([]string, 0, len(expected))
	err := multistmt.Parse(strings.NewReader(multiStmt), []byte(delimiter), maxMigrationSize, func(b []byte) bool {
		stmts = append(stmts, string(b))
		return false
	})
	assert.Nil(t, err)
	assert.Equal(t, expected, stmts)
}
```

## File: `database/mysql/mysql.go`
```go
//go:build go1.9

package mysql

import (
	"context"
	"crypto/tls"
	"crypto/x509"
	"database/sql"
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"os"
	"strconv"
	"strings"
	"sync/atomic"
	"time"

	"github.com/go-sql-driver/mysql"
	"github.com/golang-migrate/migrate/v4/database"
)

var _ database.Driver = (*Mysql)(nil) // explicit compile time type check

func init() {
	database.Register("mysql", &Mysql{})
}

var DefaultMigrationsTable = "schema_migrations"

var (
	ErrDatabaseDirty    = fmt.Errorf("database is dirty")
	ErrNilConfig        = fmt.Errorf("no config")
	ErrNoDatabaseName   = fmt.Errorf("no database name")
	ErrAppendPEM        = fmt.Errorf("failed to append PEM")
	ErrTLSCertKeyConfig = fmt.Errorf("to use TLS client authentication, both x-tls-cert and x-tls-key must not be empty")
)

type Config struct {
	MigrationsTable  string
	DatabaseName     string
	NoLock           bool
	StatementTimeout time.Duration
}

type Mysql struct {
	// mysql RELEASE_LOCK must be called from the same conn, so
	// just do everything over a single conn anyway.
	conn     *sql.Conn
	db       *sql.DB
	isLocked atomic.Bool

	config *Config
}

// connection instance must have `multiStatements` set to true
func WithConnection(ctx context.Context, conn *sql.Conn, config *Config) (*Mysql, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := conn.PingContext(ctx); err != nil {
		return nil, err
	}

	mx := &Mysql{
		conn:   conn,
		db:     nil,
		config: config,
	}

	if config.DatabaseName == "" {
		query := `SELECT DATABASE()`
		var databaseName sql.NullString
		if err := conn.QueryRowContext(ctx, query).Scan(&databaseName); err != nil {
			return nil, &database.Error{OrigErr: err, Query: []byte(query)}
		}

		if len(databaseName.String) == 0 {
			return nil, ErrNoDatabaseName
		}

		config.DatabaseName = databaseName.String
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	if err := mx.ensureVersionTable(); err != nil {
		return nil, err
	}

	return mx, nil
}

// instance must have `multiStatements` set to true
func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	ctx := context.Background()

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	conn, err := instance.Conn(ctx)
	if err != nil {
		return nil, err
	}

	mx, err := WithConnection(ctx, conn, config)
	if err != nil {
		return nil, err
	}

	mx.db = instance

	return mx, nil
}

// extractCustomQueryParams extracts the custom query params (ones that start with "x-") from
// mysql.Config.Params (connection parameters) as to not interfere with connecting to MySQL
func extractCustomQueryParams(c *mysql.Config) (map[string]string, error) {
	if c == nil {
		return nil, ErrNilConfig
	}
	customQueryParams := map[string]string{}

	for k, v := range c.Params {
		if strings.HasPrefix(k, "x-") {
			customQueryParams[k] = v
			delete(c.Params, k)
		}
	}
	return customQueryParams, nil
}

func urlToMySQLConfig(url string) (*mysql.Config, error) {
	// Need to parse out custom TLS parameters and call
	// mysql.RegisterTLSConfig() before mysql.ParseDSN() is called
	// which consumes the registered tls.Config
	// Fixes: https://github.com/golang-migrate/migrate/issues/411
	//
	// Can't use url.Parse() since it fails to parse MySQL DSNs
	// mysql.ParseDSN() also searches for "?" to find query parameters:
	// https://github.com/go-sql-driver/mysql/blob/46351a8/dsn.go#L344
	if idx := strings.LastIndex(url, "?"); idx > 0 {
		rawParams := url[idx+1:]
		parsedParams, err := nurl.ParseQuery(rawParams)
		if err != nil {
			return nil, err
		}

		ctls := parsedParams.Get("tls")
		if len(ctls) > 0 {
			if _, isBool := readBool(ctls); !isBool && strings.ToLower(ctls) != "skip-verify" {
				rootCertPool := x509.NewCertPool()
				pem, err := os.ReadFile(parsedParams.Get("x-tls-ca"))
				if err != nil {
					return nil, err
				}

				if ok := rootCertPool.AppendCertsFromPEM(pem); !ok {
					return nil, ErrAppendPEM
				}

				clientCert := make([]tls.Certificate, 0, 1)
				if ccert, ckey := parsedParams.Get("x-tls-cert"), parsedParams.Get("x-tls-key"); ccert != "" || ckey != "" {
					if ccert == "" || ckey == "" {
						return nil, ErrTLSCertKeyConfig
					}
					certs, err := tls.LoadX509KeyPair(ccert, ckey)
					if err != nil {
						return nil, err
					}
					clientCert = append(clientCert, certs)
				}

				insecureSkipVerify := false
				insecureSkipVerifyStr := parsedParams.Get("x-tls-insecure-skip-verify")
				if len(insecureSkipVerifyStr) > 0 {
					x, err := strconv.ParseBool(insecureSkipVerifyStr)
					if err != nil {
						return nil, err
					}
					insecureSkipVerify = x
				}

				err = mysql.RegisterTLSConfig(ctls, &tls.Config{
					RootCAs:            rootCertPool,
					Certificates:       clientCert,
					InsecureSkipVerify: insecureSkipVerify,
				})
				if err != nil {
					return nil, err
				}
			}
		}
	}

	config, err := mysql.ParseDSN(strings.TrimPrefix(url, "mysql://"))
	if err != nil {
		return nil, err
	}

	config.MultiStatements = true

	// Keep backwards compatibility from when we used net/url.Parse() to parse the DSN.
	// net/url.Parse() would automatically unescape it for us.
	// See: https://play.golang.org/p/q9j1io-YICQ
	user, err := nurl.QueryUnescape(config.User)
	if err != nil {
		return nil, err
	}
	config.User = user

	password, err := nurl.QueryUnescape(config.Passwd)
	if err != nil {
		return nil, err
	}
	config.Passwd = password

	return config, nil
}

func (m *Mysql) Open(url string) (database.Driver, error) {
	config, err := urlToMySQLConfig(url)
	if err != nil {
		return nil, err
	}

	customParams, err := extractCustomQueryParams(config)
	if err != nil {
		return nil, err
	}

	noLockParam, noLock := customParams["x-no-lock"], false
	if noLockParam != "" {
		noLock, err = strconv.ParseBool(noLockParam)
		if err != nil {
			return nil, fmt.Errorf("could not parse x-no-lock as bool: %w", err)
		}
	}

	statementTimeoutParam := customParams["x-statement-timeout"]
	statementTimeout := 0
	if statementTimeoutParam != "" {
		statementTimeout, err = strconv.Atoi(statementTimeoutParam)
		if err != nil {
			return nil, fmt.Errorf("could not parse x-statement-timeout as float: %w", err)
		}
	}

	db, err := sql.Open("mysql", config.FormatDSN())
	if err != nil {
		return nil, err
	}

	mx, err := WithInstance(db, &Config{
		DatabaseName:     config.DBName,
		MigrationsTable:  customParams["x-migrations-table"],
		NoLock:           noLock,
		StatementTimeout: time.Duration(statementTimeout) * time.Millisecond,
	})
	if err != nil {
		return nil, err
	}

	return mx, nil
}

func (m *Mysql) Close() error {
	connErr := m.conn.Close()
	var dbErr error
	if m.db != nil {
		dbErr = m.db.Close()
	}

	if connErr != nil || dbErr != nil {
		return fmt.Errorf("conn: %v, db: %v", connErr, dbErr)
	}
	return nil
}

func (m *Mysql) Lock() error {
	return database.CasRestoreOnErr(&m.isLocked, false, true, database.ErrLocked, func() error {
		if m.config.NoLock {
			return nil
		}
		aid, err := database.GenerateAdvisoryLockId(
			fmt.Sprintf("%s:%s", m.config.DatabaseName, m.config.MigrationsTable))
		if err != nil {
			return err
		}

		query := "SELECT GET_LOCK(?, 10)"
		var success bool
		if err := m.conn.QueryRowContext(context.Background(), query, aid).Scan(&success); err != nil {
			return &database.Error{OrigErr: err, Err: "try lock failed", Query: []byte(query)}
		}

		if !success {
			return database.ErrLocked
		}

		return nil
	})
}

func (m *Mysql) Unlock() error {
	return database.CasRestoreOnErr(&m.isLocked, true, false, database.ErrNotLocked, func() error {
		if m.config.NoLock {
			return nil
		}

		aid, err := database.GenerateAdvisoryLockId(
			fmt.Sprintf("%s:%s", m.config.DatabaseName, m.config.MigrationsTable))
		if err != nil {
			return err
		}

		query := `SELECT RELEASE_LOCK(?)`
		if _, err := m.conn.ExecContext(context.Background(), query, aid); err != nil {
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}

		// NOTE: RELEASE_LOCK could return NULL or (or 0 if the code is changed),
		// in which case isLocked should be true until the timeout expires -- synchronizing
		// these states is likely not worth trying to do; reconsider the necessity of isLocked.

		return nil
	})
}

func (m *Mysql) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}

	ctx := context.Background()
	if m.config.StatementTimeout != 0 {
		var cancel context.CancelFunc
		ctx, cancel = context.WithTimeout(ctx, m.config.StatementTimeout)
		defer cancel()
	}

	query := string(migr[:])
	if _, err := m.conn.ExecContext(ctx, query); err != nil {
		return database.Error{OrigErr: err, Err: "migration failed", Query: migr}
	}

	return nil
}

func (m *Mysql) SetVersion(version int, dirty bool) error {
	tx, err := m.conn.BeginTx(context.Background(), &sql.TxOptions{Isolation: sql.LevelSerializable})
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}

	query := "DELETE FROM `" + m.config.MigrationsTable + "` LIMIT 1"
	if _, err := tx.ExecContext(context.Background(), query); err != nil {
		if errRollback := tx.Rollback(); errRollback != nil {
			err = errors.Join(err, errRollback)
		}
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	// Also re-write the schema version for nil dirty versions to prevent
	// empty schema version for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330
	if version >= 0 || (version == database.NilVersion && dirty) {
		query := "INSERT INTO `" + m.config.MigrationsTable + "` (version, dirty) VALUES (?, ?)"
		if _, err := tx.ExecContext(context.Background(), query, version, dirty); err != nil {
			if errRollback := tx.Rollback(); errRollback != nil {
				err = errors.Join(err, errRollback)
			}
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}

	return nil
}

func (m *Mysql) Version() (version int, dirty bool, err error) {
	query := "SELECT version, dirty FROM `" + m.config.MigrationsTable + "` LIMIT 1"
	err = m.conn.QueryRowContext(context.Background(), query).Scan(&version, &dirty)
	switch {
	case err == sql.ErrNoRows:
		return database.NilVersion, false, nil

	case err != nil:
		if e, ok := err.(*mysql.MySQLError); ok {
			if e.Number == 0 {
				return database.NilVersion, false, nil
			}
		}
		return 0, false, &database.Error{OrigErr: err, Query: []byte(query)}

	default:
		return version, dirty, nil
	}
}

func (m *Mysql) Drop() (err error) {
	// select all tables
	query := `SHOW TABLES LIKE '%'`
	tables, err := m.conn.QueryContext(context.Background(), query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	// delete one table after another
	tableNames := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}
		if len(tableName) > 0 {
			tableNames = append(tableNames, tableName)
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if len(tableNames) > 0 {
		// disable checking foreign key constraints until finished
		query = `SET foreign_key_checks = 0`
		if _, err := m.conn.ExecContext(context.Background(), query); err != nil {
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}

		defer func() {
			// enable foreign key checks
			_, _ = m.conn.ExecContext(context.Background(), `SET foreign_key_checks = 1`)
		}()

		// delete one by one ...
		for _, t := range tableNames {
			query = "DROP TABLE IF EXISTS `" + t + "`"
			if _, err := m.conn.ExecContext(context.Background(), query); err != nil {
				return &database.Error{OrigErr: err, Query: []byte(query)}
			}
		}
	}

	return nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the Mysql type.
func (m *Mysql) ensureVersionTable() (err error) {
	if err = m.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := m.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	// check if migration table exists
	var result string
	query := `SHOW TABLES LIKE '` + m.config.MigrationsTable + `'`
	if err := m.conn.QueryRowContext(context.Background(), query).Scan(&result); err != nil {
		if err != sql.ErrNoRows {
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	} else {
		return nil
	}

	// if not, create the empty migration table
	query = "CREATE TABLE `" + m.config.MigrationsTable + "` (version bigint not null primary key, dirty boolean not null)"
	if _, err := m.conn.ExecContext(context.Background(), query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	return nil
}

// Returns the bool value of the input.
// The 2nd return value indicates if the input was a valid bool value
// See https://github.com/go-sql-driver/mysql/blob/a059889267dc7170331388008528b3b44479bffb/utils.go#L71
func readBool(input string) (value bool, valid bool) {
	switch input {
	case "1", "true", "TRUE", "True":
		return true, true
	case "0", "false", "FALSE", "False":
		return false, true
	}

	// Not a valid bool value
	return
}
```

## File: `database/mysql/mysql_test.go`
```go
package mysql

import (
	"context"
	"crypto/ed25519"
	"crypto/x509"
	"database/sql"
	sqldriver "database/sql/driver"
	"encoding/pem"
	"errors"
	"fmt"
	"log"
	"math/big"
	"math/rand"
	"net/url"
	"os"
	"strconv"
	"testing"

	"github.com/dhui/dktest"
	"github.com/go-sql-driver/mysql"
	"github.com/golang-migrate/migrate/v4"
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"
	_ "github.com/golang-migrate/migrate/v4/source/file"
	"github.com/stretchr/testify/assert"
)

const defaultPort = 3306

var (
	opts = dktest.Options{
		Env:          map[string]string{"MYSQL_ROOT_PASSWORD": "root", "MYSQL_DATABASE": "public"},
		PortRequired: true, ReadyFunc: isReady,
	}
	optsAnsiQuotes = dktest.Options{
		Env:          map[string]string{"MYSQL_ROOT_PASSWORD": "root", "MYSQL_DATABASE": "public"},
		PortRequired: true, ReadyFunc: isReady,
		Cmd: []string{"--sql-mode=ANSI_QUOTES"},
	}
	// Supported versions: https://www.mysql.com/support/supportedplatforms/database.html
	specs = []dktesting.ContainerSpec{
		{ImageName: "mysql:8.0", Options: opts},
		{ImageName: "mysql:8.4", Options: opts},
		{ImageName: "mysql:9.0", Options: opts},
	}
	specsAnsiQuotes = []dktesting.ContainerSpec{
		{ImageName: "mysql:8.0", Options: optsAnsiQuotes},
		{ImageName: "mysql:8.4", Options: optsAnsiQuotes},
		{ImageName: "mysql:9.0", Options: optsAnsiQuotes},
	}
)

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	ip, port, err := c.Port(defaultPort)
	if err != nil {
		return false
	}

	db, err := sql.Open("mysql", fmt.Sprintf("root:root@tcp(%v:%v)/public", ip, port))
	if err != nil {
		return false
	}
	defer func() {
		if err := db.Close(); err != nil {
			log.Println("close error:", err)
		}
	}()
	if err = db.PingContext(ctx); err != nil {
		switch err {
		case sqldriver.ErrBadConn, mysql.ErrInvalidConn:
			return false
		default:
			fmt.Println(err)
		}
		return false
	}

	return true
}

func Test(t *testing.T) {
	// mysql.SetLogger(mysql.Logger(log.New(io.Discard, "", log.Ltime)))

	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := fmt.Sprintf("mysql://root:root@tcp(%v:%v)/public", ip, port)
		p := &Mysql{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		dt.Test(t, d, []byte("SELECT 1"))

		// check ensureVersionTable
		if err := d.(*Mysql).ensureVersionTable(); err != nil {
			t.Fatal(err)
		}
		// check again
		if err := d.(*Mysql).ensureVersionTable(); err != nil {
			t.Fatal(err)
		}
	})
}

func TestMigrate(t *testing.T) {
	// mysql.SetLogger(mysql.Logger(log.New(io.Discard, "", log.Ltime)))

	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := fmt.Sprintf("mysql://root:root@tcp(%v:%v)/public", ip, port)
		p := &Mysql{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "public", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)

		// check ensureVersionTable
		if err := d.(*Mysql).ensureVersionTable(); err != nil {
			t.Fatal(err)
		}
		// check again
		if err := d.(*Mysql).ensureVersionTable(); err != nil {
			t.Fatal(err)
		}
	})
}

func TestMigrateAnsiQuotes(t *testing.T) {
	// mysql.SetLogger(mysql.Logger(log.New(io.Discard, "", log.Ltime)))

	dktesting.ParallelTest(t, specsAnsiQuotes, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := fmt.Sprintf("mysql://root:root@tcp(%v:%v)/public", ip, port)
		p := &Mysql{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "public", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)

		// check ensureVersionTable
		if err := d.(*Mysql).ensureVersionTable(); err != nil {
			t.Fatal(err)
		}
		// check again
		if err := d.(*Mysql).ensureVersionTable(); err != nil {
			t.Fatal(err)
		}
	})
}

func TestLockWorks(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := fmt.Sprintf("mysql://root:root@tcp(%v:%v)/public", ip, port)
		p := &Mysql{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		dt.Test(t, d, []byte("SELECT 1"))

		ms := d.(*Mysql)

		err = ms.Lock()
		if err != nil {
			t.Fatal(err)
		}
		err = ms.Unlock()
		if err != nil {
			t.Fatal(err)
		}

		// make sure the 2nd lock works (RELEASE_LOCK is very finicky)
		err = ms.Lock()
		if err != nil {
			t.Fatal(err)
		}
		err = ms.Unlock()
		if err != nil {
			t.Fatal(err)
		}
	})
}

func TestNoLockParamValidation(t *testing.T) {
	ip := "127.0.0.1"
	port := 3306
	addr := fmt.Sprintf("mysql://root:root@tcp(%v:%v)/public", ip, port)
	p := &Mysql{}
	_, err := p.Open(addr + "?x-no-lock=not-a-bool")
	if !errors.Is(err, strconv.ErrSyntax) {
		t.Fatal("Expected syntax error when passing a non-bool as x-no-lock parameter")
	}
}

func TestNoLockWorks(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := fmt.Sprintf("mysql://root:root@tcp(%v:%v)/public", ip, port)
		p := &Mysql{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}

		lock := d.(*Mysql)

		p = &Mysql{}
		d, err = p.Open(addr + "?x-no-lock=true")
		if err != nil {
			t.Fatal(err)
		}

		noLock := d.(*Mysql)

		// Should be possible to take real lock and no-lock at the same time
		if err = lock.Lock(); err != nil {
			t.Fatal(err)
		}
		if err = noLock.Lock(); err != nil {
			t.Fatal(err)
		}
		if err = lock.Unlock(); err != nil {
			t.Fatal(err)
		}
		if err = noLock.Unlock(); err != nil {
			t.Fatal(err)
		}
	})
}

func TestExtractCustomQueryParams(t *testing.T) {
	testcases := []struct {
		name                 string
		config               *mysql.Config
		expectedParams       map[string]string
		expectedCustomParams map[string]string
		expectedErr          error
	}{
		{name: "nil config", expectedErr: ErrNilConfig},
		{
			name:                 "no params",
			config:               mysql.NewConfig(),
			expectedCustomParams: map[string]string{},
		},
		{
			name:                 "no custom params",
			config:               &mysql.Config{Params: map[string]string{"hello": "world"}},
			expectedParams:       map[string]string{"hello": "world"},
			expectedCustomParams: map[string]string{},
		},
		{
			name: "one param, one custom param",
			config: &mysql.Config{
				Params: map[string]string{"hello": "world", "x-foo": "bar"},
			},
			expectedParams:       map[string]string{"hello": "world"},
			expectedCustomParams: map[string]string{"x-foo": "bar"},
		},
		{
			name: "multiple params, multiple custom params",
			config: &mysql.Config{
				Params: map[string]string{
					"hello": "world",
					"x-foo": "bar",
					"dead":  "beef",
					"x-cat": "hat",
				},
			},
			expectedParams:       map[string]string{"hello": "world", "dead": "beef"},
			expectedCustomParams: map[string]string{"x-foo": "bar", "x-cat": "hat"},
		},
	}
	for _, tc := range testcases {
		t.Run(tc.name, func(t *testing.T) {
			customParams, err := extractCustomQueryParams(tc.config)
			if tc.config != nil {
				assert.Equal(t, tc.expectedParams, tc.config.Params,
					"Expected config params have custom params properly removed")
			}
			assert.Equal(t, tc.expectedErr, err, "Expected errors to match")
			assert.Equal(t, tc.expectedCustomParams, customParams,
				"Expected custom params to be properly extracted")
		})
	}
}

func createTmpCert(t *testing.T) string {
	tmpCertFile, err := os.CreateTemp("", "migrate_test_cert")
	if err != nil {
		t.Fatal("Failed to create temp cert file:", err)
	}
	t.Cleanup(func() {
		if err := os.Remove(tmpCertFile.Name()); err != nil {
			t.Log("Failed to cleanup temp cert file:", err)
		}
	})

	r := rand.New(rand.NewSource(0))
	pub, priv, err := ed25519.GenerateKey(r)
	if err != nil {
		t.Fatal("Failed to generate ed25519 key for temp cert file:", err)
	}
	tmpl := x509.Certificate{
		SerialNumber: big.NewInt(0),
	}
	derBytes, err := x509.CreateCertificate(r, &tmpl, &tmpl, pub, priv)
	if err != nil {
		t.Fatal("Failed to generate temp cert file:", err)
	}
	if err := pem.Encode(tmpCertFile, &pem.Block{Type: "CERTIFICATE", Bytes: derBytes}); err != nil {
		t.Fatal("Failed to encode ")
	}
	if err := tmpCertFile.Close(); err != nil {
		t.Fatal("Failed to close temp cert file:", err)
	}
	return tmpCertFile.Name()
}

func TestURLToMySQLConfig(t *testing.T) {
	tmpCertFilename := createTmpCert(t)
	tmpCertFilenameEscaped := url.PathEscape(tmpCertFilename)

	testcases := []struct {
		name        string
		urlStr      string
		expectedDSN string // empty string signifies that an error is expected
	}{
		{name: "no user/password", urlStr: "mysql://tcp(127.0.0.1:3306)/myDB?multiStatements=true",
			expectedDSN: "tcp(127.0.0.1:3306)/myDB?multiStatements=true"},
		{name: "only user", urlStr: "mysql://username@tcp(127.0.0.1:3306)/myDB?multiStatements=true",
			expectedDSN: "username@tcp(127.0.0.1:3306)/myDB?multiStatements=true"},
		{name: "only user - with encoded :",
			urlStr:      "mysql://username%3A@tcp(127.0.0.1:3306)/myDB?multiStatements=true",
			expectedDSN: "username:@tcp(127.0.0.1:3306)/myDB?multiStatements=true"},
		{name: "only user - with encoded @",
			urlStr:      "mysql://username%40@tcp(127.0.0.1:3306)/myDB?multiStatements=true",
			expectedDSN: "username@@tcp(127.0.0.1:3306)/myDB?multiStatements=true"},
		{name: "user/password", urlStr: "mysql://username:password@tcp(127.0.0.1:3306)/myDB?multiStatements=true",
			expectedDSN: "username:password@tcp(127.0.0.1:3306)/myDB?multiStatements=true"},
		// Not supported yet: https://github.com/go-sql-driver/mysql/issues/591
		// {name: "user/password - user with encoded :",
		// 	urlStr:      "mysql://username%3A:password@tcp(127.0.0.1:3306)/myDB?multiStatements=true",
		// 	expectedDSN: "username::password@tcp(127.0.0.1:3306)/myDB?multiStatements=true"},
		{name: "user/password - user with encoded @",
			urlStr:      "mysql://username%40:password@tcp(127.0.0.1:3306)/myDB?multiStatements=true",
			expectedDSN: "username@:password@tcp(127.0.0.1:3306)/myDB?multiStatements=true"},
		{name: "user/password - password with encoded :",
			urlStr:      "mysql://username:password%3A@tcp(127.0.0.1:3306)/myDB?multiStatements=true",
			expectedDSN: "username:password:@tcp(127.0.0.1:3306)/myDB?multiStatements=true"},
		{name: "user/password - password with encoded @",
			urlStr:      "mysql://username:password%40@tcp(127.0.0.1:3306)/myDB?multiStatements=true",
			expectedDSN: "username:password@@tcp(127.0.0.1:3306)/myDB?multiStatements=true"},
		{name: "custom tls",
			urlStr:      "mysql://username:password@tcp(127.0.0.1:3306)/myDB?multiStatements=true&tls=custom&x-tls-ca=" + tmpCertFilenameEscaped,
			expectedDSN: "username:password@tcp(127.0.0.1:3306)/myDB?multiStatements=true&tls=custom&x-tls-ca=" + tmpCertFilenameEscaped},
	}
	for _, tc := range testcases {
		t.Run(tc.name, func(t *testing.T) {
			config, err := urlToMySQLConfig(tc.urlStr)
			if err != nil {
				t.Fatal("Failed to parse url string:", tc.urlStr, "error:", err)
			}
			dsn := config.FormatDSN()
			if dsn != tc.expectedDSN {
				t.Error("Got unexpected DSN:", dsn, "!=", tc.expectedDSN)
			}
		})
	}
}
```

## File: `database/mysql/README.md`
```markdown
# MySQL

`mysql://user:password@tcp(host:port)/dbname?query`

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table |
| `x-no-lock` | `NoLock` | Set to `true` to skip `GET_LOCK`/`RELEASE_LOCK` statements. Useful for [multi-master MySQL flavors](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/features/pxc-strict-mode.html#explicit-table-locking). Only run migrations from one host when this is enabled. |
| `x-statement-timeout` | `StatementTimeout` | Abort any statement that takes more than the specified number of milliseconds, functionally similar to [Server-side SELECT statement timeouts](https://dev.mysql.com/blog-archive/server-side-select-statement-timeouts/) but enforced by the client. Available for all versions of MySQL, not just >=5.7. | 
| `dbname` | `DatabaseName` | The name of the database to connect to |
| `user` | | The user to sign in as |
| `password` | | The user's password | 
| `host` | | The host to connect to. |
| `port` | | The port to bind to. |
| `tls`  | | TLS / SSL encrypted connection parameter; see [go-sql-driver](https://github.com/go-sql-driver/mysql#tls). Use any name (e.g. `migrate`) if you want to use a custom TLS config (`x-tls-` queries). |
| `x-tls-ca` | | The location of the CA (certificate authority) file. |
| `x-tls-cert` | | The location of the client certificate file. Must be used with `x-tls-key`. |
| `x-tls-key` | | The location of the private key file. Must be used with `x-tls-cert`. |
| `x-tls-insecure-skip-verify` | | Whether or not to use SSL (true\|false) | 

## Use with existing client

If you use the MySQL driver with existing database client, you must create the client with parameter `multiStatements=true`:

```go
package main

import (
    "database/sql"
    
    _ "github.com/go-sql-driver/mysql"
    "github.com/golang-migrate/migrate/v4"
    "github.com/golang-migrate/migrate/v4/database/mysql"
    _ "github.com/golang-migrate/migrate/v4/source/file"
)

func main() {
    db, _ := sql.Open("mysql", "user:password@tcp(host:port)/dbname?multiStatements=true")
    driver, _ := mysql.WithInstance(db, &mysql.Config{})
    m, _ := migrate.NewWithDatabaseInstance(
        "file:///migrations",
        "mysql", 
        driver,
    )
    
    m.Steps(2)
}
```

## Upgrading from v1

1. Write down the current migration version from schema_migrations
1. `DROP TABLE schema_migrations`
2. Wrap your existing migrations in transactions ([BEGIN/COMMIT](https://dev.mysql.com/doc/refman/5.7/en/commit.html)) if you use multiple statements within one migration.
3. Download and install the latest migrate version.
4. Force the current migration version with `migrate force <current_version>`.
```

## File: `database/mysql/examples/migrations/1_init.down.sql`
```sql
DROP TABLE IF EXISTS test;
```

## File: `database/mysql/examples/migrations/1_init.up.sql`
```sql
CREATE TABLE IF NOT EXISTS test (
  firstname VARCHAR(16)
);
```

## File: `database/neo4j/neo4j.go`
```go
package neo4j

import (
	"bytes"
	"errors"
	"fmt"
	"io"
	neturl "net/url"
	"strconv"
	"sync/atomic"

	"github.com/golang-migrate/migrate/v4/database"
	"github.com/golang-migrate/migrate/v4/database/multistmt"
	"github.com/neo4j/neo4j-go-driver/neo4j"
)

func init() {
	db := Neo4j{}
	database.Register("neo4j", &db)
}

const DefaultMigrationsLabel = "SchemaMigration"

var (
	StatementSeparator           = []byte(";")
	DefaultMultiStatementMaxSize = 10 * 1 << 20 // 10 MB
)

var (
	ErrNilConfig = fmt.Errorf("no config")
)

type Config struct {
	MigrationsLabel       string
	MultiStatement        bool
	MultiStatementMaxSize int
}

type Neo4j struct {
	driver neo4j.Driver
	lock   uint32

	// Open and WithInstance need to guarantee that config is never nil
	config *Config
}

func WithInstance(driver neo4j.Driver, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	nDriver := &Neo4j{
		driver: driver,
		config: config,
	}

	if err := nDriver.ensureVersionConstraint(); err != nil {
		return nil, err
	}

	return nDriver, nil
}

func (n *Neo4j) Open(url string) (database.Driver, error) {
	uri, err := neturl.Parse(url)
	if err != nil {
		return nil, err
	}
	password, _ := uri.User.Password()
	authToken := neo4j.BasicAuth(uri.User.Username(), password, "")
	uri.User = nil
	uri.Scheme = "bolt"
	msQuery := uri.Query().Get("x-multi-statement")

	// Whether to turn on/off TLS encryption.
	tlsEncrypted := uri.Query().Get("x-tls-encrypted")
	multi := false
	encrypted := false
	if msQuery != "" {
		multi, err = strconv.ParseBool(uri.Query().Get("x-multi-statement"))
		if err != nil {
			return nil, err
		}
	}

	if tlsEncrypted != "" {
		encrypted, err = strconv.ParseBool(tlsEncrypted)
		if err != nil {
			return nil, err
		}
	}

	multiStatementMaxSize := DefaultMultiStatementMaxSize
	if s := uri.Query().Get("x-multi-statement-max-size"); s != "" {
		multiStatementMaxSize, err = strconv.Atoi(s)
		if err != nil {
			return nil, err
		}
	}

	uri.RawQuery = ""

	driver, err := neo4j.NewDriver(uri.String(), authToken, func(config *neo4j.Config) {
		config.Encrypted = encrypted
	})
	if err != nil {
		return nil, err
	}

	return WithInstance(driver, &Config{
		MigrationsLabel:       DefaultMigrationsLabel,
		MultiStatement:        multi,
		MultiStatementMaxSize: multiStatementMaxSize,
	})
}

func (n *Neo4j) Close() error {
	return n.driver.Close()
}

// local locking in order to pass tests, Neo doesn't support database locking
func (n *Neo4j) Lock() error {
	if !atomic.CompareAndSwapUint32(&n.lock, 0, 1) {
		return database.ErrLocked
	}

	return nil
}

func (n *Neo4j) Unlock() error {
	if !atomic.CompareAndSwapUint32(&n.lock, 1, 0) {
		return database.ErrNotLocked
	}
	return nil
}

func (n *Neo4j) Run(migration io.Reader) (err error) {
	session, err := n.driver.Session(neo4j.AccessModeWrite)
	if err != nil {
		return err
	}
	defer func() {
		if cerr := session.Close(); cerr != nil {
			err = errors.Join(err, cerr)
		}
	}()

	if n.config.MultiStatement {
		_, err = session.WriteTransaction(func(transaction neo4j.Transaction) (interface{}, error) {
			var stmtRunErr error
			if err := multistmt.Parse(migration, StatementSeparator, n.config.MultiStatementMaxSize, func(stmt []byte) bool {
				trimStmt := bytes.TrimSpace(stmt)
				if len(trimStmt) == 0 {
					return true
				}
				trimStmt = bytes.TrimSuffix(trimStmt, StatementSeparator)
				if len(trimStmt) == 0 {
					return true
				}

				result, err := transaction.Run(string(trimStmt), nil)
				if _, err := neo4j.Collect(result, err); err != nil {
					stmtRunErr = err
					return false
				}
				return true
			}); err != nil {
				return nil, err
			}
			return nil, stmtRunErr
		})
		return err
	}

	body, err := io.ReadAll(migration)
	if err != nil {
		return err
	}

	_, err = neo4j.Collect(session.Run(string(body[:]), nil))
	return err
}

func (n *Neo4j) SetVersion(version int, dirty bool) (err error) {
	session, err := n.driver.Session(neo4j.AccessModeWrite)
	if err != nil {
		return err
	}
	defer func() {
		if cerr := session.Close(); cerr != nil {
			err = errors.Join(err, cerr)
		}
	}()

	query := fmt.Sprintf("MERGE (sm:%s {version: $version}) SET sm.dirty = $dirty, sm.ts = datetime()",
		n.config.MigrationsLabel)
	_, err = neo4j.Collect(session.Run(query, map[string]interface{}{"version": version, "dirty": dirty}))
	if err != nil {
		return err
	}
	return nil
}

type MigrationRecord struct {
	Version int
	Dirty   bool
}

func (n *Neo4j) Version() (version int, dirty bool, err error) {
	session, err := n.driver.Session(neo4j.AccessModeRead)
	if err != nil {
		return database.NilVersion, false, err
	}
	defer func() {
		if cerr := session.Close(); cerr != nil {
			err = errors.Join(err, cerr)
		}
	}()

	query := fmt.Sprintf(`MATCH (sm:%s) RETURN sm.version AS version, sm.dirty AS dirty
ORDER BY COALESCE(sm.ts, datetime({year: 0})) DESC, sm.version DESC LIMIT 1`,
		n.config.MigrationsLabel)
	result, err := session.ReadTransaction(func(transaction neo4j.Transaction) (interface{}, error) {
		result, err := transaction.Run(query, nil)
		if err != nil {
			return nil, err
		}
		if result.Next() {
			record := result.Record()
			mr := MigrationRecord{}
			versionResult, ok := record.Get("version")
			if !ok {
				mr.Version = database.NilVersion
			} else {
				mr.Version = int(versionResult.(int64))
			}

			dirtyResult, ok := record.Get("dirty")
			if ok {
				mr.Dirty = dirtyResult.(bool)
			}

			return mr, nil
		}
		return nil, result.Err()
	})
	if err != nil {
		return database.NilVersion, false, err
	}
	if result == nil {
		return database.NilVersion, false, err
	}
	mr := result.(MigrationRecord)
	return mr.Version, mr.Dirty, err
}

func (n *Neo4j) Drop() (err error) {
	session, err := n.driver.Session(neo4j.AccessModeWrite)
	if err != nil {
		return err
	}
	defer func() {
		if cerr := session.Close(); cerr != nil {
			err = errors.Join(err, cerr)
		}
	}()

	if _, err := neo4j.Collect(session.Run("MATCH (n) DETACH DELETE n", nil)); err != nil {
		return err
	}
	return nil
}

func (n *Neo4j) ensureVersionConstraint() (err error) {
	session, err := n.driver.Session(neo4j.AccessModeWrite)
	if err != nil {
		return err
	}
	defer func() {
		if cerr := session.Close(); cerr != nil {
			err = errors.Join(err, cerr)
		}
	}()

	/**
	Get constraint and check to avoid error duplicate
	using db.labels() to support Neo4j 3 and 4.
	Neo4J 3 doesn't support db.constraints() YIELD name
	*/
	res, err := neo4j.Collect(session.Run(fmt.Sprintf("CALL db.labels() YIELD label WHERE label=\"%s\" RETURN label", n.config.MigrationsLabel), nil))
	if err != nil {
		return err
	}
	if len(res) == 1 {
		return nil
	}

	query := fmt.Sprintf("CREATE CONSTRAINT ON (a:%s) ASSERT a.version IS UNIQUE", n.config.MigrationsLabel)
	if _, err := neo4j.Collect(session.Run(query, nil)); err != nil {
		return err
	}
	return nil
}
```

## File: `database/neo4j/neo4j_test.go`
```go
package neo4j

import (
	"bytes"
	"context"
	"fmt"
	"log"
	"testing"

	"github.com/dhui/dktest"
	"github.com/neo4j/neo4j-go-driver/neo4j"

	"github.com/golang-migrate/migrate/v4"
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

var (
	opts = dktest.Options{PortRequired: true, ReadyFunc: isReady,
		Env: map[string]string{"NEO4J_AUTH": "neo4j/migratetest", "NEO4J_ACCEPT_LICENSE_AGREEMENT": "yes"}}
	specs = []dktesting.ContainerSpec{
		{ImageName: "neo4j:4.0", Options: opts},
		{ImageName: "neo4j:4.0-enterprise", Options: opts},
		{ImageName: "neo4j:3.5", Options: opts},
		{ImageName: "neo4j:3.5-enterprise", Options: opts},
	}
)

func neoConnectionString(host, port string) string {
	return fmt.Sprintf("bolt://neo4j:migratetest@%s:%s", host, port)
}

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	ip, port, err := c.Port(7687)
	if err != nil {
		return false
	}

	driver, err := neo4j.NewDriver(
		neoConnectionString(ip, port),
		neo4j.BasicAuth("neo4j", "migratetest", ""),
		func(config *neo4j.Config) {
			config.Encrypted = false
		})
	if err != nil {
		return false
	}
	defer func() {
		if err := driver.Close(); err != nil {
			log.Println("close error:", err)
		}
	}()
	session, err := driver.Session(neo4j.AccessModeRead)
	if err != nil {
		return false
	}
	result, err := session.Run("RETURN 1", nil)
	if err != nil {
		return false
	} else if result.Err() != nil {
		return false
	}

	return true
}

func Test(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(7687)
		if err != nil {
			t.Fatal(err)
		}

		n := &Neo4j{}
		d, err := n.Open(neoConnectionString(ip, port))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		dt.Test(t, d, []byte("MATCH (a) RETURN a"))
	})
}

func TestMigrate(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(7687)
		if err != nil {
			t.Fatal(err)
		}

		n := &Neo4j{}
		neoUrl := neoConnectionString(ip, port) + "/?x-multi-statement=true"
		d, err := n.Open(neoUrl)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "neo4j", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}

func TestMalformed(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(7687)
		if err != nil {
			t.Fatal(err)
		}

		n := &Neo4j{}
		d, err := n.Open(neoConnectionString(ip, port))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		migration := bytes.NewReader([]byte("CREATE (a {qid: 1) RETURN a"))
		if err := d.Run(migration); err == nil {
			t.Fatal("expected failure for malformed migration")
		}
	})
}
```

## File: `database/neo4j/README.md`
```markdown
# neo4j
The Neo4j driver (bolt) does not natively support executing multiple statements in a single query. To allow for multiple statements in a single migration, you can use the `x-multi-statement` param. 
This mode splits the migration text into separately-executed statements by a semi-colon `;`. Thus `x-multi-statement` cannot be used when a statement in the migration contains a string with a semi-colon.
The queries **should** run in a single transaction, so partial migrations should not be a concern, but this is untested.


`neo4j://user:password@host:port/`

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-multi-statement` | `MultiStatement` | Enable multiple statements to be ran in a single migration (See note above) |
| `user` | Contained within `AuthConfig` | The user to sign in as |
| `password` | Contained within `AuthConfig` | The user's password |
| `host` | | The host to connect to. Values that start with / are for unix domain sockets. (default is localhost) |
| `port` | | The port to bind to. (default is 7687) |
|  | `MigrationsLabel` | Name of the migrations node label |

## Supported versions

Only Neo4j v3.5+ is [supported](https://github.com/neo4j/neo4j-go-driver/issues/64#issuecomment-625133600)
```

## File: `database/neo4j/TUTORIAL.md`
```markdown
## Create migrations
Let's create nodes called `Users`:
```
migrate create -ext cypher -dir db/migrations -seq create_user_nodes
```
If there were no errors, we should have two files available under `db/migrations` folder:
- 000001_create_user_nodes.down.cypher
- 000001_create_user_nodes.up.cypher

Note the `cypher` extension that we provided.

In the `.up.cypher` file let's create the table:
```
CREATE (u1:User {name: "Peter"})
CREATE (u2:User {name: "Paul"})
CREATE (u3:User {name: "Mary"})
```
And in the `.down.sql` let's delete it:
```
MATCH (u:User) WHERE u.name IN ["Peter", "Paul", "Mary"] DELETE u
```
Ideally your migrations should be idempotent. You can read more about idempotency in [getting started](../corp/docs/usage_guides/getting_started.md#create-migrations)

## Run migrations
```
migrate -database ${NEO4J_URL} -path db/migrations up
```
Let's check if the table was created properly by running `bin/cypher-shell -u neo4j -p password`, then `neo4j> MATCH (u:User)`
The output you are supposed to see:
```
+-----------------------------------------------------------------+
| u                                                               |
+-----------------------------------------------------------------+
| (:User {name: "Peter")                                          |
| (:User {name: "Paul")                                           |
| (:User {name: "Mary")                                           |
+-----------------------------------------------------------------+
```
Great! Now let's check if running reverse migration also works:
```
migrate -database ${NEO4J_URL} -path db/migrations down
```
Make sure to check if your database changed as expected in this case as well.

## Database transactions

To show database transactions usage, let's create another set of migrations by running:
```
migrate create -ext cypher -dir db/migrations -seq add_mood_to_users
```
Again, it should create for us two migrations files:
- 000002_add_mood_to_users.down.cypher
- 000002_add_mood_to_users.up.cypher

In Neo4j, when we want our queries to be done in a transaction, we need to wrap it with `:BEGIN` and `:COMMIT` commands.
Migration up:
```
:BEGIN

MATCH (u:User)
SET u.mood = "Cheery"

:COMMIT
```
Migration down:
```
:BEGIN

MATCH (u:User)
SET u.mood = null

:COMMIT
```

## Optional: Run migrations within your Go app
Here is a very simple app running migrations for the above configuration:
```
import (
	"log"

	"github.com/golang-migrate/migrate/v4"
	_ "github.com/golang-migrate/migrate/v4/database/neo4j"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

func main() {
	m, err := migrate.New(
		"file://db/migrations",
		"neo4j://neo4j:password@localhost:7687/")
	if err != nil {
		log.Fatal(err)
	}
	if err := m.Up(); err != nil {
		log.Fatal(err)
	}
}
```
```

## File: `database/neo4j/examples/migrations/1578421040_create_movies_constraint.down.cypher`
```
DROP CONSTRAINT ON (m:Movie) ASSERT m.Name IS UNIQUE
```

## File: `database/neo4j/examples/migrations/1578421040_create_movies_constraint.up.cypher`
```
CREATE CONSTRAINT ON (m:Movie) ASSERT m.Name IS UNIQUE
```

## File: `database/neo4j/examples/migrations/1578421725_create_movies.down.cypher`
```
MATCH (m:Movie)
DELETE m
```

## File: `database/neo4j/examples/migrations/1578421725_create_movies.up.cypher`
```
CREATE (:Movie {name: "Footloose"})
CREATE (:Movie {name: "Ghost"})
```

## File: `database/neo4j/examples/migrations/1578421726_multistatement_test.up.cypher`
```
CREATE (:Movie {name: "Hollow Man"});
CREATE (:Movie {name: "Mystic River"});
;;;
```

## File: `database/pgx/pgx.go`
```go
//go:build go1.9

package pgx

import (
	"context"
	"database/sql"
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"regexp"
	"strconv"
	"strings"
	"sync/atomic"
	"time"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	"github.com/golang-migrate/migrate/v4/database/multistmt"
	"github.com/jackc/pgconn"
	"github.com/jackc/pgerrcode"
	_ "github.com/jackc/pgx/v4/stdlib"
	"github.com/lib/pq"
)

const (
	LockStrategyAdvisory = "advisory"
	LockStrategyTable    = "table"
)

func init() {
	db := Postgres{}
	database.Register("pgx", &db)
	database.Register("pgx4", &db)
}

var (
	multiStmtDelimiter = []byte(";")

	DefaultMigrationsTable       = "schema_migrations"
	DefaultMultiStatementMaxSize = 10 * 1 << 20 // 10 MB
	DefaultLockTable             = "schema_lock"
	DefaultLockStrategy          = LockStrategyAdvisory
)

var (
	ErrNilConfig      = fmt.Errorf("no config")
	ErrNoDatabaseName = fmt.Errorf("no database name")
	ErrNoSchema       = fmt.Errorf("no schema")
	ErrDatabaseDirty  = fmt.Errorf("database is dirty")
)

type Config struct {
	MigrationsTable       string
	DatabaseName          string
	SchemaName            string
	LockTable             string
	LockStrategy          string
	migrationsSchemaName  string
	migrationsTableName   string
	StatementTimeout      time.Duration
	MigrationsTableQuoted bool
	MultiStatementEnabled bool
	MultiStatementMaxSize int
}

type Postgres struct {
	// Locking and unlocking need to use the same connection
	conn     *sql.Conn
	db       *sql.DB
	isLocked atomic.Bool

	// Open and WithInstance need to guarantee that config is never nil
	config *Config
}

func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	if config.DatabaseName == "" {
		query := `SELECT CURRENT_DATABASE()`
		var databaseName string
		if err := instance.QueryRow(query).Scan(&databaseName); err != nil {
			return nil, &database.Error{OrigErr: err, Query: []byte(query)}
		}

		if len(databaseName) == 0 {
			return nil, ErrNoDatabaseName
		}

		config.DatabaseName = databaseName
	}

	if config.SchemaName == "" {
		query := `SELECT CURRENT_SCHEMA()`
		var schemaName string
		if err := instance.QueryRow(query).Scan(&schemaName); err != nil {
			return nil, &database.Error{OrigErr: err, Query: []byte(query)}
		}

		if len(schemaName) == 0 {
			return nil, ErrNoSchema
		}

		config.SchemaName = schemaName
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	if len(config.LockTable) == 0 {
		config.LockTable = DefaultLockTable
	}

	if len(config.LockStrategy) == 0 {
		config.LockStrategy = DefaultLockStrategy
	}

	config.migrationsSchemaName = config.SchemaName
	config.migrationsTableName = config.MigrationsTable
	if config.MigrationsTableQuoted {
		re := regexp.MustCompile(`"(.*?)"`)
		result := re.FindAllStringSubmatch(config.MigrationsTable, -1)
		config.migrationsTableName = result[len(result)-1][1]
		if len(result) == 2 {
			config.migrationsSchemaName = result[0][1]
		} else if len(result) > 2 {
			return nil, fmt.Errorf("\"%s\" MigrationsTable contains too many dot characters", config.MigrationsTable)
		}
	}

	conn, err := instance.Conn(context.Background())

	if err != nil {
		return nil, err
	}

	px := &Postgres{
		conn:   conn,
		db:     instance,
		config: config,
	}

	if err := px.ensureLockTable(); err != nil {
		return nil, err
	}

	if err := px.ensureVersionTable(); err != nil {
		return nil, err
	}

	return px, nil
}

func (p *Postgres) Open(url string) (database.Driver, error) {
	purl, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}

	// Driver is registered as pgx, but connection string must use postgres schema
	// when making actual connection
	// i.e. pgx://user:password@host:port/db => postgres://user:password@host:port/db
	purl.Scheme = "postgres"

	db, err := sql.Open("pgx/v4", migrate.FilterCustomQuery(purl).String())
	if err != nil {
		return nil, err
	}

	migrationsTable := purl.Query().Get("x-migrations-table")
	migrationsTableQuoted := false
	if s := purl.Query().Get("x-migrations-table-quoted"); len(s) > 0 {
		migrationsTableQuoted, err = strconv.ParseBool(s)
		if err != nil {
			return nil, fmt.Errorf("unable to parse option x-migrations-table-quoted: %w", err)
		}
	}
	if (len(migrationsTable) > 0) && (migrationsTableQuoted) && ((migrationsTable[0] != '"') || (migrationsTable[len(migrationsTable)-1] != '"')) {
		return nil, fmt.Errorf("x-migrations-table must be quoted (for instance '\"migrate\".\"schema_migrations\"') when x-migrations-table-quoted is enabled, current value is: %s", migrationsTable)
	}

	statementTimeoutString := purl.Query().Get("x-statement-timeout")
	statementTimeout := 0
	if statementTimeoutString != "" {
		statementTimeout, err = strconv.Atoi(statementTimeoutString)
		if err != nil {
			return nil, err
		}
	}

	multiStatementMaxSize := DefaultMultiStatementMaxSize
	if s := purl.Query().Get("x-multi-statement-max-size"); len(s) > 0 {
		multiStatementMaxSize, err = strconv.Atoi(s)
		if err != nil {
			return nil, err
		}
		if multiStatementMaxSize <= 0 {
			multiStatementMaxSize = DefaultMultiStatementMaxSize
		}
	}

	multiStatementEnabled := false
	if s := purl.Query().Get("x-multi-statement"); len(s) > 0 {
		multiStatementEnabled, err = strconv.ParseBool(s)
		if err != nil {
			return nil, fmt.Errorf("unable to parse option x-multi-statement: %w", err)
		}
	}

	lockStrategy := purl.Query().Get("x-lock-strategy")
	lockTable := purl.Query().Get("x-lock-table")

	px, err := WithInstance(db, &Config{
		DatabaseName:          purl.Path,
		MigrationsTable:       migrationsTable,
		MigrationsTableQuoted: migrationsTableQuoted,
		StatementTimeout:      time.Duration(statementTimeout) * time.Millisecond,
		MultiStatementEnabled: multiStatementEnabled,
		MultiStatementMaxSize: multiStatementMaxSize,
		LockStrategy:          lockStrategy,
		LockTable:             lockTable,
	})

	if err != nil {
		return nil, err
	}

	return px, nil
}

func (p *Postgres) Close() error {
	connErr := p.conn.Close()
	dbErr := p.db.Close()
	if connErr != nil || dbErr != nil {
		return fmt.Errorf("conn: %v, db: %v", connErr, dbErr)
	}
	return nil
}

func (p *Postgres) Lock() error {
	return database.CasRestoreOnErr(&p.isLocked, false, true, database.ErrLocked, func() error {
		switch p.config.LockStrategy {
		case LockStrategyAdvisory:
			return p.applyAdvisoryLock()
		case LockStrategyTable:
			return p.applyTableLock()
		default:
			return fmt.Errorf("unknown lock strategy \"%s\"", p.config.LockStrategy)
		}
	})
}

func (p *Postgres) Unlock() error {
	return database.CasRestoreOnErr(&p.isLocked, true, false, database.ErrNotLocked, func() error {
		switch p.config.LockStrategy {
		case LockStrategyAdvisory:
			return p.releaseAdvisoryLock()
		case LockStrategyTable:
			return p.releaseTableLock()
		default:
			return fmt.Errorf("unknown lock strategy \"%s\"", p.config.LockStrategy)
		}
	})
}

// https://www.postgresql.org/docs/9.6/static/explicit-locking.html#ADVISORY-LOCKS
func (p *Postgres) applyAdvisoryLock() error {
	aid, err := database.GenerateAdvisoryLockId(p.config.DatabaseName, p.config.migrationsSchemaName, p.config.migrationsTableName)
	if err != nil {
		return err
	}

	// This will wait indefinitely until the lock can be acquired.
	query := `SELECT pg_advisory_lock($1)`
	if _, err := p.conn.ExecContext(context.Background(), query, aid); err != nil {
		return &database.Error{OrigErr: err, Err: "try lock failed", Query: []byte(query)}
	}
	return nil
}

func (p *Postgres) applyTableLock() error {
	tx, err := p.conn.BeginTx(context.Background(), &sql.TxOptions{})
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}
	defer func() {
		errRollback := tx.Rollback()
		if errRollback != nil {
			err = errors.Join(err, errRollback)
		}
	}()

	aid, err := database.GenerateAdvisoryLockId(p.config.DatabaseName)
	if err != nil {
		return err
	}

	query := "SELECT * FROM " + pq.QuoteIdentifier(p.config.LockTable) + " WHERE lock_id = $1"
	rows, err := tx.Query(query, aid)
	if err != nil {
		return database.Error{OrigErr: err, Err: "failed to fetch migration lock", Query: []byte(query)}
	}

	defer func() {
		if errClose := rows.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	// If row exists at all, lock is present
	locked := rows.Next()
	if locked {
		return database.ErrLocked
	}

	query = "INSERT INTO " + pq.QuoteIdentifier(p.config.LockTable) + " (lock_id) VALUES ($1)"
	if _, err := tx.Exec(query, aid); err != nil {
		return database.Error{OrigErr: err, Err: "failed to set migration lock", Query: []byte(query)}
	}

	return tx.Commit()
}

func (p *Postgres) releaseAdvisoryLock() error {
	aid, err := database.GenerateAdvisoryLockId(p.config.DatabaseName, p.config.migrationsSchemaName, p.config.migrationsTableName)
	if err != nil {
		return err
	}

	query := `SELECT pg_advisory_unlock($1)`
	if _, err := p.conn.ExecContext(context.Background(), query, aid); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}

func (p *Postgres) releaseTableLock() error {
	aid, err := database.GenerateAdvisoryLockId(p.config.DatabaseName)
	if err != nil {
		return err
	}

	query := "DELETE FROM " + pq.QuoteIdentifier(p.config.LockTable) + " WHERE lock_id = $1"
	if _, err := p.db.Exec(query, aid); err != nil {
		return database.Error{OrigErr: err, Err: "failed to release migration lock", Query: []byte(query)}
	}

	return nil
}

func (p *Postgres) Run(migration io.Reader) error {
	if p.config.MultiStatementEnabled {
		var err error
		if e := multistmt.Parse(migration, multiStmtDelimiter, p.config.MultiStatementMaxSize, func(m []byte) bool {
			if err = p.runStatement(m); err != nil {
				return false
			}
			return true
		}); e != nil {
			return e
		}
		return err
	}
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}
	return p.runStatement(migr)
}

func (p *Postgres) runStatement(statement []byte) error {
	ctx := context.Background()
	if p.config.StatementTimeout != 0 {
		var cancel context.CancelFunc
		ctx, cancel = context.WithTimeout(ctx, p.config.StatementTimeout)
		defer cancel()
	}
	query := string(statement)
	if strings.TrimSpace(query) == "" {
		return nil
	}
	if _, err := p.conn.ExecContext(ctx, query); err != nil {

		if pgErr, ok := err.(*pgconn.PgError); ok {
			var line uint
			var col uint
			var lineColOK bool
			line, col, lineColOK = computeLineFromPos(query, int(pgErr.Position))
			message := fmt.Sprintf("migration failed: %s", pgErr.Message)
			if lineColOK {
				message = fmt.Sprintf("%s (column %d)", message, col)
			}
			if pgErr.Detail != "" {
				message = fmt.Sprintf("%s, %s", message, pgErr.Detail)
			}
			return database.Error{OrigErr: err, Err: message, Query: statement, Line: line}
		}
		return database.Error{OrigErr: err, Err: "migration failed", Query: statement}
	}
	return nil
}

func computeLineFromPos(s string, pos int) (line uint, col uint, ok bool) {
	// replace crlf with lf
	s = strings.ReplaceAll(s, "\r\n", "\n")
	// pg docs: pos uses index 1 for the first character, and positions are measured in characters not bytes
	runes := []rune(s)
	if pos > len(runes) {
		return 0, 0, false
	}
	sel := runes[:pos]
	line = uint(runesCount(sel, newLine) + 1)
	col = uint(pos - 1 - runesLastIndex(sel, newLine))
	return line, col, true
}

const newLine = '\n'

func runesCount(input []rune, target rune) int {
	var count int
	for _, r := range input {
		if r == target {
			count++
		}
	}
	return count
}

func runesLastIndex(input []rune, target rune) int {
	for i := len(input) - 1; i >= 0; i-- {
		if input[i] == target {
			return i
		}
	}
	return -1
}

func (p *Postgres) SetVersion(version int, dirty bool) error {
	tx, err := p.conn.BeginTx(context.Background(), &sql.TxOptions{})
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}

	query := `TRUNCATE ` + quoteIdentifier(p.config.migrationsSchemaName) + `.` + quoteIdentifier(p.config.migrationsTableName)
	if _, err := tx.Exec(query); err != nil {
		if errRollback := tx.Rollback(); errRollback != nil {
			err = errors.Join(err, errRollback)
		}
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	// Also re-write the schema version for nil dirty versions to prevent
	// empty schema version for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330
	if version >= 0 || (version == database.NilVersion && dirty) {
		query = `INSERT INTO ` + quoteIdentifier(p.config.migrationsSchemaName) + `.` + quoteIdentifier(p.config.migrationsTableName) + ` (version, dirty) VALUES ($1, $2)`
		if _, err := tx.Exec(query, version, dirty); err != nil {
			if errRollback := tx.Rollback(); errRollback != nil {
				err = errors.Join(err, errRollback)
			}
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}

	return nil
}

func (p *Postgres) Version() (version int, dirty bool, err error) {
	query := `SELECT version, dirty FROM ` + quoteIdentifier(p.config.migrationsSchemaName) + `.` + quoteIdentifier(p.config.migrationsTableName) + ` LIMIT 1`
	err = p.conn.QueryRowContext(context.Background(), query).Scan(&version, &dirty)
	switch {
	case err == sql.ErrNoRows:
		return database.NilVersion, false, nil

	case err != nil:
		if e, ok := err.(*pgconn.PgError); ok {
			if e.SQLState() == pgerrcode.UndefinedTable {
				return database.NilVersion, false, nil
			}
		}
		return 0, false, &database.Error{OrigErr: err, Query: []byte(query)}

	default:
		return version, dirty, nil
	}
}

func (p *Postgres) Drop() (err error) {
	// select all tables in current schema
	query := `SELECT table_name FROM information_schema.tables WHERE table_schema=(SELECT current_schema()) AND table_type='BASE TABLE'`
	tables, err := p.conn.QueryContext(context.Background(), query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	// delete one table after another
	tableNames := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}

		// do not drop lock table
		if tableName == p.config.LockTable && p.config.LockStrategy == LockStrategyTable {
			continue
		}

		if len(tableName) > 0 {
			tableNames = append(tableNames, tableName)
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if len(tableNames) > 0 {
		// delete one by one ...
		for _, t := range tableNames {
			query = `DROP TABLE IF EXISTS ` + quoteIdentifier(t) + ` CASCADE`
			if _, err := p.conn.ExecContext(context.Background(), query); err != nil {
				return &database.Error{OrigErr: err, Query: []byte(query)}
			}
		}
	}

	return nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the Postgres type.
func (p *Postgres) ensureVersionTable() (err error) {
	if err = p.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := p.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	// This block checks whether the `MigrationsTable` already exists. This is useful because it allows read only postgres
	// users to also check the current version of the schema. Previously, even if `MigrationsTable` existed, the
	// `CREATE TABLE IF NOT EXISTS...` query would fail because the user does not have the CREATE permission.
	// Taken from https://github.com/mattes/migrate/blob/master/database/postgres/postgres.go#L258
	query := `SELECT COUNT(1) FROM information_schema.tables WHERE table_schema = $1 AND table_name = $2 LIMIT 1`
	row := p.conn.QueryRowContext(context.Background(), query, p.config.migrationsSchemaName, p.config.migrationsTableName)

	var count int
	err = row.Scan(&count)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if count == 1 {
		return nil
	}

	query = `CREATE TABLE IF NOT EXISTS ` + quoteIdentifier(p.config.migrationsSchemaName) + `.` + quoteIdentifier(p.config.migrationsTableName) + ` (version bigint not null primary key, dirty boolean not null)`
	if _, err = p.conn.ExecContext(context.Background(), query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}

func (p *Postgres) ensureLockTable() error {
	if p.config.LockStrategy != LockStrategyTable {
		return nil
	}

	var count int
	query := `SELECT COUNT(1) FROM information_schema.tables WHERE table_name = $1 AND table_schema = (SELECT current_schema()) LIMIT 1`
	if err := p.db.QueryRow(query, p.config.LockTable).Scan(&count); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	if count == 1 {
		return nil
	}

	query = `CREATE TABLE ` + pq.QuoteIdentifier(p.config.LockTable) + ` (lock_id BIGINT NOT NULL PRIMARY KEY)`
	if _, err := p.db.Exec(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}

// Copied from lib/pq implementation: https://github.com/lib/pq/blob/v1.9.0/conn.go#L1611
func quoteIdentifier(name string) string {
	end := strings.IndexRune(name, 0)
	if end > -1 {
		name = name[:end]
	}
	return `"` + strings.ReplaceAll(name, `"`, `""`) + `"`
}
```

## File: `database/pgx/pgx_test.go`
```go
package pgx

// error codes https://github.com/jackc/pgerrcode/blob/master/errcode.go

import (
	"context"
	"database/sql"
	sqldriver "database/sql/driver"
	"errors"
	"fmt"
	"io"
	"log"
	"strconv"
	"strings"
	"sync"
	"testing"

	"github.com/dhui/dktest"
	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"

	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

const (
	pgPassword = "postgres"
)

var (
	opts = dktest.Options{
		Env:          map[string]string{"POSTGRES_PASSWORD": pgPassword},
		PortRequired: true, ReadyFunc: isReady}
	// Supported versions: https://www.postgresql.org/support/versioning/
	specs = []dktesting.ContainerSpec{
		{ImageName: "postgres:13", Options: opts},
		{ImageName: "postgres:14", Options: opts},
		{ImageName: "postgres:15", Options: opts},
		{ImageName: "postgres:16", Options: opts},
		{ImageName: "postgres:17", Options: opts},
	}
)

func pgConnectionString(host, port string, options ...string) string {
	options = append(options, "sslmode=disable")
	return fmt.Sprintf("postgres://postgres:%s@%s:%s/postgres?%s", pgPassword, host, port, strings.Join(options, "&"))
}

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	ip, port, err := c.FirstPort()
	if err != nil {
		return false
	}

	db, err := sql.Open("pgx", pgConnectionString(ip, port))
	if err != nil {
		return false
	}
	defer func() {
		if err := db.Close(); err != nil {
			log.Println("close error:", err)
		}
	}()
	if err = db.PingContext(ctx); err != nil {
		switch err {
		case sqldriver.ErrBadConn, io.EOF:
			return false
		default:
			log.Println(err)
		}
		return false
	}

	return true
}

func mustRun(t *testing.T, d database.Driver, statements []string) {
	for _, statement := range statements {
		if err := d.Run(strings.NewReader(statement)); err != nil {
			t.Fatal(err)
		}
	}
}

func Test(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		dt.Test(t, d, []byte("SELECT 1"))
	})
}

func TestMigrate(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "pgx", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}

func TestMigrateLockTable(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port, "x-lock-strategy=table", "x-lock-table=lock_table")
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "pgx", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}

func TestMultipleStatements(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		if err := d.Run(strings.NewReader("CREATE TABLE foo (foo text); CREATE TABLE bar (bar text);")); err != nil {
			t.Fatalf("expected err to be nil, got %v", err)
		}

		// make sure second table exists
		var exists bool
		if err := d.(*Postgres).conn.QueryRowContext(context.Background(), "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'bar' AND table_schema = (SELECT current_schema()))").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table bar to exist")
		}
	})
}

func TestMultipleStatementsInMultiStatementMode(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port, "x-multi-statement=true")
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		if err := d.Run(strings.NewReader("CREATE TABLE foo (foo text); CREATE INDEX CONCURRENTLY idx_foo ON foo (foo);")); err != nil {
			t.Fatalf("expected err to be nil, got %v", err)
		}

		// make sure created index exists
		var exists bool
		if err := d.(*Postgres).conn.QueryRowContext(context.Background(), "SELECT EXISTS (SELECT 1 FROM pg_indexes WHERE schemaname = (SELECT current_schema()) AND indexname = 'idx_foo')").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table bar to exist")
		}
	})
}

func TestErrorParsing(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		wantErr := `migration failed: syntax error at or near "TABLEE" (column 37) in line 1: CREATE TABLE foo ` +
			`(foo text); CREATE TABLEE bar (bar text); (details: ERROR: syntax error at or near "TABLEE" (SQLSTATE 42601))`
		if err := d.Run(strings.NewReader("CREATE TABLE foo (foo text); CREATE TABLEE bar (bar text);")); err == nil {
			t.Fatal("expected err but got nil")
		} else if err.Error() != wantErr {
			t.Fatalf("expected '%s' but got '%s'", wantErr, err.Error())
		}
	})
}

func TestFilterCustomQuery(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port, "x-custom=foobar")
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
	})
}

func TestWithSchema(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		// create foobar schema
		if err := d.Run(strings.NewReader("CREATE SCHEMA foobar AUTHORIZATION postgres")); err != nil {
			t.Fatal(err)
		}
		if err := d.SetVersion(1, false); err != nil {
			t.Fatal(err)
		}

		// re-connect using that schema
		d2, err := p.Open(pgConnectionString(ip, port, "search_path=foobar"))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d2.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		version, _, err := d2.Version()
		if err != nil {
			t.Fatal(err)
		}
		if version != database.NilVersion {
			t.Fatal("expected NilVersion")
		}

		// now update version and compare
		if err := d2.SetVersion(2, false); err != nil {
			t.Fatal(err)
		}
		version, _, err = d2.Version()
		if err != nil {
			t.Fatal(err)
		}
		if version != 2 {
			t.Fatal("expected version 2")
		}

		// meanwhile, the public schema still has the other version
		version, _, err = d.Version()
		if err != nil {
			t.Fatal(err)
		}
		if version != 1 {
			t.Fatal("expected version 2")
		}
	})
}

func TestMigrationTableOption(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, _ := p.Open(addr)
		defer func() {
			if err := d.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		// create migrate schema
		if err := d.Run(strings.NewReader("CREATE SCHEMA migrate AUTHORIZATION postgres")); err != nil {
			t.Fatal(err)
		}

		// bad unquoted x-migrations-table parameter
		wantErr := "x-migrations-table must be quoted (for instance '\"migrate\".\"schema_migrations\"') when x-migrations-table-quoted is enabled, current value is: migrate.schema_migrations"
		d, err = p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=migrate.schema_migrations&x-migrations-table-quoted=1",
			pgPassword, ip, port))
		if (err != nil) && (err.Error() != wantErr) {
			t.Fatalf("expected '%s' but got '%s'", wantErr, err.Error())
		}

		// too many quoted x-migrations-table parameters
		wantErr = "\"\"migrate\".\"schema_migrations\".\"toomany\"\" MigrationsTable contains too many dot characters"
		d, err = p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=\"migrate\".\"schema_migrations\".\"toomany\"&x-migrations-table-quoted=1",
			pgPassword, ip, port))
		if (err != nil) && (err.Error() != wantErr) {
			t.Fatalf("expected '%s' but got '%s'", wantErr, err.Error())
		}

		// good quoted x-migrations-table parameter
		d, err = p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=\"migrate\".\"schema_migrations\"&x-migrations-table-quoted=1",
			pgPassword, ip, port))
		if err != nil {
			t.Fatal(err)
		}

		// make sure migrate.schema_migrations table exists
		var exists bool
		if err := d.(*Postgres).conn.QueryRowContext(context.Background(), "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'schema_migrations' AND table_schema = 'migrate')").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table migrate.schema_migrations to exist")
		}

		d, err = p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=migrate.schema_migrations",
			pgPassword, ip, port))
		if err != nil {
			t.Fatal(err)
		}
		if err := d.(*Postgres).conn.QueryRowContext(context.Background(), "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'migrate.schema_migrations' AND table_schema = (SELECT current_schema()))").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table 'migrate.schema_migrations' to exist")
		}

	})
}

func TestFailToCreateTableWithoutPermissions(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)

		// Check that opening the postgres connection returns NilVersion
		p := &Postgres{}

		d, err := p.Open(addr)

		if err != nil {
			t.Fatal(err)
		}

		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		// create user who is not the owner. Although we're concatenating strings in an sql statement it should be fine
		// since this is a test environment and we're not expecting to the pgPassword to be malicious
		mustRun(t, d, []string{
			"CREATE USER not_owner WITH ENCRYPTED PASSWORD '" + pgPassword + "'",
			"CREATE SCHEMA barfoo AUTHORIZATION postgres",
			"GRANT USAGE ON SCHEMA barfoo TO not_owner",
			"REVOKE CREATE ON SCHEMA barfoo FROM PUBLIC",
			"REVOKE CREATE ON SCHEMA barfoo FROM not_owner",
		})

		// re-connect using that schema
		d2, err := p.Open(fmt.Sprintf("postgres://not_owner:%s@%v:%v/postgres?sslmode=disable&search_path=barfoo",
			pgPassword, ip, port))

		defer func() {
			if d2 == nil {
				return
			}
			if err := d2.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		var e *database.Error
		if !errors.As(err, &e) || err == nil {
			t.Fatal("Unexpected error, want permission denied error. Got: ", err)
		}

		if !strings.Contains(e.OrigErr.Error(), "permission denied for schema barfoo") {
			t.Fatal(e)
		}

		// re-connect using that x-migrations-table and x-migrations-table-quoted
		d2, err = p.Open(fmt.Sprintf("postgres://not_owner:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=\"barfoo\".\"schema_migrations\"&x-migrations-table-quoted=1",
			pgPassword, ip, port))

		if !errors.As(err, &e) || err == nil {
			t.Fatal("Unexpected error, want permission denied error. Got: ", err)
		}

		if !strings.Contains(e.OrigErr.Error(), "permission denied for schema barfoo") {
			t.Fatal(e)
		}
	})
}

func TestCheckBeforeCreateTable(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)

		// Check that opening the postgres connection returns NilVersion
		p := &Postgres{}

		d, err := p.Open(addr)

		if err != nil {
			t.Fatal(err)
		}

		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		// create user who is not the owner. Although we're concatenating strings in an sql statement it should be fine
		// since this is a test environment and we're not expecting to the pgPassword to be malicious
		mustRun(t, d, []string{
			"CREATE USER not_owner WITH ENCRYPTED PASSWORD '" + pgPassword + "'",
			"CREATE SCHEMA barfoo AUTHORIZATION postgres",
			"GRANT USAGE ON SCHEMA barfoo TO not_owner",
			"GRANT CREATE ON SCHEMA barfoo TO not_owner",
		})

		// re-connect using that schema
		d2, err := p.Open(fmt.Sprintf("postgres://not_owner:%s@%v:%v/postgres?sslmode=disable&search_path=barfoo",
			pgPassword, ip, port))

		if err != nil {
			t.Fatal(err)
		}

		if err := d2.Close(); err != nil {
			t.Fatal(err)
		}

		// revoke privileges
		mustRun(t, d, []string{
			"REVOKE CREATE ON SCHEMA barfoo FROM PUBLIC",
			"REVOKE CREATE ON SCHEMA barfoo FROM not_owner",
		})

		// re-connect using that schema
		d3, err := p.Open(fmt.Sprintf("postgres://not_owner:%s@%v:%v/postgres?sslmode=disable&search_path=barfoo",
			pgPassword, ip, port))

		if err != nil {
			t.Fatal(err)
		}

		version, _, err := d3.Version()

		if err != nil {
			t.Fatal(err)
		}

		if version != database.NilVersion {
			t.Fatal("Unexpected version, want database.NilVersion. Got: ", version)
		}

		defer func() {
			if err := d3.Close(); err != nil {
				t.Fatal(err)
			}
		}()
	})
}

func TestParallelSchema(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		// create foo and bar schemas
		if err := d.Run(strings.NewReader("CREATE SCHEMA foo AUTHORIZATION postgres")); err != nil {
			t.Fatal(err)
		}
		if err := d.Run(strings.NewReader("CREATE SCHEMA bar AUTHORIZATION postgres")); err != nil {
			t.Fatal(err)
		}

		// re-connect using that schemas
		dfoo, err := p.Open(pgConnectionString(ip, port, "search_path=foo"))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := dfoo.Close(); err != nil {
				t.Error(err)
			}
		}()

		dbar, err := p.Open(pgConnectionString(ip, port, "search_path=bar"))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := dbar.Close(); err != nil {
				t.Error(err)
			}
		}()

		if err := dfoo.Lock(); err != nil {
			t.Fatal(err)
		}

		if err := dbar.Lock(); err != nil {
			t.Fatal(err)
		}

		if err := dbar.Unlock(); err != nil {
			t.Fatal(err)
		}

		if err := dfoo.Unlock(); err != nil {
			t.Fatal(err)
		}
	})
}

func TestPostgres_Lock(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}

		dt.Test(t, d, []byte("SELECT 1"))

		ps := d.(*Postgres)

		err = ps.Lock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Unlock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Lock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Unlock()
		if err != nil {
			t.Fatal(err)
		}
	})
}

func TestWithInstance_Concurrent(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		// The number of concurrent processes running WithInstance
		const concurrency = 30

		// We can instantiate a single database handle because it is
		// actually a connection pool, and so, each of the below go
		// routines will have a high probability of using a separate
		// connection, which is something we want to exercise.
		db, err := sql.Open("pgx", pgConnectionString(ip, port))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := db.Close(); err != nil {
				t.Error(err)
			}
		}()

		db.SetMaxIdleConns(concurrency)
		db.SetMaxOpenConns(concurrency)

		var wg sync.WaitGroup
		defer wg.Wait()

		wg.Add(concurrency)
		for i := 0; i < concurrency; i++ {
			go func(i int) {
				defer wg.Done()
				_, err := WithInstance(db, &Config{})
				if err != nil {
					t.Errorf("process %d error: %s", i, err)
				}
			}(i)
		}
	})
}
func Test_computeLineFromPos(t *testing.T) {
	testcases := []struct {
		pos      int
		wantLine uint
		wantCol  uint
		input    string
		wantOk   bool
	}{
		{
			15, 2, 6, "SELECT *\nFROM foo", true, // foo table does not exists
		},
		{
			16, 3, 6, "SELECT *\n\nFROM foo", true, // foo table does not exists, empty line
		},
		{
			25, 3, 7, "SELECT *\nFROM foo\nWHERE x", true, // x column error
		},
		{
			27, 5, 7, "SELECT *\n\nFROM foo\n\nWHERE x", true, // x column error, empty lines
		},
		{
			10, 2, 1, "SELECT *\nFROMM foo", true, // FROMM typo
		},
		{
			11, 3, 1, "SELECT *\n\nFROMM foo", true, // FROMM typo, empty line
		},
		{
			17, 2, 8, "SELECT *\nFROM foo", true, // last character
		},
		{
			18, 0, 0, "SELECT *\nFROM foo", false, // invalid position
		},
	}
	for i, tc := range testcases {
		t.Run("tc"+strconv.Itoa(i), func(t *testing.T) {
			run := func(crlf bool, nonASCII bool) {
				var name string
				if crlf {
					name = "crlf"
				} else {
					name = "lf"
				}
				if nonASCII {
					name += "-nonascii"
				} else {
					name += "-ascii"
				}
				t.Run(name, func(t *testing.T) {
					input := tc.input
					if crlf {
						input = strings.ReplaceAll(input, "\n", "\r\n")
					}
					if nonASCII {
						input = strings.ReplaceAll(input, "FROM", "FRÖM")
					}
					gotLine, gotCol, gotOK := computeLineFromPos(input, tc.pos)

					if tc.wantOk {
						t.Logf("pos %d, want %d:%d, %#v", tc.pos, tc.wantLine, tc.wantCol, input)
					}

					if gotOK != tc.wantOk {
						t.Fatalf("expected ok %v but got %v", tc.wantOk, gotOK)
					}
					if gotLine != tc.wantLine {
						t.Fatalf("expected line %d but got %d", tc.wantLine, gotLine)
					}
					if gotCol != tc.wantCol {
						t.Fatalf("expected col %d but got %d", tc.wantCol, gotCol)
					}
				})
			}
			run(false, false)
			run(true, false)
			run(false, true)
			run(true, true)
		})
	}
}
```

## File: `database/pgx/README.md`
```markdown
# pgx

This package is for [pgx/v4](https://pkg.go.dev/github.com/jackc/pgx/v4). A backend for the newer [pgx/v5](https://pkg.go.dev/github.com/jackc/pgx/v5) is [also available](v5).

`pgx://user:password@host:port/dbname?query`

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table |
| `x-migrations-table-quoted` | `MigrationsTableQuoted` | By default, migrate quotes the migration table for SQL injection safety reasons. This option disable quoting and naively checks that you have quoted the migration table name. e.g. `"my_schema"."schema_migrations"` |
| `x-statement-timeout` | `StatementTimeout` | Abort any statement that takes more than the specified number of milliseconds |
| `x-multi-statement` | `MultiStatementEnabled` | Enable multi-statement execution (default: false) |
| `x-multi-statement-max-size` | `MultiStatementMaxSize` | Maximum size of single statement in bytes (default: 10MB) |
| `x-lock-strategy` | `LockStrategy` | Strategy used for locking during migration (default: advisory) |
| `x-lock-table` | `LockTable` | Name of the table which maintains the migration lock (default: schema_lock) |
| `dbname` | `DatabaseName` | The name of the database to connect to |
| `search_path` | | This variable specifies the order in which schemas are searched when an object is referenced by a simple name with no schema specified. |
| `user` | | The user to sign in as |
| `password` | | The user's password |
| `host` | | The host to connect to. Values that start with / are for unix domain sockets. (default is localhost) |
| `port` | | The port to bind to. (default is 5432) |
| `fallback_application_name` | | An application_name to fall back to if one isn't provided. |
| `connect_timeout` | | Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely. |
| `sslcert` | | Cert file location. The file must contain PEM encoded data. |
| `sslkey` | | Key file location. The file must contain PEM encoded data. |
| `sslrootcert` | | The location of the root certificate file. The file must contain PEM encoded data. |
| `sslmode` | | Whether or not to use SSL (disable\|require\|verify-ca\|verify-full) |


## Upgrading from v1

1. Write down the current migration version from schema_migrations
1. `DROP TABLE schema_migrations`
2. Wrap your existing migrations in transactions ([BEGIN/COMMIT](https://www.postgresql.org/docs/current/static/transaction-iso.html)) if you use multiple statements within one migration.
3. Download and install the latest migrate version.
4. Force the current migration version with `migrate force <current_version>`.

## Multi-statement mode

In PostgreSQL running multiple SQL statements in one `Exec` executes them inside a transaction. Sometimes this
behavior is not desirable because some statements can be only run outside of transaction (e.g.
`CREATE INDEX CONCURRENTLY`). If you want to use `CREATE INDEX CONCURRENTLY` without activating multi-statement mode
you have to put such statements in a separate migration files.
```

## File: `database/pgx/examples/migrations/1085649617_create_users_table.down.sql`
```sql
DROP TABLE IF EXISTS users;
```

## File: `database/pgx/examples/migrations/1085649617_create_users_table.up.sql`
```sql
CREATE TABLE users (
  user_id integer unique,
  name    varchar(40),
  email   varchar(40)
);
```

## File: `database/pgx/examples/migrations/1185749658_add_city_to_users.down.sql`
```sql
ALTER TABLE users DROP COLUMN IF EXISTS city;
```

## File: `database/pgx/examples/migrations/1185749658_add_city_to_users.up.sql`
```sql
ALTER TABLE users ADD COLUMN city varchar(100);


```

## File: `database/pgx/examples/migrations/1285849751_add_index_on_user_emails.down.sql`
```sql
DROP INDEX IF EXISTS users_email_index;
```

## File: `database/pgx/examples/migrations/1285849751_add_index_on_user_emails.up.sql`
```sql
CREATE UNIQUE INDEX CONCURRENTLY users_email_index ON users (email);

-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/pgx/examples/migrations/1385949617_create_books_table.down.sql`
```sql
DROP TABLE IF EXISTS books;
```

## File: `database/pgx/examples/migrations/1385949617_create_books_table.up.sql`
```sql
CREATE TABLE books (
  user_id integer,
  name    varchar(40),
  author  varchar(40)
);
```

## File: `database/pgx/examples/migrations/1485949617_create_movies_table.down.sql`
```sql
DROP TABLE IF EXISTS movies;
```

## File: `database/pgx/examples/migrations/1485949617_create_movies_table.up.sql`
```sql
CREATE TABLE movies (
  user_id   integer,
  name      varchar(40),
  director  varchar(40)
);
```

## File: `database/pgx/examples/migrations/1585849751_just_a_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/pgx/examples/migrations/1685849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/pgx/examples/migrations/1785849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/pgx/examples/migrations/1885849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/pgx/v5/pgx.go`
```go
//go:build go1.9

package pgx

import (
	"context"
	"database/sql"
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"regexp"
	"strconv"
	"strings"
	"sync/atomic"
	"time"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	"github.com/golang-migrate/migrate/v4/database/multistmt"
	"github.com/jackc/pgerrcode"
	"github.com/jackc/pgx/v5/pgconn"
	_ "github.com/jackc/pgx/v5/stdlib"
)

func init() {
	db := Postgres{}
	database.Register("pgx5", &db)
}

var (
	multiStmtDelimiter = []byte(";")

	DefaultMigrationsTable       = "schema_migrations"
	DefaultMultiStatementMaxSize = 10 * 1 << 20 // 10 MB
)

var (
	ErrNilConfig      = fmt.Errorf("no config")
	ErrNoDatabaseName = fmt.Errorf("no database name")
	ErrNoSchema       = fmt.Errorf("no schema")
)

type Config struct {
	MigrationsTable       string
	DatabaseName          string
	SchemaName            string
	migrationsSchemaName  string
	migrationsTableName   string
	StatementTimeout      time.Duration
	MigrationsTableQuoted bool
	MultiStatementEnabled bool
	MultiStatementMaxSize int
}

type Postgres struct {
	// Locking and unlocking need to use the same connection
	conn     *sql.Conn
	db       *sql.DB
	isLocked atomic.Bool

	// Open and WithInstance need to guarantee that config is never nil
	config *Config
}

func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	if config.DatabaseName == "" {
		query := `SELECT CURRENT_DATABASE()`
		var databaseName string
		if err := instance.QueryRow(query).Scan(&databaseName); err != nil {
			return nil, &database.Error{OrigErr: err, Query: []byte(query)}
		}

		if len(databaseName) == 0 {
			return nil, ErrNoDatabaseName
		}

		config.DatabaseName = databaseName
	}

	if config.SchemaName == "" {
		query := `SELECT CURRENT_SCHEMA()`
		var schemaName string
		if err := instance.QueryRow(query).Scan(&schemaName); err != nil {
			return nil, &database.Error{OrigErr: err, Query: []byte(query)}
		}

		if len(schemaName) == 0 {
			return nil, ErrNoSchema
		}

		config.SchemaName = schemaName
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	config.migrationsSchemaName = config.SchemaName
	config.migrationsTableName = config.MigrationsTable
	if config.MigrationsTableQuoted {
		re := regexp.MustCompile(`"(.*?)"`)
		result := re.FindAllStringSubmatch(config.MigrationsTable, -1)
		config.migrationsTableName = result[len(result)-1][1]
		if len(result) == 2 {
			config.migrationsSchemaName = result[0][1]
		} else if len(result) > 2 {
			return nil, fmt.Errorf("\"%s\" MigrationsTable contains too many dot characters", config.MigrationsTable)
		}
	}

	conn, err := instance.Conn(context.Background())

	if err != nil {
		return nil, err
	}

	px := &Postgres{
		conn:   conn,
		db:     instance,
		config: config,
	}

	if err := px.ensureVersionTable(); err != nil {
		return nil, err
	}

	return px, nil
}

func (p *Postgres) Open(url string) (database.Driver, error) {
	purl, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}

	// Driver is registered as pgx, but connection string must use postgres schema
	// when making actual connection
	// i.e. pgx://user:password@host:port/db => postgres://user:password@host:port/db
	purl.Scheme = "postgres"

	db, err := sql.Open("pgx/v5", migrate.FilterCustomQuery(purl).String())
	if err != nil {
		return nil, err
	}

	migrationsTable := purl.Query().Get("x-migrations-table")
	migrationsTableQuoted := false
	if s := purl.Query().Get("x-migrations-table-quoted"); len(s) > 0 {
		migrationsTableQuoted, err = strconv.ParseBool(s)
		if err != nil {
			return nil, fmt.Errorf("unable to parse option x-migrations-table-quoted: %w", err)
		}
	}
	if (len(migrationsTable) > 0) && (migrationsTableQuoted) && ((migrationsTable[0] != '"') || (migrationsTable[len(migrationsTable)-1] != '"')) {
		return nil, fmt.Errorf("x-migrations-table must be quoted (for instance '\"migrate\".\"schema_migrations\"') when x-migrations-table-quoted is enabled, current value is: %s", migrationsTable)
	}

	statementTimeoutString := purl.Query().Get("x-statement-timeout")
	statementTimeout := 0
	if statementTimeoutString != "" {
		statementTimeout, err = strconv.Atoi(statementTimeoutString)
		if err != nil {
			return nil, err
		}
	}

	multiStatementMaxSize := DefaultMultiStatementMaxSize
	if s := purl.Query().Get("x-multi-statement-max-size"); len(s) > 0 {
		multiStatementMaxSize, err = strconv.Atoi(s)
		if err != nil {
			return nil, err
		}
		if multiStatementMaxSize <= 0 {
			multiStatementMaxSize = DefaultMultiStatementMaxSize
		}
	}

	multiStatementEnabled := false
	if s := purl.Query().Get("x-multi-statement"); len(s) > 0 {
		multiStatementEnabled, err = strconv.ParseBool(s)
		if err != nil {
			return nil, fmt.Errorf("unable to parse option x-multi-statement: %w", err)
		}
	}

	px, err := WithInstance(db, &Config{
		DatabaseName:          purl.Path,
		MigrationsTable:       migrationsTable,
		MigrationsTableQuoted: migrationsTableQuoted,
		StatementTimeout:      time.Duration(statementTimeout) * time.Millisecond,
		MultiStatementEnabled: multiStatementEnabled,
		MultiStatementMaxSize: multiStatementMaxSize,
	})

	if err != nil {
		return nil, err
	}

	return px, nil
}

func (p *Postgres) Close() error {
	connErr := p.conn.Close()
	dbErr := p.db.Close()
	if connErr != nil || dbErr != nil {
		return fmt.Errorf("conn: %v, db: %v", connErr, dbErr)
	}
	return nil
}

// https://www.postgresql.org/docs/9.6/static/explicit-locking.html#ADVISORY-LOCKS
func (p *Postgres) Lock() error {
	return database.CasRestoreOnErr(&p.isLocked, false, true, database.ErrLocked, func() error {
		aid, err := database.GenerateAdvisoryLockId(p.config.DatabaseName, p.config.migrationsSchemaName, p.config.migrationsTableName)
		if err != nil {
			return err
		}

		// This will wait indefinitely until the lock can be acquired.
		query := `SELECT pg_advisory_lock($1)`
		if _, err := p.conn.ExecContext(context.Background(), query, aid); err != nil {
			return &database.Error{OrigErr: err, Err: "try lock failed", Query: []byte(query)}
		}
		return nil
	})
}

func (p *Postgres) Unlock() error {
	return database.CasRestoreOnErr(&p.isLocked, true, false, database.ErrNotLocked, func() error {
		aid, err := database.GenerateAdvisoryLockId(p.config.DatabaseName, p.config.migrationsSchemaName, p.config.migrationsTableName)
		if err != nil {
			return err
		}

		query := `SELECT pg_advisory_unlock($1)`
		if _, err := p.conn.ExecContext(context.Background(), query, aid); err != nil {
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
		return nil
	})
}

func (p *Postgres) Run(migration io.Reader) error {
	if p.config.MultiStatementEnabled {
		var err error
		if e := multistmt.Parse(migration, multiStmtDelimiter, p.config.MultiStatementMaxSize, func(m []byte) bool {
			if err = p.runStatement(m); err != nil {
				return false
			}
			return true
		}); e != nil {
			return e
		}
		return err
	}
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}
	return p.runStatement(migr)
}

func (p *Postgres) runStatement(statement []byte) error {
	ctx := context.Background()
	if p.config.StatementTimeout != 0 {
		var cancel context.CancelFunc
		ctx, cancel = context.WithTimeout(ctx, p.config.StatementTimeout)
		defer cancel()
	}
	query := string(statement)
	if strings.TrimSpace(query) == "" {
		return nil
	}
	if _, err := p.conn.ExecContext(ctx, query); err != nil {

		if pgErr, ok := err.(*pgconn.PgError); ok {
			var line uint
			var col uint
			var lineColOK bool
			line, col, lineColOK = computeLineFromPos(query, int(pgErr.Position))
			message := fmt.Sprintf("migration failed: %s", pgErr.Message)
			if lineColOK {
				message = fmt.Sprintf("%s (column %d)", message, col)
			}
			if pgErr.Detail != "" {
				message = fmt.Sprintf("%s, %s", message, pgErr.Detail)
			}
			return database.Error{OrigErr: err, Err: message, Query: statement, Line: line}
		}
		return database.Error{OrigErr: err, Err: "migration failed", Query: statement}
	}
	return nil
}

func computeLineFromPos(s string, pos int) (line uint, col uint, ok bool) {
	// replace crlf with lf
	s = strings.ReplaceAll(s, "\r\n", "\n")
	// pg docs: pos uses index 1 for the first character, and positions are measured in characters not bytes
	runes := []rune(s)
	if pos > len(runes) {
		return 0, 0, false
	}
	sel := runes[:pos]
	line = uint(runesCount(sel, newLine) + 1)
	col = uint(pos - 1 - runesLastIndex(sel, newLine))
	return line, col, true
}

const newLine = '\n'

func runesCount(input []rune, target rune) int {
	var count int
	for _, r := range input {
		if r == target {
			count++
		}
	}
	return count
}

func runesLastIndex(input []rune, target rune) int {
	for i := len(input) - 1; i >= 0; i-- {
		if input[i] == target {
			return i
		}
	}
	return -1
}

func (p *Postgres) SetVersion(version int, dirty bool) error {
	tx, err := p.conn.BeginTx(context.Background(), &sql.TxOptions{})
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}

	query := `TRUNCATE ` + quoteIdentifier(p.config.migrationsSchemaName) + `.` + quoteIdentifier(p.config.migrationsTableName)
	if _, err := tx.Exec(query); err != nil {
		if errRollback := tx.Rollback(); errRollback != nil {
			err = errors.Join(err, errRollback)
		}
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	// Also re-write the schema version for nil dirty versions to prevent
	// empty schema version for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330
	if version >= 0 || (version == database.NilVersion && dirty) {
		query = `INSERT INTO ` + quoteIdentifier(p.config.migrationsSchemaName) + `.` + quoteIdentifier(p.config.migrationsTableName) + ` (version, dirty) VALUES ($1, $2)`
		if _, err := tx.Exec(query, version, dirty); err != nil {
			if errRollback := tx.Rollback(); errRollback != nil {
				err = errors.Join(err, errRollback)
			}
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}

	return nil
}

func (p *Postgres) Version() (version int, dirty bool, err error) {
	query := `SELECT version, dirty FROM ` + quoteIdentifier(p.config.migrationsSchemaName) + `.` + quoteIdentifier(p.config.migrationsTableName) + ` LIMIT 1`
	err = p.conn.QueryRowContext(context.Background(), query).Scan(&version, &dirty)
	switch {
	case err == sql.ErrNoRows:
		return database.NilVersion, false, nil

	case err != nil:
		if e, ok := err.(*pgconn.PgError); ok {
			if e.SQLState() == pgerrcode.UndefinedTable {
				return database.NilVersion, false, nil
			}
		}
		return 0, false, &database.Error{OrigErr: err, Query: []byte(query)}

	default:
		return version, dirty, nil
	}
}

func (p *Postgres) Drop() (err error) {
	// select all tables in current schema
	query := `SELECT table_name FROM information_schema.tables WHERE table_schema=(SELECT current_schema()) AND table_type='BASE TABLE'`
	tables, err := p.conn.QueryContext(context.Background(), query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	// delete one table after another
	tableNames := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}
		if len(tableName) > 0 {
			tableNames = append(tableNames, tableName)
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if len(tableNames) > 0 {
		// delete one by one ...
		for _, t := range tableNames {
			query = `DROP TABLE IF EXISTS ` + quoteIdentifier(t) + ` CASCADE`
			if _, err := p.conn.ExecContext(context.Background(), query); err != nil {
				return &database.Error{OrigErr: err, Query: []byte(query)}
			}
		}
	}

	return nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the Postgres type.
func (p *Postgres) ensureVersionTable() (err error) {
	if err = p.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := p.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	// This block checks whether the `MigrationsTable` already exists. This is useful because it allows read only postgres
	// users to also check the current version of the schema. Previously, even if `MigrationsTable` existed, the
	// `CREATE TABLE IF NOT EXISTS...` query would fail because the user does not have the CREATE permission.
	// Taken from https://github.com/mattes/migrate/blob/master/database/postgres/postgres.go#L258
	query := `SELECT COUNT(1) FROM information_schema.tables WHERE table_schema = $1 AND table_name = $2 LIMIT 1`
	row := p.conn.QueryRowContext(context.Background(), query, p.config.migrationsSchemaName, p.config.migrationsTableName)

	var count int
	err = row.Scan(&count)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if count == 1 {
		return nil
	}

	query = `CREATE TABLE IF NOT EXISTS ` + quoteIdentifier(p.config.migrationsSchemaName) + `.` + quoteIdentifier(p.config.migrationsTableName) + ` (version bigint not null primary key, dirty boolean not null)`
	if _, err = p.conn.ExecContext(context.Background(), query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}

// Copied from lib/pq implementation: https://github.com/lib/pq/blob/v1.9.0/conn.go#L1611
func quoteIdentifier(name string) string {
	end := strings.IndexRune(name, 0)
	if end > -1 {
		name = name[:end]
	}
	return `"` + strings.ReplaceAll(name, `"`, `""`) + `"`
}
```

## File: `database/pgx/v5/pgx_test.go`
```go
package pgx

// error codes https://github.com/jackc/pgerrcode/blob/master/errcode.go

import (
	"context"
	"database/sql"
	sqldriver "database/sql/driver"
	"errors"
	"fmt"
	"io"
	"log"
	"strconv"
	"strings"
	"sync"
	"testing"

	"github.com/golang-migrate/migrate/v4"

	"github.com/dhui/dktest"

	"github.com/golang-migrate/migrate/v4/database"
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

const (
	pgPassword = "postgres"
)

var (
	opts = dktest.Options{
		Env:          map[string]string{"POSTGRES_PASSWORD": pgPassword},
		PortRequired: true, ReadyFunc: isReady}
	// Supported versions: https://www.postgresql.org/support/versioning/
	specs = []dktesting.ContainerSpec{
		{ImageName: "postgres:13", Options: opts},
		{ImageName: "postgres:14", Options: opts},
		{ImageName: "postgres:15", Options: opts},
		{ImageName: "postgres:16", Options: opts},
		{ImageName: "postgres:17", Options: opts},
	}
)

func pgConnectionString(host, port string, options ...string) string {
	options = append(options, "sslmode=disable")
	return fmt.Sprintf("postgres://postgres:%s@%s:%s/postgres?%s", pgPassword, host, port, strings.Join(options, "&"))
}

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	ip, port, err := c.FirstPort()
	if err != nil {
		return false
	}

	db, err := sql.Open("pgx", pgConnectionString(ip, port))
	if err != nil {
		return false
	}
	defer func() {
		if err := db.Close(); err != nil {
			log.Println("close error:", err)
		}
	}()
	if err = db.PingContext(ctx); err != nil {
		switch err {
		case sqldriver.ErrBadConn, io.EOF:
			return false
		default:
			log.Println(err)
		}
		return false
	}

	return true
}

func mustRun(t *testing.T, d database.Driver, statements []string) {
	for _, statement := range statements {
		if err := d.Run(strings.NewReader(statement)); err != nil {
			t.Fatal(err)
		}
	}
}

func Test(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		dt.Test(t, d, []byte("SELECT 1"))
	})
}

func TestMigrate(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		m, err := migrate.NewWithDatabaseInstance("file://../examples/migrations", "pgx", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}

func TestMultipleStatements(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		if err := d.Run(strings.NewReader("CREATE TABLE foo (foo text); CREATE TABLE bar (bar text);")); err != nil {
			t.Fatalf("expected err to be nil, got %v", err)
		}

		// make sure second table exists
		var exists bool
		if err := d.(*Postgres).conn.QueryRowContext(context.Background(), "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'bar' AND table_schema = (SELECT current_schema()))").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table bar to exist")
		}
	})
}

func TestMultipleStatementsInMultiStatementMode(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port, "x-multi-statement=true")
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		if err := d.Run(strings.NewReader("CREATE TABLE foo (foo text); CREATE INDEX CONCURRENTLY idx_foo ON foo (foo);")); err != nil {
			t.Fatalf("expected err to be nil, got %v", err)
		}

		// make sure created index exists
		var exists bool
		if err := d.(*Postgres).conn.QueryRowContext(context.Background(), "SELECT EXISTS (SELECT 1 FROM pg_indexes WHERE schemaname = (SELECT current_schema()) AND indexname = 'idx_foo')").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table bar to exist")
		}
	})
}

func TestErrorParsing(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		wantErr := `migration failed: syntax error at or near "TABLEE" (column 37) in line 1: CREATE TABLE foo ` +
			`(foo text); CREATE TABLEE bar (bar text); (details: ERROR: syntax error at or near "TABLEE" (SQLSTATE 42601))`
		if err := d.Run(strings.NewReader("CREATE TABLE foo (foo text); CREATE TABLEE bar (bar text);")); err == nil {
			t.Fatal("expected err but got nil")
		} else if err.Error() != wantErr {
			t.Fatalf("expected '%s' but got '%s'", wantErr, err.Error())
		}
	})
}

func TestFilterCustomQuery(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port, "x-custom=foobar")
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
	})
}

func TestWithSchema(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		// create foobar schema
		if err := d.Run(strings.NewReader("CREATE SCHEMA foobar AUTHORIZATION postgres")); err != nil {
			t.Fatal(err)
		}
		if err := d.SetVersion(1, false); err != nil {
			t.Fatal(err)
		}

		// re-connect using that schema
		d2, err := p.Open(pgConnectionString(ip, port, "search_path=foobar"))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d2.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		version, _, err := d2.Version()
		if err != nil {
			t.Fatal(err)
		}
		if version != database.NilVersion {
			t.Fatal("expected NilVersion")
		}

		// now update version and compare
		if err := d2.SetVersion(2, false); err != nil {
			t.Fatal(err)
		}
		version, _, err = d2.Version()
		if err != nil {
			t.Fatal(err)
		}
		if version != 2 {
			t.Fatal("expected version 2")
		}

		// meanwhile, the public schema still has the other version
		version, _, err = d.Version()
		if err != nil {
			t.Fatal(err)
		}
		if version != 1 {
			t.Fatal("expected version 2")
		}
	})
}

func TestMigrationTableOption(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, _ := p.Open(addr)
		defer func() {
			if err := d.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		// create migrate schema
		if err := d.Run(strings.NewReader("CREATE SCHEMA migrate AUTHORIZATION postgres")); err != nil {
			t.Fatal(err)
		}

		// bad unquoted x-migrations-table parameter
		wantErr := "x-migrations-table must be quoted (for instance '\"migrate\".\"schema_migrations\"') when x-migrations-table-quoted is enabled, current value is: migrate.schema_migrations"
		d, err = p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=migrate.schema_migrations&x-migrations-table-quoted=1",
			pgPassword, ip, port))
		if (err != nil) && (err.Error() != wantErr) {
			t.Fatalf("expected '%s' but got '%s'", wantErr, err.Error())
		}

		// too many quoted x-migrations-table parameters
		wantErr = "\"\"migrate\".\"schema_migrations\".\"toomany\"\" MigrationsTable contains too many dot characters"
		d, err = p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=\"migrate\".\"schema_migrations\".\"toomany\"&x-migrations-table-quoted=1",
			pgPassword, ip, port))
		if (err != nil) && (err.Error() != wantErr) {
			t.Fatalf("expected '%s' but got '%s'", wantErr, err.Error())
		}

		// good quoted x-migrations-table parameter
		d, err = p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=\"migrate\".\"schema_migrations\"&x-migrations-table-quoted=1",
			pgPassword, ip, port))
		if err != nil {
			t.Fatal(err)
		}

		// make sure migrate.schema_migrations table exists
		var exists bool
		if err := d.(*Postgres).conn.QueryRowContext(context.Background(), "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'schema_migrations' AND table_schema = 'migrate')").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table migrate.schema_migrations to exist")
		}

		d, err = p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=migrate.schema_migrations",
			pgPassword, ip, port))
		if err != nil {
			t.Fatal(err)
		}
		if err := d.(*Postgres).conn.QueryRowContext(context.Background(), "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'migrate.schema_migrations' AND table_schema = (SELECT current_schema()))").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table 'migrate.schema_migrations' to exist")
		}

	})
}

func TestFailToCreateTableWithoutPermissions(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)

		// Check that opening the postgres connection returns NilVersion
		p := &Postgres{}

		d, err := p.Open(addr)

		if err != nil {
			t.Fatal(err)
		}

		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		// create user who is not the owner. Although we're concatenating strings in an sql statement it should be fine
		// since this is a test environment and we're not expecting to the pgPassword to be malicious
		mustRun(t, d, []string{
			"CREATE USER not_owner WITH ENCRYPTED PASSWORD '" + pgPassword + "'",
			"CREATE SCHEMA barfoo AUTHORIZATION postgres",
			"GRANT USAGE ON SCHEMA barfoo TO not_owner",
			"REVOKE CREATE ON SCHEMA barfoo FROM PUBLIC",
			"REVOKE CREATE ON SCHEMA barfoo FROM not_owner",
		})

		// re-connect using that schema
		d2, err := p.Open(fmt.Sprintf("postgres://not_owner:%s@%v:%v/postgres?sslmode=disable&search_path=barfoo",
			pgPassword, ip, port))

		defer func() {
			if d2 == nil {
				return
			}
			if err := d2.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		var e *database.Error
		if !errors.As(err, &e) || err == nil {
			t.Fatal("Unexpected error, want permission denied error. Got: ", err)
		}

		if !strings.Contains(e.OrigErr.Error(), "permission denied for schema barfoo") {
			t.Fatal(e)
		}

		// re-connect using that x-migrations-table and x-migrations-table-quoted
		d2, err = p.Open(fmt.Sprintf("postgres://not_owner:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=\"barfoo\".\"schema_migrations\"&x-migrations-table-quoted=1",
			pgPassword, ip, port))

		if !errors.As(err, &e) || err == nil {
			t.Fatal("Unexpected error, want permission denied error. Got: ", err)
		}

		if !strings.Contains(e.OrigErr.Error(), "permission denied for schema barfoo") {
			t.Fatal(e)
		}
	})
}

func TestCheckBeforeCreateTable(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)

		// Check that opening the postgres connection returns NilVersion
		p := &Postgres{}

		d, err := p.Open(addr)

		if err != nil {
			t.Fatal(err)
		}

		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		// create user who is not the owner. Although we're concatenating strings in an sql statement it should be fine
		// since this is a test environment and we're not expecting to the pgPassword to be malicious
		mustRun(t, d, []string{
			"CREATE USER not_owner WITH ENCRYPTED PASSWORD '" + pgPassword + "'",
			"CREATE SCHEMA barfoo AUTHORIZATION postgres",
			"GRANT USAGE ON SCHEMA barfoo TO not_owner",
			"GRANT CREATE ON SCHEMA barfoo TO not_owner",
		})

		// re-connect using that schema
		d2, err := p.Open(fmt.Sprintf("postgres://not_owner:%s@%v:%v/postgres?sslmode=disable&search_path=barfoo",
			pgPassword, ip, port))

		if err != nil {
			t.Fatal(err)
		}

		if err := d2.Close(); err != nil {
			t.Fatal(err)
		}

		// revoke privileges
		mustRun(t, d, []string{
			"REVOKE CREATE ON SCHEMA barfoo FROM PUBLIC",
			"REVOKE CREATE ON SCHEMA barfoo FROM not_owner",
		})

		// re-connect using that schema
		d3, err := p.Open(fmt.Sprintf("postgres://not_owner:%s@%v:%v/postgres?sslmode=disable&search_path=barfoo",
			pgPassword, ip, port))

		if err != nil {
			t.Fatal(err)
		}

		version, _, err := d3.Version()

		if err != nil {
			t.Fatal(err)
		}

		if version != database.NilVersion {
			t.Fatal("Unexpected version, want database.NilVersion. Got: ", version)
		}

		defer func() {
			if err := d3.Close(); err != nil {
				t.Fatal(err)
			}
		}()
	})
}

func TestParallelSchema(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		// create foo and bar schemas
		if err := d.Run(strings.NewReader("CREATE SCHEMA foo AUTHORIZATION postgres")); err != nil {
			t.Fatal(err)
		}
		if err := d.Run(strings.NewReader("CREATE SCHEMA bar AUTHORIZATION postgres")); err != nil {
			t.Fatal(err)
		}

		// re-connect using that schemas
		dfoo, err := p.Open(pgConnectionString(ip, port, "search_path=foo"))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := dfoo.Close(); err != nil {
				t.Error(err)
			}
		}()

		dbar, err := p.Open(pgConnectionString(ip, port, "search_path=bar"))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := dbar.Close(); err != nil {
				t.Error(err)
			}
		}()

		if err := dfoo.Lock(); err != nil {
			t.Fatal(err)
		}

		if err := dbar.Lock(); err != nil {
			t.Fatal(err)
		}

		if err := dbar.Unlock(); err != nil {
			t.Fatal(err)
		}

		if err := dfoo.Unlock(); err != nil {
			t.Fatal(err)
		}
	})
}

func TestPostgres_Lock(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}

		dt.Test(t, d, []byte("SELECT 1"))

		ps := d.(*Postgres)

		err = ps.Lock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Unlock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Lock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Unlock()
		if err != nil {
			t.Fatal(err)
		}
	})
}

func TestWithInstance_Concurrent(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		// The number of concurrent processes running WithInstance
		const concurrency = 30

		// We can instantiate a single database handle because it is
		// actually a connection pool, and so, each of the below go
		// routines will have a high probability of using a separate
		// connection, which is something we want to exercise.
		db, err := sql.Open("pgx", pgConnectionString(ip, port))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := db.Close(); err != nil {
				t.Error(err)
			}
		}()

		db.SetMaxIdleConns(concurrency)
		db.SetMaxOpenConns(concurrency)

		var wg sync.WaitGroup
		defer wg.Wait()

		wg.Add(concurrency)
		for i := 0; i < concurrency; i++ {
			go func(i int) {
				defer wg.Done()
				_, err := WithInstance(db, &Config{})
				if err != nil {
					t.Errorf("process %d error: %s", i, err)
				}
			}(i)
		}
	})
}
func Test_computeLineFromPos(t *testing.T) {
	testcases := []struct {
		pos      int
		wantLine uint
		wantCol  uint
		input    string
		wantOk   bool
	}{
		{
			15, 2, 6, "SELECT *\nFROM foo", true, // foo table does not exists
		},
		{
			16, 3, 6, "SELECT *\n\nFROM foo", true, // foo table does not exists, empty line
		},
		{
			25, 3, 7, "SELECT *\nFROM foo\nWHERE x", true, // x column error
		},
		{
			27, 5, 7, "SELECT *\n\nFROM foo\n\nWHERE x", true, // x column error, empty lines
		},
		{
			10, 2, 1, "SELECT *\nFROMM foo", true, // FROMM typo
		},
		{
			11, 3, 1, "SELECT *\n\nFROMM foo", true, // FROMM typo, empty line
		},
		{
			17, 2, 8, "SELECT *\nFROM foo", true, // last character
		},
		{
			18, 0, 0, "SELECT *\nFROM foo", false, // invalid position
		},
	}
	for i, tc := range testcases {
		t.Run("tc"+strconv.Itoa(i), func(t *testing.T) {
			run := func(crlf bool, nonASCII bool) {
				var name string
				if crlf {
					name = "crlf"
				} else {
					name = "lf"
				}
				if nonASCII {
					name += "-nonascii"
				} else {
					name += "-ascii"
				}
				t.Run(name, func(t *testing.T) {
					input := tc.input
					if crlf {
						input = strings.ReplaceAll(input, "\n", "\r\n")
					}
					if nonASCII {
						input = strings.ReplaceAll(input, "FROM", "FRÖM")
					}
					gotLine, gotCol, gotOK := computeLineFromPos(input, tc.pos)

					if tc.wantOk {
						t.Logf("pos %d, want %d:%d, %#v", tc.pos, tc.wantLine, tc.wantCol, input)
					}

					if gotOK != tc.wantOk {
						t.Fatalf("expected ok %v but got %v", tc.wantOk, gotOK)
					}
					if gotLine != tc.wantLine {
						t.Fatalf("expected line %d but got %d", tc.wantLine, gotLine)
					}
					if gotCol != tc.wantCol {
						t.Fatalf("expected col %d but got %d", tc.wantCol, gotCol)
					}
				})
			}
			run(false, false)
			run(true, false)
			run(false, true)
			run(true, true)
		})
	}
}
```

## File: `database/pgx/v5/README.md`
```markdown
# pgx

This package is for [pgx/v5](https://pkg.go.dev/github.com/jackc/pgx/v5). A backend for the older [pgx/v4](https://pkg.go.dev/github.com/jackc/pgx/v4). is [also available](..).

`pgx5://user:password@host:port/dbname?query`

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table |
| `x-migrations-table-quoted` | `MigrationsTableQuoted` | By default, migrate quotes the migration table for SQL injection safety reasons. This option disable quoting and naively checks that you have quoted the migration table name. e.g. `"my_schema"."schema_migrations"` |
| `x-statement-timeout` | `StatementTimeout` | Abort any statement that takes more than the specified number of milliseconds |
| `x-multi-statement` | `MultiStatementEnabled` | Enable multi-statement execution (default: false) |
| `x-multi-statement-max-size` | `MultiStatementMaxSize` | Maximum size of single statement in bytes (default: 10MB) |
| `dbname` | `DatabaseName` | The name of the database to connect to |
| `search_path` | | This variable specifies the order in which schemas are searched when an object is referenced by a simple name with no schema specified. |
| `user` | | The user to sign in as |
| `password` | | The user's password |
| `host` | | The host to connect to. Values that start with / are for unix domain sockets. (default is localhost) |
| `port` | | The port to bind to. (default is 5432) |
| `fallback_application_name` | | An application_name to fall back to if one isn't provided. |
| `connect_timeout` | | Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely. |
| `sslcert` | | Cert file location. The file must contain PEM encoded data. |
| `sslkey` | | Key file location. The file must contain PEM encoded data. |
| `sslrootcert` | | The location of the root certificate file. The file must contain PEM encoded data. |
| `sslmode` | | Whether or not to use SSL (disable\|require\|verify-ca\|verify-full) |


## Upgrading from v1

1. Write down the current migration version from schema_migrations
1. `DROP TABLE schema_migrations`
2. Wrap your existing migrations in transactions ([BEGIN/COMMIT](https://www.postgresql.org/docs/current/static/transaction-iso.html)) if you use multiple statements within one migration.
3. Download and install the latest migrate version.
4. Force the current migration version with `migrate force <current_version>`.

## Multi-statement mode

In PostgreSQL running multiple SQL statements in one `Exec` executes them inside a transaction. Sometimes this
behavior is not desirable because some statements can be only run outside of transaction (e.g.
`CREATE INDEX CONCURRENTLY`). If you want to use `CREATE INDEX CONCURRENTLY` without activating multi-statement mode
you have to put such statements in a separate migration files.
```

## File: `database/postgres/postgres.go`
```go
//go:build go1.9

package postgres

import (
	"context"
	"database/sql"
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"regexp"
	"strconv"
	"strings"
	"sync/atomic"
	"time"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	"github.com/golang-migrate/migrate/v4/database/multistmt"
	"github.com/lib/pq"
)

func init() {
	db := Postgres{}
	database.Register("postgres", &db)
	database.Register("postgresql", &db)
}

var (
	multiStmtDelimiter = []byte(";")

	DefaultMigrationsTable       = "schema_migrations"
	DefaultMultiStatementMaxSize = 10 * 1 << 20 // 10 MB
)

var (
	ErrNilConfig      = fmt.Errorf("no config")
	ErrNoDatabaseName = fmt.Errorf("no database name")
	ErrNoSchema       = fmt.Errorf("no schema")
	ErrDatabaseDirty  = fmt.Errorf("database is dirty")
)

type Config struct {
	MigrationsTable       string
	MigrationsTableQuoted bool
	MultiStatementEnabled bool
	DatabaseName          string
	SchemaName            string
	migrationsSchemaName  string
	migrationsTableName   string
	StatementTimeout      time.Duration
	MultiStatementMaxSize int
}

type Postgres struct {
	// Locking and unlocking need to use the same connection
	conn     *sql.Conn
	db       *sql.DB
	isLocked atomic.Bool

	// Open and WithInstance need to guarantee that config is never nil
	config *Config
}

func WithConnection(ctx context.Context, conn *sql.Conn, config *Config) (*Postgres, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := conn.PingContext(ctx); err != nil {
		return nil, err
	}

	if config.DatabaseName == "" {
		query := `SELECT CURRENT_DATABASE()`
		var databaseName string
		if err := conn.QueryRowContext(ctx, query).Scan(&databaseName); err != nil {
			return nil, &database.Error{OrigErr: err, Query: []byte(query)}
		}

		if len(databaseName) == 0 {
			return nil, ErrNoDatabaseName
		}

		config.DatabaseName = databaseName
	}

	if config.SchemaName == "" {
		query := `SELECT CURRENT_SCHEMA()`
		var schemaName sql.NullString
		if err := conn.QueryRowContext(ctx, query).Scan(&schemaName); err != nil {
			return nil, &database.Error{OrigErr: err, Query: []byte(query)}
		}

		if !schemaName.Valid {
			return nil, ErrNoSchema
		}

		config.SchemaName = schemaName.String
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	config.migrationsSchemaName = config.SchemaName
	config.migrationsTableName = config.MigrationsTable
	if config.MigrationsTableQuoted {
		re := regexp.MustCompile(`"(.*?)"`)
		result := re.FindAllStringSubmatch(config.MigrationsTable, -1)
		config.migrationsTableName = result[len(result)-1][1]
		if len(result) == 2 {
			config.migrationsSchemaName = result[0][1]
		} else if len(result) > 2 {
			return nil, fmt.Errorf("\"%s\" MigrationsTable contains too many dot characters", config.MigrationsTable)
		}
	}

	px := &Postgres{
		conn:   conn,
		config: config,
	}

	if err := px.ensureVersionTable(); err != nil {
		return nil, err
	}

	return px, nil
}

func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	ctx := context.Background()

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	conn, err := instance.Conn(ctx)
	if err != nil {
		return nil, err
	}

	px, err := WithConnection(ctx, conn, config)
	if err != nil {
		return nil, err
	}
	px.db = instance
	return px, nil
}

func (p *Postgres) Open(url string) (database.Driver, error) {
	purl, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}

	db, err := sql.Open("postgres", migrate.FilterCustomQuery(purl).String())
	if err != nil {
		return nil, err
	}

	migrationsTable := purl.Query().Get("x-migrations-table")
	migrationsTableQuoted := false
	if s := purl.Query().Get("x-migrations-table-quoted"); len(s) > 0 {
		migrationsTableQuoted, err = strconv.ParseBool(s)
		if err != nil {
			return nil, fmt.Errorf("unable to parse option x-migrations-table-quoted: %w", err)
		}
	}
	if (len(migrationsTable) > 0) && (migrationsTableQuoted) && ((migrationsTable[0] != '"') || (migrationsTable[len(migrationsTable)-1] != '"')) {
		return nil, fmt.Errorf("x-migrations-table must be quoted (for instance '\"migrate\".\"schema_migrations\"') when x-migrations-table-quoted is enabled, current value is: %s", migrationsTable)
	}

	statementTimeoutString := purl.Query().Get("x-statement-timeout")
	statementTimeout := 0
	if statementTimeoutString != "" {
		statementTimeout, err = strconv.Atoi(statementTimeoutString)
		if err != nil {
			return nil, err
		}
	}

	multiStatementMaxSize := DefaultMultiStatementMaxSize
	if s := purl.Query().Get("x-multi-statement-max-size"); len(s) > 0 {
		multiStatementMaxSize, err = strconv.Atoi(s)
		if err != nil {
			return nil, err
		}
		if multiStatementMaxSize <= 0 {
			multiStatementMaxSize = DefaultMultiStatementMaxSize
		}
	}

	multiStatementEnabled := false
	if s := purl.Query().Get("x-multi-statement"); len(s) > 0 {
		multiStatementEnabled, err = strconv.ParseBool(s)
		if err != nil {
			return nil, fmt.Errorf("unable to parse option x-multi-statement: %w", err)
		}
	}

	px, err := WithInstance(db, &Config{
		DatabaseName:          purl.Path,
		MigrationsTable:       migrationsTable,
		MigrationsTableQuoted: migrationsTableQuoted,
		StatementTimeout:      time.Duration(statementTimeout) * time.Millisecond,
		MultiStatementEnabled: multiStatementEnabled,
		MultiStatementMaxSize: multiStatementMaxSize,
	})

	if err != nil {
		return nil, err
	}

	return px, nil
}

func (p *Postgres) Close() error {
	connErr := p.conn.Close()
	var dbErr error
	if p.db != nil {
		dbErr = p.db.Close()
	}

	if connErr != nil || dbErr != nil {
		return fmt.Errorf("conn: %v, db: %v", connErr, dbErr)
	}
	return nil
}

// https://www.postgresql.org/docs/9.6/static/explicit-locking.html#ADVISORY-LOCKS
func (p *Postgres) Lock() error {
	return database.CasRestoreOnErr(&p.isLocked, false, true, database.ErrLocked, func() error {
		aid, err := database.GenerateAdvisoryLockId(p.config.DatabaseName, p.config.migrationsSchemaName, p.config.migrationsTableName)
		if err != nil {
			return err
		}

		// This will wait indefinitely until the lock can be acquired.
		query := `SELECT pg_advisory_lock($1)`
		if _, err := p.conn.ExecContext(context.Background(), query, aid); err != nil {
			return &database.Error{OrigErr: err, Err: "try lock failed", Query: []byte(query)}
		}

		return nil
	})
}

func (p *Postgres) Unlock() error {
	return database.CasRestoreOnErr(&p.isLocked, true, false, database.ErrNotLocked, func() error {
		aid, err := database.GenerateAdvisoryLockId(p.config.DatabaseName, p.config.migrationsSchemaName, p.config.migrationsTableName)
		if err != nil {
			return err
		}

		query := `SELECT pg_advisory_unlock($1)`
		if _, err := p.conn.ExecContext(context.Background(), query, aid); err != nil {
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
		return nil
	})
}

func (p *Postgres) Run(migration io.Reader) error {
	if p.config.MultiStatementEnabled {
		var err error
		if e := multistmt.Parse(migration, multiStmtDelimiter, p.config.MultiStatementMaxSize, func(m []byte) bool {
			if err = p.runStatement(m); err != nil {
				return false
			}
			return true
		}); e != nil {
			return e
		}
		return err
	}
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}
	return p.runStatement(migr)
}

func (p *Postgres) runStatement(statement []byte) error {
	ctx := context.Background()
	if p.config.StatementTimeout != 0 {
		var cancel context.CancelFunc
		ctx, cancel = context.WithTimeout(ctx, p.config.StatementTimeout)
		defer cancel()
	}
	query := string(statement)
	if strings.TrimSpace(query) == "" {
		return nil
	}
	if _, err := p.conn.ExecContext(ctx, query); err != nil {
		if pgErr, ok := err.(*pq.Error); ok {
			var line uint
			var col uint
			var lineColOK bool
			if pgErr.Position != "" {
				if pos, err := strconv.ParseUint(pgErr.Position, 10, 64); err == nil {
					line, col, lineColOK = computeLineFromPos(query, int(pos))
				}
			}
			message := fmt.Sprintf("migration failed: %s", pgErr.Message)
			if lineColOK {
				message = fmt.Sprintf("%s (column %d)", message, col)
			}
			if pgErr.Detail != "" {
				message = fmt.Sprintf("%s, %s", message, pgErr.Detail)
			}
			return database.Error{OrigErr: err, Err: message, Query: statement, Line: line}
		}
		return database.Error{OrigErr: err, Err: "migration failed", Query: statement}
	}
	return nil
}

func computeLineFromPos(s string, pos int) (line uint, col uint, ok bool) {
	// replace crlf with lf
	s = strings.ReplaceAll(s, "\r\n", "\n")
	// pg docs: pos uses index 1 for the first character, and positions are measured in characters not bytes
	runes := []rune(s)
	if pos > len(runes) {
		return 0, 0, false
	}
	sel := runes[:pos]
	line = uint(runesCount(sel, newLine) + 1)
	col = uint(pos - 1 - runesLastIndex(sel, newLine))
	return line, col, true
}

const newLine = '\n'

func runesCount(input []rune, target rune) int {
	var count int
	for _, r := range input {
		if r == target {
			count++
		}
	}
	return count
}

func runesLastIndex(input []rune, target rune) int {
	for i := len(input) - 1; i >= 0; i-- {
		if input[i] == target {
			return i
		}
	}
	return -1
}

func (p *Postgres) SetVersion(version int, dirty bool) error {
	tx, err := p.conn.BeginTx(context.Background(), &sql.TxOptions{})
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}

	query := `TRUNCATE ` + pq.QuoteIdentifier(p.config.migrationsSchemaName) + `.` + pq.QuoteIdentifier(p.config.migrationsTableName)
	if _, err := tx.Exec(query); err != nil {
		if errRollback := tx.Rollback(); errRollback != nil {
			err = errors.Join(err, errRollback)
		}
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	// Also re-write the schema version for nil dirty versions to prevent
	// empty schema version for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330
	if version >= 0 || (version == database.NilVersion && dirty) {
		query = `INSERT INTO ` + pq.QuoteIdentifier(p.config.migrationsSchemaName) + `.` + pq.QuoteIdentifier(p.config.migrationsTableName) + ` (version, dirty) VALUES ($1, $2)`
		if _, err := tx.Exec(query, version, dirty); err != nil {
			if errRollback := tx.Rollback(); errRollback != nil {
				err = errors.Join(err, errRollback)
			}
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}

	return nil
}

func (p *Postgres) Version() (version int, dirty bool, err error) {
	query := `SELECT version, dirty FROM ` + pq.QuoteIdentifier(p.config.migrationsSchemaName) + `.` + pq.QuoteIdentifier(p.config.migrationsTableName) + ` LIMIT 1`
	err = p.conn.QueryRowContext(context.Background(), query).Scan(&version, &dirty)
	switch {
	case err == sql.ErrNoRows:
		return database.NilVersion, false, nil

	case err != nil:
		if e, ok := err.(*pq.Error); ok {
			if e.Code.Name() == "undefined_table" {
				return database.NilVersion, false, nil
			}
		}
		return 0, false, &database.Error{OrigErr: err, Query: []byte(query)}

	default:
		return version, dirty, nil
	}
}

func (p *Postgres) Drop() (err error) {
	// select all tables in current schema
	query := `SELECT table_name FROM information_schema.tables WHERE table_schema=(SELECT current_schema()) AND table_type='BASE TABLE'`
	tables, err := p.conn.QueryContext(context.Background(), query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	// delete one table after another
	tableNames := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}
		if len(tableName) > 0 {
			tableNames = append(tableNames, tableName)
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if len(tableNames) > 0 {
		// delete one by one ...
		for _, t := range tableNames {
			query = `DROP TABLE IF EXISTS ` + pq.QuoteIdentifier(t) + ` CASCADE`
			if _, err := p.conn.ExecContext(context.Background(), query); err != nil {
				return &database.Error{OrigErr: err, Query: []byte(query)}
			}
		}
	}

	return nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the Postgres type.
func (p *Postgres) ensureVersionTable() (err error) {
	if err = p.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := p.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	// This block checks whether the `MigrationsTable` already exists. This is useful because it allows read only postgres
	// users to also check the current version of the schema. Previously, even if `MigrationsTable` existed, the
	// `CREATE TABLE IF NOT EXISTS...` query would fail because the user does not have the CREATE permission.
	// Taken from https://github.com/mattes/migrate/blob/master/database/postgres/postgres.go#L258
	query := `SELECT COUNT(1) FROM information_schema.tables WHERE table_schema = $1 AND table_name = $2 LIMIT 1`
	row := p.conn.QueryRowContext(context.Background(), query, p.config.migrationsSchemaName, p.config.migrationsTableName)

	var count int
	err = row.Scan(&count)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if count == 1 {
		return nil
	}

	query = `CREATE TABLE IF NOT EXISTS ` + pq.QuoteIdentifier(p.config.migrationsSchemaName) + `.` + pq.QuoteIdentifier(p.config.migrationsTableName) + ` (version bigint not null primary key, dirty boolean not null)`
	if _, err = p.conn.ExecContext(context.Background(), query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}
```

## File: `database/postgres/postgres_test.go`
```go
package postgres

// error codes https://github.com/lib/pq/blob/master/error.go

import (
	"context"
	"database/sql"
	sqldriver "database/sql/driver"
	"errors"
	"fmt"
	"io"
	"log"
	"strconv"
	"strings"
	"sync"
	"testing"

	"github.com/golang-migrate/migrate/v4"

	"github.com/dhui/dktest"

	"github.com/golang-migrate/migrate/v4/database"
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

const (
	pgPassword = "postgres"
)

var (
	opts = dktest.Options{
		Env:          map[string]string{"POSTGRES_PASSWORD": pgPassword},
		PortRequired: true, ReadyFunc: isReady}
	// Supported versions: https://www.postgresql.org/support/versioning/
	specs = []dktesting.ContainerSpec{
		{ImageName: "postgres:13", Options: opts},
		{ImageName: "postgres:14", Options: opts},
		{ImageName: "postgres:15", Options: opts},
		{ImageName: "postgres:16", Options: opts},
		{ImageName: "postgres:17", Options: opts},
	}
)

func pgConnectionString(host, port string, options ...string) string {
	options = append(options, "sslmode=disable")
	return fmt.Sprintf("postgres://postgres:%s@%s:%s/postgres?%s", pgPassword, host, port, strings.Join(options, "&"))
}

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	ip, port, err := c.FirstPort()
	if err != nil {
		return false
	}

	db, err := sql.Open("postgres", pgConnectionString(ip, port))
	if err != nil {
		return false
	}
	defer func() {
		if err := db.Close(); err != nil {
			log.Println("close error:", err)
		}
	}()
	if err = db.PingContext(ctx); err != nil {
		switch err {
		case sqldriver.ErrBadConn, io.EOF:
			return false
		default:
			log.Println(err)
		}
		return false
	}

	return true
}

func mustRun(t *testing.T, d database.Driver, statements []string) {
	for _, statement := range statements {
		if err := d.Run(strings.NewReader(statement)); err != nil {
			t.Fatal(err)
		}
	}
}

func Test(t *testing.T) {
	t.Run("test", test)
	t.Run("testMigrate", testMigrate)
	t.Run("testMultipleStatements", testMultipleStatements)
	t.Run("testMultipleStatementsInMultiStatementMode", testMultipleStatementsInMultiStatementMode)
	t.Run("testErrorParsing", testErrorParsing)
	t.Run("testFilterCustomQuery", testFilterCustomQuery)
	t.Run("testWithSchema", testWithSchema)
	t.Run("testMigrationTableOption", testMigrationTableOption)
	t.Run("testFailToCreateTableWithoutPermissions", testFailToCreateTableWithoutPermissions)
	t.Run("testCheckBeforeCreateTable", testCheckBeforeCreateTable)
	t.Run("testParallelSchema", testParallelSchema)
	t.Run("testPostgresLock", testPostgresLock)
	t.Run("testWithInstanceConcurrent", testWithInstanceConcurrent)
	t.Run("testWithConnection", testWithConnection)

	t.Cleanup(func() {
		for _, spec := range specs {
			t.Log("Cleaning up ", spec.ImageName)
			if err := spec.Cleanup(); err != nil {
				t.Error("Error removing ", spec.ImageName, "error:", err)
			}
		}
	})
}

func test(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		dt.Test(t, d, []byte("SELECT 1"))
	})
}

func testMigrate(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "postgres", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}

func testMultipleStatements(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		if err := d.Run(strings.NewReader("CREATE TABLE foo (foo text); CREATE TABLE bar (bar text);")); err != nil {
			t.Fatalf("expected err to be nil, got %v", err)
		}

		// make sure second table exists
		var exists bool
		if err := d.(*Postgres).conn.QueryRowContext(context.Background(), "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'bar' AND table_schema = (SELECT current_schema()))").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table bar to exist")
		}
	})
}

func testMultipleStatementsInMultiStatementMode(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port, "x-multi-statement=true")
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		if err := d.Run(strings.NewReader("CREATE TABLE foo (foo text); CREATE INDEX CONCURRENTLY idx_foo ON foo (foo);")); err != nil {
			t.Fatalf("expected err to be nil, got %v", err)
		}

		// make sure created index exists
		var exists bool
		if err := d.(*Postgres).conn.QueryRowContext(context.Background(), "SELECT EXISTS (SELECT 1 FROM pg_indexes WHERE schemaname = (SELECT current_schema()) AND indexname = 'idx_foo')").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table bar to exist")
		}
	})
}

func testErrorParsing(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		wantErr := `migration failed: syntax error at or near "TABLEE" (column 37) in line 1: CREATE TABLE foo ` +
			`(foo text); CREATE TABLEE bar (bar text); (details: pq: syntax error at or near "TABLEE")`
		if err := d.Run(strings.NewReader("CREATE TABLE foo (foo text); CREATE TABLEE bar (bar text);")); err == nil {
			t.Fatal("expected err but got nil")
		} else if err.Error() != wantErr {
			t.Fatalf("expected '%s' but got '%s'", wantErr, err.Error())
		}
	})
}

func testFilterCustomQuery(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-custom=foobar",
			pgPassword, ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
	})
}

func testWithSchema(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		// create foobar schema
		if err := d.Run(strings.NewReader("CREATE SCHEMA foobar AUTHORIZATION postgres")); err != nil {
			t.Fatal(err)
		}
		if err := d.SetVersion(1, false); err != nil {
			t.Fatal(err)
		}

		// re-connect using that schema
		d2, err := p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&search_path=foobar",
			pgPassword, ip, port))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d2.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		version, _, err := d2.Version()
		if err != nil {
			t.Fatal(err)
		}
		if version != database.NilVersion {
			t.Fatal("expected NilVersion")
		}

		// now update version and compare
		if err := d2.SetVersion(2, false); err != nil {
			t.Fatal(err)
		}
		version, _, err = d2.Version()
		if err != nil {
			t.Fatal(err)
		}
		if version != 2 {
			t.Fatal("expected version 2")
		}

		// meanwhile, the public schema still has the other version
		version, _, err = d.Version()
		if err != nil {
			t.Fatal(err)
		}
		if version != 1 {
			t.Fatal("expected version 2")
		}
	})
}

func testMigrationTableOption(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, _ := p.Open(addr)
		defer func() {
			if err := d.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		// create migrate schema
		if err := d.Run(strings.NewReader("CREATE SCHEMA migrate AUTHORIZATION postgres")); err != nil {
			t.Fatal(err)
		}

		// bad unquoted x-migrations-table parameter
		wantErr := "x-migrations-table must be quoted (for instance '\"migrate\".\"schema_migrations\"') when x-migrations-table-quoted is enabled, current value is: migrate.schema_migrations"
		d, err = p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=migrate.schema_migrations&x-migrations-table-quoted=1",
			pgPassword, ip, port))
		if (err != nil) && (err.Error() != wantErr) {
			t.Fatalf("expected '%s' but got '%s'", wantErr, err.Error())
		}

		// too many quoted x-migrations-table parameters
		wantErr = "\"\"migrate\".\"schema_migrations\".\"toomany\"\" MigrationsTable contains too many dot characters"
		d, err = p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=\"migrate\".\"schema_migrations\".\"toomany\"&x-migrations-table-quoted=1",
			pgPassword, ip, port))
		if (err != nil) && (err.Error() != wantErr) {
			t.Fatalf("expected '%s' but got '%s'", wantErr, err.Error())
		}

		// good quoted x-migrations-table parameter
		d, err = p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=\"migrate\".\"schema_migrations\"&x-migrations-table-quoted=1",
			pgPassword, ip, port))
		if err != nil {
			t.Fatal(err)
		}

		// make sure migrate.schema_migrations table exists
		var exists bool
		if err := d.(*Postgres).conn.QueryRowContext(context.Background(), "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'schema_migrations' AND table_schema = 'migrate')").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table migrate.schema_migrations to exist")
		}

		d, err = p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=migrate.schema_migrations",
			pgPassword, ip, port))
		if err != nil {
			t.Fatal(err)
		}
		if err := d.(*Postgres).conn.QueryRowContext(context.Background(), "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'migrate.schema_migrations' AND table_schema = (SELECT current_schema()))").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table 'migrate.schema_migrations' to exist")
		}

	})
}

func testFailToCreateTableWithoutPermissions(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)

		// Check that opening the postgres connection returns NilVersion
		p := &Postgres{}

		d, err := p.Open(addr)

		if err != nil {
			t.Fatal(err)
		}

		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		// create user who is not the owner. Although we're concatenating strings in an sql statement it should be fine
		// since this is a test environment and we're not expecting to the pgPassword to be malicious
		mustRun(t, d, []string{
			"CREATE USER not_owner WITH ENCRYPTED PASSWORD '" + pgPassword + "'",
			"CREATE SCHEMA barfoo AUTHORIZATION postgres",
			"GRANT USAGE ON SCHEMA barfoo TO not_owner",
			"REVOKE CREATE ON SCHEMA barfoo FROM PUBLIC",
			"REVOKE CREATE ON SCHEMA barfoo FROM not_owner",
		})

		// re-connect using that schema
		d2, err := p.Open(fmt.Sprintf("postgres://not_owner:%s@%v:%v/postgres?sslmode=disable&search_path=barfoo",
			pgPassword, ip, port))

		defer func() {
			if d2 == nil {
				return
			}
			if err := d2.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		var e *database.Error
		if !errors.As(err, &e) || err == nil {
			t.Fatal("Unexpected error, want permission denied error. Got: ", err)
		}

		if !strings.Contains(e.OrigErr.Error(), "permission denied for schema barfoo") {
			t.Fatal(e)
		}

		// re-connect using that x-migrations-table and x-migrations-table-quoted
		d2, err = p.Open(fmt.Sprintf("postgres://not_owner:%s@%v:%v/postgres?sslmode=disable&x-migrations-table=\"barfoo\".\"schema_migrations\"&x-migrations-table-quoted=1",
			pgPassword, ip, port))

		if !errors.As(err, &e) || err == nil {
			t.Fatal("Unexpected error, want permission denied error. Got: ", err)
		}

		if !strings.Contains(e.OrigErr.Error(), "permission denied for schema barfoo") {
			t.Fatal(e)
		}
	})
}

func testCheckBeforeCreateTable(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)

		// Check that opening the postgres connection returns NilVersion
		p := &Postgres{}

		d, err := p.Open(addr)

		if err != nil {
			t.Fatal(err)
		}

		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		// create user who is not the owner. Although we're concatenating strings in an sql statement it should be fine
		// since this is a test environment and we're not expecting to the pgPassword to be malicious
		mustRun(t, d, []string{
			"CREATE USER not_owner WITH ENCRYPTED PASSWORD '" + pgPassword + "'",
			"CREATE SCHEMA barfoo AUTHORIZATION postgres",
			"GRANT USAGE ON SCHEMA barfoo TO not_owner",
			"GRANT CREATE ON SCHEMA barfoo TO not_owner",
		})

		// re-connect using that schema
		d2, err := p.Open(fmt.Sprintf("postgres://not_owner:%s@%v:%v/postgres?sslmode=disable&search_path=barfoo",
			pgPassword, ip, port))

		if err != nil {
			t.Fatal(err)
		}

		if err := d2.Close(); err != nil {
			t.Fatal(err)
		}

		// revoke privileges
		mustRun(t, d, []string{
			"REVOKE CREATE ON SCHEMA barfoo FROM PUBLIC",
			"REVOKE CREATE ON SCHEMA barfoo FROM not_owner",
		})

		// re-connect using that schema
		d3, err := p.Open(fmt.Sprintf("postgres://not_owner:%s@%v:%v/postgres?sslmode=disable&search_path=barfoo",
			pgPassword, ip, port))

		if err != nil {
			t.Fatal(err)
		}

		version, _, err := d3.Version()

		if err != nil {
			t.Fatal(err)
		}

		if version != database.NilVersion {
			t.Fatal("Unexpected version, want database.NilVersion. Got: ", version)
		}

		defer func() {
			if err := d3.Close(); err != nil {
				t.Fatal(err)
			}
		}()
	})
}

func testParallelSchema(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		// create foo and bar schemas
		if err := d.Run(strings.NewReader("CREATE SCHEMA foo AUTHORIZATION postgres")); err != nil {
			t.Fatal(err)
		}
		if err := d.Run(strings.NewReader("CREATE SCHEMA bar AUTHORIZATION postgres")); err != nil {
			t.Fatal(err)
		}

		// re-connect using that schemas
		dfoo, err := p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&search_path=foo",
			pgPassword, ip, port))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := dfoo.Close(); err != nil {
				t.Error(err)
			}
		}()

		dbar, err := p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&search_path=bar",
			pgPassword, ip, port))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := dbar.Close(); err != nil {
				t.Error(err)
			}
		}()

		if err := dfoo.Lock(); err != nil {
			t.Fatal(err)
		}

		if err := dbar.Lock(); err != nil {
			t.Fatal(err)
		}

		if err := dbar.Unlock(); err != nil {
			t.Fatal(err)
		}

		if err := dfoo.Unlock(); err != nil {
			t.Fatal(err)
		}
	})
}

func testPostgresLock(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Postgres{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}

		dt.Test(t, d, []byte("SELECT 1"))

		ps := d.(*Postgres)

		err = ps.Lock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Unlock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Lock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Unlock()
		if err != nil {
			t.Fatal(err)
		}
	})
}

func testWithInstanceConcurrent(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		// The number of concurrent processes running WithInstance
		const concurrency = 30

		// We can instantiate a single database handle because it is
		// actually a connection pool, and so, each of the below go
		// routines will have a high probability of using a separate
		// connection, which is something we want to exercise.
		db, err := sql.Open("postgres", pgConnectionString(ip, port))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := db.Close(); err != nil {
				t.Error(err)
			}
		}()

		db.SetMaxIdleConns(concurrency)
		db.SetMaxOpenConns(concurrency)

		var wg sync.WaitGroup
		defer wg.Wait()

		wg.Add(concurrency)
		for i := 0; i < concurrency; i++ {
			go func(i int) {
				defer wg.Done()
				_, err := WithInstance(db, &Config{})
				if err != nil {
					t.Errorf("process %d error: %s", i, err)
				}
			}(i)
		}
	})
}

func testWithConnection(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		db, err := sql.Open("postgres", pgConnectionString(ip, port))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := db.Close(); err != nil {
				t.Error(err)
			}
		}()

		ctx := context.Background()
		conn, err := db.Conn(ctx)
		if err != nil {
			t.Fatal(err)
		}

		p, err := WithConnection(ctx, conn, &Config{})
		if err != nil {
			t.Fatal(err)
		}

		defer func() {
			if err := p.Close(); err != nil {
				t.Error(err)
			}
		}()
		dt.Test(t, p, []byte("SELECT 1"))
	})
}

func Test_computeLineFromPos(t *testing.T) {
	testcases := []struct {
		pos      int
		wantLine uint
		wantCol  uint
		input    string
		wantOk   bool
	}{
		{
			15, 2, 6, "SELECT *\nFROM foo", true, // foo table does not exists
		},
		{
			16, 3, 6, "SELECT *\n\nFROM foo", true, // foo table does not exists, empty line
		},
		{
			25, 3, 7, "SELECT *\nFROM foo\nWHERE x", true, // x column error
		},
		{
			27, 5, 7, "SELECT *\n\nFROM foo\n\nWHERE x", true, // x column error, empty lines
		},
		{
			10, 2, 1, "SELECT *\nFROMM foo", true, // FROMM typo
		},
		{
			11, 3, 1, "SELECT *\n\nFROMM foo", true, // FROMM typo, empty line
		},
		{
			17, 2, 8, "SELECT *\nFROM foo", true, // last character
		},
		{
			18, 0, 0, "SELECT *\nFROM foo", false, // invalid position
		},
	}
	for i, tc := range testcases {
		t.Run("tc"+strconv.Itoa(i), func(t *testing.T) {
			run := func(crlf bool, nonASCII bool) {
				var name string
				if crlf {
					name = "crlf"
				} else {
					name = "lf"
				}
				if nonASCII {
					name += "-nonascii"
				} else {
					name += "-ascii"
				}
				t.Run(name, func(t *testing.T) {
					input := tc.input
					if crlf {
						input = strings.ReplaceAll(input, "\n", "\r\n")
					}
					if nonASCII {
						input = strings.ReplaceAll(input, "FROM", "FRÖM")
					}
					gotLine, gotCol, gotOK := computeLineFromPos(input, tc.pos)

					if tc.wantOk {
						t.Logf("pos %d, want %d:%d, %#v", tc.pos, tc.wantLine, tc.wantCol, input)
					}

					if gotOK != tc.wantOk {
						t.Fatalf("expected ok %v but got %v", tc.wantOk, gotOK)
					}
					if gotLine != tc.wantLine {
						t.Fatalf("expected line %d but got %d", tc.wantLine, gotLine)
					}
					if gotCol != tc.wantCol {
						t.Fatalf("expected col %d but got %d", tc.wantCol, gotCol)
					}
				})
			}
			run(false, false)
			run(true, false)
			run(false, true)
			run(true, true)
		})
	}
}
```

## File: `database/postgres/README.md`
```markdown
# postgres

`postgres://user:password@host:port/dbname?query` (`postgresql://` works, too)

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table |
| `x-migrations-table-quoted` | `MigrationsTableQuoted` | By default, migrate quotes the migration table for SQL injection safety reasons. This option disable quoting and naively checks that you have quoted the migration table name. e.g. `"my_schema"."schema_migrations"` |
| `x-statement-timeout` | `StatementTimeout` | Abort any statement that takes more than the specified number of milliseconds |
| `x-multi-statement` | `MultiStatementEnabled` | Enable multi-statement execution (default: false) |
| `x-multi-statement-max-size` | `MultiStatementMaxSize` | Maximum size of single statement in bytes (default: 10MB) |
| `dbname` | `DatabaseName` | The name of the database to connect to |
| `search_path` | | This variable specifies the order in which schemas are searched when an object is referenced by a simple name with no schema specified. |
| `user` | | The user to sign in as |
| `password` | | The user's password | 
| `host` | | The host to connect to. Values that start with / are for unix domain sockets. (default is localhost) |
| `port` | | The port to bind to. (default is 5432) |
| `fallback_application_name` | | An application_name to fall back to if one isn't provided. |
| `connect_timeout` | | Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely. |
| `sslcert` | | Cert file location. The file must contain PEM encoded data. |
| `sslkey` | | Key file location. The file must contain PEM encoded data. |
| `sslrootcert` | | The location of the root certificate file. The file must contain PEM encoded data. | 
| `sslmode` | | Whether or not to use SSL (disable\|require\|verify-ca\|verify-full) |


## Upgrading from v1

1. Write down the current migration version from schema_migrations
1. `DROP TABLE schema_migrations`
2. Wrap your existing migrations in transactions ([BEGIN/COMMIT](https://www.postgresql.org/docs/current/static/transaction-iso.html)) if you use multiple statements within one migration.
3. Download and install the latest migrate version.
4. Force the current migration version with `migrate force <current_version>`.

## Multi-statement mode

In PostgreSQL running multiple SQL statements in one `Exec` executes them inside a transaction. Sometimes this
behavior is not desirable because some statements can be only run outside of transaction (e.g.
`CREATE INDEX CONCURRENTLY`). If you want to use `CREATE INDEX CONCURRENTLY` without activating multi-statement mode
you have to put such statements in a separate migration files.
```

## File: `database/postgres/TUTORIAL.md`
```markdown
# PostgreSQL tutorial for beginners

## Create/configure database

For the purpose of this tutorial let's create PostgreSQL database called `example`.
Our user here is `postgres`, password `password`, and host is `localhost`.
```
psql -h localhost -U postgres -w -c "create database example;"
```
When using Migrate CLI we need to pass to database URL. Let's export it to a variable for convenience:
```
export POSTGRESQL_URL='postgres://postgres:password@localhost:5432/example?sslmode=disable'
```
`sslmode=disable` means that the connection with our database will not be encrypted. Enabling it is left as an exercise.

You can find further description of database URLs [here](README.md#database-urls).

## Create migrations
Let's create table called `users`:
```
migrate create -ext sql -dir db/migrations -seq create_users_table
```
If there were no errors, we should have two files available under `db/migrations` folder:
- 000001_create_users_table.down.sql
- 000001_create_users_table.up.sql

Note the `sql` extension that we provided.

In the `.up.sql` file let's create the table:
```sql
CREATE TABLE IF NOT EXISTS users(
   user_id serial PRIMARY KEY,
   username VARCHAR (50) UNIQUE NOT NULL,
   password VARCHAR (50) NOT NULL,
   email VARCHAR (300) UNIQUE NOT NULL
);
```
And in the `.down.sql` let's delete it:
```sql
DROP TABLE IF EXISTS users;
```
By adding `IF EXISTS/IF NOT EXISTS` we are making migrations idempotent - you can read more about idempotency in [getting started](../corp/docs/usage_guides/getting_started.md#create-migrations)

## Run migrations
```
migrate -database ${POSTGRESQL_URL} -path db/migrations up
```
Let's check if the table was created properly by running `psql example -c "\d users"`.
The output you are supposed to see:
```
                                    Table "public.users"
  Column  |          Type          |                        Modifiers                        
----------+------------------------+---------------------------------------------------------
 user_id  | integer                | not null default nextval('users_user_id_seq'::regclass)
 username | character varying(50)  | not null
 password | character varying(50)  | not null
 email    | character varying(300) | not null
Indexes:
    "users_pkey" PRIMARY KEY, btree (user_id)
    "users_email_key" UNIQUE CONSTRAINT, btree (email)
    "users_username_key" UNIQUE CONSTRAINT, btree (username)
```
Great! Now let's check if running reverse migration also works:
```
migrate -database ${POSTGRESQL_URL} -path db/migrations down
```
Make sure to check if your database changed as expected in this case as well.

## Database transactions

To show database transactions usage, let's create another set of migrations by running:
```
migrate create -ext sql -dir db/migrations -seq add_mood_to_users
```
Again, it should create for us two migrations files:
- 000002_add_mood_to_users.down.sql
- 000002_add_mood_to_users.up.sql

In Postgres, when we want our queries to be done in a transaction, we need to wrap it with `BEGIN` and `COMMIT` commands.
In our example, we are going to add a column to our database that can only accept enumerable values or NULL.
Migration up:
```sql
BEGIN;

CREATE TYPE enum_mood AS ENUM (
	'happy',
	'sad',
	'neutral'
);
ALTER TABLE users ADD COLUMN mood enum_mood;

COMMIT;
```
Migration down:
```sql
BEGIN;

ALTER TABLE users DROP COLUMN mood;
DROP TYPE enum_mood;

COMMIT;
```

Now we can run our new migration and check the database:
```
migrate -database ${POSTGRESQL_URL} -path db/migrations up
psql example -c "\d users"
```
Expected output:
```
                                    Table "public.users"
  Column  |          Type          |                        Modifiers                        
----------+------------------------+---------------------------------------------------------
 user_id  | integer                | not null default nextval('users_user_id_seq'::regclass)
 username | character varying(50)  | not null
 password | character varying(50)  | not null
 email    | character varying(300) | not null
 mood     | enum_mood              | 
Indexes:
    "users_pkey" PRIMARY KEY, btree (user_id)
    "users_email_key" UNIQUE CONSTRAINT, btree (email)
    "users_username_key" UNIQUE CONSTRAINT, btree (username)
```

## Optional: Run migrations within your Go app
Here is a very simple app running migrations for the above configuration:
```go
import (
	"log"

	"github.com/golang-migrate/migrate/v4"
	_ "github.com/golang-migrate/migrate/v4/database/postgres"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

func main() {
	m, err := migrate.New(
		"file://db/migrations",
		"postgres://postgres:postgres@localhost:5432/example?sslmode=disable")
	if err != nil {
		log.Fatal(err)
	}
	if err := m.Up(); err != nil {
		log.Fatal(err)
	}
}
```
You can find details [here](README.md#use-in-your-go-project)

## Fix issue where migrations run twice

When the schema and role names are the same, you might run into issues if you create this schema using migrations.
This is caused by the fact that the [default `search_path`](https://www.postgresql.org/docs/current/ddl-schemas.html#DDL-SCHEMAS-PATH) is `"$user", public`.
In the first run (with an empty database) the migrate table is created in `public`.
When the migrations create the `$user` schema, the next run will store (a new) migrate table in this schema (due to order of schemas in `search_path`) and tries to apply all migrations again (most likely failing).

To solve this you need to change the default `search_path` by removing the `$user` component, so the migrate table is always stored in the (available) `public` schema.
This can be done using the [`search_path` query parameter in the URL](https://github.com/jexia/migrate/blob/fix-postgres-version-table/database/postgres/README.md#postgres).

For example to force the migrations table in the public schema you can use:
```
export POSTGRESQL_URL='postgres://postgres:password@localhost:5432/example?sslmode=disable&search_path=public'
```

Note that you need to explicitly add the schema names to the table names in your migrations when you to modify the tables of the non-public schema.

Alternatively you can add the non-public schema manually (before applying the migrations) if that is possible in your case and let the tool store the migrations table in this schema as well.
```

## File: `database/postgres/examples/migrations/1085649617_create_users_table.down.sql`
```sql
DROP TABLE IF EXISTS users;
```

## File: `database/postgres/examples/migrations/1085649617_create_users_table.up.sql`
```sql
CREATE TABLE users (
  user_id integer unique,
  name    varchar(40),
  email   varchar(40)
);
```

## File: `database/postgres/examples/migrations/1185749658_add_city_to_users.down.sql`
```sql
ALTER TABLE users DROP COLUMN IF EXISTS city;
```

## File: `database/postgres/examples/migrations/1185749658_add_city_to_users.up.sql`
```sql
ALTER TABLE users ADD COLUMN city varchar(100);


```

## File: `database/postgres/examples/migrations/1285849751_add_index_on_user_emails.down.sql`
```sql
DROP INDEX IF EXISTS users_email_index;
```

## File: `database/postgres/examples/migrations/1285849751_add_index_on_user_emails.up.sql`
```sql
CREATE UNIQUE INDEX CONCURRENTLY users_email_index ON users (email);

-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/postgres/examples/migrations/1385949617_create_books_table.down.sql`
```sql
DROP TABLE IF EXISTS books;
```

## File: `database/postgres/examples/migrations/1385949617_create_books_table.up.sql`
```sql
CREATE TABLE books (
  user_id integer,
  name    varchar(40),
  author  varchar(40)
);
```

## File: `database/postgres/examples/migrations/1485949617_create_movies_table.down.sql`
```sql
DROP TABLE IF EXISTS movies;
```

## File: `database/postgres/examples/migrations/1485949617_create_movies_table.up.sql`
```sql
CREATE TABLE movies (
  user_id   integer,
  name      varchar(40),
  director  varchar(40)
);
```

## File: `database/postgres/examples/migrations/1585849751_just_a_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/postgres/examples/migrations/1685849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/postgres/examples/migrations/1785849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/postgres/examples/migrations/1885849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/ql/ql.go`
```go
package ql

import (
	"database/sql"
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"strings"
	"sync/atomic"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	_ "modernc.org/ql/driver"
)

func init() {
	database.Register("ql", &Ql{})
}

var DefaultMigrationsTable = "schema_migrations"
var (
	ErrDatabaseDirty  = fmt.Errorf("database is dirty")
	ErrNilConfig      = fmt.Errorf("no config")
	ErrNoDatabaseName = fmt.Errorf("no database name")
	ErrAppendPEM      = fmt.Errorf("failed to append PEM")
)

type Config struct {
	MigrationsTable string
	DatabaseName    string
}

type Ql struct {
	db       *sql.DB
	isLocked atomic.Bool

	config *Config
}

func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	mx := &Ql{
		db:     instance,
		config: config,
	}
	if err := mx.ensureVersionTable(); err != nil {
		return nil, err
	}
	return mx, nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the Ql type.
func (m *Ql) ensureVersionTable() (err error) {
	if err = m.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := m.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	tx, err := m.db.Begin()
	if err != nil {
		return err
	}
	if _, err := tx.Exec(fmt.Sprintf(`
	CREATE TABLE IF NOT EXISTS %s (version uint64, dirty bool);
	CREATE UNIQUE INDEX IF NOT EXISTS version_unique ON %s (version);
`, m.config.MigrationsTable, m.config.MigrationsTable)); err != nil {
		if err := tx.Rollback(); err != nil {
			return err
		}
		return err
	}
	if err := tx.Commit(); err != nil {
		return err
	}
	return nil
}

func (m *Ql) Open(url string) (database.Driver, error) {
	purl, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}
	dbfile := strings.Replace(migrate.FilterCustomQuery(purl).String(), "ql://", "", 1)
	db, err := sql.Open("ql", dbfile)
	if err != nil {
		return nil, err
	}
	migrationsTable := purl.Query().Get("x-migrations-table")
	if len(migrationsTable) == 0 {
		migrationsTable = DefaultMigrationsTable
	}
	mx, err := WithInstance(db, &Config{
		DatabaseName:    purl.Path,
		MigrationsTable: migrationsTable,
	})
	if err != nil {
		return nil, err
	}
	return mx, nil
}
func (m *Ql) Close() error {
	return m.db.Close()
}
func (m *Ql) Drop() (err error) {
	query := `SELECT Name FROM __Table`
	tables, err := m.db.Query(query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	tableNames := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}
		if len(tableName) > 0 {
			if !strings.HasPrefix(tableName, "__") {
				tableNames = append(tableNames, tableName)
			}
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if len(tableNames) > 0 {
		for _, t := range tableNames {
			query := "DROP TABLE " + t
			err = m.executeQuery(query)
			if err != nil {
				return &database.Error{OrigErr: err, Query: []byte(query)}
			}
		}
	}

	return nil
}
func (m *Ql) Lock() error {
	if !m.isLocked.CompareAndSwap(false, true) {
		return database.ErrLocked
	}
	return nil
}
func (m *Ql) Unlock() error {
	if !m.isLocked.CompareAndSwap(true, false) {
		return database.ErrNotLocked
	}
	return nil
}
func (m *Ql) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}
	query := string(migr[:])

	return m.executeQuery(query)
}
func (m *Ql) executeQuery(query string) error {
	tx, err := m.db.Begin()
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}
	if _, err := tx.Exec(query); err != nil {
		if errRollback := tx.Rollback(); errRollback != nil {
			err = errors.Join(err, errRollback)
		}
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}
	return nil
}
func (m *Ql) SetVersion(version int, dirty bool) error {
	tx, err := m.db.Begin()
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}

	query := "TRUNCATE TABLE " + m.config.MigrationsTable
	if _, err := tx.Exec(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	// Also re-write the schema version for nil dirty versions to prevent
	// empty schema version for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330
	if version >= 0 || (version == database.NilVersion && dirty) {
		query := fmt.Sprintf(`INSERT INTO %s (version, dirty) VALUES (uint64(?1), ?2)`,
			m.config.MigrationsTable)
		if _, err := tx.Exec(query, version, dirty); err != nil {
			if errRollback := tx.Rollback(); errRollback != nil {
				err = errors.Join(err, errRollback)
			}
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}

	return nil
}

func (m *Ql) Version() (version int, dirty bool, err error) {
	query := "SELECT version, dirty FROM " + m.config.MigrationsTable + " LIMIT 1"
	err = m.db.QueryRow(query).Scan(&version, &dirty)
	if err != nil {
		return database.NilVersion, false, nil
	}
	return version, dirty, nil
}
```

## File: `database/ql/ql_test.go`
```go
package ql

import (
	"database/sql"
	"fmt"
	"path/filepath"
	"testing"

	"github.com/golang-migrate/migrate/v4"
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	_ "github.com/golang-migrate/migrate/v4/source/file"
	_ "modernc.org/ql/driver"
)

func Test(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "ql.db"))
	p := &Ql{}
	addr := fmt.Sprintf("ql://%s", filepath.Join(dir, "ql.db"))
	d, err := p.Open(addr)
	if err != nil {
		t.Fatal(err)
	}

	db, err := sql.Open("ql", filepath.Join(dir, "ql.db"))
	if err != nil {
		return
	}
	defer func() {
		if err := db.Close(); err != nil {
			return
		}
	}()
	dt.Test(t, d, []byte("CREATE TABLE t (Qty int, Name string);"))
}

func TestMigrate(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "ql.db"))

	db, err := sql.Open("ql", filepath.Join(dir, "ql.db"))
	if err != nil {
		return
	}
	defer func() {
		if err := db.Close(); err != nil {
			return
		}
	}()

	driver, err := WithInstance(db, &Config{})
	if err != nil {
		t.Fatal(err)
	}

	m, err := migrate.NewWithDatabaseInstance(
		"file://./examples/migrations",
		"ql", driver)
	if err != nil {
		t.Fatal(err)
	}
	dt.TestMigrate(t, m)
}
```

## File: `database/ql/examples/migrations/33_create_table.down.sql`
```sql
DROP TABLE IF EXISTS pets;
```

## File: `database/ql/examples/migrations/33_create_table.up.sql`
```sql
CREATE TABLE pets (
  name string
);
```

## File: `database/ql/examples/migrations/44_alter_table.down.sql`
```sql
DROP TABLE IF EXISTS pets;
```

## File: `database/ql/examples/migrations/44_alter_table.up.sql`
```sql
ALTER TABLE pets ADD predator bool;;
```

## File: `database/redshift/README.md`
```markdown
# Redshift

`redshift://user:password@host:port/dbname?query`

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table |
| `dbname` | `DatabaseName` | The name of the database to connect to |
| `search_path` | | This variable specifies the order in which schemas are searched when an object is referenced by a simple name with no schema specified. |
| `user` | | The user to sign in as |
| `password` | | The user's password | 
| `host` | | The host to connect to. Values that start with / are for unix domain sockets. (default is localhost) |
| `port` | | The port to bind to. (default is 5439) |
| `fallback_application_name` | | An application_name to fall back to if one isn't provided. |
| `connect_timeout` | | Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely. |
| `sslcert` | | Cert file location. The file must contain PEM encoded data. |
| `sslkey` | | Key file location. The file must contain PEM encoded data. |
| `sslrootcert` | | The location of the root certificate file. The file must contain PEM encoded data. | 
| `sslmode` | | Whether or not to use SSL (disable\|require\|verify-ca\|verify-full) |

Redshift is PostgreSQL compatible but has some specific features (or lack thereof) that require slightly different behavior.
```

## File: `database/redshift/redshift.go`
```go
//go:build go1.9

package redshift

import (
	"context"
	"database/sql"
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"strconv"
	"strings"
	"sync/atomic"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	"github.com/lib/pq"
)

func init() {
	db := Redshift{}
	database.Register("redshift", &db)
}

var DefaultMigrationsTable = "schema_migrations"

var (
	ErrNilConfig      = fmt.Errorf("no config")
	ErrNoDatabaseName = fmt.Errorf("no database name")
)

type Config struct {
	MigrationsTable string
	DatabaseName    string
}

type Redshift struct {
	isLocked atomic.Bool
	conn     *sql.Conn
	db       *sql.DB

	// Open and WithInstance need to guarantee that config is never nil
	config *Config
}

func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	if config.DatabaseName == "" {
		query := `SELECT CURRENT_DATABASE()`
		var databaseName string
		if err := instance.QueryRow(query).Scan(&databaseName); err != nil {
			return nil, &database.Error{OrigErr: err, Query: []byte(query)}
		}

		if len(databaseName) == 0 {
			return nil, ErrNoDatabaseName
		}

		config.DatabaseName = databaseName
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	conn, err := instance.Conn(context.Background())

	if err != nil {
		return nil, err
	}

	px := &Redshift{
		conn:   conn,
		db:     instance,
		config: config,
	}

	if err := px.ensureVersionTable(); err != nil {
		return nil, err
	}

	return px, nil
}

func (p *Redshift) Open(url string) (database.Driver, error) {
	purl, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}
	purl.Scheme = "postgres"

	db, err := sql.Open("postgres", migrate.FilterCustomQuery(purl).String())
	if err != nil {
		return nil, err
	}

	migrationsTable := purl.Query().Get("x-migrations-table")

	px, err := WithInstance(db, &Config{
		DatabaseName:    purl.Path,
		MigrationsTable: migrationsTable,
	})
	if err != nil {
		return nil, err
	}

	return px, nil
}

func (p *Redshift) Close() error {
	connErr := p.conn.Close()
	dbErr := p.db.Close()
	if connErr != nil || dbErr != nil {
		return fmt.Errorf("conn: %v, db: %v", connErr, dbErr)
	}
	return nil
}

// Redshift does not support advisory lock functions: https://docs.aws.amazon.com/redshift/latest/dg/c_unsupported-postgresql-functions.html
func (p *Redshift) Lock() error {
	if !p.isLocked.CompareAndSwap(false, true) {
		return database.ErrLocked
	}
	return nil
}

func (p *Redshift) Unlock() error {
	if !p.isLocked.CompareAndSwap(true, false) {
		return database.ErrNotLocked
	}
	return nil
}

func (p *Redshift) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}

	// run migration
	query := string(migr[:])
	if _, err := p.conn.ExecContext(context.Background(), query); err != nil {
		if pgErr, ok := err.(*pq.Error); ok {
			var line uint
			var col uint
			var lineColOK bool
			if pgErr.Position != "" {
				if pos, err := strconv.ParseUint(pgErr.Position, 10, 64); err == nil {
					line, col, lineColOK = computeLineFromPos(query, int(pos))
				}
			}
			message := fmt.Sprintf("migration failed: %s", pgErr.Message)
			if lineColOK {
				message = fmt.Sprintf("%s (column %d)", message, col)
			}
			if pgErr.Detail != "" {
				message = fmt.Sprintf("%s, %s", message, pgErr.Detail)
			}
			return database.Error{OrigErr: err, Err: message, Query: migr, Line: line}
		}
		return database.Error{OrigErr: err, Err: "migration failed", Query: migr}
	}

	return nil
}

func computeLineFromPos(s string, pos int) (line uint, col uint, ok bool) {
	// replace crlf with lf
	s = strings.ReplaceAll(s, "\r\n", "\n")
	// pg docs: pos uses index 1 for the first character, and positions are measured in characters not bytes
	runes := []rune(s)
	if pos > len(runes) {
		return 0, 0, false
	}
	sel := runes[:pos]
	line = uint(runesCount(sel, newLine) + 1)
	col = uint(pos - 1 - runesLastIndex(sel, newLine))
	return line, col, true
}

const newLine = '\n'

func runesCount(input []rune, target rune) int {
	var count int
	for _, r := range input {
		if r == target {
			count++
		}
	}
	return count
}

func runesLastIndex(input []rune, target rune) int {
	for i := len(input) - 1; i >= 0; i-- {
		if input[i] == target {
			return i
		}
	}
	return -1
}

func (p *Redshift) SetVersion(version int, dirty bool) error {
	tx, err := p.conn.BeginTx(context.Background(), &sql.TxOptions{})
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}

	query := `DELETE FROM "` + p.config.MigrationsTable + `"`
	if _, err := tx.Exec(query); err != nil {
		if errRollback := tx.Rollback(); errRollback != nil {
			err = errors.Join(err, errRollback)
		}
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	// Also re-write the schema version for nil dirty versions to prevent
	// empty schema version for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330
	if version >= 0 || (version == database.NilVersion && dirty) {
		query = `INSERT INTO "` + p.config.MigrationsTable + `" (version, dirty) VALUES ($1, $2)`
		if _, err := tx.Exec(query, version, dirty); err != nil {
			if errRollback := tx.Rollback(); errRollback != nil {
				err = errors.Join(err, errRollback)
			}
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}

	return nil
}

func (p *Redshift) Version() (version int, dirty bool, err error) {
	query := `SELECT version, dirty FROM "` + p.config.MigrationsTable + `" LIMIT 1`
	err = p.conn.QueryRowContext(context.Background(), query).Scan(&version, &dirty)
	switch {
	case err == sql.ErrNoRows:
		return database.NilVersion, false, nil

	case err != nil:
		if e, ok := err.(*pq.Error); ok {
			if e.Code.Name() == "undefined_table" {
				return database.NilVersion, false, nil
			}
		}
		return 0, false, &database.Error{OrigErr: err, Query: []byte(query)}

	default:
		return version, dirty, nil
	}
}

func (p *Redshift) Drop() (err error) {
	// select all tables in current schema
	query := `SELECT table_name FROM information_schema.tables WHERE table_schema=(SELECT current_schema()) AND table_type='BASE TABLE'`
	tables, err := p.conn.QueryContext(context.Background(), query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	// delete one table after another
	tableNames := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}
		if len(tableName) > 0 {
			tableNames = append(tableNames, tableName)
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if len(tableNames) > 0 {
		// delete one by one ...
		for _, t := range tableNames {
			query = `DROP TABLE IF EXISTS ` + t + ` CASCADE`
			if _, err := p.conn.ExecContext(context.Background(), query); err != nil {
				return &database.Error{OrigErr: err, Query: []byte(query)}
			}
		}
	}

	return nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the Redshift type.
func (p *Redshift) ensureVersionTable() (err error) {
	if err = p.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := p.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	// check if migration table exists
	var count int
	query := `SELECT COUNT(1) FROM information_schema.tables WHERE table_name = $1 AND table_schema = (SELECT current_schema()) LIMIT 1`
	if err := p.conn.QueryRowContext(context.Background(), query, p.config.MigrationsTable).Scan(&count); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	if count == 1 {
		return nil
	}

	// if not, create the empty migration table
	query = `CREATE TABLE "` + p.config.MigrationsTable + `" (version bigint not null primary key, dirty boolean not null)`
	if _, err := p.conn.ExecContext(context.Background(), query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	return nil
}
```

## File: `database/redshift/redshift_test.go`
```go
package redshift

// error codes https://github.com/lib/pq/blob/master/error.go

import (
	"bytes"
	"context"
	"database/sql"
	sqldriver "database/sql/driver"
	"fmt"
	"log"

	"github.com/golang-migrate/migrate/v4"
	"io"
	"strconv"
	"strings"
	"testing"
)

import (
	"github.com/dhui/dktest"
)

import (
	"github.com/golang-migrate/migrate/v4/database"
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

const (
	pgPassword = "redshift"
)

var (
	opts = dktest.Options{
		Env:          map[string]string{"POSTGRES_PASSWORD": pgPassword},
		PortRequired: true,
		ReadyFunc:    isReady,
	}

	specs = []dktesting.ContainerSpec{
		{ImageName: "migrate/postgres8:8", Options: opts},
	}
)

func redshiftConnectionString(host, port string) string {
	return connectionString("redshift", host, port)
}

func pgConnectionString(host, port string) string {
	return connectionString("postgres", host, port)
}

func connectionString(schema, host, port string) string {
	return fmt.Sprintf("%s://postgres:%s@%s:%s/postgres?sslmode=disable", schema, pgPassword, host, port)
}

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	ip, port, err := c.FirstPort()
	if err != nil {
		return false
	}

	db, err := sql.Open("postgres", pgConnectionString(ip, port))
	if err != nil {
		return false
	}
	defer func() {
		if err := db.Close(); err != nil {
			log.Println("close error:", err)
		}
	}()
	if err = db.PingContext(ctx); err != nil {
		switch err {
		case sqldriver.ErrBadConn, io.EOF:
			return false
		default:
			log.Println(err)
		}
		return false
	}

	return true
}

func Test(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := redshiftConnectionString(ip, port)
		p := &Redshift{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		dt.Test(t, d, []byte("SELECT 1"))
	})
}

func TestMigrate(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := redshiftConnectionString(ip, port)
		p := &Redshift{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "postgres", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}

func TestMultiStatement(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := redshiftConnectionString(ip, port)
		p := &Redshift{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		if err := d.Run(bytes.NewReader([]byte("CREATE TABLE foo (foo text); CREATE TABLE bar (bar text);"))); err != nil {
			t.Fatalf("expected err to be nil, got %v", err)
		}

		// make sure second table exists
		var exists bool
		if err := d.(*Redshift).conn.QueryRowContext(context.Background(), "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'bar' AND table_schema = (SELECT current_schema()))").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatalf("expected table bar to exist")
		}
	})
}

func TestErrorParsing(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := redshiftConnectionString(ip, port)
		p := &Redshift{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		wantErr := `migration failed: syntax error at or near "TABLEE" (column 37) in line 1: CREATE TABLE foo ` +
			`(foo text); CREATE TABLEE bar (bar text); (details: pq: syntax error at or near "TABLEE")`
		if err := d.Run(bytes.NewReader([]byte("CREATE TABLE foo (foo text); CREATE TABLEE bar (bar text);"))); err == nil {
			t.Fatal("expected err but got nil")
		} else if err.Error() != wantErr {
			t.Fatalf("expected '%s' but got '%s'", wantErr, err.Error())
		}
	})
}

func TestFilterCustomQuery(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&x-custom=foobar", pgPassword, ip, port)
		p := &Redshift{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
	})
}

func TestWithSchema(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := redshiftConnectionString(ip, port)
		p := &Redshift{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		// create foobar schema
		if err := d.Run(bytes.NewReader([]byte("CREATE SCHEMA foobar AUTHORIZATION postgres"))); err != nil {
			t.Fatal(err)
		}
		if err := d.SetVersion(1, false); err != nil {
			t.Fatal(err)
		}

		// re-connect using that schema
		d2, err := p.Open(fmt.Sprintf("postgres://postgres:%s@%v:%v/postgres?sslmode=disable&search_path=foobar", pgPassword, ip, port))
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d2.Close(); err != nil {
				t.Error(err)
			}
		}()

		version, _, err := d2.Version()
		if err != nil {
			t.Fatal(err)
		}
		if version != database.NilVersion {
			t.Fatal("expected NilVersion")
		}

		// now update version and compare
		if err := d2.SetVersion(2, false); err != nil {
			t.Fatal(err)
		}
		version, _, err = d2.Version()
		if err != nil {
			t.Fatal(err)
		}
		if version != 2 {
			t.Fatal("expected version 2")
		}

		// meanwhile, the public schema still has the other version
		version, _, err = d.Version()
		if err != nil {
			t.Fatal(err)
		}
		if version != 1 {
			t.Fatal("expected version 2")
		}
	})
}

func TestWithInstance(t *testing.T) {

}

func TestRedshift_Lock(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.FirstPort()
		if err != nil {
			t.Fatal(err)
		}

		addr := pgConnectionString(ip, port)
		p := &Redshift{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}

		dt.Test(t, d, []byte("SELECT 1"))

		ps := d.(*Redshift)

		err = ps.Lock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Unlock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Lock()
		if err != nil {
			t.Fatal(err)
		}

		err = ps.Unlock()
		if err != nil {
			t.Fatal(err)
		}
	})
}

func Test_computeLineFromPos(t *testing.T) {
	testcases := []struct {
		pos      int
		wantLine uint
		wantCol  uint
		input    string
		wantOk   bool
	}{
		{
			15, 2, 6, "SELECT *\nFROM foo", true, // foo table does not exists
		},
		{
			16, 3, 6, "SELECT *\n\nFROM foo", true, // foo table does not exists, empty line
		},
		{
			25, 3, 7, "SELECT *\nFROM foo\nWHERE x", true, // x column error
		},
		{
			27, 5, 7, "SELECT *\n\nFROM foo\n\nWHERE x", true, // x column error, empty lines
		},
		{
			10, 2, 1, "SELECT *\nFROMM foo", true, // FROMM typo
		},
		{
			11, 3, 1, "SELECT *\n\nFROMM foo", true, // FROMM typo, empty line
		},
		{
			17, 2, 8, "SELECT *\nFROM foo", true, // last character
		},
		{
			18, 0, 0, "SELECT *\nFROM foo", false, // invalid position
		},
	}
	for i, tc := range testcases {
		t.Run("tc"+strconv.Itoa(i), func(t *testing.T) {
			run := func(crlf bool, nonASCII bool) {
				var name string
				if crlf {
					name = "crlf"
				} else {
					name = "lf"
				}
				if nonASCII {
					name += "-nonascii"
				} else {
					name += "-ascii"
				}
				t.Run(name, func(t *testing.T) {
					input := tc.input
					if crlf {
						input = strings.ReplaceAll(input, "\n", "\r\n")
					}
					if nonASCII {
						input = strings.ReplaceAll(input, "FROM", "FRÖM")
					}
					gotLine, gotCol, gotOK := computeLineFromPos(input, tc.pos)

					if tc.wantOk {
						t.Logf("pos %d, want %d:%d, %#v", tc.pos, tc.wantLine, tc.wantCol, input)
					}

					if gotOK != tc.wantOk {
						t.Fatalf("expected ok %v but got %v", tc.wantOk, gotOK)
					}
					if gotLine != tc.wantLine {
						t.Fatalf("expected line %d but got %d", tc.wantLine, gotLine)
					}
					if gotCol != tc.wantCol {
						t.Fatalf("expected col %d but got %d", tc.wantCol, gotCol)
					}
				})
			}
			run(false, false)
			run(true, false)
			run(false, true)
			run(true, true)
		})
	}

}
```

## File: `database/redshift/examples/migrations/1085649617_create_users_table.down.sql`
```sql
DROP TABLE IF EXISTS users;
```

## File: `database/redshift/examples/migrations/1085649617_create_users_table.up.sql`
```sql
CREATE TABLE users (
  user_id integer unique,
  name    varchar(40),
  email   varchar(40)
);
```

## File: `database/redshift/examples/migrations/1185749658_add_city_to_users.down.sql`
```sql
ALTER TABLE users DROP COLUMN IF EXISTS city;
```

## File: `database/redshift/examples/migrations/1185749658_add_city_to_users.up.sql`
```sql
ALTER TABLE users ADD COLUMN city varchar(100);


```

## File: `database/redshift/examples/migrations/1285849751_add_index_on_user_emails.down.sql`
```sql
DROP INDEX IF EXISTS users_email_index;
```

## File: `database/redshift/examples/migrations/1285849751_add_index_on_user_emails.up.sql`
```sql
CREATE UNIQUE INDEX CONCURRENTLY users_email_index ON users (email);

-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/redshift/examples/migrations/1385949617_create_books_table.down.sql`
```sql
DROP TABLE IF EXISTS books;
```

## File: `database/redshift/examples/migrations/1385949617_create_books_table.up.sql`
```sql
CREATE TABLE books (
  user_id integer,
  name    varchar(40),
  author  varchar(40)
);
```

## File: `database/redshift/examples/migrations/1485949617_create_movies_table.down.sql`
```sql
DROP TABLE IF EXISTS movies;
```

## File: `database/redshift/examples/migrations/1485949617_create_movies_table.up.sql`
```sql
CREATE TABLE movies (
  user_id   integer,
  name      varchar(40),
  director  varchar(40)
);
```

## File: `database/redshift/examples/migrations/1585849751_just_a_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/redshift/examples/migrations/1685849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/redshift/examples/migrations/1785849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/redshift/examples/migrations/1885849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/rqlite/README.md`
```markdown
# rqlite

`rqlite://admin:secret@server1.example.com:4001/?level=strong&timeout=5`

The `rqlite` url scheme is used for both secure and insecure connections. If connecting to an insecure database, pass `x-connect-insecure` in your URL query, or use `WithInstance` to pass an established connection.

The migrations table name is configurable through the `x-migrations-table` URL query parameter, or by using `WithInstance` and passing `MigrationsTable` through `Config`.

Other connect parameters are directly passed through to the database driver. For examples of connection strings, see https://github.com/rqlite/gorqlite#examples.

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-connect-insecure` | n/a: set on instance | Boolean to indicate whether to use an insecure connection. Defaults to `false`. |
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table.  Defaults to `schema_migrations`. |

## Notes

* Uses the https://github.com/rqlite/gorqlite driver
```

## File: `database/rqlite/rqlite.go`
```go
package rqlite

import (
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"strconv"
	"strings"
	"sync/atomic"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	"github.com/rqlite/gorqlite"
)

func init() {
	database.Register("rqlite", &Rqlite{})
}

const (
	// DefaultMigrationsTable defines the default rqlite migrations table
	DefaultMigrationsTable = "schema_migrations"

	// DefaultConnectInsecure defines the default setting for connect insecure
	DefaultConnectInsecure = false
)

// ErrNilConfig is returned if no configuration was passed to WithInstance
var ErrNilConfig = fmt.Errorf("no config")

// ErrBadConfig is returned if configuration was invalid
var ErrBadConfig = fmt.Errorf("bad parameter")

// Config defines the driver configuration
type Config struct {
	// ConnectInsecure sets whether the connection uses TLS. Ineffectual when using WithInstance
	ConnectInsecure bool
	// MigrationsTable configures the migrations table name
	MigrationsTable string
}

type Rqlite struct {
	db       *gorqlite.Connection
	isLocked atomic.Bool

	config *Config
}

// WithInstance creates a rqlite database driver with an existing gorqlite database connection
// and a Config struct
func WithInstance(instance *gorqlite.Connection, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	// we use the consistency level check as a database ping
	if _, err := instance.ConsistencyLevel(); err != nil {
		return nil, err
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	driver := &Rqlite{
		db:     instance,
		config: config,
	}

	if err := driver.ensureVersionTable(); err != nil {
		return nil, err
	}

	return driver, nil
}

// OpenURL creates a rqlite database driver from a connect URL
func OpenURL(url string) (database.Driver, error) {
	d := &Rqlite{}
	return d.Open(url)
}

func (r *Rqlite) ensureVersionTable() (err error) {
	if err = r.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := r.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	stmts := []string{
		fmt.Sprintf(`CREATE TABLE IF NOT EXISTS %s (version uint64, dirty bool)`, r.config.MigrationsTable),
		fmt.Sprintf(`CREATE UNIQUE INDEX IF NOT EXISTS version_unique ON %s (version)`, r.config.MigrationsTable),
	}

	if _, err := r.db.Write(stmts); err != nil {
		return err
	}

	return nil
}

// Open returns a new driver instance configured with parameters
// coming from the URL string. Migrate will call this function
// only once per instance.
func (r *Rqlite) Open(url string) (database.Driver, error) {
	dburl, config, err := parseUrl(url)
	if err != nil {
		return nil, err
	}
	r.config = config

	r.db, err = gorqlite.Open(dburl.String())
	if err != nil {
		return nil, err
	}

	if err := r.ensureVersionTable(); err != nil {
		return nil, err
	}

	return r, nil
}

// Close closes the underlying database instance managed by the driver.
// Migrate will call this function only once per instance.
func (r *Rqlite) Close() error {
	r.db.Close()
	return nil
}

// Lock should acquire a database lock so that only one migration process
// can run at a time. Migrate will call this function before Run is called.
// If the implementation can't provide this functionality, return nil.
// Return database.ErrLocked if database is already locked.
func (r *Rqlite) Lock() error {
	if !r.isLocked.CompareAndSwap(false, true) {
		return database.ErrLocked
	}
	return nil
}

// Unlock should release the lock. Migrate will call this function after
// all migrations have been run.
func (r *Rqlite) Unlock() error {
	if !r.isLocked.CompareAndSwap(true, false) {
		return database.ErrNotLocked
	}
	return nil
}

// Run applies a migration to the database. migration is guaranteed to be not nil.
func (r *Rqlite) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}

	query := string(migr[:])
	if _, err := r.db.WriteOne(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}

// SetVersion saves version and dirty state.
// Migrate will call this function before and after each call to Run.
// version must be >= -1. -1 means NilVersion.
func (r *Rqlite) SetVersion(version int, dirty bool) error {
	deleteQuery := fmt.Sprintf(`DELETE FROM %s`, r.config.MigrationsTable)
	statements := []gorqlite.ParameterizedStatement{
		{
			Query: deleteQuery,
		},
	}

	// Also re-write the schema version for nil dirty versions to prevent
	// empty schema version for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330
	insertQuery := fmt.Sprintf(`INSERT INTO %s (version, dirty) VALUES (?, ?)`, r.config.MigrationsTable)
	if version >= 0 || (version == database.NilVersion && dirty) {
		statements = append(statements, gorqlite.ParameterizedStatement{
			Query: insertQuery,
			Arguments: []interface{}{
				version,
				dirty,
			},
		})
	}

	wr, err := r.db.WriteParameterized(statements)
	if err != nil {
		for i, res := range wr {
			if res.Err != nil {
				return &database.Error{OrigErr: err, Query: []byte(statements[i].Query)}
			}
		}

		// if somehow we're still here, return the original error with combined queries
		return &database.Error{OrigErr: err, Query: []byte(deleteQuery + "\n" + insertQuery)}
	}

	return nil
}

// Version returns the currently active version and if the database is dirty.
// When no migration has been applied, it must return version -1.
// Dirty means, a previous migration failed and user interaction is required.
func (r *Rqlite) Version() (version int, dirty bool, err error) {
	query := "SELECT version, dirty FROM " + r.config.MigrationsTable + " LIMIT 1"

	qr, err := r.db.QueryOne(query)
	if err != nil {
		return database.NilVersion, false, nil
	}

	if !qr.Next() {
		return database.NilVersion, false, nil
	}

	if err := qr.Scan(&version, &dirty); err != nil {
		return database.NilVersion, false, &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return version, dirty, nil
}

// Drop deletes everything in the database.
// Note that this is a breaking action, a new call to Open() is necessary to
// ensure subsequent calls work as expected.
func (r *Rqlite) Drop() error {
	query := `SELECT name FROM sqlite_master WHERE type = 'table'`

	tables, err := r.db.QueryOne(query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	statements := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}

		if len(tableName) > 0 {
			statement := fmt.Sprintf(`DROP TABLE %s`, tableName)
			statements = append(statements, statement)
		}
	}

	// return if nothing to do
	if len(statements) <= 0 {
		return nil
	}

	wr, err := r.db.Write(statements)
	if err != nil {
		for i, res := range wr {
			if res.Err != nil {
				return &database.Error{OrigErr: err, Query: []byte(statements[i])}
			}
		}

		// if somehow we're still here, return the original error with combined queries
		return &database.Error{OrigErr: err, Query: []byte(strings.Join(statements, "\n"))}
	}

	return nil
}

func parseUrl(url string) (*nurl.URL, *Config, error) {
	parsedUrl, err := nurl.Parse(url)
	if err != nil {
		return nil, nil, err
	}

	config, err := parseConfigFromQuery(parsedUrl.Query())
	if err != nil {
		return nil, nil, err
	}

	if parsedUrl.Scheme != "rqlite" {
		return nil, nil, fmt.Errorf("bad scheme: %w", ErrBadConfig)
	}

	// adapt from rqlite to http/https schemes
	if config.ConnectInsecure {
		parsedUrl.Scheme = "http"
	} else {
		parsedUrl.Scheme = "https"
	}

	filteredUrl := migrate.FilterCustomQuery(parsedUrl)

	return filteredUrl, config, nil
}

func parseConfigFromQuery(queryVals nurl.Values) (*Config, error) {
	c := Config{
		ConnectInsecure: DefaultConnectInsecure,
		MigrationsTable: DefaultMigrationsTable,
	}

	migrationsTable := queryVals.Get("x-migrations-table")
	if migrationsTable != "" {
		if strings.HasPrefix(migrationsTable, "sqlite_") {
			return nil, fmt.Errorf("invalid value for x-migrations-table: %w", ErrBadConfig)
		}
		c.MigrationsTable = migrationsTable
	}

	connectInsecureStr := queryVals.Get("x-connect-insecure")
	if connectInsecureStr != "" {
		connectInsecure, err := strconv.ParseBool(connectInsecureStr)
		if err != nil {
			return nil, fmt.Errorf("invalid value for x-connect-insecure: %w", ErrBadConfig)
		}
		c.ConnectInsecure = connectInsecure
	}

	return &c, nil
}
```

## File: `database/rqlite/rqlite_test.go`
```go
package rqlite

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"testing"

	"github.com/dhui/dktest"
	"github.com/rqlite/gorqlite"
	"github.com/stretchr/testify/assert"

	"github.com/golang-migrate/migrate/v4"
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

var defaultPort uint16 = 4001

var opts = dktest.Options{
	Env:          map[string]string{"NODE_ID": "1"},
	PortRequired: true,
	ReadyFunc:    isReady,
}
var specs = []dktesting.ContainerSpec{
	{ImageName: "rqlite/rqlite:7.21.4", Options: opts},
	{ImageName: "rqlite/rqlite:8.0.6", Options: opts},
	{ImageName: "rqlite/rqlite:8.11.1", Options: opts},
	{ImageName: "rqlite/rqlite:8.12.3", Options: opts},
}

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	ip, port, err := c.Port(defaultPort)
	if err != nil {
		fmt.Println("error getting port")
		return false
	}

	statusString := fmt.Sprintf("http://%s:%s/status", ip, port)
	fmt.Println(statusString)

	var readyResp struct {
		Store struct {
			Ready bool `json:"ready"`
		} `json:"store"`
	}

	resp, err := http.Get(statusString)
	if err != nil {
		fmt.Println("error getting status")
		return false
	}

	if resp.StatusCode != 200 {
		fmt.Println("statusCode != 200")
		return false
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("error reading body")
		return false
	}

	if err := json.Unmarshal(body, &readyResp); err != nil {
		fmt.Println("error unmarshaling body")
		return false
	}

	return readyResp.Store.Ready
}

func Test(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		assert.NoError(t, err)

		connectString := fmt.Sprintf("rqlite://%s:%s?level=strong&disableClusterDiscovery=true&x-connect-insecure=true", ip, port)
		t.Logf("DB connect string : %s\n", connectString)

		r := &Rqlite{}
		d, err := r.Open(connectString)
		assert.NoError(t, err)

		dt.Test(t, d, []byte("CREATE TABLE t (Qty int, Name string);"))
	})
}

func TestMigrate(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		assert.NoError(t, err)

		connectString := fmt.Sprintf("rqlite://%s:%s?level=strong&disableClusterDiscovery=true&x-connect-insecure=true", ip, port)
		t.Logf("DB connect string : %s\n", connectString)

		driver, err := OpenURL(connectString)
		assert.NoError(t, err)
		defer func() {
			if err := driver.Close(); err != nil {
				return
			}
		}()

		m, err := migrate.NewWithDatabaseInstance(
			"file://./examples/migrations",
			"ql", driver)
		assert.NoError(t, err)

		dt.TestMigrate(t, m)
	})
}

func TestBadConnectInsecureParam(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		assert.NoError(t, err)

		connectString := fmt.Sprintf("rqlite://%s:%s?x-connect-insecure=foo", ip, port)
		t.Logf("DB connect string : %s\n", connectString)

		_, err = OpenURL(connectString)
		assert.ErrorIs(t, err, ErrBadConfig)
	})
}

func TestBadProtocol(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		assert.NoError(t, err)

		connectString := fmt.Sprintf("postgres://%s:%s/database", ip, port)
		t.Logf("DB connect string : %s\n", connectString)

		_, err = OpenURL(connectString)
		assert.ErrorIs(t, err, ErrBadConfig)
	})
}

func TestNoConfig(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		assert.NoError(t, err)

		// gorqlite expects http(s) schemes
		connectString := fmt.Sprintf("http://%s:%s?level=strong&disableClusterDiscovery=true", ip, port)
		t.Logf("DB connect string : %s\n", connectString)
		db, err := gorqlite.Open(connectString)
		assert.NoError(t, err)

		_, err = WithInstance(db, nil)
		assert.ErrorIs(t, err, ErrNilConfig)
	})
}

func TestWithInstanceEmptyConfig(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		assert.NoError(t, err)

		// gorqlite expects http(s) schemes
		connectString := fmt.Sprintf("http://%s:%s?level=strong&disableClusterDiscovery=true", ip, port)
		t.Logf("DB connect string : %s\n", connectString)
		db, err := gorqlite.Open(connectString)
		assert.NoError(t, err)

		driver, err := WithInstance(db, &Config{})
		assert.NoError(t, err)

		defer func() {
			if err := driver.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		m, err := migrate.NewWithDatabaseInstance(
			"file://./examples/migrations",
			"ql", driver)
		assert.NoError(t, err)

		t.Log("UP")
		err = m.Up()
		assert.NoError(t, err)

		_, err = db.QueryOne(fmt.Sprintf("SELECT * FROM %s", DefaultMigrationsTable))
		assert.NoError(t, err)

		t.Log("DOWN")
		err = m.Down()
		assert.NoError(t, err)
	})
}

func TestMigrationTable(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		ip, port, err := c.Port(defaultPort)
		assert.NoError(t, err)

		// gorqlite expects http(s) schemes
		connectString := fmt.Sprintf("http://%s:%s?level=strong&disableClusterDiscovery=true", ip, port)
		t.Logf("DB connect string : %s\n", connectString)
		db, err := gorqlite.Open(connectString)
		assert.NoError(t, err)

		config := Config{MigrationsTable: "my_migration_table"}
		driver, err := WithInstance(db, &config)
		assert.NoError(t, err)

		defer func() {
			if err := driver.Close(); err != nil {
				t.Fatal(err)
			}
		}()

		m, err := migrate.NewWithDatabaseInstance(
			"file://./examples/migrations",
			"ql", driver)
		assert.NoError(t, err)

		t.Log("UP")
		err = m.Up()
		assert.NoError(t, err)

		_, err = db.QueryOne(fmt.Sprintf("SELECT * FROM %s", config.MigrationsTable))
		assert.NoError(t, err)

		_, err = db.WriteOne(`INSERT INTO pets (name, predator) VALUES ("franklin", true)`)
		assert.NoError(t, err)

		res, err := db.QueryOne(`SELECT name, predator FROM pets LIMIT 1`)
		assert.NoError(t, err)

		_ = res.Next()

		// make sure we can use the migrated table
		var petName string
		var petPredator int
		err = res.Scan(&petName, &petPredator)
		assert.NoError(t, err)
		assert.Equal(t, petName, "franklin")
		assert.Equal(t, petPredator, 1)

		t.Log("DOWN")
		err = m.Down()
		assert.NoError(t, err)

		_, err = db.QueryOne(fmt.Sprintf("SELECT * FROM %s", config.MigrationsTable))
		assert.NoError(t, err)
	})
}

func TestParseUrl(t *testing.T) {
	tests := []struct {
		name           string
		passedUrl      string
		expectedUrl    string
		expectedConfig *Config
		expectedErr    string
	}{
		{
			"defaults",
			"rqlite://localhost:4001",
			"https://localhost:4001",
			&Config{ConnectInsecure: DefaultConnectInsecure, MigrationsTable: DefaultMigrationsTable},
			"",
		},
		{
			"configure migration table",
			"rqlite://localhost:4001?x-migrations-table=foo",
			"https://localhost:4001",
			&Config{ConnectInsecure: DefaultConnectInsecure, MigrationsTable: "foo"},
			"",
		},
		{
			"configure connect insecure",
			"rqlite://localhost:4001?x-connect-insecure=true",
			"http://localhost:4001",
			&Config{ConnectInsecure: true, MigrationsTable: DefaultMigrationsTable},
			"",
		},
		{
			"invalid migration table",
			"rqlite://localhost:4001?x-migrations-table=sqlite_bar",
			"",
			nil,
			"invalid value for x-migrations-table: bad parameter",
		},
		{
			"invalid connect insecure",
			"rqlite://localhost:4001?x-connect-insecure=baz",
			"",
			nil,
			"invalid value for x-connect-insecure: bad parameter",
		},
		{
			"invalid url",
			string([]byte{0x7f}),
			"",
			nil,
			"parse \"\\x7f\": net/url: invalid control character in URL",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			actualUrl, actualConfig, actualErr := parseUrl(tt.passedUrl)
			if tt.expectedUrl != "" {
				assert.Equal(t, tt.expectedUrl, actualUrl.String())
			} else {
				assert.Nil(t, actualUrl)
			}

			assert.Equal(t, tt.expectedConfig, actualConfig)

			if tt.expectedErr == "" {
				assert.NoError(t, actualErr)
			} else {
				assert.EqualError(t, actualErr, tt.expectedErr)
			}
		})
	}
}
```

## File: `database/rqlite/examples/migrations/33_create_table.down.sql`
```sql
DROP TABLE IF EXISTS pets;
```

## File: `database/rqlite/examples/migrations/33_create_table.up.sql`
```sql
CREATE TABLE pets (
  name string
);
```

## File: `database/rqlite/examples/migrations/44_alter_table.down.sql`
```sql
DROP TABLE IF EXISTS pets;
```

## File: `database/rqlite/examples/migrations/44_alter_table.up.sql`
```sql
ALTER TABLE pets ADD predator bool;
```

## File: `database/snowflake/README.md`
```markdown
# Snowflake

`snowflake://user:password@accountname/schema/dbname?query`

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table |

Snowflake is PostgreSQL compatible but has some specific features (or lack thereof) that require slightly different behavior.

## Status
This driver is not officially supported as there are no tests for it.
```

## File: `database/snowflake/snowflake.go`
```go
package snowflake

import (
	"context"
	"database/sql"
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"strconv"
	"strings"
	"sync/atomic"

	"github.com/golang-migrate/migrate/v4/database"
	"github.com/lib/pq"
	sf "github.com/snowflakedb/gosnowflake"
)

func init() {
	db := Snowflake{}
	database.Register("snowflake", &db)
}

var DefaultMigrationsTable = "schema_migrations"

var (
	ErrNilConfig          = fmt.Errorf("no config")
	ErrNoDatabaseName     = fmt.Errorf("no database name")
	ErrNoPassword         = fmt.Errorf("no password")
	ErrNoSchema           = fmt.Errorf("no schema")
	ErrNoSchemaOrDatabase = fmt.Errorf("no schema/database name")
)

type Config struct {
	MigrationsTable string
	DatabaseName    string
}

type Snowflake struct {
	isLocked atomic.Bool
	conn     *sql.Conn
	db       *sql.DB

	// Open and WithInstance need to guarantee that config is never nil
	config *Config
}

func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	if config.DatabaseName == "" {
		query := `SELECT CURRENT_DATABASE()`
		var databaseName string
		if err := instance.QueryRow(query).Scan(&databaseName); err != nil {
			return nil, &database.Error{OrigErr: err, Query: []byte(query)}
		}

		if len(databaseName) == 0 {
			return nil, ErrNoDatabaseName
		}

		config.DatabaseName = databaseName
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	conn, err := instance.Conn(context.Background())

	if err != nil {
		return nil, err
	}

	px := &Snowflake{
		conn:   conn,
		db:     instance,
		config: config,
	}

	if err := px.ensureVersionTable(); err != nil {
		return nil, err
	}

	return px, nil
}

func (p *Snowflake) Open(url string) (database.Driver, error) {
	purl, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}

	password, isPasswordSet := purl.User.Password()
	if !isPasswordSet {
		return nil, ErrNoPassword
	}

	splitPath := strings.Split(purl.Path, "/")
	if len(splitPath) < 3 {
		return nil, ErrNoSchemaOrDatabase
	}

	database := splitPath[2]
	if len(database) == 0 {
		return nil, ErrNoDatabaseName
	}

	schema := splitPath[1]
	if len(schema) == 0 {
		return nil, ErrNoSchema
	}

	cfg := &sf.Config{
		Account:  purl.Host,
		User:     purl.User.Username(),
		Password: password,
		Database: database,
		Schema:   schema,
	}

	dsn, err := sf.DSN(cfg)
	if err != nil {
		return nil, err
	}

	db, err := sql.Open("snowflake", dsn)
	if err != nil {
		return nil, err
	}

	migrationsTable := purl.Query().Get("x-migrations-table")

	px, err := WithInstance(db, &Config{
		DatabaseName:    database,
		MigrationsTable: migrationsTable,
	})
	if err != nil {
		return nil, err
	}

	return px, nil
}

func (p *Snowflake) Close() error {
	connErr := p.conn.Close()
	dbErr := p.db.Close()
	if connErr != nil || dbErr != nil {
		return fmt.Errorf("conn: %v, db: %v", connErr, dbErr)
	}
	return nil
}

func (p *Snowflake) Lock() error {
	if !p.isLocked.CompareAndSwap(false, true) {
		return database.ErrLocked
	}
	return nil
}

func (p *Snowflake) Unlock() error {
	if !p.isLocked.CompareAndSwap(true, false) {
		return database.ErrNotLocked
	}
	return nil
}

func (p *Snowflake) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}

	// run migration
	query := string(migr[:])
	if _, err := p.conn.ExecContext(context.Background(), query); err != nil {
		if pgErr, ok := err.(*pq.Error); ok {
			var line uint
			var col uint
			var lineColOK bool
			if pgErr.Position != "" {
				if pos, err := strconv.ParseUint(pgErr.Position, 10, 64); err == nil {
					line, col, lineColOK = computeLineFromPos(query, int(pos))
				}
			}
			message := fmt.Sprintf("migration failed: %s", pgErr.Message)
			if lineColOK {
				message = fmt.Sprintf("%s (column %d)", message, col)
			}
			if pgErr.Detail != "" {
				message = fmt.Sprintf("%s, %s", message, pgErr.Detail)
			}
			return database.Error{OrigErr: err, Err: message, Query: migr, Line: line}
		}
		return database.Error{OrigErr: err, Err: "migration failed", Query: migr}
	}

	return nil
}

func computeLineFromPos(s string, pos int) (line uint, col uint, ok bool) {
	// replace crlf with lf
	s = strings.ReplaceAll(s, "\r\n", "\n")
	// pg docs: pos uses index 1 for the first character, and positions are measured in characters not bytes
	runes := []rune(s)
	if pos > len(runes) {
		return 0, 0, false
	}
	sel := runes[:pos]
	line = uint(runesCount(sel, newLine) + 1)
	col = uint(pos - 1 - runesLastIndex(sel, newLine))
	return line, col, true
}

const newLine = '\n'

func runesCount(input []rune, target rune) int {
	var count int
	for _, r := range input {
		if r == target {
			count++
		}
	}
	return count
}

func runesLastIndex(input []rune, target rune) int {
	for i := len(input) - 1; i >= 0; i-- {
		if input[i] == target {
			return i
		}
	}
	return -1
}

func (p *Snowflake) SetVersion(version int, dirty bool) error {
	tx, err := p.conn.BeginTx(context.Background(), &sql.TxOptions{})
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}

	query := `DELETE FROM "` + p.config.MigrationsTable + `"`
	if _, err := tx.Exec(query); err != nil {
		if errRollback := tx.Rollback(); errRollback != nil {
			err = errors.Join(err, errRollback)
		}
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	// Also re-write the schema version for nil dirty versions to prevent
	// empty schema version for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330
	if version >= 0 || (version == database.NilVersion && dirty) {
		query = `INSERT INTO "` + p.config.MigrationsTable + `" (version,
				dirty) VALUES (` + strconv.FormatInt(int64(version), 10) + `,
				` + strconv.FormatBool(dirty) + `)`
		if _, err := tx.Exec(query); err != nil {
			if errRollback := tx.Rollback(); errRollback != nil {
				err = errors.Join(err, errRollback)
			}
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}

	return nil
}

func (p *Snowflake) Version() (version int, dirty bool, err error) {
	query := `SELECT version, dirty FROM "` + p.config.MigrationsTable + `" LIMIT 1`
	err = p.conn.QueryRowContext(context.Background(), query).Scan(&version, &dirty)
	switch {
	case err == sql.ErrNoRows:
		return database.NilVersion, false, nil

	case err != nil:
		if e, ok := err.(*pq.Error); ok {
			if e.Code.Name() == "undefined_table" {
				return database.NilVersion, false, nil
			}
		}
		return 0, false, &database.Error{OrigErr: err, Query: []byte(query)}

	default:
		return version, dirty, nil
	}
}

func (p *Snowflake) Drop() (err error) {
	// select all tables in current schema
	query := `SELECT table_name FROM information_schema.tables WHERE table_schema=(SELECT current_schema()) AND table_type='BASE TABLE'`
	tables, err := p.conn.QueryContext(context.Background(), query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	// delete one table after another
	tableNames := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}
		if len(tableName) > 0 {
			tableNames = append(tableNames, tableName)
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if len(tableNames) > 0 {
		// delete one by one ...
		for _, t := range tableNames {
			query = `DROP TABLE IF EXISTS ` + t + ` CASCADE`
			if _, err := p.conn.ExecContext(context.Background(), query); err != nil {
				return &database.Error{OrigErr: err, Query: []byte(query)}
			}
		}
	}

	return nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the Snowflake type.
func (p *Snowflake) ensureVersionTable() (err error) {
	if err = p.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := p.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	// check if migration table exists
	var count int
	query := `SELECT COUNT(1) FROM information_schema.tables WHERE table_name = $1 AND table_schema = (SELECT current_schema()) LIMIT 1`
	if err := p.conn.QueryRowContext(context.Background(), query, p.config.MigrationsTable).Scan(&count); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	if count == 1 {
		return nil
	}

	// if not, create the empty migration table
	query = `CREATE TABLE if not exists "` + p.config.MigrationsTable + `" (
			version bigint not null primary key, dirty boolean not null)`
	if _, err := p.conn.ExecContext(context.Background(), query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}
```

## File: `database/spanner/README.md`
```markdown
# Google Cloud Spanner

## Usage

See [Google Spanner Documentation](https://cloud.google.com/spanner/docs) for
more details.

The DSN must be given in the following format.

`spanner://projects/{projectId}/instances/{instanceId}/databases/{databaseName}?param=true`

as described in [README.md#database-urls](../../../README.md#database-urls)

| Param | WithInstance Config | Description |
| ----- | ------------------- | ----------- |
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table |
| `x-clean-statements` | `CleanStatements` | Whether to parse and clean DDL statements before running migration towards Spanner (Required for comments and multiple statements) |
| `url` | `DatabaseName` | The full path to the Spanner database resource. If provided as part of `Config` it must not contain a scheme or query string to match the format `projects/{projectId}/instances/{instanceId}/databases/{databaseName}`|
| `projectId` || The Google Cloud Platform project id
| `instanceId` || The id of the instance running Spanner
| `databaseName` || The name of the Spanner database

> **Note:** Google Cloud Spanner migrations can take a considerable amount of 
> time. The migrations provided as part of the example take about 6 minutes to 
> run on a small instance.
>
> ```log
> 1481574547/u create_users_table (21.354507597s)
> 1496539702/u add_city_to_users (41.647359754s)
> 1496601752/u add_index_on_user_emails (2m12.155787369s)
> 1496602638/u create_books_table (2m30.77299181s)

## DDL with comments

At the moment the GCP Spanner backed does not seem to allow for comments (See https://issuetracker.google.com/issues/159730604)
so in order to be able to use migration with DDL containing comments `x-clean-statements` is required

## Multiple statements

In order to be able to use more than 1 DDL statement in the same migration file, the file has to be parsed and therefore the `x-clean-statements` flag is required

## Testing

To unit test the `spanner` driver, `SPANNER_DATABASE` needs to be set. You'll
need to sign-up to Google Cloud Platform (GCP) and have a running Spanner
instance since it is not possible to run Google Spanner outside GCP.
```

## File: `database/spanner/spanner.go`
```go
package spanner

import (
	"context"
	"errors"
	"fmt"
	"io"
	"log"
	nurl "net/url"
	"regexp"
	"strconv"
	"strings"
	"sync/atomic"

	"cloud.google.com/go/spanner"
	sdb "cloud.google.com/go/spanner/admin/database/apiv1"
	"cloud.google.com/go/spanner/spansql"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"

	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
	"google.golang.org/api/iterator"
)

func init() {
	db := Spanner{}
	database.Register("spanner", &db)
}

// DefaultMigrationsTable is used if no custom table is specified
const DefaultMigrationsTable = "SchemaMigrations"

// Driver errors
var (
	ErrNilConfig      = errors.New("no config")
	ErrNoDatabaseName = errors.New("no database name")
	ErrNoSchema       = errors.New("no schema")
	ErrDatabaseDirty  = errors.New("database is dirty")
	ErrLockHeld       = errors.New("unable to obtain lock")
	ErrLockNotHeld    = errors.New("unable to release already released lock")
)

// Config used for a Spanner instance
type Config struct {
	MigrationsTable string
	DatabaseName    string
	// Whether to parse the migration DDL with spansql before
	// running them towards Spanner.
	// Parsing outputs clean DDL statements such as reformatted
	// and void of comments.
	CleanStatements bool
}

// Spanner implements database.Driver for Google Cloud Spanner
type Spanner struct {
	db *DB

	config *Config

	lock atomic.Bool
}

type DB struct {
	admin *sdb.DatabaseAdminClient
	data  *spanner.Client
}

func NewDB(admin sdb.DatabaseAdminClient, data spanner.Client) *DB {
	return &DB{
		admin: &admin,
		data:  &data,
	}
}

// WithInstance implements database.Driver
func WithInstance(instance *DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if len(config.DatabaseName) == 0 {
		return nil, ErrNoDatabaseName
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	sx := &Spanner{
		db:     instance,
		config: config,
	}

	if err := sx.ensureVersionTable(); err != nil {
		return nil, err
	}

	return sx, nil
}

// Open implements database.Driver
func (s *Spanner) Open(url string) (database.Driver, error) {
	purl, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}

	ctx := context.Background()

	adminClient, err := sdb.NewDatabaseAdminClient(ctx)
	if err != nil {
		return nil, err
	}
	dbname := strings.Replace(migrate.FilterCustomQuery(purl).String(), "spanner://", "", 1)
	dataClient, err := spanner.NewClient(ctx, dbname)
	if err != nil {
		log.Fatal(err)
	}

	migrationsTable := purl.Query().Get("x-migrations-table")

	cleanQuery := purl.Query().Get("x-clean-statements")
	clean := false
	if cleanQuery != "" {
		clean, err = strconv.ParseBool(cleanQuery)
		if err != nil {
			return nil, err
		}
	}

	db := &DB{admin: adminClient, data: dataClient}
	return WithInstance(db, &Config{
		DatabaseName:    dbname,
		MigrationsTable: migrationsTable,
		CleanStatements: clean,
	})
}

// Close implements database.Driver
func (s *Spanner) Close() error {
	s.db.data.Close()
	return s.db.admin.Close()
}

// Lock implements database.Driver but doesn't do anything because Spanner only
// enqueues the UpdateDatabaseDdlRequest.
func (s *Spanner) Lock() error {
	if swapped := s.lock.CompareAndSwap(false, true); swapped {
		return nil
	}
	return ErrLockHeld
}

// Unlock implements database.Driver but no action required, see Lock.
func (s *Spanner) Unlock() error {
	if swapped := s.lock.CompareAndSwap(true, false); swapped {
		return nil
	}
	return ErrLockNotHeld
}

// Run implements database.Driver
func (s *Spanner) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}

	stmts := []string{string(migr)}
	if s.config.CleanStatements {
		stmts, err = cleanStatements(migr)
		if err != nil {
			return err
		}
	}

	ctx := context.Background()
	op, err := s.db.admin.UpdateDatabaseDdl(ctx, &adminpb.UpdateDatabaseDdlRequest{
		Database:   s.config.DatabaseName,
		Statements: stmts,
	})

	if err != nil {
		return &database.Error{OrigErr: err, Err: "migration failed", Query: migr}
	}

	if err := op.Wait(ctx); err != nil {
		return &database.Error{OrigErr: err, Err: "migration failed", Query: migr}
	}

	return nil
}

// SetVersion implements database.Driver
func (s *Spanner) SetVersion(version int, dirty bool) error {
	ctx := context.Background()

	_, err := s.db.data.ReadWriteTransaction(ctx,
		func(ctx context.Context, txn *spanner.ReadWriteTransaction) error {
			m := []*spanner.Mutation{
				spanner.Delete(s.config.MigrationsTable, spanner.AllKeys()),
				spanner.Insert(s.config.MigrationsTable,
					[]string{"Version", "Dirty"},
					[]interface{}{version, dirty},
				)}
			return txn.BufferWrite(m)
		})
	if err != nil {
		return &database.Error{OrigErr: err}
	}

	return nil
}

// Version implements database.Driver
func (s *Spanner) Version() (version int, dirty bool, err error) {
	ctx := context.Background()

	stmt := spanner.Statement{
		SQL: `SELECT Version, Dirty FROM ` + s.config.MigrationsTable + ` LIMIT 1`,
	}
	iter := s.db.data.Single().Query(ctx, stmt)
	defer iter.Stop()

	row, err := iter.Next()
	switch err {
	case iterator.Done:
		return database.NilVersion, false, nil
	case nil:
		var v int64
		if err = row.Columns(&v, &dirty); err != nil {
			return 0, false, &database.Error{OrigErr: err, Query: []byte(stmt.SQL)}
		}
		version = int(v)
	default:
		return 0, false, &database.Error{OrigErr: err, Query: []byte(stmt.SQL)}
	}

	return version, dirty, nil
}

var nameMatcher = regexp.MustCompile(`(CREATE TABLE\s(\S+)\s)|(CREATE.+INDEX\s(\S+)\s)`)

// Drop implements database.Driver. Retrieves the database schema first and
// creates statements to drop the indexes and tables accordingly.
// Note: The drop statements are created in reverse order to how they're
// provided in the schema. Assuming the schema describes how the database can
// be "build up", it seems logical to "unbuild" the database simply by going the
// opposite direction. More testing
func (s *Spanner) Drop() error {
	ctx := context.Background()
	res, err := s.db.admin.GetDatabaseDdl(ctx, &adminpb.GetDatabaseDdlRequest{
		Database: s.config.DatabaseName,
	})
	if err != nil {
		return &database.Error{OrigErr: err, Err: "drop failed"}
	}
	if len(res.Statements) == 0 {
		return nil
	}

	stmts := make([]string, 0)
	for i := len(res.Statements) - 1; i >= 0; i-- {
		s := res.Statements[i]
		m := nameMatcher.FindSubmatch([]byte(s))

		if len(m) == 0 {
			continue
		} else if tbl := m[2]; len(tbl) > 0 {
			stmts = append(stmts, fmt.Sprintf(`DROP TABLE %s`, tbl))
		} else if idx := m[4]; len(idx) > 0 {
			stmts = append(stmts, fmt.Sprintf(`DROP INDEX %s`, idx))
		}
	}

	op, err := s.db.admin.UpdateDatabaseDdl(ctx, &adminpb.UpdateDatabaseDdlRequest{
		Database:   s.config.DatabaseName,
		Statements: stmts,
	})
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(strings.Join(stmts, "; "))}
	}
	if err := op.Wait(ctx); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(strings.Join(stmts, "; "))}
	}

	return nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the Spanner type.
func (s *Spanner) ensureVersionTable() (err error) {
	if err = s.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := s.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	ctx := context.Background()
	tbl := s.config.MigrationsTable
	iter := s.db.data.Single().Read(ctx, tbl, spanner.AllKeys(), []string{"Version"})
	if err := iter.Do(func(r *spanner.Row) error { return nil }); err == nil {
		return nil
	}

	stmt := fmt.Sprintf(`CREATE TABLE %s (
    Version INT64 NOT NULL,
    Dirty    BOOL NOT NULL
	) PRIMARY KEY(Version)`, tbl)

	op, err := s.db.admin.UpdateDatabaseDdl(ctx, &adminpb.UpdateDatabaseDdlRequest{
		Database:   s.config.DatabaseName,
		Statements: []string{stmt},
	})

	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(stmt)}
	}
	if err := op.Wait(ctx); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(stmt)}
	}

	return nil
}

func cleanStatements(migration []byte) ([]string, error) {
	// The Spanner GCP backend does not yet support comments for the UpdateDatabaseDdl RPC
	// (see https://issuetracker.google.com/issues/159730604) we use
	// spansql to parse the DDL and output valid stamements without comments
	ddl, err := spansql.ParseDDL("", string(migration))
	if err != nil {
		return nil, err
	}
	stmts := make([]string, 0, len(ddl.List))
	for _, stmt := range ddl.List {
		stmts = append(stmts, stmt.SQL())
	}
	return stmts, nil
}
```

## File: `database/spanner/spanner_test.go`
```go
package spanner

import (
	"fmt"
	"os"
	"testing"

	"github.com/golang-migrate/migrate/v4"

	dt "github.com/golang-migrate/migrate/v4/database/testing"
	_ "github.com/golang-migrate/migrate/v4/source/file"

	"cloud.google.com/go/spanner/spannertest"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

// withSpannerEmulator is not thread-safe and cannot be used with parallel tests since it sets the emulator
func withSpannerEmulator(t *testing.T, testFunc func(t *testing.T)) {
	t.Helper()
	srv, err := spannertest.NewServer("localhost:0")
	if err != nil {
		t.Fatal("Failed to create Spanner emulator:", err)
	}
	// This is not thread-safe
	if err := os.Setenv("SPANNER_EMULATOR_HOST", srv.Addr); err != nil {
		t.Fatal("Failed to set SPANNER_EMULATOR_HOST env var:", err)
	}
	defer srv.Close()
	testFunc(t)

}

const db = "projects/abc/instances/def/databases/testdb"

func Test(t *testing.T) {
	withSpannerEmulator(t, func(t *testing.T) {
		uri := fmt.Sprintf("spanner://%s", db)
		s := &Spanner{}
		d, err := s.Open(uri)
		if err != nil {
			t.Fatal(err)
		}
		dt.Test(t, d, []byte("CREATE TABLE test (id BOOL) PRIMARY KEY (id)"))
	})
}

func TestMigrate(t *testing.T) {
	withSpannerEmulator(t, func(t *testing.T) {
		s := &Spanner{}
		uri := fmt.Sprintf("spanner://%s", db)
		d, err := s.Open(uri)
		if err != nil {
			t.Fatal(err)
		}
		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", uri, d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}

func TestCleanStatements(t *testing.T) {
	testCases := []struct {
		name           string
		multiStatement string
		expected       []string
	}{
		{
			name:           "no statement",
			multiStatement: "",
			expected:       []string{},
		},
		{
			name:           "single statement, single line, no semicolon, no comment",
			multiStatement: "CREATE TABLE table_name (id STRING(255) NOT NULL) PRIMARY KEY (id)",
			expected:       []string{"CREATE TABLE table_name (\n  id STRING(255) NOT NULL,\n) PRIMARY KEY(id)"},
		},
		{
			name: "single statement, multi line, no semicolon, no comment",
			multiStatement: `CREATE TABLE table_name (
			id STRING(255) NOT NULL,
		) PRIMARY KEY (id)`,
			expected: []string{"CREATE TABLE table_name (\n  id STRING(255) NOT NULL,\n) PRIMARY KEY(id)"},
		},
		{
			name:           "single statement, single line, with semicolon, no comment",
			multiStatement: "CREATE TABLE table_name (id STRING(255) NOT NULL) PRIMARY KEY (id);",
			expected:       []string{"CREATE TABLE table_name (\n  id STRING(255) NOT NULL,\n) PRIMARY KEY(id)"},
		},
		{
			name: "single statement, multi line, with semicolon, no comment",
			multiStatement: `CREATE TABLE table_name (
			id STRING(255) NOT NULL,
		) PRIMARY KEY (id);`,
			expected: []string{"CREATE TABLE table_name (\n  id STRING(255) NOT NULL,\n) PRIMARY KEY(id)"},
		},
		{
			name: "multi statement, with trailing semicolon. no comment",
			// From https://github.com/mattes/migrate/pull/281
			multiStatement: `CREATE TABLE table_name (
			id STRING(255) NOT NULL,
		) PRIMARY KEY(id);

		CREATE INDEX table_name_id_idx ON table_name (id);`,
			expected: []string{`CREATE TABLE table_name (
  id STRING(255) NOT NULL,
) PRIMARY KEY(id)`, "CREATE INDEX table_name_id_idx ON table_name(id)"},
		},
		{
			name: "multi statement, no trailing semicolon, no comment",
			// From https://github.com/mattes/migrate/pull/281
			multiStatement: `CREATE TABLE table_name (
			id STRING(255) NOT NULL,
		) PRIMARY KEY(id);

		CREATE INDEX table_name_id_idx ON table_name (id)`,
			expected: []string{`CREATE TABLE table_name (
  id STRING(255) NOT NULL,
) PRIMARY KEY(id)`, "CREATE INDEX table_name_id_idx ON table_name(id)"},
		},
		{
			name: "multi statement, no trailing semicolon, standalone comment",
			// From https://github.com/mattes/migrate/pull/281
			multiStatement: `CREATE TABLE table_name (
			-- standalone comment
			id STRING(255) NOT NULL,
		) PRIMARY KEY(id);

		CREATE INDEX table_name_id_idx ON table_name (id)`,
			expected: []string{`CREATE TABLE table_name (
  id STRING(255) NOT NULL,
) PRIMARY KEY(id)`, "CREATE INDEX table_name_id_idx ON table_name(id)"},
		},
		{
			name: "multi statement, no trailing semicolon, inline comment",
			// From https://github.com/mattes/migrate/pull/281
			multiStatement: `CREATE TABLE table_name (
			id STRING(255) NOT NULL, -- inline comment
		) PRIMARY KEY(id);

		CREATE INDEX table_name_id_idx ON table_name (id)`,
			expected: []string{`CREATE TABLE table_name (
  id STRING(255) NOT NULL,
) PRIMARY KEY(id)`, "CREATE INDEX table_name_id_idx ON table_name(id)"},
		},
		{
			name: "alter table with SET OPTIONS",
			multiStatement: `ALTER TABLE users ALTER COLUMN created
			SET OPTIONS (allow_commit_timestamp=true);`,
			expected: []string{"ALTER TABLE users ALTER COLUMN created SET OPTIONS (allow_commit_timestamp = true)"},
		},
		{
			name: "column with NUMERIC type",
			multiStatement: `CREATE TABLE table_name (
				id STRING(255) NOT NULL,
				sum NUMERIC,
			) PRIMARY KEY (id)`,
			expected: []string{"CREATE TABLE table_name (\n  id STRING(255) NOT NULL,\n  sum NUMERIC,\n) PRIMARY KEY(id)"},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			stmts, err := cleanStatements([]byte(tc.multiStatement))
			require.NoError(t, err, "Error cleaning statements")
			assert.Equal(t, tc.expected, stmts)
		})
	}
}
```

## File: `database/spanner/examples/migrations/1481574547_create_users_table.down.sql`
```sql
DROP TABLE Users
```

## File: `database/spanner/examples/migrations/1481574547_create_users_table.up.sql`
```sql
CREATE TABLE Users (
  UserId  INT64,
  Name    STRING(40),
  Email   STRING(83)
) PRIMARY KEY(UserId)
```

## File: `database/spanner/examples/migrations/1496539702_add_city_to_users.down.sql`
```sql
ALTER TABLE Users DROP COLUMN city
```

## File: `database/spanner/examples/migrations/1496539702_add_city_to_users.up.sql`
```sql
ALTER TABLE Users ADD COLUMN city STRING(100)
```

## File: `database/spanner/examples/migrations/1496601752_add_index_on_user_emails.down.sql`
```sql
DROP INDEX UsersEmailIndex
```

## File: `database/spanner/examples/migrations/1496601752_add_index_on_user_emails.up.sql`
```sql
CREATE UNIQUE INDEX UsersEmailIndex ON Users (Email)
```

## File: `database/spanner/examples/migrations/1496602638_create_books_table.down.sql`
```sql
DROP TABLE Books
```

## File: `database/spanner/examples/migrations/1496602638_create_books_table.up.sql`
```sql
CREATE TABLE Books (
  UserId INT64,
  Name    STRING(40),
  Author  STRING(40)
) PRIMARY KEY(UserId, Name), 
INTERLEAVE IN PARENT Users ON DELETE CASCADE
```

## File: `database/spanner/examples/migrations/1621360367_create_transactions_table.down.sql`
```sql
DROP TABLE Transactions
```

## File: `database/spanner/examples/migrations/1621360367_create_transactions_table.up.sql`
```sql
CREATE TABLE Transactions (
  UserId        INT64,
  TransactionId STRING(40),
  Total         NUMERIC
) PRIMARY KEY(UserId, TransactionId), 
INTERLEAVE IN PARENT Users ON DELETE CASCADE
```

## File: `database/sqlcipher/README.md`
```markdown
# sqlcipher

This is just a copy of the [sqlite3](https://github.com/golang-migrate/migrate/blob/master/database/sqlite3) driver except that it imports `github.com/mutecomm/go-sqlcipher`.
```

## File: `database/sqlcipher/sqlcipher.go`
```go
package sqlcipher

import (
	"database/sql"
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"strconv"
	"strings"
	"sync/atomic"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	_ "github.com/mutecomm/go-sqlcipher/v4"
)

func init() {
	database.Register("sqlcipher", &Sqlite{})
}

var DefaultMigrationsTable = "schema_migrations"
var (
	ErrDatabaseDirty  = fmt.Errorf("database is dirty")
	ErrNilConfig      = fmt.Errorf("no config")
	ErrNoDatabaseName = fmt.Errorf("no database name")
)

type Config struct {
	MigrationsTable string
	DatabaseName    string
	NoTxWrap        bool
}

type Sqlite struct {
	db       *sql.DB
	isLocked atomic.Bool

	config *Config
}

func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	mx := &Sqlite{
		db:     instance,
		config: config,
	}
	if err := mx.ensureVersionTable(); err != nil {
		return nil, err
	}
	return mx, nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the Sqlite type.
func (m *Sqlite) ensureVersionTable() (err error) {
	if err = m.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := m.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	query := fmt.Sprintf(`
	CREATE TABLE IF NOT EXISTS %s (version uint64,dirty bool);
  CREATE UNIQUE INDEX IF NOT EXISTS version_unique ON %s (version);
  `, m.config.MigrationsTable, m.config.MigrationsTable)

	if _, err := m.db.Exec(query); err != nil {
		return err
	}
	return nil
}

func (m *Sqlite) Open(url string) (database.Driver, error) {
	purl, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}
	dbfile := strings.Replace(migrate.FilterCustomQuery(purl).String(), "sqlite3://", "", 1)
	db, err := sql.Open("sqlite3", dbfile)
	if err != nil {
		return nil, err
	}

	qv := purl.Query()

	migrationsTable := qv.Get("x-migrations-table")
	if len(migrationsTable) == 0 {
		migrationsTable = DefaultMigrationsTable
	}

	noTxWrap := false
	if v := qv.Get("x-no-tx-wrap"); v != "" {
		noTxWrap, err = strconv.ParseBool(v)
		if err != nil {
			return nil, fmt.Errorf("x-no-tx-wrap: %s", err)
		}
	}

	mx, err := WithInstance(db, &Config{
		DatabaseName:    purl.Path,
		MigrationsTable: migrationsTable,
		NoTxWrap:        noTxWrap,
	})
	if err != nil {
		return nil, err
	}
	return mx, nil
}

func (m *Sqlite) Close() error {
	return m.db.Close()
}

func (m *Sqlite) Drop() (err error) {
	query := `SELECT name FROM sqlite_master WHERE type = 'table';`
	tables, err := m.db.Query(query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	tableNames := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}
		if len(tableName) > 0 {
			tableNames = append(tableNames, tableName)
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if len(tableNames) > 0 {
		for _, t := range tableNames {
			query := "DROP TABLE " + t
			err = m.executeQuery(query)
			if err != nil {
				return &database.Error{OrigErr: err, Query: []byte(query)}
			}
		}
		query := "VACUUM"
		_, err = m.db.Query(query)
		if err != nil {
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	return nil
}

func (m *Sqlite) Lock() error {
	if !m.isLocked.CompareAndSwap(false, true) {
		return database.ErrLocked
	}
	return nil
}

func (m *Sqlite) Unlock() error {
	if !m.isLocked.CompareAndSwap(true, false) {
		return database.ErrNotLocked
	}
	return nil
}

func (m *Sqlite) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}
	query := string(migr[:])

	if m.config.NoTxWrap {
		return m.executeQueryNoTx(query)
	}
	return m.executeQuery(query)
}

func (m *Sqlite) executeQuery(query string) error {
	tx, err := m.db.Begin()
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}
	if _, err := tx.Exec(query); err != nil {
		if errRollback := tx.Rollback(); errRollback != nil {
			err = errors.Join(err, errRollback)
		}
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}
	return nil
}

func (m *Sqlite) executeQueryNoTx(query string) error {
	if _, err := m.db.Exec(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	return nil
}

func (m *Sqlite) SetVersion(version int, dirty bool) error {
	tx, err := m.db.Begin()
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}

	query := "DELETE FROM " + m.config.MigrationsTable
	if _, err := tx.Exec(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	// Also re-write the schema version for nil dirty versions to prevent
	// empty schema version for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330
	if version >= 0 || (version == database.NilVersion && dirty) {
		query := fmt.Sprintf(`INSERT INTO %s (version, dirty) VALUES (?, ?)`, m.config.MigrationsTable)
		if _, err := tx.Exec(query, version, dirty); err != nil {
			if errRollback := tx.Rollback(); errRollback != nil {
				err = errors.Join(err, errRollback)
			}
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}

	return nil
}

func (m *Sqlite) Version() (version int, dirty bool, err error) {
	query := "SELECT version, dirty FROM " + m.config.MigrationsTable + " LIMIT 1"
	err = m.db.QueryRow(query).Scan(&version, &dirty)
	if err != nil {
		return database.NilVersion, false, nil
	}
	return version, dirty, nil
}
```

## File: `database/sqlcipher/sqlcipher_test.go`
```go
package sqlcipher

import (
	"database/sql"
	"fmt"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/golang-migrate/migrate/v4"
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	_ "github.com/golang-migrate/migrate/v4/source/file"
	_ "github.com/mutecomm/go-sqlcipher/v4"
)

func Test(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite3.db"))
	p := &Sqlite{}
	addr := fmt.Sprintf("sqlite3://%s", filepath.Join(dir, "sqlite3.db"))
	d, err := p.Open(addr)
	if err != nil {
		t.Fatal(err)
	}
	dt.Test(t, d, []byte("CREATE TABLE t (Qty int, Name string);"))
}

func TestMigrate(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite3.db"))

	db, err := sql.Open("sqlite3", filepath.Join(dir, "sqlite3.db"))
	if err != nil {
		return
	}
	defer func() {
		if err := db.Close(); err != nil {
			return
		}
	}()
	driver, err := WithInstance(db, &Config{})
	if err != nil {
		t.Fatal(err)
	}

	m, err := migrate.NewWithDatabaseInstance(
		"file://./examples/migrations",
		"ql", driver)
	if err != nil {
		t.Fatal(err)
	}
	dt.TestMigrate(t, m)
}

func TestMigrationTable(t *testing.T) {
	dir := t.TempDir()

	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite3.db"))

	db, err := sql.Open("sqlite3", filepath.Join(dir, "sqlite3.db"))
	if err != nil {
		return
	}
	defer func() {
		if err := db.Close(); err != nil {
			return
		}
	}()

	config := &Config{
		MigrationsTable: "my_migration_table",
	}
	driver, err := WithInstance(db, config)
	if err != nil {
		t.Fatal(err)
	}
	m, err := migrate.NewWithDatabaseInstance(
		"file://./examples/migrations",
		"ql", driver)
	if err != nil {
		t.Fatal(err)
	}
	t.Log("UP")
	err = m.Up()
	if err != nil {
		t.Fatal(err)
	}

	_, err = db.Query(fmt.Sprintf("SELECT * FROM %s", config.MigrationsTable))
	if err != nil {
		t.Fatal(err)
	}
}

func TestNoTxWrap(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite3.db"))
	p := &Sqlite{}
	addr := fmt.Sprintf("sqlite3://%s?x-no-tx-wrap=true", filepath.Join(dir, "sqlite3.db"))
	d, err := p.Open(addr)
	if err != nil {
		t.Fatal(err)
	}
	// An explicit BEGIN statement would ordinarily fail without x-no-tx-wrap.
	// (Transactions in sqlite may not be nested.)
	dt.Test(t, d, []byte("BEGIN; CREATE TABLE t (Qty int, Name string); COMMIT;"))
}

func TestNoTxWrapInvalidValue(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite3.db"))
	p := &Sqlite{}
	addr := fmt.Sprintf("sqlite3://%s?x-no-tx-wrap=yeppers", filepath.Join(dir, "sqlite3.db"))
	_, err := p.Open(addr)
	if assert.Error(t, err) {
		assert.Contains(t, err.Error(), "x-no-tx-wrap")
		assert.Contains(t, err.Error(), "invalid syntax")
	}
}
```

## File: `database/sqlcipher/examples/migrations/33_create_table.down.sql`
```sql
DROP TABLE IF EXISTS pets;
```

## File: `database/sqlcipher/examples/migrations/33_create_table.up.sql`
```sql
CREATE TABLE pets (
  name string
);
```

## File: `database/sqlcipher/examples/migrations/44_alter_table.down.sql`
```sql
DROP TABLE IF EXISTS pets;
```

## File: `database/sqlcipher/examples/migrations/44_alter_table.up.sql`
```sql
ALTER TABLE pets ADD predator bool;
```

## File: `database/sqlite/README.md`
```markdown
# sqlite

`sqlite://path/to/database?query`

Unlike other migrate database drivers, the sqlite driver will automatically wrap each migration in an implicit transaction by default.  Migrations must not contain explicit `BEGIN` or `COMMIT` statements.  This behavior may change in a future major release.  (See below for a workaround.)

The auxiliary query parameters listed below may be supplied to tailor migrate behavior.  All auxiliary query parameters are optional.

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table.  Defaults to `schema_migrations`. |
| `x-no-tx-wrap` | `NoTxWrap` | Disable implicit transactions when `true`.  Migrations may, and should, contain explicit `BEGIN` and `COMMIT` statements. |

## Notes

* Uses the `modernc.org/sqlite` sqlite db driver (pure Go)
  * Has [limited `GOOS` and `GOARCH` support](https://pkg.go.dev/modernc.org/sqlite?utm_source=godoc#hdr-Supported_platforms_and_architectures)
```

## File: `database/sqlite/sqlite.go`
```go
package sqlite

import (
	"database/sql"
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"strconv"
	"strings"
	"sync/atomic"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	_ "modernc.org/sqlite"
)

func init() {
	database.Register("sqlite", &Sqlite{})
}

var DefaultMigrationsTable = "schema_migrations"
var (
	ErrDatabaseDirty  = fmt.Errorf("database is dirty")
	ErrNilConfig      = fmt.Errorf("no config")
	ErrNoDatabaseName = fmt.Errorf("no database name")
)

type Config struct {
	MigrationsTable string
	DatabaseName    string
	NoTxWrap        bool
}

type Sqlite struct {
	db       *sql.DB
	isLocked atomic.Bool

	config *Config
}

func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	mx := &Sqlite{
		db:     instance,
		config: config,
	}
	if err := mx.ensureVersionTable(); err != nil {
		return nil, err
	}
	return mx, nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the Sqlite type.
func (m *Sqlite) ensureVersionTable() (err error) {
	if err = m.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := m.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	query := fmt.Sprintf(`
	CREATE TABLE IF NOT EXISTS %s (version uint64,dirty bool);
  CREATE UNIQUE INDEX IF NOT EXISTS version_unique ON %s (version);
  `, m.config.MigrationsTable, m.config.MigrationsTable)

	if _, err := m.db.Exec(query); err != nil {
		return err
	}
	return nil
}

func (m *Sqlite) Open(url string) (database.Driver, error) {
	purl, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}
	dbfile := strings.Replace(migrate.FilterCustomQuery(purl).String(), "sqlite://", "", 1)
	db, err := sql.Open("sqlite", dbfile)
	if err != nil {
		return nil, err
	}

	qv := purl.Query()

	migrationsTable := qv.Get("x-migrations-table")
	if len(migrationsTable) == 0 {
		migrationsTable = DefaultMigrationsTable
	}

	noTxWrap := false
	if v := qv.Get("x-no-tx-wrap"); v != "" {
		noTxWrap, err = strconv.ParseBool(v)
		if err != nil {
			return nil, fmt.Errorf("x-no-tx-wrap: %s", err)
		}
	}

	mx, err := WithInstance(db, &Config{
		DatabaseName:    purl.Path,
		MigrationsTable: migrationsTable,
		NoTxWrap:        noTxWrap,
	})
	if err != nil {
		return nil, err
	}
	return mx, nil
}

func (m *Sqlite) Close() error {
	return m.db.Close()
}

func (m *Sqlite) Drop() (err error) {
	query := `SELECT name FROM sqlite_master WHERE type = 'table';`
	tables, err := m.db.Query(query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	tableNames := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}
		if len(tableName) > 0 {
			tableNames = append(tableNames, tableName)
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if len(tableNames) > 0 {
		for _, t := range tableNames {
			query := "DROP TABLE " + t
			err = m.executeQuery(query)
			if err != nil {
				return &database.Error{OrigErr: err, Query: []byte(query)}
			}
		}
		query := "VACUUM"
		_, err = m.db.Query(query)
		if err != nil {
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	return nil
}

func (m *Sqlite) Lock() error {
	if !m.isLocked.CompareAndSwap(false, true) {
		return database.ErrLocked
	}
	return nil
}

func (m *Sqlite) Unlock() error {
	if !m.isLocked.CompareAndSwap(true, false) {
		return database.ErrNotLocked
	}
	return nil
}

func (m *Sqlite) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}
	query := string(migr[:])

	if m.config.NoTxWrap {
		return m.executeQueryNoTx(query)
	}
	return m.executeQuery(query)
}

func (m *Sqlite) executeQuery(query string) error {
	tx, err := m.db.Begin()
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}
	if _, err := tx.Exec(query); err != nil {
		if errRollback := tx.Rollback(); errRollback != nil {
			err = errors.Join(err, errRollback)
		}
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}
	return nil
}

func (m *Sqlite) executeQueryNoTx(query string) error {
	if _, err := m.db.Exec(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	return nil
}

func (m *Sqlite) SetVersion(version int, dirty bool) error {
	tx, err := m.db.Begin()
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}

	query := "DELETE FROM " + m.config.MigrationsTable
	if _, err := tx.Exec(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	// Also re-write the schema version for nil dirty versions to prevent
	// empty schema version for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330
	if version >= 0 || (version == database.NilVersion && dirty) {
		query := fmt.Sprintf(`INSERT INTO %s (version, dirty) VALUES (?, ?)`, m.config.MigrationsTable)
		if _, err := tx.Exec(query, version, dirty); err != nil {
			if errRollback := tx.Rollback(); errRollback != nil {
				err = errors.Join(err, errRollback)
			}
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}

	return nil
}

func (m *Sqlite) Version() (version int, dirty bool, err error) {
	query := "SELECT version, dirty FROM " + m.config.MigrationsTable + " LIMIT 1"
	err = m.db.QueryRow(query).Scan(&version, &dirty)
	if err != nil {
		return database.NilVersion, false, nil
	}
	return version, dirty, nil
}
```

## File: `database/sqlite/sqlite_test.go`
```go
package sqlite

import (
	"database/sql"
	"fmt"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/golang-migrate/migrate/v4"
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	_ "github.com/golang-migrate/migrate/v4/source/file"
	_ "modernc.org/sqlite"
)

func Test(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite.db"))
	p := &Sqlite{}
	addr := fmt.Sprintf("sqlite://%s", filepath.Join(dir, "sqlite.db"))
	d, err := p.Open(addr)
	if err != nil {
		t.Fatal(err)
	}
	dt.Test(t, d, []byte("CREATE TABLE t (Qty int, Name string);"))
}

func TestMigrate(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite.db"))

	db, err := sql.Open("sqlite", filepath.Join(dir, "sqlite.db"))
	if err != nil {
		return
	}
	defer func() {
		if err := db.Close(); err != nil {
			return
		}
	}()
	driver, err := WithInstance(db, &Config{})
	if err != nil {
		t.Fatal(err)
	}

	m, err := migrate.NewWithDatabaseInstance(
		"file://./examples/migrations",
		"ql", driver)
	if err != nil {
		t.Fatal(err)
	}
	dt.TestMigrate(t, m)
}

func TestMigrationTable(t *testing.T) {
	dir := t.TempDir()

	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite.db"))

	db, err := sql.Open("sqlite", filepath.Join(dir, "sqlite.db"))
	if err != nil {
		return
	}
	defer func() {
		if err := db.Close(); err != nil {
			return
		}
	}()

	config := &Config{
		MigrationsTable: "my_migration_table",
	}
	driver, err := WithInstance(db, config)
	if err != nil {
		t.Fatal(err)
	}
	m, err := migrate.NewWithDatabaseInstance(
		"file://./examples/migrations",
		"ql", driver)
	if err != nil {
		t.Fatal(err)
	}
	t.Log("UP")
	err = m.Up()
	if err != nil {
		t.Fatal(err)
	}

	_, err = db.Query(fmt.Sprintf("SELECT * FROM %s", config.MigrationsTable))
	if err != nil {
		t.Fatal(err)
	}
}

func TestNoTxWrap(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite.db"))
	p := &Sqlite{}
	addr := fmt.Sprintf("sqlite://%s?x-no-tx-wrap=true", filepath.Join(dir, "sqlite.db"))
	d, err := p.Open(addr)
	if err != nil {
		t.Fatal(err)
	}
	// An explicit BEGIN statement would ordinarily fail without x-no-tx-wrap.
	// (Transactions in sqlite may not be nested.)
	dt.Test(t, d, []byte("BEGIN; CREATE TABLE t (Qty int, Name string); COMMIT;"))
}

func TestNoTxWrapInvalidValue(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite.db"))
	p := &Sqlite{}
	addr := fmt.Sprintf("sqlite://%s?x-no-tx-wrap=yeppers", filepath.Join(dir, "sqlite.db"))
	_, err := p.Open(addr)
	if assert.Error(t, err) {
		assert.Contains(t, err.Error(), "x-no-tx-wrap")
		assert.Contains(t, err.Error(), "invalid syntax")
	}
}

func TestMigrateWithDirectoryNameContainsWhitespaces(t *testing.T) {
	dir := t.TempDir()
	dbPath := filepath.Join(dir, "sqlite.db")
	t.Logf("DB path : %s\n", dbPath)
	p := &Sqlite{}
	addr := fmt.Sprintf("sqlite://file:%s", dbPath)
	d, err := p.Open(addr)
	if err != nil {
		t.Fatal(err)
	}
	dt.Test(t, d, []byte("CREATE TABLE t (Qty int, Name string);"))
}
```

## File: `database/sqlite/examples/migrations/33_create_table.down.sql`
```sql
DROP TABLE IF EXISTS pets;
```

## File: `database/sqlite/examples/migrations/33_create_table.up.sql`
```sql
CREATE TABLE pets (
  name string
);
```

## File: `database/sqlite/examples/migrations/44_alter_table.down.sql`
```sql
DROP TABLE IF EXISTS pets;
```

## File: `database/sqlite/examples/migrations/44_alter_table.up.sql`
```sql
ALTER TABLE pets ADD predator bool;
```

## File: `database/sqlite3/README.md`
```markdown
# sqlite3

`sqlite3://path/to/database?query`

Unlike other migrate database drivers, the sqlite3 driver will automatically wrap each migration in an implicit transaction by default.  Migrations must not contain explicit `BEGIN` or `COMMIT` statements.  This behavior may change in a future major release.  (See below for a workaround.)

Refer to [upstream documentation](https://github.com/mattn/go-sqlite3/blob/master/README.md#connection-string) for a complete list of query parameters supported by the sqlite3 database driver.  The auxiliary query parameters listed below may be supplied to tailor migrate behavior.  All auxiliary query parameters are optional.

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table.  Defaults to `schema_migrations`. |
| `x-no-tx-wrap` | `NoTxWrap` | Disable implicit transactions when `true`.  Migrations may, and should, contain explicit `BEGIN` and `COMMIT` statements. |

## Notes

* Uses the `github.com/mattn/go-sqlite3` sqlite db driver (cgo)
```

## File: `database/sqlite3/sqlite3.go`
```go
package sqlite3

import (
	"database/sql"
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"strconv"
	"strings"
	"sync/atomic"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	_ "github.com/mattn/go-sqlite3"
)

func init() {
	database.Register("sqlite3", &Sqlite{})
}

var DefaultMigrationsTable = "schema_migrations"
var (
	ErrDatabaseDirty  = fmt.Errorf("database is dirty")
	ErrNilConfig      = fmt.Errorf("no config")
	ErrNoDatabaseName = fmt.Errorf("no database name")
)

type Config struct {
	MigrationsTable string
	DatabaseName    string
	NoTxWrap        bool
}

type Sqlite struct {
	db       *sql.DB
	isLocked atomic.Bool

	config *Config
}

func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	mx := &Sqlite{
		db:     instance,
		config: config,
	}
	if err := mx.ensureVersionTable(); err != nil {
		return nil, err
	}
	return mx, nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database, which deviates from the usual
// convention of "caller locks" in the Sqlite type.
func (m *Sqlite) ensureVersionTable() (err error) {
	if err = m.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := m.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	query := fmt.Sprintf(`
	CREATE TABLE IF NOT EXISTS %s (version uint64,dirty bool);
  CREATE UNIQUE INDEX IF NOT EXISTS version_unique ON %s (version);
  `, m.config.MigrationsTable, m.config.MigrationsTable)

	if _, err := m.db.Exec(query); err != nil {
		return err
	}
	return nil
}

func (m *Sqlite) Open(url string) (database.Driver, error) {
	purl, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}
	dbfile := strings.Replace(migrate.FilterCustomQuery(purl).String(), "sqlite3://", "", 1)
	db, err := sql.Open("sqlite3", dbfile)
	if err != nil {
		return nil, err
	}

	qv := purl.Query()

	migrationsTable := qv.Get("x-migrations-table")
	if len(migrationsTable) == 0 {
		migrationsTable = DefaultMigrationsTable
	}

	noTxWrap := false
	if v := qv.Get("x-no-tx-wrap"); v != "" {
		noTxWrap, err = strconv.ParseBool(v)
		if err != nil {
			return nil, fmt.Errorf("x-no-tx-wrap: %s", err)
		}
	}

	mx, err := WithInstance(db, &Config{
		DatabaseName:    purl.Path,
		MigrationsTable: migrationsTable,
		NoTxWrap:        noTxWrap,
	})
	if err != nil {
		return nil, err
	}
	return mx, nil
}

func (m *Sqlite) Close() error {
	return m.db.Close()
}

func (m *Sqlite) Drop() (err error) {
	query := `SELECT name FROM sqlite_master WHERE type = 'table';`
	tables, err := m.db.Query(query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	tableNames := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}
		if len(tableName) > 0 {
			tableNames = append(tableNames, tableName)
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if len(tableNames) > 0 {
		for _, t := range tableNames {
			query := "DROP TABLE " + t
			err = m.executeQuery(query)
			if err != nil {
				return &database.Error{OrigErr: err, Query: []byte(query)}
			}
		}
		query := "VACUUM"
		_, err = m.db.Query(query)
		if err != nil {
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	return nil
}

func (m *Sqlite) Lock() error {
	if !m.isLocked.CompareAndSwap(false, true) {
		return database.ErrLocked
	}
	return nil
}

func (m *Sqlite) Unlock() error {
	if !m.isLocked.CompareAndSwap(true, false) {
		return database.ErrNotLocked
	}
	return nil
}

func (m *Sqlite) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}
	query := string(migr[:])

	if m.config.NoTxWrap {
		return m.executeQueryNoTx(query)
	}
	return m.executeQuery(query)
}

func (m *Sqlite) executeQuery(query string) error {
	tx, err := m.db.Begin()
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}
	if _, err := tx.Exec(query); err != nil {
		if errRollback := tx.Rollback(); errRollback != nil {
			err = errors.Join(err, errRollback)
		}
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}
	return nil
}

func (m *Sqlite) executeQueryNoTx(query string) error {
	if _, err := m.db.Exec(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	return nil
}

func (m *Sqlite) SetVersion(version int, dirty bool) error {
	tx, err := m.db.Begin()
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}

	query := "DELETE FROM " + m.config.MigrationsTable
	if _, err := tx.Exec(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	// Also re-write the schema version for nil dirty versions to prevent
	// empty schema version for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330
	if version >= 0 || (version == database.NilVersion && dirty) {
		query := fmt.Sprintf(`INSERT INTO %s (version, dirty) VALUES (?, ?)`, m.config.MigrationsTable)
		if _, err := tx.Exec(query, version, dirty); err != nil {
			if errRollback := tx.Rollback(); errRollback != nil {
				err = errors.Join(err, errRollback)
			}
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}

	return nil
}

func (m *Sqlite) Version() (version int, dirty bool, err error) {
	query := "SELECT version, dirty FROM " + m.config.MigrationsTable + " LIMIT 1"
	err = m.db.QueryRow(query).Scan(&version, &dirty)
	if err != nil {
		return database.NilVersion, false, nil
	}
	return version, dirty, nil
}
```

## File: `database/sqlite3/sqlite3_test.go`
```go
package sqlite3

import (
	"database/sql"
	"fmt"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/golang-migrate/migrate/v4"
	dt "github.com/golang-migrate/migrate/v4/database/testing"
	_ "github.com/golang-migrate/migrate/v4/source/file"
	_ "github.com/mattn/go-sqlite3"
)

func Test(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite3.db"))
	p := &Sqlite{}
	addr := fmt.Sprintf("sqlite3://%s", filepath.Join(dir, "sqlite3.db"))
	d, err := p.Open(addr)
	if err != nil {
		t.Fatal(err)
	}
	dt.Test(t, d, []byte("CREATE TABLE t (Qty int, Name string);"))
}

func TestMigrate(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite3.db"))

	db, err := sql.Open("sqlite3", filepath.Join(dir, "sqlite3.db"))
	if err != nil {
		return
	}
	defer func() {
		if err := db.Close(); err != nil {
			return
		}
	}()
	driver, err := WithInstance(db, &Config{})
	if err != nil {
		t.Fatal(err)
	}

	m, err := migrate.NewWithDatabaseInstance(
		"file://./examples/migrations",
		"ql", driver)
	if err != nil {
		t.Fatal(err)
	}
	dt.TestMigrate(t, m)
}

func TestMigrationTable(t *testing.T) {
	dir := t.TempDir()

	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite3.db"))

	db, err := sql.Open("sqlite3", filepath.Join(dir, "sqlite3.db"))
	if err != nil {
		return
	}
	defer func() {
		if err := db.Close(); err != nil {
			return
		}
	}()

	config := &Config{
		MigrationsTable: "my_migration_table",
	}
	driver, err := WithInstance(db, config)
	if err != nil {
		t.Fatal(err)
	}
	m, err := migrate.NewWithDatabaseInstance(
		"file://./examples/migrations",
		"ql", driver)
	if err != nil {
		t.Fatal(err)
	}
	t.Log("UP")
	err = m.Up()
	if err != nil {
		t.Fatal(err)
	}

	_, err = db.Query(fmt.Sprintf("SELECT * FROM %s", config.MigrationsTable))
	if err != nil {
		t.Fatal(err)
	}
}

func TestNoTxWrap(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite3.db"))
	p := &Sqlite{}
	addr := fmt.Sprintf("sqlite3://%s?x-no-tx-wrap=true", filepath.Join(dir, "sqlite3.db"))
	d, err := p.Open(addr)
	if err != nil {
		t.Fatal(err)
	}
	// An explicit BEGIN statement would ordinarily fail without x-no-tx-wrap.
	// (Transactions in sqlite may not be nested.)
	dt.Test(t, d, []byte("BEGIN; CREATE TABLE t (Qty int, Name string); COMMIT;"))
}

func TestNoTxWrapInvalidValue(t *testing.T) {
	dir := t.TempDir()
	t.Logf("DB path : %s\n", filepath.Join(dir, "sqlite3.db"))
	p := &Sqlite{}
	addr := fmt.Sprintf("sqlite3://%s?x-no-tx-wrap=yeppers", filepath.Join(dir, "sqlite3.db"))
	_, err := p.Open(addr)
	if assert.Error(t, err) {
		assert.Contains(t, err.Error(), "x-no-tx-wrap")
		assert.Contains(t, err.Error(), "invalid syntax")
	}
}

func TestMigrateWithDirectoryNameContainsWhitespaces(t *testing.T) {
	dir := t.TempDir()
	dbPath := filepath.Join(dir, "sqlite3.db")
	t.Logf("DB path : %s\n", dbPath)
	p := &Sqlite{}
	addr := fmt.Sprintf("sqlite3://file:%s", dbPath)
	d, err := p.Open(addr)
	if err != nil {
		t.Fatal(err)
	}
	dt.Test(t, d, []byte("CREATE TABLE t (Qty int, Name string);"))
}
```

## File: `database/sqlite3/examples/migrations/33_create_table.down.sql`
```sql
DROP TABLE IF EXISTS pets;
```

## File: `database/sqlite3/examples/migrations/33_create_table.up.sql`
```sql
CREATE TABLE pets (
  name string
);
```

## File: `database/sqlite3/examples/migrations/44_alter_table.down.sql`
```sql
DROP TABLE IF EXISTS pets;
```

## File: `database/sqlite3/examples/migrations/44_alter_table.up.sql`
```sql
ALTER TABLE pets ADD predator bool;
```

## File: `database/sqlserver/README.md`
```markdown
# Microsoft SQL Server

`sqlserver://username:password@host/instance?param1=value&param2=value`
`sqlserver://username:password@host:port?param1=value&param2=value`

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table |
| `username` | |  enter the SQL Server Authentication user id or the Windows Authentication user id in the DOMAIN\User format. On Windows, if user id is empty or missing Single-Sign-On is used. |
| `password` | | The user's password. | 
| `host` | | The host to connect to. |
| `port` | | The port to connect to. |
| `instance` | | SQL Server instance name. |
| `database` | `DatabaseName` | The name of the database to connect to |
| `connection+timeout` | | in seconds (default is 0 for no timeout), set to 0 for no timeout. |
| `dial+timeout` | | in seconds (default is 15), set to 0 for no timeout. |
| `encrypt` | | `disable` - Data send between client and server is not encrypted. `false` - Data sent between client and server is not encrypted beyond the login packet (Default). `true` - Data sent between client and server is encrypted. |
| `app+name` || The application name (default is go-mssqldb). |
| `useMsi` | | `true` - Use Azure MSI Authentication for connecting to Sql Server. Must be running from an Azure VM/an instance with MSI enabled. `false` - Use password authentication (Default). See [here for Azure MSI Auth details](https://docs.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-connect-msi). NOTE: Since this cannot be tested locally, this is not officially supported.

See https://github.com/microsoft/go-mssqldb for full parameter list.

## Driver Support

### Which go-mssqldb driver to us?

Please note that the deprecated `mssql` driver is not supported. Please use the newer `sqlserver` driver.  
See https://github.com/microsoft/go-mssqldb#deprecated for more information.

### Official Support by migrate

Versions of MS SQL Server 2019 newer than CTP3.1 are not officially supported since there are issues testing against the Docker image.
For more info, see: https://github.com/golang-migrate/migrate/issues/160#issuecomment-522433269
```

## File: `database/sqlserver/sqlserver.go`
```go
package sqlserver

import (
	"context"
	"database/sql"
	"errors"
	"fmt"
	"io"
	nurl "net/url"
	"strconv"
	"strings"
	"sync/atomic"

	"github.com/Azure/go-autorest/autorest/adal"
	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	mssql "github.com/microsoft/go-mssqldb" // mssql support
)

func init() {
	database.Register("sqlserver", &SQLServer{})
}

// DefaultMigrationsTable is the name of the migrations table in the database
var DefaultMigrationsTable = "schema_migrations"

var (
	ErrNilConfig                 = fmt.Errorf("no config")
	ErrNoDatabaseName            = fmt.Errorf("no database name")
	ErrNoSchema                  = fmt.Errorf("no schema")
	ErrDatabaseDirty             = fmt.Errorf("database is dirty")
	ErrMultipleAuthOptionsPassed = fmt.Errorf("both password and useMsi=true were passed")
)

var lockErrorMap = map[int]string{
	-1:   "The lock request timed out.",
	-2:   "The lock request was canceled.",
	-3:   "The lock request was chosen as a deadlock victim.",
	-999: "Parameter validation or other call error.",
}

// Config for database
type Config struct {
	MigrationsTable string
	DatabaseName    string
	SchemaName      string
}

// SQL Server connection
type SQLServer struct {
	// Locking and unlocking need to use the same connection
	conn     *sql.Conn
	db       *sql.DB
	isLocked atomic.Bool

	// Open and WithInstance need to garantuee that config is never nil
	config *Config
}

// WithInstance returns a database instance from an already created database connection.
//
// Note that the deprecated `mssql` driver is not supported. Please use the newer `sqlserver` driver.
func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	if config.DatabaseName == "" {
		query := `SELECT DB_NAME()`
		var databaseName string
		if err := instance.QueryRow(query).Scan(&databaseName); err != nil {
			return nil, &database.Error{OrigErr: err, Query: []byte(query)}
		}

		if len(databaseName) == 0 {
			return nil, ErrNoDatabaseName
		}

		config.DatabaseName = databaseName
	}

	if config.SchemaName == "" {
		query := `SELECT SCHEMA_NAME()`
		var schemaName string
		if err := instance.QueryRow(query).Scan(&schemaName); err != nil {
			return nil, &database.Error{OrigErr: err, Query: []byte(query)}
		}

		if len(schemaName) == 0 {
			return nil, ErrNoSchema
		}

		config.SchemaName = schemaName
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	conn, err := instance.Conn(context.Background())

	if err != nil {
		return nil, err
	}

	ss := &SQLServer{
		conn:   conn,
		db:     instance,
		config: config,
	}

	if err := ss.ensureVersionTable(); err != nil {
		return nil, err
	}

	return ss, nil
}

// Open a connection to the database.
func (ss *SQLServer) Open(url string) (database.Driver, error) {
	purl, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}

	useMsiParam := purl.Query().Get("useMsi")
	useMsi := false
	if len(useMsiParam) > 0 {
		useMsi, err = strconv.ParseBool(useMsiParam)
		if err != nil {
			return nil, err
		}
	}

	if _, isPasswordSet := purl.User.Password(); useMsi && isPasswordSet {
		return nil, ErrMultipleAuthOptionsPassed
	}

	filteredURL := migrate.FilterCustomQuery(purl).String()

	var db *sql.DB
	if useMsi {
		resource := getAADResourceFromServerUri(purl)
		tokenProvider, err := getMSITokenProvider(resource)
		if err != nil {
			return nil, err
		}

		connector, err := mssql.NewAccessTokenConnector(
			filteredURL, tokenProvider)
		if err != nil {
			return nil, err
		}

		db = sql.OpenDB(connector)

	} else {
		db, err = sql.Open("sqlserver", filteredURL)
		if err != nil {
			return nil, err
		}
	}

	migrationsTable := purl.Query().Get("x-migrations-table")

	px, err := WithInstance(db, &Config{
		DatabaseName:    purl.Path,
		MigrationsTable: migrationsTable,
	})

	if err != nil {
		return nil, err
	}

	return px, nil
}

// Close the database connection
func (ss *SQLServer) Close() error {
	connErr := ss.conn.Close()
	dbErr := ss.db.Close()
	if connErr != nil || dbErr != nil {
		return fmt.Errorf("conn: %v, db: %v", connErr, dbErr)
	}
	return nil
}

// Lock creates an advisory local on the database to prevent multiple migrations from running at the same time.
func (ss *SQLServer) Lock() error {
	return database.CasRestoreOnErr(&ss.isLocked, false, true, database.ErrLocked, func() error {
		aid, err := database.GenerateAdvisoryLockId(ss.config.DatabaseName, ss.config.SchemaName)
		if err != nil {
			return err
		}

		// This will block until the lock is acquired.
		// MS Docs: sp_getapplock: https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-getapplock-transact-sql?view=sql-server-2017
		query := `
		DECLARE @lockResult int;
		EXEC @lockResult = sp_getapplock @Resource = @p1, @LockMode = 'Exclusive', @LockOwner = 'Session', @LockTimeout = -1;
		SELECT @lockResult;`

		var status int
		if err = ss.conn.QueryRowContext(context.Background(), query, aid).Scan(&status); err == nil && status > -1 {
			return nil
		} else if err != nil {
			return &database.Error{OrigErr: err, Err: "try lock failed", Query: []byte(query)}
		} else {
			errorDescription, ok := lockErrorMap[status]
			if !ok {
				errorDescription = "Unknown error"
			}
			return &database.Error{Err: fmt.Sprintf("try lock failed with error %v: %v", status, errorDescription), Query: []byte(query)}
		}
	})
}

// Unlock froms the migration lock from the database
func (ss *SQLServer) Unlock() error {
	return database.CasRestoreOnErr(&ss.isLocked, true, false, database.ErrNotLocked, func() error {
		aid, err := database.GenerateAdvisoryLockId(ss.config.DatabaseName, ss.config.SchemaName)
		if err != nil {
			return err
		}

		// MS Docs: sp_releaseapplock: https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-releaseapplock-transact-sql?view=sql-server-2017
		query := `EXEC sp_releaseapplock @Resource = @p1, @LockOwner = 'Session'`
		if _, err := ss.conn.ExecContext(context.Background(), query, aid); err != nil {
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}

		return nil
	})
}

// Run the migrations for the database
func (ss *SQLServer) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}

	// run migration
	query := string(migr[:])
	if _, err := ss.conn.ExecContext(context.Background(), query); err != nil {
		if msErr, ok := err.(mssql.Error); ok {
			message := fmt.Sprintf("migration failed: %s", msErr.Message)
			if msErr.ProcName != "" {
				message = fmt.Sprintf("%s (proc name %s)", msErr.Message, msErr.ProcName)
			}
			return database.Error{OrigErr: err, Err: message, Query: migr, Line: uint(msErr.LineNo)}
		}
		return database.Error{OrigErr: err, Err: "migration failed", Query: migr}
	}

	return nil
}

// SetVersion for the current database
func (ss *SQLServer) SetVersion(version int, dirty bool) error {

	tx, err := ss.conn.BeginTx(context.Background(), &sql.TxOptions{})
	if err != nil {
		return &database.Error{OrigErr: err, Err: "transaction start failed"}
	}

	query := `TRUNCATE TABLE ` + ss.getMigrationTable()
	if _, err := tx.Exec(query); err != nil {
		if errRollback := tx.Rollback(); errRollback != nil {
			err = errors.Join(err, errRollback)
		}
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	// Also re-write the schema version for nil dirty versions to prevent
	// empty schema version for failed down migration on the first migration
	// See: https://github.com/golang-migrate/migrate/issues/330
	if version >= 0 || (version == database.NilVersion && dirty) {
		var dirtyBit int
		if dirty {
			dirtyBit = 1
		}
		query = `INSERT INTO ` + ss.getMigrationTable() + ` (version, dirty) VALUES (@p1, @p2)`
		if _, err := tx.Exec(query, version, dirtyBit); err != nil {
			if errRollback := tx.Rollback(); errRollback != nil {
				err = errors.Join(err, errRollback)
			}
			return &database.Error{OrigErr: err, Query: []byte(query)}
		}
	}

	if err := tx.Commit(); err != nil {
		return &database.Error{OrigErr: err, Err: "transaction commit failed"}
	}

	return nil
}

// Version of the current database state
func (ss *SQLServer) Version() (version int, dirty bool, err error) {
	query := `SELECT TOP 1 version, dirty FROM ` + ss.getMigrationTable()
	err = ss.conn.QueryRowContext(context.Background(), query).Scan(&version, &dirty)
	switch {
	case err == sql.ErrNoRows:
		return database.NilVersion, false, nil

	case err != nil:
		// FIXME: convert to MSSQL error
		return 0, false, &database.Error{OrigErr: err, Query: []byte(query)}

	default:
		return version, dirty, nil
	}
}

// Drop all tables from the database.
func (ss *SQLServer) Drop() error {

	// drop all referential integrity constraints
	query := `
	DECLARE @Sql NVARCHAR(500) DECLARE @Cursor CURSOR

	SET @Cursor = CURSOR FAST_FORWARD FOR
	SELECT DISTINCT sql = 'ALTER TABLE [' + tc2.TABLE_NAME + '] DROP [' + rc1.CONSTRAINT_NAME + ']'
	FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS rc1
	LEFT JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc2 ON tc2.CONSTRAINT_NAME =rc1.CONSTRAINT_NAME

	OPEN @Cursor FETCH NEXT FROM @Cursor INTO @Sql

	WHILE (@@FETCH_STATUS = 0)
	BEGIN
	Exec sp_executesql @Sql
	FETCH NEXT FROM @Cursor INTO @Sql
	END

	CLOSE @Cursor DEALLOCATE @Cursor`

	if _, err := ss.conn.ExecContext(context.Background(), query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	// drop the tables
	query = `EXEC sp_MSforeachtable 'DROP TABLE ?'`
	if _, err := ss.conn.ExecContext(context.Background(), query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}

func (ss *SQLServer) ensureVersionTable() (err error) {
	if err = ss.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := ss.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	query := `IF NOT EXISTS
	(SELECT *
		 FROM sysobjects
		WHERE id = object_id(N'` + ss.getMigrationTable() + `')
			AND OBJECTPROPERTY(id, N'IsUserTable') = 1
	)
	CREATE TABLE ` + ss.getMigrationTable() + ` ( version BIGINT PRIMARY KEY NOT NULL, dirty BIT NOT NULL );`

	if _, err = ss.conn.ExecContext(context.Background(), query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}

func (ss *SQLServer) getMigrationTable() string {
	return fmt.Sprintf("[%s].[%s]", ss.config.SchemaName, ss.config.MigrationsTable)
}

func getMSITokenProvider(resource string) (func() (string, error), error) {
	msi, err := adal.NewServicePrincipalTokenFromManagedIdentity(resource, nil)
	if err != nil {
		return nil, err
	}

	return func() (string, error) {
		err := msi.EnsureFresh()
		if err != nil {
			return "", err
		}
		token := msi.OAuthToken()
		return token, nil
	}, nil
}

// The sql server resource can change across clouds so get it
// dynamically based on the server uri.
// ex. <server name>.database.windows.net -> https://database.windows.net
func getAADResourceFromServerUri(purl *nurl.URL) string {
	return fmt.Sprintf("%s%s", "https://", strings.Join(strings.Split(purl.Hostname(), ".")[1:], "."))
}
```

## File: `database/sqlserver/sqlserver_test.go`
```go
package sqlserver

import (
	"context"
	"database/sql"
	sqldriver "database/sql/driver"
	"fmt"
	"log"
	"runtime"
	"strings"
	"testing"
	"time"

	"github.com/dhui/dktest"
	"github.com/golang-migrate/migrate/v4"

	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"

	_ "github.com/golang-migrate/migrate/v4/source/file"
)

const defaultPort = 1433
const saPassword = "Root1234"

var (
	sqlServerOpts = dktest.Options{
		Env:          map[string]string{"ACCEPT_EULA": "Y", "MSSQL_SA_PASSWORD": saPassword, "MSSQL_PID": "Express"},
		PortRequired: true, ReadyFunc: isReady, PullTimeout: 2 * time.Minute,
	}
	// Container versions: https://mcr.microsoft.com/v2/mssql/server/tags/list
	specs = []dktesting.ContainerSpec{
		{ImageName: "mcr.microsoft.com/mssql/server:2022-latest", Options: sqlServerOpts},
		{ImageName: "mcr.microsoft.com/mssql/server:2019-latest", Options: sqlServerOpts},
		// Add back support for 2017 version once the image is fixed: https://github.com/microsoft/mssql-docker/issues/899
		// {ImageName: "mcr.microsoft.com/mssql/server:2017-latest", Options: sqlServerOpts},
	}
)

func msConnectionString(host, port string) string {
	return fmt.Sprintf("sqlserver://sa:%v@%v:%v?database=master", saPassword, host, port)
}

func msConnectionStringMsiWithPassword(host, port string, useMsi bool) string {
	return fmt.Sprintf("sqlserver://sa:%v@%v:%v?database=master&useMsi=%t", saPassword, host, port, useMsi)
}

func msConnectionStringMsi(host, port string, useMsi bool) string {
	return fmt.Sprintf("sqlserver://sa@%v:%v?database=master&useMsi=%t", host, port, useMsi)
}

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	ip, port, err := c.Port(defaultPort)
	if err != nil {
		return false
	}
	uri := msConnectionString(ip, port)
	db, err := sql.Open("sqlserver", uri)
	if err != nil {
		return false
	}
	defer func() {
		if err := db.Close(); err != nil {
			log.Println("close error:", err)
		}
	}()
	if err = db.PingContext(ctx); err != nil {
		switch err {
		case sqldriver.ErrBadConn:
			return false
		default:
			fmt.Println(err)
		}
		return false
	}

	return true
}

func SkipIfUnsupportedArch(t *testing.T, c dktest.ContainerInfo) {
	if strings.Contains(c.ImageName, "mssql") && !strings.HasPrefix(runtime.GOARCH, "amd") {
		t.Skipf("Image %s is not supported on arch %s", c.ImageName, runtime.GOARCH)
	}
}

func Test(t *testing.T) {
	t.Run("test", test)
	t.Run("testMigrate", testMigrate)
	t.Run("testMultiStatement", testMultiStatement)
	t.Run("testErrorParsing", testErrorParsing)
	t.Run("testLockWorks", testLockWorks)
	t.Run("testMsiTrue", testMsiTrue)
	t.Run("testOpenWithPasswordAndMSI", testOpenWithPasswordAndMSI)
	t.Run("testMsiFalse", testMsiFalse)

	t.Cleanup(func() {
		for _, spec := range specs {
			t.Log("Cleaning up ", spec.ImageName)
			if err := spec.Cleanup(); err != nil {
				t.Error("Error removing ", spec.ImageName, "error:", err)
			}
		}
	})
}

func test(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		SkipIfUnsupportedArch(t, c)
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := msConnectionString(ip, port)
		p := &SQLServer{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatalf("%v", err)
		}

		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		dt.Test(t, d, []byte("SELECT 1"))
	})
}

func testMigrate(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		SkipIfUnsupportedArch(t, c)
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := msConnectionString(ip, port)
		p := &SQLServer{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatalf("%v", err)
		}

		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "master", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}

func testMultiStatement(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		SkipIfUnsupportedArch(t, c)
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := msConnectionString(ip, port)
		ms := &SQLServer{}
		d, err := ms.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()
		if err := d.Run(strings.NewReader("CREATE TABLE foo (foo text); CREATE TABLE bar (bar text);")); err != nil {
			t.Fatalf("expected err to be nil, got %v", err)
		}

		// make sure second table exists
		var exists int
		if err := d.(*SQLServer).conn.QueryRowContext(context.Background(), "SELECT COUNT(1) FROM information_schema.tables WHERE table_name = 'bar' AND table_schema = (SELECT schema_name()) AND table_catalog = (SELECT db_name())").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if exists != 1 {
			t.Fatalf("expected table bar to exist")
		}
	})
}

func testErrorParsing(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		SkipIfUnsupportedArch(t, c)
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := msConnectionString(ip, port)

		p := &SQLServer{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		wantErr := `migration failed: Unknown object type 'TABLEE' used in a CREATE, DROP, or ALTER statement. in line 1:` +
			` CREATE TABLE foo (foo text); CREATE TABLEE bar (bar text); (details: mssql: Unknown object type ` +
			`'TABLEE' used in a CREATE, DROP, or ALTER statement.)`
		if err := d.Run(strings.NewReader("CREATE TABLE foo (foo text); CREATE TABLEE bar (bar text);")); err == nil {
			t.Fatal("expected err but got nil")
		} else if err.Error() != wantErr {
			t.Fatalf("expected '%s' but got '%s'", wantErr, err.Error())
		}
	})
}

func testLockWorks(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		SkipIfUnsupportedArch(t, c)
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := fmt.Sprintf("sqlserver://sa:%v@%v:%v?master", saPassword, ip, port)
		p := &SQLServer{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatalf("%v", err)
		}
		dt.Test(t, d, []byte("SELECT 1"))

		ms := d.(*SQLServer)

		err = ms.Lock()
		if err != nil {
			t.Fatal(err)
		}
		err = ms.Unlock()
		if err != nil {
			t.Fatal(err)
		}

		// make sure the 2nd lock works (RELEASE_LOCK is very finicky)
		err = ms.Lock()
		if err != nil {
			t.Fatal(err)
		}
		err = ms.Unlock()
		if err != nil {
			t.Fatal(err)
		}
	})
}

func testMsiTrue(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		SkipIfUnsupportedArch(t, c)
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := msConnectionStringMsi(ip, port, true)
		p := &SQLServer{}
		_, err = p.Open(addr)
		if err == nil {
			t.Fatal("MSI should fail when not running in an Azure context.")
		}
	})
}

func testOpenWithPasswordAndMSI(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		SkipIfUnsupportedArch(t, c)
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := msConnectionStringMsiWithPassword(ip, port, true)
		p := &SQLServer{}
		_, err = p.Open(addr)
		if err == nil {
			t.Fatal("Open should fail when both password and useMsi=true are passed.")
		}

		addr = msConnectionStringMsiWithPassword(ip, port, false)
		p = &SQLServer{}
		d, err := p.Open(addr)
		if err != nil {
			t.Fatal(err)
		}

		defer func() {
			if err := d.Close(); err != nil {
				t.Error(err)
			}
		}()

		dt.Test(t, d, []byte("SELECT 1"))
	})
}

func testMsiFalse(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, c dktest.ContainerInfo) {
		SkipIfUnsupportedArch(t, c)
		ip, port, err := c.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := msConnectionStringMsi(ip, port, false)
		p := &SQLServer{}
		_, err = p.Open(addr)
		if err == nil {
			t.Fatal("Open should fail since no password was passed and useMsi is false.")
		}
	})
}
```

## File: `database/sqlserver/examples/migrations/1085649617_create_users_table.down.sql`
```sql
DROP TABLE IF EXISTS users;
```

## File: `database/sqlserver/examples/migrations/1085649617_create_users_table.up.sql`
```sql
CREATE TABLE users (
  user_id integer unique,
  name    varchar(40),
  email   varchar(40)
);
```

## File: `database/sqlserver/examples/migrations/1185749658_add_city_to_users.down.sql`
```sql
ALTER TABLE users DROP COLUMN IF EXISTS city;
```

## File: `database/sqlserver/examples/migrations/1185749658_add_city_to_users.up.sql`
```sql
ALTER TABLE users ADD city varchar(100);


```

## File: `database/sqlserver/examples/migrations/1285849751_add_index_on_user_emails.down.sql`
```sql
DROP INDEX IF EXISTS users_email_index;
```

## File: `database/sqlserver/examples/migrations/1285849751_add_index_on_user_emails.up.sql`
```sql
CREATE UNIQUE INDEX users_email_index ON users (email);

-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/sqlserver/examples/migrations/1385949617_create_books_table.down.sql`
```sql
DROP TABLE IF EXISTS books;
```

## File: `database/sqlserver/examples/migrations/1385949617_create_books_table.up.sql`
```sql
CREATE TABLE books (
  user_id integer,
  name    varchar(40),
  author  varchar(40)
);
```

## File: `database/sqlserver/examples/migrations/1485949617_create_movies_table.down.sql`
```sql
DROP TABLE IF EXISTS movies;
```

## File: `database/sqlserver/examples/migrations/1485949617_create_movies_table.up.sql`
```sql
CREATE TABLE movies (
  user_id   integer,
  name      varchar(40),
  director  varchar(40)
);
```

## File: `database/sqlserver/examples/migrations/1585849751_just_a_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/sqlserver/examples/migrations/1685849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/sqlserver/examples/migrations/1785849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/sqlserver/examples/migrations/1885849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/stub/stub.go`
```go
package stub

import (
	"io"
	"reflect"
	"sync/atomic"

	"github.com/golang-migrate/migrate/v4/database"
)

func init() {
	database.Register("stub", &Stub{})
}

type Stub struct {
	Url               string
	Instance          interface{}
	CurrentVersion    int
	MigrationSequence []string
	LastRunMigration  []byte // todo: make []string
	IsDirty           bool
	isLocked          atomic.Bool

	Config *Config
}

func (s *Stub) Open(url string) (database.Driver, error) {
	return &Stub{
		Url:               url,
		CurrentVersion:    database.NilVersion,
		MigrationSequence: make([]string, 0),
		Config:            &Config{},
	}, nil
}

type Config struct{}

func WithInstance(instance interface{}, config *Config) (database.Driver, error) {
	return &Stub{
		Instance:          instance,
		CurrentVersion:    database.NilVersion,
		MigrationSequence: make([]string, 0),
		Config:            config,
	}, nil
}

func (s *Stub) Close() error {
	return nil
}

func (s *Stub) Lock() error {
	if !s.isLocked.CompareAndSwap(false, true) {
		return database.ErrLocked
	}
	return nil
}

func (s *Stub) Unlock() error {
	if !s.isLocked.CompareAndSwap(true, false) {
		return database.ErrNotLocked
	}
	return nil
}

func (s *Stub) Run(migration io.Reader) error {
	m, err := io.ReadAll(migration)
	if err != nil {
		return err
	}
	s.LastRunMigration = m
	s.MigrationSequence = append(s.MigrationSequence, string(m[:]))
	return nil
}

func (s *Stub) SetVersion(version int, state bool) error {
	s.CurrentVersion = version
	s.IsDirty = state
	return nil
}

func (s *Stub) Version() (version int, dirty bool, err error) {
	return s.CurrentVersion, s.IsDirty, nil
}

const DROP = "DROP"

func (s *Stub) Drop() error {
	s.CurrentVersion = database.NilVersion
	s.LastRunMigration = nil
	s.MigrationSequence = append(s.MigrationSequence, DROP)
	return nil
}

func (s *Stub) EqualSequence(seq []string) bool {
	return reflect.DeepEqual(seq, s.MigrationSequence)
}
```

## File: `database/stub/stub_test.go`
```go
package stub

import (
	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/source"
	"github.com/golang-migrate/migrate/v4/source/stub"
	"testing"

	dt "github.com/golang-migrate/migrate/v4/database/testing"
)

func Test(t *testing.T) {
	s := &Stub{}
	d, err := s.Open("")
	if err != nil {
		t.Fatal(err)
	}
	dt.Test(t, d, []byte("/* foobar migration */"))
}

func TestMigrate(t *testing.T) {
	s := &Stub{}
	d, err := s.Open("")
	if err != nil {
		t.Fatal(err)
	}

	stubMigrations := source.NewMigrations()
	stubMigrations.Append(&source.Migration{Version: 1, Direction: source.Up, Identifier: "CREATE 1"})
	stubMigrations.Append(&source.Migration{Version: 1, Direction: source.Down, Identifier: "DROP 1"})
	src := &stub.Stub{}
	srcDrv, err := src.Open("")
	if err != nil {
		t.Fatal(err)
	}
	srcDrv.(*stub.Stub).Migrations = stubMigrations
	m, err := migrate.NewWithInstance("stub", srcDrv, "", d)
	if err != nil {
		t.Fatal(err)
	}

	dt.TestMigrate(t, m)
}
```

## File: `database/testing/migrate_testing.go`
```go
// Package testing has the database tests.
// All database drivers must pass the Test function.
// This lives in it's own package so it stays a test dependency.
package testing

import (
	"testing"
)

import (
	"github.com/golang-migrate/migrate/v4"
)

// TestMigrate runs integration-tests between the Migrate layer and database implementations.
func TestMigrate(t *testing.T, m *migrate.Migrate) {
	TestMigrateUp(t, m)
	TestMigrateDrop(t, m)
}

// Regression test for preventing a regression for #164 https://github.com/golang-migrate/migrate/pull/173
// Similar to TestDrop(), but tests the dropping mechanism through the Migrate logic instead, to check for
// double-locking during the Drop logic.
func TestMigrateDrop(t *testing.T, m *migrate.Migrate) {
	if err := m.Drop(); err != nil {
		t.Fatal(err)
	}
}

func TestMigrateUp(t *testing.T, m *migrate.Migrate) {
	t.Log("UP")
	if err := m.Up(); err != nil {
		t.Fatal(err)
	}
}
```

## File: `database/testing/testing.go`
```go
// Package testing has the database tests.
// All database drivers must pass the Test function.
// This lives in it's own package so it stays a test dependency.
package testing

import (
	"bytes"
	"errors"
	"fmt"
	"io"
	"testing"
	"time"

	"github.com/golang-migrate/migrate/v4/database"
)

// Test runs tests against database implementations.
func Test(t *testing.T, d database.Driver, migration []byte) {
	if migration == nil {
		t.Fatal("test must provide migration reader")
	}

	TestNilVersion(t, d) // test first
	TestLockAndUnlock(t, d)
	TestRun(t, d, bytes.NewReader(migration))
	TestSetVersion(t, d) // also tests Version()
	// Drop breaks the driver, so test it last.
	TestDrop(t, d)
}

func TestNilVersion(t *testing.T, d database.Driver) {
	v, _, err := d.Version()
	if err != nil {
		t.Fatal(err)
	}
	if v != database.NilVersion {
		t.Fatalf("Version: expected version to be NilVersion (-1), got %v", v)
	}
}

func TestLockAndUnlock(t *testing.T, d database.Driver) {
	// add a timeout, in case there is a deadlock
	done := make(chan struct{})
	errs := make(chan error)

	go func() {
		timeout := time.After(15 * time.Second)
		for {
			select {
			case <-done:
				return
			case <-timeout:
				errs <- fmt.Errorf("timeout after 15 seconds, looks like a deadlock in Lock/UnLock\n%#v", d)
				return
			}
		}
	}()

	// run the locking test ...
	go func() {
		if err := d.Lock(); err != nil {
			errs <- err
			return
		}

		// try to acquire lock again
		if err := d.Lock(); err == nil {
			errs <- errors.New("lock: expected err not to be nil")
			return
		}

		// unlock
		if err := d.Unlock(); err != nil {
			errs <- err
			return
		}

		// try to lock
		if err := d.Lock(); err != nil {
			errs <- err
			return
		}
		if err := d.Unlock(); err != nil {
			errs <- err
			return
		}
		// notify everyone
		close(done)
	}()

	// wait for done or any error
	for {
		select {
		case <-done:
			return
		case err := <-errs:
			t.Fatal(err)
		}
	}
}

func TestRun(t *testing.T, d database.Driver, migration io.Reader) {
	if migration == nil {
		t.Fatal("migration can't be nil")
	}

	if err := d.Run(migration); err != nil {
		t.Fatal(err)
	}
}

func TestDrop(t *testing.T, d database.Driver) {
	if err := d.Drop(); err != nil {
		t.Fatal(err)
	}
}

func TestSetVersion(t *testing.T, d database.Driver) {
	testCases := []struct {
		name            string
		version         int
		dirty           bool
		expectedErr     error
		expectedReadErr error
		expectedVersion int
		expectedDirty   bool
	}{
		{name: "set 1 dirty", version: 1, dirty: true, expectedErr: nil, expectedReadErr: nil, expectedVersion: 1, expectedDirty: true},
		{name: "re-set 1 dirty", version: 1, dirty: true, expectedErr: nil, expectedReadErr: nil, expectedVersion: 1, expectedDirty: true},
		{name: "set 2 clean", version: 2, dirty: false, expectedErr: nil, expectedReadErr: nil, expectedVersion: 2, expectedDirty: false},
		{name: "re-set 2 clean", version: 2, dirty: false, expectedErr: nil, expectedReadErr: nil, expectedVersion: 2, expectedDirty: false},
		{name: "last migration dirty", version: database.NilVersion, dirty: true, expectedErr: nil, expectedReadErr: nil, expectedVersion: database.NilVersion, expectedDirty: true},
		{name: "last migration clean", version: database.NilVersion, dirty: false, expectedErr: nil, expectedReadErr: nil, expectedVersion: database.NilVersion, expectedDirty: false},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			err := d.SetVersion(tc.version, tc.dirty)
			if err != tc.expectedErr {
				t.Fatal("Got unexpected error:", err, "!=", tc.expectedErr)
			}
			v, dirty, readErr := d.Version()
			if readErr != tc.expectedReadErr {
				t.Fatal("Got unexpected error:", readErr, "!=", tc.expectedReadErr)
			}
			if v != tc.expectedVersion {
				t.Error("Got unexpected version:", v, "!=", tc.expectedVersion)
			}
			if dirty != tc.expectedDirty {
				t.Error("Got unexpected dirty value:", dirty, "!=", tc.dirty)
			}
		})
	}
}
```

## File: `database/yugabytedb/README.md`
```markdown
# yugabytedb

`yugabytedb://user:password@host:port/dbname?query` (`yugabyte://`, and `ysql://` work, too)

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| `x-migrations-table` | `MigrationsTable` | Name of the migrations table |
| `x-lock-table` | `LockTable` | Name of the table which maintains the migration lock |
| `x-force-lock` | `ForceLock` | Force lock acquisition to fix faulty migrations which may not have released the schema lock (Boolean, default is `false`) |
| `x-max-retries` | `MaxRetries` | How many times retry queries on retryable errors (40001, 40P01, 08006, XX000). Default is 10 |
| `x-max-retry-interval` | `MaxRetryInterval` | Interval between retries increases exponentially. This option specifies maximum duration between retries. Default is 15s |
| `x-max-retry-elapsed-time` | `MaxRetryElapsedTime` | Total retries timeout. Default is 30s |
| `dbname` | `DatabaseName` | The name of the database to connect to |
| `user` | | The user to sign in as |
| `password` | | The user's password |
| `host` | | The host to connect to. Values that start with / are for unix domain sockets. (default is localhost) |
| `port` | | The port to bind to. (default is 5432) |
| `connect_timeout` | | Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely. |
| `sslcert` | | Cert file location. The file must contain PEM encoded data. |
| `sslkey` | | Key file location. The file must contain PEM encoded data. |
| `sslrootcert` | | The location of the root certificate file. The file must contain PEM encoded data. |
| `sslmode` | | Whether or not to use SSL (disable\|require\|verify-ca\|verify-full) |
```

## File: `database/yugabytedb/yugabytedb.go`
```go
package yugabytedb

import (
	"context"
	"database/sql"
	"errors"
	"io"
	"net/url"
	"regexp"
	"strconv"
	"sync/atomic"
	"time"

	"github.com/cenkalti/backoff/v4"
	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	"github.com/jackc/pgconn"
	"github.com/jackc/pgerrcode"
	"github.com/lib/pq"
)

const (
	DefaultMaxRetryInterval    = time.Second * 15
	DefaultMaxRetryElapsedTime = time.Second * 30
	DefaultMaxRetries          = 10
	DefaultMigrationsTable     = "migrations"
	DefaultLockTable           = "migrations_locks"
)

var (
	ErrNilConfig          = errors.New("no config")
	ErrNoDatabaseName     = errors.New("no database name")
	ErrMaxRetriesExceeded = errors.New("max retries exceeded")
)

func init() {
	db := YugabyteDB{}
	database.Register("yugabyte", &db)
	database.Register("yugabytedb", &db)
	database.Register("ysql", &db)
}

type Config struct {
	MigrationsTable     string
	LockTable           string
	ForceLock           bool
	DatabaseName        string
	MaxRetryInterval    time.Duration
	MaxRetryElapsedTime time.Duration
	MaxRetries          int
}

type YugabyteDB struct {
	db       *sql.DB
	isLocked atomic.Bool

	// Open and WithInstance need to guarantee that config is never nil
	config *Config
}

func WithInstance(instance *sql.DB, config *Config) (database.Driver, error) {
	if config == nil {
		return nil, ErrNilConfig
	}

	if err := instance.Ping(); err != nil {
		return nil, err
	}

	if config.DatabaseName == "" {
		query := `SELECT current_database()`
		var databaseName string
		if err := instance.QueryRow(query).Scan(&databaseName); err != nil {
			return nil, &database.Error{OrigErr: err, Query: []byte(query)}
		}

		if len(databaseName) == 0 {
			return nil, ErrNoDatabaseName
		}

		config.DatabaseName = databaseName
	}

	if len(config.MigrationsTable) == 0 {
		config.MigrationsTable = DefaultMigrationsTable
	}

	if len(config.LockTable) == 0 {
		config.LockTable = DefaultLockTable
	}

	if config.MaxRetryInterval == 0 {
		config.MaxRetryInterval = DefaultMaxRetryInterval
	}

	if config.MaxRetryElapsedTime == 0 {
		config.MaxRetryElapsedTime = DefaultMaxRetryElapsedTime
	}

	if config.MaxRetries == 0 {
		config.MaxRetries = DefaultMaxRetries
	}

	px := &YugabyteDB{
		db:     instance,
		config: config,
	}

	// ensureVersionTable is a locking operation, so we need to ensureLockTable before we ensureVersionTable.
	if err := px.ensureLockTable(); err != nil {
		return nil, err
	}

	if err := px.ensureVersionTable(); err != nil {
		return nil, err
	}

	return px, nil
}

func (c *YugabyteDB) Open(dbURL string) (database.Driver, error) {
	purl, err := url.Parse(dbURL)
	if err != nil {
		return nil, err
	}

	// As YugabyteDB uses the postgres protocol, and 'postgres' is already a registered database, we need to replace the
	// connect prefix, with the actual protocol, so that the library can differentiate between the implementations
	re := regexp.MustCompile("^(yugabyte(db)?|ysql)")
	connectString := re.ReplaceAllString(migrate.FilterCustomQuery(purl).String(), "postgres")

	db, err := sql.Open("postgres", connectString)
	if err != nil {
		return nil, err
	}

	migrationsTable := purl.Query().Get("x-migrations-table")
	if len(migrationsTable) == 0 {
		migrationsTable = DefaultMigrationsTable
	}

	lockTable := purl.Query().Get("x-lock-table")
	if len(lockTable) == 0 {
		lockTable = DefaultLockTable
	}

	forceLockQuery := purl.Query().Get("x-force-lock")
	forceLock, err := strconv.ParseBool(forceLockQuery)
	if err != nil {
		forceLock = false
	}

	maxIntervalStr := purl.Query().Get("x-max-retry-interval")
	maxInterval, err := time.ParseDuration(maxIntervalStr)
	if err != nil {
		maxInterval = DefaultMaxRetryInterval
	}

	maxElapsedTimeStr := purl.Query().Get("x-max-retry-elapsed-time")
	maxElapsedTime, err := time.ParseDuration(maxElapsedTimeStr)
	if err != nil {
		maxElapsedTime = DefaultMaxRetryElapsedTime
	}

	maxRetriesStr := purl.Query().Get("x-max-retries")
	maxRetries, err := strconv.Atoi(maxRetriesStr)
	if err != nil {
		maxRetries = DefaultMaxRetries
	}

	px, err := WithInstance(db, &Config{
		DatabaseName:        purl.Path,
		MigrationsTable:     migrationsTable,
		LockTable:           lockTable,
		ForceLock:           forceLock,
		MaxRetryInterval:    maxInterval,
		MaxRetryElapsedTime: maxElapsedTime,
		MaxRetries:          maxRetries,
	})
	if err != nil {
		return nil, err
	}

	return px, nil
}

func (c *YugabyteDB) Close() error {
	return c.db.Close()
}

// Locking is done manually with a separate lock table. Implementing advisory locks in YugabyteDB is being discussed
// See: https://github.com/yugabyte/yugabyte-db/issues/3642
func (c *YugabyteDB) Lock() error {
	return database.CasRestoreOnErr(&c.isLocked, false, true, database.ErrLocked, func() (err error) {
		return c.doTxWithRetry(context.Background(), &sql.TxOptions{Isolation: sql.LevelSerializable}, func(tx *sql.Tx) (err error) {
			aid, err := database.GenerateAdvisoryLockId(c.config.DatabaseName)
			if err != nil {
				return err
			}

			query := "SELECT * FROM " + c.config.LockTable + " WHERE lock_id = $1"
			rows, err := tx.Query(query, aid)
			if err != nil {
				return database.Error{OrigErr: err, Err: "failed to fetch migration lock", Query: []byte(query)}
			}
			defer func() {
				if errClose := rows.Close(); errClose != nil {
					err = errors.Join(err, errClose)
				}
			}()

			// If row exists at all, lock is present
			locked := rows.Next()
			if locked && !c.config.ForceLock {
				return database.ErrLocked
			}

			query = "INSERT INTO " + c.config.LockTable + " (lock_id) VALUES ($1)"
			if _, err := tx.Exec(query, aid); err != nil {
				return database.Error{OrigErr: err, Err: "failed to set migration lock", Query: []byte(query)}
			}

			return nil
		})
	})
}

// Locking is done manually with a separate lock table. Implementing advisory locks in YugabyteDB is being discussed
// See: https://github.com/yugabyte/yugabyte-db/issues/3642
func (c *YugabyteDB) Unlock() error {
	return database.CasRestoreOnErr(&c.isLocked, true, false, database.ErrNotLocked, func() (err error) {
		aid, err := database.GenerateAdvisoryLockId(c.config.DatabaseName)
		if err != nil {
			return err
		}

		// In the event of an implementation (non-migration) error, it is possible for the lock to not be released. Until
		// a better locking mechanism is added, a manual purging of the lock table may be required in such circumstances
		query := "DELETE FROM " + c.config.LockTable + " WHERE lock_id = $1"
		if _, err := c.db.Exec(query, aid); err != nil {
			if e, ok := err.(*pq.Error); ok {
				// 42P01 is "UndefinedTableError" in YugabyteDB
				// https://github.com/yugabyte/yugabyte-db/blob/9c6b8e6beb56eed8eeb357178c0c6b837eb49896/src/postgres/src/backend/utils/errcodes.txt#L366
				if e.Code == "42P01" {
					// On drops, the lock table is fully removed; This is fine, and is a valid "unlocked" state for the schema
					return nil
				}
			}

			return database.Error{OrigErr: err, Err: "failed to release migration lock", Query: []byte(query)}
		}

		return nil
	})
}

func (c *YugabyteDB) Run(migration io.Reader) error {
	migr, err := io.ReadAll(migration)
	if err != nil {
		return err
	}

	// run migration
	query := string(migr[:])
	if _, err := c.db.Exec(query); err != nil {
		return database.Error{OrigErr: err, Err: "migration failed", Query: migr}
	}

	return nil
}

func (c *YugabyteDB) SetVersion(version int, dirty bool) error {
	return c.doTxWithRetry(context.Background(), &sql.TxOptions{Isolation: sql.LevelSerializable}, func(tx *sql.Tx) error {
		if _, err := tx.Exec(`DELETE FROM "` + c.config.MigrationsTable + `"`); err != nil {
			return err
		}

		// Also re-write the schema version for nil dirty versions to prevent
		// empty schema version for failed down migration on the first migration
		// See: https://github.com/golang-migrate/migrate/issues/330
		if version >= 0 || (version == database.NilVersion && dirty) {
			if _, err := tx.Exec(`INSERT INTO "`+c.config.MigrationsTable+`" (version, dirty) VALUES ($1, $2)`, version, dirty); err != nil {
				return err
			}
		}

		return nil
	})
}

func (c *YugabyteDB) Version() (version int, dirty bool, err error) {
	query := `SELECT version, dirty FROM "` + c.config.MigrationsTable + `" LIMIT 1`
	err = c.db.QueryRow(query).Scan(&version, &dirty)

	switch {
	case err == sql.ErrNoRows:
		return database.NilVersion, false, nil

	case err != nil:
		if e, ok := err.(*pq.Error); ok {
			// 42P01 is "UndefinedTableError" in YugabyteDB
			// https://github.com/yugabyte/yugabyte-db/blob/9c6b8e6beb56eed8eeb357178c0c6b837eb49896/src/postgres/src/backend/utils/errcodes.txt#L366
			if e.Code == "42P01" {
				return database.NilVersion, false, nil
			}
		}
		return 0, false, &database.Error{OrigErr: err, Query: []byte(query)}

	default:
		return version, dirty, nil
	}
}

func (c *YugabyteDB) Drop() (err error) {
	query := `SELECT table_name FROM information_schema.tables WHERE table_schema=(SELECT current_schema()) AND table_type='BASE TABLE'`
	tables, err := c.db.Query(query)
	if err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	defer func() {
		if errClose := tables.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	// delete one table after another
	tableNames := make([]string, 0)
	for tables.Next() {
		var tableName string
		if err := tables.Scan(&tableName); err != nil {
			return err
		}
		if len(tableName) > 0 {
			tableNames = append(tableNames, tableName)
		}
	}
	if err := tables.Err(); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	if len(tableNames) > 0 {
		for _, t := range tableNames {
			query = `DROP TABLE IF EXISTS ` + t + ` CASCADE`
			if _, err := c.db.Exec(query); err != nil {
				return &database.Error{OrigErr: err, Query: []byte(query)}
			}
		}
	}

	return nil
}

// ensureVersionTable checks if versions table exists and, if not, creates it.
// Note that this function locks the database
func (c *YugabyteDB) ensureVersionTable() (err error) {
	if err = c.Lock(); err != nil {
		return err
	}

	defer func() {
		if e := c.Unlock(); e != nil {
			err = errors.Join(err, e)
		}
	}()

	// check if migration table exists
	var count int
	query := `SELECT COUNT(1) FROM information_schema.tables WHERE table_name = $1 AND table_schema = (SELECT current_schema()) LIMIT 1`
	if err := c.db.QueryRow(query, c.config.MigrationsTable).Scan(&count); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	if count == 1 {
		return nil
	}

	// if not, create the empty migration table
	query = `CREATE TABLE "` + c.config.MigrationsTable + `" (version INT NOT NULL PRIMARY KEY, dirty BOOL NOT NULL)`
	if _, err := c.db.Exec(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	return nil
}

func (c *YugabyteDB) ensureLockTable() error {
	// check if lock table exists
	var count int
	query := `SELECT COUNT(1) FROM information_schema.tables WHERE table_name = $1 AND table_schema = (SELECT current_schema()) LIMIT 1`
	if err := c.db.QueryRow(query, c.config.LockTable).Scan(&count); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}
	if count == 1 {
		return nil
	}

	// if not, create the empty lock table
	query = `CREATE TABLE "` + c.config.LockTable + `" (lock_id TEXT NOT NULL PRIMARY KEY)`
	if _, err := c.db.Exec(query); err != nil {
		return &database.Error{OrigErr: err, Query: []byte(query)}
	}

	return nil
}

func (c *YugabyteDB) doTxWithRetry(
	ctx context.Context,
	txOpts *sql.TxOptions,
	fn func(tx *sql.Tx) error,
) error {
	backOff := c.newBackoff(ctx)

	return backoff.Retry(func() error {
		tx, err := c.db.BeginTx(ctx, txOpts)
		if err != nil {
			return backoff.Permanent(err)
		}

		// If we've tried to commit the transaction Rollback just returns sql.ErrTxDone.
		defer func() {
			_ = tx.Rollback()
		}()

		if err := fn(tx); err != nil {
			if errIsRetryable(err) {
				return err
			}

			return backoff.Permanent(err)
		}

		if err := tx.Commit(); err != nil {
			if errIsRetryable(err) {
				return err
			}

			return backoff.Permanent(err)
		}

		return nil
	}, backOff)
}

func (c *YugabyteDB) newBackoff(ctx context.Context) backoff.BackOff {
	if ctx == nil {
		ctx = context.Background()
	}

	retrier := backoff.WithMaxRetries(backoff.WithContext(&backoff.ExponentialBackOff{
		InitialInterval:     backoff.DefaultInitialInterval,
		RandomizationFactor: backoff.DefaultRandomizationFactor,
		Multiplier:          backoff.DefaultMultiplier,
		MaxInterval:         c.config.MaxRetryInterval,
		MaxElapsedTime:      c.config.MaxRetryElapsedTime,
		Stop:                backoff.Stop,
		Clock:               backoff.SystemClock,
	}, ctx), uint64(c.config.MaxRetries))

	retrier.Reset()

	return retrier
}

func errIsRetryable(err error) bool {
	var pgErr *pgconn.PgError
	if !errors.As(err, &pgErr) {
		return false
	}

	// Assume that it's safe to retry 08006 and XX000 because we check for lock existence
	// before creating and lock ID is primary key. Version field in migrations table is primary key too
	// and delete all versions is an idempotent operation.
	return pgErr.Code == pgerrcode.SerializationFailure || // optimistic locking conflict
		pgErr.Code == pgerrcode.DeadlockDetected ||
		pgErr.Code == pgerrcode.ConnectionFailure || // node down, need to reconnect
		pgErr.Code == pgerrcode.InternalError // may happen during HA
}
```

## File: `database/yugabytedb/yugabytedb_test.go`
```go
package yugabytedb

// error codes https://github.com/lib/pq/blob/master/error.go

import (
	"context"
	"database/sql"
	"fmt"
	"log"
	"strings"
	"testing"
	"time"

	"github.com/dhui/dktest"
	"github.com/golang-migrate/migrate/v4"

	_ "github.com/lib/pq"

	dt "github.com/golang-migrate/migrate/v4/database/testing"
	"github.com/golang-migrate/migrate/v4/dktesting"

	_ "github.com/golang-migrate/migrate/v4/source/file"
)

const defaultPort = 5433

var (
	opts = dktest.Options{
		Cmd:          []string{"bin/yugabyted", "start", "--daemon=false"},
		PortRequired: true,
		ReadyFunc:    isReady,
		Timeout:      time.Duration(60) * time.Second,
	}
	// Released versions: https://docs.yugabyte.com/preview/releases/release-notes/
	specs = []dktesting.ContainerSpec{
		{ImageName: "yugabytedb/yugabyte:2.14.15.0-b57", Options: opts},
		{ImageName: "yugabytedb/yugabyte:2.20.2.1-b3", Options: opts},
	}
)

func isReady(ctx context.Context, c dktest.ContainerInfo) bool {
	ip, port, err := c.Port(defaultPort)
	if err != nil {
		log.Println("port error:", err)
		return false
	}

	db, err := sql.Open("postgres", fmt.Sprintf("postgres://yugabyte:yugabyte@%v:%v?sslmode=disable", ip, port))
	if err != nil {
		log.Println("open error:", err)
		return false
	}
	if err := db.PingContext(ctx); err != nil {
		log.Println("ping error:", err)
		return false
	}
	if err := db.Close(); err != nil {
		log.Println("close error:", err)
	}
	return true
}

func createDB(t *testing.T, c dktest.ContainerInfo) {
	ip, port, err := c.Port(defaultPort)
	if err != nil {
		t.Fatal(err)
	}

	db, err := sql.Open("postgres", fmt.Sprintf("postgres://yugabyte:yugabyte@%v:%v?sslmode=disable", ip, port))
	if err != nil {
		t.Fatal(err)
	}
	if err = db.Ping(); err != nil {
		t.Fatal(err)
	}
	defer func() {
		if err := db.Close(); err != nil {
			t.Error(err)
		}
	}()

	if _, err = db.Exec("CREATE DATABASE migrate"); err != nil {
		t.Fatal(err)
	}
}

func getConnectionString(ip, port string, options ...string) string {
	options = append(options, "sslmode=disable")

	return fmt.Sprintf("yugabyte://yugabyte:yugabyte@%v:%v/migrate?%s", ip, port, strings.Join(options, "&"))
}

func Test(t *testing.T) {
	t.Run("test", test)
	t.Run("testMigrate", testMigrate)
	t.Run("testMultiStatement", testMultiStatement)
	t.Run("testFilterCustomQuery", testFilterCustomQuery)

	t.Cleanup(func() {
		for _, spec := range specs {
			t.Log("Cleaning up ", spec.ImageName)
			if err := spec.Cleanup(); err != nil {
				t.Error("Error removing ", spec.ImageName, "error:", err)
			}
		}
	})
}

func test(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, ci dktest.ContainerInfo) {
		createDB(t, ci)

		ip, port, err := ci.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := getConnectionString(ip, port)
		c := &YugabyteDB{}
		d, err := c.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		dt.Test(t, d, []byte("SELECT 1"))
	})
}

func testMigrate(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, ci dktest.ContainerInfo) {
		createDB(t, ci)

		ip, port, err := ci.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := getConnectionString(ip, port)
		c := &YugabyteDB{}
		d, err := c.Open(addr)
		if err != nil {
			t.Fatal(err)
		}

		m, err := migrate.NewWithDatabaseInstance("file://./examples/migrations", "migrate", d)
		if err != nil {
			t.Fatal(err)
		}
		dt.TestMigrate(t, m)
	})
}

func testMultiStatement(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, ci dktest.ContainerInfo) {
		createDB(t, ci)

		ip, port, err := ci.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := getConnectionString(ip, port)
		c := &YugabyteDB{}
		d, err := c.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		if err := d.Run(strings.NewReader("CREATE TABLE foo (foo text); CREATE TABLE bar (bar text);")); err != nil {
			t.Fatalf("expected err to be nil, got %v", err)
		}

		// make sure second table exists
		var exists bool
		if err := d.(*YugabyteDB).db.QueryRow("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'bar' AND table_schema = (SELECT current_schema()))").Scan(&exists); err != nil {
			t.Fatal(err)
		}
		if !exists {
			t.Fatal("expected table bar to exist")
		}
	})
}

func testFilterCustomQuery(t *testing.T) {
	dktesting.ParallelTest(t, specs, func(t *testing.T, ci dktest.ContainerInfo) {
		createDB(t, ci)

		ip, port, err := ci.Port(defaultPort)
		if err != nil {
			t.Fatal(err)
		}

		addr := getConnectionString(ip, port, "x-custom=foobar")
		c := &YugabyteDB{}
		d, err := c.Open(addr)
		if err != nil {
			t.Fatal(err)
		}
		dt.Test(t, d, []byte("SELECT 1"))
	})
}
```

## File: `database/yugabytedb/examples/migrations/1085649617_create_users_table.down.sql`
```sql
DROP TABLE IF EXISTS users;
```

## File: `database/yugabytedb/examples/migrations/1085649617_create_users_table.up.sql`
```sql
CREATE TABLE users (
  user_id integer unique,
  name    varchar(40),
  email   varchar(40)
);
```

## File: `database/yugabytedb/examples/migrations/1185749658_add_city_to_users.down.sql`
```sql
ALTER TABLE users DROP COLUMN IF EXISTS city;
```

## File: `database/yugabytedb/examples/migrations/1185749658_add_city_to_users.up.sql`
```sql
ALTER TABLE users ADD COLUMN city varchar(100);


```

## File: `database/yugabytedb/examples/migrations/1285849751_add_index_on_user_emails.down.sql`
```sql
DROP INDEX IF EXISTS users_email_index;
```

## File: `database/yugabytedb/examples/migrations/1285849751_add_index_on_user_emails.up.sql`
```sql
CREATE UNIQUE INDEX users_email_index ON users (email);

-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/yugabytedb/examples/migrations/1385949617_create_books_table.down.sql`
```sql
DROP TABLE IF EXISTS books;
```

## File: `database/yugabytedb/examples/migrations/1385949617_create_books_table.up.sql`
```sql
CREATE TABLE books (
  user_id integer,
  name    varchar(40),
  author  varchar(40)
);
```

## File: `database/yugabytedb/examples/migrations/1485949617_create_movies_table.down.sql`
```sql
DROP TABLE IF EXISTS movies;
```

## File: `database/yugabytedb/examples/migrations/1485949617_create_movies_table.up.sql`
```sql
CREATE TABLE movies (
  user_id   integer,
  name      varchar(40),
  director  varchar(40)
);
```

## File: `database/yugabytedb/examples/migrations/1585849751_just_a_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/yugabytedb/examples/migrations/1685849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/yugabytedb/examples/migrations/1785849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `database/yugabytedb/examples/migrations/1885849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `dktesting/dktesting.go`
```go
package dktesting

import (
	"context"
	"fmt"
	"testing"

	"github.com/dhui/dktest"
	"github.com/docker/docker/api/types/image"
	"github.com/docker/docker/client"
)

// ContainerSpec holds Docker testing setup specifications
type ContainerSpec struct {
	ImageName string
	Options   dktest.Options
}

// Cleanup cleanups the ContainerSpec after a test run by removing the ContainerSpec's image
func (s *ContainerSpec) Cleanup() (retErr error) {
	// copied from dktest.RunContext()
	dc, err := client.NewClientWithOpts(client.FromEnv, client.WithVersion("1.41"))
	if err != nil {
		return err
	}
	defer func() {
		if err := dc.Close(); err != nil && retErr == nil {
			retErr = fmt.Errorf("error closing Docker client: %w", err)
		}
	}()
	cleanupTimeout := s.Options.CleanupTimeout
	if cleanupTimeout <= 0 {
		cleanupTimeout = dktest.DefaultCleanupTimeout
	}
	ctx, timeoutCancelFunc := context.WithTimeout(context.Background(), cleanupTimeout)
	defer timeoutCancelFunc()
	if _, err := dc.ImageRemove(ctx, s.ImageName, image.RemoveOptions{Force: true, PruneChildren: true}); err != nil {
		return err
	}
	return nil
}

// ParallelTest runs Docker tests in parallel
func ParallelTest(t *testing.T, specs []ContainerSpec,
	testFunc func(*testing.T, dktest.ContainerInfo)) {

	for i, spec := range specs {
		spec := spec // capture range variable, see https://goo.gl/60w3p2

		// Only test against one version in short mode
		// TODO: order is random, maybe always pick first version instead?
		if i > 0 && testing.Short() {
			t.Logf("Skipping %v in short mode", spec.ImageName)
		} else {
			t.Run(spec.ImageName, func(t *testing.T) {
				t.Parallel()
				dktest.Run(t, spec.ImageName, spec.Options, testFunc)
			})
		}
	}
}
```

## File: `dktesting/example_test.go`
```go
package dktesting_test

import (
	"context"
	"testing"
)

import (
	"github.com/dhui/dktest"
)

import (
	"github.com/golang-migrate/migrate/v4/dktesting"
)

func ExampleParallelTest() {
	t := &testing.T{} // Should actually be used in a Test

	var isReady = func(ctx context.Context, c dktest.ContainerInfo) bool {
		// Return true if the container is ready to run tests.
		// Don't block here though. Use the Context to timeout container ready checks.
		return true
	}

	dktesting.ParallelTest(t, []dktesting.ContainerSpec{{ImageName: "docker_image:9.6",
		Options: dktest.Options{ReadyFunc: isReady}}}, func(t *testing.T, c dktest.ContainerInfo) {
		// Run your test/s ...
		t.Fatal("...")
	})
}
```

## File: `internal/cli/build_aws-s3.go`
```go
//go:build aws_s3

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/source/aws_s3"
)
```

## File: `internal/cli/build_bitbucket.go`
```go
//go:build bitbucket

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/source/bitbucket"
)
```

## File: `internal/cli/build_cassandra.go`
```go
//go:build cassandra

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/cassandra"
)
```

## File: `internal/cli/build_clickhouse.go`
```go
//go:build clickhouse

package cli

import (
	_ "github.com/ClickHouse/clickhouse-go"
	_ "github.com/golang-migrate/migrate/v4/database/clickhouse"
)
```

## File: `internal/cli/build_cockroachdb.go`
```go
//go:build cockroachdb

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/cockroachdb"
)
```

## File: `internal/cli/build_firebird.go`
```go
//go:build firebird

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/firebird"
)
```

## File: `internal/cli/build_github.go`
```go
//go:build github

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/source/github"
)
```

## File: `internal/cli/build_github_ee.go`
```go
//go:build github

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/source/github_ee"
)
```

## File: `internal/cli/build_gitlab.go`
```go
//go:build gitlab

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/source/gitlab"
)
```

## File: `internal/cli/build_go-bindata.go`
```go
//go:build go_bindata

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/source/go_bindata"
)
```

## File: `internal/cli/build_godoc-vfs.go`
```go
//go:build godoc_vfs

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/source/godoc_vfs"
)
```

## File: `internal/cli/build_google-cloud-storage.go`
```go
//go:build google_cloud_storage

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/source/google_cloud_storage"
)
```

## File: `internal/cli/build_mongodb.go`
```go
//go:build mongodb

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/mongodb"
)
```

## File: `internal/cli/build_mysql.go`
```go
//go:build mysql

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/mysql"
)
```

## File: `internal/cli/build_neo4j.go`
```go
//go:build neo4j

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/neo4j"
)
```

## File: `internal/cli/build_pgx.go`
```go
//go:build pgx

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/pgx"
)
```

## File: `internal/cli/build_pgxv5.go`
```go
//go:build pgx5

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/pgx/v5"
)
```

## File: `internal/cli/build_postgres.go`
```go
//go:build postgres

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/postgres"
)
```

## File: `internal/cli/build_ql.go`
```go
//go:build ql

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/ql"
)
```

## File: `internal/cli/build_redshift.go`
```go
//go:build redshift

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/redshift"
)
```

## File: `internal/cli/build_rqlite.go`
```go
//go:build rqlite

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/rqlite"
)
```

## File: `internal/cli/build_snowflake.go`
```go
//go:build snowflake

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/snowflake"
)
```

## File: `internal/cli/build_spanner.go`
```go
//go:build spanner

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/spanner"
)
```

## File: `internal/cli/build_sqlcipher.go`
```go
//go:build sqlcipher

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/sqlcipher"
)
```

## File: `internal/cli/build_sqlite.go`
```go
//go:build sqlite

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/sqlite"
)
```

## File: `internal/cli/build_sqlite3.go`
```go
//go:build sqlite3

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/sqlite3"
)
```

## File: `internal/cli/build_sqlserver.go`
```go
//go:build sqlserver

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/sqlserver"
)
```

## File: `internal/cli/build_yugabytedb.go`
```go
//go:build yugabytedb

package cli

import (
	_ "github.com/golang-migrate/migrate/v4/database/yugabytedb"
)
```

## File: `internal/cli/commands.go`
```go
package cli

import (
	"errors"
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"

	"github.com/golang-migrate/migrate/v4"
	_ "github.com/golang-migrate/migrate/v4/database/stub" // TODO remove again
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

var (
	errInvalidSequenceWidth     = errors.New("digits must be positive")
	errIncompatibleSeqAndFormat = errors.New("the seq and format options are mutually exclusive")
	errInvalidTimeFormat        = errors.New("time format may not be empty")
)

func nextSeqVersion(matches []string, seqDigits int) (string, error) {
	if seqDigits <= 0 {
		return "", errInvalidSequenceWidth
	}

	nextSeq := uint64(1)

	if len(matches) > 0 {
		filename := matches[len(matches)-1]
		matchSeqStr := filepath.Base(filename)
		idx := strings.Index(matchSeqStr, "_")

		if idx < 1 { // Using 1 instead of 0 since there should be at least 1 digit
			return "", fmt.Errorf("malformed migration filename: %s", filename)
		}

		var err error
		matchSeqStr = matchSeqStr[0:idx]
		nextSeq, err = strconv.ParseUint(matchSeqStr, 10, 64)

		if err != nil {
			return "", err
		}

		nextSeq++
	}

	version := fmt.Sprintf("%0[2]*[1]d", nextSeq, seqDigits)

	if len(version) > seqDigits {
		return "", fmt.Errorf("next sequence number %s too large, at most %d digits are allowed", version, seqDigits)
	}

	return version, nil
}

func timeVersion(startTime time.Time, format string) (version string, err error) {
	switch format {
	case "":
		err = errInvalidTimeFormat
	case "unix":
		version = strconv.FormatInt(startTime.Unix(), 10)
	case "unixNano":
		version = strconv.FormatInt(startTime.UnixNano(), 10)
	default:
		version = startTime.Format(format)
	}

	return
}

// createCmd (meant to be called via a CLI command) creates a new migration
func createCmd(dir string, startTime time.Time, format string, name string, ext string, seq bool, seqDigits int, print bool) error {
	if seq && format != defaultTimeFormat {
		return errIncompatibleSeqAndFormat
	}

	var version string
	var err error

	dir = filepath.Clean(dir)
	ext = "." + strings.TrimPrefix(ext, ".")

	if seq {
		matches, err := filepath.Glob(filepath.Join(dir, "*"+ext))

		if err != nil {
			return err
		}

		version, err = nextSeqVersion(matches, seqDigits)

		if err != nil {
			return err
		}
	} else {
		version, err = timeVersion(startTime, format)

		if err != nil {
			return err
		}
	}

	versionGlob := filepath.Join(dir, version+"_*"+ext)
	matches, err := filepath.Glob(versionGlob)

	if err != nil {
		return err
	}

	if len(matches) > 0 {
		return fmt.Errorf("duplicate migration version: %s", version)
	}

	if err = os.MkdirAll(dir, os.ModePerm); err != nil {
		return err
	}

	for _, direction := range []string{"up", "down"} {
		basename := fmt.Sprintf("%s_%s.%s%s", version, name, direction, ext)
		filename := filepath.Join(dir, basename)

		if err = createFile(filename); err != nil {
			return err
		}

		if print {
			absPath, _ := filepath.Abs(filename)
			log.Println(absPath)
		}
	}

	return nil
}

func createFile(filename string) error {
	// create exclusive (fails if file already exists)
	// os.Create() specifies 0666 as the FileMode, so we're doing the same
	f, err := os.OpenFile(filename, os.O_RDWR|os.O_CREATE|os.O_EXCL, 0666)

	if err != nil {
		return err
	}

	return f.Close()
}

func gotoCmd(m *migrate.Migrate, v uint) error {
	if err := m.Migrate(v); err != nil {
		if err != migrate.ErrNoChange {
			return err
		}
		log.Println(err)
	}
	return nil
}

func upCmd(m *migrate.Migrate, limit int) error {
	if limit >= 0 {
		if err := m.Steps(limit); err != nil {
			if err != migrate.ErrNoChange {
				return err
			}
			log.Println(err)
		}
	} else {
		if err := m.Up(); err != nil {
			if err != migrate.ErrNoChange {
				return err
			}
			log.Println(err)
		}
	}
	return nil
}

func downCmd(m *migrate.Migrate, limit int) error {
	if limit >= 0 {
		if err := m.Steps(-limit); err != nil {
			if err != migrate.ErrNoChange {
				return err
			}
			log.Println(err)
		}
	} else {
		if err := m.Down(); err != nil {
			if err != migrate.ErrNoChange {
				return err
			}
			log.Println(err)
		}
	}
	return nil
}

func dropCmd(m *migrate.Migrate) error {
	if err := m.Drop(); err != nil {
		return err
	}
	return nil
}

func forceCmd(m *migrate.Migrate, v int) error {
	if err := m.Force(v); err != nil {
		return err
	}
	return nil
}

func versionCmd(m *migrate.Migrate) error {
	v, dirty, err := m.Version()
	if err != nil {
		return err
	}
	if dirty {
		log.Printf("%v (dirty)\n", v)
	} else {
		log.Println(v)
	}
	return nil
}

// numDownMigrationsFromArgs returns an int for number of migrations to apply
// and a bool indicating if we need a confirm before applying
func numDownMigrationsFromArgs(applyAll bool, args []string) (int, bool, error) {
	if applyAll {
		if len(args) > 0 {
			return 0, false, errors.New("-all cannot be used with other arguments")
		}
		return -1, false, nil
	}

	switch len(args) {
	case 0:
		return -1, true, nil
	case 1:
		downValue := args[0]
		n, err := strconv.ParseUint(downValue, 10, 64)
		if err != nil {
			return 0, false, errors.New("can't read limit argument N")
		}
		return int(n), false, nil
	default:
		return 0, false, errors.New("too many arguments")
	}
}
```

## File: `internal/cli/commands_test.go`
```go
package cli

import (
	"errors"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"testing"
	"time"

	"github.com/stretchr/testify/suite"
)

type CreateCmdSuite struct {
	suite.Suite
}

func TestCreateCmdSuite(t *testing.T) {
	suite.Run(t, &CreateCmdSuite{})
}

func (s *CreateCmdSuite) mustCreateTempDir() string {
	tmpDir, err := os.MkdirTemp("", "migrate_")

	if err != nil {
		s.FailNow(err.Error())
	}

	return tmpDir
}

func (s *CreateCmdSuite) mustCreateDir(dir string) {
	if err := os.MkdirAll(dir, 0755); err != nil {
		s.FailNow(err.Error())
	}
}

func (s *CreateCmdSuite) mustRemoveDir(dir string) {
	if err := os.RemoveAll(dir); err != nil {
		s.FailNow(err.Error())
	}
}

func (s *CreateCmdSuite) mustWriteFile(dir, file, body string) {
	if err := os.WriteFile(filepath.Join(dir, file), []byte(body), 0644); err != nil {
		s.FailNow(err.Error())
	}
}

func (s *CreateCmdSuite) mustGetwd() string {
	cwd, err := os.Getwd()

	if err != nil {
		s.FailNow(err.Error())
	}

	return cwd
}

func (s *CreateCmdSuite) mustChdir(dir string) {
	if err := os.Chdir(dir); err != nil {
		s.FailNow(err.Error())
	}
}

func (s *CreateCmdSuite) assertEmptyDir(dir string) bool {
	fis, err := os.ReadDir(dir)

	if err != nil {
		return s.Fail(err.Error())
	}

	return s.Empty(fis)
}

func (s *CreateCmdSuite) TestNextSeqVersion() {
	cases := []struct {
		tid         string
		matches     []string
		seqDigits   int
		expected    string
		expectedErr error
	}{
		{"Bad digits", []string{}, 0, "", errInvalidSequenceWidth},
		{"Single digit initialize", []string{}, 1, "1", nil},
		{"Single digit malformed", []string{"bad"}, 1, "", errors.New("malformed migration filename: bad")},
		{"Single digit no int", []string{"bad_bad"}, 1, "", errors.New(`strconv.ParseUint: parsing "bad": invalid syntax`)},
		{"Single digit negative seq", []string{"-5_test"}, 1, "", errors.New(`strconv.ParseUint: parsing "-5": invalid syntax`)},
		{"Single digit increment", []string{"3_test", "4_test"}, 1, "5", nil},
		{"Single digit overflow", []string{"9_test"}, 1, "", errors.New("next sequence number 10 too large, at most 1 digits are allowed")},
		{"Zero-pad initialize", []string{}, 6, "000001", nil},
		{"Zero-pad malformed", []string{"bad"}, 6, "", errors.New("malformed migration filename: bad")},
		{"Zero-pad no int", []string{"bad_bad"}, 6, "", errors.New(`strconv.ParseUint: parsing "bad": invalid syntax`)},
		{"Zero-pad negative seq", []string{"-000005_test"}, 6, "", errors.New(`strconv.ParseUint: parsing "-000005": invalid syntax`)},
		{"Zero-pad increment", []string{"000003_test", "000004_test"}, 6, "000005", nil},
		{"Zero-pad overflow", []string{"999999_test"}, 6, "", errors.New("next sequence number 1000000 too large, at most 6 digits are allowed")},
		{"dir absolute path", []string{"/migrationDir/000001_test"}, 6, "000002", nil},
		{"dir relative path", []string{"migrationDir/000001_test"}, 6, "000002", nil},
		{"dir dot prefix", []string{"./migrationDir/000001_test"}, 6, "000002", nil},
		{"dir parent prefix", []string{"../migrationDir/000001_test"}, 6, "000002", nil},
		{"dir no prefix", []string{"000001_test"}, 6, "000002", nil},
	}

	for _, c := range cases {
		s.Run(c.tid, func() {
			v, err := nextSeqVersion(c.matches, c.seqDigits)

			if c.expectedErr != nil {
				s.EqualError(err, c.expectedErr.Error())
			} else {
				s.NoError(err)
				s.Equal(c.expected, v)
			}
		})
	}
}

func (s *CreateCmdSuite) TestTimeVersion() {
	ts := time.Date(2000, 12, 25, 00, 01, 02, 3456789, time.UTC)
	tsUnixStr := strconv.FormatInt(ts.Unix(), 10)
	tsUnixNanoStr := strconv.FormatInt(ts.UnixNano(), 10)

	cases := []struct {
		tid         string
		time        time.Time
		format      string
		expected    string
		expectedErr error
	}{
		{"Bad format", ts, "", "", errInvalidTimeFormat},
		{"unix", ts, "unix", tsUnixStr, nil},
		{"unixNano", ts, "unixNano", tsUnixNanoStr, nil},
		{"custom ymthms", ts, "20060102150405", "20001225000102", nil},
	}

	for _, c := range cases {
		s.Run(c.tid, func() {
			v, err := timeVersion(c.time, c.format)

			if c.expectedErr != nil {
				s.EqualError(err, c.expectedErr.Error())
			} else {
				s.NoError(err)
				s.Equal(c.expected, v)
			}
		})
	}
}

// TestCreateCmd tests function createCmd.
//
// For each test case, it creates a temp dir as "sandbox" (called `baseDir`) and
// all path manipulations are relative to `baseDir`.
func (s *CreateCmdSuite) TestCreateCmd() {
	ts := time.Date(2000, 12, 25, 00, 01, 02, 3456789, time.UTC)
	tsUnixStr := strconv.FormatInt(ts.Unix(), 10)
	tsUnixNanoStr := strconv.FormatInt(ts.UnixNano(), 10)
	testCwd := s.mustGetwd()

	cases := []struct {
		tid           string
		existingDirs  []string // directory paths to create before test. relative to baseDir.
		cwd           string   // path to chdir to before test. relative to baseDir.
		existingFiles []string // file paths created before test. relative to baseDir.
		expectedFiles []string // file paths expected to exist after test. paths relative to baseDir.
		expectedErr   error
		dir           string // `dir` parameter. if absolute path, will be converted to baseDir/dir.
		startTime     time.Time
		format        string
		seq           bool
		seqDigits     int
		ext           string
		name          string
	}{
		{"seq and format", nil, "", nil, nil, errIncompatibleSeqAndFormat, ".", ts, "unix", true, 4, "sql", "name"},
		{"seq init dir dot", nil, "", nil, []string{"0001_name.up.sql", "0001_name.down.sql"}, nil, ".", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq init dir dot trailing slash", nil, "", nil, []string{"0001_name.up.sql", "0001_name.down.sql"}, nil, "./", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq init dir double dot", []string{"subdir"}, "subdir", nil, []string{"0001_name.up.sql", "0001_name.down.sql"}, nil, "..", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq init dir double dot trailing slash", []string{"subdir"}, "subdir", nil, []string{"0001_name.up.sql", "0001_name.down.sql"}, nil, "../", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq init dir absolute", []string{"subdir"}, "", nil, []string{"subdir/0001_name.up.sql", "subdir/0001_name.down.sql"}, nil, "/subdir", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq init dir absolute trailing slash", []string{"subdir"}, "", nil, []string{"subdir/0001_name.up.sql", "subdir/0001_name.down.sql"}, nil, "/subdir/", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq init dir relative", []string{"subdir"}, "", nil, []string{"subdir/0001_name.up.sql", "subdir/0001_name.down.sql"}, nil, "subdir", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq init dir relative trailing slash", []string{"subdir"}, "", nil, []string{"subdir/0001_name.up.sql", "subdir/0001_name.down.sql"}, nil, "subdir/", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq init dir dot relative", []string{"subdir"}, "", nil, []string{"subdir/0001_name.up.sql", "subdir/0001_name.down.sql"}, nil, "./subdir", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq init dir dot relative trailing slash", []string{"subdir"}, "", nil, []string{"subdir/0001_name.up.sql", "subdir/0001_name.down.sql"}, nil, "./subdir/", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq init dir double dot relative", []string{"subdir"}, "subdir", nil, []string{"subdir/0001_name.up.sql", "subdir/0001_name.down.sql"}, nil, "../subdir", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq init dir double dot relative trailing slash", []string{"subdir"}, "subdir", nil, []string{"subdir/0001_name.up.sql", "subdir/0001_name.down.sql"}, nil, "../subdir/", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq init dir maze", []string{"subdir"}, "subdir", nil, []string{"0001_name.up.sql", "0001_name.down.sql"}, nil, "..//subdir/./.././/subdir/..", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq width invalid", nil, "", nil, nil, errInvalidSequenceWidth, ".", ts, defaultTimeFormat, true, 0, "sql", "name"},
		{"seq malformed", nil, "", []string{"bad.sql"}, []string{"bad.sql"}, errors.New("malformed migration filename: bad.sql"), ".", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq not int", nil, "", []string{"bad_bad.sql"}, []string{"bad_bad.sql"}, errors.New(`strconv.ParseUint: parsing "bad": invalid syntax`), ".", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq negative", nil, "", []string{"-5_negative.sql"}, []string{"-5_negative.sql"}, errors.New(`strconv.ParseUint: parsing "-5": invalid syntax`), ".", ts, defaultTimeFormat, true, 4, "sql", "name"},
		{"seq increment", nil, "", []string{"3_three.sql", "4_four.sql"}, []string{"3_three.sql", "4_four.sql", "0005_five.up.sql", "0005_five.down.sql"}, nil, ".", ts, defaultTimeFormat, true, 4, "sql", "five"},
		{"seq overflow", nil, "", []string{"9_nine.sql"}, []string{"9_nine.sql"}, errors.New(`next sequence number 10 too large, at most 1 digits are allowed`), ".", ts, defaultTimeFormat, true, 1, "sql", "ten"},
		{"time empty format", nil, "", nil, nil, errInvalidTimeFormat, ".", ts, "", false, 0, "sql", "name"},
		{"time unix", nil, "", nil, []string{tsUnixStr + "_name.up.sql", tsUnixStr + "_name.down.sql"}, nil, ".", ts, "unix", false, 0, "sql", "name"},
		{"time unixNano", nil, "", nil, []string{tsUnixNanoStr + "_name.up.sql", tsUnixNanoStr + "_name.down.sql"}, nil, ".", ts, "unixNano", false, 0, "sql", "name"},
		{"time custom format", nil, "", nil, []string{"20001225000102_name.up.sql", "20001225000102_name.down.sql"}, nil, ".", ts, "20060102150405", false, 0, "sql", "name"},
		{"time version collision", nil, "", []string{"20001225_name.up.sql", "20001225_name.down.sql"}, []string{"20001225_name.up.sql", "20001225_name.down.sql"}, errors.New("duplicate migration version: 20001225"), ".", ts, "20060102", false, 0, "sql", "name"},
		{"dir invalid", nil, "", []string{"file"}, []string{"file"}, errors.New("mkdir 'test: this is invalid dir name'\x00: invalid argument"), "'test: this is invalid dir name'\000", ts, "unix", false, 0, "sql", "name"},
	}

	for _, c := range cases {
		s.Run(c.tid, func() {
			baseDir := s.mustCreateTempDir()

			for _, d := range c.existingDirs {
				s.mustCreateDir(filepath.Join(baseDir, d))
			}

			cwd := baseDir

			if c.cwd != "" {
				cwd = filepath.Join(baseDir, c.cwd)
			}

			s.mustChdir(cwd)

			for _, f := range c.existingFiles {
				s.mustWriteFile(baseDir, f, "")
			}

			dir := c.dir
			dir = filepath.ToSlash(dir)
			volName := filepath.VolumeName(baseDir)
			// Windows specific, can not recognize \subdir as abs path
			isWindowsAbsPathNoLetter := strings.HasPrefix(dir, "/") && volName != ""
			isRealAbsPath := filepath.IsAbs(dir)
			if isWindowsAbsPathNoLetter || isRealAbsPath {
				dir = filepath.Join(baseDir, dir)
			}

			err := createCmd(dir, c.startTime, c.format, c.name, c.ext, c.seq, c.seqDigits, false)

			if c.expectedErr != nil {
				s.EqualError(err, c.expectedErr.Error())
			} else {
				s.NoError(err)
			}

			if len(c.expectedFiles) == 0 {
				s.assertEmptyDir(baseDir)
			} else {
				for _, f := range c.expectedFiles {
					s.FileExists(filepath.Join(baseDir, f))
				}
			}

			s.mustChdir(testCwd)
			s.mustRemoveDir(baseDir)
		})
	}
}

func TestNumDownFromArgs(t *testing.T) {
	cases := []struct {
		name                string
		args                []string
		applyAll            bool
		expectedNeedConfirm bool
		expectedNum         int
		expectedErrStr      string
	}{
		{"no args", []string{}, false, true, -1, ""},
		{"down all", []string{}, true, false, -1, ""},
		{"down 5", []string{"5"}, false, false, 5, ""},
		{"down N", []string{"N"}, false, false, 0, "can't read limit argument N"},
		{"extra arg after -all", []string{"5"}, true, false, 0, "-all cannot be used with other arguments"},
		{"extra arg before -all", []string{"5", "-all"}, false, false, 0, "too many arguments"},
	}
	for _, c := range cases {
		t.Run(c.name, func(t *testing.T) {
			num, needsConfirm, err := numDownMigrationsFromArgs(c.applyAll, c.args)
			if needsConfirm != c.expectedNeedConfirm {
				t.Errorf("Incorrect needsConfirm was: %v wanted %v", needsConfirm, c.expectedNeedConfirm)
			}

			if num != c.expectedNum {
				t.Errorf("Incorrect num was: %v wanted %v", num, c.expectedNum)
			}

			if err != nil {
				if err.Error() != c.expectedErrStr {
					t.Error("Incorrect error: " + err.Error() + " != " + c.expectedErrStr)
				}
			} else if c.expectedErrStr != "" {
				t.Error("Expected error: " + c.expectedErrStr + " but got nil instead")
			}
		})
	}
}
```

## File: `internal/cli/log.go`
```go
package cli

import (
	"fmt"
	logpkg "log"
	"os"
)

// Log represents the logger
type Log struct {
	verbose bool
}

// Printf prints out formatted string into a log
func (l *Log) Printf(format string, v ...interface{}) {
	if l.verbose {
		logpkg.Printf(format, v...)
	} else {
		fmt.Fprintf(os.Stderr, format, v...)
	}
}

// Println prints out args into a log
func (l *Log) Println(args ...interface{}) {
	if l.verbose {
		logpkg.Println(args...)
	} else {
		fmt.Fprintln(os.Stderr, args...)
	}
}

// Verbose shows if verbose print enabled
func (l *Log) Verbose() bool {
	return l.verbose
}

func (l *Log) fatal(args ...interface{}) {
	l.Println(args...)
	os.Exit(1)
}

func (l *Log) fatalErr(err error) {
	l.fatal("error:", err)
}
```

## File: `internal/cli/main.go`
```go
package cli

import (
	"flag"
	"fmt"
	"os"
	"os/signal"
	"strconv"
	"strings"
	"syscall"
	"time"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database"
	"github.com/golang-migrate/migrate/v4/source"
)

const (
	defaultTimeFormat = "20060102150405"
	defaultTimezone   = "UTC"
	createUsage       = `create [-ext E] [-dir D] [-seq] [-digits N] [-format] [-tz] NAME
	   Create a set of timestamped up/down migrations titled NAME, in directory D with extension E.
	   Use -seq option to generate sequential up/down migrations with N digits.
	   Use -format option to specify a Go time format string. Note: migrations with the same time cause "duplicate migration version" error.
           Use -tz option to specify the timezone that will be used when generating non-sequential migrations (defaults: UTC).
`
	gotoUsage = `goto V       Migrate to version V`
	upUsage   = `up [N]       Apply all or N up migrations`
	downUsage = `down [N] [-all]    Apply all or N down migrations
	Use -all to apply all down migrations`
	dropUsage = `drop [-f]    Drop everything inside database
	Use -f to bypass confirmation`
	forceUsage = `force V      Set version V but don't run migration (ignores dirty state)`
)

func handleSubCmdHelp(help bool, usage string, flagSet *flag.FlagSet) {
	if help {
		fmt.Fprintln(os.Stderr, usage)
		flagSet.PrintDefaults()
		os.Exit(0)
	}
}

func newFlagSetWithHelp(name string) (*flag.FlagSet, *bool) {
	flagSet := flag.NewFlagSet(name, flag.ExitOnError)
	helpPtr := flagSet.Bool("help", false, "Print help information")
	return flagSet, helpPtr
}

// set main log
var log = &Log{}

func printUsageAndExit() {
	flag.Usage()

	// If a command is not found we exit with a status 2 to match the behavior
	// of flag.Parse() with flag.ExitOnError when parsing an invalid flag.
	os.Exit(2)
}

// Main function of a cli application. It is public for backwards compatibility with `cli` package
func Main(version string) {
	helpPtr := flag.Bool("help", false, "")
	versionPtr := flag.Bool("version", false, "")
	verbosePtr := flag.Bool("verbose", false, "")
	prefetchPtr := flag.Uint("prefetch", 10, "")
	lockTimeoutPtr := flag.Uint("lock-timeout", 15, "")
	pathPtr := flag.String("path", "", "")
	databasePtr := flag.String("database", "", "")
	sourcePtr := flag.String("source", "", "")

	flag.Usage = func() {
		fmt.Fprintf(os.Stderr,
			`Usage: migrate OPTIONS COMMAND [arg...]
       migrate [ -version | -help ]

Options:
  -source          Location of the migrations (driver://url)
  -path            Shorthand for -source=file://path
  -database        Run migrations against this database (driver://url)
  -prefetch N      Number of migrations to load in advance before executing (default 10)
  -lock-timeout N  Allow N seconds to acquire database lock (default 15)
  -verbose         Print verbose logging
  -version         Print version
  -help            Print usage

Commands:
  %s
  %s
  %s
  %s
  %s
  %s
  version      Print current migration version

Source drivers: `+strings.Join(source.List(), ", ")+`
Database drivers: `+strings.Join(database.List(), ", ")+"\n", createUsage, gotoUsage, upUsage, downUsage, dropUsage, forceUsage)
	}

	flag.Parse()

	// initialize logger
	log.verbose = *verbosePtr

	// show cli version
	if *versionPtr {
		fmt.Fprintln(os.Stderr, version)
		os.Exit(0)
	}

	// show help
	if *helpPtr {
		flag.Usage()
		os.Exit(0)
	}

	// translate -path into -source if given
	if *sourcePtr == "" && *pathPtr != "" {
		*sourcePtr = fmt.Sprintf("file://%v", *pathPtr)
	}

	// initialize migrate
	// don't catch migraterErr here and let each command decide
	// how it wants to handle the error
	migrater, migraterErr := migrate.New(*sourcePtr, *databasePtr)
	defer func() {
		if migraterErr == nil {
			if _, err := migrater.Close(); err != nil {
				log.Println(err)
			}
		}
	}()
	if migraterErr == nil {
		migrater.Log = log
		migrater.PrefetchMigrations = *prefetchPtr
		migrater.LockTimeout = time.Duration(int64(*lockTimeoutPtr)) * time.Second

		// handle Ctrl+c
		signals := make(chan os.Signal, 1)
		signal.Notify(signals, syscall.SIGINT)
		go func() {
			for range signals {
				log.Println("Stopping after this running migration ...")
				migrater.GracefulStop <- true
				return
			}
		}()
	}

	startTime := time.Now()

	if len(flag.Args()) < 1 {
		printUsageAndExit()
	}
	args := flag.Args()[1:]

	switch flag.Arg(0) {
	case "create":

		seq := false
		seqDigits := 6

		createFlagSet, help := newFlagSetWithHelp("create")
		extPtr := createFlagSet.String("ext", "", "File extension")
		dirPtr := createFlagSet.String("dir", "", "Directory to place file in (default: current working directory)")
		formatPtr := createFlagSet.String("format", defaultTimeFormat, `The Go time format string to use. If the string "unix" or "unixNano" is specified, then the seconds or nanoseconds since January 1, 1970 UTC respectively will be used. Caution, due to the behavior of time.Time.Format(), invalid format strings will not error`)
		timezoneName := createFlagSet.String("tz", defaultTimezone, `The timezone that will be used for generating timestamps (default: utc)`)
		createFlagSet.BoolVar(&seq, "seq", seq, "Use sequential numbers instead of timestamps (default: false)")
		createFlagSet.IntVar(&seqDigits, "digits", seqDigits, "The number of digits to use in sequences (default: 6)")

		if err := createFlagSet.Parse(args); err != nil {
			log.fatalErr(err)
		}

		handleSubCmdHelp(*help, createUsage, createFlagSet)

		if createFlagSet.NArg() == 0 {
			log.fatal("error: please specify name")
		}
		name := createFlagSet.Arg(0)

		if *extPtr == "" {
			log.fatal("error: -ext flag must be specified")
		}

		timezone, err := time.LoadLocation(*timezoneName)
		if err != nil {
			log.fatal(err)
		}

		if err := createCmd(*dirPtr, startTime.In(timezone), *formatPtr, name, *extPtr, seq, seqDigits, true); err != nil {
			log.fatalErr(err)
		}

	case "goto":

		gotoSet, helpPtr := newFlagSetWithHelp("goto")

		if err := gotoSet.Parse(args); err != nil {
			log.fatalErr(err)
		}

		handleSubCmdHelp(*helpPtr, gotoUsage, gotoSet)

		if migraterErr != nil {
			log.fatalErr(migraterErr)
		}

		if gotoSet.NArg() == 0 {
			log.fatal("error: please specify version argument V")
		}

		v, err := strconv.ParseUint(gotoSet.Arg(0), 10, 64)
		if err != nil {
			log.fatal("error: can't read version argument V")
		}

		if err := gotoCmd(migrater, uint(v)); err != nil {
			log.fatalErr(err)
		}

		if log.verbose {
			log.Println("Finished after", time.Since(startTime))
		}

	case "up":
		upSet, helpPtr := newFlagSetWithHelp("up")

		if err := upSet.Parse(args); err != nil {
			log.fatalErr(err)
		}

		handleSubCmdHelp(*helpPtr, upUsage, upSet)

		if migraterErr != nil {
			log.fatalErr(migraterErr)
		}

		limit := -1
		if upSet.NArg() > 0 {
			n, err := strconv.ParseUint(upSet.Arg(0), 10, 64)
			if err != nil {
				log.fatal("error: can't read limit argument N")
			}
			limit = int(n)
		}

		if err := upCmd(migrater, limit); err != nil {
			log.fatalErr(err)
		}

		if log.verbose {
			log.Println("Finished after", time.Since(startTime))
		}

	case "down":
		downFlagSet, helpPtr := newFlagSetWithHelp("down")
		applyAll := downFlagSet.Bool("all", false, "Apply all down migrations")

		if err := downFlagSet.Parse(args); err != nil {
			log.fatalErr(err)
		}

		handleSubCmdHelp(*helpPtr, downUsage, downFlagSet)

		if migraterErr != nil {
			log.fatalErr(migraterErr)
		}

		downArgs := downFlagSet.Args()
		num, needsConfirm, err := numDownMigrationsFromArgs(*applyAll, downArgs)
		if err != nil {
			log.fatalErr(err)
		}
		if needsConfirm {
			log.Println("Are you sure you want to apply all down migrations? [y/N]")
			var response string
			_, _ = fmt.Scanln(&response)
			response = strings.ToLower(strings.TrimSpace(response))

			if response == "y" {
				log.Println("Applying all down migrations")
			} else {
				log.fatal("Not applying all down migrations")
			}
		}

		if err := downCmd(migrater, num); err != nil {
			log.fatalErr(err)
		}

		if log.verbose {
			log.Println("Finished after", time.Since(startTime))
		}

	case "drop":
		dropFlagSet, help := newFlagSetWithHelp("drop")
		forceDrop := dropFlagSet.Bool("f", false, "Force the drop command by bypassing the confirmation prompt")

		if err := dropFlagSet.Parse(args); err != nil {
			log.fatalErr(err)
		}

		handleSubCmdHelp(*help, dropUsage, dropFlagSet)

		if !*forceDrop {
			log.Println("Are you sure you want to drop the entire database schema? [y/N]")
			var response string
			_, _ = fmt.Scanln(&response)
			response = strings.ToLower(strings.TrimSpace(response))

			if response == "y" {
				log.Println("Dropping the entire database schema")
			} else {
				log.fatal("Aborted dropping the entire database schema")
			}
		}

		if migraterErr != nil {
			log.fatalErr(migraterErr)
		}

		if err := dropCmd(migrater); err != nil {
			log.fatalErr(err)
		}

		if log.verbose {
			log.Println("Finished after", time.Since(startTime))
		}

	case "force":
		forceSet, helpPtr := newFlagSetWithHelp("force")

		if err := forceSet.Parse(args); err != nil {
			log.fatalErr(err)
		}

		handleSubCmdHelp(*helpPtr, forceUsage, forceSet)

		if migraterErr != nil {
			log.fatalErr(migraterErr)
		}

		if forceSet.NArg() == 0 {
			log.fatal("error: please specify version argument V")
		}

		v, err := strconv.ParseInt(forceSet.Arg(0), 10, 64)
		if err != nil {
			log.fatal("error: can't read version argument V")
		}

		if v < -1 {
			log.fatal("error: argument V must be >= -1")
		}

		if err := forceCmd(migrater, int(v)); err != nil {
			log.fatalErr(err)
		}

		if log.verbose {
			log.Println("Finished after", time.Since(startTime))
		}

	case "version":
		if migraterErr != nil {
			log.fatalErr(migraterErr)
		}

		if err := versionCmd(migrater); err != nil {
			log.fatalErr(err)
		}

	default:
		printUsageAndExit()
	}
}
```

## File: `internal/url/url.go`
```go
package url

import (
	"errors"
	"strings"
)

var errNoScheme = errors.New("no scheme")
var errEmptyURL = errors.New("URL cannot be empty")

// schemeFromURL returns the scheme from a URL string
func SchemeFromURL(url string) (string, error) {
	if url == "" {
		return "", errEmptyURL
	}

	i := strings.Index(url, ":")

	// No : or : is the first character.
	if i < 1 {
		return "", errNoScheme
	}

	return url[0:i], nil
}
```

## File: `internal/url/url_test.go`
```go
package url

import (
	"testing"
)

func TestSchemeFromUrl(t *testing.T) {
	cases := []struct {
		name      string
		urlStr    string
		expected  string
		expectErr error
	}{
		{
			name:     "Simple",
			urlStr:   "protocol://path",
			expected: "protocol",
		},
		{
			// See issue #264
			name:     "MySQLWithPort",
			urlStr:   "mysql://user:pass@tcp(host:1337)/db",
			expected: "mysql",
		},
		{
			name:      "Empty",
			urlStr:    "",
			expectErr: errEmptyURL,
		},
		{
			name:      "NoScheme",
			urlStr:    "hello",
			expectErr: errNoScheme,
		},
	}

	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			s, err := SchemeFromURL(tc.urlStr)
			if err != tc.expectErr {
				t.Fatalf("expected %q, but received %q", tc.expectErr, err)
			}
			if s != tc.expected {
				t.Fatalf("expected %q, but received %q", tc.expected, s)
			}
		})
	}
}
```

## File: `source/driver.go`
```go
// Package source provides the Source interface.
// All source drivers must implement this interface, register themselves,
// optionally provide a `WithInstance` function and pass the tests
// in package source/testing.
package source

import (
	"fmt"
	"io"
	nurl "net/url"
	"sync"
)

var driversMu sync.RWMutex
var drivers = make(map[string]Driver)

// Driver is the interface every source driver must implement.
//
// How to implement a source driver?
//  1. Implement this interface.
//  2. Optionally, add a function named `WithInstance`.
//     This function should accept an existing source instance and a Config{} struct
//     and return a driver instance.
//  3. Add a test that calls source/testing.go:Test()
//  4. Add own tests for Open(), WithInstance() (when provided) and Close().
//     All other functions are tested by tests in source/testing.
//     Saves you some time and makes sure all source drivers behave the same way.
//  5. Call Register in init().
//
// Guidelines:
//   - All configuration input must come from the URL string in func Open()
//     or the Config{} struct in WithInstance. Don't os.Getenv().
//   - Drivers are supposed to be read only.
//   - Ideally don't load any contents (into memory) in Open or WithInstance.
type Driver interface {
	// Open returns a new driver instance configured with parameters
	// coming from the URL string. Migrate will call this function
	// only once per instance.
	Open(url string) (Driver, error)

	// Close closes the underlying source instance managed by the driver.
	// Migrate will call this function only once per instance.
	Close() error

	// First returns the very first migration version available to the driver.
	// Migrate will call this function multiple times.
	// If there is no version available, it must return os.ErrNotExist.
	First() (version uint, err error)

	// Prev returns the previous version for a given version available to the driver.
	// Migrate will call this function multiple times.
	// If there is no previous version available, it must return os.ErrNotExist.
	Prev(version uint) (prevVersion uint, err error)

	// Next returns the next version for a given version available to the driver.
	// Migrate will call this function multiple times.
	// If there is no next version available, it must return os.ErrNotExist.
	Next(version uint) (nextVersion uint, err error)

	// ReadUp returns the UP migration body and an identifier that helps
	// finding this migration in the source for a given version.
	// If there is no up migration available for this version,
	// it must return os.ErrNotExist.
	// Do not start reading, just return the ReadCloser!
	ReadUp(version uint) (r io.ReadCloser, identifier string, err error)

	// ReadDown returns the DOWN migration body and an identifier that helps
	// finding this migration in the source for a given version.
	// If there is no down migration available for this version,
	// it must return os.ErrNotExist.
	// Do not start reading, just return the ReadCloser!
	ReadDown(version uint) (r io.ReadCloser, identifier string, err error)
}

// Open returns a new driver instance.
func Open(url string) (Driver, error) {
	u, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}

	if u.Scheme == "" {
		return nil, fmt.Errorf("source driver: invalid URL scheme")
	}

	driversMu.RLock()
	d, ok := drivers[u.Scheme]
	driversMu.RUnlock()
	if !ok {
		return nil, fmt.Errorf("source driver: unknown driver '%s' (forgotten import?)", u.Scheme)
	}

	return d.Open(url)
}

// Register globally registers a driver.
func Register(name string, driver Driver) {
	driversMu.Lock()
	defer driversMu.Unlock()
	if driver == nil {
		panic("Register driver is nil")
	}
	if _, dup := drivers[name]; dup {
		panic("Register called twice for driver " + name)
	}
	drivers[name] = driver
}

// List lists the registered drivers
func List() []string {
	driversMu.RLock()
	defer driversMu.RUnlock()
	names := make([]string, 0, len(drivers))
	for n := range drivers {
		names = append(names, n)
	}
	return names
}
```

## File: `source/driver_test.go`
```go
package source

func ExampleDriver() {
	// see source/stub for an example

	// source/stub/stub.go has the driver implementation
	// source/stub/stub_test.go runs source/testing/test.go:Test
}
```

## File: `source/errors.go`
```go
package source

import "os"

// ErrDuplicateMigration is an error type for reporting duplicate migration
// files.
type ErrDuplicateMigration struct {
	Migration
	os.FileInfo
}

// Error implements error interface.
func (e ErrDuplicateMigration) Error() string {
	return "duplicate migration file: " + e.Name()
}
```

## File: `source/migration.go`
```go
package source

import (
	"sort"
)

// Direction is either up or down.
type Direction string

const (
	Down Direction = "down"
	Up   Direction = "up"
)

// Migration is a helper struct for source drivers that need to
// build the full directory tree in memory.
// Migration is fully independent from migrate.Migration.
type Migration struct {
	// Version is the version of this migration.
	Version uint

	// Identifier can be any string that helps identifying
	// this migration in the source.
	Identifier string

	// Direction is either Up or Down.
	Direction Direction

	// Raw holds the raw location path to this migration in source.
	// ReadUp and ReadDown will use this.
	Raw string
}

// Migrations wraps Migration and has an internal index
// to keep track of Migration order.
type Migrations struct {
	index      uintSlice
	migrations map[uint]map[Direction]*Migration
}

func NewMigrations() *Migrations {
	return &Migrations{
		index:      make(uintSlice, 0),
		migrations: make(map[uint]map[Direction]*Migration),
	}
}

func (i *Migrations) Append(m *Migration) (ok bool) {
	if m == nil {
		return false
	}

	if i.migrations[m.Version] == nil {
		i.migrations[m.Version] = make(map[Direction]*Migration)
	}

	// reject duplicate versions
	if _, dup := i.migrations[m.Version][m.Direction]; dup {
		return false
	}

	i.migrations[m.Version][m.Direction] = m
	i.buildIndex()

	return true
}

func (i *Migrations) buildIndex() {
	i.index = make(uintSlice, 0, len(i.migrations))
	for version := range i.migrations {
		i.index = append(i.index, version)
	}
	sort.Slice(i.index, func(x, y int) bool {
		return i.index[x] < i.index[y]
	})
}

func (i *Migrations) First() (version uint, ok bool) {
	if len(i.index) == 0 {
		return 0, false
	}
	return i.index[0], true
}

func (i *Migrations) Prev(version uint) (prevVersion uint, ok bool) {
	pos := i.findPos(version)
	if pos >= 1 && len(i.index) > pos-1 {
		return i.index[pos-1], true
	}
	return 0, false
}

func (i *Migrations) Next(version uint) (nextVersion uint, ok bool) {
	pos := i.findPos(version)
	if pos >= 0 && len(i.index) > pos+1 {
		return i.index[pos+1], true
	}
	return 0, false
}

func (i *Migrations) Up(version uint) (m *Migration, ok bool) {
	if _, ok := i.migrations[version]; ok {
		if mx, ok := i.migrations[version][Up]; ok {
			return mx, true
		}
	}
	return nil, false
}

func (i *Migrations) Down(version uint) (m *Migration, ok bool) {
	if _, ok := i.migrations[version]; ok {
		if mx, ok := i.migrations[version][Down]; ok {
			return mx, true
		}
	}
	return nil, false
}

func (i *Migrations) findPos(version uint) int {
	if len(i.index) > 0 {
		ix := i.index.Search(version)
		if ix < len(i.index) && i.index[ix] == version {
			return ix
		}
	}
	return -1
}

type uintSlice []uint

func (s uintSlice) Search(x uint) int {
	return sort.Search(len(s), func(i int) bool { return s[i] >= x })
}
```

## File: `source/migration_test.go`
```go
package source

import (
	"testing"
)

func TestNewMigrations(t *testing.T) {
	// TODO
}

func TestAppend(t *testing.T) {
	// TODO
}

func TestBuildIndex(t *testing.T) {
	// TODO
}

func TestFirst(t *testing.T) {
	// TODO
}

func TestPrev(t *testing.T) {
	// TODO
}

func TestUp(t *testing.T) {
	// TODO
}

func TestDown(t *testing.T) {
	// TODO
}

func TestFindPos(t *testing.T) {
	m := Migrations{index: uintSlice{1, 2, 3}}
	if p := m.findPos(0); p != -1 {
		t.Errorf("expected -1, got %v", p)
	}
	if p := m.findPos(1); p != 0 {
		t.Errorf("expected 0, got %v", p)
	}
	if p := m.findPos(3); p != 2 {
		t.Errorf("expected 2, got %v", p)
	}
}
```

## File: `source/parse.go`
```go
package source

import (
	"fmt"
	"regexp"
	"strconv"
)

var (
	ErrParse = fmt.Errorf("no match")
)

var (
	DefaultParse = Parse
	DefaultRegex = Regex
)

// Regex matches the following pattern:
//
//	123_name.up.ext
//	123_name.down.ext
var Regex = regexp.MustCompile(`^([0-9]+)_(.*)\.(` + string(Down) + `|` + string(Up) + `)\.(.*)$`)

// Parse returns Migration for matching Regex pattern.
func Parse(raw string) (*Migration, error) {
	m := Regex.FindStringSubmatch(raw)
	if len(m) == 5 {
		versionUint64, err := strconv.ParseUint(m[1], 10, 64)
		if err != nil {
			return nil, err
		}
		return &Migration{
			Version:    uint(versionUint64),
			Identifier: m[2],
			Direction:  Direction(m[3]),
			Raw:        raw,
		}, nil
	}
	return nil, ErrParse
}
```

## File: `source/parse_test.go`
```go
package source

import (
	"testing"
)

func TestParse(t *testing.T) {
	tt := []struct {
		name            string
		expectErr       error
		expectMigration *Migration
	}{
		{
			name:      "1_foobar.up.sql",
			expectErr: nil,
			expectMigration: &Migration{
				Version:    1,
				Identifier: "foobar",
				Direction:  Up,
				Raw:        "1_foobar.up.sql",
			},
		},
		{
			name:      "1_foobar.down.sql",
			expectErr: nil,
			expectMigration: &Migration{
				Version:    1,
				Identifier: "foobar",
				Direction:  Down,
				Raw:        "1_foobar.down.sql",
			},
		},
		{
			name:      "1_f-o_ob+ar.up.sql",
			expectErr: nil,
			expectMigration: &Migration{
				Version:    1,
				Identifier: "f-o_ob+ar",
				Direction:  Up,
				Raw:        "1_f-o_ob+ar.up.sql",
			},
		},
		{
			name:      "1485385885_foobar.up.sql",
			expectErr: nil,
			expectMigration: &Migration{
				Version:    1485385885,
				Identifier: "foobar",
				Direction:  Up,
				Raw:        "1485385885_foobar.up.sql",
			},
		},
		{
			name:      "20170412214116_date_foobar.up.sql",
			expectErr: nil,
			expectMigration: &Migration{
				Version:    20170412214116,
				Identifier: "date_foobar",
				Direction:  Up,
				Raw:        "20170412214116_date_foobar.up.sql",
			},
		},
		{
			name:            "-1_foobar.up.sql",
			expectErr:       ErrParse,
			expectMigration: nil,
		},
		{
			name:            "foobar.up.sql",
			expectErr:       ErrParse,
			expectMigration: nil,
		},
		{
			name:            "1.up.sql",
			expectErr:       ErrParse,
			expectMigration: nil,
		},
		{
			name:            "1_foobar.sql",
			expectErr:       ErrParse,
			expectMigration: nil,
		},
		{
			name:            "1_foobar.up",
			expectErr:       ErrParse,
			expectMigration: nil,
		},
		{
			name:            "1_foobar.down",
			expectErr:       ErrParse,
			expectMigration: nil,
		},
	}

	for i, v := range tt {
		f, err := Parse(v.name)

		if err != v.expectErr {
			t.Errorf("expected %v, got %v, in %v", v.expectErr, err, i)
		}

		if v.expectMigration != nil && *f != *v.expectMigration {
			t.Errorf("expected %+v, got %+v, in %v", *v.expectMigration, *f, i)
		}
	}
}
```

## File: `source/aws_s3/README.md`
```markdown
# aws_s3

`s3://<bucket>/<prefix>`
```

## File: `source/aws_s3/s3.go`
```go
package awss3

import (
	"fmt"
	"io"
	"net/url"
	"os"
	"path"
	"strings"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
	"github.com/aws/aws-sdk-go/service/s3/s3iface"
	"github.com/golang-migrate/migrate/v4/source"
)

func init() {
	source.Register("s3", &s3Driver{})
}

type s3Driver struct {
	s3client   s3iface.S3API
	config     *Config
	migrations *source.Migrations
}

type Config struct {
	Bucket string
	Prefix string
}

func (s *s3Driver) Open(folder string) (source.Driver, error) {
	config, err := parseURI(folder)
	if err != nil {
		return nil, err
	}

	sess, err := session.NewSession()
	if err != nil {
		return nil, err
	}

	return WithInstance(s3.New(sess), config)
}

func WithInstance(s3client s3iface.S3API, config *Config) (source.Driver, error) {
	driver := &s3Driver{
		config:     config,
		s3client:   s3client,
		migrations: source.NewMigrations(),
	}

	if err := driver.loadMigrations(); err != nil {
		return nil, err
	}

	return driver, nil
}

func parseURI(uri string) (*Config, error) {
	u, err := url.Parse(uri)
	if err != nil {
		return nil, err
	}

	prefix := strings.Trim(u.Path, "/")
	if prefix != "" {
		prefix += "/"
	}

	return &Config{
		Bucket: u.Host,
		Prefix: prefix,
	}, nil
}

func (s *s3Driver) loadMigrations() error {
	output, err := s.s3client.ListObjects(&s3.ListObjectsInput{
		Bucket:    aws.String(s.config.Bucket),
		Prefix:    aws.String(s.config.Prefix),
		Delimiter: aws.String("/"),
	})
	if err != nil {
		return err
	}
	for _, object := range output.Contents {
		_, fileName := path.Split(aws.StringValue(object.Key))
		m, err := source.DefaultParse(fileName)
		if err != nil {
			continue
		}
		if !s.migrations.Append(m) {
			return fmt.Errorf("unable to parse file %v", aws.StringValue(object.Key))
		}
	}
	return nil
}

func (s *s3Driver) Close() error {
	return nil
}

func (s *s3Driver) First() (uint, error) {
	v, ok := s.migrations.First()
	if !ok {
		return 0, os.ErrNotExist
	}
	return v, nil
}

func (s *s3Driver) Prev(version uint) (uint, error) {
	v, ok := s.migrations.Prev(version)
	if !ok {
		return 0, os.ErrNotExist
	}
	return v, nil
}

func (s *s3Driver) Next(version uint) (uint, error) {
	v, ok := s.migrations.Next(version)
	if !ok {
		return 0, os.ErrNotExist
	}
	return v, nil
}

func (s *s3Driver) ReadUp(version uint) (io.ReadCloser, string, error) {
	if m, ok := s.migrations.Up(version); ok {
		return s.open(m)
	}
	return nil, "", os.ErrNotExist
}

func (s *s3Driver) ReadDown(version uint) (io.ReadCloser, string, error) {
	if m, ok := s.migrations.Down(version); ok {
		return s.open(m)
	}
	return nil, "", os.ErrNotExist
}

func (s *s3Driver) open(m *source.Migration) (io.ReadCloser, string, error) {
	key := path.Join(s.config.Prefix, m.Raw)
	object, err := s.s3client.GetObject(&s3.GetObjectInput{
		Bucket: aws.String(s.config.Bucket),
		Key:    aws.String(key),
	})
	if err != nil {
		return nil, "", err
	}
	return object.Body, m.Identifier, nil
}
```

## File: `source/aws_s3/s3_test.go`
```go
package awss3

import (
	"errors"
	"io"
	"strings"
	"testing"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/service/s3"
	st "github.com/golang-migrate/migrate/v4/source/testing"
	"github.com/stretchr/testify/assert"
)

func Test(t *testing.T) {
	s3Client := fakeS3{
		bucket: "some-bucket",
		objects: map[string]string{
			"staging/migrations/1_foobar.up.sql":          "1 up",
			"staging/migrations/1_foobar.down.sql":        "1 down",
			"prod/migrations/1_foobar.up.sql":             "1 up",
			"prod/migrations/1_foobar.down.sql":           "1 down",
			"prod/migrations/3_foobar.up.sql":             "3 up",
			"prod/migrations/4_foobar.up.sql":             "4 up",
			"prod/migrations/4_foobar.down.sql":           "4 down",
			"prod/migrations/5_foobar.down.sql":           "5 down",
			"prod/migrations/7_foobar.up.sql":             "7 up",
			"prod/migrations/7_foobar.down.sql":           "7 down",
			"prod/migrations/not-a-migration.txt":         "",
			"prod/migrations/0-random-stuff/whatever.txt": "",
		},
	}
	driver, err := WithInstance(&s3Client, &Config{
		Bucket: "some-bucket",
		Prefix: "prod/migrations/",
	})
	if err != nil {
		t.Fatal(err)
	}
	st.Test(t, driver)
}

func TestParseURI(t *testing.T) {
	tests := []struct {
		name   string
		uri    string
		config *Config
	}{
		{
			"with prefix, no trailing slash",
			"s3://migration-bucket/production",
			&Config{
				Bucket: "migration-bucket",
				Prefix: "production/",
			},
		},
		{
			"without prefix, no trailing slash",
			"s3://migration-bucket",
			&Config{
				Bucket: "migration-bucket",
			},
		},
		{
			"with prefix, trailing slash",
			"s3://migration-bucket/production/",
			&Config{
				Bucket: "migration-bucket",
				Prefix: "production/",
			},
		},
		{
			"without prefix, trailing slash",
			"s3://migration-bucket/",
			&Config{
				Bucket: "migration-bucket",
			},
		},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			actual, err := parseURI(test.uri)
			if err != nil {
				t.Fatal(err)
			}
			assert.Equal(t, test.config, actual)
		})
	}
}

type fakeS3 struct {
	s3.S3
	bucket  string
	objects map[string]string
}

func (s *fakeS3) ListObjects(input *s3.ListObjectsInput) (*s3.ListObjectsOutput, error) {
	bucket := aws.StringValue(input.Bucket)
	if bucket != s.bucket {
		return nil, errors.New("bucket not found")
	}
	prefix := aws.StringValue(input.Prefix)
	delimiter := aws.StringValue(input.Delimiter)
	var output s3.ListObjectsOutput
	for name := range s.objects {
		if strings.HasPrefix(name, prefix) {
			if delimiter == "" || !strings.Contains(strings.Replace(name, prefix, "", 1), delimiter) {
				output.Contents = append(output.Contents, &s3.Object{
					Key: aws.String(name),
				})
			}
		}
	}
	return &output, nil
}

func (s *fakeS3) GetObject(input *s3.GetObjectInput) (*s3.GetObjectOutput, error) {
	bucket := aws.StringValue(input.Bucket)
	if bucket != s.bucket {
		return nil, errors.New("bucket not found")
	}
	if data, ok := s.objects[aws.StringValue(input.Key)]; ok {
		body := io.NopCloser(strings.NewReader(data))
		return &s3.GetObjectOutput{Body: body}, nil
	}
	return nil, errors.New("object not found")
}
```

## File: `source/bitbucket/.gitignore`
```
.bitbucket_test_secrets
```

## File: `source/bitbucket/bitbucket.go`
```go
package bitbucket

import (
	"fmt"
	"io"
	nurl "net/url"
	"os"
	"path"
	"path/filepath"
	"strings"

	"github.com/golang-migrate/migrate/v4/source"
	"github.com/ktrysmt/go-bitbucket"
)

func init() {
	source.Register("bitbucket", &Bitbucket{})
}

var (
	ErrNoUserInfo             = fmt.Errorf("no username:password provided")
	ErrNoAccessToken          = fmt.Errorf("no password/app password")
	ErrInvalidRepo            = fmt.Errorf("invalid repo")
	ErrInvalidBitbucketClient = fmt.Errorf("expected *bitbucket.Client")
	ErrNoDir                  = fmt.Errorf("no directory")
)

type Bitbucket struct {
	config     *Config
	client     *bitbucket.Client
	migrations *source.Migrations
}

type Config struct {
	Owner string
	Repo  string
	Path  string
	Ref   string
}

func (b *Bitbucket) Open(url string) (source.Driver, error) {
	u, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}

	if u.User == nil {
		return nil, ErrNoUserInfo
	}

	password, ok := u.User.Password()
	if !ok {
		return nil, ErrNoAccessToken
	}

	cl := bitbucket.NewBasicAuth(u.User.Username(), password)

	cfg := &Config{}
	// set owner, repo and path in repo
	cfg.Owner = u.Host
	pe := strings.Split(strings.Trim(u.Path, "/"), "/")
	if len(pe) < 1 {
		return nil, ErrInvalidRepo
	}
	cfg.Repo = pe[0]
	if len(pe) > 1 {
		cfg.Path = strings.Join(pe[1:], "/")
	}
	cfg.Ref = u.Fragment

	bi, err := WithInstance(cl, cfg)
	if err != nil {
		return nil, err
	}

	return bi, nil
}

func WithInstance(client *bitbucket.Client, config *Config) (source.Driver, error) {
	bi := &Bitbucket{
		client:     client,
		config:     config,
		migrations: source.NewMigrations(),
	}

	if err := bi.readDirectory(); err != nil {
		return nil, err
	}

	return bi, nil
}

func (b *Bitbucket) readDirectory() error {
	b.ensureFields()

	fOpt := &bitbucket.RepositoryFilesOptions{
		Owner:    b.config.Owner,
		RepoSlug: b.config.Repo,
		Ref:      b.config.Ref,
		Path:     b.config.Path,
	}

	dirContents, err := b.client.Repositories.Repository.ListFiles(fOpt)

	if err != nil {
		return err
	}

	for _, fi := range dirContents {

		m, err := source.DefaultParse(filepath.Base(fi.Path))
		if err != nil {
			continue // ignore files that we can't parse
		}
		if !b.migrations.Append(m) {
			return fmt.Errorf("unable to parse file %v", fi.Path)
		}
	}

	return nil
}

func (b *Bitbucket) ensureFields() {
	if b.config == nil {
		b.config = &Config{}
	}
}

func (b *Bitbucket) Close() error {
	return nil
}

func (b *Bitbucket) First() (version uint, er error) {
	b.ensureFields()

	if v, ok := b.migrations.First(); !ok {
		return 0, &os.PathError{Op: "first", Path: b.config.Path, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (b *Bitbucket) Prev(version uint) (prevVersion uint, err error) {
	b.ensureFields()

	if v, ok := b.migrations.Prev(version); !ok {
		return 0, &os.PathError{Op: fmt.Sprintf("prev for version %v", version), Path: b.config.Path, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (b *Bitbucket) Next(version uint) (nextVersion uint, err error) {
	b.ensureFields()

	if v, ok := b.migrations.Next(version); !ok {
		return 0, &os.PathError{Op: fmt.Sprintf("next for version %v", version), Path: b.config.Path, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (b *Bitbucket) ReadUp(version uint) (r io.ReadCloser, identifier string, err error) {
	b.ensureFields()

	if m, ok := b.migrations.Up(version); ok {
		fBlobOpt := &bitbucket.RepositoryBlobOptions{
			Owner:    b.config.Owner,
			RepoSlug: b.config.Repo,
			Ref:      b.config.Ref,
			Path:     path.Join(b.config.Path, m.Raw),
		}
		file, err := b.client.Repositories.Repository.GetFileBlob(fBlobOpt)
		if err != nil {
			return nil, "", err
		}
		if file != nil {
			r := file.Content
			return io.NopCloser(strings.NewReader(string(r))), m.Identifier, nil
		}
	}
	return nil, "", &os.PathError{Op: fmt.Sprintf("read version %v", version), Path: b.config.Path, Err: os.ErrNotExist}
}

func (b *Bitbucket) ReadDown(version uint) (r io.ReadCloser, identifier string, err error) {
	b.ensureFields()

	if m, ok := b.migrations.Down(version); ok {
		fBlobOpt := &bitbucket.RepositoryBlobOptions{
			Owner:    b.config.Owner,
			RepoSlug: b.config.Repo,
			Ref:      b.config.Ref,
			Path:     path.Join(b.config.Path, m.Raw),
		}
		file, err := b.client.Repositories.Repository.GetFileBlob(fBlobOpt)

		if err != nil {
			return nil, "", err
		}
		if file != nil {
			r := file.Content

			return io.NopCloser(strings.NewReader(string(r))), m.Identifier, nil
		}
	}
	return nil, "", &os.PathError{Op: fmt.Sprintf("read version %v", version), Path: b.config.Path, Err: os.ErrNotExist}
}
```

## File: `source/bitbucket/bitbucket_test.go`
```go
package bitbucket

import (
	"bytes"
	"os"
	"testing"

	st "github.com/golang-migrate/migrate/v4/source/testing"
)

var BitbucketTestSecret = "" // username:password

func init() {
	secrets, err := os.ReadFile(".bitbucket_test_secrets")
	if err == nil {
		BitbucketTestSecret = string(bytes.TrimSpace(secrets)[:])
	}
}

func Test(t *testing.T) {
	if len(BitbucketTestSecret) == 0 {
		t.Skip("test requires .bitbucket_test_secrets")
	}

	b := &Bitbucket{}

	d, err := b.Open("bitbucket://" + BitbucketTestSecret + "@abhishekbipp/test-migration/migrations/test#master")
	if err != nil {
		t.Fatal(err)
	}

	st.Test(t, d)
}
```

## File: `source/bitbucket/README.md`
```markdown
# bitbucket

This driver is catered for those that want to source migrations from bitbucket cloud(https://bitbucket.com).

`bitbucket://user:password@owner/repo/path#ref`

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| user | | The username of the user connecting |
| password | | User's password or an app password with repo read permission  |
| owner | | the repo owner |
| repo | | the name of the repository |
| path | | path in repo to migrations |
| ref | | (optional) can be a SHA, branch, or tag |
```

## File: `source/file/file.go`
```go
package file

import (
	nurl "net/url"
	"os"
	"path/filepath"

	"github.com/golang-migrate/migrate/v4/source"
	"github.com/golang-migrate/migrate/v4/source/iofs"
)

func init() {
	source.Register("file", &File{})
}

type File struct {
	iofs.PartialDriver
	url  string
	path string
}

func (f *File) Open(url string) (source.Driver, error) {
	p, err := parseURL(url)
	if err != nil {
		return nil, err
	}
	nf := &File{
		url:  url,
		path: p,
	}
	if err := nf.Init(os.DirFS(p), "."); err != nil {
		return nil, err
	}
	return nf, nil
}

func parseURL(url string) (string, error) {
	u, err := nurl.Parse(url)
	if err != nil {
		return "", err
	}
	// concat host and path to restore full path
	// host might be `.`
	p := u.Opaque
	if len(p) == 0 {
		p = u.Host + u.Path
	}

	if len(p) == 0 {
		// default to current directory if no path
		wd, err := os.Getwd()
		if err != nil {
			return "", err
		}
		p = wd

	} else if p[0:1] == "." || p[0:1] != "/" {
		// make path absolute if relative
		abs, err := filepath.Abs(p)
		if err != nil {
			return "", err
		}
		p = abs
	}
	return p, nil
}
```

## File: `source/file/file_test.go`
```go
package file

import (
	"errors"
	"fmt"
	"os"
	"path"
	"path/filepath"
	"testing"

	st "github.com/golang-migrate/migrate/v4/source/testing"
)

const scheme = "file://"

func Test(t *testing.T) {
	tmpDir := t.TempDir()

	// write files that meet driver test requirements
	mustWriteFile(t, tmpDir, "1_foobar.up.sql", "1 up")
	mustWriteFile(t, tmpDir, "1_foobar.down.sql", "1 down")

	mustWriteFile(t, tmpDir, "3_foobar.up.sql", "3 up")

	mustWriteFile(t, tmpDir, "4_foobar.up.sql", "4 up")
	mustWriteFile(t, tmpDir, "4_foobar.down.sql", "4 down")

	mustWriteFile(t, tmpDir, "5_foobar.down.sql", "5 down")

	mustWriteFile(t, tmpDir, "7_foobar.up.sql", "7 up")
	mustWriteFile(t, tmpDir, "7_foobar.down.sql", "7 down")

	f := &File{}
	d, err := f.Open(scheme + tmpDir)
	if err != nil {
		t.Fatal(err)
	}

	st.Test(t, d)
}

func TestOpen(t *testing.T) {
	tmpDir := t.TempDir()

	mustWriteFile(t, tmpDir, "1_foobar.up.sql", "")
	mustWriteFile(t, tmpDir, "1_foobar.down.sql", "")

	if !filepath.IsAbs(tmpDir) {
		t.Fatal("expected tmpDir to be absolute path")
	}

	f := &File{}
	_, err := f.Open(scheme + tmpDir) // absolute path
	if err != nil {
		t.Fatal(err)
	}
}

func TestOpenWithRelativePath(t *testing.T) {
	tmpDir := t.TempDir()

	wd, err := os.Getwd()
	if err != nil {
		t.Fatal(err)
	}
	defer func() {
		// rescue working dir after we are done
		if err := os.Chdir(wd); err != nil {
			t.Log(err)
		}
	}()

	if err := os.Chdir(tmpDir); err != nil {
		t.Fatal(err)
	}

	if err := os.Mkdir(filepath.Join(tmpDir, "foo"), os.ModePerm); err != nil {
		t.Fatal(err)
	}

	mustWriteFile(t, filepath.Join(tmpDir, "foo"), "1_foobar.up.sql", "")

	f := &File{}

	// dir: foo
	d, err := f.Open("file://foo")
	if err != nil {
		t.Fatal(err)
	}
	_, err = d.First()
	if err != nil {
		t.Fatalf("expected first file in working dir %v for foo", tmpDir)
	}

	// dir: ./foo
	d, err = f.Open("file://./foo")
	if err != nil {
		t.Fatal(err)
	}
	_, err = d.First()
	if err != nil {
		t.Fatalf("expected first file in working dir %v for ./foo", tmpDir)
	}
}

func TestOpenDefaultsToCurrentDirectory(t *testing.T) {
	wd, err := os.Getwd()
	if err != nil {
		t.Fatal(err)
	}

	f := &File{}
	d, err := f.Open(scheme)
	if err != nil {
		t.Fatal(err)
	}

	if d.(*File).path != wd {
		t.Fatal("expected driver to default to current directory")
	}
}

func TestOpenWithDuplicateVersion(t *testing.T) {
	tmpDir := t.TempDir()

	mustWriteFile(t, tmpDir, "1_foo.up.sql", "") // 1 up
	mustWriteFile(t, tmpDir, "1_bar.up.sql", "") // 1 up

	f := &File{}
	_, err := f.Open(scheme + tmpDir)
	if err == nil {
		t.Fatal("expected err")
	}
}

func TestClose(t *testing.T) {
	tmpDir := t.TempDir()

	f := &File{}
	d, err := f.Open(scheme + tmpDir)
	if err != nil {
		t.Fatal(err)
	}

	if d.Close() != nil {
		t.Fatal("expected nil")
	}
}

func mustWriteFile(t testing.TB, dir, file string, body string) {
	if err := os.WriteFile(path.Join(dir, file), []byte(body), 06444); err != nil {
		t.Fatal(err)
	}
}

func mustCreateBenchmarkDir(t *testing.B) (dir string) {
	tmpDir := t.TempDir()

	for i := 0; i < 1000; i++ {
		mustWriteFile(t, tmpDir, fmt.Sprintf("%v_foobar.up.sql", i), "")
		mustWriteFile(t, tmpDir, fmt.Sprintf("%v_foobar.down.sql", i), "")
	}

	return tmpDir
}

func BenchmarkOpen(b *testing.B) {
	dir := mustCreateBenchmarkDir(b)
	defer func() {
		if err := os.RemoveAll(dir); err != nil {
			b.Error(err)
		}
	}()
	b.ResetTimer()
	for n := 0; n < b.N; n++ {
		f := &File{}
		_, err := f.Open(scheme + dir)
		if err != nil {
			b.Error(err)
		}
	}
	b.StopTimer()
}

func BenchmarkNext(b *testing.B) {
	dir := mustCreateBenchmarkDir(b)
	defer func() {
		if err := os.RemoveAll(dir); err != nil {
			b.Error(err)
		}
	}()
	f := &File{}
	d, _ := f.Open(scheme + dir)
	b.ResetTimer()
	v, err := d.First()
	for n := 0; n < b.N; n++ {
		for !errors.Is(err, os.ErrNotExist) {
			v, err = d.Next(v)
		}
	}
	b.StopTimer()
}
```

## File: `source/file/README.md`
```markdown
# file

`file:///absolute/path`  
`file://relative/path`
```

## File: `source/github/.gitignore`
```
.github_test_secrets
```

## File: `source/github/github.go`
```go
package github

import (
	"context"
	"fmt"
	"io"
	"net/http"
	nurl "net/url"
	"os"
	"path"
	"strings"

	"golang.org/x/oauth2"

	"github.com/golang-migrate/migrate/v4/source"
	"github.com/google/go-github/v39/github"
)

func init() {
	source.Register("github", &Github{})
}

var (
	ErrNoUserInfo          = fmt.Errorf("no username:token provided")
	ErrNoAccessToken       = fmt.Errorf("no access token")
	ErrInvalidRepo         = fmt.Errorf("invalid repo")
	ErrInvalidGithubClient = fmt.Errorf("expected *github.Client")
	ErrNoDir               = fmt.Errorf("no directory")
)

type Github struct {
	config     *Config
	client     *github.Client
	options    *github.RepositoryContentGetOptions
	migrations *source.Migrations
}

type Config struct {
	Owner string
	Repo  string
	Path  string
	Ref   string
}

func (g *Github) Open(url string) (source.Driver, error) {
	u, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}

	// client defaults to http.DefaultClient
	var client *http.Client
	if u.User != nil {
		password, ok := u.User.Password()
		if !ok {
			return nil, ErrNoUserInfo
		}
		ts := oauth2.StaticTokenSource(
			&oauth2.Token{AccessToken: password},
		)
		client = oauth2.NewClient(context.Background(), ts)

	}

	gn := &Github{
		client:     github.NewClient(client),
		migrations: source.NewMigrations(),
		options:    &github.RepositoryContentGetOptions{Ref: u.Fragment},
	}

	gn.ensureFields()

	// set owner, repo and path in repo
	gn.config.Owner = u.Host
	pe := strings.Split(strings.Trim(u.Path, "/"), "/")
	if len(pe) < 1 {
		return nil, ErrInvalidRepo
	}
	gn.config.Repo = pe[0]
	if len(pe) > 1 {
		gn.config.Path = strings.Join(pe[1:], "/")
	}

	if err := gn.readDirectory(); err != nil {
		return nil, err
	}

	return gn, nil
}

func WithInstance(client *github.Client, config *Config) (source.Driver, error) {
	gn := &Github{
		client:     client,
		config:     config,
		migrations: source.NewMigrations(),
		options:    &github.RepositoryContentGetOptions{Ref: config.Ref},
	}

	if err := gn.readDirectory(); err != nil {
		return nil, err
	}

	return gn, nil
}

func (g *Github) readDirectory() error {
	g.ensureFields()

	fileContent, dirContents, _, err := g.client.Repositories.GetContents(
		context.Background(),
		g.config.Owner,
		g.config.Repo,
		g.config.Path,
		g.options,
	)

	if err != nil {
		return err
	}
	if fileContent != nil {
		return ErrNoDir
	}

	for _, fi := range dirContents {
		m, err := source.DefaultParse(*fi.Name)
		if err != nil {
			continue // ignore files that we can't parse
		}
		if !g.migrations.Append(m) {
			return fmt.Errorf("unable to parse file %v", *fi.Name)
		}
	}

	return nil
}

func (g *Github) ensureFields() {
	if g.config == nil {
		g.config = &Config{}
	}
}

func (g *Github) Close() error {
	return nil
}

func (g *Github) First() (version uint, err error) {
	g.ensureFields()

	if v, ok := g.migrations.First(); !ok {
		return 0, &os.PathError{Op: "first", Path: g.config.Path, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (g *Github) Prev(version uint) (prevVersion uint, err error) {
	g.ensureFields()

	if v, ok := g.migrations.Prev(version); !ok {
		return 0, &os.PathError{Op: fmt.Sprintf("prev for version %v", version), Path: g.config.Path, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (g *Github) Next(version uint) (nextVersion uint, err error) {
	g.ensureFields()

	if v, ok := g.migrations.Next(version); !ok {
		return 0, &os.PathError{Op: fmt.Sprintf("next for version %v", version), Path: g.config.Path, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (g *Github) ReadUp(version uint) (r io.ReadCloser, identifier string, err error) {
	g.ensureFields()

	if m, ok := g.migrations.Up(version); ok {
		r, _, err := g.client.Repositories.DownloadContents(
			context.Background(),
			g.config.Owner,
			g.config.Repo,
			path.Join(g.config.Path, m.Raw),
			g.options,
		)

		if err != nil {
			return nil, "", err
		}
		return r, m.Identifier, nil
	}
	return nil, "", &os.PathError{Op: fmt.Sprintf("read version %v", version), Path: g.config.Path, Err: os.ErrNotExist}
}

func (g *Github) ReadDown(version uint) (r io.ReadCloser, identifier string, err error) {
	g.ensureFields()

	if m, ok := g.migrations.Down(version); ok {
		r, _, err := g.client.Repositories.DownloadContents(
			context.Background(),
			g.config.Owner,
			g.config.Repo,
			path.Join(g.config.Path, m.Raw),
			g.options,
		)

		if err != nil {
			return nil, "", err
		}
		return r, m.Identifier, nil
	}
	return nil, "", &os.PathError{Op: fmt.Sprintf("read version %v", version), Path: g.config.Path, Err: os.ErrNotExist}
}
```

## File: `source/github/github_test.go`
```go
package github

import (
	"bytes"
	"fmt"
	"os"
	"testing"

	st "github.com/golang-migrate/migrate/v4/source/testing"
	"github.com/stretchr/testify/assert"
)

var GithubTestSecret = "" // username:token

func init() {
	secrets, err := os.ReadFile(".github_test_secrets")
	if err == nil {
		GithubTestSecret = string(bytes.TrimSpace(secrets)[:])
	}
}

func Test(t *testing.T) {
	if len(GithubTestSecret) == 0 {
		t.Skip("test requires .github_test_secrets")
	}

	g := &Github{}
	d, err := g.Open("github://" + GithubTestSecret + "@mattes/migrate_test_tmp/test#452b8003e7")
	if err != nil {
		t.Fatal(err)
	}

	st.Test(t, d)
}

func TestDefaultClient(t *testing.T) {
	g := &Github{}
	owner := "golang-migrate"
	repo := "migrate"
	path := "source/github/examples/migrations"

	url := fmt.Sprintf("github://%s/%s/%s", owner, repo, path)
	d, err := g.Open(url)
	if err != nil {
		t.Fatal(err)
	}

	ver, err := d.First()
	if err != nil {
		t.Fatal(err)
	}
	assert.Equal(t, uint(1085649617), ver)

	ver, err = d.Next(ver)
	if err != nil {
		t.Fatal(err)
	}
	assert.Equal(t, uint(1185749658), ver)
}
```

## File: `source/github/README.md`
```markdown
# github



This driver is catered for those that want to source migrations from [github.com](https://github.com). The URL scheme doesn't require a hostname, as it just simply defaults to `github.com`.



Authenticated client: `github://user:personal-access-token@owner/repo/path#ref`



Unauthenticated client: `github://owner/repo/path#ref`



| URL Query  | WithInstance Config | Description |

|------------|---------------------|-------------|

| user | | (optional) The username of the user connecting |

| personal-access-token | | (optional) An access token from GitHub (https://github.com/settings/tokens) |

| owner | | the repo owner |

| repo | | the name of the repository |

| path | | path in repo to migrations |

| ref | | (optional) can be a SHA, branch, or tag |

```

## File: `source/github/examples/migrations/1085649617_create_users_table.down.sql`
```sql
DROP TABLE IF EXISTS users;
```

## File: `source/github/examples/migrations/1085649617_create_users_table.up.sql`
```sql
CREATE TABLE users (
  user_id integer unique,
  name    varchar(40),
  email   varchar(40)
);
```

## File: `source/github/examples/migrations/1185749658_add_city_to_users.down.sql`
```sql
ALTER TABLE users DROP COLUMN IF EXISTS city;
```

## File: `source/github/examples/migrations/1185749658_add_city_to_users.up.sql`
```sql
ALTER TABLE users ADD COLUMN city varchar(100);


```

## File: `source/github/examples/migrations/1285849751_add_index_on_user_emails.down.sql`
```sql
DROP INDEX IF EXISTS users_email_index;
```

## File: `source/github/examples/migrations/1285849751_add_index_on_user_emails.up.sql`
```sql
CREATE UNIQUE INDEX CONCURRENTLY users_email_index ON users (email);

-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `source/github/examples/migrations/1385949617_create_books_table.down.sql`
```sql
DROP TABLE IF EXISTS books;
```

## File: `source/github/examples/migrations/1385949617_create_books_table.up.sql`
```sql
CREATE TABLE books (
  user_id integer,
  name    varchar(40),
  author  varchar(40)
);
```

## File: `source/github/examples/migrations/1485949617_create_movies_table.down.sql`
```sql
DROP TABLE IF EXISTS movies;
```

## File: `source/github/examples/migrations/1485949617_create_movies_table.up.sql`
```sql
CREATE TABLE movies (
  user_id   integer,
  name      varchar(40),
  director  varchar(40)
);
```

## File: `source/github/examples/migrations/1585849751_just_a_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `source/github/examples/migrations/1685849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `source/github/examples/migrations/1785849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `source/github/examples/migrations/1885849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `source/github_ee/.gitignore`
```
.github_test_secrets
```

## File: `source/github_ee/github_ee.go`
```go
package github_ee

import (
	"crypto/tls"
	"fmt"
	"net/http"
	nurl "net/url"
	"strconv"
	"strings"

	"github.com/golang-migrate/migrate/v4/source"
	gh "github.com/golang-migrate/migrate/v4/source/github"

	"github.com/google/go-github/v39/github"
)

func init() {
	source.Register("github-ee", &GithubEE{})
}

type GithubEE struct {
	source.Driver
}

func (g *GithubEE) Open(url string) (source.Driver, error) {
	verifyTLS := true

	u, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}

	if o := u.Query().Get("verify-tls"); o != "" {
		verifyTLS = parseBool(o, verifyTLS)
	}

	if u.User == nil {
		return nil, gh.ErrNoUserInfo
	}

	password, ok := u.User.Password()
	if !ok {
		return nil, gh.ErrNoUserInfo
	}

	ghc, err := g.createGithubClient(u.Host, u.User.Username(), password, verifyTLS)
	if err != nil {
		return nil, err
	}

	pe := strings.Split(strings.Trim(u.Path, "/"), "/")

	if len(pe) < 1 {
		return nil, gh.ErrInvalidRepo
	}

	cfg := &gh.Config{
		Owner: pe[0],
		Repo:  pe[1],
		Ref:   u.Fragment,
	}

	if len(pe) > 2 {
		cfg.Path = strings.Join(pe[2:], "/")
	}

	i, err := gh.WithInstance(ghc, cfg)
	if err != nil {
		return nil, err
	}

	return &GithubEE{Driver: i}, nil
}

func (g *GithubEE) createGithubClient(host, username, password string, verifyTLS bool) (*github.Client, error) {
	tr := &github.BasicAuthTransport{
		Username: username,
		Password: password,
		Transport: &http.Transport{
			TLSClientConfig: &tls.Config{InsecureSkipVerify: !verifyTLS},
		},
	}

	apiHost := fmt.Sprintf("https://%s/api/v3", host)
	uploadHost := fmt.Sprintf("https://uploads.%s", host)

	return github.NewEnterpriseClient(apiHost, uploadHost, tr.Client())
}

func parseBool(val string, fallback bool) bool {
	b, err := strconv.ParseBool(val)
	if err != nil {
		return fallback
	}

	return b
}
```

## File: `source/github_ee/github_ee_test.go`
```go
package github_ee

import (
	"net/http"
	"net/http/httptest"
	nurl "net/url"
	"testing"
)

func Test(t *testing.T) {
	ts := httptest.NewTLSServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path != "/api/v3/repos/mattes/migrate_test_tmp/contents/test" {
			w.WriteHeader(http.StatusNotFound)
			return
		}

		if ref := r.URL.Query().Get("ref"); ref != "452b8003e7" {
			w.WriteHeader(http.StatusNotFound)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)

		_, err := w.Write([]byte("[]"))
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			return
		}
	}))
	defer ts.Close()

	u, err := nurl.Parse(ts.URL)
	if err != nil {
		t.Fatal(err)
	}

	g := &GithubEE{}
	_, err = g.Open("github-ee://foo:bar@" + u.Host + "/mattes/migrate_test_tmp/test?verify-tls=false#452b8003e7")

	if err != nil {
		t.Fatal(err)
	}
}
```

## File: `source/github_ee/README.md`
```markdown
# github ee

## GitHub Enterprise Edition

This driver is catered for those who run GitHub Enterprise under private infrastructure.

The below URL scheme illustrates how to source migration files from GitHub Enterprise.

GitHub client for Go requires API and Uploads endpoint hosts in order to create an instance of GitHub Enterprise Client. We're making an assumption that the API and Uploads are available under `https://api.*` and `https://uploads.*` respectively. [GitHub Enterprise Installation Guide](https://help.github.com/en/enterprise/2.15/admin/installation/enabling-subdomain-isolation) recommends that you enable Subdomain isolation feature.

`github-ee://user:personal-access-token@host/owner/repo/path?verify-tls=true#ref`

| URL Query  | WithInstance Config | Description |
|------------|---------------------|-------------|
| user | | The username of the user connecting |
| personal-access-token | | Personal access token from your GitHub Enterprise instance |
| owner | | the repo owner |
| repo | | the name of the repository |
| path | | path in repo to migrations |
| ref | | (optional) can be a SHA, branch, or tag |
| verify-tls | | (optional) defaults to `true`. This option sets `tls.Config.InsecureSkipVerify` accordingly |
```

## File: `source/gitlab/.gitignore`
```
.gitlab_test_secrets
```

## File: `source/gitlab/gitlab.go`
```go
package gitlab

import (
	"encoding/base64"
	"fmt"
	"io"
	"net/http"
	nurl "net/url"
	"os"
	"strconv"
	"strings"

	"github.com/golang-migrate/migrate/v4/source"
	"github.com/xanzy/go-gitlab"
)

func init() {
	source.Register("gitlab", &Gitlab{})
}

const DefaultMaxItemsPerPage = 100

var (
	ErrNoUserInfo       = fmt.Errorf("no username:token provided")
	ErrNoAccessToken    = fmt.Errorf("no access token")
	ErrInvalidHost      = fmt.Errorf("invalid host")
	ErrInvalidProjectID = fmt.Errorf("invalid project id")
	ErrInvalidResponse  = fmt.Errorf("invalid response")
)

type Gitlab struct {
	client *gitlab.Client
	url    string

	projectID   string
	path        string
	listOptions *gitlab.ListTreeOptions
	getOptions  *gitlab.GetFileOptions
	migrations  *source.Migrations
}

type Config struct {
}

func (g *Gitlab) Open(url string) (source.Driver, error) {
	u, err := nurl.Parse(url)
	if err != nil {
		return nil, err
	}

	if u.User == nil {
		return nil, ErrNoUserInfo
	}

	password, ok := u.User.Password()
	if !ok {
		return nil, ErrNoAccessToken
	}

	gn := &Gitlab{
		client:     gitlab.NewClient(nil, password),
		url:        url,
		migrations: source.NewMigrations(),
	}

	if u.Host != "" {
		uri := nurl.URL{
			Scheme: "https",
			Host:   u.Host,
		}

		err = gn.client.SetBaseURL(uri.String())
		if err != nil {
			return nil, ErrInvalidHost
		}
	}

	pe := strings.Split(strings.Trim(u.Path, "/"), "/")
	if len(pe) < 1 {
		return nil, ErrInvalidProjectID
	}
	gn.projectID = pe[0]
	if len(pe) > 1 {
		gn.path = strings.Join(pe[1:], "/")
	}

	gn.listOptions = &gitlab.ListTreeOptions{
		Path: &gn.path,
		Ref:  &u.Fragment,
		ListOptions: gitlab.ListOptions{
			PerPage: DefaultMaxItemsPerPage,
		},
	}

	gn.getOptions = &gitlab.GetFileOptions{
		Ref: &u.Fragment,
	}

	if err := gn.readDirectory(); err != nil {
		return nil, err
	}

	return gn, nil
}

func WithInstance(client *gitlab.Client, config *Config) (source.Driver, error) {
	gn := &Gitlab{
		client:     client,
		migrations: source.NewMigrations(),
	}
	if err := gn.readDirectory(); err != nil {
		return nil, err
	}
	return gn, nil
}

func (g *Gitlab) readDirectory() error {
	var nodes []*gitlab.TreeNode
	for {
		n, response, err := g.client.Repositories.ListTree(g.projectID, g.listOptions)
		if err != nil {
			return err
		}

		if response.StatusCode != http.StatusOK {
			return ErrInvalidResponse
		}

		nodes = append(nodes, n...)
		if response.CurrentPage >= response.TotalPages {
			break
		}
		g.listOptions.Page = response.NextPage
	}

	for i := range nodes {
		m, err := g.nodeToMigration(nodes[i])
		if err != nil {
			continue
		}

		if !g.migrations.Append(m) {
			return fmt.Errorf("unable to parse file %v", nodes[i].Name)
		}
	}

	return nil
}

func (g *Gitlab) nodeToMigration(node *gitlab.TreeNode) (*source.Migration, error) {
	m := source.Regex.FindStringSubmatch(node.Name)
	if len(m) == 5 {
		versionUint64, err := strconv.ParseUint(m[1], 10, 64)
		if err != nil {
			return nil, err
		}
		return &source.Migration{
			Version:    uint(versionUint64),
			Identifier: m[2],
			Direction:  source.Direction(m[3]),
			Raw:        g.path + "/" + node.Name,
		}, nil
	}
	return nil, source.ErrParse
}

func (g *Gitlab) Close() error {
	return nil
}

func (g *Gitlab) First() (version uint, er error) {
	if v, ok := g.migrations.First(); !ok {
		return 0, &os.PathError{Op: "first", Path: g.path, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (g *Gitlab) Prev(version uint) (prevVersion uint, err error) {
	if v, ok := g.migrations.Prev(version); !ok {
		return 0, &os.PathError{Op: fmt.Sprintf("prev for version %v", version), Path: g.path, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (g *Gitlab) Next(version uint) (nextVersion uint, err error) {
	if v, ok := g.migrations.Next(version); !ok {
		return 0, &os.PathError{Op: fmt.Sprintf("next for version %v", version), Path: g.path, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (g *Gitlab) ReadUp(version uint) (r io.ReadCloser, identifier string, err error) {
	if m, ok := g.migrations.Up(version); ok {
		f, response, err := g.client.RepositoryFiles.GetFile(g.projectID, m.Raw, g.getOptions)
		if err != nil {
			return nil, "", err
		}

		if response.StatusCode != http.StatusOK {
			return nil, "", ErrInvalidResponse
		}

		content, err := base64.StdEncoding.DecodeString(f.Content)
		if err != nil {
			return nil, "", err
		}

		return io.NopCloser(strings.NewReader(string(content))), m.Identifier, nil
	}

	return nil, "", &os.PathError{Op: fmt.Sprintf("read version %v", version), Path: g.path, Err: os.ErrNotExist}
}

func (g *Gitlab) ReadDown(version uint) (r io.ReadCloser, identifier string, err error) {
	if m, ok := g.migrations.Down(version); ok {
		f, response, err := g.client.RepositoryFiles.GetFile(g.projectID, m.Raw, g.getOptions)
		if err != nil {
			return nil, "", err
		}

		if response.StatusCode != http.StatusOK {
			return nil, "", ErrInvalidResponse
		}

		content, err := base64.StdEncoding.DecodeString(f.Content)
		if err != nil {
			return nil, "", err
		}

		return io.NopCloser(strings.NewReader(string(content))), m.Identifier, nil
	}

	return nil, "", &os.PathError{Op: fmt.Sprintf("read version %v", version), Path: g.path, Err: os.ErrNotExist}
}
```

## File: `source/gitlab/gitlab_test.go`
```go
package gitlab

import (
	"bytes"
	"os"
	"testing"

	st "github.com/golang-migrate/migrate/v4/source/testing"
)

var GitlabTestSecret = "" // username:token

func init() {
	secrets, err := os.ReadFile(".gitlab_test_secrets")
	if err == nil {
		GitlabTestSecret = string(bytes.TrimSpace(secrets)[:])
	}
}

func Test(t *testing.T) {
	if len(GitlabTestSecret) == 0 {
		t.Skip("test requires .gitlab_test_secrets")
	}

	g := &Gitlab{}
	d, err := g.Open("gitlab://" + GitlabTestSecret + "@gitlab.com/11197284/migrations")
	if err != nil {
		t.Fatal(err)
	}

	st.Test(t, d)
}
```

## File: `source/gitlab/README.md`
```markdown
# gitlab



`gitlab://user:personal-access-token@gitlab_url/project_id/path#ref`



| URL Query  | WithInstance Config | Description |

|------------|---------------------|-------------|

| user | | The username of the user connecting |

| personal-access-token | | An access token from Gitlab (https://<gitlab_url>/profile/personal_access_tokens) |

| gitlab_url | | url of the gitlab server |

| project_id | | id of the repository |

| path | | path in repo to migrations |

| ref | | (optional) can be a SHA, branch, or tag |

```

## File: `source/gitlab/examples/migrations/1085649617_create_users_table.down.sql`
```sql
DROP TABLE IF EXISTS users;
```

## File: `source/gitlab/examples/migrations/1085649617_create_users_table.up.sql`
```sql
CREATE TABLE users (
  user_id integer unique,
  name    varchar(40),
  email   varchar(40)
);
```

## File: `source/gitlab/examples/migrations/1185749658_add_city_to_users.down.sql`
```sql
ALTER TABLE users DROP COLUMN IF EXISTS city;
```

## File: `source/gitlab/examples/migrations/1185749658_add_city_to_users.up.sql`
```sql
ALTER TABLE users ADD COLUMN city varchar(100);


```

## File: `source/gitlab/examples/migrations/1285849751_add_index_on_user_emails.down.sql`
```sql
DROP INDEX IF EXISTS users_email_index;
```

## File: `source/gitlab/examples/migrations/1285849751_add_index_on_user_emails.up.sql`
```sql
CREATE UNIQUE INDEX CONCURRENTLY users_email_index ON users (email);

-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `source/gitlab/examples/migrations/1385949617_create_books_table.down.sql`
```sql
DROP TABLE IF EXISTS books;
```

## File: `source/gitlab/examples/migrations/1385949617_create_books_table.up.sql`
```sql
CREATE TABLE books (
  user_id integer,
  name    varchar(40),
  author  varchar(40)
);
```

## File: `source/gitlab/examples/migrations/1485949617_create_movies_table.down.sql`
```sql
DROP TABLE IF EXISTS movies;
```

## File: `source/gitlab/examples/migrations/1485949617_create_movies_table.up.sql`
```sql
CREATE TABLE movies (
  user_id   integer,
  name      varchar(40),
  director  varchar(40)
);
```

## File: `source/gitlab/examples/migrations/1585849751_just_a_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `source/gitlab/examples/migrations/1685849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `source/gitlab/examples/migrations/1785849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `source/gitlab/examples/migrations/1885849751_another_comment.up.sql`
```sql
-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sed interdum velit, tristique iaculis justo. Pellentesque ut porttitor dolor. Donec sit amet pharetra elit. Cras vel ligula ex. Phasellus posuere.
```

## File: `source/godoc_vfs/vfs.go`
```go
// Package godoc_vfs contains a driver that reads migrations from a virtual file
// system.
//
// Implementations of the filesystem interface that read from zip files and
// maps, as well as the definition of the filesystem interface can be found in
// the golang.org/x/tools/godoc/vfs package.
package godoc_vfs

import (
	"github.com/golang-migrate/migrate/v4/source"
	"github.com/golang-migrate/migrate/v4/source/httpfs"

	"golang.org/x/tools/godoc/vfs"
	vfs_httpfs "golang.org/x/tools/godoc/vfs/httpfs"
)

func init() {
	source.Register("godoc-vfs", &VFS{})
}

// VFS is an implementation of driver that returns migrations from a virtual
// file system.
type VFS struct {
	httpfs.PartialDriver
	fs   vfs.FileSystem
	path string
}

// Open implements the source.Driver interface for VFS.
//
// Calling this function panics, instead use the WithInstance function.
// See the package level documentation for an example.
func (b *VFS) Open(url string) (source.Driver, error) {
	panic("not implemented")
}

// WithInstance creates a new driver from a virtual file system.
// If a tree named searchPath exists in the virtual filesystem, WithInstance
// searches for migration files there.
// It defaults to "/".
func WithInstance(fs vfs.FileSystem, searchPath string) (source.Driver, error) {
	if searchPath == "" {
		searchPath = "/"
	}

	bn := &VFS{
		fs:   fs,
		path: searchPath,
	}

	if err := bn.Init(vfs_httpfs.New(fs), searchPath); err != nil {
		return nil, err
	}

	return bn, nil
}
```

## File: `source/godoc_vfs/vfs_example_test.go`
```go
package godoc_vfs_test

import (
	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/source/godoc_vfs"
	"golang.org/x/tools/godoc/vfs/mapfs"
)

func Example_mapfs() {
	fs := mapfs.New(map[string]string{
		"1_foobar.up.sql":   "1 up",
		"1_foobar.down.sql": "1 down",
		"3_foobar.up.sql":   "3 up",
		"4_foobar.up.sql":   "4 up",
		"4_foobar.down.sql": "4 down",
		"5_foobar.down.sql": "5 down",
		"7_foobar.up.sql":   "7 up",
		"7_foobar.down.sql": "7 down",
	})

	d, err := godoc_vfs.WithInstance(fs, "")
	if err != nil {
		panic("bad migrations found!")
	}
	m, err := migrate.NewWithSourceInstance("godoc-vfs", d, "database://foobar")
	if err != nil {
		panic("error creating the migrations")
	}
	err = m.Up()
	if err != nil {
		panic("up failed")
	}
}
```

## File: `source/godoc_vfs/vfs_test.go`
```go
package godoc_vfs_test

import (
	"testing"

	"github.com/golang-migrate/migrate/v4/source/godoc_vfs"
	st "github.com/golang-migrate/migrate/v4/source/testing"
	"golang.org/x/tools/godoc/vfs/mapfs"
)

func TestVFS(t *testing.T) {
	fs := mapfs.New(map[string]string{
		"1_foobar.up.sql":   "1 up",
		"1_foobar.down.sql": "1 down",
		"3_foobar.up.sql":   "3 up",
		"4_foobar.up.sql":   "4 up",
		"4_foobar.down.sql": "4 down",
		"5_foobar.down.sql": "5 down",
		"7_foobar.up.sql":   "7 up",
		"7_foobar.down.sql": "7 down",
	})

	d, err := godoc_vfs.WithInstance(fs, "")
	if err != nil {
		t.Fatal(err)
	}
	st.Test(t, d)
}

func TestOpen(t *testing.T) {
	defer func() {
		if r := recover(); r == nil {
			t.Error("Expected Open to panic")
		}
	}()
	b := &godoc_vfs.VFS{}
	if _, err := b.Open(""); err != nil {
		t.Error(err)
	}
}
```

## File: `source/google_cloud_storage/README.md`
```markdown
# Google Cloud Storage


## Import

```go
import (
  _ "github.com/golang-migrate/migrate/v4/source/google_cloud_storage"
 )
 ```

## Connection String

`gcs://<bucket>/<prefix>`
```

## File: `source/google_cloud_storage/storage.go`
```go
package googlecloudstorage

import (
	"fmt"
	"io"
	"net/url"
	"os"
	"path"
	"strings"

	"cloud.google.com/go/storage"
	"context"
	"github.com/golang-migrate/migrate/v4/source"
	"google.golang.org/api/iterator"
)

func init() {
	source.Register("gcs", &gcs{})
}

type gcs struct {
	bucket     *storage.BucketHandle
	prefix     string
	migrations *source.Migrations
}

func (g *gcs) Open(folder string) (source.Driver, error) {
	u, err := url.Parse(folder)
	if err != nil {
		return nil, err
	}
	client, err := storage.NewClient(context.Background())
	if err != nil {
		return nil, err
	}
	driver := gcs{
		bucket:     client.Bucket(u.Host),
		prefix:     strings.Trim(u.Path, "/") + "/",
		migrations: source.NewMigrations(),
	}
	err = driver.loadMigrations()
	if err != nil {
		return nil, err
	}
	return &driver, nil
}

func (g *gcs) loadMigrations() error {
	iter := g.bucket.Objects(context.Background(), &storage.Query{
		Prefix:    g.prefix,
		Delimiter: "/",
	})
	object, err := iter.Next()
	for ; err == nil; object, err = iter.Next() {
		_, fileName := path.Split(object.Name)
		m, parseErr := source.DefaultParse(fileName)
		if parseErr != nil {
			continue
		}
		if !g.migrations.Append(m) {
			return fmt.Errorf("unable to parse file %v", object.Name)
		}
	}
	if err != iterator.Done {
		return err
	}
	return nil
}

func (g *gcs) Close() error {
	return nil
}

func (g *gcs) First() (uint, error) {
	v, ok := g.migrations.First()
	if !ok {
		return 0, os.ErrNotExist
	}
	return v, nil
}

func (g *gcs) Prev(version uint) (uint, error) {
	v, ok := g.migrations.Prev(version)
	if !ok {
		return 0, os.ErrNotExist
	}
	return v, nil
}

func (g *gcs) Next(version uint) (uint, error) {
	v, ok := g.migrations.Next(version)
	if !ok {
		return 0, os.ErrNotExist
	}
	return v, nil
}

func (g *gcs) ReadUp(version uint) (io.ReadCloser, string, error) {
	if m, ok := g.migrations.Up(version); ok {
		return g.open(m)
	}
	return nil, "", os.ErrNotExist
}

func (g *gcs) ReadDown(version uint) (io.ReadCloser, string, error) {
	if m, ok := g.migrations.Down(version); ok {
		return g.open(m)
	}
	return nil, "", os.ErrNotExist
}

func (g *gcs) open(m *source.Migration) (io.ReadCloser, string, error) {
	objectPath := path.Join(g.prefix, m.Raw)
	reader, err := g.bucket.Object(objectPath).NewReader(context.Background())
	if err != nil {
		return nil, "", err
	}
	return reader, m.Identifier, nil
}
```

## File: `source/google_cloud_storage/storage_test.go`
```go
package googlecloudstorage

import (
	"testing"

	"github.com/fsouza/fake-gcs-server/fakestorage"
	"github.com/golang-migrate/migrate/v4/source"
	st "github.com/golang-migrate/migrate/v4/source/testing"
)

func Test(t *testing.T) {
	server := fakestorage.NewServer([]fakestorage.Object{
		{BucketName: "some-bucket", Name: "staging/migrations/1_foobar.up.sql", Content: []byte("1 up")},
		{BucketName: "some-bucket", Name: "staging/migrations/1_foobar.down.sql", Content: []byte("1 down")},
		{BucketName: "some-bucket", Name: "prod/migrations/1_foobar.up.sql", Content: []byte("1 up")},
		{BucketName: "some-bucket", Name: "prod/migrations/1_foobar.down.sql", Content: []byte("1 down")},
		{BucketName: "some-bucket", Name: "prod/migrations/3_foobar.up.sql", Content: []byte("3 up")},
		{BucketName: "some-bucket", Name: "prod/migrations/4_foobar.up.sql", Content: []byte("4 up")},
		{BucketName: "some-bucket", Name: "prod/migrations/4_foobar.down.sql", Content: []byte("4 down")},
		{BucketName: "some-bucket", Name: "prod/migrations/5_foobar.down.sql", Content: []byte("5 down")},
		{BucketName: "some-bucket", Name: "prod/migrations/7_foobar.up.sql", Content: []byte("7 up")},
		{BucketName: "some-bucket", Name: "prod/migrations/7_foobar.down.sql", Content: []byte("7 down")},
		{BucketName: "some-bucket", Name: "prod/migrations/not-a-migration.txt"},
		{BucketName: "some-bucket", Name: "prod/migrations/0-random-stuff/whatever.txt"},
	})
	defer server.Stop()
	driver := gcs{
		bucket:     server.Client().Bucket("some-bucket"),
		prefix:     "prod/migrations/",
		migrations: source.NewMigrations(),
	}
	err := driver.loadMigrations()
	if err != nil {
		t.Fatal(err)
	}
	st.Test(t, &driver)
}
```

## File: `source/go_bindata/go-bindata.go`
```go
package bindata

import (
	"bytes"
	"fmt"
	"io"
	"os"

	"github.com/golang-migrate/migrate/v4/source"
)

type AssetFunc func(name string) ([]byte, error)

func Resource(names []string, afn AssetFunc) *AssetSource {
	return &AssetSource{
		Names:     names,
		AssetFunc: afn,
	}
}

type AssetSource struct {
	Names     []string
	AssetFunc AssetFunc
}

func init() {
	source.Register("go-bindata", &Bindata{})
}

type Bindata struct {
	path        string
	assetSource *AssetSource
	migrations  *source.Migrations
}

func (b *Bindata) Open(url string) (source.Driver, error) {
	return nil, fmt.Errorf("not yet implemented")
}

var (
	ErrNoAssetSource = fmt.Errorf("expects *AssetSource")
)

func WithInstance(instance interface{}) (source.Driver, error) {
	if _, ok := instance.(*AssetSource); !ok {
		return nil, ErrNoAssetSource
	}
	as := instance.(*AssetSource)

	bn := &Bindata{
		path:        "<go-bindata>",
		assetSource: as,
		migrations:  source.NewMigrations(),
	}

	for _, fi := range as.Names {
		m, err := source.DefaultParse(fi)
		if err != nil {
			continue // ignore files that we can't parse
		}

		if !bn.migrations.Append(m) {
			return nil, fmt.Errorf("unable to parse file %v", fi)
		}
	}

	return bn, nil
}

func (b *Bindata) Close() error {
	return nil
}

func (b *Bindata) First() (version uint, err error) {
	if v, ok := b.migrations.First(); !ok {
		return 0, &os.PathError{Op: "first", Path: b.path, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (b *Bindata) Prev(version uint) (prevVersion uint, err error) {
	if v, ok := b.migrations.Prev(version); !ok {
		return 0, &os.PathError{Op: fmt.Sprintf("prev for version %v", version), Path: b.path, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (b *Bindata) Next(version uint) (nextVersion uint, err error) {
	if v, ok := b.migrations.Next(version); !ok {
		return 0, &os.PathError{Op: fmt.Sprintf("next for version %v", version), Path: b.path, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (b *Bindata) ReadUp(version uint) (r io.ReadCloser, identifier string, err error) {
	if m, ok := b.migrations.Up(version); ok {
		body, err := b.assetSource.AssetFunc(m.Raw)
		if err != nil {
			return nil, "", err
		}
		return io.NopCloser(bytes.NewReader(body)), m.Identifier, nil
	}
	return nil, "", &os.PathError{Op: fmt.Sprintf("read version %v", version), Path: b.path, Err: os.ErrNotExist}
}

func (b *Bindata) ReadDown(version uint) (r io.ReadCloser, identifier string, err error) {
	if m, ok := b.migrations.Down(version); ok {
		body, err := b.assetSource.AssetFunc(m.Raw)
		if err != nil {
			return nil, "", err
		}
		return io.NopCloser(bytes.NewReader(body)), m.Identifier, nil
	}
	return nil, "", &os.PathError{Op: fmt.Sprintf("read version %v", version), Path: b.path, Err: os.ErrNotExist}
}
```

## File: `source/go_bindata/go-bindata_test.go`
```go
package bindata

import (
	"testing"

	"github.com/golang-migrate/migrate/v4/source/go_bindata/testdata"
	st "github.com/golang-migrate/migrate/v4/source/testing"
)

func Test(t *testing.T) {
	// wrap assets into Resource first
	s := Resource(testdata.AssetNames(),
		func(name string) ([]byte, error) {
			return testdata.Asset(name)
		})

	d, err := WithInstance(s)
	if err != nil {
		t.Fatal(err)
	}
	st.Test(t, d)
}

func TestWithInstance(t *testing.T) {
	// wrap assets into Resource
	s := Resource(testdata.AssetNames(),
		func(name string) ([]byte, error) {
			return testdata.Asset(name)
		})

	_, err := WithInstance(s)
	if err != nil {
		t.Fatal(err)
	}
}

func TestOpen(t *testing.T) {
	b := &Bindata{}
	_, err := b.Open("")
	if err == nil {
		t.Fatal("expected err, because it's not implemented yet")
	}
}
```

## File: `source/go_bindata/README.md`
```markdown
# go_bindata

## Usage



### Read bindata with NewWithSourceInstance

```shell
go get -u github.com/jteeuwen/go-bindata/...
cd examples/migrations && go-bindata -pkg migrations .
```

```go
import (
  "github.com/golang-migrate/migrate/v4"
  "github.com/golang-migrate/migrate/v4/source/go_bindata"
  "github.com/golang-migrate/migrate/v4/source/go_bindata/examples/migrations"
)

func main() {
  // wrap assets into Resource
  s := bindata.Resource(migrations.AssetNames(),
    func(name string) ([]byte, error) {
      return migrations.Asset(name)
    })
    
  d, err := bindata.WithInstance(s)
  m, err := migrate.NewWithSourceInstance("go-bindata", d, "database://foobar")
  m.Up() // run your migrations and handle the errors above of course
}
```

### Read bindata with URL (todo)

This will restore the assets in a tmp directory and then
proxy to source/file. go-bindata must be in your `$PATH`.

```
migrate -source go-bindata://examples/migrations/bindata.go
```


```

## File: `source/go_bindata/examples/migrations/bindata.go`
```go
// Code generated by go-bindata.
// sources:
// 1085649617_create_users_table.down.sql
// 1085649617_create_users_table.up.sql
// 1185749658_add_city_to_users.down.sql
// 1185749658_add_city_to_users.up.sql
// DO NOT EDIT!

package testdata

import (
	"bytes"
	"compress/gzip"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"
	"time"
)

func bindataRead(data []byte, name string) ([]byte, error) {
	gz, err := gzip.NewReader(bytes.NewBuffer(data))
	if err != nil {
		return nil, fmt.Errorf("Read %q: %v", name, err)
	}

	var buf bytes.Buffer
	_, err = io.Copy(&buf, gz)
	clErr := gz.Close()

	if err != nil {
		return nil, fmt.Errorf("Read %q: %v", name, err)
	}
	if clErr != nil {
		return nil, err
	}

	return buf.Bytes(), nil
}

type asset struct {
	bytes []byte
	info  os.FileInfo
}

type bindataFileInfo struct {
	name    string
	size    int64
	mode    os.FileMode
	modTime time.Time
}

func (fi bindataFileInfo) Name() string {
	return fi.name
}
func (fi bindataFileInfo) Size() int64 {
	return fi.size
}
func (fi bindataFileInfo) Mode() os.FileMode {
	return fi.mode
}
func (fi bindataFileInfo) ModTime() time.Time {
	return fi.modTime
}
func (fi bindataFileInfo) IsDir() bool {
	return false
}
func (fi bindataFileInfo) Sys() interface{} {
	return nil
}

var __1085649617_create_users_tableDownSql = []byte("\x1f\x8b\x08\x00\x00\x09\x6e\x88\x00\xff\x72\x09\xf2\x0f\x50\x08\x71\x74\xf2\x71\x55\xf0\x74\x53\x70\x8d\xf0\x0c\x0e\x09\x56\x28\x2d\x4e\x2d\x2a\xb6\xe6\x02\x04\x00\x00\xff\xff\x2c\x02\x3d\xa7\x1c\x00\x00\x00")

func _1085649617_create_users_tableDownSqlBytes() ([]byte, error) {
	return bindataRead(
		__1085649617_create_users_tableDownSql,
		"1085649617_create_users_table.down.sql",
	)
}

func _1085649617_create_users_tableDownSql() (*asset, error) {
	bytes, err := _1085649617_create_users_tableDownSqlBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "1085649617_create_users_table.down.sql", size: 28, mode: os.FileMode(420), modTime: time.Unix(1485750305, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var __1085649617_create_users_tableUpSql = []byte("\x1f\x8b\x08\x00\x00\x09\x6e\x88\x00\xff\x72\x0e\x72\x75\x0c\x71\x55\x08\x71\x74\xf2\x71\x55\x28\x2d\x4e\x2d\x2a\x56\xd0\xe0\x52\x00\xb3\xe2\x33\x53\x14\x32\xf3\x4a\x52\xd3\x53\x8b\x14\x4a\xf3\x32\x0b\x4b\x53\x75\xb8\x14\x14\xf2\x12\x73\x53\x15\x14\x14\x14\xca\x12\x8b\x92\x33\x12\x8b\x34\x4c\x0c\x34\x41\xc2\xa9\xb9\x89\x99\x39\xa8\xc2\x5c\x9a\xd6\x5c\x80\x00\x00\x00\xff\xff\xa3\x57\xbc\x0b\x5f\x00\x00\x00")

func _1085649617_create_users_tableUpSqlBytes() ([]byte, error) {
	return bindataRead(
		__1085649617_create_users_tableUpSql,
		"1085649617_create_users_table.up.sql",
	)
}

func _1085649617_create_users_tableUpSql() (*asset, error) {
	bytes, err := _1085649617_create_users_tableUpSqlBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "1085649617_create_users_table.up.sql", size: 95, mode: os.FileMode(420), modTime: time.Unix(1485803085, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var __1185749658_add_city_to_usersDownSql = []byte("\x1f\x8b\x08\x00\x00\x09\x6e\x88\x00\xff\x72\xf4\x09\x71\x0d\x52\x08\x71\x74\xf2\x71\x55\x28\x2d\x4e\x2d\x2a\x56\x70\x09\xf2\x0f\x50\x70\xf6\xf7\x09\xf5\xf5\x53\xf0\x74\x53\x70\x8d\xf0\x0c\x0e\x09\x56\x48\xce\x2c\xa9\xb4\xe6\x02\x04\x00\x00\xff\xff\xb7\x52\x88\xd7\x2e\x00\x00\x00")

func _1185749658_add_city_to_usersDownSqlBytes() ([]byte, error) {
	return bindataRead(
		__1185749658_add_city_to_usersDownSql,
		"1185749658_add_city_to_users.down.sql",
	)
}

func _1185749658_add_city_to_usersDownSql() (*asset, error) {
	bytes, err := _1185749658_add_city_to_usersDownSqlBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "1185749658_add_city_to_users.down.sql", size: 46, mode: os.FileMode(420), modTime: time.Unix(1485750443, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var __1185749658_add_city_to_usersUpSql = []byte("\x1f\x8b\x08\x00\x00\x09\x6e\x88\x00\xff\x72\xf4\x09\x71\x0d\x52\x08\x71\x74\xf2\x71\x55\x28\x2d\x4e\x2d\x2a\x56\x70\x74\x71\x51\x70\xf6\xf7\x09\xf5\xf5\x53\x48\xce\x2c\xa9\x54\x28\x4b\x2c\x4a\xce\x48\x2c\xd2\x30\x34\x30\xd0\xb4\xe6\xe2\xe2\x02\x04\x00\x00\xff\xff\xa8\x0f\x49\xc6\x32\x00\x00\x00")

func _1185749658_add_city_to_usersUpSqlBytes() ([]byte, error) {
	return bindataRead(
		__1185749658_add_city_to_usersUpSql,
		"1185749658_add_city_to_users.up.sql",
	)
}

func _1185749658_add_city_to_usersUpSql() (*asset, error) {
	bytes, err := _1185749658_add_city_to_usersUpSqlBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "1185749658_add_city_to_users.up.sql", size: 50, mode: os.FileMode(420), modTime: time.Unix(1485843733, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

// Asset loads and returns the asset for the given name.
// It returns an error if the asset could not be found or
// could not be loaded.
func Asset(name string) ([]byte, error) {
	cannonicalName := strings.Replace(name, "\\", "/", -1)
	if f, ok := _bindata[cannonicalName]; ok {
		a, err := f()
		if err != nil {
			return nil, fmt.Errorf("Asset %s can't read by error: %v", name, err)
		}
		return a.bytes, nil
	}
	return nil, fmt.Errorf("Asset %s not found", name)
}

// MustAsset is like Asset but panics when Asset would return an error.
// It simplifies safe initialization of global variables.
func MustAsset(name string) []byte {
	a, err := Asset(name)
	if err != nil {
		panic("asset: Asset(" + name + "): " + err.Error())
	}

	return a
}

// AssetInfo loads and returns the asset info for the given name.
// It returns an error if the asset could not be found or
// could not be loaded.
func AssetInfo(name string) (os.FileInfo, error) {
	cannonicalName := strings.Replace(name, "\\", "/", -1)
	if f, ok := _bindata[cannonicalName]; ok {
		a, err := f()
		if err != nil {
			return nil, fmt.Errorf("AssetInfo %s can't read by error: %v", name, err)
		}
		return a.info, nil
	}
	return nil, fmt.Errorf("AssetInfo %s not found", name)
}

// AssetNames returns the names of the assets.
func AssetNames() []string {
	names := make([]string, 0, len(_bindata))
	for name := range _bindata {
		names = append(names, name)
	}
	return names
}

// _bindata is a table, holding each asset generator, mapped to its name.
var _bindata = map[string]func() (*asset, error){
	"1085649617_create_users_table.down.sql": _1085649617_create_users_tableDownSql,
	"1085649617_create_users_table.up.sql":   _1085649617_create_users_tableUpSql,
	"1185749658_add_city_to_users.down.sql":  _1185749658_add_city_to_usersDownSql,
	"1185749658_add_city_to_users.up.sql":    _1185749658_add_city_to_usersUpSql,
}

// AssetDir returns the file names below a certain
// directory embedded in the file by go-bindata.
// For example if you run go-bindata on data/... and data contains the
// following hierarchy:
//
//	data/
//	  foo.txt
//	  img/
//	    a.png
//	    b.png
//
// then AssetDir("data") would return []string{"foo.txt", "img"}
// AssetDir("data/img") would return []string{"a.png", "b.png"}
// AssetDir("foo.txt") and AssetDir("notexist") would return an error
// AssetDir("") will return []string{"data"}.
func AssetDir(name string) ([]string, error) {
	node := _bintree
	if len(name) != 0 {
		cannonicalName := strings.Replace(name, "\\", "/", -1)
		pathList := strings.Split(cannonicalName, "/")
		for _, p := range pathList {
			node = node.Children[p]
			if node == nil {
				return nil, fmt.Errorf("Asset %s not found", name)
			}
		}
	}
	if node.Func != nil {
		return nil, fmt.Errorf("Asset %s not found", name)
	}
	rv := make([]string, 0, len(node.Children))
	for childName := range node.Children {
		rv = append(rv, childName)
	}
	return rv, nil
}

type bintree struct {
	Func     func() (*asset, error)
	Children map[string]*bintree
}

var _bintree = &bintree{nil, map[string]*bintree{
	"1085649617_create_users_table.down.sql": &bintree{_1085649617_create_users_tableDownSql, map[string]*bintree{}},
	"1085649617_create_users_table.up.sql":   &bintree{_1085649617_create_users_tableUpSql, map[string]*bintree{}},
	"1185749658_add_city_to_users.down.sql":  &bintree{_1185749658_add_city_to_usersDownSql, map[string]*bintree{}},
	"1185749658_add_city_to_users.up.sql":    &bintree{_1185749658_add_city_to_usersUpSql, map[string]*bintree{}},
}}

// RestoreAsset restores an asset under the given directory
func RestoreAsset(dir, name string) error {
	data, err := Asset(name)
	if err != nil {
		return err
	}
	info, err := AssetInfo(name)
	if err != nil {
		return err
	}
	err = os.MkdirAll(_filePath(dir, filepath.Dir(name)), os.FileMode(0755))
	if err != nil {
		return err
	}
	err = os.WriteFile(_filePath(dir, name), data, info.Mode())
	if err != nil {
		return err
	}
	err = os.Chtimes(_filePath(dir, name), info.ModTime(), info.ModTime())
	if err != nil {
		return err
	}
	return nil
}

// RestoreAssets restores an asset under the given directory recursively
func RestoreAssets(dir, name string) error {
	children, err := AssetDir(name)
	// File
	if err != nil {
		return RestoreAsset(dir, name)
	}
	// Dir
	for _, child := range children {
		err = RestoreAssets(dir, filepath.Join(name, child))
		if err != nil {
			return err
		}
	}
	return nil
}

func _filePath(dir, name string) string {
	cannonicalName := strings.Replace(name, "\\", "/", -1)
	return filepath.Join(append([]string{dir}, strings.Split(cannonicalName, "/")...)...)
}
```

## File: `source/go_bindata/testdata/bindata.go`
```go
// Code generated by go-bindata.
// sources:
// 1_test.down.sql
// 1_test.up.sql
// 3_test.up.sql
// 4_test.down.sql
// 4_test.up.sql
// 5_test.down.sql
// 7_test.down.sql
// 7_test.up.sql
// DO NOT EDIT!

package testdata

import (
	"bytes"
	"compress/gzip"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"
	"time"
)

func bindataRead(data []byte, name string) ([]byte, error) {
	gz, err := gzip.NewReader(bytes.NewBuffer(data))
	if err != nil {
		return nil, fmt.Errorf("Read %q: %v", name, err)
	}

	var buf bytes.Buffer
	_, err = io.Copy(&buf, gz)
	clErr := gz.Close()

	if err != nil {
		return nil, fmt.Errorf("Read %q: %v", name, err)
	}
	if clErr != nil {
		return nil, err
	}

	return buf.Bytes(), nil
}

type asset struct {
	bytes []byte
	info  os.FileInfo
}

type bindataFileInfo struct {
	name    string
	size    int64
	mode    os.FileMode
	modTime time.Time
}

func (fi bindataFileInfo) Name() string {
	return fi.name
}
func (fi bindataFileInfo) Size() int64 {
	return fi.size
}
func (fi bindataFileInfo) Mode() os.FileMode {
	return fi.mode
}
func (fi bindataFileInfo) ModTime() time.Time {
	return fi.modTime
}
func (fi bindataFileInfo) IsDir() bool {
	return false
}
func (fi bindataFileInfo) Sys() interface{} {
	return nil
}

var __1_testDownSql = []byte("\x1f\x8b\x08\x00\x00\x09\x6e\x88\x00\xff\x01\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00")

func _1_testDownSqlBytes() ([]byte, error) {
	return bindataRead(
		__1_testDownSql,
		"1_test.down.sql",
	)
}

func _1_testDownSql() (*asset, error) {
	bytes, err := _1_testDownSqlBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "1_test.down.sql", size: 0, mode: os.FileMode(420), modTime: time.Unix(1486440324, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var __1_testUpSql = []byte("\x1f\x8b\x08\x00\x00\x09\x6e\x88\x00\xff\x01\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00")

func _1_testUpSqlBytes() ([]byte, error) {
	return bindataRead(
		__1_testUpSql,
		"1_test.up.sql",
	)
}

func _1_testUpSql() (*asset, error) {
	bytes, err := _1_testUpSqlBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "1_test.up.sql", size: 0, mode: os.FileMode(420), modTime: time.Unix(1486440319, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var __3_testUpSql = []byte("\x1f\x8b\x08\x00\x00\x09\x6e\x88\x00\xff\x01\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00")

func _3_testUpSqlBytes() ([]byte, error) {
	return bindataRead(
		__3_testUpSql,
		"3_test.up.sql",
	)
}

func _3_testUpSql() (*asset, error) {
	bytes, err := _3_testUpSqlBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "3_test.up.sql", size: 0, mode: os.FileMode(420), modTime: time.Unix(1486440331, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var __4_testDownSql = []byte("\x1f\x8b\x08\x00\x00\x09\x6e\x88\x00\xff\x01\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00")

func _4_testDownSqlBytes() ([]byte, error) {
	return bindataRead(
		__4_testDownSql,
		"4_test.down.sql",
	)
}

func _4_testDownSql() (*asset, error) {
	bytes, err := _4_testDownSqlBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "4_test.down.sql", size: 0, mode: os.FileMode(420), modTime: time.Unix(1486440337, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var __4_testUpSql = []byte("\x1f\x8b\x08\x00\x00\x09\x6e\x88\x00\xff\x01\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00")

func _4_testUpSqlBytes() ([]byte, error) {
	return bindataRead(
		__4_testUpSql,
		"4_test.up.sql",
	)
}

func _4_testUpSql() (*asset, error) {
	bytes, err := _4_testUpSqlBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "4_test.up.sql", size: 0, mode: os.FileMode(420), modTime: time.Unix(1486440335, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var __5_testDownSql = []byte("\x1f\x8b\x08\x00\x00\x09\x6e\x88\x00\xff\x01\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00")

func _5_testDownSqlBytes() ([]byte, error) {
	return bindataRead(
		__5_testDownSql,
		"5_test.down.sql",
	)
}

func _5_testDownSql() (*asset, error) {
	bytes, err := _5_testDownSqlBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "5_test.down.sql", size: 0, mode: os.FileMode(420), modTime: time.Unix(1486440340, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var __7_testDownSql = []byte("\x1f\x8b\x08\x00\x00\x09\x6e\x88\x00\xff\x01\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00")

func _7_testDownSqlBytes() ([]byte, error) {
	return bindataRead(
		__7_testDownSql,
		"7_test.down.sql",
	)
}

func _7_testDownSql() (*asset, error) {
	bytes, err := _7_testDownSqlBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "7_test.down.sql", size: 0, mode: os.FileMode(420), modTime: time.Unix(1486440343, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var __7_testUpSql = []byte("\x1f\x8b\x08\x00\x00\x09\x6e\x88\x00\xff\x01\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00")

func _7_testUpSqlBytes() ([]byte, error) {
	return bindataRead(
		__7_testUpSql,
		"7_test.up.sql",
	)
}

func _7_testUpSql() (*asset, error) {
	bytes, err := _7_testUpSqlBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "7_test.up.sql", size: 0, mode: os.FileMode(420), modTime: time.Unix(1486440347, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

// Asset loads and returns the asset for the given name.
// It returns an error if the asset could not be found or
// could not be loaded.
func Asset(name string) ([]byte, error) {
	cannonicalName := strings.Replace(name, "\\", "/", -1)
	if f, ok := _bindata[cannonicalName]; ok {
		a, err := f()
		if err != nil {
			return nil, fmt.Errorf("Asset %s can't read by error: %v", name, err)
		}
		return a.bytes, nil
	}
	return nil, fmt.Errorf("Asset %s not found", name)
}

// MustAsset is like Asset but panics when Asset would return an error.
// It simplifies safe initialization of global variables.
func MustAsset(name string) []byte {
	a, err := Asset(name)
	if err != nil {
		panic("asset: Asset(" + name + "): " + err.Error())
	}

	return a
}

// AssetInfo loads and returns the asset info for the given name.
// It returns an error if the asset could not be found or
// could not be loaded.
func AssetInfo(name string) (os.FileInfo, error) {
	cannonicalName := strings.Replace(name, "\\", "/", -1)
	if f, ok := _bindata[cannonicalName]; ok {
		a, err := f()
		if err != nil {
			return nil, fmt.Errorf("AssetInfo %s can't read by error: %v", name, err)
		}
		return a.info, nil
	}
	return nil, fmt.Errorf("AssetInfo %s not found", name)
}

// AssetNames returns the names of the assets.
func AssetNames() []string {
	names := make([]string, 0, len(_bindata))
	for name := range _bindata {
		names = append(names, name)
	}
	return names
}

// _bindata is a table, holding each asset generator, mapped to its name.
var _bindata = map[string]func() (*asset, error){
	"1_test.down.sql": _1_testDownSql,
	"1_test.up.sql":   _1_testUpSql,
	"3_test.up.sql":   _3_testUpSql,
	"4_test.down.sql": _4_testDownSql,
	"4_test.up.sql":   _4_testUpSql,
	"5_test.down.sql": _5_testDownSql,
	"7_test.down.sql": _7_testDownSql,
	"7_test.up.sql":   _7_testUpSql,
}

// AssetDir returns the file names below a certain
// directory embedded in the file by go-bindata.
// For example if you run go-bindata on data/... and data contains the
// following hierarchy:
//     data/
//       foo.txt
//       img/
//         a.png
//         b.png
// then AssetDir("data") would return []string{"foo.txt", "img"}
// AssetDir("data/img") would return []string{"a.png", "b.png"}
// AssetDir("foo.txt") and AssetDir("notexist") would return an error
// AssetDir("") will return []string{"data"}.
func AssetDir(name string) ([]string, error) {
	node := _bintree
	if len(name) != 0 {
		cannonicalName := strings.Replace(name, "\\", "/", -1)
		pathList := strings.Split(cannonicalName, "/")
		for _, p := range pathList {
			node = node.Children[p]
			if node == nil {
				return nil, fmt.Errorf("Asset %s not found", name)
			}
		}
	}
	if node.Func != nil {
		return nil, fmt.Errorf("Asset %s not found", name)
	}
	rv := make([]string, 0, len(node.Children))
	for childName := range node.Children {
		rv = append(rv, childName)
	}
	return rv, nil
}

type bintree struct {
	Func     func() (*asset, error)
	Children map[string]*bintree
}

var _bintree = &bintree{nil, map[string]*bintree{
	"1_test.down.sql": &bintree{_1_testDownSql, map[string]*bintree{}},
	"1_test.up.sql":   &bintree{_1_testUpSql, map[string]*bintree{}},
	"3_test.up.sql":   &bintree{_3_testUpSql, map[string]*bintree{}},
	"4_test.down.sql": &bintree{_4_testDownSql, map[string]*bintree{}},
	"4_test.up.sql":   &bintree{_4_testUpSql, map[string]*bintree{}},
	"5_test.down.sql": &bintree{_5_testDownSql, map[string]*bintree{}},
	"7_test.down.sql": &bintree{_7_testDownSql, map[string]*bintree{}},
	"7_test.up.sql":   &bintree{_7_testUpSql, map[string]*bintree{}},
}}

// RestoreAsset restores an asset under the given directory
func RestoreAsset(dir, name string) error {
	data, err := Asset(name)
	if err != nil {
		return err
	}
	info, err := AssetInfo(name)
	if err != nil {
		return err
	}
	err = os.MkdirAll(_filePath(dir, filepath.Dir(name)), os.FileMode(0755))
	if err != nil {
		return err
	}
	err = os.WriteFile(_filePath(dir, name), data, info.Mode())
	if err != nil {
		return err
	}
	err = os.Chtimes(_filePath(dir, name), info.ModTime(), info.ModTime())
	if err != nil {
		return err
	}
	return nil
}

// RestoreAssets restores an asset under the given directory recursively
func RestoreAssets(dir, name string) error {
	children, err := AssetDir(name)
	// File
	if err != nil {
		return RestoreAsset(dir, name)
	}
	// Dir
	for _, child := range children {
		err = RestoreAssets(dir, filepath.Join(name, child))
		if err != nil {
			return err
		}
	}
	return nil
}

func _filePath(dir, name string) string {
	cannonicalName := strings.Replace(name, "\\", "/", -1)
	return filepath.Join(append([]string{dir}, strings.Split(cannonicalName, "/")...)...)
}
```

## File: `source/httpfs/driver.go`
```go
package httpfs

import (
	"errors"
	"net/http"

	"github.com/golang-migrate/migrate/v4/source"
)

// driver is a migration source driver for reading migrations from
// http.FileSystem instances. It implements source.Driver interface and can be
// used as a migration source for the main migrate library.
type driver struct {
	PartialDriver
}

// New creates a new migrate source driver from a http.FileSystem instance and a
// relative path to migration files within the virtual FS.
func New(fs http.FileSystem, path string) (source.Driver, error) {
	var d driver
	if err := d.Init(fs, path); err != nil {
		return nil, err
	}
	return &d, nil
}

// Open completes the implementetion of source.Driver interface. Other methods
// are implemented by the embedded PartialDriver struct.
func (d *driver) Open(url string) (source.Driver, error) {
	return nil, errors.New("open() cannot be called on the httpfs passthrough driver")
}
```

## File: `source/httpfs/driver_test.go`
```go
package httpfs_test

import (
	"net/http"
	"testing"

	"github.com/golang-migrate/migrate/v4/source/httpfs"
	st "github.com/golang-migrate/migrate/v4/source/testing"
)

func TestNewOK(t *testing.T) {
	d, err := httpfs.New(http.Dir("testdata"), "sql")
	if err != nil {
		t.Errorf("New() expected not error, got: %s", err)
	}
	st.Test(t, d)
}

func TestNewErrors(t *testing.T) {
	d, err := httpfs.New(http.Dir("does-not-exist"), "")
	if err == nil {
		t.Errorf("New() expected to return error")
	}
	if d != nil {
		t.Errorf("New() expected to return nil driver")
	}
}

func TestOpen(t *testing.T) {
	d, err := httpfs.New(http.Dir("testdata/sql"), "")
	if err != nil {
		t.Error("New() expected no error")
		return
	}
	d, err = d.Open("")
	if d != nil {
		t.Error("Open() expected to return nil driver")
	}
	if err == nil {
		t.Error("Open() expected to return error")
	}
}
```

## File: `source/httpfs/partial_driver.go`
```go
package httpfs

import (
	"errors"
	"io"
	"net/http"
	"os"
	"path"
	"strconv"

	"github.com/golang-migrate/migrate/v4/source"
)

// PartialDriver is a helper service for creating new source drivers working with
// http.FileSystem instances. It implements all source.Driver interface methods
// except for Open(). New driver could embed this struct and add missing Open()
// method.
//
// To prepare PartialDriver for use Init() function.
type PartialDriver struct {
	migrations *source.Migrations
	fs         http.FileSystem
	path       string
}

// Init prepares not initialized PartialDriver instance to read migrations from a
// http.FileSystem instance and a relative path.
func (p *PartialDriver) Init(fs http.FileSystem, path string) error {
	root, err := fs.Open(path)
	if err != nil {
		return err
	}

	files, err := root.Readdir(0)
	if err != nil {
		_ = root.Close()
		return err
	}
	if err = root.Close(); err != nil {
		return err
	}

	ms := source.NewMigrations()
	for _, file := range files {
		if file.IsDir() {
			continue
		}

		m, err := source.DefaultParse(file.Name())
		if err != nil {
			continue // ignore files that we can't parse
		}

		if !ms.Append(m) {
			return source.ErrDuplicateMigration{
				Migration: *m,
				FileInfo:  file,
			}
		}
	}

	p.fs = fs
	p.path = path
	p.migrations = ms
	return nil
}

// Close is part of source.Driver interface implementation. This is a no-op.
func (p *PartialDriver) Close() error {
	return nil
}

// First is part of source.Driver interface implementation.
func (p *PartialDriver) First() (version uint, err error) {
	if version, ok := p.migrations.First(); ok {
		return version, nil
	}
	return 0, &os.PathError{
		Op:   "first",
		Path: p.path,
		Err:  os.ErrNotExist,
	}
}

// Prev is part of source.Driver interface implementation.
func (p *PartialDriver) Prev(version uint) (prevVersion uint, err error) {
	if version, ok := p.migrations.Prev(version); ok {
		return version, nil
	}
	return 0, &os.PathError{
		Op:   "prev for version " + strconv.FormatUint(uint64(version), 10),
		Path: p.path,
		Err:  os.ErrNotExist,
	}
}

// Next is part of source.Driver interface implementation.
func (p *PartialDriver) Next(version uint) (nextVersion uint, err error) {
	if version, ok := p.migrations.Next(version); ok {
		return version, nil
	}
	return 0, &os.PathError{
		Op:   "next for version " + strconv.FormatUint(uint64(version), 10),
		Path: p.path,
		Err:  os.ErrNotExist,
	}
}

// ReadUp is part of source.Driver interface implementation.
func (p *PartialDriver) ReadUp(version uint) (r io.ReadCloser, identifier string, err error) {
	if m, ok := p.migrations.Up(version); ok {
		body, err := p.open(path.Join(p.path, m.Raw))
		if err != nil {
			return nil, "", err
		}
		return body, m.Identifier, nil
	}
	return nil, "", &os.PathError{
		Op:   "read up for version " + strconv.FormatUint(uint64(version), 10),
		Path: p.path,
		Err:  os.ErrNotExist,
	}
}

// ReadDown is part of source.Driver interface implementation.
func (p *PartialDriver) ReadDown(version uint) (r io.ReadCloser, identifier string, err error) {
	if m, ok := p.migrations.Down(version); ok {
		body, err := p.open(path.Join(p.path, m.Raw))
		if err != nil {
			return nil, "", err
		}
		return body, m.Identifier, nil
	}
	return nil, "", &os.PathError{
		Op:   "read down for version " + strconv.FormatUint(uint64(version), 10),
		Path: p.path,
		Err:  os.ErrNotExist,
	}
}

func (p *PartialDriver) open(path string) (http.File, error) {
	f, err := p.fs.Open(path)
	if err == nil {
		return f, nil
	}
	// Some non-standard file systems may return errors that don't include the path, that
	// makes debugging harder.
	if !errors.As(err, new(*os.PathError)) {
		err = &os.PathError{
			Op:   "open",
			Path: path,
			Err:  err,
		}
	}
	return nil, err
}
```

## File: `source/httpfs/partial_driver_test.go`
```go
package httpfs_test

import (
	"errors"
	"net/http"
	"strings"
	"testing"

	"github.com/golang-migrate/migrate/v4/source"
	"github.com/golang-migrate/migrate/v4/source/httpfs"
	st "github.com/golang-migrate/migrate/v4/source/testing"
)

type driver struct{ httpfs.PartialDriver }

func (d *driver) Open(url string) (source.Driver, error) { return nil, errors.New("X") }

type driverExample struct {
	httpfs.PartialDriver
}

func (d *driverExample) Open(url string) (source.Driver, error) {
	parts := strings.Split(url, ":")
	dir := parts[0]
	path := ""
	if len(parts) >= 2 {
		path = parts[1]
	}

	var de driverExample
	return &de, de.Init(http.Dir(dir), path)
}

func TestDriverExample(t *testing.T) {
	d, err := (*driverExample)(nil).Open("testdata:sql")
	if err != nil {
		t.Errorf("Open() returned error: %s", err)
	}
	st.Test(t, d)
}

func TestPartialDriverInit(t *testing.T) {
	tests := []struct {
		name string
		fs   http.FileSystem
		path string
		ok   bool
	}{
		{
			name: "valid dir and empty path",
			fs:   http.Dir("testdata/sql"),
			ok:   true,
		},
		{
			name: "valid dir and non-empty path",
			fs:   http.Dir("testdata"),
			path: "sql",
			ok:   true,
		},
		{
			name: "invalid dir",
			fs:   http.Dir("does-not-exist"),
		},
		{
			name: "file instead of dir",
			fs:   http.Dir("testdata/sql/1_foobar.up.sql"),
		},
		{
			name: "dir with duplicates",
			fs:   http.Dir("testdata/duplicates"),
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			var d driver
			err := d.Init(test.fs, test.path)
			if test.ok {
				if err != nil {
					t.Errorf("Init() returned error %s", err)
				}
				st.Test(t, &d)
				if err = d.Close(); err != nil {
					t.Errorf("Init().Close() returned error %s", err)
				}
			} else {
				if err == nil {
					t.Errorf("Init() expected error but did not get one")
				}
			}
		})
	}

}

func TestFirstWithNoMigrations(t *testing.T) {
	var d driver
	fs := http.Dir("testdata/no-migrations")

	if err := d.Init(fs, ""); err != nil {
		t.Errorf("No error on Init() expected, got: %v", err)
	}

	if _, err := d.First(); err == nil {
		t.Errorf("Expected error on First(), got: %v", err)
	}
}
```

## File: `source/httpfs/README.md`
```markdown
# httpfs

## Usage

This package could be used to create new migration source drivers that uses
`http.FileSystem` to read migration files.

Struct `httpfs.PartialDriver` partly implements the `source.Driver` interface. It has all
the methods except for `Open()`. Embedding this struct and adding `Open()` method
allows users of this package to create new migration sources. Example:

```go
struct mydriver {
        httpfs.PartialDriver
}

func (d *mydriver) Open(url string) (source.Driver, error) {
	var fs http.FileSystem
	var path string
	var ds mydriver

	// acquire fs and path from url
	// set-up ds if necessary

	if err := ds.Init(fs, path); err != nil {
		return nil, err
	}
	return &ds, nil
}
```

This package also provides a simple `source.Driver` implementation that works
with `http.FileSystem` provided by the user of this package. It is created with
`httpfs.New()` call.

Example of using `http.Dir()` to read migrations from `sql` directory:

```go
	src, err := httpfs.New(http.Dir("sql"))
	if err != nil {
		// do something
	}
	m, err := migrate.NewWithSourceInstance("httpfs", src, "database://url")
	if err != nil {
		// do something
	}
        err = m.Up()
	...
```
```

## File: `source/httpfs/testdata/duplicates/1_foobar.up.sql`
```sql
1 up
```

## File: `source/httpfs/testdata/duplicates/1_foobaz.up.sql`
```sql
1 up
```

## File: `source/httpfs/testdata/sql/1_foobar.down.sql`
```sql
1 down
```

## File: `source/httpfs/testdata/sql/1_foobar.up.sql`
```sql
1 up
```

## File: `source/httpfs/testdata/sql/3_foobar.up.sql`
```sql
3 up
```

## File: `source/httpfs/testdata/sql/4_foobar.down.sql`
```sql
4 down
```

## File: `source/httpfs/testdata/sql/4_foobar.up.sql`
```sql
4 up
```

## File: `source/httpfs/testdata/sql/5_foobar.down.sql`
```sql
5 down
```

## File: `source/httpfs/testdata/sql/7_foobar.down.sql`
```sql
7 down
```

## File: `source/httpfs/testdata/sql/7_foobar.up.sql`
```sql
7 up
```

## File: `source/iofs/doc.go`
```go
/*
Package iofs provides the Go 1.16+ io/fs#FS driver.

It can accept various file systems (like embed.FS, archive/zip#Reader) implementing io/fs#FS.

This driver cannot be used with Go versions 1.15 and below.

Also, Opening with a URL scheme is not supported.
*/
package iofs
```

## File: `source/iofs/example_test.go`
```go
//go:build go1.16

package iofs_test

import (
	"embed"
	"log"

	"github.com/golang-migrate/migrate/v4"
	_ "github.com/golang-migrate/migrate/v4/database/postgres"
	"github.com/golang-migrate/migrate/v4/source/iofs"
)

//go:embed testdata/migrations/*.sql
var fs embed.FS

func Example() {
	d, err := iofs.New(fs, "testdata/migrations")
	if err != nil {
		log.Fatal(err)
	}
	m, err := migrate.NewWithSourceInstance("iofs", d, "postgres://postgres@localhost/postgres?sslmode=disable")
	if err != nil {
		log.Fatal(err)
	}
	err = m.Up()
	if err != nil {
		// ...
	}
	// ...
}
```

## File: `source/iofs/iofs.go`
```go
//go:build go1.16

package iofs

import (
	"errors"
	"fmt"
	"io"
	"io/fs"
	"path"
	"strconv"

	"github.com/golang-migrate/migrate/v4/source"
)

type driver struct {
	PartialDriver
}

// New returns a new Driver from io/fs#FS and a relative path.
func New(fsys fs.FS, path string) (source.Driver, error) {
	var i driver
	if err := i.Init(fsys, path); err != nil {
		return nil, fmt.Errorf("failed to init driver with path %s: %w", path, err)
	}
	return &i, nil
}

// Open is part of source.Driver interface implementation.
// Open cannot be called on the iofs passthrough driver.
func (d *driver) Open(url string) (source.Driver, error) {
	return nil, errors.New("open() cannot be called on the iofs passthrough driver")
}

// PartialDriver is a helper service for creating new source drivers working with
// io/fs.FS instances. It implements all source.Driver interface methods
// except for Open(). New driver could embed this struct and add missing Open()
// method.
//
// To prepare PartialDriver for use Init() function.
type PartialDriver struct {
	migrations *source.Migrations
	fsys       fs.FS
	path       string
}

// Init prepares not initialized IoFS instance to read migrations from a
// io/fs#FS instance and a relative path.
func (d *PartialDriver) Init(fsys fs.FS, path string) error {
	entries, err := fs.ReadDir(fsys, path)
	if err != nil {
		return err
	}

	ms := source.NewMigrations()
	for _, e := range entries {
		if e.IsDir() {
			continue
		}
		m, err := source.DefaultParse(e.Name())
		if err != nil {
			continue
		}
		file, err := e.Info()
		if err != nil {
			return err
		}
		if !ms.Append(m) {
			return source.ErrDuplicateMigration{
				Migration: *m,
				FileInfo:  file,
			}
		}
	}

	d.fsys = fsys
	d.path = path
	d.migrations = ms
	return nil
}

// Close is part of source.Driver interface implementation.
// Closes the file system if possible.
func (d *PartialDriver) Close() error {
	c, ok := d.fsys.(io.Closer)
	if !ok {
		return nil
	}
	return c.Close()
}

// First is part of source.Driver interface implementation.
func (d *PartialDriver) First() (version uint, err error) {
	if version, ok := d.migrations.First(); ok {
		return version, nil
	}
	return 0, &fs.PathError{
		Op:   "first",
		Path: d.path,
		Err:  fs.ErrNotExist,
	}
}

// Prev is part of source.Driver interface implementation.
func (d *PartialDriver) Prev(version uint) (prevVersion uint, err error) {
	if version, ok := d.migrations.Prev(version); ok {
		return version, nil
	}
	return 0, &fs.PathError{
		Op:   "prev for version " + strconv.FormatUint(uint64(version), 10),
		Path: d.path,
		Err:  fs.ErrNotExist,
	}
}

// Next is part of source.Driver interface implementation.
func (d *PartialDriver) Next(version uint) (nextVersion uint, err error) {
	if version, ok := d.migrations.Next(version); ok {
		return version, nil
	}
	return 0, &fs.PathError{
		Op:   "next for version " + strconv.FormatUint(uint64(version), 10),
		Path: d.path,
		Err:  fs.ErrNotExist,
	}
}

// ReadUp is part of source.Driver interface implementation.
func (d *PartialDriver) ReadUp(version uint) (r io.ReadCloser, identifier string, err error) {
	if m, ok := d.migrations.Up(version); ok {
		body, err := d.open(path.Join(d.path, m.Raw))
		if err != nil {
			return nil, "", err
		}
		return body, m.Identifier, nil
	}
	return nil, "", &fs.PathError{
		Op:   "read up for version " + strconv.FormatUint(uint64(version), 10),
		Path: d.path,
		Err:  fs.ErrNotExist,
	}
}

// ReadDown is part of source.Driver interface implementation.
func (d *PartialDriver) ReadDown(version uint) (r io.ReadCloser, identifier string, err error) {
	if m, ok := d.migrations.Down(version); ok {
		body, err := d.open(path.Join(d.path, m.Raw))
		if err != nil {
			return nil, "", err
		}
		return body, m.Identifier, nil
	}
	return nil, "", &fs.PathError{
		Op:   "read down for version " + strconv.FormatUint(uint64(version), 10),
		Path: d.path,
		Err:  fs.ErrNotExist,
	}
}

func (d *PartialDriver) open(path string) (fs.File, error) {
	f, err := d.fsys.Open(path)
	if err == nil {
		return f, nil
	}
	// Some non-standard file systems may return errors that don't include the path, that
	// makes debugging harder.
	if !errors.As(err, new(*fs.PathError)) {
		err = &fs.PathError{
			Op:   "open",
			Path: path,
			Err:  err,
		}
	}
	return nil, err
}
```

## File: `source/iofs/iofs_test.go`
```go
//go:build go1.16

package iofs_test

import (
	"testing"

	"github.com/golang-migrate/migrate/v4/source/iofs"
	st "github.com/golang-migrate/migrate/v4/source/testing"
)

func Test(t *testing.T) {
	// reuse the embed.FS set in example_test.go
	d, err := iofs.New(fs, "testdata/migrations")
	if err != nil {
		t.Fatal(err)
	}

	st.Test(t, d)
}
```

## File: `source/iofs/README.md`
```markdown
# iofs

https://pkg.go.dev/github.com/golang-migrate/migrate/v4/source/iofs
```

## File: `source/iofs/testdata/migrations/1_foobar.down.sql`
```sql
1 down
```

## File: `source/iofs/testdata/migrations/1_foobar.up.sql`
```sql
1 up
```

## File: `source/iofs/testdata/migrations/3_foobar.up.sql`
```sql
3 up
```

## File: `source/iofs/testdata/migrations/4_foobar.down.sql`
```sql
4 down
```

## File: `source/iofs/testdata/migrations/4_foobar.up.sql`
```sql
4 up
```

## File: `source/iofs/testdata/migrations/5_foobar.down.sql`
```sql
5 down
```

## File: `source/iofs/testdata/migrations/7_foobar.down.sql`
```sql
7 down
```

## File: `source/iofs/testdata/migrations/7_foobar.up.sql`
```sql
7 up
```

## File: `source/pkger/pkger.go`
```go
package pkger

import (
	"fmt"
	"net/http"
	stdurl "net/url"

	"github.com/golang-migrate/migrate/v4/source"
	"github.com/golang-migrate/migrate/v4/source/httpfs"
	"github.com/markbates/pkger"
	"github.com/markbates/pkger/pkging"
)

func init() {
	source.Register("pkger", &Pkger{})
}

// Pkger is a source.Driver that reads migrations from instances of
// pkging.Pkger.
type Pkger struct {
	httpfs.PartialDriver
}

// Open implements source.Driver. The path component of url will be used as the
// relative location of migrations. The returned driver will use the package
// scoped pkger.Open to access migrations.  The relative root and any
// migrations must be added to the global pkger.Pkger instance by calling
// pkger.Apply. Refer to Pkger documentation for more information.
func (p *Pkger) Open(url string) (source.Driver, error) {
	u, err := stdurl.Parse(url)
	if err != nil {
		return nil, err
	}

	// wrap pkger to implement http.FileSystem.
	fs := fsFunc(func(name string) (http.File, error) {
		f, err := pkger.Open(name)
		if err != nil {
			return nil, err
		}
		return f.(http.File), nil
	})

	if err := p.Init(fs, u.Path); err != nil {
		return nil, fmt.Errorf("failed to init driver with relative path %q: %w", u.Path, err)
	}

	return p, nil
}

// WithInstance returns a source.Driver that is backed by an instance of
// pkging.Pkger. The relative location of migrations is indicated by path. The
// path must exist on the pkging.Pkger instance for the driver to initialize
// successfully.
func WithInstance(instance pkging.Pkger, path string) (source.Driver, error) {
	if instance == nil {
		return nil, fmt.Errorf("expected instance of pkging.Pkger")
	}

	// wrap pkger to implement http.FileSystem.
	fs := fsFunc(func(name string) (http.File, error) {
		f, err := instance.Open(name)
		if err != nil {
			return nil, err
		}
		return f.(http.File), nil
	})

	var p Pkger

	if err := p.Init(fs, path); err != nil {
		return nil, fmt.Errorf("failed to init driver with relative path %q: %w", path, err)
	}

	return &p, nil
}

type fsFunc func(name string) (http.File, error)

// Open implements http.FileSystem.
func (f fsFunc) Open(name string) (http.File, error) {
	return f(name)
}
```

## File: `source/pkger/pkger_test.go`
```go
package pkger

import (
	"errors"
	"os"
	"testing"

	"github.com/gobuffalo/here"
	st "github.com/golang-migrate/migrate/v4/source/testing"
	"github.com/markbates/pkger"
	"github.com/markbates/pkger/pkging"
	"github.com/markbates/pkger/pkging/mem"
)

func Test(t *testing.T) {
	t.Run("WithInstance", func(t *testing.T) {
		i := testInstance(t)

		createPkgerFile(t, i, "/1_foobar.up.sql")
		createPkgerFile(t, i, "/1_foobar.down.sql")
		createPkgerFile(t, i, "/3_foobar.up.sql")
		createPkgerFile(t, i, "/4_foobar.up.sql")
		createPkgerFile(t, i, "/4_foobar.down.sql")
		createPkgerFile(t, i, "/5_foobar.down.sql")
		createPkgerFile(t, i, "/7_foobar.up.sql")
		createPkgerFile(t, i, "/7_foobar.down.sql")

		d, err := WithInstance(i, "/")
		if err != nil {
			t.Fatal(err)
		}

		st.Test(t, d)
	})

	t.Run("Open", func(t *testing.T) {
		i := testInstance(t)

		createPkgerFile(t, i, "/1_foobar.up.sql")
		createPkgerFile(t, i, "/1_foobar.down.sql")
		createPkgerFile(t, i, "/3_foobar.up.sql")
		createPkgerFile(t, i, "/4_foobar.up.sql")
		createPkgerFile(t, i, "/4_foobar.down.sql")
		createPkgerFile(t, i, "/5_foobar.down.sql")
		createPkgerFile(t, i, "/7_foobar.up.sql")
		createPkgerFile(t, i, "/7_foobar.down.sql")

		registerPackageLevelInstance(t, i)

		d, err := (&Pkger{}).Open("pkger:///")
		if err != nil {
			t.Fatal(err)
		}

		st.Test(t, d)
	})

}

func TestWithInstance(t *testing.T) {
	t.Run("Subdir", func(t *testing.T) {
		i := testInstance(t)

		// Make sure the relative root exists so that httpfs.PartialDriver can
		// initialize.
		createPkgerSubdir(t, i, "/subdir")

		_, err := WithInstance(i, "/subdir")
		if err != nil {
			t.Fatal("")
		}
	})

	t.Run("NilInstance", func(t *testing.T) {
		_, err := WithInstance(nil, "")
		if err == nil {
			t.Fatal(err)
		}
	})

	t.Run("FailInit", func(t *testing.T) {
		i := testInstance(t)

		_, err := WithInstance(i, "/fail")
		if err == nil {
			t.Fatal(err)
		}
	})

	t.Run("FailWithoutMigrations", func(t *testing.T) {
		i := testInstance(t)

		createPkgerSubdir(t, i, "/")

		d, err := WithInstance(i, "/")
		if err != nil {
			t.Fatal(err)
		}

		if _, err := d.First(); !errors.Is(err, os.ErrNotExist) {
			t.Fatal(err)
		}

	})
}

func TestOpen(t *testing.T) {

	t.Run("InvalidURL", func(t *testing.T) {
		_, err := (&Pkger{}).Open(":///")
		if err == nil {
			t.Fatal(err)
		}
	})

	t.Run("Root", func(t *testing.T) {
		_, err := (&Pkger{}).Open("pkger:///")
		if err != nil {
			t.Fatal(err)
		}
	})

	t.Run("FailInit", func(t *testing.T) {
		_, err := (&Pkger{}).Open("pkger:///subdir")
		if err == nil {
			t.Fatal(err)
		}
	})

	i := testInstance(t)
	createPkgerSubdir(t, i, "/subdir")

	// Note that this registers the instance globally so anything run after
	// this will have access to everything container in the registered
	// instance.
	registerPackageLevelInstance(t, i)

	t.Run("Subdir", func(t *testing.T) {
		_, err := (&Pkger{}).Open("pkger:///subdir")
		if err != nil {
			t.Fatal(err)
		}
	})
}

func TestClose(t *testing.T) {
	d, err := (&Pkger{}).Open("pkger:///")
	if err != nil {
		t.Fatal(err)
	}
	if err := d.Close(); err != nil {
		t.Fatal(err)
	}
}

func registerPackageLevelInstance(t *testing.T, pkg pkging.Pkger) {
	if err := pkger.Apply(pkg, nil); err != nil {
		t.Fatalf("failed to register pkger instance: %v\n", err)
	}
}

func testInstance(t *testing.T) pkging.Pkger {
	pkg, err := inMemoryPkger()
	if err != nil {
		t.Fatalf("failed to create an  pkging.Pkger instance: %v\n", err)
	}

	return pkg
}

func createPkgerSubdir(t *testing.T, pkg pkging.Pkger, subdir string) {
	if err := pkg.MkdirAll(subdir, os.ModePerm); err != nil {
		t.Fatalf("failed to create pkger subdir %q: %v\n", subdir, err)
	}
}

func createPkgerFile(t *testing.T, pkg pkging.Pkger, name string) {
	_, err := pkg.Create(name)
	if err != nil {
		t.Fatalf("failed to create pkger file %q: %v\n", name, err)
	}
}

func inMemoryPkger() (*mem.Pkger, error) {
	info, err := here.New().Current()
	if err != nil {
		return nil, err
	}

	pkg, err := mem.New(info)
	if err != nil {
		return nil, err
	}

	return pkg, nil
}
```

## File: `source/pkger/README.md`
```markdown
# pkger
```go
package main

import (
	"errors"
	"log"

	"github.com/golang-migrate/migrate/v4"
	"github.com/markbates/pkger"

	_ "github.com/golang-migrate/migrate/v4/database/postgres"
	_ "github.com/golang-migrate/migrate/v4/source/pkger"
	_ "github.com/lib/pq"
)

func main() {
	pkger.Include("/module/path/to/migrations")
	m, err := migrate.New("pkger:///module/path/to/migrations", "postgres://postgres@localhost/postgres?sslmode=disable")
	if err != nil {
		log.Fatalln(err)
	}
	if err := m.Up(); errors.Is(err, migrate.ErrNoChange) {
		log.Println(err)
	} else if err != nil {
		log.Fatalln(err)
	}
}
```
```

## File: `source/stub/stub.go`
```go
package stub

import (
	"bytes"
	"fmt"
	"io"
	"os"

	"github.com/golang-migrate/migrate/v4/source"
)

func init() {
	source.Register("stub", &Stub{})
}

type Config struct{}

// d, _ := source.Open("stub://")
// d.(*stub.Stub).Migrations =

type Stub struct {
	Url        string
	Instance   interface{}
	Migrations *source.Migrations
	Config     *Config
}

func (s *Stub) Open(url string) (source.Driver, error) {
	return &Stub{
		Url:        url,
		Migrations: source.NewMigrations(),
		Config:     &Config{},
	}, nil
}

func WithInstance(instance interface{}, config *Config) (source.Driver, error) {
	return &Stub{
		Instance:   instance,
		Migrations: source.NewMigrations(),
		Config:     config,
	}, nil
}

func (s *Stub) Close() error {
	return nil
}

func (s *Stub) First() (version uint, err error) {
	if v, ok := s.Migrations.First(); !ok {
		return 0, &os.PathError{Op: "first", Path: s.Url, Err: os.ErrNotExist} // TODO: s.Url can be empty when called with WithInstance
	} else {
		return v, nil
	}
}

func (s *Stub) Prev(version uint) (prevVersion uint, err error) {
	if v, ok := s.Migrations.Prev(version); !ok {
		return 0, &os.PathError{Op: fmt.Sprintf("prev for version %v", version), Path: s.Url, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (s *Stub) Next(version uint) (nextVersion uint, err error) {
	if v, ok := s.Migrations.Next(version); !ok {
		return 0, &os.PathError{Op: fmt.Sprintf("next for version %v", version), Path: s.Url, Err: os.ErrNotExist}
	} else {
		return v, nil
	}
}

func (s *Stub) ReadUp(version uint) (r io.ReadCloser, identifier string, err error) {
	if m, ok := s.Migrations.Up(version); ok {
		return io.NopCloser(bytes.NewBufferString(m.Identifier)), fmt.Sprintf("%v.up.stub", version), nil
	}
	return nil, "", &os.PathError{Op: fmt.Sprintf("read up version %v", version), Path: s.Url, Err: os.ErrNotExist}
}

func (s *Stub) ReadDown(version uint) (r io.ReadCloser, identifier string, err error) {
	if m, ok := s.Migrations.Down(version); ok {
		return io.NopCloser(bytes.NewBufferString(m.Identifier)), fmt.Sprintf("%v.down.stub", version), nil
	}
	return nil, "", &os.PathError{Op: fmt.Sprintf("read down version %v", version), Path: s.Url, Err: os.ErrNotExist}
}
```

## File: `source/stub/stub_test.go`
```go
package stub

import (
	"testing"

	"github.com/golang-migrate/migrate/v4/source"
	st "github.com/golang-migrate/migrate/v4/source/testing"
)

func Test(t *testing.T) {
	s := &Stub{}
	d, err := s.Open("")
	if err != nil {
		t.Fatal(err)
	}

	m := source.NewMigrations()
	m.Append(&source.Migration{Version: 1, Direction: source.Up})
	m.Append(&source.Migration{Version: 1, Direction: source.Down})
	m.Append(&source.Migration{Version: 3, Direction: source.Up})
	m.Append(&source.Migration{Version: 4, Direction: source.Up})
	m.Append(&source.Migration{Version: 4, Direction: source.Down})
	m.Append(&source.Migration{Version: 5, Direction: source.Down})
	m.Append(&source.Migration{Version: 7, Direction: source.Up})
	m.Append(&source.Migration{Version: 7, Direction: source.Down})

	d.(*Stub).Migrations = m

	st.Test(t, d)
}
```

## File: `source/testing/testing.go`
```go
// Package testing has the source tests.
// All source drivers must pass the Test function.
// This lives in it's own package so it stays a test dependency.
package testing

import (
	"errors"
	"os"
	"testing"

	"github.com/golang-migrate/migrate/v4/source"
)

// Test runs tests against source implementations.
// It assumes that the driver tests has access to the following migrations:
//
// u = up migration, d = down migration, n = version
//
//	|  1  |  -  |  3  |  4  |  5  |  -  |  7  |
//	| u d |  -  | u   | u d |   d |  -  | u d |
//
// See source/stub/stub_test.go or source/file/file_test.go for an example.
func Test(t *testing.T, d source.Driver) {
	TestFirst(t, d)
	TestPrev(t, d)
	TestNext(t, d)
	TestReadUp(t, d)
	TestReadDown(t, d)
}

func TestFirst(t *testing.T, d source.Driver) {
	version, err := d.First()
	if err != nil {
		t.Fatalf("First: expected err to be nil, got %v", err)
	}
	if version != 1 {
		t.Errorf("First: expected 1, got %v", version)
	}
}

func TestPrev(t *testing.T, d source.Driver) {
	tt := []struct {
		version           uint
		expectErr         error
		expectPrevVersion uint
	}{
		{version: 0, expectErr: os.ErrNotExist},
		{version: 1, expectErr: os.ErrNotExist},
		{version: 2, expectErr: os.ErrNotExist},
		{version: 3, expectErr: nil, expectPrevVersion: 1},
		{version: 4, expectErr: nil, expectPrevVersion: 3},
		{version: 5, expectErr: nil, expectPrevVersion: 4},
		{version: 6, expectErr: os.ErrNotExist},
		{version: 7, expectErr: nil, expectPrevVersion: 5},
		{version: 8, expectErr: os.ErrNotExist},
		{version: 9, expectErr: os.ErrNotExist},
	}

	for i, v := range tt {
		pv, err := d.Prev(v.version)
		if (v.expectErr == os.ErrNotExist && !errors.Is(err, os.ErrNotExist)) && v.expectErr != err {
			t.Errorf("Prev: expected %v, got %v, in %v", v.expectErr, err, i)
		}
		if err == nil && v.expectPrevVersion != pv {
			t.Errorf("Prev: expected %v, got %v, in %v", v.expectPrevVersion, pv, i)
		}
	}
}

func TestNext(t *testing.T, d source.Driver) {
	tt := []struct {
		version           uint
		expectErr         error
		expectNextVersion uint
	}{
		{version: 0, expectErr: os.ErrNotExist},
		{version: 1, expectErr: nil, expectNextVersion: 3},
		{version: 2, expectErr: os.ErrNotExist},
		{version: 3, expectErr: nil, expectNextVersion: 4},
		{version: 4, expectErr: nil, expectNextVersion: 5},
		{version: 5, expectErr: nil, expectNextVersion: 7},
		{version: 6, expectErr: os.ErrNotExist},
		{version: 7, expectErr: os.ErrNotExist},
		{version: 8, expectErr: os.ErrNotExist},
		{version: 9, expectErr: os.ErrNotExist},
	}

	for i, v := range tt {
		nv, err := d.Next(v.version)
		if (v.expectErr == os.ErrNotExist && !errors.Is(err, os.ErrNotExist)) && v.expectErr != err {
			t.Errorf("Next: expected %v, got %v, in %v", v.expectErr, err, i)
		}
		if err == nil && v.expectNextVersion != nv {
			t.Errorf("Next: expected %v, got %v, in %v", v.expectNextVersion, nv, i)
		}
	}
}

func TestReadUp(t *testing.T, d source.Driver) {
	tt := []struct {
		version   uint
		expectErr error
		expectUp  bool
	}{
		{version: 0, expectErr: os.ErrNotExist},
		{version: 1, expectErr: nil, expectUp: true},
		{version: 2, expectErr: os.ErrNotExist},
		{version: 3, expectErr: nil, expectUp: true},
		{version: 4, expectErr: nil, expectUp: true},
		{version: 5, expectErr: os.ErrNotExist},
		{version: 6, expectErr: os.ErrNotExist},
		{version: 7, expectErr: nil, expectUp: true},
		{version: 8, expectErr: os.ErrNotExist},
	}

	for i, v := range tt {
		up, identifier, err := d.ReadUp(v.version)
		if (v.expectErr == os.ErrNotExist && !errors.Is(err, os.ErrNotExist)) ||
			(v.expectErr != os.ErrNotExist && err != v.expectErr) {
			t.Errorf("expected %v, got %v, in %v", v.expectErr, err, i)

		} else if err == nil {
			if len(identifier) == 0 {
				t.Errorf("expected identifier not to be empty, in %v", i)
			}

			if v.expectUp && up == nil {
				t.Errorf("expected up not to be nil, in %v", i)
			} else if !v.expectUp && up != nil {
				t.Errorf("expected up to be nil, got %v, in %v", up, i)
			}
		}
		if up != nil {
			if err := up.Close(); err != nil {
				t.Error(err)
			}
		}
	}
}

func TestReadDown(t *testing.T, d source.Driver) {
	tt := []struct {
		version    uint
		expectErr  error
		expectDown bool
	}{
		{version: 0, expectErr: os.ErrNotExist},
		{version: 1, expectErr: nil, expectDown: true},
		{version: 2, expectErr: os.ErrNotExist},
		{version: 3, expectErr: os.ErrNotExist},
		{version: 4, expectErr: nil, expectDown: true},
		{version: 5, expectErr: nil, expectDown: true},
		{version: 6, expectErr: os.ErrNotExist},
		{version: 7, expectErr: nil, expectDown: true},
		{version: 8, expectErr: os.ErrNotExist},
	}

	for i, v := range tt {
		down, identifier, err := d.ReadDown(v.version)
		if (v.expectErr == os.ErrNotExist && !errors.Is(err, os.ErrNotExist)) ||
			(v.expectErr != os.ErrNotExist && err != v.expectErr) {
			t.Errorf("expected %v, got %v, in %v", v.expectErr, err, i)

		} else if err == nil {
			if len(identifier) == 0 {
				t.Errorf("expected identifier not to be empty, in %v", i)
			}

			if v.expectDown && down == nil {
				t.Errorf("expected down not to be nil, in %v", i)
			} else if !v.expectDown && down != nil {
				t.Errorf("expected down to be nil, got %v, in %v", down, i)
			}
		}
		if down != nil {
			if err := down.Close(); err != nil {
				t.Error(err)
			}
		}
	}
}
```

## File: `testing/docker.go`
```go
// Package testing is used in driver tests and should only be used by migrate tests.
//
// Deprecated: If you'd like to test using Docker images, use package github.com/dhui/dktest instead
package testing

import (
	"bufio"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"math/rand/v2"
	"strconv"
	"strings"
	"testing"

	dockercontainer "github.com/docker/docker/api/types/container"
	dockerimage "github.com/docker/docker/api/types/image"
	dockernetwork "github.com/docker/docker/api/types/network"
	dockerclient "github.com/docker/docker/client"
)

func NewDockerContainer(t testing.TB, image string, env []string, cmd []string) (*DockerContainer, error) {
	c, err := dockerclient.NewClientWithOpts(
		dockerclient.FromEnv,
		dockerclient.WithAPIVersionNegotiation(),
	)
	if err != nil {
		return nil, err
	}

	if cmd == nil {
		cmd = make([]string, 0)
	}

	contr := &DockerContainer{
		t:         t,
		client:    c,
		ImageName: image,
		ENV:       env,
		Cmd:       cmd,
	}

	if err := contr.PullImage(); err != nil {
		return nil, err
	}

	if err := contr.Start(); err != nil {
		return nil, err
	}

	return contr, nil
}

// DockerContainer implements Instance interface
type DockerContainer struct {
	t                  testing.TB
	client             *dockerclient.Client
	ImageName          string
	ENV                []string
	Cmd                []string
	ContainerId        string
	ContainerName      string
	ContainerJSON      dockercontainer.InspectResponse
	containerInspected bool
	keepForDebugging   bool
}

func (d *DockerContainer) PullImage() (err error) {
	if d == nil {
		return errors.New("cannot pull image on a nil *DockerContainer")
	}
	d.t.Logf("Docker: Pull image %v", d.ImageName)
	r, err := d.client.ImagePull(context.Background(), d.ImageName, dockerimage.PullOptions{})
	if err != nil {
		return err
	}
	defer func() {
		if errClose := r.Close(); errClose != nil {
			err = errors.Join(err, errClose)
		}
	}()

	// read output and log relevant lines
	bf := bufio.NewScanner(r)
	for bf.Scan() {
		var resp dockerImagePullOutput
		if err := json.Unmarshal(bf.Bytes(), &resp); err != nil {
			return err
		}
		if strings.HasPrefix(resp.Status, "Status: ") {
			d.t.Logf("Docker: %v", resp.Status)
		}
	}
	return bf.Err()
}

func (d *DockerContainer) Start() error {
	if d == nil {
		return errors.New("cannot start a nil *DockerContainer")
	}

	containerName := fmt.Sprintf("migrate_test_%s", pseudoRandStr(10))

	// create container first
	resp, err := d.client.ContainerCreate(context.Background(),
		&dockercontainer.Config{
			Image:  d.ImageName,
			Labels: map[string]string{"migrate_test": "true"},
			Env:    d.ENV,
			Cmd:    d.Cmd,
		},
		&dockercontainer.HostConfig{
			PublishAllPorts: true,
		},
		&dockernetwork.NetworkingConfig{},
		nil,
		containerName)
	if err != nil {
		return err
	}

	d.ContainerId = resp.ID
	d.ContainerName = containerName

	// then start it
	if err := d.client.ContainerStart(context.Background(), resp.ID, dockercontainer.StartOptions{}); err != nil {
		return err
	}

	d.t.Logf("Docker: Started container %v (%v) for image %v listening at %v:%v", resp.ID[0:12], containerName, d.ImageName, d.Host(), d.Port())
	for _, v := range resp.Warnings {
		d.t.Logf("Docker: Warning: %v", v)
	}
	return nil
}

func (d *DockerContainer) KeepForDebugging() {
	if d == nil {
		return
	}

	d.keepForDebugging = true
}

func (d *DockerContainer) Remove() error {
	if d == nil {
		return errors.New("cannot remove a nil *DockerContainer")
	}

	if d.keepForDebugging {
		return nil
	}

	if len(d.ContainerId) == 0 {
		return errors.New("missing containerId")
	}
	if err := d.client.ContainerRemove(context.Background(), d.ContainerId,
		dockercontainer.RemoveOptions{
			Force: true,
		}); err != nil {
		d.t.Log(err)
		return err
	}
	d.t.Logf("Docker: Removed %v", d.ContainerName)
	return nil
}

func (d *DockerContainer) Inspect() error {
	if d == nil {
		return errors.New("cannot inspect a nil *DockerContainer")
	}

	if len(d.ContainerId) == 0 {
		return errors.New("missing containerId")
	}
	resp, err := d.client.ContainerInspect(context.Background(), d.ContainerId)
	if err != nil {
		return err
	}

	d.ContainerJSON = resp
	d.containerInspected = true
	return nil
}

func (d *DockerContainer) Logs() (io.ReadCloser, error) {
	if d == nil {
		return nil, errors.New("cannot view logs for a nil *DockerContainer")
	}
	if len(d.ContainerId) == 0 {
		return nil, errors.New("missing containerId")
	}

	return d.client.ContainerLogs(context.Background(), d.ContainerId, dockercontainer.LogsOptions{
		ShowStdout: true,
		ShowStderr: true,
	})
}

func (d *DockerContainer) portMapping(selectFirst bool, cPort int) (hostIP string, hostPort uint, err error) {
	if !d.containerInspected {
		if err := d.Inspect(); err != nil {
			d.t.Fatal(err)
		}
	}

	for port, bindings := range d.ContainerJSON.NetworkSettings.Ports {
		if !selectFirst && port.Int() != cPort {
			// Skip ahead until we find the port we want
			continue
		}
		if len(bindings) > 0 {
			binding := bindings[0]
			hostPortUint, err := strconv.ParseUint(binding.HostPort, 10, 64)
			if err != nil {
				return "", 0, err
			}
			return bindings[0].HostIP, uint(hostPortUint), nil
		}
	}

	if selectFirst {
		return "", 0, errors.New("no port binding")
	} else {
		return "", 0, errors.New("specified port not bound")
	}
}

func (d *DockerContainer) Host() string {
	if d == nil {
		panic("Cannot get host for a nil *DockerContainer")
	}
	hostIP, _, err := d.portMapping(true, -1)
	if err != nil {
		d.t.Fatal(err)
	}

	if hostIP == "0.0.0.0" {
		return "127.0.0.1"
	} else {
		return hostIP
	}
}

func (d *DockerContainer) Port() uint {
	if d == nil {
		panic("Cannot get port for a nil *DockerContainer")
	}
	_, port, err := d.portMapping(true, -1)
	if err != nil {
		d.t.Fatal(err)
	}
	return port
}

func (d *DockerContainer) PortFor(cPort int) uint {
	if d == nil {
		panic("Cannot get port for a nil *DockerContainer")
	}
	_, port, err := d.portMapping(false, cPort)
	if err != nil {
		d.t.Fatal(err)
	}
	return port
}

func (d *DockerContainer) NetworkSettings() dockercontainer.NetworkSettings {
	if d == nil {
		panic("Cannot get network settings for a nil *DockerContainer")
	}
	netSettings := d.ContainerJSON.NetworkSettings
	return *netSettings
}

type dockerImagePullOutput struct {
	Status          string `json:"status"`
	ProgressDetails struct {
		Current int `json:"current"`
		Total   int `json:"total"`
	} `json:"progressDetail"`
	Id       string `json:"id"`
	Progress string `json:"progress"`
}

func pseudoRandStr(n int) string {
	var letterRunes = []rune("abcdefghijklmnopqrstuvwxyz0123456789")
	b := make([]rune, n)
	for i := range b {
		b[i] = letterRunes[rand.IntN(len(letterRunes))]
	}
	return string(b)
}
```

## File: `testing/testing.go`
```go
package testing

import (
	"io"
	"os"
	"strconv"
	"testing"
	"time"

	dockercontainer "github.com/docker/docker/api/types/container"
)

type IsReadyFunc func(Instance) bool

type TestFunc func(*testing.T, Instance)

type Version struct {
	Image string
	ENV   []string
	Cmd   []string
}

func ParallelTest(t *testing.T, versions []Version, readyFn IsReadyFunc, testFn TestFunc) {
	timeout, err := strconv.Atoi(os.Getenv("MIGRATE_TEST_CONTAINER_BOOT_TIMEOUT"))
	if err != nil {
		timeout = 60 // Cassandra docker image can take ~30s to start
	}

	for i, version := range versions {
		version := version // capture range variable, see https://goo.gl/60w3p2

		// Only test against one version in short mode
		// TODO: order is random, maybe always pick first version instead?
		if i > 0 && testing.Short() {
			t.Logf("Skipping %v in short mode", version)

		} else {
			t.Run(version.Image, func(t *testing.T) {
				t.Parallel()

				// create new container
				container, err := NewDockerContainer(t, version.Image, version.ENV, version.Cmd)
				if err != nil {
					t.Fatalf("%v\n%s", err, containerLogs(t, container))
				}

				// make sure to remove container once done
				defer func() {
					if err := container.Remove(); err != nil {
						t.Error(err)
					}
				}()
				// wait until database is ready
				tick := time.NewTicker(1000 * time.Millisecond)
				defer tick.Stop()
				timeout := time.NewTimer(time.Duration(timeout) * time.Second)
				defer timeout.Stop()
			outer:
				for {
					select {
					case <-tick.C:
						if readyFn(container) {
							break outer
						}

					case <-timeout.C:
						t.Fatalf("Docker: Container not ready, timeout for %v.\n%s", version, containerLogs(t, container))
					}
				}

				// we can now run the tests
				testFn(t, container)
			})
		}
	}
}

func containerLogs(t *testing.T, c *DockerContainer) []byte {
	r, err := c.Logs()
	if err != nil {
		t.Error(err)
		return nil
	}
	defer func() {
		if err := r.Close(); err != nil {
			t.Error(err)
		}
	}()
	b, err := io.ReadAll(r)
	if err != nil {
		t.Error(err)
		return nil
	}
	return b
}

type Instance interface {
	Host() string
	Port() uint
	PortFor(int) uint
	NetworkSettings() dockercontainer.NetworkSettings
	KeepForDebugging()
}
```

## File: `testing/testing_test.go`
```go
package testing

import (
	"testing"
)

func ExampleParallelTest() {
	t := &testing.T{} // Should actually be used in a Test

	var isReady = func(i Instance) bool {
		// Return true if Instance is ready to run tests.
		// Don't block here though.
		return true
	}

	// t is *testing.T coming from parent Test(t *testing.T)
	ParallelTest(t, []Version{{Image: "docker_image:9.6"}}, isReady,
		func(t *testing.T, i Instance) {
			// Run your test/s ...
			t.Fatal("...")
		})
}
```

