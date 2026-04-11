# Knowledge Dump for api

## File: agent.md
```
# Agent

Extends: `undici.Dispatcher`

Agent allows dispatching requests against multiple different origins.

Requests are not guaranteed to be dispatched in order of invocation.

## `new undici.Agent([options])`

Arguments:

* **options** `AgentOptions` (optional)

Returns: `Agent`

### Parameter: `AgentOptions`

Extends: [`PoolOptions`](/docs/docs/api/Pool.md#parameter-pooloptions)

* **factory** `(origin: URL, opts: Object) => Dispatcher` - Default: `(origin, opts) => new Pool(origin, opts)`
* **maxOrigins** `number` (optional) - Default: `Infinity` - Limits the total number of origins that can receive requests at a time, throwing an `MaxOriginsReachedError` error when attempting to dispatch when the max is reached. If `Infinity`, no limit is enforced.

## Instance Properties

### `Agent.closed`

Implements [Client.closed](/docs/docs/api/Client.md#clientclosed)

### `Agent.destroyed`

Implements [Client.destroyed](/docs/docs/api/Client.md#clientdestroyed)

## Instance Methods

### `Agent.close([callback])`

Implements [`Dispatcher.close([callback])`](/docs/docs/api/Dispatcher.md#dispatcherclosecallback-promise).

### `Agent.destroy([error, callback])`

Implements [`Dispatcher.destroy([error, callback])`](/docs/docs/api/Dispatcher.md#dispatcherdestroyerror-callback-promise).

### `Agent.dispatch(options, handler: AgentDispatchOptions)`

Implements [`Dispatcher.dispatch(options, handler)`](/docs/docs/api/Dispatcher.md#dispatcherdispatchoptions-handler).

#### Parameter: `AgentDispatchOptions`

Extends: [`DispatchOptions`](/docs/docs/api/Dispatcher.md#parameter-dispatchoptions)

* **origin** `string | URL`

Implements [`Dispatcher.destroy([error, callback])`](/docs/docs/api/Dispatcher.md#dispatcherdestroyerror-callback-promise).

### `Agent.connect(options[, callback])`

See [`Dispatcher.connect(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherconnectoptions-callback).

### `Agent.dispatch(options, handler)`

