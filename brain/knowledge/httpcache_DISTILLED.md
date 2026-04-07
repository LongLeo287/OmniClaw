---
id: httpcache
type: knowledge
owner: OA_Triage
---
# httpcache
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# httpcache

[![GoDoc](https://godoc.org/github.com/bitcomplete/httpcache?status.svg)](https://godoc.org/github.com/bitcomplete/httpcache)

Package httpcache provides a http.RoundTripper implementation that works as a
mostly [RFC 7234](https://tools.ietf.org/html/rfc7234) compliant cache for http
responses. This incarnation of the library is an active fork of
[github.com/gregjones/httpcache](https://github.com/gregjones/httpcache) which
is unmaintained.

It is only suitable for use as a 'private' cache (i.e. for a web-browser or an
API-client and not for a shared proxy).

## Cache Backends

- The built-in 'memory' cache stores responses in an in-memory map. -
  [`github.com/bitcomplete/httpcache/diskcache`](https://github.com/bitcomplete/httpcache/tree/master/diskcache)
  provides a filesystem-backed cache using the
  [diskv](https://github.com/peterbourgon/diskv) library. -
  [`github.com/bitcomplete/httpcache/memcache`](https://github.com/bitcomplete/httpcache/tree/master/memcache)
  provides memcache implementations, for both App Engine and 'normal' memcache
  servers. -
  [`sourcegraph.com/sourcegraph/s3cache`](https://sourcegraph.com/github.com/sourcegraph/s3cache)
  uses Amazon S3 for storage. -
  [`github.com/bitcomplete/httpcache/leveldbcache`](https://github.com/bitcomplete/httpcache/tree/master/leveldbcache)
  provides a filesystem-backed cache using
  [leveldb](https://github.com/syndtr/goleveldb/leveldb). -
  [`github.com/die-net/lrucache`](https://github.com/die-net/lrucache) provides an
  in-memory cache that will evict least-recently used entries. -
  [`github.com/die-net/lrucache/twotier`](https://github.com/die-net/lrucache/tree/master/twotier)
  allows caches to be combined, for example to use lrucache above with a
  persistent disk-cache. -
  [`github.com/birkelund/boltdbcache`](https://github.com/birkelund/boltdbcache)
  provides a BoltDB implementation (based on the
  [bbolt](https://github.com/coreos/bbolt) fork).

If you implement any other backend and wish it to be linked here, please send a
PR editing this file.

## License

- [MIT License](LICENSE.txt)

```

### File: httpcache.go
```go
// Package httpcache provides a http.RoundTripper implementation that works as a
// mostly RFC-compliant cache for http responses.
//
// It is only suitable for use as a 'private' cache (i.e. for a web-browser or an API-client
// and not for a shared proxy).
//
package httpcache

import (
	"bufio"
	"bytes"
	"context"
	"errors"
	"io"
	"io/ioutil"
	"net/http"
	"net/http/httputil"
	"strings"
	"sync"
	"time"
)

const (
	stale = iota
	fresh
	transparent
	// XFromCache is the header added to responses that are returned from the cache
	XFromCache = "X-From-Cache"
)

// A Cache interface is used by the Transport to store and retrieve responses.
type Cache interface {
	// Get returns the []byte representation of a cached response and a bool
	// set to true if the value isn't empty
	Get(ctx context.Context, key string) (responseBytes []byte, ok bool)
	// Set stores the []byte representation of a response against a key
	Set(ctx context.Context, key string, responseBytes []byte)
	// Delete removes the value associated with the key
	Delete(ctx context.Context, key string)
}

type KeyFunc func(req *http.Request) string

// DefaultKeyFunc returns the cache key for req
var DefaultKeyFunc = func(req *http.Request) string {
	if req.Method == http.MethodGet {
		return req.URL.String()
	} else {
		return req.Method + " " + req.URL.String()
	}
}

// CachedResponse returns the cached http.Response for req if present, and nil
// otherwise.
func CachedResponse(ctx context.Context, c Cache, key string, req *http.Request) (resp *http.Response, err error) {
	cachedVal, ok := c.Get(ctx, key)
	if !ok {
		return
	}

	b := bytes.NewBuffer(cachedVal)
	return http.ReadResponse(bufio.NewReader(b), req)
}

// MemoryCache is an implemtation of Cache that stores responses in an in-memory map.
type MemoryCache struct {
	mu    sync.RWMutex
	items map[string][]byte
}

// Get returns the []byte representation of the response and true if present, false if not
func (c *MemoryCache) Get(ctx context.Context, key string) (resp []byte, ok bool) {
	c.mu.RLock()
	resp, ok = c.items[key]
	c.mu.RUnlock()
	return resp, ok
}

// Set saves response resp to the cache with key
func (c *MemoryCache) Set(ctx context.Context, key string, resp []byte) {
	c.mu.Lock()
	c.items[key] = resp
	c.mu.Unlock()
}

// Delete removes key from the cache
func (c *MemoryCache) Delete(ctx context.Context, key string) {
	c.mu.Lock()
	delete(c.items, key)
	c.mu.Unlock()
}

// NewMemoryCache returns a new Cache that will store items in an in-memory map
func NewMemoryCache() *MemoryCache {
	c := &MemoryCache{items: map[string][]byte{}}
	return c
}

// TransportOpt is a configuration option for creating a new Transport
type TransportOpt func(t *Transport)

// MarkCachedResponsesOpt configures a transport by setting MarkCachedResponses to true
func MarkCachedResponsesOpt(markCachedResponses bool) TransportOpt {
	return func(t *Transport) {
		t.MarkCachedResponses = markCachedResponses
	}
}

// KeyFuncOpt configures a transport by setting its KeyFunc to the one given
func KeyFuncOpt(keyFunc KeyFunc) TransportOpt {
	return func(t *Transport) {
		t.KeyFunc = keyFunc
	}
}

// Transport is an implementation of http.RoundTripper that will return values from a cache
// where possible (avoiding a network request) and will additionally add validators (etag/if-modified-since)
// to repeated requests allowing servers to return 304 / Not Modified
type Transport struct {
	// The RoundTripper interface actually used to make requests
	// If nil, http.DefaultTransport is used
	Transport http.RoundTripper
	Cache     Cache
	// If true, responses returned from the cache will be given an extra header, X-From-Cache
	MarkCachedResponses bool
	// A function to generate a cache key for the given request
	KeyFunc KeyFunc
}

// NewTransport returns a new Transport with the provided Cache and options. If
// KeyFunc is not specified in opts then DefaultKeyFunc is used.
func NewTransport(c Cache, opts ...TransportOpt) *Transport {
	t := &Transport{
		Cache:               c,
		KeyFunc:             DefaultKeyFunc,
		MarkCachedResponses: true,
	}
	for _, opt := range opts {
		opt(t)
	}
	return t
}

// Client returns an *http.Client that caches responses.
func (t *Transport) Client() *http.Client {
	return &http.Client{Transport: t}
}

// varyMatches will return false unless all of the cached values for the headers listed in Vary
// match the new request
func varyMatches(cachedResp *http.Response, req *http.Request) bool {
	for _, header := range headerAllCommaSepValues(cachedResp.Header, "vary") {
		header = http.CanonicalHeaderKey(header)
		if header != "" && req.Header.Get(header) != cachedResp.Header.Get("X-Varied-"+header) {
			return false
		}
	}
	return true
}

// RoundTrip takes a Request and returns a Response
//
// If there is a fresh Response already in cache, then it will be returned without connecting to
// the server.
//
// If there is a stale Response, then any validators it contains will be set on the new request
// to give the server a chance to respond with NotModified. If this happens, then the cached Response
// will be returned.
func (t *Transport) RoundTrip(req *http.Request) (resp *http.Response, err error) {
	cacheKey := t.KeyFunc(req)
	cacheable := (req.Method == "GET" || req.Method == "HEAD") && req.Header.Get("range") == ""
	var cachedResp *http.Response
	if cacheable {
		cachedResp, err = CachedResponse(req.Context(), t.Cache, cacheKey, req)
	} else {
		// Need to invalidate an existing value
		t.Cache.Delete(req.Context(), cacheKey)
	}

	transport := t.Transport
	if transport == nil {
		transport = http.DefaultTransport
	}

	if cacheable && cachedResp != nil && err == nil {
		if t.MarkCachedResponses {
			cachedResp.Header.Set(XFromCache, "1")
		}

		if varyMatches(cachedResp, req) {
			// Can only use cached value if the new request doesn't Vary significantly
			freshness := getFreshness(cachedResp.Header, req.Header)
			if freshness == fresh {
				return cachedResp, nil
			}

			if freshness == stale {
				var req2 *http.Request
				// Add validators if caller hasn't already done so
				etag := cachedResp.Header.Get("etag")
				if etag != "" && req.Header.Get("etag") == "" {
					req2 = cloneRequest(req)
					req2.Header.Set("if-none-match", etag)
				}
				lastModified := cachedResp.Header.Get("last-modified")
				if lastModified != "" && req.Header.Get("last-modified") == "" {
					if req2 == nil {
						req2 = cloneRequest(req)
					}
					req2.Header.Set("if-modified-since", lastModified)
				}
				if req2 != nil {
					req = req2
				}
			}
		}

		resp, err = transport.RoundTrip(req)
		if err == nil && req.Method == "GET" && resp.StatusCode == http.StatusNotModified {
			// Replace the 304 response with the one from cache, but update with some new headers
			endToEndHeaders := getEndToEndHeaders(resp.Header)
			for _, header := range endToEndHeaders {
				cachedResp.Header[header] = resp.Header[header]
			}
			resp = cachedResp
		} else if (err != nil || (cachedResp != nil && resp.StatusCode >= 500)) &&
			req.Method == "GET" && canStaleOnError(cachedResp.Header, req.Header) {
			// In case of transport failure and stale-if-error activated, returns cached content
			// when available
			return cachedResp, nil
		} else {
			if err != nil || resp.StatusCode != http.StatusOK {
				t.Cache.Delete(req.Context(), cacheKey)
			}
			if err != nil {
				return nil, err
			}
		}
	} else {
		reqCacheControl := parseCacheControl(req.Header)
		if _, ok := reqCacheControl["only-if-cached"]; ok {
			resp = newGatewayTimeoutResponse(req)
		} else {
			resp, err = transport.RoundTrip(req)
			if err != nil {
				return nil, err
			}
		}
	}

	if cacheable && canStore(parseCacheControl(req.Header), parseCacheControl(resp.Header)) {
		for _, varyKey := range headerAllCommaSepValues(resp.Header, "vary") {
			varyKey = http.CanonicalHeaderKey(varyKey)
			fakeHeader := "X-Varied-" + varyKey
			reqValue := req.Header.Get(varyKey)
			if reqValue != "" {
				resp.Header.Set(fakeHeader, reqValue)
			}
		}
		switch req.Method {
		case "GET":
			// Delay caching until EOF is reached.
			resp.Body = &cachingReadCloser{
				R: resp.Body,
				OnEOF: func(r io.Reader) {
					resp := *resp
					resp.Body = ioutil.NopCloser(r)
					respBytes, err := httputil.DumpResponse(&resp, true)
					if err == nil {
						t.Cache.Set(req.Context(), cacheKey, respBytes)
					}
				},
			}
		default:
			respBytes, err := httputil.DumpResponse(resp, true)
			if err == nil {
				t.Cache.Set(req.Context(), cacheKey, respBytes)
			}
		}
	} else {
		t.Cache.Delete(req.Context(), cacheKey)
	}
	return resp, nil
}

// ErrNoDateHeader indicates that the HTTP headers contained no Date header.
var ErrNoDateHeader = errors.New("no Date header")

// Date parses and returns the value of the Date header.
func Date(respHeaders http.Header) (date time.Time, err error) {
	dateHeader := respHeaders.Get("date")
	if dateHeader == "" {
		err = ErrNoDateHeader
		return
	}

	return time.Parse(time.RFC1123, dateHeader)
}

type realClock struct{}

func (c *realClock) since(d time.Time) time.Duration {
	return time.Since(d)
}

type timer interface {
	since(d time.Time) time.Duration
}

var clock timer = &realClock{}

// getFreshness will return one of fresh/stale/transparent based on the cache-control
// values of the request and the response
//
// fresh indicates the response can be returned
// stale indicates that the response needs validating before it is returned
// transparent indicates the response should not be used to fulfil the request
//
// Because this is only a private cache, 'public' and 'private' in cache-control aren't
// signficant. Similarly, smax-age isn't used.
func getFreshness(respHeaders, reqHeaders http.Header) (freshness int) {
	respCacheControl := parseCacheControl(respHeaders)
	reqCacheControl := parseCacheControl(reqHeaders)
	if _, ok := reqCacheControl["no-cache"]; ok {
		return transparent
	}
	if _, ok := respCacheControl["no-cache"]; ok {
		return stale
	}
	if _, ok := reqCacheControl["only-if-cached"]; ok {
		return fresh
	}

	date, err := Date(respHeaders)
	if err != nil {
		return stale
	}
	currentAge := clock.since(date)

	var lifetime time.Duration
	var zeroDuration time.Duration

	// If a response includes both an Expires header and a max-age directive,
	// the max-age directive overrides the Expires header, even if the Expires header is more restrictive.
	if maxAge, ok := respCacheControl["max-age"]; ok {
		lifetime, err = time.ParseDuration(maxAge + "s")
		if err != nil {
			lifetime = zeroDuration
		}
	} else {
		expiresHeader := respHeaders.Get("Expires")
		if expiresHeader != "" {
			expires, err := time.Parse(time.RFC1123, expiresHeader)
			if err != nil {
				lifetime = zeroDuration
			} else {
				lifetime = expires.Sub(date)
			}
		}
	}

	if maxAge, ok := reqCacheControl["max-age"]; ok {
		// the client is willing to accept a response whose age is no greater than the specified time in seconds
		lifetime, err = time.ParseDuration(maxAge + "s")
		if err != nil {
			lifetime = zeroDuration
		}
	}
	if minfresh, ok := reqCacheControl["min-fresh"]; ok {
		//  the client wants a response that will still be fresh for at least the specified number of seconds.
		minfreshDuration, err := time.ParseDuration(minfresh + "s")
		if err == nil {
			currentAge = time.Duration(currentAge + minfreshDuration)
		}
	}

	if maxstale, ok := reqCacheControl["max-stale"]; ok {
		// Indicates that the client is willing to accept a response that has exceeded its expiration time.
		// If max-stale is assigned a value, then the client is willing to accept a response that has exceeded
		// its expiration time by no more than the specified number of seconds.
		// If no value is assigned to max-stale, then the client is willing to accept a stale response of any age.
		//
		// Responses served only because of a max-stale value are supposed to have a Warning header added to them,
		// but that seems like a  hassle, and is it actually useful? If so, then there needs to be a different
		// return-value available here.
		if maxstale == "" {
			return fresh
		}
		maxstaleDuration, err := time.ParseDuration(maxstale + "s")
		if err == nil {
			currentAge = time.Duration(currentAge - maxstaleDuration)
		}
	}

	if lifetime > currentAge {
		return fresh
	}

	return stale
}

// Returns true if either the request or the response includes the stale-if-error
// cache control extension: https://tools.ietf.org/html/rfc5861
func canStaleOnError(respHeaders, reqHeaders http.Header) bool {
	respCacheControl := parseCacheControl(respHeaders)
	reqCacheControl := parseCacheControl(reqHeaders)

	var err error
	lifetime := time.Duration(-1)

	if staleMaxAge, ok := respCacheControl["stale-if-error"]; ok {
		if staleMaxAge != "" {
			lifetime, err = time.ParseDuration(staleMaxAge + "s")
			if err != nil {
				return false
			}
		} else {
			return true
		}
	}
	if staleMaxAge, ok := reqCacheControl["stale-if-error"]; ok {
		if staleMaxAge != "" {
			lifetime, err = time.ParseDuration(staleMaxAge + "s")
			if err != nil {
				return false
			}
		} else {
			return true
		}
	}

	if lifetime >= 0 {
		date, err := Date(respHeaders)
		if err != nil {
			return false
		}
		currentAge := clock.since(date)
		if lifetime > currentAge {
			return true
		}
	}

	return false
}

func getEndToEndHeaders(respHeaders http.Header) []string {
	// These headers are always hop-by-hop
	hopByHopHeaders := map[string]struct{}{
		"Connection":          {},
		"Keep-Alive":          {},
		"Proxy-Authenticate":  {},
		"Proxy-Authorization": {},
		"Te":                  {},
		"Trailers":            {},
		"Transfer-Encoding":   {},
		"Upgrade":             {},
	}

	for _, extra := range strings.Split(respHeaders.Get("connection"), ",") {
		// any header listed in connection, if present, is also considered hop-by-hop
		if strings.Trim(extra, " ") != "" {
			hopByHopHeaders[http.CanonicalHeaderKey(extra)] = struct{}{}
		}
	}
	endToEndHeaders := []string{}
	for respHeader := range respHeaders {
		if _, ok := hopByHopHeaders[respHeader]; !ok {
			endToEndHeaders = append(endToEndHeaders, respHeader)
		}
	}
	return endToEndHeaders
}

func canStore(reqCacheControl, respCacheControl cacheControl) (canStore bool) {
	if _, ok := respCacheControl["no-store"]; ok {
		return false
	}
	if _, ok := reqCacheControl["no-store"]; ok {
		return false
	}
	return true
}

func newGatewayTimeoutResponse(req *http.Request) *http.Response {
	var braw bytes.Buffer
	braw.WriteString("HTTP/1.1 504 Gateway Timeout\r\n\r\n")
	resp, err := http.ReadResponse(bufio.NewReader(&braw), req)
	if err != nil {
		panic(err)
	}
	return resp
}

// cloneRequest returns a clone of the provided *http.Request.
// The clone is a shallow copy of the struct and its Header map.
// (This function copyright goauth2 authors: https://code.google.com/p/goauth2)
func cloneRequest(r *http.Request) *http.Request {
	// shallow copy of the struct
	r2 := new(http.Req
... [TRUNCATED]
```

### File: httpcache_test.go
```go
package httpcache

import (
	"bytes"
	"errors"
	"flag"
	"io"
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"os"
	"strconv"
	"testing"
	"time"
)

var s struct {
	server    *httptest.Server
	client    http.Client
	transport *Transport
	done      chan struct{} // Closed to unlock infinite handlers.
}

type fakeClock struct {
	elapsed time.Duration
}

func (c *fakeClock) since(t time.Time) time.Duration {
	return c.elapsed
}

func TestMain(m *testing.M) {
	flag.Parse()
	setup()
	code := m.Run()
	teardown()
	os.Exit(code)
}

func setup() {
	tp := NewMemoryCacheTransport()
	client := http.Client{Transport: tp}
	s.transport = tp
	s.client = client
	s.done = make(chan struct{})

	mux := http.NewServeMux()
	s.server = httptest.NewServer(mux)

	mux.HandleFunc("/", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Cache-Control", "max-age=3600")
	}))

	mux.HandleFunc("/method", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Cache-Control", "max-age=3600")
		_, _ = w.Write([]byte(r.Method))
	}))

	mux.HandleFunc("/range", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		lm := "Fri, 14 Dec 2010 01:01:50 GMT"
		if r.Header.Get("if-modified-since") == lm {
			w.WriteHeader(http.StatusNotModified)
			return
		}
		w.Header().Set("last-modified", lm)
		if r.Header.Get("range") == "bytes=4-9" {
			w.WriteHeader(http.StatusPartialContent)
			_, _ = w.Write([]byte(" text "))
			return
		}
		_, _ = w.Write([]byte("Some text content"))
	}))

	mux.HandleFunc("/nostore", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Cache-Control", "no-store")
	}))

	mux.HandleFunc("/etag", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		etag := "124567"
		if r.Header.Get("if-none-match") == etag {
			w.WriteHeader(http.StatusNotModified)
			return
		}
		w.Header().Set("etag", etag)
	}))

	mux.HandleFunc("/lastmodified", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		lm := "Fri, 14 Dec 2010 01:01:50 GMT"
		if r.Header.Get("if-modified-since") == lm {
			w.WriteHeader(http.StatusNotModified)
			return
		}
		w.Header().Set("last-modified", lm)
	}))

	mux.HandleFunc("/varyaccept", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Cache-Control", "max-age=3600")
		w.Header().Set("Content-Type", "text/plain")
		w.Header().Set("Vary", "Accept")
		_, _ = w.Write([]byte("Some text content"))
	}))

	mux.HandleFunc("/doublevary", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Cache-Control", "max-age=3600")
		w.Header().Set("Content-Type", "text/plain")
		w.Header().Set("Vary", "Accept, Accept-Language")
		_, _ = w.Write([]byte("Some text content"))
	}))
	mux.HandleFunc("/2varyheaders", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Cache-Control", "max-age=3600")
		w.Header().Set("Content-Type", "text/plain")
		w.Header().Add("Vary", "Accept")
		w.Header().Add("Vary", "Accept-Language")
		_, _ = w.Write([]byte("Some text content"))
	}))
	mux.HandleFunc("/varyunused", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Cache-Control", "max-age=3600")
		w.Header().Set("Content-Type", "text/plain")
		w.Header().Set("Vary", "X-Madeup-Header")
		_, _ = w.Write([]byte("Some text content"))
	}))

	mux.HandleFunc("/cachederror", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		etag := "abc"
		if r.Header.Get("if-none-match") == etag {
			w.WriteHeader(http.StatusNotModified)
			return
		}
		w.Header().Set("etag", etag)
		w.WriteHeader(http.StatusNotFound)
		_, _ = w.Write([]byte("Not found"))
	}))

	updateFieldsCounter := 0
	mux.HandleFunc("/updatefields", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("X-Counter", strconv.Itoa(updateFieldsCounter))
		w.Header().Set("Etag", `"e"`)
		updateFieldsCounter++
		if r.Header.Get("if-none-match") != "" {
			w.WriteHeader(http.StatusNotModified)
			return
		}
		_, _ = w.Write([]byte("Some text content"))
	}))

	// Take 3 seconds to return 200 OK (for testing client timeouts).
	mux.HandleFunc("/3seconds", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		time.Sleep(3 * time.Second)
	}))

	mux.HandleFunc("/infinite", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		for {
			select {
			case <-s.done:
				return
			default:
				_, _ = w.Write([]byte{0})
			}
		}
	}))
}

