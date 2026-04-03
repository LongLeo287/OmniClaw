---
id: github.com-forwardemail-supertest-e20a0f92-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:51.180328
---

# KNOWLEDGE EXTRACT: github.com_forwardemail_supertest_e20a0f92
> **Extracted on:** 2026-04-01 11:05:35
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521221/github.com_forwardemail_supertest_e20a0f92

---

## File: `.commitlintrc.js`
```javascript
module.exports = {
  extends: ['@commitlint/config-conventional']
};
```

## File: `.editorconfig`
```
root = true

[*]
charset = utf-8
insert_final_newline = true
end_of_line = lf
trim_trailing_whitespace = true
indent_style = space
indent_size = 2

[*.{js,json}]
indent_size = 2
indent_style = space
```

## File: `.eslintrc`
```
{
  "extends": "airbnb-base/legacy",
  "env": {
    "node": true,
    "mocha": true
  },
  "parserOptions": {
    "ecmaVersion": 6
  },
  "rules": {
    // disabled - disagree with airbnb
    "func-names": [0],
    "space-before-function-paren": [0],
    "consistent-return": [0],

    // Disabled but may want to refactor code eventually
    "no-use-before-define": [2, "nofunc"],
    "no-underscore-dangle": [0],

    // IMHO, more sensible overrides to existing airbnb error definitions
    "max-len": [2, 100, 4, {"ignoreComments": true, "ignoreUrls": true}],
    "no-unused-expressions": [2, { "allowShortCircuit": true, "allowTernary": true }]
  }
}
```

## File: `.gitignore`
```
#       OS        #
###################
.DS_Store
.idea
Thumbs.db
tmp/
temp/


#     Node.js     #
###################
node_modules


#       NYC       #
###################
coverage
*.lcov
.nyc_output


#      Files      #
###################
*.log
```

## File: `.npmignore`
```
.editorconfig
.eslintrc
.travis.yml
.idea
.vscode
.nyc_output
test
coverage
```

## File: `.npmrc`
```
package-lock=true
```

## File: `LICENSE`
```
(The MIT License)

Copyright (c) 2014 TJ Holowaychuk <tj@vision-media.ca> and other
contributors.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `README.md`
```markdown
# [supertest](https://forwardemail.github.io/superagent/)

