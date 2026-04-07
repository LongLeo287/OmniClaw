---
id: firecrawl-go
type: knowledge
owner: OA_Triage
---
# firecrawl-go
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Firecrawl Go SDK

The Firecrawl Go SDK is a library that allows you to easily scrape and crawl websites, and output the data in a format ready for use with language models (LLMs). It provides a simple and intuitive interface for interacting with the Firecrawl API.

## Installation

To install the Firecrawl Go SDK, you can

```bash
go get github.com/mendableai/firecrawl-go/v2
```

## Usage

1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
2. Set the API key as an environment variable named `FIRECRAWL_API_KEY` or pass it as a parameter to the `FirecrawlApp` class.


Here's an example of how to use the SDK with error handling:

```go
package main

import (
	"encoding/json"
	"fmt"
	"log"

	"github.com/mendableai/firecrawl-go/v2"
)

func main() {
	// Initialize the FirecrawlApp with your API key and optional URL
	app, err := firecrawl.NewFirecrawlApp("YOUR_API_KEY", "YOUR_API_URL")
	if err != nil {
		log.Fatalf("Failed to initialize FirecrawlApp: %v", err)
	}

	// Scrape a single URL
	scrapeResult, err := app.ScrapeURL("example.com", nil)
	if err != nil {
		log.Fatalf("Failed to scrape URL: %v", err)
	}
	fmt.Println(scrapeResult.Markdown)

	// Crawl a website
	idempotencyKey := "idempotency-key" // optional idempotency key
	crawlParams := &firecrawl.CrawlParams{
		ExcludePaths: []string{"blog/*"},
		MaxDepth:     prt(2),
	}
	crawlResult, err := app.CrawlURL("example.com", crawlParams, &idempotencyKey)
	if err != nil {
		log.Fatalf("Failed to crawl URL: %v", err)
	}
	jsonCrawlResult, err := json.MarshalIndent(crawlResult, "", "  ")
	if err != nil {
		log.Fatalf("Failed to marshal crawl result: %v", err)
	}
	fmt.Println(string(jsonCrawlResult))
}
```

### Scraping a URL

To scrape a single URL with error handling, use the `ScrapeURL` method. It takes the URL as a parameter and returns the scraped data as a dictionary.

```go
url := "https://example.com"
scrapedData, err := app.ScrapeURL(url, nil)
if err != nil {
	log.Fatalf("Failed to scrape URL: %v", err)
}
fmt.Println(scrapedData)
```

### Extracting structured data from a URL

With LLM extraction, you can easily extract structured data from any URL. Here is how you to use it:

```go
jsonSchema := map[string]any{
	"type": "object",
	"properties": map[string]any{
		"top": map[string]any{
			"type": "array",
			"items": map[string]any{
				"type": "object",
				"properties": map[string]any{
					"title":       map[string]string{"type": "string"},
					"points":      map[string]string{"type": "number"},
					"by":          map[string]string{"type": "string"},
					"commentsURL": map[string]string{"type": "string"},
				},
				"required": []string{"title", "points", "by", "commentsURL"},
			},
			"minItems":    5,
			"maxItems":    5,
			"description": "Top 5 stories on Hacker News",
		},
	},
	"required": []string{"top"},
}

llmExtractionParams := map[string]any{
	"extractorOptions": firecrawl.ExtractorOptions{
		ExtractionSchema: jsonSchema,
	},
}

scrapeResult, err := app.ScrapeURL("https://news.ycombinator.com", llmExtractionParams)
if err != nil {
	log.Fatalf("Failed to perform LLM extraction: %v", err)
}
fmt.Println(scrapeResult)
```

### Crawling a Website

To crawl a website, use the `CrawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.

```go
response, err := app.CrawlURL("https://roastmywebsite.ai", nil,nil)

if err != nil {
 log.Fatalf("Failed to crawl URL: %v", err)
}

fmt.Println(response)
```

### Asynchronous Crawl

To initiate an asynchronous crawl of a website, utilize the `AsyncCrawlURL` method. This method requires the starting URL and optional parameters as inputs. The `params` argument enables you to define various settings for the asynchronous crawl, such as the maximum number of pages to crawl, permitted domains, and the output format. Upon successful initiation, this method returns an ID, which is essential for subsequently checking the status of the crawl.

```go
response, err := app.AsyncCrawlURL("https://roastmywebsite.ai", nil, nil)

if err != nil {
  log.Fatalf("Failed to crawl URL: %v", err)
}