func teardown() {
	close(s.done)
	s.server.Close()
}

func resetTest() {
	s.transport.Cache = NewMemoryCache()
	clock = &realClock{}
}

// TestCacheableMethod ensures that uncacheable method does not get stored
// in cache and get incorrectly used for a following cacheable method request.
func TestCacheableMethod(t *testing.T) {
	resetTest()
	{
		req, err := http.NewRequest("POST", s.server.URL+"/method", nil)
		if err != nil {
			t.Fatal(err)
		}
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		var buf bytes.Buffer
		_, err = io.Copy(&buf, resp.Body)
		if err != nil {
			t.Fatal(err)
		}
		err = resp.Body.Close()
		if err != nil {
			t.Fatal(err)
		}
		if got, want := buf.String(), "POST"; got != want {
			t.Errorf("got %q, want %q", got, want)
		}
		if resp.StatusCode != http.StatusOK {
			t.Errorf("response status code isn't 200 OK: %v", resp.StatusCode)
		}
	}
	{
		req, err := http.NewRequest("GET", s.server.URL+"/method", nil)
		if err != nil {
			t.Fatal(err)
		}
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		var buf bytes.Buffer
		_, err = io.Copy(&buf, resp.Body)
		if err != nil {
			t.Fatal(err)
		}
		err = resp.Body.Close()
		if err != nil {
			t.Fatal(err)
		}
		if got, want := buf.String(), "GET"; got != want {
			t.Errorf("got wrong body %q, want %q", got, want)
		}
		if resp.StatusCode != http.StatusOK {
			t.Errorf("response status code isn't 200 OK: %v", resp.StatusCode)
		}
		if resp.Header.Get(XFromCache) != "" {
			t.Errorf("XFromCache header isn't blank")
		}
	}
}