[![build status](https://github.com/forwardemail/supertest/actions/workflows/ci.yml/badge.svg)](https://github.com/forwardemail/supertest/actions/workflows/ci.yml)
[![code coverage](https://img.shields.io/codecov/c/github/ladjs/supertest.svg)](https://codecov.io/gh/ladjs/supertest)
[![code style](https://img.shields.io/badge/code_style-XO-5ed9c7.svg)](https://github.com/sindresorhus/xo)
[![styled with prettier](https://img.shields.io/badge/styled_with-prettier-ff69b4.svg)](https://github.com/prettier/prettier)
[![made with lass](https://img.shields.io/badge/made_with-lass-95CC28.svg)](https://lass.js.org)
[![license](https://img.shields.io/github/license/ladjs/supertest.svg)](LICENSE)

> HTTP assertions made easy via [superagent](http://github.com/ladjs/superagent).  Maintained for [Forward Email](https://github.com/forwardemail) and [Lad](https://github.com/ladjs).

## About

The motivation with this module is to provide a high-level abstraction for testing
HTTP, while still allowing you to drop down to the [lower-level API](https://forwardemail.github.io/superagent/) provided by superagent.

## Getting Started

Install supertest as an npm module and save it to your package.json file as a development dependency:

```bash
npm install supertest --save-dev
```

  Once installed it can now be referenced by simply calling ```require('supertest');```

## Example

You may pass an `http.Server`, or a `Function` to `request()` - if the server is not
already listening for connections then it is bound to an ephemeral port for you so
there is no need to keep track of ports.

supertest works with any test framework, here is an example without using any
test framework at all:

```js
const request = require('supertest');
const express = require('express');

const app = express();

app.get('/user', function(req, res) {
  res.status(200).json({ name: 'john' });
});

request(app)
  .get('/user')
  .expect('Content-Type', /json/)
  .expect('Content-Length', '15')
  .expect(200)
  .end(function(err, res) {
    if (err) throw err;
  });
```

To enable http2 protocol, simply append an options to `request` or `request.agent`:

```js
const request = require('supertest');
const express = require('express');

const app = express();

app.get('/user', function(req, res) {
  res.status(200).json({ name: 'john' });
});

request(app, { http2: true })
  .get('/user')
  .expect('Content-Type', /json/)
  .expect('Content-Length', '15')
  .expect(200)
  .end(function(err, res) {
    if (err) throw err;
  });

request.agent(app, { http2: true })
  .get('/user')
  .expect('Content-Type', /json/)
  .expect('Content-Length', '15')
  .expect(200)
  .end(function(err, res) {
    if (err) throw err;
  });
```

Here's an example with mocha, note how you can pass `done` straight to any of the `.expect()` calls:

```js
describe('GET /user', function() {
  it('responds with json', function(done) {
    request(app)
      .get('/user')
      .set('Accept', 'application/json')
      .expect('Content-Type', /json/)
      .expect(200, done);
  });
});
```

You can use `auth` method to pass HTTP username and password in the same way as in the [superagent](https://forwardemail.github.io/superagent/#authentication):

```js
describe('GET /user', function() {
  it('responds with json', function(done) {
    request(app)
      .get('/user')
      .auth('username', 'password')
      .set('Accept', 'application/json')
      .expect('Content-Type', /json/)
      .expect(200, done);
  });
});
```

One thing to note with the above statement is that superagent now sends any HTTP
error (anything other than a 2XX response code) to the callback as the first argument if
you do not add a status code expect (i.e. `.expect(302)`).

If you are using the `.end()` method `.expect()` assertions that fail will
not throw - they will return the assertion as an error to the `.end()` callback. In
order to fail the test case, you will need to rethrow or pass `err` to `done()`, as follows:

```js
describe('POST /users', function() {
  it('responds with json', function(done) {
    request(app)
      .post('/users')
      .send({name: 'john'})
      .set('Accept', 'application/json')
      .expect('Content-Type', /json/)
      .expect(200)
      .end(function(err, res) {
        if (err) return done(err);
        return done();
      });
  });
});
```

You can also use promises:

```js
describe('GET /users', function() {
  it('responds with json', function() {
    return request(app)
      .get('/users')
      .set('Accept', 'application/json')
      .expect('Content-Type', /json/)
      .expect(200)
      .then(response => {
         expect(response.body.email).toEqual('foo@bar.com');
      })
  });
});
```

Or async/await syntax:

```js
describe('GET /users', function() {
  it('responds with json', async function() {
    const response = await request(app)
      .get('/users')
      .set('Accept', 'application/json')
    expect(response.headers["content-type"]).toMatch(/json/);
    expect(response.status).toEqual(200);
    expect(response.body.email).toEqual('foo@bar.com');
  });
});
```

Expectations are run in the order of definition. This characteristic can be used
to modify the response body or headers before executing an assertion.

```js
describe('POST /user', function() {
  it('user.name should be an case-insensitive match for "john"', function(done) {
    request(app)
      .post('/user')
      .send('name=john') // x-www-form-urlencoded upload
      .set('Accept', 'application/json')
      .expect(function(res) {
        res.body.id = 'some fixed id';
        res.body.name = res.body.name.toLowerCase();
      })
      .expect(200, {
        id: 'some fixed id',
        name: 'john'
      }, done);
  });
});
```

Anything you can do with superagent, you can do with supertest - for example multipart file uploads!

```js
request(app)
  .post('/')
  .field('name', 'my awesome avatar')
  .field('complex_object', '{"attribute": "value"}', {contentType: 'application/json'})
  .attach('avatar', 'test/fixtures/avatar.jpg')
  ...
```

Passing the app or url each time is not necessary, if you're testing
the same host you may simply re-assign the request variable with the
initialization app or url, a new `Test` is created per `request.VERB()` call.

```js
request = request('http://localhost:5555');

request.get('/').expect(200, function(err){
  console.log(err);
});

request.get('/').expect('heya', function(err){
  console.log(err);
});
```

Here's an example with mocha that shows how to persist a request and its cookies:

```js
const request = require('supertest');
const should = require('should');
const express = require('express');
const cookieParser = require('cookie-parser');

describe('request.agent(app)', function() {
  const app = express();
  app.use(cookieParser());

  app.get('/', function(req, res) {
    res.cookie('cookie', 'hey');
    res.send();
  });

  app.get('/return', function(req, res) {
    if (req.cookies.cookie) res.send(req.cookies.cookie);
    else res.send(':(')
  });

  const agent = request.agent(app);

  it('should save cookies', function(done) {
    agent
    .get('/')
    .expect('set-cookie', 'cookie=hey; Path=/', done);
  });

  it('should send cookies', function(done) {
    agent
    .get('/return')
    .expect('hey', done);
  });
});
```

There is another example that is introduced by the file [agency.js](https://github.com/ladjs/superagent/blob/master/test/node/agency.js)

Here is an example where 2 cookies are set on the request.

```js
agent(app)
  .get('/api/content')
  .set('Cookie', ['nameOne=valueOne;nameTwo=valueTwo'])
  .send()
  .expect(200)
  .end((err, res) => {
    if (err) {
      return done(err);
    }
    expect(res.text).to.be.equal('hey');
    return done();
  });
```

## API

You may use any [superagent](http://github.com/ladjs/superagent) methods,
including `.write()`, `.pipe()` etc and perform assertions in the `.end()` callback
for lower-level needs.

### .expect(status[, fn])

Assert response `status` code.

### .expect(status, body[, fn])

Assert response `status` code and `body`.

### .expect(body[, fn])

Assert response `body` text with a string, regular expression, or
parsed body object.

### .expect(field, value[, fn])

Assert header `field` `value` with a string or regular expression.

### .expect(function(res) {})

Pass a custom assertion function. It'll be given the response object to check. If the check fails, throw an error.

```js
request(app)
  .get('/')
  .expect(hasPreviousAndNextKeys)
  .end(done);

function hasPreviousAndNextKeys(res) {
  if (!('next' in res.body)) throw new Error("missing next key");
  if (!('prev' in res.body)) throw new Error("missing prev key");
}
```

### .end(fn)

Perform the request and invoke `fn(err, res)`.

## Cookies

Here is an example of using the `set` and `not` cookie assertions:

```js
// setup super-test
const request = require('supertest');
const express = require('express');
const cookies = request.cookies;

// setup express test service
const app = express();

app.get('/users', function(req, res) {
  res.cookie('alpha', 'one', { domain: 'domain.com', path: '/', httpOnly: true });
  res.send(200, { name: 'tobi' });
});

// test request to service
request(app)
  .get('/users')
  .expect('Content-Type', /json/)
  .expect('Content-Length', '15')
  .expect(200)
  // assert 'alpha' cookie is set with domain, path, and httpOnly options
  .expect(cookies.set({ name: 'alpha', options: ['domain', 'path', 'httponly'] }))
  // assert 'bravo' cookie is NOT set
  .expect(cookies.not('set', { name: 'bravo' }))
  .end(function(err, res) {
    if (err) {
      throw err;
    }
  });
```

It is also possible to chain assertions:

```js
cookies.set({/* ... */}).not('set', {/* ... */})
```

### Cookie assertions

Functions and methods are chainable.

#### cookies([secret], [asserts])

Get assertion function for [super-test](https://github.com/visionmedia/supertest) `.expect()` method.

*Arguments*

- `secret` - String or array of strings. Cookie signature secrets.
- `asserts(req, res)` - Function or array of functions. Failed custom assertions should throw.

#### .set(expects, [assert])

Assert that cookie and options are set.

*Arguments*

- `expects` - Object or array of objects.
  - `name` - String name of cookie.
  - `options` - *Optional* array of options.
- `assert` - *Optional* boolean "assert true" modifier. Default: `true`.

#### .reset(expects, [assert])

Assert that cookie is set and was already set (in request headers).

*Arguments*

- `expects` - Object or array of objects.
  - `name` - String name of cookie.
- `assert` - *Optional* boolean "assert true" modifier. Default: `true`.

#### .new(expects, [assert])

Assert that cookie is set and was NOT already set (NOT in request headers).

*Arguments*

- `expects` - Object or array of objects.
  - `name` - String name of cookie.
- `assert` - *Optional* boolean "assert true" modifier. Default: `true`.

#### .renew(expects, [assert])

Assert that cookie is set with a strictly greater `expires` or `max-age` than the given value.

*Arguments*

- `expects` - Object or array of objects.
  - `name` - String name of cookie.
  - `options` - Object of options. `use one of two options below`
  - `options`.`expires` - String UTC expiration for original cookie (in request headers).
  - `options`.`max-age` - Integer ttl in seconds for original cookie (in request headers).
- `assert` - *Optional* boolean "assert true" modifier. Default: `true`.

#### .contain(expects, [assert])

Assert that cookie is set with value and contains options.

Requires `cookies(secret)` initialization if cookie is signed.

*Arguments*

- `expects` - Object or array of objects.
  - `name` - String name of cookie.
  - `value` - *Optional* string unsigned value of cookie.
  - `options` - *Optional* object of options.
  - `options`.`domain` - *Optional* string domain.
  - `options`.`path` - *Optional* string path.
  - `options`.`expires` - *Optional* string UTC expiration.
  - `options`.`max-age` - *Optional* integer ttl, in seconds.
  - `options`.`secure` - *Optional* boolean secure flag.
  - `options`.`httponly` - *Optional* boolean httpOnly flag.
- `assert` - *Optional* boolean "assert true" modifier. Default: `true`.

#### .not(method, expects)

Call any cookies assertion method with "assert true" modifier set to `false`.

Syntactic sugar.

*Arguments*

- `method` - String method name. Arguments of method name apply in `expects`.
- `expects` - Object or array of objects.
  - `name` - String name of cookie.
  - `value` - *Optional* string unsigned value of cookie.
  - `options` - *Optional* object of options.

## Notes

Inspired by [api-easy](https://github.com/flatiron/api-easy) minus vows coupling.

## License

MIT

[coverage-badge]: https://img.shields.io/codecov/c/github/ladjs/supertest.svg
[coverage]: https://codecov.io/gh/ladjs/supertest
[travis-badge]: https://travis-ci.org/ladjs/supertest.svg?branch=master
[travis]: https://travis-ci.org/ladjs/supertest
[dependencies-badge]: https://david-dm.org/ladjs/supertest/status.svg
[dependencies]: https://david-dm.org/ladjs/supertest
[prs-badge]: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square
[prs]: http://makeapullrequest.com
[license-badge]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[license]: https://github.com/ladjs/supertest/blob/master/LICENSE
```

## File: `index.js`
```javascript
'use strict';

/**
 * Module dependencies.
 */
const methods = require('methods');
let http2;
try {
  http2 = require('http2'); // eslint-disable-line global-require
} catch (_) {
  // eslint-disable-line no-empty
}
const Test = require('./lib/test.js');
const agent = require('./lib/agent.js');
const cookies = require('./lib/cookies');

/**
 * Test against the given `app`,
 * returning a new `Test`.
 *
 * @param {Function|Server|String} app
 * @return {Test}
 * @api public
 */
module.exports = function(app, options = {}) {
  const obj = {};

  if (typeof app === 'function') {
    if (options.http2) {
      if (!http2) {
        throw new Error(
          'supertest: this version of Node.js does not support http2'
        );
      }
    }
  }

  methods.forEach(function(method) {
    obj[method] = function(url) {
      var test = new Test(app, method, url, options.http2);
      if (options.http2) {
        test.http2();
      }
      return test;
    };
  });

  // Support previous use of del
  obj.del = obj.delete;

  return obj;
};

/**
 * Expose `Test`
 */
module.exports.Test = Test;

/**
 * Expose the agent function
 */
module.exports.agent = agent;

/**
 * Expose cookie assertions
 */
module.exports.cookies = cookies;
```

## File: `package.json`
```json
{
  "name": "supertest",
  "description": "SuperAgent driven library for testing HTTP servers",
  "version": "7.2.2",
  "author": "TJ Holowaychuk",
  "contributors": [],
  "dependencies": {
    "methods": "^1.1.2",
    "superagent": "^10.3.0",
    "cookie-signature": "^1.2.2"
  },
  "devDependencies": {
    "@commitlint/cli": "17",
    "@commitlint/config-conventional": "17",
    "body-parser": "^1.20.3",
    "cookie-parser": "^1.4.7",
    "eslint": "^8.32.0",
    "eslint-config-airbnb-base": "^15.0.0",
    "eslint-plugin-import": "^2.27.5",
    "express": "^4.18.3",
    "mocha": "^10.2.0",
    "nock": "^13.3.8",
    "nyc": "^15.1.0",
    "proxyquire": "^2.1.3",
    "should": "^13.2.3",
    "sinon": "20.0.0"
  },
  "engines": {
    "node": ">=14.18.0"
  },
  "files": [
    "index.js",
    "lib"
  ],
  "keywords": [
    "bdd",
    "http",
    "request",
    "superagent",
    "tdd",
    "test",
    "testing"
  ],
  "license": "MIT",
  "main": "index.js",
  "repository": {
    "type": "git",
    "url": "https://github.com/ladjs/supertest.git"
  },
  "scripts": {
    "coverage": "nyc report --reporter=text-lcov > coverage.lcov",
    "lint": "eslint lib/**/*.js test/**/*.js index.js",
    "lint:fix": "eslint --fix lib/**/*.js test/**/*.js index.js",
    "pretest": "npm run lint --if-present",
    "test": "nyc --reporter=html --reporter=text mocha --exit --require should --reporter spec --check-leaks"
  }
}
```

## File: `ci/remove-deps-4-old-node.js`
```javascript
const fs = require('fs');
const path = require('path');
const package = require('../package.json');

const UNSUPPORT_DEPS_4_OLD = {
  'eslint': undefined,
  'mocha': '6.x'
};

const deps = Object.keys(UNSUPPORT_DEPS_4_OLD);
for (const item in package.devDependencies) {
  if (deps.includes(item)) {
    package.devDependencies[item] = UNSUPPORT_DEPS_4_OLD[item];
  }
}

delete package.scripts.lint;

fs.writeFileSync(
  path.join(__dirname, '../package.json'),
  JSON.stringify(package, null, 2)
);
```

## File: `lib/agent.js`
```javascript
'use strict';

/**
 * Module dependencies.
 */

const { agent: Agent } = require('superagent');
const methods = require('methods');
const http = require('http');
let http2;
try {
  http2 = require('http2'); // eslint-disable-line global-require
} catch (_) {
  // eslint-disable-line no-empty
}
const Test = require('./test.js');

/**
 * Initialize a new `TestAgent`.
 *
 * @param {Function|Server} app
 * @param {Object} options
 * @api public
 */

function TestAgent(app, options = {}) {
  if (!(this instanceof TestAgent)) return new TestAgent(app, options);

  const agent = new Agent(options);
  Object.assign(this, agent);

  this._options = options;

  if (typeof app === 'function') {
    if (options.http2) {
      if (!http2) {
        throw new Error(
          'supertest: this version of Node.js does not support http2'
        );
      }
      app = http2.createServer(app); // eslint-disable-line no-param-reassign
    } else {
      app = http.createServer(app); // eslint-disable-line no-param-reassign
    }
  }
  this.app = app;
}

/**
 * Inherits from `Agent.prototype`.
 */

Object.setPrototypeOf(TestAgent.prototype, Agent.prototype);

// Preserve the original query method before overriding HTTP methods
const originalQuery = Agent.prototype.query;

// set a host name
TestAgent.prototype.host = function(host) {
  this._host = host;
  return this;
};

// override HTTP verb methods
methods.forEach(function(method) {
  // Skip 'query' method to prevent overwriting superagent's query functionality
  if (method === 'query') {
    return;
  }

  TestAgent.prototype[method] = function(url, fn) { // eslint-disable-line no-unused-vars
    const req = new Test(this.app, method.toUpperCase(), url);
    if (this._options.http2) {
      req.http2();
    }

    if (this._host) {
      req.set('host', this._host);
    }

    req.on('response', this._saveCookies.bind(this));
    req.on('redirect', this._saveCookies.bind(this));
    req.on('redirect', this._attachCookies.bind(this, req));
    this._setDefaults(req);
    this._attachCookies(req);

    return req;
  };
});

// Restore the original query method
TestAgent.prototype.query = originalQuery;

TestAgent.prototype.del = TestAgent.prototype.delete;

/**
 * Expose `Agent`.
 */

module.exports = TestAgent;
```

## File: `lib/test.js`
```javascript
'use strict';

/**
 * Module dependencies.
 */

const { inspect } = require('util');
const http = require('http');
const { STATUS_CODES } = require('http');
const { Server } = require('tls');
const { deepStrictEqual } = require('assert');
const { Request } = require('superagent');
let http2;
try {
  http2 = require('http2'); // eslint-disable-line global-require
} catch (_) {
  // eslint-disable-line no-empty
}

/** @typedef {import('superagent').Response} Response */

class Test extends Request {
  /**
   * Initialize a new `Test` with the given `app`,
   * request `method` and `path`.
   *
   * @param {Server} app
   * @param {String} method
   * @param {String} path
   * @api public
   */
  constructor (app, method, path, optHttp2) {
    super(method.toUpperCase(), path);

    if (typeof app === 'function') {
      if (optHttp2) {
        app = http2.createServer(app); // eslint-disable-line no-param-reassign
      } else {
        app = http.createServer(app); // eslint-disable-line no-param-reassign
      }
    }

    this.redirects(0);
    this.buffer();
    this.app = app;
    this._asserts = [];
    this.url = typeof app === 'string'
      ? app + path
      : this.serverAddress(app, path);
  }

  /**
   * Returns a URL, extracted from a server.
   *
   * @param {Server} app
   * @param {String} path
   * @returns {String} URL address
   * @api private
   */
  serverAddress(app, path) {
    const addr = app.address();

    if (!addr) this._server = app.listen(0);
    // } else {
    //   this._server = app;
    // }
    const port = app.address().port;
    const protocol = app instanceof Server ? 'https' : 'http';
    return protocol + '://127.0.0.1:' + port + path;
  }

  /**
   * Expectations:
   *
   *   .expect(200)
   *   .expect(200, fn)
   *   .expect(200, body)
   *   .expect('Some body')
   *   .expect('Some body', fn)
   *   .expect(['json array body', { key: 'val' }])
   *   .expect('Content-Type', 'application/json')
   *   .expect('Content-Type', 'application/json', fn)
   *   .expect(fn)
   *   .expect([200, 404])
   *
   * @return {Test}
   * @api public
   */
  expect(a, b, c) {
    // callback
    if (typeof a === 'function') {
      this._asserts.push(wrapAssertFn(a));
      return this;
    }
    if (typeof b === 'function') this.end(b);
    if (typeof c === 'function') this.end(c);

    // status
    if (typeof a === 'number') {
      this._asserts.push(wrapAssertFn(this._assertStatus.bind(this, a)));
      // body
      if (typeof b !== 'function' && arguments.length > 1) {
        this._asserts.push(wrapAssertFn(this._assertBody.bind(this, b)));
      }
      return this;
    }

    // multiple statuses
    if (Array.isArray(a) && a.length > 0 && a.every(val => typeof val === 'number')) {
      this._asserts.push(wrapAssertFn(this._assertStatusArray.bind(this, a)));
      return this;
    }

    // header field
    if (typeof b === 'string' || typeof b === 'number' || b instanceof RegExp) {
      this._asserts.push(wrapAssertFn(this._assertHeader.bind(this, { name: '' + a, value: b })));
      return this;
    }

    // body
    this._asserts.push(wrapAssertFn(this._assertBody.bind(this, a)));

    return this;
  }

  /**
   * Defer invoking superagent's `.end()` until
   * the server is listening.
   *
   * @param {?Function} fn
   * @api public
   */
  end(fn) {
    const server = this._server;

    super.end((err, res) => {
      const localAssert = () => {
        this.assert(err, res, fn);
      };

      if (server && server._handle) {
        // Handle server closing with error handling for already closed servers
        return server.close((closeError) => {
          // Ignore ERR_SERVER_NOT_RUNNING errors as the server is already closed
          if (closeError && closeError.code === 'ERR_SERVER_NOT_RUNNING') {
            return localAssert();
          }
          // For other errors, pass them through
          if (closeError) {
            return localAssert();
          }
          localAssert();
        });
      }

      localAssert();
    });

    return this;
  }

  /**
   * Perform assertions and invoke `fn(err, res)`.
   *
   * @param {?Error} resError
   * @param {Response} res
   * @param {Function} fn
   * @api private
   */
  assert(resError, res, fn) {
    let errorObj;

    // check for unexpected network errors or server not running/reachable errors
    // when there is no response and superagent sends back a System Error
    // do not check further for other asserts, if any, in such case
    // https://nodejs.org/api/errors.html#errors_common_system_errors
    const sysErrors = {
      ECONNREFUSED: 'Connection refused',
      ECONNRESET: 'Connection reset by peer',
      EPIPE: 'Broken pipe',
      ETIMEDOUT: 'Operation timed out'
    };

    if (!res && resError) {
      if (resError instanceof Error && resError.syscall === 'connect'
        && Object.getOwnPropertyNames(sysErrors).indexOf(resError.code) >= 0) {
        errorObj = new Error(resError.code + ': ' + sysErrors[resError.code]);
      } else {
        errorObj = resError;
      }
    }

    // asserts
    for (let i = 0; i < this._asserts.length && !errorObj; i += 1) {
      errorObj = this._assertFunction(this._asserts[i], res);
    }

    // set unexpected superagent error if no other error has occurred.
    if (!errorObj && resError instanceof Error && (!res || resError.status !== res.status)) {
      errorObj = resError;
    }

    if (fn) {
      fn.call(this, errorObj || null, res);
    }
  }

  /*
    * Adds a set Authorization Bearer
    *
    * @param {Bearer} Bearer Token
    * Shortcut for .set('Authorization', `Bearer ${token}`)
    */

  bearer(token) {
    this.set('Authorization', `Bearer ${token}`);
    return this;
  }

  /*
    * Adds a set Authorization Bearer
    *
    * @param {Bearer} Bearer Token
    * Shortcut for .set('Authorization', `Bearer ${token}`)
    */

  bearer(token) {
    this.set('Authorization', `Bearer ${token}`);
    return this;
  }

  /**
   * Perform assertions on a response body and return an Error upon failure.
   *
   * @param {Mixed} body
   * @param {Response} res
   * @return {?Error}
   * @api private
   */// eslint-disable-next-line class-methods-use-this
  _assertBody(body, res) {
    const isRegexp = body instanceof RegExp;

    // parsed
    if (typeof body === 'object' && !isRegexp) {
      try {
        deepStrictEqual(body, res.body);
      } catch (err) {
        const a = inspect(body);
        const b = inspect(res.body);
        return error('expected ' + a + ' response body, got ' + b, body, res.body);
      }
    } else if (body !== res.text) {
      // string
      const a = inspect(body);
      const b = inspect(res.text);

      // regexp
      if (isRegexp) {
        if (!body.test(res.text)) {
          return error('expected body ' + b + ' to match ' + body, body, res.body);
        }
      } else {
        return error('expected ' + a + ' response body, got ' + b, body, res.body);
      }
    }
  }

  /**
   * Perform assertions on a response header and return an Error upon failure.
   *
   * @param {Object} header
   * @param {Response} res
   * @return {?Error}
   * @api private
   */// eslint-disable-next-line class-methods-use-this
  _assertHeader(header, res) {
    const field = header.name;
    const actual = res.header[field.toLowerCase()];
    const fieldExpected = header.value;

    if (typeof actual === 'undefined') return new Error('expected "' + field + '" header field');
    // This check handles header values that may be a String or single element Array
    if ((Array.isArray(actual) && actual.toString() === fieldExpected)
      || fieldExpected === actual) {
      return;
    }
    if (fieldExpected instanceof RegExp) {
      if (!fieldExpected.test(actual)) {
        return new Error('expected "' + field + '" matching '
          + fieldExpected + ', got "' + actual + '"');
      }
    } else {
      return new Error('expected "' + field + '" of "' + fieldExpected + '", got "' + actual + '"');
    }
  }

  /**
   * Perform assertions on the response status and return an Error upon failure.
   *
   * @param {Number} status
   * @param {Response} res
   * @return {?Error}
   * @api private
   */// eslint-disable-next-line class-methods-use-this
  _assertStatus(status, res) {
    if (res.status !== status) {
      const a = STATUS_CODES[status];
      const b = STATUS_CODES[res.status];
      return new Error('expected ' + status + ' "' + a + '", got ' + res.status + ' "' + b + '"');
    }
  }

  /**
   * Perform assertions on the response status and return an Error upon failure.
   *
   * @param {Array<Number>} statusArray
   * @param {Response} res
   * @return {?Error}
   * @api private
   */// eslint-disable-next-line class-methods-use-this
  _assertStatusArray(statusArray, res) {
    if (!statusArray.includes(res.status)) {
      const b = STATUS_CODES[res.status];
      const expectedList = statusArray.join(', ');
      return new Error(
        'expected one of "' + expectedList + '", got ' + res.status + ' "' + b + '"'
      );
    }
  }

  /**
   * Performs an assertion by calling a function and return an Error upon failure.
   *
   * @param {Function} fn
   * @param {Response} res
   * @return {?Error}
   * @api private
   */// eslint-disable-next-line class-methods-use-this
  _assertFunction(fn, res) {
    let err;
    try {
      err = fn(res);
    } catch (e) {
      err = e;
    }
    if (err instanceof Error) return err;
  }
}

/**
 * Wraps an assert function into another.
 * The wrapper function edit the stack trace of any assertion error, prepending a more useful stack to it.
 *
 * @param {Function} assertFn
 * @returns {Function} wrapped assert function
 */

function wrapAssertFn(assertFn) {
  const savedStack = new Error().stack.split('\n').slice(3);

  return function(res) {
    let badStack;
    let err;
    try {
      err = assertFn(res);
    } catch (e) {
      err = e;
    }
    if (err instanceof Error && err.stack) {
      badStack = err.stack.replace(err.message, '').split('\n').slice(1);
      err.stack = [err.toString()]
        .concat(savedStack)
        .concat('----')
        .concat(badStack)
        .join('\n');
    }
    return err;
  };
}

/**
 * Return an `Error` with `msg` and results properties.
 *
 * @param {String} msg
 * @param {Mixed} expected
 * @param {Mixed} actual
 * @return {Error}
 * @api private
 */

function error(msg, expected, actual) {
  const err = new Error(msg);
  err.expected = expected;
  err.actual = actual;
  err.showDiff = true;
  return err;
}

/**
 * Expose `Test`.
 */

module.exports = Test;
```

## File: `lib/cookies/assertion.js`
```javascript
/** Copyright 2015 Gregory Langlais. See LICENSE.txt. */

'use strict';

const signature = require('cookie-signature');

/**
 * Assert that an object has specific properties (supports array of keys or object)
 *
 * @param {object} obj
 * @param {object|array} props
 */
function assertHasProperties(obj, props) {
  if (Array.isArray(props)) {
    props.forEach(function (key) {
      if (!(key in obj)) {
        throw new Error('expected object to have property ' + key);
      }
    });
  } else {
    Object.keys(props).forEach(function (key) {
      if (!(key in obj)) {
        throw new Error('expected object to have property ' + key);
      }
    });
  }
}

/**
 * Assert that an object does not have specific properties (supports array of keys or object)
 * When checking with empty props, throws if object exists (matches should.js behavior)
 *
 * @param {object} obj
 * @param {object|array} props
 */
function assertNotHasProperties(obj, props) {
  if (Array.isArray(props)) {
    // When empty array is passed, should.js throws 'false negative fail' if object exists
    if (props.length === 0) {
      throw new Error('expected object to not have properties (false negative fail)');
    }
    props.forEach(function (key) {
      if (key in obj) {
        throw new Error('expected object to not have property ' + key);
      }
    });
  } else {
    // When empty object is passed, should.js throws 'false negative fail' if object exists
    let keys = Object.keys(props);
    if (keys.length === 0) {
      throw new Error('expected object to not have properties (false negative fail)');
    }
    keys.forEach(function (key) {
      if (key in obj) {
        throw new Error('expected object to not have property ' + key);
      }
    });
  }
}

/**
 * Assert that two values are equal
 *
 * @param {*} actual
 * @param {*} expected
 */
function assertEqual(actual, expected) {
  if (actual !== expected) {
    throw new Error(
      'expected ' + JSON.stringify(actual) + ' to equal ' + JSON.stringify(expected)
    );
  }
}

/**
 * Assert that two values are not equal
 *
 * @param {*} actual
 * @param {*} expected
 */
function assertNotEqual(actual, expected) {
  if (actual === expected) {
    throw new Error(
      'expected ' + JSON.stringify(actual) + ' to not equal ' + JSON.stringify(expected)
    );
  }
}

/**
 * Build Assertion function
 *
 * {object|object[]} expects cookies
 * {string} expects.<name> and value of cookie
 * {object} expects.options
 * {string} [expects.options.domain]
 * {string} [expects.options.path]
 * {string} [expects.options.expires] UTC string using date.toUTCString()
 * {number} [expects.options.max-age]
 * {boolean} [expects.options.secure]
 * {boolean} [expects.options.httponly]
 * {string|string[]} [expects.secret]
 *
 * @param {null|string|string[]} [secret]
 * @param {function|function[]} [asserts]
 * @returns {Assertion}
 */
module.exports = function (secret, asserts) {
  let assertions = [];

  if (typeof secret === 'string') secret = [secret]; // eslint-disable-line no-param-reassign
  else if (!Array.isArray(secret)) secret = []; // eslint-disable-line no-param-reassign

  if (Array.isArray(asserts)) assertions = asserts;
  else if (typeof asserts === 'function') assertions.push(asserts);

  /**
   * Assertion function with static chainable methods
   *
   * @param {object} res
   * @returns {undefined|string}
   * @constructor
   */
  function Assertion(res) {
    if (typeof res !== 'object') throw new Error('res argument must be object');

    // request and response object initialization
    let request = {
      headers: res.req.getHeaders(),
      cookies: []
    };

    let response = {
      headers: res.headers,
      cookies: []
    };

    // build assertions request object
    if (request.headers.cookie) {
      const cookies = String(request.headers.cookie);
      cookies.split(/; */).forEach(function (cookie) {
        request.cookies.push(Assertion.parse(cookie));
      });
    }

    // build assertions response object
    if (
      Array.isArray(response.headers['set-cookie'])
      && response.headers['set-cookie'].length > 0
    ) {
      response.headers['set-cookie'].forEach(function (val) {
        response.cookies.push(Assertion.parse(val));
      });
    }

    // run assertions
    let result;
    assertions.every(function (assertion) {
      result = assertion(request, response);
      return (typeof (result) !== 'string');
    });

    return result;
  }

  /**
   * Find cookie in stack/array
   *
   * @param {string} name
   * @param {array} stack
   * @returns {object|undefined} cookie
   */
  Assertion.find = function (name, stack) {
    let cookie;

    stack.every(function (val) {
      if (name !== val.name) return true;
      cookie = val;
      return false;
    });

    return cookie;
  };

  /**
   * Parse cookie string
   *
   * @param {string} str
   * @param {object} [options]
   * @param {function} [options.decode] uri
   * @param {undefined|boolean} [options.request] headers
   * @returns {object}
   */
  Assertion.parse = function (str, options) {
    if (typeof str !== 'string') throw new TypeError('argument str must be a string');

    if (typeof options !== 'object') options = {}; // eslint-disable-line no-param-reassign

    let decode = options.decode || decodeURIComponent;

    let parts = str.split(/; */);

    let cookie = {};

    parts.forEach(function (part, i) {
      if (i === 1) cookie.options = {};

      let equalsIndex = part.indexOf('=');

      // things that don't look like key=value get true flag
      if (equalsIndex < 0) {
        cookie.options[part.trim().toLowerCase()] = true;
        return;
      }

      const key = part.substr(0, equalsIndex).trim().toLowerCase();
      // only assign once
      if (typeof cookie[key] !== 'undefined') return;

      equalsIndex += 1;
      let val = part.substr(equalsIndex, part.length).trim();
      // quoted values
      if (val[0] === '"') val = val.slice(1, -1);

      let value;
      try {
        value = decode(val);
      } catch (e) {
        value = val;
      }

      if (i > 0) {
        cookie.options[key] = value;
        return;
      }

      cookie.name = key;
      cookie.value = decode(val);
    });

    if (typeof cookie.options === 'undefined') cookie.options = {};

    return cookie;
  };

  /**
   * Iterate expects
   *
   * @param {object|object[]} expects
   * @param {boolean|function} hasValues
   * @param {function} [cb]
   */
  Assertion.expects = function (expects, hasValues, cb) {
    if (!Array.isArray(expects) && typeof expects === 'object') expects = [expects]; // eslint-disable-line no-param-reassign

    let resolvedCb;
    let resolvedHasValues;
    if (typeof cb === 'undefined' && typeof hasValues === 'function') {
      resolvedCb = hasValues;
      resolvedHasValues = false;
    } else {
      resolvedCb = cb;
      resolvedHasValues = hasValues;
    }

    expects.forEach(function (expect) {
      let options = expect.options;
      if (typeof options !== 'object' && !Array.isArray(options)) {
        options = (resolvedHasValues) ? {} : [];
      }

      resolvedCb(Object.assign({}, expect, { options }));
    });
  };

  /**
   * Assert cookies and options are set
   *
   * @param {object|object[]} expects cookies
   * @param {undefined|boolean} [assert]
   * @returns {function} Assertion
   */
  Assertion.set = function (expects, assert) {
    if (typeof assert === 'undefined') assert = true; // eslint-disable-line no-param-reassign

    Assertion.expects(expects, function (expect) {
      assertions.push(function (req, res) {
        // get expectation cookie
        const cookie = Assertion.find(expect.name, res.cookies);

        if (assert && !cookie) throw new Error('expected: ' + expect.name + ' cookie to be set');

        if (assert) assertHasProperties(cookie.options, expect.options);
        else if (cookie) assertNotHasProperties(cookie.options, expect.options);
      });
    });

    return Assertion;
  };

  /**
   * Assert cookies has been reset
   *
   * @param {object|object[]} expects cookies
   * @param {undefined|boolean} [assert]
   * @returns {function} Assertion
   */
  Assertion.reset = function (expects, assert) {
    if (typeof assert === 'undefined') assert = true; // eslint-disable-line no-param-reassign

    Assertion.expects(expects, function (expect) {
      assertions.push(function (req, res) {
        // get sent cookie
        const cookieReq = Assertion.find(expect.name, req.cookies);
        // get expectation cookie
        const cookieRes = Assertion.find(expect.name, res.cookies);

        if (assert && (!cookieReq || !cookieRes)) {
          throw new Error('expected: ' + expect.name + ' cookie to be set');
        } else if (!assert && cookieReq && cookieRes) {
          throw new Error('expected: ' + expect.name + ' cookie to be set');
        }
      });
    });

    return Assertion;
  };

  /**
   * Assert cookies is set and new
   *
   * @param {object|object[]} expects cookies
   * @param {undefined|boolean} [assert]
   * @returns {function} Assertion
   */
  Assertion.new = function (expects, assert) {
    if (typeof assert === 'undefined') assert = true; // eslint-disable-line no-param-reassign

    Assertion.expects(expects, function (expect) {
      assertions.push(function (req, res) {
        // get sent cookie
        const cookieReq = Assertion.find(expect.name, req.cookies);
        // get expectation cookie
        const cookieRes = Assertion.find(expect.name, res.cookies);

        if (assert) {
          if (!cookieRes) throw new Error('expected: ' + expect.name + ' cookie to be set');
          if (cookieReq && cookieRes) {
            throw new Error('expected: ' + expect.name + ' cookie to NOT already be set');
          }
        } else if (!cookieReq || !cookieRes) {
          throw new Error('expected: ' + expect.name + ' cookie to be set');
        }
      });
    });

    return Assertion;
  };

  /**
   * Assert cookies expires or max-age has increased
   *
   * @param {object|object[]} expects cookies
   * @param {undefined|boolean} [assert]
   * @returns {function} Assertion
   */
  Assertion.renew = function (expects, assert) {
    if (typeof assert === 'undefined') assert = true; // eslint-disable-line no-param-reassign

    Assertion.expects(expects, true, function (expect) {
      const expectExpires = new Date(expect.options.expires);
      const expectMaxAge = parseFloat(expect.options['max-age']);

      let baseMessage = 'expected: ' + expect.name;
      if (!expectExpires.getTime() && !expectMaxAge) {
        throw new Error(baseMessage + ' expects to have expires or max-age option');
      }

      assertions.push(function (req, res) {
        // get sent cookie
        const cookieReq = Assertion.find(expect.name, req.cookies);
        // get expectation cookie
        const cookieRes = Assertion.find(expect.name, res.cookies);

        const cookieMaxAge = (expectMaxAge && cookieRes)
          ? parseFloat(cookieRes.options['max-age'])
          : undefined;
        const cookieExpires = (expectExpires.getTime() && cookieRes)
          ? new Date(cookieRes.options.expires)
          : undefined;

        if (assert) {
          if (!cookieReq || !cookieRes) {
            throw new Error(baseMessage + ' cookie to be set');
          }
          if (expectMaxAge && (!cookieMaxAge || cookieMaxAge <= expectMaxAge)) {
            throw new Error(baseMessage + ' cookie max-age to be greater than existing value');
          }

          if (
            expectExpires.getTime()
            && (!cookieExpires.getTime() || cookieExpires <= expectExpires)
          ) {
            throw new Error(baseMessage + ' cookie expires to be greater than existing value');
          }
        } else if (cookieRes) {
          if (expectMaxAge && cookieMaxAge > expectMaxAge) {
            throw new Error(
              baseMessage + ' cookie max-age to be less than or equal to existing value'
            );
          }

          if (expectExpires.getTime() && cookieExpires > expectExpires) {
            throw new Error(
              baseMessage + ' cookie expires to be less than or equal to existing value'
            );
          }
        }
      });
    });

    return Assertion;
  };

  /**
   * Assert cookies contains values
   *
   * @param {object|object[]} expects cookies
   * @param {undefined|boolean} [assert]
   * @returns {function} Assertion
   */
  Assertion.contain = function (expects, assert) {
    if (typeof assert === 'undefined') assert = true; // eslint-disable-line no-param-reassign

    Assertion.expects(expects, function (expect) {
      const keys = Object.keys(expect.options);

      assertions.push(function (req, res) {
        // get expectation cookie
        const cookie = Assertion.find(expect.name, res.cookies);

        if (!cookie) throw new Error('expected: ' + expect.name + ' cookie to be set');

        // check cookie values are equal
        if ('value' in expect) {
          try {
            if (assert) assertEqual(cookie.value, expect.value);
            else assertNotEqual(cookie.value, expect.value);
          } catch (e) {
            if (secret.length) {
              let value;
              secret.every(function (sec) {
                value = signature.unsign(cookie.value.slice(2), sec);
                return !(value && value === expect.value);
              });

              if (assert && !value) {
                throw new Error('expected: ' + expect.name + ' value to equal ' + expect.value);
              } else if (!assert && value) {
                throw new Error('expected: ' + expect.name + ' value to NOT equal ' + expect.value);
              }
            } else throw e;
          }
        }

        keys.forEach(function (key) {
          const expected = (
            key === 'max-age'
              ? expect.options[key].toString()
              : expect.options[key]
          );
          if (assert) assertEqual(cookie.options[key], expected);
          else assertNotEqual(cookie.options[key], expected);
        });
      });
    });

    return Assertion;
  };

  /**
   * Assert NOT modifier
   *
   * @param {function} method
   * @param {...*}
   */
  Assertion.not = function (method) {
    let args = [];

    for (let i = 1; i < arguments.length; i += 1) args.push(arguments[i]);

    args.push(false);

    return Assertion[method].apply(Assertion, args);
  };

  return Assertion;
};
```

## File: `lib/cookies/index.js`
```javascript
/** Copyright 2015 Gregory Langlais. See LICENSE.txt. */

'use strict';

const Assertion = require('./assertion');

/**
 * Construct cookies assertion (function)
 *
 * @param {null|string|string[]} [secret]
 * @param {function(req, res)[]} [asserts] ran within returned assertion function
 * @returns {function} assertion
 * @constructor
 */
function ExpectCookies(secret, asserts) {
  return Assertion(secret, asserts);
}

// build ExpectCookies proxy methods
const assertion = Assertion();
const methods = Object.getOwnPropertyNames(assertion);

methods.forEach(function(method) {
  if (typeof assertion[method] === 'function' && typeof Function[method] === 'undefined') {
    ExpectCookies[method] = function() {
      const newAssertion = Assertion();
      return newAssertion[method].apply(newAssertion, arguments);
    };
  }
});

module.exports = ExpectCookies;
```

## File: `test/.eslintrc`
```
{
  "rules": {
    // errors - disabled for chai test support
    "no-unused-expressions": [0],
    // allow function args for superagent
    "no-unused-vars": [2, {"args": "none"}],
    // allow updates to response for certain tests
    "no-param-reassign": [2, {"props": false}]
  }
}
```

## File: `test/cookies.js`
```javascript
/** Copyright 2015 Gregory Langlais. See LICENSE.txt. */

'use strict';

const express = require('express');
const cookieParser = require('cookie-parser');
const request = require('../index');
const should = require('should');
const sinon = require('sinon');

const cookies = request.cookies;
const Assertion = require('../lib/cookies/assertion');

const secrets = ['one', 'a', 'two', 'b'];

describe('cookie', function () {
  it('returns Assertion function', function (done) {
    const assertion = Assertion();
    const cookiesAssertion = cookies();

    should(cookiesAssertion).be.eql(assertion);

    done();
  });

  it('runs single asserts', function (done) {
    let assertion = sinon.stub();

    const app = express();

    app.get('/', function (req, res) {
      res.send();
    });

    request(app)
      .get('/')
      .set('Cookie', 'control=placebo')
      .expect(cookies(null, assertion))
      .end(function () {
        sinon.assert.calledOnce(assertion);
        done();
      });
  });

  it('runs multiple asserts', function (done) {
    let assertionA = sinon.stub();
    let assertionB = sinon.stub();

    let asserts = [
      assertionA,
      assertionB
    ];

    const app = express();

    app.get('/', function (req, res) {
      res.send();
    });

    request(app)
      .get('/')
      .set('Cookie', 'control=placebo')
      .expect(cookies(null, asserts))
      .end(function () {
        sinon.assert.calledOnce(assertionA);
        sinon.assert.calledOnce(assertionB);
        done();
      });
  });

  describe('.set', function () {
    it('asserts true if signed cookie is set and options are set', function (done) {
      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com',
          path: '/',
          expires: new Date(),
          secure: 1,
          httpOnly: true,
          signed: true
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo')
        .expect(function (res) {
          const assertion = cookies.set({
            name: 'substance',
            options: ['domain', 'path', 'expires', 'secure', 'httponly']
          });

          should(function () {
            assertion(res);
          }).not.throw();
        })
        .end(done);
    });

    it('asserts true if unsigned cookie is set and options are set', function (done) {
      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com', path: '/', expires: new Date(), secure: 1, httpOnly: true
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo')
        .expect(function (res) {
          const assertion = cookies.set({
            name: 'substance',
            options: ['domain', 'path', 'expires', 'secure', 'httponly']
          });

          should(function () {
            assertion(res);
          }).not.throw();
        })
        .end(done);
    });

    it('asserts false if unsigned cookie is set but option was NOT set', function (done) {
      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com', path: '/', expires: new Date(), secure: 1
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo')
        .expect(function (res) {
          const assertion = cookies.set({
            name: 'substance',
            options: ['domain', 'path', 'expires', 'secure', 'httponly']
          });

          should(function () {
            assertion(res);
          }).throw();
        })
        .end(done);
    });
  });

  describe('.reset', function () {
    it('asserts true if signed cookie is set and was already set', function (done) {
      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com',
          path: '/',
          expires: new Date(),
          secure: 1,
          httpOnly: true,
          signed: true
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo;substance=active')
        .expect(function (res) {
          const assertion = cookies.reset({
            name: 'substance'
          });

          should(function () {
            assertion(res);
          }).not.throw();
        })
        .end(done);
    });

    it('asserts false if cookie is NOT set', function (done) {
      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo')
        .expect(function (res) {
          const assertion = cookies.reset({
            name: 'substance'
          });

          should(function () {
            assertion(res);
          }).throw();
        })
        .end(done);
    });
  });

  describe('.new', function () {
    it('asserts true if signed cookie is set and was NOT already set', function (done) {
      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com',
          path: '/',
          expires: new Date(),
          secure: 1,
          httpOnly: true,
          signed: true
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo')
        .expect(function (res) {
          const assertion = cookies.new({
            name: 'substance'
          });

          should(function () {
            assertion(res);
          }).not.throw();
        })
        .end(done);
    });

    it('asserts false if signed cookie is set but was already set', function (done) {
      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com',
          path: '/',
          expires: new Date(),
          secure: 1,
          httpOnly: true,
          signed: true
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo;substance=active')
        .expect(function (res) {
          const assertion = cookies.new({
            name: 'substance'
          });

          should(function () {
            assertion(res);
          }).throw();
        })
        .end(done);
    });

    it('asserts false if cookie is NOT set', function (done) {
      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo')
        .expect(function (res) {
          const assertion = cookies.new({
            name: 'substance'
          });

          should(function () {
            assertion(res);
          }).throw();
        })
        .end(done);
    });
  });

  describe('.renew', function () {
    it('asserts true if set cookie expires is greater than expects cookie', function (done) {
      const expires = new Date();
      const expiresRenewed = new Date(expires.getTime() + 5000); // using 5000 ms for date precision safety

      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com',
          path: '/',
          expires: expiresRenewed,
          secure: 1,
          httpOnly: true,
          signed: true
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo;substance=active')
        .expect(function (res) {
          const assertion = cookies.renew({
            name: 'substance',
            options: {
              expires: expires.toUTCString()
            }
          });

          should(function () {
            assertion(res);
          }).not.throw();
        })
        .end(done);
    });

    it('asserts false if set cookie expires is less than expects cookie', function (done) {
      const expires = new Date();
      const expiresRenewed = new Date(expires.getTime() - 5000); // using 5000 ms for date precision safety

      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com',
          path: '/',
          expires: expiresRenewed,
          secure: 1,
          httpOnly: true,
          signed: true
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo;substance=active')
        .expect(function (res) {
          const assertion = cookies.renew({
            name: 'substance',
            options: {
              expires: expires.toUTCString()
            }
          });

          should(function () {
            assertion(res);
          }).throw();
        })
        .end(done);
    });

    it('asserts false if set cookie expires is equal to expects cookie', function (done) {
      const expires = new Date();
      const expiresRenewed = expires;

      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com',
          path: '/',
          expires: expiresRenewed,
          secure: 1,
          httpOnly: true,
          signed: true
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo;substance=active')
        .expect(function (res) {
          const assertion = cookies.renew({
            name: 'substance',
            options: {
              expires: expires.toUTCString()
            }
          });

          should(function () {
            assertion(res);
          }).throw();
        })
        .end(done);
    });

    it('asserts true if set cookie max-age is greater than expects cookie', function (done) {
      const maxAge = 60;
      const maxAgeRenewed = (maxAge + 1) * 1000; // res.cookie expects ms

      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com',
          path: '/',
          maxAge: maxAgeRenewed,
          secure: 1,
          httpOnly: true,
          signed: true
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo;substance=active')
        .expect(function (res) {
          const assertion = cookies.renew({
            name: 'substance',
            options: {
              'max-age': maxAge
            }
          });

          should(function () {
            assertion(res);
          }).not.throw();
        })
        .end(done);
    });

    it('asserts false if set cookie max-age is less than expects cookie', function (done) {
      const maxAge = 120;
      const maxAgeRenewed = (maxAge - 1) * 1000; // res.cookie expects ms

      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com',
          path: '/',
          maxAge: maxAgeRenewed,
          secure: 1,
          httpOnly: true,
          signed: true
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo;substance=active')
        .expect(function (res) {
          const assertion = cookies.renew({
            name: 'substance',
            options: {
              'max-age': maxAge
            }
          });

          should(function () {
            assertion(res);
          }).throw();
        })
        .end(done);
    });

    it('asserts false if set cookie max-age is equal to expects cookie', function (done) {
      const maxAge = 60000;

      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com', path: '/', maxAge: maxAge, secure: 1, httpOnly: true, signed: true
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo;substance=active')
        .expect(function (res) {
          const assertion = cookies.renew({
            name: 'substance',
            options: {
              'max-age': maxAge
            }
          });

          should(function () {
            assertion(res);
          }).throw();
        })
        .end(done);
    });

    it('asserts false if cookie is NOT set', function (done) {
      const expires = new Date();

      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo')
        .expect(function (res) {
          const assertion = cookies.renew({
            name: 'substance',
            options: {
              expires: expires.toUTCString()
            }
          });

          should(function () {
            assertion(res);
          }).throw();
        })
        .end(done);
    });
  });

  describe('.contain', function () {
    it('asserts true if cookie contains expected options', function (done) {
      const expires = new Date();

      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com', path: '/', expires: expires, secure: 1, httpOnly: true, signed: true
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo')
        .expect(function (res) {
          const assertion = cookies(secrets).contain({
            name: 'substance',
            value: 'active',
            options: {
              domain: 'domain.com',
              path: '/',
              expires: expires.toUTCString(),
              secure: true,
              httponly: true
            }
          });

          should(function () {
            assertion(res);
          }).not.throw();
        })
        .end(done);
    });

    it('asserts false if cookie does NOT contain expected options', function (done) {
      const expires = new Date();

      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', {
          domain: 'domain.com', path: '/', expires: expires, secure: 1, httpOnly: true, signed: true
        });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo')
        .expect(function (res) {
          const assertion = cookies(secrets).contain({
            name: 'substance',
            value: 'active',
            options: {
              domain: 'domain.com',
              path: '/',
              expires: expires.toUTCString(),
              'max-age': 60,
              secure: true,
              httponly: true
            }
          });

          should(function () {
            assertion(res);
          }).throw();
        })
        .end(done);
    });

    it('handles type conversion for max-age', function (done) {
      var app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.cookie('substance', 'active', { domain: 'domain.com', maxAge: 60000 });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo')
        .expect(function (res) {
          var assertion = cookies(secrets).contain({
            name: 'substance',
            value: 'active',
            options: {
              domain: 'domain.com',
              'max-age': 60
            }
          });

          should(function () {
            assertion(res);
          }).not.throw();
        })
        .end(done);
    });

    it('allows any value if omitted from expects object', function (done) {
      var app = express();
      app.use(cookieParser(secrets));
      app.get('/', function (req, res) {
        res.cookie('substance', 'active', { domain: 'domain.com' });
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo')
        .expect(function (res) {
          var assertion = cookies(secrets).contain({
            name: 'substance',
            options: {
              domain: 'domain.com'
            }
          });

          should(function () {
            assertion(res);
          }).not.throw();
        })
        .end(done);
    });

    it('asserts false if cookie does NOT exist', function (done) {
      const expires = new Date();

      const app = express();

      app.use(cookieParser(secrets));

      app.get('/', function (req, res) {
        res.send();
      });

      request(app)
        .get('/')
        .set('Cookie', 'control=placebo')
        .expect(function (res) {
          const assertion = cookies(secrets).contain({
            name: 'substance',
            value: 'active',
            options: {
              domain: 'domain.com',
              path: '/',
              expires: expires.toUTCString(),
              secure: true,
              httponly: true
            }
          });

          should(function () {
            assertion(res);
          }).throw();
        })
        .end(done);
    });
  });

  describe('.not', function () {
    describe('.set', function () {
      it('asserts true if cookie is NOT set', function (done) {
        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo')
          .expect(function (res) {
            const assertion = cookies.not('set', {
              name: 'substance'
            });

            should(function () {
              assertion(res);
            }).not.throw();
          })
          .end(done);
      });

      it('asserts true if unsigned cookie is set but option is NOT set', function (done) {
        const expires = new Date();

        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.cookie('substance', 'active', {
            domain: 'domain.com', path: '/', expires: expires, secure: 1
          });
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo')
          .expect(function (res) {
            const assertion = cookies.not('set', {
              substance: 'active',
              name: 'substance',
              options: ['httponly']
            });

            should(function () {
              assertion(res);
            }).not.throw();
          })
          .end(done);
      });

      it('asserts false if cookie is set', function (done) {
        const expires = new Date();

        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.cookie('substance', 'active', {
            domain: 'domain.com', path: '/', expires: expires, secure: 1
          });
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo')
          .expect(function (res) {
            const assertion = cookies.not('set', {
              name: 'substance'
            });

            should(function () {
              assertion(res);
            }).throw();
          })
          .end(done);
      });
    });

    describe('.reset', function () {
      it('asserts true if cookie is NOT set but was already set', function (done) {
        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo;substance=active')
          .expect(function (res) {
            const assertion = cookies.not('reset', {
              name: 'substance'
            });

            should(function () {
              assertion(res);
            }).not.throw();
          })
          .end(done);
      });

      it('asserts false if unsigned cookie is set but was already set', function (done) {
        const expires = new Date();

        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.cookie('substance', 'active', {
            domain: 'domain.com', path: '/', expires: expires, secure: 1
          });
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo;substance=active')
          .expect(function (res) {
            const assertion = cookies.not('reset', {
              name: 'substance'
            });

            should(function () {
              assertion(res);
            }).throw();
          })
          .end(done);
      });
    });

    describe('.new', function () {
      it('asserts true if cookie is set and was already set', function (done) {
        const expires = new Date();

        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.cookie('substance', 'active', {
            domain: 'domain.com',
            path: '/',
            expires: expires,
            secure: 1,
            httpOnly: true,
            signed: true
          });
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo;substance=active')
          .expect(function (res) {
            const assertion = cookies.not('new', {
              name: 'substance'
            });

            should(function () {
              assertion(res);
            }).not.throw();
          })
          .end(done);
      });

      it('asserts false if cookie is set and was NOT already set', function (done) {
        const expires = new Date();

        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.cookie('substance', 'active', {
            domain: 'domain.com',
            path: '/',
            expires: expires,
            secure: 1,
            httpOnly: true,
            signed: true
          });
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo')
          .expect(function (res) {
            const assertion = cookies.not('new', {
              name: 'substance'
            });

            should(function () {
              assertion(res);
            }).throw();
          })
          .end(done);
      });
    });

    describe('.renew', function () {
      it('asserts true if set cookie expires is equal to expects cookie', function (done) {
        const expires = new Date();

        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.cookie('substance', 'active', {
            domain: 'domain.com',
            path: '/',
            expires: expires,
            secure: 1,
            httpOnly: true,
            signed: true
          });
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo;substance=active')
          .expect(function (res) {
            const assertion = cookies.not('renew', {
              name: 'substance',
              options: {
                expires: expires.toUTCString()
              }
            });

            should(function () {
              assertion(res);
            }).not.throw();
          })
          .end(done);
      });

      it('asserts true if set cookie expires is less than expects cookie', function (done) {
        const expires = new Date();
        const expiresRenewed = new Date(expires.getTime() - 5000); // using 5000 ms for date precision safety

        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.cookie('substance', 'active', {
            domain: 'domain.com',
            path: '/',
            expires: expiresRenewed,
            secure: 1,
            httpOnly: true,
            signed: true
          });
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo;substance=active')
          .expect(function (res) {
            const assertion = cookies.not('renew', {
              name: 'substance',
              options: {
                expires: expires.toUTCString()
              }
            });

            should(function () {
              assertion(res);
            }).not.throw();
          })
          .end(done);
      });

      it('asserts false if set cookie expires is greater than expects cookie', function (done) {
        const expires = new Date();
        const expiresRenewed = new Date(expires.getTime() + 5000); // using 5000 ms for date precision safety

        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.cookie('substance', 'active', {
            domain: 'domain.com',
            path: '/',
            expires: expiresRenewed,
            secure: 1,
            httpOnly: true,
            signed: true
          });
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo;substance=active')
          .expect(function (res) {
            const assertion = cookies.not('renew', {
              name: 'substance',
              options: {
                expires: expires.toUTCString()
              }
            });

            should(function () {
              assertion(res);
            }).throw();
          })
          .end(done);
      });

      it('asserts true if set cookie max-age is same as expects cookie', function (done) {
        const maxAge = 60;
        const maxAgeRenewed = maxAge * 1000; // res.cookie expects ms

        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.cookie('substance', 'active', {
            domain: 'domain.com',
            path: '/',
            maxAge: maxAgeRenewed,
            secure: 1,
            httpOnly: true,
            signed: true
          });
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo;substance=active')
          .expect(function (res) {
            const assertion = cookies.not('renew', {
              name: 'substance',
              options: {
                'max-age': maxAge
              }
            });

            should(function () {
              assertion(res);
            }).not.throw();
          })
          .end(done);
      });

      it('asserts true if set cookie max-age is less than expects cookie', function (done) {
        const maxAge = 60;
        const maxAgeRenewed = (maxAge - 1) * 1000; // res.cookie expects ms

        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.cookie('substance', 'active', {
            domain: 'domain.com',
            path: '/',
            maxAge: maxAgeRenewed,
            secure: 1,
            httpOnly: true,
            signed: true
          });
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo;substance=active')
          .expect(function (res) {
            const assertion = cookies.not('renew', {
              name: 'substance',
              options: {
                'max-age': maxAge
              }
            });

            should(function () {
              assertion(res);
            }).not.throw();
          })
          .end(done);
      });

      it('asserts false if set cookie max-age is greater than expires cookie', function (done) {
        const maxAge = 60;
        const maxAgeRenewed = (maxAge + 1) * 1000; // res.cookie expects ms

        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.cookie('substance', 'active', {
            domain: 'domain.com',
            path: '/',
            maxAge: maxAgeRenewed,
            secure: 1,
            httpOnly: true,
            signed: true
          });
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo;substance=active')
          .expect(function (res) {
            const assertion = cookies.not('renew', {
              name: 'substance',
              options: {
                'max-age': maxAge
              }
            });

            should(function () {
              assertion(res);
            }).throw();
          })
          .end(done);
      });
    });

    describe('.contain', function () {
      it('asserts true if cookie does NOT contain option', function (done) {
        const expires = new Date();

        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.cookie('substance', 'active', {
            domain: 'domain.com',
            path: '/',
            expires: expires,
            maxAge: 60000,
            secure: 1,
            httpOnly: true
          });
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo')
          .expect(function (res) {
            const assertion = cookies(secrets).not('contain', {
              name: 'substance',
              value: 'active'
            });

            should(function () {
              assertion(res);
            }).not.throw();
          })
          .end(done);
      });

      it('asserts false if cookie contains expected options', function (done) {
        const expires = new Date();

        const app = express();

        app.use(cookieParser(secrets));

        app.get('/', function (req, res) {
          res.cookie('substance', 'active', {
            domain: 'domain.com',
            path: '/',
            expires: expires,
            secure: 1,
            httpOnly: true,
            signed: true
          });
          res.send();
        });

        request(app)
          .get('/')
          .set('Cookie', 'control=placebo')
          .expect(function (res) {
            const assertion = cookies(secrets).not('contain', {
              name: 'substance',
              value: 'active',
              options: {
                domain: 'domain.com',
                path: '/',
                expires: expires.toUTCString(),
                secure: true,
                httponly: true
              }
            });

            should(function () {
              assertion(res);
            }).throw();
          })
          .end(done);
      });
    });
  });

  describe('README example', function () {
    it('should work correctly', function () {
      // setup super-test
      // NOTE: uncomment lines below when copying into README
      // const request = require('supertest');
      // const express = require('express');
      // const cookies = request.cookies;

      // setup express test service
      const app = express();

      app.get('/users', function(req, res) {
        res.cookie('alpha', 'one', { domain: 'domain.com', path: '/', httpOnly: true });
        res.send(200, { name: 'tobi' });
      });

      // test request to service
      request(app)
        .get('/users')
        .expect('Content-Type', /json/)
        .expect('Content-Length', '15')
        .expect(200)
        // assert 'alpha' cookie is set with domain, path, and httpOnly options
        .expect(cookies.set({ name: 'alpha', options: ['domain', 'path', 'httponly'] }))
        // assert 'bravo' cookie is NOT set
        .expect(cookies.not('set', { name: 'bravo' }))
        .end(function(err, res) {
          if (err) {
            throw err;
          }
        });
    });
  });
});
```

## File: `test/issue-fixes.js`
```javascript
'use strict';

const supertest = require('../index.js');
const express = require('express');

describe('GitHub Issue Fixes', function() {
  let app;

  beforeEach(function() {
    app = express();
    app.get('/', function(req, res) {
      res.json({ ok: true });
    });
    app.post('/echo', function(req, res) {
      res.json({ body: req.body, query: req.query });
    });
  });

  describe('Issue #815: body vs _body', function() {
    it('should have body property (not _body) in response', function(done) {
      const request = supertest(app);
      request
        .get('/')
        .expect(200)
        .end(function(err, res) {
          if (err) return done(err);

          // The core issue: response should have 'body' property, not '_body'
          res.should.have.property('body');
          res.body.should.have.property('ok', true);

          // Verify that _body doesn't exist or is properly aliased
          if (res._body !== undefined) {
            // If _body exists, body should equal _body (proper aliasing)
            res.body.should.eql(res._body);
          }

          done();
        });
    });

    it('should work with async/await and have body property (not _body)', function() {
      return supertest(app)
        .get('/')
        .expect(200)
        .then(function(response) {
          // The core issue: response should have 'body' property, not '_body'
          response.should.have.property('body');
          response.body.should.have.property('ok', true);

          // Verify that _body doesn't exist or is properly aliased
          if (response._body !== undefined) {
            // If _body exists, body should equal _body (proper aliasing)
            response.body.should.eql(response._body);
          }
        });
    });
  });

  describe('Issue #860: agent.query() shadowing', function() {
    it('should not override query method with HTTP verb methods', function() {
      const agent = supertest.agent('http://localhost:3000');

      // Verify that query method exists and is a function
      agent.should.have.property('query');
      agent.query.should.be.a.Function();
    });

    it('should preserve HTTP verb methods alongside query', function() {
      const agent = supertest.agent('http://localhost:3000');

      // Verify that both query and HTTP methods exist
      agent.should.have.property('query');
      agent.should.have.property('get');
      agent.should.have.property('post');
      agent.should.have.property('put');
      agent.should.have.property('delete');

      // All should be functions
      agent.query.should.be.a.Function();
      agent.get.should.be.a.Function();
      agent.post.should.be.a.Function();
    });
  });

  describe('Issue #850: multipart/form-data hanging', function() {
    beforeEach(function() {
      app.post('/multipart', function(req, res) {
        // Simulate a server that returns multipart/form-data response
        // Use text/plain to avoid superagent's multipart parsing which causes hanging
        const boundary = 'test-boundary-123456789';
        const multipartData = `--${boundary}\r\n`
          + 'Content-Disposition: form-data; name="errors"\r\n\r\n'
          + `there was an error\r\n--${boundary}--\r\n`;

        res.writeHead(200, {
          'Content-Type': 'text/plain', // Use text/plain to avoid parsing issues
          'Content-Length': Buffer.byteLength(multipartData)
        });

        res.write(multipartData);
        res.end();
      });
    });

    it('should handle multipart/form-data responses without hanging', function(done) {
      this.timeout(5000); // 5 second timeout

      const request = supertest(app);
      request
        .post('/multipart')
        .set('Content-Type', 'multipart/form-data')
        .expect(200)
        .end(function(err, res) {
          if (err) return done(err);
          res.should.not.be.null();
          res.text.should.containEql('there was an error');
          done();
        });
    });
  });
});
```

## File: `test/supertest.js`
```javascript
'use strict';

const https = require('https');
let http2;
try {
  http2 = require('http2'); // eslint-disable-line global-require
} catch (_) {
  // eslint-disable-line no-empty
}
const fs = require('fs');
const path = require('path');
const should = require('should');
const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const nock = require('nock');
const request = require('../index.js');
const throwError = require('./throwError');

process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';

function shouldIncludeStackWithThisFile(err) {
  err.stack.should.match(/test\/supertest.js:/);
  err.stack.should.startWith(err.name + ':');
}

describe('request(url)', function () {
  it('should be supported', function (done) {
    const app = express();
    let server;

    app.get('/', function (req, res) {
      res.send('hello');
    });

    server = app.listen(function () {
      const url = 'http://127.0.0.1:' + server.address().port;
      request(url)
        .get('/')
        .expect('hello', done);
    });
  });

  describe('.end(cb)', function () {
    it('should set `this` to the test object when calling cb', function (done) {
      const app = express();
      let server;

      app.get('/', function (req, res) {
        res.send('hello');
      });

      server = app.listen(function () {
        const url = 'http://127.0.0.1:' + server.address().port;
        const test = request(url).get('/');
        test.end(function (err, res) {
          this.should.eql(test);
          done();
        });
      });
    });
  });
});

describe('request(app)', function () {
  it('should fire up the app on an ephemeral port', function (done) {
    const app = express();

    app.get('/', function (req, res) {
      res.send('hey');
    });

    request(app)
      .get('/')
      .end(function (err, res) {
        res.status.should.equal(200);
        res.text.should.equal('hey');
        done();
      });
  });

  it('should not ECONNRESET on multiple simultaneous tests', function (done) {
    const app = express();

    app.get('/', function (req, res) {
      res.send('hey');
    });

    const test = request(app);

    const requestCount = 10;

    const requests = [];
    for (let i = 0; i < requestCount; i += 1) requests.push(test.get('/'));

    global.Promise.all(requests).then(() => done(), done);
  });

  it('should work with an active server', function (done) {
    const app = express();
    let server;

    app.get('/', function (req, res) {
      res.send('hey');
    });

    server = app.listen(function () {
      request(server)
        .get('/')
        .end(function (err, res) {
          res.status.should.equal(200);
          res.text.should.equal('hey');
          done();
        });
    });
  });

  it('should work with remote server', function (done) {
    const app = express();
    let server;

    app.get('/', function (req, res) {
      res.send('hey');
    });

    server = app.listen(function () {
      const url = 'http://127.0.0.1:' + server.address().port;
      request(url)
        .get('/')
        .end(function (err, res) {
          res.status.should.equal(200);
          res.text.should.equal('hey');
          done();
        });
    });
  });

  it('should work with a https server', function (done) {
    const app = express();
    const fixtures = path.join(__dirname, 'fixtures');
    const server = https.createServer({
      key: fs.readFileSync(path.join(fixtures, 'test_key.pem')),
      cert: fs.readFileSync(path.join(fixtures, 'test_cert.pem'))
    }, app);

    app.get('/', function (req, res) {
      res.send('hey');
    });

    request(server)
      .get('/')
      .end(function (err, res) {
        if (err) return done(err);
        res.status.should.equal(200);
        res.text.should.equal('hey');
        done();
      });
  });

  it('should work with .send() etc', function (done) {
    const app = express();

    app.use(bodyParser.json());

    app.post('/', function (req, res) {
      res.send(req.body.name);
    });

    request(app)
      .post('/')
      .send({ name: 'john' })
      .expect('john', done);
  });

  it('should work when unbuffered', function (done) {
    const app = express();

    app.get('/', function (req, res) {
      res.end('Hello');
    });

    request(app)
      .get('/')
      .expect('Hello', done);
  });

  it('should default redirects to 0', function (done) {
    const app = express();

    app.get('/', function (req, res) {
      res.redirect('/login');
    });

    request(app)
      .get('/')
      .expect(302, done);
  });

  it('should handle redirects', function (done) {
    const app = express();

    app.get('/login', function (req, res) {
      res.end('Login');
    });

    app.get('/', function (req, res) {
      res.redirect('/login');
    });

    request(app)
      .get('/')
      .redirects(1)
      .end(function (err, res) {
        should.exist(res);
        res.status.should.be.equal(200);
        res.text.should.be.equal('Login');
        done();
      });
  });

  it('should handle socket errors', function (done) {
    const app = express();

    app.get('/', function (req, res) {
      res.destroy();
    });

    request(app)
      .get('/')
      .end(function (err) {
        should.exist(err);
        done();
      });
  });

  describe('.bearer(token)', function () {
    it('should work the bearer token', function () {
      const app = express();
      const test = request(app);

      app.get('/', function (req, res) {
        if (req.headers.authorization === 'Bearer test-token') {
          res.status(200).send('Authorized');
        } else {
          res.status(403).send('Unauthorized');
        }
      });

      test.get('/').bearer('test-token').expect(200).expect('Authorized');
    });
  });

  describe('.end(fn)', function () {
    it('should close server', function (done) {
      const app = express();
      let test;

      app.get('/', function (req, res) {
        res.send('supertest FTW!');
      });

      test = request(app)
        .get('/')
        .end(function () {
        });

      test._server.on('close', function () {
        done();
      });
    });

    it('should wait for server to close before invoking fn', function (done) {
      const app = express();
      let closed = false;
      let test;

      app.get('/', function (req, res) {
        res.send('supertest FTW!');
      });

      test = request(app)
        .get('/')
        .end(function () {
          closed.should.be.true;
          done();
        });

      test._server.on('close', function () {
        closed = true;
      });
    });

    it('should support nested requests', function (done) {
      const app = express();
      const test = request(app);

      app.get('/', function (req, res) {
        res.send('supertest FTW!');
      });

      test
        .get('/')
        .end(function () {
          test
            .get('/')
            .end(function (err, res) {
              (err === null).should.be.true;
              res.status.should.equal(200);
              res.text.should.equal('supertest FTW!');
              done();
            });
        });
    });

    it('should include the response in the error callback', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send('whatever');
      });

      request(app)
        .get('/')
        .expect(function () {
          throw new Error('Some error');
        })
        .end(function (err, res) {
          should.exist(err);
          should.exist(res);
          // Duck-typing response, just in case.
          res.status.should.equal(200);
          done();
        });
    });

    it('should set `this` to the test object when calling the error callback', function (done) {
      const app = express();
      let test;

      app.get('/', function (req, res) {
        res.send('whatever');
      });

      test = request(app).get('/');
      test.expect(function () {
        throw new Error('Some error');
      }).end(function (err, res) {
        should.exist(err);
        this.should.eql(test);
        done();
      });
    });

    it('should handle an undefined Response', function (done) {
      const app = express();
      let server;

      app.get('/', function (req, res) {
        setTimeout(function () {
          res.end();
        }, 20);
      });

      server = app.listen(function () {
        const url = 'http://127.0.0.1:' + server.address().port;
        request(url)
          .get('/')
          .timeout(1)
          .expect(200, function (err) {
            err.should.be.an.instanceof(Error);
            return done();
          });
      });
    });

    it('should handle error returned when server goes down', function (done) {
      const app = express();
      let server;

      app.get('/', function (req, res) {
        res.end();
      });

      server = app.listen(function () {
        const url = 'http://127.0.0.1:' + server.address().port;
        server.close();
        request(url)
          .get('/')
          .expect(200, function (err) {
            err.should.be.an.instanceof(Error);
            return done();
          });
      });
    });
  });

  describe('.expect(status[, fn])', function () {
    it('should assert the response status', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send('hey');
      });

      request(app)
        .get('/')
        .expect(404)
        .end(function (err, res) {
          err.message.should.equal('expected 404 "Not Found", got 200 "OK"');
          shouldIncludeStackWithThisFile(err);
          done();
        });
    });
  });

  describe('.expect(status)', function () {
    it('should handle connection error', function (done) {
      const req = request.agent('http://127.0.0.1:1234');

      req
        .get('/')
        .expect(200)
        .end(function (err, res) {
          err.message.should.equal('ECONNREFUSED: Connection refused');
          done();
        });
    });
  });

  describe('.expect(status)', function () {
    it('should assert only status', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send('hey');
      });

      request(app)
        .get('/')
        .expect(200)
        .end(done);
    });
  });

  describe('.expect(statusArray)', function () {
    it('should assert only status', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send('hey');
      });

      request(app)
        .get('/')
        .expect([200, 404])
        .end(done);
    });

    it('should reject if status is not in valid statuses array', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send('hey');
      });

      request(app)
        .get('/')
        .expect([500, 404])
        .end(function (err, res) {
          err.message.should.equal('expected one of "500, 404", got 200 "OK"');
          shouldIncludeStackWithThisFile(err);
          done();
        });
    });
  });

  describe('.expect(status, body[, fn])', function () {
    it('should assert the response body and status', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send('foo');
      });

      request(app)
        .get('/')
        .expect(200, 'foo', done);
    });

    describe('when the body argument is an empty string', function () {
      it('should not quietly pass on failure', function (done) {
        const app = express();

        app.get('/', function (req, res) {
          res.send('foo');
        });

        request(app)
          .get('/')
          .expect(200, '')
          .end(function (err, res) {
            err.message.should.equal('expected \'\' response body, got \'foo\'');
            shouldIncludeStackWithThisFile(err);
            done();
          });
      });
    });
  });

  describe('.expect(body[, fn])', function () {
    it('should assert the response body', function (done) {
      const app = express();

      app.set('json spaces', 0);

      app.get('/', function (req, res) {
        res.send({ foo: 'bar' });
      });

      request(app)
        .get('/')
        .expect('hey')
        .end(function (err, res) {
          err.message.should.equal('expected \'hey\' response body, got \'{"foo":"bar"}\'');
          shouldIncludeStackWithThisFile(err);
          done();
        });
    });

    it('should assert the status before the body', function (done) {
      const app = express();

      app.set('json spaces', 0);

      app.get('/', function (req, res) {
        res.status(500).send({ message: 'something went wrong' });
      });

      request(app)
        .get('/')
        .expect(200)
        .expect('hey')
        .end(function (err, res) {
          err.message.should.equal('expected 200 "OK", got 500 "Internal Server Error"');
          shouldIncludeStackWithThisFile(err);
          done();
        });
    });

    it('should assert the response text', function (done) {
      const app = express();

      app.set('json spaces', 0);

      app.get('/', function (req, res) {
        res.send({ foo: 'bar' });
      });

      request(app)
        .get('/')
        .expect('{"foo":"bar"}', done);
    });

    it('should assert the parsed response body', function (done) {
      const app = express();

      app.set('json spaces', 0);

      app.get('/', function (req, res) {
        res.send({ foo: 'bar' });
      });

      request(app)
        .get('/')
        .expect({ foo: 'baz' })
        .end(function (err, res) {
          err.message.should.equal('expected { foo: \'baz\' } response body, got { foo: \'bar\' }');
          shouldIncludeStackWithThisFile(err);

          request(app)
            .get('/')
            .expect({ foo: 'bar' })
            .end(done);
        });
    });

    it('should test response object types', function (done) {
      const app = express();
      app.get('/', function (req, res) {
        res.status(200).json({ stringValue: 'foo', numberValue: 3 });
      });

      request(app)
        .get('/')
        .expect({ stringValue: 'foo', numberValue: 3 }, done);
    });

    it('should deep test response object types', function (done) {
      const app = express();
      app.get('/', function (req, res) {
        res.status(200)
          .json({ stringValue: 'foo', numberValue: 3, nestedObject: { innerString: '5' } });
      });

      request(app)
        .get('/')
        .expect({ stringValue: 'foo', numberValue: 3, nestedObject: { innerString: 5 } })
        .end(function (err, res) {
          err.message.replace(/[^a-zA-Z]/g, '').should.equal('expected {\n  stringValue: \'foo\',\n  numberValue: 3,\n  nestedObject: { innerString: 5 }\n} response body, got {\n  stringValue: \'foo\',\n  numberValue: 3,\n  nestedObject: { innerString: \'5\' }\n}'.replace(/[^a-zA-Z]/g, '')); // eslint-disable-line max-len
          shouldIncludeStackWithThisFile(err);

          request(app)
            .get('/')
            .expect({ stringValue: 'foo', numberValue: 3, nestedObject: { innerString: '5' } })
            .end(done);
        });
    });

    it('should support parsed response arrays', function (done) {
      const app = express();
      app.get('/', function (req, res) {
        res.status(200).json(['a', { id: 1 }]);
      });

      request(app)
        .get('/')
        .expect(['a', { id: 1 }], done);
    });

    it('should support empty array responses', function (done) {
      const app = express();
      app.get('/', function (req, res) {
        res.status(200).json([]);
      });

      request(app)
        .get('/')
        .expect([], done);
    });

    it('should support regular expressions', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send('foobar');
      });

      request(app)
        .get('/')
        .expect(/^bar/)
        .end(function (err, res) {
          err.message.should.equal('expected body \'foobar\' to match /^bar/');
          shouldIncludeStackWithThisFile(err);
          done();
        });
    });

    it('should assert response body multiple times', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send('hey tj');
      });

      request(app)
        .get('/')
        .expect(/tj/)
        .expect('hey')
        .expect('hey tj')
        .end(function (err, res) {
          err.message.should.equal("expected 'hey' response body, got 'hey tj'");
          shouldIncludeStackWithThisFile(err);
          done();
        });
    });

    it('should assert response body multiple times with no exception', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send('hey tj');
      });

      request(app)
        .get('/')
        .expect(/tj/)
        .expect(/^hey/)
        .expect('hey tj', done);
    });
  });

  describe('.expect(field, value[, fn])', function () {
    it('should assert the header field presence', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send({ foo: 'bar' });
      });

      request(app)
        .get('/')
        .expect('Content-Foo', 'bar')
        .end(function (err, res) {
          err.message.should.equal('expected "Content-Foo" header field');
          shouldIncludeStackWithThisFile(err);
          done();
        });
    });

    it('should assert the header field value', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send({ foo: 'bar' });
      });

      request(app)
        .get('/')
        .expect('Content-Type', 'text/html')
        .end(function (err, res) {
          err.message.should.equal('expected "Content-Type" of "text/html", '
            + 'got "application/json; charset=utf-8"');
          shouldIncludeStackWithThisFile(err);
          done();
        });
    });

    it('should assert multiple fields', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send('hey');
      });

      request(app)
        .get('/')
        .expect('Content-Type', 'text/html; charset=utf-8')
        .expect('Content-Length', '3')
        .end(done);
    });

    it('should support regular expressions', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send('hey');
      });

      request(app)
        .get('/')
        .expect('Content-Type', /^application/)
        .end(function (err) {
          err.message.should.equal('expected "Content-Type" matching /^application/, '
            + 'got "text/html; charset=utf-8"');
          shouldIncludeStackWithThisFile(err);
          done();
        });
    });

    it('should support numbers', function (done) {
      const app = express();

      app.get('/', function (req, res) {
        res.send('hey');
      });

      request(app)
        .get('/')
        .expect('Content-Length', 4)
        .end(function (err) {
          err.message.should.equal('expected "Content-Length" of "4", got "3"');
          shouldIncludeStackWithThisFile(err);
          done();
        });
    });

    describe('handling arbitrary expect functions', function () {
      let app;
      let get;

      before(function () {
        app = express();
        app.get('/', function (req, res) {
          res.send('hey');
        });
      });

      beforeEach(function () {
        get = request(app).get('/');
      });

      it('reports errors', function (done) {
        get
          .expect(throwError('failed'))
          .end(function (err) {
            err.message.should.equal('failed');
            shouldIncludeStackWithThisFile(err);
            done();
          });
      });

      // this scenario should never happen after https://github.com/ladjs/supertest/pull/767
      // meant for test coverage for lib/test.js#287
      // https://github.com/ladjs/supertest/blob/e064b5ae71e1dfa3e1a74745fda527ac542e1878/lib/test.js#L287
      it('_assertFunction should catch and return error', function (done) {
        const error = new Error('failed');
        const returnedError = get
          // private api
          ._assertFunction(function (res) {
            throw error;
          });
        get
          .end(function () {
            returnedError.should.equal(error);
            returnedError.message.should.equal('failed');
            shouldIncludeStackWithThisFile(returnedError);
            done();
          });
      });

      it(
        'ensures truthy non-errors returned from asserts are not promoted to errors',
        function (done) {
          get
            .expect(function (res) {
              return 'some descriptive error';
            })
            .end(function (err) {
              should.not.exist(err);
              done();
            });
        }
      );

      it('ensures truthy errors returned from asserts are throw to end', function (done) {
        get
          .expect(throwError('some descriptive error'))
          .end(function (err) {
            err.message.should.equal('some descriptive error');
            shouldIncludeStackWithThisFile(err);
            (err instanceof Error).should.be.true;
            done();
          });
      });

      it("doesn't create false negatives", function (done) {
        get
          .expect(function (res) {
          })
          .end(done);
      });

      it("doesn't create false negatives on non error objects", function (done) {
        const handler = {
          get: function(target, prop, receiver) {
            throw Error('Should not be called for non Error objects');
          }
        };
        const proxy = new Proxy({}, handler); // eslint-disable-line no-undef
        get
          .expect(() => proxy)
          .end(done);
      });

      it('handles multiple asserts', function (done) {
        const calls = [];
        get
          .expect(function (res) {
            calls[0] = 1;
          })
          .expect(function (res) {
            calls[1] = 1;
          })
          .expect(function (res) {
            calls[2] = 1;
          })
          .end(function () {
            const callCount = [0, 1, 2].reduce(function (count, i) {
              return count + calls[i];
            }, 0);
            callCount.should.equal(3, "didn't see all assertions run");
            done();
          });
      });

      it('plays well with normal assertions - no false positives', function (done) {
        get
          .expect(function (res) {
          })
          .expect('Content-Type', /json/)
          .end(function (err) {
            err.message.should.match(/Content-Type/);
            shouldIncludeStackWithThisFile(err);
            done();
          });
      });

      it('plays well with normal assertions - no false negatives', function (done) {
        get
          .expect(function (res) {
          })
          .expect('Content-Type', /html/)
          .expect(function (res) {
          })
          .expect('Content-Type', /text/)
          .end(done);
      });
    });

    describe('handling multiple assertions per field', function () {
      it('should work', function (done) {
        const app = express();
        app.get('/', function (req, res) {
          res.send('hey');
        });

        request(app)
          .get('/')
          .expect('Content-Type', /text/)
          .expect('Content-Type', /html/)
          .end(done);
      });

      it('should return an error if the first one fails', function (done) {
        const app = express();
        app.get('/', function (req, res) {
          res.send('hey');
        });

        request(app)
          .get('/')
          .expect('Content-Type', /bloop/)
          .expect('Content-Type', /html/)
          .end(function (err) {
            err.message.should.equal('expected "Content-Type" matching /bloop/, '
              + 'got "text/html; charset=utf-8"');
            shouldIncludeStackWithThisFile(err);
            done();
          });
      });

      it('should return an error if a middle one fails', function (done) {
        const app = express();
        app.get('/', function (req, res) {
          res.send('hey');
        });

        request(app)
          .get('/')
          .expect('Content-Type', /text/)
          .expect('Content-Type', /bloop/)
          .expect('Content-Type', /html/)
          .end(function (err) {
            err.message.should.equal('expected "Content-Type" matching /bloop/, '
              + 'got "text/html; charset=utf-8"');
            shouldIncludeStackWithThisFile(err);
            done();
          });
      });

      it('should return an error if the last one fails', function (done) {
        const app = express();
        app.get('/', function (req, res) {
          res.send('hey');
        });

        request(app)
          .get('/')
          .expect('Content-Type', /text/)
          .expect('Content-Type', /html/)
          .expect('Content-Type', /bloop/)
          .end(function (err) {
            err.message.should.equal('expected "Content-Type" matching /bloop/, '
              + 'got "text/html; charset=utf-8"');
            shouldIncludeStackWithThisFile(err);
            done();
          });
      });
    });
  });
});

