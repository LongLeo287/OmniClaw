---
id: pixl-server-web-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:30:59.367939
---

# KNOWLEDGE EXTRACT: pixl-server-web
> **Extracted on:** 2026-03-30 13:36:26
> **Source:** pixl-server-web

---

## File: `.npmignore`
```
.gitignore
node_modules/
test/test.log

```

## File: `package.json`
```json
{
	"name": "pixl-server-web",
	"version": "3.0.4",
	"description": "A web server component for the pixl-server framework.",
	"author": "Joseph Huckaby <jhuckaby@gmail.com>",
	"homepage": "https://github.com/jhuckaby/pixl-server-web",
	"license": "MIT",
	"main": "web_server.js",
	"repository": {
		"type": "git",
		"url": "https://github.com/jhuckaby/pixl-server-web"
	},
	"bugs": {
		"url": "https://github.com/jhuckaby/pixl-server-web/issues"
	},
	"keywords": [
		"web",
		"http",
		"https",
		"ssl"
	],
	"dependencies": {
		"async": "3.2.2",
		"class-plus": "^1.0.0",
		"errno": "0.1.7",
		"formidable": "3.5.4",
		"mime": "2.5.2",
		"pixl-acl": "^1.0.4",
		"pixl-perf": "^1.0.0",
		"pixl-server": "^1.0.0",
		"stream-meter": "1.0.4"
	},
	"devDependencies": {
		"pixl-request": "^2.0.0",
		"pixl-unit": "^1.0.0"
	},
	"scripts": {
		"test": "pixl-unit test/test.js"
	}
}
```

## File: `README.md`
```markdown
# Overview

This module is a component for use in [pixl-server](https://www.github.com/jhuckaby/pixl-server).  It implements a simple web server with support for both HTTP and HTTPS, serving static files, and hooks for adding custom URI handlers.

# Table of Contents

<!-- toc -->
- [Usage](#usage)
- [Configuration](#configuration)
	* [port](#port)
	* [alt_ports](#alt_ports)
	* [bind_address](#bind_address)
	* [htdocs_dir](#htdocs_dir)
	* [max_upload_size](#max_upload_size)
	* [temp_dir](#temp_dir)
	* [static_ttl](#static_ttl)
	* [static_index](#static_index)
	* [server_signature](#server_signature)
	* [compress_text](#compress_text)
	* [regex_text](#regex_text)
	* [regex_json](#regex_json)
	* [response_headers](#response_headers)
	* [code_response_headers](#code_response_headers)
	* [uri_response_headers](#uri_response_headers)
	* [timeout](#timeout)
	* [request_timeout](#request_timeout)
	* [keep_alives](#keep_alives)
		+ [default](#default)
		+ [request](#request)
		+ [close](#close)
	* [keep_alive_timeout](#keep_alive_timeout)
	* [socket_prelim_timeout](#socket_prelim_timeout)
	* [max_requests_per_connection](#max_requests_per_connection)
	* [gzip_opts](#gzip_opts)
	* [enable_brotli](#enable_brotli)
	* [brotli_opts](#brotli_opts)
	* [default_acl](#default_acl)
	* [blacklist](#blacklist)
	* [whitelist](#whitelist)
	* [allow_hosts](#allow_hosts)
	* [rewrites](#rewrites)
	* [redirects](#redirects)
	* [log_requests](#log_requests)
	* [log_request_details](#log_request_details)
	* [log_body_max](#log_body_max)
	* [regex_log](#regex_log)
	* [log_perf](#log_perf)
	* [perf_threshold_ms](#perf_threshold_ms)
	* [perf_report](#perf_report)
	* [recent_requests](#recent_requests)
	* [max_connections](#max_connections)
	* [max_concurrent_requests](#max_concurrent_requests)
	* [max_queue_length](#max_queue_length)
	* [max_queue_active](#max_queue_active)
	* [queue_skip_uri_match](#queue_skip_uri_match)
	* [clean_headers](#clean_headers)
	* [log_socket_errors](#log_socket_errors)
	* [full_uri_match](#full_uri_match)
	* [flatten_query](#flatten_query)
	* [req_max_dump_enabled](#req_max_dump_enabled)
	* [req_max_dump_dir](#req_max_dump_dir)
	* [req_max_dump_debounce](#req_max_dump_debounce)
	* [public_ip_offset](#public_ip_offset)
	* [legacy_callback_support](#legacy_callback_support)
	* [startup_message](#startup_message)
	* [debug_ttl](#debug_ttl)
	* [debug_bind_local](#debug_bind_local)
	* [chaos](#chaos)
	* [auth](#auth)
	* [https](#https)
	* [https_port](#https_port)
	* [https_alt_ports](#https_alt_ports)
	* [https_cert_file](#https_cert_file)
	* [https_key_file](#https_key_file)
	* [https_ca_file](#https_ca_file)
	* [https_force](#https_force)
	* [https_header_detect](#https_header_detect)
	* [https_timeout](#https_timeout)
	* [https_bind_address](#https_bind_address)
	* [https_cert_poll_ms](#https_cert_poll_ms)
- [Custom URI Handlers](#custom-uri-handlers)
	* [Access Control Lists](#access-control-lists)
	* [Internal File Redirects](#internal-file-redirects)
	* [Static Directory Handlers](#static-directory-handlers)
	* [Sending Responses](#sending-responses)
		+ [Standard Response](#standard-response)
		+ [Custom Response](#custom-response)
		+ [JSON Response](#json-response)
		+ [Non-Response](#non-response)
	* [args](#args)
		+ [args.request](#argsrequest)
		+ [args.response](#argsresponse)
		+ [args.ip](#argsip)
		+ [args.ips](#argsips)
		+ [args.query](#argsquery)
		+ [args.params](#argsparams)
			- [Standard HTTP POST](#standard-http-post)
			- [JSON REST POST](#json-rest-post)
			- [Unknown POST](#unknown-post)
		+ [args.files](#argsfiles)
		+ [args.cookies](#argscookies)
		+ [args.perf](#argsperf)
		+ [args.server](#argsserver)
		+ [args.id](#argsid)
		+ [args.setCookie](#argssetcookie)
	* [Request Filters](#request-filters)
- [Transaction Logging](#transaction-logging)
	* [Request Detail Logging](#request-detail-logging)
	* [Performance Threshold Logging](#performance-threshold-logging)
		+ [Including Diagnostic Reports](#including-diagnostic-reports)
	* [Including Custom Metrics](#including-custom-metrics)
- [Stats](#stats)
	* [The Server Object](#the-server-object)
	* [The Stats Object](#the-stats-object)
	* [The Listeners Object](#the-listeners-object)
	* [The Sockets Object](#the-sockets-object)
	* [The Recent Object](#the-recent-object)
	* [The Queue Object](#the-queue-object)
	* [Stats URI Handler](#stats-uri-handler)
- [Misc](#misc)
	* [Determining HTTP or HTTPS](#determining-http-or-https)
	* [Self-Referencing URLs](#self-referencing-urls)
	* [Custom Method Handlers](#custom-method-handlers)
	* [Let's Encrypt / ACME TLS Certificates](#lets-encrypt--acme-tls-certificates)
		+ [ACME clients](#acme-clients)
		+ [Point your domain at your server](#point-your-domain-at-your-server)
		+ [Install Certbot](#install-certbot)
			- [Ubuntu / Debian](#ubuntu--debian)
			- [RHEL / CentOS / Fedora](#rhel--centos--fedora)
		+ [Option A: HTTP-01 (webroot)](#option-a-http-01-webroot)
			- [Ensure HTTP is working on port 80](#ensure-http-is-working-on-port-80)
			- [Issue a certificate using webroot](#issue-a-certificate-using-webroot)
		+ [Configure pixl-server-web for HTTPS](#configure-pixl-server-web-for-https)
		+ [Automatic renewal](#automatic-renewal)
			- [Check that renewal timers are installed](#check-that-renewal-timers-are-installed)
		+ [Option B: DNS-01 with DNS API (wildcards, advanced)](#option-b-dns-01-with-dns-api-wildcards-advanced)
			- [Using Certbot DNS plugins](#using-certbot-dns-plugins)
			- [Using acme.sh](#using-acmesh)
		+ [Where your certificates live](#where-your-certificates-live)
		+ [Troubleshooting](#troubleshooting)
	* [Request Max Dump](#request-max-dump)
- [License](#license)

# Usage

Use [npm](https://www.npmjs.com/) to install the module:

```sh
npm install pixl-server pixl-server-web
```

Here is a simple usage example.  Note that the component's official name is `WebServer`, so that is what you should use for the configuration key, and for gaining access to the component via your server object.

```js
const PixlServer = require('pixl-server');
let server = new PixlServer({
	
	__name: 'MyServer',
	__version: "1.0",
	
	config: {
		"log_dir": "/var/log",
		"debug_level": 9,
		
		"WebServer": {
			"port": 80,
			"htdocs_dir": "/var/www/html"
		}
	},
	
	components: [
		require('pixl-server-web')
	]
	
});