func TestDontServeHeadResponseToGetRequest(t *testing.T) {
	resetTest()
	url := s.server.URL + "/"
	req, err := http.NewRequest(http.MethodHead, url, nil)
	if err != nil {
		t.Fatal(err)
	}
	_, err = s.client.Do(req)
	if err != nil {
		t.Fatal(err)
	}
	req, err = http.NewRequest(http.MethodGet, url, nil)
	if err != nil {
		t.Fatal(err)
	}
	resp, err := s.client.Do(req)
	if err != nil {
		t.Fatal(err)
	}
	if resp.Header.Get(XFromCache) != "" {
		t.Errorf("Cache should not match")
	}
}

func TestDontStorePartialRangeInCache(t *testing.T) {
	resetTest()
	{
		req, err := http.NewRequest("GET", s.server.URL+"/range", nil)
		if err != nil {
			t.Fatal(err)
		}
		req.Header.Set("range", "bytes=4-9")
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		var buf bytes.Buffer
		_, err = io.Copy(&buf, resp.Body)
		if err != nil {
			t.Fatal(err)
		}
		err = resp.Body.Close()
		if err != nil {
			t.Fatal(err)
		}
		if got, want := buf.String(), " text "; got != want {
			t.Errorf("got %q, want %q", got, want)
		}
		if resp.StatusCode != http.StatusPartialContent {
			t.Errorf("response status code isn't 206 Partial Content: %v", resp.StatusCode)
		}
	}
	{
		req, err := http.NewRequest("GET", s.server.URL+"/range", nil)
		if err != nil {
			t.Fatal(err)
		}
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		var buf bytes.Buffer
		_, err = io.Copy(&buf, resp.Body)
		if err != nil {
			t.Fatal(err)
		}
		err = resp.Body.Close()
		if err != nil {
			t.Fatal(err)
		}
		if got, want := buf.String(), "Some text content"; got != want {
			t.Errorf("got %q, want %q", got, want)
		}
		if resp.StatusCode != http.StatusOK {
			t.Errorf("response status code isn't 200 OK: %v", resp.StatusCode)
		}
		if resp.Header.Get(XFromCache) != "" {
			t.Error("XFromCache header isn't blank")
		}
	}
	{
		req, err := http.NewRequest("GET", s.server.URL+"/range", nil)
		if err != nil {
			t.Fatal(err)
		}
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		var buf bytes.Buffer
		_, err = io.Copy(&buf, resp.Body)
		if err != nil {
			t.Fatal(err)
		}
		err = resp.Body.Close()
		if err != nil {
			t.Fatal(err)
		}
		if got, want := buf.String(), "Some text content"; got != want {
			t.Errorf("got %q, want %q", got, want)
		}
		if resp.StatusCode != http.StatusOK {
			t.Errorf("response status code isn't 200 OK: %v", resp.StatusCode)
		}
		if resp.Header.Get(XFromCache) != "1" {
			t.Errorf(`XFromCache header isn't "1": %v`, resp.Header.Get(XFromCache))
		}
	}
	{
		req, err := http.NewRequest("GET", s.server.URL+"/range", nil)
		if err != nil {
			t.Fatal(err)
		}
		req.Header.Set("range", "bytes=4-9")
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		var buf bytes.Buffer
		_, err = io.Copy(&buf, resp.Body)
		if err != nil {
			t.Fatal(err)
		}
		err = resp.Body.Close()
		if err != nil {
			t.Fatal(err)
		}
		if got, want := buf.String(), " text "; got != want {
			t.Errorf("got %q, want %q", got, want)
		}
		if resp.StatusCode != http.StatusPartialContent {
			t.Errorf("response status code isn't 206 Partial Content: %v", resp.StatusCode)
		}
	}
}

