---
id: github.com-jhuckaby-pixl-request-428a1637-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:15.468471
---

# KNOWLEDGE EXTRACT: github.com_jhuckaby_pixl-request_428a1637
> **Extracted on:** 2026-04-01 12:21:08
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521800/github.com_jhuckaby_pixl-request_428a1637

---

## File: `.npmignore`
```
.gitignore
node_modules/
test/test.log
```

## File: `README.md`
```markdown
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
	let { resp, data, perf } = await request.json('http://myserver.com/api', { 
		"foo": "test", 
		"bar": 123 
	});
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
request.json( 'http://myserver.com/api', { "foo": "test", "bar": 123 }, function(err, resp, data, perf) {
	if (err) throw(err);
	console.log("Status: " + resp.statusCode + " " + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

# Method List

Here are all the methods available in the request library:

| Method Name | Description |
|---------------|-------------|
| [get()](#http-get) | Performs an HTTP GET request. |
| [head()](#http-head) | Performs an HTTP HEAD request. |
| [post()](#http-post) | Performs an HTTP POST request. |
| [put()](#http-put) | Performs an HTTP PUT request. |
| [delete()](#http-delete) | Performs an HTTP DELETE request. |
| [json()](#json-rest-api) | Sends a request to a JSON REST API endpoint and parses the response. |
| [xml()](#xml-rest-api) | Sends a request to an XML REST API endpoint and parses the response. |
| [setHeader()](#default-headers) | Overrides or adds a default header for future requests. |
| [setTimeout()](#handling-timeouts) | Overrides the default time-to-first-byte timeout (milliseconds). |
| [setConnectTimeout()](#handling-timeouts) | Overrides the default DNS + socket connect timeout (milliseconds). |
| [setIdleTimeout()](#handling-timeouts) | Overrides the default socket idle timeout (milliseconds). |
| [setFollow()](#automatic-redirects) | Overrides the default behavior for following redirects. |
| [setAutoDecompress()](#compressed-responses) | Overrides the default behavior of decompressing responses. |
| [setDNSCache()](#dns-caching) | Enable DNS caching and set the TTL in seconds. |
| [flushDNSCache()](#flushing-the-cache) | Flush all IPs from the internal DNS cache. |

# Request Types

Here are all the request types supported by the library.

## HTTP GET

```
PROMISE request.get( URL );
PROMISE request.get( URL, OPTIONS );
```

To perform a simple HTTP GET, call the `get()` method.  All you need to provide is the URL, and the result is an object containing the response (headers and such), data (as a buffer), and performance data:

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
	if (err) throw(err);
	console.log("Status: " + resp.statusCode + " " + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

The result of the operation is an object containing the HTTP response object from Node ([IncomingMessage](https://nodejs.org/api/http.html#class-httpincomingmessage)), a data buffer of the content (if any), and a [performance tracker](#performance-metrics).

With async or promise usage, if an error occurs it is thrown.  Note that an "error" in this case is something like a TCP connection failure, DNS lookup failure, socket timeout, connection aborted, or other internal client library failure.  By default, HTTP response codes like 404 or 500 are *not* considered errors, so make sure to look at `resp.statusCode` if you are expecting an HTTP 200.  However, if you *want* non-200 response codes to be considered errors, see [Automatic Errors](#automatic-errors) below.

To specify additional options, such as custom request headers or HTTP authentication, include an object after the URL:

```js
try {
	let { resp, data, perf } = await request.get( 'https://www.bitstamp.net/api/ticker/', {
		"headers": {
			"X-Custom-Header": "My custom value"	
		},
		"auth": "username:password"
	});
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
request.get( 'https://www.bitstamp.net/api/ticker/', {
	"headers": {
		"X-Custom-Header": "My custom value"	
	},
	"auth": "username:password"
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + " " + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Check out the Node [http.request()](https://nodejs.org/api/http.html#httprequesturl-options-callback) documentation for all the properties you can pass in the options object.

By default, connections are closed at the end of each request.  If you want to reuse a persistent connection across multiple requests, see the [Keep-Alives](#keep-alives) section below.

## HTTP HEAD

```
PROMISE request.head( URL )
PROMISE request.head( URL, OPTIONS )
```

An HTTP HEAD request will not contain any data in the response, only the response code and headers.  Example:

```js
try {
	let { resp, perf } = await request.head( 'http://myserver.com/index.html' );
	console.log("Status: " + resp.statusCode + " " + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
request.head( 'http://myserver.com/index.html', function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + " " + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

## HTTP POST

```
PROMISE request.post( URL, OPTIONS )
```

To perform a HTTP POST, call the `post()` method.  Provide a URL, and an options object with a `data` property containing your key/value pairs:

```js
try {
	let { resp, data, perf } = await request.post( 'http://myserver.com/api/post', {
		"data": {
			"full_name": "Fred Smith", 
			"gender": "male",
			"age": 35
		}
	});
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
request.post( 'http://myserver.com/api/post', {
	"data": {
		"full_name": "Fred Smith", 
		"gender": "male",
		"age": 35
	}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Your key/value pairs will be serialized using the `application/x-www-form-urlencoded` format.  For a multipart post, see [Multipart POST](#multipart-post) below.

The result of the operation is an object containing the HTTP response object from Node ([IncomingMessage](https://nodejs.org/api/http.html#class-httpincomingmessage)), a data buffer of the content (if any), and a [performance tracker](#performance-metrics).

With async or promise usage, if an error occurs it is thrown.  Note that an "error" in this case is something like a TCP connection failure, DNS lookup failure, socket timeout, connection aborted, or other internal client library failure.  By default, HTTP response codes like 404 or 500 are *not* considered errors, so make sure to look at `resp.statusCode` if you are expecting an HTTP 200.  However, if you *want* non-200 response codes to be considered errors, see [Automatic Errors](#automatic-errors) below.

Check out the Node [http.request()](https://nodejs.org/api/http.html#httprequesturl-options-callback) documentation for all the properties you can pass in the options object.

By default, connections are closed at the end of each request.  If you want to reuse a persistent connection across multiple requests, see the [Keep-Alives](#keep-alives) section below.

### Pure Data POST

To specify your own raw POST data without any key/value pre-formatting, simply pass a `Buffer` object as the `data` property value, then include your own `Content-Type` header in the `headers` object.  Example:

```js
let buf = Buffer.from("VGhpcyBpcyBhIHRlc3QhIPCfmJw=", "base64");

try {
	let { resp, data, perf } = await request.post( 'http://myserver.com/api/post', {
		"data": buf,
		"headers": {
			"Content-Type": "application/octet-stream"
		}
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
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
let buf = Buffer.from("VGhpcyBpcyBhIHRlc3QhIPCfmJw=", "base64");

request.post( 'http://myserver.com/api/post', {
	"data": buf,
	"headers": {
		"Content-Type": "application/octet-stream"
	}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

### Multipart POST

For a `multipart/form-data` post, which is typically better for binary data, all you need to do is pass in a `multipart` property in your options object, and set it to a true value.  Everything else is the same as a standard [HTTP POST](#http-post):

```js
try {
	let { resp, data, perf } = await request.post( 'http://myserver.com/api/post', {
		"multipart": true, // activate multipart/form-data
		"data": {
			"foo": Buffer.from("Joe was here!"), 
			"bar": 54321
		}
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
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
request.post( 'http://myserver.com/api/post', {
	"multipart": true, // activate multipart/form-data
	"data": {
		"foo": Buffer.from("Joe was here!"), 
		"bar": 54321
	}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Note that you can use [Buffer](https://nodejs.org/api/buffer.html) objects instead of strings for your data values.

### File Uploads

To upload files, use `post()` and include a `files` object with your options, containing key/pair pairs.  Each file needs an identifier key (POST field name), and a value which should be a path to the file on disk:

```js
try {
	let { resp, data, perf } = await request.post( 'http://myserver.com/api/upload', {
		"files": {
			"kitten1": "/images/SillyKitten1.jpg",
			"kitten2": "/images/SillyKitten2.jpg"
		}
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
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
request.post( 'http://myserver.com/api/upload', {
	"files": {
		"kitten1": "/images/SillyKitten1.jpg",
		"kitten2": "/images/SillyKitten2.jpg"
	}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

The file path can also be a readable stream, if you happen to have one of those already open:

```js
let stream = fs.createReadStream('/images/SillyKitten1.jpg');

try {
	let { resp, data, perf } = await request.post( 'http://myserver.com/api/upload', {
		"files": {
			"file1": stream
		}
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
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
let stream = fs.createReadStream('/images/SillyKitten1.jpg');

request.post( 'http://myserver.com/api/upload', {
	"files": {
		"file1": stream
	}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

If you want to customize the filename of the uploaded file, set your file value to an array, with the first element containing the file path (or a stream), and the second element the desired filename:

```js
"files": {
	"file1": ["/images/SillyKitten1.jpg", "A-New-Filename.JPG"]
}
```

You can combine file uploads with other POST data fields, just by including a `data` property in your options, similar to a standard HTTP POST.  You can of course include any other options keys as well, such as custom headers:

```js
try {
	let { resp, data, perf } = await request.post( 'http://myserver.com/api/post', {
		"files": {
			"file1": "/images/SillyKitten1.jpg"
		},
		"data": {
			"foo": Buffer.from("Joe was here!"), 
			"bar": 54321
		},
		"headers": {
			"X-Custom-Header": "My custom value"	
		}
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
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
request.post( 'http://myserver.com/api/post', {
	"files": {
		"file1": "/images/SillyKitten1.jpg"
	},
	"data": {
		"foo": Buffer.from("Joe was here!"), 
		"bar": 54321
	},
	"headers": {
		"X-Custom-Header": "My custom value"	
	}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Including a `files` property automatically sets `multipart/form-data` mode, so you don't need to include the `multipart` boolean flag in this case.

## HTTP PUT

```
PROMISE request.put( URL, OPTIONS )
```

To send an `HTTP PUT`, you can use the `put()` method.  This works identically to `post()` in every way, except that the HTTP method is changed from `POST` to `PUT`.  You can send all the various data types, upload files, etc.  Example:

```js
try {
	let { resp, data, perf } = await request.put( 'http://myserver.com/api/put', {
		"data": {
			"full_name": "Fred Smith", 
			"gender": "male",
			"age": 35
		}
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
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
request.put( 'http://myserver.com/api/put', {
	"data": {
		"full_name": "Fred Smith", 
		"gender": "male",
		"age": 35
	}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Note that data (i.e. request body) is optional, and can be omitted.

## HTTP DELETE

```
PROMISE request.delete( URL, OPTIONS )
```

To send an `HTTP DELETE`, you can use the `delete()` method.  This works identically to `post()` in every way, except that the HTTP method is changed from `POST` to `DELETE`.  You can send all the various data types, upload files, etc.  Example:

```js
try {
	let { resp, data, perf } = await request.delete( 'http://myserver.com/api/delete', {
		"data": {
			"username": "fsmith"
		}
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
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
request.delete( 'http://myserver.com/api/delete', {
	"data": {
		"username": "fsmith"
	}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Note that data (i.e. request body) is optional, and can be omitted.

## File Downloads

If you want to download the response data to a file, instead of loading it all into an in-memory Buffer object, you can specify a `download` property in your `options` object, passed to either `get()` or `post()`.  Set this property to a filesystem path, and a file will be created and written to.  Example:

```js
try {
	let { resp, perf } = await request.get( 'https://upload.wikimedia.org/wikipedia/commons/9/9b/Gustav_chocolate.jpg', {
		"download": "/var/tmp/myimage.jpg"
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
request.get( 'https://upload.wikimedia.org/wikipedia/commons/9/9b/Gustav_chocolate.jpg', {
	"download": "/var/tmp/myimage.jpg"
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

The promise will only be resolved when the file is *completely* downloaded and written to the stream.  If the response is encoded (compressed), this is handled transparently for you using an intermediate stream.  Your file will contain the final decompressed data, and no memory will be used.

Alternatively, if you already have an open writable stream object, you can pass that to the `download` property.  Example:

```js
let stream = fs.createWriteStream( '/var/tmp/myimage.jpg' );

try {
	let { resp, perf } = await request.get( 'https://upload.wikimedia.org/wikipedia/commons/9/9b/Gustav_chocolate.jpg', {
		"download": stream
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
let stream = fs.createWriteStream( '/var/tmp/myimage.jpg' );

request.get( 'https://upload.wikimedia.org/wikipedia/commons/9/9b/Gustav_chocolate.jpg', {
	"download": stream
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + " " + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

### Advanced Stream Control

If you need more control over the response stream, you can provide a `preflight` property in your `options` object, passed to either `get()` or `post()`.  Set this property to a callback function, which will be called *before* the data is downloaded, but *after* the HTTP response headers are parsed.  This allows you to essentially intercept the response and set up your own stream pipe.  Example:

```js
let stream = fs.createWriteStream( '/var/tmp/myimage.jpg' );

try {
	let { resp, perf } = await request.get( 'https://upload.wikimedia.org/wikipedia/commons/9/9b/Gustav_chocolate.jpg', {
		"download": stream,
		"preflight": function(err, resp) {
			// setup stream pipe ourselves
			resp.pipe( stream );
			return true;
		}
	});
	console.log("Status: " + resp.statusCode + " " + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
let stream = fs.createWriteStream( '/var/tmp/myimage.jpg' );

request.get( 'https://upload.wikimedia.org/wikipedia/commons/9/9b/Gustav_chocolate.jpg', {
	"download": stream,
	"preflight": function(err, resp) {
		// setup stream pipe ourselves
		resp.pipe( stream );
		return true;
	}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + " " + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Your `preflight` function can optionally return `false`, which will inform the library that you did not set up a stream pipe, and it should resolve the promise with a data buffer instead.

## Progress Updates

If you would like to receive progress updates during a file download or large data transfer, add a `progress` property to your options object, and set it to a callback function.  Your function will be called repeatedly during the data transfer, and be passed the current data chunk as a buffer, and the HTTP response object from Node ([IncomingMessage](https://nodejs.org/api/http.html#class-httpincomingmessage)).  Example use:

```js
try {
	let { resp, perf } = await request.get( 'https://upload.wikimedia.org/wikipedia/commons/9/9b/Gustav_chocolate.jpg', {
		"download": "/var/tmp/myimage.jpg"
		"progress": function(chunk, resp) {
			// called repeatedly during download
			console.log( "Got chunk, " + chunk.length + " bytes" );
		}
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
request.get( 'https://upload.wikimedia.org/wikipedia/commons/9/9b/Gustav_chocolate.jpg', {
	"download": "/var/tmp/myimage.jpg",
	"progress": function(chunk, resp) {
			// called continuously during download
			console.log( "Got chunk, " + chunk.length + " bytes of " + resp.headers['content-length'] );
		}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Note that progress events only fire on data *received* (i.e. downloaded).

## Keep-Alives

To reuse the same socket connection across multiple requests, you have two options.  First, you can use the built-in Keep-Alive handler by calling the `setKeepAlive()` method and passing `true`.  Example:

```js
request.setKeepAlive( true );
```

This will attempt to use HTTP Keep-Alives for all HTTP and HTTPS requests, by using two global [http.Agent](https://nodejs.org/api/http.html#class-httpagent) objects (one per protocol).  Note that you can configure the options passed to the agents by specifying them as a secondary object to the `setKeepAlive()` method:

```js
request.setKeepAlive( true, {
	keepAlive: true,
	keepAliveMsecs: 1000,
	maxSockets: 256,
	maxFreeSockets: 256,
	timeout: 5000
} );
```

Alternatively, you can use your own [http.Agent](https://nodejs.org/api/http.html#class-httpagent) object (provided by Node).  Simply construct an instance, set the `keepAlive` property to `true`, and pass it into the options object for your requests, using the `agent` property:

```js
let http = require('http');
let agent = new http.Agent({ keepAlive: true });

try {
	let { resp, data, perf } = await request.get( 'http://myserver.com/api/get', {
		"agent": agent, // custom agent for connection pooling
		"headers": {
			"X-Custom-Header": "My custom value"	
		}
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
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
let http = require('http');
let agent = new http.Agent({ keepAlive: true });

request.get( 'http://myserver.com/api/get', {
	"agent": agent, // custom agent for connection pooling
	"headers": {
		"X-Custom-Header": "My custom value"	
	}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

You can then use the same `agent` object for subsequent requests on the same host (provided the server you are connecting to also supports Keep-Alives).

## JSON REST API

```
PROMISE request.json( URL, JSON )
PROMISE request.json( URL, JSON, OPTIONS )
```

The `json()` method is designed for sending requests to JSON REST APIs.  If you want to send a JSON REST style HTTP POST to an API endpoint, and expect to receive a JSON formatted response, this wraps up all the serialization and parsing for you.  Example:

```js
try {
	let { resp, data, perf } = await request.json( 'http://myserver.com/api', { 
		"foo": "test", 
		"bar": 123 
	} );
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
request.json( 'http://myserver.com/api', { "foo": "test", "bar": 123 }, function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

This will serialize the object into a JSON string, and send it as the HTTP POST data to the provided URL, with a Content-Type of `application/json`.  It also expects the response back from the server to be JSON, and will parse it for you.  The result will contain the HTTP response object ([IncomingMessage](https://nodejs.org/api/http.html#class-httpincomingmessage)), the parsed JSON object, and a [performance tracker](#performance-metrics).

You can also specify options such as custom request headers using this API.  Simply include an options object as the final argument (similar to the `get()` and `post()` methods).  Example:

```js
let json = {
	"foo": "test", 
	"bar": 123
};

try {
	let { resp, data, perf } = await request.json( 'http://myserver.com/api', json, {
		"headers": {
			"X-Custom-Header": "My custom value"	
		}
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
let json = {
	"foo": "test", 
	"bar": 123
};

request.json( 'http://myserver.com/api', json, {
	"headers": {
		"X-Custom-Header": "My custom value"	
	}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

If you pass `null` or `false` as the JSON data argument, the request will be sent as a `GET` instead of a `POST`.  You can also customize the HTTP method by passing a `method` property into the `options` object.  For example, the following would send as a `HTTP PUT` with the JSON serialized in the request body:

```js
let json = {
	"foo": "test", 
	"bar": 123
};

try {
	let { resp, data, perf } = await request.json( 'http://myserver.com/api', json, {
		"method": "PUT", // override the default method here
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
let json = {
	"foo": "test", 
	"bar": 123
};

request.json( 'http://myserver.com/api', json, {
	"method": "PUT", // override the default method here
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

You can also send a custom request method with no body:

```js
try {
	let { resp, data, perf } = await request.json( 'http://myserver.com/delete/user/345', false, {
		"method": "DELETE", // override the default method here
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
request.json( 'http://myserver.com/delete/user/345', false, {
	"method": "DELETE", // override the default method here
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

**Note:** If the server doesn't send back JSON, or it cannot be parsed, an error will be thrown.

## XML REST API

```
PROMISE request.xml( URL, XML )
PROMISE request.xml( URL, XML, OPTIONS )
```

The `xml()` method is designed for sending requests to XML REST APIs.  If you want to send a XML REST style HTTP POST to an API endpoint, and expect to receive a XML formatted response, this wraps up all the serialization and parsing for you.  Example:

```js
try {
	let { resp, data, perf } = await request.xml( 'http://myserver.com/api', { 
		"foo": "test", 
		"bar": 123 
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
request.xml( 'http://myserver.com/api', { "foo": "test", "bar": 123 }, function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

This will serialize the object into an XML document (using the [pixl-xml](https://www.github.com/jhuckaby/pixl-xml) package), and send it as the HTTP POST data to the provided URL, with a Content-Type of `text/xml`.  It also expects the response back from the server to be XML, and will parse it for you.  The result will contain the HTTP response object ([IncomingMessage](https://nodejs.org/api/http.html#class-httpincomingmessage)), the parsed XML document, and a [performance tracker](#performance-metrics).

You can also specify options such as custom request headers using this API.  Simply include an options object as the final argument (similar to the `get()` and `post()` methods).  Example:

```js
let xml = {
	"foo": "test", 
	"bar": 123
};

try {
	let { resp, data, perf } = await request.xml( 'http://myserver.com/api', xml, {
		"headers": {
			"X-Custom-Header": "My custom value"	
		}
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
let xml = {
	"foo": "test", 
	"bar": 123
};

request.xml( 'http://myserver.com/api', xml, {
	"headers": {
		"X-Custom-Header": "My custom value"	
	}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Please note that [pixl-xml](https://www.github.com/jhuckaby/pixl-xml) discards the XML root node element when parsing XML, and similarly the request library doesn't expect one when serializing.  Meaning, you should omit the XML root node element (just include the contents), and expect the server XML result to be parsed in a similar fashion.

For example, if you wanted to send this XML:

```xml
<?xml version="1.0"?>
<Document>
	<foo>test</foo>
	<bar>123</bar>
</Document>
```

Then just include an object with `foo` and `bar` properties:

```js
{
	"foo": "test", 
	"bar": 123
}
```

See the [pixl-xml](https://www.github.com/jhuckaby/pixl-xml) documentation for details, including how to include attributes, etc.

By default, the XML will be serialized to a document with `<Request>` as the root node name.  However if you are posting to an API that requires a specific XML root node name, you can set it with the `xmlRootNode` property in the options object.  Example of this:

```js
let xml = {
	"foo": "test", 
	"bar": 123
};

try {
	let { resp, data, perf } = await request.xml( 'http://myserver.com/api', xml, {
		"xmlRootNode": "Document"
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
let xml = {
	"foo": "test", 
	"bar": 123
};

request.xml( 'http://myserver.com/api', xml, {
	"xmlRootNode": "Document"
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

If you pass `null` or `false` as the XML data argument, the request will be sent as a `GET` instead of a `POST`.  You can also customize the HTTP method by passing a `method` property into the `options` object.  For example, the following would send as a `HTTP PUT` with the XML serialized in the request body:

```js
let xml = {
	"foo": "test", 
	"bar": 123
};

try {
	let { resp, data, perf } = await request.xml( 'http://myserver.com/api', xml, {
		"method": "PUT", // override the default method here
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
let xml = {
	"foo": "test", 
	"bar": 123
};

request.xml( 'http://myserver.com/api', xml, {
	"method": "PUT", // override the default method here
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

You can also send a custom request method with no body:

```js
try {
	let { resp, data, perf } = await request.xml( 'http://myserver.com/delete/user/234', false, {
		"method": "DELETE", // override the default method here
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
request.xml( 'http://myserver.com/delete/user/234', false, {
	"method": "DELETE", // override the default method here
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

**Note:** If the server doesn't send back XML, or it cannot be parsed, an error will be thrown.

# Default Headers

By default the request library will add the following outgoing headers to every request:

```
User-Agent: PixlRequest 1.0.0
Accept-Encoding: gzip, deflate, br
```

You can override these by passing in custom headers with your request:

```js
try {
	let { resp, data, perf } = await request.post( 'http://myserver.com/api/post', {
		"headers": {
			"User-Agent": "My Request Library!",
			"Accept-Encoding": "none"
		},
		"data": {
			"full_name": "Fred Smith", 
			"gender": "male",
			"age": 35
		}
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
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
request.post( 'http://myserver.com/api/post', {
	"headers": {
		"User-Agent": "My Request Library!",
		"Accept-Encoding": "none"
	},
	"data": {
		"full_name": "Fred Smith", 
		"gender": "male",
		"age": 35
	}
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Or by overriding your class instance defaults before making a request:

```js
request.setHeader( "Accept-Encoding", "none" );
```

You can also replace the entire header set by rewriting the `defaultHeaders` property:

```js
request.defaultHeaders = {
	"User-Agent": "My Request Library!",
	"Accept-Encoding": "none"
};
```

# Handling Timeouts

PixlRequest handles timeouts in three different ways.  First is connect timeout, which includes DNS lookup time plus socket connect time.  Second, by measuring the "time to first byte" (TTFB), from the start of the request.  This is *not* an idle timeout, and *not* a connect timeout -- it is the maximum amount of time allowed from the start of the request, to the first byte received.  Separately, it can also track an idle socket timeout during sending and receiving.  You can set each timeout separately.

The default connect timeout is 10 seconds, while the TTFB timeout and idle timeout defaults are 30 seconds each.  You can customize these per request by including `connectTimeout`, `timeout` and/or `idleTimeout` properties with your options object, and setting them to a number of milliseconds:

```js
try {
	let { resp, data, perf } = await request.post( 'http://myserver.com/api/post', {
		"data": {
			"full_name": "Fred Smith", 
			"gender": "male",
			"age": 35
		},
		"connectTimeout": 3 * 1000, // 3 second connect timeout (DNS + socket connect)
		"timeout": 10 * 1000, // 10 second TTFB timeout
		"idleTimeout": 5 * 1000 // 5 second idle timeout
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
request.post( 'http://myserver.com/api/post', {
	"data": {
		"full_name": "Fred Smith", 
		"gender": "male",
		"age": 35
	},
	"connectTimeout": 3 * 1000, // 3 second connect timeout (DNS + socket connect)
	"timeout": 10 * 1000, // 10 second TTFB timeout
	"idleTimeout": 5 * 1000 // 5 second idle timeout
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Or you can set default timeouts for all requests on your class instance, using the `setConnectTimeout()`, `setTimeout()` and `setIdleTimeout()` methods:

```js
request.setConnectTimeout( 3 * 1000 ); // 3 seconds (DNS + socket connect)
request.setTimeout( 10 * 1000 ); // 10 seconds
request.setIdleTimeout( 5 * 1000 ); // 5 seconds
```

When a timeout occurs, an `error` event is emitted.  The error message will follow one of these formats, depending on which timeout was fired: 

```
Connect Timeout (### ms)
Request Timeout (### ms)
Idle Timeout (### ms)
```

Note that any timeout results in the socket being destroyed (i.e. [request.destroy()](https://nodejs.org/api/http.html#requestdestroyerror) is called on the request object, which in turn destroys the socket).

# Automatic Redirects

The default behavior for handling redirect responses (i.e. `HTTP 302` and friends) is to *not* follow them automatically, and instead return the original 3xx response.  You can change this by including a `follow` property with your options object, and setting it to the maximum number of redirects you want to allow:

```js
try {
	let { resp, data, perf } = await request.post( 'http://myserver.com/api/post', {
		"data": {
			"full_name": "Fred Smith", 
			"gender": "male",
			"age": 35
		},
		"follow": 2, // auto-follow up to 2 redirects
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
request.post( 'http://myserver.com/api/post', {
	"data": {
		"full_name": "Fred Smith", 
		"gender": "male",
		"age": 35
	},
	"follow": 2, // auto-follow up to 2 redirects
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: ", data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Alternatively, you can set a class instance default by calling the `setFollow()` method:

```js
request.setFollow( 2 ); // auto-follow up to 2 redirects
```

If you want to follow an unlimited number of redirects, set this to boolean `true` (not advised).  To disable the auto-follow behavior, set it to `0` or `false`.

The library recognizes HTTP codes 301, 302, 307 and 308 as "redirect" responses, as long as a `Location` header accompanies them.

# Automatic Errors

When using `get()` or `post()`, HTTP response codes like 404 or 500 are *not* considered errors, so you have to look at `resp.statusCode` if you are expecting an HTTP 200.  However, this is configurable.  If you would like all non-200 response codes to be considered errors, call the `setAutoError()` method and pass `true`.  Example:

```js
request.setAutoError( true );
```

Note that if you allow [redirects](#automatic-redirects), they will not generate an error.

To customize which response codes are considered "successful" and should *not* generate an error, call the `setSuccessMatch()` method, and pass in a new one.  The default match is shown here, which considered any HTTP response code in the 200 - 299 range to be successful:

```js
request.setSuccessMatch( /^2\d\d$/ );
```

Note that this regular expression also affects the [json()](#json-rest-api) and [xml()](#xml-rest-api) wrapper methods.

# Automatic Retries

By default errors are not retried, and the promise is resolved immediately on the first error.  However, you can enable automatic retries by either including a `retries` property in your options object (set to the maximum number of retries you want to allow), or by calling the `setRetries()` method, and specifying the maximum amount for all requests:

```js
request.setRetries( 5 );
```

This example would make up to 6 total attempts (the initial attempt plus up to 5 retries), before ultimately failing the operation and resolving the promise with the last error encountered.

For the purpose of automatic retries an "error" is considered to be any core error emitted on the request object, such as a DNS lookup failure, TCP connect failure, socket timeout, or any HTTP response code in the `5xx` range (500 - 599), such as an `Internal Server Error`.  Any other errors, for example anything in the `4xx` range, are *not* retried, as they are typically considered to be more permanent.

## Exponential Backoff

By default, retries are attempted immediately.  To set a retry delay, you can do it globally:

```js
request.setRetryDelay( 250 );
request.setRetryDelayMax( 4000 );
```

Or you can set it per request in the `options` object, using `retryDelay` and `retryDelayMax` properties (both in milliseconds).

Either way, for each retry after the first one, the retry delay is doubled, up to but not exceeding the max.  So in the above example it would wait 250ms, 500ms, 1s, 2s, then 4s.  If not specified, the default maximum retry delay is 30s.

# Compressed Responses

The request library automatically handles Brotli, Gzip and Deflate encoded responses that come back from the remote server.  These are transparently decoded for you.  However, you should know that by default all outgoing requests include an `Accept-Encoding: gzip, deflate, br` header, which broadcasts our support for it.  If you do not want responses to be compressed, you can unset this header.  See the [Default Headers](#default-headers) section above.

Alternately, if you would prefer that the library not do anything regarding compression, and pass the compressed response directly through without touching it, call the `setAutoDecompress()` method, and pass in `false`:

```js
request.setAutoDecompress( false );
```

# Abort Signals

If you have a long-running request that you may want to abort in the middle, you can use a Node.js [AbortController](https://nodejs.org/api/globals.html#class-abortcontroller).  Just pass in the `signal` property from your controller into the request options object, and then you can call `abort()` on the controller whenever you want.  Example:

```js
const controller = new AbortController();

// abort after 500ms
setTimeout( function() {
	controller.abort();
}, 500 );

// send long request
try {
	let { resp, data, perf } = await request.get( 'http://myserver.com/some/large/file.mp4', {
		"signal": controller.signal // our abort signal here
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Performance: ", perf.metrics());
}
catch (err) {
	throw err;
}
```

<details><summary><strong>Example using callback</strong></summary>

```js
const controller = new AbortController();

// abort after 500ms
setTimeout( function() {
	controller.abort();
}, 500 );

// send long request
request.get( 'http://myserver.com/some/large/file.mp4', {
	"signal": controller.signal // our abort signal here
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Note that abort signals are designed to abort requests that have already received the "first byte".  Meaning, we already received the response headers, and are streaming down the data.  That's the phase of the request that is "abortable".

# Performance Metrics

The request library keeps high resolution performance metrics on every HTTP request, including the DNS lookup time, socket connect time, request send time, wait time, receive time, decompress time, and total elapsed time.  These are all tracked using the [pixl-perf](https://www.github.com/jhuckaby/pixl-perf) module, and included in the result object for all operations.  Example use:

```js
try {
	let { resp, data, perf } = await request.get( 'https://www.bitstamp.net/api/ticker/' );
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
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
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

This would output something like the following:

```
Status: 200 OK
Performance: { 
  scale: 1000,
  perf: { 
     total: 548.556,
     dns: 25.451,
     connect: 120.155,
     send: 270.92,
     wait: 122.2,
     receive: 3.462,
     decompress: 4.321 
  },
  counters: { 
    bytes_sent: 134, 
    bytes_received: 749 
  } 
}
```

All the `perf` values are in milliseconds (represented by the `scale`).  Here are descriptions of all the metrics:

| Metric | Description |
|--------|-------------|
| `dns` | Time to resolve the hostname to an IP address via DNS.  Omitted if cached, or you specify an IP on the URL. |
| `connect` | Time to connect to the remote socket (omitted if using Keep-Alives and reusing a host). |
| `send` | Time to send the request data (typically for POST / PUT).  Also includes SSL handshake time (if HTTPS). |
| `wait` | Time spent waiting for the server response (after request is sent). |
| `receive` | Time spent downloading data from the server (after headers received). |
| `decompress` | Time taken to decompress the response (if encoded with Brotli, Gzip or Deflate). |
| `total` | Total time of the entire HTTP transaction. |

As indicated above, some of the properties may be omitted depending on the situation.  For example, if you are using a shared [http.Agent](https://nodejs.org/api/http.html#class-httpagent) with Keep-Alives, then subsequent requests to the same host won't perform a DNS lookup or socket connect, so those two metrics will be omitted.  Similarly, if the response from the server isn't compressed, then the `decompress` metric will be omitted.

Note that the `send` metric includes the SSL / TLS handshake time, if using HTTPS.  Also, this metric may be `0` if using plain HTTP GET or HEAD, as it is mainly used to measure the POST or PUT data send time (i.e. uploading file data).

The `bytes_sent` and `bytes_received` values in the `counters` object represent the total amount of raw bytes sent and received over the socket.  This includes the raw request line and request/response headers.

See the [pixl-perf](https://www.github.com/jhuckaby/pixl-perf) module for more details.

# DNS Caching

You can optionally have the library cache DNS lookups in RAM, for faster subsequent requests on the same hostnames.  You can also specify the TTL (time to live) to control how long hostnames will be cached.  This means it will only request a DNS lookup for a given hostname once every N seconds.  To enable this feature, call `setDNSCache()` and specify the number of seconds for the TTL:

```js
request.setDNSCache( 300 ); // 5 minute TTL
```

This will cache hostnames and their IP addresses in RAM for 5 minutes.  Meaning, during that time subsequent requests to the same hostname will not require a DNS lookup.  After 5 minutes, the cache objects will expire, and the next request will perform another DNS lookup.

Note that while the feature can be enabled or disabled per request object, the DNS cache itself is global.  Meaning, it is shared by all `pixl-request` objects in the same process.

## Flushing the Cache

To flush the DNS cache (i.e. eject all the IPs from it), call the `flushDNSCache()` method.  Example:

```js
request.flushDNSCache();
```

# SSL Certificate Validation

If you are trying to connect to a host via HTTPS and getting certificate errors, you may have to bypass Node's SSL certification validation.  To do this, set the `rejectUnauthorized` options property to `false`.  Example:

```js
try {
	let { resp, data, perf } = await request.get( 'https://www.bitstamp.net/api/ticker/', {
		"rejectUnauthorized": false
	});
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
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
request.get( 'https://www.bitstamp.net/api/ticker/', {
	"rejectUnauthorized": false
}, 
function(err, resp, data, perf) {
	if (err) throw err;
	console.log("Status: " + resp.statusCode + ' ' + resp.statusMessage);
	console.log("Headers: ", resp.headers);
	console.log("Content: " + data);
	console.log("Performance: ", perf.metrics());
} );
```

</details>

Please only do this if you understand the security ramifications, and *completely trust* the host you are connecting to, and the network you are on.  Skipping the certificate validation step should really only be done in special circumstances, such as testing your own internal server with a self-signed cert.

# Proxy Servers

To send requests through a proxy, simply set one or more of the [de-facto standard environment variables](https://curl.se/docs/manpage.html#ENVIRONMENT) used for this purpose:

```
HTTPS_PROXY
HTTP_PROXY
ALL_PROXY
NO_PROXY
```

The pixl-request library will detect these environment variables and automatically configure proxy routing for your requests.  The environment variable names may be upper or lower-case.  The proxy format should be a fully-qualified URL with port number.  To set a single proxy server for handling both HTTP and HTTPS requests, the simplest way is to just set `ALL_PROXY` (usually specified via a plain HTTP URL with port).  Example:

```
ALL_PROXY=http://company-proxy-server.com:8080
```

Use the `NO_PROXY` environment variable to specify a comma-separated domain whitelist.  Requests to any of the domains on this list will bypass the proxy and be sent directly.  Example:

```
NO_PROXY=direct.example.com
```

Please note that for proxying HTTPS (SSL) requests, unless you have pre-configured your client machine to trust your proxy's local SSL cert, you will have to set the `rejectUnauthorized` option to `false` in your requests.  See [SSL Certificate Validation](#ssl-certificate-validation) above for details.

The types of proxies supported are:

| Protocol | Example |
|----------|---------|
| `http` | `http://proxy-server-over-tcp.com:3128` |
| `https` | `https://proxy-server-over-tls.com:3129` |
| `socks` | `socks://username:password@some-socks-proxy.com:9050` |
| `socks5` | `socks5://username:password@some-socks-proxy.com:9050` |
| `socks4` | `socks4://some-socks-proxy.com:9050` |
| `pac-*` | `pac+http://www.example.com/proxy.pac` |

# Access Control Lists

If you want to limit outbound requests to specific IP addresses or ranges, you can specify an IP ACL, in the form of a whitelist and/or blacklist.  The methods are `setWhitelist()` for a whitelist, and `setBlacklist()` for a blacklist.  IPv4 and IPv6 addresses and ranges are both supported, including single IPs, partial IPs, and [CIDR blocks](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).

For example, if you wanted to restrict requests to your local network, and disallow all public internet access, you could use a whitelist like this:

```js
request.setWhitelist( ["127.0.0.1", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16", "::1/128", "fd00::/8", "169.254.0.0/16", "fe80::/10"] );
```

Or, if you want to explicitly block access to a particular country like NK, you could use a blacklist:

```js
request.setBlacklist( ["175.45.176.0/22", "2405:8100::/32"] );
```

See [pixl-acl](https://github.com/jhuckaby/pixl-acl) for more details on the IP syntax.

# License

**The MIT License**

*Copyright (c) 2015 - 2025 Joseph Huckaby.*

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

## File: `package.json`
```json
{
	"name": "pixl-request",
	"version": "2.6.2",
	"description": "A very simple module for making HTTP requests.",
	"author": "Joseph Huckaby <jhuckaby@gmail.com>",
	"homepage": "https://github.com/jhuckaby/pixl-request",
	"license": "MIT",
	"main": "request.js",
	"repository": {
		"type": "git",
		"url": "https://github.com/jhuckaby/pixl-request"
	},
	"bugs": {
		"url": "https://github.com/jhuckaby/pixl-request/issues"
	},
	"keywords": [
		"http",
		"request",
		"upload",
		"multipart"
	],
	"dependencies": {
		"class-plus": "^2.0.0",
		"errno": "1.0.0",
		"form-data": "4.0.4",
		"pixl-acl": "^1.0.0",
		"pixl-perf": "^1.0.0",
		"pixl-xml": "^1.0.0",
		"proxy-agent": "6.5.0"
	},
	"devDependencies": {
		"async": "3.2.5",
		"pixl-unit": "^1.0.14",
		"pixl-server": "^1.0.42",
		"pixl-server-web": "^1.3.25"
	},
	"overrides": {
		"basic-ftp": "5.2.0"
	},
	"scripts": {
		"test": "pixl-unit test/test.js --verbose"
	}
}
```

## File: `request.js`
```javascript
// Very simple HTTP request library for Node.js
// Copyright (c) 2015 - 2024 Joseph Huckaby
// Released under the MIT License

const fs = require('fs');
const http = require('http');
const https = require('https');
const querystring = require('querystring');
const zlib = require('zlib');
const net = require("net");

const FormData = require('form-data');
const XML = require('pixl-xml');
const Class = require('class-plus');
const Perf = require('pixl-perf');
const ACL = require('pixl-acl');
const ErrNo = require('errno');
const { ProxyAgent } = require('proxy-agent');

// sniff for Brotli compression support, as it was added in Node v10.16
const hasBrotli = !!zlib.BrotliCompress;
const pixlAgent = "PixlRequest " + require('./package.json').version;

// sniff for proxy
const userProxyEnv = (process.env.http_proxy || process.env.https_proxy || process.env.all_proxy || process.env.HTTP_PROXY || process.env.HTTPS_PROXY || process.env.ALL_PROXY);

var dns_cache = {};
var http_common = require('_http_common');
var checkIsHttpToken = http_common._checkIsHttpToken;
var checkInvalidHeaderChar = http_common._checkInvalidHeaderChar;

module.exports = Class({
	
	__asyncify: {
		json: ['resp', 'data', 'perf'],
		xml: ['resp', 'data', 'perf'],
		get: ['resp', 'data', 'perf'],
		head: ['resp', 'data', 'perf'],
		post: ['resp', 'data', 'perf'],
		put: ['resp', 'data', 'perf'],
		delete: ['resp', 'data', 'perf'],
		request: ['resp', 'data', 'perf']
	},
	
	defaultHeaders: null,
	
	// default TTFB timeout of 30 seconds
	defaultTimeout: 30000,
	defaultConnectTimeout: 10000,
	defaultIdleTimeout: 30000,
	
	// do not follow redirects by default
	defaultFollow: false,
	followMatch: /^(301|302|307|308)$/,
	
	// do not cache DNS by default (TTL 0s)
	dnsTTL: 0,
	
	// http code success match for json/xml wrappers
	successMatch: /^2\d\d$/,
	
	// automatically decompress gzip/inflate compression on response
	autoDecompress: true,
	
	// generate errors if response code doesn't match successMatch
	autoError: false,
	
	// use pooled http/https agents for keep-alive connections
	autoAgent: false,
	
	// use proxy agent when specific env vars are present
	proxyAgent: false,
	
	// optional retries for certain kinds of transient network errors
	defaultRetries: false,
	defaultRetryDelay: 0,
	defaultRetryDelayMax: 30000,
	retryMatch: /^5\d\d$/,
	
	// automatically include Content-Length header where applicable
	// disable if you want chunked transfer encoding
	autoContentLength: true
	
},
class Request {
	
	constructor(useragent) {
		// class constructor
		this.defaultHeaders = {
			'Accept-Encoding': hasBrotli ? "gzip, deflate, br" : "gzip, deflate"
		};
		this.setUserAgent( useragent || pixlAgent );
	}
	
	setHeader(name, value) {
		// override or add a default header
		this.defaultHeaders[name] = value;
	}
	
	setUserAgent(useragent) {
		// override the default user agent string
		this.setHeader('User-Agent', useragent);
	}
	
	setTimeout(timeout) {
		// override the default first-byte timeout (milliseconds)
		this.defaultTimeout = timeout;
	}
	setConnectTimeout(timeout) {
		// override the default connect timeout (DNS + socket connect, milliseconds)
		this.defaultConnectTimeout = timeout;
	}
	setIdleTimeout(timeout) {
		// override the default socket idle timeout (milliseconds)
		this.defaultIdleTimeout = timeout;
	}
	
	setFollow(follow) {
		// override the default follow setting (boolean or int)
		// specify integer to set limit of max redirects to allow
		this.defaultFollow = follow;
	}
	
	setRetries(retries) {
		// override the default retry setting (boolean or int)
		// specify integer to set limit of max retries to allow
		this.defaultRetries = retries;
	}
	setRetryDelay(delay) {
		// override the default retry delay (ms)
		this.defaultRetryDelay = delay;
	}
	setRetryDelayMax(delay) {
		// override the default retry delay maximum (ms)
		this.defaultRetryDelayMax = delay;
	}
	
	setDNSCache(ttl) {
		// set a DNS cache TTL (seconds) or 0 to disable
		this.dnsTTL = ttl;
	}
	
	flushDNSCache() {
		// remove all IPs from the internal DNS cache
		dns_cache = {};
	}
	
	setSuccessMatch(regexp) {
		// set success match for http code (json/xml wrappers)
		this.successMatch = regexp;
	}
	
	setAutoDecompress(enabled) {
		// set auto decompress (boolean: enabled/disabled)
		this.autoDecompress = enabled;
	}
	
	setAutoError(enabled) {
		// set auto error mode (based on successMatch)
		this.autoError = enabled;
	}
	
	setKeepAlive(enabled, opts) {
		// set auto agent mode
		if (enabled && !this.autoAgent) {
			if (!opts) opts = { keepAlive: true };
			this.autoAgent = {
				http: new http.Agent(opts),
				https: new https.Agent(opts)
			};
		}
		else if (!enabled && this.autoAgent) {
			this.autoAgent.http.destroy();
			this.autoAgent.https.destroy();
			this.autoAgent = false;
		}
	}
	
	setAutoContentLength(enabled) {
		// automatically include Content-Length, or not
		this.autoContentLength = enabled;
	}
	
	setBlacklist(ips) {
		// blacklist certain IPs or ranges
		if (!ips) { delete this.blacklist; return; }
		this.blacklist = new ACL(ips);
	}
	
	setWhitelist(ips) {
		// whitelist certain IPs or ranges
		if (!ips) { delete this.whitelist; return; }
		this.whitelist = new ACL(ips);
	}
	
	json(url, data, options, callback) {
		// convenience method: get or post json, get json back
		var self = this;
		
		if (!callback) {
			// support 3-arg calling convention
			callback = options;
			options = {};
		}
		
		var method = '';
		if (data) {
			method = 'post';
			options.json = true;
			options.data = data;
		}
		else {
			method = 'get';
		}
		
		this[method]( url, options, function(err, res, data, perf) {
			// got response, check for dns/tcp error
			if (err) return callback( err, null, null, perf );
			
			// check for http error code
			if (self.autoError && !res.statusCode.toString().match(self.successMatch)) {
				err = new Error( "HTTP " + res.statusCode + " " + res.statusMessage + ": " + url );
				err.code = res.statusCode;
				err.headers = res.headers;
				err.url = url;
				return callback( err, res, data, perf );
			}
			
			// parse json in response
			var json = null;
			try { json = JSON.parse( data.toString() ); }
			catch (err) {
				return callback( err, res, data, perf );
			}
			
			// all good, send json object back
			callback( null, res, json, perf );
		} );
	}
	
	xml(url, data, options, callback) {
		// convenience method: get or post xml, get xml back
		var self = this;
		
		if (!callback) {
			// support 3-arg calling convention
			callback = options;
			options = {};
		}
		
		var method = '';
		if (data) {
			method = 'post';
			options.xml = true;
			options.data = data;
		}
		else {
			method = 'get';
		}
		
		this[method]( url, options, function(err, res, data, perf) {
			// got response, check for dns/tcp error
			if (err) return callback( err, null, null, perf );
			
			// check for http error code
			if (self.autoError && !res.statusCode.toString().match(self.successMatch)) {
				err = new Error( "HTTP " + res.statusCode + " " + res.statusMessage + ": " + url );
				err.code = res.statusCode;
				err.headers = res.headers;
				err.url = url;
				return callback( err, res, data, perf );
			}
			
			// parse xml in response
			var xml = null;
			try { xml = XML.parse( data.toString() ); }
			catch (err) {
				return callback( err, res, data, perf );
			}
			
			// all good, send xml object back
			callback( null, res, xml, perf );
		} );
	}
	
	get(url, options, callback) {
		// perform HTTP GET
		// callback will receive: err, res, data
		if (!callback) {
			// support two-argument calling convention: url and callback
			callback = options;
			options = {};
		}
		if (!options) options = {};
		if (!options.method) options.method = 'GET';
		this.request( url, options, callback );
	}
	
	head(url, options, callback) {
		// perform HTTP HEAD
		// callback will receive: err, res, data
		if (!callback) {
			// support two-argument calling convention: url and callback
			callback = options;
			options = {};
		}
		if (!options) options = {};
		if (!options.method) options.method = 'HEAD';
		this.request( url, options, callback );
	}
	
	post(url, options, callback) {
		// perform HTTP POST, raw data or key/value pairs
		// callback will receive: err, res, data
		var key;
		if (!options) options = {};
		if (!options.headers) options.headers = {};
		if (!options.data) {
			if (options.files) options.data = {};
			else options.data = '';
		}
		
		if (!options.method) options.method = 'POST';
		
		if (!options.data) {
			// non-data post (or custom method)
			delete options.data;
			return this.request( url, options, callback );
		}
		
		// see if we have a buffer, string or other
		var is_buffer = (options.data instanceof Buffer);
		var is_string = (typeof(options.data) == 'string');
		
		// if string, convert to buffer so content length is correct (unicode)
		if (is_string) {
			// support Node v0.12 and up
			options.data = Buffer.from(options.data);
			is_buffer = true;
			is_string = false;
		}
		
		if ((typeof(options.data) == 'object') && !is_buffer) {
			// serialize data into key/value pairs
			
			// allow URL to include data e.g. [data: Key: Value]
			url = url.replace(/\s*\[data\:\s*([\w\-]+)\:\s*([^\]]+)\]/ig, function(m_all, m_g1, m_g2) {
				if (m_g2.match(/^\-?\d+$/)) m_g2 = parseInt(m_g2);
				else if (m_g2.match(/^\-?\d+\.\d+$/)) m_g2 = parseFloat(m_g2);
				else if (m_g2.match(/^true$/)) m_g2 = true;
				else if (m_g2.match(/^false$/)) m_g2 = false;
				options.data[ m_g1 ] = m_g2;
				return '';
			}).trim();
			
			if (options.json) {
				// JSON REST
				options.data = JSON.stringify(options.data) + "\n";
				options.headers['Content-Type'] = 'application/json';
				delete options.json;
			}
			else if (options.xml) {
				// XML REST
				options.data = XML.stringify(options.data, options.xmlRootNode || 'Request') + "\n";
				options.headers['Content-Type'] = 'text/xml';
				delete options.xml;
				delete options.xmlRootNode;
			}
			else if (options.files || options.multipart) {
				// use FormData
				var form = new FormData();
				
				// POST params (strings or Buffers)
				for (key in options.data) {
					form.append(key, options.data[key]);
				}
				
				// file uploads
				if (options.files) {
					for (key in options.files) {
						var file = options.files[key];
						if (typeof(file) == 'string') {
							// simple file path, convert to readable stream
							form.append( key, fs.createReadStream(file) );
						}
						else if (Array.isArray(file)) {
							// array of [file path or stream or buffer, filename]
							var file_data = file[0];
							if (typeof(file_data) == 'string') file_data = fs.createReadStream(file_data);
							
							form.append( key, file_data, {
								filename: file[1]
							} );
						}
						else {
							// assume user knows what (s)he is doing (should be stream or buffer)
							form.append( key, file );
						}
					} // foreach file
					delete options.files;
				} // files
				
				options.data = form;
			} // multipart
			else {
				// form urlencoded
				options.data = Buffer.from( querystring.stringify(options.data) );
				options.headers['Content-Type'] = 'application/x-www-form-urlencoded';
			}
		} // serialize data
		
		this.request( url, options, callback );
	}
	
	put(url, options, callback) {
		// perform HTTP PUT
		// callback will receive: err, res, data
		if (!callback) {
			// support two-argument calling convention: url and callback
			callback = options;
			options = {};
		}
		if (!options) options = {};
		if (!options.method) options.method = 'PUT';
		this.post( url, options, callback );
	}
	
	delete(url, options, callback) {
		// perform HTTP DELETE
		// callback will receive: err, res, data
		if (!callback) {
			// support two-argument calling convention: url and callback
			callback = options;
			options = {};
		}
		if (!options) options = {};
		if (!options.method) options.method = 'DELETE';
		this.post( url, options, callback );
	}
	
	request(url, options, callback) {
		// low-level request sender
		// callback will receive: err, res, data, perf
		var self = this;
		var callback_fired = false;
		var timer = null;
		var connect_timer = null;
		var upload_timer = null;
		var socket = null;
		var req = null;
		var key;
		var clearUploadMonitor = function() {};
		var clearConnectTimer = function() {
			if (connect_timer) { clearTimeout(connect_timer); connect_timer = null; }
		};
		var clearTimers = function() {
			if (timer) { clearTimeout(timer); timer = null; }
			clearConnectTimer();
			clearUploadMonitor();
		};
		if (!options) options = {};
		else {
			// make shallow copy of options so we don't clobber user's version
			var new_opts = {};
			for (key in options) new_opts[key] = options[key];
			options = new_opts;
		}
		
		// detect need for proxy agent on first request
		if (!this.proxyAgent && userProxyEnv) {
			var proxyOpts = {};
			if (this.autoAgent) {
				// use our global keep-alive agents for proxy
				proxyOpts.httpAgent = this.autoAgent.http;
				proxyOpts.httpsAgent = this.autoAgent.https;
			}
			this.proxyAgent = new ProxyAgent(proxyOpts);
		}
		
		// setup perf
		var perf = new Perf();
		perf.begin();
		
		// import previous perf (from retry or redirect)
		var old_perf = options.perf || null;
		delete options.perf;
		
		// default headers
		if (!options.headers) options.headers = {};
		for (key in this.defaultHeaders) {
			if (!(key in options.headers)) {
				options.headers[key] = this.defaultHeaders[key];
			}
		}
		
		// allow URL to include headers e.g. [header: Cookie: foo=bar]
		url = url.replace(/\s*\[header\:\s*([\w\-]+)\:\s*([^\]]+)\]/ig, function(m_all, m_g1, m_g2) {
			options.headers[ m_g1 ] = m_g2;
			return '';
		}).trim();
		
		// parse url into parts
		var parts = require('url').parse(url);
		if (!options.protocol) options.protocol = parts.protocol;
		
		// standardize on `hostname` instead of `host`
		// (one is an alias to the other, as per http.request docs)
		if (options.host && !options.hostname) {
			options.hostname = options.host;
			delete options.host;
		}
		if (options.hostname && options.port && !options.path) {
			// user likely wants a proxy request, so put full URL as `path` param
			options.path = url;
		}
		if (!options.hostname) options.hostname = parts.hostname;
		if (!options.port) options.port = parts.port || ((parts.protocol == 'https:') ? 443 : 80);
		if (!options.path) options.path = parts.path;
		if (!options.auth && parts.auth) options.auth = parts.auth;
		
		// check acls early if URL points directly at IP address
		if (net.isIP(options.hostname)) {
			if (this.whitelist && !this.whitelist.check(options.hostname)) {
				return callback( new Error("IP is not whitelisted: " + options.hostname) );
			}
			if (this.blacklist && this.blacklist.check(options.hostname)) {
				return callback( new Error("IP is blacklisted: " + options.hostname) );
			}
		}
		
		// optionally use auto agents
		// if no agent is specified, use close connections
		if (this.proxyAgent) {
			options.agent = this.proxyAgent;
		}
		else if (this.autoAgent) {
			options.agent = (parts.protocol == 'https:') ? this.autoAgent.https : this.autoAgent.http;
		}
		else if (!('agent' in options)) {
			options.agent = false;
			options.keepAlive = false;
		}
		
		// possibly use dns cache
		if (this.dnsTTL && dns_cache[options.hostname]) {
			var now = (new Date()).getTime() / 1000;
			var obj = dns_cache[options.hostname];
			if (obj.expires > now) {
				// cache is still fresh, swap in IP and add 'Host' header
				options.headers['Host'] = options.hostname;
				options.hostname = obj.ip;
			}
			else {
				// cache object has expired
				delete dns_cache[options.hostname];
			}
		} // dns cache
		
		// prep post data
		var post_data = null;
		var is_form = false;
		
		if (('data' in options) && (options.data !== null)) {
			post_data = options.data;
			delete options.data;
			
			// support FormData and raw data
			if (post_data instanceof FormData) {
				// allow form-data to populate headers (multipart boundary, etc.)
				is_form = true;
				var form_headers = post_data.getHeaders();
				for (key in form_headers) {
					options.headers[key] = form_headers[key];
				}
			}
			else if (this.autoContentLength || (options.method != 'POST')) {
				// raw data (string or buffer), add content-Length
				if (typeof(post_data) == 'string') post_data = Buffer.from(post_data, 'utf8');
				options.headers['Content-Length'] = post_data.length;
			}
		}
		
		// handle socket timeouts
		var aborted = false;
		var timeout = this.defaultTimeout;
		if ('timeout' in options) {
			timeout = options.timeout;
			delete options.timeout;
		}
		var connectTimeout = this.defaultConnectTimeout;
		if ('connectTimeout' in options) {
			connectTimeout = options.connectTimeout;
			delete options.connectTimeout;
		}
		var idleTimeout = this.defaultIdleTimeout;
		if ('idleTimeout' in options) {
			idleTimeout = options.idleTimeout;
			delete options.idleTimeout;
		}
		
		// optionally follow redirects
		var follow = this.defaultFollow;
		if ('follow' in options) {
			follow = options.follow;
			delete options.follow;
		}
		
		// optionally retry errors
		var retries = this.defaultRetries;
		if ('retries' in options) {
			retries = options.retries;
			delete options.retries;
		}
		var retryDelay = this.defaultRetryDelay;
		if ('retryDelay' in options) {
			retryDelay = options.retryDelay;
			delete options.retryDelay;
		}
		var retryDelayMax = this.defaultRetryDelayMax;
		if ('retryDelayMax' in options) {
			retryDelayMax = options.retryDelayMax;
			delete options.retryDelayMax;
		}
		
		// optional progress events
		var progress = null;
		if ('progress' in options) {
			progress = options.progress;
			delete options.progress;
		}
		
		// stream mode
		var download = null;
		var pre_download = null;
		
		if ('download' in options) {
			download = options.download;
			if (typeof(download) == 'string') {
				try { download = fs.createWriteStream(download); }
				catch (err) {
					clearTimers();
					if (callback && !callback_fired) { callback_fired = true; callback(err); }
					return;
				}
				download.on('error', function(err) {
					clearTimers();
					if (callback && !callback_fired) { callback_fired = true; callback(err); }
					return;
				});
			}
			delete options.download;
		}
		if ('preflight' in options) {
			// special callback to handle raw stream
			pre_download = options.preflight;
			delete options.preflight;
		}
		if ('pre_download' in options) {
			// legacy API, keep for compat
			pre_download = options.pre_download;
			delete options.pre_download;
		}
		
		// abort controller
		var signal = options.signal || null;
		delete options.signal;
		
		// reject bad characters in headers, which can crash node's writeHead() call
		for (var key in options.headers) {
			if (!checkIsHttpToken(key)) {
				callback_fired = true;
				return callback( new Error("Invalid characters in header name: " + key) );
			}
			if (checkInvalidHeaderChar(options.headers[key])) {
				callback_fired = true;
				return callback( new Error("Invalid characters in header value: " + key + ": " + options.headers[key]) );
			}
		}
		
		// handle timeouts
		var receivedPacket = false;
		var handleTimeout = function(msg, ms) {
			if (receivedPacket && idleTimeout) {
				// data received since last timeout, reset timer
				receivedPacket = false;
				timer = setTimeout( function() { handleTimeout(msg, ms); }, idleTimeout );
				return;
			}
			if (!aborted) {
				clearTimers();
				aborted = true;
				req.destroy();
				if (callback && !callback_fired) {
					// check for retry
					if (retries) {
						// revert options to original state
						options.timeout = timeout;
						options.connectTimeout = connectTimeout;
						options.idleTimeout = idleTimeout;
						options.follow = follow;
						options.download = download;
						options.preflight = pre_download;
						options.retries = (typeof(retries) == 'number') ? (retries - 1) : retries;
						options.retryDelay = Math.min( retryDelay * 2, retryDelayMax );
						options.retryDelayMax = retryDelayMax;
						options.progress = progress;
						options.signal = signal;
						
						perf.count('retries', 1);
						options.perf = self.finishPerf(perf, old_perf);
						
						delete options.protocol;
						delete options.hostname;
						delete options.port;
						delete options.path;
						delete options.auth;
						
						if (post_data !== null) options.data = post_data;
						
						// recurse into self for retry
						callback_fired = true; // prevent firing twice
						setTimeout( function() { self.request( url, options, callback ); }, retryDelay );
						return;
					}
					
					callback_fired = true;
					callback( new Error(msg + " (" + ms + " ms)"), null, null, self.finishPerf(perf, old_perf) );
				}
			}
		}; // timeout
		
		var handleSocketError = function(e) {
			// handle socket-related error
			if (callback && !aborted) {
				aborted = true;
				var msg = e.toString();
				if (msg.match(/ENOTFOUND/)) msg = "DNS: Failed to lookup IP from hostname: " + options.hostname;
				else if (msg.match(/ECONNREFUSED/)) msg = "Connection Refused: Failed to connect to host: " + options.hostname;
				else if (e.errno && ErrNo.code[e.errno]) {
					msg = ucfirst(ErrNo.code[e.errno].description) + " (" + e.message + ")";
				}
				clearTimers();
				if (!callback_fired) {
					// check for retry
					if (retries) {
						// revert options to original state
						options.timeout = timeout;
						options.connectTimeout = connectTimeout;
						options.idleTimeout = idleTimeout;
						options.follow = follow;
						options.download = download;
						options.preflight = pre_download;
						options.retries = (typeof(retries) == 'number') ? (retries - 1) : retries;
						options.retryDelay = Math.min( retryDelay * 2, retryDelayMax );
						options.retryDelayMax = retryDelayMax;
						options.progress = progress;
						options.signal = signal;
						
						perf.count('retries', 1);
						options.perf = self.finishPerf(perf, old_perf);
						
						delete options.protocol;
						delete options.hostname;
						delete options.port;
						delete options.path;
						delete options.auth;
						
						if (post_data !== null) options.data = post_data;
						
						// recurse into self for retry
						callback_fired = true; // prevent firing twice
						setTimeout( function() { self.request( url, options, callback ); }, retryDelay );
						return;
					}
					
					callback_fired = true;
					callback( new Error(msg), null, null, self.finishPerf(perf, old_perf) );
				}
			}
		}; // handleSocketError
			
		// monitor outgoing multipart uploads for idle socket timeout
		var startUploadMonitor = function() {
			if (!is_form || !idleTimeout || !post_data) return;
			var sentPacket = false;
			
			var markPacket = function() {
				// reset dead man's switch for upload idle timeout
				sentPacket = true;
			};
			
			var handleUploadTimeout = function() {
				if (sentPacket && idleTimeout) {
					// data sent since last timeout, reset timer
					sentPacket = false;
					upload_timer = setTimeout( handleUploadTimeout, idleTimeout );
					return;
				}
				handleTimeout('Idle Timeout', idleTimeout);
			};
			
			clearUploadMonitor = function() {
				if (upload_timer) { clearTimeout(upload_timer); upload_timer = null; }
				sentPacket = false;
				post_data.removeListener('data', markPacket);
				post_data.removeListener('error', handleSocketError);
			};
			
			post_data.on('data', markPacket);
			post_data.on('error', handleSocketError);
			upload_timer = setTimeout( handleUploadTimeout, idleTimeout );
		}; // startUploadMonitor
		
		var handleIPError = function(err) {
			// An ip-related error (whitelist or blacklist)
			if (!callback || aborted) return; // request is already done
			aborted = true;
			req.destroy();
			clearTimers();
			if (!callback_fired) {
				callback_fired = true;
				callback( err, null, null, self.finishPerf(perf, old_perf) );
			}
		}; // handleIPError
		
		// construct request object
		var proto_class = (parts.protocol == 'https:') ? https : http;
		req = proto_class.request( options, function(res) {
			// got response headers
			res.on('error', handleSocketError);
			if (req.destroyed) return;
			
			perf.end('wait', perf.perf.total.start);
			
			// clear initial timeout (first byte received)
			clearTimers();
			if (idleTimeout) timer = setTimeout( function() { handleTimeout('Idle Timeout', idleTimeout); }, idleTimeout );
			
			// check for auto-redirect
			if (follow && res.statusCode.toString().match(self.followMatch) && res.headers['location']) {
				// revert options to original state
				options.timeout = timeout;
				options.connectTimeout = connectTimeout;
				options.idleTimeout = idleTimeout;
				options.follow = (typeof(follow) == 'number') ? (follow - 1) : follow;
				options.download = download;
				options.preflight = pre_download;
				options.retries = retries;
				options.retryDelay = retryDelay;
				options.retryDelayMax = retryDelayMax;
				options.progress = progress;
				options.signal = signal;
				
				perf.count('redirects', 1);
				options.perf = self.finishPerf(perf, old_perf);
				
				delete options.protocol;
				delete options.hostname;
				delete options.port;
				delete options.path;
				delete options.auth;
				
				if (post_data !== null) options.data = post_data;
				
				// allow original request to finish
				res.on('data', function () {} );
				res.on('end', function() {} );
				
				// recurse into self for redirect
				clearTimers();
				callback_fired = true; // prevent firing twice
				self.request( res.headers['location'], options, callback );
				return;
			}
			
			// check for retry
			if (retries && res.statusCode.toString().match(self.retryMatch)) {
				// revert options to original state
				options.timeout = timeout;
				options.connectTimeout = connectTimeout;
				options.idleTimeout = idleTimeout;
				options.follow = follow;
				options.download = download;
				options.preflight = pre_download;
				options.retries = (typeof(retries) == 'number') ? (retries - 1) : retries;
				options.retryDelay = Math.min( retryDelay * 2, retryDelayMax );
				options.retryDelayMax = retryDelayMax;
				options.progress = progress;
				options.signal = signal;
				
				perf.count('retries', 1);
				options.perf = self.finishPerf(perf, old_perf);
				
				delete options.protocol;
				delete options.hostname;
				delete options.port;
				delete options.path;
				delete options.auth;
				
				if (post_data !== null) options.data = post_data;
				
				// allow original request to finish
				res.on('data', function () {} );
				res.on('end', function() {} );
				
				// recurse into self for retry
				clearTimers();
				callback_fired = true; // prevent firing twice
				setTimeout( function() { self.request( url, options, callback ); }, retryDelay );
				return;
			}
			
			// user might want non-success response codes to be considered errors
			var err = null;
			if (self.autoError && !res.statusCode.toString().match(self.successMatch)) {
				err = new Error( "HTTP " + res.statusCode + " " + res.statusMessage + ": " + url );
				err.code = res.statusCode;
				err.headers = res.headers;
				err.url = url;
			}
			
			// abort controller
			if (signal) {
				var aborter = function() {
					if (aborted || callback_fired) return;
					aborted = true;
					callback_fired = true;
					req.abort();
					callback( new Error("Request Aborted"), res, null, self.finishPerf(perf, old_perf) );
				};
				signal.addEventListener('abort', aborter, { once: true });
				if (signal.aborted) aborter();
			}
			
			if (download) {
				// stream content to a pipe
				var decompressor = null;
				
				res.on('data', function (chunk) {
					// reset dead man's switch for idle timeout
					receivedPacket = true;
					if (progress) progress(chunk, res);
				} );
				
				download.on('finish', function() {
					clearTimers();
					perf.end('receive', perf.perf.total.start);
					if (callback && !callback_fired) {
						callback_fired = true;
						callback( err, res, download, self.finishPerf(perf, old_perf) );
					}
				} );
				
				if (pre_download) {
					// special callback to handle raw stream externally
					if (pre_download( null, res, download ) === false) {
						// special pre-abort error case, switch to buffer mode
						download.removeAllListeners('finish');
						download = null;
					}
				}
				else if (self.autoDecompress && res.headers['content-encoding'] && res.headers['content-encoding'].match(/\bbr\b/i) && hasBrotli) {
					// brotli stream
					decompressor = zlib.createBrotliDecompress();
					decompressor.on('error', function(err) { /* no-op */ });
					res.pipe( decompressor ).pipe( download );
				}
				else if (self.autoDecompress && res.headers['content-encoding'] && res.headers['content-encoding'].match(/\bgzip\b/i)) {
					// gunzip stream
					decompressor = zlib.createGunzip();
					decompressor.on('error', function(err) { /* no-op */ });
					res.pipe( decompressor ).pipe( download );
				}
				else if (self.autoDecompress && res.headers['content-encoding'] && res.headers['content-encoding'].match(/\bdeflate\b/i)) {
					// inflate stream
					decompressor = zlib.createInflate();
					decompressor.on('error', function(err) { /* no-op */ });
					res.pipe( decompressor ).pipe( download );
				}
				else {
					// response is not encoded
					res.pipe( download );
				}
			} // stream mode
			
			if (!download) {
				var chunks = [];
				var total_bytes = 0;
				
				res.on('data', function (chunk) {
					// got chunk of data
					chunks.push( chunk );
					total_bytes += chunk.length;
					receivedPacket = true;
					if (progress) progress(chunk, res);
				} );
				
				res.on('end', function() {
					// end of response
					clearTimers();
					perf.end('receive', perf.perf.total.start);
					if (socket) {
						perf.count('bytes_sent', (socket.bytesWritten || 0) - (socket._pixl_orig_bytes_written || 0));
						perf.count('bytes_received', (socket.bytesRead || 0) - (socket._pixl_orig_bytes_read || 0));
						socket._pixl_orig_bytes_written = socket.bytesWritten || 0;
						socket._pixl_orig_bytes_read = socket.bytesRead || 0;
					}
					
					// prepare data
					if (total_bytes) {
						var buf = Buffer.concat(chunks, total_bytes);
						
						// check for encoding
						if (self.autoDecompress && res.headers['content-encoding'] && res.headers['content-encoding'].match(/\bbr\b/i) && hasBrotli && callback) {
							// brotli decompress
							zlib.brotliDecompress( buf, function(zerr, data) {
								perf.end('decompress', perf.perf.total.start);
								if (!callback_fired) {
									callback_fired = true;
									callback( err || zerr, res, data, self.finishPerf(perf, old_perf) );
								}
							} );
						}
						else if (self.autoDecompress && res.headers['content-encoding'] && res.headers['content-encoding'].match(/\bgzip\b/i) && callback) {
							// gunzip data first
							zlib.gunzip( buf, function(zerr, data) {
								perf.end('decompress', perf.perf.total.start);
								if (!callback_fired) {
									callback_fired = true;
									callback( err || zerr, res, data, self.finishPerf(perf, old_perf) );
								}
							} );
						}
						else if (self.autoDecompress && res.headers['content-encoding'] && res.headers['content-encoding'].match(/\bdeflate\b/i) && callback) {
							// inflate data first
							zlib.inflate( buf, function(zerr, data) {
								perf.end('decompress', perf.perf.total.start);
								if (!callback_fired) {
									callback_fired = true;
									callback( err || zerr, res, data, self.finishPerf(perf, old_perf) );
								}
							} );
						}
						else {
							// response content is not encoded (or autoDecompress is false)
							if (callback && !callback_fired) {
								callback_fired = true;
								callback( err, res, buf, self.finishPerf(perf, old_perf) );
							}
						}
					}
					else {
						// response content is empty
						if (callback && !callback_fired) {
							callback_fired = true;
							callback( err, res, Buffer.alloc(0), self.finishPerf(perf, old_perf) );
						}
					}
				} ); // end
			} // buffer mode
			
		} ); // request
		
		req.on('socket', function(sock) {
			// hook some socket events once we have a reference to it
			socket = sock;
			
			// socket may already be connected if reusing keep-alive
			if (!socket.connecting) clearConnectTimer();
			
			if (!socket._pixl_request_hooked) {
				socket._pixl_request_hooked = true;
				
				// Disable the Nagle algorithm.
				socket.setNoDelay( true );
				
				socket.once('lookup', function(err, address, family, hostname) {
					// track DNS lookup time
					perf.end('dns', perf.perf.total.start);
					
					// whitelist/blacklist checks here
					if (self.whitelist && !self.whitelist.check(address)) {
						return handleIPError( new Error("IP is not whitelisted: " + address) );
					}
					if (self.blacklist && self.blacklist.check(address)) {
						return handleIPError( new Error("IP is blacklisted: " + address) );
					}
					
					// possibly cache IP for future lookups
					if (self.dnsTTL) {
						dns_cache[ options.hostname ] = {
							ip: address,
							expires: ((new Date()).getTime() / 1000) + self.dnsTTL
						};
					}
				} );
				
				socket.once('connect', function() {
					// track socket connect time
					clearConnectTimer();
					perf.end('connect', perf.perf.total.start);
				} );
				
				// JH 2024-07-03 we should not need an error listener on the socket
				// socket.on( 'error', handleSocketError );
			} // not hooked
		} ); // socket
		
		req.on('finish', function() {
			// track data send time (only really works for POST/PUT)
			clearUploadMonitor();
			perf.end('send', perf.perf.total.start);
		} );
		
		// assume this is a socket error too
		req.on('error', handleSocketError );
		
		if (timeout) {
			// set initial socket timeout which aborts the request
			// this is cleared at first byte, then we rely on the socket idle timeout
			timer = setTimeout( function() { handleTimeout('Request Timeout', timeout); }, timeout );
		}
		if (connectTimeout && (!socket || socket.connecting)) {
			// set connect timeout (includes DNS + socket connect)
			connect_timer = setTimeout( function() { handleTimeout('Connect Timeout', connectTimeout); }, connectTimeout );
		}
		
		if (post_data !== null) {
			// write post data to socket
			if (is_form) {
				startUploadMonitor();
				post_data.pipe( req );
			}
			else {
				// Note: Sending data with req.end() prevents chunked transfer encoding
				req.end( post_data );
				// req.write( post_data );
				// req.end();
			}
		}
		else req.end();
	}
	
	finishPerf(perf, old_perf) {
		// finalize perf, adjust metrics and total
		// order: dns, connect, send, wait, receive, decompress
		var p = perf.perf;
		
		if (p.decompress && p.receive) p.decompress.elapsed -= p.receive.elapsed;
		if (p.receive && p.wait) p.receive.elapsed -= p.wait.elapsed;
		if (p.wait && p.send) p.wait.elapsed -= p.send.elapsed;
		if (p.send && p.connect) p.send.elapsed -= p.connect.elapsed;
		if (p.connect && p.dns) p.connect.elapsed -= p.dns.elapsed;
		
		for (var key in p) {
			if (p[key].elapsed) p[key].elapsed = Math.max(0, p[key].elapsed);
		}
		
		if (old_perf) {
			// import perf from previous retry/redirect
			if (old_perf.perf && old_perf.perf[perf.totalKey]) {
				for (var key in old_perf.perf) {
					if (key == perf.totalKey) {
						perf.perf[key].start = old_perf.perf[key].start;
					}
					else {
						if (!perf.perf[key]) perf.perf[key] = {};
						if (!perf.perf[key].end) perf.perf[key].end = 1;
						if (!perf.perf[key].elapsed) perf.perf[key].elapsed = 0;
						var elapsed = old_perf.perf[key].elapsed;
						perf.perf[key].elapsed += (elapsed / (old_perf.scale / perf.scale)) || 0;
					}
				}
			}
			
			if (old_perf.counters) {
				for (var key in old_perf.counters) {
					perf.count( key, old_perf.counters[key] );
				}
			}
		} // old_perf
		
		perf.count('requests', 1);
		perf.end();
		
		return perf;
	}
	
});

function ucfirst(text) {
	// capitalize first character only, lower-case rest
	return text.substring(0, 1).toUpperCase() + text.substring(1, text.length).toLowerCase();
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
// Unit tests for pixl-request
// Copyright (c) 2024 Joseph Huckaby
// Released under the MIT License

var Path = require('path');
var fs = require('fs');
var net = require('net');
var crypto = require('crypto');
var async = require('async');

var PixlServer = require('pixl-server');

var PixlRequest = require('..');
var request = new PixlRequest();

var http = require('http');
var agent_ka = new http.Agent({ keepAlive: true });
var agent_na = new http.Agent({ keepAlive: false });

process.chdir( __dirname );

var server = new PixlServer({
	
	__name: 'PixlRequestTest',
	__version: "1.0",
	
	config: {
		"log_dir": __dirname,
		"log_filename": "test.log",
		"debug_level": 9,
		"debug": 1,
		"echo": 0,
		
		"WebServer": {
			"http_port": 3020,
			"http_alt_ports": [3120],
			"http_htdocs_dir": __dirname,
			"http_max_upload_size": 1024 * 10,
			"http_static_ttl": 3600,
			"http_static_index": "index.html",
			"http_server_signature": "PixlRequestTest 1.0",
			"http_compress_text": 1,
			"http_enable_brotli": 1,
			"http_timeout": 5,
			"http_socket_prelim_timeout": 2,
			"http_response_headers": {
				"Via": "PixlRequestTest 1.0"
			},
			
			"http_log_requests": false,
			"http_regex_log": ".+",
			"http_recent_requests": 10,
			"http_max_connections": 10,
			
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
				var NUM_RETRIES = 3;
				
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
				
				web_server.addURIHandler( '/retry', 'Retry', function(args, callback) {
					// send error N times, then success
					var ms = parseInt( args.query.ms || 1 );
					
					if (NUM_RETRIES) {
						NUM_RETRIES--;
						setTimeout( function() { 
							callback( "500 Internal Server Error", {}, "Internal Server Error" );
						}, ms );
					}
					else {
						callback( {
							code: 0,
							description: "Success",
							user: { Name: "Joe", Email: "foo@bar.com" }
						} );
					}
				} );
				
				web_server.addURIHandler( '/server-status', "Server Status", true, function(args, callback) {
					// send web stats (JSON), ACL protected endpoint
					callback( server.WebServer.getStats() );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
						'Cookie': "COOKIE1=foo1234; COOKIE2=bar5678;",
						'X-Test': "Test"
					}
				},
				function(err, resp, json, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					test.ok( json.code == 0, "Correct code in JSON response: " + json.code );
					test.ok( !!json.user, "Found user object in JSON response" );
					test.ok( json.user.Name == "Joe", "Correct user name in JSON response: " + json.user.Name );
					
					test.ok( !!json.cookies, "Found cookies in JSON response" );
					test.ok( json.cookies.COOKIE1 == "foo1234", "Correct COOKIE1 value" );
					test.ok( json.cookies.COOKIE2 == "bar5678", "Correct COOKIE2 value" );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( json.files.file1.size == 43, "Uploaded file has correct size (43): " + json.files.file1.size );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
		
		// stream download to file
		function testStreamDownloadRequest(test) {
			// test simple HTTP GET to webserver backend
			var temp_file = 'downloaded.gif';
			var opts = {
				download: temp_file
			};
			request.get( 'http://127.0.0.1:3020/spacer.gif', opts,
				function(err, resp, download, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/image\/gif/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['cache-control'], "Cache-Control header present" );
					test.ok( !!resp.headers['cache-control'].match(/max\-age\=3600/), "Cache-Control header contains correct TTL" );
					
					test.ok( fs.existsSync(temp_file), temp_file + " is present" );
					test.ok( fs.readFileSync(temp_file).length === fs.readFileSync('spacer.gif').length, temp_file + " length is correct" );
					
					fs.unlinkSync(temp_file);
					test.done();
				} 
			);
		},
		
		// rate limit upstream
		function testMultipartPostRateLimit(test) {
			request.post( 'http://127.0.0.1:3020/json',
				{
					rate: 1024,
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( json.files.file1.size == 43, "Uploaded file has correct size (43): " + json.files.file1.size );
					test.done();
				} 
			);
		},
		
		// rate limit downstream (buffer)
		function testStaticBinaryRequestRateLimit(test) {
			// test simple HTTP GET to webserver backend
			var opts = {
				rate: 1024
			};
			request.get( 'http://127.0.0.1:3020/spacer.gif', opts,
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/image\/gif/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['cache-control'], "Cache-Control header present" );
					test.ok( !!resp.headers['cache-control'].match(/max\-age\=3600/), "Cache-Control header contains correct TTL" );
					
					test.ok( !resp.headers['content-encoding'], "Content-Encoding header should NOT be present!" );
					
					test.ok( !!data, "Got data in response" );
					test.ok( data.length === fs.readFileSync('spacer.gif').length, "spacer.gif content is correct" );
					
					test.done();
				} 
			);
		},
		
		// rate limit downstream (stream)
		function testStreamDownloadRequestRateLimit(test) {
			// test simple HTTP GET to webserver backend
			var temp_file = 'downloaded.gif';
			var opts = {
				rate: 1024,
				download: temp_file
			};
			request.get( 'http://127.0.0.1:3020/spacer.gif', opts,
				function(err, resp, download, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
					test.ok( !!resp.headers['content-type'], "Content-Type header present" );
					test.ok( !!resp.headers['content-type'].match(/image\/gif/), "Content-Type header contains correct value" );
					
					test.ok( !!resp.headers['cache-control'], "Cache-Control header present" );
					test.ok( !!resp.headers['cache-control'].match(/max\-age\=3600/), "Cache-Control header contains correct TTL" );
					
					test.ok( fs.existsSync(temp_file), temp_file + " is present" );
					test.ok( fs.readFileSync(temp_file).length === fs.readFileSync('spacer.gif').length, temp_file + " length is correct" );
					
					fs.unlinkSync(temp_file);
					test.done();
				} 
			);
		},
		
		// abort controller
		function testStaticBinaryRequestAbort(test) {
			// test simple HTTP GET to webserver backend
			var ac = new AbortController();
			var opts = {
				signal: ac.signal
			};
			request.get( 'http://127.0.0.1:3020/spacer.gif', opts,
				function(err, resp, data, perf) {
					test.ok( !!err, "Expected error from PixlRequest" );
					test.done();
				} 
			);
			
			// abort right away
			ac.abort();
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
		
		// http_max_connections
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
		function testRedirect(test) {
			request.get( 'http://127.0.0.1:3020/redirect',
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 302, "Got 302 response: " + resp.statusCode );
					test.ok( !!resp.headers['location'], "Got Location header" );
					test.ok( !!resp.headers['location'].match(/redirected/), "Correct Location header");
					
					var metrics = perf.metrics();
					test.ok( metrics.counters.requests == 1, "Expected 1 requests in perf metrics, got: " + metrics.counters.requests );
					test.ok( !metrics.counters.redirects, "Expected no redirects in perf metrics, got: " + metrics.counters.redirects );
					
					test.done();
				} 
			);
		},
		
		// redirect with follow
		function testRedirectFollow(test) {
			request.get( 'http://127.0.0.1:3020/redirect', { follow: 1 },
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					
					var metrics = perf.metrics();
					test.ok( metrics.counters.requests == 2, "Expected 2 requests in perf metrics, got: " + metrics.counters.requests );
					test.ok( metrics.counters.redirects == 1, "Expected 1 redirects in perf metrics, got: " + metrics.counters.redirects );
					
					test.done();
				} 
			);
		},
		
		// retries
		function testRetries(test) {
			request.get( 'http://127.0.0.1:3020/retry', { retries: 5 },
				function(err, resp, data, perf) {
					test.ok( !err, "No error from PixlRequest: " + err );
					test.ok( !!resp, "Got resp from PixlRequest" );
					test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
					
					var metrics = perf.metrics();
					test.ok( metrics.counters.requests == 4, "Expected 4 requests in perf metrics, got: " + metrics.counters.requests );
					test.ok( metrics.counters.retries == 3, "Expected 3 retries in perf metrics, got: " + metrics.counters.retries );
					
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
		
		// http_public_ip_offset
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
		
		// server acl
		function testServerACL(test) {
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
		function testServerACLBadIP(test) {
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
		
		// whitelist
		function testWhitelistAllow(test) {
			// test whitelist with allowed ip
			request.setWhitelist('127.0.0.1');
			
			request.json( 'http://127.0.0.1:3020/json', false, function(err, resp, data, perf) {
				test.ok( !err, "No error from PixlRequest: " + err );
				test.ok( !!resp, "Got resp from PixlRequest" );
				test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
				
				request.setWhitelist(false);
				test.done();
			});
		},
		function testWhitelistDeny(test) {
			// test whitelist with denied ip
			request.setWhitelist('10.0.0.0/8');
			
			request.json( 'http://127.0.0.1:3020/json', false, function(err, resp, data, perf) {
				test.ok( !!err, "Expected error from PixlRequest" );
				
				request.setWhitelist(false);
				test.done();
			});
		},
		
		// blacklist
		function testBlacklistAllow(test) {
			// test blacklist with allowed ip
			request.setBlacklist('192.168.1.1');
			
			request.json( 'http://127.0.0.1:3020/json', false, function(err, resp, data, perf) {
				test.ok( !err, "No error from PixlRequest: " + err );
				test.ok( !!resp, "Got resp from PixlRequest" );
				test.ok( resp.statusCode == 200, "Got 200 response: " + resp.statusCode );
				
				request.setBlacklist(false);
				test.done();
			});
		},
		function testBlacklistDeny(test) {
			// test blacklist with denied ip
			request.setBlacklist('127.0.0.0/8');
			
			request.json( 'http://127.0.0.1:3020/json', false, function(err, resp, data, perf) {
				test.ok( !!err, "Expected error from PixlRequest" );
				
				request.setBlacklist(false);
				test.done();
			});
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					test.ok( !!json, "Got JSON in response" );
					
					// test.debug("Web Server Stats", json);
					test.ok( !!json.server, "server obj in stats" );
					test.ok( json.server.name == "PixlRequestTest", "Correct server name in stats" );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
					
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
					test.ok( json.files.file1.size == 43, "Uploaded file has correct size (43): " + json.files.file1.size );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
					test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
				test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
							test.ok( resp.headers['via'] == "PixlRequestTest 1.0", "Correct Via header: " + resp.headers['via'] );
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
		
		// http_max_concurrent_requests
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

