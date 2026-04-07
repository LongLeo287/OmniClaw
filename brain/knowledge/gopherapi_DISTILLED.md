---
id: gopherapi
type: knowledge
owner: OA_Triage
---
# gopherapi
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
[![CircleCI](https://circleci.com/gh/friendsofgo/gopherapi/tree/master.svg?style=svg)](https://circleci.com/gh/friendsofgo/gopherapi/tree/master)

# Gopher API
The Gopher API, is a evolutive simple CRUD API for formative purpose, we're building it while writing the posts of the [blog](https://blog.friendsofgo.tech).

In this API we've learnt differents, features and patterns in Go:

* Using Gorilla Mux to create an simple API
* Using a SOLID, Hexagonal Architecture
* Testing HTTP handlers
* Integration with CircleCI
* Using Wire to build dependencies [only in v0.3.1](https://github.com/friendsofgo/gopherapi/releases/tag/v0.3.1)
* Using pattern contextkey
* Using instrumenting with Zipkin

## How can I use it?

**Install**

```sh
$ go get -u github.com/friendsofgo/gopherapi/cmd/gopherapi
```

**Usage**
Launch server with predefined data

```sh
$ gopherapi --withData
The gopher server is on tap now: http://localhost:8080
```

If you want to start the server using zipkin you will need use the next option
```sh
$ gopherapi --withTrace
```

If you want start the server using cockroachdb you will need use the next option

```sh
$gopherapi --cockroach
```

## Endpoints

Fetch all gophers

```
GET /gophers
```

Fetch a gopher by ID

```
GET /gophers/{gopher_id}
```

Add a gopher

```
POST /gophers
```

Modify a gopher
```
PUT /gophers/{gopher_id}
```

Remove a gopher
```
DELETE /gophers/{gopher_id}
```

You can import the Postman collection into `api/GopherApi.postman_collection`

## Launch Zipkin

```
docker run -d -p 9411:9411 openzipkin/zipkin
```

## Contributing
If you think that you can improve with new endpoints, and functionallities the API feel free to contribute with this project with fork this repo and send your Pull Request.

## License
MIT License, see [LICENSE](https://github.com/friendsofgo/gopherapi/blob/master/LICENSE)

```

### File: api\GopherApi.postman_collection.json
```json
{
	"info": {
		"_postman_id": "358a0a2e-a86c-47db-926f-e4ebcdc0587d",
		"name": "GopherApi",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "Fetch All Gophers",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:8080/gophers",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8080",
					"path": [
						"gophers"
					]
				}
			},
			"response": []
		},
		{
			"name": "Fetch Gopher by ID",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:8080/gophers/01D3XZ7CN92AKS9HAPSZ4D5DP9",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8080",
					"path": [
						"gophers",
						"01D3XZ7CN92AKS9HAPSZ4D5DP9"
					]
				}
			},
			"response": []
		},
		{
			"name": "Add Gopher",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"name": "Content-Type",
						"value": "application/json",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n\t\"ID\": \"01DCBP0R0MSNZY975ZQF1DCQCH\",\n        \"name\": \"Eustaqio\",\n        \"image\": \"https://storage.googleapis.com/gopherizeme.appspot.com/gophers/f73f25d73c06cc81c482821391a85c4b7dd34ba5.png\",\n        \"age\": 99\n}"
				},
				"url": {
					"raw": "http://localhost:8080/gophers",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8080",
					"path": [
						"gophers"
					]
				}
			},
			"response": []
		},
		{
			"name": "Modify Gopher",
			"request": {
				"method": "PUT",
				"header": [
					{
						"key": "Content-Type",
						"name": "Content-Type",
						"value": "application/json",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n        \"name\": \"Eustaqio\",\n        \"image\": \"https://storage.googleapis.com/gopherizeme.appspot.com/gophers/f73f25d73c06cc81c482821391a85c4b7dd34ba5.png\",\n        \"age\": 99\n}"
				},
				"url": {
					"raw": "http://localhost:8080/gophers/01D3XZ89NFJZ9QT2DHVD462AC2",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8080",
					"path": [
						"gophers",
						"01D3XZ89NFJZ9QT2DHVD462AC2"
					]
				}
			},
			"response": []
		},
		{
			"name": "Delete Gopher",
			"request": {
				"method": "DELETE",
				"header": [
					{
						"key": "Content-Type",
						"name": "Content-Type",
						"value": "application/json",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://localhost:8080/gophers/01D3XZ89NFJZ9QT2DHVD462AC2",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8080",
					"path": [
						"gophers",
						"01D3XZ89NFJZ9QT2DHVD462AC2"
					]
				}
			},
			"response": []
		}
	]
}
```

### File: pkg\gopher.go
```go
package gopher