func TestCacheOnlyIfBodyRead(t *testing.T) {
	resetTest()
	{
		req, err := http.NewRequest("GET", s.server.URL, nil)
		if err != nil {
			t.Fatal(err)
		}
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		if resp.Header.Get(XFromCache) != "" {
			t.Fatal("XFromCache header isn't blank")
		}
		// We do not read the body
		resp.Body.Close()
	}
	{
		req, err := http.NewRequest("GET", s.server.URL, nil)
		if err != nil {
			t.Fatal(err)
		}
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.Header.Get(XFromCache) != "" {
			t.Fatalf("XFromCache header isn't blank")
		}
	}
}

func TestOnlyReadBodyOnDemand(t *testing.T) {
	resetTest()

	req, err := http.NewRequest("GET", s.server.URL+"/infinite", nil)
	if err != nil {
		t.Fatal(err)
	}
	resp, err := s.client.Do(req) // This shouldn't hang forever.
	if err != nil {
		t.Fatal(err)
	}
	buf := make([]byte, 10) // Only partially read the body.
	_, err = resp.Body.Read(buf)
	if err != nil {
		t.Fatal(err)
	}
	resp.Body.Close()
}

func TestGetOnlyIfCachedHit(t *testing.T) {
	resetTest()
	{
		req, err := http.NewRequest("GET", s.server.URL, nil)
		if err != nil {
			t.Fatal(err)
		}
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.Header.Get(XFromCache) != "" {
			t.Fatal("XFromCache header isn't blank")
		}
		_, err = ioutil.ReadAll(resp.Body)
		if err != nil {
			t.Fatal(err)
		}
	}
	{
		req, err := http.NewRequest("GET", s.server.URL, nil)
		if err != nil {
			t.Fatal(err)
		}
		req.Header.Add("cache-control", "only-if-cached")
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.Header.Get(XFromCache) != "1" {
			t.Fatalf(`XFromCache header isn't "1": %v`, resp.Header.Get(XFromCache))
		}
		if resp.StatusCode != http.StatusOK {
			t.Fatalf("response status code isn't 200 OK: %v", resp.StatusCode)
		}
	}
}

