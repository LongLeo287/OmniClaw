---
id: colly-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:09.315183
---

# KNOWLEDGE EXTRACT: colly
> **Extracted on:** 2026-03-30 13:34:10
> **Source:** colly

---

## File: `.codecov.yml`
```yaml
comment: false
```

## File: `CHANGELOG.md`
```markdown
# 2.1.0 - 2020.06.09

 - HTTP tracing support
 - New callback: OnResponseHeader
 - Queue fixes
 - New collector option: Collector.CheckHead
 - Proxy fixes
 - Fixed POST revisit checking
 - Updated dependencies

# 2.0.0 - 2019.11.28

 - Breaking change: Change Collector.RedirectHandler member to Collector.SetRedirectHandler function
 - Go module support
 - Collector.HasVisited method added to be able to check if an url has been visited
 - Collector.SetClient method introduced
 - HTMLElement.ChildTexts method added
 - New user agents
 - Multiple bugfixes

# 1.2.0 - 2019.02.13

 - Compatibility with the latest htmlquery package
 - New request shortcut for HEAD requests
 - Check URL availability before visiting
 - Fix proxy URL value
 - Request counter fix
 - Minor fixes in examples

# 1.1.0 - 2018.08.13

 - Appengine integration takes context.Context instead of http.Request (API change)
 - Added "Accept" http header by default to every request
 - Support slices of pointers in unmarshal
 - Fixed a race condition in queues
 - ForEachWithBreak method added to HTMLElement
 - Added a local file example
 - Support gzip decompression of response bodies
 - Don't share waitgroup when cloning a collector
 - Fixed instagram example


# 1.0.0 - 2018.05.13
```

## File: `colly.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Package colly implements a HTTP scraping framework
package colly

import (
	"bytes"
	"context"
	"crypto/rand"
	"encoding/json"
	"errors"
	"fmt"
	"hash/fnv"
	"io"
	"log"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"os"
	"path/filepath"
	"regexp"
	"slices"
	"strconv"
	"strings"
	"sync"
	"sync/atomic"
	"time"

	"github.com/PuerkitoBio/goquery"
	"github.com/antchfx/htmlquery"
	"github.com/antchfx/xmlquery"
	"github.com/gocolly/colly/v2/debug"
	"github.com/gocolly/colly/v2/storage"
	"github.com/kennygrant/sanitize"
	whatwgUrl "github.com/nlnwa/whatwg-url/url"
	"github.com/temoto/robotstxt"
	"google.golang.org/appengine/urlfetch"
)

// A CollectorOption sets an option on a Collector.
type CollectorOption func(*Collector)

// Collector provides the scraper instance for a scraping job
type Collector struct {
	// UserAgent is the User-Agent string used by HTTP requests
	UserAgent string
	// Custom headers for the request
	Headers *http.Header
	// MaxDepth limits the recursion depth of visited URLs.
	// Set it to 0 for infinite recursion (default).
	MaxDepth int
	// AllowedDomains is a domain whitelist.
	// Leave it blank to allow any domains to be visited
	AllowedDomains []string
	// DisallowedDomains is a domain blacklist.
	DisallowedDomains []string
	// DisallowedURLFilters is a list of regular expressions which restricts
	// visiting URLs. If any of the rules matches to a URL the
	// request will be stopped. DisallowedURLFilters will
	// be evaluated before URLFilters
	// Leave it blank to allow any URLs to be visited
	DisallowedURLFilters []*regexp.Regexp
	// URLFilters is a list of regular expressions which restricts
	// visiting URLs. If any of the rules matches to a URL the
	// request won't be stopped. DisallowedURLFilters will
	// be evaluated before URLFilters

	// Leave it blank to allow any URLs to be visited
	URLFilters []*regexp.Regexp

	// AllowURLRevisit allows multiple downloads of the same URL
	AllowURLRevisit bool
	// MaxBodySize is the limit of the retrieved response body in bytes.
	// 0 means unlimited.
	// The default value for MaxBodySize is 10MB (10 * 1024 * 1024 bytes).
	MaxBodySize int
	// CacheDir specifies a location where GET requests are cached as files.
	// When it's not defined, caching is disabled.
	CacheDir string
	// IgnoreRobotsTxt allows the Collector to ignore any restrictions set by
	// the target host's robots.txt file.  See http://www.robotstxt.org/ for more
	// information.
	IgnoreRobotsTxt bool
	// Async turns on asynchronous network communication. Use Collector.Wait() to
	// be sure all requests have been finished.
	Async bool
	// ParseHTTPErrorResponse allows parsing HTTP responses with non 2xx status codes.
	// By default, Colly parses only successful HTTP responses. Set ParseHTTPErrorResponse
	// to true to enable it.
	ParseHTTPErrorResponse bool
	// ID is the unique identifier of a collector
	ID uint32
	// DetectCharset can enable character encoding detection for non-utf8 response bodies
	// without explicit charset declaration. This feature uses https://github.com/saintfish/chardet
	DetectCharset bool
	// RedirectHandler allows control on how a redirect will be managed
	// use c.SetRedirectHandler to set this value
	redirectHandler func(req *http.Request, via []*http.Request) error
	// CheckHead performs a HEAD request before every GET to pre-validate the response
	CheckHead bool
	// TraceHTTP enables capturing and reporting request performance for crawler tuning.
	// When set to true, the Response.Trace will be filled in with an HTTPTrace object.
	TraceHTTP bool
	// Context is the context that will be used for HTTP requests. You can set this
	// to support clean cancellation of scraping.
	Context context.Context
	// MaxRequests limit the number of requests done by the instance.
	// Set it to 0 for infinite requests (default).
	MaxRequests uint32

	store                    storage.Storage
	debugger                 debug.Debugger
	robotsMap                map[string]*robotstxt.RobotsData
	htmlCallbacks            []*htmlCallbackContainer
	xmlCallbacks             []*xmlCallbackContainer
	requestCallbacks         []RequestCallback
	responseCallbacks        []ResponseCallback
	responseHeadersCallbacks []ResponseHeadersCallback
	requestHeadersCallbacks  []RequestCallback
	errorCallbacks           []ErrorCallback
	scrapedCallbacks         []ScrapedCallback
	requestCount             atomic.Uint32
	responseCount            atomic.Uint32
	backend                  *httpBackend
	wg                       *sync.WaitGroup
	lock                     *sync.RWMutex
	// CacheExpiration sets the maximum age for cache files.
	// If a cached file is older than this duration, it will be ignored and refreshed.
	CacheExpiration time.Duration
}

// RequestCallback is a type alias for OnRequest callback functions
type RequestCallback func(*Request)

// ResponseHeadersCallback is a type alias for OnResponseHeaders callback functions
type ResponseHeadersCallback func(*Response)

// ResponseCallback is a type alias for OnResponse callback functions
type ResponseCallback func(*Response)

// HTMLCallback is a type alias for OnHTML callback functions
type HTMLCallback func(*HTMLElement)

// XMLCallback is a type alias for OnXML callback functions
type XMLCallback func(*XMLElement)

// ErrorCallback is a type alias for OnError callback functions
type ErrorCallback func(*Response, error)

// ScrapedCallback is a type alias for OnScraped callback functions
type ScrapedCallback func(*Response)

// ProxyFunc is a type alias for proxy setter functions.
type ProxyFunc func(*http.Request) (*url.URL, error)

// AlreadyVisitedError is the error type for already visited URLs.
//
// It's returned synchronously by Visit when the URL passed to Visit
// is already visited.
//
// When already visited URL is encountered after following
// redirects, this error appears in OnError callback, and if Async
// mode is not enabled, is also returned by Visit.
type AlreadyVisitedError struct {
	// Destination is the URL that was attempted to be visited.
	// It might not match the URL passed to Visit if redirect
	// was followed.
	Destination *url.URL
}

// Error implements error interface.
func (e *AlreadyVisitedError) Error() string {
	return fmt.Sprintf("%q already visited", e.Destination)
}

type htmlCallbackContainer struct {
	Selector string
	Function HTMLCallback
	active   atomic.Bool
}

type xmlCallbackContainer struct {
	Query    string
	Function XMLCallback
	active   atomic.Bool
}

type cookieJarSerializer struct {
	store storage.Storage
	lock  *sync.RWMutex
}

var collectorCounter uint32

// The key type is unexported to prevent collisions with context keys defined in
// other packages.
type key int

// ProxyURLKey is the context key for the request proxy address.
const (
	ProxyURLKey key = iota
	CheckRevisitKey
)

// The prefix for environment variables of Colly settings
const envVariablePrefix = "COLLY_"

var (
	// ErrForbiddenDomain is the error thrown if visiting
	// a domain which is not allowed in AllowedDomains
	ErrForbiddenDomain = errors.New("Forbidden domain")
	// ErrMissingURL is the error type for missing URL errors
	ErrMissingURL = errors.New("Missing URL")
	// ErrMaxDepth is the error type for exceeding max depth
	ErrMaxDepth = errors.New("Max depth limit reached")
	// ErrForbiddenURL is the error thrown if visiting
	// a URL which is not allowed by URLFilters
	ErrForbiddenURL = errors.New("ForbiddenURL")

	// ErrNoURLFiltersMatch is the error thrown if visiting
	// a URL which is not allowed by URLFilters
	ErrNoURLFiltersMatch = errors.New("No URLFilters match")
	// ErrRobotsTxtBlocked is the error type for robots.txt errors
	ErrRobotsTxtBlocked = errors.New("URL blocked by robots.txt")
	// ErrNoCookieJar is the error type for missing cookie jar
	ErrNoCookieJar = errors.New("Cookie jar is not available")
	// ErrNoPattern is the error type for LimitRules without patterns
	ErrNoPattern = errors.New("No pattern defined in LimitRule")
	// ErrEmptyProxyURL is the error type for empty Proxy URL list
	ErrEmptyProxyURL = errors.New("Proxy URL list is empty")
	// ErrAbortedAfterHeaders is the error returned when OnResponseHeaders aborts the transfer.
	ErrAbortedAfterHeaders = errors.New("Aborted after receiving response headers")
	// ErrAbortedBeforeRequest is the error returned when OnResponseHeaders aborts the transfer.
	ErrAbortedBeforeRequest = errors.New("Aborted before Do Request")
	// ErrQueueFull is the error returned when the queue is full
	ErrQueueFull = errors.New("Queue MaxSize reached")
	// ErrMaxRequests is the error returned when exceeding max requests
	ErrMaxRequests = errors.New("Max Requests limit reached")
	// ErrRetryBodyUnseekable is the error when retry with not seekable body
	ErrRetryBodyUnseekable = errors.New("Retry Body Unseekable")
)

var envMap = map[string]func(*Collector, string){
	"ALLOWED_DOMAINS": func(c *Collector, val string) {
		c.AllowedDomains = strings.Split(val, ",")
	},
	"CACHE_DIR": func(c *Collector, val string) {
		c.CacheDir = val
	},
	"DETECT_CHARSET": func(c *Collector, val string) {
		c.DetectCharset = isYesString(val)
	},
	"DISABLE_COOKIES": func(c *Collector, _ string) {
		c.backend.Client.Jar = nil
	},
	"DISALLOWED_DOMAINS": func(c *Collector, val string) {
		c.DisallowedDomains = strings.Split(val, ",")
	},
	"IGNORE_ROBOTSTXT": func(c *Collector, val string) {
		c.IgnoreRobotsTxt = isYesString(val)
	},
	"FOLLOW_REDIRECTS": func(c *Collector, val string) {
		if !isYesString(val) {
			c.redirectHandler = func(req *http.Request, via []*http.Request) error {
				return http.ErrUseLastResponse
			}
		}
	},
	"MAX_BODY_SIZE": func(c *Collector, val string) {
		size, err := strconv.Atoi(val)
		if err == nil {
			c.MaxBodySize = size
		}
	},
	"MAX_DEPTH": func(c *Collector, val string) {
		maxDepth, err := strconv.Atoi(val)
		if err == nil {
			c.MaxDepth = maxDepth
		}
	},
	"MAX_REQUESTS": func(c *Collector, val string) {
		maxRequests, err := strconv.ParseUint(val, 0, 32)
		if err == nil {
			c.MaxRequests = uint32(maxRequests)
		}
	},
	"PARSE_HTTP_ERROR_RESPONSE": func(c *Collector, val string) {
		c.ParseHTTPErrorResponse = isYesString(val)
	},
	"TRACE_HTTP": func(c *Collector, val string) {
		c.TraceHTTP = isYesString(val)
	},
	"USER_AGENT": func(c *Collector, val string) {
		c.UserAgent = val
	},
}

var urlParser = whatwgUrl.NewParser(whatwgUrl.WithPercentEncodeSinglePercentSign())

// NewCollector creates a new Collector instance with default configuration
func NewCollector(options ...CollectorOption) *Collector {
	c := &Collector{}
	c.Init()

	for _, f := range options {
		f(c)
	}

	c.parseSettingsFromEnv()

	return c
}

// UserAgent sets the user agent used by the Collector.
func UserAgent(ua string) CollectorOption {
	return func(c *Collector) {
		c.UserAgent = ua
	}
}

// Headers sets the custom headers used by the Collector.
func Headers(headers map[string]string) CollectorOption {
	return func(c *Collector) {
		customHeaders := make(http.Header)
		for header, value := range headers {
			customHeaders.Add(header, value)
		}
		c.Headers = &customHeaders
	}
}

// MaxDepth limits the recursion depth of visited URLs.
func MaxDepth(depth int) CollectorOption {
	return func(c *Collector) {
		c.MaxDepth = depth
	}
}

// MaxRequests limit the number of requests done by the instance.
// Set it to 0 for infinite requests (default).
func MaxRequests(max uint32) CollectorOption {
	return func(c *Collector) {
		c.MaxRequests = max
	}
}

// AllowedDomains sets the domain whitelist used by the Collector.
func AllowedDomains(domains ...string) CollectorOption {
	return func(c *Collector) {
		c.AllowedDomains = domains
	}
}

// ParseHTTPErrorResponse allows parsing responses with HTTP errors
func ParseHTTPErrorResponse() CollectorOption {
	return func(c *Collector) {
		c.ParseHTTPErrorResponse = true
	}
}

// DisallowedDomains sets the domain blacklist used by the Collector.
func DisallowedDomains(domains ...string) CollectorOption {
	return func(c *Collector) {
		c.DisallowedDomains = domains
	}
}

// DisallowedURLFilters sets the list of regular expressions which restricts
// visiting URLs. If any of the rules matches to a URL the request will be stopped.
func DisallowedURLFilters(filters ...*regexp.Regexp) CollectorOption {
	return func(c *Collector) {
		c.DisallowedURLFilters = filters
	}
}

// URLFilters sets the list of regular expressions which restricts
// visiting URLs. If any of the rules matches to a URL the request won't be stopped.
func URLFilters(filters ...*regexp.Regexp) CollectorOption {
	return func(c *Collector) {
		c.URLFilters = filters
	}
}

// AllowURLRevisit instructs the Collector to allow multiple downloads of the same URL
func AllowURLRevisit() CollectorOption {
	return func(c *Collector) {
		c.AllowURLRevisit = true
	}
}

// MaxBodySize sets the limit of the retrieved response body in bytes.
func MaxBodySize(sizeInBytes int) CollectorOption {
	return func(c *Collector) {
		c.MaxBodySize = sizeInBytes
	}
}

// CacheDir specifies the location where GET requests are cached as files.
func CacheDir(path string) CollectorOption {
	return func(c *Collector) {
		c.CacheDir = path
	}
}

// IgnoreRobotsTxt instructs the Collector to ignore any restrictions
// set by the target host's robots.txt file.
func IgnoreRobotsTxt() CollectorOption {
	return func(c *Collector) {
		c.IgnoreRobotsTxt = true
	}
}

// TraceHTTP instructs the Collector to collect and report request trace data
// on the Response.Trace.
func TraceHTTP() CollectorOption {
	return func(c *Collector) {
		c.TraceHTTP = true
	}
}

// StdlibContext sets the context that will be used for HTTP requests.
// You can set this to support clean cancellation of scraping.
func StdlibContext(ctx context.Context) CollectorOption {
	return func(c *Collector) {
		c.Context = ctx
	}
}

// ID sets the unique identifier of the Collector.
func ID(id uint32) CollectorOption {
	return func(c *Collector) {
		c.ID = id
	}
}

// Async turns on asynchronous network requests.
func Async(a ...bool) CollectorOption {
	return func(c *Collector) {
		if len(a) > 0 {
			c.Async = a[0]
		} else {
			c.Async = true
		}
	}
}

// DetectCharset enables character encoding detection for non-utf8 response bodies
// without explicit charset declaration. This feature uses https://github.com/saintfish/chardet
func DetectCharset() CollectorOption {
	return func(c *Collector) {
		c.DetectCharset = true
	}
}

// Debugger sets the debugger used by the Collector.
func Debugger(d debug.Debugger) CollectorOption {
	return func(c *Collector) {
		d.Init()
		c.debugger = d
	}
}

// CheckHead performs a HEAD request before every GET to pre-validate the response
func CheckHead() CollectorOption {
	return func(c *Collector) {
		c.CheckHead = true
	}
}

// CacheExpiration sets the maximum age for cache files.
// If a cached file is older than this duration, it will be ignored and refreshed.
func CacheExpiration(d time.Duration) CollectorOption {
	return func(c *Collector) {
		c.CacheExpiration = d
	}
}

// Init initializes the Collector's private variables and sets default
// configuration for the Collector
func (c *Collector) Init() {
	c.UserAgent = "colly - https://github.com/gocolly/colly"
	c.Headers = nil
	c.MaxDepth = 0
	c.MaxRequests = 0
	c.store = &storage.InMemoryStorage{}
	c.store.Init()
	c.MaxBodySize = 10 * 1024 * 1024
	c.backend = &httpBackend{}
	jar, _ := cookiejar.New(nil)
	c.backend.Init(jar)
	c.backend.Client.CheckRedirect = c.checkRedirectFunc()
	c.wg = &sync.WaitGroup{}
	c.lock = &sync.RWMutex{}
	c.robotsMap = make(map[string]*robotstxt.RobotsData)
	c.IgnoreRobotsTxt = true
	c.ID = atomic.AddUint32(&collectorCounter, 1)
	c.TraceHTTP = false
	c.Context = context.Background()
}

// Appengine will replace the Collector's backend http.Client
// With an Http.Client that is provided by appengine/urlfetch
// This function should be used when the scraper is run on
// Google App Engine. Example:
//
//	func startScraper(w http.ResponseWriter, r *http.Request) {
//	  ctx := appengine.NewContext(r)
//	  c := colly.NewCollector()
//	  c.Appengine(ctx)
//	   ...
//	  c.Visit("https://google.ca")
//	}
func (c *Collector) Appengine(ctx context.Context) {
	client := urlfetch.Client(ctx)
	client.Jar = c.backend.Client.Jar
	client.CheckRedirect = c.backend.Client.CheckRedirect
	client.Timeout = c.backend.Client.Timeout

	c.backend.Client = client
}

// Visit starts Collector's collecting job by creating a
// request to the URL specified in parameter.
// Visit also calls the previously provided callbacks
func (c *Collector) Visit(URL string) error {
	if c.CheckHead {
		if check := c.scrape(URL, "HEAD", 1, nil, nil, nil, true); check != nil {
			return check
		}
	}
	return c.scrape(URL, "GET", 1, nil, nil, nil, true)
}

// HasVisited checks if the provided URL has been visited
func (c *Collector) HasVisited(URL string) (bool, error) {
	return c.checkHasVisited(URL, nil)
}

// HasPosted checks if the provided URL and requestData has been visited
// This method is useful more likely to prevent re-visit same URL and POST body
func (c *Collector) HasPosted(URL string, requestData map[string]string) (bool, error) {
	return c.checkHasVisited(URL, requestData)
}

// Head starts a collector job by creating a HEAD request.
func (c *Collector) Head(URL string) error {
	return c.scrape(URL, "HEAD", 1, nil, nil, nil, false)
}

// Post starts a collector job by creating a POST request.
// Post also calls the previously provided callbacks
func (c *Collector) Post(URL string, requestData map[string]string) error {
	return c.scrape(URL, "POST", 1, createFormReader(requestData), nil, nil, true)
}

// PostRaw starts a collector job by creating a POST request with raw binary data.
// Post also calls the previously provided callbacks
func (c *Collector) PostRaw(URL string, requestData []byte) error {
	return c.scrape(URL, "POST", 1, bytes.NewReader(requestData), nil, nil, true)
}

// PostMultipart starts a collector job by creating a Multipart POST request
// with raw binary data.  PostMultipart also calls the previously provided callbacks
func (c *Collector) PostMultipart(URL string, requestData map[string][]byte) error {
	boundary := randomBoundary()
	hdr := http.Header{}
	hdr.Set("Content-Type", "multipart/form-data; boundary="+boundary)
	hdr.Set("User-Agent", c.UserAgent)
	return c.scrape(URL, "POST", 1, createMultipartReader(boundary, requestData), nil, hdr, true)
}

// Request starts a collector job by creating a custom HTTP request
// where method, context, headers and request data can be specified.
// Set requestData, ctx, hdr parameters to nil if you don't want to use them.
// Valid methods:
//   - "GET"
//   - "HEAD"
//   - "POST"
//   - "PUT"
//   - "DELETE"
//   - "PATCH"
//   - "OPTIONS"
func (c *Collector) Request(method, URL string, requestData io.Reader, ctx *Context, hdr http.Header) error {
	return c.scrape(URL, method, 1, requestData, ctx, hdr, true)
}

// SetDebugger attaches a debugger to the collector
func (c *Collector) SetDebugger(d debug.Debugger) {
	d.Init()
	c.debugger = d
}

// UnmarshalRequest creates a Request from serialized data
func (c *Collector) UnmarshalRequest(r []byte) (*Request, error) {
	req := &serializableRequest{}
	err := json.Unmarshal(r, req)
	if err != nil {
		return nil, err
	}

	u, err := url.Parse(req.URL)
	if err != nil {
		return nil, err
	}

	ctx := NewContext()
	for k, v := range req.Ctx {
		ctx.Put(k, v)
	}

	return &Request{
		Method:    req.Method,
		URL:       u,
		Depth:     req.Depth,
		Body:      bytes.NewReader(req.Body),
		Ctx:       ctx,
		ID:        c.requestCount.Add(1),
		Headers:   &req.Headers,
		collector: c,
	}, nil
}

func (c *Collector) scrape(u, method string, depth int, requestData io.Reader, ctx *Context, hdr http.Header, checkRevisit bool) error {
	parsedWhatwgURL, err := urlParser.Parse(u)
	if err != nil {
		return err
	}
	parsedURL, err := url.Parse(parsedWhatwgURL.Href(false))
	if err != nil {
		return err
	}
	if hdr == nil {
		hdr = http.Header{}
		if c.Headers != nil {
			for k, v := range *c.Headers {
				for _, value := range v {
					hdr.Add(k, value)
				}
			}
		}
	}
	if _, ok := hdr["User-Agent"]; !ok {
		hdr.Set("User-Agent", c.UserAgent)
	}
	if seeker, ok := requestData.(io.ReadSeeker); ok {
		_, err := seeker.Seek(0, io.SeekStart)
		if err != nil {
			return err
		}
	}

	req, err := http.NewRequest(method, parsedURL.String(), requestData)
	if err != nil {
		return err
	}
	req.Header = hdr
	// The Go HTTP API ignores "Host" in the headers, preferring the client
	// to use the Host field on Request.
	if hostHeader := hdr.Get("Host"); hostHeader != "" {
		req.Host = hostHeader
	}
	// note: once 1.13 is minimum supported Go version,
	// replace this with http.NewRequestWithContext
	req = req.WithContext(context.WithValue(c.Context, CheckRevisitKey, checkRevisit))

	if err := c.requestCheck(parsedURL, method, req.GetBody, depth, checkRevisit); err != nil {
		return err
	}
	u = parsedURL.String()
	c.wg.Add(1)
	if c.Async {
		go c.fetch(u, method, depth, requestData, ctx, hdr, req)
		return nil
	}
	return c.fetch(u, method, depth, requestData, ctx, hdr, req)
}

func (c *Collector) fetch(u, method string, depth int, requestData io.Reader, ctx *Context, hdr http.Header, req *http.Request) error {
	defer c.wg.Done()
	if ctx == nil {
		ctx = NewContext()
	}
	request := &Request{
		URL:       req.URL,
		Headers:   &req.Header,
		Host:      req.Host,
		Ctx:       ctx,
		Depth:     depth,
		Method:    method,
		Body:      requestData,
		collector: c,
		ID:        c.requestCount.Add(1),
	}

	if req.Header.Get("Accept") == "" {
		req.Header.Set("Accept", "*/*")
	}

	c.handleOnRequest(request)

	if request.abort {
		return nil
	}

	if method == "POST" && req.Header.Get("Content-Type") == "" {
		req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
	}

	var hTrace *HTTPTrace
	if c.TraceHTTP {
		hTrace = &HTTPTrace{}
		req = hTrace.WithTrace(req)
	}
	origURL := req.URL
	checkResponseHeadersFunc := func(req *http.Request, statusCode int, headers http.Header) bool {
		if req.URL != origURL {
			request.URL = req.URL
			request.Headers = &req.Header
		}
		c.handleOnResponseHeaders(&Response{Ctx: ctx, Request: request, StatusCode: statusCode, Headers: &headers})
		return !request.abort
	}
	checkRequestHeadersFunc := func(req *http.Request) bool {
		c.handleOnRequestHeaders(request)
		return !request.abort
	}
	response, err := c.backend.Cache(req, c.MaxBodySize, checkRequestHeadersFunc, checkResponseHeadersFunc, c.CacheDir, c.CacheExpiration)
	if proxyURL, ok := req.Context().Value(ProxyURLKey).(string); ok {
		request.ProxyURL = proxyURL
	}
	if err := c.handleOnError(response, err, request, ctx); err != nil {
		return err
	}
	c.responseCount.Add(1)
	response.Ctx = ctx
	response.Request = request
	response.Trace = hTrace

	err = response.fixCharset(c.DetectCharset, request.ResponseCharacterEncoding)
	if err != nil {
		return err
	}

	c.handleOnResponse(response)

	err = c.handleOnHTML(response)
	if err != nil {
		c.handleOnError(response, err, request, ctx)
	}

	err = c.handleOnXML(response)
	if err != nil {
		c.handleOnError(response, err, request, ctx)
	}

	c.handleOnScraped(response)

	return err
}

func (c *Collector) requestCheck(parsedURL *url.URL, method string, getBody func() (io.ReadCloser, error), depth int, checkRevisit bool) error {
	u := parsedURL.String()
	if c.MaxDepth > 0 && c.MaxDepth < depth {
		return ErrMaxDepth
	}
	if c.MaxRequests > 0 && c.requestCount.Load() >= c.MaxRequests {
		return ErrMaxRequests
	}
	if err := c.checkFilters(u, parsedURL.Hostname()); err != nil {
		return err
	}
	if method != "HEAD" && !c.IgnoreRobotsTxt {
		if err := c.checkRobots(parsedURL); err != nil {
			return err
		}
	}
	if checkRevisit && !c.AllowURLRevisit {
		// TODO weird behaviour, it allows CheckHead to work correctly,
		// but it should probably better be solved with
		// "check-but-not-save" flag or something
		if method != "GET" && getBody == nil {
			return nil
		}

		var body io.ReadCloser
		if getBody != nil {
			var err error
			body, err = getBody()
			if err != nil {
				return err
			}
			defer body.Close()
		}
		uHash := requestHash(u, body)
		visited, err := c.store.IsVisited(uHash)
		if err != nil {
			return err
		}
		if visited {
			return &AlreadyVisitedError{parsedURL}
		}
		return c.store.Visited(uHash)
	}
	return nil
}

func (c *Collector) checkFilters(URL, domain string) error {
	if len(c.DisallowedURLFilters) > 0 {
		if isMatchingFilter(c.DisallowedURLFilters, []byte(URL)) {
			return ErrForbiddenURL
		}
	}
	if len(c.URLFilters) > 0 {
		if !isMatchingFilter(c.URLFilters, []byte(URL)) {
			return ErrNoURLFiltersMatch
		}
	}
	if !c.isDomainAllowed(domain) {
		return ErrForbiddenDomain
	}
	return nil
}

func (c *Collector) isDomainAllowed(domain string) bool {
	if slices.Contains(c.DisallowedDomains, domain) {
		return false
	}
	if c.AllowedDomains == nil || len(c.AllowedDomains) == 0 {
		return true
	}
	return slices.Contains(c.AllowedDomains, domain)
}

func (c *Collector) checkRobots(u *url.URL) error {
	c.lock.RLock()
	robot, ok := c.robotsMap[u.Host]
	c.lock.RUnlock()

	if !ok {
		// no robots file cached

		// Prepare request,
		req, err := http.NewRequest("GET", u.Scheme+"://"+u.Host+"/robots.txt", nil)
		if err != nil {
			return err
		}
		hdr := http.Header{}
		if c.Headers != nil {
			for k, v := range *c.Headers {
				for _, value := range v {
					hdr.Add(k, value)
				}
			}
		}
		if _, ok := hdr["User-Agent"]; !ok {
			hdr.Set("User-Agent", c.UserAgent)
		}
		req.Header = hdr
		// The Go HTTP API ignores "Host" in the headers, preferring the client
		// to use the Host field on Request.
		if hostHeader := hdr.Get("Host"); hostHeader != "" {
			req.Host = hostHeader
		}

		resp, err := c.backend.Client.Do(req)
		if err != nil {
			return err
		}
		defer resp.Body.Close()

		robot, err = robotstxt.FromResponse(resp)
		if err != nil {
			return err
		}
		c.lock.Lock()
		c.robotsMap[u.Host] = robot
		c.lock.Unlock()
	}

	uaGroup := robot.FindGroup(c.UserAgent)
	if uaGroup == nil {
		return nil
	}

	eu := u.EscapedPath()
	if u.RawQuery != "" {
		eu += "?" + u.Query().Encode()
	}
	if !uaGroup.Test(eu) {
		return ErrRobotsTxtBlocked
	}
	return nil
}

// String is the text representation of the collector.
// It contains useful debug information about the collector's internals
func (c *Collector) String() string {
	return fmt.Sprintf(
		"Requests made: %d (%d responses) | Callbacks: OnRequest: %d, OnHTML: %d, OnResponse: %d, OnError: %d",
		c.requestCount.Load(),
		c.responseCount.Load(),
		len(c.requestCallbacks),
		len(c.htmlCallbacks),
		len(c.responseCallbacks),
		len(c.errorCallbacks),
	)
}

// Wait returns when the collector jobs are finished
func (c *Collector) Wait() {
	c.wg.Wait()
}

// OnRequest registers a function. Function will be executed on every
// request made by the Collector
func (c *Collector) OnRequest(f RequestCallback) {
	c.lock.Lock()
	if c.requestCallbacks == nil {
		c.requestCallbacks = make([]RequestCallback, 0, 4)
	}
	c.requestCallbacks = append(c.requestCallbacks, f)
	c.lock.Unlock()
}

// OnResponseHeaders registers a function. Function will be executed on every response
// when headers and status are already received, but body is not yet read.
//
// Like in OnRequest, you can call Request.Abort to abort the transfer. This might be
// useful if, for example, you're following all hyperlinks, but want to avoid
// downloading files.
//
// Be aware that using this will prevent HTTP/1.1 connection reuse, as
// the only way to abort a download is to immediately close the connection.
// HTTP/2 doesn't suffer from this problem, as it's possible to close
// specific stream inside the connection.
func (c *Collector) OnResponseHeaders(f ResponseHeadersCallback) {
	c.lock.Lock()
	c.responseHeadersCallbacks = append(c.responseHeadersCallbacks, f)
	c.lock.Unlock()
}

// OnRequestHeaders registers a function. Function will be executed on every
// request made by the Collector before Request Do
func (c *Collector) OnRequestHeaders(f RequestCallback) {
	c.lock.Lock()
	c.requestHeadersCallbacks = append(c.requestHeadersCallbacks, f)
	c.lock.Unlock()
}

// OnResponse registers a function. Function will be executed on every response
func (c *Collector) OnResponse(f ResponseCallback) {
	c.lock.Lock()
	if c.responseCallbacks == nil {
		c.responseCallbacks = make([]ResponseCallback, 0, 4)
	}
	c.responseCallbacks = append(c.responseCallbacks, f)
	c.lock.Unlock()
}

// OnHTML registers a function. Function will be executed on every HTML
// element matched by the GoQuery Selector parameter.
// GoQuery Selector is a selector used by https://github.com/PuerkitoBio/goquery
func (c *Collector) OnHTML(goquerySelector string, f HTMLCallback) {
	c.lock.Lock()
	if c.htmlCallbacks == nil {
		c.htmlCallbacks = make([]*htmlCallbackContainer, 0, 4)
	}
	cc := &htmlCallbackContainer{
		Selector: goquerySelector,
		Function: f,
	}
	cc.active.Store(true)
	c.htmlCallbacks = append(c.htmlCallbacks, cc)
	c.lock.Unlock()
}

