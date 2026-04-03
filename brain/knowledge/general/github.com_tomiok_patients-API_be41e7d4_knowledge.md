---
id: github.com-tomiok-patients-api-be41e7d4-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:28.549737
---

# KNOWLEDGE EXTRACT: github.com_tomiok_patients-API_be41e7d4
> **Extracted on:** 2026-04-01 12:58:48
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522177/github.com_tomiok_patients-API_be41e7d4

---

## File: `.gitignore`
```
db/data
.idea
```

## File: `Dockerfile`
```
FROM golang

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN make build

CMD ./patients-api
EXPOSE 8080
```

## File: `Makefile`
```
# cross parameters
SHELL:=/bin/bash -O extglob
BINARY=patients-api
VERSION=0.1.0

LDFLAGS=-ldflags "-X main.Version=${VERSION}"

# Build step, generates the binary.
build:
	go build ${LDFLAGS} -o ${BINARY} cmd/main.go

# Web is a mask to run the web interface, in our case the main function will start the http server.
web:
	@clear
	@go run cmd/main.go

# Run go formatter
fmt:
	@gofmt -w .

# Download the go lint. Not running anything.
lint-prepare:
	@echo "Installing golangci-lint"
	curl -sfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh| sh -s latest

# Run the lint across all the project. See more options https://raw.githubusercontent.com/golangci/golangci-lint .
lint:
	./bin/golangci-lint run \
		--exclude-use-default=false \
		--enable=golint \
		--enable=gocyclo \
		--enable=goconst \
		--enable=unconvert \
		./...

# Run the test for all the directories.
test:
	@clear
	@go test -v ./...

###################
# Docker commands #
###################
up:
	docker-compose up

down:
	docker-compose down --remove-orphans

clean:
	sudo rm -rf db/data
```

## File: `README.md`
```markdown
# Backend - Patients
This is a PoC for a patients API

### API endpoints


| Method | URL                             | Description                       |
|--------|---------------------------------|-----------------------------------|
| GET    | /api/v1/patients                | Get all patients                  |
| GET    | /api/v1/patients/:id            | Get one patient                   |
| POST   | /api/v1/patients                | Add one patient                   |

```

## File: `docker-compose.yml`
```yaml
version: "3.3"
services:
  db:
    image: "postgres:10.5"
    restart:
      unless-stopped
    ports:
      - "5432:5432"
    volumes:
      - ./db/data:/var/lib/postgresql/data
      - ./db/schema.sql:/docker-entrypoint-initdb.d/schema.sql
    environment:
      POSTGRES_PASSWORD: "postgres"
      POSTGRES_DB: "project"
    networks: # Networks to join
      - local
    tty:
      true
  app:
    depends_on:
      - db
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8080:8080" # Forward the exposed port 8080 on the container to port 8080 on the host machine
    restart:
      unless-stopped
    links:
      - "db"
    networks: # Networks to join
      - local
    tty:
      true
networks:
  local:
    driver: bridge
```

## File: `go.mod`
```
module github.com/tomiok/patients-API

go 1.13

require (
	github.com/go-chi/chi v4.1.0+incompatible
	github.com/lib/pq v1.3.0
)
```

## File: `go.sum`
```
github.com/go-chi/chi v4.1.0+incompatible h1:ETj3cggsVIY2Xao5ExCu6YhEh5MD6JTfcBzS37R260w=
github.com/go-chi/chi v4.1.0+incompatible/go.mod h1:eB3wogJHnLi3x/kFX2A+IbTBlXxmMeXJVKy9tTv1XzQ=
github.com/lib/pq v1.3.0 h1:/qkRGz8zljWiDcFvgpwUpwIAPu3r07TDvs3Rws+o/pU=
github.com/lib/pq v1.3.0/go.mod h1:5WUZQaWbwv1U+lTReE5YruASi9Al49XbQIvNi/34Woo=
```