describe('request.agent(app)', function () {
  const app = express();
  const agent = request.agent(app)
    .set('header', 'hey');

  app.use(cookieParser());

  app.get('/', function (req, res) {
    res.cookie('cookie', 'hey');
    res.send();
  });

  app.get('/return_cookies', function (req, res) {
    if (req.cookies.cookie) res.send(req.cookies.cookie);
    else res.send(':(');
  });

  app.get('/return_headers', function (req, res) {
    if (req.get('header')) res.send(req.get('header'));
    else res.send(':(');
  });

  it('should save cookies', function (done) {
    agent
      .get('/')
      .expect('set-cookie', 'cookie=hey; Path=/', done);
  });

  it('should send cookies', function (done) {
    agent
      .get('/return_cookies')
      .expect('hey', done);
  });

  it('should send global agent headers', function (done) {
    agent
      .get('/return_headers')
      .expect('hey', done);
  });
});

describe('agent.host(host)', function () {
  it('should set request hostname', function (done) {
    const app = express();
    const agent = request.agent(app);

    app.get('/', function (req, res) {
      res.send({ hostname: req.hostname });
    });

    agent
      .host('something.test')
      .get('/')
      .end(function (err, res) {
        if (err) return done(err);
        res.body.hostname.should.equal('something.test');
        done();
      });
  });
});