import (
	"context"
	"time"
)

// Gopher defines the properties of a gopher to be listed
type Gopher struct {
	ID        string     `json:"ID"`
	Name      string     `json:"name,omitempty"`
	Image     string     `json:"image,omitempty"`
	Age       int        `json:"age,omitempty"`
	CreatedAt *time.Time `json:"-"`
	UpdatedAt *time.Time `json:"-"`
}

// New creates a gopher
func New(ID, name, image string, age int) *Gopher {
	return &Gopher{
		ID:    ID,
		Name:  name,
		Image: image,
		Age:   age,
	}
}

//Repository provides access to the gopher storage
type Repository interface {
	// CreateGopher saves a given gopher
	CreateGopher(ctx context.Context, gopher *Gopher) error
	// FetchGophers return all gophers saved in storage
	FetchGophers(ctx context.Context) ([]Gopher, error)
	// DeleteGopher remove gopher with given ID
	DeleteGopher(ctx context.Context, ID string) error
	// UpdateGopher modify gopher with given ID and given new data
	UpdateGopher(ctx context.Context, ID string, gopher Gopher) error
	// FetchGopherByID returns the gopher with given ID
	FetchGopherByID(ctx context.Context, ID string) (*Gopher, error)
}

```

### File: pkg\log\logger.go
```go
package log

import (
	"context"
)

// Logger determine the way to centralize log messages format
type Logger interface {
	// UnexpectedError is a standard error message for unexpected errors
	UnexpectedError(ctx context.Context, err error)
}

```

### File: pkg\log\nooplogger.go
```go
package log

import "context"

type noop struct {
}

// NewNoopLogger ...
func NewNoopLogger() Logger {
	return &noop{}
}

func (l *noop) UnexpectedError(ctx context.Context, err error) {
	// nothing to do here
}

```

### File: pkg\server\context.go
```go
package server

import (
	"context"
)

var (
	contextKeyServerID        = contextKey("id")
	contextKeyXForwardedFor   = contextKey("xForwardedFor")
	contextKeyXForwardedProto = contextKey("xForwardedProto")
	contextKeyEndpoint        = contextKey("endpoint")
	contextKeyClientIP        = contextKey("clientIP")
)

type contextKey string

func (c contextKey) String() string {
	return "server" + string(c)
}

// ID gets the name server from context
func ID(ctx context.Context) (string, bool) {
	id, ok := ctx.Value(contextKeyServerID).(string)
	return id, ok
}

// XForwardedFor gets the http address server from context
func XForwardedFor(ctx context.Context) (string, bool) {
	xForwardedFor, ok := ctx.Value(contextKeyXForwardedFor).(string)
	return xForwardedFor, ok
}

// XForwardedProto gets the http address server from context
func XForwardedProto(ctx context.Context) (string, bool) {
	xForwardedProto, ok := ctx.Value(contextKeyXForwardedProto).(string)
	return xForwardedProto, ok
}

// Endpoint gets the http address server from context
func Endpoint(ctx context.Context) (string, bool) {
	endpoint, ok := ctx.Value(contextKeyEndpoint).(string)
	return endpoint, ok
}

// ClientIP gets the http address server from context
func ClientIP(ctx context.Context) (string, bool) {
	clientIP, ok := ctx.Value(contextKeyClientIP).(string)
	return clientIP, ok
}

```

### File: pkg\server\middleware.go
```go
package server

import (
	"context"
	"fmt"
	"net"
	"net/http"

	"github.com/gorilla/mux"
	"github.com/openzipkin/zipkin-go"
)

type handler struct {
	serverID string
	next     http.Handler
}

func newServerMiddleware(serverID string) func(http.Handler) http.Handler {
	return func(next http.Handler) http.Handler {
		h := &handler{
			serverID: serverID,
			next:     next,
		}
		return h
	}
}