## File: `api/api.go`
```go
package api

import (
	"github.com/tomiok/patients-API/internal/storage"
	patients "github.com/tomiok/patients-API/patients/web"
)

func Start(port string) {
	db := storage.ConnectToDB()
	defer db.Close()

	r := routes(patients.NewPatientHTTPService(db))
	server := newServer(port, r)

	server.Start()
}
```

## File: `api/routes.go`
```go
package api

import (
	"github.com/go-chi/chi"
	"github.com/tomiok/patients-API/patients/web"
)

func routes(services *patients.PatientHTTPService) *chi.Mux {
	r := chi.NewMux()

	r.Get("/patients", services.GetPatientsHandler)
	r.Post("/patients", services.CreatePatientsHandler)
	r.Get("/patients/{patientID}", services.GetPatientsByIDHandler)

	return r
}
```

## File: `api/server.go`
```go
package api

import (
	"context"
	"github.com/go-chi/chi"
	"log"
	"net/http"
	"os"
	"os/signal"
	"time"
)

type server struct {
	*http.Server
}

func newServer(listening string, mux *chi.Mux) *server {
	s := &http.Server{
		Addr:         ":" + listening,
		Handler:      mux,
		ReadTimeout:  5 * time.Second,
		WriteTimeout: 10 * time.Second,
		IdleTimeout:  15 * time.Second,
	}

	return &server{s}
}

// Start runs ListenAndServe on the http.Server with graceful shutdown
func (srv *server) Start() {
	log.Println("starting API cmd")

	go func() {
		if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			log.Fatalf("could not listen on %s due to %s", srv.Addr, err.Error())
		}
	}()
	log.Printf("cmd is ready to handle requests %s", srv.Addr)
	srv.gracefulShutdown()
}

func (srv *server) gracefulShutdown() {
	quit := make(chan os.Signal, 1)

	signal.Notify(quit, os.Interrupt)
	sig := <-quit
	log.Printf("cmd is shutting down %s", sig.String())

	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
	defer cancel()

	srv.SetKeepAlivesEnabled(false)
	if err := srv.Shutdown(ctx); err != nil {
		log.Fatalf("could not gracefully shutdown the cmd %s", err.Error())
	}
	log.Printf("cmd stopped")
}
```

## File: `cmd/main.go`
```go
package main

import (
	"log"
	"os"

	"github.com/tomiok/patients-API/api"
)

const defaultPort = "8080"

func main() {
	log.Println("stating API cmd")
	port := os.Getenv("PORT")

	if port == "" {
		port = defaultPort
	}
	api.Start(port)
	//	other.Start(param)
}
```

## File: `cmd/video_annotations.go`
```go
package main

func annotations() {

	/*
		package cmd: entrypoint - package main and function main
		package internal: cannot import an internal package

	*/

}
```

## File: `db/schema.sql`
```sql
CREATE TABLE IF NOT EXISTS patient (
    id serial PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    address text NOT NULL,
    phone text NOT NULL,
    email text NOT NULL,
    created_at timestamptz DEFAULT NOW(),
    CONSTRAINT unique_patient_name UNIQUE(first_name, last_name)
);

CREATE TABLE IF NOT EXISTS physician (
    id serial PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    created_at timestamptz DEFAULT NOW(),
    CONSTRAINT unique_physician_name UNIQUE(first_name, last_name)
);

CREATE TABLE IF NOT EXISTS visit (
    id serial PRIMARY KEY,
    patient_id integer NOT NULL REFERENCES patient(id),
    physician_id integer NOT NULL REFERENCES physician(id),
    visited_at timestamptz DEFAULT NOW(),
    location text NOT NULL,
    reason text NOT NULL
);

```

