---
id: ws-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.147741
---

# KNOWLEDGE EXTRACT: ws
> **Extracted on:** 2026-03-30 13:53:01
> **Source:** ws

---

## File: `.gitattributes`
```
* text=auto eol=lf
```

## File: `.gitignore`
```
node_modules/
.nyc_output/
coverage/
.vscode/
```

## File: `.npmrc`
```
package-lock=false
```

## File: `.prettierrc.yaml`
```yaml
arrowParens: always
endOfLine: lf
proseWrap: always
singleQuote: true
trailingComma: none
```

## File: `browser.js`
```javascript
'use strict';

module.exports = function () {
  throw new Error(
    'ws does not work in the browser. Browser clients must use the native ' +
      'WebSocket object'
  );
};
```

## File: `eslint.config.js`
```javascript
'use strict';

const pluginPrettierRecommended = require('eslint-plugin-prettier/recommended');
const globals = require('globals');
const js = require('@eslint/js');

module.exports = [
  js.configs.recommended,
  {
    ignores: ['.nyc_output/', '.vscode/', 'coverage/', 'node_modules/'],
    languageOptions: {
      ecmaVersion: 'latest',
      globals: {
        ...globals.browser,
        ...globals.mocha,
        ...globals.node
      },
      sourceType: 'module'
    },
    rules: {
      'no-console': 'off',
      'no-unused-vars': ['error', { caughtErrors: 'none' }],
      'no-var': 'error',
      'prefer-const': 'error'
    }
  },
  pluginPrettierRecommended
];
```

## File: `FUNDING.json`
```json
{
  "drips": {
    "ethereum": {
      "ownedBy": "0x3D4f997A071d2BA735AC767E68052679423c3dBe"
    }
  }
}
```

## File: `index.js`
```javascript
'use strict';

const createWebSocketStream = require('./lib/stream');
const extension = require('./lib/extension');
const PerMessageDeflate = require('./lib/permessage-deflate');
const Receiver = require('./lib/receiver');
const Sender = require('./lib/sender');
const subprotocol = require('./lib/subprotocol');
const WebSocket = require('./lib/websocket');
const WebSocketServer = require('./lib/websocket-server');

WebSocket.createWebSocketStream = createWebSocketStream;
WebSocket.extension = extension;
WebSocket.PerMessageDeflate = PerMessageDeflate;
WebSocket.Receiver = Receiver;
WebSocket.Sender = Sender;
WebSocket.Server = WebSocketServer;
WebSocket.subprotocol = subprotocol;
WebSocket.WebSocket = WebSocket;
WebSocket.WebSocketServer = WebSocketServer;

module.exports = WebSocket;
```

## File: `LICENSE`
```
Copyright (c) 2011 Einar Otto Stangvik <einaros@gmail.com>
Copyright (c) 2013 Arnout Kazemier and contributors
Copyright (c) 2016 Luigi Pinca and contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `package.json`
```json
{
  "name": "ws",
  "version": "8.20.0",
  "description": "Simple to use, blazing fast and thoroughly tested websocket client and server for Node.js",
  "keywords": [
    "HyBi",
    "Push",
    "RFC-6455",
    "WebSocket",
    "WebSockets",
    "real-time"
  ],
  "homepage": "https://github.com/websockets/ws",
  "bugs": "https://github.com/websockets/ws/issues",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/websockets/ws.git"
  },
  "author": "Einar Otto Stangvik <einaros@gmail.com> (http://2x.io)",
  "license": "MIT",
  "main": "index.js",
  "exports": {
    ".": {
      "browser": "./browser.js",
      "import": "./wrapper.mjs",
      "require": "./index.js"
    },
    "./package.json": "./package.json"
  },
  "browser": "browser.js",
  "engines": {
    "node": ">=10.0.0"
  },
  "files": [
    "browser.js",
    "index.js",
    "lib/*.js",
    "wrapper.mjs"
  ],
  "scripts": {
    "test": "nyc --reporter=lcov --reporter=text mocha --throw-deprecation test/*.test.js",
    "integration": "mocha --throw-deprecation test/*.integration.js",
    "lint": "eslint . && prettier --check --ignore-path .gitignore \"**/*.{json,md,yaml,yml}\""
  },
  "peerDependencies": {
    "bufferutil": "^4.0.1",
    "utf-8-validate": ">=5.0.2"
  },
  "peerDependenciesMeta": {
    "bufferutil": {
      "optional": true
    },
    "utf-8-validate": {
      "optional": true
    }
  },
  "devDependencies": {
    "@eslint/js": "^10.0.1",
    "benchmark": "^2.1.4",
    "bufferutil": "^4.0.1",
    "eslint": "^10.0.1",
    "eslint-config-prettier": "^10.0.1",
    "eslint-plugin-prettier": "^5.0.0",
    "globals": "^17.0.0",
    "mocha": "^8.4.0",
    "nyc": "^15.0.0",
    "prettier": "^3.0.0",
    "utf-8-validate": "^6.0.0"
  }
}
```

## File: `README.md`
```markdown
# ws: a Node.js WebSocket library

[![Version npm](https://img.shields.io/npm/v/ws.svg?logo=npm)](https://www.npmjs.com/package/ws)
[![CI](https://img.shields.io/github/actions/workflow/status/websockets/ws/ci.yml?branch=master&label=CI&logo=github)](https://github.com/websockets/ws/actions?query=workflow%3ACI+branch%3Amaster)
[![Coverage Status](https://img.shields.io/coveralls/websockets/ws/master.svg?logo=coveralls)](https://coveralls.io/github/websockets/ws)

ws is a simple to use, blazing fast, and thoroughly tested WebSocket client and
server implementation.

Passes the quite extensive Autobahn test suite: [server][server-report],
[client][client-report].

**Note**: This module does not work in the browser. The client in the docs is a
reference to a backend with the role of a client in the WebSocket communication.
Browser clients must use the native
[`WebSocket`](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
object. To make the same code work seamlessly on Node.js and the browser, you
can use one of the many wrappers available on npm, like
[isomorphic-ws](https://github.com/heineiuo/isomorphic-ws).

## Table of Contents

- [Protocol support](#protocol-support)
- [Installing](#installing)
  - [Opt-in for performance](#opt-in-for-performance)
    - [Legacy opt-in for performance](#legacy-opt-in-for-performance)
- [API docs](#api-docs)
- [WebSocket compression](#websocket-compression)
- [Usage examples](#usage-examples)
  - [Sending and receiving text data](#sending-and-receiving-text-data)
  - [Sending binary data](#sending-binary-data)
  - [Simple server](#simple-server)
  - [External HTTP/S server](#external-https-server)
  - [Multiple servers sharing a single HTTP/S server](#multiple-servers-sharing-a-single-https-server)
  - [Client authentication](#client-authentication)
  - [Server broadcast](#server-broadcast)
  - [Round-trip time](#round-trip-time)
  - [Use the Node.js streams API](#use-the-nodejs-streams-api)
  - [Other examples](#other-examples)
- [FAQ](#faq)
  - [How to get the IP address of the client?](#how-to-get-the-ip-address-of-the-client)
  - [How to detect and close broken connections?](#how-to-detect-and-close-broken-connections)
  - [How to connect via a proxy?](#how-to-connect-via-a-proxy)
- [Changelog](#changelog)
- [License](#license)

## Protocol support

- **HyBi drafts 07-12** (Use the option `protocolVersion: 8`)
- **HyBi drafts 13-17** (Current default, alternatively option
  `protocolVersion: 13`)

## Installing

```
npm install ws
```

### Opt-in for performance

[bufferutil][] is an optional module that can be installed alongside the ws
module:

```
npm install --save-optional bufferutil
```

This is a binary addon that improves the performance of certain operations such
as masking and unmasking the data payload of the WebSocket frames. Prebuilt
binaries are available for the most popular platforms, so you don't necessarily
need to have a C++ compiler installed on your machine.

To force ws to not use bufferutil, use the
[`WS_NO_BUFFER_UTIL`](./doc/ws.md#ws_no_buffer_util) environment variable. This
can be useful to enhance security in systems where a user can put a package in
the package search path of an application of another user, due to how the
Node.js resolver algorithm works.

#### Legacy opt-in for performance

If you are running on an old version of Node.js (prior to v18.14.0), ws also
supports the [utf-8-validate][] module:

```
npm install --save-optional utf-8-validate
```

This contains a binary polyfill for [`buffer.isUtf8()`][].

To force ws not to use utf-8-validate, use the
[`WS_NO_UTF_8_VALIDATE`](./doc/ws.md#ws_no_utf_8_validate) environment variable.

## API docs

See [`/doc/ws.md`](./doc/ws.md) for Node.js-like documentation of ws classes and
utility functions.

## WebSocket compression

ws supports the [permessage-deflate extension][permessage-deflate] which enables
the client and server to negotiate a compression algorithm and its parameters,
and then selectively apply it to the data payloads of each WebSocket message.

The extension is disabled by default on the server and enabled by default on the
client. It adds a significant overhead in terms of performance and memory
consumption so we suggest to enable it only if it is really needed.

Note that Node.js has a variety of issues with high-performance compression,
where increased concurrency, especially on Linux, can lead to [catastrophic
memory fragmentation][node-zlib-bug] and slow performance. If you intend to use
permessage-deflate in production, it is worthwhile to set up a test
representative of your workload and ensure Node.js/zlib will handle it with
acceptable performance and memory usage.

Tuning of permessage-deflate can be done via the options defined below. You can
also use `zlibDeflateOptions` and `zlibInflateOptions`, which is passed directly
into the creation of [raw deflate/inflate streams][node-zlib-deflaterawdocs].

See [the docs][ws-server-options] for more options.

```js
import WebSocket, { WebSocketServer } from 'ws';

const wss = new WebSocketServer({
  port: 8080,
  perMessageDeflate: {
    zlibDeflateOptions: {
      // See zlib defaults.
      chunkSize: 1024,
      memLevel: 7,
      level: 3
    },
    zlibInflateOptions: {
      chunkSize: 10 * 1024
    },
    // Other options settable:
    clientNoContextTakeover: true, // Defaults to negotiated value.
    serverNoContextTakeover: true, // Defaults to negotiated value.
    serverMaxWindowBits: 10, // Defaults to negotiated value.
    // Below options specified as default values.
    concurrencyLimit: 10, // Limits zlib concurrency for perf.
    threshold: 1024 // Size (in bytes) below which messages
    // should not be compressed if context takeover is disabled.
  }
});
```

The client will only use the extension if it is supported and enabled on the
server. To always disable the extension on the client, set the
`perMessageDeflate` option to `false`.

```js
import WebSocket from 'ws';

const ws = new WebSocket('ws://www.host.com/path', {
  perMessageDeflate: false
});
```

## Usage examples

### Sending and receiving text data

```js
import WebSocket from 'ws';

const ws = new WebSocket('ws://www.host.com/path');

ws.on('error', console.error);

ws.on('open', function open() {
  ws.send('something');
});

ws.on('message', function message(data) {
  console.log('received: %s', data);
});
```

### Sending binary data

```js
import WebSocket from 'ws';

const ws = new WebSocket('ws://www.host.com/path');

ws.on('error', console.error);

ws.on('open', function open() {
  const array = new Float32Array(5);

  for (var i = 0; i < array.length; ++i) {
    array[i] = i / 2;
  }

  ws.send(array);
});
```

### Simple server

```js
import { WebSocketServer } from 'ws';

const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', function connection(ws) {
  ws.on('error', console.error);

  ws.on('message', function message(data) {
    console.log('received: %s', data);
  });

  ws.send('something');
});
```

### External HTTP/S server

```js
import { createServer } from 'https';
import { readFileSync } from 'fs';
import { WebSocketServer } from 'ws';

const server = createServer({
  cert: readFileSync('/path/to/cert.pem'),
  key: readFileSync('/path/to/key.pem')
});
const wss = new WebSocketServer({ server });

wss.on('connection', function connection(ws) {
  ws.on('error', console.error);

  ws.on('message', function message(data) {
    console.log('received: %s', data);
  });

  ws.send('something');
});

server.listen(8080);
```

### Multiple servers sharing a single HTTP/S server

```js
import { createServer } from 'http';
import { WebSocketServer } from 'ws';

const server = createServer();
const wss1 = new WebSocketServer({ noServer: true });
const wss2 = new WebSocketServer({ noServer: true });

wss1.on('connection', function connection(ws) {
  ws.on('error', console.error);

  // ...
});

wss2.on('connection', function connection(ws) {
  ws.on('error', console.error);

  // ...
});

server.on('upgrade', function upgrade(request, socket, head) {
  const { pathname } = new URL(request.url, 'wss://base.url');

  if (pathname === '/foo') {
    wss1.handleUpgrade(request, socket, head, function done(ws) {
      wss1.emit('connection', ws, request);
    });
  } else if (pathname === '/bar') {
    wss2.handleUpgrade(request, socket, head, function done(ws) {
      wss2.emit('connection', ws, request);
    });
  } else {
    socket.destroy();
  }
});

server.listen(8080);
```

### Client authentication

```js
import { createServer } from 'http';
import { WebSocketServer } from 'ws';

function onSocketError(err) {
  console.error(err);
}

const server = createServer();
const wss = new WebSocketServer({ noServer: true });

wss.on('connection', function connection(ws, request, client) {
  ws.on('error', console.error);

  ws.on('message', function message(data) {
    console.log(`Received message ${data} from user ${client}`);
  });
});

server.on('upgrade', function upgrade(request, socket, head) {
  socket.on('error', onSocketError);

  // This function is not defined on purpose. Implement it with your own logic.
  authenticate(request, function next(err, client) {
    if (err || !client) {
      socket.write('HTTP/1.1 401 Unauthorized\r\n\r\n');
      socket.destroy();
      return;
    }

    socket.removeListener('error', onSocketError);

    wss.handleUpgrade(request, socket, head, function done(ws) {
      wss.emit('connection', ws, request, client);
    });
  });
});

server.listen(8080);
```

Also see the provided [example][session-parse-example] using `express-session`.

### Server broadcast

A client WebSocket broadcasting to all connected WebSocket clients, including
itself.

```js
import WebSocket, { WebSocketServer } from 'ws';

const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', function connection(ws) {
  ws.on('error', console.error);

  ws.on('message', function message(data, isBinary) {
    wss.clients.forEach(function each(client) {
      if (client.readyState === WebSocket.OPEN) {
        client.send(data, { binary: isBinary });
      }
    });
  });
});
```

A client WebSocket broadcasting to every other connected WebSocket clients,
excluding itself.

```js
import WebSocket, { WebSocketServer } from 'ws';

const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', function connection(ws) {
  ws.on('error', console.error);

  ws.on('message', function message(data, isBinary) {
    wss.clients.forEach(function each(client) {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(data, { binary: isBinary });
      }
    });
  });
});
```

### Round-trip time

```js
import WebSocket from 'ws';

const ws = new WebSocket('wss://websocket-echo.com/');

ws.on('error', console.error);

ws.on('open', function open() {
  console.log('connected');
  ws.send(Date.now());
});

ws.on('close', function close() {
  console.log('disconnected');
});

ws.on('message', function message(data) {
  console.log(`Round-trip time: ${Date.now() - data} ms`);

  setTimeout(function timeout() {
    ws.send(Date.now());
  }, 500);
});
```

### Use the Node.js streams API

```js
import WebSocket, { createWebSocketStream } from 'ws';

const ws = new WebSocket('wss://websocket-echo.com/');

const duplex = createWebSocketStream(ws, { encoding: 'utf8' });

duplex.on('error', console.error);

duplex.pipe(process.stdout);
process.stdin.pipe(duplex);
```

### Other examples

For a full example with a browser client communicating with a ws server, see the
examples folder.

Otherwise, see the test cases.

## FAQ

### How to get the IP address of the client?

The remote IP address can be obtained from the raw socket.

```js
import { WebSocketServer } from 'ws';

const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', function connection(ws, req) {
  const ip = req.socket.remoteAddress;

  ws.on('error', console.error);
});
```

When the server runs behind a proxy like NGINX, the de-facto standard is to use
the `X-Forwarded-For` header.

```js
wss.on('connection', function connection(ws, req) {
  const ip = req.headers['x-forwarded-for'].split(',')[0].trim();

  ws.on('error', console.error);
});
```

### How to detect and close broken connections?

Sometimes, the link between the server and the client can be interrupted in a
way that keeps both the server and the client unaware of the broken state of the
connection (e.g. when pulling the cord).

In these cases, ping messages can be used as a means to verify that the remote
endpoint is still responsive.

```js
import { WebSocketServer } from 'ws';

function heartbeat() {
  this.isAlive = true;
}

const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', function connection(ws) {
  ws.isAlive = true;
  ws.on('error', console.error);
  ws.on('pong', heartbeat);
});

const interval = setInterval(function ping() {
  wss.clients.forEach(function each(ws) {
    if (ws.isAlive === false) return ws.terminate();

    ws.isAlive = false;
    ws.ping();
  });
}, 30000);

wss.on('close', function close() {
  clearInterval(interval);
});
```

Pong messages are automatically sent in response to ping messages as required by
the spec.

Just like the server example above, your clients might as well lose connection
without knowing it. You might want to add a ping listener on your clients to
prevent that. A simple implementation would be:

```js
import WebSocket from 'ws';

function heartbeat() {
  clearTimeout(this.pingTimeout);

  // Use `WebSocket#terminate()`, which immediately destroys the connection,
  // instead of `WebSocket#close()`, which waits for the close timer.
  // Delay should be equal to the interval at which your server
  // sends out pings plus a conservative assumption of the latency.
  this.pingTimeout = setTimeout(() => {
    this.terminate();
  }, 30000 + 1000);
}

const client = new WebSocket('wss://websocket-echo.com/');

client.on('error', console.error);
client.on('open', heartbeat);
client.on('ping', heartbeat);
client.on('close', function clear() {
  clearTimeout(this.pingTimeout);
});
```

### How to connect via a proxy?

Use a custom `http.Agent` implementation like [https-proxy-agent][] or
[socks-proxy-agent][].

## Changelog

We're using the GitHub [releases][changelog] for changelog entries.

## License

[MIT](LICENSE)

[`buffer.isutf8()`]: https://nodejs.org/api/buffer.html#bufferisutf8input
[bufferutil]: https://github.com/websockets/bufferutil
[changelog]: https://github.com/websockets/ws/releases
[client-report]: http://websockets.github.io/ws/autobahn/clients/
[https-proxy-agent]: https://github.com/TooTallNate/node-https-proxy-agent
[node-zlib-bug]: https://github.com/nodejs/node/issues/8871
[node-zlib-deflaterawdocs]:
  https://nodejs.org/api/zlib.html#zlib_zlib_createdeflateraw_options
[permessage-deflate]: https://tools.ietf.org/html/rfc7692
[server-report]: http://websockets.github.io/ws/autobahn/servers/
[session-parse-example]: ./examples/express-session-parse
[socks-proxy-agent]: https://github.com/TooTallNate/node-socks-proxy-agent
[utf-8-validate]: https://github.com/websockets/utf-8-validate
[ws-server-options]: ./doc/ws.md#new-websocketserveroptions-callback
```

## File: `SECURITY.md`
```markdown
# Security Guidelines

Please contact us directly at **security@3rd-Eden.com** for any bug that might
impact the security of this project. Please prefix the subject of your email
with `[security]` in lowercase and square brackets. Our email filters will
automatically prevent these messages from being moved to our spam box.

You will receive an acknowledgement of your report within **24 hours**.

All emails that do not include security vulnerabilities will be removed and
blocked instantly.

## Exceptions

If you do not receive an acknowledgement within the said time frame, please give
us the benefit of the doubt as it's possible that we haven't seen it yet. In
this case, please send us a message **without details** using one of the
following methods:

- Contact the lead developers of this project on their personal e-mails. You can
  find the e-mails in the git logs, for example, using the following command:
  `git --no-pager show -s --format='%an <%ae>' <gitsha>` where `<gitsha>` is the
  SHA1 of their latest commit in the project.
- Create a GitHub issue stating contact details and the severity of the issue.

Once we have acknowledged receipt of your report and confirmed the bug
ourselves, we will work with you to fix the vulnerability and publicly
acknowledge your responsible disclosure, if you wish. In addition to that, we
will create and publish a security advisory to
[GitHub Security Advisories](https://github.com/websockets/ws/security/advisories?state=published).

## History

- 04 Jan 2016:
  [Buffer vulnerability](https://github.com/websockets/ws/releases/tag/1.0.1)
- 08 Nov 2017:
  [DoS in the `Sec-Websocket-Extensions` header parser](https://github.com/websockets/ws/releases/tag/3.3.1)
- 25 May 2021:
  [ReDoS in `Sec-Websocket-Protocol` header](https://github.com/websockets/ws/releases/tag/7.4.6)
- 16 Jun 2024:
  [DoS when handling a request with many HTTP headers](https://github.com/websockets/ws/releases/tag/8.17.1)
```

## File: `wrapper.mjs`
```
import createWebSocketStream from './lib/stream.js';
import extension from './lib/extension.js';
import PerMessageDeflate from './lib/permessage-deflate.js';
import Receiver from './lib/receiver.js';
import Sender from './lib/sender.js';
import subprotocol from './lib/subprotocol.js';
import WebSocket from './lib/websocket.js';
import WebSocketServer from './lib/websocket-server.js';

export {
  createWebSocketStream,
  extension,
  PerMessageDeflate,
  Receiver,
  Sender,
  subprotocol,
  WebSocket,
  WebSocketServer
};

export default WebSocket;
```

## File: `bench/parser.benchmark.js`
```javascript
'use strict';

const benchmark = require('benchmark');
const crypto = require('crypto');

const WebSocket = require('..');

const Receiver = WebSocket.Receiver;
const Sender = WebSocket.Sender;

const options = {
  fin: true,
  rsv1: false,
  mask: true,
  readOnly: false
};

function createBinaryFrame(length) {
  const list = Sender.frame(crypto.randomBytes(length), {
    opcode: 0x02,
    ...options
  });

  return Buffer.concat(list);
}

const pingFrame1 = Buffer.concat(
  Sender.frame(crypto.randomBytes(5), { opcode: 0x09, ...options })
);

const textFrame = Buffer.from('819461616161' + '61'.repeat(20), 'hex');
const pingFrame2 = Buffer.from('8980146e915a', 'hex');
const binaryFrame1 = createBinaryFrame(125);
const binaryFrame2 = createBinaryFrame(65535);
const binaryFrame3 = createBinaryFrame(200 * 1024);
const binaryFrame4 = createBinaryFrame(1024 * 1024);

const suite = new benchmark.Suite();
const receiver = new Receiver({
  binaryType: 'nodebuffer',
  extensions: {},
  isServer: true,
  skipUTF8Validation: false
});

suite.add('ping frame (5 bytes payload)', {
  defer: true,
  fn: (deferred) => {
    receiver.write(pingFrame1, deferred.resolve.bind(deferred));
  }
});
suite.add('ping frame (no payload)', {
  defer: true,
  fn: (deferred) => {
    receiver.write(pingFrame2, deferred.resolve.bind(deferred));
  }
});
suite.add('text frame (20 bytes payload)', {
  defer: true,
  fn: (deferred) => {
    receiver.write(textFrame, deferred.resolve.bind(deferred));
  }
});
suite.add('binary frame (125 bytes payload)', {
  defer: true,
  fn: (deferred) => {
    receiver.write(binaryFrame1, deferred.resolve.bind(deferred));
  }
});
suite.add('binary frame (65535 bytes payload)', {
  defer: true,
  fn: (deferred) => {
    receiver.write(binaryFrame2, deferred.resolve.bind(deferred));
  }
});
suite.add('binary frame (200 KiB payload)', {
  defer: true,
  fn: (deferred) => {
    receiver.write(binaryFrame3, deferred.resolve.bind(deferred));
  }
});
suite.add('binary frame (1 MiB payload)', {
  defer: true,
  fn: (deferred) => {
    receiver.write(binaryFrame4, deferred.resolve.bind(deferred));
  }
});

suite.on('cycle', (e) => console.log(e.target.toString()));

if (require.main === module) {
  suite.run({ async: true });
} else {
  module.exports = suite;
}
```

## File: `bench/sender.benchmark.js`
```javascript
'use strict';

const benchmark = require('benchmark');
const crypto = require('crypto');

const Sender = require('../').Sender;

const data1 = crypto.randomBytes(64);
const data2 = crypto.randomBytes(16 * 1024);
const data3 = crypto.randomBytes(64 * 1024);
const data4 = crypto.randomBytes(200 * 1024);
const data5 = crypto.randomBytes(1024 * 1024);

const opts1 = {
  readOnly: false,
  mask: false,
  rsv1: false,
  opcode: 2,
  fin: true
};
const opts2 = {
  readOnly: true,
  rsv1: false,
  mask: true,
  opcode: 2,
  fin: true
};

const suite = new benchmark.Suite();

suite.add('frame, unmasked (64 B)', () => Sender.frame(data1, opts1));
suite.add('frame, masked (64 B)', () => Sender.frame(data1, opts2));
suite.add('frame, unmasked (16 KiB)', () => Sender.frame(data2, opts1));
suite.add('frame, masked (16 KiB)', () => Sender.frame(data2, opts2));
suite.add('frame, unmasked (64 KiB)', () => Sender.frame(data3, opts1));
suite.add('frame, masked (64 KiB)', () => Sender.frame(data3, opts2));
suite.add('frame, unmasked (200 KiB)', () => Sender.frame(data4, opts1));
suite.add('frame, masked (200 KiB)', () => Sender.frame(data4, opts2));
suite.add('frame, unmasked (1 MiB)', () => Sender.frame(data5, opts1));
suite.add('frame, masked (1 MiB)', () => Sender.frame(data5, opts2));

suite.on('cycle', (e) => console.log(e.target.toString()));

if (require.main === module) {
  suite.run({ async: true });
} else {
  module.exports = suite;
}
```

## File: `bench/speed.js`
```javascript
'use strict';

const cluster = require('cluster');
const http = require('http');

const WebSocket = require('..');

const port = 8181;
const path = '';
// const path = '/tmp/wss.sock';

if (cluster.isMaster) {
  const server = http.createServer();
  const wss = new WebSocket.Server({
    maxPayload: 600 * 1024 * 1024,
    perMessageDeflate: false,
    clientTracking: false,
    server
  });

  wss.on('connection', (ws) => {
    ws.on('message', (data, isBinary) => {
      ws.send(data, { binary: isBinary });
    });
  });

  server.listen(path ? { path } : { port }, () => cluster.fork());

  cluster.on('exit', () => {
    wss.close();
    server.close();
  });
} else {
  const configs = [
    [true, 10000, 64],
    [true, 5000, 16 * 1024],
    [true, 1000, 128 * 1024],
    [true, 100, 1024 * 1024],
    [true, 1, 500 * 1024 * 1024],
    [false, 10000, 64],
    [false, 5000, 16 * 1024],
    [false, 1000, 128 * 1024],
    [false, 100, 1024 * 1024]
  ];

  const roundPrec = (num, prec) => {
    const mul = Math.pow(10, prec);
    return Math.round(num * mul) / mul;
  };

  const humanSize = (bytes) => {
    if (bytes >= 1073741824) return roundPrec(bytes / 1073741824, 2) + ' GiB';
    if (bytes >= 1048576) return roundPrec(bytes / 1048576, 2) + ' MiB';
    if (bytes >= 1024) return roundPrec(bytes / 1024, 2) + ' KiB';
    return roundPrec(bytes, 2) + ' B';
  };

  const largest = configs.reduce(
    (prev, curr) => (curr[2] > prev ? curr[2] : prev),
    0
  );
  console.log('Generating %s of test data...', humanSize(largest));
  const randomBytes = Buffer.allocUnsafe(largest);

  for (let i = 0; i < largest; ++i) {
    randomBytes[i] = ~~(Math.random() * 127);
  }

  console.log(`Testing ws on ${path || '[::]:' + port}`);

  const runConfig = (useBinary, roundtrips, size, cb) => {
    const data = randomBytes.slice(0, size);
    const url = path ? `ws+unix://${path}` : `ws://localhost:${port}`;
    const ws = new WebSocket(url, {
      maxPayload: 600 * 1024 * 1024
    });
    let roundtrip = 0;
    let time;

    ws.on('error', (err) => {
      console.error(err.stack);
      cluster.worker.disconnect();
    });
    ws.on('open', () => {
      time = process.hrtime();
      ws.send(data, { binary: useBinary });
    });
    ws.on('message', () => {
      if (++roundtrip !== roundtrips)
        return ws.send(data, { binary: useBinary });

      let elapsed = process.hrtime(time);
      elapsed = elapsed[0] * 1e9 + elapsed[1];

      console.log(
        '%d roundtrips of %s %s data:\t%ss\t%s',
        roundtrips,
        humanSize(size),
        useBinary ? 'binary' : 'text',
        roundPrec(elapsed / 1e9, 1),
        humanSize(((size * 2 * roundtrips) / elapsed) * 1e9) + '/s'
      );

      ws.close();
      cb();
    });
  };

  (function run() {
    if (configs.length === 0) return cluster.worker.disconnect();
    const config = configs.shift();
    config.push(run);
    runConfig.apply(null, config);
  })();
}
```

## File: `doc/ws.md`
```markdown
# ws

## Table of Contents

- [Class: WebSocketServer](#class-websocketserver)
  - [new WebSocketServer(options[, callback])](#new-websocketserveroptions-callback)
  - [Event: 'close'](#event-close)
  - [Event: 'connection'](#event-connection)
  - [Event: 'error'](#event-error)
  - [Event: 'headers'](#event-headers)
  - [Event: 'listening'](#event-listening)
  - [Event: 'wsClientError'](#event-wsclienterror)
  - [server.address()](#serveraddress)
  - [server.clients](#serverclients)
  - [server.close([callback])](#serverclosecallback)
  - [server.handleUpgrade(request, socket, head, callback)](#serverhandleupgraderequest-socket-head-callback)
  - [server.shouldHandle(request)](#servershouldhandlerequest)
- [Class: WebSocket](#class-websocket)
  - [Ready state constants](#ready-state-constants)
  - [new WebSocket(address[, protocols][, options])](#new-websocketaddress-protocols-options)
    - [IPC connections](#ipc-connections)
  - [Event: 'close'](#event-close-1)
  - [Event: 'error'](#event-error-1)
  - [Event: 'message'](#event-message)
  - [Event: 'open'](#event-open)
  - [Event: 'ping'](#event-ping)
  - [Event: 'pong'](#event-pong)
  - [Event: 'redirect'](#event-redirect)
  - [Event: 'unexpected-response'](#event-unexpected-response)
  - [Event: 'upgrade'](#event-upgrade)
  - [websocket.addEventListener(type, listener[, options])](#websocketaddeventlistenertype-listener-options)
  - [websocket.binaryType](#websocketbinarytype)
  - [websocket.bufferedAmount](#websocketbufferedamount)
  - [websocket.close([code[, reason]])](#websocketclosecode-reason)
  - [websocket.extensions](#websocketextensions)
  - [websocket.isPaused](#websocketispaused)
  - [websocket.onclose](#websocketonclose)
  - [websocket.onerror](#websocketonerror)
  - [websocket.onmessage](#websocketonmessage)
  - [websocket.onopen](#websocketonopen)
  - [websocket.pause()](#websocketpause)
  - [websocket.ping([data[, mask]][, callback])](#websocketpingdata-mask-callback)
  - [websocket.pong([data[, mask]][, callback])](#websocketpongdata-mask-callback)
  - [websocket.protocol](#websocketprotocol)
  - [websocket.readyState](#websocketreadystate)
  - [websocket.removeEventListener(type, listener)](#websocketremoveeventlistenertype-listener)
  - [websocket.resume()](#websocketresume)
  - [websocket.send(data[, options][, callback])](#websocketsenddata-options-callback)
  - [websocket.terminate()](#websocketterminate)
  - [websocket.url](#websocketurl)
- [createWebSocketStream(websocket[, options])](#createwebsocketstreamwebsocket-options)
- [Environment variables](#environment-variables)
  - [WS_NO_BUFFER_UTIL](#ws_no_buffer_util)
  - [WS_NO_UTF_8_VALIDATE](#ws_no_utf_8_validate)
- [Error codes](#error-codes)
  - [WS_ERR_EXPECTED_FIN](#ws_err_expected_fin)
  - [WS_ERR_EXPECTED_MASK](#ws_err_expected_mask)
  - [WS_ERR_INVALID_CLOSE_CODE](#ws_err_invalid_close_code)
  - [WS_ERR_INVALID_CONTROL_PAYLOAD_LENGTH](#ws_err_invalid_control_payload_length)
  - [WS_ERR_INVALID_OPCODE](#ws_err_invalid_opcode)
  - [WS_ERR_INVALID_UTF8](#ws_err_invalid_utf8)
  - [WS_ERR_UNEXPECTED_MASK](#ws_err_unexpected_mask)
  - [WS_ERR_UNEXPECTED_RSV_1](#ws_err_unexpected_rsv_1)
  - [WS_ERR_UNEXPECTED_RSV_2_3](#ws_err_unexpected_rsv_2_3)
  - [WS_ERR_UNSUPPORTED_DATA_PAYLOAD_LENGTH](#ws_err_unsupported_data_payload_length)
  - [WS_ERR_UNSUPPORTED_MESSAGE_LENGTH](#ws_err_unsupported_message_length)

## Class: WebSocketServer

This class represents a WebSocket server. It extends the `EventEmitter`.

### new WebSocketServer(options[, callback])

- `options` {Object}
  - `allowSynchronousEvents` {Boolean} Specifies whether any of the `'message'`,
    `'ping'`, and `'pong'` events can be emitted multiple times in the same
    tick. Defaults to `true`. Setting it to `false` improves compatibility with
    the WHATWG standard but may negatively impact performance.
  - `autoPong` {Boolean} Specifies whether or not to automatically send a pong
    in response to a ping. Defaults to `true`.
  - `backlog` {Number} The maximum length of the queue of pending connections.
  - `clientTracking` {Boolean} Specifies whether or not to track clients.
  - `closeTimeout` {Number} Duration in milliseconds to wait for a graceful
    close after [`websocket.close()`][] is called. If the limit is reached, the
    connection is forcibly terminated. Defaults to 30000.
  - `handleProtocols` {Function} A function which can be used to handle the
    WebSocket subprotocols. See description below.
  - `host` {String} The hostname where to bind the server.
  - `maxPayload` {Number} The maximum allowed message size in bytes. Defaults to
    100 MiB (104857600 bytes).
  - `noServer` {Boolean} Enable no server mode.
  - `path` {String} Accept only connections matching this path.
  - `perMessageDeflate` {Boolean|Object} Enable/disable permessage-deflate.
  - `port` {Number} The port where to bind the server.
  - `server` {http.Server|https.Server} A pre-created Node.js HTTP/S server.
  - `skipUTF8Validation` {Boolean} Specifies whether or not to skip UTF-8
    validation for text and close messages. Defaults to `false`. Set to `true`
    only if clients are trusted.
  - `verifyClient` {Function} A function which can be used to validate incoming
    connections. See description below. (Usage is discouraged: see
    [Issue #337](https://github.com/websockets/ws/issues/377#issuecomment-462152231))
  - `WebSocket` {Function} Specifies the `WebSocket` class to be used. It must
    be extended from the original `WebSocket`. Defaults to `WebSocket`.
- `callback` {Function}

Create a new server instance. One and only one of `port`, `server` or `noServer`
must be provided or an error is thrown. An HTTP server is automatically created,
started, and used if `port` is set. To use an external HTTP/S server instead,
specify only `server` or `noServer`. In this case, the HTTP/S server must be
started manually. The "noServer" mode allows the WebSocket server to be
completely detached from the HTTP/S server. This makes it possible, for example,
to share a single HTTP/S server between multiple WebSocket servers.

> **NOTE:** Use of `verifyClient` is discouraged. Rather handle client
> authentication in the `'upgrade'` event of the HTTP server. See examples for
> more details.

If `verifyClient` is not set, then the handshake is automatically accepted. If
it has a single parameter, then `ws` will invoke it with the following argument:

- `info` {Object}
  - `origin` {String} The value in the Origin header indicated by the client.
  - `req` {http.IncomingMessage} The client HTTP GET request.
  - `secure` {Boolean} `true` if `req.socket.authorized` or
    `req.socket.encrypted` is set.

The return value (`Boolean`) of the function determines whether or not to accept
the handshake.

If `verifyClient` has two parameters, then `ws` will invoke it with the
following arguments:

- `info` {Object} Same as above.
- `cb` {Function} A callback that must be called by the user upon inspection of
  the `info` fields. Arguments in this callback are:
  - `result` {Boolean} Whether or not to accept the handshake.
  - `code` {Number} When `result` is `false`, this field determines the HTTP
    error status code to be sent to the client.
  - `name` {String} When `result` is `false`, this field determines the HTTP
    reason phrase.
  - `headers` {Object} When `result` is `false`, this field determines
    additional HTTP headers to be sent to the client. For example,
    `{ 'Retry-After': 120 }`.

`handleProtocols` takes two arguments:

- `protocols` {Set} The list of WebSocket subprotocols indicated by the client
  in the `Sec-WebSocket-Protocol` header.
- `request` {http.IncomingMessage} The client HTTP GET request.

The returned value sets the value of the `Sec-WebSocket-Protocol` header in the
HTTP 101 response. If returned value is `false`, the header is not added in the
response.

If `handleProtocols` is not set, then the first of the client's requested
subprotocols is used.

`perMessageDeflate` can be used to control the behavior of [permessage-deflate
extension][permessage-deflate]. The extension is disabled when `false` (default
value). If an object is provided, then that is extension parameters:

- `serverNoContextTakeover` {Boolean} Whether to use context takeover or not.
- `clientNoContextTakeover` {Boolean} Acknowledge disabling of client context
  takeover.
- `serverMaxWindowBits` {Number} The value of `windowBits`.
- `clientMaxWindowBits` {Number} Request a custom client window size.
- `zlibDeflateOptions` {Object} [Additional options][zlib-options] to pass to
  zlib on deflate.
- `zlibInflateOptions` {Object} [Additional options][zlib-options] to pass to
  zlib on inflate.
- `threshold` {Number} Payloads smaller than this will not be compressed if
  context takeover is disabled. Defaults to 1024 bytes.
- `concurrencyLimit` {Number} The number of concurrent calls to zlib. Calls
  above this limit will be queued. Default 10. You usually won't need to touch
  this option. See [this issue][concurrency-limit] for more details.

If a property is empty, then either an offered configuration or a default value
is used. When sending a fragmented message, the length of the first fragment is
compared to the threshold. This determines if compression is used for the entire
message.

`callback` will be added as a listener for the `'listening'` event on the HTTP
server when the `port` option is set.

### Event: 'close'

Emitted when the server closes. This event depends on the `'close'` event of
HTTP server only when it is created internally. In all other cases, the event is
emitted independently.

### Event: 'connection'

- `websocket` {WebSocket}
- `request` {http.IncomingMessage}

Emitted when the handshake is complete. `request` is the http GET request sent
by the client. Useful for parsing authority headers, cookie headers, and other
information.

### Event: 'error'

- `error` {Error}

Emitted when an error occurs on the underlying server.

### Event: 'headers'

- `headers` {Array}
- `request` {http.IncomingMessage}

Emitted before the response headers are written to the socket as part of the
handshake. This allows you to inspect/modify the headers before they are sent.

### Event: 'listening'

Emitted when the underlying server has been bound.

### Event: 'wsClientError'

- `error` {Error}
- `socket` {net.Socket|tls.Socket}
- `request` {http.IncomingMessage}

Emitted when an error occurs before the WebSocket connection is established.
`socket` and `request` are respectively the socket and the HTTP request from
which the error originated. The listener of this event is responsible for
closing the socket. When the `'wsClientError'` event is emitted there is no
`http.ServerResponse` object, so any HTTP response, including the response
headers and body, must be written directly to the `socket`. If there is no
listener for this event, the socket is closed with a default 4xx response
containing a descriptive error message.

### server.address()

Returns an object with `port`, `family`, and `address` properties specifying the
bound address, the address family name, and port of the server as reported by
the operating system if listening on an IP socket. If the server is listening on
a pipe or UNIX domain socket, the name is returned as a string.

### server.clients

- {Set}

A set that stores all connected clients. This property is only added when the
`clientTracking` is truthy.

### server.close([callback])

Prevent the server from accepting new connections and close the HTTP server if
created internally. If an external HTTP server is used via the `server` or
`noServer` constructor options, it must be closed manually. Existing connections
are not closed automatically. The server emits a `'close'` event when all
connections are closed unless an external HTTP server is used and client
tracking is disabled. In this case, the `'close'` event is emitted in the next
tick. The optional callback is called when the `'close'` event occurs and
receives an `Error` if the server is already closed.

### server.handleUpgrade(request, socket, head, callback)

- `request` {http.IncomingMessage} The client HTTP GET request.
- `socket` {stream.Duplex} The network socket between the server and client.
- `head` {Buffer} The first packet of the upgraded stream.
- `callback` {Function}

Handle a HTTP upgrade request. When the HTTP server is created internally or
when the HTTP server is passed via the `server` option, this method is called
automatically. When operating in "noServer" mode, this method must be called
manually.

If the upgrade is successful, the `callback` is called with two arguments:

- `websocket` {WebSocket} A `WebSocket` object.
- `request` {http.IncomingMessage} The client HTTP GET request.

### server.shouldHandle(request)

- `request` {http.IncomingMessage} The client HTTP GET request.

See if a given request should be handled by this server. By default, this method
validates the pathname of the request, matching it against the `path` option if
provided. The return value, `true` or `false`, determines whether or not to
accept the handshake.

This method can be overridden when a custom handling logic is required.

## Class: WebSocket

This class represents a WebSocket. It extends the `EventEmitter`.

### Ready state constants

| Constant   | Value | Description                                      |
| ---------- | ----- | ------------------------------------------------ |
| CONNECTING | 0     | The connection is not yet open.                  |
| OPEN       | 1     | The connection is open and ready to communicate. |
| CLOSING    | 2     | The connection is in the process of closing.     |
| CLOSED     | 3     | The connection is closed.                        |

### new WebSocket(address[, protocols][, options])

- `address` {String|url.URL} The URL to which to connect.
- `protocols` {String|Array} The list of subprotocols.
- `options` {Object}
  - `allowSynchronousEvents` {Boolean} Specifies whether any of the `'message'`,
    `'ping'`, and `'pong'` events can be emitted multiple times in the same
    tick. Defaults to `true`. Setting it to `false` improves compatibility with
    the WHATWG standard but may negatively impact performance.
  - `autoPong` {Boolean} Specifies whether or not to automatically send a pong
    in response to a ping. Defaults to `true`.
  - `closeTimeout` {Number} Duration in milliseconds to wait for a graceful
    close after [`websocket.close()`][] is called. If the limit is reached, the
    connection is forcibly terminated. Defaults to 30000.
  - `finishRequest` {Function} A function which can be used to customize the
    headers of each HTTP request before it is sent. See description below.
  - `followRedirects` {Boolean} Whether or not to follow redirects. Defaults to
    `false`.
  - `generateMask` {Function} The function used to generate the masking key. It
    takes a `Buffer` that must be filled synchronously and is called before a
    message is sent, for each message. By default, the buffer is filled with
    cryptographically strong random bytes.
  - `handshakeTimeout` {Number} Timeout in milliseconds for the handshake
    request. This is reset after every redirection.
  - `maxPayload` {Number} The maximum allowed message size in bytes. Defaults to
    100 MiB (104857600 bytes).
  - `maxRedirects` {Number} The maximum number of redirects allowed. Defaults
    to 10.
  - `origin` {String} Value of the `Origin` or `Sec-WebSocket-Origin` header
    depending on the `protocolVersion`.
  - `perMessageDeflate` {Boolean|Object} Enable/disable permessage-deflate.
  - `protocolVersion` {Number} Value of the `Sec-WebSocket-Version` header.
  - `skipUTF8Validation` {Boolean} Specifies whether or not to skip UTF-8
    validation for text and close messages. Defaults to `false`. Set to `true`
    only if the server is trusted.
  - Any other option allowed in [`http.request()`][] or [`https.request()`][].
    Options given do not have any effect if parsed from the URL given with the
    `address` parameter.

Create a new WebSocket instance.

`perMessageDeflate` default value is `true`. When using an object, parameters
are the same of the server. The only difference is the direction of requests.
For example, `serverNoContextTakeover` can be used to ask the server to disable
context takeover.

`finishRequest` is called with arguments

- `request` {http.ClientRequest}
- `websocket` {WebSocket}

for each HTTP GET request (the initial one and any caused by redirects) when it
is ready to be sent, to allow for last minute customization of the headers. If
`finishRequest` is set, then it has the responsibility to call `request.end()`
once it is done setting request headers. This is intended for niche use-cases
where some headers can't be provided in advance e.g. because they depend on the
underlying socket.

#### IPC connections

`ws` supports IPC connections. To connect to an IPC endpoint, use the following
URL form:

- On Unices

  ```
  ws+unix:/absolute/path/to/uds_socket:/pathname?search_params
  ```

- On Windows

  ```
  ws+unix:\\.\pipe\pipe_name:/pathname?search_params
  ```

The character `:` is the separator between the IPC path (the UNIX domain socket
path or the Windows named pipe) and the URL path. The IPC path must not include
the characters `:` and `?`, otherwise the URL is incorrectly parsed. If the URL
path is omitted

```
ws+unix:/absolute/path/to/uds_socket
```

it defaults to `/`.

### Event: 'close'

- `code` {Number}
- `reason` {Buffer}

Emitted when the connection is closed. `code` is a numeric value indicating the
status code explaining why the connection has been closed. `reason` is a
`Buffer` containing a human-readable string explaining why the connection has
been closed.

### Event: 'error'

- `error` {Error}

Emitted when an error occurs. Errors may have a `.code` property, matching one
of the string values defined below under [Error codes](#error-codes).

### Event: 'message'

- `data` {ArrayBuffer|Blob|Buffer|Buffer[]}
- `isBinary` {Boolean}

Emitted when a message is received. `data` is the message content. `isBinary`
specifies whether the message is binary or not.

### Event: 'open'

Emitted when the connection is established.

### Event: 'ping'

- `data` {Buffer}

Emitted when a ping is received.

### Event: 'pong'

- `data` {Buffer}

Emitted when a pong is received.

### Event: 'redirect'

- `url` {String}
- `request` {http.ClientRequest}

Emitted before a redirect is followed. `url` is the redirect URL. `request` is
the HTTP GET request with the headers queued. This event gives the ability to
inspect confidential headers and remove them on a per-redirect basis using the
[`request.getHeader()`][] and [`request.removeHeader()`][] API. The `request`
object should be used only for this purpose. When there is at least one listener
for this event, no header is removed by default, even if the redirect is to a
different domain.

### Event: 'unexpected-response'

- `request` {http.ClientRequest}
- `response` {http.IncomingMessage}

Emitted when the server response is not the expected one, for example a 401
response. This event gives the ability to read the response in order to extract
useful information. If the server sends an invalid response and there isn't a
listener for this event, an error is emitted.

### Event: 'upgrade'

- `response` {http.IncomingMessage}

Emitted when response headers are received from the server as part of the
handshake. This allows you to read headers from the server, for example
'set-cookie' headers.

### websocket.addEventListener(type, listener[, options])

- `type` {String} A string representing the event type to listen for.
- `listener` {Function|Object} The listener to add.
- `options` {Object}
  - `once` {Boolean} A `Boolean` indicating that the listener should be invoked
    at most once after being added. If `true`, the listener would be
    automatically removed when invoked.

Register an event listener emulating the `EventTarget` interface. This method
does nothing if `type` is not one of `'close'`, `'error'`, `'message'`, or
`'open'`.

### websocket.binaryType

- {String}

A string indicating the type of binary data being transmitted by the connection.
This should be one of "nodebuffer", "arraybuffer", "blob", or "fragments".
Defaults to "nodebuffer". Type "fragments" will emit the array of fragments as
received from the sender, without copyfull concatenation, which is useful for
the performance of binary protocols transferring large messages with multiple
fragments.

### websocket.bufferedAmount

- {Number}

The number of bytes of data that have been queued using calls to `send()` but
not yet transmitted to the network. This deviates from the HTML standard in the
following ways:

1. If the data is immediately sent, the value is `0`.
1. All framing bytes are included.

### websocket.close([code[, reason]])

- `code` {Number} A numeric value indicating the status code explaining why the
  connection is being closed.
- `reason` {String|Buffer} The reason why the connection is closing.

Initiate a closing handshake.

### websocket.isPaused

- {Boolean}

Indicates whether the websocket is paused.

### websocket.extensions

- {Object}

An object containing the negotiated extensions.

### websocket.onclose

- {Function}

An event listener to be called when connection is closed. The listener receives
a `CloseEvent` named "close".

### websocket.onerror

- {Function}

An event listener to be called when an error occurs. The listener receives an
`ErrorEvent` named "error".

### websocket.onmessage

- {Function}

An event listener to be called when a message is received. The listener receives
a `MessageEvent` named "message".

### websocket.onopen

- {Function}

An event listener to be called when the connection is established. The listener
receives an `OpenEvent` named "open".

### websocket.pause()

Pause the websocket causing it to stop emitting events. Some events can still be
emitted after this is called, until all buffered data is consumed. This method
is a noop if the ready state is `CONNECTING` or `CLOSED`.

### websocket.ping([data[, mask]][, callback])

- `data`
  {Array|Number|Object|String|ArrayBuffer|Buffer|DataView|TypedArray|Blob} The
  data to send in the ping frame.
- `mask` {Boolean} Specifies whether `data` should be masked or not. Defaults to
  `true` when `websocket` is not a server client.
- `callback` {Function} An optional callback which is invoked when the ping
  frame is written out. If an error occurs, the callback is called with the
  error as its first argument.

Send a ping. This method throws an error if the ready state is `CONNECTING`.

### websocket.pong([data[, mask]][, callback])

- `data`
  {Array|Number|Object|String|ArrayBuffer|Buffer|DataView|TypedArray|Blob} The
  data to send in the pong frame.
- `mask` {Boolean} Specifies whether `data` should be masked or not. Defaults to
  `true` when `websocket` is not a server client.
- `callback` {Function} An optional callback which is invoked when the pong
  frame is written out. If an error occurs, the callback is called with the
  error as its first argument.

Send a pong. This method throws an error if the ready state is `CONNECTING`.

### websocket.protocol

- {String}

The subprotocol selected by the server.

### websocket.resume()

Make a paused socket resume emitting events. This method is a noop if the ready
state is `CONNECTING` or `CLOSED`.

### websocket.readyState

- {Number}

The current state of the connection. This is one of the ready state constants.

### websocket.removeEventListener(type, listener)

- `type` {String} A string representing the event type to remove.
- `listener` {Function|Object} The listener to remove.

Removes an event listener emulating the `EventTarget` interface. This method
only removes listeners added with
[`websocket.addEventListener()`](#websocketaddeventlistenertype-listener-options).

### websocket.send(data[, options][, callback])

- `data`
  {Array|Number|Object|String|ArrayBuffer|Buffer|DataView|TypedArray|Blob} The
  data to send. `Object` values are only supported if they conform to the
  requirements of [`Buffer.from()`][]. If those constraints are not met, a
  `TypeError` is thrown.
- `options` {Object}
  - `binary` {Boolean} Specifies whether `data` should be sent as a binary or
    not. Default is autodetected.
  - `compress` {Boolean} Specifies whether `data` should be compressed or not.
    Defaults to `true` when permessage-deflate is enabled.
  - `fin` {Boolean} Specifies whether `data` is the last fragment of a message
    or not. Defaults to `true`.
  - `mask` {Boolean} Specifies whether `data` should be masked or not. Defaults
    to `true` when `websocket` is not a server client.
- `callback` {Function} An optional callback which is invoked when `data` is
  written out. If an error occurs, the callback is called with the error as its
  first argument.

Send `data` through the connection. This method throws an error if the ready
state is `CONNECTING`.

### websocket.terminate()

Forcibly close the connection. Internally, this calls [`socket.destroy()`][].

### websocket.url

- {String}

The URL of the WebSocket server. Server clients don't have this attribute.

## createWebSocketStream(websocket[, options])

- `websocket` {WebSocket} A `WebSocket` object.
- `options` {Object} [Options][duplex-options] to pass to the `Duplex`
  constructor.

Returns a `Duplex` stream that allows to use the Node.js streams API on top of a
given `WebSocket`.

## Environment variables

### WS_NO_BUFFER_UTIL

When set to a non-empty value, prevents the optional `bufferutil` dependency
from being required.

### WS_NO_UTF_8_VALIDATE

When set to a non-empty value, prevents the optional `utf-8-validate` dependency
from being required.

## Error codes

Errors emitted by the websocket may have a `.code` property, describing the
specific type of error that has occurred:

### WS_ERR_EXPECTED_FIN

A WebSocket frame was received with the FIN bit not set when it was expected.

### WS_ERR_EXPECTED_MASK

An unmasked WebSocket frame was received by a WebSocket server.

### WS_ERR_INVALID_CLOSE_CODE

A WebSocket close frame was received with an invalid close code.

### WS_ERR_INVALID_CONTROL_PAYLOAD_LENGTH

A control frame with an invalid payload length was received.

### WS_ERR_INVALID_OPCODE

A WebSocket frame was received with an invalid opcode.

### WS_ERR_INVALID_UTF8

A text or close frame was received containing invalid UTF-8 data.

### WS_ERR_UNEXPECTED_MASK

A masked WebSocket frame was received by a WebSocket client.

### WS_ERR_UNEXPECTED_RSV_1

A WebSocket frame was received with the RSV1 bit set unexpectedly.

### WS_ERR_UNEXPECTED_RSV_2_3

A WebSocket frame was received with the RSV2 or RSV3 bit set unexpectedly.

### WS_ERR_UNSUPPORTED_DATA_PAYLOAD_LENGTH

A data frame was received with a length longer than the max supported length
(2^53 - 1, due to JavaScript language limitations).

### WS_ERR_UNSUPPORTED_MESSAGE_LENGTH

A message was received with a length longer than the maximum supported length,
as configured by the `maxPayload` option.

[concurrency-limit]: https://github.com/websockets/ws/issues/1202
[duplex-options]:
  https://nodejs.org/api/stream.html#stream_new_stream_duplex_options
[`buffer.from()`]:
  https://nodejs.org/api/buffer.html#static-method-bufferfromobject-offsetorencoding-length
[`http.request()`]:
  https://nodejs.org/api/http.html#http_http_request_options_callback
[`https.request()`]:
  https://nodejs.org/api/https.html#https_https_request_options_callback
[permessage-deflate]:
  https://tools.ietf.org/html/draft-ietf-hybi-permessage-compression-19
[`request.getheader()`]: https://nodejs.org/api/http.html#requestgetheadername
[`request.removeheader()`]:
  https://nodejs.org/api/http.html#requestremoveheadername
[`socket.destroy()`]: https://nodejs.org/api/net.html#net_socket_destroy_error
[`websocket.close()`]: #websocketclosecode-reason
[zlib-options]: https://nodejs.org/api/zlib.html#zlib_class_options
```

## File: `examples/ssl.js`
```javascript
'use strict';

const https = require('https');
const fs = require('fs');

const { WebSocket, WebSocketServer } = require('..');

const server = https.createServer({
  cert: fs.readFileSync('../test/fixtures/certificate.pem'),
  key: fs.readFileSync('../test/fixtures/key.pem')
});

const wss = new WebSocketServer({ server });

wss.on('connection', function connection(ws) {
  ws.on('error', console.error);

  ws.on('message', function message(msg) {
    console.log(msg.toString());
  });
});

server.listen(function listening() {
  //
  // If the `rejectUnauthorized` option is not `false`, the server certificate
  // is verified against a list of well-known CAs. An 'error' event is emitted
  // if verification fails.
  //
  // The certificate used in this example is self-signed so `rejectUnauthorized`
  // is set to `false`.
  //
  const ws = new WebSocket(`wss://localhost:${server.address().port}`, {
    rejectUnauthorized: false
  });

  ws.on('error', console.error);

  ws.on('open', function open() {
    ws.send('All glory to WebSockets!');
  });
});
```

## File: `examples/express-session-parse/index.js`
```javascript
'use strict';

const session = require('express-session');
const express = require('express');
const http = require('http');
const uuid = require('uuid');

const { WebSocketServer } = require('../..');

function onSocketError(err) {
  console.error(err);
}

const app = express();
const map = new Map();

//
// We need the same instance of the session parser in express and
// WebSocket server.
//
const sessionParser = session({
  saveUninitialized: false,
  secret: '$eCuRiTy',
  resave: false
});

//
// Serve static files from the 'public' folder.
//
app.use(express.static('public'));
app.use(sessionParser);

app.post('/login', function (req, res) {
  //
  // "Log in" user and set userId to session.
  //
  const id = uuid.v4();

  console.log(`Updating session for user ${id}`);
  req.session.userId = id;
  res.send({ result: 'OK', message: 'Session updated' });
});

app.delete('/logout', function (request, response) {
  const ws = map.get(request.session.userId);

  console.log('Destroying session');
  request.session.destroy(function () {
    if (ws) ws.close();

    response.send({ result: 'OK', message: 'Session destroyed' });
  });
});

//
// Create an HTTP server.
//
const server = http.createServer(app);

//
// Create a WebSocket server completely detached from the HTTP server.
//
const wss = new WebSocketServer({ clientTracking: false, noServer: true });

server.on('upgrade', function (request, socket, head) {
  socket.on('error', onSocketError);

  console.log('Parsing session from request...');

  sessionParser(request, {}, () => {
    if (!request.session.userId) {
      socket.write('HTTP/1.1 401 Unauthorized\r\n\r\n');
      socket.destroy();
      return;
    }

    console.log('Session is parsed!');

    socket.removeListener('error', onSocketError);

    wss.handleUpgrade(request, socket, head, function (ws) {
      wss.emit('connection', ws, request);
    });
  });
});

wss.on('connection', function (ws, request) {
  const userId = request.session.userId;

  map.set(userId, ws);

  ws.on('error', console.error);

  ws.on('message', function (message) {
    //
    // Here we can now use session parameters.
    //
    console.log(`Received message ${message} from user ${userId}`);
  });

  ws.on('close', function () {
    map.delete(userId);
  });
});

//
// Start the server.
//
server.listen(8080, function () {
  console.log('Listening on http://localhost:8080');
});
```

## File: `examples/express-session-parse/package.json`
```json
{
  "author": "",
  "name": "express-session-parse",
  "version": "0.0.0",
  "repository": "websockets/ws",
  "dependencies": {
    "express": "^4.16.4",
    "express-session": "^1.16.1",
    "uuid": "^8.3.2"
  }
}
```

## File: `examples/express-session-parse/public/app.js`
```javascript
(function () {
  const messages = document.querySelector('#messages');
  const wsButton = document.querySelector('#wsButton');
  const wsSendButton = document.querySelector('#wsSendButton');
  const logout = document.querySelector('#logout');
  const login = document.querySelector('#login');

  function showMessage(message) {
    messages.textContent += `\n${message}`;
    messages.scrollTop = messages.scrollHeight;
  }

  function handleResponse(response) {
    return response.ok
      ? response.json().then((data) => JSON.stringify(data, null, 2))
      : Promise.reject(new Error('Unexpected response'));
  }

  login.onclick = function () {
    fetch('/login', { method: 'POST', credentials: 'same-origin' })
      .then(handleResponse)
      .then(showMessage)
      .catch(function (err) {
        showMessage(err.message);
      });
  };

  logout.onclick = function () {
    fetch('/logout', { method: 'DELETE', credentials: 'same-origin' })
      .then(handleResponse)
      .then(showMessage)
      .catch(function (err) {
        showMessage(err.message);
      });
  };

  let ws;

  wsButton.onclick = function () {
    if (ws) {
      ws.onerror = ws.onopen = ws.onclose = null;
      ws.close();
    }

    ws = new WebSocket(`ws://${location.host}`);
    ws.onerror = function () {
      showMessage('WebSocket error');
    };
    ws.onopen = function () {
      showMessage('WebSocket connection established');
    };
    ws.onclose = function () {
      showMessage('WebSocket connection closed');
      ws = null;
    };
  };

  wsSendButton.onclick = function () {
    if (!ws) {
      showMessage('No WebSocket connection');
      return;
    }

    ws.send('Hello World!');
    showMessage('Sent "Hello World!"');
  };
})();
```

## File: `examples/express-session-parse/public/index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="utf-8">
      <title>Express session demo</title>
  </head>
  <body>
    <h1>Choose an action.</h1>
    <button id="login" type="button" title="Simulate login">
      Simulate login
    </button>
    <button id="logout" type="button" title="Simulate logout">
      Simulate logout
    </button>
    <button id="wsButton" type="button" title="Open WebSocket connection">
      Open WebSocket connection
    </button>
    <button id="wsSendButton" type="button" title="Send WebSocket message">
      Send WebSocket message
    </button>
    <pre id="messages" style="height: 400px; overflow: scroll"></pre>
    <script src="app.js"></script>
  </body>
</html>
```

## File: `examples/server-stats/index.js`
```javascript
'use strict';

const express = require('express');
const path = require('path');
const { createServer } = require('http');

const { WebSocketServer } = require('../..');

const app = express();
app.use(express.static(path.join(__dirname, '/public')));

const server = createServer(app);
const wss = new WebSocketServer({ server });

wss.on('connection', function (ws) {
  const id = setInterval(function () {
    ws.send(JSON.stringify(process.memoryUsage()), function () {
      //
      // Ignore errors.
      //
    });
  }, 100);
  console.log('started client interval');

  ws.on('error', console.error);

  ws.on('close', function () {
    console.log('stopping client interval');
    clearInterval(id);
  });
});

server.listen(8080, function () {
  console.log('Listening on http://localhost:8080');
});
```

## File: `examples/server-stats/package.json`
```json
{
  "author": "",
  "name": "serverstats",
  "version": "0.0.0",
  "repository": "websockets/ws",
  "dependencies": {
    "express": "^4.16.4"
  }
}
```

## File: `examples/server-stats/public/index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Server stats</title>
    <style>
      table, td {
        border: 1px solid #333;
      }

      thead {
        background-color: #333;
        color: #fff;
      }
    </style>
  </head>
  <body>
    <h1>Server stats</h1>
    <table>
      <thead>
        <tr>
          <th colspan="2">Memory usage</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>RSS</td>
          <td id="rss"></td>
        </tr>
        <tr>
          <td>Heap total</td>
          <td id="heapTotal"></td>
        </tr>
        <tr>
          <td>Heap used</td>
          <td id="heapUsed"></td>
        </tr>
        <tr>
          <td>External</td>
          <td id="external"></td>
        </tr>
      </tbody>
    </table>
    <script>
      (function() {
        const rss = document.getElementById('rss');
        const heapTotal = document.getElementById('heapTotal');
        const heapUsed = document.getElementById('heapUsed');
        const external = document.getElementById('external');
        const ws = new WebSocket(`ws://${location.host}`);

        ws.onmessage = function(event) {
          const data = JSON.parse(event.data);

          rss.textContent = data.rss;
          heapTotal.textContent = data.heapTotal;
          heapUsed.textContent = data.heapUsed;
          external.textContent = data.external;
        };
      })();
    </script>
  </body>
</html>
```

## File: `lib/buffer-util.js`
```javascript
'use strict';

const { EMPTY_BUFFER } = require('./constants');

const FastBuffer = Buffer[Symbol.species];

/**
 * Merges an array of buffers into a new buffer.
 *
 * @param {Buffer[]} list The array of buffers to concat
 * @param {Number} totalLength The total length of buffers in the list
 * @return {Buffer} The resulting buffer
 * @public
 */
function concat(list, totalLength) {
  if (list.length === 0) return EMPTY_BUFFER;
  if (list.length === 1) return list[0];

  const target = Buffer.allocUnsafe(totalLength);
  let offset = 0;

  for (let i = 0; i < list.length; i++) {
    const buf = list[i];
    target.set(buf, offset);
    offset += buf.length;
  }

  if (offset < totalLength) {
    return new FastBuffer(target.buffer, target.byteOffset, offset);
  }

  return target;
}

/**
 * Masks a buffer using the given mask.
 *
 * @param {Buffer} source The buffer to mask
 * @param {Buffer} mask The mask to use
 * @param {Buffer} output The buffer where to store the result
 * @param {Number} offset The offset at which to start writing
 * @param {Number} length The number of bytes to mask.
 * @public
 */
function _mask(source, mask, output, offset, length) {
  for (let i = 0; i < length; i++) {
    output[offset + i] = source[i] ^ mask[i & 3];
  }
}

/**
 * Unmasks a buffer using the given mask.
 *
 * @param {Buffer} buffer The buffer to unmask
 * @param {Buffer} mask The mask to use
 * @public
 */
function _unmask(buffer, mask) {
  for (let i = 0; i < buffer.length; i++) {
    buffer[i] ^= mask[i & 3];
  }
}

/**
 * Converts a buffer to an `ArrayBuffer`.
 *
 * @param {Buffer} buf The buffer to convert
 * @return {ArrayBuffer} Converted buffer
 * @public
 */
function toArrayBuffer(buf) {
  if (buf.length === buf.buffer.byteLength) {
    return buf.buffer;
  }

  return buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.length);
}

/**
 * Converts `data` to a `Buffer`.
 *
 * @param {*} data The data to convert
 * @return {Buffer} The buffer
 * @throws {TypeError}
 * @public
 */
function toBuffer(data) {
  toBuffer.readOnly = true;

  if (Buffer.isBuffer(data)) return data;

  let buf;

  if (data instanceof ArrayBuffer) {
    buf = new FastBuffer(data);
  } else if (ArrayBuffer.isView(data)) {
    buf = new FastBuffer(data.buffer, data.byteOffset, data.byteLength);
  } else {
    buf = Buffer.from(data);
    toBuffer.readOnly = false;
  }

  return buf;
}

module.exports = {
  concat,
  mask: _mask,
  toArrayBuffer,
  toBuffer,
  unmask: _unmask
};

/* istanbul ignore else  */
if (!process.env.WS_NO_BUFFER_UTIL) {
  try {
    const bufferUtil = require('bufferutil');

    module.exports.mask = function (source, mask, output, offset, length) {
      if (length < 48) _mask(source, mask, output, offset, length);
      else bufferUtil.mask(source, mask, output, offset, length);
    };

    module.exports.unmask = function (buffer, mask) {
      if (buffer.length < 32) _unmask(buffer, mask);
      else bufferUtil.unmask(buffer, mask);
    };
  } catch (e) {
    // Continue regardless of the error.
  }
}
```

## File: `lib/constants.js`
```javascript
'use strict';

const BINARY_TYPES = ['nodebuffer', 'arraybuffer', 'fragments'];
const hasBlob = typeof Blob !== 'undefined';

if (hasBlob) BINARY_TYPES.push('blob');

module.exports = {
  BINARY_TYPES,
  CLOSE_TIMEOUT: 30000,
  EMPTY_BUFFER: Buffer.alloc(0),
  GUID: '258EAFA5-E914-47DA-95CA-C5AB0DC85B11',
  hasBlob,
  kForOnEventAttribute: Symbol('kIsForOnEventAttribute'),
  kListener: Symbol('kListener'),
  kStatusCode: Symbol('status-code'),
  kWebSocket: Symbol('websocket'),
  NOOP: () => {}
};
```

## File: `lib/event-target.js`
```javascript
'use strict';

const { kForOnEventAttribute, kListener } = require('./constants');

const kCode = Symbol('kCode');
const kData = Symbol('kData');
const kError = Symbol('kError');
const kMessage = Symbol('kMessage');
const kReason = Symbol('kReason');
const kTarget = Symbol('kTarget');
const kType = Symbol('kType');
const kWasClean = Symbol('kWasClean');

/**
 * Class representing an event.
 */
class Event {
  /**
   * Create a new `Event`.
   *
   * @param {String} type The name of the event
   * @throws {TypeError} If the `type` argument is not specified
   */
  constructor(type) {
    this[kTarget] = null;
    this[kType] = type;
  }

  /**
   * @type {*}
   */
  get target() {
    return this[kTarget];
  }

  /**
   * @type {String}
   */
  get type() {
    return this[kType];
  }
}

Object.defineProperty(Event.prototype, 'target', { enumerable: true });
Object.defineProperty(Event.prototype, 'type', { enumerable: true });

/**
 * Class representing a close event.
 *
 * @extends Event
 */
class CloseEvent extends Event {
  /**
   * Create a new `CloseEvent`.
   *
   * @param {String} type The name of the event
   * @param {Object} [options] A dictionary object that allows for setting
   *     attributes via object members of the same name
   * @param {Number} [options.code=0] The status code explaining why the
   *     connection was closed
   * @param {String} [options.reason=''] A human-readable string explaining why
   *     the connection was closed
   * @param {Boolean} [options.wasClean=false] Indicates whether or not the
   *     connection was cleanly closed
   */
  constructor(type, options = {}) {
    super(type);

    this[kCode] = options.code === undefined ? 0 : options.code;
    this[kReason] = options.reason === undefined ? '' : options.reason;
    this[kWasClean] = options.wasClean === undefined ? false : options.wasClean;
  }

  /**
   * @type {Number}
   */
  get code() {
    return this[kCode];
  }

  /**
   * @type {String}
   */
  get reason() {
    return this[kReason];
  }

  /**
   * @type {Boolean}
   */
  get wasClean() {
    return this[kWasClean];
  }
}

Object.defineProperty(CloseEvent.prototype, 'code', { enumerable: true });
Object.defineProperty(CloseEvent.prototype, 'reason', { enumerable: true });
Object.defineProperty(CloseEvent.prototype, 'wasClean', { enumerable: true });

/**
 * Class representing an error event.
 *
 * @extends Event
 */
class ErrorEvent extends Event {
  /**
   * Create a new `ErrorEvent`.
   *
   * @param {String} type The name of the event
   * @param {Object} [options] A dictionary object that allows for setting
   *     attributes via object members of the same name
   * @param {*} [options.error=null] The error that generated this event
   * @param {String} [options.message=''] The error message
   */
  constructor(type, options = {}) {
    super(type);

    this[kError] = options.error === undefined ? null : options.error;
    this[kMessage] = options.message === undefined ? '' : options.message;
  }

  /**
   * @type {*}
   */
  get error() {
    return this[kError];
  }

  /**
   * @type {String}
   */
  get message() {
    return this[kMessage];
  }
}

Object.defineProperty(ErrorEvent.prototype, 'error', { enumerable: true });
Object.defineProperty(ErrorEvent.prototype, 'message', { enumerable: true });

/**
 * Class representing a message event.
 *
 * @extends Event
 */
class MessageEvent extends Event {
  /**
   * Create a new `MessageEvent`.
   *
   * @param {String} type The name of the event
   * @param {Object} [options] A dictionary object that allows for setting
   *     attributes via object members of the same name
   * @param {*} [options.data=null] The message content
   */
  constructor(type, options = {}) {
    super(type);

    this[kData] = options.data === undefined ? null : options.data;
  }

  /**
   * @type {*}
   */
  get data() {
    return this[kData];
  }
}

Object.defineProperty(MessageEvent.prototype, 'data', { enumerable: true });

/**
 * This provides methods for emulating the `EventTarget` interface. It's not
 * meant to be used directly.
 *
 * @mixin
 */
const EventTarget = {
  /**
   * Register an event listener.
   *
   * @param {String} type A string representing the event type to listen for
   * @param {(Function|Object)} handler The listener to add
   * @param {Object} [options] An options object specifies characteristics about
   *     the event listener
   * @param {Boolean} [options.once=false] A `Boolean` indicating that the
   *     listener should be invoked at most once after being added. If `true`,
   *     the listener would be automatically removed when invoked.
   * @public
   */
  addEventListener(type, handler, options = {}) {
    for (const listener of this.listeners(type)) {
      if (
        !options[kForOnEventAttribute] &&
        listener[kListener] === handler &&
        !listener[kForOnEventAttribute]
      ) {
        return;
      }
    }

    let wrapper;

    if (type === 'message') {
      wrapper = function onMessage(data, isBinary) {
        const event = new MessageEvent('message', {
          data: isBinary ? data : data.toString()
        });

        event[kTarget] = this;
        callListener(handler, this, event);
      };
    } else if (type === 'close') {
      wrapper = function onClose(code, message) {
        const event = new CloseEvent('close', {
          code,
          reason: message.toString(),
          wasClean: this._closeFrameReceived && this._closeFrameSent
        });

        event[kTarget] = this;
        callListener(handler, this, event);
      };
    } else if (type === 'error') {
      wrapper = function onError(error) {
        const event = new ErrorEvent('error', {
          error,
          message: error.message
        });

        event[kTarget] = this;
        callListener(handler, this, event);
      };
    } else if (type === 'open') {
      wrapper = function onOpen() {
        const event = new Event('open');

        event[kTarget] = this;
        callListener(handler, this, event);
      };
    } else {
      return;
    }

    wrapper[kForOnEventAttribute] = !!options[kForOnEventAttribute];
    wrapper[kListener] = handler;

    if (options.once) {
      this.once(type, wrapper);
    } else {
      this.on(type, wrapper);
    }
  },

  /**
   * Remove an event listener.
   *
   * @param {String} type A string representing the event type to remove
   * @param {(Function|Object)} handler The listener to remove
   * @public
   */
  removeEventListener(type, handler) {
    for (const listener of this.listeners(type)) {
      if (listener[kListener] === handler && !listener[kForOnEventAttribute]) {
        this.removeListener(type, listener);
        break;
      }
    }
  }
};

module.exports = {
  CloseEvent,
  ErrorEvent,
  Event,
  EventTarget,
  MessageEvent
};

/**
 * Call an event listener
 *
 * @param {(Function|Object)} listener The listener to call
 * @param {*} thisArg The value to use as `this`` when calling the listener
 * @param {Event} event The event to pass to the listener
 * @private
 */
function callListener(listener, thisArg, event) {
  if (typeof listener === 'object' && listener.handleEvent) {
    listener.handleEvent.call(listener, event);
  } else {
    listener.call(thisArg, event);
  }
}
```

## File: `lib/extension.js`
```javascript
'use strict';

const { tokenChars } = require('./validation');

/**
 * Adds an offer to the map of extension offers or a parameter to the map of
 * parameters.
 *
 * @param {Object} dest The map of extension offers or parameters
 * @param {String} name The extension or parameter name
 * @param {(Object|Boolean|String)} elem The extension parameters or the
 *     parameter value
 * @private
 */
function push(dest, name, elem) {
  if (dest[name] === undefined) dest[name] = [elem];
  else dest[name].push(elem);
}

/**
 * Parses the `Sec-WebSocket-Extensions` header into an object.
 *
 * @param {String} header The field value of the header
 * @return {Object} The parsed object
 * @public
 */
function parse(header) {
  const offers = Object.create(null);
  let params = Object.create(null);
  let mustUnescape = false;
  let isEscaping = false;
  let inQuotes = false;
  let extensionName;
  let paramName;
  let start = -1;
  let code = -1;
  let end = -1;
  let i = 0;

  for (; i < header.length; i++) {
    code = header.charCodeAt(i);

    if (extensionName === undefined) {
      if (end === -1 && tokenChars[code] === 1) {
        if (start === -1) start = i;
      } else if (
        i !== 0 &&
        (code === 0x20 /* ' ' */ || code === 0x09) /* '\t' */
      ) {
        if (end === -1 && start !== -1) end = i;
      } else if (code === 0x3b /* ';' */ || code === 0x2c /* ',' */) {
        if (start === -1) {
          throw new SyntaxError(`Unexpected character at index ${i}`);
        }

        if (end === -1) end = i;
        const name = header.slice(start, end);
        if (code === 0x2c) {
          push(offers, name, params);
          params = Object.create(null);
        } else {
          extensionName = name;
        }

        start = end = -1;
      } else {
        throw new SyntaxError(`Unexpected character at index ${i}`);
      }
    } else if (paramName === undefined) {
      if (end === -1 && tokenChars[code] === 1) {
        if (start === -1) start = i;
      } else if (code === 0x20 || code === 0x09) {
        if (end === -1 && start !== -1) end = i;
      } else if (code === 0x3b || code === 0x2c) {
        if (start === -1) {
          throw new SyntaxError(`Unexpected character at index ${i}`);
        }

        if (end === -1) end = i;
        push(params, header.slice(start, end), true);
        if (code === 0x2c) {
          push(offers, extensionName, params);
          params = Object.create(null);
          extensionName = undefined;
        }

        start = end = -1;
      } else if (code === 0x3d /* '=' */ && start !== -1 && end === -1) {
        paramName = header.slice(start, i);
        start = end = -1;
      } else {
        throw new SyntaxError(`Unexpected character at index ${i}`);
      }
    } else {
      //
      // The value of a quoted-string after unescaping must conform to the
      // token ABNF, so only token characters are valid.
      // Ref: https://tools.ietf.org/html/rfc6455#section-9.1
      //
      if (isEscaping) {
        if (tokenChars[code] !== 1) {
          throw new SyntaxError(`Unexpected character at index ${i}`);
        }
        if (start === -1) start = i;
        else if (!mustUnescape) mustUnescape = true;
        isEscaping = false;
      } else if (inQuotes) {
        if (tokenChars[code] === 1) {
          if (start === -1) start = i;
        } else if (code === 0x22 /* '"' */ && start !== -1) {
          inQuotes = false;
          end = i;
        } else if (code === 0x5c /* '\' */) {
          isEscaping = true;
        } else {
          throw new SyntaxError(`Unexpected character at index ${i}`);
        }
      } else if (code === 0x22 && header.charCodeAt(i - 1) === 0x3d) {
        inQuotes = true;
      } else if (end === -1 && tokenChars[code] === 1) {
        if (start === -1) start = i;
      } else if (start !== -1 && (code === 0x20 || code === 0x09)) {
        if (end === -1) end = i;
      } else if (code === 0x3b || code === 0x2c) {
        if (start === -1) {
          throw new SyntaxError(`Unexpected character at index ${i}`);
        }

        if (end === -1) end = i;
        let value = header.slice(start, end);
        if (mustUnescape) {
          value = value.replace(/\\/g, '');
          mustUnescape = false;
        }
        push(params, paramName, value);
        if (code === 0x2c) {
          push(offers, extensionName, params);
          params = Object.create(null);
          extensionName = undefined;
        }

        paramName = undefined;
        start = end = -1;
      } else {
        throw new SyntaxError(`Unexpected character at index ${i}`);
      }
    }
  }

  if (start === -1 || inQuotes || code === 0x20 || code === 0x09) {
    throw new SyntaxError('Unexpected end of input');
  }

  if (end === -1) end = i;
  const token = header.slice(start, end);
  if (extensionName === undefined) {
    push(offers, token, params);
  } else {
    if (paramName === undefined) {
      push(params, token, true);
    } else if (mustUnescape) {
      push(params, paramName, token.replace(/\\/g, ''));
    } else {
      push(params, paramName, token);
    }
    push(offers, extensionName, params);
  }

  return offers;
}

/**
 * Builds the `Sec-WebSocket-Extensions` header field value.
 *
 * @param {Object} extensions The map of extensions and parameters to format
 * @return {String} A string representing the given object
 * @public
 */
function format(extensions) {
  return Object.keys(extensions)
    .map((extension) => {
      let configurations = extensions[extension];
      if (!Array.isArray(configurations)) configurations = [configurations];
      return configurations
        .map((params) => {
          return [extension]
            .concat(
              Object.keys(params).map((k) => {
                let values = params[k];
                if (!Array.isArray(values)) values = [values];
                return values
                  .map((v) => (v === true ? k : `${k}=${v}`))
                  .join('; ');
              })
            )
            .join('; ');
        })
        .join(', ');
    })
    .join(', ');
}

module.exports = { format, parse };
```

## File: `lib/limiter.js`
```javascript
'use strict';

const kDone = Symbol('kDone');
const kRun = Symbol('kRun');

/**
 * A very simple job queue with adjustable concurrency. Adapted from
 * https://github.com/STRML/async-limiter
 */
class Limiter {
  /**
   * Creates a new `Limiter`.
   *
   * @param {Number} [concurrency=Infinity] The maximum number of jobs allowed
   *     to run concurrently
   */
  constructor(concurrency) {
    this[kDone] = () => {
      this.pending--;
      this[kRun]();
    };
    this.concurrency = concurrency || Infinity;
    this.jobs = [];
    this.pending = 0;
  }

  /**
   * Adds a job to the queue.
   *
   * @param {Function} job The job to run
   * @public
   */
  add(job) {
    this.jobs.push(job);
    this[kRun]();
  }

  /**
   * Removes a job from the queue and runs it if possible.
   *
   * @private
   */
  [kRun]() {
    if (this.pending === this.concurrency) return;

    if (this.jobs.length) {
      const job = this.jobs.shift();

      this.pending++;
      job(this[kDone]);
    }
  }
}

module.exports = Limiter;
```

## File: `lib/permessage-deflate.js`
```javascript
'use strict';

const zlib = require('zlib');

const bufferUtil = require('./buffer-util');
const Limiter = require('./limiter');
const { kStatusCode } = require('./constants');

const FastBuffer = Buffer[Symbol.species];
const TRAILER = Buffer.from([0x00, 0x00, 0xff, 0xff]);
const kPerMessageDeflate = Symbol('permessage-deflate');
const kTotalLength = Symbol('total-length');
const kCallback = Symbol('callback');
const kBuffers = Symbol('buffers');
const kError = Symbol('error');

//
// We limit zlib concurrency, which prevents severe memory fragmentation
// as documented in https://github.com/nodejs/node/issues/8871#issuecomment-250915913
// and https://github.com/websockets/ws/issues/1202
//
// Intentionally global; it's the global thread pool that's an issue.
//
let zlibLimiter;

/**
 * permessage-deflate implementation.
 */
class PerMessageDeflate {
  /**
   * Creates a PerMessageDeflate instance.
   *
   * @param {Object} [options] Configuration options
   * @param {(Boolean|Number)} [options.clientMaxWindowBits] Advertise support
   *     for, or request, a custom client window size
   * @param {Boolean} [options.clientNoContextTakeover=false] Advertise/
   *     acknowledge disabling of client context takeover
   * @param {Number} [options.concurrencyLimit=10] The number of concurrent
   *     calls to zlib
   * @param {Boolean} [options.isServer=false] Create the instance in either
   *     server or client mode
   * @param {Number} [options.maxPayload=0] The maximum allowed message length
   * @param {(Boolean|Number)} [options.serverMaxWindowBits] Request/confirm the
   *     use of a custom server window size
   * @param {Boolean} [options.serverNoContextTakeover=false] Request/accept
   *     disabling of server context takeover
   * @param {Number} [options.threshold=1024] Size (in bytes) below which
   *     messages should not be compressed if context takeover is disabled
   * @param {Object} [options.zlibDeflateOptions] Options to pass to zlib on
   *     deflate
   * @param {Object} [options.zlibInflateOptions] Options to pass to zlib on
   *     inflate
   */
  constructor(options) {
    this._options = options || {};
    this._threshold =
      this._options.threshold !== undefined ? this._options.threshold : 1024;
    this._maxPayload = this._options.maxPayload | 0;
    this._isServer = !!this._options.isServer;
    this._deflate = null;
    this._inflate = null;

    this.params = null;

    if (!zlibLimiter) {
      const concurrency =
        this._options.concurrencyLimit !== undefined
          ? this._options.concurrencyLimit
          : 10;
      zlibLimiter = new Limiter(concurrency);
    }
  }

  /**
   * @type {String}
   */
  static get extensionName() {
    return 'permessage-deflate';
  }

  /**
   * Create an extension negotiation offer.
   *
   * @return {Object} Extension parameters
   * @public
   */
  offer() {
    const params = {};

    if (this._options.serverNoContextTakeover) {
      params.server_no_context_takeover = true;
    }
    if (this._options.clientNoContextTakeover) {
      params.client_no_context_takeover = true;
    }
    if (this._options.serverMaxWindowBits) {
      params.server_max_window_bits = this._options.serverMaxWindowBits;
    }
    if (this._options.clientMaxWindowBits) {
      params.client_max_window_bits = this._options.clientMaxWindowBits;
    } else if (this._options.clientMaxWindowBits == null) {
      params.client_max_window_bits = true;
    }

    return params;
  }

  /**
   * Accept an extension negotiation offer/response.
   *
   * @param {Array} configurations The extension negotiation offers/reponse
   * @return {Object} Accepted configuration
   * @public
   */
  accept(configurations) {
    configurations = this.normalizeParams(configurations);

    this.params = this._isServer
      ? this.acceptAsServer(configurations)
      : this.acceptAsClient(configurations);

    return this.params;
  }

  /**
   * Releases all resources used by the extension.
   *
   * @public
   */
  cleanup() {
    if (this._inflate) {
      this._inflate.close();
      this._inflate = null;
    }

    if (this._deflate) {
      const callback = this._deflate[kCallback];

      this._deflate.close();
      this._deflate = null;

      if (callback) {
        callback(
          new Error(
            'The deflate stream was closed while data was being processed'
          )
        );
      }
    }
  }

  /**
   *  Accept an extension negotiation offer.
   *
   * @param {Array} offers The extension negotiation offers
   * @return {Object} Accepted configuration
   * @private
   */
  acceptAsServer(offers) {
    const opts = this._options;
    const accepted = offers.find((params) => {
      if (
        (opts.serverNoContextTakeover === false &&
          params.server_no_context_takeover) ||
        (params.server_max_window_bits &&
          (opts.serverMaxWindowBits === false ||
            (typeof opts.serverMaxWindowBits === 'number' &&
              opts.serverMaxWindowBits > params.server_max_window_bits))) ||
        (typeof opts.clientMaxWindowBits === 'number' &&
          !params.client_max_window_bits)
      ) {
        return false;
      }

      return true;
    });

    if (!accepted) {
      throw new Error('None of the extension offers can be accepted');
    }

    if (opts.serverNoContextTakeover) {
      accepted.server_no_context_takeover = true;
    }
    if (opts.clientNoContextTakeover) {
      accepted.client_no_context_takeover = true;
    }
    if (typeof opts.serverMaxWindowBits === 'number') {
      accepted.server_max_window_bits = opts.serverMaxWindowBits;
    }
    if (typeof opts.clientMaxWindowBits === 'number') {
      accepted.client_max_window_bits = opts.clientMaxWindowBits;
    } else if (
      accepted.client_max_window_bits === true ||
      opts.clientMaxWindowBits === false
    ) {
      delete accepted.client_max_window_bits;
    }

    return accepted;
  }

  /**
   * Accept the extension negotiation response.
   *
   * @param {Array} response The extension negotiation response
   * @return {Object} Accepted configuration
   * @private
   */
  acceptAsClient(response) {
    const params = response[0];

    if (
      this._options.clientNoContextTakeover === false &&
      params.client_no_context_takeover
    ) {
      throw new Error('Unexpected parameter "client_no_context_takeover"');
    }

    if (!params.client_max_window_bits) {
      if (typeof this._options.clientMaxWindowBits === 'number') {
        params.client_max_window_bits = this._options.clientMaxWindowBits;
      }
    } else if (
      this._options.clientMaxWindowBits === false ||
      (typeof this._options.clientMaxWindowBits === 'number' &&
        params.client_max_window_bits > this._options.clientMaxWindowBits)
    ) {
      throw new Error(
        'Unexpected or invalid parameter "client_max_window_bits"'
      );
    }

    return params;
  }

  /**
   * Normalize parameters.
   *
   * @param {Array} configurations The extension negotiation offers/reponse
   * @return {Array} The offers/response with normalized parameters
   * @private
   */
  normalizeParams(configurations) {
    configurations.forEach((params) => {
      Object.keys(params).forEach((key) => {
        let value = params[key];

        if (value.length > 1) {
          throw new Error(`Parameter "${key}" must have only a single value`);
        }

        value = value[0];

        if (key === 'client_max_window_bits') {
          if (value !== true) {
            const num = +value;
            if (!Number.isInteger(num) || num < 8 || num > 15) {
              throw new TypeError(
                `Invalid value for parameter "${key}": ${value}`
              );
            }
            value = num;
          } else if (!this._isServer) {
            throw new TypeError(
              `Invalid value for parameter "${key}": ${value}`
            );
          }
        } else if (key === 'server_max_window_bits') {
          const num = +value;
          if (!Number.isInteger(num) || num < 8 || num > 15) {
            throw new TypeError(
              `Invalid value for parameter "${key}": ${value}`
            );
          }
          value = num;
        } else if (
          key === 'client_no_context_takeover' ||
          key === 'server_no_context_takeover'
        ) {
          if (value !== true) {
            throw new TypeError(
              `Invalid value for parameter "${key}": ${value}`
            );
          }
        } else {
          throw new Error(`Unknown parameter "${key}"`);
        }

        params[key] = value;
      });
    });

    return configurations;
  }

  /**
   * Decompress data. Concurrency limited.
   *
   * @param {Buffer} data Compressed data
   * @param {Boolean} fin Specifies whether or not this is the last fragment
   * @param {Function} callback Callback
   * @public
   */
  decompress(data, fin, callback) {
    zlibLimiter.add((done) => {
      this._decompress(data, fin, (err, result) => {
        done();
        callback(err, result);
      });
    });
  }

  /**
   * Compress data. Concurrency limited.
   *
   * @param {(Buffer|String)} data Data to compress
   * @param {Boolean} fin Specifies whether or not this is the last fragment
   * @param {Function} callback Callback
   * @public
   */
  compress(data, fin, callback) {
    zlibLimiter.add((done) => {
      this._compress(data, fin, (err, result) => {
        done();
        callback(err, result);
      });
    });
  }

  /**
   * Decompress data.
   *
   * @param {Buffer} data Compressed data
   * @param {Boolean} fin Specifies whether or not this is the last fragment
   * @param {Function} callback Callback
   * @private
   */
  _decompress(data, fin, callback) {
    const endpoint = this._isServer ? 'client' : 'server';

    if (!this._inflate) {
      const key = `${endpoint}_max_window_bits`;
      const windowBits =
        typeof this.params[key] !== 'number'
          ? zlib.Z_DEFAULT_WINDOWBITS
          : this.params[key];

      this._inflate = zlib.createInflateRaw({
        ...this._options.zlibInflateOptions,
        windowBits
      });
      this._inflate[kPerMessageDeflate] = this;
      this._inflate[kTotalLength] = 0;
      this._inflate[kBuffers] = [];
      this._inflate.on('error', inflateOnError);
      this._inflate.on('data', inflateOnData);
    }

    this._inflate[kCallback] = callback;

    this._inflate.write(data);
    if (fin) this._inflate.write(TRAILER);

    this._inflate.flush(() => {
      const err = this._inflate[kError];

      if (err) {
        this._inflate.close();
        this._inflate = null;
        callback(err);
        return;
      }

      const data = bufferUtil.concat(
        this._inflate[kBuffers],
        this._inflate[kTotalLength]
      );

      if (this._inflate._readableState.endEmitted) {
        this._inflate.close();
        this._inflate = null;
      } else {
        this._inflate[kTotalLength] = 0;
        this._inflate[kBuffers] = [];

        if (fin && this.params[`${endpoint}_no_context_takeover`]) {
          this._inflate.reset();
        }
      }

      callback(null, data);
    });
  }

  /**
   * Compress data.
   *
   * @param {(Buffer|String)} data Data to compress
   * @param {Boolean} fin Specifies whether or not this is the last fragment
   * @param {Function} callback Callback
   * @private
   */
  _compress(data, fin, callback) {
    const endpoint = this._isServer ? 'server' : 'client';

    if (!this._deflate) {
      const key = `${endpoint}_max_window_bits`;
      const windowBits =
        typeof this.params[key] !== 'number'
          ? zlib.Z_DEFAULT_WINDOWBITS
          : this.params[key];

      this._deflate = zlib.createDeflateRaw({
        ...this._options.zlibDeflateOptions,
        windowBits
      });

      this._deflate[kTotalLength] = 0;
      this._deflate[kBuffers] = [];

      this._deflate.on('data', deflateOnData);
    }

    this._deflate[kCallback] = callback;

    this._deflate.write(data);
    this._deflate.flush(zlib.Z_SYNC_FLUSH, () => {
      if (!this._deflate) {
        //
        // The deflate stream was closed while data was being processed.
        //
        return;
      }

      let data = bufferUtil.concat(
        this._deflate[kBuffers],
        this._deflate[kTotalLength]
      );

      if (fin) {
        data = new FastBuffer(data.buffer, data.byteOffset, data.length - 4);
      }

      //
      // Ensure that the callback will not be called again in
      // `PerMessageDeflate#cleanup()`.
      //
      this._deflate[kCallback] = null;

      this._deflate[kTotalLength] = 0;
      this._deflate[kBuffers] = [];

      if (fin && this.params[`${endpoint}_no_context_takeover`]) {
        this._deflate.reset();
      }

      callback(null, data);
    });
  }
}

module.exports = PerMessageDeflate;

/**
 * The listener of the `zlib.DeflateRaw` stream `'data'` event.
 *
 * @param {Buffer} chunk A chunk of data
 * @private
 */
function deflateOnData(chunk) {
  this[kBuffers].push(chunk);
  this[kTotalLength] += chunk.length;
}

/**
 * The listener of the `zlib.InflateRaw` stream `'data'` event.
 *
 * @param {Buffer} chunk A chunk of data
 * @private
 */
function inflateOnData(chunk) {
  this[kTotalLength] += chunk.length;

  if (
    this[kPerMessageDeflate]._maxPayload < 1 ||
    this[kTotalLength] <= this[kPerMessageDeflate]._maxPayload
  ) {
    this[kBuffers].push(chunk);
    return;
  }

  this[kError] = new RangeError('Max payload size exceeded');
  this[kError].code = 'WS_ERR_UNSUPPORTED_MESSAGE_LENGTH';
  this[kError][kStatusCode] = 1009;
  this.removeListener('data', inflateOnData);

  //
  // The choice to employ `zlib.reset()` over `zlib.close()` is dictated by the
  // fact that in Node.js versions prior to 13.10.0, the callback for
  // `zlib.flush()` is not called if `zlib.close()` is used. Utilizing
  // `zlib.reset()` ensures that either the callback is invoked or an error is
  // emitted.
  //
  this.reset();
}

/**
 * The listener of the `zlib.InflateRaw` stream `'error'` event.
 *
 * @param {Error} err The emitted error
 * @private
 */
function inflateOnError(err) {
  //
  // There is no need to call `Zlib#close()` as the handle is automatically
  // closed when an error is emitted.
  //
  this[kPerMessageDeflate]._inflate = null;

  if (this[kError]) {
    this[kCallback](this[kError]);
    return;
  }

  err[kStatusCode] = 1007;
  this[kCallback](err);
}
```

## File: `lib/receiver.js`
```javascript
'use strict';

const { Writable } = require('stream');

const PerMessageDeflate = require('./permessage-deflate');
const {
  BINARY_TYPES,
  EMPTY_BUFFER,
  kStatusCode,
  kWebSocket
} = require('./constants');
const { concat, toArrayBuffer, unmask } = require('./buffer-util');
const { isValidStatusCode, isValidUTF8 } = require('./validation');

const FastBuffer = Buffer[Symbol.species];

const GET_INFO = 0;
const GET_PAYLOAD_LENGTH_16 = 1;
const GET_PAYLOAD_LENGTH_64 = 2;
const GET_MASK = 3;
const GET_DATA = 4;
const INFLATING = 5;
const DEFER_EVENT = 6;

/**
 * HyBi Receiver implementation.
 *
 * @extends Writable
 */
class Receiver extends Writable {
  /**
   * Creates a Receiver instance.
   *
   * @param {Object} [options] Options object
   * @param {Boolean} [options.allowSynchronousEvents=true] Specifies whether
   *     any of the `'message'`, `'ping'`, and `'pong'` events can be emitted
   *     multiple times in the same tick
   * @param {String} [options.binaryType=nodebuffer] The type for binary data
   * @param {Object} [options.extensions] An object containing the negotiated
   *     extensions
   * @param {Boolean} [options.isServer=false] Specifies whether to operate in
   *     client or server mode
   * @param {Number} [options.maxPayload=0] The maximum allowed message length
   * @param {Boolean} [options.skipUTF8Validation=false] Specifies whether or
   *     not to skip UTF-8 validation for text and close messages
   */
  constructor(options = {}) {
    super();

    this._allowSynchronousEvents =
      options.allowSynchronousEvents !== undefined
        ? options.allowSynchronousEvents
        : true;
    this._binaryType = options.binaryType || BINARY_TYPES[0];
    this._extensions = options.extensions || {};
    this._isServer = !!options.isServer;
    this._maxPayload = options.maxPayload | 0;
    this._skipUTF8Validation = !!options.skipUTF8Validation;
    this[kWebSocket] = undefined;

    this._bufferedBytes = 0;
    this._buffers = [];

    this._compressed = false;
    this._payloadLength = 0;
    this._mask = undefined;
    this._fragmented = 0;
    this._masked = false;
    this._fin = false;
    this._opcode = 0;

    this._totalPayloadLength = 0;
    this._messageLength = 0;
    this._fragments = [];

    this._errored = false;
    this._loop = false;
    this._state = GET_INFO;
  }

  /**
   * Implements `Writable.prototype._write()`.
   *
   * @param {Buffer} chunk The chunk of data to write
   * @param {String} encoding The character encoding of `chunk`
   * @param {Function} cb Callback
   * @private
   */
  _write(chunk, encoding, cb) {
    if (this._opcode === 0x08 && this._state == GET_INFO) return cb();

    this._bufferedBytes += chunk.length;
    this._buffers.push(chunk);
    this.startLoop(cb);
  }

  /**
   * Consumes `n` bytes from the buffered data.
   *
   * @param {Number} n The number of bytes to consume
   * @return {Buffer} The consumed bytes
   * @private
   */
  consume(n) {
    this._bufferedBytes -= n;

    if (n === this._buffers[0].length) return this._buffers.shift();

    if (n < this._buffers[0].length) {
      const buf = this._buffers[0];
      this._buffers[0] = new FastBuffer(
        buf.buffer,
        buf.byteOffset + n,
        buf.length - n
      );

      return new FastBuffer(buf.buffer, buf.byteOffset, n);
    }

    const dst = Buffer.allocUnsafe(n);

    do {
      const buf = this._buffers[0];
      const offset = dst.length - n;

      if (n >= buf.length) {
        dst.set(this._buffers.shift(), offset);
      } else {
        dst.set(new Uint8Array(buf.buffer, buf.byteOffset, n), offset);
        this._buffers[0] = new FastBuffer(
          buf.buffer,
          buf.byteOffset + n,
          buf.length - n
        );
      }

      n -= buf.length;
    } while (n > 0);

    return dst;
  }

  /**
   * Starts the parsing loop.
   *
   * @param {Function} cb Callback
   * @private
   */
  startLoop(cb) {
    this._loop = true;

    do {
      switch (this._state) {
        case GET_INFO:
          this.getInfo(cb);
          break;
        case GET_PAYLOAD_LENGTH_16:
          this.getPayloadLength16(cb);
          break;
        case GET_PAYLOAD_LENGTH_64:
          this.getPayloadLength64(cb);
          break;
        case GET_MASK:
          this.getMask();
          break;
        case GET_DATA:
          this.getData(cb);
          break;
        case INFLATING:
        case DEFER_EVENT:
          this._loop = false;
          return;
      }
    } while (this._loop);

    if (!this._errored) cb();
  }

  /**
   * Reads the first two bytes of a frame.
   *
   * @param {Function} cb Callback
   * @private
   */
  getInfo(cb) {
    if (this._bufferedBytes < 2) {
      this._loop = false;
      return;
    }

    const buf = this.consume(2);

    if ((buf[0] & 0x30) !== 0x00) {
      const error = this.createError(
        RangeError,
        'RSV2 and RSV3 must be clear',
        true,
        1002,
        'WS_ERR_UNEXPECTED_RSV_2_3'
      );

      cb(error);
      return;
    }

    const compressed = (buf[0] & 0x40) === 0x40;

    if (compressed && !this._extensions[PerMessageDeflate.extensionName]) {
      const error = this.createError(
        RangeError,
        'RSV1 must be clear',
        true,
        1002,
        'WS_ERR_UNEXPECTED_RSV_1'
      );

      cb(error);
      return;
    }

    this._fin = (buf[0] & 0x80) === 0x80;
    this._opcode = buf[0] & 0x0f;
    this._payloadLength = buf[1] & 0x7f;

    if (this._opcode === 0x00) {
      if (compressed) {
        const error = this.createError(
          RangeError,
          'RSV1 must be clear',
          true,
          1002,
          'WS_ERR_UNEXPECTED_RSV_1'
        );

        cb(error);
        return;
      }

      if (!this._fragmented) {
        const error = this.createError(
          RangeError,
          'invalid opcode 0',
          true,
          1002,
          'WS_ERR_INVALID_OPCODE'
        );

        cb(error);
        return;
      }

      this._opcode = this._fragmented;
    } else if (this._opcode === 0x01 || this._opcode === 0x02) {
      if (this._fragmented) {
        const error = this.createError(
          RangeError,
          `invalid opcode ${this._opcode}`,
          true,
          1002,
          'WS_ERR_INVALID_OPCODE'
        );

        cb(error);
        return;
      }

      this._compressed = compressed;
    } else if (this._opcode > 0x07 && this._opcode < 0x0b) {
      if (!this._fin) {
        const error = this.createError(
          RangeError,
          'FIN must be set',
          true,
          1002,
          'WS_ERR_EXPECTED_FIN'
        );

        cb(error);
        return;
      }

      if (compressed) {
        const error = this.createError(
          RangeError,
          'RSV1 must be clear',
          true,
          1002,
          'WS_ERR_UNEXPECTED_RSV_1'
        );

        cb(error);
        return;
      }

      if (
        this._payloadLength > 0x7d ||
        (this._opcode === 0x08 && this._payloadLength === 1)
      ) {
        const error = this.createError(
          RangeError,
          `invalid payload length ${this._payloadLength}`,
          true,
          1002,
          'WS_ERR_INVALID_CONTROL_PAYLOAD_LENGTH'
        );

        cb(error);
        return;
      }
    } else {
      const error = this.createError(
        RangeError,
        `invalid opcode ${this._opcode}`,
        true,
        1002,
        'WS_ERR_INVALID_OPCODE'
      );

      cb(error);
      return;
    }

    if (!this._fin && !this._fragmented) this._fragmented = this._opcode;
    this._masked = (buf[1] & 0x80) === 0x80;

    if (this._isServer) {
      if (!this._masked) {
        const error = this.createError(
          RangeError,
          'MASK must be set',
          true,
          1002,
          'WS_ERR_EXPECTED_MASK'
        );

        cb(error);
        return;
      }
    } else if (this._masked) {
      const error = this.createError(
        RangeError,
        'MASK must be clear',
        true,
        1002,
        'WS_ERR_UNEXPECTED_MASK'
      );

      cb(error);
      return;
    }

    if (this._payloadLength === 126) this._state = GET_PAYLOAD_LENGTH_16;
    else if (this._payloadLength === 127) this._state = GET_PAYLOAD_LENGTH_64;
    else this.haveLength(cb);
  }

  /**
   * Gets extended payload length (7+16).
   *
   * @param {Function} cb Callback
   * @private
   */
  getPayloadLength16(cb) {
    if (this._bufferedBytes < 2) {
      this._loop = false;
      return;
    }

    this._payloadLength = this.consume(2).readUInt16BE(0);
    this.haveLength(cb);
  }

  /**
   * Gets extended payload length (7+64).
   *
   * @param {Function} cb Callback
   * @private
   */
  getPayloadLength64(cb) {
    if (this._bufferedBytes < 8) {
      this._loop = false;
      return;
    }

    const buf = this.consume(8);
    const num = buf.readUInt32BE(0);

    //
    // The maximum safe integer in JavaScript is 2^53 - 1. An error is returned
    // if payload length is greater than this number.
    //
    if (num > Math.pow(2, 53 - 32) - 1) {
      const error = this.createError(
        RangeError,
        'Unsupported WebSocket frame: payload length > 2^53 - 1',
        false,
        1009,
        'WS_ERR_UNSUPPORTED_DATA_PAYLOAD_LENGTH'
      );

      cb(error);
      return;
    }

    this._payloadLength = num * Math.pow(2, 32) + buf.readUInt32BE(4);
    this.haveLength(cb);
  }

  /**
   * Payload length has been read.
   *
   * @param {Function} cb Callback
   * @private
   */
  haveLength(cb) {
    if (this._payloadLength && this._opcode < 0x08) {
      this._totalPayloadLength += this._payloadLength;
      if (this._totalPayloadLength > this._maxPayload && this._maxPayload > 0) {
        const error = this.createError(
          RangeError,
          'Max payload size exceeded',
          false,
          1009,
          'WS_ERR_UNSUPPORTED_MESSAGE_LENGTH'
        );

        cb(error);
        return;
      }
    }

    if (this._masked) this._state = GET_MASK;
    else this._state = GET_DATA;
  }

  /**
   * Reads mask bytes.
   *
   * @private
   */
  getMask() {
    if (this._bufferedBytes < 4) {
      this._loop = false;
      return;
    }

    this._mask = this.consume(4);
    this._state = GET_DATA;
  }

  /**
   * Reads data bytes.
   *
   * @param {Function} cb Callback
   * @private
   */
  getData(cb) {
    let data = EMPTY_BUFFER;

    if (this._payloadLength) {
      if (this._bufferedBytes < this._payloadLength) {
        this._loop = false;
        return;
      }

      data = this.consume(this._payloadLength);

      if (
        this._masked &&
        (this._mask[0] | this._mask[1] | this._mask[2] | this._mask[3]) !== 0
      ) {
        unmask(data, this._mask);
      }
    }

    if (this._opcode > 0x07) {
      this.controlMessage(data, cb);
      return;
    }

    if (this._compressed) {
      this._state = INFLATING;
      this.decompress(data, cb);
      return;
    }

    if (data.length) {
      //
      // This message is not compressed so its length is the sum of the payload
      // length of all fragments.
      //
      this._messageLength = this._totalPayloadLength;
      this._fragments.push(data);
    }

    this.dataMessage(cb);
  }

  /**
   * Decompresses data.
   *
   * @param {Buffer} data Compressed data
   * @param {Function} cb Callback
   * @private
   */
  decompress(data, cb) {
    const perMessageDeflate = this._extensions[PerMessageDeflate.extensionName];

    perMessageDeflate.decompress(data, this._fin, (err, buf) => {
      if (err) return cb(err);

      if (buf.length) {
        this._messageLength += buf.length;
        if (this._messageLength > this._maxPayload && this._maxPayload > 0) {
          const error = this.createError(
            RangeError,
            'Max payload size exceeded',
            false,
            1009,
            'WS_ERR_UNSUPPORTED_MESSAGE_LENGTH'
          );

          cb(error);
          return;
        }

        this._fragments.push(buf);
      }

      this.dataMessage(cb);
      if (this._state === GET_INFO) this.startLoop(cb);
    });
  }

  /**
   * Handles a data message.
   *
   * @param {Function} cb Callback
   * @private
   */
  dataMessage(cb) {
    if (!this._fin) {
      this._state = GET_INFO;
      return;
    }

    const messageLength = this._messageLength;
    const fragments = this._fragments;

    this._totalPayloadLength = 0;
    this._messageLength = 0;
    this._fragmented = 0;
    this._fragments = [];

    if (this._opcode === 2) {
      let data;

      if (this._binaryType === 'nodebuffer') {
        data = concat(fragments, messageLength);
      } else if (this._binaryType === 'arraybuffer') {
        data = toArrayBuffer(concat(fragments, messageLength));
      } else if (this._binaryType === 'blob') {
        data = new Blob(fragments);
      } else {
        data = fragments;
      }

      if (this._allowSynchronousEvents) {
        this.emit('message', data, true);
        this._state = GET_INFO;
      } else {
        this._state = DEFER_EVENT;
        setImmediate(() => {
          this.emit('message', data, true);
          this._state = GET_INFO;
          this.startLoop(cb);
        });
      }
    } else {
      const buf = concat(fragments, messageLength);

      if (!this._skipUTF8Validation && !isValidUTF8(buf)) {
        const error = this.createError(
          Error,
          'invalid UTF-8 sequence',
          true,
          1007,
          'WS_ERR_INVALID_UTF8'
        );

        cb(error);
        return;
      }

      if (this._state === INFLATING || this._allowSynchronousEvents) {
        this.emit('message', buf, false);
        this._state = GET_INFO;
      } else {
        this._state = DEFER_EVENT;
        setImmediate(() => {
          this.emit('message', buf, false);
          this._state = GET_INFO;
          this.startLoop(cb);
        });
      }
    }
  }

  /**
   * Handles a control message.
   *
   * @param {Buffer} data Data to handle
   * @return {(Error|RangeError|undefined)} A possible error
   * @private
   */
  controlMessage(data, cb) {
    if (this._opcode === 0x08) {
      if (data.length === 0) {
        this._loop = false;
        this.emit('conclude', 1005, EMPTY_BUFFER);
        this.end();
      } else {
        const code = data.readUInt16BE(0);

        if (!isValidStatusCode(code)) {
          const error = this.createError(
            RangeError,
            `invalid status code ${code}`,
            true,
            1002,
            'WS_ERR_INVALID_CLOSE_CODE'
          );

          cb(error);
          return;
        }

        const buf = new FastBuffer(
          data.buffer,
          data.byteOffset + 2,
          data.length - 2
        );

        if (!this._skipUTF8Validation && !isValidUTF8(buf)) {
          const error = this.createError(
            Error,
            'invalid UTF-8 sequence',
            true,
            1007,
            'WS_ERR_INVALID_UTF8'
          );

          cb(error);
          return;
        }

        this._loop = false;
        this.emit('conclude', code, buf);
        this.end();
      }

      this._state = GET_INFO;
      return;
    }

    if (this._allowSynchronousEvents) {
      this.emit(this._opcode === 0x09 ? 'ping' : 'pong', data);
      this._state = GET_INFO;
    } else {
      this._state = DEFER_EVENT;
      setImmediate(() => {
        this.emit(this._opcode === 0x09 ? 'ping' : 'pong', data);
        this._state = GET_INFO;
        this.startLoop(cb);
      });
    }
  }

  /**
   * Builds an error object.
   *
   * @param {function(new:Error|RangeError)} ErrorCtor The error constructor
   * @param {String} message The error message
   * @param {Boolean} prefix Specifies whether or not to add a default prefix to
   *     `message`
   * @param {Number} statusCode The status code
   * @param {String} errorCode The exposed error code
   * @return {(Error|RangeError)} The error
   * @private
   */
  createError(ErrorCtor, message, prefix, statusCode, errorCode) {
    this._loop = false;
    this._errored = true;

    const err = new ErrorCtor(
      prefix ? `Invalid WebSocket frame: ${message}` : message
    );

    Error.captureStackTrace(err, this.createError);
    err.code = errorCode;
    err[kStatusCode] = statusCode;
    return err;
  }
}

module.exports = Receiver;
```

## File: `lib/sender.js`
```javascript
/* eslint no-unused-vars: ["error", { "varsIgnorePattern": "^Duplex" }] */

'use strict';

const { Duplex } = require('stream');
const { randomFillSync } = require('crypto');

const PerMessageDeflate = require('./permessage-deflate');
const { EMPTY_BUFFER, kWebSocket, NOOP } = require('./constants');
const { isBlob, isValidStatusCode } = require('./validation');
const { mask: applyMask, toBuffer } = require('./buffer-util');

const kByteLength = Symbol('kByteLength');
const maskBuffer = Buffer.alloc(4);
const RANDOM_POOL_SIZE = 8 * 1024;
let randomPool;
let randomPoolPointer = RANDOM_POOL_SIZE;

const DEFAULT = 0;
const DEFLATING = 1;
const GET_BLOB_DATA = 2;

/**
 * HyBi Sender implementation.
 */
class Sender {
  /**
   * Creates a Sender instance.
   *
   * @param {Duplex} socket The connection socket
   * @param {Object} [extensions] An object containing the negotiated extensions
   * @param {Function} [generateMask] The function used to generate the masking
   *     key
   */
  constructor(socket, extensions, generateMask) {
    this._extensions = extensions || {};

    if (generateMask) {
      this._generateMask = generateMask;
      this._maskBuffer = Buffer.alloc(4);
    }

    this._socket = socket;

    this._firstFragment = true;
    this._compress = false;

    this._bufferedBytes = 0;
    this._queue = [];
    this._state = DEFAULT;
    this.onerror = NOOP;
    this[kWebSocket] = undefined;
  }

  /**
   * Frames a piece of data according to the HyBi WebSocket protocol.
   *
   * @param {(Buffer|String)} data The data to frame
   * @param {Object} options Options object
   * @param {Boolean} [options.fin=false] Specifies whether or not to set the
   *     FIN bit
   * @param {Function} [options.generateMask] The function used to generate the
   *     masking key
   * @param {Boolean} [options.mask=false] Specifies whether or not to mask
   *     `data`
   * @param {Buffer} [options.maskBuffer] The buffer used to store the masking
   *     key
   * @param {Number} options.opcode The opcode
   * @param {Boolean} [options.readOnly=false] Specifies whether `data` can be
   *     modified
   * @param {Boolean} [options.rsv1=false] Specifies whether or not to set the
   *     RSV1 bit
   * @return {(Buffer|String)[]} The framed data
   * @public
   */
  static frame(data, options) {
    let mask;
    let merge = false;
    let offset = 2;
    let skipMasking = false;

    if (options.mask) {
      mask = options.maskBuffer || maskBuffer;

      if (options.generateMask) {
        options.generateMask(mask);
      } else {
        if (randomPoolPointer === RANDOM_POOL_SIZE) {
          /* istanbul ignore else  */
          if (randomPool === undefined) {
            //
            // This is lazily initialized because server-sent frames must not
            // be masked so it may never be used.
            //
            randomPool = Buffer.alloc(RANDOM_POOL_SIZE);
          }

          randomFillSync(randomPool, 0, RANDOM_POOL_SIZE);
          randomPoolPointer = 0;
        }

        mask[0] = randomPool[randomPoolPointer++];
        mask[1] = randomPool[randomPoolPointer++];
        mask[2] = randomPool[randomPoolPointer++];
        mask[3] = randomPool[randomPoolPointer++];
      }

      skipMasking = (mask[0] | mask[1] | mask[2] | mask[3]) === 0;
      offset = 6;
    }

    let dataLength;

    if (typeof data === 'string') {
      if (
        (!options.mask || skipMasking) &&
        options[kByteLength] !== undefined
      ) {
        dataLength = options[kByteLength];
      } else {
        data = Buffer.from(data);
        dataLength = data.length;
      }
    } else {
      dataLength = data.length;
      merge = options.mask && options.readOnly && !skipMasking;
    }

    let payloadLength = dataLength;

    if (dataLength >= 65536) {
      offset += 8;
      payloadLength = 127;
    } else if (dataLength > 125) {
      offset += 2;
      payloadLength = 126;
    }

    const target = Buffer.allocUnsafe(merge ? dataLength + offset : offset);

    target[0] = options.fin ? options.opcode | 0x80 : options.opcode;
    if (options.rsv1) target[0] |= 0x40;

    target[1] = payloadLength;

    if (payloadLength === 126) {
      target.writeUInt16BE(dataLength, 2);
    } else if (payloadLength === 127) {
      target[2] = target[3] = 0;
      target.writeUIntBE(dataLength, 4, 6);
    }

    if (!options.mask) return [target, data];

    target[1] |= 0x80;
    target[offset - 4] = mask[0];
    target[offset - 3] = mask[1];
    target[offset - 2] = mask[2];
    target[offset - 1] = mask[3];

    if (skipMasking) return [target, data];

    if (merge) {
      applyMask(data, mask, target, offset, dataLength);
      return [target];
    }

    applyMask(data, mask, data, 0, dataLength);
    return [target, data];
  }

  /**
   * Sends a close message to the other peer.
   *
   * @param {Number} [code] The status code component of the body
   * @param {(String|Buffer)} [data] The message component of the body
   * @param {Boolean} [mask=false] Specifies whether or not to mask the message
   * @param {Function} [cb] Callback
   * @public
   */
  close(code, data, mask, cb) {
    let buf;

    if (code === undefined) {
      buf = EMPTY_BUFFER;
    } else if (typeof code !== 'number' || !isValidStatusCode(code)) {
      throw new TypeError('First argument must be a valid error code number');
    } else if (data === undefined || !data.length) {
      buf = Buffer.allocUnsafe(2);
      buf.writeUInt16BE(code, 0);
    } else {
      const length = Buffer.byteLength(data);

      if (length > 123) {
        throw new RangeError('The message must not be greater than 123 bytes');
      }

      buf = Buffer.allocUnsafe(2 + length);
      buf.writeUInt16BE(code, 0);

      if (typeof data === 'string') {
        buf.write(data, 2);
      } else {
        buf.set(data, 2);
      }
    }

    const options = {
      [kByteLength]: buf.length,
      fin: true,
      generateMask: this._generateMask,
      mask,
      maskBuffer: this._maskBuffer,
      opcode: 0x08,
      readOnly: false,
      rsv1: false
    };

    if (this._state !== DEFAULT) {
      this.enqueue([this.dispatch, buf, false, options, cb]);
    } else {
      this.sendFrame(Sender.frame(buf, options), cb);
    }
  }

  /**
   * Sends a ping message to the other peer.
   *
   * @param {*} data The message to send
   * @param {Boolean} [mask=false] Specifies whether or not to mask `data`
   * @param {Function} [cb] Callback
   * @public
   */
  ping(data, mask, cb) {
    let byteLength;
    let readOnly;

    if (typeof data === 'string') {
      byteLength = Buffer.byteLength(data);
      readOnly = false;
    } else if (isBlob(data)) {
      byteLength = data.size;
      readOnly = false;
    } else {
      data = toBuffer(data);
      byteLength = data.length;
      readOnly = toBuffer.readOnly;
    }

    if (byteLength > 125) {
      throw new RangeError('The data size must not be greater than 125 bytes');
    }

    const options = {
      [kByteLength]: byteLength,
      fin: true,
      generateMask: this._generateMask,
      mask,
      maskBuffer: this._maskBuffer,
      opcode: 0x09,
      readOnly,
      rsv1: false
    };

    if (isBlob(data)) {
      if (this._state !== DEFAULT) {
        this.enqueue([this.getBlobData, data, false, options, cb]);
      } else {
        this.getBlobData(data, false, options, cb);
      }
    } else if (this._state !== DEFAULT) {
      this.enqueue([this.dispatch, data, false, options, cb]);
    } else {
      this.sendFrame(Sender.frame(data, options), cb);
    }
  }

  /**
   * Sends a pong message to the other peer.
   *
   * @param {*} data The message to send
   * @param {Boolean} [mask=false] Specifies whether or not to mask `data`
   * @param {Function} [cb] Callback
   * @public
   */
  pong(data, mask, cb) {
    let byteLength;
    let readOnly;

    if (typeof data === 'string') {
      byteLength = Buffer.byteLength(data);
      readOnly = false;
    } else if (isBlob(data)) {
      byteLength = data.size;
      readOnly = false;
    } else {
      data = toBuffer(data);
      byteLength = data.length;
      readOnly = toBuffer.readOnly;
    }

    if (byteLength > 125) {
      throw new RangeError('The data size must not be greater than 125 bytes');
    }

    const options = {
      [kByteLength]: byteLength,
      fin: true,
      generateMask: this._generateMask,
      mask,
      maskBuffer: this._maskBuffer,
      opcode: 0x0a,
      readOnly,
      rsv1: false
    };

    if (isBlob(data)) {
      if (this._state !== DEFAULT) {
        this.enqueue([this.getBlobData, data, false, options, cb]);
      } else {
        this.getBlobData(data, false, options, cb);
      }
    } else if (this._state !== DEFAULT) {
      this.enqueue([this.dispatch, data, false, options, cb]);
    } else {
      this.sendFrame(Sender.frame(data, options), cb);
    }
  }

  /**
   * Sends a data message to the other peer.
   *
   * @param {*} data The message to send
   * @param {Object} options Options object
   * @param {Boolean} [options.binary=false] Specifies whether `data` is binary
   *     or text
   * @param {Boolean} [options.compress=false] Specifies whether or not to
   *     compress `data`
   * @param {Boolean} [options.fin=false] Specifies whether the fragment is the
   *     last one
   * @param {Boolean} [options.mask=false] Specifies whether or not to mask
   *     `data`
   * @param {Function} [cb] Callback
   * @public
   */
  send(data, options, cb) {
    const perMessageDeflate = this._extensions[PerMessageDeflate.extensionName];
    let opcode = options.binary ? 2 : 1;
    let rsv1 = options.compress;

    let byteLength;
    let readOnly;

    if (typeof data === 'string') {
      byteLength = Buffer.byteLength(data);
      readOnly = false;
    } else if (isBlob(data)) {
      byteLength = data.size;
      readOnly = false;
    } else {
      data = toBuffer(data);
      byteLength = data.length;
      readOnly = toBuffer.readOnly;
    }

    if (this._firstFragment) {
      this._firstFragment = false;
      if (
        rsv1 &&
        perMessageDeflate &&
        perMessageDeflate.params[
          perMessageDeflate._isServer
            ? 'server_no_context_takeover'
            : 'client_no_context_takeover'
        ]
      ) {
        rsv1 = byteLength >= perMessageDeflate._threshold;
      }
      this._compress = rsv1;
    } else {
      rsv1 = false;
      opcode = 0;
    }

    if (options.fin) this._firstFragment = true;

    const opts = {
      [kByteLength]: byteLength,
      fin: options.fin,
      generateMask: this._generateMask,
      mask: options.mask,
      maskBuffer: this._maskBuffer,
      opcode,
      readOnly,
      rsv1
    };

    if (isBlob(data)) {
      if (this._state !== DEFAULT) {
        this.enqueue([this.getBlobData, data, this._compress, opts, cb]);
      } else {
        this.getBlobData(data, this._compress, opts, cb);
      }
    } else if (this._state !== DEFAULT) {
      this.enqueue([this.dispatch, data, this._compress, opts, cb]);
    } else {
      this.dispatch(data, this._compress, opts, cb);
    }
  }

  /**
   * Gets the contents of a blob as binary data.
   *
   * @param {Blob} blob The blob
   * @param {Boolean} [compress=false] Specifies whether or not to compress
   *     the data
   * @param {Object} options Options object
   * @param {Boolean} [options.fin=false] Specifies whether or not to set the
   *     FIN bit
   * @param {Function} [options.generateMask] The function used to generate the
   *     masking key
   * @param {Boolean} [options.mask=false] Specifies whether or not to mask
   *     `data`
   * @param {Buffer} [options.maskBuffer] The buffer used to store the masking
   *     key
   * @param {Number} options.opcode The opcode
   * @param {Boolean} [options.readOnly=false] Specifies whether `data` can be
   *     modified
   * @param {Boolean} [options.rsv1=false] Specifies whether or not to set the
   *     RSV1 bit
   * @param {Function} [cb] Callback
   * @private
   */
  getBlobData(blob, compress, options, cb) {
    this._bufferedBytes += options[kByteLength];
    this._state = GET_BLOB_DATA;

    blob
      .arrayBuffer()
      .then((arrayBuffer) => {
        if (this._socket.destroyed) {
          const err = new Error(
            'The socket was closed while the blob was being read'
          );

          //
          // `callCallbacks` is called in the next tick to ensure that errors
          // that might be thrown in the callbacks behave like errors thrown
          // outside the promise chain.
          //
          process.nextTick(callCallbacks, this, err, cb);
          return;
        }

        this._bufferedBytes -= options[kByteLength];
        const data = toBuffer(arrayBuffer);

        if (!compress) {
          this._state = DEFAULT;
          this.sendFrame(Sender.frame(data, options), cb);
          this.dequeue();
        } else {
          this.dispatch(data, compress, options, cb);
        }
      })
      .catch((err) => {
        //
        // `onError` is called in the next tick for the same reason that
        // `callCallbacks` above is.
        //
        process.nextTick(onError, this, err, cb);
      });
  }

  /**
   * Dispatches a message.
   *
   * @param {(Buffer|String)} data The message to send
   * @param {Boolean} [compress=false] Specifies whether or not to compress
   *     `data`
   * @param {Object} options Options object
   * @param {Boolean} [options.fin=false] Specifies whether or not to set the
   *     FIN bit
   * @param {Function} [options.generateMask] The function used to generate the
   *     masking key
   * @param {Boolean} [options.mask=false] Specifies whether or not to mask
   *     `data`
   * @param {Buffer} [options.maskBuffer] The buffer used to store the masking
   *     key
   * @param {Number} options.opcode The opcode
   * @param {Boolean} [options.readOnly=false] Specifies whether `data` can be
   *     modified
   * @param {Boolean} [options.rsv1=false] Specifies whether or not to set the
   *     RSV1 bit
   * @param {Function} [cb] Callback
   * @private
   */
  dispatch(data, compress, options, cb) {
    if (!compress) {
      this.sendFrame(Sender.frame(data, options), cb);
      return;
    }

    const perMessageDeflate = this._extensions[PerMessageDeflate.extensionName];

    this._bufferedBytes += options[kByteLength];
    this._state = DEFLATING;
    perMessageDeflate.compress(data, options.fin, (_, buf) => {
      if (this._socket.destroyed) {
        const err = new Error(
          'The socket was closed while data was being compressed'
        );

        callCallbacks(this, err, cb);
        return;
      }

      this._bufferedBytes -= options[kByteLength];
      this._state = DEFAULT;
      options.readOnly = false;
      this.sendFrame(Sender.frame(buf, options), cb);
      this.dequeue();
    });
  }

  /**
   * Executes queued send operations.
   *
   * @private
   */
  dequeue() {
    while (this._state === DEFAULT && this._queue.length) {
      const params = this._queue.shift();

      this._bufferedBytes -= params[3][kByteLength];
      Reflect.apply(params[0], this, params.slice(1));
    }
  }

  /**
   * Enqueues a send operation.
   *
   * @param {Array} params Send operation parameters.
   * @private
   */
  enqueue(params) {
    this._bufferedBytes += params[3][kByteLength];
    this._queue.push(params);
  }

  /**
   * Sends a frame.
   *
   * @param {(Buffer | String)[]} list The frame to send
   * @param {Function} [cb] Callback
   * @private
   */
  sendFrame(list, cb) {
    if (list.length === 2) {
      this._socket.cork();
      this._socket.write(list[0]);
      this._socket.write(list[1], cb);
      this._socket.uncork();
    } else {
      this._socket.write(list[0], cb);
    }
  }
}

module.exports = Sender;

/**
 * Calls queued callbacks with an error.
 *
 * @param {Sender} sender The `Sender` instance
 * @param {Error} err The error to call the callbacks with
 * @param {Function} [cb] The first callback
 * @private
 */
function callCallbacks(sender, err, cb) {
  if (typeof cb === 'function') cb(err);

  for (let i = 0; i < sender._queue.length; i++) {
    const params = sender._queue[i];
    const callback = params[params.length - 1];

    if (typeof callback === 'function') callback(err);
  }
}

/**
 * Handles a `Sender` error.
 *
 * @param {Sender} sender The `Sender` instance
 * @param {Error} err The error
 * @param {Function} [cb] The first pending callback
 * @private
 */
function onError(sender, err, cb) {
  callCallbacks(sender, err, cb);
  sender.onerror(err);
}
```

## File: `lib/stream.js`
```javascript
/* eslint no-unused-vars: ["error", { "varsIgnorePattern": "^WebSocket$" }] */
'use strict';

const WebSocket = require('./websocket');
const { Duplex } = require('stream');

/**
 * Emits the `'close'` event on a stream.
 *
 * @param {Duplex} stream The stream.
 * @private
 */
function emitClose(stream) {
  stream.emit('close');
}

/**
 * The listener of the `'end'` event.
 *
 * @private
 */
function duplexOnEnd() {
  if (!this.destroyed && this._writableState.finished) {
    this.destroy();
  }
}

/**
 * The listener of the `'error'` event.
 *
 * @param {Error} err The error
 * @private
 */
function duplexOnError(err) {
  this.removeListener('error', duplexOnError);
  this.destroy();
  if (this.listenerCount('error') === 0) {
    // Do not suppress the throwing behavior.
    this.emit('error', err);
  }
}

/**
 * Wraps a `WebSocket` in a duplex stream.
 *
 * @param {WebSocket} ws The `WebSocket` to wrap
 * @param {Object} [options] The options for the `Duplex` constructor
 * @return {Duplex} The duplex stream
 * @public
 */
function createWebSocketStream(ws, options) {
  let terminateOnDestroy = true;

  const duplex = new Duplex({
    ...options,
    autoDestroy: false,
    emitClose: false,
    objectMode: false,
    writableObjectMode: false
  });

  ws.on('message', function message(msg, isBinary) {
    const data =
      !isBinary && duplex._readableState.objectMode ? msg.toString() : msg;

    if (!duplex.push(data)) ws.pause();
  });

  ws.once('error', function error(err) {
    if (duplex.destroyed) return;

    // Prevent `ws.terminate()` from being called by `duplex._destroy()`.
    //
    // - If the `'error'` event is emitted before the `'open'` event, then
    //   `ws.terminate()` is a noop as no socket is assigned.
    // - Otherwise, the error is re-emitted by the listener of the `'error'`
    //   event of the `Receiver` object. The listener already closes the
    //   connection by calling `ws.close()`. This allows a close frame to be
    //   sent to the other peer. If `ws.terminate()` is called right after this,
    //   then the close frame might not be sent.
    terminateOnDestroy = false;
    duplex.destroy(err);
  });

  ws.once('close', function close() {
    if (duplex.destroyed) return;

    duplex.push(null);
  });

  duplex._destroy = function (err, callback) {
    if (ws.readyState === ws.CLOSED) {
      callback(err);
      process.nextTick(emitClose, duplex);
      return;
    }

    let called = false;

    ws.once('error', function error(err) {
      called = true;
      callback(err);
    });

    ws.once('close', function close() {
      if (!called) callback(err);
      process.nextTick(emitClose, duplex);
    });

    if (terminateOnDestroy) ws.terminate();
  };

  duplex._final = function (callback) {
    if (ws.readyState === ws.CONNECTING) {
      ws.once('open', function open() {
        duplex._final(callback);
      });
      return;
    }

    // If the value of the `_socket` property is `null` it means that `ws` is a
    // client websocket and the handshake failed. In fact, when this happens, a
    // socket is never assigned to the websocket. Wait for the `'error'` event
    // that will be emitted by the websocket.
    if (ws._socket === null) return;

    if (ws._socket._writableState.finished) {
      callback();
      if (duplex._readableState.endEmitted) duplex.destroy();
    } else {
      ws._socket.once('finish', function finish() {
        // `duplex` is not destroyed here because the `'end'` event will be
        // emitted on `duplex` after this `'finish'` event. The EOF signaling
        // `null` chunk is, in fact, pushed when the websocket emits `'close'`.
        callback();
      });
      ws.close();
    }
  };

  duplex._read = function () {
    if (ws.isPaused) ws.resume();
  };

  duplex._write = function (chunk, encoding, callback) {
    if (ws.readyState === ws.CONNECTING) {
      ws.once('open', function open() {
        duplex._write(chunk, encoding, callback);
      });
      return;
    }

    ws.send(chunk, callback);
  };

  duplex.on('end', duplexOnEnd);
  duplex.on('error', duplexOnError);
  return duplex;
}

module.exports = createWebSocketStream;
```

## File: `lib/subprotocol.js`
```javascript
'use strict';

const { tokenChars } = require('./validation');

/**
 * Parses the `Sec-WebSocket-Protocol` header into a set of subprotocol names.
 *
 * @param {String} header The field value of the header
 * @return {Set} The subprotocol names
 * @public
 */
function parse(header) {
  const protocols = new Set();
  let start = -1;
  let end = -1;
  let i = 0;

  for (i; i < header.length; i++) {
    const code = header.charCodeAt(i);

    if (end === -1 && tokenChars[code] === 1) {
      if (start === -1) start = i;
    } else if (
      i !== 0 &&
      (code === 0x20 /* ' ' */ || code === 0x09) /* '\t' */
    ) {
      if (end === -1 && start !== -1) end = i;
    } else if (code === 0x2c /* ',' */) {
      if (start === -1) {
        throw new SyntaxError(`Unexpected character at index ${i}`);
      }

      if (end === -1) end = i;

      const protocol = header.slice(start, end);

      if (protocols.has(protocol)) {
        throw new SyntaxError(`The "${protocol}" subprotocol is duplicated`);
      }

      protocols.add(protocol);
      start = end = -1;
    } else {
      throw new SyntaxError(`Unexpected character at index ${i}`);
    }
  }

  if (start === -1 || end !== -1) {
    throw new SyntaxError('Unexpected end of input');
  }

  const protocol = header.slice(start, i);

  if (protocols.has(protocol)) {
    throw new SyntaxError(`The "${protocol}" subprotocol is duplicated`);
  }

  protocols.add(protocol);
  return protocols;
}

module.exports = { parse };
```

## File: `lib/validation.js`
```javascript
'use strict';

const { isUtf8 } = require('buffer');

const { hasBlob } = require('./constants');

//
// Allowed token characters:
//
// '!', '#', '$', '%', '&', ''', '*', '+', '-',
// '.', 0-9, A-Z, '^', '_', '`', a-z, '|', '~'
//
// tokenChars[32] === 0 // ' '
// tokenChars[33] === 1 // '!'
// tokenChars[34] === 0 // '"'
// ...
//
// prettier-ignore
const tokenChars = [
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, // 0 - 15
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, // 16 - 31
  0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, // 32 - 47
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, // 48 - 63
  0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, // 64 - 79
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, // 80 - 95
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, // 96 - 111
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0 // 112 - 127
];

/**
 * Checks if a status code is allowed in a close frame.
 *
 * @param {Number} code The status code
 * @return {Boolean} `true` if the status code is valid, else `false`
 * @public
 */
function isValidStatusCode(code) {
  return (
    (code >= 1000 &&
      code <= 1014 &&
      code !== 1004 &&
      code !== 1005 &&
      code !== 1006) ||
    (code >= 3000 && code <= 4999)
  );
}

/**
 * Checks if a given buffer contains only correct UTF-8.
 * Ported from https://www.cl.cam.ac.uk/%7Emgk25/ucs/utf8_check.c by
 * Markus Kuhn.
 *
 * @param {Buffer} buf The buffer to check
 * @return {Boolean} `true` if `buf` contains only correct UTF-8, else `false`
 * @public
 */
function _isValidUTF8(buf) {
  const len = buf.length;
  let i = 0;

  while (i < len) {
    if ((buf[i] & 0x80) === 0) {
      // 0xxxxxxx
      i++;
    } else if ((buf[i] & 0xe0) === 0xc0) {
      // 110xxxxx 10xxxxxx
      if (
        i + 1 === len ||
        (buf[i + 1] & 0xc0) !== 0x80 ||
        (buf[i] & 0xfe) === 0xc0 // Overlong
      ) {
        return false;
      }

      i += 2;
    } else if ((buf[i] & 0xf0) === 0xe0) {
      // 1110xxxx 10xxxxxx 10xxxxxx
      if (
        i + 2 >= len ||
        (buf[i + 1] & 0xc0) !== 0x80 ||
        (buf[i + 2] & 0xc0) !== 0x80 ||
        (buf[i] === 0xe0 && (buf[i + 1] & 0xe0) === 0x80) || // Overlong
        (buf[i] === 0xed && (buf[i + 1] & 0xe0) === 0xa0) // Surrogate (U+D800 - U+DFFF)
      ) {
        return false;
      }

      i += 3;
    } else if ((buf[i] & 0xf8) === 0xf0) {
      // 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
      if (
        i + 3 >= len ||
        (buf[i + 1] & 0xc0) !== 0x80 ||
        (buf[i + 2] & 0xc0) !== 0x80 ||
        (buf[i + 3] & 0xc0) !== 0x80 ||
        (buf[i] === 0xf0 && (buf[i + 1] & 0xf0) === 0x80) || // Overlong
        (buf[i] === 0xf4 && buf[i + 1] > 0x8f) ||
        buf[i] > 0xf4 // > U+10FFFF
      ) {
        return false;
      }

      i += 4;
    } else {
      return false;
    }
  }

  return true;
}

/**
 * Determines whether a value is a `Blob`.
 *
 * @param {*} value The value to be tested
 * @return {Boolean} `true` if `value` is a `Blob`, else `false`
 * @private
 */
function isBlob(value) {
  return (
    hasBlob &&
    typeof value === 'object' &&
    typeof value.arrayBuffer === 'function' &&
    typeof value.type === 'string' &&
    typeof value.stream === 'function' &&
    (value[Symbol.toStringTag] === 'Blob' ||
      value[Symbol.toStringTag] === 'File')
  );
}

module.exports = {
  isBlob,
  isValidStatusCode,
  isValidUTF8: _isValidUTF8,
  tokenChars
};

if (isUtf8) {
  module.exports.isValidUTF8 = function (buf) {
    return buf.length < 24 ? _isValidUTF8(buf) : isUtf8(buf);
  };
} /* istanbul ignore else  */ else if (!process.env.WS_NO_UTF_8_VALIDATE) {
  try {
    const isValidUTF8 = require('utf-8-validate');

    module.exports.isValidUTF8 = function (buf) {
      return buf.length < 32 ? _isValidUTF8(buf) : isValidUTF8(buf);
    };
  } catch (e) {
    // Continue regardless of the error.
  }
}
```

## File: `lib/websocket-server.js`
```javascript
/* eslint no-unused-vars: ["error", { "varsIgnorePattern": "^Duplex$", "caughtErrors": "none" }] */

'use strict';

const EventEmitter = require('events');
const http = require('http');
const { Duplex } = require('stream');
const { createHash } = require('crypto');

const extension = require('./extension');
const PerMessageDeflate = require('./permessage-deflate');
const subprotocol = require('./subprotocol');
const WebSocket = require('./websocket');
const { CLOSE_TIMEOUT, GUID, kWebSocket } = require('./constants');

const keyRegex = /^[+/0-9A-Za-z]{22}==$/;

const RUNNING = 0;
const CLOSING = 1;
const CLOSED = 2;

/**
 * Class representing a WebSocket server.
 *
 * @extends EventEmitter
 */
class WebSocketServer extends EventEmitter {
  /**
   * Create a `WebSocketServer` instance.
   *
   * @param {Object} options Configuration options
   * @param {Boolean} [options.allowSynchronousEvents=true] Specifies whether
   *     any of the `'message'`, `'ping'`, and `'pong'` events can be emitted
   *     multiple times in the same tick
   * @param {Boolean} [options.autoPong=true] Specifies whether or not to
   *     automatically send a pong in response to a ping
   * @param {Number} [options.backlog=511] The maximum length of the queue of
   *     pending connections
   * @param {Boolean} [options.clientTracking=true] Specifies whether or not to
   *     track clients
   * @param {Number} [options.closeTimeout=30000] Duration in milliseconds to
   *     wait for the closing handshake to finish after `websocket.close()` is
   *     called
   * @param {Function} [options.handleProtocols] A hook to handle protocols
   * @param {String} [options.host] The hostname where to bind the server
   * @param {Number} [options.maxPayload=104857600] The maximum allowed message
   *     size
   * @param {Boolean} [options.noServer=false] Enable no server mode
   * @param {String} [options.path] Accept only connections matching this path
   * @param {(Boolean|Object)} [options.perMessageDeflate=false] Enable/disable
   *     permessage-deflate
   * @param {Number} [options.port] The port where to bind the server
   * @param {(http.Server|https.Server)} [options.server] A pre-created HTTP/S
   *     server to use
   * @param {Boolean} [options.skipUTF8Validation=false] Specifies whether or
   *     not to skip UTF-8 validation for text and close messages
   * @param {Function} [options.verifyClient] A hook to reject connections
   * @param {Function} [options.WebSocket=WebSocket] Specifies the `WebSocket`
   *     class to use. It must be the `WebSocket` class or class that extends it
   * @param {Function} [callback] A listener for the `listening` event
   */
  constructor(options, callback) {
    super();

    options = {
      allowSynchronousEvents: true,
      autoPong: true,
      maxPayload: 100 * 1024 * 1024,
      skipUTF8Validation: false,
      perMessageDeflate: false,
      handleProtocols: null,
      clientTracking: true,
      closeTimeout: CLOSE_TIMEOUT,
      verifyClient: null,
      noServer: false,
      backlog: null, // use default (511 as implemented in net.js)
      server: null,
      host: null,
      path: null,
      port: null,
      WebSocket,
      ...options
    };

    if (
      (options.port == null && !options.server && !options.noServer) ||
      (options.port != null && (options.server || options.noServer)) ||
      (options.server && options.noServer)
    ) {
      throw new TypeError(
        'One and only one of the "port", "server", or "noServer" options ' +
          'must be specified'
      );
    }

    if (options.port != null) {
      this._server = http.createServer((req, res) => {
        const body = http.STATUS_CODES[426];

        res.writeHead(426, {
          'Content-Length': body.length,
          'Content-Type': 'text/plain'
        });
        res.end(body);
      });
      this._server.listen(
        options.port,
        options.host,
        options.backlog,
        callback
      );
    } else if (options.server) {
      this._server = options.server;
    }

    if (this._server) {
      const emitConnection = this.emit.bind(this, 'connection');

      this._removeListeners = addListeners(this._server, {
        listening: this.emit.bind(this, 'listening'),
        error: this.emit.bind(this, 'error'),
        upgrade: (req, socket, head) => {
          this.handleUpgrade(req, socket, head, emitConnection);
        }
      });
    }

    if (options.perMessageDeflate === true) options.perMessageDeflate = {};
    if (options.clientTracking) {
      this.clients = new Set();
      this._shouldEmitClose = false;
    }

    this.options = options;
    this._state = RUNNING;
  }

  /**
   * Returns the bound address, the address family name, and port of the server
   * as reported by the operating system if listening on an IP socket.
   * If the server is listening on a pipe or UNIX domain socket, the name is
   * returned as a string.
   *
   * @return {(Object|String|null)} The address of the server
   * @public
   */
  address() {
    if (this.options.noServer) {
      throw new Error('The server is operating in "noServer" mode');
    }

    if (!this._server) return null;
    return this._server.address();
  }

  /**
   * Stop the server from accepting new connections and emit the `'close'` event
   * when all existing connections are closed.
   *
   * @param {Function} [cb] A one-time listener for the `'close'` event
   * @public
   */
  close(cb) {
    if (this._state === CLOSED) {
      if (cb) {
        this.once('close', () => {
          cb(new Error('The server is not running'));
        });
      }

      process.nextTick(emitClose, this);
      return;
    }

    if (cb) this.once('close', cb);

    if (this._state === CLOSING) return;
    this._state = CLOSING;

    if (this.options.noServer || this.options.server) {
      if (this._server) {
        this._removeListeners();
        this._removeListeners = this._server = null;
      }

      if (this.clients) {
        if (!this.clients.size) {
          process.nextTick(emitClose, this);
        } else {
          this._shouldEmitClose = true;
        }
      } else {
        process.nextTick(emitClose, this);
      }
    } else {
      const server = this._server;

      this._removeListeners();
      this._removeListeners = this._server = null;

      //
      // The HTTP/S server was created internally. Close it, and rely on its
      // `'close'` event.
      //
      server.close(() => {
        emitClose(this);
      });
    }
  }

  /**
   * See if a given request should be handled by this server instance.
   *
   * @param {http.IncomingMessage} req Request object to inspect
   * @return {Boolean} `true` if the request is valid, else `false`
   * @public
   */
  shouldHandle(req) {
    if (this.options.path) {
      const index = req.url.indexOf('?');
      const pathname = index !== -1 ? req.url.slice(0, index) : req.url;

      if (pathname !== this.options.path) return false;
    }

    return true;
  }

  /**
   * Handle a HTTP Upgrade request.
   *
   * @param {http.IncomingMessage} req The request object
   * @param {Duplex} socket The network socket between the server and client
   * @param {Buffer} head The first packet of the upgraded stream
   * @param {Function} cb Callback
   * @public
   */
  handleUpgrade(req, socket, head, cb) {
    socket.on('error', socketOnError);

    const key = req.headers['sec-websocket-key'];
    const upgrade = req.headers.upgrade;
    const version = +req.headers['sec-websocket-version'];

    if (req.method !== 'GET') {
      const message = 'Invalid HTTP method';
      abortHandshakeOrEmitwsClientError(this, req, socket, 405, message);
      return;
    }

    if (upgrade === undefined || upgrade.toLowerCase() !== 'websocket') {
      const message = 'Invalid Upgrade header';
      abortHandshakeOrEmitwsClientError(this, req, socket, 400, message);
      return;
    }

    if (key === undefined || !keyRegex.test(key)) {
      const message = 'Missing or invalid Sec-WebSocket-Key header';
      abortHandshakeOrEmitwsClientError(this, req, socket, 400, message);
      return;
    }

    if (version !== 13 && version !== 8) {
      const message = 'Missing or invalid Sec-WebSocket-Version header';
      abortHandshakeOrEmitwsClientError(this, req, socket, 400, message, {
        'Sec-WebSocket-Version': '13, 8'
      });
      return;
    }

    if (!this.shouldHandle(req)) {
      abortHandshake(socket, 400);
      return;
    }

    const secWebSocketProtocol = req.headers['sec-websocket-protocol'];
    let protocols = new Set();

    if (secWebSocketProtocol !== undefined) {
      try {
        protocols = subprotocol.parse(secWebSocketProtocol);
      } catch (err) {
        const message = 'Invalid Sec-WebSocket-Protocol header';
        abortHandshakeOrEmitwsClientError(this, req, socket, 400, message);
        return;
      }
    }

    const secWebSocketExtensions = req.headers['sec-websocket-extensions'];
    const extensions = {};

    if (
      this.options.perMessageDeflate &&
      secWebSocketExtensions !== undefined
    ) {
      const perMessageDeflate = new PerMessageDeflate({
        ...this.options.perMessageDeflate,
        isServer: true,
        maxPayload: this.options.maxPayload
      });

      try {
        const offers = extension.parse(secWebSocketExtensions);

        if (offers[PerMessageDeflate.extensionName]) {
          perMessageDeflate.accept(offers[PerMessageDeflate.extensionName]);
          extensions[PerMessageDeflate.extensionName] = perMessageDeflate;
        }
      } catch (err) {
        const message =
          'Invalid or unacceptable Sec-WebSocket-Extensions header';
        abortHandshakeOrEmitwsClientError(this, req, socket, 400, message);
        return;
      }
    }

    //
    // Optionally call external client verification handler.
    //
    if (this.options.verifyClient) {
      const info = {
        origin:
          req.headers[`${version === 8 ? 'sec-websocket-origin' : 'origin'}`],
        secure: !!(req.socket.authorized || req.socket.encrypted),
        req
      };

      if (this.options.verifyClient.length === 2) {
        this.options.verifyClient(info, (verified, code, message, headers) => {
          if (!verified) {
            return abortHandshake(socket, code || 401, message, headers);
          }

          this.completeUpgrade(
            extensions,
            key,
            protocols,
            req,
            socket,
            head,
            cb
          );
        });
        return;
      }

      if (!this.options.verifyClient(info)) return abortHandshake(socket, 401);
    }

    this.completeUpgrade(extensions, key, protocols, req, socket, head, cb);
  }

  /**
   * Upgrade the connection to WebSocket.
   *
   * @param {Object} extensions The accepted extensions
   * @param {String} key The value of the `Sec-WebSocket-Key` header
   * @param {Set} protocols The subprotocols
   * @param {http.IncomingMessage} req The request object
   * @param {Duplex} socket The network socket between the server and client
   * @param {Buffer} head The first packet of the upgraded stream
   * @param {Function} cb Callback
   * @throws {Error} If called more than once with the same socket
   * @private
   */
  completeUpgrade(extensions, key, protocols, req, socket, head, cb) {
    //
    // Destroy the socket if the client has already sent a FIN packet.
    //
    if (!socket.readable || !socket.writable) return socket.destroy();

    if (socket[kWebSocket]) {
      throw new Error(
        'server.handleUpgrade() was called more than once with the same ' +
          'socket, possibly due to a misconfiguration'
      );
    }

    if (this._state > RUNNING) return abortHandshake(socket, 503);

    const digest = createHash('sha1')
      .update(key + GUID)
      .digest('base64');

    const headers = [
      'HTTP/1.1 101 Switching Protocols',
      'Upgrade: websocket',
      'Connection: Upgrade',
      `Sec-WebSocket-Accept: ${digest}`
    ];

    const ws = new this.options.WebSocket(null, undefined, this.options);

    if (protocols.size) {
      //
      // Optionally call external protocol selection handler.
      //
      const protocol = this.options.handleProtocols
        ? this.options.handleProtocols(protocols, req)
        : protocols.values().next().value;

      if (protocol) {
        headers.push(`Sec-WebSocket-Protocol: ${protocol}`);
        ws._protocol = protocol;
      }
    }

    if (extensions[PerMessageDeflate.extensionName]) {
      const params = extensions[PerMessageDeflate.extensionName].params;
      const value = extension.format({
        [PerMessageDeflate.extensionName]: [params]
      });
      headers.push(`Sec-WebSocket-Extensions: ${value}`);
      ws._extensions = extensions;
    }

    //
    // Allow external modification/inspection of handshake headers.
    //
    this.emit('headers', headers, req);

    socket.write(headers.concat('\r\n').join('\r\n'));
    socket.removeListener('error', socketOnError);

    ws.setSocket(socket, head, {
      allowSynchronousEvents: this.options.allowSynchronousEvents,
      maxPayload: this.options.maxPayload,
      skipUTF8Validation: this.options.skipUTF8Validation
    });

    if (this.clients) {
      this.clients.add(ws);
      ws.on('close', () => {
        this.clients.delete(ws);

        if (this._shouldEmitClose && !this.clients.size) {
          process.nextTick(emitClose, this);
        }
      });
    }

    cb(ws, req);
  }
}

module.exports = WebSocketServer;

/**
 * Add event listeners on an `EventEmitter` using a map of <event, listener>
 * pairs.
 *
 * @param {EventEmitter} server The event emitter
 * @param {Object.<String, Function>} map The listeners to add
 * @return {Function} A function that will remove the added listeners when
 *     called
 * @private
 */
function addListeners(server, map) {
  for (const event of Object.keys(map)) server.on(event, map[event]);

  return function removeListeners() {
    for (const event of Object.keys(map)) {
      server.removeListener(event, map[event]);
    }
  };
}

/**
 * Emit a `'close'` event on an `EventEmitter`.
 *
 * @param {EventEmitter} server The event emitter
 * @private
 */
function emitClose(server) {
  server._state = CLOSED;
  server.emit('close');
}

/**
 * Handle socket errors.
 *
 * @private
 */
function socketOnError() {
  this.destroy();
}

/**
 * Close the connection when preconditions are not fulfilled.
 *
 * @param {Duplex} socket The socket of the upgrade request
 * @param {Number} code The HTTP response status code
 * @param {String} [message] The HTTP response body
 * @param {Object} [headers] Additional HTTP response headers
 * @private
 */
function abortHandshake(socket, code, message, headers) {
  //
  // The socket is writable unless the user destroyed or ended it before calling
  // `server.handleUpgrade()` or in the `verifyClient` function, which is a user
  // error. Handling this does not make much sense as the worst that can happen
  // is that some of the data written by the user might be discarded due to the
  // call to `socket.end()` below, which triggers an `'error'` event that in
  // turn causes the socket to be destroyed.
  //
  message = message || http.STATUS_CODES[code];
  headers = {
    Connection: 'close',
    'Content-Type': 'text/html',
    'Content-Length': Buffer.byteLength(message),
    ...headers
  };

  socket.once('finish', socket.destroy);

  socket.end(
    `HTTP/1.1 ${code} ${http.STATUS_CODES[code]}\r\n` +
      Object.keys(headers)
        .map((h) => `${h}: ${headers[h]}`)
        .join('\r\n') +
      '\r\n\r\n' +
      message
  );
}

/**
 * Emit a `'wsClientError'` event on a `WebSocketServer` if there is at least
 * one listener for it, otherwise call `abortHandshake()`.
 *
 * @param {WebSocketServer} server The WebSocket server
 * @param {http.IncomingMessage} req The request object
 * @param {Duplex} socket The socket of the upgrade request
 * @param {Number} code The HTTP response status code
 * @param {String} message The HTTP response body
 * @param {Object} [headers] The HTTP response headers
 * @private
 */
function abortHandshakeOrEmitwsClientError(
  server,
  req,
  socket,
  code,
  message,
  headers
) {
  if (server.listenerCount('wsClientError')) {
    const err = new Error(message);
    Error.captureStackTrace(err, abortHandshakeOrEmitwsClientError);

    server.emit('wsClientError', err, socket, req);
  } else {
    abortHandshake(socket, code, message, headers);
  }
}
```

## File: `lib/websocket.js`
```javascript
/* eslint no-unused-vars: ["error", { "varsIgnorePattern": "^Duplex|Readable$", "caughtErrors": "none" }] */

'use strict';

const EventEmitter = require('events');
const https = require('https');
const http = require('http');
const net = require('net');
const tls = require('tls');
const { randomBytes, createHash } = require('crypto');
const { Duplex, Readable } = require('stream');
const { URL } = require('url');

const PerMessageDeflate = require('./permessage-deflate');
const Receiver = require('./receiver');
const Sender = require('./sender');
const { isBlob } = require('./validation');

const {
  BINARY_TYPES,
  CLOSE_TIMEOUT,
  EMPTY_BUFFER,
  GUID,
  kForOnEventAttribute,
  kListener,
  kStatusCode,
  kWebSocket,
  NOOP
} = require('./constants');
const {
  EventTarget: { addEventListener, removeEventListener }
} = require('./event-target');
const { format, parse } = require('./extension');
const { toBuffer } = require('./buffer-util');

const kAborted = Symbol('kAborted');
const protocolVersions = [8, 13];
const readyStates = ['CONNECTING', 'OPEN', 'CLOSING', 'CLOSED'];
const subprotocolRegex = /^[!#$%&'*+\-.0-9A-Z^_`|a-z~]+$/;

/**
 * Class representing a WebSocket.
 *
 * @extends EventEmitter
 */
class WebSocket extends EventEmitter {
  /**
   * Create a new `WebSocket`.
   *
   * @param {(String|URL)} address The URL to which to connect
   * @param {(String|String[])} [protocols] The subprotocols
   * @param {Object} [options] Connection options
   */
  constructor(address, protocols, options) {
    super();

    this._binaryType = BINARY_TYPES[0];
    this._closeCode = 1006;
    this._closeFrameReceived = false;
    this._closeFrameSent = false;
    this._closeMessage = EMPTY_BUFFER;
    this._closeTimer = null;
    this._errorEmitted = false;
    this._extensions = {};
    this._paused = false;
    this._protocol = '';
    this._readyState = WebSocket.CONNECTING;
    this._receiver = null;
    this._sender = null;
    this._socket = null;

    if (address !== null) {
      this._bufferedAmount = 0;
      this._isServer = false;
      this._redirects = 0;

      if (protocols === undefined) {
        protocols = [];
      } else if (!Array.isArray(protocols)) {
        if (typeof protocols === 'object' && protocols !== null) {
          options = protocols;
          protocols = [];
        } else {
          protocols = [protocols];
        }
      }

      initAsClient(this, address, protocols, options);
    } else {
      this._autoPong = options.autoPong;
      this._closeTimeout = options.closeTimeout;
      this._isServer = true;
    }
  }

  /**
   * For historical reasons, the custom "nodebuffer" type is used by the default
   * instead of "blob".
   *
   * @type {String}
   */
  get binaryType() {
    return this._binaryType;
  }

  set binaryType(type) {
    if (!BINARY_TYPES.includes(type)) return;

    this._binaryType = type;

    //
    // Allow to change `binaryType` on the fly.
    //
    if (this._receiver) this._receiver._binaryType = type;
  }

  /**
   * @type {Number}
   */
  get bufferedAmount() {
    if (!this._socket) return this._bufferedAmount;

    return this._socket._writableState.length + this._sender._bufferedBytes;
  }

  /**
   * @type {String}
   */
  get extensions() {
    return Object.keys(this._extensions).join();
  }

  /**
   * @type {Boolean}
   */
  get isPaused() {
    return this._paused;
  }

  /**
   * @type {Function}
   */
  /* istanbul ignore next */
  get onclose() {
    return null;
  }

  /**
   * @type {Function}
   */
  /* istanbul ignore next */
  get onerror() {
    return null;
  }

  /**
   * @type {Function}
   */
  /* istanbul ignore next */
  get onopen() {
    return null;
  }

  /**
   * @type {Function}
   */
  /* istanbul ignore next */
  get onmessage() {
    return null;
  }

  /**
   * @type {String}
   */
  get protocol() {
    return this._protocol;
  }

  /**
   * @type {Number}
   */
  get readyState() {
    return this._readyState;
  }

  /**
   * @type {String}
   */
  get url() {
    return this._url;
  }

  /**
   * Set up the socket and the internal resources.
   *
   * @param {Duplex} socket The network socket between the server and client
   * @param {Buffer} head The first packet of the upgraded stream
   * @param {Object} options Options object
   * @param {Boolean} [options.allowSynchronousEvents=false] Specifies whether
   *     any of the `'message'`, `'ping'`, and `'pong'` events can be emitted
   *     multiple times in the same tick
   * @param {Function} [options.generateMask] The function used to generate the
   *     masking key
   * @param {Number} [options.maxPayload=0] The maximum allowed message size
   * @param {Boolean} [options.skipUTF8Validation=false] Specifies whether or
   *     not to skip UTF-8 validation for text and close messages
   * @private
   */
  setSocket(socket, head, options) {
    const receiver = new Receiver({
      allowSynchronousEvents: options.allowSynchronousEvents,
      binaryType: this.binaryType,
      extensions: this._extensions,
      isServer: this._isServer,
      maxPayload: options.maxPayload,
      skipUTF8Validation: options.skipUTF8Validation
    });

    const sender = new Sender(socket, this._extensions, options.generateMask);

    this._receiver = receiver;
    this._sender = sender;
    this._socket = socket;

    receiver[kWebSocket] = this;
    sender[kWebSocket] = this;
    socket[kWebSocket] = this;

    receiver.on('conclude', receiverOnConclude);
    receiver.on('drain', receiverOnDrain);
    receiver.on('error', receiverOnError);
    receiver.on('message', receiverOnMessage);
    receiver.on('ping', receiverOnPing);
    receiver.on('pong', receiverOnPong);

    sender.onerror = senderOnError;

    //
    // These methods may not be available if `socket` is just a `Duplex`.
    //
    if (socket.setTimeout) socket.setTimeout(0);
    if (socket.setNoDelay) socket.setNoDelay();

    if (head.length > 0) socket.unshift(head);

    socket.on('close', socketOnClose);
    socket.on('data', socketOnData);
    socket.on('end', socketOnEnd);
    socket.on('error', socketOnError);

    this._readyState = WebSocket.OPEN;
    this.emit('open');
  }

  /**
   * Emit the `'close'` event.
   *
   * @private
   */
  emitClose() {
    if (!this._socket) {
      this._readyState = WebSocket.CLOSED;
      this.emit('close', this._closeCode, this._closeMessage);
      return;
    }

    if (this._extensions[PerMessageDeflate.extensionName]) {
      this._extensions[PerMessageDeflate.extensionName].cleanup();
    }

    this._receiver.removeAllListeners();
    this._readyState = WebSocket.CLOSED;
    this.emit('close', this._closeCode, this._closeMessage);
  }

  /**
   * Start a closing handshake.
   *
   *          +----------+   +-----------+   +----------+
   *     - - -|ws.close()|-->|close frame|-->|ws.close()|- - -
   *    |     +----------+   +-----------+   +----------+     |
   *          +----------+   +-----------+         |
   * CLOSING  |ws.close()|<--|close frame|<--+-----+       CLOSING
   *          +----------+   +-----------+   |
   *    |           |                        |   +---+        |
   *                +------------------------+-->|fin| - - - -
   *    |         +---+                      |   +---+
   *     - - - - -|fin|<---------------------+
   *              +---+
   *
   * @param {Number} [code] Status code explaining why the connection is closing
   * @param {(String|Buffer)} [data] The reason why the connection is
   *     closing
   * @public
   */
  close(code, data) {
    if (this.readyState === WebSocket.CLOSED) return;
    if (this.readyState === WebSocket.CONNECTING) {
      const msg = 'WebSocket was closed before the connection was established';
      abortHandshake(this, this._req, msg);
      return;
    }

    if (this.readyState === WebSocket.CLOSING) {
      if (
        this._closeFrameSent &&
        (this._closeFrameReceived || this._receiver._writableState.errorEmitted)
      ) {
        this._socket.end();
      }

      return;
    }

    this._readyState = WebSocket.CLOSING;
    this._sender.close(code, data, !this._isServer, (err) => {
      //
      // This error is handled by the `'error'` listener on the socket. We only
      // want to know if the close frame has been sent here.
      //
      if (err) return;

      this._closeFrameSent = true;

      if (
        this._closeFrameReceived ||
        this._receiver._writableState.errorEmitted
      ) {
        this._socket.end();
      }
    });

    setCloseTimer(this);
  }

  /**
   * Pause the socket.
   *
   * @public
   */
  pause() {
    if (
      this.readyState === WebSocket.CONNECTING ||
      this.readyState === WebSocket.CLOSED
    ) {
      return;
    }

    this._paused = true;
    this._socket.pause();
  }

  /**
   * Send a ping.
   *
   * @param {*} [data] The data to send
   * @param {Boolean} [mask] Indicates whether or not to mask `data`
   * @param {Function} [cb] Callback which is executed when the ping is sent
   * @public
   */
  ping(data, mask, cb) {
    if (this.readyState === WebSocket.CONNECTING) {
      throw new Error('WebSocket is not open: readyState 0 (CONNECTING)');
    }

    if (typeof data === 'function') {
      cb = data;
      data = mask = undefined;
    } else if (typeof mask === 'function') {
      cb = mask;
      mask = undefined;
    }

    if (typeof data === 'number') data = data.toString();

    if (this.readyState !== WebSocket.OPEN) {
      sendAfterClose(this, data, cb);
      return;
    }

    if (mask === undefined) mask = !this._isServer;
    this._sender.ping(data || EMPTY_BUFFER, mask, cb);
  }

  /**
   * Send a pong.
   *
   * @param {*} [data] The data to send
   * @param {Boolean} [mask] Indicates whether or not to mask `data`
   * @param {Function} [cb] Callback which is executed when the pong is sent
   * @public
   */
  pong(data, mask, cb) {
    if (this.readyState === WebSocket.CONNECTING) {
      throw new Error('WebSocket is not open: readyState 0 (CONNECTING)');
    }

    if (typeof data === 'function') {
      cb = data;
      data = mask = undefined;
    } else if (typeof mask === 'function') {
      cb = mask;
      mask = undefined;
    }

    if (typeof data === 'number') data = data.toString();

    if (this.readyState !== WebSocket.OPEN) {
      sendAfterClose(this, data, cb);
      return;
    }

    if (mask === undefined) mask = !this._isServer;
    this._sender.pong(data || EMPTY_BUFFER, mask, cb);
  }

  /**
   * Resume the socket.
   *
   * @public
   */
  resume() {
    if (
      this.readyState === WebSocket.CONNECTING ||
      this.readyState === WebSocket.CLOSED
    ) {
      return;
    }

    this._paused = false;
    if (!this._receiver._writableState.needDrain) this._socket.resume();
  }

  /**
   * Send a data message.
   *
   * @param {*} data The message to send
   * @param {Object} [options] Options object
   * @param {Boolean} [options.binary] Specifies whether `data` is binary or
   *     text
   * @param {Boolean} [options.compress] Specifies whether or not to compress
   *     `data`
   * @param {Boolean} [options.fin=true] Specifies whether the fragment is the
   *     last one
   * @param {Boolean} [options.mask] Specifies whether or not to mask `data`
   * @param {Function} [cb] Callback which is executed when data is written out
   * @public
   */
  send(data, options, cb) {
    if (this.readyState === WebSocket.CONNECTING) {
      throw new Error('WebSocket is not open: readyState 0 (CONNECTING)');
    }

    if (typeof options === 'function') {
      cb = options;
      options = {};
    }

    if (typeof data === 'number') data = data.toString();

    if (this.readyState !== WebSocket.OPEN) {
      sendAfterClose(this, data, cb);
      return;
    }

    const opts = {
      binary: typeof data !== 'string',
      mask: !this._isServer,
      compress: true,
      fin: true,
      ...options
    };

    if (!this._extensions[PerMessageDeflate.extensionName]) {
      opts.compress = false;
    }

    this._sender.send(data || EMPTY_BUFFER, opts, cb);
  }

  /**
   * Forcibly close the connection.
   *
   * @public
   */
  terminate() {
    if (this.readyState === WebSocket.CLOSED) return;
    if (this.readyState === WebSocket.CONNECTING) {
      const msg = 'WebSocket was closed before the connection was established';
      abortHandshake(this, this._req, msg);
      return;
    }

    if (this._socket) {
      this._readyState = WebSocket.CLOSING;
      this._socket.destroy();
    }
  }
}

/**
 * @constant {Number} CONNECTING
 * @memberof WebSocket
 */
Object.defineProperty(WebSocket, 'CONNECTING', {
  enumerable: true,
  value: readyStates.indexOf('CONNECTING')
});

/**
 * @constant {Number} CONNECTING
 * @memberof WebSocket.prototype
 */
Object.defineProperty(WebSocket.prototype, 'CONNECTING', {
  enumerable: true,
  value: readyStates.indexOf('CONNECTING')
});

/**
 * @constant {Number} OPEN
 * @memberof WebSocket
 */
Object.defineProperty(WebSocket, 'OPEN', {
  enumerable: true,
  value: readyStates.indexOf('OPEN')
});

/**
 * @constant {Number} OPEN
 * @memberof WebSocket.prototype
 */
Object.defineProperty(WebSocket.prototype, 'OPEN', {
  enumerable: true,
  value: readyStates.indexOf('OPEN')
});

/**
 * @constant {Number} CLOSING
 * @memberof WebSocket
 */
Object.defineProperty(WebSocket, 'CLOSING', {
  enumerable: true,
  value: readyStates.indexOf('CLOSING')
});

/**
 * @constant {Number} CLOSING
 * @memberof WebSocket.prototype
 */
Object.defineProperty(WebSocket.prototype, 'CLOSING', {
  enumerable: true,
  value: readyStates.indexOf('CLOSING')
});

/**
 * @constant {Number} CLOSED
 * @memberof WebSocket
 */
Object.defineProperty(WebSocket, 'CLOSED', {
  enumerable: true,
  value: readyStates.indexOf('CLOSED')
});

/**
 * @constant {Number} CLOSED
 * @memberof WebSocket.prototype
 */
Object.defineProperty(WebSocket.prototype, 'CLOSED', {
  enumerable: true,
  value: readyStates.indexOf('CLOSED')
});

[
  'binaryType',
  'bufferedAmount',
  'extensions',
  'isPaused',
  'protocol',
  'readyState',
  'url'
].forEach((property) => {
  Object.defineProperty(WebSocket.prototype, property, { enumerable: true });
});

//
// Add the `onopen`, `onerror`, `onclose`, and `onmessage` attributes.
// See https://html.spec.whatwg.org/multipage/comms.html#the-websocket-interface
//
['open', 'error', 'close', 'message'].forEach((method) => {
  Object.defineProperty(WebSocket.prototype, `on${method}`, {
    enumerable: true,
    get() {
      for (const listener of this.listeners(method)) {
        if (listener[kForOnEventAttribute]) return listener[kListener];
      }

      return null;
    },
    set(handler) {
      for (const listener of this.listeners(method)) {
        if (listener[kForOnEventAttribute]) {
          this.removeListener(method, listener);
          break;
        }
      }

      if (typeof handler !== 'function') return;

      this.addEventListener(method, handler, {
        [kForOnEventAttribute]: true
      });
    }
  });
});

WebSocket.prototype.addEventListener = addEventListener;
WebSocket.prototype.removeEventListener = removeEventListener;

module.exports = WebSocket;

/**
 * Initialize a WebSocket client.
 *
 * @param {WebSocket} websocket The client to initialize
 * @param {(String|URL)} address The URL to which to connect
 * @param {Array} protocols The subprotocols
 * @param {Object} [options] Connection options
 * @param {Boolean} [options.allowSynchronousEvents=true] Specifies whether any
 *     of the `'message'`, `'ping'`, and `'pong'` events can be emitted multiple
 *     times in the same tick
 * @param {Boolean} [options.autoPong=true] Specifies whether or not to
 *     automatically send a pong in response to a ping
 * @param {Number} [options.closeTimeout=30000] Duration in milliseconds to wait
 *     for the closing handshake to finish after `websocket.close()` is called
 * @param {Function} [options.finishRequest] A function which can be used to
 *     customize the headers of each http request before it is sent
 * @param {Boolean} [options.followRedirects=false] Whether or not to follow
 *     redirects
 * @param {Function} [options.generateMask] The function used to generate the
 *     masking key
 * @param {Number} [options.handshakeTimeout] Timeout in milliseconds for the
 *     handshake request
 * @param {Number} [options.maxPayload=104857600] The maximum allowed message
 *     size
 * @param {Number} [options.maxRedirects=10] The maximum number of redirects
 *     allowed
 * @param {String} [options.origin] Value of the `Origin` or
 *     `Sec-WebSocket-Origin` header
 * @param {(Boolean|Object)} [options.perMessageDeflate=true] Enable/disable
 *     permessage-deflate
 * @param {Number} [options.protocolVersion=13] Value of the
 *     `Sec-WebSocket-Version` header
 * @param {Boolean} [options.skipUTF8Validation=false] Specifies whether or
 *     not to skip UTF-8 validation for text and close messages
 * @private
 */
function initAsClient(websocket, address, protocols, options) {
  const opts = {
    allowSynchronousEvents: true,
    autoPong: true,
    closeTimeout: CLOSE_TIMEOUT,
    protocolVersion: protocolVersions[1],
    maxPayload: 100 * 1024 * 1024,
    skipUTF8Validation: false,
    perMessageDeflate: true,
    followRedirects: false,
    maxRedirects: 10,
    ...options,
    socketPath: undefined,
    hostname: undefined,
    protocol: undefined,
    timeout: undefined,
    method: 'GET',
    host: undefined,
    path: undefined,
    port: undefined
  };

  websocket._autoPong = opts.autoPong;
  websocket._closeTimeout = opts.closeTimeout;

  if (!protocolVersions.includes(opts.protocolVersion)) {
    throw new RangeError(
      `Unsupported protocol version: ${opts.protocolVersion} ` +
        `(supported versions: ${protocolVersions.join(', ')})`
    );
  }

  let parsedUrl;

  if (address instanceof URL) {
    parsedUrl = address;
  } else {
    try {
      parsedUrl = new URL(address);
    } catch {
      throw new SyntaxError(`Invalid URL: ${address}`);
    }
  }

  if (parsedUrl.protocol === 'http:') {
    parsedUrl.protocol = 'ws:';
  } else if (parsedUrl.protocol === 'https:') {
    parsedUrl.protocol = 'wss:';
  }

  websocket._url = parsedUrl.href;

  const isSecure = parsedUrl.protocol === 'wss:';
  const isIpcUrl = parsedUrl.protocol === 'ws+unix:';
  let invalidUrlMessage;

  if (parsedUrl.protocol !== 'ws:' && !isSecure && !isIpcUrl) {
    invalidUrlMessage =
      'The URL\'s protocol must be one of "ws:", "wss:", ' +
      '"http:", "https:", or "ws+unix:"';
  } else if (isIpcUrl && !parsedUrl.pathname) {
    invalidUrlMessage = "The URL's pathname is empty";
  } else if (parsedUrl.hash) {
    invalidUrlMessage = 'The URL contains a fragment identifier';
  }

  if (invalidUrlMessage) {
    const err = new SyntaxError(invalidUrlMessage);

    if (websocket._redirects === 0) {
      throw err;
    } else {
      emitErrorAndClose(websocket, err);
      return;
    }
  }

  const defaultPort = isSecure ? 443 : 80;
  const key = randomBytes(16).toString('base64');
  const request = isSecure ? https.request : http.request;
  const protocolSet = new Set();
  let perMessageDeflate;

  opts.createConnection =
    opts.createConnection || (isSecure ? tlsConnect : netConnect);
  opts.defaultPort = opts.defaultPort || defaultPort;
  opts.port = parsedUrl.port || defaultPort;
  opts.host = parsedUrl.hostname.startsWith('[')
    ? parsedUrl.hostname.slice(1, -1)
    : parsedUrl.hostname;
  opts.headers = {
    ...opts.headers,
    'Sec-WebSocket-Version': opts.protocolVersion,
    'Sec-WebSocket-Key': key,
    Connection: 'Upgrade',
    Upgrade: 'websocket'
  };
  opts.path = parsedUrl.pathname + parsedUrl.search;
  opts.timeout = opts.handshakeTimeout;

  if (opts.perMessageDeflate) {
    perMessageDeflate = new PerMessageDeflate({
      ...opts.perMessageDeflate,
      isServer: false,
      maxPayload: opts.maxPayload
    });
    opts.headers['Sec-WebSocket-Extensions'] = format({
      [PerMessageDeflate.extensionName]: perMessageDeflate.offer()
    });
  }
  if (protocols.length) {
    for (const protocol of protocols) {
      if (
        typeof protocol !== 'string' ||
        !subprotocolRegex.test(protocol) ||
        protocolSet.has(protocol)
      ) {
        throw new SyntaxError(
          'An invalid or duplicated subprotocol was specified'
        );
      }

      protocolSet.add(protocol);
    }

    opts.headers['Sec-WebSocket-Protocol'] = protocols.join(',');
  }
  if (opts.origin) {
    if (opts.protocolVersion < 13) {
      opts.headers['Sec-WebSocket-Origin'] = opts.origin;
    } else {
      opts.headers.Origin = opts.origin;
    }
  }
  if (parsedUrl.username || parsedUrl.password) {
    opts.auth = `${parsedUrl.username}:${parsedUrl.password}`;
  }

  if (isIpcUrl) {
    const parts = opts.path.split(':');

    opts.socketPath = parts[0];
    opts.path = parts[1];
  }

  let req;

  if (opts.followRedirects) {
    if (websocket._redirects === 0) {
      websocket._originalIpc = isIpcUrl;
      websocket._originalSecure = isSecure;
      websocket._originalHostOrSocketPath = isIpcUrl
        ? opts.socketPath
        : parsedUrl.host;

      const headers = options && options.headers;

      //
      // Shallow copy the user provided options so that headers can be changed
      // without mutating the original object.
      //
      options = { ...options, headers: {} };

      if (headers) {
        for (const [key, value] of Object.entries(headers)) {
          options.headers[key.toLowerCase()] = value;
        }
      }
    } else if (websocket.listenerCount('redirect') === 0) {
      const isSameHost = isIpcUrl
        ? websocket._originalIpc
          ? opts.socketPath === websocket._originalHostOrSocketPath
          : false
        : websocket._originalIpc
          ? false
          : parsedUrl.host === websocket._originalHostOrSocketPath;

      if (!isSameHost || (websocket._originalSecure && !isSecure)) {
        //
        // Match curl 7.77.0 behavior and drop the following headers. These
        // headers are also dropped when following a redirect to a subdomain.
        //
        delete opts.headers.authorization;
        delete opts.headers.cookie;

        if (!isSameHost) delete opts.headers.host;

        opts.auth = undefined;
      }
    }

    //
    // Match curl 7.77.0 behavior and make the first `Authorization` header win.
    // If the `Authorization` header is set, then there is nothing to do as it
    // will take precedence.
    //
    if (opts.auth && !options.headers.authorization) {
      options.headers.authorization =
        'Basic ' + Buffer.from(opts.auth).toString('base64');
    }

    req = websocket._req = request(opts);

    if (websocket._redirects) {
      //
      // Unlike what is done for the `'upgrade'` event, no early exit is
      // triggered here if the user calls `websocket.close()` or
      // `websocket.terminate()` from a listener of the `'redirect'` event. This
      // is because the user can also call `request.destroy()` with an error
      // before calling `websocket.close()` or `websocket.terminate()` and this
      // would result in an error being emitted on the `request` object with no
      // `'error'` event listeners attached.
      //
      websocket.emit('redirect', websocket.url, req);
    }
  } else {
    req = websocket._req = request(opts);
  }

  if (opts.timeout) {
    req.on('timeout', () => {
      abortHandshake(websocket, req, 'Opening handshake has timed out');
    });
  }

  req.on('error', (err) => {
    if (req === null || req[kAborted]) return;

    req = websocket._req = null;
    emitErrorAndClose(websocket, err);
  });

  req.on('response', (res) => {
    const location = res.headers.location;
    const statusCode = res.statusCode;

    if (
      location &&
      opts.followRedirects &&
      statusCode >= 300 &&
      statusCode < 400
    ) {
      if (++websocket._redirects > opts.maxRedirects) {
        abortHandshake(websocket, req, 'Maximum redirects exceeded');
        return;
      }

      req.abort();

      let addr;

      try {
        addr = new URL(location, address);
      } catch (e) {
        const err = new SyntaxError(`Invalid URL: ${location}`);
        emitErrorAndClose(websocket, err);
        return;
      }

      initAsClient(websocket, addr, protocols, options);
    } else if (!websocket.emit('unexpected-response', req, res)) {
      abortHandshake(
        websocket,
        req,
        `Unexpected server response: ${res.statusCode}`
      );
    }
  });

  req.on('upgrade', (res, socket, head) => {
    websocket.emit('upgrade', res);

    //
    // The user may have closed the connection from a listener of the
    // `'upgrade'` event.
    //
    if (websocket.readyState !== WebSocket.CONNECTING) return;

    req = websocket._req = null;

    const upgrade = res.headers.upgrade;

    if (upgrade === undefined || upgrade.toLowerCase() !== 'websocket') {
      abortHandshake(websocket, socket, 'Invalid Upgrade header');
      return;
    }

    const digest = createHash('sha1')
      .update(key + GUID)
      .digest('base64');

    if (res.headers['sec-websocket-accept'] !== digest) {
      abortHandshake(websocket, socket, 'Invalid Sec-WebSocket-Accept header');
      return;
    }

    const serverProt = res.headers['sec-websocket-protocol'];
    let protError;

    if (serverProt !== undefined) {
      if (!protocolSet.size) {
        protError = 'Server sent a subprotocol but none was requested';
      } else if (!protocolSet.has(serverProt)) {
        protError = 'Server sent an invalid subprotocol';
      }
    } else if (protocolSet.size) {
      protError = 'Server sent no subprotocol';
    }

    if (protError) {
      abortHandshake(websocket, socket, protError);
      return;
    }

    if (serverProt) websocket._protocol = serverProt;

    const secWebSocketExtensions = res.headers['sec-websocket-extensions'];

    if (secWebSocketExtensions !== undefined) {
      if (!perMessageDeflate) {
        const message =
          'Server sent a Sec-WebSocket-Extensions header but no extension ' +
          'was requested';
        abortHandshake(websocket, socket, message);
        return;
      }

      let extensions;

      try {
        extensions = parse(secWebSocketExtensions);
      } catch (err) {
        const message = 'Invalid Sec-WebSocket-Extensions header';
        abortHandshake(websocket, socket, message);
        return;
      }

      const extensionNames = Object.keys(extensions);

      if (
        extensionNames.length !== 1 ||
        extensionNames[0] !== PerMessageDeflate.extensionName
      ) {
        const message = 'Server indicated an extension that was not requested';
        abortHandshake(websocket, socket, message);
        return;
      }

      try {
        perMessageDeflate.accept(extensions[PerMessageDeflate.extensionName]);
      } catch (err) {
        const message = 'Invalid Sec-WebSocket-Extensions header';
        abortHandshake(websocket, socket, message);
        return;
      }

      websocket._extensions[PerMessageDeflate.extensionName] =
        perMessageDeflate;
    }

    websocket.setSocket(socket, head, {
      allowSynchronousEvents: opts.allowSynchronousEvents,
      generateMask: opts.generateMask,
      maxPayload: opts.maxPayload,
      skipUTF8Validation: opts.skipUTF8Validation
    });
  });

  if (opts.finishRequest) {
    opts.finishRequest(req, websocket);
  } else {
    req.end();
  }
}

/**
 * Emit the `'error'` and `'close'` events.
 *
 * @param {WebSocket} websocket The WebSocket instance
 * @param {Error} The error to emit
 * @private
 */
function emitErrorAndClose(websocket, err) {
  websocket._readyState = WebSocket.CLOSING;
  //
  // The following assignment is practically useless and is done only for
  // consistency.
  //
  websocket._errorEmitted = true;
  websocket.emit('error', err);
  websocket.emitClose();
}

/**
 * Create a `net.Socket` and initiate a connection.
 *
 * @param {Object} options Connection options
 * @return {net.Socket} The newly created socket used to start the connection
 * @private
 */
function netConnect(options) {
  options.path = options.socketPath;
  return net.connect(options);
}

/**
 * Create a `tls.TLSSocket` and initiate a connection.
 *
 * @param {Object} options Connection options
 * @return {tls.TLSSocket} The newly created socket used to start the connection
 * @private
 */
function tlsConnect(options) {
  options.path = undefined;

  if (!options.servername && options.servername !== '') {
    options.servername = net.isIP(options.host) ? '' : options.host;
  }

  return tls.connect(options);
}

/**
 * Abort the handshake and emit an error.
 *
 * @param {WebSocket} websocket The WebSocket instance
 * @param {(http.ClientRequest|net.Socket|tls.Socket)} stream The request to
 *     abort or the socket to destroy
 * @param {String} message The error message
 * @private
 */
function abortHandshake(websocket, stream, message) {
  websocket._readyState = WebSocket.CLOSING;

  const err = new Error(message);
  Error.captureStackTrace(err, abortHandshake);

  if (stream.setHeader) {
    stream[kAborted] = true;
    stream.abort();

    if (stream.socket && !stream.socket.destroyed) {
      //
      // On Node.js >= 14.3.0 `request.abort()` does not destroy the socket if
      // called after the request completed. See
      // https://github.com/websockets/ws/issues/1869.
      //
      stream.socket.destroy();
    }

    process.nextTick(emitErrorAndClose, websocket, err);
  } else {
    stream.destroy(err);
    stream.once('error', websocket.emit.bind(websocket, 'error'));
    stream.once('close', websocket.emitClose.bind(websocket));
  }
}

/**
 * Handle cases where the `ping()`, `pong()`, or `send()` methods are called
 * when the `readyState` attribute is `CLOSING` or `CLOSED`.
 *
 * @param {WebSocket} websocket The WebSocket instance
 * @param {*} [data] The data to send
 * @param {Function} [cb] Callback
 * @private
 */
function sendAfterClose(websocket, data, cb) {
  if (data) {
    const length = isBlob(data) ? data.size : toBuffer(data).length;

    //
    // The `_bufferedAmount` property is used only when the peer is a client and
    // the opening handshake fails. Under these circumstances, in fact, the
    // `setSocket()` method is not called, so the `_socket` and `_sender`
    // properties are set to `null`.
    //
    if (websocket._socket) websocket._sender._bufferedBytes += length;
    else websocket._bufferedAmount += length;
  }

  if (cb) {
    const err = new Error(
      `WebSocket is not open: readyState ${websocket.readyState} ` +
        `(${readyStates[websocket.readyState]})`
    );
    process.nextTick(cb, err);
  }
}

/**
 * The listener of the `Receiver` `'conclude'` event.
 *
 * @param {Number} code The status code
 * @param {Buffer} reason The reason for closing
 * @private
 */
function receiverOnConclude(code, reason) {
  const websocket = this[kWebSocket];

  websocket._closeFrameReceived = true;
  websocket._closeMessage = reason;
  websocket._closeCode = code;

  if (websocket._socket[kWebSocket] === undefined) return;

  websocket._socket.removeListener('data', socketOnData);
  process.nextTick(resume, websocket._socket);

  if (code === 1005) websocket.close();
  else websocket.close(code, reason);
}

/**
 * The listener of the `Receiver` `'drain'` event.
 *
 * @private
 */
function receiverOnDrain() {
  const websocket = this[kWebSocket];

  if (!websocket.isPaused) websocket._socket.resume();
}

/**
 * The listener of the `Receiver` `'error'` event.
 *
 * @param {(RangeError|Error)} err The emitted error
 * @private
 */
function receiverOnError(err) {
  const websocket = this[kWebSocket];

  if (websocket._socket[kWebSocket] !== undefined) {
    websocket._socket.removeListener('data', socketOnData);

    //
    // On Node.js < 14.0.0 the `'error'` event is emitted synchronously. See
    // https://github.com/websockets/ws/issues/1940.
    //
    process.nextTick(resume, websocket._socket);

    websocket.close(err[kStatusCode]);
  }

  if (!websocket._errorEmitted) {
    websocket._errorEmitted = true;
    websocket.emit('error', err);
  }
}

/**
 * The listener of the `Receiver` `'finish'` event.
 *
 * @private
 */
function receiverOnFinish() {
  this[kWebSocket].emitClose();
}

/**
 * The listener of the `Receiver` `'message'` event.
 *
 * @param {Buffer|ArrayBuffer|Buffer[])} data The message
 * @param {Boolean} isBinary Specifies whether the message is binary or not
 * @private
 */
function receiverOnMessage(data, isBinary) {
  this[kWebSocket].emit('message', data, isBinary);
}

/**
 * The listener of the `Receiver` `'ping'` event.
 *
 * @param {Buffer} data The data included in the ping frame
 * @private
 */
function receiverOnPing(data) {
  const websocket = this[kWebSocket];

  if (websocket._autoPong) websocket.pong(data, !this._isServer, NOOP);
  websocket.emit('ping', data);
}

/**
 * The listener of the `Receiver` `'pong'` event.
 *
 * @param {Buffer} data The data included in the pong frame
 * @private
 */
function receiverOnPong(data) {
  this[kWebSocket].emit('pong', data);
}

/**
 * Resume a readable stream
 *
 * @param {Readable} stream The readable stream
 * @private
 */
function resume(stream) {
  stream.resume();
}

/**
 * The `Sender` error event handler.
 *
 * @param {Error} The error
 * @private
 */
function senderOnError(err) {
  const websocket = this[kWebSocket];

  if (websocket.readyState === WebSocket.CLOSED) return;
  if (websocket.readyState === WebSocket.OPEN) {
    websocket._readyState = WebSocket.CLOSING;
    setCloseTimer(websocket);
  }

  //
  // `socket.end()` is used instead of `socket.destroy()` to allow the other
  // peer to finish sending queued data. There is no need to set a timer here
  // because `CLOSING` means that it is already set or not needed.
  //
  this._socket.end();

  if (!websocket._errorEmitted) {
    websocket._errorEmitted = true;
    websocket.emit('error', err);
  }
}

/**
 * Set a timer to destroy the underlying raw socket of a WebSocket.
 *
 * @param {WebSocket} websocket The WebSocket instance
 * @private
 */
function setCloseTimer(websocket) {
  websocket._closeTimer = setTimeout(
    websocket._socket.destroy.bind(websocket._socket),
    websocket._closeTimeout
  );
}

/**
 * The listener of the socket `'close'` event.
 *
 * @private
 */
function socketOnClose() {
  const websocket = this[kWebSocket];

  this.removeListener('close', socketOnClose);
  this.removeListener('data', socketOnData);
  this.removeListener('end', socketOnEnd);

  websocket._readyState = WebSocket.CLOSING;

  //
  // The close frame might not have been received or the `'end'` event emitted,
  // for example, if the socket was destroyed due to an error. Ensure that the
  // `receiver` stream is closed after writing any remaining buffered data to
  // it. If the readable side of the socket is in flowing mode then there is no
  // buffered data as everything has been already written. If instead, the
  // socket is paused, any possible buffered data will be read as a single
  // chunk.
  //
  if (
    !this._readableState.endEmitted &&
    !websocket._closeFrameReceived &&
    !websocket._receiver._writableState.errorEmitted &&
    this._readableState.length !== 0
  ) {
    const chunk = this.read(this._readableState.length);

    websocket._receiver.write(chunk);
  }

  websocket._receiver.end();

  this[kWebSocket] = undefined;

  clearTimeout(websocket._closeTimer);

  if (
    websocket._receiver._writableState.finished ||
    websocket._receiver._writableState.errorEmitted
  ) {
    websocket.emitClose();
  } else {
    websocket._receiver.on('error', receiverOnFinish);
    websocket._receiver.on('finish', receiverOnFinish);
  }
}

/**
 * The listener of the socket `'data'` event.
 *
 * @param {Buffer} chunk A chunk of data
 * @private
 */
function socketOnData(chunk) {
  if (!this[kWebSocket]._receiver.write(chunk)) {
    this.pause();
  }
}

/**
 * The listener of the socket `'end'` event.
 *
 * @private
 */
function socketOnEnd() {
  const websocket = this[kWebSocket];

  websocket._readyState = WebSocket.CLOSING;
  websocket._receiver.end();
  this.end();
}

/**
 * The listener of the socket `'error'` event.
 *
 * @private
 */
function socketOnError() {
  const websocket = this[kWebSocket];

  this.removeListener('error', socketOnError);
  this.on('error', NOOP);

  if (websocket) {
    websocket._readyState = WebSocket.CLOSING;
    this.destroy();
  }
}
```

## File: `test/autobahn-server.js`
```javascript
'use strict';

const WebSocket = require('../');

const port = process.argv.length > 2 ? parseInt(process.argv[2]) : 9001;
const wss = new WebSocket.Server({ port }, () => {
  console.log(
    `Listening to port ${port}. Use extra argument to define the port`
  );
});

wss.on('connection', (ws) => {
  ws.on('message', (data, isBinary) => {
    ws.send(data, { binary: isBinary });
  });
  ws.on('error', (e) => console.error(e));
});
```

## File: `test/autobahn.js`
```javascript
'use strict';

const WebSocket = require('../');

let currentTest = 1;
let testCount;

function nextTest() {
  let ws;

  if (currentTest > testCount) {
    ws = new WebSocket('ws://localhost:9001/updateReports?agent=ws');
    return;
  }

  console.log(`Running test case ${currentTest}/${testCount}`);

  ws = new WebSocket(
    `ws://localhost:9001/runCase?case=${currentTest}&agent=ws`
  );
  ws.on('message', (data, isBinary) => {
    ws.send(data, { binary: isBinary });
  });
  ws.on('close', () => {
    currentTest++;
    process.nextTick(nextTest);
  });
  ws.on('error', (e) => console.error(e));
}

const ws = new WebSocket('ws://localhost:9001/getCaseCount');
ws.on('message', (data) => {
  testCount = parseInt(data);
});
ws.on('close', () => {
  if (testCount > 0) {
    nextTest();
  }
});
```

## File: `test/buffer-util.test.js`
```javascript
'use strict';

const assert = require('assert');

const { concat } = require('../lib/buffer-util');

describe('bufferUtil', () => {
  describe('concat', () => {
    it('never returns uninitialized data', () => {
      const buf = concat([Buffer.from([1, 2]), Buffer.from([3, 4])], 6);

      assert.ok(buf.equals(Buffer.from([1, 2, 3, 4])));
    });
  });
});
```

## File: `test/create-websocket-stream.test.js`
```javascript
'use strict';

const assert = require('assert');
const EventEmitter = require('events');
const { createServer } = require('http');
const { Duplex, getDefaultHighWaterMark } = require('stream');
const { randomBytes } = require('crypto');

const createWebSocketStream = require('../lib/stream');
const Sender = require('../lib/sender');
const WebSocket = require('..');
const { EMPTY_BUFFER } = require('../lib/constants');

const highWaterMark = getDefaultHighWaterMark
  ? getDefaultHighWaterMark(false)
  : 16 * 1024;

describe('createWebSocketStream', () => {
  it('is exposed as a property of the `WebSocket` class', () => {
    assert.strictEqual(WebSocket.createWebSocketStream, createWebSocketStream);
  });

  it('returns a `Duplex` stream', () => {
    const duplex = createWebSocketStream(new EventEmitter());

    assert.ok(duplex instanceof Duplex);
  });

  it('passes the options object to the `Duplex` constructor', (done) => {
    const wss = new WebSocket.Server({ port: 0 }, () => {
      const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
      const duplex = createWebSocketStream(ws, {
        allowHalfOpen: false,
        encoding: 'utf8'
      });

      duplex.on('data', (chunk) => {
        assert.strictEqual(chunk, 'hi');

        duplex.on('close', () => {
          wss.close(done);
        });
      });
    });

    wss.on('connection', (ws) => {
      ws.send(Buffer.from('hi'));
      ws.close();
    });
  });

  describe('The returned stream', () => {
    it('buffers writes if `readyState` is `CONNECTING`', (done) => {
      const chunk = randomBytes(1024);
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        assert.strictEqual(ws.readyState, WebSocket.CONNECTING);

        const duplex = createWebSocketStream(ws);

        duplex.write(chunk);
      });

      wss.on('connection', (ws) => {
        ws.on('message', (message, isBinary) => {
          ws.on('close', (code, reason) => {
            assert.deepStrictEqual(message, chunk);
            assert.ok(isBinary);
            assert.strictEqual(code, 1005);
            assert.strictEqual(reason, EMPTY_BUFFER);
            wss.close(done);
          });
        });

        ws.close();
      });
    });

    it('errors if a write occurs when `readyState` is `CLOSING`', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        const duplex = createWebSocketStream(ws);

        duplex.on('error', (err) => {
          assert.ok(duplex.destroyed);
          assert.ok(err instanceof Error);
          assert.strictEqual(
            err.message,
            'WebSocket is not open: readyState 2 (CLOSING)'
          );

          duplex.on('close', () => {
            wss.close(done);
          });
        });

        ws.on('open', () => {
          ws._receiver.on('conclude', () => {
            duplex.write('hi');
          });
        });
      });

      wss.on('connection', (ws) => {
        ws.close();
      });
    });

    it('errors if a write occurs when `readyState` is `CLOSED`', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        const duplex = createWebSocketStream(ws);

        duplex.on('error', (err) => {
          assert.ok(duplex.destroyed);
          assert.ok(err instanceof Error);
          assert.strictEqual(
            err.message,
            'WebSocket is not open: readyState 3 (CLOSED)'
          );

          duplex.on('close', () => {
            wss.close(done);
          });
        });

        ws.on('close', () => {
          duplex.write('hi');
        });
      });

      wss.on('connection', (ws) => {
        ws.close();
      });
    });

    it('does not error if `_final()` is called while connecting', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        assert.strictEqual(ws.readyState, WebSocket.CONNECTING);

        const duplex = createWebSocketStream(ws);

        duplex.on('close', () => {
          wss.close(done);
        });

        duplex.resume();
        duplex.end();
      });
    });

    it('makes `_final()` a noop if no socket is assigned', (done) => {
      const server = createServer();

      server.on('upgrade', (request, socket) => {
        socket.on('end', socket.end);

        const headers = [
          'HTTP/1.1 101 Switching Protocols',
          'Upgrade: websocket',
          'Connection: Upgrade',
          'Sec-WebSocket-Accept: foo'
        ];

        socket.write(headers.concat('\r\n').join('\r\n'));
      });

      server.listen(() => {
        const called = [];
        const ws = new WebSocket(`ws://localhost:${server.address().port}`);
        const duplex = WebSocket.createWebSocketStream(ws);
        const final = duplex._final;

        duplex._final = (callback) => {
          called.push('final');
          assert.strictEqual(ws.readyState, WebSocket.CLOSING);
          assert.strictEqual(ws._socket, null);

          final(callback);
        };

        duplex.on('error', (err) => {
          called.push('error');
          assert.ok(err instanceof Error);
          assert.strictEqual(
            err.message,
            'Invalid Sec-WebSocket-Accept header'
          );
        });

        duplex.on('finish', () => {
          called.push('finish');
        });

        duplex.on('close', () => {
          assert.deepStrictEqual(called, ['final', 'error']);
          server.close(done);
        });

        ws.on('upgrade', () => {
          process.nextTick(() => {
            duplex.end();
          });
        });
      });
    });

    it('reemits errors', (done) => {
      let duplexCloseEventEmitted = false;
      let serverClientCloseEventEmitted = false;

      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        const duplex = createWebSocketStream(ws);

        duplex.on('error', (err) => {
          assert.ok(err instanceof RangeError);
          assert.strictEqual(err.code, 'WS_ERR_INVALID_OPCODE');
          assert.strictEqual(
            err.message,
            'Invalid WebSocket frame: invalid opcode 5'
          );

          duplex.on('close', () => {
            duplexCloseEventEmitted = true;
            if (serverClientCloseEventEmitted) wss.close(done);
          });
        });
      });

      wss.on('connection', (ws) => {
        ws._socket.write(Buffer.from([0x85, 0x00]));
        ws.on('close', (code, reason) => {
          assert.strictEqual(code, 1002);
          assert.deepStrictEqual(reason, EMPTY_BUFFER);

          serverClientCloseEventEmitted = true;
          if (duplexCloseEventEmitted) wss.close(done);
        });
      });
    });

    it('does not swallow errors that may occur while destroying', (done) => {
      const frame = Buffer.concat(
        Sender.frame(Buffer.from([0x22, 0xfa, 0xec, 0x78]), {
          fin: true,
          rsv1: true,
          opcode: 0x02,
          mask: false,
          readOnly: false
        })
      );

      const wss = new WebSocket.Server(
        {
          perMessageDeflate: true,
          port: 0
        },
        () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
          const duplex = createWebSocketStream(ws);

          duplex.on('error', (err) => {
            assert.ok(err instanceof Error);
            assert.strictEqual(err.code, 'Z_DATA_ERROR');
            assert.strictEqual(err.errno, -3);

            duplex.on('close', () => {
              wss.close(done);
            });
          });

          let bytesRead = 0;

          ws.on('open', () => {
            ws._socket.on('data', (chunk) => {
              bytesRead += chunk.length;
              if (bytesRead === frame.length) duplex.destroy();
            });
          });
        }
      );

      wss.on('connection', (ws) => {
        ws._socket.write(frame);
      });
    });

    it("does not suppress the throwing behavior of 'error' events", (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        createWebSocketStream(ws);
      });

      wss.on('connection', (ws) => {
        ws._socket.write(Buffer.from([0x85, 0x00]));
      });

      assert.strictEqual(
        process.listenerCount('uncaughtException'),
        EventEmitter.usingDomains ? 2 : 1
      );

      const listener = process.listeners('uncaughtException').pop();

      process.removeListener('uncaughtException', listener);
      process.once('uncaughtException', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(
          err.message,
          'Invalid WebSocket frame: invalid opcode 5'
        );

        process.on('uncaughtException', listener);
        wss.close(done);
      });
    });

    it("is destroyed after 'end' and 'finish' are emitted (1/2)", (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const events = [];
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        const duplex = createWebSocketStream(ws);

        duplex.on('end', () => {
          events.push('end');
          assert.ok(duplex.destroyed);
        });

        duplex.on('close', () => {
          assert.deepStrictEqual(events, ['finish', 'end']);
          wss.close(done);
        });

        duplex.on('finish', () => {
          events.push('finish');
          assert.ok(!duplex.destroyed);
          assert.ok(duplex.readable);

          duplex.resume();
        });

        ws.on('close', () => {
          duplex.end();
        });
      });

      wss.on('connection', (ws) => {
        ws.send('foo');
        ws.close();
      });
    });

    it("is destroyed after 'end' and 'finish' are emitted (2/2)", (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const events = [];
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        const duplex = createWebSocketStream(ws);

        duplex.on('end', () => {
          events.push('end');
          assert.ok(!duplex.destroyed);
          assert.ok(duplex.writable);

          duplex.end();
        });

        duplex.on('close', () => {
          assert.deepStrictEqual(events, ['end', 'finish']);
          wss.close(done);
        });

        duplex.on('finish', () => {
          events.push('finish');
        });

        duplex.resume();
      });

      wss.on('connection', (ws) => {
        ws.close();
      });
    });

    it('handles backpressure (1/3)', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        // eslint-disable-next-line no-unused-vars
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
      });

      wss.on('connection', (ws) => {
        const duplex = createWebSocketStream(ws);

        duplex.resume();

        duplex.on('drain', () => {
          duplex.on('close', () => {
            wss.close(done);
          });

          duplex.end();
        });

        const chunk = randomBytes(1024);
        let ret;

        do {
          ret = duplex.write(chunk);
        } while (ret !== false);
      });
    });

    it('handles backpressure (2/3)', (done) => {
      const wss = new WebSocket.Server(
        { port: 0, perMessageDeflate: true },
        () => {
          const called = [];
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
          const duplex = createWebSocketStream(ws);
          const read = duplex._read;

          duplex._read = () => {
            duplex._read = read;
            called.push('read');
            assert.ok(ws._receiver._writableState.needDrain);
            read();
            assert.ok(ws._socket.isPaused());
          };

          ws.on('open', () => {
            ws._socket.on('pause', () => {
              duplex.resume();
            });

            ws._receiver.on('drain', () => {
              called.push('drain');
              assert.ok(!ws._socket.isPaused());
              duplex.end();
            });

            const opts = {
              fin: true,
              opcode: 0x02,
              mask: false,
              readOnly: false
            };

            const list = [
              ...Sender.frame(randomBytes(highWaterMark), {
                rsv1: false,
                ...opts
              }),
              ...Sender.frame(Buffer.alloc(1), { rsv1: true, ...opts })
            ];

            // This hack is used because there is no guarantee that more than
            // `highWaterMark` bytes will be sent as a single TCP packet.
            ws._socket.push(Buffer.concat(list));
          });

          duplex.on('close', () => {
            assert.deepStrictEqual(called, ['read', 'drain']);
            wss.close(done);
          });
        }
      );
    });

    it('handles backpressure (3/3)', (done) => {
      const wss = new WebSocket.Server(
        { port: 0, perMessageDeflate: true },
        () => {
          const called = [];
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
          const duplex = createWebSocketStream(ws);
          const read = duplex._read;

          duplex._read = () => {
            called.push('read');
            assert.ok(!ws._receiver._writableState.needDrain);
            read();
            assert.ok(!ws._socket.isPaused());
            duplex.end();
          };

          ws.on('open', () => {
            ws._receiver.on('drain', () => {
              called.push('drain');
              assert.ok(ws._socket.isPaused());
              duplex.resume();
            });

            const opts = {
              fin: true,
              opcode: 0x02,
              mask: false,
              readOnly: false
            };

            const list = [
              ...Sender.frame(randomBytes(highWaterMark), {
                rsv1: false,
                ...opts
              }),
              ...Sender.frame(Buffer.alloc(1), { rsv1: true, ...opts })
            ];

            ws._socket.push(Buffer.concat(list));
          });

          duplex.on('close', () => {
            assert.deepStrictEqual(called, ['drain', 'read']);
            wss.close(done);
          });
        }
      );
    });

    it('can be destroyed (1/2)', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const error = new Error('Oops');
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        const duplex = createWebSocketStream(ws);

        duplex.on('error', (err) => {
          assert.strictEqual(err, error);

          duplex.on('close', () => {
            wss.close(done);
          });
        });

        ws.on('open', () => {
          duplex.destroy(error);
        });
      });
    });

    it('can be destroyed (2/2)', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        const duplex = createWebSocketStream(ws);

        duplex.on('close', () => {
          wss.close(done);
        });

        ws.on('open', () => {
          duplex.destroy();
        });
      });
    });

    it('converts text messages to strings in readable object mode', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const events = [];
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        const duplex = createWebSocketStream(ws, { readableObjectMode: true });

        duplex.on('data', (data) => {
          events.push('data');
          assert.strictEqual(data, 'foo');
        });

        duplex.on('end', () => {
          events.push('end');
          duplex.end();
        });

        duplex.on('close', () => {
          assert.deepStrictEqual(events, ['data', 'end']);
          wss.close(done);
        });
      });

      wss.on('connection', (ws) => {
        ws.send('foo');
        ws.close();
      });
    });

    it('resumes the socket if `readyState` is `CLOSING`', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        const duplex = createWebSocketStream(ws);

        ws.on('message', () => {
          assert.ok(ws._socket.isPaused());

          duplex.on('close', () => {
            wss.close(done);
          });

          duplex.end();

          process.nextTick(() => {
            assert.strictEqual(ws.readyState, WebSocket.CLOSING);
            duplex.resume();
          });
        });
      });

      wss.on('connection', (ws) => {
        ws.send(randomBytes(highWaterMark));
      });
    });
  });
});
```

## File: `test/duplex-pair.js`
```javascript
//
// This code was copied from
// https://github.com/nodejs/node/blob/c506660f3267/test/common/duplexpair.js
//
// Copyright Node.js contributors. All rights reserved.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to
// deal in the Software without restriction, including without limitation the
// rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
// sell copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
// FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
// IN THE SOFTWARE.
//
'use strict';

const assert = require('assert');
const { Duplex } = require('stream');

const kCallback = Symbol('Callback');
const kOtherSide = Symbol('Other');

class DuplexSocket extends Duplex {
  constructor() {
    super();
    this[kCallback] = null;
    this[kOtherSide] = null;
  }

  _read() {
    const callback = this[kCallback];
    if (callback) {
      this[kCallback] = null;
      callback();
    }
  }

  _write(chunk, encoding, callback) {
    assert.notStrictEqual(this[kOtherSide], null);
    assert.strictEqual(this[kOtherSide][kCallback], null);
    if (chunk.length === 0) {
      process.nextTick(callback);
    } else {
      this[kOtherSide].push(chunk);
      this[kOtherSide][kCallback] = callback;
    }
  }

  _final(callback) {
    this[kOtherSide].on('end', callback);
    this[kOtherSide].push(null);
  }
}

function makeDuplexPair() {
  const clientSide = new DuplexSocket();
  const serverSide = new DuplexSocket();
  clientSide[kOtherSide] = serverSide;
  serverSide[kOtherSide] = clientSide;
  return { clientSide, serverSide };
}

module.exports = makeDuplexPair;
```

## File: `test/event-target.test.js`
```javascript
'use strict';

const assert = require('assert');

const {
  CloseEvent,
  ErrorEvent,
  Event,
  MessageEvent
} = require('../lib/event-target');

describe('Event', () => {
  describe('#ctor', () => {
    it('takes a `type` argument', () => {
      const event = new Event('foo');

      assert.strictEqual(event.type, 'foo');
    });
  });

  describe('Properties', () => {
    describe('`target`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          Event.prototype,
          'target'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });

      it('defaults to `null`', () => {
        const event = new Event('foo');

        assert.strictEqual(event.target, null);
      });
    });

    describe('`type`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          Event.prototype,
          'type'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });
    });
  });
});

describe('CloseEvent', () => {
  it('inherits from `Event`', () => {
    assert.ok(CloseEvent.prototype instanceof Event);
  });

  describe('#ctor', () => {
    it('takes a `type` argument', () => {
      const event = new CloseEvent('foo');

      assert.strictEqual(event.type, 'foo');
    });

    it('takes an optional `options` argument', () => {
      const event = new CloseEvent('close', {
        code: 1000,
        reason: 'foo',
        wasClean: true
      });

      assert.strictEqual(event.type, 'close');
      assert.strictEqual(event.code, 1000);
      assert.strictEqual(event.reason, 'foo');
      assert.strictEqual(event.wasClean, true);
    });
  });

  describe('Properties', () => {
    describe('`code`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          CloseEvent.prototype,
          'code'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });

      it('defaults to 0', () => {
        const event = new CloseEvent('close');

        assert.strictEqual(event.code, 0);
      });
    });

    describe('`reason`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          CloseEvent.prototype,
          'reason'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });

      it('defaults to an empty string', () => {
        const event = new CloseEvent('close');

        assert.strictEqual(event.reason, '');
      });
    });

    describe('`wasClean`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          CloseEvent.prototype,
          'wasClean'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });

      it('defaults to false', () => {
        const event = new CloseEvent('close');

        assert.strictEqual(event.wasClean, false);
      });
    });
  });
});

describe('ErrorEvent', () => {
  it('inherits from `Event`', () => {
    assert.ok(ErrorEvent.prototype instanceof Event);
  });

  describe('#ctor', () => {
    it('takes a `type` argument', () => {
      const event = new ErrorEvent('foo');

      assert.strictEqual(event.type, 'foo');
    });

    it('takes an optional `options` argument', () => {
      const error = new Error('Oops');
      const event = new ErrorEvent('error', { error, message: error.message });

      assert.strictEqual(event.type, 'error');
      assert.strictEqual(event.error, error);
      assert.strictEqual(event.message, error.message);
    });
  });

  describe('Properties', () => {
    describe('`error`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          ErrorEvent.prototype,
          'error'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });

      it('defaults to `null`', () => {
        const event = new ErrorEvent('error');

        assert.strictEqual(event.error, null);
      });
    });

    describe('`message`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          ErrorEvent.prototype,
          'message'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });

      it('defaults to an empty string', () => {
        const event = new ErrorEvent('error');

        assert.strictEqual(event.message, '');
      });
    });
  });
});

describe('MessageEvent', () => {
  it('inherits from `Event`', () => {
    assert.ok(MessageEvent.prototype instanceof Event);
  });

  describe('#ctor', () => {
    it('takes a `type` argument', () => {
      const event = new MessageEvent('foo');

      assert.strictEqual(event.type, 'foo');
    });

    it('takes an optional `options` argument', () => {
      const event = new MessageEvent('message', { data: 'bar' });

      assert.strictEqual(event.type, 'message');
      assert.strictEqual(event.data, 'bar');
    });
  });

  describe('Properties', () => {
    describe('`data`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          MessageEvent.prototype,
          'data'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });

      it('defaults to `null`', () => {
        const event = new MessageEvent('message');

        assert.strictEqual(event.data, null);
      });
    });
  });
});
```

## File: `test/extension.test.js`
```javascript
'use strict';

const assert = require('assert');

const { format, parse } = require('../lib/extension');

describe('extension', () => {
  describe('parse', () => {
    it('parses a single extension', () => {
      assert.deepStrictEqual(parse('foo'), {
        foo: [{ __proto__: null }],
        __proto__: null
      });
    });

    it('parses params', () => {
      assert.deepStrictEqual(parse('foo;bar;baz=1;bar=2'), {
        foo: [{ bar: [true, '2'], baz: ['1'], __proto__: null }],
        __proto__: null
      });
    });

    it('parses multiple extensions', () => {
      assert.deepStrictEqual(parse('foo,bar;baz,foo;baz'), {
        foo: [{ __proto__: null }, { baz: [true], __proto__: null }],
        bar: [{ baz: [true], __proto__: null }],
        __proto__: null
      });
    });

    it('parses quoted params', () => {
      assert.deepStrictEqual(parse('foo;bar="hi"'), {
        foo: [{ bar: ['hi'], __proto__: null }],
        __proto__: null
      });
      assert.deepStrictEqual(parse('foo;bar="\\0"'), {
        foo: [{ bar: ['0'], __proto__: null }],
        __proto__: null
      });
      assert.deepStrictEqual(parse('foo;bar="b\\a\\z"'), {
        foo: [{ bar: ['baz'], __proto__: null }],
        __proto__: null
      });
      assert.deepStrictEqual(parse('foo;bar="b\\az";bar'), {
        foo: [{ bar: ['baz', true], __proto__: null }],
        __proto__: null
      });
      assert.throws(
        () => parse('foo;bar="baz"qux'),
        /^SyntaxError: Unexpected character at index 13$/
      );
      assert.throws(
        () => parse('foo;bar="baz" qux'),
        /^SyntaxError: Unexpected character at index 14$/
      );
    });

    it('works with names that match `Object.prototype` property names', () => {
      assert.deepStrictEqual(parse('hasOwnProperty, toString'), {
        hasOwnProperty: [{ __proto__: null }],
        toString: [{ __proto__: null }],
        __proto__: null
      });
      assert.deepStrictEqual(parse('foo;constructor'), {
        foo: [{ constructor: [true], __proto__: null }],
        __proto__: null
      });
    });

    it('ignores the optional white spaces', () => {
      const header = 'foo; bar\t; \tbaz=1\t ;  bar="1"\t\t, \tqux\t ;norf';

      assert.deepStrictEqual(parse(header), {
        foo: [{ bar: [true, '1'], baz: ['1'], __proto__: null }],
        qux: [{ norf: [true], __proto__: null }],
        __proto__: null
      });
    });

    it('throws an error if a name is empty', () => {
      [
        [',', 0],
        ['foo,,', 4],
        ['foo,  ,', 6],
        ['foo;=', 4],
        ['foo; =', 5],
        ['foo;;', 4],
        ['foo; ;', 5],
        ['foo;bar=,', 8],
        ['foo;bar=""', 9]
      ].forEach((element) => {
        assert.throws(
          () => parse(element[0]),
          new RegExp(
            `^SyntaxError: Unexpected character at index ${element[1]}$`
          )
        );
      });
    });

    it('throws an error if a white space is misplaced', () => {
      [
        [' foo', 0],
        ['f oo', 2],
        ['foo;ba r', 7],
        ['foo;bar =', 8],
        ['foo;bar= ', 8],
        ['foo;bar=ba z', 11]
      ].forEach((element) => {
        assert.throws(
          () => parse(element[0]),
          new RegExp(
            `^SyntaxError: Unexpected character at index ${element[1]}$`
          )
        );
      });
    });

    it('throws an error if a token contains invalid characters', () => {
      [
        ['f@o', 1],
        ['f\\oo', 1],
        ['"foo"', 0],
        ['f"oo"', 1],
        ['foo;b@r', 5],
        ['foo;b\\ar', 5],
        ['foo;"bar"', 4],
        ['foo;b"ar"', 5],
        ['foo;bar=b@z', 9],
        ['foo;bar=b\\az ', 9],
        ['foo;bar="b@z"', 10],
        ['foo;bar="baz;"', 12],
        ['foo;bar=b"az"', 9],
        ['foo;bar="\\\\"', 10]
      ].forEach((element) => {
        assert.throws(
          () => parse(element[0]),
          new RegExp(
            `^SyntaxError: Unexpected character at index ${element[1]}$`
          )
        );
      });
    });

    it('throws an error if the header value ends prematurely', () => {
      [
        '',
        'foo ',
        'foo\t',
        'foo, ',
        'foo;',
        'foo;bar ',
        'foo;bar,',
        'foo;bar; ',
        'foo;bar=',
        'foo;bar="baz',
        'foo;bar="1\\',
        'foo;bar="baz" '
      ].forEach((header) => {
        assert.throws(
          () => parse(header),
          /^SyntaxError: Unexpected end of input$/
        );
      });
    });
  });

  describe('format', () => {
    it('formats a single extension', () => {
      const extensions = format({ foo: {} });

      assert.strictEqual(extensions, 'foo');
    });

    it('formats params', () => {
      const extensions = format({ foo: { bar: [true, 2], baz: 1 } });

      assert.strictEqual(extensions, 'foo; bar; bar=2; baz=1');
    });

    it('formats multiple extensions', () => {
      const extensions = format({
        foo: [{}, { baz: true }],
        bar: { baz: true }
      });

      assert.strictEqual(extensions, 'foo, foo; baz, bar; baz');
    });
  });
});
```

## File: `test/limiter.test.js`
```javascript
'use strict';

const assert = require('assert');

const Limiter = require('../lib/limiter');

describe('Limiter', () => {
  describe('#ctor', () => {
    it('takes a `concurrency` argument', () => {
      const limiter = new Limiter(0);

      assert.strictEqual(limiter.concurrency, Infinity);
    });
  });

  describe('#kRun', () => {
    it('limits the number of jobs allowed to run concurrently', (done) => {
      const limiter = new Limiter(1);

      limiter.add((callback) => {
        setImmediate(() => {
          callback();

          assert.strictEqual(limiter.jobs.length, 0);
          assert.strictEqual(limiter.pending, 1);
        });
      });

      limiter.add((callback) => {
        setImmediate(() => {
          callback();

          assert.strictEqual(limiter.pending, 0);
          done();
        });
      });

      assert.strictEqual(limiter.jobs.length, 1);
    });
  });
});
```

## File: `test/permessage-deflate.test.js`
```javascript
'use strict';

const assert = require('assert');

const PerMessageDeflate = require('../lib/permessage-deflate');
const extension = require('../lib/extension');

describe('PerMessageDeflate', () => {
  describe('#offer', () => {
    it('creates an offer', () => {
      const perMessageDeflate = new PerMessageDeflate();

      assert.deepStrictEqual(perMessageDeflate.offer(), {
        client_max_window_bits: true
      });
    });

    it('uses the configuration options', () => {
      const perMessageDeflate = new PerMessageDeflate({
        serverNoContextTakeover: true,
        clientNoContextTakeover: true,
        serverMaxWindowBits: 10,
        clientMaxWindowBits: 11
      });

      assert.deepStrictEqual(perMessageDeflate.offer(), {
        server_no_context_takeover: true,
        client_no_context_takeover: true,
        server_max_window_bits: 10,
        client_max_window_bits: 11
      });
    });
  });

  describe('#accept', () => {
    it('throws an error if a parameter has multiple values', () => {
      const perMessageDeflate = new PerMessageDeflate();
      const extensions = extension.parse(
        'permessage-deflate; server_no_context_takeover; server_no_context_takeover'
      );

      assert.throws(
        () => perMessageDeflate.accept(extensions['permessage-deflate']),
        /^Error: Parameter "server_no_context_takeover" must have only a single value$/
      );
    });

    it('throws an error if a parameter has an invalid name', () => {
      const perMessageDeflate = new PerMessageDeflate();
      const extensions = extension.parse('permessage-deflate;foo');

      assert.throws(
        () => perMessageDeflate.accept(extensions['permessage-deflate']),
        /^Error: Unknown parameter "foo"$/
      );
    });

    it('throws an error if client_no_context_takeover has a value', () => {
      const perMessageDeflate = new PerMessageDeflate();
      const extensions = extension.parse(
        'permessage-deflate; client_no_context_takeover=10'
      );

      assert.throws(
        () => perMessageDeflate.accept(extensions['permessage-deflate']),
        /^TypeError: Invalid value for parameter "client_no_context_takeover": 10$/
      );
    });

    it('throws an error if server_no_context_takeover has a value', () => {
      const perMessageDeflate = new PerMessageDeflate();
      const extensions = extension.parse(
        'permessage-deflate; server_no_context_takeover=10'
      );

      assert.throws(
        () => perMessageDeflate.accept(extensions['permessage-deflate']),
        /^TypeError: Invalid value for parameter "server_no_context_takeover": 10$/
      );
    });

    it('throws an error if server_max_window_bits has an invalid value', () => {
      const perMessageDeflate = new PerMessageDeflate();

      let extensions = extension.parse(
        'permessage-deflate; server_max_window_bits=7'
      );
      assert.throws(
        () => perMessageDeflate.accept(extensions['permessage-deflate']),
        /^TypeError: Invalid value for parameter "server_max_window_bits": 7$/
      );

      extensions = extension.parse(
        'permessage-deflate; server_max_window_bits'
      );
      assert.throws(
        () => perMessageDeflate.accept(extensions['permessage-deflate']),
        /^TypeError: Invalid value for parameter "server_max_window_bits": true$/
      );
    });

    describe('As server', () => {
      it('accepts an offer with no parameters', () => {
        const perMessageDeflate = new PerMessageDeflate({ isServer: true });

        assert.deepStrictEqual(perMessageDeflate.accept([{}]), {});
      });

      it('accepts an offer with parameters', () => {
        const perMessageDeflate = new PerMessageDeflate({ isServer: true });
        const extensions = extension.parse(
          'permessage-deflate; server_no_context_takeover; ' +
            'client_no_context_takeover; server_max_window_bits=10; ' +
            'client_max_window_bits=11'
        );

        assert.deepStrictEqual(
          perMessageDeflate.accept(extensions['permessage-deflate']),
          {
            server_no_context_takeover: true,
            client_no_context_takeover: true,
            server_max_window_bits: 10,
            client_max_window_bits: 11,
            __proto__: null
          }
        );
      });

      it('prefers the configuration options', () => {
        const perMessageDeflate = new PerMessageDeflate({
          serverNoContextTakeover: true,
          clientNoContextTakeover: true,
          serverMaxWindowBits: 12,
          clientMaxWindowBits: 11,
          isServer: true
        });
        const extensions = extension.parse(
          'permessage-deflate; server_max_window_bits=14; client_max_window_bits=13'
        );

        assert.deepStrictEqual(
          perMessageDeflate.accept(extensions['permessage-deflate']),
          {
            server_no_context_takeover: true,
            client_no_context_takeover: true,
            server_max_window_bits: 12,
            client_max_window_bits: 11,
            __proto__: null
          }
        );
      });

      it('accepts the first supported offer', () => {
        const perMessageDeflate = new PerMessageDeflate({
          isServer: true,
          serverMaxWindowBits: 11
        });
        const extensions = extension.parse(
          'permessage-deflate; server_max_window_bits=10, permessage-deflate'
        );

        assert.deepStrictEqual(
          perMessageDeflate.accept(extensions['permessage-deflate']),
          {
            server_max_window_bits: 11,
            __proto__: null
          }
        );
      });

      it('throws an error if server_no_context_takeover is unsupported', () => {
        const perMessageDeflate = new PerMessageDeflate({
          isServer: true,
          serverNoContextTakeover: false
        });
        const extensions = extension.parse(
          'permessage-deflate; server_no_context_takeover'
        );

        assert.throws(
          () => perMessageDeflate.accept(extensions['permessage-deflate']),
          /^Error: None of the extension offers can be accepted$/
        );
      });

      it('throws an error if server_max_window_bits is unsupported', () => {
        const perMessageDeflate = new PerMessageDeflate({
          isServer: true,
          serverMaxWindowBits: false
        });
        const extensions = extension.parse(
          'permessage-deflate; server_max_window_bits=10'
        );

        assert.throws(
          () => perMessageDeflate.accept(extensions['permessage-deflate']),
          /^Error: None of the extension offers can be accepted$/
        );
      });

      it('throws an error if server_max_window_bits is less than configuration', () => {
        const perMessageDeflate = new PerMessageDeflate({
          isServer: true,
          serverMaxWindowBits: 11
        });
        const extensions = extension.parse(
          'permessage-deflate; server_max_window_bits=10'
        );

        assert.throws(
          () => perMessageDeflate.accept(extensions['permessage-deflate']),
          /^Error: None of the extension offers can be accepted$/
        );
      });

      it('throws an error if client_max_window_bits is unsupported on client', () => {
        const perMessageDeflate = new PerMessageDeflate({
          isServer: true,
          clientMaxWindowBits: 10
        });
        const extensions = extension.parse('permessage-deflate');

        assert.throws(
          () => perMessageDeflate.accept(extensions['permessage-deflate']),
          /^Error: None of the extension offers can be accepted$/
        );
      });

      it('throws an error if client_max_window_bits has an invalid value', () => {
        const perMessageDeflate = new PerMessageDeflate({ isServer: true });

        const extensions = extension.parse(
          'permessage-deflate; client_max_window_bits=16'
        );
        assert.throws(
          () => perMessageDeflate.accept(extensions['permessage-deflate']),
          /^TypeError: Invalid value for parameter "client_max_window_bits": 16$/
        );
      });
    });

    describe('As client', () => {
      it('accepts a response with no parameters', () => {
        const perMessageDeflate = new PerMessageDeflate({});

        assert.deepStrictEqual(perMessageDeflate.accept([{}]), {});
      });

      it('accepts a response with parameters', () => {
        const perMessageDeflate = new PerMessageDeflate({});
        const extensions = extension.parse(
          'permessage-deflate; server_no_context_takeover; ' +
            'client_no_context_takeover; server_max_window_bits=10; ' +
            'client_max_window_bits=11'
        );

        assert.deepStrictEqual(
          perMessageDeflate.accept(extensions['permessage-deflate']),
          {
            server_no_context_takeover: true,
            client_no_context_takeover: true,
            server_max_window_bits: 10,
            client_max_window_bits: 11,
            __proto__: null
          }
        );
      });

      it('throws an error if client_no_context_takeover is unsupported', () => {
        const perMessageDeflate = new PerMessageDeflate({
          clientNoContextTakeover: false
        });
        const extensions = extension.parse(
          'permessage-deflate; client_no_context_takeover'
        );

        assert.throws(
          () => perMessageDeflate.accept(extensions['permessage-deflate']),
          /^Error: Unexpected parameter "client_no_context_takeover"$/
        );
      });

      it('throws an error if client_max_window_bits is unsupported', () => {
        const perMessageDeflate = new PerMessageDeflate({
          clientMaxWindowBits: false
        });
        const extensions = extension.parse(
          'permessage-deflate; client_max_window_bits=10'
        );

        assert.throws(
          () => perMessageDeflate.accept(extensions['permessage-deflate']),
          /^Error: Unexpected or invalid parameter "client_max_window_bits"$/
        );
      });

      it('throws an error if client_max_window_bits is greater than configuration', () => {
        const perMessageDeflate = new PerMessageDeflate({
          clientMaxWindowBits: 10
        });
        const extensions = extension.parse(
          'permessage-deflate; client_max_window_bits=11'
        );

        assert.throws(
          () => perMessageDeflate.accept(extensions['permessage-deflate']),
          /^Error: Unexpected or invalid parameter "client_max_window_bits"$/
        );
      });

      it('throws an error if client_max_window_bits has an invalid value', () => {
        const perMessageDeflate = new PerMessageDeflate();

        let extensions = extension.parse(
          'permessage-deflate; client_max_window_bits=16'
        );
        assert.throws(
          () => perMessageDeflate.accept(extensions['permessage-deflate']),
          /^TypeError: Invalid value for parameter "client_max_window_bits": 16$/
        );

        extensions = extension.parse(
          'permessage-deflate; client_max_window_bits'
        );
        assert.throws(
          () => perMessageDeflate.accept(extensions['permessage-deflate']),
          /^TypeError: Invalid value for parameter "client_max_window_bits": true$/
        );
      });

      it('uses the config value if client_max_window_bits is not specified', () => {
        const perMessageDeflate = new PerMessageDeflate({
          clientMaxWindowBits: 10
        });

        assert.deepStrictEqual(perMessageDeflate.accept([{}]), {
          client_max_window_bits: 10
        });
      });
    });
  });

  describe('#compress and #decompress', () => {
    it('works with unfragmented messages', (done) => {
      const perMessageDeflate = new PerMessageDeflate();
      const buf = Buffer.from([1, 2, 3]);

      perMessageDeflate.accept([{}]);
      perMessageDeflate.compress(buf, true, (err, data) => {
        if (err) return done(err);

        perMessageDeflate.decompress(data, true, (err, data) => {
          if (err) return done(err);

          assert.ok(data.equals(buf));
          done();
        });
      });
    });

    it('works with fragmented messages', (done) => {
      const perMessageDeflate = new PerMessageDeflate();
      const buf = Buffer.from([1, 2, 3, 4]);

      perMessageDeflate.accept([{}]);

      perMessageDeflate.compress(buf.slice(0, 2), false, (err, compressed1) => {
        if (err) return done(err);

        perMessageDeflate.compress(buf.slice(2), true, (err, compressed2) => {
          if (err) return done(err);

          perMessageDeflate.decompress(compressed1, false, (err, data1) => {
            if (err) return done(err);

            perMessageDeflate.decompress(compressed2, true, (err, data2) => {
              if (err) return done(err);

              assert.ok(Buffer.concat([data1, data2]).equals(buf));
              done();
            });
          });
        });
      });
    });

    it('works with the negotiated parameters', (done) => {
      const perMessageDeflate = new PerMessageDeflate({
        zlibDeflateOptions: {
          memLevel: 5,
          level: 9
        }
      });
      const extensions = extension.parse(
        'permessage-deflate; server_no_context_takeover; ' +
          'client_no_context_takeover; server_max_window_bits=10; ' +
          'client_max_window_bits=11'
      );
      const buf = Buffer.from("Some compressible data, it's compressible.");

      perMessageDeflate.accept(extensions['permessage-deflate']);

      perMessageDeflate.compress(buf, true, (err, data) => {
        if (err) return done(err);

        perMessageDeflate.decompress(data, true, (err, data) => {
          if (err) return done(err);

          assert.ok(data.equals(buf));
          done();
        });
      });
    });

    it('honors the `level` option', (done) => {
      const lev0 = new PerMessageDeflate({
        zlibDeflateOptions: { level: 0 }
      });
      const lev9 = new PerMessageDeflate({
        zlibDeflateOptions: { level: 9 }
      });
      const extensionStr =
        'permessage-deflate; server_no_context_takeover; ' +
        'client_no_context_takeover; server_max_window_bits=10; ' +
        'client_max_window_bits=11';
      const buf = Buffer.from("Some compressible data, it's compressible.");

      lev0.accept(extension.parse(extensionStr)['permessage-deflate']);
      lev9.accept(extension.parse(extensionStr)['permessage-deflate']);

      lev0.compress(buf, true, (err, compressed1) => {
        if (err) return done(err);

        lev0.decompress(compressed1, true, (err, decompressed1) => {
          if (err) return done(err);

          lev9.compress(buf, true, (err, compressed2) => {
            if (err) return done(err);

            lev9.decompress(compressed2, true, (err, decompressed2) => {
              if (err) return done(err);

              // Level 0 compression actually adds a few bytes due to headers.
              assert.ok(compressed1.length > buf.length);
              // Level 9 should not, of course.
              assert.ok(compressed2.length < buf.length);
              // Ensure they both decompress back properly.
              assert.ok(decompressed1.equals(buf));
              assert.ok(decompressed2.equals(buf));
              done();
            });
          });
        });
      });
    });

    it('honors the `zlib{Deflate,Inflate}Options` option', (done) => {
      const lev0 = new PerMessageDeflate({
        zlibDeflateOptions: {
          level: 0,
          chunkSize: 256
        },
        zlibInflateOptions: {
          chunkSize: 2048
        }
      });
      const lev9 = new PerMessageDeflate({
        zlibDeflateOptions: {
          level: 9,
          chunkSize: 128
        },
        zlibInflateOptions: {
          chunkSize: 1024
        }
      });

      // Note no context takeover so we can get a hold of the raw streams after
      // we do the dance.
      const extensionStr =
        'permessage-deflate; server_max_window_bits=10; ' +
        'client_max_window_bits=11';
      const buf = Buffer.from("Some compressible data, it's compressible.");

      lev0.accept(extension.parse(extensionStr)['permessage-deflate']);
      lev9.accept(extension.parse(extensionStr)['permessage-deflate']);

      lev0.compress(buf, true, (err, compressed1) => {
        if (err) return done(err);

        lev0.decompress(compressed1, true, (err, decompressed1) => {
          if (err) return done(err);

          lev9.compress(buf, true, (err, compressed2) => {
            if (err) return done(err);

            lev9.decompress(compressed2, true, (err, decompressed2) => {
              if (err) return done(err);
              // Level 0 compression actually adds a few bytes due to headers.
              assert.ok(compressed1.length > buf.length);
              // Level 9 should not, of course.
              assert.ok(compressed2.length < buf.length);
              // Ensure they both decompress back properly.
              assert.ok(decompressed1.equals(buf));
              assert.ok(decompressed2.equals(buf));

              // Assert options were set.
              assert.ok(lev0._deflate._level === 0);
              assert.ok(lev9._deflate._level === 9);
              assert.ok(lev0._deflate._chunkSize === 256);
              assert.ok(lev9._deflate._chunkSize === 128);
              assert.ok(lev0._inflate._chunkSize === 2048);
              assert.ok(lev9._inflate._chunkSize === 1024);
              done();
            });
          });
        });
      });
    });

    it("doesn't use contex takeover if not allowed", (done) => {
      const perMessageDeflate = new PerMessageDeflate({ isServer: true });
      const extensions = extension.parse(
        'permessage-deflate;server_no_context_takeover'
      );
      const buf = Buffer.from('foofoo');

      perMessageDeflate.accept(extensions['permessage-deflate']);

      perMessageDeflate.compress(buf, true, (err, compressed1) => {
        if (err) return done(err);

        perMessageDeflate.decompress(compressed1, true, (err, data) => {
          if (err) return done(err);

          assert.ok(data.equals(buf));
          perMessageDeflate.compress(data, true, (err, compressed2) => {
            if (err) return done(err);

            assert.strictEqual(compressed2.length, compressed1.length);
            perMessageDeflate.decompress(compressed2, true, (err, data) => {
              if (err) return done(err);

              assert.ok(data.equals(buf));
              done();
            });
          });
        });
      });
    });

    it('uses contex takeover if allowed', (done) => {
      const perMessageDeflate = new PerMessageDeflate({ isServer: true });
      const extensions = extension.parse('permessage-deflate');
      const buf = Buffer.from('foofoo');

      perMessageDeflate.accept(extensions['permessage-deflate']);

      perMessageDeflate.compress(buf, true, (err, compressed1) => {
        if (err) return done(err);

        perMessageDeflate.decompress(compressed1, true, (err, data) => {
          if (err) return done(err);

          assert.ok(data.equals(buf));
          perMessageDeflate.compress(data, true, (err, compressed2) => {
            if (err) return done(err);

            assert.ok(compressed2.length < compressed1.length);
            perMessageDeflate.decompress(compressed2, true, (err, data) => {
              if (err) return done(err);

              assert.ok(data.equals(buf));
              done();
            });
          });
        });
      });
    });

    it('calls the callback when an error occurs (inflate)', (done) => {
      const perMessageDeflate = new PerMessageDeflate();
      const data = Buffer.from('something invalid');

      perMessageDeflate.accept([{}]);
      perMessageDeflate.decompress(data, true, (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(err.code, 'Z_DATA_ERROR');
        assert.strictEqual(err.errno, -3);
        done();
      });
    });

    it('calls the callback when `maxPayload` is exceeded (1/2)', (done) => {
      const perMessageDeflate = new PerMessageDeflate({
        isServer: false,
        maxPayload: 25
      });
      const buf = Buffer.alloc(50, 'A');

      perMessageDeflate.accept([{}]);
      perMessageDeflate.compress(buf, true, (err, data) => {
        if (err) return done(err);

        perMessageDeflate.decompress(data, true, (err) => {
          assert.ok(err instanceof RangeError);
          assert.strictEqual(err.message, 'Max payload size exceeded');
          done();
        });
      });
    });

    it('calls the callback when `maxPayload` is exceeded (2/2)', (done) => {
      // A copy of the previous test but with a larger input. See
      // https://github.com/websockets/ws/pull/2285.
      const perMessageDeflate = new PerMessageDeflate({
        isServer: false,
        maxPayload: 25
      });
      const buf = Buffer.alloc(1024 * 1024, 'A');

      perMessageDeflate.accept([{}]);
      perMessageDeflate.compress(buf, true, (err, data) => {
        if (err) return done(err);

        perMessageDeflate.decompress(data, true, (err) => {
          assert.ok(err instanceof RangeError);
          assert.strictEqual(err.message, 'Max payload size exceeded');
          done();
        });
      });
    });

    it('calls the callback if the deflate stream is closed prematurely', (done) => {
      const perMessageDeflate = new PerMessageDeflate();
      const buf = Buffer.from('A'.repeat(50));

      perMessageDeflate.accept([{}]);
      perMessageDeflate.compress(buf, true, (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(
          err.message,
          'The deflate stream was closed while data was being processed'
        );
        done();
      });

      process.nextTick(() => perMessageDeflate.cleanup());
    });

    it('recreates the inflate stream if it ends', (done) => {
      const perMessageDeflate = new PerMessageDeflate();
      const extensions = extension.parse(
        'permessage-deflate; client_no_context_takeover; ' +
          'server_no_context_takeover'
      );
      const buf = Buffer.from('33343236313533b7000000', 'hex');
      const expected = Buffer.from('12345678');

      perMessageDeflate.accept(extensions['permessage-deflate']);

      perMessageDeflate.decompress(buf, true, (err, data) => {
        assert.ok(data.equals(expected));

        perMessageDeflate.decompress(buf, true, (err, data) => {
          assert.ok(data.equals(expected));
          done();
        });
      });
    });
  });
});
```

## File: `test/receiver.test.js`
```javascript
'use strict';

const assert = require('assert');
const crypto = require('crypto');
const EventEmitter = require('events');

const PerMessageDeflate = require('../lib/permessage-deflate');
const Receiver = require('../lib/receiver');
const Sender = require('../lib/sender');
const { EMPTY_BUFFER, hasBlob, kStatusCode } = require('../lib/constants');

describe('Receiver', () => {
  it('parses an unmasked text message', (done) => {
    const receiver = new Receiver();

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, Buffer.from('Hello'));
      assert.ok(!isBinary);
      done();
    });

    receiver.write(Buffer.from('810548656c6c6f', 'hex'));
  });

  it('parses a close message', (done) => {
    const receiver = new Receiver();

    receiver.on('conclude', (code, data) => {
      assert.strictEqual(code, 1005);
      assert.strictEqual(data, EMPTY_BUFFER);
      done();
    });

    receiver.write(Buffer.from('8800', 'hex'));
  });

  it('parses a close message spanning multiple writes', (done) => {
    const receiver = new Receiver();

    receiver.on('conclude', (code, data) => {
      assert.strictEqual(code, 1000);
      assert.deepStrictEqual(data, Buffer.from('DONE'));
      done();
    });

    receiver.write(Buffer.from('8806', 'hex'));
    receiver.write(Buffer.from('03e8444F4E45', 'hex'));
  });

  it('parses a masked text message', (done) => {
    const receiver = new Receiver({ isServer: true });

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, Buffer.from('5:::{"name":"echo"}'));
      assert.ok(!isBinary);
      done();
    });

    receiver.write(
      Buffer.from('81933483a86801b992524fa1c60959e68a5216e6cb005ba1d5', 'hex')
    );
  });

  it('parses a masked text message longer than 125 B', (done) => {
    const receiver = new Receiver({ isServer: true });
    const msg = Buffer.from('A'.repeat(200));

    const list = Sender.frame(msg, {
      fin: true,
      rsv1: false,
      opcode: 0x01,
      mask: true,
      readOnly: true
    });

    const frame = Buffer.concat(list);

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, msg);
      assert.ok(!isBinary);
      done();
    });

    receiver.write(frame.slice(0, 2));
    setImmediate(() => receiver.write(frame.slice(2)));
  });

  it('parses a really long masked text message', (done) => {
    const receiver = new Receiver({ isServer: true });
    const msg = Buffer.from('A'.repeat(64 * 1024));

    const list = Sender.frame(msg, {
      fin: true,
      rsv1: false,
      opcode: 0x01,
      mask: true,
      readOnly: true
    });

    const frame = Buffer.concat(list);

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, msg);
      assert.ok(!isBinary);
      done();
    });

    receiver.write(frame);
  });

  it('parses a 300 B fragmented masked text message', (done) => {
    const receiver = new Receiver({ isServer: true });
    const msg = Buffer.from('A'.repeat(300));

    const fragment1 = msg.slice(0, 150);
    const fragment2 = msg.slice(150);

    const options = { rsv1: false, mask: true, readOnly: true };

    const frame1 = Buffer.concat(
      Sender.frame(fragment1, {
        fin: false,
        opcode: 0x01,
        ...options
      })
    );
    const frame2 = Buffer.concat(
      Sender.frame(fragment2, {
        fin: true,
        opcode: 0x00,
        ...options
      })
    );

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, msg);
      assert.ok(!isBinary);
      done();
    });

    receiver.write(frame1);
    receiver.write(frame2);
  });

  it('parses a ping message', (done) => {
    const receiver = new Receiver({ isServer: true });
    const msg = Buffer.from('Hello');

    const list = Sender.frame(msg, {
      fin: true,
      rsv1: false,
      opcode: 0x09,
      mask: true,
      readOnly: true
    });

    const frame = Buffer.concat(list);

    receiver.on('ping', (data) => {
      assert.deepStrictEqual(data, msg);
      done();
    });

    receiver.write(frame);
  });

  it('parses a ping message with no data', (done) => {
    const receiver = new Receiver();

    receiver.on('ping', (data) => {
      assert.strictEqual(data, EMPTY_BUFFER);
      done();
    });

    receiver.write(Buffer.from('8900', 'hex'));
  });

  it('parses a 300 B fragmented masked text message with a ping in the middle (1/2)', (done) => {
    const receiver = new Receiver({ isServer: true });
    const msg = Buffer.from('A'.repeat(300));
    const pingMessage = Buffer.from('Hello');

    const fragment1 = msg.slice(0, 150);
    const fragment2 = msg.slice(150);

    const options = { rsv1: false, mask: true, readOnly: true };

    const frame1 = Buffer.concat(
      Sender.frame(fragment1, {
        fin: false,
        opcode: 0x01,
        ...options
      })
    );
    const frame2 = Buffer.concat(
      Sender.frame(pingMessage, {
        fin: true,
        opcode: 0x09,
        ...options
      })
    );
    const frame3 = Buffer.concat(
      Sender.frame(fragment2, {
        fin: true,
        opcode: 0x00,
        ...options
      })
    );

    let gotPing = false;

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, msg);
      assert.ok(!isBinary);
      assert.ok(gotPing);
      done();
    });
    receiver.on('ping', (data) => {
      gotPing = true;
      assert.ok(data.equals(pingMessage));
    });

    receiver.write(frame1);
    receiver.write(frame2);
    receiver.write(frame3);
  });

  it('parses a 300 B fragmented masked text message with a ping in the middle (2/2)', (done) => {
    const receiver = new Receiver({ isServer: true });
    const msg = Buffer.from('A'.repeat(300));
    const pingMessage = Buffer.from('Hello');

    const fragment1 = msg.slice(0, 150);
    const fragment2 = msg.slice(150);

    const options = { rsv1: false, mask: true, readOnly: false };

    const frame1 = Buffer.concat(
      Sender.frame(Buffer.from(fragment1), {
        fin: false,
        opcode: 0x01,
        ...options
      })
    );
    const frame2 = Buffer.concat(
      Sender.frame(Buffer.from(pingMessage), {
        fin: true,
        opcode: 0x09,
        ...options
      })
    );
    const frame3 = Buffer.concat(
      Sender.frame(Buffer.from(fragment2), {
        fin: true,
        opcode: 0x00,
        ...options
      })
    );

    let chunks = [];
    const splitBuffer = (buf) => {
      const i = Math.floor(buf.length / 2);
      return [buf.slice(0, i), buf.slice(i)];
    };

    chunks = chunks.concat(splitBuffer(frame1));
    chunks = chunks.concat(splitBuffer(frame2));
    chunks = chunks.concat(splitBuffer(frame3));

    let gotPing = false;

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, msg);
      assert.ok(!isBinary);
      assert.ok(gotPing);
      done();
    });
    receiver.on('ping', (data) => {
      gotPing = true;
      assert.ok(data.equals(pingMessage));
    });

    for (let i = 0; i < chunks.length; ++i) {
      receiver.write(chunks[i]);
    }
  });

  it('parses a 100 B masked binary message', (done) => {
    const receiver = new Receiver({ isServer: true });
    const msg = crypto.randomBytes(100);

    const list = Sender.frame(msg, {
      fin: true,
      rsv1: false,
      opcode: 0x02,
      mask: true,
      readOnly: true
    });

    const frame = Buffer.concat(list);

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, msg);
      assert.ok(isBinary);
      done();
    });

    receiver.write(frame);
  });

  it('parses a 256 B masked binary message', (done) => {
    const receiver = new Receiver({ isServer: true });
    const msg = crypto.randomBytes(256);

    const list = Sender.frame(msg, {
      fin: true,
      rsv1: false,
      opcode: 0x02,
      mask: true,
      readOnly: true
    });

    const frame = Buffer.concat(list);

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, msg);
      assert.ok(isBinary);
      done();
    });

    receiver.write(frame);
  });

  it('parses a 200 KiB masked binary message', (done) => {
    const receiver = new Receiver({ isServer: true });
    const msg = crypto.randomBytes(200 * 1024);

    const list = Sender.frame(msg, {
      fin: true,
      rsv1: false,
      opcode: 0x02,
      mask: true,
      readOnly: true
    });

    const frame = Buffer.concat(list);

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, msg);
      assert.ok(isBinary);
      done();
    });

    receiver.write(frame);
  });

  it('parses a 200 KiB unmasked binary message', (done) => {
    const receiver = new Receiver();
    const msg = crypto.randomBytes(200 * 1024);

    const list = Sender.frame(msg, {
      fin: true,
      rsv1: false,
      opcode: 0x02,
      mask: false,
      readOnly: true
    });

    const frame = Buffer.concat(list);

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, msg);
      assert.ok(isBinary);
      done();
    });

    receiver.write(frame);
  });

  it('parses a compressed message', (done) => {
    const perMessageDeflate = new PerMessageDeflate();
    perMessageDeflate.accept([{}]);

    const receiver = new Receiver({
      extensions: {
        'permessage-deflate': perMessageDeflate
      }
    });
    const buf = Buffer.from('Hello');

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, buf);
      assert.ok(!isBinary);
      done();
    });

    perMessageDeflate.compress(buf, true, (err, data) => {
      if (err) return done(err);

      receiver.write(Buffer.from([0xc1, data.length]));
      receiver.write(data);
    });
  });

  it('parses a compressed and fragmented message', (done) => {
    const perMessageDeflate = new PerMessageDeflate();
    perMessageDeflate.accept([{}]);

    const receiver = new Receiver({
      extensions: {
        'permessage-deflate': perMessageDeflate
      }
    });
    const buf1 = Buffer.from('foo');
    const buf2 = Buffer.from('bar');

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, Buffer.concat([buf1, buf2]));
      assert.ok(!isBinary);
      done();
    });

    perMessageDeflate.compress(buf1, false, (err, fragment1) => {
      if (err) return done(err);

      receiver.write(Buffer.from([0x41, fragment1.length]));
      receiver.write(fragment1);

      perMessageDeflate.compress(buf2, true, (err, fragment2) => {
        if (err) return done(err);

        receiver.write(Buffer.from([0x80, fragment2.length]));
        receiver.write(fragment2);
      });
    });
  });

  it('parses a buffer with thousands of frames', (done) => {
    const buf = Buffer.allocUnsafe(40000);

    for (let i = 0; i < buf.length; i += 2) {
      buf[i] = 0x81;
      buf[i + 1] = 0x00;
    }

    const receiver = new Receiver();
    let counter = 0;

    receiver.on('message', (data, isBinary) => {
      assert.strictEqual(data, EMPTY_BUFFER);
      assert.ok(!isBinary);
      if (++counter === 20000) done();
    });

    receiver.write(buf);
  });

  it('resets `totalPayloadLength` only on final frame (unfragmented)', (done) => {
    const receiver = new Receiver({ maxPayload: 10 });

    receiver.on('message', (data, isBinary) => {
      assert.strictEqual(receiver._totalPayloadLength, 0);
      assert.deepStrictEqual(data, Buffer.from('Hello'));
      assert.ok(!isBinary);
      done();
    });

    assert.strictEqual(receiver._totalPayloadLength, 0);
    receiver.write(Buffer.from('810548656c6c6f', 'hex'));
  });

  it('resets `totalPayloadLength` only on final frame (fragmented)', (done) => {
    const receiver = new Receiver({ maxPayload: 10 });

    receiver.on('message', (data, isBinary) => {
      assert.strictEqual(receiver._totalPayloadLength, 0);
      assert.deepStrictEqual(data, Buffer.from('Hello'));
      assert.ok(!isBinary);
      done();
    });

    assert.strictEqual(receiver._totalPayloadLength, 0);
    receiver.write(Buffer.from('01024865', 'hex'));
    assert.strictEqual(receiver._totalPayloadLength, 2);
    receiver.write(Buffer.from('80036c6c6f', 'hex'));
  });

  it('resets `totalPayloadLength` only on final frame (fragmented + ping)', (done) => {
    const receiver = new Receiver({ maxPayload: 10 });
    let data;

    receiver.on('ping', (buf) => {
      assert.strictEqual(receiver._totalPayloadLength, 2);
      data = buf;
    });
    receiver.on('message', (buf, isBinary) => {
      assert.strictEqual(receiver._totalPayloadLength, 0);
      assert.deepStrictEqual(data, EMPTY_BUFFER);
      assert.deepStrictEqual(buf, Buffer.from('Hello'));
      assert.ok(isBinary);
      done();
    });

    assert.strictEqual(receiver._totalPayloadLength, 0);
    receiver.write(Buffer.from('02024865', 'hex'));
    receiver.write(Buffer.from('8900', 'hex'));
    receiver.write(Buffer.from('80036c6c6f', 'hex'));
  });

  it('ignores any data after a close frame', (done) => {
    const perMessageDeflate = new PerMessageDeflate();
    perMessageDeflate.accept([{}]);

    const receiver = new Receiver({
      extensions: {
        'permessage-deflate': perMessageDeflate
      }
    });
    const results = [];
    const push = results.push.bind(results);

    receiver.on('conclude', push).on('message', push);
    receiver.on('finish', () => {
      assert.deepStrictEqual(results, [
        EMPTY_BUFFER,
        false,
        1005,
        EMPTY_BUFFER
      ]);
      done();
    });

    receiver.write(Buffer.from([0xc1, 0x01, 0x00]));
    receiver.write(Buffer.from([0x88, 0x00]));
    receiver.write(Buffer.from([0x81, 0x00]));
  });

  it('emits an error if RSV1 is on and permessage-deflate is disabled', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_UNEXPECTED_RSV_1');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: RSV1 must be clear'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0xc2, 0x80, 0x00, 0x00, 0x00, 0x00]));
  });

  it('emits an error if RSV1 is on and opcode is 0', (done) => {
    const perMessageDeflate = new PerMessageDeflate();
    perMessageDeflate.accept([{}]);

    const receiver = new Receiver({
      extensions: {
        'permessage-deflate': perMessageDeflate
      }
    });

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_UNEXPECTED_RSV_1');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: RSV1 must be clear'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0x40, 0x00]));
  });

  it('emits an error if RSV2 is on', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_UNEXPECTED_RSV_2_3');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: RSV2 and RSV3 must be clear'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0xa2, 0x00]));
  });

  it('emits an error if RSV3 is on', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_UNEXPECTED_RSV_2_3');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: RSV2 and RSV3 must be clear'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0x92, 0x00]));
  });

  it('emits an error if the first frame in a fragmented message has opcode 0', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_INVALID_OPCODE');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: invalid opcode 0'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0x00, 0x00]));
  });

  it('emits an error if a frame has opcode 1 in the middle of a fragmented message', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_INVALID_OPCODE');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: invalid opcode 1'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0x01, 0x00]));
    receiver.write(Buffer.from([0x01, 0x00]));
  });

  it('emits an error if a frame has opcode 2 in the middle of a fragmented message', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_INVALID_OPCODE');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: invalid opcode 2'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0x01, 0x00]));
    receiver.write(Buffer.from([0x02, 0x00]));
  });

  it('emits an error if a control frame has the FIN bit off', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_EXPECTED_FIN');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: FIN must be set'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0x09, 0x00]));
  });

  it('emits an error if a control frame has the RSV1 bit on', (done) => {
    const perMessageDeflate = new PerMessageDeflate();
    perMessageDeflate.accept([{}]);

    const receiver = new Receiver({
      extensions: {
        'permessage-deflate': perMessageDeflate
      }
    });

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_UNEXPECTED_RSV_1');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: RSV1 must be clear'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0xc9, 0x00]));
  });

  it('emits an error if a control frame has the FIN bit off', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_EXPECTED_FIN');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: FIN must be set'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0x09, 0x00]));
  });

  it('emits an error if a frame has the MASK bit off (server mode)', (done) => {
    const receiver = new Receiver({ isServer: true });

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_EXPECTED_MASK');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: MASK must be set'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0x81, 0x02, 0x68, 0x69]));
  });

  it('emits an error if a frame has the MASK bit on (client mode)', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_UNEXPECTED_MASK');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: MASK must be clear'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(
      Buffer.from([0x81, 0x82, 0x56, 0x3a, 0xac, 0x80, 0x3e, 0x53])
    );
  });

  it('emits an error if a control frame has a payload bigger than 125 B', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_INVALID_CONTROL_PAYLOAD_LENGTH');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: invalid payload length 126'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0x89, 0x7e]));
  });

  it('emits an error if a data frame has a payload bigger than 2^53 - 1 B', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_UNSUPPORTED_DATA_PAYLOAD_LENGTH');
      assert.strictEqual(
        err.message,
        'Unsupported WebSocket frame: payload length > 2^53 - 1'
      );
      assert.strictEqual(err[kStatusCode], 1009);
      done();
    });

    receiver.write(Buffer.from([0x82, 0x7f]));
    setImmediate(() =>
      receiver.write(
        Buffer.from([0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
      )
    );
  });

  it('emits an error if a text frame contains invalid UTF-8 data (1/2)', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof Error);
      assert.strictEqual(err.code, 'WS_ERR_INVALID_UTF8');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: invalid UTF-8 sequence'
      );
      assert.strictEqual(err[kStatusCode], 1007);
      done();
    });

    receiver.write(Buffer.from([0x81, 0x04, 0xce, 0xba, 0xe1, 0xbd]));
  });

  it('emits an error if a text frame contains invalid UTF-8 data (2/2)', (done) => {
    const perMessageDeflate = new PerMessageDeflate();
    perMessageDeflate.accept([{}]);

    const receiver = new Receiver({
      extensions: {
        'permessage-deflate': perMessageDeflate
      }
    });
    const buf = Buffer.from([0xce, 0xba, 0xe1, 0xbd]);

    receiver.on('error', (err) => {
      assert.ok(err instanceof Error);
      assert.strictEqual(err.code, 'WS_ERR_INVALID_UTF8');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: invalid UTF-8 sequence'
      );
      assert.strictEqual(err[kStatusCode], 1007);
      done();
    });

    perMessageDeflate.compress(buf, true, (err, data) => {
      if (err) return done(err);

      receiver.write(Buffer.from([0xc1, data.length]));
      receiver.write(data);
    });
  });

  it('emits an error if a close frame has a payload of 1 B', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_INVALID_CONTROL_PAYLOAD_LENGTH');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: invalid payload length 1'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0x88, 0x01]));
  });

  it('emits an error if a close frame contains an invalid close code', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_INVALID_CLOSE_CODE');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: invalid status code 0'
      );
      assert.strictEqual(err[kStatusCode], 1002);
      done();
    });

    receiver.write(Buffer.from([0x88, 0x02, 0x00, 0x00]));
  });

  it('emits an error if a close frame contains invalid UTF-8 data', (done) => {
    const receiver = new Receiver();

    receiver.on('error', (err) => {
      assert.ok(err instanceof Error);
      assert.strictEqual(err.code, 'WS_ERR_INVALID_UTF8');
      assert.strictEqual(
        err.message,
        'Invalid WebSocket frame: invalid UTF-8 sequence'
      );
      assert.strictEqual(err[kStatusCode], 1007);
      done();
    });

    receiver.write(
      Buffer.from([0x88, 0x06, 0x03, 0xef, 0xce, 0xba, 0xe1, 0xbd])
    );
  });

  it('emits an error if a frame payload length is bigger than `maxPayload`', (done) => {
    const receiver = new Receiver({ isServer: true, maxPayload: 20 * 1024 });
    const msg = crypto.randomBytes(200 * 1024);

    const list = Sender.frame(msg, {
      fin: true,
      rsv1: false,
      opcode: 0x02,
      mask: true,
      readOnly: true
    });

    const frame = Buffer.concat(list);

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_UNSUPPORTED_MESSAGE_LENGTH');
      assert.strictEqual(err.message, 'Max payload size exceeded');
      assert.strictEqual(err[kStatusCode], 1009);
      done();
    });

    receiver.write(frame);
  });

  it('emits an error if the message length exceeds `maxPayload`', (done) => {
    const perMessageDeflate = new PerMessageDeflate({
      isServer: false,
      maxPayload: 25
    });
    perMessageDeflate.accept([{}]);

    const receiver = new Receiver({
      extensions: { 'permessage-deflate': perMessageDeflate },
      isServer: false,
      maxPayload: 25
    });
    const buf = Buffer.from('A'.repeat(50));

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_UNSUPPORTED_MESSAGE_LENGTH');
      assert.strictEqual(err.message, 'Max payload size exceeded');
      assert.strictEqual(err[kStatusCode], 1009);
      done();
    });

    perMessageDeflate.compress(buf, true, (err, data) => {
      if (err) return done(err);

      receiver.write(Buffer.from([0xc1, data.length]));
      receiver.write(data);
    });
  });

  it('emits an error if the sum of fragment lengths exceeds `maxPayload`', (done) => {
    const perMessageDeflate = new PerMessageDeflate({
      isServer: false,
      maxPayload: 25
    });
    perMessageDeflate.accept([{}]);

    const receiver = new Receiver({
      extensions: { 'permessage-deflate': perMessageDeflate },
      isServer: false,
      maxPayload: 25
    });
    const buf = Buffer.from('A'.repeat(15));

    receiver.on('error', (err) => {
      assert.ok(err instanceof RangeError);
      assert.strictEqual(err.code, 'WS_ERR_UNSUPPORTED_MESSAGE_LENGTH');
      assert.strictEqual(err.message, 'Max payload size exceeded');
      assert.strictEqual(err[kStatusCode], 1009);
      done();
    });

    perMessageDeflate.compress(buf, false, (err, fragment1) => {
      if (err) return done(err);

      receiver.write(Buffer.from([0x41, fragment1.length]));
      receiver.write(fragment1);

      perMessageDeflate.compress(buf, true, (err, fragment2) => {
        if (err) return done(err);

        receiver.write(Buffer.from([0x80, fragment2.length]));
        receiver.write(fragment2);
      });
    });
  });

  it("honors the 'nodebuffer' binary type", (done) => {
    const receiver = new Receiver();
    const frags = [
      crypto.randomBytes(7321),
      crypto.randomBytes(137),
      crypto.randomBytes(285787),
      crypto.randomBytes(3)
    ];

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, Buffer.concat(frags));
      assert.ok(isBinary);
      done();
    });

    frags.forEach((frag, i) => {
      Sender.frame(frag, {
        fin: i === frags.length - 1,
        opcode: i === 0 ? 2 : 0,
        readOnly: true,
        mask: false,
        rsv1: false
      }).forEach((buf) => receiver.write(buf));
    });
  });

  it("honors the 'arraybuffer' binary type", (done) => {
    const receiver = new Receiver({ binaryType: 'arraybuffer' });
    const frags = [
      crypto.randomBytes(19221),
      crypto.randomBytes(954),
      crypto.randomBytes(623987)
    ];

    receiver.on('message', (data, isBinary) => {
      assert.ok(data instanceof ArrayBuffer);
      assert.deepStrictEqual(Buffer.from(data), Buffer.concat(frags));
      assert.ok(isBinary);
      done();
    });

    frags.forEach((frag, i) => {
      Sender.frame(frag, {
        fin: i === frags.length - 1,
        opcode: i === 0 ? 2 : 0,
        readOnly: true,
        mask: false,
        rsv1: false
      }).forEach((buf) => receiver.write(buf));
    });
  });

  it("honors the 'fragments' binary type", (done) => {
    const receiver = new Receiver({ binaryType: 'fragments' });
    const frags = [
      crypto.randomBytes(17),
      crypto.randomBytes(419872),
      crypto.randomBytes(83),
      crypto.randomBytes(9928),
      crypto.randomBytes(1)
    ];

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, frags);
      assert.ok(isBinary);
      done();
    });

    frags.forEach((frag, i) => {
      Sender.frame(frag, {
        fin: i === frags.length - 1,
        opcode: i === 0 ? 2 : 0,
        readOnly: true,
        mask: false,
        rsv1: false
      }).forEach((buf) => receiver.write(buf));
    });
  });

  it("honors the 'blob' binary type", function (done) {
    if (!hasBlob) return this.skip();

    const receiver = new Receiver({ binaryType: 'blob' });
    const frags = [
      crypto.randomBytes(75688),
      crypto.randomBytes(2688),
      crypto.randomBytes(46753)
    ];

    receiver.on('message', (data, isBinary) => {
      assert.ok(data instanceof Blob);
      assert.ok(isBinary);

      data
        .arrayBuffer()
        .then((arrayBuffer) => {
          assert.deepStrictEqual(
            Buffer.from(arrayBuffer),
            Buffer.concat(frags)
          );

          done();
        })
        .catch(done);
    });

    frags.forEach((frag, i) => {
      Sender.frame(frag, {
        fin: i === frags.length - 1,
        opcode: i === 0 ? 2 : 0,
        readOnly: true,
        mask: false,
        rsv1: false
      }).forEach((buf) => receiver.write(buf));
    });
  });

  it('honors the `skipUTF8Validation` option (1/2)', (done) => {
    const receiver = new Receiver({ skipUTF8Validation: true });

    receiver.on('message', (data, isBinary) => {
      assert.deepStrictEqual(data, Buffer.from([0xf8]));
      assert.ok(!isBinary);
      done();
    });

    receiver.write(Buffer.from([0x81, 0x01, 0xf8]));
  });

  it('honors the `skipUTF8Validation` option (2/2)', (done) => {
    const receiver = new Receiver({ skipUTF8Validation: true });

    receiver.on('conclude', (code, data) => {
      assert.strictEqual(code, 1000);
      assert.deepStrictEqual(data, Buffer.from([0xf8]));
      done();
    });

    receiver.write(Buffer.from([0x88, 0x03, 0x03, 0xe8, 0xf8]));
  });

  it('honors the `allowSynchronousEvents` option', (done) => {
    const actual = [];
    const expected = [
      '1',
      '- 1',
      '-- 1',
      '2',
      '- 2',
      '-- 2',
      '3',
      '- 3',
      '-- 3',
      '4',
      '- 4',
      '-- 4'
    ];

    function listener(data) {
      const message = data.toString();
      actual.push(message);

      // `queueMicrotask()` is not available in Node.js < 11.
      Promise.resolve().then(() => {
        actual.push(`- ${message}`);

        Promise.resolve().then(() => {
          actual.push(`-- ${message}`);

          if (actual.length === 12) {
            assert.deepStrictEqual(actual, expected);
            done();
          }
        });
      });
    }

    const receiver = new Receiver({ allowSynchronousEvents: false });

    receiver.on('message', listener);
    receiver.on('ping', listener);
    receiver.on('pong', listener);

    receiver.write(Buffer.from('8101318901328a0133820134', 'hex'));
  });

  it('does not swallow errors thrown from event handlers', (done) => {
    const receiver = new Receiver();
    let count = 0;

    receiver.on('message', () => {
      if (++count === 2) {
        throw new Error('Oops');
      }
    });

    assert.strictEqual(
      process.listenerCount('uncaughtException'),
      EventEmitter.usingDomains ? 2 : 1
    );

    const listener = process.listeners('uncaughtException').pop();

    process.removeListener('uncaughtException', listener);
    process.once('uncaughtException', (err) => {
      assert.ok(err instanceof Error);
      assert.strictEqual(err.message, 'Oops');

      process.on('uncaughtException', listener);
      done();
    });

    setImmediate(() => {
      receiver.write(Buffer.from('82008200', 'hex'));
    });
  });
});
```

## File: `test/sender.test.js`
```javascript
'use strict';

const assert = require('assert');

const extension = require('../lib/extension');
const PerMessageDeflate = require('../lib/permessage-deflate');
const Sender = require('../lib/sender');
const { EMPTY_BUFFER, hasBlob } = require('../lib/constants');

class MockSocket {
  constructor({ write } = {}) {
    this.readable = true;
    this.writable = true;

    if (write) this.write = write;
  }

  cork() {}
  write() {}
  uncork() {}
}

describe('Sender', () => {
  describe('.frame', () => {
    it('does not mutate the input buffer if data is `readOnly`', () => {
      const buf = Buffer.from([1, 2, 3, 4, 5]);

      Sender.frame(buf, {
        readOnly: true,
        rsv1: false,
        mask: true,
        opcode: 2,
        fin: true
      });

      assert.ok(buf.equals(Buffer.from([1, 2, 3, 4, 5])));
    });

    it('honors the `rsv1` option', () => {
      const list = Sender.frame(EMPTY_BUFFER, {
        readOnly: false,
        mask: false,
        rsv1: true,
        opcode: 1,
        fin: true
      });

      assert.strictEqual(list[0][0] & 0x40, 0x40);
    });

    it('accepts a string as first argument', () => {
      const list = Sender.frame('€', {
        readOnly: false,
        rsv1: false,
        mask: false,
        opcode: 1,
        fin: true
      });

      assert.deepStrictEqual(list[0], Buffer.from('8103', 'hex'));
      assert.deepStrictEqual(list[1], Buffer.from('e282ac', 'hex'));
    });
  });

  describe('#send', () => {
    it('compresses data if compress option is enabled', (done) => {
      const chunks = [];
      const perMessageDeflate = new PerMessageDeflate();
      const mockSocket = new MockSocket({
        write: (chunk) => {
          chunks.push(chunk);
          if (chunks.length !== 6) return;

          assert.strictEqual(chunks[0].length, 2);
          assert.strictEqual(chunks[0][0] & 0x40, 0x40);

          assert.strictEqual(chunks[2].length, 2);
          assert.strictEqual(chunks[2][0] & 0x40, 0x40);

          assert.strictEqual(chunks[4].length, 2);
          assert.strictEqual(chunks[4][0] & 0x40, 0x40);
          done();
        }
      });
      const sender = new Sender(mockSocket, {
        'permessage-deflate': perMessageDeflate
      });

      perMessageDeflate.accept([{}]);

      const options = { compress: true, fin: true };
      const array = new Uint8Array([0x68, 0x69]);

      sender.send(array.buffer, options);
      sender.send(array, options);
      sender.send('hi', options);
    });

    describe('when context takeover is disabled', () => {
      it('honors the compression threshold', (done) => {
        const chunks = [];
        const perMessageDeflate = new PerMessageDeflate();
        const mockSocket = new MockSocket({
          write: (chunk) => {
            chunks.push(chunk);
            if (chunks.length !== 2) return;

            assert.strictEqual(chunks[0].length, 2);
            assert.notStrictEqual(chunk[0][0] & 0x40, 0x40);
            assert.strictEqual(chunks[1], 'hi');
            done();
          }
        });
        const sender = new Sender(mockSocket, {
          'permessage-deflate': perMessageDeflate
        });
        const extensions = extension.parse(
          'permessage-deflate; client_no_context_takeover'
        );

        perMessageDeflate.accept(extensions['permessage-deflate']);

        sender.send('hi', { compress: true, fin: true });
      });

      it('compresses all fragments of a fragmented message', (done) => {
        const chunks = [];
        const perMessageDeflate = new PerMessageDeflate({ threshold: 3 });
        const mockSocket = new MockSocket({
          write: (chunk) => {
            chunks.push(chunk);
            if (chunks.length !== 4) return;

            assert.strictEqual(chunks[0].length, 2);
            assert.strictEqual(chunks[0][0] & 0x40, 0x40);
            assert.strictEqual(chunks[1].length, 9);

            assert.strictEqual(chunks[2].length, 2);
            assert.strictEqual(chunks[2][0] & 0x40, 0x00);
            assert.strictEqual(chunks[3].length, 4);
            done();
          }
        });
        const sender = new Sender(mockSocket, {
          'permessage-deflate': perMessageDeflate
        });
        const extensions = extension.parse(
          'permessage-deflate; client_no_context_takeover'
        );

        perMessageDeflate.accept(extensions['permessage-deflate']);

        sender.send('123', { compress: true, fin: false });
        sender.send('12', { compress: true, fin: true });
      });

      it('does not compress any fragments of a fragmented message', (done) => {
        const chunks = [];
        const perMessageDeflate = new PerMessageDeflate({ threshold: 3 });
        const mockSocket = new MockSocket({
          write: (chunk) => {
            chunks.push(chunk);
            if (chunks.length !== 4) return;

            assert.strictEqual(chunks[0].length, 2);
            assert.strictEqual(chunks[0][0] & 0x40, 0x00);
            assert.strictEqual(chunks[1].length, 2);

            assert.strictEqual(chunks[2].length, 2);
            assert.strictEqual(chunks[2][0] & 0x40, 0x00);
            assert.strictEqual(chunks[3].length, 3);
            done();
          }
        });
        const sender = new Sender(mockSocket, {
          'permessage-deflate': perMessageDeflate
        });
        const extensions = extension.parse(
          'permessage-deflate; client_no_context_takeover'
        );

        perMessageDeflate.accept(extensions['permessage-deflate']);

        sender.send('12', { compress: true, fin: false });
        sender.send('123', { compress: true, fin: true });
      });

      it('compresses empty buffer as first fragment', (done) => {
        const chunks = [];
        const perMessageDeflate = new PerMessageDeflate({ threshold: 0 });
        const mockSocket = new MockSocket({
          write: (chunk) => {
            chunks.push(chunk);
            if (chunks.length !== 4) return;

            assert.strictEqual(chunks[0].length, 2);
            assert.strictEqual(chunks[0][0] & 0x40, 0x40);
            assert.strictEqual(chunks[1].length, 5);

            assert.strictEqual(chunks[2].length, 2);
            assert.strictEqual(chunks[2][0] & 0x40, 0x00);
            assert.strictEqual(chunks[3].length, 6);
            done();
          }
        });
        const sender = new Sender(mockSocket, {
          'permessage-deflate': perMessageDeflate
        });
        const extensions = extension.parse(
          'permessage-deflate; client_no_context_takeover'
        );

        perMessageDeflate.accept(extensions['permessage-deflate']);

        sender.send(Buffer.alloc(0), { compress: true, fin: false });
        sender.send('data', { compress: true, fin: true });
      });

      it('compresses empty buffer as last fragment', (done) => {
        const chunks = [];
        const perMessageDeflate = new PerMessageDeflate({ threshold: 0 });
        const mockSocket = new MockSocket({
          write: (chunk) => {
            chunks.push(chunk);
            if (chunks.length !== 4) return;

            assert.strictEqual(chunks[0].length, 2);
            assert.strictEqual(chunks[0][0] & 0x40, 0x40);
            assert.strictEqual(chunks[1].length, 10);

            assert.strictEqual(chunks[2].length, 2);
            assert.strictEqual(chunks[2][0] & 0x40, 0x00);
            assert.strictEqual(chunks[3].length, 1);
            done();
          }
        });
        const sender = new Sender(mockSocket, {
          'permessage-deflate': perMessageDeflate
        });
        const extensions = extension.parse(
          'permessage-deflate; client_no_context_takeover'
        );

        perMessageDeflate.accept(extensions['permessage-deflate']);

        sender.send('data', { compress: true, fin: false });
        sender.send(Buffer.alloc(0), { compress: true, fin: true });
      });
    });
  });

  describe('#ping', () => {
    it('can send a string as ping payload', (done) => {
      const perMessageDeflate = new PerMessageDeflate();
      let count = 0;
      const mockSocket = new MockSocket({
        write: (data) => {
          if (++count < 3) return;

          if (count === 3) {
            assert.deepStrictEqual(data, Buffer.from([0x89, 0x02]));
          } else {
            assert.strictEqual(data, 'hi');
            done();
          }
        }
      });
      const sender = new Sender(mockSocket, {
        'permessage-deflate': perMessageDeflate
      });

      perMessageDeflate.accept([{}]);

      sender.send('foo', { compress: true, fin: true });
      sender.ping('hi', false);
    });

    it('can send a `TypedArray` as ping payload', (done) => {
      let count = 0;
      const mockSocket = new MockSocket({
        write: (data) => {
          if (++count === 1) {
            assert.deepStrictEqual(data, Buffer.from([0x89, 0x02]));
          } else {
            assert.deepStrictEqual(data, Buffer.from([0x68, 0x69]));
            done();
          }
        }
      });

      const sender = new Sender(mockSocket);
      const array = new Uint8Array([0x68, 0x69]);

      sender.ping(array, false);
    });

    it('can send an `ArrayBuffer` as ping payload', (done) => {
      let count = 0;
      const mockSocket = new MockSocket({
        write: (data) => {
          if (++count === 1) {
            assert.deepStrictEqual(data, Buffer.from([0x89, 0x02]));
          } else {
            assert.deepStrictEqual(data, Buffer.from([0x68, 0x69]));
            done();
          }
        }
      });

      const sender = new Sender(mockSocket);
      const array = new Uint8Array([0x68, 0x69]);

      sender.ping(array.buffer, false);
    });

    it('can send a `Blob` as ping payload', function (done) {
      if (!hasBlob) return this.skip();

      let count = 0;
      const mockSocket = new MockSocket({
        write: (data) => {
          if (++count % 2) {
            assert.deepStrictEqual(data, Buffer.from([0x89, 0x02]));
          } else {
            assert.deepStrictEqual(data, Buffer.from([0x68, 0x69]));
            if (count === 4) done();
          }
        }
      });

      const sender = new Sender(mockSocket);
      const blob = new Blob(['hi']);

      sender.ping(blob, false);
      sender.ping(blob, false);
    });
  });

  describe('#pong', () => {
    it('can send a string as ping payload', (done) => {
      const perMessageDeflate = new PerMessageDeflate();
      let count = 0;
      const mockSocket = new MockSocket({
        write: (data) => {
          if (++count < 3) return;

          if (count === 3) {
            assert.deepStrictEqual(data, Buffer.from([0x8a, 0x02]));
          } else {
            assert.strictEqual(data, 'hi');
            done();
          }
        }
      });
      const sender = new Sender(mockSocket, {
        'permessage-deflate': perMessageDeflate
      });

      perMessageDeflate.accept([{}]);

      sender.send('foo', { compress: true, fin: true });
      sender.pong('hi', false);
    });

    it('can send a `TypedArray` as ping payload', (done) => {
      let count = 0;
      const mockSocket = new MockSocket({
        write: (data) => {
          if (++count === 1) {
            assert.deepStrictEqual(data, Buffer.from([0x8a, 0x02]));
          } else {
            assert.deepStrictEqual(data, Buffer.from([0x68, 0x69]));
            done();
          }
        }
      });

      const sender = new Sender(mockSocket);
      const array = new Uint8Array([0x68, 0x69]);

      sender.pong(array, false);
    });

    it('can send an `ArrayBuffer` as ping payload', (done) => {
      let count = 0;
      const mockSocket = new MockSocket({
        write: (data) => {
          if (++count === 1) {
            assert.deepStrictEqual(data, Buffer.from([0x8a, 0x02]));
          } else {
            assert.deepStrictEqual(data, Buffer.from([0x68, 0x69]));
            done();
          }
        }
      });

      const sender = new Sender(mockSocket);
      const array = new Uint8Array([0x68, 0x69]);

      sender.pong(array.buffer, false);
    });

    it('can send a `Blob` as ping payload', function (done) {
      if (!hasBlob) return this.skip();

      let count = 0;
      const mockSocket = new MockSocket({
        write: (data) => {
          if (++count % 2) {
            assert.deepStrictEqual(data, Buffer.from([0x8a, 0x02]));
          } else {
            assert.deepStrictEqual(data, Buffer.from([0x68, 0x69]));
            if (count === 4) done();
          }
        }
      });

      const sender = new Sender(mockSocket);
      const blob = new Blob(['hi']);

      sender.pong(blob, false);
      sender.pong(blob, false);
    });
  });

  describe('#close', () => {
    it('throws an error if the first argument is invalid', () => {
      const mockSocket = new MockSocket();
      const sender = new Sender(mockSocket);

      assert.throws(
        () => sender.close('error'),
        /^TypeError: First argument must be a valid error code number$/
      );

      assert.throws(
        () => sender.close(1004),
        /^TypeError: First argument must be a valid error code number$/
      );
    });

    it('throws an error if the message is greater than 123 bytes', () => {
      const mockSocket = new MockSocket();
      const sender = new Sender(mockSocket);

      assert.throws(
        () => sender.close(1000, 'a'.repeat(124)),
        /^RangeError: The message must not be greater than 123 bytes$/
      );
    });

    it('should consume all data before closing', (done) => {
      const perMessageDeflate = new PerMessageDeflate();

      let count = 0;
      const mockSocket = new MockSocket({
        write: (data, cb) => {
          count++;
          if (cb) cb();
        }
      });
      const sender = new Sender(mockSocket, {
        'permessage-deflate': perMessageDeflate
      });

      perMessageDeflate.accept([{}]);

      sender.send('foo', { compress: true, fin: true });
      sender.send('bar', { compress: true, fin: true });
      sender.send('baz', { compress: true, fin: true });

      sender.close(1000, undefined, false, () => {
        assert.strictEqual(count, 8);
        done();
      });
    });
  });
});
```

## File: `test/subprotocol.test.js`
```javascript
'use strict';

const assert = require('assert');

const { parse } = require('../lib/subprotocol');

describe('subprotocol', () => {
  describe('parse', () => {
    it('parses a single subprotocol', () => {
      assert.deepStrictEqual(parse('foo'), new Set(['foo']));
    });

    it('parses multiple subprotocols', () => {
      assert.deepStrictEqual(
        parse('foo,bar,baz'),
        new Set(['foo', 'bar', 'baz'])
      );
    });

    it('ignores the optional white spaces', () => {
      const header = 'foo , bar\t, \tbaz\t ,  qux\t\t,norf';

      assert.deepStrictEqual(
        parse(header),
        new Set(['foo', 'bar', 'baz', 'qux', 'norf'])
      );
    });

    it('throws an error if a subprotocol is empty', () => {
      [
        [',', 0],
        ['foo,,', 4],
        ['foo,  ,', 6]
      ].forEach((element) => {
        assert.throws(
          () => parse(element[0]),
          new RegExp(
            `^SyntaxError: Unexpected character at index ${element[1]}$`
          )
        );
      });
    });

    it('throws an error if a subprotocol is duplicated', () => {
      ['foo,foo,bar', 'foo,bar,foo'].forEach((header) => {
        assert.throws(
          () => parse(header),
          /^SyntaxError: The "foo" subprotocol is duplicated$/
        );
      });
    });

    it('throws an error if a white space is misplaced', () => {
      [
        ['f oo', 2],
        [' foo', 0]
      ].forEach((element) => {
        assert.throws(
          () => parse(element[0]),
          new RegExp(
            `^SyntaxError: Unexpected character at index ${element[1]}$`
          )
        );
      });
    });

    it('throws an error if a subprotocol contains invalid characters', () => {
      [
        ['f@o', 1],
        ['f\\oo', 1],
        ['foo,b@r', 5]
      ].forEach((element) => {
        assert.throws(
          () => parse(element[0]),
          new RegExp(
            `^SyntaxError: Unexpected character at index ${element[1]}$`
          )
        );
      });
    });

    it('throws an error if the header value ends prematurely', () => {
      ['foo ', 'foo, ', 'foo,bar ', 'foo,bar,'].forEach((header) => {
        assert.throws(
          () => parse(header),
          /^SyntaxError: Unexpected end of input$/
        );
      });
    });
  });
});
```

## File: `test/validation.test.js`
```javascript
'use strict';

const assert = require('assert');

const { isValidUTF8 } = require('../lib/validation');

describe('extension', () => {
  describe('isValidUTF8', () => {
    it('returns false if it finds invalid bytes', () => {
      assert.strictEqual(isValidUTF8(Buffer.from([0xf8])), false);
    });

    it('returns false for overlong encodings', () => {
      assert.strictEqual(isValidUTF8(Buffer.from([0xc0, 0xa0])), false);
      assert.strictEqual(isValidUTF8(Buffer.from([0xe0, 0x80, 0xa0])), false);
      assert.strictEqual(
        isValidUTF8(Buffer.from([0xf0, 0x80, 0x80, 0xa0])),
        false
      );
    });

    it('returns false for code points in the range U+D800 - U+DFFF', () => {
      for (let i = 0xa0; i < 0xc0; i++) {
        for (let j = 0x80; j < 0xc0; j++) {
          assert.strictEqual(isValidUTF8(Buffer.from([0xed, i, j])), false);
        }
      }
    });

    it('returns false for code points greater than U+10FFFF', () => {
      assert.strictEqual(
        isValidUTF8(Buffer.from([0xf4, 0x90, 0x80, 0x80])),
        false
      );
      assert.strictEqual(
        isValidUTF8(Buffer.from([0xf5, 0x80, 0x80, 0x80])),
        false
      );
    });

    it('returns true for a well-formed UTF-8 byte sequence', () => {
      // prettier-ignore
      const buf = Buffer.from([
        0xe2, 0x82, 0xAC, // €
        0xf0, 0x90, 0x8c, 0x88, // 𐍈
        0x24 // $
      ]);

      assert.strictEqual(isValidUTF8(buf), true);
    });
  });
});
```

## File: `test/websocket-server.test.js`
```javascript
/* eslint no-unused-vars: ["error", { "varsIgnorePattern": "^ws$" }] */

'use strict';

const assert = require('assert');
const crypto = require('crypto');
const https = require('https');
const http = require('http');
const path = require('path');
const net = require('net');
const fs = require('fs');
const os = require('os');

const makeDuplexPair = require('./duplex-pair');
const Sender = require('../lib/sender');
const WebSocket = require('..');
const { NOOP } = require('../lib/constants');

describe('WebSocketServer', () => {
  describe('#ctor', () => {
    it('throws an error if no option object is passed', () => {
      assert.throws(
        () => new WebSocket.Server(),
        new RegExp(
          '^TypeError: One and only one of the "port", "server", or ' +
            '"noServer" options must be specified$'
        )
      );
    });

    describe('options', () => {
      it('throws an error if required options are not specified', () => {
        assert.throws(
          () => new WebSocket.Server({}),
          new RegExp(
            '^TypeError: One and only one of the "port", "server", or ' +
              '"noServer" options must be specified$'
          )
        );
      });

      it('throws an error if mutually exclusive options are specified', () => {
        const server = http.createServer();
        const variants = [
          { port: 0, noServer: true, server },
          { port: 0, noServer: true },
          { port: 0, server },
          { noServer: true, server }
        ];

        for (const options of variants) {
          assert.throws(
            () => new WebSocket.Server(options),
            new RegExp(
              '^TypeError: One and only one of the "port", "server", or ' +
                '"noServer" options must be specified$'
            )
          );
        }
      });

      it('exposes options passed to constructor', (done) => {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          assert.strictEqual(wss.options.port, 0);
          wss.close(done);
        });
      });

      it('accepts the `maxPayload` option', (done) => {
        const maxPayload = 20480;
        const wss = new WebSocket.Server(
          {
            perMessageDeflate: true,
            maxPayload,
            port: 0
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

            ws.on('open', ws.close);
          }
        );

        wss.on('connection', (ws) => {
          assert.strictEqual(ws._receiver._maxPayload, maxPayload);
          assert.strictEqual(
            ws._receiver._extensions['permessage-deflate']._maxPayload,
            maxPayload
          );
          wss.close(done);
        });
      });

      it('honors the `WebSocket` option', (done) => {
        class CustomWebSocket extends WebSocket.WebSocket {
          get foo() {
            return 'foo';
          }
        }

        const wss = new WebSocket.Server(
          {
            port: 0,
            WebSocket: CustomWebSocket
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

            ws.on('open', ws.close);
          }
        );

        wss.on('connection', (ws) => {
          assert.ok(ws instanceof CustomWebSocket);
          assert.strictEqual(ws.foo, 'foo');
          wss.close(done);
        });
      });

      it('honors the `autoPong` option', (done) => {
        const wss = new WebSocket.Server({ autoPong: false, port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          ws.on('open', () => {
            ws.ping();
          });

          ws.on('pong', () => {
            done(new Error("Unexpected 'pong' event"));
          });
        });

        wss.on('connection', (ws) => {
          ws.on('ping', () => {
            ws.close();
          });

          ws.on('close', () => {
            wss.close(done);
          });
        });
      });

      it('honors the `closeTimeout` option', (done) => {
        const closeTimeout = 1000;
        const wss = new WebSocket.Server({ closeTimeout, port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        });

        wss.on('connection', (ws) => {
          ws.on('close', () => {
            wss.close(done);
          });

          ws.close();
          assert.strictEqual(ws._closeTimer._idleTimeout, closeTimeout);
        });
      });
    });

    it('emits an error if http server bind fails', (done) => {
      const wss1 = new WebSocket.Server({ port: 0 }, () => {
        const wss2 = new WebSocket.Server({
          port: wss1.address().port
        });

        wss2.on('error', () => wss1.close(done));
      });
    });

    it('starts a server on a given port', (done) => {
      const port = 1337;
      const wss = new WebSocket.Server({ port }, () => {
        const ws = new WebSocket(`ws://localhost:${port}`);

        ws.on('open', ws.close);
      });

      wss.on('connection', () => wss.close(done));
    });

    it('binds the server on any IPv6 address when available', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        assert.strictEqual(wss._server.address().address, '::');
        wss.close(done);
      });
    });

    it('uses a precreated http server', (done) => {
      const server = http.createServer();

      server.listen(0, () => {
        const wss = new WebSocket.Server({ server });

        wss.on('connection', () => {
          server.close(done);
        });

        const ws = new WebSocket(`ws://localhost:${server.address().port}`);

        ws.on('open', ws.close);
      });
    });

    it('426s for non-Upgrade requests', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        http.get(`http://localhost:${wss.address().port}`, (res) => {
          let body = '';

          assert.strictEqual(res.statusCode, 426);
          res.on('data', (chunk) => {
            body += chunk;
          });
          res.on('end', () => {
            assert.strictEqual(body, http.STATUS_CODES[426]);
            wss.close(done);
          });
        });
      });
    });

    it('uses a precreated http server listening on IPC', (done) => {
      const randomString = crypto.randomBytes(4).toString('hex');
      const ipcPath =
        process.platform === 'win32'
          ? `\\\\.\\pipe\\ws-pipe-${randomString}`
          : path.join(os.tmpdir(), `ws-${randomString}.sock`);

      const server = http.createServer();

      server.listen(ipcPath, () => {
        const wss = new WebSocket.Server({ server });

        wss.on('connection', (ws, req) => {
          if (wss.clients.size === 1) {
            assert.strictEqual(req.url, '/foo?bar=bar');
          } else {
            assert.strictEqual(req.url, '/');

            for (const client of wss.clients) {
              client.close();
            }

            server.close(done);
          }
        });

        const ws = new WebSocket(`ws+unix:${ipcPath}:/foo?bar=bar`);
        ws.on('open', () => new WebSocket(`ws+unix:${ipcPath}`));
      });
    });
  });

  describe('#address', () => {
    it('returns the address of the server', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const addr = wss.address();

        assert.deepStrictEqual(addr, wss._server.address());
        wss.close(done);
      });
    });

    it('throws an error when operating in "noServer" mode', () => {
      const wss = new WebSocket.Server({ noServer: true });

      assert.throws(() => {
        wss.address();
      }, /^Error: The server is operating in "noServer" mode$/);
    });

    it('returns `null` if called after close', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        wss.close(() => {
          assert.strictEqual(wss.address(), null);
          done();
        });
      });
    });
  });

  describe('#close', () => {
    it('does not throw if called multiple times', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        wss.on('close', done);

        wss.close();
        wss.close();
        wss.close();
      });
    });

    it("doesn't close a precreated server", (done) => {
      const server = http.createServer();
      const realClose = server.close;

      server.close = () => {
        done(new Error('Must not close pre-created server'));
      };

      const wss = new WebSocket.Server({ server });

      wss.on('connection', () => {
        wss.close();
        server.close = realClose;
        server.close(done);
      });

      server.listen(0, () => {
        const ws = new WebSocket(`ws://localhost:${server.address().port}`);

        ws.on('open', ws.close);
      });
    });

    it('invokes the callback in noServer mode', (done) => {
      const wss = new WebSocket.Server({ noServer: true });

      wss.close(done);
    });

    it('cleans event handlers on precreated server', (done) => {
      const server = http.createServer();
      const listeningListenerCount = server.listenerCount('listening');
      const wss = new WebSocket.Server({ server });

      server.listen(0, () => {
        wss.close(() => {
          assert.strictEqual(
            server.listenerCount('listening'),
            listeningListenerCount
          );
          assert.strictEqual(server.listenerCount('upgrade'), 0);
          assert.strictEqual(server.listenerCount('error'), 0);

          server.close(done);
        });
      });
    });

    it("emits the 'close' event after the server closes", (done) => {
      let serverCloseEventEmitted = false;

      const wss = new WebSocket.Server({ port: 0 }, () => {
        net.createConnection({ port: wss.address().port });
      });

      wss._server.on('connection', (socket) => {
        wss.close();

        //
        // The server is closing. Ensure this does not emit a `'close'`
        // event before the server is actually closed.
        //
        wss.close();

        process.nextTick(() => {
          socket.end();
        });
      });

      wss._server.on('close', () => {
        serverCloseEventEmitted = true;
      });

      wss.on('close', () => {
        assert.ok(serverCloseEventEmitted);
        done();
      });
    });

    it("emits the 'close' event if client tracking is disabled", (done) => {
      const wss = new WebSocket.Server({
        noServer: true,
        clientTracking: false
      });

      wss.on('close', done);
      wss.close();
    });

    it('calls the callback if the server is already closed', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        wss.close(() => {
          assert.strictEqual(wss._state, 2);

          wss.close((err) => {
            assert.ok(err instanceof Error);
            assert.strictEqual(err.message, 'The server is not running');
            done();
          });
        });
      });
    });

    it("emits the 'close' event if the server is already closed", (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        wss.close(() => {
          assert.strictEqual(wss._state, 2);

          wss.on('close', done);
          wss.close();
        });
      });
    });
  });

  describe('#clients', () => {
    it('returns a list of connected clients', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        assert.strictEqual(wss.clients.size, 0);

        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', ws.close);
      });

      wss.on('connection', () => {
        assert.strictEqual(wss.clients.size, 1);
        wss.close(done);
      });
    });

    it('can be disabled', (done) => {
      const wss = new WebSocket.Server(
        { port: 0, clientTracking: false },
        () => {
          assert.strictEqual(wss.clients, undefined);
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          ws.on('open', () => ws.close());
        }
      );

      wss.on('connection', (ws) => {
        assert.strictEqual(wss.clients, undefined);
        ws.on('close', () => wss.close(done));
      });
    });

    it('is updated when client terminates the connection', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => ws.terminate());
      });

      wss.on('connection', (ws) => {
        ws.on('close', () => {
          assert.strictEqual(wss.clients.size, 0);
          wss.close(done);
        });
      });
    });

    it('is updated when client closes the connection', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => ws.close());
      });

      wss.on('connection', (ws) => {
        ws.on('close', () => {
          assert.strictEqual(wss.clients.size, 0);
          wss.close(done);
        });
      });
    });
  });

  describe('#shouldHandle', () => {
    it('returns true when the path matches', () => {
      const wss = new WebSocket.Server({ noServer: true, path: '/foo' });

      assert.strictEqual(wss.shouldHandle({ url: '/foo' }), true);
      assert.strictEqual(wss.shouldHandle({ url: '/foo?bar=baz' }), true);
    });

    it("returns false when the path doesn't match", () => {
      const wss = new WebSocket.Server({ noServer: true, path: '/foo' });

      assert.strictEqual(wss.shouldHandle({ url: '/bar' }), false);
    });
  });

  describe('#handleUpgrade', () => {
    it('can be used for a pre-existing server', (done) => {
      const server = http.createServer();

      server.listen(0, () => {
        const wss = new WebSocket.Server({ noServer: true });

        server.on('upgrade', (req, socket, head) => {
          wss.handleUpgrade(req, socket, head, (ws) => {
            ws.send('hello');
            ws.close();
          });
        });

        const ws = new WebSocket(`ws://localhost:${server.address().port}`);

        ws.on('message', (message, isBinary) => {
          assert.deepStrictEqual(message, Buffer.from('hello'));
          assert.ok(!isBinary);
          server.close(done);
        });
      });
    });

    it("closes the connection when path doesn't match", (done) => {
      const wss = new WebSocket.Server({ port: 0, path: '/ws' }, () => {
        const req = http.get({
          port: wss.address().port,
          headers: {
            Connection: 'Upgrade',
            Upgrade: 'websocket',
            'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ==',
            'Sec-WebSocket-Version': 13
          }
        });

        req.on('response', (res) => {
          assert.strictEqual(res.statusCode, 400);
          wss.close(done);
        });
      });
    });

    it('closes the connection when protocol version is Hixie-76', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const req = http.get({
          port: wss.address().port,
          headers: {
            Connection: 'Upgrade',
            Upgrade: 'WebSocket',
            'Sec-WebSocket-Key1': '4 @1  46546xW%0l 1 5',
            'Sec-WebSocket-Key2': '12998 5 Y3 1  .P00',
            'Sec-WebSocket-Protocol': 'sample'
          }
        });

        req.on('response', (res) => {
          assert.strictEqual(res.statusCode, 400);

          const chunks = [];

          res.on('data', (chunk) => {
            chunks.push(chunk);
          });

          res.on('end', () => {
            assert.strictEqual(
              Buffer.concat(chunks).toString(),
              'Missing or invalid Sec-WebSocket-Key header'
            );
            wss.close(done);
          });
        });
      });
    });

    it('completes a WebSocket upgrade over any duplex stream', (done) => {
      const server = http.createServer();

      server.listen(0, () => {
        const wss = new WebSocket.Server({ noServer: true });

        server.on('upgrade', (req, socket, head) => {
          //
          // Put a stream between the raw socket and our websocket processing.
          //
          const { clientSide, serverSide } = makeDuplexPair();

          socket.pipe(clientSide);
          clientSide.pipe(socket);

          //
          // Pass the other side of the stream as the socket to upgrade.
          //
          wss.handleUpgrade(req, serverSide, head, (ws) => {
            ws.send('hello');
            ws.close();
          });
        });

        const ws = new WebSocket(`ws://localhost:${server.address().port}`);

        ws.on('message', (message, isBinary) => {
          assert.deepStrictEqual(message, Buffer.from('hello'));
          assert.ok(!isBinary);
          server.close(done);
        });
      });
    });
  });

  describe('#completeUpgrade', () => {
    it('throws an error if called twice with the same socket', (done) => {
      const server = http.createServer();

      server.listen(0, () => {
        const wss = new WebSocket.Server({ noServer: true });

        server.on('upgrade', (req, socket, head) => {
          wss.handleUpgrade(req, socket, head, (ws) => {
            ws.close();
          });
          assert.throws(
            () => wss.handleUpgrade(req, socket, head, NOOP),
            (err) => {
              assert.ok(err instanceof Error);
              assert.strictEqual(
                err.message,
                'server.handleUpgrade() was called more than once with the ' +
                  'same socket, possibly due to a misconfiguration'
              );
              return true;
            }
          );
        });

        const ws = new WebSocket(`ws://localhost:${server.address().port}`);

        ws.on('open', () => {
          ws.on('close', () => {
            server.close(done);
          });
        });
      });
    });
  });

  describe('Connection establishing', () => {
    it('fails if the HTTP method is not GET', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const req = http.request({
          method: 'POST',
          port: wss.address().port,
          headers: {
            Connection: 'Upgrade',
            Upgrade: 'websocket'
          }
        });

        req.on('response', (res) => {
          assert.strictEqual(res.statusCode, 405);

          const chunks = [];

          res.on('data', (chunk) => {
            chunks.push(chunk);
          });

          res.on('end', () => {
            assert.strictEqual(
              Buffer.concat(chunks).toString(),
              'Invalid HTTP method'
            );
            wss.close(done);
          });
        });

        req.end();
      });

      wss.on('connection', () => {
        done(new Error("Unexpected 'connection' event"));
      });
    });

    it('fails if the Upgrade header field value cannot be read', (done) => {
      const server = http.createServer();
      const wss = new WebSocket.Server({ noServer: true });

      server.maxHeadersCount = 1;

      server.on('upgrade', (req, socket, head) => {
        assert.deepStrictEqual(req.headers, { foo: 'bar' });
        wss.handleUpgrade(req, socket, head, () => {
          done(new Error('Unexpected callback invocation'));
        });
      });

      server.listen(() => {
        const req = http.get({
          port: server.address().port,
          headers: {
            foo: 'bar',
            bar: 'baz',
            Connection: 'Upgrade',
            Upgrade: 'websocket'
          }
        });

        req.on('response', (res) => {
          assert.strictEqual(res.statusCode, 400);

          const chunks = [];

          res.on('data', (chunk) => {
            chunks.push(chunk);
          });

          res.on('end', () => {
            assert.strictEqual(
              Buffer.concat(chunks).toString(),
              'Invalid Upgrade header'
            );
            server.close(done);
          });
        });
      });
    });

    it('fails if the Upgrade header field value is not "websocket"', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const req = http.get({
          port: wss.address().port,
          headers: {
            Connection: 'Upgrade',
            Upgrade: 'foo'
          }
        });

        req.on('response', (res) => {
          assert.strictEqual(res.statusCode, 400);

          const chunks = [];

          res.on('data', (chunk) => {
            chunks.push(chunk);
          });

          res.on('end', () => {
            assert.strictEqual(
              Buffer.concat(chunks).toString(),
              'Invalid Upgrade header'
            );
            wss.close(done);
          });
        });
      });

      wss.on('connection', () => {
        done(new Error("Unexpected 'connection' event"));
      });
    });

    it('fails if the Sec-WebSocket-Key header is invalid (1/2)', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const req = http.get({
          port: wss.address().port,
          headers: {
            Connection: 'Upgrade',
            Upgrade: 'websocket'
          }
        });

        req.on('response', (res) => {
          assert.strictEqual(res.statusCode, 400);

          const chunks = [];

          res.on('data', (chunk) => {
            chunks.push(chunk);
          });

          res.on('end', () => {
            assert.strictEqual(
              Buffer.concat(chunks).toString(),
              'Missing or invalid Sec-WebSocket-Key header'
            );
            wss.close(done);
          });
        });
      });

      wss.on('connection', () => {
        done(new Error("Unexpected 'connection' event"));
      });
    });

    it('fails if the Sec-WebSocket-Key header is invalid (2/2)', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const req = http.get({
          port: wss.address().port,
          headers: {
            Connection: 'Upgrade',
            Upgrade: 'websocket',
            'Sec-WebSocket-Key': 'P5l8BJcZwRc='
          }
        });

        req.on('response', (res) => {
          assert.strictEqual(res.statusCode, 400);

          const chunks = [];

          res.on('data', (chunk) => {
            chunks.push(chunk);
          });

          res.on('end', () => {
            assert.strictEqual(
              Buffer.concat(chunks).toString(),
              'Missing or invalid Sec-WebSocket-Key header'
            );
            wss.close(done);
          });
        });
      });

      wss.on('connection', () => {
        done(new Error("Unexpected 'connection' event"));
      });
    });

    it('fails if the Sec-WebSocket-Version header is invalid (1/2)', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const req = http.get({
          port: wss.address().port,
          headers: {
            Connection: 'Upgrade',
            Upgrade: 'websocket',
            'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ=='
          }
        });

        req.on('response', (res) => {
          assert.strictEqual(res.statusCode, 400);
          assert.strictEqual(res.headers['sec-websocket-version'], '13, 8');

          const chunks = [];

          res.on('data', (chunk) => {
            chunks.push(chunk);
          });

          res.on('end', () => {
            assert.strictEqual(
              Buffer.concat(chunks).toString(),
              'Missing or invalid Sec-WebSocket-Version header'
            );
            wss.close(done);
          });
        });
      });

      wss.on('connection', () => {
        done(new Error("Unexpected 'connection' event"));
      });
    });

    it('fails if the Sec-WebSocket-Version header is invalid (2/2)', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const req = http.get({
          port: wss.address().port,
          headers: {
            Connection: 'Upgrade',
            Upgrade: 'websocket',
            'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ==',
            'Sec-WebSocket-Version': 12
          }
        });

        req.on('response', (res) => {
          assert.strictEqual(res.statusCode, 400);
          assert.strictEqual(res.headers['sec-websocket-version'], '13, 8');

          const chunks = [];

          res.on('data', (chunk) => {
            chunks.push(chunk);
          });

          res.on('end', () => {
            assert.strictEqual(
              Buffer.concat(chunks).toString(),
              'Missing or invalid Sec-WebSocket-Version header'
            );
            wss.close(done);
          });
        });
      });

      wss.on('connection', () => {
        done(new Error("Unexpected 'connection' event"));
      });
    });

    it('fails is the Sec-WebSocket-Protocol header is invalid', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const req = http.get({
          port: wss.address().port,
          headers: {
            Connection: 'Upgrade',
            Upgrade: 'websocket',
            'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ==',
            'Sec-WebSocket-Version': 13,
            'Sec-WebSocket-Protocol': 'foo;bar'
          }
        });

        req.on('response', (res) => {
          assert.strictEqual(res.statusCode, 400);

          const chunks = [];

          res.on('data', (chunk) => {
            chunks.push(chunk);
          });

          res.on('end', () => {
            assert.strictEqual(
              Buffer.concat(chunks).toString(),
              'Invalid Sec-WebSocket-Protocol header'
            );
            wss.close(done);
          });
        });
      });

      wss.on('connection', () => {
        done(new Error("Unexpected 'connection' event"));
      });
    });

    it('fails if the Sec-WebSocket-Extensions header is invalid', (done) => {
      const wss = new WebSocket.Server(
        {
          perMessageDeflate: true,
          port: 0
        },
        () => {
          const req = http.get({
            port: wss.address().port,
            headers: {
              Connection: 'Upgrade',
              Upgrade: 'websocket',
              'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ==',
              'Sec-WebSocket-Version': 13,
              'Sec-WebSocket-Extensions':
                'permessage-deflate; server_max_window_bits=foo'
            }
          });

          req.on('response', (res) => {
            assert.strictEqual(res.statusCode, 400);

            const chunks = [];

            res.on('data', (chunk) => {
              chunks.push(chunk);
            });

            res.on('end', () => {
              assert.strictEqual(
                Buffer.concat(chunks).toString(),
                'Invalid or unacceptable Sec-WebSocket-Extensions header'
              );
              wss.close(done);
            });
          });
        }
      );

      wss.on('connection', () => {
        done(new Error("Unexpected 'connection' event"));
      });
    });

    it("emits the 'wsClientError' event", (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const req = http.request({
          method: 'POST',
          port: wss.address().port,
          headers: {
            Connection: 'Upgrade',
            Upgrade: 'websocket'
          }
        });

        req.on('response', (res) => {
          assert.strictEqual(res.statusCode, 400);
          wss.close(done);
        });

        req.end();
      });

      wss.on('wsClientError', (err, socket, request) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(err.message, 'Invalid HTTP method');

        assert.ok(request instanceof http.IncomingMessage);
        assert.strictEqual(request.method, 'POST');

        socket.end('HTTP/1.1 400 Bad Request\r\n\r\n');
      });

      wss.on('connection', () => {
        done(new Error("Unexpected 'connection' event"));
      });
    });

    it('fails if the WebSocket server is closing or closed', (done) => {
      const server = http.createServer();
      const wss = new WebSocket.Server({ noServer: true });

      server.on('upgrade', (req, socket, head) => {
        wss.close();
        wss.handleUpgrade(req, socket, head, () => {
          done(new Error('Unexpected callback invocation'));
        });
      });

      server.listen(0, () => {
        const ws = new WebSocket(`ws://localhost:${server.address().port}`);

        ws.on('unexpected-response', (req, res) => {
          assert.strictEqual(res.statusCode, 503);
          res.resume();
          server.close(done);
        });
      });
    });

    it('handles unsupported extensions', (done) => {
      const wss = new WebSocket.Server(
        {
          perMessageDeflate: true,
          port: 0
        },
        () => {
          const req = http.get({
            port: wss.address().port,
            headers: {
              Connection: 'Upgrade',
              Upgrade: 'websocket',
              'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ==',
              'Sec-WebSocket-Version': 13,
              'Sec-WebSocket-Extensions': 'foo; bar'
            }
          });

          req.on('upgrade', (res, socket, head) => {
            if (head.length) socket.unshift(head);

            socket.once('data', (chunk) => {
              assert.strictEqual(chunk[0], 0x88);
              socket.destroy();
              wss.close(done);
            });
          });
        }
      );

      wss.on('connection', (ws) => {
        assert.strictEqual(ws.extensions, '');
        ws.close();
      });
    });

    describe('`verifyClient`', () => {
      it('can reject client synchronously', (done) => {
        const wss = new WebSocket.Server(
          {
            verifyClient: () => false,
            port: 0
          },
          () => {
            const req = http.get({
              port: wss.address().port,
              headers: {
                Connection: 'Upgrade',
                Upgrade: 'websocket',
                'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ==',
                'Sec-WebSocket-Version': 8
              }
            });

            req.on('response', (res) => {
              assert.strictEqual(res.statusCode, 401);
              wss.close(done);
            });
          }
        );

        wss.on('connection', () => {
          done(new Error("Unexpected 'connection' event"));
        });
      });

      it('can accept client synchronously', (done) => {
        const server = https.createServer({
          cert: fs.readFileSync('test/fixtures/certificate.pem'),
          key: fs.readFileSync('test/fixtures/key.pem')
        });

        const wss = new WebSocket.Server({
          verifyClient: (info) => {
            assert.strictEqual(info.origin, 'https://example.com');
            assert.strictEqual(info.req.headers.foo, 'bar');
            assert.ok(info.secure, true);
            return true;
          },
          server
        });

        wss.on('connection', () => {
          server.close(done);
        });

        server.listen(0, () => {
          const ws = new WebSocket(`wss://localhost:${server.address().port}`, {
            headers: { Origin: 'https://example.com', foo: 'bar' },
            rejectUnauthorized: false
          });

          ws.on('open', ws.close);
        });
      });

      it('can accept client asynchronously', (done) => {
        const wss = new WebSocket.Server(
          {
            verifyClient: (o, cb) => process.nextTick(cb, true),
            port: 0
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

            ws.on('open', ws.close);
          }
        );

        wss.on('connection', () => wss.close(done));
      });

      it('can reject client asynchronously', (done) => {
        const wss = new WebSocket.Server(
          {
            verifyClient: (info, cb) => process.nextTick(cb, false),
            port: 0
          },
          () => {
            const req = http.get({
              port: wss.address().port,
              headers: {
                Connection: 'Upgrade',
                Upgrade: 'websocket',
                'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ==',
                'Sec-WebSocket-Version': 8
              }
            });

            req.on('response', (res) => {
              assert.strictEqual(res.statusCode, 401);
              wss.close(done);
            });
          }
        );

        wss.on('connection', () => {
          done(new Error("Unexpected 'connection' event"));
        });
      });

      it('can reject client asynchronously w/ status code', (done) => {
        const wss = new WebSocket.Server(
          {
            verifyClient: (info, cb) => process.nextTick(cb, false, 404),
            port: 0
          },
          () => {
            const req = http.get({
              port: wss.address().port,
              headers: {
                Connection: 'Upgrade',
                Upgrade: 'websocket',
                'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ==',
                'Sec-WebSocket-Version': 8
              }
            });

            req.on('response', (res) => {
              assert.strictEqual(res.statusCode, 404);
              wss.close(done);
            });
          }
        );

        wss.on('connection', () => {
          done(new Error("Unexpected 'connection' event"));
        });
      });

      it('can reject client asynchronously w/ custom headers', (done) => {
        const wss = new WebSocket.Server(
          {
            verifyClient: (info, cb) => {
              process.nextTick(cb, false, 503, '', { 'Retry-After': 120 });
            },
            port: 0
          },
          () => {
            const req = http.get({
              port: wss.address().port,
              headers: {
                Connection: 'Upgrade',
                Upgrade: 'websocket',
                'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ==',
                'Sec-WebSocket-Version': 8
              }
            });

            req.on('response', (res) => {
              assert.strictEqual(res.statusCode, 503);
              assert.strictEqual(res.headers['retry-after'], '120');
              wss.close(done);
            });
          }
        );

        wss.on('connection', () => {
          done(new Error("Unexpected 'connection' event"));
        });
      });
    });

    it("doesn't emit the 'connection' event if socket is closed prematurely", (done) => {
      const server = http.createServer();

      server.listen(0, () => {
        const wss = new WebSocket.Server({
          verifyClient: ({ req: { socket } }, cb) => {
            assert.strictEqual(socket.readable, true);
            assert.strictEqual(socket.writable, true);

            socket.on('end', () => {
              assert.strictEqual(socket.readable, false);
              assert.strictEqual(socket.writable, true);
              cb(true);
            });
          },
          server
        });

        wss.on('connection', () => {
          done(new Error("Unexpected 'connection' event"));
        });

        const socket = net.connect(
          {
            port: server.address().port,
            allowHalfOpen: true
          },
          () => {
            socket.end(
              [
                'GET / HTTP/1.1',
                'Host: localhost',
                'Upgrade: websocket',
                'Connection: Upgrade',
                'Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==',
                'Sec-WebSocket-Version: 13',
                '\r\n'
              ].join('\r\n')
            );
          }
        );

        socket.on('end', () => {
          wss.close();
          server.close(done);
        });
      });
    });

    it('handles data passed along with the upgrade request', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const req = http.request({
          port: wss.address().port,
          headers: {
            Connection: 'Upgrade',
            Upgrade: 'websocket',
            'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ==',
            'Sec-WebSocket-Version': 13
          }
        });

        const list = Sender.frame(Buffer.from('Hello'), {
          fin: true,
          rsv1: false,
          opcode: 0x01,
          mask: true,
          readOnly: false
        });

        req.write(Buffer.concat(list));
        req.end();
      });

      wss.on('connection', (ws) => {
        ws.on('message', (data, isBinary) => {
          assert.deepStrictEqual(data, Buffer.from('Hello'));
          assert.ok(!isBinary);
          wss.close(done);
        });
      });
    });

    describe('`handleProtocols`', () => {
      it('allows to select a subprotocol', (done) => {
        const handleProtocols = (protocols, request) => {
          assert.ok(request instanceof http.IncomingMessage);
          assert.strictEqual(request.url, '/');
          return Array.from(protocols).pop();
        };
        const wss = new WebSocket.Server({ handleProtocols, port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`, [
            'foo',
            'bar'
          ]);

          ws.on('open', () => {
            assert.strictEqual(ws.protocol, 'bar');
            wss.close(done);
          });
        });

        wss.on('connection', (ws) => {
          ws.close();
        });
      });
    });

    it("emits the 'headers' event", (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(
          `ws://localhost:${wss.address().port}?foo=bar`
        );

        ws.on('open', ws.close);
      });

      wss.on('headers', (headers, request) => {
        assert.deepStrictEqual(headers.slice(0, 3), [
          'HTTP/1.1 101 Switching Protocols',
          'Upgrade: websocket',
          'Connection: Upgrade'
        ]);
        assert.ok(request instanceof http.IncomingMessage);
        assert.strictEqual(request.url, '/?foo=bar');

        wss.on('connection', () => wss.close(done));
      });
    });
  });

  describe('permessage-deflate', () => {
    it('is disabled by default', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', ws.close);
      });

      wss.on('connection', (ws, req) => {
        assert.strictEqual(
          req.headers['sec-websocket-extensions'],
          'permessage-deflate; client_max_window_bits'
        );
        assert.strictEqual(ws.extensions, '');
        wss.close(done);
      });
    });

    it('uses configuration options', (done) => {
      const wss = new WebSocket.Server(
        {
          perMessageDeflate: { clientMaxWindowBits: 8 },
          port: 0
        },
        () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          ws.on('upgrade', (res) => {
            assert.strictEqual(
              res.headers['sec-websocket-extensions'],
              'permessage-deflate; client_max_window_bits=8'
            );

            wss.close(done);
          });
        }
      );

      wss.on('connection', (ws) => {
        ws.close();
      });
    });
  });
});
```

## File: `test/websocket.integration.js`
```javascript
'use strict';

const assert = require('assert');

const WebSocket = require('..');

describe('WebSocket', () => {
  it('communicates successfully with echo service (ws)', (done) => {
    const ws = new WebSocket('ws://websocket-echo.com/', {
      protocolVersion: 13
    });

    let dataReceived = false;

    ws.on('open', () => {
      ws.send('hello');
    });

    ws.on('close', () => {
      assert.ok(dataReceived);
      done();
    });

    ws.on('message', (message, isBinary) => {
      dataReceived = true;
      assert.ok(!isBinary);
      assert.strictEqual(message.toString(), 'hello');
      ws.close();
    });
  });

  it('communicates successfully with echo service (wss)', (done) => {
    const ws = new WebSocket('wss://websocket-echo.com/', {
      protocolVersion: 13
    });

    let dataReceived = false;

    ws.on('open', () => {
      ws.send('hello');
    });

    ws.on('close', () => {
      assert.ok(dataReceived);
      done();
    });

    ws.on('message', (message, isBinary) => {
      dataReceived = true;
      assert.ok(!isBinary);
      assert.strictEqual(message.toString(), 'hello');
      ws.close();
    });
  });
});
```

## File: `test/websocket.test.js`
```javascript
/* eslint no-unused-vars: ["error", { "varsIgnorePattern": "^ws$" }] */

'use strict';

const assert = require('assert');
const crypto = require('crypto');
const https = require('https');
const http = require('http');
const path = require('path');
const net = require('net');
const tls = require('tls');
const os = require('os');
const fs = require('fs');
const { getDefaultHighWaterMark } = require('stream');
const { URL } = require('url');

const Sender = require('../lib/sender');
const WebSocket = require('..');
const {
  CloseEvent,
  ErrorEvent,
  Event,
  MessageEvent
} = require('../lib/event-target');
const {
  EMPTY_BUFFER,
  GUID,
  hasBlob,
  kListener,
  NOOP
} = require('../lib/constants');

const highWaterMark = getDefaultHighWaterMark
  ? getDefaultHighWaterMark(false)
  : 16 * 1024;

class CustomAgent extends http.Agent {
  addRequest() {}
}

describe('WebSocket', () => {
  describe('#ctor', () => {
    it('throws an error when using an invalid url', () => {
      assert.throws(
        () => new WebSocket('foo'),
        /^SyntaxError: Invalid URL: foo$/
      );

      assert.throws(
        () => new WebSocket('bad-scheme://websocket-echo.com'),
        (err) => {
          assert.strictEqual(
            err.message,
            'The URL\'s protocol must be one of "ws:", "wss:", ' +
              '"http:", "https:", or "ws+unix:"'
          );

          return true;
        }
      );

      assert.throws(
        () => new WebSocket('ws+unix:'),
        /^SyntaxError: The URL's pathname is empty$/
      );

      assert.throws(
        () => new WebSocket('wss://websocket-echo.com#foo'),
        /^SyntaxError: The URL contains a fragment identifier$/
      );
    });

    it('throws an error if a subprotocol is invalid or duplicated', () => {
      for (const subprotocol of [null, '', 'a,b', ['a', 'a']]) {
        assert.throws(
          () => new WebSocket('ws://localhost', subprotocol),
          /^SyntaxError: An invalid or duplicated subprotocol was specified$/
        );
      }
    });

    it('accepts `url.URL` objects as url', (done) => {
      const agent = new http.Agent();

      agent.addRequest = (req, opts) => {
        assert.strictEqual(opts.host, '::1');
        assert.strictEqual(req.path, '/');
        done();
      };

      const ws = new WebSocket(new URL('ws://[::1]'), { agent });
    });

    it('allows the http scheme', (done) => {
      const agent = new CustomAgent();

      agent.addRequest = (req, opts) => {
        assert.strictEqual(opts.host, 'localhost');
        assert.strictEqual(opts.port, 80);
        done();
      };

      const ws = new WebSocket('http://localhost', { agent });
    });

    it('allows the https scheme', (done) => {
      const agent = new https.Agent();

      agent.addRequest = (req, opts) => {
        assert.strictEqual(opts.host, 'localhost');
        assert.strictEqual(opts.port, 443);
        done();
      };

      const ws = new WebSocket('https://localhost', { agent });
    });

    describe('options', () => {
      it('accepts the `options` object as 3rd argument', () => {
        const agent = new http.Agent();
        let count = 0;
        let ws;

        agent.addRequest = (req) => {
          assert.strictEqual(
            req.getHeader('sec-websocket-protocol'),
            undefined
          );
          count++;
        };

        ws = new WebSocket('ws://localhost', undefined, { agent });
        ws = new WebSocket('ws://localhost', [], { agent });

        assert.strictEqual(count, 2);
      });

      it('accepts the `maxPayload` option', (done) => {
        const maxPayload = 20480;
        const wss = new WebSocket.Server(
          {
            perMessageDeflate: true,
            port: 0
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
              perMessageDeflate: true,
              maxPayload
            });

            ws.on('open', () => {
              assert.strictEqual(ws._receiver._maxPayload, maxPayload);
              assert.strictEqual(
                ws._receiver._extensions['permessage-deflate']._maxPayload,
                maxPayload
              );
              wss.close(done);
            });
          }
        );

        wss.on('connection', (ws) => {
          ws.close();
        });
      });

      it('throws an error when using an invalid `protocolVersion`', () => {
        assert.throws(
          () => new WebSocket('ws://localhost', { protocolVersion: 1000 }),
          /^RangeError: Unsupported protocol version: 1000 \(supported versions: 8, 13\)$/
        );
      });

      it('honors the `generateMask` option', (done) => {
        const data = Buffer.from('foo');
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
            generateMask() {}
          });

          ws.on('open', () => {
            ws.send(data);
          });

          ws.on('close', (code, reason) => {
            assert.strictEqual(code, 1005);
            assert.deepStrictEqual(reason, EMPTY_BUFFER);

            wss.close(done);
          });
        });

        wss.on('connection', (ws) => {
          const chunks = [];

          ws._socket.prependListener('data', (chunk) => {
            chunks.push(chunk);
          });

          ws.on('message', (message) => {
            assert.deepStrictEqual(message, data);
            assert.deepStrictEqual(
              Buffer.concat(chunks).slice(2, 6),
              Buffer.alloc(4)
            );

            ws.close();
          });
        });
      });

      it('honors the `autoPong` option', (done) => {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
            autoPong: false
          });

          ws.on('ping', () => {
            ws.close();
          });

          ws.on('close', () => {
            wss.close(done);
          });
        });

        wss.on('connection', (ws) => {
          ws.on('pong', () => {
            done(new Error("Unexpected 'pong' event"));
          });

          ws.ping();
        });
      });

      it('honors the `closeTimeout` option', (done) => {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const closeTimeout = 1000;
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
            closeTimeout
          });

          ws.on('open', () => {
            ws.close();
            assert.strictEqual(ws._closeTimer._idleTimeout, closeTimeout);
          });

          ws.on('close', () => {
            wss.close(done);
          });
        });
      });
    });
  });

  describe('Constants', () => {
    const readyStates = {
      CONNECTING: 0,
      OPEN: 1,
      CLOSING: 2,
      CLOSED: 3
    };

    Object.keys(readyStates).forEach((state) => {
      describe(`\`${state}\``, () => {
        it('is enumerable property of class', () => {
          const descriptor = Object.getOwnPropertyDescriptor(WebSocket, state);

          assert.deepStrictEqual(descriptor, {
            configurable: false,
            enumerable: true,
            value: readyStates[state],
            writable: false
          });
        });

        it('is enumerable property of prototype', () => {
          const descriptor = Object.getOwnPropertyDescriptor(
            WebSocket.prototype,
            state
          );

          assert.deepStrictEqual(descriptor, {
            configurable: false,
            enumerable: true,
            value: readyStates[state],
            writable: false
          });
        });
      });
    });
  });

  describe('Attributes', () => {
    describe('`binaryType`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          WebSocket.prototype,
          'binaryType'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set !== undefined);
      });

      it("defaults to 'nodebuffer'", () => {
        const ws = new WebSocket('ws://localhost', {
          agent: new CustomAgent()
        });

        assert.strictEqual(ws.binaryType, 'nodebuffer');
      });

      it("can be changed to 'arraybuffer' or 'fragments'", () => {
        const ws = new WebSocket('ws://localhost', {
          agent: new CustomAgent()
        });

        ws.binaryType = 'arraybuffer';
        assert.strictEqual(ws.binaryType, 'arraybuffer');

        ws.binaryType = 'foo';
        assert.strictEqual(ws.binaryType, 'arraybuffer');

        ws.binaryType = 'fragments';
        assert.strictEqual(ws.binaryType, 'fragments');

        ws.binaryType = '';
        assert.strictEqual(ws.binaryType, 'fragments');

        ws.binaryType = 'nodebuffer';
        assert.strictEqual(ws.binaryType, 'nodebuffer');
      });
    });

    describe('`bufferedAmount`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          WebSocket.prototype,
          'bufferedAmount'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });

      it('defaults to zero', () => {
        const ws = new WebSocket('ws://localhost', {
          agent: new CustomAgent()
        });

        assert.strictEqual(ws.bufferedAmount, 0);
      });

      it('defaults to zero upon "open"', (done) => {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          ws.onopen = () => {
            assert.strictEqual(ws.bufferedAmount, 0);
            wss.close(done);
          };
        });

        wss.on('connection', (ws) => {
          ws.close();
        });
      });

      it('takes into account the data in the sender queue', (done) => {
        const wss = new WebSocket.Server(
          {
            perMessageDeflate: true,
            port: 0
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
              perMessageDeflate: { threshold: 0 }
            });

            ws.on('open', () => {
              ws.send('foo');

              assert.strictEqual(ws.bufferedAmount, 3);

              ws.send('bar', (err) => {
                assert.ifError(err);
                assert.strictEqual(ws.bufferedAmount, 0);
                wss.close(done);
              });

              assert.strictEqual(ws.bufferedAmount, 6);
            });
          }
        );

        wss.on('connection', (ws) => {
          ws.close();
        });
      });

      it('takes into account the data in the socket queue', (done) => {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        });

        wss.on('connection', (ws) => {
          const data = Buffer.alloc(1024, 61);

          while (ws.bufferedAmount === 0) {
            ws.send(data);
          }

          assert.ok(ws.bufferedAmount > 0);
          assert.strictEqual(
            ws.bufferedAmount,
            ws._socket._writableState.length
          );

          ws.on('close', () => wss.close(done));
          ws.close();
        });
      });
    });

    describe('`extensions`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          WebSocket.prototype,
          'bufferedAmount'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });

      it('exposes the negotiated extensions names (1/2)', (done) => {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          assert.strictEqual(ws.extensions, '');

          ws.on('open', () => {
            assert.strictEqual(ws.extensions, '');
            ws.on('close', () => wss.close(done));
          });
        });

        wss.on('connection', (ws) => {
          assert.strictEqual(ws.extensions, '');
          ws.close();
        });
      });

      it('exposes the negotiated extensions names (2/2)', (done) => {
        const wss = new WebSocket.Server(
          {
            perMessageDeflate: true,
            port: 0
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

            assert.strictEqual(ws.extensions, '');

            ws.on('open', () => {
              assert.strictEqual(ws.extensions, 'permessage-deflate');
              ws.on('close', () => wss.close(done));
            });
          }
        );

        wss.on('connection', (ws) => {
          assert.strictEqual(ws.extensions, 'permessage-deflate');
          ws.close();
        });
      });
    });

    describe('`isPaused`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          WebSocket.prototype,
          'isPaused'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });

      it('indicates whether the websocket is paused', (done) => {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          ws.on('open', () => {
            ws.pause();
            assert.ok(ws.isPaused);

            ws.resume();
            assert.ok(!ws.isPaused);

            ws.close();
            wss.close(done);
          });

          assert.ok(!ws.isPaused);
        });
      });
    });

    describe('`protocol`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          WebSocket.prototype,
          'protocol'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });

      it('exposes the subprotocol selected by the server', (done) => {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const port = wss.address().port;
          const ws = new WebSocket(`ws://localhost:${port}`, 'foo');

          assert.strictEqual(ws.extensions, '');

          ws.on('open', () => {
            assert.strictEqual(ws.protocol, 'foo');
            ws.on('close', () => wss.close(done));
          });
        });

        wss.on('connection', (ws) => {
          assert.strictEqual(ws.protocol, 'foo');
          ws.close();
        });
      });
    });

    describe('`readyState`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          WebSocket.prototype,
          'readyState'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });

      it('defaults to `CONNECTING`', () => {
        const ws = new WebSocket('ws://localhost', {
          agent: new CustomAgent()
        });

        assert.strictEqual(ws.readyState, WebSocket.CONNECTING);
      });

      it('is set to `OPEN` once connection is established', (done) => {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          ws.on('open', () => {
            assert.strictEqual(ws.readyState, WebSocket.OPEN);
            ws.close();
          });

          ws.on('close', () => wss.close(done));
        });
      });

      it('is set to `CLOSED` once connection is closed', (done) => {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          ws.on('close', () => {
            assert.strictEqual(ws.readyState, WebSocket.CLOSED);
            wss.close(done);
          });

          ws.on('open', () => ws.close(1001));
        });
      });

      it('is set to `CLOSED` once connection is terminated', (done) => {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          ws.on('close', () => {
            assert.strictEqual(ws.readyState, WebSocket.CLOSED);
            wss.close(done);
          });

          ws.on('open', () => ws.terminate());
        });
      });
    });

    describe('`url`', () => {
      it('is enumerable and configurable', () => {
        const descriptor = Object.getOwnPropertyDescriptor(
          WebSocket.prototype,
          'url'
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set === undefined);
      });

      it('exposes the server url', () => {
        const schemes = new Map([
          ['ws', 'ws'],
          ['wss', 'wss'],
          ['http', 'ws'],
          ['https', 'wss']
        ]);

        for (const [key, value] of schemes) {
          const ws = new WebSocket(`${key}://localhost/`, { lookup() {} });

          assert.strictEqual(ws.url, `${value}://localhost/`);
        }
      });
    });
  });

  describe('Events', () => {
    it("emits an 'error' event if an error occurs (1/2)", (done) => {
      let clientCloseEventEmitted = false;
      let serverClientCloseEventEmitted = false;

      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('error', (err) => {
          assert.ok(err instanceof RangeError);
          assert.strictEqual(err.code, 'WS_ERR_INVALID_OPCODE');
          assert.strictEqual(
            err.message,
            'Invalid WebSocket frame: invalid opcode 5'
          );

          ws.on('close', (code, reason) => {
            assert.strictEqual(code, 1006);
            assert.strictEqual(reason, EMPTY_BUFFER);

            clientCloseEventEmitted = true;
            if (serverClientCloseEventEmitted) wss.close(done);
          });
        });
      });

      wss.on('connection', (ws) => {
        ws.on('close', (code, reason) => {
          assert.strictEqual(code, 1002);
          assert.deepStrictEqual(reason, EMPTY_BUFFER);

          serverClientCloseEventEmitted = true;
          if (clientCloseEventEmitted) wss.close(done);
        });

        ws._socket.write(Buffer.from([0x85, 0x00]));
      });
    });

    it("emits an 'error' event if an error occurs (2/2)", function (done) {
      if (!fs.openAsBlob) return this.skip();

      const randomString = crypto.randomBytes(4).toString('hex');
      const file = path.join(os.tmpdir(), `ws-${randomString}.txt`);

      fs.writeFileSync(file, 'x'.repeat(64));

      fs.openAsBlob(file)
        .then((blob) => {
          fs.writeFileSync(file, 'x'.repeat(32));
          runTest(blob);
        })
        .catch(done);

      function runTest(blob) {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        });

        wss.on('connection', (ws) => {
          ws.send(blob);

          ws.on('error', (err) => {
            try {
              assert.ok(err instanceof DOMException);
              assert.strictEqual(err.name, 'NotReadableError');
              assert.strictEqual(err.message, 'The blob could not be read');
            } finally {
              fs.unlinkSync(file);
            }

            ws.on('close', () => {
              wss.close(done);
            });
          });
        });
      }
    });

    it("emits the 'error' event only once (1/2)", function (done) {
      if (!fs.openAsBlob) return this.skip();

      const randomString = crypto.randomBytes(4).toString('hex');
      const file = path.join(os.tmpdir(), `ws-${randomString}.txt`);

      fs.writeFileSync(file, 'x'.repeat(64));

      fs.openAsBlob(file)
        .then((blob) => {
          fs.writeFileSync(file, 'x'.repeat(32));
          runTest(blob);
        })
        .catch(done);

      function runTest(blob) {
        const wss = new WebSocket.Server(
          {
            perMessageDeflate: true,
            port: 0
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
              perMessageDeflate: { threshold: 0 }
            });

            ws.on('open', () => {
              ws.send('foo');
              ws.send(blob);
            });

            ws.on('error', (err) => {
              try {
                assert.ok(err instanceof RangeError);
                assert.strictEqual(err.code, 'WS_ERR_INVALID_OPCODE');
                assert.strictEqual(
                  err.message,
                  'Invalid WebSocket frame: invalid opcode 5'
                );
              } finally {
                fs.unlinkSync(file);
              }

              ws.on('close', () => {
                wss.close(done);
              });
            });
          }
        );

        wss.on('connection', (ws) => {
          ws._socket.write(Buffer.from([0x85, 0x00]));
        });
      }
    });

    it("emits the 'error' event only once (2/2)", function (done) {
      if (!fs.openAsBlob) return this.skip();

      const randomString = crypto.randomBytes(4).toString('hex');
      const file = path.join(os.tmpdir(), `ws-${randomString}.txt`);

      fs.writeFileSync(file, 'x'.repeat(64));

      fs.openAsBlob(file)
        .then((blob) => {
          fs.writeFileSync(file, 'x'.repeat(32));
          runTest(blob);
        })
        .catch(done);

      function runTest(blob) {
        const wss = new WebSocket.Server(
          {
            perMessageDeflate: true,
            port: 0
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

            ws.on('open', () => {
              ws.send(blob);
            });

            ws.on('error', (err) => {
              try {
                assert.ok(err instanceof DOMException);
                assert.strictEqual(err.name, 'NotReadableError');
                assert.strictEqual(err.message, 'The blob could not be read');
              } finally {
                fs.unlinkSync(file);
              }

              ws.on('close', () => {
                wss.close(done);
              });
            });
          }
        );

        wss.on('connection', (ws) => {
          const buf = Buffer.from('c10100'.repeat(5) + '8500', 'hex');

          ws._socket.write(buf);
        });
      }
    });

    it("does not emit 'error' after 'close'", function (done) {
      if (!fs.openAsBlob) return this.skip();

      const randomString = crypto.randomBytes(4).toString('hex');
      const file = path.join(os.tmpdir(), `ws-${randomString}.bin`);

      fs.writeFileSync(file, crypto.randomBytes(1024 * 1024));
      fs.openAsBlob(file).then(runTest).catch(done);

      function runTest(blob) {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          ws.on('open', () => {
            ws.send(blob, (err) => {
              try {
                assert.ok(err instanceof DOMException);
                assert.strictEqual(err.name, 'NotReadableError');
                assert.strictEqual(err.message, 'The blob could not be read');
              } catch (e) {
                ws.removeListener(onClose);
                throw e;
              } finally {
                fs.unlinkSync(file);
              }

              wss.close(done);
            });
          });

          ws.on('error', () => {
            done(new Error("Unexpected 'error' event"));
          });
          ws.on('close', onClose);

          function onClose() {
            fs.writeFileSync(file, crypto.randomBytes(32));
          }
        });

        wss.on('connection', (ws) => {
          ws._socket.end();
        });
      }
    });

    it('does not re-emit `net.Socket` errors', function (done) {
      //
      // `socket.resetAndDestroy()` is not available in Node.js < 16.17.0.
      //
      if (process.versions.modules < 93) return this.skip();

      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws._socket.on('error', (err) => {
            assert.ok(err instanceof Error);
            assert.strictEqual(err.code, 'ECONNRESET');
            ws.on('close', (code, message) => {
              assert.strictEqual(code, 1006);
              assert.strictEqual(message, EMPTY_BUFFER);
              wss.close(done);
            });
          });

          wss.clients.values().next().value._socket.resetAndDestroy();
        });
      });
    });

    it("emits an 'upgrade' event", (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        ws.on('upgrade', (res) => {
          assert.ok(res instanceof http.IncomingMessage);
          wss.close(done);
        });
      });

      wss.on('connection', (ws) => {
        ws.close();
      });
    });

    it("emits a 'ping' event", (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        ws.on('ping', () => wss.close(done));
      });

      wss.on('connection', (ws) => {
        ws.ping();
        ws.close();
      });
    });

    it("emits a 'pong' event", (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
        ws.on('pong', () => wss.close(done));
      });

      wss.on('connection', (ws) => {
        ws.pong();
        ws.close();
      });
    });

    it("emits a 'redirect' event", (done) => {
      const server = http.createServer();
      const wss = new WebSocket.Server({ noServer: true, path: '/foo' });

      server.once('upgrade', (req, socket) => {
        socket.end('HTTP/1.1 302 Found\r\nLocation: /foo\r\n\r\n');
        server.once('upgrade', (req, socket, head) => {
          wss.handleUpgrade(req, socket, head, (ws) => {
            ws.close();
          });
        });
      });

      server.listen(() => {
        const port = server.address().port;
        const ws = new WebSocket(`ws://localhost:${port}`, {
          followRedirects: true
        });

        ws.on('redirect', (url, req) => {
          assert.strictEqual(ws._redirects, 1);
          assert.strictEqual(url, `ws://localhost:${port}/foo`);
          assert.ok(req instanceof http.ClientRequest);

          ws.on('close', (code) => {
            assert.strictEqual(code, 1005);
            server.close(done);
          });
        });
      });
    });
  });

  describe('Connection establishing', () => {
    const server = http.createServer();

    beforeEach((done) => server.listen(0, done));
    afterEach((done) => server.close(done));

    it('fails if the Upgrade header field value cannot be read', (done) => {
      server.once('upgrade', (req, socket) => {
        socket.on('end', socket.end);
        socket.write(
          'HTTP/1.1 101 Switching Protocols\r\n' +
            'Connection: Upgrade\r\n' +
            'Upgrade: websocket\r\n' +
            '\r\n'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`);

      ws._req.maxHeadersCount = 1;

      ws.on('upgrade', (res) => {
        assert.deepStrictEqual(res.headers, { connection: 'Upgrade' });

        ws.on('error', (err) => {
          assert.ok(err instanceof Error);
          assert.strictEqual(err.message, 'Invalid Upgrade header');
          done();
        });
      });
    });

    it('fails if the Upgrade header field value is not "websocket"', (done) => {
      server.once('upgrade', (req, socket) => {
        socket.on('end', socket.end);
        socket.write(
          'HTTP/1.1 101 Switching Protocols\r\n' +
            'Connection: Upgrade\r\n' +
            'Upgrade: foo\r\n' +
            '\r\n'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`);

      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(err.message, 'Invalid Upgrade header');
        done();
      });
    });

    it('fails if the Sec-WebSocket-Accept header is invalid', (done) => {
      server.once('upgrade', (req, socket) => {
        socket.on('end', socket.end);
        socket.write(
          'HTTP/1.1 101 Switching Protocols\r\n' +
            'Upgrade: websocket\r\n' +
            'Connection: Upgrade\r\n' +
            'Sec-WebSocket-Accept: CxYS6+NgJSBG74mdgLvGscRvpns=\r\n' +
            '\r\n'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`);

      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(err.message, 'Invalid Sec-WebSocket-Accept header');
        done();
      });
    });

    it('close event is raised when server closes connection', (done) => {
      server.once('upgrade', (req, socket) => {
        const key = crypto
          .createHash('sha1')
          .update(req.headers['sec-websocket-key'] + GUID)
          .digest('base64');

        socket.end(
          'HTTP/1.1 101 Switching Protocols\r\n' +
            'Upgrade: websocket\r\n' +
            'Connection: Upgrade\r\n' +
            `Sec-WebSocket-Accept: ${key}\r\n` +
            '\r\n'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`);

      ws.on('close', (code, reason) => {
        assert.strictEqual(code, 1006);
        assert.strictEqual(reason, EMPTY_BUFFER);
        done();
      });
    });

    it('error is emitted if server aborts connection', (done) => {
      server.once('upgrade', (req, socket) => {
        socket.end(
          `HTTP/1.1 401 ${http.STATUS_CODES[401]}\r\n` +
            'Connection: close\r\n' +
            'Content-type: text/html\r\n' +
            `Content-Length: ${http.STATUS_CODES[401].length}\r\n` +
            '\r\n'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`);

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(err.message, 'Unexpected server response: 401');
        done();
      });
    });

    it('unexpected response can be read when sent by server', (done) => {
      server.once('upgrade', (req, socket) => {
        socket.end(
          `HTTP/1.1 401 ${http.STATUS_CODES[401]}\r\n` +
            'Connection: close\r\n' +
            'Content-type: text/html\r\n' +
            'Content-Length: 3\r\n' +
            '\r\n' +
            'foo'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`);

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', () => done(new Error("Unexpected 'error' event")));
      ws.on('unexpected-response', (req, res) => {
        assert.strictEqual(res.statusCode, 401);

        let data = '';

        res.on('data', (v) => {
          data += v;
        });

        res.on('end', () => {
          assert.strictEqual(data, 'foo');
          done();
        });
      });
    });

    it('request can be aborted when unexpected response is sent by server', (done) => {
      server.once('upgrade', (req, socket) => {
        socket.end(
          `HTTP/1.1 401 ${http.STATUS_CODES[401]}\r\n` +
            'Connection: close\r\n' +
            'Content-type: text/html\r\n' +
            'Content-Length: 3\r\n' +
            '\r\n' +
            'foo'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`);

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', () => done(new Error("Unexpected 'error' event")));
      ws.on('unexpected-response', (req, res) => {
        assert.strictEqual(res.statusCode, 401);

        res.on('end', done);
        req.abort();
      });
    });

    it('fails if the opening handshake timeout expires', (done) => {
      server.once('upgrade', (req, socket) => socket.on('end', socket.end));

      const port = server.address().port;
      const ws = new WebSocket(`ws://localhost:${port}`, {
        handshakeTimeout: 100
      });

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(err.message, 'Opening handshake has timed out');
        done();
      });
    });

    it('fails if an unexpected Sec-WebSocket-Extensions header is received', (done) => {
      server.once('upgrade', (req, socket) => {
        const key = crypto
          .createHash('sha1')
          .update(req.headers['sec-websocket-key'] + GUID)
          .digest('base64');

        socket.end(
          'HTTP/1.1 101 Switching Protocols\r\n' +
            'Upgrade: websocket\r\n' +
            'Connection: Upgrade\r\n' +
            `Sec-WebSocket-Accept: ${key}\r\n` +
            'Sec-WebSocket-Extensions: foo\r\n' +
            '\r\n'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`, {
        perMessageDeflate: false
      });

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(
          err.message,
          'Server sent a Sec-WebSocket-Extensions header but no extension ' +
            'was requested'
        );
        ws.on('close', () => done());
      });
    });

    it('fails if the Sec-WebSocket-Extensions header is invalid (1/2)', (done) => {
      server.once('upgrade', (req, socket) => {
        const key = crypto
          .createHash('sha1')
          .update(req.headers['sec-websocket-key'] + GUID)
          .digest('base64');

        socket.end(
          'HTTP/1.1 101 Switching Protocols\r\n' +
            'Upgrade: websocket\r\n' +
            'Connection: Upgrade\r\n' +
            `Sec-WebSocket-Accept: ${key}\r\n` +
            'Sec-WebSocket-Extensions: foo;=\r\n' +
            '\r\n'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`);

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(
          err.message,
          'Invalid Sec-WebSocket-Extensions header'
        );
        ws.on('close', () => done());
      });
    });

    it('fails if the Sec-WebSocket-Extensions header is invalid (2/2)', (done) => {
      server.once('upgrade', (req, socket) => {
        const key = crypto
          .createHash('sha1')
          .update(req.headers['sec-websocket-key'] + GUID)
          .digest('base64');

        socket.end(
          'HTTP/1.1 101 Switching Protocols\r\n' +
            'Upgrade: websocket\r\n' +
            'Connection: Upgrade\r\n' +
            `Sec-WebSocket-Accept: ${key}\r\n` +
            'Sec-WebSocket-Extensions: ' +
            'permessage-deflate; client_max_window_bits=7\r\n' +
            '\r\n'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`);

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(
          err.message,
          'Invalid Sec-WebSocket-Extensions header'
        );
        ws.on('close', () => done());
      });
    });

    it('fails if an unexpected extension is received (1/2)', (done) => {
      server.once('upgrade', (req, socket) => {
        const key = crypto
          .createHash('sha1')
          .update(req.headers['sec-websocket-key'] + GUID)
          .digest('base64');

        socket.end(
          'HTTP/1.1 101 Switching Protocols\r\n' +
            'Upgrade: websocket\r\n' +
            'Connection: Upgrade\r\n' +
            `Sec-WebSocket-Accept: ${key}\r\n` +
            'Sec-WebSocket-Extensions: foo\r\n' +
            '\r\n'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`);

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(
          err.message,
          'Server indicated an extension that was not requested'
        );
        ws.on('close', () => done());
      });
    });

    it('fails if an unexpected extension is received (2/2)', (done) => {
      server.once('upgrade', (req, socket) => {
        const key = crypto
          .createHash('sha1')
          .update(req.headers['sec-websocket-key'] + GUID)
          .digest('base64');

        socket.end(
          'HTTP/1.1 101 Switching Protocols\r\n' +
            'Upgrade: websocket\r\n' +
            'Connection: Upgrade\r\n' +
            `Sec-WebSocket-Accept: ${key}\r\n` +
            'Sec-WebSocket-Extensions: permessage-deflate,foo\r\n' +
            '\r\n'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`);

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(
          err.message,
          'Server indicated an extension that was not requested'
        );
        ws.on('close', () => done());
      });
    });

    it('fails if server sends a subprotocol when none was requested', (done) => {
      const wss = new WebSocket.Server({ server });

      wss.on('headers', (headers) => {
        headers.push('Sec-WebSocket-Protocol: foo');
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`);

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(
          err.message,
          'Server sent a subprotocol but none was requested'
        );
        ws.on('close', () => wss.close(done));
      });
    });

    it('fails if server sends an invalid subprotocol (1/2)', (done) => {
      const wss = new WebSocket.Server({
        handleProtocols: () => 'baz',
        server
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`, [
        'foo',
        'bar'
      ]);

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(err.message, 'Server sent an invalid subprotocol');
        ws.on('close', () => wss.close(done));
      });
    });

    it('fails if server sends an invalid subprotocol (2/2)', (done) => {
      server.once('upgrade', (req, socket) => {
        const key = crypto
          .createHash('sha1')
          .update(req.headers['sec-websocket-key'] + GUID)
          .digest('base64');

        socket.end(
          'HTTP/1.1 101 Switching Protocols\r\n' +
            'Upgrade: websocket\r\n' +
            'Connection: Upgrade\r\n' +
            `Sec-WebSocket-Accept: ${key}\r\n` +
            'Sec-WebSocket-Protocol:\r\n' +
            '\r\n'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`, [
        'foo',
        'bar'
      ]);

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(err.message, 'Server sent an invalid subprotocol');
        ws.on('close', () => done());
      });
    });

    it('fails if server sends no subprotocol', (done) => {
      const wss = new WebSocket.Server({
        handleProtocols() {},
        server
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`, [
        'foo',
        'bar'
      ]);

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(err.message, 'Server sent no subprotocol');
        ws.on('close', () => wss.close(done));
      });
    });

    it('honors the `createConnection` option', (done) => {
      const wss = new WebSocket.Server({ noServer: true, path: '/foo' });

      server.once('upgrade', (req, socket, head) => {
        assert.strictEqual(req.headers.host, 'google.com:22');
        wss.handleUpgrade(req, socket, head, NOOP);
      });

      const ws = new WebSocket('ws://google.com:22/foo', {
        createConnection: (options) => {
          assert.strictEqual(options.host, 'google.com');
          assert.strictEqual(options.port, '22');

          // Ignore the `options` argument, and use the correct hostname and
          // port to connect to the server.
          return net.createConnection({
            host: 'localhost',
            port: server.address().port
          });
        }
      });

      ws.on('open', () => {
        assert.strictEqual(ws.url, 'ws://google.com:22/foo');
        ws.on('close', () => done());
        ws.close();
      });
    });

    it('does not follow redirects by default', (done) => {
      server.once('upgrade', (req, socket) => {
        socket.end(
          'HTTP/1.1 301 Moved Permanently\r\n' +
            'Location: ws://localhost:8080\r\n' +
            '\r\n'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`);

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(err.message, 'Unexpected server response: 301');
        assert.strictEqual(ws._redirects, 0);
        ws.on('close', () => done());
      });
    });

    it('honors the `followRedirects` option', (done) => {
      const wss = new WebSocket.Server({ noServer: true, path: '/foo' });

      server.once('upgrade', (req, socket) => {
        socket.end('HTTP/1.1 302 Found\r\nLocation: /foo\r\n\r\n');
        server.once('upgrade', (req, socket, head) => {
          wss.handleUpgrade(req, socket, head, NOOP);
        });
      });

      const port = server.address().port;
      const ws = new WebSocket(`ws://localhost:${port}`, {
        followRedirects: true
      });

      ws.on('open', () => {
        assert.strictEqual(ws.url, `ws://localhost:${port}/foo`);
        assert.strictEqual(ws._redirects, 1);
        ws.on('close', () => done());
        ws.close();
      });
    });

    it('honors the `maxRedirects` option', (done) => {
      const onUpgrade = (req, socket) => {
        socket.end('HTTP/1.1 302 Found\r\nLocation: /\r\n\r\n');
      };

      server.on('upgrade', onUpgrade);

      const ws = new WebSocket(`ws://localhost:${server.address().port}`, {
        followRedirects: true,
        maxRedirects: 1
      });

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(err.message, 'Maximum redirects exceeded');
        assert.strictEqual(ws._redirects, 2);

        server.removeListener('upgrade', onUpgrade);
        ws.on('close', () => done());
      });
    });

    it('emits an error if the redirect URL is invalid (1/2)', (done) => {
      server.once('upgrade', (req, socket) => {
        socket.end('HTTP/1.1 302 Found\r\nLocation: ws://\r\n\r\n');
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`, {
        followRedirects: true
      });

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof SyntaxError);
        assert.strictEqual(err.message, 'Invalid URL: ws://');
        assert.strictEqual(ws._redirects, 1);

        ws.on('close', () => done());
      });
    });

    it('emits an error if the redirect URL is invalid (2/2)', (done) => {
      server.once('upgrade', (req, socket) => {
        socket.end(
          'HTTP/1.1 302 Found\r\nLocation: bad-scheme://localhost\r\n\r\n'
        );
      });

      const ws = new WebSocket(`ws://localhost:${server.address().port}`, {
        followRedirects: true
      });

      ws.on('open', () => done(new Error("Unexpected 'open' event")));
      ws.on('error', (err) => {
        assert.ok(err instanceof SyntaxError);
        assert.strictEqual(
          err.message,
          'The URL\'s protocol must be one of "ws:", "wss:", ' +
            '"http:", "https:", or "ws+unix:"'
        );
        assert.strictEqual(ws._redirects, 1);

        ws.on('close', () => done());
      });
    });

    it('uses the first url userinfo when following redirects', (done) => {
      const wss = new WebSocket.Server({ noServer: true, path: '/foo' });
      const authorization = 'Basic Zm9vOmJhcg==';

      server.once('upgrade', (req, socket) => {
        socket.end(
          'HTTP/1.1 302 Found\r\n' +
            `Location: ws://baz:qux@localhost:${port}/foo\r\n\r\n`
        );
        server.once('upgrade', (req, socket, head) => {
          wss.handleUpgrade(req, socket, head, (ws, req) => {
            assert.strictEqual(req.headers.authorization, authorization);
            ws.close();
          });
        });
      });

      const port = server.address().port;
      const ws = new WebSocket(`ws://foo:bar@localhost:${port}`, {
        followRedirects: true
      });

      assert.strictEqual(ws._req.getHeader('Authorization'), authorization);

      ws.on('close', (code) => {
        assert.strictEqual(code, 1005);
        assert.strictEqual(ws.url, `ws://baz:qux@localhost:${port}/foo`);
        assert.strictEqual(ws._redirects, 1);

        wss.close(done);
      });
    });

    describe('When moving away from a secure context', () => {
      function proxy(httpServer, httpsServer) {
        const server = net.createServer({ allowHalfOpen: true });

        server.on('connection', (socket) => {
          socket.on('readable', function read() {
            socket.removeListener('readable', read);

            const buf = socket.read(1);
            const target = buf[0] === 22 ? httpsServer : httpServer;

            socket.unshift(buf);
            target.emit('connection', socket);
          });
        });

        return server;
      }

      describe("If there is no 'redirect' event listener", () => {
        it('drops the `auth` option', (done) => {
          const httpServer = http.createServer();
          const httpsServer = https.createServer({
            cert: fs.readFileSync('test/fixtures/certificate.pem'),
            key: fs.readFileSync('test/fixtures/key.pem')
          });
          const server = proxy(httpServer, httpsServer);

          server.listen(() => {
            const port = server.address().port;

            httpsServer.on('upgrade', (req, socket) => {
              socket.on('error', NOOP);
              socket.end(
                'HTTP/1.1 302 Found\r\n' +
                  `Location: ws://localhost:${port}/\r\n\r\n`
              );
            });

            const wss = new WebSocket.Server({ server: httpServer });

            wss.on('connection', (ws, req) => {
              assert.strictEqual(req.headers.authorization, undefined);
              ws.close();
            });

            const ws = new WebSocket(`wss://localhost:${port}`, {
              auth: 'foo:bar',
              followRedirects: true,
              rejectUnauthorized: false
            });

            assert.strictEqual(
              ws._req.getHeader('Authorization'),
              'Basic Zm9vOmJhcg=='
            );

            ws.on('close', (code) => {
              assert.strictEqual(code, 1005);
              assert.strictEqual(ws.url, `ws://localhost:${port}/`);
              assert.strictEqual(ws._redirects, 1);

              server.close(done);
            });
          });
        });

        it('drops the Authorization and Cookie headers', (done) => {
          const httpServer = http.createServer();
          const httpsServer = https.createServer({
            cert: fs.readFileSync('test/fixtures/certificate.pem'),
            key: fs.readFileSync('test/fixtures/key.pem')
          });
          const server = proxy(httpServer, httpsServer);

          server.listen(() => {
            const port = server.address().port;

            httpsServer.on('upgrade', (req, socket) => {
              socket.on('error', NOOP);
              socket.end(
                'HTTP/1.1 302 Found\r\n' +
                  `Location: ws://localhost:${port}/\r\n\r\n`
              );
            });

            const headers = {
              authorization: 'Basic Zm9vOmJhcg==',
              cookie: 'foo=bar',
              host: 'foo'
            };

            const wss = new WebSocket.Server({ server: httpServer });

            wss.on('connection', (ws, req) => {
              assert.strictEqual(req.headers.authorization, undefined);
              assert.strictEqual(req.headers.cookie, undefined);
              assert.strictEqual(req.headers.host, headers.host);

              ws.close();
            });

            const ws = new WebSocket(`wss://localhost:${port}`, {
              followRedirects: true,
              headers,
              rejectUnauthorized: false
            });

            const firstRequest = ws._req;

            assert.strictEqual(
              firstRequest.getHeader('Authorization'),
              headers.authorization
            );
            assert.strictEqual(
              firstRequest.getHeader('Cookie'),
              headers.cookie
            );
            assert.strictEqual(firstRequest.getHeader('Host'), headers.host);

            ws.on('close', (code) => {
              assert.strictEqual(code, 1005);
              assert.strictEqual(ws.url, `ws://localhost:${port}/`);
              assert.strictEqual(ws._redirects, 1);

              server.close(done);
            });
          });
        });
      });

      describe("If there is at least one 'redirect' event listener", () => {
        it('does not drop any headers by default', (done) => {
          const httpServer = http.createServer();
          const httpsServer = https.createServer({
            cert: fs.readFileSync('test/fixtures/certificate.pem'),
            key: fs.readFileSync('test/fixtures/key.pem')
          });
          const server = proxy(httpServer, httpsServer);

          server.listen(() => {
            const port = server.address().port;

            httpsServer.on('upgrade', (req, socket) => {
              socket.on('error', NOOP);
              socket.end(
                'HTTP/1.1 302 Found\r\n' +
                  `Location: ws://localhost:${port}/\r\n\r\n`
              );
            });

            const headers = {
              authorization: 'Basic Zm9vOmJhcg==',
              cookie: 'foo=bar',
              host: 'foo'
            };

            const wss = new WebSocket.Server({ server: httpServer });

            wss.on('connection', (ws, req) => {
              assert.strictEqual(
                req.headers.authorization,
                headers.authorization
              );
              assert.strictEqual(req.headers.cookie, headers.cookie);
              assert.strictEqual(req.headers.host, headers.host);

              ws.close();
            });

            const ws = new WebSocket(`wss://localhost:${port}`, {
              followRedirects: true,
              headers,
              rejectUnauthorized: false
            });

            const firstRequest = ws._req;

            assert.strictEqual(
              firstRequest.getHeader('Authorization'),
              headers.authorization
            );
            assert.strictEqual(
              firstRequest.getHeader('Cookie'),
              headers.cookie
            );
            assert.strictEqual(firstRequest.getHeader('Host'), headers.host);

            ws.on('redirect', (url, req) => {
              assert.strictEqual(ws._redirects, 1);
              assert.strictEqual(url, `ws://localhost:${port}/`);
              assert.notStrictEqual(firstRequest, req);
              assert.strictEqual(
                req.getHeader('Authorization'),
                headers.authorization
              );
              assert.strictEqual(req.getHeader('Cookie'), headers.cookie);
              assert.strictEqual(req.getHeader('Host'), headers.host);

              ws.on('close', (code) => {
                assert.strictEqual(code, 1005);
                server.close(done);
              });
            });
          });
        });
      });
    });

    describe('When the redirect host is different', () => {
      describe("If there is no 'redirect' event listener", () => {
        it('drops the `auth` option', (done) => {
          const wss = new WebSocket.Server({ port: 0 }, () => {
            const port = wss.address().port;

            server.once('upgrade', (req, socket) => {
              socket.end(
                'HTTP/1.1 302 Found\r\n' +
                  `Location: ws://localhost:${port}/\r\n\r\n`
              );
            });

            const ws = new WebSocket(
              `ws://localhost:${server.address().port}`,
              {
                auth: 'foo:bar',
                followRedirects: true
              }
            );

            assert.strictEqual(
              ws._req.getHeader('Authorization'),
              'Basic Zm9vOmJhcg=='
            );

            ws.on('close', (code) => {
              assert.strictEqual(code, 1005);
              assert.strictEqual(ws.url, `ws://localhost:${port}/`);
              assert.strictEqual(ws._redirects, 1);

              wss.close(done);
            });
          });

          wss.on('connection', (ws, req) => {
            assert.strictEqual(req.headers.authorization, undefined);
            ws.close();
          });
        });

        it('drops the Authorization, Cookie and Host headers (1/4)', (done) => {
          // Test the `ws:` to `ws:` case.

          const wss = new WebSocket.Server({ port: 0 }, () => {
            const port = wss.address().port;

            server.once('upgrade', (req, socket) => {
              socket.end(
                'HTTP/1.1 302 Found\r\n' +
                  `Location: ws://localhost:${port}/\r\n\r\n`
              );
            });

            const headers = {
              authorization: 'Basic Zm9vOmJhcg==',
              cookie: 'foo=bar',
              host: 'foo'
            };

            const ws = new WebSocket(
              `ws://localhost:${server.address().port}`,
              { followRedirects: true, headers }
            );

            const firstRequest = ws._req;

            assert.strictEqual(
              firstRequest.getHeader('Authorization'),
              headers.authorization
            );
            assert.strictEqual(
              firstRequest.getHeader('Cookie'),
              headers.cookie
            );
            assert.strictEqual(firstRequest.getHeader('Host'), headers.host);

            ws.on('close', (code) => {
              assert.strictEqual(code, 1005);
              assert.strictEqual(ws.url, `ws://localhost:${port}/`);
              assert.strictEqual(ws._redirects, 1);

              wss.close(done);
            });
          });

          wss.on('connection', (ws, req) => {
            assert.strictEqual(req.headers.authorization, undefined);
            assert.strictEqual(req.headers.cookie, undefined);
            assert.strictEqual(
              req.headers.host,
              `localhost:${wss.address().port}`
            );

            ws.close();
          });
        });

        it('drops the Authorization, Cookie and Host headers (2/4)', (done) => {
          // Test the `ws:` to `ws+unix:` case.

          const randomString = crypto.randomBytes(4).toString('hex');
          const ipcPath =
            process.platform === 'win32'
              ? `\\\\.\\pipe\\ws-pipe-${randomString}`
              : path.join(os.tmpdir(), `ws-${randomString}.sock`);

          server.once('upgrade', (req, socket) => {
            socket.end(
              `HTTP/1.1 302 Found\r\nLocation: ws+unix:${ipcPath}\r\n\r\n`
            );
          });

          const redirectedServer = http.createServer();
          const wss = new WebSocket.Server({ server: redirectedServer });

          wss.on('connection', (ws, req) => {
            assert.strictEqual(req.headers.authorization, undefined);
            assert.strictEqual(req.headers.cookie, undefined);
            assert.strictEqual(req.headers.host, 'localhost');

            ws.close();
          });

          redirectedServer.listen(ipcPath, () => {
            const headers = {
              authorization: 'Basic Zm9vOmJhcg==',
              cookie: 'foo=bar',
              host: 'foo'
            };

            const ws = new WebSocket(
              `ws://localhost:${server.address().port}`,
              { followRedirects: true, headers }
            );

            const firstRequest = ws._req;

            assert.strictEqual(
              firstRequest.getHeader('Authorization'),
              headers.authorization
            );
            assert.strictEqual(
              firstRequest.getHeader('Cookie'),
              headers.cookie
            );
            assert.strictEqual(firstRequest.getHeader('Host'), headers.host);

            ws.on('close', (code) => {
              assert.strictEqual(code, 1005);
              assert.strictEqual(ws.url, `ws+unix:${ipcPath}`);
              assert.strictEqual(ws._redirects, 1);

              redirectedServer.close(done);
            });
          });
        });

        it('drops the Authorization, Cookie and Host headers (3/4)', (done) => {
          // Test the `ws+unix:` to `ws+unix:` case.

          const randomString1 = crypto.randomBytes(4).toString('hex');
          const randomString2 = crypto.randomBytes(4).toString('hex');
          let redirectingServerIpcPath;
          let redirectedServerIpcPath;

          if (process.platform === 'win32') {
            redirectingServerIpcPath = `\\\\.\\pipe\\ws-pipe-${randomString1}`;
            redirectedServerIpcPath = `\\\\.\\pipe\\ws-pipe-${randomString2}`;
          } else {
            redirectingServerIpcPath = path.join(
              os.tmpdir(),
              `ws-${randomString1}.sock`
            );
            redirectedServerIpcPath = path.join(
              os.tmpdir(),
              `ws-${randomString2}.sock`
            );
          }

          const redirectingServer = http.createServer();

          redirectingServer.on('upgrade', (req, socket) => {
            socket.end(
              'HTTP/1.1 302 Found\r\n' +
                `Location: ws+unix:${redirectedServerIpcPath}\r\n\r\n`
            );
          });

          const redirectedServer = http.createServer();
          const wss = new WebSocket.Server({ server: redirectedServer });

          wss.on('connection', (ws, req) => {
            assert.strictEqual(req.headers.authorization, undefined);
            assert.strictEqual(req.headers.cookie, undefined);
            assert.strictEqual(req.headers.host, 'localhost');

            ws.close();
          });

          redirectingServer.listen(redirectingServerIpcPath, listening);
          redirectedServer.listen(redirectedServerIpcPath, listening);

          let callCount = 0;

          function listening() {
            if (++callCount !== 2) return;

            const headers = {
              authorization: 'Basic Zm9vOmJhcg==',
              cookie: 'foo=bar',
              host: 'foo'
            };

            const ws = new WebSocket(`ws+unix:${redirectingServerIpcPath}`, {
              followRedirects: true,
              headers
            });

            const firstRequest = ws._req;

            assert.strictEqual(
              firstRequest.getHeader('Authorization'),
              headers.authorization
            );
            assert.strictEqual(
              firstRequest.getHeader('Cookie'),
              headers.cookie
            );
            assert.strictEqual(firstRequest.getHeader('Host'), headers.host);

            ws.on('close', (code) => {
              assert.strictEqual(code, 1005);
              assert.strictEqual(ws.url, `ws+unix:${redirectedServerIpcPath}`);
              assert.strictEqual(ws._redirects, 1);

              redirectingServer.close();
              redirectedServer.close(done);
            });
          }
        });

        it('drops the Authorization, Cookie and Host headers (4/4)', (done) => {
          // Test the `ws+unix:` to `ws:` case.

          const redirectingServer = http.createServer();
          const redirectedServer = http.createServer();
          const wss = new WebSocket.Server({ server: redirectedServer });

          wss.on('connection', (ws, req) => {
            assert.strictEqual(req.headers.authorization, undefined);
            assert.strictEqual(req.headers.cookie, undefined);
            assert.strictEqual(
              req.headers.host,
              `localhost:${redirectedServer.address().port}`
            );

            ws.close();
          });

          const randomString = crypto.randomBytes(4).toString('hex');
          const ipcPath =
            process.platform === 'win32'
              ? `\\\\.\\pipe\\ws-pipe-${randomString}`
              : path.join(os.tmpdir(), `ws-${randomString}.sock`);

          redirectingServer.listen(ipcPath, listening);
          redirectedServer.listen(0, listening);

          let callCount = 0;

          function listening() {
            if (++callCount !== 2) return;

            const port = redirectedServer.address().port;

            redirectingServer.on('upgrade', (req, socket) => {
              socket.end(
                `HTTP/1.1 302 Found\r\nLocation: ws://localhost:${port}\r\n\r\n`
              );
            });

            const headers = {
              authorization: 'Basic Zm9vOmJhcg==',
              cookie: 'foo=bar',
              host: 'foo'
            };

            const ws = new WebSocket(`ws+unix:${ipcPath}`, {
              followRedirects: true,
              headers
            });

            const firstRequest = ws._req;

            assert.strictEqual(
              firstRequest.getHeader('Authorization'),
              headers.authorization
            );
            assert.strictEqual(
              firstRequest.getHeader('Cookie'),
              headers.cookie
            );
            assert.strictEqual(firstRequest.getHeader('Host'), headers.host);

            ws.on('close', (code) => {
              assert.strictEqual(code, 1005);
              assert.strictEqual(ws.url, `ws://localhost:${port}/`);
              assert.strictEqual(ws._redirects, 1);

              redirectingServer.close();
              redirectedServer.close(done);
            });
          }
        });
      });

      describe("If there is at least one 'redirect' event listener", () => {
        it('does not drop any headers by default', (done) => {
          const headers = {
            authorization: 'Basic Zm9vOmJhcg==',
            cookie: 'foo=bar',
            host: 'foo'
          };

          const wss = new WebSocket.Server({ port: 0 }, () => {
            const port = wss.address().port;

            server.once('upgrade', (req, socket) => {
              socket.end(
                'HTTP/1.1 302 Found\r\n' +
                  `Location: ws://localhost:${port}/\r\n\r\n`
              );
            });

            const ws = new WebSocket(
              `ws://localhost:${server.address().port}`,
              { followRedirects: true, headers }
            );

            const firstRequest = ws._req;

            assert.strictEqual(
              firstRequest.getHeader('Authorization'),
              headers.authorization
            );
            assert.strictEqual(
              firstRequest.getHeader('Cookie'),
              headers.cookie
            );
            assert.strictEqual(firstRequest.getHeader('Host'), headers.host);

            ws.on('redirect', (url, req) => {
              assert.strictEqual(ws._redirects, 1);
              assert.strictEqual(url, `ws://localhost:${port}/`);
              assert.notStrictEqual(firstRequest, req);
              assert.strictEqual(
                req.getHeader('Authorization'),
                headers.authorization
              );
              assert.strictEqual(req.getHeader('Cookie'), headers.cookie);
              assert.strictEqual(req.getHeader('Host'), headers.host);

              ws.on('close', (code) => {
                assert.strictEqual(code, 1005);
                wss.close(done);
              });
            });
          });

          wss.on('connection', (ws, req) => {
            assert.strictEqual(
              req.headers.authorization,
              headers.authorization
            );
            assert.strictEqual(req.headers.cookie, headers.cookie);
            assert.strictEqual(req.headers.host, headers.host);
            ws.close();
          });
        });
      });
    });

    describe("In a listener of the 'redirect' event", () => {
      it('allows to abort the request without swallowing errors', (done) => {
        server.once('upgrade', (req, socket) => {
          socket.end('HTTP/1.1 302 Found\r\nLocation: /foo\r\n\r\n');
        });

        const port = server.address().port;
        const ws = new WebSocket(`ws://localhost:${port}`, {
          followRedirects: true
        });

        ws.on('redirect', (url, req) => {
          assert.strictEqual(ws._redirects, 1);
          assert.strictEqual(url, `ws://localhost:${port}/foo`);

          req.on('socket', () => {
            req.abort();
          });

          ws.on('error', (err) => {
            assert.ok(err instanceof Error);
            assert.strictEqual(err.message, 'socket hang up');

            ws.on('close', (code) => {
              assert.strictEqual(code, 1006);
              done();
            });
          });
        });
      });

      it('allows to remove headers', (done) => {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const port = wss.address().port;

          server.once('upgrade', (req, socket) => {
            socket.end(
              'HTTP/1.1 302 Found\r\n' +
                `Location: ws://localhost:${port}/\r\n\r\n`
            );
          });

          const headers = {
            authorization: 'Basic Zm9vOmJhcg==',
            cookie: 'foo=bar'
          };

          const ws = new WebSocket(`ws://localhost:${server.address().port}`, {
            followRedirects: true,
            headers
          });

          ws.on('redirect', (url, req) => {
            assert.strictEqual(ws._redirects, 1);
            assert.strictEqual(url, `ws://localhost:${port}/`);
            assert.strictEqual(
              req.getHeader('Authorization'),
              headers.authorization
            );
            assert.strictEqual(req.getHeader('Cookie'), headers.cookie);

            req.removeHeader('authorization');
            req.removeHeader('cookie');

            ws.on('close', (code) => {
              assert.strictEqual(code, 1005);
              wss.close(done);
            });
          });
        });

        wss.on('connection', (ws, req) => {
          assert.strictEqual(req.headers.authorization, undefined);
          assert.strictEqual(req.headers.cookie, undefined);
          ws.close();
        });
      });
    });
  });

  describe('#pause', () => {
    it('does nothing if `readyState` is `CONNECTING` or `CLOSED`', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        assert.strictEqual(ws.readyState, WebSocket.CONNECTING);
        assert.ok(!ws.isPaused);

        ws.pause();
        assert.ok(!ws.isPaused);

        ws.on('open', () => {
          ws.on('close', () => {
            assert.strictEqual(ws.readyState, WebSocket.CLOSED);

            ws.pause();
            assert.ok(!ws.isPaused);

            wss.close(done);
          });

          ws.close();
        });
      });
    });

    it('pauses the socket', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
      });

      wss.on('connection', (ws) => {
        assert.ok(!ws.isPaused);
        assert.ok(!ws._socket.isPaused());

        ws.pause();
        assert.ok(ws.isPaused);
        assert.ok(ws._socket.isPaused());

        ws.terminate();
        wss.close(done);
      });
    });
  });

  describe('#ping', () => {
    it('throws an error if `readyState` is `CONNECTING`', () => {
      const ws = new WebSocket('ws://localhost', {
        lookup() {}
      });

      assert.throws(
        () => ws.ping(),
        /^Error: WebSocket is not open: readyState 0 \(CONNECTING\)$/
      );

      assert.throws(
        () => ws.ping(NOOP),
        /^Error: WebSocket is not open: readyState 0 \(CONNECTING\)$/
      );
    });

    it('increases `bufferedAmount` if `readyState` is 2 or 3', (done) => {
      const ws = new WebSocket('ws://localhost', {
        lookup() {}
      });

      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(
          err.message,
          'WebSocket was closed before the connection was established'
        );

        assert.strictEqual(ws.readyState, WebSocket.CLOSING);
        assert.strictEqual(ws.bufferedAmount, 0);

        ws.ping('hi');
        assert.strictEqual(ws.bufferedAmount, 2);

        ws.ping();
        assert.strictEqual(ws.bufferedAmount, 2);

        ws.on('close', () => {
          assert.strictEqual(ws.readyState, WebSocket.CLOSED);

          ws.ping('hi');
          assert.strictEqual(ws.bufferedAmount, 4);

          ws.ping();
          assert.strictEqual(ws.bufferedAmount, 4);

          if (hasBlob) {
            ws.ping(new Blob(['hi']));
            assert.strictEqual(ws.bufferedAmount, 6);
          }

          done();
        });
      });

      ws.close();
    });

    it('calls the callback w/ an error if `readyState` is 2 or 3', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
      });

      wss.on('connection', (ws) => {
        ws.close();

        assert.strictEqual(ws.bufferedAmount, 0);

        ws.ping('hi', (err) => {
          assert.ok(err instanceof Error);
          assert.strictEqual(
            err.message,
            'WebSocket is not open: readyState 2 (CLOSING)'
          );
          assert.strictEqual(ws.bufferedAmount, 2);

          ws.on('close', () => {
            ws.ping((err) => {
              assert.ok(err instanceof Error);
              assert.strictEqual(
                err.message,
                'WebSocket is not open: readyState 3 (CLOSED)'
              );
              assert.strictEqual(ws.bufferedAmount, 2);

              wss.close(done);
            });
          });
        });
      });
    });

    it('can send a ping with no data', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.ping(() => {
            ws.ping();
            ws.close();
          });
        });
      });

      wss.on('connection', (ws) => {
        let pings = 0;
        ws.on('ping', (data) => {
          assert.ok(Buffer.isBuffer(data));
          assert.strictEqual(data.length, 0);
          if (++pings === 2) wss.close(done);
        });
      });
    });

    it('can send a ping with data', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.ping('hi', () => {
            ws.ping('hi', true);
            ws.close();
          });
        });
      });

      wss.on('connection', (ws) => {
        let pings = 0;
        ws.on('ping', (message) => {
          assert.strictEqual(message.toString(), 'hi');
          if (++pings === 2) wss.close(done);
        });
      });
    });

    it('can send numbers as ping payload', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.ping(0);
          ws.close();
        });
      });

      wss.on('connection', (ws) => {
        ws.on('ping', (message) => {
          assert.strictEqual(message.toString(), '0');
          wss.close(done);
        });
      });
    });

    it('throws an error if the data size is greater than 125 bytes', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          assert.throws(
            () => ws.ping(Buffer.alloc(126)),
            /^RangeError: The data size must not be greater than 125 bytes$/
          );

          wss.close(done);
        });
      });

      wss.on('connection', (ws) => {
        ws.close();
      });
    });
  });

  describe('#pong', () => {
    it('throws an error if `readyState` is `CONNECTING`', () => {
      const ws = new WebSocket('ws://localhost', {
        lookup() {}
      });

      assert.throws(
        () => ws.pong(),
        /^Error: WebSocket is not open: readyState 0 \(CONNECTING\)$/
      );

      assert.throws(
        () => ws.pong(NOOP),
        /^Error: WebSocket is not open: readyState 0 \(CONNECTING\)$/
      );
    });

    it('increases `bufferedAmount` if `readyState` is 2 or 3', (done) => {
      const ws = new WebSocket('ws://localhost', {
        lookup() {}
      });

      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(
          err.message,
          'WebSocket was closed before the connection was established'
        );

        assert.strictEqual(ws.readyState, WebSocket.CLOSING);
        assert.strictEqual(ws.bufferedAmount, 0);

        ws.pong('hi');
        assert.strictEqual(ws.bufferedAmount, 2);

        ws.pong();
        assert.strictEqual(ws.bufferedAmount, 2);

        ws.on('close', () => {
          assert.strictEqual(ws.readyState, WebSocket.CLOSED);

          ws.pong('hi');
          assert.strictEqual(ws.bufferedAmount, 4);

          ws.pong();
          assert.strictEqual(ws.bufferedAmount, 4);

          if (hasBlob) {
            ws.pong(new Blob(['hi']));
            assert.strictEqual(ws.bufferedAmount, 6);
          }

          done();
        });
      });

      ws.close();
    });

    it('calls the callback w/ an error if `readyState` is 2 or 3', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
      });

      wss.on('connection', (ws) => {
        ws.close();

        assert.strictEqual(ws.bufferedAmount, 0);

        ws.pong('hi', (err) => {
          assert.ok(err instanceof Error);
          assert.strictEqual(
            err.message,
            'WebSocket is not open: readyState 2 (CLOSING)'
          );
          assert.strictEqual(ws.bufferedAmount, 2);

          ws.on('close', () => {
            ws.pong((err) => {
              assert.ok(err instanceof Error);
              assert.strictEqual(
                err.message,
                'WebSocket is not open: readyState 3 (CLOSED)'
              );
              assert.strictEqual(ws.bufferedAmount, 2);

              wss.close(done);
            });
          });
        });
      });
    });

    it('can send a pong with no data', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.pong(() => {
            ws.pong();
            ws.close();
          });
        });
      });

      wss.on('connection', (ws) => {
        let pongs = 0;
        ws.on('pong', (data) => {
          assert.ok(Buffer.isBuffer(data));
          assert.strictEqual(data.length, 0);
          if (++pongs === 2) wss.close(done);
        });
      });
    });

    it('can send a pong with data', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.pong('hi', () => {
            ws.pong('hi', true);
            ws.close();
          });
        });
      });

      wss.on('connection', (ws) => {
        let pongs = 0;
        ws.on('pong', (message) => {
          assert.strictEqual(message.toString(), 'hi');
          if (++pongs === 2) wss.close(done);
        });
      });
    });

    it('can send numbers as pong payload', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.pong(0);
          ws.close();
        });
      });

      wss.on('connection', (ws) => {
        ws.on('pong', (message) => {
          assert.strictEqual(message.toString(), '0');
          wss.close(done);
        });
      });
    });

    it('throws an error if the data size is greater than 125 bytes', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          assert.throws(
            () => ws.pong(Buffer.alloc(126)),
            /^RangeError: The data size must not be greater than 125 bytes$/
          );

          wss.close(done);
        });
      });

      wss.on('connection', (ws) => {
        ws.close();
      });
    });

    it('is called automatically when a ping is received', (done) => {
      const buf = Buffer.from('hi');
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.ping(buf);
        });

        ws.on('pong', (data) => {
          assert.deepStrictEqual(data, buf);
          wss.close(done);
        });
      });

      wss.on('connection', (ws) => {
        ws.on('ping', (data) => {
          assert.deepStrictEqual(data, buf);
          ws.close();
        });
      });
    });
  });

  describe('#resume', () => {
    it('does nothing if `readyState` is `CONNECTING` or `CLOSED`', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        assert.strictEqual(ws.readyState, WebSocket.CONNECTING);
        assert.ok(!ws.isPaused);

        // Verify that no exception is thrown.
        ws.resume();

        ws.on('open', () => {
          ws.pause();
          assert.ok(ws.isPaused);

          ws.on('close', () => {
            assert.strictEqual(ws.readyState, WebSocket.CLOSED);

            ws.resume();
            assert.ok(ws.isPaused);

            wss.close(done);
          });

          ws.terminate();
        });
      });
    });

    it('resumes the socket', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
      });

      wss.on('connection', (ws) => {
        assert.ok(!ws.isPaused);
        assert.ok(!ws._socket.isPaused());

        ws.pause();
        assert.ok(ws.isPaused);
        assert.ok(ws._socket.isPaused());

        ws.resume();
        assert.ok(!ws.isPaused);
        assert.ok(!ws._socket.isPaused());

        ws.close();
        wss.close(done);
      });
    });
  });

  describe('#send', () => {
    it('throws an error if `readyState` is `CONNECTING`', () => {
      const ws = new WebSocket('ws://localhost', {
        lookup() {}
      });

      assert.throws(
        () => ws.send('hi'),
        /^Error: WebSocket is not open: readyState 0 \(CONNECTING\)$/
      );

      assert.throws(
        () => ws.send('hi', NOOP),
        /^Error: WebSocket is not open: readyState 0 \(CONNECTING\)$/
      );
    });

    it('increases `bufferedAmount` if `readyState` is 2 or 3', (done) => {
      const ws = new WebSocket('ws://localhost', {
        lookup() {}
      });

      ws.on('error', (err) => {
        assert.ok(err instanceof Error);
        assert.strictEqual(
          err.message,
          'WebSocket was closed before the connection was established'
        );

        assert.strictEqual(ws.readyState, WebSocket.CLOSING);
        assert.strictEqual(ws.bufferedAmount, 0);

        ws.send('hi');
        assert.strictEqual(ws.bufferedAmount, 2);

        ws.send();
        assert.strictEqual(ws.bufferedAmount, 2);

        ws.on('close', () => {
          assert.strictEqual(ws.readyState, WebSocket.CLOSED);

          ws.send('hi');
          assert.strictEqual(ws.bufferedAmount, 4);

          ws.send();
          assert.strictEqual(ws.bufferedAmount, 4);

          if (hasBlob) {
            ws.send(new Blob(['hi']));
            assert.strictEqual(ws.bufferedAmount, 6);
          }

          done();
        });
      });

      ws.close();
    });

    it('calls the callback w/ an error if `readyState` is 2 or 3', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
      });

      wss.on('connection', (ws) => {
        ws.close();

        assert.strictEqual(ws.bufferedAmount, 0);

        ws.send('hi', (err) => {
          assert.ok(err instanceof Error);
          assert.strictEqual(
            err.message,
            'WebSocket is not open: readyState 2 (CLOSING)'
          );
          assert.strictEqual(ws.bufferedAmount, 2);

          ws.on('close', () => {
            ws.send('hi', (err) => {
              assert.ok(err instanceof Error);
              assert.strictEqual(
                err.message,
                'WebSocket is not open: readyState 3 (CLOSED)'
              );
              assert.strictEqual(ws.bufferedAmount, 4);

              wss.close(done);
            });
          });
        });
      });
    });

    it('can send a big binary message', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const array = new Float32Array(1024 * 1024);

        for (let i = 0; i < array.length; i++) {
          array[i] = i / 5;
        }

        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => ws.send(array));
        ws.on('message', (msg, isBinary) => {
          assert.deepStrictEqual(msg, Buffer.from(array.buffer));
          assert.ok(isBinary);
          wss.close(done);
        });
      });

      wss.on('connection', (ws) => {
        ws.on('message', (msg, isBinary) => {
          assert.ok(isBinary);
          ws.send(msg);
          ws.close();
        });
      });
    });

    it('can send text data', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => ws.send('hi'));
        ws.on('message', (message, isBinary) => {
          assert.deepStrictEqual(message, Buffer.from('hi'));
          assert.ok(!isBinary);
          wss.close(done);
        });
      });

      wss.on('connection', (ws) => {
        ws.on('message', (msg, isBinary) => {
          ws.send(msg, { binary: isBinary });
          ws.close();
        });
      });
    });

    it('does not override the `fin` option', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.send('fragment', { fin: false });
          ws.send('fragment', { fin: true });
          ws.close();
        });
      });

      wss.on('connection', (ws) => {
        ws.on('message', (msg, isBinary) => {
          assert.deepStrictEqual(msg, Buffer.from('fragmentfragment'));
          assert.ok(!isBinary);
          wss.close(done);
        });
      });
    });

    it('sends numbers as strings', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.send(0);
          ws.close();
        });
      });

      wss.on('connection', (ws) => {
        ws.on('message', (msg, isBinary) => {
          assert.deepStrictEqual(msg, Buffer.from('0'));
          assert.ok(!isBinary);
          wss.close(done);
        });
      });
    });

    it('can send a `TypedArray`', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const array = new Float32Array(6);

        for (let i = 0; i < array.length; ++i) {
          array[i] = i / 2;
        }

        const partial = array.subarray(2, 5);
        const buf = Buffer.from(
          partial.buffer,
          partial.byteOffset,
          partial.byteLength
        );

        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.send(partial);
          ws.close();
        });

        ws.on('message', (message, isBinary) => {
          assert.deepStrictEqual(message, buf);
          assert.ok(isBinary);
          wss.close(done);
        });
      });

      wss.on('connection', (ws) => {
        ws.on('message', (msg, isBinary) => {
          assert.ok(isBinary);
          ws.send(msg);
        });
      });
    });

    it('can send an `ArrayBuffer`', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const array = new Float32Array(5);

        for (let i = 0; i < array.length; ++i) {
          array[i] = i / 2;
        }

        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.send(array.buffer);
          ws.close();
        });

        ws.onmessage = (event) => {
          assert.ok(event.data.equals(Buffer.from(array.buffer)));
          wss.close(done);
        };
      });

      wss.on('connection', (ws) => {
        ws.on('message', (msg, isBinary) => {
          assert.ok(isBinary);
          ws.send(msg);
        });
      });
    });

    it('can send a `Buffer`', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const buf = Buffer.from('foobar');
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.send(buf);
          ws.close();
        });

        ws.onmessage = (event) => {
          assert.deepStrictEqual(event.data, buf);
          wss.close(done);
        };
      });

      wss.on('connection', (ws) => {
        ws.on('message', (msg, isBinary) => {
          assert.ok(isBinary);
          ws.send(msg);
        });
      });
    });

    it('can send a `Blob`', function (done) {
      if (!hasBlob) return this.skip();

      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        const messages = [];

        ws.on('open', () => {
          ws.send(new Blob(['foo']));
          ws.send(new Blob(['bar']));
          ws.close();
        });

        ws.on('message', (message, isBinary) => {
          assert.ok(isBinary);
          messages.push(message.toString());

          if (messages.length === 2) {
            assert.deepStrictEqual(messages, ['foo', 'bar']);
            wss.close(done);
          }
        });
      });

      wss.on('connection', (ws) => {
        ws.on('message', (message, isBinary) => {
          assert.ok(isBinary);
          ws.send(message);
        });
      });
    });

    it('calls the callback when data is written out', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.send('hi', (err) => {
            assert.ifError(err);
            wss.close(done);
          });
        });
      });

      wss.on('connection', (ws) => {
        ws.close();
      });
    });

    it('calls the callback if the socket is forcibly closed', function (done) {
      if (!hasBlob) return this.skip();

      const called = [];
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.send(new Blob(['foo']), (err) => {
            called.push(1);

            assert.strictEqual(ws.readyState, WebSocket.CLOSING);
            assert.ok(err instanceof Error);
            assert.strictEqual(
              err.message,
              'The socket was closed while the blob was being read'
            );
          });
          ws.send('bar');
          ws.send('baz', (err) => {
            called.push(2);

            assert.strictEqual(ws.readyState, WebSocket.CLOSING);
            assert.ok(err instanceof Error);
            assert.strictEqual(
              err.message,
              'The socket was closed while the blob was being read'
            );
          });

          ws.terminate();
        });
      });

      wss.on('connection', (ws) => {
        ws.on('close', () => {
          assert.deepStrictEqual(called, [1, 2]);
          wss.close(done);
        });
      });
    });

    it('works when the `data` argument is falsy', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws.send();
          ws.close();
        });
      });

      wss.on('connection', (ws) => {
        ws.on('message', (message, isBinary) => {
          assert.strictEqual(message, EMPTY_BUFFER);
          assert.ok(isBinary);
          wss.close(done);
        });
      });
    });

    it('honors the `mask` option', (done) => {
      let clientCloseEventEmitted = false;
      let serverClientCloseEventEmitted = false;

      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => ws.send('hi', { mask: false }));
        ws.on('close', (code, reason) => {
          assert.strictEqual(code, 1002);
          assert.deepStrictEqual(reason, EMPTY_BUFFER);

          clientCloseEventEmitted = true;
          if (serverClientCloseEventEmitted) wss.close(done);
        });
      });

      wss.on('connection', (ws) => {
        const chunks = [];

        ws._socket.prependListener('data', (chunk) => {
          chunks.push(chunk);
        });

        ws.on('error', (err) => {
          assert.ok(err instanceof RangeError);
          assert.strictEqual(
            err.message,
            'Invalid WebSocket frame: MASK must be set'
          );
          assert.ok(
            Buffer.concat(chunks).slice(0, 2).equals(Buffer.from('8102', 'hex'))
          );

          ws.on('close', (code, reason) => {
            assert.strictEqual(code, 1006);
            assert.strictEqual(reason, EMPTY_BUFFER);

            serverClientCloseEventEmitted = true;
            if (clientCloseEventEmitted) wss.close(done);
          });
        });
      });
    });
  });

  describe('#close', () => {
    it('closes the connection if called while connecting (1/3)', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => done(new Error("Unexpected 'open' event")));
        ws.on('error', (err) => {
          assert.ok(err instanceof Error);
          assert.strictEqual(
            err.message,
            'WebSocket was closed before the connection was established'
          );
          ws.on('close', () => wss.close(done));
        });
        ws.close(1001);
      });
    });

    it('closes the connection if called while connecting (2/3)', (done) => {
      const wss = new WebSocket.Server(
        {
          verifyClient: (info, cb) => setTimeout(cb, 300, true),
          port: 0
        },
        () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          ws.on('open', () => done(new Error("Unexpected 'open' event")));
          ws.on('error', (err) => {
            assert.ok(err instanceof Error);
            assert.strictEqual(
              err.message,
              'WebSocket was closed before the connection was established'
            );
            ws.on('close', () => wss.close(done));
          });
          setTimeout(() => ws.close(1001), 150);
        }
      );
    });

    it('closes the connection if called while connecting (3/3)', (done) => {
      const server = http.createServer();

      server.listen(0, () => {
        const ws = new WebSocket(`ws://localhost:${server.address().port}`);

        ws.on('open', () => done(new Error("Unexpected 'open' event")));
        ws.on('error', (err) => {
          assert.ok(err instanceof Error);
          assert.strictEqual(
            err.message,
            'WebSocket was closed before the connection was established'
          );
          ws.on('close', () => {
            server.close(done);
          });
        });

        ws.on('unexpected-response', (req, res) => {
          assert.strictEqual(res.statusCode, 502);

          const chunks = [];

          res.on('data', (chunk) => {
            chunks.push(chunk);
          });

          res.on('end', () => {
            assert.strictEqual(Buffer.concat(chunks).toString(), 'foo');
            ws.close();
          });
        });
      });

      server.on('upgrade', (req, socket) => {
        socket.on('end', socket.end);

        socket.write(
          `HTTP/1.1 502 ${http.STATUS_CODES[502]}\r\n` +
            'Connection: keep-alive\r\n' +
            'Content-type: text/html\r\n' +
            'Content-Length: 3\r\n' +
            '\r\n' +
            'foo'
        );
      });
    });

    it('can be called from an error listener while connecting', (done) => {
      const server = net.createServer();

      server.on('connection', (socket) => {
        socket.on('end', socket.end);
        socket.resume();
        socket.write(Buffer.from('foo\r\n'));
      });

      server.listen(0, () => {
        const ws = new WebSocket(`ws://localhost:${server.address().port}`);

        ws.on('open', () => done(new Error("Unexpected 'open' event")));
        ws.on('error', (err) => {
          assert.ok(err instanceof Error);
          assert.strictEqual(err.code, 'HPE_INVALID_CONSTANT');
          ws.close();
          ws.on('close', () => {
            server.close(done);
          });
        });
      });
    });

    it("can be called from a listener of the 'redirect' event", (done) => {
      const server = http.createServer();

      server.once('upgrade', (req, socket) => {
        socket.end('HTTP/1.1 302 Found\r\nLocation: /foo\r\n\r\n');
      });

      server.listen(() => {
        const port = server.address().port;
        const ws = new WebSocket(`ws://localhost:${port}`, {
          followRedirects: true
        });

        ws.on('open', () => {
          done(new Error("Unexpected 'open' event"));
        });

        ws.on('error', (err) => {
          assert.ok(err instanceof Error);
          assert.strictEqual(
            err.message,
            'WebSocket was closed before the connection was established'
          );

          ws.on('close', (code) => {
            assert.strictEqual(code, 1006);
            server.close(done);
          });
        });

        ws.on('redirect', () => {
          ws.close();
        });
      });
    });

    it("can be called from a listener of the 'upgrade' event", (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => done(new Error("Unexpected 'open' event")));
        ws.on('error', (err) => {
          assert.ok(err instanceof Error);
          assert.strictEqual(
            err.message,
            'WebSocket was closed before the connection was established'
          );
          ws.on('close', () => wss.close(done));
        });
        ws.on('upgrade', () => ws.close());
      });
    });

    it('sends the close status code only when necessary', (done) => {
      let sent;
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => {
          ws._socket.once('data', (data) => {
            sent = data;
          });
        });
      });

      wss.on('connection', (ws) => {
        ws._socket.once('data', (received) => {
          assert.deepStrictEqual(
            received.slice(0, 2),
            Buffer.from([0x88, 0x80])
          );
          assert.deepStrictEqual(sent, Buffer.from([0x88, 0x00]));

          ws.on('close', (code, reason) => {
            assert.strictEqual(code, 1005);
            assert.strictEqual(reason, EMPTY_BUFFER);
            wss.close(done);
          });
        });
        ws.close();
      });
    });

    it('works when close reason is not specified', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => ws.close(1000));
      });

      wss.on('connection', (ws) => {
        ws.on('close', (code, message) => {
          assert.strictEqual(code, 1000);
          assert.deepStrictEqual(message, EMPTY_BUFFER);
          wss.close(done);
        });
      });
    });

    it('works when close reason is specified', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => ws.close(1000, 'some reason'));
      });

      wss.on('connection', (ws) => {
        ws.on('close', (code, message) => {
          assert.strictEqual(code, 1000);
          assert.deepStrictEqual(message, Buffer.from('some reason'));
          wss.close(done);
        });
      });
    });

    it('permits all buffered data to be delivered', (done) => {
      const wss = new WebSocket.Server(
        {
          perMessageDeflate: { threshold: 0 },
          port: 0
        },
        () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
          const messages = [];

          ws.on('message', (message, isBinary) => {
            assert.ok(!isBinary);
            messages.push(message.toString());
          });
          ws.on('close', (code) => {
            assert.strictEqual(code, 1005);
            assert.deepStrictEqual(messages, ['foo', 'bar', 'baz']);
            wss.close(done);
          });
        }
      );

      wss.on('connection', (ws) => {
        const callback = (err) => assert.ifError(err);

        ws.send('foo', callback);
        ws.send('bar', callback);
        ws.send('baz', callback);
        ws.close();
        ws.close();
      });
    });

    it('allows close code 1013', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('close', (code) => {
          assert.strictEqual(code, 1013);
          wss.close(done);
        });
      });

      wss.on('connection', (ws) => ws.close(1013));
    });

    it('allows close code 1014', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('close', (code) => {
          assert.strictEqual(code, 1014);
          wss.close(done);
        });
      });

      wss.on('connection', (ws) => ws.close(1014));
    });

    it('does nothing if `readyState` is `CLOSED`', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('close', (code) => {
          assert.strictEqual(code, 1005);
          assert.strictEqual(ws.readyState, WebSocket.CLOSED);
          ws.close();
          wss.close(done);
        });
      });

      wss.on('connection', (ws) => ws.close());
    });

    it('sets a timer for the closing handshake to complete', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('close', (code, reason) => {
          assert.strictEqual(code, 1000);
          assert.deepStrictEqual(reason, Buffer.from('some reason'));
          wss.close(done);
        });

        ws.on('open', () => {
          let callbackCalled = false;

          assert.strictEqual(ws._closeTimer, null);

          ws.send('foo', () => {
            callbackCalled = true;
          });

          ws.close(1000, 'some reason');

          //
          // Check that the close timer is set even if the `Sender.close()`
          // callback is not called.
          //
          assert.strictEqual(callbackCalled, false);
          assert.strictEqual(ws._closeTimer._idleTimeout, 30000);
        });
      });
    });
  });

  describe('#terminate', () => {
    it('closes the connection if called while connecting (1/2)', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => done(new Error("Unexpected 'open' event")));
        ws.on('error', (err) => {
          assert.ok(err instanceof Error);
          assert.strictEqual(
            err.message,
            'WebSocket was closed before the connection was established'
          );
          ws.on('close', () => wss.close(done));
        });
        ws.terminate();
      });
    });

    it('closes the connection if called while connecting (2/2)', (done) => {
      const wss = new WebSocket.Server(
        {
          verifyClient: (info, cb) => setTimeout(cb, 300, true),
          port: 0
        },
        () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          ws.on('open', () => done(new Error("Unexpected 'open' event")));
          ws.on('error', (err) => {
            assert.ok(err instanceof Error);
            assert.strictEqual(
              err.message,
              'WebSocket was closed before the connection was established'
            );
            ws.on('close', () => wss.close(done));
          });
          setTimeout(() => ws.terminate(), 150);
        }
      );
    });

    it('can be called from an error listener while connecting', (done) => {
      const server = net.createServer();

      server.on('connection', (socket) => {
        socket.on('end', socket.end);
        socket.resume();
        socket.write(Buffer.from('foo\r\n'));
      });

      server.listen(0, () => {
        const ws = new WebSocket(`ws://localhost:${server.address().port}`);

        ws.on('open', () => done(new Error("Unexpected 'open' event")));
        ws.on('error', (err) => {
          assert.ok(err instanceof Error);
          assert.strictEqual(err.code, 'HPE_INVALID_CONSTANT');
          ws.terminate();
          ws.on('close', () => {
            server.close(done);
          });
        });
      });
    });

    it("can be called from a listener of the 'redirect' event", (done) => {
      const server = http.createServer();

      server.once('upgrade', (req, socket) => {
        socket.end('HTTP/1.1 302 Found\r\nLocation: /foo\r\n\r\n');
      });

      server.listen(() => {
        const port = server.address().port;
        const ws = new WebSocket(`ws://localhost:${port}`, {
          followRedirects: true
        });

        ws.on('open', () => {
          done(new Error("Unexpected 'open' event"));
        });

        ws.on('error', (err) => {
          assert.ok(err instanceof Error);
          assert.strictEqual(
            err.message,
            'WebSocket was closed before the connection was established'
          );

          ws.on('close', (code) => {
            assert.strictEqual(code, 1006);
            server.close(done);
          });
        });

        ws.on('redirect', () => {
          ws.terminate();
        });
      });
    });

    it("can be called from a listener of the 'upgrade' event", (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('open', () => done(new Error("Unexpected 'open' event")));
        ws.on('error', (err) => {
          assert.ok(err instanceof Error);
          assert.strictEqual(
            err.message,
            'WebSocket was closed before the connection was established'
          );
          ws.on('close', () => wss.close(done));
        });
        ws.on('upgrade', () => ws.terminate());
      });
    });

    it('does nothing if `readyState` is `CLOSED`', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('close', (code) => {
          assert.strictEqual(code, 1006);
          assert.strictEqual(ws.readyState, WebSocket.CLOSED);
          ws.terminate();
          wss.close(done);
        });
      });

      wss.on('connection', (ws) => ws.terminate());
    });
  });

  describe('WHATWG API emulation', () => {
    it('supports the `on{close,error,message,open}` attributes', () => {
      for (const property of ['onclose', 'onerror', 'onmessage', 'onopen']) {
        const descriptor = Object.getOwnPropertyDescriptor(
          WebSocket.prototype,
          property
        );

        assert.strictEqual(descriptor.configurable, true);
        assert.strictEqual(descriptor.enumerable, true);
        assert.ok(descriptor.get !== undefined);
        assert.ok(descriptor.set !== undefined);
      }

      const ws = new WebSocket('ws://localhost', { agent: new CustomAgent() });

      assert.strictEqual(ws.onmessage, null);
      assert.strictEqual(ws.onclose, null);
      assert.strictEqual(ws.onerror, null);
      assert.strictEqual(ws.onopen, null);

      ws.onmessage = NOOP;
      ws.onerror = NOOP;
      ws.onclose = NOOP;
      ws.onopen = NOOP;

      assert.strictEqual(ws.onmessage, NOOP);
      assert.strictEqual(ws.onclose, NOOP);
      assert.strictEqual(ws.onerror, NOOP);
      assert.strictEqual(ws.onopen, NOOP);

      ws.onmessage = 'foo';

      assert.strictEqual(ws.onmessage, null);
      assert.strictEqual(ws.listenerCount('message'), 0);
    });

    it('works like the `EventEmitter` interface', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.onmessage = (messageEvent) => {
          assert.strictEqual(messageEvent.data, 'foo');
          ws.onclose = (closeEvent) => {
            assert.strictEqual(closeEvent.wasClean, true);
            assert.strictEqual(closeEvent.code, 1005);
            assert.strictEqual(closeEvent.reason, '');
            wss.close(done);
          };
          ws.close();
        };

        ws.onopen = () => ws.send('foo');
      });

      wss.on('connection', (ws) => {
        ws.on('message', (msg, isBinary) => {
          ws.send(msg, { binary: isBinary });
        });
      });
    });

    it("doesn't return listeners added with `on`", () => {
      const ws = new WebSocket('ws://localhost', { agent: new CustomAgent() });

      ws.on('open', NOOP);

      assert.deepStrictEqual(ws.listeners('open'), [NOOP]);
      assert.strictEqual(ws.onopen, null);
    });

    it("doesn't remove listeners added with `on`", () => {
      const ws = new WebSocket('ws://localhost', { agent: new CustomAgent() });

      ws.on('close', NOOP);
      ws.onclose = NOOP;

      let listeners = ws.listeners('close');

      assert.strictEqual(listeners.length, 2);
      assert.strictEqual(listeners[0], NOOP);
      assert.strictEqual(listeners[1][kListener], NOOP);

      ws.onclose = NOOP;

      listeners = ws.listeners('close');

      assert.strictEqual(listeners.length, 2);
      assert.strictEqual(listeners[0], NOOP);
      assert.strictEqual(listeners[1][kListener], NOOP);
    });

    it('supports the `addEventListener` method', () => {
      const events = [];
      const ws = new WebSocket('ws://localhost', { agent: new CustomAgent() });

      ws.addEventListener('foo', () => {});
      assert.strictEqual(ws.listenerCount('foo'), 0);

      function onOpen() {
        events.push('open');
        assert.strictEqual(ws.listenerCount('open'), 1);
      }

      ws.addEventListener('open', onOpen);
      ws.addEventListener('open', onOpen);

      assert.strictEqual(ws.listenerCount('open'), 1);

      const listener = {
        handleEvent() {
          events.push('message');
          assert.strictEqual(this, listener);
          assert.strictEqual(ws.listenerCount('message'), 0);
        }
      };

      ws.addEventListener('message', listener, { once: true });
      ws.addEventListener('message', listener);

      assert.strictEqual(ws.listenerCount('message'), 1);

      ws.addEventListener('close', NOOP);
      ws.onclose = NOOP;

      let listeners = ws.listeners('close');

      assert.strictEqual(listeners.length, 2);
      assert.strictEqual(listeners[0][kListener], NOOP);
      assert.strictEqual(listeners[1][kListener], NOOP);

      ws.onerror = NOOP;
      ws.addEventListener('error', NOOP);

      listeners = ws.listeners('error');

      assert.strictEqual(listeners.length, 2);
      assert.strictEqual(listeners[0][kListener], NOOP);
      assert.strictEqual(listeners[1][kListener], NOOP);

      ws.emit('open');
      ws.emit('message', EMPTY_BUFFER, false);

      assert.deepStrictEqual(events, ['open', 'message']);
    });

    it("doesn't return listeners added with `addEventListener`", () => {
      const ws = new WebSocket('ws://localhost', { agent: new CustomAgent() });

      ws.addEventListener('open', NOOP);

      const listeners = ws.listeners('open');

      assert.strictEqual(listeners.length, 1);
      assert.strictEqual(listeners[0][kListener], NOOP);

      assert.strictEqual(ws.onopen, null);
    });

    it("doesn't remove listeners added with `addEventListener`", () => {
      const ws = new WebSocket('ws://localhost', { agent: new CustomAgent() });

      ws.addEventListener('close', NOOP);
      ws.onclose = NOOP;

      let listeners = ws.listeners('close');

      assert.strictEqual(listeners.length, 2);
      assert.strictEqual(listeners[0][kListener], NOOP);
      assert.strictEqual(listeners[1][kListener], NOOP);

      ws.onclose = NOOP;

      listeners = ws.listeners('close');

      assert.strictEqual(listeners.length, 2);
      assert.strictEqual(listeners[0][kListener], NOOP);
      assert.strictEqual(listeners[1][kListener], NOOP);
    });

    it('supports the `removeEventListener` method', () => {
      const ws = new WebSocket('ws://localhost', { agent: new CustomAgent() });

      const listener = { handleEvent() {} };

      ws.addEventListener('message', listener);
      ws.addEventListener('open', NOOP);

      assert.strictEqual(ws.listeners('message')[0][kListener], listener);
      assert.strictEqual(ws.listeners('open')[0][kListener], NOOP);

      ws.removeEventListener('message', () => {});

      assert.strictEqual(ws.listeners('message')[0][kListener], listener);

      ws.removeEventListener('message', listener);
      ws.removeEventListener('open', NOOP);

      assert.strictEqual(ws.listenerCount('message'), 0);
      assert.strictEqual(ws.listenerCount('open'), 0);

      ws.addEventListener('message', NOOP, { once: true });
      ws.addEventListener('open', NOOP, { once: true });

      assert.strictEqual(ws.listeners('message')[0][kListener], NOOP);
      assert.strictEqual(ws.listeners('open')[0][kListener], NOOP);

      ws.removeEventListener('message', () => {});

      assert.strictEqual(ws.listeners('message')[0][kListener], NOOP);

      ws.removeEventListener('message', NOOP);
      ws.removeEventListener('open', NOOP);

      assert.strictEqual(ws.listenerCount('message'), 0);
      assert.strictEqual(ws.listenerCount('open'), 0);

      // Listeners not added with `websocket.addEventListener()`.
      ws.on('message', NOOP);

      assert.deepStrictEqual(ws.listeners('message'), [NOOP]);

      ws.removeEventListener('message', NOOP);

      assert.deepStrictEqual(ws.listeners('message'), [NOOP]);

      ws.onclose = NOOP;

      assert.strictEqual(ws.listeners('close')[0][kListener], NOOP);

      ws.removeEventListener('close', NOOP);

      assert.strictEqual(ws.listeners('close')[0][kListener], NOOP);
    });

    it('wraps text data in a `MessageEvent`', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.addEventListener('open', () => {
          ws.send('hi');
          ws.close();
        });

        ws.addEventListener('message', (event) => {
          assert.ok(event instanceof MessageEvent);
          assert.strictEqual(event.data, 'hi');
          wss.close(done);
        });
      });

      wss.on('connection', (ws) => {
        ws.on('message', (msg, isBinary) => {
          ws.send(msg, { binary: isBinary });
        });
      });
    });

    it('receives a `CloseEvent` when server closes (1000)', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.addEventListener('close', (event) => {
          assert.ok(event instanceof CloseEvent);
          assert.ok(event.wasClean);
          assert.strictEqual(event.reason, '');
          assert.strictEqual(event.code, 1000);
          wss.close(done);
        });
      });

      wss.on('connection', (ws) => ws.close(1000));
    });

    it('receives a `CloseEvent` when server closes (4000)', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.addEventListener('close', (event) => {
          assert.ok(event instanceof CloseEvent);
          assert.ok(event.wasClean);
          assert.strictEqual(event.reason, 'some daft reason');
          assert.strictEqual(event.code, 4000);
          wss.close(done);
        });
      });

      wss.on('connection', (ws) => ws.close(4000, 'some daft reason'));
    });

    it('sets `target` and `type` on events', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const err = new Error('forced');
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.addEventListener('open', (event) => {
          assert.ok(event instanceof Event);
          assert.strictEqual(event.type, 'open');
          assert.strictEqual(event.target, ws);
        });
        ws.addEventListener('message', (event) => {
          assert.ok(event instanceof MessageEvent);
          assert.strictEqual(event.type, 'message');
          assert.strictEqual(event.target, ws);
          ws.close();
        });
        ws.addEventListener('close', (event) => {
          assert.ok(event instanceof CloseEvent);
          assert.strictEqual(event.type, 'close');
          assert.strictEqual(event.target, ws);
          ws.emit('error', err);
        });
        ws.addEventListener('error', (event) => {
          assert.ok(event instanceof ErrorEvent);
          assert.strictEqual(event.message, 'forced');
          assert.strictEqual(event.type, 'error');
          assert.strictEqual(event.target, ws);
          assert.strictEqual(event.error, err);

          wss.close(done);
        });
      });

      wss.on('connection', (client) => client.send('hi'));
    });

    it('passes binary data as a Node.js `Buffer` by default', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.onmessage = (evt) => {
          assert.ok(Buffer.isBuffer(evt.data));
          wss.close(done);
        };
      });

      wss.on('connection', (ws) => {
        ws.send(new Uint8Array(4096));
        ws.close();
      });
    });

    it('ignores `binaryType` for text messages', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.binaryType = 'arraybuffer';

        ws.onmessage = (evt) => {
          assert.strictEqual(evt.data, 'foo');
          wss.close(done);
        };
      });

      wss.on('connection', (ws) => {
        ws.send('foo');
        ws.close();
      });
    });

    it('allows to update `binaryType` on the fly', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        function testType(binaryType, next) {
          const buf = Buffer.from(binaryType);
          ws.binaryType = binaryType;

          ws.onmessage = (evt) => {
            if (binaryType === 'nodebuffer') {
              assert.ok(Buffer.isBuffer(evt.data));
              assert.deepStrictEqual(evt.data, buf);
              next();
            } else if (binaryType === 'arraybuffer') {
              assert.ok(evt.data instanceof ArrayBuffer);
              assert.deepStrictEqual(Buffer.from(evt.data), buf);
              next();
            } else if (binaryType === 'fragments') {
              assert.deepStrictEqual(evt.data, [buf]);
              next();
            } else if (binaryType === 'blob') {
              assert.ok(evt.data instanceof Blob);
              evt.data
                .arrayBuffer()
                .then((arrayBuffer) => {
                  assert.deepStrictEqual(Buffer.from(arrayBuffer), buf);
                  next();
                })
                .catch(done);
            }
          };

          ws.send(buf);
        }

        function close() {
          ws.close();
          wss.close(done);
        }

        ws.onopen = () => {
          testType('nodebuffer', () => {
            testType('arraybuffer', () => {
              testType('fragments', () => {
                if (hasBlob) testType('blob', close);
                else close();
              });
            });
          });
        };
      });

      wss.on('connection', (ws) => {
        ws.on('message', (msg, isBinary) => {
          assert.ok(isBinary);
          ws.send(msg);
        });
      });
    });
  });

  describe('SSL', () => {
    it('connects to secure websocket server', (done) => {
      const server = https.createServer({
        cert: fs.readFileSync('test/fixtures/certificate.pem'),
        key: fs.readFileSync('test/fixtures/key.pem')
      });
      const wss = new WebSocket.Server({ server });

      wss.on('connection', () => {
        server.close(done);
      });

      server.listen(0, () => {
        const ws = new WebSocket(`wss://127.0.0.1:${server.address().port}`, {
          rejectUnauthorized: false
        });

        ws.on('open', ws.close);
      });
    });

    it('connects to secure websocket server with client side certificate', (done) => {
      const server = https.createServer({
        cert: fs.readFileSync('test/fixtures/certificate.pem'),
        ca: [fs.readFileSync('test/fixtures/ca-certificate.pem')],
        key: fs.readFileSync('test/fixtures/key.pem'),
        requestCert: true
      });

      const wss = new WebSocket.Server({ noServer: true });

      server.on('upgrade', (request, socket, head) => {
        assert.ok(socket.authorized);

        wss.handleUpgrade(request, socket, head, (ws) => {
          ws.on('close', (code) => {
            assert.strictEqual(code, 1005);
            server.close(done);
          });
        });
      });

      server.listen(0, () => {
        const ws = new WebSocket(`wss://localhost:${server.address().port}`, {
          cert: fs.readFileSync('test/fixtures/client-certificate.pem'),
          key: fs.readFileSync('test/fixtures/client-key.pem'),
          rejectUnauthorized: false
        });

        ws.on('open', ws.close);
      });
    });

    it('cannot connect to secure websocket server via ws://', (done) => {
      const server = https.createServer({
        cert: fs.readFileSync('test/fixtures/certificate.pem'),
        key: fs.readFileSync('test/fixtures/key.pem')
      });
      const wss = new WebSocket.Server({ server });

      server.listen(0, () => {
        const ws = new WebSocket(`ws://localhost:${server.address().port}`, {
          rejectUnauthorized: false
        });

        ws.on('error', () => {
          server.close(done);
          wss.close();
        });
      });
    });

    it('can send and receive text data', (done) => {
      const server = https.createServer({
        cert: fs.readFileSync('test/fixtures/certificate.pem'),
        key: fs.readFileSync('test/fixtures/key.pem')
      });
      const wss = new WebSocket.Server({ server });

      wss.on('connection', (ws) => {
        ws.on('message', (message, isBinary) => {
          assert.deepStrictEqual(message, Buffer.from('foobar'));
          assert.ok(!isBinary);
          server.close(done);
        });
      });

      server.listen(0, () => {
        const ws = new WebSocket(`wss://localhost:${server.address().port}`, {
          rejectUnauthorized: false
        });

        ws.on('open', () => {
          ws.send('foobar');
          ws.close();
        });
      });
    });

    it('can send a big binary message', (done) => {
      const buf = crypto.randomBytes(5 * 1024 * 1024);
      const server = https.createServer({
        cert: fs.readFileSync('test/fixtures/certificate.pem'),
        key: fs.readFileSync('test/fixtures/key.pem')
      });
      const wss = new WebSocket.Server({ server });

      wss.on('connection', (ws) => {
        ws.on('message', (message, isBinary) => {
          assert.ok(isBinary);
          ws.send(message);
          ws.close();
        });
      });

      server.listen(0, () => {
        const ws = new WebSocket(`wss://localhost:${server.address().port}`, {
          rejectUnauthorized: false
        });

        ws.on('open', () => ws.send(buf));
        ws.on('message', (message, isBinary) => {
          assert.deepStrictEqual(message, buf);
          assert.ok(isBinary);

          server.close(done);
        });
      });
    }).timeout(4000);

    it('allows to disable sending the SNI extension', (done) => {
      const original = tls.connect;

      tls.connect = (options) => {
        assert.strictEqual(options.servername, '');
        tls.connect = original;
        done();
      };

      const ws = new WebSocket('wss://127.0.0.1', { servername: '' });
    });

    it("works around a double 'error' event bug in Node.js", function (done) {
      //
      // The `minVersion` and `maxVersion` options are not supported in
      // Node.js < 10.16.0.
      //
      if (process.versions.modules < 64) return this.skip();

      //
      // The `'error'` event can be emitted multiple times by the
      // `http.ClientRequest` object in Node.js < 13. This test reproduces the
      // issue in Node.js 12.
      //
      const server = https.createServer({
        cert: fs.readFileSync('test/fixtures/certificate.pem'),
        key: fs.readFileSync('test/fixtures/key.pem'),
        minVersion: 'TLSv1.2'
      });
      const wss = new WebSocket.Server({ server });

      server.listen(0, () => {
        const ws = new WebSocket(`wss://localhost:${server.address().port}`, {
          maxVersion: 'TLSv1.1',
          rejectUnauthorized: false
        });

        ws.on('error', (err) => {
          assert.ok(err instanceof Error);
          server.close(done);
          wss.close();
        });
      });
    });
  });

  describe('Request headers', () => {
    it('adds the authorization header if the url has userinfo', (done) => {
      const agent = new http.Agent();
      const userinfo = 'test:testpass';

      agent.addRequest = (req) => {
        assert.strictEqual(
          req.getHeader('authorization'),
          `Basic ${Buffer.from(userinfo).toString('base64')}`
        );
        done();
      };

      const ws = new WebSocket(`ws://${userinfo}@localhost`, { agent });
    });

    it('honors the `auth` option', (done) => {
      const agent = new http.Agent();
      const auth = 'user:pass';

      agent.addRequest = (req) => {
        assert.strictEqual(
          req.getHeader('authorization'),
          `Basic ${Buffer.from(auth).toString('base64')}`
        );
        done();
      };

      const ws = new WebSocket('ws://localhost', { agent, auth });
    });

    it('favors the url userinfo over the `auth` option', (done) => {
      const agent = new http.Agent();
      const auth = 'foo:bar';
      const userinfo = 'baz:qux';

      agent.addRequest = (req) => {
        assert.strictEqual(
          req.getHeader('authorization'),
          `Basic ${Buffer.from(userinfo).toString('base64')}`
        );
        done();
      };

      const ws = new WebSocket(`ws://${userinfo}@localhost`, { agent, auth });
    });

    it('adds custom headers', (done) => {
      const agent = new http.Agent();

      agent.addRequest = (req) => {
        assert.strictEqual(req.getHeader('cookie'), 'foo=bar');
        done();
      };

      const ws = new WebSocket('ws://localhost', {
        headers: { Cookie: 'foo=bar' },
        agent
      });
    });

    it('excludes default ports from host header', () => {
      const options = { lookup() {} };
      const variants = [
        ['wss://localhost:8443', 'localhost:8443'],
        ['wss://localhost:443', 'localhost'],
        ['ws://localhost:88', 'localhost:88'],
        ['ws://localhost:80', 'localhost']
      ];

      for (const [url, host] of variants) {
        const ws = new WebSocket(url, options);
        assert.strictEqual(ws._req.getHeader('host'), host);
      }
    });

    it("doesn't add the origin header by default", (done) => {
      const agent = new http.Agent();

      agent.addRequest = (req) => {
        assert.strictEqual(req.getHeader('origin'), undefined);
        done();
      };

      const ws = new WebSocket('ws://localhost', { agent });
    });

    it('honors the `origin` option (1/2)', (done) => {
      const agent = new http.Agent();

      agent.addRequest = (req) => {
        assert.strictEqual(req.getHeader('origin'), 'https://example.com:8000');
        done();
      };

      const ws = new WebSocket('ws://localhost', {
        origin: 'https://example.com:8000',
        agent
      });
    });

    it('honors the `origin` option (2/2)', (done) => {
      const agent = new http.Agent();

      agent.addRequest = (req) => {
        assert.strictEqual(
          req.getHeader('sec-websocket-origin'),
          'https://example.com:8000'
        );
        done();
      };

      const ws = new WebSocket('ws://localhost', {
        origin: 'https://example.com:8000',
        protocolVersion: 8,
        agent
      });
    });

    it('honors the `finishRequest` option', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const host = `localhost:${wss.address().port}`;
        const ws = new WebSocket(`ws://${host}`, {
          finishRequest(req, ws) {
            assert.ok(req instanceof http.ClientRequest);
            assert.strictEqual(req.getHeader('host'), host);
            assert.ok(ws instanceof WebSocket);
            assert.strictEqual(req, ws._req);

            req.on('socket', (socket) => {
              socket.on('connect', () => {
                req.setHeader('Cookie', 'foo=bar');
                req.end();
              });
            });
          }
        });

        ws.on('close', (code) => {
          assert.strictEqual(code, 1005);
          wss.close(done);
        });
      });

      wss.on('connection', (ws, req) => {
        assert.strictEqual(req.headers.cookie, 'foo=bar');
        ws.close();
      });
    });
  });

  describe('permessage-deflate', () => {
    it('is enabled by default', (done) => {
      const agent = new http.Agent();

      agent.addRequest = (req) => {
        assert.strictEqual(
          req.getHeader('sec-websocket-extensions'),
          'permessage-deflate; client_max_window_bits'
        );
        done();
      };

      const ws = new WebSocket('ws://localhost', { agent });
    });

    it('can be disabled', (done) => {
      const agent = new http.Agent();

      agent.addRequest = (req) => {
        assert.strictEqual(
          req.getHeader('sec-websocket-extensions'),
          undefined
        );
        done();
      };

      const ws = new WebSocket('ws://localhost', {
        perMessageDeflate: false,
        agent
      });
    });

    it('can send extension parameters', (done) => {
      const agent = new http.Agent();

      const value =
        'permessage-deflate; server_no_context_takeover;' +
        ' client_no_context_takeover; server_max_window_bits=10;' +
        ' client_max_window_bits';

      agent.addRequest = (req) => {
        assert.strictEqual(req.getHeader('sec-websocket-extensions'), value);
        done();
      };

      const ws = new WebSocket('ws://localhost', {
        perMessageDeflate: {
          clientNoContextTakeover: true,
          serverNoContextTakeover: true,
          clientMaxWindowBits: true,
          serverMaxWindowBits: 10
        },
        agent
      });
    });

    it('consumes all received data when connection is closed (1/2)', (done) => {
      const wss = new WebSocket.Server(
        {
          perMessageDeflate: { threshold: 0 },
          port: 0
        },
        () => {
          const messages = [];
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          ws.on('open', () => {
            ws._socket.on('close', () => {
              assert.strictEqual(ws._receiver._state, 5);
            });
          });

          ws.on('message', (message, isBinary) => {
            assert.ok(!isBinary);
            messages.push(message.toString());
          });

          ws.on('close', (code) => {
            assert.strictEqual(code, 1006);
            assert.deepStrictEqual(messages, ['foo', 'bar', 'baz', 'qux']);
            wss.close(done);
          });
        }
      );

      wss.on('connection', (ws) => {
        ws.send('foo');
        ws.send('bar');
        ws.send('baz');
        ws.send('qux', () => ws._socket.end());
      });
    });

    it('consumes all received data when connection is closed (2/2)', (done) => {
      const wss = new WebSocket.Server(
        {
          perMessageDeflate: true,
          port: 0
        },
        () => {
          const messageLengths = [];
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

          ws.on('open', () => {
            ws._socket.prependListener('close', () => {
              assert.strictEqual(ws._receiver._state, 5);
              assert.strictEqual(ws._socket._readableState.length, 3);
            });

            const push = ws._socket.push;

            // Override `ws._socket.push()` to know exactly when data is
            // received and call `ws.terminate()` immediately after that without
            // relying on a timer.
            ws._socket.push = (data) => {
              ws._socket.push = push;
              ws._socket.push(data);
              ws.terminate();
            };

            const payload1 = Buffer.alloc(highWaterMark - 1024);
            const payload2 = Buffer.alloc(1);

            const opts = {
              fin: true,
              opcode: 0x02,
              mask: false,
              readOnly: false
            };

            const list = [
              ...Sender.frame(payload1, { rsv1: false, ...opts }),
              ...Sender.frame(payload2, { rsv1: true, ...opts })
            ];

            for (let i = 0; i < 340; i++) {
              list.push(list[list.length - 2], list[list.length - 1]);
            }

            const data = Buffer.concat(list);

            assert.ok(data.length > highWaterMark);

            // This hack is used because there is no guarantee that more than
            // `highWaterMark` bytes will be sent as a single TCP packet.
            push.call(ws._socket, data);

            wss.clients
              .values()
              .next()
              .value.send(payload2, { compress: false });
          });

          ws.on('message', (message, isBinary) => {
            assert.ok(isBinary);
            messageLengths.push(message.length);
          });

          ws.on('close', (code) => {
            assert.strictEqual(code, 1006);
            assert.strictEqual(messageLengths.length, 343);
            assert.strictEqual(messageLengths[0], highWaterMark - 1024);
            assert.strictEqual(messageLengths[messageLengths.length - 1], 1);
            wss.close(done);
          });
        }
      );
    });

    it('handles a close frame received while compressing data', (done) => {
      const wss = new WebSocket.Server(
        {
          perMessageDeflate: true,
          port: 0
        },
        () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
            perMessageDeflate: { threshold: 0 }
          });

          ws.on('open', () => {
            ws._receiver.on('conclude', () => {
              assert.strictEqual(ws._sender._state, 1);
            });

            ws.send('foo');
            ws.send('bar');
            ws.send('baz');
            ws.send('qux');
          });
        }
      );

      wss.on('connection', (ws) => {
        const messages = [];

        ws.on('message', (message, isBinary) => {
          assert.ok(!isBinary);
          messages.push(message.toString());
        });

        ws.on('close', (code, reason) => {
          assert.deepStrictEqual(messages, ['foo', 'bar', 'baz', 'qux']);
          assert.strictEqual(code, 1000);
          assert.deepStrictEqual(reason, EMPTY_BUFFER);
          wss.close(done);
        });

        ws.close(1000);
      });
    });

    describe('#close', () => {
      it('can be used while data is being decompressed', (done) => {
        const wss = new WebSocket.Server(
          {
            perMessageDeflate: true,
            port: 0
          },
          () => {
            const messages = [];
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

            ws.on('message', (message, isBinary) => {
              assert.ok(!isBinary);

              if (messages.push(message.toString()) > 1) return;

              setImmediate(() => {
                process.nextTick(() => {
                  assert.strictEqual(ws._receiver._state, 5);
                  ws.close(1000);
                });
              });
            });

            ws.on('close', (code, reason) => {
              assert.deepStrictEqual(messages, ['', '', '', '']);
              assert.strictEqual(code, 1000);
              assert.deepStrictEqual(reason, EMPTY_BUFFER);
              wss.close(done);
            });
          }
        );

        wss.on('connection', (ws) => {
          const buf = Buffer.from('c10100c10100c10100c10100', 'hex');
          ws._socket.write(buf);
        });
      });
    });

    describe('#send', () => {
      it('can send text data', (done) => {
        const wss = new WebSocket.Server(
          {
            perMessageDeflate: { threshold: 0 },
            port: 0
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
              perMessageDeflate: { threshold: 0 }
            });

            ws.on('open', () => {
              ws.send('hi', { compress: true });
              ws.close();
            });

            ws.on('message', (message, isBinary) => {
              assert.deepStrictEqual(message, Buffer.from('hi'));
              assert.ok(!isBinary);
              wss.close(done);
            });
          }
        );

        wss.on('connection', (ws) => {
          ws.on('message', (message, isBinary) => {
            ws.send(message, { binary: isBinary, compress: true });
          });
        });
      });

      it('can send a `TypedArray`', (done) => {
        const array = new Float32Array(5);

        for (let i = 0; i < array.length; i++) {
          array[i] = i / 2;
        }

        const wss = new WebSocket.Server(
          {
            perMessageDeflate: { threshold: 0 },
            port: 0
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
              perMessageDeflate: { threshold: 0 }
            });

            ws.on('open', () => {
              ws.send(array, { compress: true });
              ws.close();
            });

            ws.on('message', (message, isBinary) => {
              assert.deepStrictEqual(message, Buffer.from(array.buffer));
              assert.ok(isBinary);
              wss.close(done);
            });
          }
        );

        wss.on('connection', (ws) => {
          ws.on('message', (message, isBinary) => {
            assert.ok(isBinary);
            ws.send(message, { compress: true });
          });
        });
      });

      it('can send an `ArrayBuffer`', (done) => {
        const array = new Float32Array(5);

        for (let i = 0; i < array.length; i++) {
          array[i] = i / 2;
        }

        const wss = new WebSocket.Server(
          {
            perMessageDeflate: { threshold: 0 },
            port: 0
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
              perMessageDeflate: { threshold: 0 }
            });

            ws.on('open', () => {
              ws.send(array.buffer, { compress: true });
              ws.close();
            });

            ws.on('message', (message, isBinary) => {
              assert.deepStrictEqual(message, Buffer.from(array.buffer));
              assert.ok(isBinary);
              wss.close(done);
            });
          }
        );

        wss.on('connection', (ws) => {
          ws.on('message', (message, isBinary) => {
            assert.ok(isBinary);
            ws.send(message, { compress: true });
          });
        });
      });

      it('can send a `Blob`', function (done) {
        if (!hasBlob) return this.skip();

        const wss = new WebSocket.Server(
          {
            perMessageDeflate: { threshold: 0 },
            port: 0
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
              perMessageDeflate: { threshold: 0 }
            });

            const messages = [];

            ws.on('open', () => {
              ws.send(new Blob(['foo']));
              ws.send(new Blob(['bar']));
              ws.close();
            });

            ws.on('message', (message, isBinary) => {
              assert.ok(isBinary);
              messages.push(message.toString());

              if (messages.length === 2) {
                assert.deepStrictEqual(messages, ['foo', 'bar']);
                wss.close(done);
              }
            });
          }
        );

        wss.on('connection', (ws) => {
          ws.on('message', (message, isBinary) => {
            assert.ok(isBinary);
            ws.send(message);
          });
        });
      });

      it('ignores the `compress` option if the extension is disabled', (done) => {
        const wss = new WebSocket.Server({ port: 0 }, () => {
          const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
            perMessageDeflate: false
          });

          ws.on('open', () => {
            ws.send('hi', { compress: true });
            ws.close();
          });

          ws.on('message', (message, isBinary) => {
            assert.deepStrictEqual(message, Buffer.from('hi'));
            assert.ok(!isBinary);
            wss.close(done);
          });
        });

        wss.on('connection', (ws) => {
          ws.on('message', (message, isBinary) => {
            ws.send(message, { binary: isBinary, compress: true });
          });
        });
      });

      it('calls the callback if the socket is closed prematurely', (done) => {
        const called = [];
        const wss = new WebSocket.Server(
          { perMessageDeflate: true, port: 0 },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
              perMessageDeflate: { threshold: 0 }
            });

            ws.on('open', () => {
              ws.send('foo');
              ws.send('bar', (err) => {
                called.push(1);

                assert.strictEqual(ws.readyState, WebSocket.CLOSING);
                assert.ok(err instanceof Error);
                assert.strictEqual(
                  err.message,
                  'The socket was closed while data was being compressed'
                );
              });
              ws.send('baz');
              ws.send('qux', (err) => {
                called.push(2);

                assert.strictEqual(ws.readyState, WebSocket.CLOSING);
                assert.ok(err instanceof Error);
                assert.strictEqual(
                  err.message,
                  'The socket was closed while data was being compressed'
                );
              });
              ws.close();
            });
          }
        );

        wss.on('connection', (ws) => {
          ws.on('close', () => {
            assert.deepStrictEqual(called, [1, 2]);
            wss.close(done);
          });

          ws._socket.end();
        });
      });
    });

    describe('#terminate', () => {
      it('can be used while data is being compressed', (done) => {
        const wss = new WebSocket.Server(
          {
            perMessageDeflate: { threshold: 0 },
            port: 0
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`, {
              perMessageDeflate: { threshold: 0 }
            });

            ws.on('open', () => {
              ws.send('hi', (err) => {
                assert.strictEqual(ws.readyState, WebSocket.CLOSING);
                assert.ok(err instanceof Error);
                assert.strictEqual(
                  err.message,
                  'The socket was closed while data was being compressed'
                );

                ws.on('close', () => {
                  wss.close(done);
                });
              });
              ws.terminate();
            });
          }
        );
      });

      it('can be used while data is being decompressed', (done) => {
        const wss = new WebSocket.Server(
          {
            perMessageDeflate: true,
            port: 0
          },
          () => {
            const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
            const messages = [];

            ws.on('message', (message, isBinary) => {
              assert.ok(!isBinary);

              if (messages.push(message.toString()) > 1) return;

              setImmediate(() => {
                process.nextTick(() => {
                  assert.strictEqual(ws._receiver._state, 5);
                  ws.terminate();
                });
              });
            });

            ws.on('close', (code, reason) => {
              assert.deepStrictEqual(messages, ['', '', '', '']);
              assert.strictEqual(code, 1006);
              assert.strictEqual(reason, EMPTY_BUFFER);
              wss.close(done);
            });
          }
        );

        wss.on('connection', (ws) => {
          const buf = Buffer.from('c10100c10100c10100c10100', 'hex');
          ws._socket.write(buf);
        });
      });
    });
  });

  describe('Connection close', () => {
    it('closes cleanly after simultaneous errors (1/2)', (done) => {
      let clientCloseEventEmitted = false;
      let serverClientCloseEventEmitted = false;

      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('error', (err) => {
          assert.ok(err instanceof RangeError);
          assert.strictEqual(err.code, 'WS_ERR_INVALID_OPCODE');
          assert.strictEqual(
            err.message,
            'Invalid WebSocket frame: invalid opcode 5'
          );

          ws.on('close', (code, reason) => {
            assert.strictEqual(code, 1006);
            assert.strictEqual(reason, EMPTY_BUFFER);

            clientCloseEventEmitted = true;
            if (serverClientCloseEventEmitted) wss.close(done);
          });
        });

        ws.on('open', () => {
          // Write an invalid frame in both directions to trigger simultaneous
          // failure.
          const chunk = Buffer.from([0x85, 0x00]);

          wss.clients.values().next().value._socket.write(chunk);
          ws._socket.write(chunk);
        });
      });

      wss.on('connection', (ws) => {
        ws.on('error', (err) => {
          assert.ok(err instanceof RangeError);
          assert.strictEqual(err.code, 'WS_ERR_INVALID_OPCODE');
          assert.strictEqual(
            err.message,
            'Invalid WebSocket frame: invalid opcode 5'
          );

          ws.on('close', (code, reason) => {
            assert.strictEqual(code, 1006);
            assert.strictEqual(reason, EMPTY_BUFFER);

            serverClientCloseEventEmitted = true;
            if (clientCloseEventEmitted) wss.close(done);
          });
        });
      });
    });

    it('closes cleanly after simultaneous errors (2/2)', (done) => {
      let clientCloseEventEmitted = false;
      let serverClientCloseEventEmitted = false;

      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);

        ws.on('error', (err) => {
          assert.ok(err instanceof RangeError);
          assert.strictEqual(err.code, 'WS_ERR_INVALID_OPCODE');
          assert.strictEqual(
            err.message,
            'Invalid WebSocket frame: invalid opcode 5'
          );

          ws.on('close', (code, reason) => {
            assert.strictEqual(code, 1006);
            assert.strictEqual(reason, EMPTY_BUFFER);

            clientCloseEventEmitted = true;
            if (serverClientCloseEventEmitted) wss.close(done);
          });
        });

        ws.on('open', () => {
          // Write an invalid frame in both directions and change the
          // `readyState` to `WebSocket.CLOSING`.
          const chunk = Buffer.from([0x85, 0x00]);
          const serverWs = wss.clients.values().next().value;

          serverWs._socket.write(chunk);
          serverWs.close();

          ws._socket.write(chunk);
          ws.close();
        });
      });

      wss.on('connection', (ws) => {
        ws.on('error', (err) => {
          assert.ok(err instanceof RangeError);
          assert.strictEqual(err.code, 'WS_ERR_INVALID_OPCODE');
          assert.strictEqual(
            err.message,
            'Invalid WebSocket frame: invalid opcode 5'
          );

          ws.on('close', (code, reason) => {
            assert.strictEqual(code, 1006);
            assert.strictEqual(reason, EMPTY_BUFFER);

            serverClientCloseEventEmitted = true;
            if (clientCloseEventEmitted) wss.close(done);
          });
        });
      });
    });

    it('resumes the socket when an error occurs', (done) => {
      const maxPayload = 16 * 1024;
      const wss = new WebSocket.Server({ maxPayload, port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
      });

      wss.on('connection', (ws) => {
        const list = [
          ...Sender.frame(Buffer.alloc(maxPayload + 1), {
            fin: true,
            opcode: 0x02,
            mask: true,
            readOnly: false
          })
        ];

        ws.on('error', (err) => {
          assert.ok(err instanceof RangeError);
          assert.strictEqual(err.code, 'WS_ERR_UNSUPPORTED_MESSAGE_LENGTH');
          assert.strictEqual(err.message, 'Max payload size exceeded');

          ws.on('close', (code, reason) => {
            assert.strictEqual(code, 1006);
            assert.strictEqual(reason, EMPTY_BUFFER);
            wss.close(done);
          });
        });

        ws._socket.push(Buffer.concat(list));
      });
    });

    it('resumes the socket when the close frame is received', (done) => {
      const wss = new WebSocket.Server({ port: 0 }, () => {
        const ws = new WebSocket(`ws://localhost:${wss.address().port}`);
      });

      wss.on('connection', (ws) => {
        const opts = { fin: true, mask: true, readOnly: false };
        const list = [
          ...Sender.frame(Buffer.alloc(16 * 1024), { opcode: 0x02, ...opts }),
          ...Sender.frame(EMPTY_BUFFER, { opcode: 0x08, ...opts })
        ];

        ws.on('close', (code, reason) => {
          assert.strictEqual(code, 1005);
          assert.strictEqual(reason, EMPTY_BUFFER);
          wss.close(done);
        });

        ws._socket.push(Buffer.concat(list));
      });
    });
  });
});
```

## File: `test/fixtures/ca-certificate.pem`
```
-----BEGIN CERTIFICATE-----
MIIBtTCCAVoCCQCXqK2FegDgiDAKBggqhkjOPQQDAjBhMQswCQYDVQQGEwJJVDEQ
MA4GA1UECAwHUGVydWdpYTEQMA4GA1UEBwwHRm9saWdubzETMBEGA1UECgwKd2Vi
c29ja2V0czELMAkGA1UECwwCd3MxDDAKBgNVBAMMA2NhMTAgFw0yMTA1MjYxOTA1
MjdaGA8yMTIxMDUwMjE5MDUyN1owYTELMAkGA1UEBhMCSVQxEDAOBgNVBAgMB1Bl
cnVnaWExEDAOBgNVBAcMB0ZvbGlnbm8xEzARBgNVBAoMCndlYnNvY2tldHMxCzAJ
BgNVBAsMAndzMQwwCgYDVQQDDANjYTEwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC
AASHE75QDQN6XNo/711YSbckaa8r4lt0hGkgtADaBFT9Qn9gcm5omapePZT76Ff9
rwjMcS+YPXS7J7bk+QHLihJMMAoGCCqGSM49BAMCA0kAMEYCIQCUMdUih+sE0ZTu
ORlcKiM8DKyiKkGU4Ty+dslz6nVJjAIhAMcSy0SBsBDgsai1s9aCmAGJXCijNb6g
vfWaatgq+ma2
-----END CERTIFICATE-----
```

## File: `test/fixtures/ca-key.pem`
```
-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIAa/Onpk27cLkqzje69Bac8yG+LTBXIPWT8yGlyjEFbboAoGCCqGSM49
AwEHoUQDQgAEhxO+UA0DelzaP+9dWEm3JGmvK+JbdIRpILQA2gRU/UJ/YHJuaJmq
Xj2U++hX/a8IzHEvmD10uye25PkBy4oSTA==
-----END EC PRIVATE KEY-----
```

## File: `test/fixtures/certificate.pem`
```
-----BEGIN CERTIFICATE-----
MIIBujCCAWACCQDjKdAMt3mZhDAKBggqhkjOPQQDAjBkMQswCQYDVQQGEwJJVDEQ
MA4GA1UECAwHUGVydWdpYTEQMA4GA1UEBwwHRm9saWdubzETMBEGA1UECgwKd2Vi
c29ja2V0czELMAkGA1UECwwCd3MxDzANBgNVBAMMBnNlcnZlcjAgFw0yMTA1MjYx
OTEwMjlaGA8yMTIxMDUwMjE5MTAyOVowZDELMAkGA1UEBhMCSVQxEDAOBgNVBAgM
B1BlcnVnaWExEDAOBgNVBAcMB0ZvbGlnbm8xEzARBgNVBAoMCndlYnNvY2tldHMx
CzAJBgNVBAsMAndzMQ8wDQYDVQQDDAZzZXJ2ZXIwWTATBgcqhkjOPQIBBggqhkjO
PQMBBwNCAAQKhyRhdSVOecbJU4O5XkB/iGodbnCOqmchs4TXmE3Prv5SrNDhODDv
rOWTXwR3/HrrdNfOzPdb54amu8POwpohMAoGCCqGSM49BAMCA0gAMEUCIHMRUSPl
8FGkDLl8KF1A+SbT2ds3zUOLdYvj30Z2SKSVAiEA84U/R1ly9wf5Rzv93sTHI99o
KScsr/PHN8rT2pop5pk=
-----END CERTIFICATE-----
```

## File: `test/fixtures/client-certificate.pem`
```
-----BEGIN CERTIFICATE-----
MIIBtzCCAV0CCQDDIX2dKuKP0zAKBggqhkjOPQQDAjBhMQswCQYDVQQGEwJJVDEQ
MA4GA1UECAwHUGVydWdpYTEQMA4GA1UEBwwHRm9saWdubzETMBEGA1UECgwKd2Vi
c29ja2V0czELMAkGA1UECwwCd3MxDDAKBgNVBAMMA2NhMTAgFw0yMTA1MjYxOTE3
NDJaGA8yMTIxMDUwMjE5MTc0MlowZDELMAkGA1UEBhMCSVQxEDAOBgNVBAgMB1Bl
cnVnaWExEDAOBgNVBAcMB0ZvbGlnbm8xEzARBgNVBAoMCndlYnNvY2tldHMxCzAJ
BgNVBAsMAndzMQ8wDQYDVQQDDAZhZ2VudDEwWTATBgcqhkjOPQIBBggqhkjOPQMB
BwNCAATwHlNS2b13TMhBTSWBXAn6TEPxrsvG93ZZyUlmrEMOXSMX2hI7sv660YNj
+eGyE2CV33XsQxV3TUqi51fUjIu8MAoGCCqGSM49BAMCA0gAMEUCIQCxsqBre+Do
jnfg6XmCaB0fywNzcDlvdoVNuNAWfVNrSAIgDQmbM0mXZaSAkf4sgtKdXnpE3vrb
MElb457Bi3B+rkE=
-----END CERTIFICATE-----
```

## File: `test/fixtures/client-key.pem`
```
-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIKVGskK0UR86WwMo5H0+hNAFGRBYsEevK3ye4y1YberVoAoGCCqGSM49
AwEHoUQDQgAE8B5TUtm9d0zIQU0lgVwJ+kxD8a7Lxvd2WclJZqxDDl0jF9oSO7L+
utGDY/nhshNgld917EMVd01KoudX1IyLvA==
-----END EC PRIVATE KEY-----
```

## File: `test/fixtures/key.pem`
```
-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIIjLz7YEWIrsGem2+YV8eJhHhetsjYIrjuqJLbdG7B3zoAoGCCqGSM49
AwEHoUQDQgAECockYXUlTnnGyVODuV5Af4hqHW5wjqpnIbOE15hNz67+UqzQ4Tgw
76zlk18Ed/x663TXzsz3W+eGprvDzsKaIQ==
-----END EC PRIVATE KEY-----
```