// ServeHTTP implements http.Handler.
func (h handler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	ctx := h.createRequestContext(r)
	h.next.ServeHTTP(w, r.WithContext(ctx))
}

func (h handler) createRequestContext(req *http.Request) context.Context {
	ctx := req.Context()

	var (
		xForwardedFor   = req.Header.Get("X-FORWARDED-FOR")
		xForwardedProto = req.Header.Get("X-FORWARDED-PROTO")
	)

	if xForwardedFor != "" {
		ctx = context.WithValue(ctx, contextKeyXForwardedFor, xForwardedFor)
	}
	if xForwardedProto != "" {
		ctx = context.WithValue(ctx, contextKeyXForwardedProto, xForwardedProto)
	}

	ip, _, _ := net.SplitHostPort(req.RemoteAddr)
	ctx = context.WithValue(ctx, contextKeyClientIP, ip)
	ctx = context.WithValue(ctx, contextKeyEndpoint, req.URL.RequestURI())

	ctx = context.WithValue(ctx, contextKeyServerID, h.serverID)
	zipkinSpanHttpName(ctx, req)
	return ctx
}

func zipkinSpanHttpName(ctx context.Context, req *http.Request) {
	if span := zipkin.SpanFromContext(ctx); span != nil {
		if currentRoute := mux.CurrentRoute(req); currentRoute != nil {
			if routePath, err := currentRoute.GetPathTemplate(); err == nil {
				zipkin.TagHTTPRoute.Set(span, routePath)
				span.SetName(fmt.Sprintf("%s %s", req.Method, routePath))

			}
		}
	}
}

```

### File: pkg\server\server.go
```go
package server

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/openzipkin/zipkin-go"
	zipkinhttp "github.com/openzipkin/zipkin-go/middleware/http"

	"github.com/friendsofgo/gopherapi/pkg/adding"
	"github.com/friendsofgo/gopherapi/pkg/fetching"
	"github.com/friendsofgo/gopherapi/pkg/modifying"
	"github.com/friendsofgo/gopherapi/pkg/removing"

	"github.com/gorilla/mux"
)

// server all server necessary dependencies
type server struct {
	serverID string

	tracer *zipkin.Tracer

	router http.Handler

	fetching  fetching.Service
	adding    adding.Service
	modifying modifying.Service
	removing  removing.Service
}

// Server representation of gopher server
type Server interface {
	Router() http.Handler
	FetchGophers(w http.ResponseWriter, r *http.Request)
	FetchGopher(w http.ResponseWriter, r *http.Request)
	AddGopher(w http.ResponseWriter, r *http.Request)
	ModifyGopher(w http.ResponseWriter, r *http.Request)
	RemoveGopher(w http.ResponseWriter, r *http.Request)
}

// New initialize the server
func New(
	serverID string,
	tracer *zipkin.Tracer,
	fS fetching.Service,
	aS adding.Service,
	mS modifying.Service,
	rS removing.Service,
) Server {
	a := &server{
		serverID:  serverID,
		tracer:    tracer,
		fetching:  fS,
		adding:    aS,
		modifying: mS,
		removing:  rS}
	router(a)

	return a
}

func router(s *server) {
	r := mux.NewRouter()

	r.Use(
		zipkinhttp.NewServerMiddleware(s.tracer),
		newServerMiddleware(s.serverID),
	)

	r.HandleFunc("/gophers", s.FetchGophers).Methods(http.MethodGet)
	r.HandleFunc("/gophers/{ID:[a-zA-Z0-9_]+}", s.FetchGopher).Methods(http.MethodGet)
	r.HandleFunc("/gophers", s.AddGopher).Methods(http.MethodPost)
	r.HandleFunc("/gophers/{ID:[a-zA-Z0-9_]+}", s.ModifyGopher).Methods(http.MethodPut)
	r.HandleFunc("/gophers/{ID:[a-zA-Z0-9_]+}", s.RemoveGopher).Methods(http.MethodDelete)

	s.router = r
}

func (s *server) Router() http.Handler {
	return s.router
}

// FetchGophers return a list of all gophers
func (s *server) FetchGophers(w http.ResponseWriter, r *http.Request) {
	gophers, _ := s.fetching.FetchGophers(r.Context())

	w.Header().Set("Content-Type", "application/json")
	_ = json.NewEncoder(w).Encode(gophers)

}