// OnXML registers a function. Function will be executed on every XML
// element matched by the xpath Query parameter.
// xpath Query is used by https://github.com/antchfx/xmlquery
func (c *Collector) OnXML(xpathQuery string, f XMLCallback) {
	c.lock.Lock()
	if c.xmlCallbacks == nil {
		c.xmlCallbacks = make([]*xmlCallbackContainer, 0, 4)
	}
	cc := &xmlCallbackContainer{
		Query:    xpathQuery,
		Function: f,
	}
	cc.active.Store(true)
	c.xmlCallbacks = append(c.xmlCallbacks, cc)
	c.lock.Unlock()
}

// OnHTMLDetach deregister a function. Function will not be execute after detached
func (c *Collector) OnHTMLDetach(goquerySelector string) {
	c.lock.Lock()
	defer c.lock.Unlock()

	for _, cc := range c.htmlCallbacks {
		if cc.Selector == goquerySelector {
			cc.active.Store(false)
		}
	}
}

// OnXMLDetach deregister a function. Function will not be execute after detached
func (c *Collector) OnXMLDetach(xpathQuery string) {
	c.lock.Lock()
	defer c.lock.Unlock()

	for _, cc := range c.xmlCallbacks {
		if cc.Query == xpathQuery {
			cc.active.Store(false)
		}
	}
}

// OnError registers a function. Function will be executed if an error
// occurs during the HTTP request.
func (c *Collector) OnError(f ErrorCallback) {
	c.lock.Lock()
	if c.errorCallbacks == nil {
		c.errorCallbacks = make([]ErrorCallback, 0, 4)
	}
	c.errorCallbacks = append(c.errorCallbacks, f)
	c.lock.Unlock()
}

// OnScraped registers a function that will be executed as the final part of
// the scraping, after OnHTML and OnXML have finished.
func (c *Collector) OnScraped(f ScrapedCallback) {
	c.lock.Lock()
	if c.scrapedCallbacks == nil {
		c.scrapedCallbacks = make([]ScrapedCallback, 0, 4)
	}
	c.scrapedCallbacks = append(c.scrapedCallbacks, f)
	c.lock.Unlock()
}

// SetClient will override the previously set http.Client
func (c *Collector) SetClient(client *http.Client) {
	c.backend.Client = client
}

// WithTransport allows you to set a custom http.RoundTripper (transport)
func (c *Collector) WithTransport(transport http.RoundTripper) {
	c.backend.Client.Transport = transport
}

// DisableCookies turns off cookie handling
func (c *Collector) DisableCookies() {
	c.backend.Client.Jar = nil
}

// SetCookieJar overrides the previously set cookie jar
func (c *Collector) SetCookieJar(j http.CookieJar) {
	c.backend.Client.Jar = j
}

// SetRequestTimeout overrides the default timeout (10 seconds) for this collector
func (c *Collector) SetRequestTimeout(timeout time.Duration) {
	c.backend.Client.Timeout = timeout
}

// SetStorage overrides the default in-memory storage.
// Storage stores scraping related data like cookies and visited urls
func (c *Collector) SetStorage(s storage.Storage) error {
	if err := s.Init(); err != nil {
		return err
	}
	c.store = s
	c.backend.Client.Jar = createJar(s)
	return nil
}

// SetProxy sets a proxy for the collector. This method overrides the previously
// used http.Transport if the type of the transport is not http.RoundTripper.
// The proxy type is determined by the URL scheme. "http"
// and "socks5" are supported. If the scheme is empty,
// "http" is assumed.
func (c *Collector) SetProxy(proxyURL string) error {
	proxyParsed, err := url.Parse(proxyURL)
	if err != nil {
		return err
	}

	c.SetProxyFunc(http.ProxyURL(proxyParsed))

	return nil
}

// SetProxyFunc sets a custom proxy setter/switcher function.
// See built-in ProxyFuncs for more details.
// This method overrides the previously used http.Transport
// if the type of the transport is not *http.Transport.
// The proxy type is determined by the URL scheme. "http"
// and "socks5" are supported. If the scheme is empty,
// "http" is assumed.
func (c *Collector) SetProxyFunc(p ProxyFunc) {
	t, ok := c.backend.Client.Transport.(*http.Transport)
	if c.backend.Client.Transport != nil && ok {
		t.Proxy = p
		t.DisableKeepAlives = true
	} else {
		c.backend.Client.Transport = &http.Transport{
			Proxy:             p,
			DisableKeepAlives: true,
		}
	}
}

func createEvent(eventType string, requestID, collectorID uint32, kvargs map[string]string) *debug.Event {
	return &debug.Event{
		CollectorID: collectorID,
		RequestID:   requestID,
		Type:        eventType,
		Values:      kvargs,
	}
}

func (c *Collector) handleOnRequest(r *Request) {
	if c.debugger != nil {
		c.debugger.Event(createEvent("request", r.ID, c.ID, map[string]string{
			"url": r.URL.String(),
		}))
	}
	for _, f := range c.requestCallbacks {
		f(r)
	}
}

func (c *Collector) handleOnResponse(r *Response) {
	if c.debugger != nil {
		c.debugger.Event(createEvent("response", r.Request.ID, c.ID, map[string]string{
			"url":    r.Request.URL.String(),
			"status": http.StatusText(r.StatusCode),
		}))
	}
	for _, f := range c.responseCallbacks {
		f(r)
	}
}

func (c *Collector) handleOnResponseHeaders(r *Response) {
	if c.debugger != nil {
		c.debugger.Event(createEvent("responseHeaders", r.Request.ID, c.ID, map[string]string{
			"url":    r.Request.URL.String(),
			"status": http.StatusText(r.StatusCode),
		}))
	}
	for _, f := range c.responseHeadersCallbacks {
		f(r)
	}
}
func (c *Collector) handleOnRequestHeaders(r *Request) {
	if c.debugger != nil {
		c.debugger.Event(createEvent("requestHeaders", r.ID, c.ID, map[string]string{
			"url": r.URL.String(),
		}))
	}
	for _, f := range c.requestHeadersCallbacks {
		f(r)
	}
}

func (c *Collector) handleOnHTML(resp *Response) error {
	c.lock.RLock()
	htmlCallbacks := slices.Clone(c.htmlCallbacks)
	c.lock.RUnlock()

	if len(htmlCallbacks) == 0 {
		return nil
	}

	contentType := resp.Headers.Get("Content-Type")
	if contentType == "" {
		contentType = http.DetectContentType(resp.Body)
	}
	// implementation of mime.ParseMediaType without parsing the params
	// part
	mediatype, _, _ := strings.Cut(contentType, ";")
	mediatype = strings.TrimSpace(strings.ToLower(mediatype))

	// TODO we also want to parse application/xml as XHTML if it has
	// appropriate doctype
	switch mediatype {
	case "text/html", "application/xhtml+xml":
	default:
		return nil
	}

	doc, err := goquery.NewDocumentFromReader(bytes.NewBuffer(resp.Body))
	if err != nil {
		return err
	}
	if href, found := doc.Find("base[href]").Attr("href"); found {
		u, err := urlParser.ParseRef(resp.Request.URL.String(), href)
		if err == nil {
			baseURL, err := url.Parse(u.Href(false))
			if err == nil {
				resp.Request.baseURL = baseURL
			}
		}

	}
	for _, cc := range htmlCallbacks {
		if !cc.active.Load() {
			continue
		}
		i := 0
		doc.Find(cc.Selector).Each(func(_ int, s *goquery.Selection) {
			for _, n := range s.Nodes {
				e := NewHTMLElementFromSelectionNode(resp, s, n, i)
				i++
				if c.debugger != nil {
					c.debugger.Event(createEvent("html", resp.Request.ID, c.ID, map[string]string{
						"selector": cc.Selector,
						"url":      resp.Request.URL.String(),
					}))
				}
				cc.Function(e)
			}
		})
	}
	return nil
}

func (c *Collector) handleOnXML(resp *Response) error {
	c.lock.RLock()
	xmlCallbacks := slices.Clone(c.xmlCallbacks)
	c.lock.RUnlock()

	if len(xmlCallbacks) == 0 {
		return nil
	}
	contentType := strings.ToLower(resp.Headers.Get("Content-Type"))
	isXMLFile := strings.HasSuffix(strings.ToLower(resp.Request.URL.Path), ".xml") || strings.HasSuffix(strings.ToLower(resp.Request.URL.Path), ".xml.gz")
	if !strings.Contains(contentType, "html") && (!strings.Contains(contentType, "xml") && !isXMLFile) {
		return nil
	}

	if strings.Contains(contentType, "html") {
		doc, err := htmlquery.Parse(bytes.NewBuffer(resp.Body))
		if err != nil {
			return err
		}
		if e := htmlquery.FindOne(doc, "//base"); e != nil {
			for _, a := range e.Attr {
				if a.Key == "href" {
					baseURL, err := resp.Request.URL.Parse(a.Val)
					if err == nil {
						resp.Request.baseURL = baseURL
					}
					break
				}
			}
		}

		for _, cc := range xmlCallbacks {
			if !cc.active.Load() {
				continue
			}
			for i, n := range htmlquery.Find(doc, cc.Query) {
				e := NewXMLElementFromHTMLNode(resp, n)
				e.Index = i
				if c.debugger != nil {
					c.debugger.Event(createEvent("xml", resp.Request.ID, c.ID, map[string]string{
						"selector": cc.Query,
						"url":      resp.Request.URL.String(),
					}))
				}
				cc.Function(e)
			}
		}
	} else if strings.Contains(contentType, "xml") || isXMLFile {
		doc, err := xmlquery.Parse(bytes.NewBuffer(resp.Body))
		if err != nil {
			return err
		}

		for _, cc := range xmlCallbacks {
			if !cc.active.Load() {
				continue
			}
			xmlquery.FindEach(doc, cc.Query, func(i int, n *xmlquery.Node) {
				e := NewXMLElementFromXMLNode(resp, n)
				if c.debugger != nil {
					c.debugger.Event(createEvent("xml", resp.Request.ID, c.ID, map[string]string{
						"selector": cc.Query,
						"url":      resp.Request.URL.String(),
					}))
				}
				cc.Function(e)
			})
		}
	}
	return nil
}

func (c *Collector) handleOnError(response *Response, err error, request *Request, ctx *Context) error {
	if err == nil && (c.ParseHTTPErrorResponse || response.StatusCode < 203) {
		return nil
	}
	if err == nil && response.StatusCode >= 203 {
		err = errors.New(http.StatusText(response.StatusCode))
	}
	if response == nil {
		response = &Response{
			Request: request,
			Ctx:     ctx,
		}
	}
	if c.debugger != nil {
		c.debugger.Event(createEvent("error", request.ID, c.ID, map[string]string{
			"url":    request.URL.String(),
			"status": http.StatusText(response.StatusCode),
		}))
	}
	if response.Request == nil {
		response.Request = request
	}
	if response.Ctx == nil {
		response.Ctx = request.Ctx
	}
	for _, f := range c.errorCallbacks {
		f(response, err)
	}
	return err
}

func (c *Collector) cleanupCallbacks() {
	c.lock.Lock()
	defer c.lock.Unlock()

	// Clean HTML callbacks
	c.htmlCallbacks = slices.DeleteFunc(c.htmlCallbacks, func(cc *htmlCallbackContainer) bool {
		return !cc.active.Load()
	})

	// Clean XML callbacks
	c.xmlCallbacks = slices.DeleteFunc(c.xmlCallbacks, func(cc *xmlCallbackContainer) bool {
		return !cc.active.Load()
	})
}

func (c *Collector) handleOnScraped(r *Response) {
	if c.debugger != nil {
		c.debugger.Event(createEvent("scraped", r.Request.ID, c.ID, map[string]string{
			"url": r.Request.URL.String(),
		}))
	}
	for _, f := range c.scrapedCallbacks {
		f(r)
	}

	// Cleanup inactive callbacks after processing each response
	c.cleanupCallbacks()
}

// Limit adds a new LimitRule to the collector
func (c *Collector) Limit(rule *LimitRule) error {
	return c.backend.Limit(rule)
}

// Limits adds new LimitRules to the collector
func (c *Collector) Limits(rules []*LimitRule) error {
	return c.backend.Limits(rules)
}

// SetRedirectHandler instructs the Collector to allow multiple downloads of the same URL
func (c *Collector) SetRedirectHandler(f func(req *http.Request, via []*http.Request) error) {
	c.redirectHandler = f
	c.backend.Client.CheckRedirect = c.checkRedirectFunc()
}

// SetCookies handles the receipt of the cookies in a reply for the given URL
func (c *Collector) SetCookies(URL string, cookies []*http.Cookie) error {
	if c.backend.Client.Jar == nil {
		return ErrNoCookieJar
	}
	u, err := url.Parse(URL)
	if err != nil {
		return err
	}
	c.backend.Client.Jar.SetCookies(u, cookies)
	return nil
}

// Cookies returns the cookies to send in a request for the given URL.
func (c *Collector) Cookies(URL string) []*http.Cookie {
	if c.backend.Client.Jar == nil {
		return nil
	}
	u, err := url.Parse(URL)
	if err != nil {
		return nil
	}
	return c.backend.Client.Jar.Cookies(u)
}

// Clone creates an exact copy of a Collector without callbacks.
// HTTP backend, robots.txt cache and cookie jar are shared
// between collectors.
func (c *Collector) Clone() *Collector {
	return &Collector{
		AllowedDomains:         c.AllowedDomains,
		AllowURLRevisit:        c.AllowURLRevisit,
		CacheDir:               c.CacheDir,
		CacheExpiration:        c.CacheExpiration,
		DetectCharset:          c.DetectCharset,
		DisallowedDomains:      c.DisallowedDomains,
		ID:                     atomic.AddUint32(&collectorCounter, 1),
		IgnoreRobotsTxt:        c.IgnoreRobotsTxt,
		MaxBodySize:            c.MaxBodySize,
		MaxDepth:               c.MaxDepth,
		MaxRequests:            c.MaxRequests,
		DisallowedURLFilters:   c.DisallowedURLFilters,
		URLFilters:             c.URLFilters,
		CheckHead:              c.CheckHead,
		ParseHTTPErrorResponse: c.ParseHTTPErrorResponse,
		UserAgent:              c.UserAgent,
		Headers:                c.Headers,
		TraceHTTP:              c.TraceHTTP,
		Context:                c.Context,
		store:                  c.store,
		backend:                c.backend,
		debugger:               c.debugger,
		Async:                  c.Async,
		redirectHandler:        c.redirectHandler,
		errorCallbacks:         make([]ErrorCallback, 0, 8),
		htmlCallbacks:          make([]*htmlCallbackContainer, 0, 8),
		xmlCallbacks:           make([]*xmlCallbackContainer, 0, 8),
		scrapedCallbacks:       make([]ScrapedCallback, 0, 8),
		lock:                   c.lock,
		requestCallbacks:       make([]RequestCallback, 0, 8),
		responseCallbacks:      make([]ResponseCallback, 0, 8),
		robotsMap:              c.robotsMap,
		wg:                     &sync.WaitGroup{},
	}
}

func (c *Collector) checkRedirectFunc() func(req *http.Request, via []*http.Request) error {
	return func(req *http.Request, via []*http.Request) error {
		if err := c.checkFilters(req.URL.String(), req.URL.Hostname()); err != nil {
			return fmt.Errorf("Not following redirect to %q: %w", req.URL, err)
		}

		// allow redirects to the original destination
		// to support websites redirecting to the same page while setting
		// session cookies
		samePageRedirect := normalizeURL(req.URL.String()) == normalizeURL(via[0].URL.String())

		if !c.AllowURLRevisit && !samePageRedirect {
			var body io.ReadCloser
			if req.GetBody != nil {
				var err error
				body, err = req.GetBody()
				if err != nil {
					return err
				}
				defer body.Close()
			}
			uHash := requestHash(req.URL.String(), body)
			visited, err := c.store.IsVisited(uHash)
			if err != nil {
				return err
			}
			if visited {
				if checkRevisit, ok := req.Context().Value(CheckRevisitKey).(bool); !ok || checkRevisit {
					return &AlreadyVisitedError{req.URL}
				}
			}
			err = c.store.Visited(uHash)
			if err != nil {
				return err
			}
		}

		if c.redirectHandler != nil {
			return c.redirectHandler(req, via)
		}

		// Honor golangs default of maximum of 10 redirects
		if len(via) >= 10 {
			return http.ErrUseLastResponse
		}

		lastRequest := via[len(via)-1]

		// If domain has changed, remove the Authorization-header if it exists
		if req.URL.Host != lastRequest.URL.Host {
			req.Header.Del("Authorization")
		}

		return nil
	}
}

func (c *Collector) parseSettingsFromEnv() {
	for _, e := range os.Environ() {
		if !strings.HasPrefix(e, envVariablePrefix) {
			continue
		}
		pair := strings.SplitN(e[len(envVariablePrefix):], "=", 2)
		if f, ok := envMap[pair[0]]; ok {
			f(c, pair[1])
		} else {
			log.Println("Unknown environment variable:", pair[0])
		}
	}
}

func (c *Collector) checkHasVisited(URL string, requestData map[string]string) (bool, error) {
	hash := requestHash(URL, createFormReader(requestData))
	return c.store.IsVisited(hash)
}

// SanitizeFileName replaces dangerous characters in a string
// so the return value can be used as a safe file name.
func SanitizeFileName(fileName string) string {
	ext := filepath.Ext(fileName)
	cleanExt := sanitize.BaseName(ext)
	if cleanExt == "" {
		cleanExt = ".unknown"
	}
	return strings.Replace(fmt.Sprintf(
		"%s.%s",
		sanitize.BaseName(fileName[:len(fileName)-len(ext)]),
		cleanExt[1:],
	), "-", "_", -1)
}

func createFormReader(data map[string]string) io.Reader {
	form := url.Values{}
	for k, v := range data {
		form.Add(k, v)
	}
	return strings.NewReader(form.Encode())
}

func createMultipartReader(boundary string, data map[string][]byte) io.Reader {
	dashBoundary := "--" + boundary

	body := []byte{}
	buffer := bytes.NewBuffer(body)

	buffer.WriteString("Content-type: multipart/form-data; boundary=" + boundary + "\n\n")
	for contentType, content := range data {
		buffer.WriteString(dashBoundary + "\n")
		buffer.WriteString("Content-Disposition: form-data; name=" + contentType + "\n")
		buffer.WriteString(fmt.Sprintf("Content-Length: %d \n\n", len(content)))
		buffer.Write(content)
		buffer.WriteString("\n")
	}
	buffer.WriteString(dashBoundary + "--\n\n")
	return bytes.NewReader(buffer.Bytes())

}

// randomBoundary was borrowed from
// github.com/golang/go/mime/multipart/writer.go#randomBoundary
func randomBoundary() string {
	var buf [30]byte
	_, err := io.ReadFull(rand.Reader, buf[:])
	if err != nil {
		panic(err)
	}
	return fmt.Sprintf("%x", buf[:])
}

func isYesString(s string) bool {
	switch strings.ToLower(s) {
	case "1", "yes", "true", "y":
		return true
	}
	return false
}

func createJar(s storage.Storage) http.CookieJar {
	return &cookieJarSerializer{store: s, lock: &sync.RWMutex{}}
}

func (j *cookieJarSerializer) SetCookies(u *url.URL, cookies []*http.Cookie) {
	j.lock.Lock()
	defer j.lock.Unlock()
	cookieStr := j.store.Cookies(u)

	// Merge existing cookies, new cookies have precedence.
	cnew := make([]*http.Cookie, len(cookies))
	copy(cnew, cookies)
	existing := storage.UnstringifyCookies(cookieStr)
	for _, c := range existing {
		if !storage.ContainsCookie(cnew, c.Name) {
			cnew = append(cnew, c)
		}
	}
	j.store.SetCookies(u, storage.StringifyCookies(cnew))
}

func (j *cookieJarSerializer) Cookies(u *url.URL) []*http.Cookie {
	cookies := storage.UnstringifyCookies(j.store.Cookies(u))
	// Filter.
	now := time.Now()
	cnew := make([]*http.Cookie, 0, len(cookies))
	for _, c := range cookies {
		// Drop expired cookies.
		if c.RawExpires != "" && c.Expires.Before(now) {
			continue
		}
		// Drop secure cookies if not over https.
		if c.Secure && u.Scheme != "https" {
			continue
		}
		cnew = append(cnew, c)
	}
	return cnew
}

func isMatchingFilter(fs []*regexp.Regexp, d []byte) bool {
	for _, r := range fs {
		if r.Match(d) {
			return true
		}
	}
	return false
}

func normalizeURL(u string) string {
	parsed, err := urlParser.Parse(u)
	if err != nil {
		return u
	}
	return parsed.String()
}

func requestHash(url string, body io.Reader) uint64 {
	h := fnv.New64a()
	// reparse the url to fix ambiguities such as
	// "http://example.com" vs "http://example.com/"
	io.WriteString(h, normalizeURL(url))
	if body != nil {
		io.Copy(h, body)
	}
	return h.Sum64()
}
```

## File: `colly_test.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package colly

import (
	"bufio"
	"bytes"
	"context"
	"errors"
	"fmt"
	"net/http"
	"net/http/httptest"
	"net/url"
	"os"
	"reflect"
	"regexp"
	"strings"
	"testing"
	"time"

	"github.com/PuerkitoBio/goquery"

	"github.com/gocolly/colly/v2/debug"
)

var serverIndexResponse = []byte("hello world\n")
var callbackTestHTML = []byte(`
<!DOCTYPE html>
<html>
<head>
<title>Callback Test Page</title>
</head>
<body>
<div id="firstElem">First</div>
<div id="secondElem">Second</div>
<div id="thirdElem">Third</div>
</body>
</html>
`)
var robotsFile = `
User-agent: *
Allow: /allowed
Disallow: /disallowed
Disallow: /allowed*q=
`

func newUnstartedTestServer() *httptest.Server {
	mux := http.NewServeMux()

	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(200)
		w.Write(serverIndexResponse)
	})

	mux.HandleFunc("/callback_test", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "text/html")
		w.WriteHeader(200)
		w.Write(callbackTestHTML)
	})

	mux.HandleFunc("/html", func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Query().Get("no-content-type") != "" {
			w.Header()["Content-Type"] = nil
		} else {
			w.Header().Set("Content-Type", "text/html")
		}
		w.Write([]byte(`<!DOCTYPE html>
<html>
<head>
<title>Test Page</title>
</head>
<body>
<h1>Hello World</h1>
<p class="description">This is a test page</p>
<p class="description">This is a test paragraph</p>
</body>
</html>
		`))
	})

	mux.HandleFunc("/xml", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/xml")
		w.Write([]byte(`<?xml version="1.0" encoding="UTF-8"?>
<page>
	<title>Test Page</title>
	<paragraph type="description">This is a test page</paragraph>
	<paragraph type="description">This is a test paragraph</paragraph>
</page>
		`))
	})

	mux.HandleFunc("/login", func(w http.ResponseWriter, r *http.Request) {
		if r.Method == "POST" {
			w.Header().Set("Content-Type", "text/html")
			w.Write([]byte(r.FormValue("name")))
		}
	})

	mux.HandleFunc("/robots.txt", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(200)
		w.Write([]byte(robotsFile))
	})

	mux.HandleFunc("/allowed", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(200)
		w.Write([]byte("allowed"))
	})

	mux.HandleFunc("/disallowed", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(200)
		w.Write([]byte("disallowed"))
	})

	mux.Handle("/redirect", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		destination := "/redirected/"
		if d := r.URL.Query().Get("d"); d != "" {
			destination = d
		}
		http.Redirect(w, r, destination, http.StatusSeeOther)

	}))

	mux.Handle("/redirected/", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, `<a href="test">test</a>`)
	}))

	mux.HandleFunc("/set_cookie", func(w http.ResponseWriter, r *http.Request) {
		c := &http.Cookie{Name: "test", Value: "testv", HttpOnly: false}
		http.SetCookie(w, c)
		w.WriteHeader(200)
		w.Write([]byte("ok"))
	})

	mux.HandleFunc("/check_cookie", func(w http.ResponseWriter, r *http.Request) {
		cs := r.Cookies()
		if len(cs) != 1 || r.Cookies()[0].Value != "testv" {
			w.WriteHeader(500)
			w.Write([]byte("nok"))
			return
		}
		w.WriteHeader(200)
		w.Write([]byte("ok"))
	})

	mux.HandleFunc("/500", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "text/html")
		w.WriteHeader(500)
		w.Write([]byte("<p>error</p>"))
	})

	mux.HandleFunc("/user_agent", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(200)
		w.Write([]byte(r.Header.Get("User-Agent")))
	})

	mux.HandleFunc("/host_header", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(200)
		w.Write([]byte(r.Host))
	})

	mux.HandleFunc("/accept_header", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(200)
		w.Write([]byte(r.Header.Get("Accept")))
	})

	mux.HandleFunc("/custom_header", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(200)
		w.Write([]byte(r.Header.Get("Test")))
	})

	mux.HandleFunc("/base", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "text/html")
		w.Write([]byte(`<!DOCTYPE html>
<html>
<head>
<title>Test Page</title>
<base href="http://xy.com/" />
</head>
<body>
<a href="z">link</a>
</body>
</html>
		`))
	})

	mux.HandleFunc("/base_relative", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "text/html")
		w.Write([]byte(`<!DOCTYPE html>
<html>
<head>
<title>Test Page</title>
<base href="/foobar/" />
</head>
<body>
<a href="z">link</a>
</body>
</html>
		`))
	})

	mux.HandleFunc("/tabs_and_newlines", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "text/html")
		w.Write([]byte(`<!DOCTYPE html>
<html>
<head>
<title>Test Page</title>
<base href="/foo	bar/" />
</head>
<body>
<a href="x
y">link</a>
</body>
</html>
		`))
	})

	mux.HandleFunc("/foobar/xy", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "text/html")
		w.Write([]byte(`<!DOCTYPE html>
<html>
<head>
<title>Test Page</title>
</head>
<body>
<p>hello</p>
</body>
</html>
		`))
	})

	mux.HandleFunc("/100%25", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("100 percent"))
	})

	mux.HandleFunc("/large_binary", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/octet-stream")
		ww := bufio.NewWriter(w)
		defer ww.Flush()
		for {
			// have to check error to detect client aborting download
			if _, err := ww.Write([]byte{0x41}); err != nil {
				return
			}
		}
	})

	mux.HandleFunc("/slow", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(200)

		ticker := time.NewTicker(100 * time.Millisecond)
		defer ticker.Stop()

		i := 0

		for {
			select {
			case <-r.Context().Done():
				return
			case t := <-ticker.C:
				fmt.Fprintf(w, "%s\n", t)
				if flusher, ok := w.(http.Flusher); ok {
					flusher.Flush()
				}
				i++
				if i == 10 {
					return
				}
			}
		}
	})

	mux.HandleFunc("/sitemap.xml.gz", func(w http.ResponseWriter, r *http.Request) {
		// Return a 404 HTML page for a non-existent .xml.gz URL.
		// This simulates the scenario in issue #745 where a server
		// returns an HTML error page for a missing gzipped sitemap.
		w.Header().Set("Content-Type", "text/html")
		w.WriteHeader(404)
		w.Write([]byte(`<!DOCTYPE html><html><body><h1>404 Not Found</h1></body></html>`))
	})

	return httptest.NewUnstartedServer(mux)
}

func newTestServer() *httptest.Server {
	srv := newUnstartedTestServer()
	srv.Start()
	return srv
}

var newCollectorTests = map[string]func(*testing.T){
	"UserAgent": func(t *testing.T) {
		for _, ua := range []string{
			"foo",
			"bar",
		} {
			c := NewCollector(UserAgent(ua))

			if got, want := c.UserAgent, ua; got != want {
				t.Fatalf("c.UserAgent = %q, want %q", got, want)
			}
		}
	},
	"MaxDepth": func(t *testing.T) {
		for _, depth := range []int{
			12,
			34,
			0,
		} {
			c := NewCollector(MaxDepth(depth))

			if got, want := c.MaxDepth, depth; got != want {
				t.Fatalf("c.MaxDepth = %d, want %d", got, want)
			}
		}
	},
	"AllowedDomains": func(t *testing.T) {
		for _, domains := range [][]string{
			{"example.com", "example.net"},
			{"example.net"},
			{},
			nil,
		} {
			c := NewCollector(AllowedDomains(domains...))

			if got, want := c.AllowedDomains, domains; !reflect.DeepEqual(got, want) {
				t.Fatalf("c.AllowedDomains = %q, want %q", got, want)
			}
		}
	},
	"DisallowedDomains": func(t *testing.T) {
		for _, domains := range [][]string{
			{"example.com", "example.net"},
			{"example.net"},
			{},
			nil,
		} {
			c := NewCollector(DisallowedDomains(domains...))

			if got, want := c.DisallowedDomains, domains; !reflect.DeepEqual(got, want) {
				t.Fatalf("c.DisallowedDomains = %q, want %q", got, want)
			}
		}
	},
	"DisallowedURLFilters": func(t *testing.T) {
		for _, filters := range [][]*regexp.Regexp{
			{regexp.MustCompile(`.*not_allowed.*`)},
		} {
			c := NewCollector(DisallowedURLFilters(filters...))

			if got, want := c.DisallowedURLFilters, filters; !reflect.DeepEqual(got, want) {
				t.Fatalf("c.DisallowedURLFilters = %v, want %v", got, want)
			}
		}
	},
	"URLFilters": func(t *testing.T) {
		for _, filters := range [][]*regexp.Regexp{
			{regexp.MustCompile(`\w+`)},
			{regexp.MustCompile(`\d+`)},
			{},
			nil,
		} {
			c := NewCollector(URLFilters(filters...))

			if got, want := c.URLFilters, filters; !reflect.DeepEqual(got, want) {
				t.Fatalf("c.URLFilters = %v, want %v", got, want)
			}
		}
	},
	"AllowURLRevisit": func(t *testing.T) {
		c := NewCollector(AllowURLRevisit())

		if !c.AllowURLRevisit {
			t.Fatal("c.AllowURLRevisit = false, want true")
		}
	},
	"MaxBodySize": func(t *testing.T) {
		for _, sizeInBytes := range []int{
			1024 * 1024,
			1024,
			0,
		} {
			c := NewCollector(MaxBodySize(sizeInBytes))

			if got, want := c.MaxBodySize, sizeInBytes; got != want {
				t.Fatalf("c.MaxBodySize = %d, want %d", got, want)
			}
		}
	},
	"CacheDir": func(t *testing.T) {
		for _, path := range []string{
			"/tmp/",
			"/var/cache/",
		} {
			c := NewCollector(CacheDir(path))

			if got, want := c.CacheDir, path; got != want {
				t.Fatalf("c.CacheDir = %q, want %q", got, want)
			}
		}
	},
	"CacheExpiration": func(t *testing.T) {
		for _, d := range []time.Duration{
			5 * time.Second,
			10 * time.Minute,
			0,
		} {
			c := NewCollector(CacheExpiration(d))

			if got, want := c.CacheExpiration, d; got != want {
				t.Fatalf("c.CacheExpiration = %v, want %v", got, want)
			}
		}
	},
	"IgnoreRobotsTxt": func(t *testing.T) {
		c := NewCollector(IgnoreRobotsTxt())

		if !c.IgnoreRobotsTxt {
			t.Fatal("c.IgnoreRobotsTxt = false, want true")
		}
	},
	"ID": func(t *testing.T) {
		for _, id := range []uint32{
			0,
			1,
			2,
		} {
			c := NewCollector(ID(id))

			if got, want := c.ID, id; got != want {
				t.Fatalf("c.ID = %d, want %d", got, want)
			}
		}
	},
	"DetectCharset": func(t *testing.T) {
		c := NewCollector(DetectCharset())

		if !c.DetectCharset {
			t.Fatal("c.DetectCharset = false, want true")
		}
	},
	"Debugger": func(t *testing.T) {
		d := &debug.LogDebugger{}
		c := NewCollector(Debugger(d))

		if got, want := c.debugger, d; got != want {
			t.Fatalf("c.debugger = %v, want %v", got, want)
		}
	},
	"CheckHead": func(t *testing.T) {
		c := NewCollector(CheckHead())

		if !c.CheckHead {
			t.Fatal("c.CheckHead = false, want true")
		}
	},
	"Async": func(t *testing.T) {
		c := NewCollector(Async())

		if !c.Async {
			t.Fatal("c.Async = false, want true")
		}
	},
}

func TestNoAcceptHeader(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	var receivedHeader string
	// checks if Accept is enabled by default
	func() {
		c := NewCollector()
		c.OnResponse(func(resp *Response) {
			receivedHeader = string(resp.Body)
		})
		c.Visit(ts.URL + "/accept_header")
		if receivedHeader != "*/*" {
			t.Errorf("default Accept header isn't */*. got: %v", receivedHeader)
		}
	}()

	// checks if Accept can be disabled
	func() {
		c := NewCollector()
		c.OnRequest(func(r *Request) {
			r.Headers.Del("Accept")
		})
		c.OnResponse(func(resp *Response) {
			receivedHeader = string(resp.Body)
		})
		c.Visit(ts.URL + "/accept_header")
		if receivedHeader != "" {
			t.Errorf("failed to pass request with no Accept header. got: %v", receivedHeader)
		}
	}()
}