func TestGetOnlyIfCachedMiss(t *testing.T) {
	resetTest()
	req, err := http.NewRequest("GET", s.server.URL, nil)
	if err != nil {
		t.Fatal(err)
	}
	req.Header.Add("cache-control", "only-if-cached")
	resp, err := s.client.Do(req)
	if err != nil {
		t.Fatal(err)
	}
	defer resp.Body.Close()
	if resp.Header.Get(XFromCache) != "" {
		t.Fatal("XFromCache header isn't blank")
	}
	if resp.StatusCode != http.StatusGatewayTimeout {
		t.Fatalf("response status code isn't 504 GatewayTimeout: %v", resp.StatusCode)
	}
}

func TestGetNoStoreRequest(t *testing.T) {
	resetTest()
	req, err := http.NewRequest("GET", s.server.URL, nil)
	if err != nil {
		t.Fatal(err)
	}
	req.Header.Add("Cache-Control", "no-store")
	{
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.Header.Get(XFromCache) != "" {
			t.Fatal("XFromCache header isn't blank")
		}
	}
	{
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.Header.Get(XFromCache) != "" {
			t.Fatal("XFromCache header isn't blank")
		}
	}
}

func TestGetNoStoreResponse(t *testing.T) {
	resetTest()
	req, err := http.NewRequest("GET", s.server.URL+"/nostore", nil)
	if err != nil {
		t.Fatal(err)
	}
	{
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.Header.Get(XFromCache) != "" {
			t.Fatal("XFromCache header isn't blank")
		}
	}
	{
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.Header.Get(XFromCache) != "" {
			t.Fatal("XFromCache header isn't blank")
		}
	}
}