// FetchGopher return a gopher by ID
func (s *server) FetchGopher(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	gopher := s.fetching.FetchGopherByID(r.Context(), vars["ID"])
	w.Header().Set("Content-Type", "application/json")
	if gopher == nil {
		w.WriteHeader(http.StatusNotFound)
		_ = json.NewEncoder(w).Encode("Gopher Not found")
		return
	}

	_ = json.NewEncoder(w).Encode(gopher)

}

type addGopherRequest struct {
	ID    string `json:"ID"`
	Name  string `json:"name"`
	Image string `json:"image"`
	Age   int    `json:"age"`
}

// AddGopher save a gopher
func (s *server) AddGopher(w http.ResponseWriter, r *http.Request) {
	decoder := json.NewDecoder(r.Body)

	var g addGopherRequest
	err := decoder.Decode(&g)

	w.Header().Set("Content-Type", "application/json")
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		_ = json.NewEncoder(w).Encode("Error unmarshalling request body")
		return
	}
	if err := s.adding.AddGopher(r.Context(), g.ID, g.Name, g.Image, g.Age); err != nil {
		log.Println(err)
		w.WriteHeader(http.StatusInternalServerError)
		_ = json.NewEncoder(w).Encode("Can't create a gopher")
		return
	}

	w.WriteHeader(http.StatusCreated)
}

type modifyGopherRequest struct {
	Name  string `json:"name"`
	Image string `json:"image"`
	Age   int    `json:"age"`
}

// ModifyGopher modify gopher data
func (s *server) ModifyGopher(w http.ResponseWriter, r *http.Request) {
	decoder := json.NewDecoder(r.Body)

	var g addGopherRequest
	err := decoder.Decode(&g)

	w.Header().Set("Content-Type", "application/json")
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		_ = json.NewEncoder(w).Encode("Error unmarshalling request body")
		return
	}
	vars := mux.Vars(r)
	if err := s.modifying.ModifyGopher(r.Context(), vars["ID"], g.Name, g.Image, g.Age); err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		_ = json.NewEncoder(w).Encode("Can't modify a gopher")
		return
	}

	w.WriteHeader(http.StatusNoContent)
}

// RemoveGopher remove a gopher
func (s *server) RemoveGopher(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)

	_ = s.removing.RemoveGopher(r.Context(), vars["ID"])
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusNoContent)

}

```

### File: pkg\server\server_test.go
```go
package server

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/friendsofgo/gopherapi/pkg/log"
	"github.com/friendsofgo/gopherapi/pkg/removing"
	"github.com/friendsofgo/gopherapi/pkg/tracer"

	"github.com/friendsofgo/gopherapi/pkg/adding"
	"github.com/friendsofgo/gopherapi/pkg/fetching"
	"github.com/friendsofgo/gopherapi/pkg/modifying"

	sample "github.com/friendsofgo/gopherapi/cmd/sample-data"
	gopher "github.com/friendsofgo/gopherapi/pkg"
	"github.com/friendsofgo/gopherapi/pkg/storage/inmem"
)

func TestFetchGophers(t *testing.T) {
	req, err := http.NewRequest("GET", "/gophers", nil)
	if err != nil {
		t.Fatalf("could not created request: %v", err)
	}

	s := buildServer()

	rec := httptest.NewRecorder()

	s.FetchGophers(rec, req)

	res := rec.Result()
	defer res.Body.Close()
	if res.StatusCode != http.StatusOK {
		t.Errorf("expected %d, got: %d", http.StatusOK, res.StatusCode)
	}
	b, err := ioutil.ReadAll(res.Body)
	if err != nil {
		t.Fatalf("could not read response: %v", err)
	}

	var got []gopher.Gopher
	err = json.Unmarshal(b, &got)
	if err != nil {
		t.Fatalf("could not unmarshall response %v", err)
	}

	expected := len(sample.Gophers)

	if len(got) != expected {
		t.Errorf("expected %v gophers, got: %v gopher", sample.Gophers, got)
	}
}