func TestNewCollector(t *testing.T) {
	t.Run("Functional Options", func(t *testing.T) {
		for name, test := range newCollectorTests {
			t.Run(name, test)
		}
	})
}

func TestCollectorVisit(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()

	onRequestCalled := false
	onResponseCalled := false
	onScrapedCalled := false

	c.OnRequest(func(r *Request) {
		onRequestCalled = true
		r.Ctx.Put("x", "y")
	})

	c.OnResponse(func(r *Response) {
		onResponseCalled = true

		if r.Ctx.Get("x") != "y" {
			t.Error("Failed to retrieve context value for key 'x'")
		}

		if !bytes.Equal(r.Body, serverIndexResponse) {
			t.Error("Response body does not match with the original content")
		}
	})

	c.OnScraped(func(r *Response) {
		if !onResponseCalled {
			t.Error("OnScraped called before OnResponse")
		}

		if !onRequestCalled {
			t.Error("OnScraped called before OnRequest")
		}

		onScrapedCalled = true
	})

	c.Visit(ts.URL)

	if !onRequestCalled {
		t.Error("Failed to call OnRequest callback")
	}

	if !onResponseCalled {
		t.Error("Failed to call OnResponse callback")
	}

	if !onScrapedCalled {
		t.Error("Failed to call OnScraped callback")
	}
}

func TestCollectorVisitWithAllowedDomains(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector(AllowedDomains("localhost", "127.0.0.1", "::1"))
	err := c.Visit(ts.URL)
	if err != nil {
		t.Errorf("Failed to visit url %s", ts.URL)
	}

	err = c.Visit("http://example.com")
	if err != ErrForbiddenDomain {
		t.Errorf("c.Visit should return ErrForbiddenDomain, but got %v", err)
	}
}

func TestCollectorVisitWithDisallowedDomains(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector(DisallowedDomains("localhost", "127.0.0.1", "::1"))
	err := c.Visit(ts.URL)
	if err != ErrForbiddenDomain {
		t.Errorf("c.Visit should return ErrForbiddenDomain, but got %v", err)
	}

	c2 := NewCollector(DisallowedDomains("example.com"))
	err = c2.Visit("http://example.com:8080")
	if err != ErrForbiddenDomain {
		t.Errorf("c.Visit should return ErrForbiddenDomain, but got %v", err)
	}
	err = c2.Visit(ts.URL)
	if err != nil {
		t.Errorf("Failed to visit url %s", ts.URL)
	}
}

func TestCollectorVisitResponseHeaders(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	var onResponseHeadersCalled bool

	c := NewCollector()
	c.OnResponseHeaders(func(r *Response) {
		onResponseHeadersCalled = true
		if r.Headers.Get("Content-Type") == "application/octet-stream" {
			r.Request.Abort()
		}
	})
	c.OnResponse(func(r *Response) {
		t.Error("OnResponse was called")
	})
	c.Visit(ts.URL + "/large_binary")
	if !onResponseHeadersCalled {
		t.Error("OnResponseHeaders was not called")
	}
}

func TestCollectorOnHTML(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()

	titleCallbackCalled := false
	paragraphCallbackCount := 0

	c.OnHTML("title", func(e *HTMLElement) {
		titleCallbackCalled = true
		if e.Text != "Test Page" {
			t.Error("Title element text does not match, got", e.Text)
		}
	})

	c.OnHTML("p", func(e *HTMLElement) {
		paragraphCallbackCount++
		if e.Attr("class") != "description" {
			t.Error("Failed to get paragraph's class attribute")
		}
	})

	c.OnHTML("body", func(e *HTMLElement) {
		if e.ChildAttr("p", "class") != "description" {
			t.Error("Invalid class value")
		}
		classes := e.ChildAttrs("p", "class")
		if len(classes) != 2 {
			t.Error("Invalid class values")
		}
	})

	c.Visit(ts.URL + "/html")

	if !titleCallbackCalled {
		t.Error("Failed to call OnHTML callback for <title> tag")
	}

	if paragraphCallbackCount != 2 {
		t.Error("Failed to find all <p> tags")
	}
}

func TestCollectorContentSniffing(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()

	htmlCallbackCalled := false

	c.OnResponse(func(r *Response) {
		if (*r.Headers)["Content-Type"] != nil {
			t.Error("Content-Type unexpectedly not nil")
		}
	})

	c.OnHTML("html", func(e *HTMLElement) {
		htmlCallbackCalled = true
	})

	err := c.Visit(ts.URL + "/html?no-content-type=yes")
	if err != nil {
		t.Fatal(err)
	}

	if !htmlCallbackCalled {
		t.Error("OnHTML was not called")
	}
}

func TestCollectorURLRevisit(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()

	visitCount := 0

	c.OnRequest(func(r *Request) {
		visitCount++
	})

	c.Visit(ts.URL)
	c.Visit(ts.URL)

	if visitCount != 1 {
		t.Error("URL revisited")
	}

	c.AllowURLRevisit = true

	c.Visit(ts.URL)
	c.Visit(ts.URL)

	if visitCount != 3 {
		t.Error("URL not revisited")
	}
}

func TestCollectorPostRevisit(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	postValue := "hello"
	postData := map[string]string{
		"name": postValue,
	}
	visitCount := 0

	c := NewCollector()
	c.OnResponse(func(r *Response) {
		if postValue != string(r.Body) {
			t.Error("Failed to send data with POST")
		}
		visitCount++
	})

	c.Post(ts.URL+"/login", postData)
	c.Post(ts.URL+"/login", postData)
	c.Post(ts.URL+"/login", map[string]string{
		"name":     postValue,
		"lastname": "world",
	})

	if visitCount != 2 {
		t.Error("URL POST revisited")
	}

	c.AllowURLRevisit = true

	c.Post(ts.URL+"/login", postData)
	c.Post(ts.URL+"/login", postData)

	if visitCount != 4 {
		t.Error("URL POST not revisited")
	}
}

func TestCollectorURLRevisitCheck(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()

	visited, err := c.HasVisited(ts.URL)

	if err != nil {
		t.Error(err.Error())
	}

	if visited != false {
		t.Error("Expected URL to NOT have been visited")
	}

	c.Visit(ts.URL)

	visited, err = c.HasVisited(ts.URL)

	if err != nil {
		t.Error(err.Error())
	}

	if visited != true {
		t.Error("Expected URL to have been visited")
	}

	errorTestCases := []struct {
		Path             string
		DestinationError string
	}{
		{"/", "/"},
		{"/redirect?d=/", "/"},
		// now that /redirect?d=/ itself is recorded as visited,
		// it's now returned in error
		{"/redirect?d=/", "/redirect?d=/"},
		{"/redirect?d=/redirect%3Fd%3D/", "/redirect?d=/"},
		{"/redirect?d=/redirect%3Fd%3D/", "/redirect?d=/redirect%3Fd%3D/"},
		{"/redirect?d=/redirect%3Fd%3D/&foo=bar", "/redirect?d=/"},
	}

	for i, testCase := range errorTestCases {
		err := c.Visit(ts.URL + testCase.Path)
		if testCase.DestinationError == "" {
			if err != nil {
				t.Errorf("got unexpected error in test %d: %q", i, err)
			}
		} else {
			var ave *AlreadyVisitedError
			if !errors.As(err, &ave) {
				t.Errorf("err=%q returned when trying to revisit, expected AlreadyVisitedError", err)
			} else {
				if got, want := ave.Destination.String(), ts.URL+testCase.DestinationError; got != want {
					t.Errorf("wrong destination in AlreadyVisitedError in test %d, got=%q want=%q", i, got, want)
				}
			}
		}
	}
}

func TestSetCookieRedirect(t *testing.T) {
	type middleware = func(http.Handler) http.Handler
	for _, m := range []middleware{
		requireSessionCookieSimple,
		requireSessionCookieAuthPage,
	} {
		t.Run("", func(t *testing.T) {
			ts := newUnstartedTestServer()
			ts.Config.Handler = m(ts.Config.Handler)
			ts.Start()
			defer ts.Close()
			c := NewCollector()
			c.OnResponse(func(r *Response) {
				if got, want := r.Body, serverIndexResponse; !bytes.Equal(got, want) {
					t.Errorf("bad response body got=%q want=%q", got, want)
				}
				if got, want := r.StatusCode, http.StatusOK; got != want {
					t.Errorf("bad response code got=%d want=%d", got, want)
				}
			})
			if err := c.Visit(ts.URL); err != nil {
				t.Fatal(err)
			}
		})
	}
}

func TestCollectorPostURLRevisitCheck(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()

	postValue := "hello"
	postData := map[string]string{
		"name": postValue,
	}

	posted, err := c.HasPosted(ts.URL+"/login", postData)

	if err != nil {
		t.Error(err.Error())
	}

	if posted != false {
		t.Error("Expected URL to NOT have been visited")
	}

	c.Post(ts.URL+"/login", postData)

	posted, err = c.HasPosted(ts.URL+"/login", postData)

	if err != nil {
		t.Error(err.Error())
	}

	if posted != true {
		t.Error("Expected URL to have been visited")
	}

	postData["lastname"] = "world"
	posted, err = c.HasPosted(ts.URL+"/login", postData)

	if err != nil {
		t.Error(err.Error())
	}

	if posted != false {
		t.Error("Expected URL to NOT have been visited")
	}

	c.Post(ts.URL+"/login", postData)

	posted, err = c.HasPosted(ts.URL+"/login", postData)

	if err != nil {
		t.Error(err.Error())
	}

	if posted != true {
		t.Error("Expected URL to have been visited")
	}
}

// TestCollectorURLRevisitDomainDisallowed ensures that disallowed URL is not considered visited.
func TestCollectorURLRevisitDomainDisallowed(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	parsedURL, err := url.Parse(ts.URL)
	if err != nil {
		t.Fatal(err)
	}

	c := NewCollector(DisallowedDomains(parsedURL.Hostname()))
	err = c.Visit(ts.URL)
	if got, want := err, ErrForbiddenDomain; got != want {
		t.Fatalf("wrong error on first visit: got=%v want=%v", got, want)
	}
	err = c.Visit(ts.URL)
	if got, want := err, ErrForbiddenDomain; got != want {
		t.Fatalf("wrong error on second visit: got=%v want=%v", got, want)
	}

}

func TestCollectorPost(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	postValue := "hello"
	c := NewCollector()

	c.OnResponse(func(r *Response) {
		if postValue != string(r.Body) {
			t.Error("Failed to send data with POST")
		}
	})

	c.Post(ts.URL+"/login", map[string]string{
		"name": postValue,
	})
}

func TestCollectorPostRaw(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	postValue := "hello"
	c := NewCollector()

	c.OnResponse(func(r *Response) {
		if postValue != string(r.Body) {
			t.Error("Failed to send data with POST")
		}
	})

	c.PostRaw(ts.URL+"/login", []byte("name="+postValue))
}

func TestCollectorPostRawRevisit(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	postValue := "hello"
	postData := "name=" + postValue
	visitCount := 0

	c := NewCollector()
	c.OnResponse(func(r *Response) {
		if postValue != string(r.Body) {
			t.Error("Failed to send data with POST RAW")
		}
		visitCount++
	})

	c.PostRaw(ts.URL+"/login", []byte(postData))
	c.PostRaw(ts.URL+"/login", []byte(postData))
	c.PostRaw(ts.URL+"/login", []byte(postData+"&lastname=world"))

	if visitCount != 2 {
		t.Error("URL POST RAW revisited")
	}

	c.AllowURLRevisit = true

	c.PostRaw(ts.URL+"/login", []byte(postData))
	c.PostRaw(ts.URL+"/login", []byte(postData))

	if visitCount != 4 {
		t.Error("URL POST RAW not revisited")
	}
}

func TestRedirect(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()
	c.OnHTML("a[href]", func(e *HTMLElement) {
		u := e.Request.AbsoluteURL(e.Attr("href"))
		if !strings.HasSuffix(u, "/redirected/test") {
			t.Error("Invalid URL after redirect: " + u)
		}
	})

	c.OnResponseHeaders(func(r *Response) {
		if !strings.HasSuffix(r.Request.URL.String(), "/redirected/") {
			t.Error("Invalid URL in Request after redirect (OnResponseHeaders): " + r.Request.URL.String())
		}
	})

	c.OnResponse(func(r *Response) {
		if !strings.HasSuffix(r.Request.URL.String(), "/redirected/") {
			t.Error("Invalid URL in Request after redirect (OnResponse): " + r.Request.URL.String())
		}
	})
	c.Visit(ts.URL + "/redirect")
}

func TestIssue594(t *testing.T) {
	// This is a regression test for a data race bug. There's no
	// assertions because it's meant to be used with race detector
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()
	// if timeout is set, this bug is not triggered
	c.SetClient(&http.Client{Timeout: 0 * time.Second})

	c.Visit(ts.URL)
}

func TestRedirectWithDisallowedURLs(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()
	c.DisallowedURLFilters = []*regexp.Regexp{regexp.MustCompile(ts.URL + "/redirected/test")}
	c.OnHTML("a[href]", func(e *HTMLElement) {
		u := e.Request.AbsoluteURL(e.Attr("href"))
		err := c.Visit(u)
		if !errors.Is(err, ErrForbiddenURL) {
			t.Error("URL should have been forbidden: " + u)
		}
	})

	c.Visit(ts.URL + "/redirect")
}

func TestBaseTag(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()
	c.OnHTML("a[href]", func(e *HTMLElement) {
		u := e.Request.AbsoluteURL(e.Attr("href"))
		if u != "http://xy.com/z" {
			t.Error("Invalid <base /> tag handling in OnHTML: expected https://xy.com/z, got " + u)
		}
	})
	c.Visit(ts.URL + "/base")

	c2 := NewCollector()
	c2.OnXML("//a", func(e *XMLElement) {
		u := e.Request.AbsoluteURL(e.Attr("href"))
		if u != "http://xy.com/z" {
			t.Error("Invalid <base /> tag handling in OnXML: expected https://xy.com/z, got " + u)
		}
	})
	c2.Visit(ts.URL + "/base")
}

func TestBaseTagRelative(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()
	c.OnHTML("a[href]", func(e *HTMLElement) {
		u := e.Request.AbsoluteURL(e.Attr("href"))
		expected := ts.URL + "/foobar/z"
		if u != expected {
			t.Errorf("Invalid <base /> tag handling in OnHTML: expected %q, got %q", expected, u)
		}
	})
	c.Visit(ts.URL + "/base_relative")

	c2 := NewCollector()
	c2.OnXML("//a", func(e *XMLElement) {
		u := e.Request.AbsoluteURL(e.Attr("href"))
		expected := ts.URL + "/foobar/z"
		if u != expected {
			t.Errorf("Invalid <base /> tag handling in OnXML: expected %q, got %q", expected, u)
		}
	})
	c2.Visit(ts.URL + "/base_relative")
}

func TestTabsAndNewlines(t *testing.T) {
	// this test might look odd, but see step 3 of
	// https://url.spec.whatwg.org/#concept-basic-url-parser

	ts := newTestServer()
	defer ts.Close()

	visited := map[string]struct{}{}
	expected := map[string]struct{}{
		"/tabs_and_newlines": {},
		"/foobar/xy":         {},
	}

	c := NewCollector()
	c.OnResponse(func(res *Response) {
		visited[res.Request.URL.EscapedPath()] = struct{}{}
	})
	c.OnHTML("a[href]", func(e *HTMLElement) {
		if err := e.Request.Visit(e.Attr("href")); err != nil {
			t.Errorf("visit failed: %v", err)
		}
	})

	if err := c.Visit(ts.URL + "/tabs_and_newlines"); err != nil {
		t.Errorf("visit failed: %v", err)
	}

	if !reflect.DeepEqual(visited, expected) {
		t.Errorf("visited=%v expected=%v", visited, expected)
	}
}

func TestLonePercent(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	var visitedPath string

	c := NewCollector()
	c.OnResponse(func(res *Response) {
		visitedPath = res.Request.URL.RequestURI()
	})
	if err := c.Visit(ts.URL + "/100%"); err != nil {
		t.Errorf("visit failed: %v", err)
	}
	// Automatic encoding is not really correct: browsers
	// would send bare percent here. However, Go net/http
	// cannot send such requests due to
	// https://github.com/golang/go/issues/29808. So we have two
	// alternatives really: return an error when attempting
	// to fetch such URLs, or at least try the encoded variant.
	// This test checks that the latter is attempted.
	if got, want := visitedPath, "/100%25"; got != want {
		t.Errorf("got=%q want=%q", got, want)
	}
	// invalid URL escape in query component is not a problem,
	// but check it anyway
	if err := c.Visit(ts.URL + "/?a=100%zz"); err != nil {
		t.Errorf("visit failed: %v", err)
	}
	if got, want := visitedPath, "/?a=100%zz"; got != want {
		t.Errorf("got=%q want=%q", got, want)
	}
}

func TestCollectorCookies(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()

	if err := c.Visit(ts.URL + "/set_cookie"); err != nil {
		t.Fatal(err)
	}

	if err := c.Visit(ts.URL + "/check_cookie"); err != nil {
		t.Fatalf("Failed to use previously set cookies: %s", err)
	}
}

func TestRobotsWhenAllowed(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()
	c.IgnoreRobotsTxt = false

	c.OnResponse(func(resp *Response) {
		if resp.StatusCode != 200 {
			t.Fatalf("Wrong response code: %d", resp.StatusCode)
		}
	})

	err := c.Visit(ts.URL + "/allowed")

	if err != nil {
		t.Fatal(err)
	}
}

func TestRobotsWhenDisallowed(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()
	c.IgnoreRobotsTxt = false

	c.OnResponse(func(resp *Response) {
		t.Fatalf("Received response: %d", resp.StatusCode)
	})

	err := c.Visit(ts.URL + "/disallowed")
	if err.Error() != "URL blocked by robots.txt" {
		t.Fatalf("wrong error message: %v", err)
	}
}

func TestRobotsWhenDisallowedWithQueryParameter(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()
	c.IgnoreRobotsTxt = false

	c.OnResponse(func(resp *Response) {
		t.Fatalf("Received response: %d", resp.StatusCode)
	})

	err := c.Visit(ts.URL + "/allowed?q=1")
	if err.Error() != "URL blocked by robots.txt" {
		t.Fatalf("wrong error message: %v", err)
	}
}

func TestIgnoreRobotsWhenDisallowed(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()
	c.IgnoreRobotsTxt = true

	c.OnResponse(func(resp *Response) {
		if resp.StatusCode != 200 {
			t.Fatalf("Wrong response code: %d", resp.StatusCode)
		}
	})

	err := c.Visit(ts.URL + "/disallowed")

	if err != nil {
		t.Fatal(err)
	}

}

func TestConnectionErrorOnRobotsTxtResultsInError(t *testing.T) {
	ts := newTestServer()
	ts.Close() // immediately close the server to force a connection error

	c := NewCollector()
	c.IgnoreRobotsTxt = false
	err := c.Visit(ts.URL)

	if err == nil {
		t.Fatal("Error expected")
	}
}

func TestEnvSettings(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	os.Setenv("COLLY_USER_AGENT", "test")
	defer os.Unsetenv("COLLY_USER_AGENT")

	c := NewCollector()

	valid := false

	c.OnResponse(func(resp *Response) {
		if string(resp.Body) == "test" {
			valid = true
		}
	})

	c.Visit(ts.URL + "/user_agent")

	if !valid {
		t.Fatalf("Wrong user-agent from environment")
	}
}

func TestUserAgent(t *testing.T) {
	const exampleUserAgent1 = "Example/1.0"
	const exampleUserAgent2 = "Example/2.0"
	const defaultUserAgent = "colly - https://github.com/gocolly/colly"

	ts := newTestServer()
	defer ts.Close()

	var receivedUserAgent string

	func() {
		c := NewCollector()
		c.OnResponse(func(resp *Response) {
			receivedUserAgent = string(resp.Body)
		})
		c.Visit(ts.URL + "/user_agent")
		if got, want := receivedUserAgent, defaultUserAgent; got != want {
			t.Errorf("mismatched User-Agent: got=%q want=%q", got, want)
		}
	}()
	func() {
		c := NewCollector(UserAgent(exampleUserAgent1))
		c.OnResponse(func(resp *Response) {
			receivedUserAgent = string(resp.Body)
		})
		c.Visit(ts.URL + "/user_agent")
		if got, want := receivedUserAgent, exampleUserAgent1; got != want {
			t.Errorf("mismatched User-Agent: got=%q want=%q", got, want)
		}
	}()
	func() {
		c := NewCollector(UserAgent(exampleUserAgent1))
		c.OnResponse(func(resp *Response) {
			receivedUserAgent = string(resp.Body)
		})

		c.Request("GET", ts.URL+"/user_agent", nil, nil, nil)
		if got, want := receivedUserAgent, exampleUserAgent1; got != want {
			t.Errorf("mismatched User-Agent (nil hdr): got=%q want=%q", got, want)
		}
	}()
	func() {
		c := NewCollector(UserAgent(exampleUserAgent1))
		c.OnResponse(func(resp *Response) {
			receivedUserAgent = string(resp.Body)
		})

		c.Request("GET", ts.URL+"/user_agent", nil, nil, http.Header{})
		if got, want := receivedUserAgent, exampleUserAgent1; got != want {
			t.Errorf("mismatched User-Agent (non-nil hdr): got=%q want=%q", got, want)
		}
	}()
	func() {
		c := NewCollector(UserAgent(exampleUserAgent1))
		c.OnResponse(func(resp *Response) {
			receivedUserAgent = string(resp.Body)
		})
		hdr := http.Header{}
		hdr.Set("User-Agent", "")

		c.Request("GET", ts.URL+"/user_agent", nil, nil, hdr)
		if got, want := receivedUserAgent, ""; got != want {
			t.Errorf("mismatched User-Agent (hdr with empty UA): got=%q want=%q", got, want)
		}
	}()
	func() {
		c := NewCollector(UserAgent(exampleUserAgent1))
		c.OnResponse(func(resp *Response) {
			receivedUserAgent = string(resp.Body)
		})
		hdr := http.Header{}
		hdr.Set("User-Agent", exampleUserAgent2)

		c.Request("GET", ts.URL+"/user_agent", nil, nil, hdr)
		if got, want := receivedUserAgent, exampleUserAgent2; got != want {
			t.Errorf("mismatched User-Agent (hdr with UA): got=%q want=%q", got, want)
		}
	}()
}

func TestHeaders(t *testing.T) {
	const exampleHostHeader = "example.com"
	const exampleTestHeader = "Testing"

	ts := newTestServer()
	defer ts.Close()

	var receivedHeader string

	func() {
		c := NewCollector(
			Headers(map[string]string{"Host": exampleHostHeader}),
		)
		c.OnResponse(func(resp *Response) {
			receivedHeader = string(resp.Body)
		})
		c.Visit(ts.URL + "/host_header")
		if got, want := receivedHeader, exampleHostHeader; got != want {
			t.Errorf("mismatched Host header: got=%q want=%q", got, want)
		}
	}()
	func() {
		c := NewCollector(
			Headers(map[string]string{"Test": exampleTestHeader}),
		)
		c.OnResponse(func(resp *Response) {
			receivedHeader = string(resp.Body)
		})
		c.Visit(ts.URL + "/custom_header")
		if got, want := receivedHeader, exampleTestHeader; got != want {
			t.Errorf("mismatched custom header: got=%q want=%q", got, want)
		}
	}()
}

func TestParseHTTPErrorResponse(t *testing.T) {
	contentCount := 0
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector(
		AllowURLRevisit(),
	)

	c.OnHTML("p", func(e *HTMLElement) {
		if e.Text == "error" {
			contentCount++
		}
	})

	c.Visit(ts.URL + "/500")

	if contentCount != 0 {
		t.Fatal("Content is parsed without ParseHTTPErrorResponse enabled")
	}

	c.ParseHTTPErrorResponse = true

	c.Visit(ts.URL + "/500")

	if contentCount != 1 {
		t.Fatal("Content isn't parsed with ParseHTTPErrorResponse enabled")
	}

}

func TestHTMLElement(t *testing.T) {
	ctx := &Context{}
	resp := &Response{
		Request: &Request{
			Ctx: ctx,
		},
		Ctx: ctx,
	}

	in := `<a href="http://go-colly.org">Colly</a>`
	sel := "a[href]"
	doc, err := goquery.NewDocumentFromReader(bytes.NewBuffer([]byte(in)))
	if err != nil {
		t.Fatal(err)
	}
	elements := []*HTMLElement{}
	i := 0
	doc.Find(sel).Each(func(_ int, s *goquery.Selection) {
		for _, n := range s.Nodes {
			elements = append(elements, NewHTMLElementFromSelectionNode(resp, s, n, i))
			i++
		}
	})
	elementsLen := len(elements)
	if elementsLen != 1 {
		t.Errorf("element length mismatch. got %d, expected %d.\n", elementsLen, 1)
	}
	v := elements[0]
	if v.Name != "a" {
		t.Errorf("element tag mismatch. got %s, expected %s.\n", v.Name, "a")
	}
	if v.Text != "Colly" {
		t.Errorf("element content mismatch. got %s, expected %s.\n", v.Text, "Colly")
	}
	if v.Attr("href") != "http://go-colly.org" {
		t.Errorf("element href mismatch. got %s, expected %s.\n", v.Attr("href"), "http://go-colly.org")
	}
}

func TestCollectorOnXMLWithHtml(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()

	titleCallbackCalled := false
	paragraphCallbackCount := 0

	c.OnXML("/html/head/title", func(e *XMLElement) {
		titleCallbackCalled = true
		if e.Text != "Test Page" {
			t.Error("Title element text does not match, got", e.Text)
		}
	})

	c.OnXML("/html/body/p", func(e *XMLElement) {
		paragraphCallbackCount++
		if e.Attr("class") != "description" {
			t.Error("Failed to get paragraph's class attribute")
		}
	})

	c.OnXML("/html/body", func(e *XMLElement) {
		if e.ChildAttr("p", "class") != "description" {
			t.Error("Invalid class value")
		}
		classes := e.ChildAttrs("p", "class")
		if len(classes) != 2 {
			t.Error("Invalid class values")
		}
	})

	c.Visit(ts.URL + "/html")

	if !titleCallbackCalled {
		t.Error("Failed to call OnXML callback for <title> tag")
	}

	if paragraphCallbackCount != 2 {
		t.Error("Failed to find all <p> tags")
	}
}

func TestCollectorOnXMLWithXML(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()

	titleCallbackCalled := false
	paragraphCallbackCount := 0

	c.OnXML("//page/title", func(e *XMLElement) {
		titleCallbackCalled = true
		if e.Text != "Test Page" {
			t.Error("Title element text does not match, got", e.Text)
		}
	})

	c.OnXML("//page/paragraph", func(e *XMLElement) {
		paragraphCallbackCount++
		if e.Attr("type") != "description" {
			t.Error("Failed to get paragraph's type attribute")
		}
	})

	c.OnXML("/page", func(e *XMLElement) {
		if e.ChildAttr("paragraph", "type") != "description" {
			t.Error("Invalid type value")
		}
		classes := e.ChildAttrs("paragraph", "type")
		if len(classes) != 2 {
			t.Error("Invalid type values")
		}
	})

	c.Visit(ts.URL + "/xml")

	if !titleCallbackCalled {
		t.Error("Failed to call OnXML callback for <title> tag")
	}

	if paragraphCallbackCount != 2 {
		t.Error("Failed to find all <paragraph> tags")
	}
}

func TestCollectorVisitWithTrace(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector(AllowedDomains("localhost", "127.0.0.1", "::1"), TraceHTTP())
	c.OnResponse(func(resp *Response) {
		if resp.Trace == nil {
			t.Error("Failed to initialize trace")
		}
	})

	err := c.Visit(ts.URL)
	if err != nil {
		t.Errorf("Failed to visit url %s", ts.URL)
	}
}

func TestCollectorVisitWithCheckHead(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector(CheckHead())
	var requestMethodChain []string
	c.OnResponse(func(resp *Response) {
		requestMethodChain = append(requestMethodChain, resp.Request.Method)
	})

	err := c.Visit(ts.URL)
	if err != nil {
		t.Errorf("Failed to visit url %s", ts.URL)
	}
	if requestMethodChain[0] != "HEAD" && requestMethodChain[1] != "GET" {
		t.Errorf("Failed to perform a HEAD request before GET")
	}
}

func TestCollectorDepth(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()
	maxDepth := 2
	c1 := NewCollector(
		MaxDepth(maxDepth),
		AllowURLRevisit(),
	)
	requestCount := 0
	c1.OnResponse(func(resp *Response) {
		requestCount++
		if requestCount >= 10 {
			return
		}
		c1.Visit(ts.URL)
	})
	c1.Visit(ts.URL)
	if requestCount < 10 {
		t.Errorf("Invalid number of requests: %d (expected 10) without using MaxDepth", requestCount)
	}

	c2 := c1.Clone()
	requestCount = 0
	c2.OnResponse(func(resp *Response) {
		requestCount++
		resp.Request.Visit(ts.URL)
	})
	c2.Visit(ts.URL)
	if requestCount != 2 {
		t.Errorf("Invalid number of requests: %d (expected 2) with using MaxDepth 2", requestCount)
	}

	c1.Visit(ts.URL)
	if requestCount < 10 {
		t.Errorf("Invalid number of requests: %d (expected 10) without using MaxDepth again", requestCount)
	}

	requestCount = 0
	c2.Visit(ts.URL)
	if requestCount != 2 {
		t.Errorf("Invalid number of requests: %d (expected 2) with using MaxDepth 2 again", requestCount)
	}
}

func TestCollectorRequests(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()
	maxRequests := uint32(5)
	c1 := NewCollector(
		MaxRequests(maxRequests),
		AllowURLRevisit(),
	)
	requestCount := 0
	c1.OnResponse(func(resp *Response) {
		requestCount++
		c1.Visit(ts.URL)
	})
	c1.Visit(ts.URL)
	if requestCount != 5 {
		t.Errorf("Invalid number of requests: %d (expected 5) with MaxRequests", requestCount)
	}
}

func TestCollectorContext(t *testing.T) {
	// "/slow" takes 1 second to return the response.
	// If context does abort the transfer after 0.5 seconds as it should,
	// OnError will be called, and the test is passed. Otherwise, test is failed.

	ts := newTestServer()
	defer ts.Close()

	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel()

	c := NewCollector(StdlibContext(ctx))

	onErrorCalled := false

	c.OnResponse(func(resp *Response) {
		t.Error("OnResponse was called, expected OnError")
	})

	c.OnError(func(resp *Response, err error) {
		onErrorCalled = true
		if err != context.DeadlineExceeded {
			t.Errorf("OnError got err=%#v, expected context.DeadlineExceeded", err)
		}
	})

	err := c.Visit(ts.URL + "/slow")
	if err != context.DeadlineExceeded {
		t.Errorf("Visit return err=%#v, expected context.DeadlineExceeded", err)
	}

	if !onErrorCalled {
		t.Error("OnError was not called")
	}

}

func BenchmarkOnHTML(b *testing.B) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()
	c.OnHTML("p", func(_ *HTMLElement) {})

	for n := 0; n < b.N; n++ {
		c.Visit(fmt.Sprintf("%s/html?q=%d", ts.URL, n))
	}
}

func BenchmarkOnXML(b *testing.B) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()
	c.OnXML("//p", func(_ *XMLElement) {})

	for n := 0; n < b.N; n++ {
		c.Visit(fmt.Sprintf("%s/html?q=%d", ts.URL, n))
	}
}

func BenchmarkOnResponse(b *testing.B) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()
	c.AllowURLRevisit = true
	c.OnResponse(func(_ *Response) {})

	for n := 0; n < b.N; n++ {
		c.Visit(ts.URL)
	}
}

func requireSessionCookieSimple(handler http.Handler) http.Handler {
	const cookieName = "session_id"

	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if _, err := r.Cookie(cookieName); err == http.ErrNoCookie {
			http.SetCookie(w, &http.Cookie{Name: cookieName, Value: "1"})
			http.Redirect(w, r, r.RequestURI, http.StatusFound)
			return
		}
		handler.ServeHTTP(w, r)
	})
}

func requireSessionCookieAuthPage(handler http.Handler) http.Handler {
	const setCookiePath = "/auth"
	const cookieName = "session_id"

	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == setCookiePath {
			destination := r.URL.Query().Get("return")
			http.Redirect(w, r, destination, http.StatusFound)
			return
		}
		if _, err := r.Cookie(cookieName); err == http.ErrNoCookie {
			http.SetCookie(w, &http.Cookie{Name: cookieName, Value: "1"})
			http.Redirect(w, r, setCookiePath+"?return="+url.QueryEscape(r.RequestURI), http.StatusFound)
			return
		}
		handler.ServeHTTP(w, r)
	})
}