server.startup( function() {
	// server startup complete
	
	server.WebServer.addURIHandler( '/my/custom/uri', 'Custom Name', function(args, callback) {
		// custom request handler for our URI
		callback( 
			"200 OK", 
			{ 'Content-Type': "text/html" }, 
			"Hello this is custom content!\n" 
		);
	} );
} );
```

Notice how we are loading the [pixl-server](https://www.github.com/jhuckaby/pixl-server) parent module, and then specifying [pixl-server-web](https://www.github.com/jhuckaby/pixl-server-web) as a component:

```js
components: [
	require('pixl-server-web')
]
```

This example is a very simple web server configuration, which will listen on port 80 and serve static files out of `/var/www/html`.  However, if the URI is `/my/custom/uri`, a custom callback function is fired and can serve up any response it wants.  This is a great way to implement an API.

# Configuration

The configuration for this component is set by passing in a `WebServer` key in the `config` element when constructing the `PixlServer` object, or, if a JSON configuration file is used, a `WebServer` object at the outermost level of the file structure.  It can contain the following keys:

## port

This is the main port to listen on.  The standard web port is 80, but note that only the root user can listen on ports below 1024.

## alt_ports

If you would like to have the server listen on additional ports, add them here as an array.  Example:

```json
{
	"port": 80,
	"alt_ports": [ 3000, 8080 ]
}
```

## bind_address

Optionally specify an exact local IP address to bind the listeners to.  By default this binds to all available addresses on the machine.  Example:

```json
{
	"bind_address": "127.0.0.1"
}
```

This example would cause the server to *only* listen on localhost, and not any external network interface.

## htdocs_dir

This is the path to the directory to serve static files out of, e.g. `/var/www/html`.

## max_upload_size

This is the maximum allowed upload size.  If uploading files, this is a per-file limit.  If submitting raw data, this is an overall POST content limit.  The default is 32MB.

## temp_dir

This is where file uploads will be stored temporarily, until they are renamed or deleted.  If omitted, this defaults to the operating system's temp directory, as returned from `os.tmpDir()`.

## static_ttl

This is the TTL (time to live) value to pass on the `Cache-Control` response header.  This causes static files to be cached for a number of seconds.  The default is 0 seconds.

## static_index

This sets the filename to look for when directories are requested.  It defaults to `index.html`.

## server_signature

This is a string to send back to the client with every request, as the `Server` HTTP response header.  This is typically used to declare the web server software being used.  The default is `WebServer`.

## compress_text

This is a boolean indicating whether or not to compress text responses using [zlib](https://nodejs.org/api/zlib.html) software compression in Node.js.  The default is `false`.  The compression format is chosen automatically based on the `Accept-Encoding` request header sent from the client.  The supported formats are Brotli (see [enable_brotli](#enable_brotli)), Gzip and Deflate, chosen in that order.

You can force compression on an individual response basis, by including a `X-Compress: 1` response header in your URI handler code.  The web server will detect this outgoing header and force-enable compression on the data, regardless of the `compress_text` or `regex_text` settings.  Note that it still honors the client `Accept-Encoding` header, and will only enable compression if this request header is present and contains a supported scheme.

**Note:** The legacy `gzip_text` property is still supported, and is now a shortcut for `compress_text`.

## regex_text

This is a regular expression string which is compared against the `Content-Type` response header.  When this matches, and [compress_text](#compress_text) is enabled, this will kick in compression.  It defaults to `(text|javascript|json|css|html)`.

## regex_json

This is a regular expression string used to determine if the incoming POST request contains JSON.  It is compared against the `Content-Type` request header.  The default is `(javascript|js|json)`.

## response_headers

This param allows you to send back additional custom HTTP headers with *every* response.  Set the param to an object containing keys for each header, like this:

```json
{
	"response_headers": {
		"X-My-Custom-Header": "12345",
		"X-Another-Header": "Hello"
	}
}
```

## code_response_headers

This property allows you to include *conditional* response headers, based on the HTTP response code.  For example, you can instruct the web server to send back a custom header with `404` (File Not Found) responses, like this:

```json
{
	"code_response_headers": {
		"404": {
			"X-Message": "And don't come back!"
		}
	}
}
```

An actual useful case would be to include a [Retry-After](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After) header with all `429` (Too Many Requests) responses, like this:

```json
{
	"code_response_headers": {
		"429": {
			"Retry-After": "10"
		}
	}
}
```

This would give a hint to clients when they receive a `429` (Too Many Requests) response from the web server, that they should wait `10` seconds before trying again.

## uri_response_headers

This property allows you to include *conditional* response headers, based on regular expression matches on incoming request URIs.  You may specify multiple patterns, and multiple headers to inject for each URI match.  For example, you can instruct the web server to send back custom headers for a specific URI prefix, like this:

```json
{
	"uri_response_headers": {
		"^/secret": {
			"X-Message": "You found the secret area!",
			"X-Foo": "Bar"
		}
	}
}
```

An actual useful case would be to include a set of [CSP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) for all HTML files, and URIs that end in a slash (which typically present an HTML file).  Example:

```json
{
	"uri_response_headers": {
		"(\/|\\.html)$": {
			"Content-Security-Policy": "default-src 'none'; script-src 'self'; script-src-elem 'self'; script-src-attr 'unsafe-inline'; style-src 'self' 'unsafe-inline'; style-src-attr 'unsafe-inline'; manifest-src 'self';img-src 'self' data: blob:; font-src 'self'; connect-src 'self' ws: wss:; media-src 'self' blob:; worker-src 'self' blob:; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'none';",
			"X-Content-Type-Options": "nosniff",
			"Referrer-Policy": "strict-origin-when-cross-origin",
			"Permissions-Policy": "camera=(), microphone=(), geolocation=(), fullscreen=()"
		}
	}
}
```

## timeout

This sets the idle socket timeout for all incoming HTTP requests, in seconds.  If omitted, the Node.js default is 120 seconds.  Example:

```json
{
	"timeout": 120
}
```

This only applies to reading from sockets when data is expected.  It is an *idle read timeout* on the socket itself, and doesn't apply to request handlers.

## request_timeout

This property sets an actual hard request timeout for all incoming requests.  If the total combined request processing, handling and response time exceeds this value, specified in seconds, then the request is aborted and a `HTTP 408 Request Timeout` response is sent back to the client.  This defaults to `0` (disabled).  Example use:

```json
{
	"request_timeout": 300
}
```

Note that this includes request processing time (e.g. receiving uploaded data from a HTTP POST).

## keep_alives

This controls the [HTTP Keep-Alive](https://en.wikipedia.org/wiki/HTTP_persistent_connection) behavior in the web server.  There are three possible settings, which should be specified as a string:

### default

```json
{
	"keep_alives": "default"
}
```

This **enables** Keep-Alives for all incoming connections by default, unless the client specifically requests a close connection via a `Connection: close` header.

### request

```json
{
	"keep_alives": "request"
}
```

This **disables** Keep-Alives for all incoming connections by default, unless the client specifically requests a Keep-Alive connection by passing a `Connection: keep-alive` header.

### close

```json
{
	"keep_alives": "close"
}
```

This completely disables Keep-Alives for all connections.  All requests result in the socket being closed after completion, and each socket only serves one single request.

## keep_alive_timeout

This sets the HTTP Keep-Alive idle timeout for all sockets, measured in seconds.  If omitted, the Node.js default is 5 seconds.  See [server.keepAliveTimeout](https://nodejs.org/api/http.html#serverkeepalivetimeout) for details.  Example:

```json
{
	"keep_alive_timeout": 5
}
```

## socket_prelim_timeout

This sets a special preliminary timeout for brand new sockets when they are first connected, measured in seconds.  If an HTTP request doesn't come over the socket within this timeout (specified in seconds), then the socket is hard closed.  This timeout should always be set lower than the [timeout](#timeout) if used.  This defaults to `0` (disabled).  Example use:

```json
{
	"socket_prelim_timeout": 3
}
```

The idea here is to prevent certain DDoS-style attacks, where an attacker opens a large amount of TCP connections without sending any requests over them.

**Note:** Do not enable this feature if you attach a WebSocket server such as [ws](https://github.com/websockets/ws).

## max_requests_per_connection

This allows you to set a maximum number of requests to allow per Keep-Alive connection.  It defaults to `0` which means unlimited.  If set, and the maximum is reached, a `Connection: close` header is returned, politely asking the client to close the connection.  It does not actually hard-close the socket.  Example:

```json
{
	"max_requests_per_connection": 100
}
```

## gzip_opts

This allows you to set various options for the automatic GZip compression in HTTP responses.  Example:

```json
{
	"gzip_opts": {
		"level": 6,
		"memLevel": 8
	}
}
```

Please see the Node [Zlib Class Options](https://nodejs.org/api/zlib.html#class-options) for more details on what can be set here.

## enable_brotli

Set this to `true` to enable [Brotli](https://en.wikipedia.org/wiki/Brotli) compression support.  The default is `false` (disabled).  When enabled, and the client advertises support via the `Accept-Encoding` request header, and [compress_text](#compress_text) is enabled, and the response `Content-Type` matches the [regex_text](#regex_text) pattern, Brotli will be used.

Brotli is a newer compression format written by Google, which was added to Node.js in v10.16.0.  With careful tuning (see below) you can produce equivalent payload sizes to Gzip but considerably faster (i.e. less CPU), or even up to ~20% smaller sizes than Gzip but much slower (i.e. more CPU).

## brotli_opts

If [enable_brotli](#enable_brotli) is set to `true`, then you can set various options via the `brotli_opts` configuration property.  Example:

```json
{
	"brotli_opts": {
		"chunkSize": 16 * 1024,
		"mode": "text",
		"level": 4,
		"hint": 0
	}
}
```

See the Node [Brotli Class Options](https://nodejs.org/api/zlib.html#class-brotlioptions) for more details on what can be set here.  Note that `mode` is a convenience shortcut for `zlib.constants.BROTLI_PARAM_MODE` (which can set to `text`, `font` or `generic`), `level` is a shortcut for `zlib.constants.BROTLI_PARAM_QUALITY`, and `hint` is a shortcut for `zlib.constants.BROTLI_PARAM_SIZE_HINT`.

## default_acl

This allows you to configure the default [ACL](https://en.wikipedia.org/wiki/Access_control_list), which is only used for URI handlers that register themselves as private.  To customize it, specify an array of [IPv4](https://en.wikipedia.org/wiki/IPv4) and/or [IPv6](https://en.wikipedia.org/wiki/IPv6) addresses, partials or [CIDR blocks](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).  It defaults to [localhost](https://en.wikipedia.org/wiki/Localhost) plus the [IPv4 private reserved](https://en.wikipedia.org/wiki/Private_network#Private_IPv4_addresses) and [IPv6 private reserved ranges](https://en.wikipedia.org/wiki/Private_network#Private_IPv6_addresses).  Example:

```json
{
	"default_acl": ["127.0.0.1", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16", "::1/128", "fd00::/8", "169.254.0.0/16", "fe80::/10"]
}
```

See [Access Control Lists](#access-control-lists) below for more details.

## blacklist

The `blacklist` property allows you to specify a list of IPs or IP ranges which are blacklisted.  Meaning, all requests from these IPs are immediately rejected by the web server (see details below).  The format of the `blacklist` is the same as `default_acl` (see [Access Control Lists](#access-control-lists)).  It defaults to an empty list (i.e. disabled).

To customize it, specify an array of [IPv4](https://en.wikipedia.org/wiki/IPv4) and/or [IPv6](https://en.wikipedia.org/wiki/IPv6) addresses, partials or [CIDR blocks](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).  Example:

```json
{
	"blacklist": ["17.0.0.0/8", "12.0.0.0/8"]
}
```

This example would reject all incoming IP addresses from Apple and AT&T (who own the `17.0.0.0/8` and `12.0.0.0/8` IPv4 blocks, respectively).

When a new incoming connection is established, the socket IP is immediately checked against the blacklist, and if matched, the socket is "hard closed".  This is an early detection and rejection, before the HTTP request even comes in.  In this case a HTTP response isn't sent back (as the socket is simply slammed shut).  However, if you are using a load balancer or proxy, the user's true IP address might not be known until later on in the request cycle, once the HTTP headers are read in.  At that point all the user's IPs are checked against the blacklist again, and if any of them match, a `HTTP 403 Forbidden` response is sent back to the client.

## whitelist

The `whitelist` property allows you to specify a list of IPs or IP ranges which are whitelisted.  Meaning, all requests must originate from these IPs, or else they are immediately rejected by the web server (see details below).  The format of the `whitelist` is the same as `default_acl` (see [Access Control Lists](#access-control-lists)).  It defaults to an empty list (i.e. disabled).

To customize it, specify an array of [IPv4](https://en.wikipedia.org/wiki/IPv4) and/or [IPv6](https://en.wikipedia.org/wiki/IPv6) addresses, partials or [CIDR blocks](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).  Example:

```json
{
	"whitelist": ["17.0.0.0/8", "12.0.0.0/8"]
}
```

This example would reject all incoming IP addresses **unless* they were from Apple and AT&T (who own the `17.0.0.0/8` and `12.0.0.0/8` IPv4 blocks, respectively).

When a new incoming connection is established, the socket IP is immediately checked against the whitelist, and if it doesn't match, the socket is "hard closed".  This is an early detection and rejection, before the HTTP request even comes in.  In this case a HTTP response isn't sent back (as the socket is simply slammed shut).  However, if you are using a load balancer or proxy, the user's true IP address might not be known until later on in the request cycle, once the HTTP headers are read in.  At that point all the user's IPs are checked against the whitelist again, and **any of them do not match**, a `HTTP 403 Forbidden` response is sent back to the client.

## allow_hosts

The `allow_hosts` property allows you to specify a limited set of hosts to allow for incoming requests.  Specifically, this matches the incoming HTTP `Host` request header, or SNI (TLS handshake) host for HTTPS, and the value must match at least one entry in the array (case-insensitive).  For example, if you are hosting your application behind a domain name, you may want to restrict incoming requests so that they must explicitly point to your domain name.  Here is how to set this up:

```json
	"allow_hosts": ["mydomain.com"]
```

In the above example, only requests to `mydomain.com` would be allowed.  All other domains or IP addresses in the URL would be rejected with a `HTTP 403 Forbidden` error (or in the case of SNI / TLS handshake the socket is simply closed).  Include multiple entries in the array for things like subdomains:

```json
	"allow_hosts": ["mydomain.com", "www.mydomain.com"]
```

If the `allow_hosts` array is empty or omitted entirely, all hosts are allowed.  This is the default behavior.

## rewrites

If you need to rewrite certain incoming URLs on-the-fly, you can define rules in the `rewrites` object.  The basic format is as follows: keys are regular expressions matched on incoming URI paths, and the values are the substitution strings to use as replacements.  Here is a simple example:

```json
{
	"rewrites": {
		"^/rewrite/me": "/target/path"
	}
}
```

This would match any incoming URI paths that start with `/rewrite/me` and replace that section of the path with `/target/path`.  So for example a full URI path of `/rewrite/me/please?foo=bar` would rewrite to `/target/path/please?foo=bar`.  Note that the suffix after the match was copied over, as well as the query string.  Rewriting happens very early in the request cycle before any other processing occurs, including URI filters, method handers and URI handlers, so they all see the final transformed URI, and not the original.

Since URIs are matched using regular expressions, you can define capturing groups and refer to them in the target substitution string, using the standard `$1`, `$2`, `$3` syntax.  Example:

```json
{
	"rewrites": {
		"^/rewrite/me(.*)$": "/target/path?oldpath=$1"
	}
}
```

This example would grab everything after `/rewrite/me` and store it in a capture group, which is then expanded into the replacement string using the `$1` macro.

For even more control over your rewrites, you can specify them using an advanced syntax.  Instead of the target path string, set the value to an object containing the following:

| Property Name | Type | Description |
|---------------|------|-------------|
| `url` | String | The target URI replacement string. |
| `headers` | Object | Optionally insert custom headers into the incoming request. |
| `last` | Boolean | Set this to `true` to ensure no futher rewrites happen on the request. |

Here is an example showing an advanced configuration:

```json
{
	"rewrites": {
		"^/rewrite/me": {
			"url": "/target/path",
			"headers": { "X-Rewritten": "Yes" },
			"last": true
		}
	}
}
```

A URI may be rewritten multiple times if it matches multiple rules, which are applied in the order which they appear in your configuration.  You can specify a `last` property to ensure that rule matching stops when the specified rule matches a request.

You can use the `headers` property to insert custom HTTP headers into the request.  These will be accessible by downstream URI handlers, and they will also be logged if [log_requests](#log_requests) is enabled.

## redirects

If you need to redirect certain incoming requests to external URLs, you can define rules in the `redirects` object.  When matched, these will interrupt the current request and return a redirect response to the client.  The basic format is as follows: keys are regular expressions matched on incoming URI paths, and the values are the fully-qualified URLs to redirect to.  Here is a simple example:

```json
{
	"redirects": {
		"^/redirect/me": "https://disney.com/"
	}
}
```

This would match any incoming URI paths that start with `/redirect/me` and redirect the user to `https://disney.com/`.  Redirects are matched during the URI handling portion of the request cycle, so things like requests and URI filters have already been handled.  URI request handlers are not invoked if a redirect occurs.

Since URIs are matched using regular expressions, you can define capturing groups and refer to them in the target redirect URL, using the standard `$1`, `$2`, `$3` syntax.  Example:

```json
{
	"redirects": {
		"^/github/(.*)$": "https://github.com/jhuckaby/$1"
	}
}
```

This example would grab everything after `/github/` and store it in a capture group, which is then expanded into the replacement string using the `$1` macro.  For example, `/github/pixl-server-web` would redirect to `https://github.com/jhuckaby/pixl-server-web`.

For even more control over your redirects, you can specify them using an advanced syntax.  Instead of the target URL, set the value to an object containing the following:

| Property Name | Type | Description |
|---------------|------|-------------|
| `url` | String | The fully qualified URL to redirect to. |
| `headers` | Object | Optionally insert custom headers into the incoming request. |
| `status` | String | The HTTP response code and status to use, default is `302 Found`. |

Here is an example showing an advanced configuration:

```json
{
	"redirects": {
		"^/redirect/me": {
			"url": "https://disney.com/",
			"headers": { "X-Redirected": "Yes" },
			"status": "301 Moved Permanently"
		}
	}
}
```

You can use the `headers` property to insert custom HTTP headers into the redirect response.  Use the `status` to customize the HTTP response code and status (it defaults to `302 Found`).

## log_requests

This boolean allows you to enable transaction logging in the web server.  It defaults to `false` (disabled).  See [Transaction Logging](#transaction-logging) below for details.

## log_request_details

This boolean adds verbose detail in the transaction log.  It defaults to `false` (disabled).  See [Transaction Logging](#transaction-logging) below for details.

**Note:** This property only has effect if [log_requests](#log_requests) is enabled.

## log_body_max

This property sets the maximum allowed request and response body length that can be logged, when [log_request_details](#log_request_details) is enabled.  It defaults to `32768` (32K).  If the request or response body length exceeds this amount, they will not be included in the transaction log.

**Note:** This property only has effect if [log_request_details](#log_request_details) is enabled.

## regex_log

If [log_requests](#log_requests) is enabled, this allows you to specify a regular expression to match against incoming request URIs.  Only requests that match will be logged.  It defaults to match all URIs (`.+`).  See [Transaction Logging](#transaction-logging) below for details.

## log_perf

This boolean allows you to enable performance threshold logging.  It defaults to `false` (disabled).  See [Performance Threshold Logging](#performance-threshold-logging) below for details.

## perf_threshold_ms

If [log_perf](#log_perf) is enabled, this allows you to specify the request elapsed time threshold in milliseconds.  All requests equal to or longer will be logged.  It defaults to `100` milliseconds.  See [Performance Threshold Logging](#performance-threshold-logging) below for details.

## perf_report

This property allows you to include a complete or partial [Node.js Diagnostic Report](https://nodejs.org/docs/latest/api/report.html) in your [Performance Threshold Log](#performance-threshold-logging).  Specifically, you can set this to an array of report keys to include in the log data.  See [Including Diagnostic Reports](#including-diagnostic-reports) below for details.

## recent_requests

This integer specifies the number of recent requests to provide in the `getStats()` response.  It defaults to `10`.  See [Stats](#stats) below for details.

## max_connections

This integer specifies the maximum number of concurrent connections to allow.  It defaults to `0` (no limit).  If specified and the amount is exceeded, new incoming connections will be denied (socket force-closed without reading any data), and an error logged for each attempt (with error code `maxconns`).

## max_concurrent_requests

This integer specifies the maximum number of concurrent requests to allow.  It defaults to `0` (no limit).  If more than the maximum allowed requests arrive in parallel, additional requests are queued, and processed as soon as slots become available.  Requests are always processed in the order they were received.

The idea here is that you can set [max_connections](#max_connections) to a much higher value, for things like load balancers pre-opening connections or clients using a pool of keep-alive connections, but then only allow your application code to process a smaller amount of requests in parallel.  For example:

```json
{
	"max_connections": 2048,
	"max_concurrent_requests": 64
}
```

This would allow up to 2,048 concurrent connections (sockets) to be open at any given time, but only allow 64 active requests to run in parallel.  If more than 64 requests came in at once, the remainder would be queued up, and processed as soon as other requests completed.

## max_queue_length

The `max_queue_length` property is designed to work in conjunction with [max_concurrent_requests](#max_concurrent_requests).  It specifies the maximum number of requests to allow in the queue, before rejecting new requests.  It defaults to `0` (infinite).  If the number of enqueued requests reaches this limit, then new incoming requests are immediately aborted with a `HTTP 429 Too Many Requests` response.  An error is also logged with a `429` code in this case.  Example error log entry:

```
[1587614950.774][2020-04-22 21:09:10][joe16.local][93307][WebServer][error][429][Queue is maxed out (100 pending reqs), denying request from: 127.0.0.1][{"ips":["127.0.0.1"],"uri":"/sleep?ms=500","headers":{"accept-encoding":"gzip, deflate, br","user-agent":"Overflow Test Agent 1.0","host":"localhost:3012","connection":"keep-alive"},"pending":100,"active":1024,"sockets":1175}]
```

The error log data column includes some additional information including the total requests pending, the number of concurrent active requests, and the number of open sockets.

## max_queue_active

The `max_queue_active` property is designed to work in conjunction with [max_connections](#max_connections), [max_concurrent_requests](#max_concurrent_requests) and [max_queue_length](#max_queue_length).  It sets an upper maximum for number of concurrent *active* requests in the queue (i.e. concurrent active requests), before new ones are immediately rejected with an `HTTP 429` response, without actually queueing up.  This defaults to `0` (disabled), which means there is no limit imposed at the queue level.

The only reason you'd ever need to set this property is to handle a request overload situation by rejecting requests out of the queue via `HTTP 429`, rather than blocking them at the socket level (hard close), and also not allowing them to queue up (potential lag situation).  Example configuration:

```json
{
	"max_connections": 8192,
	"max_concurrent_requests": 1024,
	"max_queue_length": 1024,
	"max_queue_active": 1024
}
```

The idea here is that pixl-server-web will allow up to 1,024 concurrent requests, but additional requests beyond the maximum are still accepted and responded to with a nice `HTTP 429` response, rather than the alternatives (i.e. allowing requests to queue up, possibly introducing unwanted lag, or performing a hard socket close).  This works as long as the total concurrent sockets do not exceed the upper limit (8,192 in this case).

With both `max_queue_length` and `max_queue_active` set to non-zero values, the first limit reached aborts the request.

## queue_skip_uri_match

The `queue_skip_uri_match` property is designed to work in conjunction with [max_concurrent_requests](#max_concurrent_requests).  It allows you to specify a URI pattern match that will always skip over the queue and be processed immediately, regardless of limits.  Using this feature you can allow things like health checks (possibly from a load balancer) to always be serviced, even during an overload situation.  Example use:

```json
{
	"queue_skip_uri_match": "^/server-status"
}
```

This property defaults to `false` (disabled).

## clean_headers

This boolean enables HTTP response header cleansing.  When set to `true` it will strip all illegal characters from your response header values, which otherwise could cause Node.js to crash.  It defaults to `false`.  The regular expression it uses is `/([\x7F-\xFF\x00-\x1F\u00FF-\uFFFF])/g`.

## log_socket_errors

This boolean enables logging socket related errors, specifically sockets being closed unexpectedly (i.e. client closed socket, or some network error caused socket to abort).  This defaults to `true`, meaning these will be logged as errors.  If this generates too much log noise for your production stack, you can set the configuration property to `false`, which will only log a level 9 debug event.  Example:

```json
{
	"log_socket_errors": false
}
```

Example error log entry:

```
[1545121086.42][2018-12-18 00:18:06][myserver01.mycompany.com][29801][WebServer][error][socket][Socket closed unexpectedly: c43593][][][{"id":"c43593","proto":"http","port":80,"time_start":1545120267519,"num_requests":886,"bytes_in":652041,"bytes_out":1307291,"total_elapsed":818901,"url":"http://mycompany.com/example/url","ips":["1.1.1.1","2.2.2.2"]}]
```

## full_uri_match

When this boolean is set to `true`, [Custom URI Handlers](#custom-uri-handlers) will match against the *full* incoming URI, including the query string.  By default this is disabled, meaning URIs are only matched using their path.  Example:

```json
{
	"full_uri_match": true
}
```

## flatten_query

By default, we use the Node.js core [Query String](https://nodejs.org/api/querystring.html) module to parse query strings.  This module handles duplicate query params by converting them to arrays.  For example, an incoming URI such as `/something?foo=bar1&foo=bar2&name=joe` would produce the following `args.query` object:

```json
{
	"foo": ["bar1", "bar2"],
	"name": "joe"
}
```

However, if you set `flatten_query` to `true` in your configuration, the web server will "flatten" query string parameters, so that duplicate keys will be combined into one, with the latter prevailing.  Example:

```json
{
	"foo": "bar2",
	"name": "joe"
}
```

## req_max_dump_enabled

When this boolean is set to `true`, the [Request Max Dump](#request-max-dump) system is enabled.  This will produce a JSON dump file when the web server is maxed out on requests.

## req_max_dump_dir

When the [Request Max Dump](#request-max-dump) system is enabled, the `req_max_dump_dir` property sets the directory path where JSON dump files are dropped.  The directory will be created if needed.

## req_max_dump_debounce

When the [Request Max Dump](#request-max-dump) system is enabled, the `req_max_dump_debounce` property sets how many seconds should elapse between dumps, as to not overwhelm the filesystem.

## public_ip_offset

This controls how [args.ip](#argsip) is chosen from the list of IP addresses in [args.ips](#argsips) for each incoming request.  By default, the client IP is chosen by scanning the list from left to right, and selecting the first non-private IP.  However, [modern wisdom](https://adam-p.ca/blog/2022/03/x-forwarded-for/) suggests that alternate selection logic may be more desirable to find the true public IP.

By setting `public_ip_offset` to an integer value, you can select *exactly* which IP to select from the list.  Use negative numbers to select IP address from the *end* (right side) of the list.  Here are the recommended values:

| Offset | Description |
|--------|-------------|
| `0` | The default value.  Allow the server to select the public IP automatically. |
| `-1` | Always select the *last* IP in the list (i.e. the TCP socket IP).  Use this mode if your server is connected to the internet directly. |
| `-2` | Always select the *second-to-last* IP in the list.  Use this mode if you have a single proxy device in front of your server (e.g. a load balancer). |
| `-3` | Always select the *third-to-last* IP in the list.  Use this mode if you have two proxy devices in front of your server (e.g. a load balancer and CDN / cache). |

## legacy_callback_support

This adds support for legacy applications, which require JSONP callback-style API responses, as well as extremely old HTML-wrapped IFRAME API responses.  It defaults to disabled.  It is **highly recommended** that you *leave this disabled* for all modern applications, as it prevents a classic [XSS reflection attack](https://owasp.org/www-community/attacks/xss/#reflected-xss-attacks) on your APIs:

```json
{
	"legacy_callback_support": false
}
```

Only enable this if you are supporting a legacy application which is hosted on a private, trusted network.

## startup_message

When set to `true` and running in debug or foreground mode (i.e. `--debug` or `--foreground` CLI flags on startup), this will emit a message to the console on startup detailing all the socket listeners, ports, and URL endpoints you can hit.  Example conaole message:

```
Web Server Listeners:

	Listening for HTTP on port 3020, network '::' (all)
	--> http://192.168.3.25:3020/

	Listening for HTTPS on port 3021, network '::' (all)
	--> https://192.168.3.25:3021/
```

## debug_ttl

When set to `true` and running in debug mode (i.e. `--debug` CLI flag on startup), this will override the value of [static_ttl](#static_ttl) with `0`.  Useful for local development, i.e. reloading your web app in the browser.

This feature defaults to `false` (disabled).

## debug_bind_local

When set to `true` and running in debug mode (i.e. `--debug` CLI flag on startup), this will override the value of [bind_address](#bind_address) with `localhost`.  This will keep your local development environment secure, and not exposed to the network.  To override this behavior, add an `--expose` CLI flag or explicitly set the `bind_address` in your config.

This feature defaults to `false` (disabled).

## chaos

Use the `chaos` feature to introduce optional and random fault injection into your web requests.  Used for testing purposes, this feature can introduce a random delay on every request, and also hijack requests and inject random error responses based on probabilities you specify.  Here is how to use it:

```json
"chaos": { 
	"enabled": true, 
	"uri": ".+", 
	"delay": { 
		"min":0, 
		"max":2000 
	}, 
	"errors": { 
		"503 Service Unavailable": 0.1 
	}, 
	"headers": {
		"Retry-After": 10
	} 
}
```

Set the `chaos.enabled` flag to `true` to enable fault injection.  By default, all URIs will be affected, unless you specify a `chaos.uri` (regular expression) to limit the requests.  Set `chaos.delay.min` and `chaos.delay.max` to the range you want to delay requests (in milliseconds).  Fill the `chaos.errors` object the HTTP repsonse codes (and status messages) you want to see, and how often.  The values are interpreted as probabilities from `0.0` (never) to `1.0` (always).  In the above example, the `HTTP 503` error code will be injected approximately 10% of the time.  When errors are injected, you can include additional response headers in the `chaos.headers` object.

## auth

Use the `auth` feature to protect URI patterns behind HTTP authentication challenges.  Each key in the `auth` object should be a URI regular expression, and each value should be an auth definition.  Here is an example:

```json
"auth": {
	"^/protected": {
		"enabled": true,
		"type": "basic",
		"realm": "Secret Area",
		"username": "foo",
		"password": "bar"
	}
}
```

Set `auth.URI.enabled` to `true` to enable auth for that URI pattern.  Set `auth.URI.type` to `basic` to enable HTTP Basic Auth.  Currently, `basic` is the only supported authentication scheme.  The server will challenge unauthorized clients with the configured `auth.URI.realm`, and then compare `auth.URI.username` and `auth.URI.password` against the credentials provided by the client.

The URI match key (e.g. `^/protected`) is treated as a regular expression and is evaluated as a request URI filter.  If credentials are missing or invalid, the request is rejected with `HTTP 401 Unauthorized`.

## https

This boolean allows you to enable HTTPS (SSL) support in the web server.  It defaults to `false`.  Note that you must also set `https_port`, and possibly `https_cert_file` and `https_key_file` for this to work.

The SSL certificate files are automatically reloaded if changed on disk.  This is done without a server restart.

## https_port

If HTTPS mode is enabled, this is the port to listen on for secure requests.  The standard HTTPS port is 443.

## https_alt_ports

If you would like to have the server listen on additional HTTPS ports, add them here as an array.  Example:

```json
{
	"https_port": 443,
	"https_alt_ports": [ 9000, 9001 ]
}
```

## https_cert_file

If HTTPS mode is enabled, this should point to your SSL certificate file on disk.  The certificate file typically has a `.crt` filename extension, or possibly `cert.pem` if using [Let's Encrypt](https://letsencrypt.org/).

## https_key_file

If HTTPS mode is enabled, this should point to your SSL private key file on disk.  The key file typically has a `.key` filename extension, or possibly `privkey.pem` if using [Let's Encrypt](https://letsencrypt.org/).

## https_ca_file

If HTTPS mode is enabled, this should point to your SSL chain file on disk.  This is optional, as some SSL certificates do not provide one.  If using [Let's Encrypt](https://letsencrypt.org/) this file will be named `chain.pem`.

## https_force

If HTTPS mode is enabled, you can set this param to boolean `true` to force all requests to be HTTPS.  Meaning, if someone attempts a non-secure plain HTTP request to any URI, their client will be redirected to an equivalent HTTPS URI.

## https_header_detect

Your network architecture may have a proxy server or load balancer sitting in front of the web server, and performing all HTTPS/SSL encryption for you.  Usually, these devices inject some kind of HTTP request header into the back-end web server request, so you can "detect" a front-end HTTPS proxy request in your code.  For example, Amazon AWS load balancers inject the following HTTP request header into all back-end requests:

```
X-Forwarded-Proto: https
```

The `https_header_detect` property allows you to define any number of header regular expression matches, that will "pseudo-enable" SSL mode in the web server.  Meaning, the `args.request.headers.ssl` property will be set to `true`, and calls to `server.getSelfURL()` will have a `https://` prefix.  Here is an example configuration, which detects many commonly used headers:

```json
{
	"https_header_detect": {
		"Front-End-Https": "^on$",
		"X-Url-Scheme": "^https$",
		"X-Forwarded-Protocol": "^https$",
		"X-Forwarded-Proto": "^https$",
		"X-Forwarded-Ssl": "^on$"
	}
}
```

Note that these are matched using logical OR, so only one of them needs to match to enable SSL mode.  The values are interpreted as regular expressions, in case you need to match more than one header value.

## https_timeout

This sets the idle socket timeout for all incoming HTTPS requests.  If omitted, the Node.js default is 2 minutes.  Please specify your value in seconds.

## https_bind_address

Optionally specify an exact local IP address to bind the HTTPS listener to.  By default this uses the value of [bind_address](#bind_address), but you can bind them differently using this property.  Example:

```json
{
	"bind_address": "127.0.0.1",
	"https_bind_address": "0.0.0.0"
}
```

This example would cause the server to only listen on localhost for plain HTTP traffic, but listen on *all* network interfaces for HTTPS traffic.

## https_cert_poll_ms

The `https_cert_poll_ms` property allows you to customize the polling interval for monitoring the SSL cert files on disk.  The value is in milliseconds, and defaults to `60000` (1 minute).  This is used to poll the SSL cert files on disk to see if they changed (i.e. cert renewal).  If so, they are automatically reloaded without restarting the server.

# Custom URI Handlers

You can attach your own handler methods for intercepting and responding to certain incoming URIs.  So for example, instead of the URI `/api/add_user` looking for a static file on disk, you can have the web server invoke your own function for handling it, and sending a custom response.  

To do this, call the `addURIHandler()` method and pass in the URI string, a name (for logging), and a callback function:

```js
server.WebServer.addURIHandler( '/my/custom/uri', 'Custom Name', function(args, callback) {
	// custom request handler for our URI
	callback( 
		"200 OK", 
		{ 'Content-Type': "text/html" }, 
		"Hello this is custom content!\n" 
	);
} );
```

URIs must match exactly (sans the query string), and the case is sensitive.  If you need to implement something more complicated, such as a regular expression match, you can pass one of these in as well.  Example:

```js
server.WebServer.addURIHandler( /^\/custom\/match\/$/i, 'Custom2', function(args, callback) {...} );
```

Your handler function is passed exactly two arguments.  First, an `args` object containing all kinds of useful information about the request (see [args](#args) below), and a callback function that you must call when the request is complete and you want to send a response.

If you specified a regular expression with parenthesis groups for the URI, the matches array will be included in the `args` object as `args.matches`.  Using this you can extract your matched groups from the URI, for e.g. `/^\/api\/(\w+)/`.

Note that by default, URIs are only matched on their path portion (i.e. sans query string).  To include the query string in URI matches, set the [full_uri_match](#full_uri_match) configuration property to `true`.

## Access Control Lists

If you want to restrict access to certain URI handlers, you can specify an [ACL](https://en.wikipedia.org/wiki/Access_control_list) which represents a list of IP address ranges to allow.  To use the [default ACL](#default_acl), simply pass `true` as the 3rd argument to `addURIHandler()`, just before your callback.  This flags the URI as private.  Example:

```js
server.WebServer.addURIHandler( /^\/private/, "Private Admin Area", true, function(args, callback) {
	// request allowed
	callback( "200 OK", { 'Content-Type': 'text/html' }, "<h1>Access granted!</h1>\n" );
} );
```

This will protect the handler using the *default ACL*, as specified by the [default_acl](#default_acl) configuration parameter.  However, if you want to specify a *custom* ACL per handler, simply replace the `true` argument with an array of [IPv4](https://en.wikipedia.org/wiki/IPv4) and/or [IPv6](https://en.wikipedia.org/wiki/IPv6) addresses, partials or [CIDR blocks](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).  Example:

```js
server.WebServer.addURIHandler( /^\/secret/, "Super Secret Area", ['10.0.0.0/8', 'fd00::/8'], function(args, callback) {
	// request allowed
	callback( "200 OK", { 'Content-Type': 'text/html' }, "<h1>Access granted!</h1>\n" );
} );
```

This would only allow requests from either `10.0.0.0/8` (IPv4) or `fd00::/8` (IPv6).

The ACL code scans *all* the IP addresses from the client, including the socket IP and any passed as part of HTTP headers (populated by load balancers, proxies, etc.).  See [args.ips](#argsips) for more details on this.  All the IPs must pass the ACL test in order for the request to be allowed through to your handler.

If a request is rejected, your handler isn't even called.  Instead, a standard `HTTP 403 Forbidden` response is sent to the client, and an error is logged.

## Internal File Redirects

To setup an internal file redirect, you can substitute the final callback function for a string, pointing to a fully-qualified filesystem path.  The target file will be served up in place of the original URI.  You can also combine this with an ACL for extra protection for private files.  Example:

```js
server.WebServer.addURIHandler( /^\/secret.txt$/, "Special Secrets", true, '/private/myapp/docs/secret.txt' );
```

Note that the `Content-Type` response header is automatically set based on the target file you are redirecting to.

## Static Directory Handlers

If you would like to host static files in other places besides [htdocs_dir](#htdocs_dir), possibly with different options, then look no further than the `addDirectoryHandler()` method.  This allows you to set up static file handling with a custom base URI, a custom base directory on disk, and apply other options as well.  You can call this method as many times as you like to setup multiple static file directories.  Example:

```js
server.WebServer.addDirectoryHandler( /^\/mycustomdir/, '/var/www/custom' );
```

The above example would catch all incoming requests starting with `/mycustomdir`, and serve up static files inside of the `/var/www/custom` directory on disk (and possibly nested directories as well).  So a URL such as `http://MYSERVER/mycustomdir/foo/file1.txt` would map to the file `/var/www/custom/foo/file1.txt` on disk.

In this case a default TTL is applied to all files via [static_ttl](#static_ttl).  If you would like to customize the TTL for your custom static directory, as well as specify other options, pass in an object as the 3rd argument to `addDirectoryHandler()`.  Example of this:

```js
server.WebServer.addDirectoryHandler( /^\/mycustomdir/, '/var/www/custom', {
	acl: true
	ttl: 3600,
	headers: {
		'X-Custom': '12345'
	}
} );
```

In this example the files would be restricted to client IP addresses matching the [default_acl](#default_acl), and would be served up with a custom TTL of 3600 seconds (specifically, the `Cache-Control` response header would be set to `public, max-age=3600`).  Finally, all static file responses would include the `X-Custom: 12345` header.  Here is a list of the available properties in the options object:

| Property Name | Type | Description |
|---------------|------|-------------|
| `acl` | Boolean | Optionally restrict the static files to an IP-based ACL.  You can set this to Boolean `true` to use the [default_acl](#default_acl), or specify an array of [IPv4](https://en.wikipedia.org/wiki/IPv4) and/or [IPv6](https://en.wikipedia.org/wiki/IPv6) addresses, partials or [CIDR blocks](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). |
| `ttl` | Mixed | Optionally customize the TTL (`Cache-Control` header).  Set this to a number to use the `public, max-age=###` format, or a string to specify the entire header value yourself. |
| `headers` | Object | Optionally include additional HTTP headers with every static response.  Note that you cannot use this to override built-in headers like `Content-Type`, `Content-Length`, `ETag`, and others.  It can only be used to insert unique headers. |

## Sending Responses

There are actually four different ways you can send an HTTP response.  They are all detailed below:

### Standard Response

The first type of response is shown above, and that is passing three arguments to the callback function.  The HTTP response status line (e.g. `200 OK` or `404 File Not Found`), a response headers object containing key/value pairs for any custom headers you want to send back (will be combined with the default ones), and finally the content body.  Example:

```js
callback( 
	"200 OK", 
	{ 'Content-Type': "text/html" }, 
	"Hello this is custom content!\n" 
);
```

The content body can be a string, a [Buffer](https://nodejs.org/api/buffer.html) object, or a [readable stream](https://nodejs.org/api/stream.html#class-streamreadable).

Note that you can omit the status text and just return a code, e.g. `"200"`, and the web server will fill in the text.

### Custom Response

The second type of response is to send content directly to the underlying Node.js server by yourself, using `args.response` (see below).  If you do this, you can pass `true` to the callback function, indicating to the web server that you "handled" the response, and it shouldn't do anything else.  Example:

```js
server.WebServer.addURIHandler( '/my/custom/uri', 'Custom Name', function(args, callback) {
	// send custom raw response
	let response = args.response;
	response.writeHead( 200, "OK", { 'Content-Type': "text/html" } );
	response.write( "Hello this is custom content!\n" );
	response.end();
	
	// indicate we are done, and have handled things ourselves
	callback( true );
} );
```

### JSON Response

The third way is to pass a single object to the callback function, which will be serialized to JSON and sent back as an AJAX style response to the client.  Example:

```js
server.WebServer.addURIHandler( '/my/custom/uri', 'Custom Name', function(args, callback) {
	// send custom JSON response
	callback( {
		Code: 0,
		Description: "Success",
		User: { Name: "Joe", Email: "foo@bar.com" }
	} );
} );
```

This is sent as pure JSON with the Content-Type `application/json`.  The raw HTTP response would look something like this:

```
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 79
Content-Type: application/json
Date: Sun, 05 Apr 2015 20:58:50 GMT
Server: Test 1.0

{"Code":0,"Description":"Success","User":{"Name":"Joe","Email":"foo@bar.com"}}
```

### Non-Response

The fourth and final type of response is a non-response, and this is achieved by passing `false` to the callback function.  This indicates to the web server that your code did *not* handle the request, and it should fall back to looking up a static file on disk.  Example:

```js
server.WebServer.addURIHandler( '/my/custom/uri', 'Custom Name', function(args, callback) {
	// we did not handle the request, so tell the web server to do so
	callback( false );
} );
```

Note that there is currently no logic to fallback to other custom URI handlers.  The only fallback logic, if a handler returns false, is to lookup a static file on disk.

To perform an internal file redirect from inside your URI handler code, set the `internalFile` property of the `args` object to your destination filesystem path, then pass `false` to the callback:

```js
server.WebServer.addURIHandler( '/intredir', "Internal Redirect", true, function(args, callback) {
	// perform internal redirect to custom file
	args.internalFile = '/private/myapp/docs/secret.txt';
	callback(false);
} );
```

## args

Your URI handler function is passed an `args` object containing the following properties:

### args.request

This is a reference to the underlying [Node.js server request](https://nodejs.org/api/http.html#class-httpincomingmessage) object.  From this you have access to things like:

| Property | Description |
|----------|-------------|
| `request.httpVersion` | The version of the HTTP protocol used in the request. |
| `request.headers` | An object containing all the HTTP request headers (lower-cased). | 
| `request.method` | The HTTP method used in the request, e.g. `GET`, `POST`, etc. | 
| `request.url` | The complete URI of the request (sans protocol and hostname). | 
| `request.socket` | A reference to the underlying socket connection for the request. | 

For more detailed documentation on the request object, see Node's [http.IncomingMessage](https://nodejs.org/api/http.html#class-httpincomingmessage).

### args.response

This is a reference to the underlying [Node.js server response](https://nodejs.org/api/http.html#class-httpserverresponse) object.  From this you have access to things like:

| Property / Method() | Description |
|----------|-------------|
| `response.writeHead()` | This writes the HTTP status code, message and headers to the socket. |
| `response.setTimeout()` | This sets a timeout on the response. |
| `response.statusCode` | This sets the HTTP status code, e.g. 200, 404, etc. |
| `response.statusMessage` | This sets the HTTP status message, e.g. OK, File Not Found, etc. |
| `response.setHeader()` | This sets a single header key / value pair in the response. |
| `response.write()` | This writes a chunk of data to the socket. |
| `response.end()` | This indicates that the response has been completely sent. |

For more detailed documentation on the response object, see Node's [http.ServerResponse](https://nodejs.org/api/http.html#class-httpserverresponse).

### args.ip

This will be set to the user's remote IP address.  Generally, it will be set to the *first public IP address* if multiple addresses are provided via proxy HTTP headers and the socket.

Meaning, if the user is sitting behind one or more proxy servers, *or* your web server is behind a load balancer, this will attempt to locate the user's true public (non-private) IP address.  If none is found, it'll just return the first IP address, honoring proxy headers before the socket (which is usually correct).

See [public_ip_offset](https://github.com/jhuckaby/pixl-server-web#public_ip_offset) for details on customizing the behavior of this property.

If you just want the socket IP by itself, you can get it from `args.request.socket.remoteAddress`.

### args.ips

This will be set to an array of *all* the user's remote IP addresses, taking into account the socket IP and various HTTP headers populated by proxies and load balancers, if applicable.  The header address(es) will come first, if applicable, followed by the socket IP at the end.

The following HTTP headers are scanned for IP addresses to build the `args.ips` array:

| Header | Syntax | Description |
|--------|--------|-------------|
| `X-Forwarded-For` | Comma-Separated | The de-facto standard header for identifying the originating IP address of a client connecting through an HTTP proxy or load balancer.  See [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For). |
| `Forwarded-For` | Comma-Separated | Alias for `X-Forwarded-For`. |
| `Forwarded` | Custom | New standard header as defined in [RFC 7239](https://tools.ietf.org/html/rfc7239#section-4), with custom syntax.  See [Forwarded](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Forwarded).
| `X-Forwarded` | Custom | Alias for `Forwarded`. |
| `X-Client-IP` | Single | Non-standard, used by Heroku, etc. |
| `CF-Connecting-IP` | Single | Non-standard, used by CloudFlare. |
| `True-Client-IP` | Single | Non-standard, used by Akamai, CloudFlare, etc. |
| `X-Real-IP` | Single | Non-standard, used by Nginx, FCGI, etc. |
| `X-Cluster-Client-IP` | Single | Non-standard, used by Rackspace, Riverbed, etc. |

### args.query

This will be an object containing key/value pairs from the URL query string, if applicable, parsed via the Node.js core [Query String](https://nodejs.org/api/querystring.html) module.

Duplicate query params become an array.  For example, an incoming URI such as `/something?foo=bar1&foo=bar2&name=joe` would produce the following `args.query` object:

```json
{
	"foo": ["bar1", "bar2"],
	"name": "joe"
}
```

See [flatten_query](#flatten_query) if you would rather duplicate query parameters be flattened (latter prevails).

### args.params

If the request was a HTTP POST, this will contain all the post parameters as key/value pairs.  This will take one of three forms, depending on the request's `Content-Type` header:

#### Standard HTTP POST

If the request Content-Type was one of the standard `application/x-www-form-urlencoded` or `multipart/form-data`, all the key/value pairs from the post data will be parsed, and provided in the `args.params` object.  We use the 3rd party [Formidable](https://www.npmjs.com/package/formidable) module for this work.

#### JSON REST POST

If the request is a "pure" JSON POST, meaning the Content-Type contains `json` or `javascript`, the content body will be parsed as a single JSON string, and the result object placed into `args.params`.

#### Unknown POST

If the Content-Type doesn't match any of the above values, it will simply be treated as a plain binary data, and a [Buffer](https://nodejs.org/api/buffer.html) will be placed into `args.params.raw`.

### args.files

If the request was a HTTP POST and contained any file uploads, they will be accessible through this property.  Files are saved to a temp directory and can be moved to a custom location, or loaded directly.  They will be keyed by the POST parameter name, and the value will be an object containing the following properties:

| Property | Description |
|----------|-------------|
| `size` | The size of the uploaded file in bytes. |
| `path` | The path to the temp file on disk containing the file contents. |
| `name` | The filename of the file as provided by the client. |
| `type` | The mime type of the file, according to the client. |
| `lastModifiedDate` | A date object containing the last mod date of the file, if available. |

For more details, please see the documentation on the [Formidable.File](https://github.com/felixge/node-formidable#formidablefile) object.

All temp files are automatically deleted at the end of the request.

### args.cookies

This is an object parsed from the incoming `Cookie` HTTP header, if present.  The contents will be key/value pairs for each semicolon-separated cookie provided.  For example, if the client sent in a `session_id` cookie, it could be accessed like this:

```js
let session_id = args.cookies['session_id'];
```

### args.perf

This is a reference to a [pixl-perf](https://www.github.com/jhuckaby/pixl-perf) object, which is used internally by the web server to track performance metrics for the request.  The metrics may be logged at the end of each request (see [Transaction Logging](#transaction-logging) below) and included in the stats (see [Stats](#stats) below).

### args.server

This is a reference to the pixl-server object which handled the request.

### args.id

This is an internal ID string used by the server to track and log individual requests.

### args.setCookie

A utility function used to serialize cookies into the proper format, and set or append them to the `Set-Cookie` response header.  It accepts a name, a value, and an optional set of options.  Example use:

```js
args.setCookie( 'session', 'ABDEF01234567890', { path: '/', maxAge: 86400, secure: true, httpOnly: true, sameSite: 'Lax' } );
```

## Request Filters

Filters allow you to preprocess a request, before any handlers get their hands on it.  They can pass data through, manipulate it, or even interrupt and abort requests.  Filters are attached to particular URIs or URI patterns, and multiple may be applied to one request, depending on your rules.  They can be asynchronous, and can also pass data between one another if desired.

You can attach your own filter methods for intercepting and responding to certain incoming URIs.  So for example, let's say we want to filter the URI `/api/add_user` before the handler gets it, and inject some custom data.  To do this, call the `addURIFilter()` method and pass in the URI string, a name (for logging), and a callback function:

```js
server.WebServer.addURIFilter( /.+/, "My Filter", function(args, callback) {
	// add a nugget into request query
	args.query.filter_nugget = 42;
	
	// add a custom response header too
	args.response.setHeader('X-Filtered', "4242");
	
	callback(false); // passthru
} );
```

So here we are injecting `filter_nugget` into the `args.query` object, which is preserved and passed down to other filters and handlers.  Also, we are adding a `X-Filtered` header to the response (whoever ends up sending it).  Finally, we call the `callback` function passing `false`, which means to pass the request through to other filters and/or handlers (see below for more on this).

URI strings must match exactly (sans the query string), and the case is sensitive.  If you need to match something more complicated, such as a regular expression, you can pass one of these in place of the URI string.  Example:

```js
server.WebServer.addURIFilter( /^\/custom\/match\/$/i, 'Custom2', function(args, callback) {...} );
```

Your filter handler function is passed exactly two arguments.  First, an `args` object containing all kinds of useful information about the request (see [args](#args) above), and a callback function that you must invoke when the filter is complete, and you want to either allow the request to continue, or interrupt it and send your own response.

As shown above, passing `false` to the callback means to pass the request through to downstream filters and handlers.  If you want to intercept and abort the request, and send your own response preventing any further processing, you can pass a [Standard Response](#standard-response) to the callback, i.e. send exactly 3 arguments, an HTTP response code, HTTP response headers, and the response body (or `null`):

```js
server.WebServer.addURIFilter( /.+/, "Reject All", function(args, callback) {
	// intercept everything and send our own custom response
	callback(
		"418 I'm a teapot", 
		{ 'X-Filtered': 42 },
		null
	);
} );
```

This will intercept and abort all requests, sending back a `HTTP 418` error.

To pass data between filters and potentially handlers, simply add properties into the `args` object.  This object is preserved for the lifetime of the request, and the same object reference is passed to all filters and handlers.  Just be careful of namespace collisions with existing properties in the object.  See [args](#args) above for details.

# Transaction Logging

In addition to the standard debug logging in [pixl-server](https://github.com/jhuckaby/pixl-server), the web server component can also log each request as a `transaction`.  This is an optional feature which is disabled by default.  To enable it, set the [log_requests](#log_requests) configuration property to `true`.  The pixl-server log will then include a `transaction` row for every completed web request.  Example:

```
[1466210619.37][2016/06/17 17:43:39][joeretina.local][WebServer][transaction][HTTP 200 OK][/server-status?pretty=1][{"id":"r4","proto":"http","ips":["::ffff:127.0.0.1"],"host":"127.0.0.1:3012","ua":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/601.6.17 (KHTML, like Gecko) Version/9.1.1 Safari/601.6.17","perf":{"scale":1000,"perf":{"total":10.266,"read":0.256,"process":1.077,"write":7.198},"counters":{"bytes_in":587,"bytes_out":431,"num_requests":1}}}]
```

The log columns are configurable in pixl-server, but are typically the following:

| Column | Name | Description |
|--------|------|-------------|
| 1 | `hires_epoch` | Epoch date/time, including milliseconds (floating point). |
| 2 | `date` | Human-readable date/time, in the local server timezone. |
| 3 | `hostname` | The hostname of the server. |
| 4 | `component` | The server component name (`WebServer`). |
| 5 | `category` | The category of the log entry (`transaction`). |
| 6 | `code` | The HTTP response code and message, e.g. `HTTP 200 OK`. |
| 7 | `msg` | The URI of the request. |
| 8 | `data` | A JSON document containing data about the request. |

The `data` column is a JSON document containing various bits of additional information about the request.  Here is a formatted example:

```json
{
	"id": "r4",
	"proto": "http",
	"ip": "::ffff:127.0.0.1",
	"ips": [
		"::ffff:127.0.0.1"
	],
	"port": 3012,
	"socket": "c13",
	"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/601.6.17 (KHTML, like Gecko) Version/9.1.1 Safari/601.6.17",
	"host": "localhost",
	"perf": {
		"scale": 1000,
		"perf": {
			"total": 8.041,
			"read": 0.077,
			"process": 1.315,
			"write": 5.451
		},
		"counters": {
			"bytes_in": 587,
			"bytes_out": 639,
			"num_requests": 1
		}
	}
}
```

Here are descriptions of the data JSON properties:

| Property | Type | Description |
|----------|------|-------------|
| `id` | String | The internal ID for the request. |
| `method` | String | The HTTP method for the request, e.g. `GET`, `POST`. |
| `proto` | String | The protocol of the request (`http` or `https`). |
| `ip` | String | The first non-internal IP address (see [args.ip](#argsip)). |
| `ips` | Array | All the client IPs as an array (includes those from proxy headers). |
| `port` | Number | Which port number the request came in on. |
| `socket` | String | The unique ID of the socket which served the request. |
| `ua` | String | The `User-Agent` string from the request headers. |
| `host` | String | The hostname from the request URL. |
| `perf` | Object | Performance metrics, see below. |

The `perf` object contains performance metrics for the request, as returned from the [pixl-perf](https://www.github.com/jhuckaby/pixl-perf) module.  It includes a `scale` property denoting that all the metrics are displayed in milliseconds (i.e. `1000`).  The metrics themselves are in the `perf` object, and counters such as the number of bytes in/out are in the `counters` object.

If you only want to log *some* requests, but not all of them, you can specify a regular expression in the [regex_log](#regex_log) configuration property, which is matched against the incoming request URIs.  Example:

```json
{
	"regex_log": "^/my/special/path"
}
```

## Request Detail Logging

If you set both the [log_requests](#log_requests) and [log_request_details](#log_request_details) configuration properties to `true`, pixl-server will include verbose details in the transaction logs, specifically in the JSON-formatted `data` column.  It will include the raw request and raw response (if in text format), and extra details about both the request and the response.  Example of the `data` column from the log, pretty-printed:

```json
{
	"id": "r10",
	"method": "POST",
	"proto": "http",
	"ip": "::1",
	"ips": [
		"::1"
	],
	"port": 3012,
	"socket": "c8",
	"perf": {
		"scale": 1000,
		"perf": {
			"total": 22.689,
			"queue": 0.261,
			"read": 15.176,
			"process": 1.791,
			"encode": 1.281,
			"write": 1.159
		},
		"counters": {
			"bytes_in": 975133,
			"bytes_out": 413,
			"num_requests": 1
		}
	},
	"files": {
		"file1": {
			"path": "/var/folders/11/r_0sz6s13cx1jn68l4m90zfr0000gn/T/f92cd259263698f0e19581400.LBM",
			"type": "application/octet-stream",
			"name": "V04.LBM",
			"size": 318742,
			"mtime": "2024-03-18T20:45:01.328Z"
		}
	},
	"headers": {
		"host": "localhost:3012",
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"sec-fetch-site": "same-origin",
		"accept-language": "en-US,en;q=0.9",
		"accept-encoding": "gzip, deflate",
		"sec-fetch-mode": "navigate",
		"content-type": "multipart/form-data; boundary=----WebKitFormBoundaryAzquNdwdvTjj9ArR",
		"origin": "http://localhost:3012",
		"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
		"referer": "http://localhost:3012/upload.html",
		"upgrade-insecure-requests": "1",
		"content-length": "319132",
		"connection": "keep-alive",
		"sec-fetch-dest": "document"
	},
	"cookies": {},
	"query": {
		"pretty": "1"
	},
	"params": {
		"key1": "value1",
		"key2": "value2"
	},
	"response": {
		"code": 200,
		"status": "OK",
		"headers": {
			"content-type": "application/json",
			"x-joetest": "9876",
			"server": "Test Server 1.0",
			"content-length": "261",
			"content-encoding": "gzip"
		},
		"raw": "{\n\t\"code\": 0,\n\t\"query\": {\n\t\t\"pretty\": \"1\"\n\t},\n\t\"params\": {\n\t\t\"key1\": \"value1\",\n\t\t\"key2\": \"value2\"\n\t},\n\t\"cookies\": {},\n\t\"files\": {\n\t\t\"file1\": {\n\t\t\t\"path\": \"/var/folders/11/r_0sz6s13cx1jn68l4m90zfr0000gn/T/f92cd259263698f0e19581400.LBM\",\n\t\t\t\"type\": \"application/octet-stream\",\n\t\t\t\"name\": \"V04.LBM\",\n\t\t\t\"size\": 318742,\n\t\t\t\"mtime\": \"2024-03-18T20:45:01.328Z\"\n\t\t}\n\t}\n}\n"
	}
}
```

As you can see, in addition to all the information logged with [log_requests](#log_requests), the `data` column now includes even more detail.  Here is the full list of all JSON properties and their descriptions, logged with [log_request_details](#log_request_details) enabled:

| Property | Type | Description |
|----------|------|-------------|
| `id` | String | The internal ID for the request. |
| `method` | String | The HTTP method for the request, e.g. `GET`, `POST`. |
| `proto` | String | The protocol of the request (`http` or `https`). |
| `ip` | String | The first non-internal IP address (see [args.ip](#argsip)). |
| `ips` | Array | All the client IPs as an array (includes those from proxy headers). |
| `port` | Number | Which port number the request came in on. |
| `socket` | String | The unique ID of the socket which served the request. |
| `perf` | Object | Performance metrics, in [pixl-perf](https://github.com/jhuckaby/pixl-perf) format. |
| `files` | Object | If applicable, metadata about all file uploads (file names, sizes, types, and dates). |
| `headers` | Object | All the HTTP request headers in key/value format (lower-cased keys). |
| `cookies` | Object | Cookies from the request, parsed and in key/value form. |
| `query` | Object | The query string from the request URL parsed into key/value pairs. |
| `params` | Object | Key/value pairs from the request, i.e. parsed JSON or form POST data. |
| `params.raw` | String | If applicable, the raw request body as a UTF-8 string (see below). |
| `response` | Object | Details about the HTTP response sent to the client. |
| `response.code` | Number | The HTTP response code (e.g. `200`). |
| `response.status` | String | The HTTP response status (e.g. `OK`). |
| `response.headers` | Object | All the HTTP response headers sent to the client (lower-cased keys). |
| `response.raw` | String | If applicable, the raw response body as a UTF-8 string (see below). |

The raw request and response content will only be logged in certain cases:

- If the request was a JSON POST, then the parsed JSON document will be in the `params` object.
- If the request was a non-JSON POST, but the content is recognized to be text, then the raw request body will be in `params.raw` as a UTF-8 string.
- If the request was a form post, then the key/value pairs will be in the `params` object.
- If the request contained file uploads, they will be summarized in the `files` object (see above for example).
- If the response is recognized as text, it will be included in `response.raw` as a UTF-8 string.
- If the response is non-text (binary), the raw content will not be logged.
- If the response is pre-compressed by application code, it will not be logged.
- If the response is a stream, it will not be logged.

## Performance Threshold Logging

In addition to [Transaction Logging](#transaction-logging), pixl-server-web can also log performance metrics for certain requests, if the total request elapsed time meets or exceeds a custom threshold.  This allows you to log only "slow" requests, i.e. those possibly requiring investigation.  This is an optional feature which is disabled by default.  To enable it, set the [log_perf](#log_perf) configuration property to `true`, and then set the [perf_threshold_ms](#perf_threshold_ms) property to the desired logging threshold in milliseconds.  Example:

```json
{
	"log_perf": true,
	"perf_threshold_ms": 100
}
```

This would log all requests that took 100ms or longer.  Here is an example performance log row for such a request:

```
[1654144635.900786][2022-06-01 21:37:15][joemax.local][25638][WebServer][perf][200 OK][/sleep?ms=110][{"id":"r4","proto":"http","ips":["127.0.0.1"],"host":"localhost:3012","ua":"curl/7.79.1","perf":{"scale":1000,"perf":{"total":117.214,"queue":0.072,"read":0.018,"process":112.894,"write":3.467},"counters":{"bytes_in":90,"bytes_out":179,"num_requests":1}},"pending":0,"running":0,"sockets":1}]
```

The log columns are configurable in [pixl-server](https://github.com/jhuckaby/pixl-server), but are typically the following:

| Column | Name | Description |
|--------|------|-------------|
| 1 | `hires_epoch` | Epoch date/time, including milliseconds (floating point).  This is retroactively adjusted to log the *start* of the request. |
| 2 | `date` | Human-readable date/time, in the local server timezone.  This is retroactively adjusted to log the *start* of the request. |
| 3 | `hostname` | The hostname of the server. |
| 4 | `component` | The server component name (`WebServer`). |
| 5 | `category` | The category of the log entry (`perf`). |
| 6 | `code` | The HTTP response code and message, e.g. `200 OK`. |
| 7 | `msg` | The URI of the request. |
| 8 | `data` | A JSON document containing data about the request and performance metrics. |

The `data` column is a JSON document containing various bits of additional information about the request, including the performance metrics.  Here is a formatted example:

```json
{
	"id": "r4",
	"proto": "http",
	"ips": [
		"127.0.0.1"
	],
	"host": "localhost:3012",
	"ua": "curl/7.79.1",
	"perf": {
		"scale": 1000,
		"perf": {
			"total": 117.214,
			"queue": 0.072,
			"read": 0.018,
			"process": 112.894,
			"write": 3.467
		},
		"counters": {
			"bytes_in": 90,
			"bytes_out": 179,
			"num_requests": 1
		}
	},
	"pending": 0,
	"running": 0,
	"sockets": 1
}
```

Here are descriptions of the data JSON properties:

| Property | Description |
|----------|-------------|
| `id` | The internal ID for the request. |
| `proto` | The protocol of the request (`http` or `https`). |
| `ips` | All the client IPs as an array (includes those from proxy headers). |
| `ua` | The `User-Agent` string from the request headers. |
| `host` | The hostname from the request URL. |
| `perf` | Performance metrics, see below. |
| `pending` | The total number of pending requests in the queue, as captured at the *start* of the current request. |
| `running` | The total number of running (active) requests being served, as captured at the *start* of the current request. |
| `sockets` | The total number of connected sockets, as captured at the *start* of the current request. |

The `perf` object contains performance metrics for the request, as returned from the [pixl-perf](https://www.github.com/jhuckaby/pixl-perf) module.  It includes a `scale` property denoting that all the metrics are displayed in milliseconds (i.e. `1000`).  The metrics themselves are in the `perf` object, and counters such as the number of bytes in/out are in the `counters` object.

The performance threshold system retroactively adjusts the log to represent the state of things at the *start* of the slow request.  Meaning, the `hires_epoch` and `date` columns are adjusted so that they represent the *start* of the request, not the end.  Furthermore, the `pending`, `running` and `sockets` counts in the data object also represent things at the start of the request, not the end.  The idea here is to help you diagnose what caused the slow request, so the log presents certain things as they were *just before* the request happened.

**Note:** When analyzing your performance logs, make sure that you *presort the rows* by the `hires_epoch` column.  The reason is, they will likely be out of order in the log file, because the logging operation actually happens at the end of the request, not the beginning.  For example, a long request that started first may be logged *after* a shorter request that started later.

### Including Diagnostic Reports

To include a partial or complete [Node.js Diagnostic Report](https://nodejs.org/docs/latest/api/report.html) in your performance log data, set the [perf_report](#perf_report) configuration property.  For a full report, set it to `true`:

```json
{
	"perf_report": true
}
```

However, please note that this is *very* verbose.  For a partial report, you can set it to an array of report keys to include.  Example:

```json
{
	"perf_report": ["uvthreadResourceUsage"]
}
```

Example log entry with a partial report included:

```
[1654217763.817487][2022-06-02 17:56:03][joemax.local][27616][WebServer][perf][200 OK][/sleep?ms=110][{"id":"r2","proto":"http","ips":["127.0.0.1"],"host":"localhost:3012","ua":"curl/7.79.1","perf":{"scale":1000,"perf":{"total":117.513,"queue":0.615,"read":0.021,"process":111.677,"write":2.996},"counters":{"bytes_in":90,"bytes_out":179,"num_requests":1}},"pending":0,"running":0,"sockets":1,"report":{"uvthreadResourceUsage":{"userCpuSeconds":0.081054,"kernelCpuSeconds":0.016156,"cpuConsumptionPercent":3.24033,"maxRss":46305116160,"pageFaults":{"IORequired":1,"IONotRequired":3365},"fsActivity":{"reads":0,"writes":0}}}}]
```

## Including Custom Metrics

To include your own application-level performance metrics in the logs and stats, a [pixl-perf](https://www.github.com/jhuckaby/pixl-perf) performance tracker is made available to your URI handler code via `args.perf`.  You can call `begin()` and `end()` on this object directly, to measure your own operations:

```js
server.WebServer.addURIHandler( '/my/custom/uri', 'Custom Name', function(args, callback) {
	// custom request handler for our URI
	
	args.perf.begin('db_query');
	// Run DB query here
	args.perf.end('db_query');
	args.perf.count('my_counter', 1);
	
	callback( 
		"200 OK", 
		{ 'Content-Type': "text/html" }, 
		"Hello this is custom content!\n" 
	);
} );
```

Please do not call `begin()` or `end()` without arguments, as that will mess up the existing performance tracking.  Also, make sure you prefix your perf keys so you don't collide with the built-in ones.

Alternatively, if you already use your own private [pixl-perf](https://www.github.com/jhuckaby/pixl-perf) object in your app, you can "import" it into the `args.perf` object at the very end of your handler code, just before you fire the request callback.  Example:

```js
my_perf.end();
args.perf.import( my_perf, "app_" );
```

This would import all your metrics and prefix the keys with `app_`.

See the [pixl-perf](https://www.github.com/jhuckaby/pixl-perf) documentation for more details on how to use the tracker.

# Stats

The web server keeps internal statistics including all open sockets, all active and recently completed requests, and performance metrics.  You can query for these by calling the `getStats()` method on the web server component.  Example:

```js
let stats = server.WebServer.getStats();
```

The result is an object in this format:

```json
{
	"server": {
		"uptime": 80,
		"hostname": "joeretina.local",
		"ip": "10.1.10.247",
		"name": "MyServer",
		"version": "1.0"
	},
	"stats": {
		"total": {
			"st": "mma",
			"min": 0.108,
			"max": 19.964,
			"total": 18719.696,
			"count": 2997,
			"avg": 6.246
		},
		"queue": {
			"st": "mma",
			"min": 3.707,
			"max": 10.917,
			"total": 8510.662,
			"count": 1373,
			"avg": 6.198
		},
		"read": {
			"st": "mma",
			"min": 0,
			"max": 0.134,
			"total": 2.533,
			"count": 1373,
			"avg": 0.001
		},
		"filter": {
			"st": "mma",
			"min": 0,
			"max": 0,
			"total": 0,
			"count": 0,
			"avg": 0
		}
		"process": {
			"st": "mma",
			"min": 0.834,
			"max": 6.1,
			"total": 3513.736,
			"count": 1373,
			"avg": 2.559
		},
		"write": {
			"st": "mma",
			"min": 0.08,
			"max": 8.85,
			"total": 6523.865,
			"count": 2997,
			"avg": 2.176
		},
		"bytes_in": 0,
		"bytes_out": 1175,
		"num_requests": 11,
		"num_sockets": 2
	},
	"listeners": {
		"http": {
			"address": "::",
			"family": "IPv6",
			"port": 80
		}
	},
	"sockets": {
		"c109": {
			"state": "idle",
			"ip": "::ffff:127.0.0.1",
			"proto": "http",
			"port": 80,
			"uptime_ms": 70315,
			"elapsed_ms": 5.343,
			"num_requests": 1,
			"bytes_in": 172,
			"bytes_out": 3869
		},
		"c110": {
			"state": "processing",
			"ip": "::ffff:127.0.0.1",
			"proto": "http",
			"port": 80,
			"uptime_ms": 1.23,
			"elapsed_ms": 0.280054,
			"num_requests": 38,
			"bytes_in": 0,
			"bytes_out": 14659,
			"ips": [
				"::ffff:127.0.0.1"
			],
			"method": "GET",
			"uri": "/server-status?pretty=1",
			"host": "localhost"
		}
	},
	"recent": [
		{
			"when": 1466203237,
			"proto": "http",
			"port": 80,
			"code": 200,
			"status": "OK",
			"uri": "/rimfire/native",
			"host": "localhost",
			"ips": [
				"::ffff:127.0.0.1"
			],
			"ua": "libwww-perl/6.08",
			"perf": {
				"scale": 1000,
				"perf": {
					"total": 2.403,
					"read": 0.02,
					"process": 0.281,
					"write": 2.026
				},
				"counters": {
					"bytes_in": 131,
					"bytes_out": 190,
					"num_requests": 1
				}
			}
		}
	],
	"queue": {
		"pending": 0,
		"running": 1
	}
}
```

## The Server Object

The `server` object contains information about the server as a whole.  The properties include:

| Property | Type | Description |
|----------|------|-------------|
| `hostname` | String | The hostname of the server. |
| `ip` | String | The local IP address of the server. |
| `name` | String | The name of your pixl-server instance. |
| `version` | String | The version of your pixl-server instance. |
| `uptime` | Integer | The number of seconds since the server was started. |

## The Stats Object

The `stats` object contains real-time performance metrics, representing one whole second of time.  Your server will need to have a constant flow of requests for this to actually show any meaningful data.  The properties include:

| Property | Type | Description |
|----------|------|-------------|
| `total` | Min/Max/Avg | Total request elapsed time. |
| `queue` | Min/Max/Avg | Total request time in queue. |
| `read` | Min/Max/Avg | Total request read time. |
| `filter` | Min/Max/Avg | Total request filter time. |
| `process` | Min/Max/Avg | Total request process time (i.e. custom URI handler). |
| `write` | Min/Max/Avg | Total request write time. |
| `bytes_in` | Simple Counter | Total bytes received in the last full second. |
| `bytes_out` | Simple Counter | Total sent in the last full second. |
| `num_requests` | Simple Counter | Total requests served in the last full second. |
| `num_sockets` | Simple Counter | Total number of open sockets at the current time. |

The object consists of both simple counters, and min/max/avg objects.  The latter is designed to represent specific performance metrics, and we include the minimum, maximum, and a count and total (for computing the average).  Simply divide the total by the count and you'll have the average over the 1.0 seconds of sample time.

The min/max/avg objects are all tagged with an `st` (stat type) key set to `mma` (min/max/avg).  This is simply an identifier for libraries wanting to display or graph the data.

If you add any of your own app's performance metrics via `args.perf`, they will be included in this object as well.  See [Including Custom Metrics](#including-custom-metrics) below for details.

## The Listeners Object

The `listeners` object contains information about the socket listeners currently open and receiving connections.  There may be one or two of these, depending on if HTTPS/SSL is enabled.  The `listeners` object will contain `http` and/or `https` sub-objects, each with the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `address` | String | The bound local IP address, or `::` for wildcard IPv6 or `0.0.0.0` for wildcard IPv4 (i.e. all network interfaces). |
| `port` | Integer | The local port number we are listening on. |
| `family` | String | The IP family, will be one of `IPv6` or `IPv4`. |

## The Sockets Object

The `sockets` object contains information about all currently open sockets.  Note that this is an object, not an array.  The keys are internal identifiers, and the values are sub-objects containing the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `state` | String | The current state of the socket, will be one of: `idle`, `reading`, `processing`, or `writing`. |
| `ip` | String | The client IP address connected to the socket (may be a load balancer or proxy). |
| `proto` | String | The protocol of the socket, will be `http` or `https`. |
| `port` | Integer | The listening port of the socket, e.g. `80` or `443`. |
| `uptime_ms` | Number | The total time the socket has been connected, in milliseconds. |
| `num_requests` | Integer | The total number of requests served by the socket (i.e. keep-alives). |
| `bytes_in` | Integer | The total number of bytes received by the socket. |
| `bytes_out` | Integer | The total number of bytes sent by the socket. |
| `elapsed_ms` | Number | If an HTTP request is in progress, this will contain the elapsed request time, in milliseconds. |
| `ips` | Array | If an HTTP request is in progress, this will contain the array of client IPs, including proxy IPs. |
| `method` | String | If an HTTP request is in progress, this will contain the request method (e.g. `GET`, `POST`, etc.) |
| `uri` | String | If an HTTP request is in progress, this will contain the full request URI. |
| `host` | String | If an HTTP request is in progress, this will contain the hostname from the URL. |

## The Recent Object

The `recent` array is a sorted list of the last 10 completed requests (most recent first).  Each element of the array is an object containing the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `when` | Integer | The date/time of the *completion* of the request, as high-res Epoch seconds. |
| `proto` | String | The protocol of the original client request, will be `http` or `https`. |
| `port` | Integer | The listening port of the socket, e.g. `80` or `443`. |
| `code` | Integer | The HTTP response code, e.g. `200` or `404`. |
| `status` | String | The HTTP response status message, e.g. `OK` or `File Not Found`. |
| `uri` | String | The full request URI including query string. |
| `host` | String | The hostname from the request URL. |
| `ips` | Array | The array of client IPs, including proxy IPs. |
| `ua` | String | The client's `User-Agent` string. |
| `perf` | Object | A [pixl-perf](https://www.github.com/jhuckaby/pixl-perf) performance metrics object containing stats for the request. |

If you would like more than 10 requests, set the [recent_requests](#recent_requests) configuration property to the number you want.

## The Queue Object

The `queue` object contains information about the request queue.  This includes the number of current active requests running in parallel, and the number of queued requests waiting to be processed.  The pending count is only relevant if [max_concurrent_requests](#max_concurrent_requests) is non-zero.  Here are the queue object properties:

| Property | Type | Description |
|----------|------|-------------|
| `pending` | Integer | The number of requests queued, waiting for processing.  Only used if [max_concurrent_requests](#max_concurrent_requests) is non-zero. |
| `running` | Integer | The number of active requests currently being processed in parallel. |

## Stats URI Handler

If you want to expose the `getStats()` object as a JSON web service, doing so is very easy.  Just register a URI handler via `addURIHandler()`, and pass the `getStats()` return value to the callback.  Example:

```js
server.WebServer.addURIHandler( '/server-status', "Server Status", true, function(args, callback) {
	callback( server.WebServer.getStats() );
} );
```

It is recommended that you lock this service down via ACL, as you probably don't want to expose it to the world.  See the [Access Control Lists](#access-control-lists) section for details on using ACLs in your handlers.

# Misc

## Determining HTTP or HTTPS

To determine if a request is HTTP or HTTPS, check to see if there is an `args.request.headers.ssl` property.  If this is set to a `true` value, then the request was sent in via HTTPS, otherwise you can assume it was HTTP.

Please note that if you have a load balancer or other proxy handling HTTPS / SSL for you, the final request to the web server may not be HTTPS.  To determine if the *original* request from the client was HTTPS, you may need to sniff for a particular request header, e.g. `X-Forwarded-Proto: https` (used by Amazon's ELB).

See the [https_header_detect](#https_header_detect) configuration property for an automatic way to handle this.

## Self-Referencing URLs

To build a URL that points at the current server, call `getSelfURL()` and pass in the `args.request` object.  This will produce a URL using the same protocol as the request (HTTP or HTTPS), the same hostname used on the request, and the port number if applicable.  By default, the URL will point to the root path (`/`).  Example:

```js
let url = server.WebServer.getSelfURL(args.request);
```

You can optionally pass in a URI path as the second argument.  For example, to build a URL to the exact request URI that came in, pass in `args.request.url` as the second argument:

```js
let url = server.WebServer.getSelfURL(args.request, args.request.url);
```

## Custom Method Handlers

You can also register a handler that is invoked for every single request for a given request method (i.e. `GET`, `POST`, `HEAD`, `OPTIONS`, etc.).  So instead of matching on the URI, this matches *all* requests for a specific method.  Method handlers are matched first, before URIs are checked.  

To use this, call the server `addMethodHandler()` method, and pass in the method name, title (for logging), and a callback function.  One potential use of this is to capture `OPTIONS` requests, which browsers send in for [CORS AJAX Preflights](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS).  Example:

```js
server.WebServer.addMethodHandler( "OPTIONS", "CORS Preflight", function(args, callback) {
	// handler for HTTP OPTIONS calls (CORS AJAX preflight)
	callback( "200 OK", 
		{
			'Access-Control-Allow-Origin': args.request.headers['origin'] || "*",
			'Access-Control-Allow-Methods': "POST, GET, HEAD, OPTIONS",
			'Access-Control-Allow-Headers': args.request.headers['access-control-request-headers'] || "*",
			'Access-Control-Max-Age': "1728000",
			'Content-Length': "0"
		},
		null
	);
} );
```

## Let's Encrypt / ACME TLS Certificates

These are instructions for using [Let's Encrypt](https://letsencrypt.org/) TLS certificates with **pixl-server-web**: how to get your certificate issued and how to keep it renewed automatically.

The examples below use the domain `mydomain.com`. Replace this with your own real domain.

### ACME clients

Let's Encrypt issues certificates using the **ACME protocol**. To talk ACME, you need an ACME *client*.

For most people, Let's Encrypt recommends **Certbot** as the default ACME client:

https://letsencrypt.org/docs/client-options/

Other popular clients include:

* **acme.sh** – pure shell, great DNS-API support.
* Various language-specific clients (Go, Rust, Node, etc.) – see the Let's Encrypt “ACME clients” list for a full catalog.

These docs focus on **Certbot**, with a short note about acme.sh for DNS-based / wildcard setups.

### Point your domain at your server

Before you can get a certificate:

1. Make sure your server has a **public IPv4 (and/or IPv6) address**.
2. In your DNS provider’s control panel, create an **A record** for your domain:
	- Name: `@` (or `mydomain.com`, provider-specific)
	- Type: `A`
	- Value: your server’s IPv4 address
	- Optionally create an **AAAA record** for IPv6.
3. Wait for DNS to propagate.

You should be able to open http://mydomain.com/ in a browser and hit your server.

### Install Certbot

1. Go to: https://certbot.eff.org/
2. Select:
	- Your OS (e.g. “Ubuntu 24.04” or “Debian 12”)
	- Web server: **“None of the above (or other)”**
3. Follow the instructions shown there.

Typical examples:

#### Ubuntu / Debian

Certbot’s maintainers (EFF) now publish current builds only through Snap:

```sh
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/local/bin/certbot
```

#### RHEL / CentOS / Fedora

DNF is the correct command to use on RedHat and family:

```sh
sudo dnf install certbot
```

Verify installation:

```sh
certbot --version
```

### Option A: HTTP-01 (webroot)

HTTP-01 requires port **80** open and a web root directory that pixl-server-web (or another HTTP server) uses.

#### Ensure HTTP is working on port 80

Configure pixl-server-web (or any HTTP server) to:

- Listen on **port 80**.
- Serve static content from a directory, for example `/var/www/html`.

Then visit: http://mydomain.com/

#### Issue a certificate using webroot

```sh
sudo certbot certonly --webroot -w /var/www/html -d mydomain.com
```

Add more hostnames if needed:

```sh
sudo certbot certonly --webroot -w /var/www/html -d mydomain.com -d www.mydomain.com
```

Certbot will create:

```
/etc/letsencrypt/live/mydomain.com/fullchain.pem
/etc/letsencrypt/live/mydomain.com/privkey.pem
/etc/letsencrypt/live/mydomain.com/cert.pem
/etc/letsencrypt/live/mydomain.com/chain.pem
```

### Configure pixl-server-web for HTTPS

In your pixl-server-web config:

```js
"https": true,
"https_port": 443,
"https_cert_file":  "/etc/letsencrypt/live/mydomain.com/cert.pem",
"https_key_file":   "/etc/letsencrypt/live/mydomain.com/privkey.pem",
"https_ca_file":    "/etc/letsencrypt/live/mydomain.com/chain.pem"
```

Then restart pixl-server-web so it can bind to port 443.

Visit: https://mydomain.com/

### Automatic renewal

Let's Encrypt certificates are valid for **90 days**.

Certbot automatically installs:

- A **systemd timer**, or
- A **cron job**

that runs `certbot renew` twice a day.

pixl-server-web will automatically reload certs when they change on disk.  There is no need to trigger a restart.

#### Check that renewal timers are installed

```sh
systemctl list-timers | grep certbot
```

Test renewal:

```sh
sudo certbot renew --dry-run
```

### Option B: DNS-01 with DNS API (wildcards, advanced)

Use DNS-01 if:

* You want a **wildcard cert** (`*.mydomain.com`).
* Port 80 is blocked or server is not exposed to the internet.
* You want a central ACME box managing certs.

DNS-01 works by creating a TXT record:

```
_acme-challenge.mydomain.com
```

#### Using Certbot DNS plugins

Example: Cloudflare

Install plugin (package varies by distro):

```
sudo apt install python3-certbot-dns-cloudflare
```

Create credentials file:

`~/.secrets/certbot/cloudflare.ini`

```ini
dns_cloudflare_api_token = YOUR_TOKEN
```

Lock permissions:

```sh
chmod 600 ~/.secrets/certbot/cloudflare.ini
```

Issue wildcard cert:

```sh
sudo certbot certonly --dns-cloudflare --dns-cloudflare-credentials ~/.secrets/certbot/cloudflare.ini -d mydomain.com -d '*.mydomain.com'
```

#### Using acme.sh

Install:

```sh
curl https://get.acme.sh | sh
```

Issue DNS-based cert:

```sh
~/.acme.sh/acme.sh --issue --dns dns_cf -d mydomain.com -d '*.mydomain.com'
```

Install certs into your preferred paths:

```sh
~/.acme.sh/acme.sh --install-cert -d mydomain.com --key-file /etc/letsencrypt/live/mydomain.com/privkey.pem --fullchain-file /etc/letsencrypt/live/mydomain.com/fullchain.pem
```

### Where your certificates live

Default Certbot paths:

```
/etc/letsencrypt/live/mydomain.com/privkey.pem
/etc/letsencrypt/live/mydomain.com/fullchain.pem
/etc/letsencrypt/live/mydomain.com/cert.pem
/etc/letsencrypt/live/mydomain.com/chain.pem
```

### Troubleshooting

Test renewal:

```sh
sudo certbot renew --dry-run
```

Logs:

```
/var/log/letsencrypt/letsencrypt.log
```

- DNS-01 issues:
	- Verify TXT record exists using `dig` or `nslookup`.
	- Ensure your API credentials have minimum DNS permissions.

For more information:

- https://letsencrypt.org/docs/
- https://certbot.eff.org/docs/

## Request Max Dump

For debugging and troubleshooting purposes, pixl-server-web can optionally generate a "dump" file when it reaches certain traffic limits.  Specifically, when one of these events occur:

- When the [max_connections](#max_connections) limit is reached.
- When the [max_queue_length](#max_queue_length) limit is reached.
- When the [max_queue_active](#max_queue_active) limit is reached.

To enable this feature, set the [req_max_dump_enabled](#req_max_dump_enabled) configuration property to `true`, the [req_max_dump_dir](#req_max_dump_dir) property to a path on your filesystem to hold your dump files (this will be created if needed), and [req_max_dump_debounce](#req_max_dump_debounce) to the maximum frequency you want files dumped (in seconds).  Example:

```json
"req_max_dump_enabled": true,
"req_max_dump_dir": "/var/log/web-server-dumps",
"req_max_dump_debounce": 10
```

This would generate dump files in the `/var/log/web-server-dumps` directory every 10 seconds, while one or more maximum limits are maxed out.

The dump files themselves are in JSON format, and contain everything from the [Stats API](#stats), as well as a list of all active and pending requests.  For each request, an object like the following is provided:

```json
{
	"r2945": {
		"uri": "/api/test/sleep?ms=1",
		"ip": "127.0.0.1",
		"ips": [
			"127.0.0.1"
		],
		"headers": {
			"accept-encoding": "gzip, deflate, br",
			"user-agent": "Mozilla/5.0; wperf/1.0.4",
			"host": "localhost:3012",
			"connection": "keep-alive"
		},
		"state": "writing",
		"date": 1644617758.688,
		"elapsed": 0.009999990463256836
	}
}
```

Here is a description of each property:

| Property Name | Type | Description |
|---------------|------|-------------|
| `uri` | String | The request URI path (sans protocol and hostname). |
| `ip` | String | The client's public IP address (may be a load balancer or proxy). |
| `ips` | All the client IPs as an array (includes those from proxy headers). |
| `headers` | String | All the incoming HTTP request headers from the client (lower-cased keys). |
| `state` | String | The state of the request, will be one of `queued`, `reading`, `filtering`, `processing` or `writing`. |
| `date` | String | The timestamp of the start of the request, in Epoch seconds. |
| `elapsed` | String | The elapsed time of the request in seconds. |

Each dump file is given a unique filename using the current server hostname, the pixl-server-web process PID, and a high-resolution timestamp in [Base36](https://en.wikipedia.org/wiki/Base36) format.  Example:

```
req-dump-joemax.local-67463-kziyy7eq.json
req-dump-joemax.local-67463-kziyy86i.json
req-dump-joemax.local-67463-kziyy8yc.json
```

# License

**The MIT License (MIT)**

*Copyright (c) 2015 - 2022 Joseph Huckaby.*

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

## File: `web_server.js`
```javascript
// Simple HTTP / HTTPS Web Server
// A component for the pixl-server daemon framework.
// Copyright (c) 2015 - 2022 Joseph Huckaby
// Released under the MIT License

const fs = require('fs');
const os = require('os');
const crypto = require('crypto');
const zlib = require('zlib');
const async = require('async');
const Class = require("class-plus");
const Component = require("pixl-server/component");
const ACL = require('pixl-acl');

module.exports = Class({
	
	__mixins: [
		require('./lib/http.js'),
		require('./lib/https.js'),
		require('./lib/handlers.js'),
		require('./lib/request.js'),
		require('./lib/response.js'),
		require('./lib/static.js')
	],
	
	version: require( __dirname + '/package.json' ).version,
	
	defaultConfig: {
		"private_ip_ranges": ['127.0.0.1', '10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16', '::1/128', 'fd00::/8', '169.254.0.0/16', 'fe80::/10'],
		"regex_text": "(text|javascript|json|css|html)",
		"regex_json": "(javascript|js|json)",
		"keep_alives": "default",
		"timeout": 120,
		"static_index": "index.html",
		"static_ttl": 0,
		"max_upload_size": 32 * 1024 * 1024,
		"temp_dir": os.tmpdir(),
		"gzip_opts": {
			"level": zlib.constants.Z_DEFAULT_COMPRESSION, 
			"memLevel": 8 
		},
		"brotli_opts": {
			"chunkSize": 16 * 1024,
			"mode": "text",
			"level": 4
		},
		"compress_text": false,
		"enable_brotli": false,
		"default_acl": ['127.0.0.1', '10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16', '::1/128', 'fd00::/8', '169.254.0.0/16', 'fe80::/10'],
		"blacklist": [],
		"whitelist": [],
		"allow_hosts": [],
		"log_requests": false,
		"log_request_details": false,
		"log_body_max": 32768,
		"log_perf": false,
		"perf_threshold_ms": 100,
		"perf_report": false,
		"recent_requests": 10,
		"max_connections": 0,
		"max_requests_per_connection": 0,
		"max_concurrent_requests": 0,
		"max_queue_length": 0,
		"max_queue_active": 0,
		"queue_skip_uri_match": false,
		"clean_headers": false,
		"log_socket_errors": true,
		"full_uri_match": false,
		"flatten_query": false,
		"request_timeout": 0,
		"req_max_dump_enabled": false,
		"req_max_dump_dir": "",
		"req_max_dump_debounce": 10,
		"code_response_headers": null,
		"legacy_callback_support": false,
		"https_cert_poll_ms": 60000
	},
	
	conns: null,
	numConns: 0,
	nextId: 1,
	uriFilters: null,
	uriHandlers: null,
	methodHandlers: null,
	defaultACL: null,
	stats: null,
	recent: null,
	
	badHeaderCharPattern: /([\x7F-\xFF\x00-\x1F\u00FF-\uFFFF])/g,
	
	responseCodes: {
		"100": "Continue",
		"101": "Switching Protocols",
		"102": "Processing",
		"103": "Early Hints",
		"200": "OK",
		"201": "Created",
		"202": "Accepted",
		"203": "Non Authoritative Information",
		"204": "No Content",
		"205": "Reset Content",
		"206": "Partial Content",
		"207": "Multi-Status",
		"300": "Multiple Choices",
		"301": "Moved Permanently",
		"302": "Moved Temporarily",
		"303": "See Other",
		"304": "Not Modified",
		"305": "Use Proxy",
		"307": "Temporary Redirect",
		"308": "Permanent Redirect",
		"400": "Bad Request",
		"401": "Unauthorized",
		"402": "Payment Required",
		"403": "Forbidden",
		"404": "Not Found",
		"405": "Method Not Allowed",
		"406": "Not Acceptable",
		"407": "Proxy Authentication Required",
		"408": "Request Timeout",
		"409": "Conflict",
		"410": "Gone",
		"411": "Length Required",
		"412": "Precondition Failed",
		"413": "Request Entity Too Large",
		"414": "Request-URI Too Long",
		"415": "Unsupported Media Type",
		"416": "Requested Range Not Satisfiable",
		"417": "Expectation Failed",
		"418": "I'm a teapot",
		"419": "Insufficient Space on Resource",
		"420": "Method Failure",
		"421": "Misdirected Request",
		"422": "Unprocessable Entity",
		"423": "Locked",
		"424": "Failed Dependency",
		"426": "Upgrade Required",
		"428": "Precondition Required",
		"429": "Too Many Requests",
		"431": "Request Header Fields Too Large",
		"451": "Unavailable For Legal Reasons",
		"500": "Internal Server Error",
		"501": "Not Implemented",
		"502": "Bad Gateway",
		"503": "Service Unavailable",
		"504": "Gateway Timeout",
		"505": "HTTP Version Not Supported",
		"507": "Insufficient Storage",
		"511": "Network Authentication Required"
	}
	
},
class WebServer extends Component {
	
	startup(callback) {
		// start http server
		var self = this;
		
		this.logDebug(2, "pixl-server-web v" + this.version + " starting up");
		
		// setup connections and handlers
		this.listeners = [];
		this.conns = {};
		this.requests = {};
		this.uriFilters = [];
		this.uriHandlers = [];
		this.methodHandlers = [];
		this.stats = { current: {}, last: {} };
		this.recent = [];
		
		this.prepConfig();
		this.config.on('reload', this.prepConfig.bind(this) );
		
		// setup queue to handle all requests
		// if both max concurrent req AND max connections are not set, just use a very large number
		this.queue = async.queue( this.parseHTTPRequest.bind(this), this.maxConcurrentReqs || 8192 );
		
		// listen for tick events to swap stat buffers
		this.server.on( 'tick', this.tick.bind(this) );
		
		// show post-startup foreground console message if applicable
		if ((this.server.debug || this.server.foreground) && this.config.get('startup_message')) {
			// add a slight delay to increase chances of user seeing it in the console
			this.server.on('ready', function() { setTimeout( self.postStartupMessage.bind(self), 250 ); } );
		}
		
		// optional chaos (fault injection)
		if (this.config.getPath('chaos.enabled')) this.setupChaos();
		
		// optional auth endpoints
		if (this.config.get('auth')) this.setupAuth();
		
		// start listeners
		this.startAll(callback);
	}
	
	setupAuth() {
		// basic auth behind custom URI patterns
		// auth: { "URI": { enabled, type, realm, username, password } }
		var self = this;
		var auth_config = this.config.get('auth');
		
		// constant-time comparison to avoid timing attacks
		var safeCompare = function(a, b) {
			const bufA = Buffer.from(a);
			const bufB = Buffer.from(b);
			if (bufA.length !== bufB.length) return false;
			return crypto.timingSafeEqual(bufA, bufB);
		};
		
		var checkBasicAuth = function(req, auth) {
			const header = req.headers['authorization'];
			if (!header) return false;
			
			const [scheme, encoded] = header.split(' ');
			if (scheme !== 'Basic' || !encoded) return false;
			
			const decoded = Buffer.from(encoded, 'base64').toString('utf8');
			const index = decoded.indexOf(':');
			if (index === -1) return false;
			
			const username = decoded.slice(0, index);
			const password = decoded.slice(index + 1);
			
			return safeCompare(username, auth.username) && safeCompare(password, auth.password);
		};
		
		Object.keys(auth_config).forEach( function(uri_match) {
			var auth = auth_config[uri_match];
			if (!auth.enabled) return;
			if (auth.type != 'basic') {
				self.logError('auth', "Unsupported auth type: " + auth.type);
				return;
			}
			
			self.addURIFilter( new RegExp(uri_match), "Auth", function(args, callback) {
				self.logDebug(9, "Checking auth for: " + uri_match, { realm: auth.realm });
				if (!checkBasicAuth(args.request, auth)) {
					return callback( "401 Unauthorized", {
						'WWW-Authenticate': `Basic realm="${auth.realm}"`,
						'Content-Type': 'text/plain'
					}, "Unauthorized" );
				}
				self.logDebug(9, "Authentication successful for: " + uri_match, { realm: auth.realm, username: auth.username });
				callback(false); // passthru
			} ); // addURIFilter
		} ); // foreach auth
	}
	
	setupChaos() {
		// setup chaos system (random delays, errors, etc.)
		// chaos: { enabled, uri?, delay?: { min:0, max:250 }, errors?: { "503 Service Unavailable": 0.1 }, headers? }
		var self = this;
		var chaos = this.config.get('chaos');
		
		this.addURIFilter( new RegExp(chaos.uri || '.+'), "Chaos", function(args, callback) {
			var ms = chaos.delay ? Math.round( chaos.delay.min + (Math.random() * (chaos.delay.max - chaos.delay.min)) ) : 0;
			if (ms) self.logDebug(9, `Chaos: Delaying request for ${ms}ms`);
			
			setTimeout( function() {
				if (!chaos.errors) return callback(false); // passthru
				var chosen = false;
				
				for (var status in chaos.errors) {
					if (Math.random() <= chaos.errors[status]) { chosen = status; break; }
				}
				
				if (chosen) {
					self.logDebug(9, `Chaos: Injecting fault: $(chosen)`);
					callback( chosen, chaos.headers || {}, "Simulated Error: " + chosen );
				}
				else callback(false);
			}, ms); // setTimeout
		}); // addURIFilter
	}
	
	prepConfig() {
		// prep config at startup, and when config is hot reloaded
		
		// support old config format with `http_` prefixed keys
		for (var key in this.config.get()) {
			if (key.match(/^(http_)(\w+)$/)) this.config.set( RegExp.$2, this.config.get(key) );
		}
		
		// setup default acl
		try { 
			this.defaultACL = new ACL( this.config.get('default_acl') ); 
		}
		catch (err) {
			this.logError('acl', "Failed to initialize default ACL: " + err);
			this.defaultACL = new ACL();
		}
		
		// setup blacklist
		delete this.aclBlacklist;
		var blacklist = this.config.get('blacklist');
		if (blacklist && blacklist.length) {
			try { this.aclBlacklist = new ACL( blacklist ); }
			catch (err) { this.logError('acl', "Failed to initialize blacklist: " + err); }
		}
		
		// setup whitelist
		delete this.aclWhitelist;
		var whitelist = this.config.get('whitelist');
		if (whitelist && whitelist.length) {
			try { this.aclWhitelist = new ACL( whitelist ); }
			catch (err) { this.logError('acl', "Failed to initialize whitelist: " + err); }
		}
		
		// setup private range matcher
		try {
			this.aclPrivateRanges = new ACL( this.config.get('private_ip_ranges') );
		}
		catch (err) {
			this.logError('acl', "Failed to initialize private range ACL: " + err);
			this.aclPrivateRanges = new ACL();
		}
		
		// pre-compute some config values
		this.regexTextContent = new RegExp( this.config.get('regex_text'), "i" );
		this.regexJSONContent = new RegExp( this.config.get('regex_json'), "i" );
		this.logRequests = this.config.get('log_requests');
		this.logRequestDetails = this.config.get('log_request_details');
		this.logRequestBodyMax = this.config.get('log_body_max');
		this.regexLogRequests = this.logRequests ? (new RegExp( this.config.get('regex_log') || '.+' )) : null;
		this.logPerfEnabled = this.config.get('log_perf');
		this.logPerfThreshold = this.config.get('perf_threshold_ms');
		this.logPerfReport = this.config.get('perf_report');
		this.keepRecentRequests = this.config.get('recent_requests');
		
		// optionally compress text
		this.compressText = this.config.get('compress_text') || this.config.get('gzip_text');
		
		// brotli compression support
		this.hasBrotli = !!zlib.BrotliCompress && this.config.get('enable_brotli');
		this.acceptEncodingMatch = this.hasBrotli ? /\b(gzip|deflate|br)\b/i : /\b(gzip|deflate)\b/i;
		
		// map friendly keys to brotli constants
		var brotli_opts = this.config.get('brotli_opts');
		if ("mode" in brotli_opts) {
			switch (brotli_opts.mode) {
				case 'text': brotli_opts.mode = zlib.constants.BROTLI_MODE_TEXT; break;
				case 'font': brotli_opts.mode = zlib.constants.BROTLI_MODE_FONT; break;
				case 'generic': brotli_opts.mode = zlib.constants.BROTLI_MODE_GENERIC; break;
			}
			if (!brotli_opts.params) brotli_opts.params = {};
			brotli_opts.params[ zlib.constants.BROTLI_PARAM_MODE ] = brotli_opts.mode;
			delete brotli_opts.mode;
		}
		if ("level" in brotli_opts) {
			if (!brotli_opts.params) brotli_opts.params = {};
			brotli_opts.params[ zlib.constants.BROTLI_PARAM_QUALITY ] = brotli_opts.level;
			delete brotli_opts.level;
		}
		if ("hint" in brotli_opts) {
			if (!brotli_opts.params) brotli_opts.params = {};
			brotli_opts.params[ zlib.constants.BROTLI_PARAM_SIZE_HINT ] = brotli_opts.hint;
			delete brotli_opts.hint;
		}
		
		// keep-alives
		this.keepAlives = this.config.get('keep_alives');
		if (this.keepAlives === false) this.keepAlives = 0;
		else if (this.keepAlives === true) this.keepAlives = 1;
		
		// optional max requests per KA connection
		this.maxReqsPerConn = this.config.get('max_requests_per_connection');
		this.maxQueueLength = this.config.get('max_queue_length');
		this.maxQueueActive = this.config.get('max_queue_active');
		
		// NOTE: changing maxConcurrentReqs at runtime has no effect
		this.maxConcurrentReqs = this.config.get('max_concurrent_requests') || this.config.get('max_connections');
		
		this.queueSkipMatch = this.config.get('queue_skip_uri_match') ? 
			new RegExp( this.config.get('queue_skip_uri_match') ) : false;
		
		// front-end https header detection
		var ssl_headers = this.config.get('https_header_detect');
		if (ssl_headers) {
			this.ssl_header_detect = {};
			for (var key in ssl_headers) {
				this.ssl_header_detect[ key.toLowerCase() ] = new RegExp( ssl_headers[key] );
			}
		}
		else delete this.ssl_header_detect;
		
		// initialize request max dump system, if enabled
		this.reqMaxDumpEnabled = this.config.get('req_max_dump_enabled');
		this.reqMaxDumpDir = this.config.get('req_max_dump_dir');
		this.reqMaxDumpDebounce = this.config.get('req_max_dump_debounce');
		this.reqMaxDumpLast = 0;
		
		if (this.reqMaxDumpEnabled && this.reqMaxDumpDir && !fs.existsSync(this.reqMaxDumpDir)) {
			fs.mkdirSync( this.reqMaxDumpDir, { mode: 0o777, recursive: true } );
		}
		
		// url rewrites
		this.rewrites = [];
		if (this.config.get('rewrites')) {
			var rewrite_map = this.config.get('rewrites');
			for (var key in rewrite_map) {
				var rewrite = rewrite_map[key];
				if (typeof(rewrite) == 'string') rewrite = { url: rewrite_map[key] };
				rewrite.regexp = new RegExp(key);
				this.rewrites.push(rewrite);
			}
		}
		
		// url redirects
		this.redirects = [];
		if (this.config.get('redirects')) {
			var redir_map = this.config.get('redirects');
			for (var key in redir_map) {
				var redirect = redir_map[key];
				if (typeof(redirect) == 'string') redirect = { url: redir_map[key] };
				redirect.regexp = new RegExp(key);
				this.redirects.push(redirect);
			}
		}
		
		// custom host list
		this.allowHosts = (this.config.get('allow_hosts') || []).map( function(host) { return host.toLowerCase(); } );
		this.httpsAllowHosts = (this.config.get('https_allow_hosts') || this.config.get('allow_hosts') || []).map( function(host) { return host.toLowerCase(); } );
		
		// set static TTL to 0 in debug mode
		if (this.server.debug && this.config.get('debug_ttl')) {
			this.logDebug(5, "Setting static TTL to 0 for debug mode");
			this.config.set('static_ttl', 0);
		}
		
		// default bind addr to localhost in debug mode
		if (this.server.debug && !this.config.get('bind_address') && !this.server.config.get('expose') && this.config.get('debug_bind_local')) {
			this.logDebug(5, "Setting bind address to localhost for debug mode");
			this.config.set('bind_address', 'localhost');
		}
		
		// pre-compile regexps for uri_response_headers
		this.uriResponseHeaders = [];
		var patterns = this.config.get('uri_response_headers');
		if (patterns) {
			for (var pat in patterns) {
				this.logDebug(5, "Adding custom response headers for URI pattern: " + pat, patterns[pat]);
				this.uriResponseHeaders.push({
					regexp: new RegExp(pat),
					headers: patterns[pat]
				});
			}
		}
	}
	
	postStartupMessage() {
		// show startup message in console (debug / foreground only)
		var self = this;
		var stats = this.getStats();
		var text = '';
		
		text += "\nWeb Server Listeners:\n";
		
		stats.listeners.forEach( function(info) {
			// {"address":"::1","family":"IPv6","port":3013,"ssl":true}
			var type = info.ssl ? 'HTTPS' : 'HTTP';
			var host = info.address;
			text += `\n\tListening for ${type} on port ${info.port}, network '${info.address}'`;
			
			switch (info.address) {
				case '::1':
				case '127.0.0.1':
					text += ' (localhost)';
					host = 'localhost';
				break;
				
				case '::':
				case '0.0.0.0':
					text += ' (all)';
					host = self.server.ip; // best guess (ipv4)
				break;
			}
			
			text += "\n";
			var url = (info.ssl ? 'https://' : 'http://') + host;
			if (info.ssl && (info.port != 443)) url += ':' + info.port;
			if (!info.ssl & (info.port != 80)) url += ':' + info.port;
			url += '/';
			text += "\t--> " + url + "\n";
		} );
		
		console.log(text);
	}
	
	startAll(callback) {
		// start all HTTP(s) listeners
		var self = this;
		var tasks = [];
		
		// always start plain HTTP on base port
		tasks.push([ this.config.get('port'), 'startHTTP' ]);
		
		// optional additional ports
		(this.config.get('alt_ports') || []).forEach( function(port) {
			tasks.push([ port, 'startHTTP' ]);
		} );
		
		// optional HTTPS
		if (this.config.get('https')) {
			tasks.push([ this.config.get('https_port'), 'startHTTPS' ]);
			
			// optional additional ports
			(this.config.get('https_alt_ports') || []).forEach( function(port) {
				tasks.push([ port, 'startHTTPS' ]);
			} );
			
			// load certs and setup monitoring
			this.setupHTTPS();
		}
		
		// start all listeners in parallel
		async.each( tasks,
			function(task, callback) {
				var port = task[0];
				var func = task[1];
				self[func](port, callback);
			},
			callback
		);
	}
	
	dumpAllRequests() {
		// create dump file containing info on all active/pending requests
		// this is called when requests or sockets are maxed out
		// only write file every N seconds
		var self = this;
		var now = Date.now() / 1000;
		if (!this.reqMaxDumpEnabled) return;
		if (now - this.reqMaxDumpLast < this.reqMaxDumpDebounce) return;
		this.reqMaxDumpLast = now;
		
		var dump_file = this.reqMaxDumpDir + '/req-dump-' + os.hostname() + '-' + process.pid + '-' + Date.now().toString(36) + '.json';
		var json = this.getStats();
		json.requests = {};
		
		for (var id in this.requests) {
			var args = this.requests[id];
			var info = {
				uri: args.request.url,
				ip: args.ip,
				ips: args.ips,
				headers: args.request.headers,
				state: args.state,
				date: args.date,
				elapsed: now - args.date
			};
			if (args.request.socket && args.request.socket._pixl_data && args.request.socket._pixl_data.aborted) {
				info.aborted = true;
			}
			json.requests[id] = info;
		}
		
		this.logDebug(5, "Writing dump file: " + dump_file );
		fs.writeFile( dump_file, JSON.stringify(json, null, "\t") + "\n", function(err) {
			if (err) self.logError('dump', "Failed to write dump file: " + dump_file + ": " + err, err);
		} );
	}
	
	deleteUploadTempFiles(args) {
		// delete leftover temp files created by Formidable
		for (var key in args.files) {
			var file = args.files[key];
			fs.unlink( file.path, function(err) {
				// file may have been moved / deleted already, so ignore error here
			} );
		}
	}
	
	tick() {
		// swap current and last stat buffers
		// called every 1s via server tick event
		this.stats.last = this.stats.current;
		this.stats.current = {};
	}
	
	getStats() {
		// get current stats, merged with live socket and request info
		var socket_info = {};
		var listener_info = [];
		var now = (new Date()).getTime();
		var num_sockets = 0;
		
		listener_info = this.listeners.map( function(listener) {
			var info = listener.address() || { port: 'n/a' };
			if (listener.setSecureContext) info.ssl = true;
			return info;
		} );
		
		for (var key in this.conns) {
			var socket = this.conns[key];
			var socket_data = socket._pixl_data;
			var info = {
				state: 'idle',
				ip: socket.remoteAddress,
				proto: socket_data.proto,
				port: socket_data.port,
				uptime_ms: now - socket_data.time_start,
				num_requests: socket_data.num_requests,
				bytes_in: socket_data.bytes_in,
				bytes_out: socket_data.bytes_out
			};
			if (socket_data.current) {
				// current request in progress, merge this in
				var args = socket_data.current;
				info.ips = args.ips;
				info.state = args.state;
				info.method = args.request.method;
				info.uri = args.request.url;
				info.host = args.request.headers['host'] || '';
				info.elapsed_ms = args.perf.calcElapsed( args.perf.perf.total.start );
			}
			socket_info[key] = info;
			num_sockets++;
		}
		
		var stats = this.stats.last;
		stats.num_sockets = num_sockets;
		if (!stats.num_requests) stats.num_requests = 0;
		if (!stats.bytes_in) stats.bytes_in = 0;
		if (!stats.bytes_out) stats.bytes_out = 0;
		
		['total', 'queue', 'read', 'filter', 'process', 'encode', 'write'].forEach( function(key) {
			if (!stats[key]) stats[key] = { "st": "mma", "min": 0, "max": 0, "total": 0, "count": 0 };
		} );
		
		for (var key in stats) {
			var stat = stats[key];
			if ((stat.st == "mma") && ("total" in stat) && ("count" in stat)) {
				stat.avg = stat.total / (stat.count || 1);
			}
		}
		
		return {
			server: {
				uptime_sec: Math.floor(now / 1000) - this.server.started,
				hostname: this.server.hostname,
				ip: this.server.ip,
				name: this.server.__name,
				version: this.server.__version,
				ports: listener_info.map( function(info) { return info.port; } )
			},
			stats: stats,
			listeners: listener_info,
			sockets: socket_info,
			recent: this.recent,
			queue: {
				pending: this.queue.length(),
				running: this.queue.running()
			}
		};
	}
	
	getAllClientIPs(request) {
		// create array of all IPs from the request, using the socket IP and X-Forwarded-For, if applicable
		var ips = [];
		var headers = request.headers || {};
		
		// single IP headers
		['x-client-ip', 'cf-connecting-ip', 'true-client-ip', 'x-real-ip', 'x-cluster-client-ip'].forEach( function(key) {
			if (headers[key]) ips.push( headers[key] );
		} );
		
		// multi-CSV IP headers
		['x-forwarded-for', 'forwarded-for'].forEach( function(key) {
			if (headers[key]) [].push.apply( ips, headers[key].split(/\,\s*/) );
		} );
		
		// special headers
		// e.g. Forwarded: for=192.0.2.43, for="[2001:db8:cafe::17]"
		['x-forwarded', 'forwarded'].forEach( function(key) {
			if (headers[key]) headers[key].replace( /\bfor\=\"?\[?([^\,\]\"]+)/g, function(m_all, m_g1) {
				ips.push( m_g1 );
			} );
		} );
		
		// add socket ip to end of array
		var ip = ''+request.socket.remoteAddress;
		if (ip.match(/\:(\d+\.\d+\.\d+\.\d+)/)) ip = RegExp.$1; // extract IPv4 from IPv6 wrapper
		ips.push( ip );
		
		return ips;
	}
	
	getPublicIP(ips) {
		// filter out garbage that doesn't resemble ips
		var public_ip_offset = this.config.get('public_ip_offset') || 0;
		
		var real_ips = ips.filter( function(ip) {
			return ip.match( /^([\d\.]+|[a-f0-9:]+)$/ );
		} );
		
		if (public_ip_offset) {
			// locate public IP using custom offset (usually negative, from end of list)
			var temp = real_ips.slice( public_ip_offset, public_ip_offset + 1 || real_ips.length );
			if (temp[0]) return temp[0];
		}
		else {
			// determine first public IP from list of IPs
			for (var idx = 0, len = real_ips.length; idx < len; idx++) {
				if (!this.aclPrivateRanges.check(real_ips[idx])) return real_ips[idx];
			}
		}
		
		// default to first ip
		return real_ips[0];
	}
	
	getSelfURL(request, uri) {
		// build self referencing URL given request object
		// and optional replacement URI
		if (!request.headers.host) return null;
		
		var ssl = !!request.headers.ssl;
		var url = ssl ? 'https://' : 'http://';
		url += request.headers.host.replace(/\:\d+$/, '');
		
		// only re-add port number if original incoming request had one
		if (request.headers.host.match(/\:\d+$/)) {
			if (ssl && this.config.get('https_port') && (this.config.get('https_port') != 443)) {
				url += ':' + this.config.get('https_port');
			}
			else if (!ssl && this.config.get('port') && (this.config.get('port') != 80)) {
				url += ':' + this.config.get('port');
			}
		}
		
		url += (uri || '/');
		
		return url;
	}
	
	getNextId(prefix) {
		// get unique ID with prefix
		return '' + prefix + Math.floor(this.nextId++);
	}
	
	ucfirst(text) {
		// capitalize first character only, lower-case rest
		return text.substring(0, 1).toUpperCase() + text.substring(1, text.length).toLowerCase();
	}
	
	shutdown(callback) {
		// shutdown http server
		var self = this;
		
		if (this.listeners.length) {
			this.logDebug(2, "Shutting down HTTP server");
			
			for (var id in this.requests) {
				var args = this.requests[id];
				this.logDebug(4, "Request still active: " + args.id, {
					id: args.id,
					ips: args.ips,
					uri: args.request ? args.request.url : '',
					headers: args.request ? args.request.headers : {},
					socket: (args.request && args.request.socket && args.request.socket._pixl_data) ? args.request.socket._pixl_data.id : '',
					stats: args.state,
					date: args.date,
					age: (Date.now() / 1000) - args.date
				});
				if (args.callback) {
					args.callback();
					delete args.callback;
				}
			} // foreach req
			
			for (var id in this.conns) {
				this.logDebug(4, "Closing HTTP connection: " + id);
				// this.conns[id].destroy();
				this.conns[id].end();
				this.conns[id].unref();
				this.numConns--;
			} // foreach conn
			
			// close all listeners
			this.listeners.forEach( function(listener) {
				var info = listener.address() || { port: 'n/a' };
				if (listener.setSecureContext) info.ssl = true;
				listener.close( function() { self.logDebug(3, (info.ssl ? "HTTPS": "HTTP") + " server on port " + info.port + " has shut down.", info); } );
			} );
			
			this.requests = {};
			this.queue.kill();
		}
		
		callback();
	}
	
});
```

## File: `lib/args.js`
```javascript
// Simple HTTP / HTTPS Web Server
// A component for the pixl-server daemon framework.
// Copyright (c) 2015 - 2025 Joseph Huckaby
// Released under the MIT License

module.exports = class Args {
	
	constructor(args = {}) {
		// import k/v pairs
		for (var key in args) this[key] = args[key];
	}
	
	setCookie(name, value, opts) {
		// set cookie in response headers
		// opts: { maxAge?, expires?, domain?, path?, secure?, httpOnly?, sameSite? }
		const res = this.response;
		const enc = (s) => encodeURIComponent(s);
		const parts = [`${enc(name)}=${value === '' ? '' : enc(value)}`];
		
		// serialize cookie to string
		if (opts.maxAge != null) parts.push(`Max-Age=${Math.floor(opts.maxAge)}`);
		if (opts.expires) parts.push(`Expires=${opts.expires.toUTCString()}`);
		if (opts.domain) parts.push(`Domain=${opts.domain}`);
		parts.push(`Path=${opts.path || '/'}`);
		if (opts.secure) {
			if (opts.secure === 'auto') {
				if (this.request.headers.ssl) parts.push('Secure');
			}
			else parts.push('Secure');
		}
		if (opts.httpOnly !== false) parts.push('HttpOnly'); // default on
		if (opts.sameSite) {
			const ss = String(opts.sameSite).toLowerCase();
			const token = ss === 'strict' ? 'Strict' : ss === 'none' ? 'None' : 'Lax';
			parts.push(`SameSite=${token}`);
		} else {
			parts.push('SameSite=Lax');
		}
		const cookieStr = parts.join('; ');
		
		// append to previous set-cookie or set as solo header
		const prev = res.getHeader('Set-Cookie');
		if (!prev) res.setHeader('Set-Cookie', cookieStr);
		else if (Array.isArray(prev)) res.setHeader('Set-Cookie', prev.concat(cookieStr));
		else res.setHeader('Set-Cookie', [prev, cookieStr]);
	}
	
};
```

## File: `lib/handlers.js`
```javascript
// Simple HTTP / HTTPS Web Server
// A component for the pixl-server daemon framework.
// Copyright (c) 2015 - 2021 Joseph Huckaby
// Released under the MIT License

const fs = require('fs');
const Path = require('path');
const ACL = require('pixl-acl');

module.exports = class Handlers {
	
	addURIFilter(uri, name, callback) {
		// add custom filter (chainable pre-handler) for URI
		this.logDebug(3, "Adding custom URI filter: " + uri + ": " + name);
		
		if (typeof(uri) == 'string') {
			uri = new RegExp("^" + uri + "$");
		}
		
		this.uriFilters.push({
			regexp: uri,
			name: name,
			callback: callback
		});
	}
	
	removeURIFilter(name) {
		// remove filter for URI given name
		this.uriFilters = this.uriFilters.filter( function(item) {
			return( item.name != name );
		} );
	}
	
	addURIHandler() {
		// add custom handler for URI
		// Calling conventions:
		//		uri, name, callback
		//		uri, name, acl, callback
		var self = this;
		var uri = arguments[0];
		var name = arguments[1];
		var acl = false;
		var callback = null;
		
		if (arguments.length == 4) { acl = arguments[2]; callback = arguments[3]; }
		else { callback = arguments[2]; }
		
		if (acl) {
			if (Array.isArray(acl)) {
				// custom ACL for this handler
				var blocks = new ACL();
				try {
					acl.forEach( function(block) {
						blocks.add( block );
					} );
					acl = blocks;
				}
				catch (err) {
					var err_msg = "Failed to initialize custom ACL: " + err.message;
					this.logError('acl', err_msg);
					throw new Error(err_msg);
				}
			}
			else {
				// use default ACL list
				acl = this.defaultACL;
			}
		} // acl
		
		this.logDebug(3, "Adding custom URI handler: " + uri + ": " + name);
		if (typeof(uri) == 'string') {
			uri = new RegExp("^" + uri + "$");
		}
		
		// special case: pass string as callback for internal file redirect
		if (typeof(callback) == 'string') {
			var target_file = callback;
			callback = function(args, cb) {
				self.logDebug(9, "Performing internal redirect to: " + target_file);
				args.internalFile = target_file;
				cb(false);
			};
		}
		
		this.uriHandlers.push({
			regexp: uri,
			name: name,
			acl: acl,
			callback: callback
		});
	}
	
	removeURIHandler(name) {
		// remove handler for URI given name
		this.uriHandlers = this.uriHandlers.filter( function(item) {
			return( item.name != name );
		} );
	}
	
	addMethodHandler(method, name, callback) {
		// add a handler for an entire request method, e.g. OPTIONS
		this.logDebug(3, "Adding custom request method handler: " + method + ": " + name);
		this.methodHandlers.push({
			method: method,
			name: name,
			callback: callback
		});
	}
	
	removeMethodHandler(name) {
		// remove handler for method given name
		this.methodHandlers = this.methodHandlers.filter( function(item) {
			return( item.name != name );
		} );
	}
	
	addDirectoryHandler(uri_match, base_path, opts) {
		// special URI handler that serves up a static directory
		// opts: { acl, ttl, headers }
		var self = this;
		if (!opts) opts = {};
		
		if (typeof(uri_match) == 'string') {
			// if string, assume is uri prefix
			uri_match = new RegExp("^" + uri_match);
		}
		
		this.addURIHandler(uri_match, "Static Directory: " + uri_match, opts.acl, function(args, callback) {
			var uri = args.request.url.replace(/\?.*$/, '');
			var file = Path.join( base_path, uri.replace(uri_match, '') ).replace(/\/$/, '');
			
			self.logDebug(9, "Routing static request for: " + uri, {
				base_path: base_path,
				file: file
			});
			
			if (opts.headers) {
				for (var key in opts.headers) {
					args.response.setHeader( key, opts.headers[key] );
				}
			}
			
			args.internalTTL = opts.ttl || 0;
			args.internalFile = file;
			callback(false);
		});
	}
	
	removeDirectoryHandler(uri_match) {
		// remove static directory handler by uri match specifier
		if (typeof(uri_match) == 'string') {
			// if string, assume is uri prefix
			uri_match = new RegExp("^" + uri_match);
		}
		this.removeURIHandler( "Static Directory: " + uri_match );
	}
	
};
```

## File: `lib/http.js`
```javascript
// Simple HTTP / HTTPS Web Server
// A component for the pixl-server daemon framework.
// Copyright (c) 2015 - 2021 Joseph Huckaby
// Released under the MIT License

const ErrNo = require('errno');
const Perf = require('pixl-perf');

module.exports = class HTTP {
	
	startHTTP(port, callback) {
		// start http server
		var self = this;
		var bind_addr = this.config.get('bind_address') || '';
		var max_conns = this.config.get('max_connections') || 0;
		var https_force = self.config.get('https_force') || false;
		var socket_prelim_timeout = self.config.get('socket_prelim_timeout') || 0;
		
		this.logDebug(2, "Starting HTTP server on port: " + port, bind_addr);
		
		var handler = function(request, response) {
			if (socket_prelim_timeout && request.socket._pixl_data.prelim_timer) {
				clearTimeout( request.socket._pixl_data.prelim_timer );
				delete request.socket._pixl_data.prelim_timer;
			}
			if (https_force) {
				self.logDebug(6, "Forcing redirect to HTTPS (SSL)");
				request.headers.ssl = 1; // force SSL url
				
				var args = {
					request: request,
					response: response,
					perf: new Perf()
				};
				args.perf.begin();
				
				var redirect_url = self.getSelfURL(request, request.url);
				if (!redirect_url) {
					self.sendHTTPResponse( args, "400 Bad Request", {}, "" );
					return;
				}
				
				self.sendHTTPResponse( args, 
					"301 Moved Permanently", 
					{ 'Location': redirect_url }, 
					"" // empty body
				);
			}
			else {
				self.enqueueHTTPRequest( request, response );
			}
		};
		
		var listener = require('http').createServer( handler );
		
		listener.on('connection', function(socket) {
			var ip = socket.remoteAddress || '';
			
			if (max_conns && (self.numConns >= max_conns)) {
				// reached maximum concurrent connections, abort new ones
				self.logError('maxconns', "Maximum concurrent connections reached, denying connection from: " + ip, { ip: ip, port: port, max: max_conns });
				socket.end();
				socket.unref();
				socket.destroy(); // hard close
				self.dumpAllRequests();
				return;
			}
			if (self.server.shut) {
				// server is shutting down, abort new connections
				self.logError('shutdown', "Server is shutting down, denying connection from: " + ip, { ip: ip, port: port });
				socket.end();
				socket.unref();
				socket.destroy(); // hard close
				return;
			}
			if (ip && self.aclBlacklist && self.aclBlacklist.check(ip)) {
				self.logError('blacklist', "IP is blacklisted, denying connection from: " + ip, { ip: ip, port: port });
				socket.end();
				socket.unref();
				socket.destroy(); // hard close
				return;
			}
			if (ip && self.aclWhitelist && !self.aclWhitelist.check(ip)) {
				self.logError('whitelist', "IP is not whitelisted, denying connection from: " + ip, { ip: ip, port: port });
				socket.end();
				socket.unref();
				socket.destroy(); // hard close
				return;
			}
			
			var id = self.getNextId('c');
			self.conns[ id ] = socket;
			self.numConns++;
			self.logDebug(8, "New incoming HTTP connection: " + id, { ip: ip, port: port, num_conns: self.numConns });
			
			// Disable the Nagle algorithm.
			socket.setNoDelay( true );
			
			// add our own metadata to socket
			socket._pixl_data = {
				id: id,
				port: port,
				proto: 'http',
				port: port,
				time_start: (new Date()).getTime(),
				num_requests: 0,
				bytes_in: 0,
				bytes_out: 0
			};
			
			// optional preliminary socket timeout for first request
			if (socket_prelim_timeout) {
				socket._pixl_data.prelim_timer = setTimeout( function() {
					delete socket._pixl_data.prelim_timer;
					var msg = "Socket preliminary timeout waiting for initial request (" + socket_prelim_timeout + " seconds)";
					var err_args = {
						ip: ip,
						port: port,
						pending: self.queue.length(),
						active: self.queue.running(),
						sockets: self.numConns
					};
					if (self.config.get('log_socket_errors')) {
						self.logError('socket', "Socket error: " + socket._pixl_data.id + ": " + msg, err_args);
					}
					else {
						self.logDebug(5, "Socket error: " + socket._pixl_data.id + ": " + msg, err_args);
					}
					
					socket._pixl_data.aborted = true;
					socket.end();
					socket.unref();
					socket.destroy(); // hard close
				}, socket_prelim_timeout * 1000 );
			} // socket_prelim_timeout
			
			self.emit('socket', socket);
			
			socket.on('error', function(err) {
				// client aborted connection?
				var args = socket._pixl_data.current || { request: {} };
				var msg = err.message;
				if (err.errno && ErrNo.code[err.errno]) {
					msg = self.ucfirst(ErrNo.code[err.errno].description) + " (" + err.message + ")";
				}
				if (self.config.get('log_socket_errors')) {
					self.logError(err.code || 'socket', "Socket error: " + id + ": " + msg, {
						ip: ip,
						ips: args.ips,
						port: port,
						state: args.state,
						method: args.request.method,
						uri: args.request.url,
						pending: self.queue.length(),
						active: self.queue.running(),
						sockets: self.numConns
					});
				}
				if (args.callback) {
					args.http_code = 0;
					args.http_status = "Socket Error";
					self.finishRequest(args);
				}
			} );
			
			socket.on('close', function() {
				// socket has closed
				if (socket._pixl_data.prelim_timer) {
					clearTimeout( socket._pixl_data.prelim_timer );
					delete socket._pixl_data.prelim_timer;
				}
				var now = (new Date()).getTime();
				self.logDebug(8, "HTTP connection has closed: " + id, {
					ip: ip,
					port: port,
					total_elapsed: now - socket._pixl_data.time_start,
					num_requests: socket._pixl_data.num_requests,
					bytes_in: socket._pixl_data.bytes_in,
					bytes_out: socket._pixl_data.bytes_out
				});
				delete self.conns[ id ];
				self.numConns--;
				socket._pixl_data.aborted = true;
			} );
		} );
		
		listener.on('clientError', function(err, socket) {
			// https://nodejs.org/api/http.html#http_event_clienterror
			if (!socket._pixl_data) socket._pixl_data = {};
			var args = socket._pixl_data.current || { request: {}, id: 'n/a' };
			var msg = err.message;
			
			if (err.errno && ErrNo.code[err.errno]) {
				msg = self.ucfirst(ErrNo.code[err.errno].description) + " (" + err.message + ")";
			}
			
			var err_args = {
				id: args.id,
				ip: socket.remoteAddress,
				ips: args.ips,
				port: port,
				state: args.state,
				method: args.request.method,
				uri: args.request.url,
				pending: self.queue.length(),
				active: self.queue.running(),
				sockets: self.numConns
			};
			if (self.config.get('log_socket_errors')) {
				self.logError(err.code || 'socket', "Client error: " + socket._pixl_data.id + ": " + msg, err_args);
			}
			else if (err.code != 'ECONNRESET') {
				self.logDebug(5, "Client error: " + socket._pixl_data.id + ": " + msg, err_args);
			}
			
			// do not try to write to socket if already closed
			if ((err.code != 'ECONNRESET') && socket.writable) {
				if (err.code == 'HPE_INVALID_METHOD') socket.destroy();
				else socket.end('HTTP/1.1 400 Bad Request\r\n\r\n');
			}
			socket._pixl_data.aborted = true;
			
			if (args.callback) {
				args.http_code = 0;
				args.http_status = "Socket Error";
				self.finishRequest(args);
			}
		});
		
		listener.once('error', function(err) {
			// fatal startup error on HTTP server, probably EADDRINUSE
			self.logError('startup', "Failed to start HTTP listener on port: " + port + ": " + err.message);
			return callback(err);
		} );
		
		var listen_opts = { port: port };
		if (bind_addr) listen_opts.host = bind_addr;
		
		listener.listen( listen_opts, function(err) {
			if (err) {
				self.logError('startup', "Failed to start HTTP listener on port: " + port + ": " + err.message);
				return callback(err);
			}
			var info = listener.address();
			self.logDebug(3, "Now listening for HTTP connections", info);
			if (!port) {
				port = info.port;
				self.config.set('port', port);
				self.logDebug(3, "Actual HTTP listener port chosen: " + port);
			}
			self.listeners.push(listener);
			
			// LEGACY HACK -- FOR CRONICLE VERSIONS UNDER v0.9.34
			self.http = listener;
			
			callback();
		} );
		
		// set idle socket timeout
		if (this.config.get('timeout')) {
			listener.setTimeout( this.config.get('timeout') * 1000 );
		}
		if (this.config.get('keep_alive_timeout')) {
			listener.keepAliveTimeout = this.config.get('keep_alive_timeout') * 1000;
		}
	}
	
};
```

## File: `lib/https.js`
```javascript
// Simple HTTP / HTTPS Web Server
// A component for the pixl-server daemon framework.
// Copyright (c) 2015 - 2025 Joseph Huckaby
// Released under the MIT License

const fs = require('fs');
const os = require('os');
const zlib = require('zlib');
const https = require('https');
const tls = require('tls');
const async = require('async');
const Formidable = require('formidable');
const Querystring = require('querystring');
const ErrNo = require('errno');
const StreamMeter = require("stream-meter");
const Class = require("class-plus");
const Component = require("pixl-server/component");
const Perf = require('pixl-perf');
const ACL = require('pixl-acl');

module.exports = class HTTP2 {
	
	setupHTTPS() {
		// load certs and setup monitoring
		// this is called only once, even if we have multiple ssl listeners
		this.reloadCert();
		
		// monitor files for changes
		this.server.on('tick', this.monitorCert.bind(this));
	}
	
	reloadCert() {
		// reload certs and secure context
		var self = this;
		var mgr = {
			files: {
				cert: this.config.get('https_cert_file'),
				key: this.config.get('https_key_file')
			},
			opts: {
				cert: fs.readFileSync( this.config.get('https_cert_file') ),
				key: fs.readFileSync( this.config.get('https_key_file') )
			},
			mods: {
				cert: fs.statSync(this.config.get('https_cert_file')).mtimeMs,
				key: fs.statSync(this.config.get('https_key_file')).mtimeMs
			},
			lastCheck: Date.now()
		};
		
		if (this.config.get('https_ca_file')) {
			// optional chain.pem or the like
			mgr.files.ca = this.config.get('https_ca_file');
			mgr.opts.ca = fs.readFileSync( this.config.get('https_ca_file') );
			mgr.mods.ca = fs.statSync(this.config.get('https_ca_file')).mtimeMs;
		}
		
		this.logDebug(3, "Loading SSL cert", mgr.files);
		
		// save mgr for later use
		// also, only assign this at the very end in case a reload crashes
		this.certMgr = mgr;
	}
	
	monitorCert() {
		// keep track of cert changes on disk
		var self = this;
		var mgr = this.certMgr;
		
		// every N seconds
		var now = Date.now();
		if (now - mgr.lastCheck < this.config.get('https_cert_poll_ms')) return;
		mgr.lastCheck = now;
		
		// stat files async as to not stall the event loop
		var mods = {};
		async.eachSeries( Object.keys(mgr.files),
			function(key, callback) {
				fs.stat( mgr.files[key], function(err, stats) {
					mods[key] = stats ? stats.mtimeMs : 0;
					callback();
				} );
			},
			function() {
				// did anything change?
				var changed = false;
				for (var key in mgr.files) {
					if (mods[key] && (mgr.mods[key] != mods[key])) changed = true;
				}
				if (!changed) return;
				
				// reload now!
				self.logDebug(3, "SSL cert has changed on disk, reloading now");
				
				// reloading is rare, so we can do it with sync calls
				// however, catch error here so a bad file doesn't bring down the whole server
				try { 
					self.reloadCert();
					
					// now infuse the new certs into all applicable listeners
					self.listeners.forEach( function(listener) {
						if (listener.setSecureContext) listener.setSecureContext( self.certMgr.opts );
					} );
					
					self.logDebug(3, "SSL cert reload complete");
				}
				catch (err) {
					self.logError('cert', "Failed to reload SSL cert: " + err);
				}
			}
		); // eachSeries
	}
	
	startHTTPS(port, callback) {
		// start https server
		var self = this;
		var bind_addr = this.config.get('https_bind_address') || this.config.get('bind_address') || '';
		var max_conns = this.config.get('https_max_connections') || this.config.get('max_connections') || 0;
		var socket_prelim_timeout = self.config.get('https_socket_prelim_timeout') || self.config.get('socket_prelim_timeout') || 0;
		
		this.logDebug(2, "Starting HTTPS (SSL) server on port: " + port, bind_addr );
		
		var handler = function(request, response) {
			if (socket_prelim_timeout && request.socket._pixl_data.prelim_timer) {
				clearTimeout( request.socket._pixl_data.prelim_timer );
				delete request.socket._pixl_data.prelim_timer;
			}
			
			// add a flag in headers for downstream code to detect
			request.headers['ssl'] = 1;
			request.headers['https'] = 1;
			
			self.enqueueHTTPRequest( request, response );
		};
		
		var listener = https.createServer( self.certMgr.opts, handler );
		
		listener.on('secureConnection', function(socket) {
			var ip = socket.remoteAddress || '';
			
			if (max_conns && (self.numConns >= max_conns)) {
				// reached maximum concurrent connections, abort new ones
				self.logError('maxconns', "Maximum concurrent connections reached, denying request from: " + ip, { host: socket.servername || '', ip: ip, port: port, max: max_conns });
				socket.end();
				socket.unref();
				socket.destroy(); // hard close
				self.dumpAllRequests();
				return;
			}
			if (self.server.shut) {
				// server is shutting down, abort new connections
				self.logError('shutdown', "Server is shutting down, denying connection from: " + ip, { host: socket.servername || '', ip: ip, port: port});
				socket.end();
				socket.unref();
				socket.destroy(); // hard close
				return;
			}
			if (ip && self.aclBlacklist && self.aclBlacklist.check(ip)) {
				self.logError('blacklist', "IP is blacklisted, denying connection from: " + ip, { host: socket.servername || '', ip: ip, port: port });
				socket.end();
				socket.unref();
				socket.destroy(); // hard close
				return;
			}
			if (ip && self.aclWhitelist && !self.aclWhitelist.check(ip)) {
				self.logError('whitelist', "IP is not whitelisted, denying connection from: " + ip, { ip: ip, port: port });
				socket.end();
				socket.unref();
				socket.destroy(); // hard close
				return;
			}
			
			// SNI: check allow list at socket connect time
			if (self.httpsAllowHosts.length && !self.httpsAllowHosts.includes( ('' + socket.servername).toLowerCase() )) {
				self.logError('allowhosts', "SNI host not allowed: " + (socket.servername || 'n/a'), { host: socket.servername || '', ip: ip, port: port });
				socket.end();
				socket.unref();
				socket.destroy(); // hard close
				return;
			}
			
			var id = self.getNextId('cs');
			self.conns[ id ] = socket;
			self.numConns++;
			self.logDebug(8, "New incoming HTTPS (SSL) connection: " + id, { host: socket.servername || '', ip: ip, port: port, num_conns: self.numConns });
			
			// Disable the Nagle algorithm.
			socket.setNoDelay( true );
			
			// add our own metadata to socket
			socket._pixl_data = {
				id: id,
				port: port,
				proto: 'https',
				port: port,
				time_start: (new Date()).getTime(),
				num_requests: 0,
				bytes_in: 0,
				bytes_out: 0
			};
			
			// optional preliminary socket timeout for first request
			if (socket_prelim_timeout) {
				socket._pixl_data.prelim_timer = setTimeout( function() {
					delete socket._pixl_data.prelim_timer;
					var msg = "Socket preliminary timeout waiting for initial request (" + socket_prelim_timeout + " seconds)";
					var err_args = {
						ip: ip,
						port: port,
						pending: self.queue.length(),
						active: self.queue.running(),
						sockets: self.numConns
					};
					if (self.config.get('log_socket_errors')) {
						self.logError('socket', "Socket error: " + socket._pixl_data.id + ": " + msg, err_args);
					}
					else {
						self.logDebug(5, "Socket error: " + socket._pixl_data.id + ": " + msg, err_args);
					}
					
					socket._pixl_data.aborted = true;
					socket.end();
					socket.unref();
					socket.destroy(); // hard close
				}, socket_prelim_timeout * 1000 );
			} // socket_prelim_timeout
			
			self.emit('socket', socket);
			
			socket.on('error', function(err) {
				// client aborted connection?
				var args = socket._pixl_data.current || { request: {} };
				var msg = err.message;
				if (err.errno && ErrNo.code[err.errno]) {
					msg = self.ucfirst(ErrNo.code[err.errno].description) + " (" + err.message + ")";
				}
				if (self.config.get('log_socket_errors')) {
					self.logError(err.code || 'socket', "Socket error: " + id + ": " + msg, {
						ip: ip,
						ips: args.ips,
						port: port,
						state: args.state,
						method: args.request.method,
						uri: args.request.url,
						pending: self.queue.length(),
						active: self.queue.running(),
						sockets: self.numConns
					});
				}
				if (args.callback) {
					args.http_code = 0;
					args.http_status = "Socket Error";
					self.finishRequest(args);
				}
			} );
			
			socket.on('close', function() {
				// socket has closed
				if (socket._pixl_data.prelim_timer) {
					clearTimeout( socket._pixl_data.prelim_timer );
					delete socket._pixl_data.prelim_timer;
				}
				var now = (new Date()).getTime();
				self.logDebug(8, "HTTPS (SSL) connection has closed: " + id, {
					ip: ip,
					port: port,
					total_elapsed: now - socket._pixl_data.time_start,
					num_requests: socket._pixl_data.num_requests,
					bytes_in: socket._pixl_data.bytes_in,
					bytes_out: socket._pixl_data.bytes_out
				});
				delete self.conns[ id ];
				self.numConns--;
				socket._pixl_data.aborted = true;
			} );
		} );
		
		listener.on('clientError', function(err, socket) {
			// https://nodejs.org/api/http.html#http_event_clienterror
			if (!socket._pixl_data) socket._pixl_data = {};
			var args = socket._pixl_data.current || { request: {}, id: 'n/a' };
			var msg = err.message;
			
			if (err.errno && ErrNo.code[err.errno]) {
				msg = self.ucfirst(ErrNo.code[err.errno].description) + " (" + err.message + ")";
			}
			
			var err_args = {
				id: args.id,
				ip: socket.remoteAddress,
				ips: args.ips,
				port: port,
				state: args.state,
				method: args.request.method,
				uri: args.request.url,
				pending: self.queue.length(),
				active: self.queue.running(),
				sockets: self.numConns
			};
			if (self.config.get('log_socket_errors')) {
				self.logError(err.code || 'socket', "Client error: " + socket._pixl_data.id + ": " + msg, err_args);
			}
			else if (err.code != 'ECONNRESET') {
				self.logDebug(5, "Client error: " + socket._pixl_data.id + ": " + msg, err_args);
			}
			
			// do not try to write to socket if already closed
			if ((err.code != 'ECONNRESET') && socket.writable) {
				if (err.code == 'HPE_INVALID_METHOD') socket.destroy();
				else socket.end('HTTP/1.1 400 Bad Request\r\n\r\n');
			}
			socket._pixl_data.aborted = true;
			
			if (args.callback) {
				args.http_code = 0;
				args.http_status = "Socket Error";
				self.finishRequest(args);
			}
		});
		
		listener.once('error', function(err) {
			// fatal startup error on HTTPS server, probably EADDRINUSE
			self.logError('startup', "Failed to start HTTPS listener on port: " + port + ": " + err.message);
			return callback(err);
		} );
		
		var listen_opts = { port: port };
		if (bind_addr) listen_opts.host = bind_addr;
		
		listener.listen( listen_opts, function(err) {
			if (err) {
				self.logError('startup', "Failed to start HTTPS listener on port: " + port + ": " + err.message);
				return callback(err);
			}
			var info = listener.address();
			self.logDebug(3, "Now listening for HTTPS connections", info);
			if (!port) {
				port = info.port;
				self.config.set('https_port', port);
				self.logDebug(3, "Actual HTTPS listener port chosen: " + port);
			}
			self.listeners.push(listener);
			
			// LEGACY HACK -- FOR CRONICLE VERSIONS UNDER v0.9.34
			self.https = listener;
			
			callback();
		} );
		
		// set idle socket timeout
		var timeout_sec = this.config.get('https_timeout') || this.config.get('timeout') || 0;
		if (timeout_sec) {
			listener.setTimeout( timeout_sec * 1000 );
		}
		if (this.config.get('https_keep_alive_timeout')) {
			listener.keepAliveTimeout = this.config.get('https_keep_alive_timeout') * 1000;
		}
		else if (this.config.get('keep_alive_timeout')) {
			listener.keepAliveTimeout = this.config.get('keep_alive_timeout') * 1000;
		}
	}
	
};
```

## File: `lib/request.js`
```javascript
// Simple HTTP / HTTPS Web Server
// A component for the pixl-server daemon framework.
// Copyright (c) 2015 - 2021 Joseph Huckaby
// Released under the MIT License

const async = require('async');
const Formidable = require('formidable');
const Querystring = require('querystring');
const Perf = require('pixl-perf');
const Args = require('./args.js');

module.exports = class Request {

	enqueueHTTPRequest(request, response) {
		// enqueue request for handling as soon as concurrency limits allow
		var args = new Args({
			id: this.getNextId('r'),
			date: Date.now() / 1000,
			request: request,
			response: response,
			state: 'queued',
			perf: new Perf()
		});
		
		// take snapshot of req and socket counts at start of request, used by perf logger at end
		if (this.logPerfEnabled) {
			args._start = {
				pending: this.queue.length(),
				running: this.queue.running(),
				sockets: this.numConns
			};
		}
		
		args.perf.begin();
		
		var ips = args.ips = this.getAllClientIPs(request);
		var ip = args.ip = this.getPublicIP(ips);
		
		if (!request.socket.remoteAddress) {
			// weird situation: a request came in without a remoteAddress -- reject immediately
			this.logError(400, "No socket IP address -- rejecting request", 
				{ id: args.id, ips: ips, uri: request.url, headers: request.headers }
			);
			this.sendHTTPResponse( args, "400 Bad Request", {}, "" );
			return;
		}
		
		if (this.server.shut) {
			// server is shutting down, deny new requests
			this.logError(503, "Server is shutting down, denying request from: " + ip, 
				{ id: args.id, ips: ips, uri: request.url, headers: request.headers }
			);
			this.sendHTTPResponse( args, "503 Service Unavailable", {}, "503 Service Unavailable (server shutting down)" );
			return;
		}
		
		// socket ip was already checked against blacklist at connection time,
		// so here we only need to check the header IPs, if any
		if ((ips.length > 1) && this.aclBlacklist && this.aclBlacklist.checkAny( ips.slice(0, -1) )) {
			this.logError(403, "Forbidden: IP addresses blacklisted: " + ips.join(', '), {
				id: args.id,
				useragent: args.request.headers['user-agent'] || '',
				referrer: args.request.headers['referer'] || '',
				cookie: args.request.headers['cookie'] || '',
				url: this.getSelfURL(args.request, args.request.url) || args.request.url
			});
			this.sendHTTPResponse( args, 
				"403 Forbidden", 
				{ 'Content-Type': "text/html" }, 
				"403 Forbidden\n"
			);
			return;
		}
		
		// socket ip was already checked against whitelist at connection time,
		// so here we only need to check the header IPs, if any
		if ((ips.length > 1) && this.aclWhitelist && !this.aclWhitelist.checkAll( ips.slice(0, -1) )) {
			this.logError(403, "Forbidden: IP addresses not whitelisted: " + ips.join(', '), {
				id: args.id,
				useragent: args.request.headers['user-agent'] || '',
				referrer: args.request.headers['referer'] || '',
				cookie: args.request.headers['cookie'] || '',
				url: this.getSelfURL(args.request, args.request.url) || args.request.url
			});
			this.sendHTTPResponse( args, 
				"403 Forbidden", 
				{ 'Content-Type': "text/html" }, 
				"403 Forbidden\n"
			);
			return;
		}
		
		// custom host allow list
		if (this.allowHosts.length && !this.allowHosts.includes( ('' + request.headers['host']).toLowerCase().replace(/\:\d+$/, '') )) {
			this.logError(403, "Forbidden: Host not allowed: " + (request.headers['host'] || 'n/a'), {
				id: args.id,
				host: request.headers['host'] || '',
				useragent: request.headers['user-agent'] || '',
				referrer: request.headers['referer'] || '',
				cookie: request.headers['cookie'] || '',
				url: this.getSelfURL(request, request.url) || request.url
			});
			this.sendHTTPResponse( args, 
				"403 Forbidden", 
				{ 'Content-Type': "text/html" }, 
				"403 Forbidden\n"
			);
			return;
		}
		
		// allow special URIs to skip the line
		if (this.queueSkipMatch && request.url.match(this.queueSkipMatch)) {
			this.logDebug(8, "Bumping request to front of queue: " + request.url);
			this.requests[ args.id ] = args;
			args.perf.begin('queue');
			this.queue.unshift(args);
			return;
		}
		
		if (this.maxQueueActive && (this.queue.running() >= this.maxQueueActive)) {
			// queue is maxed out on active reqs, reject request immediately
			this.logError(429, "Queue is maxed out (" + this.queue.running() + " active reqs), denying new request from: " + ip, { 
				id: args.id,
				ips: ips, 
				uri: request.url, 
				headers: request.headers,
				pending: this.queue.length(),
				active: this.queue.running(),
				sockets: this.numConns
			});
			this.sendHTTPResponse( args, "429 Too Many Requests", {}, "429 Too Many Requests (queue active maxed out)" );
			this.dumpAllRequests();
			return;
		}
		
		if (this.maxQueueLength && (this.queue.length() >= this.maxQueueLength)) {
			// queue is maxed out on pending reqs, reject request immediately
			this.logError(429, "Queue is maxed out (" + this.queue.length() + " pending reqs), denying new request from: " + ip, { 
				id: args.id,
				ips: ips, 
				uri: request.url, 
				headers: request.headers,
				pending: this.queue.length(),
				active: this.queue.running(),
				sockets: this.numConns
			});
			this.sendHTTPResponse( args, "429 Too Many Requests", {}, "429 Too Many Requests (queue pending maxed out)" );
			this.dumpAllRequests();
			return;
		}
		
		this.requests[ args.id ] = args;
		
		args.perf.begin('queue');
		this.queue.push(args);
	}
	
	parseHTTPRequest(args, callback) {
		// handle raw http request
		// (async dequeue handler function)
		var self = this;
		var request = args.request;
		var ips = args.ips;
		var ip = args.ip;
		
		args.perf.end('queue');
		
		// all requests will end up in this callback here
		args.callback = function() {
			if (args.timer) { clearTimeout(args.timer); delete args.timer; }
			delete self.requests[ args.id ];
			callback();
		};
		
		// add timer for request timeout
		if (this.config.get('request_timeout')) {
			args.timer = setTimeout( function() {
				// request took too long
				delete args.timer;
				
				self.logError(408, "Request timed out: " + self.config.get('request_timeout') + " seconds", {
					id: args.id,
					socket: request.socket._pixl_data.id,
					ips: args.ips,
					url: self.getSelfURL(args.request, request.url) || request.url,
					state: args.state
				});
				
				self.sendHTTPResponse( args, 
					"408 Request Timeout", 
					{ 'Content-Type': "text/html" }, 
					"408 Request Timeout: " + self.config.get('request_timeout') + " seconds.\n"
				);
				
				self.deleteUploadTempFiles(args);
			}, this.config.get('request_timeout') * 1000 );
		}
		
		// check for early abort (client error)
		if (request.socket._pixl_data.aborted) {
			if (args.callback) {
				args.callback();
				delete args.callback;
			}
			return;
		}
		
		this.logDebug(8, "New HTTP request: " + request.method + " " + request.url + " (" + ips.join(', ') + ")", {
			id: args.id,
			socket: request.socket._pixl_data.id,
			version: request.httpVersion
		});
		this.logDebug(9, "Incoming HTTP Headers:", request.headers);
		
		// url rewrites
		for (var idx = 0, len = this.rewrites.length; idx < len; idx++) {
			var rewrite = this.rewrites[idx];
			if (request.url.match(rewrite.regexp)) {
				request.url = request.url.replace(rewrite.regexp, rewrite.url);
				this.logDebug(8, "URL rewritten to: " + request.url);
				if (rewrite.headers) {
					for (var key in rewrite.headers) {
						request.headers[key] = rewrite.headers[key];
					}
				}
				if (rewrite.last) idx = len;
			}
		}
		
		// detect front-end https
		if (!request.headers.ssl && this.ssl_header_detect) {
			for (var key in this.ssl_header_detect) {
				if (request.headers[key] && request.headers[key].match(this.ssl_header_detect[key])) {
					this.logDebug(9, "Detected front-end HTTPS request: " + key + ": " + request.headers[key]);
					request.headers.ssl = 1;
					request.headers.https = 1;
					break;
				}
			}
		}
		
		// parse query string
		var query = {};
		if (request.url.match(/\?(.+)$/)) {
			query = Querystring.parse( RegExp.$1 );
		}
		
		// optionally flatten query (latter prevails)
		if (this.config.get('flatten_query')) {
			for (var key in query) {
				if (typeof(query[key]) == 'object') query[key] = query[key].pop();
			}
		}
		
		// determine how to process request body
		var params = {};
		var files = {};
		
		// setup args for call to handler
		args.ip = ip;
		args.ips = ips;
		args.query = query;
		args.params = params;
		args.files = files;
		args.server = this;
		args.state = 'reading';
		
		if (this.server.shut) {
			// server is shutting down, deny new requests
			this.logError(503, "Server is shutting down, denying request from: " + ip, 
				{ id: args.id, ips: ips, uri: request.url, headers: request.headers }
			);
			this.sendHTTPResponse( args, "503 Service Unavailable", {}, "503 Service Unavailable (server shutting down)" );
			return;
		}
		
		args.perf.begin('read');
		
		// parse HTTP cookies, if present
		args.cookies = {};
		if (request.headers['cookie']) {
			var pairs = request.headers['cookie'].split(/\;\s*/);
			for (var idx = 0, len = pairs.length; idx < len; idx++) {
				if (pairs[idx].match(/^([^\=]+)\=(.*)$/)) {
					var key = RegExp.$1, value = RegExp.$2;
					try { args.cookies[ decodeURIComponent(key) ] = decodeURIComponent(value); }
					catch (err) { this.logError('cookie', "Malformed cookie header: " + pairs[idx] + ": " + err) }
				}
			} // foreach cookie
		} // headers.cookie
		
		// we have to guess at the http raw status + raw header size
		// as Node's http.js has already parsed it
		var raw_bytes_read = 0;
		raw_bytes_read += [request.method, request.url, 'HTTP/' + request.httpVersion + "\r\n"].join(' ').length;
		raw_bytes_read += request.rawHeaders.join("\r\n").length + 4; // CRLFx2
		args.perf.count('bytes_in', raw_bytes_read);
		
		// track current request in socket metadata
		request.socket._pixl_data.current = args;
		
		// post or get/head
		if ((request.method != 'HEAD') && (request.headers['content-length'] || request.headers['transfer-encoding'])) {
			var content_type = request.headers['content-type'] || '';
			var content_encoding = request.headers['content-encoding'] || '';
			
			if (content_type.match(/(multipart|urlencoded)/i) && !content_encoding) {
				// use formidable for the heavy lifting
				var form = Formidable.formidable({
					keepExtensions: true,
					maxFieldsSize: self.config.get('max_upload_size'),
					maxFileSize: self.config.get('max_upload_size'),
					uploadDir: self.config.get('temp_dir'),
					allowEmptyFiles: self.config.get('allow_empty_files') || false
				});
				
				form.onPart = function (part) {
					// Only treat as file if it actually has a filename
					if (!part.originalFilename) {
						// Force it to be processed as a field
						part.mimetype = null;
						this._handlePart(part);
						return;
					}
					// Real file upload
					this._handlePart(part);
				}; // onPart
				
				form.on('progress', function(bytesReceived, bytesExpected) {
					self.logDebug(9, "Upload progress: " + bytesReceived + " of " + (bytesExpected || '(Unknown)') + " bytes", {
						socket: request.socket._pixl_data.id
					});
					args.perf.count('bytes_in', bytesReceived);
				} );
				
				form.parse(request, function(err, _fields, _files) {
					args.perf.end('read');
					
					if (err) {
						self.logError(400, "Error processing data from: " + ip + ": " + request.url + ": " + (err.message || err), 
							{ id: args.id, ips: ips, uri: request.url, headers: request.headers }
						);
						self.sendHTTPResponse( args, "400 Bad Request", {}, "400 Bad Request" );
						return;
					}
					else {
						// restore original formidable v1 API for our fields and files
						args.params = {};
						for (var key in _fields) {
							args.params[key] = (_fields[key].length == 1) ? _fields[key][0] : _fields[key];
						}
						
						args.files = {};
						if (_files) {
							for (var key in _files) {
								var file = _files[key][0];
								args.files[key] = {
									path: file.filepath,
									type: file.mimetype,
									name: file.originalFilename,
									size: file.size,
									mtime: file.mtime || file.lastModifiedDate
								};
							}
						}
						
						self.filterHTTPRequest(args);
					}
				} );
			}
			else {
				// parse ourselves (i.e. raw json)
				var bytesMax = self.config.get('max_upload_size');
				var bytesExpected = request.headers['content-length'] || "(Unknown)";
				var total_bytes = 0;
				var chunks = [];
				
				request.on('data', function(chunk) {
					// receive data chunk
					chunks.push( chunk );
					total_bytes += chunk.length;
					args.perf.count('bytes_in', chunk.length);
					
					self.logDebug(9, "Upload progress: " + total_bytes + " of " + bytesExpected + " bytes", {
						socket: request.socket._pixl_data.id
					});
					if (total_bytes > bytesMax) {
						self.logError(413, "Error processing data from: " + ip + ": " + request.url + ": Max data size exceeded", 
							{ id: args.id, ips: ips, uri: request.url, headers: request.headers }
						);
						request.socket.end();
						
						// note: request ending here without a call to sendHTTPResponse, hence the args.callback is fired
						if (args.callback) {
							args.callback();
							delete args.callback;
						}
						return;
					}
				} );
				request.on('end', function() {
					// request body is complete
					var body = Buffer.concat(chunks, total_bytes);
					
					if (content_type.match(self.regexJSONContent) && !content_encoding) {
						// parse json
						try {
							args.params = JSON.parse( body.toString() );
						}
						catch (e) {
							self.logError(400, "Error processing data from: " + ip + ": " + request.url + ": Failed to parse JSON: " + e, 
								{ id: args.id, ips: ips, uri: request.url, headers: request.headers, body: body.toString() }
							);
							self.sendHTTPResponse( args, "400 Bad Request", {}, "400 Bad Request" );
							return;
						}
					}
					else {
						// raw post, no parse
						args.params.raw = body;
					}
					
					// now we can handle the full request
					args.perf.end('read');
					self.filterHTTPRequest(args);
				} );
			}
		} // post
		else {
			// non-post, i.e. get or head, handle right away
			args.perf.end('read');
			this.filterHTTPRequest(args);
		}
	}
	
	filterHTTPRequest(args) {
		// apply URL filters to request, if any, before calling handlers
		var self = this;
		
		// quick early exit: no filters, jump out now
		if (!this.uriFilters.length) return this.handleHTTPRequest(args);
		
		// see which filters need to be applied
		var uri = args.request.url.replace(/\?.*$/, '');
		var filters = [];
		
		for (var idx = 0, len = this.uriFilters.length; idx < len; idx++) {
			if (uri.match(this.uriFilters[idx].regexp)) filters.push( this.uriFilters[idx] );
		}
		
		// if no filters matched, another quick early exit
		if (!filters.length) return this.handleHTTPRequest(args);
		
		args.state = 'filtering';
		
		// use async to allow filters to run in sequence
		async.eachSeries( filters,
			function(filter, callback) {
				self.logDebug(8, "Invoking filter for request: " + args.request.method + ' ' + uri + ": " + filter.name, { id: args.id });
				
				args.perf.begin('filter');
				filter.callback( args, function() {
					// custom filter complete
					args.perf.end('filter');
					
					if ((arguments.length == 3) && (typeof(arguments[0]) == "string")) {
						// filter sent status, headers and body
						self.sendHTTPResponse( args, arguments[0], arguments[1], arguments[2] );
						return callback("ABORT");
					}
					else if (arguments[0] === true) {
						// true means filter sent the raw response itself
						self.logDebug(9, "Filter sent custom response");
						return callback("ABORT");
					}
					else if (arguments[0] === false) {
						// false means filter exited normally
						self.logDebug(9, "Filter passthru, continuing onward");
						return callback();
					}
					else {
						// unknown response
						self.sendHTTPResponse( args, 
							"500 Internal Server Error", 
							{ 'Content-Type': "text/html" }, 
							"500 Internal Server Error: URI filter " + filter.name + " returned unknown data type.\n"
						);
						return callback("ABORT");
					}
				} );
			},
			function(err) {
				// all filters complete
				// if a filter handled the response, we're done
				if (err === "ABORT") {
					self.deleteUploadTempFiles(args);
					if (args.callback) {
						args.callback();
						delete args.callback;
					}
					return;
				}
				
				// otherwise, proceed to handling the request proper (method / URI handlers)
				self.handleHTTPRequest(args);
			}
		); // eachSeries
	}
	
	handleHTTPRequest(args) {
		// determine if we have an API route
		var self = this;
		var uri = args.request.url;
		if (!this.config.get('full_uri_match')) uri = uri.replace(/\?.*$/, '');
		var handler = null;
		
		// handle redirects first
		for (var idx = 0, len = this.redirects.length; idx < len; idx++) {
			var redirect = this.redirects[idx];
			var matches = args.request.url.match(redirect.regexp);
			if (matches) {
				// redirect now
				var headers = redirect.headers || {};
				
				// allow regexp-style placeholder substitution in target url
				headers.Location = redirect.url.replace(/\$(\d+)/g, function(m_all, m_g1) { return matches[ parseInt(m_g1) ]; });
				
				this.logDebug(8, "Redirecting to URL: " + headers.Location);
				this.sendHTTPResponse( args, redirect.status || "302 Found", headers, null );
				this.deleteUploadTempFiles(args);
				return;
			} // matched
		} // foreach redirect
		
		args.state = 'processing';
		args.perf.begin('process');
		
		// check method handlers first, e.g. OPTIONS
		for (var idx = 0, len = this.methodHandlers.length; idx < len; idx++) {
			if (this.methodHandlers[idx].method && (this.methodHandlers[idx].method == args.request.method)) {
				handler = this.methodHandlers[idx];
				idx = len;
			}
		}
		
		// only check URI handlers if no method handler matched
		if (!handler) {
			for (var idx = 0, len = this.uriHandlers.length; idx < len; idx++) {
				var matches = uri.match(this.uriHandlers[idx].regexp);
				if (matches) {
					args.matches = matches;
					handler = this.uriHandlers[idx];
					idx = len;
				}
			}
		}
		
		if (handler) {
			this.logDebug(6, "Invoking handler for request: " + args.request.method + ' ' + uri + ": " + handler.name, { id: args.id });
			
			// Check ACL here
			if (handler.acl) {
				if (handler.acl.checkAll(args.ips)) {
					// yay!
					this.logDebug(9, "ACL allowed request", args.ips);
				}
				else {
					// nope
					this.logError(403, "Forbidden: IP addresses rejected by ACL: " + args.ips.join(', '), {
						id: args.id,
						acl: handler.acl.toString(),
						useragent: args.request.headers['user-agent'] || '',
						referrer: args.request.headers['referer'] || '',
						cookie: args.request.headers['cookie'] || '',
						url: this.getSelfURL(args.request, args.request.url) || args.request.url
					});
					
					args.perf.end('process');
					
					this.sendHTTPResponse( args, 
						"403 Forbidden", 
						{ 'Content-Type': "text/html" }, 
						"403 Forbidden: ACL disallowed request.\n"
					);
					
					this.deleteUploadTempFiles(args);
					return;
				} // not allowed
			} // acl check
			
			handler.callback( args, function() {
				// custom handler complete, send response
				if ((arguments.length == 3) && (typeof(arguments[0]) == "string")) {
					// handler sent status, headers and body
					args.perf.end('process');
					self.sendHTTPResponse( args, arguments[0], arguments[1], arguments[2] );
				}
				else if (arguments[0] === true) {
					// true means handler sent the raw response itself
					args.resp_headers = { ...args.response.getHeaders() };
					
					if (args.request.socket.destroyed) {
						args.http_code = 0;
						args.http_status = 'Socket Closed';
						self.logDebug(9, "Socket closed during custom response");
					}
					else {
						args.http_code = args.response.statusCode || 0;
						args.http_status = args.response.statusMessage || '';
						self.logDebug(9, "Handler sent custom response", {
							statusCode: args.http_code,
							statusMessage: args.http_status,
							headers: args.resp_headers
						});
					}
					
					self.finishRequest(args);
				}
				else if (arguments[0] === false) {
					// false means handler did nothing, fall back to static
					self.logDebug(9, "Handler declined, falling back to static file");
					args.perf.end('process');
					self.sendStaticResponse( args );
				}
				else if (typeof(arguments[0]) == "object") {
					// REST-style JSON response
					var json = arguments[0];
					self.logDebug(10, "API Response JSON:", json);
					args.perf.end('process');
					
					var status = arguments[1] || "200 OK";
					var headers = arguments[2] || {};
					var payload = args.query.pretty ? JSON.stringify(json, null, "\t") : JSON.stringify(json);
					
					if (args.query.format && (args.query.format.match(/html/i)) && args.query.callback && self.config.get('legacy_callback_support')) {
						// old school IFRAME style response
						headers['Content-Type'] = "text/html";
						self.sendHTTPResponse( args, 
							status, 
							headers, 
							'<html><head><script>' + 
								args.query.callback + "(" + payload + ");\n" + 
								'</script></head><body>&nbsp;</body></html>' + "\n"
						);
					}
					else if (args.query.callback && self.config.get('legacy_callback_support')) {
						// JSON with JS callback wrapper
						headers['Content-Type'] = "text/javascript";
						self.sendHTTPResponse( args, 
							status, 
							headers, 
							args.query.callback + "(" + payload + ");\n"
						);
					}
					else {
						// pure json
						headers['Content-Type'] = "application/json";
						self.sendHTTPResponse( args, 
							status, 
							headers, 
							payload + "\n"
						);
					} // pure json
				} // json response
				else {
					// unknown response
					self.sendHTTPResponse( args, 
						"500 Internal Server Error", 
						{ 'Content-Type': "text/html" }, 
						"500 Internal Server Error: URI handler " + handler.name + " returned unknown data type.\n"
					);
				}
				
				// delete temp files
				self.deleteUploadTempFiles(args);
			} );
		} // uri handler
		else {
			// no uri handler, serve static file instead
			args.perf.end('process');
			this.sendStaticResponse( args );
			
			// delete temp files
			this.deleteUploadTempFiles(args);
		}
	}
	
};
```

## File: `lib/response.js`
```javascript
// Simple HTTP / HTTPS Web Server
// A component for the pixl-server daemon framework.
// Copyright (c) 2015 - 2021 Joseph Huckaby
// Released under the MIT License

const zlib = require('zlib');
const StreamMeter = require("stream-meter");

module.exports = class Response {
	
	sendHTTPResponse(args, status, headers, body) {
		// send http response
		var self = this;
		var request = args.request;
		var response = args.response;
		
		// copy headers object so we don't clobber user data
		if (headers) headers = Object.assign({}, headers);
		else headers = {};
		
		// in case the URI handler called sendHTTPResponse() directly, end the process metric
		if (args.perf && args.perf.perf.process && !args.perf.perf.process.end) args.perf.end('process');
		
		// check for destroyed socket
		if (args.request.socket.destroyed) {
			var socket_data = args.request.socket._pixl_data;
			delete socket_data.current;
			socket_data.total_elapsed = (new Date()).getTime() - socket_data.time_start;
			socket_data.url = this.getSelfURL(request, request.url) || request.url;
			socket_data.ips = args.ips;
			socket_data.req_id = args.id;
			
			if (this.config.get('log_socket_errors')) {
				this.logError('socket', "Socket closed unexpectedly: " + socket_data.id, socket_data);
			}
			else {
				this.logDebug(9, "Socket closed unexpectedly: " + socket_data.id, socket_data);
			}
			
			args.http_code = 0;
			args.http_status = "Socket Closed";
			this.finishRequest(args);
			
			// destroy stream if appliable (prevents filehandle leak)
			if (body && body.pipe && body.destroy) body.destroy();
			
			return;
		} // destroyed socket
		
		// catch double-callback
		if (args.state == 'writing') {
			this.logError('write', "Warning: Double call to sendHTTPResponse on same request detected.  Aborting second call.");
			return;
		}
		
		args.state = 'writing';
		
		// merge in default response headers
		var default_headers = this.config.get('response_headers') || null;
		if (default_headers) {
			for (var key in default_headers) {
				if (typeof(headers[key]) == 'undefined') headers[key] = default_headers[key];
			}
		}
		if (typeof(headers['Server']) == 'undefined') {
			headers['Server'] = this.config.get('server_signature') || this.__name;
		}
		
		// possibly overwrite 'Connection' header for KA closure
		this.manageKeepAliveResponse(args, headers);
		
		// parse code and status
		var http_code = 200;
		var http_status = "OK";
		
		if (status.match(/^(\d+)\s+(.+)$/)) {
			http_code = parseInt( RegExp.$1 );
			http_status = RegExp.$2;
		}
		else if (this.responseCodes[status]) {
			http_code = parseInt(status);
			http_status = this.responseCodes[status];
		}
		
		args.http_code = http_code;
		args.http_status = http_status;
		
		// merge in conditional headers based on response code
		var code_headers = this.config.get('code_response_headers');
		if (code_headers && (http_code in code_headers)) {
			this.logDebug(9, "Injecting custom response headers for HTTP code: " + http_code, code_headers[http_code]);
			for (var key in code_headers[http_code]) {
				headers[key] = code_headers[http_code][key];
			}
		}
		
		// merge in conditional headers based on URI
		var uri = request.url;
		if (!this.config.get('full_uri_match')) uri = uri.replace(/\?.*$/, '');
		
		this.uriResponseHeaders.forEach( function(item) {
			if (!uri.match(item.regexp)) return;
			self.logDebug(9, "Injecting custom response headers for URI match: " + item.regexp, item.headers);
			
			for (var key in item.headers) {
				headers[key] = item.headers[key];
			}
		} );
		
		// use duck typing to see if we have a stream, buffer or string
		var is_stream = (body && body.pipe);
		var is_buffer = (body && body.fill);
		var is_string = (body && !is_stream && !is_buffer);
		
		// if string, convert to buffer so content length is correct (unicode)
		if (is_string) {
			body = Buffer.from(body);
		}
		
		// set content-type if not already set
		if (body && !is_stream && (typeof(headers['Content-Length']) == 'undefined')) {
			headers['Content-Length'] = body.length;
		}
		
		// copy stuff into args for detail logging
		if (this.logRequestDetails) {
			if (headers['Content-Encoding']) args.resp_body = Buffer.from("(Compressed)"); else args.resp_body = body;
			args.resp_headers = headers;
		}
		
		// track stream bytes, if applicable
		var meter = null;
		
		response.on('finish', function() {
			// response actually completed writing
			self.logDebug(9, "Response finished writing to socket", { id: args.id });
			
			// guess number of bytes in response header, minus data payload
			args.perf.count('bytes_out', ("HTTP " + args.http_code + " OK\r\n").length);
			for (var key in headers) {
				args.perf.count('bytes_out', (key + ": " + headers[key] + "\r\n").length);
			}
			args.perf.count('bytes_out', 4); // CRLFx2
			
			// add metered bytes if streamed
			if (meter) args.perf.count('bytes_out', meter.bytes || 0);
			
			// done writing
			args.perf.end('write');
			self.finishRequest(args);
		} );
		
		response.on('close', function() {
			if (args.callback) { 
				// socket closed during active response
				if (self.config.get('log_socket_errors')) {
					self.logError('socket', "Socket connection terminated unexpectedly during response", {
						id: args.id,
						ips: args.ips,
						useragent: request.headers['user-agent'] || '',
						referrer: request.headers['referer'] || '',
						cookie: request.headers['cookie'] || '',
						url: self.getSelfURL(request, request.url) || request.url
					});
				}
				
				args.http_code = 0;
				args.http_status = "Socket Closed";
				self.finishRequest(args);
			}
		});
		
		// handle stream errors (abort response)
		if (is_stream) {
			body.on('error', function(err) {
				self.logError('stream', "Stream error serving response: " + request.url + ": " + err.message, {
					id: args.id,
					ips: args.ips,
					useragent: request.headers['user-agent'] || '',
					referrer: request.headers['referer'] || '',
					cookie: request.headers['cookie'] || '',
					url: self.getSelfURL(request, request.url) || request.url
				});
				
				args.http_code = 500;
				args.http_status = "Internal Server Error";
				args.perf.count('errors', 1);
				
				body.unpipe();
				response.end();
			});
		}
		
		// see if handler has requested gzip, or auto-detect it
		var do_compress = headers['X-Compress'] || headers['x-compress'] || false;
		if (!do_compress) {
			do_compress = !!(
				this.compressText && 
				headers['Content-Type'] && 
				headers['Content-Type'].match(this.regexTextContent)
			);
		}
		
		// auto-gzip response based on content type
		if (body && 
			(http_code == 200) && 
			do_compress && 
			!headers['Content-Encoding'] && // do not encode if already encoded
			args.request && 
			args.request.headers['accept-encoding'] && 
			args.request.headers['accept-encoding'].match(self.acceptEncodingMatch)) {
			
			// prep encoding compression
			var compressor = null;
			var zlib_opts = null;
			var zlib_func = '';
			var accept_encoding = args.request.headers['accept-encoding'].toLowerCase();
			
			if (self.hasBrotli && accept_encoding.match(/\b(br)\b/)) {
				// prefer brotli first, if supported by Node.js
				zlib_func = 'brotliCompress';
				zlib_opts = self.config.get('brotli_opts') || {};
				headers['Content-Encoding'] = 'br';
				if (is_stream) compressor = zlib.createBrotliCompress( zlib_opts );
			}
			else if (accept_encoding.match(/\b(gzip)\b/)) {
				// prefer gzip second
				zlib_func = 'gzip';
				zlib_opts = self.config.get('gzip_opts') || {};
				headers['Content-Encoding'] = 'gzip';
				if (is_stream) compressor = zlib.createGzip( zlib_opts );
			}
			else if (accept_encoding.match(/\b(deflate)\b/)) {
				// prefer deflate third
				zlib_func = 'deflate';
				zlib_opts = self.config.get('gzip_opts') || {}; // yes, same opts as gzip
				headers['Content-Encoding'] = 'deflate';
				if (is_stream) compressor = zlib.createDeflate( zlib_opts );
			}
			
			if (is_stream) {
				// send response as stream pipe
				delete headers['Content-Length'];
				self.logDebug(9, "Sending compressed streaming HTTP response with " + zlib_func + ": " + status, headers);
				args.perf.begin('write');
				
				if (self.writeHead( args, http_code, http_status, headers )) {
					meter = new StreamMeter();
					body.pipe( compressor ).pipe( meter ).pipe( response );
					self.logDebug(9, "Request complete");
				}
			}
			else {
				// compress and send response as buffer
				args.perf.begin('encode');
				zlib[ zlib_func ]( body, zlib_opts, function(err, data) {
					args.perf.end('encode');
					args.perf.begin('write');
					if (err) {
						// should never happen
						self.logError('zlib', "Failed to compress content with " + zlib_func + ": " + err);
						data = body;
					}
					else {
						// no error
						body = null; // free up memory
						self.logDebug(9, "Compressed text output with " + zlib_func + ": " + headers['Content-Length'] + " bytes down to: " + data.length + " bytes");
						headers['Content-Length'] = data.length;
					}
					
					self.logDebug(9, "Sending compressed HTTP response with " + zlib_func + ": " + status, headers);
					
					// send data
					if (self.writeHead( args, http_code, http_status, headers )) {
						response.write( data );
						response.end();
						
						args.perf.count('bytes_out', data.length);
						self.logDebug(9, "Request complete");
					}
				}); // zlib
			} // buffer or string
		} // compress
		else {
			// no compression
			args.perf.begin('write');
			
			if (is_stream) {
				this.logDebug(9, "Sending streaming HTTP response: " + status, headers);
				
				if (self.writeHead( args, http_code, http_status, headers )) {
					meter = new StreamMeter();
					body.pipe( meter ).pipe( response );
				}
			}
			else {
				this.logDebug(9, "Sending HTTP response: " + status, headers);
				
				// send data
				if (self.writeHead( args, http_code, http_status, headers )) {
					if (body) {
						response.write( body );
						args.perf.count('bytes_out', body.length);
					}
					response.end();
				}
			}
			this.logDebug(9, "Request complete", { id: args.id });
		}
	}
	
	writeHead(args, http_code, http_status, headers) {
		// wrap call to response.writeHead(), as it can throw
		var request = args.request;
		var response = args.response;
		
		if (headers && this.config.get('clean_headers')) {
			// prevent bad characters in headers, which can crash node's writeHead() call
			for (var key in headers) {
				if (typeof(headers[key]) == 'object') {
					for (var idx = 0, len = headers[key].length; idx < len; idx++) {
						headers[key][idx] = headers[key][idx].toString().replace(this.badHeaderCharPattern, '');
					}
				}
				else {
					headers[key] = headers[key].toString().replace(this.badHeaderCharPattern, '');
				}
			}
		}
		
		response.writeHead( http_code, http_status, headers || {} );
		return true;
	}
	
	finishRequest(args) {
		// finish up request tracking
		if (args.requestFinished) return;
		args.requestFinished = true;
		
		args.perf.count('num_requests', 1);
		args.perf.end();
		
		var socket_data = args.request.socket._pixl_data;
		var metrics = args.perf.metrics();
		this.emit('metrics', metrics, args);
		
		this.logDebug(9, "Request performance metrics:", metrics);
		
		// write to access log
		if (this.logRequests && args.request.url.match(this.regexLogRequests)) {
			var data = {
				id: args.id,
				method: args.request.method,
				proto: args.request.headers['ssl'] ? 'https' : socket_data.proto,
				ip: args.ip,
				ips: args.ips,
				port: socket_data.port,
				socket: socket_data.id,
				perf: metrics
			};
			
			if (this.logRequestDetails) {
				// extra transaction log details
				data.files = args.files || {};
				data.headers = args.request.headers || {};
				data.cookies = args.cookies || {};
				data.query = args.query || {};
				data.params = Object.assign( {}, args.params || {} );
				
				// special handling for raw request body
				if (data.params.raw && data.params.raw.buffer && data.params.raw.toString) {
					if (args.request.headers['content-type'] && args.request.headers['content-type'].match(/(text|javascript|json|xml)/) && (data.params.raw.length <= this.logRequestBodyMax)) {
						data.params.raw = data.params.raw.toString('utf8');
					}
					else data.params.raw = '(Buffer)';
				}
				
				// include details on response as well
				data.response = {
					code: args.http_code,
					status: args.http_status,
					headers: {}
				};
				
				// convert header keys to lower-case
				if (args.resp_headers) {
					for (var key in args.resp_headers) {
						data.response.headers[ key.toLowerCase() ] = args.resp_headers[key];
					}
				}
				
				// special handling for stream and buffer responses
				if (args.resp_body && args.resp_body.pipe) {
					data.response.raw = '(Stream)';
				}
				else if (args.resp_body && args.resp_body.buffer && args.resp_body.toString) {
					if (data.response.headers && data.response.headers['content-type'] && data.response.headers['content-type'].match(/(text|javascript|json|xml)/) && (args.resp_body.length <= this.logRequestBodyMax)) {
						data.response.raw = args.resp_body.toString('utf8');
					}
					else data.response.raw = '(Buffer)';
				}
				
				// cleanup
				delete args.resp_body;
				delete args.resp_headers;
			}
			else {
				// standard transaction log
				data.host = args.request.headers['host'] || '';
				data.ua = args.request.headers['user-agent'] || '';
			}
			
			this.logTransaction( 'HTTP ' + args.http_code + ' ' + args.http_status, args.request.url, data );
		}
		
		// optional threshold-based perf log
		if (this.logPerfEnabled && (metrics.perf.total >= this.logPerfThreshold)) {
			var epoch = (Date.now() - metrics.perf.total) / 1000;
			var log_data = {
				id: args.id,
				proto: args.request.headers['ssl'] ? 'https' : socket_data.proto,
				ips: args.ips,
				host: args.request.headers['host'] || '',
				ua: args.request.headers['user-agent'] || '',
				perf: metrics,
				pending: args._start.pending,
				running: args._start.running,
				sockets: args._start.sockets
			};
			if (this.logPerfReport) {
				var report = process.report.getReport();
				if (Array.isArray(this.logPerfReport)) {
					log_data.report = {};
					this.logPerfReport.forEach( function(key) {
						if (key in report) log_data.report[key] = report[key];
					} );
				}
				else log_data.report = report;
			}
			this.logger.print({
				now: epoch, // retroactive time (start of request)
				category: 'perf', 
				code: args.http_code + ' ' + args.http_status, 
				msg: args.request.url,
				data: log_data
			});
		}
		
		// keep a list of the most recent N requests
		if (this.keepRecentRequests) {
			this.recent.unshift({
				id: args.id,
				when: (new Date()).getTime() / 1000,
				proto: args.request.headers['ssl'] ? 'https' : socket_data.proto,
				port: socket_data.port,
				code: args.http_code,
				status: args.http_status,
				method: args.request.method,
				uri: args.request.url,
				ip: args.ip,
				ips: args.ips,
				host: args.request.headers['host'] || '',
				ua: args.request.headers['user-agent'] || '',
				perf: metrics
			});
			if (this.recent.length > this.keepRecentRequests) this.recent.pop();
		}
		
		// add metrics to socket
		socket_data.num_requests++;
		socket_data.bytes_in += metrics.counters.bytes_in || 0;
		socket_data.bytes_out += metrics.counters.bytes_out || 0;
		
		// add metrics to stats system
		var stats = this.stats.current;
		
		for (var key in metrics.perf) {
			var elapsed = metrics.perf[key];
			if (!stats[key]) {
				stats[key] = {
					'st': 'mma', // stat type: "min max avg"
					'min': elapsed,
					'max': elapsed,
					'total': elapsed,
					'count': 1
				};
			}
			else {
				var stat = stats[key];
				if (elapsed < stat.min) stat.min = elapsed;
				else if (elapsed > stat.max) stat.max = elapsed;
				stat.total += elapsed;
				stat.count++;
			}
		}
		
		for (var key in metrics.counters) {
			var amount = metrics.counters[key];
			if (!stats[key]) stats[key] = 0;
			stats[key] += amount;
		}
		
		// remove reference to current request
		delete socket_data.current;
		
		// Handle HTTP Keep-Alives
		var request = args.request;
		
		// only do this if socket is still open
		if (args.http_code != 0) switch (this.keepAlives) {
			case 0:
			case 'close':
				// KA disabled, always close
				this.logDebug(9, "Closing socket: " + socket_data.id);
				request.socket.end(); // close nicely
			break;
			
			case 1:
			case 'request':
				// KA enabled only if client explicitly requests it
				if (!request.headers.connection || !request.headers.connection.match(/keep\-alive/i)) {
					// close socket
					this.logDebug(9, "Closing socket: " + socket_data.id);
					request.socket.end(); // close nicely
				}
				else {
					this.logDebug(9, "Keeping socket open for keep-alives: " + socket_data.id);
				}
			break;
			
			case 2:
			case 'default':
				// KA enabled by default, only disable if client says close
				if (request.headers.connection && request.headers.connection.match(/close/i)) {
					this.logDebug(9, "Closing socket: " + socket_data.id);
					request.socket.end(); // close nicely
				}
				else {
					this.logDebug(9, "Keeping socket open for keep-alives: " + socket_data.id);
				}
			break;
		} // switch
		
		// fire final request callback (queue)
		if (args.callback) {
			args.callback();
			delete args.callback;
		}
	}
	
	manageKeepAliveResponse(args, headers) {
		// massage outgoing headers for keep-alive requests
		// possibly override response 'Connection' header, if we want the client to close
		var request = args.request;
		var socket_data = request.socket._pixl_data || { num_requests: 0 };
		
		switch (this.keepAlives) {
			case 0:
			case 'close':
				// KA disabled, always close
				headers['Connection'] = 'close';
			break;
			
			case 1:
			case 'request':
				// KA enabled only if client explicitly requests it
				if (!request.headers.connection || !request.headers.connection.match(/keep\-alive/i)) {
					headers['Connection'] = 'close';
				}
				else if (this.maxReqsPerConn && (socket_data.num_requests >= this.maxReqsPerConn - 1)) {
					this.logDebug(8, "Closing socket after " + this.maxReqsPerConn + " keep-alive requests: " + socket_data.id);
					headers['Connection'] = 'close';
				}
				else if (this.server.shut) {
					this.logDebug(8, "Closing socket due to server shutting down: " + socket_data.id);
					headers['Connection'] = 'close';
				}
			break;
			
			case 2:
			case 'default':
				// KA enabled by default, only disable if client says close
				if (request.headers.connection && request.headers.connection.match(/close/i)) {
					headers['Connection'] = 'close';
				}
				else if (this.maxReqsPerConn && (socket_data.num_requests >= this.maxReqsPerConn - 1)) {
					this.logDebug(8, "Closing socket after " + this.maxReqsPerConn + " keep-alive requests: " + socket_data.id);
					headers['Connection'] = 'close';
				}
				else if (this.server.shut) {
					this.logDebug(8, "Closing socket due to server shutting down: " + socket_data.id);
					headers['Connection'] = 'close';
				}
			break;
		} // switch
	}
	
};
```

## File: `lib/static.js`
```javascript
// Simple HTTP / HTTPS Web Server
// A component for the pixl-server daemon framework.
// Copyright (c) 2015 - 2021 Joseph Huckaby
// Released under the MIT License

const fs = require('fs');
const Path = require('path');
const async = require('async');
const mime = require('mime');

module.exports = class Static {
	
	sendStaticResponse(args) {
		// serve static file for URI
		var self = this;
		var request = args.request;
		var response = args.response;
		var headers = {};
		
		// catch double-callback
		if (args.state == 'writing') {
			this.logError('write', "Warning: Double call to sendStaticResponse on same request detected.  Aborting second call.");
			return;
		}
		
		// convert URI to file path
		var file = '';
		if (args.internalFile) {
			file = args.internalFile;
			this.logDebug(9, "Serving static file for internal redirect: " + file);
		}
		else {
			var base_dir = Path.resolve( this.config.get('htdocs_dir') );
			file = Path.resolve( base_dir + request.url.replace(/\?.*$/, '').replace(/\/$/, '') );
			this.logDebug(9, "Serving static file for: " + args.request.url, { file });
			
			if (file.indexOf(base_dir) !== 0) {
				// trying to access file outside base -- just 404 it
				return self.sendHTTPResponse( args, 
					"404 Not Found", 
					{ 'Content-Type': "text/html" }, 
					"404 Not Found: " + request.url + "\n"
				);
			}
		}
		
		// determine format
		var http_status = "200 OK";
		var mime_type = mime.getType(file) || 'application/octet-stream';
		var file_stats = null;
		var is_dir = false;
		
		async.series([
			function(callback) {
				// first check if it's a directory, and if so, add /index.html
				fs.stat( file, function(err, stats) {
					if (err) return callback(err);
					file_stats = stats;
					
					if (stats.isDirectory()) {
						is_dir = true;
						file += '/' + self.config.get('static_index');
						mime_type = mime.getType(file) || 'application/octet-stream';
						self.logDebug(9, "Serving directory index: " + file);
						
						fs.stat( file, function(err, stats) {
							if (err) return callback(err);
							file_stats = stats;
							callback();
						}); // fs.stat
					}
					else callback();
				}); // fs.stat
			},
			function(callback) {
				// if mime is textish, check for gz file variant
				if (mime_type.match(self.regexTextContent) && request.headers['accept-encoding'] && request.headers['accept-encoding'].match(/\bgzip\b/i)) {
					var gz_file = file + '.gz';
					
					fs.stat( gz_file, function(err, stats) {
						if (err) return callback(); // non-fatal, fallback to non-gz
						
						// go for gz version
						file = gz_file;
						file_stats = stats;
						headers['Content-Encoding'] = 'gzip';
						self.logDebug(9, "Serving pre-gzipped version of file: " + file);
						callback();
					}); // fs.stat
				}
				else process.nextTick(callback);
			}
		],
		function(err) {
			if (err) {
				return self.sendHTTPResponse( args, 
					"404 Not Found", 
					{ 'Content-Type': "text/html" }, 
					"404 Not Found: " + request.url + "\n"
				);
			}
			
			// redirect for dir index without trailing slash
			if (is_dir && !request.url.match(/\/(\?|$)/)) {
				var new_url = self.getSelfURL( request, request.url.replace( /^(.+?)(\?.*)?$/, '$1/$2' ) );
				self.logDebug(9, "Redirecting for directory (adding trailing slash): " + new_url);
				return self.sendHTTPResponse( args, 
					"302 Found", 
					{ 'Location': new_url.replace(self.badHeaderCharPattern, '') }, 
					""
				);
			}
			
			// range request or nah
			var range = self.parseByteRange(request, file_stats);
			if (range) {
				headers['Content-Range'] = 'bytes ' + range.from + '-' + range.to + '/' + file_stats.size;
				http_status = "206 Partial Content";
				self.logDebug(9, "Serving partial file content: " + headers['Content-Range']);
			}
			else {
				range = { from: 0, to: file_stats.size - 1 };
			}
			
			// conditional get
			const file_mtime = file_stats.mtime.getTime();
			const file_etag = JSON.stringify([file_stats.ino, file_stats.size, file_mtime].join('-'));
			const req_etag = request.headers['if-none-match'];
			const req_mtime = Date.parse( request.headers['if-modified-since'] );
			
			if ((req_mtime || req_etag) && (!req_etag || (req_etag === file_etag)) && (!req_mtime || (req_mtime >= file_mtime))) {
				// file has not changed, send back 304
				return self.sendHTTPResponse( args, "304 Not Modified", {}, "" );
			}
			
			// standard headers
			headers['Etag'] = file_etag;
			headers['Last-Modified'] = (new Date(file_stats.mtime)).toUTCString();
			headers['Content-Type'] = mime_type;
			headers['Content-Length'] = (range.to - range.from) + 1;
			
			// cache-control
			var ttl = args.internalTTL || self.config.get('static_ttl') || 0;
			if (typeof(ttl) == 'number') headers['Cache-Control'] = "public, max-age=" + ttl;
			else headers['Cache-Control'] = ttl;
			
			// check for HEAD request
			if (request.method == 'HEAD') {
				return self.sendHTTPResponse( args, http_status, headers, "" );
			}
			
			// special response for 0-byte files
			if (!file_stats.size) {
				return self.sendHTTPResponse( args, http_status, headers, "" );
			}
			
			// open file stream
			var stream = fs.createReadStream( file, {
				start: range.from,
				end: range.to
			} );
			
			// send it
			self.sendHTTPResponse( args, http_status, headers, stream );
			
		}); // async.series
	}
	
	parseByteRange(req, stat) {
		// parse byte range header from request
		// Example header: Range: bytes=31-49
		const byteRange = {
			from: 0,
			to: 0
		}
		
		let rangeHeader = req.headers['range'];
		const flavor = 'bytes=';
		
		if (rangeHeader && rangeHeader.startsWith(flavor) && !rangeHeader.includes(',')) {
			// Parse
			rangeHeader = rangeHeader.substr(flavor.length).split('-');
			byteRange.from = parseInt(rangeHeader[0]);
			byteRange.to = parseInt(rangeHeader[1]);
			
			// Replace empty fields of differential requests by absolute values 
			if (isNaN(byteRange.from) && !isNaN(byteRange.to)) {
				byteRange.from = stat.size - byteRange.to;
				byteRange.to = stat.size ? stat.size - 1 : 0;
			} 
			else if (!isNaN(byteRange.from) && isNaN(byteRange.to)) {
				byteRange.to = stat.size ? stat.size - 1 : 0;
			}
			
			// General byte range validation
			if (!isNaN(byteRange.from) && !isNaN(byteRange.to) && (0 <= byteRange.from) && (byteRange.from <= byteRange.to) && (byteRange.to < stat.size)) {
				return byteRange;
			}
		}
		
		return null;
	}
	
};
```

## File: `test/index.html`
```html
<!DOCTYPE html>
<html>
<head>
	<title>Test</title>
</head>
<body>
	Test
</body>
</html>
```

## File: `test/robots.txt`
```
User-agent: *
Disallow: /
```

## File: `test/ssl.crt`
```
-----BEGIN CERTIFICATE-----
MIIDMjCCAhqgAwIBAgIJANQO8EFYRaZiMA0GCSqGSIb3DQEBBQUAMBoxGDAWBgNV
BAMTD3d3dy5leGFtcGxlLmNvbTAeFw0xMzA2MjUxNDMxMDFaFw0yMzA2MjMxNDMx
MDFaMBoxGDAWBgNVBAMTD3d3dy5leGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEB
BQADggEPADCCAQoCggEBANhUOPoivca6J5zWqqp3xkd/iTjE3ME7/36wTprNDIt4
VQpiQfMMUeE4UQadivNJJnzAsB/LtZs2T3h//InwhC+40bsmtj0DVqGadthr8x8l
tV15vfwztMQ5e1eU3u0oBQzS3o1sLplD8U88GeTAqamgQLG769kHbqqsxA/lYuAh
O3SRHxkpEgW5pC72lbsTqE8U6ipLry3S3wT1+4BCFC/gFtdg4ILjgqfPNAvzR72R
X+kdy2jJ5fAaE3C/ca8uRkN+rqt2QV5c1MP12UNn5OEQntMNrB6/91V3jfN3UEEF
s9hLZSstPIxYye2B7PkFlW3irR34HuDrSki0u0k4xIkCAwEAAaN7MHkwHQYDVR0O
BBYEFHb75UVd2UnNO2ml+y227nRujASpMEoGA1UdIwRDMEGAFHb75UVd2UnNO2ml
+y227nRujASpoR6kHDAaMRgwFgYDVQQDEw93d3cuZXhhbXBsZS5jb22CCQDUDvBB
WEWmYjAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUAA4IBAQDXiSZaNq0p0IQq
tttyaksuIITs7WYusXhZiMufO9rbIiQErCgTZuUE/DahIPQFKAUwTS6VQO9rkFTj
1nfDJe/SD9EoIco7gxe/9a/FiGi53uTlVq8F87clr87NCh+t8VMwLMO/43tsgl2U
A0kaExBo1roJwJcrADNsyCfSsB8n2y2n7Q8QOdJ0HOzHT0vvYUJZaOprV9dp+8Yj
+raVZRibPA+H4jUEBHk387knpUx5tWeJd+7RCA1pCcAU2b3lfcL6zbiUGhJdrAbx
LZ3egEKpKR4Ld7w1NN7rQaGQ3FWlIdIGUGFiMsT5LdubC6ABnqdxd+Sg6sfnsbcK
/x+0/eC8
-----END CERTIFICATE-----
```

## File: `test/ssl.key`
```
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEA2FQ4+iK9xronnNaqqnfGR3+JOMTcwTv/frBOms0Mi3hVCmJB
8wxR4ThRBp2K80kmfMCwH8u1mzZPeH/8ifCEL7jRuya2PQNWoZp22GvzHyW1XXm9
/DO0xDl7V5Te7SgFDNLejWwumUPxTzwZ5MCpqaBAsbvr2QduqqzED+Vi4CE7dJEf
GSkSBbmkLvaVuxOoTxTqKkuvLdLfBPX7gEIUL+AW12DgguOCp880C/NHvZFf6R3L
aMnl8BoTcL9xry5GQ36uq3ZBXlzUw/XZQ2fk4RCe0w2sHr/3VXeN83dQQQWz2Etl
Ky08jFjJ7YHs+QWVbeKtHfge4OtKSLS7STjEiQIDAQABAoIBADv3hN/Z9496FPcG
DsM4do9lTC2fbK5oKlf9GZ0R0DNtRO2e9TchqCTtjpBt5ZGxKmkUpP37YzlGYds+
Z0v5jzsHWaQug///x+j+P4mYywlMU604zTB3SNnIMWfCzdUh7dxzK9w6K+Syj9bu
CyN9QMrTsHtUY3mC9Ot8/tCFPtZv/SQY2Y9kqCb2RJJ/vTcTcsjEXjMHFuCv9+KZ
VUGX1sm+VtYY5nUtNEmVYWxCfrU5YRxL6W8iuwdWveGIrvkAnktdmnFPM+MGztmh
7MCxE5X8m8+yUDo/SqUeqniX6nYq6/I7MpNG3XVEE1OEY5o/20+cDxXci9Pn6AXj
TuiZ/XECgYEA+wxFtLh4nna1UE3+nPHel13IC90cneqdRT8wISNXF+Sm1rRfSI4s
r461xmA/BwEFhWrO1xbNi15978zsTUUaPWka4sqh7ZI+/m93C3vbvI1xWGttSqg0
pWI/RjO3rM4vnd0tMgmmNCc/47IB/DXiKJPOcfUScyCS+4j+1ghJ250CgYEA3Jig
5jltZXyUTpHP+FoLV+BGjkxu1S35xjWHg6i6j9LPYxsMWgXTc7OhmCXEBY5lPPSF
hTjqKMvzr79obzPKHt083USzZIyDC0P7uCsmBL6oiTVN1XhpO/1gG8tFHLuZa6B3
Jd074vrsrAMcEottoxyST9jgdiB7Fh47Rjfqht0CgYANBTLsT5D57wAyXQkyjJzV
zuhcLSiZzBxCBifx4ApZU+OPSSWT9sO8izNESaObMmNd6w81OpqIeusfL8qlq0rU
Goppbsb9MlOQEKnk75SS7+cMBe5SK+0nErRjaLVDAiKYFmuMp9F17P80SPwvX4AO
SLQxVtuRGwRkhVNqOF3URQKBgAdyD1w16/9U6RyNx1s2jtN0em0rH0KKvrd17xD+
jO11zBIoQ452S+DH21hrTeZyG/CmwCry9NRTrfHsn/XA5b2M8hT10KhAJdwne0OI
EUxvsviOmAXwfnzL3IaToc2Kd28uh1b71J2gooRbxoLJufWbbUTMqSbTidQBSTbh
hETxAoGAN4E5AJF+CiSzG0TO4BbKpfnmr6HV/mD4zMiUHYNPQDHRoFo0hxsPEwzj
CY2RL6tBnCdzFtZiZYsX7D0uAma0dVRyVvlkDVIH2A65T4OUcXbeaB6Jcf2Z706f
iNPBZa/RKsDJ/RTeZDP8NZfhfhqJq2Nvp/1/hMGCbWfHshltL0M=
-----END RSA PRIVATE KEY-----
```

## File: `test/test.js`
```javascript
// Unit tests for pixl-server-web
// Copyright (c) 2017 - 2019 Joseph Huckaby
// Released under the MIT License

var Path = require('path');
var fs = require('fs');
var net = require('net');
var crypto = require('crypto');
var async = require('async');

var Class = require("pixl-class");
var PixlServer = require('pixl-server');

var PixlRequest = require('pixl-request');
var request = new PixlRequest();
request.setTimeout( 5 * 1000 ); // 5 seconds
request.setIdleTimeout( 5 * 1000 ); // 5 seconds

var http = require('http');
var agent_ka = new http.Agent({ keepAlive: true });
var agent_na = new http.Agent({ keepAlive: false });

process.chdir( __dirname );

var server = new PixlServer({
	
	__name: 'WebServerTest',
	__version: "1.0",
	
	config: {
		"log_dir": __dirname,
		"log_filename": "test.log",
		"debug_level": 9,
		"debug": 1,
		"echo": 0,
		
		"WebServer": {
			"port": 3020,
			"alt_ports": [3120],
			"htdocs_dir": __dirname,
			"max_upload_size": 1024 * 10,
			"static_ttl": 3600,
			"static_index": "index.html",
			"server_signature": "WebServerTest 1.0",
			"compress_text": 1,
			"enable_brotli": 1,
			"timeout": 5,
			"socket_prelim_timeout": 2,
			"response_headers": {
				"Via": "WebServerTest 1.0"
			},
			
			"log_requests": false,
			"regex_log": ".+",
			"recent_requests": 10,
			"max_connections": 10,
			
			"blacklist": ["5.6.7.0/24"],
			
			"rewrites": {
				"^/rewrite(.*)$": "/json$1"
			},
			"redirects": {
				"^/disney": "https://disney.com/",
				"^/pixar(.*)$": {
					"url": "https://pixar.com$1",
					"headers": { "X-Animal": "Frog" },
					"status": "301 Moved Permanently"
				}
			},
			"auth": {
				"^/protected": {
					"enabled": true,
					"type": "basic",
					"realm": "Secret Area",
					"username": "foo",
					"password": "bar"
				}
			},
			
			"https": 1,
			"https_port": 3021,
			"https_alt_ports": [3121],
			"https_cert_file": "ssl.crt",
			"https_key_file": "ssl.key",
			"https_force": 0,
			"https_timeout": 5,
			"https_header_detect": {
				"Front-End-Https": "^on$",
				"X-Url-Scheme": "^https$",
				"X-Forwarded-Protocol": "^https$",
				"X-Forwarded-Proto": "^https$",
				"X-Forwarded-Ssl": "^on$"
			}
		}
	},
	
	components: [
		require('pixl-server-web')
	]
	
});

// Unit Tests

module.exports = {
	setUp: function (callback) {
		var self = this;
		this.server = server;
		
		// delete old unit test log
		fs.unlink( "test.log", function(err) {
			// startup mock server
			server.startup( function() {
				// startup complete
				var web_server = self.web_server = server.WebServer;
				
				// write log in sync mode, for troubleshooting
				server.logger.set('sync', true);
				
				web_server.addURIHandler( '/json', 'JSON Test', function(args, callback) {
					// send custom JSON response
					callback( {
						code: 0,
						description: "Success",
						user: { Name: "Joe", Email: "foo@bar.com" },
						params: args.params,
						query: args.query,
						cookies: args.cookies,
						files: args.files,
						headers: args.request.headers,
						socket_id: args.request.socket._pixl_data.id || 0,
						method: args.request.method,
						ip: args.ip,
						ips: args.ips
					} );
				} );
				
				web_server.addURIHandler( '/sleep', 'Sleep Test', function(args, callback) {
					// send custom JSON response
					var ms = parseInt( args.query.ms );
					
					setTimeout( function() {
						if (args.query.error) {
							callback( 
								"500 Internal Server Error", 
								{ 'X-Sleep': 1 },
								null
							);
						}
						else {
							callback( {
								code: 0,
								description: "Slept for " + ms + "ms",
								ms: ms
							} );
						}
					}, ms );
				} );
				
				web_server.addURIHandler( '/redirect', 'Redirect Test', function(args, callback) {
					// send custom redirect response
					callback( 
						"302 Found", 
						{ 'Location': web_server.getSelfURL(args.request, "/json?redirected=1") },
						null
					);
				} );
				
				web_server.addURIHandler( '/server-status', "Server Status", true, function(args, callback) {
					// send web stats (JSON), ACL protected endpoint
					callback( server.WebServer.getStats() );
				} );
				
				web_server.addURIHandler( '/protected', 'Protected Test', function(args, callback) {
					// auth protected endpoint
					callback( {
						code: 0,
						description: "Protected endpoint success"
					} );
				} );
				
				web_server.addURIHandler( '/binary-force-compress', 'Force Compress Test', function(args, callback) {
					// send custom compressed response
					callback( 
						"200 OK", 
						{ 'Content-Type': "image/gif", 'X-Compress': 1 },
						fs.readFileSync( 'spacer.gif' )
					);
				} );
				
				web_server.addDirectoryHandler( '/parentdir', Path.dirname(__dirname), { ttl: 25, headers: { 'X-Frogs': 'Toads' } } );
				
				// test suite ready
				callback();
				
			} ); // startup
		} ); // delete
	},
	
	tests: [
		
		function testSimpleRequest(test) {
			// test simple HTTP GET request to webserver backend
			request.json( 'http://127.0.0.1:3020/json', false,
				{
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					test.done();
				} 
			);
		},
		
		function testSimpleURLRewrite(test) {
			// test simple rewrite
			request.json( 'http://127.0.0.1:3020/rewrite', false,
				{
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					test.done();
				} 
			);
		},
		
		function testAdvancedURLRewrite(test) {
			// test advanced rewrite
			request.json( 'http://127.0.0.1:3020/rewrite?foo=bar1234&baz=bop%20pog&animal=frog&animal=dog', false,
				{
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					test.ok( !!json.query, "Found query object in JSON response" );
					test.ok( json.query.foo == "bar1234", "Query contains correct foo key" );
					test.ok( json.query.baz == "bop pog", "Query contains correct baz key (URL encoding)" );
					
					// dupes should become array by default
					test.ok( typeof(json.query.animal) == 'object', "Query param animal is an object" );
					test.ok( json.query.animal.length == 2, "Query param animal has length 2" );
					test.ok( json.query.animal[0] === 'frog', "First animal is frog" );
					test.ok( json.query.animal[1] === 'dog', "Second animal is dog" );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					test.done();
				} 
			);
		},
		
		function testSimpleURLRedirect(test) {
			// simple 302
			request.get( 'http://127.0.0.1:3020/disney',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 302, "Got 302 response: " + resp.statusCode );
					test.ok( !!resp.headers['location'], "Got Location header" );
					test.ok( !!resp.headers['location'].match(/disney\.com/), "Correct Location header");
					test.done();
				} 
			);
		},
		
		function testAdvancedURLRedirect(test) {
			// more complex redirect config (301, custom header)
			request.get( 'http://127.0.0.1:3020/pixar/toads',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 301, "Got 301 response: " + resp.statusCode );
					test.ok( !!resp.headers['location'], "Got Location header" );
					test.ok( !!resp.headers['location'].match(/pixar\.com\/toads/), "Correct Location header");
					test.ok( !!resp.headers['x-animal'], "Got x-animal header" );
					test.ok( !!resp.headers['x-animal'].match(/frog/i), "Correct x-animal header");
					test.done();
				} 
			);
		},
		
		function testHTTPAltPort(test) {
			// test simple HTTP GET request to webserver backend, alternate port
			request.json( 'http://127.0.0.1:3120/json', false,
				{
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					test.done();
				} 
			);
		},
		
		function testBadRequest(test) {
			// test bad HTTP GET request to webserver backend
			// this still resolves to the root dir index due to the ../
			request.get( 'http://127.0.0.1:3020/%0ASet-Cookie%3Acrlfinjection/../',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.done();
				} 
			);
		},
		
		// query string
		function testQueryString(test) {
			// test simple HTTP GET request with query string
			request.json( 'http://127.0.0.1:3020/json?foo=bar1234&baz=bop%20pog&animal=frog&animal=dog', false,
				{
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					test.ok( !!json.query, "Found query object in JSON response" );
					test.ok( json.query.foo == "bar1234", "Query contains correct foo key" );
					test.ok( json.query.baz == "bop pog", "Query contains correct baz key (URL encoding)" );
					
					// dupes should become array by default
					test.ok( typeof(json.query.animal) == 'object', "Query param animal is an object" );
					test.ok( json.query.animal.length == 2, "Query param animal has length 2" );
					test.ok( json.query.animal[0] === 'frog', "First animal is frog" );
					test.ok( json.query.animal[1] === 'dog', "Second animal is dog" );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					test.done();
				} 
			);
		},
		
		function testQueryStringFlatten(test) {
			// test simple HTTP GET request with query string dupes flattened
			var web = this.web_server;
			web.config.set('flatten_query', true);
			
			request.json( 'http://127.0.0.1:3020/json?foo=bar1234&baz=bop%20pog&animal=frog&animal=dog', false,
				{
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					test.ok( !!json.query, "Found query object in JSON response" );
					test.ok( json.query.foo == "bar1234", "Query contains correct foo key" );
					test.ok( json.query.baz == "bop pog", "Query contains correct baz key (URL encoding)" );
					
					test.ok( typeof(json.query.animal) == 'string', "Query param animal is a string" );
					test.ok( json.query.animal === 'dog', "Animal is dog" );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					// revert our hot config change
					web.config.set('flatten_query', false);
					
					test.done();
				} 
			);
		},
		
		// Cookies in request
		function testCookieRequest(test) {
			// test simple HTTP GET request with cookies
			request.json( 'http://127.0.0.1:3020/json', false,
				{
					headers: {
						'Cookie': "COOKIE1=foo1234; COOKIE2=bar=5678;",
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					test.ok( !!json.cookies, "Found cookies in JSON response" );
					test.ok( json.cookies.COOKIE1 == "foo1234", "Correct COOKIE1 value" );
					test.ok( json.cookies.COOKIE2 == "bar=5678", "Correct COOKIE2 value" );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					test.done();
				} 
			);
		},
		
		// Bad Cookies in request
		function testBadCookieRequest(test) {
			// test simple HTTP GET request with cookies
			request.json( 'http://127.0.0.1:3020/json', false,
				{
					headers: {
						'Cookie': "COOKIE1=foo1234; COOKIE2=bar5678%E0%A4%A;",
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					test.ok( !!json.cookies, "Found cookies in JSON response" );
					test.ok( json.cookies.COOKIE1 == "foo1234", "Correct COOKIE1 value" );
					test.ok( !json.cookies.COOKIE2, "Expected missing COOKIE2 value" );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					test.done();
				} 
			);
		},
		
		// HTTP POST (Standard)
		function testStandardPost(test) {
			request.post( 'http://127.0.0.1:3020/json',
				{
					headers: {
						'X-Test': "Test"
					},
					data: {
						myparam: "foobar4567"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					// parse json in response
					var json = null;
					try { json = JSON.parse( data.toString() ); }
					catch (err) {
						test.ok( false, "Error parsing JSON: " + err );
						test.done();
					}
					
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.params, "Found params object in JSON response" );
					test.ok( json.params.myparam === "foobar4567", "Correct param in JSON response: " + json.params.myparam );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					test.done();
				} 
			);
		},
		
		// HTTP POST + File Upload
		function testMultipartPost(test) {
			request.post( 'http://127.0.0.1:3020/json',
				{
					headers: {
						'X-Test': "Test"
					},
					multipart: true,
					data: {
						myparam: "foobar5678"
					},
					files: {
						file1: "spacer.gif"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					// parse json in response
					var json = null;
					try { json = JSON.parse( data.toString() ); }
					catch (err) {
						test.ok( false, "Error parsing JSON: " + err );
						test.done();
					}
					
					// test.debug( "JSON Response: ", json );
					
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.params, "Found params object in JSON response" );
					test.ok( json.params.myparam == "foobar5678", "Correct param in JSON response: " + json.params.myparam );
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					test.ok( !!json.files, "Found files object in JSON response" );
					test.ok( !!json.files.file1, "Found file1 object in JSON response" );
					
					// {"path":"/var/folders/11/r_0sz6s13cx1jn68l4m90zfr0000gn/T/40c1602ef5d90ed480edd3000.gif","type":"image/gif","name":"spacer.gif","size":43,"mtime":"2024-04-23T17:56:22.159Z"}
					var file1 = json.files.file1;
					test.ok( file1.size == 43, "Uploaded file has correct size (43): " + file1.size );
					test.ok( !!file1.path, "Uploaded file has no path" );
					test.ok( file1.type == 'image/gif', "Unexpected file type after upload: " + file1.type );
					test.ok( file1.name == 'spacer.gif', "Unexpected file name: " + file1.name );
					test.ok( !!file1.mtime, "Uploaded file has no mtime" );
					test.ok( !isNaN(Date.parse(file1.mtime)), "Invalid mtime in uploaded file: " + file1.mtime );
					
					test.done();
				}
			);
		},
		
		// JSON POST
		function testJSONPOST(test) {
			// test JSON HTTP POST request to webserver backend
			request.json( 'http://127.0.0.1:3020/json', { foo: 'barpost' },
				{
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.debug( "JSON Response", json );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					
					test.ok( !!json.params, "Found params object in JSON response" );
					test.ok( json.params.foo == "barpost", "Correct param in JSON response: " + json.params.foo );
					
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					test.done();
				} 
			);
		},
		
		// HTTP PUT
		function testStandardPut(test) {
			request.put( 'http://127.0.0.1:3020/json',
				{
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					// parse json in response
					var json = null;
					try { json = JSON.parse( data.toString() ); }
					catch (err) {
						test.ok( false, "Error parsing JSON: " + err );
						test.done();
					}
					
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					// make sure echoed request method is correct
					test.ok( json.method == "PUT", "Request method is incorrect: " + json.method + " (expected PUT)" );
					
					test.done();
				} 
			);
		},
		
		// HTTP PUT with request body
		function testStandardPutWithData(test) {
			request.put( 'http://127.0.0.1:3020/json',
				{
					headers: {
						'X-Test': "Test"
					},
					data: {
						myparam: "foobar4567"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					// parse json in response
					var json = null;
					try { json = JSON.parse( data.toString() ); }
					catch (err) {
						test.ok( false, "Error parsing JSON: " + err );
						test.done();
					}
					
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.params, "Found params object in JSON response" );
					test.ok( json.params.myparam == "foobar4567", "Correct param in JSON response: " + json.params.myparam );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					// make sure echoed request method is correct
					test.ok( json.method == "PUT", "Request method is incorrect: " + json.method + " (expected PUT)" );
					
					test.done();
				} 
			);
		},
		
		// JSON HTTP PUT
		function testJSONPut(test) {
			// test simple JSON HTTP PUT request to webserver backend
			request.json( 'http://127.0.0.1:3020/json', false,
				{
					method: "PUT",
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					// make sure echoed request method is correct
					test.ok( json.method == "PUT", "Request method is incorrect: " + json.method + " (expected PUT)" );
					
					test.done();
				} 
			);
		},
		
		// JSON HTTP PUT with request body
		function testJSONPutWithData(test) {
			// test simple JSON HTTP PUT request to webserver backend
			request.json( 'http://127.0.0.1:3020/json', { myparam: "foobar4567" },
				{
					method: "PUT",
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					// request content is echoed too
					test.ok( !!json.params, "Found params object in JSON response" );
					test.ok( json.params.myparam == "foobar4567", "Correct param in JSON response: " + json.params.myparam );
					
					// make sure echoed request method is correct
					test.ok( json.method == "PUT", "Request method is incorrect: " + json.method + " (expected PUT)" );
					
					test.done();
				} 
			);
		},
		
		// HTTP DELETE
		function testStandardDelete(test) {
			request.delete( 'http://127.0.0.1:3020/json',
				{
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					// parse json in response
					var json = null;
					try { json = JSON.parse( data.toString() ); }
					catch (err) {
						test.ok( false, "Error parsing JSON: " + err );
						test.done();
					}
					
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					// make sure echoed request method is correct
					test.ok( json.method == "DELETE", "Request method is incorrect: " + json.method + " (expected DELETE)" );
					
					test.done();
				} 
			);
		},
		
		// HTTP DELETE with request body
		function testStandardDeleteWithData(test) {
			request.delete( 'http://127.0.0.1:3020/json',
				{
					headers: {
						'X-Test': "Test"
					},
					data: {
						myparam: "foobar4567"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					// parse json in response
					var json = null;
					try { json = JSON.parse( data.toString() ); }
					catch (err) {
						test.ok( false, "Error parsing JSON: " + err );
						test.done();
					}
					
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.params, "Found params object in JSON response" );
					test.ok( json.params.myparam == "foobar4567", "Correct param in JSON response: " + json.params.myparam );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					// make sure echoed request method is correct
					test.ok( json.method == "DELETE", "Request method is incorrect: " + json.method + " (expected DELETE)" );
					
					test.done();
				} 
			);
		},
		
		// JSON HTTP DELETE
		function testJSONDelete(test) {
			// test simple JSON HTTP DELETE request to webserver backend
			request.json( 'http://127.0.0.1:3020/json', false,
				{
					method: "DELETE",
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					// make sure echoed request method is correct
					test.ok( json.method == "DELETE", "Request method is incorrect: " + json.method + " (expected DELETE)" );
					
					test.done();
				} 
			);
		},
		
		// JSON HTTP DELETE with request body
		function testJSONDeleteWithData(test) {
			// test simple JSON HTTP DELETE request to webserver backend
			request.json( 'http://127.0.0.1:3020/json', { myparam: "foobar4567" },
				{
					method: "DELETE",
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					test.ok( !!json.params, "Found params object in JSON response" );
					test.ok( json.params.myparam == "foobar4567", "Correct param in JSON response: " + json.params.myparam );
					
					// make sure echoed request method is correct
					test.ok( json.method == "DELETE", "Request method is incorrect: " + json.method + " (expected DELETE)" );
					
					test.done();
				} 
			);
		},
		
		// HTTP HEAD
		function testStandardHead(test) {
			request.head( 'http://127.0.0.1:3020/spacer.gif',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/image\/gif/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['cache-control'], "Cache-Control header present" );
					test.ok( !!resp.headers['cache-control'].match(/max\-age\=3600/), "Cache-Control header contains correct TTL" );
					
					test.ok( !resp.headers['content-encoding'], "Content-Encoding header should NOT be present for a GIF!" );
					test.ok( resp.headers['content-length'] == 43, "spacer.gif is not 43 bytes as expected: " + resp.headers['content-length'] );
					
					test.ok( !!data, "No data object present in HEAD response" );
					test.ok( data.length == 0, "Non-zero data length in HEAD response: " + data.length );
					
					test.done();
				} 
			);
		},
		
		// Error (404)
		function testFileNotFound(test) {
			request.get( 'http://127.0.0.1:3020/noexist',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 404, "Got 404 response: " + resp.statusCode );
					test.done();
				} 
			);
		},
		
		// Error (Front-end Timeout)
		function testFrontEndTimeout(test) {
			request.get( 'http://127.0.0.1:3020/sleep?ms=750',
				{
					timeout: 500
				},
				function(err, resp, data, perf) {
					test.ok( !!err, "Got error from PixlRequest" );
					test.ok( err.toString().match(/timeout|timed out/i), "Correct error message: " + err );
					test.done();
				} 
			);
		},
		
		// Error (Back-end Timeout)
		function testBackEndTimeout(test) {
			var self = this;
			var web = this.web_server;
			web.config.set('request_timeout', 0.5); // 500ms
			
			request.get( 'http://127.0.0.1:3020/sleep?ms=750', {},
				function(err, resp, data, perf) {
					web.config.set('request_timeout', 0); // reset timeout
					test.ok( !err, "Unexpected error from PixlRequest: " + err );
					test.ok( resp.statusCode == 408, "Unexpected HTTP response code: " + resp.statusCode );
					test.done();
				} 
			);
		},
		
		// static file get
		// check ttl, check gzip
		function testStaticTextRequest(test) {
			// test simple HTTP GET to webserver backend
			request.get( 'http://127.0.0.1:3020/index.html',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/text\/html/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['cache-control'], "Cache-Control header present" );
					test.ok( !!resp.headers['cache-control'].match(/max\-age\=3600/), "Cache-Control header contains correct TTL" );
					
					test.ok( !!resp.headers['content-encoding'], "Content-Encoding header present" );
					test.ok( !!resp.headers['content-encoding'].match(/gzip/), "Content-Encoding header contains gzip" );
					
					test.ok( !!data, "Got HTML in response" );
					test.ok( data.toString() === fs.readFileSync('index.html', 'utf8'), "index.html content is correct" );
					
					test.done();
				} 
			);
		},
		
		// static file get
		// this file is not pre-gzipped, so web server should do it in real time
		// this will use brotli
		function testStaticTextRequest2(test) {
			// test simple HTTP GET to webserver backend
			request.get( 'http://127.0.0.1:3020/robots.txt',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/text\/plain/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['cache-control'], "Cache-Control header present" );
					test.ok( !!resp.headers['cache-control'].match(/max\-age\=3600/), "Cache-Control header contains correct TTL" );
					
					test.ok( !!resp.headers['content-encoding'], "Content-Encoding header present" );
					test.ok( !!resp.headers['content-encoding'].match(/br/), "Content-Encoding header contains br" );
					
					test.ok( !!data, "Got text in response" );
					test.ok( data.toString() === fs.readFileSync('robots.txt', 'utf8'), "robots.txt content is correct" );
					
					test.done();
				} 
			);
		},
		
		// binary get
		// should NOT be gzip encoded
		function testStaticBinaryRequest(test) {
			// test simple HTTP GET to webserver backend
			request.get( 'http://127.0.0.1:3020/spacer.gif',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/image\/gif/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['cache-control'], "Cache-Control header present" );
					test.ok( !!resp.headers['cache-control'].match(/max\-age\=3600/), "Cache-Control header contains correct TTL" );
					
					test.ok( !resp.headers['content-encoding'], "Content-Encoding header should NOT be present!" );
					
					test.ok( !!data, "Got data in response" );
					
					test.done();
				} 
			);
		},
		
		// static range request
		function testStaticRangeRequest(test) {
			// test ranged HTTP GET to webserver backend
			var opts = {
				headers: {
					'Accept-Encoding': 'none',
					'Range': 'bytes=31-49'
				}
			};
			request.get( 'http://127.0.0.1:3020/index.html', opts,
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 206, "Got 206 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/text\/html/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['cache-control'], "Cache-Control header present" );
					test.ok( !!resp.headers['cache-control'].match(/max\-age\=3600/), "Cache-Control header contains correct TTL" );
					
					test.ok( !resp.headers['content-encoding'], "Content-Encoding header not present" );
					
					test.ok( !!data, "Got HTML in response" );
					test.ok( data.toString() === '<title>Test</title>', "index.html range snippet is correct: >>>" + data.toString() + "<<<" );
					
					test.done();
				} 
			);
		},
		
		// invalid range request
		function testStaticInvalidRangeRequest(test) {
			// test simple HTTP GET to webserver backend
			var opts = {
				headers: {
					'Accept-Encoding': 'none',
					'Range': 'bytes=1-0'
				}
			};
			request.get( 'http://127.0.0.1:3020/index.html', opts,
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/text\/html/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['cache-control'], "Cache-Control header present" );
					test.ok( !!resp.headers['cache-control'].match(/max\-age\=3600/), "Cache-Control header contains correct TTL" );
					
					test.ok( !resp.headers['content-encoding'], "Content-Encoding header not present" );
					
					// invalid range will fallback to entire file
					test.ok( !!data, "Got HTML in response" );
					test.ok( data.toString() === fs.readFileSync('index.html', 'utf8'), "index.html content is correct" );
					
					test.done();
				} 
			);
		},
		
		// static directory request
		function testStaticDirectoryRequest(test) {
			// test simple HTTP GET to webserver backend
			request.get( 'http://127.0.0.1:3020/',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/text\/html/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['cache-control'], "Cache-Control header present" );
					test.ok( !!resp.headers['cache-control'].match(/max\-age\=3600/), "Cache-Control header contains correct TTL" );
					
					// Note: this is gzip (and not brotli) because of the pre-gzipped static file (index.html.gz)
					test.ok( !!resp.headers['content-encoding'], "Content-Encoding header present" );
					test.ok( !!resp.headers['content-encoding'].match(/gzip/), "Content-Encoding header contains gzip" );
					
					test.ok( !!data, "Got HTML in response" );
					test.ok( data.toString() === fs.readFileSync('index.html', 'utf8'), "index.html content is correct" );
					
					test.done();
				} 
			);
		},
		
		// custom static dir
		function testCustomStaticRequest(test) {
			// test simple HTTP GET to webserver backend
			request.get( 'http://127.0.0.1:3020/parentdir/package.json',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( resp.headers['x-frogs'] == "Toads", "Correct X-Frogs header: " + resp.headers['x-frogs'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/application\/json/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['cache-control'], "Cache-Control header present" );
					test.ok( !!resp.headers['cache-control'].match(/max\-age\=25/), "Cache-Control header contains correct TTL" );
					
					test.ok( !!resp.headers['content-encoding'], "Content-Encoding header present" );
					test.ok( !!resp.headers['content-encoding'].match(/\bbr\b/), "Content-Encoding header contains br" );
					
					test.ok( !!data, "Got JSON in response" );
					test.ok( data.toString() === fs.readFileSync('../package.json', 'utf8'), "package.json content is correct" );
					
					test.done();
				} 
			);
		},
		
		function testCustomStaticDirectoryRequest(test) {
			// test simple HTTP GET to webserver backend
			request.get( 'http://127.0.0.1:3020/parentdir/test/',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( resp.headers['x-frogs'] == "Toads", "Correct X-Frogs header: " + resp.headers['x-frogs'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present (custom)" );
					test.ok( !!resp.headers['content-type'].match(/text\/html/), "Content-Type header contains correct value (custom)" );
					
					test.ok( !!resp.headers['cache-control'], "Cache-Control header present (custom)" );
					test.ok( !!resp.headers['cache-control'].match(/max\-age\=25/), "Cache-Control header contains correct TTL (custom)" );
					
					// Note: this is gzip (and not brotli) because of the pre-gzipped static file (index.html.gz)
					test.ok( !!resp.headers['content-encoding'], "Content-Encoding header present (custom)" );
					test.ok( !!resp.headers['content-encoding'].match(/gzip/), "Content-Encoding header contains gzip (custom)" );
					
					test.ok( !!data, "Got HTML in response (custom)" );
					test.ok( data.toString() === fs.readFileSync('index.html', 'utf8'), "index.html content is correct (custom)" );
					
					test.done();
				} 
			);
		},
		
		function testCustomStaticDirectoryRedirect(test) {
			// test simple HTTP GET to webserver backend
			request.get( 'http://127.0.0.1:3020/parentdir/test',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 302, "Got 302 response: " + resp.statusCode );
					
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( resp.headers['x-frogs'] == "Toads", "Correct X-Frogs header: " + resp.headers['x-frogs'] );
					
					test.ok( !!resp.headers['location'], "Location header present (custom)" );
					test.ok( !!resp.headers['location'].match(/\/parentdir\/test\//), "Location header contains correct value (custom)" );
					
					test.done();
				} 
			);
		},
		
		// binary force compress
		// this is a binary file (typically not compressed), but the handler is forcing compression
		function testBinaryForceCompress(test) {
			// test HTTP GET to webserver backend, make sure response is compressed
			request.get( 'http://127.0.0.1:3020/binary-force-compress',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/image\/gif/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['content-encoding'], "Content-Encoding header present" );
					test.ok( !!resp.headers['content-encoding'].match(/\b(deflate|gzip|br)\b/), "Content-Encoding header contains appropriate value" );
					
					test.ok( !!data, "Got data in response" );
					test.ok( data.length === fs.readFileSync('spacer.gif').length, "spacer.gif content is correct" );
					
					test.done();
				} 
			);
		},
		
		// no encoding
		function testNoEncoding(test) {
			// test simple HTTP GET to webserver backend
			// do not accept any encoding from client side
			request.get( 'http://127.0.0.1:3020/json',
				{
					headers: {
						'Accept-Encoding': "none"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/json/), "Content-Type header contains correct value" );
					
					test.ok( !resp.headers['content-encoding'], "Content-Encoding header should NOT be present!" );
					
					test.ok( !!data, "Got data in response" );
					test.ok( !!data.length, "Data has non-zero length" );
					test.done();
				} 
			);
		},
		
		// deflate encoding
		function testDeflateEncoding(test) {
			// test simple HTTP GET to webserver backend
			// only accept deflate encoding from client side
			request.get( 'http://127.0.0.1:3020/json',
				{
					headers: {
						'Accept-Encoding': "deflate"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/json/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['content-encoding'], "Content-Encoding header present" );
					test.ok( !!resp.headers['content-encoding'].match(/\b(deflate)\b/), "Content-Encoding header contains deflate" );
					
					test.ok( !!data, "Got data in response" );
					test.ok( !!data.length, "Data has non-zero length" );
					test.done();
				} 
			);
		},
		
		// gzip encoding
		function testGzipEncoding(test) {
			// test simple HTTP GET to webserver backend
			// only accept gzip encoding from client side
			request.get( 'http://127.0.0.1:3020/json',
				{
					headers: {
						'Accept-Encoding': "gzip"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/json/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['content-encoding'], "Content-Encoding header present" );
					test.ok( !!resp.headers['content-encoding'].match(/\b(gzip)\b/), "Content-Encoding header contains gzip" );
					
					test.ok( !!data, "Got data in response" );
					test.ok( !!data.length, "Data has non-zero length" );
					test.done();
				} 
			);
		},
		
		// brotli encoding
		function testBrotliEncoding(test) {
			// test simple HTTP GET to webserver backend
			// only accept brotli encoding from client side
			request.get( 'http://127.0.0.1:3020/json',
				{
					headers: {
						'Accept-Encoding': "br"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/json/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['content-encoding'], "Content-Encoding header present" );
					test.ok( !!resp.headers['content-encoding'].match(/\b(br)\b/), "Content-Encoding header contains br" );
					
					test.ok( !!data, "Got data in response" );
					test.ok( !!data.length, "Data has non-zero length" );
					test.done();
				} 
			);
		},
		
		// socket prelim timeout
		function testSocketPrelimTimeout(test) {
			var connected_time = 0;
			var client = net.connect({ port: 3020 }, function() {
				test.debug("Connected to port 3020 (raw socket)");
				connected_time = Date.now() / 1000;
			});
			client.on('data', function(data) {
				test.ok( false, "Should NOT have received any data from socket! " + data );
			});
			client.on('end', function() {
				test.debug("Raw socket disconnected");
				var now = Date.now() / 1000;
				var elapsed = now - connected_time;
				test.ok( Math.abs(elapsed - 2.0) < 1.0, "Incorrect time elapsed for socket prelim timeout: " + elapsed );
				test.done();
			});
		},
		
		function waitForAllSockets(test) {
			// wait for all sockets to close for next test (requires clean slate)
			var self = this;
			
			test.debug("Connections still open: ", Object.keys(self.web_server.conns) );
			
			for (var id in this.web_server.conns) {
				this.web_server.conns[id].end();
			}
			
			async.whilst(
				function(cb) { 
					cb( null, Object.keys(self.web_server.conns).length > 0 );
				},
				function(callback) {
					setTimeout( function() { callback(); }, 100 );
				},
				function() {
					test.done();
				}
			); // async.whilst
		},
		
		// max_connections
		function testMaxConnections(test) {
			// test going over max concurrent connections (10)
			// this test is very perf and timing sensitive, may fail on overloaded or underpowered servers
			// we need ALL sockets to be closed for this
			var self = this;
			
			test.ok( Object.keys(self.web_server.conns).length == 0, "Oops, there's one or more sockets left" );
			
			// open 10 concurrent
			for (var idx = 0; idx < 10; idx++) {
				request.get( 'http://127.0.0.1:3020/sleep?ms=500',
					function(err, resp, data, perf) {
						// ignore
					} 
				);
			} // loop
			
			// sleep for 250ms, then test
			setTimeout( function() {
				// now, all 10 requests should be in progress, so 11th should fail
				request.get( 'http://127.0.0.1:3020/json',
					function(err, resp, data, perf) {
						test.ok( !!err, "Expected error from PixlRequest" );
						setTimeout( function() { test.done(); }, 500 ); // wait for all 10 to complete
					} 
				);
			}, 250 );
		},
		
		// post size too large
		function testLargeMultipartPost(test) {
			request.post( 'http://127.0.0.1:3020/json',
				{
					multipart: true,
					data: {
						myparam: crypto.randomBytes( (1024 * 10) + 1 )
					}
				},
				function(err, resp, data, perf) {
					// multi-part relies on 'formidable' to throw an error, so it is a HTTP 400
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 400, "Got 400 response: " + resp.statusCode );
					test.done();
				} 
			);
		},
		function testLargeRawPost(test) {
			request.post( 'http://127.0.0.1:3020/json',
				{
					headers: {
						'Content-Type': "application/octet-stream"
					},
					data: crypto.randomBytes( (1024 * 10) + 1 )
				},
				function(err, resp, data, perf) {
					// pure post generates a socket-closing super error
					test.ok( !!err, "Expected error from PixlRequest" );
					test.done();
				} 
			);
		},
		
		// keep-alives
		function testKeepAlives(test) {
			// test keep-alive sockets
			var sendReqGetSocketID = function(ka, callback) {
				request.json( 'http://127.0.0.1:3020/json', false, { agent: ka ? agent_ka : agent_na },
					function(err, resp, json, perf) {
						if (err && !json && !json.socket_id) return callback(false);
						callback( json.socket_id );
					} 
				); // request.json
			}; // sendReqGetSocketID
			
			sendReqGetSocketID( false, function(socket1) {
				test.ok( !!socket1, "Got Socket ID 1 (close)" );
				
				sendReqGetSocketID( false, function(socket2) {
					test.ok( !!socket2, "Got Socket ID 2 (close)" );
					
					test.ok( socket1 != socket2, "Socket IDs differ with close" );
					
					// now try it again with KA
					sendReqGetSocketID( true, function(socket3) {
						test.ok( !!socket3, "Got Socket ID 3 (KA)" );
						
						sendReqGetSocketID( true, function(socket4) {
							test.ok( !!socket4, "Got Socket ID 4 (KA)" );
							
							test.ok( socket3 == socket4, "Socket IDs same with KA" );
							test.done();
							
						} ); // req 4
					} ); // req 3
				} ); // req 2
			} ); // req 1
		},
		
		// redirect
		function testRedirectHandler(test) {
			request.get( 'http://127.0.0.1:3020/redirect',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 302, "Got 302 response: " + resp.statusCode );
					test.ok( !!resp.headers['location'], "Got Location header" );
					test.ok( !!resp.headers['location'].match(/redirected/), "Correct Location header");
					test.done();
				} 
			);
		},
		
		// x-forwarded-for
		function testForwardedFor(test) {
			request.json( 'http://127.0.0.1:3020/json', false, 
				{
					headers: {
						"X-Forwarded-For": "1.2.3.4" // external IP
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( data.ip === "1.2.3.4", "Correct Public IP in response: " + data.ip );
					test.done();
				} 
			);
		},
		function testForwardedForGarbage(test) {
			request.json( 'http://127.0.0.1:3020/json', false, 
				{
					headers: {
						"X-Forwarded-For": "garbage, 1.2.3.4, more garbage" // external IP
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( data.ip === "1.2.3.4", "Correct Public IP in response: " + data.ip );
					test.done();
				} 
			);
		},
		function testForwardedForAllGarbage(test) {
			request.json( 'http://127.0.0.1:3020/json', false, 
				{
					headers: {
						"X-Forwarded-For": "garbage" // external IP
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( data.ip === "127.0.0.1", "Correct Public IP in response: " + data.ip );
					test.done();
				} 
			);
		},
		
		// public_ip_offset
		function testForwardedForOffsetNeg1(test) {
			var self = this;
			var web = this.web_server;
			web.config.set('public_ip_offset', -1);
			
			request.json( 'http://127.0.0.1:3020/json', false, 
				{
					headers: {
						"X-Forwarded-For": "1.2.3.4, 2.3.4.5, 3.4.5.6"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( data.ip === "127.0.0.1", "Correct offset public IP in response: " + data.ip );
					web.config.set('public_ip_offset', 0); // reset
					test.done();
				} 
			);
		},
		function testForwardedForOffsetNeg2(test) {
			var self = this;
			var web = this.web_server;
			web.config.set('public_ip_offset', -2);
			
			request.json( 'http://127.0.0.1:3020/json', false, 
				{
					headers: {
						"X-Forwarded-For": "1.2.3.4, 2.3.4.5, 3.4.5.6"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( data.ip === "3.4.5.6", "Correct offset public IP in response: " + data.ip );
					web.config.set('public_ip_offset', 0); // reset
					test.done();
				} 
			);
		},
		function testForwardedForOffsetNeg3(test) {
			var self = this;
			var web = this.web_server;
			web.config.set('public_ip_offset', -3);
			
			request.json( 'http://127.0.0.1:3020/json', false, 
				{
					headers: {
						"X-Forwarded-For": "1.2.3.4, 2.3.4.5, 3.4.5.6"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( data.ip === "2.3.4.5", "Correct offset public IP in response: " + data.ip );
					web.config.set('public_ip_offset', 0); // reset
					test.done();
				} 
			);
		},
		
		// acl block
		function testACL(test) {
			request.get( 'http://127.0.0.1:3020/server-status', // ACL'ed endpoint
				{
					headers: {
						"X-Forwarded-For": "1.2.3.4" // external IP
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 403, "Got 403 response: " + resp.statusCode );
					test.done();
				} 
			);
		},
		
		function testACLBadIP(test) {
			// test badly-formatted IP
			request.get( 'http://127.0.0.1:3020/server-status', // ACL'ed endpoint
				{
					headers: {
						"X-Forwarded-For": "THIS-IS-NOT-AN-IP-ADDRESS" // external IP
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 403, "Got 403 response: " + resp.statusCode );
					test.done();
				} 
			);
		},
		
		function testAuthRequired(test) {
			// no auth header should be challenged
			request.get( 'http://127.0.0.1:3020/protected',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 401, "Got 401 response: " + resp.statusCode );
					test.ok( !!resp.headers['www-authenticate'], "Got WWW-Authenticate header" );
					test.ok( !!resp.headers['www-authenticate'].match(/Basic realm="Secret Area"/), "Correct WWW-Authenticate header: " + resp.headers['www-authenticate'] );
					test.ok( data.toString() == "Unauthorized", "Correct response body: " + data.toString() );
					test.done();
				}
			);
		},
		
		function testAuthBadCredentials(test) {
			// invalid basic auth should fail
			request.get( 'http://127.0.0.1:3020/protected',
				{
					headers: {
						"Authorization": "Basic " + Buffer.from("foo:nope").toString('base64')
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 401, "Got 401 response: " + resp.statusCode );
					test.ok( data.toString() == "Unauthorized", "Correct response body: " + data.toString() );
					test.done();
				}
			);
		},
		
		function testAuthGoodCredentials(test) {
			// valid basic auth should pass through
			request.json( 'http://127.0.0.1:3020/protected', false,
				{
					headers: {
						"Authorization": "Basic " + Buffer.from("foo:bar").toString('base64')
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( json.description == "Protected endpoint success", "Correct description in JSON response: " + json.description );
					test.done();
				}
			);
		},
		
		// blacklist
		function testBlacklistedIP(test) {
			request.get( 'http://127.0.0.1:3020/json', 
				{
					headers: {
						"X-Forwarded-For": "5.6.7.8" // blacklisted
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 403, "Got 403 response: " + resp.statusCode );
					test.done();
				} 
			);
		},
		function testAnotherBlacklistedIP(test) {
			request.get( 'http://127.0.0.1:3020/json', 
				{
					headers: {
						"X-Forwarded-For": "1.2.3.4, 5.6.7.255, 2.3.4.5" // blacklisted
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 403, "Got 403 response: " + resp.statusCode );
					test.done();
				} 
			);
		},
		function testAllowedIP(test) {
			request.get( 'http://127.0.0.1:3020/json', 
				{
					headers: {
						"X-Forwarded-For": "5.6.8.7" // just outside blacklisted range
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.done();
				} 
			);
		},
		
		function testConditionalResponseHeaders(test) {
			// test response headers per http code
			var self = this;
			var web = this.web_server;
			
			web.config.set('code_response_headers', {
				"403": { 'X-Test-Cond': "Tree Frogs" }
			});
			
			request.get( 'http://127.0.0.1:3020/server-status', // ACL'ed endpoint
				{
					headers: {
						"X-Forwarded-For": "1.2.3.4" // external IP
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 403, "Got 403 response: " + resp.statusCode );
					test.ok( resp.headers['x-test-cond'] === "Tree Frogs", "Unexpected header: " + resp.headers['X-Test-Cond'] );
					
					// make sure basic 200 doesn't have header
					request.json( 'http://127.0.0.1:3020/json', false, {}, 
						function(err, resp, json, perf) {
							test.ok( !err, "No error from PixlRequest: " + err );
							test.ok( !!resp, "Got resp from PixlRequest" );
							test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
							test.ok( !resp.headers['x-test-cond'], "Unexpected X-Test-Cond header for HTTP 200!" );
							web.config.set('code_response_headers', null); // reset config
							test.done();
						}
					);
				} 
			);
		},
		
		// get stats
		function testStats(test) {
			// test stats API (this also tests ACL pass)
			request.json( 'http://127.0.0.1:3020/server-status', false,
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					
					// test.debug("Web Server Stats", json);
					test.ok( !!json.server, "server obj in stats" );
					test.ok( json.server.name == "WebServerTest", "Correct server name in stats" );
					test.ok( !!json.stats, "stats present" );
					test.ok( !!json.stats.total, "total in stats" );
					test.ok( !!json.sockets, "sockets in stats" );
					test.ok( Object.keys(json.sockets).length == 2, "Exactly 2 active sockets" );
					test.ok( !!json.recent, "recent in stats" );
					test.ok( json.recent.length > 0, "recent has length" );
					
					test.done();
				} 
			);
		},
		
		// https
		function testHTTPSRequest(test) {
			// test HTTPS GET request to webserver backend
			request.json( 'https://127.0.0.1:3021/json', false,
				{
					rejectUnauthorized: false, // self-signed cert
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					test.ok( !!json.headers.ssl, "SSL pseudo-header present in echo" );
					
					test.done();
				} 
			);
		},
		
		function testHTTPSAltPort(test) {
			// test HTTPS GET request to webserver backend on alt port
			request.json( 'https://127.0.0.1:3121/json', false,
				{
					rejectUnauthorized: false, // self-signed cert
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					test.ok( !!json.headers.ssl, "SSL pseudo-header present in echo" );
					
					test.done();
				} 
			);
		},
		
		function testHTTPSPost(test) {
			request.post( 'https://127.0.0.1:3021/json',
				{
					rejectUnauthorized: false, // self-signed cert
					headers: {
						'X-Test': "Test"
					},
					data: {
						myparam: "foobar4567"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					// parse json in response
					var json = null;
					try { json = JSON.parse( data.toString() ); }
					catch (err) {
						test.ok( false, "Error parsing JSON: " + err );
						test.done();
					}
					
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.params, "Found params object in JSON response" );
					test.ok( json.params.myparam === "foobar4567", "Correct param in JSON response: " + json.params.myparam );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					test.ok( !!json.headers.ssl, "SSL pseudo-header present in echo" );
					
					test.done();
				} 
			);
		},
		
		// HTTPS POST + File Upload
		function testHTTPSMultipartPost(test) {
			request.post( 'https://127.0.0.1:3021/json',
				{
					rejectUnauthorized: false, // self-signed cert
					headers: {
						'X-Test': "Test"
					},
					multipart: true,
					data: {
						myparam: "foobar5678"
					},
					files: {
						file1: "spacer.gif"
					}
				},
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					// parse json in response
					var json = null;
					try { json = JSON.parse( data.toString() ); }
					catch (err) {
						test.ok( false, "Error parsing JSON: " + err );
						test.done();
					}
					
					// test.debug( "JSON Response: ", json );
					
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.params, "Found params object in JSON response" );
					test.ok( json.params.myparam == "foobar5678", "Correct param in JSON response: " + json.params.myparam );
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					test.ok( !!json.headers.ssl, "SSL pseudo-header present in echo" );
					test.ok( !!json.files, "Found files object in JSON response" );
					test.ok( !!json.files.file1, "Found file1 object in JSON response" );
					
					// {"path":"/var/folders/11/r_0sz6s13cx1jn68l4m90zfr0000gn/T/40c1602ef5d90ed480edd3000.gif","type":"image/gif","name":"spacer.gif","size":43,"mtime":"2024-04-23T17:56:22.159Z"}
					var file1 = json.files.file1;
					test.ok( file1.size == 43, "Uploaded file has correct size (43): " + file1.size );
					test.ok( !!file1.path, "Uploaded file has no path" );
					test.ok( file1.type == 'image/gif', "Unexpected file type after upload: " + file1.type );
					test.ok( file1.name == 'spacer.gif', "Unexpected file name: " + file1.name );
					test.ok( !!file1.mtime, "Uploaded file has no mtime" );
					test.ok( !isNaN(Date.parse(file1.mtime)), "Invalid mtime in uploaded file: " + file1.mtime );
					
					test.done();
				} 
			);
		},
		
		// SSL JSON POST
		function testHTTPSJSONPOST(test) {
			// test JSON HTTPS POST request to webserver backend
			request.json( 'https://127.0.0.1:3021/json', { foo: 'barpost' },
				{
					rejectUnauthorized: false, // self-signed cert
					headers: {
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.debug( "JSON Response", json );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					
					test.ok( !!json.params, "Found params object in JSON response" );
					test.ok( json.params.foo == "barpost", "Correct param in JSON response: " + json.params.foo );
					
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					test.ok( !!json.headers.ssl, "SSL pseudo-header present in echo" );
					
					test.done();
				} 
			);
		},
		
		// https_header_detect
		function testHTTPSHeaderDetect(test) {
			// test HTTP GET request to webserver backend, simulating an external SSL proxy (LB, etc.)
			request.json( 'http://127.0.0.1:3020/json', false,
				{
					headers: {
						'X-Forwarded-Proto': "https",
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					// request headers will be echoed back
					test.ok( !!json.headers, "Found headers echoed in JSON response" );
					test.ok( json.headers['x-test'] == "Test", "Found Test header echoed in JSON response" );
					
					// even though this wasn't an SSL request, we simulated one, which should have triggered https_header_detect
					test.ok( !!json.headers.ssl, "SSL pseudo-header present in echo" );
					
					test.done();
				} 
			);
		},
		
		// filters
		function testFilterPassthrough(test) {
			// setup filter for passthrough
			var self = this;
			
			this.web_server.addURIFilter( /^\/json/, "Test Filter", function(args, callback) {
				// add a nugget into request query
				args.query.filter_nugget = 42;
				
				// add a custom response header too
				args.response.setHeader('X-Filtered', "4242");
				
				callback(false); // passthru
			} );
			
			request.json( 'http://127.0.0.1:3020/json', false, function(err, resp, json, perf) {
				test.ok( !err, "No error from PixlRequest: " + err );
				test.ok( !!resp, "Got resp from PixlRequest" );
				test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
				test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
				test.ok( !!json, "Got JSON in response" );
				test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
				
				// did our query nugget make it all the way through?
				test.ok( json.query.filter_nugget == "42", "Found filter nugget infused into query" );
				
				// and our response header nugget too?
				test.ok( resp.headers['x-filtered'] == "4242", "Correct X-Filtered header: " + resp.headers['x-filtered'] );
				
				// remove filter
				self.web_server.removeURIFilter('Test Filter');
				
				test.done();
			} );
		},
		
		function testFilterIntercept(test) {
			// setup filter for intercepting request and sending custom response
			var self = this;
			
			this.web_server.addURIFilter( /.+/, "Test Filter 418", function(args, callback) {
				// send our own custom response
				callback(
					"418 I'm a teapot", 
					{ 'X-Filtered': 42 },
					null
				);
			} );
			
			request.get( 'http://127.0.0.1:3020/index.html',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 418, "Got 418 response: " + resp.statusCode );
					test.ok( resp.headers['x-filtered'] == 42, "Correct X-Filtered header: " + resp.headers['x-filtered'] );
					
					// remove filter
					self.web_server.removeURIFilter('Test Filter 418');
					
					// make sure things are back to good
					request.get( 'http://127.0.0.1:3020/index.html',
						function(err, resp, data, perf) {
							test.ok( !err, "No error from PixlRequest: " + err );
							test.ok( !!resp, "Got resp from PixlRequest" );
							test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
							test.ok( resp.headers['via'] == "WebServerTest 1.0", "Correct Via header: " + resp.headers['via'] );
							test.done();
						}
					); // request.get #2
				}
			); // request.get #1
		},
		
		function waitForAllSockets2(test) {
			// wait for all sockets to close for next test (requires clean slate)
			var self = this;
			
			test.debug("Connections still open: ", Object.keys(self.web_server.conns) );
			
			for (var id in this.web_server.conns) {
				this.web_server.conns[id].end();
			}
			
			async.whilst(
				function(cb) { 
					cb( null, Object.keys(self.web_server.conns).length > 0 );
				},
				function(callback) {
					setTimeout( function() { callback(); }, 100 );
				},
				function() {
					test.done();
				}
			); // async.whilst
		},
		
		// max_concurrent_requests
		function testMaxConcurrentRequests(test) {
			// test going over max concurrent requests, remainder should be queued
			var self = this;
			test.expect( 1 + (3 * 10) + 2 + 2 );
			this.web_server.queue.concurrency = 5;
			
			// open 10 concurrent, 5 should queue
			// test.debug( "Stats:", self.web_server.getStats() );
			test.ok( Object.keys(self.web_server.conns).length == 0, "Oops, there's one or more sockets left" );
			
			async.times( 10,
				function(idx, callback) {
					request.get( 'http://127.0.0.1:3020/sleep?ms=500',
						function(err, resp, data, perf) {
							test.ok( !err, "No error from PixlRequest: " + err );
							test.ok( !!resp, "Got resp from PixlRequest" );
							test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
							callback();
						}
					);
				},
				function() {
					// all 10 requests completed, queue should be empty now
					var stats = self.web_server.getStats();
					test.ok( stats.queue.pending == 0, "Expected 0 pending requests, got: " + stats.queue.pending );
					test.ok( stats.queue.running == 0, "Expected 0 running requests, got: " + stats.queue.running );
					test.done();
				}
			); // async.times
			
			// sleep for 250ms, then grab stats
			setTimeout( function() {
				// now, 5 requests should be in progress, and 5 queued
				var stats = self.web_server.getStats();
				test.ok( stats.queue.pending == 5, "Expected 5 pending requests, got: " + stats.queue.pending );
				test.ok( stats.queue.running == 5, "Expected 5 running requests, got: " + stats.queue.running );
			}, 250 );
		}
		
	], // tests
	
	tearDown: function (callback) {
		// clean up
		var self = this;
		
		this.server.shutdown( function() {
			callback();
		} );
	}
	
};
```