func TestFetchGopher(t *testing.T) {

	testData := []struct {
		name   string
		g      *gopher.Gopher
		status int
		err    string
	}{
		{name: "gopher found", g: gopherSample(), status: http.StatusOK},
		{name: "gopher not found", g: &gopher.Gopher{ID: "123"}, status: http.StatusNotFound, err: "Gopher Not found"},
	}

	for _, tt := range testData {
		t.Run(tt.name, func(t *testing.T) {
			uri := fmt.Sprintf("/gophers/%s", tt.g.ID)
			req, err := http.NewRequest("GET", uri, nil)
			if err != nil {
				t.Fatalf("could not created request: %v", err)
			}

			s := buildServer()

			rec := httptest.NewRecorder()
			s.Router().ServeHTTP(rec, req)

			res := rec.Result()

			defer res.Body.Close()
			if tt.status != res.StatusCode {
				t.Errorf("expected %d, got: %d", tt.status, res.StatusCode)
			}
			b, err := ioutil.ReadAll(res.Body)
			if err != nil {
				t.Fatalf("could not read response: %v", err)
			}

			if tt.err == "" {
				var got *gopher.Gopher
				err = json.Unmarshal(b, &got)
				if err != nil {
					t.Fatalf("could not unmarshall response %v", err)
				}

				if *got != *tt.g {
					t.Fatalf("expected %v, got: %v", tt.g, got)
				}
			}
		})
	}

}

func TestAddGopher(t *testing.T) {
	bodyJSON := []byte(`{
        "ID": "01DCBP0R0MSNZY975ZQF1DCQCH",
        "name": "Eustaqio",
        "image": "https://storage.googleapis.com/gopherizeme.appspot.com/gophers/f73f25d73c06cc81c482821391a85c4b7dd34ba5.png",
        "age": 99
    }`)
	req, err := http.NewRequest("POST", "/gophers", bytes.NewBuffer(bodyJSON))
	if err != nil {
		t.Fatalf("could not created request: %v", err)
	}
	s := buildServer()
	rec := httptest.NewRecorder()

	s.AddGopher(rec, req)
	res := rec.Result()
	defer res.Body.Close()

	if res.StatusCode != http.StatusCreated {
		t.Errorf("expected %d, got: %d", http.StatusCreated, res.StatusCode)
	}
}

func TestModifyGopher(t *testing.T) {
	bodyJSON := []byte(`{
        "name": "Eustaqio",
        "image": "https://storage.googleapis.com/gopherizeme.appspot.com/gophers/f73f25d73c06cc81c482821391a85c4b7dd34ba5.png",
        "age": 99
    }`)
	req, err := http.NewRequest("PUT", "/gophers/01D3XZ89NFJZ9QT2DHVD462AC2", bytes.NewBuffer(bodyJSON))
	if err != nil {
		t.Fatalf("could not created request: %v", err)
	}
	s := buildServer()
	rec := httptest.NewRecorder()

	s.ModifyGopher(rec, req)
	res := rec.Result()
	defer res.Body.Close()

	if res.StatusCode != http.StatusNoContent {
		t.Errorf("expected %d, got: %d", http.StatusNoContent, res.StatusCode)
	}
}

func TestRemoveGopher(t *testing.T) {

	uri := fmt.Sprintf("/gophers/%s", "01D3XZ89NFJZ9QT2DHVD462AC2")
	req, err := http.NewRequest("DELETE", uri, nil)
	if err != nil {
		t.Fatalf("could not created request: %v", err)
	}

	s := buildServer()

	rec := httptest.NewRecorder()
	s.Router().ServeHTTP(rec, req)

	res := rec.Result()

	defer res.Body.Close()
	if http.StatusNoContent != res.StatusCode {
		t.Errorf("expected %d, got: %d", http.StatusNoContent, res.StatusCode)
	}

}

func gopherSample() *gopher.Gopher {
	return &gopher.Gopher{
		ID:    "01D3XZ3ZHCP3KG9VT4FGAD8KDR",
		Name:  "Jenny",
		Age:   18,
		Image: "https://storage.googleapis.com/gopherizeme.appspot.com/gophers/0ceb2c10fc0c30575c18ff1defa1ffd41501bc62.png",
	}
}

func buildServer() Server {

	noopTracer := tracer.NewNoopTracer()
	repo := inmem.NewRepository(sample.Gophers, tracer.NewNoopTracer())
	fS := fetching.NewService(repo, log.NewNoopLogger())
	aS := adding.NewService(repo)
	mS := modifying.NewService(repo)
	rS := removing.NewService(repo)

	return New("test", noopTracer, fS, aS, mS, rS)
}