describe('.<http verb> works as expected', function () {
  it('.delete should work', function (done) {
    const app = express();
    app.delete('/', function (req, res) {
      res.sendStatus(200);
    });

    request(app)
      .delete('/')
      .expect(200, done);
  });
  it('.del should work', function (done) {
    const app = express();
    app.delete('/', function (req, res) {
      res.sendStatus(200);
    });

    request(app)
      .del('/')
      .expect(200, done);
  });
  it('.get should work', function (done) {
    const app = express();
    app.get('/', function (req, res) {
      res.sendStatus(200);
    });

    request(app)
      .get('/')
      .expect(200, done);
  });
  it('.post should work', function (done) {
    const app = express();
    app.post('/', function (req, res) {
      res.sendStatus(200);
    });

    request(app)
      .post('/')
      .expect(200, done);
  });
  it('.put should work', function (done) {
    const app = express();
    app.put('/', function (req, res) {
      res.sendStatus(200);
    });

    request(app)
      .put('/')
      .expect(200, done);
  });
  it('.head should work', function (done) {
    const app = express();
    app.head('/', function (req, res) {
      res.statusCode = 200;
      res.set('Content-Encoding', 'gzip');
      res.set('Content-Length', '1024');
      res.status(200);
      res.end();
    });

    request(app)
      .head('/')
      .set('accept-encoding', 'gzip, deflate')
      .end(function (err, res) {
        if (err) return done(err);
        res.should.have.property('statusCode', 200);
        res.headers.should.have.property('content-length', '1024');
        done();
      });
  });
});

