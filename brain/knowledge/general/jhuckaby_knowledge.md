---
id: jhuckaby-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:55.967228
---

# KNOWLEDGE EXTRACT: jhuckaby
> **Extracted on:** 2026-03-30 17:38:11
> **Source:** jhuckaby

---

## File: `Cronicle.md`
```markdown
# 📦 jhuckaby/Cronicle [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/Cronicle
🌐 http://cronicle.net

## Meta
- **Stars:** ⭐ 5566 | **Forks:** 🍴 485
- **Language:** JavaScript | **License:** NOASSERTION
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A simple, distributed task scheduler and runner with a web based UI.

## README (trích đầu)
```
# xyOps™

![xyOps Screenshot](https://pixlcore.com/images/blog/xyops/workflow-edit.webp)

Announcing **xyOps™**, the spiritual successor to Cronicle!  Beta v0.9 is now available for testing:

https://github.com/pixlcore/xyops

Let me know what you think!

Cronicle will still be supported and maintained going forward (mainly bug fixes and security issues will be patched).

# Overview

**Cronicle** is a multi-server task scheduler and runner, with a web based front-end UI.  It handles both scheduled, repeating and on-demand jobs, targeting any number of worker servers, with real-time stats and live log viewer.  It's basically a fancy [Cron](https://en.wikipedia.org/wiki/Cron) replacement written in [Node.js](https://nodejs.org/).  You can give it simple shell commands, or write Plugins in virtually any language.

![Main Screenshot](https://pixlcore.com/software/cronicle/screenshots-new/job-details-complete.png)

## Features at a Glance

* Single or multi-server setup.
* Automated failover to backup servers.
* Auto-discovery of nearby servers.
* Real-time job status with live log viewer.
* Plugins can be written in any language.
* Schedule events in multiple timezones.
* Optionally queue up long-running events.
* Track CPU and memory usage for each job.
* Historical stats with performance graphs.
* Simple JSON messaging system for Plugins.
* Web hooks for external notification systems.
* Simple REST API for scheduling and running events.
* API Keys for authenticating remote apps.

## Documentation

The Cronicle documentation is split up across these files:

- &rarr; **[Installation & Setup](https://github.com/jhuckaby/Cronicle/blob/master/docs/Setup.md)**
- &rarr; **[Configuration](https://github.com/jhuckaby/Cronicle/blob/master/docs/Configuration.md)**
- &rarr; **[Web UI](https://github.com/jhuckaby/Cronicle/blob/master/docs/WebUI.md)**
- &rarr; **[Plugins](https://github.com/jhuckaby/Cronicle/blob/master/docs/Plugins.md)**
- &rarr; **[Command Line](https://github.com/jhuckaby/Cronicle/blob/master/docs/CommandLine.md)**
- &rarr; **[Inner Workings](https://github.com/jhuckaby/Cronicle/blob/master/docs/InnerWorkings.md)**
- &rarr; **[API Reference](https://github.com/jhuckaby/Cronicle/blob/master/docs/APIReference.md)**
- &rarr; **[Development](https://github.com/jhuckaby/Cronicle/blob/master/docs/Development.md)**

## Glossary

A quick introduction to some common terms used in Cronicle:

| Term | Description |
|------|-------------|
| **Primary Server** | The primary server which keeps time and runs the scheduler, assigning jobs to other servers, and/or itself. |
| **Backup Server** | A worker server which will automatically become primary and take over duties if the current primary dies. |
| **Worker Server** | A server which sits idle until it is assigned jobs by the primary server. |
| **Server Group** | A named group of servers which can be targeted by events, and tagged as "primary eligible", or "worker only". |
| **API Key** | A special key t
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `performa-satellite.md`
```markdown
# 📦 jhuckaby/performa-satellite [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/performa-satellite


## Meta
- **Stars:** ⭐ 22 | **Forks:** 🍴 5
- **Language:** JavaScript | **License:** NOASSERTION
- **Last updated:** 2025-09-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Remote data collector for Performa.

## README (trích đầu)
```
# Overview

This module is a companion to the [Performa](https://github.com/jhuckaby/performa) monitoring system.  It is the data collector, which can be installed on all your servers.  It collects metrics and sends them to the central Performa server every minute, and is activated by [cron](https://en.wikipedia.org/wiki/Cron).  It is shipped as a precompiled binary and thus has no dependencies.

# Installation

The easiest way to install Performa Satellite is to use one of our precompiled binaries.  It can live anywhere on the filesystem, but for these examples we place it into the `/opt/performa` directory.  Make sure you are `root` (superuser) to install this.

```
mkdir /opt/performa
curl -L https://github.com/jhuckaby/performa-satellite/releases/latest/download/performa-satellite-linux-x64 > /opt/performa/satellite.bin
chmod 755 /opt/performa/satellite.bin
/opt/performa/satellite.bin --install
```

Note that in this case you will have to select the correct binary for your platform.  The static binary flavors available are:

- `performa-satellite-linux-arm64`
- `performa-satellite-linux-x64`
- `performa-satellite-macos-arm64`
- `performa-satellite-macos-x64`

The `performa-satellite-linux-x86` binary should work on any 64-bit Linux OS on x86 hardware, including RedHat/CentOS and Debian/Ubuntu.  Change `x86` to `arm64` if you are running Linux on ARM (e.g. Raspberry Pi).  If you are installing on macOS, replace `linux` with `macos`, but note your Mac's architecture (`x64` or `arm64` a.k.a. Apple Silicon).

Running the binary with the `--install` argument will add it to [cron](https://en.wikipedia.org/wiki/Cron), specifically in `/etc/cron.d/performa-satellite`, which is set to run once per minute.  It also creates a default configuration file, if one doesn't exist.

# Configuration

Performa Satellite expects a JSON formatted configuration file to live in the same directory as the binary executable, and named `config.json`.  Here is an example file:

```json
{
	"enabled": true,
	"host": "performa.local:5511",
	"secret_key": "CHANGE_ME",
	"group": ""
}
```

Here are descriptions of the properties you can put in the file:

| Property Name | Type | Description |
|---------------|------|-------------|
| `enabled` | Boolean | This enables or disables Performa Satellite.  Set this to `false` to pause metrics collection. |
| `host` | String | Set this to the hostname and port of your Performa master server, e.g. `performa.mycompany.com:5511`.  The default port for Performa is `5511`. |
| `secret_key` | String | Set this to the same secret key string on your Performa master server.  See [Secret Key](https://github.com/jhuckaby/performa#secret_key) for details. |
| `group` | String | **(Optional)** The group ID is optional, and only needed if you have servers with indeterminate hostnames (i.e. serverless, autoscale, etc.).  See [Groups](https://github.com/jhuckaby/performa#groups) for details. |
| `proto` | String | **(Optional)** If you have configure
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-acl.md`
```markdown
# 📦 jhuckaby/pixl-acl [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-acl


## Meta
- **Stars:** ⭐ 3 | **Forks:** 🍴 1
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2024-08-02
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A simple but fast implementation of IPv4 and IPv6 ACL filtering.

## README (trích đầu)
```
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

To create an ACL consisting of all the [IPv4](https://en.wikipedia.org/wiki/Private_network#Private_IPv4_addresses) and [IPv6](https://en.wikipedia.org/wiki/Private_network#Private_IPv6_addresses) private address ranges, including the [localhost loopback](https://en.wikipedia.or
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-boot.md`
```markdown
# 📦 jhuckaby/pixl-boot [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-boot


## Meta
- **Stars:** ⭐ 5 | **Forks:** 🍴 3
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-01-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Register your service to launch on server startup (Linux / OS X).

## README (trích đầu)
```
# Overview

`pixl-boot` will automatically register a startup service for your module on Linux and macOS, so your daemon will be started on a server reboot.  It is configured entirely out of your [package.json](https://docs.npmjs.com/files/package.json) file, and will handle all the details of registering a [systemd service](https://en.wikipedia.org/wiki/Systemd) on Linux, or a [LaunchAgent/LaunchDaemon](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html) on macOS.

This is only designed for packages that are installed as the root user.

# Usage

First, add the `pixl-boot` package in the `dependencies` section of your `package.json` file:

```js
"dependencies": {
	"pixl-boot": "^2.0.0"
}
```

Next, you need to provide a shell script for starting and stopping your background daemon.  This can be a simple bash (or Node.js) script that responds to `start` and `stop` commands on the CLI.  If you do not have one of these scripts we provide a sample one for you (instructions below).

Once you have your control script ready, link to it in the `bin` property in your `package.json` file:

```js
"bin": "bin/control.sh",
```

Finally, you need to have npm run `pixl-boot` on install and uninstall of your package, so that it has a chance to register and unregister your startup service.  Do this by adding `boot` and `unboot` properties in the `scripts` section of your `package.json` file:

```js
"scripts": {
	"boot": "pixl-boot install",
	"unboot": "pixl-boot uninstall"
}
```

Then your users need to be instructed to type:

```sh
npm run boot
npm run unboot
```

To install and uninstall the startup service, respectively.

## Advanced

The `pixl-boot install` and `pixl-boot uninstall` commands accept some optional CLI arguments which you can add if desired:

### name

Add `--name` if you want to customize the startup service name.  This defaults to the `name` property from your `package.json` file, and is converted to lower-case alphanumeric.  Make sure you add this to both the install and uninstall commands.  Example:

```js
"scripts": {
	"boot": "pixl-boot install --name mycustomservice",
	"unboot": "pixl-boot uninstall --name mycustomservice"
}
```

### company

Add `--company` if you want to customize the "company" (organization) name that goes into your startup service metadata.  This defaults to the word `Node`, and may be displayed as part of your package description, depending on the OS.  This is really just a cosmetic detail that has no operational effect on your service.  Make sure you add this to both the install and uninstall commands.  Example use:

```js
"scripts": {
	"boot": "pixl-boot install --company MyCompany",
	"unboot": "pixl-boot uninstall --company MyCompany"
}
```

### script

Add `--script` to specify a custom location of your shell control script, relative to the base directory of your package.  Use this option if you do not want to pull this from the `bin` prop
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-chart.md`
```markdown
# 📦 jhuckaby/pixl-chart [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-chart


## Meta
- **Stars:** ⭐ 39 | **Forks:** 🍴 5
- **Language:** JavaScript | **License:** NOASSERTION
- **Last updated:** 2026-03-15
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A simple time series chart renderer using HTML5 Canvas.

## README (trích đầu)
```
<details><summary>Table of Contents</summary>

<!-- toc -->
- [Overview](#overview)
	* [Features](#features)
	* [Demos](#demos)
- [Usage](#usage)
	* [Adding Layers](#adding-layers)
		+ [Layer Properties](#layer-properties)
	* [Chart Management](#chart-management)
		+ [Auto Resizing](#auto-resizing)
	* [Line Smoothing](#line-smoothing)
	* [Legend Display](#legend-display)
	* [Dates and Times](#dates-and-times)
	* [Dark Mode](#dark-mode)
	* [Snapshots](#snapshots)
		+ [Downloads](#downloads)
	* [Headroom](#headroom)
	* [Data Labels](#data-labels)
	* [Zooming](#zooming)
	* [Hover Overlay](#hover-overlay)
	* [Flatten Layers](#flatten-layers)
	* [Configuration](#configuration)
		+ [autoHeadroom](#autoheadroom)
		+ [autoManage](#automanage)
		+ [autoResize](#autoresize)
		+ [background](#background)
		+ [borderColor](#bordercolor)
		+ [canvas](#canvas)
		+ [clip](#clip)
		+ [colors](#colors)
		+ [cursor](#cursor)
		+ [dataGapImage](#datagapimage)
		+ [dataSuffix](#datasuffix)
		+ [dataType](#datatype)
			- [integer](#integer)
			- [float](#float)
			- [bytes](#bytes)
			- [seconds](#seconds)
			- [milliseconds](#milliseconds)
		+ [dateStyles](#datestyles)
		+ [delta](#delta)
		+ [deltaMinValue](#deltaminvalue)
		+ [divideByDelta](#dividebydelta)
		+ [density](#density)
		+ [emptyMessage](#emptymessage)
		+ [fill](#fill)
		+ [flatten](#flatten)
		+ [floatPrecision](#floatprecision)
		+ [fontColor](#fontcolor)
		+ [fontFamily](#fontfamily)
		+ [fontSize](#fontsize)
		+ [height](#height)
		+ [horizLabelPadding](#horizlabelpadding)
		+ [horizTicks](#horizticks)
		+ [hover](#hover)
		+ [hoverSort](#hoversort)
		+ [hoverMax](#hovermax)
		+ [layers](#layers)
		+ [legend](#legend)
		+ [legendMaxLines](#legendmaxlines)
		+ [legendPadding](#legendpadding)
		+ [lineCap](#linecap)
		+ [lineDashes](#linedashes)
		+ [lineJoin](#linejoin)
		+ [lineWidth](#linewidth)
		+ [live](#live)
		+ [locale](#locale)
		+ [minHorizScale](#minhorizscale)
		+ [minVertScale](#minvertscale)
		+ [padding](#padding)
		+ [progressive](#progressive)
		+ [reducedMotion](#reducedmotion)
		+ [showDataGaps](#showdatagaps)
		+ [showSubtitle](#showsubtitle)
		+ [smoothing](#smoothing)
		+ [smoothingMaxSamples](#smoothingmaxsamples)
		+ [smoothingMaxTotalSamples](#smoothingmaxtotalsamples)
		+ [stroke](#stroke)
		+ [subtitle](#subtitle)
		+ [timeZone](#timezone)
		+ [title](#title)
		+ [titlePadding](#titlepadding)
		+ [titleSize](#titlesize)
		+ [titleStyle](#titlestyle)
		+ [titleColor](#titlecolor)
		+ [vertLabelPadding](#vertlabelpadding)
		+ [vertLabelSide](#vertlabelside)
		+ [vertTicks](#vertticks)
		+ [width](#width)
		+ [zeroFloor](#zerofloor)
		+ [zoom](#zoom)
	* [API](#api)
		+ [addLayer](#addlayer)
		+ [addLayers](#addlayers)
		+ [addLayerSample](#addlayersample)
		+ [render](#render)
		+ [update](#update)
		+ [snapshot](#snapshot)
		+ [download](#download)
		+ [on](#on)
		+ [off](#off)
		+ [destroy](#destroy)
	* [Properties](#properties)
		+ [dataLimits](#datalimits)
		+ [bounds](#
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-logger.md`
```markdown
# 📦 jhuckaby/pixl-logger [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-logger


## Meta
- **Stars:** ⭐ 6 | **Forks:** 🍴 1
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-01-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A simple logging class which generates [bracket][delimited] log columns.

## README (trích đầu)
```
(Không lấy được README)
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-mail.md`
```markdown
# 📦 jhuckaby/pixl-mail [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-mail


## Meta
- **Stars:** ⭐ 6 | **Forks:** 🍴 2
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-01-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A very simple class for sending e-mail via SMTP or local sendmail.

## README (trích đầu)
```
<details><summary>Table of Contents</summary>

<!-- toc -->
- [Overview](#overview)
- [Usage](#usage)
	* [Placeholder Substitution](#placeholder-substitution)
	* [Loading From Files](#loading-from-files)
	* [Attachments](#attachments)
	* [HTML Emails](#html-emails)
	* [Options](#options)
	* [Logging](#logging)
	* [Debugging](#debugging)
- [License](#license)

</details>

# Overview

This module provides a very simple e-mail sender, which leans heavily on the awesome [nodemailer](https://nodemailer.com/) package.  It layers on the ability to pass in a complete e-mail message with headers and body in one string (or file), and optionally perform placeholder substitution using [sub()](https://www.npmjs.com/package/pixl-tools#sub) from the [pixl-tools](https://www.npmjs.com/package/pixl-tools) package.  Auto-detects HTML or plain text e-mail body, and supports custom headers and attachments as well.

# Usage

Use [npm](https://www.npmjs.com/) to install the module:

```sh
npm install pixl-mail
```

Then use `require()` to load it in your code:

```js
const PixlMail = require('pixl-mail');
```

Instantiate a mailer object and pass in the SMTP hostname (defaults to `127.0.0.1`) and the port number (defaults to `25`):

```js
let mail = new PixlMail( 'smtp.myserver.com', 25 );
let mail = new PixlMail( '127.0.0.1' );
let mail = new PixlMail();
```

Send mail using the `send()` method.  Pass in the complete e-mail message as a multi-line string including `To`, `From` and `Subject` headers, and a callback:

```js
let message = 
	"To: president@whitehouse.gov\n" + 
	"From: citizen@email.com\n" + 
	"Subject: State Budget\n" +
	"\n" +  
	"Dear Mr. President,\nOur state needs more money.\n";

mail.send( message, function(err) {
	if (err) console.error( "Mail Error: " + err );
} );
```

For multiple recipients, simply separate them by commas on the `To` line.  You can also specify `Cc` and/or `Bcc` headers, as well as any custom MIME headers.

## Placeholder Substitution

The library supports a simple e-mail templating system, where you can insert `[bracket_placeholders]` in your e-mail message, and have the library fill them with appropriate content from a separate object.  This feature uses the [sub()](https://github.com/jhuckaby/pixl-tools#sub) function from the [pixl-tools](https://github.com/jhuckaby/pixl-tools) package.

As an example, imagine a welcome e-mail for a new user who has signed up for your app.  You have the welcome e-mail "template" stored separately, and want to fill in the user's e-mail address, full name and username at sending time.  Here is how to do this:

```js
// email template
let message = 
	"To: [email]\n" + 
	"From: support@myapp.com\n" + 
	"Subject: Welcome to My App, [full_name]!\n" +
	"\n" +  
	"Dear [full_name],\nWelcome to My App!  Your username is '[username]'.\n";

// placeholder args
let user = {
	username: "jhuckaby",
	full_name: "Joseph Huckaby",
	email: "jhuckaby@email.com"
};

mail.send( message, user, function(err) {
	i
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-perf.md`
```markdown
# 📦 jhuckaby/pixl-perf [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-perf


## Meta
- **Stars:** ⭐ 5 | **Forks:** 🍴 1
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2024-05-08
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A simple, high precision performance tracking system for Node.JS apps.

## README (trích đầu)
```
# Overview

This module provides an easy way to track high resolution performance metrics in your app.  Basically, you wrap your function calls or async operations you want to measure with `begin()` and `end()` calls, provide IDs for each metric, and the library provides a summary report whenever you want one.  You can also increment arbitrary counters, and include that data in the report as well.

# Usage

Use [npm](https://www.npmjs.com/) to install the module:

```sh
npm install pixl-perf
```

Then use `require()` to load it in your code:

```js
const Perf = require('pixl-perf');
```

To use the module, instantiate an object, and start tracking.  The first thing you should do is call `begin()` without any arguments, which starts the overall tracking system.  Similar, the last thing you should do is call `end()` also with no arguments.  These allow the system to track a "total time elapsed".  Example:

```js
let perf = new Perf();
perf.begin(); // start overall tracking

// do stuff here

perf.end(); // end all tracking
```

To track individual metrics, simply pass an identifier key to `begin()` and `end()`.  Here is an example for tracking something synchronous:

```js
let perf = new Perf();
perf.begin(); // start overall tracking

perf.begin('json_parse');
let obj = JSON.parse("{ ...some long JSON document here... }");
perf.end('json_parse');

perf.end(); // end all tracking
```

You can overlap and nest multiple metrics inside each other.  For example, you could have an overall `db` metric for database operations, but also an inner `db_query` for the actual DB query time.

```js
let perf = new Perf();
perf.begin(); // start overall tracking

perf.begin('db');
// connect to db here

	perf.begin('db_query');
	// run db query here
	perf.end('db_query');

// disconnect from db here
perf.end('db');

perf.end(); // end all tracking
```

For tracking asynchronous operations, a little extra care is needed.  We can't simply call `end()` with a plain key, because multiple Node "threads" may be running the same operation at the same time.  So in this case, we can use the return value of `begin()` as a promise.  `begin()` always returns a special unique tracker object, which has its own `end()` method on it.

```js
let perf = new Perf();
perf.begin(); // start overall tracking

let tracker = perf.begin('something'); // begin measuring 'something'
setTimeout( function() {
	// one second later...
	tracker.end(); // done with something
	
	perf.end(); // end all tracking
	console.log("Perf Metrics: ", perf.metrics());
}, 1000 );
```

This way, if your app happens to call the same code multiple times simultaneously, each one will have its own unique tracker object, and not clobber each other.  When `end()` is called on the tracker object, it merges the results back into the main instance it was spawned from.

As you can see, the above example also introduces the `metrics()` method, for fetching a summary of all our measurements.  This would output something 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-request.md`
```markdown
# 📦 jhuckaby/pixl-request [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-request


## Meta
- **Stars:** ⭐ 5 | **Forks:** 🍴 2
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-03-11
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A very simple module for making HTTP requests.

## README (trích đầu)
```
# Overview

This module is a very simple wrapper around Node's built-in [http](https://nodejs.org/api/http.html) library for making HTTP requests.  It provides an easy way to send an HTTP GET or POST, including things like support for HTTPS (SSL), file uploads and JSON REST style API calls.  Compressed responses are also handled automatically.

# Table of Contents

<!-- toc -->
- [Usage](#usage)
- [Method List](#method-list)
- [Request Types](#request-types)
	* [HTTP GET](#http-get)
	* [HTTP HEAD](#http-head)
	* [HTTP POST](#http-post)
		+ [Pure Data POST](#pure-data-post)
		+ [Multipart POST](#multipart-post)
		+ [File Uploads](#file-uploads)
	* [HTTP PUT](#http-put)
	* [HTTP DELETE](#http-delete)
	* [File Downloads](#file-downloads)
		+ [Advanced Stream Control](#advanced-stream-control)
	* [Progress Updates](#progress-updates)
	* [Keep-Alives](#keep-alives)
	* [JSON REST API](#json-rest-api)
	* [XML REST API](#xml-rest-api)
- [Default Headers](#default-headers)
- [Handling Timeouts](#handling-timeouts)
- [Automatic Redirects](#automatic-redirects)
- [Automatic Errors](#automatic-errors)
- [Automatic Retries](#automatic-retries)
- [Compressed Responses](#compressed-responses)
- [Abort Signals](#abort-signals)
- [Performance Metrics](#performance-metrics)
- [DNS Caching](#dns-caching)
	* [Flushing the Cache](#flushing-the-cache)
- [SSL Certificate Validation](#ssl-certificate-validation)
- [Proxy Servers](#proxy-servers)
- [Access Control Lists](#access-control-lists)
- [License](#license)

# Usage

Use [npm](https://www.npmjs.com/) to install the module:

```
npm install pixl-request
```

Then use `require()` to load it in your code:

```js
const PixlRequest = require('pixl-request');
```

Instantiate a request object and pass in an optional user agent string (you can also set this later via a header):

```js
let request = new PixlRequest( "My Custom Agent 1.0" );
```

Here is a simple HTTP GET example:

```js
try {
	let { data } = await request.get('https://www.bitstamp.net/api/ticker/');
	console.log("Success: " + data);
}
catch (err) {
	throw err;
}
```

The result object actually contains other properties besides `data`.  Here is an example using all of them:

```js
try {
	let { resp, data, perf } = await request.get('https://www.bitstamp.net/api/ticker/');
	console.log("Status: " + resp.statusCode + " " + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
request.get( 'https://www.bitstamp.net/api/ticker/', function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + " " + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

And here is a simple JSON REST API request:

```js
try {
	let { resp, 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-server-api.md`
```markdown
# 📦 jhuckaby/pixl-server-api [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-server-api


## Meta
- **Stars:** ⭐ 3 | **Forks:** 🍴 2
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-03-15
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A JSON REST API component for the pixl-server framework.

## README (trích đầu)
```
# Overview

This module is a component for use in [pixl-server](https://www.github.com/jhuckaby/pixl-server).  It implements a simple JSON REST API framework, and is built atop the [pixl-server-web](https://www.github.com/jhuckaby/pixl-server-web) component.  You can use this to define your own API methods or API classes, which are invoked based on a URL pattern such as `/api/NAME` or `/api/CLASS/NAME`.  The base URI is configurable.

# Usage

Use [npm](https://www.npmjs.com/) to install the module:

```sh
npm install pixl-server pixl-server-web pixl-server-api
```

Here is a simple usage example.  Note that the component's official name is `API`, so that is what you should use for the configuration key, and for gaining access to the component via your server object.

```js
const PixlServer = require('pixl-server');
let server = new PixlServer({
	
	__name: 'MyServer',
	__version: "1.0",
	
	config: {
		"log_dir": "/let/log",
		"debug_level": 9,
		
		"WebServer": {
			"http_port": 80,
			"http_htdocs_dir": "/let/www/html"
		},
		
		"API": {
			"base_uri": "/api"
		}
	},
	
	components: [
		require('pixl-server-web'),
		require('pixl-server-api')
	]
	
});

server.startup( function() {
	// server startup complete
	
	server.API.addHandler( 'add_user', function(args, callback) {
		// custom request handler for our API
		callback({
			code: 0,
			description: "Success!"
		});
	} );
} );
```

Notice how we are loading the [pixl-server](https://www.github.com/jhuckaby/pixl-server) parent module, and then specifying [pixl-server-web](https://www.github.com/jhuckaby/pixl-server-web) and [pixl-server-api](https://www.github.com/jhuckaby/pixl-server-api) as components:

```js
components: [
	require('pixl-server-web'),
	require('pixl-server-api')
]
```

This example demonstrates a very simple API service, which will answer to `/api/add_user` URIs, and sends back a serialized JSON response.

# Configuration

The configuration for this component is set by passing in a `API` key in the `config` element when constructing the `PixlServer` object, or, if a JSON configuration file is used, a `API` object at the outermost level of the file structure.  It can contain the following keys:

## base_uri

The `base_uri` property specifies the URL prefix that will activate the API service.  Basically, this means the API service will "listen" for incoming web server requests that begin with this URL.  The default value is `/api`, so API handlers are activated by `/api/HANDLER_NAME`.

# Adding API Handlers

To add an API handler, call the `addHandler()` method on the API component.  You can access the API component by the `API` property in the main server object.  Example:

```js
server.API.addHandler( 'add_user', function(args, callback) {
	// custom request handler for our API
	callback({
		code: 0,
		description: "Success!"
	});
} );
```

Your handler method is passed an `args` object containing information about the request.  See the [args](https://www.github.com/jhuckaby/p
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-server-storage.md`
```markdown
# 📦 jhuckaby/pixl-server-storage [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-server-storage


## Meta
- **Stars:** ⭐ 11 | **Forks:** 🍴 8
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-02-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A key/value/list/hash storage component for the pixl-server framework.

## README (trích đầu)
```
# Overview

This module is a component for use in [pixl-server](https://www.github.com/jhuckaby/pixl-server).  It implements a simple key/value storage system that can use multiple back-ends, such as [Amazon S3](https://aws.amazon.com/s3/), [Redis](https://redis.io/), or a local filesystem.  It introduces the concept of a "chunked linked list", which supports extremely fast push, pop, shift, unshift, and random reads/writes.  Also provided is a fast hash table implementation with key iteration, a transaction system, and an indexing and search system.

## Features at a Glance

* Uses very little memory in most cases.
* Store JSON or binary (raw) data records.
* Supports multiple back-ends including Amazon S3, Redis, and local filesystem.
* Linked lists with very fast push, pop, shift, unshift, and random reads/writes.
* Hash tables with key iterators, and very fast reads / writes.
* Advisory locking system with shared and exclusive locks.
* Variable expiration dates per key and automatic deletion.
* Transaction system for isolated compound operations and atomic commits, rollbacks.
* Indexing system for searches across collections of JSON records.
* Supports Google-style full-text search queries.

## Table of Contents

The documentation is split up across six files:

- &rarr; **[Main Docs](https://github.com/jhuckaby/pixl-server-storage/blob/master/README.md)** *(You are here)*
- &rarr; **[Lists](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Lists.md)**
- &rarr; **[Hashes](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Hashes.md)**
- &rarr; **[Transactions](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Transactions.md)**
- &rarr; **[Indexer](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Indexer.md)**
- &rarr; **[API Reference](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/API.md)**

Here is the table of contents for this current document:

<!-- toc -->
- [Usage](#usage)
	* [Standalone Mode](#standalone-mode)
- [Configuration](#configuration)
	* [engine](#engine)
	* [engine_path](#engine_path)
	* [list_page_size](#list_page_size)
	* [hash_page_size](#hash_page_size)
	* [concurrency](#concurrency)
	* [maintenance](#maintenance)
	* [log_event_types](#log_event_types)
	* [max_recent_events](#max_recent_events)
	* [expiration_updates](#expiration_updates)
	* [lower_case_keys](#lower_case_keys)
	* [debug (standalone)](#debug-standalone)
- [Engines](#engines)
	* [Local Filesystem](#local-filesystem)
		+ [Key Namespaces](#key-namespaces)
		+ [Raw File Paths](#raw-file-paths)
		+ [Key Template](#key-template)
		+ [Filesystem Cache](#filesystem-cache)
	* [Amazon S3](#amazon-s3)
		+ [S3 File Extensions](#s3-file-extensions)
		+ [S3 Key Prefix](#s3-key-prefix)
		+ [S3 Key Template](#s3-key-template)
		+ [S3 Cache](#s3-cache)
		+ [S3 Compatible Services](#s3-compatible-services)
	* [Redis](#redis)
		+ [RedisCluster](#rediscluster)
	* [SQLite](#sqlite)
	* [Hybrid](#hybr
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-server-unbase.md`
```markdown
# 📦 jhuckaby/pixl-server-unbase [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-server-unbase


## Meta
- **Stars:** ⭐ 3 | **Forks:** 🍴 1
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-01-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A database component for the pixl-server framework.

## README (trích đầu)
```
# Overview

Unbase is a component for use in [pixl-server](https://github.com/jhuckaby/pixl-server).  It implements a database-like system, built on top of [pixl-server-storage](https://github.com/jhuckaby/pixl-server-storage).  It is basically a thin wrapper around the [Indexer](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Indexer.md), with some additional record storage, database management and live search capabilities.

The main idea behind Unbase is to provide a database (or something sort of like one) on top of simple JSON files on disk (or S3 if you are insane).  Both the record data and the indexes are built out of simple JSON documents.  It uses as little memory as possible, at the cost of speed.

This component does not implement any sort of external API, nor user authentication.  It is merely an internal programmatic API to a database-like system, which can be embedded into an application or higher level database.  Unbase is a single-master database (only one process can do writes at a time), as all locks and transactions are RAM-based.  Also see [Indexer Caveats](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Indexer.md#caveats).

## Features at a Glance

- Database management and data storage services.
- Stores JSON records which can be retrieved by ID.
- Database-like "tables" (called indexes) which can be searched.
- Both [simple](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Indexer.md#simple-queries) and [complex](https://github.com/jhuckaby/pixl-server-storage/blob/master/docs/Indexer.md#pxql-queries) query languages are supported.
- Supports Google-style full-text search queries, with exact phrase matching.
- Live search queries which can be "subscribed" to.

## Table of Contents

<!-- toc -->
- [Usage](#usage)
- [Configuration](#configuration)
	* [indexes](#indexes)
	* [base_path](#base_path)
- [Basic Functions](#basic-functions)
	* [Creating, Updating and Deleting Indexes](#creating-updating-and-deleting-indexes)
	* [Adding, Updating and Deleting Fields](#adding-updating-and-deleting-fields)
	* [Adding, Updating and Deleting Sorters](#adding-updating-and-deleting-sorters)
	* [Inserting, Updating and Deleting Records](#inserting-updating-and-deleting-records)
		+ [Bulk Operations](#bulk-operations)
	* [Fetching Records](#fetching-records)
	* [Searching](#searching)
	* [Live Search](#live-search)
		+ [Live Summaries](#live-summaries)
	* [Jobs](#jobs)
- [API](#api)
	* [getIndex](#getindex)
	* [createIndex](#createindex)
	* [updateIndex](#updateindex)
	* [reindex](#reindex)
	* [deleteIndex](#deleteindex)
	* [addField](#addfield)
	* [updateField](#updatefield)
	* [deleteField](#deletefield)
	* [addSorter](#addsorter)
	* [updateSorter](#updatesorter)
	* [deleteSorter](#deletesorter)
	* [insert](#insert)
	* [update](#update)
	* [delete](#delete)
	* [get](#get)
	* [bulkInsert](#bulkinsert)
	* [bulkUpdate](#bulkupdate)
	* [bulkDelete](#bulkdelete)
	* [search](#search)
	* [subscri
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-server-user.md`
```markdown
# 📦 jhuckaby/pixl-server-user [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-server-user


## Meta
- **Stars:** ⭐ 4 | **Forks:** 🍴 3
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-03-15
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A basic user login and session management system for the pixl-server framework.

## README (trích đầu)
```
<details><summary>Table of Contents</summary>

<!-- toc -->
- [Overview](#overview)
- [Usage](#usage)
- [Configuration](#configuration)
	* [free_accounts](#free_accounts)
	* [session_expire_days](#session_expire_days)
	* [max_failed_logins_per_hour](#max_failed_logins_per_hour)
	* [max_forgot_passwords_per_hour](#max_forgot_passwords_per_hour)
	* [sort_global_users](#sort_global_users)
	* [use_bcrypt](#use_bcrypt)
	* [smtp_hostname](#smtp_hostname)
	* [email_templates](#email_templates)
	* [default_privileges](#default_privileges)
- [User Accounts](#user-accounts)
	* [Global User List](#global-user-list)
	* [Privileges](#privileges)
- [Sessions](#sessions)
	* [Resuming Sessions](#resuming-sessions)
- [Cookies](#cookies)
- [Emails](#emails)
	* [welcome_new_user](#welcome_new_user)
	* [changed_password](#changed_password)
	* [recover_password](#recover_password)
- [Initial Setup](#initial-setup)
	* [Creating an initial administrator](#creating-an-initial-administrator)
	* [Creating the initial user list](#creating-the-initial-user-list)
	* [Storage Maintenance](#storage-maintenance)
- [API](#api)
	* [create](#create)
	* [login](#login)
	* [logout](#logout)
	* [resume_session](#resume_session)
	* [update](#update)
	* [delete](#delete)
	* [forgot_password](#forgot_password)
	* [reset_password](#reset_password)
	* [admin_create](#admin_create)
	* [admin_update](#admin_update)
	* [admin_delete](#admin_delete)
	* [admin_get_user](#admin_get_user)
	* [admin_get_users](#admin_get_users)
- [Adding Your Own APIs](#adding-your-own-apis)
	* [Validating The Session](#validating-the-session)
- [Hooks](#hooks)
	* [before_create](#before_create)
	* [after_create](#after_create)
	* [before_login](#before_login)
	* [after_login](#after_login)
	* [before_logout](#before_logout)
	* [after_logout](#after_logout)
	* [before_resume_session](#before_resume_session)
	* [after_resume_session](#after_resume_session)
	* [before_update](#before_update)
	* [after_update](#after_update)
	* [before_delete](#before_delete)
	* [after_delete](#after_delete)
	* [before_forgot_password](#before_forgot_password)
	* [after_forgot_password](#after_forgot_password)
	* [before_reset_password](#before_reset_password)
	* [after_reset_password](#after_reset_password)
- [Transaction Log](#transaction-log)
	* [user_create](#user_create)
	* [user_login](#user_login)
	* [user_logout](#user_logout)
	* [user_update](#user_update)
	* [user_delete](#user_delete)
	* [user_forgot_password](#user_forgot_password)
	* [user_password_reset](#user_password_reset)
- [External User Login Systems](#external-user-login-systems)
	* [Returning User Information](#returning-user-information)
	* [Redirecting to a Login Page](#redirecting-to-a-login-page)
	* [Logging Out](#logging-out)
- [License](#license)

</details>

# Overview

This module is a component for use in [pixl-server](https://www.github.com/jhuckaby/pixl-server).  It implements a server-side user login and management API, and is built atop the [pixl-s
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-server-web.md`
```markdown
# 📦 jhuckaby/pixl-server-web [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-server-web


## Meta
- **Stars:** ⭐ 11 | **Forks:** 🍴 2
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-02-17
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A web server component for the pixl-server framework.

## README (trích đầu)
```
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
	* [Internal File Redirects](#internal-file-redir
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-server.md`
```markdown
# 📦 jhuckaby/pixl-server [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-server


## Meta
- **Stars:** ⭐ 22 | **Forks:** 🍴 3
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-02-13
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A simple server daemon framework for Node.js.

## README (trích đầu)
```
<details><summary>Table of Contents</summary>

<!-- toc -->
- [Overview](#overview)
- [Usage](#usage)
- [Components](#components)
	* [Stock Components](#stock-components)
		+ [WebServer (pixl-server-web)](#webserver-pixl-server-web)
		+ [PoolManager (pixl-server-pool)](#poolmanager-pixl-server-pool)
		+ [JSON API (pixl-server-api)](#json-api-pixl-server-api)
		+ [UserManager (pixl-server-user)](#usermanager-pixl-server-user)
		+ [Storage (pixl-server-storage)](#storage-pixl-server-storage)
		+ [MultiServer (pixl-server-multi)](#multiserver-pixl-server-multi)
- [Events](#events)
	* [init](#init)
	* [prestart](#prestart)
	* [ready](#ready)
	* [shutdown](#shutdown)
	* [Maintenance Events](#maintenance-events)
		+ [tick](#tick)
		+ [minute](#minute)
			- [:MM](#mm)
			- [HH:MM](#hhmm)
		+ [hour](#hour)
		+ [day](#day)
		+ [month](#month)
		+ [year](#year)
- [Configuration](#configuration)
	* [Command-Line Arguments](#command-line-arguments)
		+ [Optional Echo Categories](#optional-echo-categories)
	* [Multi-File Configuration](#multi-file-configuration)
	* [Config Overrides File](#config-overrides-file)
	* [Environment Variables](#environment-variables)
- [Logging](#logging)
	* [Log Filtering](#log-filtering)
- [Component Development](#component-development)
	* [Startup and Shutdown](#startup-and-shutdown)
	* [Accessing Your Configuration](#accessing-your-configuration)
	* [Accessing The Root Server](#accessing-the-root-server)
	* [Accessing Other Components](#accessing-other-components)
	* [Accessing The Server Log](#accessing-the-server-log)
- [Uncaught Exceptions](#uncaught-exceptions)
- [License](#license)

</details>

# Overview

This module is a generic server daemon framework, which supports a component plug-in system.  It can be used as a basis to create custom daemons such as web app backends.  It provides basic services such as configuration file loading, command-line argument parsing, logging, and more.  Component plug-ins can be created by you, or you can use some pre-made ones.

# Usage

Use [npm](https://www.npmjs.com/) to install the module:

```sh
npm install pixl-server
```

Then use `require()` to load it in your code:

```js
const PixlServer = require('pixl-server');
```

Then instantiate a server object and start it up:

```js
let server = new PixlServer({
	
	__name: 'MyServer',
	__version: "1.0",
	
	config: {
		"log_dir": "/let/log",
		"debug_level": 9,
		"uid": "www"
	},
	
	components: []
	
});
server.startup( function() {
	// startup complete
} );
```

Of course, this example won't actually do anything useful, because the server has no components.  Let's add a web server component to our server, just to show how it works:

```js
let PixlServer = require('pixl-server');

let server = new PixlServer({
	
	__name: 'MyServer',
	__version: "1.0",
	
	config: {
		"log_dir": "/let/log",
		"debug_level": 9,
		"uid": "www",
		
		"WebServer": {
			"http_port": 80,
			"http_htdocs_dir": "/let/www/html"
		}
	},
	
	components: [
		require('pi
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-tools.md`
```markdown
# 📦 jhuckaby/pixl-tools [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-tools


## Meta
- **Stars:** ⭐ 5 | **Forks:** 🍴 3
- **Language:** JavaScript | **License:** NOASSERTION
- **Last updated:** 2026-01-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A set of miscellaneous utility functions for Node.JS.

## README (trích đầu)
```
<details><summary>Table of Contents</summary>

<!-- toc -->
- [Overview](#overview)
- [Usage](#usage)
- [Function List](#function-list)
	* [timeNow](#timenow)
	* [generateUniqueID](#generateuniqueid)
	* [generateUniqueBase64](#generateuniquebase64)
	* [generateShortID](#generateshortid)
	* [digestHex](#digesthex)
	* [digestBase64](#digestbase64)
	* [numKeys](#numkeys)
	* [firstKey](#firstkey)
	* [hashKeysToArray](#hashkeystoarray)
	* [hashValuesToArray](#hashvaluestoarray)
	* [isaHash](#isahash)
	* [isaArray](#isaarray)
	* [copyHash](#copyhash)
	* [copyHashRemoveKeys](#copyhashremovekeys)
	* [copyHashRemoveProto](#copyhashremoveproto)
	* [mergeHashes](#mergehashes)
	* [mergeHashInto](#mergehashinto)
	* [parseQueryString](#parsequerystring)
	* [composeQueryString](#composequerystring)
	* [findObjectsIdx](#findobjectsidx)
	* [findObjectIdx](#findobjectidx)
	* [findObject](#findobject)
	* [findObjects](#findobjects)
	* [findObjectDeep](#findobjectdeep)
	* [findObjectsDeep](#findobjectsdeep)
	* [deleteObject](#deleteobject)
	* [deleteObjects](#deleteobjects)
	* [alwaysArray](#alwaysarray)
	* [sub](#sub)
	* [setPath](#setpath)
	* [getPath](#getpath)
	* [deletePath](#deletepath)
	* [getDateArgs](#getdateargs)
	* [getTimeFromArgs](#gettimefromargs)
	* [normalizeTime](#normalizetime)
	* [formatDate](#formatdate)
	* [getTextFromBytes](#gettextfrombytes)
	* [getBytesFromText](#getbytesfromtext)
	* [commify](#commify)
	* [shortFloat](#shortfloat)
	* [pct](#pct)
	* [zeroPad](#zeropad)
	* [clamp](#clamp)
	* [lerp](#lerp)
	* [getTextFromSeconds](#gettextfromseconds)
	* [getSecondsFromText](#getsecondsfromtext)
	* [getNiceRemainingTime](#getniceremainingtime)
	* [randArray](#randarray)
	* [pluralize](#pluralize)
	* [escapeRegExp](#escaperegexp)
	* [ucfirst](#ucfirst)
	* [getErrorDescription](#geterrordescription)
	* [bufferSplit](#buffersplit)
	* [fileEachLine](#fileeachline)
	* [getpwnam](#getpwnam)
	* [getgrnam](#getgrnam)
	* [tween](#tween)
	* [findFiles](#findfiles)
	* [findFilesSync](#findfilessync)
	* [walkDir](#walkdir)
	* [walkDirSync](#walkdirsync)
	* [glob](#glob)
	* [globSync](#globsync)
	* [rimraf](#rimraf)
	* [rimrafSync](#rimrafsync)
	* [mkdirp](#mkdirp)
	* [mkdirpSync](#mkdirpsync)
	* [writeFileAtomic](#writefileatomic)
	* [writeFileAtomicSync](#writefileatomicsync)
	* [parseJSON](#parsejson)
	* [findBin](#findbin)
	* [findBinSync](#findbinsync)
	* [sortBy](#sortby)
	* [includesAny](#includesany)
	* [includesAll](#includesall)
	* [stripANSI](#stripansi)
	* [noop](#noop)
- [Misc](#misc)
	* [async](#async)
	* [isLinux](#islinux)
	* [isMac](#ismac)
	* [isWindows](#iswindows)
	* [NEVER_MATCH](#never_match)
	* [MATCH_ANSI](#match_ansi)
	* [MATCH_BAD_KEY](#match_bad_key)
- [License](#license)

</details>

# Overview

This module contains a set of miscellaneous utility functions that don't fit into any particular category.

# Usage

Use [npm](https://www.npmjs.com/) to install the module:

```sh
npm install pixl-tools
```

Then use `require()` to load i
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pixl-unit.md`
```markdown
# 📦 jhuckaby/pixl-unit [🔖 PENDING/APPROVE]
🔗 https://github.com/jhuckaby/pixl-unit


## Meta
- **Stars:** ⭐ 2 | **Forks:** 🍴 1
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-01-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A very simple unit test runner for Node.JS.

## README (trích đầu)
```
# Overview

This module is a very simple unit test runner.

# Usage

Use [npm](https://www.npmjs.com/) to install the module as a command-line executable:

```
sudo npm install -g pixl-unit
```

Then call it using `pixl-unit` and specify a path to your unit test file or directory:

```
pixl-unit /path/to/your/unit/tests.js
```

You may specify multiple files and/or directories, separated by spaces.  If you specify directories, the script will scan the contents and execute all JS files within (one level deep only).

```
pixl-unit /path/to/your/unit/test/dir/
```

## Command-Line Arguments

Specify command-line arguments using the format `--key value` and do this *after* any and all unit test files / directories.  The following command-line switches are supported:

| Argument | Default Value | Description |
| -------- | ------------- | ----------- |
| `threads` | 1 | The total number of threads to use when executing tests.  See warning below. | 
| `verbose` | 0 | Set this to `1` to enable verbose output to the console. | 
| `quiet` | 0 | Set this to `1` to suppress all output to the console. | 
| `color` | 1 | Enables or disables color output using the chalk module. | 
| `fatal` | 0 | Set this to `1` to exit immediately after the first assertion failure (includes stack trace). | 
| `output` | "" | Set this to a file path to emit a JSON report (works with quiet mode). | 
| `delay` | 0 | Insert a delay between each test by setting this to the desired number of seconds. |
| `times` | 1 | Run the tests a specified number of times. |

Here is an example, which runs all the tests in `tests.js`, enables quiet mode, and generates a JSON report file:

```
pixl-unit /path/to/tests.js --quiet --output /var/tmp/unit-results.json
```

Please be careful when increasing the `--threads` setting, beyond the default value of `1`.  This will cause multiple tests to run simultaneously.  If any of your tests rely on previous tests completing, this will not go well.

## Use in Modules

To use `pixl-unit` in your own npm module, first declare it in your `package.json` in the `devDependencies` section:

```javascript
"devDependencies": {
	"pixl-unit": "*"
}
```

Then add a test script command to your `scripts` section:

```javascript
"scripts": {
	"test": "pixl-unit test/*.js"
}
```

This example assumes you have a `test/` directory in your module containing one or more JS files containing unit tests compatible with `pixl-unit`.

Then you can simply type `npm test` to run your module's unit tests.

## Sample Output

`pixl-unit` outputs to the console by default, using the [chalk](https://www.npmjs.com/package/chalk) module for ANSI color.  Stats are summarized at the bottom.  You can also suppress this output and/or generate a JSON report file (see below).

```
Simple Unit Test Runner v1.0
Sat Mar 07 2015 12:50:11 GMT-0800 (PST)

Args: {"threads":1,"verbose":0,"quiet":0,"color":1,"fatal":0,"output":""}
Suites: ["/Users/jhuckaby/node_modules/pixl-unit/test.js"]

Suite: /Us
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