```

### File: pkg\storage\redis\conn.go
```go
package redis

import (
	"github.com/gomodule/redigo/redis"
	"time"
)

func NewConn(addr string) *redis.Pool {
	return &redis.Pool{
		MaxIdle:     3,
		IdleTimeout: 240 * time.Second,
		Dial:        func() (redis.Conn, error) { return redis.Dial("tcp", addr) },
	}
}

```

### File: pkg\storage\redis\example_test.go
```go
package redis

import (
	"context"
	"github.com/alicebob/miniredis/v2"
	gopher "github.com/friendsofgo/gopherapi/pkg"
	"github.com/stretchr/testify/assert"
	"testing"
)

func Test_GopherRepository_Example(t *testing.T) {
	// GIVEN a miniredis instance and a Redis implementation of result.Repository
	s, err := miniredis.Run()
	if err != nil {
		panic(err)
	}
	defer s.Close()

	repo := NewRepository(NewConn(s.Addr()))

	// WHEN two gophers are created
	gopherA, gopherB := buildGopher("123ABC"), buildGopher("ABC123")

	err = repo.CreateGopher(context.Background(), &gopherA)
	assert.NoError(t, err)

	err = repo.CreateGopher(context.Background(), &gopherB)
	assert.NoError(t, err)

	// THEN they can be fetched by ID
	result, err := repo.FetchGopherByID(context.Background(), gopherA.ID)
	assert.NoError(t, err)
	assert.Equal(t, gopherA, *result)

	result, err = repo.FetchGopherByID(context.Background(), gopherB.ID)
	assert.NoError(t, err)
	assert.Equal(t, gopherB, *result)

	// AND they can be fetched in batch
	results, err := repo.FetchGophers(context.Background())
	assert.NoError(t, err)
	assert.Equal(t, []gopher.Gopher{gopherA, gopherB}, results)
}

```

### File: pkg\storage\redis\repository.go
```go
package redis

import (
	"context"
	"encoding/json"
	"errors"
	gopherapi "github.com/friendsofgo/gopherapi/pkg"
	"github.com/gomodule/redigo/redis"
	_ "github.com/lib/pq"
)

const (
	onlyIfExists = "XX"
)

type gopherRepository struct {
	pool *redis.Pool
}

// NewRepository instances a Redis implementation of the gopherapi.Repository
func NewRepository(pool *redis.Pool) gopherapi.Repository {
	return gopherRepository{
		pool: pool,
	}
}

// CreateGopher satisfies the gopherapi.Repository interface
func (r gopherRepository) CreateGopher(ctx context.Context, gopher *gopherapi.Gopher) error {
	bytes, err := json.Marshal(gopher)
	if err != nil {
		return err
	}

	conn, err := r.pool.GetContext(ctx)
	if err != nil {
		return err
	}

	_, err = conn.Do("SET", gopher.ID, string(bytes))
	return err
}

func (r gopherRepository) FetchGophers(ctx context.Context) ([]gopherapi.Gopher, error) {
	conn, err := r.pool.GetContext(ctx)
	if err != nil {
		return nil, err
	}

	keys, err := redis.Strings(conn.Do("KEYS", "*"))
	if err != nil {
		return nil, err
	}

	if len(keys) == 0 {
		return []gopherapi.Gopher{}, nil
	}

	args := make([]interface{}, 0, len(keys))
	for _, key := range keys {
		args = append(args, key)
	}

	results, err := redis.Strings(conn.Do("MGET", args...))
	if err != nil {
		return nil, err
	}

	gophers := make([]gopherapi.Gopher, 0, len(results))
	for _, result := range results {
		gopher := gopherapi.Gopher{}

		err := json.Unmarshal([]byte(result), &gopher)
		if err != nil {
			return nil, err
		}

		gophers = append(gophers, gopher)
	}
	return gophers, nil
}

func (r gopherRepository) DeleteGopher(ctx context.Context, ID string) error {
	conn, err := r.pool.GetContext(ctx)
	if err != nil {
		return err
	}

	_, err = conn.Do("DEL", ID)
	return err
}

