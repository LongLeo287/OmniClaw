---
id: supertest
type: knowledge
owner: OA_Triage
---
# supertest
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: index.js
```js
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

### File: package.json
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

### File: README.md
```md
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

### File: .commitlintrc.js
```js
module.exports = {
  extends: ['@commitlint/config-conventional']
};

```

### File: package-lock.json
```json
{
  "name": "supertest",
  "version": "7.2.2",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "supertest",
      "version": "7.2.2",
      "license": "MIT",
      "dependencies": {
        "cookie-signature": "^1.2.2",
        "methods": "^1.1.2",
        "superagent": "^10.3.0"
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
      }
    },
    "node_modules/@ampproject/remapping": {
      "version": "2.3.0",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@jridgewell/gen-mapping": "^0.3.5",
        "@jridgewell/trace-mapping": "^0.3.24"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.27.1",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.28.0",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.28.0",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@ampproject/remapping": "^2.2.0",
        "@babel/code-frame": "^7.27.1",
        "@babel/generator": "^7.28.0",
        "@babel/helper-compilation-targets": "^7.27.2",
        "@babel/helper-module-transforms": "^7.27.3",
        "@babel/helpers": "^7.27.6",
        "@babel/parser": "^7.28.0",
        "@babel/template": "^7.27.2",
        "@babel/traverse": "^7.28.0",
        "@babel/types": "^7.28.0",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/core/node_modules/convert-source-map": {
      "version": "2.0.0",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@babel/core/node_modules/debug": {
      "version": "4.4.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/@babel/core/node_modules/ms": {
      "version": "2.1.3",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@babel/core/node_modules/semver": {
      "version": "6.3.1",
      "dev": true,
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.28.0",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.28.0",
        "@babel/types": "^7.28.0",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.27.2",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.27.2",
        "@babel/helper-validator-option": "^7.27.1",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets/node_modules/lru-cache": {
      "version": "5.1.1",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "yallist": "^3.0.2"
      }
    },
    "node_modules/@babel/helper-compilation-targets/node_modules/semver": {
      "version": "6.3.1",
      "dev": true,
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      }
    },
    "node_modules/@babel/helper-compilation-targets/node_modules/yallist": {
      "version": "3.1.1",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.28.0",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.27.1",
        "@babel/types": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.27.3",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.27.1",
        "@babel/traverse": "^7.27.3"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helpers": {
      "version": "7.27.6",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/template": "^7.27.2",
        "@babel/types": "^7.27.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.28.0",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.28.0"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/template": {
      "version": "7.27.2",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.27.1",
        "@babel/parser": "^7.27.2",
        "@babel/types": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/traverse": {
      "version": "7.28.0",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.27.1",
        "@babel/generator": "^7.28.0",
        "@babel/helper-globals": "^7.28.0",
        "@babel/parser": "^7.28.0",
        "@babel/template": "^7.27.2",
        "@babel/types": "^7.28.0",
        "debug": "^4.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/traverse/node_modules/debug": {
      "version": "4.4.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/@babel/traverse/node_modules/ms": {
      "version": "2.1.3",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@babel/types": {
      "version": "7.28.0",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@commitlint/cli": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@commitlint/format": "^17.8.1",
        "@commitlint/lint": "^17.8.1",
        "@commitlint/load": "^17.8.1",
        "@commitlint/read": "^17.8.1",
        "@commitlint/types": "^17.8.1",
        "execa": "^5.0.0",
        "lodash.isfunction": "^3.0.9",
        "resolve-from": "5.0.0",
        "resolve-global": "1.0.0",
        "yargs": "^17.0.0"
      },
      "bin": {
        "commitlint": "cli.js"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/config-conventional": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "conventional-changelog-conventionalcommits": "^6.1.0"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/config-validator": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@commitlint/types": "^17.8.1",
        "ajv": "^8.11.0"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/ensure": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@commitlint/types": "^17.8.1",
        "lodash.camelcase": "^4.3.0",
        "lodash.kebabcase": "^4.1.1",
        "lodash.snakecase": "^4.1.1",
        "lodash.startcase": "^4.4.0",
        "lodash.upperfirst": "^4.3.1"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/execute-rule": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/format": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@commitlint/types": "^17.8.1",
        "chalk": "^4.1.0"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/is-ignored": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@commitlint/types": "^17.8.1",
        "semver": "7.5.4"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/lint": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@commitlint/is-ignored": "^17.8.1",
        "@commitlint/parse": "^17.8.1",
        "@commitlint/rules": "^17.8.1",
        "@commitlint/types": "^17.8.1"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/load": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@commitlint/config-validator": "^17.8.1",
        "@commitlint/execute-rule": "^17.8.1",
        "@commitlint/resolve-extends": "^17.8.1",
        "@commitlint/types": "^17.8.1",
        "@types/node": "20.5.1",
        "chalk": "^4.1.0",
        "cosmiconfig": "^8.0.0",
        "cosmiconfig-typescript-loader": "^4.0.0",
        "lodash.isplainobject": "^4.0.6",
        "lodash.merge": "^4.6.2",
        "lodash.uniq": "^4.5.0",
        "resolve-from": "^5.0.0",
        "ts-node": "^10.8.1",
        "typescript": "^4.6.4 || ^5.2.2"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/message": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/parse": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@commitlint/types": "^17.8.1",
        "conventional-changelog-angular": "^6.0.0",
        "conventional-commits-parser": "^4.0.0"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/read": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@commitlint/top-level": "^17.8.1",
        "@commitlint/types": "^17.8.1",
        "fs-extra": "^11.0.0",
        "git-raw-commits": "^2.0.11",
        "minimist": "^1.2.6"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/resolve-extends": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@commitlint/config-validator": "^17.8.1",
        "@commitlint/types": "^17.8.1",
        "import-fresh": "^3.0.0",
        "lodash.mergewith": "^4.6.2",
        "resolve-from": "^5.0.0",
        "resolve-global": "^1.0.0"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/rules": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@commitlint/ensure": "^17.8.1",
        "@commitlint/message": "^17.8.1",
        "@commitlint/to-lines": "^17.8.1",
        "@commitlint/types": "^17.8.1",
        "execa": "^5.0.0"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/to-lines": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/top-level": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "find-up": "^5.0.0"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@commitlint/types": {
      "version": "17.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "chalk": "^4.1.0"
      },
      "engines": {
        "node": ">=v14"
      }
    },
    "node_modules/@cspotcode/source-map-support": {
      "version": "0.8.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/trace-mapping": "0.3.9"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@cspotcode/source-map-support/node_modules/@jridgewell/trace-mapping": {
      "version": "0.3.9",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/resolve-uri": "^3.0.3",
        "@jridgewell/sourcemap-codec": "^1.4.10"
      }
    },
    "node_modules/@eslint-community/eslint-utils": {
      "version": "4.7.0",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "eslint-visitor-keys": "^3.4.3"
      },
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      },
      "peer
... [TRUNCATED]
```

### File: ci\remove-deps-4-old-node.js
```js
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

### File: lib\agent.js
```js
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

### File: lib\test.js
```js
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

### File: test\cookies.js
```js
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

    
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