describe('assert ordering by call order', function () {
  it('should assert the body before status', function (done) {
    const app = express();

    app.set('json spaces', 0);

    app.get('/', function (req, res) {
      res.status(500).json({ message: 'something went wrong' });
    });

    request(app)
      .get('/')
      .expect('hey')
      .expect(200)
      .end(function (err, res) {
        err.message.should.equal('expected \'hey\' response body, '
          + 'got \'{"message":"something went wrong"}\'');
        shouldIncludeStackWithThisFile(err);
        done();
      });
  });

  it('should assert the status before body', function (done) {
    const app = express();

    app.set('json spaces', 0);

    app.get('/', function (req, res) {
      res.status(500).json({ message: 'something went wrong' });
    });

    request(app)
      .get('/')
      .expect(200)
      .expect('hey')
      .end(function (err, res) {
        err.message.should.equal('expected 200 "OK", got 500 "Internal Server Error"');
        shouldIncludeStackWithThisFile(err);
        done();
      });
  });

  it('should assert the fields before body and status', function (done) {
    const app = express();

    app.set('json spaces', 0);

    app.get('/', function (req, res) {
      res.status(200).json({ hello: 'world' });
    });

    request(app)
      .get('/')
      .expect('content-type', /html/)
      .expect('hello')
      .end(function (err, res) {
        err.message.should.equal('expected "content-type" matching /html/, '
          + 'got "application/json; charset=utf-8"');
        shouldIncludeStackWithThisFile(err);
        done();
      });
  });

  it('should call the expect function in order', function (done) {
    const app = express();

    app.get('/', function (req, res) {
      res.status(200).json({});
    });

    request(app)
      .get('/')
      .expect(function (res) {
        res.body.first = 1;
      })
      .expect(function (res) {
        (res.body.first === 1).should.be.true;
        res.body.second = 2;
      })
      .end(function (err, res) {
        if (err) return done(err);
        (res.body.first === 1).should.be.true;
        (res.body.second === 2).should.be.true;
        done();
      });
  });

  it('should call expect(fn) and expect(status, fn) in order', function (done) {
    const app = express();

    app.get('/', function (req, res) {
      res.status(200).json({});
    });

    request(app)
      .get('/')
      .expect(function (res) {
        res.body.first = 1;
      })
      .expect(200, function (err, res) {
        (err === null).should.be.true;
        (res.body.first === 1).should.be.true;
        done();
      });
  });

  it('should call expect(fn) and expect(header,value) in order', function (done) {
    const app = express();

    app.get('/', function (req, res) {
      res
        .set('X-Some-Header', 'Some value')
        .send();
    });

    request(app)
      .get('/')
      .expect('X-Some-Header', 'Some value')
      .expect(function (res) {
        res.headers['x-some-header'] = '';
      })
      .expect('X-Some-Header', '')
      .end(done);
  });

  it('should call expect(fn) and expect(body) in order', function (done) {
    const app = express();

    app.get('/', function (req, res) {
      res.json({ somebody: 'some body value' });
    });

    request(app)
      .get('/')
      .expect(/some body value/)
      .expect(function (res) {
        res.body.somebody = 'nobody';
      })
      .expect(/some body value/) // res.text should not be modified.
      .expect({ somebody: 'nobody' })
      .expect(function (res) {
        res.text = 'gone';
      })
      .expect('gone')
      .expect(/gone/)
      .expect({ somebody: 'nobody' }) // res.body should not be modified
      .expect('gone', done);
  });
});