func TestGetWithEtag(t *testing.T) {
	resetTest()
	req, err := http.NewRequest("GET", s.server.URL+"/etag", nil)
	if err != nil {
		t.Fatal(err)
	}
	{
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.Header.Get(XFromCache) != "" {
			t.Fatal("XFromCache header isn't blank")
		}
		_, err = ioutil.ReadAll(resp.Body)
		if err != nil {
			t.Fatal(err)
		}

	}
	{
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.Header.Get(XFromCache) != "1" {
			t.Fatalf(`XFromCache header isn't "1": %v`, resp.Header.Get(XFromCache))
		}
		// additional assertions to verify that 304 response is converted properly
		if resp.StatusCode != http.StatusOK {
			t.Fatalf("response status code isn't 200 OK: %v", resp.StatusCode)
		}
		if _, ok := resp.Header["Connection"]; ok {
			t.Fatalf("Connection header isn't absent")
		}
	}
}

func TestGetWithLastModified(t *testing.T) {
	resetTest()
	req, err := http.NewRequest("GET", s.server.URL+"/lastmodified", nil)
	if err != nil {
		t.Fatal(err)
	}
	{
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.Header.Get(XFromCache) != "" {
			t.Fatal("XFromCache header isn't blank")
		}
		_, err = ioutil.ReadAll(resp.Body)
		if err != nil {
			t.Fatal(err)
		}
	}
	{
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.Header.Get(XFromCache) != "1" {
			t.Fatalf(`XFromCache header isn't "1": %v`, resp.Header.Get(XFromCache))
		}
	}
}

