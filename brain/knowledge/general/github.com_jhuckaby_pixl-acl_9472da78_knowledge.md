---
id: github.com-jhuckaby-pixl-acl-9472da78-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:15.304261
---

# KNOWLEDGE EXTRACT: github.com_jhuckaby_pixl-acl_9472da78
> **Extracted on:** 2026-04-01 13:29:44
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522492/github.com_jhuckaby_pixl-acl_9472da78

---

## File: `.npmignore`
```
.gitignore
node_modules/
```

## File: `README.md`
```markdown
# Overview

**pixl-acl** is a simple [Access Control List](https://en.wikipedia.org/wiki/Access_control_list) (ACL) system for quickly matching IP addresses against a set of IP ranges.  It is built upon the [ipaddr.js](https://github.com/whitequark/ipaddr.js) module (the only dependency, also MIT licensed).  IPv4 and IPv6 addresses and ranges are both supported, including single IPs, partial IPs, and [CIDR blocks](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).  This is a perfect library for implementing an IP whitelist or blacklist.

# Usage

Use [npm](https://www.npmjs.com/) to install the module:

```
npm install pixl-acl
```

Then use `require()` to load it in your code:

```js
const ACL = require('pixl-acl');
```

To use the module, instantiate an object, and specify one or more IPv4 or IPv6 addresses or ranges (you can mix/match the two):

```js
let acl = new ACL( "10.0.0.0/8" );
let acl = new ACL([ "10.11.12.13", "fd00::/8" ]);
```

You can optionally add addresses or ranges after construction using `add()`:

```js
acl.add( "172.16.0.0/12" );
acl.add([ "127.0.0.1", "::1" ]);
```

Partial IP addresses are also accepted, in which case the CIDR bits are guessed:

```js
acl.add( "10." );        // expands to: 10.0.0.0/8
acl.add( "192.168" );    // expands to: 192.168.0.0/16
acl.add( "2001:db8::" ); // expands to: 2001:db8:0:0:0:0:0:0/32
acl.add( "::1" );        // expands to: 0:0:0:0:0:0:0:1/128
```

Limited IP ranges are also accepted.  Make sure they are separated by a dash (with zero or more spaces), and that they can be represented accurately with one single CIDR block:

```js
acl.add( "8.12.144.0 - 8.12.144.255" );
acl.add( "2600:1f70:4000:300:0:0:0:0 - 2600:1f70:4000:3ff:ffff:ffff:ffff:ffff" );
```

Complex ranges that require multiple CIDR blocks are not supported.

## Matching IP Addresses

To match a single IP address against your ACL, call the `check()` method:

```js
if (acl.check("10.20.30.40")) {
	// IP is within one of our ranges
}
```

To match multiple IP addresses at once, presumably from a [proxy chain](#handling-proxy-chains), call either `checkAll()` (for a whitelist) or `checkAny()` (for a blacklist).  For example, to see if **all** IPs match a whitelist use `checkAll()` like this:

```js
if (acl.checkAll([ "1.2.3.4", "192.168.1.2", "::1" ])) {
	// all 3 IPs are in the ACL, allow request through
}
```

Or alternatively, to see if **any** IPs are in a blacklist use `checkAny()` like this:

```js
if (acl.checkAny([ "5.6.7.8", "2001:0db8:85a3:0000:0000:8a2e:0370:7334" ])) {
	// One or more IPs are blacklisted, reject request!
}
```

You can pass IPv4 and/or IPv6 addresses to all methods, including a mix of the two.

# Private Addresses

To create an ACL consisting of all the [IPv4](https://en.wikipedia.org/wiki/Private_network#Private_IPv4_addresses) and [IPv6](https://en.wikipedia.org/wiki/Private_network#Private_IPv6_addresses) private address ranges, including the [localhost loopback](https://en.wikipedia.org/wiki/Localhost#Loopback) addresses (both IPv4 and IPv6 versions), and [link-local addresses](https://en.wikipedia.org/wiki/Link-local_address) (both IPv4 and IPv6 versions) you can use the following set of [CIDR blocks](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing):

```js
let acl = new ACL([ "::1/128", "127.0.0.1/32", "169.254.0.0/16", "fe80::/10", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16", "fd00::/8" ]);
```

# Handling Proxy Chains

When receiving incoming HTTP requests for a web application, you should consider all the IP addresses in the request, including those added to various headers by proxies and/or load balancers.  It is recommended that you scan the following request headers and compile a list of all IPs, including the socket IP address itself.

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

# License

**The MIT License (MIT)**

*Copyright (c) 2018 - 2023 Joseph Huckaby.*

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

## File: `acl.js`
```javascript
// pixl-acl
// Copyright (c) 2018 Joseph Huckaby
// Released under the MIT License

var ipaddr = require('ipaddr.js');

module.exports = class ACL {
	
	constructor(ranges) {
		// class constructor
		this.ipv4s = [];
		this.ipv6s = [];
		if (ranges) this.add(ranges);
	}
	
	add(ranges) {
		// add one or more IP ranges
		var self = this;
		if (typeof(ranges) == 'string') ranges = [ranges];
		
		ranges.forEach( function(str) {
			// convert IP ranges to CIDR format
			if (str.match(/\-/)) {
				str = self.parseRange(str);
			}
			
			if (!str.match(/\/\d+$/)) {
				// try to guess bits (i.e. partial IP was passed in)
				if (str.match(/\:/)) {
					// ipv6 massage
					if (str.match(/^\:\:/)) str += '/128';
					else {
						var parts = str.replace(/\:+$/, '').split(/\:/);
						var bits = parts.length * 16;
						str += '/' + bits;
					}
				}
				else {
					// ipv4 massage
					str = str.replace(/\.$/, '');
					var parts = str.split(/\./);
					var bits = parts.length * 8;
					str += '/' + bits;
				}
			}
			var range = null;
			try { range = ipaddr.parseCIDR( str ); }
			catch (err) {
				throw new Error( err.message + ": " + str );
			}
			if (range[0].kind() == 'ipv4') self.ipv4s.push( range );
			else self.ipv6s.push( range );
		} );
	}
	
	check(ips) {
		// check one or more IPs against ACL ranges
		// return number of IPs that matched
		var self = this;
		var count = 0;
		if (typeof(ips) == 'string') ips = [ips];
		
		for (var idx = 0, len = ips.length; idx < len; idx++) {
			var ip = ips[idx];
			var addr = null;
			try {
				addr = ipaddr.process( ip ); // process() converts IPv6-wrapped-IPv4 back to IPv4
			}
			catch (err) {
				addr = null;
			}
			if (addr) {
				var contains = false;
				var ranges = (addr.kind() == 'ipv4') ? this.ipv4s : this.ipv6s;
				
				if (ranges.length) {
					for (var idy = 0, ley = ranges.length; idy < ley; idy++) {
						if (addr.match(ranges[idy])) {
							contains = true;
							idy = ley;
						}
					} // foreach range
				}
				
				if (contains) count++;
			}
		} // foreach ip
		
		return count;
	}
	
	checkAll(ips) {
		// whitelist-style check
		// return true if all are in, false if any are out
		if (typeof(ips) == 'string') ips = [ips];
		return( this.check(ips) == ips.length );
	}
	
	checkAny(ips) {
		// blacklist-style check
		// return true if any are in, false otherwise
		if (typeof(ips) == 'string') ips = [ips];
		return( this.check(ips) > 0 );
	}
	
	toString() {
		// convert ranges to string (for debugging, logging, etc.)
		return [].concat(this.ipv4s, this.ipv6s).join(', ');
	}
	
	parseRange(str) {
		// parse dash-delimited IP range (e.g. '8.12.144.0 - 8.12.144.255') into CIDR block (e.g. '8.12.144.0/24')
		// suppport IPv4 and IPv6
		var parts = str.split(/\s*\-\s*/);
		var start_ip = parts[0].trim();
		var end_ip = parts[1].trim();
		
		if (start_ip.match(/^\d+\.\d+\.\d+\.\d+$/)) return rangeToCIDR(start_ip, end_ip);
		else return rangeToCIDRv6(start_ip, end_ip);
	}
	
}; // class

// Internal Utility Functions:

function ipToInteger(ip) {
	return ip.split('.').reduce((acc, octet) => acc * 256 + parseInt(octet, 10), 0) >>> 0;
}

function integerToIP(int) {
	return [int >>> 24, int >> 16 & 255, int >> 8 & 255, int & 255].join('.');
}

function rangeToCIDR(startIP, endIP) {
	const start = ipToInteger(startIP);
	const end = ipToInteger(endIP);
	const range = end - start + 1;
	const bits = Math.floor(Math.log2(range));
	const mask = 32 - bits;
	const cidr = integerToIP(start & (0xFFFFFFFF << bits)) + '/' + mask;
	return cidr;
}

function ipv6ToBigInt(ipv6) {
	const sections = ipv6.split(':').map(section => parseInt(section, 16));
	return sections.reduce((acc, section) => acc * 65536n + BigInt(section), 0n);
}

function bigIntToIPv6(bigInt) {
	const parts = [];
	for (let i = 0; i < 8; i++) {
		parts.unshift((bigInt & 0xffffn).toString(16));
		bigInt >>= 16n;
	}
	return parts.join(':');
}

function rangeToCIDRv6(startIP, endIP) {
	const start = ipv6ToBigInt(startIP);
	const end = ipv6ToBigInt(endIP);
	const range = end - start + 1n;
	const bits = BigInt(Math.floor(Math.log2(Number(range))));
	const mask = 128n - bits;
	let cidr = bigIntToIPv6(start & (0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFn << bits)) + '/' + mask;
    return cidr;
}
```

## File: `package.json`
```json
{
	"name": "pixl-acl",
	"version": "1.0.4",
	"description": "A simple but fast implementation of IPv4 and IPv6 ACL filtering.",
	"author": "Joseph Huckaby <jhuckaby@gmail.com>",
	"homepage": "https://github.com/jhuckaby/pixl-acl",
	"license": "MIT",
	"main": "acl.js",
	"repository": {
		"type": "git",
		"url": "https://github.com/jhuckaby/pixl-acl"
	},
	"bugs": {
		"url": "https://github.com/jhuckaby/pixl-acl/issues"
	},
	"keywords": [
		"acl",
		"ipv4",
		"ipv6"
	],
	"dependencies": {
		"ipaddr.js": "1.8.1"
	}
}
```