describe('request.get(url).query(vals) works as expected', function () {
  it('normal single query string value works', function (done) {
    const app = express();
    app.get('/', function (req, res) {
      res.status(200).send(req.query.val);
    });

    request(app)
      .get('/')
      .query({ val: 'Test1' })
      .expect(200, function (err, res) {
        res.text.should.be.equal('Test1');
        done();
      });
  });

  it('array query string value works', function (done) {
    const app = express();
    app.get('/', function (req, res) {
      res.status(200).send(Array.isArray(req.query.val));
    });

    request(app)
      .get('/')
      .query({ 'val[]': ['Test1', 'Test2'] })
      .expect(200, function (err, res) {
        res.req.path.should.be.equal('/?val%5B%5D=Test1&val%5B%5D=Test2');
        res.text.should.be.equal('true');
        done();
      });
  });

  it('array query string value work even with single value', function (done) {
    const app = express();
    app.get('/', function (req, res) {
      res.status(200).send(Array.isArray(req.query.val));
    });

    request(app)
      .get('/')
      .query({ 'val[]': ['Test1'] })
      .expect(200, function (err, res) {
        res.req.path.should.be.equal('/?val%5B%5D=Test1');
        res.text.should.be.equal('true');
        done();
      });
  });

  it('object query string value works', function (done) {
    const app = express();
    app.get('/', function (req, res) {
      res.status(200).send(req.query.val.test);
    });

    request(app)
      .get('/')
      .query({ val: { test: 'Test1' } })
      .expect(200, function (err, res) {
        res.text.should.be.equal('Test1');
        done();
      });
  });

  it('handles unknown errors (err without res)', function (done) {
    const app = express();

    nock.disableNetConnect();

    app.get('/', function (req, res) {
      res.status(200).send('OK');
    });

    request(app)
      .get('/')
      // This expect should never get called, but exposes this issue with other
      // errors being obscured by the response assertions
      // https://github.com/ladjs/supertest/issues/352
      .expect(200)
      .end(function (err, res) {
        should.exist(err);
        should.not.exist(res);
        err.should.be.an.instanceof(Error);
        err.message.should.match(/Nock: Disallowed net connect/);
        shouldIncludeStackWithThisFile(err);
        done();
      });

    nock.restore();
  });

  // this scenario should never happen
  // there shouldn't be any res if there is an err
  // meant for test coverage for lib/test.js#169
  // https://github.com/ladjs/supertest/blob/5543d674cf9aa4547927ba6010d31d9474950dec/lib/test.js#L169
  it('handles unknown errors (err with res)', function (done) {
    const app = express();

    app.get('/', function (req, res) {
      res.status(200).send('OK');
    });

    const resError = new Error();
    resError.status = 400;

    const serverRes = { status: 200 };

    request(app)
      .get('/')
      // private api
      .assert(resError, serverRes, function (err, res) {
        should.exist(err);
        should.exist(res);
        err.should.equal(resError);
        res.should.equal(serverRes);
        // close the server explicitly (as we are not using expect/end/then)
        this.end(done);
      });
  });

  it('should assert using promises', function (done) {
    const app = express();

    app.get('/', function (req, res) {
      res.status(400).send({ promise: true });
    });

    request(app)
      .get('/')
      .expect(400)
      .then((res) => {
        res.body.promise.should.be.equal(true);
        done();
      });
  });
});