## File: `internal/storage/storage.go`
```go
package storage

import (
	"database/sql"
	"fmt"
	_ "github.com/lib/pq"
	"log"
	"os"
)

func ConnectToDB() *sql.DB {
	server := os.Getenv("GCP_HOSTNAME")
	if server == "" {
		server = "localhost"
	}
	connURL := fmt.Sprintf("postgres://postgres:postgres@%s/project?sslmode=disable", server)
	db, err := sql.Open("postgres", connURL)
	if err != nil {
		log.Fatalf("Failed to connect to DB via %s: %v", connURL, err)
	}
	if err = db.Ping(); err != nil {
		log.Fatalf("Failed to ping DB via %s: %v", connURL, err)
	}
	log.Println("Connected to DB")
	return db
}
```

## File: `internal/web/api_response.go`
```go
package web

import (
	"encoding/json"
	"net/http"
)

type ResponseAPI struct {
	Success bool        `json:"success"`
	Status  int         `json:"status,omitempty"`
	Result  interface{} `json:"result,omitempty"`
}

func Success(result interface{}, status int) *ResponseAPI {
	return &ResponseAPI{
		Success: true,
		Status:  status,
		Result:  result,
	}
}
func (r *ResponseAPI) Send(w http.ResponseWriter) error {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(r.Status)
	return json.NewEncoder(w).Encode(r)
}
```

## File: `internal/web/errors.go`
```go
package web

import (
	"encoding/json"
	"net/http"
)

var (
	ErrBadRequest  = GameError{StatusCode: http.StatusBadRequest, Type: "api_error", Message: "Cannot process current request"}
	ErrInvalidJSON = GameError{StatusCode: http.StatusBadRequest, Type: "invalid_json", Message: "Invalid or malformed JSON"}
)

type GameError struct {
	StatusCode int    `json:"-"`
	Type       string `json:"type"`
	Message    string `json:"message,omitempty"`
}

func (e GameError) Send(w http.ResponseWriter) error {
	statusCode := e.StatusCode
	if statusCode == 0 {
		statusCode = http.StatusBadRequest
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(statusCode)
	return json.NewEncoder(w).Encode(e)
}
```

## File: `patients/gateway/patient_create_gateway.go`
```go
package patients

import (
	"database/sql"
	"github.com/tomiok/patients-API/patients/models"
)

type PatientGateway interface {
	CreatePatient(p *patients.CreatePatientCMD) (*patients.Patient, error)
	GetPatients() []*patients.Patient
	GetPatientByID(id int64) (*patients.Patient, error)
}
type CreatePatientInDB struct {
	PatientStorage
}

func (c *CreatePatientInDB) CreatePatient(p *patients.CreatePatientCMD) (*patients.Patient, error) {
	return c.createPatientDB(p)
}

func (c *CreatePatientInDB) GetPatients() []*patients.Patient {
	return c.getPatientsDB()
}

func (c *CreatePatientInDB) GetPatientByID(id int64) (*patients.Patient, error) {
	return c.getPatientByIDBD(id)
}

func NewPatientGateway(db *sql.DB) PatientGateway {
	return &CreatePatientInDB{NewPatientStorageGateway(db)}
}
```