Implements [`Dispatcher.dispatch(options, handler)`](/docs/docs/api/Dispatcher.md#dispatcherdispatchoptions-handler).

### `Agent.pipeline(options, handler)`

See [`Dispatcher.pipeline(options, handler)`](/docs/docs/api/Dispatcher.md#dispatcherpipelineoptions-handler).

### `Agent.request(options[, callback])`

See [`Dispatcher.request(options [, callback])`](/docs/docs/api/Dispatcher.md#dispatcherrequestoptions-callback).

### `Agent.stream(options, factory[, callback])`

See [`Dispatcher.stream(options, factory[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherstreamoptions-factory-callback).

### `Agent.upgrade(options[, callback])`

See [`Dispatcher.upgrade(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherupgradeoptions-callback).

### `Agent.stats()`

Returns an object of stats by origin in the format of `Record<string, TClientStats | TPoolStats>`

See [`PoolStats`](/docs/docs/api/PoolStats.md) and [`ClientStats`](/docs/docs/api/ClientStats.md).

```

## File: ag_ui.md
```
# `pydantic_ai.ag_ui`

::: pydantic_ai.ag_ui

```

## File: api_lifecycle.md
```
# Client Lifecycle

An Undici [Client](/docs/docs/api/Client.md) can be best described as a state machine. The following list is a summary of the various state transitions the `Client` will go through in its lifecycle. This document also contains detailed breakdowns of each state.

> This diagram is not a perfect representation of the undici Client. Since the Client class is not actually implemented as a state-machine, actual execution may deviate slightly from what is described below. Consider this as a general resource for understanding the inner workings of the Undici client rather than some kind of formal specification.

## State Transition Overview

* A `Client` begins in the **idle** state with no socket connection and no requests in queue.
  * The *connect* event transitions the `Client` to the **pending** state where requests can be queued prior to processing.
  * The *close* and *destroy* events transition the `Client` to the **destroyed** state. Since there are no requests in the queue, the *close* event immediately transitions to the **destroyed** state.
* The **pending** state indicates the underlying socket connection has been successfully established and requests are queueing.
  * The *process* event transitions the `Client` to the **processing** state where requests are processed.
  * If requests are queued, the *close* event transitions to the **processing** state; otherwise, it transitions to the **destroyed** state.
  * The *destroy* event transitions to the **destroyed** state.
* The **processing** state initializes to the **processing.running** state.
  * If the current request requires draining, the *needDrain* event transitions the `Client` into the **processing.busy** state which will return to the **processing.running** state with the *drainComplete* event.
  * After all queued requests are completed, the *keepalive* event transitions the `Client` back to the **pending** state. If no requests are queued during the timeout, the **close** event transitions the `Client` to the **destroyed** state.
  * If the *close* event is fired while the `Client` still has queued requests, the `Client` transitions to the **process.closing** state where it will complete all existing requests before firing the *done* event.
  * The *done* event gracefully transitions the `Client` to the **destroyed** state.
  * At any point in time, the *destroy* event will transition the `Client` from the **processing** state to the **destroyed** state, destroying any queued requests.
* The **destroyed** state is a final state and the `Client` is no longer functional.

A state diagram representing an Undici Client instance:

```mermaid
stateDiagram-v2
  [*] --> idle
  idle --> pending : connect
  idle --> destroyed : destroy/close

  pending --> idle : timeout
  pending --> destroyed : destroy

  state close_fork <<fork>>
  pending --> close_fork : close
  close_fork --> processing
  close_fork --> destroyed

  pending --> processing : process

  processing --> pending : keepalive
  processing --> destroyed : done
  processing --> destroyed : destroy

  destroyed --> [*]

  state processing {
      [*] --> running
      running --> closing : close
      running --> busy : needDrain
      busy --> running : drainComplete
      running --> [*] : keepalive
      closing --> [*] : done
  }
```
## State details

### idle

The **idle** state is the initial state of a `Client` instance. While an `origin` is required for instantiating a `Client` instance, the underlying socket connection will not be established until a request is queued using [`Client.dispatch()`](/docs/docs/api/Client.md#clientdispatchoptions-handlers). By calling `Client.dispatch()` directly or using one of the multiple implementations ([`Client.connect()`](Client.md#clientconnectoptions-callback), [`Client.pipeline()`](Client.md#clientpipelineoptions-handler), [`Client.request()`](Client.md#clientrequestoptions-callback), [`Client.stream()`](Client.md#clientstreamoptions-factory-callback), and [`Client.upgrade()`](/docs/docs/api/Client.md#clientupgradeoptions-callback)), the `Client` instance will transition from **idle** to [**pending**](/docs/docs/api/Client.md#pending) and then most likely directly to [**processing**](/docs/docs/api/Client.md#processing).

Calling [`Client.close()`](/docs/docs/api/Client.md#clientclosecallback) or [`Client.destroy()`](Client.md#clientdestroyerror-callback) transitions directly to the [**destroyed**](/docs/docs/api/Client.md#destroyed) state since the `Client` instance will have no queued requests in this state.

### pending

The **pending** state signifies a non-processing `Client`. Upon entering this state, the `Client` establishes a socket connection and emits the [`'connect'`](/docs/docs/api/Client.md#event-connect) event signalling a connection was successfully established with the `origin` provided during `Client` instantiation. The internal queue is initially empty, and requests can start queueing.

Calling [`Client.close()`](/docs/docs/api/Client.md#clientclosecallback) with queued requests, transitions the `Client` to the [**processing**](/docs/docs/api/Client.md#processing) state. Without queued requests, it transitions to the [**destroyed**](/docs/docs/api/Client.md#destroyed) state.

Calling [`Client.destroy()`](/docs/docs/api/Client.md#clientdestroyerror-callback) transitions directly to the [**destroyed**](/docs/docs/api/Client.md#destroyed) state regardless of existing requests.

### processing

The **processing** state is a state machine within itself. It initializes to the [**processing.running**](/docs/docs/api/Client.md#running) state. The [`Client.dispatch()`](/docs/docs/api/Client.md#clientdispatchoptions-handlers), [`Client.close()`](Client.md#clientclosecallback), and [`Client.destroy()`](Client.md#clientdestroyerror-callback) can be called at any time while the `Client` is in this state. `Client.dispatch()` will add more requests to the queue while existing requests continue to be processed. `Client.close()` will transition to the [**processing.closing**](/docs/docs/api/Client.md#closing) state. And `Client.destroy()` will transition to [**destroyed**](/docs/docs/api/Client.md#destroyed).

#### running

In the **processing.running** sub-state, queued requests are being processed in a FIFO order. If a request body requires draining, the *needDrain* event transitions to the [**processing.busy**](/docs/docs/api/Client.md#busy) sub-state. The *close* event transitions the Client to the [**process.closing**](/docs/docs/api/Client.md#closing) sub-state. If all queued requests are processed and neither [`Client.close()`](/docs/docs/api/Client.md#clientclosecallback) nor [`Client.destroy()`](Client.md#clientdestroyerror-callback) are called, then the [**processing**](/docs/docs/api/Client.md#processing) machine will trigger a *keepalive* event transitioning the `Client` back to the [**pending**](/docs/docs/api/Client.md#pending) state. During this time, the `Client` is waiting for the socket connection to timeout, and once it does, it triggers the *timeout* event and transitions to the [**idle**](/docs/docs/api/Client.md#idle) state.

#### busy

This sub-state is only entered when a request body is an instance of [Stream](https://nodejs.org/api/stream.html) and requires draining. The `Client` cannot process additional requests while in this state and must wait until the currently processing request body is completely drained before transitioning back to [**processing.running**](/docs/docs/api/Client.md#running).

#### closing

This sub-state is only entered when a `Client` instance has queued requests and the [`Client.close()`](/docs/docs/api/Client.md#clientclosecallback) method is called. In this state, the `Client` instance continues to process requests as usual, with the one exception that no additional requests can be queued. Once all of the queued requests are processed, the `Client` will trigger the *done* event gracefully entering the [**destroyed**](/docs/docs/api/Client.md#destroyed) state without an error.

### destroyed

The **destroyed** state is a final state for the `Client` instance. Once in this state, a `Client` is nonfunctional. Calling any other `Client` methods will result in an `ClientDestroyedError`.

```

## File: balancedpool.md
```
# Class: BalancedPool

Extends: `undici.Dispatcher`

A pool of [Pool](/docs/docs/api/Pool.md) instances connected to multiple upstreams.

Requests are not guaranteed to be dispatched in order of invocation.

## `new BalancedPool(upstreams [, options])`

Arguments:

* **upstreams** `URL | string | string[]` - It should only include the **protocol, hostname, and port**.
* **options** `BalancedPoolOptions` (optional)

### Parameter: `BalancedPoolOptions`

Extends: [`PoolOptions`](/docs/docs/api/Pool.md#parameter-pooloptions)

* **factory** `(origin: URL, opts: Object) => Dispatcher` - Default: `(origin, opts) => new Pool(origin, opts)`

The `PoolOptions` are passed to each of the `Pool` instances being created.
## Instance Properties

### `BalancedPool.upstreams`

Returns an array of upstreams that were previously added.

### `BalancedPool.closed`

Implements [Client.closed](/docs/docs/api/Client.md#clientclosed)

### `BalancedPool.destroyed`

Implements [Client.destroyed](/docs/docs/api/Client.md#clientdestroyed)

### `Pool.stats`

Returns [`PoolStats`](/docs/docs/api/PoolStats.md) instance for this pool.

## Instance Methods

### `BalancedPool.addUpstream(upstream)`

Add an upstream.

Arguments:

* **upstream** `string` - It should only include the **protocol, hostname, and port**.

### `BalancedPool.removeUpstream(upstream)`

Removes an upstream that was previously added.

### `BalancedPool.close([callback])`

Implements [`Dispatcher.close([callback])`](/docs/docs/api/Dispatcher.md#dispatcherclosecallback-promise).

### `BalancedPool.destroy([error, callback])`

Implements [`Dispatcher.destroy([error, callback])`](/docs/docs/api/Dispatcher.md#dispatcherdestroyerror-callback-promise).

### `BalancedPool.connect(options[, callback])`

See [`Dispatcher.connect(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherconnectoptions-callback).

### `BalancedPool.dispatch(options, handlers)`

Implements [`Dispatcher.dispatch(options, handlers)`](/docs/docs/api/Dispatcher.md#dispatcherdispatchoptions-handler).

### `BalancedPool.pipeline(options, handler)`

See [`Dispatcher.pipeline(options, handler)`](/docs/docs/api/Dispatcher.md#dispatcherpipelineoptions-handler).

### `BalancedPool.request(options[, callback])`

See [`Dispatcher.request(options [, callback])`](/docs/docs/api/Dispatcher.md#dispatcherrequestoptions-callback).

### `BalancedPool.stream(options, factory[, callback])`

See [`Dispatcher.stream(options, factory[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherstreamoptions-factory-callback).

### `BalancedPool.upgrade(options[, callback])`

See [`Dispatcher.upgrade(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherupgradeoptions-callback).

## Instance Events

### Event: `'connect'`

See [Dispatcher Event: `'connect'`](/docs/docs/api/Dispatcher.md#event-connect).

### Event: `'disconnect'`

See [Dispatcher Event: `'disconnect'`](/docs/docs/api/Dispatcher.md#event-disconnect).

### Event: `'drain'`

See [Dispatcher Event: `'drain'`](/docs/docs/api/Dispatcher.md#event-drain).

```

## File: builtin_tools.md
```
# `pydantic_ai.builtin_tools`

::: pydantic_ai.builtin_tools

```

## File: cachestorage.md
```
# CacheStorage

Undici exposes a W3C spec-compliant implementation of [CacheStorage](https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage) and [Cache](https://developer.mozilla.org/en-US/docs/Web/API/Cache).

## Opening a Cache

Undici exports a top-level CacheStorage instance. You can open a new Cache, or duplicate a Cache with an existing name, by using `CacheStorage.prototype.open`. If you open a Cache with the same name as an already-existing Cache, its list of cached Responses will be shared between both instances.

```mjs
import { caches } from 'undici'

const cache_1 = await caches.open('v1')
const cache_2 = await caches.open('v1')

// Although .open() creates a new instance,
assert(cache_1 !== cache_2)
// The same Response is matched in both.
assert.deepStrictEqual(await cache_1.match('/req'), await cache_2.match('/req'))
```

## Deleting a Cache

If a Cache is deleted, the cached Responses/Requests can still be used.

```mjs
const response = await cache_1.match('/req')
await caches.delete('v1')

await response.text() // the Response's body
```

```

## File: cachestore.md
```
# Cache Store

A Cache Store is responsible for storing and retrieving cached responses.
It is also responsible for deciding which specific response to use based off of
a response's `Vary` header (if present). It is expected to be compliant with
[RFC-9111](https://www.rfc-editor.org/rfc/rfc9111.html).

## Pre-built Cache Stores

### `MemoryCacheStore`

The `MemoryCacheStore` stores the responses in-memory.

**Options**

- `maxSize` - The maximum total size in bytes of all stored responses. Default `104857600` (100MB).
- `maxCount` - The maximum amount of responses to store. Default `1024`.
- `maxEntrySize` - The maximum size in bytes that a response's body can be. If a response's body is greater than or equal to this, the response will not be cached. Default `5242880` (5MB).

### Getters

#### `MemoryCacheStore.size`

Returns the current total size in bytes of all stored responses.

### Methods

#### `MemoryCacheStore.isFull()`

Returns a boolean indicating whether the cache has reached its maximum size or count.

### Events

#### `'maxSizeExceeded'`

Emitted when the cache exceeds its maximum size or count limits. The event payload contains `size`, `maxSize`, `count`, and `maxCount` properties.


### `SqliteCacheStore`

The `SqliteCacheStore` stores the responses in a SQLite database.
Under the hood, it uses Node.js' [`node:sqlite`](https://nodejs.org/api/sqlite.html) api.
The `SqliteCacheStore` is only exposed if the `node:sqlite` api is present.

**Options**

- `location` - The location of the SQLite database to use. Default `:memory:`.
- `maxCount` - The maximum number of entries to store in the database. Default `Infinity`.
- `maxEntrySize` - The maximum size in bytes that a response's body can be. If a response's body is greater than or equal to this, the response will not be cached. Default `Infinity`.

## Defining a Custom Cache Store

The store must implement the following functions:

### Getter: `isFull`

Optional. This tells the cache interceptor if the store is full or not. If this is true,
the cache interceptor will not attempt to cache the response.

### Function: `get`

Parameters:

* **req** `Dispatcher.RequestOptions` - Incoming request

Returns: `GetResult | Promise<GetResult | undefined> | undefined` - If the request is cached, the cached response is returned. If the request's method is anything other than HEAD, the response is also returned.
If the request isn't cached, `undefined` is returned.

The `get` method may return a `Promise` for async cache stores (e.g. Redis-backed or remote stores). The cache interceptor handles both synchronous and asynchronous return values, including in revalidation paths (304 Not Modified handling and stale-while-revalidate background revalidation).

Response properties:

* **response** `CacheValue` - The cached response data.
* **body** `Readable | Iterable<Buffer> | undefined` - The response's body. This can be an array of `Buffer` chunks (with a `.values()` method) or a `Readable` stream. Both formats are supported in all code paths, including 304 revalidation.

### Function: `createWriteStream`

Parameters:

* **req** `Dispatcher.RequestOptions` - Incoming request
* **value** `CacheValue` - Response to store

Returns: `Writable | undefined` - If the store is full, return `undefined`. Otherwise, return a writable so that the cache interceptor can stream the body and trailers to the store.

## `CacheValue`

This is an interface containing the majority of a response's data (minus the body).

### Property `statusCode`

`number` - The response's HTTP status code.

### Property `statusMessage`

`string` - The response's HTTP status message.

### Property `rawHeaders`

`Buffer[]` - The response's headers.

### Property `vary`

`Record<string, string | string[] | null> | undefined` - The headers defined by the response's `Vary` header
and their respective values for later comparison. Values are `null` when the
header specified in `Vary` was not present in the original request. These `null`
values are automatically filtered out during revalidation so they are not sent
as request headers.

For example, for a response like
```
Vary: content-encoding, accepts
content-encoding: utf8
accepts: application/json
```

This would be
```js
{
  'content-encoding': 'utf8',
  accepts: 'application/json'
}
```

If the original request did not include the `accepts` header:
```js
{
  'content-encoding': 'utf8',
  accepts: null
}
```

### Property `cachedAt`

`number` - Time in millis that this value was cached.

### Property `staleAt`

`number` - Time in millis that this value is considered stale.

### Property `deleteAt`

`number` - Time in millis that this value is to be deleted from the cache. This
is either the same sa staleAt or the `max-stale` caching directive.

The store must not return a response after the time defined in this property.

## `CacheStoreReadable`

This extends Node's [`Readable`](https://nodejs.org/api/stream.html#class-streamreadable)
and defines extra properties relevant to the cache interceptor.

### Getter: `value`

The response's [`CacheStoreValue`](/docs/docs/api/CacheStore.md#cachestorevalue)

## `CacheStoreWriteable`

This extends Node's [`Writable`](https://nodejs.org/api/stream.html#class-streamwritable)
and defines extra properties relevant to the cache interceptor.

### Setter: `rawTrailers`

If the response has trailers, the cache interceptor will pass them to the cache
interceptor through this method.

```

## File: capabilities.md
```
# `pydantic_ai.capabilities`

::: pydantic_ai.capabilities

```

## File: client.md
```
# Class: Client

Extends: `undici.Dispatcher`

A basic HTTP/1.1 client, mapped on top a single TCP/TLS connection. Pipelining is disabled by default.

Requests are not guaranteed to be dispatched in order of invocation.

## `new Client(url[, options])`

Arguments:

* **url** `URL | string` - Should only include the **protocol, hostname, and port**.
* **options** `ClientOptions` (optional)

Returns: `Client`

### Parameter: `ClientOptions`

* **bodyTimeout** `number | null` (optional) - Default: `300e3` - The timeout after which a request will time out, in milliseconds. Monitors time between receiving body data. Use `0` to disable it entirely. Defaults to 300 seconds. Please note the `timeout` will be reset if you keep writing data to the socket everytime.
* **headersTimeout** `number | null` (optional) - Default: `300e3` - The amount of time, in milliseconds, the parser will wait to receive the complete HTTP headers while not sending the request. Defaults to 300 seconds.
* **keepAliveMaxTimeout** `number | null` (optional) - Default: `600e3` - The maximum allowed `keepAliveTimeout`, in milliseconds, when overridden by *keep-alive* hints from the server. Defaults to 10 minutes.
* **keepAliveTimeout** `number | null` (optional) - Default: `4e3` - The timeout, in milliseconds, after which a socket without active requests will time out. Monitors time between activity on a connected socket. This value may be overridden by *keep-alive* hints from the server. See [MDN: HTTP - Headers - Keep-Alive directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Keep-Alive#directives) for more details. Defaults to 4 seconds.
* **keepAliveTimeoutThreshold** `number | null` (optional) - Default: `2e3` - A number of milliseconds subtracted from server *keep-alive* hints when overriding `keepAliveTimeout` to account for timing inaccuracies caused by e.g. transport latency. Defaults to 2 seconds.
* **maxHeaderSize** `number | null` (optional) - Default: `--max-http-header-size` or `16384` - The maximum length of request headers in bytes. Defaults to Node.js' --max-http-header-size or 16KiB.
* **maxResponseSize** `number | null` (optional) - Default: `-1` - The maximum length of response body in bytes. Set to `-1` to disable.
* **pipelining** `number | null` (optional) - Default: `1` - The amount of concurrent requests to be sent over the single TCP/TLS connection according to [RFC7230](https://tools.ietf.org/html/rfc7230#section-6.3.2). Carefully consider your workload and environment before enabling concurrent requests as pipelining may reduce performance if used incorrectly. Pipelining is sensitive to network stack settings as well as head of line blocking caused by e.g. long running requests. Set to `0` to disable keep-alive connections.
* **connect** `ConnectOptions | Function | null` (optional) - Default: `null`.
* **strictContentLength** `Boolean` (optional) - Default: `true` - Whether to treat request content length mismatches as errors. If true, an error is thrown when the request content-length header doesn't match the length of the request body. **Security Warning:** Disabling this option can expose your application to HTTP Request Smuggling attacks, where mismatched content-length headers cause servers and proxies to interpret request boundaries differently. This can lead to cache poisoning, credential hijacking, and bypassing security controls. Only disable this in controlled environments where you fully trust the request source.
* **autoSelectFamily**: `boolean` (optional) - Default: depends on local Node version, on Node 18.13.0 and above is `false`. Enables a family autodetection algorithm that loosely implements section 5 of [RFC 8305](https://tools.ietf.org/html/rfc8305#section-5). See [here](https://nodejs.org/api/net.html#socketconnectoptions-connectlistener) for more details. This option is ignored if not supported by the current Node version.
* **autoSelectFamilyAttemptTimeout**: `number` - Default: depends on local Node version, on Node 18.13.0 and above is `250`. The amount of time in milliseconds to wait for a connection attempt to finish before trying the next address when using the `autoSelectFamily` option. See [here](https://nodejs.org/api/net.html#socketconnectoptions-connectlistener) for more details.
* **allowH2**: `boolean` - Default: `true`. Enables support for H2 if the server has assigned bigger priority to it through ALPN negotiation.
* **useH2c**: `boolean` - Default: `false`. Enforces h2c for non-https connections.
* **maxConcurrentStreams**: `number` - Default: `100`. Dictates the maximum number of concurrent streams for a single H2 session. It can be overridden by a SETTINGS remote frame.
* **initialWindowSize**: `number` (optional) - Default: `262144` (256KB). Sets the HTTP/2 stream-level flow-control window size (SETTINGS_INITIAL_WINDOW_SIZE). Must be a positive integer greater than 0. This default is higher than Node.js core's default (65535 bytes) to improve throughput, Node's choice is very conservative for current high-bandwith networks. See [RFC 7540 Section 6.9.2](https://datatracker.ietf.org/doc/html/rfc7540#section-6.9.2) for more details.
* **connectionWindowSize**: `number` (optional) - Default `524288` (512KB). Sets the HTTP/2 connection-level flow-control window size using `ClientHttp2Session.setLocalWindowSize()`. Must be a positive integer greater than 0. This provides better flow control for the entire connection across multiple streams. See [Node.js HTTP/2 documentation](https://nodejs.org/api/http2.html#clienthttp2sessionsetlocalwindowsize) for more details.
* **pingInterval**: `number` - Default: `60e3`. The time interval in milliseconds between PING frames sent to the server. Set to `0` to disable PING frames. This is only applicable for HTTP/2 connections. This will emit a `ping` event on the client with the duration of the ping in milliseconds.

> **Notes about HTTP/2**
> - It only works under TLS connections. h2c is not supported.
> - The server must support HTTP/2 and choose it as the protocol during the ALPN negotiation.
>   - The server must not have a bigger priority for HTTP/1.1 than HTTP/2.
> - Pseudo headers are automatically attached to the request. If you try to set them, they will be overwritten.
>   - The `:path` header is automatically set to the request path.
>   - The `:method` header is automatically set to the request method.
>   - The `:scheme` header is automatically set to the request scheme.
>   - The `:authority` header is automatically set to the request `host[:port]`.
> - `PUSH` frames are yet not supported.

#### Parameter: `ConnectOptions`

Every Tls option, see [here](https://nodejs.org/api/tls.html#tls_tls_connect_options_callback).
Furthermore, the following options can be passed:

* **socketPath** `string | null` (optional) - Default: `null` - An IPC endpoint, either Unix domain socket or Windows named pipe.
* **maxCachedSessions** `number | null` (optional) - Default: `100` - Maximum number of TLS cached sessions. Use 0 to disable TLS session caching. Default: 100.
* **timeout** `number | null` (optional) -  In milliseconds, Default `10e3`.
* **servername** `string | null` (optional)
* **keepAlive** `boolean | null` (optional) - Default: `true` - TCP keep-alive enabled
* **keepAliveInitialDelay** `number | null` (optional) - Default: `60000` - TCP keep-alive interval for the socket in milliseconds

### Example - Basic Client instantiation

This will instantiate the undici Client, but it will not connect to the origin until something is queued. Consider using `client.connect` to prematurely connect to the origin, or just call `client.request`.

```js
'use strict'
import { Client } from 'undici'

const client = new Client('http://localhost:3000')
```

### Example - Custom connector

This will allow you to perform some additional check on the socket that will be used for the next request.

```js
'use strict'
import { Client, buildConnector } from 'undici'

const connector = buildConnector({ rejectUnauthorized: false })
const client = new Client('https://localhost:3000', {
  connect (opts, cb) {
    connector(opts, (err, socket) => {
      if (err) {
        cb(err)
      } else if (/* assertion */) {
        socket.destroy()
        cb(new Error('kaboom'))
      } else {
        cb(null, socket)
      }
    })
  }
})
```

## Instance Methods

### `Client.close([callback])`

Implements [`Dispatcher.close([callback])`](/docs/docs/api/Dispatcher.md#dispatcherclosecallback-promise).

### `Client.destroy([error, callback])`

Implements [`Dispatcher.destroy([error, callback])`](/docs/docs/api/Dispatcher.md#dispatcherdestroyerror-callback-promise).

Waits until socket is closed before invoking the callback (or returning a promise if no callback is provided).

### `Client.connect(options[, callback])`

See [`Dispatcher.connect(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherconnectoptions-callback).

### `Client.dispatch(options, handlers)`

Implements [`Dispatcher.dispatch(options, handlers)`](/docs/docs/api/Dispatcher.md#dispatcherdispatchoptions-handler).

### `Client.pipeline(options, handler)`

See [`Dispatcher.pipeline(options, handler)`](/docs/docs/api/Dispatcher.md#dispatcherpipelineoptions-handler).

### `Client.request(options[, callback])`

See [`Dispatcher.request(options [, callback])`](/docs/docs/api/Dispatcher.md#dispatcherrequestoptions-callback).

### `Client.stream(options, factory[, callback])`

See [`Dispatcher.stream(options, factory[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherstreamoptions-factory-callback).

### `Client.upgrade(options[, callback])`

See [`Dispatcher.upgrade(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherupgradeoptions-callback).

## Instance Properties

### `Client.closed`

* `boolean`

`true` after `client.close()` has been called.

### `Client.destroyed`

* `boolean`

`true` after `client.destroyed()` has been called or `client.close()` has been called and the client shutdown has completed.

### `Client.pipelining`

* `number`

Property to get and set the pipelining factor.

## Instance Events

### Event: `'connect'`

See [Dispatcher Event: `'connect'`](/docs/docs/api/Dispatcher.md#event-connect).

Parameters:

* **origin** `URL`
* **targets** `Array<Dispatcher>`

Emitted when a socket has been created and connected. The client will connect once `client.size > 0`.

#### Example - Client connect event

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  response.end('Hello, World!')
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)

client.on('connect', (origin) => {
  console.log(`Connected to ${origin}`) // should print before the request body statement
})

try {
  const { body } = await client.request({
    path: '/',
    method: 'GET'
  })
  body.setEncoding('utf-8')
  body.on('data', console.log)
  client.close()
  server.close()
} catch (error) {
  console.error(error)
  client.close()
  server.close()
}
```

### Event: `'disconnect'`

See [Dispatcher Event: `'disconnect'`](/docs/docs/api/Dispatcher.md#event-disconnect).

Parameters:

* **origin** `URL`
* **targets** `Array<Dispatcher>`
* **error** `Error`

Emitted when socket has disconnected. The error argument of the event is the error which caused the socket to disconnect. The client will reconnect if or once `client.size > 0`.

#### Example - Client disconnect event

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  response.destroy()
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)

client.on('disconnect', (origin) => {
  console.log(`Disconnected from ${origin}`)
})

try {
  await client.request({
    path: '/',
    method: 'GET'
  })
} catch (error) {
  console.error(error.message)
  client.close()
  server.close()
}
```

### Event: `'drain'`

Emitted when pipeline is no longer busy.

See [Dispatcher Event: `'drain'`](/docs/docs/api/Dispatcher.md#event-drain).

#### Example - Client drain event

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  response.end('Hello, World!')
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)

client.on('drain', () => {
  console.log('drain event')
  client.close()
  server.close()
})

const requests = [
  client.request({ path: '/', method: 'GET' }),
  client.request({ path: '/', method: 'GET' }),
  client.request({ path: '/', method: 'GET' })
]

await Promise.all(requests)

console.log('requests completed')
```

### Event: `'error'`

Invoked for user errors such as throwing in the `onResponseError` handler.

```

## File: clientstats.md
```
# Class: ClientStats

Stats for a [Client](/docs/docs/api/Client.md).

## `new ClientStats(client)`

Arguments:

* **client** `Client` - Client from which to return stats.

## Instance Properties

### `ClientStats.connected`

Boolean if socket as open connection by this client.

### `ClientStats.pending`

Number of pending requests of this client.

### `ClientStats.running`

Number of currently active requests across this client.

### `ClientStats.size`

Number of active, pending, or queued requests of this clients.

```

## File: common_tools.md
```
# `pydantic_ai.common_tools`

::: pydantic_ai.common_tools.duckduckgo

::: pydantic_ai.common_tools.exa

::: pydantic_ai.common_tools.tavily

```

## File: concurrency.md
```
# `pydantic_ai` — Concurrency

::: pydantic_ai.ConcurrencyLimitedModel

::: pydantic_ai.limit_model_concurrency

::: pydantic_ai.AbstractConcurrencyLimiter

::: pydantic_ai.ConcurrencyLimiter

::: pydantic_ai.ConcurrencyLimit

::: pydantic_ai.AnyConcurrencyLimit

::: pydantic_ai.ConcurrencyLimitExceeded

```

## File: connector.md
```
# Connector

Undici creates the underlying socket via the connector builder.
Normally, this happens automatically and you don't need to care about this,
but if you need to perform some additional check over the currently used socket,
this is the right place.

If you want to create a custom connector, you must import the `buildConnector` utility.

#### Parameter: `buildConnector.BuildOptions`

Every Tls option, see [here](https://nodejs.org/api/tls.html#tls_tls_connect_options_callback).
Furthermore, the following options can be passed:

* **socketPath** `string | null` (optional) - Default: `null` - An IPC endpoint, either Unix domain socket or Windows named pipe.
* **maxCachedSessions** `number | null` (optional) - Default: `100` - Maximum number of TLS cached sessions. Use 0 to disable TLS session caching. Default: `100`.
* **timeout** `number | null` (optional) -  In milliseconds. Default `10e3`.
* **servername** `string | null` (optional)

Once you call `buildConnector`, it will return a connector function, which takes the following parameters.

#### Parameter: `connector.Options`

* **hostname** `string` (required)
* **host** `string` (optional)
* **protocol** `string` (required)
* **port** `string` (required)
* **servername** `string` (optional)
* **localAddress** `string | null` (optional) Local address the socket should connect from.
* **httpSocket** `Socket` (optional) Establish secure connection on a given socket rather than creating a new socket. It can only be sent on TLS update.

### Basic example

```js
'use strict'

import { Client, buildConnector } from 'undici'

const connector = buildConnector({ rejectUnauthorized: false })
const client = new Client('https://localhost:3000', {
  connect (opts, cb) {
    connector(opts, (err, socket) => {
      if (err) {
        cb(err)
      } else if (/* assertion */) {
        socket.destroy()
        cb(new Error('kaboom'))
      } else {
        cb(null, socket)
      }
    })
  }
})
```

### Example: validate the CA fingerprint

```js
'use strict'

import { Client, buildConnector } from 'undici'

const caFingerprint = 'FO:OB:AR'
const connector = buildConnector({ rejectUnauthorized: false })
const client = new Client('https://localhost:3000', {
  connect (opts, cb) {
    connector(opts, (err, socket) => {
      if (err) {
        cb(err)
      } else if (getIssuerCertificate(socket).fingerprint256 !== caFingerprint) {
        socket.destroy()
        cb(new Error('Fingerprint does not match or malformed certificate'))
      } else {
        cb(null, socket)
      }
    })
  }
})

client.request({
  path: '/',
  method: 'GET'
}, (err, data) => {
  if (err) throw err

  const bufs = []
  data.body.on('data', (buf) => {
    bufs.push(buf)
  })
  data.body.on('end', () => {
    console.log(Buffer.concat(bufs).toString('utf8'))
    client.close()
  })
})

function getIssuerCertificate (socket) {
  let certificate = socket.getPeerCertificate(true)
  while (certificate && Object.keys(certificate).length > 0) {
    // invalid certificate
    if (certificate.issuerCertificate == null) {
      return null
    }

    // We have reached the root certificate.
    // In case of self-signed certificates, `issuerCertificate` may be a circular reference.
    if (certificate.fingerprint256 === certificate.issuerCertificate.fingerprint256) {
      break
    }

    // continue the loop
    certificate = certificate.issuerCertificate
  }
  return certificate
}
```

```

## File: contenttype.md
```
# MIME Type Parsing

## `MIMEType` interface

* **type** `string`
* **subtype** `string`
* **parameters** `Map<string, string>`
* **essence** `string`

## `parseMIMEType(input)`

Implements [parse a MIME type](https://mimesniff.spec.whatwg.org/#parse-a-mime-type).

Parses a MIME type, returning its type, subtype, and any associated parameters. If the parser can't parse an input it returns the string literal `'failure'`.

```js
import { parseMIMEType } from 'undici'

parseMIMEType('text/html; charset=gbk')
// {
//   type: 'text',
//   subtype: 'html',
//   parameters: Map(1) { 'charset' => 'gbk' },
//   essence: 'text/html'
// }
```

Arguments:

* **input** `string`

Returns: `MIMEType|'failure'`

## `serializeAMimeType(input)`

Implements [serialize a MIME type](https://mimesniff.spec.whatwg.org/#serialize-a-mime-type).

Serializes a MIMEType object.

```js
import { serializeAMimeType } from 'undici'

serializeAMimeType({
  type: 'text',
  subtype: 'html',
  parameters: new Map([['charset', 'gbk']]),
  essence: 'text/html'
})
// text/html;charset=gbk

```

Arguments:

* **mimeType** `MIMEType`

Returns: `string`

```

## File: cookies.md
```
# Cookie Handling

## `Cookie` interface

* **name** `string`
* **value** `string`
* **expires** `Date|number` (optional)
* **maxAge** `number` (optional)
* **domain** `string` (optional)
* **path** `string` (optional)
* **secure** `boolean` (optional)
* **httpOnly** `boolean` (optional)
* **sameSite** `'String'|'Lax'|'None'` (optional)
* **unparsed** `string[]` (optional) Left over attributes that weren't parsed.

## `deleteCookie(headers, name[, attributes])`

Sets the expiry time of the cookie to the unix epoch, causing browsers to delete it when received.

```js
import { deleteCookie, Headers } from 'undici'

const headers = new Headers()
deleteCookie(headers, 'name')

console.log(headers.get('set-cookie')) // name=; Expires=Thu, 01 Jan 1970 00:00:00 GMT
```

Arguments:

* **headers** `Headers`
* **name** `string`
* **attributes** `{ path?: string, domain?: string }` (optional)

Returns: `void`

## `getCookies(headers)`

Parses the `Cookie` header and returns a list of attributes and values.

```js
import { getCookies, Headers } from 'undici'

const headers = new Headers({
  cookie: 'get=cookies; and=attributes'
})

console.log(getCookies(headers)) // { get: 'cookies', and: 'attributes' }
```

Arguments:

* **headers** `Headers`

Returns: `Record<string, string>`

## `getSetCookies(headers)`

Parses all `Set-Cookie` headers.

```js
import { getSetCookies, Headers } from 'undici'

const headers = new Headers({ 'set-cookie': 'undici=getSetCookies; Secure' })

console.log(getSetCookies(headers))
// [
//   {
//     name: 'undici',
//     value: 'getSetCookies',
//     secure: true
//   }
// ]

```

Arguments:

* **headers** `Headers`

Returns: `Cookie[]`

## `setCookie(headers, cookie)`

Appends a cookie to the `Set-Cookie` header.

```js
import { setCookie, Headers } from 'undici'

const headers = new Headers()
setCookie(headers, { name: 'undici', value: 'setCookie' })

console.log(headers.get('Set-Cookie')) // undici=setCookie
```

Arguments:

* **headers** `Headers`
* **cookie** `Cookie`

Returns: `void`

```

## File: debug.md
```
# Debug

Undici (and subsenquently `fetch` and `websocket`) exposes a debug statement that can be enabled by setting `NODE_DEBUG` within the environment.

The flags available are:

## `undici`

This flag enables debug statements for the core undici library.

```sh
NODE_DEBUG=undici node script.js

UNDICI 16241: connecting to nodejs.org using https:h1
UNDICI 16241: connecting to nodejs.org using https:h1
UNDICI 16241: connected to nodejs.org using https:h1
UNDICI 16241: sending request to GET https://nodejs.org/
UNDICI 16241: received response to GET https://nodejs.org/ - HTTP 307
UNDICI 16241: connecting to nodejs.org using https:h1
UNDICI 16241: trailers received from GET https://nodejs.org/
UNDICI 16241: connected to nodejs.org using https:h1
UNDICI 16241: sending request to GET https://nodejs.org/en
UNDICI 16241: received response to GET https://nodejs.org/en - HTTP 200
UNDICI 16241: trailers received from GET https://nodejs.org/en
```

## `fetch`

This flag enables debug statements for the `fetch` API.

> **Note**: statements are pretty similar to the ones in the `undici` flag, but scoped to `fetch`

```sh
NODE_DEBUG=fetch node script.js

FETCH 16241: connecting to nodejs.org using https:h1
FETCH 16241: connecting to nodejs.org using https:h1
FETCH 16241: connected to nodejs.org using https:h1
FETCH 16241: sending request to GET https://nodejs.org/
FETCH 16241: received response to GET https://nodejs.org/ - HTTP 307
FETCH 16241: connecting to nodejs.org using https:h1
FETCH 16241: trailers received from GET https://nodejs.org/
FETCH 16241: connected to nodejs.org using https:h1
FETCH 16241: sending request to GET https://nodejs.org/en
FETCH 16241: received response to GET https://nodejs.org/en - HTTP 200
FETCH 16241: trailers received from GET https://nodejs.org/en
```

## `websocket`

This flag enables debug statements for the `Websocket` API.

> **Note**: statements can overlap with `UNDICI` ones if `undici` or `fetch` flag has been enabled as well.

```sh
NODE_DEBUG=websocket node script.js

WEBSOCKET 18309: connecting to echo.websocket.org using https:h1
WEBSOCKET 18309: connected to echo.websocket.org using https:h1
WEBSOCKET 18309: sending request to GET https://echo.websocket.org/
WEBSOCKET 18309: connection opened <ip_address>
```

```

## File: diagnosticschannel.md
```
# Diagnostics Channel Support

Stability: Experimental.

Undici supports the [`diagnostics_channel`](https://nodejs.org/api/diagnostics_channel.html) (currently available only on Node.js v16+).
It is the preferred way to instrument Undici and retrieve internal information.

The channels available are the following.

## `undici:request:create`

This message is published when a new outgoing request is created.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:request:create').subscribe(({ request }) => {
  console.log('origin', request.origin)
  console.log('completed', request.completed)
  console.log('method', request.method)
  console.log('path', request.path)
  console.log('headers', request.headers) // array of strings, e.g: ['foo', 'bar']
  request.addHeader('hello', 'world')
  console.log('headers', request.headers) // e.g. ['foo', 'bar', 'hello', 'world']
})
```

Note: a request is only loosely completed to a given socket.

## `undici:request:bodyChunkSent`

This message is published when a chunk of the request body is being sent.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:request:bodyChunkSent').subscribe(({ request, chunk }) => {
  // request is the same object undici:request:create
})
```

## `undici:request:bodySent`

This message is published after the request body has been fully sent.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:request:bodySent').subscribe(({ request }) => {
  // request is the same object undici:request:create
})
```

## `undici:request:headers`

This message is published after the response headers have been received.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:request:headers').subscribe(({ request, response }) => {
  // request is the same object undici:request:create
  console.log('statusCode', response.statusCode)
  console.log(response.statusText)
  // response.headers are buffers.
  console.log(response.headers.map((x) => x.toString()))
})
```

## `undici:request:bodyChunkReceived`

This message is published after a chunk of the response body has been received.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:request:bodyChunkReceived').subscribe(({ request, chunk }) => {
  // request is the same object undici:request:create
})
```

## `undici:request:trailers`

This message is published after the response body and trailers have been received, i.e. the response has been completed.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:request:trailers').subscribe(({ request, trailers }) => {
  // request is the same object undici:request:create
  console.log('completed', request.completed)
  // trailers are buffers.
  console.log(trailers.map((x) => x.toString()))
})
```

## `undici:request:error`

This message is published if the request is going to error, but it has not errored yet.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:request:error').subscribe(({ request, error }) => {
  // request is the same object undici:request:create
})
```

## `undici:client:sendHeaders`

This message is published right before the first byte of the request is written to the socket.

*Note*: It will publish the exact headers that will be sent to the server in raw format.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:client:sendHeaders').subscribe(({ request, headers, socket }) => {
  // request is the same object undici:request:create
  console.log(`Full headers list ${headers.split('\r\n')}`);
})
```

## `undici:client:beforeConnect`

This message is published before creating a new connection for **any** request.
You can not assume that this event is related to any specific request.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:client:beforeConnect').subscribe(({ connectParams, connector }) => {
  // const { host, hostname, protocol, port, servername, version } = connectParams
  // connector is a function that creates the socket
})
```

## `undici:client:connected`

This message is published after a connection is established.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:client:connected').subscribe(({ socket, connectParams, connector }) => {
  // const { host, hostname, protocol, port, servername, version } = connectParams
 // connector is a function that creates the socket
})
```

## `undici:client:connectError`

This message is published if it did not succeed to create new connection

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:client:connectError').subscribe(({ error, socket, connectParams, connector }) => {
  // const { host, hostname, protocol, port, servername, version } = connectParams
  // connector is a function that creates the socket
  console.log(`Connect failed with ${error.message}`)
})
```

## `undici:websocket:open`

This message is published after the client has successfully connected to a server.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:websocket:open').subscribe(({ 
  address,           // { address: string, family: string, port: number }
  protocol,          // string - negotiated subprotocol
  extensions,        // string - negotiated extensions
  websocket,         // WebSocket - the WebSocket instance
  handshakeResponse  // object - HTTP response that upgraded the connection
}) => {
  console.log(address) // address, family, and port
  console.log(protocol) // negotiated subprotocols
  console.log(extensions) // negotiated extensions
  console.log(websocket) // the WebSocket instance
  
  // Handshake response details
  console.log(handshakeResponse.status) // 101 for HTTP/1.1, 200 for HTTP/2 extended CONNECT
  console.log(handshakeResponse.statusText) // 'Switching Protocols' for HTTP/1.1, commonly 'OK' for HTTP/2 in Node.js
  console.log(handshakeResponse.headers) // Object containing response headers
})
```

### Handshake Response Object

The `handshakeResponse` object contains the HTTP response that established the WebSocket connection:

- `status` (number): The HTTP status code (`101` for HTTP/1.1 upgrade, `200` for HTTP/2 extended CONNECT)
- `statusText` (string): The HTTP status message (`'Switching Protocols'` for HTTP/1.1, commonly `'OK'` for HTTP/2 in Node.js)
- `headers` (object): The HTTP response headers from the server, including:
  - `sec-websocket-accept` and other WebSocket-related headers
  - `upgrade: 'websocket'`
  - `connection: 'upgrade'`

  The `upgrade` and `connection` headers are only present for HTTP/1.1 handshakes.

This information is particularly useful for debugging and monitoring WebSocket connections, as it provides access to the initial HTTP handshake response that established the WebSocket connection.

## `undici:websocket:close`

This message is published after the connection has closed.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:websocket:close').subscribe(({ websocket, code, reason }) => {
  console.log(websocket) // the WebSocket instance
  console.log(code) // the closing status code
  console.log(reason) // the closing reason
})
```

## `undici:websocket:socket_error`

This message is published if the socket experiences an error.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:websocket:socket_error').subscribe((error) => {
  console.log(error)
})
```

## `undici:websocket:ping`

This message is published after the client receives a ping frame, if the connection is not closing.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:websocket:ping').subscribe(({ payload, websocket }) => {
  // a Buffer or undefined, containing the optional application data of the frame
  console.log(payload)
  console.log(websocket) // the WebSocket instance
})
```

## `undici:websocket:pong`

This message is published after the client receives a pong frame.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:websocket:pong').subscribe(({ payload, websocket }) => {
  // a Buffer or undefined, containing the optional application data of the frame
  console.log(payload)
  console.log(websocket) // the WebSocket instance
})
```

## `undici:proxy:connected`

This message is published after the `ProxyAgent` establishes a connection to the proxy server.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:proxy:connected').subscribe(({ socket, connectParams }) => {
  console.log(socket)
  console.log(connectParams)
  // const { origin, port, path, signal, headers, servername } = connectParams
})
```

## `undici:request:pending-requests`

This message is published when the deduplicate interceptor's pending request map changes. This is useful for monitoring and debugging request deduplication behavior.

The deduplicate interceptor automatically deduplicates concurrent requests for the same resource. When multiple identical requests are made while one is already in-flight, only one request is sent to the origin server, and all waiting handlers receive the same response.

```js
import diagnosticsChannel from 'diagnostics_channel'

diagnosticsChannel.channel('undici:request:pending-requests').subscribe(({ type, size, key }) => {
  console.log(type)  // 'added' or 'removed'
  console.log(size)  // current number of pending requests
  console.log(key)   // the deduplication key for this request
})
```

### Event Properties

- `type` (`string`): Either `'added'` when a new pending request is registered, or `'removed'` when a pending request completes (successfully or with an error).
- `size` (`number`): The current number of pending requests after the change.
- `key` (`string`): The deduplication key for the request, composed of the origin, method, path, and request headers.

### Example: Monitoring Request Deduplication

```js
import diagnosticsChannel from 'diagnostics_channel'

const channel = diagnosticsChannel.channel('undici:request:pending-requests')

channel.subscribe(({ type, size, key }) => {
  if (type === 'added') {
    console.log(`New pending request: ${key} (${size} total pending)`)
  } else {
    console.log(`Request completed: ${key} (${size} remaining)`)
  }
})
```

This can be useful for:
- Verifying that request deduplication is working as expected
- Monitoring the number of concurrent in-flight requests
- Debugging deduplication behavior in production environments

```

## File: direct.md
```
# `pydantic_ai.direct`

::: pydantic_ai.direct

```

## File: dispatcher.md
```
# Dispatcher

Extends: `events.EventEmitter`

Dispatcher is the core API used to dispatch requests.

Requests are not guaranteed to be dispatched in order of invocation.

## Instance Methods

### `Dispatcher.close([callback]): Promise`

Closes the dispatcher and gracefully waits for enqueued requests to complete before resolving.

Arguments:

* **callback** `(error: Error | null, data: null) => void` (optional)

Returns: `void | Promise<null>` - Only returns a `Promise` if no `callback` argument was passed

```js
dispatcher.close() // -> Promise
dispatcher.close(() => {}) // -> void
```

#### Example - Request resolves before Client closes

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  response.end('undici')
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)

try {
  const { body } = await client.request({
      path: '/',
      method: 'GET'
  })
  body.setEncoding('utf8')
  body.on('data', console.log)
} catch (error) {}

await client.close()

console.log('Client closed')
server.close()
```

### `Dispatcher.connect(options[, callback])`

Starts two-way communications with the requested resource using [HTTP CONNECT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/CONNECT).

Arguments:

* **options** `ConnectOptions`
* **callback** `(err: Error | null, data: ConnectData | null) => void` (optional)

Returns: `void | Promise<ConnectData>` - Only returns a `Promise` if no `callback` argument was passed

#### Parameter: `ConnectOptions`

* **path** `string`
* **headers** `UndiciHeaders` (optional) - Default: `null`
* **signal** `AbortSignal | events.EventEmitter | null` (optional) - Default: `null`
* **opaque** `unknown` (optional) - This argument parameter is passed through to `ConnectData`

#### Parameter: `ConnectData`

* **statusCode** `number`
* **headers** `Record<string, string | string[] | undefined>`
* **socket** `stream.Duplex`
* **opaque** `unknown`

#### Example - Connect request with echo

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  throw Error('should never get here')
}).listen()

server.on('connect', (req, socket, head) => {
  socket.write('HTTP/1.1 200 Connection established\r\n\r\n')

  let data = head.toString()
  socket.on('data', (buf) => {
    data += buf.toString()
  })

  socket.on('end', () => {
    socket.end(data)
  })
})

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)

try {
  const { socket } = await client.connect({
    path: '/'
  })
  const wanted = 'Body'
  let data = ''
  socket.on('data', d => { data += d })
  socket.on('end', () => {
    console.log(`Data received: ${data.toString()} | Data wanted: ${wanted}`)
    client.close()
    server.close()
  })
  socket.write(wanted)
  socket.end()
} catch (error) { }
```

### `Dispatcher.destroy([error, callback]): Promise`

Destroy the dispatcher abruptly with the given error. All the pending and running requests will be asynchronously aborted and error. Since this operation is asynchronously dispatched there might still be some progress on dispatched requests.

Both arguments are optional; the method can be called in four different ways:

Arguments:

* **error** `Error | null` (optional)
* **callback** `(error: Error | null, data: null) => void` (optional)

Returns: `void | Promise<void>` - Only returns a `Promise` if no `callback` argument was passed

```js
dispatcher.destroy() // -> Promise
dispatcher.destroy(new Error()) // -> Promise
dispatcher.destroy(() => {}) // -> void
dispatcher.destroy(new Error(), () => {}) // -> void
```

#### Example - Request is aborted when Client is destroyed

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  response.end()
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)

try {
  const request = client.request({
    path: '/',
    method: 'GET'
  })
  client.destroy()
    .then(() => {
      console.log('Client destroyed')
      server.close()
    })
  await request
} catch (error) {
  console.error(error)
}
```

### `Dispatcher.dispatch(options, handler)`

This is the low level API which all the preceding APIs are implemented on top of.
This API is expected to evolve through semver-major versions and is less stable than the preceding higher level APIs.
It is primarily intended for library developers who implement higher level APIs on top of this.

Arguments:

* **options** `DispatchOptions`
* **handler** `DispatchHandler`

Returns: `Boolean` - `false` if dispatcher is busy and further dispatch calls won't make any progress until the `'drain'` event has been emitted.

#### Parameter: `DispatchOptions`

* **origin** `string | URL`
* **path** `string`
* **method** `string`
* **reset** `boolean` (optional) - Default: `false` - If `false`, the request will attempt to create a long-living connection by sending the `connection: keep-alive` header,otherwise will attempt to close it immediately after response by sending `connection: close` within the request and closing the socket afterwards.
* **body** `string | Buffer | Uint8Array | stream.Readable | Iterable | AsyncIterable | null` (optional) - Default: `null`
* **headers** `UndiciHeaders` (optional) - Default: `null`.
* **query** `Record<string, any> | null` (optional) - Default: `null` - Query string params to be embedded in the request URL. Note that both keys and values of query are encoded using `encodeURIComponent`. If for some reason you need to send them unencoded, embed query params into path directly instead.
* **idempotent** `boolean` (optional) - Default: `true` if `method` is `'HEAD'` or `'GET'` - Whether the requests can be safely retried or not. If `false` the request won't be sent until all preceding requests in the pipeline has completed.
* **blocking** `boolean` (optional) - Default: `method !== 'HEAD'` - Whether the response is expected to take a long time and would end up blocking the pipeline. When this is set to `true` further pipelining will be avoided on the same connection until headers have been received.
* **upgrade** `string | null` (optional) - Default: `null` - Upgrade the request. Should be used to specify the kind of upgrade i.e. `'Websocket'`.
* **bodyTimeout** `number | null` (optional) - The timeout after which a request will time out, in milliseconds. Monitors time between receiving body data. Use `0` to disable it entirely. Defaults to 300 seconds.
* **headersTimeout** `number | null` (optional) - The amount of time, in milliseconds, the parser will wait to receive the complete HTTP headers while not sending the request. Defaults to 300 seconds.
* **expectContinue** `boolean` (optional) - Default: `false` - For H2, it appends the expect: 100-continue header, and halts the request body until a 100-continue is received from the remote server

#### Parameter: `DispatchHandler`

* **onRequestStart** `(controller: DispatchController, context: object) => void` - Invoked before request is dispatched on socket. May be invoked multiple times when a request is retried when the request at the head of the pipeline fails.
* **onRequestUpgrade** `(controller: DispatchController, statusCode: number, headers: Record<string, string | string[]>, socket: Duplex) => void` (optional) - Invoked when request is upgraded. Required if `DispatchOptions.upgrade` is defined or `DispatchOptions.method === 'CONNECT'`.
* **onResponseStart** `(controller: DispatchController, statusCode: number, headers: Record<string, string | string []>, statusMessage?: string) => void` - Invoked when statusCode and headers have been received. May be invoked multiple times due to 1xx informational headers. Not required for `upgrade` requests. Any return value is ignored.
* **onResponseData** `(controller: DispatchController, chunk: Buffer) => void` - Invoked when response payload data is received. Not required for `upgrade` requests.
* **onResponseEnd** `(controller: DispatchController, trailers: Record<string, string | string[]>) => void` - Invoked when response payload and trailers have been received and the request has completed. Not required for `upgrade` requests.
* **onResponseError** `(controller: DispatchController, error: Error) => void` - Invoked when an error has occurred. May not throw.

#### Migration from legacy handler API

If you were previously using `onConnect/onHeaders/onData/onComplete/onError`, switch to the new callbacks:

- `onConnect(abort)` → `onRequestStart(controller)` and call `controller.abort(reason)`
- `onHeaders(status, rawHeaders, resume, statusText)` → `onResponseStart(controller, status, headers, statusText)`
- `onData(chunk)` → `onResponseData(controller, chunk)`
- `onComplete(trailers)` → `onResponseEnd(controller, trailers)`
- `onError(err)` → `onResponseError(controller, err)`
- `onUpgrade(status, rawHeaders, socket)` → `onRequestUpgrade(controller, status, headers, socket)`

To access raw header arrays (for preserving duplicates/casing), read them from the controller:

- `controller.rawHeaders` for response headers
- `controller.rawTrailers` for trailers

Pause/resume now uses the controller:

- Call `controller.pause()` and `controller.resume()` instead of returning `false` from handlers.

#### Compatibility notes

Undici now stores the global dispatcher under `Symbol.for('undici.globalDispatcher.2')`.
This avoids conflicts with runtimes (such as Node.js built-in `fetch`) that still rely on the legacy dispatcher handler interface.

`setGlobalDispatcher()` also mirrors the configured dispatcher to `Symbol.for('undici.globalDispatcher.1')` using a `Dispatcher1Wrapper`, so Node's built-in `fetch` can keep using the legacy handler contract.

If you need to expose a new dispatcher/agent to legacy v1 handler consumers (`onConnect/onHeaders/onData/onComplete/onError/onUpgrade`), use `Dispatcher1Wrapper`:

```js
import { Agent, Dispatcher1Wrapper } from 'undici'

const legacyCompatibleDispatcher = new Dispatcher1Wrapper(new Agent())
```

#### Example 1 - Dispatch GET request

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  response.end('Hello, World!')
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)

const data = []

client.dispatch({
  path: '/',
  method: 'GET',
  headers: {
    'x-foo': 'bar'
  }
}, {
  onRequestStart: () => {
    console.log('Connected!')
  },
  onResponseError: (_controller, error) => {
    console.error(error)
  },
  onResponseStart: (_controller, statusCode, headers) => {
    console.log(`onResponseStart | statusCode: ${statusCode} | headers: ${JSON.stringify(headers)}`)
  },
  onResponseData: (_controller, chunk) => {
    console.log('onResponseData: chunk received')
    data.push(chunk)
  },
  onResponseEnd: (_controller, trailers) => {
    console.log(`onResponseEnd | trailers: ${JSON.stringify(trailers)}`)
    const res = Buffer.concat(data).toString('utf8')
    console.log(`Data: ${res}`)
    client.close()
    server.close()
  }
})
```

#### Example 2 - Dispatch Upgrade Request

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  response.end()
}).listen()

await once(server, 'listening')

server.on('upgrade', (request, socket, head) => {
  console.log('Node.js Server - upgrade event')
  socket.write('HTTP/1.1 101 Web Socket Protocol Handshake\r\n')
  socket.write('Upgrade: WebSocket\r\n')
  socket.write('Connection: Upgrade\r\n')
  socket.write('\r\n')
  socket.end()
})

const client = new Client(`http://localhost:${server.address().port}`)

client.dispatch({
  path: '/',
  method: 'GET',
  upgrade: 'websocket'
}, {
  onRequestStart: () => {
    console.log('Undici Client - onRequestStart')
  },
  onResponseError: () => {
    console.log('onResponseError') // shouldn't print
  },
  onRequestUpgrade: (_controller, statusCode, headers, socket) => {
    console.log('Undici Client - onRequestUpgrade')
    console.log(`onRequestUpgrade Headers: ${JSON.stringify(headers)}`)
    socket.on('data', buffer => {
      console.log(buffer.toString('utf8'))
    })
    socket.on('end', () => {
      client.close()
      server.close()
    })
    socket.end()
  }
})
```

#### Example 3 - Dispatch POST request

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  request.on('data', (data) => {
    console.log(`Request Data: ${data.toString('utf8')}`)
    const body = JSON.parse(data)
    body.message = 'World'
    response.end(JSON.stringify(body))
  })
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)

const data = []

client.dispatch({
  path: '/',
  method: 'POST',
  headers: {
    'content-type': 'application/json'
  },
  body: JSON.stringify({ message: 'Hello' })
}, {
  onRequestStart: () => {
    console.log('Connected!')
  },
  onResponseError: (_controller, error) => {
    console.error(error)
  },
  onResponseStart: (_controller, statusCode, headers) => {
    console.log(`onResponseStart | statusCode: ${statusCode} | headers: ${JSON.stringify(headers)}`)
  },
  onResponseData: (_controller, chunk) => {
    console.log('onResponseData: chunk received')
    data.push(chunk)
  },
  onResponseEnd: (_controller, trailers) => {
    console.log(`onResponseEnd | trailers: ${JSON.stringify(trailers)}`)
    const res = Buffer.concat(data).toString('utf8')
    console.log(`Response Data: ${res}`)
    client.close()
    server.close()
  }
})
```

### `Dispatcher.pipeline(options, handler)`

For easy use with [stream.pipeline](https://nodejs.org/api/stream.html#streampipelinesource-transforms-destination-options). The `handler` argument should return a `Readable` from which the result will be read. Usually it should just return the `body` argument unless some kind of transformation needs to be performed based on e.g. `headers` or `statusCode`. The `handler` should validate the response and save any required state. If there is an error, it should be thrown. The function returns a `Duplex` which writes to the request and reads from the response.

Arguments:

* **options** `PipelineOptions`
* **handler** `(data: PipelineHandlerData) => stream.Readable`

Returns: `stream.Duplex`

#### Parameter: PipelineOptions

Extends: [`RequestOptions`](/docs/docs/api/Dispatcher.md#parameter-requestoptions)

* **objectMode** `boolean` (optional) - Default: `false` - Set to `true` if the `handler` will return an object stream.

#### Parameter: PipelineHandlerData

* **statusCode** `number`
* **headers** `Record<string, string | string[] | undefined>`
* **opaque** `unknown`
* **body** `stream.Readable`
* **context** `object`
* **onInfo** `({statusCode: number, headers: Record<string, string | string[]>}) => void | null` (optional) - Default: `null` - Callback collecting all the info headers (HTTP 100-199) received.

#### Example 1 - Pipeline Echo

```js
import { Readable, Writable, PassThrough, pipeline } from 'stream'
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  request.pipe(response)
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)

let res = ''

pipeline(
  new Readable({
    read () {
      this.push(Buffer.from('undici'))
      this.push(null)
    }
  }),
  client.pipeline({
    path: '/',
    method: 'GET'
  }, ({ statusCode, headers, body }) => {
    console.log(`response received ${statusCode}`)
    console.log('headers', headers)
    return pipeline(body, new PassThrough(), () => {})
  }),
  new Writable({
    write (chunk, _, callback) {
      res += chunk.toString()
      callback()
    },
    final (callback) {
      console.log(`Response pipelined to writable: ${res}`)
      callback()
    }
  }),
  error => {
    if (error) {
      console.error(error)
    }

    client.close()
    server.close()
  }
)
```

### `Dispatcher.request(options[, callback])`

Performs a HTTP request.

Non-idempotent requests will not be pipelined in order
to avoid indirect failures.

Idempotent requests will be automatically retried if
they fail due to indirect failure from the request
at the head of the pipeline. This does not apply to
idempotent requests with a stream request body.

All response bodies must always be fully consumed or destroyed.

Arguments:

* **options** `RequestOptions`
* **callback** `(error: Error | null, data: ResponseData) => void` (optional)

Returns: `void | Promise<ResponseData>` - Only returns a `Promise` if no `callback` argument was passed.

#### Parameter: `RequestOptions`

Extends: [`DispatchOptions`](/docs/docs/api/Dispatcher.md#parameter-dispatchoptions)

* **opaque** `unknown` (optional) - Default: `null` - Used for passing through context to `ResponseData`.
* **signal** `AbortSignal | events.EventEmitter | null` (optional) - Default: `null`.
* **onInfo** `({statusCode: number, headers: Record<string, string | string[]>}) => void | null` (optional) - Default: `null` - Callback collecting all the info headers (HTTP 100-199) received.

The `RequestOptions.method` property should not be value `'CONNECT'`.

#### Parameter: `ResponseData`

* **statusCode** `number`
* **statusText** `string` - The status message from the response (e.g., "OK", "Not Found").
* **headers** `Record<string, string | string[]>` - Note that all header keys are lower-cased, e.g. `content-type`.
* **body** `stream.Readable` which also implements [the body mixin from the Fetch Standard](https://fetch.spec.whatwg.org/#body-mixin).
* **trailers** `Record<string, string>` - This object starts out
  as empty and will be mutated to contain trailers after `body` has emitted `'end'`.
* **opaque** `unknown`
* **context** `object`

`body` contains the following additional [body mixin](https://fetch.spec.whatwg.org/#body-mixin) methods and properties:

* [`.arrayBuffer()`](https://fetch.spec.whatwg.org/#dom-body-arraybuffer)
* [`.blob()`](https://fetch.spec.whatwg.org/#dom-body-blob)
* [`.bytes()`](https://fetch.spec.whatwg.org/#dom-body-bytes)
* [`.json()`](https://fetch.spec.whatwg.org/#dom-body-json)
* [`.text()`](https://fetch.spec.whatwg.org/#dom-body-text)
* `body`
* `bodyUsed`

`body` can not be consumed twice. For example, calling `text()` after `json()` throws `TypeError`.

`body` contains the following additional extensions:

- `dump({ limit: Integer })`, dump the response by reading up to `limit` bytes without killing the socket (optional) - Default: 262144.

Note that body will still be a `Readable` even if it is empty, but attempting to deserialize it with `json()` will result in an exception. Recommended way to ensure there is a body to deserialize is to check if status code is not 204, and `content-type` header starts with `application/json`.

#### Example 1 - Basic GET Request

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  response.end('Hello, World!')
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)

try {
  const { body, headers, statusCode, statusText, trailers } = await client.request({
    path: '/',
    method: 'GET'
  })
  console.log(`response received ${statusCode}`)
  console.log('headers', headers)
  body.setEncoding('utf8')
  body.on('data', console.log)
  body.on('error', console.error)
  body.on('end', () => {
    console.log('trailers', trailers)
  })

  client.close()
  server.close()
} catch (error) {
  console.error(error)
}
```

#### Example 2 - Aborting a request

> Node.js v15+ is required to run this example

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  response.end('Hello, World!')
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)
const abortController = new AbortController()

try {
  client.request({
    path: '/',
    method: 'GET',
    signal: abortController.signal
  })
} catch (error) {
  console.error(error) // should print an RequestAbortedError
  client.close()
  server.close()
}

abortController.abort()
```

Alternatively, any `EventEmitter` that emits an `'abort'` event may be used as an abort controller:

```js
import { createServer } from 'http'
import { Client } from 'undici'
import EventEmitter, { once } from 'events'

const server = createServer((request, response) => {
  response.end('Hello, World!')
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)
const ee = new EventEmitter()

try {
  client.request({
    path: '/',
    method: 'GET',
    signal: ee
  })
} catch (error) {
  console.error(error) // should print an RequestAbortedError
  client.close()
  server.close()
}

ee.emit('abort')
```

Destroying the request or response body will have the same effect.

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  response.end('Hello, World!')
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)

try {
  const { body } = await client.request({
    path: '/',
    method: 'GET'
  })
  body.destroy()
} catch (error) {
  console.error(error) // should print an RequestAbortedError
  client.close()
  server.close()
}
```

#### Example 3 - Conditionally reading the body

Remember to fully consume the body even in the case when it is not read.

```js
const { body, statusCode } = await client.request({
  path: '/',
  method: 'GET'
})

if (statusCode === 200) {
  return await body.arrayBuffer()
}

await body.dump()

return null
```

### `Dispatcher.stream(options, factory[, callback])`

A faster version of `Dispatcher.request`. This method expects the second argument `factory` to return a [`stream.Writable`](https://nodejs.org/api/stream.html#stream_class_stream_writable) stream which the response will be written to. This improves performance by avoiding creating an intermediate [`stream.Readable`](https://nodejs.org/api/stream.html#stream_readable_streams) stream when the user expects to directly pipe the response body to a [`stream.Writable`](https://nodejs.org/api/stream.html#stream_class_stream_writable) stream.

As demonstrated in [Example 1 - Basic GET stream request](/docs/docs/api/Dispatcher.md#example-1-basic-get-stream-request), it is recommended to use the `option.opaque` property to avoid creating a closure for the `factory` method. This pattern works well with Node.js Web Frameworks such as [Fastify](https://fastify.io). See [Example 2 - Stream to Fastify Response](/docs/docs/api/Dispatch.md#example-2-stream-to-fastify-response) for more details.

Arguments:

* **options** `RequestOptions`
* **factory** `(data: StreamFactoryData) => stream.Writable`
* **callback** `(error: Error | null, data: StreamData) => void` (optional)

Returns: `void | Promise<StreamData>` - Only returns a `Promise` if no `callback` argument was passed

#### Parameter: `StreamFactoryData`

* **statusCode** `number`
* **headers** `Record<string, string | string[] | undefined>`
* **opaque** `unknown`
* **onInfo** `({statusCode: number, headers: Record<string, string | string[]>}) => void | null` (optional) - Default: `null` - Callback collecting all the info headers (HTTP 100-199) received.

#### Parameter: `StreamData`

* **opaque** `unknown`
* **trailers** `Record<string, string>`
* **context** `object`

#### Example 1 - Basic GET stream request

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'
import { Writable } from 'stream'

const server = createServer((request, response) => {
  response.end('Hello, World!')
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)

const bufs = []

try {
  await client.stream({
    path: '/',
    method: 'GET',
    opaque: { bufs }
  }, ({ statusCode, headers, opaque: { bufs } }) => {
    console.log(`response received ${statusCode}`)
    console.log('headers', headers)
    return new Writable({
      write (chunk, encoding, callback) {
        bufs.push(chunk)
        callback()
      }
    })
  })

  console.log(Buffer.concat(bufs).toString('utf-8'))

  client.close()
  server.close()
} catch (error) {
  console.error(error)
}
```

#### Example 2 - Stream to Fastify Response

In this example, a (fake) request is made to the fastify server using `fastify.inject()`. This request then executes the fastify route handler which makes a subsequent request to the raw Node.js http server using `undici.dispatcher.stream()`. The fastify response is passed to the `opaque` option so that undici can tap into the underlying writable stream using `response.raw`. This methodology demonstrates how one could use undici and fastify together to create fast-as-possible requests from one backend server to another.

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'
import fastify from 'fastify'

const nodeServer = createServer((request, response) => {
  response.end('Hello, World! From Node.js HTTP Server')
}).listen()

await once(nodeServer, 'listening')

console.log('Node Server listening')

const nodeServerUndiciClient = new Client(`http://localhost:${nodeServer.address().port}`)

const fastifyServer = fastify()

fastifyServer.route({
  url: '/',
  method: 'GET',
  handler: (request, response) => {
    nodeServerUndiciClient.stream({
      path: '/',
      method: 'GET',
      opaque: response
    }, ({ opaque }) => opaque.raw)
  }
})

await fastifyServer.listen()

console.log('Fastify Server listening')

const fastifyServerUndiciClient = new Client(`http://localhost:${fastifyServer.server.address().port}`)

try {
  const { statusCode, body } = await fastifyServerUndiciClient.request({
    path: '/',
    method: 'GET'
  })

  console.log(`response received ${statusCode}`)
  body.setEncoding('utf8')
  body.on('data', console.log)

  nodeServerUndiciClient.close()
  fastifyServerUndiciClient.close()
  fastifyServer.close()
  nodeServer.close()
} catch (error) { }
```

### `Dispatcher.upgrade(options[, callback])`

Upgrade to a different protocol. Visit [MDN - HTTP - Protocol upgrade mechanism](https://developer.mozilla.org/en-US/docs/Web/HTTP/Protocol_upgrade_mechanism) for more details.

Arguments:

* **options** `UpgradeOptions`

* **callback** `(error: Error | null, data: UpgradeData) => void` (optional)

Returns: `void | Promise<UpgradeData>` - Only returns a `Promise` if no `callback` argument was passed

#### Parameter: `UpgradeOptions`

* **path** `string`
* **method** `string` (optional) - Default: `'GET'`
* **headers** `UndiciHeaders` (optional) - Default: `null`
* **protocol** `string` (optional) - Default: `'Websocket'` - A string of comma separated protocols, in descending preference order.
* **signal** `AbortSignal | EventEmitter | null` (optional) - Default: `null`

#### Parameter: `UpgradeData`

* **headers** `http.IncomingHeaders`
* **socket** `stream.Duplex`
* **opaque** `unknown`

#### Example 1 - Basic Upgrade Request

```js
import { createServer } from 'http'
import { Client } from 'undici'
import { once } from 'events'

const server = createServer((request, response) => {
  response.statusCode = 101
  response.setHeader('connection', 'upgrade')
  response.setHeader('upgrade', request.headers.upgrade)
  response.end()
}).listen()

await once(server, 'listening')

const client = new Client(`http://localhost:${server.address().port}`)

try {
  const { headers, socket } = await client.upgrade({
    path: '/',
  })
  socket.on('end', () => {
    console.log(`upgrade: ${headers.upgrade}`) // upgrade: Websocket
    client.close()
    server.close()
  })
  socket.end()
} catch (error) {
  console.error(error)
  client.close()
  server.close()
}
```

### `Dispatcher.compose(interceptors[, interceptor])`

Compose a new dispatcher from the current dispatcher and the given interceptors.

> _Notes_:
> - The order of the interceptors matters. The last interceptor will be the first to be called.
> - It is important to note that the `interceptor` function should return a function that follows the `Dispatcher.dispatch` signature.
> - Any fork of the chain of `interceptors` can lead to unexpected results.
>
> **Interceptor Stack Visualization:**
> ```
> compose([interceptor1, interceptor2, interceptor3])
>
> Request Flow:
> ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
> │   Request   │───▶│interceptor3 │───▶│interceptor2 │───▶│interceptor1 │───▶│  dispatcher │
> └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    │   .dispatch │
>                           ▲                   ▲                   ▲         └─────────────┘
>                           │                   │                   │                ▲
>                    (called first)      (called second)     (called last)           │
>                                                                                    │
> ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
> │  Response   │◀───│interceptor3 │◀───│interceptor2 │◀───│interceptor1 │◀─────────┘
> └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
>
> The interceptors are composed in reverse order due to function composition.
> ```

Arguments:

* **interceptors** `Interceptor[interceptor[]]`: It is an array of `Interceptor` functions passed as only argument, or several interceptors passed as separate arguments.

Returns: `Dispatcher`.

#### Parameter: `Interceptor`

A function that takes a `dispatch` method and returns a `dispatch`-like function.

#### Example 1 - Basic Compose

```js
const { Client, RedirectHandler } = require('undici')

const redirectInterceptor = dispatch => {
    return (opts, handler) => {
      const { maxRedirections } = opts

      if (!maxRedirections) {
        return dispatch(opts, handler)
      }

      const redirectHandler = new RedirectHandler(
        dispatch,
        maxRedirections,
        opts,
        handler
      )
      opts = { ...opts, maxRedirections: 0 } // Stop sub dispatcher from also redirecting.
      return dispatch(opts, redirectHandler)
    }
}

const client = new Client('http://localhost:3000')
  .compose(redirectInterceptor)

await client.request({ path: '/', method: 'GET' })
```

#### Example 2 - Chained Compose

```js
const { Client, RedirectHandler, RetryHandler } = require('undici')

const redirectInterceptor = dispatch => {
    return (opts, handler) => {
      const { maxRedirections } = opts

      if (!maxRedirections) {
        return dispatch(opts, handler)
      }

      const redirectHandler = new RedirectHandler(
        dispatch,
        maxRedirections,
        opts,
        handler
      )
      opts = { ...opts, maxRedirections: 0 }
      return dispatch(opts, redirectHandler)
    }
}

const retryInterceptor = dispatch => {
  return function retryInterceptor (opts, handler) {
    return dispatch(
      opts,
      new RetryHandler(opts, {
        handler,
        dispatch
      })
    )
  }
}

const client = new Client('http://localhost:3000')
  .compose(redirectInterceptor)
  .compose(retryInterceptor)

await client.request({ path: '/', method: 'GET' })
```

#### Pre-built interceptors

##### `redirect`

The `redirect` interceptor allows you to customize the way your dispatcher handles redirects.

It accepts the same arguments as the [`RedirectHandler` constructor](/docs/docs/api/RedirectHandler.md).

**Example - Basic Redirect Interceptor**

```js
const { Client, interceptors } = require("undici");
const { redirect } = interceptors;

const client = new Client("http://service.example").compose(
  redirect({ maxRedirections: 3, throwOnMaxRedirect: true })
);
client.request({ path: "/" })
```

##### `retry`

The `retry` interceptor allows you to customize the way your dispatcher handles retries.

It accepts the same arguments as the [`RetryHandler` constructor](/docs/docs/api/RetryHandler.md).

**Example - Basic Redirect Interceptor**

```js
const { Client, interceptors } = require("undici");
const { retry } = interceptors;

const client = new Client("http://service.example").compose(
  retry({
    maxRetries: 3,
    minTimeout: 1000,
    maxTimeout: 10000,
    timeoutFactor: 2,
    retryAfter: true,
  })
);
```

##### `dump`

The `dump` interceptor enables you to dump the response body from a request upon a given limit.

**Options**
- `maxSize` - The maximum size (in bytes) of the response body to dump. If the size of the request's body exceeds this value then the connection will be closed. Default: `1048576`.

> The `Dispatcher#options` also gets extended with the options `dumpMaxSize`, `abortOnDumped`, and `waitForTrailers` which can be used to configure the interceptor at a request-per-request basis.

**Example - Basic Dump Interceptor**

```js
const { Client, interceptors } = require("undici");
const { dump } = interceptors;

const client = new Client("http://service.example").compose(
  dump({
    maxSize: 1024,
  })
);

// or
client.dispatch(
  {
    path: "/",
    method: "GET",
    dumpMaxSize: 1024,
  },
  handler
);
```

##### `dns`

The `dns` interceptor enables you to cache DNS lookups for a given duration, per origin.

>It is well suited for scenarios where you want to cache DNS lookups to avoid the overhead of resolving the same domain multiple times

**Options**
- `maxTTL` - The maximum time-to-live (in milliseconds) of the DNS cache. It should be a positive integer. Default: `10000`.
  - Set `0` to disable TTL.
- `maxItems` - The maximum number of items to cache. It should be a positive integer. Default: `Infinity`.
- `dualStack` - Whether to resolve both IPv4 and IPv6 addresses. Default: `true`.
  - It will also attempt a happy-eyeballs-like approach to connect to the available addresses in case of a connection failure.
- `affinity` - Whether to use IPv4 or IPv6 addresses. Default: `4`.
  - It can be either `4` or `6`.
  - It will only take effect if `dualStack` is `false`.
- `lookup: (hostname: string, options: LookupOptions, callback: (err: NodeJS.ErrnoException | null, addresses: DNSInterceptorRecord[]) => void) => void` - Custom lookup function. Default: `dns.lookup`.
  - For more info see [dns.lookup](https://nodejs.org/api/dns.html#dnslookuphostname-options-callback).
- `pick: (origin: URL, records: DNSInterceptorRecords, affinity: 4 | 6) => DNSInterceptorRecord` - Custom pick function. Default: `RoundRobin`.
  - The function should return a single record from the records array.
  - By default a simplified version of Round Robin is used.
  - The `records` property can be mutated to store the state of the balancing algorithm.
- `storage: DNSStorage` - Custom storage for resolved DNS records

> The `Dispatcher#options` also gets extended with the options `dns.affinity`, `dns.dualStack`, `dns.lookup` and `dns.pick` which can be used to configure the interceptor at a request-per-request basis.


**DNSInterceptorRecord**
It represents a DNS record.
- `family` - (`number`) The IP family of the address. It can be either `4` or `6`.
- `address` - (`string`) The IP address.

**DNSInterceptorOriginRecords**
It represents a map of DNS IP addresses records for a single origin.
- `4.ips` - (`DNSInterceptorRecord[] | null`) The IPv4 addresses.
- `6.ips` - (`DNSInterceptorRecord[] | null`) The IPv6 addresses.

**DNSStorage**
It represents a storage object for resolved DNS records.
- `size` - (`number`) current size of the storage.
- `get` - (`(origin: string) => DNSInterceptorOriginRecords | null`) method to get the records for a given origin.
- `set` - (`(origin: string, records: DNSInterceptorOriginRecords | null, options: { ttl: number }) => void`) method to set the records for a given origin.
- `delete` - (`(origin: string) => void`) method to delete records for a given origin.
- `full` - (`() => boolean`) method to check if the storage is full, if returns `true`, DNS lookup will be skipped in this interceptor and new records will not be stored.

**Example - Basic DNS Interceptor**

```js
const { Client, interceptors } = require("undici");
const { dns } = interceptors;

const client = new Agent().compose([
  dns({ ...opts })
])

const response = await client.request({
  origin: `http://localhost:3030`,
  ...requestOpts
})
```

**Example - DNS Interceptor and LRU cache as a storage**

```js
const { Client, interceptors } = require("undici");
const QuickLRU = require("quick-lru");
const { dns } = interceptors;

const lru = new QuickLRU({ maxSize: 100 });

const lruAdapter = {
  get size() {
    return lru.size;
  },
  get(origin) {
    return lru.get(origin);
  },
  set(origin, records, { ttl }) {
    lru.set(origin, records, { maxAge: ttl });
  },
  delete(origin) {
    lru.delete(origin);
  },
  full() {
    // For LRU cache, we can always store new records,
    // old records will be evicted automatically
    return false;
  }
}

const client = new Agent().compose([
  dns({ storage: lruAdapter })
])

const response = await client.request({
  origin: `http://localhost:3030`,
  ...requestOpts
})
```

##### `responseError`

The `responseError` interceptor throws an error for responses with status code errors (>= 400).

**Example**

```js
const { Client, interceptors } = require("undici");
const { responseError } = interceptors;

const client = new Client("http://service.example").compose(
  responseError()
);

// Will throw a ResponseError for status codes >= 400
await client.request({
  method: "GET",
  path: "/"
});
```

##### `decompress`

⚠️ The decompress interceptor is experimental and subject to change.

The `decompress` interceptor automatically decompresses response bodies that are compressed with gzip, deflate, brotli, or zstd compression. It removes the `content-encoding` and `content-length` headers from decompressed responses and supports RFC-9110 compliant multiple encodings.

**Options**

- `skipErrorResponses` - Whether to skip decompression for error responses (status codes >= 400). Default: `true`.
- `skipStatusCodes` - Array of status codes to skip decompression for. Default: `[204, 304]`.

**Example - Basic Decompress Interceptor**

```js
const { Client, interceptors } = require("undici");
const { decompress } = interceptors;

const client = new Client("http://service.example").compose(
  decompress()
);

// Automatically decompresses gzip/deflate/brotli/zstd responses
const response = await client.request({
  method: "GET",
  path: "/"
});
```

**Example - Custom Options**

```js
const { Client, interceptors } = require("undici");
const { decompress } = interceptors;

const client = new Client("http://service.example").compose(
  decompress({
    skipErrorResponses: false, // Decompress 5xx responses
    skipStatusCodes: [204, 304, 201] // Skip these status codes
  })
);
```

**Supported Encodings**

- `gzip` / `x-gzip` - GZIP compression
- `deflate` / `x-compress` - DEFLATE compression  
- `br` - Brotli compression
- `zstd` - Zstandard compression
- Multiple encodings (e.g., `gzip, deflate`) are supported per RFC-9110

**Behavior**

- Skips decompression for status codes < 200 or >= 400 (configurable)
- Skips decompression for 204 No Content and 304 Not Modified by default
- Removes `content-encoding` and `content-length` headers when decompressing
- Passes through unsupported encodings unchanged
- Handles case-insensitive encoding names
- Supports streaming decompression without buffering

##### `Cache Interceptor`

The `cache` interceptor implements client-side response caching as described in
[RFC9111](https://www.rfc-editor.org/rfc/rfc9111.html).

**Options**

- `methods` - The [**safe** HTTP methods](https://www.rfc-editor.org/rfc/rfc9110#section-9.2.1) to cache the response of.
- `cacheByDefault` - The default expiration time to cache responses by if they don't have an explicit expiration and cannot have an heuristic expiry computed. If this isn't present, responses neither with an explicit expiration nor heuristically cacheable will not be cached. Default `undefined`.
- `type` - The [type of cache](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching#types_of_caches) for Undici to act as. Can be `shared` or `private`. Default `shared`. `private` implies privately cacheable responses will be cached and potentially shared with other users of your application.

**Usage with `fetch`**

```js
const { Agent, cacheStores, interceptors, setGlobalDispatcher } = require('undici')

const client = new Agent().compose(interceptors.cache({
  store: new cacheStores.MemoryCacheStore({
    maxSize: 100 * 1024 * 1024, // 100MB
    maxCount: 1000,
    maxEntrySize: 5 * 1024 * 1024 // 5MB
  })
}))

setGlobalDispatcher(client)

// First request goes to the network and is cached when cache headers allow it.
const first = await fetch('https://example.com/data')

// Second request can be served from cache according to RFC9111 rules.
const second = await fetch('https://example.com/data')
```

##### `Deduplicate Interceptor`

The `deduplicate` interceptor deduplicates concurrent identical requests. When multiple identical requests are made while one is already in-flight, only one request is sent to the origin server, and all waiting handlers receive the same response. This reduces server load and improves performance.

**Options**

- `methods` - The [**safe** HTTP methods](https://www.rfc-editor.org/rfc/rfc9110#section-9.2.1) to deduplicate. Default `['GET']`.
- `skipHeaderNames` - Header names that, if present in a request, will cause the request to skip deduplication entirely. Useful for headers like `idempotency-key` where presence indicates unique processing. Header name matching is case-insensitive. Default `[]`.
- `excludeHeaderNames` - Header names to exclude from the deduplication key. Requests with different values for these headers will still be deduplicated together. Useful for headers like `x-request-id` that vary per request but shouldn't affect deduplication. Header name matching is case-insensitive. Default `[]`.
- `maxBufferSize` - Maximum bytes buffered per paused waiting deduplicated handler. If a waiting handler remains paused and exceeds this threshold, it is failed with an abort error to prevent unbounded memory growth. Default `5 * 1024 * 1024`.

**Usage**

```js
const { Client, interceptors } = require("undici");
const { deduplicate, cache } = interceptors;

// Deduplicate only
const client = new Client("http://service.example").compose(
  deduplicate()
);

// Deduplicate with caching
const clientWithCache = new Client("http://service.example").compose(
  deduplicate(),
  cache()
);
```

Requests are considered identical if they have the same:
- Origin
- HTTP method
- Path
- Request headers (excluding any headers specified in `excludeHeaderNames`)

All deduplicated requests receive the complete response including status code, headers, and body.

For observability, request deduplication events are published to the `undici:request:pending-requests` [diagnostic channel](/docs/docs/api/DiagnosticsChannel.md#undicirequestpending-requests).

## Instance Events

### Event: `'connect'`

Parameters:

* **origin** `URL`
* **targets** `Array<Dispatcher>`

### Event: `'disconnect'`

Parameters:

* **origin** `URL`
* **targets** `Array<Dispatcher>`
* **error** `Error`

Emitted when the dispatcher has been disconnected from the origin.

> **Note**: For HTTP/2, this event is also emitted when the dispatcher has received the [GOAWAY Frame](https://webconcepts.info/concepts/http2-frame-type/0x7) with an Error with the message `HTTP/2: "GOAWAY" frame received` and the code `UND_ERR_INFO`.
> Due to nature of the protocol of using binary frames, it is possible that requests gets hanging as a frame can be received between the `HEADER` and `DATA` frames.
> It is recommended to handle this event and close the dispatcher to create a new HTTP/2 session.

### Event: `'connectionError'`

Parameters:

* **origin** `URL`
* **targets** `Array<Dispatcher>`
* **error** `Error`

Emitted when dispatcher fails to connect to
origin.

### Event: `'drain'`

Parameters:

* **origin** `URL`

Emitted when dispatcher is no longer busy.

## Parameter: `UndiciHeaders`

* `Record<string, string | string[] | undefined> | string[] | Iterable<[string, string | string[] | undefined]> | null`

Header arguments such as `options.headers` in [`Client.dispatch`](/docs/docs/api/Client.md#clientdispatchoptions-handlers) can be specified in three forms:
* As an object specified by the `Record<string, string | string[] | undefined>` (`IncomingHttpHeaders`) type.
* As an array of strings. An array representation of a header list must have an even length, or an `InvalidArgumentError` will be thrown.
* As an iterable that can encompass `Headers`, `Map`, or a custom iterator returning key-value pairs.
Keys are lowercase and values are not modified.

Undici validates header syntax at the protocol level (for example, invalid header names and invalid control characters in string values), but it does not sanitize untrusted application input. Validate and sanitize any user-provided header names and values before passing them to Undici to prevent header/body injection vulnerabilities.

When using the array header format (`string[]`), Undici processes only indexed elements. Additional properties assigned to the array object are ignored.

Response headers will derive a `host` from the `url` of the [Client](/docs/docs/api/Client.md#class-client) instance if no `host` header was previously specified.

### Example 1 - Object

```js
{
  'content-length': '123',
  'content-type': 'text/plain',
  connection: 'keep-alive',
  host: 'mysite.com',
  accept: '*/*'
}
```

### Example 2 - Array

```js
[
  'content-length', '123',
  'content-type', 'text/plain',
  'connection', 'keep-alive',
  'host', 'mysite.com',
  'accept', '*/*'
]
```

### Example 3 - Iterable

```js
new Headers({
  'content-length': '123',
  'content-type': 'text/plain',
  connection: 'keep-alive',
  host: 'mysite.com',
  accept: '*/*'
})
```
or
```js
new Map([
  ['content-length', '123'],
  ['content-type', 'text/plain'],
  ['connection', 'keep-alive'],
  ['host', 'mysite.com'],
  ['accept', '*/*']
])
```
or
```js
{
  *[Symbol.iterator] () {
    yield ['content-length', '123']
    yield ['content-type', 'text/plain']
    yield ['connection', 'keep-alive']
    yield ['host', 'mysite.com']
    yield ['accept', '*/*']
  }
}
```

```

## File: durable_exec.md
```
# `pydantic_ai.durable_exec`

::: pydantic_ai.durable_exec.temporal

::: pydantic_ai.durable_exec.dbos

::: pydantic_ai.durable_exec.prefect

```

## File: embeddings.md
```
# `pydantic_ai.embeddings`

::: pydantic_ai.embeddings

::: pydantic_ai.embeddings.base

::: pydantic_ai.embeddings.result

::: pydantic_ai.embeddings.settings

::: pydantic_ai.embeddings.openai

::: pydantic_ai.embeddings.cohere

::: pydantic_ai.embeddings.google

::: pydantic_ai.embeddings.bedrock

::: pydantic_ai.embeddings.voyageai

::: pydantic_ai.embeddings.sentence_transformers

::: pydantic_ai.embeddings.test

::: pydantic_ai.embeddings.wrapper

::: pydantic_ai.embeddings.instrumented

```

## File: envhttpproxyagent.md
```
# Class: EnvHttpProxyAgent

Extends: `undici.Dispatcher`

EnvHttpProxyAgent automatically reads the proxy configuration from the environment variables `http_proxy`, `https_proxy`, and `no_proxy` and sets up the proxy agents accordingly. When `http_proxy` and `https_proxy` are set, `http_proxy` is used for HTTP requests and `https_proxy` is used for HTTPS requests. If only `http_proxy` is set, `http_proxy` is used for both HTTP and HTTPS requests. If only `https_proxy` is set, it is only used for HTTPS requests.

`no_proxy` is a comma or space-separated list of hostnames that should not be proxied. The list may contain leading wildcard characters (`*`). If `no_proxy` is set, the EnvHttpProxyAgent will bypass the proxy for requests to hosts that match the list. If `no_proxy` is set to `"*"`, the EnvHttpProxyAgent will bypass the proxy for all requests.

Uppercase environment variables are also supported: `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY`. However, if both the lowercase and uppercase environment variables are set, the uppercase environment variables will be ignored.

## `new EnvHttpProxyAgent([options])`

Arguments:

* **options** `EnvHttpProxyAgentOptions` (optional) - extends the `Agent` options.

Returns: `EnvHttpProxyAgent`

### Parameter: `EnvHttpProxyAgentOptions`

Extends: [`AgentOptions`](/docs/docs/api/Agent.md#parameter-agentoptions)

* **httpProxy** `string` (optional) - When set, it will override the `HTTP_PROXY` environment variable.
* **httpsProxy** `string` (optional) - When set, it will override the `HTTPS_PROXY` environment variable.
* **noProxy** `string` (optional) - When set, it will override the `NO_PROXY` environment variable.

Examples:

```js
import { EnvHttpProxyAgent } from 'undici'

const envHttpProxyAgent = new EnvHttpProxyAgent()
// or
const envHttpProxyAgent = new EnvHttpProxyAgent({ httpProxy: 'my.proxy.server:8080', httpsProxy: 'my.proxy.server:8443', noProxy: 'localhost' })
```

#### Example - EnvHttpProxyAgent instantiation

This will instantiate the EnvHttpProxyAgent. It will not do anything until registered as the agent to use with requests.

```js
import { EnvHttpProxyAgent } from 'undici'

const envHttpProxyAgent = new EnvHttpProxyAgent()
```

#### Example - Basic Proxy Fetch with global agent dispatcher

```js
import { setGlobalDispatcher, fetch, EnvHttpProxyAgent } from 'undici'

const envHttpProxyAgent = new EnvHttpProxyAgent()
setGlobalDispatcher(envHttpProxyAgent)

const { status, json } = await fetch('http://localhost:3000/foo')

console.log('response received', status) // response received 200

const data = await json() // data { foo: "bar" }
```

#### Example - Basic Proxy Request with global agent dispatcher

```js
import { setGlobalDispatcher, request, EnvHttpProxyAgent } from 'undici'

const envHttpProxyAgent = new EnvHttpProxyAgent()
setGlobalDispatcher(envHttpProxyAgent)

const { statusCode, body } = await request('http://localhost:3000/foo')

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - Basic Proxy Request with local agent dispatcher

```js
import { EnvHttpProxyAgent, request } from 'undici'

const envHttpProxyAgent = new EnvHttpProxyAgent()

const {
  statusCode,
  body
} = await request('http://localhost:3000/foo', { dispatcher: envHttpProxyAgent })

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - Basic Proxy Fetch with local agent dispatcher

```js
import { EnvHttpProxyAgent, fetch } from 'undici'

const envHttpProxyAgent = new EnvHttpProxyAgent()

const {
  status,
  json
} = await fetch('http://localhost:3000/foo', { dispatcher: envHttpProxyAgent })

console.log('response received', status) // response received 200

const data = await json() // data { foo: "bar" }
```

## Instance Methods

### `EnvHttpProxyAgent.close([callback])`

Implements [`Dispatcher.close([callback])`](/docs/docs/api/Dispatcher.md#dispatcherclosecallback-promise).

### `EnvHttpProxyAgent.destroy([error, callback])`

Implements [`Dispatcher.destroy([error, callback])`](/docs/docs/api/Dispatcher.md#dispatcherdestroyerror-callback-promise).

### `EnvHttpProxyAgent.dispatch(options, handler: AgentDispatchOptions)`

Implements [`Dispatcher.dispatch(options, handler)`](/docs/docs/api/Dispatcher.md#dispatcherdispatchoptions-handler).

#### Parameter: `AgentDispatchOptions`

Extends: [`DispatchOptions`](/docs/docs/api/Dispatcher.md#parameter-dispatchoptions)

* **origin** `string | URL`

Implements [`Dispatcher.destroy([error, callback])`](/docs/docs/api/Dispatcher.md#dispatcherdestroyerror-callback-promise).

### `EnvHttpProxyAgent.connect(options[, callback])`

See [`Dispatcher.connect(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherconnectoptions-callback).

### `EnvHttpProxyAgent.dispatch(options, handler)`

Implements [`Dispatcher.dispatch(options, handler)`](/docs/docs/api/Dispatcher.md#dispatcherdispatchoptions-handler).

### `EnvHttpProxyAgent.pipeline(options, handler)`

See [`Dispatcher.pipeline(options, handler)`](/docs/docs/api/Dispatcher.md#dispatcherpipelineoptions-handler).

### `EnvHttpProxyAgent.request(options[, callback])`

See [`Dispatcher.request(options [, callback])`](/docs/docs/api/Dispatcher.md#dispatcherrequestoptions-callback).

### `EnvHttpProxyAgent.stream(options, factory[, callback])`

See [`Dispatcher.stream(options, factory[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherstreamoptions-factory-callback).

### `EnvHttpProxyAgent.upgrade(options[, callback])`

See [`Dispatcher.upgrade(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherupgradeoptions-callback).

```

## File: errors.md
```
# Errors

Undici exposes a variety of error objects that you can use to enhance your error handling.
You can find all the error objects inside the `errors` key.

```js
import { errors } from 'undici'
```

| Error                                | Error Codes                           | Description                                                               |
| ------------------------------------ | ------------------------------------- | ------------------------------------------------------------------------- |
| `UndiciError`                        | `UND_ERR`                             | all errors below are extended from `UndiciError`.                         |
| `ConnectTimeoutError`                | `UND_ERR_CONNECT_TIMEOUT`             | socket is destroyed due to connect timeout.                               |
| `HeadersTimeoutError`                | `UND_ERR_HEADERS_TIMEOUT`             | socket is destroyed due to headers timeout.                               |
| `HeadersOverflowError`               | `UND_ERR_HEADERS_OVERFLOW`            | socket is destroyed due to headers' max size being exceeded.              |
| `BodyTimeoutError`                   | `UND_ERR_BODY_TIMEOUT`                | socket is destroyed due to body timeout.                                  |
| `InvalidArgumentError`               | `UND_ERR_INVALID_ARG`                 | passed an invalid argument.                                               |
| `InvalidReturnValueError`            | `UND_ERR_INVALID_RETURN_VALUE`        | returned an invalid value.                                                |
| `RequestAbortedError`                | `UND_ERR_ABORTED`                     | the request has been aborted by the user                                  |
| `ClientDestroyedError`               | `UND_ERR_DESTROYED`                   | trying to use a destroyed client.                                         |
| `ClientClosedError`                  | `UND_ERR_CLOSED`                      | trying to use a closed client.                                            |
| `SocketError`                        | `UND_ERR_SOCKET`                      | there is an error with the socket.                                        |
| `NotSupportedError`                  | `UND_ERR_NOT_SUPPORTED`               | encountered unsupported functionality.                                    |
| `RequestContentLengthMismatchError`  | `UND_ERR_REQ_CONTENT_LENGTH_MISMATCH` | request body does not match content-length header                         |
| `ResponseContentLengthMismatchError` | `UND_ERR_RES_CONTENT_LENGTH_MISMATCH` | response body does not match content-length header                        |
| `InformationalError`                 | `UND_ERR_INFO`                        | expected error with reason                                                |
| `ResponseExceededMaxSizeError`       | `UND_ERR_RES_EXCEEDED_MAX_SIZE`       | response body exceed the max size allowed                                 |
| `SecureProxyConnectionError`         | `UND_ERR_PRX_TLS`                     | tls connection to a proxy failed                                          |
| `MessageSizeExceededError`           | `UND_ERR_WS_MESSAGE_SIZE_EXCEEDED`    | WebSocket decompressed message exceeded the maximum allowed size          |

Be aware of the possible difference between the global dispatcher version and the actual undici version you might be using. We recommend to avoid the check `instanceof errors.UndiciError` and seek for the `error.code === '<error_code>'` instead to avoid inconsistencies.
### `SocketError`

The `SocketError` has a `.socket` property which holds socket metadata:

```ts
interface SocketInfo {
  localAddress?: string
  localPort?: number
  remoteAddress?: string
  remotePort?: number
  remoteFamily?: string
  timeout?: number
  bytesWritten?: number
  bytesRead?: number
}
```

Be aware that in some cases the `.socket` property can be `null`.

```

## File: eventsource.md
```
# EventSource

> ⚠️ Warning: the EventSource API is experimental.

Undici exposes a WHATWG spec-compliant implementation of [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource)
for [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events).

## Instantiating EventSource

Undici exports a EventSource class. You can instantiate the EventSource as
follows:

```mjs
import { EventSource } from 'undici'

const eventSource = new EventSource('http://localhost:3000')
eventSource.onmessage = (event) => {
  console.log(event.data)
}
```

## Using a custom Dispatcher

undici allows you to set your own Dispatcher in the EventSource constructor.

An example which allows you to modify the request headers is:

```mjs
import { EventSource, Agent } from 'undici'

class CustomHeaderAgent extends Agent {
  dispatch (opts) {
    opts.headers['x-custom-header'] = 'hello world'
    return super.dispatch(...arguments)
  }
}

const eventSource = new EventSource('http://localhost:3000', {
  dispatcher: new CustomHeaderAgent()
})

```

More information about the EventSource API can be found on
[MDN](https://developer.mozilla.org/en-US/docs/Web/API/EventSource).

```

## File: exceptions.md
```
# `pydantic_ai.exceptions`

::: pydantic_ai.exceptions

```

## File: ext.md
```
# `pydantic_ai.ext`

::: pydantic_ai.ext.langchain

::: pydantic_ai.ext.aci

```

## File: fasta2a.md
```
# `fasta2a`

::: fasta2a

::: fasta2a.schema

::: fasta2a.client

```

## File: fetch.md
```
# Fetch

Undici exposes a fetch() method starts the process of fetching a resource from the network.

Documentation and examples can be found on [MDN](https://developer.mozilla.org/en-US/docs/Web/API/fetch).

## FormData

This API is implemented as per the standard, you can find documentation on [MDN](https://developer.mozilla.org/en-US/docs/Web/API/FormData).

If any parameters are passed to the FormData constructor other than `undefined`, an error will be thrown. Other parameters are ignored.

When you use `FormData` as a request body, keep `fetch` and `FormData` from the
same implementation. Use the built-in global `FormData` with the built-in
global `fetch()`, and use `undici`'s `FormData` with `undici.fetch()`.

If you want the installed `undici` package to provide the globals, call
[`install()`](/docs/api/GlobalInstallation.md) so `fetch`, `Headers`,
`Response`, `Request`, and `FormData` are installed together as a matching set.

## Response

This API is implemented as per the standard, you can find documentation on [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Response)

## Request

This API is implemented as per the standard, you can find documentation on [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Request)

## Header

This API is implemented as per the standard, you can find documentation on [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Headers)

# Body Mixins

`Response` and `Request` body inherit body mixin methods. These methods include:

- [`.arrayBuffer()`](https://fetch.spec.whatwg.org/#dom-body-arraybuffer)
- [`.blob()`](https://fetch.spec.whatwg.org/#dom-body-blob)
- [`.bytes()`](https://fetch.spec.whatwg.org/#dom-body-bytes)
- [`.formData()`](https://fetch.spec.whatwg.org/#dom-body-formdata)
- [`.json()`](https://fetch.spec.whatwg.org/#dom-body-json)
- [`.text()`](https://fetch.spec.whatwg.org/#dom-body-text)

There is an ongoing discussion regarding `.formData()` and its usefulness and performance in server environments. It is recommended to use a dedicated library for parsing `multipart/form-data` bodies, such as [Busboy](https://www.npmjs.com/package/busboy) or [@fastify/busboy](https://www.npmjs.com/package/@fastify/busboy).

These libraries can be interfaced with fetch with the following example code:

```mjs
import { Busboy } from '@fastify/busboy'
import { Readable } from 'node:stream'

const response = await fetch('...')
const busboy = new Busboy({
  headers: {
    'content-type': response.headers.get('content-type')
  }
})

Readable.fromWeb(response.body).pipe(busboy)
```

```

## File: format_prompt.md
```
# `pydantic_ai.format_prompt`

::: pydantic_ai.format_prompt
    options:
        members:
            - format_as_xml

```

## File: function_signature.md
```
# `pydantic_ai.function_signature`

::: pydantic_ai.function_signature

```

## File: globalinstallation.md
```
# Global Installation

Undici provides an `install()` function to add all WHATWG fetch classes to `globalThis`, making them available globally without requiring imports.

## `install()`

Install all WHATWG fetch classes globally on `globalThis`.

**Example:**

```js
import { install } from 'undici'

// Install all WHATWG fetch classes globally  
install()

// Now you can use fetch classes globally without importing
const response = await fetch('https://api.example.com/data')
const data = await response.json()

// All classes are available globally:
const headers = new Headers([['content-type', 'application/json']])
const request = new Request('https://example.com')
const formData = new FormData()
const ws = new WebSocket('wss://example.com')
const eventSource = new EventSource('https://example.com/events')
```

## Installed Classes

The `install()` function adds the following classes to `globalThis`:

| Class | Description |
|-------|-------------|
| `fetch` | The fetch function for making HTTP requests |
| `Headers` | HTTP headers management |
| `Response` | HTTP response representation |
| `Request` | HTTP request representation |
| `FormData` | Form data handling |
| `WebSocket` | WebSocket client |
| `CloseEvent` | WebSocket close event |
| `ErrorEvent` | WebSocket error event |
| `MessageEvent` | WebSocket message event |
| `EventSource` | Server-sent events client |

## Using `FormData` with `fetch`

If you send a `FormData` body, use matching implementations for `fetch` and
`FormData`.

These two patterns are safe:

```js
// Built-in globals from Node.js
const body = new FormData()
await fetch('https://example.com', {
  method: 'POST',
  body
})
```

```js
// Globals installed from the undici package
import { install } from 'undici'

install()

const body = new FormData()
await fetch('https://example.com', {
  method: 'POST',
  body
})
```

After `install()`, `fetch`, `Headers`, `Response`, `Request`, and `FormData`
all come from the installed `undici` package, so they work as a matching set.

If you do not want to install globals, import both from `undici` instead:

```js
import { fetch, FormData } from 'undici'

const body = new FormData()
await fetch('https://example.com', {
  method: 'POST',
  body
})
```

Avoid mixing a global `FormData` with `undici.fetch()`, or `undici.FormData`
with the built-in global `fetch()`. Keeping them paired avoids surprising
multipart behavior across Node.js and undici versions.

## Use Cases

Global installation is useful for:

- **Polyfilling environments** that don't have native fetch support
- **Ensuring consistent behavior** across different Node.js versions
- **Library compatibility** when third-party libraries expect global fetch
- **Migration scenarios** where you want to replace built-in implementations
- **Testing environments** where you need predictable fetch behavior

## Example: Polyfilling an Environment

```js
import { install } from 'undici'

// Check if fetch is available and install if needed
if (typeof globalThis.fetch === 'undefined') {
  install()
  console.log('Undici fetch installed globally')
}

// Now fetch is guaranteed to be available
const response = await fetch('https://api.example.com')
```

## Example: Testing Environment

```js
import { install } from 'undici'

// In test setup, ensure consistent fetch behavior
install()

// Now all tests use undici's implementations
test('fetch API test', async () => {
  const response = await fetch('https://example.com')
  expect(response).toBeInstanceOf(Response)
})
```

## Notes

- The `install()` function overwrites any existing global implementations
- Classes installed are undici's implementations, not Node.js built-ins
- This provides access to undici's latest features and performance improvements
- The global installation persists for the lifetime of the process
```

## File: h2cclient.md
```
# Class: H2CClient

Extends: `undici.Dispatcher`

A basic H2C client.

**Example**

```js
const { createServer } = require('node:http2')
const { once } = require('node:events')
const { H2CClient } = require('undici')

const server = createServer((req, res) => {
  res.writeHead(200)
  res.end('Hello, world!')
})

server.listen()
once(server, 'listening').then(() => {
  const client = new H2CClient(`http://localhost:${server.address().port}/`)

  const response = await client.request({ path: '/', method: 'GET' })
  console.log(response.statusCode) // 200
  response.body.text.then((text) => {
    console.log(text) // Hello, world!
  })
})
```

## `new H2CClient(url[, options])`

Arguments:

- **url** `URL | string` - Should only include the **protocol, hostname, and port**. It only supports `http` protocol.
- **options** `H2CClientOptions` (optional)

Returns: `H2CClient`

### Parameter: `H2CClientOptions`

- **bodyTimeout** `number | null` (optional) - Default: `300e3` - The timeout after which a request will time out, in milliseconds. Monitors time between receiving body data. Use `0` to disable it entirely. Defaults to 300 seconds. Please note the `timeout` will be reset if you keep writing data to the socket everytime.
- **headersTimeout** `number | null` (optional) - Default: `300e3` - The amount of time, in milliseconds, the parser will wait to receive the complete HTTP headers while not sending the request. Defaults to 300 seconds.
- **keepAliveMaxTimeout** `number | null` (optional) - Default: `600e3` - The maximum allowed `keepAliveTimeout`, in milliseconds, when overridden by _keep-alive_ hints from the server. Defaults to 10 minutes.
- **keepAliveTimeout** `number | null` (optional) - Default: `4e3` - The timeout, in milliseconds, after which a socket without active requests will time out. Monitors time between activity on a connected socket. This value may be overridden by _keep-alive_ hints from the server. See [MDN: HTTP - Headers - Keep-Alive directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Keep-Alive#directives) for more details. Defaults to 4 seconds.
- **keepAliveTimeoutThreshold** `number | null` (optional) - Default: `2e3` - A number of milliseconds subtracted from server _keep-alive_ hints when overriding `keepAliveTimeout` to account for timing inaccuracies caused by e.g. transport latency. Defaults to 2 seconds.
- **maxHeaderSize** `number | null` (optional) - Default: `--max-http-header-size` or `16384` - The maximum length of request headers in bytes. Defaults to Node.js' --max-http-header-size or 16KiB.
- **maxResponseSize** `number | null` (optional) - Default: `-1` - The maximum length of response body in bytes. Set to `-1` to disable.
- **maxConcurrentStreams**: `number` - Default: `100`. Dictates the maximum number of concurrent streams for a single H2 session. It can be overridden by a SETTINGS remote frame.
- **pipelining** `number | null` (optional) - Default to `maxConcurrentStreams` - The amount of concurrent requests sent over a single HTTP/2 session in accordance with [RFC-7540](https://httpwg.org/specs/rfc7540.html#StreamsLayer) Stream specification. Streams can be closed up by remote server at any time.
- **pingInterval**: `number` - Default: `60e3`. The time interval in milliseconds between PING frames sent to the server. Set to `0` to disable PING frames. This is only applicable for HTTP/2 connections.
- **connect** `ConnectOptions | null` (optional) - Default: `null`.
- **strictContentLength** `Boolean` (optional) - Default: `true` - Whether to treat request content length mismatches as errors. If true, an error is thrown when the request content-length header doesn't match the length of the request body. **Security Warning:** Disabling this option can expose your application to HTTP Request Smuggling attacks, where mismatched content-length headers cause servers and proxies to interpret request boundaries differently. This can lead to cache poisoning, credential hijacking, and bypassing security controls. Only disable this in controlled environments where you fully trust the request source.
- **autoSelectFamily**: `boolean` (optional) - Default: depends on local Node version, on Node 18.13.0 and above is `false`. Enables a family autodetection algorithm that loosely implements section 5 of [RFC 8305](https://tools.ietf.org/html/rfc8305#section-5). See [here](https://nodejs.org/api/net.html#socketconnectoptions-connectlistener) for more details. This option is ignored if not supported by the current Node version.
- **autoSelectFamilyAttemptTimeout**: `number` - Default: depends on local Node version, on Node 18.13.0 and above is `250`. The amount of time in milliseconds to wait for a connection attempt to finish before trying the next address when using the `autoSelectFamily` option. See [here](https://nodejs.org/api/net.html#socketconnectoptions-connectlistener) for more details.

#### Parameter: `H2CConnectOptions`

- **socketPath** `string | null` (optional) - Default: `null` - An IPC endpoint, either Unix domain socket or Windows named pipe.
- **timeout** `number | null` (optional) - In milliseconds, Default `10e3`.
- **servername** `string | null` (optional)
- **keepAlive** `boolean | null` (optional) - Default: `true` - TCP keep-alive enabled
- **keepAliveInitialDelay** `number | null` (optional) - Default: `60000` - TCP keep-alive interval for the socket in milliseconds

### Example - Basic Client instantiation

This will instantiate the undici H2CClient, but it will not connect to the origin until something is queued. Consider using `client.connect` to prematurely connect to the origin, or just call `client.request`.

```js
"use strict";
import { H2CClient } from "undici";

const client = new H2CClient("http://localhost:3000");
```

## Instance Methods

### `H2CClient.close([callback])`

Implements [`Dispatcher.close([callback])`](/docs/docs/api/Dispatcher.md#dispatcherclosecallback-promise).

### `H2CClient.destroy([error, callback])`

Implements [`Dispatcher.destroy([error, callback])`](/docs/docs/api/Dispatcher.md#dispatcherdestroyerror-callback-promise).

Waits until socket is closed before invoking the callback (or returning a promise if no callback is provided).

### `H2CClient.connect(options[, callback])`

See [`Dispatcher.connect(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherconnectoptions-callback).

### `H2CClient.dispatch(options, handlers)`

Implements [`Dispatcher.dispatch(options, handlers)`](/docs/docs/api/Dispatcher.md#dispatcherdispatchoptions-handler).

### `H2CClient.pipeline(options, handler)`

See [`Dispatcher.pipeline(options, handler)`](/docs/docs/api/Dispatcher.md#dispatcherpipelineoptions-handler).

### `H2CClient.request(options[, callback])`

See [`Dispatcher.request(options [, callback])`](/docs/docs/api/Dispatcher.md#dispatcherrequestoptions-callback).

### `H2CClient.stream(options, factory[, callback])`

See [`Dispatcher.stream(options, factory[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherstreamoptions-factory-callback).

### `H2CClient.upgrade(options[, callback])`

See [`Dispatcher.upgrade(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherupgradeoptions-callback).

## Instance Properties

### `H2CClient.closed`

- `boolean`

`true` after `H2CClient.close()` has been called.

### `H2CClient.destroyed`

- `boolean`

`true` after `client.destroyed()` has been called or `client.close()` has been called and the client shutdown has completed.

### `H2CClient.pipelining`

- `number`

Property to get and set the pipelining factor.

## Instance Events

### Event: `'connect'`

See [Dispatcher Event: `'connect'`](/docs/docs/api/Dispatcher.md#event-connect).

Parameters:

- **origin** `URL`
- **targets** `Array<Dispatcher>`

Emitted when a socket has been created and connected. The client will connect once `client.size > 0`.

#### Example - Client connect event

```js
import { createServer } from "node:http2";
import { H2CClient } from "undici";
import { once } from "events";

const server = createServer((request, response) => {
  response.end("Hello, World!");
}).listen();

await once(server, "listening");

const client = new H2CClient(`http://localhost:${server.address().port}`);

client.on("connect", (origin) => {
  console.log(`Connected to ${origin}`); // should print before the request body statement
});

try {
  const { body } = await client.request({
    path: "/",
    method: "GET",
  });
  body.setEncoding("utf-8");
  body.on("data", console.log);
  client.close();
  server.close();
} catch (error) {
  console.error(error);
  client.close();
  server.close();
}
```

### Event: `'disconnect'`

See [Dispatcher Event: `'disconnect'`](/docs/docs/api/Dispatcher.md#event-disconnect).

Parameters:

- **origin** `URL`
- **targets** `Array<Dispatcher>`
- **error** `Error`

Emitted when socket has disconnected. The error argument of the event is the error which caused the socket to disconnect. The client will reconnect if or once `client.size > 0`.

#### Example - Client disconnect event

```js
import { createServer } from "node:http2";
import { H2CClient } from "undici";
import { once } from "events";

const server = createServer((request, response) => {
  response.destroy();
}).listen();

await once(server, "listening");

const client = new H2CClient(`http://localhost:${server.address().port}`);

client.on("disconnect", (origin) => {
  console.log(`Disconnected from ${origin}`);
});

try {
  await client.request({
    path: "/",
    method: "GET",
  });
} catch (error) {
  console.error(error.message);
  client.close();
  server.close();
}
```

### Event: `'drain'`

Emitted when pipeline is no longer busy.

See [Dispatcher Event: `'drain'`](/docs/docs/api/Dispatcher.md#event-drain).

#### Example - Client drain event

```js
import { createServer } from "node:http2";
import { H2CClient } from "undici";
import { once } from "events";

const server = createServer((request, response) => {
  response.end("Hello, World!");
}).listen();

await once(server, "listening");

const client = new H2CClient(`http://localhost:${server.address().port}`);

client.on("drain", () => {
  console.log("drain event");
  client.close();
  server.close();
});

const requests = [
  client.request({ path: "/", method: "GET" }),
  client.request({ path: "/", method: "GET" }),
  client.request({ path: "/", method: "GET" }),
];

await Promise.all(requests);

console.log("requests completed");
```

### Event: `'error'`

Invoked for user errors such as throwing in the `onResponseError` handler.

```

## File: mcp.md
```
# `pydantic_ai.mcp`

::: pydantic_ai.mcp

```

## File: messages.md
```
# `pydantic_ai.messages`

The structure of [`ModelMessage`][pydantic_ai.messages.ModelMessage] can be shown as a graph:

```mermaid
graph RL
    SystemPromptPart(SystemPromptPart) --- ModelRequestPart
    UserPromptPart(UserPromptPart) --- ModelRequestPart
    ToolReturnPart(ToolReturnPart) --- ModelRequestPart
    RetryPromptPart(RetryPromptPart) --- ModelRequestPart
    TextPart(TextPart) --- ModelResponsePart
    ToolCallPart(ToolCallPart) --- ModelResponsePart
    ThinkingPart(ThinkingPart) --- ModelResponsePart
    ModelRequestPart("ModelRequestPart<br>(Union)") --- ModelRequest
    ModelRequest("ModelRequest(parts=list[...])") --- ModelMessage
    ModelResponsePart("ModelResponsePart<br>(Union)") --- ModelResponse
    ModelResponse("ModelResponse(parts=list[...])") --- ModelMessage("ModelMessage<br>(Union)")
```

::: pydantic_ai.messages

```

## File: mockagent.md
```
# Class: MockAgent

Extends: `undici.Dispatcher`

A mocked Agent class that implements the Agent API. It allows one to intercept HTTP requests made through undici and return mocked responses instead.

## `new MockAgent([options])`

Arguments:

* **options** `MockAgentOptions` (optional) - It extends the `Agent` options.

Returns: `MockAgent`

### Parameter: `MockAgentOptions`

Extends: [`AgentOptions`](/docs/docs/api/Agent.md#parameter-agentoptions)

* **agent** `Agent` (optional) - Default: `new Agent([options])` - a custom agent encapsulated by the MockAgent.

* **ignoreTrailingSlash** `boolean` (optional) - Default: `false` - set the default value for `ignoreTrailingSlash` for interceptors.

* **acceptNonStandardSearchParameters** `boolean` (optional) - Default: `false` - set to `true` if the matcher should also accept non standard search parameters such as multi-value items specified with `[]` (e.g. `param[]=1&param[]=2&param[]=3`) and multi-value items which values are comma separated (e.g. `param=1,2,3`).

### Example - Basic MockAgent instantiation

This will instantiate the MockAgent. It will not do anything until registered as the agent to use with requests and mock interceptions are added.

```js
import { MockAgent } from 'undici'

const mockAgent = new MockAgent()
```

### Example - Basic MockAgent instantiation with custom agent

```js
import { Agent, MockAgent } from 'undici'

const agent = new Agent()

const mockAgent = new MockAgent({ agent })
```

## Instance Methods

### `MockAgent.get(origin)`

This method creates and retrieves MockPool or MockClient instances which can then be used to intercept HTTP requests. If the number of connections on the mock agent is set to 1, a MockClient instance is returned. Otherwise a MockPool instance is returned.

For subsequent `MockAgent.get` calls on the same origin, the same mock instance will be returned.

Arguments:

* **origin** `string | RegExp | (value) => boolean` - a matcher for the pool origin to be retrieved from the MockAgent.

| Matcher type | Condition to pass          |
|:------------:| -------------------------- |
| `string`     | Exact match against string |
| `RegExp`     | Regex must pass            |
| `Function`   | Function must return true  |

Returns: `MockClient | MockPool`.

| `MockAgentOptions`   | Mock instance returned |
| -------------------- | ---------------------- |
| `connections === 1`  | `MockClient`           |
| `connections` > `1`  | `MockPool`             |

#### Example - Basic Mocked Request

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')
mockPool.intercept({ path: '/foo' }).reply(200, 'foo')

const { statusCode, body } = await request('http://localhost:3000/foo')

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - Basic Mocked Request with local mock agent dispatcher

```js
import { MockAgent, request } from 'undici'

const mockAgent = new MockAgent()

const mockPool = mockAgent.get('http://localhost:3000')
mockPool.intercept({ path: '/foo' }).reply(200, 'foo')

const {
  statusCode,
  body
} = await request('http://localhost:3000/foo', { dispatcher: mockAgent })

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - Basic Mocked Request with local mock pool dispatcher

```js
import { MockAgent, request } from 'undici'

const mockAgent = new MockAgent()

const mockPool = mockAgent.get('http://localhost:3000')
mockPool.intercept({ path: '/foo' }).reply(200, 'foo')

const {
  statusCode,
  body
} = await request('http://localhost:3000/foo', { dispatcher: mockPool })

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - Basic Mocked Request with local mock client dispatcher

```js
import { MockAgent, request } from 'undici'

const mockAgent = new MockAgent({ connections: 1 })

const mockClient = mockAgent.get('http://localhost:3000')
mockClient.intercept({ path: '/foo' }).reply(200, 'foo')

const {
  statusCode,
  body
} = await request('http://localhost:3000/foo', { dispatcher: mockClient })

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - Basic Mocked requests with multiple intercepts

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')
mockPool.intercept({ path: '/foo' }).reply(200, 'foo')
mockPool.intercept({ path: '/hello'}).reply(200, 'hello')

const result1 = await request('http://localhost:3000/foo')

console.log('response received', result1.statusCode) // response received 200

for await (const data of result1.body) {
  console.log('data', data.toString('utf8')) // data foo
}

const result2 = await request('http://localhost:3000/hello')

console.log('response received', result2.statusCode) // response received 200

for await (const data of result2.body) {
  console.log('data', data.toString('utf8')) // data hello
}
```

#### Example - Mock different requests within the same file

```js
const { MockAgent, setGlobalDispatcher } = require('undici');
const agent = new MockAgent();
agent.disableNetConnect();
setGlobalDispatcher(agent);
describe('Test', () => {
  it('200', async () => {
    const mockAgent = agent.get('http://test.com');
    // your test
  });
  it('200', async () => {
    const mockAgent = agent.get('http://testing.com');
    // your test
  });
});
```

#### Example - Mocked request with query body, headers and trailers

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

mockPool.intercept({
  path: '/foo?hello=there&see=ya',
  method: 'POST',
  body: 'form1=data1&form2=data2'
}).reply(200, { foo: 'bar' }, {
  headers: { 'content-type': 'application/json' },
  trailers: { 'Content-MD5': 'test' }
})

const {
  statusCode,
  headers,
  trailers,
  body
} = await request('http://localhost:3000/foo?hello=there&see=ya', {
  method: 'POST',
  body: 'form1=data1&form2=data2'
})

console.log('response received', statusCode) // response received 200
console.log('headers', headers) // { 'content-type': 'application/json' }

for await (const data of body) {
  console.log('data', data.toString('utf8')) // '{"foo":"bar"}'
}

console.log('trailers', trailers) // { 'content-md5': 'test' }
```

#### Example - Mocked request with origin regex

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get(new RegExp('http://localhost:3000'))
mockPool.intercept({ path: '/foo' }).reply(200, 'foo')

const {
  statusCode,
  body
} = await request('http://localhost:3000/foo')

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - Mocked request with origin function

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get((origin) => origin === 'http://localhost:3000')
mockPool.intercept({ path: '/foo' }).reply(200, 'foo')

const {
  statusCode,
  body
} = await request('http://localhost:3000/foo')

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

### `MockAgent.close()`

Closes the mock agent and waits for registered mock pools and clients to also close before resolving.

Returns: `Promise<void>`

#### Example - clean up after tests are complete

```js
import { MockAgent, setGlobalDispatcher } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

await mockAgent.close()
```

### `MockAgent.dispatch(options, handlers)`

Implements [`Agent.dispatch(options, handlers)`](/docs/docs/api/Agent.md#parameter-agentdispatchoptions).

### `MockAgent.request(options[, callback])`

See [`Dispatcher.request(options [, callback])`](/docs/docs/api/Dispatcher.md#dispatcherrequestoptions-callback).

#### Example - MockAgent request

```js
import { MockAgent } from 'undici'

const mockAgent = new MockAgent()

const mockPool = mockAgent.get('http://localhost:3000')
mockPool.intercept({ path: '/foo' }).reply(200, 'foo')

const {
  statusCode,
  body
} = await mockAgent.request({
  origin: 'http://localhost:3000',
  path: '/foo',
  method: 'GET'
})

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

### `MockAgent.deactivate()`

This method disables mocking in MockAgent.

Returns: `void`

#### Example - Deactivate Mocking

```js
import { MockAgent, setGlobalDispatcher } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

mockAgent.deactivate()
```

### `MockAgent.activate()`

This method enables mocking in a MockAgent instance. When instantiated, a MockAgent is automatically activated. Therefore, this method is only effective after `MockAgent.deactivate` has been called.

Returns: `void`

#### Example - Activate Mocking

```js
import { MockAgent, setGlobalDispatcher } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

mockAgent.deactivate()
// No mocking will occur

// Later
mockAgent.activate()
```

### `MockAgent.enableNetConnect([host])`

When requests are not matched in a MockAgent intercept, a real HTTP request is attempted. We can control this further through the use of `enableNetConnect`. This is achieved by defining host matchers so only matching requests will be attempted.

When using a string, it should only include the **hostname and optionally, the port**. In addition, calling this method multiple times with a string will allow all HTTP requests that match these values.

Arguments:

* **host** `string | RegExp | (value) => boolean` - (optional)

Returns: `void`

#### Example - Allow all non-matching urls to be dispatched in a real HTTP request

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

mockAgent.enableNetConnect()

await request('http://example.com')
// A real request is made
```

#### Example - Allow requests matching a host string to make real requests

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

mockAgent.enableNetConnect('example-1.com')
mockAgent.enableNetConnect('example-2.com:8080')

await request('http://example-1.com')
// A real request is made

await request('http://example-2.com:8080')
// A real request is made

await request('http://example-3.com')
// Will throw
```

#### Example - Allow requests matching a host regex to make real requests

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

mockAgent.enableNetConnect(new RegExp('example.com'))

await request('http://example.com')
// A real request is made
```

#### Example - Allow requests matching a host function to make real requests

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

mockAgent.enableNetConnect((value) => value === 'example.com')

await request('http://example.com')
// A real request is made
```

### `MockAgent.disableNetConnect()`

This method causes all requests to throw when requests are not matched in a MockAgent intercept.

Returns: `void`

#### Example - Disable all non-matching requests by throwing an error for each

```js
import { MockAgent, request } from 'undici'

const mockAgent = new MockAgent()

mockAgent.disableNetConnect()

await request('http://example.com')
// Will throw
```

### `MockAgent.pendingInterceptors()`

This method returns any pending interceptors registered on a mock agent. A pending interceptor meets one of the following criteria:

- Is registered with neither `.times(<number>)` nor `.persist()`, and has not been invoked;
- Is persistent (i.e., registered with `.persist()`) and has not been invoked;
- Is registered with `.times(<number>)` and has not been invoked `<number>` of times.

Returns: `PendingInterceptor[]` (where `PendingInterceptor` is a `MockDispatch` with an additional `origin: string`)

#### Example - List all pending interceptors

```js
const agent = new MockAgent()
agent.disableNetConnect()

agent
  .get('https://example.com')
  .intercept({ method: 'GET', path: '/' })
  .reply(200)

const pendingInterceptors = agent.pendingInterceptors()
// Returns [
//   {
//     timesInvoked: 0,
//     times: 1,
//     persist: false,
//     consumed: false,
//     pending: true,
//     path: '/',
//     method: 'GET',
//     body: undefined,
//     headers: undefined,
//     data: {
//       error: null,
//       statusCode: 200,
//       data: '',
//       headers: {},
//       trailers: {}
//     },
//     origin: 'https://example.com'
//   }
// ]
```

### `MockAgent.assertNoPendingInterceptors([options])`

This method throws if the mock agent has any pending interceptors. A pending interceptor meets one of the following criteria:

- Is registered with neither `.times(<number>)` nor `.persist()`, and has not been invoked;
- Is persistent (i.e., registered with `.persist()`) and has not been invoked;
- Is registered with `.times(<number>)` and has not been invoked `<number>` of times.

#### Example - Check that there are no pending interceptors

```js
const agent = new MockAgent()
agent.disableNetConnect()

agent
  .get('https://example.com')
  .intercept({ method: 'GET', path: '/' })
  .reply(200)

agent.assertNoPendingInterceptors()
// Throws an UndiciError with the following message:
//
// 1 interceptor is pending:
//
// ┌─────────┬────────┬───────────────────────┬──────┬─────────────┬────────────┬─────────────┬───────────┐
// │ (index) │ Method │        Origin         │ Path │ Status code │ Persistent │ Invocations │ Remaining │
// ├─────────┼────────┼───────────────────────┼──────┼─────────────┼────────────┼─────────────┼───────────┤
// │    0    │ 'GET'  │ 'https://example.com' │ '/'  │     200     │    '❌'    │      0      │     1     │
// └─────────┴────────┴───────────────────────┴──────┴─────────────┴────────────┴─────────────┴───────────┘
```

#### Example - access call history on MockAgent

You can register every call made within a MockAgent to be able to retrieve the body, headers and so on.

This is not enabled by default.

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent({ enableCallHistory: true })
setGlobalDispatcher(mockAgent)

await request('http://example.com', { query: { item: 1 }})

mockAgent.getCallHistory()?.firstCall()
// Returns
// MockCallHistoryLog {
//   body: undefined,
//   headers: undefined,
//   method: 'GET',
//   origin: 'http://example.com',
//   fullUrl: 'http://example.com/?item=1',
//   path: '/',
//   searchParams: { item: '1' },
//   protocol: 'http:',
//   host: 'example.com',
//   port: ''
// }
```

#### Example - clear call history

```js
const mockAgent = new MockAgent()

mockAgent.clearAllCallHistory()
```

#### Example - call history instance class method

```js
const mockAgent = new MockAgent()

const mockAgentHistory = mockAgent.getCallHistory()

mockAgentHistory?.calls() // returns an array of MockCallHistoryLogs
mockAgentHistory?.firstCall() // returns the first MockCallHistoryLogs or undefined
mockAgentHistory?.lastCall() // returns the last MockCallHistoryLogs or undefined
mockAgentHistory?.nthCall(3) // returns the third MockCallHistoryLogs or undefined
mockAgentHistory?.filterCalls({ path: '/endpoint', hash: '#hash-value' }) // returns an Array of MockCallHistoryLogs WHERE path === /endpoint OR hash === #hash-value
mockAgentHistory?.filterCalls({ path: '/endpoint', hash: '#hash-value' }, { operator: 'AND' }) // returns an Array of MockCallHistoryLogs WHERE path === /endpoint AND hash === #hash-value
mockAgentHistory?.filterCalls(/"data": "{}"/) // returns an Array of MockCallHistoryLogs where any value match regexp
mockAgentHistory?.filterCalls('application/json') // returns an Array of MockCallHistoryLogs where any value === 'application/json'
mockAgentHistory?.filterCalls((log) => log.path === '/endpoint') // returns an Array of MockCallHistoryLogs when given function returns true
mockAgentHistory?.clear() // clear the history
```

```

## File: mockcallhistory.md
```
# Class: MockCallHistory

Access to an instance with :

```js
const mockAgent = new MockAgent({ enableCallHistory: true })
mockAgent.getCallHistory()

// or
const mockAgent = new MockAgent()
mockAgent.enableMockHistory()
mockAgent.getCallHistory()

```

a MockCallHistory instance implements a **Symbol.iterator** letting you iterate on registered logs :

```ts
for (const log of mockAgent.getCallHistory()) {
  //...
}

const array: Array<MockCallHistoryLog> = [...mockAgent.getCallHistory()]
const set: Set<MockCallHistoryLog> = new Set(mockAgent.getCallHistory())
```

## class methods

### clear

Clear all MockCallHistoryLog registered. This is automatically done when calling `mockAgent.close()`

```js
mockAgent.clearCallHistory()
// same as
mockAgent.getCallHistory()?.clear()
```

### calls

Get all MockCallHistoryLog registered as an array

```js
mockAgent.getCallHistory()?.calls()
```

### firstCall

Get the first MockCallHistoryLog registered or undefined

```js
mockAgent.getCallHistory()?.firstCall()
```

### lastCall

Get the last MockCallHistoryLog registered or undefined

```js
mockAgent.getCallHistory()?.lastCall()
```

### nthCall

Get the nth MockCallHistoryLog registered or undefined

```js
mockAgent.getCallHistory()?.nthCall(3) // the third MockCallHistoryLog registered
```

### filterCallsByProtocol

Filter MockCallHistoryLog by protocol.

> more details for the first parameter can be found [here](/docs/docs/api/MockCallHistory.md#filter-parameter)

```js
mockAgent.getCallHistory()?.filterCallsByProtocol(/https/)
mockAgent.getCallHistory()?.filterCallsByProtocol('https:')
```

### filterCallsByHost

Filter MockCallHistoryLog by host.

> more details for the first parameter can be found [here](/docs/docs/api/MockCallHistory.md#filter-parameter)

```js
mockAgent.getCallHistory()?.filterCallsByHost(/localhost/)
mockAgent.getCallHistory()?.filterCallsByHost('localhost:3000')
```

### filterCallsByPort

Filter MockCallHistoryLog by port.

> more details for the first parameter can be found [here](/docs/docs/api/MockCallHistory.md#filter-parameter)

```js
mockAgent.getCallHistory()?.filterCallsByPort(/3000/)
mockAgent.getCallHistory()?.filterCallsByPort('3000')
mockAgent.getCallHistory()?.filterCallsByPort('')
```

### filterCallsByOrigin

Filter MockCallHistoryLog by origin.

> more details for the first parameter can be found [here](/docs/docs/api/MockCallHistory.md#filter-parameter)

```js
mockAgent.getCallHistory()?.filterCallsByOrigin(/http:\/\/localhost:3000/)
mockAgent.getCallHistory()?.filterCallsByOrigin('http://localhost:3000')
```

### filterCallsByPath

Filter MockCallHistoryLog by path.

> more details for the first parameter can be found [here](/docs/docs/api/MockCallHistory.md#filter-parameter)

```js
mockAgent.getCallHistory()?.filterCallsByPath(/api\/v1\/graphql/)
mockAgent.getCallHistory()?.filterCallsByPath('/api/v1/graphql')
```

### filterCallsByHash

Filter MockCallHistoryLog by hash.

> more details for the first parameter can be found [here](/docs/docs/api/MockCallHistory.md#filter-parameter)

```js
mockAgent.getCallHistory()?.filterCallsByPath(/hash/)
mockAgent.getCallHistory()?.filterCallsByPath('#hash')
```

### filterCallsByFullUrl

Filter MockCallHistoryLog by fullUrl. fullUrl contains protocol, host, port, path, hash, and query params

> more details for the first parameter can be found [here](/docs/docs/api/MockCallHistory.md#filter-parameter)

```js
mockAgent.getCallHistory()?.filterCallsByFullUrl(/https:\/\/localhost:3000\/\?query=value#hash/)
mockAgent.getCallHistory()?.filterCallsByFullUrl('https://localhost:3000/?query=value#hash')
```

### filterCallsByMethod

Filter MockCallHistoryLog by method.

> more details for the first parameter can be found [here](/docs/docs/api/MockCallHistory.md#filter-parameter)

```js
mockAgent.getCallHistory()?.filterCallsByMethod(/POST/)
mockAgent.getCallHistory()?.filterCallsByMethod('POST')
```

### filterCalls

This class method is a meta function / alias to apply complex filtering in a single way.

Parameters :

- criteria : the first parameter. a function, regexp or object.
  - function : filter MockCallHistoryLog when the function returns false
- options : the second parameter. an object.
  - options.operator : `'AND'` or `'OR'` (default `'OR'`). Used only if criteria is an object. see below

```js
mockAgent.getCallHistory()?.filterCalls((log) => log.hash === value && log.headers?.['authorization'] !== undefined)
mockAgent.getCallHistory()?.filterCalls(/"data": "{ "errors": "wrong body" }"/)

// returns an Array of MockCallHistoryLog which all have
// - a hash containing my-hash
// - OR
// - a path equal to /endpoint
mockAgent.getCallHistory()?.filterCalls({ hash: /my-hash/, path: '/endpoint' })

// returns an Array of MockCallHistoryLog which all have
// - a hash containing my-hash
// - AND
// - a path equal to /endpoint
mockAgent.getCallHistory()?.filterCalls({ hash: /my-hash/, path: '/endpoint' }, { operator: 'AND' })
```

## filter parameter

Can be :

- string. MockCallHistoryLog filtered if `value !== parameterValue`
- null. MockCallHistoryLog filtered if `value !== parameterValue`
- undefined. MockCallHistoryLog filtered if `value !== parameterValue`
- regexp. MockCallHistoryLog filtered if `!parameterValue.test(value)`

```

## File: mockcallhistorylog.md
```
# Class: MockCallHistoryLog

Access to an instance with :

```js
const mockAgent = new MockAgent({ enableCallHistory: true })
mockAgent.getCallHistory()?.firstCall()
```

## class properties

- body `mockAgent.getCallHistory()?.firstCall()?.body`
- headers `mockAgent.getCallHistory()?.firstCall()?.headers` an object
- method `mockAgent.getCallHistory()?.firstCall()?.method` a string
- fullUrl `mockAgent.getCallHistory()?.firstCall()?.fullUrl` a string containing the protocol, origin, path, query and hash
- origin `mockAgent.getCallHistory()?.firstCall()?.origin` a string containing the protocol and the host
- headers `mockAgent.getCallHistory()?.firstCall()?.headers` an object
- path `mockAgent.getCallHistory()?.firstCall()?.path` a string always starting with `/`
- searchParams `mockAgent.getCallHistory()?.firstCall()?.searchParams` an object
- protocol `mockAgent.getCallHistory()?.firstCall()?.protocol` a string (`https:`)
- host `mockAgent.getCallHistory()?.firstCall()?.host` a string
- port `mockAgent.getCallHistory()?.firstCall()?.port` an empty string or a string containing numbers
- hash `mockAgent.getCallHistory()?.firstCall()?.hash` an empty string or a string starting with `#`

## class methods

### toMap

Returns a Map instance

```js
mockAgent.getCallHistory()?.firstCall()?.toMap()?.get('hash')
// #hash
```

### toString

Returns a string computed with any class property name and value pair

```js
mockAgent.getCallHistory()?.firstCall()?.toString()
// protocol->https:|host->localhost:4000|port->4000|origin->https://localhost:4000|path->/endpoint|hash->#here|searchParams->{"query":"value"}|fullUrl->https://localhost:4000/endpoint?query=value#here|method->PUT|body->"{ "data": "hello" }"|headers->{"content-type":"application/json"}
```

```

## File: mockclient.md
```
# Class: MockClient

Extends: `undici.Client`

A mock client class that implements the same api as [MockPool](/docs/docs/api/MockPool.md).

## `new MockClient(origin, [options])`

Arguments:

* **origin** `string` - It should only include the **protocol, hostname, and port**.
* **options** `MockClientOptions` - It extends the `Client` options.

Returns: `MockClient`

### Parameter: `MockClientOptions`

Extends: `ClientOptions`

* **agent** `Agent` - the agent to associate this MockClient with.

### Example - Basic MockClient instantiation

We can use MockAgent to instantiate a MockClient ready to be used to intercept specified requests. It will not do anything until registered as the agent to use and any mock request are registered.

```js
import { MockAgent } from 'undici'

// Connections must be set to 1 to return a MockClient instance
const mockAgent = new MockAgent({ connections: 1 })

const mockClient = mockAgent.get('http://localhost:3000')
```

## Instance Methods

### `MockClient.intercept(options)`

Implements: [`MockPool.intercept(options)`](/docs/docs/api/MockPool.md#mockpoolinterceptoptions)

### `MockClient.cleanMocks()`

Implements: [`MockPool.cleanMocks()`](/docs/docs/api/MockPool.md#mockpoolcleanmocks)

### `MockClient.close()`

Implements: [`MockPool.close()`](/docs/docs/api/MockPool.md#mockpoolclose)

### `MockClient.dispatch(options, handlers)`

Implements [`Dispatcher.dispatch(options, handlers)`](/docs/docs/api/Dispatcher.md#dispatcherdispatchoptions-handler).

### `MockClient.request(options[, callback])`

See [`Dispatcher.request(options [, callback])`](/docs/docs/api/Dispatcher.md#dispatcherrequestoptions-callback).

#### Example - MockClient request

```js
import { MockAgent } from 'undici'

const mockAgent = new MockAgent({ connections: 1 })

const mockClient = mockAgent.get('http://localhost:3000')
mockClient.intercept({ path: '/foo' }).reply(200, 'foo')

const {
  statusCode,
  body
} = await mockClient.request({
  origin: 'http://localhost:3000',
  path: '/foo',
  method: 'GET'
})

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

```

## File: mockerrors.md
```
# MockErrors

Undici exposes a variety of mock error objects that you can use to enhance your mock error handling.
You can find all the mock error objects inside the `mockErrors` key.

```js
import { mockErrors } from 'undici'
```

| Mock Error            | Mock Error Codes                | Description                                                |
| --------------------- | ------------------------------- | ---------------------------------------------------------- |
| `MockNotMatchedError` | `UND_MOCK_ERR_MOCK_NOT_MATCHED` | The request does not match any registered mock dispatches. |

```

## File: mockpool.md
```
# Class: MockPool

Extends: `undici.Pool`

A mock Pool class that implements the Pool API and is used by MockAgent to intercept real requests and return mocked responses.

## `new MockPool(origin, [options])`

Arguments:

* **origin** `string` - It should only include the **protocol, hostname, and port**.
* **options** `MockPoolOptions` - It extends the `Pool` options.

Returns: `MockPool`

### Parameter: `MockPoolOptions`

Extends: `PoolOptions`

* **agent** `Agent` - the agent to associate this MockPool with.

### Example - Basic MockPool instantiation

We can use MockAgent to instantiate a MockPool ready to be used to intercept specified requests. It will not do anything until registered as the agent to use and any mock request are registered.

```js
import { MockAgent } from 'undici'

const mockAgent = new MockAgent()

const mockPool = mockAgent.get('http://localhost:3000')
```

## Instance Methods

### `MockPool.intercept(options)`

This method defines the interception rules for matching against requests for a MockPool or MockPool. We can intercept multiple times on a single instance, but each intercept is only used once. For example if you expect to make 2 requests inside a test, you need to call `intercept()` twice. Assuming you use `disableNetConnect()` you will get `MockNotMatchedError` on the second request when you only call `intercept()` once.

When defining interception rules, all the rules must pass for a request to be intercepted. If a request is not intercepted, a real request will be attempted.

| Matcher type | Condition to pass          |
|:------------:| -------------------------- |
| `string`     | Exact match against string |
| `RegExp`     | Regex must pass            |
| `Function`   | Function must return true  |

Arguments:

* **options** `MockPoolInterceptOptions` - Interception options.

Returns: `MockInterceptor` corresponding to the input options.

### Parameter: `MockPoolInterceptOptions`

* **path** `string | RegExp | (path: string) => boolean` - a matcher for the HTTP request path. When a `RegExp` or callback is used, it will match against the request path including all query parameters in alphabetical order. When a `string` is provided, the query parameters can be conveniently specified through the `MockPoolInterceptOptions.query` setting.
* **method** `string | RegExp | (method: string) => boolean` - (optional) - a matcher for the HTTP request method. Defaults to `GET`.
* **body** `string | RegExp | (body: string) => boolean` - (optional) - a matcher for the HTTP request body.
* **headers** `Record<string, string | RegExp | (body: string) => boolean`> - (optional) - a matcher for the HTTP request headers. To be intercepted, a request must match all defined headers. Extra headers not defined here may (or may not) be included in the request and do not affect the interception in any way.
* **query** `Record<string, any> | null` - (optional) - a matcher for the HTTP request query string params. Only applies when a `string` was provided for `MockPoolInterceptOptions.path`.
* **ignoreTrailingSlash** `boolean` - (optional) - set to `true` if the matcher should also match by ignoring potential trailing slashes in `MockPoolInterceptOptions.path`.

### Return: `MockInterceptor`

We can define the behaviour of an intercepted request with the following options.

* **reply** `(statusCode: number, replyData: string | Buffer | object | MockInterceptor.MockResponseDataHandler, responseOptions?: MockResponseOptions) => MockScope` - define a reply for a matching request. You can define the replyData as a callback to read incoming request data. Default for `responseOptions` is `{}`.
* **reply** `(callback: MockInterceptor.MockReplyOptionsCallback) => MockScope` - define a reply for a matching request, allowing dynamic mocking of all reply options rather than just the data.
* **replyWithError** `(error: Error) => MockScope` - define an error for a matching request to throw.
* **defaultReplyHeaders** `(headers: Record<string, string>) => MockInterceptor` - define default headers to be included in subsequent replies. These are in addition to headers on a specific reply.
* **defaultReplyTrailers** `(trailers: Record<string, string>) => MockInterceptor` - define default trailers to be included in subsequent replies. These are in addition to trailers on a specific reply.
* **replyContentLength** `() => MockInterceptor` - define automatically calculated `content-length` headers to be included in subsequent replies.

The reply data of an intercepted request may either be a string, buffer, or JavaScript object. Objects are converted to JSON while strings and buffers are sent as-is.

By default, `reply` and `replyWithError` define the behaviour for the first matching request only. Subsequent requests will not be affected (this can be changed using the returned `MockScope`).

### Parameter: `MockResponseOptions`

* **headers** `Record<string, string>` - headers to be included on the mocked reply.
* **trailers** `Record<string, string>` - trailers to be included on the mocked reply.

### Return: `MockScope`

A `MockScope` is associated with a single `MockInterceptor`. With this, we can configure the default behaviour of an intercepted reply.

* **delay** `(waitInMs: number) => MockScope` - delay the associated reply by a set amount in ms.
* **persist** `() => MockScope` - any matching request will always reply with the defined response indefinitely.
* **times** `(repeatTimes: number) => MockScope` - any matching request will reply with the defined response a fixed amount of times. This is overridden by **persist**.

#### Example - Basic Mocked Request

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

// MockPool
const mockPool = mockAgent.get('http://localhost:3000')
mockPool.intercept({ path: '/foo' }).reply(200, 'foo')

const {
  statusCode,
  body
} = await request('http://localhost:3000/foo')

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - Mocked request using reply data callbacks

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

mockPool.intercept({
  path: '/echo',
  method: 'GET',
  headers: {
    'User-Agent': 'undici',
    Host: 'example.com'
  }
}).reply(200, ({ headers }) => ({ message: headers.get('message') }))

const { statusCode, body, headers } = await request('http://localhost:3000', {
  headers: {
    message: 'hello world!'
  }
})

console.log('response received', statusCode) // response received 200
console.log('headers', headers) // { 'content-type': 'application/json' }

for await (const data of body) {
  console.log('data', data.toString('utf8')) // { "message":"hello world!" }
}
```

#### Example - Mocked request using reply options callback

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

mockPool.intercept({
  path: '/echo',
  method: 'GET',
  headers: {
    'User-Agent': 'undici',
    Host: 'example.com'
  }
}).reply(({ headers }) => ({ statusCode: 200, data: { message: headers.get('message') }})))

const { statusCode, body, headers } = await request('http://localhost:3000', {
  headers: {
    message: 'hello world!'
  }
})

console.log('response received', statusCode) // response received 200
console.log('headers', headers) // { 'content-type': 'application/json' }

for await (const data of body) {
  console.log('data', data.toString('utf8')) // { "message":"hello world!" }
}
```

#### Example - Basic Mocked requests with multiple intercepts

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

mockPool.intercept({
  path: '/foo',
  method: 'GET'
}).reply(200, 'foo')

mockPool.intercept({
  path: '/hello',
  method: 'GET',
}).reply(200, 'hello')

const result1 = await request('http://localhost:3000/foo')

console.log('response received', result1.statusCode) // response received 200

for await (const data of result1.body) {
  console.log('data', data.toString('utf8')) // data foo
}

const result2 = await request('http://localhost:3000/hello')

console.log('response received', result2.statusCode) // response received 200

for await (const data of result2.body) {
  console.log('data', data.toString('utf8')) // data hello
}
```

#### Example - Mocked request with query body, request headers and response headers and trailers

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

mockPool.intercept({
  path: '/foo?hello=there&see=ya',
  method: 'POST',
  body: 'form1=data1&form2=data2',
  headers: {
    'User-Agent': 'undici',
    Host: 'example.com'
  }
}).reply(200, { foo: 'bar' }, {
  headers: { 'content-type': 'application/json' },
  trailers: { 'Content-MD5': 'test' }
})

const {
  statusCode,
  headers,
  trailers,
  body
} = await request('http://localhost:3000/foo?hello=there&see=ya', {
    method: 'POST',
    body: 'form1=data1&form2=data2',
    headers: {
      foo: 'bar',
      'User-Agent': 'undici',
      Host: 'example.com'
    }
  })

console.log('response received', statusCode) // response received 200
console.log('headers', headers) // { 'content-type': 'application/json' }

for await (const data of body) {
  console.log('data', data.toString('utf8')) // '{"foo":"bar"}'
}

console.log('trailers', trailers) // { 'content-md5': 'test' }
```

#### Example - Mocked request using different matchers

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

mockPool.intercept({
  path: '/foo',
  method: /^GET$/,
  body: (value) => value === 'form=data',
  headers: {
    'User-Agent': 'undici',
    Host: /^example.com$/
  }
}).reply(200, 'foo')

const {
  statusCode,
  body
} = await request('http://localhost:3000/foo', {
  method: 'GET',
  body: 'form=data',
  headers: {
    foo: 'bar',
    'User-Agent': 'undici',
    Host: 'example.com'
  }
})

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - Mocked request with reply with a defined error

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

mockPool.intercept({
  path: '/foo',
  method: 'GET'
}).replyWithError(new Error('kaboom'))

try {
  await request('http://localhost:3000/foo', {
    method: 'GET'
  })
} catch (error) {
  console.error(error) // TypeError: fetch failed
  console.error(error.cause) // Error: kaboom
}
```

#### Example - Mocked request with defaultReplyHeaders

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

mockPool.intercept({
  path: '/foo',
  method: 'GET'
}).defaultReplyHeaders({ foo: 'bar' })
  .reply(200, 'foo')

const { headers } = await request('http://localhost:3000/foo')

console.log('headers', headers) // headers { foo: 'bar' }
```

#### Example - Mocked request with defaultReplyTrailers

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

mockPool.intercept({
  path: '/foo',
  method: 'GET'
}).defaultReplyTrailers({ foo: 'bar' })
  .reply(200, 'foo')

const { trailers } = await request('http://localhost:3000/foo')

console.log('trailers', trailers) // trailers { foo: 'bar' }
```

#### Example - Mocked request with automatic content-length calculation

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

mockPool.intercept({
  path: '/foo',
  method: 'GET'
}).replyContentLength().reply(200, 'foo')

const { headers } = await request('http://localhost:3000/foo')

console.log('headers', headers) // headers { 'content-length': '3' }
```

#### Example - Mocked request with automatic content-length calculation on an object

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

mockPool.intercept({
  path: '/foo',
  method: 'GET'
}).replyContentLength().reply(200, { foo: 'bar' })

const { headers } = await request('http://localhost:3000/foo')

console.log('headers', headers) // headers { 'content-length': '13' }
```

#### Example - Mocked request with persist enabled

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

mockPool.intercept({
  path: '/foo',
  method: 'GET'
}).reply(200, 'foo').persist()

const result1 = await request('http://localhost:3000/foo')
// Will match and return mocked data

const result2 = await request('http://localhost:3000/foo')
// Will match and return mocked data

// Etc
```

#### Example - Mocked request with times enabled

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

mockPool.intercept({
  path: '/foo',
  method: 'GET'
}).reply(200, 'foo').times(2)

const result1 = await request('http://localhost:3000/foo')
// Will match and return mocked data

const result2 = await request('http://localhost:3000/foo')
// Will match and return mocked data

const result3 = await request('http://localhost:3000/foo')
// Will not match and make attempt a real request
```

#### Example - Mocked request with path callback

```js
import { MockAgent, setGlobalDispatcher, request } from 'undici'
import querystring from 'querystring'

const mockAgent = new MockAgent()
setGlobalDispatcher(mockAgent)

const mockPool = mockAgent.get('http://localhost:3000')

const matchPath = requestPath => {
  const [pathname, search] = requestPath.split('?')
  const requestQuery = querystring.parse(search)

  if (!pathname.startsWith('/foo')) {
    return false
  }

  if (!Object.keys(requestQuery).includes('foo') || requestQuery.foo !== 'bar') {
    return false
  }

  return true
}

mockPool.intercept({
  path: matchPath,
  method: 'GET'
}).reply(200, 'foo')

const result = await request('http://localhost:3000/foo?foo=bar')
// Will match and return mocked data
```

### `MockPool.close()`

Closes the mock pool and de-registers from associated MockAgent.

Returns: `Promise<void>`

#### Example - clean up after tests are complete

```js
import { MockAgent } from 'undici'

const mockAgent = new MockAgent()
const mockPool = mockAgent.get('http://localhost:3000')

await mockPool.close()
```

### `MockPool.dispatch(options, handlers)`

Implements [`Dispatcher.dispatch(options, handlers)`](/docs/docs/api/Dispatcher.md#dispatcherdispatchoptions-handler).

### `MockPool.request(options[, callback])`

See [`Dispatcher.request(options [, callback])`](/docs/docs/api/Dispatcher.md#dispatcherrequestoptions-callback).

#### Example - MockPool request

```js
import { MockAgent } from 'undici'

const mockAgent = new MockAgent()

const mockPool = mockAgent.get('http://localhost:3000')
mockPool.intercept({
  path: '/foo',
  method: 'GET',
}).reply(200, 'foo')

const {
  statusCode,
  body
} = await mockPool.request({
  origin: 'http://localhost:3000',
  path: '/foo',
  method: 'GET'
})

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

### `MockPool.cleanMocks()`

This method cleans up all the prepared mocks.

Returns: `void`

```

## File: output.md
```
# `pydantic_ai.output`

::: pydantic_ai.output
    options:
        inherited_members: true
        members:
            - OutputDataT
            - ToolOutput
            - NativeOutput
            - PromptedOutput
            - TextOutput
            - StructuredDict
            - DeferredToolRequests

```

## File: pool.md
```
# Class: Pool

Extends: `undici.Dispatcher`

A pool of [Client](/docs/docs/api/Client.md) instances connected to the same upstream target.

Requests are not guaranteed to be dispatched in order of invocation.

## `new Pool(url[, options])`

Arguments:

* **url** `URL | string` - It should only include the **protocol, hostname, and port**.
* **options** `PoolOptions` (optional)

### Parameter: `PoolOptions`

Extends: [`ClientOptions`](/docs/docs/api/Client.md#parameter-clientoptions)

* **factory** `(origin: URL, opts: Object) => Dispatcher` - Default: `(origin, opts) => new Client(origin, opts)`
* **connections** `number | null` (optional) - Default: `null` - The number of `Client` instances to create. When set to `null`, the `Pool` instance will create an unlimited amount of `Client` instances.
* **clientTtl** `number | null` (optional) - Default: `null` - The amount of time before a `Client` instance is removed from the `Pool` and closed.   When set to `null`, `Client` instances will not be removed or closed based on age.

## Instance Properties

### `Pool.closed`

Implements [Client.closed](/docs/docs/api/Client.md#clientclosed)

### `Pool.destroyed`

Implements [Client.destroyed](/docs/docs/api/Client.md#clientdestroyed)

### `Pool.stats`

Returns [`PoolStats`](PoolStats.md) instance for this pool.

## Instance Methods

### `Pool.close([callback])`

Implements [`Dispatcher.close([callback])`](/docs/docs/api/Dispatcher.md#dispatcherclosecallback-promise).

### `Pool.destroy([error, callback])`

Implements [`Dispatcher.destroy([error, callback])`](/docs/docs/api/Dispatcher.md#dispatcherdestroyerror-callback-promise).

### `Pool.connect(options[, callback])`

See [`Dispatcher.connect(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherconnectoptions-callback).

### `Pool.dispatch(options, handler)`

Implements [`Dispatcher.dispatch(options, handler)`](/docs/docs/api/Dispatcher.md#dispatcherdispatchoptions-handler).

### `Pool.pipeline(options, handler)`

See [`Dispatcher.pipeline(options, handler)`](/docs/docs/api/Dispatcher.md#dispatcherpipelineoptions-handler).

### `Pool.request(options[, callback])`

See [`Dispatcher.request(options [, callback])`](/docs/docs/api/Dispatcher.md#dispatcherrequestoptions-callback).

### `Pool.stream(options, factory[, callback])`

See [`Dispatcher.stream(options, factory[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherstreamoptions-factory-callback).

### `Pool.upgrade(options[, callback])`

See [`Dispatcher.upgrade(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherupgradeoptions-callback).

## Instance Events

### Event: `'connect'`

See [Dispatcher Event: `'connect'`](/docs/docs/api/Dispatcher.md#event-connect).

### Event: `'disconnect'`

See [Dispatcher Event: `'disconnect'`](/docs/docs/api/Dispatcher.md#event-disconnect).

### Event: `'drain'`

See [Dispatcher Event: `'drain'`](/docs/docs/api/Dispatcher.md#event-drain).

```

## File: poolstats.md
```
# Class: PoolStats

Aggregate stats for a [Pool](/docs/docs/api/Pool.md) or [BalancedPool](/docs/docs/api/BalancedPool.md).

## `new PoolStats(pool)`

Arguments:

* **pool** `Pool` - Pool or BalancedPool from which to return stats.

## Instance Properties

### `PoolStats.connected`

Number of open socket connections in this pool.

### `PoolStats.free`

Number of open socket connections in this pool that do not have an active request.

### `PoolStats.pending`

Number of pending requests across all clients in this pool.

### `PoolStats.queued`

Number of queued requests across all clients in this pool.

### `PoolStats.running`

Number of currently active requests across all clients in this pool.

### `PoolStats.size`

Number of active, pending, or queued requests across all clients in this pool.

```

## File: profiles.md
```
# `pydantic_ai.profiles`

::: pydantic_ai.profiles.ModelProfile

::: pydantic_ai.profiles.openai

::: pydantic_ai.profiles.anthropic

::: pydantic_ai.profiles.google

::: pydantic_ai.profiles.meta

::: pydantic_ai.profiles.amazon

::: pydantic_ai.profiles.deepseek

::: pydantic_ai.profiles.grok

::: pydantic_ai.profiles.mistral

::: pydantic_ai.profiles.qwen

```

## File: providers.md
```
# `pydantic_ai.providers`

::: pydantic_ai.providers.Provider

::: pydantic_ai.providers.gateway.gateway_provider

::: pydantic_ai.providers.anthropic.AnthropicProvider

::: pydantic_ai.providers.google

::: pydantic_ai.providers.openai

::: pydantic_ai.providers.xai

::: pydantic_ai.providers.deepseek

::: pydantic_ai.providers.bedrock

::: pydantic_ai.providers.groq

::: pydantic_ai.providers.azure

::: pydantic_ai.providers.cohere

::: pydantic_ai.providers.voyageai.VoyageAIProvider

::: pydantic_ai.providers.cerebras.CerebrasProvider

::: pydantic_ai.providers.mistral.MistralProvider

::: pydantic_ai.providers.fireworks.FireworksProvider

::: pydantic_ai.providers.grok.GrokProvider

::: pydantic_ai.providers.together.TogetherProvider

::: pydantic_ai.providers.heroku.HerokuProvider

::: pydantic_ai.providers.github.GitHubProvider

::: pydantic_ai.providers.openrouter.OpenRouterProvider

::: pydantic_ai.providers.vercel.VercelProvider

::: pydantic_ai.providers.huggingface.HuggingFaceProvider

::: pydantic_ai.providers.moonshotai.MoonshotAIProvider

::: pydantic_ai.providers.ollama.OllamaProvider

::: pydantic_ai.providers.litellm.LiteLLMProvider

::: pydantic_ai.providers.nebius.NebiusProvider

::: pydantic_ai.providers.ovhcloud.OVHcloudProvider

::: pydantic_ai.providers.alibaba.AlibabaProvider

::: pydantic_ai.providers.sambanova.SambaNovaProvider

```

## File: proxyagent.md
```
# Class: ProxyAgent

Extends: `undici.Dispatcher`

A Proxy Agent class that implements the Agent API. It allows the connection through proxy in a simple way.

## `new ProxyAgent([options])`

Arguments:

* **options** `ProxyAgentOptions` (required) - It extends the `Agent` options.

Returns: `ProxyAgent`

### Parameter: `ProxyAgentOptions`

Extends: [`AgentOptions`](/docs/docs/api/Agent.md#parameter-agentoptions)
> It ommits `AgentOptions#connect`.

> **Note:** When `AgentOptions#connections` is set, and different from `0`, the non-standard [`proxy-connection` header](https://udger.com/resources/http-request-headers-detail?header=Proxy-Connection) will be set to `keep-alive` in the request.

* **uri** `string | URL` (required) - The URI of the proxy server.  This can be provided as a string, as an instance of the URL class, or as an object with a `uri` property of type string.
If the `uri` is provided as a string or `uri` is an object with an `uri` property of type string, then it will be parsed into a `URL` object according to the [WHATWG URL Specification](https://url.spec.whatwg.org).
For detailed information on the parsing process and potential validation errors, please refer to the ["Writing" section](https://url.spec.whatwg.org/#writing) of the WHATWG URL Specification.
* **token** `string` (optional) - It can be passed by a string of token for authentication.
* **auth** `string` (**deprecated**) - Use token.
* **clientFactory** `(origin: URL, opts: Object) => Dispatcher` (optional) - Default: `(origin, opts) => new Pool(origin, opts)`
* **proxyTunnel** `boolean` (optional) - For connections involving secure protocols, Undici will always establish a tunnel via the HTTP2  CONNECT extension. If proxyTunnel is set to true, this will occur for unsecured proxy/endpoint connections as well. Currently, there is no way to facilitate HTTP1 IP tunneling as described in https://www.rfc-editor.org/rfc/rfc9484.html#name-http-11-request. If proxyTunnel is set to false (the default), ProxyAgent connections where both the Proxy and Endpoint are unsecured will issue all requests to the Proxy, and prefix the endpoint request path with the endpoint origin address.

Examples:

```js
import { ProxyAgent } from 'undici'

const proxyAgent = new ProxyAgent('my.proxy.server')
// or
const proxyAgent = new ProxyAgent(new URL('my.proxy.server'))
// or
const proxyAgent = new ProxyAgent({ uri: 'my.proxy.server' })
// or
const proxyAgent = new ProxyAgent({
  uri: new URL('my.proxy.server'),
  proxyTls: {
    signal: AbortSignal.timeout(1000)
  }
})
```

#### Example - Basic ProxyAgent instantiation

This will instantiate the ProxyAgent. It will not do anything until registered as the agent to use with requests.

```js
import { ProxyAgent } from 'undici'

const proxyAgent = new ProxyAgent('my.proxy.server')
```

#### Example - Basic Proxy Request with global agent dispatcher

```js
import { setGlobalDispatcher, request, ProxyAgent } from 'undici'

const proxyAgent = new ProxyAgent('my.proxy.server')
setGlobalDispatcher(proxyAgent)

const { statusCode, body } = await request('http://localhost:3000/foo')

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - Basic Proxy Request with local agent dispatcher

```js
import { ProxyAgent, request } from 'undici'

const proxyAgent = new ProxyAgent('my.proxy.server')

const {
  statusCode,
  body
} = await request('http://localhost:3000/foo', { dispatcher: proxyAgent })

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - Basic Proxy Request with authentication

```js
import { setGlobalDispatcher, request, ProxyAgent } from 'undici';

const proxyAgent = new ProxyAgent({
  uri: 'my.proxy.server',
  // token: 'Bearer xxxx'
  token: `Basic ${Buffer.from('username:password').toString('base64')}`
});
setGlobalDispatcher(proxyAgent);

const { statusCode, body } = await request('http://localhost:3000/foo');

console.log('response received', statusCode); // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')); // data foo
}
```

### `ProxyAgent.close()`

Closes the proxy agent and waits for registered pools and clients to also close before resolving.

Returns: `Promise<void>`

#### Example - clean up after tests are complete

```js
import { ProxyAgent, setGlobalDispatcher } from 'undici'

const proxyAgent = new ProxyAgent('my.proxy.server')
setGlobalDispatcher(proxyAgent)

await proxyAgent.close()
```

### `ProxyAgent.dispatch(options, handlers)`

Implements [`Agent.dispatch(options, handlers)`](/docs/docs/api/Agent.md#parameter-agentdispatchoptions).

### `ProxyAgent.request(options[, callback])`

See [`Dispatcher.request(options [, callback])`](/docs/docs/api/Dispatcher.md#dispatcherrequestoptions-callback).


#### Example - ProxyAgent with Fetch

This example demonstrates how to use `fetch` with a proxy via `ProxyAgent`. It is particularly useful for scenarios requiring proxy tunneling.

```javascript
import { ProxyAgent, fetch } from 'undici';

// Define the ProxyAgent
const proxyAgent = new ProxyAgent('http://localhost:8000');

// Make a GET request through the proxy
const response = await fetch('http://localhost:3000/foo', {
  dispatcher: proxyAgent,
  method: 'GET',
});

console.log('Response status:', response.status);
console.log('Response data:', await response.text());
```

---

#### Example - ProxyAgent with a Custom Proxy Server

This example shows how to create a custom proxy server and use it with `ProxyAgent`.

```javascript
import * as http from 'node:http';
import { createProxy } from 'proxy';
import { ProxyAgent, fetch } from 'undici';

// Create a proxy server
const proxyServer = createProxy(http.createServer());
proxyServer.listen(8000, () => {
  console.log('Proxy server running on port 8000');
});

// Define and use the ProxyAgent
const proxyAgent = new ProxyAgent('http://localhost:8000');

const response = await fetch('http://example.com', {
  dispatcher: proxyAgent,
  method: 'GET',
});

console.log('Response status:', response.status);
console.log('Response data:', await response.text());
```

---

#### Example - ProxyAgent with HTTPS Tunneling

This example demonstrates how to perform HTTPS tunneling using a proxy.

```javascript
import { ProxyAgent, fetch } from 'undici';

// Define a ProxyAgent for HTTPS proxy
const proxyAgent = new ProxyAgent('https://secure.proxy.server');

// Make a request to an HTTPS endpoint via the proxy
const response = await fetch('https://secure.endpoint.com/api/data', {
  dispatcher: proxyAgent,
  method: 'GET',
});

console.log('Response status:', response.status);
console.log('Response data:', await response.json());
```

#### Example - ProxyAgent as a Global Dispatcher

`ProxyAgent` can be configured as a global dispatcher, making it available for all requests without explicitly passing it. This simplifies code and is useful when a single proxy configuration applies to all requests.

```javascript
import { ProxyAgent, setGlobalDispatcher, fetch } from 'undici';

// Define and configure the ProxyAgent
const proxyAgent = new ProxyAgent('http://localhost:8000');
setGlobalDispatcher(proxyAgent);

// Make requests without specifying the dispatcher
const response = await fetch('http://example.com');
console.log('Response status:', response.status);
console.log('Response data:', await response.text());

```

## File: redirecthandler.md
```
# Class: RedirectHandler

A class that handles redirection logic for HTTP requests.

## `new RedirectHandler(dispatch, maxRedirections, opts, handler)`

Arguments:

- **dispatch** `function` - The dispatch function to be called after every retry.
- **maxRedirections** `number` - Maximum number of redirections allowed.
- **opts** `object` - Options for handling redirection.
- **handler** `object` - An object containing handlers for different stages of the request lifecycle.

Returns: `RedirectHandler`

### Parameters

- **dispatch** `(options: Dispatch.DispatchOptions, handlers: Dispatch.DispatchHandler) => Promise<Dispatch.DispatchResponse>` (required) - Dispatch function to be called after every redirection.
- **maxRedirections** `number` (required) - Maximum number of redirections allowed.
- **opts** `object` (required) - Options for handling redirection.
- **handler** `object` (required) - Handlers for different stages of the request lifecycle.

### Properties

- **location** `string` - The current redirection location.
- **abort** `function` - The abort function.
- **opts** `object` - The options for handling redirection.
- **maxRedirections** `number` - Maximum number of redirections allowed.
- **handler** `object` - Handlers for different stages of the request lifecycle.
- **history** `Array` - An array representing the history of URLs during redirection.

### Methods

#### `onRequestStart(controller, context)`

Called when the request starts.

Parameters:

- **controller** `DispatchController` - The request controller.
- **context** `object` - The dispatch context.

#### `onRequestUpgrade(controller, statusCode, headers, socket)`

Called when an upgrade is requested.

Parameters:

- **controller** `DispatchController` - The request controller.
- **statusCode** `number` - The HTTP status code.
- **headers** `object` - The headers received in the response.
- **socket** `object` - The socket object.

#### `onResponseError(controller, error)`

Called when an error occurs.

Parameters:

- **controller** `DispatchController` - The request controller.
- **error** `Error` - The error that occurred.

#### `onResponseStart(controller, statusCode, headers, statusText)`

Called when headers are received.

Parameters:

- **controller** `DispatchController` - The request controller.
- **statusCode** `number` - The HTTP status code.
- **headers** `object` - The headers received in the response.
- **statusText** `string` - The status text.

#### `onResponseData(controller, chunk)`

Called when data is received.

Parameters:

- **controller** `DispatchController` - The request controller.
- **chunk** `Buffer` - The data chunk received.

#### `onResponseEnd(controller, trailers)`

Called when the request is complete.

Parameters:

- **controller** `DispatchController` - The request controller.
- **trailers** `object` - The trailers received.

#### `onBodySent(chunk)`

Called when the request body is sent.

Parameters:

- **chunk** `Buffer` - The chunk of the request body sent.

```

## File: result.md
```
# `pydantic_ai.result`

::: pydantic_ai.result
    options:
        inherited_members: true
        members:
            - StreamedRunResult
            - StreamedRunResultSync

```

## File: retries.md
```
# `pydantic_ai.retries`

::: pydantic_ai.retries

```

## File: retryagent.md
```
# Class: RetryAgent

Extends: `undici.Dispatcher`

A `undici.Dispatcher` that allows to automatically retry a request.
Wraps a `undici.RetryHandler`.

## `new RetryAgent(dispatcher, [options])`

Arguments:

* **dispatcher** `undici.Dispatcher` (required) - the dispatcher to wrap
* **options** `RetryHandlerOptions` (optional) - the options

Returns: `ProxyAgent`

### Parameter: `RetryHandlerOptions`

- **throwOnError** `boolean` (optional) - Disable to prevent throwing error on last retry attept, useful if you need the body on errors from server or if you have custom error handler. Default: `true`
- **retry** `(err: Error, context: RetryContext, callback: (err?: Error | null) => void) => void` (optional) - Function to be called after every retry. It should pass error if no more retries should be performed.
- **maxRetries** `number` (optional) - Maximum number of retries. Default: `5`
- **maxTimeout** `number` (optional) - Maximum number of milliseconds to wait before retrying. Default: `30000` (30 seconds)
- **minTimeout** `number` (optional) - Minimum number of milliseconds to wait before retrying. Default: `500` (half a second)
- **timeoutFactor** `number` (optional) - Factor to multiply the timeout by for each retry attempt. Default: `2`
- **retryAfter** `boolean` (optional) - It enables automatic retry after the `Retry-After` header is received. Default: `true`
- **methods** `string[]` (optional) - Array of HTTP methods to retry. Default: `['GET', 'PUT', 'HEAD', 'OPTIONS', 'DELETE']`
- **statusCodes** `number[]` (optional) - Array of HTTP status codes to retry. Default: `[429, 500, 502, 503, 504]`
- **errorCodes** `string[]` (optional) - Array of Error codes to retry. Default: `['ECONNRESET', 'ECONNREFUSED', 'ENOTFOUND', 'ENETDOWN','ENETUNREACH', 'EHOSTDOWN', 'UND_ERR_SOCKET']`

**`RetryContext`**

- `state`: `RetryState` - Current retry state. It can be mutated.
- `opts`: `Dispatch.DispatchOptions & RetryOptions` - Options passed to the retry handler.

Example:

```js
import { Agent, RetryAgent } from 'undici'

const agent = new RetryAgent(new Agent())

const res = await agent.request({
  method: 'GET',
  origin: 'http://example.com',
  path: '/',
})
console.log(res.statusCode)
console.log(await res.body.text())
```

```

## File: retryhandler.md
```
# Class: RetryHandler

Extends: `undici.DispatcherHandlers`

A handler class that implements the retry logic for a request.

## `new RetryHandler(dispatchOptions, retryHandlers, [retryOptions])`

Arguments:

- **options** `Dispatch.DispatchOptions & RetryOptions` (required) - It is an intersection of `Dispatcher.DispatchOptions` and `RetryOptions`.
- **retryHandlers** `RetryHandlers` (required) - Object containing the `dispatch` to be used on every retry, and `handler` for handling the `dispatch` lifecycle.

Returns: `retryHandler`

### Parameter: `Dispatch.DispatchOptions & RetryOptions`

Extends: [`Dispatch.DispatchOptions`](/docs/docs/api/Dispatcher.md#parameter-dispatchoptions).

#### `RetryOptions`

- **throwOnError** `boolean` (optional) - Disable to prevent throwing error on last retry attept, useful if you need the body on errors from server or if you have custom error handler.
- **retry** `(err: Error, context: RetryContext, callback: (err?: Error | null) => void) => number | null` (optional) - Function to be called after every retry. It should pass error if no more retries should be performed.
- **maxRetries** `number` (optional) - Maximum number of retries. Default: `5`
- **maxTimeout** `number` (optional) - Maximum number of milliseconds to wait before retrying. Default: `30000` (30 seconds)
- **minTimeout** `number` (optional) - Minimum number of milliseconds to wait before retrying. Default: `500` (half a second)
- **timeoutFactor** `number` (optional) - Factor to multiply the timeout by for each retry attempt. Default: `2`
- **retryAfter** `boolean` (optional) - It enables automatic retry after the `Retry-After` header is received. Default: `true`
- **methods** `string[]` (optional) - Array of HTTP methods to retry. Default: `['GET', 'PUT', 'HEAD', 'OPTIONS', 'DELETE']`
- **statusCodes** `number[]` (optional) - Array of HTTP status codes to retry. Default: `[429, 500, 502, 503, 504]`
- **errorCodes** `string[]` (optional) - Array of Error codes to retry. Default: `['ECONNRESET', 'ECONNREFUSED', 'ENOTFOUND', 'ENETDOWN','ENETUNREACH', 'EHOSTDOWN', 'UND_ERR_SOCKET']`

**`RetryContext`**

- `state`: `RetryState` - Current retry state. It can be mutated.
- `opts`: `Dispatch.DispatchOptions & RetryOptions` - Options passed to the retry handler.

**`RetryState`**

It represents the retry state for a given request.

- `counter`: `number` - Current retry attempt.

### Parameter `RetryHandlers`

- **dispatch** `(options: Dispatch.DispatchOptions, handlers: Dispatch.DispatchHandler) => Promise<Dispatch.DispatchResponse>` (required) - Dispatch function to be called after every retry.

>__Note__: The `RetryHandler` does not retry over stateful bodies (e.g. streams, AsyncIterable) as those, once consumed, are left in a state that cannot be reutilized. For these situations the `RetryHandler` will identify
>the body as stateful and will not retry the request rejecting with the error `UND_ERR_REQ_RETRY`.

Examples:

```js
const client = new Client(`http://localhost:${server.address().port}`);
const chunks = [];
const handler = new RetryHandler(
  {
    ...dispatchOptions,
    retryOptions: {
      // custom retry function
      retry: function (err, state, callback) {
        counter++;

        if (err.code && err.code === "UND_ERR_DESTROYED") {
          callback(err);
          return;
        }

        if (err.statusCode === 206) {
          callback(err);
          return;
        }

        setTimeout(() => callback(null), 1000);
      },
    },
  },
  {
    dispatch: (...args) => {
      return client.dispatch(...args);
    },
    handler: {
      onRequestStart() {},
      onBodySent(chunk) {},
      onResponseStart(_controller, status, headers) {
        // do something with headers
      },
      onResponseData(_controller, chunk) {
        chunks.push(chunk);
      },
      onResponseEnd() {},
      onResponseError(_controller, err) {
        // handle error properly
      },
    },
  }
);
```

#### Example - Basic RetryHandler with defaults

```js
const client = new Client(`http://localhost:${server.address().port}`);
const handler = new RetryHandler(dispatchOptions, {
  dispatch: client.dispatch.bind(client),
  handler: {
    onRequestStart() {},
    onBodySent(chunk) {},
    onResponseStart(_controller, status, headers) {},
    onResponseData(_controller, chunk) {},
    onResponseEnd() {},
    onResponseError(_controller, err) {},
  },
});
```

```

## File: roundrobinpool.md
```
# Class: RoundRobinPool

Extends: `undici.Dispatcher`

A pool of [Client](/docs/docs/api/Client.md) instances connected to the same upstream target with round-robin client selection.

Unlike [`Pool`](/docs/docs/api/Pool.md), which always selects the first available client, `RoundRobinPool` cycles through clients in a round-robin fashion. This ensures even distribution of requests across all connections, which is particularly useful when the upstream target is behind a load balancer that round-robins TCP connections across multiple backend servers (e.g., Kubernetes Services).

Requests are not guaranteed to be dispatched in order of invocation.

## `new RoundRobinPool(url[, options])`

Arguments:

* **url** `URL | string` - It should only include the **protocol, hostname, and port**.
* **options** `RoundRobinPoolOptions` (optional)

### Parameter: `RoundRobinPoolOptions`

Extends: [`ClientOptions`](/docs/docs/api/Client.md#parameter-clientoptions)

* **factory** `(origin: URL, opts: Object) => Dispatcher` - Default: `(origin, opts) => new Client(origin, opts)`
* **connections** `number | null` (optional) - Default: `null` - The number of `Client` instances to create. When set to `null`, the `RoundRobinPool` instance will create an unlimited amount of `Client` instances.
* **clientTtl** `number | null` (optional) - Default: `null` - The amount of time before a `Client` instance is removed from the `RoundRobinPool` and closed. When set to `null`, `Client` instances will not be removed or closed based on age.

## Use Case

`RoundRobinPool` is designed for scenarios where:

1. You connect to a single origin (e.g., `http://my-service.namespace.svc`)
2. That origin is backed by a load balancer distributing TCP connections across multiple servers
3. You want requests evenly distributed across all backend servers

**Example**: In Kubernetes, when using a Service DNS name with multiple Pod replicas, kube-proxy load balances TCP connections. `RoundRobinPool` ensures each connection (and thus each Pod) receives an equal share of requests.

### Important: Backend Distribution Considerations

`RoundRobinPool` distributes **HTTP requests** evenly across **TCP connections**. Whether this translates to even backend server distribution depends on the load balancer's behavior:

**✓ Works when the load balancer**:
- Assigns different backends to different TCP connections from the same client
- Uses algorithms like: round-robin, random, least-connections (without client affinity)
- Example: Default Kubernetes Services without `sessionAffinity`

**✗ Does NOT work when**:
- Load balancer has client/source IP affinity (all connections from one IP → same backend)
- Load balancer uses source-IP-hash or sticky sessions

**How it works:**
1. `RoundRobinPool` creates N TCP connections to the load balancer endpoint
2. Load balancer assigns each TCP connection to a backend (per its algorithm)
3. `RoundRobinPool` cycles HTTP requests across those N connections
4. Result: Requests distributed proportionally to how the LB distributed the connections

If the load balancer assigns all connections to the same backend (e.g., due to session affinity), `RoundRobinPool` cannot overcome this. In such cases, consider using [`BalancedPool`](/docs/docs/api/BalancedPool.md) with direct backend addresses (e.g., individual pod IPs) instead of a load-balanced endpoint.

## Instance Properties

### `RoundRobinPool.closed`

Implements [Client.closed](/docs/docs/api/Client.md#clientclosed)

### `RoundRobinPool.destroyed`

Implements [Client.destroyed](/docs/docs/api/Client.md#clientdestroyed)

### `RoundRobinPool.stats`

Returns [`PoolStats`](PoolStats.md) instance for this pool.

## Instance Methods

### `RoundRobinPool.close([callback])`

Implements [`Dispatcher.close([callback])`](/docs/docs/api/Dispatcher.md#dispatcherclosecallback-promise).

### `RoundRobinPool.destroy([error, callback])`

Implements [`Dispatcher.destroy([error, callback])`](/docs/docs/api/Dispatcher.md#dispatcherdestroyerror-callback-promise).

### `RoundRobinPool.connect(options[, callback])`

See [`Dispatcher.connect(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherconnectoptions-callback).

### `RoundRobinPool.dispatch(options, handler)`

Implements [`Dispatcher.dispatch(options, handler)`](/docs/docs/api/Dispatcher.md#dispatcherdispatchoptions-handler).

### `RoundRobinPool.pipeline(options, handler)`

See [`Dispatcher.pipeline(options, handler)`](/docs/docs/api/Dispatcher.md#dispatcherpipelineoptions-handler).

### `RoundRobinPool.request(options[, callback])`

See [`Dispatcher.request(options [, callback])`](/docs/docs/api/Dispatcher.md#dispatcherrequestoptions-callback).

### `RoundRobinPool.stream(options, factory[, callback])`

See [`Dispatcher.stream(options, factory[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherstreamoptions-factory-callback).

### `RoundRobinPool.upgrade(options[, callback])`

See [`Dispatcher.upgrade(options[, callback])`](/docs/docs/api/Dispatcher.md#dispatcherupgradeoptions-callback).

## Instance Events

### Event: `'connect'`

See [Dispatcher Event: `'connect'`](/docs/docs/api/Dispatcher.md#event-connect).

### Event: `'disconnect'`

See [Dispatcher Event: `'disconnect'`](/docs/docs/api/Dispatcher.md#event-disconnect).

### Event: `'drain'`

See [Dispatcher Event: `'drain'`](/docs/docs/api/Dispatcher.md#event-drain).

## Example

```javascript
import { RoundRobinPool } from 'undici'

const pool = new RoundRobinPool('http://my-service.default.svc.cluster.local', {
  connections: 10
})

// Requests will be distributed evenly across all 10 connections
for (let i = 0; i < 100; i++) {
  const { body } = await pool.request({
    path: '/api/data',
    method: 'GET'
  })
  console.log(await body.json())
}

await pool.close()
```

## See Also

- [Issue #3648](https://github.com/nodejs/undici/issues/3648) - Original issue describing uneven distribution


```

## File: run.md
```
# `pydantic_ai.run`

::: pydantic_ai.run

```

## File: settings.md
```
# `pydantic_ai.settings`

::: pydantic_ai.settings
    options:
      inherited_members: true
      members:
        - ModelSettings
        - UsageLimits

```

## File: snapshotagent.md
```
# SnapshotAgent

The `SnapshotAgent` provides a powerful way to record and replay HTTP requests for testing purposes. It extends `MockAgent` to enable automatic snapshot testing, eliminating the need to manually define mock responses.

## Use Cases

- **Integration Testing**: Record real API interactions and replay them in tests
- **Offline Development**: Work with APIs without network connectivity
- **Consistent Test Data**: Ensure tests use the same responses across runs
- **API Contract Testing**: Capture and validate API behavior over time

## Constructor

```javascript
new SnapshotAgent([options])
```

### Parameters

- **options** `Object` (optional)
  - **mode** `String` - The snapshot mode: `'record'`, `'playback'`, or `'update'`. Default: `'record'`
  - **snapshotPath** `String` - Path to the snapshot file for loading/saving
  - **maxSnapshots** `Number` - Maximum number of snapshots to keep in memory. Default: `Infinity`
  - **autoFlush** `Boolean` - Whether to automatically save snapshots to disk. Default: `false`
  - **flushInterval** `Number` - Interval in milliseconds for auto-flush. Default: `30000`
  - **matchHeaders** `Array<String>` - Specific headers to include in request matching. Default: all headers
  - **ignoreHeaders** `Array<String>` - Headers to ignore during request matching
  - **excludeHeaders** `Array<String>` - Headers to exclude from snapshots (for security)
  - **matchBody** `Boolean` - Whether to include request body in matching. Default: `true`
  - **matchQuery** `Boolean` - Whether to include query parameters in matching. Default: `true`
  - **caseSensitive** `Boolean` - Whether header matching is case-sensitive. Default: `false`
  - **shouldRecord** `Function` - Callback to determine if a request should be recorded
  - **shouldPlayback** `Function` - Callback to determine if a request should be played back
  - **excludeUrls** `Array` - URL patterns (strings or RegExp) to exclude from recording/playback
  - All other options from `MockAgent` are supported

### Modes

#### Record Mode (`'record'`)
Makes real HTTP requests and saves the responses to snapshots.

```javascript
import { SnapshotAgent, setGlobalDispatcher } from 'undici'

const agent = new SnapshotAgent({ 
  mode: 'record',
  snapshotPath: './test/snapshots/api-calls.json'
})
setGlobalDispatcher(agent)

// Makes real requests and records them
const response = await fetch('https://api.example.com/users')
const users = await response.json()

// Save recorded snapshots
await agent.saveSnapshots()
```

#### Playback Mode (`'playback'`)
Replays recorded responses without making real HTTP requests.

```javascript
import { SnapshotAgent, setGlobalDispatcher } from 'undici'

const agent = new SnapshotAgent({
  mode: 'playback',
  snapshotPath: './test/snapshots/api-calls.json'
})
setGlobalDispatcher(agent)

// Uses recorded response instead of real request
const response = await fetch('https://api.example.com/users')
```

#### Update Mode (`'update'`)
Uses existing snapshots when available, but records new ones for missing requests.

```javascript
import { SnapshotAgent, setGlobalDispatcher } from 'undici'

const agent = new SnapshotAgent({
  mode: 'update',
  snapshotPath: './test/snapshots/api-calls.json'
})
setGlobalDispatcher(agent)

// Uses snapshot if exists, otherwise makes real request and records it
const response = await fetch('https://api.example.com/new-endpoint')
```

## Instance Methods

### `agent.saveSnapshots([filePath])`

Saves all recorded snapshots to a file.

#### Parameters

- **filePath** `String` (optional) - Path to save snapshots. Uses constructor `snapshotPath` if not provided.

#### Returns

`Promise<void>`

```javascript
await agent.saveSnapshots('./custom-snapshots.json')
```

## Advanced Configuration

### Header Filtering

Control which headers are used for request matching and what gets stored in snapshots:

```javascript
const agent = new SnapshotAgent({
  mode: 'record',
  snapshotPath: './snapshots.json',
  
  // Only match these specific headers
  matchHeaders: ['content-type', 'accept'],
  
  // Ignore these headers during matching (but still store them)
  ignoreHeaders: ['user-agent', 'date'],
  
  // Exclude sensitive headers from snapshots entirely
  excludeHeaders: ['authorization', 'x-api-key', 'cookie']
})
```

### Custom Request/Response Filtering

Use callback functions to determine what gets recorded or played back:

```javascript
const agent = new SnapshotAgent({
  mode: 'record',
  snapshotPath: './snapshots.json',
  
  // Only record GET requests to specific endpoints
  shouldRecord: (requestOpts) => {
    const url = new URL(requestOpts.path, requestOpts.origin)
    return requestOpts.method === 'GET' && url.pathname.startsWith('/api/v1/')
  },
  
  // Skip authentication endpoints during playback
  shouldPlayback: (requestOpts) => {
    const url = new URL(requestOpts.path, requestOpts.origin)
    return !url.pathname.includes('/auth/')
  }
})
```

### URL Pattern Exclusion

Exclude specific URLs from recording/playback using patterns:

```javascript
const agent = new SnapshotAgent({
  mode: 'record',
  snapshotPath: './snapshots.json',
  
  excludeUrls: [
    'https://analytics.example.com',  // String match
    /\/api\/v\d+\/health/,           // Regex pattern
    'telemetry'                      // Substring match
  ]
})
```

### Memory Management

Configure automatic memory and disk management:

```javascript
const agent = new SnapshotAgent({
  mode: 'record',
  snapshotPath: './snapshots.json',
  
  // Keep only 1000 snapshots in memory
  maxSnapshots: 1000,
  
  // Automatically save to disk every 30 seconds
  autoFlush: true,
  flushInterval: 30000
})
```

### Sequential Response Handling

Handle multiple responses for the same request (similar to nock):

```javascript
// In record mode, multiple identical requests get recorded as separate responses
const agent = new SnapshotAgent({ mode: 'record', snapshotPath: './sequential.json' })

// First call returns response A
await fetch('https://api.example.com/random')

// Second call returns response B  
await fetch('https://api.example.com/random')

await agent.saveSnapshots()

// In playback mode, calls return responses in sequence
const playbackAgent = new SnapshotAgent({ mode: 'playback', snapshotPath: './sequential.json' })

// Returns response A
const first = await fetch('https://api.example.com/random')

// Returns response B
const second = await fetch('https://api.example.com/random')

// Third call repeats the last response (B)
const third = await fetch('https://api.example.com/random')
```

## Managing Snapshots

### Replacing Existing Snapshots

```javascript
// Load existing snapshots
await agent.loadSnapshots('./old-snapshots.json')

// Get snapshot data
const recorder = agent.getRecorder()
const snapshots = recorder.getSnapshots()

// Modify or filter snapshots
const filteredSnapshots = snapshots.filter(s => 
  !s.request.url.includes('deprecated')
)

// Replace all snapshots
agent.replaceSnapshots(filteredSnapshots.map((snapshot, index) => ({
  hash: `new-hash-${index}`,
  snapshot
})))

// Save updated snapshots
await agent.saveSnapshots('./updated-snapshots.json')
```

### `agent.loadSnapshots([filePath])`

Loads snapshots from a file.

#### Parameters

- **filePath** `String` (optional) - Path to load snapshots from. Uses constructor `snapshotPath` if not provided.

#### Returns

`Promise<void>`

```javascript
await agent.loadSnapshots('./existing-snapshots.json')
```

### `agent.getRecorder()`

Gets the underlying `SnapshotRecorder` instance.

#### Returns

`SnapshotRecorder`

```javascript
const recorder = agent.getRecorder()
console.log(`Recorded ${recorder.size()} interactions`)
```

### `agent.getMode()`

Gets the current snapshot mode.

#### Returns

`String` - The current mode (`'record'`, `'playback'`, or `'update'`)

### `agent.clearSnapshots()`

Clears all recorded snapshots from memory.

```javascript
agent.clearSnapshots()
```

## Working with Different Request Types

### GET Requests

```javascript
// Record mode
const agent = new SnapshotAgent({ mode: 'record', snapshotPath: './get-snapshots.json' })
setGlobalDispatcher(agent)

const response = await fetch('https://jsonplaceholder.typicode.com/posts/1')
const post = await response.json()

await agent.saveSnapshots()
```

### POST Requests with Body

```javascript
// Record mode
const agent = new SnapshotAgent({ mode: 'record', snapshotPath: './post-snapshots.json' })
setGlobalDispatcher(agent)

const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ title: 'Test Post', body: 'Content' })
})

await agent.saveSnapshots()
```

### Using with `undici.request`

SnapshotAgent works with all undici APIs, not just fetch:

```javascript
import { SnapshotAgent, request, setGlobalDispatcher } from 'undici'

const agent = new SnapshotAgent({ mode: 'record', snapshotPath: './request-snapshots.json' })
setGlobalDispatcher(agent)

const { statusCode, headers, body } = await request('https://api.example.com/data')
const data = await body.json()

await agent.saveSnapshots()
```

## Test Integration

### Basic Test Setup

```javascript
import { test } from 'node:test'
import { SnapshotAgent, setGlobalDispatcher, getGlobalDispatcher } from 'undici'

test('API integration test', async (t) => {
  const originalDispatcher = getGlobalDispatcher()
  
  const agent = new SnapshotAgent({
    mode: 'playback',
    snapshotPath: './test/snapshots/api-test.json'
  })
  setGlobalDispatcher(agent)
  
  t.after(() => setGlobalDispatcher(originalDispatcher))
  
  // This will use recorded data
  const response = await fetch('https://api.example.com/users')
  const users = await response.json()
  
  assert(Array.isArray(users))
  assert(users.length > 0)
})
```

### Environment-Based Mode Selection

```javascript
const mode = process.env.SNAPSHOT_MODE || 'playback'

const agent = new SnapshotAgent({
  mode,
  snapshotPath: './test/snapshots/integration.json'
})

// Run with: SNAPSHOT_MODE=record npm test (to record)
// Run with: npm test (to playback)
```

### Test Helper Function

```javascript
function createSnapshotAgent(testName, mode = 'playback') {
  return new SnapshotAgent({
    mode,
    snapshotPath: `./test/snapshots/${testName}.json`
  })
}

test('user API test', async (t) => {
  const agent = createSnapshotAgent('user-api')
  setGlobalDispatcher(agent)
  
  // Test implementation...
})
```

## Snapshot File Format

Snapshots are stored as JSON with the following structure:

```json
[
  {
    "hash": "dGVzdC1oYXNo...",
    "snapshot": {
      "request": {
        "method": "GET",
        "url": "https://api.example.com/users",
        "headers": {
          "authorization": "Bearer token"
        },
        "body": undefined
      },
      "response": {
        "statusCode": 200,
        "headers": {
          "content-type": "application/json"
        },
        "body": "eyJkYXRhIjoidGVzdCJ9", // base64 encoded
        "trailers": {}
      },
      "timestamp": "2024-01-01T00:00:00.000Z"
    }
  }
]
```

## Security Considerations

### Sensitive Data in Snapshots

By default, SnapshotAgent records all headers and request/response data. For production use, always exclude sensitive information:

```javascript
const agent = new SnapshotAgent({
  mode: 'record',
  snapshotPath: './snapshots.json',
  
  // Exclude sensitive headers from snapshots
  excludeHeaders: [
    'authorization',
    'x-api-key', 
    'cookie',
    'set-cookie',
    'x-auth-token',
    'x-csrf-token'
  ],
  
  // Filter out requests with sensitive data
  shouldRecord: (requestOpts) => {
    const url = new URL(requestOpts.path, requestOpts.origin)
    
    // Don't record authentication endpoints
    if (url.pathname.includes('/auth/') || url.pathname.includes('/login')) {
      return false
    }
    
    // Don't record if request contains sensitive body data
    if (requestOpts.body && typeof requestOpts.body === 'string') {
      const body = requestOpts.body.toLowerCase()
      if (body.includes('password') || body.includes('secret')) {
        return false
      }
    }
    
    return true
  }
})
```

### Snapshot File Security

**Important**: Snapshot files may contain sensitive data. Handle them securely:

- ✅ Add snapshot files to `.gitignore` if they contain real API data
- ✅ Use environment-specific snapshots (dev/staging/prod)
- ✅ Regularly review snapshot contents for sensitive information
- ✅ Use the `excludeHeaders` option for production snapshots
- ❌ Never commit snapshots with real authentication tokens
- ❌ Don't share snapshot files containing personal data

```gitignore
# Exclude snapshots with real data
/test/snapshots/production-*.json
/test/snapshots/*-real-data.json

# Include sanitized test snapshots
!/test/snapshots/mock-*.json
```

## Error Handling

### Missing Snapshots in Playback Mode

```javascript
try {
  const response = await fetch('https://api.example.com/nonexistent')
} catch (error) {
  if (error.message.includes('No snapshot found')) {
    // Handle missing snapshot
    console.log('Snapshot not found for this request')
  }
}
```

### Handling Network Errors in Record Mode

```javascript
const agent = new SnapshotAgent({ mode: 'record', snapshotPath: './snapshots.json' })

try {
  const response = await fetch('https://nonexistent-api.example.com/data')
} catch (error) {
  // Network errors are not recorded as snapshots
  console.log('Network error:', error.message)
}
```

## Best Practices

### 1. Organize Snapshots by Test Suite

```javascript
// Use descriptive snapshot file names
const agent = new SnapshotAgent({
  mode: 'playback',
  snapshotPath: `./test/snapshots/${testSuiteName}-${testName}.json`
})
```

### 2. Version Control Snapshots

Add snapshot files to version control to ensure consistent test behavior across environments:

```gitignore
# Include snapshots in version control
!/test/snapshots/*.json
```

### 3. Clean Up Test Data

```javascript
test('API test', async (t) => {
  const agent = new SnapshotAgent({
    mode: 'playback',
    snapshotPath: './test/snapshots/temp-test.json'
  })
  
  // Clean up after test
  t.after(() => {
    agent.clearSnapshots()
  })
})
```

### 4. Snapshot Validation

```javascript
test('validate snapshot contents', async (t) => {
  const agent = new SnapshotAgent({
    mode: 'playback',
    snapshotPath: './test/snapshots/validation.json'
  })
  
  const recorder = agent.getRecorder()
  const snapshots = recorder.getSnapshots()
  
  // Validate snapshot structure
  assert(snapshots.length > 0, 'Should have recorded snapshots')
  assert(snapshots[0].request.url.startsWith('https://'), 'Should use HTTPS')
})
```

## Comparison with Other Tools

### vs Manual MockAgent Setup

**Manual MockAgent:**
```javascript
const mockAgent = new MockAgent()
const mockPool = mockAgent.get('https://api.example.com')

mockPool.intercept({
  path: '/users',
  method: 'GET'
}).reply(200, [
  { id: 1, name: 'User 1' },
  { id: 2, name: 'User 2' }
])
```

**SnapshotAgent:**
```javascript
// Record once
const agent = new SnapshotAgent({ mode: 'record', snapshotPath: './snapshots.json' })
// Real API call gets recorded automatically

// Use in tests
const agent = new SnapshotAgent({ mode: 'playback', snapshotPath: './snapshots.json' })
// Automatically replays recorded response
```

### vs nock

SnapshotAgent provides similar functionality to nock but is specifically designed for undici:

- ✅ Works with all undici APIs (`request`, `stream`, `pipeline`, etc.)
- ✅ Supports undici-specific features (RetryAgent, connection pooling)
- ✅ Better TypeScript integration
- ✅ More efficient for high-performance scenarios

## See Also

```

## File: socks5proxyagent.md
```
# Class: Socks5ProxyAgent

Extends: `undici.Dispatcher`

A SOCKS5 proxy wrapper class that implements the Dispatcher API. It enables HTTP requests to be routed through a SOCKS5 proxy server, providing connection tunneling and authentication support.

## `new Socks5ProxyAgent(proxyUrl[, options])`

Arguments:

* **proxyUrl** `string | URL` (required) - The SOCKS5 proxy server URL. Must use `socks5://` or `socks://` protocol.
* **options** `Socks5ProxyAgent.Options` (optional) - Additional configuration options.

Returns: `Socks5ProxyAgent`

### Parameter: `Socks5ProxyAgent.Options`

Extends: [`PoolOptions`](/docs/docs/api/Pool.md#parameter-pooloptions)

* **headers** `IncomingHttpHeaders` (optional) - Additional headers to send with proxy connections.
* **username** `string` (optional) - SOCKS5 proxy username for authentication. Can also be provided in the proxy URL.
* **password** `string` (optional) - SOCKS5 proxy password for authentication. Can also be provided in the proxy URL.
* **connect** `Function` (optional) - Custom connector function for the proxy connection.
* **proxyTls** `BuildOptions` (optional) - TLS options for the proxy connection (when using SOCKS5 over TLS).

Examples:

```js
import { Socks5ProxyAgent } from 'undici'

const socks5Proxy = new Socks5ProxyAgent('socks5://localhost:1080')
// or with authentication
const socks5ProxyWithAuth = new Socks5ProxyAgent('socks5://user:pass@localhost:1080')
// or with options
const socks5ProxyWithOptions = new Socks5ProxyAgent('socks5://localhost:1080', {
  username: 'user',
  password: 'pass',
  connections: 10
})
```

#### Example - Basic SOCKS5 Proxy instantiation

This will instantiate the Socks5ProxyAgent. It will not do anything until registered as the dispatcher to use with requests.

```js
import { Socks5ProxyAgent } from 'undici'

const socks5Proxy = new Socks5ProxyAgent('socks5://localhost:1080')
```

#### Example - Basic SOCKS5 Proxy Request with global dispatcher

```js
import { setGlobalDispatcher, request, Socks5ProxyAgent } from 'undici'

const socks5Proxy = new Socks5ProxyAgent('socks5://localhost:1080')
setGlobalDispatcher(socks5Proxy)

const { statusCode, body } = await request('http://localhost:3000/foo')

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - Basic SOCKS5 Proxy Request with local dispatcher

```js
import { Socks5ProxyAgent, request } from 'undici'

const socks5Proxy = new Socks5ProxyAgent('socks5://localhost:1080')

const {
  statusCode,
  body
} = await request('http://localhost:3000/foo', { dispatcher: socks5Proxy })

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - SOCKS5 Proxy Request with authentication

```js
import { setGlobalDispatcher, request, Socks5ProxyAgent } from 'undici'

// Authentication via URL
const socks5Proxy = new Socks5ProxyAgent('socks5://username:password@localhost:1080')

// Or authentication via options
// const socks5Proxy = new Socks5ProxyAgent('socks5://localhost:1080', {
//   username: 'username',
//   password: 'password'
// })

setGlobalDispatcher(socks5Proxy)

const { statusCode, body } = await request('http://localhost:3000/foo')

console.log('response received', statusCode) // response received 200

for await (const data of body) {
  console.log('data', data.toString('utf8')) // data foo
}
```

#### Example - SOCKS5 Proxy with HTTPS requests

SOCKS5 proxy supports both HTTP and HTTPS requests through tunneling:

```js
import { Socks5ProxyAgent, request } from 'undici'

const socks5Proxy = new Socks5ProxyAgent('socks5://localhost:1080')

const response = await request('https://api.example.com/data', {
  dispatcher: socks5Proxy,
  method: 'GET'
})

console.log('Response status:', response.statusCode)
console.log('Response data:', await response.body.json())
```

#### Example - SOCKS5 Proxy with Fetch

```js
import { Socks5ProxyAgent, fetch } from 'undici'

const socks5Proxy = new Socks5ProxyAgent('socks5://localhost:1080')

const response = await fetch('http://localhost:3000/api/users', {
  dispatcher: socks5Proxy,
  method: 'GET'
})

console.log('Response status:', response.status)
console.log('Response data:', await response.text())
```

#### Example - Connection Pooling

SOCKS5ProxyWrapper automatically manages connection pooling for better performance:

```js
import { Socks5ProxyAgent, request } from 'undici'

const socks5Proxy = new Socks5ProxyAgent('socks5://localhost:1080', {
  connections: 10, // Allow up to 10 concurrent connections
  pipelining: 1    // Enable HTTP/1.1 pipelining
})

// Multiple requests will reuse connections through the SOCKS5 tunnel
const responses = await Promise.all([
  request('http://api.example.com/endpoint1', { dispatcher: socks5Proxy }),
  request('http://api.example.com/endpoint2', { dispatcher: socks5Proxy }),
  request('http://api.example.com/endpoint3', { dispatcher: socks5Proxy })
])

console.log('All requests completed through the same SOCKS5 proxy')
```

### `Socks5ProxyAgent.close()`

Closes the SOCKS5 proxy wrapper and waits for all underlying pools and connections to close before resolving.

Returns: `Promise<void>`

#### Example - clean up after tests are complete

```js
import { Socks5ProxyAgent, setGlobalDispatcher } from 'undici'

const socks5Proxy = new Socks5ProxyAgent('socks5://localhost:1080')
setGlobalDispatcher(socks5Proxy)

// ... make requests

await socks5Proxy.close()
```

### `Socks5ProxyAgent.destroy([err])`

Destroys the SOCKS5 proxy wrapper and all underlying connections immediately.

Arguments:
* **err** `Error` (optional) - The error that caused the destruction.

Returns: `Promise<void>`

#### Example - force close all connections

```js
import { Socks5ProxyAgent } from 'undici'

const socks5Proxy = new Socks5ProxyAgent('socks5://localhost:1080')

// Force close all connections
await socks5Proxy.destroy()
```

### `Socks5ProxyAgent.dispatch(options, handlers)`

Implements [`Dispatcher.dispatch(options, handlers)`](/docs/docs/api/Dispatcher.md#dispatcherdispatchoptions-handlers).

### `Socks5ProxyAgent.request(options[, callback])`

See [`Dispatcher.request(options [, callback])`](/docs/docs/api/Dispatcher.md#dispatcherrequestoptions-callback).

## Debugging

SOCKS5 proxy connections can be debugged using Node.js diagnostics:

```sh
NODE_DEBUG=undici:socks5 node script.js
```

This will output detailed information about the SOCKS5 handshake, authentication, and connection establishment.

## SOCKS5 Protocol Support

The Socks5ProxyAgent supports the following SOCKS5 features:

### Authentication Methods

- **No Authentication** (`0x00`) - For public or internal proxies
- **Username/Password** (`0x02`) - RFC 1929 authentication

### Address Types

- **IPv4** (`0x01`) - Standard IPv4 addresses
- **Domain Name** (`0x03`) - Domain names (recommended for flexibility)
- **IPv6** (`0x04`) - IPv6 addresses (full support for standard and compressed notation)

### Commands

- **CONNECT** (`0x01`) - Establish TCP connection (primary use case for HTTP)

### Error Handling

The wrapper handles various SOCKS5 error conditions:

- Connection refused by proxy
- Authentication failures
- Network unreachable
- Host unreachable
- Unsupported address types or commands

## Performance Considerations

- **Connection Pooling**: Automatically pools connections through the SOCKS5 tunnel for better performance
- **HTTP/1.1 Pipelining**: Supports pipelining when enabled
- **DNS Resolution**: Domain names are resolved by the SOCKS5 proxy, reducing local DNS queries
- **TLS Termination**: HTTPS connections are encrypted end-to-end, with the SOCKS5 proxy only handling the TCP tunnel

## Security Notes

1. **Authentication**: Credentials are sent to the SOCKS5 proxy in plaintext unless using SOCKS5 over TLS
2. **DNS Leaks**: All DNS resolution happens on the proxy server, preventing DNS leaks
3. **End-to-end Encryption**: HTTPS traffic remains encrypted between client and final destination
4. **Connection Security**: Consider using authenticated proxies and secure networks

## Compatibility

- **Protocol**: SOCKS5 (RFC 1928) with Username/Password Authentication (RFC 1929)
- **Transport**: TCP only (UDP support not implemented)
- **Node.js**: Compatible with all supported Node.js versions
- **HTTP Versions**: Works with HTTP/1.1 and HTTP/2 over the tunnel
```

## File: tools.md
```
# `pydantic_ai.tools`

::: pydantic_ai.tools

```

## File: toolsets.md
```
# `pydantic_ai.toolsets`

::: pydantic_ai.toolsets
    options:
        members:
        - AbstractToolset
        - CombinedToolset
        - ExternalToolset
        - ApprovalRequiredToolset
        - FilteredToolset
        - FunctionToolset
        - IncludeReturnSchemasToolset
        - DeferredLoadingToolset
        - PrefixedToolset
        - RenamedToolset
        - SetMetadataToolset
        - PreparedToolset
        - WrapperToolset
        - ToolsetFunc

::: pydantic_ai.toolsets.fastmcp

```

## File: usage.md
```
# `pydantic_ai.usage`

::: pydantic_ai.usage

```

## File: util.md
```
# Util

Utility API for third-party implementations of the dispatcher API.

## `parseHeaders(headers, [obj])`

Receives a header object and returns the parsed value.

Arguments:

- **headers** `(Buffer | string | (Buffer | string)[])[]` (required) - Header object.

- **obj** `Record<string, string | string[]>` (optional) - Object to specify a proxy object. The parsed value is assigned to this object. But, if **headers** is an object, it is not used.

Returns: `Record<string, string | string[]>` If **obj** is specified, it is equivalent to **obj**.

## `headerNameToString(value)`

Retrieves a header name and returns its lowercase value.

Arguments:

- **value** `string | Buffer` (required) - Header name.

Returns: `string`

```

## File: websocket.md
```
# Class: WebSocket

Extends: [`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)

The WebSocket object provides a way to manage a WebSocket connection to a server, allowing bidirectional communication. The API follows the [WebSocket spec](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) and [RFC 6455](https://datatracker.ietf.org/doc/html/rfc6455).

## `new WebSocket(url[, protocol])`

Arguments:

* **url** `URL | string`

### WebSocketInit

When passing an object as the second argument, the following options are available:

* **protocols** `string | string[]` (optional) - Subprotocol(s) to request the server use.
* **headers** `HeadersInit` (optional) - Custom headers to include in the WebSocket handshake request.

### Example:

This example will not work in browsers or other platforms that don't allow passing an object.

```js
import { WebSocket, ProxyAgent } from 'undici'

const proxyAgent = new ProxyAgent('my.proxy.server')

const ws = new WebSocket('wss://echo.websocket.events', {
  dispatcher: proxyAgent,
  protocols: ['echo', 'chat']
})
```

If you do not need a custom Dispatcher, it's recommended to use the following pattern:

```js
import { WebSocket } from 'undici'

const ws = new WebSocket('wss://echo.websocket.events', ['echo', 'chat'])
```

### Example with HTTP/2:

> ⚠️ Warning: WebSocket over HTTP/2 is experimental, it is likely to change in the future.

> 🗒️ Note: WebSocket over HTTP/2 may be enabled by default in a future version,
> this will happen by enabling HTTP/2 connections as the default behavior of Undici's Agent as well the global dispatcher.
> Stay tuned to the changelog for more information.

This example will not work in browsers or other platforms that don't allow passing an object.

```js
import { Agent } from 'undici'

const agent = new Agent({ allowH2: true })

const ws = new WebSocket('wss://echo.websocket.events', {
  dispatcher: agent,
  protocols: ['echo', 'chat']
})
```

# Class: WebSocketStream

> ⚠️ Warning: the WebSocketStream API has not been finalized and is likely to change.

See [MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebSocketStream) for more information.

## `new WebSocketStream(url[, protocol])`

Arguments:

* **url** `URL | string`
* **options** `WebSocketStreamOptions` (optional)

### WebSocketStream Example

```js
const stream = new WebSocketStream('https://echo.websocket.org/')
const { readable, writable } = await stream.opened

async function read () {
  /** @type {ReadableStreamReader} */
  const reader = readable.getReader()

  while (true) {
    const { done, value } = await reader.read()
    if (done) break

    // do something with value
  }
}

async function write () {
  /** @type {WritableStreamDefaultWriter} */
  const writer = writable.getWriter()
  writer.write('Hello, world!')
  writer.releaseLock()
}

read()

setInterval(() => write(), 5000)

```

## ping(websocket, payload)
Arguments:

* **websocket** `WebSocket` - The WebSocket instance to send the ping frame on
* **payload** `Buffer|undefined` (optional) - Optional payload data to include with the ping frame. Must not exceed 125 bytes.

Sends a ping frame to the WebSocket server. The server must respond with a pong frame containing the same payload data. This can be used for keepalive purposes or to verify that the connection is still active.

### Example:

```js
import { WebSocket, ping } from 'undici'

const ws = new WebSocket('wss://echo.websocket.events')

ws.addEventListener('open', () => {
  // Send ping with no payload
  ping(ws)

  // Send ping with payload
  const payload = Buffer.from('hello')
  ping(ws, payload)
})
```

**Note**: A ping frame cannot have a payload larger than 125 bytes. The ping will only be sent if the WebSocket connection is in the OPEN state.

## Read More

- [MDN - WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [The WebSocket Specification](https://www.rfc-editor.org/rfc/rfc6455)
- [The WHATWG WebSocket Specification](https://websockets.spec.whatwg.org/)

```

## File: _DIR_IDENTITY.md
```
---
entity_type: "agent"
domain: "knowledge"
classification: "api"
parent_system: "oma"
---

# api

**Identity**: `api`
**Domain**: knowledge
**Clearance**: Level 3

Generated automatically via Phoenix V3 Pipeline.

```

## File: models\anthropic.md
```
# `pydantic_ai.models.anthropic`

## Setup

For details on how to set up authentication with this model, see [model configuration for Anthropic](../../models/anthropic.md).

::: pydantic_ai.models.anthropic

```

## File: models\base.md
```
# `pydantic_ai.models`

::: pydantic_ai.models
    options:
      members:
        - KnownModelName
        - ModelRequestParameters
        - Model
        - AbstractToolDefinition
        - StreamedResponse
        - ALLOW_MODEL_REQUESTS
        - check_allow_model_requests
        - override_allow_model_requests

```

## File: models\bedrock.md
```
# `pydantic_ai.models.bedrock`

## Setup

For details on how to set up authentication with this model, see [model configuration for Bedrock](../../models/bedrock.md).

::: pydantic_ai.models.bedrock

```

## File: models\cerebras.md
```
# `pydantic_ai.models.cerebras`

## Setup

For details on how to set up authentication with this model, see [model configuration for Cerebras](../../models/cerebras.md).

::: pydantic_ai.models.cerebras

```

## File: models\cohere.md
```
# `pydantic_ai.models.cohere`

## Setup

For details on how to set up authentication with this model, see [model configuration for Cohere](../../models/cohere.md).

::: pydantic_ai.models.cohere

```

## File: models\fallback.md
```
# pydantic_ai.models.fallback

::: pydantic_ai.models.fallback

```

## File: models\function.md
```
# `pydantic_ai.models.function`

A model controlled by a local function.

[`FunctionModel`][pydantic_ai.models.function.FunctionModel] is similar to [`TestModel`](test.md),
but allows greater control over the model's behavior.

Its primary use case is for more advanced unit testing than is possible with `TestModel`.

Here's a minimal example:

```py {title="function_model_usage.py" call_name="test_my_agent" noqa="I001"}
from pydantic_ai import Agent
from pydantic_ai import ModelMessage, ModelResponse, TextPart
from pydantic_ai.models.function import FunctionModel, AgentInfo

my_agent = Agent('openai:gpt-5.2')


async def model_function(
    messages: list[ModelMessage], info: AgentInfo
) -> ModelResponse:
    print(messages)
    """
    [
        ModelRequest(
            parts=[
                UserPromptPart(
                    content='Testing my agent...',
                    timestamp=datetime.datetime(...),
                )
            ],
            timestamp=datetime.datetime(...),
            run_id='...',
        )
    ]
    """
    print(info)
    """
    AgentInfo(
        function_tools=[],
        allow_text_output=True,
        output_tools=[],
        model_settings=None,
        model_request_parameters=ModelRequestParameters(
            function_tools=[], builtin_tools=[], output_tools=[]
        ),
        instructions=None,
    )
    """
    return ModelResponse(parts=[TextPart('hello world')])


async def test_my_agent():
    """Unit test for my_agent, to be run by pytest."""
    with my_agent.override(model=FunctionModel(model_function)):
        result = await my_agent.run('Testing my agent...')
        assert result.output == 'hello world'
```

See [Unit testing with `FunctionModel`](../../testing.md#unit-testing-with-functionmodel) for detailed documentation.

::: pydantic_ai.models.function

```

## File: models\google.md
```
# `pydantic_ai.models.google`

Interface that uses the [`google-genai`](https://pypi.org/project/google-genai/) package under the hood to
access Google's Gemini models via both the Generative Language API and Vertex AI.

## Setup

For details on how to set up authentication with this model, see [model configuration for Google](../../models/google.md).

::: pydantic_ai.models.google

```

## File: models\groq.md
```
# `pydantic_ai.models.groq`

## Setup

For details on how to set up authentication with this model, see [model configuration for Groq](../../models/groq.md).

::: pydantic_ai.models.groq

```

## File: models\huggingface.md
```
# `pydantic_ai.models.huggingface`

## Setup

For details on how to set up authentication with this model, see [model configuration for Hugging Face](../../models/huggingface.md).

::: pydantic_ai.models.huggingface

```

## File: models\instrumented.md
```
# pydantic_ai.models.instrumented

::: pydantic_ai.models.instrumented

```

## File: models\mcp_sampling.md
```
# pydantic_ai.models.mcp_sampling

::: pydantic_ai.models.mcp_sampling

```

## File: models\mistral.md
```
# `pydantic_ai.models.mistral`

## Setup

For details on how to set up authentication with this model, see [model configuration for Mistral](../../models/mistral.md).

::: pydantic_ai.models.mistral

```

## File: models\openai.md
```
# `pydantic_ai.models.openai`

## Setup

For details on how to set up authentication with this model, see [model configuration for OpenAI](../../models/openai.md).

::: pydantic_ai.models.openai

```

## File: models\openrouter.md
```
# `pydantic_ai.models.openrouter`

## Setup

For details on how to set up authentication with this model, see [model configuration for OpenRouter](../../models/openrouter.md).

::: pydantic_ai.models.openrouter

```

## File: models\outlines.md
```
# `pydantic_ai.models.outlines`

## Setup

For details on how to set up this model, see [model configuration for Outlines](../../models/outlines.md).

::: pydantic_ai.models.outlines

```

## File: models\test.md
```
# `pydantic_ai.models.test`

Utility model for quickly testing apps built with Pydantic AI.

Here's a minimal example:

```py {title="test_model_usage.py" call_name="test_my_agent" noqa="I001"}
from pydantic_ai import Agent
from pydantic_ai.models.test import TestModel

my_agent = Agent('openai:gpt-5.2', instructions='...')


async def test_my_agent():
    """Unit test for my_agent, to be run by pytest."""
    m = TestModel()
    with my_agent.override(model=m):
        result = await my_agent.run('Testing my agent...')
        assert result.output == 'success (no tool calls)'
    assert m.last_model_request_parameters.function_tools == []
```

See [Unit testing with `TestModel`](../../testing.md#unit-testing-with-testmodel) for detailed documentation.

::: pydantic_ai.models.test

```

## File: models\wrapper.md
```
# pydantic_ai.models.wrapper

::: pydantic_ai.models.wrapper

```

## File: models\xai.md
```
# `pydantic_ai.models.xai`

## Setup

For details on how to set up authentication with this model, see [model configuration for xAI](../../models/xai.md).

::: pydantic_ai.models.xai

```

## File: pydantic_evals\dataset.md
```
# `pydantic_evals.dataset`

::: pydantic_evals.dataset

```

## File: pydantic_evals\evaluators.md
```
# `pydantic_evals.evaluators`

::: pydantic_evals.evaluators

::: pydantic_evals.evaluators.llm_as_a_judge

```

## File: pydantic_evals\generation.md
```
# `pydantic_evals.generation`

::: pydantic_evals.generation

```

## File: pydantic_evals\lifecycle.md
```
# `pydantic_evals.lifecycle`

::: pydantic_evals.lifecycle

```

## File: pydantic_evals\online.md
```
# `pydantic_evals.online`

::: pydantic_evals.online

```

## File: pydantic_evals\otel.md
```
# `pydantic_evals.otel`

::: pydantic_evals.otel

```

## File: pydantic_evals\reporting.md
```
# `pydantic_evals.reporting`

::: pydantic_evals.reporting

```

## File: pydantic_graph\beta.md
```
# `pydantic_graph.beta`

::: pydantic_graph.beta

```

## File: pydantic_graph\beta_decision.md
```
# `pydantic_graph.beta.decision`

::: pydantic_graph.beta.decision

```

## File: pydantic_graph\beta_graph.md
```
# `pydantic_graph.beta.graph`

::: pydantic_graph.beta.graph

```

## File: pydantic_graph\beta_graph_builder.md
```
# `pydantic_graph.beta.graph_builder`

::: pydantic_graph.beta.graph_builder

```

## File: pydantic_graph\beta_join.md
```
# `pydantic_graph.beta.join`

::: pydantic_graph.beta.join

```

## File: pydantic_graph\beta_node.md
```
# `pydantic_graph.beta.node`

::: pydantic_graph.beta.node

```

## File: pydantic_graph\beta_step.md
```
# `pydantic_graph.beta.step`

::: pydantic_graph.beta.step

```

## File: pydantic_graph\exceptions.md
```
# `pydantic_graph.exceptions`

::: pydantic_graph.exceptions

```

## File: pydantic_graph\graph.md
```
# `pydantic_graph`

::: pydantic_graph.graph

```

## File: pydantic_graph\mermaid.md
```
# `pydantic_graph.mermaid`

::: pydantic_graph.mermaid

```

## File: pydantic_graph\nodes.md
```
# `pydantic_graph.nodes`

::: pydantic_graph.nodes
    options:
        members:
            - StateT
            - GraphRunContext
            - BaseNode
            - End
            - Edge
            - DepsT
            - RunEndT
            - NodeRunEndT

```

## File: pydantic_graph\persistence.md
```
# `pydantic_graph.persistence`

::: pydantic_graph.persistence

::: pydantic_graph.persistence.in_mem

::: pydantic_graph.persistence.file

```

## File: ui\ag_ui.md
```
# `pydantic_ai.ui.ag_ui`

::: pydantic_ai.ui.ag_ui

::: pydantic_ai.ui.ag_ui.app

```

## File: ui\base.md
```
# `pydantic_ai.ui`

::: pydantic_ai.ui

```

## File: ui\vercel_ai.md
```
# `pydantic_ai.ui.vercel_ai`

::: pydantic_ai.ui.vercel_ai

::: pydantic_ai.ui.vercel_ai.request_types

::: pydantic_ai.ui.vercel_ai.response_types

```