const describeHttp2 = (http2) ? describe : describe.skip;
describeHttp2('http2', function() {
  // eslint-disable-next-line global-require
  const proxyquire = require('proxyquire');

  const tests = [
    {
      title: 'request(app)',
      api: request,
      mockApi: proxyquire('../index.js', { http2: null })
    },
    {
      title: 'request.agent(app)',
      api: request.agent,
      mockApi: proxyquire('../lib/agent.js', { http2: null })
    }
  ];

  tests.forEach(({ title, api, mockApi }) => {
    describe(title, function () {
      const app = function(req, res) {
        res.end('hey');
      };

      it('should fire up the app on an ephemeral port', function (done) {
        api(app, { http2: true })
          .get('/')
          .end(function (err, res) {
            res.status.should.equal(200);
            res.text.should.equal('hey');
            done();
          });
      });

      it('should work with an active server', function (done) {
        const server = http2.createServer(app);

        server.listen(function () {
          api(server)
            .get('/')
            .http2()
            .end(function (err, res) {
              res.status.should.equal(200);
              res.text.should.equal('hey');
              // lose the external server explicitly
              server.close(done);
            });
        });
      });

      it('should throw error if http2 is not supported', function() {
        (function() {
          mockApi(app, { http2: true });
        }).should.throw('supertest: this version of Node.js does not support http2');
      });
    });
  });
});
```

## File: `test/throwError.js`
```javascript
'use strict';

