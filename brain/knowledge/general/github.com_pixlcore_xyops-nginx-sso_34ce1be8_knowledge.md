---
id: github.com-pixlcore-xyops-nginx-sso-34ce1be8-knowl
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:13.202752
---

# KNOWLEDGE EXTRACT: github.com_pixlcore_xyops-nginx-sso_34ce1be8
> **Extracted on:** 2026-04-01 16:45:50
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525295/github.com_pixlcore_xyops-nginx-sso_34ce1be8

---

## File: `Dockerfile`
```
FROM nginx:latest

RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y nodejs
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/healthcheck
COPY . .

RUN mv nginx.conf /etc/nginx/
RUN mv conf.d/* /etc/nginx/conf.d/

RUN npm install -g @pixlcore/xyops-healthcheck

CMD ["sh", "start.sh"]
```

## File: `LICENSE.md`
```markdown
# License

**The MIT License (MIT)**

*Copyright (c) 2025 - 2026 PixlCore LLC*

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `README.md`
```markdown
# xyOps Multi-Master Nginx TLS/SSO

This repo generates a custom Docker Image designed to be used with [xyOps](https://xyops.io).

This is a wrapper around the official [Nginx Docker Image](https://hub.docker.com/_/nginx), which layers in [Node.js](https://nodejs.org/) and a custom [Health Check Daemon](https://github.com/pixlcore/xyops-healthcheck) for [xyOps](https://xyops.io).  This is for use with xyOps multi-master setups, utilizing TLS, and [OAuth2-Proxy](https://github.com/oauth2-proxy/oauth2-proxy) for SSO integration.  For setup instructions, please see the [xyOps SSO Setup Guide](https://github.com/pixlcore/xyops/blob/main/docs/sso.md).

## Current Versions

- Nginx v1.28
- OAuth2-Proxy v7.12
- Node.js v22
- Health Check v1.0.5

# Usage

## Docker

This repo automatically publishes a Docker image on every tag, which is designed to run with [Nginx](https://nginx.org/) for xyOps mutli-master installs.  For usage instructions, see the [xyOps SSO Setup Guide](https://github.com/pixlcore/xyops/blob/main/docs/sso.md).  The Docker Image name is:

```
ghcr.io/pixlcore/xyops-nginx-sso
```

Example use:

```yaml
services:
  nginx:
    image: ghcr.io/pixlcore/xyops-nginx-sso:latest
    depends_on:
      - oauth2-proxy
    init: true
    environment:
      XYOPS_masters: xyops01.yourcompany.com,xyops02.yourcompany.com
      XYOPS_port: 5522
    volumes:
      - "./tls.crt:/etc/tls.crt:ro"
      - "./tls.key:/etc/tls.key:ro"
    ports:
      - "443:443"
    networks:
      xyops-net:

  oauth2-proxy:
    image: quay.io/oauth2-proxy/oauth2-proxy:latest
    ...
```

# License

**The MIT License (MIT)**

*Copyright (c) 2025 - 2026 PixlCore LLC.*

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

## File: `nginx.conf`
```

user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log debug;
pid        /run/nginx.pid;


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

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}
```

## File: `package.json`
```json
{
	"name": "xyops-nginx-sso",
	"version": "1.0.8",
	"private": true,
	"description": "xyOps Multi-Master Nginx TLS/SSO.",
	"author": "Joseph Huckaby <jhuckaby@pixlcore.com>",
	"homepage": "https://github.com/pixlcore/xyops-nginx-sso"
}
```

## File: `start.sh`
```bash
#!/bin/sh

# Start healthcheck as a background daemon process (it does this itself)
/usr/bin/xyops-healthcheck

# Start nginx in the foreground
exec /usr/sbin/nginx -g 'daemon off;'
```

## File: `conf.d/backend.conf`
```
# dummy backend route, will be overwritten by healthcheck
upstream backend {
	server 127.0.0.1:5522;
}
```

## File: `conf.d/default.conf`
```
# ---------- upstreams ----------
upstream oauth2_upstream {
	server oauth2-proxy:4180;
}

# ---------- WebSocket support ----------
map $http_upgrade $connection_upgrade {
	default upgrade;
	''      close;
}

# ---------- HTTPS configuration ----------
server {
	listen 443 ssl;
	
	ssl_certificate     /etc/tls.crt;
	ssl_certificate_key /etc/tls.key;
	# ssl_certificate /etc/ssl/certs/ssl-cert-snakeoil.pem;
	# ssl_certificate_key /etc/ssl/private/ssl-cert-snakeoil.key;
	
	# Always tell upstreams the original scheme/host/client IP
	proxy_set_header Host               $host;
	proxy_set_header X-Real-IP          $remote_addr;
	proxy_set_header X-Forwarded-For    $proxy_add_x_forwarded_for;
	proxy_set_header X-Forwarded-Host   $host;
	proxy_set_header X-Forwarded-Proto  $scheme;
	
	# Bypass auth for static/public paths
	location ~ ^/(api|files|health|images|js|css|fonts|sounds|codemirror|manifest.webmanifest)(/|$) {
		proxy_pass http://backend;
	}
	
	# ---- the auth subrequest for protected routes ----
	location = /oauth2/auth {
		internal;
		proxy_pass http://oauth2_upstream;
		proxy_set_header Host              $host;
		proxy_set_header X-Original-URI    $request_uri;
		proxy_set_header X-Real-IP         $remote_addr;
		proxy_set_header X-Forwarded-Proto $scheme;
		proxy_set_header X-Forwarded-Uri   $request_uri;
		proxy_pass_request_body off; # /auth only needs headers
		proxy_set_header Content-Length ""; 
	}
	
	# ---- proxy the oauth2-proxy app endpoints (/oauth2/*) ----
	# These handle sign_in/start/callback, cookie setting, etc.
	location /oauth2/ {
		proxy_pass http://oauth2_upstream;
		proxy_set_header Host $host;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-Proto $scheme;
	}
	
	# ---- your protected app ----
	location / {
		set $return_to "$scheme://$http_host$uri$is_args$args";
		
		# Check auth first
		auth_request /oauth2/auth;
		
		# If auth says 401, send user into the signin flow with return-to
		error_page 401 = @oauth2_signin;
		
		proxy_set_header Host               $host;
		proxy_set_header X-Real-IP          $remote_addr;
		proxy_set_header X-Forwarded-For    $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Host   $host;
		proxy_set_header X-Forwarded-Proto  $scheme;
		
		# hoist identity headers from the subrequest to the app
		auth_request_set $user   $upstream_http_x_auth_request_user;
		auth_request_set $email  $upstream_http_x_auth_request_email;
		auth_request_set $groups $upstream_http_x_auth_request_groups;
		auth_request_set $authz  $upstream_http_authorization;
		
		proxy_set_header X-Auth-Request-User   $user;
		proxy_set_header X-Auth-Request-Email  $email;
		proxy_set_header X-Auth-Request-Groups $groups;
		proxy_set_header Authorization         $authz;
		
		# Support for WebSockets
		proxy_http_version 1.1;
		proxy_set_header Upgrade $http_upgrade;
		proxy_set_header Connection $connection_upgrade;
		proxy_read_timeout 30s;
		proxy_send_timeout 30s;
		
		# Pass along to xyOps
		proxy_pass http://backend;
	}
	
	# Centralized redirect to login (preserves original URL)
	location @oauth2_signin {
		return 302 /oauth2/start?rd=$return_to;
	}
	
}
```

