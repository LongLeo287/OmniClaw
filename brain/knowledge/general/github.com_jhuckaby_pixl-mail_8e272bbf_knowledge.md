---
id: github.com-jhuckaby-pixl-mail-8e272bbf-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:15.394078
---

# KNOWLEDGE EXTRACT: github.com_jhuckaby_pixl-mail_8e272bbf
> **Extracted on:** 2026-04-01 08:49:51
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519821/github.com_jhuckaby_pixl-mail_8e272bbf

---

## File: `.npmignore`
```
.gitignore
node_modules/
test.js
```

## File: `README.md`
```markdown
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
	if (err) console.log(err);
} );
```

So in this case our e-mail template has several placeholders, including `[email]`, `[full_name]` and `[username]`.  These are pulled from the `user` object which is passed to `send()` as the 2nd argument.  So the final e-mail that would be sent is:

```
To: jhuckaby@email.com
From: support@myapp.com
Subject: Welcome to My App, Joseph Huckaby!

Dear Joseph Huckaby,
Welcome to My App!  Your username is 'jhuckaby'.
```

You can actually use a complex hash / array tree of arguments, and then specify `[filesystem/style/paths]` or `[dot.style.paths]` in your placeholders.  See the [sub()](https://github.com/jhuckaby/pixl-tools#sub) docs for details.

## Loading From Files

You can specify a file path instead of the raw message, like this:

```js
let user = {
	username: "jhuckaby",
	full_name: "Joseph Huckaby",
	email: "jhuckaby@email.com"
};

mail.send( "conf/emails/new_user_welcome.txt", user, function(err) {
	if (err) console.log(err);
} );
```

## Attachments

To attach files, include an `attachments` array in your `args` object, and specify a `filename` and `path` for each one.  This is passed directly to [nodemailer](https://nodemailer.com/), so you can use all of their attachment features.  Example:

```js
let args = {
	attachments: [
		{ filename: "contract.pdf", path: "files/contracts/4573D.PDF" },
		{ filename: "policy.pdf", path: "files/misc/POLICY-2015.PDF" }
	]
};

mail.send( message, args, function(err) {
	if (err) console.error( "Mail Error: " + err );
} );
```

For details, see the [Attachments](https://nodemailer.com/message/attachments/) section in the [nodemailer](https://nodemailer.com/) docs.

## HTML Emails

If you want to send HTML formatted e-mails, the library will automatically detect this.  Just provide the headers in plain text, two end-of-lines, then start your HTML markup.  Example:

```js
let message = 
	"To: president@whitehouse.gov\n" + 
	"From: citizen@email.com\n" + 
	"Subject: State Budget\n" + 
	"\n" + 
	"<h1>Dear Mr. President,</h1>\n<p><b>Please</b> give our state more <i>money</i>.</p>\n";

mail.send( message, function(err) {
	if (err) console.error( "Mail Error: " + err );
} );
```

**Note:** Your e-mail body must begin with an HTML tag for it to be recognized.

## Options

You can set a number of options using the `setOption()` or `setOptions()` methods.  These are passed directly to the underlying [nodemailer](https://nodemailer.com/) module, so please check out their documentation for details.  Examples include setting timeouts, SSL, and authentication.

The `setOption()` method takes one single key/value to set or replace, while `setOptions()` accepts an object containing multiple keys/values.

```js
mail.setOption( 'secure', true ); // use ssl
mail.setOption( 'auth', { user: 'fsmith', pass: '12345' } );

mail.setOptions({
	connectionTimeout: 10000, // milliseconds
	greetingTimeout: 10000, // milliseconds
	socketTimeout: 10000 // milliseconds
});
```

You can also use local [sendmail](https://nodemailer.com/transports/sendmail/), if you have that configured on your server.  To do this, set the following options, and tune as needed:

```js
mail.setOptions({
	"sendmail": true,
	"newline": "unix",
	"path": "/usr/sbin/sendmail"
});
```

## Logging

You can optionally attach a [pixl-logger](https://github.com/jhuckaby/pixl-logger) compatible log agent, which will log all the [nodemailer](https://nodemailer.com/) debug messages at level 9, with the component column set to `Mailer`.  To use this feature, call the `attachLogAgent()` method on your class instance, and pass in your pixl-logger instance:

```js
mail.attachLogAgent( logger );
```

## Debugging

The `send()` method actually returns three arguments: the error (if any), the final composed mail body with headers (after all macro expansion), and a full debug log capture from [nodemailer](https://nodemailer.com/).  Here is how to use them:

```js
mail.send( message, function(err, message, log) {
	if (err) console.error( "Mail Error: " + err );
	
	console.log( "Full composed message: " + message );
	
	log.forEach( function(row) {
		console.log( ...row );
	} );
} );
```

Each log row will contain two elements: the log message itself, and an object containing additional metadata.  These come directly from [nodemailer](https://nodemailer.com/).  Here is an example excerpt:

```
Creating transport: nodemailer (6.4.11; +https://nodemailer.com/; SMTP/6.4.11[client:6.4.11])
{"component":"mail","tnx":"create"}

Sending mail using SMTP/6.4.11[client:6.4.11]
{"component":"mail","tnx":"transport","name":"SMTP","version":"6.4.11[client:6.4.11]","action":"send"}

Resolved localhost as ::1 [cache miss]
{"component":"smtp-connection","sid":"N5uAYhHPKsY","tnx":"dns","source":"localhost","resolved":"::1","cached":false}

Connection established to ::1:25
{"component":"smtp-connection","sid":"N5uAYhHPKsY","tnx":"network","localAddress":"::1","localPort":53068,"remoteAddress":"::1","remotePort":25}

220 joemax.local ESMTP Postfix
{"component":"smtp-connection","sid":"N5uAYhHPKsY","tnx":"server"}

EHLO joemax.local
{"component":"smtp-connection","sid":"N5uAYhHPKsY","tnx":"client"}
```

# License

**The MIT License (MIT)**

*Copyright (c) 2015 - 2024 Joseph Huckaby.*

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

## File: `mail.js`
```javascript
// Simple SMTP Email Sender
// Copyright (c) 2015 - 2024 Joseph Huckaby
// Released under the MIT License

const fs = require('fs');
const util = require('util');
const nodemailer = require('nodemailer');
const Tools = require('pixl-tools');

module.exports = class Mailer {
	
	constructor(host, port) {
		// class constructor
		this.options = {
			host: host || '127.0.0.1',
			port: port || 25
		};
	}
	
	setOption(key, value) {
		// set single option
		this.options[key] = value;
	}
	
	setOptions(opts) {
		// set multiple options
		for (var key in opts) {
			this.options[key] = opts[key];
		}
	}
	
	attachLogAgent(agent) {
		// attach pixl-logger compatible log agent
		this.logger = agent;
	}
	
	send(data, args, callback) {
		// send e-mail
		var self = this;
		
		// support 2-argument convention (data and callback only)
		if (!callback && (typeof(args) == 'function')) {
			callback = args;
			args = null;
		}
		
		// support buffers
		if (data instanceof Buffer) {
			data = data.toString();
		}
		
		// support loading files
		if (!data.match(/\n/)) {
			fs.readFile(data, { encoding: 'utf8' }, function (err, data) {
				if (err) callback(err);
				else self.send( data, args, callback );
			} );
			return;
		}
		
		// support null callback
		if (!callback) callback = function() {};
		
		// perform placeholder substitution on body
		if (args) data = Tools.sub( data, args );
		
		// fix line endings
		data = data.replace(/\r\n/g, "\n").replace(/\r/g, "\n");
		
		// split out headers and body
		var parts = data.split(/\n\n/);
		var headers_raw = parts.shift();
		var body_raw = parts.join("\n\n");
		if (!body_raw.match(/\S/)) return callback( new Error("Cannot locate e-mail body."), data );
		
		// parse headers into key/value pairs
		var headers = {};
		headers_raw.replace(/([\w\-]+)\:\s*([^\n]*)/g, function(m_all, m1, m2) {
			headers[ m1 ] = m2;
			return '';
		} );
		
		// grab to, from and subject
		var to = headers['To'];
		var from = headers['From'];
		var subject = headers['Subject'];
		
		if (!to) return callback( new Error("Missing required header: 'To'"), data );
		if (!from) return callback( new Error("Missing required header: 'From'"), data );
		if (!subject) return callback( new Error("Missing required header: 'Subject'"), data );
		
		delete headers['To'];
		delete headers['From'];
		delete headers['Subject'];
		
		if (this.options.sendmail) {
			delete this.options.host;
			delete this.options.port;
		}
		
		// capture debug trace from nodemailer, and log if configured
		// also send it back with response, whatever the result
		this.options.debug = true;
		this.options.logger = {};
		var log = [];
		
		['trace', 'debug', 'info', 'warn', 'error', 'fatal'].forEach( function(level) {
			self.options.logger[level] = function(entry, message, ...args) {
				if (!entry) entry = {};
				message = util.format(message, ...args);
				self.logDebug(9, message, entry);
				log.push([ message, { date: Tools.timeNow(), level, ...entry } ]);
			};
		} );
		
		// setup transport
		var transport = nodemailer.createTransport(this.options);
		
		var opts = {
			from: from,
			to: to,
			subject: subject
		};
		
		// support cc and bcc
		if (headers['Cc']) { opts.cc = headers['Cc']; delete headers['Cc']; }
		if (headers['Bcc']) { opts.bcc = headers['Bcc']; delete headers['Bcc']; }
		
		// custom headers
		if (Tools.numKeys(headers)) opts.headers = headers;
		
		// attachments
		if (args && args.attachments) opts.attachments = args.attachments;
		
		// auto-detect html or text
		if (body_raw.match(/^\s*</)) opts.html = body_raw;
		else opts.text = body_raw;
		
		// send mail
		transport.sendMail( opts, function(err) {
			callback( err, data, log );
		} );
	}
	
	logDebug(level, msg, data) {
		// log if we have an attached agent
		if (this.logger) {
			this.logger.set( 'component', 'Mailer' );
			this.logger.debug( level, msg, data );
		}
	}
	
};
```

## File: `package.json`
```json
{
	"name": "pixl-mail",
	"version": "1.1.6",
	"description": "A very simple class for sending e-mail via SMTP.",
	"author": "Joseph Huckaby <jhuckaby@gmail.com>",
	"homepage": "https://github.com/jhuckaby/pixl-mail",
	"license": "MIT",
	"main": "mail.js",
	"repository": {
		"type": "git",
		"url": "https://github.com/jhuckaby/pixl-mail"
	},
	"bugs": {
		"url": "https://github.com/jhuckaby/pixl-mail/issues"
	},
	"keywords": [
		"mail",
		"email",
		"smtp"
	],
	"dependencies": {
		"nodemailer": "8.0.4",
		"pixl-tools": "^2.0.2"
	},
	"devDependencies": {
		
	}
}
```