func (r gopherRepository) UpdateGopher(ctx context.Context, ID string, gopher gopherapi.Gopher) error {
	bytes, err := json.Marshal(gopher)
	if err != nil {
		return err
	}

	conn, err := r.pool.GetContext(ctx)
	if err != nil {
		return err
	}

	result, err := conn.Do("SET", ID, string(bytes), onlyIfExists)
	if result == nil {
		return errors.New("not found")
	}
	return err
}

func (r gopherRepository) FetchGopherByID(ctx context.Context, ID string) (*gopherapi.Gopher, error) {
	conn, err := r.pool.GetContext(ctx)
	if err != nil {
		return nil, err
	}

	result, err := redis.String(conn.Do("GET", ID))
	if err != nil {
		return nil, err
	}

	if result == "" {
		return nil, errors.New("not found")
	}

	gopher := &gopherapi.Gopher{}
	err = json.Unmarshal([]byte(result), gopher)

	return gopher, err
}

```

### File: pkg\storage\redis\repository_test.go
```go
package redis

import (
	"context"
	"encoding/json"
	"errors"
	gopherapi "github.com/friendsofgo/gopherapi/pkg"
	"github.com/gomodule/redigo/redis"
	_ "github.com/lib/pq"
	"github.com/rafaeljusto/redigomock"
	"github.com/stretchr/testify/assert"
	"testing"
	"time"
)