func TestGetWithVary(t *testing.T) {
	resetTest()
	req, err := http.NewRequest("GET", s.server.URL+"/varyaccept", nil)
	if err != nil {
		t.Fatal(err)
	}
	req.Header.Set("Accept", "text/plain")
	{
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.Header.Get("Vary") != "Accept" {
			t.Fatalf(`Vary header isn't "Accept": %v`, resp.Header.Get("Vary"))
		}
		_, err = ioutil.ReadAll(resp.Body)
		if err != nil {
			t.Fatal(err)
		}
	}
	{
		resp, err := s.client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.Header.Get(XFro
... [TRUNCATED]
```

### File: LICENSE.txt
```txt
Copyright © 2012 Greg Jones (greg.jones@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

### File: redis\redis.go
```go
// Package redis provides a redis interface for http caching.
package redis

import (
	"context"
	"time"

	"github.com/bitcomplete/httpcache"
	"github.com/go-redis/redis/v8"
)

// cache is an implementation of httpcache.Cache that caches responses in a
// redis server.
type cache struct {
	client     *redis.Client
	expiration time.Duration
}

// cacheKey modifies an httpcache key for use in redis. Specifically, it
// prefixes keys to avoid collision with other data stored in redis.
func cacheKey(key string) string {
	return "rediscache:" + key
}

// Get returns the response corresponding to key if present.
func (c cache) Get(ctx context.Context, key string) (resp []byte, ok bool) {
	item, err := c.client.Get(ctx, cacheKey(key)).Bytes()
	if err != nil {
		return nil, false
	}
	return item, true
}

// Set saves a response to the cache as key.
func (c cache) Set(ctx context.Context, key string, resp []byte) {
	c.client.Set(ctx, cacheKey(key), resp, c.expiration)
}

// Delete removes the response with key from the cache.
func (c cache) Delete(ctx context.Context, key string) {
	c.client.Del(ctx, cacheKey(key))
}

// Opt is a configuration option for creating a new Redis cache
type Opt func(*cache)

// ExpirationOpt configures a Redis cache by setting its expiration
func ExpirationOpt(expiration time.Duration) Opt {
	return func(c *cache) {
		c.expiration = expiration
	}
}

// NewWithClient returns a new Cache with the given redis connection.
func NewWithClient(client *redis.Client, opts ...Opt) httpcache.Cache {
	c := cache{client: client}
	for _, opt := range opts {
		opt(&c)
	}
	return c
}

```

### File: redis\redis_test.go
```go
package redis

import (
	"context"
	"testing"

	"github.com/bitcomplete/httpcache/test"
	"github.com/go-redis/redis/v8"
)

func TestRedisCache(t *testing.T) {
	client := redis.NewClient(&redis.Options{
		Addr: "localhost:6379",
	})
	if err := client.Ping(context.Background()).Err(); err != nil {
		// TODO: rather than skip the test, fall back to a faked redis server
		t.Skipf("skipping test; no server running at localhost:6379")
	}
	client.FlushAll(context.Background())

	test.Cache(t, NewWithClient(client))
}

```

### File: test\test.go
```go
package test

import (
	"bytes"
	"context"
	"testing"

	"github.com/bitcomplete/httpcache"
)

// Cache excercises a httpcache.Cache implementation.
func Cache(t *testing.T, cache httpcache.Cache) {
	key := "testKey"
	_, ok := cache.Get(context.Background(), key)
	if ok {
		t.Fatal("retrieved key before adding it")
	}

	val := []byte("some bytes")
	cache.Set(context.Background(), key, val)

	retVal, ok := cache.Get(context.Background(), key)
	if !ok {
		t.Fatal("could not retrieve an element we just added")
	}
	if !bytes.Equal(retVal, val) {
		t.Fatal("retrieved a different value than what we put in")
	}

	cache.Delete(context.Background(), key)

	_, ok = cache.Get(context.Background(), key)
	if ok {
		t.Fatal("deleted key still present")
	}
}

```

### File: test\test_test.go
```go
package test_test

import (
	"testing"

	"github.com/bitcomplete/httpcache"
	"github.com/bitcomplete/httpcache/test"
)

func TestMemoryCache(t *testing.T) {
	test.Cache(t, httpcache.NewMemoryCache())
}

```

### File: .github\workflows\go.yaml
```yaml
name: go
on: push
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: golangci-lint
        uses: golangci/golangci-lint-action@v2
        with:
          version: v1.46.2

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-go@v2
        with:
          go-version: "^1.18"
      - run: go test -v -race ./...

```