func TestCallbackDetachment(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()
	c.AllowURLRevisit = true

	var executions [3]int // tracks number of executions of each callback

	c.OnHTML("#firstElem", func(e *HTMLElement) {
		executions[0]++
		// Detach this callback after first execution
		c.OnHTMLDetach("#firstElem")
	})
	c.OnHTML("#secondElem", func(e *HTMLElement) {
		executions[1]++
	})
	c.OnHTML("#thirdElem", func(e *HTMLElement) {
		executions[2]++
	})

	// First visit - all callbacks should execute
	c.Visit(ts.URL + "/callback_test")
	// Second visit - first callback should NOT execute
	c.Visit(ts.URL + "/callback_test")

	// Verify callback counts
	if executions[0] != 1 {
		t.Errorf("firstElem callback executed %d times, expected 1", executions[0])
	}
	if executions[1] != 2 {
		t.Errorf("secondElem callback executed %d times, expected 2", executions[1])
	}
	if executions[2] != 2 {
		t.Errorf("thirdElem callback executed %d times, expected 2", executions[2])
	}
}

func TestCollectorPostRetry(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	postValue := "hello"
	c := NewCollector()
	try := false
	c.OnResponse(func(r *Response) {
		if r.Ctx.Get("notFirst") == "" {
			r.Ctx.Put("notFirst", "first")
			_ = r.Request.Retry()
			return
		}
		if postValue != string(r.Body) {
			t.Error("Failed to send data with POST")
		}
		try = true
	})

	c.Post(ts.URL+"/login", map[string]string{
		"name": postValue,
	})
	if !try {
		t.Error("OnResponse Retry was not called")
	}
}
func TestCollectorGetRetry(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()
	try := false

	c := NewCollector()

	c.OnResponse(func(r *Response) {
		if r.Ctx.Get("notFirst") == "" {
			r.Ctx.Put("notFirst", "first")
			_ = r.Request.Retry()
			return
		}
		if !bytes.Equal(r.Body, serverIndexResponse) {
			t.Error("Response body does not match with the original content")
		}
		try = true
	})

	c.Visit(ts.URL)
	if !try {
		t.Error("OnResponse Retry was not called")
	}
}

func TestCollectorPostRetryUnseekable(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()
	try := false
	postValue := "hello"
	c := NewCollector()

	c.OnResponse(func(r *Response) {
		if postValue != string(r.Body) {
			t.Error("Failed to send data with POST")
		}

		if r.Ctx.Get("notFirst") == "" {
			r.Ctx.Put("notFirst", "first")
			err := r.Request.Retry()
			if !errors.Is(err, ErrRetryBodyUnseekable) {
				t.Errorf("Unexpected error Type ErrRetryBodyUnseekable : %v", err)
			}
			return
		}
		try = true
	})
	c.Request("POST", ts.URL+"/login", bytes.NewBuffer([]byte("name="+postValue)), nil, nil)
	if try {
		t.Error("OnResponse Retry was called but BodyUnseekable")
	}
}

func TestRedirectErrorRetry(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()
	c := NewCollector()
	c.OnError(func(r *Response, err error) {
		if r.Ctx.Get("notFirst") == "" {
			r.Ctx.Put("notFirst", "first")
			_ = r.Request.Retry()
			return
		}
		if e := (&AlreadyVisitedError{}); errors.As(err, &e) {
			t.Error("loop AlreadyVisitedError")
		}

	})
	c.OnResponse(func(response *Response) {
		//println(1)
	})
	c.Visit(ts.URL + "/redirected/")
	c.Visit(ts.URL + "/redirect")
}

func TestCheckRequestHeadersFunc(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()
	try := false

	c := NewCollector()

	c.OnRequestHeaders(func(r *Request) {
		try = true
		r.Abort()
	})
	c.OnScraped(func(r *Response) {
		try = false
	})
	c.Visit(ts.URL)
	if try == false {
		t.Error("TestCheckRequestHeadersFunc failed")
	}
}

func TestIssue745GzipURLWith404Response(t *testing.T) {
	ts := newTestServer()
	defer ts.Close()

	c := NewCollector()

	var responseStatusCode int
	c.OnError(func(resp *Response, err error) {
		responseStatusCode = resp.StatusCode
		// The error should NOT be "gzip: invalid header".
		// A 404 response for a .xml.gz URL should be treated as a
		// normal HTTP error, not a decompression failure.
		if strings.Contains(err.Error(), "gzip") {
			t.Errorf("Expected HTTP error, got gzip decompression error: %v", err)
		}
	})

	c.OnResponse(func(resp *Response) {
		// A 404 should not reach OnResponse as a successful response
		if resp.StatusCode == 404 {
			responseStatusCode = resp.StatusCode
		}
	})

	c.Visit(ts.URL + "/sitemap.xml.gz")

	// The response should have been received (either via OnError or OnResponse)
	// with status 404, not a gzip decompression error
	if responseStatusCode != 404 {
		t.Errorf("Expected status code 404, got %d", responseStatusCode)
	}
}
```

## File: `context.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package colly

import (
	"sync"
)

// Context provides a tiny layer for passing data between callbacks
type Context struct {
	contextMap map[string]interface{}
	lock       *sync.RWMutex
}

// NewContext initializes a new Context instance
func NewContext() *Context {
	return &Context{
		contextMap: make(map[string]interface{}),
		lock:       &sync.RWMutex{},
	}
}

// UnmarshalBinary decodes Context value to nil
// This function is used by request caching
func (c *Context) UnmarshalBinary(_ []byte) error {
	return nil
}

// MarshalBinary encodes Context value
// This function is used by request caching
func (c *Context) MarshalBinary() (_ []byte, _ error) {
	return nil, nil
}

// Put stores a value of any type in Context
func (c *Context) Put(key string, value interface{}) {
	c.lock.Lock()
	c.contextMap[key] = value
	c.lock.Unlock()
}

// Get retrieves a string value from Context.
// Get returns an empty string if key not found
func (c *Context) Get(key string) string {
	c.lock.RLock()
	defer c.lock.RUnlock()
	if v, ok := c.contextMap[key]; ok {
		return v.(string)
	}
	return ""
}

// GetAny retrieves a value from Context.
// GetAny returns nil if key not found
func (c *Context) GetAny(key string) interface{} {
	c.lock.RLock()
	defer c.lock.RUnlock()
	if v, ok := c.contextMap[key]; ok {
		return v
	}
	return nil
}

// ForEach iterate context
func (c *Context) ForEach(fn func(k string, v interface{}) interface{}) []interface{} {
	c.lock.RLock()
	defer c.lock.RUnlock()

	ret := make([]interface{}, 0, len(c.contextMap))
	for k, v := range c.contextMap {
		ret = append(ret, fn(k, v))
	}

	return ret
}

// Clone clones context
func (c *Context) Clone() *Context {
	c.lock.RLock()
	defer c.lock.RUnlock()
	newCtx := NewContext()
	c.ForEach(func(key string, value interface{}) interface{} {
		newCtx.Put(key, value)
		return nil
	})
	return newCtx
}
```

## File: `context_test.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package colly

import (
	"strconv"
	"testing"
)

func TestContextIteration(t *testing.T) {
	ctx := NewContext()
	for i := 0; i < 10; i++ {
		ctx.Put(strconv.Itoa(i), i)
	}
	values := ctx.ForEach(func(k string, v interface{}) interface{} {
		return v.(int)
	})
	if len(values) != 10 {
		t.Fatal("fail to iterate context")
	}
	for _, i := range values {
		v := i.(int)
		if v != ctx.GetAny(strconv.Itoa(v)).(int) {
			t.Fatal("value not equal")
		}
	}
}

func TestContextClone(t *testing.T) {
	ctxOrg := NewContext()
	for i := 0; i < 10; i++ {
		ctxOrg.Put(strconv.Itoa(i), i)
	}

	ctx := ctxOrg.Clone()
	values := ctx.ForEach(func(k string, v interface{}) interface{} {
		return v.(int)
	})
	if len(values) != 10 {
		t.Fatal("fail to iterate context")
	}
	for _, i := range values {
		v := i.(int)
		if v != ctx.GetAny(strconv.Itoa(v)).(int) {
			t.Fatal("value not equal")
		}
	}
}
```

## File: `CONTRIBUTING.md`
```markdown
# Contribute

## Introduction

First, thank you for considering contributing to colly! It's people like you that make the open source community such a great community! 😊