func Test_GopherRepository_CreateGopher_RepositoryError(t *testing.T) {
	gopher := buildGopher("123ABC")

	conn := redigomock.NewConn()
	conn.Command("SET", gopher.ID, gopherToJSONString(gopher)).ExpectError(errors.New("something failed"))

	repo := NewRepository(wrapRedisConn(conn))
	err := repo.CreateGopher(context.Background(), &gopher)

	assert.Error(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
}

func Test_GopherRepository_CreateGopher_Success(t *testing.T) {
	gopher := buildGopher("123ABC")

	conn := redigomock.NewConn()
	conn.Command("SET", gopher.ID, gopherToJSONString(gopher)).Expect("OK")

	repo := NewRepository(wrapRedisConn(conn))
	err := repo.CreateGopher(context.Background(), &gopher)

	assert.NoError(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
}

func Test_GopherRepository_FetchGophers_RepositoryError(t *testing.T) {
	conn := redigomock.NewConn()
	conn.Command("KEYS", "*").ExpectError(errors.New("something failed"))

	repo := NewRepository(wrapRedisConn(conn))
	_, err := repo.FetchGophers(context.Background())

	assert.Error(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
}

func Test_GopherRepository_FetchGophers_NoRows(t *testing.T) {
	conn := redigomock.NewConn()
	conn.Command("KEYS", "*").Expect([]interface{}{})

	repo := NewRepository(wrapRedisConn(conn))
	gophers, err := repo.FetchGophers(context.Background())

	assert.NoError(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
	assert.Len(t, gophers, 0)
}

func Test_GopherRepository_FetchGophers_RowWithInvalidData(t *testing.T) {
	conn := redigomock.NewConn()
	conn.Command("KEYS", "*").Expect([]interface{}{"123", "456"})
	conn.Command("MGET", "123", "456").Expect([]interface{}{"invalid-data"})

	repo := NewRepository(wrapRedisConn(conn))
	_, err := repo.FetchGophers(context.Background())

	assert.Error(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
}

func Test_GopherRepository_FetchGophers_Succeeded(t *testing.T) {
	gopherA, gopherB := buildGopher("123ABC"), buildGopher("ABC123")
	expectedGophers := []gopherapi.Gopher{gopherA, gopherB}

	conn := redigomock.NewConn()
	conn.Command("KEYS", "*").Expect([]interface{}{gopherA.ID, gopherB.ID})
	conn.Command("MGET", gopherA.ID, gopherB.ID).Expect(
		[]interface{}{gopherToJSONString(gopherA), gopherToJSONString(gopherB)},
	)

	repo := NewRepository(wrapRedisConn(conn))
	gophers, err := repo.FetchGophers(context.Background())

	assert.NoError(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
	assert.Equal(t, expectedGophers, gophers)
}

func Test_GopherRepository_DeleteGopher_RepositoryError(t *testing.T) {
	gopherID := "123ABC"

	conn := redigomock.NewConn()
	conn.Command("DEL", gopherID).ExpectError(errors.New("something failed"))

	repo := NewRepository(wrapRedisConn(conn))
	err := repo.DeleteGopher(context.Background(), gopherID)

	assert.Error(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
}

func Test_GopherRepository_DeleteGopher_Success(t *testing.T) {
	gopherID := "123ABC"

	conn := redigomock.NewConn()
	conn.Command("DEL", gopherID).Expect(1)

	repo := NewRepository(wrapRedisConn(conn))
	err := repo.DeleteGopher(context.Background(), gopherID)

	assert.NoError(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
}

func Test_GopherRepository_UpdateGopher_RepositoryError(t *testing.T) {
	gopher := buildGopher("123ABC")

	conn := redigomock.NewConn()
	conn.Command("SET", gopher.ID, gopherToJSONString(gopher), "XX").ExpectError(errors.New("something failed"))

	repo := NewRepository(wrapRedisConn(conn))
	err := repo.UpdateGopher(context.Background(), gopher.ID, gopher)

	assert.Error(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
}

func Test_GopherRepository_UpdateGopher_NotFound(t *testing.T) {
	gopher := buildGopher("123ABC")

	conn := redigomock.NewConn()
	conn.Command("SET", gopher.ID, gopherToJSONString(gopher), "XX").Expect(nil)

	repo := NewRepository(wrapRedisConn(conn))
	err := repo.UpdateGopher(context.Background(), gopher.ID, gopher)

	assert.Error(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
}

func Test_GopherRepository_UpdateGopher_Success(t *testing.T) {
	gopher := buildGopher("123ABC")

	conn := redigomock.NewConn()
	conn.Command("SET", gopher.ID, gopherToJSONString(gopher), "XX").Expect("OK")

	repo := NewRepository(wrapRedisConn(conn))
	err := repo.UpdateGopher(context.Background(), gopher.ID, gopher)

	assert.NoError(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
}

func Test_GopherRepository_FetchGopherByID_RepositoryError(t *testing.T) {
	gopherID := "123ABC"

	conn := redigomock.NewConn()
	conn.Command("GET", gopherID).ExpectError(errors.New("something failed"))

	repo := NewRepository(wrapRedisConn(conn))
	_, err := repo.FetchGopherByID(context.Background(), gopherID)

	assert.Error(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
}

func Test_GopherRepository_FetchGopherByID_NoRows(t *testing.T) {
	gopherID := "123ABC"

	conn := redigomock.NewConn()
	conn.Command("GET", gopherID).Expect(nil)

	repo := NewRepository(wrapRedisConn(conn))
	_, err := repo.FetchGopherByID(context.Background(), gopherID)

	assert.Error(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
}

func Test_GopherRepository_FetchGopherByID_RowWithInvalidData(t *testing.T) {
	gopherID := "123ABC"

	conn := redigomock.NewConn()
	conn.Command("GET", gopherID).Expect("invalid-data")

	repo := NewRepository(wrapRedisConn(conn))
	_, err := repo.FetchGopherByID(context.Background(), gopherID)

	assert.Error(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
}

func Test_GopherRepository_FetchGopherByID_Succeeded(t *testing.T) {
	gopherID := "123ABC"
	expectedGopher := buildGopher(gopherID)

	conn := redigomock.NewConn()
	conn.Command("GET", gopherID).Expect(gopherToJSONString(expectedGopher))

	repo := NewRepository(wrapRedisConn(conn))
	gopher, err := repo.FetchGopherByID(context.Background(), gopherID)

	assert.NoError(t, err)
	assert.NoError(t, conn.ExpectationsWereMet())
	assert.Equal(t, &expectedGopher, gopher)
}

func buildGopher(ID string) gopherapi.Gopher {
	return gopherapi.Gopher{
		ID:    ID,
		Name:  "The Saviour",
		Image: "https://via.placeholder.com/150.png",
		Age:   8,
	}
}

func gopherToJSONString(gopher gopherapi.Gopher) string {
	bytes, _ := json.Marshal(&gopher)
	return string(bytes)
}

func wrapRedisConn(conn redis.Conn) *redis.Pool {
	return &redis.Pool{
		MaxIdle:     3,
		IdleTimeout: 240 * time.Second,
		Dial:        func() (redis.Conn, error) { return conn, nil },
	}
}

```

