---
id: github.com-vouch-vouch-proxy-02829025-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:40.788793
---

# KNOWLEDGE EXTRACT: github.com_vouch_vouch-proxy_02829025
> **Extracted on:** 2026-04-01 16:46:12
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525307/github.com_vouch_vouch-proxy_02829025

---

## File: `.defaults.yml`
```yaml
# default values for Vouch Proxy
# this is related to Env Vars
# https://github.com/vouch/vouch-proxy/issues/132
# https://github.com/vouch/vouch-proxy/pull/134

# you don't want to mess with these
vouch:
  logLevel: info
  testing: false
  listen: 0.0.0.0
  port: 9090
  socket_mode: 0660 
  # document_root:
  # domains:
  allowAllUsers: false
  publicAccess: false
  # whiteList:
  # teamWhitelist:
  writeTimeout: 15
  readTimeout: 15
  idleTimeout: 15
  tls:
    # cert:
    # key:
    profile: intermediate

  jwt:
    #   secret:
    issuer: Vouch
    maxAge: 240
    compress: true
    signing_method: HS256

  cookie:
    name: VouchCookie
    # domain:
    secure: true
    httpOnly: true
    maxAge: 240
    # sameSite:

  session:
    name: VouchSession
    maxAge: 5
    # key:

  headers:
    jwt: X-Vouch-Token
    user: X-Vouch-User
    success: X-Vouch-Success
    error: X-Vouch-Error
    querystring: access_token
    redirect: X-Vouch-Requested-URI
    # claims:
    claimheader: X-Vouch-IdP-Claims-
    # https://github.com/vouch/vouch-proxy/issues/287
    # accesstoken: X-Vouch-IdP-AccessToken
    # idtoken: X-Vouch-IdP-IdToken
  # test_url:
  # post_logout_redirect_uris:
# oauth:
#   provider:
#   client_id:
#   client_secret:
#   callback_url:
#   callback_urls:
#   preferredDomain:
#   auth_url:
#   token_url:
#   user_info_url:
#   end_session_endpoint:
#   scopes:
```

## File: `.dockerignore`
```
config/config.yml
pkg/model/storage-test.db
main
config/google_config.json
.vscode/*
lasso
config/config.yml_google
config/config.yml_github
config/secret
config/config.yml_orig
.dockerignore
Dockerfile
handlers/rice-box.go
certs
.cover/*
.github
.whitesource
```

## File: `.gitignore`
```
vouch
vouch-proxy
main
config/config.yml
config/*config.yml
config/config.yml_*
!config/config.yml_example_pocket-id
config/google_config.json
config/secret
!config/testing/*
pkg/model/storage-test.db
.vscode/*
certs/*
coverage.out
coverage.html.env_google
.env*
.cover
config/testing/rsa.key
config/testing/rsa.pub
```

## File: `.travis.yml`
```yaml
language: go
go_import_path: github.com/vouch/vouch-proxy

sudo: false

services:
  - docker

go:
  - "1.23"

env:
  - ISTRAVIS=true

before_install:
  - sudo apt-get install openssl
  - ./do.sh goget
  # - go get github.com/golang/lint/golint # Linter
  # - go get github.com/fzipp/gocyclo

script:
  # TODO: enable gofmt
  # - gofmt -w -s . && git diff --exit-code
  - ./do.sh build
  - ./do.sh test
#  - docker build -t $TRAVIS_REPO_SLUG .

#deploy:
#  - provider: script
#    skip_cleanup: true
#    script: bash .travis/docker_push
#    on:
#      go: "1.10"
#      branch: master
#  - provider: script
#    skip_cleanup: true
#    script: bash .travis/docker_push
#    on:
#      go: "1.10"
#      tags: true
#
notifications:
  irc: "irc.libera.chat#vouch"
```

## File: `.whitesource`
```
{
  "scanSettings": {
    "baseBranches": []
  },
  "checkRunSettings": {
    "vulnerableCheckRunConclusionLevel": "failure",
    "displayMode": "diff"
  },
  "issueSettings": {
    "minSeverityLevel": "LOW"
  }
}
```

## File: `AUTHORS.txt`
```
bnfinet
aaronpk
```

## File: `CHANGELOG.md`
```markdown
# Changelog for Vouch Proxy

## Unreleased

Coming soon! Please document any work in progress here as part of your PR. It will be moved to the next tag when released.

## v0.45.0

- Implement a Discord provider that uses `Username` as the username to match against in the `whiteList` config
  - Or uses `Username#Discriminator` if the Discriminator is present
  - Or uses ID if `discord_use_ids` is set

## v0.44.0

- migrate to github.com/golang-jwt/jwt/v4

## v0.43.0

- support multi-platform / multi-arch builds for published Docker images including `linux/amd64` and `linux/arm64`

## v0.42.0

- [fix auth to github](https://github.com/vouch/vouch-proxy/pull/601)
- cleanup of minor issues flagged by gostaticcheck

## v0.41.0

- upgrade golang to `v1.23` from `v1.22`

## v0.40.0

- upgrade golang to `v1.22` from `v1.18`

## v0.39.0

- [add support for listening on unix domain sockets](https://github.com/vouch/vouch-proxy/pull/488)

## v0.38.0

- upgrade golang to `v1.18` from `v1.16`

## v0.37.0

- [allow configurable Write, Read and Idle timeouts for the http server](https://github.com/vouch/vouch-proxy/pull/468)

## v0.36.0

- [run Docker containers as non-root user](https://github.com/vouch/vouch-proxy/pull/444)

Permissions may need to be adjusted for `/config/secret` and `/config/config.yml` in Docker environemnts. See the [README](https://github.com/vouch/vouch-proxy#running-from-docker)

## v0.35.1

- [include DocumentRoot if configured in error pages](https://github.com/vouch/vouch-proxy/pull/439)

## v0.35.0

- [make session.MaxAge configurable](https://github.com/vouch/vouch-proxy/issues/318) to allow more time to login at the IdP

## v0.34.2

- [log github token only at `logLevel: debug`](https://github.com/vouch/vouch-proxy/pull/436)
- documentation edits
- move `cookie.sameSite` configuration to `cookie.Configure()`

## v0.34.1

- bug fix: [Azure provider no longer requires `oauth.user_info_url` to be configured](https://github.com/vouch/vouch-proxy/issues/417)

## v0.34.0

- add support for [the "claims" Request Parameter](https://openid.net/specs/openid-connect-core-1_0.html#ClaimsParameter) to support Twitch OIDC as IdP
- add [Twitch OIDC example](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example_twitch)

## v0.33.0

- [Vouch Proxy running in a path](https://github.com/vouch/vouch-proxy/issues/373)

## v0.32.0

- [Slack oidc example](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example_slack) and [slack app manifest](https://github.com/vouch/vouch-proxy/blob/master/examples/slack/vouch-slack-oidc-app-manifest.yml)
- [CHANGELOG.md](https://github.com/vouch/vouch-proxy/blob/master/CHANGELOG.md)

## v0.31.0

- [use quay.io](https://quay.io/repository/vouch/vouch-proxy?tab=tags) instead of Docker Hub for docker image hosting
- use [httprouter's](https://github.com/julienschmidt/httprouter) more performant mux

## v0.29.0

- embed static assets as templates using [go:embed](https://golang.org/pkg/embed/)

## v0.28.0

- add support for a custom 'relying party identifier' for ADFS

_the rest is history_ and can be teased out with `git log`
```

## File: `CONTRIBUTING.md`
```markdown
# Setting up a Development Environment

## Running Tests 

```bash
 export VOUCH_ROOT=`pwd` # if not using GOPATH
 ./do.sh test
```

After running these tests manually once (which creates a test key pair), it is possible to run the tests with VSCode Test Explorer.

To get it to work, we must set some environment variables in `.vscode/settings.json` which otherwise would be set by `do.sh`:

```json
{
    "go.testEnvVars": {
        "VOUCH_ROOT": "${workspaceFolder}",
        "VOUCH_CONFIG": "${workspaceFolder}/config/testing/test_config.yml",
        "TEST_PRIVATE_KEY_FILE": "${workspaceFolder}/config/testing/rsa.key",
        "TEST_PUBLIC_KEY_FILE": "${workspaceFolder}/config/testing/rsa.pub",
    }
}
```

### Contributing to Vouch Proxy by submitting a Pull Request

**_I really love Vouch Proxy! I wish it did XXXX..._**

That's really wonderful and contributions are greatly appreciated. However, please search through the existing issues, both open and closed, to look for any prior work or conversation. Then please make a proposal before we all spend valuable time considering and integrating a new feature.

Code contributions should..

- generally be discussed beforehand in a GitHub issue
- include unit tests and in some cases end-to-end tests
- be formatted with `go fmt`, checked with `go vet` and other common go tools
- accomodate configuration via `config.yml` as well as `ENVIRONMENT_VARIABLEs`.
- not break existing setups without a clear reason (usually security related)
- include an entry at the top of CHANGELOG.md in the **Unreleased** section

For larger contributions or code related to a platform that we don't currently support we will ask you to commit to supporting the feature for an agreed upon period. Invariably someone will pop up here with a question and we want to be able to support these requests.

**Thank you to all of the contributors that have provided their time and effort and thought to improving VP.**
```

## File: `Dockerfile`
```
# quay.io/vouch/vouch-proxy
# https://github.com/vouch/vouch-proxy
FROM golang:1.23 AS builder

ARG UID=999
ARG GID=999
LABEL maintainer="vouch@bnf.net"

RUN mkdir -p ${GOPATH}/src/github.com/vouch/vouch-proxy
WORKDIR ${GOPATH}/src/github.com/vouch/vouch-proxy

RUN groupadd -g $GID vouch \
    && useradd --system vouch --uid=$UID --gid=$GID

COPY . .


RUN ./do.sh goget
RUN ./do.sh gobuildstatic # see `do.sh` for vouch-proxy build details
RUN ./do.sh install

FROM scratch
LABEL maintainer="vouch@bnf.net"
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY --from=builder /go/bin/vouch-proxy /vouch-proxy

USER vouch

EXPOSE 9090
ENTRYPOINT ["/vouch-proxy"]
HEALTHCHECK --interval=1m --timeout=5s CMD [ "/vouch-proxy", "-healthcheck" ]
```

## File: `Dockerfile.alpine`
```
# quay.io/vouch/vouch-proxy
# https://github.com/vouch/vouch-proxy
FROM golang:1.23 AS builder

ARG UID=999
ARG GID=999
LABEL maintainer="vouch@bnf.net"

RUN mkdir -p ${GOPATH}/src/github.com/vouch/vouch-proxy
WORKDIR ${GOPATH}/src/github.com/vouch/vouch-proxy

COPY . .

RUN ./do.sh goget
RUN ./do.sh gobuildstatic # see `do.sh` for vouch-proxy build details
RUN ./do.sh install

RUN groupadd -g $GID vouch \
    && useradd --system vouch --uid=$UID --gid=$GID

FROM alpine:latest
LABEL maintainer="vouch@bnf.net"
ENV VOUCH_ROOT=/
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

#  do.sh requires bash
RUN apk add --no-cache bash
COPY do.sh /do.sh

COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY --from=builder /go/bin/vouch-proxy /vouch-proxy

USER vouch

EXPOSE 9090
ENTRYPOINT ["/vouch-proxy"]
HEALTHCHECK --interval=1m --timeout=5s CMD [ "/vouch-proxy", "-healthcheck" ]
```

## File: `LICENSE`
```
The MIT License (MIT)

Copyright (c) 2017 The Vouch Proxy Authors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
# Vouch Proxy

[![GitHub stars](https://img.shields.io/github/stars/vouch/vouch-proxy.svg)](https://github.com/vouch/vouch-proxy)
[![Build Status](https://travis-ci.org/vouch/vouch-proxy.svg?branch=master)](https://travis-ci.org/vouch/vouch-proxy)
[![Go Report Card](https://goreportcard.com/badge/github.com/vouch/vouch-proxy)](https://goreportcard.com/report/github.com/vouch/vouch-proxy)
[![MIT license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/vouch/vouch-proxy/blob/master/LICENSE)
[![GitHub version](https://img.shields.io/github/v/tag/vouch/vouch-proxy.svg?sort=semver&color=green)](https://github.com/vouch/vouch-proxy)

An SSO solution for Nginx using the [auth_request](http://nginx.org/en/docs/http/ngx_http_auth_request_module.html) module. Vouch Proxy can protect all of your websites at once.

Vouch Proxy supports many OAuth and OIDC login providers and can enforce authentication to...

- [Google](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example_google)
- [GitHub](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example_github)
- [GitHub Enterprise](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example_github_enterprise)
- [IndieAuth](https://indieauth.spec.indieweb.org/)
- [Okta](https://developer.okta.com/blog/2018/08/28/nginx-auth-request)
- [Slack](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example_slack)
- [ADFS](https://github.com/vouch/vouch-proxy/pull/68)
- [Azure AD](https://github.com/vouch/vouch-proxy/issues/290)
- [Alibaba / Aliyun iDaas](https://github.com/vouch/vouch-proxy/issues/344)
- [AWS Cognito](https://github.com/vouch/vouch-proxy/issues/105)
- [Twitch](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example_twitch)
- [Discord](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example_discord)
- [SecureAuth](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example_secureauth)
- [Gitea](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example_gitea)
- [Keycloak](config/config.yml_example_keycloak)
- [OAuth2 Server Library for PHP](https://github.com/vouch/vouch-proxy/issues/99)
- [HomeAssistant](https://developers.home-assistant.io/docs/en/auth_api.html)
- [OpenStax](https://github.com/vouch/vouch-proxy/pull/141)
- [Ory Hydra](https://github.com/vouch/vouch-proxy/issues/288)
- [Nextcloud](https://docs.nextcloud.com/server/latest/admin_manual/configuration_server/oauth2.html)
- [Pocket ID](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example_pocket-id)
- most other OpenID Connect (OIDC) providers

Please do let us know when you have deployed Vouch Proxy with your preffered IdP or library so we can update the list.

If Vouch is running on the same host as the Nginx reverse proxy the response time from the `/validate` endpoint to Nginx should be **less than 1ms**.

---

## Table of Contents

- [What Vouch Proxy Does...](#what-vouch-proxy-does)
- [Installation and Configuration](#installation-and-configuration)
  - [Vouch Proxy "in a path"](#vouch-proxy-in-a-path)
  - [Additional Nginx Configurations](#additional-nginx-configurations)
  - [Configuration via Environmental Variables](#configuring-via-environmental-variables)
- [Tips, Tricks and Advanced Configurations](#tips-tricks-and-advanced-configurations)
  - [Scopes and Claims](#scopes-and-claims)
- [Running from Docker](#running-from-docker)
- [Kubernetes Nginx Ingress](#kubernetes-nginx-ingress)
- [Compiling from source and running the binary](#compiling-from-source-and-running-the-binary)
- [/login and /logout endpoint redirection](#login-and-logout-endpoint-redirection)
- [Troubleshooting, Support and Feature Requests](#troubleshooting-support-and-feature-requests-read-this-before-submitting-an-issue-at-github)
  (Read this before submitting an issue at GitHub)
  - [I'm getting an infinite redirect loop which returns me to my IdP (Google/Okta/GitHub/...)](#im-getting-an-infinite-redirect-loop-which-returns-me-to-my-idp-googleoktagithub)
  - [Okay, I looked at the issues and have tried some things with my configs but it's still not working](#okay-i-looked-at-the-issues-and-have-tried-some-things-with-my-configs-but-its-still-not-working)
  - [Contributing to Vouch Proxy](#contributing)
- [Advanced Authorization Using OpenResty](#advanced-authorization-using-openresty)
- [The flow of login and authentication using Google Oauth](#the-flow-of-login-and-authentication-using-google-oauth)

## What Vouch Proxy Does

Vouch Proxy (VP) forces visitors to login and authenticate with an [IdP](https://en.wikipedia.org/wiki/Identity_provider) (such as one of the services listed above) before allowing them access to a website.

![Vouch Proxy protects websites](https://github.com/vouch/vouch-proxy/blob/master/examples/nginx-vouch-private_simple.png?raw=true)

VP can also be used as a Single Sign On (SSO) solution to protect all web applications in the same domain.

![Vouch Proxy is a Single Sign On solution](https://github.com/vouch/vouch-proxy/blob/master/examples/nginx-vouch-private_appA_appB_appC.png?raw=true)

After a visitor logs in Vouch Proxy allows access to the protected websites for several hours. Every request is checked by VP to ensure that it is valid.

VP can send the visitor's email, name and other information which the IdP provides (including access tokens) to the web application as HTTP headers. VP can be used to replace application user management entirely.

## Installation and Configuration

Vouch Proxy relies on the ability to share a cookie between the Vouch Proxy server and the application it's protecting. Typically this will be done by running Vouch on a subdomain such as `vouch.yourdomain.com` with apps running at `app1.yourdomain.com` and `app2.yourdomain.com`. The protected domain is `.yourdomain.com` and the Vouch Proxy cookie must be set in this domain by setting [vouch.domains](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example#L38-L48) to include `yourdomain.com` or sometimes by setting [vouch.cookie.domain](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example#L109-L114) to `yourdomain.com`.

- `cp ./config/config.yml_example_$OAUTH_PROVIDER ./config/config.yml`
- create OAuth credentials for Vouch Proxy at [google](https://console.developers.google.com/apis/credentials) or [github](https://developer.github.com/apps/building-integrations/setting-up-and-registering-oauth-apps/about-authorization-options-for-oauth-apps/), etc
  - be sure to direct the callback URL to the Vouch Proxy `/auth` endpoint
- configure Nginx...

The following Nginx config assumes..

- Nginx, `vouch.yourdomain.com` and `protectedapp.yourdomain.com` are running on the same server
- both domains are served as `https` and have valid certs (if not, change to `listen 80` and set [vouch.cookie.secure](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example#L84-L85) to `false`)

```nginx
server {
    listen 443 ssl http2;
    server_name protectedapp.yourdomain.com;
    root /var/www/html/;

    ssl_certificate /etc/letsencrypt/live/protectedapp.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/protectedapp.yourdomain.com/privkey.pem;

    # send all requests to the `/validate` endpoint for authorization
    auth_request /validate;

    location = /validate {
      # forward the /validate request to Vouch Proxy
      proxy_pass http://127.0.0.1:9090/validate;
      # be sure to pass the original host header
      proxy_set_header Host $http_host;

      # Vouch Proxy only acts on the request headers
      proxy_pass_request_body off;
      proxy_set_header Content-Length "";

      # optionally add X-Vouch-User as returned by Vouch Proxy along with the request
      auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;

      # optionally add X-Vouch-IdP-Claims-* custom claims you are tracking
      #    auth_request_set $auth_resp_x_vouch_idp_claims_groups $upstream_http_x_vouch_idp_claims_groups;
      #    auth_request_set $auth_resp_x_vouch_idp_claims_given_name $upstream_http_x_vouch_idp_claims_given_name;
      # optinally add X-Vouch-IdP-AccessToken or X-Vouch-IdP-IdToken
      #    auth_request_set $auth_resp_x_vouch_idp_accesstoken $upstream_http_x_vouch_idp_accesstoken;
      #    auth_request_set $auth_resp_x_vouch_idp_idtoken $upstream_http_x_vouch_idp_idtoken;

      # these return values are used by the @error401 call
      auth_request_set $auth_resp_jwt $upstream_http_x_vouch_jwt;
      auth_request_set $auth_resp_err $upstream_http_x_vouch_err;
      auth_request_set $auth_resp_failcount $upstream_http_x_vouch_failcount;

      # Vouch Proxy can run behind the same Nginx reverse proxy
      # may need to comply to "upstream" server naming
      # proxy_pass http://vouch.yourdomain.com/validate;
      # proxy_set_header Host $http_host;
    }

    # if validate returns `401 not authorized` then forward the request to the error401block
    error_page 401 = @error401;

    location @error401 {
        # redirect to Vouch Proxy for login
        return 302 https://vouch.yourdomain.com/login?url=$scheme://$http_host$request_uri&vouch-failcount=$auth_resp_failcount&X-Vouch-Token=$auth_resp_jwt&error=$auth_resp_err;
        # you usually *want* to redirect to Vouch running behind the same Nginx config proteced by https
        # but to get started you can just forward the end user to the port that vouch is running on
        # return 302 http://vouch.yourdomain.com:9090/login?url=$scheme://$http_host$request_uri&vouch-failcount=$auth_resp_failcount&X-Vouch-Token=$auth_resp_jwt&error=$auth_resp_err;
    }

    location / {
      # forward authorized requests to your service protectedapp.yourdomain.com
      proxy_pass http://127.0.0.1:8080;
      # you may need to set these variables in this block as per https://github.com/vouch/vouch-proxy/issues/26#issuecomment-425215810
      #    auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;
      #    auth_request_set $auth_resp_x_vouch_idp_claims_groups $upstream_http_x_vouch_idp_claims_groups;
      #    auth_request_set $auth_resp_x_vouch_idp_claims_given_name $upstream_http_x_vouch_idp_claims_given_name;

      # set user header (usually an email)
      proxy_set_header X-Vouch-User $auth_resp_x_vouch_user;
      # optionally pass any custom claims you are tracking
      #     proxy_set_header X-Vouch-IdP-Claims-Groups $auth_resp_x_vouch_idp_claims_groups;
      #     proxy_set_header X-Vouch-IdP-Claims-Given_Name $auth_resp_x_vouch_idp_claims_given_name;
      # optionally pass the accesstoken or idtoken
      #     proxy_set_header X-Vouch-IdP-AccessToken $auth_resp_x_vouch_idp_accesstoken;
      #     proxy_set_header X-Vouch-IdP-IdToken $auth_resp_x_vouch_idp_idtoken;
    }
}

```

If Vouch is configured behind the **same** nginx reverseproxy ([perhaps so you can configure ssl](https://github.com/vouch/vouch-proxy/issues/64#issuecomment-461085139)) be sure to pass the `Host` header properly, otherwise the JWT cookie cannot be set into the domain

```nginx
server {
    listen 443 ssl http2;
    server_name vouch.yourdomain.com;
    ssl_certificate /etc/letsencrypt/live/vouch.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/vouch.yourdomain.com/privkey.pem;

    location / {
      proxy_pass http://127.0.0.1:9090;
      # be sure to pass the original host header
      proxy_set_header Host $http_host;
    }
}
```

### Vouch Proxy "in a path"

As of `v0.33.0` Vouch Proxy can be served within an Nginx location (path) by configuring `vouch.document_root: /vp_in_a_path`

This avoids the need to setup a separate domain for Vouch Proxy such as `vouch.yourdomain.com`. For example VP login will be served from `https://protectedapp.yourdomain.com/vp_in_a_path/login`

```nginx
server {
    listen 443 ssl http2;
    server_name protectedapp.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/protectedapp.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/protectedapp.yourdomain.com/privkey.pem;

    # This location serves all Vouch Proxy endpoints as /vp_in_a_path/$uri
    #   including /vp_in_a_path/validate, /vp_in_a_path/login, /vp_in_a_path/logout, /vp_in_a_path/auth, /vp_in_a_path/auth/$STATE, etc
    location /vp_in_a_path {
      proxy_pass http://127.0.0.1:9090; # must not! have a slash at the end
      proxy_set_header Host $http_host;
      proxy_pass_request_body off;
      proxy_set_header Content-Length "";

      # these return values are used by the @error401 call
      auth_request_set $auth_resp_jwt $upstream_http_x_vouch_jwt;
      auth_request_set $auth_resp_err $upstream_http_x_vouch_err;
      auth_request_set $auth_resp_failcount $upstream_http_x_vouch_failcount;
    }

    # if /vp_in_a_path/validate returns `401 not authorized` then forward the request to the error401block
    error_page 401 = @error401;

    location @error401 {
        # redirect to Vouch Proxy for login
        return 302 https://protectedapp.yourdomain.com/vp_in_a_path/login?url=$scheme://$http_host$request_uri&vouch-failcount=$auth_resp_failcount&X-Vouch-Token=$auth_resp_jwt&error=$auth_resp_err;
    }

    location / {
      auth_request /vp_in_a_path/validate;
      proxy_pass http://127.0.0.1:8080;
      # see the Nginx config above for additional headers which can be set from Vouch Proxy
    }
}
```

### Additional Nginx Configurations

Additional Nginx configurations can be found in the [examples](https://github.com/vouch/vouch-proxy/tree/master/examples) directory.

### Configuring via Environmental Variables

Here's a minimal setup using Google's OAuth...

```bash
VOUCH_DOMAINS=yourdomain.com \
  OAUTH_PROVIDER=google \
  OAUTH_CLIENT_ID=1234 \
  OAUTH_CLIENT_SECRET=secretsecret \
  OAUTH_CALLBACK_URL=https://vouch.yourdomain.com/auth \
  ./vouch-proxy
```

Environmental variable names are documented in [config/config.yml_example](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example)

All lists with multiple values must be comma separated: `VOUCH_DOMAINS="yourdomain.com,yourotherdomain.com"`

The variable `VOUCH_CONFIG` can be used to set an alternate location for the configuration file. `VOUCH_ROOT` can be used to set an alternate root directory for Vouch Proxy to look for support files.

## Tips, Tricks and Advanced Configurations

All Vouch Proxy configuration items are documented in [config/config.yml_example](https://github.com/vouch/vouch-proxy/blob/master/config/config.yml_example)

- [Cacheing of the Vouch Proxy `/validate` response in Nginx](https://github.com/vouch/vouch-proxy/issues/76#issuecomment-464028743)
- [Handling `OPTIONS` requests when protecting an API with Vouch Proxy](https://github.com/vouch/vouch-proxy/issues/216)
- [Validation by GitHub Team or GitHub Org](https://github.com/vouch/vouch-proxy/pull/205)
- [Running VP on a Raspberry Pi using the ARM based Docker image](https://github.com/vouch/vouch-proxy/pull/247)
- [Kubernetes architecture post ingress](https://github.com/vouch/vouch-proxy/pull/263#issuecomment-628297832)
- [set `HTTP_PROXY` to relay Vouch Proxy IdP requests through an outbound proxy server](https://github.com/vouch/vouch-proxy/issues/291)
- [Reverse Proxy for Google Cloud Run Services](https://github.com/karthikv2k/oauth_reverse_proxy)
- [Enable native TLS in Vouch Proxy](https://github.com/vouch/vouch-proxy/pull/332#issue-522612010)
- [FreeBSD support](https://github.com/vouch/vouch-proxy/issues/368)
- [`systemd` startup of Vouch Proxy](https://github.com/vouch/vouch-proxy/tree/master/examples/startup)
- [Using Node.js instead of Nginx to route requests](https://github.com/vouch/vouch-proxy/issues/359)
- [Developing a Single Page App (SPA) while consuming a VP protected API](https://github.com/vouch/vouch-proxy/issues/416)
- [Integrate Vouch Proxy into a server side application for User Authn and Authz](https://github.com/vouch/vouch-proxy/issues/421)
- [Filter by IP address before VP validation by using `satisfy any;`](https://github.com/vouch/vouch-proxy/issues/378#issuecomment-814423460)

Please do help us to expand this list.

### Scopes and Claims

With Vouch Proxy you can request various `scopes` (standard and custom) to obtain more information about the user or gain access to the provider's APIs. Internally, Vouch Proxy launches a requests to `user_info_url` after successful authentication. The required `claims` are extracted from the provider's response and stored in the VP cookie.

⚠️ **Additional claims and tokens will be added to the VP cookie and can make it large**

The VP cookie may be split into several cookies to accomdate browser cookie size limits. But if you need it, you need it. Large cookies and headers require Nginx to be configured with larger buffers. See [large_client_header_buffers](http://nginx.org/en/docs/http/ngx_http_core_module.html#large_client_header_buffers) and [proxy_buffer_size](http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_buffer_size) for more information.

#### Setup `scopes` and `claims` in Vouch Proxy with Nginx

0. Configure Vouch Proxy for Nginx and your IdP as normal (See: [Installation and Configuration](#installation-and-configuration))

1. Set the necessary `scope`s in the `oauth` section of the vouch-proxy `config.yml` ([example config](config/config.yml_example_scopes_and_claims))
   1. set `idtoken: X-Vouch-IdP-IdToken` in the `headers` section of vouch-proxy's `config.yml`
   2. log in and call the `/validate` endpoint in a modern browser
   3. check the response header for a `X-Vouch-IdP-IdToken` header
   4. copy the value of the header into the debugger at [https://jwt.io/](https://jwt.io/) and ensure that the necessary claims are part of the jwt
   5. if they are not, you need to adjust the `scopes` in the `oauth` section of your `config.yml` or reconfigure your oauth provider
2. Set the necessary `claims` in the `header` section of the vouch-proxy `config.yml`
   1. log in and call the `/validate` endpoint in a modern browser
   2. check the response headers for headers of the form `X-Vouch-IdP-Claims-<ClaimName>`
   3. If they are not there clear your cookies and cached browser data
   4. 🐞 If they are still not there but exist in the jwt (esp. custom claims) there might be a bug
   5. remove the `idtoken: X-Vouch-IdP-IdToken` from the `headers` section of vouch-proxy's `config.yml` if you don't need it
3. Use `auth_request_set` after `auth_request` inside the protected location in the nginx [`server.conf`](examples/nginx/nginx_scopes_and_claims.conf)
4. Consume the claim ([example nginx config](examples/nginx/nginx_scopes_and_claims.conf))

## Running from Docker

```bash
docker run -d \
    -p 9090:9090 \
    --name vouch-proxy \
    -v ${PWD}/config:/config \
    quay.io/vouch/vouch-proxy
```

or

```bash
docker run -d \
    -p 9090:9090 \
    --name vouch-proxy \
    -e VOUCH_DOMAINS=yourdomain.com \
    -e OAUTH_PROVIDER=google \
    -e OAUTH_CLIENT_ID=1234 \
    -e OAUTH_CLIENT_SECRET=secretsecret \
    -e OAUTH_CALLBACK_URL=https://vouch.yourdomain.com/auth \
    quay.io/vouch/vouch-proxy
```

As of `v0.36.0` the docker process in the container runs as user `vouch` with UID 999 and GID 999. You may need to set the permissions of `/config/config.yml` and `/config/secret` to correspond to be readable by this user, or otherwise use `docker run --user $UID:$GID ...` or perhaps build the docker container from source and use the available ARGs for UID and GID.

Automated container builds for each Vouch Proxy release are available from [quay.io](https://quay.io/repository/vouch/vouch-proxy). Each release produces..

a minimal go binary container built from `Dockerfile`

- `quay.io/vouch/vouch-proxy:latest`
- `quay.io/vouch/vouch-proxy:x.y.z` such as `quay.io/vouch/vouch-proxy:0.28.0`

an `alpine` based container built from `Dockerfile.alpine`

- `quay.io/vouch/vouch-proxy:alpine-latest`
- `quay.io/vouch/vouch-proxy:alpine-x.y.z`

As of `v0.43.0` both of these images are [Multi-platform builds](https://docs.docker.com/build/building/multi-platform/) supporting `linux/amd64` and `linux/arm64`.

Vouch Proxy `arm` images are available on [Docker Hub](https://hub.docker.com/r/voucher/vouch-proxy/)

- `voucher/vouch-proxy:latest-arm`

## Kubernetes Nginx Ingress

If you are using kubernetes with [nginx-ingress](https://github.com/kubernetes/ingress-nginx), you can configure your ingress with the following annotations (note quoting the `auth-signin` annotation):

```bash
    nginx.ingress.kubernetes.io/auth-signin: "https://vouch.yourdomain.com/login?url=$scheme://$http_host$request_uri&vouch-failcount=$auth_resp_failcount&X-Vouch-Token=$auth_resp_jwt&error=$auth_resp_err"
    nginx.ingress.kubernetes.io/auth-url: https://vouch.yourdomain.com/validate
    nginx.ingress.kubernetes.io/auth-response-headers: X-Vouch-User
    nginx.ingress.kubernetes.io/auth-snippet: |
      # these return values are used by the @error401 call
      auth_request_set $auth_resp_jwt $upstream_http_x_vouch_jwt;
      auth_request_set $auth_resp_err $upstream_http_x_vouch_err;
      auth_request_set $auth_resp_failcount $upstream_http_x_vouch_failcount;
      # when VP is hosted externally to k8s ensure the SSL cert is valid to avoid MITM risk
      # proxy_ssl_trusted_certificate /etc/ssl/certs/ca-certificates.crt;
      # proxy_ssl_session_reuse on;
      # proxy_ssl_verify_depth 2;
      # proxy_ssl_verify on;
```

Helm Charts are maintained by [punkle](https://github.com/punkle), [martina-if](https://github.com/martina-if) and [halkeye](https://github.com/halkeye) and are available at [https://github.com/vouch/helm-charts](https://github.com/vouch/helm-charts)

## Compiling from source and running the binary

```bash
  ./do.sh goget
  ./do.sh build
  ./vouch-proxy
```

As of `v0.29.0` all templates, static assets and configuration defaults in `.defaults.yml` are built into the static binary using [go:embed](https://pkg.go.dev/embed) directives.

## /login and /logout endpoint redirection

As of `v0.11.0` additional checks are in place to reduce [the attack surface of url redirection](https://blog.detectify.com/2019/05/16/the-real-impact-of-an-open-redirect/).

### /login?url=POST_LOGIN_URL

The passed URL...

- must start with either `http` or `https`
- must have a domain overlap with either a domain in the `vouch.domains` list or the `vouch.cookie.domain` (if either of those are configured)
- cannot have a parameter which includes a URL to [prevent URL chaining attacks](https://hackerone.com/reports/202781)

### /logout?url=NEXT_URL

The Vouch Proxy `/logout` endpoint accepts a `url` parameter in the query string which can be used to `302` redirect a user to your orignal OAuth provider/IDP/OIDC provider's [revocation_endpoint](https://tools.ietf.org/html/rfc7009)

```bash
    https://vouch.oursites.com/logout?url=https://oauth2.googleapis.com/revoke
```

this url must be present in the configuration file on the list `vouch.post_logout_redirect_uris`

```yaml
# in order to prevent redirection attacks all redirected URLs to /logout must be specified
# the URL must still be passed to Vouch Proxy as https://vouch.yourdomain.com/logout?url=${ONE OF THE URLS BELOW}
post_logout_redirect_uris:
  # your apps login page
  - https://yourdomain.com/login
  # your IdPs logout enpoint
  # from https://accounts.google.com/.well-known/openid-configuration
  - https://oauth2.googleapis.com/revoke
  # you may be daisy chaining to your IdP
  - https://myorg.okta.com/oauth2/123serverid/v1/logout?post_logout_redirect_uri=http://myapp.yourdomain.com/login
```

Note that your IdP will likely carry their own, separate `post_logout_redirect_uri` list.

logout resources..

- [Google](https://developers.google.com/identity/protocols/OAuth2WebServer#tokenrevoke)
- [Okta](https://developer.okta.com/docs/api/resources/oidc#logout)
- [Auth0](https://auth0.com/docs/logout/guides/logout-idps)

## Troubleshooting, Support and Feature Requests (Read this before submitting an issue at GitHub)

Getting the stars to align between Nginx, Vouch Proxy and your IdP can be tricky. We want to help you get up and running as quickly as possible. The most common problem is..

### I'm getting an infinite redirect loop which returns me to my IdP (Google/Okta/GitHub/...)

Double check that you are running Vouch Proxy and your apps on a common domain that can share cookies. For example, `vouch.yourdomain.com` and `app.yourdomain.com` can share cookies on the `.yourdomain.com` domain. (It will not work if you are trying to use `vouch.yourdomain.org` and `app.yourdomain.net`.)

You may need to explicitly define the domain that the cookie should be set on. You can do this in the config file by setting the option:

```yaml
vouch:
  cookie:
    # force the domain of the cookie to set
    domain: yourdomain.com
```

If you continue to have trouble, try the following:

- **turn on `vouch.testing: true`**. This will slow down the loop.
- set `vouch.logLevel: debug`.
- the `Host:` header in the http request, the `oauth.callback_url` and the configured `vouch.domains` must all align so that the cookie that carries the JWT can be placed properly into the browser and then returned on each request
- it helps to **_think like a cookie_**.

  - a cookie is set into a domain. If you have `siteA.yourdomain.com` and `siteB.yourdomain.com` protected by Vouch Proxy, you want the Vouch Proxy cookie to be set into `.yourdomain.com`
  - if you authenticate to `vouch.yourdomain.com` the cookie will not be able to be seen by `dev.anythingelse.com`
  - unless you are using https, you should set `vouch.cookie.secure: false`
  - cookies **are** available to all ports of a domain

- please see the [issues which have been closed that mention redirect](https://github.com/vouch/vouch-proxy/issues?utf8=%E2%9C%93&q=is%3Aissue+redirect+)

### Okay, I looked at the issues and have tried some things with my configs but it's still not working

Please [submit a new issue](https://github.com/vouch/vouch-proxy/issues) in the following fashion..

TLDR:

- set `vouch.testing: true`
- set `vouch.logLevel: debug`
- conduct two full round trips of `./vouch-proxy` capturing the output..
  - VP startup
  - `/validate`
  - `/login` - even if the error is here
  - `/auth`
  - `/validate` - capture everything
- put all your logs and config in a `gist`.
- `./do.sh bug_report` is your friend

#### But read this anyways because we'll ask you to read it if you don't follow these instruction. :)

- **turn on `vouch.testing: true`** and set `vouch.logLevel: debug`.
- use a [gist](https://gist.github.com/) or another **paste service** such as [hasteb.in](https://hasteb.in/). **_DO NOT PUT YOUR LOGS AND CONFIG INTO THE GITHUB ISSUE_**. Using a paste service is important as it will maintain spacing and will provide line numbers and formatting. We are hunting for needles in haystacks with setups with several moving parts, these features help considerably. Paste services save your time and our time and help us to help you quickly. You're more likely to get good support from us in a timely manner by following this advice.
- run `./do.sh bug_report secretdomain.com secretpass [anothersecret..]` which will create a redacted version of your config and logs removing each of those strings
  - and follow the instructions at the end to redact your Nginx config
- all of those go into a [gist](https://gist.github.com/)
- then [open a new issue](https://github.com/vouch/vouch-proxy/issues/new) in this repository

A bug report can be generated from a docker environment using the `quay.io/vouch/vouch-proxy:alpine` image...

```!bash
docker run --name vouch_proxy -v $PWD/config:/config -v $PWD/certs:/certs -it --rm --entrypoint /do.sh quay.io/vouch/vouch-proxy:alpine bug_report yourdomain.com anotherdomain.com someothersecret
```

### Contributing

We'd love to have you contribute! Please refer to our [contribution guidelines](https://github.com/vouch/vouch-proxy/blob/master/CONTRIBUTING.md) for details.

## Advanced Authorization Using OpenResty

OpenResty® is a full-fledged web platform that integrates the standard Nginx core, LuaJIT, many carefully written Lua libraries, lots of high quality 3rd-party Nginx modules, and most of their external dependencies.

You can replace nginx with [OpenResty](https://openresty.org/en/installation.html) fairly easily.

With OpenResty and Lua it is possible to provide customized and advanced authorization on any header or claims vouch passes down.

OpenResty and configs for a variety of scenarios are available in the [examples](https://github.com/vouch/vouch-proxy/tree/master/examples) directory.

## The flow of login and authentication using Google Oauth

- Bob visits `https://private.oursites.com`
- the Nginx reverse proxy...

  - recieves the request for private.oursites.com from Bob
  - uses the `auth_request` module configured for the `/validate` path
  - `/validate` is configured to `proxy_pass` requests to the authentication service at `https://vouch.oursites.com/validate`
    - if `/validate` returns...
      - 200 OK then SUCCESS allow Bob through
      - 401 NotAuthorized then
        - respond to Bob with a 302 redirect to `https://vouch.oursites.com/login?url=https://private.oursites.com`

- Vouch Proxy `https://vouch.oursites.com/validate`

  - recieves the request for private.oursites.com from Bob via Nginx `proxy_pass`
  - looks for a cookie named "oursitesSSO" that contains a JWT
  - if the cookie is found, and the JWT is valid
    - returns `200 OK` to Nginx, which will allow access (bob notices nothing)
  - if the cookie is NOT found, or the JWT is NOT valid
    - return `401 NotAuthorized` to Nginx (which forwards the request on to login)

- Bob is first forwarded briefly to `https://vouch.oursites.com/login?url=https://private.oursites.com`

  - clears out the cookie named "oursitesSSO" if it exists
  - generates a nonce and stores it in session variable \$STATE
  - stores the url `https://private.oursites.com` from the query string in session variable `$requestedURL`
  - respond to Bob with a 302 redirect to Google's OAuth Login form, including the `$STATE` nonce

- Bob logs into his Google account using Oauth

  - after successful login
  - Google responds to Bob with a 302 redirect to `https://vouch.oursites.com/auth?state=$STATE`

- Bob is forwarded to `https://vouch.oursites.com/auth?state=$STATE`
  - if the \$STATE nonce from the url matches the session variable "state"
  - make a "third leg" request of Google (server to server) to exchange the OAuth code for Bob's user info including email address bob@oursites.com
  - if the email address matches the domain oursites.com (it does)
    - issue bob a JWT in the form of a cookie named "oursitesSSO"
    - retrieve the session variable `$requestedURL` and 302 redirect bob back to `https://private.oursites.com`

Note that outside of some innocuos redirection, Bob only ever sees `https://private.oursites.com` and the Google Login screen in his browser. While Vouch does interact with Bob's browser several times, it is just to set cookies, and if the 302 redirects work properly Bob will log in quickly.

Once the JWT is set, Bob will be authorized for all other sites which are configured to use `https://vouch.oursites.com/validate` from the `auth_request` Nginx module.

The next time Bob is forwarded to google for login, since he has already authorized the Vouch Proxy OAuth app, Google immediately forwards him back and sets the cookie and sends him on his merry way. In some browsers such as Chrome, Bob may not even notice that he logged in using Vouch Proxy.
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Reporting a Vulnerability

If you have discovered a vulnerability in Vouch Proxy DO NOT post an issue on GitHub.

Please do email the maintainers at vouch-proxy-security@bnf.net

We will respond in short order (usually within a day or two).
```

## File: `do.sh`
```bash
#!/usr/bin/env bash
set -e

# change dir to where this script is running
CURDIR=${PWD}
SCRIPT=$(readlink -f "$0")
SDIR=$(dirname "$SCRIPT")
cd $SDIR

if [ -z "$VOUCH_ROOT" ]; then
  export VOUCH_ROOT=${GOPATH}/src/github.com/vouch/vouch-proxy/
fi

IMAGE=quay.io/vouch/vouch-proxy:latest
ALPINE=quay.io/vouch/vouch-proxy:alpine-latest
GOIMAGE=golang:1.23
NAME=vouch-proxy
HTTPPORT=9090
GODOC_PORT=5050

run () {
  go run main.go
}

build () {
  local VERSION=$(git describe --always --long)
  local DT=$(date -u +"%Y-%m-%dT%H:%M:%SZ") # ISO-8601
  local UQDN=$(_hostname)
  local SEMVER=$(git tag --list --sort="v:refname" | tail -n -1)
  local BRANCH=$(git rev-parse --abbrev-ref HEAD)
  local UNAME=$(uname)
  go build -v -ldflags=" -X main.version=${VERSION} -X main.uname=${UNAME} -X main.builddt=${DT} -X main.host=${UQDN} -X main.semver=${SEMVER} -X main.branch=${BRANCH}" .
}

_hostname() {
  local FQDN
  local UQDN
  FQDN=$(hostname)
  UQDN=${FQDN/.*/}

  if [ -z "$UQDN" ]; then
    >&2 echo "error: Could determine the fully qualified domain name."
    return 1
  fi
  echo "$UQDN"
  return 0;
}

install () {
  cp ./vouch-proxy ${GOPATH}/bin/vouch-proxy
}

gogo () {
  docker run --rm -i -t -v /var/run/docker.sock:/var/run/docker.sock -v ${SDIR}/go:/go --name gogo $GOIMAGE $*
}

dbuild () {
  docker build -f Dockerfile -t $IMAGE .
}

dbuildalpine () {
  docker build -f Dockerfile.alpine -t $ALPINE .
}

gobuildstatic () {
  export CGO_ENABLED=0
  export GOOS=linux
  build
}

drun () {
  if [ "$(docker ps | grep $NAME)" ]; then
    docker stop $NAME
    docker rm $NAME
  fi
  WITHCERTS=""
  if [ -d "${SDIR}/certs" ] && [ -z $(find ${SDIR}/certs -type d -empty) ]; then
    WITHCERTS="-v ${SDIR}/certs:/certs"
  fi


  CMD="docker run --rm -i -t
    -p ${HTTPPORT}:${HTTPPORT}
    --name $NAME
    -v ${SDIR}/config:/config
    $WITHCERTS
    $IMAGE $* "

    echo $CMD
    $CMD
}

drunalpine () {
  IMAGE=$ALPINE
  drun $*
}


watch () {
  CMD=$@;
  if [ -z "$CMD" ]; then
      CMD="go run main.go"
  fi
  clear
  echo -e "starting watcher for:\n\t$CMD"

  # TODO: add *.tmpl and *.css
  # find . -type f -name '*.css' | entr -cr $CMD
  find . -name '*.go' | entr -cr $CMD
}

goget () {
  # install all the things
  go get -u -v ./...
  go mod tidy
}

REDACT=""
bug_report() {
  set +e
  # CONFIG=$1; shift;
  CONFIG=config/config.yml
  REDACT=$*

  if [ -z "$REDACT" ]; then
    cat <<EOF

    bug_report cleans the ${CONFIG} and the Vouch Proxy logs of secrets and any additional strings (usually domains and email addresses)

    usage:

      $0 bug_report redacted_string redacted_string

EOF
    exit 1;
  fi
  echo -e "#\n# If sensitive information is still visible in the output, first try appending the string.."
  echo -e "#\n#    '$0 bug_report badstring1 badstring2'\n#\n"
  echo -e "#\n# Please consider submitting a PR for the './do.sh _redact' routine if you feel that it should be improved.\n#"
  echo -e "\n-------------------------\n\n#\n# redacted Vouch Proxy ${CONFIG}\n# $(date -I)\n#\n"
  cat $CONFIG | _redact

  echo -e "\n-------------------------\n\n#\n# redacted Vouch Proxy logs\n# $(date -I)\n#\n"
  echo -e "# be sure to set 'vouch.testing: true' and 'vouch.logLevel: debug' in your config\n"

  trap _redact_exit SIGINT
  ./vouch-proxy 2>&1 | _redact

}

_redact_exit () {
  echo -e "\n\n-------------------------\n"
  echo -e "redact your nginx config with:\n"
  echo -e "\tcat nginx.conf | sed 's/yourdomain.com/DOMAIN.COM/g'\n"
  echo -e "Please upload configs and logs to a gist and open an issue on GitHub at https://github.com/vouch/vouch-proxy/issues\n"
}

_redact() {
  SECRET_FIELDS=("client_id client_secret secret ClientSecret ClientID")
  while IFS= read -r LINE; do
    for i in $SECRET_FIELDS; do
      LINE=$(echo "$LINE" | sed -r "s/${i}..[[:graph:]]*\>/${i}: XXXXXXXXXXX/g")
    done
    # j=$(expr $j + 1)
    for i in $REDACT; do
      r=$i
      r=$(echo "$r" | sed "s/[[:alnum:]]/+/g")
      # LINE=$(echo "$LINE" | sed "s/${i}/+++++++/g")
      LINE=$(echo "$LINE" | sed "s/${i}/${r}/g")
    done
    echo "${LINE}"
  done
}

coverage() {
  mkdir -p .cover && go test -v -coverprofile=.cover/cover.out ./...
}

coveragereport() {
  go tool cover -html=.cover/cover.out -o .cover/coverage.html
}

test() {
  export SKIPPERFTEST=true;
  _tests
}

test_perf() {
  _tests
}

_tests() {
  if [ -z "$VOUCH_CONFIG" ]; then
    export VOUCH_CONFIG="$SDIR/config/testing/test_config.yml"
  fi

  TEST_PRIVATE_KEY_FILE="$SDIR/config/testing/rsa.key"
  TEST_PUBLIC_KEY_FILE="$SDIR/config/testing/rsa.pub"
  if [[ ! -f "$TEST_PRIVATE_KEY_FILE" ]]; then
    openssl genrsa -out "$TEST_PRIVATE_KEY_FILE" 4096
  fi
  if [[ ! -f "$TEST_PUBLIC_KEY_FILE" ]]; then
    openssl rsa -in "$TEST_PRIVATE_KEY_FILE" -pubout > "$TEST_PUBLIC_KEY_FILE"
  fi

  go get -t ./...
  # test all the things
  if [ -n "$*" ]; then
    # go test -v -race $EXTRA_TEST_ARGS $*
    go test -race $EXTRA_TEST_ARGS $*
  else
    # go test -v -race $EXTRA_TEST_ARGS ./...
    go test -race $EXTRA_TEST_ARGS ./...
  fi
}

test_logging() {
  build

  declare -a levels=(error warn info debug)

  echo "testing loglevel set from command line"
  levelcount=0
  for ll in ${levels[*]}; do
    # test that we can see the current level and no level below this level

    declare -a shouldnotfind=()
    for (( i=0; i<${#levels[@]}; i++ ));  do
      if (( $i > $levelcount )); then
        shouldnotfind+=(${levels[$i]})
      fi
    done

    linesread=0
    IFS=$'\n';for line in $(./vouch-proxy -logtest -loglevel ${ll} -config ./config/testing/test_config.yml); do
      let "linesread+=1"
      # echo "$linesread $line"
      # first line is log info
      if (( $linesread > 1 )); then
        for nono in ${shouldnotfind[*]} ; do
          if echo $line | grep $nono; then
            echo "error: line should not contain '$nono' when loglevel is '$ll'"
            echo "$linesread $line"
            exit 1;
          fi
        done
      fi
    done
    let "levelcount+=1"
  done
  echo "passed"

  echo "testing loglevel set from config file"
  levelcount=0
  for ll in ${levels[*]}; do
    # test that we can see the current level and no level below this level
    declare -a shouldnotfind=()
    for (( i=0; i<${#levels[@]}; i++ ));  do
      if (( $i > $levelcount )); then
        shouldnotfind+=(${levels[$i]})
      fi
    done

    linesread=0
    IFS=$'\n';for line in $(./vouch-proxy -logtest -config ./config/testing/logging_${ll}.yml); do
      let "linesread+=1"
      # the first four messages are log and info when starting from the command line
      if (( $linesread > 4 )); then
        # echo "$linesread $line"
        for nono in ${shouldnotfind[*]} ; do
          # echo "testing $nono"
          if echo $line | grep $nono; then
            echo "error: line should not contain '$nono' when loglevel is '$ll'"
            echo "$linesread $line"
            exit 1;
          fi
        done
      fi
    done
    let "levelcount+=1"

  done
  echo "passed"
  exit 0
}

stats () {
  echo -n "lines of code: "
  find . -name '*.go' | xargs wc -l | grep total

  echo -n "number of go files: "
  find . -name '*.go' | wc -l

  echo -n "number of covered packages: "
  covered=$(coverage | grep ok | wc -l)
  echo $covered
  echo -n "number of packages not covered: "
  coverage | grep -v ok | wc -l

  echo -n "average of coverage for all covered packages: "
  sumcoverage=$(coverage | grep ok | awk '{print $5}' | sed 's/%//' | paste -sd+ - | bc)
  # echo " sumcoverage: $sumcoverage "
  perl -le "print $sumcoverage/$covered, '%'"
  exit 0;
}

license() {
  local FILE=$1;
  if [ ! -f "${FILE}" ]; then
    echo "need filename";
    exit 1;
  fi
  FOUND=$(_has_license $FILE)
  if [ -z "${FOUND}" ]; then
    local YEAR=$(git log -1 --format="%ai" -- $FILE | cut -d- -f1);
    _print_license $YEAR > ${FILE}_licensed
    cat $FILE >> ${FILE}_licensed
    mv ${FILE}_licensed $FILE
    echo "added license to the header of $FILE"
  fi

  # and then format the codebase
  gofmt

}

_print_license() {
  local YEAR=$1;
  if [ -z "$YEAR" ]; then
    YEAR=$(date +%Y)
  fi
  cat <<EOF
/*

Copyright $YEAR The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

EOF

}

_has_license() {
  local FILE=$1;
  # echo checking $FILE
  echo $(grep -P 'Copyright \d\d\d\d The Vouch Proxy Authors' ${FILE})
}

profile() {
  echo "for profiling to work you may need to uncomment the code in main.go"
  build
  ./vouch-proxy -profile
  go tool pprof -http=0.0.0.0:19091 http://0.0.0.0:9090/debug/pprof/profile?seconds=10
}

gofmt() {
  # segfault's without exec since it would just call this function infinitely :)
  exec gofmt -w -s .
}

gosec() {
  # segfault's without exec since it would just call this function infinitely :)
  exec gosec ./...
}

selfcert() {
  # https://stackoverflow.com/questions/63588254/how-to-set-up-an-https-server-with-a-self-signed-certificate-in-golang
  set -e
  mkdir -p $SDIR/certs
  # openssl genrsa -out $SDIR/certs/server.key 2048
  openssl ecparam -genkey -name secp384r1 -out $SDIR/certs/server.key
  openssl req -new -x509 -sha256 -key $SDIR/certs/server.key -out $SDIR/certs/server.crt -days 3650
  echo -e "created self signed certs in '$SDIR/certs'\n"
}

usage() {
   cat <<EOF
   usage:
     $0 run                                - go run main.go
     $0 build                              - go build
     $0 install                            - move binary to ${GOPATH}/bin/vouch
     $0 goget                              - get all dependencies
     $0 gofmt                              - gofmt the entire code base
     $0 gosec                              - gosec security audit of the entire code base
     $0 selfcert                           - calls openssl to create a self signed key and cert
     $0 dbuild                             - build docker container
     $0 drun [args]                        - run docker container
     $0 dbuildalpine                       - build docker container for alpine
     $0 drunalpine [args]                  - run docker container for alpine
     $0 test [./pkg_test.go]               - run go tests (defaults to NOT run performance tests)
     $0 test_perf                          - run go tests including performance tests
     $0 test_logging                       - test the logging output
     $0 coverage                           - coverage test
     $0 coveragereport                     - coverage report published to .cover/coverage.html
     $0 profile                            - go pprof tools
     $0 bug_report domain.com [badstr2..]  - print config file and log removing secrets and each provided string
     $0 gogo [gocmd]                       - run, build, any go cmd
     $0 stats                              - simple metrics (lines of code in project, number of go files)
     $0 watch [cmd]                        - watch the \$CWD for any change and re-reun the [cmd] (defaults to 'go run main.go')
     $0 license [file]                     - apply the license to the file

  do is like make

EOF
  exit 1

}

ARG=$1;

case "$ARG" in
   'run' \
   |'build' \
   |'dbuild' \
   |'drun' \
   |'dbuildalpine' \
   |'drunalpine' \
   |'install' \
   |'test' \
   |'goget' \
   |'selfcert' \
   |'gogo' \
   |'watch' \
   |'gobuildstatic' \
   |'coverage' \
   |'coveragereport' \
   |'stats' \
   |'usage' \
   |'bug_report' \
   |'test_perf' \
   |'test_logging' \
   |'license' \
   |'profile' \
   |'gosec' \
   |'gofmt')
   shift
   $ARG $*
   ;;
   'godoc')
   echo "godoc running at http://${GODOC_PORT}"
   godoc -http=:${GODOC_PORT}
   ;;
   'all')
   shift
   gobuildstatic
   dbuild
   drun $*
   ;;
   *)
   usage
   ;;
esac

exit;
```

## File: `go.mod`
```
module github.com/vouch/vouch-proxy

go 1.23.0

toolchain go1.23.2

require (
	github.com/go-viper/mapstructure/v2 v2.4.0
	github.com/google/go-cmp v0.7.0
	github.com/gorilla/sessions v1.4.0
	github.com/julienschmidt/httprouter v1.3.0
	github.com/karupanerura/go-mock-http-response v0.0.0-20171201120521-7c242a447d45
	github.com/kelseyhightower/envconfig v1.4.0
	github.com/nirasan/go-oauth-pkce-code-verifier v0.0.0-20220510032225-4f9f17eaec4c
	github.com/patrickmn/go-cache v2.1.0+incompatible
	github.com/spf13/viper v1.20.1
	github.com/stretchr/testify v1.10.0
	github.com/theckman/go-securerandom v0.1.1
	github.com/tsenart/vegeta v12.7.0+incompatible
	go.uber.org/zap v1.27.0
	golang.org/x/net v0.42.0
	golang.org/x/oauth2 v0.30.0
)

require (
	cloud.google.com/go/compute/metadata v0.7.0 // indirect
	github.com/bmizerany/perks v0.0.0-20141205001514-d9a9656a3a4b // indirect
	github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc // indirect
	github.com/dgryski/go-gk v0.0.0-20200319235926-a69029f61654 // indirect
	github.com/fsnotify/fsnotify v1.9.0 // indirect
	github.com/gorilla/securecookie v1.1.2 // indirect
	github.com/influxdata/tdigest v0.0.1 // indirect
	github.com/josharian/intern v1.0.0 // indirect
	github.com/mailru/easyjson v0.7.7 // indirect
	github.com/pelletier/go-toml/v2 v2.2.4 // indirect
	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2 // indirect
	github.com/sagikazarmark/locafero v0.9.0 // indirect
	github.com/sourcegraph/conc v0.3.0 // indirect
	github.com/spf13/afero v1.14.0 // indirect
	github.com/spf13/cast v1.9.2 // indirect
	github.com/spf13/pflag v1.0.7 // indirect
	github.com/streadway/quantile v0.0.0-20150917103942-b0c588724d25 // indirect
	github.com/subosito/gotenv v1.6.0 // indirect
	go.uber.org/multierr v1.11.0 // indirect
	golang.org/x/exp v0.0.0-20250718183923-645b1fa84792 // indirect
	golang.org/x/sys v0.34.0 // indirect
	golang.org/x/text v0.27.0 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)

require github.com/golang-jwt/jwt/v4 v4.5.2
```

## File: `go.sum`
```
cloud.google.com/go/compute/metadata v0.7.0 h1:PBWF+iiAerVNe8UCHxdOt6eHLVc3ydFeOCw78U8ytSU=
cloud.google.com/go/compute/metadata v0.7.0/go.mod h1:j5MvL9PprKL39t166CoB1uVHfQMs4tFQZZcKwksXUjo=
github.com/bmizerany/perks v0.0.0-20141205001514-d9a9656a3a4b h1:AP/Y7sqYicnjGDfD5VcY4CIfh1hRXBUavxrvELjTiOE=
github.com/bmizerany/perks v0.0.0-20141205001514-d9a9656a3a4b/go.mod h1:ac9efd0D1fsDb3EJvhqgXRbFx7bs2wqZ10HQPeU8U/Q=
github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc h1:U9qPSI2PIWSS1VwoXQT9A3Wy9MM3WgvqSxFWenqJduM=
github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/dgryski/go-gk v0.0.0-20200319235926-a69029f61654 h1:XOPLOMn/zT4jIgxfxSsoXPxkrzz0FaCHwp33x5POJ+Q=
github.com/dgryski/go-gk v0.0.0-20200319235926-a69029f61654/go.mod h1:qm+vckxRlDt0aOla0RYJJVeqHZlWfOm2UIxHaqPB46E=
github.com/frankban/quicktest v1.14.6 h1:7Xjx+VpznH+oBnejlPUj8oUpdxnVs4f8XU8WnHkI4W8=
github.com/frankban/quicktest v1.14.6/go.mod h1:4ptaffx2x8+WTWXmUCuVU6aPUX1/Mz7zb5vbUoiM6w0=
github.com/fsnotify/fsnotify v1.9.0 h1:2Ml+OJNzbYCTzsxtv8vKSFD9PbJjmhYF14k/jKC7S9k=
github.com/fsnotify/fsnotify v1.9.0/go.mod h1:8jBTzvmWwFyi3Pb8djgCCO5IBqzKJ/Jwo8TRcHyHii0=
github.com/go-viper/mapstructure/v2 v2.4.0 h1:EBsztssimR/CONLSZZ04E8qAkxNYq4Qp9LvH92wZUgs=
github.com/go-viper/mapstructure/v2 v2.4.0/go.mod h1:oJDH3BJKyqBA2TXFhDsKDGDTlndYOZ6rGS0BRZIxGhM=
github.com/golang-jwt/jwt/v4 v4.5.2 h1:YtQM7lnr8iZ+j5q71MGKkNw9Mn7AjHM68uc9g5fXeUI=
github.com/golang-jwt/jwt/v4 v4.5.2/go.mod h1:m21LjoU+eqJr34lmDMbreY2eSTRJ1cv77w39/MY0Ch0=
github.com/google/go-cmp v0.2.0/go.mod h1:oXzfMopK8JAjlY9xF4vHSVASa0yLyX7SntLO5aqRK0M=
github.com/google/go-cmp v0.7.0 h1:wk8382ETsv4JYUZwIsn6YpYiWiBsYLSJiTsyBybVuN8=
github.com/google/go-cmp v0.7.0/go.mod h1:pXiqmnSA92OHEEa9HXL2W4E7lf9JzCmGVUdgjX3N/iU=
github.com/google/gofuzz v1.2.0 h1:xRy4A+RhZaiKjJ1bPfwQ8sedCA+YS2YcCHW6ec7JMi0=
github.com/google/gofuzz v1.2.0/go.mod h1:dBl0BpW6vV/+mYPU4Po3pmUjxk6FQPldtuIdl/M65Eg=
github.com/gorilla/securecookie v1.1.2 h1:YCIWL56dvtr73r6715mJs5ZvhtnY73hBvEF8kXD8ePA=
github.com/gorilla/securecookie v1.1.2/go.mod h1:NfCASbcHqRSY+3a8tlWJwsQap2VX5pwzwo4h3eOamfo=
github.com/gorilla/sessions v1.4.0 h1:kpIYOp/oi6MG/p5PgxApU8srsSw9tuFbt46Lt7auzqQ=
github.com/gorilla/sessions v1.4.0/go.mod h1:FLWm50oby91+hl7p/wRxDth9bWSuk0qVL2emc7lT5ik=
github.com/influxdata/tdigest v0.0.1 h1:XpFptwYmnEKUqmkcDjrzffswZ3nvNeevbUSLPP/ZzIY=
github.com/influxdata/tdigest v0.0.1/go.mod h1:Z0kXnxzbTC2qrx4NaIzYkE1k66+6oEDQTvL95hQFh5Y=
github.com/josharian/intern v1.0.0 h1:vlS4z54oSdjm0bgjRigI+G1HpF+tI+9rE5LLzOg8HmY=
github.com/josharian/intern v1.0.0/go.mod h1:5DoeVV0s6jJacbCEi61lwdGj/aVlrQvzHFFd8Hwg//Y=
github.com/julienschmidt/httprouter v1.3.0 h1:U0609e9tgbseu3rBINet9P48AI/D3oJs4dN7jwJOQ1U=
github.com/julienschmidt/httprouter v1.3.0/go.mod h1:JR6WtHb+2LUe8TCKY3cZOxFyyO8IZAc4RVcycCCAKdM=
github.com/karupanerura/go-mock-http-response v0.0.0-20171201120521-7c242a447d45 h1:XSik/ETzj52cVbZcv7tJuUFX14XzvRX0te26UaKY0Aw=
github.com/karupanerura/go-mock-http-response v0.0.0-20171201120521-7c242a447d45/go.mod h1:FULZ2B7LE0CUYtI8XLMYxI58AF9M6MTg6nWmZvWoFHQ=
github.com/kelseyhightower/envconfig v1.4.0 h1:Im6hONhd3pLkfDFsbRgu68RDNkGF1r3dvMUtDTo2cv8=
github.com/kelseyhightower/envconfig v1.4.0/go.mod h1:cccZRl6mQpaq41TPp5QxidR+Sa3axMbJDNb//FQX6Gg=
github.com/kr/pretty v0.3.1 h1:flRD4NNwYAUpkphVc1HcthR4KEIFJ65n8Mw5qdRn3LE=
github.com/kr/pretty v0.3.1/go.mod h1:hoEshYVHaxMs3cyo3Yncou5ZscifuDolrwPKZanG3xk=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/mailru/easyjson v0.7.7 h1:UGYAvKxe3sBsEDzO8ZeWOSlIQfWFlxbzLZe7hwFURr0=
github.com/mailru/easyjson v0.7.7/go.mod h1:xzfreul335JAWq5oZzymOObrkdz5UnU4kGfJJLY9Nlc=
github.com/nirasan/go-oauth-pkce-code-verifier v0.0.0-20220510032225-4f9f17eaec4c h1:4RYnE0ISVwRxm9Dfo7utw1dh0kdRDEmVYq2MFVLy5zI=
github.com/nirasan/go-oauth-pkce-code-verifier v0.0.0-20220510032225-4f9f17eaec4c/go.mod h1:DvuJJ/w1Y59rG8UTDxsMk5U+UJXJwuvUgbiJSm9yhX8=
github.com/patrickmn/go-cache v2.1.0+incompatible h1:HRMgzkcYKYpi3C8ajMPV8OFXaaRUnok+kx1WdO15EQc=
github.com/patrickmn/go-cache v2.1.0+incompatible/go.mod h1:3Qf8kWWT7OJRJbdiICTKqZju1ZixQ/KpMGzzAfe6+WQ=
github.com/pelletier/go-toml/v2 v2.2.4 h1:mye9XuhQ6gvn5h28+VilKrrPoQVanw5PMw/TB0t5Ec4=
github.com/pelletier/go-toml/v2 v2.2.4/go.mod h1:2gIqNv+qfxSVS7cM2xJQKtLSTLUE9V8t9Stt+h56mCY=
github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2 h1:Jamvg5psRIccs7FGNTlIRMkT8wgtp5eCXdBlqhYGL6U=
github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/rogpeppe/go-internal v1.9.0 h1:73kH8U+JUqXU8lRuOHeVHaa/SZPifC7BkcraZVejAe8=
github.com/rogpeppe/go-internal v1.9.0/go.mod h1:WtVeX8xhTBvf0smdhujwtBcq4Qrzq/fJaraNFVN+nFs=
github.com/sagikazarmark/locafero v0.9.0 h1:GbgQGNtTrEmddYDSAH9QLRyfAHY12md+8YFTqyMTC9k=
github.com/sagikazarmark/locafero v0.9.0/go.mod h1:UBUyz37V+EdMS3hDF3QWIiVr/2dPrx49OMO0Bn0hJqk=
github.com/sourcegraph/conc v0.3.0 h1:OQTbbt6P72L20UqAkXXuLOj79LfEanQ+YQFNpLA9ySo=
github.com/sourcegraph/conc v0.3.0/go.mod h1:Sdozi7LEKbFPqYX2/J+iBAM6HpqSLTASQIKqDmF7Mt0=
github.com/spf13/afero v1.14.0 h1:9tH6MapGnn/j0eb0yIXiLjERO8RB6xIVZRDCX7PtqWA=
github.com/spf13/afero v1.14.0/go.mod h1:acJQ8t0ohCGuMN3O+Pv0V0hgMxNYDlvdk+VTfyZmbYo=
github.com/spf13/cast v1.9.2 h1:SsGfm7M8QOFtEzumm7UZrZdLLquNdzFYfIbEXntcFbE=
github.com/spf13/cast v1.9.2/go.mod h1:jNfB8QC9IA6ZuY2ZjDp0KtFO2LZZlg4S/7bzP6qqeHo=
github.com/spf13/pflag v1.0.7 h1:vN6T9TfwStFPFM5XzjsvmzZkLuaLX+HS+0SeFLRgU6M=
github.com/spf13/pflag v1.0.7/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/spf13/viper v1.20.1 h1:ZMi+z/lvLyPSCoNtFCpqjy0S4kPbirhpTMwl8BkW9X4=
github.com/spf13/viper v1.20.1/go.mod h1:P9Mdzt1zoHIG8m2eZQinpiBjo6kCmZSKBClNNqjJvu4=
github.com/streadway/quantile v0.0.0-20150917103942-b0c588724d25 h1:7z3LSn867ex6VSaahyKadf4WtSsJIgne6A1WLOAGM8A=
github.com/streadway/quantile v0.0.0-20150917103942-b0c588724d25/go.mod h1:lbP8tGiBjZ5YWIc2fzuRpTaz0b/53vT6PEs3QuAWzuU=
github.com/stretchr/testify v1.10.0 h1:Xv5erBjTwe/5IxqUQTdXv5kgmIvbHo3QQyRwhJsOfJA=
github.com/stretchr/testify v1.10.0/go.mod h1:r2ic/lqez/lEtzL7wO/rwa5dbSLXVDPFyf8C91i36aY=
github.com/subosito/gotenv v1.6.0 h1:9NlTDc1FTs4qu0DDq7AEtTPNw6SVm7uBMsUCUjABIf8=
github.com/subosito/gotenv v1.6.0/go.mod h1:Dk4QP5c2W3ibzajGcXpNraDfq2IrhjMIvMSWPKKo0FU=
github.com/theckman/go-securerandom v0.1.1 h1:5KctSyM0D5KKFK+bsypIyLq7yik0CEaI5i2fGcUGcsQ=
github.com/theckman/go-securerandom v0.1.1/go.mod h1:bmkysLfBH6i891sBpcP4xRM3XIB7jMeiKJB31jlResI=
github.com/tsenart/vegeta v12.7.0+incompatible h1:sGlrv11EMxQoKOlDuMWR23UdL90LE5VlhKw/6PWkZmU=
github.com/tsenart/vegeta v12.7.0+incompatible/go.mod h1:Smz/ZWfhKRcyDDChZkG3CyTHdj87lHzio/HOCkbndXM=
go.uber.org/goleak v1.3.0 h1:2K3zAYmnTNqV73imy9J1T3WC+gmCePx2hEGkimedGto=
go.uber.org/goleak v1.3.0/go.mod h1:CoHD4mav9JJNrW/WLlf7HGZPjdw8EucARQHekz1X6bE=
go.uber.org/multierr v1.11.0 h1:blXXJkSxSSfBVBlC76pxqeO+LN3aDfLQo+309xJstO0=
go.uber.org/multierr v1.11.0/go.mod h1:20+QtiLqy0Nd6FdQB9TLXag12DsQkrbs3htMFfDN80Y=
go.uber.org/zap v1.27.0 h1:aJMhYGrd5QSmlpLMr2MftRKl7t8J8PTZPA732ud/XR8=
go.uber.org/zap v1.27.0/go.mod h1:GB2qFLM7cTU87MWRP2mPIjqfIDnGu+VIO4V/SdhGo2E=
golang.org/x/exp v0.0.0-20180321215751-8460e604b9de/go.mod h1:CJ0aWSM057203Lf6IL+f9T1iT9GByDxfZKAQTCR3kQA=
golang.org/x/exp v0.0.0-20250718183923-645b1fa84792 h1:R9PFI6EUdfVKgwKjZef7QIwGcBKu86OEFpJ9nUEP2l4=
golang.org/x/exp v0.0.0-20250718183923-645b1fa84792/go.mod h1:A+z0yzpGtvnG90cToK5n2tu8UJVP2XUATh+r+sfOOOc=
golang.org/x/net v0.42.0 h1:jzkYrhi3YQWD6MLBJcsklgQsoAcw89EcZbJw8Z614hs=
golang.org/x/net v0.42.0/go.mod h1:FF1RA5d3u7nAYA4z2TkclSCKh68eSXtiFwcWQpPXdt8=
golang.org/x/oauth2 v0.30.0 h1:dnDm7JmhM45NNpd8FDDeLhK6FwqbOf4MLCM9zb1BOHI=
golang.org/x/oauth2 v0.30.0/go.mod h1:B++QgG3ZKulg6sRPGD/mqlHQs5rB3Ml9erfeDY7xKlU=
golang.org/x/sys v0.34.0 h1:H5Y5sJ2L2JRdyv7ROF1he/lPdvFsd0mJHFw2ThKHxLA=
golang.org/x/sys v0.34.0/go.mod h1:BJP2sWEmIv4KK5OTEluFJCKSidICx8ciO85XgH3Ak8k=
golang.org/x/text v0.27.0 h1:4fGWRpyh641NLlecmyl4LOe6yDdfaYNrGb2zdfo4JV4=
golang.org/x/text v0.27.0/go.mod h1:1D28KMCvyooCX9hBiosv5Tz/+YLxj0j7XhWjpSUF7CU=
golang.org/x/tools v0.0.0-20180525024113-a5b4c53f6e8b/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
gonum.org/v1/gonum v0.0.0-20181121035319-3f7ecaa7e8ca h1:PupagGYwj8+I4ubCxcmcBRk3VlUWtTg5huQpZR9flmE=
gonum.org/v1/gonum v0.0.0-20181121035319-3f7ecaa7e8ca/go.mod h1:Y+Yx5eoAFn32cQvJDxZx5Dpnq+c3wtXuadVZAcxbbBo=
gonum.org/v1/netlib v0.0.0-20181029234149-ec6d1f5cefe6/go.mod h1:wa6Ws7BG/ESfp6dHfk7C6KdzKA7wR7u/rKwOGE66zvw=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20190902080502-41f04d3bba15 h1:YR8cESwS4TdDjEe65xsg0ogRM/Nc3DYOhEAlW+xobZo=
gopkg.in/check.v1 v1.0.0-20190902080502-41f04d3bba15/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `main.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package main

// Vouch Proxy
// github.com/vouch/vouch-proxy

/*

Hello Developer!  Thanks for looking at the code!

Before submitting PRs, please see the README...
https://github.com/vouch/vouch-proxy#submitting-a-pull-request-for-a-new-feature

*/

import (
	"embed"
	"errors"
	"flag"
	"fmt"
	"io/fs"
	"log"
	"net"
	"net/http"
	"os"
	"os/user"
	"strconv"
	"strings"
	"time"

	// "net/http/pprof"

	"github.com/julienschmidt/httprouter"
	"go.uber.org/zap"

	"github.com/vouch/vouch-proxy/handlers"
	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/cookie"
	"github.com/vouch/vouch-proxy/pkg/domains"
	"github.com/vouch/vouch-proxy/pkg/healthcheck"
	"github.com/vouch/vouch-proxy/pkg/jwtmanager"
	"github.com/vouch/vouch-proxy/pkg/responses"
	"github.com/vouch/vouch-proxy/pkg/timelog"
)

// `version`, `semver` and others are populated during build by..
// go build -i -v -ldflags="-X main.version=$(git describe --always --long) -X main.semver=v$(git semver get)"
var (
	version     = "undefined"
	builddt     = "undefined"
	host        = "undefined"
	semver      = "undefined"
	branch      = "undefined"
	uname       = "undefined"
	logger      *zap.SugaredLogger
	fastlog     *zap.Logger
	showVersion = flag.Bool("version", false, "display version and exit")
	help        = flag.Bool("help", false, "show usage")
	scheme      = map[bool]string{
		false: "http",
		true:  "https",
	}
	// doProfile = flag.Bool("profile", false, "run profiler at /debug/pprof")
)

//go:embed static
var staticFs embed.FS

//go:embed templates
var templatesFs embed.FS

//go:embed .defaults.yml
var defaultsFs embed.FS

// fwdToZapWriter allows us to use the zap.Logger as our http.Server ErrorLog
// see https://stackoverflow.com/questions/52294334/net-http-set-custom-logger
type fwdToZapWriter struct {
	logger *zap.Logger
}

func (fw *fwdToZapWriter) Write(p []byte) (n int, err error) {
	fw.logger.Error(string(p))
	return len(p), nil
}

// configure() is essentially init()
// for most other projects you would think of this as init()
// this epic issue related to the flag.parse change of behavior for go 1.13 explains some of what's going on here
// https://github.com/golang/go/issues/31859
// essentially, flag.parse() must be called in vouch-proxy's main() and *not* in init()
// this has a cascading effect on the zap logger since the log level can be set on the command line
// configure() explicitly calls package configure functions (domains.Configure() etc) mostly to set the logger
// without this setup testing and logging are screwed up
func configure() {
	flag.Parse()

	if *help {
		flag.PrintDefaults()
		os.Exit(1)
	}

	if *showVersion {
		fmt.Printf("%s\n", semver)
		os.Exit(0)
	}

	cfg.Templates = templatesFs
	cfg.Defaults = defaultsFs

	cfg.Configure()
	healthcheck.CheckAndExitIfIsHealthCheck()

	logger = cfg.Logging.Logger
	fastlog = cfg.Logging.FastLogger

	if err := cfg.ValidateConfiguration(); err != nil {
		logger.Fatal(err)
	}

	domains.Configure()
	jwtmanager.Configure()
	cookie.Configure()
	responses.Configure()
	handlers.Configure()
	timelog.Configure()
}

func main() {
	configure()
	listenStr := cfg.Cfg.Listen
	if !strings.HasPrefix(cfg.Cfg.Listen, "unix:") {
		listenStr = cfg.Cfg.Listen + ":" + strconv.Itoa(cfg.Cfg.Port)
		checkTCPPortAvailable(listenStr)
	}

	tls := (cfg.Cfg.TLS.Cert != "" && cfg.Cfg.TLS.Key != "")
	logger.Infow("starting "+cfg.Branding.FullName,
		// "semver":    semver,
		"version", version,
		"buildtime", builddt,
		"uname", uname,
		"buildhost", host,
		"branch", branch,
		"semver", semver,
		"listen", scheme[tls]+"://"+listenStr,
		"tls", tls,
		"document_root", cfg.Cfg.DocumentRoot,
		"oauth.provider", cfg.GenOAuth.Provider)

	// router := mux.NewRouter()
	router := httprouter.New()

	if cfg.Cfg.DocumentRoot != "" {
		logger.Debugf("adjusting all served URIs to be under %s", cfg.Cfg.DocumentRoot)
	}

	authH := http.HandlerFunc(handlers.ValidateRequestHandler)
	router.HandlerFunc(http.MethodGet, cfg.Cfg.DocumentRoot+"/validate", timelog.TimeLog(jwtmanager.JWTCacheHandler(authH)))
	router.HandlerFunc(http.MethodGet, cfg.Cfg.DocumentRoot+"/_external-auth-:id", timelog.TimeLog(jwtmanager.JWTCacheHandler(authH)))

	loginH := http.HandlerFunc(handlers.LoginHandler)
	router.HandlerFunc(http.MethodGet, cfg.Cfg.DocumentRoot+"/login", timelog.TimeLog(loginH))

	logoutH := http.HandlerFunc(handlers.LogoutHandler)
	router.HandlerFunc(http.MethodGet, cfg.Cfg.DocumentRoot+"/logout", timelog.TimeLog(logoutH))

	callH := http.HandlerFunc(handlers.CallbackHandler)
	router.HandlerFunc(http.MethodGet, cfg.Cfg.DocumentRoot+"/auth", timelog.TimeLog(callH))

	authStateH := http.HandlerFunc(handlers.AuthStateHandler)
	router.HandlerFunc(http.MethodGet, cfg.Cfg.DocumentRoot+"/auth/:state/", timelog.TimeLog(authStateH))

	healthH := http.HandlerFunc(handlers.HealthcheckHandler)
	router.HandlerFunc(http.MethodGet, "/healthcheck", timelog.TimeLog(healthH))

	// this is the documented implemenation for static file serving but it doesn't seem to work with go:embed
	// router.ServeFiles("/static/*filepath", http.FS(staticFs))

	// so instead we publish all three routes
	router.Handler(http.MethodGet, cfg.Cfg.DocumentRoot+"/static/css/main.css", http.StripPrefix(cfg.Cfg.DocumentRoot, http.FileServer(http.FS(staticFs))))
	router.Handler(http.MethodGet, cfg.Cfg.DocumentRoot+"/static/img/favicon.ico", http.StripPrefix(cfg.Cfg.DocumentRoot, http.FileServer(http.FS(staticFs))))
	router.Handler(http.MethodGet, cfg.Cfg.DocumentRoot+"/static/img/multicolor_V_500x500.png", http.StripPrefix(cfg.Cfg.DocumentRoot, http.FileServer(http.FS(staticFs))))

	// this also works for static files
	// router.NotFound = http.FileServer(http.FS(staticFs))

	//
	// if *doProfile {
	// 	addProfilingHandlers(router)
	// }

	srv := &http.Server{
		Handler: router,
		// Good practice: enforce timeouts for servers you create!
		WriteTimeout: time.Duration(cfg.Cfg.WriteTimeout) * time.Second,
		ReadTimeout:  time.Duration(cfg.Cfg.ReadTimeout) * time.Second,
		IdleTimeout:  time.Duration(cfg.Cfg.IdleTimeout) * time.Second,
		ErrorLog:     log.New(&fwdToZapWriter{fastlog}, "", 0),
	}

	lis, cleanupFn, err := listen()
	if err != nil {
		logger.Fatal(err)
	}
	defer cleanupFn()

	if tls {
		srv.TLSConfig = cfg.TLSConfig(cfg.Cfg.TLS.Profile)
		logger.Fatal(srv.ServeTLS(lis, cfg.Cfg.TLS.Cert, cfg.Cfg.TLS.Key))
	} else {
		logger.Fatal(srv.Serve(lis))
	}

}

func listen() (lis net.Listener, cleanupFn func(), err error) {
	if !strings.HasPrefix(cfg.Cfg.Listen, "unix:") {
		lis, err = net.Listen("tcp", fmt.Sprintf("%s:%d", cfg.Cfg.Listen, cfg.Cfg.Port))
		return lis, func() {}, err
	}

	socketPath := strings.TrimPrefix(cfg.Cfg.Listen, "unix:")
	_, err = os.Stat(socketPath)
	if err == nil {
		if err = os.Remove(socketPath); err != nil {
			return nil, nil, fmt.Errorf("remove existing socket file %s: %w", socketPath, err)
		}
	} else if !os.IsNotExist(err) {
		return nil, nil, fmt.Errorf("stat socket file %s: %w", socketPath, err)
	}

	lis, err = net.Listen("unix", socketPath)
	if err != nil {
		return nil, nil, fmt.Errorf("listen %s: %w", socketPath, err)
	}

	mode := fs.FileMode(cfg.Cfg.SocketMode) // defaults to 0660 - see .defaults.yml
	if err = os.Chmod(socketPath, mode); err != nil {
		return nil, nil, fmt.Errorf("chmod socket file %s %#o", socketPath, mode)
	}

	if cfg.Cfg.SocketGroup != "" {
		group, err := user.LookupGroup(cfg.Cfg.SocketGroup)
		if err != nil {
			return nil, nil, fmt.Errorf("lookup socket group: %s %w", cfg.Cfg.SocketGroup, err)
		}
		gid, err := strconv.Atoi(group.Gid)
		if err != nil {
			return nil, nil, fmt.Errorf("lookup socket group: invalid gid: %w", err)
		}
		if err := os.Chown(socketPath, -1, gid); err != nil {
			return nil, nil, fmt.Errorf("chown socket: group: %s %w", socketPath, err)
		}
	}
	return lis, func() { _ = os.Remove(socketPath) }, nil
}

func checkTCPPortAvailable(listen string) {
	logger.Debug("checking availability of tcp port: " + listen)
	conn, err := net.Listen("tcp", listen)
	if err != nil {
		logger.Error(err)
		logger.Fatal(errors.New(listen + " is not available (is " + cfg.Branding.FullName + " already running?)"))
	}
	if err = conn.Close(); err != nil {
		logger.Error(err)
	}
}

// if you'd like to enable profiling uncomment these
// func addProfilingHandlers(router *httprouter.Router) {
// 	// https://stackoverflow.com/questions/47452471/pprof-profile-with-julienschmidtrouter-and-benchmarks-not-profiling-handler
// 	logger.Debugf("profiling routes added at http://%s:%d/debug/pprof/", cfg.Cfg.Listen, cfg.Cfg.Port)
// 	router.HandlerFunc(http.MethodGet, "/debug/pprof/", pprof.Index)
// 	router.HandlerFunc(http.MethodGet, "/debug/pprof/cmdline", pprof.Cmdline)
// 	router.HandlerFunc(http.MethodGet, "/debug/pprof/profile", pprof.Profile)
// 	router.HandlerFunc(http.MethodGet, "/debug/pprof/symbol", pprof.Symbol)
// 	router.HandlerFunc(http.MethodGet, "/debug/pprof/trace", pprof.Trace)
// 	router.Handler(http.MethodGet, "/debug/pprof/goroutine", pprof.Handler("goroutine"))
// 	router.Handler(http.MethodGet, "/debug/pprof/heap", pprof.Handler("heap"))
// 	router.Handler(http.MethodGet, "/debug/pprof/threadcreate", pprof.Handler("threadcreate"))
// 	router.Handler(http.MethodGet, "/debug/pprof/block", pprof.Handler("block"))
// }
```

## File: `main_test.go`
```go
package main

import (
	"io/fs"
	"os"
	"path/filepath"
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/vouch/vouch-proxy/pkg/cfg"
)

func Test_listenUds(t *testing.T) {
	setUp(t, "testing/socket_basic.yml")
	defer cleanUp()
	tempDir, err := os.MkdirTemp("", "")
	assert.NoError(t, err)
	defer func() {
		_ = os.RemoveAll(tempDir)
	}()
	socketPath := filepath.Join(tempDir, "socket0")

	cfg.Cfg.Listen = strings.Join([]string{"unix", socketPath}, ":")
	lis, cleanupFn, err := listen()
	assert.NoError(t, err)
	assertSocket(t, socketPath)

	fi, err := os.Stat(socketPath)
	assert.NoError(t, err)
	assert.Equal(t, fs.FileMode(0660), fi.Mode().Perm())

	assert.NotNil(t, lis)
	assert.NoError(t, lis.Close())
	cleanupFn()
	_, err = os.Stat(socketPath)
	assert.True(t, os.IsNotExist(err))
}

// check that socket listening works when the socket path already exists
func Test_listenUds_alreadyExists(t *testing.T) {
	setUp(t, "testing/socket_basic.yml")
	defer cleanUp()
	tempDir, err := os.MkdirTemp("", "")
	assert.NoError(t, err)
	defer func() {
		_ = os.RemoveAll(tempDir)
	}()
	socketPath := filepath.Join(tempDir, "socket0")
	assert.NoError(t, os.WriteFile(socketPath, []byte("stuff in the socket file"), 0600))

	cfg.Cfg.Listen = strings.Join([]string{"unix", socketPath}, ":")
	lis, cleanupFn, err := listen()
	assert.NoError(t, err)
	assertSocket(t, socketPath)

	assert.NotNil(t, lis)
	assert.NoError(t, lis.Close())
	cleanupFn()
}

// check that the socket mode is adjusted when the SocketMode configuration is present
func Test_listenUds_mode(t *testing.T) {
	setUp(t, "config/testing/socket_mode.yml")
	defer cleanUp()
	tempDir, err := os.MkdirTemp("", "")
	assert.NoError(t, err)
	defer func() {
		_ = os.RemoveAll(tempDir)
	}()
	socketPath := filepath.Join(tempDir, "socket0")
	cfg.Cfg.Listen = strings.Join([]string{"unix", socketPath}, ":")

	lis, cleanupFn, err := listen()
	assert.NoError(t, err)
	assert.NotNil(t, lis)
	assertSocket(t, socketPath)

	stat, err := os.Stat(socketPath)
	assert.NoError(t, err)
	assert.Equal(t, fs.FileMode(cfg.Cfg.SocketMode), stat.Mode().Perm())

	assert.NoError(t, lis.Close())
	cleanupFn()
}

func assertSocket(t *testing.T, socketPath string) {
	fi, err := os.Stat(socketPath)
	assert.NoError(t, err)
	assert.Equal(t, os.ModeSocket, fi.Mode()&os.ModeSocket)
}

func setUp(t *testing.T, configFile string) {
	assert.NoError(t, os.Setenv(cfg.Branding.UCName+"_CONFIG", configFile))
	cfg.InitForTestPurposes()
}

func cleanUp() {
	os.Clearenv()
}
```

## File: `config/config.yml_example`
```
# Vouch Proxy configuration

# you should probably start with one of the other example configs in this directory
# Vouch Proxy does a fairly good job of setting its config to sane defaults

# be aware of the yaml indentation, the only top level elements are `vouch` and `oauth`. 

# Vouch Proxy can also be configured using Environmental Variables.  The associated env var for
# each configuration is shown such as VOUCH_LOGLEVEL.

vouch:
  # logLevel: debug # VOUCH_LOGLEVEL
  logLevel: info

  # testing: false - VOUCH_TESTING
  # force all 302 redirects to be rendered as a webpage with a link
  # if you're having problems, turn on testing
  testing: true

  listen: 0.0.0.0  # VOUCH_LISTEN
  port: 9090       # VOUCH_PORT

  # Listen can specify a Unix domain socket instead.
  # listen: unix:/path/to/socket # VOUCH_LISTEN

  # Optionally set the mode of the Unix domain socket. The default if not specified is 0777.
  # socket_mode: 0770 # VOUCH_SOCKETMODE

  # Optionally set the group owner of the Unix domain socket.
  # socket_group: users # VOUCH_SOCKETGROUP

  # The default read, write and idle timeouts are 15 seconds.
  # If you have a load balancer or proxy in front that has its
  # own idle timeout, you may need to ensure that the Vouch idle
  # timeout is longer than the proxy's, to avoid intermittent
  # 502 errors.
  # See https://github.com/vouch/vouch-proxy/issues/317 for more
  # information.
  writeTimeout: 15 # VOUCH_WRITETIMEOUT
  readTimeout: 15  # VOUCH_READTIMEOUT
  idleTimeout: 15  # VOUCH_IDLETIMEOUT

  # document_root - VOUCH_DOCUMENT_ROOT
  # see README for `Vouch Proxy "in a path"` - https://github.com/vouch/vouch-proxy#vouch-proxy-in-a-path
  # document_root: vp_in_a_path

  # domains - VOUCH_DOMAINS
  # each of these domains must serve the url https://vouch.$domains[0] https://vouch.$domains[1] ...
  # so that the cookie which stores the JWT can be set in the relevant domain
  # you usually *don't* want to list every individual website that will be protected
  # if you have siteA.internal.yourdomain.com and siteB.internal.yourdomain.com 
  # then your domains should be set as yourdomain.com or perhaps internal.yourdomain.com   
  # usually you'll just have one.
  # Comment `domains:` out if you set allowAllUser:true
  domains:
  - yourdomain.com
  - yourotherdomain.com

  # Set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at the configured provider - VOUCH_ALLOWALLUSERS
  # allowAllUsers: false
  # vouch.cookie.domain must be set below when enabling allowAllUsers

  # Setting publicAccess: true will accept all requests, even without a valid jwt/cookie.  - VOUCH_PUBLICACCESS
  # If the user is logged in, the cookie will be validated and the user header will be set.
  # You will need to direct people to the Vouch Proxy login page from your application.
  # publicAccess: false

  # whiteList (optional) allows only the listed usernames - VOUCH_WHITELIST
  # usernames are usually email addresses (google, most oidc providers) or login/username for github and github enterprise
  whiteList:
  - bob@yourdomain.com
  - alice@yourdomain.com
  - joe@yourdomain.com

  # teamWhitelist - VOUCH_TEAMWHITELIST
  # only used for github orgs/teams
  # teamWhitelist:
  # - vouch
  # - myOrg
  # - myOrg/myTeam

  tls:
    # cert: /path/to/signed_cert_plus_intermediates # VOUCH_TLS_CERT
    # key: /path/to/private_key                     # VOUCH_TLS_KEY
    # profile - defines the TLS configuration profile (modern, intermediate, old, default)
    profile: intermediate                           # VOUCH_TLS_PROFILE

  jwt:
    # signing_method: the algorithm used to sign the JWT.  # VOUCH_JWT_SIGNING_METHOD
    # Can be one of HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384, ES512
    # Default is HS256 (HMAC) - and requires jwt.secret to be set
    # Both RS* (RSA) and ES* (ECDSA) methods require jwt.private_key_file and
    # jwt.public_key_file to be set.
    # signing_method: HS256

    # secret - VOUCH_JWT_SECRET
    # a random string used to cryptographically sign the jwt when signing_method is set to HS256, HS384 or HS512
    # Vouch Proxy complains if the string is less than 44 characters (256 bits as 32 base64 bytes)
    # if the secret is not set here then Vouch Proxy will..
    # - look for the secret in `./config/secret`
    # - if `./config/secret` doesn't exist then randomly generate a secret and store it there
    # in order to run multiple instances of vouch on multiple servers (perhaps purely for validating the jwt),
    # you'll want them all to have the same secret
    secret: your_random_string

    # Path to the public/private key files when using an RSA or ECDSA signing method.
    # public_key_file:  # VOUCH_JWT_PUBLIC_KEY_FILE
    # private_key_file: # VOUCH_JWT_PRIVATE_KEY_FILE

    # issuer: Vouch # VOUCH_JWT_ISSUER

    # number of minutes until jwt expires - VOUCH_JWT_MAXAGE
    maxAge: 240

    # compress the jwt - VOUCH_JWT_COMPRESS
    compress: true 

  cookie: 
    # name of cookie to store the jwt - VOUCH_COOKIE_NAME
    name: VouchCookie

    # optionally force the domain of the cookie to set
    # domain: yourdomain.com # VOUCH_COOKIE_DOMAIN

    # Set `secure: false` when protecting a non-https site such as http://app.yourdmain.com - VOUCH_COOKIE_SECURE
    secure: true

    # httpOnly: true # VOUCH_COOKIE_HTTPONLY

    # Number of minutes until session cookie expires - VOUCH_COOKIE_MAXAGE
    # Set cookie maxAge to 0 to delete the cookie every time the browser is closed.
    # Must not be longer than jwt.maxAge
    maxAge: 240

    # Set SameSite attribute to restrict browser behaviour wrt sending the cookie along with cross-site requests. - VOUCH_COOKIE_SAMESITE
    # Possible attribute values lax, strict, none.
    # If attribute not specified then cross-site behaviour will depend on the browser used. If sameSite=none then secure must be set to true
    # More context: https://github.com/vouch/vouch-proxy/issues/210
    sameSite: lax

  session:
    # name of session variable stored locally - VOUCH_SESSION_NAME
    name: VouchSession
    # number of minutes for maximum session age, configuring how long the user has to login at their IdP (defaults to 5) - VOUCH_SESSION_MAXAGE
    maxAge: 5
    # key - a cryptographic string used to store the session variable - VOUCH_SESSION_KEY
    # if the key is not set here then it is generated at startup and stored in memory
    # Vouch Proxy complains if the string is less than 44 characters (256 bits as 32 base64 bytes)
    # you only want to set this if you're running multiple user facing vouch.yourdomain.com instances
    # where each instance may rely on a session cookie for state or the original requested URL
    # key: your_random_key


  headers:
    jwt: X-Vouch-Token                # VOUCH_HEADERS_JWT
    querystring: access_token         # VOUCH_HEADERS_QUERYSTRING
    redirect: X-Vouch-Requested-URI   # VOUCH_HEADERS_REDIRECT

    # GENERAL WARNING ABOUT claims AND tokens
    # all of these config elements can cause performance impacts due to the amount of information being 
    # moved around.  They will get added to the Vouch cookie and (possibly) make it large.  The Vouch cookie will 
    # get split up into several cookies. But if you need it, you need it.
    # With large cookies and headers it will require additional nginx config to open up the buffers a bit..
    # see `large_client_header_buffers` http://nginx.org/en/docs/http/ngx_http_core_module.html#large_client_header_buffers
    # and `proxy_buffer_size` http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_buffer_size

    # claims - a list of claims that will be stored in the JWT and passed down to applications via headers - VOUCH_HEADERS_CLAIMS
    # By default claims are sent down as headers with a prefix of X-Vouch-IdP-Claims-ClaimKey
    # Only when a claim is found in the user's info will the header exist.  This is optional.  These are case sensitive.
    claims:
      - groups
      - given_name
    # these will result in two headers being passed back to nginx as the headers
    #   X-Vouch-IdP-Claims-Groups: groupa, groupb, groupc
    #   X-Vouch-IdP-Claims-Given-Name: Robert
    # nginx will populate the variables
    #   $auth_resp_x_vouch_idp_claims_groups
    #   $auth_resp_x_vouch_idp_claims_given-name
    # see https://github.com/vouch/vouch-proxy/issues/183 regarding claims and header naming

    # claimheader - Customizable claim header prefix (instead of default `X-Vouch-IdP-Claims-`) - VOUCH_HEADERS_CLAIMHEADER
    # claimheader: My-Custom-Claim-Prefix

    # accesstoken - Pass the user's access token from the provider.  This is useful if you need to pass the IdP token to a downstream - VOUCH_HEADERS_ACCESSTOKEN
    # application. This is optional.
    # accesstoken: X-Vouch-IdP-AccessToken
    # idtoken - Pass the user's Id token from the provider.  This is useful if you need to pass this token to a downstream - VOUCH_HEADERS_IDTOKEN
    # application. This is optional.
    # idtoken: X-Vouch-IdP-IdToken

  # test_url - add this URL to the page which vouch displays during testing (a convenience for testing) - VOUCH_TESTURL
  test_url: http://yourdomain.com

  # post_logout_redirect_uris - VOUCH_POST_LOGOUT_REDIRECT_URIS
  # in order to prevent redirection attacks all redirected URLs to /logout must be specified
  # the URL must still be passed to Vouch Proxy as https://vouch.yourdomain.com/logout?url=${ONE OF THE URLS BELOW}
  # in line with the OIDC spec https://openid.net/specs/openid-connect-session-1_0.html#RedirectionAfterLogout
  post_logout_redirect_uris:
    # your apps login page
    - http://myapp.yourdomain.com/login
    # your IdPs logout enpoint
    # from https://accounts.google.com/.well-known/openid-configuration
    - https://oauth2.googleapis.com/revoke
    # you may be daisy chaining to your IdP
    - https://myorg.okta.com/oauth2/123serverid/v1/logout?post_logout_redirect_uri=http://myapp.yourdomain.com/login


#
# OAuth
#

# environmental variables for OAuth config:
#   provider:                OAUTH_PROVIDER
#   client_id:               OAUTH_CLIENT_ID
#   client_secret:           OAUTH_CLIENT_SECRET
#   auth_url:                OAUTH_AUTH_URL
#   token_url:               OAUTH_TOKEN_URL
#   end_session_endpoint:    OAUTH_END_SESSION_ENDPOINT
#   callback_url:            OAUTH_CALLBACK_URL
#   user_info_url:           OAUTH_USER_INFO_URL
#   user_team_url:           OAUTH_USER_TEAM_URL
#   user_org_url:            OAUTH_USER_ORG_URL
#   preferreddomain:         OAUTH_PREFERREDDOMAIN
#   callback_urls:           OAUTH_CALLBACK_URLS
#   scopes:                  OAUTH_SCOPES
#   claims:                  OAUTH_CLAIMS
#   code_challenge_method:   OAUTH_CODE_CHALLENGE_METHOD
#   relying_party_id         OAUTH_RELYING_PARTY_ID

#
# configure ONLY ONE of the following oauth providers
#

oauth:

  # Google
  provider: google
  # create new credentials at:
  # https://console.developers.google.com/apis/credentials
  client_id: 
  client_secret: 
  callback_urls:
    - http://vouch.yourdomain.com:9090/auth
    - http://vouch.yourotherdomain.com:9090/auth
  preferredDomain: yourdomain.com
  # optionally set scopes, defaults to 'email'
  # https://developers.google.com/identity/protocols/googlescopes#google_sign-in
  # scopes:
  #  - email

  # GitHub
  # https://developer.github.com/apps/building-integrations/setting-up-and-registering-oauth-apps/about-authorization-options-for-oauth-apps/
  provider: github
  client_id:
  client_secret:
  # callback_url is configured at github.com when setting up the app
  # Set to e.g. https://vouch.yourdomain.com/auth
  # defaults (uncomment and change these if you are using github enterprise on-prem)
  # auth_url: https://github.com/login/oauth/authorize
  # token_url: https://github.com/login/oauth/access_token
  # user_info_url: https://api.github.com/user?access_token=
  # scopes:
    # - user

  # Generic OpenID Connect
  provider: oidc
  client_id: 
  client_secret: 
  auth_url: https://{yourOktaDomain}/oauth2/default/v1/authorize
  token_url: https://{yourOktaDomain}/oauth2/default/v1/token
  user_info_url: https://{yourOktaDomain}/oauth2/default/v1/userinfo
  # end_session_endpoint is usually the IdP's logout URL
  # see https://github.com/vouch/vouch-proxy/pull/258
  end_session_endpoint: https://{yourOktaDomain}/oauth2/default/v1/logout
  scopes:
    - openid
    - email
    - profile
  callback_url: http://vouch.yourdomain.com:9090/auth
  # optionally set the "claims" request parameter (see https://openid.net/specs/openid-connect-core-1_0.html#ClaimsParameter)
  # required by Twitch, resolves issue https://github.com/vouch/vouch-proxy/issues/414
  # claims:
    # userinfo:
      # given_name:
        # essential: true
      # nickname: null
      # email:
        # essential: true
      # email_verified:
        # essential: true
      # picture: null
      # "http://example.info/claims/groups": null
    # id_token:
      # auth_time:
        # essential: true
      # acr:
        # values:
          # - "urn:mace:incommon:iap:silver"
  # PKCE method if enabled, S256 is currently supported (check https://www.oauth.com/oauth2-servers/pkce/)
  # resolves issue https://github.com/vouch/vouch-proxy/issues/303
  code_challenge_method: S256

  # IndieAuth
  # https://indielogin.com/api
  provider: indieauth
  client_id: http://yourdomain.com
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.yourdomain.com:9090/auth

  # adfs
  provider: adfs
  client_id:
  client_secret:
  auth_url: https://adfs.yourdomain.com/adfs/oauth2/authorize/
  token_url: https://adfs.yourdomain.com/adfs/oauth2/token/
  # vouch-proxy use RedirectURL as relying party identifier by default, if you want a custom one:
  # see https://github.com/vouch/vouch-proxy/issues/189
  # relying_party_id:  487d8ff7-80a8-4f62-b926-c2852ab06e94
  scopes:
    - openid
    - email
    - profile
  callback_url: https://vouch.yourdomain.com/auth


```

## File: `config/config.yml_example_adfs`
```
# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with adfs

vouch:
  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate to ADFS
  allowAllUsers: true

  cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    # secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    #  domain: yourdomain.com


oauth:
  provider: adfs
  client_id: k8s
  client_secret: sauceSecret
  auth_url: https://adfs.yourdomain.com/adfs/oauth2/authorize/
  token_url: https://adfs.yourdomain.com/adfs/oauth2/token/
  # vouch-proxy use RedirectURL as relying party identifier by default, if you want a custom one:
  # see https://github.com/vouch/vouch-proxy/issues/189
  # relying_party_id:  487d8ff7-80a8-4f62-b926-c2852ab06e94
  scopes:
    - openid
    - email
    - profile
  callback_url: https://vouch.yourdomain.com/auth
```

## File: `config/config.yml_example_azure`
```
# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with Azure AD
# https://github.com/vouch/vouch-proxy/issues/290

vouch:
  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate to Azure AD
  allowAllUsers: true

  cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    # secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    #  domain: yourdomain.com

oauth:
  provider: azure
  client_id: 123456789
  client_secret: ********
  auth_url: https://login.microsoftonline.com/.../oauth2/v2.0/authorize
  token_url: https://login.microsoftonline.com/.../oauth2/v2.0/token
  scopes:
    - openid
    - email
    - profile
  callback_url: https://vouch.yourdomain/auth
  azure_token: id_token # access_token and id_token supported
```

## File: `config/config.yml_example_discord`
```

# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with Discord as an OpenID Provider


vouch:
  domains:
    - yourdomain.com

  # whiteList is a list of usernames that will allow a login if allowAllUsers is false
  whiteList:
    # The default behavior matches the Discord user's username
    - loganintech

    # If the user still hasn't chosen a new username, the old username#discrimnator format will work
    - LoganInTech#1203

    # If discord_use_ids is set to true, you must use the user's ID
    - 12345678901234567

  cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com)
    secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    # domain: yourdomain.com

# https://discord.com/developers/docs/topics/oauth2
oauth:
  provider: discord
  client_id: xxxxxxxxxxxxxxxxxxxxxxxxxxxx
  client_secret: xxxxxxxxxxxxxxxxxxxxxxxx
  callback_url: http://vouch.yourdomain.com:9090/auth
  ## Uncomment this to match users based on their Discord ID
  # discord_use_ids: true
```

## File: `config/config.yml_example_gitea`
```

# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with Gitea

vouch:
  domains:
  - yourdomain.com

  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at Gitea
  # allowAllUsers: true

  # cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    # secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    # domain: yourdomain.com


oauth:
  # replace "gitea.yourdomain.com" with the domain your Gitea instance runs on
  # create a new OAuth application at:
  # https://gitea.yourdomain.com/user/settings/applications
  provider: oidc
  client_id: xxxxxxxxxxxxxxxxxxxx
  client_secret: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  auth_url: https://gitea.yourdomain.com/login/oauth/authorize
  token_url: https://gitea.yourdomain.com/login/oauth/access_token
  user_info_url: https://gitea.yourdomain.com/login/oauth/userinfo
  callback_url: https://yourdomain.com/auth
```

## File: `config/config.yml_example_github`
```

# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with github

vouch:
  # domains:
  # valid domains that the jwt cookies can be set into
  # the callback_urls will be to these domains
  # for github that's only one domain since they only allow one callback URL
  # https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#redirect-urls
  # each of these domains must serve the url https://login.$domains[0] https://login.$domains[1] ...
  domains:
  - yourothersite.io

  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at GitHub
  # allowAllUsers: true

  cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    #  domain: yourdomain.com


  # set teamWhitelist: to list of teams and/or GitHub organizations
  # When putting an organization id without a slash, it will allow all (public) members from the organization.
  # The client will try to read the private organization membership using the client credentials, if that's not possible
  # due to access restriction, it will try to evaluate the publicly visible membership.
  # Allowing members form a specific team can be configured by qualifying the team with the organization, separated by
  # a slash.
  # teamWhitelist:
  # - myOrg
  # - myOrg/myTeam
  # In case both vouch.teamWhitelist AND oauth.scopes is configured, make sure read:org scope is included

oauth:
  # create a new OAuth application at:
  # https://github.com/settings/applications/new
  #
  # callback_url is configured at github.com when setting up the app
  # Set to e.g. https://vouch.yourdomain.com/auth or https://yourdomain.com/vp_in_a_path/auth
  provider: github
  client_id: xxxxxxxxxxxxxxxxxxxx
  client_secret: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  # endpoints set from https://godoc.org/golang.org/x/oauth2/github
```

## File: `config/config.yml_example_github_enterprise`
```
# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with github enterprise
# see config.yml_example for all options

vouch:
  # domains:
  # valid domains that the jwt cookies can be set into
  # each of these domains must serve the url https://login.$domains[0] https://login.$domains[1] ...
  # the callback_urls will be to these domains
  domains:
  - yourdomain.com
  - yourothersite.io

  # - OR -
  # instead of setting specific domains you may prefer to allow all users...
  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at the configured provider
  # allowAllUsers: true

  cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    #  domain: yourdomain.com


  # set teamWhitelist: to list of teams and/or GitHub organizations
  # When putting an organization id without a slash, it will allow all (public) members from the organization.
  # The client will try to read the private organization membership using the client credentials, if that's not possible
  # due to access restriction, it will try to evaluate the publicly visible membership.
  # Allowing members form a specific team can be configured by qualifying the team with the organization, separated by
  # a slash.
  # teamWhitelist:
  # - myOrg
  # - myOrg/myTeam
  # In case both vouch.teamWhitelist AND oauth.scopes is configured, make sure read:org scope is included

oauth:
  # create a new OAuth application at:
  # https://githubenterprise.yourdomain.com/settings/applications/new
  provider: github
  client_id: xxxxxxxxxxxxxxxxxxxx
  client_secret: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  auth_url: https://githubenterprise.yourdomain.com/login/oauth/authorize
  token_url: https://githubenterprise.yourdomain.com/login/oauth/access_token
  user_info_url: https://githubenterprise.yourdomain.com/api/v3/user?access_token=
  # relevant only if teamWhitelist is configured; colon-prefixed parts are parameters that
  # will be replaced with the respective values.
  user_team_url: https://githubenterprise.yourdomain.com/api/v3/orgs/:org_id/teams/:team_slug/memberships/:username?access_token=
  user_org_url: https://githubenterprise.yourdomain.com/api/v3/orgs/:org_id/members/:username?access_token=
  # these GitHub OAuth defaults are set for you..
  # scopes:
  #   - user
  # In case both vouch.teamWhitelist AND oauth.scopes is configured, make sure read:org scope is included
```

## File: `config/config.yml_example_gitlab_ce`
```
# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with GitLab CE Authentication

vouch:
  # domains:
  # valid domains that the jwt cookies can be set into
  # the callback_urls will be to these domains
  domains:
  - yourdomain.com
  - yourotherdomain.com

  # - OR -
  # instead of setting specific domains you may prefer to allow all users...
  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at the configured provider
  # allowAllUsers: true

  cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    # domain: yourdomain.com

oauth:
  # Create a new global or group application and paste the id and the secret
  provider: oidc
  client_id: xxxxxxxxxxxxxxxxxxxxxxxxxxxx
  client_secret: xxxxxxxxxxxxxxxxxxxxxxxx
  scopes:
    - openid
    - email
    - profile
  auth_url:      https://gitlab.yourdomain.com/oauth/authorize
  token_url:     https://gitlab.yourdomain.com/oauth/token
  user_info_url: https://gitlab.yourdomain.com/oauth/userinfo
  callback_url:  http://vouch.yourdomain.com:9090/auth
```

## File: `config/config.yml_example_google`
```

# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with google

vouch:
  domains:
  - yourdomain.com
  - yourotherdomain.com

  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate with Google
  # allowAllUsers: true

  cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    #  domain: yourdomain.com


oauth:
  provider: google
  # get credentials from...
  # https://console.developers.google.com/apis/credentials
  client_id: xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com
  client_secret: xxxxxxxxxxxxxxxxxxxxxxxx
  # Google may require callback_urls (redirect URIs) to be 'https'
  callback_urls: 
    - https://yourdomain.com:9090/auth
    - https://yourotherdomain.com:9090/auth
  preferredDomain: yourdomain.com # be careful with this option, it may conflict with chrome on Android 
  # endpoints are set from https://godoc.org/golang.org/x/oauth2/google
```

## File: `config/config.yml_example_homeassistant`
```
# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with HomeAssistant

vouch:
  # logLevel: debug
  logLevel: info
  
  # domains:
  # valid domains that the jwt cookies can be set into
  # the callback_urls will be to these domains
  domains:
  - yourdomain.com

  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at Gitea
  # allowAllUsers: true

  # cookie:
    # secure: false           # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    # domain: yourdomain.com  # vouch.cookie.domain must be set when enabling allowAllUsers


  # whiteList - (optional) allows only the listed usernames
  # usernames are usually email addresses (google, most oidc providers) or login/username for github and github enterprise
  # using static value for HomeAssistant
  whiteList:
  - homeassistant

oauth:
  # HomeAssistant Auth
  # HomeAssistant typically uses a port in the url (8123 by default) and this maybe required for the auth_url and token_url 
  # depending on your setup of HA
  # https://developers.home-assistant.io/docs/en/auth_api.html
  provider: homeassistant
  client_id: https://vouch.yourdomain.com
  callback_url: https://vouch.yourdomain.com/auth
  auth_url: https://homeassistant.yourdomain.com:port/auth/authorize
  token_url: https://homeassistant.yourdomain.com:port/auth/token
```

## File: `config/config.yml_example_indieauth`
```

# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with IndieAuth

vouch:
  # domains:
  # valid domains that the jwt cookies can be set into
  # the callback_urls will be to these domains
  # domains:
  # - yourdomain.com

  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at the configured provider
  allowAllUsers: true

  cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    # domain: yourdomain.com

  # Setting publicAccess: true will accept all requests, even without a cookie. 
  publicAccess: true

oauth:
  # IndieAuth
  # https://indielogin.com/api
  provider: indieauth
  client_id: http://yourdomain.com
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.yourdomain.com:9090/auth
```

## File: `config/config.yml_example_keycloak`
```

# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with Keycloak

vouch:
  domains:
  - yourdomain.com

  # - OR -
  # instead of setting specific domains you may prefer to allow all users...
  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at the configured provider
  # and set vouch.cookie.domain to the domain you wish to protect
  # allowAllUsers: true

  cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    # domain: yourdomain.com

oauth:
  # Generic OpenID Connect
  # for Keycloak
  provider: oidc
  client_id: xxxxxxxxxxxxxxxxxxxxxxxxxxxx
  client_secret: xxxxxxxxxxxxxxxxxxxxxxxx
  auth_url: https://{yourKeycloakDomain}/realms/{yourKeycloakRealm}/protocol/openid-connect/auth
  token_url: https://{yourKeycloakDomain}/realms/{yourKeycloakRealm}/protocol/openid-connect/token
  user_info_url: https://{yourKeycloakDomain}/realms/{yourKeycloakRealm}/protocol/openid-connect/userinfo
  scopes:
    - openid
    - email
    - profile
  callback_url: http://vouch.yourdomain.com:9090/auth
  # you can get values of of auth_url, token_url and user_info_url from https://{yourKeycloakDomain}/realms/{yourKeycloakRealm}/.well-known/openid-configuration
  # When configuring client in Keycloak, you should use following values
  ## valid redirect: http://vouch.yourdomain.com:9090/auth
  ## valid logout: http://vouch.yourdomain.com:9090/logout
  ## web origin: http://vouch.yourdomain.com:9090
```

## File: `config/config.yml_example_nextcloud`
```

# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with Nextcloud Authentication

vouch:
  # domains:
  # valid domains that the jwt cookies can be set into
  # the callback_urls will be to these domains
  domains:
  - yourdomain.com
  - yourotherdomain.com

  # - OR -
  # instead of setting specific domains you may prefer to allow all users...
  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at the configured provider
  # allowAllUsers: true

  cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    # domain: yourdomain.com

oauth:
  # This assumes usage of pretty URLs otherwise add /index.php/
  # to start of URL path
  provider: nextcloud
  client_id: xxxxxxxxxxxxxxxxxxxxxxxxxxxx
  client_secret: xxxxxxxxxxxxxxxxxxxxxxxx
  auth_url: https://nextcloud.yourdomain.com/apps/oauth2/authorize
  token_url: https://nextcloud.yourdomain.com/apps/oauth2/api/v1/token
  user_info_url: https://nextcloud.yourdomain.com/ocs/v2.php/cloud/user?format=json
  scopes:
    - openid
    - email
    - profile
  callback_url: http://vouch.yourdomain.com:9090/auth
```

## File: `config/config.yml_example_oidc`
```

# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with OpenID Connect (such as okta)

vouch:
  # domains:
  # valid domains that the jwt cookies can be set into
  # the callback_urls will be to these domains
  domains:
  - yourdomain.com
  - yourotherdomain.com

  # - OR -
  # instead of setting specific domains you may prefer to allow all users...
  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at the configured provider
  # and set vouch.cookie.domain to the domain you wish to protect
  # allowAllUsers: true

  cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    # domain: yourdomain.com

oauth:
  # Generic OpenID Connect
  # including okta
  provider: oidc
  client_id: xxxxxxxxxxxxxxxxxxxxxxxxxxxx
  client_secret: xxxxxxxxxxxxxxxxxxxxxxxx
  auth_url: https://{yourOktaDomain}/oauth2/default/v1/authorize
  token_url: https://{yourOktaDomain}/oauth2/default/v1/token
  user_info_url: https://{yourOktaDomain}/oauth2/default/v1/userinfo
  scopes:
    - openid
    - email
    - profile
  callback_url: http://vouch.yourdomain.com:9090/auth
```

## File: `config/config.yml_example_pocket-id`
```

# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with pocket-id

# Pocket ID
# https://pocket-id.org
# https://github.com/pocket-id/pocket-id

vouch:
  # domains:
  # valid domains that the jwt cookies can be set into
  # the callback_urls will be to these domains
  domains:
  - yourdomain.com
  - yourotherdomain.com

  # - OR -
  # instead of setting specific domains you may prefer to allow all users...
  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at the configured provider
  # and set vouch.cookie.domain to the domain you wish to protect
  # allowAllUsers: true

  cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    # domain: yourdomain.com

oauth:
  # pocket-id
  provider: oidc
  client_id: xxxxxxxxxxxxxxxxxxxxxxxxxxxx
  client_secret: xxxxxxxxxxxxxxxxxxxxxxxx
  auth_url: https://{yourPocketIdDomain}/authorize
  token_url: https://{yourPocketIdDomain}/api/oidc/token
  user_info_url: https://{yourPocketIdDomain}/api/oidc/userinfo
  scopes:
    - openid
    - email
    - profile
  callback_url: http://vouch.{yourdomain.com}/auth
```

## File: `config/config.yml_example_scopes_and_claims`
```
vouch:
  # .... domain configuration goes here

  headers:   
    # The idtoken is used for debugging during configuration
    # use the idtoken to make sure the oauth provider returns the necessary claims
    idtoken: X-Vouch-IdP-IdToken

    # make sure to list all the claims you need
    # Note: they will be stored in the cookie AND header and get sent with each request
    claims:
      - sub
      - name
      - email
      - email_verified

oauth:
  # .... your provider config goes here
  scopes:
    # make sure to set the required scopes
    - openid
    - email
    - profile
```

## File: `config/config.yml_example_secureauth`
```

# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with SecureAuth OpenID Connect

vouch:
  domains:
  - yourdomain.com

  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at Gitea
  # allowAllUsers: true

  # cookie:
    # secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    # domain: yourdomain.com

oauth:
  # SecureAuth OpenID Connect
  provider: oidc
  client_id: XXXXXXXXXXXXXXX
  client_secret: XXXXXXXXXXXXXXXXXXXXXX
  auth_url: https://<SecureAuth FQDN>/SecureAuth<XX>/SecureAuth.aspx
  token_url: https://<SecureAuth FQDN>/SecureAuth<XX>/OidcToken.aspx
  user_info_url: https://<SecureAuth FQDN>/SecureAuth<XX>/OidcUserInfo.aspx
  scopes:
    - openid
    - email
    - profile
  # callback_url needs to be set as a "redirect url" on the SecureAuth Post Auth tab 
  callback_url: https://<vouch>.<domain.com>/auth 
```

## File: `config/config.yml_example_slack`
```

# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with Slack

vouch:
  domains:
  - yourdomain.com

  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at Gitea
  # allowAllUsers: true

  # cookie:
    # secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    # domain: yourdomain.com


oauth:
  # create a new OAuth application at:
  # https://api.slack.com/apps
  # use the manifest at `examples/slack/vouch-slack-oidc-app-manifest.yml`
  # but be sure to match the `callback_url`'s below to the `redirect_urls` in the manifest
  # then install the new app to your slack instance
  provider: oidc
  # careful! the slack client_id must be single quoted so that the yaml parser 
  # doesn't interpret it as a number (because yaml is actually javascript)
  client_id: 'xxxxxxxxxxxxxxx.xxxxxxxxxxxxxxxxx'
  client_secret: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  callback_url: https://vouch.yourdomain.com/auth  
  # from https://slack.com/.well-known/openid-configuration
  auth_url: https://slack.com/openid/connect/authorize
  token_url: https://slack.com/api/openid.connect.token
  user_info_url: https://slack.com/api/openid.connect.userInfo
```

## File: `config/config.yml_example_twitch`
```

# Vouch Proxy configuration
# bare minimum to get Vouch Proxy running with Twitch

vouch:
  # domains:
  # valid domains that the jwt cookies can be set into
  # the callback_urls will be to these domains
  domains:
  - yourdomain.com
  - yourotherdomain.com

  # - OR -
  # instead of setting specific domains you may prefer to allow all users...
  # set allowAllUsers: true to use Vouch Proxy to just accept anyone who can authenticate at the configured provider
  # and set vouch.cookie.domain to the domain you wish to protect
  # allowAllUsers: true

  cookie:
    # allow the jwt/cookie to be set into http://yourdomain.com (defaults to true, requiring https://yourdomain.com) 
    # secure: false
    # vouch.cookie.domain must be set when enabling allowAllUsers
    # domain: yourdomain.com

oauth:
  # Generic OpenID Connect
  provider: oidc
  client_id: xxxxxxxxxxxxxxxxxxxxxxxxxxxx
  client_secret: xxxxxxxxxxxxxxxxxxxxxxxx
  auth_url: https://id.twitch.tv/oauth2/authorize
  token_url: https://id.twitch.tv/oauth2/token
  user_info_url: https://id.twitch.tv/oauth2/userinfo
  callback_url: https://vouch.yourdomain.com/auth
  scopes:
    - openid
    - user:read:email
  # Twitch uses the claims parameter to configure the information returned via `user_info_url`
  claims:
    userinfo:
      email:
        essential: true
      email_verified:
        essential: true
```

## File: `config/testing/handler_allowallusers.yml`
```yaml
vouch:
  allowAllUsers: true

  jwt:
    secret: testingsecret

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/handler_claims.yml`
```yaml
vouch:
  testing: true
  logLevel: debug
  listen: 0.0.0.0
  port: 9090

  allowAllUsers: true

  headers:
    claims:
      - groups
      - boolean_claim
      - family_name
      - http://www.example.com/favorite_color

  cookie:
    name: vouchTestingCookie

  session:
    name: VouchTestingSession

  jwt:
    secret: testing

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/handler_email.yml`
```yaml
vouch:
  logLevel: error
  domains:
    - example.com

  jwt:
    secret: testingsecret

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/handler_login_redirecturls.yml`
```yaml
vouch:
  domains:
    - example.com
    - other.com

  cookie:
    secure: false

  jwt:
    secret: testingsecret

oauth:
  provider: google
  client_id: 1234567
  client_secret: testingsecret
  auth_url: https://indielogin.com/auth
  callback_urls:
    - http://vouch.example.com:9090/auth
    - http://vouch.other.com:9090/auth
```

## File: `config/testing/handler_login_url.yml`
```yaml
vouch:
  domains:
    - example.com

  cookie:
    secure: false
    domain: example.com

  jwt:
    secret: testingsecret

oauth:
  provider: google
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/handler_login_url_document_root.yml`
```yaml
vouch:
  document_root: /vouch_in_a_path
  domains:
    - example.com

  cookie:
    secure: false
    domain: example.com

  jwt:
    secret: testingsecret

oauth:
  provider: google
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/handler_logout_provider.yml`
```yaml
vouch:
  domains:
    - example.com

  cookie:
    secure: false

  jwt:
    secret: testingsecret

  post_logout_redirect_uris:
    - http://myapp.example.com/login
    # https://accounts.google.com/.well-known/openid-configuration
    - https://oauth2.googleapis.com/revoke

oauth:
  provider: google
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
  end_session_endpoint: https://indielogin.com/logout
```

## File: `config/testing/handler_logout_url.yml`
```yaml
vouch:
  domains:
    - example.com

  cookie:
    secure: false

  jwt:
    secret: testingsecret

  post_logout_redirect_uris:
    - http://myapp.example.com/login
    # https://accounts.google.com/.well-known/openid-configuration
    - https://oauth2.googleapis.com/revoke

oauth:
  provider: google
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/handler_nodomains.yml`
```yaml
vouch:
  jwt:
    secret: testingsecret

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/handler_teams.yml`
```yaml
vouch:
  logLevel: debug
  domains:
    - example.com

  teamWhitelist:
    - "org1/team1"
    - "org1/team2"

  jwt:
    secret: testingsecret

oauth:
  provider: github
  client_id: fake
  auth_url: fake
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/handler_whitelist.yml`
```yaml
vouch:
  logLevel: debug
  domains:
    - example.com

  whiteList:
    - test@example.com

  jwt:
    secret: testingsecret

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/jwtmanager_has_idp_token_claims.yml`
```yaml
vouch:
  testing: true
  logLevel: debug
  listen: 0.0.0.0
  port: 9090

  allowAllUsers: true

  headers:
    claims:
      - groups
      - boolean_claim
      - family_name
      - http://www.example.com/favorite_color
    accesstoken: X-Vouch-IdP-AccessToken
    idtoken: X-Vouch-IdP-IdToken

  cookie:
    name: vouchTestingCookie

  session:
    name: VouchTestingSession

  jwt:
    secret: testing

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/logging_debug.yml`
```yaml
vouch:
  logLevel: debug
  allowAllUsers: true

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/logging_error.yml`
```yaml
vouch:
  logLevel: error
  allowAllUsers: true

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/logging_info.yml`
```yaml
vouch:
  logLevel: info
  allowAllUsers: true

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/logging_warn.yml`
```yaml
vouch:
  logLevel: warn
  allowAllUsers: true

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/minimal.yml`
```yaml
vouch:
  allowAllUsers: true

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/socket_basic.yml`
```yaml
vouch:
  listen: unix:/fake/path/to/socket

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/socket_mode.yml`
```yaml
vouch:
  listen: unix:/fake/path/to/socket
  socket_mode: 0644

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/test_config.yml`
```yaml
vouch:
  logLevel: debug
  listen: 0.0.0.0
  port: 9090
  domains:
    - vouch.github.io

  whiteList:
    - bob@yourdomain.com
    - alice@yourdomain.com
    - joe@yourdomain.com

  cookie:
    name: vouchTestingCookie

  session:
    name: VouchTestingSession

  jwt:
    secret: testingsecret

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `config/testing/test_config_oauth_claims.yml`
```yaml
vouch:
  logLevel: debug
  listen: 0.0.0.0
  port: 9090
  domains:
    - vouch.github.io

  whiteList:
    - bob@yourdomain.com
    - alice@yourdomain.com
    - joe@yourdomain.com

  cookie:
    name: vouchTestingCookie

  session:
    name: VouchTestingSession

  jwt:
    secret: testingsecret

oauth:
  provider: oidc
  auth_url: https://oauth2.example.info/authorize
  token_url: https://oauth2.example.info/token
  user_info_url: https://oauth2.example.info/userinfo
  scopes:
    - openid
    - email
    - profile
  claims:
    userinfo:
      given_name:
        essential: true
      nickname: null
      email:
        essential: true
      email_verified:
        essential: true
      picture: null
      "http://example.info/claims/groups": null
    id_token:
      auth_time:
        essential: true
      acr:
        values:
          - "urn:mace:incommon:iap:silver"
  callback_url: https://vouch.yourdomain.com:9090/auth
```

## File: `config/testing/test_config_rsa.yml`
```yaml
vouch:
  logLevel: debug
  listen: 0.0.0.0
  port: 9090
  domains:
    - vouch.github.io

  whiteList:
    - bob@yourdomain.com
    - alice@yourdomain.com
    - joe@yourdomain.com

  cookie:
    name: vouchTestingCookie

  session:
    name: VouchTestingSession

  jwt:
    signing_method: RS512
    private_key_file: config/testing/rsa.key
    public_key_file: config/testing/rsa.pub

oauth:
  provider: indieauth
  client_id: http://vouch.github.io
  auth_url: https://indielogin.com/auth
  callback_url: http://vouch.github.io:9090/auth
```

## File: `examples/OpenResty/README.md`
```markdown
# Advanced Authorization Using OpenResty

## What is OpenResty?
OpenResty® is a full-fledged web platform that integrates the standard Nginx core, LuaJIT, many carefully written Lua libraries, lots of high quality 3rd-party Nginx modules, and most of their external dependencies.

## Instructions

You can replace nginx with OpenResty very easily. OpenResty installation documents can be found [here](https://openresty.org/en/installation.html).

The following configuration files demonstrate a front-end proxy with multiple backend applications that are authenticated using various methods.

| File                              | Description |
| :---                              | :---        |
| conf/nginx.conf                   | Only the generic nginx config without any 'server' fields.  It includes anything at ../conf.d/*.conf |
| lua/group_auth.lua                | A lua file that validates a list of groups against the values in X-Vouch-IdP-Claims-Groups. |
| lua/user_auth.lua                 | A lua file that validates a list of users against the value in X-Vouch-User. |
| conf.d/app1.yourdomain.com.conf   | Configuration for an authenticated application at https://app1.yourdomain.com.  Uses user authorization. |
| conf.d/app2.yourdomain.com.conf   | Configuration for an authenticated application at https://app2.yourdomain.com.  Uses group authorization.  This file can be duplicated for every application you'd like to deploy. |
| conf.d/unauthenticated_app3.yourdomain.com.conf | A simple configuration for an unauthenticated application or page.  This could be a terms of service, license, or generic help page.  It could also be some application or API endpoint that you simply don't want to authenticate.  |
| conf.d/vouch.yourdomain.com.conf  | Configuration for exposing vouch at the proxy using https to a vouch instance on localhost.  This configuration supports secure cookies. |

With OpenResty and Lua it is possible to provide customized and advanced authorization on any header or claims vouch passes down.
```

## File: `examples/OpenResty/conf/nginx.conf`
```
user  nobody;
worker_processes  2;

error_log  /var/log/nginx/error.log warn;
pid       logs/nginx.pid;

events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;
    lua_code_cache off;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log   /var/log/nginx/access.log  main;

    sendfile        on;

    keepalive_timeout  65;
    init_by_lua_block {
      -- Function to find a key in a table
      function tableHasKey(table,key)
        return table[key] ~= nil
      end
      -- Function to turn a table with only values into a k=>v table
      function Set (list)
        local set = {}
        for _, l in ipairs(list) do set[l] = true end
          return set
        end
    }

    include ../conf.d/*.conf;
}
```

## File: `examples/OpenResty/conf.d/app1.yourdomain.com.conf`
```
server {
    listen 443 ssl http2;
    server_name app1.yourdomain.com;
    root /var/www/html/;

    ssl_certificate /etc/letsencrypt/live/app1.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/app1.yourdomain.com/privkey.pem;

    # send all requests to the `/validate` endpoint for authorization
    auth_request /validate;

    location = /validate {
      # Vouch Proxy can run behind the same Nginx reverse proxy
      # may need to comply to "upstream" server naming
      proxy_pass https://vouch.yourdomain.com:9090/validate;

      # be sure to pass the original host header
      proxy_set_header Host $http_host;

      # Vouch Proxy only acts on the request headers
      proxy_pass_request_body off;
      proxy_set_header Content-Length "";

      # optionally add X-Vouch-User as returned by Vouch Proxy along with the request
      auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;

      # optionally add X-Vouch-IdP-Claims-* custom claims you are tracking
      #    auth_request_set $auth_resp_x_vouch_idp_claims_groups $upstream_http_x_vouch_idp_claims_groups;
      #    auth_request_set $auth_resp_x_vouch_idp_claims_given_name $upstream_http_x_vouch_idp_claims_given_name;
      # optinally add X-Vouch-IdP-AccessToken or X-Vouch-IdP-IdToken
      #    auth_request_set $auth_resp_x_vouch_idp_accesstoken $upstream_http_x_vouch_idp_accesstoken;
      #    auth_request_set $auth_resp_x_vouch_idp_idtoken $upstream_http_x_vouch_idp_idtoken;

      # these return values are used by the @error401 call
      auth_request_set $auth_resp_jwt $upstream_http_x_vouch_jwt;
      auth_request_set $auth_resp_err $upstream_http_x_vouch_err;
      auth_request_set $auth_resp_failcount $upstream_http_x_vouch_failcount;
    }

    # if validate returns `401 not authorized` then forward the request to the error401block
    error_page 401 = @error401;

    location @error401 {
        # redirect to Vouch Proxy for login
        return 302 https://vouch.yourdomain.com/login?url=$scheme://$http_host$request_uri&vouch-failcount=$auth_resp_failcount&X-Vouch-Token=$auth_resp_jwt&error=$auth_resp_err;
    }

    # proxy pass authorized requests to your service
    location / {
      proxy_pass http://app1-private.yourdomain.com:8080;
      #  may need to set
      #    auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;
      #    auth_request_set $auth_resp_x_vouch_idp_claims_groups $upstream_http_x_vouch_idp_claims_groups;
      #    auth_request_set $auth_resp_x_vouch_idp_claims_given_name $upstream_http_x_vouch_idp_claims_given_name;

      # set user header (usually an email)
      proxy_set_header X-Vouch-User $auth_resp_x_vouch_user;
      # optionally pass any custom claims you are tracking
      #     proxy_set_header X-Vouch-IdP-Claims-Groups $auth_resp_x_vouch_idp_claims_groups;
      #     proxy_set_header X-Vouch-IdP-Claims-Given_Name $auth_resp_x_vouch_idp_claims_given_name;
      # optionally pass the accesstoken or idtoken
      #     proxy_set_header X-Vouch-IdP-AccessToken $auth_resp_x_vouch_idp_accesstoken;
      #     proxy_set_header X-Vouch-IdP-IdToken $auth_resp_x_vouch_idp_idtoken;

      # Authenticate the application by user
      access_by_lua_file  lua/user_auth.lua;
    }
}
```

## File: `examples/OpenResty/conf.d/app2.yourdomain.com.conf`
```
server {
    listen 443 ssl http2;
    server_name app2.yourdomain.com;
    root /var/www/html/;

    ssl_certificate /etc/letsencrypt/live/app2.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/app2.yourdomain.com/privkey.pem;

    # send all requests to the `/validate` endpoint for authorization
    auth_request /validate;

    location = /validate {
      # Vouch Proxy can run behind the same Nginx reverse proxy
      # may need to comply to "upstream" server naming
      proxy_pass https://vouch.yourdomain.com/validate;

      # be sure to pass the original host header
      proxy_set_header Host $http_host;

      # Vouch Proxy only acts on the request headers
      proxy_pass_request_body off;
      proxy_set_header Content-Length "";

      # optionally add X-Vouch-User as returned by Vouch Proxy along with the request
      auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;

      # optionally add X-Vouch-IdP-Claims-* custom claims you are tracking
      auth_request_set $auth_resp_x_vouch_idp_claims_groups $upstream_http_x_vouch_idp_claims_group;
      #    auth_request_set $auth_resp_x_vouch_idp_claims_given_name $upstream_http_x_vouch_idp_claims_given_name;
      # optinally add X-Vouch-IdP-AccessToken or X-Vouch-IdP-IdToken
      #    auth_request_set $auth_resp_x_vouch_idp_accesstoken $upstream_http_x_vouch_idp_accesstoken;
      #    auth_request_set $auth_resp_x_vouch_idp_idtoken $upstream_http_x_vouch_idp_idtoken;

      # these return values are used by the @error401 call
      auth_request_set $auth_resp_jwt $upstream_http_x_vouch_jwt;
      auth_request_set $auth_resp_err $upstream_http_x_vouch_err;
      auth_request_set $auth_resp_failcount $upstream_http_x_vouch_failcount;
    }

    # if validate returns `401 not authorized` then forward the request to the error401block
    error_page 401 = @error401;

    location @error401 {
        # redirect to Vouch Proxy for login
        return 302 https://vouch.yourdomain.com/login?url=$scheme://$http_host$request_uri&vouch-failcount=$auth_resp_failcount&X-Vouch-Token=$auth_resp_jwt&error=$auth_resp_err;
    }

    # proxy pass authorized requests to your service
    location / {
      proxy_pass http://app2-private.yourdomain.com:8080;
      #  may need to set
      #    auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;
      #    auth_request_set $auth_resp_x_vouch_idp_claims_groups $upstream_http_x_vouch_idp_claims_groups;
      #    auth_request_set $auth_resp_x_vouch_idp_claims_given_name $upstream_http_x_vouch_idp_claims_given_name;

      # set user header (usually an email)
      proxy_set_header X-Vouch-User $auth_resp_x_vouch_user;
      # optionally pass any custom claims you are tracking
      proxy_set_header X-Vouch-IdP-Claims-Groups $auth_resp_x_vouch_idp_claims_group;
      #     proxy_set_header X-Vouch-IdP-Claims-Given_Name $auth_resp_x_vouch_idp_claims_given_name;
      # optionally pass the accesstoken or idtoken
      #     proxy_set_header X-Vouch-IdP-AccessToken $auth_resp_x_vouch_idp_accesstoken;
      #     proxy_set_header X-Vouch-IdP-IdToken $auth_resp_x_vouch_idp_idtoken;

      # Authenticate the application by group
      access_by_lua_file  lua/group_auth.lua;
    }
}
```

## File: `examples/OpenResty/conf.d/unauthenticated_app3.yourdown.com.conf`
```
server {
    listen 443 ssl http2;
    server_name app3.yourdomain.com;
    root /var/www/html/;

    ssl_certificate /etc/letsencrypt/live/app3.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/app3.yourdomain.com/privkey.pem;


    # This application is simply proxy-passed without any authentication
    location / {
      proxy_pass http://app3-private.yourdomain.com:8080;
    }
}
```

## File: `examples/OpenResty/conf.d/vouch.yourdomain.com.conf`
```
server {
    # Setting vouch behind SSL allows you to use the Secure flag for cookies.
    listen 443 ssl http2;
    server_name vouch.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/vouch.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/vouch.yourdomain.com/privkey.pem;

    location / {
       proxy_pass http://127.0.0.1:9090;
       # be sure to pass the original host header
       proxy_set_header Host vouch.yourdomain.com;
    }
}
```

## File: `examples/OpenResty/lua/group_auth.lua`
```
-- ==============================
--     Group Authentication
--    via X-Vouch-IdP-Groups
-- ==============================
-- Function to turn a table with only values into a k=>v table
function Set (list)
    local set = {}
    for _, l in ipairs(list) do set[l] = true end
    return set
end
-- Function to find a key in a table
function tableHasKey(table,key)
    return table[key] ~= nil
end
-- Validate that a user is in a group
local authorized_groups = Set {
    "CN=Domain Users,CN=Users,DC=Contoso,DC=com",
    "CN=Website Users,CN=Users,DC=Contoso,DC=com"
}
-- Verify the variable exists
if ngx.var.auth_resp_x_vouch_idp_claims_groups then
    -- Check if the found user is in the allowed_users table
    local cjson = require("cjson")
    local groups = cjson.decode("[" .. ngx.var.auth_resp_x_vouch_idp_claims_groups .. "]")
    local found = false
    -- Parse the groups and check if they match any of our authorized groups
    for i, group in ipairs(groups) do
        if tableHasKey(authorized_groups, group) then
            -- If we found an authorized group, say so and break the loop
            found = true
            break
        end
    end
    -- If we didn't find out group in our list, then return forbidden
    if not found then
        -- If not, throw a forbidden
        ngx.exit(ngx.HTTP_FORBIDDEN)
    end
else
    -- Throw forbidden if variable doesn't exist
    ngx.exit(ngx.HTTP_FORBIDDEN)
end
```

## File: `examples/OpenResty/lua/user_auth.lua`
```
-- ==============================
--     User Authentication
--      via X-Vouch-User
-- ==============================
-- Function to turn a table with only values into a k=>v table
function Set (list)
    local set = {}
    for _, l in ipairs(list) do set[l] = true end
    return set
end
-- Function to find a key in a table
function tableHasKey(table,key)
    return table[key] ~= nil
end
-- Validate a user in nginx, instead of vouch
local authorized_users = Set {
    "my@account.com",
    "friend@gmail.com"
}
-- Verify the variable exists
if ngx.var.auth_resp_x_vouch_user then
    -- Check if the found user is in the authorized_users table
    if not tableHasKey(authorized_users, ngx.var.auth_resp_x_vouch_user) then
        -- If not, throw a forbidden
        ngx.exit(ngx.HTTP_FORBIDDEN)
    end
else
    -- Throw forbidden if variable doesn't exist
    ngx.exit(ngx.HTTP_FORBIDDEN)
end
```

## File: `examples/nginx/README.md`
```markdown
# NGINX Examples

Nginx can be used for most deployments of Vouch Proxy.  Nginx is always an appropriate choice unless you wan to do advanced authorization of users based on information being returned from Vouch Proxy.

## Configuration Examples

### Single-File
Use the single file examples when you only have one or a small number of applications you would like to proxy.  The single file examples are simple and easy to implement.

### Multi-File
Use the multi-file examples if you want to better organize your configuration files and make it easier to add/remove proxied applications.
```

## File: `examples/nginx/nginx_scopes_and_claims.conf`
```
server {
  listen       80;
  server_name  mydomain.com;

  location ^~ /sso/validate {
    proxy_pass http://vouch:9090/validate;
    proxy_set_header Host $http_host;
    proxy_pass_request_body off;
  }

  location ^~ /api/v1/ {
    auth_request /sso/validate;
    
    # get the claim/s into a local nginx variable
    auth_request_set $sub       $upstream_http_x_vouch_idp_claims_sub;
    auth_request_set $email     $upstream_http_x_vouch_idp_claims_email;
    auth_request_set $verified  $upstream_http_x_vouch_idp_claims_email_verified;

    # forward the claim to the proxied server
    proxy_set_header X-sub              $sub;
    proxy_set_header X-email            $email;
    proxy_set_header X-email-verified   $verified;

    # generic proxy headers
    proxy_set_header Host $http_host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;

    proxy_redirect off;
    proxy_buffering off;
    proxy_pass http://api./;
  }
}
```

## File: `examples/nginx/multi-file/README.md`
```markdown
# Nginx Multi-File Configuration Example

Nginx can be configured to include conf files, allowing you to properly organize nginx configurations into individual apps.  This keeps configurations cleaner and easier to manage.

| File                      | Description |
| :---                      | :---        |
| nginx.conf                | Only the generic nginx config without any 'server' fields.  It includes anything at conf.d/*.conf |
| conf.d/app1.yourdomain.com.conf | Configuration for an authenticated application at https://app1.yourdomain.com |
| conf.d/app2.yourdomain.com.conf | Configuration for an authenticated application at https://app2.yourdomain.com.  This file can be duplicated for every application you'd like to deploy. |
| conf.d/unauthenticated_app3.yourdomain.com.conf | A simple configuration for an unauthenticated application or page.  This could be a terms of service, license, or generic help page.  It could also be some application or API endpoint that you simply don't want to authenticate.  |
| conf.d/vouch.yourdomain.com.conf | Configuration for exposing vouch at the proxy using https to a vouch instance on localhost.  This configuration supports secure cookies. | 
```

## File: `examples/nginx/multi-file/nginx.conf`
```
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}


http {
    resolver 127.0.0.1;
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    # This line allows you to keep separate configs for multiple applications in a different folder.
    include /etc/nginx/conf.d/*.conf;
}
```

## File: `examples/nginx/multi-file/conf.d/app1.yourdomain.com.conf`
```
server {
    listen 443 ssl http2;
    server_name app1.yourdomain.com;
    root /var/www/html/;

    ssl_certificate /etc/letsencrypt/live/app1.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/app1.yourdomain.com/privkey.pem;

    # send all requests to the `/validate` endpoint for authorization
    auth_request /validate;

    location = /validate {
      # forward the /validate request to Vouch Proxy
      proxy_pass http://127.0.0.1:9090/validate;

      # be sure to pass the original host header
      proxy_set_header Host $http_host;

      # Vouch Proxy only acts on the request headers
      proxy_pass_request_body off;
      proxy_set_header Content-Length "";

      # optionally add X-Vouch-User as returned by Vouch Proxy along with the request
      auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;

      # these return values are used by the @error401 call
      auth_request_set $auth_resp_jwt $upstream_http_x_vouch_jwt;
      auth_request_set $auth_resp_err $upstream_http_x_vouch_err;
      auth_request_set $auth_resp_failcount $upstream_http_x_vouch_failcount;
    }

    # if validate returns `401 not authorized` then forward the request to the error401block
    error_page 401 = @error401;

    location @error401 {
        # redirect to Vouch Proxy for login
        return 302 https://vouch.yourdomain.com:9090/login?url=$scheme://$http_host$request_uri&vouch-failcount=$auth_resp_failcount&X-Vouch-Token=$auth_resp_jwt&error=$auth_resp_err;
    }

    # proxy pass authorized requests to your service
    location / {
      proxy_pass http://app1.yourdomain.com:8080;
      #  may need to set
      #    auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;
      #  in this bock as per https://github.com/vouch/vouch-proxy/issues/26#issuecomment-425215810
      # set user header (usually an email)
      proxy_set_header X-Vouch-User $auth_resp_x_vouch_user;
    }
}
```

## File: `examples/nginx/multi-file/conf.d/app2.yourdomain.com.conf`
```
server {
    listen 443 ssl http2;
    server_name app2.yourdomain.com;
    root /var/www/html/;

    ssl_certificate /etc/letsencrypt/live/app2.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/app2.yourdomain.com/privkey.pem;

    # send all requests to the `/validate` endpoint for authorization
    auth_request /validate;

    location = /validate {
      # forward the /validate request to Vouch Proxy
      proxy_pass http://127.0.0.1:9090/validate;

      # be sure to pass the original host header
      proxy_set_header Host $http_host;

      # Vouch Proxy only acts on the request headers
      proxy_pass_request_body off;
      proxy_set_header Content-Length "";

      # optionally add X-Vouch-User as returned by Vouch Proxy along with the request
      auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;

      # these return values are used by the @error401 call
      auth_request_set $auth_resp_jwt $upstream_http_x_vouch_jwt;
      auth_request_set $auth_resp_err $upstream_http_x_vouch_err;
      auth_request_set $auth_resp_failcount $upstream_http_x_vouch_failcount;
    }

    # if validate returns `401 not authorized` then forward the request to the error401block
    error_page 401 = @error401;

    location @error401 {
        # redirect to Vouch Proxy for login
        return 302 https://vouch.yourdomain.com:9090/login?url=$scheme://$http_host$request_uri&vouch-failcount=$auth_resp_failcount&X-Vouch-Token=$auth_resp_jwt&error=$auth_resp_err;
    }

    # proxy pass authorized requests to your service
    location / {
      proxy_pass http://app2.yourdomain.com:8080;
      #  may need to set
      #    auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;
      #  in this bock as per https://github.com/vouch/vouch-proxy/issues/26#issuecomment-425215810
      # set user header (usually an email)
      proxy_set_header X-Vouch-User $auth_resp_x_vouch_user;
    }
}
```

## File: `examples/nginx/multi-file/conf.d/unauthenticated_app3.yourdown.com.conf`
```
server {
    listen 443 ssl http2;
    server_name app3.yourdomain.com;
    root /var/www/html/;

    ssl_certificate /etc/letsencrypt/live/app3.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/app3.yourdomain.com/privkey.pem;


    # This application is simply proxy-passed without any authentication
    location / {
      proxy_pass http://app3.yourdomain.com:8080;
    }
}
```

## File: `examples/nginx/multi-file/conf.d/vouch.yourdomain.com.conf`
```
server {
    # Setting vouch behind SSL allows you to use the Secure flag for cookies.
    listen 443 ssl http2;
    server_name vouch.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/vouch.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/vouch.yourdomain.com/privkey.pem;

    location / {
       proxy_pass http://127.0.0.1:9090;
       # be sure to pass the original host header
       proxy_set_header Host vouch.yourdomain.com;
    }
}
```

## File: `examples/nginx/single-file/README.md`
```markdown
# Nginx Single-File Configuration Examples


| File                      | Description |
| :---                      | :---        |
| nginx_basic.conf          | The basic nginx configuration example.   Provides authentication for an app at https://protectedapp.yourdomain.com.  Vouch is running on vouch.yourdomain.com:9090 directly accessible.|
| nginx_with_vouch.conf     | Builds on the basic example by adding a proxy (port 80) for vouch to a vouch instance on localhost.  |
| nginx-with_vouch_ssl.conf | Builds on the basic example by adding a proxy (port 443) for vouch using https to a vouch instance on localhost.  This configuration supports secure cookies. Multiple backends can listen on port 443 at the same time when using server_name field.|
```

## File: `examples/nginx/single-file/nginx_basic.conf`
```
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;


    server {
        listen 443 ssl http2;
        server_name protectedapp.yourdomain.com;
        root /var/www/html/;

        ssl_certificate /etc/letsencrypt/live/protectedapp.yourdomain.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/protectedapp.yourdomain.com/privkey.pem;

        # send all requests to the `/validate` endpoint for authorization
        auth_request /validate;

        location = /validate {
          # forward the /validate request to Vouch Proxy
          proxy_pass http://vouch.yourdomain.com:9090/validate;

          # be sure to pass the original host header
          proxy_set_header Host $http_host;

          # Vouch Proxy only acts on the request headers
          proxy_pass_request_body off;
          proxy_set_header Content-Length "";

          # optionally add X-Vouch-User as returned by Vouch Proxy along with the request
          auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;

          # these return values are used by the @error401 call
          auth_request_set $auth_resp_jwt $upstream_http_x_vouch_jwt;
          auth_request_set $auth_resp_err $upstream_http_x_vouch_err;
          auth_request_set $auth_resp_failcount $upstream_http_x_vouch_failcount;
        }

        # if validate returns `401 not authorized` then forward the request to the error401block
        error_page 401 = @error401;

        location @error401 {
            # redirect to Vouch Proxy for login
            return 302 http://vouch.yourdomain.com:9090/login?url=$scheme://$http_host$request_uri&vouch-failcount=$auth_resp_failcount&X-Vouch-Token=$auth_resp_jwt&error=$auth_resp_err;
            # you usually *want* to redirect to Vouch running behind the same Nginx config proteced by https
            # but to get started you can just forward the end user to the port that vouch is running on
        }

        # proxy pass authorized requests to your service
        location / {
          # forward authorized requests to your service protectedapp.yourdomain.com
          proxy_pass http://127.0.0.1:8080;
          # you may need to set these variables in this block as per https://github.com/vouch/vouch-proxy/issues/26#issuecomment-425215810
          #    auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;
          #    auth_request_set $auth_resp_x_vouch_idp_claims_groups $upstream_http_x_vouch_idp_claims_groups;
          #    auth_request_set $auth_resp_x_vouch_idp_claims_given_name $upstream_http_x_vouch_idp_claims_given_name;

          # set user header (usually an email)
          proxy_set_header X-Vouch-User $auth_resp_x_vouch_user;
          # optionally pass any custom claims you are tracking
          #     proxy_set_header X-Vouch-IdP-Claims-Groups $auth_resp_x_vouch_idp_claims_groups;
          #     proxy_set_header X-Vouch-IdP-Claims-Given_Name $auth_resp_x_vouch_idp_claims_given_name;
          # optionally pass the accesstoken or idtoken
          #     proxy_set_header X-Vouch-IdP-AccessToken $auth_resp_x_vouch_idp_accesstoken;
          #     proxy_set_header X-Vouch-IdP-IdToken $auth_resp_x_vouch_idp_idtoken;
        }
    }

}
```

## File: `examples/nginx/single-file/nginx_with_vouch.conf`
```
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    server {
        listen 443 ssl http2;
        server_name protectedapp.yourdomain.com;
        root /var/www/html/;

        ssl_certificate /etc/letsencrypt/live/protectedapp.yourdomain.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/protectedapp.yourdomain.com/privkey.pem;

        # send all requests to the `/validate` endpoint for authorization
        auth_request /validate;

        location = /validate {
        # forward the /validate request to Vouch Proxy
        proxy_pass http://127.0.0.1:9090/validate;

        # be sure to pass the original host header
        proxy_set_header Host $http_host;

        # Vouch Proxy only acts on the request headers
        proxy_pass_request_body off;
        proxy_set_header Content-Length "";

        # optionally add X-Vouch-User as returned by Vouch Proxy along with the request
        auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;

        # these return values are used by the @error401 call
        auth_request_set $auth_resp_jwt $upstream_http_x_vouch_jwt;
        auth_request_set $auth_resp_err $upstream_http_x_vouch_err;
        auth_request_set $auth_resp_failcount $upstream_http_x_vouch_failcount;
        }

        # if validate returns `401 not authorized` then forward the request to the error401block
        error_page 401 = @error401;

        location @error401 {
            # redirect to Vouch Proxy for login
            return 302 http://vouch.yourdomain.com/login?url=$scheme://$http_host$request_uri&vouch-failcount=$auth_resp_failcount&X-Vouch-Token=$auth_resp_jwt&error=$auth_resp_err;
            # you usually *want* to redirect to Vouch running behind the same Nginx config proteced by https
            # but to get started you can just forward the end user to the port that vouch is running on
        }

        # proxy pass authorized requests to your service
        location / {
        # forward authorized requests to your service protectedapp.yourdomain.com
        proxy_pass http://127.0.0.1:8080;
        # you may need to set these variables in this block as per https://github.com/vouch/vouch-proxy/issues/26#issuecomment-425215810
        #    auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;
        #    auth_request_set $auth_resp_x_vouch_idp_claims_groups $upstream_http_x_vouch_idp_claims_groups;
        #    auth_request_set $auth_resp_x_vouch_idp_claims_given_name $upstream_http_x_vouch_idp_claims_given_name;

        # set user header (usually an email)
        proxy_set_header X-Vouch-User $auth_resp_x_vouch_user;
        # optionally pass any custom claims you are tracking
        #     proxy_set_header X-Vouch-IdP-Claims-Groups $auth_resp_x_vouch_idp_claims_groups;
        #     proxy_set_header X-Vouch-IdP-Claims-Given_Name $auth_resp_x_vouch_idp_claims_given_name;
        # optionally pass the accesstoken or idtoken
        #     proxy_set_header X-Vouch-IdP-AccessToken $auth_resp_x_vouch_idp_accesstoken;
        #     proxy_set_header X-Vouch-IdP-IdToken $auth_resp_x_vouch_idp_idtoken;
        }
    }

    server {
        listen 80 default_server;
        server_name vouch.yourdomain.com;
        location / {
        proxy_pass http://127.0.0.1:9090;
        # be sure to pass the original host header
        proxy_set_header Host vouch.yourdomain.com;
        }
    }

}
```

## File: `examples/nginx/single-file/nginx_with_vouch_single_server.conf`
```
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    upstream vouch {
        # set this to location of the vouch proxy
        server localhost:9090;
    }

    server {
        listen 443 ssl http2;
        server_name protectedapp.yourdomain.com;
        root /var/www/html/;

        ssl_certificate /etc/letsencrypt/live/protectedapp.yourdomain.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/protectedapp.yourdomain.com/privkey.pem;

        # This location serves all of the paths vouch uses
        location ~ ^/(auth|login|logout|static) {
          proxy_pass http://vouch;
          proxy_set_header Host $http_host;
        }

        location = /validate {
          # forward the /validate request to Vouch Proxy
          proxy_pass http://vouch/validate;

          # be sure to pass the original host header
          proxy_set_header Host $http_host;

          # Vouch Proxy only acts on the request headers
          proxy_pass_request_body off;
          proxy_set_header Content-Length "";

          # optionally add X-Vouch-User as returned by Vouch Proxy along with the request
          auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;

          # these return values are used by the @error401 call
          auth_request_set $auth_resp_jwt $upstream_http_x_vouch_jwt;
          auth_request_set $auth_resp_err $upstream_http_x_vouch_err;
          auth_request_set $auth_resp_failcount $upstream_http_x_vouch_failcount;
        }

        # if validate returns `401 not authorized` then forward the request to the error401block
        error_page 401 = @error401;

        location @error401 {
            # redirect to Vouch Proxy for login
            return 302 $scheme://$http_host/login?url=$scheme://$http_host$request_uri&vouch-failcount=$auth_resp_failcount&X-Vouch-Token=$auth_resp_jwt&error=$auth_resp_err;
            # you usually *want* to redirect to Vouch running behind the same Nginx config proteced by https
            # but to get started you can just forward the end user to the port that vouch is running on
        }

        # proxy pass authorized requests to your service
        location / {
          # send all requests to the `/validate` endpoint for authorization
          auth_request /validate;

          # forward authorized requests to your service protectedapp.yourdomain.com
          proxy_pass http://127.0.0.1:8080;
          # you may need to set these variables in this block as per https://github.com/vouch/vouch-proxy/issues/26#issuecomment-425215810
          #    auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;
          #    auth_request_set $auth_resp_x_vouch_idp_claims_groups $upstream_http_x_vouch_idp_claims_groups;
          #    auth_request_set $auth_resp_x_vouch_idp_claims_given_name $upstream_http_x_vouch_idp_claims_given_name;

          # set user header (usually an email)
          proxy_set_header X-Vouch-User $auth_resp_x_vouch_user;
          # optionally pass any custom claims you are tracking
          #     proxy_set_header X-Vouch-IdP-Claims-Groups $auth_resp_x_vouch_idp_claims_groups;
          #     proxy_set_header X-Vouch-IdP-Claims-Given_Name $auth_resp_x_vouch_idp_claims_given_name;
          # optionally pass the accesstoken or idtoken
          #     proxy_set_header X-Vouch-IdP-AccessToken $auth_resp_x_vouch_idp_accesstoken;
          #     proxy_set_header X-Vouch-IdP-IdToken $auth_resp_x_vouch_idp_idtoken;
        }
    }

}
```

## File: `examples/nginx/single-file/nginx_with_vouch_ssl.conf`
```
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;


    server {
        listen 443 ssl http2;
        server_name protectedapp.yourdomain.com;
        root /var/www/html/;

        ssl_certificate /etc/letsencrypt/live/protectedapp.yourdomain.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/protectedapp.yourdomain.com/privkey.pem;

        # send all requests to the `/validate` endpoint for authorization
        auth_request /validate;

        location = /validate {
        # forward the /validate request to Vouch Proxy
        proxy_pass http://127.0.0.1:9090/validate;

        # be sure to pass the original host header
        proxy_set_header Host $http_host;

        # Vouch Proxy only acts on the request headers
        proxy_pass_request_body off;
        proxy_set_header Content-Length "";

        # optionally add X-Vouch-User as returned by Vouch Proxy along with the request
        auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;

        # these return values are used by the @error401 call
        auth_request_set $auth_resp_jwt $upstream_http_x_vouch_jwt;
        auth_request_set $auth_resp_err $upstream_http_x_vouch_err;
        auth_request_set $auth_resp_failcount $upstream_http_x_vouch_failcount;
        }

        # if validate returns `401 not authorized` then forward the request to the error401block
        error_page 401 = @error401;

        location @error401 {
            # redirect to Vouch Proxy for login
            return 302 https://vouch.yourdomain.com/login?url=$scheme://$http_host$request_uri&vouch-failcount=$auth_resp_failcount&X-Vouch-Token=$auth_resp_jwt&error=$auth_resp_err;
        }

        # proxy pass authorized requests to your service
        location / {
        # forward authorized requests to your service protectedapp.yourdomain.com
        proxy_pass http://127.0.0.1:8080;
        # you may need to set these variables in this block as per https://github.com/vouch/vouch-proxy/issues/26#issuecomment-425215810
        #    auth_request_set $auth_resp_x_vouch_user $upstream_http_x_vouch_user;
        #    auth_request_set $auth_resp_x_vouch_idp_claims_groups $upstream_http_x_vouch_idp_claims_groups;
        #    auth_request_set $auth_resp_x_vouch_idp_claims_given_name $upstream_http_x_vouch_idp_claims_given_name;

        # set user header (usually an email)
        proxy_set_header X-Vouch-User $auth_resp_x_vouch_user;
        # optionally pass any custom claims you are tracking
        #     proxy_set_header X-Vouch-IdP-Claims-Groups $auth_resp_x_vouch_idp_claims_groups;
        #     proxy_set_header X-Vouch-IdP-Claims-Given_Name $auth_resp_x_vouch_idp_claims_given_name;
        # optionally pass the accesstoken or idtoken
        #     proxy_set_header X-Vouch-IdP-AccessToken $auth_resp_x_vouch_idp_accesstoken;
        #     proxy_set_header X-Vouch-IdP-IdToken $auth_resp_x_vouch_idp_idtoken;
        }
    }

    server {
        # Setting vouch behind SSL allows you to use the Secure flag for cookies.
        listen 443 ssl http2;
        server_name vouch.yourdomain.com;

        ssl_certificate /etc/letsencrypt/live/vouch.yourdomain.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/vouch.yourdomain.com/privkey.pem;

        location / {
        proxy_pass http://127.0.0.1:9090;
        # be sure to pass the original host header
        proxy_set_header Host vouch.yourdomain.com;
        }
    }

}
```

## File: `examples/slack/vouch-slack-oidc-app-manifest.yml`
```yaml
_metadata:
  major_version: 1
  minor_version: 1
display_information:
  name: Vouch Proxy - Login to Slack
  description: enforce login to Slack to provide authorized access to your websites
  background_color: "#002da8"
oauth_config:
  # these need to match the 
  redirect_urls:    
    - https://vouch.yourdomain.com/auth
  scopes:
    user:
      - email
      - openid
      - profile
```

## File: `examples/startup/README.md`
```markdown
# Startups Scripts

If you are running Vouch Proxy on a linux system, instead of docker, you may want to automatically start Vouch Proxy.

:bangbang: Please note, we highly recommend running Vouch Proxy as a **regular user**.  Vouch Proxy listens on port 9090 and doesn't require ANY root privileges.  **Please DO NOT run Vouch as root**.

All provided scripts assume that the compiled Vouch Proxy binary `vouch-proxy` has been installed in `/opt/vouch-proxy` with the executable flag set and owned by `vouch-proxy` user (that has also been created)
 
## Systemd

```
cp startup/systemd/vouch-proxy.service /etc/systemd/system/vouch-proxy.service
systemctl enable vouch-proxy.service
systemctl start vouch-proxy.service
```
```

## File: `examples/startup/systemd/vouch-proxy.service`
```
[Unit]
Description=Vouch Proxy
After=network.target

[Service]
Type=simple
User=vouch-proxy
WorkingDirectory=/opt/vouch-proxy
ExecStart=/opt/vouch-proxy/vouch-proxy
Restart=on-failure
RestartSec=5
StartLimitInterval=60s
StartLimitBurst=3

[Install]
WantedBy=default.target
```

## File: `handlers/auth.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package handlers

import (
	"fmt"
	"net/http"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/cookie"
	"github.com/vouch/vouch-proxy/pkg/domains"
	"github.com/vouch/vouch-proxy/pkg/jwtmanager"
	"github.com/vouch/vouch-proxy/pkg/responses"
	"github.com/vouch/vouch-proxy/pkg/structs"

	"golang.org/x/oauth2"
)

// CallbackHandler /auth
// - redirects to /auth/{state}/ with the state coming from the query parameter
func CallbackHandler(w http.ResponseWriter, r *http.Request) {
	log.Debug("/auth")

	// did the IdP return an error?
	errorIDP := r.URL.Query().Get("error")
	if errorIDP != "" {
		errorDescription := r.URL.Query().Get("error_description")
		responses.Error401HTTP(w, r, fmt.Errorf("/auth Error from IdP: %s - %s", errorIDP, errorDescription))
		return
	}

	queryState := r.URL.Query().Get("state")
	if queryState == "" {
		responses.Error400(w, r, fmt.Errorf("/auth: could not find state in query %s", r.URL.RawQuery))
		return
	}

	// has to have a trailing / in its path, because the path of the session cookie is set to /auth/{state}/.
	// see note in login.go and https://github.com/vouch/vouch-proxy/issues/373
	authStateURL := fmt.Sprintf("%s/auth/%s/?%s", cfg.Cfg.DocumentRoot, queryState, r.URL.RawQuery)
	responses.Redirect302(w, r, authStateURL)
}

// AuthStateHandler /auth/{state}/
// - validate info from oauth provider (Google, GitHub, OIDC, etc)
// - issue jwt in the form of a cookie
func AuthStateHandler(w http.ResponseWriter, r *http.Request) {
	log.Debug("/auth/{state}/")
	// Handle the exchange code to initiate a transport.

	session, err := sessstore.Get(r, cfg.Cfg.Session.Name)
	if err != nil {
		responses.Error400(w, r, fmt.Errorf("/auth %w: could not find session store %s", err, cfg.Cfg.Session.Name))
		return
	}

	// is the nonce "state" valid?
	queryState := r.URL.Query().Get("state")
	if session.Values["state"] != queryState {
		responses.Error400(w, r, fmt.Errorf("/auth Invalid session state: stored %s, returned %s", session.Values["state"], queryState))
		return
	}

	user := structs.User{}
	customClaims := structs.CustomClaims{}
	ptokens := structs.PTokens{}

	// is code challenge enabled?
	authCodeOptions := []oauth2.AuthCodeOption{}

	if cfg.GenOAuth.CodeChallengeMethod != "" {
		authCodeOptions = []oauth2.AuthCodeOption{
			oauth2.SetAuthURLParam("code_challenge", session.Values["codeChallenge"].(string)),
			oauth2.SetAuthURLParam("code_verifier", session.Values["codeVerifier"].(string)),
		}
	}

	if err := getUserInfo(r, &user, &customClaims, &ptokens, authCodeOptions...); err != nil {
		responses.Error400(w, r, fmt.Errorf("/auth Error while retrieving user info after successful login at the OAuth provider: %w", err))
		return
	}
	log.Debugf("/auth/{state}/ Claims from userinfo: %+v", customClaims)

	// verify / authz the user
	if ok, err := verifyUser(user); !ok {
		responses.Error403(w, r, fmt.Errorf("/auth User is not authorized: %w . Please try again or seek support from your administrator", err))
		return
	}

	// SUCCESS!! they are authorized

	// issue the jwt

	tokenstring, err := jwtmanager.NewVPJWT(user, customClaims, ptokens)
	if err != nil {
		responses.Error500(w, r, fmt.Errorf("/auth Token creation failure: %w . Please seek support from your administrator", err))
		return

	}
	cookie.SetCookie(w, r, tokenstring)

	// get the originally requested URL so we can send them on their way
	requestedURL := session.Values["requestedURL"].(string)
	if requestedURL != "" {
		// clear out the session value
		session.Values["requestedURL"] = ""
		session.Values[requestedURL] = 0
		session.Options.MaxAge = -1
		if err = session.Save(r, w); err != nil {
			log.Error(err)
		}

		responses.Redirect302(w, r, requestedURL)
		return
	}

	// otherwise serve an error
	responses.RenderIndex(w, "/auth "+tokenstring)
}

// verifyUser validates that the domains match for the user
func verifyUser(u interface{}) (bool, error) {

	user := u.(structs.User)

	switch {

	// AllowAllUsers
	case cfg.Cfg.AllowAllUsers:
		log.Debugf("verifyUser: Success! skipping verification, cfg.Cfg.AllowAllUsers is %t", cfg.Cfg.AllowAllUsers)
		return true, nil

	// WhiteList
	case len(cfg.Cfg.WhiteList) != 0:
		for _, wl := range cfg.Cfg.WhiteList {
			if user.Username == wl {
				log.Debugf("verifyUser: Success! found user.Username in WhiteList: %s", user.Username)
				return true, nil
			}
		}
		return false, fmt.Errorf("verifyUser: user.Username not found in WhiteList: %s", user.Username)

	// TeamWhiteList
	case len(cfg.Cfg.TeamWhiteList) != 0:
		for _, team := range user.TeamMemberships {
			for _, wl := range cfg.Cfg.TeamWhiteList {
				if team == wl {
					log.Debugf("verifyUser: Success! found user.TeamWhiteList in TeamWhiteList: %s for user %s", wl, user.Username)
					return true, nil
				}
			}
		}
		return false, fmt.Errorf("verifyUser: user.TeamMemberships %s not found in TeamWhiteList: %s for user %s", user.TeamMemberships, cfg.Cfg.TeamWhiteList, user.Username)

	// Domains
	case len(cfg.Cfg.Domains) != 0:
		if domains.IsUnderManagement(user.Email) {
			log.Debugf("verifyUser: Success! Email %s found within a %s managed domain", user.Email, cfg.Branding.FullName)
			return true, nil
		}
		return false, fmt.Errorf("verifyUser: Email %s is not within a %s managed domain", user.Email, cfg.Branding.FullName)

	// nothing configured, allow everyone through
	default:
		log.Warn("verifyUser: no domains, whitelist, teamWhitelist or AllowAllUsers configured, any successful auth to the IdP authorizes access")
		return true, nil
	}
}

func getUserInfo(r *http.Request, user *structs.User, customClaims *structs.CustomClaims, ptokens *structs.PTokens, opts ...oauth2.AuthCodeOption) error {
	return provider.GetUserInfo(r, user, customClaims, ptokens, opts...)
}
```

## File: `handlers/auth_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package handlers

import (
	"fmt"
	"net/http"
	"net/http/httptest"
	"net/url"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/vouch/vouch-proxy/pkg/cfg"
)

func TestCallbackHandlerDocumentRoot(t *testing.T) {
	handlerL := http.HandlerFunc(LoginHandler)
	handlerA := http.HandlerFunc(CallbackHandler)

	tests := []struct {
		name       string
		configFile string
		wantcode   int
	}{
		{"should have URL that begins with DocumentRoot", "/config/testing/handler_login_url_document_root.yml", http.StatusFound},
		{"should have URL that does not begin with DocumentRoot", "/config/testing/handler_login_url.yml", http.StatusFound},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			setUp(tt.configFile)

			// first make a request of /login to set the session cookie
			reqLogin, err := http.NewRequest("GET", cfg.Cfg.DocumentRoot+"/login?url=http://myapp.example.com/logout", nil)
			reqLogin.Header.Set("Host", "my.example.com")
			if err != nil {
				t.Fatal(err)
			}
			rrL := httptest.NewRecorder()
			handlerL.ServeHTTP(rrL, reqLogin)

			// grab the state from the session cookie to
			session, err := sessstore.Get(reqLogin, cfg.Cfg.Session.Name)
			state := session.Values["state"].(string)
			if err != nil {
				t.Fatal(err)
			}

			// now mimic an IdP returning the state variable back to us
			reqAuth, err := http.NewRequest("GET", cfg.Cfg.DocumentRoot+"/auth?state="+state, nil)
			reqAuth.Header.Set("Host", "my.example.com")
			if err != nil {
				t.Fatal(err)
			}
			// transfer the cookie from rrL to reqAuth
			rrA := httptest.NewRecorder()

			handlerA.ServeHTTP(rrA, reqAuth)
			if rrA.Code != tt.wantcode {
				t.Errorf("LoginHandler() status = %v, want %v", rrA.Code, tt.wantcode)
			}

			// confirm the requst to $DocumentRoot/auth is redirected to $DocumentRoot/auth/$state
			redirectURL, err := url.Parse(rrA.Header()["Location"][0])
			if err != nil {
				t.Fatal(err)
			}
			assert.Equal(t, fmt.Sprintf("%s/auth/%s/", cfg.Cfg.DocumentRoot, state), redirectURL.Path)

		})
	}
}

func TestAuthStateHandler(t *testing.T) {
	type args struct {
		w http.ResponseWriter
		r *http.Request
	}
	tests := []struct {
		name string
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			AuthStateHandler(tt.args.w, tt.args.r)
		})
	}
}
```

## File: `handlers/handlers.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package handlers

import (
	"net/http"

	"github.com/gorilla/sessions"
	"github.com/vouch/vouch-proxy/pkg/providers/discord"
	"go.uber.org/zap"
	"golang.org/x/oauth2"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/cookie"
	"github.com/vouch/vouch-proxy/pkg/providers/adfs"
	"github.com/vouch/vouch-proxy/pkg/providers/alibaba"
	"github.com/vouch/vouch-proxy/pkg/providers/azure"
	"github.com/vouch/vouch-proxy/pkg/providers/common"
	"github.com/vouch/vouch-proxy/pkg/providers/github"
	"github.com/vouch/vouch-proxy/pkg/providers/google"
	"github.com/vouch/vouch-proxy/pkg/providers/homeassistant"
	"github.com/vouch/vouch-proxy/pkg/providers/indieauth"
	"github.com/vouch/vouch-proxy/pkg/providers/nextcloud"
	"github.com/vouch/vouch-proxy/pkg/providers/openid"
	"github.com/vouch/vouch-proxy/pkg/providers/openstax"
	"github.com/vouch/vouch-proxy/pkg/structs"
)

// Provider each Provider must support GetuserInfo
type Provider interface {
	Configure()
	GetUserInfo(r *http.Request, user *structs.User, customClaims *structs.CustomClaims, ptokens *structs.PTokens, opts ...oauth2.AuthCodeOption) error
}

const (
	base64Bytes = 32
)

var (
	sessstore *sessions.CookieStore
	log       *zap.SugaredLogger
	fastlog   *zap.Logger
	provider  Provider
)

// Configure see main.go configure()
func Configure() {
	log = cfg.Logging.Logger
	fastlog = cfg.Logging.FastLogger
	// http://www.gorillatoolkit.org/pkg/sessions
	sessstore = sessions.NewCookieStore([]byte(cfg.Cfg.Session.Key))
	sessstore.Options.HttpOnly = cfg.Cfg.Cookie.HTTPOnly
	sessstore.Options.Secure = cfg.Cfg.Cookie.Secure
	sessstore.Options.SameSite = cookie.SameSite()
	sessstore.Options.MaxAge = cfg.Cfg.Session.MaxAge * 60 // convert minutes to seconds

	provider = getProvider()
	provider.Configure()
	common.Configure()
}

func getProvider() Provider {
	switch cfg.GenOAuth.Provider {
	case cfg.Providers.IndieAuth:
		return indieauth.Provider{}
	case cfg.Providers.ADFS:
		return adfs.Provider{}
	case cfg.Providers.Azure:
		return azure.Provider{}
	case cfg.Providers.HomeAssistant:
		return homeassistant.Provider{}
	case cfg.Providers.OpenStax:
		return openstax.Provider{}
	case cfg.Providers.Google:
		return google.Provider{}
	case cfg.Providers.GitHub:
		return github.Provider{PrepareTokensAndClient: common.PrepareTokensAndClient}
	case cfg.Providers.Nextcloud:
		return nextcloud.Provider{}
	case cfg.Providers.OIDC:
		return openid.Provider{}
	case cfg.Providers.Alibaba:
		return alibaba.Provider{}
	case cfg.Providers.Discord:
		return discord.Provider{}
	default:
		// shouldn't ever reach this since cfg checks for a properly configure `oauth.provider`
		log.Fatal("oauth.provider appears to be misconfigured, please check your config")
		return nil
	}
}
```

## File: `handlers/handlers_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package handlers

import (
	"encoding/json"
	"os"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/cookie"
	"github.com/vouch/vouch-proxy/pkg/domains"
	"github.com/vouch/vouch-proxy/pkg/jwtmanager"
	"github.com/vouch/vouch-proxy/pkg/responses"
	"github.com/vouch/vouch-proxy/pkg/structs"
)

// var (
// 	token = &oauth2.Token{AccessToken: "123"}
// )

// setUp load config file and then call Configure() for dependent packages
func setUp(configFile string) {
	os.Setenv("VOUCH_CONFIG", filepath.Join(os.Getenv("VOUCH_ROOT"), configFile))
	cfg.InitForTestPurposes()

	Configure()
	domains.Configure()
	jwtmanager.Configure()
	cookie.Configure()
	responses.Configure()
}

func TestVerifyUserPositiveUserInWhiteList(t *testing.T) {
	setUp("/config/testing/handler_whitelist.yml")
	user := &structs.User{Username: "test@example.com", Email: "test@example.com", Name: "Test Name"}
	ok, err := verifyUser(*user)
	assert.True(t, ok)
	assert.Nil(t, err)
}

func TestVerifyUserPositiveAllowAllUsers(t *testing.T) {
	setUp("/config/testing/handler_allowallusers.yml")

	user := &structs.User{Username: "testuser", Email: "test@example.com", Name: "Test Name"}

	ok, err := verifyUser(*user)
	assert.True(t, ok)
	assert.Nil(t, err)
}

func TestVerifyUserPositiveByEmail(t *testing.T) {
	setUp("/config/testing/handler_email.yml")
	user := &structs.User{Username: "testuser", Email: "test@example.com", Name: "Test Name"}
	ok, err := verifyUser(*user)
	assert.True(t, ok)
	assert.Nil(t, err)
}

func TestVerifyUserPositiveByTeam(t *testing.T) {
	setUp("/config/testing/handler_teams.yml")

	// cfg.Cfg.TeamWhiteList = append(cfg.Cfg.TeamWhiteList, "org1/team2", "org1/team1")
	user := &structs.User{Username: "testuser", Email: "test@example.com", Name: "Test Name"}
	user.TeamMemberships = append(user.TeamMemberships, "org1/team3")
	user.TeamMemberships = append(user.TeamMemberships, "org1/team1")
	ok, err := verifyUser(*user)
	assert.True(t, ok)
	assert.Nil(t, err)
}

func TestVerifyUserNegativeByTeam(t *testing.T) {
	setUp("/config/testing/handler_teams.yml")
	user := &structs.User{Username: "testuser", Email: "test@example.com", Name: "Test Name"}
	// cfg.Cfg.TeamWhiteList = append(cfg.Cfg.TeamWhiteList, "org1/team1")

	ok, err := verifyUser(*user)
	assert.False(t, ok)
	assert.NotNil(t, err)
}

func TestVerifyUserPositiveNoDomainsConfigured(t *testing.T) {
	setUp("/config/testing/handler_nodomains.yml")

	user := &structs.User{Username: "testuser", Email: "test@example.com", Name: "Test Name"}
	cfg.Cfg.Domains = make([]string, 0)
	ok, err := verifyUser(*user)

	assert.True(t, ok)
	assert.Nil(t, err)
}

func TestVerifyUserNegative(t *testing.T) {
	setUp("/config/testing/test_config.yml")
	user := &structs.User{Username: "testuser", Email: "test@example.com", Name: "Test Name"}
	ok, err := verifyUser(*user)

	assert.False(t, ok)
	assert.NotNil(t, err)
}

// copied from jwtmanager_test.go
// it should live there but circular imports are resolved if it lives here
var (
	u1 = structs.User{
		Username: "test@testing.com",
		Name:     "Test Name",
	}
	t1 = structs.PTokens{
		PAccessToken: "eyJhbGciOiJSUzI1NiIsImtpZCI6IjRvaXU4In0.eyJzdWIiOiJuZnlmZSIsImF1ZCI6ImltX29pY19jbGllbnQiLCJqdGkiOiJUOU4xUklkRkVzUE45enU3ZWw2eng2IiwiaXNzIjoiaHR0cHM6XC9cL3Nzby5tZXljbG91ZC5uZXQ6OTAzMSIsImlhdCI6MTM5MzczNzA3MSwiZXhwIjoxMzkzNzM3MzcxLCJub25jZSI6ImNiYTU2NjY2LTRiMTItNDU2YS04NDA3LTNkMzAyM2ZhMTAwMiIsImF0X2hhc2giOiJrdHFvZVBhc2praVY5b2Z0X3o5NnJBIn0.g1Jc9DohWFfFG3ppWfvW16ib6YBaONC5VMs8J61i5j5QLieY-mBEeVi1D3vr5IFWCfivY4hZcHtoJHgZk1qCumkAMDymsLGX-IGA7yFU8LOjUdR4IlCPlZxZ_vhqr_0gQ9pCFKDkiOv1LVv5x3YgAdhHhpZhxK6rWxojg2RddzvZ9Xi5u2V1UZ0jukwyG2d4PRzDn7WoRNDGwYOEt4qY7lv_NO2TY2eAklP-xYBWu0b9FBElapnstqbZgAXdndNs-Wqp4gyQG5D0owLzxPErR9MnpQfgNcai-PlWI_UrvoopKNbX0ai2zfkuQ-qh6Xn8zgkiaYDHzq4gzwRfwazaqA",
		PIdToken:     "eyJhbGciOiJSUzI1NiIsImtpZCI6IjRvaXU4In0.eyJzdWIiOiJuZnlmZSIsImF1ZCI6ImltX29pY19jbGllbnQiLCJqdGkiOiJUOU4xUklkRkVzUE45enU3ZWw2eng2IiwiaXNzIjoiaHR0cHM6XC9cL3Nzby5tZXljbG91ZC5uZXQ6OTAzMSIsImlhdCI6MTM5MzczNzA3MSwiZXhwIjoxMzkzNzM3MzcxLCJub25jZSI6ImNiYTU2NjY2LTRiMTItNDU2YS04NDA3LTNkMzAyM2ZhMTAwMiIsImF0X2hhc2giOiJrdHFvZVBhc2praVY5b2Z0X3o5NnJBIn0.g1Jc9DohWFfFG3ppWfvW16ib6YBaONC5VMs8J61i5j5QLieY-mBEeVi1D3vr5IFWCfivY4hZcHtoJHgZk1qCumkAMDymsLGX-IGA7yFU8LOjUdR4IlCPlZxZ_vhqr_0gQ9pCFKDkiOv1LVv5x3YgAdhHhpZhxK6rWxojg2RddzvZ9Xi5u2V1UZ0jukwyG2d4PRzDn7WoRNDGwYOEt4qY7lv_NO2TY2eAklP-xYBWu0b9FBElapnstqbZgAXdndNs-Wqp4gyQG5D0owLzxPErR9MnpQfgNcai-PlWI_UrvoopKNbX0ai2zfkuQ-qh6Xn8zgkiaYDHzq4gzwRfwazaqA",
	}

	lc jwtmanager.VouchClaims

	claimjson = `{
		"sub": "f:a95afe53-60ba-4ac6-af15-fab870e72f3d:mrtester",
		"groups": ["Website Users", "Test Group"],
		"given_name": "Mister",
		"family_name": "Tester",
		"email": "mrtester@test.int"
	}`
	customClaims = structs.CustomClaims{}
)

// copied from jwtmanager_test.go
func init() {
	// log.SetLevel(log.DebugLevel)

	lc = jwtmanager.VouchClaims{
		Username:       u1.Username,
		CustomClaims:   customClaims.Claims,
		PAccessToken:   t1.PAccessToken,
		PIdToken:       t1.PIdToken,
		StandardClaims: jwtmanager.StandardClaims,
	}
	json.Unmarshal([]byte(claimjson), &customClaims.Claims)
}

func TestParsedIdPTokens(t *testing.T) {
	tests := []struct {
		name          string
		configFile    string
		wantIDPTokens bool
	}{
		{"no IdP tokens", "/config/testing/handler_claims.yml", false},
		{"wants IdP tokens", "/config/testing/jwtmanager_has_idp_token_claims.yml", true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			setUp(tt.configFile)
			uts, err := jwtmanager.NewVPJWT(u1, customClaims, t1)
			assert.NoError(t, err)
			utsParsed, _ := jwtmanager.ParseTokenString(uts)
			utsPtokens, _ := jwtmanager.PTokenClaims(utsParsed)

			if tt.wantIDPTokens {
				if t1.PIdToken != utsPtokens.PIdToken || t1.PAccessToken != utsPtokens.PAccessToken {
					t.Errorf("got PIdToken = %s, PAccessToken = %s, \nwant %s , %s", utsPtokens.PIdToken, utsPtokens.PAccessToken, t1.PIdToken, t1.PAccessToken)
				}
			} else {
				if utsPtokens.PIdToken != "" || utsPtokens.PAccessToken != "" {
					t.Errorf("PIdToken and PAccessToken = should be '' got '%s', '%s'", utsPtokens.PIdToken, utsPtokens.PAccessToken)
				}
			}
		})
	}

}
```

## File: `handlers/healthcheck.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package handlers

import (
	"fmt"
	"net/http"
)

// HealthcheckHandler /healthcheck
// just returns 200 '{ "ok": true }'
func HealthcheckHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	if _, err := fmt.Fprintf(w, "{ \"ok\": true }"); err != nil {
		log.Error(err)
	}
}
```

## File: `handlers/login.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package handlers

import (
	"errors"
	"fmt"
	"net/http"
	"net/url"
	"regexp"
	"strings"

	"github.com/gorilla/sessions"
	cv "github.com/nirasan/go-oauth-pkce-code-verifier"
	"github.com/theckman/go-securerandom"
	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/cookie"
	"github.com/vouch/vouch-proxy/pkg/domains"
	"github.com/vouch/vouch-proxy/pkg/responses"
	"golang.org/x/oauth2"
)

// see https://github.com/vouch/vouch-proxy/issues/282
var errTooManyRedirects = errors.New("too many unsuccessful authorization attempts for the requested URL")

const failCountLimit = 6

// LoginHandler /login
// currently performs a 302 redirect to Google
func LoginHandler(w http.ResponseWriter, r *http.Request) {
	log.Debug("/login")
	// no matter how you ended up here, make sure the cookie gets cleared out
	cookie.ClearCookie(w, r)

	session, err := sessstore.Get(r, cfg.Cfg.Session.Name)
	if err != nil {
		log.Infof("couldn't find existing encrypted secure cookie with name %s: %s (probably fine)", cfg.Cfg.Session.Name, err)
	}

	state, err := generateStateNonce()
	if err != nil {
		log.Error(err)
	}

	// set the state variable in the session
	session.Values["state"] = state

	// set the path for the session cookie to only send the correct cookie to /auth/{state}/
	// must have a trailing slash. Otherwise, it is send to all endpoints that _start_ with the cookie path.
	session.Options.Path = fmt.Sprintf("%s/auth/%s/", cfg.Cfg.DocumentRoot, state)

	log.Debugf("session state set to %s", session.Values["state"])

	// requestedURL comes from nginx in the query string via a 302 redirect
	// it sets the ultimate destination
	// https://vouch.yoursite.com/login?url=
	// need to clean the URL to prevent malicious redirection
	var requestedURL string
	if requestedURL, err = getValidRequestedURL(r); err != nil {
		responses.Error400(w, r, err)
		return
	}

	// set session variable for eventual 302 redirecton to original request
	session.Values["requestedURL"] = requestedURL
	log.Debugf("session requestedURL set to %s", session.Values["requestedURL"])

	// increment the failure counter for the requestedURL
	// stop them after three failures for this URL
	var failcount = 0
	if session.Values[requestedURL] != nil {
		failcount = session.Values[requestedURL].(int)
		log.Debugf("failcount for %s is %d", requestedURL, failcount)
	}
	failcount++
	session.Values[requestedURL] = failcount

	// Add code challenge if enabled
	if cfg.GenOAuth.CodeChallengeMethod != "" {
		log.Debugf("Adding code challenge")
		appendCodeChallenge(*session)
	}

	log.Debugf("saving session with failcount %d", failcount)
	if err = session.Save(r, w); err != nil {
		log.Error(err)
	}

	if failcount > failCountLimit {
		var vouchError = r.URL.Query().Get("error")
		responses.Error400(w, r, fmt.Errorf("/login %w %s %s", errTooManyRedirects, requestedURL, vouchError))
		return
	}

	// SUCCESS
	// bounce to oauth provider for login
	var oURL = oauthLoginURL(r, *session)
	log.Debugf("redirecting to oauthURL %s", oURL)
	responses.Redirect302(w, r, oURL)
}

var (
	errNoURL      = errors.New("no destination URL requested")
	errInvalidURL = errors.New("requested destination URL appears to be invalid")
	errURLNotHTTP = errors.New("requested destination URL is not a valid URL (does not begin with 'http://' or 'https://')")
	errDangerQS   = errors.New("requested destination URL has a dangerous query string")
	badStrings    = []string{"http://", "https://", "data:", "ftp://", "ftps://", "//", "javascript:"}
	reAmpSemi     = regexp.MustCompile("[&;]")
)

// inspect login query params to located the url param, while taking into account that the login URL may be
// presented in an RFC-non-compliant way (for example, it is common for the url param to
// not have its own query params property encoded, leading to URLs like
// http://host/login?X-Vouch-Token=token&url=http://host/path?param=value&param2=value2&vouch-failcount=value3
// where some params -- here X-Vouch-Token and vouch-failcount -- belong to login, and some others
// -- here param and param2 -- belong to the url param of login)
// The algorithm is as follows:
// * All login params starting with vouch- or x-vouch- (case insensitively) are treated as true login params
// * The "error" login param (case sensitively) is treated as true login param
// * The "rd" login param (case sensitively) added by nginx ingress is treated as true login param https://github.com/vouch/vouch-proxy/issues/289
// * All other login params are treated as non-login params
// * All non-login params between the url param and the first true login param are folded into the url param
// * All remaining non-login params are considered stray non-login params
//
// Returns
// * _, _, err: if an error occurred while parsing the URL
// * URL, empty array, nil: if URL is valid and contains no stray non-login params
// * URL, array of stray params, nil: if URL is valid and contains stray non-login params
func normalizeLoginURLParam(loginURL *url.URL) (*url.URL, []string, error) {
	// url.URL.Query return a map and therefore makes no guarantees about param order
	// Therefore we have to ascertain the param order by inspecting the raw query
	var urlParam *url.URL = nil // Will be url.URL for the url param
	urlParamDone := false       // Will be true when we're done building urlParam (but we're still checking for stray params)
	strays := []string{}        // List of stray params

	for _, param := range reAmpSemi.Split(loginURL.RawQuery, -1) {
		paramKeyVal := strings.Split(param, "=")
		paramKey := paramKeyVal[0]
		lcParamKey := strings.ToLower(paramKey)
		isVouchParam := strings.HasPrefix(lcParamKey, cfg.Branding.LCName) ||
			strings.HasPrefix(lcParamKey, "x-"+cfg.Branding.LCName) ||
			paramKey == "error" || // Used by VouchProxy login
			paramKey == "rd" // Passed to VouchProxy by nginx-ingress and then ignored (see #289)

		if urlParam == nil {
			// Still looking for url param
			if paramKey == "url" {
				// Found it
				parsed, e := url.ParseQuery(param)

				if e != nil {
					return nil, []string{}, e // failure to parse url param
				}

				urlParam, e = url.Parse(parsed.Get("url"))

				if e != nil {
					return nil, []string{}, e // failure to parse url param
				}
			} else if !isVouchParam {
				// Non-vouch param before url param is a stray param
				log.Infof("Stray param in login request (%s)", paramKey)
				strays = append(strays, paramKey)
			} // else vouch param before url param, doesn't change outcome
		} else {
			// Looking at params after url param
			if !urlParamDone && isVouchParam {
				// First vouch param after url param
				urlParamDone = true
				// But keep going to check for strays
			} else if !urlParamDone {
				// Non-vouch param after url and before first vouch param, fold it into urlParam
				if urlParam.RawQuery == "" {
					urlParam.RawQuery = param
				} else {
					urlParam.RawQuery = urlParam.RawQuery + "&" + param
				}
			} else if !isVouchParam {
				// Non-vouch param after vouch param is a stray param
				log.Infof("Stray param in login request (%s)", paramKey)
				strays = append(strays, paramKey)
			} // else vouch param after vouch param, doesn't change outcome
		}
	}

	log.Debugf("Login url param normalized to '%s'", urlParam)
	return urlParam, strays, nil

}

func getValidRequestedURL(r *http.Request) (string, error) {
	u, strays, err := normalizeLoginURLParam(r.URL)

	if len(strays) > 0 {
		log.Debugf("Stray params in login url (%+q) will be ignored", strays)
	}

	if err != nil {
		return "", fmt.Errorf("not a valid login URL: %w %s", errInvalidURL, err)
	}

	if u == nil || u.String() == "" {
		return "", errNoURL
	}

	if u.Scheme != "http" && u.Scheme != "https" {
		return "", errURLNotHTTP
	}

	for _, v := range u.Query() {
		// log.Debugf("validateRequestedURL %s:%s", k, v)
		for _, vval := range v {
			for _, bad := range badStrings {
				if strings.HasPrefix(strings.ToLower(vval), bad) {
					return "", fmt.Errorf("%w looks bad: %s includes %s", errDangerQS, vval, bad)
				}
			}
		}
	}

	hostname := u.Hostname()
	if cfg.GenOAuth.Provider != cfg.Providers.IndieAuth {
		d := domains.Matches(hostname)
		if d == "" {
			inCookieDomain := (hostname == cfg.Cfg.Cookie.Domain || strings.HasSuffix(hostname, "."+cfg.Cfg.Cookie.Domain))
			if cfg.Cfg.Cookie.Domain == "" || !inCookieDomain {
				return "", fmt.Errorf("%w: not within a %s managed domain", errInvalidURL, cfg.Branding.FullName)
			}
		}
	}

	// if the requested URL is http then the cookie cannot be seen if cfg.Cfg.Cookie.Secure is set
	if u.Scheme == "http" && cfg.Cfg.Cookie.Secure {
		return "", fmt.Errorf("%w: mismatch between requested destination URL and '%s.cookie.secure: %v' (the cookie is only visible to 'https' but the requested site is 'http')", errInvalidURL, cfg.Branding.LCName, cfg.Cfg.Cookie.Secure)
	}

	return u.String(), nil
}

func oauthLoginURL(r *http.Request, session sessions.Session) string {
	// State can be some kind of random generated hash string.
	// See relevant RFC: http://tools.ietf.org/html/rfc6749#section-10.12
	var state string = session.Values["state"].(string)
	opts := []oauth2.AuthCodeOption{}
	if cfg.GenOAuth.Provider == cfg.Providers.IndieAuth {
		return cfg.OAuthClient.AuthCodeURL(state, oauth2.SetAuthURLParam("response_type", "id"))
	}

	// cfg.OAuthClient.RedirectURL is set in cfg
	// this checks the multiple redirect case for multiple matching domains
	if len(cfg.GenOAuth.RedirectURLs) > 0 {
		found := false
		domain := domains.Matches(r.Host)
		log.Debugf("/login looking for callback_url matching %s", domain)
		for _, v := range cfg.GenOAuth.RedirectURLs {
			if strings.Contains(v, domain) {
				found = true
				log.Debugf("/login callback_url set to %s", v)
				cfg.OAuthClient.RedirectURL = v
				break
			}
		}
		if !found {
			log.Infof("/login no callback_url matched %s (is the `Host` header being passed to Vouch Proxy?)", domain)
		}
	}
	// append code challenge and code challenge method query parameters if enabled

	if cfg.GenOAuth.CodeChallengeMethod != "" {
		opts = append(opts, oauth2.SetAuthURLParam("code_challenge_method", cfg.GenOAuth.CodeChallengeMethod))
		opts = append(opts, oauth2.SetAuthURLParam("code_challenge", session.Values["codeChallenge"].(string)))
	}
	if cfg.OAuthopts != nil {
		opts = append(opts, cfg.OAuthopts...)
	}
	return cfg.OAuthClient.AuthCodeURL(state, opts...)
}

var regExJustAlphaNum, _ = regexp.Compile("[^a-zA-Z0-9]+")

func generateStateNonce() (string, error) {
	state, err := securerandom.URLBase64InBytes(base64Bytes)
	if err != nil {
		return "", err
	}
	state = regExJustAlphaNum.ReplaceAllString(state, "")
	return state, nil
}

func appendCodeChallenge(session sessions.Session) {
	var codeChallenge string
	var CodeVerifier, _ = cv.CreateCodeVerifier()
	switch strings.ToUpper(cfg.GenOAuth.CodeChallengeMethod) {
	case "S256":
		codeChallenge = CodeVerifier.CodeChallengeS256()
	case "PLAIN":
		// TODO support plain text code challenge
		//codeChallenge = CodeVerifier.CodeChallengePlain()
		log.Fatal("plain code challenge method is not supported")
		return
	default:
		log.Fatal("Code challenge method %s is invalid", cfg.GenOAuth.CodeChallengeMethod)
		return
	}
	session.Values["codeChallenge"] = codeChallenge
	session.Values["codeVerifier"] = CodeVerifier.Value
}
```

## File: `handlers/login_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package handlers

import (
	"net/http"
	"net/http/httptest"
	"net/url"
	"strings"
	"testing"

	"github.com/google/go-cmp/cmp"
	"github.com/stretchr/testify/assert"
	"github.com/vouch/vouch-proxy/pkg/cfg"
)

func Test_normalizeLoginURL(t *testing.T) {
	setUp("/config/testing/handler_login_url.yml")
	tests := []struct {
		name      string
		url       string
		want      string
		wantStray []string
		wantErr   bool
	}{
		// This is not an RFC-compliant URL because it does not encode :// in the url param; we accept it anyway
		{"extra params", "http://host/login?url=http://host/path?p2=2", "http://host/path?p2=2", []string{}, false},
		{"extra params (blank)", "http://host/login?url=http://host/path?p2=", "http://host/path?p2=", []string{}, false},
		// This is not an RFC-compliant URL because it does not encode :// in the url param; we accept it anyway
		// Even though the p1 param is not a login param, we do not interpret is as part of the url param because it precedes it
		{"prior params", "http://host/login?p1=1&url=http://host/path", "http://host/path", []string{"p1"}, false},
		// This is not an RFC-compliant URL because it does not encode :// in the url param; we accept it anyway
		// We assume vouch-* is a login param and do not fold it into url
		{"vouch-* params after", "http://host/login?url=http://host/path&vouch-xxx=2", "http://host/path", []string{}, false},
		// This is not an RFC-compliant URL because it does not encode :// in the url param; we accept it anyway
		// We assume vouch-* is a login param and do not fold it into url
		{"vouch-* params before", "http://host/login?vouch-xxx=1&url=http://host/path", "http://host/path", []string{}, false},
		// This is not an RFC-compliant URL because it does not encode :// in the url param; we accept it anyway
		// We assume x-vouch-* is a login param and do not fold it into url
		{"x-vouch-* params after", "http://host/login?url=http://host/path&vouch-xxx=2", "http://host/path", []string{}, false},
		// This is not an RFC-compliant URL because it does not encode :// in the url param; we accept it anyway
		// We assume x-vouch-* is a login param and do not fold it into url
		{"x-vouch-* params before", "http://host/login?x-vouch-xxx=1&url=http://host/path", "http://host/path", []string{}, false},
		// This is not an RFC-compliant URL because it does not encode :// in the url param; we accept it anyway
		// Even though p1 is not a login param, we do not interpret is as part of url because it follows a login param (vouch-*)
		{"params after vouch-* params", "http://host/login?url=http://host/path&vouch-xxx=2&p3=3", "http://host/path", []string{"p3"}, false},
		// This is not an RFC-compliant URL because it does not encode :// in the url param; we accept it anyway
		// Even though p1 is not a login param, we do not interpret is as part of url because it follows a login param (x-vouch-*)
		{"params after x-vouch-* params", "http://host/login?url=http://host/path&x-vouch-xxx=2&p3=3", "http://host/path", []string{"p3"}, false},
		// This is not an RFC-compliant URL; it combines all the aspects above
		{"all params", "http://host/login?p1=1&url=http://host/path?p2=2&p3=3&x-vouch-xxx=4&vouch=5&error=6&p7=7", "http://host/path?p2=2&p3=3", []string{"p1", "p7"}, false},
		// This is an RFC-compliant URL
		{"all params (encoded)", "http://host/login?p1=1&url=http%3a%2f%2fhost/path%3fp2=2%26p3=3&x-vouch-xxx=4&vouch=5&error=6&p7=7", "http://host/path?p2=2&p3=3", []string{"p1", "p7"}, false},
		// This is not an RFC-compliant URL; it combines all the aspects above, and it uses semicolons as parameter separators
		// Note that when we fold a stray param into the url param, we always do so with &s
		{"all params (semicolons)", "http://host/login?p1=1;url=http://host/path?p2=2;p3=3;x-vouch-xxx=4;p5=5", "http://host/path?p2=2&p3=3", []string{"p1", "p5"}, false},
		// This is an RFC-compliant URL that uses semicolons as parameter separators
		{"all params (encoded, semicolons)", "http://host/login?p1=1;url=http%3a%2f%2fhost/path%3fp2=2%3bp3=3;x-vouch-xxx=4;p5=5", "http://host/path?p2=2;p3=3", []string{"p1", "p5"}, false},
		// Real world tests
		// since v0.4.0 the vouch README has specified an Nginx config including a 302 redirect in the following format...
		{"Vouch Proxy README (with error)", "http://host/login?url=http://host/path?p2=2&vouch-failcount=3&X-Vouch-Token=TOKEN&error=anerror", "http://host/path?p2=2", []string{}, false},
		{"Vouch Proxy README (blank error)", "http://host/login?url=http://host/path?p2=2&vouch-failcount=&X-Vouch-Token=&error=", "http://host/path?p2=2", []string{}, false},
		{"Vouch Proxy README (semicolons, blank error)", "http://host/login?url=http://host/path?p2=2;p3=3&vouch-failcount=&X-Vouch-Token=&error=", "http://host/path?p2=2&p3=3", []string{}, false},
		// Nginx Ingress controler for Kubernetes adds the parameter `rd` to these calls
		// https://github.com/vouch/vouch-proxy/issues/289
		{"rd param appended by Nginx Ingress", "http://host/login?url=http://host/path?p2=2&p3=3&vouch-failcount=&X-Vouch-Token=&error=&rd=http%3a%2f%2fhost/path%3fp2=2%3bp3=3", "http://host/path?p2=2&p3=3", []string{}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			u, _ := url.Parse(tt.url)
			got, stray, err := normalizeLoginURLParam(u)
			if got.String() != tt.want {
				t.Errorf("normalizeLoginURLParam() = %v, want %v", got, tt.want)
			}
			if !cmp.Equal(stray, tt.wantStray) {
				t.Errorf("normalizeLoginURLParam() stray params incorrectly parsed, got %+q, expected %+q", stray, tt.wantStray)
			}
			if (err != nil) != tt.wantErr {
				t.Errorf("normalizeLoginURLParam() err = %v", err)
			}
		})
	}
}

func Test_getValidRequestedURL(t *testing.T) {
	setUp("/config/testing/handler_login_url.yml")
	r := &http.Request{}
	tests := []struct {
		name    string
		url     string
		want    string
		wantErr bool
	}{
		{"no https", "example.com/dest", "", true},
		{"redirection chaining", "http://example.com/dest?url=https://", "", true},
		{"redirection chaining upper case", "http://example.com/dest?url=HTTPS://someplaceelse.com", "", true},
		{"redirection chaining no protocol", "http://example.com/dest?url=//someplaceelse.com", "", true},
		{"redirection chaining escaped https://", "http://example.com/dest?url=https%3a%2f%2fsomeplaceelse.com", "", true},
		{"data uri", "http://example.com/dest?url=data:text/plain,Example+Text", "", true},
		{"javascript uri", "http://example.com/dest?url=javascript:alert(1)", "", true},
		{"not in domain but contains domain", "http://example.com.somewherelse.com/", "", true},
		{"not in domain", "http://somewherelse.com/", "", true},
		{"should warn", "https://example.com/", "https://example.com/", false},
		{"should be fine", "http://example.com/", "http://example.com/", false},
		{"multiple query param", "http://example.com/?strange=but-true&also-strange=but-false", "http://example.com/?strange=but-true&also-strange=but-false", false},
		{"multiple query params, one of them bad", "http://example.com/?strange=but-true&also-strange=but-false&strange-but-bad=https://badandstrange.com", "", true},
		{"multiple query params, one of them bad (escaped)", "http://example.com/?strange=but-true&also-strange=but-false&strange-but-bad=https%3a%2f%2fbadandstrange.com", "", true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			r.URL, _ = url.Parse("http://vouch.example.com/login?url=" + tt.url)
			got, err := getValidRequestedURL(r)
			if (err != nil) != tt.wantErr {
				t.Errorf("getValidRequestedURL() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if got != tt.want {
				t.Errorf("getValidRequestedURL() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestLoginHandlerDocumentRoot(t *testing.T) {
	handler := http.HandlerFunc(LoginHandler)

	tests := []struct {
		name       string
		configFile string
		wantcode   int
	}{
		{"general test", "/config/testing/handler_login_url_document_root.yml", http.StatusFound},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			setUp(tt.configFile)

			req, err := http.NewRequest("GET", cfg.Cfg.DocumentRoot+"/logout?url=http://myapp.example.com/login", nil)
			req.Header.Set("Host", "my.example.com")
			if err != nil {
				t.Fatal(err)
			}
			rr := httptest.NewRecorder()
			handler.ServeHTTP(rr, req)

			if rr.Code != tt.wantcode {
				t.Errorf("LogoutHandler() status = %v, want %v", rr.Code, tt.wantcode)
			}

			found := false
			for _, c := range rr.Result().Cookies() {
				if c.Name == cfg.Cfg.Session.Name {
					if strings.HasPrefix(c.Path, cfg.Cfg.DocumentRoot+"/auth") {
						found = true
					}
				}
			}
			if !found {
				t.Errorf("session cookie is not set into path that begins with Cfg.DocumentRoot %s", cfg.Cfg.DocumentRoot)
			}

			// confirm the OAuthClient has a properly configured
			redirectURL, err := url.Parse(rr.Header()["Location"][0])
			if err != nil {
				t.Fatal(err)
			}
			redirectParam := redirectURL.Query().Get("redirect_uri")
			assert.NotEmpty(t, cfg.OAuthClient.RedirectURL, "cfg.OAuthClient.RedirectURL is empty")
			assert.NotEmpty(t, redirectParam, "redirect_uri should not be empty when redirected to google oauth")

		})
	}
}
func TestLoginHandler(t *testing.T) {
	handler := http.HandlerFunc(LoginHandler)

	tests := []struct {
		name       string
		configFile string
		wantcode   int
	}{
		{"general test", "/config/testing/handler_login_url.yml", http.StatusFound},
		{"general test", "/config/testing/handler_login_redirecturls.yml", http.StatusFound},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			setUp(tt.configFile)

			req, err := http.NewRequest("GET", "/logout?url=http://myapp.example.com/login", nil)
			if err != nil {
				t.Fatal(err)
			}
			rr := httptest.NewRecorder()
			handler.ServeHTTP(rr, req)

			if rr.Code != tt.wantcode {
				t.Errorf("LogoutHandler() status = %v, want %v", rr.Code, tt.wantcode)
			}

			// confirm the OAuthClient has a properly configured
			redirectURL, err := url.Parse(rr.Header()["Location"][0])
			if err != nil {
				t.Fatal(err)
			}
			redirectParam := redirectURL.Query().Get("redirect_uri")
			assert.NotEmpty(t, cfg.OAuthClient.RedirectURL, "cfg.OAuthClient.RedirectURL is empty")
			assert.NotEmpty(t, redirectParam, "redirect_uri should not be empty when redirected to google oauth")

		})
	}
}
func TestLoginErrTooManyRedirects(t *testing.T) {

	handler := http.HandlerFunc(LoginHandler)

	setUp("/config/testing/handler_login_url.yml")

	tests := []struct {
		name        string
		wantcode    int
		numRequests int
	}{
		{"try the URL a few times", http.StatusFound, failCountLimit}, // after we make successive number of requests up to the failCountLimit ``
		{"then fail ErrTooManyRedirects", http.StatusBadRequest, 1},   // then we generate the error and return `400 Bad Request`
	}

	var rr *httptest.ResponseRecorder
	req, err := http.NewRequest("GET", "/logout?url=http://myapp.example.com/login", nil)
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {

			for i := 0; i < tt.numRequests; i++ {
				if err != nil {
					t.Fatal(err)
				}
				rr = httptest.NewRecorder()
				handler.ServeHTTP(rr, req)

				if rr.Code != tt.wantcode {
					t.Errorf("LogoutHandler() status = %v, want %v", rr.Code, tt.wantcode)
				}

				for _, c := range rr.Result().Cookies() {
					req.AddCookie(c)
				}

			}

		})
	}
}
```

## File: `handlers/logout.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package handlers

import (
	"fmt"
	"net/http"
	"net/url"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/cookie"
	"github.com/vouch/vouch-proxy/pkg/jwtmanager"
	"github.com/vouch/vouch-proxy/pkg/responses"
)

var errUnauthRedirURL = fmt.Errorf("/logout The requested url is not present in `%s.post_logout_redirect_uris`", cfg.Branding.LCName)

// LogoutHandler /logout
// Destroys Vouch session
// If oauth.end_session_endpoint present in conf, also redirects to destroy session at oauth provider
// If "url" param present in request, also redirects to that (after destroying one or both sessions)
func LogoutHandler(w http.ResponseWriter, r *http.Request) {
	log.Debug("/logout")

	jwt := jwtmanager.FindJWT(r)
	claims, err := jwtmanager.ClaimsFromJWT(jwt)
	if err != nil {
		log.Error(err)
	}

	var token = ""
	if claims != nil {
		token = claims.PIdToken
	}

	cookie.ClearCookie(w, r)
	log.Debug("/logout deleting session")
	session, err := sessstore.Get(r, cfg.Cfg.Session.Name)
	session.Options.MaxAge = -1
	if err != nil {
		log.Error(err)
	}
	if err = session.Save(r, w); err != nil {
		log.Error(err)
	}

	providerLogoutURL := cfg.GenOAuth.LogoutURL
	redirectURL := r.URL.Query().Get("url")

	// Make sure that redirectURL, if given, is allowed by config
	if redirectURL != "" {
		redirectValid := false
		for _, allowed := range cfg.Cfg.LogoutRedirectURLs {
			if allowed == redirectURL {
				log.Debugf("/logout found ")
				redirectValid = true
				break
			}
		}
		if !redirectValid {
			responses.Error400(w, r, fmt.Errorf("%w: %s", errUnauthRedirURL, redirectURL))
			return
		}
	}

	// If provider logout URL is configured, redirect to it (and pass redirectURL along)
	// If provider logout URL is not configured, redirect directly to redirectURL
	if providerLogoutURL != "" {
		newRedirectURL, err := url.Parse(providerLogoutURL)
		if err != nil {
			log.Error(err)
		}

		q := newRedirectURL.Query()
		if redirectURL != "" {
			q.Add("post_logout_redirect_uri", redirectURL)
		}
		if token != "" {
			// Optional in spec, required by some providers (Okta, for example)
			q.Add("id_token_hint", token)
		}
		newRedirectURL.RawQuery = q.Encode()
		redirectURL = newRedirectURL.String()
	}

	if redirectURL != "" {
		responses.Redirect302(w, r, redirectURL)
	} else {
		responses.RenderIndex(w, "/logout you have been logged out")
	}
}
```

## File: `handlers/logout_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package handlers

import (
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/vouch/vouch-proxy/pkg/cfg"
)

func TestLogoutHandler(t *testing.T) {
	setUp("/config/testing/handler_logout_url.yml")
	handler := http.HandlerFunc(LogoutHandler)

	tests := []struct {
		name     string
		url      string
		wantcode int
	}{
		{"allowed", "http://myapp.example.com/login", http.StatusFound},
		{"allowed", "https://oauth2.googleapis.com/revoke", http.StatusFound},
		{"not allowed", "http://myapp.example.com/loginagain", http.StatusBadRequest},
		{"not allowed", "http://google.com/", http.StatusBadRequest},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			req, err := http.NewRequest("GET", "/logout?url="+tt.url, nil)
			req.Host = "myapp.example.com"
			if err != nil {
				t.Fatal(err)
			}
			rr := httptest.NewRecorder()
			handler.ServeHTTP(rr, req)
			if rr.Code != tt.wantcode {
				t.Errorf("LogoutHandler() status = %v, want %v", rr.Code, tt.wantcode)
			}
			if rr.Code == http.StatusFound && rr.Header().Get("Location") != tt.url {
				t.Errorf("LogoutHandler() redirect = %s, want %s", rr.Header().Get("Location"), tt.url)
			}
		})
	}
}

func TestProviderLogoutHandler(t *testing.T) {
	setUp("/config/testing/handler_logout_provider.yml")
	handler := http.HandlerFunc(LogoutHandler)

	tests := []struct {
		name     string
		url      string
		wantcode int
	}{
		{"allowed", "http://myapp.example.com/login", http.StatusFound},
		{"allowed", "https://oauth2.googleapis.com/revoke", http.StatusFound},
		{"not allowed", "http://myapp.example.com/loginagain", http.StatusBadRequest},
		{"not allowed", "http://google.com/", http.StatusBadRequest},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			req, err := http.NewRequest("GET", "/logout?url="+tt.url, nil)
			if err != nil {
				t.Fatal(err)
			}
			rr := httptest.NewRecorder()
			handler.ServeHTTP(rr, req)
			if rr.Code != tt.wantcode {
				t.Errorf("LogoutHandler() status = %v, want %v", rr.Code, tt.wantcode)
			}
			if rr.Code == http.StatusFound {
				wanted := tt.url
				req, _ := http.NewRequest("GET", cfg.GenOAuth.LogoutURL, nil)

				q := req.URL.Query()
				q.Add("post_logout_redirect_uri", wanted)
				req.URL.RawQuery = q.Encode()
				wanted = req.URL.String()

				if rr.Header().Get("Location") != wanted {
					t.Errorf("LogoutHandler() redirect = %s, want %s", rr.Header().Get("Location"), wanted)
				}
			}
		})
	}
}
```

## File: `handlers/validate.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package handlers

import (
	"errors"
	"fmt"
	"net/http"
	"reflect"
	"strings"

	"go.uber.org/zap"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/jwtmanager"
	"github.com/vouch/vouch-proxy/pkg/responses"
)

var (
	errNoJWT  = errors.New("no jwt found in request")
	errNoUser = errors.New("no User found in jwt")
)

// ValidateRequestHandler /validate
func ValidateRequestHandler(w http.ResponseWriter, r *http.Request) {
	fastlog.Debug("/validate")

	jwt := jwtmanager.FindJWT(r)
	if jwt == "" {
		send401or200PublicAccess(w, r, errNoJWT)
		return
	}

	claims, err := jwtmanager.ClaimsFromJWT(jwt)
	if err != nil {
		send401or200PublicAccess(w, r, err)
		return
	}

	if claims.Username == "" {
		send401or200PublicAccess(w, r, errNoUser)
		return
	}

	if !cfg.Cfg.AllowAllUsers {
		if !claims.SiteInAudience(r.Host) {
			send401or200PublicAccess(w, r,
				fmt.Errorf("http header 'Host: %s' not authorized for configured `vouch.domains` (is Host being sent properly?)", r.Host))
			return
		}
	}

	generateCustomClaimsHeaders(w, claims)
	w.Header().Add(cfg.Cfg.Headers.User, claims.Username)
	w.Header().Add(cfg.Cfg.Headers.Success, "true")

	if cfg.Cfg.Headers.AccessToken != "" && claims.PAccessToken != "" {
		w.Header().Add(cfg.Cfg.Headers.AccessToken, claims.PAccessToken)
	}
	if cfg.Cfg.Headers.IDToken != "" && claims.PIdToken != "" {
		w.Header().Add(cfg.Cfg.Headers.IDToken, claims.PIdToken)
	}
	// fastlog.Debugf("response headers %+v", w.Header())
	// fastlog.Debug("response header",
	// 	zap.String(cfg.Cfg.Headers.User, w.Header().Get(cfg.Cfg.Headers.User)))
	fastlog.Debug("response header",
		zap.Any("all headers", w.Header()))

	// good to go!!

	if cfg.Cfg.Testing {
		responses.RenderIndex(w, "user authorized "+claims.Username)
	} else {
		responses.OK200(w, r)
	}

	// TODO
	// parse the jwt and see if the claim is valid for the domain

}

func generateCustomClaimsHeaders(w http.ResponseWriter, claims *jwtmanager.VouchClaims) {
	if len(cfg.Cfg.Headers.ClaimsCleaned) > 0 {
		log.Debug("Found claims in config, finding specific keys...")
		// Run through all the claims found
		for k, v := range claims.CustomClaims {
			// Run through the claims we are looking for
			for claim, header := range cfg.Cfg.Headers.ClaimsCleaned {
				// Check for matching claim
				if claim == k {
					log.Debugf("Found matching claim key: %s", k)
					if val, ok := v.([]interface{}); ok {
						strs := make([]string, len(val))
						for i, v := range val {
							strs[i] = fmt.Sprintf("\"%s\"", v)
						}
						log.Debugf("Adding header for claim %s - %s: %s", k, header, val)
						w.Header().Add(header, strings.Join(strs, ","))
					} else {
						// convert to string
						val := fmt.Sprint(v)
						if reflect.TypeOf(val).Kind() == reflect.String {
							// if val, ok := v.(string); ok {
							w.Header().Add(header, val)
							log.Debugf("Adding header for claim %s - %s: %s", k, header, val)
						} else {
							log.Errorf("Couldn't parse header type for %s %+v.  Please submit an issue.", k, v)
						}
					}
				}
			}
		}
	}

}

func send401or200PublicAccess(w http.ResponseWriter, r *http.Request, e error) {
	if cfg.Cfg.PublicAccess {
		log.Debugf("error: %s, but public access is '%v', returning OK200", e, cfg.Cfg.PublicAccess)
		w.Header().Add(cfg.Cfg.Headers.User, "")
		responses.OK200(w, r)
		return
	}

	responses.Error401(w, r, e)
}
```

## File: `handlers/validate_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package handlers

import (
	"net/http"
	"net/http/httptest"
	"os"
	"strings"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	vegeta "github.com/tsenart/vegeta/lib"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/jwtmanager"
	"github.com/vouch/vouch-proxy/pkg/structs"
)

func BenchmarkValidateRequestHandler(b *testing.B) {
	setUp("/config/testing/handler_email.yml")
	user := &structs.User{Username: "testuser", Email: "test@example.com", Name: "Test Name"}
	tokens := structs.PTokens{}
	customClaims := structs.CustomClaims{}

	userTokenString, err := jwtmanager.NewVPJWT(*user, customClaims, tokens)
	assert.NoError(b, err)

	c := &http.Cookie{
		// Name:    cfg.Cfg.Cookie.Name + "_1of1",
		Name:    cfg.Cfg.Cookie.Name,
		Value:   userTokenString,
		Expires: time.Now().Add(1 * time.Hour),
	}

	handler := jwtmanager.JWTCacheHandler(http.HandlerFunc(ValidateRequestHandler))
	// handler := http.HandlerFunc(ValidateRequestHandler)
	ts := httptest.NewServer(handler)
	defer ts.Close()

	req, err := http.NewRequest("GET", "/validate", nil)
	if err != nil {
		b.Fatal(err)
	}
	req.Host = "myapp.example.com"
	req.AddCookie(c)
	w := httptest.NewRecorder()

	for i := 0; i < b.N; i++ {
		handler.ServeHTTP(w, req)
	}

}

func TestValidateRequestHandlerPerf(t *testing.T) {
	if _, ok := os.LookupEnv("ISTRAVIS"); ok {
		t.Skip("travis doesn't like perf tests, skipping")
	}
	if _, ok := os.LookupEnv("SKIPPERFTEST"); ok {
		t.Skip("skipping performance tests")
	}

	setUp("/config/testing/handler_email.yml")
	user := &structs.User{Username: "testuser", Email: "test@example.com", Name: "Test Name"}
	tokens := structs.PTokens{}
	customClaims := structs.CustomClaims{}

	vpjwt, err := jwtmanager.NewVPJWT(*user, customClaims, tokens)
	assert.NoError(t, err)

	c := &http.Cookie{
		// Name:    cfg.Cfg.Cookie.Name + "_1of1",
		Name:    cfg.Cfg.Cookie.Name,
		Value:   vpjwt,
		Expires: time.Now().Add(1 * time.Hour),
	}

	// handler := http.HandlerFunc(ValidateRequestHandler)
	handler := jwtmanager.JWTCacheHandler(http.HandlerFunc(ValidateRequestHandler))
	ts := httptest.NewServer(handler)
	defer ts.Close()

	freq := 1000
	duration := 5 * time.Second

	rate := vegeta.Rate{Freq: freq, Per: time.Second}
	h := &http.Header{}
	h.Add("Cookie", c.String())
	h.Add("Host", "myapp.example.com")
	targeter := vegeta.NewStaticTargeter(vegeta.Target{
		Method: "GET",
		URL:    ts.URL,
		Header: *h,
	})

	attacker := vegeta.NewAttacker()

	var metrics vegeta.Metrics
	mustFail := false
	for res := range attacker.Attack(targeter, rate, duration, "Big Bang!") {
		if res.Code != http.StatusOK {
			t.Logf("/validate perf %d response code %d", res.Seq, res.Code)
			mustFail = true
		}
		metrics.Add(res)
	}
	metrics.Close()

	limit := time.Millisecond
	if mustFail || metrics.Latencies.P95 > limit {
		t.Logf("99th percentile latencies: %s", metrics.Latencies.P99)
		t.Logf("95th percentile latencies: %s", metrics.Latencies.P95)
		t.Logf("50th percentile latencies: %s", metrics.Latencies.P50)
		t.Logf("mean latencies: %s", metrics.Latencies.Mean)
		t.Logf("max latencies: %s", metrics.Latencies.Max)
		t.Logf("/validate 95th percentile latency is higher than %s", limit)
		if mustFail {
			t.Logf("not all requests were %d", http.StatusOK)
		}
		t.FailNow()
	}

}

func TestValidateRequestHandlerWithGroupClaims(t *testing.T) {
	setUp("/config/testing/handler_claims.yml")

	customClaims := structs.CustomClaims{
		Claims: map[string]interface{}{
			"sub": "f:a95afe53-60ba-4ac6-af15-fab870e72f3d:mrtester",
			"groups": []string{
				"Website Users",
				"Test Group",
			},
			"given_name":    "Mister",
			"family_name":   "Tester",
			"email":         "mrtester@test.int",
			"boolean_claim": true,
			// Auth0 custom claim are URLs
			// https://auth0.com/docs/tokens/guides/create-namespaced-custom-claims
			"http://www.example.com/favorite_color": "blue",
		},
	}

	groupHeader := "X-Vouch-IdP-Claims-Groups"
	booleanHeader := "X-Vouch-IdP-Claims-Boolean-Claim"
	familyNameHeader := "X-Vouch-IdP-Claims-Family-Name"
	favoriteColorHeader := "X-Vouch-IdP-Claims-Www-Example-Com-Favorite-Color"

	tokens := structs.PTokens{}

	user := &structs.User{Username: "testuser", Email: "test@example.com", Name: "Test Name"}
	vpjwt, err := jwtmanager.NewVPJWT(*user, customClaims, tokens)
	assert.NoError(t, err)

	req, err := http.NewRequest("GET", "/validate", nil)
	if err != nil {
		t.Fatal(err)
	}

	req.AddCookie(&http.Cookie{
		// Name:    cfg.Cfg.Cookie.Name + "_1of1",
		Name:    cfg.Cfg.Cookie.Name,
		Value:   vpjwt,
		Expires: time.Now().Add(1 * time.Hour),
	})

	rr := httptest.NewRecorder()

	handler := http.HandlerFunc(ValidateRequestHandler)
	handler.ServeHTTP(rr, req)

	if status := rr.Code; status != http.StatusOK {
		t.Errorf("handler returned wrong status code: got %v want %v",
			status, http.StatusOK)
	}

	// Check that the custom claim headers are what we expected
	customClaimHeaders := map[string][]string{
		strings.ToLower(groupHeader):         {},
		strings.ToLower(booleanHeader):       {},
		strings.ToLower(familyNameHeader):    {},
		strings.ToLower(favoriteColorHeader): {},
	}

	for k, v := range rr.Result().Header {
		k = strings.ToLower(k)
		if _, exist := customClaimHeaders[k]; exist {
			customClaimHeaders[k] = v
		}
	}
	expectedCustomClaimHeaders := map[string][]string{
		strings.ToLower(groupHeader):         {"\"Website Users\",\"Test Group\""},
		strings.ToLower(booleanHeader):       {"true"},
		strings.ToLower(familyNameHeader):    {"Tester"},
		strings.ToLower(favoriteColorHeader): {"blue"},
	}
	assert.Equal(t, expectedCustomClaimHeaders, customClaimHeaders)
}

func TestJWTCacheHandler(t *testing.T) {
	setUp("/config/testing/handler_logout_url.yml")
	handler := jwtmanager.JWTCacheHandler(http.HandlerFunc(ValidateRequestHandler))

	user := &structs.User{Username: "testuser", Email: "test@example.com", Name: "Test Name"}
	tokens := structs.PTokens{}
	customClaims := structs.CustomClaims{}

	jwt, err := jwtmanager.NewVPJWT(*user, customClaims, tokens)
	assert.NoError(t, err)
	badjwt := strings.ReplaceAll(jwt, "a", "z")
	badjwt = strings.ReplaceAll(badjwt, "b", "x")

	c := &http.Cookie{
		// Name:    cfg.Cfg.Cookie.Name + "_1of1",
		Name:    cfg.Cfg.Cookie.Name,
		Value:   jwt,
		Expires: time.Now().Add(1 * time.Hour),
		Domain:  cfg.Cfg.Cookie.Domain,
	}

	cBlank := &http.Cookie{
		// Name:    cfg.Cfg.Cookie.Name + "_1of1",
		Name:    cfg.Cfg.Cookie.Name,
		Value:   "",
		Expires: time.Now().Add(1 * time.Hour),
		Domain:  cfg.Cfg.Cookie.Domain,
	}

	tests := []struct {
		name      string
		cookie    *http.Cookie
		bearerJWT string
		wantcode  int
	}{
		// because we're testing the cacheing we run these multiple times
		{"authorized 1", c, "", http.StatusOK},
		{"authorized 2", c, "", http.StatusOK},
		{"notauthorized 1", cBlank, "", http.StatusUnauthorized},
		{"notauthorized 2", cBlank, "", http.StatusUnauthorized},
		{"authorized 3", c, "", http.StatusOK},
		{"bearer 1", nil, jwt, http.StatusOK},
		{"badBearer 1", nil, badjwt, http.StatusUnauthorized},
		// {"badBearer", nil, badjwt, http.StatusUnauthorized},
		{"bearer 2", nil, jwt, http.StatusOK},
		{"badBearer 2", nil, badjwt, http.StatusUnauthorized},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			req, err := http.NewRequest("GET", "/validate", nil)
			req.Host = "myapp.example.com"

			if tt.cookie != nil {
				req.AddCookie(tt.cookie)
			}

			// https://github.com/vouch/vouch-proxy/issues/278
			if tt.bearerJWT != "" {
				req.Header.Add("Authorization", "Bearer "+tt.bearerJWT)
			}

			if err != nil {
				t.Fatal(err)
			}
			rr := httptest.NewRecorder()
			handler.ServeHTTP(rr, req)
			if rr.Code != tt.wantcode {
				t.Errorf("JWTCacheHandler() = %v, want %v", rr.Code, tt.wantcode)
			}
		})
	}
}
```

## File: `pkg/capturewriter/capturewriter.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package capturewriter

import (
	"net/http"
	"strconv"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"go.uber.org/zap"
)

// we wrap ResponseWriter so that we can store the StatusCode
// and then pull it out later for logging
// https://play.golang.org/p/wPHaX9DH-Ik

// var logger *zap.SugaredLogger
var log *zap.Logger

// Configure see main.go configure()
func Configure() {
	// logger = cfg.Logging.Logger
	log = cfg.Logging.FastLogger
}

// CaptureWriter extends http.ResponseWriter
type CaptureWriter struct {
	http.ResponseWriter
	StatusCode int
}

func (w *CaptureWriter) Write(b []byte) (int, error) {
	if w.StatusCode == 0 {
		w.StatusCode = 200
		// log.Debug("CaptureWriter.Write set w.StatusCode " + strconv.Itoa(w.StatusCode))
	}
	return w.ResponseWriter.Write(b)
}

// Header calls http.Writer.Header()
func (w *CaptureWriter) Header() http.Header {
	return w.ResponseWriter.Header()
}

// WriteHeader calls http.Writer.WriteHeader(code)
func (w *CaptureWriter) WriteHeader(code int) {
	w.StatusCode = code
	log.Debug("CaptureWriter.Write set w.StatusCode " + strconv.Itoa(w.StatusCode))
	w.ResponseWriter.WriteHeader(code)
}

// GetStatusCode return w.StatusCode
func (w *CaptureWriter) GetStatusCode() int {
	return w.StatusCode
}
```

## File: `pkg/cfg/cfg.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package cfg

import (
	"bytes"
	"embed"
	"errors"
	"flag"
	"fmt"
	"io"
	"io/fs"
	"net/http"
	"os"
	"os/user"
	"path"
	"path/filepath"
	"reflect"
	"strings"

	"github.com/go-viper/mapstructure/v2"
	"github.com/golang-jwt/jwt/v4"
	"github.com/kelseyhightower/envconfig"
	"github.com/spf13/viper"
	securerandom "github.com/theckman/go-securerandom"
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
)

// Config vouch jwt cookie configuration
// Note to developers!  Any new config elements
// should use `snake_case` such as `post_logout_redirect_uris`
// in certain situations you'll need to add both a `mapstructure` tag used by viper
// as well as a `envconfig` tag used by https://github.com/kelseyhightower/envconfig
// though most of the time envconfig will use the struct key's name: VOUCH_PORT VOUCH_JWT_MAXAGE
// default values should be set in .defaults.yml
type Config struct {
	LogLevel      string   `mapstructure:"logLevel"`
	Listen        string   `mapstructure:"listen"`
	Port          int      `mapstructure:"port"`
	SocketMode    int      `mapstructure:"socket_mode"`
	SocketGroup   string   `mapstructure:"socket_group"`
	DocumentRoot  string   `mapstructure:"document_root" envconfig:"document_root"`
	WriteTimeout  int      `mapstructure:"writeTimeout"`
	ReadTimeout   int      `mapstructure:"readTimeout"`
	IdleTimeout   int      `mapstructure:"idleTimeout"`
	Domains       []string `mapstructure:"domains"`
	WhiteList     []string `mapstructure:"whitelist"`
	TeamWhiteList []string `mapstructure:"teamWhitelist"`
	AllowAllUsers bool     `mapstructure:"allowAllUsers"`
	PublicAccess  bool     `mapstructure:"publicAccess"`
	TLS           struct {
		Cert    string `mapstructure:"cert"`
		Key     string `mapstructure:"key"`
		Profile string `mapstructure:"profile"`
	}
	JWT struct {
		SigningMethod  string `mapstructure:"signing_method"`
		MaxAge         int    `mapstructure:"maxAge"` // in minutes
		Issuer         string `mapstructure:"issuer"`
		Secret         string `mapstructure:"secret"`
		PrivateKeyFile string `mapstructure:"private_key_file"`
		PublicKeyFile  string `mapstructure:"public_key_file"`
		Compress       bool   `mapstructure:"compress"`
	}
	Cookie struct {
		Name     string `mapstructure:"name"`
		Domain   string `mapstructure:"domain"`
		Secure   bool   `mapstructure:"secure"`
		HTTPOnly bool   `mapstructure:"httpOnly"`
		MaxAge   int    `mapstructure:"maxage"`
		SameSite string `mapstructure:"sameSite"`
	}

	Headers struct {
		JWT           string            `mapstructure:"jwt"`
		User          string            `mapstructure:"user"`
		QueryString   string            `mapstructure:"querystring"`
		Redirect      string            `mapstructure:"redirect"`
		Success       string            `mapstructure:"success"`
		Error         string            `mapstructure:"error"`
		ClaimHeader   string            `mapstructure:"claimheader"`
		Claims        []string          `mapstructure:"claims"`
		AccessToken   string            `mapstructure:"accesstoken"`
		IDToken       string            `mapstructure:"idtoken"`
		ClaimsCleaned map[string]string // the rawClaim is mapped to the actual claims header
	}
	Session struct {
		Name   string `mapstructure:"name"`
		MaxAge int    `mapstructure:"maxage"`
		Key    string `mapstructure:"key"`
	}
	TestURL            string   `mapstructure:"test_url"`
	TestURLs           []string `mapstructure:"test_urls"`
	Testing            bool     `mapstructure:"testing"`
	LogoutRedirectURLs []string `mapstructure:"post_logout_redirect_uris" envconfig:"post_logout_redirect_uris"`
}

type branding struct {
	LCName   string // lower case vouch
	UCName   string // UPPER CASE VOUCH
	CcName   string // camelCase Vouch
	FullName string // Vouch Proxy
	URL      string // https://github.com/vouch/vouch-proxy
}

var (
	// Branding that's our name
	Branding = branding{"vouch", "VOUCH", "Vouch", "Vouch Proxy", "https://github.com/vouch/vouch-proxy"}

	// RootDir is where Vouch Proxy looks for ./config/config.yml and ./data
	RootDir string

	secretFile string

	// CmdLine command line arguments
	CmdLine = &cmdLineFlags{
		IsHealthCheck: flag.Bool("healthcheck", false, "invoke healthcheck (check process return value)"),
		port:          flag.Int("port", -1, "port"),
		configFile:    flag.String("config", "", "specify alternate config.yml file as command line arg"),
		// https://github.com/uber-go/zap/blob/master/flag.go
		logLevel: zap.LevelFlag("loglevel", cmdLineLoggingDefault, "set log level to one of: panic, error, warn, info, debug"),
		logTest:  flag.Bool("logtest", false, "print a series of log messages and exit (used for testing)"),
	}

	// Cfg the main exported config variable
	Cfg = &Config{}
	// IsHealthCheck see main.go
	IsHealthCheck = false

	errConfigNotFound = errors.New("configuration file not found")
	// TODO: audit errors and use errConfigIsBad
	// errConfigIsBad    = errors.New("configuration file is malformed")

	// Templates are loaded from the file system with a go:embed directive in main.go
	Templates fs.FS

	// Defaults are loaded from the file system with a go:embed directive in main.go
	Defaults embed.FS
)

type cmdLineFlags struct {
	IsHealthCheck *bool
	port          *int
	configFile    *string
	logLevel      *zapcore.Level
	logTest       *bool
}

const (
	// for a Base64 string we need 44 characters to get 32bytes (6 bits per char)
	minBase64Length = 44
	base64Bytes     = 32

	// ErrCtxKey set or check the http request context to see if it has errored
	// see `responses.Error401` and `jwtmanager.JWTCacheHandler` for example
	ErrCtxKey ctxKey = 0
)

// use a typed ctxKey to avoid context key collision
// https://blog.golang.org/context#TOC_3.2.
type ctxKey int

// Configure called at the very top of main()
// the order of config follows the Viper conventions...
//
// The priority of the sources is the following:
// 1. command line flags
// 2. env. variables
// 3. config file
// 4. defaults
//
// so we process these in backwards order (defaults then config file)
func Configure() {
	logger.Info("Copyright 2020-2023 the " + Branding.FullName + " Authors")
	logger.Warn(Branding.FullName + " is free software with ABSOLUTELY NO WARRANTY.")

	Logging.configureFromCmdline()

	setRootDir()
	secretFile = filepath.Join(RootDir, "config/secret")

	// bail if we're testing
	if flag.Lookup("test.v") != nil {
		log.Debug("`go test` detected, not loading regular config")
		Logging.setLogLevel(zap.WarnLevel)
		return
	}

	setDefaults()
	configFileErr := parseConfigFile()

	didConfigFromEnv := configureFromEnv()

	if !didConfigFromEnv && configFileErr != nil {
		// then it's probably config file not found
		logSysInfo()
		log.Fatal(configFileErr)
	}

	fixConfigOptions()
	Logging.configure()

	if err := configureOauth(); err == nil {
		setProviderDefaults()
	}
	if err := cleanClaimsHeaders(); err != nil {
		log.Fatalf("%w: %w", configFileErr, err)
	}
	if *CmdLine.port != -1 {
		Cfg.Port = *CmdLine.port
	}
	logConfigIfDebug()
}

// using envconfig
// https://github.com/kelseyhightower/envconfig
func configureFromEnv() bool {
	preEnvConfig := *Cfg
	err := envconfig.Process(Branding.UCName, Cfg)
	if err != nil {
		log.Fatal(err.Error())
	}
	preEnvGenOAuth := *GenOAuth

	err = envconfig.Process("OAUTH", GenOAuth)
	if err != nil {
		log.Fatal(err.Error())
	}
	// did anything change?
	if !reflect.DeepEqual(preEnvConfig, *Cfg) ||
		!reflect.DeepEqual(preEnvGenOAuth, *GenOAuth) {

		// set logLevel before calling Log.Debugf()
		if preEnvConfig.LogLevel != Cfg.LogLevel {
			Logging.setLogLevelString(Cfg.LogLevel)
		}
		// log.Debugf("preEnvConfig %+v", preEnvConfig)
		log.Infof("%s configuration set from Environmental Variables", Branding.FullName)
		return true
	}
	return false
}

// ValidateConfiguration confirm the Configuration is valid
func ValidateConfiguration() error {
	if Cfg.Testing {
		// Logging.setLogLevel(zap.DebugLevel)
		Logging.setDevelopmentLogger()
	}

	return basicTest()
}

func setRootDir() {
	// set RootDir from VOUCH_ROOT env var, or to the executable's directory
	if os.Getenv(Branding.UCName+"_ROOT") != "" {
		RootDir = os.Getenv(Branding.UCName + "_ROOT")
		log.Warnf("set cfg.RootDir from VOUCH_ROOT env var: %s", RootDir)
	} else {
		ex, errEx := os.Executable()
		if errEx != nil {
			log.Panic(errEx)
		}
		RootDir = filepath.Dir(ex)
	}
}

// parseConfig parse the config file
func parseConfigFile() error {
	configEnv := os.Getenv(Branding.UCName + "_CONFIG")

	if configEnv != "" {
		log.Warnf("config file loaded from environmental variable %s: %s", Branding.UCName+"_CONFIG", configEnv)
		configFile, _ := filepath.Abs(configEnv)
		viper.SetConfigFile(configFile)
	} else if *CmdLine.configFile != "" {
		log.Infof("config file set on commandline: %s", *CmdLine.configFile)
		viper.AddConfigPath("/")
		viper.AddConfigPath(RootDir)
		viper.AddConfigPath(filepath.Join(RootDir, "config"))
		viper.SetConfigFile(*CmdLine.configFile)
	} else {
		viper.SetConfigName("config")
		viper.SetConfigType("yaml")
		viper.AddConfigPath(filepath.Join(RootDir, "config"))
	}
	err := viper.ReadInConfig() // Find and read the config file
	if err != nil {             // Handle errors reading the config file

		return fmt.Errorf("%w: %s", errConfigNotFound, err)
	}

	if err = checkConfigFileWellFormed(); err != nil {
		log.Error("configuration error: config file should have only two top level elements: `vouch` and `oauth`.  These and other syntax errors follow...")
		log.Error(err)
		log.Error("continuing... (maybe you know what you're doing :)")
	}

	if err = UnmarshalKey(Branding.LCName, &Cfg); err != nil {
		log.Error(err)
	}
	// don't log the secret!
	// log.Debugf("secret: %s", string(Cfg.JWT.Secret))
	return nil
}

// consolidate config related Log.Debugf() calls so that they can be placed *after* we set the logLevel
func logConfigIfDebug() {
	log.Debugf("cfg.RootDir: %s", RootDir)
	// log.Debugf("viper settings %+v", viper.AllSettings())

	// Mask sensitive configuration items before logging
	maskedCfg := *Cfg
	if len(Cfg.Session.Key) != 0 {
		maskedCfg.Session.Key = "XXXXXXXX"
	}
	if len(Cfg.JWT.Secret) != 0 {
		maskedCfg.JWT.Secret = "XXXXXXXX"
	}
	log.Debugf("Cfg %+v", maskedCfg)

	maskedGenOAuth := *GenOAuth
	maskedGenOAuth.ClientID = "12345678"
	maskedGenOAuth.ClientSecret = "XXXXXXXX"
	log.Debugf("cfg.GenOauth %+v", maskedGenOAuth)
}

func fixConfigOptions() {
	if Cfg.Cookie.MaxAge > Cfg.JWT.MaxAge {
		log.Warnf("setting `%s.cookie.maxage` to `%s.jwt.maxage` value of %d minutes (curently set to %d minutes)", Branding.LCName, Branding.LCName, Cfg.JWT.MaxAge, Cfg.Cookie.MaxAge)
		Cfg.Cookie.MaxAge = Cfg.JWT.MaxAge
	}

	// headers defaults
	if !viper.IsSet(Branding.LCName + ".headers.redirect") {
		Cfg.Headers.Redirect = "X-" + Branding.CcName + "-Requested-URI"
	}

	// jwt defaults
	if strings.HasPrefix(Cfg.JWT.SigningMethod, "HS") && len(Cfg.JWT.Secret) == 0 {
		Cfg.JWT.Secret = getOrGenerateJWTSecret()
	}

	if len(Cfg.JWT.PrivateKeyFile) > 0 && !path.IsAbs(Cfg.JWT.PrivateKeyFile) {
		Cfg.JWT.PrivateKeyFile = path.Join(RootDir, Cfg.JWT.PrivateKeyFile)
	}

	if len(Cfg.JWT.PublicKeyFile) > 0 && !path.IsAbs(Cfg.JWT.PublicKeyFile) {
		Cfg.JWT.PublicKeyFile = path.Join(RootDir, Cfg.JWT.PublicKeyFile)
	}

	if len(Cfg.Session.Key) == 0 {
		log.Warn("generating random session.key")
		rstr, err := securerandom.Base64OfBytes(base64Bytes)
		if err != nil {
			log.Fatal(err)
		}
		Cfg.Session.Key = rstr
	}

	if Cfg.TestURL != "" {
		Cfg.TestURLs = append(Cfg.TestURLs, Cfg.TestURL)
	}

}

// use viper and mapstructure check to see if
// https://pkg.go.dev/github.com/spf13/viper@v1.20.1?tab=doc#Unmarshal
// https://github.com/go-viper/mapstructure
func checkConfigFileWellFormed() error {
	opt := func(dc *mapstructure.DecoderConfig) {
		dc.ErrorUnused = true
	}

	type quick struct {
		Vouch Config
		OAuth oauthConfig
	}
	q := &quick{}

	return viper.Unmarshal(q, opt)
}

// UnmarshalKey populate struct from contents of cfg tree at key
func UnmarshalKey(key string, rawVal interface{}) error {
	return viper.UnmarshalKey(key, rawVal)
}

// Get string value for key
func Get(key string) string {
	return viper.GetString(key)
}

// basicTest just a quick sanity check to see if the config is sound
func basicTest() error {
	// check oauth config
	if err := oauthBasicTest(); err != nil {
		return err
	}

	if GenOAuth.Provider == "" {
		return errors.New("configuration error: required configuration option 'oauth.provider' is not set")
	}
	if GenOAuth.ClientID == "" {
		return errors.New("configuration error: required configuration option 'oauth.client_id' is not set")
	}

	// Domains is required _unless_ Cfg.AllowAllUsers is set
	if (!Cfg.AllowAllUsers && len(Cfg.Domains) == 0) ||
		(Cfg.AllowAllUsers && len(Cfg.Domains) > 0) {
		return fmt.Errorf("configuration error: either one of %s or %s needs to be set (but not both)", Branding.LCName+".domains", Branding.LCName+".allowAllUsers")
	}

	// issue a warning if the secret is too small
	log.Debugf("vouch.jwt.secret is %d characters long", len(Cfg.JWT.Secret))

	allowedSigningMethods := map[string]struct{}{
		"HS256": {}, "HS384": {}, "HS512": {}, // HMAC
		"RS256": {}, "RS384": {}, "RS512": {}, // RSA
		"ES256": {}, "ES384": {}, "ES512": {}, // ECDSA
	}
	if _, ok := allowedSigningMethods[Cfg.JWT.SigningMethod]; !ok {
		return fmt.Errorf("configuration error: %s.jwt.signing_method value not allowed", Branding.LCName)
	}

	if strings.HasPrefix(Cfg.JWT.SigningMethod, "HS") {
		if len(Cfg.JWT.PublicKeyFile) > 0 {
			return fmt.Errorf("%s.jwt.public_key_file should not be set when using signing method %s", Branding.LCName, Cfg.JWT.SigningMethod)
		}

		if len(Cfg.JWT.PrivateKeyFile) > 0 {
			return fmt.Errorf("%s.jwt.private_key_file should not be set when using signing method %s", Branding.LCName, Cfg.JWT.SigningMethod)
		}

		if len(Cfg.JWT.Secret) < minBase64Length {
			log.Errorf("Your secret is too short! (%d characters long). Please consider deleting %s to automatically generate a secret of %d characters",
				len(Cfg.JWT.Secret),
				Branding.LCName+".jwt.secret",
				minBase64Length)
		}
	}

	if strings.HasPrefix(Cfg.JWT.SigningMethod, "RS") || strings.HasPrefix(Cfg.JWT.SigningMethod, "ES") {
		if len(Cfg.JWT.Secret) > 0 {
			return fmt.Errorf("%s.jwt.secret should not be set when using signing method %s", Branding.LCName, Cfg.JWT.SigningMethod)
		}

		if len(Cfg.JWT.PublicKeyFile) == 0 {
			return fmt.Errorf("%s.jwt.public_key_file needs to be set for signing method %s", Branding.LCName, Cfg.JWT.SigningMethod)
		}

		if len(Cfg.JWT.PrivateKeyFile) == 0 {
			return fmt.Errorf("%s.jwt.private_key_file needs to be set for signing method %s", Branding.LCName, Cfg.JWT.SigningMethod)
		}
	}

	log.Debugf("vouch.session.key is %d characters long", len(Cfg.Session.Key))
	if len(Cfg.Session.Key) < minBase64Length {
		log.Errorf("Your session key is too short! (%d characters long). Please consider deleting %s to automatically generate a secret of %d characters",
			len(Cfg.Session.Key),
			Branding.LCName+".session.key",
			minBase64Length)
	}
	if Cfg.Cookie.MaxAge < 0 {
		return fmt.Errorf("configuration error: cookie maxAge cannot be lower than 0 (currently: %d)", Cfg.Cookie.MaxAge)
	}
	if Cfg.JWT.MaxAge <= 0 {
		return fmt.Errorf("configuration error: JWT maxAge cannot be zero or lower (currently: %d)", Cfg.JWT.MaxAge)
	}
	if Cfg.Cookie.MaxAge > Cfg.JWT.MaxAge {
		return fmt.Errorf("configuration error: Cookie maxAge (%d) cannot be larger than the JWT maxAge (%d)", Cfg.Cookie.MaxAge, Cfg.JWT.MaxAge)
	}

	// check tls config
	if Cfg.TLS.Key != "" && Cfg.TLS.Cert == "" {
		return fmt.Errorf("configuration error: TLS certificate file not provided but TLS key is set (%s)", Cfg.TLS.Key)
	}
	if Cfg.TLS.Cert != "" && Cfg.TLS.Key == "" {
		return fmt.Errorf("configuration error: TLS key file not provided but TLS certificate is set (%s)", Cfg.TLS.Cert)
	}

	return nil
}

// setDefaults set default options for most items from `.defaults.yml` in the root dir
func setDefaults() {

	// viper.SetConfigName(".defaults")
	viper.SetConfigType("yaml")
	// viper.AddConfigPath(RootDir)
	// viper.ReadInConfig()
	d, err := Defaults.ReadFile(".defaults.yml")
	if err != nil {
		log.Fatal(err)
	}
	viper.ReadConfig(bytes.NewBuffer(d))
	if err := viper.UnmarshalKey(Branding.LCName, &Cfg); err != nil {
		log.Error(err)
	}
	// keep this here for development, we're still pre configurating of LogLevel
	// log.Debugf("setDefaults from .defaults.yml %+v", Cfg)

	// bare minimum for healthcheck achieved
	if *CmdLine.IsHealthCheck {
		return
	}

}

func claimToHeader(claim string) (string, error) {
	was := claim

	// Auth0 allows "namespaceing" of claims and represents them as URLs
	claim = strings.TrimPrefix(claim, "http://")
	claim = strings.TrimPrefix(claim, "https://")

	// not allowed in header: "(),/:;<=>?@[\]{}"
	// https://greenbytes.de/tech/webdav/rfc7230.html#rfc.section.3.2.6
	// and we don't allow underscores `_` or periods `.` because nginx doesn't like them
	// "Valid names are composed of English letters, digits, hyphens, and possibly underscores"
	// as per http://nginx.org/en/docs/http/ngx_http_core_module.html#underscores_in_headers
	for _, r := range `"(),/\:;<=>?@[]{}_.` {
		claim = strings.ReplaceAll(claim, string(r), "-")
	}

	// The field-name must be composed of printable ASCII characters (i.e., characters)
	// that have values between 33. and 126., decimal, except colon).
	// https://github.com/vouch/vouch-proxy/issues/183#issuecomment-564427548
	// get the rune (char) for each claim character
	for _, r := range claim {
		// log.Debugf("claimToHeader rune %c - %d", r, r)
		if r < 33 || r > 126 {
			log.Debugf("%s.header.claims %s includes character %c, replacing with '-'", Branding.CcName, was, r)
			claim = strings.Replace(claim, string(r), "-", 1)
		}
	}
	claim = Cfg.Headers.ClaimHeader + http.CanonicalHeaderKey(claim)
	if claim != was {
		log.Infof("%s.header.claims %s will be forwarded downstream in the Header %s", Branding.CcName, was, claim)
		log.Debugf("nginx will populate the variable $auth_resp_%s", strings.ReplaceAll(strings.ToLower(claim), "-", "_"))
	}
	// log.Errorf("%s.header.claims %s will be forwarded in the Header %s", Branding.CcName, was, claim)
	return claim, nil

}

// fix the claims headers
// https://github.com/vouch/vouch-proxy/issues/183

func cleanClaimsHeaders() error {
	cleanedHeaders := make(map[string]string)
	for _, claim := range Cfg.Headers.Claims {
		header, err := claimToHeader(claim)
		if err != nil {
			return err
		}
		cleanedHeaders[claim] = header
	}
	Cfg.Headers.ClaimsCleaned = cleanedHeaders
	return nil
}

// InitForTestPurposes is called by most *_testing.go files in Vouch Proxy
func InitForTestPurposes() {
	InitForTestPurposesWithProvider("")
}

// InitForTestPurposesWithProvider just for testing
func InitForTestPurposesWithProvider(provider string) {
	Cfg = &Config{} // clear it out since we're called multiple times from subsequent tests

	Logging.setLogLevel(zapcore.InfoLevel)
	setRootDir()
	// _, b, _, _ := runtime.Caller(0)
	// basepath := filepath.Dir(b)
	configEnv := os.Getenv(Branding.UCName + "_CONFIG")
	if configEnv == "" {
		if err := os.Setenv(Branding.UCName+"_CONFIG", filepath.Join(RootDir, "config/testing/test_config.yml")); err != nil {
			log.Error(err)
		}
	}
	// Configure()
	// setRootDir()

	// can't use setDefaults for testing which is go:embed based so we do it the old way
	// setDefaults()
	viper.SetConfigName(".defaults")
	viper.SetConfigType("yaml")
	viper.AddConfigPath(RootDir)
	viper.ReadInConfig()
	if err := UnmarshalKey(Branding.LCName, &Cfg); err != nil {
		log.Error(err)
	}

	// this also mimics the go:embed testing setup
	Templates = os.DirFS(RootDir)

	if err := parseConfigFile(); err != nil {
		log.Error(err)
	}
	configureFromEnv()
	if err := configureOauth(); err == nil {
		setProviderDefaults()
	}
	fixConfigOptions()
	// setDevelopmentLogger()

	// Needed to override the provider, which is otherwise set via yml
	if provider != "" {
		GenOAuth.Provider = provider
		setProviderDefaults()
	}
	_ = cleanClaimsHeaders()

}

func DecryptionKey() (interface{}, error) {
	if strings.HasPrefix(Cfg.JWT.SigningMethod, "HS") {
		return []byte(Cfg.JWT.Secret), nil
	}

	f, err := os.Open(Cfg.JWT.PublicKeyFile)
	if err != nil {
		return nil, fmt.Errorf("error opening Key %s: %s", Cfg.JWT.PublicKeyFile, err)
	}

	keyBytes, err := io.ReadAll(f)
	if err != nil {
		return nil, fmt.Errorf("error reading Key: %s", err)
	}

	var key interface{}
	switch {
	case strings.HasPrefix(Cfg.JWT.SigningMethod, "RS"):
		key, err = jwt.ParseRSAPublicKeyFromPEM(keyBytes)
	case strings.HasPrefix(Cfg.JWT.SigningMethod, "ES"):
		key, err = jwt.ParseECPublicKeyFromPEM(keyBytes)
	default:
		// signingMethod should already have been validated, this should not happen
		return nil, fmt.Errorf("unexpected signing method %s", Cfg.JWT.SigningMethod)
	}

	if err != nil {
		return nil, fmt.Errorf("error parsing Key: %s", err)
	}

	return key, nil
}

func SigningKey() (interface{}, error) {
	if strings.HasPrefix(Cfg.JWT.SigningMethod, "HS") {
		return []byte(Cfg.JWT.Secret), nil
	}

	f, err := os.Open(Cfg.JWT.PrivateKeyFile)
	if err != nil {
		return nil, fmt.Errorf("error opening RSA Key %s: %s", Cfg.JWT.PrivateKeyFile, err)
	}

	keyBytes, err := io.ReadAll(f)
	if err != nil {
		return nil, fmt.Errorf("error reading Key: %s", err)
	}

	var key interface{}
	switch {
	case strings.HasPrefix(Cfg.JWT.SigningMethod, "RS"):
		key, err = jwt.ParseRSAPrivateKeyFromPEM(keyBytes)
	case strings.HasPrefix(Cfg.JWT.SigningMethod, "ES"):
		key, err = jwt.ParseECPrivateKeyFromPEM(keyBytes)
	default:
		// We should have validated this before
		return nil, fmt.Errorf("unexpected signing method %s", Cfg.JWT.SigningMethod)
	}

	if err != nil {
		return nil, fmt.Errorf("error parsing Key: %s", err)
	}

	return key, nil
}

// Check that we have read permission for this file
// https://stackoverflow.com/questions/60128401/how-to-check-if-a-file-is-executable-in-go
func canRead(file string) bool {
	stat, err := os.Stat(file)
	if err != nil {
		log.Debug(err)
		return false
	}

	m := stat.Mode()
	return m&0400 != 0
}

// detect if we're in a docker environment
func isDocker() bool {
	return canRead("/.dockerenv")
}

func logSysInfo() {
	if isDocker() {
		log.Warn("detected Docker environment, beware of Docker userid and permissions changes in v0.36.0")
	}
	u, err := user.Current()
	if err != nil {
		log.Error(err)
	}
	g, err := user.LookupGroupId(u.Gid)
	if err != nil {
		log.Error(err)
	}
	p, err := os.FindProcess(os.Getpid())
	if err != nil {
		log.Error(err)
	}
	exe, err := os.Executable()
	if err != nil {
		log.Error(err)
	}
	log.Debugf("%s was executed as '%s' (pid: %d) running as user %s (uid: %s) with group %s (gid: %s)", Branding.FullName, exe, p.Pid, u.Username, u.Uid, g.Name, u.Gid)
}
```

## File: `pkg/cfg/cfg_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package cfg

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

func setUp(configFile string) {
	os.Setenv("VOUCH_CONFIG", filepath.Join(os.Getenv("VOUCH_ROOT"), configFile))
	InitForTestPurposes()
}

func TestConfigParsing(t *testing.T) {
	InitForTestPurposes()
	Configure()

	// UnmarshalKey(Branding.LCName, &cfg)
	log.Debugf("cfgPort %d", Cfg.Port)
	log.Debugf("cfgDomains %s", Cfg.Domains[0])

	assert.Equal(t, Cfg.Port, 9090)

	assert.NotEmpty(t, Cfg.JWT.MaxAge)

}
func TestConfigEnvPrecedence(t *testing.T) {
	t.Cleanup(cleanupEnv)

	envVar := "OAUTH_CLIENT_SECRET"
	envVal := "testing123"

	os.Setenv(envVar, envVal)
	// Configure()
	setUp("/config/testing/handler_login_url.yml")

	assert.Equal(t, envVal, GenOAuth.ClientSecret)

	// assert.NotEmpty(t, Cfg.JWT.MaxAge)

}

func TestConfigWithTLS(t *testing.T) {
	tests := []struct {
		name        string
		tlsKeyFile  string
		tlsCertFile string
		wantErr     bool
	}{
		{"TLSConfigOK", "/path/to/key", "/path/to/cert", false},
		{"TLSConfigKONoCert", "/path/to/key", "", true},
		{"TLSConfigKONoKey", "", "/path/to/cert", true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Cleanup(cleanupEnv)
			InitForTestPurposes()
			Cfg.TLS.Cert = tt.tlsCertFile
			Cfg.TLS.Key = tt.tlsKeyFile
			err := ValidateConfiguration()

			if (err != nil) != tt.wantErr {
				t.Errorf("error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}
func TestSetGitHubDefaults(t *testing.T) {
	InitForTestPurposesWithProvider("github")
	assert.Equal(t, []string{"read:user"}, GenOAuth.Scopes)
}

func TestSetGitHubDefaultsWithTeamWhitelist(t *testing.T) {
	InitForTestPurposesWithProvider("github")
	Cfg.TeamWhiteList = append(Cfg.TeamWhiteList, "org/team")
	GenOAuth.Scopes = []string{}

	setDefaultsGitHub()
	assert.Contains(t, GenOAuth.Scopes, "read:user")
	assert.Contains(t, GenOAuth.Scopes, "read:org")
}

func TestCheckConfigWithRSA(t *testing.T) {
	setUp("config/testing/test_config_rsa.yml")
	assert.Contains(t, Cfg.JWT.PrivateKeyFile, "config/testing/rsa.key")
	assert.Contains(t, Cfg.JWT.PublicKeyFile, "config/testing/rsa.pub")
}

func Test_claimToHeader(t *testing.T) {
	tests := []struct {
		name    string
		arg     string
		want    string
		wantErr bool
	}{
		{"remove http://", "http://test.example.com", Cfg.Headers.ClaimHeader + "Test-Example-Com", false},
		{"remove https://", "https://test.example.com", Cfg.Headers.ClaimHeader + "Test-Example-Com", false},
		{"auth0 fix https://", "https://test.auth0.com/user", Cfg.Headers.ClaimHeader + "Test-Auth0-Com-User", false},
		{"cognito user:groups", "user:groups", Cfg.Headers.ClaimHeader + "User-Groups", false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := claimToHeader(tt.arg)
			if (err != nil) != tt.wantErr {
				t.Errorf("claimToHeader() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if got != tt.want {
				t.Errorf("claimToHeader() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_configureFromEnvCfg(t *testing.T) {
	t.Cleanup(cleanupEnv)
	// each of these env vars holds a..
	// string
	// get all the values
	senv := []string{"VOUCH_LISTEN", "VOUCH_JWT_ISSUER", "VOUCH_JWT_SECRET", "VOUCH_HEADERS_JWT",
		"VOUCH_HEADERS_USER", "VOUCH_HEADERS_QUERYSTRING", "VOUCH_HEADERS_REDIRECT", "VOUCH_HEADERS_SUCCESS", "VOUCH_HEADERS_ERROR",
		"VOUCH_HEADERS_CLAIMHEADER", "VOUCH_HEADERS_ACCESSTOKEN", "VOUCH_HEADERS_IDTOKEN", "VOUCH_COOKIE_NAME", "VOUCH_COOKIE_DOMAIN",
		"VOUCH_COOKIE_SAMESITE", "VOUCH_TESTURL", "VOUCH_SESSION_NAME", "VOUCH_SESSION_KEY", "VOUCH_DOCUMENT_ROOT", "VOUCH_SOCKETGROUP"}
	// array of strings
	saenv := []string{"VOUCH_DOMAINS", "VOUCH_WHITELIST", "VOUCH_TEAMWHITELIST", "VOUCH_HEADERS_CLAIMS", "VOUCH_TESTURLS", "VOUCH_POST_LOGOUT_REDIRECT_URIS"}
	// int
	ienv := []string{"VOUCH_PORT", "VOUCH_JWT_MAXAGE", "VOUCH_COOKIE_MAXAGE", "VOUCH_SESSION_MAXAGE", "VOUCH_WRITETIMEOUT", "VOUCH_READTIMEOUT",
		"VOUCH_IDLETIMEOUT", "VOUCH_SOCKETMODE"}
	// bool
	benv := []string{"VOUCH_ALLOWALLUSERS", "VOUCH_PUBLICACCESS", "VOUCH_JWT_COMPRESS", "VOUCH_COOKIE_SECURE",
		"VOUCH_COOKIE_HTTPONLY", "VOUCH_TESTING"}

	// populate environmental variables
	svalue := "svalue"
	for _, v := range senv {
		os.Setenv(v, svalue)
	}
	// "VOUCH_LOGLEVEL" is special since logging is occurring during these tests, needs to be an actual level
	os.Setenv("VOUCH_LOGLEVEL", "debug")

	savalue := []string{"arrayone", "arraytwo", "arraythree"}

	for _, v := range saenv {
		os.Setenv(v, strings.Join(savalue, ","))
		t.Logf("savalue: %s", savalue)
	}
	ivalue := 1234
	for _, v := range ienv {
		os.Setenv(v, fmt.Sprint(ivalue))
	}
	bvalue := false
	for _, v := range benv {
		os.Setenv(v, fmt.Sprint(bvalue))
	}

	// run the thing
	configureFromEnv()
	scfg := []string{Cfg.Listen, Cfg.JWT.Issuer, Cfg.JWT.Secret, Cfg.Headers.JWT,
		Cfg.Headers.User, Cfg.Headers.QueryString, Cfg.Headers.Redirect, Cfg.Headers.Success, Cfg.Headers.Error,
		Cfg.Headers.ClaimHeader, Cfg.Headers.AccessToken, Cfg.Headers.IDToken, Cfg.Cookie.Name, Cfg.Cookie.Domain,
		Cfg.Cookie.SameSite, Cfg.TestURL, Cfg.Session.Name, Cfg.Session.Key, Cfg.DocumentRoot, Cfg.SocketGroup,
	}

	sacfg := [][]string{Cfg.Domains, Cfg.WhiteList, Cfg.TeamWhiteList, Cfg.Headers.Claims, Cfg.TestURLs, Cfg.LogoutRedirectURLs}
	icfg := []int{Cfg.Port, Cfg.JWT.MaxAge, Cfg.Cookie.MaxAge, Cfg.WriteTimeout, Cfg.ReadTimeout, Cfg.IdleTimeout, Cfg.SocketMode}
	bcfg := []bool{Cfg.AllowAllUsers, Cfg.PublicAccess, Cfg.JWT.Compress,
		Cfg.Cookie.Secure,
		Cfg.Cookie.HTTPOnly,
		Cfg.Testing,
	}

	tests := []struct {
		name string
	}{
		{"Cfg struct field should be populated from env var"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			assert.Equal(t, Cfg.LogLevel, "debug", "Cfg.LogLevel is not debug")
			for i, v := range scfg {
				assert.Equal(t, svalue, v, fmt.Sprintf("%d: v is %s not %s", i, v, svalue))
			}
			for _, v := range sacfg {
				assert.Equal(t, savalue, v, "v is %+s not %+s", v, savalue)
			}
			for _, v := range icfg {
				assert.Equal(t, ivalue, v, "v is %+s not %+s", v, ivalue)
			}
			for _, v := range bcfg {
				assert.Equal(t, bvalue, v, "v is %+s not %+s", v, bvalue)
			}
		})
	}

}

func Test_configureFromEnvOAuth(t *testing.T) {
	t.Cleanup(cleanupEnv)

	// each of these env vars holds a..
	// string
	// get all the values
	senv := []string{
		"OAUTH_PROVIDER", "OAUTH_CLIENT_ID", "OAUTH_CLIENT_SECRET", "OAUTH_AUTH_URL", "OAUTH_TOKEN_URL",
		"OAUTH_END_SESSION_ENDPOINT", "OAUTH_CALLBACK_URL", "OAUTH_USER_INFO_URL", "OAUTH_USER_TEAM_URL", "OAUTH_USER_ORG_URL",
		"OAUTH_PREFERREDDOMAIN", "OAUTH_RELYING_PARTY_ID",
	}
	// array of strings
	saenv := []string{"OAUTH_CALLBACK_URLS", "OAUTH_SCOPES"}

	// populate environmental variables
	svalue := "svalue"
	for _, v := range senv {
		os.Setenv(v, svalue)
	}
	savalue := []string{"arrayone", "arraytwo", "arraythree"}
	for _, v := range saenv {
		os.Setenv(v, strings.Join(savalue, ","))
		t.Logf("savalue: %s", savalue)
	}

	// run the thing
	configureFromEnv()

	scfg := []string{
		GenOAuth.Provider,
		GenOAuth.ClientID,
		GenOAuth.ClientSecret,
		GenOAuth.AuthURL,
		GenOAuth.TokenURL,
		GenOAuth.LogoutURL,
		GenOAuth.RedirectURL,
		GenOAuth.UserInfoURL,
		GenOAuth.UserTeamURL,
		GenOAuth.UserOrgURL,
		GenOAuth.PreferredDomain,
		GenOAuth.RelyingPartyId,
	}
	sacfg := [][]string{
		GenOAuth.RedirectURLs,
		GenOAuth.Scopes,
	}

	tests := []struct {
		name string
	}{
		{"OAuth struct field should be populated from env var"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			for i, v := range scfg {
				assert.Equal(t, svalue, v, fmt.Sprintf("%d: v is %s not %s", i, v, svalue))
			}
			for i, v := range sacfg {
				assert.Equal(t, savalue, v, fmt.Sprintf("%d: v is %s not %s", i, v, savalue))
			}
		})
	}
}

func cleanupEnv() {
	os.Clearenv()
	os.Setenv(Branding.UCName+"_ROOT", RootDir)
	Cfg = &Config{}
	GenOAuth = &oauthConfig{}
}
```

## File: `pkg/cfg/jwt.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package cfg

import (
	"os"

	securerandom "github.com/theckman/go-securerandom"
)

func getOrGenerateJWTSecret() string {
	b, err := os.ReadFile(secretFile)
	if err == nil {
		log.Info("jwt.secret read from " + secretFile)
	} else {
		// then generate a new secret and store it in the file
		log.Debug(err)
		log.Info("jwt.secret not found in " + secretFile)
		log.Warn("generating random jwt.secret and storing it in " + secretFile)

		// make sure to create 256 bits for the secret
		// see https://github.com/vouch/vouch-proxy/issues/54
		rstr, err := securerandom.Base64OfBytes(base64Bytes)
		if err != nil {
			log.Fatal(err)
		}
		b = []byte(rstr)
		err = os.WriteFile(secretFile, b, 0600)
		if err != nil {
			log.Error(err)
			logSysInfo()
		}
	}
	return string(b)
}
```

## File: `pkg/cfg/logging.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package cfg

import (
	"os"
	"strconv"

	"github.com/spf13/viper"
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
)

type logging struct {
	Logger          *zap.SugaredLogger
	FastLogger      *zap.Logger
	AtomicLogLevel  zap.AtomicLevel
	DefaultLogLevel zapcore.Level
}

var (
	logger *zap.Logger
	log    *zap.SugaredLogger

	// Logging is the public interface to logging
	Logging = &logging{
		AtomicLogLevel:  zap.NewAtomicLevel(),
		DefaultLogLevel: zap.InfoLevel,
	}
)

const cmdLineLoggingDefault = -2

func init() {
	Logging.AtomicLogLevel = zap.NewAtomicLevel()
	// zap needs to start at zapcore.DebugLevel so that it can then be decreased to a lesser level
	Logging.AtomicLogLevel.SetLevel(zapcore.DebugLevel)
	encoderCfg := zap.NewProductionEncoderConfig()
	logger = zap.New(zapcore.NewCore(
		zapcore.NewJSONEncoder(encoderCfg),
		zapcore.Lock(os.Stdout),
		Logging.AtomicLogLevel,
	))

	defer logger.Sync() // flushes buffer, if any
	log = logger.Sugar()
	Logging.FastLogger = logger
	Logging.Logger = log
	// 	Logging.FastLogger = zap.L()
	// 	Logging.Logger = zap.S()
	// 	log = Logging.Logger
	// log.Info("logger set")

}

func (logging) setLogLevel(lvl zapcore.Level) {
	// https://github.com/uber-go/zap/blob/master/zapcore/level.go#L59
	if Logging.AtomicLogLevel.Level() != lvl {
		log.Infof("setting LogLevel to %s", lvl)
		Logging.AtomicLogLevel.SetLevel(lvl)
	}
}

func (logging) setLogLevelString(str string) {
	if err := CmdLine.logLevel.Set(str); err != nil {
		log.Fatal(err)
	}
	Logging.setLogLevel(*CmdLine.logLevel)
}

func (logging) setDevelopmentLogger() {
	// then configure the logger for development output
	clone := Logging.FastLogger.WithOptions(
		zap.WrapCore(
			// func(zapcore.Core) zapcore.Core {
			func(zapcore.Core) zapcore.Core {
				return zapcore.NewCore(zapcore.NewConsoleEncoder(zap.NewDevelopmentEncoderConfig()), zapcore.AddSync(os.Stderr), Logging.AtomicLogLevel)
			}))
	// zap.ReplaceGlobals(clone)
	log = clone.Sugar()
	// Logging.FastLogger = log.Desugar()
	// Logging.Logger = log
	Logging.FastLogger = log.Desugar()
	Logging.Logger = log
	log.Infof("testing: %s, using development console logger", strconv.FormatBool(Cfg.Testing))
}

var configured = false

func (logging) configure() {
	// logging

	if configured {
		return
	}

	// then we weren't configured via command line, check the config file
	if !viper.IsSet(Branding.LCName + ".logLevel") {
		// then we weren't configured via the config file, set the default
		Cfg.LogLevel = Logging.DefaultLogLevel.String()
	}

	if Cfg.LogLevel != Logging.AtomicLogLevel.Level().String() {
		// log.Errorf("Logging.configure() Logging.LogLevel %s Cfg.LogLevel %s", Logging.LogLeveLogging.String(), Cfg.LogLevel)
		Logging.setLogLevelString(Cfg.LogLevel)
	}

	// if we're supposed to run tests, run tests and exit
	if *CmdLine.logTest {
		Logging.cmdlineTestLogs()
	}

	configured = true
}

func (logging) configureFromCmdline() {

	if *CmdLine.logLevel != cmdLineLoggingDefault {
		Logging.setLogLevel(*CmdLine.logLevel) // defaults to Logging.DefaultLogLevel which is zap.InfoLevel
		log.Info("logging configured from cmdline")
		// if we're supposed to run tests, run tests and exit
		if *CmdLine.logTest {
			Logging.cmdlineTestLogs()
		}

		configured = true
	}
}

// in support of `./do.sh test_logging`
func (logging) cmdlineTestLogs() {
	Logging.Logger.Error("error")
	Logging.Logger.Warn("warn")
	Logging.Logger.Info("info")
	Logging.Logger.Debug("debug")
	// Logging.Logger.Panic("panic")
	os.Exit(0)
}
```

## File: `pkg/cfg/logging_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package cfg

import (
	"fmt"
	"testing"

	"go.uber.org/zap/zapcore"
	"go.uber.org/zap/zaptest/observer"
)

func Test_logging_setLogLevel(t *testing.T) {
	_, obs := observer.New(Logging.AtomicLogLevel)
	// type args struct {
	// }
	tests := []struct {
		name string
		lvl  zapcore.Level
	}{
		{"debug", zapcore.DebugLevel},
		{"info", zapcore.InfoLevel},
		{"warn", zapcore.WarnLevel},
		{"error", zapcore.ErrorLevel},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			Logging.setLogLevel(tt.lvl)
			Logging.Logger.Debugf("%s %d", tt.name, tt.lvl)
			Logging.Logger.Infof("%s %d", tt.name, tt.lvl)
			Logging.Logger.Warnf("%s %d", tt.name, tt.lvl)
			Logging.Logger.Errorf("%s %d", tt.name, tt.lvl)

			for _, logEntry := range obs.All() {
				fmt.Printf("logEntry: %+v", logEntry)
				if logEntry.Level < tt.lvl {
					t.Errorf("should not have log level of %s", logEntry.Level)
				}
				t.Logf("tt.name %s", tt.name)
			}
		})
	}
}
```

## File: `pkg/cfg/oauth.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package cfg

import (
	"encoding/json"
	"errors"
	"fmt"
	"strings"

	"golang.org/x/oauth2"
	"golang.org/x/oauth2/github"
	"golang.org/x/oauth2/google"
)

var (
	// GenOAuth exported OAuth config variable
	// TODO: GenOAuth and OAuthClient should be combined
	GenOAuth = &oauthConfig{}

	// OAuthClient is the configured client which will call the provider
	// this actually carries the oauth2 client ala oauthclient.Client(oauth2.NoContext, providerToken)
	OAuthClient *oauth2.Config
	// OAuthopts authentication options
	OAuthopts []oauth2.AuthCodeOption

	// Providers static strings to test against
	Providers = &OAuthProviders{
		Google:        "google",
		GitHub:        "github",
		IndieAuth:     "indieauth",
		ADFS:          "adfs",
		Azure:         "azure",
		OIDC:          "oidc",
		HomeAssistant: "homeassistant",
		OpenStax:      "openstax",
		Nextcloud:     "nextcloud",
		Alibaba:       "alibaba",
		Discord:       "discord",
	}
)

// OAuthProviders holds the stings for
type OAuthProviders struct {
	Google        string
	GitHub        string
	IndieAuth     string
	ADFS          string
	Azure         string
	OIDC          string
	HomeAssistant string
	OpenStax      string
	Nextcloud     string
	Alibaba       string
	Discord       string
}

// oauth config items endoint for access
// `envconfig` tag is for env var support
// https://github.com/kelseyhightower/envconfig
type oauthConfig struct {
	Provider       string   `mapstructure:"provider"`
	ClientID       string   `mapstructure:"client_id" envconfig:"client_id"`
	ClientSecret   string   `mapstructure:"client_secret" envconfig:"client_secret"`
	AuthURL        string   `mapstructure:"auth_url" envconfig:"auth_url"`
	TokenURL       string   `mapstructure:"token_url" envconfig:"token_url"`
	LogoutURL      string   `mapstructure:"end_session_endpoint"  envconfig:"end_session_endpoint"`
	RedirectURL    string   `mapstructure:"callback_url"  envconfig:"callback_url"`
	RedirectURLs   []string `mapstructure:"callback_urls"  envconfig:"callback_urls"`
	RelyingPartyId string   `mapstructure:"relying_party_id"  envconfig:"relying_party_id"`
	Scopes         []string `mapstructure:"scopes"`
	// pointer-to-pointer so that the default uninitialized value is nil
	Claims              **oauthClaimsConfig `mapstructure:"claims"`
	UserInfoURL         string              `mapstructure:"user_info_url" envconfig:"user_info_url"`
	UserTeamURL         string              `mapstructure:"user_team_url" envconfig:"user_team_url"`
	UserOrgURL          string              `mapstructure:"user_org_url" envconfig:"user_org_url"`
	PreferredDomain     string              `mapstructure:"preferredDomain"`
	AzureToken          string              `mapstructure:"azure_token" envconfig:"azure_token"`
	CodeChallengeMethod string              `mapstructure:"code_challenge_method" envconfig:"code_challenge_method"`
	// DiscordUseIDs defaults to false, maintaining the more common username checking behavior
	// If set to true, match the Discord user's ID instead of their username
	DiscordUseIDs bool `mapstructure:"discord_use_ids" envconfig:"discord_use_ids"`
}

type oauthClaimsConfig struct {
	UserInfo map[string]*oauthClaimValueConfig `mapstructure:"userinfo" json:"userinfo,omitempty"`
	IDToken  map[string]*oauthClaimValueConfig `mapstructure:"id_token" json:"id_token,omitempty"`
}

type oauthClaimValueConfig struct {
	Essential bool          `mapstructure:"essential" json:"essential,omitempty"`
	Value     interface{}   `mapstructure:"value" json:"value,omitempty"`
	Values    []interface{} `mapstructure:"values" json:"values,omitempty"`
}

func configureOauth() error {
	// OAuth defaults and client configuration
	if err := UnmarshalKey("oauth", &GenOAuth); err != nil {
		return err
	}
	if GenOAuth.Claims != nil {
		claims, err := json.Marshal(GenOAuth.Claims)
		if err != nil {
			return err
		}
		log.Infof("setting OAuth param 'claims' to %s", claims)
		OAuthopts = append(OAuthopts, oauth2.SetAuthURLParam("claims", string(claims)))
	}
	return nil
}

func oauthBasicTest() error {
	if GenOAuth.Provider != Providers.Google &&
		GenOAuth.Provider != Providers.GitHub &&
		GenOAuth.Provider != Providers.IndieAuth &&
		GenOAuth.Provider != Providers.HomeAssistant &&
		GenOAuth.Provider != Providers.ADFS &&
		GenOAuth.Provider != Providers.Azure &&
		GenOAuth.Provider != Providers.OIDC &&
		GenOAuth.Provider != Providers.OpenStax &&
		GenOAuth.Provider != Providers.Nextcloud &&
		GenOAuth.Provider != Providers.Alibaba &&
		GenOAuth.Provider != Providers.Discord {
		return errors.New("configuration error: Unknown oauth provider: " + GenOAuth.Provider)
	}
	// OAuthconfig Checks
	switch {
	case GenOAuth.ClientID == "":
		// everyone has a clientID
		return errors.New("configuration error: oauth.client_id not found")
	case GenOAuth.Provider != Providers.IndieAuth && GenOAuth.Provider != Providers.HomeAssistant && GenOAuth.Provider != Providers.ADFS && GenOAuth.Provider != Providers.OIDC && GenOAuth.ClientSecret == "":
		// everyone except IndieAuth has a clientSecret
		// ADFS and OIDC providers also do not require this, but can have it optionally set.
		return errors.New("configuration error: oauth.client_secret not found")
	case GenOAuth.Provider != Providers.Google && GenOAuth.AuthURL == "":
		// everyone except IndieAuth and Google has an authURL
		return errors.New("configuration error: oauth.auth_url not found")
	case GenOAuth.Provider != Providers.Google && GenOAuth.Provider != Providers.IndieAuth && GenOAuth.Provider != Providers.HomeAssistant && GenOAuth.Provider != Providers.ADFS && GenOAuth.Provider != Providers.Azure && GenOAuth.UserInfoURL == "":
		// everyone except IndieAuth, Google and ADFS has an userInfoURL, and Azure does not actively use it
		return errors.New("configuration error: oauth.user_info_url not found")
	case GenOAuth.Provider != Providers.Discord && GenOAuth.DiscordUseIDs:
		return errors.New("configuration error: discord_use_ids is true but oauth.provider is not 'discord'")
	case GenOAuth.CodeChallengeMethod != "" && (GenOAuth.CodeChallengeMethod != "plain" && GenOAuth.CodeChallengeMethod != "S256"):
		return errors.New("configuration error: oauth.code_challenge_method must be either 'S256' or 'plain'")
	case GenOAuth.Provider == Providers.Azure || GenOAuth.Provider == Providers.ADFS || GenOAuth.Provider == Providers.Nextcloud || GenOAuth.Provider == Providers.OIDC:
		checkScopes([]string{"openid", "email", "profile"})
	}

	if GenOAuth.RedirectURL != "" {
		if err := checkCallbackConfig(GenOAuth.RedirectURL); err != nil {
			return err
		}
	}
	if len(GenOAuth.RedirectURLs) > 0 {
		for _, cb := range GenOAuth.RedirectURLs {
			if err := checkCallbackConfig(cb); err != nil {
				return err
			}
		}
	}

	return nil
}

func checkScopes(scopes []string) {
	for _, s := range scopes {
		if !arrContains(GenOAuth.Scopes, s) {
			log.Warnf("Configuration Warning: for 'oauth.provider: %s', 'oauth.scopes' should usually contain: -%s", GenOAuth.Provider, strings.Join(scopes, " -"))
			return
		}
	}
}

// TODO: all of these methods should become `provider.SetDefaults()` or `provider.SetDefaults(*GenOAuth)`
func setProviderDefaults() {
	if GenOAuth.Provider == Providers.Google {
		setDefaultsGoogle()
		// setDefaultsGoogle also configures the OAuthClient
	} else if GenOAuth.Provider == Providers.GitHub {
		setDefaultsGitHub()
		configureOAuthClient()
	} else if GenOAuth.Provider == Providers.ADFS {
		setDefaultsADFS()
		configureOAuthClient()
	} else if GenOAuth.Provider == Providers.Azure {
		setDefaultsAzure()
		configureOAuthClient()
	} else if GenOAuth.Provider == Providers.IndieAuth {
		GenOAuth.CodeChallengeMethod = "S256"
		configureOAuthClient()
	} else if GenOAuth.Provider == Providers.Discord {
		setDefaultsDiscord()
		configureOAuthClient()
	} else {
		// OIDC, OpenStax, Nextcloud
		configureOAuthClient()
	}
}

func setDefaultsGoogle() {
	log.Info("configuring Google OAuth")
	GenOAuth.UserInfoURL = "https://www.googleapis.com/oauth2/v3/userinfo"
	if len(GenOAuth.Scopes) == 0 {
		// You have to select a scope from
		// https://developers.google.com/identity/protocols/googlescopes#google_sign-in
		GenOAuth.Scopes = []string{"email"}
	}
	OAuthClient = &oauth2.Config{
		ClientID:     GenOAuth.ClientID,
		ClientSecret: GenOAuth.ClientSecret,
		Scopes:       GenOAuth.Scopes,
		Endpoint:     google.Endpoint,
		RedirectURL:  GenOAuth.RedirectURL,
	}
	if GenOAuth.PreferredDomain != "" {
		log.Infof("setting Google OAuth preferred login domain param 'hd' to %s", GenOAuth.PreferredDomain)
		OAuthopts = append(OAuthopts, oauth2.SetAuthURLParam("hd", GenOAuth.PreferredDomain))
	}
	GenOAuth.CodeChallengeMethod = "S256"
}

func setDefaultsADFS() {
	log.Info("configuring ADFS OAuth")

	if GenOAuth.RelyingPartyId == "" {
		GenOAuth.RelyingPartyId = GenOAuth.RedirectURL
	}

	OAuthopts = append(OAuthopts, oauth2.SetAuthURLParam("resource", GenOAuth.RelyingPartyId))
}

func setDefaultsAzure() {
	log.Info("configuring Azure OAuth")
	if len(GenOAuth.AzureToken) == 0 {
		log.Info("Using Default Azure Token: access_token")
		GenOAuth.AzureToken = "access_token"
	} else if GenOAuth.AzureToken == "access_token" {
		log.Info("Using Azure Token: access_token")
	} else if GenOAuth.AzureToken == "id_token" {
		log.Info("Using Azure Token: id_token")
	} else {
		log.Fatal("'oauth.azure_token' must be either 'access_token' or 'id_token'")
	}
	GenOAuth.CodeChallengeMethod = "S256"
}

func setDefaultsGitHub() {
	// log.Info("configuring GitHub OAuth")
	if GenOAuth.AuthURL == "" {
		GenOAuth.AuthURL = github.Endpoint.AuthURL
	}
	if GenOAuth.TokenURL == "" {
		GenOAuth.TokenURL = github.Endpoint.TokenURL
	}
	if GenOAuth.UserInfoURL == "" {
		GenOAuth.UserInfoURL = "https://api.github.com/user"
	}
	if GenOAuth.UserTeamURL == "" {
		GenOAuth.UserTeamURL = "https://api.github.com/orgs/:org_id/teams/:team_slug/memberships/:username"
	}
	if GenOAuth.UserOrgURL == "" {
		GenOAuth.UserOrgURL = "https://api.github.com/orgs/:org_id/members/:username"
	}
	if len(GenOAuth.Scopes) == 0 {
		// https://github.com/vouch/vouch-proxy/issues/63
		// https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/
		GenOAuth.Scopes = []string{"read:user"}

		if len(Cfg.TeamWhiteList) > 0 {
			GenOAuth.Scopes = append(GenOAuth.Scopes, "read:org")
		}
	}
	GenOAuth.CodeChallengeMethod = "S256"
}

func setDefaultsDiscord() {
	// log.Info("configuring GitHub OAuth")
	if GenOAuth.AuthURL == "" {
		GenOAuth.AuthURL = "https://discord.com/oauth2/authorize"
	}
	if GenOAuth.TokenURL == "" {
		GenOAuth.TokenURL = "https://discord.com/api/oauth2/token"
	}
	if GenOAuth.UserInfoURL == "" {
		GenOAuth.UserInfoURL = "https://discord.com/api/users/@me"
	}
	if len(GenOAuth.Scopes) == 0 {
		//Required for UserInfo URL
		//https://discord.com/developers/docs/resources/user#get-current-user
		GenOAuth.Scopes = []string{"identify", "email"}
	}
	GenOAuth.CodeChallengeMethod = "S256"
}

func configureOAuthClient() {
	log.Infof("configuring %s OAuth with Endpoint %s", GenOAuth.Provider, GenOAuth.AuthURL)
	OAuthClient = &oauth2.Config{
		ClientID:     GenOAuth.ClientID,
		ClientSecret: GenOAuth.ClientSecret,
		Endpoint: oauth2.Endpoint{
			AuthURL:  GenOAuth.AuthURL,
			TokenURL: GenOAuth.TokenURL,
		},
		RedirectURL: GenOAuth.RedirectURL,
		Scopes:      GenOAuth.Scopes,
	}
}

func checkCallbackConfig(url string) error {
	if !strings.Contains(url, "/auth") {
		log.Errorf("configuration error: oauth.callback_url (%s) should almost always point at the vouch-proxy '/auth' endpoint", url)
	}

	found := false
	for _, d := range append(Cfg.Domains, Cfg.Cookie.Domain) {
		if d != "" && strings.Contains(url, d) {
			found = true
			break
		}
	}
	if !found {
		return fmt.Errorf("configuration error: oauth.callback_url (%s) must be within a configured domains where the cookie will be set: either `vouch.domains` %s or `vouch.cookie.domain` %s",
			url,
			Cfg.Domains,
			Cfg.Cookie.Domain)
	}

	return nil
}

func arrContains(arr []string, str string) bool {
	for _, v := range arr {
		if v == str {
			return true
		}
	}
	return false
}
```

## File: `pkg/cfg/oauth_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package cfg

import (
	"net/url"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_checkCallbackConfig(t *testing.T) {
	setUp("/config/testing/handler_login_url.yml")

	tests := []struct {
		name    string
		url     string
		wantErr bool
	}{
		{"correct", "http://vouch.example.com:9090/auth", false},
		{"bad", "http://vouch.notgonna.com:9090/somewhereelse", true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if err := checkCallbackConfig(tt.url); (err != nil) != tt.wantErr {
				t.Errorf("checkCallbackConfig() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func Test_configureOAuthWithClaims(t *testing.T) {
	setUp("/config/testing/test_config_oauth_claims.yml")
	authCodeURL, err := url.Parse(OAuthClient.AuthCodeURL("state", OAuthopts...))
	assert.Nil(t, err)
	assert.Equal(t, authCodeURL.Query().Get("claims"), `{"userinfo":{"email":{"essential":true},"email_verified":{"essential":true},"given_name":{"essential":true},"http://example.info/claims/groups":null,"nickname":null,"picture":null},"id_token":{"acr":{"values":["urn:mace:incommon:iap:silver"]},"auth_time":{"essential":true}}}`)
}
```

## File: `pkg/cfg/tls.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package cfg

import (
	"crypto/tls"
)

// TLSConfig config returns a *tls.Config with the specified profile (modern, intermediate, old, default) configuration.
func TLSConfig(profile string) *tls.Config {
	c := &tls.Config{}

	// Source: https://ssl-config.mozilla.org/#server=go&version=1.14&config=modern&hsts=false&guideline=5.6
	switch profile {
	case "modern":
		c = &tls.Config{
			MinVersion: tls.VersionTLS13,
		}
	case "intermediate":
		c = &tls.Config{
			MinVersion:               tls.VersionTLS12,
			CurvePreferences:         []tls.CurveID{tls.CurveP521, tls.CurveP384, tls.CurveP256},
			PreferServerCipherSuites: true,
			CipherSuites: []uint16{
				tls.TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,
				tls.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,
				tls.TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,
				tls.TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,
				tls.TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305,
				tls.TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305,
			},
		}
	case "old":
		c = &tls.Config{
			MinVersion:               tls.VersionTLS10,
			PreferServerCipherSuites: true,
			CipherSuites: []uint16{
				tls.TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,
				tls.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,
				tls.TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,
				tls.TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,
				tls.TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305,
				tls.TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305,
				tls.TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256,
				tls.TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256,
				tls.TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA,
				tls.TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA,
				tls.TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA,
				tls.TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA,
				tls.TLS_RSA_WITH_AES_128_GCM_SHA256,
				tls.TLS_RSA_WITH_AES_256_GCM_SHA384,
				tls.TLS_RSA_WITH_AES_128_CBC_SHA256,
				tls.TLS_RSA_WITH_AES_128_CBC_SHA,
				tls.TLS_RSA_WITH_AES_256_CBC_SHA,
				tls.TLS_RSA_WITH_3DES_EDE_CBC_SHA,
			},
		}
	}

	return c
}
```

## File: `pkg/cfg/tls_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package cfg

import (
	"crypto/tls"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTLSConfig(t *testing.T) {
	tests := []struct {
		name              string
		profile           string
		wantTLSMinVersion uint16
	}{
		{"TLSDefaultProfile", "", 0},
		{"TLSModernProfile", "modern", tls.VersionTLS13},
		{"TLSIntermediateProfile", "intermediate", tls.VersionTLS12},
		{"TLSOldProfile", "old", tls.VersionTLS10},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tlsConfig := TLSConfig(tt.profile)
			assert.Equal(t, tt.wantTLSMinVersion, tlsConfig.MinVersion)
		})
	}
}
```

## File: `pkg/cookie/cookie.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package cookie

import (
	"errors"
	"fmt"
	"net/http"
	"strconv"
	"strings"
	"unicode/utf8"

	// "github.com/vouch/vouch-proxy/pkg/structs"
	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/domains"
	"go.uber.org/zap"
)

const maxCookieSize = 4000

var log *zap.SugaredLogger
var sameSite http.SameSite

// Configure see main.go configure()
func Configure() {
	log = cfg.Logging.Logger
	sameSite = SameSite()
}

// SetCookie http
func SetCookie(w http.ResponseWriter, r *http.Request, val string) {
	setCookie(w, r, val, cfg.Cfg.Cookie.MaxAge*60) // convert minutes to seconds
}

func setCookie(w http.ResponseWriter, r *http.Request, val string, maxAge int) {
	cookieName := cfg.Cfg.Cookie.Name
	// foreach domain
	domain := domains.Matches(r.Host)
	// Allow overriding the cookie domain in the config file
	if cfg.Cfg.Cookie.Domain != "" {
		domain = cfg.Cfg.Cookie.Domain
		log.Debugf("setting the cookie domain to %v", domain)
	}

	cookie := http.Cookie{
		Name:     cfg.Cfg.Cookie.Name,
		Value:    val,
		Path:     "/",
		Domain:   domain,
		MaxAge:   maxAge,
		Secure:   cfg.Cfg.Cookie.Secure,
		HttpOnly: cfg.Cfg.Cookie.HTTPOnly,
		SameSite: sameSite,
	}
	cookieSize := len(cookie.String())
	cookie.Value = ""
	emptyCookieSize := len(cookie.String())
	// Cookies have a max size of 4096 bytes, but to support most browsers, we should stay below 4000 bytes
	// https://tools.ietf.org/html/rfc6265#section-6.1
	// http://browsercookielimits.squawky.net/
	if cookieSize > maxCookieSize {
		// https://www.lifewire.com/cookie-limit-per-domain-3466809
		log.Warnf("cookie size: %d.  cookie sizes over ~4093 bytes(depending on the browser and platform) have shown to cause issues or simply aren't supported.", cookieSize)
		cookieParts := splitCookie(val, maxCookieSize-emptyCookieSize)
		for i, cookiePart := range cookieParts {
			// Cookies are named 1of3, 2of3, 3of3
			cookieName = fmt.Sprintf("%s_%dof%d", cfg.Cfg.Cookie.Name, i+1, len(cookieParts))
			http.SetCookie(w, &http.Cookie{
				Name:     cookieName,
				Value:    cookiePart,
				Path:     "/",
				Domain:   domain,
				MaxAge:   maxAge,
				Secure:   cfg.Cfg.Cookie.Secure,
				HttpOnly: cfg.Cfg.Cookie.HTTPOnly,
				SameSite: sameSite,
			})
		}
	} else {
		http.SetCookie(w, &http.Cookie{
			Name:     cookieName,
			Value:    val,
			Path:     "/",
			Domain:   domain,
			MaxAge:   maxAge,
			Secure:   cfg.Cfg.Cookie.Secure,
			HttpOnly: cfg.Cfg.Cookie.HTTPOnly,
			SameSite: sameSite,
		})
	}
}

// Cookie get the vouch jwt cookie
func Cookie(r *http.Request) (string, error) {

	cookieParts := make([]string, 0)
	var numParts = -1

	var err error
	cookies := r.Cookies()
	// Get the remaining parts
	// search for cookie parts in order
	// this is the hotpath so we're trying to only walk once
	for _, cookie := range cookies {
		if cookie.Name == cfg.Cfg.Cookie.Name {
			return cookie.Value, nil
		}
		cookieUnder := fmt.Sprintf("%s_", cfg.Cfg.Cookie.Name)
		if strings.HasPrefix(cookie.Name, cookieUnder) {
			log.Debugw("cookie",
				"cookieName", cookie.Name,
				"cookieValue", cookie.Value,
			)
			xOFy := strings.Replace(cookie.Name, cookieUnder, "", 1)
			xyArray := strings.Split(xOFy, "of")
			if numParts == -1 { // then its uninitialized
				if numParts, err = strconv.Atoi(xyArray[1]); err != nil {
					return "", fmt.Errorf("multipart cookie fail: %s", err)
				}
				log.Debugf("make cookieParts of size %d", numParts)
				cookieParts = make([]string, numParts)
			}
			var i int
			if i, err = strconv.Atoi(xyArray[0]); err != nil {
				return "", fmt.Errorf("multipart cookie fail: %s", err)
			}
			cookieParts[i-1] = cookie.Value
		}

	}
	// combinedCookieStr := combinedCookie.String()
	combinedCookieStr := strings.Join(cookieParts, "")
	if combinedCookieStr == "" {
		return "", errors.New("cookie token empty")
	}

	log.Debugw("combined cookie",
		"cookieValue", combinedCookieStr,
	)
	return combinedCookieStr, err
}

// ClearCookie get rid of the existing cookie
func ClearCookie(w http.ResponseWriter, r *http.Request) {
	cookies := r.Cookies()
	domain := domains.Matches(r.Host)
	// Allow overriding the cookie domain in the config file
	if cfg.Cfg.Cookie.Domain != "" {
		domain = cfg.Cfg.Cookie.Domain
		log.Debugf("setting the cookie domain to %v", domain)
	}
	// search for cookie parts
	for _, cookie := range cookies {
		if strings.HasPrefix(cookie.Name, cfg.Cfg.Cookie.Name) {
			log.Debugf("deleting cookie: %s", cookie.Name)
			http.SetCookie(w, &http.Cookie{
				Name:     cookie.Name,
				Value:    "delete",
				Path:     "/",
				Domain:   domain,
				MaxAge:   -1,
				Secure:   cfg.Cfg.Cookie.Secure,
				HttpOnly: cfg.Cfg.Cookie.HTTPOnly,
			})
		}
	}
}

// SameSite return cfg.Cfg.Cookie.SameSite as http.Samesite
// if cfg.Cfg.Cookie.SameSite is unconfigured return http.SameSite(0)
// see https://github.com/vouch/vouch-proxy/issues/210
func SameSite() http.SameSite {
	sameSite := http.SameSite(0)
	if cfg.Cfg.Cookie.SameSite != "" {
		switch strings.ToLower(cfg.Cfg.Cookie.SameSite) {
		case "lax":
			sameSite = http.SameSiteLaxMode
		case "strict":
			sameSite = http.SameSiteStrictMode
		case "none":
			if !cfg.Cfg.Cookie.Secure {
				log.Error("SameSite cookie attribute with sameSite=none should also be specified with secure=true.")
			}
			sameSite = http.SameSiteNoneMode
		}
	}
	return sameSite
}

// splitCookie separate string into several strings of specified length
func splitCookie(longString string, maxLen int) []string {
	splits := make([]string, 0)

	var l, r int
	for l, r = 0, maxLen; r < len(longString); l, r = r, r+maxLen {
		for !utf8.RuneStart(longString[r]) {
			r--
		}
		splits = append(splits, longString[l:r])
	}
	splits = append(splits, longString[l:])
	return splits
}
```

## File: `pkg/cookie/cookie_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package cookie

import (
	"fmt"
	"net/http"
	"reflect"
	"testing"

	"github.com/vouch/vouch-proxy/pkg/cfg"
)

func init() {
	cfg.InitForTestPurposes()
	Configure()
}

func TestSplitCookie(t *testing.T) {
	type args struct {
		longString string
		maxLen     int
	}
	tests := []struct {
		name string
		args args
		want []string
	}{
		{"small split", args{"AAAbbbCCCdddEEEfffGGGhhhIIIjjj", 3}, []string{"AAA", "bbb", "CCC", "ddd", "EEE", "fff", "GGG", "hhh", "III", "jjj"}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := splitCookie(tt.args.longString, tt.args.maxLen); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("splitCookie() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestCookie(t *testing.T) {
	cfg.Cfg.Cookie.Name = "_alpha_beta"
	ckValue1 := "charlie"
	ckValue2 := "delta"
	expectedValue := fmt.Sprintf("%s%s", ckValue1, ckValue2)
	r := &http.Request{
		Header: map[string][]string{
			"Cookie": {
				fmt.Sprintf("%s_1of2=%s", cfg.Cfg.Cookie.Name, ckValue1),
				fmt.Sprintf("%s_2of2=%s", cfg.Cfg.Cookie.Name, ckValue2),
			},
		},
	}
	r.Cookies()
	s, err := Cookie(r)
	if err != nil {
		t.Error(err)
	}
	if expectedValue != s {
		t.Errorf("expected \"%s\" received \"%s\"", expectedValue, s)
	}
}
```

## File: `pkg/domains/domains.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package domains

import (
	"sort"
	"strings"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"go.uber.org/zap"
)

var log *zap.SugaredLogger

// Configure see main.go configure()
func Configure() {
	log = cfg.Logging.Logger
	sort.Sort(ByLengthDesc(cfg.Cfg.Domains))
}

// Matches returns one of the domains we're configured for
func Matches(s string) string {
	if strings.Contains(s, ":") {
		// then we have a port and we just want to check the host
		split := strings.Split(s, ":")
		log.Debugf("removing port from %s to test domain %s", s, split[0])
		s = split[0]
	}

	if len(cfg.Cfg.Domains) > 0 {
		for i, v := range cfg.Cfg.Domains {
			if s == v || strings.HasSuffix(s, "."+v) {
				log.Debugf("domain %s matched array value at [%d]=%v", s, i, v)
				return v
			}
		}
		log.Warnf("domain %s not found in any domains %v", s, cfg.Cfg.Domains)
	}
	return ""
}

// IsUnderManagement check if an email is under vouch-managed domain
func IsUnderManagement(email string) bool {
	split := strings.Split(email, "@")
	if len(split) != 2 {
		log.Warnf("not a valid email: %s", email)
		return false
	}

	match := Matches(split[1])
	return match != ""
}

// ByLengthDesc sort from
// https://play.golang.org/p/N6GbEgBffd
type ByLengthDesc []string

func (s ByLengthDesc) Len() int {
	return len(s)
}
func (s ByLengthDesc) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

// this differs by offing the longest first
func (s ByLengthDesc) Less(i, j int) bool {
	return len(s[j]) < len(s[i])
}
```

## File: `pkg/domains/domains_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package domains

import (
	"github.com/stretchr/testify/assert"
	"testing"

	"github.com/vouch/vouch-proxy/pkg/cfg"
)

func init() {
	cfg.InitForTestPurposes()
	cfg.Cfg.Domains = []string{"vouch.github.io", "sub.test.mydomain.com", "test.mydomain.com"}
	Configure()
}

func TestIsUnderManagement(t *testing.T) {
	assert.True(t, IsUnderManagement("test@vouch.github.io"))
	assert.True(t, IsUnderManagement("test@sub.vouch.github.io"))
	assert.True(t, IsUnderManagement("test@test.mydomain.com"))
	assert.True(t, IsUnderManagement("test@sub.test.mydomain.com"))

	assert.False(t, IsUnderManagement("test@example.com"))
	assert.False(t, IsUnderManagement("vouch.github.io@example.com"))
	assert.False(t, IsUnderManagement("test-vouch.github.io@example.com"))
	assert.False(t, IsUnderManagement("test@vouch.github.io.com"))
}

func TestMatches(t *testing.T) {
	// Full email should not be accepted
	assert.Equal(t, "", Matches("test@vouch.github.io"))

	assert.Equal(t, "vouch.github.io", Matches("vouch.github.io"))
	assert.Equal(t, "vouch.github.io", Matches("sub.vouch.github.io"))
	assert.Equal(t, "", Matches("a-different-vouch.github.io"))

	assert.Equal(t, "", Matches("mydomain.com"))

	assert.Equal(t, "test.mydomain.com", Matches("test.mydomain.com"))
	assert.Equal(t, "sub.test.mydomain.com", Matches("sub.test.mydomain.com"))
	assert.Equal(t, "sub.test.mydomain.com", Matches("subsub.sub.test.mydomain.com"))
	assert.Equal(t, "test.mydomain.com", Matches("other.test.mydomain.com"))
}
```

## File: `pkg/healthcheck/healthcheck.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package healthcheck

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"go.uber.org/zap"
)

var log *zap.SugaredLogger

func configure() {
	// cfg.ConfigureLogger()
	log = cfg.Logging.Logger
	if !cfg.Cfg.Testing {
		cfg.Logging.AtomicLogLevel.SetLevel(zap.ErrorLevel)
	}
}

// CheckAndExitIfIsHealthCheck healthcheck is a command line flag `-healthcheck`
func CheckAndExitIfIsHealthCheck() {

	if *cfg.CmdLine.IsHealthCheck {
		configure()
		healthcheck()
	}
}

func healthcheck() {
	url := fmt.Sprintf("http://%s:%d/healthcheck", cfg.Cfg.Listen, cfg.Cfg.Port)
	log.Debugf("Invoking healthcheck on %s", url)
	// #nosec - turn off gosec checking which flags `http.Get(url)`
	resp, err := http.Get(url)
	if err == nil {
		body, err := io.ReadAll(resp.Body)
		resp.Body.Close()
		if err == nil {
			var result map[string]interface{}
			jsonErr := json.Unmarshal(body, &result)
			if jsonErr == nil {
				if result["ok"] == true {
					log.Debugf("Healthcheck succeeded for %s", url)
					os.Exit(0)
				}
			}
		}
	}
	log.Errorf("Healthcheck failed for %s", url)
	os.Exit(1)
}
```

## File: `pkg/jwtmanager/jwtcache.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package jwtmanager

import (
	"net/http"
	"strings"
	"time"

	cache "github.com/patrickmn/go-cache"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/responses"
)

// Cache in memory temporary store for responses from /validate for jwt
var Cache *cache.Cache
var expire int = 20 // default 20 minutes
var dExp time.Duration

func cacheConfigure() {

	if cfg.Cfg.JWT.MaxAge < expire {
		expire = cfg.Cfg.JWT.MaxAge
	}
	dExp = time.Duration(expire) * time.Minute
	purgeCheck := dExp / 5
	// log.Debugf("cacheConfigure expire %d dExp %d purgecheck %d", expire, dExp, purgeCheck)
	Cache = cache.New(dExp, purgeCheck)
	log.Infof("jwtcache: the returned headers for a valid jwt will be cached for %d minutes", expire)
}

// CachedResponse caches the JWT response
// type CachedResponse struct {
// 	*CaptureWriter
// 	rawResponse []byte
// }

// JWTCacheHandler looks for a JWT and...
// returns a cached response
// or passes the request to /validate
// all tests for JWTCacheHandler are present in `handlers/validate_test.go` to avoid circular imports
func JWTCacheHandler(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {

		jwt := FindJWT(r)

		// check to see if we have headers cached for this jwt
		if jwt != "" {
			if resp, found := Cache.Get(jwt); found {
				// found it in cache!
				logger.Debug("/validate found response headers for jwt in cache")
				// TODO: instead of the copy for each, can we just append the whole blob?
				// or better still can we just cache the entire response including 200OK?
				for k, v := range resp.(http.Header) {
					w.Header().Add(k, strings.Join(v, ","))

				}

				responses.OK200(w, r)

				return
			}
		}

		next.ServeHTTP(w, r)

		if jwt != "" &&
			r.Context().Err() == nil {
			// see responses.addErrandCancelRequest()
			// r.Context().Done() is still open
			// cache the response headers for this jwt
			// log.Debug("setting cache for %+v", w.Header().Clone())

			claims, err := ClaimsFromJWT(jwt)
			if err != nil {
				log.Error("very unusual error, we found a jwt for /validate but we couldn't parse it for claims while setting it into cache, returning")
				return
				// log.Debugf("claims expire, time.now.unix, dExp %d - %d = %d > %d", claims.ExpiresAt, now, claims.ExpiresAt-now, int64(dExp))
				// log.Debugf("time.Duration((claims.ExpiresAt-time.Now().Unix())*time.Second.Nanoseconds()) %d", time.Duration((claims.ExpiresAt-time.Now().Unix())*time.Second.Nanoseconds()))
			}

			cacheExp := getCacheExpirationDuration(claims)
			Cache.Set(jwt, w.Header().Clone(), cacheExp)
		}
	})
}

// getCacheExpirationDuration - return time.Duration til the jwt should be purged from cache
// first see if the jwt's expiration will arrive before the cache expiration
// if this jwt expires in 10 minutes then we don't want to cache it for 20
// this might happen if the jwt expiration is set to 240 minutes, and the user last logged into the IdP 230 minutes ago
// then the user went away, cache was purged and now they return with 10 minutes left before token expiration
func getCacheExpirationDuration(claims *VouchClaims) time.Duration {

	now := time.Now().Unix()
	expiresAt := now + int64(dExp/time.Second)
	if !claims.VerifyExpiresAt(expiresAt, true) {
		jwtExpiresIn := time.Duration((claims.ExpiresAt - now) * int64(time.Second))
		log.Debugf("cache default expiration (%d) is after jwt expiration (%d). setting cache expiration to claim expiration for this entry", dExp, jwtExpiresIn)
		return jwtExpiresIn
	}
	return dExp
}
```

## File: `pkg/jwtmanager/jwtcache_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package jwtmanager

import (
	"fmt"
	"reflect"
	"testing"
	"time"
)

func Test_getCacheExpirationDuration(t *testing.T) {
	// default cache expire is 20 minutes, so we test +/- 5 minutes of that
	expire = 17
	now := time.Now()

	claimsA := lc
	claimsA.ExpiresAt = now.Add(time.Minute * time.Duration(expire+5)).Unix()

	claimsB := lc
	dBexp := time.Minute * time.Duration(expire-5)
	claimsB.ExpiresAt = now.Add(dBexp).Unix()

	tests := []struct {
		name   string
		claims *VouchClaims
		want   time.Duration
	}{
		{fmt.Sprintf("should equal %d", expire), &claimsA, dExp}, // dExp is the default expiration duration
		{fmt.Sprintf("should equal %d -5", expire), &claimsB, dBexp},
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getCacheExpirationDuration(tt.claims); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("getCacheExpirationDuration() = %v, want %v", got, tt.want)
			}
		})
	}
}
```

## File: `pkg/jwtmanager/jwtmanager.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package jwtmanager

import (
	"bytes"
	"compress/gzip"
	"encoding/base64"
	"errors"
	"fmt"
	"io"
	"net/http"
	"strings"
	"time"

	jwt "github.com/golang-jwt/jwt/v4"
	"go.uber.org/zap"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/cookie"
	"github.com/vouch/vouch-proxy/pkg/structs"
)

const comma = ","

// VouchClaims jwt Claims specific to vouch
type VouchClaims struct {
	Username     string `json:"username"`
	CustomClaims map[string]interface{}
	PAccessToken string
	PIdToken     string
	jwt.StandardClaims
}

// StandardClaims jwt.StandardClaims implementation
var StandardClaims jwt.StandardClaims

var logger *zap.Logger
var log *zap.SugaredLogger
var aud string

// Configure see main.go configure()
func Configure() {
	log = cfg.Logging.Logger
	logger = cfg.Logging.FastLogger
	cacheConfigure()
	aud = audience()
	StandardClaims = jwt.StandardClaims{
		Issuer:   cfg.Cfg.JWT.Issuer,
		Audience: aud,
	}
}

// `aud` of the issued JWT https://tools.ietf.org/html/rfc7519#section-4.1.3
func audience() string {
	aud := make([]string, 0)
	// TODO: the Sites that end up in the JWT come from here
	// if we add fine grain ability (ACL?) to the equation
	// then we're going to have to add something fancier here
	for i := 0; i < len(cfg.Cfg.Domains); i++ {
		aud = append(aud, cfg.Cfg.Domains[i])
	}
	if cfg.Cfg.Cookie.Domain != "" {
		aud = append(aud, cfg.Cfg.Cookie.Domain)
	}
	return strings.Join(aud, comma)
}

// NewVPJWT issue a signed Vouch Proxy JWT for a user
func NewVPJWT(u structs.User, customClaims structs.CustomClaims, ptokens structs.PTokens) (string, error) {
	// User`token`
	// u.PrepareUserData()
	claims := VouchClaims{
		u.Username,
		customClaims.Claims,
		ptokens.PAccessToken,
		ptokens.PIdToken,
		StandardClaims,
	}

	claims.Audience = aud
	claims.ExpiresAt = time.Now().Add(time.Minute * time.Duration(cfg.Cfg.JWT.MaxAge)).Unix()

	// https://github.com/vouch/vouch-proxy/issues/287
	if cfg.Cfg.Headers.AccessToken == "" {
		claims.PAccessToken = ""
	}

	if cfg.Cfg.Headers.IDToken == "" {
		claims.PIdToken = ""
	}

	// https://godoc.org/github.com/golang-jwt/jwt#NewWithClaims
	token := jwt.NewWithClaims(jwt.GetSigningMethod(cfg.Cfg.JWT.SigningMethod), claims)
	// log.Debugf("token: %v", token)
	log.Debugf("token created, expires: %d diff from now: %d", claims.StandardClaims.ExpiresAt, claims.StandardClaims.ExpiresAt-time.Now().Unix())

	key, err := cfg.SigningKey()
	if err != nil {
		log.Errorf("%s", err)
	}

	ss, err := token.SignedString(key)
	if ss == "" || err != nil {
		return "", fmt.Errorf("new JWT: signed token error: %s", err)
	}
	if cfg.Cfg.JWT.Compress {
		ss, err = compressAndEncodeTokenString(ss)
		if ss == "" || err != nil {
			return "", fmt.Errorf("new JWT: compressed token error: %w", err)
		}
	}
	return ss, nil
}

// SiteInToken searches does the token contain the site?
func SiteInToken(site string, token *jwt.Token) bool {
	if claims, ok := token.Claims.(*VouchClaims); ok {
		log.Debugf("site %s claim %v", site, claims)
		if claims.SiteInAudience(site) {
			return true
		}
	}
	log.Errorf("site %s not found in token audience", site)
	return false
}

// ParseTokenString converts signed token to jwt struct
func ParseTokenString(tokenString string) (*jwt.Token, error) {
	log.Debugf("tokenString length: %d", len(tokenString))
	if cfg.Cfg.JWT.Compress {
		tokenString = decodeAndDecompressTokenString(tokenString)
		log.Debugf("decompressed tokenString length %d", len(tokenString))
	}

	key, err := cfg.DecryptionKey()
	if err != nil {
		log.Errorf("%s", err)
	}

	return jwt.ParseWithClaims(tokenString, &VouchClaims{}, func(token *jwt.Token) (interface{}, error) {
		// return jwt.ParseWithClaims(tokenString, &VouchClaims{}, func(token *jwt.Token) (interface{}, error) {
		if token.Method != jwt.GetSigningMethod(cfg.Cfg.JWT.SigningMethod) {
			return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
		}

		return key, nil
	})

}

// SiteInAudience does the claim contain the value?
func (claims *VouchClaims) SiteInAudience(site string) bool {
	for _, s := range strings.Split(aud, comma) {
		if strings.Contains(site, s) {
			log.Debugf("site %s is found for claims.Audience %s", site, s)
			return true
		}
	}
	return false
}

// PTokenClaims get all the claims
func PTokenClaims(ptoken *jwt.Token) (*VouchClaims, error) {
	ptokenClaims, ok := ptoken.Claims.(*VouchClaims)
	if !ok {
		log.Debugf("failed claims: %v %v", ptokenClaims, ptoken.Claims)
		return ptokenClaims, errors.New("cannot parse claims")
	}
	log.Debugf("*ptokenCLaims: %v", *ptokenClaims)
	return ptokenClaims, nil
}

func decodeAndDecompressTokenString(encgzipss string) string {
	var gzipss []byte
	// gzipss, err := url.QueryUnescape(encgzipss)
	gzipss, err := base64.URLEncoding.DecodeString(encgzipss)
	if err != nil {
		log.Debugf("Error in Base64decode: %v", err)
	}

	breader := bytes.NewReader(gzipss)
	zr, err := gzip.NewReader(breader)
	if err != nil {
		log.Debugf("Error reading gzip data: %v", err)
		return ""
	}
	if err := zr.Close(); err != nil {
		log.Debugf("Error decoding token: %v", err)
	}
	ss, _ := io.ReadAll(zr)
	return string(ss)
}

func compressAndEncodeTokenString(ss string) (string, error) {
	var buf bytes.Buffer
	zw := gzip.NewWriter(&buf)
	if _, err := zw.Write([]byte(ss)); err != nil {
		return "", err
	}
	if err := zw.Close(); err != nil {
		return "", err
	}

	ret := base64.URLEncoding.EncodeToString(buf.Bytes())
	// ret := url.QueryEscape(buf.String())
	log.Debugf("token compressed: was %d bytes, now %d", len(ss), len(ret))
	return ret, nil
}

// FindJWT look for JWT in Cookie, JWT Header, Authorization Header (OAuth2 Bearer Token)
// and Query String in that order
func FindJWT(r *http.Request) string {
	jwt, err := cookie.Cookie(r)
	if err == nil {
		logger.Debug("jwt found in cookie")
		return jwt
	}
	jwt = r.Header.Get(cfg.Cfg.Headers.JWT)
	if jwt != "" {
		log.Debugf("jwt from header %s: %s", cfg.Cfg.Headers.JWT, jwt)
		return jwt
	}
	auth := r.Header.Get("Authorization")
	if auth != "" {
		s := strings.SplitN(auth, " ", 2)
		if len(s) == 2 {
			jwt = s[1]
			log.Debugf("jwt from authorization header: %s", jwt)
			return jwt
		}
	}
	jwt = r.URL.Query().Get(cfg.Cfg.Headers.QueryString)
	if jwt != "" {
		log.Debugf("jwt from querystring %s: %s", cfg.Cfg.Headers.QueryString, jwt)
		return jwt
	}
	return ""
}

// ClaimsFromJWT parse the jwt and return the claims
func ClaimsFromJWT(jwt string) (*VouchClaims, error) {
	var claims *VouchClaims

	jwtParsed, err := ParseTokenString(jwt)
	if err != nil {
		return nil, err
	}

	claims, err = PTokenClaims(jwtParsed)
	if err != nil {
		// claims = jwtmanager.PTokenClaims(jwtParsed)
		// if claims == &jwtmanager.VouchClaims{} {
		return nil, err
	}
	return claims, nil
}
```

## File: `pkg/jwtmanager/jwtmanager_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package jwtmanager

import (
	"encoding/json"
	"os"
	"path/filepath"
	"testing"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/structs"

	"github.com/stretchr/testify/assert"
)

var (
	u1 = structs.User{
		Username: "test@testing.com",
		Name:     "Test Name",
	}
	t1 = structs.PTokens{
		PAccessToken: "eyJhbGciOiJSUzI1NiIsImtpZCI6IjRvaXU4In0.eyJzdWIiOiJuZnlmZSIsImF1ZCI6ImltX29pY19jbGllbnQiLCJqdGkiOiJUOU4xUklkRkVzUE45enU3ZWw2eng2IiwiaXNzIjoiaHR0cHM6XC9cL3Nzby5tZXljbG91ZC5uZXQ6OTAzMSIsImlhdCI6MTM5MzczNzA3MSwiZXhwIjoxMzkzNzM3MzcxLCJub25jZSI6ImNiYTU2NjY2LTRiMTItNDU2YS04NDA3LTNkMzAyM2ZhMTAwMiIsImF0X2hhc2giOiJrdHFvZVBhc2praVY5b2Z0X3o5NnJBIn0.g1Jc9DohWFfFG3ppWfvW16ib6YBaONC5VMs8J61i5j5QLieY-mBEeVi1D3vr5IFWCfivY4hZcHtoJHgZk1qCumkAMDymsLGX-IGA7yFU8LOjUdR4IlCPlZxZ_vhqr_0gQ9pCFKDkiOv1LVv5x3YgAdhHhpZhxK6rWxojg2RddzvZ9Xi5u2V1UZ0jukwyG2d4PRzDn7WoRNDGwYOEt4qY7lv_NO2TY2eAklP-xYBWu0b9FBElapnstqbZgAXdndNs-Wqp4gyQG5D0owLzxPErR9MnpQfgNcai-PlWI_UrvoopKNbX0ai2zfkuQ-qh6Xn8zgkiaYDHzq4gzwRfwazaqA",
		PIdToken:     "eyJhbGciOiJSUzI1NiIsImtpZCI6IjRvaXU4In0.eyJzdWIiOiJuZnlmZSIsImF1ZCI6ImltX29pY19jbGllbnQiLCJqdGkiOiJUOU4xUklkRkVzUE45enU3ZWw2eng2IiwiaXNzIjoiaHR0cHM6XC9cL3Nzby5tZXljbG91ZC5uZXQ6OTAzMSIsImlhdCI6MTM5MzczNzA3MSwiZXhwIjoxMzkzNzM3MzcxLCJub25jZSI6ImNiYTU2NjY2LTRiMTItNDU2YS04NDA3LTNkMzAyM2ZhMTAwMiIsImF0X2hhc2giOiJrdHFvZVBhc2praVY5b2Z0X3o5NnJBIn0.g1Jc9DohWFfFG3ppWfvW16ib6YBaONC5VMs8J61i5j5QLieY-mBEeVi1D3vr5IFWCfivY4hZcHtoJHgZk1qCumkAMDymsLGX-IGA7yFU8LOjUdR4IlCPlZxZ_vhqr_0gQ9pCFKDkiOv1LVv5x3YgAdhHhpZhxK6rWxojg2RddzvZ9Xi5u2V1UZ0jukwyG2d4PRzDn7WoRNDGwYOEt4qY7lv_NO2TY2eAklP-xYBWu0b9FBElapnstqbZgAXdndNs-Wqp4gyQG5D0owLzxPErR9MnpQfgNcai-PlWI_UrvoopKNbX0ai2zfkuQ-qh6Xn8zgkiaYDHzq4gzwRfwazaqA",
	}

	lc VouchClaims

	claimjson = `{
		"sub": "f:a95afe53-60ba-4ac6-af15-fab870e72f3d:mrtester",
		"groups": ["Website Users", "Test Group"],
		"given_name": "Mister",
		"family_name": "Tester",
		"email": "mrtester@test.int"
	}`
	customClaims = structs.CustomClaims{}
)

func init() {
	cfg.InitForTestPurposes()
	Configure()

	lc = VouchClaims{
		u1.Username,
		customClaims.Claims,
		t1.PAccessToken,
		t1.PIdToken,
		StandardClaims,
	}

}

func TestClaimsHMAC(t *testing.T) {
	rootDir := os.Getenv(cfg.Branding.UCName + "_ROOT")
	for _, cfgFile := range []string{"test_config.yml", "test_config_rsa.yml"} {
		if err := os.Setenv(cfg.Branding.UCName+"_CONFIG", filepath.Join(rootDir, "config/testing", cfgFile)); err != nil {
			t.Errorf("failed setting environment variable %s_CONFIG", cfg.Branding.UCName)
		}

		json.Unmarshal([]byte(claimjson), &customClaims.Claims)

		log.Debugf("jwt config %s %d", string(cfg.Cfg.JWT.Secret), cfg.Cfg.JWT.MaxAge)
		assert.NotEmpty(t, cfg.Cfg.JWT.SigningMethod)
		assert.NotEmpty(t, cfg.Cfg.JWT.MaxAge)

		uts, err := NewVPJWT(u1, customClaims, t1)
		assert.NoError(t, err)

		utsParsed, err := ParseTokenString(uts)
		assert.NoError(t, err)

		log.Infof("utsParsed: %+v", utsParsed)
		// log.Infof("Sites: %+v", Sites)
		assert.True(t, SiteInToken(cfg.Cfg.Domains[0], utsParsed))
	}
	json.Unmarshal([]byte(claimjson), &customClaims.Claims)
}

func TestClaims(t *testing.T) {
	aud = audience()
	log.Debugf("jwt config %s %d", string(cfg.Cfg.JWT.Secret), cfg.Cfg.JWT.MaxAge)
	assert.NotEmpty(t, cfg.Cfg.JWT.Secret)
	assert.NotEmpty(t, cfg.Cfg.JWT.MaxAge)

	// now := time.Now()
	// d := time.Duration(ExpiresAtMinutes) * time.Minute
	// log.Infof("lc d %s", d.String())
	// lc.StandardClaims.ExpiresAt = now.Add(time.Duration(ExpiresAtMinutes) * time.Minute).Unix()
	// log.Infof("lc expiresAt %d", now.Unix()-lc.StandardClaims.ExpiresAt)
	uts, err := NewVPJWT(u1, customClaims, t1)
	assert.NoError(t, err)
	utsParsed, _ := ParseTokenString(uts)
	log.Infof("utsParsed: %+v", utsParsed)
	log.Infof("Audience: %+v", aud)
	assert.True(t, SiteInToken(cfg.Cfg.Domains[0], utsParsed))
}
```

## File: `pkg/providers/adfs/adfs.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package adfs

import (
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"regexp"
	"strconv"
	"strings"

	"go.uber.org/zap"
	"golang.org/x/oauth2"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/providers/common"
	"github.com/vouch/vouch-proxy/pkg/structs"
)

// Provider provider specific functions
type Provider struct{}

type adfsTokenRes struct {
	AccessToken string `json:"access_token"`
	TokenType   string `json:"token_type"`
	IDToken     string `json:"id_token"`
	ExpiresIn   int64  `json:"expires_in"` // relative seconds from now
}

var log *zap.SugaredLogger

// Configure see main.go configure()
func (Provider) Configure() {
	log = cfg.Logging.Logger
}

// GetUserInfo provider specific call to get userinfomation
// More info: https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/overview/ad-fs-scenarios-for-developers#supported-scenarios
func (Provider) GetUserInfo(r *http.Request, user *structs.User, customClaims *structs.CustomClaims, ptokens *structs.PTokens, opts ...oauth2.AuthCodeOption) (rerr error) {
	code := r.URL.Query().Get("code")
	log.Debugf("code: %s", code)

	formData := url.Values{}
	formData.Set("code", code)
	formData.Set("grant_type", "authorization_code")
	formData.Set("resource", cfg.GenOAuth.RelyingPartyId)
	formData.Set("client_id", cfg.GenOAuth.ClientID)
	formData.Set("redirect_uri", cfg.GenOAuth.RedirectURL)
	if cfg.GenOAuth.ClientSecret != "" {
		formData.Set("client_secret", cfg.GenOAuth.ClientSecret)
	}
	req, err := http.NewRequest("POST", cfg.GenOAuth.TokenURL, strings.NewReader(formData.Encode()))
	if err != nil {
		return err
	}
	req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
	req.Header.Add("Content-Length", strconv.Itoa(len(formData.Encode())))
	req.Header.Set("Accept", "application/json")

	client := &http.Client{}
	userinfo, err := client.Do(req)

	if err != nil {
		return err
	}
	defer func() {
		if err := userinfo.Body.Close(); err != nil {
			rerr = err
		}
	}()

	data, _ := io.ReadAll(userinfo.Body)
	tokenRes := adfsTokenRes{}

	if err := json.Unmarshal(data, &tokenRes); err != nil {
		return fmt.Errorf("getUserInfoFromADFS oauth2: cannot fetch token: %+v", err)
	}

	ptokens.PAccessToken = string(tokenRes.AccessToken)
	ptokens.PIdToken = string(tokenRes.IDToken)

	s := strings.Split(tokenRes.IDToken, ".")
	if len(s) < 2 {
		return fmt.Errorf("getUserInfoFromADFS jws: invalid token received")
	}

	idToken, err := base64.RawURLEncoding.DecodeString(s[1])
	if err != nil {
		return fmt.Errorf("getUserInfoFromADFS decode token: %+v", err)
	}
	log.Debugf("getUserInfoFromADFS idToken: %+v", string(idToken))

	adfsUser := structs.ADFSUser{}
	json.Unmarshal([]byte(idToken), &adfsUser)
	log.Infof("adfs adfsUser: %+v", adfsUser)
	// data contains an access token, refresh token, and id token
	// Please note that in order for custom claims to work you MUST set allatclaims in ADFS to be passed
	// https://oktotechnologies.ca/2018/08/26/adfs-openidconnect-configuration/
	if err = common.MapClaims([]byte(idToken), customClaims); err != nil {
		return err
	}
	adfsUser.PrepareUserData()
	var rxEmail = regexp.MustCompile("^[a-zA-Z0-9.!#$%&'*+\\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")

	if len(adfsUser.Email) == 0 {
		// If the email is blank, we will try to determine if the UPN is an email.
		if rxEmail.MatchString(adfsUser.UPN) {
			// Set the email from UPN if there is a valid email present.
			adfsUser.Email = adfsUser.UPN
		}
	}
	user.Username = adfsUser.Username
	user.Email = adfsUser.Email
	log.Debugf("User Obj: %+v", user)
	return nil
}
```

## File: `pkg/providers/alibaba/alibaba.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package alibaba

import (
	"encoding/json"
	"io"
	"net/http"

	"golang.org/x/oauth2"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/providers/common"
	"github.com/vouch/vouch-proxy/pkg/structs"
	"go.uber.org/zap"
)

// Provider provider specific functions
type Provider struct{}

var log *zap.SugaredLogger

// Configure see main.go configure()
func (Provider) Configure() {
	log = cfg.Logging.Logger
}

// GetUserInfo provider specific call to get userinfomation
func (Provider) GetUserInfo(r *http.Request, user *structs.User, customClaims *structs.CustomClaims, ptokens *structs.PTokens, opts ...oauth2.AuthCodeOption) (rerr error) {
	client, _, err := common.PrepareTokensAndClient(r, ptokens, true)
	if err != nil {
		return err
	}
	userinfo, err := client.Get(cfg.GenOAuth.UserInfoURL)
	if err != nil {
		return err
	}
	defer func() {
		if err := userinfo.Body.Close(); err != nil {
			rerr = err
		}
	}()
	data, _ := io.ReadAll(userinfo.Body)
	log.Infof("Alibaba userinfo body: %s", string(data))
	if err = common.MapClaims(data, customClaims); err != nil {
		log.Error(err)
		return err
	}
	aliUser := structs.AlibabaUser{}
	if err = json.Unmarshal(data, &aliUser); err != nil {
		log.Error(err)
		return err
	}
	aliUser.PrepareUserData()
	user.Username = aliUser.Username
	user.Email = aliUser.Email
	return nil
}
```

## File: `pkg/providers/azure/azure.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package azure

import (
	"encoding/base64"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"

	"golang.org/x/oauth2"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/providers/common"
	"github.com/vouch/vouch-proxy/pkg/structs"
	"go.uber.org/zap"
)

// Provider provider specific functions
type Provider struct{}

var log *zap.SugaredLogger

// Configure see main.go configure()
func (Provider) Configure() {
	log = cfg.Logging.Logger
}

// GetUserInfo provider specific call to get userinfomation
func (Provider) GetUserInfo(r *http.Request, user *structs.User, customClaims *structs.CustomClaims, ptokens *structs.PTokens, opts ...oauth2.AuthCodeOption) (rerr error) {
	_, _, err := common.PrepareTokensAndClient(r, ptokens, true, opts...)
	if err != nil {
		return err
	}

	// For Azure AD, there is very little information in the /userinfo response.
	// Since we can get everything we currently need from the access token, we are
	// just going to extract user info and custom claims from there.
	azureUser := structs.AzureUser{}

	var tokenParts []string

	if cfg.GenOAuth.AzureToken == "access_token" {
		tokenParts = strings.Split(ptokens.PAccessToken, ".")
	} else if cfg.GenOAuth.AzureToken == "id_token" {
		tokenParts = strings.Split(ptokens.PIdToken, ".")
	} else {
		err = fmt.Errorf("azure Token not access_token or id_token")
		log.Error(err)
		return err
	}

	if len(tokenParts) < 2 {
		err = fmt.Errorf("azure GetUserInfo: invalid token received; not enough parts")
		log.Error(err)
		return err
	}

	tokenBytes, err := base64.RawURLEncoding.DecodeString(tokenParts[1])
	if err != nil {
		err = fmt.Errorf("azure GetUserInfo: decoding token failed: %+v", err)
		log.Error(err)
		return err
	}

	if err = common.MapClaims(tokenBytes, customClaims); err != nil {
		log.Error(err)
		return err
	}

	log.Debugf("azure GetUserInfo: getting user info from token: %+v", string(tokenBytes))
	if err = json.Unmarshal(tokenBytes, &azureUser); err != nil {
		err = fmt.Errorf("azure getUserInfoFromTokens: unpacking token into AzureUser failed: %+v", err)
		log.Error(err)
		return err
	}

	azureUser.PrepareUserData()

	user.Username = azureUser.Username
	user.Name = azureUser.Name
	user.Email = azureUser.Email
	log.Infof("azure GetUserInfo: User: %+v", user)

	return nil
}
```

## File: `pkg/providers/common/common.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package common

import (
	"context"
	"encoding/json"
	"net/http"

	"go.uber.org/zap"
	"golang.org/x/oauth2"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/structs"
)

var log *zap.SugaredLogger

// Configure see main.go configure()
func Configure() {
	log = cfg.Logging.Logger
}

// PrepareTokensAndClient setup the client, usually for a UserInfo request
func PrepareTokensAndClient(r *http.Request, ptokens *structs.PTokens, setProviderToken bool, opts ...oauth2.AuthCodeOption) (*http.Client, *oauth2.Token, error) {
	providerToken, err := cfg.OAuthClient.Exchange(context.TODO(), r.URL.Query().Get("code"), opts...)
	if err != nil {
		return nil, nil, err
	}
	ptokens.PAccessToken = providerToken.AccessToken

	if setProviderToken {
		if providerToken.Extra("id_token") != nil {
			// Certain providers (eg. gitea) don't provide an id_token
			// and it's not necessary for the authentication phase
			ptokens.PIdToken = providerToken.Extra("id_token").(string)
		} else {
			log.Debugf("id_token missing - may not be supported by this provider")
		}
	}

	log.Debugf("ptokens: accessToken length: %d, IdToken length: %d", len(ptokens.PAccessToken), len(ptokens.PIdToken))
	client := cfg.OAuthClient.Client(context.TODO(), providerToken)
	return client, providerToken, err
}

// MapClaims populate CustomClaims from userInfo for each configure claims header
func MapClaims(claims []byte, customClaims *structs.CustomClaims) error {
	var f interface{}
	err := json.Unmarshal(claims, &f)
	if err != nil {
		log.Error("Error unmarshaling claims")
		return err
	}
	m := f.(map[string]interface{})
	for k := range m {
		var found = false
		for claim := range cfg.Cfg.Headers.ClaimsCleaned {
			if k == claim {
				found = true
			}
		}
		if !found {
			delete(m, k)
		}
	}
	customClaims.Claims = m
	return nil
}
```

## File: `pkg/providers/discord/discord.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package discord

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"

	"golang.org/x/oauth2"

	"go.uber.org/zap"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/providers/common"
	"github.com/vouch/vouch-proxy/pkg/structs"
)

// Provider provider specific functions
type Provider struct{}

var log *zap.SugaredLogger

// Configure see main.go configure()
func (Provider) Configure() {
	log = cfg.Logging.Logger
}

// GetUserInfo provider specific call to get userinfomation
func (Provider) GetUserInfo(r *http.Request, user *structs.User, customClaims *structs.CustomClaims, ptokens *structs.PTokens, opts ...oauth2.AuthCodeOption) (rerr error) {
	client, _, err := common.PrepareTokensAndClient(r, ptokens, true, opts...)
	if err != nil {
		return err
	}
	userinfo, err := client.Get(cfg.GenOAuth.UserInfoURL)
	if err != nil {
		return err
	}
	defer func() {
		if err := userinfo.Body.Close(); err != nil {
			rerr = err
		}
	}()
	data, err := io.ReadAll(userinfo.Body)
	if err != nil {
		return err
	}
	log.Infof("Discord userinfo body: %s", string(data))
	if err = common.MapClaims(data, customClaims); err != nil {
		log.Error(err)
		return err
	}
	dUser := structs.DiscordUser{}
	if err = json.Unmarshal(data, &dUser); err != nil {
		log.Error(err)
		return err
	}

	// If the provider is configured to use IDs, the ID is copied to PreparedUsername.
	if cfg.GenOAuth.DiscordUseIDs {
		user.Username = dUser.Id
	} else {
		user.Username = dUser.Username

		// If the Discriminator is present that is appended to the Username in the format "Username#Discriminator"
		// to match the old format of Discord usernames
		// Previous format which is being phased out: https://support.discord.com/hc/en-us/articles/4407571667351-Law-Enforcement-Guidelines Subheading "How to find usernames and discriminators"
		// Details about the new username requirements: https://support.discord.com/hc/en-us/articles/12620128861463
		if dUser.Discriminator != "0" {
			user.Username = fmt.Sprintf("%s#%s", dUser.Username, dUser.Discriminator)
		}
	}
	user.Email = dUser.Email

	return nil
}
```

## File: `pkg/providers/github/github.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package github

import (
	"encoding/json"
	"errors"
	"io"
	"net/http"
	"strings"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/providers/common"
	"github.com/vouch/vouch-proxy/pkg/structs"
	"go.uber.org/zap"
	"golang.org/x/oauth2"
)

// Provider provider specific functions
type Provider struct {
	PrepareTokensAndClient func(r *http.Request, ptokens *structs.PTokens, setProviderToken bool, opts ...oauth2.AuthCodeOption) (*http.Client, *oauth2.Token, error)
}

var log *zap.SugaredLogger

// Configure see main.go configure()
func (Provider) Configure() {
	log = cfg.Logging.Logger
}

// GetUserInfo github user info, calls github api for org and teams
func (me Provider) GetUserInfo(r *http.Request, user *structs.User, customClaims *structs.CustomClaims, ptokens *structs.PTokens, opts ...oauth2.AuthCodeOption) (rerr error) {
	client, _, err := me.PrepareTokensAndClient(r, ptokens, true, opts...)
	if err != nil {
		return err
	}
	userinfo, err := client.Get(cfg.GenOAuth.UserInfoURL)
	if err != nil {
		return err
	}
	defer func() {
		if err := userinfo.Body.Close(); err != nil {
			rerr = err
		}
	}()
	data, _ := io.ReadAll(userinfo.Body)
	log.Infof("github userinfo body: %s", string(data))
	if err = common.MapClaims(data, customClaims); err != nil {
		log.Error(err)
		return err
	}
	ghUser := structs.GitHubUser{}
	if err = json.Unmarshal(data, &ghUser); err != nil {
		log.Error(err)
		return err
	}
	log.Debug("getUserInfoFromGitHub ghUser")
	log.Debug(ghUser)
	log.Debug("getUserInfoFromGitHub user")
	log.Debug(user)

	ghUser.PrepareUserData()
	user.Email = ghUser.Email
	user.Name = ghUser.Name
	user.Username = ghUser.Username
	user.ID = ghUser.ID

	// user = &ghUser.User

	toOrgAndTeam := func(orgAndTeam string) (string, string) {
		split := strings.Split(orgAndTeam, "/")
		if len(split) == 1 {
			// only organization given
			return orgAndTeam, ""
		} else if len(split) == 2 {
			return split[0], split[1]
		} else {
			return "", ""
		}
	}

	if len(cfg.Cfg.TeamWhiteList) != 0 {
		for _, orgAndTeam := range cfg.Cfg.TeamWhiteList {
			org, team := toOrgAndTeam(orgAndTeam)
			if org != "" {
				log.Info(org)
				var err error
				isMember := false
				if team != "" {
					isMember, err = getTeamMembershipStateFromGitHub(client, user, org, team)
				} else {
					isMember, err = getOrgMembershipStateFromGitHub(client, user, org)
				}
				if err != nil {
					return err
				}
				if isMember {
					user.TeamMemberships = append(user.TeamMemberships, orgAndTeam)
				}

			} else {
				log.Warnf("Invalid org/team format in %s: must be written as <orgId>/<teamSlug>", orgAndTeam)
			}
		}
	}

	log.Debug("getUserInfoFromGitHub")
	log.Debug(user)
	return nil
}

func getOrgMembershipStateFromGitHub(client *http.Client, user *structs.User, orgID string) (isMember bool, rerr error) {
	replacements := strings.NewReplacer(":org_id", orgID, ":username", user.Username)
	orgMembershipResp, err := client.Get(replacements.Replace(cfg.GenOAuth.UserOrgURL))
	if err != nil {
		log.Error(err)
		return false, err
	}

	if orgMembershipResp.StatusCode == 302 {
		log.Debug("Need to check public membership")
		location := orgMembershipResp.Header.Get("Location")
		if location != "" {
			orgMembershipResp, err = client.Get(location)
			if err != nil {
				log.Error(err)
			}
		}
	}

	if orgMembershipResp.StatusCode == 204 {
		log.Debug("getOrgMembershipStateFromGitHub isMember: true")
		return true, nil
	} else if orgMembershipResp.StatusCode == 404 {
		log.Debug("getOrgMembershipStateFromGitHub isMember: false")
		return false, nil
	} else {
		log.Errorf("getOrgMembershipStateFromGitHub: unexpected status code %d", orgMembershipResp.StatusCode)
		return false, errors.New("Unexpected response status " + orgMembershipResp.Status)
	}
}

func getTeamMembershipStateFromGitHub(client *http.Client, user *structs.User, orgID string, team string) (isMember bool, rerr error) {
	replacements := strings.NewReplacer(":org_id", orgID, ":team_slug", team, ":username", user.Username)
	membershipStateResp, err := client.Get(replacements.Replace(cfg.GenOAuth.UserTeamURL))
	if err != nil {
		log.Error(err)
		return false, err
	}
	defer func() {
		if err := membershipStateResp.Body.Close(); err != nil {
			rerr = err
		}
	}()
	if membershipStateResp.StatusCode == 200 {
		data, _ := io.ReadAll(membershipStateResp.Body)
		log.Infof("github team membership body: ", string(data))
		ghTeamState := structs.GitHubTeamMembershipState{}
		if err = json.Unmarshal(data, &ghTeamState); err != nil {
			log.Error(err)
			return false, err
		}
		log.Debugf("getTeamMembershipStateFromGitHub ghTeamState %s", ghTeamState)
		return ghTeamState.State == "active", nil
	} else if membershipStateResp.StatusCode == 404 {
		log.Debug("getTeamMembershipStateFromGitHub isMember: false")
		return false, err
	} else {
		log.Errorf("getTeamMembershipStateFromGitHub: unexpected status code %d", membershipStateResp.StatusCode)
		return false, errors.New("Unexpected response status " + membershipStateResp.Status)
	}
}
```

## File: `pkg/providers/github/github_test.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package github

import (
	"encoding/json"
	"net/http"
	"regexp"
	"testing"

	mockhttp "github.com/karupanerura/go-mock-http-response"
	"github.com/stretchr/testify/assert"
	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/domains"
	"github.com/vouch/vouch-proxy/pkg/structs"
	"golang.org/x/oauth2"
)

type ReqMatcher func(*http.Request) bool

type FunResponsePair struct {
	matcher  ReqMatcher
	response *mockhttp.ResponseMock
}

type Transport struct {
	MockError error
}

func (c *Transport) RoundTrip(req *http.Request) (*http.Response, error) {
	if c.MockError != nil {
		return nil, c.MockError
	}
	for _, p := range mockedResponses {
		if p.matcher(req) {
			requests = append(requests, req.URL.String())
			return p.response.MakeResponse(req), nil
		}
	}
	return nil, nil
}

func mockResponse(fun ReqMatcher, statusCode int, headers map[string]string, body []byte) {
	mockedResponses = append(mockedResponses, FunResponsePair{matcher: fun, response: mockhttp.NewResponseMock(statusCode, headers, body)})
}

func regexMatcher(expr string) ReqMatcher {
	return func(r *http.Request) bool {
		matches, _ := regexp.Match(expr, []byte(r.URL.String()))
		return matches
	}
}

func urlEquals(value string) ReqMatcher {
	return func(r *http.Request) bool {
		return r.URL.String() == value
	}
}

func assertURLCalled(t *testing.T, url string) {
	found := false
	for _, requestedURL := range requests {
		if requestedURL == url {
			found = true
			break
		}
	}
	assert.True(t, found, "Expected %s to have been called, but got only %s", url, requests)
}

var (
	user            *structs.User
	token           = &oauth2.Token{AccessToken: "123"}
	mockedResponses = []FunResponsePair{}
	requests        []string
	client          = &http.Client{Transport: &Transport{}}
)

func setUp() {
	log = cfg.Logging.Logger
	cfg.InitForTestPurposesWithProvider("github")

	cfg.Cfg.AllowAllUsers = false
	cfg.Cfg.WhiteList = make([]string, 0)
	cfg.Cfg.TeamWhiteList = make([]string, 0)
	cfg.Cfg.Domains = []string{"domain1"}

	domains.Configure()

	mockedResponses = []FunResponsePair{}
	requests = make([]string, 0)

	user = &structs.User{Username: "testuser", Email: "test@example.com"}
}

func TestGetTeamMembershipStateFromGitHubActive(t *testing.T) {
	setUp()
	mockResponse(regexMatcher(".*"), http.StatusOK, map[string]string{}, []byte("{\"state\": \"active\"}"))

	isMember, err := getTeamMembershipStateFromGitHub(client, user, "org1", "team1")

	assert.Nil(t, err)
	assert.True(t, isMember)
}

func TestGetTeamMembershipStateFromGitHubInactive(t *testing.T) {
	setUp()
	mockResponse(regexMatcher(".*"), http.StatusOK, map[string]string{}, []byte("{\"state\": \"inactive\"}"))

	isMember, err := getTeamMembershipStateFromGitHub(client, user, "org1", "team1")

	assert.Nil(t, err)
	assert.False(t, isMember)
}

func TestGetTeamMembershipStateFromGitHubNotAMember(t *testing.T) {
	setUp()
	mockResponse(regexMatcher(".*"), http.StatusNotFound, map[string]string{}, []byte(""))

	isMember, err := getTeamMembershipStateFromGitHub(client, user, "org1", "team1")

	assert.Nil(t, err)
	assert.False(t, isMember)
}

func TestGetOrgMembershipStateFromGitHubNotFound(t *testing.T) {
	setUp()
	mockResponse(regexMatcher(".*"), http.StatusNotFound, map[string]string{}, []byte(""))

	isMember, err := getOrgMembershipStateFromGitHub(client, user, "myorg")

	assert.Nil(t, err)
	assert.False(t, isMember)

	expectedOrgMembershipURL := "https://api.github.com/orgs/myorg/members/" + user.Username
	assertURLCalled(t, expectedOrgMembershipURL)
}

func TestGetOrgMembershipStateFromGitHubNoOrgAccess(t *testing.T) {
	setUp()
	location := "https://api.github.com/orgs/myorg/public_members/" + user.Username

	mockResponse(regexMatcher(".*orgs/myorg/members.*"), http.StatusFound, map[string]string{"Location": location}, []byte(""))
	mockResponse(regexMatcher(".*orgs/myorg/public_members.*"), http.StatusNoContent, map[string]string{}, []byte(""))

	isMember, err := getOrgMembershipStateFromGitHub(client, user, "myorg")

	assert.Nil(t, err)
	assert.True(t, isMember)

	expectedOrgMembershipURL := "https://api.github.com/orgs/myorg/members/" + user.Username
	assertURLCalled(t, expectedOrgMembershipURL)

	expectedOrgPublicMembershipURL := "https://api.github.com/orgs/myorg/public_members/" + user.Username
	assertURLCalled(t, expectedOrgPublicMembershipURL)
}

func TestGetUserInfo(t *testing.T) {
	setUp()

	userInfoContent, _ := json.Marshal(structs.GitHubUser{
		User: structs.User{
			Username:   "test",
			CreatedOn:  123,
			Email:      "email@example.com",
			ID:         1,
			LastUpdate: 123,
			Name:       "name",
		},
		Login:   "myusername",
		Picture: "avatar-url",
	})
	mockResponse(urlEquals(cfg.GenOAuth.UserInfoURL), http.StatusOK, map[string]string{}, userInfoContent)

	cfg.Cfg.TeamWhiteList = append(cfg.Cfg.TeamWhiteList, "myOtherOrg", "myorg/myteam")

	mockResponse(regexMatcher(".*teams.*"), http.StatusOK, map[string]string{}, []byte("{\"state\": \"active\"}"))
	mockResponse(regexMatcher(".*members.*"), http.StatusNoContent, map[string]string{}, []byte(""))

	provider := Provider{PrepareTokensAndClient: func(_ *http.Request, _ *structs.PTokens, _ bool, opts ...oauth2.AuthCodeOption) (*http.Client, *oauth2.Token, error) {
		return client, token, nil
	}}
	err := provider.GetUserInfo(nil, user, &structs.CustomClaims{}, &structs.PTokens{})

	assert.Nil(t, err)
	assert.Equal(t, "myusername", user.Username)
	assert.Equal(t, []string{"myOtherOrg", "myorg/myteam"}, user.TeamMemberships)

	expectedTeamMembershipURL := "https://api.github.com/orgs/myorg/teams/myteam/memberships/myusername"
	assertURLCalled(t, expectedTeamMembershipURL)
}
```

## File: `pkg/providers/google/google.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package google

import (
	"encoding/json"
	"io"
	"net/http"

	"golang.org/x/oauth2"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/providers/common"
	"github.com/vouch/vouch-proxy/pkg/structs"
	"go.uber.org/zap"
)

// Provider provider specific functions
type Provider struct{}

var log *zap.SugaredLogger

// Configure see main.go configure()
func (Provider) Configure() {
	log = cfg.Logging.Logger
}

// GetUserInfo provider specific call to get userinfomation
func (Provider) GetUserInfo(r *http.Request, user *structs.User, customClaims *structs.CustomClaims, ptokens *structs.PTokens, opts ...oauth2.AuthCodeOption) (rerr error) {
	client, _, err := common.PrepareTokensAndClient(r, ptokens, true, opts...)
	if err != nil {
		return err
	}
	userinfo, err := client.Get(cfg.GenOAuth.UserInfoURL)
	if err != nil {
		return err
	}
	defer func() {
		if err := userinfo.Body.Close(); err != nil {
			rerr = err
		}
	}()
	data, _ := io.ReadAll(userinfo.Body)
	log.Infof("google userinfo body: ", string(data))
	if err = common.MapClaims(data, customClaims); err != nil {
		log.Error(err)
		return err
	}
	if err = json.Unmarshal(data, user); err != nil {
		log.Error(err)
		return err
	}
	user.PrepareUserData()

	return nil
}
```

## File: `pkg/providers/homeassistant/homeassistant.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package homeassistant

import (
	"net/http"

	"golang.org/x/oauth2"

	"github.com/vouch/vouch-proxy/pkg/providers/common"
	"github.com/vouch/vouch-proxy/pkg/structs"
)

// Provider provider specific functions
type Provider struct{}

// var log *zap.SugaredLogger

// Configure see main.go configure()
func (Provider) Configure() {
	// log = cfg.Logging.Logger
}

// GetUserInfo provider specific call to get userinfomation
// More info: https://developers.home-assistant.io/docs/en/auth_api.html
func (Provider) GetUserInfo(r *http.Request, user *structs.User, customClaims *structs.CustomClaims, ptokens *structs.PTokens, opts ...oauth2.AuthCodeOption) (rerr error) {
	_, providerToken, err := common.PrepareTokensAndClient(r, ptokens, false, opts...)
	if err != nil {
		return err
	}
	ptokens.PAccessToken = providerToken.Extra("access_token").(string)
	// Home assistant does not provide an API to query username, so we statically set it to "homeassistant"
	user.Username = "homeassistant"
	return nil
}
```

## File: `pkg/providers/indieauth/indieauth.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package indieauth

import (
	"bytes"
	"encoding/json"
	"io"
	"mime/multipart"
	"net/http"

	"golang.org/x/oauth2"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/providers/common"
	"github.com/vouch/vouch-proxy/pkg/structs"
	"go.uber.org/zap"
)

// Provider provider specific functions
type Provider struct{}

var log *zap.SugaredLogger

// Configure see main.go configure()
func (Provider) Configure() {
	log = cfg.Logging.Logger
}

// GetUserInfo provider specific call to get userinfomation
func (Provider) GetUserInfo(r *http.Request, user *structs.User, customClaims *structs.CustomClaims, ptokens *structs.PTokens, opts ...oauth2.AuthCodeOption) (rerr error) {
	// indieauth sends the "me" setting in json back to the callback, so just pluck it from the callback
	code := r.URL.Query().Get("code")
	log.Errorf("ptoken.AccessToken: %s", code)
	var b bytes.Buffer
	w := multipart.NewWriter(&b)
	// v.Set("code", code)
	fw, err := w.CreateFormField("code")
	if err != nil {
		return err
	}
	if _, err = fw.Write([]byte(code)); err != nil {
		return err
	}
	// v.Set("redirect_uri", cfg.GenOAuth.RedirectURL)
	if fw, err = w.CreateFormField("redirect_uri"); err != nil {
		return err
	}
	if _, err = fw.Write([]byte(cfg.GenOAuth.RedirectURL)); err != nil {
		return err
	}
	// v.Set("client_id", cfg.GenOAuth.ClientID)
	if fw, err = w.CreateFormField("client_id"); err != nil {
		return err
	}
	if _, err = fw.Write([]byte(cfg.GenOAuth.ClientID)); err != nil {
		return err
	}
	if err = w.Close(); err != nil {
		log.Error("error closing writer.")
	}

	req, err := http.NewRequest("POST", cfg.GenOAuth.AuthURL, &b)
	if err != nil {
		return err
	}
	req.Header.Set("Content-Type", w.FormDataContentType())
	req.Header.Set("Accept", "application/json")

	// v := url.Values{}
	// userinfo, err := client.PostForm(cfg.GenOAuth.UserInfoURL, v)

	client := &http.Client{}
	userinfo, err := client.Do(req)

	if err != nil {
		// http.Error(w, err.Error(), http.StatusBadRequest)
		return err
	}
	defer func() {
		if err := userinfo.Body.Close(); err != nil {
			rerr = err
		}
	}()

	data, _ := io.ReadAll(userinfo.Body)
	log.Infof("indieauth userinfo body: %s", string(data))
	if err = common.MapClaims(data, customClaims); err != nil {
		log.Error(err)
		return err
	}
	iaUser := structs.IndieAuthUser{}
	if err = json.Unmarshal(data, &iaUser); err != nil {
		log.Error(err)
		return err
	}
	iaUser.PrepareUserData()
	user.Username = iaUser.Username
	log.Debug(user)
	return nil
}
```

## File: `pkg/providers/nextcloud/nextcloud.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package nextcloud

import (
	"encoding/json"
	"io"
	"net/http"

	"golang.org/x/oauth2"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/providers/common"
	"github.com/vouch/vouch-proxy/pkg/structs"
	"go.uber.org/zap"
)

// Provider provider specific functions
type Provider struct{}

var log *zap.SugaredLogger

// Configure see main.go configure()
func (Provider) Configure() {
	log = cfg.Logging.Logger
}

// GetUserInfo provider specific call to get userinfomation
func (Provider) GetUserInfo(r *http.Request, user *structs.User, customClaims *structs.CustomClaims, ptokens *structs.PTokens, opts ...oauth2.AuthCodeOption) (rerr error) {
	client, _, err := common.PrepareTokensAndClient(r, ptokens, true)
	if err != nil {
		return err
	}
	userinfo, err := client.Get(cfg.GenOAuth.UserInfoURL)
	if err != nil {
		return err
	}
	defer func() {
		if err := userinfo.Body.Close(); err != nil {
			rerr = err
		}
	}()
	data, _ := io.ReadAll(userinfo.Body)
	log.Infof("Ocs userinfo body: %s", string(data))
	if err = common.MapClaims(data, customClaims); err != nil {
		log.Error(err)
		return err
	}
	ncUser := structs.NextcloudUser{}
	if err = json.Unmarshal(data, &ncUser); err != nil {
		log.Error(err)
		return err
	}
	ncUser.PrepareUserData()
	user.Username = ncUser.Username
	user.Email = ncUser.Email
	return nil
}
```

## File: `pkg/providers/openid/openid.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package openid

import (
	"encoding/json"
	"io"
	"net/http"

	"golang.org/x/oauth2"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/providers/common"
	"github.com/vouch/vouch-proxy/pkg/structs"
	"go.uber.org/zap"
)

// Provider provider specific functions
type Provider struct{}

var log *zap.SugaredLogger

// Configure see main.go configure()
func (Provider) Configure() {
	log = cfg.Logging.Logger
}

// GetUserInfo provider specific call to get userinfomation
func (Provider) GetUserInfo(r *http.Request, user *structs.User, customClaims *structs.CustomClaims, ptokens *structs.PTokens, opts ...oauth2.AuthCodeOption) (rerr error) {
	client, _, err := common.PrepareTokensAndClient(r, ptokens, true, opts...)
	if err != nil {
		return err
	}
	userinfo, err := client.Get(cfg.GenOAuth.UserInfoURL)
	if err != nil {
		return err
	}
	defer func() {
		if err := userinfo.Body.Close(); err != nil {
			rerr = err
		}
	}()
	data, _ := io.ReadAll(userinfo.Body)
	log.Infof("OpenID userinfo body: %s", string(data))
	if err = common.MapClaims(data, customClaims); err != nil {
		log.Error(err)
		return err
	}
	if err = json.Unmarshal(data, user); err != nil {
		log.Error(err)
		return err
	}
	user.PrepareUserData()
	return nil
}
```

## File: `pkg/providers/openstax/openstax.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package openstax

import (
	"encoding/json"
	"io"
	"net/http"

	"golang.org/x/oauth2"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/providers/common"
	"github.com/vouch/vouch-proxy/pkg/structs"
	"go.uber.org/zap"
)

// Provider provider specific functions
type Provider struct{}

var log *zap.SugaredLogger

// Configure see main.go configure()
func (Provider) Configure() {
	log = cfg.Logging.Logger
}

// GetUserInfo provider specific call to get userinfomation
func (Provider) GetUserInfo(r *http.Request, user *structs.User, customClaims *structs.CustomClaims, ptokens *structs.PTokens, opts ...oauth2.AuthCodeOption) (rerr error) {
	client, _, err := common.PrepareTokensAndClient(r, ptokens, false, opts...)
	if err != nil {
		return err
	}
	userinfo, err := client.Get(cfg.GenOAuth.UserInfoURL)
	if err != nil {
		return err
	}
	defer func() {
		if err := userinfo.Body.Close(); err != nil {
			rerr = err
		}
	}()
	data, _ := io.ReadAll(userinfo.Body)
	log.Infof("OpenStax userinfo body: %s", string(data))
	if err = common.MapClaims(data, customClaims); err != nil {
		log.Error(err)
		return err
	}
	oxUser := structs.OpenStaxUser{}
	if err = json.Unmarshal(data, &oxUser); err != nil {
		log.Error(err)
		return err
	}

	oxUser.PrepareUserData()
	user.Email = oxUser.Email
	user.Name = oxUser.Name
	user.Username = oxUser.Username
	user.ID = oxUser.ID
	user.PrepareUserData()
	return nil
}
```

## File: `pkg/responses/responses.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package responses

import (
	"html/template"
	"net/http"

	"github.com/vouch/vouch-proxy/pkg/cfg"
	"github.com/vouch/vouch-proxy/pkg/cookie"
	"go.uber.org/zap"
	"golang.org/x/net/context"
)

// Index variables passed to index.tmpl
type Index struct {
	Msg          string
	TestURLs     []string
	Testing      bool
	DocumentRoot string
}

var (
	indexTemplate *template.Template
	log           *zap.SugaredLogger
	// fastlog       *zap.Logger

	// errorTemplate *template.Template
	// errNotAuthorized = errors.New("not authorized")
)

// Configure see main.go configure()
func Configure() {
	log = cfg.Logging.Logger
	// fastlog = cfg.Logging.FastLogger

	log.Debugf("responses.Configure() attempting to parse embedded templates")
	indexTemplate = template.Must(template.ParseFS(cfg.Templates, "templates/index.tmpl"))
}

// RenderIndex render the response as an HTML page, mostly used in testing
func RenderIndex(w http.ResponseWriter, msg string) {
	if err := indexTemplate.Execute(w, &Index{Msg: msg, TestURLs: cfg.Cfg.TestURLs, Testing: cfg.Cfg.Testing, DocumentRoot: cfg.Cfg.DocumentRoot}); err != nil {
		log.Error(err)
	}
}

// renderError html error page
// something terse for the end user
func renderError(w http.ResponseWriter, msg string, status int) {
	log.Debugf("rendering error for user: %s", msg)
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	w.Header().Set("X-Content-Type-Options", "nosniff")
	w.WriteHeader(status)
	if err := indexTemplate.Execute(w, &Index{Msg: msg, DocumentRoot: cfg.Cfg.DocumentRoot}); err != nil {
		log.Error(err)
	}
}

// OK200 returns "200 OK"
func OK200(w http.ResponseWriter, r *http.Request) {
	_, err := w.Write([]byte("200 OK\n"))
	if err != nil {
		log.Error(err)
	}
}

// Redirect302 redirect to the specified rURL
func Redirect302(w http.ResponseWriter, r *http.Request, rURL string) {
	if cfg.Cfg.Testing {
		cfg.Cfg.TestURLs = append(cfg.Cfg.TestURLs, rURL)
		RenderIndex(w, "302 redirect to: "+rURL)
		return
	}
	http.Redirect(w, r, rURL, http.StatusFound)
}

// Error400 Bad Request
func Error400(w http.ResponseWriter, r *http.Request, e error) {
	cancelClearSetError(w, r, e)
	renderError(w, "400 Bad Request", http.StatusBadRequest)
}

// Error401 Unauthorized, the standard error returned when failing /validate
// this is captured by nginx, which converts the 401 into 302 to the login page
func Error401(w http.ResponseWriter, r *http.Request, e error) {
	cancelClearSetError(w, r, e)
	http.Error(w, e.Error(), http.StatusUnauthorized)
	// renderError(w, "401 Unauthorized")
}

// Error401HTTP
func Error401HTTP(w http.ResponseWriter, r *http.Request, e error) {
	cancelClearSetError(w, r, e)
	renderError(w, e.Error(), http.StatusUnauthorized)
}

// Error403 Forbidden
// if there's an error during /auth or if they don't pass validation in /auth
func Error403(w http.ResponseWriter, r *http.Request, e error) {
	cancelClearSetError(w, r, e)
	renderError(w, "403 Forbidden", http.StatusForbidden)
}

// Error500 Internal Error
// something is not right, hopefully this never happens
func Error500(w http.ResponseWriter, r *http.Request, e error) {
	cancelClearSetError(w, r, e)
	log.Infof("If this error persists it may be worthy of a bug report but please check your setup first.  See the README at %s", cfg.Branding.URL)
	renderError(w, "500 - Internal Server Error", http.StatusInternalServerError)
}

// cancelClearSetError convenience method to keep it DRY
func cancelClearSetError(w http.ResponseWriter, r *http.Request, e error) {
	log.Warn(e)
	cookie.ClearCookie(w, r)
	w.Header().Set(cfg.Cfg.Headers.Error, e.Error())
	addErrandCancelRequest(r)
}

// cfg.ErrCtx is tested by `jwtmanager.JWTCacheHandler`
func addErrandCancelRequest(r *http.Request) {
	ctx, cancel := context.WithCancel(r.Context())
	ctx = context.WithValue(ctx, cfg.ErrCtxKey, true)
	*r = *r.Clone(ctx)
	cancel() // we're done
}
```

## File: `pkg/structs/structs.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package structs

import (
	"strconv"
)

// CustomClaims Temporary struct storing custom claims until JWT creation.
type CustomClaims struct {
	Claims map[string]interface{}
}

// UserI each *User struct must prepare the data for being placed in the JWT
type UserI interface {
	PrepareUserData()
}

// User is inherited.
type User struct {
	// TODO: set Provider here so that we can pass it to db
	// populated by db (via mapstructure) or from provider (via json)
	// Provider   string `json:"provider",mapstructure:"provider"`
	Username   string `json:"username" mapstructure:"username"`
	Name       string `json:"name" mapstructure:"name"`
	Email      string `json:"email" mapstructure:"email"`
	CreatedOn  int64  `json:"createdon"`
	LastUpdate int64  `json:"lastupdate"`
	// don't populate ID from json https://github.com/vouch/vouch-proxy/issues/185
	ID int `json:"-" mapstructure:"id"`
	// jwt.StandardClaims

	TeamMemberships []string
}

// PrepareUserData implement PersonalData interface
func (u *User) PrepareUserData() {
	if u.Username == "" {
		u.Username = u.Email
	}
}

// AzureUser is a retrieved and authenticated user from Azure AD
type AzureUser struct {
	User
	Sub               string `json:"sub"`
	UPN               string `json:"upn"`
	PreferredUsername string `json:"preferred_username"`
}

// PrepareUserData implement PersonalData interface
func (u *AzureUser) PrepareUserData() {
	// AzureAD uses the 'upn' (UserPrincipleName) field to store the email address of the user
	// See https://docs.microsoft.com/en-us/azure/active-directory/hybrid/plan-connect-userprincipalname

	if u.Username == "" {
		u.Username = u.UPN
	}

	if u.Username == "" {
		u.Username = u.PreferredUsername
	}

	if u.Email == "" {
		u.Email = u.UPN
	}
}

// GoogleUser is a retrieved and authentiacted user from Google.
// unused!
// TODO: see if these should be pointers to the *User object as per
// https://golang.org/doc/effective_go.html#embedding
type GoogleUser struct {
	User
	Sub           string `json:"sub"`
	GivenName     string `json:"given_name"`
	FamilyName    string `json:"family_name"`
	Profile       string `json:"profile"`
	Picture       string `json:"picture"`
	EmailVerified bool   `json:"email_verified"`
	Gender        string `json:"gender"`
	HostDomain    string `json:"hd"`
	// jwt.StandardClaims
}

// PrepareUserData implement PersonalData interface
func (u *GoogleUser) PrepareUserData() {
	u.Username = u.Email
}

// ADFSUser Active Directory user record
type ADFSUser struct {
	User
	Sub string `json:"sub"`
	UPN string `json:"upn"`
	// UniqueName string `json:"unique_name"`
	// PwdExp     string `json:"pwd_exp"`
	// SID        string `json:"sid"`
	// Groups     string `json:"groups"`
	// jwt.StandardClaims
}

// PrepareUserData implement PersonalData interface
func (u *ADFSUser) PrepareUserData() {
	u.Username = u.UPN
}

// GitHubUser is a retrieved and authentiacted user from GitHub.
type GitHubUser struct {
	User
	Login   string `json:"login"`
	Picture string `json:"avatar_url"`
	// jwt.StandardClaims
}

// GitHubTeamMembershipState for GitHub team api call
type GitHubTeamMembershipState struct {
	State string `json:"state"`
}

// PrepareUserData implement PersonalData interface
func (u *GitHubUser) PrepareUserData() {
	// always use the u.Login as the u.Username
	u.Username = u.Login
}

// IndieAuthUser see indieauth.net
type IndieAuthUser struct {
	User
	URL string `json:"me"`
}

// PrepareUserData implement PersonalData interface
func (u *IndieAuthUser) PrepareUserData() {
	u.Username = u.URL
}

// Contact used for OpenStaxUser
type Contact struct {
	Type     string `json:"type"`
	Value    string `json:"value"`
	Verified bool   `json:"is_verified"`
}

// OpenStaxUser is a retrieved and authenticated user from OpenStax Accounts
type OpenStaxUser struct {
	User
	Contacts []Contact `json:"contact_infos"`
}

// PrepareUserData implement PersonalData interface
func (u *OpenStaxUser) PrepareUserData() {
	if u.Email == "" {
		// assuming first contact of type "EmailAddress"
		for _, c := range u.Contacts {
			if c.Type == "EmailAddress" && c.Verified {
				u.Email = c.Value
				break
			}
		}
	}
}

// Ocs used for NextcloudUser
type Ocs struct {
	Data struct {
		UserID string `json:"id"`
		Email  string `json:"email"`
	} `json:"data"`
}

// NextcloudUser User of Nextcloud retreived from ocs endpoint
type NextcloudUser struct {
	User
	Ocs Ocs `json:"ocs"`
}

// PrepareUserData NextcloudUser
func (u *NextcloudUser) PrepareUserData() {
	if u.Username == "" {
		u.Username = u.Ocs.Data.UserID
		u.Email = u.Ocs.Data.Email
	}
}

// AlibabaUser Aliyun
type AlibabaUser struct {
	User
	Data AliData `json:"data"`
	// jwt.StandardClaims
}

// PrepareUserData implement PersonalData interface
func (u *AlibabaUser) PrepareUserData() {
	u.Username = u.Data.Username
	u.Name = u.Data.Nickname
	u.Email = u.Data.Email
	id, _ := strconv.Atoi(u.Data.ID)
	u.ID = id
}

// AliData `data` subobject of Alibaba User response
// https://github.com/vouch/vouch-proxy/issues/344
type AliData struct {
	Sub      string `json:"sub"`
	Username string `json:"username"`
	Nickname string `json:"nickname"`
	Email    string `json:"email"`
	ID       string `json:"ou_id"`
	Phone    string `json:"phone_number"`
	OuName   string `json:"ou_name"`
}

// Team has members and provides acess to sites
type Team struct {
	Name       string   `json:"name" mapstructure:"name"`
	Members    []string `json:"members" mapstructure:"members"` // just the emails
	Sites      []string `json:"sites" mapstructure:"sites"`     // just the domains
	CreatedOn  int64    `json:"createdon" mapstructure:"createdon"`
	LastUpdate int64    `json:"lastupdate" mapstructure:"lastupdate"`
	ID         int      `json:"id" mapstructure:"id"`
}

// Site is the basic unit of auth
type Site struct {
	Domain     string `json:"domain"`
	CreatedOn  int64  `json:"createdon"`
	LastUpdate int64  `json:"lastupdate"`
	ID         int    `json:"id" mapstructure:"id"`
}

// PTokens provider tokens (from the IdP)
type PTokens struct {
	PAccessToken string
	PIdToken     string
}

// DiscordUser deserializes values from the Discord User Object: https://discord.com/developers/docs/resources/user#user-object-user-structure
type DiscordUser struct {
	Id            string `json:"id"`
	Username      string `json:"username"`
	Discriminator string `json:"discriminator"`
	GlobalName    string `json:"global_name"`
	Email         string `json:"email"`
	Verified      bool   `json:"verified"`

	PreparedUsername string
}
```

## File: `pkg/timelog/timelog.go`
```go
/*

Copyright 2020 The Vouch Proxy Authors.
Use of this source code is governed by The MIT License (MIT) that
can be found in the LICENSE file. Software distributed under The
MIT License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.

*/

package timelog

import (
	"context"
	"fmt"
	"net/http"
	"time"

	"github.com/vouch/vouch-proxy/pkg/capturewriter"
	"github.com/vouch/vouch-proxy/pkg/cfg"
	"go.uber.org/zap"
)

var (
	req        = int64(0)
	avgLatency = int64(0)
	log        *zap.SugaredLogger
)

// Configure see main.go configure()
func Configure() {
	log = cfg.Logging.Logger

	capturewriter.Configure()

}

// TimeLog records how long it takes to process the http request and produce the response (latency)
func TimeLog(nextHandler http.Handler) func(http.ResponseWriter, *http.Request) {
	return func(w http.ResponseWriter, r *http.Request) {
		// log.Debugf("Request received : %v", r)
		start := time.Now()

		// make the call
		v := capturewriter.CaptureWriter{ResponseWriter: w, StatusCode: 0}
		ctx := context.Background()
		nextHandler.ServeHTTP(&v, r.WithContext(ctx))

		// Stop timer
		end := time.Now()

		go func() {
			latency := end.Sub(start)
			req++
			avgLatency = avgLatency + ((int64(latency) - avgLatency) / req)
			// log.Debugf("Request handled successfully: %v", v.GetStatusCode())
			var statusCode = v.GetStatusCode()

			path := r.URL.Path
			host := r.Host
			referer := r.Header.Get("Referer")
			clientIP := r.RemoteAddr
			method := r.Method

			log.Infow(fmt.Sprintf("|%d| %10v %s", statusCode, time.Duration(latency), path),
				"statusCode", statusCode,
				"request", req,
				"latency", time.Duration(latency),
				"avgLatency", time.Duration(avgLatency),
				"ipPort", clientIP,
				"method", method,
				"host", host,
				"path", path,
				"referer", referer,
			)
		}()

	}
}
```

## File: `static/css/main.css`
```css
@charset "UTF-8";

body,
button,
input,
select,
textarea {
  font-family: BlinkMacSystemFont, -apple-system, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    'Helvetica', 'Arial', sans-serif;
}

code,
pre {
  -moz-osx-font-smoothing: auto;
  -webkit-font-smoothing: auto;
  font-family: monospace;
}

body {
  background-color: #ffffff;
  margin: 5px 10px;
}

.top img {
  height: 50px;
  width: 50px;
  margin: 10px;
  vertical-align: middle;
}

.top span {
  margin: 5px;
  font-size: 1.5em;
}

.top a {
  text-decoration: none;
}

.top a,
.bottom a {
  color: #000000;
}

.content {
  margin: 5px 10px;
}

.test {
  clear: both;
}
```

## File: `templates/auth.tmpl`
```
<!DOCTYPE html>
<link rel="icon"
      type="image/png"
      href="/img/favicon.ico" />
<html>
  <head>
    <link rel="stylesheet" href="/css/main.css">
  </head>
  <body>
      <a href="{{ .link }}"><button>Login with Google!</button></a>
  </body>
</html>
```

## File: `templates/error.tmpl`
```
<!DOCTYPE html>
<link rel="icon"
      type="image/png"
      href="/img/favicon.ico" />
<html>
  <head>
    <link rel="stylesheet" href="/css/main.css">
  </head>
  <body>
    <h1>{{ .message }}</h1>
  </body>
</html>
```

## File: `templates/index.tmpl`
```
<!DOCTYPE html>
<html>
  <head>
    <link rel="icon" type="image/png" href="{{ .DocumentRoot }}/static/img/favicon.ico" />
    <link rel="stylesheet" href="{{ .DocumentRoot }}/static/css/main.css" />
    <meta name="robots" content="noindex, nofollow" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta
      name="viewport"
      content="width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=7"
    />
    <title>Vouch Proxy - {{ .Msg }}</title>
  </head>
  <body>
<div class="top">
  <a href="https://github.com/vouch/vouch-proxy"><img src="{{ .DocumentRoot }}/static/img/multicolor_V_500x500.png"/></a>
  <a href="https://github.com/vouch/vouch-proxy"><span>Vouch Proxy</span></a>
</div>

<div class="content">
<h1>{{ .Msg }}</h1>

{{ if .Testing }}
<p class="test">
<h2>-- test mode --</h2>
The config file includes <code>testing: true</code>
<p/>
All 302 redirects will be captured and presented as links here


<ul>
  <li><a href="{{ .DocumentRoot }}/login">login</a></li>
  <li><a href="{{ .DocumentRoot }}/logout">logout</a></li>
  <li><a href="{{ .DocumentRoot }}/validate">validate</a></li>
{{ if .TestURLs }}
  {{ range $url := .TestURLs}}
  <li><a href="{{ $url }}">{{ $url }}</a></li>
  {{ end }}
{{ end }}
</ul>
{{ end }}
<div class="bottom">
For support, please contact your network administrator or whomever configured Nginx to use Vouch Proxy.
<p/>
For help with <a href="https://github.com/vouch/vouch-proxy">Vouch Proxy</a> or to file a bug report, please visit <a href="https://github.com/vouch/vouch-proxy">https://github.com/vouch/vouch-proxy</a>
<p/>
</div>
</div>
  </body>
</html>
```