We welcome any type of contribution, not only code. You can help with 
- **QA**: file bug reports, the more details you can give the better (e.g. screenshots with the console open)
- **Marketing**: writing blog posts, howto's, printing stickers, ...
- **Community**: presenting the project at meetups, organizing a dedicated meetup for the local community, ...
- **Code**: take a look at the [open issues](https://github.com/gocolly/colly/issues). Even if you can't write code, commenting on them, showing that you care about a given issue matters. It helps us triage them.
- **Money**: we welcome financial contributions in full transparency on our [open collective](https://opencollective.com/colly).

## Your First Contribution

Working on your first Pull Request? You can learn how from this *free* series, [How to Contribute to an Open Source Project on GitHub](https://app.egghead.io/playlists/how-to-contribute-to-an-open-source-project-on-github).

## Submitting code

Any code change should be submitted as a pull request. The description should explain what the code does and give steps to execute it. The pull request should also contain tests.

## Code review process

The bigger the pull request, the longer it will take to review and merge. Try to break down large pull requests in smaller chunks that are easier to review and merge.
It is also always helpful to have some context for your pull request. What was the purpose? Why does it matter to you?

## Financial contributions

We also welcome financial contributions in full transparency on our [open collective](https://opencollective.com/colly).
Anyone can file an expense. If the expense makes sense for the development of the community, it will be "merged" in the ledger of our open collective by the core contributors and the person who filed the expense will be reimbursed.

## Questions

If you have any questions, create an [issue](https://github.com/gocolly/colly/issues/new) (protip: do a quick search first to see if someone else didn't ask the same question before!).
You can also reach us at hello@colly.opencollective.com.

## Credits

### Contributors

Thank you to all the people who have already contributed to colly!
<a href="graphs/contributors"><img src="https://opencollective.com/colly/contributors.svg?width=890" /></a>


### Backers

Thank you to all our backers! [[Become a backer](https://opencollective.com/colly#backer)]

<a href="https://opencollective.com/colly#backers" target="_blank"><img src="https://opencollective.com/colly/backers.svg?width=890"></a>


### Sponsors

Thank you to all our sponsors! (please ask your company to also support this open source project by [becoming a sponsor](https://opencollective.com/colly#sponsor))

<a href="https://opencollective.com/colly/sponsor/0/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/1/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/2/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/3/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/4/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/5/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/6/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/7/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/8/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/9/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/9/avatar.svg"></a>

<!-- This `CONTRIBUTING.md` is based on @nayafia's template https://github.com/nayafia/contributing-template -->
```

## File: `go.mod`
```
module github.com/gocolly/colly/v2

go 1.24.0

toolchain go1.24.9

require (
	github.com/PuerkitoBio/goquery v1.11.0
	github.com/antchfx/htmlquery v1.3.5
	github.com/antchfx/xmlquery v1.5.0
	github.com/gobwas/glob v0.2.3
	github.com/gocolly/colly v1.2.0
	github.com/jawher/mow.cli v1.1.0
	github.com/kennygrant/sanitize v1.2.4
	github.com/nlnwa/whatwg-url v0.6.2
	github.com/saintfish/chardet v0.0.0-20230101081208-5e3ef4b5456d
	github.com/temoto/robotstxt v1.1.2
	golang.org/x/net v0.47.0
	google.golang.org/appengine v1.6.8
)

require (
	github.com/andybalholm/cascadia v1.3.3 // indirect
	github.com/antchfx/xpath v1.3.5 // indirect
	github.com/bits-and-blooms/bitset v1.24.4 // indirect
	github.com/golang/groupcache v0.0.0-20241129210726-2c02b8208cf8 // indirect
	github.com/golang/protobuf v1.5.4 // indirect
	golang.org/x/text v0.31.0 // indirect
	google.golang.org/protobuf v1.36.10 // indirect
)
```

## File: `go.sum`
```
github.com/PuerkitoBio/goquery v1.10.2 h1:7fh2BdHcG6VFZsK7toXBT/Bh1z5Wmy8Q9MV9HqT2AM8=
github.com/PuerkitoBio/goquery v1.10.2/go.mod h1:0guWGjcLu9AYC7C1GHnpysHy056u9aEkUHwhdnePMCU=
github.com/PuerkitoBio/goquery v1.11.0 h1:jZ7pwMQXIITcUXNH83LLk+txlaEy6NVOfTuP43xxfqw=
github.com/PuerkitoBio/goquery v1.11.0/go.mod h1:wQHgxUOU3JGuj3oD/QFfxUdlzW6xPHfqyHre6VMY4DQ=
github.com/andybalholm/cascadia v1.3.3 h1:AG2YHrzJIm4BZ19iwJ/DAua6Btl3IwJX+VI4kktS1LM=
github.com/andybalholm/cascadia v1.3.3/go.mod h1:xNd9bqTn98Ln4DwST8/nG+H0yuB8Hmgu1YHNnWw0GeA=
github.com/antchfx/htmlquery v1.3.4 h1:Isd0srPkni2iNTWCwVj/72t7uCphFeor5Q8nCzj1jdQ=
github.com/antchfx/htmlquery v1.3.4/go.mod h1:K9os0BwIEmLAvTqaNSua8tXLWRWZpocZIH73OzWQbwM=
github.com/antchfx/htmlquery v1.3.5 h1:aYthDDClnG2a2xePf6tys/UyyM/kRcsFRm+ifhFKoU0=
github.com/antchfx/htmlquery v1.3.5/go.mod h1:5oyIPIa3ovYGtLqMPNjBF2Uf25NPCKsMjCnQ8lvjaoA=
github.com/antchfx/xmlquery v1.4.4 h1:mxMEkdYP3pjKSftxss4nUHfjBhnMk4imGoR96FRY2dg=
github.com/antchfx/xmlquery v1.4.4/go.mod h1:AEPEEPYE9GnA2mj5Ur2L5Q5/2PycJ0N9Fusrx9b12fc=
github.com/antchfx/xmlquery v1.5.0 h1:uAi+mO40ZWfyU6mlUBxRVvL6uBNZ6LMU4M3+mQIBV4c=
github.com/antchfx/xmlquery v1.5.0/go.mod h1:lJfWRXzYMK1ss32zm1GQV3gMIW/HFey3xDZmkP1SuNc=
github.com/antchfx/xpath v1.3.3 h1:tmuPQa1Uye0Ym1Zn65vxPgfltWb/Lxu2jeqIGteJSRs=
github.com/antchfx/xpath v1.3.3/go.mod h1:i54GszH55fYfBmoZXapTHN8T8tkcHfRgLyVwwqzXNcs=
github.com/antchfx/xpath v1.3.5 h1:PqbXLC3TkfeZyakF5eeh3NTWEbYl4VHNVeufANzDbKQ=
github.com/antchfx/xpath v1.3.5/go.mod h1:i54GszH55fYfBmoZXapTHN8T8tkcHfRgLyVwwqzXNcs=
github.com/bits-and-blooms/bitset v1.20.0/go.mod h1:7hO7Gc7Pp1vODcmWvKMRA9BNmbv6a/7QIWpPxHddWR8=
github.com/bits-and-blooms/bitset v1.22.0 h1:Tquv9S8+SGaS3EhyA+up3FXzmkhxPGjQQCkcs2uw7w4=
github.com/bits-and-blooms/bitset v1.22.0/go.mod h1:7hO7Gc7Pp1vODcmWvKMRA9BNmbv6a/7QIWpPxHddWR8=
github.com/bits-and-blooms/bitset v1.24.4 h1:95H15Og1clikBrKr/DuzMXkQzECs1M6hhoGXLwLQOZE=
github.com/bits-and-blooms/bitset v1.24.4/go.mod h1:7hO7Gc7Pp1vODcmWvKMRA9BNmbv6a/7QIWpPxHddWR8=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/gobwas/glob v0.2.3 h1:A4xDbljILXROh+kObIiy5kIaPYD8e96x1tgBhUI5J+Y=
github.com/gobwas/glob v0.2.3/go.mod h1:d3Ez4x06l9bZtSvzIay5+Yzi0fmZzPgnTbPcKjJAkT8=
github.com/gocolly/colly v1.2.0 h1:qRz9YAn8FIH0qzgNUw+HT9UN7wm1oF9OBAilwEWpyrI=
github.com/gocolly/colly v1.2.0/go.mod h1:Hof5T3ZswNVsOHYmba1u03W65HDWgpV5HifSuueE0EA=
github.com/golang/groupcache v0.0.0-20210331224755-41bb18bfe9da/go.mod h1:cIg4eruTrX1D+g88fzRXU5OdNfaM+9IcxsU14FzY7Hc=
github.com/golang/groupcache v0.0.0-20241129210726-2c02b8208cf8 h1:f+oWsMOmNPc8JmEHVZIycC7hBoQxHH9pNKQORJNozsQ=
github.com/golang/groupcache v0.0.0-20241129210726-2c02b8208cf8/go.mod h1:wcDNUvekVysuuOpQKo3191zZyTpiI6se1N1ULghS0sw=
github.com/golang/protobuf v1.5.0/go.mod h1:FsONVRAS9T7sI+LIUmWTfcYkHO4aIWwzhcaSAoJOfIk=
github.com/golang/protobuf v1.5.2/go.mod h1:XVQd3VNwM+JqD3oG2Ue2ip4fOMUkwXdXDdiuN0vRsmY=
github.com/golang/protobuf v1.5.4 h1:i7eJL8qZTpSEXOPTxNKhASYpMn+8e5Q6AdndVa1dWek=
github.com/golang/protobuf v1.5.4/go.mod h1:lnTiLA8Wa4RWRcIUkrtSVa5nRhsEGBg48fD6rSs7xps=
github.com/google/go-cmp v0.5.5/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.6.0 h1:ofyhxvXcZhMsU5ulbFiLKl/XBFqE1GSq7atu8tAmTRI=
github.com/google/go-cmp v0.6.0/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/google/go-cmp v0.7.0 h1:wk8382ETsv4JYUZwIsn6YpYiWiBsYLSJiTsyBybVuN8=
github.com/jawher/mow.cli v1.1.0 h1:NdtHXRc0CwZQ507wMvQ/IS+Q3W3x2fycn973/b8Zuk8=
github.com/jawher/mow.cli v1.1.0/go.mod h1:aNaQlc7ozF3vw6IJ2dHjp2ZFiA4ozMIYY6PyuRJwlUg=
github.com/kennygrant/sanitize v1.2.4 h1:gN25/otpP5vAsO2djbMhF/LQX6R7+O1TB4yv8NzpJ3o=
github.com/kennygrant/sanitize v1.2.4/go.mod h1:LGsjYYtgxbetdg5owWB2mpgUL6e2nfw2eObZ0u0qvak=
github.com/nlnwa/whatwg-url v0.6.1 h1:Zlefa3aglQFHF/jku45VxbEJwPicDnOz64Ra3F7npqQ=
github.com/nlnwa/whatwg-url v0.6.1/go.mod h1:x0FPXJzzOEieQtsBT/AKvbiBbQ46YlL6Xa7m02M1ECk=
github.com/nlnwa/whatwg-url v0.6.2 h1:jU61lU2ig4LANydbEJmA2nPrtCGiKdtgT0rmMd2VZ/Q=
github.com/nlnwa/whatwg-url v0.6.2/go.mod h1:x0FPXJzzOEieQtsBT/AKvbiBbQ46YlL6Xa7m02M1ECk=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/saintfish/chardet v0.0.0-20230101081208-5e3ef4b5456d h1:hrujxIzL1woJ7AwssoOcM/tq5JjjG2yYOc8odClEiXA=
github.com/saintfish/chardet v0.0.0-20230101081208-5e3ef4b5456d/go.mod h1:uugorj2VCxiV1x+LzaIdVa9b4S4qGAcH6cbhh4qVxOU=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.2.0/go.mod h1:qt09Ya8vawLte6SNmTgCsAVtYtaKzEcn8ATUoHMkEqE=
github.com/stretchr/testify v1.3.0 h1:TivCn/peBQ7UY8ooIcPgZFpTNSz0Q2U6UrFlUfqbe0Q=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/temoto/robotstxt v1.1.2 h1:W2pOjSJ6SWvldyEuiFXNxz3xZ8aiWX5LbfDiOFd7Fxg=
github.com/temoto/robotstxt v1.1.2/go.mod h1:+1AmkuG3IYkh1kv0d2qEB9Le88ehNO0zwOr3ujewlOo=
github.com/yuin/goldmark v1.4.13/go.mod h1:6yULJ656Px+3vBD8DxQVa3kxgyrAnzto9xy5taEt/CY=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20210921155107-089bfa567519/go.mod h1:GvvjBRRGRdwPK5ydBHafDWAxML/pGHZbMvKqRZ5+Abc=
golang.org/x/crypto v0.13.0/go.mod h1:y6Z2r+Rw4iayiXXAIxJIDAJ1zMW4yaTpebo8fPOliYc=
golang.org/x/crypto v0.19.0/go.mod h1:Iy9bg/ha4yyC70EfRS8jz+B6ybOBKMaSxLj6P6oBDfU=
golang.org/x/crypto v0.23.0/go.mod h1:CKFgDieR+mRhux2Lsu27y0fO304Db0wZe70UKqHu0v8=
golang.org/x/crypto v0.31.0/go.mod h1:kDsLvtWBEx7MV9tJOj9bnXsPbxwJQ6csT/x4KIN4Ssk=
golang.org/x/crypto v0.32.0/go.mod h1:ZnnJkOaASj8g0AjIduWNlq2NRxL0PlBrbKVyZ6V/Ugc=
golang.org/x/mod v0.6.0-dev.0.20220419223038-86c51ed26bb4/go.mod h1:jJ57K6gSWd91VN4djpZkiMVwK6gcyfeH4XE8wZrZaV4=
golang.org/x/mod v0.8.0/go.mod h1:iBbtSCu2XBx23ZKBPSOrRkjjQPZFPuis4dIYUhu/chs=
golang.org/x/mod v0.12.0/go.mod h1:iBbtSCu2XBx23ZKBPSOrRkjjQPZFPuis4dIYUhu/chs=
golang.org/x/mod v0.15.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/mod v0.17.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/net v0.0.0-20190620200207-3b0461eec859/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20210226172049-e18ecbb05110/go.mod h1:m0MpNAwzfU5UDzcl9v0D8zg8gWTRqZa9RBIspLL5mdg=
golang.org/x/net v0.0.0-20220722155237-a158d28d115b/go.mod h1:XRhObCWvk6IyKnWLug+ECip1KBveYUHfp+8e9klMJ9c=
golang.org/x/net v0.6.0/go.mod h1:2Tu9+aMcznHK/AK1HMvgo6xiTLG5rD5rZLDS+rp2Bjs=
golang.org/x/net v0.10.0/go.mod h1:0qNGK6F8kojg2nk9dLZ2mShWaEBan6FAoqfSigmmuDg=
golang.org/x/net v0.15.0/go.mod h1:idbUs1IY1+zTqbi8yxTbhexhEEk5ur9LInksu6HrEpk=
golang.org/x/net v0.21.0/go.mod h1:bIjVDfnllIU7BJ2DNgfnXvpSvtn8VRwhlsaeUTyUS44=
golang.org/x/net v0.25.0/go.mod h1:JkAGAh7GEvH74S6FOH42FLoXpXbE/aqXSrIQjXgsiwM=
golang.org/x/net v0.33.0/go.mod h1:HXLR5J+9DxmrqMwG9qjGCxZ+zKXxBru04zlTvWlWuN4=
golang.org/x/net v0.34.0/go.mod h1:di0qlW3YNM5oh6GqDGQr92MyTozJPmybPK4Ev/Gm31k=
golang.org/x/net v0.37.0 h1:1zLorHbz+LYj7MQlSf1+2tPIIgibq2eL5xkrGk6f+2c=
golang.org/x/net v0.37.0/go.mod h1:ivrbrMbzFq5J41QOQh0siUuly180yBYtLp+CKbEaFx8=
golang.org/x/net v0.47.0 h1:Mx+4dIFzqraBXUugkia1OOvlD6LemFo1ALMHjrXDOhY=
golang.org/x/net v0.47.0/go.mod h1:/jNxtkgq5yWUGYkaZGqo27cfGZ1c5Nen03aYrrKpVRU=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20220722155255-886fb9371eb4/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.1.0/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.3.0/go.mod h1:FU7BRWz2tNW+3quACPkgCx/L+uEAv1htQ0V83Z9Rj+Y=
golang.org/x/sync v0.6.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.7.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.10.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20201119102817-f84b799fce68/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210615035016-665e8c7367d1/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220520151302-bc2c85ada10a/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220722155257-8c9f86f7a55f/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.5.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.8.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.12.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.17.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/sys v0.20.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/sys v0.28.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/sys v0.29.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/telemetry v0.0.0-20240228155512-f48c80bd79b2/go.mod h1:TeRTkGYfJXctD9OcfyVLyj2J3IxLnKwHJR8f4D8a3YE=
golang.org/x/term v0.0.0-20201126162022-7de9c90e9dd1/go.mod h1:bj7SfCRtBDWHUb9snDiAeCFNEtKQo2Wmx5Cou7ajbmo=
golang.org/x/term v0.0.0-20210927222741-03fcf44c2211/go.mod h1:jbD1KX2456YbFQfuXm/mYQcufACuNUgVhRMnK/tPxf8=
golang.org/x/term v0.5.0/go.mod h1:jMB1sMXY+tzblOD4FWmEbocvup2/aLOaQEp7JmGp78k=
golang.org/x/term v0.8.0/go.mod h1:xPskH00ivmX89bAKVGSKKtLOWNx2+17Eiy94tnKShWo=
golang.org/x/term v0.12.0/go.mod h1:owVbMEjm3cBLCHdkQu9b1opXd4ETQWc3BhuQGKgXgvU=
golang.org/x/term v0.17.0/go.mod h1:lLRBjIVuehSbZlaOtGMbcMncT+aqLLLmKrsjNrUguwk=
golang.org/x/term v0.20.0/go.mod h1:8UkIAJTvZgivsXaD6/pH6U9ecQzZ45awqEOzuCvwpFY=
golang.org/x/term v0.27.0/go.mod h1:iMsnZpn0cago0GOrHO2+Y7u7JPn5AylBrcoWkElMTSM=
golang.org/x/term v0.28.0/go.mod h1:Sw/lC2IAUZ92udQNf3WodGtn4k/XoLyZoh8v/8uiwek=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.3/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.7/go.mod h1:u+2+/6zg+i71rQMx5EYifcz6MCKuco9NR6JIITiCfzQ=
golang.org/x/text v0.3.8/go.mod h1:E6s5w1FMmriuDzIBO73fBruAKo1PCIq6d2Q6DHfQ8WQ=
golang.org/x/text v0.7.0/go.mod h1:mrYo+phRRbMaCq/xk9113O4dZlRixOauAjOtrjsXDZ8=
golang.org/x/text v0.9.0/go.mod h1:e1OnstbJyHTd6l/uOt8jFFHp6TRDWZR/bV3emEE/zU8=
golang.org/x/text v0.13.0/go.mod h1:TvPlkZtksWOMsz7fbANvkp4WM8x/WCo/om8BMLbz+aE=
golang.org/x/text v0.14.0/go.mod h1:18ZOQIKpY8NJVqYksKHtTdi31H5itFRjB5/qKTNYzSU=
golang.org/x/text v0.15.0/go.mod h1:18ZOQIKpY8NJVqYksKHtTdi31H5itFRjB5/qKTNYzSU=
golang.org/x/text v0.21.0/go.mod h1:4IBbMaMmOPCJ8SecivzSH54+73PCFmPWxNTLm+vZkEQ=
golang.org/x/text v0.23.0 h1:D71I7dUrlY+VX0gQShAThNGHFxZ13dGLBHQLVl1mJlY=
golang.org/x/text v0.23.0/go.mod h1:/BLNzu4aZCJ1+kcD0DNRotWKage4q2rGVAg4o22unh4=
golang.org/x/text v0.31.0 h1:aC8ghyu4JhP8VojJ2lEHBnochRno1sgL6nEi9WGFGMM=
golang.org/x/text v0.31.0/go.mod h1:tKRAlv61yKIjGGHX/4tP1LTbc13YSec1pxVEWXzfoeM=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20191119224855-298f0cb1881e/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.1.12/go.mod h1:hNGJHUnrk76NpqgfD5Aqm5Crs+Hm0VOH/i9J2+nxYbc=
golang.org/x/tools v0.6.0/go.mod h1:Xwgl3UAJ/d3gWutnCtw505GrjyAbvKui8lOU390QaIU=
golang.org/x/tools v0.13.0/go.mod h1:HvlwmtVNQAhOuCjW7xxvovg8wbNq7LwfXh/k7wXUl58=
golang.org/x/tools v0.21.1-0.20240508182429-e35e4ccd0d2d/go.mod h1:aiJjzUbINMkxbQROHiO6hDPo2LHcIPhhQsa9DLh0yGk=
golang.org/x/xerrors v0.0.0-20190717185122-a985d3407aa7/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
google.golang.org/appengine v1.6.8 h1:IhEN5q69dyKagZPYMSdIjS2HqprW324FRQZJcGqPAsM=
google.golang.org/appengine v1.6.8/go.mod h1:1jJ3jBArFh5pcgW8gCtRJnepW8FzD1V44FJffLiz/Ds=
google.golang.org/protobuf v1.26.0-rc.1/go.mod h1:jlhhOSvTdKEhbULTjvd4ARK9grFBp09yW+WbY/TyQbw=
google.golang.org/protobuf v1.26.0/go.mod h1:9q0QmTI4eRPtz6boOQmLYwt+qCgq0jsYwAQnmE0givc=
google.golang.org/protobuf v1.36.6 h1:z1NpPI8ku2WgiWnf+t9wTPsn6eP1L7ksHUlkfLvd9xY=
google.golang.org/protobuf v1.36.6/go.mod h1:jduwjTPXsFjZGTmRluh+L6NjiWu7pchiJ2/5YcXBHnY=
google.golang.org/protobuf v1.36.10 h1:AYd7cD/uASjIL6Q9LiTjz8JLcrh/88q5UObnmY3aOOE=
google.golang.org/protobuf v1.36.10/go.mod h1:HTf+CrKn2C3g5S8VImy6tdcUvCska2kB7j23XfzDpco=
```

## File: `htmlelement.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package colly

import (
	"strings"

	"github.com/PuerkitoBio/goquery"
	"golang.org/x/net/html"
)

// HTMLElement is the representation of a HTML tag.
type HTMLElement struct {
	// Name is the name of the tag
	Name       string
	Text       string
	attributes []html.Attribute
	// Request is the request object of the element's HTML document
	Request *Request
	// Response is the Response object of the element's HTML document
	Response *Response
	// DOM is the goquery parsed DOM object of the page. DOM is relative
	// to the current HTMLElement
	DOM *goquery.Selection
	// Index stores the position of the current element within all the elements matched by an OnHTML callback
	Index int
}

// NewHTMLElementFromSelectionNode creates a HTMLElement from a goquery.Selection Node.
func NewHTMLElementFromSelectionNode(resp *Response, s *goquery.Selection, n *html.Node, idx int) *HTMLElement {
	return &HTMLElement{
		Name:       n.Data,
		Request:    resp.Request,
		Response:   resp,
		Text:       goquery.NewDocumentFromNode(n).Text(),
		DOM:        s,
		Index:      idx,
		attributes: n.Attr,
	}
}

// Attr returns the selected attribute of a HTMLElement or empty string
// if no attribute found
func (h *HTMLElement) Attr(k string) string {
	for _, a := range h.attributes {
		if a.Key == k {
			return a.Val
		}
	}
	return ""
}

// ChildText returns the concatenated and stripped text content of the matching
// elements.
func (h *HTMLElement) ChildText(goquerySelector string) string {
	return strings.TrimSpace(h.DOM.Find(goquerySelector).Text())
}

// ChildTexts returns the stripped text content of all the matching
// elements.
func (h *HTMLElement) ChildTexts(goquerySelector string) []string {
	var res []string
	h.DOM.Find(goquerySelector).Each(func(_ int, s *goquery.Selection) {

		res = append(res, strings.TrimSpace(s.Text()))
	})
	return res
}

// ChildAttr returns the stripped text content of the first matching
// element's attribute.
func (h *HTMLElement) ChildAttr(goquerySelector, attrName string) string {
	if attr, ok := h.DOM.Find(goquerySelector).Attr(attrName); ok {
		return strings.TrimSpace(attr)
	}
	return ""
}

// ChildAttrs returns the stripped text content of all the matching
// element's attributes.
func (h *HTMLElement) ChildAttrs(goquerySelector, attrName string) []string {
	var res []string
	h.DOM.Find(goquerySelector).Each(func(_ int, s *goquery.Selection) {
		if attr, ok := s.Attr(attrName); ok {
			res = append(res, strings.TrimSpace(attr))
		}
	})
	return res
}

// ForEach iterates over the elements matched by the first argument
// and calls the callback function on every HTMLElement match.
func (h *HTMLElement) ForEach(goquerySelector string, callback func(int, *HTMLElement)) {
	i := 0
	h.DOM.Find(goquerySelector).Each(func(_ int, s *goquery.Selection) {
		for _, n := range s.Nodes {
			callback(i, NewHTMLElementFromSelectionNode(h.Response, s, n, i))
			i++
		}
	})
}

// ForEachWithBreak iterates over the elements matched by the first argument
// and calls the callback function on every HTMLElement match.
// It is identical to ForEach except that it is possible to break
// out of the loop by returning false in the callback function. It returns the
// current Selection object.
func (h *HTMLElement) ForEachWithBreak(goquerySelector string, callback func(int, *HTMLElement) bool) {
	i := 0
	h.DOM.Find(goquerySelector).EachWithBreak(func(_ int, s *goquery.Selection) bool {
		for _, n := range s.Nodes {
			if callback(i, NewHTMLElementFromSelectionNode(h.Response, s, n, i)) {
				i++
				return true
			}
		}
		return false
	})
}
```

## File: `http_backend.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package colly

import (
	"crypto/sha1"
	"encoding/gob"
	"encoding/hex"
	"io"
	"math/rand"
	"net/http"
	"os"
	"path"
	"regexp"
	"strings"
	"sync"
	"time"

	"compress/gzip"

	"github.com/gobwas/glob"
)

type httpBackend struct {
	LimitRules []*LimitRule
	Client     *http.Client
	lock       *sync.RWMutex
}

type checkResponseHeadersFunc func(req *http.Request, statusCode int, header http.Header) bool
type checkRequestHeadersFunc func(req *http.Request) bool

// LimitRule provides connection restrictions for domains.
// Both DomainRegexp and DomainGlob can be used to specify
// the included domains patterns, but at least one is required.
// There can be two kind of limitations:
//   - Parallelism: Set limit for the number of concurrent requests to matching domains
//   - Delay: Wait specified amount of time between requests (parallelism is 1 in this case)
type LimitRule struct {
	// DomainRegexp is a regular expression to match against domains
	DomainRegexp string
	// DomainGlob is a glob pattern to match against domains
	DomainGlob string
	// Delay is the duration to wait before creating a new request to the matching domains
	Delay time.Duration
	// RandomDelay is the extra randomized duration to wait added to Delay before creating a new request
	RandomDelay time.Duration
	// Parallelism is the number of the maximum allowed concurrent requests of the matching domains
	Parallelism    int
	waitChan       chan bool
	compiledRegexp *regexp.Regexp
	compiledGlob   glob.Glob
}

// Init initializes the private members of LimitRule
func (r *LimitRule) Init() error {
	r.waitChan = make(chan bool, max(r.Parallelism, 1))
	hasPattern := false
	if r.DomainRegexp != "" {
		c, err := regexp.Compile(r.DomainRegexp)
		if err != nil {
			return err
		}
		r.compiledRegexp = c
		hasPattern = true
	}
	if r.DomainGlob != "" {
		c, err := glob.Compile(r.DomainGlob)
		if err != nil {
			return err
		}
		r.compiledGlob = c
		hasPattern = true
	}
	if !hasPattern {
		return ErrNoPattern
	}
	return nil
}

func (h *httpBackend) Init(jar http.CookieJar) {
	rand.Seed(time.Now().UnixNano())
	h.Client = &http.Client{
		Jar:     jar,
		Timeout: 10 * time.Second,
	}
	h.lock = &sync.RWMutex{}
}

// Match checks that the domain parameter triggers the rule
func (r *LimitRule) Match(domain string) bool {
	match := false
	if r.compiledRegexp != nil && r.compiledRegexp.MatchString(domain) {
		match = true
	}
	if r.compiledGlob != nil && r.compiledGlob.Match(domain) {
		match = true
	}
	return match
}

func (h *httpBackend) GetMatchingRule(domain string) *LimitRule {
	if h.LimitRules == nil {
		return nil
	}
	h.lock.RLock()
	defer h.lock.RUnlock()
	for _, r := range h.LimitRules {
		if r.Match(domain) {
			return r
		}
	}
	return nil
}

func (h *httpBackend) Cache(request *http.Request, bodySize int, checkRequestHeadersFunc checkRequestHeadersFunc, checkResponseHeadersFunc checkResponseHeadersFunc, cacheDir string, cacheExpiration time.Duration) (*Response, error) {
	if cacheDir == "" || request.Method != "GET" || request.Header.Get("Cache-Control") == "no-cache" {
		return h.Do(request, bodySize, checkRequestHeadersFunc, checkResponseHeadersFunc)
	}
	sum := sha1.Sum([]byte(request.URL.String()))
	hash := hex.EncodeToString(sum[:])
	dir := path.Join(cacheDir, hash[:2])
	filename := path.Join(dir, hash)

	if fileInfo, err := os.Stat(filename); err == nil && cacheExpiration > 0 {
		if time.Since(fileInfo.ModTime()) > cacheExpiration {
			_ = os.Remove(filename)
		}
	}

	if file, err := os.Open(filename); err == nil {
		resp := new(Response)
		err := gob.NewDecoder(file).Decode(resp)
		file.Close()
		checkResponseHeadersFunc(request, resp.StatusCode, *resp.Headers)
		if resp.StatusCode < 500 {
			return resp, err
		}
	}
	resp, err := h.Do(request, bodySize, checkRequestHeadersFunc, checkResponseHeadersFunc)
	if err != nil || resp.StatusCode >= 500 {
		return resp, err
	}
	if _, err := os.Stat(dir); err != nil {
		if err := os.MkdirAll(dir, 0750); err != nil {
			return resp, err
		}
	}
	file, err := os.Create(filename + "~")
	if err != nil {
		return resp, err
	}
	if err := gob.NewEncoder(file).Encode(resp); err != nil {
		file.Close()
		return resp, err
	}
	file.Close()
	return resp, os.Rename(filename+"~", filename)
}

func (h *httpBackend) Do(request *http.Request, bodySize int, checkRequestHeadersFunc checkRequestHeadersFunc, checkResponseHeadersFunc checkResponseHeadersFunc) (*Response, error) {
	r := h.GetMatchingRule(request.URL.Host)
	if r != nil {
		r.waitChan <- true
		defer func(r *LimitRule) {
			randomDelay := time.Duration(0)
			if r.RandomDelay != 0 {
				randomDelay = time.Duration(rand.Int63n(int64(r.RandomDelay)))
			}
			time.Sleep(r.Delay + randomDelay)
			<-r.waitChan
		}(r)
	}
	if !checkRequestHeadersFunc(request) {
		return nil, ErrAbortedBeforeRequest
	}
	res, err := h.Client.Do(request)
	if err != nil {
		return nil, err
	}
	defer res.Body.Close()

	finalRequest := request
	if res.Request != nil {
		finalRequest = res.Request
	}
	if !checkResponseHeadersFunc(finalRequest, res.StatusCode, res.Header) {
		// closing res.Body (see defer above) without reading it aborts
		// the download
		return nil, ErrAbortedAfterHeaders
	}

	var bodyReader io.Reader = res.Body
	if bodySize > 0 {
		bodyReader = io.LimitReader(bodyReader, int64(bodySize))
	}
	contentEncoding := strings.ToLower(res.Header.Get("Content-Encoding"))
	if !res.Uncompressed && (strings.Contains(contentEncoding, "gzip") || (contentEncoding == "" && strings.Contains(strings.ToLower(res.Header.Get("Content-Type")), "gzip")) || (strings.HasSuffix(strings.ToLower(finalRequest.URL.Path), ".xml.gz") && res.StatusCode >= 200 && res.StatusCode < 300)) {
		bodyReader, err = gzip.NewReader(bodyReader)
		if err != nil {
			return nil, err
		}
		defer bodyReader.(*gzip.Reader).Close()
	}
	body, err := io.ReadAll(bodyReader)
	if err != nil {
		return nil, err
	}
	return &Response{
		StatusCode: res.StatusCode,
		Body:       body,
		Headers:    &res.Header,
	}, nil
}

func (h *httpBackend) Limit(rule *LimitRule) error {
	h.lock.Lock()
	if h.LimitRules == nil {
		h.LimitRules = make([]*LimitRule, 0, 8)
	}
	h.LimitRules = append(h.LimitRules, rule)
	h.lock.Unlock()
	return rule.Init()
}

func (h *httpBackend) Limits(rules []*LimitRule) error {
	for _, r := range rules {
		if err := h.Limit(r); err != nil {
			return err
		}
	}
	return nil
}
```

## File: `http_trace.go`
```go
package colly

import (
	"net/http"
	"net/http/httptrace"
	"time"
)

// HTTPTrace provides a datastructure for storing an http trace.
type HTTPTrace struct {
	start, connect    time.Time
	ConnectDuration   time.Duration
	FirstByteDuration time.Duration
}

// trace returns a httptrace.ClientTrace object to be used with an http
// request via httptrace.WithClientTrace() that fills in the HttpTrace.
func (ht *HTTPTrace) trace() *httptrace.ClientTrace {
	trace := &httptrace.ClientTrace{
		ConnectStart: func(network, addr string) { ht.connect = time.Now() },
		ConnectDone: func(network, addr string, err error) {
			ht.ConnectDuration = time.Since(ht.connect)
		},

		GetConn: func(hostPort string) { ht.start = time.Now() },
		GotFirstResponseByte: func() {
			ht.FirstByteDuration = time.Since(ht.start)
		},
	}
	return trace
}

// WithTrace returns the given HTTP Request with this HTTPTrace added to its
// context.
func (ht *HTTPTrace) WithTrace(req *http.Request) *http.Request {
	return req.WithContext(httptrace.WithClientTrace(req.Context(), ht.trace()))
}
```

## File: `http_trace_test.go`
```go
package colly

import (
	"net/http"
	"net/http/httptest"
	"testing"
	"time"
)

const testDelay = 200 * time.Millisecond

func newTraceTestServer(delay time.Duration) *httptest.Server {
	mux := http.NewServeMux()

	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		time.Sleep(delay)
		w.WriteHeader(200)
	})
	mux.HandleFunc("/error", func(w http.ResponseWriter, r *http.Request) {
		time.Sleep(delay)
		w.WriteHeader(500)
	})

	return httptest.NewServer(mux)
}

func TestTraceWithNoDelay(t *testing.T) {
	ts := newTraceTestServer(0)
	defer ts.Close()

	client := ts.Client()
	req, err := http.NewRequest("GET", ts.URL, nil)
	if err != nil {
		t.Errorf("Failed to construct request %v", err)
	}
	trace := &HTTPTrace{}
	req = trace.WithTrace(req)

	if _, err = client.Do(req); err != nil {
		t.Errorf("Failed to make request %v", err)
	}

	if trace.ConnectDuration > testDelay {
		t.Errorf("trace ConnectDuration should be (almost) 0, got %v", trace.ConnectDuration)
	}
	if trace.FirstByteDuration > testDelay {
		t.Errorf("trace FirstByteDuration should be (almost) 0, got %v", trace.FirstByteDuration)
	}
}

func TestTraceWithDelay(t *testing.T) {
	ts := newTraceTestServer(testDelay)
	defer ts.Close()

	client := ts.Client()
	req, err := http.NewRequest("GET", ts.URL, nil)
	if err != nil {
		t.Errorf("Failed to construct request %v", err)
	}
	trace := &HTTPTrace{}
	req = trace.WithTrace(req)

	if _, err = client.Do(req); err != nil {
		t.Errorf("Failed to make request %v", err)
	}

	if trace.ConnectDuration > testDelay {
		t.Errorf("trace ConnectDuration should be (almost) 0, got %v", trace.ConnectDuration)
	}
	if trace.FirstByteDuration < testDelay {
		t.Errorf("trace FirstByteDuration should be at least 200ms, got %v", trace.FirstByteDuration)
	}
}
```

## File: `LICENSE.txt`
```

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `README.md`
```markdown
# Colly

Lightning Fast and Elegant Scraping Framework for Gophers

Colly provides a clean interface to write any kind of crawler/scraper/spider.

With Colly you can easily extract structured data from websites, which can be used for a wide range of applications, like data mining, data processing or archiving.

[![GoDoc](https://godoc.org/github.com/gocolly/colly?status.svg)](https://pkg.go.dev/github.com/gocolly/colly/v2)
[![Backers on Open Collective](https://opencollective.com/colly/backers/badge.svg)](#backers) [![Sponsors on Open Collective](https://opencollective.com/colly/sponsors/badge.svg)](#sponsors) [![build status](https://github.com/gocolly/colly/actions/workflows/ci.yml/badge.svg)](https://github.com/gocolly/colly/actions/workflows/ci.yml)
[![report card](https://img.shields.io/badge/report%20card-a%2B-ff3333.svg?style=flat-square)](http://goreportcard.com/report/gocolly/colly)
[![view examples](https://img.shields.io/badge/learn%20by-examples-0077b3.svg?style=flat-square)](https://github.com/gocolly/colly/tree/master/_examples)
[![Code Coverage](https://img.shields.io/codecov/c/github/gocolly/colly/master.svg)](https://codecov.io/github/gocolly/colly?branch=master)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fgocolly%2Fcolly.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fgocolly%2Fcolly?ref=badge_shield)
[![Twitter URL](https://img.shields.io/badge/twitter-follow-green.svg)](https://twitter.com/gocolly)


## Features

-   Clean API
-   Fast (>1k request/sec on a single core)
-   Manages request delays and maximum concurrency per domain
-   Automatic cookie and session handling
-   Sync/async/parallel scraping
-   Caching
-   Automatic encoding of non-unicode responses
-   Robots.txt support
-   Distributed scraping
-   Configuration via environment variables
-   Extensions

## Example

```go

import (
	"fmt"

	"github.com/gocolly/colly/v2"
)

func main() {
	c := colly.NewCollector()

	// Find and visit all links
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		e.Request.Visit(e.Attr("href"))
	})

	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL)
	})

	c.Visit("http://go-colly.org/")
}
```

See [examples folder](https://github.com/gocolly/colly/tree/master/_examples) for more detailed examples.

## Installation

`go get github.com/gocolly/colly/v2`


## Bugs

Bugs or suggestions? Visit the [issue tracker](https://github.com/gocolly/colly/issues) or join `#colly` on freenode

## Other Projects Using Colly

Below is a list of public, open source projects that use Colly:

-   [greenpeace/check-my-pages](https://github.com/greenpeace/check-my-pages) Scraping script to test the Spanish Greenpeace web archive.
-   [altsab/gowap](https://github.com/altsab/gowap) Wappalyzer implementation in Go.
-   [jesuiscamille/goquotes](https://github.com/jesuiscamille/goquotes) A quotes scraper, making your day a little better!
-   [jivesearch/jivesearch](https://github.com/jivesearch/jivesearch) A search engine that doesn't track you.
-   [Leagify/colly-draft-prospects](https://github.com/Leagify/colly-draft-prospects) A scraper for future NFL Draft prospects.
-   [lucasepe/go-ps4](https://github.com/lucasepe/go-ps4) Search playstation store for your favorite PS4 games using the command line.
-   [yringler/inside-chassidus-scraper](https://github.com/yringler/inside-chassidus-scraper) Scrapes Rabbi Paltiel's web site for lesson metadata.
-   [gamedb/gamedb](https://github.com/gamedb/gamedb) A database of Steam games.
-   [lawzava/scrape](https://github.com/lawzava/scrape) CLI for email scraping from any website.
-   [eureka101v/WeiboSpiderGo](https://github.com/eureka101v/WeiboSpiderGo) A sina weibo(chinese twitter) scraper
-   [Go-phie/gophie](https://github.com/Go-phie/gophie) Search, Download and Stream movies from your terminal
-   [imthaghost/goclone](https://github.com/imthaghost/goclone) Clone websites to your computer within seconds.
-   [superiss/spidy](https://github.com/superiss/spidy) Crawl the web and collect expired domains.
-   [docker-slim/docker-slim](https://github.com/docker-slim/docker-slim) Optimize your Docker containers to make them smaller and better.
-   [seversky/gachifinder](https://github.com/seversky/gachifinder) an agent for asynchronous scraping, parsing and writing to some storages(elasticsearch for now)
-   [eval-exec/goodreads](https://github.com/eval-exec/goodreads) crawl all tags and all pages of quotes from goodreads.

If you are using Colly in a project please send a pull request to add it to the list.

## Contributors

This project exists thanks to all the people who contribute. [[Contribute]](CONTRIBUTING.md).
<a href="https://github.com/gocolly/colly/graphs/contributors"><img src="https://opencollective.com/colly/contributors.svg?width=890" /></a>

## Backers

Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/colly#backer)]

<a href="https://opencollective.com/colly#backers" target="_blank"><img src="https://opencollective.com/colly/backers.svg?width=890"></a>

## Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/colly#sponsor)]

<a href="https://opencollective.com/colly/sponsor/0/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/1/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/2/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/3/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/4/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/5/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/6/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/7/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/8/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/colly/sponsor/9/website" target="_blank"><img src="https://opencollective.com/colly/sponsor/9/avatar.svg"></a>

## License

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fgocolly%2Fcolly.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fgocolly%2Fcolly?ref=badge_large)
```

## File: `request.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package colly

import (
	"bytes"
	"encoding/json"
	"io"
	"net/http"
	"net/url"
	"strings"
)

// Request is the representation of a HTTP request made by a Collector
type Request struct {
	// URL is the parsed URL of the HTTP request
	URL *url.URL
	// Headers contains the Request's HTTP headers
	Headers *http.Header
	// the Host header
	Host string
	// Ctx is a context between a Request and a Response
	Ctx *Context
	// Depth is the number of the parents of the request
	Depth int
	// Method is the HTTP method of the request
	Method string
	// Body is the request body which is used on POST/PUT requests
	Body io.Reader
	// ResponseCharacterencoding is the character encoding of the response body.
	// Leave it blank to allow automatic character encoding of the response body.
	// It is empty by default and it can be set in OnRequest callback.
	ResponseCharacterEncoding string
	// ID is the Unique identifier of the request
	ID        uint32
	collector *Collector
	abort     bool
	baseURL   *url.URL
	// ProxyURL is the proxy address that handles the request
	ProxyURL string
}

type serializableRequest struct {
	URL     string
	Method  string
	Depth   int
	Body    []byte
	ID      uint32
	Ctx     map[string]interface{}
	Headers http.Header
	Host    string
}

// New creates a new request with the context of the original request
func (r *Request) New(method, URL string, body io.Reader) (*Request, error) {
	u, err := urlParser.Parse(URL)
	if err != nil {
		return nil, err
	}
	u2, err := url.Parse(u.Href(false))
	if err != nil {
		return nil, err
	}
	return &Request{
		Method:    method,
		URL:       u2,
		Body:      body,
		Ctx:       r.Ctx,
		Headers:   &http.Header{},
		Host:      r.Host,
		ID:        r.collector.requestCount.Add(1),
		collector: r.collector,
	}, nil
}

// Abort cancels the HTTP request when called in an OnRequest callback
func (r *Request) Abort() {
	r.abort = true
}

// IsAbort returns true if the request has been aborted
func (r *Request) IsAbort() bool {
	return r.abort
}

// AbsoluteURL returns with the resolved absolute URL of an URL chunk.
// AbsoluteURL returns empty string if the URL chunk is a fragment or
// could not be parsed
func (r *Request) AbsoluteURL(u string) string {
	if strings.HasPrefix(u, "#") {
		return ""
	}
	var base *url.URL
	if r.baseURL != nil {
		base = r.baseURL
	} else {
		base = r.URL
	}

	absURL, err := urlParser.ParseRef(base.String(), u)
	if err != nil {
		return ""
	}
	return absURL.Href(false)
}

// Visit continues Collector's collecting job by creating a
// request and preserves the Context of the previous request.
// Visit also calls the previously provided callbacks
func (r *Request) Visit(URL string) error {
	return r.collector.scrape(r.AbsoluteURL(URL), "GET", r.Depth+1, nil, r.Ctx, nil, true)
}

// HasVisited checks if the provided URL has been visited
func (r *Request) HasVisited(URL string) (bool, error) {
	return r.collector.HasVisited(URL)
}

// Post continues a collector job by creating a POST request and preserves the Context
// of the previous request.
// Post also calls the previously provided callbacks
func (r *Request) Post(URL string, requestData map[string]string) error {
	return r.collector.scrape(r.AbsoluteURL(URL), "POST", r.Depth+1, createFormReader(requestData), r.Ctx, nil, true)
}

// PostRaw starts a collector job by creating a POST request with raw binary data.
// PostRaw preserves the Context of the previous request
// and calls the previously provided callbacks
func (r *Request) PostRaw(URL string, requestData []byte) error {
	return r.collector.scrape(r.AbsoluteURL(URL), "POST", r.Depth+1, bytes.NewReader(requestData), r.Ctx, nil, true)
}

// PostMultipart starts a collector job by creating a Multipart POST request
// with raw binary data.  PostMultipart also calls the previously provided.
// callbacks
func (r *Request) PostMultipart(URL string, requestData map[string][]byte) error {
	boundary := randomBoundary()
	hdr := http.Header{}
	hdr.Set("Content-Type", "multipart/form-data; boundary="+boundary)
	hdr.Set("User-Agent", r.collector.UserAgent)
	return r.collector.scrape(r.AbsoluteURL(URL), "POST", r.Depth+1, createMultipartReader(boundary, requestData), r.Ctx, hdr, true)
}

// Retry submits HTTP request again with the same parameters
func (r *Request) Retry() error {
	r.Headers.Del("Cookie")
	if _, ok := r.Body.(io.ReadSeeker); r.Body != nil && !ok {
		return ErrRetryBodyUnseekable
	}
	return r.collector.scrape(r.URL.String(), r.Method, r.Depth, r.Body, r.Ctx, *r.Headers, false)
}

// Do submits the request
func (r *Request) Do() error {
	return r.collector.scrape(r.URL.String(), r.Method, r.Depth, r.Body, r.Ctx, *r.Headers, !r.collector.AllowURLRevisit)
}

// Marshal serializes the Request
func (r *Request) Marshal() ([]byte, error) {
	ctx := make(map[string]interface{})
	if r.Ctx != nil {
		r.Ctx.ForEach(func(k string, v interface{}) interface{} {
			ctx[k] = v
			return nil
		})
	}
	var err error
	var body []byte
	if r.Body != nil {
		body, err = io.ReadAll(r.Body)
		if err != nil {
			return nil, err
		}
	}
	sr := &serializableRequest{
		URL:    r.URL.String(),
		Host:   r.Host,
		Method: r.Method,
		Depth:  r.Depth,
		Body:   body,
		ID:     r.ID,
		Ctx:    ctx,
	}
	if r.Headers != nil {
		sr.Headers = *r.Headers
	}
	return json.Marshal(sr)
}
```

## File: `response.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package colly

import (
	"bytes"
	"fmt"
	"io"
	"mime"
	"net/http"
	"os"
	"strings"

	"github.com/saintfish/chardet"
	"golang.org/x/net/html/charset"
)

// Response is the representation of a HTTP response made by a Collector
type Response struct {
	// StatusCode is the status code of the Response
	StatusCode int
	// Body is the content of the Response
	Body []byte
	// Ctx is a context between a Request and a Response
	Ctx *Context
	// Request is the Request object of the response
	Request *Request
	// Headers contains the Response's HTTP headers
	Headers *http.Header
	// Trace contains the HTTPTrace for the request. Will only be set by the
	// collector if Collector.TraceHTTP is set to true.
	Trace *HTTPTrace
}

// Save writes response body to disk
func (r *Response) Save(fileName string) error {
	return os.WriteFile(fileName, r.Body, 0644)
}

// FileName returns the sanitized file name parsed from "Content-Disposition"
// header or from URL
func (r *Response) FileName() string {
	_, params, err := mime.ParseMediaType(r.Headers.Get("Content-Disposition"))
	if fName, ok := params["filename"]; ok && err == nil {
		return SanitizeFileName(fName)
	}
	if r.Request.URL.RawQuery != "" {
		return SanitizeFileName(fmt.Sprintf("%s_%s", r.Request.URL.Path, r.Request.URL.RawQuery))
	}
	return SanitizeFileName(strings.TrimPrefix(r.Request.URL.Path, "/"))
}

func (r *Response) fixCharset(detectCharset bool, defaultEncoding string) error {
	if len(r.Body) == 0 {
		return nil
	}
	if defaultEncoding != "" {
		tmpBody, err := encodeBytes(r.Body, "text/plain; charset="+defaultEncoding)
		if err != nil {
			return err
		}
		r.Body = tmpBody
		return nil
	}
	contentType := strings.ToLower(r.Headers.Get("Content-Type"))

	if strings.Contains(contentType, "image/") ||
		strings.Contains(contentType, "video/") ||
		strings.Contains(contentType, "audio/") ||
		strings.Contains(contentType, "font/") {
		// These MIME types should not have textual data.

		return nil
	}

	if !strings.Contains(contentType, "charset") {
		if !detectCharset {
			return nil
		}
		d := chardet.NewTextDetector()
		r, err := d.DetectBest(r.Body)
		if err != nil {
			return err
		}
		contentType = "text/plain; charset=" + r.Charset
	}
	if strings.Contains(contentType, "utf-8") || strings.Contains(contentType, "utf8") {
		return nil
	}
	tmpBody, err := encodeBytes(r.Body, contentType)
	if err != nil {
		return err
	}
	r.Body = tmpBody
	return nil
}

func encodeBytes(b []byte, contentType string) ([]byte, error) {
	r, err := charset.NewReader(bytes.NewReader(b), contentType)
	if err != nil {
		return nil, err
	}
	return io.ReadAll(r)
}
```

## File: `unmarshal.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package colly

import (
	"errors"
	"reflect"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

// Unmarshal is a shorthand for colly.UnmarshalHTML
func (h *HTMLElement) Unmarshal(v interface{}) error {
	return UnmarshalHTML(v, h.DOM, nil)
}

// UnmarshalWithMap is a shorthand for colly.UnmarshalHTML, extended to allow maps to be passed in.
func (h *HTMLElement) UnmarshalWithMap(v interface{}, structMap map[string]string) error {
	return UnmarshalHTML(v, h.DOM, structMap)
}

// UnmarshalHTML declaratively extracts text or attributes to a struct from
// HTML response using struct tags composed of css selectors.
// Allowed struct tags:
//   - "selector" (required): CSS (goquery) selector of the desired data
//   - "attr" (optional): Selects the matching element's attribute's value.
//     Leave it blank or omit to get the text of the element.
//
// Example struct declaration:
//
//	type Nested struct {
//		String  string   `selector:"div > p"`
//	   Classes []string `selector:"li" attr:"class"`
//		Struct  *Nested  `selector:"div > div"`
//	}
//
// Supported types: struct, *struct, string, []string
func UnmarshalHTML(v interface{}, s *goquery.Selection, structMap map[string]string) error {
	rv := reflect.ValueOf(v)

	if rv.Kind() != reflect.Ptr || rv.IsNil() {
		return errors.New("Invalid type or nil-pointer")
	}

	sv := rv.Elem()
	st := reflect.TypeOf(v).Elem()
	if structMap != nil {
		for k, v := range structMap {
			attrV := sv.FieldByName(k)
			if !attrV.CanAddr() || !attrV.CanSet() {
				continue
			}
			if err := unmarshalSelector(s, attrV, v); err != nil {
				return err
			}
		}
	} else {
		for i := 0; i < sv.NumField(); i++ {
			attrV := sv.Field(i)
			if !attrV.CanAddr() || !attrV.CanSet() {
				continue
			}
			if err := unmarshalAttr(s, attrV, st.Field(i)); err != nil {
				return err
			}

		}
	}

	return nil
}

func unmarshalSelector(s *goquery.Selection, attrV reflect.Value, selector string) error {
	//selector is "-" specify that field should ignore.
	if selector == "-" {
		return nil
	}
	htmlAttr := ""
	// TODO support more types
	switch attrV.Kind() {
	case reflect.Slice:
		if err := unmarshalSlice(s, selector, htmlAttr, attrV); err != nil {
			return err
		}
	case reflect.String:
		var val string
		if selector == "" && htmlAttr != "" {
			val = getDOMValue(s, htmlAttr)
		} else {
			val = getDOMValue(s.Find(selector), htmlAttr)
		}
		attrV.Set(reflect.Indirect(reflect.ValueOf(val)))
	case reflect.Struct:
		if err := unmarshalStruct(s, selector, attrV); err != nil {
			return err
		}
	case reflect.Ptr:
		if err := unmarshalPtr(s, selector, attrV); err != nil {
			return err
		}
	default:
		return errors.New("Invalid type: " + attrV.String())
	}
	return nil
}

func unmarshalAttr(s *goquery.Selection, attrV reflect.Value, attrT reflect.StructField) error {
	selector := attrT.Tag.Get("selector")
	//selector is "-" specify that field should ignore.
	if selector == "-" {
		return nil
	}
	htmlAttr := attrT.Tag.Get("attr")
	// TODO support more types
	switch attrV.Kind() {
	case reflect.Slice:
		if err := unmarshalSlice(s, selector, htmlAttr, attrV); err != nil {
			return err
		}
	case reflect.String:
		val := getDOMValue(s.Find(selector), htmlAttr)
		attrV.Set(reflect.Indirect(reflect.ValueOf(val)))
	case reflect.Struct:
		if err := unmarshalStruct(s, selector, attrV); err != nil {
			return err
		}
	case reflect.Ptr:
		if err := unmarshalPtr(s, selector, attrV); err != nil {
			return err
		}
	default:
		return errors.New("Invalid type: " + attrV.String())
	}
	return nil
}

func unmarshalStruct(s *goquery.Selection, selector string, attrV reflect.Value) error {
	newS := s
	if selector != "" {
		newS = newS.Find(selector)
	}
	if newS.Nodes == nil {
		return nil
	}
	v := reflect.New(attrV.Type())
	err := UnmarshalHTML(v.Interface(), newS, nil)
	if err != nil {
		return err
	}
	attrV.Set(reflect.Indirect(v))
	return nil
}

func unmarshalPtr(s *goquery.Selection, selector string, attrV reflect.Value) error {
	newS := s
	if selector != "" {
		newS = newS.Find(selector)
	}
	if newS.Nodes == nil {
		return nil
	}
	e := attrV.Type().Elem()
	if e.Kind() != reflect.Struct {
		return errors.New("Invalid slice type")
	}
	v := reflect.New(e)
	err := UnmarshalHTML(v.Interface(), newS, nil)
	if err != nil {
		return err
	}
	attrV.Set(v)
	return nil
}

func unmarshalSlice(s *goquery.Selection, selector, htmlAttr string, attrV reflect.Value) error {
	if attrV.Pointer() == 0 {
		v := reflect.MakeSlice(attrV.Type(), 0, 0)
		attrV.Set(v)
	}
	switch attrV.Type().Elem().Kind() {
	case reflect.String:
		s.Find(selector).Each(func(_ int, s *goquery.Selection) {
			val := getDOMValue(s, htmlAttr)
			attrV.Set(reflect.Append(attrV, reflect.Indirect(reflect.ValueOf(val))))
		})
	case reflect.Ptr:
		s.Find(selector).Each(func(_ int, innerSel *goquery.Selection) {
			someVal := reflect.New(attrV.Type().Elem().Elem())
			UnmarshalHTML(someVal.Interface(), innerSel, nil)
			attrV.Set(reflect.Append(attrV, someVal))
		})
	case reflect.Struct:
		s.Find(selector).Each(func(_ int, innerSel *goquery.Selection) {
			someVal := reflect.New(attrV.Type().Elem())
			UnmarshalHTML(someVal.Interface(), innerSel, nil)
			attrV.Set(reflect.Append(attrV, reflect.Indirect(someVal)))
		})
	default:
		return errors.New("Invalid slice type")
	}
	return nil
}

func getDOMValue(s *goquery.Selection, attr string) string {
	if attr == "" {
		return strings.TrimSpace(s.First().Text())
	}
	attrV, _ := s.Attr(attr)
	return attrV
}
```

## File: `unmarshal_test.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package colly

import (
	"bytes"
	"testing"

	"github.com/PuerkitoBio/goquery"
)

var basicTestData = []byte(`<ul><li class="x">list <span>item</span> 1</li><li>list item 2</li><li>3</li></ul>`)
var nestedTestData = []byte(`<div><p>a</p><div><p>b</p><div><p>c</p></div></div></div>`)
var pointerSliceTestData = []byte(`<ul class="object"><li class="info">Information: <span>Info 1</span></li><li class="info">Information: <span>Info 2</span></li></ul>`)

func TestBasicUnmarshal(t *testing.T) {
	doc, _ := goquery.NewDocumentFromReader(bytes.NewBuffer(basicTestData))
	e := &HTMLElement{
		DOM: doc.First(),
	}
	s := struct {
		String string   `selector:"li:first-child" attr:"class"`
		Items  []string `selector:"li"`
		Struct struct {
			String string `selector:"li:last-child"`
		}
	}{}
	if err := e.Unmarshal(&s); err != nil {
		t.Error("Cannot unmarshal struct: " + err.Error())
	}
	if s.String != "x" {
		t.Errorf(`Invalid data for String: %q, expected "x"`, s.String)
	}
	if s.Struct.String != "3" {
		t.Errorf(`Invalid data for Struct.String: %q, expected "3"`, s.Struct.String)
	}
}

func TestNestedUnmarshalMap(t *testing.T) {
	doc, _ := goquery.NewDocumentFromReader(bytes.NewBuffer(nestedTestData))
	e := &HTMLElement{
		DOM: doc.First(),
	}
	doc2, _ := goquery.NewDocumentFromReader(bytes.NewBuffer(basicTestData))
	e2 := &HTMLElement{
		DOM: doc2.First(),
	}
	type nested struct {
		String string
	}
	mapSelector := make(map[string]string)
	mapSelector["String"] = "div > p"

	mapSelector2 := make(map[string]string)
	mapSelector2["String"] = "span"

	s := nested{}
	s2 := nested{}
	if err := e.UnmarshalWithMap(&s, mapSelector); err != nil {
		t.Error("Cannot unmarshal struct: " + err.Error())
	}
	if err := e2.UnmarshalWithMap(&s2, mapSelector2); err != nil {
		t.Error("Cannot unmarshal struct: " + err.Error())
	}
	if s.String != "a" {
		t.Errorf(`Invalid data for String: %q, expected "a"`, s.String)
	}
	if s2.String != "item" {
		t.Errorf(`Invalid data for String: %q, expected "a"`, s.String)
	}
}

func TestNestedUnmarshal(t *testing.T) {
	doc, _ := goquery.NewDocumentFromReader(bytes.NewBuffer(nestedTestData))
	e := &HTMLElement{
		DOM: doc.First(),
	}
	type nested struct {
		String string  `selector:"div > p"`
		Struct *nested `selector:"div > div"`
	}
	s := nested{}
	if err := e.Unmarshal(&s); err != nil {
		t.Error("Cannot unmarshal struct: " + err.Error())
	}
	if s.String != "a" {
		t.Errorf(`Invalid data for String: %q, expected "a"`, s.String)
	}
	if s.Struct.String != "b" {
		t.Errorf(`Invalid data for Struct.String: %q, expected "b"`, s.Struct.String)
	}
	if s.Struct.Struct.String != "c" {
		t.Errorf(`Invalid data for Struct.Struct.String: %q, expected "c"`, s.Struct.Struct.String)
	}
}

func TestPointerSliceUnmarshall(t *testing.T) {
	type info struct {
		Text string `selector:"span"`
	}
	type object struct {
		Info []*info `selector:"li.info"`
	}

	doc, _ := goquery.NewDocumentFromReader(bytes.NewBuffer(pointerSliceTestData))
	e := HTMLElement{DOM: doc.First()}
	o := object{}
	err := e.Unmarshal(&o)
	if err != nil {
		t.Fatalf("Failed to unmarshal page: %s\n", err.Error())
	}

	if len(o.Info) != 2 {
		t.Errorf("Invalid length for Info: %d, expected 2", len(o.Info))
	}
	if o.Info[0].Text != "Info 1" {
		t.Errorf("Invalid data for Info.[0].Text: %s, expected Info 1", o.Info[0].Text)
	}
	if o.Info[1].Text != "Info 2" {
		t.Errorf("Invalid data for Info.[1].Text: %s, expected Info 2", o.Info[1].Text)
	}

}

func TestStructSliceUnmarshall(t *testing.T) {
	type info struct {
		Text string `selector:"span"`
	}
	type object struct {
		Info []info `selector:"li.info"`
	}

	doc, _ := goquery.NewDocumentFromReader(bytes.NewBuffer(pointerSliceTestData))
	e := HTMLElement{DOM: doc.First()}
	o := object{}
	err := e.Unmarshal(&o)
	if err != nil {
		t.Fatalf("Failed to unmarshal page: %s\n", err.Error())
	}

	if len(o.Info) != 2 {
		t.Errorf("Invalid length for Info: %d, expected 2", len(o.Info))
	}
	if o.Info[0].Text != "Info 1" {
		t.Errorf("Invalid data for Info.[0].Text: %s, expected Info 1", o.Info[0].Text)
	}
	if o.Info[1].Text != "Info 2" {
		t.Errorf("Invalid data for Info.[1].Text: %s, expected Info 2", o.Info[1].Text)
	}

}
```

## File: `VERSION`
```
2.1.0
```

## File: `xmlelement.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package colly

import (
	"strings"

	"github.com/antchfx/htmlquery"
	"github.com/antchfx/xmlquery"
	"golang.org/x/net/html"
)

// XMLElement is the representation of a XML tag.
type XMLElement struct {
	// Name is the name of the tag
	Name       string
	Text       string
	attributes interface{}
	// Request is the request object of the element's HTML document
	Request *Request
	// Response is the Response object of the element's HTML document
	Response *Response
	// DOM is the DOM object of the page. DOM is relative
	// to the current XMLElement and is either a html.Node or xmlquery.Node
	// based on how the XMLElement was created.
	DOM    interface{}
	isHTML bool
	// Index stores the position of the current element within all the elements matched by an OnXML callback
	Index int
}

// NewXMLElementFromHTMLNode creates a XMLElement from a html.Node.
func NewXMLElementFromHTMLNode(resp *Response, s *html.Node) *XMLElement {
	return &XMLElement{
		Name:       s.Data,
		Request:    resp.Request,
		Response:   resp,
		Text:       htmlquery.InnerText(s),
		DOM:        s,
		attributes: s.Attr,
		isHTML:     true,
	}
}

// NewXMLElementFromXMLNode creates a XMLElement from a xmlquery.Node.
func NewXMLElementFromXMLNode(resp *Response, s *xmlquery.Node) *XMLElement {
	return &XMLElement{
		Name:       s.Data,
		Request:    resp.Request,
		Response:   resp,
		Text:       s.InnerText(),
		DOM:        s,
		attributes: s.Attr,
		isHTML:     false,
	}
}

// Attr returns the selected attribute of a HTMLElement or empty string
// if no attribute found
func (h *XMLElement) Attr(k string) string {
	if h.isHTML {
		for _, a := range h.attributes.([]html.Attribute) {
			if a.Key == k {
				return a.Val
			}
		}
	} else {
		for _, a := range h.attributes.([]xmlquery.Attr) {
			if a.Name.Local == k {
				return a.Value
			}
		}
	}
	return ""
}

// ChildText returns the concatenated and stripped text content of the matching
// elements.
func (h *XMLElement) ChildText(xpathQuery string) string {
	if h.isHTML {
		child := htmlquery.FindOne(h.DOM.(*html.Node), xpathQuery)
		if child == nil {
			return ""
		}
		return strings.TrimSpace(htmlquery.InnerText(child))
	}
	child := xmlquery.FindOne(h.DOM.(*xmlquery.Node), xpathQuery)
	if child == nil {
		return ""
	}
	return strings.TrimSpace(child.InnerText())

}

// ChildAttr returns the stripped text content of the first matching
// element's attribute.
func (h *XMLElement) ChildAttr(xpathQuery, attrName string) string {
	if h.isHTML {
		child := htmlquery.FindOne(h.DOM.(*html.Node), xpathQuery)
		if child != nil {
			for _, attr := range child.Attr {
				if attr.Key == attrName {
					return strings.TrimSpace(attr.Val)
				}
			}
		}
	} else {
		child := xmlquery.FindOne(h.DOM.(*xmlquery.Node), xpathQuery)
		if child != nil {
			for _, attr := range child.Attr {
				if attr.Name.Local == attrName {
					return strings.TrimSpace(attr.Value)
				}
			}
		}
	}

	return ""
}

// ChildAttrs returns the stripped text content of all the matching
// element's attributes.
func (h *XMLElement) ChildAttrs(xpathQuery, attrName string) []string {
	var res []string
	if h.isHTML {
		for _, child := range htmlquery.Find(h.DOM.(*html.Node), xpathQuery) {
			for _, attr := range child.Attr {
				if attr.Key == attrName {
					res = append(res, strings.TrimSpace(attr.Val))
				}
			}
		}
	} else {
		xmlquery.FindEach(h.DOM.(*xmlquery.Node), xpathQuery, func(i int, child *xmlquery.Node) {
			for _, attr := range child.Attr {
				if attr.Name.Local == attrName {
					res = append(res, strings.TrimSpace(attr.Value))
				}
			}
		})
	}
	return res
}

// ChildTexts returns an array of strings corresponding to child elements that match the xpath query.
// Each item in the array is the stripped text content of the corresponding matching child element.
func (h *XMLElement) ChildTexts(xpathQuery string) []string {
	texts := make([]string, 0)
	if h.isHTML {
		for _, child := range htmlquery.Find(h.DOM.(*html.Node), xpathQuery) {
			texts = append(texts, strings.TrimSpace(htmlquery.InnerText(child)))
		}
	} else {
		xmlquery.FindEach(h.DOM.(*xmlquery.Node), xpathQuery, func(i int, child *xmlquery.Node) {
			texts = append(texts, strings.TrimSpace(child.InnerText()))
		})
	}
	return texts
}
```

## File: `xmlelement_test.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package colly_test

import (
	"github.com/antchfx/htmlquery"
	"github.com/gocolly/colly/v2"
	"reflect"
	"strings"
	"testing"
)

// Borrowed from http://infohost.nmt.edu/tcc/help/pubs/xhtml/example.html
// Added attributes to the `<li>` tags for testing purposes
const htmlPage = `
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
 "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
  <head>
    <title>Your page title here</title>
  </head>
  <body>
    <h1>Your major heading here</h1>
    <p>
      This is a regular text paragraph.
    </p>
    <ul>
      <li class="list-item-1">
        First bullet of a bullet list.
      </li>
      <li class="list-item-2">
        This is the <em>second</em> bullet.
      </li>
    </ul>
  </body>
</html>
`

func TestAttr(t *testing.T) {
	resp := &colly.Response{StatusCode: 200, Body: []byte(htmlPage)}
	doc, _ := htmlquery.Parse(strings.NewReader(htmlPage))
	xmlNode := htmlquery.FindOne(doc, "/html")
	xmlElem := colly.NewXMLElementFromHTMLNode(resp, xmlNode)

	if xmlElem.Attr("xmlns") != "http://www.w3.org/1999/xhtml" {
		t.Fatalf("failed xmlns attribute test: %v != http://www.w3.org/1999/xhtml", xmlElem.Attr("xmlns"))
	}

	if xmlElem.Attr("xml:lang") != "en" {
		t.Fatalf("failed lang attribute test: %v != en", xmlElem.Attr("lang"))
	}
}

func TestChildText(t *testing.T) {
	resp := &colly.Response{StatusCode: 200, Body: []byte(htmlPage)}
	doc, _ := htmlquery.Parse(strings.NewReader(htmlPage))
	xmlNode := htmlquery.FindOne(doc, "/html")
	xmlElem := colly.NewXMLElementFromHTMLNode(resp, xmlNode)

	if text := xmlElem.ChildText("//p"); text != "This is a regular text paragraph." {
		t.Fatalf("failed child tag test: %v != This is a regular text paragraph.", text)
	}
	if text := xmlElem.ChildText("//dl"); text != "" {
		t.Fatalf("failed child tag test: %v != \"\"", text)
	}
}

func TestChildTexts(t *testing.T) {
	resp := &colly.Response{StatusCode: 200, Body: []byte(htmlPage)}
	doc, _ := htmlquery.Parse(strings.NewReader(htmlPage))
	xmlNode := htmlquery.FindOne(doc, "/html")
	xmlElem := colly.NewXMLElementFromHTMLNode(resp, xmlNode)
	expected := []string{"First bullet of a bullet list.", "This is the second bullet."}
	if texts := xmlElem.ChildTexts("//li"); reflect.DeepEqual(texts, expected) == false {
		t.Fatalf("failed child tags test: %v != %v", texts, expected)
	}
	if texts := xmlElem.ChildTexts("//dl"); reflect.DeepEqual(texts, make([]string, 0)) == false {
		t.Fatalf("failed child tag test: %v != \"\"", texts)
	}
}
func TestChildAttr(t *testing.T) {
	resp := &colly.Response{StatusCode: 200, Body: []byte(htmlPage)}
	doc, _ := htmlquery.Parse(strings.NewReader(htmlPage))
	xmlNode := htmlquery.FindOne(doc, "/html")
	xmlElem := colly.NewXMLElementFromHTMLNode(resp, xmlNode)

	if attr := xmlElem.ChildAttr("/body/ul/li[1]", "class"); attr != "list-item-1" {
		t.Fatalf("failed child attribute test: %v != list-item-1", attr)
	}
	if attr := xmlElem.ChildAttr("/body/ul/li[2]", "class"); attr != "list-item-2" {
		t.Fatalf("failed child attribute test: %v != list-item-2", attr)
	}
}

func TestChildAttrs(t *testing.T) {
	resp := &colly.Response{StatusCode: 200, Body: []byte(htmlPage)}
	doc, _ := htmlquery.Parse(strings.NewReader(htmlPage))
	xmlNode := htmlquery.FindOne(doc, "/html")
	xmlElem := colly.NewXMLElementFromHTMLNode(resp, xmlNode)

	attrs := xmlElem.ChildAttrs("/body/ul/li", "class")
	if len(attrs) != 2 {
		t.Fatalf("failed child attributes length test: %d != 2", len(attrs))
	}

	for _, attr := range attrs {
		if !(attr == "list-item-1" || attr == "list-item-2") {
			t.Fatalf("failed child attributes values test: %s != list-item-(1 or 2)", attr)
		}
	}
}
```

## File: `cmd/colly/colly.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"bytes"
	"fmt"
	"log"
	"os"
	"strings"

	"github.com/jawher/mow.cli"
)

var scraperHeadTemplate = `package main

import (
	"log"

	"github.com/gocolly/colly/v2"
)

func main() {
	c := colly.NewCollector()
`

var scraperEndTemplate = `
	c.Visit("https://yourdomain.com/")
}
`

var htmlCallbackTemplate = `
	c.OnHTML("element-selector", func(e *colly.HTMLElement) {
		log.Println(e.Text)
	})
`

var requestCallbackTemplate = `
	c.OnRequest(func(r *colly.Request) {
		log.Println("Visiting", r.URL)
	})
`

var responseCallbackTemplate = `
	c.OnResponse(func(r *colly.Response) {
		log.Println("Visited", r.Request.URL, r.StatusCode)
	})
`

var errorCallbackTemplate = `
	c.OnError(func(r *colly.Response, err error) {
		log.Printf("Error on %s: %s", r.Request.URL, err)
	})
`

func main() {
	app := cli.App("colly", "Scraping Framework for Gophers")

	app.Command("new", "Create new scraper", func(cmd *cli.Cmd) {
		var (
			callbacks = cmd.StringOpt("callbacks", "", "Add callbacks to the template. (E.g. '--callbacks=html,response,error')")
			hosts     = cmd.StringOpt("hosts", "", "Specify scraper's allowed hosts. (e.g. '--hosts=xy.com,abcd.com')")
			path      = cmd.StringArg("PATH", "", "Path of the new scraper")
		)

		cmd.Spec = "[--callbacks] [--hosts] [PATH]"

		cmd.Action = func() {
			scraper := bytes.NewBufferString(scraperHeadTemplate)
			outfile := os.Stdout
			if *path != "" {
				var err error
				outfile, err = os.Create(*path)
				if err != nil {
					log.Fatal(err)
				}
				defer outfile.Close()
			}
			if *hosts != "" {
				scraper.WriteString("\n	c.AllowedDomains = []string{")
				for i, h := range strings.Split(*hosts, ",") {
					if i > 0 {
						scraper.WriteString(", ")
					}
					scraper.WriteString(fmt.Sprintf("%q", h))
				}
				scraper.WriteString("}\n")
			}
			if len(*callbacks) > 0 {
				for _, c := range strings.Split(*callbacks, ",") {
					switch c {
					case "html":
						scraper.WriteString(htmlCallbackTemplate)
					case "request":
						scraper.WriteString(requestCallbackTemplate)
					case "response":
						scraper.WriteString(responseCallbackTemplate)
					case "error":
						scraper.WriteString(errorCallbackTemplate)
					}
				}
			}
			scraper.WriteString(scraperEndTemplate)
			outfile.Write(scraper.Bytes())
		}
	})

	app.Run(os.Args)
}
```

## File: `debug/debug.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package debug

// Event represents an action inside a collector
type Event struct {
	// Type is the type of the event
	Type string
	// RequestID identifies the HTTP request of the Event
	RequestID uint32
	// CollectorID identifies the collector of the Event
	CollectorID uint32
	// Values contains the event's key-value pairs. Different type of events
	// can return different key-value pairs
	Values map[string]string
}

// Debugger is an interface for different type of debugging backends
type Debugger interface {
	// Init initializes the backend
	Init() error
	// Event receives a new collector event.
	Event(e *Event)
}
```

## File: `debug/logdebugger.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package debug

import (
	"io"
	"log"
	"os"
	"sync/atomic"
	"time"
)

// LogDebugger is the simplest debugger which prints log messages to the STDERR
type LogDebugger struct {
	// Output is the log destination, anything can be used which implements them
	// io.Writer interface. Leave it blank to use STDERR
	Output io.Writer
	// Prefix appears at the beginning of each generated log line
	Prefix string
	// Flag defines the logging properties.
	Flag    int
	logger  *log.Logger
	counter int32
	start   time.Time
}

// Init initializes the LogDebugger
func (l *LogDebugger) Init() error {
	l.counter = 0
	l.start = time.Now()
	if l.Output == nil {
		l.Output = os.Stderr
	}
	l.logger = log.New(l.Output, l.Prefix, l.Flag)
	return nil
}

// Event receives Collector events and prints them to STDERR
func (l *LogDebugger) Event(e *Event) {
	i := atomic.AddInt32(&l.counter, 1)
	l.logger.Printf("[%06d] %d [%6d - %s] %q (%s)\n", i, e.CollectorID, e.RequestID, e.Type, e.Values, time.Since(l.start))
}
```

## File: `debug/webdebugger.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package debug

import (
	"encoding/json"
	"log"
	"net/http"
	"sync"
	"time"
)

// WebDebugger is a web based debugging frontend for colly
type WebDebugger struct {
	// Address is the address of the web server. It is 127.0.0.1:7676 by default.
	Address         string
	initialized     bool
	CurrentRequests map[uint32]requestInfo
	RequestLog      []requestInfo
	sync.Mutex
}

type requestInfo struct {
	URL            string
	Started        time.Time
	Duration       time.Duration
	ResponseStatus string
	ID             uint32
	CollectorID    uint32
}

// Init initializes the WebDebugger
func (w *WebDebugger) Init() error {
	if w.initialized {
		return nil
	}
	defer func() {
		w.initialized = true
	}()
	if w.Address == "" {
		w.Address = "127.0.0.1:7676"
	}
	w.RequestLog = make([]requestInfo, 0)
	w.CurrentRequests = make(map[uint32]requestInfo)
	http.HandleFunc("/", w.indexHandler)
	http.HandleFunc("/status", w.statusHandler)
	log.Println("Starting debug webserver on", w.Address)
	go http.ListenAndServe(w.Address, nil)
	return nil
}

// Event updates the debugger's status
func (w *WebDebugger) Event(e *Event) {
	w.Lock()
	defer w.Unlock()

	switch e.Type {
	case "request":
		w.CurrentRequests[e.RequestID] = requestInfo{
			URL:         e.Values["url"],
			Started:     time.Now(),
			ID:          e.RequestID,
			CollectorID: e.CollectorID,
		}
	case "response", "error":
		r := w.CurrentRequests[e.RequestID]
		r.Duration = time.Since(r.Started)
		r.ResponseStatus = e.Values["status"]
		w.RequestLog = append(w.RequestLog, r)
		delete(w.CurrentRequests, e.RequestID)
	}
}

func (w *WebDebugger) indexHandler(wr http.ResponseWriter, r *http.Request) {
	wr.Write([]byte(`<!DOCTYPE html>
<html>
<head>
 <title>Colly Debugger WebUI</title>
 <script src="https://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
 <link rel="stylesheet" type="text/css" href="https://semantic-ui.com/dist/semantic.min.css">
</head>
<body>
<div class="ui inverted vertical masthead center aligned segment" id="menu">
 <div class="ui tiny secondary inverted menu">
   <a class="item" href="/"><b>Colly WebDebugger</b></a>
 </div>
</div>
<div class="ui grid container">
 <div class="row">
  <div class="eight wide column">
   <h1>Current Requests <span id="current_request_count"></span></h1>
   <div id="current_requests" class="ui small feed"></div>
  </div>
  <div class="eight wide column">
   <h1>Finished Requests <span id="request_log_count"></span></h1>
   <div id="request_log" class="ui small feed"></div>
  </div>
 </div>
</div>
<script>
function curRequestTpl(url, started, collectorId) {
  return '<div class="event"><div class="content"><div class="summary">' + url + '</div><div class="meta">Collector #' + collectorId + ' - ' + started + "</div></div></div>";
}
function requestLogTpl(url, duration, collectorId) {
  return '<div class="event"><div class="content"><div class="summary">' + url + '</div><div class="meta">Collector #' + collectorId + ' - ' + (duration/1000000000) + "s</div></div></div>";
}
function fetchStatus() {
  $.getJSON("/status", function(data) {
    $("#current_requests").html("");
    $("#request_log").html("");
    $("#current_request_count").text('(' + Object.keys(data.CurrentRequests).length + ')');
    $("#request_log_count").text('(' + data.RequestLog.length + ')');
    for(var i in data.CurrentRequests) {
      var r = data.CurrentRequests[i];
      $("#current_requests").append(curRequestTpl(r.URL, r.Started, r.CollectorID));
    }
    for(var i in data.RequestLog.reverse()) {
      var r = data.RequestLog[i];
      $("#request_log").append(requestLogTpl(r.URL, r.Duration, r.CollectorID));
    }
    setTimeout(fetchStatus, 1000);
  });
}
$(document).ready(function() {
    fetchStatus();
});
</script>
</body>
</html>
`))
}

func (w *WebDebugger) statusHandler(wr http.ResponseWriter, r *http.Request) {
	w.Lock()
	jsonData, err := json.MarshalIndent(w, "", "  ")
	w.Unlock()
	if err != nil {
		panic(err)
	}
	wr.Write(jsonData)
}
```

## File: `extensions/extensions.go`
```go
// Package extensions implements various helper addons for Colly
package extensions
```

## File: `extensions/random_user_agent.go`
```go
package extensions

import (
	"fmt"
	"math/rand"
	"strings"

	"github.com/gocolly/colly/v2"
)

var uaGens = []func() string{
	genFirefoxUA,
	genChromeUA,
	genEdgeUA,
	genOperaUA,
}

var uaGensMobile = []func() string{
	genMobilePixel7UA,
	genMobilePixel6UA,
	genMobilePixel5UA,
	genMobilePixel4UA,
	genMobileNexus10UA,
}

// RandomUserAgent generates a random DESKTOP browser user-agent on every requests
func RandomUserAgent(c *colly.Collector) {
	c.OnRequest(func(r *colly.Request) {
		r.Headers.Set("User-Agent", uaGens[rand.Intn(len(uaGens))]())
	})
}

// RandomMobileUserAgent generates a random MOBILE browser user-agent on every requests
func RandomMobileUserAgent(c *colly.Collector) {
	c.OnRequest(func(r *colly.Request) {
		r.Headers.Set("User-Agent", uaGensMobile[rand.Intn(len(uaGensMobile))]())
	})
}

var ffVersions = []float32{
	// NOTE: Only version released after Jun 1, 2022 will be listed.
	// Data source: https://en.wikipedia.org/wiki/Firefox_version_history

	// 2022
	102.0,
	103.0,
	104.0,
	105.0,
	106.0,
	107.0,
	108.0,

	// 2023
	109.0,
	110.0,
	111.0,
	112.0,
	113.0,
}

var chromeVersions = []string{
	// NOTE: Only version released after Jun 1, 2022 will be listed.
	// Data source: https://chromereleases.googleblog.com/search/label/Stable%20updates

	// https://chromereleases.googleblog.com/2022/06/stable-channel-update-for-desktop.html
	"102.0.5005.115",

	// https://chromereleases.googleblog.com/2022/06/stable-channel-update-for-desktop_21.html
	"103.0.5060.53",

	// https://chromereleases.googleblog.com/2022/06/stable-channel-update-for-desktop_27.html
	"103.0.5060.66",

	// https://chromereleases.googleblog.com/2022/07/stable-channel-update-for-desktop.html
	"103.0.5060.114",

	// https://chromereleases.googleblog.com/2022/07/stable-channel-update-for-desktop_19.html
	"103.0.5060.134",

	// https://chromereleases.googleblog.com/2022/08/stable-channel-update-for-desktop.html
	"104.0.5112.79",
	"104.0.5112.80",
	"104.0.5112.81",

	// https://chromereleases.googleblog.com/2022/08/stable-channel-update-for-desktop_16.html
	"104.0.5112.101",
	"104.0.5112.102",

	// https://chromereleases.googleblog.com/2022/08/stable-channel-update-for-desktop_30.html
	"105.0.5195.52",
	"105.0.5195.53",
	"105.0.5195.54",

	// https://chromereleases.googleblog.com/2022/09/stable-channel-update-for-desktop.html
	"105.0.5195.102",

	// https://chromereleases.googleblog.com/2022/09/stable-channel-update-for-desktop_14.html
	"105.0.5195.125",
	"105.0.5195.126",
	"105.0.5195.127",

	// https://chromereleases.googleblog.com/2022/09/stable-channel-update-for-desktop_27.html
	"106.0.5249.61",
	"106.0.5249.62",

	// https://chromereleases.googleblog.com/2022/09/stable-channel-update-for-desktop_30.html
	"106.0.5249.91",

	// https://chromereleases.googleblog.com/2022/10/stable-channel-update-for-desktop.html
	"106.0.5249.103",

	// https://chromereleases.googleblog.com/2022/10/stable-channel-update-for-desktop_11.html
	"106.0.5249.119",

	// https://chromereleases.googleblog.com/2022/10/stable-channel-update-for-desktop_25.html
	"107.0.5304.62",
	"107.0.5304.63",
	"107.0.5304.68",

	// https://chromereleases.googleblog.com/2022/10/stable-channel-update-for-desktop_27.html
	"107.0.5304.87",
	"107.0.5304.88",

	// https://chromereleases.googleblog.com/2022/11/stable-channel-update-for-desktop.html
	"107.0.5304.106",
	"107.0.5304.107",
	"107.0.5304.110",

	// https://chromereleases.googleblog.com/2022/11/stable-channel-update-for-desktop_24.html
	"107.0.5304.121",
	"107.0.5304.122",

	// https://chromereleases.googleblog.com/2022/11/stable-channel-update-for-desktop_29.html
	"108.0.5359.71",
	"108.0.5359.72",

	// https://chromereleases.googleblog.com/2022/12/stable-channel-update-for-desktop.html
	"108.0.5359.94",
	"108.0.5359.95",

	// https://chromereleases.googleblog.com/2022/12/stable-channel-update-for-desktop_7.html
	"108.0.5359.98",
	"108.0.5359.99",

	// https://chromereleases.googleblog.com/2022/12/stable-channel-update-for-desktop_13.html
	"108.0.5359.124",
	"108.0.5359.125",

	// https://chromereleases.googleblog.com/2023/01/stable-channel-update-for-desktop.html
	"109.0.5414.74",
	"109.0.5414.75",
	"109.0.5414.87",

	// https://chromereleases.googleblog.com/2023/01/stable-channel-update-for-desktop_24.html
	"109.0.5414.119",
	"109.0.5414.120",

	// https://chromereleases.googleblog.com/2023/02/stable-channel-update-for-desktop.html
	"110.0.5481.77",
	"110.0.5481.78",

	// https://chromereleases.googleblog.com/2023/02/stable-channel-desktop-update.html
	"110.0.5481.96",
	"110.0.5481.97",

	// https://chromereleases.googleblog.com/2023/02/stable-channel-desktop-update_14.html
	"110.0.5481.100",

	// https://chromereleases.googleblog.com/2023/02/stable-channel-desktop-update_16.html
	"110.0.5481.104",

	// https://chromereleases.googleblog.com/2023/02/stable-channel-desktop-update_22.html
	"110.0.5481.177",
	"110.0.5481.178",

	// https://chromereleases.googleblog.com/2023/02/stable-channel-desktop-update_97.html
	"109.0.5414.129",

	// https://chromereleases.googleblog.com/2023/03/stable-channel-update-for-desktop.html
	"111.0.5563.64",
	"111.0.5563.65",

	// https://chromereleases.googleblog.com/2023/03/stable-channel-update-for-desktop_21.html
	"111.0.5563.110",
	"111.0.5563.111",

	// https://chromereleases.googleblog.com/2023/03/stable-channel-update-for-desktop_27.html
	"111.0.5563.146",
	"111.0.5563.147",

	// https://chromereleases.googleblog.com/2023/04/stable-channel-update-for-desktop.html
	"112.0.5615.49",
	"112.0.5615.50",

	// https://chromereleases.googleblog.com/2023/04/stable-channel-update-for-desktop_12.html
	"112.0.5615.86",
	"112.0.5615.87",

	// https://chromereleases.googleblog.com/2023/04/stable-channel-update-for-desktop_14.html
	"112.0.5615.121",

	// https://chromereleases.googleblog.com/2023/04/stable-channel-update-for-desktop_18.html
	"112.0.5615.137",
	"112.0.5615.138",
	"112.0.5615.165",

	// https://chromereleases.googleblog.com/2023/05/stable-channel-update-for-desktop.html
	"113.0.5672.63",
	"113.0.5672.64",

	// https://chromereleases.googleblog.com/2023/05/stable-channel-update-for-desktop_8.html
	"113.0.5672.92",
	"113.0.5672.93",
}

var edgeVersions = []string{
	// NOTE: Only version released after Jun 1, 2022 will be listed.
	// Data source: https://learn.microsoft.com/en-us/deployedge/microsoft-edge-release-schedule

	// 2022
	"103.0.0.0,103.0.1264.37",
	"104.0.0.0,104.0.1293.47",
	"105.0.0.0,105.0.1343.25",
	"106.0.0.0,106.0.1370.34",
	"107.0.0.0,107.0.1418.24",
	"108.0.0.0,108.0.1462.42",

	// 2023
	"109.0.0.0,109.0.1518.49",
	"110.0.0.0,110.0.1587.41",
	"111.0.0.0,111.0.1661.41",
	"112.0.0.0,112.0.1722.34",
	"113.0.0.0,113.0.1774.3",
}

var operaVersions = []string{
	// NOTE: Only version released after Jan 1, 2023 will be listed.
	// Data source: https://blogs.opera.com/desktop/

	// https://blogs.opera.com/desktop/changelog-for-96/
	"110.0.5449.0,96.0.4640.0",
	"110.0.5464.2,96.0.4653.0",
	"110.0.5464.2,96.0.4660.0",
	"110.0.5481.30,96.0.4674.0",
	"110.0.5481.30,96.0.4691.0",
	"110.0.5481.30,96.0.4693.12",
	"110.0.5481.77,96.0.4693.16",
	"110.0.5481.100,96.0.4693.20",
	"110.0.5481.178,96.0.4693.31",
	"110.0.5481.178,96.0.4693.50",
	"110.0.5481.192,96.0.4693.80",

	// https://blogs.opera.com/desktop/changelog-for-97/
	"111.0.5532.2,97.0.4711.0",
	"111.0.5532.2,97.0.4704.0",
	"111.0.5532.2,97.0.4697.0",
	"111.0.5562.0,97.0.4718.0",
	"111.0.5563.19,97.0.4719.4",
	"111.0.5563.19,97.0.4719.11",
	"111.0.5563.41,97.0.4719.17",
	"111.0.5563.65,97.0.4719.26",
	"111.0.5563.65,97.0.4719.28",
	"111.0.5563.111,97.0.4719.43",
	"111.0.5563.147,97.0.4719.63",
	"111.0.5563.147,97.0.4719.83",

	// https://blogs.opera.com/desktop/changelog-for-98/
	"112.0.5596.2,98.0.4756.0",
	"112.0.5596.2,98.0.4746.0",
	"112.0.5615.20,98.0.4759.1",
	"112.0.5615.50,98.0.4759.3",
	"112.0.5615.87,98.0.4759.6",
	"112.0.5615.165,98.0.4759.15",
	"112.0.5615.165,98.0.4759.21",
	"112.0.5615.165,98.0.4759.39",
}

var pixel7AndroidVersions = []string{
	// Data source:
	// - https://developer.android.com/about/versions
	// - https://source.android.com/brain/knowledge/docs_legacy/setup/about/build-numbers#source-code-tags-and-builds
	"13",
}

var pixel6AndroidVersions = []string{
	// Data source:
	// - https://developer.android.com/about/versions
	// - https://source.android.com/brain/knowledge/docs_legacy/setup/about/build-numbers#source-code-tags-and-builds
	"12",
	"13",
}

var pixel5AndroidVersions = []string{
	// Data source:
	// - https://developer.android.com/about/versions
	// - https://source.android.com/brain/knowledge/docs_legacy/setup/about/build-numbers#source-code-tags-and-builds
	"11",
	"12",
	"13",
}

var pixel4AndroidVersions = []string{
	// Data source:
	// - https://developer.android.com/about/versions
	// - https://source.android.com/brain/knowledge/docs_legacy/setup/about/build-numbers#source-code-tags-and-builds
	"10",
	"11",
	"12",
	"13",
}

var nexus10AndroidVersions = []string{
	// Data source:
	// - https://developer.android.com/about/versions
	// - https://source.android.com/brain/knowledge/docs_legacy/setup/about/build-numbers#source-code-tags-and-builds
	"4.4.2",
	"4.4.4",
	"5.0",
	"5.0.1",
	"5.0.2",
	"5.1",
	"5.1.1",
}

var nexus10Builds = []string{
	// Data source: https://source.android.com/brain/knowledge/docs_legacy/setup/about/build-numbers#source-code-tags-and-builds

	"LMY49M", // android-5.1.1_r38 (Lollipop)
	"LMY49J", // android-5.1.1_r37 (Lollipop)
	"LMY49I", // android-5.1.1_r36 (Lollipop)
	"LMY49H", // android-5.1.1_r35 (Lollipop)
	"LMY49G", // android-5.1.1_r34 (Lollipop)
	"LMY49F", // android-5.1.1_r33 (Lollipop)
	"LMY48Z", // android-5.1.1_r30 (Lollipop)
	"LMY48X", // android-5.1.1_r25 (Lollipop)
	"LMY48T", // android-5.1.1_r19 (Lollipop)
	"LMY48M", // android-5.1.1_r14 (Lollipop)
	"LMY48I", // android-5.1.1_r9 (Lollipop)
	"LMY47V", // android-5.1.1_r1 (Lollipop)
	"LMY47D", // android-5.1.0_r1 (Lollipop)
	"LRX22G", // android-5.0.2_r1 (Lollipop)
	"LRX22C", // android-5.0.1_r1 (Lollipop)
	"LRX21P", // android-5.0.0_r4.0.1 (Lollipop)
	"KTU84P", // android-4.4.4_r1 (KitKat)
	"KTU84L", // android-4.4.3_r1 (KitKat)
	"KOT49H", // android-4.4.2_r1 (KitKat)
	"KOT49E", // android-4.4.1_r1 (KitKat)
	"KRT16S", // android-4.4_r1.2 (KitKat)
	"JWR66Y", // android-4.3_r1.1 (Jelly Bean)
	"JWR66V", // android-4.3_r1 (Jelly Bean)
	"JWR66N", // android-4.3_r0.9.1 (Jelly Bean)
	"JDQ39 ", // android-4.2.2_r1 (Jelly Bean)
	"JOP40F", // android-4.2.1_r1.1 (Jelly Bean)
	"JOP40D", // android-4.2.1_r1 (Jelly Bean)
	"JOP40C", // android-4.2_r1 (Jelly Bean)
}

var osStrings = []string{
	// MacOS - High Sierra
	"Macintosh; Intel Mac OS X 10_13",
	"Macintosh; Intel Mac OS X 10_13_1",
	"Macintosh; Intel Mac OS X 10_13_2",
	"Macintosh; Intel Mac OS X 10_13_3",
	"Macintosh; Intel Mac OS X 10_13_4",
	"Macintosh; Intel Mac OS X 10_13_5",
	"Macintosh; Intel Mac OS X 10_13_6",

	// MacOS - Mojave
	"Macintosh; Intel Mac OS X 10_14",
	"Macintosh; Intel Mac OS X 10_14_1",
	"Macintosh; Intel Mac OS X 10_14_2",
	"Macintosh; Intel Mac OS X 10_14_3",
	"Macintosh; Intel Mac OS X 10_14_4",
	"Macintosh; Intel Mac OS X 10_14_5",
	"Macintosh; Intel Mac OS X 10_14_6",

	// MacOS - Catalina
	"Macintosh; Intel Mac OS X 10_15",
	"Macintosh; Intel Mac OS X 10_15_1",
	"Macintosh; Intel Mac OS X 10_15_2",
	"Macintosh; Intel Mac OS X 10_15_3",
	"Macintosh; Intel Mac OS X 10_15_4",
	"Macintosh; Intel Mac OS X 10_15_5",
	"Macintosh; Intel Mac OS X 10_15_6",
	"Macintosh; Intel Mac OS X 10_15_7",

	// MacOS - Big Sur
	"Macintosh; Intel Mac OS X 11_0",
	"Macintosh; Intel Mac OS X 11_0_1",
	"Macintosh; Intel Mac OS X 11_1",
	"Macintosh; Intel Mac OS X 11_2",
	"Macintosh; Intel Mac OS X 11_2_1",
	"Macintosh; Intel Mac OS X 11_2_2",
	"Macintosh; Intel Mac OS X 11_2_3",
	"Macintosh; Intel Mac OS X 11_3",
	"Macintosh; Intel Mac OS X 11_3_1",
	"Macintosh; Intel Mac OS X 11_4",
	"Macintosh; Intel Mac OS X 11_5",
	"Macintosh; Intel Mac OS X 11_5_1",
	"Macintosh; Intel Mac OS X 11_5_2",
	"Macintosh; Intel Mac OS X 11_6",
	"Macintosh; Intel Mac OS X 11_6_1",
	"Macintosh; Intel Mac OS X 11_6_2",
	"Macintosh; Intel Mac OS X 11_6_3",
	"Macintosh; Intel Mac OS X 11_6_4",
	"Macintosh; Intel Mac OS X 11_6_5",
	"Macintosh; Intel Mac OS X 11_6_6",
	"Macintosh; Intel Mac OS X 11_6_7",
	"Macintosh; Intel Mac OS X 11_6_8",
	"Macintosh; Intel Mac OS X 11_7",
	"Macintosh; Intel Mac OS X 11_7_1",
	"Macintosh; Intel Mac OS X 11_7_2",
	"Macintosh; Intel Mac OS X 11_7_3",
	"Macintosh; Intel Mac OS X 11_7_4",
	"Macintosh; Intel Mac OS X 11_7_5",
	"Macintosh; Intel Mac OS X 11_7_6",

	// MacOS - Monterey
	"Macintosh; Intel Mac OS X 12_0",
	"Macintosh; Intel Mac OS X 12_0_1",
	"Macintosh; Intel Mac OS X 12_1",
	"Macintosh; Intel Mac OS X 12_2",
	"Macintosh; Intel Mac OS X 12_2_1",
	"Macintosh; Intel Mac OS X 12_3",
	"Macintosh; Intel Mac OS X 12_3_1",
	"Macintosh; Intel Mac OS X 12_4",
	"Macintosh; Intel Mac OS X 12_5",
	"Macintosh; Intel Mac OS X 12_5_1",
	"Macintosh; Intel Mac OS X 12_6",
	"Macintosh; Intel Mac OS X 12_6_1",
	"Macintosh; Intel Mac OS X 12_6_2",
	"Macintosh; Intel Mac OS X 12_6_3",
	"Macintosh; Intel Mac OS X 12_6_4",
	"Macintosh; Intel Mac OS X 12_6_5",

	// MacOS - Ventura
	"Macintosh; Intel Mac OS X 13_0",
	"Macintosh; Intel Mac OS X 13_0_1",
	"Macintosh; Intel Mac OS X 13_1",
	"Macintosh; Intel Mac OS X 13_2",
	"Macintosh; Intel Mac OS X 13_2_1",
	"Macintosh; Intel Mac OS X 13_3",
	"Macintosh; Intel Mac OS X 13_3_1",

	// Windows
	"Windows NT 10.0; Win64; x64",
	"Windows NT 5.1",
	"Windows NT 6.1; WOW64",
	"Windows NT 6.1; Win64; x64",

	// Linux
	"X11; Linux x86_64",
}

// Generates Firefox Browser User-Agent (Desktop)
//
// -> "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0"
func genFirefoxUA() string {
	version := ffVersions[rand.Intn(len(ffVersions))]
	os := osStrings[rand.Intn(len(osStrings))]
	return fmt.Sprintf("Mozilla/5.0 (%s; rv:%.1f) Gecko/20100101 Firefox/%.1f", os, version, version)
}

// Generates Chrome Browser User-Agent (Desktop)
//
// -> "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
func genChromeUA() string {
	version := chromeVersions[rand.Intn(len(chromeVersions))]
	os := osStrings[rand.Intn(len(osStrings))]
	return fmt.Sprintf("Mozilla/5.0 (%s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s Safari/537.36", os, version)
}

// Generates Microsoft Edge User-Agent (Desktop)
//
// -> "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.39"
func genEdgeUA() string {
	version := edgeVersions[rand.Intn(len(edgeVersions))]
	chromeVersion := strings.Split(version, ",")[0]
	edgeVersion := strings.Split(version, ",")[1]
	os := osStrings[rand.Intn(len(osStrings))]
	return fmt.Sprintf("Mozilla/5.0 (%s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s Safari/537.36 Edg/%s", os, chromeVersion, edgeVersion)
}

// Generates Opera Browser User-Agent (Desktop)
//
// -> "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.4759.3"
func genOperaUA() string {
	version := operaVersions[rand.Intn(len(operaVersions))]
	chromeVersion := strings.Split(version, ",")[0]
	operaVersion := strings.Split(version, ",")[1]
	os := osStrings[rand.Intn(len(osStrings))]
	return fmt.Sprintf("Mozilla/5.0 (%s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s Safari/537.36 OPR/%s", os, chromeVersion, operaVersion)
}

// Generates Pixel 7 Browser User-Agent (Mobile)
//
// -> Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36
func genMobilePixel7UA() string {
	android := pixel7AndroidVersions[rand.Intn(len(pixel7AndroidVersions))]
	chrome := chromeVersions[rand.Intn(len(chromeVersions))]
	return fmt.Sprintf("Mozilla/5.0 (Linux; Android %s; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s Safari/537.36", android, chrome)
}

// Generates Pixel 6 Browser User-Agent (Mobile)
//
// -> "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
func genMobilePixel6UA() string {
	android := pixel6AndroidVersions[rand.Intn(len(pixel6AndroidVersions))]
	chrome := chromeVersions[rand.Intn(len(chromeVersions))]
	return fmt.Sprintf("Mozilla/5.0 (Linux; Android %s; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s Safari/537.36", android, chrome)
}

// Generates Pixel 5 Browser User-Agent (Mobile)
//
// -> "Mozilla/5.0 (Linux; Android 13; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
func genMobilePixel5UA() string {
	android := pixel5AndroidVersions[rand.Intn(len(pixel5AndroidVersions))]
	chrome := chromeVersions[rand.Intn(len(chromeVersions))]
	return fmt.Sprintf("Mozilla/5.0 (Linux; Android %s; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s Safari/537.36", android, chrome)
}

// Generates Pixel 4 Browser User-Agent (Mobile)
//
// -> "Mozilla/5.0 (Linux; Android 13; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
func genMobilePixel4UA() string {
	android := pixel4AndroidVersions[rand.Intn(len(pixel4AndroidVersions))]
	chrome := chromeVersions[rand.Intn(len(chromeVersions))]
	return fmt.Sprintf("Mozilla/5.0 (Linux; Android %s; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s Safari/537.36", android, chrome)
}

// Generates Nexus 10 Browser User-Agent (Mobile)
//
// -> "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 10 Build/LMY48T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.91 Safari/537.36"
func genMobileNexus10UA() string {
	build := nexus10Builds[rand.Intn(len(nexus10Builds))]
	android := nexus10AndroidVersions[rand.Intn(len(nexus10AndroidVersions))]
	chrome := chromeVersions[rand.Intn(len(chromeVersions))]
	return fmt.Sprintf("Mozilla/5.0 (Linux; Android %s; Nexus 10 Build/%s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s Safari/537.36", android, build, chrome)
}
```

## File: `extensions/referer.go`
```go
package extensions

import (
	"github.com/gocolly/colly/v2"
)

// Referer sets valid Referer HTTP header to requests.
// Warning: this extension works only if you use Request.Visit
// from callbacks instead of Collector.Visit.
func Referer(c *colly.Collector) {
	c.OnResponse(func(r *colly.Response) {
		r.Ctx.Put("_referer", r.Request.URL.String())
	})
	c.OnRequest(func(r *colly.Request) {
		if ref := r.Ctx.Get("_referer"); ref != "" {
			r.Headers.Set("Referer", ref)
		}
	})
}
```

## File: `extensions/url_length_filter.go`
```go
package extensions

import (
	"github.com/gocolly/colly/v2"
)

// URLLengthFilter filters out requests with URLs longer than URLLengthLimit
func URLLengthFilter(c *colly.Collector, URLLengthLimit int) {
	c.OnRequest(func(r *colly.Request) {
		if len(r.URL.String()) > URLLengthLimit {
			r.Abort()
		}
	})
}
```

## File: `proxy/proxy.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package proxy

import (
	"context"
	"net/http"
	"net/url"
	"sync/atomic"

	"github.com/gocolly/colly/v2"
)

type roundRobinSwitcher struct {
	proxyURLs []*url.URL
	index     uint32
}

func (r *roundRobinSwitcher) GetProxy(pr *http.Request) (*url.URL, error) {
	index := atomic.AddUint32(&r.index, 1) - 1
	u := r.proxyURLs[index%uint32(len(r.proxyURLs))]

	ctx := context.WithValue(pr.Context(), colly.ProxyURLKey, u.String())
	*pr = *pr.WithContext(ctx)
	return u, nil
}

// RoundRobinProxySwitcher creates a proxy switcher function which rotates
// ProxyURLs on every request.
// The proxy type is determined by the URL scheme. "http", "https"
// and "socks5" are supported. If the scheme is empty,
// "http" is assumed.
func RoundRobinProxySwitcher(ProxyURLs ...string) (colly.ProxyFunc, error) {
	if len(ProxyURLs) < 1 {
		return nil, colly.ErrEmptyProxyURL
	}
	urls := make([]*url.URL, len(ProxyURLs))
	for i, u := range ProxyURLs {
		parsedU, err := url.Parse(u)
		if err != nil {
			return nil, err
		}
		urls[i] = parsedU
	}
	return (&roundRobinSwitcher{urls, 0}).GetProxy, nil
}
```

## File: `queue/queue.go`
```go
package queue

import (
	"net/url"
	"sync"

	whatwgUrl "github.com/nlnwa/whatwg-url/url"

	"github.com/gocolly/colly/v2"
)

const stop = true

var urlParser = whatwgUrl.NewParser(whatwgUrl.WithPercentEncodeSinglePercentSign())

// Storage is the interface of the queue's storage backend
// Storage must be concurrently safe for multiple goroutines.
type Storage interface {
	// Init initializes the storage
	Init() error
	// AddRequest adds a serialized request to the queue
	AddRequest([]byte) error
	// GetRequest pops the next request from the queue
	// or returns error if the queue is empty
	GetRequest() ([]byte, error)
	// QueueSize returns with the size of the queue
	QueueSize() (int, error)
}

// Queue is a request queue which uses a Collector to consume
// requests in multiple threads
type Queue struct {
	// Threads defines the number of consumer threads
	Threads int
	storage Storage
	wake    chan struct{}
	mut     sync.Mutex // guards wake and running
	running bool
}

// InMemoryQueueStorage is the default implementation of the Storage interface.
// InMemoryQueueStorage holds the request queue in memory.
type InMemoryQueueStorage struct {
	// MaxSize defines the capacity of the queue.
	// New requests are discarded if the queue size reaches MaxSize
	MaxSize int
	lock    *sync.RWMutex
	size    int
	first   *inMemoryQueueItem
	last    *inMemoryQueueItem
}

type inMemoryQueueItem struct {
	Request []byte
	Next    *inMemoryQueueItem
}

// New creates a new queue with a Storage specified in argument
// A standard InMemoryQueueStorage is used if Storage argument is nil.
func New(threads int, s Storage) (*Queue, error) {
	if s == nil {
		s = &InMemoryQueueStorage{MaxSize: 100000}
	}
	if err := s.Init(); err != nil {
		return nil, err
	}
	return &Queue{
		Threads: threads,
		storage: s,
		running: true,
	}, nil
}

// IsEmpty returns true if the queue is empty
func (q *Queue) IsEmpty() bool {
	s, _ := q.Size()
	return s == 0
}

// AddURL adds a new URL to the queue
func (q *Queue) AddURL(URL string) error {
	u, err := urlParser.Parse(URL)
	if err != nil {
		return err
	}
	u2, err := url.Parse(u.Href(false))
	if err != nil {
		return err
	}
	r := &colly.Request{
		URL:    u2,
		Method: "GET",
	}
	d, err := r.Marshal()
	if err != nil {
		return err
	}
	return q.storage.AddRequest(d)
}

// AddRequest adds a new Request to the queue
func (q *Queue) AddRequest(r *colly.Request) error {
	q.mut.Lock()
	waken := q.wake != nil
	q.mut.Unlock()
	if !waken {
		return q.storeRequest(r)
	}
	err := q.storeRequest(r)
	if err != nil {
		return err
	}
	q.wake <- struct{}{}
	return nil
}

func (q *Queue) storeRequest(r *colly.Request) error {
	d, err := r.Marshal()
	if err != nil {
		return err
	}
	return q.storage.AddRequest(d)
}

// Size returns the size of the queue
func (q *Queue) Size() (int, error) {
	return q.storage.QueueSize()
}

// Run starts consumer threads and calls the Collector
// to perform requests. Run blocks while the queue has active requests
// The given Storage must not be used directly while Run blocks.
func (q *Queue) Run(c *colly.Collector) error {
	q.mut.Lock()
	if q.wake != nil && q.running == true {
		q.mut.Unlock()
		panic("cannot call duplicate Queue.Run")
	}
	q.wake = make(chan struct{})
	q.running = true
	q.mut.Unlock()

	requestc := make(chan *colly.Request)
	complete, errc := make(chan struct{}), make(chan error, 1)
	for i := 0; i < q.Threads; i++ {
		go independentRunner(requestc, complete)
	}
	go q.loop(c, requestc, complete, errc)
	defer close(requestc)
	return <-errc
}

// Stop will stop the running queue
func (q *Queue) Stop() {
	q.mut.Lock()
	q.running = false
	q.mut.Unlock()
}

func (q *Queue) loop(c *colly.Collector, requestc chan<- *colly.Request, complete <-chan struct{}, errc chan<- error) {
	var active int
	for {
		size, err := q.storage.QueueSize()
		if err != nil {
			errc <- err
			break
		}
		if size == 0 && active == 0 || !q.running {
			// Terminate when
			//   1. No active requests
			//   2. Empty queue
			errc <- nil
			break
		}
		sent := requestc
		var req *colly.Request
		if size > 0 {
			req, err = q.loadRequest(c)
			if err != nil {
				// ignore an error returned by GetRequest() or
				// UnmarshalRequest()
				continue
			}
		} else {
			sent = nil
		}
	Sent:
		for {
			select {
			case sent <- req:
				active++
				break Sent
			case <-q.wake:
				if sent == nil {
					break Sent
				}
			case <-complete:
				active--
				if sent == nil && active == 0 {
					break Sent
				}
			}
		}
	}
}

func independentRunner(requestc <-chan *colly.Request, complete chan<- struct{}) {
	for req := range requestc {
		req.Do()
		complete <- struct{}{}
	}
}

func (q *Queue) loadRequest(c *colly.Collector) (*colly.Request, error) {
	buf, err := q.storage.GetRequest()
	if err != nil {
		return nil, err
	}
	copied := make([]byte, len(buf))
	copy(copied, buf)
	return c.UnmarshalRequest(copied)
}

// Init implements Storage.Init() function
func (q *InMemoryQueueStorage) Init() error {
	q.lock = &sync.RWMutex{}
	return nil
}

// AddRequest implements Storage.AddRequest() function
func (q *InMemoryQueueStorage) AddRequest(r []byte) error {
	q.lock.Lock()
	defer q.lock.Unlock()
	// Discard URLs if size limit exceeded
	if q.MaxSize > 0 && q.size >= q.MaxSize {
		return colly.ErrQueueFull
	}
	i := &inMemoryQueueItem{Request: r}
	if q.first == nil {
		q.first = i
	} else {
		q.last.Next = i
	}
	q.last = i
	q.size++
	return nil
}

// GetRequest implements Storage.GetRequest() function
func (q *InMemoryQueueStorage) GetRequest() ([]byte, error) {
	q.lock.Lock()
	defer q.lock.Unlock()
	if q.size == 0 {
		return nil, nil
	}
	r := q.first.Request
	q.first = q.first.Next
	q.size--
	return r, nil
}

// QueueSize implements Storage.QueueSize() function
func (q *InMemoryQueueStorage) QueueSize() (int, error) {
	q.lock.Lock()
	defer q.lock.Unlock()
	return q.size, nil
}
```

## File: `queue/queue_test.go`
```go
package queue

import (
	"math/rand"
	"net/http"
	"net/http/httptest"
	"sync"
	"sync/atomic"
	"testing"
	"time"

	"github.com/gocolly/colly/v2"
)

func TestQueue(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(serverHandler))
	defer server.Close()

	rng := rand.New(rand.NewSource(12387123712321232))
	var rngMu sync.Mutex

	var (
		items    uint32
		requests uint32
		success  uint32
		failure  uint32
	)
	storage := &InMemoryQueueStorage{MaxSize: 100000}
	q, err := New(10, storage)
	if err != nil {
		panic(err)
	}
	put := func() {
		rngMu.Lock()
		t := time.Duration(rng.Intn(50)) * time.Microsecond
		rngMu.Unlock()
		url := server.URL + "/delay?t=" + t.String()
		atomic.AddUint32(&items, 1)
		q.AddURL(url)
	}
	for i := 0; i < 3000; i++ {
		put()
		storage.AddRequest([]byte("error request"))
	}
	c := colly.NewCollector(
		colly.AllowURLRevisit(),
	)
	c.OnRequest(func(req *colly.Request) {
		atomic.AddUint32(&requests, 1)
	})
	c.OnResponse(func(resp *colly.Response) {
		if resp.StatusCode == http.StatusOK {
			atomic.AddUint32(&success, 1)
		} else {
			atomic.AddUint32(&failure, 1)
		}
		rngMu.Lock()
		toss := rng.Intn(2) == 0
		rngMu.Unlock()
		if toss {
			put()
		}
	})
	c.OnError(func(resp *colly.Response, err error) {
		atomic.AddUint32(&failure, 1)
	})
	err = q.Run(c)
	if err != nil {
		t.Fatalf("Queue.Run() return an error: %v", err)
	}
	if items != requests || success+failure != requests || failure > 0 {
		t.Fatalf("wrong Queue implementation: "+
			"items = %d, requests = %d, success = %d, failure = %d",
			items, requests, success, failure)
	}
}

func serverHandler(w http.ResponseWriter, req *http.Request) {
	if !serverRoute(w, req) {
		shutdown(w)
	}
}

func serverRoute(w http.ResponseWriter, req *http.Request) bool {
	if req.URL.Path == "/delay" {
		return serveDelay(w, req) == nil
	}
	return false
}

func serveDelay(w http.ResponseWriter, req *http.Request) error {
	q := req.URL.Query()
	t, err := time.ParseDuration(q.Get("t"))
	if err != nil {
		return err
	}
	time.Sleep(t)
	w.WriteHeader(http.StatusOK)
	return nil
}

func shutdown(w http.ResponseWriter) {
	taker, ok := w.(http.Hijacker)
	if !ok {
		return
	}
	raw, _, err := taker.Hijack()
	if err != nil {
		return
	}
	raw.Close()
}
```

## File: `vault/storage.go`
```go
// Copyright 2018 Adam Tauber
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package storage

import (
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"strings"
	"sync"
)

// Storage is an interface which handles Collector's internal data,
// like visited urls and cookies.
// The default Storage of the Collector is the InMemoryStorage.
// Collector's storage can be changed by calling Collector.SetStorage()
// function.
type Storage interface {
	// Init initializes the storage
	Init() error
	// Visited receives and stores a request ID that is visited by the Collector
	Visited(requestID uint64) error
	// IsVisited returns true if the request was visited before IsVisited
	// is called
	IsVisited(requestID uint64) (bool, error)
	// Cookies retrieves stored cookies for a given host
	Cookies(u *url.URL) string
	// SetCookies stores cookies for a given host
	SetCookies(u *url.URL, cookies string)
}

// InMemoryStorage is the default storage backend of colly.
// InMemoryStorage keeps cookies and visited urls in memory
// without persisting data on the disk.
type InMemoryStorage struct {
	visitedURLs map[uint64]bool
	lock        *sync.RWMutex
	jar         *cookiejar.Jar
}

// Init initializes InMemoryStorage
func (s *InMemoryStorage) Init() error {
	if s.visitedURLs == nil {
		s.visitedURLs = make(map[uint64]bool)
	}
	if s.lock == nil {
		s.lock = &sync.RWMutex{}
	}
	if s.jar == nil {
		var err error
		s.jar, err = cookiejar.New(nil)
		return err
	}
	return nil
}

// Visited implements Storage.Visited()
func (s *InMemoryStorage) Visited(requestID uint64) error {
	s.lock.Lock()
	s.visitedURLs[requestID] = true
	s.lock.Unlock()
	return nil
}

// IsVisited implements Storage.IsVisited()
func (s *InMemoryStorage) IsVisited(requestID uint64) (bool, error) {
	s.lock.RLock()
	visited := s.visitedURLs[requestID]
	s.lock.RUnlock()
	return visited, nil
}

// Cookies implements Storage.Cookies()
func (s *InMemoryStorage) Cookies(u *url.URL) string {
	return StringifyCookies(s.jar.Cookies(u))
}

// SetCookies implements Storage.SetCookies()
func (s *InMemoryStorage) SetCookies(u *url.URL, cookies string) {
	s.jar.SetCookies(u, UnstringifyCookies(cookies))
}

// Close implements Storage.Close()
func (s *InMemoryStorage) Close() error {
	return nil
}

// StringifyCookies serializes list of http.Cookies to string
func StringifyCookies(cookies []*http.Cookie) string {
	// Stringify cookies.
	cs := make([]string, len(cookies))
	for i, c := range cookies {
		cs[i] = c.String()
	}
	return strings.Join(cs, "\n")
}

// UnstringifyCookies deserializes a cookie string to http.Cookies
func UnstringifyCookies(s string) []*http.Cookie {
	h := http.Header{}
	for _, c := range strings.Split(s, "\n") {
		h.Add("Set-Cookie", c)
	}
	r := http.Response{Header: h}
	return r.Cookies()
}

// ContainsCookie checks if a cookie name is represented in cookies
func ContainsCookie(cookies []*http.Cookie, name string) bool {
	for _, c := range cookies {
		if c.Name == name {
			return true
		}
	}
	return false
}
```

## File: `_examples/README.md`
```markdown
# Colly examples

This folder provides easy to understand code snippets on how to get started with colly.

To execute an example run `go run [example/example.go]`


## Demo

```
$ go run rate_limit/rate_limit.go
[000001] 1 [     1 - request] map["url":"https://httpbin.org/delay/2?n=4"] (60.872µs)
[000002] 1 [     2 - request] map["url":"https://httpbin.org/delay/2?n=2"] (154.425µs)
[000003] 1 [     3 - request] map["url":"https://httpbin.org/delay/2?n=0"] (158.374µs)
[000004] 1 [     5 - request] map["url":"https://httpbin.org/delay/2?n=3"] (426.999µs)
[000005] 1 [     4 - request] map["url":"https://httpbin.org/delay/2?n=1"] (448.75µs)
[000007] 1 [     2 - response] map["url":"https://httpbin.org/delay/2?n=2" "status":"OK"] (2.855764394s)
[000008] 1 [     2 - scraped] map["url":"https://httpbin.org/delay/2?n=2"] (2.855797868s)
[000006] 1 [     1 - response] map["url":"https://httpbin.org/delay/2?n=4" "status":"OK"] (2.855756753s)
[000009] 1 [     1 - scraped] map["url":"https://httpbin.org/delay/2?n=4"] (2.855819581s)
[000010] 1 [     3 - response] map["status":"OK" "url":"https://httpbin.org/delay/2?n=0"] (5.002065299s)
[000011] 1 [     3 - scraped] map["url":"https://httpbin.org/delay/2?n=0"] (5.002103755s)
[000012] 1 [     5 - response] map["status":"OK" "url":"https://httpbin.org/delay/2?n=3"] (5.012080614s)
[000013] 1 [     5 - scraped] map["url":"https://httpbin.org/delay/2?n=3"] (5.012101056s)
[000014] 1 [     4 - response] map["url":"https://httpbin.org/delay/2?n=1" "status":"OK"] (7.155725591s)
[000015] 1 [     4 - scraped] map["url":"https://httpbin.org/delay/2?n=1"] (7.155759136s)

```
```

## File: `_examples/basic/basic.go`
```go
package main

import (
	"fmt"

	"github.com/gocolly/colly/v2"
)

func main() {
	// Instantiate default collector
	c := colly.NewCollector(
		// Visit only domains: hackerspaces.org, wiki.hackerspaces.org
		colly.AllowedDomains("hackerspaces.org", "wiki.hackerspaces.org"),
	)

	// On every a element which has href attribute call callback
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		link := e.Attr("href")
		// Print link
		fmt.Printf("Link found: %q -> %s\n", e.Text, link)
		// Visit link found on page
		// Only those links are visited which are in AllowedDomains
		c.Visit(e.Request.AbsoluteURL(link))
	})

	// Before making a request print "Visiting ..."
	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL.String())
	})

	// Start scraping on https://hackerspaces.org
	c.Visit("https://hackerspaces.org/")
}
```

## File: `_examples/coursera_courses/coursera_courses.go`
```go
package main

import (
	"encoding/json"
	"log"
	"os"
	"strings"
	"time"

	"github.com/gocolly/colly/v2"
)

// Course stores information about a coursera course
type Course struct {
	Title       string
	Description string
	Creator     string
	Level       string
	URL         string
	Language    string
	Commitment  string
	Rating      string
}

func main() {
	fName := "courses.json"
	file, err := os.Create(fName)
	if err != nil {
		log.Fatalf("Cannot create file %q: %s\n", fName, err)
		return
	}
	defer file.Close()

	// Instantiate default collector
	c := colly.NewCollector(
		// Visit only domains: coursera.org, www.coursera.org
		colly.AllowedDomains("coursera.org", "www.coursera.org"),

		// Cache responses to prevent multiple download of pages
		// even if the collector is restarted
		colly.CacheDir("./coursera_cache"),
		// Cached responses older than the specified duration will be refreshed
		colly.CacheExpiration(24*time.Hour),
	)

	// Create another collector to scrape course details
	detailCollector := c.Clone()

	courses := make([]Course, 0, 200)

	// On every <a> element which has "href" attribute call callback
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		// If attribute class is this long string return from callback
		// As this a is irrelevant
		if e.Attr("class") == "Button_1qxkboh-o_O-primary_cv02ee-o_O-md_28awn8-o_O-primaryLink_109aggg" {
			return
		}
		link := e.Attr("href")
		// If link start with browse or includes either signup or login return from callback
		if !strings.HasPrefix(link, "/browse") || strings.Index(link, "=signup") > -1 || strings.Index(link, "=login") > -1 {
			return
		}
		// start scaping the page under the link found
		e.Request.Visit(link)
	})

	// Before making a request print "Visiting ..."
	c.OnRequest(func(r *colly.Request) {
		log.Println("visiting", r.URL.String())
	})

	// On every <a> element with collection-product-card class call callback
	c.OnHTML(`a.collection-product-card`, func(e *colly.HTMLElement) {
		// Activate detailCollector if the link contains "coursera.org/learn"
		courseURL := e.Request.AbsoluteURL(e.Attr("href"))
		if strings.Index(courseURL, "coursera.org/learn") != -1 {
			detailCollector.Visit(courseURL)
		}
	})

	// Extract details of the course
	detailCollector.OnHTML(`div[id=rendered-content]`, func(e *colly.HTMLElement) {
		log.Println("Course found", e.Request.URL)
		title := e.ChildText(".banner-title")
		if title == "" {
			log.Println("No title found", e.Request.URL)
		}
		course := Course{
			Title:       title,
			URL:         e.Request.URL.String(),
			Description: e.ChildText("div.content"),
			Creator:     e.ChildText("li.banner-instructor-info > a > div > div > span"),
			Rating:      e.ChildText("span.number-rating"),
		}
		// Iterate over div components and add details to course
		e.ForEach(".AboutCourse .ProductGlance > div", func(_ int, el *colly.HTMLElement) {
			svgTitle := strings.Split(el.ChildText("div:nth-child(1) svg title"), " ")
			lastWord := svgTitle[len(svgTitle)-1]
			switch lastWord {
			// svg Title: Available Languages
			case "languages":
				course.Language = el.ChildText("div:nth-child(2) > div:nth-child(1)")
			// svg Title: Mixed/Beginner/Intermediate/Advanced Level
			case "Level":
				course.Level = el.ChildText("div:nth-child(2) > div:nth-child(1)")
			// svg Title: Hours to complete
			case "complete":
				course.Commitment = el.ChildText("div:nth-child(2) > div:nth-child(1)")
			}
		})
		courses = append(courses, course)
	})

	// Start scraping on http://coursera.com/browse
	c.Visit("https://coursera.org/browse")

	enc := json.NewEncoder(file)
	enc.SetIndent("", "  ")

	// Dump json to the standard output
	enc.Encode(courses)
}
```

## File: `_examples/cryptocoinmarketcap/cryptocoinmarketcap.go`
```go
package main

import (
	"encoding/csv"
	"log"
	"os"

	"github.com/gocolly/colly/v2"
)

func main() {
	fName := "cryptocoinmarketcap.csv"
	file, err := os.Create(fName)
	if err != nil {
		log.Fatalf("Cannot create file %q: %s\n", fName, err)
		return
	}
	defer file.Close()
	writer := csv.NewWriter(file)
	defer writer.Flush()

	// Write CSV header
	writer.Write([]string{"Name", "Symbol", "Market Cap (USD)", "Price (USD)", "Circulating Supply (USD)", "Volume (24h)", "Change (1h)", "Change (24h)", "Change (7d)"})

	// Instantiate default collector
	c := colly.NewCollector()

	c.OnHTML("tbody tr", func(e *colly.HTMLElement) {
		writer.Write([]string{
			e.ChildText(".cmc-table__column-name"),
			e.ChildText(".cmc-table__cell--sort-by__symbol"),
			e.ChildText(".cmc-table__cell--sort-by__market-cap"),
			e.ChildText(".cmc-table__cell--sort-by__price"),
			e.ChildText(".cmc-table__cell--sort-by__circulating-supply"),
			e.ChildText(".cmc-table__cell--sort-by__volume-24-h"),
			e.ChildText(".cmc-table__cell--sort-by__percent-change-1-h"),
			e.ChildText(".cmc-table__cell--sort-by__percent-change-24-h"),
			e.ChildText(".cmc-table__cell--sort-by__percent-change-7-d"),
		})
	})

	c.Visit("https://coinmarketcap.com/all/views/all/")

	log.Printf("Scraping finished, check file %q for results\n", fName)
}
```

## File: `_examples/error_handling/error_handling.go`
```go
package main

import (
	"fmt"

	"github.com/gocolly/colly/v2"
)

func main() {
	// Create a collector
	c := colly.NewCollector()

	// Set HTML callback
	// Won't be called if error occurs
	c.OnHTML("*", func(e *colly.HTMLElement) {
		fmt.Println(e)
	})

	// Set error handler
	c.OnError(func(r *colly.Response, err error) {
		fmt.Println("Request URL:", r.Request.URL, "failed with response:", r, "\nError:", err)
	})

	// Start scraping
	c.Visit("https://definitely-not-a.website/")
}
```

## File: `_examples/factba.se/factbase.go`
```go
package main

import (
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/gocolly/colly/v2"
)

var baseSearchURL = "https://factba.se/json/json-transcript.php?q=&f=&dt=&p="
var baseTranscriptURL = "https://factba.se/transcript/"

type result struct {
	Slug string `json:"slug"`
	Date string `json:"date"`
}

type results struct {
	Data []*result `json:"data"`
}

type transcript struct {
	Speaker string
	Text    string
}

func main() {
	c := colly.NewCollector(
		colly.AllowedDomains("factba.se"),
	)

	d := c.Clone()

	d.OnHTML("body", func(e *colly.HTMLElement) {
		t := make([]transcript, 0)
		e.ForEach(".topic-media-row", func(_ int, el *colly.HTMLElement) {
			t = append(t, transcript{
				Speaker: el.ChildText(".speaker-label"),
				Text:    el.ChildText(".transcript-text-block"),
			})
		})
		jsonData, err := json.MarshalIndent(t, "", "  ")
		if err != nil {
			return
		}
		os.WriteFile(colly.SanitizeFileName(e.Request.Ctx.Get("date")+"_"+e.Request.Ctx.Get("slug"))+".json", jsonData, 0644)
	})

	stop := false
	c.OnResponse(func(r *colly.Response) {
		rs := &results{}
		err := json.Unmarshal(r.Body, rs)
		if err != nil || len(rs.Data) == 0 {
			stop = true
			return
		}
		for _, res := range rs.Data {
			u := baseTranscriptURL + res.Slug
			ctx := colly.NewContext()
			ctx.Put("date", res.Date)
			ctx.Put("slug", res.Slug)
			d.Request("GET", u, nil, ctx, nil)
		}
	})

	for i := 1; i < 1000; i++ {
		if stop {
			break
		}
		if err := c.Visit(baseSearchURL + strconv.Itoa(i)); err != nil {
			fmt.Println("Error:", err)
			break
		}
	}
}
```

## File: `_examples/google_groups/google_groups.go`
```go
package main

import (
	"encoding/json"
	"flag"
	"log"
	"os"
	"strings"

	"github.com/gocolly/colly/v2"
)

// Mail is the container of a single e-mail
type Mail struct {
	Title   string
	Link    string
	Author  string
	Date    string
	Message string
}

func main() {
	var groupName string
	flag.StringVar(&groupName, "group", "hspbp", "Google Groups group name")
	flag.Parse()

	threads := make(map[string][]Mail)

	threadCollector := colly.NewCollector()
	mailCollector := colly.NewCollector()

	// Collect threads
	threadCollector.OnHTML("tr", func(e *colly.HTMLElement) {
		ch := e.DOM.Children()
		author := ch.Eq(1).Text()
		// deleted topic
		if author == "" {
			return
		}

		title := ch.Eq(0).Text()
		link, _ := ch.Eq(0).Children().Eq(0).Attr("href")
		// fix link to point to the pure HTML version of the thread
		link = strings.Replace(link, ".com/d/topic", ".com/forum/?_escaped_fragment_=topic", 1)
		date := ch.Eq(2).Text()

		log.Printf("Thread found: %s %q %s %s\n", link, title, author, date)
		mailCollector.Visit(link)
	})

	// Visit next page
	threadCollector.OnHTML("body > a[href]", func(e *colly.HTMLElement) {
		log.Println("Next page link found:", e.Attr("href"))
		e.Request.Visit(e.Attr("href"))
	})

	// Extract mails
	mailCollector.OnHTML("body", func(e *colly.HTMLElement) {
		// Find subject
		threadSubject := e.ChildText("h2")
		if _, ok := threads[threadSubject]; !ok {
			threads[threadSubject] = make([]Mail, 0, 8)
		}

		// Extract mails
		e.ForEach("table tr", func(_ int, el *colly.HTMLElement) {
			mail := Mail{
				Title:   el.ChildText("td:nth-of-type(1)"),
				Link:    el.ChildAttr("td:nth-of-type(1)", "href"),
				Author:  el.ChildText("td:nth-of-type(2)"),
				Date:    el.ChildText("td:nth-of-type(3)"),
				Message: el.ChildText("td:nth-of-type(4)"),
			}
			threads[threadSubject] = append(threads[threadSubject], mail)
		})

		// Follow next page link
		if link, found := e.DOM.Find("> a[href]").Attr("href"); found {
			e.Request.Visit(link)
		} else {
			log.Printf("Thread %q done\n", threadSubject)
		}
	})

	threadCollector.Visit("https://groups.google.com/forum/?_escaped_fragment_=forum/" + groupName)

	enc := json.NewEncoder(os.Stdout)
	enc.SetIndent("", "  ")

	// Dump json to the standard output
	enc.Encode(threads)
}
```

## File: `_examples/hackernews_comments/hackernews_comments.go`
```go
package main

import (
	"encoding/json"
	"flag"
	"log"
	"os"
	"strconv"
	"strings"

	"github.com/gocolly/colly/v2"
)

type comment struct {
	Author  string `selector:"a.hnuser"`
	URL     string `selector:".age a[href]" attr:"href"`
	Comment string `selector:".comment"`
	Replies []*comment
	depth   int
}

func main() {
	var itemID string
	flag.StringVar(&itemID, "id", "", "hackernews post id")
	flag.Parse()

	if itemID == "" {
		log.Println("Hackernews post id required")
		os.Exit(1)
	}

	comments := make([]*comment, 0)

	// Instantiate default collector
	c := colly.NewCollector()

	// Extract comment
	c.OnHTML(".comment-tree tr.athing", func(e *colly.HTMLElement) {
		width, err := strconv.Atoi(e.ChildAttr("td.ind img", "width"))
		if err != nil {
			return
		}
		// hackernews uses 40px spacers to indent comment replies,
		// so we have to divide the width with it to get the depth
		// of the comment
		depth := width / 40
		c := &comment{
			Replies: make([]*comment, 0),
			depth:   depth,
		}
		e.Unmarshal(c)
		c.Comment = strings.TrimSpace(c.Comment[:len(c.Comment)-5])
		if depth == 0 {
			comments = append(comments, c)
			return
		}
		parent := comments[len(comments)-1]
		// append comment to its parent
		for i := 0; i < depth-1; i++ {
			parent = parent.Replies[len(parent.Replies)-1]
		}
		parent.Replies = append(parent.Replies, c)
	})

	c.Visit("https://news.ycombinator.com/item?id=" + itemID)

	enc := json.NewEncoder(os.Stdout)
	enc.SetIndent("", "  ")

	// Dump json to the standard output
	enc.Encode(comments)
}
```

## File: `_examples/instagram/instagram.go`
```go
package main

import (
	"crypto/md5"
	"encoding/json"
	"fmt"
	"log"
	"net/url"
	"os"
	"regexp"
	"strings"

	"github.com/gocolly/colly/v2"
)

// "id": user id, "after": end cursor
const nextPageURL string = `https://www.instagram.com/graphql/query/?query_hash=%s&variables=%s`
const nextPagePayload string = `{"id":"%s","first":50,"after":"%s"}`

var requestID string
var requestIds [][]byte
var queryIdPattern = regexp.MustCompile(`queryId:".{32}"`)

type pageInfo struct {
	EndCursor string `json:"end_cursor"`
	NextPage  bool   `json:"has_next_page"`
}

type mainPageData struct {
	Rhxgis    string `json:"rhx_gis"`
	EntryData struct {
		ProfilePage []struct {
			Graphql struct {
				User struct {
					Id    string `json:"id"`
					Media struct {
						Edges []struct {
							Node struct {
								ImageURL     string `json:"display_url"`
								ThumbnailURL string `json:"thumbnail_src"`
								IsVideo      bool   `json:"is_video"`
								Date         int    `json:"date"`
								Dimensions   struct {
									Width  int `json:"width"`
									Height int `json:"height"`
								} `json:"dimensions"`
							} `json:node"`
						} `json:"edges"`
						PageInfo pageInfo `json:"page_info"`
					} `json:"edge_owner_to_timeline_media"`
				} `json:"user"`
			} `json:"graphql"`
		} `json:"ProfilePage"`
	} `json:"entry_data"`
}

type nextPageData struct {
	Data struct {
		User struct {
			Container struct {
				PageInfo pageInfo `json:"page_info"`
				Edges    []struct {
					Node struct {
						ImageURL     string `json:"display_url"`
						ThumbnailURL string `json:"thumbnail_src"`
						IsVideo      bool   `json:"is_video"`
						Date         int    `json:"taken_at_timestamp"`
						Dimensions   struct {
							Width  int `json:"width"`
							Height int `json:"height"`
						}
					}
				} `json:"edges"`
			} `json:"edge_owner_to_timeline_media"`
		}
	} `json:"data"`
}

func main() {
	if len(os.Args) != 2 {
		log.Println("Missing account name argument")
		os.Exit(1)
	}

	var actualUserId string
	instagramAccount := os.Args[1]
	outputDir := fmt.Sprintf("./instagram_%s/", instagramAccount)

	c := colly.NewCollector(
		//colly.CacheDir("./_instagram_cache/"),
		colly.UserAgent("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"),
	)

	c.OnRequest(func(r *colly.Request) {
		r.Headers.Set("X-Requested-With", "XMLHttpRequest")
		r.Headers.Set("Referer", "https://www.instagram.com/"+instagramAccount)
		if r.Ctx.Get("gis") != "" {
			gis := fmt.Sprintf("%s:%s", r.Ctx.Get("gis"), r.Ctx.Get("variables"))
			h := md5.New()
			h.Write([]byte(gis))
			gisHash := fmt.Sprintf("%x", h.Sum(nil))
			r.Headers.Set("X-Instagram-GIS", gisHash)
		}
	})

	c.OnHTML("html", func(e *colly.HTMLElement) {
		d := c.Clone()
		d.OnResponse(func(r *colly.Response) {
			requestIds = queryIdPattern.FindAll(r.Body, -1)
			requestID = string(requestIds[1][9:41])
		})
		requestIDURL := e.Request.AbsoluteURL(e.ChildAttr(`link[as="script"]`, "href"))
		d.Visit(requestIDURL)

		dat := e.ChildText("body > script:first-of-type")
		jsonData := dat[strings.Index(dat, "{") : len(dat)-1]
		data := &mainPageData{}
		err := json.Unmarshal([]byte(jsonData), data)
		if err != nil {
			log.Fatal(err)
		}

		log.Println("saving output to ", outputDir)
		os.MkdirAll(outputDir, os.ModePerm)
		page := data.EntryData.ProfilePage[0]
		actualUserId = page.Graphql.User.Id
		for _, obj := range page.Graphql.User.Media.Edges {
			// skip videos
			if obj.Node.IsVideo {
				continue
			}
			c.Visit(obj.Node.ImageURL)
		}
		nextPageVars := fmt.Sprintf(nextPagePayload, actualUserId, page.Graphql.User.Media.PageInfo.EndCursor)
		e.Request.Ctx.Put("variables", nextPageVars)
		if page.Graphql.User.Media.PageInfo.NextPage {
			u := fmt.Sprintf(
				nextPageURL,
				requestID,
				url.QueryEscape(nextPageVars),
			)
			log.Println("Next page found", u)
			e.Request.Ctx.Put("gis", data.Rhxgis)
			e.Request.Visit(u)
		}
	})

	c.OnError(func(r *colly.Response, e error) {
		log.Println("error:", e, r.Request.URL, string(r.Body))
	})

	c.OnResponse(func(r *colly.Response) {
		if strings.Index(r.Headers.Get("Content-Type"), "image") > -1 {
			r.Save(outputDir + r.FileName())
			return
		}

		if strings.Index(r.Headers.Get("Content-Type"), "json") == -1 {
			return
		}

		data := &nextPageData{}
		err := json.Unmarshal(r.Body, data)
		if err != nil {
			log.Fatal(err)
		}

		for _, obj := range data.Data.User.Container.Edges {
			// skip videos
			if obj.Node.IsVideo {
				continue
			}
			c.Visit(obj.Node.ImageURL)
		}
		if data.Data.User.Container.PageInfo.NextPage {
			nextPageVars := fmt.Sprintf(nextPagePayload, actualUserId, data.Data.User.Container.PageInfo.EndCursor)
			r.Request.Ctx.Put("variables", nextPageVars)
			u := fmt.Sprintf(
				nextPageURL,
				requestID,
				url.QueryEscape(nextPageVars),
			)
			log.Println("Next page found", u)
			r.Request.Visit(u)
		}
	})

	c.Visit("https://instagram.com/" + instagramAccount)
}
```

## File: `_examples/local_files/local_files.go`
```go
package main

import (
	"fmt"
	"net/http"
	"os"
	"path/filepath"

	"github.com/gocolly/colly/v2"
)

func main() {
	dir, err := filepath.Abs(filepath.Dir(os.Args[0]))
	if err != nil {
		panic(err)
	}

	t := &http.Transport{}
	t.RegisterProtocol("file", http.NewFileTransport(http.Dir("/")))

	c := colly.NewCollector()
	c.WithTransport(t)

	pages := []string{}

	c.OnHTML("h1", func(e *colly.HTMLElement) {
		pages = append(pages, e.Text)
	})

	c.OnHTML("a", func(e *colly.HTMLElement) {
		c.Visit("file://" + dir + "/html" + e.Attr("href"))
	})

	fmt.Println("file://" + dir + "/html/index.html")
	c.Visit("file://" + dir + "/html/index.html")
	c.Wait()
	for i, p := range pages {
		fmt.Printf("%d : %s\n", i, p)
	}
}
```

## File: `_examples/local_files/html/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Index.html</h1>
    <ul>
        <li><a href="/child_page/one.html"></a></li>
        <li><a href="/child_page/two.html"></a></li>
        <li><a href="/child_page/three.html"></a></li>
    </ul>
</body>
</html>
```

## File: `_examples/local_files/html/child_page/one.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Child Page One</h1>
</body>
</html>
```

## File: `_examples/local_files/html/child_page/three.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Child Page Three</h1>
</body>
</html>
```

## File: `_examples/local_files/html/child_page/two.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Child Page Two</h1>
</body>
</html>
```

## File: `_examples/login/login.go`
```go
package main

import (
	"log"

	"github.com/gocolly/colly/v2"
)

func main() {
	// create a new collector
	c := colly.NewCollector()

	// authenticate
	err := c.Post("http://example.com/login", map[string]string{"username": "admin", "password": "admin"})
	if err != nil {
		log.Fatal(err)
	}

	// attach callbacks after login
	c.OnResponse(func(r *colly.Response) {
		log.Println("response received", r.StatusCode)
	})

	// start scraping
	c.Visit("https://example.com/")
}
```

## File: `_examples/max_depth/max_depth.go`
```go
package main

import (
	"fmt"

	"github.com/gocolly/colly/v2"
)

func main() {
	// Instantiate default collector
	c := colly.NewCollector(
		// MaxDepth is 1, so only the links on the scraped page
		// is visited, and no further links are followed
		colly.MaxDepth(1),
	)

	// On every a element which has href attribute call callback
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		link := e.Attr("href")
		// Print link
		fmt.Println(link)
		// Visit link found on page
		e.Request.Visit(link)
	})

	// Start scraping on https://en.wikipedia.org
	c.Visit("https://en.wikipedia.org/")
}
```

## File: `_examples/multipart/multipart.go`
```go
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"time"

	"github.com/gocolly/colly/v2"
)

func generateFormData() map[string][]byte {
	f, _ := os.Open("gocolly.jpg")
	defer f.Close()

	imgData, _ := io.ReadAll(f)

	return map[string][]byte{
		"firstname": []byte("one"),
		"lastname":  []byte("two"),
		"email":     []byte("onetwo@example.com"),
		"file":      imgData,
	}
}

func setupServer() {
	var handler http.HandlerFunc = func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("received request")
		err := r.ParseMultipartForm(10000000)
		if err != nil {
			fmt.Println("server: Error")
			w.WriteHeader(500)
			w.Write([]byte("<html><body>Internal Server Error</body></html>"))
			return
		}
		w.WriteHeader(200)
		fmt.Println("server: OK")
		w.Write([]byte("<html><body>Success</body></html>"))
	}

	go http.ListenAndServe(":8080", handler)
}

func main() {
	// Start a single route http server to post an image to.
	setupServer()

	c := colly.NewCollector(colly.AllowURLRevisit(), colly.MaxDepth(5))

	// On every a element which has href attribute call callback
	c.OnHTML("html", func(e *colly.HTMLElement) {
		fmt.Println(e.Text)
		time.Sleep(1 * time.Second)
		e.Request.PostMultipart("http://localhost:8080/", generateFormData())
	})

	// Before making a request print "Visiting ..."
	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Posting gocolly.jpg to", r.URL.String())
	})

	// Start scraping
	c.PostMultipart("http://localhost:8080/", generateFormData())
	c.Wait()
}
```

## File: `_examples/openedx_courses/openedx_courses.go`
```go
package main

import (
	"encoding/json"
	"fmt"
	"strings"
	"time"

	"github.com/gocolly/colly/v2"
)

// DATE_FORMAT default format date used in openedx
const DATE_FORMAT = "02 Jan, 2006"

// Course store openedx course data
type Course struct {
	CourseID  string
	Run       string
	Name      string
	Number    string
	StartDate *time.Time
	EndDate   *time.Time
	URL       string
}

func main() {
	// Instantiate default collector
	c := colly.NewCollector(
		// Using IndonesiaX as sample
		colly.AllowedDomains("indonesiax.co.id", "www.indonesiax.co.id"),

		// Cache responses to prevent multiple download of pages
		// even if the collector is restarted
		colly.CacheDir("./cache"),
	)

	courses := make([]Course, 0, 200)

	// On every a element which has href attribute call callback
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		link := e.Attr("href")
		if !strings.HasPrefix(link, "/courses/") {
			return
		}
		// start scraping the page under the link found
		e.Request.Visit(link)
	})

	c.OnHTML("div[class=main-container]", func(e *colly.HTMLElement) {
		if e.DOM.Find("section#course-info").Length() == 0 {
			return
		}
		title := strings.Split(e.ChildText(".course-info__title"), "\n")[0]
		course_id := e.ChildAttr("input[name=course_id]", "value")
		texts := e.ChildTexts("span[data-datetime]")
		start_date, _ := time.Parse(DATE_FORMAT, texts[0])
		end_date, _ := time.Parse(DATE_FORMAT, texts[1])
		var run string
		if len(strings.Split(course_id, "_")) > 1 {
			run = strings.Split(course_id, "_")[1]
		}
		course := Course{
			CourseID:  course_id,
			Run:       run,
			Name:      title,
			Number:    e.ChildText("span.course-number"),
			StartDate: &start_date,
			EndDate:   &end_date,
			URL:       fmt.Sprintf("/courses/%s/about", course_id),
		}
		courses = append(courses, course)
	})

	// Start scraping on https://openedxdomain/courses
	c.Visit("https://www.indonesiax.co.id/courses")

	// Convert results to JSON data if the scraping job has finished
	jsonData, err := json.MarshalIndent(courses, "", "  ")
	if err != nil {
		panic(err)
	}

	// Dump json to the standard output (can be redirected to a file)
	fmt.Println(string(jsonData))
}
```

## File: `_examples/parallel/parallel.go`
```go
package main

import (
	"fmt"

	"github.com/gocolly/colly/v2"
)

func main() {
	// Instantiate default collector
	c := colly.NewCollector(
		// MaxDepth is 2, so only the links on the scraped page
		// and links on those pages are visited
		colly.MaxDepth(2),
		colly.Async(),
	)

	// Limit the maximum parallelism to 2
	// This is necessary if the goroutines are dynamically
	// created to control the limit of simultaneous requests.
	//
	// Parallelism can be controlled also by spawning fixed
	// number of go routines.
	c.Limit(&colly.LimitRule{DomainGlob: "*", Parallelism: 2})

	// On every a element which has href attribute call callback
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		link := e.Attr("href")
		// Print link
		fmt.Println(link)
		// Visit link found on page on a new thread
		e.Request.Visit(link)
	})

	// Start scraping on https://en.wikipedia.org
	c.Visit("https://en.wikipedia.org/")
	// Wait until threads are finished
	c.Wait()
}
```

## File: `_examples/proxy_switcher/proxy_switcher.go`
```go
package main