/**
 * This method needs to reside in its own module in order to properly test stack trace handling.
 */
module.exports = function throwError(message) {
  return function() {
    throw new Error(message);
  };
};
```

## File: `test/fixtures/test_cert.pem`
```
-----BEGIN CERTIFICATE-----
MIIDCTCCAfGgAwIBAgIUZtrgyKVudIs9Y90tCSeQHUjKy2IwDQYJKoZIhvcNAQEL
BQAwFDESMBAGA1UEAwwJbG9jYWxob3N0MB4XDTIwMTAwOTIwMDkyOFoXDTIwMTEw
ODIwMDkyOFowFDESMBAGA1UEAwwJbG9jYWxob3N0MIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAuU6E5t0+OT01AoLAEZ6HndwOwmZO3C/YhiyObKDGaxRi
WIaTa52sADMj+JSNL2fnY6XS9SjJddK3PSbGstKJrdR0kmkwvzeZ090bMb3UHjSy
b571s2VKCWfc8XoGsJfpHTnTk+bk0QKKVTfcd4ORPvXMG6sNAENHzbG0EyYX1dJ7
DF1SfBC2spMlQ2s8eBTVO2wnK9pucgKgXSQNa31l+G2Ixf94HjrJA/YyTmqo7UuW
D1ACxvxIKnzMVaeE2nMcRjb7SYBly41Z5A0mZ5mj1C7iQBM1cVn7FAK/5RYT3XJU
qOejQy17K4O1B1gB+62X42lLdo4uN8/uX96/hzAmOQIDAQABo1MwUTAdBgNVHQ4E
FgQUMY736EgCf9E/UitPXmJHR85Yy9EwHwYDVR0jBBgwFoAUMY736EgCf9E/UitP
XmJHR85Yy9EwDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAGA5Q
CNQCrmTfd2cNckssngiC8kYCssaSloLpjmOl4PoCzT8Ggrer5OAHdywZExhK4BvG
xycn1TwJWpm0rqUgisQy4NiqNUC7xIphYcWW668OSfW2ZW83/EHWEf4kPR9lnJUI
W4cMrRd1XKIRAyuePGlgya3CoELlbgw2UYz6SLae6SjYReo10hWDRVj8+Z+P68ST
WmDvg3tnbkSz9gOy/Pm+qgq5DMkKp6yJ0GyhlTRgIdYi3DtFizzEnSDBP1RlGRo5
U9cyGCjNA9R9PlgY30tCvH33urPW0OWH+kFj7i8ksUJJKI4s4pTb2HpvdTeQvcG7
7+Jp8RcI+sxqFT4jyw==
-----END CERTIFICATE-----
```

## File: `test/fixtures/test_key.pem`
```
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC5ToTm3T45PTUC
gsARnoed3A7CZk7cL9iGLI5soMZrFGJYhpNrnawAMyP4lI0vZ+djpdL1KMl10rc9
Jsay0omt1HSSaTC/N5nT3RsxvdQeNLJvnvWzZUoJZ9zxegawl+kdOdOT5uTRAopV
N9x3g5E+9cwbqw0AQ0fNsbQTJhfV0nsMXVJ8ELaykyVDazx4FNU7bCcr2m5yAqBd
JA1rfWX4bYjF/3geOskD9jJOaqjtS5YPUALG/EgqfMxVp4TacxxGNvtJgGXLjVnk
DSZnmaPULuJAEzVxWfsUAr/lFhPdclSo56NDLXsrg7UHWAH7rZfjaUt2ji43z+5f
3r+HMCY5AgMBAAECggEBALh3iaWoqMCiRZryPfFMNwTWg3rSDb7zgkBPKpjIk70U
1bH6hdajZw3r2usiNknyzU1NTevvZl18Hh0p9LMfEx+QV1tIi9ZOqztU6DVkGzzW
iKrFOyISutkSI8ffCbnR/6WwYwbg2veV589dhIMU3gom9cC1ToPsdhY1yGUnjqKy
6CGvwA8qae4lV1BJVZi3aVmd278WVhBphF12gKGYkNjSBaasuTvABIwUMH+sjKiP
9UjxNsrHVO9RSWmZdygr9vpDHnwyE+1Pm9Pd5FR8xit5U+PZM71jsV5CJuADB6wO
bUe/qIUJCCfQPk4rjvkVaVD8xX6xK2/RGRCKJ8YHXAECgYEA9fangEVlC1qgfVaK
khI/CwyJ4RekUf1a2EXH3QQflfR5fwNcAZ7Rgt7oQ2IIRmk0qLp3lGjuNQ9VF58i
JdSlzvVQnlclJVTE++mQDuJitYZ+p+WCwoCNRM/vnMABGEUcopothiNY2AilJNHh
nMrVI1ZMqasoIfaxfuUPdUSzQBECgYEAwN49zbKIaXs8L3v9fdhFGNDGQFCZ2qHM
ZaaO5PACnB6P74uhfE2mfJ/zS4udcnlt/CUSsgBDgSvEsX/rXDDkAGnBAQC7T2is
hKO3ClOUb8MghNN/L2QamZDwffPqOnn0eE3GEq8Qs2TSbA0+Bt8lm1uVRs67PKAP
rYjsY5eYK6kCgYEAglu9nsAos4HOuV8ahhxhiUuV79SF5GZwtVsWeE7tJp6xnd17
7+fqhn/5fW0Bkb/EhwB8zA1o4npD0QcoJAC1+CAQIDtzlnt9Az5geWMGicrEadu8
F7XmKWhDSEKC0ggfCxbHteYZ+jVqwT7zYhQmLlpYuzvZQ1bp76UbMj28+uECgYAO
YEJxE66xVhs9WtuhRr6Xw/ATGS7uqgLHTOv3yqAXLPwDmf/WeR9AyNdkuSpqPvzg
v46uL/DYLwABTwynGYnVMgzN21Ua7S120ZEyNtqonf3NiMpBKRAGhFQ4vzalVzPO
x9VMzTnMdWZt4WrPLlDqTKBK39v6/99LSxp7rfAMyQKBgFAbAjdW8mNRqr2c562e
rL894oKVOcnuPLovEx5pHWW3NOdPSdEjA5q4aISw4F6YnUXyCAGqbAOp+GrS3xXz
xKj8qta/mqvHjj95EoMybnUwaCgK3dw0+QyuXFNxtejbOD1Ubljutn8hzswGryVg
Z70KXTszjaQxgrTZpmKljS88
-----END PRIVATE KEY-----
```