## File: `patients/gateway/storage.go`
```go
package patients

import (
	"database/sql"
	"github.com/tomiok/patients-API/patients/models"
	"log"
	"time"
)

type PatientStorage interface {
	createPatientDB(p *patients.CreatePatientCMD) (*patients.Patient, error)
	getPatientsDB() []*patients.Patient
	getPatientByIDBD(id int64) (*patients.Patient, error)
}

type PatientService struct {
	db *sql.DB
}

func NewPatientStorageGateway(db *sql.DB) PatientStorage {
	return &PatientService{db: db}
}

func (s *PatientService) createPatientDB(p *patients.CreatePatientCMD) (*patients.Patient, error) {
	log.Println("creating a new patient")
	res, err := s.db.Exec("insert into patient (first_name, last_name, address, phone, email) values (?,?,?,?,?)",
		p.FirstName, p.LastName, p.Address, p.Phone, p.Email)

	if err != nil {
		log.Printf("cannot save the patient, %s", err.Error())
		return nil, err
	}

	id, err := res.LastInsertId()

	return &patients.Patient{
		ID:        id,
		FirstName: p.FirstName,
		LastName:  p.LastName,
		Address:   p.Address,
		Phone:     p.Phone,
		Email:     p.Email,
		CreatedAt: time.Now(),
	}, nil
}

func (s *PatientService) getPatientsDB() []*patients.Patient {
	rows, err := s.db.Query("select id, first_name, last_name, address, phone, email, created_at from patient")

	if err != nil {
		log.Printf("cannot execute select query: %s", err.Error())
		return nil
	}
	defer rows.Close()
	var p []*patients.Patient
	for rows.Next() {
		var patient patients.Patient
		err := rows.Scan(&patient.ID, &patient.FirstName, &patient.LastName, &patient.Address, &patient.Phone,
			&patient.Email, &patient.CreatedAt)
		if err != nil {
			log.Println("cannot read current row")
			return nil
		}
		p = append(p, &patient)
	}

	return p
}

func (s *PatientService) getPatientByIDBD(id int64) (*patients.Patient, error) {
	var patient patients.Patient
	err := s.db.QueryRow(`select id, first_name, last_name, address, phone, email, created_at from patient
		where id = ?`, id).Scan(&patient.ID, &patient.FirstName, &patient.LastName, &patient.Address, &patient.Phone,
		&patient.Email, &patient.CreatedAt)

	if err != nil {
		log.Printf("cannot fetch patient")
		return nil, err
	}

	return &patient, nil
}
```

## File: `patients/models/patients.go`
```go
package patients

import "time"

type Patient struct {
	ID        int64     `json:"id"`
	FirstName string    `json:"first_name"`
	LastName  string    `json:"last_name"`
	Address   string    `json:"address"`
	Phone     string    `json:"phone"`
	Email     string    `json:"email"`
	CreatedAt time.Time `json:"created_at"`
}

type CreatePatientCMD struct {
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
	Address   string `json:"address"`
	Phone     string `json:"phone"`
	Email     string `json:"email"`
}
```

## File: `patients/web/patients_handler.go`
```go
package patients

import (
	"database/sql"
	"encoding/json"
	"github.com/go-chi/chi"
	"github.com/tomiok/patients-API/internal/web"
	patients "github.com/tomiok/patients-API/patients/gateway"
	models "github.com/tomiok/patients-API/patients/models"
	"log"
	"net/http"
	"strconv"
)

type PatientHTTPService struct {
	gtw patients.PatientGateway
}

func NewPatientHTTPService(db *sql.DB) *PatientHTTPService {
	return &PatientHTTPService{
		patients.NewPatientGateway(db),
	}
}

func (s *PatientHTTPService) GetPatientsHandler(w http.ResponseWriter, r *http.Request) {
	p := s.gtw.GetPatients()
	if p == nil || len(p) == 0 {
		p = []*models.Patient{}
	}
	web.Success(&p, http.StatusOK).Send(w)
}

func (s *PatientHTTPService) GetPatientsByIDHandler(w http.ResponseWriter, r *http.Request) {
	patientID := chi.URLParam(r, "patientID")
	id, _ := strconv.ParseInt(patientID, 10, 64)
	patient, err := s.gtw.GetPatientByID(id)

	if err != nil {
		web.ErrBadRequest.Send(w)
		return
	}

	web.Success(&patient, http.StatusOK).Send(w)
}

func (s *PatientHTTPService) CreatePatientsHandler(w http.ResponseWriter, r *http.Request) {
	body := r.Body
	defer body.Close()
	var cmd models.CreatePatientCMD
	err := json.NewDecoder(body).Decode(&cmd)

	if err != nil {
		web.ErrInvalidJSON.Send(w)
		return
	}

	patient, err := s.gtw.CreatePatient(&cmd)

	if err != nil {
		web.ErrBadRequest.Send(w)
		return
	}

	log.Println(patient)
	web.Success(&patient, http.StatusOK).Send(w)
}
```