import (
	"bytes"
	"log"

	"github.com/gocolly/colly/v2"
	"github.com/gocolly/colly/v2/proxy"
)

func main() {
	// Instantiate default collector
	c := colly.NewCollector(colly.AllowURLRevisit())

	// Rotate two socks5 proxies
	rp, err := proxy.RoundRobinProxySwitcher("socks5://127.0.0.1:1337", "socks5://127.0.0.1:1338")
	if err != nil {
		log.Fatal(err)
	}
	c.SetProxyFunc(rp)

	// Print the response
	c.OnResponse(func(r *colly.Response) {
		log.Printf("Proxy Address: %s\n", r.Request.ProxyURL)
		log.Printf("%s\n", bytes.Replace(r.Body, []byte("\n"), nil, -1))
	})

	// Fetch httpbin.org/ip five times
	for i := 0; i < 5; i++ {
		c.Visit("https://httpbin.org/ip")
	}
}
```

## File: `_examples/queue/queue.go`
```go
package main

import (
	"fmt"

	"github.com/gocolly/colly/v2"
	"github.com/gocolly/colly/v2/queue"
)

func main() {
	url := "https://httpbin.org/delay/1"

	// Instantiate default collector
	c := colly.NewCollector(colly.AllowURLRevisit())

	// create a request queue with 2 consumer threads
	q, _ := queue.New(
		2, // Number of consumer threads
		&queue.InMemoryQueueStorage{MaxSize: 10000}, // Use default queue storage
	)

	c.OnRequest(func(r *colly.Request) {
		fmt.Println("visiting", r.URL)
		if r.ID < 15 {
			r2, err := r.New("GET", fmt.Sprintf("%s?x=%v", url, r.ID), nil)
			if err == nil {
				q.AddRequest(r2)
			}
		}
	})

	for i := 0; i < 5; i++ {
		// Add URLs to the queue
		q.AddURL(fmt.Sprintf("%s?n=%d", url, i))
	}
	// Consume URLs
	q.Run(c)

}
```

## File: `_examples/random_delay/random_delay.go`
```go
package main