fmt.Println(response) 
```


### Checking Crawl Status

To check the status of a crawl job, use the `CheckCrawlStatus` method. It takes the crawl ID as a parameter and returns the current status of the crawl job.

```go
status, err := app.CheckCrawlStatus(id)
if err != nil {
	log.Fatalf("Failed to check crawl status: %v", err)
}
fmt.Println(status)
```

### Canceling a Crawl Job
To cancel a crawl job, use the `CancelCrawlJob` method. It takes the job ID as a parameter and returns the cancellation status of the crawl job.

```go
canceled, err := app.CancelCrawlJob(jobId)
if err != nil {
	log.Fatalf("Failed to cancel crawl job: %v", err)
}
fmt.Println(canceled)
```

## Error Handling

The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.

## Contributing

Contributions to the Firecrawl Go SDK are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

The Firecrawl Go SDK is licensed under the MIT License. This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the SDK, subject to the following conditions:

- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Please note that while this SDK is MIT licensed, it is part of a larger project which may be under different licensing terms. Always refer to the license information in the root directory of the main project for overall licensing details.

```

### File: firecrawl.go
```go
// Package firecrawl provides a client for interacting with the Firecrawl API.
package firecrawl

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"math"
	"net/http"
	"os"
	"time"
)

type StringOrStringSlice []string

func (s *StringOrStringSlice) UnmarshalJSON(data []byte) error {
	var single string
	if err := json.Unmarshal(data, &single); err == nil {
		*s = []string{single}
		return nil
	}

	var list []string
	if err := json.Unmarshal(data, &list); err == nil {
		*s = list
		return nil
	}

	return fmt.Errorf("field is neither a string nor a list of strings")
}

// FirecrawlDocumentMetadata represents metadata for a Firecrawl document
type FirecrawlDocumentMetadata struct {
	Title             *string              `json:"title,omitempty"`
	Description       *StringOrStringSlice `json:"description,omitempty"`
	Language          *StringOrStringSlice `json:"language,omitempty"`
	Keywords          *StringOrStringSlice `json:"keywords,omitempty"`
	Robots            *StringOrStringSlice `json:"robots,omitempty"`
	OGTitle           *StringOrStringSlice `json:"ogTitle,omitempty"`
	OGDescription     *StringOrStringSlice `json:"ogDescription,omitempty"`
	OGURL             *StringOrStringSlice `json:"ogUrl,omitempty"`
	OGImage           *StringOrStringSlice `json:"ogImage,omitempty"`
	OGAudio           *StringOrStringSlice `json:"ogAudio,omitempty"`
	OGDeterminer      *StringOrStringSlice `json:"ogDeterminer,omitempty"`
	OGLocale          *StringOrStringSlice `json:"ogLocale,omitempty"`
	OGLocaleAlternate []*string            `json:"ogLocaleAlternate,omitempty"`
	OGSiteName        *StringOrStringSlice `json:"ogSiteName,omitempty"`
	OGVideo           *StringOrStringSlice `json:"ogVideo,omitempty"`
	DCTermsCreated    *StringOrStringSlice `json:"dctermsCreated,omitempty"`
	DCDateCreated     *StringOrStringSlice `json:"dcDateCreated,omitempty"`
	DCDate            *StringOrStringSlice `json:"dcDate,omitempty"`
	DCTermsType       *StringOrStringSlice `json:"dctermsType,omitempty"`
	DCType            *StringOrStringSlice `json:"dcType,omitempty"`
	DCTermsAudience   *StringOrStringSlice `json:"dctermsAudience,omitempty"`
	DCTermsSubject    *StringOrStringSlice `json:"dctermsSubject,omitempty"`
	DCSubject         *StringOrStringSlice `json:"dcSubject,omitempty"`
	DCDescription     *StringOrStringSlice `json:"dcDescription,omitempty"`
	DCTermsKeywords   *StringOrStringSlice `json:"dctermsKeywords,omitempty"`
	ModifiedTime      *StringOrStringSlice `json:"modifiedTime,omitempty"`
	PublishedTime     *StringOrStringSlice `json:"publishedTime,omitempty"`
	ArticleTag        *StringOrStringSlice `json:"articleTag,omitempty"`
	ArticleSection    *StringOrStringSlice `json:"articleSection,omitempty"`
	URL               *string              `json:"url,omitempty"`
	ScrapeID          *string              `json:"scrapeId,omitempty"`
	SourceURL         *string              `json:"sourceURL,omitempty"`
	StatusCode        *int                 `json:"statusCode,omitempty"`
	Error             *string              `json:"error,omitempty"`
}

// JsonOptions represents the options for JSON extraction
type JsonOptions struct {
	Schema       map[string]any `json:"schema,omitempty"`
	SystemPrompt *string        `json:"systemPrompt,omitempty"`
	Prompt       *string        `json:"prompt,omitempty"`
}

// FirecrawlDocument represents a document in Firecrawl
type FirecrawlDocument struct {
	Markdown   string                     `json:"markdown,omitempty"`
	HTML       string                     `json:"html,omitempty"`
	RawHTML    string                     `json:"rawHtml,omitempty"`
	Screenshot string                     `json:"screenshot,omitempty"`
	JSON       map[string]any             `json:"json,omitempty"`
	Links      []string                   `json:"links,omitempty"`
	Metadata   *FirecrawlDocumentMetadata `json:"metadata,omitempty"`
}

// ScrapeParams represents the parameters for a scrape request.
type ScrapeParams struct {
	Formats         []string           `json:"formats,omitempty"`
	Headers         *map[string]string `json:"headers,omitempty"`
	IncludeTags     []string           `json:"includeTags,omitempty"`
	ExcludeTags     []string           `json:"excludeTags,omitempty"`
	OnlyMainContent *bool              `json:"onlyMainContent,omitempty"`
	WaitFor         *int               `json:"waitFor,omitempty"`
	ParsePDF        *bool              `json:"parsePDF,omitempty"`
	Timeout         *int               `json:"timeout,omitempty"`
	MaxAge          *int               `json:"maxAge,omitempty"`
	JsonOptions     *JsonOptions       `json:"jsonOptions,omitempty"`
}

// ScrapeResponse represents the response for scraping operations
type ScrapeResponse struct {
	Success bool               `json:"success"`
	Data    *FirecrawlDocument `json:"data,omitempty"`
}

// CrawlParams represents the parameters for a crawl request.
type CrawlParams struct {
	ScrapeOptions         ScrapeParams `json:"scrapeOptions"`
	Webhook               *string      `json:"webhook,omitempty"`
	Limit                 *int         `json:"limit,omitempty"`
	IncludePaths          []string     `json:"includePaths,omitempty"`
	ExcludePaths          []string     `json:"excludePaths,omitempty"`
	MaxDepth              *int         `json:"maxDepth,omitempty"`
	AllowBackwardLinks    *bool        `json:"allowBackwardLinks,omitempty"`
	AllowExternalLinks    *bool        `json:"allowExternalLinks,omitempty"`
	IgnoreSitemap         *bool        `json:"ignoreSitemap,omitempty"`
	IgnoreQueryParameters *bool        `json:"ignoreQueryParameters,omitempty"`
}

// CrawlResponse represents the response for crawling operations
type CrawlResponse struct {
	Success bool   `json:"success"`
	ID      string `json:"id,omitempty"`
	URL     string `json:"url,omitempty"`
}

// CrawlStatusResponse (old JobStatusResponse) represents the response for checking crawl job
type CrawlStatusResponse struct {
	Status      string               `json:"status"`
	Total       int                  `json:"total,omitempty"`
	Completed   int                  `json:"completed,omitempty"`
	CreditsUsed int                  `json:"creditsUsed,omitempty"`
	ExpiresAt   string               `json:"expiresAt,omitempty"`
	Next        *string              `json:"next,omitempty"`
	Data        []*FirecrawlDocument `json:"data,omitempty"`
}

// CancelCrawlJobResponse represents the response for canceling a crawl job
type CancelCrawlJobResponse struct {
	Success bool   `json:"success"`
	Status  string `json:"status"`
}

// MapParams represents the parameters for a map request.
type MapParams struct {
	IncludeSubdomains *bool   `json:"includeSubdomains,omitempty"`
	Search            *string `json:"search,omitempty"`
	IgnoreSitemap     *bool   `json:"ignoreSitemap,omitempty"`
	Limit             *int    `json:"limit,omitempty"`
}

// MapResponse represents the response for mapping operations
type MapResponse struct {
	Success bool     `json:"success"`
	Links   []string `json:"links,omitempty"`
	Error   string   `json:"error,omitempty"`
}

// requestOptions represents options for making requests.
type requestOptions struct {
	retries int
	backoff int
}

// requestOption is a functional option type for requestOptions.
type requestOption func(*requestOptions)

// newRequestOptions creates a new requestOptions instance with the provided options.
//
// Parameters:
//   - opts: Optional request options.
//
// Returns:
//   - *requestOptions: A new instance of requestOptions with the provided options.
func newRequestOptions(opts ...requestOption) *requestOptions {
	options := &requestOptions{retries: 1}
	for _, opt := range opts {
		opt(options)
	}
	return options
}

// withRetries sets the number of retries for a request.
//
// Parameters:
//   - retries: The number of retries to be performed.
//
// Returns:
//   - requestOption: A functional option that sets the number of retries for a request.
func withRetries(retries int) requestOption {
	return func(opts *requestOptions) {
		opts.retries = retries
	}
}

// withBackoff sets the backoff interval for a request.
//
// Parameters:
//   - backoff: The backoff interval (in milliseconds) to be used for retries.
//
// Returns:
//   - requestOption: A functional option that sets the backoff interval for a request.
func withBackoff(backoff int) requestOption {
	return func(opts *requestOptions) {
		opts.backoff = backoff
	}
}

// FirecrawlApp represents a client for the Firecrawl API.
type FirecrawlApp struct {
	APIKey  string
	APIURL  string
	Client  *http.Client
	Version string
}

// NewFirecrawlApp creates a new instance of FirecrawlApp with the provided API key and API URL.
// If the API key or API URL is not provided, it attempts to retrieve them from environment variables.
// If the API key is still not found, it returns an error.
//
// Parameters:
//   - apiKey: The API key for authenticating with the Firecrawl API. If empty, it will be retrieved from the FIRECRAWL_API_KEY environment variable.
//   - apiURL: The base URL for the Firecrawl API. If empty, it will be retrieved from the FIRECRAWL_API_URL environment variable, defaulting to "https://api.firecrawl.dev".
//   - timeout: The timeout for the HTTP client. If not provided, it will default to 60 seconds.
//
// Returns:
//   - *FirecrawlApp: A new instance of FirecrawlApp configured with the provided or retrieved API key and API URL.
//   - error: An error if the API key is not provided or retrieved.
func NewFirecrawlApp(apiKey, apiURL string, timeout ...time.Duration) (*FirecrawlApp, error) {
	if apiKey == "" {
		apiKey = os.Getenv("FIRECRAWL_API_KEY")
		if apiKey == "" {
			return nil, fmt.Errorf("no API key provided")
		}
	}

	if apiURL == "" {
		apiURL = os.Getenv("FIRECRAWL_API_URL")
		if apiURL == "" {
			apiURL = "https://api.firecrawl.dev"
		}
	}

	t := 120 * time.Second // default
	if len(timeout) > 0 {
		t = timeout[0]
	}

	client := &http.Client{
		Timeout:   t,
		Transport: http.DefaultTransport,
	}

	return &FirecrawlApp{
		APIKey: apiKey,
		APIURL: apiURL,
		Client: client,
	}, nil
}

// ScrapeURL scrapes the content of the specified URL using the Firecrawl API.
//
// Parameters:
//   - url: The URL to be scraped.
//   - params: Optional parameters for the scrape request, including extractor options for LLM extraction.
//
// Returns:
//   - *FirecrawlDocument or *FirecrawlDocumentV0: The scraped document data depending on the API version.
//   - error: An error if the scrape request fails.
func (app *FirecrawlApp) ScrapeURL(url string, params *ScrapeParams) (*FirecrawlDocument, error) {
	headers := app.prepareHeaders(nil)
	scrapeBody := map[string]any{"url": url}

	// if params != nil {
	// 	if extractorOptions, ok := params["extractorOptions"].(ExtractorOptions); ok {
	// 		if schema, ok := extractorOptions.ExtractionSchema.(interface{ schema() any }); ok {
	// 			extractorOptions.ExtractionSchema = schema.schema()
	// 		}
	// 		if extractorOptions.Mode == "" {
	// 			extractorOptions.Mode = "llm-extraction"
	// 		}
	// 		scrapeBody["extractorOptions"] = extractorOptions
	// 	}

	// 	for key, value := range params {
	// 		if key != "extractorOptions" {
	// 			scrapeBody[key] = value
	// 		}
	// 	}
	// }

	if params != nil {
		if params.Formats != nil {
			scrapeBody["formats"] = params.Formats
		}
		if params.Headers != nil {
			scrapeBody["headers"] = params.Headers
		}
		if params.IncludeTags != nil {
			scrapeBody["includeTags"] = params.IncludeTags
		}
		if params.ExcludeTags != nil {
			scrapeBody["excludeTags"] = params.ExcludeTags
		}
		if params.OnlyMainContent != nil {
			scrapeBody["onlyMainContent"] = params.OnlyMainContent
		}
		if params.WaitFor != nil {
			scrapeBody["waitFor"] = params.WaitFor
		}
		if params.ParsePDF != nil {
			scrapeBody["parsePDF"] = params.ParsePDF
		}
		if params.Timeout != nil {
			scrapeBody["timeout"] = params.Timeout
		}
		if params.MaxAge != nil {
			scrapeBody["maxAge"] = params.MaxAge
		}
		if params.JsonOptions != nil {
			scrapeBody["jsonOptions"] = params.JsonOptions
		}
	}

	resp, err := app.makeRequest(
		http.MethodPost,
		fmt.Sprintf("%s/v1/scrape", app.APIURL),
		scrapeBody,
		headers,
		"scrape URL",
	)
	if err != nil {
		return nil, err
	}

	var scrapeResponse ScrapeResponse
	err = json.Unmarshal(resp, &scrapeResponse)

	if scrapeResponse.Success {
		return scrapeResponse.Data, nil
	}

	if err != nil {
		return nil, err
	}

	return nil, fmt.Errorf("failed to scrape URL")
}

// CrawlURL starts a crawl job for the specified URL using the Firecrawl API.
//
// Parameters:
//   - url: The URL to crawl.
//   - params: Optional parameters for the crawl request.
//   - idempotencyKey: An optional idempotency key to ensure the request is idempotent (can be nil).
//   - pollInterval: An optional interval (in seconds) at which to poll the job status. Default is 2 seconds.
//
// Returns:
//   - CrawlStatusResponse: The crawl result if the job is completed.
//   - error: An error if the crawl request fails.
func (app *FirecrawlApp) CrawlURL(url string, params *CrawlParams, idempotencyKey *string, pollInterval ...int) (*CrawlStatusResponse, error) {
	var key string
	if idempotencyKey != nil {
		key = *idempotencyKey
	}

	headers := app.prepareHeaders(&key)
	crawlBody := map[string]any{"url": url}

	if params != nil {
		if params.ScrapeOptions.Formats != nil {
			crawlBody["scrapeOptions"] = params.ScrapeOptions
		}
		if params.Webhook != nil {
			crawlBody["webhook"] = params.Webhook
		}
		if params.Limit != nil {
			crawlBody["limit"] = params.Limit
		}
		if params.IncludePaths != nil {
			crawlBody["includePaths"] = params.IncludePaths
		}
		if params.ExcludePaths != nil {
			crawlBody["excludePaths"] = params.ExcludePaths
		}
		if params.MaxDepth != nil {
			crawlBody["maxDepth"] = params.MaxDepth
		}
		if params.AllowBackwardLinks != nil {
			crawlBody["allowBackwardLinks"] = params.AllowBackwardLinks
		}
		if params.AllowExternalLinks != nil {
			crawlBody["allowExternalLinks"] = params.AllowExternalLinks
		}
		if params.IgnoreSitemap != nil {
			crawlBody["ignoreSitemap"] = params.IgnoreSitemap
		}
		if params.IgnoreQueryParameters != nil {
			crawlBody["ignoreQueryParameters"] = params.IgnoreQueryParameters
		}
	}

	actualPollInterval := 2
	if len(pollInterval) > 0 {
		actualPollInterval = pollInterval[0]
	}

	resp, err := app.makeRequest(
		http.MethodPost,
		fmt.Sprintf("%s/v1/crawl", app.APIURL),
		crawlBody,
		headers,
		"start crawl job",
		withRetries(3),
		withBackoff(500),
	)
	if err != nil {
		return nil, err
	}

	var crawlResponse CrawlResponse
	err = json.Unmarshal(resp, &crawlResponse)
	if err != nil {
		return nil, err
	}

	return app.monitorJobStatus(crawlResponse.ID, headers, actualPollInterval)
}

// CrawlURL starts a crawl job for the specified URL using the Firecrawl API.
//
// Parameters:
//   - url: The URL to crawl.
//   - params: Optional parameters for the crawl request.
//   - idempotencyKey: An optional idempotency key to ensure the request is idempotent.
//
// R
... [TRUNCATED]
```