import (
	"fmt"
	"time"

	"github.com/gocolly/colly/v2"
	"github.com/gocolly/colly/v2/debug"
)

func main() {
	url := "https://httpbin.org/delay/2"

	// Instantiate default collector
	c := colly.NewCollector(
		// Attach a debugger to the collector
		colly.Debugger(&debug.LogDebugger{}),
		colly.Async(),
	)

	// Limit the number of threads started by colly to two
	// when visiting links which domains' matches "*httpbin.*" glob
	c.Limit(&colly.LimitRule{
		DomainGlob:  "*httpbin.*",
		Parallelism: 2,
		RandomDelay: 5 * time.Second,
	})

	// Start scraping in four threads on https://httpbin.org/delay/2
	for i := 0; i < 4; i++ {
		c.Visit(fmt.Sprintf("%s?n=%d", url, i))
	}
	// Start scraping on https://httpbin.org/delay/2
	c.Visit(url)
	// Wait until threads are finished
	c.Wait()
}
```

## File: `_examples/rate_limit/rate_limit.go`
```go
package main

import (
	"fmt"

	"github.com/gocolly/colly/v2"
	"github.com/gocolly/colly/v2/debug"
)

func main() {
	url := "https://httpbin.org/delay/2"

	// Instantiate default collector
	c := colly.NewCollector(
		// Turn on asynchronous requests
		colly.Async(),
		// Attach a debugger to the collector
		colly.Debugger(&debug.LogDebugger{}),
	)

	// Limit the number of threads started by colly to two
	// when visiting links which domains' matches "*httpbin.*" glob
	c.Limit(&colly.LimitRule{
		DomainGlob:  "*httpbin.*",
		Parallelism: 2,
		//Delay:      5 * time.Second,
	})

	// Start scraping in five threads on https://httpbin.org/delay/2
	for i := 0; i < 5; i++ {
		c.Visit(fmt.Sprintf("%s?n=%d", url, i))
	}
	// Wait until threads are finished
	c.Wait()
}
```

## File: `_examples/reddit/reddit.go`
```go
package main

import (
	"fmt"
	"os"
	"time"

	"github.com/gocolly/colly/v2"
)

type item struct {
	StoryURL  string
	Source    string
	comments  string
	CrawledAt time.Time
	Comments  string
	Title     string
}

func main() {
	stories := []item{}
	// Instantiate default collector
	c := colly.NewCollector(
		// Visit only domains: old.reddit.com
		colly.AllowedDomains("old.reddit.com"),
		// Parallelism
		colly.Async(true),
	)

	// On every a element which has .top-matter attribute call callback
	// This class is unique to the div that holds all information about a story
	c.OnHTML(".top-matter", func(e *colly.HTMLElement) {
		temp := item{}
		temp.StoryURL = e.ChildAttr("a[data-event-action=title]", "href")
		temp.Source = "https://old.reddit.com/r/programming/"
		temp.Title = e.ChildText("a[data-event-action=title]")
		temp.Comments = e.ChildAttr("a[data-event-action=comments]", "href")
		temp.CrawledAt = time.Now()
		stories = append(stories, temp)
	})

	// On every span tag with the class next-button
	c.OnHTML("span.next-button", func(h *colly.HTMLElement) {
		t := h.ChildAttr("a", "href")
		c.Visit(t)
	})

	// Set max Parallelism and introduce a Random Delay
	c.Limit(&colly.LimitRule{
		Parallelism: 2,
		RandomDelay: 5 * time.Second,
	})

	// Before making a request print "Visiting ..."
	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL.String())

	})

	// Crawl all reddits the user passes in
	reddits := os.Args[1:]
	for _, reddit := range reddits {
		c.Visit(reddit)

	}

	c.Wait()
	fmt.Println(stories)

}
```

## File: `_examples/request_context/request_context.go`
```go
package main

import (
	"fmt"

	"github.com/gocolly/colly/v2"
)

func main() {
	// Instantiate default collector
	c := colly.NewCollector()

	// Before making a request put the URL with
	// the key of "url" into the context of the request
	c.OnRequest(func(r *colly.Request) {
		r.Ctx.Put("url", r.URL.String())
	})

	// After making a request get "url" from
	// the context of the request
	c.OnResponse(func(r *colly.Response) {
		fmt.Println(r.Ctx.Get("url"))
	})

	// Start scraping on https://en.wikipedia.org
	c.Visit("https://en.wikipedia.org/")
}
```

## File: `_examples/scraper_server/scraper_server.go`
```go
package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gocolly/colly/v2"
)

type pageInfo struct {
	StatusCode int
	Links      map[string]int
}

func handler(w http.ResponseWriter, r *http.Request) {
	URL := r.URL.Query().Get("url")
	if URL == "" {
		log.Println("missing URL argument")
		return
	}
	log.Println("visiting", URL)

	c := colly.NewCollector()

	p := &pageInfo{Links: make(map[string]int)}

	// count links
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		link := e.Request.AbsoluteURL(e.Attr("href"))
		if link != "" {
			p.Links[link]++
		}
	})

	// extract status code
	c.OnResponse(func(r *colly.Response) {
		log.Println("response received", r.StatusCode)
		p.StatusCode = r.StatusCode
	})
	c.OnError(func(r *colly.Response, err error) {
		log.Println("error:", r.StatusCode, err)
		p.StatusCode = r.StatusCode
	})

	c.Visit(URL)

	// dump results
	b, err := json.Marshal(p)
	if err != nil {
		log.Println("failed to serialize response:", err)
		return
	}
	w.Header().Add("Content-Type", "application/json")
	w.Write(b)
}

func main() {
	// example usage: curl -s 'http://127.0.0.1:7171/?url=http://go-colly.org/'
	addr := ":7171"

	http.HandleFunc("/", handler)

	log.Println("listening on", addr)
	log.Fatal(http.ListenAndServe(addr, nil))
}
```

## File: `_examples/shopify_sitemap/shopify_sitemap.go`
```go
package main

import (
	"fmt"

	"github.com/gocolly/colly/v2"
)

func main() {
	// Array containing all the known URLs in a sitemap
	knownUrls := []string{}

	// Create a Collector specifically for Shopify
	c := colly.NewCollector(colly.AllowedDomains("www.shopify.com"))

	// Create a callback on the XPath query searching for the URLs
	c.OnXML("//urlset/url/loc", func(e *colly.XMLElement) {
		knownUrls = append(knownUrls, e.Text)
	})

	// Start the collector
	c.Visit("https://www.shopify.com/sitemap.xml")

	fmt.Println("All known URLs:")
	for _, url := range knownUrls {
		fmt.Println("\t", url)
	}
	fmt.Println("Collected", len(knownUrls), "URLs")
}
```

## File: `_examples/url_filter/url_filter.go`
```go
package main

import (
	"fmt"
	"regexp"

	"github.com/gocolly/colly/v2"
)

func main() {
	// Instantiate default collector
	c := colly.NewCollector(
		// Visit only root url and urls which start with "e" or "h" on httpbin.org
		colly.URLFilters(
			regexp.MustCompile("http://httpbin\\.org/(|e.+)$"),
			regexp.MustCompile("http://httpbin\\.org/h.+"),
		),
	)

	// On every a element which has href attribute call callback
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		link := e.Attr("href")
		// Print link
		fmt.Printf("Link found: %q -> %s\n", e.Text, link)
		// Visit link found on page
		// Only those links are visited which are matched by  any of the URLFilter regexps
		c.Visit(e.Request.AbsoluteURL(link))
	})

	// Before making a request print "Visiting ..."
	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL.String())
	})

	// Start scraping on http://httpbin.org
	c.Visit("http://httpbin.org/")
}
```

## File: `_examples/xkcd_store/xkcd_store.go`
```go
package main

import (
	"encoding/csv"
	"log"
	"os"

	"github.com/gocolly/colly/v2"
)

func main() {
	fName := "xkcd_store_items.csv"
	file, err := os.Create(fName)
	if err != nil {
		log.Fatalf("Cannot create file %q: %s\n", fName, err)
		return
	}
	defer file.Close()
	writer := csv.NewWriter(file)
	defer writer.Flush()
	// Write CSV header
	writer.Write([]string{"Name", "Price", "URL", "Image URL"})

	// Instantiate default collector
	c := colly.NewCollector(
		// Allow requests only to store.xkcd.com
		colly.AllowedDomains("store.xkcd.com"),
	)

	// Extract product details
	c.OnHTML(".product-grid-item", func(e *colly.HTMLElement) {
		writer.Write([]string{
			e.ChildAttr("a", "title"),
			e.ChildText("span"),
			e.Request.AbsoluteURL(e.ChildAttr("a", "href")),
			"https:" + e.ChildAttr("img", "src"),
		})
	})

	// Find and visit next page links
	c.OnHTML(`.next a[href]`, func(e *colly.HTMLElement) {
		e.Request.Visit(e.Attr("href"))
	})

	c.Visit("https://store.xkcd.com/collections/everything")

	log.Printf("Scraping finished, check file %q for results\n", fName)

	// Display collector's statistics
	log.Println(c)
}
```