### File: firecrawl_test.go
```go
package firecrawl

import (
	"log"
	"os"
	"testing"
	"time"

	"github.com/google/uuid"
	"github.com/joho/godotenv"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

var API_URL string
var TEST_API_KEY string

func ptr[T any](v T) *T {
	return &v
}

func init() {
	err := godotenv.Load(".env")
	if err != nil {
		log.Fatalf("Error loading .env file: %v", err)
	}
	API_URL = os.Getenv("API_URL")
	TEST_API_KEY = os.Getenv("TEST_API_KEY")
}

func TestNoAPIKey(t *testing.T) {
	_, err := NewFirecrawlApp("", API_URL)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "no API key provided")
}

func TestScrapeURLInvalidAPIKey(t *testing.T) {
	app, err := NewFirecrawlApp("invalid_api_key", API_URL)
	require.NoError(t, err)

	_, err = app.ScrapeURL("https://firecrawl.dev", nil)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "Unexpected error during scrape URL: Status code 401. Unauthorized: Invalid token")
}

func TestBlocklistedURL(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	_, err = app.ScrapeURL("https://facebook.com/fake-test", nil)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "Status code 403")
}

func TestScrapeURLE2E(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	response, err := app.ScrapeURL("https://www.scrapethissite.com", nil)
	require.NoError(t, err)
	assert.NotNil(t, response)

	assert.Contains(t, response.Markdown, "# Scrape This Site")
	assert.NotEqual(t, response.Markdown, "")
	assert.NotNil(t, response.Metadata)
	assert.Equal(t, response.HTML, "")
}

func TestSuccessfulResponseWithValidAPIKeyAndIncludeHTML(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	params := ScrapeParams{
		Formats:         []string{"markdown", "html", "rawHtml", "screenshot", "links"},
		Headers:         ptr(map[string]string{"x-key": "test"}),
		IncludeTags:     []string{"h1"},
		ExcludeTags:     []string{"h2"},
		OnlyMainContent: ptr(true),
		Timeout:         ptr(30000),
		WaitFor:         ptr(1000),
	}

	response, err := app.ScrapeURL("https://www.scrapethissite.com", &params)
	require.NoError(t, err)
	assert.NotNil(t, response)

	assert.Contains(t, response.Markdown, "# Scrape This Site")
	assert.Contains(t, response.HTML, "<h1")
	assert.Contains(t, response.RawHTML, "<h1")
	assert.NotNil(t, response.Screenshot)
	assert.NotEmpty(t, response.Screenshot)
	assert.Contains(t, response.Screenshot, "https://")
	assert.NotNil(t, response.Links)
	assert.NotNil(t, response.Metadata)
}

func TestSuccessfulResponseForValidScrapeWithPDFFile(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	response, err := app.ScrapeURL("https://arxiv.org/pdf/astro-ph/9301001.pdf", nil)
	require.NoError(t, err)
	assert.NotNil(t, response)

	assert.Contains(t, response.Markdown, "We present spectrophotometric observations of the Broad Line Radio Galaxy")
	assert.NotNil(t, response.Metadata)
}

func TestSuccessfulResponseForValidScrapeWithPDFFileWithoutExplicitExtension(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	response, err := app.ScrapeURL("https://arxiv.org/pdf/astro-ph/9301001", nil)
	require.NoError(t, err)
	assert.NotNil(t, response)

	assert.Contains(t, response.Markdown, "We present spectrophotometric observations of the Broad Line Radio Galaxy")
	assert.NotNil(t, response.Metadata)
}

func TestCrawlURLInvalidAPIKey(t *testing.T) {
	app, err := NewFirecrawlApp("invalid_api_key", API_URL)
	require.NoError(t, err)

	_, err = app.CrawlURL("https://firecrawl.dev", nil, nil)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "Unexpected error during start crawl job: Status code 401. Unauthorized: Invalid token")
}

func TestShouldReturnErrorForBlocklistedURL(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	_, err = app.CrawlURL("https://twitter.com/fake-test", nil, nil)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "Status code 403")
}

func TestCrawlURLE2E(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	response, err := app.CrawlURL("https://www.scrapethissite.com", nil, nil)
	require.NoError(t, err)
	assert.NotNil(t, response)

	assert.Greater(t, response.Total, 0)
	assert.Greater(t, response.Completed, 0)
	assert.Greater(t, response.CreditsUsed, 0)
	assert.NotEmpty(t, response.ExpiresAt)
	assert.Equal(t, response.Status, "completed")

	data := response.Data
	assert.IsType(t, []*FirecrawlDocument{}, data)

	assert.Greater(t, len(data), 0)
	assert.Contains(t, data[0].Markdown, "# Scrape This Site")
	assert.NotNil(t, data[0].Metadata)
}

func TestCrawlURLWithOptionsE2E(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	response, err := app.CrawlURL("https://www.scrapethissite.com",
		&CrawlParams{
			ExcludePaths:       []string{"blog/*"},
			IncludePaths:       []string{"/"},
			MaxDepth:           ptr(2),
			IgnoreSitemap:      ptr(true),
			Limit:              ptr(10),
			AllowBackwardLinks: ptr(true),
			AllowExternalLinks: ptr(true),
			ScrapeOptions: ScrapeParams{
				Formats:         []string{"markdown", "html", "rawHtml", "screenshot", "links"},
				Headers:         ptr(map[string]string{"x-key": "test"}),
				IncludeTags:     []string{"h1"},
				ExcludeTags:     []string{"h2"},
				OnlyMainContent: ptr(true),
				WaitFor:         ptr(1000),
			},
		},
		nil,
	)
	require.NoError(t, err)
	assert.NotNil(t, response)

	assert.Greater(t, response.Total, 0)
	assert.Greater(t, response.Completed, 0)
	assert.Greater(t, response.CreditsUsed, 0)
	assert.NotEmpty(t, response.ExpiresAt)
	assert.Equal(t, response.Status, "completed")

	data := response.Data
	assert.IsType(t, []*FirecrawlDocument{}, data)

	assert.Greater(t, len(data), 0)
	assert.Contains(t, data[0].Markdown, "# Scrape This Site")
	assert.NotNil(t, data[0].Metadata)
	assert.Contains(t, data[0].HTML, "<h1")
	assert.Contains(t, data[0].RawHTML, "<h1")
	assert.Contains(t, data[0].Screenshot, "https://")
	assert.NotNil(t, data[0].Links)
	assert.NotNil(t, data[0].Metadata.Title)
	assert.NotNil(t, data[0].Metadata.Description)
	assert.NotNil(t, data[0].Metadata.Language)
	assert.NotNil(t, data[0].Metadata.SourceURL)
	assert.NotNil(t, data[0].Metadata.StatusCode)
	assert.Equal(t, 200, *data[0].Metadata.StatusCode)
	assert.Empty(t, data[0].Metadata.Error)
}

func TestCrawlURLWithIdempotencyKeyE2E(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	uniqueIdempotencyKey := uuid.New().String()
	params := &CrawlParams{
		ExcludePaths: []string{"blog/*"},
		Limit:        ptr(10),
	}
	response, err := app.CrawlURL("https://www.scrapethissite.com", params, &uniqueIdempotencyKey)
	require.NoError(t, err)
	assert.NotNil(t, response)

	data := response.Data
	require.Greater(t, len(data), 0)
	require.IsType(t, []*FirecrawlDocument{}, data)
	assert.Contains(t, data[0].Markdown, "# Scrape This Site")

	_, err = app.CrawlURL("https://firecrawl.dev", params, &uniqueIdempotencyKey)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "Conflict: Failed to start crawl job due to a conflict. Idempotency key already used")
}

func TestAsyncCrawlURLE2E(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	response, err := app.AsyncCrawlURL("https://www.scrapethissite.com", nil, nil)
	require.NoError(t, err)
	assert.NotNil(t, response)

	assert.NotEmpty(t, response.ID)
	assert.NotEmpty(t, response.URL)
	assert.True(t, response.Success)
}

func TestAsyncCrawlURLWithOptionsE2E(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	response, err := app.AsyncCrawlURL("https://www.scrapethissite.com",
		&CrawlParams{
			ExcludePaths:       []string{"blog/*"},
			IncludePaths:       []string{"/"},
			MaxDepth:           ptr(2),
			IgnoreSitemap:      ptr(true),
			Limit:              ptr(10),
			AllowBackwardLinks: ptr(true),
			AllowExternalLinks: ptr(true),
			ScrapeOptions: ScrapeParams{
				Formats:         []string{"markdown", "html", "rawHtml", "screenshot", "links"},
				Headers:         ptr(map[string]string{"x-key": "test"}),
				IncludeTags:     []string{"h1"},
				ExcludeTags:     []string{"h2"},
				OnlyMainContent: ptr(true),
				WaitFor:         ptr(1000),
			},
		},
		nil,
	)
	require.NoError(t, err)
	assert.NotNil(t, response)

	assert.NotEmpty(t, response.ID)
	assert.NotEmpty(t, response.URL)
	assert.True(t, response.Success)
}

func TestAsyncCrawlURLWithIdempotencyKeyE2E(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	uniqueIdempotencyKey := uuid.New().String()
	params := &CrawlParams{
		ExcludePaths: []string{"blog/*"},
	}
	response, err := app.AsyncCrawlURL("https://www.scrapethissite.com", params, &uniqueIdempotencyKey)
	require.NoError(t, err)
	assert.NotNil(t, response)
	assert.NotNil(t, response.ID)
	assert.NotNil(t, response.URL)
	assert.True(t, response.Success)

	_, err = app.AsyncCrawlURL("https://firecrawl.dev", params, &uniqueIdempotencyKey)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "Conflict: Failed to start crawl job due to a conflict. Idempotency key already used")
}

func TestCheckCrawlStatusE2E(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	params := &CrawlParams{
		ScrapeOptions: ScrapeParams{
			Formats: []string{"markdown", "html", "rawHtml", "screenshot", "links"},
		},
	}
	asyncCrawlResponse, err := app.AsyncCrawlURL("https://firecrawl.dev", params, nil)
	require.NoError(t, err)
	assert.NotNil(t, asyncCrawlResponse)

	const maxChecks = 15
	checks := 0

	for {
		if checks >= maxChecks {
			break
		}

		time.Sleep(5 * time.Second) // wait for 5 seconds

		response, err := app.CheckCrawlStatus(asyncCrawlResponse.ID)
		require.NoError(t, err)
		assert.NotNil(t, response)

		assert.GreaterOrEqual(t, len(response.Data), 0)
		assert.GreaterOrEqual(t, response.Total, 0)
		assert.GreaterOrEqual(t, response.CreditsUsed, 0)

		if response.Status == "completed" {
			break
		}

		checks++
	}

	// Final check after loop or if completed
	response, err := app.CheckCrawlStatus(asyncCrawlResponse.ID)
	require.NoError(t, err)
	assert.NotNil(t, response)

	assert.Equal(t, "completed", response.Status)
	assert.Greater(t, len(response.Data), 0)
	assert.Greater(t, response.Total, 0)
	assert.Greater(t, response.Completed, 0)
	assert.Greater(t, response.CreditsUsed, 0)
	assert.NotNil(t, response.Data[0].Markdown)
	assert.Contains(t, response.Data[0].HTML, "<div")
	assert.Contains(t, response.Data[0].RawHTML, "<div")
	assert.Contains(t, response.Data[0].Screenshot, "https://")
	assert.NotNil(t, response.Data[0].Links)
	assert.Greater(t, len(response.Data[0].Links), 0)
	assert.NotNil(t, response.Data[0].Metadata.Title)
	assert.NotNil(t, response.Data[0].Metadata.Description)
	assert.NotNil(t, response.Data[0].Metadata.Language)
	assert.NotNil(t, response.Data[0].Metadata.SourceURL)
	assert.NotNil(t, response.Data[0].Metadata.StatusCode)
	assert.Empty(t, response.Data[0].Metadata.Error)
}

func TestMapURLInvalidAPIKey(t *testing.T) {
	invalidApp, err := NewFirecrawlApp("invalid_api_key", API_URL)
	require.NoError(t, err)
	_, err = invalidApp.MapURL("https://www.scrapethissite.com", nil)
	require.Error(t, err)
	assert.Contains(t, err.Error(), "Status code 401")
}

func TestMapURLBlocklistedURL(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)
	blocklistedUrl := "https://facebook.com/fake-test"
	_, err = app.MapURL(blocklistedUrl, nil)
	require.Error(t, err)
	assert.Contains(t, err.Error(), "Status code 403")
}

func TestMapURLValidMap(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	response, err := app.MapURL("https://www.scrapethissite.com", nil)
	require.NoError(t, err)
	assert.NotNil(t, response)
	assert.IsType(t, &MapResponse{}, response)
	assert.Greater(t, len(response.Links), 0)
	assert.Contains(t, response.Links[0], "https://")
	assert.Contains(t, response.Links[0], "scrapethissite.com")
}

func TestMapURLWithSearchParameter(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	_, err = app.Search("https://www.scrapethissite.com", nil)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "Search is not implemented in API version 1.0.0")
}

func TestScrapeURLWithMaxAge(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	// Test with maxAge set to 1 hour (3600000 milliseconds)
	params := &ScrapeParams{
		Formats: []string{"markdown"},
		MaxAge:  ptr(3600000), // 1 hour in milliseconds
	}

	response, err := app.ScrapeURL("https://roastmywebsite.ai", params)
	require.NoError(t, err)
	assert.NotNil(t, response)

	assert.Contains(t, response.Markdown, "_Roast_")
	assert.NotEqual(t, response.Markdown, "")
	assert.NotNil(t, response.Metadata)
}

func TestScrapeURLWithMaxAgeZero(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	// Test with maxAge set to 0 (disable caching)
	params := &ScrapeParams{
		Formats: []string{"markdown"},
		MaxAge:  ptr(0), // Disable caching
	}

	response, err := app.ScrapeURL("https://roastmywebsite.ai", params)
	require.NoError(t, err)
	assert.NotNil(t, response)

	assert.Contains(t, response.Markdown, "_Roast_")
	assert.NotEqual(t, response.Markdown, "")
	assert.NotNil(t, response.Metadata)
}

func TestCrawlURLWithMaxAge(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	// Test crawling with maxAge set to 1 hour (3600000 milliseconds)
	params := &CrawlParams{
		ScrapeOptions: ScrapeParams{
			Formats: []string{"markdown"},
			MaxAge:  ptr(3600000), // 1 hour in milliseconds
		},
		Limit: ptr(5), // Limit to 5 pages for faster test
	}

	response, err := app.CrawlURL("https://roastmywebsite.ai", params, nil)
	require.NoError(t, err)
	assert.NotNil(t, response)

	assert.Greater(t, response.Total, 0)
	assert.Greater(t, response.Completed, 0)
	assert.Greater(t, response.CreditsUsed, 0)
	assert.NotEmpty(t, response.ExpiresAt)
	assert.Equal(t, response.Status, "completed")

	data := response.Data
	assert.IsType(t, []*FirecrawlDocument{}, data)
	assert.Greater(t, len(data), 0)
	assert.Contains(t, data[0].Markdown, "_Roast_")
	assert.NotNil(t, data[0].Metadata)
}

func TestScrapeURLWithJsonOptions(t *testing.T) {
	app, err := NewFirecrawlApp(TEST_API_KEY, API_URL)
	require.NoError(t, err)

	// Test with JsonOptions for LLM extraction
	systemPrompt := "You are a helpful assistant that extracts information from web pages."
	prompt := "Extract the main title and description from this page."

	params := &ScrapeParams{
		Formats: []string{"markdown", "json"},
		JsonOptions: &Jso
... [TRUNCATED]
```

